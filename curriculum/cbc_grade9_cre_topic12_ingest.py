"""
VLearn CBC Grade 9 CRE — Topic 12: The Gifts of the Holy Spirit
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 12: The Gifts of the Holy Spirit (Order: 12)

8 Discrete Units / Published Lessons:
  1. Lesson 1: Jesus' Teachings on the Role of the Holy Spirit (John 14:15-26, John 16:7-15)
  2. Lesson 2: Introduction to the Spiritual Gifts (1 Corinthians 12:1-11, Romans 12:3-8)
  3. Lesson 3: The Nine Gifts of the Holy Spirit (1 Corinthians 12:7-11)
  4. Lesson 4: Classification of the Spiritual Gifts (Revelation, Power, Utterance)
  5. Lesson 5: The Supremacy of Love (1 Corinthians 13:1-13)
  6. Lesson 6: Detecting False Teachings and Ungodly Cults (1 John 4:1-6, Matthew 7:15-20)
  7. Lesson 7: Criteria for Discerning Spiritual Manifestations (Galatians 5:22-23, 1 Thessalonians 5:19-22)
  8. Lesson 8: Proper Use and Misuse of Spiritual Gifts (1 Corinthians 14:26-40)

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
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|BIBLE VERSE)[^\]]*\]', '', text, flags=re.IGNORECASE)
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
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ROLES OF THE HOLY SPIRIT (THE PARACLETE)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">John 14:15-26 &amp; John 16:7-15 — Fivefold Ministry in the Believer's Life</text>

  <!-- Central Hub: The Paraclete -->
  <circle cx="400" cy="235" r="55" fill="url(#goldGrad1)" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="230" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE PARACLETE</text>
  <text x="400" y="246" fill="#1e293b" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">(Advocate/Helper)</text>

  <!-- 5 Surrounding Role Nodes -->
  <!-- 1. Teacher -->
  <line x1="400" y1="180" x2="400" y2="125" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(280, 85)">
    <rect width="240" height="42" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="120" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. Personal Teacher &amp; Guide</text>
  </g>

  <!-- 2. Spiritual Reminder -->
  <line x1="445" y1="200" x2="580" y2="145" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(560, 125)">
    <rect width="210" height="42" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="105" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. Spiritual Reminder</text>
  </g>

  <!-- 3. Convicts of Sin &amp; Righteousness -->
  <line x1="440" y1="270" x2="560" y2="310" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(540, 290)">
    <rect width="230" height="42" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="115" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. Internal Moral Convictor</text>
  </g>

  <!-- 4. Empowers for Witnessing -->
  <line x1="360" y1="270" x2="240" y2="310" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(30, 290)">
    <rect width="230" height="42" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="115" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. Empowers for Witnessing</text>
  </g>

  <!-- 5. Counselor &amp; Comforter -->
  <line x1="355" y1="200" x2="220" y2="145" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(30, 125)">
    <rect width="210" height="42" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="105" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">5. Counselor &amp; Comforter</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"He will teach you all things and bring to your remembrance all that I said" (John 14:26)</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE BODY OF CHRIST &amp; SPIRITUAL GIFTS (CHARISMATA)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Corinthians 12:1-11 — Diversity of Gifts, One Common Spirit, Edification for All</text>

  <!-- 3 Foundational Pillars -->
  <g transform="translate(40, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. ONE SOURCE</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Same Spirit, Lord &amp; God</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">All gifts originate from the</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Trinitarian Godhead.</text>
    <text x="15" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sovereign Distribution</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Given as He determines,</text>
    <text x="15" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">not based on human merit.</text>
    <text x="15" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• No Self-Promotion</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">No room for personal boasting</text>
    <text x="15" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">or feeling spiritually superior.</text>
  </g>

  <g transform="translate(290, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. DIVERSE FUNCTIONS</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Body Metaphor</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Eye, hand, ear, foot — each</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">part is uniquely indispensable.</text>
    <text x="15" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Interdependence</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">The eye cannot say to the hand,</text>
    <text x="15" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">'I have no need of you.'</text>
    <text x="15" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mutual Honor</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Less prominent parts receive</text>
    <text x="15" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">greater, special honor.</text>
  </g>

  <g transform="translate(540, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. THE COMMON GOOD</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Edification of Church</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gifts exist to build up,</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">encourage, and strengthen faith.</text>
    <text x="15" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sacrificial Service</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Used for helping the needy,</text>
    <text x="15" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">not commercial profiteering.</text>
    <text x="15" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Governed by Love</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Spectacular gifts without love</text>
    <text x="15" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">are hollow, noisy gongs.</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"To each is given the manifestation of the Spirit for the common good." (1 Cor 12:7)</text>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE NINE GIFTS OF THE HOLY SPIRIT</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Corinthians 12:8-10 — Complete Spiritual Arsenal for the Body of Christ</text>

  <!-- 3x3 Grid of 9 Gifts -->
  <!-- Row 1 -->
  <g transform="translate(40, 85)">
    <rect width="225" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Word of Wisdom</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Supernatural insight for practical,</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">godly decisions in critical crises.</text>
  </g>
  <g transform="translate(285, 85)">
    <rect width="230" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Word of Knowledge</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Supernatural grasp of divine truths</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and unrevealed spiritual facts.</text>
  </g>
  <g transform="translate(535, 85)">
    <rect width="225" height="85" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="15" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Gift of Faith</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Extraordinary mountain-moving</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">conviction in God's power.</text>
  </g>

  <!-- Row 2 -->
  <g transform="translate(40, 185)">
    <rect width="225" height="85" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="15" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Gifts of Healing</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Supernatural restoration of physical</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and mental health in Jesus' name.</text>
  </g>
  <g transform="translate(285, 185)">
    <rect width="230" height="85" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="15" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">5. Working of Miracles</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Acts altering natural laws, casting</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">out demons, and divine deliverances.</text>
  </g>
  <g transform="translate(535, 185)">
    <rect width="225" height="85" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.2"/>
    <text x="15" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">6. Gift of Prophecy</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Proclaiming timely divine messages</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">for edification, comfort, &amp; warning.</text>
  </g>

  <!-- Row 3 -->
  <g transform="translate(40, 285)">
    <rect width="225" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">7. Discerning Spirits</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Testing manifestations: whether</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">from God, human self, or demonic.</text>
  </g>
  <g transform="translate(285, 285)">
    <rect width="230" height="85" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.2"/>
    <text x="15" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">8. Diverse Tongues</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Supernatural speech in unlearned</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">languages for prayer and praise.</text>
  </g>
  <g transform="translate(535, 285)">
    <rect width="225" height="85" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.2"/>
    <text x="15" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">9. Interpretation</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Explaining messages in tongues</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">so the whole church understands.</text>
  </g>

  <rect x="180" y="385" width="440" height="28" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="403" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">"All these are empowered by one and the same Spirit" (1 Cor 12:11)</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE THREE-TIER CLASSIFICATION OF SPIRITUAL GIFTS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Categorized by Function: Revelation (Mind), Power (Hand), and Utterance (Mouth)</text>

  <!-- Category 1: Revelation -->
  <g transform="translate(40, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="220" height="36" rx="10" fill="#0284c7"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. REVELATION (THINK)</text>
    <text x="110" y="55" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Gifts to Reveal God's Mind</text>
    <line x1="20" y1="68" x2="200" y2="68" stroke="#334155" stroke-width="1"/>
    <text x="15" y="98" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Word of Wisdom</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Practical divine answers</text>
    <text x="15" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Word of Knowledge</text>
    <text x="15" y="166" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Supernatural spiritual facts</text>
    <text x="15" y="198" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Discerning Spirits</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Distinguishing spiritual source</text>
    <rect x="15" y="238" width="190" height="20" rx="4" fill="#0f172a"/>
    <text x="105" y="252" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Divine Intellect &amp; Insight</text>
  </g>

  <!-- Category 2: Power -->
  <g transform="translate(290, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="220" height="36" rx="10" fill="#d97706"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. POWER (DO)</text>
    <text x="110" y="55" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Gifts to Do God's Acts</text>
    <line x1="20" y1="68" x2="200" y2="68" stroke="#334155" stroke-width="1"/>
    <text x="15" y="98" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Gift of Faith</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Mountain-moving confidence</text>
    <text x="15" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Gifts of Healing</text>
    <text x="15" y="166" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Restoring body and mind</text>
    <text x="15" y="198" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Working of Miracles</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Altering the natural order</text>
    <rect x="15" y="238" width="190" height="20" rx="4" fill="#0f172a"/>
    <text x="105" y="252" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Divine Action &amp; Authority</text>
  </g>

  <!-- Category 3: Utterance -->
  <g transform="translate(540, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="220" height="36" rx="10" fill="#059669"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. UTTERANCE (SPEAK)</text>
    <text x="110" y="55" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Gifts to Speak God's Voice</text>
    <line x1="20" y1="68" x2="200" y2="68" stroke="#334155" stroke-width="1"/>
    <text x="15" y="98" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Gift of Prophecy</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Proclaiming timely divine word</text>
    <text x="15" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Speaking in Tongues</text>
    <text x="15" y="166" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Supernatural prayer language</text>
    <text x="15" y="198" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Interpretation</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Translating tongues for church</text>
    <rect x="15" y="238" width="190" height="20" rx="4" fill="#0f172a"/>
    <text x="105" y="252" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Divine Proclamation</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">FUNCTIONAL UNITY: THINK, DO, AND SPEAK UNDER ONE SOVEREIGN SPIRIT</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE SUPREMACY OF AGAPE LOVE (1 CORINTHIANS 13)</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Why Spectacular Spiritual Power Without Character is Empty Noise</text>

  <!-- Left: Gifts Without Love (Spiritual Zero) -->
  <g transform="translate(40, 95)">
    <rect width="335" height="270" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#dc2626"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">GIFTS WITHOUT LOVE (EMPTY / NOISY)</text>
    <text x="15" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Tongues Without Love:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">A noisy, resounding gong or clanging cymbal.</text>
    <text x="15" y="108" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Prophecy &amp; Knowledge Without Love:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">I am spiritually nothing (zero value).</text>
    <text x="15" y="154" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mountain-Moving Faith Without Love:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">I gain nothing before God.</text>
    <text x="15" y="200" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Giving Everything to Poor Without Love:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Profits nothing; hollow self-glorification.</text>
    <rect x="15" y="234" width="305" height="24" rx="4" fill="#0f172a"/>
    <text x="167" y="250" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"If I have not love, I am nothing" (v. 2)</text>
  </g>

  <!-- Right: The Nature of Agape Love (Eternal) -->
  <g transform="translate(425, 95)">
    <rect width="335" height="270" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#059669"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE CHARACTER OF AGAPE LOVE</text>
    <text x="15" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Love IS:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Patient, kind, protective, trusting, hopeful, persevering.</text>
    <text x="15" y="108" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Love is NOT:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Envious, boastful, proud, rude, self-seeking, irritable.</text>
    <text x="15" y="154" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Love Does Not:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Keep a record of wrongs; rejoices with the truth.</text>
    <text x="15" y="200" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Love is ETERNAL:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Prophecies pass away; love never fails.</text>
    <rect x="15" y="234" width="305" height="24" rx="4" fill="#0f172a"/>
    <text x="167" y="250" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"The greatest of these is love" (v. 13)</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">LOVE IS THE FOUNDATIONAL CHARACTER THAT GIVES GIFTS THEIR VALUE</text>
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

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">RED FLAGS OF UNGODLY CULTS &amp; FALSE TEACHERS</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Matthew 7:15-20 &amp; 1 John 4:1-6 — Identifying Ferocious Wolves in Sheep's Clothing</text>

  <!-- 5 Red Flag Nodes -->
  <g transform="translate(40, 95)">
    <rect width="335" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="25" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Social &amp; Family Isolation</text>
    <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Demanding members cut off contact with parents,</text>
    <text x="15" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">family, and schoolmates who "don't understand."</text>
    <text x="15" y="92" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Red Flag: Secrecy and broken relationships</text>
  </g>

  <g transform="translate(425, 95)">
    <rect width="335" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="25" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Authoritarian Human Leader</text>
    <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Leader claims exclusive divine revelation; words</text>
    <text x="15" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">cannot be questioned or tested against Scripture.</text>
    <text x="15" y="92" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Red Flag: Unquestioned personal devotion</text>
  </g>

  <g transform="translate(40, 235)">
    <rect width="335" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="25" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Commercial Exploitation (Greed)</text>
    <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Charging money for prayers, oils, or "prophetic words";</text>
    <text x="15" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">manipulating people through fear of curses.</text>
    <text x="15" y="92" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Red Flag: Selling God's free grace for cash</text>
  </g>

  <g transform="translate(425, 235)">
    <rect width="335" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="25" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Denial of Christ's Divinity / Moral Decay</text>
    <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Denying Jesus came in the flesh, or engaging in sexual</text>
    <text x="15" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">immorality, sorcery, and lawbreaking under "liberty."</text>
    <text x="15" y="92" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Red Flag: Heresy and secret moral vices</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"By their fruit you will recognize them. Test the spirits to see if they are from God."</text>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">DISCERNMENT MATRIX: HOLY SPIRIT VS DECEPTIVE SPIRITS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 John 4:1-3, Galatians 5:19-23, &amp; 1 Corinthians 14:33 — Objective Biblical Criteria</text>

  <!-- Table Header -->
  <rect x="40" y="90" width="180" height="30" rx="4" fill="#334155"/>
  <text x="130" y="110" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CRITERIA FILTER</text>

  <rect x="230" y="90" width="260" height="30" rx="4" fill="#059669"/>
  <text x="360" y="110" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">GENUINE HOLY SPIRIT</text>

  <rect x="500" y="90" width="260" height="30" rx="4" fill="#dc2626"/>
  <text x="630" y="110" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">DECEPTIVE / COUNTERFEIT</text>

  <!-- Row 1: Christology -->
  <g transform="translate(40, 128)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Confession of Christ</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Exalts Jesus as Lord in the flesh</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Denies Christ; exalts human leader</text>
  </g>

  <!-- Row 2: Moral Fruit -->
  <g transform="translate(40, 180)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Character &amp; Fruits</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Fruit of Spirit: love, peace, purity</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Works of flesh: immorality, strife</text>
  </g>

  <!-- Row 3: Scripture Alignment -->
  <g transform="translate(40, 232)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Word Alignment</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Perfect harmony with Bible truth</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Contradicts Scripture; 'new revelations'</text>
  </g>

  <!-- Row 4: Money & Order -->
  <g transform="translate(40, 284)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Financial / Order</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Free grace; orderly self-control</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Commercial extortion; wild chaos</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Do not quench the Spirit. Test everything; hold fast what is good." (1 Thess 5:19, 21)</text>
</svg>"""


def get_svg_lesson_8():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PROPER USE VS MISUSE OF SPIRITUAL GIFTS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Corinthians 14:26-40 &amp; 1 Peter 4:10 — Biblical Stewardship and Order in Worship</text>

  <!-- Left: Proper Biblical Use -->
  <g transform="translate(40, 95)">
    <rect width="335" height="270" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#059669"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PROPER USE (EDIFICATION &amp; STEWARDSHIP)</text>
    <text x="15" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Edification of the Body:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Used to strengthen faith, comfort, and build others up.</text>
    <text x="15" y="108" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Advancing the Gospel:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Witnessing with supernatural boldness and compassion.</text>
    <text x="15" y="154" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Serving the Needy:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Caring for orphans, widows, and the vulnerable.</text>
    <text x="15" y="200" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Orderly Worship:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Speaking in turn with interpretation so all are blessed.</text>
    <rect x="15" y="234" width="305" height="24" rx="4" fill="#0f172a"/>
    <text x="167" y="250" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">✓ "Let all things be done decently and in order" (v. 40)</text>
  </g>

  <!-- Right: Common Misuses Today -->
  <g transform="translate(425, 95)">
    <rect width="335" height="270" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#dc2626"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CRITICAL MISUSES (PRIDE &amp; EXPLOITATION)</text>
    <text x="15" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Pride &amp; Showmanship:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Displaying gifts publicly to boast and claim superiority.</text>
    <text x="15" y="108" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Commercialization (Simonism):</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Selling prophecy, healing, or demanding monetary fees.</text>
    <text x="15" y="154" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sowing Division &amp; Strife:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Manipulating followers or dividing families with claims.</text>
    <text x="15" y="200" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Worship Chaos &amp; Out of Control:</text>
    <text x="15" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Loss of self-control; unruly shouting without order.</text>
    <rect x="15" y="234" width="305" height="24" rx="4" fill="#0f172a"/>
    <text x="167" y="250" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">❌ "God is not a God of confusion but of peace" (v. 33)</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">STEWARDSHIP MANDATE: SERVE OTHERS AS FAITHFUL STEWARDS OF GOD'S GRACE</text>
</svg>"""


# ─── LESSON DATA CONFIGURATIONS (8 LESSONS) ───────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Jesus' Teachings on the Role of the Holy Spirit",
        "unit_description": "Analyze Jesus' farewell teachings on the Holy Spirit, exploring His roles as Paraclete, Advocate, Teacher, Spiritual Reminder, and Source of Power for believers.",
        "lesson_title": "Jesus' Teachings on the Role of the Holy Spirit",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/8b/The_Pentecost_%28The_Descent_of_the_Holy_Spirit%29_MET_DP854927.jpg",
            "title": "Visual Hook: The Descent of the Holy Spirit at Pentecost",
            "author": "Metropolitan Museum of Art Collection",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The Holy Spirit descending upon the Apostles, fulfilling Jesus' promise to send the permanent divine Advocate, Teacher, and Counselor."
        },
        "youtube": {
            "youtube_id": "oNNZO9i1Gjc",
            "title": "BibleProject: Holy Spirit (Ruakh)",
            "description": "An engaging visual overview of the Holy Spirit as God's personal presence, empowering believers, guiding the Church, and bringing divine truth into human hearts."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Explain the theological meaning of the Greek term Parakletos as Advocate, Teacher, and Counselor.",
            "Analyze five distinct roles of the Holy Spirit in the personal life of a believer and the modern Church.",
            "Evaluate how Christians listen to and obey the internal conviction and guidance of the Holy Spirit daily."
        ],
        "intro": "Have you ever had to navigate a completely dark, unfamiliar pathway at night? It is terrifying—you stumble, trip over obstacles, and feel utterly lost. Now imagine someone hands you a powerful lantern, takes your hand, and walks alongside you, guiding every single step.\n\nThat is what Jesus promised to His followers in the Upper Room. Knowing that His physical departure would leave them feeling vulnerable, He promised to send the Holy Spirit as their permanent, personal Advocate—the Paraclete—who would live inside their hearts to guide them through every challenge.",
        "core_scripture": "### Scriptural Passages: John 14:15-26 & John 16:7-15\n\n> *\"If you love me, keep my commands. And I will ask the Father, and he will give you another advocate to help you and be with you forever—the Spirit of truth. The world cannot accept him, because it neither sees him nor knows him. But you know him, for he lives with you and will be in you.\"* (John 14:15-17)\n\n> *\"But the Advocate, the Holy Spirit, whom the Father will send in my name, will teach you all things and will remind you of everything I have said to you.\"* (John 14:26)\n\n> *\"Unless I go away, the Advocate will not come to you; but if I go, I will send him to you. When he comes, he will prove the world to be in the wrong about sin and righteousness and judgment.\"* (John 16:7-8)",
        "theological_pillars": "### Theological Exegesis: The Ministry of the Paraclete\n\n1. **The Meaning of Parakletos:** The Greek term *Parakletos* literally translates to *'one called alongside'*. In ancient judicial contexts, a Paraclete was a trusted legal defender, advocate, and counselor who stood beside a defendant to plead their case and provide protective counsel.\n2. **The Spirit of Truth:** The Holy Spirit reveals the genuine character of God, exposes the deceptive falsehoods of the world, and guides believers into all spiritual truth.\n3. **Divine Indwelling:** Unlike Old Testament manifestations where the Spirit came upon leaders temporarily, the New Covenant Holy Spirit permanently indwells every believer.\n4. **Conviction of Sin, Righteousness, and Judgment:** The Holy Spirit acts as an internal moral compass, convicting the world of unbelief, illuminating Christ's perfect righteousness, and confirming the defeat of Satan.\n5. **Empowerment for Bold Witnessing:** As fulfilled in Acts 1:8, the Holy Spirit infuses ordinary disciples with supernatural courage to preach the Gospel despite persecution.",
        "deep_dive": "### Deep Dive: Why Jesus Said His Departure Was 'To Our Advantage'\n\nIn John 16:7, Jesus made a startling statement: *'It is to your advantage that I go away.'* How could losing the physical presence of Jesus be advantageous?\n\n- **Overcoming Physical Limitations:** In His earthly incarnation, Jesus was geographically localized in Judea and Galilee. Through the Holy Spirit, God's presence is omnipresent, indwelling millions of believers across the globe simultaneously.\n- **From External Teacher to Internal Guide:** Jesus was beside the disciples; the Holy Spirit is inside the disciples, transforming hearts from within.\n- **Continuous Ministry:** The Holy Spirit illuminates Scripture, comforts during grief, and intercedes in prayer when we do not know what to say (Romans 8:26).",
        "practical": {
            "title": "Action Framework: Cultivating Sensitivity to the Holy Spirit",
            "steps": [
                "Step 1: Daily Scripture Meditation — Read God's Word attentively to allow the Holy Spirit to teach and illuminate divine truth.",
                "Step 2: Respond to Moral Conviction — When you feel the quiet inner nudge that you have acted wrongly, repent and make amends immediately.",
                "Step 3: Seek Guidance in Prayer — Pause before major decisions or peer interactions, asking the Counselor for wisdom and clarity.",
                "Step 4: Step Out in Courageous Obedience — Boldly stand up for truth, defend vulnerable classmates, and share Christ's love."
            ]
        },
        "kenyan_context": "In Kenyan schools and neighborhoods, young people constantly face moral choices—from academic integrity during exams to resisting negative peer pressure regarding substance abuse. Recognizing the Holy Spirit as an internal Counselor empowers learners to make righteous choices even when no teacher or parent is watching.",
        "reflection": "### Reflection on the Counselor's Voice\n\nReflect on your daily conscience:\n- Have you ever felt a sudden, quiet 'whisper' in your heart warning you to step away from gossip, delete an inappropriate app, or apologize to someone you hurt?\n- How does knowing that the Holy Spirit lives inside you change the way you treat your body, your thoughts, and your friends?",
        "takeaways": [
            "The Holy Spirit is the promised Paraclete (Advocate, Counselor, Helper) who lives permanently within believers (John 14:16-17).",
            "His fivefold ministry includes teaching divine truth, reminding believers of Christ's words, convicting of sin, empowering for witnessing, and providing comfort.",
            "Jesus explained that His departure enabled the Holy Spirit to be universally present with all believers across time and geography.",
            "Believers maintain spiritual sensitivity through prayer, obedience, and listening to the Holy Spirit's quiet inner conviction."
        ],
        "mcq": {
            "question": "What is the literal meaning and function of the Greek term Parakletos used by Jesus to describe the Holy Spirit in John 14?",
            "options": [
                "A) A military general who commands earthly armies to destroy political enemies",
                "B) An Advocate or Counselor called to stand alongside a person to defend, guide, and assist them",
                "C) A historical scribe who translates ancient legal scrolls in the temple",
                "D) A mysterious wind that puts believers into a physical trance"
            ],
            "answer": "B",
            "explanation": "Parakletos literally means 'one called alongside to help'. Jesus used it to describe the Holy Spirit as our divine legal defender, counselor, teacher, and comforter who supports believers daily."
        }
    },

    # ─── LESSON 2 ────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Introduction to the Spiritual Gifts",
        "unit_description": "Define spiritual gifts (Charismata), analyze Paul's teachings on the Body of Christ, and emphasize that gifts are granted for the common good and mutual edification.",
        "lesson_title": "Introduction to the Spiritual Gifts",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/2/20/Valentin_de_Boulogne_-_Saint_Paul_Writing_His_Epistles_-_BF.1991.4_-_Museum_of_Fine_Arts.jpg",
            "title": "Visual Hook: Saint Paul Writing His Epistles",
            "author": "Valentin de Boulogne (1591–1632)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Apostle Paul penning his pastoral epistles to the early churches, explaining the theological nature, purpose, and unified diversity of spiritual gifts."
        },
        "youtube": {
            "youtube_id": "yiSjZXmAe08",
            "title": "BibleProject: 1 Corinthians",
            "description": "Explores Paul's letter to Corinth, highlighting how the Corinthians' pride and division over spiritual gifts were corrected by Paul's theology of love and the Body of Christ."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Define the term 'Spiritual Gifts' (Charismata) and distinguish them from natural human talents.",
            "Explain Apostle Paul's metaphor of the Church as the Body of Christ in 1 Corinthians 12.",
            "Analyze the primary purpose of spiritual gifts: edifying the community for the common good."
        ],
        "intro": "Imagine you are part of a school football team. If the goalkeeper decided he only wanted to dribble and score goals, the defenders spent the match showing off tricks to the crowd, and the strikers refused to pass the ball, what would happen? The team would collapse and lose miserably.\n\nA team only succeeds when every player fulfills their distinct position for the collective victory. In 1 Corinthians 12, Apostle Paul used this exact concept to describe the Church: each believer receives unique spiritual abilities designed to make the entire Body of Christ flourish in harmony.",
        "core_scripture": "### Scriptural Passage: 1 Corinthians 12:1-11 & Romans 12:3-8\n\n> *\"Now about the gifts of the Spirit, brothers and sisters, I do not want you to be uninformed... There are different kinds of gifts, but the same Spirit distributes them. There are different kinds of service, but the same Lord. There are different kinds of working, but in all of them and in everyone it is the same God at work.\n> Now to each one the manifestation of the Spirit is given for the common good.\n> All these are the work of one and the same Spirit, and he distributes them to each one, just as he determines.\"* (1 Corinthians 12:1, 4-7, 11)",
        "theological_pillars": "### Theological Foundations of Charismata\n\n1. **Definition of Charismata:** The Greek word *Charismata* derives from *charis* (grace). Spiritual gifts are supernatural abilities freely bestowed upon believers by the Holy Spirit to serve others and build up the Church.\n2. **Natural Talents vs Spiritual Gifts:** Natural talents (e.g. musical aptitude, athletic ability) are received at biological birth through common grace. Spiritual gifts are supernaturally imparted upon spiritual rebirth for kingdom ministry.\n3. **Trinitarian Harmony:** In 1 Corinthians 12:4-6, Paul roots the gifts in the Trinity: the *same Spirit* gives gifts, the *same Lord* (Jesus) directs service, and the *same God* (Father) empowers all workings.\n4. **The Common Good (*Sympheron*):** Gifts are never personal trophies for private boasting or financial gain; their explicit divine mandate is the common good—strengthening the faith of the community.\n5. **Sovereign Distribution:** The Spirit distributes gifts *'as He determines'*. No Christian possesses every gift, and no gift is given to every Christian, creating intentional interdependence.",
        "deep_dive": "### Deep Dive: Paul's Correction of the Corinthian Church\n\nThe church in Corinth was dynamic and highly gifted, but suffered from severe immaturity, spiritual pride, and division:\n\n- **The Error of Superiority:** Certain members who spoke in tongues considered themselves spiritually superior to those with less flamboyant gifts like administration or helping.\n- **The Body Metaphor:** Paul dismantled their arrogance by arguing that an eye cannot despise the hand, nor can the head despise the feet (1 Cor 12:21). The seemingly 'weaker' or less visible parts are often the most indispensable.\n- **Equality in Value:** In God's eyes, quiet gifts of mercy and service carry equal kingdom honor to visible platform gifts.",
        "practical": {
            "title": "Action Framework: Discovering and Stewarding Your Spiritual Gifts",
            "steps": [
                "Step 1: Cultivate Humility — Recognize that all gifts are unearned gifts of grace, leaving no room for boasting or arrogance.",
                "Step 2: Engage in Active Service — Participate in church youth groups, school Christian unions, and community service to discover where God uses you.",
                "Step 3: Value Diverse Talents in Others — Celebrate the unique abilities of your peers without jealousy, comparison, or contempt.",
                "Step 4: Align Service with Love — Ensure that your motivation in utilizing any talent or gift is genuine care for the well-being of others."
            ]
        },
        "kenyan_context": "In Kenyan Christian Unions (CU) and local parishes, youth often participate in diverse ministries—singing in the choir, ushering, organizing charity drives, or playing musical instruments. Understanding the Body of Christ helps students collaborate harmoniously without competing for the spotlight.",
        "reflection": "### Reflection on Interdependence\n\nConsider how you interact with others in your community:\n- Do you ever look down on classmates whose talents seem less visible or glamorous than yours?\n- How does Paul's body metaphor encourage you to appreciate and support every single member of your class and church?",
        "takeaways": [
            "Spiritual gifts (Charismata) are supernatural graces distributed by the Holy Spirit for the common good of the Church (1 Cor 12:7).",
            "The Trinity is the unified source behind diverse gifts, ministries, and workings (1 Cor 12:4-6).",
            "Paul compares the Church to the human body, where every distinct member is necessary and interdependent.",
            "Gifts are not given for personal pride or financial profit, but to serve and build up others in humble love."
        ],
        "mcq": {
            "question": "According to 1 Corinthians 12:7, what is the primary biblical purpose of spiritual gifts?",
            "options": [
                "A) To establish a hierarchy where gifted believers rule over less gifted members",
                "B) To serve the common good and build up the entire Church community",
                "C) To enable Christians to amass wealth and become famous spiritual celebrities",
                "D) To prove that certain individuals are completely sinless and holy"
            ],
            "answer": "B",
            "explanation": "Paul explicitly states in 1 Corinthians 12:7 that the manifestation of the Spirit is given to each one 'for the common good'—to edify, strengthen, and serve the whole body of believers."
        }
    },

    # ─── LESSON 3 ────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "The Nine Gifts of the Holy Spirit",
        "unit_description": "Examine the catalog of the nine spiritual gifts listed by Paul in 1 Corinthians 12:8-10, explaining the definition and specific church function of each gift.",
        "lesson_title": "The Nine Gifts of the Holy Spirit",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/09/Bowyer_Bible_Luke_Pentecost_Acts_2_1-4_K%C3%BCsel.jpg",
            "title": "Visual Hook: The Outpouring of the Holy Spirit",
            "author": "Melchior Küsel (1626–1683), Bowyer Bible Collection",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The early Church endowed with the diverse gifts of the Holy Spirit, enabling disciples to speak, heal, discern, and lead with supernatural power."
        },
        "youtube": {
            "youtube_id": "oNNZO9i1Gjc",
            "title": "BibleProject: The Holy Spirit in Action",
            "description": "Examines how the Holy Spirit empowers God's people with supernatural wisdom, courage, healing, and prophetic utterance to carry out the divine mission."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "List and define the nine distinct gifts of the Holy Spirit recorded in 1 Corinthians 12:8-10.",
            "Explain the specific functional role each gift plays in the protection and edification of the Church.",
            "Demonstrate how the nine gifts provide a complete spiritual toolkit for Christian ministry."
        ],
        "intro": "Have you ever opened a multi-tool Swiss army knife or a master carpenter's toolbox? It doesn't just have one tool; it contains screwdrivers, pliers, blades, saws, and measuring tape. You would never use a saw to tighten a tiny screw, nor a screwdriver to cut timber. Each tool is engineered for a specific task.\n\nIn 1 Corinthians 12:8-10, Apostle Paul opens the Holy Spirit's master toolbox, detailing nine extraordinary spiritual gifts that equip the Church to handle every spiritual, emotional, and physical challenge.",
        "core_scripture": "### Scriptural Passage: 1 Corinthians 12:8-10\n\n> *\"To one there is given through the Spirit a message of wisdom, to another a message of knowledge by means of the same Spirit, to another faith by the same Spirit, to another gifts of healing by that one Spirit, to another miraculous powers, to another prophecy, to another distinguishing between spirits, to another speaking in different kinds of tongues, and to still another the interpretation of tongues.\"*",
        "theological_pillars": "### The Nine Spiritual Gifts Defined\n\n1. **Word of Wisdom:** Supernatural insight given to apply divine truth to complex, critical situations, providing godly practical solutions.\n2. **Word of Knowledge:** Supernatural revelation of facts, principles, or spiritual situations not acquired through ordinary human intellect or research.\n3. **Gift of Faith:** An extraordinary, unwavering conviction and mountain-moving confidence in God's power to intervene supernaturally in impossible circumstances.\n4. **Gifts of Healing:** Supernatural power to restore physical, psychological, and emotional wholeness to the sick without natural medical means, in Jesus' name.\n5. **Working of Miracles:** Supernatural acts altering the ordinary laws of nature, demonstrating God's sovereign authority (e.g. casting out demons, divine provision).\n6. **Gift of Prophecy:** Proclaiming a timely, inspired message from God for the purpose of edification, encouragement, and consolation (1 Cor 14:3).\n7. **Distinguishing of Spirits (Discernment):** The critical spiritual ability to perceive whether a teaching, manifestation, or person is motivated by the Holy Spirit, human ego, or demonic forces.\n8. **Diverse Kinds of Tongues:** The supernatural ability to pray or speak in unlearned languages—either human dialects or heavenly prayer languages.\n9. **Interpretation of Tongues:** The supernatural ability to translate and convey the spiritual meaning of a message spoken in tongues so that the entire church is edified.",
        "deep_dive": "### Deep Dive: Function and Synergy of the Gifts\n\nThe nine gifts do not operate in isolation; they function synergistically to safeguard and empower the community:\n\n- **Guarding Truth:** The *Word of Knowledge* and *Discerning of Spirits* protect the congregation from fraudulent claims and spiritual deception.\n- **Meeting Human Need:** *Gifts of Healing* and *Working of Miracles* bring physical relief and validate the Gospel message before unbelievers.\n- **Directing Worship:** *Prophecy*, *Tongues*, and *Interpretation* facilitate vibrant corporate worship and timely divine guidance.",
        "practical": {
            "title": "Action Framework: Operating in Spiritual Maturity",
            "steps": [
                "Step 1: Pray for Spiritual Understanding — Ask God to open your heart to understand how spiritual gifts operate biblically.",
                "Step 2: Exercise Discernment — Always test prophetic messages and spiritual claims against the written Scriptures.",
                "Step 3: Seek to Build Others Up — When exercising any gift or ability, ask yourself: 'Does this help, encourage, and comfort my neighbor?'",
                "Step 4: Maintain Order and Humility — Never use spiritual abilities to draw attention to yourself or disrupt peaceful fellowship."
            ]
        },
        "kenyan_context": "In Kenyan churches, services are often rich with prayer for the sick, prophetic exhortations, and diverse worship expressions. Understanding the biblical definitions of all nine gifts helps young believers participate faithfully while avoiding confusion or emotional manipulation.",
        "reflection": "### Reflection on God's Diverse Gifts\n\nReflect on the variety of spiritual gifts:\n- Why did God provide nine diverse gifts rather than giving all abilities to a single person or leader?\n- How does this distribution foster humility, teamwork, and mutual respect among Christians?",
        "takeaways": [
            "1 Corinthians 12:8-10 outlines nine distinct gifts of the Holy Spirit: Wisdom, Knowledge, Faith, Healing, Miracles, Prophecy, Discerning Spirits, Tongues, and Interpretation.",
            "Each gift is a specific divine enablement designed to meet spiritual, physical, and pastoral needs within the Church.",
            "The gifts work in synergy to reveal God's mind, demonstrate His power, and speak His messages.",
            "Spiritual maturity requires exercising all gifts with order, scriptural alignment, and love."
        ],
        "mcq": {
            "question": "Which spiritual gift specifically enables a believer to determine whether a spiritual manifestation or teaching originates from the Holy Spirit, human emotion, or demonic deception?",
            "options": [
                "A) The Gift of Prophecy",
                "B) The Gift of Distinguishing / Discerning of Spirits",
                "C) The Gift of Tongues",
                "D) The Gift of Miracles"
            ],
            "answer": "B",
            "explanation": "The gift of distinguishing of spirits (discernment) provides supernatural insight to evaluate the genuine source behind spiritual manifestations, safeguarding the Church against deception."
        }
    },

    # ─── LESSON 4 ────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Classification of the Spiritual Gifts",
        "unit_description": "Classify the nine spiritual gifts into three classical functional categories: Gifts of Revelation (Mind), Gifts of Power (Hand), and Gifts of Utterance (Mouth).",
        "lesson_title": "Classification of the Spiritual Gifts",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Bowyer_Bible_Luke_Pentecost_Acts_2_1-4_after_Rubens.jpg",
            "title": "Visual Hook: The Tripartite Manifestation of Spiritual Grace",
            "author": "After Peter Paul Rubens, Bowyer Bible Collection",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The systematic outpouring of divine gifts equipping the mind, the hand, and the voice of the Church for ordered gospel mission."
        },
        "youtube": {
            "youtube_id": "tp5MI_UC6mg",
            "title": "BibleProject: God's Blueprint for the Church",
            "description": "An exploration of how God systematically structures and equips His people with wisdom, power, and prophetic speech to reflect His kingdom on earth."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Classify the nine spiritual gifts into the three classical categories: Revelation, Power, and Utterance.",
            "Explain the distinctive function, biblical examples, and domain of each classification category.",
            "Analyze how the tripartite classification promotes orderliness and systematic understanding in Christian theology."
        ],
        "intro": "Think about how books are arranged in your school library. Are thousands of books dumped in a giant, chaotic pile on the floor? Of course not. They are categorized into Science, History, Languages, and Mathematics. Classification brings clarity, structure, and accessibility.\n\nTo help believers understand and apply the nine spiritual gifts systematically, theologians classify them into **three functional families**: Gifts of Revelation (to think/know), Gifts of Power (to do/act), and Gifts of Utterance (to speak/proclaim).",
        "core_scripture": "### Scriptural Passage: 1 Corinthians 12:8-10 & 1 Corinthians 14:26-33\n\n> *\"To one there is given through the Spirit a message of wisdom, to another a message of knowledge... to another faith... gifts of healing... miraculous powers... to another prophecy... distinguishing between spirits... speaking in different kinds of tongues, and to still another the interpretation of tongues.\"*\n\n> *\"For God is not a God of disorder but of peace—as in all the congregations of the Lord's people.\"* (1 Corinthians 14:33)",
        "theological_pillars": "### The Three-Tier Functional Classification\n\n1. **Gifts of Revelation (Gifts to Think / Reveal):** These gifts reveal something supernatural from the mind of God that human intellect could not otherwise discover:\n   - **Word of Wisdom:** Revelation of God's mind for practical application.\n   - **Word of Knowledge:** Revelation of facts in the divine mind.\n   - **Discerning of Spirits:** Revelation of the spiritual realm and source.\n2. **Gifts of Power (Gifts to Do / Act):** These gifts demonstrate God's supernatural authority and power through physical, tangible actions in the natural world:\n   - **Gift of Faith:** Supernatural confidence to receive miracles.\n   - **Gifts of Healing:** Supernatural power to cure diseases and infirmities.\n   - **Working of Miracles:** Supernatural acts altering the laws of nature.\n3. **Gifts of Utterance (Gifts to Speak / Proclaim):** These gifts utilize human vocal organs supernaturally to convey God's message:\n   - **Gift of Prophecy:** Inspired, spontaneous utterance in a known tongue.\n   - **Speaking in Tongues:** Supernatural prayer language in an unknown tongue.\n   - **Interpretation of Tongues:** Translating an inspired message into the common language.",
        "deep_dive": "### Deep Dive: The Tripartite Balance in Church Life\n\nA healthy, biblically balanced church requires all three categories working in harmony:\n\n- **Without Revelation Gifts:** The church is vulnerable to deception, confusion, and spiritual blindness.\n- **Without Power Gifts:** The church lacks tangible demonstration of God's compassion for suffering and the sick.\n- **Without Utterance Gifts:** The church lacks timely prophetic encouragement, comfort, and dynamic worship.\n- **God of Order:** Classification highlights that the Holy Spirit is methodical and intentional, establishing structure rather than chaotic confusion.",
        "practical": {
            "title": "Action Framework: Structuring Your Whole-Person Development",
            "steps": [
                "Step 1: Develop Your Mind (Revelation) — Read widely, study Scripture, and pray for godly discernment in your academic and moral life.",
                "Step 2: Act in Faith (Power) — Step out in tangible acts of compassion, helping the sick, standing up for justice, and serving the needy.",
                "Step 3: Guard Your Speech (Utterance) — Use your words exclusively to encourage, speak truth, build others up, and worship God.",
                "Step 4: Maintain Orderly Discipline — Organize your daily schedule, studies, and devotional habits with godly orderliness."
            ]
        },
        "kenyan_context": "In Kenyan schools, holistic education emphasizes academic knowledge (mind), co-curricular activities and manual skills (action), and debate or public speaking (speech). The three categories of spiritual gifts parallel this holistic growth, showing that God cares about our thoughts, actions, and words.",
        "reflection": "### Reflection on Whole-Person Ministry\n\nReflect on how you use your abilities:\n- Which area of your life—your thoughts (mind), your actions (hands), or your speech (words)—is currently bringing the most glory to God?\n- How can you allow the Holy Spirit to strengthen the areas where you are weakest?",
        "takeaways": [
            "The nine spiritual gifts are classified into three functional families: Revelation (Mind), Power (Hand), and Utterance (Mouth).",
            "Revelation gifts (Wisdom, Knowledge, Discernment) reveal God's thoughts and expose spiritual realities.",
            "Power gifts (Faith, Healing, Miracles) demonstrate God's supernatural physical authority.",
            "Utterance gifts (Prophecy, Tongues, Interpretation) proclaim God's timely messages for community edification."
        ],
        "mcq": {
            "question": "Which of the following groupings correctly lists only the 'Gifts of Power' (Gifts to Do)?",
            "options": [
                "A) Word of Wisdom, Word of Knowledge, and Prophecy",
                "B) Gift of Faith, Gifts of Healing, and Working of Miracles",
                "C) Diverse Tongues, Interpretation of Tongues, and Discerning of Spirits",
                "D) Gifts of Healing, Word of Wisdom, and Tongues"
            ],
            "answer": "B",
            "explanation": "The Gifts of Power (Faith, Healing, and Working of Miracles) are characterized by physical, supernatural actions demonstrating God's sovereign authority over sickness, nature, and circumstances."
        }
    },

    # ─── LESSON 5 ────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "The Supremacy of Love",
        "unit_description": "Analyze Paul's teachings in 1 Corinthians 13 on Agape love, explaining why supernatural spiritual gifts without character and love are spiritually hollow and useless.",
        "lesson_title": "The Supremacy of Love",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/2/22/Bowyer_Bible_Luke_Pentecost_Acts_2_1-4_after_Carracci.jpg",
            "title": "Visual Hook: Faith, Hope, and Charity in Early Christian Ministry",
            "author": "After Annibale Carracci, Bowyer Bible Collection",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The supreme Christian virtue of Agape love governing all spiritual operations, enduring long after temporary gifts have ceased."
        },
        "youtube": {
            "youtube_id": "yiSjZXmAe08",
            "title": "BibleProject: The Way of Love (1 Corinthians 13)",
            "description": "A deep theological look at 1 Corinthians 13, showing how self-sacrificial love is the eternal core of Christian character and the governing law of spiritual gifts."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Define the biblical concept of Agape love and distinguish it from emotional or romantic affection.",
            "Analyze Paul's warnings in 1 Corinthians 13:1-3 regarding spiritual gifts exercised without love.",
            "Explain why spiritual gifts are temporary while love, faith, and hope are eternal."
        ],
        "intro": "Imagine a brilliant medical doctor who can cure rare diseases, but speaks to her dying patients with cruel sarcasm and mocks their pain. Or imagine a genius teacher who knows every scientific fact, but screams insults at struggling students. Does their brilliance excuse their lack of love? No. It makes them terrifying.\n\nIn 1 Corinthians 13, Apostle Paul paused his teaching on spiritual gifts to drop a spiritual bombshell: no matter how spectacular your spiritual gifts are—even if you speak in angelic tongues, prophesy the future, or move mountains with your faith—if you do not have love, you are spiritually absolute zero.",
        "core_scripture": "### Scriptural Passage: 1 Corinthians 13:1-13\n\n> *\"If I speak in the tongues of men or of angels, but do not have love, I am only a resounding gong or a clanging cymbal. If I have the gift of prophecy and can fathom all mysteries and all knowledge, and if I have a faith that can move mountains, but do not have love, I am nothing. If I give all I possess to the poor and give over my body to hardship that I may boast, but do not have love, I gain nothing.\n> Love is patient, love is kind. It does not envy, it does not boast, it is not proud. It does not dishonor others, it is not self-seeking, it is not easily angered, it keeps no record of wrongs. Love does not delight in evil but rejoices with the truth. It always protects, always trusts, always hopes, always perseveres.\n> Love never fails... And now these three remain: faith, hope and love. But the greatest of these is love.\"*",
        "theological_pillars": "### The Theological Supremacy of Agape\n\n1. **Agape Love Defined:** *Agape* is unconditional, self-sacrificial, active divine love. It is not a fickle emotional feeling, but a deliberate decision of the will to seek the highest good of another, regardless of cost.\n2. **The Spiritual Zero Formula:** In verses 1-3, Paul equates spectacular spiritual manifestations minus love to absolute nothingness:\n   - *Tongues - Love = Noisy Gong / Clanging Cymbal* (irritating, useless noise).\n   - *Prophecy + Knowledge + Faith - Love = Spiritual Zero* (I am nothing).\n   - *Philanthropy + Martyrdom - Love = Zero Reward* (I gain nothing).\n3. **The 15 Characteristics of Love:** Paul defines love by what it *does* (patient, kind, protective, trusting, hopeful, persevering) and what it *refuses to do* (envy, boast, be proud, dishonor others, be self-seeking, keep records of wrongs).\n4. **The Permanence of Love:** Prophecies will cease, tongues will be stilled, and partial knowledge will pass away when the perfect arrives. But love is eternal because God Himself is love (1 John 4:8).",
        "deep_dive": "### Deep Dive: Gifts vs Fruits of the Spirit\n\nA critical distinction in biblical theology is between spiritual gifts (*charismata*) and spiritual fruits (*karpos*):\n\n- **Spiritual Gifts:** Relate to **ability** and **service**. They are given freely and instantaneously by grace, regardless of the recipient's spiritual maturity.\n- **Spiritual Fruit (Love, Joy, Peace):** Relates to **character** and **holiness**. It grows slowly through discipleship, obedience, and abiding in Christ (Galatians 5:22-23).\n- **Danger of Disconnection:** Exercising great spiritual gifts without corresponding fruit of love leads inevitably to spiritual pride, moral downfall, and devastating abuse of power.",
        "practical": {
            "title": "Action Framework: Practicing Agape Love in Daily Life",
            "steps": [
                "Step 1: Choose Patience and Kindness — In moments of irritation with classmates or siblings, deliberately respond with gentle words.",
                "Step 2: Destroy Mental Records of Wrongs — Forgive those who offend you instead of keeping a mental list to use during future arguments.",
                "Step 3: Celebrate Others' Success — When a classmate wins an award or receives praise, rejoice sincerely rather than feeling envious.",
                "Step 4: Serve Without Selfish Motives — Help others quietly without expecting applause, favors, or social media validation."
            ]
        },
        "kenyan_context": "In Kenyan boarding schools and community life, students live in close quarters where irritations, rumors, and competition can easily spark hostility. Living out 1 Corinthians 13—being slow to anger, refusing to hold grudges, and showing kindness—builds lasting peace and genuine unity across diverse backgrounds.",
        "reflection": "### Reflection on the Power of Love\n\nReflect on your personal motivation:\n- If someone observed your words, actions, and attitudes throughout this week, would they describe you as patient, kind, and humble?\n- Why is having a loving character vastly more important to God than possessing spectacular talents or winning academic competitions?",
        "takeaways": [
            "Agape love is unconditional, self-sacrificial action, not merely a fleeting emotional feeling.",
            "Possessing spectacular gifts like tongues, prophecy, or faith without love makes a believer spiritually empty and noisy (1 Cor 13:1-3).",
            "Paul provides 15 behavioral marks of love, highlighting patience, kindness, humility, and forgiveness.",
            "Spiritual gifts are temporary tools for earthly ministry, but love is eternal and represents the supreme Christian virtue (1 Cor 13:13)."
        ],
        "mcq": {
            "question": "According to Apostle Paul in 1 Corinthians 13:1-3, what is the spiritual value of performing miracles, speaking in tongues, and moving mountains if one lacks love?",
            "options": [
                "A) It is still highly rewarded because miracles automatically prove holiness",
                "B) It makes the believer spiritually nothing, producing only annoying noise like a clanging cymbal",
                "C) It replaces the need for repentance and church attendance",
                "D) It earns eternal life regardless of personal moral conduct"
            ],
            "answer": "B",
            "explanation": "Paul emphatically states that without love, spectacular spiritual abilities like speaking in tongues make one a 'resounding gong or clanging cymbal' and reduce one's spiritual value before God to 'nothing'."
        }
    },

    # ─── LESSON 6 ────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Detecting False Teachings and Ungodly Cults",
        "unit_description": "Define religious cults and extremism, examine five critical warning signs of false teachers, and apply biblical discernment strategies to protect against spiritual deception.",
        "lesson_title": "Detecting False Teachings and Ungodly Cults",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Bowyer_Bible_Luke_Pentecost_Acts_2_1_Borcht.jpg",
            "title": "Visual Hook: Disciples Defending the Gospel against False Doctrines",
            "author": "Petrus van der Borcht, Bowyer Bible Collection",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Early Christian disciples standing firm on the apostolic Scriptures, exposing deceptive heresies and protecting the flock from spiritual wolves."
        },
        "youtube": {
            "youtube_id": "G-2e9mMf7E8",
            "title": "BibleProject: Testing the Truth",
            "description": "An overview of apostolic warnings against deceptive teachings, counterfeit spirituality, and the importance of anchoring faith in the historical person of Jesus Christ."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Define the terms 'Cult' and 'Religious Extremism' in contemporary sociological and biblical contexts.",
            "Identify five critical red flags that distinguish deceptive cults from genuine Christian fellowships.",
            "Apply Jesus' principle of 'recognizing trees by their fruit' (Matthew 7:15-20) to detect false prophets."
        ],
        "intro": "Have you ever bought an electronic gadget or designer shoes in town or online that looked completely genuine on the packaging, only to open it at home and discover it was a cheap, non-functional fake? Counterfeits succeed because they look almost identical to the genuine product on the outside.\n\nIn the spiritual realm, false prophets and ungodly cults operate the exact same way. They use religious jargon, carry Bibles, and promise instant miracles or wealth, but underneath, they manipulate, exploit, and destroy lives. Jesus warned: *'Watch out for false prophets. They come to you in sheep's clothing, but inwardly they are ferocious wolves.'*",
        "core_scripture": "### Scriptural Passages: Matthew 7:15-20 & 1 John 4:1-6\n\n> *\"Watch out for false prophets. They come to you in sheep's clothing, but inwardly they are ferocious wolves. By their fruit you will recognize them. Do people pick grapes from thornbushes, or figs from thistles? Likewise, every good tree bears good fruit, but a bad tree bears bad fruit. A good tree cannot bear bad fruit, and a bad tree cannot bear good fruit... Thus, by their fruit you will recognize them.\"* (Matthew 7:15-18, 20)\n\n> *\"Dear friends, do not believe every spirit, but test the spirits to see whether they are from God, because many false prophets have gone out into the world. This is how you can recognize the Spirit of God: Every spirit that acknowledges that Jesus Christ has come in the flesh is from God, but every spirit that does not acknowledge Jesus is not from God.\"* (1 John 4:1-3)",
        "theological_pillars": "### Definitions and Red Flags of Deceptive Cults\n\n1. **Definitions:**\n   - **Cult:** A religious group characterized by extreme devotion to an authoritarian human leader, holding deceptive or hidden doctrines that isolate members from family and society, often resulting in severe emotional, financial, or physical exploitation.\n   - **Religious Extremism:** Fanatical religious beliefs that promote hatred, intolerance, and destructive or illegal behavior under the guise of divine commands.\n2. **Five Critical Warning Signs of Ungodly Cults:**\n   - **1. Isolation from Family and Society:** Demanding members cut ties with parents, relatives, and school friends who 'lack spiritual light'.\n   - **2. Unquestioned Human Leader:** The leader claims exclusive divine revelations that cannot be checked or challenged by Scripture.\n   - **3. Financial Exploitation (Commercialization):** Coercing members into giving money, property, or 'seed offerings' to purchase blessings or escape curses.\n   - **4. Moral Compromise and Secret Vices:** Promoting sexual immorality, illegal acts, or sorcery behind closed doors.\n   - **5. Culture of Fear and Manipulation:** Threatening members with supernatural death, illness, or damnation if they question doctrines or attempt to leave.",
        "deep_dive": "### Deep Dive: Why Youth are Targeted by Cults\n\nSociological and pastoral studies reveal why young people are particularly vulnerable to cult recruitment:\n\n- **Search for Identity and Belonging:** Teens struggling with low self-esteem or broken family relationships are easily attracted to groups offering intensive initial affection (known as 'love bombing').\n- **Desire for Quick Solutions:** Promises of instant exam success, wealth, or supernatural popularity without hard work appeal to anxious learners.\n- **Biblical Illiteracy:** Learners who do not know the Scriptures can easily be deceived by out-of-context verses manipulated by charismatic speakers.",
        "practical": {
            "title": "Action Framework: Guarding Against Spiritual Deception",
            "steps": [
                "Step 1: Test Everything with the Bible — When you hear a sermon or teaching, verify if it aligns with the complete written Word of God.",
                "Step 2: Reject Secrecy — Never join secretive religious groups that demand you hide your participation from your parents, guardians, or teachers.",
                "Step 3: Examine Moral Character — Evaluate leaders not by their eloquence or flashy attire, but by their humility, honesty, and moral purity.",
                "Step 4: Report Suspicious Groups — If approached by recruiters demanding money, oaths, or isolation, report immediately to trusted elders and authorities."
            ]
        },
        "kenyan_context": "Kenya has witnessed tragic incidents where extreme religious cults (such as the Shakahola tragedy) led to devastating loss of life through enforced starvation, isolation, and brainwashing. Grade 9 learners must understand these warning signs to protect themselves, their families, and their peers.",
        "reflection": "### Reflection on Spiritual Vigilance\n\nReflect on the teachings you encounter on social media and television:\n- When you watch dynamic preachers promising instant wealth on TikTok or TV, do their teachings exalt Christ and holy living, or do they focus on demanding money?\n- How can you strengthen your knowledge of Scripture so you are never swayed by deceptive teachers?",
        "takeaways": [
            "Cults are characterized by authoritarian leaders, isolation from family, financial greed, fear manipulation, and heretical doctrines.",
            "Jesus commanded believers to test prophets by their 'fruit'—evaluating their character, teachings, and lifestyle (Matthew 7:15-20).",
            "1 John 4:1-3 warns against believing every spirit, commanding Christians to test spirits against the truth of Christ's incarnation and lordship.",
            "Vigilance, deep biblical literacy, and open communication with parents and mentors protect youth from cult exploitation."
        ],
        "mcq": {
            "question": "What did Jesus establish in Matthew 7:15-20 as the definitive test to expose false prophets dressed in sheep's clothing?",
            "options": [
                "A) The size of their congregations and the expensive luxury cars they drive",
                "B) 'By their fruit you will recognize them'—examining their moral character, lifestyle, and scriptural truth",
                "C) Their ability to shout loudly and perform convincing psychological illusions",
                "D) The number of followers they have on digital social media platforms"
            ],
            "answer": "B",
            "explanation": "Jesus taught that while false teachers can easily disguise themselves in religious vocabulary ('sheep's clothing'), their bad moral fruit—greed, pride, immorality, and deception—will inevitably expose their true nature."
        }
    },

    # ─── LESSON 7 ────────────────────────────────────────────────────────────
    {
        "unit_order": 7,
        "unit_name": "Criteria for Discerning Spiritual Manifestations",
        "unit_description": "Establish objective biblical criteria to test spiritual manifestations, contrasting the genuine Holy Spirit with counterfeit spirits across confession, character, doctrine, and order.",
        "lesson_title": "Criteria for Discerning Spiritual Manifestations",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/6/64/Mechelen_St_-_Jan_Lucas_Franchoys_Descent_of_the_Holy_Spirit_01.jpg",
            "title": "Visual Hook: Apostolic Discernment and the Holy Spirit",
            "author": "Jan Lucas Franchoys (1616–1681), Church of St. John, Mechelen",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The apostolic Church exercising spiritual vigilance and discernment, anchored in the Holy Spirit's fruits of truth, love, and order."
        },
        "youtube": {
            "youtube_id": "oNNZO9i1Gjc",
            "title": "BibleProject: Testing the Spirits",
            "description": "An analysis of the biblical criteria for spiritual discernment, examining how genuine spiritual operations consistently reflect the character, humility, and truth of Jesus."
        },
        "svg_fn": get_svg_lesson_7,
        "goals": [
            "Outline five objective biblical criteria for discerning whether a spiritual manifestation is genuinely from God.",
            "Contrast genuine manifestations of the Holy Spirit with counterfeit and demonic operations.",
            "Apply the Fruit of the Spirit (Galatians 5:22-23) and the Spirit of Order (1 Corinthians 14:33) to contemporary church experiences."
        ],
        "intro": "Have you ever watched a skilled illusionist or stage magician perform in town or on video? They make objects levitate, appear to read minds, or escape impossible locks. To your physical eyes, it looks entirely real. But you know it is a clever trick designed to entertain.\n\nIn the spiritual world, how can we determine whether a dramatic display of prophecy, healing, or tongues is genuinely the Holy Spirit at work, or merely human emotional hype and demonic counterfeit? God did not leave us to guess; He provided five bulletproof biblical filters.",
        "core_scripture": "### Scriptural Passages: 1 John 4:1-3, Galatians 5:19-23, & 1 Corinthians 12:2-3\n\n> *\"This is how you can recognize the Spirit of God: Every spirit that acknowledges that Jesus Christ has come in the flesh is from God, but every spirit that does not acknowledge Jesus is not from God. This is the spirit of the antichrist.\"* (1 John 4:2-3)\n\n> *\"Therefore I want you to know that no one who is speaking by the Spirit of God says, 'Jesus be cursed,' and no one can say, 'Jesus is Lord,' except by the Holy Spirit.\"* (1 Corinthians 12:3)\n\n> *\"But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. Against such things there is no law.\"* (Galatians 5:22-23)",
        "theological_pillars": "### The Five Biblical Criteria for Discernment\n\n1. **The Christological Criterion (Confession of Jesus):** A genuine manifestation always exalts Jesus Christ as Lord, God incarnate, and Savior (1 Cor 12:3, 1 John 4:2). Any spirit that diminishes Christ, denies His bodily incarnation, or elevates a human leader is counterfeit.\n2. **The Moral Fruit Criterion:** Genuine manifestations produce the Fruit of the Spirit—love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, and self-control (Gal 5:22-23). Counterfeits produce works of the flesh: sexual immorality, greed, jealousy, and arrogance.\n3. **The Scriptural Consistency Criterion:** The Holy Spirit is the Author of Scripture; therefore, genuine spiritual manifestations never contradict the written Word of God. Any 'revelation' that conflicts with biblical truth is false.\n4. **The Attitude to Money (Non-Commercialization):** Genuine spiritual ministry is motivated by humble compassion and free grace (Matthew 10:8: *'Freely you have received; freely give'*). False spirits commercialize prayer, selling 'holy water' or prophetic words.\n5. **The Spirit of Order and Self-Control:** 1 Corinthians 14:32-33 states that *'the spirits of prophets are subject to the control of prophets. For God is not a God of disorder but of peace.'* The Holy Spirit never forces a person to lose their self-control or act violently.",
        "deep_dive": "### Deep Dive: The Balance of 1 Thessalonians 5:19-22\n\nApostle Paul provides the golden rule of Christian discernment in four concise commands:\n\n- *'Do not quench the Spirit'* — Do not be cynical, cold, or dismissive of genuine spiritual gifts.\n- *'Do not treat prophecies with contempt'* — Keep an open, respectful posture toward God speaking through His people.\n- *'Test everything'* — Filter all words, claims, and experiences through the objective grid of Scripture and Christian character.\n- *'Hold fast to what is good, and abstain from every form of evil'* — Embrace genuine biblical truth while resolutely rejecting counterfeit deception.",
        "practical": {
            "title": "Action Framework: Applying the Discernment Filter",
            "steps": [
                "Step 1: Check the Christ Focus — Does the teaching or miracle give glory solely to Jesus Christ, or does it glorify a human preacher?",
                "Step 2: Compare with Scripture — Look up Bible passages to confirm whether the claims and practices align with God's Word.",
                "Step 3: Observe Moral Character — Look at the lifestyle of the speaker over time: do they demonstrate honesty, humility, and self-control?",
                "Step 4: Evaluate Financial Integrity — Beware of any individual who demands payment, money, or property in exchange for prayers or blessings."
            ]
        },
        "kenyan_context": "In contemporary Kenyan media and open-air crusades, claims of miracles, prophecies, and deliverance are widespread. Equipping learners with these five objective criteria empowers them to navigate diverse spiritual claims with wisdom, maturity, and scriptural clarity.",
        "reflection": "### Reflection on Self-Control and Order\n\nReflect on the nature of worship:\n- Why did Apostle Paul emphasize that 'the spirits of prophets are subject to the control of prophets'?\n- How does maintaining self-control during worship prove that God is a God of peace and order rather than chaotic confusion?",
        "takeaways": [
            "Spiritual manifestations must be tested against five biblical criteria: Confession of Christ, Moral Fruit, Scriptural Alignment, Financial Integrity, and Orderliness.",
            "Genuine manifestations exalt Jesus as Lord and produce the ninefold Fruit of the Spirit (Gal 5:22-23).",
            "The Holy Spirit never forces people into chaotic loss of self-control; worship must be orderly and edifying (1 Cor 14:32-33).",
            "Paul commands believers neither to quench the Spirit nor swallow claims blindly, but to 'test everything and hold fast to the good' (1 Thess 5:19-21)."
        ],
        "mcq": {
            "question": "According to 1 Corinthians 14:32-33, how does the true Holy Spirit operate during corporate worship in contrast to deceptive chaotic spirits?",
            "options": [
                "A) He causes believers to completely lose their self-control and faint in mass hysteria",
                "B) He inspires orderly, peaceful worship where the spirit of the prophet remains subject to the prophet's control",
                "C) He demands that all church members speak at the exact same time as loudly as possible",
                "D) He prohibits any preaching from the Bible"
            ],
            "answer": "B",
            "explanation": "Paul explicitly states that 'the spirits of prophets are subject to the control of prophets' because 'God is not a God of disorder but of peace,' meaning genuine manifestations maintain self-control and order."
        }
    },

    # ─── LESSON 8 ────────────────────────────────────────────────────────────
    {
        "unit_order": 8,
        "unit_name": "Proper Use and Misuse of Spiritual Gifts",
        "unit_description": "Contrast constructive, biblical stewardship of spiritual gifts with common contemporary misuses including pride, commercialization (Simonism), and disorder.",
        "lesson_title": "Proper Use and Misuse of Spiritual Gifts",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Mechelen_St_-_Jan_Lucas_Franchoys_Descent_of_the_Holy_Spirit_02.jpg",
            "title": "Visual Hook: Faithful Stewardship in the Church",
            "author": "Jan Lucas Franchoys (1616–1681), Church of St. John, Mechelen",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Disciples of Christ exercising their gifts with humility, integrity, and sacrificial devotion for the edification of the community."
        },
        "youtube": {
            "youtube_id": "yiSjZXmAe08",
            "title": "BibleProject: Order and Edification (1 Corinthians 14)",
            "description": "An insightful exploration of 1 Corinthians 14, detailing Paul's guidelines for orderly worship, intelligible preaching, and using gifts to build up others."
        },
        "svg_fn": get_svg_lesson_8,
        "goals": [
            "Contrast the proper, biblical use of spiritual gifts with critical contemporary misuses in society.",
            "Explain the concept of Christian stewardship in managing God-given spiritual abilities (1 Peter 4:10).",
            "Commit to utilizing personal talents and spiritual gifts with integrity, humility, and selfless service."
        ],
        "intro": "Have you ever seen someone who possessed extraordinary technical brilliance—like a master computer coder—who used their gifts to hack into bank accounts and steal money instead of developing helpful educational software? The person is undeniably gifted, but they are misusing their ability for destructive greed.\n\nIn the spiritual life, the exact same tragedy can happen. Divine gifts given freely by God to heal, comfort, and build community can be hijacked by proud or greedy individuals to exploit vulnerable believers. Let us examine how we can honor God as faithful, clean stewards of His spiritual grace.",
        "core_scripture": "### Scriptural Passages: 1 Corinthians 14:26-40, 1 Peter 4:10-11, & Acts 8:18-20\n\n> *\"Each of you should use whatever gift you have received to serve others, as faithful stewards of God's grace in its various forms. If anyone speaks, they should do so as one who speaks the very words of God. If anyone serves, they should do so with the strength God provides, so that in all things God may be praised through Jesus Christ.\"* (1 Peter 4:10-11)\n\n> *\"What then shall we say, brothers and sisters? When you come together, each of you has a hymn, or a word of instruction, a revelation, a tongue or an interpretation. Everything must be done so that the church may be built up... For God is not a God of disorder but of peace... But all things should be done decently and in order.\"* (1 Corinthians 14:26, 33, 40)",
        "theological_pillars": "### Stewardship vs Exploitation: A Direct Contrast\n\n1. **Biblical Stewardship (*Oikonomia*):** In 1 Peter 4:10, believers are called 'stewards of God's grace'. A steward does not own the resources; they manage them on behalf of the Master for the benefit of the entire household.\n2. **Three Proper Uses of Spiritual Gifts:**\n   - **1. Edification of the Church:** Strengthening the weak, comforting the grieving, and teaching believers to mature in faith (1 Cor 14:3).\n   - **2. Advancing the Gospel:** Demonstrating the reality, compassion, and power of God to lead unbelievers to repentance (1 Cor 14:24-25).\n   - **3. Selfless Service to the Needy:** Using wisdom, giving, and mercy to care for orphans, widows, the poor, and the sick.\n3. **Three Critical Misuses of Spiritual Gifts Today:**\n   - **1. Spiritual Pride & Showmanship:** Using gifts publicly to impress others, gain social media clout, or claim spiritual superiority (1 Cor 12:21).\n   - **2. Commercialization (Simonism):** Demanding money, tithes, or material favors in exchange for prophetic words or healing prayers, echoing Simon the Sorcerer in Acts 8:18-20.\n   - **3. Sowing Division and Strife:** Using alleged 'prophecies' to turn family members against each other or manipulate church leadership.",
        "deep_dive": "### Deep Dive: Simonism and the Free Grace of God\n\nIn Acts 8:18-20, a magician named Simon saw the Apostles imparting the Holy Spirit through laying on of hands and offered them money, saying: *'Give me also this power.'* Peter sternly rebuked him: *'May your money perish with you, because you thought you could buy the gift of God with money!'*\n\n- **The Root of Simonism:** Commercializing divine power for financial gain or personal prestige.\n- **The Remedy:** True Christian servants remember Christ's mandate: *'Freely you have received; freely give'* (Matthew 10:8). Spiritual gifts must never be commodified.",
        "practical": {
            "title": "Action Framework: Serving with Blameless Integrity",
            "steps": [
                "Step 1: Check Your Motives — Before taking on any leadership, prayer, or music ministry, ask: 'Am I doing this for God's glory or human praise?'",
                "Step 2: Refuse Commercial Exploitation — Never demand or accept money, favors, or gifts in exchange for praying for others.",
                "Step 3: Prioritize Practical Service — Complement spiritual gifts with practical acts of kindness: tutoring struggling classmates, cleaning, and helping the poor.",
                "Step 4: Welcome Accountability — Submit your service and teachings to the oversight of mature Christian mentors and pastors."
            ]
        },
        "kenyan_context": "In Kenya, community fundraising (Harambee) and church tithes are intended to build schools, hospitals, and support church missions. However, when rogue preachers exploit believers by selling 'anointing oils' or demanding 'seed money' for miracles, it damages faith. Grade 9 learners must champion integrity and selfless service in their communities.",
        "reflection": "### Reflection on Faithful Stewardship\n\nReflect on how you handle your God-given gifts:\n- If God has blessed you with public speaking, music, leadership, or academic brilliance, are you using it to serve others or to gain praise for yourself?\n- How can you ensure that in all things, 'God may be praised through Jesus Christ' rather than yourself?",
        "takeaways": [
            "Christians are stewards of God's grace, entrusted with spiritual gifts to serve others selflessly (1 Peter 4:10).",
            "Proper uses of gifts include edifying the Church, spreading the Gospel, and meeting the needs of the vulnerable.",
            "Misuses include spiritual pride, showmanship, sowing division, and commercializing God's free grace (Simonism).",
            "All spiritual operations must be governed by love, humility, and orderly conduct that builds up the body of Christ."
        ],
        "mcq": {
            "question": "What serious spiritual offense, illustrated by Simon the Sorcerer in Acts 8:18-20, occurs when someone attempts to sell or buy God's spiritual gifts for money?",
            "options": [
                "A) Hermeneutics",
                "B) Simonism (Commercialization of spiritual gifts)",
                "C) Exegesis",
                "D) Liturgical Reformation"
            ],
            "answer": "B",
            "explanation": "Simonism is the sin of commercializing, buying, or selling spiritual gifts and divine power for financial gain or personal prestige, vehemently condemned by Apostle Peter in Acts 8."
        }
    }
]


# ─── MAIN INGESTION FUNCTION ──────────────────────────────────────────────────

def ingest_grade9_cre_topic12():
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 9 CRE — Topic 12: The Gifts of the Holy Spirit")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade 9, CRE, and Topic 12
        curriculum = Curriculum.objects.get(id=5) # CBC
        grade = Grade.objects.get(id=18)          # Grade 9
        subject = Subject.objects.get(id=50, grade=grade) # CRE

        print(f"[✓] Resolved Curriculum: {curriculum.name} (ID: {curriculum.id})")
        print(f"[✓] Resolved Grade     : {grade.name} (ID: {grade.id}, Level: {grade.level})")
        print(f"[✓] Resolved Subject   : {subject.name} (ID: {subject.id})")

        # Resolve or create Topic 12 under Subject 50
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=12,
            defaults={
                "name": "The Gifts of the Holy Spirit",
                "description": clean_text(
                    "This topic explores the spiritual resources God provides to His Church. "
                    "It details the role of the Holy Spirit as taught by Jesus, analyzes the nine spiritual gifts "
                    "listed by Paul, classifies them systematically, establishes biblical criteria for discerning genuine spiritual "
                    "manifestations, and warns against false teachings and ungodly cults."
                )
            }
        )
        if created:
            print(f"[✓] Created Topic 12: '{topic.name}' (ID: {topic.id})")
        else:
            topic.name = "The Gifts of the Holy Spirit"
            topic.description = clean_text(
                "This topic explores the spiritual resources God provides to His Church. "
                "It details the role of the Holy Spirit as taught by Jesus, analyzes the nine spiritual gifts "
                "listed by Paul, classifies them systematically, establishes biblical criteria for discerning genuine spiritual "
                "manifestations, and warns against false teachings and ungodly cults."
            )
            topic.save()
            print(f"[✓] Resolved existing Topic 12: '{topic.name}' (ID: {topic.id})")

        # 2. Clear previous units/lessons under Topic 12 for clean idempotent execution
        existing_units = LearningUnit.objects.filter(topic=topic)
        for unit in existing_units:
            for lsn in unit.lessons.all():
                lsn.blocks.all().delete()
                lsn.assets.all().delete()
                lsn.delete()
            unit.delete()
        # Also clean any orphaned lessons directly under topic
        for lsn in Lesson.objects.filter(topic=topic):
            lsn.blocks.all().delete()
            lsn.assets.all().delete()
            lsn.delete()
        print("[✓] Cleared previous units and lessons under Topic 12 for clean idempotent rebuild.")

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
                    "topic_order": 12,
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
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_12_lesson_{u_order}.svg",
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
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 12:")
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
    ingest_grade9_cre_topic12()
