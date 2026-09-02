"""
VLearn CBC Grade 9 CRE — Topic 10: Jesus' Passion, Death and Resurrection
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 10: Jesus' Passion, Death and Resurrection (Order: 10)

8 Discrete Units / Published Lessons:
  1. Lesson 1: The Lord's Supper (The Last Supper) (Luke 22:7-23, 1 Corinthians 11:23-26)
  2. Lesson 2: Prayer and Agony at the Mount of Olives (Luke 22:39-46, Hebrews 5:7-8)
  3. Lesson 3: Betrayal, Arrest, and Peter's Denial (Luke 22:47-62)
  4. Lesson 4: The Trials of Jesus (Luke 22:66-71, Luke 23:1-25, Isaiah 53:7)
  5. Lesson 5: The Crucifixion and Death of Jesus (Luke 23:26-49)
  6. Lesson 6: The Burial of Jesus (Luke 23:50-56, Isaiah 53:9)
  7. Lesson 7: The Resurrection of Jesus and Witnesses (Luke 24:1-12, 1 Corinthians 15:3-8)
  8. Lesson 8: The Ascension and the Second Coming (Luke 24:50-53, Acts 1:9-11, 1 Thessalonians 4:16-17)

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
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|BIBLE VERSE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|COMPARISON TABLE)[^\]]*\]', '', text, flags=re.IGNORECASE)
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
    <linearGradient id="redGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">PASSOVER VS. THE LORD'S SUPPER: COVENANT TRANSFORMATION</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">From Ancient Sinai Deliverance to Eternal Universal Redemption in Christ</text>

  <!-- Left Box: Old Covenant Passover -->
  <g transform="translate(45, 90)">
    <rect width="330" height="300" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="330" height="36" rx="10" fill="url(#goldGrad1)"/>
    <text x="165" y="24" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">OLD COVENANT (PASSOVER)</text>

    <text x="20" y="65" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Historical Deliverance:</text>
    <text x="20" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Freed Israel from physical slavery in Egypt.</text>

    <text x="20" y="115" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sacrificial Blood:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Physical blood of unblemished yearling lamb.</text>

    <text x="20" y="165" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Core Protective Sign:</text>
    <text x="20" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Blood smeared on doorposts &amp; lintels.</text>

    <text x="20" y="215" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Scope &amp; Target Audience:</text>
    <text x="20" y="232" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Exclusively for the nation of Israel at Sinai.</text>

    <rect x="20" y="255" width="290" height="32" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="165" y="275" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">TEMPORAL &amp; NATIONAL DELIVERANCE</text>
  </g>

  <!-- Center Arrow / Transition -->
  <g transform="translate(385, 220)">
    <circle cx="15" cy="0" r="22" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="15" y="5" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">&#10140;</text>
  </g>

  <!-- Right Box: New Covenant Holy Communion -->
  <g transform="translate(425, 90)">
    <rect width="330" height="300" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="330" height="36" rx="10" fill="url(#redGrad1)"/>
    <text x="165" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">NEW COVENANT (LORD'S SUPPER)</text>

    <text x="20" y="65" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Deliverance:</text>
    <text x="20" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Frees all humankind from spiritual bondage of sin.</text>

    <text x="20" y="115" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sacrificial Blood:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Jesus Christ's own precious blood on Calvary.</text>

    <text x="20" y="165" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Core Sacramental Signs:</text>
    <text x="20" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Bread (His broken Body) &amp; Wine (His Blood).</text>

    <text x="20" y="215" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Scope &amp; Target Audience:</text>
    <text x="20" y="232" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Universal scope open to all who believe worldwide.</text>

    <rect x="20" y="255" width="290" height="32" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="165" y="275" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">ETERNAL &amp; UNIVERSAL REDEMPTION</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">LUKE 22:19-20: "THIS CUP IS THE NEW COVENANT IN MY BLOOD, WHICH IS POURED OUT FOR YOU"</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="emeraldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE AGONY AT GETHSEMANE: THE TRIUMPH OF OBEDIENCE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Analyzing the Clash Between Human Anguish and Total Divine Submission (Luke 22:39-46)</text>

  <!-- Box 1: Human Agony -->
  <g transform="translate(45, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#e11d48"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. AUTHENTIC AGONY</text>

    <text x="15" y="60" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Intense Dread:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Felt the crushing weight</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">of human sin &amp; cross.</text>

    <text x="15" y="120" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Hematidrosis:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Sweat fell like great drops</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">of blood under stress.</text>

    <text x="15" y="180" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• The Human Cry:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Father, if willing, take</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">this cup from me..."</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
    <text x="110" y="254" fill="#fda4af" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">True Human Reality</text>
  </g>

  <!-- Box 2: Divine Assistance & Watchfulness -->
  <g transform="translate(290, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="url(#blueGrad2)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. PRAYER &amp; WATCH</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Divine Strengthening:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">An angel appeared from</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">heaven to sustain Him.</text>

    <text x="15" y="120" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Sleeping Disciples:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Exhausted by grief,</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">failing to stay alert.</text>

    <text x="15" y="180" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Jesus' Warning:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Pray that you will not</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">fall into temptation."</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="110" y="254" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Spiritual Fortification</text>
  </g>

  <!-- Box 3: Total Submission -->
  <g transform="translate(535, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="url(#emeraldGrad2)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. SUPREME SUBMISSION</text>

    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Perfect Alignment:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"...yet not my will, but</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">yours be done."</text>

    <text x="15" y="120" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Loving Obedience:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Embraced the cup of</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">salvation for humanity.</text>

    <text x="15" y="180" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Model for Believers:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Trusting God through</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">unfathomable trials.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="110" y="254" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Victory in Surrender</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">HEBREWS 5:8: "ALTHOUGH HE WAS A SON, HE LEARNED OBEDIENCE FROM WHAT HE SUFFERED"</text>
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
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE NIGHT OF ARREST &amp; DENIAL: CONTRASTING RESPONSES</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Jesus' Nonviolent Grace vs. Judas' Traitorous Remorse vs. Peter's Restorative Repentance</text>

  <!-- 3 Main Pillars -->
  <!-- Pillar 1: Jesus & Non-Violence -->
  <g transform="translate(45, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">JESUS: PEACEFUL LORD</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Calm Surrender:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Confronted the mob with</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">dignity and calm authority.</text>

    <text x="15" y="120" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Rejected Violence:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Healed Malchus' ear when</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Peter struck with sword.</text>

    <text x="15" y="180" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Spiritual Kingdom:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Not established by force,</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">but by sacrificial love.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="110" y="254" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Non-Violent Grace</text>
  </g>

  <!-- Pillar 2: Judas' Betrayal & Despair -->
  <g transform="translate(290, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#b91c1c"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">JUDAS: THE TRAITOR</text>

    <text x="15" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Hypocritical Kiss:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Used a sign of affection</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">to identify Jesus to mob.</text>

    <text x="15" y="120" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Greed &amp; Deceit:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Sold his Master for</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">30 pieces of silver.</text>

    <text x="15" y="180" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• False Remorse:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Fell into self-focused guilt</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and despair without God.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="110" y="254" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Fatal Despair</text>
  </g>

  <!-- Pillar 3: Peter's Denial & True Repentance -->
  <g transform="translate(535, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">PETER: THE PENITENT</text>

    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Three Denials:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Overcome by fear by the</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">courtyard fire at dawn.</text>

    <text x="15" y="120" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• The Lord's Gaze:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Rooster crowed; Jesus turned</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and looked straight at him.</text>

    <text x="15" y="180" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Bitter Weeping &amp; Return:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Wept bitterly in genuine</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">repentance; fully restored.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="110" y="254" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Restorative Repentance</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">LUKE 22:61: "THE LORD TURNED AND LOOKED STRAIGHT AT PETER... AND HE WENT OUTSIDE AND WEPT BITTERLY"</text>
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

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE FOUR SEQUENTIAL TRIALS OF JESUS: LEGAL MAP</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">From Jewish Religious Accusation to Roman Political Injustice (Luke 22:66 - 23:25)</text>

  <!-- Stage 1: Sanhedrin -->
  <g transform="translate(30, 95)">
    <rect width="170" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#d97706"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. SANHEDRIN</text>

    <text x="10" y="58" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Jewish High Council</text>
    <text x="10" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Met at dawn.</text>

    <text x="10" y="100" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Religious Charge:</text>
    <text x="10" y="116" fill="#ef4444" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">BLASPHEMY</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Claimed to be the Son</text>
    <text x="10" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">of God and Messiah.</text>

    <rect x="10" y="225" width="150" height="38" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="85" y="242" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">RELIGIOUS VERDICT:</text>
    <text x="85" y="254" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Deserves Death (Torah)</text>
  </g>

  <!-- Arrow 1 -->
  <text x="212" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700">&#10140;</text>

  <!-- Stage 2: Pilate First Hearing -->
  <g transform="translate(225, 95)">
    <rect width="170" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#0284c7"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. PILATE (PART 1)</text>

    <text x="10" y="58" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Roman Governor</text>
    <text x="10" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Praetorium Palace.</text>

    <text x="10" y="100" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Political Charge:</text>
    <text x="10" y="116" fill="#ef4444" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">TREASON &amp; TAX REVOLT</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Claimed to be a king,</text>
    <text x="10" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">subverting Caesar.</text>

    <rect x="10" y="225" width="150" height="38" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="85" y="242" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">PILATE'S DECLARATION:</text>
    <text x="85" y="254" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"I find no fault in Him"</text>
  </g>

  <!-- Arrow 2 -->
  <text x="407" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700">&#10140;</text>

  <!-- Stage 3: Herod Antipas -->
  <g transform="translate(420, 95)">
    <rect width="170" height="280" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#7e22ce"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. HEROD ANTIPAS</text>

    <text x="10" y="58" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Ruler of Galilee</text>
    <text x="10" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Wanted miracle show.</text>

    <text x="10" y="100" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Jesus' Demeanor:</text>
    <text x="10" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Dignified silence.</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Mocked with royal robe</text>
    <text x="10" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">and sent back to Pilate.</text>

    <rect x="10" y="225" width="150" height="38" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="85" y="242" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">HEROD'S VERDICT:</text>
    <text x="85" y="254" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">No Charge, Mocked</text>
  </g>

  <!-- Arrow 3 -->
  <text x="602" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700">&#10140;</text>

  <!-- Stage 4: Pilate Sentencing -->
  <g transform="translate(615, 95)">
    <rect width="155" height="280" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="155" height="34" rx="10" fill="#b91c1c"/>
    <text x="77" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. SENTENCING</text>

    <text x="8" y="58" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Crowd Pressure</text>
    <text x="8" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Priests stirred mob.</text>

    <text x="8" y="100" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Barabbas Swapped:</text>
    <text x="8" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Murderer freed;</text>
    <text x="8" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Innocent condemned.</text>

    <rect x="8" y="225" width="139" height="38" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="77" y="242" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">FINAL SENTENCE:</text>
    <text x="77" y="254" fill="#ef4444" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">CRUCIFIXION</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">ISAIAH 53:7: "HE WAS OPPRESSED AND AFFLICTED, YET HE DID NOT OPEN HIS MOUTH"</text>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="redGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE CRUCIFIXION ON CALVARY: COSMIC SIGNS &amp; SAVING GRACE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Divine Mercy on the Cross and the Breaking of the Heavenly Barrier (Luke 23:26-49)</text>

  <!-- 3 Main Pillars -->
  <!-- Pillar 1: Words of Mercy -->
  <g transform="translate(45, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. WORDS OF MERCY</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Forgiving His Killers:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Father, forgive them, for</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">they know not what they do."</text>

    <text x="15" y="120" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Repentant Criminal:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Today you will be with</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">me in paradise."</text>

    <text x="15" y="180" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Final Surrender:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Father, into your hands</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">I commit my spirit."</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="110" y="254" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Triumph of Grace</text>
  </g>

  <!-- Pillar 2: Cosmic Signs -->
  <g transform="translate(290, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. COSMIC PHENOMENA</text>

    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Supernatural Darkness:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">From noon to 3:00 PM;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">creation mourning Creator.</text>

    <text x="15" y="120" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Torn Temple Veil:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Tore top to bottom;</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">opened direct access to God.</text>

    <text x="15" y="180" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Centurion Witness:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Certainly this was an</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">innocent, righteous man!"</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="110" y="254" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Divine Vindication</text>
  </g>

  <!-- Pillar 3: Theological Impact -->
  <g transform="translate(535, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="url(#redGrad5)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. ATONEMENT &amp; ACCESS</text>

    <text x="15" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Complete Atonement:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Paid the full debt of human</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">sin once and for all.</text>

    <text x="15" y="120" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Direct Communion:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">No human high priest</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">barrier between God &amp; man.</text>

    <text x="15" y="180" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Universal Invitation:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Gentiles &amp; Jews reconciled</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">into one holy people.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="110" y="254" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Redemption Sealed</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">LUKE 23:45: "AND THE SUN STOPPED SHINING. AND THE CURTAIN OF THE TEMPLE WAS TORN IN TWO"</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="slateGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE BURIAL OF JESUS &amp; PROPHETIC FULFILLMENT</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Courage of Joseph of Arimathea, Sabbath Rest, and Isaiah's Ancient Prediction</text>

  <!-- 3 Main Pillars -->
  <!-- Pillar 1: Joseph of Arimathea -->
  <g transform="translate(45, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. COURAGEOUS DISCIPLE</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Sanhedrin Member:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Noble counselor who did</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">not consent to crucifixion.</text>

    <text x="15" y="120" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Bold Request:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Approached Pilate openly</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">to claim Jesus' body.</text>

    <text x="15" y="180" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Personal Sacrificial Cost:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Gave his own newly hewn</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">rock-cut private tomb.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="110" y="254" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Bold Public Faith</text>
  </g>

  <!-- Pillar 2: Prophetic Fulfillment -->
  <g transform="translate(290, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. PROPHETIC FULFILLMENT</text>

    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Isaiah 53:9 Prophecy:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Assigned a grave with the</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">rich in his death..."</text>

    <text x="15" y="120" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Rock-Cut Sepulchre:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Unused tomb carved from</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">solid bedrock, sealed by stone.</text>

    <text x="15" y="180" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Indisputable Evidence:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Ensured no confusion with</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">any other human corpse.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="110" y="254" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Scripture Fulfilled</text>
  </g>

  <!-- Pillar 3: Faithful Women & Sabbath -->
  <g transform="translate(535, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. FAITHFUL DEVOTION</text>

    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Galilean Women:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Followed to the tomb and</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">observed where He lay.</text>

    <text x="15" y="120" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Spices &amp; Perfumes:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Prepared spices to honor</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and anoint His body.</text>

    <text x="15" y="180" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Sabbath Obedience:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Rested on the Sabbath in</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">reverent obedience to Law.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="110" y="254" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Devotion &amp; Obedience</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">LUKE 23:53: "THEN HE TOOK IT DOWN, WRAPPED IT IN LINEN CLOTH AND PLACED IT IN A TOMB CUT IN THE ROCK"</text>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE RESURRECTION &amp; WITNESSES: THE LIVING HOPE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Empty Tomb, Emmaus Revelation, and the Cornerstone of Christian Faith (Luke 24:1-49)</text>

  <!-- 3 Main Pillars -->
  <!-- Pillar 1: The Empty Tomb & First Witnesses -->
  <g transform="translate(45, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="url(#goldGrad7)"/>
    <text x="110" y="22" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. THE EMPTY TOMB</text>

    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Stone Rolled Away:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Early Sunday morning;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">tomb was wide open &amp; empty.</text>

    <text x="15" y="120" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Women First Evangelists:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Mary Magdalene &amp; Joanna;</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">first entrusted with good news.</text>

    <text x="15" y="180" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Angelic Proclamation:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Why look for the living</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">among the dead? He is risen!"</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="110" y="254" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Historical Reality</text>
  </g>

  <!-- Pillar 2: The Emmaus Road Encounter -->
  <g transform="translate(290, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. THE EMMAUS ROAD</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Despair to Scripture:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Two disciples walking;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Jesus explained prophecies.</text>

    <text x="15" y="120" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Burning Hearts:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Hearts burned within them</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">as He unfolded the Word.</text>

    <text x="15" y="180" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Breaking of Bread:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Eyes opened in fellowship;</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">ran back to tell the Eleven.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="110" y="254" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Sacramental Revelation</text>
  </g>

  <!-- Pillar 3: Glorified Physical Reality -->
  <g transform="translate(535, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. GLORIFIED REALITY</text>

    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Flesh &amp; Bones:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Showed hands and feet;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">proved He was not a ghost.</text>

    <text x="15" y="120" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Ate in Their Sight:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Ate broiled fish to establish</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">His physical resurrection.</text>

    <text x="15" y="180" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Christian Foundation:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Defeated death forever,</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">guaranteeing eternal life.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="110" y="254" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Foundation of Hope</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">1 CORINTHIANS 15:20: "BUT CHRIST HAS INDEED BEEN RAISED FROM THE DEAD, THE FIRSTFRUITS OF THOSE WHO HAVE FALLEN ASLEEP"</text>
</svg>"""


def get_svg_lesson_8():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cyanGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE ASCENSION, GREAT COMMISSION &amp; SECOND COMING</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">From the Mount of Olives to the Glorious Return: Living in Faithful Readiness (Acts 1:9-11)</text>

  <!-- 3 Main Pillars -->
  <!-- Pillar 1: The Ascension & Commission -->
  <g transform="translate(45, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="url(#cyanGrad8)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. THE ASCENSION</text>

    <text x="15" y="60" fill="#67e8f9" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Exaltation to Heaven:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Ascended from Bethany;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">seated at God's right hand.</text>

    <text x="15" y="120" fill="#67e8f9" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• The Great Commission:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Preach repentance &amp;</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">forgiveness to all nations.</text>

    <text x="15" y="180" fill="#67e8f9" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Promise of the Spirit:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Wait in Jerusalem for</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Holy Spirit's power.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="1"/>
    <text x="110" y="254" fill="#67e8f9" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Heavenly Exaltation</text>
  </g>

  <!-- Pillar 2: The Promised Second Coming -->
  <g transform="translate(290, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. THE PAROUSIA</text>

    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Angelic Guarantee:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Will come back in the same</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">way you saw Him go."</text>

    <text x="15" y="120" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Glorious Triumph:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Returning in majesty to</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">judge evil &amp; reign in glory.</text>

    <text x="15" y="180" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Eternal Home:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"I go to prepare a place</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">for you..." (John 14:2).</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="110" y="254" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Sure Blessed Hope</text>
  </g>

  <!-- Pillar 3: Active Preparation Today -->
  <g transform="translate(535, 95)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. READINESS &amp; STEWARDSHIP</text>

    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Holy Living:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Resisting temptation;</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">maintaining moral purity.</text>

    <text x="15" y="120" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Constant Repentance:</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Reconciling with others</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and keeping clean hearts.</text>

    <text x="15" y="180" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Active Witness:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Serving the needy, studying</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Word, and sharing Christ.</text>

    <rect x="15" y="235" width="190" height="30" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="110" y="254" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Faithful Diligence</text>
  </g>

  <text x="400" y="420" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">ACTS 1:11: "THIS SAME JESUS, WHO HAS BEEN TAKEN FROM YOU INTO HEAVEN, WILL COME BACK IN THE SAME WAY"</text>
</svg>"""


# ─── 8 LESSON DATA CONFIGURATIONS ─────────────────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "The Lord's Supper (The Last Supper)",
        "unit_description": "Analyze the historical context of the Last Supper, compare it with the Sinai Passover feast, and explain the spiritual significance of the New Covenant in the Holy Eucharist.",
        "lesson_title": "The Lord's Supper (The Last Supper)",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Leonardo_da_Vinci_-_The_Last_Supper_high_res.jpg/800px-Leonardo_da_Vinci_-_The_Last_Supper_high_res.jpg",
            "title": "Visual Hook: The Last Supper by Leonardo da Vinci",
            "author": "Leonardo da Vinci (1452–1519)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus sharing His final Passover meal with the Twelve Apostles in the Upper Room, instituting the New Covenant through the bread and wine."
        },
        "youtube": {
            "youtube_id": "G-2e9mMf7E8",
            "title": "BibleProject: Luke 22-24 — The Last Supper, Death, and Resurrection",
            "description": "An illustrated deep dive into Luke chapters 22 to 24, showing how Jesus transformed the ancient Passover meal into the inauguration of the New Covenant."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Explain the historical background of the Passover and how Jesus transformed it into the Lord's Supper (Luke 22:7-23).",
            "Contrast the Sinai Old Covenant with the New Covenant sealed in Christ's sacrificial blood.",
            "Demonstrate the values of repentance, thanksgiving, and spiritual preparation when participating in the Holy Eucharist today."
        ],
        "intro": "Have you ever participated in a special memorial family meal to remember an ancestor or a major national milestone? In many African and global cultures, sharing a sacred meal is the most intimate way to keep a memory alive.\n\nFor the Jewish people, the annual Passover meal was the ultimate memorial—reminding them of the night God miraculously delivered their ancestors from brutal Egyptian bondage. During His final night in Jerusalem, Jesus gathered His disciples in an Upper Room, took this well-known memorial feast, and transformed it into a brand-new, eternal covenant that Christians across the world celebrate every single week.",
        "core_scripture": "### Scriptural Passage: Luke 22:14-20 & 1 Corinthians 11:23-26\n\n#### Luke 22:14-20 — Institution of the Lord's Supper\n> *\"When the hour came, Jesus and his apostles reclined at the table. And he said to them, 'I have eagerly desired to eat this Passover with you before I suffer. For I tell you, I will not eat it again until it finds fulfillment in the kingdom of God.'\n> After taking the cup, he gave thanks and said, 'Take this and divide it among you. For I tell you I will not drink again from the fruit of the vine until the kingdom of God comes.'\n> And he took bread, gave thanks and broke it, and gave it to them, saying, 'This is my body given for you; do this in remembrance of me.'\n> In the same way, after the supper he took the cup, saying, 'This cup is the new covenant in my blood, which is poured out for you.'\"*\n\n#### 1 Corinthians 11:26 — Proclaiming His Death\n> *\"For whenever you eat this bread and drink this cup, you proclaim the Lord's death until he comes.\"*",
        "theological_pillars": "### Theological Exegesis & Analysis: From Shadow to Substance\n\n1. **The Passover Fulfillment:** In Exodus 12, unblemished lambs were slaughtered, and their blood on doorposts protected Israel from the angel of death. Jesus is the true, unblemished *Lamb of God* (John 1:29) whose sacrifice delivers humanity not from physical Egypt, but from the spiritual bondage of sin and eternal death.\n2. **The New Covenant (*Berith / Diatheke*):** The Old Covenant at Mount Sinai was sealed with the blood of sacrificed animals (Exodus 24:8). The New Covenant prophesied by Jeremiah (Jeremiah 31:31-34) was established and sealed once and for all by Jesus' own sacrificial blood on Calvary.\n3. **The Bread & The Wine:** \n   - **The Bread:** Symbolizes Jesus' physical body, given up and broken in suffering on the cross.\n   - **The Cup of Wine:** Symbolizes the blood of the New Covenant poured out for the remission of human sins.\n4. **Eucharist (Thanksgiving) & Anamnesis (Remembrance):** *Eucharist* is derived from the Greek *eucharisteo* (giving thanks). *Anamnesis* means active, living remembrance—not merely looking back at past history, but making the living reality of Christ's sacrifice present in our lives today.",
        "deep_dive": "### Deep Dive: Comparative Covenant Analysis\n\n| Dimension | The Sinai Passover (Old Covenant) | The Lord's Supper (New Covenant) |\n| :--- | :--- | :--- |\n| **Nature of Deliverance** | Delivered Israel from physical slavery in Egypt | Delivers all humankind from spiritual slavery to sin |\n| **Sacrificial Blood** | Blood of slaughtered yearling lambs and goats | The sinless blood of Jesus Christ on the cross |\n| **Core Memorial Sign** | Doorposts smeared with lamb's blood; unleavened bread | Broken bread (His body) and wine (His blood) |\n| **Scope & Accessibility** | Exclusive to the biological nation of Israel | Universal scope open to all tribes, nations, and peoples |\n| **Duration & Efficacy** | Repeated annually; pointed forward to the Messiah | Offered once for all; eternal efficacy and redemption |",
        "practical": {
            "title": "Action Framework: Approaching the Lord's Table with Integrity",
            "steps": [
                "Step 1: Self-Examination — Honestly examine your thoughts, motives, and recent conduct before God in prayer (1 Corinthians 11:28).",
                "Step 2: Sincere Repentance — Confess ungodly habits, secret disobedience, and harboring hatred, asking Christ for inward cleansing.",
                "Step 3: Reconciliation — Seek peace and forgive classmates, siblings, or friends who have wronged you before partaking.",
                "Step 4: Living Dedication — Step forward in faith, expressing heartfelt thanksgiving (Eucharist) and renewing your commitment to live like Christ daily."
            ]
        },
        "kenyan_context": "In Kenyan churches—whether Anglican, Catholic, PCEA, AIC, Methodist, or Pentecostal—Holy Communion (Eucharist) is celebrated as the highest communal sacrament. However, students sometimes treat Communion as a routine ritual or social spectacle. CBC learners are challenged to understand that partaking requires genuine moral integrity, reconciliation with peers at school, and living out Christ's love in the wider Kenyan society.",
        "reflection": "### Spiritual Reflection: The Lamb of God\n\nReflect on the words of Jesus: *'This is my body given for you.'*\n- When you observe or receive the bread and wine, do you view it as a mere tradition, or as a life-changing encounter with the boundless love of God?\n- Are there relationships in your school dormitory, classroom, or family that need healing before you come before God in worship?",
        "takeaways": [
            "Jesus instituted the Lord's Supper during the Jewish Passover, establishing the promised New Covenant in His own blood (Luke 22:19-20).",
            "The bread represents His broken body and the wine represents His blood shed for universal forgiveness of sins.",
            "The Lord's Supper replaces animal sacrifices, providing eternal spiritual deliverance for all humanity.",
            "Believers must approach the Holy Eucharist with self-examination, sincere repentance, and reconciliation with others."
        ],
        "mcq": {
            "question": "Why did Jesus replace the traditional Passover animal blood sacrifices with the bread and wine during the Last Supper?",
            "options": [
                "A) Animal sacrifices had become too expensive for the disciples to purchase in Jerusalem",
                "B) He instituted the New Covenant, sealing eternal redemption for all humanity through His own body and blood",
                "C) The Roman military authorities had forbidden animal slaughter in Judea",
                "D) The disciples forgot to prepare a lamb for the Passover evening"
            ],
            "answer": "B",
            "explanation": "In Luke 22:19-20 and 1 Corinthians 11:23-26, Jesus revealed that His own sacrifice on the cross fulfilled and replaced the Old Testament animal sacrifices, establishing the New Covenant for universal forgiveness."
        }
    },

    # ─── LESSON 2 ────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Prayer and Agony at the Mount of Olives",
        "unit_description": "Examine the events at Gethsemane on the Mount of Olives, analyzing Jesus' intense emotional agony, His submission to the Father's will, and the call to spiritual watchfulness.",
        "lesson_title": "Prayer and Agony at the Mount of Olives",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Carl_Heinrich_Bloch_-_Gethsemane.jpg/800px-Carl_Heinrich_Bloch_-_Gethsemane.jpg",
            "title": "Visual Hook: Christ in Gethsemane by Carl Bloch",
            "author": "Carl Heinrich Bloch (1834–1890)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus praying in profound anguish among the olive trees of Gethsemane, comforted and strengthened by an angel while submitting to the Father's will."
        },
        "youtube": {
            "youtube_id": "WuvUo_3r83s",
            "title": "BibleProject: The Gospel of Luke — Jesus' Journey to the Cross",
            "description": "An overview of Jesus' agonizing moments of prayer at the Mount of Olives and His resolute obedience to face suffering for human redemption."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Describe Jesus' prayer and emotional agony on the Mount of Olives (Luke 22:39-46).",
            "Analyze the theological meaning of 'the cup of suffering' and Jesus' absolute submission to God's will.",
            "Apply the principles of spiritual watchfulness, persistent prayer, and resilience when confronting severe personal trials."
        ],
        "intro": "Have you ever faced a looming crisis or heartbreaking situation that made your stomach twist in sheer dread? Perhaps it was a major national examination you felt unprepared for, the sudden illness of a parent, or facing the terrifying consequences of a mistake. In those moments of crushing anxiety, human instinct screams for an immediate escape.\n\nJesus Christ, in His authentic human nature, experienced this dread on a cosmic scale. Knowing the torture, betrayal, and spiritual weight of the cross that awaited Him in just hours, He did not run away or numb His feelings. Instead, He retreated to His favorite olive grove and poured out His soul to God in persistent, agonizing prayer.",
        "core_scripture": "### Scriptural Passage: Luke 22:39-46 & Hebrews 5:7-8\n\n#### Luke 22:39-46 — The Prayer of Surrender\n> *\"Jesus went out as usual to the Mount of Olives, and his disciples followed him. On reaching the place, he said to them, 'Pray that you will not fall into temptation.' He withdrew about a stone's throw beyond them, knelt down and prayed, 'Father, if you are willing, take this cup from me; yet not my will, but yours be done.'\n> An angel from heaven appeared to him and strengthened him. And being in anguish, he prayed more earnestly, and his sweat was like drops of blood falling to the ground.\n> When he rose from prayer and went back to the disciples, he found them asleep, exhausted from sorrow. 'Why are you sleeping?' he asked them. 'Get up and pray so that you will not fall into temptation.'\"*\n\n#### Hebrews 5:7-8 — Learning Obedience Through Suffering\n> *\"During the days of Jesus' life on earth, he offered up prayers and petitions with fervent cries and tears to the one who could save him from death, and he was heard because of his reverent submission. Son though he was, he learned obedience from what he suffered.\"*",
        "theological_pillars": "### Theological Exegesis: The Battle of the Will in Gethsemane\n\n1. **Gethsemane (*Gat-Shemanim*):** Meaning 'oil press' in Hebrew, this olive grove at the foot of the Mount of Olives became the place where Jesus was spiritually pressed under the crushing weight of impending judgment.\n2. **The Cup of Suffering:** In Old Testament prophetic literature (Isaiah 51:17, Jeremiah 25:15), the 'cup' symbolizes God's righteous wrath against human wickedness. Jesus was about to drink this bitter cup on behalf of sinful humanity.\n3. **Hematidrosis (Sweating Blood):** Luke, a physician, notes that Jesus' sweat became like drops of blood falling to the ground. Under severe psychological agony, capillary blood vessels in sweat glands can rupture, producing bloody perspiration.\n4. **Dual Nature of Christ:** Jesus' prayer reveals His complete humanity (shrinking from physical torment and spiritual separation) in perfect harmony with His divine obedience (*'not my will, but yours be done'*).\n5. **Spiritual Watchfulness vs. Human Frailty:** The disciples fell asleep due to emotional and physical exhaustion. Jesus warned that prayer is the only spiritual shield capable of preventing defeat when temptation strikes.",
        "deep_dive": "### Deep Dive: Three Lessons on Christian Prayer During Crisis\n\n- **Honest Lament:** Jesus did not pretend everything was fine. He openly expressed His anguish to the Father (*'Father, if you are willing, take this cup from me'*). Genuine Christian prayer welcomes raw honesty.\n- **Unconditional Submission:** Jesus ended His petition with absolute surrender (*'yet not my will, but yours be done'*). Spiritual victory is found not in bending God's will to ours, but in aligning our hearts with God's sovereign plan.\n- **Divine Strengthening:** God sent an angel to fortify Jesus in prayer. When believers seek God in crisis, He provides supernatural grace and fortitude to endure the trial.",
        "practical": {
            "title": "Action Framework: Overcoming Anxiety Through Persistent Prayer",
            "steps": [
                "Step 1: Create a Sacred Prayer Sanctuary — Establish a quiet, distraction-free environment to seek God when stress or grief strikes.",
                "Step 2: Pour Out Your Honest Burdens — Express your fears, anxieties, and struggles to God without masking your true feelings.",
                "Step 3: Pray the Prayer of Surrender — Consciously surrender your personal preferences by praying: 'Lord, not my will, but Yours be done.'",
                "Step 4: Cultivate Daily Watchfulness — Avoid spiritual laziness by maintaining consistent prayer and scripture reading before crises occur.",
            ]
        },
        "kenyan_context": "Kenyan secondary school students often encounter immense pressures—academic competition, financial hardships, peer rejection, or family conflicts. When overwhelmed, young people may be tempted to escape through substance abuse, silence, or giving up. Jesus' example in Gethsemane demonstrates that taking our deepest pain to God in prayer produces resilience, clarity, and divine strength to overcome life's greatest storms.",
        "reflection": "### Spiritual Reflection: Aligning Our Will with God\n\nReflect on the words: *'Yet not my will, but yours be done.'*\n- What personal desires or ambitions do you find hardest to surrender to God's guidance?\n- When facing a difficult challenge, do you tend to fall into spiritual slumber like the disciples, or do you rise and seek God's strength in prayer?",
        "takeaways": [
            "At the Mount of Olives (Gethsemane), Jesus experienced deep agony, sweating drops of blood as He faced the cross (Luke 22:44).",
            "The 'cup of suffering' represents bearing the weight of human sin and judgment on Calvary.",
            "Jesus modeled supreme submission by praying: 'Not my will, but yours be done' (Luke 22:42).",
            "Jesus commanded His disciples to watch and pray, showing that persistent prayer is vital to resist temptation."
        ],
        "mcq": {
            "question": "What does Jesus' prayer on the Mount of Olives ('Take this cup from me; yet not my will, but yours be done') reveal about His nature and character?",
            "options": [
                "A) He wanted to abandon His mission and return to Nazareth",
                "B) He had an authentic human nature that felt intense agony, perfectly surrendered in divine obedience to the Father's will",
                "C) He was teaching the disciples that prayer is unable to change anything",
                "D) He wished to prove that angels are more powerful than human beings"
            ],
            "answer": "B",
            "explanation": "Jesus' agonizing prayer highlights His genuine humanity (which recoiled from the horrific suffering of the cross) perfectly united with His complete, loving submission to God's redemption plan (Luke 22:42)."
        }
    },

    # ─── LESSON 3 ────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Betrayal, Arrest, and Peter's Denial",
        "unit_description": "Examine Judas Iscariot's betrayal, Jesus' non-violent arrest, Peter's threefold denial in the High Priest's courtyard, and the profound difference between remorse and true repentance.",
        "lesson_title": "Betrayal, Arrest, and Peter's Denial",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Caravaggio_-_Taking_of_Christ_-_Dublin.jpg/800px-Caravaggio_-_Taking_of_Christ_-_Dublin.jpg",
            "title": "Visual Hook: The Taking of Christ by Caravaggio",
            "author": "Caravaggio (1571–1610)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The dramatic moment of Jesus' arrest in Gethsemane as Judas identifies Him with a kiss while armed Temple guards move in."
        },
        "youtube": {
            "youtube_id": "V_bXQz7h6gA",
            "title": "BibleProject: Character Study of Peter — From Denial to Restoration",
            "description": "Explores Simon Peter's journey of discipleship, his catastrophic failure in the courtyard, and his restorative transformation by the risen Christ."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "Summarize the events surrounding Jesus' betrayal and arrest in Gethsemane (Luke 22:47-53).",
            "Analyze the causes and sequence of Peter's threefold denial in the High Priest's courtyard (Luke 22:54-62).",
            "Contrast the tragic despair of Judas with the genuine repentance and restoration of Peter."
        ],
        "intro": "Have you ever experienced the crushing pain of betrayal by someone you trusted implicitly—a close friend who exposed your secrets, or a teammate who abandoned you when trouble struck? Betrayal cuts deep into the human heart.\n\nImagine Jesus standing in the shadowy olive grove, looking into the eyes of Judas Iscariot—one of His chosen twelve disciples who had walked with Him for three years—only to receive a hypocritical kiss that sold Him for thirty pieces of silver. Moments later, Simon Peter, the boldest apostle, crumbled under the pressure of a servant girl's questions and swore that he never knew Jesus.",
        "core_scripture": "### Scriptural Passage: Luke 22:47-62\n\n#### Luke 22:47-51 — The Arrest and Rejection of Violence\n> *\"While he was still speaking a crowd came up, and the man who was called Judas, one of the Twelve, was leading them. He approached Jesus to kiss him, but Jesus asked him, 'Judas, are you betraying the Son of Man with a kiss?'\n> When Jesus' followers saw what was going to happen, they said, 'Lord, should we strike with our swords?' And one of them struck the servant of the high priest, cutting off his right ear.\n> But Jesus answered, 'No more of this!' And he touched the man's ear and healed him.\"*\n\n#### Luke 22:54-62 — Peter's Denial and the Lord's Look\n> *\"Then seizing him, they led him away and took him into the house of the high priest. Peter followed at a distance. And when some there had kindled a fire in the middle of the courtyard and had sat down together, Peter sat down with them. A servant girl saw him seated there in the firelight. She looked closely at him and said, 'This man was with him.'\n> But he denied it. 'Woman, I don't know him,' he said.\n> A little later someone else saw him and said, 'You also are one of them.'\n> 'Man, I am not!' Peter replied.\n> About an hour later another asserted, 'Certainly this fellow was with him, for he is a Galilean.'\n> Peter replied, 'Man, I don't know what you're talking about!' Just as he was speaking, the rooster crowed.\n> The Lord turned and looked straight at Peter. Then Peter remembered the word the Lord had spoken to him: 'Before the rooster crows today, you will disown me three times.' And he went outside and wept bitterly.\"*",
        "theological_pillars": "### Theological Exegesis: Betrayal, Denial, and the Grace of Repentance\n\n1. **The Traitor's Kiss:** Judas twisted a universal cultural sign of reverence, warmth, and brotherhood into an instrument of deceit and arrest. Jesus gently confronted his hypocrisy (*'Judas, are you betraying the Son of Man with a kiss?'*).\n2. **Rejection of Armed Resistance:** When Peter drew a sword and severed the ear of Malchus (the High Priest's servant), Jesus immediately intervened, healed the man, and commanded peace. Jesus rejected military messianism, declaring that God's kingdom overcomes darkness through sacrificial love, not physical violence (Matthew 26:52).\n3. **The Anatomy of Peter's Fall:** Peter's denial did not happen overnight; it followed a clear spiritual decline:\n   - *Overconfidence:* Boasting that he would never fall even if others did (Luke 22:33).\n   - *Prayerlessness:* Sleeping instead of watching and praying in Gethsemane.\n   - *Following at a Distance:* Keeping a safe compromise rather than standing openly with Jesus.\n   - *Sitting Among the Scorners:* Warming himself at the enemies' fire in the courtyard.\n4. **The Piercing Gaze of Jesus:** When the rooster crowed, Jesus turned and looked straight at Peter. This was not a look of hatred, but of brokenhearted love and prophetic reminder, which shattered Peter's self-deception and ignited true godly sorrow.",
        "deep_dive": "### Deep Dive: Judas vs. Peter — Remorse vs. Repentance\n\n| Character | Nature of Sorrow | Action Taken | Ultimate Outcome |\n| :--- | :--- | :--- | :--- |\n| **Judas Iscariot** | Worldly grief / Remorse | Threw money in temple; isolated himself in despair | Tragic suicide; spiritual ruin (Matthew 27:3-5) |\n| **Simon Peter** | Godly sorrow / True Repentance | Wept bitterly; returned to the fellowship of believers | Forgiven and restored as leader of the Church (John 21:15-19) |\n\n*Key Theological Principle:* Worldly grief leads to self-destruction and fatal despair, but godly sorrow produces repentance that leads to salvation without regret (2 Corinthians 7:10).",
        "practical": {
            "title": "Action Framework: Standing Firm Under Peer Pressure and Recovering from Failure",
            "steps": [
                "Step 1: Guard Against Spiritual Pride — Never boast about your moral strength; acknowledge your vulnerability and rely on God's grace daily.",
                "Step 2: Choose Your Associations Wisely — Avoid sitting comfortably among peer groups that mock God or pressure you to compromise your morals.",
                "Step 3: Respond to Godly Conviction — When you stumble or sin, do not make excuses; acknowledge your wrongdoing immediately.",
                "Step 4: Embrace God's Restorative Grace — Turn away from despair; seek God's forgiveness through sincere repentance and rebuild your integrity."
            ]
        },
        "kenyan_context": "In Kenyan schools and youth communities, peer pressure to compromise moral standards—such as cheating in exams, bullying junior students, engaging in substance abuse, or denying one's faith—is a daily reality. Peter's courtyard failure warns young people against the danger of 'following from a distance.' More importantly, Peter's restoration shows that a past mistake does not define one's future if one turns back to God in genuine repentance.",
        "reflection": "### Spiritual Reflection: When the Rooster Crows\n\nReflect on the moment Jesus looked at Peter:\n- Have you ever felt the 'crowing rooster' of your conscience after compromising your Christian values to fit in with friends?\n- When you make mistakes, do you react with pride and despair like Judas, or with humble, tearful repentance like Peter?",
        "takeaways": [
            "Judas betrayed Jesus with a hypocritical kiss, exchanging his Master for thirty silver coins (Luke 22:47-48).",
            "Jesus healed the High Priest's servant and rebuked the sword, firmly establishing a non-violent spiritual kingdom.",
            "Peter denied Jesus three times due to overconfidence, prayerlessness, and yielding to courtyard peer pressure (Luke 22:56-60).",
            "When the rooster crowed, Jesus looked at Peter, leading to bitter weeping and true repentance, unlike Judas' fatal despair."
        ],
        "mcq": {
            "question": "What is the crucial theological difference between Judas' remorse and Peter's reaction after denying Jesus?",
            "options": [
                "A) Judas wrote a letter of apology while Peter fled to Rome",
                "B) Judas fell into self-focused despair and ended his life, while Peter experienced godly sorrow that led to true repentance and restoration",
                "C) Peter was immediately rewarded with gold coins by the Sanhedrin",
                "D) Judas joined the Roman military while Peter remained in hiding permanently"
            ],
            "answer": "B",
            "explanation": "As 2 Corinthians 7:10 and the Gospels show, Judas experienced worldly remorse and despair that drove him to suicide, whereas Peter wept bitterly in godly repentance and was fully restored by Christ."
        }
    },

    # ─── LESSON 4 ────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "The Trials of Jesus",
        "unit_description": "Trace the sequential trials of Jesus through the Jewish Sanhedrin and Roman courts, examining the shifting accusations, Pilate's political compromise, and Jesus' blameless integrity.",
        "lesson_title": "The Trials of Jesus",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Antonio_Ciseri_-_Ecce_Homo.jpg/800px-Antonio_Ciseri_-_Ecce_Homo.jpg",
            "title": "Visual Hook: Ecce Homo by Antonio Ciseri",
            "author": "Antonio Ciseri (1821–1891)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Pontius Pilate presenting the beaten and crowned Jesus to the hostile Jerusalem crowd from his palace balcony, declaring 'Ecce Homo' (Behold the Man)."
        },
        "youtube": {
            "youtube_id": "XbXWqUj5T0E",
            "title": "BibleProject: The Trials and Crucifixion of Jesus",
            "description": "A comprehensive pedagogical breakdown of the legal and political dynamics behind Jesus' trials before the Sanhedrin, Pontius Pilate, and Herod Antipas."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Outline the four sequential stages of Jesus' trials before Jewish and Roman authorities (Luke 22:66 - 23:25).",
            "Identify the contrasting charges leveled against Jesus (religious blasphemy vs. political treason).",
            "Analyze how Pontius Pilate compromised justice for political expediency, and evaluate the importance of standing for truth today."
        ],
        "intro": "Have you ever been falsely accused of wrongdoing while the real offender walked away freely? Or have you seen a group of people gang up on an innocent classmate simply because a popular ringleader told them to? It feels infuriating and deeply unjust.\n\nOn the morning of Good Friday, the most catastrophic miscarriage of justice in human history took place. Jesus Christ, who was completely innocent and blameless, was dragged through four consecutive kangaroo court sessions. Even though Roman Governor Pontius Pilate repeatedly declared, 'I find no fault in this man,' political ambition and crowd pressure led him to sentence the Son of God to execution while releasing a violent murderer.",
        "core_scripture": "### Scriptural Passage: Luke 22:66 - 23:25 & Isaiah 53:7\n\n#### Luke 22:66-71 — Before the Sanhedrin\n> *\"At daybreak the council of the elders of the people, both the chief priests and the teachers of the law, met together, and Jesus was led before them. 'If you are the Messiah,' they said, 'tell us.'\n> Jesus answered, 'If I tell you, you will not believe me, and if I asked you, you would not answer. But from now on, the Son of Man will be seated at the right hand of the mighty God.'\n> They all asked, 'Are you then the Son of God?'\n> He replied, 'You say that I am.'\n> Then they said, 'Why do we need any more testimony? We have heard it from his own lips.'\"*\n\n#### Luke 23:1-4, 20-24 — Before Pontius Pilate\n> *\"Then the whole assembly rose and led him off to Pilate. And they began to accuse him, saying, 'We have found this man subverting our nation. He opposes payment of taxes to Caesar and claims to be Messiah, a king.'\n> So Pilate asked Jesus, 'Are you the king of the Jews?'\n> 'You have said so,' Jesus replied.\n> Then Pilate announced to the chief priests and the crowd, 'I find no basis for a charge against this man.' ...\n> Wanting to release Jesus, Pilate appealed to them again. But they kept shouting, 'Crucify him! Crucify him!' ... So Pilate decided to grant their demand. He released the man who had been thrown into prison for insurrection and murder, and surrendered Jesus to their will.\"*",
        "theological_pillars": "### Theological Exegesis: The Four Sequential Trials of Jesus\n\n1. **Trial 1: Before the Jewish Sanhedrin (Religious Court):**\n   - *Context:* The supreme 71-member Jewish council met at dawn.\n   - *Charge:* **Blasphemy** (claiming divinity and asserting He would sit at God's right hand).\n   - *Limitation:* Under Roman occupation (*Pax Romana*), the Sanhedrin lacked legal authority (*ius gladii*) to carry out capital punishment (John 18:31).\n2. **Trial 2: Before Pontius Pilate (First Roman Hearing):**\n   - *Shifting Accusation:* Because Pilate did not care about Jewish religious laws, the priests fabricated political charges of **Treason**, inciting tax revolt, and claiming to be a rival king against Caesar.\n   - *Declaration of Innocence:* After interrogating Jesus, Pilate publicly announced: *'I find no basis for a charge against this man.'*\n3. **Trial 3: Before Herod Antipas (Galilean Jurisdiction):**\n   - *Context:* Hearing Jesus was from Galilee, Pilate sent Him to Herod Antipas, who was in Jerusalem for the feast.\n   - *Outcome:* Herod treated Jesus like an entertainer, hoping to see a miracle. Jesus maintained majestic silence, fulfilling Isaiah 53:7. Herod's soldiers mocked Him with an elegant robe and returned Him.\n4. **Trial 4: Final Sentencing Before Pilate (The Great Compromise):**\n   - *The Barabbas Swap:* Pilate tried to release Jesus by offering an amnesty custom, but the incited crowd demanded the release of **Barabbas** (a convicted terrorist and murderer) and screamed for Jesus' crucifixion.\n   - *Moral Failure:* Pilate chose personal political survival and crowd-pleasing over truth, sentencing the innocent Jesus to death.",
        "deep_dive": "### Deep Dive: The Prophetic Typology of Barabbas\n\nThe exchange between Jesus and Barabbas provides a stunning picture of the Gospel:\n\n- **Barabbas' Reality:** A guilty rebel, murderer, and lawbreaker justly condemned to death on a Roman cross.\n- **Jesus' Reality:** The sinless, spotless Son of God who committed no crime and spoke no deceit.\n- **The Great Substitution:** The guilty criminal walked out of death row completely free, while the innocent Savior took his place on the wooden cross.\n- **Theological Message:** Barabbas represents all humanity. We are the guilty rebels deserving judgment, but Jesus took our place on the cross so that we might walk free into eternal life (2 Corinthians 5:21).",
        "practical": {
            "title": "Action Framework: Standing for Justice Against Mob Mentality",
            "steps": [
                "Step 1: Seek Objective Truth — Never jump to conclusions or spread gossip without verifying facts independently.",
                "Step 2: Resist Groupthink and Mob Pressure — Refuse to join in when a crowd of peers is mocking, scapegoating, or bullying someone.",
                "Step 3: Defend the Marginalized — Speak up boldly for classmates or community members who are unfairly accused or powerless.",
                "Step 4: Value Conscience Over Popularity — Choose integrity and righteousness, even if doing what is right costs you social popularity or status."
            ]
        },
        "kenyan_context": "In Kenya, the judicial system and governance structures face continuous challenges regarding corruption, political compromise, and public mob justice. Pontius Pilate stands as an eternal warning against leaders and citizens who compromise justice to protect their personal positions or appease popular opinion. CBC learners are trained to become leaders of integrity who champion the rule of law and stand up for the truth.",
        "reflection": "### Spiritual Reflection: Pilate's Washing of Hands\n\nPilate tried to wash his hands in a basin of water, claiming he was innocent of Jesus' blood.\n- Can physical rituals or making excuses ever absolve us of moral responsibility when we permit injustice?\n- When faced with peer pressure to join an unfair act at school, do you wash your hands like Pilate, or stand for righteousness like Christ?",
        "takeaways": [
            "Jesus underwent four successive trial hearings before the Sanhedrin, Pilate, Herod Antipas, and Pilate again (Luke 22:66 - 23:25).",
            "The religious leaders shifted their accusation from religious blasphemy to political treason to secure a Roman death sentence.",
            "Pilate declared Jesus innocent multiple times, yet condemned Him to death to appease the chanting mob.",
            "The release of guilty Barabbas in exchange for innocent Jesus illustrates the core Gospel doctrine of substitutionary atonement."
        ],
        "mcq": {
            "question": "Why did the Jewish leaders change their accusation against Jesus from 'blasphemy' in the Sanhedrin to 'treason' when they brought Him before Pontius Pilate?",
            "options": [
                "A) They realized blasphemy was not a sin under the Mosaic Law",
                "B) Roman authorities had no interest in Jewish religious debates, but punished political treason against Caesar with execution",
                "C) Pilate requested them to bring a military charge instead",
                "D) The high priest forgot the original religious accusation during the walk"
            ],
            "answer": "B",
            "explanation": "Pilate, as Roman Governor, would dismiss internal theological disputes (blasphemy), so the Jewish leaders fabricated political charges of tax evasion and rebellion against Caesar (Luke 23:2) to force a death sentence."
        }
    },

    # ─── LESSON 5 ────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "The Crucifixion and Death of Jesus",
        "unit_description": "Analyze the events of Mount Calvary, Jesus' seven last words, the cosmic signs that accompanied His death, and the theological doctrine of universal atonement.",
        "lesson_title": "The Crucifixion and Death of Jesus",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Christ_on_the_Cross_by_Rubens.jpg/800px-Christ_on_the_Cross_by_Rubens.jpg",
            "title": "Visual Hook: Christ on the Cross by Peter Paul Rubens",
            "author": "Peter Paul Rubens (1577–1640)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus hanging upon the cross on Mount Calvary between two criminals, surrounded by darkness and weeping faithful followers."
        },
        "youtube": {
            "youtube_id": "cI8m3k2gK1w",
            "title": "BibleProject: The Crucifixion and Atonement of Jesus",
            "description": "Explores how Jesus' sacrificial death on the cross serves as the ultimate act of divine love, breaking the power of evil and opening direct access to God."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Recount the events of Jesus' crucifixion on Golgotha / Calvary (Luke 23:26-49).",
            "Analyze the significance of Jesus' words from the cross and the cosmic signs accompanying His death.",
            "Explain the theological meaning of the torn temple veil and the Roman centurion's confession."
        ],
        "intro": "If you were unjustly condemned to the most painful execution known to history, what would your final words be? Bitterness? Rage? Curses against those who nailed you to the wood?\n\nAs Roman soldiers drove heavy iron spikes through Jesus' hands and feet at Golgotha, His first words were not a cry of revenge, but a prayer of boundless mercy: 'Father, forgive them, for they know not what they do.' On Mount Calvary, Jesus demonstrated that the love of God is infinitely stronger than human wickedness, transforming the cruelest instrument of Roman torture into the eternal symbol of salvation.",
        "core_scripture": "### Scriptural Passage: Luke 23:26-49\n\n#### Luke 23:32-43 — Forgiveness and Mercy on Calvary\n> *\"Two other men, both criminals, were also led out with him to be executed. When they came to the place called the Skull, they crucified him there, along with the criminals—one on his right, the other on his left. Jesus said, 'Father, forgive them, for they do not know what they are doing.' And they divided up his clothes by casting lots. ...\n> One of the criminals who hung there hurled insults at him: 'Aren't you the Messiah? Save yourself and us!'\n> But the other criminal rebuked him. 'Don't you fear God,' he said, 'since you are under the same sentence? We are punished justly, for we are getting what our deeds deserve. But this man has done nothing wrong.'\n> Then he said, 'Jesus, remember me when you come into your kingdom.'\n> Jesus answered him, 'Truly I tell you, today you will be with me in paradise.'\"*\n\n#### Luke 23:44-47 — The Cosmic Signs and Death\n> *\"It was now about noon, and darkness came over the whole land until three in the afternoon, for the sun stopped shining. And the curtain of the temple was torn in two. Jesus called out with a loud voice, 'Father, into your hands I commit my spirit.' When he had said this, he breathed his last.\n> The centurion, seeing what had happened, praised God and said, 'Surely this was a righteous man.'\"*",
        "theological_pillars": "### Theological Exegesis: The Seven Wonders of Calvary\n\n1. **Simon of Cyrene (The African Cross-Bearer):** An African from modern Libya was compelled by Roman soldiers to carry Jesus' heavy crossbeam (*patibulum*), symbolizing Africa's intimate participation in the journey of salvation.\n2. **The Repentant Criminal:** While one criminal mocked, the other showed genuine repentance—fearing God, acknowledging his personal guilt, declaring Jesus' innocence, and seeking mercy. Jesus granted him immediate assurance of salvation (*'Today you will be with me in paradise'*).\n3. **Supernatural Darkness (Noon to 3:00 PM):** An unprecedented darkness covered Judea for three hours, symbolizing God's judgment upon sin and creation in mourning as the Creator bore the sins of the world.\n4. **The Tearing of the Temple Veil:** The massive, sixty-foot-high woven curtain sealing off the Holy of Holies in the Jerusalem Temple tore in two from top to bottom (Matthew 27:51). This miraculous event proclaimed that through Christ's broken body, the barrier between God and humanity was abolished, granting every believer direct, unhindered access to God's presence (Hebrews 10:19-22).\n5. **The Centurion's Declaration:** The seasoned Roman executioner, moved by Jesus' forgiving spirit and the cosmic signs, praised God and declared, *'Surely this was a righteous man!'*—the first Gentile confession of Christ's innocence at the cross.",
        "deep_dive": "### Deep Dive: The Words of Grace from the Cross\n\nIn Luke's Gospel, Jesus' final utterances on the cross model perfect Christian discipleship:\n\n- **Unconditional Forgiveness:** Praying for His executioners and mockers (Luke 23:34).\n- **Boundless Mercy:** Welcoming the repentant thief into paradise at the eleventh hour (Luke 23:43).\n- **Complete Trust in the Father:** Committing His spirit into the Father's hands with His dying breath (Luke 23:46).\n\nChrist's death was not a defeat; it was the decisive victory over sin, Satan, and death—sealing the universal atonement (*katallage*) of all humankind.",
        "practical": {
            "title": "Action Framework: Living Out the Sacrificial Love of the Cross",
            "steps": [
                "Step 1: Extend Radical Forgiveness — Release grudges and bitterness against classmates, siblings, or friends who have hurt you deeply.",
                "Step 2: Pray for Those Who Mistreat You — Follow Jesus' model by praying for God's mercy on people who ridicule or oppose you.",
                "Step 3: Embrace Direct Fellowship with God — Approach God boldly in daily personal prayer without fear, knowing the temple veil is torn.",
                "Step 4: Offer Compassion to the Broken — Reach out to marginalized, struggling, or hurting individuals with the unconditional love of Christ."
            ]
        },
        "kenyan_context": "In Kenyan society, inter-personal disputes, tribal prejudices, and domestic conflicts often lead to cycles of revenge and broken relationships. The message of the Cross challenges Kenyan youth to break the cycle of vengeance through Christ-like forgiveness. When young people choose forgiveness over retaliation, they reflect the sacrificial love that healed humanity on Calvary.",
        "reflection": "### Spiritual Reflection: Direct Access to God\n\nReflect on the tearing of the temple veil:\n- You no longer need an earthly high priest or an animal sacrifice to speak with God. How often do you take advantage of this incredible privilege of direct prayer?\n- Is there someone in your life whom you need to forgive today, echoing Jesus' prayer: 'Father, forgive them'?",
        "takeaways": [
            "Jesus was crucified on Golgotha (Calvary) between two criminals, fulfilling the prophecy of being numbered with transgressors (Luke 23:33).",
            "Jesus demonstrated divine mercy by forgiving His executioners and welcoming the repentant thief into paradise (Luke 23:34, 43).",
            "Cosmic darkness fell from noon to 3 PM, and the temple veil tore from top to bottom, signifying direct access to God's presence for all believers.",
            "The Roman centurion declared Jesus righteous, marking the first Gentile witness to Christ's divine innocence at the cross."
        ],
        "mcq": {
            "question": "What was the profound theological significance of the temple veil tearing in two at the moment Jesus died?",
            "options": [
                "A) It indicated that the Jerusalem temple building was structurally unsound",
                "B) It proved that the Roman soldiers had vandalized the Holy of Holies",
                "C) It symbolized that the barrier of sin was destroyed, granting all believers direct, unhindered access to God's presence through Christ",
                "D) It meant that animal sacrifices would now be performed outside the city gates"
            ],
            "answer": "C",
            "explanation": "The tearing of the thick temple curtain from top to bottom (Luke 23:45, Hebrews 10:19-20) signified that Christ's sacrifice abolished the separation between God and humanity, opening direct access to God for everyone."
        }
    },

    # ─── LESSON 6 ────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "The Burial of Jesus",
        "unit_description": "Examine the details of Jesus' burial, the bold discipleship of Joseph of Arimathea, the faithful witness of the Galilean women, and the fulfillment of Isaiah's ancient prophecy.",
        "lesson_title": "The Burial of Jesus",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Caravaggio_-_The_Entombment_of_Christ.jpg/800px-Caravaggio_-_The_Entombment_of_Christ.jpg",
            "title": "Visual Hook: The Entombment of Christ by Caravaggio",
            "author": "Caravaggio (1571–1610)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Joseph of Arimathea, Nicodemus, and the faithful women reverently placing the body of Jesus into the new rock-cut tomb before the Sabbath sunset."
        },
        "youtube": {
            "youtube_id": "9mQk_4j4O28",
            "title": "BibleProject: Isaiah's Suffering Servant — Prophecy Fulfilled",
            "description": "Explores how Jesus' life, death, and honorable burial in a rich man's tomb directly fulfilled the prophetic portrait of Isaiah 53."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Describe the burial of Jesus by Joseph of Arimathea as recorded in Luke 23:50-56.",
            "Analyze how Jesus' burial in a wealthy man's tomb fulfilled the Messianic prophecy of Isaiah 53:9.",
            "Demonstrate the virtues of moral courage, generosity, and reverent devotion modeled by Joseph and the Galilean women."
        ],
        "intro": "Have you ever kept your faith, values, or talents secret because you were terrified of what your peers, classmates, or teachers might say? It takes immense courage to stand up and be counted when everyone around you is hostile.\n\nJoseph of Arimathea was a wealthy, highly respected member of the Jewish Sanhedrin. For months, he had been a secret disciple because he feared his colleagues. But the moment Jesus was crucified and died as a despised criminal, Joseph stepped into the light. Risking his political reputation, wealth, and status, he walked straight into the Roman Governor's palace and demanded the body of Jesus for an honorable burial.",
        "core_scripture": "### Scriptural Passage: Luke 23:50-56 & Isaiah 53:9\n\n#### Luke 23:50-56 — The Honorable Burial\n> *\"Now there was a man named Joseph, a member of the Council, a good and upright man, who had not consented to their decision and action. He came from the Judean town of Arimathea, and he himself was waiting for the kingdom of God. Going to Pilate, he asked for Jesus' body.\n> Then he took it down, wrapped it in linen cloth and placed it in a tomb cut in the rock, one in which no one had yet been laid. It was Preparation Day, and the Sabbath was about to begin.\n> The women who had come with Jesus from Galilee followed Joseph and saw the tomb and how his body was laid in it. Then they went home and prepared spices and perfumes. But they rested on the Sabbath in obedience to the commandment.\"*\n\n#### Isaiah 53:9 — Prophecy of the Rich Man's Tomb\n> *\"He was assigned a grave with the wicked, and with the rich in his death, though he had done no violence, nor was any deceit in his mouth.\"*",
        "theological_pillars": "### Theological Exegesis: The Significance of the Burial\n\n1. **The Courage of Joseph of Arimathea:**\n   - *High Sanhedrin Status:* Joseph was an elite member of the 71-member supreme council. He had refused to consent to their unlawful plot against Jesus.\n   - *Public Identification:* By asking Pilate for the corpse of a condemned rebel, Joseph risked being branded a traitor to Rome and an outcast by the Sanhedrin.\n   - *Generous Sacrifice:* He donated his personal, brand-new family tomb cut out of solid rock, along with costly fine linen.\n2. **Prophetic Fulfillment (Isaiah 53:9):** Seven centuries before Christ, Isaiah prophesied that the Messiah would be 'assigned a grave with the wicked' (executed between thieves) but would be 'with the rich in his death' (buried in a wealthy counselor's private tomb).\n3. **Indisputable Historical Proof:**\n   - *The Brand-New Tomb:* The tomb was cut into solid limestone bedrock and had never held any other corpse. This eliminated any possibility of body confusion or mistaken identity later.\n   - *The Galilean Women as Witnesses:* Mary Magdalene and other women followed, carefully noting the exact tomb and how the body was placed, establishing eyewitness confirmation of His genuine physical death.\n4. **Reverent Sabbath Rest:** The women prepared spices and perfumes to perfume His body, but halted their work at Friday sunset to rest on the Sabbath in faithful obedience to God's fourth commandment.",
        "deep_dive": "### Deep Dive: Historical & Legal Significance of the Burial\n\nUnder Roman law, executed criminals were typically thrown into a communal mass pit (*polyandrion*) or left on the cross for scavengers. By intervening before sunset:\n\n- **Prevented Desecration:** Joseph ensured that the body of the Lord received a dignified, holy burial in accordance with Jewish law (Deuteronomy 21:22-23).\n- **Established the Empty Tomb Reality:** Because the tomb was an identifiable, private rock-cut cave sealed with a massive rolling stone and guarded, the subsequent fact of its absolute emptiness on Sunday morning was incontrovertible proof of bodily resurrection.",
        "practical": {
            "title": "Action Framework: Using Your Resources and Influence for God's Kingdom",
            "steps": [
                "Step 1: Step Out of the Shadows — Stop hiding your Christian convictions; let your peers and teachers know where you stand for truth.",
                "Step 2: Dedicate Your Resources to God — Follow Joseph's generosity by using your time, pocket money, or talents to support church and community welfare.",
                "Step 3: Stand with the Marginalized — Show kindness and honor to individuals whom others despise, reject, or ignore.",
                "Step 4: Practice Faithful Obedience — Like the Galilean women, remain faithful to God's commandments in all circumstances."
            ]
        },
        "kenyan_context": "In Kenyan cultural traditions, funeral and burial rites are considered sacred communal obligations where family and friends show ultimate respect to the deceased. Joseph of Arimathea's noble act resonates deeply with African values of dignity, family honor, and hospitality. CBC learners are encouraged to use their family resources, leadership status, and courage to serve God and care for the vulnerable in their schools and communities.",
        "reflection": "### Spiritual Reflection: Stepping Up When it Counts\n\nReflect on the transformation of Joseph of Arimathea:\n- Joseph was silent for a long time, but when the moment of greatest crisis arrived, he took a bold stand for Christ.\n- Are you willing to use your social standing, talents, or resources to honor God when others are mocking Christian values?",
        "takeaways": [
            "Joseph of Arimathea, a respected Sanhedrin member, courageously requested Jesus' body from Pilate for an honorable burial (Luke 23:50-52).",
            "Jesus was wrapped in fine linen and placed in a brand-new rock-cut tomb where no one had ever been laid, fulfilling Isaiah 53:9.",
            "The Galilean women observed the exact burial location, establishing reliable eyewitness proof of Jesus' death.",
            "The women prepared spices and perfumes but rested on the Sabbath in obedience to the Law, demonstrating faithful devotion."
        ],
        "mcq": {
            "question": "How did Jesus' burial in Joseph of Arimathea's new rock-cut tomb confirm the indisputable reality of His resurrection?",
            "options": [
                "A) It allowed Roman guards to secretly replace the body during the night",
                "B) Because the unused rock-cut tomb had never held another body, there was zero possibility of confusing Jesus' body with anyone else when the tomb was found empty",
                "C) It showed that Joseph of Arimathea had greater political authority than Pontius Pilate",
                "D) It allowed the disciples to construct secret tunnels under Jerusalem"
            ],
            "answer": "B",
            "explanation": "Luke 23:53 specifies that the tomb was carved from solid rock and had never been used before, providing airtight physical and legal evidence that the empty tomb on Sunday morning was genuinely Christ's empty grave."
        }
    },

    # ─── LESSON 7 ────────────────────────────────────────────────────────────
    {
        "unit_order": 7,
        "unit_name": "The Resurrection of Jesus and Witnesses",
        "unit_description": "Explore the historical reality of the Resurrection, analyze encounters with the risen Christ, explain the chosen role of women as first witnesses, and affirm the cornerstone of Christian hope.",
        "lesson_title": "The Resurrection of Jesus and Witnesses",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Piero_della_Francesca_-_Resurrection_-_Sansepolcro.jpg/800px-Piero_della_Francesca_-_Resurrection_-_Sansepolcro.jpg",
            "title": "Visual Hook: The Resurrection by Piero della Francesca",
            "author": "Piero della Francesca (1415–1492)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The victorious risen Christ stepping forth from the tomb with the banner of victory, surrounded by sleeping Roman soldiers."
        },
        "youtube": {
            "youtube_id": "35o-8Xl6gZs",
            "title": "BibleProject: The Resurrection of Jesus",
            "description": "An inspiring animated exploration of Jesus' bodily resurrection, its validation of His divine identity, and the hope of new creation for all believers."
        },
        "svg_fn": get_svg_lesson_7,
        "goals": [
            "Narrate the events of the Resurrection morning and the discovery of the empty tomb (Luke 24:1-12).",
            "Explain the theological significance of women being chosen as the first witnesses and apostolic messengers.",
            "Analyze the Emmaus road encounter (Luke 24:13-35) and explain why the Resurrection is the cornerstone of Christian faith (1 Corinthians 15:3-8, 14-20)."
        ],
        "intro": "Imagine you had the most world-changing, destiny-shattering news in human history—news that conquered the finality of the grave and guaranteed eternal life. Who would you choose to carry that message to the world? A Roman Emperor? A high priest? A famous philosopher?\n\nIn first-century Jewish society, women were marginalized and legally disqualified from giving testimony in a court of law. Yet God completely turned human pride upside down. On early Sunday morning, God bypassed the imperial palaces of Rome and the religious elite of Jerusalem, entrusting the greatest announcement of all time—'He is not here; He has risen!'—to a devoted group of faithful women.",
        "core_scripture": "### Scriptural Passage: Luke 24:1-12 & 1 Corinthians 15:3-8, 20\n\n#### Luke 24:1-9 — The Empty Tomb and Angelic Proclamation\n> *\"On the first day of the week, very early in the morning, the women took the spices they had prepared and went to the tomb. They found the stone rolled away from the tomb, but when they entered, they did not find the body of the Lord Jesus. While they were wondering about this, suddenly two men in clothes that gleamed like lightning stood beside them.\n> In their fright the women bowed down with their faces to the ground, but the men said to them, 'Why do you look for the living among the dead? He is not here; he has risen! Remember how he told you, while he was still with you in Galilee: \"The Son of Man must be delivered over to the hands of sinners, be crucified and on the third day be raised again.\"' Then they remembered his words.\n> When they came back from the tomb, they told all these things to the Eleven and to all the others.\"*\n\n#### 1 Corinthians 15:3-4, 20 — The Cornerstone of Faith\n> *\"For what I received I passed on to you as of first importance: that Christ died for our sins according to the Scriptures, that he was buried, that he was raised on the third day according to the Scriptures. ... But Christ has indeed been raised from the dead, the firstfruits of those who have fallen asleep.\"*",
        "theological_pillars": "### Theological Exegesis: The Triumph of the Resurrected Lord\n\n1. **The Historical Fact of the Empty Tomb:** On the third day (Sunday morning), the massive stone was rolled away. The grave was empty, containing only the folded linen cloths (Luke 24:12), proving that Jesus' body was not stolen or moved, but resurrected.\n2. **Women as First Evangelists (*Apostolae Apostolorum*):** Mary Magdalene, Joanna, Mary the mother of James, and other women were the first to encounter the empty tomb and angelic messengers. Their selection is powerful historical evidence for the authenticity of the Gospels, as no fabricated first-century legend would invent female witnesses as primary testifiers.\n3. **The Emmaus Road Encounter (Luke 24:13-35):** Jesus joined two despondent disciples walking to Emmaus, explaining how all Old Testament prophecies pointed to the Messiah's suffering and glory. Their hearts 'burned within them,' and their eyes were opened during the **breaking of the bread**.\n4. **The Glorified Physical Body:** When Jesus appeared to the terrified Eleven in Jerusalem (Luke 24:36-43), He proved He was not a disembodied ghost. He invited them to touch His nail-pierced hands and feet, declaring: *'A ghost does not have flesh and bones, as you see I have,'* and ate broiled fish in their presence.\n5. **The Cornerstone of Christian Hope:** As St. Paul declared, if Christ has not been raised, Christian preaching is useless and faith is futile (1 Corinthians 15:14). The Resurrection is God's final victory over sin, satanic power, and physical death.",
        "deep_dive": "### Deep Dive: Theological Implications of the Resurrection\n\n- **Vindication of Jesus' Identity:** Proved conclusively that Jesus is the divine Son of God and that all His teachings and promises are true.\n- **Guarantee of Forgiveness & Justification:** Confirmed that God accepted Christ's sacrifice on Calvary as full payment for human sin (Romans 4:25).\n- **The Firstfruits of Eternal Life:** Christ's bodily resurrection is the guarantee (*firstfruits*) that all believers who die in faith will also experience bodily resurrection into eternal glory (1 Corinthians 15:20-23).",
        "practical": {
            "title": "Action Framework: Living in the Power of the Resurrection",
            "steps": [
                "Step 1: Anchor Your Hope in the Living Christ — Overcome despair and grief, knowing that death has been defeated forever.",
                "Step 2: Encounter Christ in Scripture and Fellowship — Open your heart to the Word of God daily so your heart burns with spiritual truth.",
                "Step 3: Honor the Dignity and Voice of All Believers — Follow God's example by respecting and empowering everyone, regardless of gender or social standing.",
                "Step 4: Proclaim the Good News Joyfully — Share the message of Christ's victory, hope, and forgiveness with your classmates and community."
            ]
        },
        "kenyan_context": "In many African communities, death is traditionally viewed with deep terror and finality. The Christian proclamation of the Resurrection completely transforms how Kenyan Christians face death, bereavement, and terminal sickness. Because Christ lives, Christian funerals are filled with hope and triumphant hymns, reassuring believers that physical death is merely a doorway into eternal fellowship with God.",
        "reflection": "### Spiritual Reflection: 'Why Look for the Living Among the Dead?'\n\nReflect on the angelic question:\n- Are you searching for lasting joy, purpose, and peace in dead things (such as fleeting peer popularity, worldly materialism, or sinful habits)?\n- How does the reality that Jesus is alive right now give you courage to face your daily fears and anxieties?",
        "takeaways": [
            "Jesus physically rose from the dead on the third day (Sunday morning), leaving the tomb completely empty (Luke 24:1-6).",
            "God chose faithful women as the first witnesses and apostolic heralds of the Resurrection.",
            "On the road to Emmaus, Jesus illuminated the scriptures and revealed Himself in the breaking of bread (Luke 24:30-32).",
            "Jesus proved His physical resurrection by showing His hands and feet and eating fish, validating the Christian hope of eternal life."
        ],
        "mcq": {
            "question": "Why is the physical resurrection of Jesus Christ considered the absolute 'foundation' of the entire Christian faith?",
            "options": [
                "A) Without the resurrection, Jesus would be merely a dead moral teacher, and Christian faith and hope of eternal life would be futile",
                "B) It allowed the apostles to overthrow the Roman garrison in Jerusalem by physical force",
                "C) It proved that the disciples were superior philosophers compared to the Greeks",
                "D) It provided a legal justification for establishing Sunday as a national holiday"
            ],
            "answer": "A",
            "explanation": "As 1 Corinthians 15:14-20 and Christian theology teach, without the resurrection, faith is futile and believers remain dead in sin; the resurrection confirms Jesus' divinity, validates His sacrifice, and guarantees eternal life."
        }
    },

    # ─── LESSON 8 ────────────────────────────────────────────────────────────
    {
        "unit_order": 8,
        "unit_name": "The Ascension and the Second Coming",
        "unit_description": "Examine the physical ascension of Jesus Christ into heaven, His Great Commission to the Church, and the blessed hope and practical preparation for His promised Second Coming.",
        "lesson_title": "The Ascension and the Second Coming",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/The_Ascension_by_John_Singleton_Copley.jpg/800px-The_Ascension_by_John_Singleton_Copley.jpg",
            "title": "Visual Hook: The Ascension by John Singleton Copley",
            "author": "John Singleton Copley (1738–1815)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The risen Lord Jesus ascending into heaven from the Mount of Olives while blessing His disciples, who watch in worship and awe."
        },
        "youtube": {
            "youtube_id": "H4cWvT7t738",
            "title": "BibleProject: Acts 1-7 — The Ascension and the Holy Spirit",
            "description": "An overview of Jesus' ascension, the promise of His return, and the commissioning of believers to be His witnesses to the ends of the earth."
        },
        "svg_fn": get_svg_lesson_8,
        "goals": [
            "Describe the event of Jesus' Ascension into heaven from the Mount of Olives near Bethany (Luke 24:50-53, Acts 1:9-11).",
            "Explain the meaning and theological significance of the Great Commission and the Second Coming (*Parousia*).",
            "List and apply practical, actionable ways a Christian youth can live in faithful preparation for eternity today."
        ],
        "intro": "Imagine your parents are traveling abroad for an entire year on a crucial work assignment. Before leaving, they hand you the keys to the family home, give you a clear list of responsibilities, and promise: 'We will return on a day you least expect. Manage the home with excellence, take care of your siblings, and do your best.' Would you spend the year partying and neglecting your studies, or living with diligent responsibility?\n\nJesus' departure at the Ascension is our ultimate commissioning. Forty days after His resurrection, Jesus blessed His disciples, ascended into heaven in a cloud of glory, and left His Church with a universal mission and an unbreakable promise: 'I will return in the same way you have seen me go.' How should we live as faithful stewards in the meantime?",
        "core_scripture": "### Scriptural Passages: Luke 24:50-53, Acts 1:9-11 & 1 Thessalonians 4:16-17\n\n#### Luke 24:50-53 — The Blessing and Ascension\n> *\"When he had led them out to the vicinity of Bethany, he lifted up his hands and blessed them. While he was blessing them, he left them and was taken up into heaven. Then they worshiped him and returned to Jerusalem with great joy. And they stayed continually at the temple, praising God.\"*\n\n#### Acts 1:9-11 — The Promise of Return\n> *\"After he said this, he was taken up before their very eyes, and a cloud hid him from their sight. They were looking intently up into the sky as he was going, when suddenly two men dressed in white stood beside them. 'Men of Galilee,' they said, 'why do you stand here looking into the sky? This same Jesus, who has been taken from you into heaven, will come back in the same way you have seen him go into heaven.'\"*\n\n#### 1 Thessalonians 4:16-17 — The Glorious Return\n> *\"For the Lord himself will come down from heaven, with a loud command, with the voice of the archangel and with the trumpet call of God, and the dead in Christ will rise first.\"*",
        "theological_pillars": "### Theological Exegesis: Exaltation, Mission, and Parousia\n\n1. **The Ascension (*Analepsis*):** Forty days after the resurrection, Jesus led the Eleven to Bethany on the Mount of Olives. He physically ascended into heaven, marking the transition from His earthly, localized ministry to His exalted, universal reign at the right hand of God the Father (Psalm 110:1, Ephesians 1:20-22).\n2. **The Great Commission & Holy Spirit Promise:** Before ascending, Jesus commanded His followers not to disperse, but to wait in Jerusalem for the baptism of the Holy Spirit (Acts 1:8). The Spirit would empower them to be bold witnesses in Jerusalem, Judea, Samaria, and to the ends of the earth.\n3. **The Second Coming (*Parousia*):** The Greek term *Parousia* signifies the royal arrival and visible appearance of the King. The angels in white declared that Christ's return will be personal, visible, and glorious—returning to judge the living and the dead and establish God's eternal Kingdom (Revelation 1:7).\n4. **Eternal Intercession:** In heaven today, Jesus acts as our Great High Priest and eternal Advocate, interceding continuously before the Father on behalf of believers (Hebrews 7:25, 1 John 2:1).\n5. **Living in Constant Watchfulness:** Because neither the angels nor humanity knows the day or hour of Christ's return (Matthew 24:36), Christians are called to live not in passive fear, but in active, joyful holiness and diligent stewardship.",
        "deep_dive": "### Deep Dive: Five Pillars of Youth Preparation for the Second Coming\n\n1. **Cultivate Moral Holiness:** Actively flee sexual immorality, dishonesty, and peer pressure, keeping one's heart and life pure before God (1 John 3:2-3).\n2. **Practice Continuous Repentance:** Maintain short accounts with God by promptly confessing sins and receiving His cleansing grace.\n3. **Forgive and Reconcile Promptly:** Live in peace with family members, classmates, and neighbors, harboring no malice or bitterness.\n4. **Be an Active Christian Witness:** Share the love and truth of Christ through good deeds, academic diligence, and evangelism (Matthew 28:19-20).\n5. **Anchor in God's Word & Prayer:** Build a daily habit of Bible study and intercession, growing in spiritual maturity and discernment.",
        "practical": {
            "title": "Action Framework: Diligent Daily Stewardship for Eternity",
            "steps": [
                "Step 1: Manage Time Responsibly — Treat each day as a gift from God; avoid wasting precious hours on unproductive digital addictions or gossip.",
                "Step 2: Strive for Academic and Moral Excellence — Work diligently in your studies and duties as unto the Lord, demonstrating Christian integrity.",
                "Step 3: Serve the Marginalized — Share your resources and time with the needy, orphans, and struggling peers in your community (Matthew 25:35-40).",
                "Step 4: Keep an Eternal Perspective — Face worldly trials with joyful confidence, knowing that Christ is preparing an eternal home for you (John 14:1-3)."
            ]
        },
        "kenyan_context": "In Kenyan schools, churches, and youth groups, discussions on the end times (Eschatology) can sometimes lead to confusion or passive fear. Christian Religious Education emphasizes that preparing for Christ's return is about active, faithful living today—working hard in school, rejecting corruption, conserving the environment, and living as upright Kenyan citizens who bring glory to God.",
        "reflection": "### Spiritual Reflection: 'Why Stand Looking into the Sky?'\n\nReflect on the angelic rebuke to the apostles:\n- The angels reminded the disciples that their calling was not to stare passively into the clouds, but to get to work sharing the Gospel.\n- How are you actively using your talents, voice, and youthful energy to serve Christ and prepare for His glorious return?",
        "takeaways": [
            "Jesus physically ascended into heaven from the Mount of Olives near Bethany, exalted to the right hand of God (Luke 24:50-51).",
            "The Great Commission commands believers to preach repentance and forgiveness to all nations in the power of the Holy Spirit (Acts 1:8).",
            "The angels promised that Jesus will return visibly and gloriously in the Second Coming (Parousia) to judge evil and establish His Kingdom (Acts 1:11).",
            "Believers prepare for eternity through moral holiness, daily repentance, active witness, and diligent stewardship of time and talents."
        ],
        "mcq": {
            "question": "What comfort and practical motivation does Jesus' promised return (Second Coming) give to a Christian youth facing hardships today?",
            "options": [
                "A) It encourages believers to stop attending school and wait passively on mountain peaks",
                "B) It assures believers that earthly suffering is temporary, motivating them to live faithfully, uprightly, and diligently as stewards of Christ's Kingdom",
                "C) It promises that Christians will automatically become wealthy and exempt from physical sickness in this life",
                "D) It suggests that moral choices and ethical behavior do not matter"
            ],
            "answer": "B",
            "explanation": "The promise of Christ's return (John 14:1-3, Acts 1:11, Titus 2:12-13) provides ultimate hope that suffering has an expiration date, inspiring believers to live holy, active, and productive lives in joyful anticipation."
        }
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_topic10():
    print("=" * 80)
    print("VLEARN CBC GRADE 9 CRE — TOPIC 10 INGESTION ENGINE")
    print("Topic: Jesus' Passion, Death and Resurrection")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Curriculum
        curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
        if not curriculum:
            curriculum = Curriculum.objects.first()
        if not curriculum:
            raise RuntimeError("Curriculum not found in database.")
        print(f"[+] Curriculum resolved: {curriculum.name} (ID: {curriculum.id})")

        # 2. Resolve Grade 9 (ID: 18)
        grade = Grade.objects.filter(id=18).first()
        if not grade:
            grade = Grade.objects.filter(curriculum=curriculum, level=9).first()
        if not grade:
            raise RuntimeError("Grade 9 (ID: 18) not found in database.")
        print(f"[+] Grade resolved: {grade.name} (ID: {grade.id}, Level: {grade.level})")

        # 3. Resolve Subject CRE (ID: 50)
        subject = Subject.objects.filter(id=50).first()
        if not subject:
            subject = Subject.objects.filter(grade=grade, name__icontains="CRE").first()
        if not subject:
            raise RuntimeError("Subject CRE (ID: 50) not found in database.")
        print(f"[+] Subject resolved: {subject.name} (ID: {subject.id})")

        # 4. Resolve / Create Topic 10
        topic_name = "Jesus' Passion, Death and Resurrection"
        topic = Topic.objects.filter(subject=subject, order=10).first()
        if not topic:
            topic = Topic.objects.filter(subject=subject, name__icontains="Passion").first()

        if not topic:
            topic = Topic.objects.create(
                subject=subject,
                order=10,
                name=topic_name,
                description=(
                    "Explore the dramatic culmination of Jesus Christ's earthly mission: "
                    "His Last Supper, agony in Gethsemane, trials, crucifixion, burial, "
                    "glorious resurrection, ascension, and promised Second Coming."
                )
            )
            print(f"[+] Created Topic: Order {topic.order} — {topic.name} (ID: {topic.id})")
        else:
            topic.name = topic_name
            topic.order = 10
            topic.description = (
                "Explore the dramatic culmination of Jesus Christ's earthly mission: "
                "His Last Supper, agony in Gethsemane, trials, crucifixion, burial, "
                "glorious resurrection, ascension, and promised Second Coming."
            )
            topic.save()
            print(f"[+] Updated Topic: Order {topic.order} — {topic.name} (ID: {topic.id})")

        # 5. Clear previous units/lessons under this topic to ensure clean, idempotent ingestion
        existing_units = LearningUnit.objects.filter(topic=topic)
        unit_count = existing_units.count()
        if unit_count > 0:
            print(f"[-] Cleaning up {unit_count} existing LearningUnit(s) under Topic {topic.id}...")
            existing_units.delete()

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 6. Ingest 8 Lessons
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
                    "topic_order": 10,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "author": "VLearn Grade 9 CRE Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            total_lessons += 1

            # ───────────────────────────────────────────────────────────────────
            # CREATE 3 LESSON ASSETS
            # ───────────────────────────────────────────────────────────────────
            # Asset 1: Wikimedia Historical Artwork Image
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

            # Asset 2: Custom Pedagogical Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_10_lesson_{u_order}.svg",
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
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 10:")
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
    ingest_grade9_cre_topic10()
