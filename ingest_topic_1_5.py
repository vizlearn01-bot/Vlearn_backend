"""
VLearn CBC Grade 10 CRE — Topic 1.5: The Exodus
Production Ingestion Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5)
Subject: CRE (ID: 46)
Topic: Topic 1.5: The Exodus (Topic Order: 5)

Decomposed into 6 Learning Units & 6 Published Lessons (each with 6 progressive cards, 12 blocks, 3 linked assets):
  1. The Call and Vocation of Moses (Exodus 3:1-22) (6 Cards, 12 Blocks)
  2. The Divine-Human Discourse: Objections and Reassurances (Exodus 4:1-19) (6 Cards, 12 Blocks)
  3. The Ten Plagues and the Defeat of Egyptian Deities (Exodus 7:14 - 11:10) (6 Cards, 12 Blocks)
  4. Divine Attributes Revealed in the Plagues (6 Cards, 12 Blocks)
  5. The Passover and Foreshadowing of Christ's Atonement (Exodus 12:1-31) (6 Cards, 12 Blocks)
  6. God's Miraculous Care in the Wilderness and True Liberation (Exodus 14-17) (6 Cards, 12 Blocks)
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

def clean_text(text: str) -> str:
    """Removes bracket citations and internal metadata markers."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [1.5], [223], [1.3, 1.1]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags e.g. [VISUAL: ...], [BIBLE PASSAGE: ...], [VALUES], etc.
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|MCQ: HIGH)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

# Lesson 1: Call of Moses & Burning Bush
SVG_LESSON_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="bushFireGrad" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="50%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#fef08a"/>
    </linearGradient>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="glow1" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad1)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="40" fill="#f8fafc" font-size="21" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Anatomy of a Divine Call: Moses at Mount Horeb</text>
  <text x="400" y="64" fill="#94a3b8" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Theophany, Divine Sovereignty, and the Vocation to Deliver Israel (Exodus 3:1-22)</text>

  <!-- Central Bush Theophany Icon -->
  <g transform="translate(350, 95)" filter="url(#glow1)">
    <!-- Bush Silhouette -->
    <path d="M 50 110 Q 30 70 10 75 Q 35 50 25 25 Q 50 40 50 10 Q 55 40 75 25 Q 65 50 90 75 Q 70 70 50 110 Z" fill="url(#bushFireGrad)"/>
    <path d="M 50 110 L 50 70 M 50 90 L 30 75 M 50 85 L 70 70" stroke="#78350f" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="132" fill="#fef08a" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Unconsumed Bush</text>
  </g>

  <!-- Left Box: The Human Context (Shepherd in Midian) -->
  <g filter="url(#shadow1)">
    <rect x="35" y="95" width="280" height="230" rx="10" fill="url(#cardGrad1)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="35" y="95" width="280" height="34" rx="10" fill="#0284c7"/>
    <text x="175" y="118" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. Human Fragility &amp; Exile</text>
    
    <text x="50" y="155" fill="#38bdf8" font-size="12" font-weight="700" font-family="system-ui, sans-serif">From Pharaoh's Palace to Desert:</text>
    <text x="50" y="176" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">• 40 years as a humble Midianite shepherd</text>
    <text x="50" y="196" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">• Stripped of royal pride and self-reliance</text>
    <text x="50" y="216" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">• Learning patience, guidance &amp; vigilance</text>
    <text x="50" y="242" fill="#94a3b8" font-size="10.5" font-style="italic" font-family="system-ui, sans-serif">"Moses led the flock to Horeb, the mountain of God."</text>
    
    <rect x="50" y="265" width="250" height="42" rx="6" fill="#0f172a"/>
    <text x="175" y="283" fill="#e0f2fe" font-size="10" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Key Value: Humility &amp; Preparation</text>
    <text x="175" y="297" fill="#7dd3fc" font-size="9.5" font-family="system-ui, sans-serif" text-anchor="middle">God trains deliverers in quiet obscurity</text>
  </g>

  <!-- Right Box: The Divine Revelation & Commission -->
  <g filter="url(#shadow1)">
    <rect x="485" y="95" width="280" height="230" rx="10" fill="url(#cardGrad1)" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="485" y="95" width="280" height="34" rx="10" fill="#d97706"/>
    <text x="625" y="118" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. The Divine Commission</text>
    
    <text x="500" y="155" fill="#fbbf24" font-size="12" font-weight="700" font-family="system-ui, sans-serif">God's Initiative &amp; Covenant Name:</text>
    <text x="500" y="176" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">• "I have seen the misery of My people"</text>
    <text x="500" y="196" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">• Divine Holy Ground: "Take off your sandals"</text>
    <text x="500" y="216" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">• Self-Revelation: "I AM WHO I AM" (Ex 3:14)</text>
    <text x="500" y="242" fill="#94a3b8" font-size="10.5" font-style="italic" font-family="system-ui, sans-serif">"So now, go. I am sending you to Pharaoh."</text>
    
    <rect x="500" y="265" width="250" height="42" rx="6" fill="#0f172a"/>
    <text x="625" y="283" fill="#fef3c7" font-size="10" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Key Value: Reverence &amp; Holy Trust</text>
    <text x="625" y="297" fill="#fcd34d" font-size="9.5" font-family="system-ui, sans-serif" text-anchor="middle">God hears the oppressed and initiates salvation</text>
  </g>

  <!-- Bottom Pathway Banner -->
  <rect x="35" y="348" width="730" height="75" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="55" y="372" fill="#38bdf8" font-size="12" font-weight="700" font-family="system-ui, sans-serif">THEOLOGICAL PRINCIPLE: VOCATION IS GOD-CENTERED</text>
  <text x="55" y="392" fill="#cbd5e1" font-size="11" font-family="system-ui, sans-serif">God does not call the qualified; He qualifies the called. Deliverance is entirely Yahweh's covenant work executed through obedient human instruments.</text>
  <text x="55" y="410" fill="#94a3b8" font-size="10.5" font-style="italic" font-family="system-ui, sans-serif">Covenant Reference: Genesis 15:13-14 fulfilled in Exodus 3:7-10.</text>
</svg>"""

# Lesson 2: Five Objections & Divine Answers
SVG_LESSON_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad2)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Divine Dialogue: Moses' 5 Objections &amp; God's Answers</text>
  <text x="400" y="60" fill="#94a3b8" font-size="12.5" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Exodus 3:11 - 4:17: From Human Reluctance to Divine Empowerment</text>

  <!-- Objections Table Grid -->
  <!-- Header Row -->
  <rect x="30" y="78" width="740" height="32" rx="6" fill="#334155"/>
  <text x="50" y="99" fill="#94a3b8" font-size="11" font-weight="700" font-family="system-ui, sans-serif">NO.</text>
  <text x="140" y="99" fill="#f87171" font-size="11" font-weight="700" font-family="system-ui, sans-serif">MOSES' EXCUSE / OBJECTION</text>
  <text x="460" y="99" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif">GOD'S REASSURING PROVISION</text>

  <!-- Row 1 -->
  <g filter="url(#shadow2)">
    <rect x="30" y="116" width="740" height="52" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <circle cx="58" cy="142" r="14" fill="#38bdf8"/>
    <text x="58" y="147" fill="#0f172a" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="90" y="136" fill="#fca5a5" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Inadequacy: "Who am I that I should go?" (3:11)</text>
    <text x="90" y="154" fill="#94a3b8" font-size="10.5" font-family="system-ui, sans-serif">Focus on personal insignificance and unworthiness</text>
    <text x="430" y="136" fill="#6ee7b7" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Divine Presence: "I will be with you" (3:12)</text>
    <text x="430" y="154" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">The focus shifts from Moses' identity to God's presence</text>
  </g>

  <!-- Row 2 -->
  <g filter="url(#shadow2)">
    <rect x="30" y="174" width="740" height="52" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <circle cx="58" cy="200" r="14" fill="#38bdf8"/>
    <text x="58" y="205" fill="#0f172a" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="90" y="194" fill="#fca5a5" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Authority: "What is His name? What shall I say?" (3:13)</text>
    <text x="90" y="212" fill="#94a3b8" font-size="10.5" font-family="system-ui, sans-serif">Lack of theological standing before Israel</text>
    <text x="430" y="194" fill="#6ee7b7" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Self-Revelation: "I AM WHO I AM" (3:14)</text>
    <text x="430" y="212" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">The eternal, self-existent Covenant Lord of Patriarchs</text>
  </g>

  <!-- Row 3 -->
  <g filter="url(#shadow2)">
    <rect x="30" y="232" width="740" height="52" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <circle cx="58" cy="258" r="14" fill="#38bdf8"/>
    <text x="58" y="263" fill="#0f172a" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="90" y="252" fill="#fca5a5" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Credibility: "They will not believe me or listen" (4:1)</text>
    <text x="90" y="270" fill="#94a3b8" font-size="10.5" font-family="system-ui, sans-serif">Fear of skepticism and public rejection</text>
    <text x="430" y="252" fill="#6ee7b7" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">3 Signs of Power: Staff, Leprous Hand, Water (4:2-9)</text>
    <text x="430" y="270" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">Miracles demonstrating sovereignty over Pharaoh &amp; nature</text>
  </g>

  <!-- Row 4 -->
  <g filter="url(#shadow2)">
    <rect x="30" y="290" width="740" height="52" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <circle cx="58" cy="316" r="14" fill="#38bdf8"/>
    <text x="58" y="321" fill="#0f172a" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="90" y="310" fill="#fca5a5" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Eloquence: "I am slow of speech and tongue" (4:10)</text>
    <text x="90" y="328" fill="#94a3b8" font-size="10.5" font-family="system-ui, sans-serif">Inability to deliver eloquent royal speeches</text>
    <text x="430" y="310" fill="#6ee7b7" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Creator's Power: "Who made human mouths?" (4:11)</text>
    <text x="430" y="328" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">God promises divine inspiration: "I will teach you"</text>
  </g>

  <!-- Row 5 -->
  <g filter="url(#shadow2)">
    <rect x="30" y="348" width="740" height="52" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <circle cx="58" cy="374" r="14" fill="#38bdf8"/>
    <text x="58" y="379" fill="#0f172a" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">5</text>
    <text x="90" y="368" fill="#fca5a5" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Rejection: "Please send someone else!" (4:13)</text>
    <text x="90" y="386" fill="#94a3b8" font-size="10.5" font-family="system-ui, sans-serif">Direct reluctance to accept the commission</text>
    <text x="430" y="368" fill="#6ee7b7" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif">Shared Leadership: Aaron appointed spokesman (4:14)</text>
    <text x="430" y="386" fill="#cbd5e1" font-size="10.5" font-family="system-ui, sans-serif">God accommodates weakness while maintaining His mission</text>
  </g>

  <!-- Footer Insight -->
  <text x="400" y="430" fill="#94a3b8" font-size="11" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Key Takeaway: God equips those He calls and overcomes every human limitation through His grace.</text>
</svg>"""

# Lesson 3: The 10 Plagues and Egyptian Deities
SVG_LESSON_3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="plagueHeader" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad3)" rx="12"/>

  <!-- Title & Header -->
  <rect x="30" y="15" width="740" height="48" rx="8" fill="url(#plagueHeader)"/>
  <text x="400" y="36" fill="#ffffff" font-size="18" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">THE TEN PLAGUES: DIVINE POLEMIC AGAINST EGYPTIAN GODS</text>
  <text x="400" y="54" fill="#fecaca" font-size="11.5" font-family="system-ui, sans-serif" text-anchor="middle">"On all the gods of Egypt I will execute judgments: I am the LORD." — Exodus 12:12</text>

  <!-- 3-Column Cycle Breakdown -->
  <!-- Column 1: Plagues 1 to 4 -->
  <g transform="translate(30, 75)">
    <rect width="235" height="280" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <rect width="235" height="26" rx="8" fill="#334155"/>
    <text x="117" y="18" fill="#38bdf8" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">CYCLE 1: WATER &amp; INSECTS</text>
    
    <text x="12" y="46" fill="#f87171" font-size="11" font-weight="700">1. Nile to Blood</text>
    <text x="12" y="60" fill="#94a3b8" font-size="9.5">Target: Hapi &amp; Osiris (Nile life)</text>
    
    <text x="12" y="86" fill="#f87171" font-size="11" font-weight="700">2. Frogs</text>
    <text x="12" y="100" fill="#94a3b8" font-size="9.5">Target: Heqet (Goddess of fertility)</text>
    
    <text x="12" y="126" fill="#f87171" font-size="11" font-weight="700">3. Gnats / Lice</text>
    <text x="12" y="140" fill="#94a3b8" font-size="9.5">Target: Geb (Earth god) • Finger of God</text>
    
    <text x="12" y="166" fill="#f87171" font-size="11" font-weight="700">4. Flies / Swarms</text>
    <text x="12" y="180" fill="#94a3b8" font-size="9.5">Target: Khepri • Goshen spared!</text>

    <rect x="10" y="205" width="215" height="60" rx="6" fill="#0f172a"/>
    <text x="117" y="224" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Magicians' Limit</text>
    <text x="117" y="240" fill="#cbd5e1" font-size="9" text-anchor="middle">Court sorcerers fail at Plague 3:</text>
    <text x="117" y="254" fill="#fef08a" font-size="9" font-style="italic" text-anchor="middle">"This is the finger of God!"</text>
  </g>

  <!-- Column 2: Plagues 5 to 8 -->
  <g transform="translate(282, 75)">
    <rect width="235" height="280" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <rect width="235" height="26" rx="8" fill="#334155"/>
    <text x="117" y="18" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">CYCLE 2: DISEASE &amp; NATURE</text>
    
    <text x="12" y="46" fill="#fbbf24" font-size="11" font-weight="700">5. Death of Livestock</text>
    <text x="12" y="60" fill="#94a3b8" font-size="9.5">Target: Apis (Bull) &amp; Hathor (Cow)</text>
    
    <text x="12" y="86" fill="#fbbf24" font-size="11" font-weight="700">6. Boils on Flesh</text>
    <text x="12" y="100" fill="#94a3b8" font-size="9.5">Target: Sekhmet &amp; Imhotep (Healing)</text>
    
    <text x="12" y="126" fill="#fbbf24" font-size="11" font-weight="700">7. Hail &amp; Fire</text>
    <text x="12" y="140" fill="#94a3b8" font-size="9.5">Target: Nut (Sky) &amp; Osiris (Crops)</text>
    
    <text x="12" y="180" fill="#94a3b8" font-size="9.5">Target: Serapis &amp; Isis (Harvest protect)</text>
    <text x="12" y="166" fill="#fbbf24" font-size="11" font-weight="700">8. Locusts</text>

    <rect x="10" y="205" width="215" height="60" rx="6" fill="#0f172a"/>
    <text x="117" y="224" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">Goshen's Distinction</text>
    <text x="117" y="240" fill="#cbd5e1" font-size="9" text-anchor="middle">God sets a clear division between</text>
    <text x="117" y="254" fill="#6ee7b7" font-size="9" font-weight="600" text-anchor="middle">His people and the oppressors.</text>
  </g>

  <!-- Column 3: Plagues 9 & 10 (Climax) -->
  <g transform="translate(535, 75)">
    <rect width="235" height="280" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="235" height="26" rx="8" fill="#991b1b"/>
    <text x="117" y="18" fill="#ffffff" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">CYCLE 3: CLIMACTIC JUDGMENT</text>
    
    <text x="12" y="52" fill="#ef4444" font-size="12" font-weight="800">9. Total Darkness</text>
    <text x="12" y="68" fill="#94a3b8" font-size="10">Target: Ra / Amun-Ra (Sun god)</text>
    <text x="12" y="84" fill="#cbd5e1" font-size="9.5">3 days of palpable blackout across Egypt</text>
    
    <line x1="12" y1="100" x2="223" y2="100" stroke="#334155" stroke-width="1"/>

    <text x="12" y="122" fill="#f87171" font-size="12" font-weight="800">10. Death of Firstborn</text>
    <text x="12" y="138" fill="#94a3b8" font-size="10">Target: Pharaoh &amp; Heirs (Living god)</text>
    <text x="12" y="154" fill="#cbd5e1" font-size="9.5">Shatters royal dynasty and power</text>

    <rect x="10" y="180" width="215" height="85" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="117" y="202" fill="#f87171" font-size="10.5" font-weight="700" text-anchor="middle">Passover Deliverance</text>
    <text x="117" y="220" fill="#cbd5e1" font-size="9" text-anchor="middle">The Blood of the unblemished Lamb</text>
    <text x="117" y="236" fill="#cbd5e1" font-size="9" text-anchor="middle">shields Israel from the Angel of Death.</text>
    <text x="117" y="252" fill="#34d399" font-size="9" font-weight="600" text-anchor="middle">Israel marches out in freedom!</text>
  </g>

  <!-- Bottom Summary Banner -->
  <rect x="30" y="370" width="740" height="60" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="392" fill="#f8fafc" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Theological Core: Systematic dismantling of polytheism and imperial tyranny</text>
  <text x="400" y="412" fill="#94a3b8" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">Every plague proved that Egypt's pantheon had zero power before Yahweh, the sole Sovereign Creator.</text>
</svg>"""

# Lesson 4: Divine Attributes in the Plagues
SVG_LESSON_4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="coreAttrGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#4f46e5"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad4)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Attributes of God Revealed in the Plagues</text>
  <text x="400" y="60" fill="#94a3b8" font-size="12.5" font-family="system-ui, sans-serif" text-anchor="middle">How God's Character and Eternal Nature are Manifested in Judgment and Deliverance</text>

  <!-- Central Hub: Sovereign Yahweh -->
  <g transform="translate(320, 90)">
    <rect width="160" height="60" rx="10" fill="url(#coreAttrGrad)" filter="url(#shadow4)"/>
    <text x="80" y="27" fill="#ffffff" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">YAHWEH</text>
    <text x="80" y="45" fill="#e0e7ff" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">The Living Sovereign</text>
  </g>

  <!-- 4 Quadrant Cards -->
  <!-- Card 1: Omnipotence -->
  <g filter="url(#shadow4)" transform="translate(35, 175)">
    <rect width="345" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="345" height="28" rx="8" fill="#0369a1"/>
    <text x="172" y="19" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. OMNIPOTENCE (Total Power)</text>
    <text x="15" y="48" fill="#38bdf8" font-size="11" font-weight="600">Manifestation in Plagues:</text>
    <text x="15" y="66" fill="#cbd5e1" font-size="10.5">• Total mastery over nature, Nile, weather &amp; sun</text>
    <text x="15" y="84" fill="#cbd5e1" font-size="10.5">• Exposes the complete impotence of Egyptian idols</text>
    <text x="15" y="100" fill="#94a3b8" font-size="9.5" font-style="italic">Lesson: No power in heaven or earth rivals God.</text>
  </g>

  <!-- Card 2: Justice & Righteousness -->
  <g filter="url(#shadow4)" transform="translate(420, 175)">
    <rect width="345" height="110" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="345" height="28" rx="8" fill="#b91c1c"/>
    <text x="172" y="19" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. DIVINE JUSTICE (Cosmic Redress)</text>
    <text x="15" y="48" fill="#f87171" font-size="11" font-weight="600">Manifestation in Plagues:</text>
    <text x="15" y="66" fill="#cbd5e1" font-size="10.5">• Direct judgment on 400 years of oppression</text>
    <text x="15" y="84" fill="#cbd5e1" font-size="10.5">• Avenges infanticide and systemic cruelty</text>
    <text x="15" y="100" fill="#94a3b8" font-size="9.5" font-style="italic">Lesson: God holds every oppressive empire accountable.</text>
  </g>

  <!-- Card 3: Faithfulness to Covenant -->
  <g filter="url(#shadow4)" transform="translate(35, 305)">
    <rect width="345" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="345" height="28" rx="8" fill="#047857"/>
    <text x="172" y="19" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. COVENANT FAITHFULNESS</text>
    <text x="15" y="48" fill="#34d399" font-size="11" font-weight="600">Manifestation in Plagues:</text>
    <text x="15" y="66" fill="#cbd5e1" font-size="10.5">• Remembers the Abrahamic covenant (Gen 15:13-14)</text>
    <text x="15" y="84" fill="#cbd5e1" font-size="10.5">• Sparing Goshen demonstrates covenant protection</text>
    <text x="15" y="100" fill="#94a3b8" font-size="9.5" font-style="italic">Lesson: God never abandons His promises across generations.</text>
  </g>

  <!-- Card 4: Mercy & Longsuffering -->
  <g filter="url(#shadow4)" transform="translate(420, 305)">
    <rect width="345" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="345" height="28" rx="8" fill="#d97706"/>
    <text x="172" y="19" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">4. PATIENT MERCY</text>
    <text x="15" y="48" fill="#fbbf24" font-size="11" font-weight="600">Manifestation in Plagues:</text>
    <text x="15" y="66" fill="#cbd5e1" font-size="10.5">• Progressive warnings (Plagues 1 to 9) before final strike</text>
    <text x="15" y="84" fill="#cbd5e1" font-size="10.5">• Gave Pharaoh and Egypt ample opportunities to repent</text>
    <text x="15" y="100" fill="#94a3b8" font-size="9.5" font-style="italic">Lesson: God's wrath is slow, giving sinners room for repentance.</text>
  </g>
</svg>"""

# Lesson 5: The Passover and Christological Typology
SVG_LESSON_5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="typeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="antitypeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#831843"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <filter id="shadow5" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad5)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Passover Typology: Old Testament Type &amp; New Testament Antitype</text>
  <text x="400" y="60" fill="#94a3b8" font-size="12.5" font-family="system-ui, sans-serif" text-anchor="middle">How the Hebrew Exodus Passover Foreshadows the Sacrificial Atonement of Jesus Christ</text>

  <!-- Side-by-Side Comparison Container -->
  <!-- Left Side: Old Testament Type (Passover Lamb) -->
  <g transform="translate(30, 80)" filter="url(#shadow5)">
    <rect width="350" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="350" height="36" rx="10" fill="url(#typeGrad)"/>
    <text x="175" y="24" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">OLD TESTAMENT TYPE (Passover Lamb)</text>
    
    <rect x="15" y="50" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="68" fill="#38bdf8" font-size="11" font-weight="700">1. Flawless Male Lamb (Ex 12:5)</text>
    <text x="25" y="85" fill="#cbd5e1" font-size="10.5">Year-old male without spot or blemish</text>

    <rect x="15" y="105" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="123" fill="#38bdf8" font-size="11" font-weight="700">2. Blood Applied to Doorposts (Ex 12:7)</text>
    <text x="25" y="140" fill="#cbd5e1" font-size="10.5">Shielded household from physical death</text>

    <rect x="15" y="160" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="178" fill="#38bdf8" font-size="11" font-weight="700">3. No Bones Broken (Ex 12:46)</text>
    <text x="25" y="195" fill="#cbd5e1" font-size="10.5">Lamb roasted whole with complete integrity</text>

    <rect x="15" y="215" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="233" fill="#38bdf8" font-size="11" font-weight="700">4. Unleavened Bread &amp; Herbs (Ex 12:8)</text>
    <text x="25" y="250" fill="#cbd5e1" font-size="10.5">Hasty departure and remembrance of bitter slavery</text>

    <rect x="15" y="270" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="288" fill="#38bdf8" font-size="11" font-weight="700">5. Physical Deliverance (Ex 12:31)</text>
    <text x="25" y="305" fill="#cbd5e1" font-size="10.5">Liberation from Egyptian slavery to Promised Land</text>
  </g>

  <!-- Right Side: New Testament Antitype (Jesus Christ) -->
  <g transform="translate(420, 80)" filter="url(#shadow5)">
    <rect width="350" height="330" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="350" height="36" rx="10" fill="url(#antitypeGrad)"/>
    <text x="175" y="24" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">NEW TESTAMENT ANTITYPE (Jesus Christ)</text>
    
    <rect x="15" y="50" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="68" fill="#fb7185" font-size="11" font-weight="700">1. Sinless Lamb of God (1 Pet 1:19; Jn 1:29)</text>
    <text x="25" y="85" fill="#cbd5e1" font-size="10.5">Pure, blameless sacrifice for global humanity</text>

    <rect x="15" y="105" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="123" fill="#fb7185" font-size="11" font-weight="700">2. Blood of Christ on Believer (Rom 5:9)</text>
    <text x="25" y="140" fill="#cbd5e1" font-size="10.5">Cleanses from sin and saves from eternal wrath</text>

    <rect x="15" y="160" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="178" fill="#fb7185" font-size="11" font-weight="700">3. Legs Not Broken on Cross (Jn 19:36)</text>
    <text x="25" y="195" fill="#cbd5e1" font-size="10.5">Fulfillment of prophetic scriptural typology</text>

    <rect x="15" y="215" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="233" fill="#fb7185" font-size="11" font-weight="700">4. Lord's Supper Communion (Lk 22:19)</text>
    <text x="25" y="250" fill="#cbd5e1" font-size="10.5">Bread of life and cup of the New Covenant</text>

    <rect x="15" y="270" width="320" height="45" rx="6" fill="#0f172a"/>
    <text x="25" y="288" fill="#fb7185" font-size="11" font-weight="700">5. Spiritual Deliverance (Col 1:13)</text>
    <text x="25" y="305" fill="#cbd5e1" font-size="10.5">Rescued from dominion of darkness into Kingdom</text>
  </g>

  <!-- Central Bridge Indicator -->
  <g transform="translate(385, 230)">
    <circle cx="15" cy="15" r="14" fill="#fbbf24"/>
    <text x="15" y="20" fill="#0f172a" font-size="14" font-weight="900" font-family="system-ui, sans-serif" text-anchor="middle">➔</text>
  </g>

  <!-- Bottom Summary Line -->
  <text x="400" y="430" fill="#94a3b8" font-size="11" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Typological Principle: The Exodus is the physical model of the spiritual salvation achieved in Christ.</text>
</svg>"""

# Lesson 6: Wilderness Care & The Duality of Liberation
SVG_LESSON_6 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="routeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <filter id="shadow6" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad6)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="36" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Stations of Wilderness Provision &amp; The Nature of Liberation</text>
  <text x="400" y="58" fill="#94a3b8" font-size="12.5" font-family="system-ui, sans-serif" text-anchor="middle">Exodus 14-17: Divine Sustenance, Communal Teamwork, and Freedom for Service</text>

  <!-- Top Timeline Track -->
  <rect x="30" y="75" width="740" height="150" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="45" y="98" fill="#38bdf8" font-size="12" font-weight="700" font-family="system-ui, sans-serif">GEOGRAPHICAL STATIONS OF MIRACULOUS CARE</text>

  <!-- Connecting Pathway Line -->
  <line x1="60" y1="140" x2="740" y2="140" stroke="url(#routeGrad)" stroke-width="4"/>

  <!-- Station 1: Red Sea -->
  <g transform="translate(60, 120)">
    <circle cx="20" cy="20" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="20" y="25" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">1</text>
    <text x="20" y="50" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">Red Sea</text>
    <text x="20" y="65" fill="#94a3b8" font-size="9" text-anchor="middle">Parted waters</text>
    <text x="20" y="78" fill="#94a3b8" font-size="9" text-anchor="middle">Chariots routed</text>
  </g>

  <!-- Station 2: Marah & Elim -->
  <g transform="translate(230, 120)">
    <circle cx="20" cy="20" r="16" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
    <text x="20" y="25" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">2</text>
    <text x="20" y="50" fill="#fbbf24" font-size="10.5" font-weight="700" text-anchor="middle">Marah &amp; Elim</text>
    <text x="20" y="65" fill="#94a3b8" font-size="9" text-anchor="middle">Bitter water sweet</text>
    <text x="20" y="78" fill="#94a3b8" font-size="9" text-anchor="middle">12 oasis springs</text>
  </g>

  <!-- Station 3: Desert of Sin -->
  <g transform="translate(400, 120)">
    <circle cx="20" cy="20" r="16" fill="#059669" stroke="#34d399" stroke-width="2"/>
    <text x="20" y="25" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">3</text>
    <text x="20" y="50" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">Desert of Sin</text>
    <text x="20" y="65" fill="#94a3b8" font-size="9" text-anchor="middle">Daily Manna</text>
    <text x="20" y="78" fill="#94a3b8" font-size="9" text-anchor="middle">Evening quails</text>
  </g>

  <!-- Station 4: Rephidim -->
  <g transform="translate(570, 120)">
    <circle cx="20" cy="20" r="16" fill="#7c3aed" stroke="#a78bfa" stroke-width="2"/>
    <text x="20" y="25" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">4</text>
    <text x="20" y="50" fill="#a78bfa" font-size="10.5" font-weight="700" text-anchor="middle">Rephidim</text>
    <text x="20" y="65" fill="#94a3b8" font-size="9" text-anchor="middle">Water from Rock</text>
    <text x="20" y="78" fill="#94a3b8" font-size="9" text-anchor="middle">Aaron &amp; Hur assist</text>
  </g>

  <!-- Station 5: Mount Sinai -->
  <g transform="translate(710, 120)">
    <circle cx="20" cy="20" r="16" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
    <text x="20" y="25" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">5</text>
    <text x="20" y="50" fill="#f87171" font-size="10.5" font-weight="700" text-anchor="middle">Sinai</text>
    <text x="20" y="65" fill="#94a3b8" font-size="9" text-anchor="middle">Covenant &amp; Law</text>
  </g>

  <!-- Bottom Section: The Duality of True Freedom -->
  <g transform="translate(30, 240)" filter="url(#shadow6)">
    <rect width="355" height="155" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <rect width="355" height="28" rx="8" fill="#991b1b"/>
    <text x="177" y="19" fill="#ffffff" font-size="11.5" font-weight="700" text-anchor="middle">FREEDOM FROM (Deliverance)</text>
    <text x="15" y="50" fill="#fca5a5" font-size="11" font-weight="600">• Bondage &amp; Forced Mortar Labor</text>
    <text x="15" y="70" fill="#cbd5e1" font-size="10.5">• Fear of Imperial Tyranny &amp; Infanticide</text>
    <text x="15" y="90" fill="#cbd5e1" font-size="10.5">• Deceptive Egyptian Polytheism</text>
    <text x="15" y="110" fill="#cbd5e1" font-size="10.5">• Physical Hunger &amp; Desert Dehydration</text>
    <text x="15" y="132" fill="#94a3b8" font-size="9.5" font-style="italic">Rescued from destruction by God's mighty outstretched arm.</text>
  </g>

  <g transform="translate(415, 240)" filter="url(#shadow6)">
    <rect width="355" height="155" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <rect width="355" height="28" rx="8" fill="#047857"/>
    <text x="177" y="19" fill="#ffffff" font-size="11.5" font-weight="700" text-anchor="middle">FREEDOM TO (Purpose &amp; Vocation)</text>
    <text x="15" y="50" fill="#6ee7b7" font-size="11" font-weight="600">• Worship God in Spirit &amp; Truth</text>
    <text x="15" y="70" fill="#cbd5e1" font-size="10.5">• Live in Holy Covenant Community</text>
    <text x="15" y="90" fill="#cbd5e1" font-size="10.5">• Practice Responsible Resource Stewardship</text>
    <text x="15" y="110" fill="#cbd5e1" font-size="10.5">• Support Weak Leaders (Aaron &amp; Hur Model)</text>
    <text x="15" y="132" fill="#94a3b8" font-size="9.5" font-style="italic">"We are not merely freed from slavery; we are freed for service."</text>
  </g>

  <!-- Footer Insight -->
  <text x="400" y="425" fill="#94a3b8" font-size="11" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Wilderness Principle: Daily dependence on God transforms a grumbling mob into a disciplined covenant nation.</text>
</svg>"""

# =============================================================================
# CURATED DISCRETE LESSON UNITS DEFINITIONS
# =============================================================================

TOPIC_1_5_UNITS = [
    # -------------------------------------------------------------------------
    # UNIT 1 / LESSON 1
    # -------------------------------------------------------------------------
    {
        "unit_order": 1,
        "unit_name": "The Call of Moses (Exodus 3:1-22)",
        "unit_description": "Examine the historical setting of Israelite oppression in Egypt, Moses' exile in Midian, the theophany of the burning bush at Mount Horeb, and God's sovereign commission of Moses as deliverer.",
        "lesson_title": "The Call and Vocation of Moses",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Mount_Sinai%2C_Egypt.jpg/1280px-Mount_Sinai%2C_Egypt.jpg",
        "image_caption": "The rugged landscape of Mount Sinai (Horeb), the traditional biblical mountain where Moses encountered God at the burning bush.",
        "svg_content": SVG_LESSON_1,
        "youtube_id": "0BbzC_aXhQY",
        "youtube_title": "BibleProject: Exodus 1-18 Overview",
        "youtube_description": "Explore the literary structure and theological themes of Exodus chapters 1-18, focusing on God hearing Israel's cry and raising Moses.",
        "pages": [
            # Page 1: Hook & Context
            [
                {
                    "type": "suggested_image",
                    "title": "Historical Context: Mount Sinai & The Wilderness",
                    "content": {
                        "caption": "The rugged wilderness of Mount Sinai (Horeb), where Moses was shepherding when God appeared in the burning bush.",
                        "credit": "Wikimedia Commons / Creative Commons Attribution"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Egyptian Bondage and the Cry of Israel",
                    "content": {
                        "text": "The Exodus narrative begins against a dark backdrop of severe imperial oppression. Following the death of Joseph, a new Pharaoh ascended the Egyptian throne who did not remember Joseph's service. Fearing the rapid population growth of the Hebrews, Egypt subjected them to bitter slavery, brutal mortar and brick labor, and state-sanctioned male infanticide.\n\nIn their agony, the Israelites cried out to God. God heard their groaning, remembered His covenant with Abraham, Isaac, and Jacob, and prepared a deliverer: Moses, who had fled Egypt and spent 40 years as a humble shepherd in Midian near Mount Horeb."
                    }
                }
            ],
            # Page 2: Vector Blueprint & Concept
            [
                {
                    "type": "suggested_diagram",
                    "title": "Diagram: The Divine Vocation Architecture",
                    "content": {
                        "description": "Visualizing Moses' transition from royal privilege to desert humility, culminating in the burning bush theophany."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Burning Bush and Holy Ground",
                    "content": {
                        "text": "At Mount Horeb, Moses witnessed an astounding sight: a desert bush burning with intense fire yet not consumed. This supernatural phenomenon is a **theophany**—a visible, sensory manifestation of God's presence.\n\nKey elements of the encounter:\n- **Divine Initiative:** God called Moses by name: 'Moses! Moses!' Moses responded, 'Here I am.'\n- **Reverence Command:** God commanded, 'Take off your sandals, for the place where you are standing is holy ground.'\n- **Covenant Identity:** God identified Himself as the God of Abraham, Isaac, and Jacob.\n- **The Commission:** God announced His sovereign intervention: 'So now, go. I am sending you to Pharaoh to bring my people out of Egypt.'"
                    }
                }
            ],
            # Page 3: Key Verse & Misconception
            [
                {
                    "type": "callout",
                    "title": "Scriptural Anchor: Exodus 3:14",
                    "content": {
                        "type": "quote",
                        "text": "God said to Moses, 'I AM WHO I AM.' And he said, 'Say this to the people of Israel: \"I AM has sent me to you.\"'",
                        "reference": "Exodus 3:14 (ESV)"
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The 'Fearless Leader' Myth",
                    "content": {
                        "misconception": "Learners often assume that Biblical prophets and leaders were fearless heroes who instantly accepted dangerous divine missions without hesitation.",
                        "truth": "Moses was deeply overwhelmed, terrified of returning to Egypt, and repeatedly questioned his ability. Biblical leadership is rooted not in superhuman confidence, but in human humility learning total dependence on God's sovereign power."
                    }
                }
            ],
            # Page 4: Video & Multimedia
            [
                {
                    "type": "suggested_video",
                    "title": "Curated Video: The Story of Exodus (BibleProject)",
                    "content": {
                        "description": "Examine how Exodus traces God's rescue of His oppressed people from Egyptian tyranny through the call of Moses."
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Classroom Dramatization & Role-Play",
                    "content": {
                        "instructions": "In groups of three, assign the roles of **Moses**, **The Voice from the Burning Bush**, and **The Narrator**.\n\n1. Enact Exodus 3:1-12, focusing on the dramatic shift from quiet shepherding to a high-stakes royal mission.\n2. Express Moses' transition from curiosity to trembling awe as he removes his sandals.\n3. Evaluate your performance using the peer rubric: Historical Accuracy (1-5), Reverence (1-5), Emotional Realism (1-5)."
                    }
                }
            ],
            # Page 5: Values & Critical Thinking
            [
                {
                    "type": "callout",
                    "title": "Core Values: Reverence & Holy Trust",
                    "content": {
                        "type": "values",
                        "text": "• **Reverence:** Removing sandals symbolizes humility before absolute divine holiness. In modern life, we express reverence by respecting sacred spaces, treating human beings with dignity, and honoring God's creation.\n• **Trust:** Believing that God sees human suffering and acts in justice, even when relief seems delayed."
                    }
                },
                {
                    "type": "reflection",
                    "title": "Critical Thinking: The Midian Preparation",
                    "content": {
                        "prompt": "Moses spent 40 years as an elite royal in Pharaoh's court, followed by 40 years as an ordinary shepherd in the Midian desert. How did the quiet, demanding task of shepherding prepare Moses to lead millions of stubborn, fragile people through the harsh wilderness?",
                        "guiding_points": [
                            "Patience in leading slow, vulnerable animals",
                            "Navigating desert terrain and locating water sources",
                            "Shedding Egyptian royal pride to embrace humble servanthood"
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Key Takeaway
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Moses at Mount Horeb",
                    "content": {
                        "question": "Where was Moses shepherding his flock when he encountered the theophany of the burning bush?",
                        "options": [
                            "In the royal gardens of Memphis in Egypt",
                            "In the fertile plains of Moab near the Jordan",
                            "Near Mount Horeb in Midian",
                            "In the coastal delta of Goshen"
                        ],
                        "correct_answer": "Near Mount Horeb in Midian",
                        "explanation": "According to Exodus 3:1, Moses was shepherding the flock of his father-in-law Jethro in Midian when he led them to Horeb, the mountain of God."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Key Takeaways: The Call of Moses",
                    "content": {
                        "points": [
                            "God hears the cry of the oppressed and initiates salvation according to His covenant promises.",
                            "A theophany is a visible manifestation of God, requiring absolute reverence and obedience.",
                            "Divine vocation is God-centered: He equips ordinary, imperfect human beings for extraordinary service."
                        ]
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 2 / LESSON 2
    # -------------------------------------------------------------------------
    {
        "unit_order": 2,
        "unit_name": "The Discourse Between God and Moses (Exodus 4:1-19)",
        "unit_description": "Analyze Moses' five objections to his divine commission, God's patient reassuring answers, the three miraculous signs of equipping, and practical applications for leadership and obedience.",
        "lesson_title": "The Divine-Human Discourse: Objections and Reassurances",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Geb_and_Nut.jpg/1280px-Geb_and_Nut.jpg",
        "image_caption": "Ancient Egyptian relief depicting divine authority and royal staff emblems, reflecting the imperial court context Moses had to confront.",
        "svg_content": SVG_LESSON_2,
        "youtube_id": "6ZzVlX8rI5U",
        "youtube_title": "The Five Excuses of Moses & God's Provision",
        "youtube_description": "A comprehensive pedagogical breakdown of Exodus 3:11 to 4:17 examining how God answers human doubt with sovereign authority.",
        "pages": [
            # Page 1: Hook & Narrative
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Context: Royal Court Authority & Shepherd Staff",
                    "content": {
                        "caption": "Egyptian reliefs demonstrating the sceptres of imperial power, which God challenged through Moses' simple wooden shepherd staff.",
                        "credit": "Wikimedia Commons / Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Dramatic Dialogue of Commissioning",
                    "content": {
                        "text": "When God commanded Moses to return to Egypt and confront Pharaoh, Moses did not immediately comply. Instead, a dramatic and prolonged discourse ensued in Exodus 3:11 - 4:17.\n\nMoses raised five distinct objections, reflecting profound self-doubt, fear of rejection, and public inadequacy. Rather than striking Moses down, God patiently answered each objection with reassurance, theological revelation, supernatural signs, and shared structural leadership."
                    }
                }
            ],
            # Page 2: Vector Table of Objections
            [
                {
                    "type": "suggested_diagram",
                    "title": "Diagram: Flowchart of Moses' 5 Objections & God's Answers",
                    "content": {
                        "description": "Visual matrix matching each human excuse with its corresponding divine provision and empowering promise."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Five Objections and Divine Solutions",
                    "content": {
                        "text": "1. **Personal Inadequacy (Ex 3:11):** *'Who am I that I should go?'* — **God's Answer:** *'I will be with you'* (Ex 3:12). Divine presence, not human prestige, guarantees success.\n2. **Lack of Authority (Ex 3:13):** *'What is His name?'* — **God's Answer:** *'I AM WHO I AM'* (Ex 3:14). Revelation of the eternal, covenant-keeping Yahweh.\n3. **Lack of Credibility (Ex 4:1):** *'They will not believe me'* — **God's Answer:** Equips Moses with 3 supernatural signs.\n4. **Lack of Eloquence (Ex 4:10):** *'I am slow of speech and tongue'* — **God's Answer:** *'Who gave human beings their mouths? I will teach you'* (Ex 4:11-12).\n5. **Outright Reluctance (Ex 4:13):** *'Please send someone else'* — **God's Answer:** God provides Aaron the Levite as Moses' articulate spokesman (Ex 4:14-16)."
                    }
                }
            ],
            # Page 3: Miraculous Signs & Typology
            [
                {
                    "type": "concept_explanation",
                    "title": "The Three Miraculous Equipping Signs",
                    "content": {
                        "text": "To dismantle Moses' fear that Israel would not believe him, God provided three profound signs (Exodus 4:2-9):\n\n- **The Staff to Serpent:** The shepherd's staff turned into a venomous snake when cast down. In Egypt, the serpent (uraeus) was the supreme symbol of Pharaoh's royal sovereignty. Moses grabbing its tail and restoring it to wood symbolized Yahweh's authority to subdue Pharaoh.\n- **The Leprous Hand:** Moses placed his hand in his cloak and pulled it out covered in white leprosy; putting it back restored it completely. This demonstrated God's power over incurable illness, life, and bodily restoration.\n- **Nile Water to Blood:** Pouring Nile water on dry ground turned it to blood, foreshadowing the first plague and God's power over Egypt's sacred river."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Moses' Speech Impediment",
                    "content": {
                        "misconception": "Some learners believe Moses had an incurable physical handicap that made it impossible for him to communicate at all.",
                        "truth": "Moses' objection ('heavy of speech') reflected anxiety regarding formal royal rhetoric in the Egyptian court. Stephen notes in Acts 7:22 that Moses was 'powerful in speech and action.' The lesson is that anxiety often blinds us to how God has already equipped us."
                    }
                }
            ],
            # Page 4: Curated Video & Activity
            [
                {
                    "type": "suggested_video",
                    "title": "Curated Video: The Five Excuses of Moses",
                    "content": {
                        "description": "Analyze how God addresses human inadequacy and why divine empowerment surpasses natural charisma."
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Excuse vs. Divine Answer Matching Exercise",
                    "content": {
                        "instructions": "Match each excuse with its divine provision in your study group:\n\n1. 'Who am I that I should go?' ➔ [Divine Presence: 'I will be with you']\n2. 'What is His name?' ➔ [Self-Revelation: 'I AM WHO I AM']\n3. 'They will not believe me!' ➔ [Three Miraculous Signs of Power]\n4. 'I am slow of speech!' ➔ [Creator of the mouth promises inspiration]\n5. 'Please send someone else!' ➔ [Aaron appointed as co-leader]\n\nReflect: Which of these excuses do you most often make when called to serve others?"
                    }
                }
            ],
            # Page 5: Real-World Ethical Dilemma
            [
                {
                    "type": "reflection",
                    "title": "Real-World Ethical Scenario: Student Leadership",
                    "content": {
                        "prompt": "You are a quiet, reflective student who listens well and maintains high moral integrity. Your class teacher and classmates nominate you to be the Head of the Peer Counseling Club. However, you are terrified of public speaking and believe you lack the loud, charismatic personality of other popular student leaders.\n\n1. Would you decline the nomination out of fear of public speaking, or accept it trusting that your listening skills are what struggling students need?\n2. How does Moses' fourth objection ('I am slow of speech') and God's answer apply to your decision?",
                        "guiding_points": [
                            "Integrity and empathy are more vital for counseling than loud speech",
                            "God provides teammates (like Aaron) to support areas of weakness",
                            "Stepping out of comfort zones builds true leadership maturity"
                        ]
                    }
                },
                {
                    "type": "callout",
                    "title": "Core Values: Humility & Faithful Obedience",
                    "content": {
                        "type": "values",
                        "text": "• **Humility:** Recognizing personal limitations without allowing those limitations to become an excuse for disobedience.\n• **Obedience:** Acting in faith upon God's command even when the assignment appears daunting or impossible."
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: The Divine Discourse",
                    "content": {
                        "question": "What theological truth is demonstrated by Moses' shepherd staff turning into a serpent and back into a staff?",
                        "options": [
                            "It showed that Moses was a skilled Egyptian magician.",
                            "It proved that snakes are inherently sacred creatures in biblical law.",
                            "It symbolized God's sovereign power to subdue Pharaoh's royal authority represented by the cobra.",
                            "It was a warning that Moses would die in the desert if he disobeyed."
                        ],
                        "correct_answer": "It symbolized God's sovereign power to subdue Pharaoh's royal authority represented by the cobra.",
                        "explanation": "In ancient Egypt, the serpent (uraeus) symbolized Pharaoh's imperial rule and divinity. Subduing the serpent proved Yahweh's authority over Egypt's crown."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Key Takeaways: Discourse and Divine Provision",
                    "content": {
                        "points": [
                            "God patiently listens to our doubts and systematically provides for our weaknesses.",
                            "Divine vocation relies on God's eternal presence ('I AM') rather than human eloquence or prestige.",
                            "God often pairs leaders in collaborative teams (Moses and Aaron) to accomplish His redemptive mission."
                        ]
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 3 / LESSON 3
    # -------------------------------------------------------------------------
    {
        "unit_order": 3,
        "unit_name": "The Ten Plagues (Exodus 7:14 - 11:10)",
        "unit_description": "Examine the Ten Plagues as systematic divine judgments against Egypt's pantheon, the limits of occult magic, the hardening of Pharaoh's heart, and the sovereign distinction sparing Goshen.",
        "lesson_title": "The Ten Plagues and the Defeat of Egyptian Deities",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/The_Seven_Plagues_of_Egypt_%281%29.jpg/1280px-The_Seven_Plagues_of_Egypt_%281%29.jpg",
        "image_caption": "Historic etching depicting the catastrophic impact of the plagues of Egypt, demonstrating divine sovereignty over nature.",
        "svg_content": SVG_LESSON_3,
        "youtube_id": "bx_GWz3p3mU",
        "youtube_title": "BibleProject: The 10 Plagues and the Gods of Egypt",
        "youtube_description": "Discover how the 10 Plagues were a direct theological confrontation between Yahweh and the oppressive gods of Pharaoh's empire.",
        "pages": [
            # Page 1: Hook & Background
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Artifact: Egyptian Relief of the Nile Deities",
                    "content": {
                        "caption": "Ancient relief of Hapi, the god of the Nile flood, whom the first plague systematically exposed as powerless.",
                        "credit": "Wikimedia Commons / CC-BY-SA"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Introduction: Why the Ten Plagues?",
                    "content": {
                        "text": "When Moses and Aaron delivered God's command—'Let my people go, that they may hold a festival to me'—Pharaoh arrogantly answered: 'Who is the LORD, that I should obey his voice? I do not know the LORD, and I will not let Israel go' (Exodus 5:2).\n\nIn response, God sent Ten Plagues upon Egypt (Exodus 7:14 - 11:10). Far from random ecological catastrophes, these plagues were targeted **theological polemics**—divine judgments exposing the complete powerlessness of Egypt's gods and establishing Yahweh's universal sovereignty."
                    }
                }
            ],
            # Page 2: Vector Blueprint & The 10 Plagues Breakdown
            [
                {
                    "type": "suggested_diagram",
                    "title": "Diagram: The 10 Plagues & Targeted Deities",
                    "content": {
                        "description": "A 3-cycle matrix showing each plague, its scriptural reference, and the specific Egyptian false god defeated."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Cycles of Plagues and Egyptian Deities",
                    "content": {
                        "text": "The plagues progressed through three distinct 3-plague cycles culminating in the tenth plague:\n\n- **Plague 1: Water to Blood (Ex 7:14-25):** Targets *Hapi* (Nile god) and *Osiris* (Nile as bloodstream).\n- **Plague 2: Frogs (Ex 8:1-15):** Targets *Heqet* (frog-headed goddess of fertility).\n- **Plague 3: Gnats/Lice (Ex 8:16-19):** Targets *Geb* (god of earth and soil).\n- **Plague 4: Flies/Swarms (Ex 8:20-32):** Targets *Khepri* (scarab-beetle god of creation).\n- **Plague 5: Livestock Pestilence (Ex 9:1-7):** Targets *Apis* (sacred bull) & *Hathor* (cow goddess).\n- **Plague 6: Boils (Ex 9:8-12):** Targets *Imhotep* and *Sekhmet* (deities of healing and medicine).\n- **Plague 7: Hail & Fire (Ex 9:13-35):** Targets *Nut* (sky goddess) and *Isis*.\n- **Plague 8: Locusts (Ex 10:1-20):** Targets *Osiris* and *Serapis* (agricultural protectors).\n- **Plague 9: Darkness (Ex 10:21-29):** Targets *Ra* (supreme sun god) and *Aten*.\n- **Plague 10: Death of Firstborn (Ex 11:1-10):** Targets *Pharaoh himself* (worshipped as Horus on earth)."
                    }
                }
            ],
            # Page 3: Key Analytical Themes
            [
                {
                    "type": "concept_explanation",
                    "title": "The Magicians' Limits & The Goshen Distinction",
                    "content": {
                        "text": "Three critical theological dynamics emerge throughout the plague narrative:\n\n1. **The Magicians' Failure:** Pharaoh's court sorcerers replicated the first two plagues through deceptive occult arts. But when dust became gnats in Plague 3, their powers failed, compelling them to confess: *'This is the finger of God!'* (Exodus 8:19).\n2. **The Sovereign Exemption of Goshen:** From Plague 4 (flies) onward, God made a distinct division between Egypt and Goshen: *'I will deal differently with the land of Goshen, where my people live; no swarms of flies will be there'* (Exodus 8:22). This proved Yahweh's selective covenant protection.\n3. **The Hardening of Pharaoh's Heart:** Pharaoh initially hardened his own heart through stubborn arrogance (Plagues 1-5). Subsequently, God solidified Pharaoh in his chosen rebellion, demonstrating that persistent rejection of light results in spiritual blindness."
                    }
                },
                {
                    "type": "callout",
                    "title": "Scriptural Anchor: Exodus 12:12",
                    "content": {
                        "type": "quote",
                        "text": "For I will pass through the land of Egypt that night, and I will strike all the firstborn in the land of Egypt, both man and beast; and on all the gods of Egypt I will execute judgments: I am the LORD.",
                        "reference": "Exodus 12:12 (ESV)"
                    }
                }
            ],
            # Page 4: Video & Collaborative Activity
            [
                {
                    "type": "suggested_video",
                    "title": "Curated Video: The 10 Plagues and the Defeat of False Gods",
                    "content": {
                        "description": "Watch how the plagues systematically shattered the religious, economic, and imperial foundations of Egypt."
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Group Sketching: Plague Sequencing Poster",
                    "content": {
                        "instructions": "In groups of four, take a large poster board and create a 10-grid matrix:\n\n1. Sketch a representative icon for each of the 10 plagues in chronological sequence.\n2. Annotate each box with the corresponding Egyptian god defeated.\n3. Highlight Plagues 4 through 10 with a special marker showing 'Goshen Protected'.\n4. Present to the class: Why was the 10th plague the decisive blow to Pharaoh's imperial power?"
                    }
                }
            ],
            # Page 5: High-Level MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: The Finger of God",
                    "content": {
                        "question": "Why did the Egyptian magicians declare, 'This is the finger of God,' during the third plague of gnats/lice?",
                        "options": [
                            "Because they successfully replicated the miracle to please Pharaoh",
                            "Because they reached the limit of their secret arts and recognized Yahweh's superior creative power",
                            "Because Pharaoh commanded them to bow before Moses and Aaron",
                            "Because the plague only affected Egyptian livestock and spared the palace"
                        ],
                        "correct_answer": "Because they reached the limit of their secret arts and recognized Yahweh's superior creative power",
                        "explanation": "In Exodus 8:19, the magicians failed to produce gnats from dust and openly acknowledged that this was direct divine intervention surpassing all human or occult magic."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Sparing the Land of Goshen",
                    "content": {
                        "question": "What is the primary theological significance of God sparing the land of Goshen starting from the fourth plague of flies?",
                        "options": [
                            "It proved Goshen possessed better geographic sanitation than Egyptian cities",
                            "It showed God makes a sovereign distinction between His covenant people and their oppressors",
                            "It indicated that Moses had paid Pharaoh a tax to protect Goshen",
                            "It excused the Israelites from needing to observe the Passover blood ritual"
                        ],
                        "correct_answer": "It showed God makes a sovereign distinction between His covenant people and their oppressors",
                        "explanation": "Exodus 8:22-23 explicitly states that God set apart the land of Goshen to show that Yahweh is actively present in the land and shields His covenant people."
                    }
                }
            ],
            # Page 6: Values & Takeaways
            [
                {
                    "type": "callout",
                    "title": "Core Values: Truthfulness & Social Justice",
                    "content": {
                        "type": "values",
                        "text": "• **Truthfulness:** Exposing false secular idols and fraudulent claims of ultimate power.\n• **Social Justice:** God does not remain neutral in the face of long-term tyranny and human exploitation. Christians must advocate for the oppressed just as God intervened for enslaved Israel."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Key Takeaways: The Ten Plagues",
                    "content": {
                        "points": [
                            "The plagues demonstrated Yahweh's absolute sovereignty over creation and exposed the vanity of Egypt's gods.",
                            "Occult deception has strict boundaries and collapses before the almighty power of God.",
                            "God protects His people in the midst of global upheaval and brings righteous judgment upon unrepentant oppressors."
                        ]
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 4 / LESSON 4
    # -------------------------------------------------------------------------
    {
        "unit_order": 4,
        "unit_name": "Attributes of God Revealed in the Plagues",
        "unit_description": "Analyze the divine character revealed through the Exodus plagues: Omnipotence, Justice, Sovereignty, Covenant Faithfulness, and Patient Mercy, with modern ethical applications.",
        "lesson_title": "Divine Attributes Revealed in the Plagues",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Nile_near_Aswan.jpg/1280px-Nile_near_Aswan.jpg",
        "image_caption": "The Nile River at dusk, reflecting the natural lifelines of ancient civilizations that Yahweh commanded and judged.",
        "svg_content": SVG_LESSON_4,
        "youtube_id": "oXbNfW_YgQw",
        "youtube_title": "The Character of God in Exodus (BibleProject)",
        "youtube_description": "An in-depth study of God's justice, mercy, and faithfulness as revealed through the dramatic deliverance of Israel.",
        "pages": [
            # Page 1: Hook & Concept
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Reflection: The Majesty of the Nile",
                    "content": {
                        "caption": "The Nile River, the vital artery of Egypt's empire, which God transformed to demonstrate His absolute lordship over nature.",
                        "credit": "Wikimedia Commons / CC-BY-SA"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Plagues as Self-Revelation of God's Character",
                    "content": {
                        "text": "The plagues of Egypt were not merely destructive displays of raw force; they were profound acts of divine self-revelation. Through them, God answered Pharaoh's defiant question—'Who is the LORD?'—and revealed His eternal attributes to both the Egyptians and the Israelites.\n\nGod revealed that He is neither a localized tribal deity nor a silent spectator of history, but the righteous Creator and Judge of the universe."
                    }
                }
            ],
            # Page 2: Vector Concept Map & Core Attributes
            [
                {
                    "type": "suggested_diagram",
                    "title": "Diagram: Concept Map of Divine Attributes in the Plagues",
                    "content": {
                        "description": "Quadrant blueprint illustrating God's Omnipotence, Justice, Covenant Faithfulness, and Longsuffering Mercy."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Core Divine Attributes in Action",
                    "content": {
                        "text": "1. **Omnipotence (All-Powerful Nature):** God exercised total mastery over every realm of nature—water, soil, amphibians, insects, animal health, human skin, atmospheric weather, and the solar disk. Every Egyptian deity was shown to be powerless.\n2. **Cosmic Justice:** The plagues directly redressed 400 years of unpunished slavery, forced labor, and the drowning of Hebrew baby boys in the Nile. Divine justice balances the scales of human history.\n3. **Covenant Faithfulness:** Rescuing Israel fulfilled the ancient promise God spoke to Abraham centuries earlier in Genesis 15:13-14: *'I will punish the nation they serve as slaves, and afterward they will come out with great possessions.'*\n4. **Patient Mercy & Longsuffering:** Rather than annihilating Egypt in an instant, God sent progressive warnings across Plagues 1 through 9, giving Pharaoh and the Egyptian people repeated opportunities to repent and submit."
                    }
                }
            ],
            # Page 3: Natural vs Supernatural Debate
            [
                {
                    "type": "reflection",
                    "title": "Critical Thinking: Ecological Coincidence vs. Supernatural Acts",
                    "content": {
                        "prompt": "Some modern secular commentators attempt to explain the Ten Plagues as purely natural chain reactions (e.g. volcanic ash polluting the Nile, causing frogs to leave the water, leading to insect swarms and livestock disease).\n\nWhile God can use natural elements (like the east wind to bring locusts), how do the **precise timing**, the **unprecedented severity**, Moses' predictive words, and the **miraculous exemption of Goshen** prove that these were intentional, supernatural divine interventions?",
                        "guiding_points": [
                            "Plagues started and stopped precisely when Moses prayed",
                            "The sudden, sharp boundary protecting Goshen while Egypt suffered",
                            "The supernatural 3-day darkness that could be 'felt' across Egypt"
                        ]
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: God as a Vindictive Tyrant",
                    "content": {
                        "misconception": "Some readers view the plagues as harsh cruelty inflicted by a wrathful God on innocent people.",
                        "truth": "God endured 400 years of Israelite enslavement and infant murder before sending judgment. The plagues were measured judicial warnings against a genocidal empire. God's justice protects the vulnerable from unchecked evil."
                    }
                }
            ],
            # Page 4: Video & Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Curated Video: The Justice and Mercy of God",
                    "content": {
                        "description": "Understand the tension between divine justice against oppression and divine patience with rebellious rulers."
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Contemporary Case Study: Oppression & Divine Justice",
                    "content": {
                        "instructions": "In pairs, analyze modern examples of economic exploitation (e.g. child labor in mines, human trafficking, corrupt sweatshops).\n\n1. How does the biblical truth of God's justice give hope to victims of modern exploitation?\n2. What ethical responsibility do Christians have to advocate for fair wages and human rights today?"
                    }
                }
            ],
            # Page 5: Values & Ethical Commitments
            [
                {
                    "type": "callout",
                    "title": "Core Values: Integrity & Respect for Human Rights",
                    "content": {
                        "type": "values",
                        "text": "• **Integrity:** Standing for the truth of God's sovereignty even in hostile environments.\n• **Respect for Human Rights:** Recognizing that every human being is made in God's image, making systemic oppression an offense against God Himself."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Faithfulness to the Abrahamic Covenant",
                    "content": {
                        "question": "Which ancient covenant promise was God fulfilling when He delivered Israel from Egyptian bondage?",
                        "options": [
                            "The covenant with Noah never to flood the earth again",
                            "The covenant with Abraham in Genesis 15:13-14 promising to judge their oppressors and bring them out with great wealth",
                            "The covenant with King David promising an eternal throne",
                            "The covenant with Adam in the Garden of Eden regarding the tree of life"
                        ],
                        "correct_answer": "The covenant with Abraham in Genesis 15:13-14 promising to judge their oppressors and bring them out with great wealth",
                        "explanation": "God explicitly remembered His covenant with Abraham, Isaac, and Jacob (Exodus 2:24; Gen 15:13-14), proving His unbreakable faithfulness across generations."
                    }
                }
            ],
            # Page 6: Summary & Practical Takeaway
            [
                {
                    "type": "key_takeaway",
                    "title": "Key Takeaways: Divine Attributes in the Plagues",
                    "content": {
                        "points": [
                            "God is Omnipotent: Creation obeys its Maker, and no earthly power can resist His will.",
                            "God is Just: Oppression and cruelty never escape divine accountability.",
                            "God is Faithful: His promises span centuries and are fulfilled with unwavering precision.",
                            "God is Patiently Merciful: He warns before He judges, inviting all people to repentance."
                        ]
                    }
                },
                {
                    "type": "callout",
                    "title": "Personal Reflection Anchor",
                    "content": {
                        "type": "quote",
                        "text": "The LORD is slow to anger and great in power, and the LORD will by no means clear the guilty.",
                        "reference": "Nahum 1:3 / Exodus 34:6-7"
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 5 / LESSON 5
    # -------------------------------------------------------------------------
    {
        "unit_order": 5,
        "unit_name": "The Passover and Foreshadowing of Christ's Atonement (Exodus 12:1-31)",
        "unit_description": "Examine the institution of the Hebrew Passover (Pesach), its symbolic ritual elements, the blood on the doorposts, and its profound typological fulfillment in the sacrificial death of Jesus Christ.",
        "lesson_title": "The Passover and Foreshadowing of Christ's Atonement",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/The_First_Passover.jpg/1280px-The_First_Passover.jpg",
        "image_caption": "Historic illustration of a Hebrew family applying the blood of the Passover lamb to the doorposts with hyssop in Egypt.",
        "svg_content": SVG_LESSON_5,
        "youtube_id": "g_mFdrg_rI8",
        "youtube_title": "BibleProject: The Passover Lamb & Jesus",
        "youtube_description": "Explore how the Passover ritual in Exodus 12 lays the foundation for Jesus' Last Supper and His death as the Lamb of God.",
        "pages": [
            # Page 1: Hook & Passover Institution
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Hook: Slaying the Passover Lamb & Marking Doorposts",
                    "content": {
                        "caption": "Depiction of the first Passover night, when the blood of the unblemished lamb marked the threshold of Israelite homes.",
                        "credit": "Wikimedia Commons / Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Institution of the Passover (Exodus 12:1-31)",
                    "content": {
                        "text": "To escape the final, catastrophic plague—the death of all firstborn in Egypt—God commanded the Israelites to institute the **Passover** (*Pesach*). This sacred ritual marked the official birth of Israel as a liberated, covenant nation and was to be celebrated annually across all generations.\n\nEvery Hebrew household was commanded to take an unblemished male lamb, slaughter it at twilight, and apply its blood to the top lintel and two side doorposts of their house. When the judgment of God passed through Egypt, homes marked with the blood were spared."
                    }
                }
            ],
            # Page 2: Vector Blueprint & Typology Matrix
            [
                {
                    "type": "suggested_diagram",
                    "title": "Diagram: Passover Type and New Testament Antitype",
                    "content": {
                        "description": "Side-by-side comparative blueprint mapping the Old Testament Passover Lamb to Jesus Christ's atonement on the cross."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Symbolic Elements of the Passover Meal",
                    "content": {
                        "text": "Every element of the Passover meal carried deep spiritual and historical meaning:\n\n- **The Unblemished Lamb:** A flawless one-year-old male lamb representing purity and innocence (Exodus 12:5).\n- **The Blood on the Doorposts:** Applied with hyssop, serving as an outward sign of faith and substitutionary protection: *'When I see the blood, I will pass over you'* (Exodus 12:13).\n- **Unleavened Bread (*Matzah*):** Baked without yeast to symbolize the haste of their departure (no time for dough to rise) and moral purity (yeast symbolized sin).\n- **Bitter Herbs (*Maror*):** Symbolized the bitter agony and tears of their 400-year slavery in Egypt.\n- **Eaten in Haste:** Eaten with robes tucked into belts, sandals on feet, and staff in hand, ready for instant flight when the call came."
                    }
                }
            ],
            # Page 3: Typology & Christological Fulfillment
            [
                {
                    "type": "concept_explanation",
                    "title": "Typology: Jesus Christ, the Ultimate Passover Lamb",
                    "content": {
                        "text": "**Biblical Typology** is the study of how Old Testament events, institutions, and people (the *Type*) foreshadow and find fulfillment in New Testament realities (the *Antitype*).\n\nThe Passover is the supreme Old Testament type of Christ's atonement:\n\n- **Flawless Lamb ➔ Sinless Christ:** Jesus is the spotless, sinless Lamb of God (John 1:29; 1 Peter 1:18-19).\n- **Blood on Doorposts ➔ Blood of the Cross:** Christ's shed blood shields believers from spiritual death and eternal condemnation (Romans 5:9).\n- **No Bones Broken ➔ Crucifixion Prophecy:** In Exodus 12:46, no bone of the lamb was to be broken. John 19:33-36 records that the Roman soldiers did not break Jesus' legs on the cross.\n- **Passover Meal ➔ The Lord's Supper:** At the Last Supper (a Passover meal), Jesus broke the bread and poured the cup, establishing the New Covenant in His blood (Luke 22:19-20)."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Typological Erasure of History",
                    "content": {
                        "misconception": "Some students mistakenly believe that because the Passover prefigures Christ, the historical Exodus event was merely an allegory that never really happened.",
                        "truth": "Christian theology insists that the historical liberation of real Hebrew slaves from real Egyptian oppression is the concrete historical anchor that gives spiritual redemption in Christ its rich meaning."
                    }
                }
            ],
            # Page 4: Curated Video & Reflection Journal
            [
                {
                    "type": "suggested_video",
                    "title": "Curated Video: The Passover and the Lamb of God",
                    "content": {
                        "description": "Watch how the biblical narrative connects the blood on the doorposts in Egypt with Jesus' sacrifice on Calvary."
                    }
                },
                {
                    "type": "reflection",
                    "title": "Personal Reflection: Stepping Out of Your 'Personal Egypt'",
                    "content": {
                        "prompt": "The Passover marked the moment Israel stepped out of slavery into freedom by faith in the blood of the lamb.\n\nReflect in your journal: What negative habits, destructive peer pressures, guilt, or secret fears represent your 'personal Egypt' today? How does faith in Christ's love and sacrifice give you the moral courage to leave those bondages behind?",
                        "guiding_points": [
                            "Identifying destructive behaviors that hold you captive",
                            "Understanding that forgiveness in Christ breaks the power of guilt",
                            "Living as a free person dedicated to God's purpose"
                        ]
                    }
                }
            ],
            # Page 5: High-Level MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Sparing the Bones of the Lamb",
                    "content": {
                        "question": "Sparing the bones of the Passover lamb from being broken (Exodus 12:46) directly prefigures which New Testament event?",
                        "options": [
                            "Jesus' birth in the humble stable of Bethlehem",
                            "Jesus' baptism by John in the Jordan River",
                            "The Roman soldiers refraining from breaking Jesus' legs on the cross",
                            "The ascension of Jesus into heaven from the Mount of Olives"
                        ],
                        "correct_answer": "The Roman soldiers refraining from breaking Jesus' legs on the cross",
                        "explanation": "John 19:33-36 records that while the two criminals had their legs broken, Jesus was already dead, fulfilling Exodus 12:46: 'Not one of his bones will be broken.'"
                    }
                },
                {
                    "type": "callout",
                    "title": "Scriptural Anchor: 1 Corinthians 5:7",
                    "content": {
                        "type": "quote",
                        "text": "Cleanse out the old leaven that you may be a new lump, as you really are unleavened. For Christ, our Passover lamb, has been sacrificed.",
                        "reference": "1 Corinthians 5:7 (ESV)"
                    }
                }
            ],
            # Page 6: Values & Key Takeaway
            [
                {
                    "type": "callout",
                    "title": "Core Values: Gratitude, Purity & Sanctification",
                    "content": {
                        "type": "values",
                        "text": "• **Gratitude:** Deep thanksgiving for the unearned gift of redemption and deliverance from death.\n• **Purity:** Living an 'unleavened' life of sincerity and truth, free from malice, hypocrisy, and corrupt habits."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Key Takeaways: The Passover and Christ",
                    "content": {
                        "points": [
                            "The Passover marked Israel's national birth through substitutionary blood and obedience in faith.",
                            "Every ritual element—unblemished lamb, shed blood, unleavened bread, bitter herbs—pointed forward to Jesus Christ.",
                            "Christians celebrate Christ as the true Passover Lamb who permanently delivers believers from the slavery of sin."
                        ]
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 6 / LESSON 6
    # -------------------------------------------------------------------------
    {
        "unit_order": 6,
        "unit_name": "God's Care in the Wilderness and True Liberation (Exodus 14-17)",
        "unit_description": "Trace Israel's journey from the Red Sea crossing through Marah, Elim, the Desert of Sin (Manna and Quails), to Rephidim (Water from Rock & defeating Amalek), synthesizing the true biblical meaning of liberation.",
        "lesson_title": "God's Miraculous Care in the Wilderness and True Liberation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Red_Sea_at_Sunset.jpg/1280px-Red_Sea_at_Sunset.jpg",
        "image_caption": "The waters of the Red Sea coast, scene of God's miraculous deliverance of the Israelite multitude.",
        "svg_content": SVG_LESSON_6,
        "youtube_id": "Ikyk3gIuDk8",
        "youtube_title": "BibleProject: Wilderness Journey & Testing",
        "youtube_description": "Explore the wilderness narrative in Exodus 14-18 and learn how God tests and provides for His newly liberated people.",
        "pages": [
            # Page 1: Hook & Red Sea Crossing
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Context: The Red Sea Coastline",
                    "content": {
                        "caption": "The Gulf of Suez / Red Sea coastline, where the cornered Israelites witnessed the sea divide before them.",
                        "credit": "Wikimedia Commons / CC-BY-SA"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Deliverance at the Red Sea (Exodus 14:5-31)",
                    "content": {
                        "text": "Deliverance from Egypt was not a one-time event; it was the initiation of an ongoing relationship of trust. Soon after Israel departed, Pharaoh regretted losing his slave workforce and pursued them with 600 elite chariots.\n\nTrapped between the approaching Egyptian army and the waters of the Red Sea, the Israelites panicked. God commanded Moses: *'Why do you cry to me? Tell the Israelites to move forward. Raise your staff and stretch out your hand over the sea.'*\n\nThrough a strong east wind, God parted the waters, allowing Israel to cross on dry ground with walls of water on their right and left. When the Egyptian army pursued, the waters collapsed, permanently breaking the military power of the oppressor."
                    }
                }
            ],
            # Page 2: Vector Blueprint & Wilderness Stations
            [
                {
                    "type": "suggested_diagram",
                    "title": "Diagram: Stations of Wilderness Care & Duality of Freedom",
                    "content": {
                        "description": "Geographical timeline from the Red Sea to Sinai alongside the theological framework of Freedom From vs. Freedom To."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Stations of Miraculous Care",
                    "content": {
                        "text": "In the arid Sinai desert, God systematically addressed every physical survival need of the young nation:\n\n1. **Bitter Water Made Sweet at Marah (Ex 15:22-27):** After 3 days without water, the water at Marah was undrinkable. God showed Moses a piece of wood; when thrown into the water, it turned sweet. God revealed Himself as *Yahweh-Rapha* ('The Lord who heals you') before leading them to **Elim** with 12 springs and 70 palm trees.\n2. **Daily Manna and Evening Quail (Ex 16:1-36):** Facing hunger, God rained down 'bread from heaven' (Manna) and sent quails at twilight. The daily gathering rule taught dependence and Sabbath rest.\n3. **Water from the Rock at Rephidim (Ex 17:1-7):** When the people grumbled from thirst, God commanded Moses to strike the rock at Horeb with his staff, causing streams of life-giving water to gush forth.\n4. **Defeat of the Amalekites (Ex 17:8-16):** When the nomadic Amalekites attacked, Joshua fought while Moses held up God's staff with the vital assistance of Aaron and Hur."
                    }
                }
            ],
            # Page 3: Teamwork & The Aaron and Hur Model
            [
                {
                    "type": "concept_explanation",
                    "title": "Communal Cooperation: The Aaron and Hur Principle",
                    "content": {
                        "text": "During the fierce battle against Amalek at Rephidim (Exodus 17:8-16), an essential principle of leadership emerged:\n\nAs long as Moses held up his hands holding God's staff, Israel prevailed; whenever he lowered his hands, Amalek prevailed. But Moses' hands grew weary and heavy.\n\n**The Cooperative Solution:** Aaron and Hur placed a stone under Moses so he could sit, and they stood on either side, holding his hands steady until sunset. This secured complete victory and proved that even the greatest spiritual leaders cannot carry missions alone—collaborative support, teamwork, and shared responsibility are essential for community success."
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Active Learning: Acting as 'Aaron and Hur' Today",
                    "content": {
                        "instructions": "In groups of five, discuss:\n\n1. Identify leaders in your school, family, or community (e.g. teachers, class prefects, church leaders) who are overburdened and at risk of burnout.\n2. Develop a concrete 'Aaron and Hur Support Plan': What three practical tasks can your group undertake this term to uphold their hands and share their burdens?"
                    }
                }
            ],
            # Page 4: Video & True Meaning of Liberation
            [
                {
                    "type": "suggested_video",
                    "title": "Curated Video: The Wilderness Journey & Testing",
                    "content": {
                        "description": "Watch how the wilderness experience transformed an enslaved mob into a disciplined, covenant-keeping community."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Duality of Liberation: Freedom For Service",
                    "content": {
                        "text": "The Exodus reveals that biblical liberation has two complementary dimensions:\n\n- **Freedom FROM:** Rescued from physical slavery, forced brickmaking, dehumanizing violence, and imperial idolatry.\n- **Freedom TO:** Liberated to worship Yahweh in holiness, live in loving covenant community, protect the vulnerable, and practice responsible stewardship.\n\n*Theological Maxim:* We are not merely freed *from* bondage; we are freed *for* faithful service to God and humanity."
                    }
                }
            ],
            # Page 5: High-Level MCQs & Sequencing
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Holding up Moses' Hands",
                    "content": {
                        "question": "Who stood beside Moses to hold up his hands during the battle against the Amalekites at Rephidim?",
                        "options": [
                            "Joshua and Caleb",
                            "Aaron and Hur",
                            "Jethro and Zipporah",
                            "Miriam and Gershom"
                        ],
                        "correct_answer": "Aaron and Hur",
                        "explanation": "Exodus 17:12 states that Aaron and Hur held Moses' hands up—one on one side, one on the other—so that his hands remained steady until sunset."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Wilderness Route Chronology",
                    "content": {
                        "question": "Which of the following represents the correct chronological sequence of stations in the Exodus journey?",
                        "options": [
                            "Marah ➔ Egypt ➔ Mount Sinai ➔ Red Sea ➔ Manna in Desert of Sin",
                            "Egypt ➔ Red Sea Crossing ➔ Marah & Elim ➔ Desert of Sin (Manna) ➔ Rephidim & Sinai",
                            "Rephidim ➔ Red Sea ➔ Egypt ➔ Marah ➔ Desert of Sin",
                            "Mount Sinai ➔ Rephidim ➔ Desert of Sin ➔ Red Sea ➔ Egypt"
                        ],
                        "correct_answer": "Egypt ➔ Red Sea Crossing ➔ Marah & Elim ➔ Desert of Sin (Manna) ➔ Rephidim & Sinai",
                        "explanation": "Israel marched from Egypt across the Red Sea, traveled to Marah/Elim, then to the Desert of Sin, Rephidim, and finally arrived at Mount Sinai."
                    }
                }
            ],
            # Page 6: Values, Reflection & Comprehensive Takeaway
            [
                {
                    "type": "callout",
                    "title": "Core Values: Compassion, Cooperation & Contentment",
                    "content": {
                        "type": "values",
                        "text": "• **Compassion:** Caring for the thirsty, hungry, and exhausted in times of transition.\n• **Cooperation:** Standing shoulder-to-shoulder with community leaders to ensure shared success.\n• **Contentment:** Trusting God for daily needs (like daily Manna) without succumbing to greed or anxiety."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Key Takeaways: The Exodus and Divine Deliverance",
                    "content": {
                        "points": [
                            "The Exodus is the central redemptive event of the Old Testament, demonstrating God's supreme power over all worldly empires.",
                            "God guides, feeds, heals, and protects His people through every wilderness trial.",
                            "True freedom is not autonomous lawlessness, but covenant relationship and loving service to God and community."
                        ]
                    }
                }
            ]
        ]
    }
]

# =============================================================================
# INGESTION EXECUTION ENGINE
# =============================================================================

def ingest_grade10_cre_topic_1_5(replace: bool = True):
    print("=" * 80)
    print("STARTING VLEARN GRADE 10 CRE TOPIC 1.5 INGESTION ENGINE")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade, Subject, Topic
        grade = Grade.objects.get(id=5) # Grade 10
        subject = Subject.objects.get(id=46) # CRE

        topic, t_created = Topic.objects.get_or_create(
            subject=subject,
            order=5,
            defaults={
                "name": "Topic 1.5: The Exodus",
                "description": "Examine the historical and theological milestone of the Exodus: the call of Moses, the discourse with God, the ten plagues against Egyptian deities, divine attributes, the institution of the Passover, Christological typology, and God's miraculous care in the wilderness."
            }
        )
        if not t_created:
            topic.name = "Topic 1.5: The Exodus"
            topic.description = "Examine the historical and theological milestone of the Exodus: the call of Moses, the discourse with God, the ten plagues against Egyptian deities, divine attributes, the institution of the Passover, Christological typology, and God's miraculous care in the wilderness."
            topic.save()

        print(f"Target Topic Resolved: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

        # If replace, clean existing learning units under this topic
        if replace:
            print("Purging existing LearningUnits, Lessons, Blocks and Assets under Topic 1.5...")
            for old_unit in topic.learning_units.all():
                for old_lesson in old_unit.lessons.all():
                    old_lesson.blocks.all().delete()
                    old_lesson.assets.all().delete()
                    old_lesson.delete()
                old_unit.delete()

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for unit_def in TOPIC_1_5_UNITS:
            u_order = unit_def["unit_order"]
            u_name = unit_def["unit_name"]
            u_desc = unit_def["unit_description"]
            l_title = unit_def["lesson_title"]
            pages = unit_def["pages"]

            # Create or resolve LearningUnit
            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={
                    "name": u_name,
                    "description": u_desc
                }
            )
            if not u_created:
                unit.name = u_name
                unit.description = u_desc
                unit.save()
            total_units += 1

            # Create or resolve Lesson (Published, Version 1)
            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": l_title,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "author": "VLearn Grade 10 CRE Topic 1.5 Ingestion Agent",
                        "grade": "Grade 10",
                        "subject": "CRE",
                        "topic_order": 5,
                        "unit_order": u_order
                    }
                }
            )
            if not l_created:
                lesson.title = l_title
                lesson.status = "published"
                lesson.version = 1
                lesson.immutable_metadata = {
                    "author": "VLearn Grade 10 CRE Topic 1.5 Ingestion Agent",
                    "grade": "Grade 10",
                    "subject": "CRE",
                    "topic_order": 5,
                    "unit_order": u_order
                }
                lesson.save()

            # Clean existing blocks and assets for idempotency
            lesson.blocks.all().delete()
            lesson.assets.all().delete()
            total_lessons += 1

            # -----------------------------------------------------------------
            # 1. LessonAsset: Photographic Visual Hook (Wikimedia)
            # -----------------------------------------------------------------
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                title=f"Visual Hook: {l_title}",
                url=unit_def["image_url"],
                metadata={"caption": unit_def["image_caption"], "source": "Wikimedia Commons"}
            )
            total_assets += 1

            # -----------------------------------------------------------------
            # 2. LessonAsset: Sanitized Vector SVG Diagram
            # -----------------------------------------------------------------
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                title=f"Vector Blueprint: {l_title}",
                metadata={"svg_content": unit_def["svg_content"]}
            )
            total_assets += 1

            # -----------------------------------------------------------------
            # 3. LessonAsset: Curated Educational YouTube Video
            # -----------------------------------------------------------------
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                title=unit_def["youtube_title"],
                url=f"https://www.youtube.com/watch?v={unit_def['youtube_id']}",
                metadata={"youtube_id": unit_def["youtube_id"], "description": unit_def["youtube_description"]}
            )
            total_assets += 1

            # -----------------------------------------------------------------
            # Ingest Pages and LessonBlocks
            # -----------------------------------------------------------------
            block_order_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    # Inject resolved media URLs / SVGs into block content
                    if b_type == "suggested_image":
                        b_content["resolved_image_url"] = unit_def["image_url"]
                        b_content["url"] = unit_def["image_url"]
                        b_content["source"] = "Wikimedia Commons"
                    elif b_type == "suggested_diagram":
                        b_content["svg"] = unit_def["svg_content"]
                        b_content["svg_xml"] = unit_def["svg_content"]
                    elif b_type == "suggested_video":
                        b_content["url"] = f"https://www.youtube.com/watch?v={unit_def['youtube_id']}"
                        b_content["youtube_id"] = unit_def["youtube_id"]

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t1_5_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_order_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 5, "unit_order": u_order, "page": page_idx}
                    )

                    # Attach corresponding LessonAsset to specific blocks if relevant
                    if b_type == "suggested_image":
                        block.assets.add(img_asset)
                    elif b_type == "suggested_diagram":
                        block.assets.add(svg_asset)
                    elif b_type == "suggested_video":
                        block.assets.add(yt_asset)

                    block_order_counter += 1
                    total_blocks += 1

            print(f"  Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages/Cards, {block_order_counter - 1} Blocks, 3 Assets)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 1.5 '{topic.name}'")
    print(f"  Total Learning Units: {total_units}")
    print(f"  Total Published Lessons: {total_lessons}")
    print(f"  Total Progressive Pages (Cards): {total_pages}")
    print(f"  Total Enriched Blocks: {total_blocks}")
    print(f"  Total Attached Assets: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_grade10_cre_topic_1_5(replace=replace_flag)
