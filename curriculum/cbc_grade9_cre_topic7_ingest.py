"""
VLearn CBC Grade 9 CRE — Topic 7: Parable on Prayer — A Friend at Midnight
Complete Ingestion Script for All 6 Lessons

Target Grade: Grade 9 (ID: 18)
Target Subject: CRE (ID: 50)
Target Topic: Parable on Prayer — A Friend at Midnight (Order: 7)

Structure for Every Lesson (6 Cards / Pages, 13 Blocks, 3 Assets):
- Card 1 (Discovery & Objectives): suggested_image (order 10), learning_goal (order 20), concept_explanation (order 30)
- Card 2 (Scriptural Exegesis): concept_explanation (order 40), concept_explanation (order 45)
- Card 3 (Pedagogical Diagram & Deep Dive): suggested_diagram (order 50), concept_explanation (order 60)
- Card 4 (Practical Application & Context): step_process (order 70), concept_explanation (order 75)
- Card 5 (Multimedia & Reflection): suggested_video (order 80), concept_explanation (order 90)
- Card 6 (Mastery Check): summary (order 100), knowledge_check (order 110)
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
    # Strip bracket citations e.g. [68], [68, 235], [2, 14]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(
        r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE)[^\]]*\]',
        '', text, flags=re.IGNORECASE
    )
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


# ─── SVG VECTOR DIAGRAMS (viewBox="0 0 800 450", theme #0f172a) ───────────────

def get_svg_lesson_1():
    """Lesson 1: The Mechanics and Purpose of Parables (Mashal)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="amberCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE ARCHITECTURE OF A BIBLICAL PARABLE (MASHAL)</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">How Jesus Placed Everyday Experiences Beside Eternal Realities to Reveal Kingdom Truths</text>

  <!-- Flow Arrows / Bridge -->
  <path d="M 230 200 L 305 200 M 495 200 L 565 200" stroke="#475569" stroke-width="3" stroke-dasharray="6 4"/>
  <polygon points="308,200 298,194 298,206" fill="#fbbf24"/>
  <polygon points="568,200 558,194 558,206" fill="#a855f7"/>

  <!-- CARD 1: EARTHLY SCENARIO -->
  <g transform="translate(35, 95)">
    <rect width="195" height="235" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="195" height="34" rx="10" fill="url(#blueCard)"/>
    <text x="97" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. EARTHLY REALITY</text>

    <text x="14" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Visible Experience:</text>
    <text x="14" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Bread, seeds, sheep,</text>
    <text x="14" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">farming, neighbors in need.</text>

    <text x="14" y="130" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Accessibility:</text>
    <text x="14" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Familiar to fishermen,</text>
    <text x="14" y="163" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">farmers, and townspeople.</text>

    <text x="14" y="195" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Hook:</text>
    <text x="14" y="213" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5">Engages the imagination.</text>
  </g>

  <!-- CARD 2: THE BRIDGE OF COMPARISON -->
  <g transform="translate(305, 95)">
    <rect width="190" height="235" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect width="190" height="34" rx="10" fill="url(#amberCard)"/>
    <text x="95" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">2. THE MASHAL BRIDGE</text>

    <rect x="20" y="46" width="150" height="22" rx="6" fill="#d97706" fill-opacity="0.3"/>
    <text x="95" y="61" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Comparison &amp; Contrast</text>

    <text x="12" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Greek: Parabole</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">To place side by side.</text>

    <text x="12" y="132" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Hebrew: Mashal</text>
    <text x="12" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Proverb, riddle, lesson.</text>

    <text x="12" y="172" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Dual Function:</text>
    <text x="12" y="188" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5">Reveals to humble seekers,</text>
    <text x="12" y="202" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5">conceals from the proud.</text>
  </g>

  <!-- CARD 3: HEAVENLY TRUTH -->
  <g transform="translate(565, 95)">
    <rect width="200" height="235" rx="10" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <rect width="200" height="34" rx="10" fill="url(#purpleCard)"/>
    <text x="100" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. HEAVENLY TRUTH</text>

    <text x="14" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Kingdom Principle:</text>
    <text x="14" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">God's love, sovereign grace,</text>
    <text x="14" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">readiness to answer prayer.</text>

    <text x="14" y="130" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Moral Demands:</text>
    <text x="14" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Persistent faith, humility,</text>
    <text x="14" y="163" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">unconditional obedience.</text>

    <text x="14" y="195" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Transformation:</text>
    <text x="14" y="213" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10.5">Life-changing discipleship.</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="35" y="350" width="730" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="371" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MATTHEW 13:11 • "THE KNOWLEDGE OF THE SECRETS OF THE KINGDOM OF HEAVEN HAS BEEN GIVEN TO YOU"</text>
  <text x="400" y="389" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Parables use tangible earthly illustrations as mirrors to convict hearts and windows to reveal God's eternal character.</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 7: PARABLE ON PRAYER • LESSON 1 CONCEPT MAP</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 2: The Narrative and Cultural Setting of the Friend at Midnight"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="travelerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="hostGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="neighborGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE TRIAD OF CHARACTERS &amp; CULTURAL DYNAMICS (LUKE 11:5-8)</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Ancient Hospitality Laws, Midnight Emergencies, and Shameless Audacity (Anaideia)</text>

  <!-- Flow Arrows -->
  <path d="M 235 200 L 290 200 M 500 200 L 555 200" stroke="#475569" stroke-width="3" stroke-dasharray="6 4"/>
  <polygon points="293,200 283,194 283,206" fill="#f59e0b"/>
  <polygon points="558,200 548,194 548,206" fill="#a855f7"/>

  <!-- ACTOR 1: THE TRAVELER -->
  <g transform="translate(30, 95)">
    <rect width="205" height="235" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="205" height="34" rx="10" fill="url(#travelerGrad)"/>
    <text x="102" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">1. THE TRAVELER</text>

    <text x="12" y="62" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Nighttime Journey:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Traveled by night to avoid</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">blistering desert sun.</text>

    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Condition:</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Exhausted, hungry, and</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">wholly dependent on host.</text>

    <text x="12" y="178" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Symbolism:</text>
    <text x="12" y="194" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5">Human vulnerability and</text>
    <text x="12" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5">intercession on behalf of others.</text>
  </g>

  <!-- ACTOR 2: THE HOST (PETITIONER) -->
  <g transform="translate(290, 95)">
    <rect width="210" height="235" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="210" height="34" rx="10" fill="url(#hostGrad)"/>
    <text x="105" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">2. THE HOST (PETITIONER)</text>

    <text x="12" y="62" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Moral Obligation:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Hospitality is sacred duty;</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">refusal brings village shame.</text>

    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Shameless Audacity:</text>
    <text x="12" y="136" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5">Greek: *Anaideia* (boldness,</text>
    <text x="12" y="150" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5">importunity, refusal to yield).</text>

    <text x="12" y="178" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Purpose:</text>
    <text x="12" y="194" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Knocks boldly to obtain</text>
    <text x="12" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">3 loaves of bread for another.</text>
  </g>

  <!-- ACTOR 3: THE SLEEPING NEIGHBOR -->
  <g transform="translate(555, 95)">
    <rect width="215" height="235" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="215" height="34" rx="10" fill="url(#neighborGrad)"/>
    <text x="107" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">3. THE SLEEPING NEIGHBOR</text>

    <text x="12" y="62" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Ancient Home Setting:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Single-room house, bolted door,</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">sleeping children and livestock.</text>

    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Reluctance Overcome:</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Not yielding due to friendship,</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">but relentless persistence.</text>

    <text x="12" y="178" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Contrast with God:</text>
    <text x="12" y="194" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10.5">If a reluctant man gives bread,</text>
    <text x="12" y="208" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10.5">how much more will God respond?</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="30" y="350" width="740" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="371" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">LUKE 11:8 • "YET BECAUSE OF THE MAN'S BOLDNESS (ANAIDEIA) HE WILL RISE AND GIVE HIM AS MUCH AS HE NEEDS"</text>
  <text x="400" y="389" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Christian intercession requires shameless boldness, standing in the gap for the vulnerable without fear of rejection.</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 7: PARABLE ON PRAYER • LESSON 2 CONCEPT MAP</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 3: The Staircase of Active Faith — Ask, Seek, Knock (A.S.K.)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="step1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="step2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="step3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE ASCENDING STAIRCASE OF ACTIVE FAITH (A.S.K.)</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Luke 11:9-10 • The Progressive Intensity of Continuous Present Imperative Prayer</text>

  <!-- STEP 1: ASK (Bottom Step) -->
  <g transform="translate(40, 220)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="220" height="28" rx="8" fill="url(#step1Grad)"/>
    <text x="110" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">1. ASK (Aiteite)</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Vocalizing Humility</text>
    <text x="12" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Expressing dependence; asking</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God directly with childlike trust.</text>
    <text x="12" y="96" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Promise: "It will be given"</text>
  </g>

  <!-- STEP 2: SEEK (Middle Step) -->
  <g transform="translate(290, 160)">
    <rect width="220" height="170" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="220" height="28" rx="8" fill="url(#step2Grad)"/>
    <text x="110" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">2. SEEK (Zeteite)</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Active Investigation</text>
    <text x="12" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Engaging mind and feet;</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">searching Scripture and God's will.</text>
    <text x="12" y="102" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Heart Alignment</text>
    <text x="12" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Purifying motives &amp; choices.</text>
    <text x="12" y="148" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Promise: "You will find"</text>
  </g>

  <!-- STEP 3: KNOCK (Top Step) -->
  <g transform="translate(540, 100)">
    <rect width="220" height="230" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect width="220" height="28" rx="8" fill="url(#step3Grad)"/>
    <text x="110" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">3. KNOCK (Krouete)</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Resilient Perseverance</text>
    <text x="12" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Physical &amp; spiritual endurance;</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">refusing to yield to closed doors.</text>
    <text x="12" y="102" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Overcoming Obstacles</text>
    <text x="12" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Standing firm in delays.</text>
    <text x="12" y="142" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Continuous Action</text>
    <text x="12" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Present imperative: keep knocking!</text>
    <text x="12" y="198" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800">Promise: "Door will be opened"</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="40" y="355" width="720" height="48" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="375" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">GREEK PRESENT IMPERATIVE • "KEEP ON ASKING, KEEP ON SEEKING, KEEP ON KNOCKING"</text>
  <text x="400" y="393" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Jesus commands a progressive, uninterrupted posture of faith that transitions from words to active search and relentless perseverance.</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 7: PARABLE ON PRAYER • LESSON 3 CONCEPT MAP</text>
</svg>"""


def get_svg_lesson_4():
    """Lesson 4: The Contrast of Earthly vs Heavenly Gifts & The Holy Spirit"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="earthGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="heavenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="spiritGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE DIVINE CONTRAST OF GIFTS &amp; THE SUPREME PROMISE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Luke 11:11-13 • Imperfect Human Fathers vs. The Infinite Love of the Heavenly Father</text>

  <!-- Flow Comparison Connector -->
  <path d="M 360 200 L 440 200" stroke="#475569" stroke-width="3" stroke-dasharray="6 4"/>
  <polygon points="443,200 433,194 433,206" fill="#fbbf24"/>

  <!-- LEFT: EARTHLY PARENTAL CARE -->
  <g transform="translate(40, 95)">
    <rect width="320" height="235" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="320" height="34" rx="10" fill="url(#earthGrad)"/>
    <text x="160" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">EARTHLY PARENTS (THE LESSER)</text>

    <!-- Contrast Item 1 -->
    <rect x="15" y="48" width="290" height="52" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="25" y="68" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Fish vs. Serpent:</text>
    <text x="25" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Would never substitute nourishing fish with a venomous water snake.</text>

    <!-- Contrast Item 2 -->
    <rect x="15" y="108" width="290" height="52" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="25" y="128" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Egg vs. Scorpion:</text>
    <text x="25" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Would never hand a curled pale scorpion looking like a bird egg.</text>

    <!-- Insight -->
    <text x="15" y="185" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Human Nature:</text>
    <text x="15" y="201" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Though imperfect and flawed, parents instinctively love and provide.</text>
    <text x="15" y="218" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">They protect children from harm and nourish their bodies.</text>
  </g>

  <!-- RIGHT: HEAVENLY FATHER'S SUPREME GIFT -->
  <g transform="translate(440, 95)">
    <rect width="320" height="235" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect width="320" height="34" rx="10" fill="url(#heavenGrad)"/>
    <text x="160" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">HEAVENLY FATHER (HOW MUCH MORE)</text>

    <!-- Holy Spirit Box -->
    <rect x="15" y="48" width="290" height="70" rx="8" fill="url(#spiritGrad)" stroke="#c084fc"/>
    <text x="160" y="72" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE SUPREME GIFT: THE HOLY SPIRIT</text>
    <text x="160" y="90" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Divine Counselor • Comforter • Spirit of Truth • Guide</text>
    <text x="160" y="106" fill="#fef08a" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">More valuable than gold, fame, or earthly comfort.</text>

    <text x="15" y="142" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Infinite Goodness:</text>
    <text x="15" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">God's heart is purely benevolent; He never tricks or deceives.</text>

    <text x="15" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Divine Security:</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">We approach prayer with absolute boldness, knowing God grants</text>
    <text x="15" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">what is eternally beneficial for our souls.</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="40" y="350" width="720" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="371" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">LUKE 11:13 • "HOW MUCH MORE WILL YOUR FATHER IN HEAVEN GIVE THE HOLY SPIRIT TO THOSE WHO ASK HIM!"</text>
  <text x="400" y="389" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">God does not merely give material crumbs; He imparts His own Holy Spirit to empower and counsel those who seek Him.</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 7: PARABLE ON PRAYER • LESSON 4 CONCEPT MAP</text>
</svg>"""


def get_svg_lesson_5():
    """Lesson 5: Persistent Prayer in Christian Life (The Consistency Loop & Philippians 4)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d9488"/>
      <stop offset="100%" stop-color="#0f766e"/>
    </linearGradient>
    <linearGradient id="blueGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="amberGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE CONTINUOUS CYCLE OF CHRISTIAN PRAYER &amp; PEACE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">1 Thessalonians 5:17 &amp; Philippians 4:6-7 • Transforming Anxiety into Unshakable Divine Peace</text>

  <!-- 4 Stage Horizontal Cycle Cards -->
  <!-- CARD 1: PRAY CONTINUALLY -->
  <g transform="translate(30, 95)">
    <rect width="165" height="235" rx="8" fill="#1e293b" stroke="#2dd4bf" stroke-width="1.5"/>
    <rect width="165" height="32" rx="8" fill="url(#tealGrad)"/>
    <text x="82" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. UNCEASING PRAYER</text>
    <text x="12" y="56" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1 Thess 5:17</text>
    <text x="12" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Pray without ceasing."</text>
    <text x="12" y="98" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Posture:</text>
    <text x="12" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Constant spiritual</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">awareness and unbroken</text>
    <text x="12" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">fellowship with God.</text>
    <text x="12" y="174" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Fixed morning/night</text>
    <text x="12" y="190" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Breath prayers all day</text>
  </g>

  <!-- CARD 2: SURRENDER ANXIETY -->
  <g transform="translate(220, 95)">
    <rect width="165" height="235" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="165" height="32" rx="8" fill="url(#blueGrad5)"/>
    <text x="82" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. CAST ANXIETY</text>
    <text x="12" y="56" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Phil 4:6</text>
    <text x="12" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Do not be anxious</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">about anything..."</text>
    <text x="12" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Method:</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">In every situation,</text>
    <text x="12" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">by prayer, petition,</text>
    <text x="12" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">with thanksgiving,</text>
    <text x="12" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">make requests known.</text>
  </g>

  <!-- CARD 3: PERSIST IN FAITH -->
  <g transform="translate(410, 95)">
    <rect width="165" height="235" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="165" height="32" rx="8" fill="url(#amberGrad5)"/>
    <text x="82" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. PERSIST IN FAITH</text>
    <text x="12" y="56" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Luke 18:1</text>
    <text x="12" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Always pray and</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">not give up."</text>
    <text x="12" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Benefits:</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Tests sincerity</text>
    <text x="12" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Builds patience</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Refines character</text>
    <text x="12" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Prepares gratitude</text>
  </g>

  <!-- CARD 4: SUPERNATURAL PEACE -->
  <g transform="translate(600, 95)">
    <rect width="170" height="235" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
    <rect width="170" height="32" rx="8" fill="url(#purpleGrad5)"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">4. PEACE OF GOD</text>
    <text x="12" y="56" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Phil 4:7</text>
    <text x="12" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"The peace of God,</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">transcending all</text>
    <text x="12" y="102" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">understanding..."</text>
    <text x="12" y="126" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Divine Guard:</text>
    <text x="12" y="144" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10">Guards hearts and</text>
    <text x="12" y="158" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10">minds in Christ Jesus</text>
    <text x="12" y="172" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10">through all life trials.</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="30" y="350" width="740" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="371" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHILIPPIANS 4:6-7 • "PRESENT YOUR REQUESTS TO GOD AND THE PEACE OF GOD WILL GUARD YOUR HEARTS"</text>
  <text x="400" y="389" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Persistent prayer transforms human anxiety into spiritual resilience, guarding the mind with peace that surpasses comprehension.</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 7: PARABLE ON PRAYER • LESSON 5 CONCEPT MAP</text>
</svg>"""


def get_svg_lesson_6():
    """Lesson 6: The Threefold Sovereign Responses of God (Yes, No, Wait) & Romans 8:28"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="yesGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="noGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="waitGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="romGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE THREEFOLD SOVEREIGN RESPONSES OF GOD</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Romans 8:26-28 &amp; James 1:5-6 • Trusting Divine Wisdom in Answers, Redirections, and Delays</text>

  <!-- 3 Response Cards -->
  <!-- CARD 1: YES -->
  <g transform="translate(35, 95)">
    <rect width="220" height="235" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="220" height="34" rx="10" fill="url(#yesGrad)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1. YES (PROVISION)</text>

    <text x="12" y="62" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Divine Alignment:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Request aligns perfectly with</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">God's will, purpose, and timing.</text>

    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Manifestation:</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Gracious granting of wisdom,</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">healing, help, and resources.</text>

    <text x="12" y="178" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Proper Response:</text>
    <text x="12" y="194" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Immediate praise, joyful</text>
    <text x="12" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">thanksgiving, and service.</text>
  </g>

  <!-- CARD 2: NO -->
  <g transform="translate(290, 95)">
    <rect width="220" height="235" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
    <rect width="220" height="34" rx="10" fill="url(#noGrad)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">2. NO (PROTECTION)</text>

    <text x="12" y="62" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Shield of Grace:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Request is harmful, selfish,</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">or counter to eternal good.</text>

    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Christ's Example:</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Gethsemane: "Yet not my</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">will, but Yours be done."</text>

    <text x="12" y="178" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Proper Response:</text>
    <text x="12" y="194" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Humble surrender, trusting</text>
    <text x="12" y="208" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">God's superior foresight.</text>
  </g>

  <!-- CARD 3: WAIT -->
  <g transform="translate(545, 95)">
    <rect width="220" height="235" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect width="220" height="34" rx="10" fill="url(#waitGrad)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">3. WAIT (PREPARATION)</text>

    <text x="12" y="62" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Right Request, Next Season:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">The desire is wholesome, but</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">timing requires maturation.</text>

    <text x="12" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Sanctification Work:</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Builds endurance, strengthens</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">faith, purifies motives.</text>

    <text x="12" y="178" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Proper Response:</text>
    <text x="12" y="194" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Steadfast patience, active</text>
    <text x="12" y="208" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">service, unyielding hope.</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="35" y="350" width="730" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="371" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ROMANS 8:28 • "IN ALL THINGS GOD WORKS FOR THE GOOD OF THOSE WHO LOVE HIM"</text>
  <text x="400" y="389" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Whether God grants immediate provision, protective redirection, or patient preparation, His sovereign purpose is eternal blessing.</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 7: PARABLE ON PRAYER • LESSON 6 CONCEPT MAP</text>
</svg>"""


# ─── 6 LESSONS DATA DEFINITIONS ───────────────────────────────────────────────

TOPIC_7_LESSONS = [
    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 1
    # ─────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Understanding the Nature of Parables",
        "unit_description": "Examine the definition of parables, the Hebrew origin Mashal, and the theological reasons why Jesus used everyday stories to teach eternal spiritual truths.",
        "lesson_title": "Understanding the Nature of Parables",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/James_Tissot_-_Jesus_Teaching_in_the_Synagogues_-_Brooklyn_Museum.jpg/800px-James_Tissot_-_Jesus_Teaching_in_the_Synagogues_-_Brooklyn_Museum.jpg",
            "title": "Visual Hook: Jesus Teaching in Parables",
            "author": "James Tissot (Brooklyn Museum)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus teaching crowds through relatable earthly illustrations, engaging the imagination to communicate profound spiritual truths."
        },
        "youtube": {
            "youtube_id": "XX-K-ALeeU4",
            "title": "BibleProject: The Parables of Jesus",
            "description": "Explores how Jesus used parables to announce God's Kingdom, challenging listeners' worldviews and inviting humble seekers into discipleship."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Define the term 'parable' and identify its Hebrew counterpart 'Mashal'.",
            "Analyze Matthew 13:10-17 and Mark 4:33-34 to explain why Jesus chose parables as His primary teaching methodology.",
            "Formulate modern relatable scenarios that convey moral and spiritual values in home and school environments."
        ],
        "intro": "Imagine you are trying to explain how the internet or wireless cellular network functions to a great-grandparent who has never seen an electronic screen. You might explain, 'It is like an invisible highway in the sky carrying letters, photographs, and songs instantly to every home.' You take something visible and concrete—a highway—to explain something invisible and abstract—digital radio frequencies.\n\nJesus Christ utilized this exact pedagogical approach throughout His earthly ministry. When teaching diverse crowds comprising simple Galilee fishermen, humble farmers, and sophisticated religious scholars, He did not deliver dry, theoretical lectures. Instead, He utilized common everyday elements—seeds, bread, lamps, sheep, and persistent neighbors—to reveal the invisible reality of the Kingdom of God.",
        "core_scripture": "### Biblical Foundations of Parables\n\n#### Matthew 13:10-13, 16-17 — The Purpose of Parables\n> *\"The disciples came to him and asked, 'Why do you speak to the people in parables?' He replied, 'Because the knowledge of the secrets of the kingdom of heaven has been given to you, but not to them. Whoever has will be given more, and they will have an abundance. Whoever does not have, even what they have will be taken from them. This is why I speak to them in parables: Though seeing, they do not see; though hearing, they do not hear or understand... But blessed are your eyes because they see, and your ears because they hear.'\"*\n\n#### Luke 11:1-4 — The Model for Kingdom Prayer\n> *\"One day Jesus was praying in a certain place. When he finished, one of his disciples said to him, 'Lord, teach us to pray, just as John taught his disciples.' He said to them, 'When you pray, say: Father, hallowed be your name, your kingdom come. Give us each day our daily bread. Forgive us our sins, for we also forgive everyone who sins against us. And lead us not into temptation.'\"*",
        "theological_pillars": "### Theological & Linguistic Dimensions of Parables\n\n1. **The Hebrew Concept of Mashal:** In the Old Testament tradition, a parable corresponds to the Hebrew word *Mashal*, meaning a proverb, comparison, riddle, or figurative discourse. A *Mashal* places two distinct concepts side by side to stimulate critical discernment and self-reflection.\n2. **The Greek Term Parabole:** Derived from *para* (alongside) and *ballein* (to throw or cast), *Parabole* literally means 'casting alongside'—throwing an earthly scenario beside a divine truth to illuminate its spiritual meaning.\n3. **The Dual Function of Parables:** Parables served both as a mirror and a filter. For humble, sincere seekers, parables illuminated divine wisdom and called for heartfelt transformation. For cynical, self-righteous critics, parables concealed deeper mysteries, preventing superficial exploitation while convicting rebellious hearts.",
        "deep_dive": "### Deep Dive: Four Theological Reasons Jesus Taught in Parables\n\n- **1. Simplifying Profound Kingdom Realities:** Spiritual concepts such as divine grace, repentance, and persistent intercession can seem abstract. By grounding them in agricultural and household settings, Jesus made high theology accessible to everyday people.\n- **2. Engaging Active Critical Thinking:** Rather than passive listening, parables require listeners to solve a moral puzzle. Listeners must evaluate the characters' decisions, identify with their struggles, and examine their own moral lives.\n- **3. Protecting Sacred Truth from Cynics:** In fulfillment of Isaiah 6:9-10 (cited in Matthew 13:14-15), parables separated curious truth-seekers who stayed to ask questions from hardened critics who dismissed the stories on the surface.\n- **4. Enhancing Long-Term Memory & Oral Transmission:** Earthly narratives about midnight knockers, lost coins, and prodigal sons are memorable, easily retold across generations, and resilient in oral traditions.",
        "practical": {
            "title": "Action Framework: Analyzing and Applying Biblical Parables",
            "steps": [
                "Step 1: Identify the Earthly Scenario — Observe the cultural characters, household objects, and societal tensions depicted in the story.",
                "Step 2: Bridge the Mashal Comparison — Determine what heavenly or spiritual reality Jesus is placing alongside the earthly narrative.",
                "Step 3: Uncover the Theological Challenge — Pinpoint the central moral turning point that convicts human pride or invites faith.",
                "Step 4: Execute Life Transformation — Translate the Kingdom principle into tangible daily practices, academic integrity, and prayer habits."
            ]
        },
        "kenyan_context": "In traditional Kenyan societies and contemporary communities, storytelling (oral literature) serves as a cornerstone of moral education. Grandparents and community elders gather children around the evening hearth to share stories of clever animals, loyal friends, and foolish decisions. Just as African folklore imparts enduring virtues of honesty, hard work, and communal solidarity, Jesus utilized Palestinian cultural stories to instill eternal Kingdom values in His followers.",
        "reflection": "### Spiritual & Ethical Reflection\n\n- If Jesus were walking through your Kenyan school or neighborhood today, what modern comparisons (e.g., mobile phones, sports tournaments, exam revision, matatu transport) might He use to teach about the Kingdom of God?\n- When you listen to sermons, school guidance talks, or parents' advice, do you search for deeper wisdom or do you merely focus on the surface words?",
        "takeaways": [
            "A parable is an earthly story with a heavenly meaning, derived from the Hebrew 'Mashal' (comparison/riddle) and Greek 'Parabole' (casting alongside).",
            "Jesus utilized parables to simplify deep spiritual concepts, provoke critical self-examination, and make Kingdom principles unforgettable.",
            "Parables reveal divine secrets to humble, earnest seekers while concealing truth from hardened, arrogant skeptics (Matthew 13:11-13).",
            "Biblical parables bridge relatable daily experiences with profound spiritual obligations regarding prayer, faith, and ethical living."
        ],
        "mcq": {
            "question": "What is the Hebrew term for 'parable', which refers to a proverb, comparison, or riddle placed beside spiritual truth?",
            "options": [
                "A) Vocare",
                "B) Mashal",
                "C) Eschatus",
                "D) Torah"
            ],
            "answer": "B",
            "explanation": "Mashal is the Hebrew term signifying a proverb, comparison, or riddle (Matthew 13:10-15). Vocare means 'to call' (vocation), Eschatus refers to the end times, and Torah denotes the Law of Moses."
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 2
    # ─────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "The Story of a Friend at Midnight",
        "unit_description": "Analyze the dramatic narrative in Luke 11:5-8, exploring ancient Near Eastern hospitality customs, single-room dwellings, and the power of bold persistence (Anaideia).",
        "lesson_title": "The Story of a Friend at Midnight",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Millais_The_Friend_at_Midnight.jpg/800px-Millais_The_Friend_at_Midnight.jpg",
            "title": "Visual Hook: The Friend at Midnight",
            "author": "John Everett Millais (1864)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "An earnest homeowner knocking urgently on his neighbor's locked wooden door at midnight to request bread for an unexpected traveler."
        },
        "youtube": {
            "youtube_id": "VMBEj_8Xq_I",
            "title": "BibleProject: Gospel of Luke & The Journey to Jerusalem",
            "description": "Explores Jesus' revolutionary teachings on hospitality, prayer, and persistent intercession as recorded in the Gospel of Luke."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Retell the sequence of events in the Parable of the Friend at Midnight (Luke 11:5-8).",
            "Examine ancient Near Eastern hospitality customs and the cultural significance of the single-room dwelling.",
            "Analyze the theological concept of 'Anaideia' (shameless audacity/persistence) in Christian intercession."
        ],
        "intro": "Have you ever experienced an unexpected guest arriving at your family home late at night when your pantry was completely empty? You immediately feel a surge of anxiety and urgency. In modern towns, one might dash to a 24-hour convenience store or place a quick delivery order. \n\nHowever, in an ancient Palestinian village without electricity, grocery stores, or streetlights, you faced an acute social emergency. Turning an exhausted traveler away without food brought severe community disgrace. In such a predicament, you would have to take a humiliating, desperate step: walk through the dark village and knock loudly on a sleeping neighbor's locked door at midnight.",
        "core_scripture": "### Biblical Passage: The Friend at Midnight\n\n#### Luke 11:5-8 — The Narrative of Midnight Importunity\n> *\"Then Jesus said to them, 'Suppose you have a friend, and you go to him at midnight and say, \"Friend, lend me three loaves of bread; a friend of mine on a journey has come to me, and I have no food to offer him.\"'*\n>\n> *'And suppose the one inside answers, \"Don't bother me. The door is already locked, and my children and I are in bed. I can't get up and give you anything.\"'*\n>\n> *'I tell you, even though he will not get up and give him the bread because of friendship, yet because of the man’s boldness he will surely get up and give him as much as he needs.'\"*",
        "theological_pillars": "### Cultural and Theological Exegesis of Luke 11:5-8\n\n1. **The Sacred Duty of Village Hospitality:** In ancient Mediterranean and Semitic cultures, hospitality was not merely a polite courtesy—it was a sacred, communal moral obligation. A traveler arriving after dark had to be fed and lodged with honor. Failing to provide a meal brought shame not only upon the host, but upon the entire village.\n2. **The Architecture of the Ancient Home:** Peasant families lived in single-room stone homes. At night, the family slept together on an elevated wooden mat or platform, while domestic livestock (chickens, sheep, goats) were housed on the lower dirt floor by the entrance. Unbolting a heavy wooden beam would awaken crying infants and agitate the animals.\n3. **The Greek Concept of Anaideia:** In verse 8, Jesus attributes the neighbor's compliance to the host's *Anaideia*, translated as 'boldness', 'shamelessness', or 'audacity'. The petitioner cast aside social hesitation and embarrassment because the urgency of his friend's need outweighed personal pride.",
        "deep_dive": "### Deep Dive: The Triad of Characters and Spiritual Intercession\n\n- **1. The Weary Traveler:** Represents human helplessness, physical limitation, and the unexpected crises of life. Traveling occurred at dusk or night to avoid scorching daytime heat.\n- **2. The Interceding Host:** Represents the believer who acknowledges their personal bankruptcy ('I have nothing to set before him') and approaches God boldly on behalf of others in crisis.\n- **3. The Reluctant Sleeping Neighbor:** Serves as a rhetorical contrast. If an imperfect, grumbling human neighbor will eventually get out of warm bed to provide bread solely due to shameless knocking, *how much more* will our loving, never-sleeping Heavenly Father answer the bold prayers of His children!\n- **4. The Nature of Intercessory Prayer:** The host was not begging bread for personal luxury or selfish indulgence; he was interceding tirelessly to meet the urgent necessity of another person.",
        "practical": {
            "title": "Action Framework: Practicing Bold Community Intercession",
            "steps": [
                "Step 1: Recognize Human Inadequacy — Acknowledge honestly when personal resources or wisdom are insufficient to solve a crisis.",
                "Step 2: Step into the Gap for Others — Identify vulnerable classmates, neighbors, or relatives who urgently require support and prayer.",
                "Step 3: Pray with Shameless Boldness (Anaideia) — Approach God persistently without timidity, doubt, or fear of being burdensome.",
                "Step 4: Combine Prayer with Tangible Hospitality — Accompany spiritual intercession with practical acts of food sharing, hospitality, and encouragement."
            ]
        },
        "kenyan_context": "In Kenyan culture, the values of *Utu* (humanity), *Ubuntu* ('I am because we are'), and *Harambee* (mutual pulling together) resonate powerfully with this parable. When an unexpected guest arrives in a rural or urban Kenyan household, family members immediately prepare hot tea and food, even if it means borrowing sugar or maize flour from a next-door neighbor. This communal solidarity reflects the selfless hospitality commanded in Scripture.",
        "reflection": "### Spiritual & Ethical Reflection\n\n- Have you ever hesitated to ask God for help because you felt your request was 'too small' or that you might be 'bothering' Him?\n- How does the host's willingness to endure midnight embarrassment for a friend challenge you to advocate boldly for peers facing injustice or poverty?",
        "takeaways": [
            "The Parable of the Friend at Midnight (Luke 11:5-8) highlights sacred hospitality, relational persistence, and intercessory prayer.",
            "Ancient Near Eastern single-room houses made nighttime disturbances costly, yet the host's shameless persistence (*Anaideia*) overcame the barrier.",
            "Intercessory prayer begins when we recognize our lack of resources and boldly ask God to provide for those in need.",
            "If an imperfect, reluctant neighbor answers midnight knocking, our benevolent Heavenly Father will certainly respond to faithful petitions."
        ],
        "mcq": {
            "question": "What Greek term is used in Luke 11:8 to describe the host's shameless boldness and relentless persistence in knocking for bread?",
            "options": [
                "A) Agape",
                "B) Koinonia",
                "C) Anaideia",
                "D) Diakonia"
            ],
            "answer": "C",
            "explanation": "Anaideia is the Greek word meaning shamelessness, audacity, or bold persistence. Agape means unconditional love, Koinonia means fellowship, and Diakonia means service."
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 3
    # ─────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Ask, Seek, and Knock",
        "unit_description": "Analyze Jesus' threefold progressive command in Luke 11:9-10 (Ask, Seek, Knock), understanding the Greek present imperative of continuous active faith.",
        "lesson_title": "Ask, Seek, and Knock",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/William_Holman_Hunt_-_The_Light_of_the_World_-_Google_Art_Project.jpg/800px-William_Holman_Hunt_-_The_Light_of_the_World_-_Google_Art_Project.jpg",
            "title": "Visual Hook: Knocking at the Door",
            "author": "William Holman Hunt (Keble College, Oxford)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A classic depiction of knocking persistently at the door, symbolizing the spiritual urgency of active, unbroken communion with God."
        },
        "youtube": {
            "youtube_id": "8b5r3X7kQ8c",
            "title": "BibleProject: Prayer & The Character of God",
            "description": "Explores Jesus' teaching on active, persistent prayer and the character of God who welcomes our honest petitions."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "Analyze the progression of the acronym A.S.K. (Ask, Seek, Knock) in Luke 11:9-10.",
            "Explain the theological significance of the Greek present imperative tense ('keep on asking, seeking, knocking').",
            "Apply the discipline of continuous spiritual diligence to academic studies, personal character growth, and prayer routines."
        ],
        "intro": "Consider what happens when you learn a demanding skill, such as playing a musical instrument, mastering competitive football, or understanding advanced mathematics formulas. You do not simply make one casual request and instantly become an expert. You must ask questions, actively search for instructional guides, practice tirelessly, and repeatedly knock on the doors of teachers and coaches until the skill is mastered.\n\nSpiritual discipleship and prayer operate on the same dynamic principle. Immediately following the parable of the midnight petitioner, Jesus issued a famous threefold command that moves the believer from verbal requesting to active pursuit and persistent endurance.",
        "core_scripture": "### Biblical Passage: The Command to A.S.K.\n\n#### Luke 11:9-10 — The Tripartite Promise of Answered Prayer\n> *\"So I say to you: Ask and it will be given to you; seek and you will find; knock and the door will be opened to you.\n>\n> For everyone who asks receives; the one who seeks finds; and to the one who knocks, the door will be opened.\"*\n\n#### Matthew 7:7-8 — Parallel Teaching on the Mount\n> *\"Ask and it will be given to you; seek and you will find; knock and the door will be opened to you. For everyone who asks receives; the one who seeks finds; and to the one who knocks, the door will be opened.\"*",
        "theological_pillars": "### Exegetical Analysis of Luke 11:9-10\n\n1. **The Ascending Progression of Action (A.S.K.):**\n   - **ASK (Aiteite):** The vocalization of conscious need. It expresses humility and childlike reliance, admitting that we do not control everything.\n   - **SEEK (Zeteite):** Involves the mind, eyes, and feet. It moves beyond words into active exploration, searching the Scriptures, seeking godly counsel, and aligning our desires with God's will.\n   - **KNOCK (Krouete):** The most intense physical and spiritual effort. It represents encountering closed doors, overcoming spiritual and emotional friction, and persevering through delays.\n2. **The Greek Present Imperative Tense:** In the original Koine Greek manuscripts, the verbs *aiteite*, *zeteite*, and *krouete* are constructed in the present continuous imperative mood. A precise translation is: *'Keep on asking and it shall be given; keep on seeking and you shall find; keep on knocking and the door shall be opened.'* Prayer is not a one-time transaction, but a continuous lifestyle of communion.",
        "deep_dive": "### Deep Dive: Why God Demands Continuous Persistence\n\n- **1. Prayer is Relational, Not Mechanical:** God is not an automated vending machine where we insert a quick prayer token and demand an instant product. God desires a deepening, interactive relationship of trust and love.\n- **2. Persistence Purifies Human Motives:** When we are required to keep asking and seeking over time, our superficial and selfish wishes fall away, leaving behind sincere desires that align with God's Kingdom.\n- **3. Developing Spiritual Stamina & Resilience:** Spiritual maturity is forged in the waiting room of faith. Continuous knocking builds patient endurance and moral character (James 1:3-4).\n- **4. Universal Scope of the Promise:** Jesus emphasizes that *'everyone who asks receives'*. God's invitation is not reserved for an elite few, but is open to every humble seeker who approaches with sincere faith.",
        "practical": {
            "title": "Action Framework: The A.S.K. Method in Daily Student Life",
            "steps": [
                "Step 1: ASK with Humility — Articulate your daily academic, emotional, and spiritual challenges to God in clear, simple language.",
                "Step 2: SEEK with Diligence — Pair your prayers with active investigation: study your textbooks, read Scripture, and consult mentors.",
                "Step 3: KNOCK with Resilience — When facing difficult exams, rejected applications, or personal struggles, refuse to give up; persevere in prayer.",
                "Step 4: RECEIVE with Thanksgiving — Celebrate God's answers, record them in a journal, and use your blessings to uplift your school and family."
            ]
        },
        "kenyan_context": "In Kenyan secondary schools and CBC junior secondary education, students understand that passing competitive national examinations requires the A.S.K. principle in practice. A dedicated student does not merely 'ask' a teacher once; they 'seek' revision past papers in the library and 'knock' on the staffroom door for remedial assistance until difficult topics are mastered. Academic excellence mirrors this spiritual law of diligence.",
        "reflection": "### Spiritual & Ethical Reflection\n\n- When you pray for a specific need and do not receive an immediate answer within 24 hours, do you stop praying or do you press into deeper seeking?\n- How does understanding that the Greek text means 'keep on knocking' change your approach to praying for long-term family peace or academic success?",
        "takeaways": [
            "Jesus provides a threefold progressive command: Ask (humble petition), Seek (active search), and Knock (resilient perseverance).",
            "In Greek, the verbs are in the present continuous imperative tense, commanding believers to 'keep on asking, keep on seeking, keep on knocking'.",
            "Persistence in prayer is not about convincing a reluctant God, but about cultivating faith, purifying motives, and building spiritual character.",
            "God promises that continuous, active faith will never be ignored: everyone who asks receives, the seeker finds, and the door opens."
        ],
        "mcq": {
            "question": "What does the Greek present continuous imperative tense in Luke 11:9 indicate about how believers should approach prayer?",
            "options": [
                "A) Pray only once and never repeat the request",
                "B) Maintain continuous, uninterrupted persistence in asking, seeking, and knocking",
                "C) Pray exclusively during formal weekend worship services",
                "D) Recite long theological words without understanding their meaning"
            ],
            "answer": "B",
            "explanation": "The present continuous imperative in Greek indicates ongoing, habitual action: 'keep on asking, keep on seeking, keep on knocking' (Luke 11:9-10)."
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 4
    # ─────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "The Analogy of the Father's Good Gifts",
        "unit_description": "Examine the contrast in Luke 11:11-13 between imperfect earthly parents and the Heavenly Father, analyzing lookalike gifts and the supreme gift of the Holy Spirit.",
        "lesson_title": "The Analogy of the Father's Good Gifts",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Rembrandt_Harmensz_van_Rijn_-_Return_of_the_Prodigal_Son_-_Google_Art_Project.jpg/800px-Rembrandt_Harmensz_van_Rijn_-_Return_of_the_Prodigal_Son_-_Google_Art_Project.jpg",
            "title": "Visual Hook: The Loving Father",
            "author": "Rembrandt van Rijn (Hermitage Museum)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A profound artistic portrayal of divine fatherhood, illustrating unconditional love, protective care, and sovereign generosity."
        },
        "youtube": {
            "youtube_id": "oNNZO9i1Gjc",
            "title": "BibleProject: The Holy Spirit",
            "description": "Explores the identity, power, and role of the Holy Spirit as God's supreme personal gift that guides, comforts, and transforms believers."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Analyze the metaphorical comparisons in Luke 11:11-13 (fish vs. serpent, egg vs. scorpion).",
            "Explain Jesus' 'how much more' theological argument contrasting earthly parenting with the perfect character of God.",
            "Identify why the Holy Spirit is revealed as the supreme gift given by the Heavenly Father to those who ask."
        ],
        "intro": "Imagine coming home after a strenuous day of sports and studies, telling your parent or guardian that you are starving, and asking for a piece of roasted fish or a boiled egg. How would you react if they chuckled and handed you a live, poisonous cobra or a venomous scorpion? You would be horrified and bewildered!\n\nEven human parents—who have flaws, bad moods, and limitations—instinctively love, feed, and protect their children from danger. Jesus used this universal family instinct to construct an unshakeable theological truth: if flawed human beings know how to give good gifts to their children, how infinitely more can we trust the loving heart of our Heavenly Father?",
        "core_scripture": "### Biblical Passage: The Analogy of Parental Care\n\n#### Luke 11:11-13 — Earthly Fathers vs. The Heavenly Father\n> *\"Which of you fathers, if your son asks for a fish, will give him a snake instead? Or if he asks for an egg, will give him a scorpion?\n>\n> If you then, though you are evil, know how to give good gifts to your children, how much more will your Father in heaven give the Holy Spirit to those who ask him!\"*\n\n#### Matthew 7:9-11 — The Parallel Witness\n> *\"Which of you, if your son asks for bread, will give him a stone? Or if he asks for a fish, will give him a snake? If you, then, though you are evil, know how to give good gifts to your children, how much more will your Father in heaven give good gifts to those who ask him!\"*",
        "theological_pillars": "### Theological & Cultural Analysis of Luke 11:11-13\n\n1. **The Deceptive Lookalikes in Palestine:**\n   - **Fish vs. Serpent:** In the Sea of Galilee, an eel or water snake could look superficially similar to a scaleless fish, but the serpent was non-kosher, slimy, and dangerous.\n   - **Egg vs. Scorpion:** The pale Palestinian scorpion (*Buthus quinquestriatus*) curls its tail tightly when resting, closely resembling a small bird's egg in size and color. A cruel father could theoretically substitute one for the other, inflicting a deadly sting.\n2. **The 'A Fortiori' Argument (From Lesser to Greater):** Jesus utilizes a classic Rabbinic reasoning known as *Kal Vachomer* (light and heavy, or how much more). If imperfect, sinful human beings are moved by natural affection to provide wholesome nutrition, God—who is the author of pure love—will never deceive, trick, or harm His children.\n3. **The Supreme Gift — The Holy Spirit:** While Matthew 7:11 records 'good gifts', Luke 11:13 specifies 'the Holy Spirit'. Jesus shifts the focus from temporary material sustenance to eternal spiritual empowerment. The Holy Spirit is God's own presence dwelling within believers, offering wisdom, moral courage, and comforting peace.",
        "deep_dive": "### Deep Dive: Trusting the Character of God in Prayer\n\n- **1. Eliminating Fear and Suspicion in Prayer:** Many believers fear that asking God for help might lead to arbitrary punishment or severe deprivation. Jesus destroys this misconception: God is a good Father whose nature is generosity and protection.\n- **2. Understanding God's Refusals:** If a child mistakenly asks for a brightly colored poisonous snake thinking it is a toy, a loving father says 'No!' Similarly, when God denies or redirects our prayers, it is because He refuses to hand us scorpions that would destroy our spiritual lives.\n- **3. The Superiority of Spiritual Gifts over Material Goods:** Material riches, exam scores, and physical comfort pass away. The Holy Spirit provides eternal life, spiritual discernment, the fruit of righteousness (Galatians 5:22-23), and continuous access to the Father.",
        "practical": {
            "title": "Action Framework: Praying with Childlike Trust and Seeking the Spirit",
            "steps": [
                "Step 1: Approach God as a Loving Father — Discard feelings of fear, unworthiness, or intimidation; pray with the confidence of a beloved child.",
                "Step 2: Entrust Your Needs to Divine Wisdom — Bring all physical and academic needs honestly, while trusting God's discernment on what is truly good for you.",
                "Step 3: Pray Daily for the Infilling of the Holy Spirit — Ask specifically for wisdom in your studies, patience in trials, and moral courage against peer pressure.",
                "Step 4: Honor Earthly Parents and Guardians — Express gratitude to parents and guardians who work hard daily to provide nourishment, shelter, and education."
            ]
        },
        "kenyan_context": "In Kenyan communities, parents make immense sacrifices—selling agricultural produce, working overtime, and taking cooperative loans—to pay school fees and provide nutritious meals (ugali, sukuma wiki, fish, milk, and eggs) for their children. Reflecting on this parental dedication helps Kenyan learners understand the boundless, sacrificial love of God, who supplies all our spiritual and physical needs.",
        "reflection": "### Spiritual & Ethical Reflection\n\n- When you ask God for something and do not receive it, do you ever consider that God might be protecting you from a 'hidden serpent or scorpion'?\n- Why is having the Holy Spirit within your heart more valuable than having abundant pocket money or material luxuries?",
        "takeaways": [
            "Jesus uses the analogy of parental care (fish vs. serpent, egg vs. scorpion) to illustrate God's pure benevolence.",
            "If imperfect earthly parents provide good things for their children, our perfect Heavenly Father will grant far greater blessings.",
            "Luke 11:13 reveals that the greatest, most transformative gift God gives to those who ask is the Holy Spirit.",
            "Believers can pray with absolute security and joy, knowing that God never tricks, harms, or abandons His children."
        ],
        "mcq": {
            "question": "In Luke 11:13, what supreme gift does Jesus promise that the Heavenly Father will give to those who ask Him?",
            "options": [
                "A) Boundless material wealth and gold",
                "B) Exemption from all academic tests",
                "C) The Holy Spirit",
                "D) Political authority over neighbors"
            ],
            "answer": "C",
            "explanation": "In Luke 11:13, Jesus concludes that the Heavenly Father will give the Holy Spirit to those who ask Him, providing eternal wisdom, comfort, and guidance."
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 5
    # ─────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Persistent Prayer in Christian Life",
        "unit_description": "Examine the spiritual discipline of persistent, unceasing prayer (1 Thessalonians 5:17, Philippians 4:6-7), exploring how persistence transforms character and builds intimacy with God.",
        "lesson_title": "Persistent Prayer in Christian Life",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Nicolaes_Maes_-_Old_Woman_at_Prayer_-_WGA13830.jpg/800px-Nicolaes_Maes_-_Old_Woman_at_Prayer_-_WGA13830.jpg",
            "title": "Visual Hook: Old Woman at Prayer",
            "author": "Nicolaes Maes (Rijksmuseum, Amsterdam)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A devoted woman pausing in humble thanksgiving before a simple meal, embodying lifelong dedication and constant prayer."
        },
        "youtube": {
            "youtube_id": "174h316-c-8",
            "title": "BibleProject: 1 Thessalonians & Praying Without Ceasing",
            "description": "Explores Paul's exhortation to live in constant communion with God through unceasing prayer, thanksgiving, and joyful hope."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Define 'persistence' in Christian Religious Education and differentiate it from mechanical repetition.",
            "Analyze 1 Thessalonians 5:17 and Philippians 4:6-7 to explain the spiritual benefits of continuous prayer.",
            "Design a structured personal daily prayer routine that integrates morning devotions, breath prayers, and intercession."
        ],
        "intro": "Imagine an athlete who desires to win a gold medal in the national athletics championships. Does the athlete go to the running track on one single Monday, jog for ten minutes, and expect to break records? Of course not! True physical conditioning requires waking up at dawn day after day, running through rain and heat, stretching sore muscles, and maintaining strict dietary discipline over months and years.\n\nPersistent prayer functions in the exact same manner for our spiritual life. Prayer is not a magical emergency siren that we pull only when disaster strikes; it is the spiritual oxygen and discipline that sustains our daily walk with God, shaping our character and anchoring our peace.",
        "core_scripture": "### Biblical Foundations of Unceasing Prayer\n\n#### 1 Thessalonians 5:16-18 — Unbroken Devotion\n> *\"Rejoice always, pray continually, give thanks in all circumstances; for this is God’s will for you in Christ Jesus.\"*\n\n#### Philippians 4:6-7 — Replacing Anxiety with Prayer\n> *\"Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.\"*\n\n#### Luke 18:1 — The Parable of the Persistent Widow\n> *\"Then Jesus told his disciples a parable to show them that they should always pray and not give up.\"*",
        "theological_pillars": "### Theological Foundations of Persistent Prayer\n\n1. **What Persistence (Importunity) Means:** Christian persistence is the unwavering, steadfast dedication to seek God continuously despite delays, emotional exhaustion, or apparent obstacles. It is not an attempt to overcome God's reluctance, but a demonstration of total reliance upon God's sovereignty.\n2. **Praying Continually (*Adialeiptos*):** In 1 Thessalonians 5:17, Paul uses the Greek adverb *adialeiptos*, which was used in ancient times to describe a hacking cough or recurring heartbeat. It does not mean reciting words non-stop every second, but living in unbroken spiritual awareness and open dialogue with God throughout all daily activities.\n3. **The Divine Exchange of Peace:** Philippians 4:6-7 outlines a spiritual law: when believers intentionally transfer their worries, academic pressures, and fears into God's hands through prayer accompanied by thanksgiving, God replaces inner turmoil with supernatural peace (*shalom*) that protects the heart.",
        "deep_dive": "### Deep Dive: Four Spiritual Transformations Wrought by Persistence\n\n- **1. Persistence Tests and Deepens Sincerity:** Casual, flippant requests are quickly forgotten. When we return to God repeatedly over months for a family member's salvation or personal integrity, we demonstrate genuine moral conviction.\n- **2. Persistence Forges Character and Patience:** Living in an age of instant digital gratification makes waiting difficult. Persistent prayer teaches us delayed gratification, spiritual endurance, and submission to God's perfect timetable.\n- **3. Persistence Aligns Desires with God's Will:** As we spend extended time in God's presence, the Holy Spirit convicts us of selfish motives, purifying our petitions until our desires reflect Kingdom priorities.\n- **4. Persistence Enhances Gratitude and Joy:** When an answer arrives after a long season of faithful prayer, our hearts overflow with genuine thanksgiving and praise, strengthening the faith of the entire community.",
        "practical": {
            "title": "Action Framework: Building a Resilient Daily Prayer Routine",
            "steps": [
                "Step 1: Set Designated Prayer Anchors — Establish specific morning and evening times for uninterrupted Scripture reading and quiet prayer.",
                "Step 2: Practice Continuous Breath Prayers — Whisper short prayers of thanksgiving, praise, and guidance between classes and during daily chores.",
                "Step 3: Maintain a Written Prayer Journal — Record specific petitions, dates of request, scripture promises, and notes on how God responds over time.",
                "Step 4: Intercede Faithfully for Others — Dedicate days of the week to pray for family members, school teachers, struggling peers, and national leaders."
            ]
        },
        "kenyan_context": "In Kenyan educational and community life, persistent prayer is reflected in traditions such as school Christian Union (CU) fellowships, Young Christian Students (YCS), morning assemblies, and community *Keshas* (overnight prayer vigils). When families face drought, economic hardship, or medical challenges, church communities gather faithfully to uphold one another in relentless, unified intercession.",
        "reflection": "### Spiritual & Ethical Reflection\n\n- When exam anxiety or peer pressure threatens to overwhelm your mind, do you panic or do you practice Philippians 4:6 by converting worry into prayer with thanksgiving?\n- How can keeping a personal prayer notebook help you recognize God's faithfulness during seasons when you feel spiritually discouraged?",
        "takeaways": [
            "Persistent prayer is an essential Christian discipline commanding believers to 'pray continually' and never give up (1 Thess 5:17, Luke 18:1).",
            "Continuous prayer is not babbling words endlessly, but maintaining a constant posture of spiritual communion and dependence upon God.",
            "Philippians 4:6-7 promises that bringing every anxiety to God in prayer produces supernatural peace that guards our hearts and minds.",
            "Persistence refines our sincerity, builds moral endurance, purifies our motives, and prepares us to receive God's answers with gratitude."
        ],
        "mcq": {
            "question": "According to Philippians 4:6-7, what is promised to believers who bring their anxieties to God through prayer with thanksgiving?",
            "options": [
                "A) Immediate material wealth and instant success",
                "B) Complete exemption from all earthly troubles",
                "C) The peace of God, which transcends all understanding, guarding hearts and minds",
                "D) The ability to see future historical events in advance"
            ],
            "answer": "C",
            "explanation": "Philippians 4:6-7 promises that presenting our requests to God with thanksgiving brings the peace of God, which transcends understanding, guarding our hearts and minds in Christ Jesus."
        }
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LESSON 6
    # ─────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Trusting God's Answers",
        "unit_description": "Analyze the threefold nature of God's answers to prayer (Yes, No, Wait), examining Romans 8:26-28 and James 1:5-6 to develop spiritual maturity in handling delays and redirections.",
        "lesson_title": "Trusting God's Answers",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Hofmann-ChristInTheGardenOfGethsemane.jpg/800px-Hofmann-ChristInTheGardenOfGethsemane.jpg",
            "title": "Visual Hook: Christ in Gethsemane",
            "author": "Heinrich Hofmann (Riverside Church, New York)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus praying in the Garden of Gethsemane, demonstrating absolute submission to the Father's sovereign will: 'Not my will, but Yours be done.'"
        },
        "youtube": {
            "youtube_id": "qn-hLHWw9yY",
            "title": "BibleProject: Romans 8 & Trusting God in Suffering",
            "description": "Explores how the Holy Spirit intercedes for us in our weakness and how God sovereignly orchestrates all circumstances for the eternal good of His children."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Analyze the three primary ways God answers prayer: 'Yes' (Provision), 'No' (Protection), and 'Wait' (Preparation).",
            "Examine Romans 8:26-28 and James 1:5-6 to understand the Holy Spirit's intercession and God's sovereign wisdom.",
            "Demonstrate spiritual maturity when dealing with disappointments, delayed outcomes, or unmet personal expectations."
        ],
        "intro": "Imagine a five-year-old child who excitedly asks their parent for a sharp, shiny butcher knife to use as a toy during playtime. What does a loving parent immediately say? 'No!' The young child might burst into tears, stomp their feet, and complain that the parent is being cruel and unfair. Yet the parent's firm 'No' is an act of deep, protective love.\n\nIn our relationship with God, we often act like that five-year-old child. We ask for things that seem appealing on the surface, but which would harm our character, distract us from our purpose, or lead us into spiritual danger. Spiritual maturity begins when we recognize that God answers every single prayer with perfect wisdom—sometimes with 'Yes', sometimes with 'No', and often with 'Wait'.",
        "core_scripture": "### Biblical Foundations of Trusting Divine Answers\n\n#### Romans 8:26-28 — The Spirit's Intercession and God's Sovereign Good\n> *\"In the same way, the Spirit helps us in our weakness. We do not know what we ought to pray for, but the Spirit himself intercedes for us through wordless groans. And he who searches our hearts knows the mind of the Spirit, because the Spirit intercedes for God’s people in accordance with the will of God.\n>\n> And we know that in all things God works for the good of those who love him, who have been called according to his purpose.\"*\n\n#### James 1:5-6 — Asking for Wisdom in Faith\n> *\"If any of you lacks wisdom, you should ask God, who gives generously to all without finding fault, and it will be given to you. But when you ask, you must believe and not doubt, because the one who doubts is like a wave of the sea, blown and tossed by the wind.\"*\n\n#### Luke 22:42 — Christ's Supreme Surrender in Gethsemane\n> *\"'Father, if you are willing, take this cup from me; yet not my will, but yours be done.'\"*",
        "theological_pillars": "### The Threefold Categories of God's Answers\n\n1. **YES (Immediate Provision):** When our request aligns with God's Word, timing, and divine purpose, He grants it graciously. The appropriate Christian response is immediate thanksgiving, humility, and dedicating the blessing to serve others.\n2. **NO (Protective Redirection):** When our petition is driven by selfish motives (James 4:3), pride, or would result in spiritual harm, God says 'No'. God's refusal is a shield of grace. Even Jesus in Gethsemane surrendered to the Father's 'No' regarding the cup of crucifixion, accomplishing universal salvation.\n3. **WAIT (Patient Preparation):** When the request is good, but our character or timing is not yet ready. The period of waiting develops endurance, tests faith, and prepares the believer to steward the blessing responsibly without succumbing to pride.",
        "deep_dive": "### Deep Dive: Navigating Unanswered Prayers and Delays\n\n- **1. The Intercession of the Holy Spirit (Romans 8:26):** In seasons of profound sorrow, confusion, or weakness, believers often do not know what words to formulate. The Holy Spirit intercedes within our hearts, translating our wordless groans into perfect alignment with the Father's will.\n- **2. The Assurance of Romans 8:28:** God does not promise that every earthly event will be pleasant, but that He will sovereignly weave all circumstances—including closed doors and disappointments—into ultimate spiritual good for those who love Him.\n- **3. Examining Motives and Overcoming Bitterness (James 4:3):** When prayers seem delayed, we must avoid resentment. We should examine whether we are asking for personal vanity, material greed, or peer validation, and realign our hearts with God's Kingdom.",
        "practical": {
            "title": "Action Framework: Responding to God's Answers with Faith and Maturity",
            "steps": [
                "Step 1: Adopt the Gethsemane Posture — Pray with complete honesty, while concluding every petition with: 'Not my will, but Yours be done.'",
                "Step 2: Evaluate Personal Motives (James 4:3) — Reflect on whether your requests seek God's glory and community service or selfish status.",
                "Step 3: Embrace Waiting Seasons with Productive Service — Instead of idling or complaining, serve actively in school, home, and church while waiting on God.",
                "Step 4: Trust Romans 8:28 in Setbacks — When facing disappointing exam results or missed opportunities, praise God for His protective wisdom and redirect your focus."
            ]
        },
        "kenyan_context": "In Kenyan academic and youth life, students often face intense emotional moments: awaiting KCSE / Junior School assessment placements, competing for school prefect roles, or facing family financial hurdles. When a student does not get selected for their dream school or leadership post, a spiritually mature learner trusts that God has a different path for their growth, maintaining diligence and supporting fellow students with genuine kindness.",
        "reflection": "### Spiritual & Ethical Reflection\n\n- Can you remember a past prayer request where God said 'No' or 'Wait', and you later realized it spared you from serious harm or regret?\n- How does knowing that the Holy Spirit intercedes for you when you don't know what to pray bring comfort in difficult times?",
        "takeaways": [
            "God answers prayers in three primary ways: 'Yes' (Provision), 'No' (Protection), and 'Wait' (Preparation).",
            "God's 'No' is an act of protective love, shielding us from requests that would harm our spiritual well-being or compromise our purpose.",
            "Romans 8:26-28 assures believers that the Holy Spirit intercedes in our weakness and that God orchestrates all things for our ultimate good.",
            "Spiritual maturity is demonstrated by submitting to God's sovereign will with trust, patience, and continued obedience (Luke 22:42)."
        ],
        "mcq": {
            "question": "How should a mature Christian respond when God answers a prayer request with a protective 'No' or a delayed 'Wait'?",
            "options": [
                "A) Stop praying entirely, complain bitterly, and abandon church",
                "B) Trust in God's sovereign wisdom, maintain patience, and continue faithful obedience",
                "C) Try to bribe God with financial promises",
                "D) Conclude that God is indifferent and uncaring"
            ],
            "answer": "B",
            "explanation": "A mature Christian recognizes that God's wisdom is perfect (Romans 8:28). When God says 'No' or 'Wait', the believer responds with trust, patience, and continued obedience (Luke 22:42)."
        }
    }
]


# ─── MAIN INGESTION FUNCTION ──────────────────────────────────────────────────

def ingest_all_grade9_cre_topic7_lessons():
    print("=" * 80)
    print("STARTING INGESTION FOR GRADE 9 CRE — TOPIC 7: PARABLE ON PRAYER — A FRIEND AT MIDNIGHT")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade & Subject
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50, grade=grade)

        print(f"Curriculum: {grade.curriculum.name}")
        print(f"Grade     : {grade.name} (ID: {grade.id})")
        print(f"Subject   : {subject.name} (ID: {subject.id})")

        # 2. Resolve / Create Topic 7
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=7,
            defaults={
                "name": "Parable on Prayer — A Friend at Midnight",
                "description": "Explores Jesus' teachings on prayer through the Parable of the Friend at Midnight (Luke 11:5-13), focusing on the nature of parables, the value of persistence in prayer, the character of God as a loving Father, and cultivating a consistent prayer life."
            }
        )
        if not created:
            topic.name = "Parable on Prayer — A Friend at Midnight"
            topic.description = "Explores Jesus' teachings on prayer through the Parable of the Friend at Midnight (Luke 11:5-13), focusing on the nature of parables, the value of persistence in prayer, the character of God as a loving Father, and cultivating a consistent prayer life."
            topic.save()
            print(f"[+] Resolved existing Topic ID: {topic.id} (Order: {topic.order}, Name: '{topic.name}')")
        else:
            print(f"[+] Created Topic ID: {topic.id} (Order: {topic.order}, Name: '{topic.name}')")

        # Ingest each of the 6 lessons
        for l_idx, cfg in enumerate(TOPIC_7_LESSONS, start=1):
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            print("\n" + "-" * 70)
            print(f"[*] Ingesting Lesson {l_idx}/6: '{l_title}' (Unit {u_order}: '{u_name}')")
            print("-" * 70)

            # Clean existing LearningUnit for this order if present to guarantee clean slate
            existing_units = LearningUnit.objects.filter(topic=topic, order=u_order)
            if existing_units.exists():
                for eu in existing_units:
                    print(f"  [-] Removing existing LearningUnit order={u_order} (ID: {eu.id})")
                    eu.delete()

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=clean_text(cfg["unit_description"])
            )
            print(f"  [+] Created LearningUnit ID: {unit.id} ('{unit.name}', order={unit.order})")

            # Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                immutable_metadata={
                    "grade": "Grade 9",
                    "grade_id": 18,
                    "subject": "CRE",
                    "subject_id": 50,
                    "topic_order": 7,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "unit_name": unit.name,
                    "author": "VLearn Grade 9 CRE Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            print(f"  [+] Created Lesson ID: {lesson.id} ('{lesson.title}')")

            # ─── ATTACH 3 LESSON ASSETS ───
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

            # Asset 2: Responsive SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_7_lesson_{l_idx}.svg",
                metadata={
                    "svg_xml": svg_content,
                    "viewBox": "0 0 800 450",
                    "theme": "#0f172a"
                }
            )

            # Asset 3: Curated YouTube Video
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
            print(f"  [+] Attached 3 LessonAssets (Image, SVG Diagram, YouTube Video)")

            # ─── CREATE 6 CARDS / PAGES WITH 13 LESSON BLOCKS ───

            # CARD 1 (Page 1): Discovery & Objectives (3 blocks)
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
                title="Engaging Hook & Real-World Connection",
                content={"markdown": clean_text(cfg["intro"])}
            )

            # CARD 2 (Page 2): Scriptural Exegesis (2 blocks)
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Core Biblical Foundations",
                content={"markdown": clean_text(cfg["core_scripture"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=45, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Exegesis & Linguistic Insights",
                content={"markdown": clean_text(cfg["theological_pillars"])}
            )

            # CARD 3 (Page 3): Pedagogical Diagram & Deep Dive (2 blocks)
            b6 = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram & Deep Dive",
                order=50, component_order=1,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {l_title}",
                content={
                    "title": f"Pedagogical Diagram: {l_title}",
                    "caption": f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b6.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram & Deep Dive",
                order=60, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title=f"Deep Dive Analysis: {l_title}",
                content={"markdown": clean_text(cfg["deep_dive"])}
            )

            # CARD 4 (Page 4): Practical Application & Context (2 blocks)
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
                title="Kenyan Real-World Context & Cultural Values",
                content={"markdown": clean_text(cfg["kenyan_context"])}
            )

            # CARD 5 (Page 5): Multimedia & Reflection (2 blocks)
            b10 = LessonBlock.objects.create(
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
            b10.assets.add(yt_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
                order=90, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Spiritual Reflection & Ethical Questions",
                content={"markdown": clean_text(cfg["reflection"])}
            )

            # CARD 6 (Page 6): Mastery Check (2 blocks)
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

            print(f"  [+] Created 6 Pages (13 Blocks total) for Lesson ID: {lesson.id}")

    print("\n" + "=" * 80)
    print("ALL 6 LESSONS FOR TOPIC 7 INGESTED SUCCESSFULLY!")
    print("=" * 80)


if __name__ == "__main__":
    ingest_all_grade9_cre_topic7_lessons()
