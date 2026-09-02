"""
VLearn CBC Grade 10 CRE — Topic 1.6: The Sinai Covenant
Production Ingestion Script

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5)
Subject: CRE (ID: 46)
Topic: Topic 1.6: The Sinai Covenant (Order: 6)

6 Discrete Learning Units & Lessons:
  1. Unit 1: Introduction to the Sinai Covenant (Covenant vs. Contract)
  2. Unit 2: The Making of the Sinai Covenant & Theophany (Exodus 19)
  3. Unit 3: The Ten Commandments (Decalogue) & Moral Law (Exodus 20)
  4. Unit 4: The Breaking of the Sinai Covenant: The Golden Calf (Exodus 32)
  5. Unit 5: The Renewal of the Sinai Covenant & God's Character (Exodus 34)
  6. Unit 6: Wilderness Tabernacle Worship & Modern Christian Living (Exodus 25-40)
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

# =============================================================================
# TEXT CLEANING UTILITIES
# =============================================================================

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return text
    # Strip bracket citations e.g. [1], [223], [12]
    cleaned = re.sub(r'\[\d+\]', '', text)
    # Strip internal pedagogical markup tags
    cleaned = re.sub(
        r'\[(VISUAL|BIBLE PASSAGE|KEY VERSE|VALUES|MISCONCEPTION|CRITICAL THINKING|REAL WORLD APPLICATION|MCQ|MCQ: HIGH)[^\]]*\]:?',
        '',
        cleaned,
        flags=re.IGNORECASE
    )
    # Strip redundant spaces and clean double blanks
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned.strip()

def clean_dict(d):
    if isinstance(d, dict):
        return {k: clean_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [clean_dict(v) for v in d]
    elif isinstance(d, str):
        return clean_text(d)
    return d

# =============================================================================
# SVG VECTOR DIAGRAMS (Clean XML, Responsive viewBox, Clear Typography)
# =============================================================================

# Diagram 1: Covenant vs Contract Comparison Architecture
SVG_COVENANT_VS_CONTRACT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 500" width="100%" height="100%">
  <defs>
    <linearGradient id="headerGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <linearGradient id="contractGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef2f2"/>
      <stop offset="100%" stop-color="#fee2e2"/>
    </linearGradient>
    <linearGradient id="covenantGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#eff6ff"/>
      <stop offset="100%" stop-color="#dbeafe"/>
    </linearGradient>
    <filter id="shadow1" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.1"/>
    </filter>
  </defs>

  <rect width="850" height="500" rx="16" fill="#f8fafc"/>

  <!-- Header Banner -->
  <rect x="30" y="20" width="790" height="64" rx="12" fill="url(#headerGrad1)" filter="url(#shadow1)"/>
  <text x="425" y="46" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle">BIBLICAL COVENANT (BERITH) VS. SECULAR CONTRACT</text>
  <text x="425" y="68" fill="#bfdbfe" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">The Structural &amp; Theological Distinction of the Sinai Agreement</text>

  <!-- Left Column: Secular Contract -->
  <g transform="translate(35, 105)" filter="url(#shadow1)">
    <rect width="370" height="365" rx="12" fill="url(#contractGrad)" stroke="#ef4444" stroke-width="2"/>
    <rect x="15" y="14" width="340" height="34" rx="8" fill="#b91c1c"/>
    <text x="185" y="37" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SECULAR CONTRACT (AGREEMENT)</text>

    <!-- Key Attributes -->
    <rect x="15" y="60" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="80" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Underlying Foundation:</text>
    <text x="25" y="98" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Based on mutual suspicion, distrust &amp; self-protection</text>

    <rect x="15" y="120" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="140" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Sealing &amp; Ratification:</text>
    <text x="25" y="158" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Signed with physical ink, paper, or legal witnesses</text>

    <rect x="15" y="180" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="200" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Duration &amp; Conditions:</text>
    <text x="25" y="218" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Conditional; easily voided/broken if terms are violated</text>

    <rect x="15" y="240" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="260" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Core Motivation:</text>
    <text x="25" y="278" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Focuses on self-interest: "What do I gain from this deal?"</text>

    <!-- Bottom summary -->
    <rect x="15" y="302" width="340" height="48" rx="6" fill="#7f1d1d"/>
    <text x="185" y="322" fill="#fecaca" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Legal Exchange of Property or Services</text>
    <text x="185" y="338" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Can be terminated at convenience</text>
  </g>

  <!-- Right Column: Biblical Covenant -->
  <g transform="translate(445, 105)" filter="url(#shadow1)">
    <rect width="370" height="365" rx="12" fill="url(#covenantGrad)" stroke="#2563eb" stroke-width="2"/>
    <rect x="15" y="14" width="340" height="34" rx="8" fill="#1d4ed8"/>
    <text x="185" y="37" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">BIBLICAL COVENANT (HEBREW: BERITH)</text>

    <!-- Key Attributes -->
    <rect x="15" y="60" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="80" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Underlying Foundation:</text>
    <text x="25" y="98" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Founded upon unconditional love, trust &amp; divine grace</text>

    <rect x="15" y="120" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="140" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Sealing &amp; Ratification:</text>
    <text x="25" y="158" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Sealed through sacred solemn oaths, sacrifice &amp; blood</text>

    <rect x="15" y="180" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="200" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Duration &amp; Conditions:</text>
    <text x="25" y="218" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Lifelong, sacred, unbreakable bond involving the soul</text>

    <rect x="15" y="240" width="340" height="52" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="260" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Core Motivation:</text>
    <text x="25" y="278" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Outlines holy identity: "Who do I become in relationship?"</text>

    <!-- Bottom summary -->
    <rect x="15" y="302" width="340" height="48" rx="6" fill="#1e3a8a"/>
    <text x="185" y="322" fill="#bfdbfe" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Sacred Union of Persons &amp; Calling</text>
    <text x="185" y="338" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Exodus 19:5-6: "A Kingdom of Priests &amp; Holy Nation"</text>
  </g>
</svg>"""

# Diagram 2: Mount Sinai Boundaries & Theophany Architecture
SVG_SINAI_BOUNDARIES_THEOPHANY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 520" width="100%" height="100%">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="50%" stop-color="#431407"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="mountainGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="40%" stop-color="#9a3412"/>
      <stop offset="100%" stop-color="#451a03"/>
    </linearGradient>
    <linearGradient id="campGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <filter id="theophanyGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect width="850" height="520" rx="16" fill="#0f172a"/>

  <!-- Mountain Peak with Theophany (Fire, Smoke, Lightning) -->
  <polygon points="425,70 180,340 670,340" fill="url(#mountainGrad)"/>
  <circle cx="425" cy="70" r="45" fill="#f59e0b" fill-opacity="0.3" filter="url(#theophanyGlow)"/>
  <circle cx="425" cy="70" r="25" fill="#fbbf24" fill-opacity="0.6"/>

  <!-- Smoke and Fire Details -->
  <path d="M 400,60 Q 425,30 450,60 T 425,100 Z" fill="#f97316" opacity="0.8"/>
  <path d="M 370,110 Q 425,80 480,110 Q 450,140 400,130 Z" fill="#7c2d12" opacity="0.7"/>

  <!-- Theophany Labels -->
  <rect x="275" y="20" width="300" height="34" rx="8" fill="#1e1b4b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="425" y="42" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">DIVINE THEOPHANY: FIRE, SMOKE &amp; THUNDER</text>

  <!-- Moses Mediator Marker -->
  <g transform="translate(405, 175)">
    <circle cx="20" cy="20" r="16" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
    <text x="20" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">✝</text>
  </g>
  <rect x="330" y="215" width="190" height="26" rx="6" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1"/>
  <text x="425" y="232" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">MOSES AS COVENANT MEDIATOR</text>

  <!-- STRICT BOUNDARY ZONE -->
  <g transform="translate(50, 310)">
    <rect width="750" height="42" rx="8" fill="#dc2626" stroke="#fecaca" stroke-width="2"/>
    <text x="375" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">⛔ STRICT BOUNDARY LIMIT: DO NOT TOUCH THE MOUNTAIN (EXODUS 19:12)</text>
    <text x="375" y="38" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Teaches radical separation between Holy Creator and sinful humanity</text>
  </g>

  <!-- Israel's Consecration Camp -->
  <g transform="translate(50, 365)">
    <rect width="750" height="135" rx="10" fill="url(#campGrad)" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="375" y="25" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE CONGREGATION OF ISRAEL: THREE-DAY CONSECRATION PROTOCOL</text>

    <!-- 3 Pillars of Consecration -->
    <rect x="25" y="40" width="220" height="75" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
    <text x="135" y="60" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. Washing Clothes</text>
    <text x="135" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">External cleanliness</text>
    <text x="135" y="96" fill="#475569" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">symbolizing heart purity</text>

    <rect x="265" y="40" width="220" height="75" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
    <text x="375" y="60" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. Physical Abstinence</text>
    <text x="375" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Setting aside physical desire</text>
    <text x="375" y="96" fill="#475569" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">for focused spiritual awe</text>

    <rect x="505" y="40" width="220" height="75" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
    <text x="615" y="60" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. Respecting Boundaries</text>
    <text x="615" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Approaching God with</text>
    <text x="615" y="96" fill="#475569" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">reverence, not presumption</text>
  </g>
</svg>"""

# Diagram 3: Two Tablets of the Law (Decalogue Architecture)
SVG_DECALOGUE_TWO_TABLETS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 520" width="100%" height="100%">
  <defs>
    <linearGradient id="headerGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
    <linearGradient id="tabletGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="850" height="520" rx="16" fill="#f1f5f9"/>

  <!-- Title Header -->
  <rect x="30" y="18" width="790" height="56" rx="12" fill="url(#headerGrad3)" filter="url(#shadow3)"/>
  <text x="425" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">THE TEN COMMANDMENTS (DECALOGUE: EXODUS 20:1-17)</text>
  <text x="425" y="62" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">The Moral Framework of Biblical Covenant: Godward Worship &amp; Neighborward Justice</text>

  <!-- TABLET I: GODWARD DUTIES (Commands 1 - 4) -->
  <g transform="translate(45, 90)" filter="url(#shadow3)">
    <!-- Arch shape for stone tablet -->
    <path d="M 0,40 Q 0,0 40,0 L 320,0 Q 360,0 360,40 L 360,400 Q 360,410 350,410 L 10,410 Q 0,410 0,400 Z" fill="url(#tabletGrad1)" stroke="#2563eb" stroke-width="2.5"/>
    
    <rect x="20" y="20" width="320" height="34" rx="6" fill="#1e40af"/>
    <text x="180" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">TABLET I: GODWARD DUTIES (1-4)</text>

    <!-- Commands 1 to 4 -->
    <rect x="15" y="65" width="330" height="72" rx="6" fill="#ffffff" stroke="#bfdbfe" stroke-width="1"/>
    <text x="25" y="85" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. No Other Gods Before Me</text>
    <text x="25" y="103" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Exclusive devotion; reject all modern/ancient idols</text>
    <text x="25" y="121" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Loyalty to the One True Sovereign Lord</text>

    <rect x="15" y="145" width="330" height="72" rx="6" fill="#ffffff" stroke="#bfdbfe" stroke-width="1"/>
    <text x="25" y="165" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Do Not Make or Worship Idols</text>
    <text x="25" y="183" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• God is spirit; cannot be reduced to physical images</text>
    <text x="25" y="201" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Forbids manipulating the divine through charms</text>

    <rect x="15" y="225" width="330" height="72" rx="6" fill="#ffffff" stroke="#bfdbfe" stroke-width="1"/>
    <text x="25" y="245" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Do Not Misuse God's Holy Name</text>
    <text x="25" y="263" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Revering God's name in speech, oaths &amp; lifestyle</text>
    <text x="25" y="281" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Forbids hypocrisy, false swearing &amp; blasphemy</text>

    <rect x="15" y="305" width="330" height="72" rx="6" fill="#ffffff" stroke="#bfdbfe" stroke-width="1"/>
    <text x="25" y="325" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Keep the Sabbath Day Holy</text>
    <text x="25" y="343" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Dedicated cycle of physical rest &amp; spiritual refocus</text>
    <text x="25" y="361" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Affirming that human worth transcends nonstop labor</text>

    <text x="180" y="398" fill="#1e40af" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Pillar: Supreme Love for the Lord</text>
  </g>

  <!-- TABLET II: NEIGHBORWARD DUTIES (Commands 5 - 10) -->
  <g transform="translate(445, 90)" filter="url(#shadow3)">
    <path d="M 0,40 Q 0,0 40,0 L 320,0 Q 360,0 360,40 L 360,400 Q 360,410 350,410 L 10,410 Q 0,410 0,400 Z" fill="url(#tabletGrad1)" stroke="#059669" stroke-width="2.5"/>
    
    <rect x="20" y="20" width="320" height="34" rx="6" fill="#047857"/>
    <text x="180" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">TABLET II: NEIGHBORWARD DUTIES (5-10)</text>

    <rect x="15" y="60" width="330" height="48" rx="5" fill="#ffffff" stroke="#a7f3d0" stroke-width="1"/>
    <text x="25" y="78" fill="#065f46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Honor Father &amp; Mother</text>
    <text x="25" y="96" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Respecting family authority and generational stability</text>

    <rect x="15" y="114" width="330" height="48" rx="5" fill="#ffffff" stroke="#a7f3d0" stroke-width="1"/>
    <text x="25" y="132" fill="#065f46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">6. Do Not Murder</text>
    <text x="25" y="150" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Protecting the sacred sanctity of human life (Imago Dei)</text>

    <rect x="15" y="168" width="330" height="48" rx="5" fill="#ffffff" stroke="#a7f3d0" stroke-width="1"/>
    <text x="25" y="186" fill="#065f46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">7. Do Not Commit Adultery</text>
    <text x="25" y="204" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Safeguarding marital covenant, sexual purity &amp; trust</text>

    <rect x="15" y="222" width="330" height="48" rx="5" fill="#ffffff" stroke="#a7f3d0" stroke-width="1"/>
    <text x="25" y="240" fill="#065f46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">8. Do Not Steal</text>
    <text x="25" y="258" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Respecting property rights, fair trade &amp; honesty</text>

    <rect x="15" y="276" width="330" height="48" rx="5" fill="#ffffff" stroke="#a7f3d0" stroke-width="1"/>
    <text x="25" y="294" fill="#065f46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">9. Do Not Bear False Testimony</text>
    <text x="25" y="312" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Defending courtroom justice, truthfulness &amp; integrity</text>

    <rect x="15" y="330" width="330" height="48" rx="5" fill="#ffffff" stroke="#a7f3d0" stroke-width="1"/>
    <text x="25" y="348" fill="#065f46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">10. Do Not Covet</text>
    <text x="25" y="366" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Purifying heart desires, contentness &amp; joy for others</text>

    <text x="180" y="398" fill="#047857" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Pillar: Love Your Neighbor as Yourself</text>
  </g>
</svg>"""

# Diagram 4: Golden Calf Breakdown & Renewal Pathway
SVG_GOLDEN_CALF_BREACH_PATHWAY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 490" width="100%" height="100%">
  <defs>
    <linearGradient id="headerGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#ea580c"/>
    </linearGradient>
    <filter id="shadow4" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.1"/>
    </filter>
  </defs>

  <rect width="850" height="490" rx="16" fill="#f8fafc"/>

  <!-- Title Header -->
  <rect x="30" y="18" width="790" height="58" rx="12" fill="url(#headerGrad4)" filter="url(#shadow4)"/>
  <text x="425" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">THE PATHWAY OF COVENANT BREACH &amp; RESTORATION (EXODUS 32-34)</text>
  <text x="425" y="62" fill="#fef08a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">From Impatience &amp; Compromise to Idolatry, Righteous Judgment, and Intercession</text>

  <!-- Step 1 -->
  <g transform="translate(40, 95)" filter="url(#shadow4)">
    <rect width="230" height="150" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="10" y="10" width="210" height="26" rx="4" fill="#b91c1c"/>
    <text x="115" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. DELAY &amp; IMPATIENCE</text>
    <text x="15" y="55" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Moses on mountain 40 days</text>
    <text x="15" y="75" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Fear &amp; anxiety grip people</text>
    <text x="15" y="95" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Demands: "Make us gods!"</text>
    <text x="15" y="125" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Lack of spiritual endurance</text>
  </g>

  <!-- Arrow 1 -->
  <text x="290" y="175" fill="#ef4444" font-family="system-ui, sans-serif" font-size="22" font-weight="800" text-anchor="middle">➔</text>

  <!-- Step 2 -->
  <g transform="translate(310, 95)" filter="url(#shadow4)">
    <rect width="230" height="150" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="10" y="10" width="210" height="26" rx="4" fill="#d97706"/>
    <text x="115" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. WEAK LEADERSHIP</text>
    <text x="15" y="55" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Aaron yields to mob pressure</text>
    <text x="15" y="75" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Collects gold earrings</text>
    <text x="15" y="95" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Fashions the Golden Calf</text>
    <text x="15" y="125" fill="#b45309" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Popularity over moral truth</text>
  </g>

  <!-- Arrow 2 -->
  <text x="560" y="175" fill="#ef4444" font-family="system-ui, sans-serif" font-size="22" font-weight="800" text-anchor="middle">➔</text>

  <!-- Step 3 -->
  <g transform="translate(580, 95)" filter="url(#shadow4)">
    <rect width="230" height="150" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
    <rect x="10" y="10" width="210" height="26" rx="4" fill="#991b1b"/>
    <text x="115" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. BLATANT IDOLATRY</text>
    <text x="15" y="55" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• "These are your gods, Israel!"</text>
    <text x="15" y="75" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Wild dancing &amp; revelry</text>
    <text x="15" y="95" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Violates Commands 1 &amp; 2</text>
    <text x="15" y="125" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Total covenant breach</text>
  </g>

  <!-- Downward Arrows -->
  <text x="695" y="270" fill="#2563eb" font-family="system-ui, sans-serif" font-size="22" font-weight="800" text-anchor="middle">⬇</text>
  <text x="155" y="270" fill="#2563eb" font-family="system-ui, sans-serif" font-size="22" font-weight="800" text-anchor="middle">⬆</text>

  <!-- Step 4 -->
  <g transform="translate(580, 290)" filter="url(#shadow4)">
    <rect width="230" height="175" rx="8" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <rect x="10" y="10" width="210" height="26" rx="4" fill="#7f1d1d"/>
    <text x="115" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. SHATTERED TABLETS</text>
    <text x="15" y="55" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Moses descends in anger</text>
    <text x="15" y="75" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Smashes tablets at base</text>
    <text x="15" y="95" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Symbolizes broken covenant</text>
    <text x="15" y="115" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Grinds calf to dust</text>
    <text x="15" y="145" fill="#7f1d1d" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Righteous divine confrontation</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(310, 290)" filter="url(#shadow4)">
    <rect width="230" height="175" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="10" y="10" width="210" height="26" rx="4" fill="#1d4ed8"/>
    <text x="115" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. MOSES' INTERCESSION</text>
    <text x="15" y="55" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Pleads for God's mercy</text>
    <text x="15" y="75" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Reminds God of Abraham</text>
    <text x="15" y="95" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Offers his own life</text>
    <text x="15" y="115" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Stays divine wrath</text>
    <text x="15" y="145" fill="#1e40af" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Selfless pastoral leadership</text>
  </g>

  <!-- Step 6 -->
  <g transform="translate(40, 290)" filter="url(#shadow4)">
    <rect width="230" height="175" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
    <rect x="10" y="10" width="210" height="26" rx="4" fill="#047857"/>
    <text x="115" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">6. COVENANT RENEWAL</text>
    <text x="15" y="55" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• 2 new tablets carved</text>
    <text x="15" y="75" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• God reveals character</text>
    <text x="15" y="95" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Law rewritten identically</text>
    <text x="15" y="115" fill="#1f2937" font-family="system-ui, sans-serif" font-size="10.5">• Moses' radiant face</text>
    <text x="15" y="145" fill="#065f46" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Restoration through grace</text>
  </g>
</svg>"""

# Diagram 5: Divine Character Matrix (Exodus 34:6-7)
SVG_DIVINE_CHARACTER_REVELATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 480" width="100%" height="100%">
  <defs>
    <linearGradient id="headerGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312e81"/>
      <stop offset="100%" stop-color="#4338ca"/>
    </linearGradient>
    <linearGradient id="graceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="100%" stop-color="#d1fae5"/>
    </linearGradient>
    <linearGradient id="justiceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff7ed"/>
      <stop offset="100%" stop-color="#ffedd5"/>
    </linearGradient>
    <filter id="shadow5" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.1"/>
    </filter>
  </defs>

  <rect width="850" height="480" rx="16" fill="#f8fafc"/>

  <!-- Title Header -->
  <rect x="30" y="18" width="790" height="60" rx="12" fill="url(#headerGrad5)" filter="url(#shadow5)"/>
  <text x="425" y="44" fill="#ffffff" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">THE SELF-REVELATION OF GOD'S CHARACTER (EXODUS 34:6-7)</text>
  <text x="425" y="65" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="12" font-weight="500" text-anchor="middle">The Dynamic Harmony of Boundless Grace and Uncompromising Holy Justice</text>

  <!-- Left Card: Divine Grace & Mercy -->
  <g transform="translate(40, 95)" filter="url(#shadow5)">
    <rect width="365" height="355" rx="12" fill="url(#graceGrad)" stroke="#10b981" stroke-width="2"/>
    <rect x="15" y="14" width="335" height="34" rx="6" fill="#047857"/>
    <text x="182" y="37" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">BOUNDLESS DIVINE MERCY (HESED)</text>

    <!-- Attributes -->
    <rect x="15" y="60" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="78" fill="#065f46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Compassionate (Rachum):</text>
    <text x="25" y="94" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Tender maternal/paternal empathy towards suffering</text>

    <rect x="15" y="112" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="130" fill="#065f46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Gracious (Channun):</text>
    <text x="25" y="146" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Bestows unearned favor and second chances freely</text>

    <rect x="15" y="164" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="182" fill="#065f46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Slow to Anger (Erek Apayim):</text>
    <text x="25" y="198" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Immense patience; provides room for repentance</text>

    <rect x="15" y="216" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="234" fill="#065f46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Abounding in Love &amp; Faithfulness:</text>
    <text x="25" y="250" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Loyal covenant love extending to thousands of generations</text>

    <!-- Bottom summary -->
    <rect x="15" y="270" width="335" height="68" rx="6" fill="#064e3b"/>
    <text x="182" y="292" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">"Forgiving wickedness, rebellion &amp; sin"</text>
    <text x="182" y="312" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Restores broken relationships when sinners turn back</text>
  </g>

  <!-- Right Card: Divine Holiness & Justice -->
  <g transform="translate(445, 95)" filter="url(#shadow5)">
    <rect width="365" height="355" rx="12" fill="url(#justiceGrad)" stroke="#f97316" stroke-width="2"/>
    <rect x="15" y="14" width="335" height="34" rx="6" fill="#c2410c"/>
    <text x="182" y="37" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">UNCOMPROMISING HOLY JUSTICE (MISHPAT)</text>

    <!-- Attributes -->
    <rect x="15" y="60" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="78" fill="#9a3412" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Does Not Leave Guilty Unpunished:</text>
    <text x="25" y="94" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Evil and corruption are never ignored or swept aside</text>

    <rect x="15" y="112" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="130" fill="#9a3412" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Demands Moral Accountability:</text>
    <text x="25" y="146" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Rejection of presumptuous or cheap grace</text>

    <rect x="15" y="164" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="182" fill="#9a3412" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Protection of the Oppressed:</text>
    <text x="25" y="198" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Divine judgment defends victims from wickedness</text>

    <rect x="15" y="216" width="335" height="45" rx="6" fill="#ffffff" fill-opacity="0.9"/>
    <text x="25" y="234" fill="#9a3412" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">Generational Consequence:</text>
    <text x="25" y="250" fill="#1f2937" font-family="system-ui, sans-serif" font-size="11">• Sin produces ripple effects if unaddressed</text>

    <!-- Bottom summary -->
    <rect x="15" y="270" width="335" height="68" rx="6" fill="#7c2d12"/>
    <text x="182" y="292" fill="#fed7aa" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">"Yet He does not leave the guilty unpunished"</text>
    <text x="182" y="312" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Guarantees eternal cosmic justice and righteousness</text>
  </g>
</svg>"""

# Diagram 6: Tabernacle Architecture & Layout
SVG_TABERNACLE_SACRED_ARCHITECTURE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 540" width="100%" height="100%">
  <defs>
    <linearGradient id="headerGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="courtGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="100%" stop-color="#fde68a"/>
    </linearGradient>
    <linearGradient id="holyPlaceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#dbeafe"/>
      <stop offset="100%" stop-color="#bfdbfe"/>
    </linearGradient>
    <linearGradient id="holyOfHoliesGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#facc15"/>
    </linearGradient>
    <filter id="shadow6" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="880" height="540" rx="16" fill="#f8fafc"/>

  <!-- Title Header -->
  <rect x="30" y="16" width="820" height="56" rx="12" fill="url(#headerGrad6)" filter="url(#shadow6)"/>
  <text x="440" y="40" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">THE WILDERNESS TABERNACLE (MISHKAN) ARCHITECTURE &amp; STATIONS</text>
  <text x="440" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Exodus 25-40: The Progression from Outer Cleansing to Inner Divine Communion</text>

  <!-- Outer Court Perimeter -->
  <g transform="translate(40, 85)" filter="url(#shadow6)">
    <rect width="800" height="430" rx="12" fill="url(#courtGrad)" stroke="#b45309" stroke-width="2.5"/>
    <text x="400" y="24" fill="#78350f" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1. THE OUTER COURT (PUBLIC GATHERING &amp; SACRIFICIAL RECONCILIATION)</text>

    <!-- Bronze Altar -->
    <g transform="translate(600, 75)">
      <rect width="140" height="120" rx="8" fill="#b45309" stroke="#78350f" stroke-width="2"/>
      <text x="70" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BRONZE ALTAR</text>
      <text x="70" y="55" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Animal Sacrifices</text>
      <text x="70" y="75" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Atonement for Sin</text>
      <text x="70" y="95" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Leviticus 1-7</text>
    </g>

    <!-- Bronze Basin / Laver -->
    <g transform="translate(470, 95)">
      <circle cx="45" cy="45" r="45" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="45" y="38" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">BRONZE</text>
      <text x="45" y="54" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">BASIN</text>
      <text x="45" y="72" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Priestly Cleansing</text>
    </g>

    <!-- TENT OF MEETING (TABERNACLE PROPER) -->
    <g transform="translate(40, 50)">
      <!-- Outer boundary of tent -->
      <rect width="390" height="340" rx="8" fill="#ffffff" stroke="#1e293b" stroke-width="2"/>

      <!-- 2. Holy Place -->
      <rect x="140" y="20" width="230" height="300" rx="6" fill="url(#holyPlaceGrad)" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="255" y="45" fill="#1e40af" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2. THE HOLY PLACE</text>
      <text x="255" y="60" fill="#3b82f6" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">(Priests enter daily)</text>

      <!-- Menorah (Lampstand) -->
      <rect x="160" y="80" width="190" height="50" rx="4" fill="#ffffff" stroke="#60a5fa" stroke-width="1"/>
      <text x="255" y="100" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">GOLDEN LAMPSTAND (MENORAH)</text>
      <text x="255" y="118" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Spiritual light &amp; divine guidance</text>

      <!-- Table of Showbread -->
      <rect x="160" y="145" width="190" height="50" rx="4" fill="#ffffff" stroke="#60a5fa" stroke-width="1"/>
      <text x="255" y="165" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">TABLE OF SHOWBREAD</text>
      <text x="255" y="183" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">12 Loaves = God's constant provision</text>

      <!-- Altar of Incense -->
      <rect x="160" y="210" width="190" height="50" rx="4" fill="#ffffff" stroke="#60a5fa" stroke-width="1"/>
      <text x="255" y="230" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">ALTAR OF INCENSE</text>
      <text x="255" y="248" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Daily prayers rising before God</text>

      <!-- THE VEIL -->
      <line x1="135" y1="20" x2="135" y2="320" stroke="#7c3aed" stroke-width="4" stroke-dasharray="6,4"/>
      <text x="135" y="295" fill="#6d28d9" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle" transform="rotate(-90 135 295)">SACRED VEIL</text>

      <!-- 3. Holy of Holies -->
      <rect x="15" y="20" width="110" height="300" rx="6" fill="url(#holyOfHoliesGrad)" stroke="#ca8a04" stroke-width="2"/>
      <text x="70" y="45" fill="#713f12" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">3. HOLY OF</text>
      <text x="70" y="60" fill="#713f12" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">HOLIES</text>

      <!-- Ark of the Covenant -->
      <rect x="25" y="110" width="90" height="120" rx="6" fill="#ca8a04" stroke="#854d0e" stroke-width="1.5"/>
      <text x="70" y="135" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ARK OF THE</text>
      <text x="70" y="150" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">COVENANT</text>
      <text x="70" y="175" fill="#fef08a" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Mercy Seat &amp;</text>
      <text x="70" y="190" fill="#fef08a" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Cherubim</text>
      <text x="70" y="212" fill="#ffffff" font-family="system-ui, sans-serif" font-size="8" font-weight="600" text-anchor="middle">Throne of God</text>
    </g>

    <!-- Directional Pathway of Worship -->
    <rect x="470" y="235" width="290" height="150" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <text x="615" y="260" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">THE PILGRIMAGE OF WORSHIP</text>
    <text x="485" y="285" fill="#475569" font-family="system-ui, sans-serif" font-size="10.5">1. Sinner enters Outer Gate with sacrifice</text>
    <text x="485" y="305" fill="#475569" font-family="system-ui, sans-serif" font-size="10.5">2. Priest washes at Bronze Laver (Purity)</text>
    <text x="485" y="325" fill="#475569" font-family="system-ui, sans-serif" font-size="10.5">3. Enters Holy Place for Prayer &amp; Light</text>
    <text x="485" y="345" fill="#475569" font-family="system-ui, sans-serif" font-size="10.5">4. High Priest enters Holy of Holies (Atonement)</text>
    <text x="485" y="368" fill="#1e40af" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Fulfilled in Christ: Free access to God's presence</text>
  </g>
</svg>"""

# =============================================================================
# CURRICULUM DATA DEFINITION FOR TOPIC 1.6 (6 DISCRETE UNITS & LESSONS)
# =============================================================================

def build_topic_1_6_curriculum():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Introduction to the Sinai Covenant
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Introduction to the Sinai Covenant",
            "unit_description": "Exploring the foundational meaning of biblical covenant (Berith), contrasting covenant with secular contracts, and examining God's purpose for Israel as a kingdom of priests in Exodus 19:5-6.",
            "lesson_title": "The Nature of Covenant: Covenant vs. Contract",
            "pages": [
                # Card 1: Photographic Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Historical Setting: The Rugged Landscape of Mount Sinai",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Sinai_05-2016_img03_Mount_Sinai.jpg",
                            "caption": "The rugged granite peaks of Mount Sinai (Jabal Musa) in the Sinai Peninsula, the historic biblical site where God established His covenant with Israel.",
                            "author": "Wikimedia Commons / Berthold Werner",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_introduction",
                        "title": "Welcome to the Sinai Covenant",
                        "content": {
                            "text": "Imagine being part of an entire nation that has just walked out of four centuries of brutal slavery into the desert. You have no constitution, no king, no formal laws, and no unified identity.\n\nAt the foot of Mount Sinai, the Almighty God met these former slaves not to impose a crushing dictatorship, but to offer them a sacred, life-transforming relationship: the **Sinai Covenant**.\n\nIn this lesson, we uncover what makes a biblical covenant fundamentally different from any legal contract in modern society."
                        }
                    }
                ],
                # Card 2: Theological Concept: Covenant vs Contract
                [
                    {
                        "type": "definition_card",
                        "title": "Theological Concept: Berith (Biblical Covenant)",
                        "content": {
                            "term": "Berith (בְּרִית — Covenant)",
                            "definition": "A solemn, binding, and sacred relationship of mutual commitment initiated by God, sealed with sacrifice and blood, establishing an enduring family bond between God and His people.",
                            "contrast": "Unlike a contract (which exchanges goods or services based on self-interest and suspicion), a covenant exchanges persons and hearts based on love, loyalty, and shared life."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why a Covenant is Not Just a Contract",
                        "content": {
                            "text": "In daily commercial life, we encounter contracts: tenancy agreements, phone plans, or employment terms. If one party violates a clause, the contract is nullified.\n\nA **covenant**, however:\n- Is grounded in **sacrificial love and faithfulness** rather than mutual distrust.\n- Focuses on **identity and transformation** ('Who do we become together?') rather than mere transactional advantage ('What do I get out of this?').\n- Demands lifelong moral loyalty and mutual responsibility."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Covenant vs. Contract Architecture",
                        "content": {
                            "title": "Structural Matrix: Biblical Covenant vs. Secular Contract",
                            "caption": "A side-by-side comparative analysis of motives, sealing methods, durability, and theological implications of Berith.",
                            "svg_content": SVG_COVENANT_VS_CONTRACT
                        }
                    },
                    {
                        "type": "interactive_takeaway",
                        "title": "Key Insight: The Communal Nature of Berith",
                        "content": {
                            "text": "The Sinai Covenant was not a private, individual contract. God established it with the **entire assembly of Israel**, binding them into a cohesive spiritual and ethical commonwealth accountable to God and to each other."
                        }
                    }
                ],
                # Card 4: Curated YouTube Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: Understanding Biblical Covenants",
                        "content": {
                            "youtube_id": "7_CGP-12AE0",
                            "url": "https://www.youtube.com/watch?v=7_CGP-12AE0",
                            "description": "An engaging overview by BibleProject exploring the overarching theme of covenants in the Bible and how God partners with humanity."
                        }
                    },
                    {
                        "type": "video_reflection",
                        "title": "Video Study & Theological Reflection",
                        "content": {
                            "reflection_prompt": "As you watch the video, observe how God makes promises through covenants to redeem humanity despite human unfaithfulness. How does the Sinai Covenant build upon the Abrahamic Covenant?",
                            "key_takeaways": [
                                "God initiates covenants out of unmerited grace.",
                                "Covenants establish a relational framework where humanity reflects God's character.",
                                "Faithfulness to the covenant brings life and blessing to the entire community."
                            ]
                        }
                    }
                ],
                # Card 5: Scriptural Anchor & Core Values
                [
                    {
                        "type": "scripture_spotlight",
                        "title": "Scriptural Anchor: Exodus 19:5-6",
                        "content": {
                            "verse_text": "\"Now if you obey me fully and keep my covenant, then out of all nations you will be my treasured possession. Although the whole earth is mine, you will be for me a kingdom of priests and a holy nation.\"",
                            "reference": "Exodus 19:5-6 (NIV)",
                            "theological_meaning": "God did not choose Israel because they were powerful, but to be His 'kingdom of priests'—a nation representing God to the surrounding world and demonstrating His justice, mercy, and holiness."
                        }
                    },
                    {
                        "type": "values_application",
                        "title": "Living Values: Responsibility & Faithfulness",
                        "content": {
                            "values": [
                                {
                                    "value": "Responsibility",
                                    "description": "Entering into any covenant (with God, family, or society) brings solemn duties. Keeping our promises builds trust and social stability."
                                },
                                {
                                    "value": "Faithfulness",
                                    "description": "Remaining committed to our moral convictions and promises even when situations become demanding or inconvenient."
                                }
                            ]
                        }
                    },
                    {
                        "type": "misconception_buster",
                        "title": "Misconception Alert: The 'Private Promise' Error",
                        "content": {
                            "misconception": "A covenant is merely a private, personal promise between an isolated individual and God.",
                            "reality": "The Sinai Covenant was fundamentally communal; it forged an entire nation into a mutually responsible community governed by God's righteous laws."
                        }
                    }
                ],
                # Card 6: Formative Assessment MCQs
                [
                    {
                        "type": "interactive_quiz",
                        "title": "Formative Mastery Quiz: Nature of the Sinai Covenant",
                        "content": {
                            "questions": [
                                {
                                    "question": "What is the central difference between a secular legal contract and a biblical covenant (Berith)?",
                                    "options": [
                                        "A contract is signed by elders, while a covenant requires a public assembly.",
                                        "A contract is based on self-interest and suspicion, while a covenant is built on love, sacrifice, and lifelong faithfulness.",
                                        "A contract requires animal sacrifices, while a covenant is entirely verbal.",
                                        "There is no difference; both are identical legal agreements."
                                    ],
                                    "correct_answer": "A contract is based on self-interest and suspicion, while a covenant is built on love, sacrifice, and lifelong faithfulness.",
                                    "explanation": "Secular contracts are protective legal tools created out of mutual distrust to exchange property, whereas biblical covenants exchange persons and establish lifelong, sacred relationships sealed by sacrifice."
                                },
                                {
                                    "question": "According to Exodus 19:5-6, what special identity and mission did God offer Israel through the Sinai Covenant?",
                                    "options": [
                                        "An invincible military empire conquering all nations.",
                                        "A wealthy merchant guild controlling desert trade routes.",
                                        "A treasured possession, a kingdom of priests, and a holy nation.",
                                        "A secluded group exempted from all moral commandments."
                                    ],
                                    "correct_answer": "A treasured possession, a kingdom of priests, and a holy nation.",
                                    "explanation": "God explicitly declared that through covenant obedience, Israel would become His 'treasured possession' and a 'kingdom of priests' to showcase God's holiness to the nations."
                                }
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: The Making of the Sinai Covenant (Exodus 19:3-24)
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "The Making of the Sinai Covenant & Theophany",
            "unit_description": "Analyzing the divine proposal, the three-day physical and spiritual consecration, strict mountain boundaries, and the terrifying theophany at Mount Sinai in Exodus 19.",
            "lesson_title": "Mount Sinai: Divine Proposal, Consecration, and Theophany",
            "pages": [
                # Card 1: Photographic Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Visualizing Mount Sinai Peak at Dawn",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Mount_Sinai_Egypt.jpg",
                            "caption": "The summit of Mount Sinai in Egypt, where Moses climbed to receive God's covenant proposal and where the divine presence descended in fire.",
                            "author": "Wikimedia Commons / Mohammed Moussa",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_introduction",
                        "title": "Meeting the Holy Creator at the Mountain",
                        "content": {
                            "text": "Before God spoke His moral law to Israel, He established strict protocols of preparation. Entering into communion with the Sovereign Creator is not casual; it requires radical reverence, cleansing, and awe.\n\nIn Exodus 19, we witness how God prepared a community of millions to experience His holy presence."
                        }
                    }
                ],
                # Card 2: Divine Proposal & 3-Day Consecration
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Divine Proposal & The People's Assent",
                        "content": {
                            "text": "When Moses went up Mount Sinai, the Lord gave him this message for Israel:\n- **The Divine Reminder:** *'You yourselves have seen what I did to Egypt, and how I carried you on eagles’ wings and brought you to myself.'*\n- **The National Assent:** Moses called the elders, and the entire assembly responded unanimously: *'We will do everything the Lord has said!'* (Exodus 19:8)."
                        }
                    },
                    {
                        "type": "step_by_step_protocol",
                        "title": "The Three Requirements of Consecration (Exodus 19:10-15)",
                        "content": {
                            "intro": "For three days, the entire nation underwent rigorous preparation:",
                            "steps": [
                                {
                                    "step": "1. Washing Clothes",
                                    "meaning": "External physical washing served as a vivid visual reminder of the internal spiritual purity required to approach God."
                                },
                                {
                                    "step": "2. Abstaining from Sexual Relations",
                                    "meaning": "Temporarily setting aside physical marital pleasures to dedicate complete attention and sacred focus to the Lord."
                                },
                                {
                                    "step": "3. Setting Mountain Boundaries",
                                    "meaning": "Strict limits were marked around the mountain. Anyone—human or animal—who touched the mountain was to be executed. This taught the infinite boundary between Holy Creator and sinful creation."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Mount Sinai Reverence & Boundary Architecture",
                        "content": {
                            "title": "The Sinai Theophany, Mountain Boundaries, and Camp Consecration",
                            "caption": "A vertical spatial layout illustrating the divine fire on the peak, Moses as mediator, the boundary line, and the consecrated camp below.",
                            "svg_content": SVG_SINAI_BOUNDARIES_THEOPHANY
                        }
                    },
                    {
                        "type": "theological_insight",
                        "title": "The Principle of God's Unapproachable Holiness",
                        "content": {
                            "text": "The physical boundary around Mount Sinai was not meant to keep people from loving God, but to teach them **reverence**. God cannot be treated casually or approached with careless presumption."
                        }
                    }
                ],
                # Card 4: Curated YouTube Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Exodus & The Mount Sinai Experience",
                        "content": {
                            "youtube_id": "jH_AO08eaWA",
                            "url": "https://www.youtube.com/watch?v=jH_AO08eaWA",
                            "description": "BibleProject exploration of Exodus 19-40: How God invites Israel into covenant at Mount Sinai and establishes His presence among them."
                        }
                    },
                    {
                        "type": "video_analysis",
                        "title": "Key Insights from the Sinai Theophany",
                        "content": {
                            "points": [
                                "Theophany means a visible and audible manifestation of God to humanity.",
                                "God descends in fire and smoke to demonstrate His purity and majestic sovereignty.",
                                "Moses acts as the necessary covenant mediator standing in the gap between God and the trembling people."
                            ]
                        }
                    }
                ],
                # Card 5: The Dramatic Theophany
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Theophany on the Morning of the Third Day",
                        "content": {
                            "text": "On the third day, the camp awoke to an overwhelming sensory experience (Exodus 19:16-19):\n- **Thunder and Lightning:** Flashes illuminating dense dark storm clouds.\n- **A Piercing Trumpet Blast (Shofar):** Growing louder and louder until every person in the camp trembled with holy fear.\n- **Mount Sinai Covered in Smoke:** The Lord descended upon it in fire, and smoke billowed up like smoke from a furnace.\n- **Violent Earthquake:** The entire mountain shook violently, demonstrating the awesome presence of the Lord of all creation."
                        }
                    },
                    {
                        "type": "critical_thinking_prompt",
                        "title": "Critical Thinking: Holy Awe vs. Casual Familiarity",
                        "content": {
                            "question": "Why did God require three days of consecration and a thunderous theophany rather than appearing casually? How should this shape the way modern Christians conduct themselves during public worship and prayer?"
                        }
                    }
                ],
                # Card 6: Formative Assessment
                [
                    {
                        "type": "interactive_quiz",
                        "title": "Formative Mastery Quiz: The Making of the Sinai Covenant",
                        "content": {
                            "questions": [
                                {
                                    "question": "What penalty was decreed for any person or animal that touched the foot of Mount Sinai during the theophany?",
                                    "options": [
                                        "They were banished to the desert of Sin for seven days.",
                                        "They were put to death by stoning or with arrows.",
                                        "They were required to offer two rams as a guilt offering.",
                                        "They were assigned to wash the priests' garments."
                                    ],
                                    "correct_answer": "They were put to death by stoning or with arrows.",
                                    "explanation": "Exodus 19:12-13 explicitly commanded that whoever touched the mountain was to be put to death, underscoring the absolute holiness of God's presence."
                                },
                                {
                                    "question": "What did the physical requirement of washing clothes symbolize for the Israelites before meeting God?",
                                    "options": [
                                        "Their desire to display wealthy Egyptian linens to God.",
                                        "A sanitary measure to prevent waterborne diseases in the camp.",
                                        "An outward expression of inner spiritual cleansing and purity of heart.",
                                        "A formal military uniform inspection before marching."
                                    ],
                                    "correct_answer": "An outward expression of inner spiritual cleansing and purity of heart.",
                                    "explanation": "External cleanliness was an intentional physical ritual symbolizing internal moral and spiritual consecration before approaching the holy God."
                                }
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: The Ten Commandments (Decalogue) & Moral Law (Exodus 20:1-17)
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "The Ten Commandments & Moral Law",
            "unit_description": "Comprehensive breakdown of the Decalogue (Exodus 20:1-17), distinguishing Godward obligations from Neighborward ethics, and applying moral principles to school and community life.",
            "lesson_title": "The Decalogue: Godward Duties, Neighborward Ethics, and Modern Application",
            "pages": [
                # Card 1: Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Historic Decalogue Manuscript & Stone Tablet Tradition",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/6/65/Decalogue_parchment_by_Jitskhak_ben_Eli%27ezer_1768.jpg",
                            "caption": "An illuminated 1768 Decalogue parchment manuscript displaying the Hebrew Ten Commandments arranged in two symmetrical columns representing Godward and Neighborward duties.",
                            "author": "Wikimedia Commons / Jitskhak ben Eli'ezer",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "concept_introduction",
                        "title": "The Moral Architecture of Society",
                        "content": {
                            "text": "Out of the fire of Mount Sinai, God spoke the **Ten Commandments** (*Decalogue*, meaning 'Ten Words').\n\nThese are not mere cultural suggestions or temporary rules; they represent God's universal, immutable moral standard designed to foster reverence for God and flourishing, peaceful relationships within human society."
                        }
                    }
                ],
                # Card 2: Decalogue Structure
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two Tablets of the Law: Decalogue Structure",
                        "content": {
                            "text": "The Ten Commandments naturally divide into two interrelated dimensions:\n\n1. **Tablet I: Godward Duties (Commandments 1 to 4)**\n   - Govern humanity's direct relationship with God: exclusive worship, spiritual purity, honoring His name, and observing the Sabbath.\n\n2. **Tablet II: Neighborward Duties (Commandments 5 to 10)**\n   - Govern interpersonal and community ethics: honoring parental authority, protecting human life, safeguarding marriage, defending property, speaking truth in justice, and restraining greedy desires of the heart."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Two Tablets of the Law Architecture",
                        "content": {
                            "title": "The Decalogue: Symmetrical Structure of Godward vs. Neighborward Commandments",
                            "caption": "A structured infographic illustrating the 4 Godward commands on Tablet I and the 6 Neighborward commands on Tablet II.",
                            "svg_content": SVG_DECALOGUE_TWO_TABLETS
                        }
                    },
                    {
                        "type": "theological_insight",
                        "title": "The Inseparable Connection: Love God, Love Neighbor",
                        "content": {
                            "text": "Jesus later summarized these two tablets in Matthew 22:37-40: *'Love the Lord your God with all your heart... and love your neighbor as yourself.'* You cannot genuinely love God while mistreating your neighbor, nor can you truly love your neighbor without honoring God."
                        }
                    }
                ],
                # Card 4: Curated YouTube Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Law (Torah) Explained",
                        "content": {
                            "youtube_id": "3BGO953HunU",
                            "url": "https://www.youtube.com/watch?v=3BGO953HunU",
                            "description": "BibleProject explains the purpose of the Law (Torah) in Israel's history and how it points to righteous, flourishing community living."
                        }
                    },
                    {
                        "type": "video_reflection",
                        "title": "Reflecting on the Spirit of the Law",
                        "content": {
                            "key_points": [
                                "The commandments were given to liberated people to maintain their freedom, not to earn their salvation.",
                                "God gave the law to make Israel a beacon of justice, compassion, and truth in an ancient world filled with exploitation.",
                                "The 10th commandment (Do not covet) reveals that God cares about the internal thoughts and motives of our hearts, not just external behaviors."
                            ]
                        }
                    }
                ],
                # Card 5: Deep Dive into the 10 Commandments
                [
                    {
                        "type": "commandment_reference_grid",
                        "title": "Comprehensive Examination of the Decalogue (Exodus 20:1-17)",
                        "content": {
                            "commandments": [
                                {"num": 1, "text": "No other gods before Me", "application": "Demands absolute, undivided loyalty to Yahweh; rejects putting wealth, popularity, or power ahead of God."},
                                {"num": 2, "text": "Do not make or worship idols", "application": "Prohibits reducing God to carved images or superstitious charms; God must be worshipped in spirit and truth."},
                                {"num": 3, "text": "Do not misuse the Name of the Lord", "application": "Forbids swearing false oaths in God's name, hypocrisy, or using sacred religion for selfish deceit."},
                                {"num": 4, "text": "Remember the Sabbath day by keeping it holy", "application": "Preserves a weekly rhythm of rest, worship, and physical renewal; acknowledges God as ultimate provider."},
                                {"num": 5, "text": "Honor your father and your mother", "application": "The bridge between divine and social order; respecting parents and legitimate authority creates societal harmony."},
                                {"num": 6, "text": "Do not murder", "application": "Protects the sacred value of human life created in God's image (Imago Dei); condemns unjust killing, violence, and malice."},
                                {"num": 7, "text": "Do not commit adultery", "application": "Safeguards the sacred sanctity of marriage, marital fidelity, and emotional/sexual integrity."},
                                {"num": 8, "text": "Do not steal", "application": "Protects private property, labor rights, and mandates fair economic dealings without fraud or theft."},
                                {"num": 9, "text": "Do not give false testimony against your neighbor", "application": "Defends honesty, courtroom justice, integrity in speech, and condemns slander, perjury, and gossip."},
                                {"num": 10, "text": "Do not covet your neighbor's house, spouse, or possessions", "application": "Targets internal heart greed and toxic jealousy, which are the root causes of theft, murder, and adultery."}
                            ]
                        }
                    }
                ],
                # Card 6: Interactive Ethics Lab
                [
                    {
                        "type": "ethical_dilemma_case",
                        "title": "Real-World Ethical Dilemma: The Exam Leakage",
                        "content": {
                            "scenario": "Your best friend, Sarah, obtains an unauthorized copy of the final term national CRE exam paper from a staff assistant. She urges you to revise with her, claiming: 'Our parents have sacrificed everything for our school fees. We must score straight A's to honor our parents and bring pride to our families!'",
                            "moral_conflict": "Sarah is using the 5th Commandment ('Honor parents') as an excuse to violate the 9th Commandment (Dishonesty/Falsehood) and the 8th Commandment (Stealing intellectual property).",
                            "guided_resolution": [
                                "1. Identify the False Logic: Honoring parents can never be achieved through deceit; dishonest success dishonors parents and shatters personal integrity.",
                                "2. Apply Covenant Principles: Covenant ethics demand absolute truthfulness and trust in God's provision through honest hard work.",
                                "3. Courageous Action: Respectfully decline the leaked paper, urge your friend to discard it, and report the vulnerability to prevent unfair injustice against fellow candidates."
                            ]
                        }
                    }
                ],
                # Card 7: Formative Assessment MCQs
                [
                    {
                        "type": "interactive_quiz",
                        "title": "Formative Mastery Quiz: The Ten Commandments",
                        "content": {
                            "questions": [
                                {
                                    "question": "Which commandment specifically targets the internal desires and thoughts of the heart, acting as the root cause for other social sins?",
                                    "options": [
                                        "The 5th Commandment (Honor father and mother)",
                                        "The 6th Commandment (Do not murder)",
                                        "The 10th Commandment (Do not covet)",
                                        "The 3rd Commandment (Do not misuse God's name)"
                                    ],
                                    "correct_answer": "The 10th Commandment (Do not covet)",
                                    "explanation": "While commands 6 to 9 forbid outward actions (murder, adultery, theft, perjury), the 10th command targets covetousness—the internal greed of the heart that drives those outward sins."
                                },
                                {
                                    "question": "How are the Ten Commandments divided between the two tablets of the law?",
                                    "options": [
                                        "Tablet I contains laws for priests; Tablet II contains laws for common farmers.",
                                        "Tablet I contains Godward duties (1-4); Tablet II contains Neighborward duties (5-10).",
                                        "Tablet I contains ceremonial rituals; Tablet II contains dietary guidelines.",
                                        "Tablet I contains blessings; Tablet II contains civil punishments."
                                    ],
                                    "correct_answer": "Tablet I contains Godward duties (1-4); Tablet II contains Neighborward duties (5-10).",
                                    "explanation": "The Decalogue has two distinct sections: the first 4 commandments define our relationship with God (Godward), while commandments 5 through 10 define our social responsibilities toward our neighbor."
                                }
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: The Breaking of the Sinai Covenant (Exodus 32:1-35)
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "The Breaking of the Sinai Covenant",
            "unit_description": "Investigating the causes and tragic consequences of Israel's idolatry with the Golden Calf in Exodus 32, the failure of Aaron's leadership, and Moses' heroic intercession.",
            "lesson_title": "The Golden Calf Crisis: Leadership Failure, Idolatry, and Moses' Intercession",
            "pages": [
                # Card 1: Photographic Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Depiction of the Broken Tablets of the Law",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Moses_breaking_the_tablets_of_the_law_by_Rembrandt.jpg",
                            "caption": "Moses Breaking the Tablets of the Law (1659) by Rembrandt, capturing the tragic moment when Moses shatters the stone tablets upon witnessing Israel's idolatry.",
                            "author": "Wikimedia Commons / Rembrandt van Rijn",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "concept_introduction",
                        "title": "A Tragedy at the Foot of the Mountain",
                        "content": {
                            "text": "Barely weeks after trembling before the thunderous theophany and shouting *'All that the Lord has spoken we will do'*, Israel committed an act of catastrophic spiritual treason.\n\nIn Exodus 32, we examine how impatience, anxiety, and weak leadership caused the covenant to be shattered before the stone tablets even entered the camp."
                        }
                    }
                ],
                # Card 2: Causes of the Fall
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Catalyst: Moses' Absence & Popular Panic (Exodus 32:1-6)",
                        "content": {
                            "text": "Moses remained on the summit of Mount Sinai in prayer with God for **forty days and forty nights**.\n\nDown in the valley, the people grew anxious and impatient:\n- **Spiritual Insecurity:** Accustomed to Egyptian visible idols, they could not handle waiting on an invisible God.\n- **Demands on Aaron:** The mob surrounded Aaron, demanding: *'Come, make us gods who will go before us. As for this fellow Moses who brought us up out of Egypt, we don't know what has happened to him!'*"
                        }
                    },
                    {
                        "type": "leadership_contrast",
                        "title": "The Failure of Leadership: Aaron vs. Moses",
                        "content": {
                            "aaron_leadership": {
                                "trait": "Weak & People-Pleasing",
                                "actions": "Instead of confronting the mob, Aaron compromised. He told them to strip off their gold earrings, melted them, and carved the **Golden Calf** (resembling the Egyptian Apis bull of fertility and power), declaring a feast to the idol."
                            },
                            "moses_leadership": {
                                "trait": "Courageous & Principle-Centered",
                                "actions": "Moses was willing to confront sin directly, hold people accountable, and risk his own life to intercede for the nation."
                            }
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pathway of Covenant Breach Diagram",
                        "content": {
                            "title": "The Six-Stage Progression of Covenant Breakdown & Restoration",
                            "caption": "A flowchart tracing the spiral from Moses' 40-day delay, to mob pressure, Aaron's compromise, idolatrous revelry, shattered tablets, and Moses' intercession.",
                            "svg_content": SVG_GOLDEN_CALF_BREACH_PATHWAY
                        }
                    },
                    {
                        "type": "theological_insight",
                        "title": "The Symbolic Shattering of the Tablets",
                        "content": {
                            "text": "When Moses hurled the stone tablets to the ground at the base of the mountain, it was not merely a loss of temper; it was a **profound legal and prophetic act**. By engaging in idolatry and wild revelry, Israel had completely annulled the covenant relationship."
                        }
                    }
                ],
                # Card 4: Curated YouTube Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Golden Calf & Exodus 32",
                        "content": {
                            "youtube_id": "jH_AO08eaWA",
                            "url": "https://www.youtube.com/watch?v=jH_AO08eaWA",
                            "description": "BibleProject analysis of Exodus 32-34: Israel's heartbreaking idolatry with the Golden Calf and God's surprising response of mercy."
                        }
                    },
                    {
                        "type": "video_reflection",
                        "title": "Reflecting on Idolatry and Loyalty",
                        "content": {
                            "questions": [
                                "Why was Israel so quick to exchange the glorious Creator for a mute golden cow?",
                                "What modern 'golden calves' (such as money, social status, peer validation, or technology) tempt young people today to compromise their moral convictions?"
                            ]
                        }
                    }
                ],
                # Card 5: Moses' Intercession and Judgment
                [
                    {
                        "type": "concept_explanation",
                        "title": "Moses' Heroic Intercession (Exodus 32:7-14, 30-35)",
                        "content": {
                            "text": "When the Lord told Moses of the people's corruption and proposed to destroy them and build a new nation through Moses, Moses demonstrated selfless pastoral love:\n- **Reminding God of His Promises:** Moses pleaded based on the Abrahamic covenant.\n- **Defending God's Honor:** Moses argued that Egypt would mock God if Israel perished in the wilderness.\n- **Self-Sacrificial Love:** In Exodus 32:32, Moses prayed: *'Please forgive their sin—but if not, then blot me out of the book you have written.'*\n\nMoses put the lives of a rebellious people ahead of his own glory."
                        }
                    },
                    {
                        "type": "consequences_summary",
                        "title": "The Immediate Consequences of Sin",
                        "content": {
                            "points": [
                                "The Golden Calf was burned, ground into fine dust, thrown into the stream, and the people were forced to drink it, tasting the bitterness of their folly.",
                                "A plague struck the unrepentant rebels, demonstrating that sin always carries severe real-world consequences.",
                                "The original stone tablets lay shattered, requiring a complete restoration process."
                            ]
                        }
                    }
                ],
                # Card 6: Formative Assessment
                [
                    {
                        "type": "interactive_quiz",
                        "title": "Formative Mastery Quiz: The Breaking of the Sinai Covenant",
                        "content": {
                            "questions": [
                                {
                                    "question": "Why did Aaron fashion the Golden Calf for the Israelites at the foot of Mount Sinai?",
                                    "options": [
                                        "God commanded him to test the people's loyalty.",
                                        "Moses sent a messenger ordering him to build an altar for cattle.",
                                        "He yielded to mob pressure because the people were anxious and impatient during Moses' 40-day absence.",
                                        "He wanted to restart an Egyptian trade guild in the desert."
                                    ],
                                    "correct_answer": "He yielded to mob pressure because the people were anxious and impatient during Moses' 40-day absence.",
                                    "explanation": "Aaron failed as a leader because he succumbed to the crowd's fear, anxiety, and demands for a tangible, visible god rather than standing firm for the invisible Lord."
                                },
                                {
                                    "question": "What was the deeper symbolic meaning behind Moses shattering the stone tablets at the foot of Mount Sinai?",
                                    "options": [
                                        "He slipped on the rocks due to fatigue from descending the steep mountain.",
                                        "It legally and visually demonstrated that Israel had completely broken their covenant relationship with God.",
                                        "He wanted to hide the commandments from the people so they would not be judged.",
                                        "The stones were too heavy to carry through the dancing crowds."
                                    ],
                                    "correct_answer": "It legally and visually demonstrated that Israel had completely broken their covenant relationship with God.",
                                    "explanation": "Shattering the tablets was a formal visual act symbolizing that Israel had violated the foundation of the covenant before the ink was dry."
                                }
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: The Renewal of the Sinai Covenant (Exodus 34:1-35)
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "The Renewal of the Sinai Covenant & God's Character",
            "unit_description": "Exploring God's initiative of mercy in Exodus 34, the profound self-revelation of divine grace and justice (Exodus 34:6-7), the carving of the new tablets, and Moses' radiant face.",
            "lesson_title": "Covenant Restored: Divine Grace, Justice, and Transformed Living",
            "pages": [
                # Card 1: Photographic Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Artistic Representation: Moses with the Second Set of Tablets",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Moses_with_the_Ten_Commandments_by_Philippe_de_Champaigne.jpg",
                            "caption": "Moses with the Ten Commandments by Philippe de Champaigne (1648), depicting the renewed covenant tablets written by God's grace.",
                            "author": "Wikimedia Commons / Philippe de Champaigne",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "concept_introduction",
                        "title": "A Second Chance: The God of Restoration",
                        "content": {
                            "text": "If human contracts fail when violated, what happens when humanity shatters a divine covenant?\n\nIn Exodus 34, God reveals that His mercy is far greater than human failure. God invites Moses back up the mountain to chisel two new stone tablets and renew the covenant."
                        }
                    }
                ],
                # Card 2: God's Initiative of Mercy
                [
                    {
                        "type": "concept_explanation",
                        "title": "Carving the Second Stone Tablets (Exodus 34:1-4)",
                        "content": {
                            "text": "The Lord told Moses: *'Chisel out two stone tablets like the first ones, and I will write on them the words that were on the first tablets, which you broke.'*\n\nKey theological truths:\n- **God Initiates Restoration:** Humans broke the covenant, but God initiated the reconciliation.\n- **God's Moral Law is Immutable:** God did not lower or dilute His moral standard; He wrote the exact same Ten Commandments on the new tablets."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "God's Character Matrix Diagram",
                        "content": {
                            "title": "The Dual Character of God: Boundless Grace vs. Holy Justice (Exodus 34:6-7)",
                            "caption": "An infographic analyzing the creative balance between God's compassion, grace, and patience alongside His uncompromising justice and moral accountability.",
                            "svg_content": SVG_DIVINE_CHARACTER_REVELATION
                        }
                    },
                    {
                        "type": "theological_insight",
                        "title": "The Cornerstone of Biblical Theology",
                        "content": {
                            "text": "Exodus 34:6-7 is the most frequently quoted passage in the entire Old Testament! It forms the foundational definition of who God is: loving enough to forgive, yet holy enough to oppose evil."
                        }
                    }
                ],
                # Card 4: Curated YouTube Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Character of God (Exodus 34:6-7)",
                        "content": {
                            "youtube_id": "OMQMWXZG-bA",
                            "url": "https://www.youtube.com/watch?v=OMQMWXZG-bA",
                            "description": "BibleProject deep dive on the Character of God: How Yahweh reveals Himself as compassionate, gracious, and slow to anger."
                        }
                    },
                    {
                        "type": "video_reflection",
                        "title": "Reflecting on God's Hesed (Loyal Love)",
                        "content": {
                            "key_learnings": [
                                "Hesed is the Hebrew term for faithful, covenant-keeping love that persists even when the partner fails.",
                                "God's anger is slow and provoked only by injustice and idolatry, whereas His mercy is spontaneous and eternal.",
                                "True repentance aligns us with God's forgiving heart and leads to genuine life change."
                            ]
                        }
                    }
                ],
                # Card 5: Signs of Restoration & Radiant Face
                [
                    {
                        "type": "concept_explanation",
                        "title": "Moses' Radiant Face: The Mark of True Fellowship (Exodus 34:29-35)",
                        "content": {
                            "text": "When Moses descended Mount Sinai with the two renewed tablets, his face was **literally radiant and shining** because he had been speaking directly with God.\n- **The People's Reaction:** Aaron and the Israelites were terrified to come near him because of the supernatural brightness.\n- **The Veil:** Moses placed a veil over his face when speaking to the people, removing it only when he entered God's presence.\n- **The Spiritual Symbolism:** Genuine, prolonged fellowship with God transforms a believer's inner heart and visible countenance, reflecting God's holy light to the world."
                        }
                    }
                ],
                # Card 6: Formative Assessment
                [
                    {
                        "type": "interactive_quiz",
                        "title": "Formative Mastery Quiz: The Renewal of the Sinai Covenant",
                        "content": {
                            "questions": [
                                {
                                    "question": "What proclamation did God make about His own character when passing in front of Moses in Exodus 34:6-7?",
                                    "options": [
                                        "He is a distant ruler who only cares about strict sacrifices.",
                                        "He is compassionate and gracious, slow to anger, abounding in love, yet does not leave the guilty unpunished.",
                                        "He has abolished the Ten Commandments and replaced them with animal offerings.",
                                        "He will immediately destroy any person who commits a mistake."
                                    ],
                                    "correct_answer": "He is compassionate and gracious, slow to anger, abounding in love, yet does not leave the guilty unpunished.",
                                    "explanation": "Exodus 34:6-7 is God's foundational self-revelation, balancing infinite mercy ('compassionate, gracious, forgiving sin') with holy justice ('does not leave the guilty unpunished')."
                                },
                                {
                                    "question": "Why did Moses have to wear a veil over his face after coming down from Mount Sinai with the renewed tablets?",
                                    "options": [
                                        "He had suffered severe sunburn from the desert heat.",
                                        "His face was supernatural and brightly radiant from speaking face-to-face with God, making the people afraid.",
                                        "He was in deep mourning for the shattered golden calf.",
                                        "It was a ritual requirement to disguise the high priest."
                                    ],
                                    "correct_answer": "His face was supernatural and brightly radiant from speaking face-to-face with God, making the people afraid.",
                                    "explanation": "Exodus 34:29-35 records that Moses' skin shone with divine glory because he had conversed with Yahweh, symbolizing the transformative power of divine communion."
                                }
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6: Wilderness Tabernacle Worship & Modern Living (Exodus 25-40)
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Wilderness Tabernacle Worship & Modern Christian Living",
            "unit_description": "Studying the sacred architecture, layout, and furnishings of the Wilderness Tabernacle (Exodus 25-40), their spiritual symbolism, and transforming ancient worship principles into modern Christian living.",
            "lesson_title": "The Wilderness Tabernacle: Sacred Space, Symbolism, and Living Worship",
            "pages": [
                # Card 1: Photographic Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Full-Scale Tabernacle Replica in the Desert Landscape",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Model_of_the_Tabernacle_in_Timna_Park_Israel.jpg",
                            "caption": "A life-size reconstruction of the biblical Tabernacle in Timna Park, Israel, showing the Outer Court enclosure, the Bronze Altar, and the Tent of Meeting in the desert.",
                            "author": "Wikimedia Commons / Dr. Yehuda",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_introduction",
                        "title": "God Dwelling Among His People",
                        "content": {
                            "text": "How could a holy God live in the midst of an imperfect, nomadic people wandering through the desert?\n\nGod instructed Moses to construct the **Tabernacle** (*Mishkan*, meaning 'Dwelling Place'). It was a portable sanctuary that stood at the exact center of Israel's 12-tribe camp, demonstrating that God was traveling *with* them."
                        }
                    }
                ],
                # Card 2: Tabernacle Architecture & Stations
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Zones of the Tabernacle Sanctuary",
                        "content": {
                            "text": "The Tabernacle was designed with three concentric levels of increasing holiness and intimacy:\n\n1. **The Outer Court:**\n   - Open to all clean Israelites. Contained the **Bronze Altar** for animal sacrifices (atonement) and the **Bronze Basin** filled with water for priests to wash hands and feet (sanctification).\n\n2. **The Holy Place (Outer Room of the Tent):**\n   - Entered daily only by consecrated priests. Contained the **Golden Lampstand (Menorah)** providing perpetual light, the **Table of Showbread** holding 12 loaves symbolizing God's provision for the 12 tribes, and the **Altar of Incense** representing daily prayers.\n\n3. **The Holy of Holies (Inner Sanctuary / Most Holy Place):**\n   - Separated by a massive, richly woven **Veil**. Entered **only once a year** by the High Priest on the Day of Atonement (*Yom Kippur*). Contained the **Ark of the Covenant** capped by the **Mercy Seat** with two golden cherubim—God's earthly throne of grace."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Master Blueprint: The Tabernacle Layout & Sacred Stations",
                        "content": {
                            "title": "Architectural Plan of the Wilderness Tabernacle (Exodus 25-40)",
                            "caption": "A detailed spatial blueprint showing the Outer Court (Bronze Altar & Laver), Holy Place (Menorah, Showbread, Incense), The Veil, and Holy of Holies (Ark of the Covenant).",
                            "svg_content": SVG_TABERNACLE_SACRED_ARCHITECTURE
                        }
                    },
                    {
                        "type": "theological_insight",
                        "title": "The Pilgrimage of Worship",
                        "content": {
                            "text": "The physical movement through the Tabernacle illustrated the journey of salvation: from outside in sin -> to the sacrifice (Bronze Altar) -> through cleansing (Basin) -> into fellowship and light (Holy Place) -> into the direct presence of God (Holy of Holies)."
                        }
                    }
                ],
                # Card 4: Curated YouTube Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Curated Video: The Tabernacle & Sacred Space",
                        "content": {
                            "youtube_id": "1mFZsK08m20",
                            "url": "https://www.youtube.com/watch?v=1mFZsK08m20",
                            "description": "BibleProject explains the Tabernacle's design and how it served as a portable Eden where heaven and earth overlapped in the wilderness."
                        }
                    },
                    {
                        "type": "video_reflection",
                        "title": "Understanding Sanctuary Symbolism",
                        "content": {
                            "key_points": [
                                "The Tabernacle was decorated with garden imagery (pomegranates, blossoms, cherubim) recalling the Garden of Eden.",
                                "God desired to dwell among His people, making Himself accessible through ordained sacrificial pathways.",
                                "In the New Testament, John 1:14 states that Jesus 'became flesh and tabernacled among us.'"
                            ]
                        }
                    }
                ],
                # Card 5: Sacred Furnishings Grid & Modern Comparison
                [
                    {
                        "type": "furnishing_symbolism_matrix",
                        "title": "Symbolism of Tabernacle Furnishings & Modern Christian Equivalence",
                        "content": {
                            "comparisons": [
                                {
                                    "furnishing": "Bronze Altar (Outer Court)",
                                    "ancient_role": "Daily animal sacrifice for atonement of sin",
                                    "modern_application": "Praise for Jesus Christ's once-for-all sacrifice on the Cross; prayers of thanksgiving."
                                },
                                {
                                    "furnishing": "Bronze Basin (Laver)",
                                    "ancient_role": "Washing hands and feet before sacred ministry",
                                    "modern_application": "Baptism and daily confession of sins; maintaining pure hearts and clean hands."
                                },
                                {
                                    "furnishing": "Golden Lampstand (Menorah)",
                                    "ancient_role": "Continuous olive oil light in the darkness",
                                    "modern_application": "Walking in the light of the Holy Spirit and shining as moral lights in our school and community."
                                },
                                {
                                    "furnishing": "Table of Showbread",
                                    "ancient_role": "12 loaves eaten by priests each Sabbath",
                                    "modern_application": "Trusting God for physical and spiritual daily bread; Holy Communion / Lord's Supper."
                                },
                                {
                                    "furnishing": "Altar of Incense",
                                    "ancient_role": "Sweet aromatic smoke rising continuously",
                                    "modern_application": "Consistent morning and evening personal devotions and corporate prayer."
                                },
                                {
                                    "furnishing": "The Ark of the Covenant & Mercy Seat",
                                    "ancient_role": "Throne of God's presence; held Law, Manna, Aaron's rod",
                                    "modern_application": "Free, direct access to God's throne of grace through Christ, whose torn veil opened the way (Hebrews 10:19-22)."
                                }
                            ]
                        }
                    }
                ],
                # Card 6: Worship Journal Practicum & Living Application
                [
                    {
                        "type": "interactive_practicum",
                        "title": "Personal Worship Journal & Active Reverence Practicum",
                        "content": {
                            "instruction": "Reflect on how you participate in school chapel, church services, or family devotions. Are you a passive spectator or an active worshipper?",
                            "action_commitments": [
                                {
                                    "area": "Reverence and Punctuality",
                                    "commitment": "Arriving early, quieting my mind, and preparing my heart with prayer rather than chatting or using phones carelessly."
                                },
                                {
                                    "area": "Active Participation",
                                    "commitment": "Singing enthusiastically, following Scripture readings carefully, and taking structured notes during sermons."
                                },
                                {
                                    "area": "Integrity of Life",
                                    "commitment": "Ensuring my daily conduct outside church reflects the worship and moral holiness I profess inside."
                                }
                            ]
                        }
                    }
                ],
                # Card 7: Final Summative Assessment MCQs & Case Study
                [
                    {
                        "type": "interactive_quiz",
                        "title": "Summative Mastery Exam: Topic 1.6 The Sinai Covenant",
                        "content": {
                            "questions": [
                                {
                                    "question": "What sacred object was kept inside the Holy of Holies (Most Holy Place) in the Tabernacle?",
                                    "options": [
                                        "The Altar of Incense",
                                        "The Golden Menorah Lampstand",
                                        "The Table of Showbread",
                                        "The Ark of the Covenant"
                                    ],
                                    "correct_answer": "The Ark of the Covenant",
                                    "explanation": "The Holy of Holies contained only the Ark of the Covenant capped by the Mercy Seat and golden cherubim, representing God's throne of grace."
                                },
                                {
                                    "question": "How does the tearing of the temple veil at the death of Jesus Christ transform the wilderness Tabernacle pattern for modern Christians?",
                                    "options": [
                                        "It abolished all forms of prayer and corporate singing.",
                                        "It grants all believers direct, unhindered access to God's presence through Christ without needing an earthly high priest.",
                                        "It moved the Holy of Holies to an underground desert vault.",
                                        "It commanded Christians to rebuild the portable tent sanctuary in Jerusalem."
                                    ],
                                    "correct_answer": "It grants all believers direct, unhindered access to God's presence through Christ without needing an earthly high priest.",
                                    "explanation": "Hebrews 10:19-22 explains that Christ's sacrifice opened the veil, allowing every believer to enter boldly into God's presence at all times."
                                }
                            ]
                        }
                    },
                    {
                        "type": "structured_scenario_case",
                        "title": "Summative Ethics & Worship Case Study",
                        "content": {
                            "case_prompt": "Your classmate, Caleb, asserts: 'Since God is loving and forgiving, outward behavior during CRE prayers and chapel does not matter at all. We can dress casually, talk loudly, and joke around because God only looks at the heart.'",
                            "model_analysis": "Using the theophany of Mount Sinai (Exodus 19) and the Tabernacle holiness protocol (Exodus 25-40), explain to Caleb why true love for God must produce outward reverence, order, and active respect during community worship. Genuine inner faith naturally produces outer honor and sacred reverence for the Creator."
                        }
                    }
                ]
            ]
        }
    ]

# =============================================================================
# INGESTION EXECUTION ENGINE
# =============================================================================

def ingest_grade10_cre_topic_1_6(replace: bool = True):
    print("=" * 80)
    print("STARTING VLEARN GRADE 10 CRE TOPIC 1.6 PRODUCTION INGESTION")
    print("=" * 80)

    # 1. Resolve Grade 10 (Curriculum CBC ID: 5, Grade ID: 5)
    grade = Grade.objects.get(id=5)
    print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id}, Curriculum: {grade.curriculum_id})")

    # 2. Resolve Subject: CRE (ID: 46)
    subject = Subject.objects.get(id=46, grade=grade)
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id})")

    # 3. Create or Resolve Topic 1.6
    with transaction.atomic():
        topic, t_created = Topic.objects.get_or_create(
            subject=subject,
            order=6,
            defaults={
                "name": "Topic 1.6: The Sinai Covenant",
                "description": "Comprehensive exploration of the Sinai Covenant: covenant vs contract, divine theophany and preparation at Mount Sinai, the Ten Commandments (Decalogue), the golden calf failure, covenant renewal, and wilderness tabernacle worship.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Sinai_05-2016_img03_Mount_Sinai.jpg"
            }
        )
        if not t_created:
            topic.name = "Topic 1.6: The Sinai Covenant"
            topic.description = "Comprehensive exploration of the Sinai Covenant: covenant vs contract, divine theophany and preparation at Mount Sinai, the Ten Commandments (Decalogue), the golden calf failure, covenant renewal, and wilderness tabernacle worship."
            topic.image = "https://upload.wikimedia.org/wikipedia/commons/d/d7/Sinai_05-2016_img03_Mount_Sinai.jpg"
            topic.save()
            print(f"[*] Updated Topic 1.6: {topic.name} (ID: {topic.id})")
        else:
            print(f"[*] Created Topic 1.6: {topic.name} (ID: {topic.id})")

        # 4. Clean replace if requested
        if replace:
            print("[*] Replace mode active: Deleting existing Topic 1.6 units, lessons, blocks, and assets...")
            existing_lessons = Lesson.objects.filter(topic=topic)
            LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
            topic.learning_units.all().delete()
            topic.lessons.all().delete()

        # Build curriculum dataset
        units_data = build_topic_1_6_curriculum()

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for unit_def in units_data:
            u_order = unit_def["unit_order"]
            u_name = unit_def["unit_name"]
            u_desc = unit_def["unit_description"]
            l_title = unit_def["lesson_title"]
            pages = unit_def["pages"]

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            # Create Lesson (Published, Version 1)
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Grade 10 CRE Topic 1.6 Ingestion Agent",
                    "grade": "Grade 10",
                    "subject": "CRE",
                    "topic_order": 6,
                    "unit_order": u_order
                }
            )
            total_lessons += 1

            # Ingest Pages and Blocks
            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t1_6_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 6, "unit_order": u_order, "page": page_idx}
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

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Cards/Pages, {block_counter - 1} Blocks)")

        print("=" * 80)
        print("TOPIC 1.6 INGESTION SUMMARY:")
        print(f"  Target Topic:    {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  Units Created:   {total_units}")
        print(f"  Lessons Created: {total_lessons} (All published, v1)")
        print(f"  Pages (Cards):   {total_pages}")
        print(f"  Blocks Created:  {total_blocks}")
        print(f"  Assets Linked:   {total_assets}")
        print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_cre_topic_1_6(replace=True)
