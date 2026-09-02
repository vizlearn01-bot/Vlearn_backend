"""
VLearn CBC Grade 9 CRE — Topic 9: Jesus' Ministry in Jerusalem
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 9: Jesus' Ministry in Jerusalem (Order: 9)

8 Discrete Units / Published Lessons:
  1. The Triumphant Entry into Jerusalem (Luke 19:28-40, Zechariah 9:9)
  2. Jesus Weeps and Cleanses the Temple (Luke 19:41-48, Isaiah 56:7, Jeremiah 7:11)
  3. Conflict Over Jesus' Authority and the Parable of the Tenants (Luke 20:1-19, Psalm 118:22)
  4. Paying Taxes to Caesar (Luke 20:20-26, Romans 13:1-7)
  5. The Question of the Resurrection (Luke 20:27-40, Exodus 3:6)
  6. Scribes' Hypocrisy and the Widow's Two Copper Coins (Luke 20:45-47, Luke 21:1-4)
  7. Teachings on Eschatology and Signs of the End Times (Luke 21:5-28)
  8. The Parable of the Fig Tree and Watchfulness (Luke 21:29-38, 1 Thessalonians 5:1-6)

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
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|MAP|DIAGRAM|COMPARISON|TIMELINE)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE TRIUMPHANT ENTRY: KING OF PEACE VS. MILITARY CONQUEROR</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Analyzing Prophetic Messianic Royalty (Zechariah 9:9 &amp; Luke 19:28-40)</text>

  <!-- Left: Roman / Earthly Monarch -->
  <g transform="translate(40, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="#dc2626"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">EARTHLY / ROMAN CONQUEROR</text>

    <text x="15" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mount of War: Armored Stallion</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">War horses symbolized military conquest,</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">brute violence, and armed domination.</text>

    <text x="15" y="124" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Royal Retinue: Armed Soldiers</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Guarded by spears, swords, and legions</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">instilling terror and subjugation in subjects.</text>

    <text x="15" y="186" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Motive: Political Power &amp; Tribute</text>
    <text x="15" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Demanding taxation, forced allegiance, and</text>
    <text x="15" y="218" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">earthly glorification of the imperial Caesar.</text>

    <rect x="15" y="245" width="300" height="32" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="165" y="265" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Rule by Coercion, Fear &amp; Pride</text>
  </g>

  <!-- Center Icon / Divider -->
  <g transform="translate(378, 220)">
    <circle cx="22" cy="20" r="18" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="22" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VS</text>
  </g>

  <!-- Right: Jesus Christ - King of Peace -->
  <g transform="translate(430, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#blueGrad1)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">JESUS: THE PRINCE OF PEACE</text>

    <text x="15" y="62" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mount of Peace: Unridden Donkey Colt</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Fulfills Zechariah 9:9: gentle, peaceful, and</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">consecrated for sacred divine mission.</text>

    <text x="15" y="124" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Royal Retinue: Praising Disciples &amp; Crowds</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Spreading cloaks and waving palm branches,</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">singing: "Blessed is the King who comes!"</text>

    <text x="15" y="186" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Cosmic Praise: Stones Will Cry Out</text>
    <text x="15" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">If human praise is silenced by Pharisees,</text>
    <text x="15" y="218" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">creation itself will declare His glory.</text>

    <rect x="15" y="245" width="300" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="165" y="265" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Rule by Self-Giving Love &amp; Humility</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">THEOLOGICAL TRUTH: TRUE MESSIANIC KINGSHIP IS ROOTED IN HUMILITY, SACRIFICE, AND UNIVERSAL PEACE</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="amberGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="emeraldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">CLEANSING THE TEMPLE: HOUSE OF PRAYER VS. DEN OF THIEVES</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Deconstructing Jesus' Righteous Anger &amp; Prophetic Judgment (Luke 19:41-48)</text>

  <!-- Left: Corruption in the Court of Gentiles -->
  <g transform="translate(40, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#amberGrad2)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE PERVERSION: "DEN OF THIEVES"</text>

    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Commercialized Worship</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Court of Gentiles turned into an overcrowded, noisy</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">cattle bazaar and extortionate money-exchange hub.</text>

    <text x="15" y="118" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Exploitation of Poor Pilgrims</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Traders charged exorbitant exchange fees to convert</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Roman coins into required Tyrian temple shekels.</text>

    <text x="15" y="176" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• False Spiritual Security (Jeremiah 7:11)</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Religious elites treated the Temple as a safe cave</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">to hide in after committing weekly economic crimes.</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="165" y="253" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Defilement of Sacred International Space</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Barred Gentiles from quiet worship and prayer</text>
  </g>

  <!-- Right: Divine Restoration of Sacred Worship -->
  <g transform="translate(430, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#emeraldGrad2)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE RESTORATION: "HOUSE OF PRAYER"</text>

    <text x="15" y="60" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Righteous Anger in Action</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus overturns money tables and drives out sellers</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">with holy zeal for God's holiness and justice.</text>

    <text x="15" y="118" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Universal Access for Nations (Isaiah 56:7)</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Reclaims the outer court so seekers from all tribes</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and nations can pray in serene holiness.</text>

    <text x="15" y="176" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Heart as the New Living Temple</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Believers' bodies and assembly are sanctuaries of</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">the Holy Spirit demanding moral purity (1 Cor 6:19).</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="165" y="253" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Restoration of Reverence, Purity &amp; Truth</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Jesus daily taught crowds who hung on His words</text>
  </g>

  <!-- Central Dynamic Arrow -->
  <g transform="translate(382, 220)">
    <path d="M 0 10 L 25 10 L 25 3 L 36 15 L 25 27 L 25 20 L 0 20 Z" fill="#38bdf8"/>
    <text x="18" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">ZEAL</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">PROPHETIC LESSON: SACRED PLACES AND HUMAN HEARTS MUST BE FREE FROM GREED AND CORRUPTION</text>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="purpleGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE PARABLE OF THE TENANTS &amp; THE CORNERSTONE</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Mapping Allegorical Figures to Salvation History (Luke 20:1-19 &amp; Psalm 118:22)</text>

  <!-- 4 Allegorical Horizontal Cards -->
  <!-- 1. The Vineyard & Owner -->
  <g transform="translate(40, 90)">
    <rect width="345" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
    <rect width="345" height="28" rx="8" fill="#0284c7"/>
    <text x="15" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">1. VINEYARD OWNER &amp; THE VINEYARD</text>
    <text x="15" y="50" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Parable Symbol:</text>
    <text x="120" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Landowner plants vines &amp; leases farm</text>
    <text x="15" y="74" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Biblical Reality:</text>
    <text x="120" y="74" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">God the Creator &amp; Covenant Israel</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God established Israel, giving them the Law, promises,</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and divine care, expecting fruits of righteousness.</text>
  </g>

  <!-- 2. Corrupt Tenants & Servants -->
  <g transform="translate(415, 90)">
    <rect width="345" height="135" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
    <rect width="345" height="28" rx="8" fill="#d97706"/>
    <text x="15" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">2. CORRUPT TENANTS &amp; BEATEN SERVANTS</text>
    <text x="15" y="50" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Parable Symbol:</text>
    <text x="120" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Tenants beat &amp; mistreat sent servants</text>
    <text x="15" y="74" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Biblical Reality:</text>
    <text x="120" y="74" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Jewish leaders persecute OT Prophets</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Priests and Pharisees rejected Elijah, Jeremiah, and</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">John the Baptist who called them to repentance.</text>
  </g>

  <!-- 3. The Beloved Son -->
  <g transform="translate(40, 240)">
    <rect width="345" height="145" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2"/>
    <rect width="345" height="28" rx="8" fill="#dc2626"/>
    <text x="15" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">3. THE BELOVED SON &amp; MURDER PLOT</text>
    <text x="15" y="50" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Parable Symbol:</text>
    <text x="120" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Tenants cast out the Son &amp; kill Him</text>
    <text x="15" y="74" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Biblical Reality:</text>
    <text x="120" y="74" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Sanhedrin crucifies Jesus outside city</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Driven by jealousy and lust for power, the leaders</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">conspire to kill Jesus, the rightful Divine Heir.</text>
    <text x="15" y="130" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Judgment: Vineyard transferred to faithful stewards</text>
  </g>

  <!-- 4. The Cornerstone -->
  <g transform="translate(415, 240)">
    <rect width="345" height="145" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.2"/>
    <rect width="345" height="28" rx="8" fill="url(#purpleGrad3)"/>
    <text x="15" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">4. THE REJECTED CORNERSTONE (PS 118:22)</text>
    <text x="15" y="50" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Prophecy:</text>
    <text x="90" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">"Stone builders rejected becomes cornerstone"</text>
    <text x="15" y="74" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Fulfillment:</text>
    <text x="90" y="74" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Jesus is the resurrected Chief Foundation</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Whoever stumbles on Him is broken; whoever rejects</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">His authority faces crushing righteous judgment.</text>
    <text x="15" y="130" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Foundation of the Church and universal Kingdom</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">STEWARDSHIP PRINCIPLE: LEADERS ARE ACCOUNTABLE TO GOD; REJECTING CHRIST BRINGS CERTAIN JUDGMENT</text>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="silverGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <linearGradient id="goldGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PAYING TAXES TO CAESAR: DUAL CITIZENSHIP FRAMEWORK</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Balancing Civic Duty to Earthly Government with Devotion to God (Luke 20:20-26)</text>

  <!-- Left: Caesar's Realm (The Silver Denarius) -->
  <g transform="translate(40, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#silverGrad4)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">CAESAR'S SPHERE: CIVIC DUTY</text>

    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• The Denarius Coin (Image &amp; Inscription)</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Stamped with the face and name of Emperor Tiberius;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">part of the Roman imperial monetary system.</text>

    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Legitimate Public Services</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Citizens benefit from roads, courts, public order,</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">infrastructure, security, and municipal systems.</text>

    <text x="15" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Civic Obligation (Romans 13:1-7)</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pay taxes, obey traffic &amp; civil laws, protect public</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">property, and contribute to national development.</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#94a3b8" stroke-width="1"/>
    <text x="165" y="253" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">"Give to Caesar What Belongs to Caesar"</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Earthly Currency for Temporal Governance</text>
  </g>

  <!-- Right: God's Realm (The Image of God) -->
  <g transform="translate(430, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#goldGrad4)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">GOD'S SPHERE: TOTAL DEVOTION</text>

    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Stamped with God's Image (Imago Dei)</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Genesis 1:27: Human souls bear the imprint</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and likeness of God, indicating His eternal ownership.</text>

    <text x="15" y="118" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Unconditional Spiritual Loyalty</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Our conscience, worship, moral obedience, and</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">eternal allegiance belong exclusively to the Lord.</text>

    <text x="15" y="176" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Moral Boundary of State Power</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">If human laws contradict God's moral commandments,</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">believers obey God rather than men (Acts 5:29).</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="165" y="253" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">"Give to God What Belongs to God"</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Whole Heart, Soul, Mind &amp; Life to God</text>
  </g>

  <!-- Center Balance Symbol -->
  <g transform="translate(382, 220)">
    <circle cx="18" cy="18" r="18" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="18" y="23" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">⚖️</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CIVIC PRINCIPLE: BELIEVERS MAINTAIN FAITHFUL CITIZENSHIP IN BOTH EARTHLY SOCIETY AND GOD'S KINGDOM</text>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="earthGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="resGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE RESURRECTION &amp; GOD OF THE LIVING (LUKE 20:27-40)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Refuting the Sadducees: Earthly Mortal Life vs. Glorified Resurrected State</text>

  <!-- Left: Present Age (Mortal / Earthly Order) -->
  <g transform="translate(40, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#earthGrad5)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">THIS PRESENT AGE (EARTHLY ORDER)</text>

    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Marriage &amp; Procreation</text>
    <text x="15" y="76" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Men and women marry to build families and perpetuate</text>
    <text x="15" y="90" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">the human race against biological mortality.</text>

    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Levirate Marriage Law (Deut 25:5)</text>
    <text x="15" y="134" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Designed to protect childless widows and preserve</text>
    <text x="15" y="148" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">ancestral tribal property lines in ancient Israel.</text>

    <text x="15" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mortality &amp; Physical Death</text>
    <text x="15" y="192" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Physical bodies age, decay, and suffer physical</text>
    <text x="15" y="206" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">death; earthly relationships are temporal.</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
    <text x="165" y="253" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Sadducees' Flawed Assumption</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Assuming eternity is a mere clone of earthly marriage</text>
  </g>

  <!-- Right: The Age to Come (Resurrected Reality) -->
  <g transform="translate(430, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#resGrad5)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">THE AGE TO COME (RESURRECTION)</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Like the Angels (Isangeloi)</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Resurrected saints neither marry nor are given in</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">marriage; they exist in direct divine fellowship.</text>

    <text x="15" y="118" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Immortality: "They Can No Longer Die"</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Endowed with incorruptible bodies, children of God</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and children of the glorious resurrection.</text>

    <text x="15" y="176" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• The Burning Bush Proof (Exodus 3:6)</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God said: "I AM the God of Abraham, Isaac &amp; Jacob."</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">He is God of the living, for to Him all are alive!</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="165" y="253" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Eternal Covenant Victory Over Death</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Definitive refutation of Sadducean skepticism</text>
  </g>

  <g transform="translate(382, 220)">
    <path d="M 0 10 L 25 10 L 25 3 L 36 15 L 25 27 L 25 20 L 0 20 Z" fill="#38bdf8"/>
    <text x="18" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">HOPE</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">DOCTRINAL TRUTH: OUR GOD IS THE GOD OF THE LIVING, GUARANTEEING RESURRECTION AND ETERNAL LIFE</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="copperGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">SCRIBES' HYPOCRISY VS. THE WIDOW'S TWO COPPER COINS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comparing Outward Showmanship with Sacrificial Faith (Luke 20:45-47 &amp; 21:1-4)</text>

  <!-- Left: The Hypocritical Scribes -->
  <g transform="translate(40, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="#dc2626"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">THE SCRIBES: OSTENTATIOUS SHOW</text>

    <text x="15" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Love of Status &amp; Prominence</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Paraded in flowing robes, seeking public greetings,</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">chief synagogue seats, and banquet head tables.</text>

    <text x="15" y="118" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Exploitation: "Devour Widows' Houses"</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Misused legal trust to take over estates of helpless</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">widows while staging long theatrical public prayers.</text>

    <text x="15" y="176" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Surplus Giving Without Cost</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gave large financial amounts easily out of immense</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">wealth without personal sacrifice or true faith.</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="165" y="253" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Verdict: "Punished Most Severely"</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Hypocrisy, spiritual pride, and exploitation</text>
  </g>

  <!-- Right: The Poor Widow -->
  <g transform="translate(430, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#goldGrad6)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">THE POOR WIDOW: SACRIFICIAL HEART</text>

    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Two Small Copper Coins (Lepta)</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Dropped in the smallest fraction of monetary value;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">quietly, humbly, without fanfare or public praise.</text>

    <text x="15" y="118" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Total Trust: "All She Had to Live On"</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gave her entire livelihood (bios), surrendering her</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">next meal in complete dependence on God's provision.</text>

    <text x="15" y="176" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Divine Kingdom Arithmetic</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus: "She put in more than all the others." God</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">measures the sacrifice of the heart, not amount.</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="165" y="253" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Verdict: "Put in More Than All"</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Genuine faith, radical generosity, and sincerity</text>
  </g>

  <!-- Center Balance -->
  <g transform="translate(382, 220)">
    <circle cx="18" cy="18" r="18" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="18" y="23" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">💰</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">MORAL AXIOM: GOD MEASURES GENEROSITY BY THE PROPORTION OF SACRIFICE AND THE SINCERITY OF LOVE</text>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="redGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="blueGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ESCHATOLOGY &amp; SIGNS OF THE END TIMES (LUKE 21:5-28)</text>
  <text x="400" y="63" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">A Comprehensive Roadmap from Temple Destruction to the Glorious Return of the Son of Man</text>

  <!-- 3 Stage Timeline Cards -->
  <!-- Phase 1: Historical Fall of Jerusalem -->
  <g transform="translate(30, 85)">
    <rect width="230" height="305" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="#dc2626"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. FALL OF JERUSALEM (70 AD)</text>

    <text x="12" y="55" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Temple Dismantled</text>
    <text x="12" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Not one stone left on</text>
    <text x="12" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">another" fulfilled literally</text>
    <text x="12" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">by Roman General Titus.</text>

    <text x="12" y="122" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• City Besieged</text>
    <text x="12" y="137" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Enemies built embankments</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">surrounding Jerusalem,</text>
    <text x="12" y="163" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">causing severe distress.</text>

    <text x="12" y="189" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Dispersion of People</text>
    <text x="12" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Fallen by sword and led</text>
    <text x="12" y="217" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">captive to all nations.</text>

    <rect x="12" y="250" width="206" height="38" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="115" y="267" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Historical Prophecy</text>
    <text x="115" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">End of the Old Temple Era</text>
  </g>

  <!-- Phase 2: Age of Tribulation & Signs -->
  <g transform="translate(285, 85)">
    <rect width="230" height="305" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="#d97706"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. TRIBULATION &amp; SIGNS</text>

    <text x="12" y="55" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• False Messiahs</text>
    <text x="12" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Impostors claiming: "I am</text>
    <text x="12" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">He!" Do not follow them.</text>

    <text x="12" y="108" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Wars &amp; Calamities</text>
    <text x="12" y="123" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Nation vs. nation, famines,</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">earthquakes, and plagues.</text>

    <text x="12" y="161" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Persecution &amp; Witness</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Arrested and betrayed for</text>
    <text x="12" y="189" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Christ's name; opportunity</text>
    <text x="12" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">for courageous testimony.</text>

    <rect x="12" y="250" width="206" height="38" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="115" y="267" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">"Stand Firm &amp; Win Life"</text>
    <text x="115" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Divine protection of soul</text>
  </g>

  <!-- Phase 3: Cosmic Climax & Return -->
  <g transform="translate(540, 85)">
    <rect width="230" height="305" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="url(#blueGrad7)"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. GLORIOUS RETURN</text>

    <text x="12" y="55" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Cosmic Disturbances</text>
    <text x="12" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Signs in sun, moon, stars;</text>
    <text x="12" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">roaring seas, heavenly</text>
    <text x="12" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">bodies shaken.</text>

    <text x="12" y="122" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Son of Man in Power</text>
    <text x="12" y="137" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Coming in a cloud with</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">supreme authority, majesty,</text>
    <text x="12" y="163" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and cosmic glory.</text>

    <text x="12" y="189" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Full Redemption Nears</text>
    <text x="12" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Stand up and lift up your</text>
    <text x="12" y="217" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">heads, redemption draws near!"</text>

    <rect x="12" y="250" width="206" height="38" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="115" y="267" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Ultimate Victory of God</text>
    <text x="115" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Establishment of Eternal Kingdom</text>
  </g>

  <!-- Connecting Arrows -->
  <g transform="translate(262, 220)">
    <path d="M 0 5 L 18 5 L 18 0 L 25 8 L 18 16 L 18 11 L 0 11 Z" fill="#94a3b8"/>
  </g>
  <g transform="translate(517, 220)">
    <path d="M 0 5 L 18 5 L 18 0 L 25 8 L 18 16 L 18 11 L 0 11 Z" fill="#94a3b8"/>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">ESCHATOLOGICAL POSTURE: ENDURANCE, CONFIDENCE, AND LIFTING UP HEADS IN JOYFUL HOPE</text>
</svg>"""


def get_svg_lesson_8():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="greenGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="roseGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#9f1239"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE FIG TREE &amp; THE CALL TO SPIRITUAL WATCHFULNESS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Discerning the Signs &amp; Guarding the Heart Against Worldly Traps (Luke 21:29-38)</text>

  <!-- Left: The Fig Tree Analogy (Natural Discernment) -->
  <g transform="translate(40, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="url(#greenGrad8)"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">THE FIG TREE: NATURAL DISCERNMENT</text>

    <text x="15" y="60" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sprouting Leaves = Summer is Near</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Anyone observing budding twigs knows summer and</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">harvest season are arriving without being told.</text>

    <text x="15" y="118" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Discerning God's Prophetic Timeline</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Seeing prophetic signs unfold confirms that the</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Kingdom of God is near and actively breaking in.</text>

    <text x="15" y="176" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Permanence of Christ's Word</text>
    <text x="15" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Heaven and earth will pass away, but my words will</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">never pass away." Unshakable foundation of truth.</text>

    <rect x="15" y="235" width="300" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="165" y="253" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Spiritual Alertness &amp; Discernment</text>
    <text x="165" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Living with clear awareness of God's timing</text>
  </g>

  <!-- Right: Guarding the Heart & Persistent Prayer -->
  <g transform="translate(430, 95)">
    <rect width="330" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="#0284c7"/>
    <text x="165" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">WATCHFULNESS: GUARDING THE HEART</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Beware of 3 Weigh-Down Traps</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">1. Carousing (reckless, uncontrolled partying)</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">2. Drunkenness (substance abuse &amp; escapism)</text>
    <text x="15" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">3. Anxieties of Life (obsession with wealth &amp; worry)</text>

    <text x="15" y="132" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• The Sudden Trap</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Unprepared souls are caught suddenly in a snare;</text>
    <text x="15" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">spiritual lethargy leads to irreversible loss.</text>

    <text x="15" y="190" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Practice: "Be Always on the Watch &amp; Pray"</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pray continuously for strength to overcome evil,</text>
    <text x="15" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and to stand boldly before the Son of Man.</text>

    <rect x="15" y="245" width="300" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="165" y="265" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Active Readiness in Daily Obedience &amp; Prayer</text>
  </g>

  <!-- Center Shield Icon -->
  <g transform="translate(382, 220)">
    <circle cx="18" cy="18" r="18" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="18" y="23" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">🛡️</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">DISCIPLESHIP IMPERATIVE: LIVE EVERY DAY IN PRAYERFUL READINESS, UNENCUMBERED BY WORLDLY ANXIETIES</text>
</svg>"""


# ─── COMPLETE LESSON DATA (8 LESSONS) ────────────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "The Triumphant Entry into Jerusalem",
        "unit_description": "Explores Jesus' royal yet humble entry into Jerusalem riding on an unridden donkey colt (Luke 19:28-40), fulfilling Zechariah 9:9, contrasting peace with military violence, and analyzing the cosmic significance of creation crying out.",
        "lesson_title": "The Triumphant Entry into Jerusalem",
        "image": {
            "title": "Giotto di Bondone: Entry into Jerusalem (Scrovegni Chapel)",
            "caption": "14th-century fresco depicting Jesus riding a humble donkey colt into Jerusalem as disciples and pilgrims lay their cloaks on the dusty road.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Giotto_-_Scrovegni_-_-26-_-_Entry_into_Jerusalem.jpg/800px-Giotto_-_Scrovegni_-_-26-_-_Entry_into_Jerusalem.jpg",
            "author": "Giotto di Bondone",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_1,
        "youtube": {
            "title": "BibleProject: Gospel of Luke (Chapters 19-24)",
            "description": "Visual exploration of Jesus' final week in Jerusalem, His royal entry as the Prince of Peace, and the climax of Luke's Gospel.",
            "youtube_id": "26z_KhwNqnM"
        },
        "goals": [
            "Retell the sequence of events during Jesus' triumphant entry into Jerusalem from the Mount of Olives.",
            "Explain the symbolic difference between a humble donkey colt and an imperial war horse in ancient biblical times.",
            "Formulate actionable ways to practice servant leadership and peaceful humility in school, home, and community life."
        ],
        "intro": """Have you ever witnessed a major national celebration—like a president's inauguration or a high-ranking military parade—where leaders arrive in armored bulletproof motorcades, accompanied by heavily armed police outriders, sirens, and intimidating security escorts? It is a massive show of worldly power, prestige, and dominance.

When Jesus Christ, the King of kings and Lord of lords, made His official, royal entry into the holy capital city of Jerusalem, He did not assemble chariots, armed legions, or muscular war horses. Instead, He rode on a borrowed, humble young donkey colt that had never been ridden before. Why did the supreme King choose such profound gentleness and humility?""",
        "core_scripture": """### Luke 19:28-40 (NIV)
> "After Jesus had said this, he went on ahead, going up to Jerusalem. As he approached Bethphage and Bethany at the hill called the Mount of Olives, he sent two of his disciples, saying to them, 'Go to the village ahead of you, and as you enter it, you will find a colt tied there, which no one has ever ridden. Untie it and bring it here. If anyone asks you, \"Why are you untying it?\" say, \"The Lord needs it.\"'
>
> Those who were sent ahead went and found it just as he had told them. As they were untying the colt, its owners asked them, 'Why are you untying the colt?' They replied, 'The Lord needs it.' They brought it to Jesus, threw their cloaks on the colt and put Jesus on it.
>
> As he went along, people spread their cloaks on the road. When he came near the place where the road goes down the Mount of Olives, the whole crowd of disciples began joyfully to praise God in loud voices for all the miracles they had seen:
>
> 'Blessed is the king who comes in the name of the Lord!'
> 'Peace in heaven and glory in the highest!'
>
> Some of the Pharisees in the crowd said to Jesus, 'Teacher, rebuke your disciples!'
>
> 'I tell you,' he replied, 'if they keep quiet, the stones will cry out.'\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. Fulfilling Prophecy: Zechariah 9:9
Five hundred years before Christ's birth, the prophet Zechariah declared:
> *"Rejoice greatly, Daughter Zion! Shout, Daughter Jerusalem! See, your king comes to you, righteous and victorious, lowly and riding on a donkey, on a colt, the foal of a donkey."* (Zechariah 9:9)

By deliberately arranging to ride a donkey colt, Jesus was publicly proclaiming His true Messianic royalty. He was not an accidental pilgrim; He was Israel's promised, righteous King arriving in the royal city of David.

#### 2. The Donkey: Mount of Peace vs. Stallion of War
In ancient Near Eastern culture:
- **War Horses & Stallions:** Ridden by military conquerors, generals, and kings embarking on bloody campaigns to subjugate territories and slaughter enemies.
- **Donkeys:** Ridden by rulers during times of peace, reconciliation, and civil justice, signaling peaceful and benevolent intentions.

Jesus demonstrated that His Kingdom is not established through brute military force, coercion, or political rebellion against Rome, but through sacrificial love, spiritual reconciliation, and peace between God and humanity.

#### 3. The Unridden Colt & Sacred Consecration
Under Mosaic Law (e.g., Numbers 19:2, Deuteronomy 21:3), an animal that had never borne a yoke or been ridden was set apart exclusively for sacred, divine purposes. Jesus riding an unridden colt signified that His mission was purely consecrated to the Father.

#### 4. Spreading Cloaks: Total Loyalty & Surrender
When the crowds threw their cloaks on the donkey's back and spread them across the dusty road (an ancient practice seen in 2 Kings 9:13 for King Jehu), they were demonstrating absolute submission: *"We place our lives, our dignity, and our allegiance beneath Your royal feet."*

#### 5. "The Stones Will Cry Out": Cosmic Messianic Glory
When irritated Pharisees commanded Jesus to silence the singing crowd, Jesus replied that if human voices were silenced, the very stones would shout. This reveals that Christ's Lordship is woven into the fabric of creation; nature itself recognizes its Maker and will not allow His glory to go unproclaimed.""",
        "deep_dive": """### Deep Dive: Geography, Messianic Hope, and the Mount of Olives

#### The Geographic Route
Jesus' descent began from Bethphage and Bethany on the eastern slope of the Mount of Olives, looking west across the Kidron Valley directly toward the magnificent Temple complex and the Golden Gate (Eastern Gate). This high vantage point was steeped in Messianic expectation (Zechariah 14:4 prophesied that God's Messiah would stand on the Mount of Olives).

#### The Expectation of the Crowds
Jerusalem was overflowing with hundreds of thousands of Passover pilgrims celebrating Israel's ancient liberation from Egyptian slavery. The crowds hoped Jesus would be a military liberator who would overthrow the oppressive Roman governor Pontius Pilate and restore Jewish political sovereignty. However, Jesus came to liberate them from a far deadlier tyrant: sin, spiritual darkness, and eternal death.""",
        "practical": {
            "title": "4-Step Framework for Practicing Servant Leadership",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Choose Approachability Over Intimidation",
                    "description": "Whether appointed as a class prefect, sports captain, or group leader, reject harshness and loud demands. Lead with gentleness, active listening, and warmth."
                },
                {
                    "step_number": 2,
                    "title": "Serve Behind the Scenes",
                    "description": "Emulate Christ's humility by undertaking unglamorous tasks—such as arranging desks, collecting books, or cleaning communal areas—without seeking applause."
                },
                {
                    "step_number": 3,
                    "title": "Promote Peace in Peer Conflicts",
                    "description": "Act as a peacemaker during disagreements among classmates. De-escalate arguments through calm dialogue, empathy, and constructive mediation."
                },
                {
                    "step_number": 4,
                    "title": "Give Glory to God for Achievements",
                    "description": "When praised for academic, sporting, or artistic excellence, remain humble and acknowledge God as the source of your talents and opportunities."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenyan society, political leadership and social status are often associated with VIP convoys, bodyguards, sirens, and lavish displays of wealth. This cultural perception can tempt young people to equate authority with dominating others and showing off.

Jesus' model of triumphant humility provides a vital blueprint for Kenyan youth leadership:
- **Student Councils & Prefect Bodies:** In secondary schools and junior schools, student leaders must abandon bullying or punitive favoritism, choosing instead to serve and protect their peers.
- **National Cohesion & Peaceful Coexistence:** In a diverse multi-ethnic nation like Kenya, embracing Christ's posture of peace inspires youth to build bridges across tribal and cultural divides rather than engaging in conflict or political riots.
- **Community Volunteering:** Demonstrating true leadership by participating in local environmental cleanups, tree planting, and supporting vulnerable neighbors in informal settlements.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Humility and Peace
- **Self-Examination:** Do you seek popularity and influence by dominating others, or do you earn respect through genuine kindness, helpfulness, and integrity?
- **Prayer of Dedication:** "Lord Jesus, Prince of Peace, teach me to walk in Your humility. Strip away my pride, boastfulness, and desire for worldly showmanship. Help me to use whatever influence and gifts I possess to serve my school, family, and nation with a gentle and faithful heart. Amen.\"""",
        "takeaways": [
            "Jesus entered Jerusalem riding an unridden donkey colt, deliberately fulfilling the ancient prophecy of Zechariah 9:9 as Israel's humble King.",
            "A donkey symbolized peace, reconciliation, and servant royalty, directly contrasting with the war horses of violent earthly conquerors.",
            "The crowd laid cloaks and palm branches on the road as an act of total surrender and joyful loyalty to the Messiah.",
            "Jesus declared that if people failed to praise Him, the stones would cry out, demonstrating the cosmic reality of His Lordship.",
            "Christian leadership is measured not by how many people serve us, but by how humbly and faithfully we serve others."
        ],
        "mcq": {
            "question": "What did Jesus' choice to ride a young donkey colt into Jerusalem symbolize about His Messianic mission?",
            "options": [
                "A) That He was unable to afford a Roman chariot or military horse",
                "B) That He came as the humble Prince of Peace fulfilling Zechariah 9:9, rather than a violent military conqueror",
                "C) That He intended to start an agricultural enterprise in the Kidron Valley",
                "D) That He was rushing urgently and mounted the nearest available animal"
            ],
            "answer": "B",
            "explanation": "In ancient Near Eastern culture, riding a donkey symbolized peace and friendly intentions. Jesus fulfilled Zechariah 9:9 by entering Jerusalem as the humble, righteous King who brings spiritual peace and salvation, rejecting worldly military conquest."
        }
    },

    # ─── LESSON 2 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Jesus Weeps and Cleanses the Temple",
        "unit_description": "Examines why Jesus wept over Jerusalem's impending destruction (Luke 19:41-44) and His dramatic cleansing of the Temple (Luke 19:45-48), citing Isaiah 56:7 and Jeremiah 7:11 to reclaim God's house as a holy house of prayer.",
        "lesson_title": "Jesus Weeps and Cleanses the Temple",
        "image": {
            "title": "Carl Bloch: Cleansing of the Temple",
            "caption": "19th-century masterwork portraying Jesus driving out corrupt merchants and overturning tables in the Temple courts with righteous zeal.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Carl_Bloch_-_Cleansing_of_the_Temple.jpg/800px-Carl_Bloch_-_Cleansing_of_the_Temple.jpg",
            "author": "Carl Bloch",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_2,
        "youtube": {
            "title": "BibleProject: Temple",
            "description": "An overview of how God's Temple was designed as the sacred meeting place between Heaven and Earth, and how Jesus reclaimed and fulfilled it.",
            "youtube_id": "wTnq6I3vUbY"
        },
        "goals": [
            "Explain the compassionate reasons why Jesus wept over the holy city of Jerusalem as He approached it.",
            "Analyze how the Court of the Gentiles was corrupted by traders and explain why Jesus cleared it with righteous anger.",
            "Apply the principle of reverence for sacred spaces and personal holiness in daily Christian living."
        ],
        "intro": """Imagine walking into your school chapel or classroom during morning worship and discovering that several individuals have set up noisy commercial stalls inside. They are shouting loudly, selling snacks at inflated prices, exchanging currency with unfair fees, and blocking students who came to pray. You would feel deeply disturbed and outraged.

Holy places are designed for reverence, quiet reflection, and pure worship. When Jesus entered God's Temple in Jerusalem—the most sacred sanctuary in Judaism—He found a corrupt marketplace exploiting poor worshippers. Let us examine His tears of compassion and His bold action of cleansing.""",
        "core_scripture": """### Luke 19:41-48 (NIV)
> "As he approached Jerusalem and saw the city, he wept over it and said, 'If you, even you, had only known on this day what would bring you peace—but now it is hidden from your eyes. The days will come upon you when your enemies will build an embankment against you and encircle you and hem you in on every side. They will dash you to the ground, you and the children within your walls. They will not leave one stone on another, because you did not recognize the time of God's coming to you.'
>
> When Jesus entered the temple courts, he began to drive out those who were selling. 'It is written,' he said to them, '\"My house will be a house of prayer\"; but you have made it \"a den of thieves.\"'
>
> Every day he was teaching at the temple. But the chief priests, the teachers of the law and the leaders among the people were trying to kill him. Yet they could not find any way to do it, because all the people hung on his words.\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. Jesus Weeps Over Jerusalem (Compassion & Judgment)
As Jesus crested the Mount of Olives and looked upon Jerusalem, He did not gloat or display pride. He wept openly (*eklausen* in Greek—wept aloud with deep grief).
- **The Tragedy of Rejection:** The people were blind to the Messiah of peace. By choosing political nationalism and rejecting Christ, they were heading toward catastrophic destruction.
- **Prophecy of 70 AD:** Jesus predicted the Roman siege of Jerusalem under General Titus in 70 AD, where the city was surrounded, starved, and the magnificent Temple burned and razed to the ground.

#### 2. The Court of the Gentiles: Desecration of Sacred Space
The Temple had distinct courts: the Holy of Holies, Court of Priests, Court of Israel, Court of Women, and the outermost **Court of the Gentiles**.
- The Court of the Gentiles was the only area where non-Jewish seekers from other nations could come to pray and seek the one true God.
- The high-priestly family of Annas had converted this court into the "Bazaars of Annas," filling it with noisy animals, bird cages, and money-exchange tables.
- This effectively shut out international seekers, transforming a place of global prayer into a chaotic, greedy trade depot.

#### 3. Righteous Anger vs. Sinful Temper
Jesus' action was not an uncontrolled loss of temper, but **righteous anger**—a holy, passionate indignation against injustice, oppression of the poor, and the dishonoring of God. He overturned tables and drove out sellers with divine authority.

#### 4. "House of Prayer" vs. "Den of Thieves"
Jesus quoted two profound Old Testament scriptures:
- **Isaiah 56:7:** *"My house will be called a house of prayer for all nations."* God intended His sanctuary for international worship, peace, and communion.
- **Jeremiah 7:11:** *"Has this house, which bears my Name, become a den of robbers to you?"* In Jeremiah's day, bandits hid in mountain caves after robbing people. Similarly, corrupt religious leaders were cheating pilgrims all week, then hiding in the Temple pretending to be righteous.""",
        "deep_dive": """### Deep Dive: The Currency Scam and Animal Monopoly

#### The Temple Currency Monopoly
Jewish law required every male to pay an annual half-shekel Temple tax during Passover (Exodus 30:13). However, Roman, Greek, and Persian coins bearing the images of pagan emperors and gods were forbidden in the Temple treasury. Pilgrims were forced to exchange their secular coins for official Tyrian shekels. Moneychangers charged extortionate exchange fees (up to 25%), lining the pockets of the corrupt high priests.

#### Sacrificial Animal Inspections
Pilgrims who brought their own sheep or doves from long distances had them inspected by Temple priests. Priests would routinely declare the pilgrims' animals "blemished" and force them to buy expensive "pre-approved" animals from Temple merchants at inflated rates. Jesus intervened directly to protect these impoverished and exploited worshippers.""",
        "practical": {
            "title": "4-Step Framework for Maintaining Reverence and Purity",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Maintain Reverence in Places of Worship",
                    "description": "When attending church, chapel, or Christian Union meetings, switch off phone distractions, refrain from gossip, and engage your heart in sincere prayer."
                },
                {
                    "step_number": 2,
                    "title": "Guard Your Body as God's Living Temple",
                    "description": "Recognize that your physical body is the temple of the Holy Spirit (1 Corinthians 6:19). Protect it from substance abuse, immorality, and harmful habits."
                },
                {
                    "step_number": 3,
                    "title": "Stand Up Against Injustice and Greed",
                    "description": "Speak out peacefully against corruption, extortion, and cheating in your school or community, defending the vulnerable from exploitation."
                },
                {
                    "step_number": 4,
                    "title": "Prioritize Spiritual Value Over Material Gain",
                    "description": "Never allow financial greed or commercial interests to overshadow integrity, honest relationships, and love for God and others."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenya, issues regarding financial transparency within religious institutions and sacred venues are widely discussed:
- **Commercialization of Faith:** Some unscrupulous preachers exploit vulnerable citizens by demanding money for "miracles," "holy water," or "special blessings." Jesus' cleansing of the Temple teaches Kenyan youth to reject commercialized religion and uphold genuine, biblically sound worship.
- **Respecting School and Community Sanctuaries:** Ensuring that school halls, prayer rooms, and church facilities are maintained with cleanliness, order, and dignity.
- **Fighting Financial Exploitation:** Young people are called to practice strict honesty in handling club funds, student treasury collections, and church offerings.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Respect for Sacred Spaces, Sincerity, and Justice
- **Self-Examination:** Have you allowed selfish motives, distraction, or dishonest shortcuts to clutter your heart, which is God's living temple?
- **Prayer of Dedication:** "Lord God, cleanse my heart and mind from all impurities, selfishness, and hypocrisy. Make my life a sacred house of prayer, devotion, and compassion. Give me courage to stand for truth and protect the vulnerable from exploitation. In Jesus' name, Amen.\"""",
        "takeaways": [
            "Jesus wept over Jerusalem because He foresaw its impending destruction in 70 AD due to its rejection of the Prince of Peace.",
            "The Court of the Gentiles had been corrupted into a noisy, extortionate marketplace by greedy merchants and chief priests.",
            "Jesus drove out traders with righteous anger, citing Isaiah 56:7 and Jeremiah 7:11 to restore the Temple as a house of prayer.",
            "Righteous anger is holy indignation against moral injustice, corruption, and the exploitation of the weak.",
            "Today, believers are called to honor church sanctuaries and maintain personal holiness as living temples of the Holy Spirit."
        ],
        "mcq": {
            "question": "Why did Jesus quote Isaiah 56:7 and Jeremiah 7:11 when driving merchants out of the Temple courts?",
            "options": [
                "A) Because He wanted to encourage the Roman government to build a military barracks inside the sanctuary",
                "B) Because the Court of the Gentiles had been turned from an international house of prayer into an extortionate den of thieves",
                "C) Because the traders had failed to pay municipal property taxes to the Jerusalem city council",
                "D) Because He wanted to take over the commercial sales and manage the currency exchange Himself"
            ],
            "answer": "B",
            "explanation": "Jesus cleansed the Temple because religious elites had converted the Court of the Gentiles—meant for prayer for all nations (Isaiah 56:7)—into an exploitative marketplace where corrupt merchants cheated poor pilgrims (Jeremiah 7:11)."
        }
    },

    # ─── LESSON 3 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Conflict Over Jesus' Authority and the Parable of the Tenants",
        "unit_description": "Analyzes the Sanhedrin's challenge to Jesus' authority (Luke 20:1-8), Jesus' question about John's baptism, the allegorical meaning of the Parable of the Tenants (Luke 20:9-19), and Christ as the rejected Cornerstone (Psalm 118:22).",
        "lesson_title": "Conflict Over Jesus' Authority and the Parable of the Tenants",
        "image": {
            "title": "James Tissot: The Corner Stone (La Pierre d'Angle)",
            "caption": "Late 19th-century illustration showing Jesus teaching in the Temple porticoes, confronting chief priests and scribes with the truth of the rejected Cornerstone.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Brooklyn_Museum_-_The_Corner_Stone_%28La_pierre_de_l%27angle%29_-_James_Tissot.jpg/800px-Brooklyn_Museum_-_The_Corner_Stone_%28La_pierre_de_l%27angle%29_-_James_Tissot.jpg",
            "author": "James Tissot",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_3,
        "youtube": {
            "title": "BibleProject: Gospel of Luke (Chapters 19-24)",
            "description": "An in-depth look at Jesus' confrontations with religious leaders in the Jerusalem Temple and His prophetic teachings.",
            "youtube_id": "26z_KhwNqnM"
        },
        "goals": [
            "Describe how Jesus countered the religious leaders' trap regarding the divine origin of His authority.",
            "Decode the allegorical figures in the Parable of the Tenants and connect them to God's salvation history.",
            "Explain the theological meaning of Jesus as the 'rejected Cornerstone' from Psalm 118:22 and apply faithful stewardship in life."
        ],
        "intro": """Imagine a newly appointed, highly effective student leader organizes a massive school cleanup campaign that transforms a messy campus into a spotless environment. Instead of celebrating the improvement, older, lazy prefects feel threatened because their own neglect has been exposed. They march up angrily and demand: "Who gave you permission to do this? Who do you think you are?"

They are not concerned with the cleanliness of the school; they only care about protecting their threatened prestige. This is precisely how the chief priests, scribes, and elders confronted Jesus after He cleansed the Temple. Let us explore His masterclass in divine wisdom.""",
        "core_scripture": """### Luke 20:1-19 (NIV)
> "One day as Jesus was teaching the people in the temple courts and proclaiming the good news, the chief priests and the teachers of the law, together with the elders, came up to him. 'Tell us by what authority you are doing these things,' they said. 'Who gave you this authority?'
>
> He replied, 'I will also ask you a question. Tell me: John’s baptism—was it from heaven, or of human origin?'
>
> They discussed it among themselves and said, 'If we say, \"From heaven,\" he will ask, \"Why didn't you believe him?\" But if we say, \"Of human origin,\" all the people will stone us, because they are persuaded that John was a prophet.' So they answered, 'We don't know where it came from.'
>
> Jesus said, 'Neither will I tell you by what authority I am doing these things.'
>
> He went on to tell the people this parable: 'A man planted a vineyard, rented it to some tenant farmers and went away for a long time. At harvest time he sent a servant to the tenants so they would give him some of the fruit of the vineyard. But the tenants beat him and sent him away empty-handed. He sent another servant, but that one also they beat and treated shamefully and sent away empty-handed. He sent still a third, and they wounded him and threw him out.
>
> 'Then the owner of the vineyard said, \"What shall I do? I will send my son, whom I love; perhaps they will respect him.\"
>
> 'But when the tenants saw him, they talked it over. \"This is the heir,\" they said. \"Let’s kill him, and the inheritance will be ours.\" So they threw him out of the vineyard and killed him.
>
> 'What then will the owner of the vineyard do to them? He will come and kill those tenants and give the vineyard to others.'
>
> When the people heard this, they said, 'God forbid!'
>
> Jesus looked directly at them and asked, 'Then what is the meaning of that which is written: \"The stone the builders rejected has become the cornerstone\"? Everyone who falls on that stone will be broken to pieces; anyone on whom it falls will be crushed.'
>
> The teachers of the law and the chief priests looked for a way to arrest him immediately, because they knew he had spoken this parable against them. But they were afraid of the people.\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. The Counter-Question: Exposing Intellectual Dishonesty
The Sanhedrin demanded Jesus' credentials. If Jesus replied, "By God's authority," they would accuse Him of blasphemy. If He replied, "By human authority," they would dismiss Him as an unauthorized teacher.
- Jesus asked about John the Baptist: *"Was his baptism from heaven or of human origin?"*
- This trapped the leaders in their own hypocrisy. John had publicly testified that Jesus was the Lamb of God. If they admitted John was from God, they stood condemned for rejecting John's testimony about Jesus. If they denied John, the crowd would stone them.
- Their cowardly answer ("We don't know") exposed their bad faith, justifying Jesus' refusal to indulge them.

#### 2. Decoding the Parable of the Tenants
Jesus immediately told a biting allegory rooted in Isaiah 5 (the Song of the Vineyard):
- **The Landowner:** God the Father, who lovingly planted Israel as His vineyard.
- **The Vineyard:** The nation of Israel and the Kingdom of God.
- **The Tenants:** The religious leaders (chief priests, scribes, Sanhedrin) entrusted to shepherd the people and yield spiritual fruit.
- **The Sent Servants (Beat & Wounded):** Old Testament prophets (Elijah, Jeremiah, Zechariah) who called Israel to repentance and were persecuted or killed.
- **The Beloved Son:** Jesus Christ, God's only begotten Son, whom the tenants cast out of the vineyard (crucified outside Jerusalem's city walls) to seize control.
- **The Judgment:** The vineyard would be taken from corrupt leaders and given to others (the Apostles, Gentiles, and the global Church).

#### 3. The Cornerstone (Psalm 118:22)
In ancient construction, the cornerstone was the primary, flawlessly cut stone laid at the corner to anchor and align the entire foundation:
- The "builders" (religious authorities) rejected Jesus as unsuitable for their political ambitions.
- God exalted this rejected stone to become the supreme Foundation of the Church.
- Rejecting Christ brings spiritual ruin: stumbling over Him leads to brokenness, and opposing His final reign leads to crushing judgment.""",
        "deep_dive": """### Deep Dive: Ancient Tenant Farming Laws and Inheritance Claims

#### Ancient Near Eastern Tenant Laws
In the first century, Roman and Jewish property laws held that if an absentee landlord died without legal heirs, tenant farmers who had occupied the land could claim squatter's rights and take legal ownership of the estate.

When the tenants in the parable saw the Beloved Son arriving alone, they assumed the owner had died and the son had come to claim the estate. They reasoned: *"If we kill the sole heir, the vineyard will become ours legally."* This mirrors the Sanhedrin's mindset: they believed that by executing Jesus, they would eliminate His challenge and maintain absolute religious power over the Jewish people forever.""",
        "practical": {
            "title": "4-Step Framework for Practicing Godly Stewardship",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Acknowledge God's Ultimate Ownership",
                    "description": "Recognize that your life, health, intellectual abilities, and resources belong to God. You are a steward entrusted to manage them faithfully."
                },
                {
                    "step_number": 2,
                    "title": "Yield Spiritual Fruit Consistently",
                    "description": "Produce good fruit in your character—such as honesty, diligence, kindness, and self-control—rather than living in selfish rebellion."
                },
                {
                    "step_number": 3,
                    "title": "Respect Legitimate Authority with Wisdom",
                    "description": "Honor parents, teachers, and mentors. When confronting unfair opposition, respond with Christlike wisdom and calmness rather than rage."
                },
                {
                    "step_number": 4,
                    "title": "Build Your Life on Jesus the Cornerstone",
                    "description": "Make Jesus Christ the foundational anchor of your decisions, moral values, and future ambitions, ensuring your life stands firm against life's storms."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenya, disputes regarding land ownership, tenancy agreements, and inheritance rights are common in courts and rural communities:
- **Integrity in Stewardship:** Land caretakers and agricultural managers must never defraud property owners or misappropriate harvests. Biblical stewardship demands absolute honesty.
- **Accountability of Leaders:** Just as the corrupt tenants faced divine judgment, Kenyan leaders in government, corporations, schools, and churches are accountable to God and citizens for how they manage public resources.
- **Listening to Truth:** Rejecting wise counsel and silencing whistleblowers leads to institutional collapse, just as Israel's leaders suffered destruction for rejecting the prophets.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Wisdom, Justice, and Faithful Stewardship
- **Self-Examination:** Are you managing the gifts, education, and time God has entrusted to you responsibly, or are you acting like the rebellious tenants who claimed ownership for themselves?
- **Prayer of Dedication:** "Heavenly Father, You are the Creator and Owner of all things. Forgive me for times when I take Your blessings for granted. Help me to be a faithful steward of my talents and opportunities, and anchor my entire life upon Jesus Christ, my true Cornerstone. Amen.\"""",
        "takeaways": [
            "Jesus silenced the Sanhedrin's challenge by questioning them on John the Baptist's authority, exposing their insincerity.",
            "The Parable of the Tenants illustrates Israel's history of persecuting God's prophets and prophesies the murder of God's Beloved Son.",
            "Jesus predicted that God's Kingdom would be taken from corrupt leaders and entrusted to faithful stewards across all nations.",
            "Jesus is the rejected Cornerstone (Psalm 118:22), the essential foundation upon which the Church and Christian life are established.",
            "Human authority is temporary and delegated; all leaders will give an account of their stewardship before God."
        ],
        "mcq": {
            "question": "In the Parable of the Tenants (Luke 20:9-19), what does the murder of the 'Beloved Son' represent?",
            "options": [
                "A) The tragic death of King David's son Absalom in battle",
                "B) The execution of the prophet John the Baptist by King Herod",
                "C) The upcoming crucifixion of Jesus Christ outside Jerusalem by the plotting religious authorities",
                "D) A routine agricultural dispute between Galilean farmers and Roman soldiers"
            ],
            "answer": "C",
            "explanation": "In Jesus' parable, the Landowner's 'Beloved Son' sent to the vineyard represents Jesus Christ Himself, whom the Jewish religious leaders conspired to arrest and crucify outside Jerusalem in a futile attempt to preserve their own power."
        }
    },

    # ─── LESSON 4 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Paying Taxes to Caesar",
        "unit_description": "Explores the political trap regarding Roman taxation (Luke 20:20-26), Jesus' iconic reply with the denarius coin, and the dual citizenship framework balancing civic duty with absolute devotion to God (Romans 13:1-7).",
        "lesson_title": "Paying Taxes to Caesar",
        "image": {
            "title": "Peter Paul Rubens: The Tribute Money",
            "caption": "17th-century masterpiece depicting Jesus holding the Roman denarius coin, confounding the deceptive spies with His timeless answer.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Peter_Paul_Rubens_-_The_Tribute_Money_-_Google_Art_Project.jpg/800px-Peter_Paul_Rubens_-_The_Tribute_Money_-_Google_Art_Project.jpg",
            "author": "Peter Paul Rubens",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_4,
        "youtube": {
            "title": "BibleProject: Image of God",
            "description": "Explores what it means to be made in God's image and how our entire lives bear His divine imprint, linking directly to Jesus' teaching on Caesar and God.",
            "youtube_id": "YbipxEDBDsc"
        },
        "goals": [
            "Analyze the dangerous political double-trap engineered by spies regarding the payment of Roman poll taxes.",
            "Explain the theological and civic meaning of Jesus' response: 'Give to Caesar what is Caesar's, and to God what is God's.'",
            "Demonstrate how Christian youth can fulfill civic obligations (patriotism, obeying laws) while maintaining undivided devotion to God."
        ],
        "intro": """Have you ever been confronted with a vicious double-trap question designed to guarantee your failure no matter what you say? For example, imagine a mischievous classmate asks in front of the teacher: "Is our school administration completely unfair, or are you just a coward?" If you say the administration is unfair, you get suspended for indiscipline. If you say you are a coward, you lose the respect of your peers.

The enemies of Jesus thought they had devised the ultimate, foolproof political trap to destroy Him regarding Roman taxation. Let us examine how Jesus sliced through their deception with divine brilliance.""",
        "core_scripture": """### Luke 20:20-26 (NIV)
> "Keeping a close watch on him, they sent spies, who pretended to be sincere. They hoped to catch Jesus in something he said, so that they might hand him over to the power and authority of the governor.
>
> So the spies questioned him: 'Teacher, we know that you speak and teach what is right, and that you do not show partiality but teach the way of God in accordance with the truth. Is it right for us to pay taxes to Caesar or not?'
>
> He saw through their duplicity and said to them, 'Show me a denarius. Whose image and inscription are on it?'
>
> 'Caesar’s,' they replied.
>
> He said to them, 'Then give back to Caesar what is Caesar’s, and to God what is God’s.'
>
> They were unable to trap him in what he had said there in public. And astonishment at his answer silenced them.\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. The Anatomy of the Political Trap
Judea was under Roman military occupation. Every Jewish resident was subject to an annual poll tax (*tributum capitis*) paid directly to the Roman Emperor.
- **If Jesus said "Yes, pay taxes":** The patriotic Jewish crowds, who despised Roman oppression, would view Him as a traitor, collaborator, and false Messiah who bowed to Rome.
- **If Jesus said "No, do not pay":** The spies would immediately report Him to Roman Governor Pontius Pilate as a seditious rebel inciting a tax revolt against Caesar, carrying an immediate death penalty.

#### 2. The Silver Denarius Coin
Jesus asked for a denarius. By producing the Roman coin, His critics admitted they were already utilizing Caesar's currency in daily commerce.
- The silver denarius was stamped with the portrait of Emperor Tiberius Caesar and bore the Latin inscription: *"Tiberius Caesar, Divi Augusti Filius Augustus, Pontifex Maximus"* (Tiberius Caesar, Worshipful Son of the Divine Augustus, High Priest).
- The coin carried Caesar's **image** (*eikon*) and **inscription**, proving it belonged to the imperial monetary system.

#### 3. "Give to Caesar What Belongs to Caesar" (Civic Responsibility)
Because citizens benefit from public infrastructure, roads, defense, civil order, and legal systems maintained by the government, they have a legitimate moral obligation to pay taxes and support good governance (Romans 13:1-7). Civil authority is ordained by God to maintain justice and societal order.

#### 4. "Give to God What Belongs to God" (The Imago Dei)
Jesus elevated the discourse to profound spiritual truth:
- The coin bears Caesar's image, so pay Caesar his temporal tax.
- **Human beings bear the divine image of God** (Genesis 1:27: *Imago Dei*).
- Therefore, your soul, your conscience, your worship, your moral obedience, and your eternal destiny belong exclusively to God, not to any earthly emperor or state.""",
        "deep_dive": """### Deep Dive: Dual Citizenship and the Limits of Government Authority

#### The Concept of Dual Citizenship
The Christian lives with dual citizenship:
1. **Earthly Citizenship:** Obligating believers to be law-abiding, constructive members of society, paying taxes, voting responsibly, protecting public assets, and promoting national development.
2. **Heavenly Citizenship (Philippians 3:20):** Our supreme allegiance is to Jesus Christ.

#### When State Demands Conflict with God's Word
Earthly government authority is not absolute; it is delegated by God. If any government or ruler commands believers to violate God's moral commandments—such as forcing idol worship, lying, or persecuting the innocent—believers must obey God rather than human authorities (Acts 5:29: *"We must obey God rather than human beings!"*).""",
        "practical": {
            "title": "4-Step Framework for Responsible Civic and Spiritual Living",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Obey School and Civil Laws Diligently",
                    "description": "Follow school rules, traffic regulations, environmental protection laws, and safety guidelines faithfully without cutting corners."
                },
                {
                    "step_number": 2,
                    "title": "Protect and Respect Public Property",
                    "description": "Never participate in vandalism, school unrest, destruction of desks, or misuse of public amenities. Treat communal property with care."
                },
                {
                    "step_number": 3,
                    "title": "Practice Honesty in Financial Obligations",
                    "description": "When paying school fees, bus fare, or community dues, be transparent and honest. Shun tax evasion and fraudulent bribery."
                },
                {
                    "step_number": 4,
                    "title": "Give God Your Undivided Heart and Life",
                    "description": "Ensure your ultimate love, daily worship, prayer, and moral loyalty belong to God, resisting worldly pressures to compromise your faith."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenya, civic awareness and tax compliance are central to national development through the Kenya Revenue Authority (KRA):
- **Taxation and Public Services:** Taxes fund public schools, highways (such as the Nairobi Expressway and Thika Superhighway), hospitals, and national security. Jesus' teaching affirms that paying taxes is a biblical civic duty.
- **Youth Patriotism:** Kenyan students demonstrate patriotism by singing the National Anthem with respect, honoring the National Flag, keeping environments clean, and avoiding riots.
- **Integrity Against Corruption:** Christians must champion transparency, opposing the embezzlement of public funds and demanding that tax revenues are used fairly to benefit all citizens.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Patriotism, Honesty, and Divine Allegiance
- **Self-Examination:** Do you balance your duties as a student and citizen with your personal devotion and obedience to God?
- **Prayer of Dedication:** "Lord God Almighty, thank You for the nation of Kenya and my school community. Help me to be a law-abiding, honest, and patriotic citizen who respects public order. Above all, I surrender my soul and life to You, for I am created in Your divine image. In Jesus' name, Amen.\"""",
        "takeaways": [
            "Jesus' opponents attempted to trap Him with a question about Roman taxation to either alienate the crowd or have Him arrested by Rome.",
            "Jesus requested a silver denarius, pointing out that Caesar's image on the coin established Caesar's claim to temporal tax revenue.",
            "'Give to Caesar what belongs to Caesar' teaches that believers must fulfill civic duties, obey civil laws, and pay taxes (Romans 13:1-7).",
            "'Give to God what belongs to God' teaches that because humans are created in God's image (Genesis 1:27), our total devotion belongs to Him.",
            "Christians possess dual citizenship, honoring legitimate civil authority while maintaining supreme allegiance to the Kingdom of God."
        ],
        "mcq": {
            "question": "What core principle did Jesus establish by declaring: 'Give to Caesar what is Caesar's, and to God what is God's'?",
            "options": [
                "A) That Christians should completely withdraw from society and refuse to obey civil laws",
                "B) That believers have a civic duty to support government order (taxes) and a supreme spiritual duty to surrender their lives to God",
                "C) That Roman emperors had divine authority to dictate all religious doctrines in the Temple",
                "D) That physical coins have spiritual power to grant forgiveness of sins"
            ],
            "answer": "B",
            "explanation": "Jesus taught that believers have a dual responsibility: fulfilling legitimate civic duties (such as paying taxes to civil government) while giving their entire heart, soul, and moral devotion to God, whose image they bear."
        }
    },

    # ─── LESSON 5 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "The Question of the Resurrection",
        "unit_description": "Explores the Sadducees' theological skepticism regarding the resurrection (Luke 20:27-40), their hypothetical riddle about seven brothers and one widow, Jesus' revelation of the glorified angelic state, and God as the God of the living (Exodus 3:6).",
        "lesson_title": "The Question of the Resurrection",
        "image": {
            "title": "Julius Schnorr von Carolsfeld: Jesus Refutes the Sadducees",
            "caption": "19th-century biblical woodcut illustrating Jesus silencing the skeptical Sadducees with Scripture regarding the reality of the resurrection.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Die_Bibel_in_Bildern_%281860%29_illustration_p200.jpg/800px-Die_Bibel_in_Bildern_%281860%29_illustration_p200.jpg",
            "author": "Julius Schnorr von Carolsfeld",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_5,
        "youtube": {
            "title": "BibleProject: Eternal Life",
            "description": "A theological exploration of eternal life, the resurrection, and how God's divine life overcomes death and decay.",
            "youtube_id": "VbQk4UAwV28"
        },
        "goals": [
            "Contrast the theological beliefs of the Sadducees with biblical doctrine regarding the resurrection and afterlife.",
            "Explain how Jesus answered the Sadducees' marriage riddle by contrasting the mortal earthly order with the glorified heavenly state.",
            "Analyze Jesus' proof from Exodus 3:6 that God is 'the God of the living' and find Christian comfort regarding eternal life."
        ],
        "intro": """Have you ever encountered someone who tried to make your deepest beliefs look ridiculous by asking an extreme, far-fetched hypothetical riddle? For example, someone might ask: "If a computer gets struck by lightning while printing your homework, which button does the cloud press?" It is an exaggerated, absurd scenario meant to mock serious logic.

The Sadducees—the wealthy, aristocratic ruling class of Jerusalem—did not believe in angels, spirits, or life after death. They concocted an extreme story about a woman who married seven brothers sequentially, hoping to prove that belief in the resurrection was foolish nonsense. Let us examine how Jesus shattered their skepticism.""",
        "core_scripture": """### Luke 20:27-40 (NIV)
> "Some of the Sadducees, who say there is no resurrection, came to Jesus with a question. 'Teacher,' they said, 'Moses wrote for us that if a man’s brother dies and leaves a wife but no children, the man must marry the widow and raise up offspring for his brother. Now there were seven brothers. The first one married a woman and died childless. The second and then the third married her, and in the same way the seven died, leaving no children. Finally, the woman died too. Now then, at the resurrection whose wife will she be, since the seven were married to her?'
>
> Jesus replied, 'The people of this age marry and are given in marriage. But those who are considered worthy of taking part in the age to come and in the resurrection from the dead will neither marry nor be given in marriage, and they can no longer die; for they are like the angels. They are God’s children, since they are children of the resurrection.
>
> But in the account of the burning bush, even Moses showed that the dead rise, for he calls the Lord \"the God of Abraham, and the God of Isaac, and the God of Jacob.\" He is not the God of the dead, but of the living, for to him all are alive.'
>
> Some of the teachers of the law responded, 'Well said, teacher!' And no one dared to ask him any more questions.\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. Identity & Beliefs of the Sadducees
The Sadducees were the wealthy, politically connected priestly elite who controlled the Temple treasury and collaborated with Roman authorities.
- **Scriptural Canon:** They accepted only the five books of Moses (the Pentateuch / Torah) as authoritative Scripture, rejecting the Prophets and Writings.
- **Theological Skepticism:** They denied the resurrection of the body, life after death, rewards/punishments in eternity, and the existence of angels and spirits (Acts 23:8).

#### 2. The Levirate Marriage Law (Deuteronomy 25:5-6)
Under ancient Mosaic Law, if a married man died without producing a male heir, his brother was obligated to marry the widow (*levir* is Latin for brother-in-law). The firstborn son would carry the deceased brother's name to ensure his family name and ancestral land were not erased. The Sadducees used this law to construct their riddle about seven brothers.

#### 3. Jesus' Two-Fold Refutation
Jesus dismantled their argument completely on two foundational grounds:

##### A. Misunderstanding the Nature of Resurrected Life
The Sadducees assumed eternity is merely a continuation of physical, earthly biological mechanics.
- In this mortal age, marriage is necessary for procreation, companionship, and preserving the human race against death.
- In the age to come, resurrected saints **can no longer die**. They receive glorified, incorruptible bodies, becoming *isangeloi* ("like angels")—living in direct, perfect communion with God without need for physical marriage or procreation.

##### B. Scriptural Proof from the Pentateuch (Exodus 3:6)
Because the Sadducees only accepted Moses' books, Jesus quoted their own foundation: God's revelation at the Burning Bush.
- God declared to Moses: *"I AM the God of Abraham, the God of Isaac, and the God of Jacob"* (present tense, centuries after the patriarchs had physically died).
- God did not say "I *was* their God."
- Therefore, Abraham, Isaac, and Jacob were alive to God. God is not the God of decaying corpses, but the God of the living!""",
        "deep_dive": """### Deep Dive: The Greek Grammar of Divine Living (*Pantes Gar Auto Zosin*)

#### "For to Him All Are Alive"
In Luke 20:38, Jesus concludes with the profound theological axiom: *pantes gar auto zosin* ("for all live to Him"). From our limited earthly perspective, deceased patriarchs and believers have passed away into the grave. But from God's eternal perspective, physical death is merely a transition; their spirits exist actively in His glorious presence, awaiting bodily resurrection at the Last Day. This proved that the resurrection is rooted in God's eternal covenant faithfulness.""",
        "practical": {
            "title": "4-Step Framework for Living with Resurrection Hope",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Anchor Your Faith in Eternal Life",
                    "description": "Recognize that physical earthly existence is not the end of your story. Live with eternity in mind, investing in character, love, and godliness."
                },
                {
                    "step_number": 2,
                    "title": "Comfort Those Grieving the Loss of Loved Ones",
                    "description": "When family or classmates lose loved ones, offer comfort with the Christian hope that believers in Christ are alive in God's presence and will be resurrected."
                },
                {
                    "step_number": 3,
                    "title": "Overcome the Fear of Death and Trials",
                    "description": "Approach life's hardships, sickness, and dangers with courageous faith, knowing that Christ has conquered the power of death and the grave."
                },
                {
                    "step_number": 4,
                    "title": "Study God's Word Deeply to Avoid Error",
                    "description": "Ground yourself in biblical truth through personal reading, Sunday school, and Bible study, avoiding spiritual skepticism and theological misconceptions."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenyan communities, beliefs regarding death, ancestors, and the afterlife hold significant cultural importance:
- **Traditional African Perspectives and Christian Resurrection:** Many Kenyan communities traditionally believe in the "living dead" (ancestors whose memory is honored). Jesus' teaching provides ultimate clarity: God preserves the living souls of all who trust Him, guaranteeing a bodily resurrection in glory.
- **Bereavement and Hope in Families:** During funeral services in Kenya, the doctrine of the resurrection brings profound comfort and peace to grieving families, preventing despair and hopelessness.
- **Standing Firm Against Modern Skepticism:** Equipping youth to defend their Christian faith rationally when challenged by secular skepticism in academic and social circles.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Faith, Hope, and Eternal Assurance
- **Self-Examination:** Does your daily life reflect the reality that you are an eternal child of God and a child of the resurrection?
- **Prayer of Dedication:** "Lord God of Abraham, Isaac, and Jacob, You are the God of the living. Thank You for the blessed hope of the resurrection and eternal life in Christ Jesus. When I face grief, sickness, or uncertainty, anchor my heart in Your victory over death and teach me to live for Your eternal Kingdom. Amen.\"""",
        "takeaways": [
            "The Sadducees rejected the resurrection, angels, and spirits, attempting to mock eternal life with a riddle about seven brothers.",
            "Jesus explained that heavenly resurrected life is not a duplicate of earthly biological marriage; saints become like the angels and cannot die.",
            "Resurrected believers are God's children and children of the resurrection, endowed with incorruptible, glorified existence.",
            "Jesus proved the resurrection from Exodus 3:6, showing that God is the God of the living, for Abraham, Isaac, and Jacob are alive to Him.",
            "Christian hope is grounded in the reality of the resurrection, giving believers courage, comfort in grief, and eternal purpose."
        ],
        "mcq": {
            "question": "How did Jesus prove from the Pentateuch (Exodus 3:6) that the dead are raised?",
            "options": [
                "A) By performing an immediate miracle to physically summon Abraham and Moses into the Temple",
                "B) By pointing out that God told Moses at the burning bush 'I AM the God of Abraham, Isaac, and Jacob,' proving they are alive to Him",
                "C) By showing them an ancient Egyptian tomb inscription regarding the afterlife",
                "D) By arguing that Moses built seven altars for the seven deceased brothers"
            ],
            "answer": "B",
            "explanation": "Jesus quoted Exodus 3:6, where God declared at the burning bush that He IS (present tense) the God of Abraham, Isaac, and Jacob. Since God is not the God of the dead but of the living, the patriarchs are alive to Him, proving the reality of the resurrection."
        }
    },

    # ─── LESSON 6 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Scribes' Hypocrisy and the Widow's Two Copper Coins",
        "unit_description": "Contrasts the pride, ostentation, and exploitation of the Scribes (Luke 20:45-47) with the quiet, sacrificial generosity of the poor widow who gave her last two copper coins (Luke 21:1-4), exploring God's kingdom arithmetic.",
        "lesson_title": "Scribes' Hypocrisy and the Widow's Two Copper Coins",
        "image": {
            "title": "James Tissot: The Widow's Mite (Le Denier de la Veuve)",
            "caption": "Late 19th-century watercolor portraying the humble poor widow quietly dropping her two tiny copper coins into the Temple treasury trumpet.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Brooklyn_Museum_-_The_Widow%27s_Mite_%28Le_denier_de_la_veuve%29_-_James_Tissot.jpg/800px-Brooklyn_Museum_-_The_Widow%27s_Mite_%28Le_denier_de_la_veuve%29_-_James_Tissot.jpg",
            "author": "James Tissot",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_6,
        "youtube": {
            "title": "BibleProject: Generosity",
            "description": "An inspiring visual overview of biblical generosity, showing how God's abundant grace transforms how we share our resources.",
            "youtube_id": "62CliEkRCso"
        },
        "goals": [
            "Contrast the hypocritical behaviors of the Scribes with the sincere humility of the poor widow.",
            "Explain why Jesus declared that the poor widow gave 'more than all the others' using God's kingdom arithmetic.",
            "Practice quiet, sacrificial generosity with time, talents, and resources in daily school and family life."
        ],
        "intro": """Imagine your school organizes a charity fundraising drive to support an orphanage. A student from a very wealthy family casually pulls a 1,000-shilling note from a thick wallet of pocket money and tosses it into the collection box, laughing loudly to make sure everyone sees. Meanwhile, another student from a struggling family, who walked three kilometers to school to save their 20-shilling bus fare, quietly drops those 20 shillings into the box without a word.

Who gave more? In human mathematics, 1,000 is fifty times larger than 20. But in God's divine arithmetic, the 20 shillings represent a far greater sacrifice and love. Let us examine how Jesus observed this exact contrast in the Jerusalem Temple.""",
        "core_scripture": """### Luke 20:45-47 & Luke 21:1-4 (NIV)
> "While all the people were listening, Jesus said to his disciples, 'Beware of the teachers of the law. They like to walk around in flowing robes and love to be greeted with respect in the marketplaces and have the most important seats in the synagogues and the places of honor at banquets. They devour widows’ houses and for a show make long prayers. These men will be punished most severely.'
>
> As Jesus looked up, he saw the rich putting their gifts into the temple treasury. He also saw a poor widow put in two very small copper coins.
>
> 'Truly I tell you,' he said, 'this poor widow has put in more than all the others. All these people gave their gifts out of their wealth; but she out of her poverty put in all she had to live on.'\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. The Condemnation of the Scribes (Hypocrisy & Exploitation)
Scribes were the legal and religious scholars responsible for copying, interpreting, and teaching the Mosaic Law. Jesus exposed three fatal sins in their conduct:
- **Vanity & Ostentation:** They wore elaborate, long white linen robes (*stolai*) with elongated fringes to flaunt their status, seeking obsequious greetings in public squares.
- **Lust for Social Preeminence:** Demanding the prominent front seats in synagogues (facing the congregation) and head seats at banquets.
- **Greed & Exploitation ("Devour Widows' Houses"):** Under Jewish custom, scribes acted as legal guardians, estate trustees, and advisers for helpless widows. Corrupt scribes charged exorbitant legal fees or mismanaged widows' properties to enrich themselves, masking their theft with theatrical, lengthy public prayers.

#### 2. The Temple Treasury Setting
In the Court of Women stood thirteen trumpet-shaped bronze receptacles (*shofarot*) where worshippers deposited voluntary offerings and temple taxes. The rich tossed in large bags of gold and silver coins, producing loud clanging noises that drew public admiration.

#### 3. The Two Copper Coins (*Lepta*)
A poor widow stepped up unnoticed. She dropped in two *lepta* (the smallest Jewish copper coin in circulation, worth about 1/64th of a day's agricultural wage / a *denarius*).
- She could have kept one coin for a piece of bread and given the other.
- Instead, she gave both coins—surrendering her entire livelihood (*holon ton bion*).

#### 4. God's Divine Arithmetic
Jesus gathered His disciples to deliver a revolutionary kingdom principle:
- **The Rich:** Gave out of their *perisseuontos* (abundance/surplus). Their large gifts cost them nothing; their lifestyle, meals, and bank accounts were untouched.
- **The Widow:** Gave out of her *hystereseos* (poverty/deficiency). She gave sacrificially, exercising radical faith in God as her ultimate Provider.""",
        "deep_dive": """### Deep Dive: Cultural Vulnerability of Widows in the Ancient World

#### The Social Plight of First-Century Widows
In biblical antiquity, widows had no social safety net, pension system, or independent legal standing unless they had adult sons or an upright kinsman-redeemer. Losing a husband often plunged a woman into severe destitution, making her prey to dishonest landlords and corrupt estate managers.

In this context, the widow's gift was an extraordinary act of spiritual devotion. While corrupt religious leaders were devouring widows' houses, this faithful widow was offering her last coins to God's house, shaming the entire religious establishment.""",
        "practical": {
            "title": "4-Step Framework for Practicing Sincere and Sacrificial Generosity",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Give Sincerity Over Showmanship",
                    "description": "When contributing to church offerings, school charity drives, or helping a needy friend, do so quietly without boasting or seeking social media praise."
                },
                {
                    "step_number": 2,
                    "title": "Practice Sacrificial Giving with What You Have",
                    "description": "Never think you are too poor or young to make a difference. Share your snack, stationary, revision notes, or small pocket money cheerfully."
                },
                {
                    "step_number": 3,
                    "title": "Protect and Care for Vulnerable People",
                    "description": "Support orphans, widows, elderly neighbors, and struggling classmates by offering your physical energy, chores, and compassionate advocacy."
                },
                {
                    "step_number": 4,
                    "title": "Trust God as Your Ultimate Provider",
                    "description": "Cultivate a heart of faith that trusts God to provide for your daily needs, freeing you from hoarding and materialistic anxiety."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenya, the spirit of *Harambee* (community pulling together) and charitable fundraising is woven into daily life:
- **Sincere Harambee Giving:** In school fundraisers, medical harambees, and church projects, the value of a contribution is not judged solely by its monetary size, but by the heart and sacrifice behind it.
- **Protecting Widows' Property Rights:** Under Kenya's Succession Act and Constitution, disinheriting widows or grabbing their ancestral land is illegal and ungodly. Christian youth must champion the legal and moral protection of widows.
- **Authentic Discipleship in Schools:** Rejecting cliquish pride and ostentatious fashion competitions among students, valuing inner character and servant generosity above outward labels.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Sincerity, Sacrificial Generosity, and Humility
- **Self-Examination:** Do you give to others only when you have excess, or are you willing to give sacrificially of your time, energy, and resources to bless someone in need?
- **Prayer of Dedication:** "Lord Jesus, You saw and honored the widow's two copper coins. Cleanse my heart of pride, hypocrisy, and love of praise. Teach me to give sacrificially, to defend the vulnerable, and to place my absolute security in Your loving care. In Your precious name, Amen.\"""",
        "takeaways": [
            "Jesus severely rebuked the Scribes for their outward religious showmanship, love of prestige, and exploitation of vulnerable widows.",
            "The poor widow quietly deposited two tiny copper coins (lepta), representing her entire livelihood and total trust in God.",
            "God measures generosity not by the numerical size of the gift, but by the proportion of sacrifice and sincerity of the giver's heart.",
            "The wealthy gave easily from their surplus without cost, whereas the widow gave everything she had out of her poverty.",
            "True Christian discipleship is characterized by quiet generosity, humility, and active defense of the vulnerable in society."
        ],
        "mcq": {
            "question": "Why did Jesus declare that the poor widow put 'more than all the others' into the Temple treasury?",
            "options": [
                "A) Because her two copper coins were rare and valuable collector items",
                "B) Because she gave sacrificially out of her poverty, putting in all she had, while the wealthy gave easily from their surplus",
                "C) Because the priests had promised to give her a leadership position in the Temple",
                "D) Because she dropped the coins into all thirteen collection trumpets simultaneously"
            ],
            "answer": "B",
            "explanation": "Jesus taught that God measures generosity by the level of sacrifice and heart devotion rather than monetary quantity. The rich gave easily from their excess wealth without personal sacrifice, whereas the widow gave her entire livelihood in complete faith."
        }
    },

    # ─── LESSON 7 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 7,
        "unit_name": "Teachings on Eschatology and Signs of the End Times",
        "unit_description": "Defines eschatology, explores Jesus' Olivet Discourse predicting the historical destruction of the Jerusalem Temple (Luke 21:5-6), identifies the geopolitical, cosmic, and persecution signs of the end of the age (Luke 21:7-28), and outlines the posture of joyful endurance.",
        "lesson_title": "Teachings on Eschatology and Signs of the End Times",
        "image": {
            "title": "David Roberts: The Destruction of Jerusalem (1850)",
            "caption": "19th-century panoramic oil painting depicting the dramatic siege and destruction of Jerusalem and its Temple by Roman legions in 70 AD.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/David_Roberts_The_Destruction_of_Jerusalem_1850.jpg/800px-David_Roberts_The_Destruction_of_Jerusalem_1850.jpg",
            "author": "David Roberts",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_7,
        "youtube": {
            "title": "BibleProject: Day of the Lord",
            "description": "Explores the biblical concept of the 'Day of the Lord,' how God confronts human injustice, and the ultimate restoration of creation.",
            "youtube_id": "tEaT8G4720U"
        },
        "goals": [
            "Define the theological term 'eschatology' and state the context of Jesus' predictions regarding the Jerusalem Temple.",
            "Identify the geopolitical, natural, cosmic, and persecution signs of the end times outlined by Jesus in Luke 21.",
            "Formulate practical strategies for Christian students to maintain resilience, peace, and bold witness during times of global or personal crisis."
        ],
        "intro": """Have you ever read a thrilling novel or watched a suspenseful documentary where the story grows increasingly intense, chaotic, and dramatic as it approaches the final chapter? You eagerly ask: "How will this story end? What are the unmistakable signs that the climax is here?"

Human history is not an aimless, random cycle; it is a grand narrative written by God moving purposefully toward a glorious culmination. When Jesus sat in the Temple courts with His disciples, He pulled back the curtain on future history, revealing the signs of the end of the age to prepare His followers to stand firm. Let us explore His teachings on Eschatology.""",
        "core_scripture": """### Luke 21:5-28 (NIV)
> "Some of his disciples were remarking about how the temple was adorned with beautiful stones and with gifts dedicated to God. But Jesus said, 'As for what you see here, the time will come when not one stone will be left on another; every one of them will be thrown down.'
>
> 'Teacher,' they asked, 'when will these things happen? And what will be the sign that they are about to take place?'
>
> He replied: 'Watch out that you are not deceived. For many will come in my name, claiming, \"I am he,\" and, \"The time is near.\" Do not follow them. When you hear of wars and uprisings, do not be frightened. These things must happen first, but the end will not come right away.'
>
> Then he said to them: 'Nation will rise against nation, and kingdom against kingdom. There will be great earthquakes, famines and pestilences in various places, and fearful events and great signs from heaven.
>
> 'But before all this, they will seize you and persecute you. They will hand you over to synagogues and put you in prison, and you will be brought before kings and governors, and all on account of my name. And so you will bear testimony to me... By standing firm, you will win life.
>
> 'When you see Jerusalem being surrounded by armies, you will know that its desolation is near... There will be signs in the sun, moon and stars. On the earth, nations will be in anguish and perplexity at the roaring and tossing of the sea. People will faint from terror, apprehensive of what is coming on the world, for the heavenly bodies will be shaken.
>
> At that time they will see the Son of Man coming in a cloud with power and great glory. When these things begin to take place, stand up and lift up your heads, because your redemption is drawing near.'\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. Definition of Eschatology
- **Etymology:** Derived from two Greek words: *eschatos* (meaning "last," "final," or "end") and *logos* (meaning "study," "word," or "discourse").
- **Theological Definition:** The branch of Christian theology concerned with the final events of history, the second coming of Jesus Christ (*Parousia*), the resurrection of the dead, final judgment, and the eternal Kingdom of God.

#### 2. The Prophecy of the Temple's Demolition (70 AD)
The Second Temple, expanded by King Herod the Great, was one of the architectural wonders of the Greco-Roman world, built with massive polished white stones (some over 40 feet long) and overlaid with sheets of pure gold.
- Jesus shocked His disciples by predicting: *"Not one stone will be left on another."*
- This was fulfilled literally in August 70 AD when the Roman Tenth Legion besieged Jerusalem, set fire to the Temple, and dismantled its stones to salvage the melted gold.

#### 3. The Multi-Layered Signs of the End Times (Luke 21)
Jesus provided a comprehensive taxonomy of signs to prevent deception and panic:
1. **Spiritual Deception:** False messiahs, counterfeit prophets, and cult leaders claiming divine authority and setting false dates.
2. **Geopolitical Conflicts:** Wars, international rebellions, ethnic strife, and rumors of war (*"nation will rise against nation"*).
3. **Natural & Environmental Calamities:** Severe earthquakes, widespread famines, and deadly epidemics/pestilences across various regions.
4. **Persecution & Witness:** Believers handed over to courts, betrayed by relatives, and imprisoned, providing an opportunity to proclaim the Gospel with Spirit-given wisdom.
5. **Cosmic Disruptions & Terror:** Disturbances in the sun, moon, and stars, roaring seas, and nations paralyzed with fear.

#### 4. The Glorious Climax: Return of the Son of Man
History concludes not in nuclear disaster or cosmic oblivion, but in the triumphant return of Jesus Christ in a cloud with divine power and glory (fulfilling Daniel 7:13-14). Believers are commanded not to cower in fear, but to *"stand up and lift up your heads, because your redemption is drawing near!"*""",
        "deep_dive": """### Deep Dive: The Dual Horizon of Biblical Prophecy

#### The Prophetic Foreshortening Principle
In biblical prophecy, prophets often viewed near-term historical events and far-term end-time events through a single perspective (like looking at two distant mountain peaks aligned in a row):
1. **Near Horizon (70 AD):** The Roman siege of Jerusalem and the destruction of the physical Temple.
2. **Far Horizon (The End of the Age):** The global tribulations, cosmic signs, and the bodily return of Jesus Christ to judge the earth.
Understanding this dual horizon prevents Christians from confusing historical first-century fulfillments with the ultimate climax of human history.""",
        "practical": {
            "title": "4-Step Framework for Spiritual Resilience and Readiness",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Guard Against False Doctrines and Deception",
                    "description": "Refuse to follow self-proclaimed prophets or sensational social media cults predicting exact dates for the end of the world. Test every teaching with the Bible."
                },
                {
                    "step_number": 2,
                    "title": "Maintain Calm and Peace Amid Bad News",
                    "description": "When global news broadcasts report wars, economic inflation, or natural disasters, do not panic. Anchor your soul in Christ's sovereign control."
                },
                {
                    "step_number": 3,
                    "title": "Stand Firm for Christ Under Peer Pressure",
                    "description": "When mocked or pressured by classmates for your Christian moral stance, stand firm in faith. Use the moment as a courageous testimony for Christ."
                },
                {
                    "step_number": 4,
                    "title": "Share the Gospel of Hope Diligently",
                    "description": "Encourage discouraged friends, participate actively in Christian Union and church outreach, and live as an ambassador of God's Kingdom."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenya and across East Africa, end-times speculation and cultic movements have caused real-world harm (e.g., the tragic Shakahola cult incidents):
- **Discerning False Cults:** Jesus' clear warning—*"Watch out that you are not deceived; do not follow them"*—is crucial for Kenyan youth. Christians must avoid extremist groups that isolate believers or preach unbiblical end-time starvation.
- **Handling Climate and Economic Challenges:** Kenya frequently faces severe droughts in ASAL regions, flash floods, and economic inflation. Understanding biblical prophecy teaches students to respond with compassionate community relief and environmental stewardship rather than fatalism.
- **Standing for Moral Integrity:** Youth are challenged to be resilient lights in their schools, demonstrating honesty and peace even when societal standards decline.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Vigilance, Resilience, and Unshakable Faith
- **Self-Examination:** When you hear of global crises, conflicts, or trials, do you react with paralyzing fear or with the quiet confidence that Christ holds the future?
- **Prayer of Dedication:** "Lord Jesus Christ, King of history, thank You for forewarning us about the trials and signs of the end of the age. Grant me discernment to avoid deception, courage to stand firm for Your name under pressure, and joy as I look forward to Your glorious return. In Your holy name, Amen.\"""",
        "takeaways": [
            "Eschatology is the theological study of the end times, the return of Christ, resurrection, and the final establishment of God's Kingdom.",
            "Jesus accurately predicted the destruction of the Jerusalem Temple, which was fulfilled literally in 70 AD by Roman legions.",
            "Signs of the end times include spiritual deception, international wars, earthquakes, famines, plagues, and persecution of believers.",
            "Persecution provides believers with a divine opportunity to bear bold, Spirit-empowered testimony for Christ before authorities.",
            "Rather than living in terror of global crises, Christians are commanded to stand up and lift their heads in joyful anticipation of Christ's return."
        ],
        "mcq": {
            "question": "What is the meaning of the theological term 'eschatology'?",
            "options": [
                "A) The scientific study of ancient desert architecture and temple excavation",
                "B) The branch of Christian theology that studies the end times, final events of history, and the return of Jesus Christ",
                "C) The historical classification of Roman monetary systems and imperial taxation",
                "D) The biological study of plant seasons and fig tree agriculture"
            ],
            "answer": "B",
            "explanation": "Eschatology is derived from the Greek words 'eschatos' (last/end) and 'logos' (study), representing the theological study of the end times, the second coming of Christ, resurrection, final judgment, and eternal life."
        }
    },

    # ─── LESSON 8 ─────────────────────────────────────────────────────────────
    {
        "unit_order": 8,
        "unit_name": "The Parable of the Fig Tree and Watchfulness",
        "unit_description": "Explores the Parable of the Fig Tree (Luke 21:29-33), the eternal permanence of Christ's words, warnings against the traps of carousing, drunkenness, and worldly anxieties (Luke 21:34-38), and practical habits of constant prayer and watchfulness (1 Thessalonians 5:1-6).",
        "lesson_title": "The Parable of the Fig Tree and Watchfulness",
        "image": {
            "title": "James Tissot: The Lesson of the Fig Tree",
            "caption": "Late 19th-century watercolor portraying Jesus using the budding branches of a fig tree to teach His disciples about spiritual alertness and readiness.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Brooklyn_Museum_-_The_Lesson_of_the_Fig-tree_%28La_le%C3%A7on_du_figuier%29_-_James_Tissot.jpg/800px-Brooklyn_Museum_-_The_Lesson_of_the_Fig-tree_%28La_le%C3%A7on_du_figuier%29_-_James_Tissot.jpg",
            "author": "James Tissot",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "svg_fn": get_svg_lesson_8,
        "youtube": {
            "title": "BibleProject: Gospel of Luke (Chapters 19-24)",
            "description": "Visual overview of Jesus' final teachings, the Olivet Discourse on watchfulness, and the culmination of His Jerusalem ministry.",
            "youtube_id": "26z_KhwNqnM"
        },
        "goals": [
            "Explain the spiritual lesson of the Parable of the Fig Tree regarding discerning the signs of God's Kingdom.",
            "Identify the three spiritual traps that weigh down the human heart (carousing, drunkenness, and the anxieties of life) from Luke 21:34.",
            "Develop a concrete, daily routine of constant prayer, moral vigilance, and spiritual readiness in school and personal life."
        ],
        "intro": """Imagine your school principal announces on Monday morning that an official national inspection team from the Ministry of Education could walk into your classroom at any unannounced hour of any day this week to inspect your exercise books, check your uniform, and interview you about your academic progress.

What would you do? You would not wait until Friday evening to start tidying your desk, completing backlogged homework, and polishing your shoes. You would maintain clean notes, do your daily homework every evening, and arrive alert every single morning.

This proactive, continuous readiness is the exact attitude of **spiritual watchfulness** that Jesus Christ demands of all His disciples as we await His return. Let us explore His final parable and exhortation in the Jerusalem Temple.""",
        "core_scripture": """### Luke 21:29-38 (NIV)
> "He told them this parable: 'Look at the fig tree and all the trees. When they sprout leaves, you can see for yourselves and know that summer is near. Even so, when you see these things happening, you know that the kingdom of God is near.
>
> 'Truly I tell you, this generation will certainly not pass away until all these things have happened. Heaven and earth will pass away, but my words will never pass away.
>
> 'Be careful, or your hearts will be weighed down with carousing, drunkenness and the anxieties of life, and that day will close on you suddenly like a trap. For it will come on all those who live on the face of the whole earth.
>
> 'Be always on the watch, and pray that you may be able to escape all that is about to happen, and that you may be able to stand before the Son of Man.'
>
> Each day Jesus was teaching at the temple, and each evening he went out to spend the night on the hill called the Mount of Olives, and all the people came early in the morning to hear him at the temple.\"""",
        "theological_pillars": """### Theological Exegesis & Analysis

#### 1. The Parable of the Fig Tree: Discerning Seasons
In Palestine, most deciduous trees shed their leaves in winter. The fig tree is unique: its thick green leaves sprout late in the spring, signaling unmistakably that summer and harvest season are just around the corner.
- **Natural Discernment:** Anyone looking at budding green shoots knows summer is near without needing an expert to explain it.
- **Spiritual Application:** When believers witness the prophetic signs unfolding, they should know with certainty that God's Kingdom is actively advancing toward its final consummation.

#### 2. The Unshakable Permanence of Christ's Words
Jesus made a monumental divine declaration:
> *"Heaven and earth will pass away, but my words will never pass away."* (Luke 21:33)

Physical creation—the vast cosmos, earthly empires, mountains, and currencies—is temporary and subject to change. But Jesus' divine words, promises, and moral truths are eternal, unalterable, and utterly trustworthy.

#### 3. The Three Heart-Weighing Traps (Luke 21:34)
Jesus warns believers against three specific spiritual hazards that numb the soul:
1. **Carousing (*Kraipale*):** The reckless, dizzying pursuit of wild partying, sensual pleasure, and uncontrolled revelry.
2. **Drunkenness (*Methe*):** Substance abuse, alcohol, and drug dependence that dull moral sensitivity and cloud spiritual judgment.
3. **Anxieties of Life (*Merimnais Biotikais*):** Becoming so excessively consumed, worried, and obsessed with material status, money, exams, clothes, and worldly security that God is pushed out of the heart.

#### 4. The Spiritual Snare and Constant Prayer
A soul weighed down by these traps falls asleep spiritually, causing the Day of the Lord to snap shut like a hunter's sudden trap (*pagis*).
- **The Remedy:** *"Be always on the watch, and pray."* True watchfulness is not passive fear, but active daily prayer, righteous living, and joyful obedience, enabling believers to stand unashamed before the Son of Man (1 Thessalonians 5:1-6).""",
        "deep_dive": """### Deep Dive: Watchfulness (*Agrypneite*) and Daily Temple Ministry

#### The Meaning of Biblical Watchfulness (*Agrypneo*)
In the Greek text, Jesus commands: *agrypneite de en panti kairo deomenoi* ("be sleepless/alert at all times in prayer"). It portrays a faithful sentry stationed on city walls during the dark hours of night, scanning the horizon, keeping his eyes open, and communicating constantly with headquarters.

#### Jesus' Faithful Routine (Luke 21:37-38)
Luke concludes Topic 9 by showing Jesus' daily routine: He taught God's Word in the Temple courts all day, retreated to the Mount of Olives at night for communion with the Father, and crowds arrived early every morning to hear Him. Jesus practiced the very discipline and dedication He taught.""",
        "practical": {
            "title": "4-Step Framework for Practicing Daily Spiritual Watchfulness",
            "steps": [
                {
                    "step_number": 1,
                    "title": "Establish a Daily Morning Prayer Habit",
                    "description": "Begin each day by reading Scripture and praying for guidance, wisdom in your studies, and strength to resist temptation."
                },
                {
                    "step_number": 2,
                    "title": "Reject Substance Abuse and Wild Escapism",
                    "description": "Firmly refuse alcohol, drugs, miraa, or immoral parties that numb your conscience and destroy your future. Seek healthy, godly recreation."
                },
                {
                    "step_number": 3,
                    "title": "Cast Worldly Anxieties on God in Prayer",
                    "description": "When academic pressure or family worries build up, surrender them to God (1 Peter 5:7) rather than allowing anxiety to weigh down your heart."
                },
                {
                    "step_number": 4,
                    "title": "Live with Continuous Integrity and Love",
                    "description": "Perform your schoolwork, home chores, and relationships with excellence, living every day as if Jesus could return at any moment."
                }
            ]
        },
        "kenyan_context": """### Kenyan Real-World Context & Civic Integration

In Kenyan society, teenagers face numerous modern distractions and pressures that threaten spiritual alertness:
- **Substance Abuse and Youth Parties:** Alcoholism, shisha, bhang, and miraa abuse at teenage parties have derailed many young lives. Jesus' warning against drunkenness and carousing is a direct shield protecting Kenyan youth from destructive addictions.
- **Mental Health and Academic Anxiety:** Students facing high-stakes national assessments (such as CBC junior school assessments and KCSE) often experience paralyzing anxiety. Christ urges youth to replace panic with persistent prayer and healthy study habits.
- **Consistent Christian Witness:** Active participation in school Christian Union (C.U.), YCS, and community youth groups helps students remain spiritually vibrant and supportive of one another.""",
        "reflection": """### Spiritual Reflection & Core Values

- **Core Value:** Responsibility, Vigilance, and Faithfulness
- **Self-Examination:** Is your heart weighed down by worries about the future, peer pressure, or careless habits? What concrete step will you take today to awaken your spiritual life?
- **Prayer of Dedication:** "Lord Jesus, Your words will never pass away. Keep my heart awake, alert, and watchful. Protect me from the snares of substance abuse, wild pleasures, and worldly anxiety. Fill me with Your Holy Spirit so that I may walk in righteousness and stand joyfully before You on that great Day. Amen.\"""",
        "takeaways": [
            "The Parable of the Fig Tree teaches that believers can discern the arrival of God's Kingdom just as sprouting leaves signal summer.",
            "Jesus affirmed the eternal permanence of His divine words, declaring that heaven and earth will pass away, but His words will endure forever.",
            "Christ warned against three heart-weighing hazards: carousing (wild revelry), drunkenness (substance abuse), and the anxieties of life.",
            "Spiritual watchfulness involves continuous prayer and active moral obedience, preventing the Day of the Lord from snapping shut like a trap.",
            "Believers are called to live with daily faithfulness, integrity, and prayerful readiness, ready to stand unashamed before the Son of Man."
        ],
        "mcq": {
            "question": "According to Luke 21:34, which three things did Jesus warn could weigh down our hearts and catch us unprepared like a sudden trap?",
            "options": [
                "A) Studying hard for exams, eating nutritious meals, and planting fruit trees",
                "B) Carousing, drunkenness, and the anxieties/cares of this life",
                "C) Speaking foreign languages, traveling by boat, and building houses",
                "D) Reciting ancient Psalms, memorizing dates, and paying temple taxes"
            ],
            "answer": "B",
            "explanation": "In Luke 21:34, Jesus explicitly cautions: 'Be careful, or your hearts will be weighed down with carousing, drunkenness and the anxieties of life, and that day will close on you suddenly like a trap.'"
        }
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_topic9():
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: GRADE 9 CRE — TOPIC 9: JESUS' MINISTRY IN JERUSALEM")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Target Hierarchy
        curriculum = Curriculum.objects.get(id=5) # CBC
        grade = Grade.objects.get(id=18)          # Grade 9
        subject = Subject.objects.get(id=50, grade=grade) # CRE

        print(f"[✓] Target Hierarchy Verified: {curriculum.name} -> {grade.name} (ID: {grade.id}) -> {subject.name} (ID: {subject.id})")

        # 2. Get or Create Topic 9
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=9,
            defaults={
                "name": "Jesus' Ministry in Jerusalem",
                "description": "Details Jesus Christ's final public ministry in the holy city of Jerusalem, covering His triumphant entry, the cleansing of the Temple, major theological conflicts with Jewish authorities, the poor widow's offering, and His teachings on end times (Eschatology)."
            }
        )
        if not created:
            topic.name = "Jesus' Ministry in Jerusalem"
            topic.description = "Details Jesus Christ's final public ministry in the holy city of Jerusalem, covering His triumphant entry, the cleansing of the Temple, major theological conflicts with Jewish authorities, the poor widow's offering, and His teachings on end times (Eschatology)."
            topic.save()
            print(f"[✓] Updated existing Topic: Order {topic.order} — '{topic.name}' (ID: {topic.id})")
        else:
            print(f"[✓] Created Topic: Order {topic.order} — '{topic.name}' (ID: {topic.id})")

        # Clean existing units/lessons under topic 9 for clean idempotent rebuild
        existing_units = LearningUnit.objects.filter(topic=topic)
        for unit in existing_units:
            for lsn in unit.lessons.all():
                lsn.blocks.all().delete()
                lsn.assets.all().delete()
                lsn.delete()
            unit.delete()
        print("[✓] Cleared previous units and lessons under Topic 9 for clean idempotent rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 3. Ingest 8 Lessons
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
                    "topic_order": 9,
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
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_9_lesson_{u_order}.svg",
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
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 9:")
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
    ingest_grade9_cre_topic9()
