"""
VLearn CBC Grade 10 CRE — Topic 1.1: The Holy Bible
Production Ingestion Script
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

# ==============================================================================
# SVGs DEFINITIONS (Vector pedagogical diagrams)
# ==============================================================================

SVG_ORGANIC_INSPIRATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="divineGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="humanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#c2410c" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="overlapGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#6d28d9" stop-opacity="1"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="880" height="440" rx="16" fill="#0f172a"/>
  
  <!-- Title & Subtitle -->
  <text x="440" y="42" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">The Concept of Organic Inspiration (Theopneustos)</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="13" text-anchor="middle">2 Timothy 3:16 — God-breathed truth through human personalities and styles</text>

  <!-- Left Circle: Divine Guidance -->
  <circle cx="280" cy="235" r="140" fill="url(#divineGrad)" filter="url(#shadow)" opacity="0.88"/>
  <text x="210" y="195" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">DIVINE ORIGIN</text>
  <text x="210" y="220" fill="#e0f2fe" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">• Holy Spirit guidance</text>
  <text x="210" y="242" fill="#e0f2fe" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">• Divine Truth &amp; Authority</text>
  <text x="210" y="264" fill="#e0f2fe" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">• Inerrant Message</text>
  <text x="210" y="286" fill="#bae6fd" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">(God as Primary Author)</text>

  <!-- Right Circle: Human Agency -->
  <circle cx="600" cy="235" r="140" fill="url(#humanGrad)" filter="url(#shadow)" opacity="0.88"/>
  <text x="670" y="195" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">HUMAN WRITERS</text>
  <text x="670" y="220" fill="#ffedd5" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">• Distinct Personalities</text>
  <text x="670" y="242" fill="#ffedd5" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">• Cultural &amp; Historical Context</text>
  <text x="670" y="264" fill="#ffedd5" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">• Varied Literary Styles</text>
  <text x="670" y="286" fill="#fed7aa" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">(Kings, Shepherds, Prophets)</text>

  <!-- Overlap Center Box -->
  <rect x="360" y="150" width="160" height="170" rx="12" fill="url(#overlapGrad)" filter="url(#shadow)" stroke="#c4b5fd" stroke-width="1.5"/>
  <text x="440" y="180" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="800" text-anchor="middle">HOLY SCRIPTURE</text>
  <line x1="380" y1="190" x2="500" y2="190" stroke="#ddd6fe" stroke-width="1"/>
  <text x="440" y="210" fill="#f5f3ff" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">100% Divine Message</text>
  <text x="440" y="230" fill="#ddd6fe" font-family="system-ui, -apple-system, sans-serif" font-size="11" text-anchor="middle">+</text>
  <text x="440" y="250" fill="#f5f3ff" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">100% Human Writing</text>
  <text x="440" y="275" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">"God-Breathed"</text>
  <text x="440" y="295" fill="#ede9fe" font-family="system-ui, -apple-system, sans-serif" font-size="10" text-anchor="middle">(Theopneustos)</text>

  <!-- Bottom Contrast Callout: Organic vs Mechanical Dictation -->
  <rect x="100" y="390" width="680" height="34" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="440" y="412" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">
    <tspan fill="#38bdf8" font-weight="700">Organic Inspiration:</tspan> Partnership preserving human style &amp; mind | <tspan fill="#f87171" font-weight="700">Mechanical Dictation (False):</tspan> Passive trance / typing machine
  </text>
</svg>"""

SVG_HUMAN_AUTHORS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000" flood-opacity="0.2"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="880" height="480" rx="16" fill="#0f172a"/>
  
  <!-- Header -->
  <text x="440" y="36" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Diversity of Old Testament Human Authors</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="13" text-anchor="middle">God utilized individuals across 1,500 years from every walk of life</text>

  <!-- Grid of 6 representative authors -->
  <!-- Card 1: Moses -->
  <g transform="translate(40, 80)" filter="url(#cardShadow)">
    <rect width="250" height="175" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="36" rx="10" fill="#1d4ed8"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">MOSES</text>
    <text x="16" y="62" fill="#93c5fd" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Background:</text>
    <text x="16" y="80" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="12">Prince, Shepherd, Lawgiver</text>
    <text x="16" y="108" fill="#93c5fd" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Books Written:</text>
    <text x="16" y="126" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Pentateuch / Torah (5 Books)</text>
    <text x="16" y="144" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11">Genesis to Deuteronomy</text>
    <text x="16" y="162" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Style: Legal Code &amp; Narrative</text>
  </g>

  <!-- Card 2: David -->
  <g transform="translate(315, 80)" filter="url(#cardShadow)">
    <rect width="250" height="175" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="36" rx="10" fill="#047857"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">DAVID</text>
    <text x="16" y="62" fill="#6ee7b7" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Background:</text>
    <text x="16" y="80" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="12">Shepherd Boy, Warrior, King</text>
    <text x="16" y="108" fill="#6ee7b7" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Books Written:</text>
    <text x="16" y="126" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Psalms (Primary Author)</text>
    <text x="16" y="144" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11">e.g., Psalm 23, 51, 103</text>
    <text x="16" y="162" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Style: Lyrical Poetry, Prayer &amp; Song</text>
  </g>

  <!-- Card 3: Solomon -->
  <g transform="translate(590, 80)" filter="url(#cardShadow)">
    <rect width="250" height="175" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="36" rx="10" fill="#b45309"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SOLOMON</text>
    <text x="16" y="62" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Background:</text>
    <text x="16" y="80" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="12">Wise Monarch, Temple Builder</text>
    <text x="16" y="108" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Books Written:</text>
    <text x="16" y="126" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Proverbs, Ecclesiastes, Song</text>
    <text x="16" y="144" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11">Wisdom Literature</text>
    <text x="16" y="162" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Style: Maxims, Philosophical Reflection</text>
  </g>

  <!-- Card 4: Amos -->
  <g transform="translate(40, 275)" filter="url(#cardShadow)">
    <rect width="250" height="175" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="36" rx="10" fill="#be185d"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">AMOS</text>
    <text x="16" y="62" fill="#fbcfe8" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Background:</text>
    <text x="16" y="80" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="12">Rural Shepherd, Sycamore Dresser</text>
    <text x="16" y="108" fill="#fbcfe8" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Books Written:</text>
    <text x="16" y="126" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Book of Amos</text>
    <text x="16" y="144" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11">Minor Prophet (9 Chapters)</text>
    <text x="16" y="162" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Style: Bold Social Justice &amp; Imagery</text>
  </g>

  <!-- Card 5: Jeremiah -->
  <g transform="translate(315, 275)" filter="url(#cardShadow)">
    <rect width="250" height="175" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="36" rx="10" fill="#6d28d9"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">JEREMIAH</text>
    <text x="16" y="62" fill="#ddd6fe" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Background:</text>
    <text x="16" y="80" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="12">Village Priest, "Weeping Prophet"</text>
    <text x="16" y="108" fill="#ddd6fe" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Books Written:</text>
    <text x="16" y="126" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Jeremiah, Lamentations</text>
    <text x="16" y="144" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11">Major Prophet &amp; Funeral Laments</text>
    <text x="16" y="162" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Style: Prophetic Warning &amp; Grief</text>
  </g>

  <!-- Card 6: Joshua & Samuel -->
  <g transform="translate(590, 275)" filter="url(#cardShadow)">
    <rect width="250" height="175" rx="10" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="36" rx="10" fill="#0e7490"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">JOSHUA &amp; SAMUEL</text>
    <text x="16" y="62" fill="#a5f3fc" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Background:</text>
    <text x="16" y="80" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="12">Military Leader &amp; Judge/Prophet</text>
    <text x="16" y="108" fill="#a5f3fc" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Books Written:</text>
    <text x="16" y="126" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600">Joshua, 1 &amp; 2 Samuel (Parts)</text>
    <text x="16" y="144" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11">Historical Books</text>
    <text x="16" y="162" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Style: Historical Chronicling</text>
  </g>
</svg>"""

SVG_OT_ORGANISATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 500" width="100%" height="100%">
  <defs>
    <filter id="shelfShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="880" height="500" rx="16" fill="#0f172a"/>

  <!-- Header -->
  <text x="440" y="36" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Structure of the Old Testament Library (39 Books)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="13" text-anchor="middle">Four distinct functional sections arranged by literary character and historical role</text>

  <!-- Shelf 1: The Law -->
  <g transform="translate(40, 80)" filter="url(#shelfShadow)">
    <rect width="800" height="85" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect x="0" y="0" width="180" height="85" rx="10" fill="#1d4ed8"/>
    <text x="90" y="38" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">THE LAW</text>
    <text x="90" y="58" fill="#bfdbfe" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">(Pentateuch / Torah)</text>
    <text x="90" y="74" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5 BOOKS</text>
    
    <text x="200" y="34" fill="#60a5fa" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700">Genesis • Exodus • Leviticus • Numbers • Deuteronomy</text>
    <text x="200" y="58" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Focus: Creation, patriarchal covenant, origin of Israel, and God's moral and ceremonial commandments given through Moses.</text>
  </g>

  <!-- Shelf 2: Historical Books -->
  <g transform="translate(40, 180)" filter="url(#shelfShadow)">
    <rect width="800" height="85" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="180" height="85" rx="10" fill="#047857"/>
    <text x="90" y="38" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">HISTORICAL</text>
    <text x="90" y="58" fill="#a7f3d0" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">National Chronicles</text>
    <text x="90" y="74" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">12 BOOKS</text>
    
    <text x="200" y="30" fill="#34d399" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="700">Joshua • Judges • Ruth • 1 &amp; 2 Samuel • 1 &amp; 2 Kings • 1 &amp; 2 Chronicles • Ezra • Nehemiah • Esther</text>
    <text x="200" y="56" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Focus: Conquest of Canaan, judges, monarchy, civil war, Babylonian exile, and return to rebuild the Jerusalem temple.</text>
  </g>

  <!-- Shelf 3: Poetry & Wisdom -->
  <g transform="translate(40, 280)" filter="url(#shelfShadow)">
    <rect width="800" height="85" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="180" height="85" rx="10" fill="#b45309"/>
    <text x="90" y="38" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14.5" font-weight="700" text-anchor="middle">POETRY &amp; WISDOM</text>
    <text x="90" y="58" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Worship &amp; Life Skills</text>
    <text x="90" y="74" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5 BOOKS</text>
    
    <text x="200" y="34" fill="#fbbf24" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700">Job • Psalms • Proverbs • Ecclesiastes • Song of Songs</text>
    <text x="200" y="58" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Focus: Deep reflection on human suffering, prayers of praise and lament, practical moral sayings, and divine love.</text>
  </g>

  <!-- Shelf 4: Prophetic Books -->
  <g transform="translate(40, 380)" filter="url(#shelfShadow)">
    <rect width="800" height="100" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="180" height="100" rx="10" fill="#7e22ce"/>
    <text x="90" y="44" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">PROPHETIC</text>
    <text x="90" y="66" fill="#e9d5ff" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Messages &amp; Visions</text>
    <text x="90" y="86" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">17 BOOKS</text>
    
    <!-- Major Prophets -->
    <text x="200" y="28" fill="#c084fc" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="700">Major Prophets (5 Longer Books): <tspan fill="#f1f5f9" font-weight="400">Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel</tspan></text>
    <!-- Minor Prophets -->
    <text x="200" y="52" fill="#c084fc" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="700">Minor Prophets (12 Shorter Books): <tspan fill="#f1f5f9" font-weight="400">Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi</tspan></text>
    <text x="200" y="80" fill="#fef08a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600">Note: "Major" vs "Minor" indicates book length (scroll size), NOT spiritual value or authority!</text>
  </g>
</svg>"""

SVG_LITERARY_FORMS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">
  <defs>
    <filter id="boxShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="880" height="460" rx="16" fill="#0f172a"/>

  <!-- Title -->
  <text x="440" y="36" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Major Literary Genres of the Bible &amp; Interpretation Rules</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="13" text-anchor="middle">Every biblical genre has its own unique rules of interpretation</text>

  <!-- Genre 1: Narrative -->
  <g transform="translate(40, 80)" filter="url(#boxShadow)">
    <rect width="250" height="165" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="#1d4ed8"/>
    <text x="125" y="23" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. NARRATIVE (Stories)</text>
    <text x="14" y="58" fill="#93c5fd" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Examples:</text>
    <text x="14" y="76" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Genesis 1-2, Exodus, Ruth</text>
    <text x="14" y="102" fill="#93c5fd" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">How to Read:</text>
    <text x="14" y="120" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Look for God's actions and overall moral lesson across the full arc.</text>
    <text x="14" y="148" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Warning: Don't assume all acts are approved.</text>
  </g>

  <!-- Genre 2: Law -->
  <g transform="translate(315, 80)" filter="url(#boxShadow)">
    <rect width="250" height="165" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="#047857"/>
    <text x="125" y="23" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. LAW (Commandments)</text>
    <text x="14" y="58" fill="#6ee7b7" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Examples:</text>
    <text x="14" y="76" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Exodus 20 (10 Commandments)</text>
    <text x="14" y="102" fill="#6ee7b7" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">How to Read:</text>
    <text x="14" y="120" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Identify the enduring moral principle behind the covenant command.</text>
    <text x="14" y="148" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Warning: Understand ancient legal context.</text>
  </g>

  <!-- Genre 3: Poetry -->
  <g transform="translate(590, 80)" filter="url(#boxShadow)">
    <rect width="250" height="165" rx="10" fill="#f59e0b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="#b45309"/>
    <text x="125" y="23" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. POETRY (Songs/Laments)</text>
    <text x="14" y="58" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Examples:</text>
    <text x="14" y="76" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Psalms, Song of Songs</text>
    <text x="14" y="102" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">How to Read:</text>
    <text x="14" y="120" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Focus on emotional expression, parallel lines, metaphors, and symbols.</text>
    <text x="14" y="148" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Warning: Don't read metaphors as literal science.</text>
  </g>

  <!-- Genre 4: Prophecy -->
  <g transform="translate(40, 265)" filter="url(#boxShadow)">
    <rect width="250" height="165" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="#6d28d9"/>
    <text x="125" y="23" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">4. PROPHECY</text>
    <text x="14" y="58" fill="#ddd6fe" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Examples:</text>
    <text x="14" y="76" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Isaiah, Jeremiah, Amos</text>
    <text x="14" y="102" fill="#ddd6fe" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">How to Read:</text>
    <text x="14" y="120" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Focus on the call to justice, repentance, and covenant faithfulness.</text>
    <text x="14" y="148" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Warning: It is mostly forthtelling, not secret code.</text>
  </g>

  <!-- Genre 5: Wisdom Literature -->
  <g transform="translate(315, 265)" filter="url(#boxShadow)">
    <rect width="250" height="165" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="#be185d"/>
    <text x="125" y="23" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">5. WISDOM</text>
    <text x="14" y="58" fill="#fbcfe8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Examples:</text>
    <text x="14" y="76" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Proverbs, Ecclesiastes, Job</text>
    <text x="14" y="102" fill="#fbcfe8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">How to Read:</text>
    <text x="14" y="120" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">General practical principles and observations for righteous living.</text>
    <text x="14" y="148" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Warning: Proverbs are general truths, not absolute promises.</text>
  </g>

  <!-- Genre 6: Genealogy -->
  <g transform="translate(590, 265)" filter="url(#boxShadow)">
    <rect width="250" height="165" rx="10" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="250" height="34" rx="10" fill="#0e7490"/>
    <text x="125" y="23" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">6. GENEALOGY</text>
    <text x="14" y="58" fill="#a5f3fc" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Examples:</text>
    <text x="14" y="76" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">Genesis 5, 11, 1 Chronicles 1-9</text>
    <text x="14" y="102" fill="#a5f3fc" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">How to Read:</text>
    <text x="14" y="120" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="11">Traces God's covenant faithfulness through family lines and promises.</text>
    <text x="14" y="148" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Warning: Links theology with real historical lineage.</text>
  </g>
</svg>"""

SVG_PARALLELISM_TYPES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">
  <defs>
    <filter id="pShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000" flood-opacity="0.2"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="880" height="460" rx="16" fill="#0f172a"/>

  <!-- Header -->
  <text x="440" y="36" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Hebrew Poetry: The 3 Primary Forms of Parallelism</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="13" text-anchor="middle">Ancient Hebrew poetry rhymes concepts and ideas rather than phonetic sounds</text>

  <!-- Card 1: Synonymous Parallelism -->
  <g transform="translate(40, 80)" filter="url(#pShadow)">
    <rect width="250" height="340" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect width="250" height="40" rx="10" fill="#1d4ed8"/>
    <text x="125" y="26" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SYNONYMOUS (=)</text>
    
    <text x="125" y="68" fill="#60a5fa" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Idea A = Repeated in Idea B</text>
    <text x="16" y="92" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">The second line repeats the thought of the first line using different words for emphasis.</text>

    <!-- Visual Diagram Box -->
    <rect x="16" y="130" width="218" height="58" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="125" y="152" fill="#93c5fd" font-family="system-ui, -apple-system, sans-serif" font-size="11" text-anchor="middle">Line 1: ➔ ➔ [Idea 1]</text>
    <text x="125" y="172" fill="#93c5fd" font-family="system-ui, -apple-system, sans-serif" font-size="11" text-anchor="middle">Line 2: ➔ ➔ [Same Idea Rephrased]</text>

    <text x="16" y="210" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700">Scripture Example:</text>
    <text x="16" y="230" fill="#60a5fa" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600">Psalm 19:1</text>
    <text x="16" y="250" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-style="italic">"The heavens declare the glory of God;"</text>
    <text x="16" y="280" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-style="italic">"The skies proclaim the work of His hands."</text>
    
    <text x="16" y="316" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Heavens = Skies | Declare = Proclaim</text>
  </g>

  <!-- Card 2: Antithetic Parallelism -->
  <g transform="translate(315, 80)" filter="url(#pShadow)">
    <rect width="250" height="340" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="250" height="40" rx="10" fill="#b91c1c"/>
    <text x="125" y="26" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ANTITHETIC (≠ / vs)</text>
    
    <text x="125" y="68" fill="#f87171" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Idea A vs Contrasted with B</text>
    <text x="16" y="92" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">The second line expresses the opposite or contrasting thought to show a sharp division.</text>

    <!-- Visual Diagram Box -->
    <rect x="16" y="130" width="218" height="58" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="125" y="152" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="11" text-anchor="middle">Line 1: ➔ ➔ [Positive Concept]</text>
    <text x="125" y="172" fill="#fca5a5" font-family="system-ui, -apple-system, sans-serif" font-size="11" text-anchor="middle">Line 2: ➔ ➔ [Negative / Opposite]</text>

    <text x="16" y="210" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700">Scripture Example:</text>
    <text x="16" y="230" fill="#f87171" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600">Proverbs 10:1</text>
    <text x="16" y="250" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-style="italic">"A wise son brings joy to his father,"</text>
    <text x="16" y="280" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-style="italic">"But a foolish son brings grief to his mother."</text>
    
    <text x="16" y="316" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Wise/Foolish • Joy/Grief • Father/Mother</text>
  </g>

  <!-- Card 3: Synthetic Parallelism -->
  <g transform="translate(590, 80)" filter="url(#pShadow)">
    <rect width="250" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="250" height="40" rx="10" fill="#047857"/>
    <text x="125" y="26" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SYNTHETIC (+ / &gt;)</text>
    
    <text x="125" y="68" fill="#34d399" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Idea A + Completed by B</text>
    <text x="16" y="92" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5">The second line builds on, develops, or completes the thought introduced in the first line.</text>

    <!-- Visual Diagram Box -->
    <rect x="16" y="130" width="218" height="58" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="125" y="152" fill="#6ee7b7" font-family="system-ui, -apple-system, sans-serif" font-size="11" text-anchor="middle">Line 1: ➔ [Premise / Foundation]</text>
    <text x="125" y="172" fill="#6ee7b7" font-family="system-ui, -apple-system, sans-serif" font-size="11" text-anchor="middle">Line 2: ➔ ➔ [Outcome / Climax]</text>

    <text x="16" y="210" fill="#fde68a" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700">Scripture Example:</text>
    <text x="16" y="230" fill="#34d399" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600">Psalm 23:1</text>
    <text x="16" y="250" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-style="italic">"The Lord is my shepherd;"</text>
    <text x="16" y="280" fill="#e2e8f0" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-style="italic">"I shall not want."</text>
    
    <text x="16" y="316" fill="#cbd5e1" font-family="system-ui, -apple-system, sans-serif" font-size="10.5">Line 2 is the direct consequence of Line 1</text>
  </g>
</svg>"""


# ==============================================================================
# LESSON DATA DEFINITIONS (5 Published Lessons)
# ==============================================================================

CRE_TOPIC_1_LESSONS = [
    # -------------------------------------------------------------------------
    # LESSON 1: The Bible as the Inspired Word of God
    # -------------------------------------------------------------------------
    {
        "unit_order": 1,
        "unit_name": "The Bible as the Inspired Word of God",
        "unit_description": "Christian understanding of divine inspiration (theopneustos), scriptural evidence, and distinguishing organic inspiration from mechanical dictation.",
        "lesson_title": "The Bible as the Inspired Word of God",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Ancient Codex Sinaiticus Manuscript",
                    "content": {
                        "title": "Codex Sinaiticus Ancient Manuscript",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Codex_Sinaiticus_Matthew_6%2C4-8%2C1.jpg",
                        "caption": "A page from Codex Sinaiticus, one of the earliest surviving four-century Greek Bible manuscripts, showing hand-scribed biblical text.",
                        "author": "Wikimedia Commons / British Library",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the Christian concept of divine inspiration (theopneustos).\n- Identify scriptural evidence supporting the Bible as the inspired Word of God.\n- Distinguish between organic divine inspiration and mechanical dictation.\n- Apply the values of truthfulness, reverence, and humility in daily life."
                    }
                }
            ],
            # Card 2: Scripture Foundation & Key Verses
            [
                {
                    "type": "definition_card",
                    "title": "Divine Inspiration (Theopneustos)",
                    "content": {
                        "term": "Divine Inspiration",
                        "definition": "The special supernatural influence of the Holy Spirit upon human authors, ensuring that their writings faithfully and accurately communicate God's message."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Scriptural Testimony to God's Word",
                    "content": {
                        "text": "The Bible testifies to its own divine origin across both Testaments:\n\n- **2 Timothy 3:16-17:** *'All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness, so that the servant of God may be thoroughly equipped for every good work.'*\n- **Psalm 12:6:** *'The words of the Lord are pure words, like silver tried in a furnace of earth, purified seven times.'*\n- **Psalm 119:160:** *'The entirety of Your word is truth, and every one of Your righteous judgments endures forever.'*\n- **Jeremiah 1:9:** *'Then the Lord put forth His hand and touched my mouth, and said to me: Behold, I have put My words in your mouth.'*"
                    }
                }
            ],
            # Card 3: Pedagogical SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Organic Inspiration: Divine Truth through Human Agency",
                    "content": {
                        "title": "Organic Inspiration Concept Map",
                        "caption": "Diagram depicting organic inspiration: The Holy Spirit guides the divine message while fully engaging the author's personality, background, and literary style.",
                        "svg_content": SVG_ORGANIC_INSPIRATION
                    }
                }
            ],
            # Card 4: Deeper Explanation & Misconceptions
            [
                {
                    "type": "concept_explanation",
                    "title": "Organic Inspiration vs Mechanical Dictation",
                    "content": {
                        "text": "When Christians confess that Scripture is **God-breathed** (*theopneustos*), it refers to a dynamic, organic partnership:\n\n- **Organic Inspiration (Christian Doctrine):** God the Holy Spirit illuminated and guided human writers without bypassing their intelligence, vocabulary, historical context, or feelings. A king wrote from royal experience, while a shepherd drew upon flock imagery.\n- **Mechanical Dictation (Common Misconception):** The false idea that human authors were passive typing machines or in unconscious trances, merely taking down whispered words without using their minds."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "What is the Bible? by BibleProject",
                    "content": {
                        "title": "What is the Bible? (BibleProject)",
                        "youtube_id": "ak06MSETeo4",
                        "embed_url": "https://www.youtube.com/embed/ak06MSETeo4",
                        "description": "An engaging visual overview of how the Bible was written, its divine inspiration, and how diverse ancient scrolls unite into a single story."
                    }
                }
            ],
            # Card 5: Values & Contemporary Ethical Dilemma
            [
                {
                    "type": "concept_explanation",
                    "title": "Christian Values: Truthfulness & Academic Integrity",
                    "content": {
                        "text": "Belief in God's inspired Word anchors three core values:\n\n- **Truthfulness:** Committing to absolute honesty in our speech and academic work.\n- **Reverence:** Treating sacred Scripture with deep respect and honoring God's authority.\n- **Humility:** Willingly submitting our opinions to God's moral guidance."
                    }
                },
                {
                    "type": "ethical_dilemma",
                    "title": "Contemporary Dilemma: The Academic Integrity Test",
                    "content": {
                        "scenario": "Your best friend has experienced severe family illness and could not study for an end-of-term national evaluation. During the exam, they ask you to tilt your paper so they can copy your answers to avoid failing.",
                        "options": [
                            "Option A: Allow them to copy out of sympathy so they pass without trouble.",
                            "Option B: Politely protect your script, then offer to tutor them and approach the teacher for academic support."
                        ],
                        "guidance": "Option B upholds Biblical truthfulness and integrity while providing constructive, genuine compassion without cheating."
                    }
                }
            ],
            # Card 6: Knowledge Check MCQ
            [
                {
                    "type": "mcq_interactive",
                    "title": "Knowledge Check: Organic Divine Inspiration",
                    "content": {
                        "question": "Which of the following statements accurately describes the Christian belief in the 'organic inspiration' of the Bible?",
                        "options": [
                            "A. God dictated every word word-for-word while the human writers were in an unconscious trance.",
                            "B. The Holy Spirit guided human authors to communicate divine truth while using their unique writing styles, backgrounds, and vocabularies.",
                            "C. Human authors wrote purely from human memory and wisdom, and God approved the books centuries later.",
                            "D. The Bible fell from heaven as a complete, bound physical book in ancient times."
                        ],
                        "correct_answer": "B",
                        "explanation": "Organic inspiration means God worked through living human agents—preserving their personalities, cultural idioms, and literary styles—so that the resulting Scriptures communicate God's authoritative Word perfectly."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 2: Human Authors Inspired to Write the Holy Bible
    # -------------------------------------------------------------------------
    {
        "unit_order": 2,
        "unit_name": "Human Authors Inspired to Write the Holy Bible",
        "unit_description": "Prominent human writers of the Old Testament, their diverse socio-economic backgrounds, and how God uses human experiences in revelation.",
        "lesson_title": "Human Authors Inspired to Write the Holy Bible",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "The Prophet Jeremiah by Michelangelo",
                    "content": {
                        "title": "Michelangelo's Depiction of the Prophet Jeremiah",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/41/Michelangelo_Buonarroti_026.jpg",
                        "caption": "Michelangelo's Sistine Chapel fresco depicting the human sorrow and prophetic reflection of the prophet Jeremiah.",
                        "author": "Michelangelo / Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify prominent Old Testament human authors and the books traditionally attributed to them.\n- Match biblical authors with their diverse social roles and life backgrounds.\n- Appreciate how God uses varied human personalities and occupations to reveal His truth."
                    }
                }
            ],
            # Card 2: Core Concept & Author Overview
            [
                {
                    "type": "concept_explanation",
                    "title": "Diversity of Human Authors",
                    "content": {
                        "text": "The Old Testament was written over 1,500 years by more than 40 distinct human authors. God did not recruit from one elite class; He spoke through:\n\n- **Princes & Lawgivers:** Moses was educated in Pharaoh's palace and later led Israel in the desert.\n- **Kings & Shepherds:** David was a humble shepherd before becoming Israel's most celebrated warrior-king.\n- **Royal Sages:** Solomon possessed royal resources and worldly wisdom, compiling thousands of proverbs.\n- **Agricultural Workers:** Amos was an ordinary shepherd and tender of sycamore fig trees.\n- **Priests & Prophets:** Jeremiah came from a village priestly family in Anathoth."
                    }
                }
            ],
            # Card 3: Comparison Table
            [
                {
                    "type": "comparison_table",
                    "title": "Old Testament Authors, Backgrounds & Works",
                    "content": {
                        "headers": ["Human Author", "Social Role / Background", "Books Attributed", "Literary Style / Theme"],
                        "rows": [
                            ["Moses", "Prince of Egypt, Shepherd, Lawgiver", "Pentateuch (Genesis to Deuteronomy)", "Law, Historical Covenant Narrative"],
                            ["Joshua", "Military Commander & Successor", "Book of Joshua", "Historical Conquest Narratives"],
                            ["David", "Shepherd Boy, Warrior, Monarch", "Psalms (Main Psalmist)", "Poetry, Songs of Praise & Lament"],
                            ["Solomon", "Wise King, Builder of Temple", "Proverbs, Ecclesiastes, Song of Songs", "Wisdom Sayings, Practical Maxims"],
                            ["Amos", "Rural Shepherd, Sycamore Dresser", "Book of Amos", "Prophetic Social Justice Critiques"],
                            ["Jeremiah", "Village Priest, 'Weeping Prophet'", "Jeremiah, Lamentations", "Prophetic Warnings & Funeral Laments"]
                        ]
                    }
                }
            ],
            # Card 4: Pedagogical SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Diversity of Old Testament Human Authors",
                    "content": {
                        "title": "Old Testament Authors Profile Grid",
                        "caption": "Pedagogical infographic detailing representative Old Testament human writers, their occupations, and their contributions to Scripture.",
                        "svg_content": SVG_HUMAN_AUTHORS
                    }
                }
            ],
            # Card 5: Educational Video & Values Application
            [
                {
                    "type": "suggested_video",
                    "title": "The Story of the Bible: Human Authors",
                    "content": {
                        "title": "The Making of the Old Testament (BibleProject)",
                        "youtube_id": "ALcL3C465no",
                        "embed_url": "https://www.youtube.com/embed/ALcL3C465no",
                        "description": "How God partnered with diverse human writers over centuries to produce the cohesive Hebrew Scriptures."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Real-World Value: Academic Honesty & Attribution",
                    "content": {
                        "text": "Just as the Bible transparently names and attributes its human writers, students must practice **Integrity** and **Intellectual Honesty** by always citing authors and avoiding plagiarism in school assignments."
                    }
                }
            ],
            # Card 6: Knowledge Check MCQ
            [
                {
                    "type": "mcq_interactive",
                    "title": "Knowledge Check: Old Testament Authors",
                    "content": {
                        "question": "Which of the following pairings of an Old Testament author and their background is INCORRECT?",
                        "options": [
                            "A. David — Shepherd boy and King who authored many Psalms.",
                            "B. Amos — Wealthy royal priest from Jerusalem who wrote official court annals.",
                            "C. Solomon — Monarch renowned for wisdom who compiled Proverbs.",
                            "D. Moses — Prophet and lawgiver associated with the Pentateuch."
                        ],
                        "correct_answer": "B",
                        "explanation": "Amos was not a wealthy royal priest; he was a rural shepherd and caretaker of sycamore-fig trees from Tekoa called to deliver God's message of social justice."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 3: Organisation of the Old Testament Books
    # -------------------------------------------------------------------------
    {
        "unit_order": 3,
        "unit_name": "Organisation of the Old Testament Books",
        "unit_description": "Classification of the 39 Old Testament books into Law (Torah), Historical, Poetical/Wisdom, and Prophetic (Major and Minor) categories.",
        "lesson_title": "Organisation of the Old Testament Books",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Traditional Hebrew Torah Scroll",
                    "content": {
                        "title": "Sefer Torah Scroll on Bima",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Torah_Scroll.jpg",
                        "caption": "An open Hebrew parchment scroll of the Torah (Law of Moses), representing the foundational five books of the Old Testament.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the four primary divisions of the 39 Old Testament books.\n- Correctly classify individual books into their appropriate section.\n- Explain the true distinction between 'Major' and 'Minor' prophets based on scroll length."
                    }
                }
            ],
            # Card 2: The 4 Sections of the Old Testament Library
            [
                {
                    "type": "concept_explanation",
                    "title": "The Old Testament Library of 39 Books",
                    "content": {
                        "text": "The Old Testament is organized into four main sections:\n\n1. **The Law (Pentateuch / Torah) — 5 Books:** Genesis, Exodus, Leviticus, Numbers, Deuteronomy.\n2. **Historical Books — 12 Books:** Joshua, Judges, Ruth, 1 & 2 Samuel, 1 & 2 Kings, 1 & 2 Chronicles, Ezra, Nehemiah, Esther.\n3. **Poetical and Wisdom Literature — 5 Books:** Job, Psalms, Proverbs, Ecclesiastes, Song of Songs.\n4. **Prophetic Books — 17 Books:** Divided into 5 Major Prophets (longer texts) and 12 Minor Prophets (shorter scrolls)."
                    }
                }
            ],
            # Card 3: Pedagogical SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Old Testament Library Architecture (39 Books)",
                    "content": {
                        "title": "Old Testament Classification Map",
                        "caption": "Visual shelf diagram of the 39 Old Testament books broken down into Law, History, Poetry/Wisdom, and Major/Minor Prophets.",
                        "svg_content": SVG_OT_ORGANISATION
                    }
                }
            ],
            # Card 4: Major vs Minor Prophets Explanation
            [
                {
                    "type": "concept_explanation",
                    "title": "Understanding Major and Minor Prophets",
                    "content": {
                        "text": "A frequent misconception among learners is that 'Major' prophets held higher rank or divine authority than 'Minor' prophets.\n\n- **The True Difference:** The terms refer purely to **physical book length and scroll capacity**.\n- **Major Prophets (5 Books):** Isaiah (66 chapters), Jeremiah (52 chapters), Lamentations (5 chapters/poem collection), Ezekiel (48 chapters), Daniel (12 chapters).\n- **Minor Prophets (12 Books):** Hosea, Joel, Amos, Obadiah (1 chapter), Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi. In the ancient Hebrew canon, all twelve were grouped together onto a single scroll called *The Twelve*."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Overview of the Old Testament (BibleProject)",
                    "content": {
                        "title": "The Old Testament Canon Overview",
                        "youtube_id": "7_CGP-12AE0",
                        "embed_url": "https://www.youtube.com/embed/7_CGP-12AE0",
                        "description": "A structural overview of the Old Testament collection, its categories, and its overarching theological message."
                    }
                }
            ],
            # Card 5: Interactive Sorting & Library Practice
            [
                {
                    "type": "comparison_table",
                    "title": "Quick Reference: Old Testament Book Classification",
                    "content": {
                        "headers": ["Book Name", "Old Testament Division", "Subcategory", "Primary Theme"],
                        "rows": [
                            ["Deuteronomy", "The Law (Pentateuch)", "Torah", "Covenant renewal and moral laws"],
                            ["Nehemiah", "Historical Books", "Post-Exilic History", "Rebuilding Jerusalem's walls and spiritual reform"],
                            ["Psalms", "Poetical & Wisdom", "Poetry / Prayer", "Hymns of praise, thanksgiving, and lament"],
                            ["Isaiah", "Prophetic Books", "Major Prophet", "Messianic prophecy and judgment/redemption"],
                            ["Amos", "Prophetic Books", "Minor Prophet", "Social justice, righteousness, and warning to Israel"]
                        ]
                    }
                }
            ],
            # Card 6: Knowledge Check MCQ
            [
                {
                    "type": "mcq_interactive",
                    "title": "Knowledge Check: Old Testament Classification",
                    "content": {
                        "question": "Why are books like Hosea, Amos, Micah, and Malachi designated as 'Minor Prophets' in the Christian Bible?",
                        "options": [
                            "A. Their spiritual messages were of secondary importance to Israel.",
                            "B. They were written during periods of spiritual decline.",
                            "C. Their books are shorter in physical length and word count compared to the Major Prophets.",
                            "D. They were written by younger prophets with less social authority."
                        ],
                        "correct_answer": "C",
                        "explanation": "The term 'Minor' refers solely to the shorter length of their writings, not their theological weight or prophetic authority."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 4: Literary Forms Used in Writing the Bible
    # -------------------------------------------------------------------------
    {
        "unit_order": 4,
        "unit_name": "Literary Forms Used in Writing the Bible",
        "unit_description": "Recognizing major biblical literary genres—narrative, law, poetry, prophecy, wisdom, and genealogy—and applying genre-appropriate interpretation.",
        "lesson_title": "Literary Forms Used in Writing the Bible",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Dead Sea Scrolls Parchment Fragment",
                    "content": {
                        "title": "Dead Sea Scrolls Great Isaiah Scroll",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/The_Great_Isaiah_Scroll_MS_A_%281QIsa%29_-_Israel_Museum_-_Jerusalem.jpg",
                        "caption": "The Great Isaiah Scroll found at Qumran, demonstrating Hebrew poetic and prophetic text layout from ancient times.",
                        "author": "The Israel Museum / Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the major literary genres found in the Old Testament.\n- Match biblical passages to their appropriate literary form.\n- Explain why genre awareness is essential to avoid misinterpreting biblical passages."
                    }
                }
            ],
            # Card 2: Core Concepts & The 6 Major Genres
            [
                {
                    "type": "concept_explanation",
                    "title": "Why Literary Forms Matter in Bible Study",
                    "content": {
                        "text": "Just as a reader interprets a newspaper headline differently from a song lyric or a science textbook, biblical passages must be read according to their **literary form**:\n\n1. **Narrative (Historical Stories):** Factual historical accounts written to show God's covenant actions (e.g., Abraham's call in Genesis 12).\n2. **Law (Commandments):** Direct moral, ceremonial, and civil commands (e.g., Exodus 20).\n3. **Poetry (Songs & Laments):** Expressive emotional language using metaphors and parallel ideas (e.g., Psalms).\n4. **Prophecy (Spoken Word of God):** Messages confronting injustice, proclaiming divine judgment, and offering hope (e.g., Isaiah, Amos).\n5. **Wisdom Literature:** Practical guidelines, observations, and maxims for righteous living (e.g., Proverbs).\n6. **Genealogy (Lineage Records):** Historical family records connecting covenant generations (e.g., Genesis 5, 1 Chronicles 1)."
                    }
                }
            ],
            # Card 3: Pedagogical SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Biblical Literary Genres & Interpretation Guidelines",
                    "content": {
                        "title": "Literary Genre Analysis Chart",
                        "caption": "Pedagogical diagram mapping the six primary Old Testament genres with rules of engagement and common interpretative pitfalls.",
                        "svg_content": SVG_LITERARY_FORMS
                    }
                }
            ],
            # Card 4: Genre Interpretation Rules Table
            [
                {
                    "type": "comparison_table",
                    "title": "Reading Rules and Pitfalls for Biblical Genres",
                    "content": {
                        "headers": ["Genre", "Primary Purpose", "Accurate Reading Method", "Common Pitfall to Avoid"],
                        "rows": [
                            ["Narrative", "Tells what occurred in redemptive history", "Look for the central theological lesson and character arc", "Assuming every character's action is endorsed by God"],
                            ["Law", "Governs covenant community conduct", "Identify the timeless moral principle behind the specific law", "Applying ancient civil penalties directly to modern secular law"],
                            ["Poetry", "Expresses emotion and worship", "Appreciate metaphors, imagery, and poetic feelings", "Interpreting poetic metaphors (e.g. 'trees clapping') as literal science"],
                            ["Prophecy", "Calls people back to covenant faithfulness", "Focus on the urgent call for justice and repentance in its day", "Treating prophecy purely as a codebook for modern dates"],
                            ["Wisdom", "Provides life advice and observations", "Read as general principles for successful righteous living", "Treating proverbs as mechanical, unconditional promises"]
                        ]
                    }
                }
            ],
            # Card 5: Video & Practical Genre Detection
            [
                {
                    "type": "suggested_video",
                    "title": "Literary Styles in the Bible (BibleProject)",
                    "content": {
                        "title": "Literary Styles in the Bible",
                        "youtube_id": "oUUBlHP1mho",
                        "embed_url": "https://www.youtube.com/embed/oUUBlHP1mho",
                        "description": "How the Bible uses narrative, poetry, and discourse to weave a multi-layered theological masterpiece."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Practice: Identifying Biblical Genres",
                    "content": {
                        "text": "Test your genre identification skills on these passages:\n\n- *'The Lord is my rock and my fortress and my deliverer...'* (Psalm 18:2) ➔ **Poetry (Metaphor)**\n- *'Honor your father and your mother...'* (Exodus 20:12) ➔ **Law (Commandment)**\n- *'In the second year of King Darius, word came through Haggai...'* (Haggai 1:1) ➔ **Prophecy**\n- *'This is the family line of Noah: Noah was a righteous man...'* (Genesis 6:9) ➔ **Narrative / Genealogy**"
                    }
                }
            ],
            # Card 6: Knowledge Check MCQ
            [
                {
                    "type": "mcq_interactive",
                    "title": "Knowledge Check: Literary Forms",
                    "content": {
                        "question": "Why is it essential to recognize the literary form of a biblical passage before interpreting its meaning?",
                        "options": [
                            "A. Because only narratives and laws are inspired, while poems are optional human reflections.",
                            "B. Because each genre follows different literary rules, and a poetic metaphor should not be read as literal technical science.",
                            "C. To determine whether the biblical text was written in Hebrew, Greek, or Latin.",
                            "D. To rank which passages carry superior divine authority over others."
                        ],
                        "correct_answer": "B",
                        "explanation": "Literary forms carry distinct conventions. Interpreting a poetic metaphor or proverb as a literal scientific description distorts the original meaning intended by the inspired author."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 5: Utilizing the Poetic Form: Songs from the Book of Psalms
    # -------------------------------------------------------------------------
    {
        "unit_order": 5,
        "unit_name": "Utilizing the Poetic Form: Songs from the Book of Psalms",
        "unit_description": "Key elements of Hebrew poetry in Psalms, including synonymous, antithetic, and synthetic parallelism, imagery, and emotional honesty in worship.",
        "lesson_title": "Utilizing the Poetic Form: Songs from the Book of Psalms",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "King David Playing the Harp",
                    "content": {
                        "title": "King David Playing the Harp (Gerard van Honthorst)",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Gerard_van_Honthorst_-_King_David_Playing_the_Harp_-_WGA11651.jpg",
                        "caption": "King David composing a psalm of praise with the lyre, representing the musical and liturgical heart of the Hebrew Psalms.",
                        "author": "Gerard van Honthorst / Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain how Hebrew poetry rhymed thoughts and concepts through parallelism.\n- Distinguish between synonymous, antithetic, and synthetic parallelism.\n- Analyze poetic imagery and metaphors in beloved Psalms (such as Psalms 23 and 121).\n- Value authentic, emotionally honest communication with God in prayer."
                    }
                }
            ],
            # Card 2: Hebrew Poetry and Parallelism Concept
            [
                {
                    "type": "definition_card",
                    "title": "Parallelism in Hebrew Poetry",
                    "content": {
                        "term": "Parallelism",
                        "definition": "The hallmark structure of biblical Hebrew poetry where two or more successive lines balance, contrast, or build upon ideas rather than rhyming word endings."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Primary Types of Parallelism",
                    "content": {
                        "text": "Ancient Hebrew poetry uses thought-rhyme across three primary forms:\n\n- **1. Synonymous Parallelism:** The second line repeats the central idea of the first line using different words to provide reinforcement.\n- **2. Antithetic Parallelism:** The second line presents a sharp contrast or opposite truth to highlight a moral distinction.\n- **3. Synthetic Parallelism:** The second line develops, expands, or completes the thought started in the first line."
                    }
                }
            ],
            # Card 3: Pedagogical SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Types of Hebrew Poetic Parallelism",
                    "content": {
                        "title": "Parallelism Classification Chart",
                        "caption": "Pedagogical diagram showing the structure, directional logic, and scriptural examples of synonymous, antithetic, and synthetic parallelism.",
                        "svg_content": SVG_PARALLELISM_TYPES
                    }
                }
            ],
            # Card 4: Poetic Imagery & Case Studies
            [
                {
                    "type": "concept_explanation",
                    "title": "Poetic Imagery in Psalms 23 and 121",
                    "content": {
                        "text": "The Psalms use vivid imagery to communicate spiritual intimacy and divine protection:\n\n- **Metaphor in Psalm 23:1:** *'The Lord is my shepherd; I shall not want.'* God is directly compared to a vigilant shepherd who provides pasture, rest, and protection.\n- **Synthetic Parallelism in Psalm 121:1-2:** *'I lift up my eyes to the hills—where does my help come from? My help comes from the Lord, the Maker of heaven and earth.'* Travelers navigating rugged, bandit-infested Judean mountains find ultimate security not in hills, but in the Creator."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Book of Psalms (BibleProject)",
                    "content": {
                        "title": "The Book of Psalms Overview",
                        "youtube_id": "j9phNEaPrv8",
                        "embed_url": "https://www.youtube.com/embed/j9phNEaPrv8",
                        "description": "How the Book of Psalms was compiled into a five-part prayer book for God's covenant people."
                    }
                }
            ],
            # Card 5: Values & Emotional Honesty in Worship
            [
                {
                    "type": "concept_explanation",
                    "title": "Emotional Honesty & The Prayer of Lament",
                    "content": {
                        "text": "Over a third of the Psalms are **laments**—prayers where believers cry out in sorrow, fear, or confusion (e.g., Psalm 13: *'How long, O Lord? Will you forget me forever?'*).\n\n- **Key Insight:** God welcomes genuine human emotion. Faithful prayer does not require pretending everything is fine; it brings real struggles honestly before God in trust."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Examples of Parallelism Types in Psalms & Proverbs",
                    "content": {
                        "headers": ["Passage", "First Line", "Second Line", "Parallelism Type"],
                        "rows": [
                            ["Psalm 19:1", "The heavens declare the glory of God;", "The skies proclaim the work of His hands.", "Synonymous Parallelism"],
                            ["Psalm 1:6", "The Lord watches over the way of the righteous,", "But the way of the wicked leads to destruction.", "Antithetic Parallelism"],
                            ["Psalm 23:1", "The Lord is my shepherd;", "I shall not want.", "Synthetic Parallelism"],
                            ["Proverbs 15:1", "A gentle answer turns away wrath,", "But a harsh word stirs up anger.", "Antithetic Parallelism"]
                        ]
                    }
                }
            ],
            # Card 6: Knowledge Check MCQ
            [
                {
                    "type": "mcq_interactive",
                    "title": "Knowledge Check: Parallelism in the Psalms",
                    "content": {
                        "question": "Read Psalm 1:6: 'For the Lord watches over the way of the righteous, but the way of the wicked leads to destruction.' What poetic form is demonstrated here?",
                        "options": [
                            "A. Synonymous Parallelism",
                            "B. Antithetic Parallelism",
                            "C. Synthetic Parallelism",
                            "D. Narrative Prose"
                        ],
                        "correct_answer": "B",
                        "explanation": "This is Antithetic Parallelism because the second line directly contrasts the destiny of the 'righteous' with the destructive outcome of the 'wicked'."
                    }
                }
            ]
        ]
    }
]


# ==============================================================================
# INGESTION WORKFLOW
# ==============================================================================

def clean_text(text: str) -> str:
    """Removes bracket citations and internal marker tags."""
    if not text:
        return ""
    # Strip bracket numbers e.g. [1], [223], [17, 303]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{1,})\]', '', text)
    # Strip internal visual tags
    text = re.sub(r'\[VISUAL:.*?\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[BIBLE PASSAGE:.*?\]', '', text)
    text = re.sub(r'\[KEY VERSE:.*?\]', '', text)
    text = re.sub(r'\[MISCONCEPTION\]', '', text)
    text = re.sub(r'\[VALUES\]', '', text)
    text = re.sub(r'\[INTERACTION:.*?\]', '', text)
    text = re.sub(r'\[BIBLICAL CONTEXT\]', '', text)
    text = re.sub(r'\[REAL WORLD APPLICATION\]', '', text)
    # Normalize bullet points
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
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


def ingest_topic_1_1(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 1.1: The Holy Bible (Grade 10 CRE)")
    print("=" * 80)

    # 1. Resolve Grade 10 and Subject CRE
    grade = Grade.objects.get(id=5)
    subject = Subject.objects.get(id=46)
    print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id})")
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id})")

    # 2. Get or Create Topic 1.1: The Holy Bible
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={
            "name": "The Holy Bible",
            "description": "Divine inspiration, human authorship, organization of the 39 Old Testament books, and biblical literary and poetic forms."
        }
    )
    if not t_created:
        topic.name = "The Holy Bible"
        topic.description = "Divine inspiration, human authorship, organization of the 39 Old Testament books, and biblical literary and poetic forms."
        topic.save()
    print(f"[*] Resolved Topic 1: {topic.name} (ID: {topic.id})")

    # 3. Clean up existing records if replacing
    if replace:
        print("[*] Clearing existing topic units, lessons, blocks, and assets...")
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
        for item in CRE_TOPIC_1_LESSONS:
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
                    "topic_order": 1,
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
                        block_id=f"g10_cre_t1_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 1, "unit_order": u_order, "page": page_idx}
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
                                "licensing": b_content.get("licensing", "Public Domain"),
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
                            url=b_content.get("embed_url", f"https://www.youtube.com/embed/{b_content['youtube_id']}"),
                            metadata={
                                "youtube_id": b_content["youtube_id"],
                                "embed_url": b_content.get("embed_url", ""),
                                "description": b_content.get("description", "")
                            }
                        )
                        block.assets.add(asset)
                        total_assets += 1

    print("\n" + "=" * 80)
    print("INGESTION & AUDIT COMPLETE SUMMARY")
    print("=" * 80)
    print(f"[*] Total Learning Units Created: {total_units}")
    print(f"[*] Total Lessons Created (Published): {total_lessons}")
    print(f"[*] Total Cards / Pages Created: {total_pages}")
    print(f"[*] Total Lesson Blocks Created: {total_blocks}")
    print(f"[*] Total Lesson Assets Attached: {total_assets}")
    print("=" * 80)

    return {
        "units": total_units,
        "lessons": total_lessons,
        "pages": total_pages,
        "blocks": total_blocks,
        "assets": total_assets
    }

if __name__ == "__main__":
    ingest_topic_1_1(replace=True)
