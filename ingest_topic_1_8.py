"""
VLearn CBC Grade 10 CRE — Topic 1.8: The Old Testament Prophets
Production Ingestion Script

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5)
Subject: CRE (ID: 46)
Topic: Topic 1.8: The Old Testament Prophets (Topic Order: 8)

7 Discrete Learning Units & Published Lessons:
  1. Understanding Prophets and Prophecy (6 Cards, ~12 Blocks)
  2. Categories of Prophets in the Old Testament (6 Cards, ~12 Blocks)
  3. Importance of Prophets in Israel (6 Cards, ~12 Blocks)
  4. Relationship Between Old and New Testament Prophecies (6 Cards, ~12 Blocks)
  5. Characteristics of False Prophets (6 Cards, ~12 Blocks)
  6. Discerning False Prophets Today (6 Cards, ~12 Blocks)
  7. Relevance of Prophecy to Christians Today (6 Cards, ~12 Blocks)
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
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    """Removes bracket citations and internal metadata markers."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [70], [73, 74], [23], etc.
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags e.g. [VISUAL: ...], [BIBLE PASSAGE: ...], [VALUES], etc.
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|ETHICAL APPLICATION|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|MCQ: HIGH|MCQ|TABLE)[^\]]*\]', '', text, flags=re.IGNORECASE)
    # Normalize unicode bullets
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

# =============================================================================
# SANITIZED RESPONSIVE VECTOR SVG DEFINITIONS (viewBox="0 0 800 450")
# =============================================================================

# Lesson 1: The Two Dimensions of Prophecy (Forthtelling vs Foretelling)
SVG_LESSON_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="forthGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="foreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="nabiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad1)" rx="14"/>

  <!-- Title Header -->
  <text x="400" y="40" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">THE TWIN DIMENSIONS OF BIBLICAL PROPHECY</text>
  <text x="400" y="65" fill="#94a3b8" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Prophet (Nabi) as God's Authorized Mouthpiece and Covenant Guardian</text>

  <!-- Center Hub: The Nabi -->
  <g filter="url(#shadow1)">
    <circle cx="400" cy="180" r="60" fill="url(#nabiGrad)" stroke="#fbbf24" stroke-width="3"/>
    <text x="400" y="168" fill="#ffffff" font-size="16" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">THE NABI</text>
    <text x="400" y="188" fill="#ffffff" font-size="11" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">נָביא (Spokesperson)</text>
    <text x="400" y="206" fill="#fef3c7" font-size="10" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Jeremiah 1:9</text>
  </g>

  <!-- Flow Arrows -->
  <path d="M 340 180 L 260 180" stroke="#3b82f6" stroke-width="3" stroke-dasharray="6,4"/>
  <polygon points="260,175 250,180 260,185" fill="#3b82f6"/>

  <path d="M 460 180 L 540 180" stroke="#10b981" stroke-width="3" stroke-dasharray="6,4"/>
  <polygon points="540,175 550,180 540,185" fill="#10b981"/>

  <!-- Left Card: Forthtelling (Proclamation) -->
  <g filter="url(#shadow1)">
    <rect x="35" y="90" width="215" height="230" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect x="35" y="90" width="215" height="38" rx="10" fill="url(#forthGrad)"/>
    <text x="142" y="115" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. FORTHTELLING (~90%)</text>
    
    <circle cx="142" cy="155" r="20" fill="#1e3a8a"/>
    <text x="142" y="161" fill="#93c5fd" font-size="16" text-anchor="middle">📢</text>

    <text x="142" y="195" fill="#60a5fa" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Present Moral Proclamation</text>
    <text x="50" y="220" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Exposes present social sins</text>
    <text x="50" y="240" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Calls for radical repentance</text>
    <text x="50" y="260" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Rebukes injustice &amp; greed</text>
    <text x="50" y="280" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Real-time covenant defense</text>
    <text x="142" y="306" fill="#38bdf8" font-size="10" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">e.g., Amos 5:24</text>
  </g>

  <!-- Right Card: Foretelling (Prediction) -->
  <g filter="url(#shadow1)">
    <rect x="550" y="90" width="215" height="230" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="550" y="90" width="215" height="38" rx="10" fill="url(#foreGrad)"/>
    <text x="657" y="115" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. FORETELLING (~10%)</text>
    
    <circle cx="657" cy="155" r="20" fill="#064e3b"/>
    <text x="657" y="161" fill="#a7f3d0" font-size="16" text-anchor="middle">👁️</text>

    <text x="657" y="195" fill="#34d399" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Future Sovereign Prediction</text>
    <text x="565" y="220" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Reveals God's future acts</text>
    <text x="565" y="240" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Foretells exile &amp; return</text>
    <text x="565" y="260" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Foreshadows the Messiah</text>
    <text x="565" y="280" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Offers eternal restoration</text>
    <text x="657" y="306" fill="#6ee7b7" font-size="10" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">e.g., Isaiah 53 / Micah 5:2</text>
  </g>

  <!-- Bottom Clarification Footer -->
  <rect x="35" y="340" width="730" height="85" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="365" fill="#fbbf24" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">CRITICAL INSIGHT: BEYOND FORTUNE-TELLING</text>
  <text x="400" y="388" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">Biblical prophets were not fortunetellers predicting personal trivialities for hire.</text>
  <text x="400" y="408" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">They were divine prosecutors holding leaders and nations accountable to God's holy Law.</text>
</svg>"""

# Lesson 2: Categories of Prophets (Major, Minor, Non-Writing)
SVG_LESSON_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="majGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="minGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="nonGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad2)" rx="14"/>

  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">TAXONOMY OF OLD TESTAMENT PROPHETS</text>
  <text x="400" y="62" fill="#94a3b8" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Classification by Literary Scope, Scroll Length, and Historical Ministry Mode</text>

  <!-- Column 1: Major Prophets -->
  <g filter="url(#shadow2)">
    <rect x="30" y="85" width="230" height="260" rx="10" fill="#1e293b" stroke="#7c3aed" stroke-width="2"/>
    <rect x="30" y="85" width="230" height="38" rx="10" fill="url(#majGrad)"/>
    <text x="145" y="110" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">MAJOR PROPHETS (4/5)</text>

    <text x="145" y="145" fill="#c084fc" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Extensive, Expansive Scrolls</text>
    <text x="45" y="172" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Isaiah (66 Chapters)</text>
    <text x="45" y="192" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Jeremiah (+ Lamentations)</text>
    <text x="45" y="212" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Ezekiel (48 Chapters)</text>
    <text x="45" y="232" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Daniel (12 Chapters)</text>

    <rect x="42" y="255" width="206" height="75" rx="6" fill="#0f172a"/>
    <text x="50" y="275" fill="#a855f7" font-size="10" font-weight="700" font-family="system-ui, sans-serif">Distinguishing Feature:</text>
    <text x="50" y="295" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">Vast theological scope &amp; international</text>
    <text x="50" y="312" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">vision spanning multiple empires.</text>
  </g>

  <!-- Column 2: Minor Prophets -->
  <g filter="url(#shadow2)">
    <rect x="285" y="85" width="230" height="260" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
    <rect x="285" y="85" width="230" height="38" rx="10" fill="url(#minGrad)"/>
    <text x="400" y="110" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">MINOR PROPHETS (The 12)</text>

    <text x="400" y="145" fill="#38bdf8" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Shorter, Focused Scrolls</text>
    <text x="300" y="172" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif">• Hosea, Joel, Amos, Obadiah</text>
    <text x="300" y="192" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif">• Jonah, Micah, Nahum, Habakkuk</text>
    <text x="300" y="212" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif">• Zephaniah, Haggai</text>
    <text x="300" y="232" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif">• Zechariah, Malachi</text>

    <rect x="297" y="255" width="206" height="75" rx="6" fill="#0f172a"/>
    <text x="305" y="275" fill="#38bdf8" font-size="10" font-weight="700" font-family="system-ui, sans-serif">Distinguishing Feature:</text>
    <text x="305" y="295" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">Concise scrolls addressing urgent local</text>
    <text x="305" y="312" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">crises, social justice, and repentance.</text>
  </g>

  <!-- Column 3: Non-Writing Prophets -->
  <g filter="url(#shadow2)">
    <rect x="540" y="85" width="230" height="260" rx="10" fill="#1e293b" stroke="#d97706" stroke-width="2"/>
    <rect x="540" y="85" width="230" height="38" rx="10" fill="url(#nonGrad)"/>
    <text x="655" y="110" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">NON-WRITING (Action/Court)</text>

    <text x="655" y="145" fill="#fbbf24" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Recorded in Historical Books</text>
    <text x="555" y="172" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Samuel (Transition to Kings)</text>
    <text x="555" y="192" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Nathan (Confronted David)</text>
    <text x="555" y="212" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Elijah (Carmel showdown)</text>
    <text x="555" y="232" fill="#e2e8f0" font-size="11" font-weight="600" font-family="system-ui, sans-serif">• Elisha (Miracles &amp; State)</text>

    <rect x="552" y="255" width="206" height="75" rx="6" fill="#0f172a"/>
    <text x="560" y="275" fill="#fbbf24" font-size="10" font-weight="700" font-family="system-ui, sans-serif">Distinguishing Feature:</text>
    <text x="560" y="295" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">Direct, dynamic confrontations with</text>
    <text x="560" y="312" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">kings; books compiled by historians.</text>
  </g>

  <!-- Bottom Alert -->
  <rect x="30" y="360" width="740" height="65" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="385" fill="#f87171" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">COMMON MISCONCEPTION DEBUNKED</text>
  <text x="400" y="405" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">"Major" does NOT mean spiritually superior. All true prophets spoke with equal divine authority.</text>
</svg>"""

# Lesson 3: Importance and Multifaceted Roles of Prophets in Israel
SVG_LESSON_3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="centerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad3)" rx="14"/>

  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">THE MULTI-FACETED ROLES OF ISRAEL'S PROPHETS</text>
  <text x="400" y="62" fill="#94a3b8" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Moral Conscience, Covenant Guardians, and Voices of Divine Accountability</text>

  <!-- Central Hub: Sinaitic Covenant -->
  <g filter="url(#shadow3)">
    <circle cx="400" cy="220" r="65" fill="url(#centerGrad)" stroke="#fef3c7" stroke-width="2"/>
    <text x="400" y="210" fill="#ffffff" font-size="14" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">THE SINAITIC</text>
    <text x="400" y="228" fill="#ffffff" font-size="14" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">COVENANT</text>
    <text x="400" y="246" fill="#fde68a" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Moral Anchor</text>
  </g>

  <!-- Role 1: Rebuking Kings (Top-Left) -->
  <g filter="url(#shadow3)">
    <rect x="40" y="90" width="240" height="105" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="160" y="115" fill="#60a5fa" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. POLITICAL CONFRONTATION</text>
    <text x="55" y="138" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Advising and rebuking monarchs</text>
    <text x="55" y="156" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Enforcing God's supreme sovereignty</text>
    <text x="55" y="174" fill="#93c5fd" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">e.g., Nathan confronts David (2 Sam 12)</text>
  </g>
  <line x1="280" y1="155" x2="345" y2="190" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4,3"/>

  <!-- Role 2: Social Justice (Top-Right) -->
  <g filter="url(#shadow3)">
    <rect x="520" y="90" width="240" height="105" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="640" y="115" fill="#34d399" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. SOCIAL JUSTICE ADVOCACY</text>
    <text x="535" y="138" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Championing the poor, widows &amp; orphans</text>
    <text x="535" y="156" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Exposing rigged scales &amp; bribe extortion</text>
    <text x="535" y="174" fill="#a7f3d0" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">e.g., Amos condemns merchants (Amos 8:5)</text>
  </g>
  <line x1="520" y1="155" x2="455" y2="190" stroke="#10b981" stroke-width="2" stroke-dasharray="4,3"/>

  <!-- Role 3: Spiritual Renewal (Bottom-Left) -->
  <g filter="url(#shadow3)">
    <rect x="40" y="250" width="240" height="105" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="160" y="275" fill="#a78bfa" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. SPIRITUAL RENEWAL</text>
    <text x="55" y="298" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Eradicating pagan idolatry &amp; Baalism</text>
    <text x="55" y="316" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Demanding heart repentance over empty rituals</text>
    <text x="55" y="334" fill="#c4b5fd" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">e.g., Elijah on Mount Carmel (1 Kings 18)</text>
  </g>
  <line x1="280" y1="290" x2="345" y2="250" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,3"/>

  <!-- Role 4: Messianic Hope (Bottom-Right) -->
  <g filter="url(#shadow3)">
    <rect x="520" y="250" width="240" height="105" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="640" y="275" fill="#fbbf24" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">4. MESSIANIC HOPE &amp; RESTORATION</text>
    <text x="535" y="298" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Comforting exiled &amp; brokenhearted people</text>
    <text x="535" y="316" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Foretelling the Righteous Branch &amp; Savior</text>
    <text x="535" y="334" fill="#fde68a" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">e.g., Isaiah 53 &amp; Jeremiah 31 (New Covenant)</text>
  </g>
  <line x1="520" y1="290" x2="455" y2="250" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,3"/>

  <!-- Bottom Synthesis Banner -->
  <rect x="40" y="375" width="720" height="50" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="405" fill="#f8fafc" font-size="11" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Core Summary: Without prophets, Israel would have disintegrated into pagan tyranny and moral chaos.</text>
</svg>"""

# Lesson 4: OT Prophecies & NT Christological Fulfillment
SVG_LESSON_4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="otGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="ntGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#064e3b"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad4)" rx="14"/>

  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">OLD TESTAMENT PROPHECY &amp; NEW TESTAMENT FULFILLMENT</text>
  <text x="400" y="62" fill="#94a3b8" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Jesus Christ as the Divine Culmination of Prophecy and Typological Shadows</text>

  <!-- OT Column Header -->
  <rect x="40" y="85" width="310" height="34" rx="6" fill="url(#otGrad)"/>
  <text x="195" y="107" fill="#ffffff" font-size="12.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">OLD TESTAMENT PROMISES &amp; TYPES</text>

  <!-- NT Column Header -->
  <rect x="450" y="85" width="310" height="34" rx="6" fill="url(#ntGrad)"/>
  <text x="605" y="107" fill="#ffffff" font-size="12.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">NEW TESTAMENT CHRISTOLOGICAL REALITY</text>

  <!-- Row 1: Virgin Birth -->
  <g filter="url(#shadow4)">
    <rect x="40" y="130" width="310" height="55" rx="6" fill="#1e293b" stroke="#d97706" stroke-width="1"/>
    <text x="55" y="152" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Isaiah 7:14 — The Virgin Conception</text>
    <text x="55" y="170" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">"A virgin shall conceive and bear Immanuel"</text>

    <rect x="450" y="130" width="310" height="55" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="465" y="152" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Matthew 1:22-23 — Jesus Born of Mary</text>
    <text x="465" y="170" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">Incarnation: "God with Us" in human flesh</text>
  </g>
  <path d="M 355 157 L 445 157" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="445,153 450,157 445,161" fill="#fbbf24"/>

  <!-- Row 2: Bethlehem Birthplace -->
  <g filter="url(#shadow4)">
    <rect x="40" y="195" width="310" height="55" rx="6" fill="#1e293b" stroke="#d97706" stroke-width="1"/>
    <text x="55" y="217" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Micah 5:2 — Ruler from Bethlehem</text>
    <text x="55" y="235" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">"From you, Bethlehem Ephrathah, shall come..."</text>

    <rect x="450" y="195" width="310" height="55" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="465" y="217" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Matthew 2:1-6 — Birth in Bethlehem</text>
    <text x="465" y="235" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">Fulfills the ancient Davidic lineage promise</text>
  </g>
  <path d="M 355 222 L 445 222" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="445,218 450,222 445,226" fill="#fbbf24"/>

  <!-- Row 3: The Suffering Servant -->
  <g filter="url(#shadow4)">
    <rect x="40" y="260" width="310" height="55" rx="6" fill="#1e293b" stroke="#d97706" stroke-width="1"/>
    <text x="55" y="282" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Isaiah 53:5 — Pierced for Iniquities</text>
    <text x="55" y="300" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">Substitutionary suffering and healing by wounds</text>

    <rect x="450" y="260" width="310" height="55" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="465" y="282" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif">1 Peter 2:24 / Mark 15 — The Cross</text>
    <text x="465" y="300" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">Atonement: Christ bore our sins in His body</text>
  </g>
  <path d="M 355 287 L 445 287" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="445,283 450,287 445,291" fill="#fbbf24"/>

  <!-- Row 4: Typology: Passover Lamb -->
  <g filter="url(#shadow4)">
    <rect x="40" y="325" width="310" height="55" rx="6" fill="#1e293b" stroke="#d97706" stroke-width="1"/>
    <text x="55" y="347" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Exodus 12: The Passover Lamb</text>
    <text x="55" y="365" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">Spotless lamb's blood protects from death</text>

    <rect x="450" y="325" width="310" height="55" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="465" y="347" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif">1 Cor 5:7 / John 1:29 — Christ our Passover</text>
    <text x="465" y="365" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">"Look, the Lamb of God who takes away the sin!"</text>
  </g>
  <path d="M 355 352 L 445 352" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="445,348 450,352 445,356" fill="#fbbf24"/>

  <!-- Summary Line -->
  <text x="400" y="415" fill="#38bdf8" font-size="11.5" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Matthew 5:17 — "I have not come to abolish the Law or the Prophets, but to fulfill them."</text>
</svg>"""

# Lesson 5: Characteristics and Anatomy of False Prophets
SVG_LESSON_5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="dangerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad5)" rx="14"/>

  <text x="400" y="38" fill="#f87171" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">THE ANATOMY OF FALSE PROPHETS</text>
  <text x="400" y="62" fill="#cbd5e1" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Biblical Warning Criteria from Deuteronomy 18, Jeremiah 14, Micah 3 &amp; Matthew 7</text>

  <!-- 6 Grid Hallmarks -->
  <!-- Hallmark 1 -->
  <g filter="url(#shadow5)">
    <rect x="35" y="85" width="225" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="35" y="85" width="225" height="28" rx="8" fill="url(#dangerGrad)"/>
    <text x="147" y="104" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. SELF-ORIGINATED VISIONS</text>
    <text x="47" y="132" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Speak from their own imagination</text>
    <text x="47" y="150" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Fabricate divine dreams</text>
    <text x="47" y="185" fill="#fca5a5" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">Jeremiah 14:14 ("Lies in my name")</text>
  </g>

  <!-- Hallmark 2 -->
  <g filter="url(#shadow5)">
    <rect x="285" y="85" width="230" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="285" y="85" width="230" height="28" rx="8" fill="url(#dangerGrad)"/>
    <text x="400" y="104" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. CHEAP PEACE &amp; FLATTERY</text>
    <text x="297" y="132" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Preach what tickles itching ears</text>
    <text x="297" y="150" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Promise safety without repentance</text>
    <text x="297" y="185" fill="#fca5a5" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">Jeremiah 6:14 ("Peace when no peace")</text>
  </g>

  <!-- Hallmark 3 -->
  <g filter="url(#shadow5)">
    <rect x="540" y="85" width="225" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="540" y="85" width="225" height="28" rx="8" fill="url(#dangerGrad)"/>
    <text x="652" y="104" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. COMMODIFYING BLESSINGS</text>
    <text x="552" y="132" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Driven by money, fame &amp; status</text>
    <text x="552" y="150" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Charge fees for prayers / miracles</text>
    <text x="552" y="185" fill="#fca5a5" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">Micah 3:11 ("Prophets divine for money")</text>
  </g>

  <!-- Hallmark 4 -->
  <g filter="url(#shadow5)">
    <rect x="35" y="220" width="225" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="35" y="220" width="225" height="28" rx="8" fill="url(#dangerGrad)"/>
    <text x="147" y="239" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">4. SCRIPTURAL CONTRADICTION</text>
    <text x="47" y="267" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Distort orthodox doctrine</text>
    <text x="47" y="285" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Encourage idolatry and syncretism</text>
    <text x="47" y="320" fill="#fca5a5" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">Deuteronomy 13:1-3 (Luring to idols)</text>
  </g>

  <!-- Hallmark 5 -->
  <g filter="url(#shadow5)">
    <rect x="285" y="220" width="230" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="285" y="220" width="230" height="28" rx="8" fill="url(#dangerGrad)"/>
    <text x="400" y="239" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">5. MORALLY CORRUPT FRUIT</text>
    <text x="297" y="267" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Arrogance, greed &amp; immorality</text>
    <text x="297" y="285" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Wolves disguised in sheep's clothing</text>
    <text x="297" y="320" fill="#fca5a5" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">Matthew 7:15-20 ("By fruit you know them")</text>
  </g>

  <!-- Hallmark 6 -->
  <g filter="url(#shadow5)">
    <rect x="540" y="220" width="225" height="120" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="540" y="220" width="225" height="28" rx="8" fill="url(#dangerGrad)"/>
    <text x="652" y="239" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">6. FAILED PREDICTIONS</text>
    <text x="552" y="267" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Prophesy sensational events</text>
    <text x="552" y="285" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">• Words fail to pass in reality</text>
    <text x="552" y="320" fill="#fca5a5" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif">Deut 18:21-22 ("Presumptuous word")</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="35" y="360" width="730" height="60" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="385" fill="#fca5a5" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">JESUS' WARNING (Matthew 7:15)</text>
  <text x="400" y="405" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">"Watch out for false prophets. They come to you in sheep's clothing, but inwardly they are ferocious wolves."</text>
</svg>"""

# Lesson 6: 4-Point Discernment Radar for Today
SVG_LESSON_6 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="radarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d9488"/>
      <stop offset="100%" stop-color="#0f766e"/>
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad6)" rx="14"/>

  <text x="400" y="38" fill="#2dd4bf" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">THE DISCERNMENT RADAR FOR THE DIGITAL AGE</text>
  <text x="400" y="62" fill="#cbd5e1" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Evaluating Modern Preachers, Social Media Influencers, and Sensational Claims</text>

  <!-- 4 Step Sequential Process -->
  <!-- Step 1: Scriptural Consistency -->
  <g filter="url(#shadow6)">
    <rect x="30" y="85" width="165" height="240" rx="8" fill="#1e293b" stroke="#14b8a6" stroke-width="1.5"/>
    <rect x="30" y="85" width="165" height="34" rx="8" fill="url(#radarGrad)"/>
    <text x="112" y="107" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. SCRIPTURE</text>

    <circle cx="112" cy="145" r="18" fill="#134e4a"/>
    <text x="112" y="151" fill="#5eead4" font-size="14" text-anchor="middle">📖</text>

    <text x="112" y="180" fill="#2dd4bf" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Biblical Filter</text>
    <text x="40" y="205" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Does it align with the whole Bible?</text>
    <text x="40" y="235" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Are verses twisted out of context?</text>
    <text x="40" y="265" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Berean standard (Acts 17:11)</text>
  </g>

  <!-- Step 2: Character and Fruit -->
  <g filter="url(#shadow6)">
    <rect x="220" y="85" width="165" height="240" rx="8" fill="#1e293b" stroke="#14b8a6" stroke-width="1.5"/>
    <rect x="220" y="85" width="165" height="34" rx="8" fill="url(#radarGrad)"/>
    <text x="302" y="107" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. FRUIT CHECK</text>

    <circle cx="302" cy="145" r="18" fill="#134e4a"/>
    <text x="302" y="151" fill="#5eead4" font-size="14" text-anchor="middle">🍇</text>

    <text x="302" y="180" fill="#2dd4bf" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Lifestyle Audit</text>
    <text x="230" y="205" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Is their life marked by humility &amp; love?</text>
    <text x="230" y="235" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Are they obsessed with luxury &amp; cash?</text>
    <text x="230" y="265" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Galatians 5:22 fruit</text>
  </g>

  <!-- Step 3: Christ-Centricity -->
  <g filter="url(#shadow6)">
    <rect x="410" y="85" width="165" height="240" rx="8" fill="#1e293b" stroke="#14b8a6" stroke-width="1.5"/>
    <rect x="410" y="85" width="165" height="34" rx="8" fill="url(#radarGrad)"/>
    <text x="492" y="107" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. CHRIST FOCUS</text>

    <circle cx="492" cy="145" r="18" fill="#134e4a"/>
    <text x="492" y="151" fill="#5eead4" font-size="14" text-anchor="middle">✝️</text>

    <text x="492" y="180" fill="#2dd4bf" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Message Core</text>
    <text x="420" y="205" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Does it point to Jesus and the cross?</text>
    <text x="420" y="235" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Or to the speaker's ego and 'special powers'?</text>
    <text x="420" y="265" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• John 3:30 principle</text>
  </g>

  <!-- Step 4: Accountability & Oversight -->
  <g filter="url(#shadow6)">
    <rect x="600" y="85" width="165" height="240" rx="8" fill="#1e293b" stroke="#14b8a6" stroke-width="1.5"/>
    <rect x="600" y="85" width="165" height="34" rx="8" fill="url(#radarGrad)"/>
    <text x="682" y="107" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">4. OVERSIGHT</text>

    <circle cx="682" cy="145" r="18" fill="#134e4a"/>
    <text x="682" y="151" fill="#5eead4" font-size="14" text-anchor="middle">🛡️</text>

    <text x="682" y="180" fill="#2dd4bf" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Community Check</text>
    <text x="610" y="205" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Are they accountable to church elders?</text>
    <text x="610" y="235" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Do they refuse financial audits or law?</text>
    <text x="610" y="265" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Hebrews 13:17 order</text>
  </g>

  <!-- Bottom Guidance -->
  <rect x="30" y="345" width="735" height="75" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="370" fill="#2dd4bf" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">DIGITAL MEDIA RULE FOR CHRISTIAN YOUTH</text>
  <text x="400" y="390" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">Never send money to 'buy' blessings on mobile apps. Test every online teaching before sharing.</text>
  <text x="400" y="408" fill="#94a3b8" font-size="10" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">1 John 4:1 — "Dear friends, do not believe every spirit, but test the spirits to see whether they are from God."</text>
</svg>"""

# Lesson 7: Timeless Relevance of Prophecy to Modern Christians
SVG_LESSON_7 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="pillarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#4338ca"/>
    </linearGradient>
    <filter id="shadow7" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad7)" rx="14"/>

  <text x="400" y="38" fill="#818cf8" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">5 PILLARS OF PROPHETIC RELEVANCE TODAY</text>
  <text x="400" y="62" fill="#cbd5e1" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Why Ancient Prophetic Voices Matter in 21st Century Christian Ethics</text>

  <!-- 5 Pillars Flex Layout -->
  <!-- Pillar 1 -->
  <g filter="url(#shadow7)">
    <rect x="25" y="85" width="138" height="250" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="25" y="85" width="138" height="34" rx="8" fill="url(#pillarGrad)"/>
    <text x="94" y="106" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. GOD'S HEART</text>

    <circle cx="94" cy="140" r="16" fill="#312e81"/>
    <text x="94" y="145" fill="#a5b4fc" font-size="13" text-anchor="middle">👑</text>

    <text x="94" y="172" fill="#c7d2fe" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Holy Character</text>
    <text x="32" y="195" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">Reveals God's</text>
    <text x="32" y="210" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">unceasing holiness,</text>
    <text x="32" y="225" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">justice, mercy, and</text>
    <text x="32" y="240" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">covenant fidelity.</text>
  </g>

  <!-- Pillar 2 -->
  <g filter="url(#shadow7)">
    <rect x="178" y="85" width="138" height="250" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="178" y="85" width="138" height="34" rx="8" fill="url(#pillarGrad)"/>
    <text x="247" y="106" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. HISTORY LESSON</text>

    <circle cx="247" cy="140" r="16" fill="#312e81"/>
    <text x="247" y="145" fill="#a5b4fc" font-size="13" text-anchor="middle">📜</text>

    <text x="247" y="172" fill="#c7d2fe" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Warning from Past</text>
    <text x="185" y="195" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">Israel's exile shows</text>
    <text x="185" y="210" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">moral decline has</text>
    <text x="185" y="225" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">severe societal</text>
    <text x="185" y="240" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">consequences.</text>
  </g>

  <!-- Pillar 3 -->
  <g filter="url(#shadow7)">
    <rect x="331" y="85" width="138" height="250" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="331" y="85" width="138" height="34" rx="8" fill="url(#pillarGrad)"/>
    <text x="400" y="106" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. SOCIAL JUSTICE</text>

    <circle cx="400" cy="140" r="16" fill="#312e81"/>
    <text x="400" y="145" fill="#a5b4fc" font-size="13" text-anchor="middle">⚖️</text>

    <text x="400" y="172" fill="#c7d2fe" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Defending the Weak</text>
    <text x="338" y="195" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">Strong biblical</text>
    <text x="338" y="210" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">mandate to oppose</text>
    <text x="338" y="225" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">corruption, poverty</text>
    <text x="338" y="240" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">and exploitation.</text>
  </g>

  <!-- Pillar 4 -->
  <g filter="url(#shadow7)">
    <rect x="484" y="85" width="138" height="250" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="484" y="85" width="138" height="34" rx="8" fill="url(#pillarGrad)"/>
    <text x="553" y="106" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">4. CHRIST CLARITY</text>

    <circle cx="553" cy="140" r="16" fill="#312e81"/>
    <text x="553" y="145" fill="#a5b4fc" font-size="13" text-anchor="middle">✝️</text>

    <text x="553" y="172" fill="#c7d2fe" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Messianic Context</text>
    <text x="491" y="195" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">Foretold Christ's</text>
    <text x="491" y="210" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">incarnation,</text>
    <text x="491" y="225" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">atoning death, and</text>
    <text x="491" y="240" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">eternal kingdom.</text>
  </g>

  <!-- Pillar 5 -->
  <g filter="url(#shadow7)">
    <rect x="637" y="85" width="138" height="250" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="637" y="85" width="138" height="34" rx="8" fill="url(#pillarGrad)"/>
    <text x="706" y="106" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">5. GUARD IDOLATRY</text>

    <circle cx="706" cy="140" r="16" fill="#312e81"/>
    <text x="706" y="145" fill="#a5b4fc" font-size="13" text-anchor="middle">🛡️</text>

    <text x="706" y="172" fill="#c7d2fe" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Modern Idols</text>
    <text x="644" y="195" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">Guards against</text>
    <text x="644" y="210" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">modern Baalism:</text>
    <text x="644" y="225" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">materialism, vanity</text>
    <text x="644" y="240" fill="#cbd5e1" font-size="9" font-family="system-ui, sans-serif">and self-worship.</text>
  </g>

  <!-- Bottom Synthesis -->
  <rect x="25" y="350" width="750" height="75" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="375" fill="#a5b4fc" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2 TIMOTHY 3:16 — THE LIVING WORD</text>
  <text x="400" y="395" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">"All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness."</text>
  <text x="400" y="412" fill="#94a3b8" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">The Old Testament Prophets provide the moral blueprint for active Christian discipleship.</text>
</svg>"""

# =============================================================================
# TOPIC 1.8 DATA STRUCTURE: 7 LEARNING UNITS & PUBLISHED LESSONS
# =============================================================================

TOPIC_DATA = {
    "topic_order": 8,
    "topic_name": "Topic 1.8: The Old Testament Prophets",
    "topic_description": "Comprehensive exploration of Old Testament prophets, their categories, importance in Israel, Christological fulfillments, and biblical discernment frameworks against false prophets.",
    "units": [
        # ---------------------------------------------------------------------
        # UNIT 1: Understanding Prophets and Prophecy
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Understanding Prophets and Prophecy",
            "unit_description": "Define the terms prophet and prophecy biblically, and distinguish between forthtelling (proclamation) and foretelling (prediction).",
            "lesson_title": "Understanding Prophets and Prophecy",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Great_Isaiah_Scroll_-_Chapter_53.jpg/800px-Great_Isaiah_Scroll_-_Chapter_53.jpg",
            "image_caption": "The Great Isaiah Scroll discovered at Qumran (Dead Sea Scrolls), preserving ancient prophetic proclamations dating back to the 2nd century BCE.",
            "svg_content": SVG_LESSON_1,
            "youtube_id": "edllQ5H_cT0",
            "youtube_title": "The Prophets | BibleProject",
            "youtube_description": "Explore the role of biblical prophets as covenant guardians who called ancient Israel back to God's heart and revealed God's sovereign plans.",
            "pages": [
                # Card 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: The Great Isaiah Scroll",
                        "content": {
                            "title": "Visual Hook: Ancient Prophetic Scroll of Isaiah",
                            "caption": "The Great Isaiah Scroll discovered at Qumran (Dead Sea Scrolls), preserving ancient prophetic proclamations dating back to the 2nd century BCE."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Voice of God's Spokesperson",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define the Hebrew term **Nabi** and the biblical meaning of a prophet.",
                                "Distinguish between the primary role of **forthtelling** (proclamation) and **foretelling** (prediction).",
                                "Examine the divine calling of prophets in **Deuteronomy 18:18** and **Jeremiah 1:9**.",
                                "Analyze why prophetic messages challenged the political and social status quo."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: Who Were the Prophets?",
                        "content": {
                            "title": "The Divine Spokespersons (Nabi)",
                            "text": "In ancient Israel, a prophet was not a self-appointed religious professional or a psychic seeking profit. The primary Hebrew word for prophet is **Nabi** (נָבִיא), which literally means *'one who is called'* or *'an authorized spokesperson'*. \n\nProphets were chosen and commissioned directly by Yahweh to speak on His behalf. Their authority came solely from possessing the Word of the Lord. As recorded in **Jeremiah 1:9**: *'Then the Lord put forth His hand and touched my mouth, and the Lord said to me: Behold, I have put My words in your mouth.'*"
                        }
                    }
                ],
                # Card 2: Forthtelling vs Foretelling
                [
                    {
                        "type": "concept_explanation",
                        "title": "Core Concept: The Twin Dimensions of Prophecy",
                        "content": {
                            "title": "Forthtelling vs. Foretelling",
                            "text": "A widespread misconception is that biblical prophecy is solely about fortune-telling or predicting distant future events. In reality, prophetic ministry operated in two distinct dimensions:\n\n- **1. Forthtelling (Proclamation of Truth):** This comprised approximately 90% of prophetic speech. It involved proclaiming God's moral truth to the people in their current context—exposing social injustices, calling out corruption among leaders, demanding moral integrity, and urging immediate repentance.\n- **2. Foretelling (Predictive Revelation):** Comprising roughly 10% of prophetic messages, foretelling involved declaring future historical events ordained by God, such as impending judgment, exile, national restoration, and the future coming of the Messiah."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Definitions: Forthtelling & Foretelling",
                        "content": {
                            "title": "Prophetic Vocabulary Breakdown",
                            "definition": "The dual facets of biblical prophecy:",
                            "dimensions": [
                                "- **Forthtelling:** God's message for the **PRESENT** — addressing current sins, societal evils, and covenant obligations.",
                                "- **Foretelling:** God's message for the **FUTURE** — revealing divine interventions, judgment, and redemption."
                            ]
                        }
                    }
                ],
                # Card 3: Vector Blueprint (Dimensions)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The Twin Dimensions of Prophecy",
                        "content": {
                            "title": "Vector Blueprint: The Twin Dimensions of Prophecy",
                            "caption": "Infographic illustrating the prophet as God's spokesperson (Nabi) balancing forthtelling proclamation and foretelling prediction.",
                            "svg": SVG_LESSON_1
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Prophet as Covenant Prosecutor",
                        "content": {
                            "title": "Enforcing the Sinai Covenant",
                            "text": "The prophets functioned as 'divine covenant prosecutors'. When Israel forgot the Law given at Mount Sinai, God sent prophets to issue a formal covenant lawsuit (*rib* in Hebrew). \n\nThey warned the king, priests, and citizens that breaking the covenant would bring national calamity, but repentance would unlock divine mercy."
                        }
                    }
                ],
                # Card 4: Video Integration & Amos Case Study
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Prophets | BibleProject",
                        "content": {
                            "title": "The Prophets | BibleProject",
                            "description": "Discover how the Old Testament prophets challenged Israel's leaders and called the nation back to covenant faithfulness.",
                            "url": "https://www.youtube.com/watch?v=edllQ5H_cT0"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Case Study: Amos 5:24 in Context",
                        "content": {
                            "title": "Let Justice Roll Down Like Waters",
                            "text": "Consider the fiery words of Amos to the wealthy northern kingdom of Israel:\n\n> *'But let justice roll on like a river, righteousness like a never-failing stream!'* (Amos 5:24)\n\nThis is pure **forthtelling**. Amos was not predicting the weather; he was commanding the ruling class to stop oppressing the poor and to align their daily business practices with God's righteousness."
                        }
                    }
                ],
                # Card 5: Critical Thinking & Activity
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Critical Thinking: The Cost of Prophetic Speech",
                        "content": {
                            "title": "Why Were Prophets Often Persecuted?",
                            "scenario": "Because prophets engaged in 'forthtelling' that exposed greed, bribe-taking, and false worship, they were rarely popular with the wealthy ruling elites. Prophets like Jeremiah were thrown into muddy cisterns, and Elijah was hunted by King Ahab.",
                            "reflection_prompts": [
                                "Why is telling people the truth about their moral failures more dangerous than simply predicting abstract future events?",
                                "How can a modern student show 'prophetic courage' when peers engage in bullying or cheating?"
                            ]
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Biblical Prophet vs Ancient Diviner",
                        "content": {
                            "headers": ["Feature", "Biblical Prophet (Nabi)", "Pagan Diviner / Psychic"],
                            "rows": [
                                ["Calling", "Direct sovereign call from Yahweh", "Self-trained or hired for trade"],
                                ["Primary Task", "Calling nation to moral repentance", "Predicting personal fortunes for a fee"],
                                ["Motive", "God's glory and covenant fidelity", "Personal profit, prestige, and influence"],
                                ["Message Basis", "God's revealed Law and character", "Omens, astrology, and manipulation"]
                            ]
                        }
                    }
                ],
                # Card 6: Assessment & Mastery MCQ
                [
                    {
                        "type": "mcq_interactive",
                        "title": "Mastery Assessment: Role of an Old Testament Prophet",
                        "content": {
                            "question": "Which of the following statements most accurately captures the primary role of an Old Testament prophet?",
                            "options": [
                                "A military general who organized conquests against neighboring nations.",
                                "A fortune teller who charged money to reveal personal fortunes to kings.",
                                "A divine messenger and covenant guardian called to align the people's present behavior with God's Law.",
                                "A temple administrator in charge of animal sacrifice logistics."
                            ],
                            "correct_answer": "C",
                            "explanation": "Biblical prophets were covenant guardians whose primary mission was forthtelling—declaring God's moral will to their contemporary society and urging repentance."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lesson 1",
                        "content": {
                            "takeaways": [
                                "A prophet (*Nabi*) is an authorized spokesperson called and sent by God.",
                                "Forthtelling (proclaiming present moral truth) accounted for 90% of prophetic ministry.",
                                "Foretelling (predicting future events) revealed God's sovereignty and Messianic hope.",
                                "Prophets were guardians of the covenant who challenged social corruption."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # UNIT 2: Categories of Prophets in the Old Testament
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Categories of Prophets in the Old Testament",
            "unit_description": "Classify Old Testament prophets into Major, Minor, and Non-Writing categories based on literary scope and ministry mode.",
            "lesson_title": "Categories of Prophets in the Old Testament",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Michelangelo_Buonarroti_030.jpg/800px-Michelangelo_Buonarroti_030.jpg",
            "image_caption": "Michelangelo's fresco of the Prophet Isaiah on the Sistine Chapel ceiling, symbolizing the profound literary and theological legacy of the Major Prophets.",
            "svg_content": SVG_LESSON_2,
            "youtube_id": "DNCi5YkXgKk",
            "youtube_title": "Old Testament Overview: The Prophets | BibleProject",
            "youtube_description": "Learn the structure of the prophetic books in the Old Testament canon, from the expansive Major Prophets to the Book of the Twelve Minor Prophets.",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Michelangelo's Prophet Isaiah",
                        "content": {
                            "title": "Visual Hook: The Prophet Isaiah",
                            "caption": "Michelangelo's fresco of the Prophet Isaiah on the Sistine Chapel ceiling, symbolizing the profound literary and theological legacy of the Major Prophets."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Classifying the Prophetic Canon",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Categorize Old Testament prophets into **Major Prophets**, **Minor Prophets**, and **Non-Writing Prophets**.",
                                "Debunk the misconception that 'Major' implies greater spiritual importance than 'Minor'.",
                                "Identify key figures in each category and understand their historical contexts.",
                                "Explain how scroll length and literary structure determined biblical classification."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Diversity of Prophetic Voices",
                        "content": {
                            "title": "How the Prophetic Books Are Organized",
                            "text": "The Old Testament contains a rich tapestry of prophetic ministries spanning hundreds of years. To study them systematically, biblical scholars organize them into three distinct categories based on literary form, scroll length, and historical transmission:\n\n- **1. Major Writing Prophets**\n- **2. Minor Writing Prophets (The Twelve)**\n- **3. Non-Writing (Oral / Historical) Prophets**"
                        }
                    }
                ],
                # Card 2: Major vs Minor Prophets
                [
                    {
                        "type": "concept_explanation",
                        "title": "Major vs. Minor: A Question of Scroll Length",
                        "content": {
                            "title": "Understanding the Literary Classification",
                            "text": "A common mistake among students is assuming that 'Major Prophets' were more spiritually gifted or held higher authority than 'Minor Prophets'. This is false.\n\n- **Major Prophets:** Designated 'major' solely because of the **length and breadth of their written scrolls**. They authored large books covering expansive theological themes and geopolitical destinies. The four major writing prophets are **Isaiah** (66 chapters), **Jeremiah** (+ Lamentations), **Ezekiel** (48 chapters), and **Daniel** (12 chapters).\n- **Minor Prophets:** Known collectively in the Hebrew canon as the *Book of the Twelve* because all twelve short books could fit onto a single standard papyrus scroll. They include: **Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, and Malachi**."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Crucial Distinction: Scope vs Spiritual Value",
                        "content": {
                            "title": "Scroll Length Classification",
                            "definition": "The distinction between Major and Minor prophets:",
                            "dimensions": [
                                "- **Major Prophets:** Long scrolls with wide international horizons.",
                                "- **Minor Prophets:** Concise scrolls addressing specific crises with equal divine inspiration.",
                                "- **Spiritual Value:** Identical. Every true prophet spoke the infallible Word of the Lord."
                            ]
                        }
                    }
                ],
                # Card 3: Non-Writing Prophets
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Non-Writing (Oral / Court) Prophets",
                        "content": {
                            "title": "Prophets of Action in Kings and Samuel",
                            "text": "Not every prophet authored a book carrying their name. Many of the most powerful prophets in Israel's history were **Non-Writing Prophets** whose public actions, state confrontations, and miracles were documented by biblical historians in 1 & 2 Samuel, 1 & 2 Kings, and Chronicles.\n\nKey examples include:\n- **Samuel:** Transition figure who anointed Israel's first two kings, Saul and David.\n- **Nathan:** Royal court prophet who courageously rebuked King David over Bathsheba and Uriah.\n- **Elijah:** Fierce prophet who confronted King Ahab and defeated 450 prophets of Baal on Mount Carmel.\n- **Elisha:** Elijah's successor who performed numerous miracles and advised Israel's military leaders."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Taxonomy of Old Testament Prophets",
                        "content": {
                            "title": "Vector Blueprint: Taxonomy of Old Testament Prophets",
                            "caption": "Taxonomy matrix classifying Old Testament prophets into Major, Minor, and Non-Writing categories.",
                            "svg": SVG_LESSON_2
                        }
                    }
                ],
                # Card 4: Video & Structural Overview
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: Old Testament Overview: The Prophets",
                        "content": {
                            "title": "Old Testament Overview: The Prophets | BibleProject",
                            "description": "Understand the literary architecture of the Hebrew prophetic collection and how each book contributes to salvation history.",
                            "url": "https://www.youtube.com/watch?v=DNCi5YkXgKk"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master Summary Table: The 3 Prophetic Categories",
                        "content": {
                            "headers": ["Category", "Prophetic Figures / Books", "Primary Distinction", "Focus & Setting"],
                            "rows": [
                                ["Major Prophets", "Isaiah, Jeremiah, Ezekiel, Daniel", "Very long scrolls with multi-era international vision", "Israel, Judah, and world empires during Assyrian & Babylonian exiles"],
                                ["Minor Prophets", "Hosea through Malachi (12 books)", "Shorter scrolls addressing focused themes", "Local populations confronting immediate social injustice and apostasy"],
                                ["Non-Writing", "Samuel, Nathan, Elijah, Elisha, Ahijah", "Authored no books; ministry recorded by historians", "Direct monarchical confrontations in royal courts and public showdowns"]
                            ]
                        }
                    }
                ],
                # Card 5: Interactive Sorting Activity
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Classroom Activity: Prophetic Sorting Jigsaw",
                        "content": {
                            "title": "Categorize the Prophetic Figures",
                            "scenario": "Imagine organizing an ancient library of Hebrew scrolls. You must sort these 9 figures into their proper shelves: Nathan, Hosea, Isaiah, Micah, Samuel, Daniel, Haggai, Elisha, Jeremiah.",
                            "reflection_prompts": [
                                "Major Shelf: Isaiah, Jeremiah, Daniel",
                                "Minor Shelf: Hosea, Micah, Haggai",
                                "Non-Writing Shelf: Nathan, Samuel, Elisha",
                                "Why did God raise up both literary authors and direct court confronters?"
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Ministry Context of the Non-Writing Prophets",
                        "content": {
                            "title": "Direct Checks on Monarchical Power",
                            "text": "In ancient Near Eastern empires, kings ruled as absolute despots with unquestioned power. In Israel, however, God placed the non-writing prophets directly inside or adjacent to the royal court to ensure the king remembered he was merely a servant of the true King, Yahweh."
                        }
                    }
                ],
                # Card 6: Assessment & Mastery MCQ
                [
                    {
                        "type": "mcq_interactive",
                        "title": "Mastery Assessment: Literary Classification of Prophets",
                        "content": {
                            "question": "Why are the books of Hosea, Amos, and Micah categorized as 'Minor Prophets' in the biblical canon?",
                            "options": [
                                "Because they performed fewer miracles than Isaiah and Jeremiah.",
                                "Because their theological authority is lower than that of the Major Prophets.",
                                "Because their written scrolls are shorter in length compared to the Major Prophets.",
                                "Because they ministered after the New Testament period."
                            ],
                            "correct_answer": "C",
                            "explanation": "The term 'Minor' refers strictly to the length of the written scroll, not to the prophet's importance or divine authority."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lesson 2",
                        "content": {
                            "takeaways": [
                                "Major Prophets (Isaiah, Jeremiah, Ezekiel, Daniel) wrote expansive, lengthy scrolls.",
                                "Minor Prophets (The Twelve) wrote concise books of equal theological inspiration.",
                                "Non-Writing Prophets (Samuel, Nathan, Elijah, Elisha) operated through direct oral confrontation.",
                                "Classification reflects literary scope, never spiritual hierarchy."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # UNIT 3: Importance of Prophets in Israel
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Importance of Prophets in Israel",
            "unit_description": "Outline the key functions of prophets in Israel's history as covenant keepers, ethical advocates, and advisers.",
            "lesson_title": "Importance of Prophets in Israel",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Elijah_and_Ahab_by_Arthur_Murch.jpg/800px-Elijah_and_Ahab_by_Arthur_Murch.jpg",
            "image_caption": "Arthur Murch's depiction of the Prophet Elijah confronting King Ahab in Naboth's vineyard, demonstrating the prophet's fearless defense of divine justice.",
            "svg_content": SVG_LESSON_3,
            "youtube_id": "cI8_Fm3Y_eU",
            "youtube_title": "The Book of Amos | BibleProject",
            "youtube_description": "See how Amos exposed religious hypocrisy and demanded social justice for the vulnerable in ancient Israel.",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Elijah Confronting Ahab",
                        "content": {
                            "title": "Visual Hook: Prophet Elijah Rebuking King Ahab",
                            "caption": "Arthur Murch's depiction of the Prophet Elijah confronting King Ahab in Naboth's vineyard, demonstrating the prophet's fearless defense of divine justice."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Indispensable Role of Prophets",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Examine the 5 essential roles played by prophets in the history of Israel.",
                                "Analyze how prophets acted as the **moral conscience** and **covenant guardians** of the nation.",
                                "Evaluate prophetic advocacy for **social justice** and defense of the vulnerable.",
                                "Understand the scriptural foundation in **2 Kings 17:13** and **Amos 3:7**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: Israel's Moral Anchor",
                        "content": {
                            "title": "What if Israel Had No Prophets?",
                            "text": "Ancient Israel was constantly prone to spiritual amnesia and syncretism—adopting the brutal, immoral practices of surrounding pagan nations. The priesthood was frequently compromised by political ties, and monarchs easily abused their absolute power.\n\nIn this fragile society, God raised up prophets to serve as the nation's **moral conscience** and unyielding guardians of covenant law (2 Kings 17:13)."
                        }
                    }
                ],
                # Card 2: The 5 Multifaceted Roles
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Vital Functions of Prophets in Israel",
                        "content": {
                            "title": "How Prophets Shaped Israel's Destiny",
                            "text": "The prophetic ministry in Israel fulfilled five critical functions:\n\n- **1. God's Direct Spokespersons:** Delivering divine decrees, warnings, and calls to repentance, ensuring the nation never lost touch with Yahweh's living voice.\n- **2. Guardians of the Sinaitic Covenant:** Reminding leaders and citizens of their sacred promises at Mount Sinai and warning that persistent idolatry would lead to exile.\n- **3. Champions of Social Justice:** Boldly denouncing the exploitation of widows, orphans, and the poor, and exposing dishonest merchants and corrupt judges.\n- **4. Moral Advisers and Rebukers of Kings:** Confronting monarchs (like Nathan confronting David and Elijah confronting Ahab) to ensure human rulers remained submissive to God's law.\n- **5. Harbingers of Messianic Hope:** Comforting brokenhearted people during disaster and exile by revealing God's future promises of mercy, restoration, and the Messiah."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Definition: Covenant Guardian",
                        "content": {
                            "title": "The Covenant Prosecutor",
                            "definition": "A prophet whose mission was to call a backsliding nation back to the terms of the Mount Sinai covenant, warning of judgment while extending God's invitation to grace."
                        }
                    }
                ],
                # Card 3: Vector Blueprint & Social Justice
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The Multi-Faceted Roles of Israel's Prophets",
                        "content": {
                            "title": "Vector Blueprint: The Multi-Faceted Roles of Israel's Prophets",
                            "caption": "Diagram mapping the 4 core pillars of prophetic ministry anchored in the Sinaitic Covenant.",
                            "svg": SVG_LESSON_3
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Prophets as Voices for the Voiceless",
                        "content": {
                            "title": "The Heart of Biblical Social Justice",
                            "text": "Prophets like Amos and Micah did not separate spiritual worship from ethical living. They taught that offering thousands of sacrifices while exploiting workers or cheating the vulnerable was repulsive to God (Isaiah 1:11-17).\n\nTrue worship of Yahweh demanded economic fairness, honest weights and balances, and proactive defense of widows, orphans, and resident foreigners."
                        }
                    }
                ],
                # Card 4: Video Integration & Amos Case Study
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Book of Amos | BibleProject",
                        "content": {
                            "title": "The Book of Amos | BibleProject",
                            "description": "Watch how the shepherd-prophet Amos confronted the wealthy elite of Samaria over their neglect of social justice.",
                            "url": "https://www.youtube.com/watch?v=cI8_Fm3Y_eU"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Historic Flashpoints of Prophetic Ministry",
                        "content": {
                            "title": "Three Historic Confontations",
                            "text": "Consider how individual prophets exercised their calling:\n\n- **Nathan to David (2 Samuel 12):** *'You are the man!'* Nathan fearlessly exposed King David's adultery with Bathsheba and the orchestrated murder of Uriah.\n- **Elijah to Ahab (1 Kings 21):** Rebuking Ahab and Jezebel for the judicial murder of Naboth to steal his ancestral vineyard.\n- **Amos to Israel (Amos 8:4-6):** Condemning merchants who could not wait for the Sabbath to end so they could skim the grain measure and use dishonest scales."
                        }
                    }
                ],
                # Card 5: Ethical Dilemma & Application
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Ethical Application: Modern Prophetic Courage",
                        "content": {
                            "title": "Confronting Injustice in Peer Circles",
                            "scenario": "A popular group in school begins spreading humiliating rumors online about a quiet classmate from an underprivileged background. Most students laugh or stay silent to protect their own social status.",
                            "reflection_prompts": [
                                "What would 'prophetic courage' look like in this high school situation?",
                                "How does remaining silent make an individual complicit in the injustice?",
                                "What personal risks did Old Testament prophets take when speaking truth to power?"
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Prophet's Burden: Costly Obedience",
                        "content": {
                            "title": "Speaking Truth Regardless of Cost",
                            "text": "Old Testament prophets were not armchair critics. They suffered physical abuse, imprisonment, and social ostracization. Yet their loyalty to God's covenant compelled them to speak without compromise."
                        }
                    }
                ],
                # Card 6: Assessment & Mastery MCQ
                [
                    {
                        "type": "mcq_interactive",
                        "title": "Mastery Assessment: Role of a Covenant Guardian",
                        "content": {
                            "question": "Which of the following actions best illustrates an Old Testament prophet fulfilling the role of a 'Covenant Guardian' in Israel?",
                            "options": [
                                "Building luxurious summer palaces for the king's royal family.",
                                "Calling the nation back to the moral commandments of Mount Sinai and warning of judgment for apostasy.",
                                "Introducing Canaanite religious ceremonies to modernize Israelite worship.",
                                "Collecting foreign customs duties from international trade caravans."
                            ],
                            "correct_answer": "B",
                            "explanation": "As guardians of the covenant, prophets constantly realigned the nation's spiritual and ethical lifestyle with the Sinaitic Law."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lesson 3",
                        "content": {
                            "takeaways": [
                                "Prophets were God's spokespersons and Israel's moral conscience.",
                                "They guarded the Sinai Covenant against idolatry and syncretism.",
                                "They championed social justice, defending widows, orphans, and the poor.",
                                "They advised and rebuked kings, ensuring human authority stayed accountable to God."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # UNIT 4: Relationship Between Old and New Testament Prophecies
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Relationship Between Old and New Testament Prophecies",
            "unit_description": "Tracing the theological continuity between Old Testament prophetic expectations and New Testament fulfillments in Jesus Christ.",
            "lesson_title": "Relationship Between Old and New Testament Prophecies",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Duccio_di_Buoninsegna_-_Annunciation_-_WGA06740.jpg/800px-Duccio_di_Buoninsegna_-_Annunciation_-_WGA06740.jpg",
            "image_caption": "Duccio's 'Annunciation' depicting the fulfillment of Isaiah 7:14, connecting ancient Messianic prophecy to the New Testament Incarnation.",
            "svg_content": SVG_LESSON_4,
            "youtube_id": "7_CGP-12AE0",
            "youtube_title": "Messiah | BibleProject",
            "youtube_description": "Discover how the Old Testament promises of a royal deliverer and suffering servant find their ultimate fulfillment in Jesus of Nazareth.",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Duccio's Annunciation",
                        "content": {
                            "title": "Visual Hook: The Annunciation & Prophetic Fulfillment",
                            "caption": "Duccio's 'Annunciation' depicting the fulfillment of Isaiah 7:14, connecting ancient Messianic prophecy to the New Testament Incarnation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Grand Arc of Prophetic Fulfillment",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Understand the theological continuity between the Old and New Testaments.",
                                "Distinguish between **Direct Prophetic Fulfillment** and **Typological Foreshadowing**.",
                                "Analyze key Messianic prophecies in Isaiah, Micah, and Jeremiah fulfilled in Jesus Christ.",
                                "Examine Luke 24:27 and Matthew 5:17 as foundational hermeneutical anchors."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: Christianity as the Climax of Prophecy",
                        "content": {
                            "title": "One Seamless Story of Redemption",
                            "text": "The New Testament writers did not present Jesus Christ as the founder of an unrelated religion. Rather, they saw Jesus as the planned climax and fulfillment of Israel's ancient prophetic Scriptures.\n\nOn the road to Emmaus, Jesus demonstrated this principle: *'And beginning with Moses and all the Prophets, He explained to them what was said in all the Scriptures concerning Himself'* (Luke 24:27)."
                        }
                    }
                ],
                # Card 2: Direct Fulfillment vs Typology
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two Primary Channels of Prophetic Continuity",
                        "content": {
                            "title": "Direct Predictions and Typological Shadows",
                            "text": "Old Testament prophecies relate to the New Testament in two profound ways:\n\n- **1. Direct Messianic Prophecies:** Specific, explicit predictions made by Old Testament prophets regarding the Messiah's lineage, birth, ministry, suffering, death, and resurrection that were precisely fulfilled in the historical life of Jesus.\n- **2. Typology (Sacred Shadows):** Historical persons, institutions, events, or rituals in the Old Testament that served as divinely designed patterns or foreshadows of the higher spiritual realities realized in Jesus Christ (Hebrews 10:1)."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Definition: Biblical Typology",
                        "content": {
                            "title": "Understanding Typology",
                            "definition": "The study of Old Testament symbols, events, or persons (types) that prefigure and find their ultimate spiritual fulfillment (antitype) in Jesus Christ in the New Testament."
                        }
                    }
                ],
                # Card 3: Key Messianic Prophecies Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Messianic Fulfillment Matrix: OT Promise to NT Reality",
                        "content": {
                            "headers": ["Prophetic Promise", "Old Testament Passage", "New Testament Fulfillment", "Theological Reality"],
                            "rows": [
                                ["Virgin Birth", "Isaiah 7:14", "Matthew 1:18-25", "Incarnation: God dwelling with humanity"],
                                ["Birthplace: Bethlehem", "Micah 5:2", "Matthew 2:1-6", "Davidic lineage and royal heritage"],
                                ["Mission of Liberation", "Isaiah 61:1-2", "Luke 4:18-21", "Compassionate Kingdom proclamation"],
                                ["Suffering Servant", "Isaiah 53:3-7", "1 Peter 2:24 / Mark 15", "Substitutionary Atonement on the cross"],
                                ["The Righteous Branch", "Jeremiah 23:5-6", "Luke 1:32-33", "Eternal, righteous Davidic reign"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Old Testament Prophecy & NT Fulfillment",
                        "content": {
                            "title": "Vector Blueprint: Old Testament Prophecy & NT Fulfillment",
                            "caption": "Comparative infographic illustrating direct prophecies and typological fulfillments in Jesus Christ.",
                            "svg": SVG_LESSON_4
                        }
                    }
                ],
                # Card 4: Video Integration & Typological Case Studies
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: Messiah | BibleProject",
                        "content": {
                            "title": "Messiah | BibleProject",
                            "description": "Trace the biblical theme of the promised King who delivers humanity from the curse of sin through sacrifice.",
                            "url": "https://www.youtube.com/watch?v=7_CGP-12AE0"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Mastering Typology: 3 Classical Examples",
                        "content": {
                            "title": "Old Testament Types Fulfilled in Christ",
                            "text": "Notice how ancient Old Testament institutions prefigured Christ:\n\n- **1. The Passover Lamb (Exodus 12):** The blood of an unblemished lamb saved Israel's firstborn from death. Fulfilled when Jesus, the true Lamb of God, shed His spotless blood to deliver believers from eternal death (1 Corinthians 5:7).\n- **2. The High Priest (Levitical Order):** The Levitical priest mediated between God and sinful humans with animal blood. Fulfilled in Jesus, our supreme and perfect High Priest who entered heaven itself with His own blood (Hebrews 4:14-16).\n- **3. Jonah in the Great Fish (Jonah 1:17):** Jonah's three days in darkness prefigured Jesus' three days in the tomb followed by His triumphant resurrection (Matthew 12:40)."
                        }
                    }
                ],
                # Card 5: Interactive Knowledge Check
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Interactive True / False Challenge",
                        "content": {
                            "title": "Testing Prophetic Continuity",
                            "scenario": "Evaluate these statements based on Lesson 4:",
                            "reflection_prompts": [
                                "Statement 1: 'Jesus came to abolish the Old Testament and discard all ancient prophecies.' (False: Matthew 5:17 affirms He came to fulfill them).",
                                "Statement 2: 'Typology is when an ancient event, person, or ritual acts as a shadow of a greater New Testament reality.' (True).",
                                "Statement 3: 'Micah 5:2 predicted that the Messiah would be born in the city of Jerusalem.' (False: It explicitly specified Bethlehem Ephrathah)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Prophetic Fulfillment Matters to Modern Faith",
                        "content": {
                            "title": "Evidence of God's Sovereign Plan",
                            "text": "The precise fulfillment of prophecies written centuries apart by different authors across multiple cultures proves that the Bible is not a random collection of human opinions, but the inspired, sovereign Word of God."
                        }
                    }
                ],
                # Card 6: Assessment & Mastery MCQ
                [
                    {
                        "type": "mcq_interactive",
                        "title": "Mastery Assessment: Typological Fulfillment",
                        "content": {
                            "question": "How does the New Testament presentation of the 'Passover Lamb' relate to Old Testament prophecy?",
                            "options": [
                                "It was a literal animal that Jesus and the disciples had to sacrifice every Sabbath.",
                                "It serves as a typological shadow prefiguring Jesus Christ's sacrifice which delivers humanity from the penalty of sin.",
                                "It was an ancient Egyptian cultural custom that had no theological meaning for Israel.",
                                "It showed that Jesus came to completely abolish the historical Exodus narrative."
                            ],
                            "correct_answer": "B",
                            "explanation": "The Passover lamb is a prime example of biblical typology, where an ancient historical ritual foreshadows Jesus Christ's ultimate redemptive sacrifice."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lesson 4",
                        "content": {
                            "takeaways": [
                                "The New Testament fulfills the promises and patterns of the Old Testament.",
                                "Direct prophecies accurately predicted Christ's birth, lineage, ministry, and cross.",
                                "Typological shadows (Passover lamb, High Priest, Jonah) prefigured Christ's salvation.",
                                "Christological fulfillment demonstrates the sovereign unity of God's redemptive plan."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # UNIT 5: Characteristics of False Prophets
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Characteristics of False Prophets",
            "unit_description": "Expose the behavioral, spiritual, and moral hallmarks of false prophets using Old and New Testament warning criteria.",
            "lesson_title": "Characteristics of False Prophets",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Jeremiah_and_Hananiah_in_the_temple.jpg/800px-Jeremiah_and_Hananiah_in_the_temple.jpg",
            "image_caption": "Historical illustration of the temple clash between the true prophet Jeremiah and the false prophet Hananiah (Jeremiah 28), showing the tension between popular lies and painful divine truth.",
            "svg_content": SVG_LESSON_5,
            "youtube_id": "PkyU2rE6u5E",
            "youtube_title": "The Book of Jeremiah | BibleProject",
            "youtube_description": "Witness Jeremiah's heartbreaking struggle against the corrupt false prophets of Jerusalem who preached false peace.",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Jeremiah Confronting Hananiah",
                        "content": {
                            "title": "Visual Hook: The Clash of Prophets in the Temple",
                            "caption": "Historical illustration of the temple clash between the true prophet Jeremiah and the false prophet Hananiah (Jeremiah 28), showing the tension between popular lies and painful divine truth."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Exposing the Wolf's Marks",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Identify the 6 core biblical characteristics of false prophets.",
                                "Analyze why false prophets were popular while true prophets were persecuted.",
                                "Examine key warning passages in **Deuteronomy 18**, **Jeremiah 14**, and **Matthew 7**.",
                                "Compare the motivations of true prophets vs. self-interested deceivers."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Hazard of Deception",
                        "content": {
                            "title": "Why Did False Prophets Flourish?",
                            "text": "False prophets were an enduring plague in Israel's history. While true prophets like Jeremiah endured arrest, mockery, and dungeon imprisonment for preaching hard truths, false prophets were celebrated in royal courts and markets.\n\nWhy? Because false prophets told people exactly what their flesh wanted to hear: continuous peace, effortless prosperity, and zero need for moral repentance."
                        }
                    }
                ],
                # Card 2: The 6 Hallmarks of False Prophets
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 6 Biblical Marks of False Prophets",
                        "content": {
                            "title": "Diagnostic Framework from Scripture",
                            "text": "Scripture provides definitive diagnostic tests to identify false prophets:\n\n- **1. Self-Originating Messages (Jeremiah 14:14):** They claim God spoke to them, but their 'visions' and 'dreams' are fabricated products of their own human imagination.\n- **2. Preaching Cheap Peace and Flattery (Jeremiah 6:14, 5:31):** They promise unbroken blessings and luxury without demanding repentance, moral discipline, or justice.\n- **3. Driven by Commercial Greed (Micah 3:11):** They commodify the faith—demanding cash payments, tithes, or gifts before dispensing 'prophetic words' and blessings.\n- **4. Contradicting Written Scripture (Deuteronomy 13:1-3):** They preach ideas that distort established biblical doctrine and lead believers into idolatry or worldly compromise.\n- **5. Rotten Moral Character (Matthew 7:15-20):** In private life, they exhibit arrogance, sexual immorality, manipulation, and pride ('wolves in sheep's clothing').\n- **6. Failed Predictive Accuracy (Deuteronomy 18:21-22):** Their sensational future predictions fail to materialize in historical reality."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Warning: Ferocious Wolves",
                        "content": {
                            "title": "Matthew 7:15 Warning",
                            "definition": "Jesus warned: 'Watch out for false prophets. They come to you in sheep's clothing, but inwardly they are ferocious wolves.' Their outward religious charisma masks predatory self-interest."
                        }
                    }
                ],
                # Card 3: Vector Blueprint (Anatomy)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The Anatomy of False Prophets",
                        "content": {
                            "title": "Vector Blueprint: The Anatomy of False Prophets",
                            "caption": "Six-part diagnostic matrix outlining the biblical hallmarks and warning criteria against false prophets.",
                            "svg": SVG_LESSON_5
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Case Study: Jeremiah vs. Hananiah (Jeremiah 28)",
                        "content": {
                            "title": "Sweet Lies vs. Painful Truth",
                            "text": "When King Nebuchadnezzar threatened Jerusalem, the false prophet Hananiah took a wooden yoke from Jeremiah's neck, broke it, and declared: *'Within two years, God will break Babylon's yoke!'* The crowd cheered.\n\nJeremiah responded with God's truth: God was placing an iron yoke on the nation due to unrepentant sin. Within months, Hananiah died as God had spoken, and Babylon conquered Jerusalem."
                        }
                    }
                ],
                # Card 4: Video Integration & Commercialization
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Book of Jeremiah | BibleProject",
                        "content": {
                            "title": "The Book of Jeremiah | BibleProject",
                            "description": "Explore Jeremiah's struggle to warn Judah about judgment while false prophets comforted the people with lies.",
                            "url": "https://www.youtube.com/watch?v=PkyU2rE6u5E"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Side-by-Side Comparison: True vs False Prophets",
                        "content": {
                            "headers": ["Characteristic", "True Biblical Prophet", "False Prophet"],
                            "rows": [
                                ["Message Source", "Direct revelation from Yahweh", "Human imagination & wishful thinking"],
                                ["Core Theme", "Call to repentance, holiness & justice", "Guaranteed peace, wealth & flatteries"],
                                ["Financial Stance", "Refused payments; suffered poverty", "Divined for money, prestige & gifts"],
                                ["Audience Reaction", "Often rejected, mocked & persecuted", "Popular, praised & court-favored"],
                                ["Lifestyle & Fruit", "Integrity, humility & godly character", "Greed, moral laxity & manipulation"]
                            ]
                        }
                    }
                ],
                # Card 5: Interactive Sorting Activity
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Interactive Activity: True Prophet (T) vs False Prophet (F)",
                        "content": {
                            "title": "Diagnostic Sorting Challenge",
                            "scenario": "Evaluate each prophetic scenario and classify as True (T) or False (F):",
                            "reflection_prompts": [
                                "1. Delivers God's warning even when it leads to arrest and unpopularity. -> [True Prophet]",
                                "2. Demands a fixed financial fee before praying for a sick family member. -> [False Prophet]",
                                "3. Preaches that God does not care about private sexual morality as long as you attend church. -> [False Prophet]",
                                "4. Rebukes corrupt judges for accepting bribes and defending the rich. -> [True Prophet]"
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Danger of Emotional Exploitation",
                        "content": {
                            "title": "Preying on Human Fear and Grief",
                            "text": "False prophets frequently target people during crises (illness, financial strain, death). By claiming to hold the exclusive 'cure' or 'blessing', they manipulate vulnerable individuals into parting with their life savings."
                        }
                    }
                ],
                # Card 6: Assessment & Mastery MCQ
                [
                    {
                        "type": "mcq_interactive",
                        "title": "Mastery Assessment: Biblical Check for True Prophecy",
                        "content": {
                            "question": "According to Deuteronomy 18:21-22, what is one of the definitive biblical tests to determine if a predictive prophecy came from the Lord?",
                            "options": [
                                "The prophet is supported and funded by the reigning king.",
                                "The prophet performs dazzling magic tricks on stage.",
                                "The prediction comes to pass accurately in historical reality.",
                                "The message is praised by all the popular political commentators."
                            ],
                            "correct_answer": "C",
                            "explanation": "Deuteronomy 18:21-22 states that if a prophet speaks in the name of the Lord and the thing does not happen, it is a word the Lord has not spoken."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lesson 5",
                        "content": {
                            "takeaways": [
                                "False prophets invent messages from their own imagination (Jeremiah 14:14).",
                                "They preach flattery and peace without repentance to gain popularity.",
                                "They exploit the faith for financial gain and prestige (Micah 3:11).",
                                "True prophets are known by their godly character, scriptural fidelity, and verified words."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # UNIT 6: Discerning False Prophets Today
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Discerning False Prophets Today",
            "unit_description": "Apply biblical evaluation tools and media literacy skills to identify and avoid contemporary false prophets and sensational religious movements.",
            "lesson_title": "Discerning False Prophets Today",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Spurgeon_metropolitan_tabernacle.jpg/800px-Spurgeon_metropolitan_tabernacle.jpg",
            "image_caption": "Charles Spurgeon preaching in London; Spurgeon famously warned that discernment is not knowing the difference between right and wrong, but knowing the difference between right and almost right.",
            "svg_content": SVG_LESSON_6,
            "youtube_id": "PbcJ5XF7j8w",
            "youtube_title": "The Book of 1 Timothy | BibleProject",
            "youtube_description": "Learn how Paul instructed Timothy to confront false teachers and maintain sound doctrine, godly character, and church accountability.",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Spurgeon Preaching on Discernment",
                        "content": {
                            "title": "Visual Hook: Standing for Sound Doctrine",
                            "caption": "Charles Spurgeon preaching in London; Spurgeon famously warned that discernment is not knowing the difference between right and wrong, but knowing the difference between right and almost right."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Spiritual and Digital Discernment",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Apply the **4-Point Discernment Radar** to evaluate modern religious claims.",
                                "Develop critical media literacy against deceptive online preachers on TikTok, YouTube, and TV.",
                                "Examine the Berean standard of testing all teaching against written Scripture (Acts 17:11).",
                                "Understand the necessity of church community accountability and ethical financial oversight."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: False Prophecy in the Digital Age",
                        "content": {
                            "title": "Deception in the Palm of Your Hand",
                            "text": "In the ancient world, false prophets operated in town squares and temples. Today, digital algorithms, viral TikTok videos, televangelism broadcasts, and social media platforms deliver deceptive religious messages directly into teenagers' bedrooms.\n\nModern Christians require sharp spiritual and media discernment to avoid falling prey to sensationalism, fear-mongering, and financial scams (1 Timothy 4:1-2)."
                        }
                    }
                ],
                # Card 2: The 4-Point Discernment Radar
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4-Point Discernment Radar",
                        "content": {
                            "title": "How to Test Every Spiritual Message",
                            "text": "To protect against modern deception, every believer should run religious messages through four biblical filters:\n\n- **1. The Scripture Filter (Acts 17:11):** Like the noble Bereans, examine the whole Bible to see if the preacher's claims match orthodox Scripture, or if single verses are being isolated and twisted.\n- **2. The Fruit and Lifestyle Audit (Matthew 7:16-20):** Examine how the leader lives when cameras are off. Do they exhibit the fruit of the Spirit (Galatians 5:22-23)—humility, self-control, and honesty—or luxurious greed and autocratic pride?\n- **3. The Christ-Centricity Check (John 3:30):** Does the message point people to Jesus Christ, the cross, and holy living? Or does it glorify the speaker's 'anointing', special powers, and prophetic titles?\n- **4. The Community Accountability Test (Hebrews 13:17):** Does the ministry submit to church elders, financial audits, and national laws? Or does the leader operate as an untouchable 'lone ranger' who refuses external oversight?"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Principle: The Berean Standard",
                        "content": {
                            "title": "Acts 17:11",
                            "definition": "The Bereans were praised because 'they received the message with great eagerness and examined the Scriptures every day to see if what Paul said was true.' Even the Apostle Paul was evaluated against the written Word."
                        }
                    }
                ],
                # Card 3: Vector Blueprint (Radar)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The Discernment Radar for the Digital Age",
                        "content": {
                            "title": "Vector Blueprint: The Discernment Radar for the Digital Age",
                            "caption": "Four-quadrant discernment framework showing Scripture, Fruit, Christ-Centricity, and Oversight filters.",
                            "svg": SVG_LESSON_6
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sensationalism and Fear-Mongering",
                        "content": {
                            "title": "How Modern Scammers Create Panic",
                            "text": "A primary weapon of contemporary false prophets is manufactured panic—predicting specific doomsday dates, claiming 'generational curses' on your family, or declaring that failure in exams is due to demonic hexes that only their 'miracle oil' or a financial 'seed' can break.\n\nBiblical faith rejects emotional extortion and rests peacefully in Christ's sovereign finished work on the cross."
                        }
                    }
                ],
                # Card 4: Video Integration & Real World Case
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Book of 1 Timothy | BibleProject",
                        "content": {
                            "title": "The Book of 1 Timothy | BibleProject",
                            "description": "Discover Paul's practical guidance to young Timothy on identifying greedy teachers and cultivating sound doctrine.",
                            "url": "https://www.youtube.com/watch?v=PbcJ5XF7j8w"
                        }
                    },
                    {
                        "type": "interactive_scenario",
                        "title": "Real-World Case Study: The Viral Seed Trap",
                        "content": {
                            "title": "Analyzing an Online Video Claim",
                            "scenario": "A viral video on social media shows a preacher with 500,000 followers declaring: 'There is a curse of academic failure over your family! Send 3,000 Shillings immediately to this mobile money number to receive a prophetic breakthrough before your final national exams!'",
                            "reflection_prompts": [
                                "1. Which hallmarks of a false prophet are active in this video? (Financial greed, manipulating fear, self-originating claims).",
                                "2. What is the biblical path to academic success? (Diligent study, personal responsibility, integrity, and prayerful trust in God's grace).",
                                "3. How can you advise a friend who is about to send their pocket money to this preacher?"
                            ]
                        }
                    }
                ],
                # Card 5: Practical Action Protocol
                [
                    {
                        "type": "comparison_table",
                        "title": "Digital Safety Guidelines for Christian Youth",
                        "content": {
                            "headers": ["Scenario", "Dangerous Response", "Biblical Discernment Response"],
                            "rows": [
                                ["Preacher predicts exact world end date", "Panic, sell schoolbooks, donate money", "Recognize that Jesus said no one knows the day or hour (Matt 24:36); stay calm"],
                                ["Influencer sells 'anointed water/oil' for exam success", "Buy the product hoping for a shortcut", "Reject commercialized items; study hard and trust God (Colossians 3:23)"],
                                ["Preacher insults and curses critics", "Accept that they are 'untouchable'", "Remember Christ commanded love and humility; test fruit (1 John 4:1)"],
                                ["Ministry refuses financial accounting", "Keep donating blindly", "Demand biblical stewardship and accountability (2 Corinthians 8:20-21)"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Safeguard of Local Church Community",
                        "content": {
                            "title": "Why You Need a Local Church",
                            "text": "Isolated individuals browsing the internet alone are the most vulnerable to deception. God designed the local church—with mature pastors, teachers, and elders—to serve as a protective spiritual family that guards believers against cunning deceit (Ephesians 4:11-14)."
                        }
                    }
                ],
                # Card 6: Assessment & Mastery MCQ
                [
                    {
                        "type": "mcq_interactive",
                        "title": "Mastery Assessment: Responding to Online Sensationalism",
                        "content": {
                            "question": "A self-proclaimed media prophet on YouTube predicts an exact date for the end of the world and demands viewers sell their property and send money to his account. How should a discerning Christian respond?",
                            "options": [
                                "Sell all school materials immediately because the world is ending anyway.",
                                "Send half of the family savings just in case his prediction turns out to be true.",
                                "Remain calm, reject the fear-mongering, and recognize that his demands contradict biblical stewardship, Matthew 24:36, and church accountability.",
                                "Stop attending school and wait in isolation on a mountain."
                            ],
                            "correct_answer": "C",
                            "explanation": "Biblical discernment rejects sensational predictions of dates (Matthew 24:36) and identifies financial extortion as the hallmark of a false prophet."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lesson 6",
                        "content": {
                            "takeaways": [
                                "Modern false prophecy proliferates rapidly through digital media and sensational claims.",
                                "The 4-Point Discernment Radar checks Scripture, Fruit, Christ-Centricity, and Accountability.",
                                "The Berean standard requires testing all preaching against the written Word of God.",
                                "Local church community and biblical literacy provide impenetrable shields against deception."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # UNIT 7: Relevance of Prophecy to Christians Today
        # ---------------------------------------------------------------------
        {
            "unit_order": 7,
            "unit_name": "Relevance of Prophecy to Christians Today",
            "unit_description": "Synthesize the teachings of the prophets and evaluate how ancient prophetic messages apply to modern ethical decisions, community development, and personal faith.",
            "lesson_title": "Relevance of Prophecy to Christians Today",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Wailing_wall_1920.jpg/800px-Wailing_wall_1920.jpg",
            "image_caption": "The Western Wall in Jerusalem, a living monument to biblical history, exile, and prophetic restoration, reminding modern believers of God's unchanging covenant faithfulness.",
            "svg_content": SVG_LESSON_7,
            "youtube_id": "MFEUEcxKmww",
            "youtube_title": "Micah | BibleProject",
            "youtube_description": "Discover Micah's timeless prophetic summary: 'To act justly and to love mercy and to walk humbly with your God' (Micah 6:8).",
            "pages": [
                # Card 1: Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: The Western Wall in Jerusalem",
                        "content": {
                            "title": "Visual Hook: Ancient History and Timeless Truth",
                            "caption": "The Western Wall in Jerusalem, a living monument to biblical history, exile, and prophetic restoration, reminding modern believers of God's unchanging covenant faithfulness."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Living Prophetic Legacy",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Synthesize the 5 primary pillars of prophetic relevance for 21st-century Christians.",
                                "Apply ancient prophetic principles of **justice, mercy, and humility** (Micah 6:8) to modern community ethics.",
                                "Identify modern subtle idols (materialism, vanity, power) through the lens of ancient anti-Baal polemics.",
                                "Examine Hebrews 1:1-2 and 2 Timothy 3:16 as scriptural anchors for ongoing relevance."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: Why Read Ancient Prophets Today?",
                        "content": {
                            "title": "Why Does an Ancient Voice Matter to a Modern Teenager?",
                            "text": "Some people assume that because Jesus has already inaugurated the New Covenant, the Old Testament prophetic books are obsolete relics of an ancient past.\n\nYet as **Hebrews 1:1-2** and **2 Timothy 3:16** affirm, the prophetic writings remain living, God-breathed Scripture. Their passionate calls for holiness, integrity, and social justice provide the essential moral backbone for Christian discipleship today."
                        }
                    }
                ],
                # Card 2: The 5 Pillars of Relevance
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Pillars of Enduring Prophetic Relevance",
                        "content": {
                            "title": "What the Prophets Teach 21st Century Believers",
                            "text": "Old Testament prophecies hold timeless value in five key areas:\n\n- **1. Revealing the Unchanging Character of God:** The prophets demonstrate that God is not an indifferent bystander. He is passionately committed to justice, holiness, covenant faithfulness, and the defense of the vulnerable.\n- **2. Learning from History:** The national failures, exile, and restoration of Israel show that moral compromise carries severe systemic consequences, while genuine repentance releases divine mercy.\n- **3. Ethical Foundation for Social Justice:** The prophets provide our strongest biblical vocabulary for fighting institutional corruption, defending the poor, and championing ethical business practices.\n- **4. Illuminating the Identity and Mission of Jesus:** We cannot fully grasp Jesus' identity as Messiah, King of kings, and Suffering Servant without understanding the prophetic blueprint He fulfilled.\n- **5. Warning Against Modern Idolatry:** The prophets' relentless battle against ancient Baal worship warns us to guard our hearts against modern, subtle idols—consumerism, greed, digital vanity, and self-worship."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Verse: Micah 6:8",
                        "content": {
                            "title": "The Prophetic Blueprint",
                            "definition": "'He has shown you, O mortal, what is good. And what does the Lord require of you? To act justly and to love mercy and to walk humbly with your God.' The ultimate summary of prophetic ethics."
                        }
                    }
                ],
                # Card 3: Vector Blueprint (5 Pillars)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: 5 Pillars of Prophetic Relevance Today",
                        "content": {
                            "title": "Vector Blueprint: 5 Pillars of Prophetic Relevance Today",
                            "caption": "Pillar-based architecture demonstrating how ancient prophetic teachings anchor contemporary Christian life.",
                            "svg": SVG_LESSON_7
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Confronting 21st Century Baalism",
                        "content": {
                            "title": "Modern Idols in Ancient Garb",
                            "text": "Ancient Baalism promised agricultural prosperity and sexual gratification in exchange for religious ritual. \n\nToday, modern idolatry operates under new names: unrestrained consumerism, career obsession at the expense of family and integrity, and social media addiction. The prophetic call to exclusive loyalty to Yahweh remains urgently relevant."
                        }
                    }
                ],
                # Card 4: Video Integration & Classroom Debate
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: Micah | BibleProject",
                        "content": {
                            "title": "Micah | BibleProject",
                            "description": "Explore how the prophet Micah's warning against corrupt leaders and vision of messianic peace speaks directly to today's society.",
                            "url": "https://www.youtube.com/watch?v=MFEUEcxKmww"
                        }
                    },
                    {
                        "type": "interactive_scenario",
                        "title": "Classroom Debate: The Relevance of Prophecy",
                        "content": {
                            "title": "Debating Old Testament Relevance",
                            "scenario": "Group A argues that Christians only need the Gospels and Epistles because Jesus completed everything. Group B argues that without the Old Testament prophets, Christians lose their biblical mandate for social justice and moral courage.",
                            "reflection_prompts": [
                                "How does Amos 5:24 bridge both arguments, showing that ethical justice is a perpetual requirement?",
                                "How did Jesus Himself quote the prophets in His inaugural sermon in Luke 4:18-21?",
                                "What happens to a church's social impact when it ignores prophetic teachings on economic fairness?"
                            ]
                        }
                    }
                ],
                # Card 5: Practical Application Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Prophetic Principles Applied to Contemporary Youth Life",
                        "content": {
                            "headers": ["Prophetic Principle", "Ancient Application", "21st Century Student Application"],
                            "rows": [
                                ["Honest Weights (Amos 8:5)", "Fair grain scales in the marketplace", "Refusing exam cheating, plagiarism, and digital fraud"],
                                ["Defending Widows (Isa 1:17)", "Legal protection in ancient city gates", "Standing up for bullied, orphaned, or disabled classmates"],
                                ["Rejecting Idolatry (Elijah)", "Destroying physical Baal altars", "Resisting digital addictions, materialism, and vanity"],
                                ["Walking Humbly (Micah 6:8)", "Rejecting royal arrogance", "Using academic, athletic, and musical talents to serve others"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Living as Modern Prophetic Witnesses",
                        "content": {
                            "title": "Being Salt and Light",
                            "text": "To be a 'prophetic voice' today does not mean predicting the future; it means having the courage to speak up for truth, act with unwavering honesty in school, and live out God's sacrificial love in our neighborhoods."
                        }
                    }
                ],
                # Card 6: Assessment & Topic Mastery MCQ
                [
                    {
                        "type": "mcq_interactive",
                        "title": "Mastery Assessment: Interpreting Prophecy Today",
                        "content": {
                            "question": "How should a modern Christian interpret and apply the teachings of the Old Testament prophets?",
                            "options": [
                                "By using their judgment imagery to scare peers into attending religious meetings.",
                                "By treating every prophecy as an automatic, literal prediction of current geopolitical headlines.",
                                "By extracting their timeless ethical principles—such as justice, repentance, and loyalty to God—to guide modern moral choices.",
                                "By ignoring them completely because the Old Covenant is no longer in effect."
                            ],
                            "correct_answer": "C",
                            "explanation": "While specific historical prophecies addressed ancient settings, the underlying revelation of God's character, justice, and covenant ethics remains fully active and authoritative for Christian living."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lesson 7 & Topic 1.8 Synthesis",
                        "content": {
                            "takeaways": [
                                "The prophets reveal God's unchanging heart for justice, holiness, and mercy.",
                                "Ancient warnings against compromise help us identify modern subtle idols.",
                                "Prophetic literature provides the indispensable foundation for Christian social ethics.",
                                "Micah 6:8 calls every believer to act justly, love mercy, and walk humbly with God."
                            ]
                        }
                    }
                ]
            ]
        }
    ]
}

# =============================================================================
# INGESTION ENGINE
# =============================================================================

def ingest_grade10_cre_topic_1_8(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 CRE — Topic 1.8: The Old Testament Prophets")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade & Subject
        grade = Grade.objects.filter(id=5).first()
        if not grade:
            grade = Grade.objects.filter(curriculum_id=5, level=10).first()
        if not grade:
            raise RuntimeError("Grade 10 (Curriculum CBC, ID 5) not found!")

        subject = Subject.objects.filter(id=46).first()
        if not subject:
            subject = Subject.objects.filter(grade=grade, name__icontains="CRE").first()
        if not subject:
            raise RuntimeError("Subject CRE (ID 46) not found!")

        print(f"Verified Context: Grade='{grade.name}' (ID: {grade.id}), Subject='{subject.name}' (ID: {subject.id})")

        # 2. Resolve Topic 1.8
        topic_order = TOPIC_DATA["topic_order"]
        topic_name = TOPIC_DATA["topic_name"]
        topic_desc = TOPIC_DATA["topic_description"]

        topic, t_created = Topic.objects.get_or_create(
            subject=subject,
            order=topic_order,
            defaults={
                "name": topic_name,
                "description": topic_desc
            }
        )
        if not t_created:
            topic.name = topic_name
            topic.description = topic_desc
            topic.save()

        print(f"Target Topic: '{topic.name}' (ID: {topic.id}, Order: {topic.order})")

        # If replacing, clear existing learning units & lessons for clean idempotent ingestion
        if replace:
            existing_units = LearningUnit.objects.filter(topic=topic)
            for u in existing_units:
                for l in u.lessons.all():
                    l.blocks.all().delete()
                    l.assets.all().delete()
                    l.delete()
                u.delete()
            print("  -> Cleared previous learning units, lessons, blocks, and assets for clean rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 3. Ingest Each Learning Unit & Lesson
        for u_data in TOPIC_DATA["units"]:
            u_order = u_data["unit_order"]
            u_name = u_data["unit_name"]
            u_desc = u_data["unit_description"]
            l_title = u_data["lesson_title"]
            pages = u_data["pages"]

            # Create Learning Unit
            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={
                    "name": u_name,
                    "description": u_desc
                }
            )
            unit.name = u_name
            unit.description = u_desc
            unit.save()
            total_units += 1

            # Create Published Lesson (Version 1)
            lesson, _ = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": l_title,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "author": "VLearn Grade 10 CRE Topic 1.8 Ingestion Agent",
                        "curriculum": "CBC",
                        "grade_id": grade.id,
                        "subject_id": subject.id,
                        "topic_order": topic_order,
                        "unit_order": u_order
                    }
                }
            )
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()
            total_lessons += 1

            # Clear any leftover blocks / assets
            lesson.blocks.all().delete()
            lesson.assets.all().delete()

            # Create LessonAsset 1: Authentic Photographic Wikimedia Hook
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                title=f"Visual Hook: {l_title}",
                url=u_data["image_url"],
                metadata={
                    "caption": u_data["image_caption"],
                    "source": "Wikimedia Commons",
                    "verified": True
                }
            )
            total_assets += 1

            # Create LessonAsset 2: Pedagogical Responsive Vector SVG Diagram
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                title=f"Vector Blueprint: {l_title}",
                metadata={
                    "svg_content": u_data["svg_content"],
                    "responsive": True,
                    "viewBox": "0 0 800 450"
                }
            )
            total_assets += 1

            # Create LessonAsset 3: Curated Educational YouTube Video
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                title=u_data["youtube_title"],
                url=f"https://www.youtube.com/watch?v={u_data['youtube_id']}",
                metadata={
                    "youtube_id": u_data["youtube_id"],
                    "description": u_data["youtube_description"]
                }
            )
            total_assets += 1

            # Ingest Progressive Pages & LessonBlocks
            block_order_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, b_def in enumerate(page_blocks, start=1):
                    b_type = b_def["type"]
                    b_title = clean_text(b_def.get("title", ""))
                    b_content = clean_dict(b_def.get("content", {}))

                    # Inject resolved media assets into block content
                    if b_type == "suggested_image":
                        b_content["url"] = u_data["image_url"]
                        b_content["resolved_image_url"] = u_data["image_url"]
                        b_content["source"] = "Wikimedia Commons"
                    elif b_type == "suggested_diagram":
                        b_content["svg"] = u_data["svg_content"]
                        b_content["svg_xml"] = u_data["svg_content"]
                    elif b_type == "suggested_video":
                        b_content["url"] = f"https://www.youtube.com/watch?v={u_data['youtube_id']}"
                        b_content["youtube_id"] = u_data["youtube_id"]

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t1_8_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_order_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={
                            "topic_order": topic_order,
                            "unit_order": u_order,
                            "page_index": page_idx
                        }
                    )

                    # Explicitly link LessonAsset records to their corresponding LessonBlocks
                    if b_type == "suggested_image":
                        block.assets.add(img_asset)
                    elif b_type == "suggested_diagram":
                        block.assets.add(svg_asset)
                    elif b_type == "suggested_video":
                        block.assets.add(yt_asset)

                    block_order_counter += 1
                    total_blocks += 1

            print(f"  -> Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Cards, {block_order_counter - 1} Blocks, 3 Linked Assets)")

        print("=" * 80)
        print("INGESTION COMPLETED SUCCESSFULLY!")
        print(f"  Target Topic: {topic.name} (ID: {topic.id})")
        print(f"  Learning Units Created: {total_units}")
        print(f"  Published Lessons Created: {total_lessons}")
        print(f"  Total Lesson Pages (Cards): {total_pages}")
        print(f"  Total Lesson Blocks: {total_blocks}")
        print(f"  Total Lesson Assets: {total_assets}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--no-replace" not in sys.argv
    ingest_grade10_cre_topic_1_8(replace=replace_flag)
