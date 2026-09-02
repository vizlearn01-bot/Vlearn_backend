"""
VLearn CBC Grade 10 CRE — Topic 1.2: Methods of Studying the Holy Bible
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: CRE (Subject ID: 46)
Topic: Topic 1.2: Methods of Studying the Holy Bible (Order: 2)

Learning Units / Lessons:
  Unit 1 / Lesson 1: Sharing Experiences and Brainstorming Study Methods (6 Pages, 8 Blocks)
  Unit 2 / Lesson 2: Exploring Five Methods of Studying the Bible (6 Pages, 8 Blocks)
  Unit 3 / Lesson 3: Examining the Benefits of Studying the Holy Bible (6 Pages, 8 Blocks)
  Unit 4 / Lesson 4: Applying the Inductive Bible Study Method (7 Pages, 9 Blocks)
  Unit 5 / Lesson 5: Utilising the Biography Method (Book of Jonah) & Daily Reading (7 Pages, 9 Blocks)
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    """Removes bracket citations, internal tags, and normalizes formatting."""
    if not text:
        return ""
    # Strip citation brackets e.g. [182, 315], [223], [VISUAL: ...], [BIBLE PASSAGE: ...]
    text = re.sub(r'\[(?:VISUAL|BIBLE PASSAGE|INTERACTION|REAL WORLD APPLICATION):?[^\]]*\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

# ==============================================================================
# SVG VECTOR DIAGRAMS
# ==============================================================================

SVG_LESSON_1_CYCLE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="grad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <!-- Title -->
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">THE 4-STAGE BIBLE STUDY CYCLE</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="13">A continuous, systematic methodology for transformative scripture study</text>

  <!-- Central Hub -->
  <circle cx="400" cy="245" r="55" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <text x="400" y="240" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">LIFELONG</text>
  <text x="400" y="258" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="bold">GROWTH</text>

  <!-- Stage 1: Preparation (Top Left) -->
  <g transform="translate(60, 95)">
    <rect x="0" y="0" width="280" height="120" rx="12" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect x="15" y="15" width="36" height="36" rx="8" fill="url(#grad1)"/>
    <text x="33" y="39" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">1</text>
    <text x="62" y="38" fill="#60a5fa" font-size="15" font-weight="bold">PREPARATION</text>
    <text x="15" y="72" fill="#cbd5e1" font-size="12">• Choose method &amp; select passage</text>
    <text x="15" y="92" fill="#cbd5e1" font-size="12">• Pray for guidance &amp; quiet your mind</text>
  </g>

  <!-- Stage 2: Investigation (Top Right) -->
  <g transform="translate(460, 95)">
    <rect x="0" y="0" width="280" height="120" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="15" y="15" width="36" height="36" rx="8" fill="url(#grad2)"/>
    <text x="33" y="39" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">2</text>
    <text x="62" y="38" fill="#34d399" font-size="15" font-weight="bold">INVESTIGATION</text>
    <text x="15" y="72" fill="#cbd5e1" font-size="12">• Read carefully and observe clues</text>
    <text x="15" y="92" fill="#cbd5e1" font-size="12">• Note context, keywords &amp; background</text>
  </g>

  <!-- Stage 3: Reflection (Bottom Right) -->
  <g transform="translate(460, 265)">
    <rect x="0" y="0" width="280" height="120" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="15" y="15" width="36" height="36" rx="8" fill="url(#grad3)"/>
    <text x="33" y="39" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">3</text>
    <text x="62" y="38" fill="#fbbf24" font-size="15" font-weight="bold">REFLECTION</text>
    <text x="15" y="72" fill="#cbd5e1" font-size="12">• Discern core theological truth</text>
    <text x="15" y="92" fill="#cbd5e1" font-size="12">• Let the message search your heart</text>
  </g>

  <!-- Stage 4: Integration (Bottom Left) -->
  <g transform="translate(60, 265)">
    <rect x="0" y="0" width="280" height="120" rx="12" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <rect x="15" y="15" width="36" height="36" rx="8" fill="url(#grad4)"/>
    <text x="33" y="39" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">4</text>
    <text x="62" y="38" fill="#a78bfa" font-size="15" font-weight="bold">INTEGRATION</text>
    <text x="15" y="72" fill="#cbd5e1" font-size="12">• Plan concrete daily life action</text>
    <text x="15" y="92" fill="#cbd5e1" font-size="12">• Live out ethical obedience</text>
  </g>

  <!-- Connecting Directional Lines & Arrows -->
  <path d="M 345 155 L 450 155" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#arrow)" stroke-dasharray="4 4"/>
  <path d="M 600 220 L 600 260" stroke="#34d399" stroke-width="2.5" stroke-dasharray="4 4"/>
  <path d="M 455 325 L 345 325" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4 4"/>
  <path d="M 200 260 L 200 220" stroke="#a78bfa" stroke-width="2.5" stroke-dasharray="4 4"/>
</svg>"""

SVG_LESSON_2_METHODS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 480" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Title -->
  <text x="410" y="35" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">THE 5 BIBLE STUDY METHODS FRAMEWORK</text>
  <text x="410" y="58" text-anchor="middle" fill="#94a3b8" font-size="13">Selecting the right theological tool for your specific learning goal</text>

  <!-- Method 1: Devotional -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="760" height="66" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="12" y="12" width="160" height="42" rx="6" fill="#0284c7"/>
    <text x="92" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">1. DEVOTIONAL</text>
    <text x="190" y="29" fill="#38bdf8" font-size="12" font-weight="bold">Focus: Personal Reflection &amp; Prayer</text>
    <text x="190" y="49" fill="#cbd5e1" font-size="11">Best for: Daily quiet time | Key Question: How does this truth guide my heart today?</text>
  </g>

  <!-- Method 2: Topical -->
  <g transform="translate(30, 155)">
    <rect x="0" y="0" width="760" height="66" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect x="12" y="12" width="160" height="42" rx="6" fill="#059669"/>
    <text x="92" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">2. TOPICAL</text>
    <text x="190" y="29" fill="#34d399" font-size="12" font-weight="bold">Focus: Cross-Referencing Specific Themes</text>
    <text x="190" y="49" fill="#cbd5e1" font-size="11">Best for: Ethics, Justice, Forgiveness | Uses: Concordance &amp; Topical indexes</text>
  </g>

  <!-- Method 3: Character Study -->
  <g transform="translate(30, 230)">
    <rect x="0" y="0" width="760" height="66" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect x="12" y="12" width="160" height="42" rx="6" fill="#d97706"/>
    <text x="92" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">3. CHARACTER STUDY</text>
    <text x="190" y="29" fill="#fbbf24" font-size="12" font-weight="bold">Focus: Biographical Narrative Analysis</text>
    <text x="190" y="49" fill="#cbd5e1" font-size="11">Best for: Life lessons, role models, warnings | Example: Abraham, Ruth, Jonah</text>
  </g>

  <!-- Method 4: Verse-by-Verse -->
  <g transform="translate(30, 305)">
    <rect x="0" y="0" width="760" height="66" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect x="12" y="12" width="160" height="42" rx="6" fill="#7c3aed"/>
    <text x="92" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">4. VERSE-BY-VERSE</text>
    <text x="190" y="29" fill="#a78bfa" font-size="12" font-weight="bold">Focus: Expository &amp; Microscopic Flow</text>
    <text x="190" y="49" fill="#cbd5e1" font-size="11">Best for: Deep academic book study | Examines grammar, syntax &amp; historical context</text>
  </g>

  <!-- Method 5: Inductive -->
  <g transform="translate(30, 380)">
    <rect x="0" y="0" width="760" height="66" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect x="12" y="12" width="160" height="42" rx="6" fill="#e11d48"/>
    <text x="92" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">5. INDUCTIVE</text>
    <text x="190" y="29" fill="#fb7185" font-size="12" font-weight="bold">Focus: Observation → Interpretation → Application</text>
    <text x="190" y="49" fill="#cbd5e1" font-size="11">Best for: Objective scripture discovery | Prevents premature assumptions</text>
  </g>
</svg>"""

SVG_LESSON_3_BENEFITS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Title -->
  <text x="400" y="38" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">FOUR DIMENSIONS OF BIBLE STUDY BENEFITS</text>
  <text x="400" y="62" text-anchor="middle" fill="#94a3b8" font-size="13">Holistic transformation of mind, character, spirit, and community</text>

  <!-- Quadrant 1: Spiritual (Top Left) -->
  <g transform="translate(50, 90)">
    <rect x="0" y="0" width="335" height="150" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#0284c7"/>
    <text x="35" y="40" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">✝</text>
    <text x="65" y="40" fill="#38bdf8" font-size="15" font-weight="bold">SPIRITUAL GROWTH</text>
    <text x="20" y="75" fill="#cbd5e1" font-size="12">• Revelation of God's true holy character</text>
    <text x="20" y="98" fill="#cbd5e1" font-size="12">• Unshakeable faith, peace &amp; hope in trials</text>
    <text x="20" y="121" fill="#cbd5e1" font-size="12">• Living relationship with the Creator</text>
  </g>

  <!-- Quadrant 2: Moral & Character (Top Right) -->
  <g transform="translate(415, 90)">
    <rect x="0" y="0" width="335" height="150" rx="12" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#059669"/>
    <text x="35" y="40" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">★</text>
    <text x="65" y="40" fill="#34d399" font-size="15" font-weight="bold">MORAL TRANSFORMATION</text>
    <text x="20" y="75" fill="#cbd5e1" font-size="12">• Word acts as a mirror exposing pride</text>
    <text x="20" y="98" fill="#cbd5e1" font-size="12">• Clear ethical compass for youth choices</text>
    <text x="20" y="121" fill="#cbd5e1" font-size="12">• Development of integrity and self-control</text>
  </g>

  <!-- Quadrant 3: Intellectual (Bottom Left) -->
  <g transform="translate(50, 260)">
    <rect x="0" y="0" width="335" height="150" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#d97706"/>
    <text x="35" y="40" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">💡</text>
    <text x="65" y="40" fill="#fbbf24" font-size="15" font-weight="bold">INTELLECTUAL SHARPNESS</text>
    <text x="20" y="75" fill="#cbd5e1" font-size="12">• Critical thinking &amp; analytical discernment</text>
    <text x="20" y="98" fill="#cbd5e1" font-size="12">• Historical, literary &amp; cultural literacy</text>
    <text x="20" y="121" fill="#cbd5e1" font-size="12">• Synthesizing complex narrative themes</text>
  </g>

  <!-- Quadrant 4: Social & Community (Bottom Right) -->
  <g transform="translate(415, 260)">
    <rect x="0" y="0" width="335" height="150" rx="12" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#e11d48"/>
    <text x="35" y="40" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">🤝</text>
    <text x="65" y="40" fill="#fb7185" font-size="15" font-weight="bold">COMMUNITY &amp; JUSTICE</text>
    <text x="20" y="75" fill="#cbd5e1" font-size="12">• Dismantling prejudice &amp; tribal divisions</text>
    <text x="20" y="98" fill="#cbd5e1" font-size="12">• Championing social justice for the weak</text>
    <text x="20" y="121" fill="#cbd5e1" font-size="12">• Living out sacrificial love for neighbors</text>
  </g>
</svg>"""

SVG_LESSON_4_INDUCTIVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Title -->
  <text x="400" y="35" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">THE INDUCTIVE STUDY LADDER</text>
  <text x="400" y="58" text-anchor="middle" fill="#94a3b8" font-size="13">Sequential 3-step discipline: Never leap to application without observation!</text>

  <!-- Step 3: Application (Top) -->
  <g transform="translate(100, 85)">
    <rect x="0" y="0" width="600" height="95" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="18" y="16" width="140" height="62" rx="8" fill="#059669"/>
    <text x="88" y="42" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">STEP 3</text>
    <text x="88" y="62" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="bold">APPLICATION</text>
    <text x="180" y="38" fill="#34d399" font-size="15" font-weight="bold">"How does this apply to my life today?"</text>
    <text x="180" y="62" fill="#cbd5e1" font-size="12">• Concrete obedience, behavioral changes &amp; prayerful response</text>
  </g>

  <!-- Arrow Up 2 -->
  <path d="M 400 195 L 400 205" stroke="#34d399" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="415" y="200" fill="#94a3b8" font-size="10" font-weight="bold">BUILDS UPON</text>

  <!-- Step 2: Interpretation (Middle) -->
  <g transform="translate(100, 205)">
    <rect x="0" y="0" width="600" height="95" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="18" y="16" width="140" height="62" rx="8" fill="#d97706"/>
    <text x="88" y="42" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">STEP 2</text>
    <text x="88" y="62" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="bold">INTERPRETATION</text>
    <text x="180" y="38" fill="#fbbf24" font-size="15" font-weight="bold">"What does the text mean?"</text>
    <text x="180" y="62" fill="#cbd5e1" font-size="12">• Original historical context, author's intent &amp; theological principles</text>
  </g>

  <!-- Arrow Up 1 -->
  <path d="M 400 315 L 400 325" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="415" y="320" fill="#94a3b8" font-size="10" font-weight="bold">FOUNDATION</text>

  <!-- Step 1: Observation (Base) -->
  <g transform="translate(100, 325)">
    <rect x="0" y="0" width="600" height="95" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="18" y="16" width="140" height="62" rx="8" fill="#0284c7"/>
    <text x="88" y="42" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">STEP 1</text>
    <text x="88" y="62" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="bold">OBSERVATION</text>
    <text x="180" y="38" fill="#38bdf8" font-size="15" font-weight="bold">"What does the text say?"</text>
    <text x="180" y="62" fill="#cbd5e1" font-size="12">• Who, What, Where, When, key repeated words &amp; grammatical structure</text>
  </g>
</svg>"""

SVG_LESSON_5_BIOGRAPHY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 460" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Title -->
  <text x="410" y="35" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="bold">THE BIOGRAPHY METHOD &amp; PROPHET JONAH'S JOURNEY</text>
  <text x="410" y="58" text-anchor="middle" fill="#94a3b8" font-size="13">Examining character choices, divine sovereignty, and heart transformation</text>

  <!-- Stage 1: The Rebellion -->
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="175" height="150" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" fill="#f87171" font-size="13" font-weight="bold">1. REBELLION</text>
    <text x="12" y="60" fill="#fca5a5" font-size="11" font-weight="bold">Call to Nineveh:</text>
    <text x="12" y="80" fill="#cbd5e1" font-size="10">• Flees to Tarshish</text>
    <text x="12" y="100" fill="#cbd5e1" font-size="10">• Boarded ship at Joppa</text>
    <text x="12" y="125" fill="#94a3b8" font-size="10">Motivated by hatred</text>
  </g>

  <!-- Stage 2: Consequence & Fish -->
  <g transform="translate(225, 85)">
    <rect x="0" y="0" width="175" height="150" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">2. RESCUE</text>
    <text x="12" y="60" fill="#fde68a" font-size="11" font-weight="bold">Storm &amp; Great Fish:</text>
    <text x="12" y="80" fill="#cbd5e1" font-size="10">• Thrown into ocean</text>
    <text x="12" y="100" fill="#cbd5e1" font-size="10">• 3 days in fish belly</text>
    <text x="12" y="125" fill="#94a3b8" font-size="10">Repentance &amp; Prayer</text>
  </g>

  <!-- Stage 3: Second Chance -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="175" height="150" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" fill="#60a5fa" font-size="13" font-weight="bold">3. PREACHING</text>
    <text x="12" y="60" fill="#93c5fd" font-size="11" font-weight="bold">Obedience in Nineveh:</text>
    <text x="12" y="80" fill="#cbd5e1" font-size="10">• Preaches judgment</text>
    <text x="12" y="100" fill="#cbd5e1" font-size="10">• Whole city repents</text>
    <text x="12" y="125" fill="#94a3b8" font-size="10">God relents &amp; forgives</text>
  </g>

  <!-- Stage 4: Heart Lesson -->
  <g transform="translate(615, 85)">
    <rect x="0" y="0" width="175" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">4. THE LESSON</text>
    <text x="12" y="60" fill="#a7f3d0" font-size="11" font-weight="bold">The Leafy Vine &amp; Worm:</text>
    <text x="12" y="80" fill="#cbd5e1" font-size="10">• Jonah's anger exposed</text>
    <text x="12" y="100" fill="#cbd5e1" font-size="10">• God cares for 120k</text>
    <text x="12" y="125" fill="#94a3b8" font-size="10">Universal compassion</text>
  </g>

  <!-- Bottom Banner: Daily Reflection Habit -->
  <g transform="translate(30, 260)">
    <rect x="0" y="0" width="760" height="165" rx="12" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <text x="380" y="32" text-anchor="middle" fill="#818cf8" font-size="14" font-weight="bold">THE DAILY DEVOTIONAL REFLECTION JOURNAL (5 PROMPTS)</text>
    <text x="25" y="65" fill="#cbd5e1" font-size="12"><tspan fill="#a5b4fc" font-weight="bold">1. What passage did I read today?</tspan> (Establishes specific reference)</text>
    <text x="25" y="88" fill="#cbd5e1" font-size="12"><tspan fill="#a5b4fc" font-weight="bold">2. What stood out to me?</tspan> (Focuses on key observations and phrases)</text>
    <text x="25" y="111" fill="#cbd5e1" font-size="12"><tspan fill="#a5b4fc" font-weight="bold">3. What does it teach about God &amp; humanity?</tspan> (Theological interpretation)</text>
    <text x="25" y="134" fill="#cbd5e1" font-size="12"><tspan fill="#a5b4fc" font-weight="bold">4. How will I apply it today?</tspan> (Concrete, measurable personal action)</text>
    <text x="25" y="157" fill="#cbd5e1" font-size="12"><tspan fill="#a5b4fc" font-weight="bold">5. What question or prayer do I have?</tspan> (Honest personal dialogue with God)</text>
  </g>
</svg>"""

# ==============================================================================
# LESSON CURRICULUM DEFINITIONS
# ==============================================================================

TOPIC_1_2_LESSONS = [
    # --------------------------------------------------------------------------
    # LESSON 1: Sharing Experiences and Brainstorming Study Methods
    # --------------------------------------------------------------------------
    {
        "unit_order": 1,
        "unit_name": "Sharing Experiences and Brainstorming Study Methods",
        "unit_description": "Personal experiences with Bible reading, common barriers, comparative study skills across disciplines, and introducing systematic Bible study methods.",
        "lesson_title": "Sharing Experiences & Brainstorming Bible Study Methods",
        "pages": [
            # Page 1: Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Exploring the Treasures of Scripture",
                    "content": {
                        "title": "Exploring the Treasures of Scripture",
                        "caption": "An open copy of the Holy Bible with handwritten study notes, illustrating active investigation and methodical study.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Open_Bible.jpg",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0",
                        "verified": True
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Bible Study Foundations",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Reflect on personal experiences and common challenges encountered when reading the Bible\n- Compare how we study general academic texts with how we study Biblical literature\n- Brainstorm and outline systematic methods for analyzing Scripture"
                    }
                }
            ],
            # Page 2: Concept Explanation & Academic Connection
            [
                {
                    "type": "concept_explanation",
                    "title": "Reading vs. Systematic Studying",
                    "content": {
                        "text": "Suppose you are given a map of a vast, dense forest containing a hidden treasure. If you simply glance at the map for ten seconds, will you find the treasure? No. You must study the lines, understand the symbols, calculate the scale, and plan your route systematically.\n\nThe Bible is a vast landscape of divine truth. To discover its treasures, we cannot just skim through it randomly; we need structured methods of study.\n\n### Applying Academic Study Skills to Scripture\nThink about how you study other subjects:\n- **Science Textbooks:** You examine diagrams, define technical terms, and trace causal processes.\n- **History:** When learning about figures like Nelson Mandela or Jomo Kenyatta, you examine their background, struggles, motivations, and impact on society.\n- **Literature:** You analyze themes, character motivations, plot conflicts, and the writer's style.\n\nWe can apply these exact critical thinking skills to the study of the Holy Bible!"
                    }
                }
            ],
            # Page 3: Common Challenges & Brainstormed Approaches
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Challenges and Brainstormed Solutions",
                    "content": {
                        "text": "Many people who attempt to read the Bible encounter real obstacles:\n- **The Language Barrier:** Ancient phrasing, idioms, or unfamiliar theological concepts.\n- **Lack of Historical Context:** Reading about ancient cities (like Nineveh, Babylon, or Jerusalem) and customs without understanding their cultural significance.\n- **Lack of Consistency:** Reading a random verse here and there without a coherent, ongoing plan.\n\n### Core Brainstormed Approaches\nDuring a classroom brainstorming session, students identify several complementary ways to approach Scripture:\n1. **Personal Quiet Reflection:** Reading a short passage and praying for personal guidance.\n2. **Thematic Exploration:** Tracing a single theme (like Love, Justice, or Peace) across multiple books.\n3. **Biographical Investigation:** Studying the life choices and spiritual lessons of a biblical figure.\n4. **Sequential Expository Study:** Analyzing a book verse-by-verse from beginning to end."
                    }
                }
            ],
            # Page 4: Visual Diagram — The Bible Study Cycle
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Four-Stage Bible Study Cycle",
                    "content": {
                        "title": "The Four-Stage Bible Study Cycle",
                        "caption": "A pedagogical vector diagram illustrating the continuous cycle of Preparation, Investigation, Reflection, and Integration.",
                        "svg_content": SVG_LESSON_1_CYCLE
                    }
                }
            ],
            # Page 5: Curated Educational Video
            [
                {
                    "type": "suggested_video",
                    "title": "Educational Video: How to Read and Study the Bible",
                    "content": {
                        "title": "How to Read and Study the Bible - BibleProject Overview",
                        "description": "An engaging overview exploring how the Bible is a diverse collection of literary styles designed for thoughtful, lifelong meditation and systematic study.",
                        "url": "https://www.youtube.com/watch?v=7_CGP-12AE0",
                        "youtube_id": "7_CGP-12AE0"
                    }
                }
            ],
            # Page 6: Knowledge Check & Key Takeaway
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: The Value of Study Methods",
                    "content": {
                        "question": "Why are systematic 'methods' of Bible study helpful compared to just reading random verses?",
                        "options": [
                            "A) They make the reader holier and superior to other people.",
                            "B) They help overcome barriers like lack of context, language difficulty, and fragmentation of ideas.",
                            "C) They allow the reader to predict specific future dates and lottery numbers.",
                            "D) They eliminate the need to ever ask questions about faith."
                        ],
                        "correct_answer": "B",
                        "explanation": "Systematic Bible study methods guide us through historical, literary, and practical contexts, preventing misinterpretation and unlocking the rich meaning of God's Word."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson Summary & Core Values",
                    "content": {
                        "text": "- **Openness to Learning:** Approach Scripture with humility, recognizing that structured methods help us understand what we do not know.\n- **Intellectual Rigor:** Applying careful investigation and academic discipline to spiritual texts yields deeper, life-transforming insights.\n- **From Skimming to Studying:** Moving from passive reading to active study bridges ancient context with modern daily life."
                    }
                }
            ]
        ]
    },

    # --------------------------------------------------------------------------
    # LESSON 2: Exploring Five Methods of Studying the Bible
    # --------------------------------------------------------------------------
    {
        "unit_order": 2,
        "unit_name": "Exploring Five Methods of Studying the Bible",
        "unit_description": "Detailed definition, mechanics, strengths, and limitations of the 5 established Bible study methods: Devotional, Topical, Character Study, Verse-by-Verse, and Inductive.",
        "lesson_title": "Exploring Five Methods of Studying the Holy Bible",
        "pages": [
            # Page 1: Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "The Theologian's Study Toolkit",
                    "content": {
                        "title": "The Theologian's Study Toolkit",
                        "caption": "Historical printed Latin Bible open for scholarly cross-referencing and verse examination.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Gutenberg_Bible%2C_Lenox_Copy%2C_New_York_Public_Library%2C_2009._Pic_01.jpg",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0",
                        "verified": True
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Five Study Methods",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define and explain the five major methods of studying the Holy Bible\n- Analyze the unique strengths and limitations of each study method\n- Select the most appropriate method for different personal, spiritual, and academic study goals"
                    }
                }
            ],
            # Page 2: Methods 1, 2, and 3 Explained
            [
                {
                    "type": "concept_explanation",
                    "title": "Devotional, Topical, and Character Study Methods",
                    "content": {
                        "text": "If you want to build a house, you cannot do the entire job using only a hammer. You need a trowel for bricks, a saw for timber, and a level for walls. In the same way, Christians and scholars utilize different study methods depending on their purpose.\n\n### 1. The Devotional Method\n- **How it works:** Read a brief passage (3-5 verses), quiet your mind, and ask: *What is God saying to me personally today? How does this comfort or guide me?*\n- **Strength:** Highly personal, builds intimacy with God, and feeds daily spiritual devotion.\n- **Limitation:** Can lead to self-centered interpretation if original historical context is ignored.\n\n### 2. The Topical Method\n- **How it works:** Choose a specific subject or ethical issue (e.g., *Forgiveness, Justice, Stewardship*). Use a **Concordance** to trace verses across multiple books and synthesize their teachings.\n- **Strength:** Provides a comprehensive, systematic theological understanding of a theme.\n- **Limitation:** Risk of 'proof-texting' (taking isolated verses out of their original literary context).\n\n### 3. The Character Study (Biographical) Method\n- **How it works:** Trace the life, choices, motivations, crises, and spiritual legacy of a biblical figure (e.g., Abraham, Ruth, David, Jonah, or Paul).\n- **Strength:** Highly practical; teaches life lessons through real human successes and failures.\n- **Limitation:** Readers must distinguish between description (what a person did) and prescription (what God commands)."
                    }
                }
            ],
            # Page 3: Methods 4 and 5 Explained
            [
                {
                    "type": "concept_explanation",
                    "title": "Verse-by-Verse and Inductive Methods",
                    "content": {
                        "text": "### 4. The Verse-by-Verse (Expository) Method\n- **How it works:** A microscopic, detailed analysis of every single verse in a chapter or book, examining word definitions, sentence syntax, historical cross-references, and the logical flow of the author's argument.\n- **Strength:** Extremely accurate; prevents taking verses out of context.\n- **Limitation:** Requires significant time, academic discipline, and study reference tools.\n\n### 5. The Inductive Method\n- **How it works:** A rigorous, objective 3-step investigation:\n  1. **Observation:** *What does the text say?* (Raw facts, words, actors)\n  2. **Interpretation:** *What does the text mean?* (Original author intent & theology)\n  3. **Application:** *How does this apply to me today?* (Concrete action)\n- **Strength:** Objective and logical; allows scripture to speak for itself before drawing conclusions.\n- **Limitation:** Demands patience to complete observation and interpretation before jumping to application."
                    }
                }
            ],
            # Page 4: Visual Diagram — Methods Framework
            [
                {
                    "type": "suggested_diagram",
                    "title": "Overview of the Five Bible Study Methods",
                    "content": {
                        "title": "Overview of the Five Bible Study Methods",
                        "caption": "A structured vector matrix comparing the core focus, ideal use case, and primary question for all five methods.",
                        "svg_content": SVG_LESSON_2_METHODS
                    }
                }
            ],
            # Page 5: Curated Educational Video
            [
                {
                    "type": "suggested_video",
                    "title": "Educational Video: Exploring Bible Study Methods",
                    "content": {
                        "title": "Overview of Bible Study Approaches and Tools",
                        "description": "An instructional guide illustrating how to select between topical, character, and expository Bible study approaches for personal and group learning.",
                        "url": "https://www.youtube.com/watch?v=kU_W3EaHqB4",
                        "youtube_id": "kU_W3EaHqB4"
                    }
                }
            ],
            # Page 6: Knowledge Check & Key Takeaway
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Method Selection",
                    "content": {
                        "question": "If a CRE class wants to understand the Bible's complete teachings on 'Stewardship over Creation,' which method should they choose?",
                        "options": [
                            "A) The Devotional Method",
                            "B) The Character Study Method",
                            "C) The Topical Method",
                            "D) The Verse-by-Verse Method on a single psalm"
                        ],
                        "correct_answer": "C",
                        "explanation": "The Topical Method searches and synthesizes verses across the entire Bible relating to a specific subject, providing a comprehensive overview of Christian stewardship."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson Summary: Matching Tool to Goal",
                    "content": {
                        "text": "- **Devotional:** Best for daily personal prayer and heart reflection.\n- **Topical:** Best for exploring Christian ethical and thematic questions.\n- **Character Study:** Best for learning from real-life role models and warnings.\n- **Verse-by-Verse:** Best for in-depth scholarly analysis of an entire book.\n- **Inductive:** Best for objective, evidence-based scripture discovery."
                    }
                }
            ]
        ]
    },

    # --------------------------------------------------------------------------
    # LESSON 3: Examining the Benefits of Studying the Holy Bible
    # --------------------------------------------------------------------------
    {
        "unit_order": 3,
        "unit_name": "Examining the Benefits of Studying the Holy Bible",
        "unit_description": "Holistic benefits of Bible study across spiritual, moral, intellectual, and social/community dimensions, with real-world leader insights.",
        "lesson_title": "Examining the Benefits of Studying the Holy Bible",
        "pages": [
            # Page 1: Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "The Power of Daily Scripture Engagement",
                    "content": {
                        "title": "The Power of Daily Scripture Engagement",
                        "caption": "A Christian believer engaging in quiet study and reflection with an open Bible.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Bible.jpg",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0",
                        "verified": True
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Benefits of Bible Study",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Outline the spiritual, moral, intellectual, and social benefits of regular Bible study\n- Analyze insights from community leaders regarding the transformational power of Scripture\n- Develop a personal weekly Bible study plan to guide ethical decision-making"
                    }
                }
            ],
            # Page 2: Spiritual and Moral Benefits
            [
                {
                    "type": "concept_explanation",
                    "title": "Spiritual and Moral Transformation",
                    "content": {
                        "text": "When we commit to studying God's Word consistently, it impacts every aspect of our lives.\n\n### 1. Spiritual Benefits\n- **Knowing God's True Character:** The Bible is God's self-revelation. Studying it corrects false cultural superstitions and reveals His holiness, love, justice, and mercy.\n- **Anchor of Faith & Hope:** Reading God's promises during seasons of grief, doubt, or illness provides an enduring foundation of peace and comfort.\n\n### 2. Moral and Character Benefits\n- **The Word as a Moral Mirror:** Scripture reveals hidden pride, jealousy, or dishonesty, leading us toward repentance and character maturity.\n- **A Compass for Tough Choices:** In youth, peer pressure often creates ethical dilemmas. Biblical principles of integrity, justice, and self-control provide clear guidance."
                    }
                }
            ],
            # Page 3: Intellectual and Social/Community Benefits
            [
                {
                    "type": "concept_explanation",
                    "title": "Intellectual Sharpness and Social Transformation",
                    "content": {
                        "text": "### 3. Intellectual Benefits\n- **Critical Thinking and Wisdom:** Analyzing complex ancient texts, evaluating historical contexts, and synthesizing themes sharpens analytical ability and academic maturity.\n- **Cultural and Literary Literacy:** Understanding biblical history, metaphors, and poetry elevates overall communication and humanities performance.\n\n### 4. Social and Community Benefits\n- **Fostering Unity and Love:** Bible study teaches us to love our neighbors as ourselves, dismantling tribalism, xenophobia, and social prejudice.\n- **Advocacy for Social Justice:** Inspired by the Old Testament prophets (like Amos, Micah, and Isaiah) and Jesus Christ, believers are empowered to defend the vulnerable, the poor, and the marginalized."
                    }
                }
            ],
            # Page 4: Visual Diagram — Four Dimensions of Benefits
            [
                {
                    "type": "suggested_diagram",
                    "title": "Four Dimensions of Bible Study Benefits",
                    "content": {
                        "title": "Four Dimensions of Bible Study Benefits",
                        "caption": "A pedagogical infographic categorizing the holistic spiritual, moral, intellectual, and social impacts of Scripture study.",
                        "svg_content": SVG_LESSON_3_BENEFITS
                    }
                }
            ],
            # Page 5: Curated Educational Video
            [
                {
                    "type": "suggested_video",
                    "title": "Educational Video: How the Bible Transforms Society and Character",
                    "content": {
                        "title": "The Impact of Biblical Wisdom on Daily Life and Ethics",
                        "description": "An engaging exploration of how biblical wisdom literature reshapes human character, moral responsibility, and community flourishing.",
                        "url": "https://www.youtube.com/watch?v=gab36_m2fpo",
                        "youtube_id": "gab36_m2fpo"
                    }
                }
            ],
            # Page 6: Knowledge Check & Key Takeaway
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Moral and Social Impact",
                    "content": {
                        "question": "Which benefit of studying the Bible directly empowers a high school student to resist negative peer pressure?",
                        "options": [
                            "A) Memorizing the historical timeline of ancient Persian kings.",
                            "B) Moral transformation and internalizing an ethical compass founded on integrity and courage.",
                            "C) Knowing how many chapters are in the Old Testament.",
                            "D) Predicting future geopolitical alliances."
                        ],
                        "correct_answer": "B",
                        "explanation": "Moral transformation and having deeply internalized values of honesty and self-control give students the moral strength to resist negative peer pressure."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson Summary & Personal Application",
                    "content": {
                        "text": "- **Holistic Impact:** Bible study shapes our spirit (faith), character (moral integrity), mind (wisdom), and community (justice and unity).\n- **My Action Plan:** Choose a regular daily time (e.g. 15 minutes each morning), select an initial book (such as Luke or Proverbs), and invite a study partner for mutual accountability."
                    }
                }
            ]
        ]
    },

    # --------------------------------------------------------------------------
    # LESSON 4: Applying the Inductive Bible Study Method
    # --------------------------------------------------------------------------
    {
        "unit_order": 4,
        "unit_name": "Applying the Inductive Bible Study Method",
        "unit_description": "The 3-step inductive method (Observation, Interpretation, Application) with detailed workshop application to Matthew 13:44-46.",
        "lesson_title": "Applying the Inductive Bible Study Method",
        "pages": [
            # Page 1: Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "The Scripture Detective",
                    "content": {
                        "title": "The Scripture Detective",
                        "caption": "A student carefully examining ancient scripture texts with a magnifying lens, symbolizing meticulous observation.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Bible_Study_%28Unsplash%29.jpg",
                        "author": "Wikimedia Commons",
                        "licensing": "CC0 / Public Domain",
                        "verified": True
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: The Inductive Method",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Master the three sequential steps of the Inductive Method (Observation, Interpretation, Application)\n- Apply inductive analysis systematically to the parables in Matthew 13:44-46\n- Distinguish clearly between original author meaning and contemporary personal application"
                    }
                }
            ],
            # Page 2: The Three Steps Explained
            [
                {
                    "type": "concept_explanation",
                    "title": "The Three Inductive Steps: Observation, Interpretation, Application",
                    "content": {
                        "text": "A good detective never enters a crime scene and immediately guesses the outcome. First, they gather physical clues (Observation). Second, they reconstruct what happened and why (Interpretation). Third, they take legal action (Application). In Inductive Bible Study, you follow this exact disciplined progression:\n\n### Step 1: Observation — 'What does the text say?'\nAct like an investigative journalist. Read the passage multiple times and ask:\n- **Who** are the actors? **What** actions are taken? **Where** and **When** does this take place?\n- Which keywords, phrases, or comparisons are repeated?\n\n### Step 2: Interpretation — 'What does the text mean?'\nDiscover the meaning intended by the original author for the original audience:\n- What was the historical, cultural, or geographical background?\n- What core theological principle is being taught?\n\n### Step 3: Application — 'How does this truth apply to my life today?'\nTranslate timeless theological truths into personal, concrete daily action:\n- Is there a command to obey, a warning to heed, an example to follow, or a promise to trust?"
                    }
                }
            ],
            # Page 3: Visual Diagram — The Inductive Ladder
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Inductive Study Ladder",
                    "content": {
                        "title": "The Inductive Study Ladder",
                        "caption": "A pedagogical vector diagram depicting the three-step upward progression from Observation to Interpretation and Application.",
                        "svg_content": SVG_LESSON_4_INDUCTIVE
                    }
                }
            ],
            # Page 4: Workshop: Matthew 13:44-46
            [
                {
                    "type": "concept_explanation",
                    "title": "Practical Workshop: Matthew 13:44-46",
                    "content": {
                        "text": "Let us apply our inductive detective skills to Jesus' parables of the Hidden Treasure and the Priceless Pearl:\n\n> *'Again, the kingdom of heaven is like treasure hidden in a field, which a man found and hid; and for joy over it he goes and sells all that he has and buys that field.*\n>\n> *Again, the kingdom of heaven is like a merchant seeking beautiful pearls, who, when he had found one pearl of great price, went and sold all that he had and bought it.'* (Matthew 13:44-46)\n\n### 1. Observation (The Clues)\n- **Actors:** A man in a field; a merchant seeking fine pearls.\n- **Actions:** Finding, hiding, experiencing joy, selling *everything*, and buying the prize.\n- **Repeated Phrases:** 'Kingdom of heaven is like', 'found', 'sold all that he had', 'bought it'.\n\n### 2. Interpretation (The Meaning)\n- **Ancient Context:** In the ancient Near East without commercial banks, burying valuables protected them during wars. If a family died out, hidden treasure remained undiscovered for decades.\n- **Theological Meaning:** The Kingdom of God (salvation, knowing God, His eternal reign) possesses supreme, infinite worth. Finding it brings overwhelming joy, making any sacrifice of temporary earthly status worthwhile.\n\n### 3. Application (My Life Today)\n- **Personal Reflection:** Do I value my relationship with God as a supreme treasure or as a dull routine?\n- **Concrete Action:** Identify habits or distractions competing with spiritual growth (excessive screen time, dishonest compromises) and willingly surrender them to prioritize God's kingdom."
                    }
                }
            ],
            # Page 5: Curated Educational Video
            [
                {
                    "type": "suggested_video",
                    "title": "Educational Video: Step-by-Step Inductive Bible Study",
                    "content": {
                        "title": "How to Do Inductive Bible Study - Observation, Interpretation, Application",
                        "description": "A practical step-by-step masterclass demonstrating how to mark keywords, ask investigative questions, and draw faithful life applications.",
                        "url": "https://www.youtube.com/watch?v=fDoxZ-Goh4I",
                        "youtube_id": "fDoxZ-Goh4I"
                    }
                }
            ],
            # Page 6: Knowledge Check & Key Takeaway
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Identifying Inductive Steps",
                    "content": {
                        "question": "In our study of Matthew 13:44-46, which statement represents the 'Interpretation' step?",
                        "options": [
                            "A) The man and the merchant both sold all they had to buy what they found.",
                            "B) The Kingdom of God is of infinite, surpassing value, and finding it brings supreme joy worth sacrificing everything for.",
                            "C) I will wake up 15 minutes earlier tomorrow to pray before breakfast.",
                            "D) The Greek word for merchant is 'émporos'."
                        ],
                        "correct_answer": "B",
                        "explanation": "Option B identifies the underlying theological meaning intended by Jesus. Option A is an observation of text details, and Option C is a personal application."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson Summary & Inductive Discipline",
                    "content": {
                        "text": "- **Diligence in Observation:** Never assume you know what a passage means before carefully observing what it actually says.\n- **Contextual Interpretation:** Reconstruct the author's original cultural and historical message first.\n- **Transformative Application:** Real Bible study concludes in obedience, love, and life-changing personal action."
                    }
                }
            ]
        ]
    },

    # --------------------------------------------------------------------------
    # LESSON 5: Utilising the Biography Method (Jonah) & Daily Reading
    # --------------------------------------------------------------------------
    {
        "unit_order": 5,
        "unit_name": "Utilising the Biography Method and Building Daily Habits",
        "unit_description": "Biographical method applied to Prophet Jonah (rebellion, consequence, preaching, lesson of mercy), study tools (Concordance, Dictionary), and Daily Reflection Journaling.",
        "lesson_title": "Utilising the Biography Method (Jonah) & Daily Reading Habits",
        "pages": [
            # Page 1: Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Jonah and the Great Fish",
                    "content": {
                        "title": "Jonah and the Great Fish (Pieter Lastman, 1621)",
                        "caption": "Prophet Jonah emerging from the great fish onto dry land after his prayer of repentance, illustrating divine mercy and second chances.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Pieter_Lastman_004.jpg",
                        "author": "Pieter Lastman / Wikimedia Commons",
                        "licensing": "Public Domain",
                        "verified": True
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Biography Study & Lifelong Habits",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Apply the Biography Method systematically to trace the life, struggles, and lessons of Prophet Jonah\n- Utilize reference tools like a Bible Concordance and Bible Dictionary for topical research\n- Set up a sustainable Daily Reflection Journal using the 5-prompt framework for lifelong spiritual growth"
                    }
                }
            ],
            # Page 2: Jonah's Life Story: 4 Narrative Stages
            [
                {
                    "type": "concept_explanation",
                    "title": "Biographical Case Study: The Life of Prophet Jonah",
                    "content": {
                        "text": "The Book of Jonah is unique because it is not a book of poetic sermons; it is a dramatic **narrative biography** of a reluctant prophet:\n\n### 1. The Call & Rebellion (Jonah 1)\n- **God's Command:** Go to Nineveh (capital of brutal Assyria, Israel's oppressor) and preach judgment against their wickedness.\n- **Jonah's Flight:** Boarded a ship at Joppa bound for Tarshish—in the exact opposite direction! Jonah hated the Assyrians and feared God's mercy might spare them if they repented.\n\n### 2. The Storm, Sea & Great Fish (Jonah 1-2)\n- God sent a violent storm. The pagan sailors cast lots, and the lot fell on Jonah.\n- Jonah confessed he was fleeing from Yahweh and told them to cast him overboard. When they did, the sea calmed. God provided a great fish to swallow Jonah, where he prayed a psalm of thanksgiving and was delivered to dry land.\n\n### 3. The Second Chance & Nineveh's Repentance (Jonah 3)\n- God called Jonah a second time. Jonah went and preached: *'Forty more days and Nineveh will be overthrown.'*\n- Surprisingly, Nineveh repented immediately from the King to the cattle, fasting in sackcloth. God showed mercy and relented from destroying the city.\n\n### 4. Jonah's Anger and the Leafy Vine (Jonah 4)\n- Jonah was furious because his enemies were spared! God grew a leafy plant to give Jonah shade, then sent a worm to wither it. When Jonah mourned the plant, God revealed the ultimate lesson:\n  > *'You have been concerned about this plant, which you did not tend or make grow... Should I not have concern for the great city of Nineveh, in which there are more than 120,000 people...?'*"
                    }
                }
            ],
            # Page 3: Biographical Analysis & Character Matrix
            [
                {
                    "type": "concept_explanation",
                    "title": "Character Analysis: Strengths, Weaknesses, and Divine Revelations",
                    "content": {
                        "text": "### Jonah's Character Breakdown\n- **Strengths:** Honest in crisis (admitted his guilt to sailors); capable of deep prayer and repentance; a potent communicator when obedient.\n- **Weaknesses:** Ethnocentric hatred (refused to desire mercy for enemies); stubborn disobedience; prioritized personal comfort (the vine) over 120,000 human lives.\n\n### Major Life Lessons & Divine Revelations\n- **You Cannot Run From God:** God's sovereign presence encompasses the oceans, the storm, the fish, and all nations.\n- **God's Universal Compassion:** God's grace is not restricted to one nation or tribe; His redemptive love embraces all humanity, challenging our prejudices.\n- **Distinguishing Description vs. Prescription:** Jonah is a mirror showing how bitterness blinds us to God's heart of mercy."
                    }
                }
            ],
            # Page 4: Visual Diagram — Jonah's Journey & Daily Reflection Template
            [
                {
                    "type": "suggested_diagram",
                    "title": "Jonah's Biographical Journey & Daily Reflection Framework",
                    "content": {
                        "title": "Jonah's Biographical Journey & Daily Reflection Framework",
                        "caption": "A comprehensive vector chart detailing the four narrative stages of Jonah and the 5-prompt daily devotional journal template.",
                        "svg_content": SVG_LESSON_5_BIOGRAPHY
                    }
                }
            ],
            # Page 5: Study Tools & Curated Educational Video
            [
                {
                    "type": "concept_explanation",
                    "title": "Essential Tools for Lifelong Scripture Study",
                    "content": {
                        "text": "To sustain daily Bible reading and deep research, learn to use these three indispensable study tools:\n\n1. **Bible Concordance:** An alphabetical index of all words in Scripture. If researching 'Integrity' or 'Mercy,' it directs you to every occurrence across the Old and New Testaments.\n2. **Bible Dictionary / Encyclopaedia:** Provides rich historical, geographical, and cultural background for ancient terms, cities (Nineveh, Joppa, Tarshish), and customs.\n3. **Daily Reflection Journal:** A personal log using the 5 core prompts (*Passage, Standout observation, God/humanity lesson, Concrete application, Prayer/question*)."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Educational Video: The Book of Jonah Animation",
                    "content": {
                        "title": "The Book of Jonah - BibleProject Animated Guide",
                        "description": "An award-winning animated visual breakdown of the Book of Jonah, exploring its subversive literary design, irony, and the boundless mercy of God.",
                        "url": "https://www.youtube.com/watch?v=dLIabZc0O4c",
                        "youtube_id": "dLIabZc0O4c"
                    }
                }
            ],
            # Page 6: Knowledge Check & Reflection Dilemma
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: The Lesson of Jonah 4",
                    "content": {
                        "question": "What was the primary theological lesson God taught Jonah through the withered plant and the worm in Jonah 4?",
                        "options": [
                            "A) Prophets should always carry shelter when preaching in desert climates.",
                            "B) God has sovereign, boundless compassion for all human lives, and His followers must align their hearts with His mercy rather than harbor hatred for enemies.",
                            "C) Plants are more valuable than ancient cities in Old Testament theology.",
                            "D) God wanted to prove to Jonah that worms are destructive agricultural pests."
                        ],
                        "correct_answer": "B",
                        "explanation": "God used the contrast between Jonah's pity for a short-lived plant and his lack of compassion for Nineveh to demonstrate that His mercy and love extend to all nations."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson Summary & Spiritual Growth Pledge",
                    "content": {
                        "text": "- **Biographical Reflection:** Jonah challenges us to eradicate tribalism and bitterness, welcoming God's radical mercy for everyone.\n- **Daily Discipline:** Lifelong spiritual maturity is built on consistent, daily engagement with God's Word using a structured Reflection Journal.\n- **My Commitment:** Commit 10-15 minutes daily to quiet reading, journal the 5 prompts, and let Scripture transform your character every single day."
                    }
                }
            ]
        ]
    }
]

# ==============================================================================
# INGESTION RUNNER
# ==============================================================================

def ingest_grade10_cre_topic1_2(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 1.2: Methods of Studying the Holy Bible (Grade 10 CRE)")
    print("=" * 80)

    # 1. Resolve Curriculum & Grade
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' (ID 5) not found in database.")

    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        raise ValueError("Grade 'Grade 10' not found under CBC curriculum.")

    # 2. Resolve Subject (CRE, Subject ID: 46)
    subject = Subject.objects.filter(id=46).first()
    if not subject:
        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="CRE",
            defaults={"description": "Christian Religious Education Senior Secondary Curriculum"}
        )
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name} (Grade ID: {grade.id})")

    # 3. Resolve Topic (Topic 1.2: Methods of Studying the Holy Bible, Order: 2)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=2,
        defaults={
            "name": "Topic 1.2: Methods of Studying the Holy Bible",
            "description": "Methods of studying Scripture including Devotional, Topical, Character Study, Verse-by-Verse, and Inductive approaches, their benefits, tools, and daily habit formation."
        }
    )
    if not t_created:
        topic.name = "Topic 1.2: Methods of Studying the Holy Bible"
        topic.description = "Methods of studying Scripture including Devotional, Topical, Character Study, Verse-by-Verse, and Inductive approaches, their benefits, tools, and daily habit formation."
        topic.save()
    print(f"[*] Resolved Topic 1.2: {topic.name} (ID: {topic.id})")

    # 4. Clean replace if requested
    if replace:
        print("[*] Replacing existing Topic 1.2 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for item in TOPIC_1_2_LESSONS:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            pages = item["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Senior CRE Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "CRE",
                    "topic_order": 2,
                    "unit_order": u_order
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t1_2_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 2, "unit_order": u_order, "page": page_idx}
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAsset if applicable
                    if b_type == "suggested_diagram" and "svg_content" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": b_content["svg_content"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            url=b_content["url"],
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA 3.0"),
                                "caption": b_content.get("caption", "")
                            }
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_video" and "youtube_id" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("description", b_title),
                            url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                            metadata={"youtube_id": b_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print(f"TOPIC 1.2 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_cre_topic1_2(replace=True)
