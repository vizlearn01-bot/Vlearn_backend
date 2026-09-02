"""
VLearn CBC Grade 10 CRE — Topic 1.4: Stewardship over Creation
Production Ingestion Script

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5)
Subject: CRE (ID: 46)
Topic: Topic 1.4: Stewardship over Creation (Order: 4)

7 Discrete Learning Units & Lessons:
  1. Defining Good Stewardship (6 Cards)
  2. Biblical Basis for Stewardship: Genesis 1:26-28 (6 Cards)
  3. Biblical Basis for Stewardship: Genesis 2:15-16 (6 Cards)
  4. Principles of Good Stewardship (6 Cards)
  5. Essential Qualities of a Good Steward (6 Cards)
  6. Expressing Stewardship Through Poetry and Creative Arts (6 Cards)
  7. Documenting Good Stewardship in Daily Life and Practicum (6 Cards)
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
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

# =============================================================================
# SVG DIAGRAM DEFINITIONS
# =============================================================================

# Lesson 1: Stewardship vs Ownership
SVG_STEWARDSHIP_VS_OWNERSHIP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="ownerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#eff6ff"/>
      <stop offset="100%" stop-color="#dbeafe"/>
    </linearGradient>
    <linearGradient id="stewardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="100%" stop-color="#d1fae5"/>
    </linearGradient>
    <filter id="dropShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.1"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="480" rx="16" fill="#f8fafc"/>

  <!-- Header Banner -->
  <rect x="30" y="20" width="740" height="60" rx="12" fill="url(#headerGrad)" filter="url(#dropShadow)"/>
  <text x="400" y="44" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">STEWARDSHIP ARCHITECTURE: OWNERSHIP VS. MANAGEMENT</text>
  <text x="400" y="64" fill="#bae6fd" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">The Biblical Framework of Human Authority Under Sovereign Divine Title</text>

  <!-- Left Card: The Owner (God) -->
  <g transform="translate(30, 100)" filter="url(#dropShadow)">
    <rect width="350" height="350" rx="14" fill="url(#ownerGrad)" stroke="#3b82f6" stroke-width="2"/>
    <rect x="20" y="16" width="310" height="36" rx="8" fill="#1d4ed8"/>
    <text x="175" y="40" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">THE SOVEREIGN OWNER (GOD)</text>
    
    <circle cx="175" cy="95" r="28" fill="#bfdbfe"/>
    <text x="175" y="103" fill="#1e40af" font-family="system-ui, sans-serif" font-size="24" text-anchor="middle">👑</text>

    <!-- Key Attributes -->
    <rect x="20" y="138" width="310" height="90" rx="8" fill="#ffffff" fill-opacity="0.9"/>
    <text x="32" y="160" fill="#1e40af" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Divine Rights &amp; Reality:</text>
    <text x="32" y="180" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5">• Ultimate &amp; Perpetual Title (Psalm 24:1)</text>
    <text x="32" y="200" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5">• Sovereign Authority over all elements</text>
    <text x="32" y="220" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5">• Supreme Judge who demands accountability</text>

    <!-- Scriptural Anchor Box -->
    <rect x="20" y="240" width="310" height="90" rx="8" fill="#172554"/>
    <text x="32" y="262" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Scriptural Declaration:</text>
    <text x="32" y="282" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-style="italic">"The earth is the LORD's, and everything</text>
    <text x="32" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-style="italic">in it, the world, and all who live in it."</text>
    <text x="32" y="318" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">— Psalm 24:1</text>
  </g>

  <!-- Right Card: The Steward (Humanity) -->
  <g transform="translate(420, 100)" filter="url(#dropShadow)">
    <rect width="350" height="350" rx="14" fill="url(#stewardGrad)" stroke="#10b981" stroke-width="2"/>
    <rect x="20" y="16" width="310" height="36" rx="8" fill="#047857"/>
    <text x="175" y="40" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">THE TRUSTED STEWARD (HUMANITY)</text>
    
    <circle cx="175" cy="95" r="28" fill="#a7f3d0"/>
    <text x="175" y="103" fill="#065f46" font-family="system-ui, sans-serif" font-size="24" text-anchor="middle">🗝️</text>

    <!-- Key Attributes -->
    <rect x="20" y="138" width="310" height="90" rx="8" fill="#ffffff" fill-opacity="0.9"/>
    <text x="32" y="160" fill="#065f46" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Delegated Duties &amp; Calling:</text>
    <text x="32" y="180" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5">• Delegated Management (Day-to-day care)</text>
    <text x="32" y="200" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5">• Moral &amp; Ecological Trusteeship</text>
    <text x="32" y="220" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11.5">• Strict Obligation of Final Accountability</text>

    <!-- Scriptural Anchor Box -->
    <rect x="20" y="240" width="310" height="90" rx="8" fill="#064e3b"/>
    <text x="32" y="262" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">The Steward's Commission:</text>
    <text x="32" y="282" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-style="italic">"Now it is required that those who have</text>
    <text x="32" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-style="italic">been given a trust must prove faithful."</text>
    <text x="32" y="318" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">— 1 Corinthians 4:2</text>
  </g>

  <!-- Central Bridge Flow Indicator -->
  <g transform="translate(378, 240)">
    <circle cx="22" cy="22" r="20" fill="#0284c7" stroke="#ffffff" stroke-width="3"/>
    <text x="22" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">➔</text>
  </g>
</svg>"""

# Lesson 2: Genesis 1:26-28 Mandate Flow
SVG_GENESIS_1_MANDATE_FLOW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="g1HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#0d9488"/>
    </linearGradient>
    <linearGradient id="boxGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#eff6ff"/>
      <stop offset="100%" stop-color="#dbeafe"/>
    </linearGradient>
    <linearGradient id="boxGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="100%" stop-color="#fde68a"/>
    </linearGradient>
    <linearGradient id="boxGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="100%" stop-color="#d1fae5"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#f8fafc"/>

  <!-- Header -->
  <rect x="30" y="20" width="740" height="60" rx="12" fill="url(#g1HeaderGrad)" filter="url(#shadow)"/>
  <text x="400" y="44" fill="#ffffff" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE GENESIS 1:26-28 STEWARDSHIP MANDATE</text>
  <text x="400" y="64" fill="#ccfbf1" font-family="system-ui, sans-serif" font-size="12" font-weight="500" text-anchor="middle">From Divine Origin to Loving, Responsible Earth-Keeping (Radah &amp; Kabash)</text>

  <!-- Step 1: Imago Dei -->
  <g transform="translate(30, 100)" filter="url(#shadow)">
    <rect width="225" height="330" rx="12" fill="url(#boxGrad1)" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="12" y="14" width="201" height="32" rx="6" fill="#1d4ed8"/>
    <text x="112" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. IMAGO DEI</text>
    
    <text x="112" y="70" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">Image &amp; Likeness</text>
    <circle cx="112" cy="110" r="26" fill="#bfdbfe"/>
    <text x="112" y="118" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">✨</text>

    <rect x="12" y="150" width="201" height="160" rx="6" fill="#ffffff" fill-opacity="0.95"/>
    <text x="20" y="172" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Divine Representatives:</text>
    <text x="20" y="190" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">Endowed with moral reason,</text>
    <text x="20" y="206" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">creativity, and love.</text>
    <text x="20" y="232" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mirroring Character:</text>
    <text x="20" y="250" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">Humanity represents God's</text>
    <text x="20" y="266" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">benevolent rule to all living</text>
    <text x="20" y="282" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">creatures on earth.</text>
  </g>

  <!-- Step 2: Divine Blessing -->
  <g transform="translate(285, 100)" filter="url(#shadow)">
    <rect width="230" height="330" rx="12" fill="url(#boxGrad2)" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="12" y="14" width="206" height="32" rx="6" fill="#d97706"/>
    <text x="115" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. DIVINE BLESSING</text>
    
    <text x="115" y="70" fill="#b45309" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">Fruitfulness &amp; Multiplicity</text>
    <circle cx="115" cy="110" r="26" fill="#fde68a"/>
    <text x="115" y="118" fill="#b45309" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">🌱</text>

    <rect x="12" y="150" width="206" height="160" rx="6" fill="#ffffff" fill-opacity="0.95"/>
    <text x="20" y="172" fill="#92400e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• "Be Fruitful &amp; Fill":</text>
    <text x="20" y="190" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">A divine gift authorizing</text>
    <text x="20" y="206" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">human flourishing.</text>
    <text x="20" y="232" fill="#92400e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sustainable Growth:</text>
    <text x="20" y="250" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">Populating the earth must</text>
    <text x="20" y="266" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">honor ecological carrying</text>
    <text x="20" y="282" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">capacity and resources.</text>
  </g>

  <!-- Step 3: Dominion & Subduing -->
  <g transform="translate(545, 100)" filter="url(#shadow)">
    <rect width="225" height="330" rx="12" fill="url(#boxGrad3)" stroke="#10b981" stroke-width="1.5"/>
    <rect x="12" y="14" width="201" height="32" rx="6" fill="#047857"/>
    <text x="112" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. RADAH &amp; KABASH</text>
    
    <text x="112" y="70" fill="#065f46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">Dominion &amp; Subduing</text>
    <circle cx="112" cy="110" r="26" fill="#a7f3d0"/>
    <text x="112" y="118" fill="#047857" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">🛡️</text>

    <rect x="12" y="150" width="201" height="160" rx="6" fill="#ffffff" fill-opacity="0.95"/>
    <text x="20" y="172" fill="#064e3b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Radah (Dominion):</text>
    <text x="20" y="190" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">Loving leadership and</text>
    <text x="20" y="206" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">protection (NOT tyranny).</text>
    <text x="20" y="232" fill="#064e3b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Kabash (Subdue):</text>
    <text x="20" y="250" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">Cultivating order and care,</text>
    <text x="20" y="266" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">NOT stripping forests bare.</text>
  </g>
</svg>"""

# Lesson 3: Shabad & Shamar Balance Scale
SVG_SHABAD_SHAMAR_BALANCE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="headerGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#15803d"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.1"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#f8fafc"/>

  <!-- Header -->
  <rect x="30" y="20" width="740" height="60" rx="12" fill="url(#headerGrad3)" filter="url(#shadow3)"/>
  <text x="400" y="44" fill="#ffffff" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">GENESIS 2:15 STEWARDSHIP EQUILIBRIUM: SHABAD &amp; SHAMAR</text>
  <text x="400" y="64" fill="#bbf7d0" font-family="system-ui, sans-serif" font-size="12" font-weight="500" text-anchor="middle">The Sacred Balance Between Productive Cultivation and Ecological Protection</text>

  <!-- Central Scale Fulcrum / Pillar -->
  <polygon points="400,160 380,390 420,390" fill="#334155"/>
  <rect x="350" y="390" width="100" height="16" rx="4" fill="#1e293b"/>
  <circle cx="400" cy="160" r="14" fill="#f59e0b" stroke="#ffffff" stroke-width="3"/>

  <!-- Scale Crossbar -->
  <line x1="160" y1="160" x2="640" y2="160" stroke="#475569" stroke-width="8" stroke-linecap="round"/>

  <!-- Left Scale Pan: SHABAD (Work It / Cultivate) -->
  <line x1="160" y1="160" x2="110" y2="240" stroke="#94a3b8" stroke-width="2"/>
  <line x1="160" y1="160" x2="210" y2="240" stroke="#94a3b8" stroke-width="2"/>
  
  <g transform="translate(45, 230)" filter="url(#shadow3)">
    <rect width="230" height="185" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <rect x="10" y="10" width="210" height="30" rx="6" fill="#2563eb"/>
    <text x="115" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SHABAD (עָבַד) — "WORK IT"</text>
    
    <text x="16" y="60" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Cultivation &amp; Productive Service:</text>
    <text x="16" y="80" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Tilling the soil for food crops</text>
    <text x="16" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Sustainable technological innovation</text>
    <text x="16" y="120" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Developing natural resources</text>
    <text x="16" y="140" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Active, energetic service to land</text>
    
    <rect x="10" y="152" width="210" height="24" rx="4" fill="#dbeafe"/>
    <text x="115" y="168" fill="#1e40af" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Goal: Fruitfulness &amp; Vitality</text>
  </g>

  <!-- Right Scale Pan: SHAMAR (Take Care Of / Protect) -->
  <line x1="640" y1="160" x2="590" y2="240" stroke="#94a3b8" stroke-width="2"/>
  <line x1="640" y1="160" x2="690" y2="240" stroke="#94a3b8" stroke-width="2"/>

  <g transform="translate(525, 230)" filter="url(#shadow3)">
    <rect width="230" height="185" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <rect x="10" y="10" width="210" height="30" rx="6" fill="#059669"/>
    <text x="115" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SHAMAR (שָׁמַר) — "GUARD IT"</text>
    
    <text x="16" y="60" fill="#065f46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Preservation &amp; Watchmanship:</text>
    <text x="16" y="80" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Guarding water wells and rivers</text>
    <text x="16" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Soil conservation &amp; reforestation</text>
    <text x="16" y="120" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Preventing industrial pollution</text>
    <text x="16" y="140" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Protecting biodiversity &amp; habitats</text>
    
    <rect x="10" y="152" width="210" height="24" rx="4" fill="#d1fae5"/>
    <text x="115" y="168" fill="#065f46" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Goal: Sustainable Preservation</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <rect x="230" y="426" width="340" height="36" rx="8" fill="#1e293b"/>
  <text x="400" y="449" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">HARMONY = WORKING WITHOUT DESTROYING</text>
</svg>"""

# Lesson 4: Four Pillars of Stewardship
SVG_FOUR_PILLARS_STEWARDSHIP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="pillHeader" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4338ca"/>
      <stop offset="100%" stop-color="#6366f1"/>
    </linearGradient>
    <filter id="shadowPill" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#f8fafc"/>

  <!-- Top Banner -->
  <rect x="30" y="18" width="740" height="54" rx="10" fill="url(#pillHeader)" filter="url(#shadowPill)"/>
  <text x="400" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE FOUR PILLARS OF GOOD STEWARDSHIP</text>
  <text x="400" y="60" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">The Indispensable Foundation of Christian Environmental &amp; Resource Ethics</text>

  <!-- Pillar 1 -->
  <g transform="translate(30, 90)" filter="url(#shadowPill)">
    <rect width="170" height="340" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="10" y="12" width="150" height="36" rx="6" fill="#1d4ed8"/>
    <text x="85" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PILLAR 1</text>
    <text x="85" y="42" fill="#bfdbfe" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">GOD'S OWNERSHIP</text>
    
    <circle cx="85" cy="78" r="20" fill="#bfdbfe"/>
    <text x="85" y="85" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🌍</text>

    <rect x="10" y="108" width="150" height="120" rx="6" fill="#ffffff"/>
    <text x="16" y="126" fill="#1e3a8a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The Core Principle:</text>
    <text x="16" y="142" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">God holds absolute,</text>
    <text x="16" y="156" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">eternal title deed to</text>
    <text x="16" y="170" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">all creation, nature,</text>
    <text x="16" y="184" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">and living creatures</text>
    <text x="16" y="198" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">(Psalm 24:1).</text>

    <rect x="10" y="238" width="150" height="82" rx="6" fill="#1e40af"/>
    <text x="16" y="254" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Ethical Mandate:</text>
    <text x="16" y="270" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">We own nothing</text>
    <text x="16" y="284" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">permanently; all is</text>
    <text x="16" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">held in sacred trust.</text>
  </g>

  <!-- Pillar 2 -->
  <g transform="translate(220, 90)" filter="url(#shadowPill)">
    <rect width="170" height="340" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
    <rect x="10" y="12" width="150" height="36" rx="6" fill="#047857"/>
    <text x="85" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PILLAR 2</text>
    <text x="85" y="42" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">HUMAN RESPONSIBILITY</text>
    
    <circle cx="85" cy="78" r="20" fill="#a7f3d0"/>
    <text x="85" y="85" fill="#047857" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🤝</text>

    <rect x="10" y="108" width="150" height="120" rx="6" fill="#ffffff"/>
    <text x="16" y="126" fill="#064e3b" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The Core Principle:</text>
    <text x="16" y="142" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">God actively delegated</text>
    <text x="16" y="156" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">management duty to</text>
    <text x="16" y="170" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">human hands using</text>
    <text x="16" y="184" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">wisdom and creative</text>
    <text x="16" y="198" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">intellect.</text>

    <rect x="10" y="238" width="150" height="82" rx="6" fill="#065f46"/>
    <text x="16" y="254" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Ethical Mandate:</text>
    <text x="16" y="270" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">Passivity is a sin;</text>
    <text x="16" y="284" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">we must take active</text>
    <text x="16" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">restorative action.</text>
  </g>

  <!-- Pillar 3 -->
  <g transform="translate(410, 90)" filter="url(#shadowPill)">
    <rect width="170" height="340" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="10" y="12" width="150" height="36" rx="6" fill="#d97706"/>
    <text x="85" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PILLAR 3</text>
    <text x="85" y="42" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">ACCOUNTABILITY</text>
    
    <circle cx="85" cy="78" r="20" fill="#fde68a"/>
    <text x="85" y="85" fill="#d97706" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⚖️</text>

    <rect x="10" y="108" width="150" height="120" rx="6" fill="#ffffff"/>
    <text x="16" y="126" fill="#92400e" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The Core Principle:</text>
    <text x="16" y="142" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">Every person will</text>
    <text x="16" y="156" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">render an account</text>
    <text x="16" y="170" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">to God for how they</text>
    <text x="16" y="184" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">treated the earth and</text>
    <text x="16" y="198" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">resources.</text>

    <rect x="10" y="238" width="150" height="82" rx="6" fill="#92400e"/>
    <text x="16" y="254" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Ethical Mandate:</text>
    <text x="16" y="270" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">Greed &amp; destruction</text>
    <text x="16" y="284" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">face divine moral</text>
    <text x="16" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">judgment.</text>
  </g>

  <!-- Pillar 4 -->
  <g transform="translate(600, 90)" filter="url(#shadowPill)">
    <rect width="170" height="340" rx="10" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="10" y="12" width="150" height="36" rx="6" fill="#be185d"/>
    <text x="85" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PILLAR 4</text>
    <text x="85" y="42" fill="#fbcfe8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">COMMON BENEFIT</text>
    
    <circle cx="85" cy="78" r="20" fill="#fbcfe8"/>
    <text x="85" y="85" fill="#be185d" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🌿</text>

    <rect x="10" y="108" width="150" height="120" rx="6" fill="#ffffff"/>
    <text x="16" y="126" fill="#9d174d" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The Core Principle:</text>
    <text x="16" y="142" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">Creation is designed</text>
    <text x="16" y="156" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">for the mutual health,</text>
    <text x="16" y="170" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">equity, and sustained</text>
    <text x="16" y="184" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">benefit of present</text>
    <text x="16" y="198" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">&amp; future generations.</text>

    <rect x="10" y="238" width="150" height="82" rx="6" fill="#9d174d"/>
    <text x="16" y="254" fill="#fbcfe8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Ethical Mandate:</text>
    <text x="16" y="270" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">Defend downstream</text>
    <text x="16" y="284" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">neighbors &amp; future</text>
    <text x="16" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9">children from harm.</text>
  </g>
</svg>"""

# Lesson 5: Qualities Wheel
SVG_QUALITIES_OF_STEWARD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="wheelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f766e"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>
    <filter id="shadowQ" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#f8fafc"/>

  <!-- Header -->
  <rect x="30" y="18" width="740" height="54" rx="10" fill="url(#wheelGrad)" filter="url(#shadowQ)"/>
  <text x="400" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ESSENTIAL MORAL QUALITIES OF A GOOD STEWARD</text>
  <text x="400" y="60" fill="#cffafe" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Scriptural Virtues Governing Environmental and Resource Management</text>

  <!-- Central Hub -->
  <circle cx="400" cy="275" r="54" fill="#0f766e" stroke="#ffffff" stroke-width="4" filter="url(#shadowQ)"/>
  <text x="400" y="270" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">CHRISTIAN</text>
  <text x="400" y="286" fill="#5eead4" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">STEWARD</text>

  <!-- 6 Outer Quality Nodes -->
  <!-- 1. Selflessness (Top-Left) -->
  <g transform="translate(40, 95)" filter="url(#shadowQ)">
    <rect width="210" height="100" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="12" y="24" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Selflessness (Phil 2:3-4)</text>
    <text x="12" y="44" fill="#334155" font-family="system-ui, sans-serif" font-size="10">Prioritizing the health of</text>
    <text x="12" y="58" fill="#334155" font-family="system-ui, sans-serif" font-size="10">creation &amp; neighbors ahead of</text>
    <text x="12" y="72" fill="#334155" font-family="system-ui, sans-serif" font-size="10">short-term personal profit.</text>
  </g>

  <!-- 2. Humility (Top-Right) -->
  <g transform="translate(550, 95)" filter="url(#shadowQ)">
    <rect width="210" height="100" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
    <text x="12" y="24" fill="#047857" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Humility (Micah 6:8)</text>
    <text x="12" y="44" fill="#334155" font-family="system-ui, sans-serif" font-size="10">Serving as a gentle caretaker</text>
    <text x="12" y="58" fill="#334155" font-family="system-ui, sans-serif" font-size="10">under God, rather than an</text>
    <text x="12" y="72" fill="#334155" font-family="system-ui, sans-serif" font-size="10">arrogant, destructive owner.</text>
  </g>

  <!-- 3. Wisdom (Middle-Left) -->
  <g transform="translate(40, 220)" filter="url(#shadowQ)">
    <rect width="210" height="100" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="12" y="24" fill="#b45309" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Wisdom (Prov 3:19)</text>
    <text x="12" y="44" fill="#334155" font-family="system-ui, sans-serif" font-size="10">Applying scientific foresight,</text>
    <text x="12" y="58" fill="#334155" font-family="system-ui, sans-serif" font-size="10">careful planning, and sound</text>
    <text x="12" y="72" fill="#334155" font-family="system-ui, sans-serif" font-size="10">judgment to preserve nature.</text>
  </g>

  <!-- 4. Patience (Middle-Right) -->
  <g transform="translate(550, 220)" filter="url(#shadowQ)">
    <rect width="210" height="100" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.5"/>
    <text x="12" y="24" fill="#be185d" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Patience (Gal 6:9)</text>
    <text x="12" y="44" fill="#334155" font-family="system-ui, sans-serif" font-size="10">Persevering in conservation</text>
    <text x="12" y="58" fill="#334155" font-family="system-ui, sans-serif" font-size="10">duties (e.g. nurturing trees)</text>
    <text x="12" y="72" fill="#334155" font-family="system-ui, sans-serif" font-size="10">even when growth is slow.</text>
  </g>

  <!-- 5. Tolerance (Bottom-Left) -->
  <g transform="translate(40, 345)" filter="url(#shadowQ)">
    <rect width="210" height="100" rx="8" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="12" y="24" fill="#6d28d9" font-family="system-ui, sans-serif" font-size="12" font-weight="700">5. Forbearance (Col 3:13)</text>
    <text x="12" y="44" fill="#334155" font-family="system-ui, sans-serif" font-size="10">Resolving group disputes</text>
    <text x="12" y="58" fill="#334155" font-family="system-ui, sans-serif" font-size="10">peacefully without destroying</text>
    <text x="12" y="72" fill="#334155" font-family="system-ui, sans-serif" font-size="10">property or community unity.</text>
  </g>

  <!-- 6. Cheerful Giving (Bottom-Right) -->
  <g transform="translate(550, 345)" filter="url(#shadowQ)">
    <rect width="210" height="100" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
    <text x="12" y="24" fill="#c2410c" font-family="system-ui, sans-serif" font-size="12" font-weight="700">6. Cheerful Giving (2 Cor 9:7)</text>
    <text x="12" y="44" fill="#334155" font-family="system-ui, sans-serif" font-size="10">Gladly volunteering time,</text>
    <text x="12" y="58" fill="#334155" font-family="system-ui, sans-serif" font-size="10">labor, and resources to clean</text>
    <text x="12" y="72" fill="#334155" font-family="system-ui, sans-serif" font-size="10">and protect God's world.</text>
  </g>
</svg>"""

# Lesson 6: Poetry Structure
SVG_POETIC_FRAMEWORK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="poetGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>
    <filter id="shadowP" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#f8fafc"/>

  <!-- Header -->
  <rect x="30" y="18" width="740" height="54" rx="10" fill="url(#poetGrad)" filter="url(#shadowP)"/>
  <text x="400" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE ANATOMY OF A STEWARDSHIP POEM</text>
  <text x="400" y="60" fill="#f3e8ff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Transforming Biblical Theology into Creative Ecological Advocacy</text>

  <!-- Stanza 1 Card -->
  <g transform="translate(30, 95)" filter="url(#shadowP)">
    <rect width="225" height="330" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="10" y="12" width="205" height="32" rx="6" fill="#1d4ed8"/>
    <text x="112" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STANZA 1: DIVINE PRAISE</text>
    
    <rect x="10" y="54" width="205" height="110" rx="6" fill="#ffffff"/>
    <text x="18" y="74" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Thematic Focus:</text>
    <text x="18" y="92" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• God's supreme ownership</text>
    <text x="18" y="108" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Majestic beauty of creation</text>
    <text x="18" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Rivers, hills, wildlife awe</text>
    <text x="18" y="140" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Biblical anchor: Psalm 24:1</text>

    <rect x="10" y="174" width="205" height="140" rx="6" fill="#172554"/>
    <text x="18" y="194" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sample Line:</text>
    <text x="18" y="214" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">"The hills of green, the rivers</text>
    <text x="18" y="228" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">bright and clear,</text>
    <text x="18" y="246" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">Are leased to us by God,</text>
    <text x="18" y="260" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">who holds them dear."</text>
  </g>

  <!-- Stanza 2 Card -->
  <g transform="translate(285, 95)" filter="url(#shadowP)">
    <rect width="230" height="330" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
    <rect x="10" y="12" width="210" height="32" rx="6" fill="#047857"/>
    <text x="115" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STANZA 2: THE MANDATE</text>
    
    <rect x="10" y="54" width="210" height="110" rx="6" fill="#ffffff"/>
    <text x="18" y="74" fill="#065f46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Thematic Focus:</text>
    <text x="18" y="92" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Hands-on labor &amp; duty</text>
    <text x="18" y="108" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Shabad (Work) &amp; Shamar (Keep)</text>
    <text x="18" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Protecting the vulnerable soil</text>
    <text x="18" y="140" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Biblical anchor: Genesis 2:15</text>

    <rect x="10" y="174" width="210" height="140" rx="6" fill="#064e3b"/>
    <text x="18" y="194" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sample Line:</text>
    <text x="18" y="214" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">"With Shamar's shield and</text>
    <text x="18" y="228" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">Shabad's serving hand,</text>
    <text x="18" y="246" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">To heal the wounds and</text>
    <text x="18" y="260" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">beautify the land."</text>
  </g>

  <!-- Stanza 3 Card -->
  <g transform="translate(545, 95)" filter="url(#shadowP)">
    <rect width="225" height="330" rx="10" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>
    <rect x="10" y="12" width="205" height="32" rx="6" fill="#e11d48"/>
    <text x="112" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STANZA 3: THE PLEDGE</text>
    
    <rect x="10" y="54" width="205" height="110" rx="6" fill="#ffffff"/>
    <text x="18" y="74" fill="#9f1239" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Thematic Focus:</text>
    <text x="18" y="92" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Denouncing greed &amp; waste</text>
    <text x="18" y="108" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Personal moral vow</text>
    <text x="18" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Rising as faithful youth stewards</text>
    <text x="18" y="140" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Biblical anchor: Micah 6:8</text>

    <rect x="10" y="174" width="205" height="140" rx="6" fill="#881337"/>
    <text x="18" y="194" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sample Line:</text>
    <text x="18" y="214" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">"We pledge to rise, with wisdom,</text>
    <text x="18" y="228" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">grace, and pride,</text>
    <text x="18" y="246" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">As faithful stewards, with</text>
    <text x="18" y="260" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-style="italic">the Lord our Guide."</text>
  </g>
</svg>"""

# Lesson 7: Bento Grid Diary Log
SVG_DAILY_STEWARDSHIP_LOG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="logGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
    <filter id="shadowL" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#f8fafc"/>

  <!-- Header -->
  <rect x="30" y="18" width="740" height="54" rx="10" fill="url(#logGrad)" filter="url(#shadowL)"/>
  <text x="400" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ONE-WEEK DAILY STEWARDSHIP LOG: 4-QUADRANT MATRIX</text>
  <text x="400" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Practical Documentation Framework for Grade 10 Christian Religious Education</text>

  <!-- Quadrant 1: Resource Management (Top Left) -->
  <g transform="translate(30, 90)" filter="url(#shadowL)">
    <rect width="355" height="170" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="12" y="12" width="331" height="28" rx="6" fill="#1d4ed8"/>
    <text x="177" y="31" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. RESOURCE CONSERVATION (GOD'S PROVISION)</text>
    
    <text x="20" y="62" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Daily Reflection Prompts:</text>
    <text x="20" y="82" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I turn off dripping taps and save clean water?</text>
    <text x="20" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I switch off unused lights and power devices?</text>
    <text x="20" y="118" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I prevent food wastage during family meals?</text>
    <rect x="12" y="132" width="331" height="26" rx="4" fill="#dbeafe"/>
    <text x="177" y="149" fill="#1e40af" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action Goal: Zero Waste &amp; Wise Energy Usage</text>
  </g>

  <!-- Quadrant 2: Environmental Care (Top Right) -->
  <g transform="translate(415, 90)" filter="url(#shadowL)">
    <rect width="355" height="170" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
    <rect x="12" y="12" width="331" height="28" rx="6" fill="#047857"/>
    <text x="177" y="31" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. ENVIRONMENTAL CARE (EARTH KEEPING)</text>
    
    <text x="20" y="62" fill="#065f46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Daily Reflection Prompts:</text>
    <text x="20" y="82" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I collect plastic litter from the school compound?</text>
    <text x="20" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I plant, weed, or water flowers/trees?</text>
    <text x="20" y="118" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I treat domestic &amp; wild animals with kindness?</text>
    <rect x="12" y="132" width="331" height="26" rx="4" fill="#d1fae5"/>
    <text x="177" y="149" fill="#065f46" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action Goal: Active Compound Beautification</text>
  </g>

  <!-- Quadrant 3: Personal Gifts & Time (Bottom Left) -->
  <g transform="translate(30, 280)" filter="url(#shadowL)">
    <rect width="355" height="170" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="12" y="12" width="331" height="28" rx="6" fill="#d97706"/>
    <text x="177" y="31" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. PERSONAL GIFTS &amp; TIME MANAGEMENT</text>
    
    <text x="20" y="62" fill="#b45309" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Daily Reflection Prompts:</text>
    <text x="20" y="82" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I dedicate planned study hours to my homework?</text>
    <text x="20" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I avoid excessive screen time &amp; social media?</text>
    <text x="20" y="118" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I maintain and protect my school uniform &amp; books?</text>
    <rect x="12" y="132" width="331" height="26" rx="4" fill="#fde68a"/>
    <text x="177" y="149" fill="#92400e" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action Goal: Disciplined Talent Stewardship</text>
  </g>

  <!-- Quadrant 4: Community Service (Bottom Right) -->
  <g transform="translate(415, 280)" filter="url(#shadowL)">
    <rect width="355" height="170" rx="10" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="12" y="12" width="331" height="28" rx="6" fill="#be185d"/>
    <text x="177" y="31" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. CHEERFUL COMMUNITY INVOLVEMENT</text>
    
    <text x="20" y="62" fill="#9d174d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Daily Reflection Prompts:</text>
    <text x="20" y="82" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I volunteer to wash dishes or clean the house?</text>
    <text x="20" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I assist a classmate who was struggling in study?</text>
    <text x="20" y="118" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Did I perform chores with joy rather than grumbling?</text>
    <rect x="12" y="132" width="331" height="26" rx="4" fill="#fbcfe8"/>
    <text x="177" y="149" fill="#9d174d" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action Goal: Selfless, Joyful Service to Others</text>
  </g>
</svg>"""

# =============================================================================
# CLEANING UTILITIES
# =============================================================================

def clean_text(text: str) -> str:
    """Strips bracket citations, internal formatting tags, and standardizes list markers."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [1.4], [223]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal visual/passage tags e.g. [VISUAL: ...], [BIBLE PASSAGE: ...], [KEY VERSE]
    text = re.sub(r'\[(?:VISUAL|BIBLE PASSAGE|KEY VERSE|CRITICAL THINKING|REAL WORLD APPLICATION|INTERACTION|IMAGE|DIAGRAM|TABLE|INFOGRAPHIC)[^\]]*\]', '', text, flags=re.IGNORECASE)
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
# CURRICULUM LESSON DATA SPECIFICATION
# =============================================================================

def build_topic_1_4_curriculum():
    """Returns the complete 7-lesson pedagogical data for Topic 1.4: Stewardship over Creation."""
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Defining Good Stewardship
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Defining Good Stewardship",
            "unit_description": "Exploration of stewardship as management, responsibility, and trusteeship under God's ultimate ownership. Contrasting owners and stewards in practical life.",
            "lesson_title": "Defining Good Stewardship",
            "pages": [
                # Card 1: Discovery Hook & Wikimedia Photographic Anchor
                [
                    {
                        "type": "suggested_image",
                        "title": "Sustainable Tea Plantation Management in Kericho, Kenya",
                        "content": {
                            "title": "Human Cultivation and Responsible Resource Management",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Tea_plantations_in_Kericho%2C_Kenya.jpg",
                            "caption": "Vast tea estates in Kericho, Kenya illustrate how human beings manage fertile agricultural landscapes while serving as trusted caretakers of natural resources.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Essence of Stewardship",
                        "content": {
                            "goals": [
                                "Define the terms **steward** and **good stewardship** from a biblical worldview.",
                                "Analyze the three core pillars of stewardship: **management, responsibility, and trusteeship**.",
                                "Contrast the rights of an **owner** with the delegated duties of a **steward**.",
                                "Apply stewardship principles to family, school, and community responsibilities."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introductory Scenario: The Farm Manager",
                        "content": {
                            "text": "Imagine a wealthy landowner who travels abroad for five years. Before departing, she hands over the keys to her modern commercial farm—including high-tech tractors, hundreds of dairy cattle, and fertile maize fields—to a young manager.\n\nShe gives one clear instruction:\n> *\"I am giving you full authority to cultivate, run, and manage this farm. But remember—it is not yours. When I return, I expect to see how you have cared for my property and made it flourish.\"*\n\nIf the manager neglects the cattle, sells off the farm machinery for quick personal cash, and allows toxic chemicals to pollute the water well, he has failed catastrophically. He forgot the most fundamental truth: **he is not the owner, but a trusted steward**."
                        }
                    }
                ],
                # Card 2: Core Concept & Scriptural Foundations
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Pillars of Biblical Stewardship",
                        "content": {
                            "text": "In Christian Religious Education, stewardship is not merely an environmental slogan; it is a foundational spiritual calling defined by three essential elements:\n\n1. **Management:** The active, daily oversight and productive direction of resources, living things, and environments that belong to God.\n2. **Responsibility:** The profound moral, social, and spiritual duty to nurture, protect, and make fruitful the assets placed in your custody.\n3. **Trusteeship:** Holding resources in sacred trust on behalf of the Owner, acting faithfully in accordance with the Owner's purpose rather than selfish desires."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Good Stewardship over Creation",
                        "content": {
                            "term": "Good Stewardship over Creation",
                            "definition": "The responsible, loving, and careful management of God's earth and all living creatures, recognizing that the earth belongs sovereignly to God, and humanity is commissioned to preserve, protect, and sustainably develop it for His glory and the mutual benefit of all.",
                            "scripture": "1 Corinthians 4:2 — 'Now it is required that those who have been given a trust must prove faithful.'"
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Stewardship Architecture: Management vs. Ownership",
                        "content": {
                            "title": "Owner vs. Steward Structural Matrix",
                            "caption": "A visual framework contrasting God's supreme title and perpetual ownership against humanity's delegated authority and accountability.",
                            "svg_content": SVG_STEWARDSHIP_VS_OWNERSHIP
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Owner vs. Steward: Key Distinctions",
                        "content": {
                            "headers": ["Dimension", "The Sovereign Owner (God)", "The Trusted Steward (Humanity)"],
                            "rows": [
                                ["Title & Rights", "Holds absolute, original, and eternal title deed", "Holds delegated, temporary management authority"],
                                ["Authority Level", "Supreme authority to set moral boundaries and laws", "Operational authority executed within the Owner's rules"],
                                ["Resource Origin", "Created all things ex nihilo (out of nothing)", "Receives all resources, talents, and time as gifts"],
                                ["Accountability", "Demands accounting; judges faithful vs unfaithful care", "Must render a strict accounting for every resource used"]
                            ]
                        }
                    }
                ],
                # Card 4: Curated Educational Video & Reflection
                [
                    {
                        "type": "suggested_video",
                        "title": "The Biblical Theology of Creation and Stewardship",
                        "content": {
                            "title": "BibleProject: Humanity and God's Good Creation",
                            "youtube_id": "G_KnXv7mK6k",
                            "url": "https://www.youtube.com/watch?v=G_KnXv7mK6k",
                            "description": "An animated exploration of how biblical narratives depict humans as royal stewards called to partner with God in caring for the earth."
                        }
                    },
                    {
                        "type": "real_world_example",
                        "title": "Everyday Stewards: School and Family Roles",
                        "content": {
                            "title": "Recognizing Stewardship in Daily Life",
                            "text": "You do not need to manage a massive estate to practice stewardship today:\n- **The School Prefect:** Entrusted with leadership over classmates and school property. They do not own the school and are held accountable by the school administration.\n- **Managing Pocket Money:** Entrusted with financial resources by your parents to purchase school items. Spending money wisely on books rather than wasting it is good stewardship.\n- **Caring for Siblings:** When entrusted with the safety and care of younger siblings while parents are away."
                        }
                    }
                ],
                # Card 5: Common Misconceptions & Ethical Scenario
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconceptions Surrounding Stewardship",
                        "content": {
                            "misconception": "Stewardship means human beings have zero authority or freedom to use natural resources.",
                            "correction": "Stewardship does not mean passive non-use; it encourages creative, productive, and sustainable development while strictly guarding against destructive exploitation.",
                            "why_it_matters": "Believing stewardship forbids resource utilization leads to poverty and neglect, whereas true stewardship creates thriving, sustainable communities."
                        }
                    },
                    {
                        "type": "ethical_scenario",
                        "title": "Ethical Dilemma: The Community Water Borehole",
                        "content": {
                            "scenario": "A community borehole was drilled with donor funds and placed under a youth committee. One committee member proposes selling water at exorbitant prices to poor neighbors to build a private recreation lounge for the committee.",
                            "question": "How does this proposal violate the fundamental definition of stewardship?",
                            "guided_resolution": "The proposal violates stewardship because the borehole was given in trusteeship for the common benefit of the community. Using public trust for selfish personal enrichment contradicts the duty of a faithful manager."
                        }
                    }
                ],
                # Card 6: Knowledge Check & Lesson Synthesis
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Owner vs Steward",
                        "content": {
                            "question": "Which of the following statements represents the most accurate distinction between an owner and a steward in biblical theology?",
                            "options": [
                                "A steward has absolute right to dispose of resources however they wish.",
                                "A steward manages resources belonging to another and must render an account to the owner.",
                                "An owner must perform all manual labor alone without delegating tasks.",
                                "A steward only cares for spiritual matters, while an owner manages physical property."
                            ],
                            "correct_answer": 1,
                            "explanation": "Option B is correct. The defining mark of a steward is holding delegated management authority over property belonging to an owner, accompanied by the moral requirement of accountability."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 1 Summary: The Steward's Identity",
                        "content": {
                            "text": "- **God is the Sovereign Owner** of the universe and all its contents (Psalm 24:1).\n- **Humanity is commissioned as Stewards** entrusted with management, responsibility, and trusteeship.\n- **Accountability is mandatory**: Every steward must eventually show how faithfully they handled what was entrusted to them."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Biblical Basis for Stewardship (Genesis 1:26-28)
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Biblical Basis for Stewardship (Genesis 1:26-28)",
            "unit_description": "Understanding human identity in the Image of God (Imago Dei) and the divine mandate to exercise dominion (Radah) and subdue the earth (Kabash) as benevolent caretakers.",
            "lesson_title": "Biblical Basis for Stewardship: Genesis 1:26-28",
            "pages": [
                # Card 1: Hook & Photographic Anchor
                [
                    {
                        "type": "suggested_image",
                        "title": "Wildlife and Habitat Harmony in Amboseli, Kenya",
                        "content": {
                            "title": "Protecting Biodiversity Under Human Dominion",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/43/Amboseli_elephant.jpg",
                            "caption": "An African elephant roaming protected savannah in Amboseli National Park, Kenya, demonstrating human responsibility to protect and preserve God's diverse animal kingdom.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Genesis 1 Mandate",
                        "content": {
                            "goals": [
                                "Explain the theological meaning of being created in the **Image of God (Imago Dei)**.",
                                "Analyze the biblical mandate in **Genesis 1:26-28**.",
                                "Differentiate between the true biblical meaning of **dominion (Radah)** and destructive exploitation.",
                                "Examine the meaning of **subduing the earth (Kabash)** in terms of orderly, life-giving development."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Human Identity and the Divine Mandate",
                        "content": {
                            "text": "Have you ever wondered why human beings have such an immense, transformative impact on planet Earth compared to all other living creatures? We build civilizations, cultivate vast agricultural landscapes, and manage natural ecosystems.\n\nThe Christian faith traces this unique responsibility directly to Genesis 1, where God creates humankind as the pinnacle of His earthly creation and confers upon them a specific royal mandate."
                        }
                    }
                ],
                # Card 2: Scripture Reading & Linguistic Analysis
                [
                    {
                        "type": "concept_explanation",
                        "title": "Genesis 1:26-28 Scriptural Text",
                        "content": {
                            "text": "> *\"Then God said, 'Let us make mankind in our image, in our likeness, so that they may rule over the fish in the sea and the birds in the sky, over the livestock and all the wild animals, and over all the creatures that move along the ground.'*\n>\n> *So God created mankind in his own image, in the image of God he created them; male and female he created them.*\n>\n> *God blessed them and said to them, 'Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the sky and over every living creature that moves on the ground.'\"*\n> — **Genesis 1:26-28**"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Theological Concept: Imago Dei",
                        "content": {
                            "term": "Imago Dei (Image of God)",
                            "definition": "The doctrine that humanity was uniquely created with moral reasoning, creativity, spiritual awareness, and capacity for love, enabling them to reflect God's holy character and represent His benevolent rule on earth.",
                            "implication": "Because humans represent God, their rule over creation must mirror God's own character—bringing life, order, justice, and protection."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Genesis 1:26-28 Stewardship Mandate Architecture",
                        "content": {
                            "title": "Imago Dei, Blessing, and Responsible Dominion Flow",
                            "caption": "A structured flowchart showing the progression from divine identity to life-affirming environmental leadership.",
                            "svg_content": SVG_GENESIS_1_MANDATE_FLOW
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Deciphering Hebrew Terms: Radah and Kabash",
                        "content": {
                            "text": "To prevent severe misinterpretations, we must examine the original Hebrew vocabulary used in Genesis 1:\n\n- **Radah (רָדָה — 'Rule / Dominion'):** In ancient biblical culture, a good king's rule was judged by whether he protected the weak, fostered peace, and ensured prosperity. *Radah* is a call to **loving leadership and protective care**, not arrogant tyranny or ruthless exploitation.\n- **Kabash (כָּבַשׁ — 'Subdue'):** Refers to cultivating wilderness, bringing harmony out of chaos, and harnessing natural potential for food, shelter, and community well-being. It means turning barren ground into fruitful gardens, never turning fruitful land into a barren desert."
                        }
                    }
                ],
                # Card 4: Educational Video & Critical Thinking
                [
                    {
                        "type": "suggested_video",
                        "title": "Understanding the Image of God and Dominion",
                        "content": {
                            "title": "BibleProject: Image of God (Imago Dei)",
                            "youtube_id": "YbipxDV_flc",
                            "url": "https://www.youtube.com/watch?v=YbipxDV_flc",
                            "description": "Visual study explaining how the Image of God confers a royal commission to manage creation with justice and wisdom."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Critical Comparison: Exploitation vs. Stewardship",
                        "content": {
                            "text": "Consider how different attitudes impact the environment:\n\n### 1. Destructive Exploitation (Distorted Dominion)\n- Clear-cutting an indigenous rainforest for short-term charcoal profit.\n- Leaving hillsides bare, leading to massive soil erosion, mudslides, and lost habitats.\n- Treating nature as an expendable commodity to be looted.\n\n### 2. Biblical Stewardship (True Dominion)\n- Harvesting mature timber selectively while planting multiple native tree seedlings.\n- Constructing terraces to preserve soil and nurturing biodiversity.\n- Treating nature as God's sacred handiwork to be developed sustainably for generations."
                        }
                    }
                ],
                # Card 5: Interactive Ethical Scenario & Guided Reflection
                [
                    {
                        "type": "ethical_scenario",
                        "title": "Community Scenario: The Sand Harvesting Crisis",
                        "content": {
                            "scenario": "A local contractor offers cash payments to villagers to scoop sand continuously from the local riverbed. Within months, the river dries up, water tables drop, and downstream farmers lose their irrigation water.",
                            "question": "Using Genesis 1:26-28, evaluate the contractor's actions. Did they exercise true dominion (*Radah*)?",
                            "guided_resolution": "No. The contractor engaged in destructive exploitation. True dominion mirrors God's life-giving character; destroying the riverbed strips life from the ecosystem and harms neighboring communities."
                        }
                    }
                ],
                # Card 6: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Meaning of Radah",
                        "content": {
                            "question": "What is the true biblical meaning of humanity's 'dominion' (Radah) over creation in Genesis 1:28?",
                            "options": [
                                "Humanity has unrestricted permission to destroy nature for selfish economic profit.",
                                "Humanity is called to exercise loving, responsible leadership that protects and nurtures creation as God's representatives.",
                                "Humanity should completely avoid touching or farming any natural resources.",
                                "Animals and plants have greater authority over the earth than human beings."
                            ],
                            "correct_answer": 1,
                            "explanation": "Option B is correct. Dominion (*Radah*) in the biblical text denotes benevolent, protective leadership mirroring God's character, not destructive exploitation."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 2 Summary: Imago Dei & Royal Mandate",
                        "content": {
                            "text": "- **Created in God's Image (Imago Dei):** Humans represent God's character on earth.\n- **Dominion (*Radah*):** A royal commission of protective leadership, not tyrannical abuse.\n- **Subduing (*Kabash*):** Creative, orderly cultivation of the earth for sustainable human thriving."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Biblical Basis for Stewardship (Genesis 2:15-16)
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Biblical Basis for Stewardship (Genesis 2:15-16)",
            "unit_description": "The Gardener's commission in Genesis 2:15. Detailed theological analysis of Shabad (working/serving) and Shamar (guarding/protecting), and freedom within moral boundaries.",
            "lesson_title": "Biblical Basis for Stewardship: Genesis 2:15-16",
            "pages": [
                # Card 1: Discovery Hook & Photographic Anchor
                [
                    {
                        "type": "suggested_image",
                        "title": "Reforestation and Forest Conservation in the Mau Forest, Kenya",
                        "content": {
                            "title": "Working and Guarding the Earth in Practice",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Tree_planting_in_Kenya.jpg",
                            "caption": "Kenyan youth planting indigenous seedlings in a community reforestation campaign, exemplifying the dual biblical mandate to cultivate (*Shabad*) and preserve (*Shamar*) the land.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Gardener's Commission",
                        "content": {
                            "goals": [
                                "Examine the practical commission of humanity in **Genesis 2:15-17**.",
                                "Analyze the theological meaning of the Hebrew concepts **Shabad (Work/Till/Serve)** and **Shamar (Guard/Protect/Keep)**.",
                                "Explain the balance between **human freedom and moral boundaries** in creation.",
                                "Conduct an environmental audit applying Genesis 2:15 to your school or home."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Gardener's Calling",
                        "content": {
                            "text": "While Genesis 1 presents a grand, cosmic perspective of creation, Genesis 2 zooms in with intimate detail. Here, we encounter the first human placed in a physical garden with a practical, hands-on job description.\n\nWork is not a curse or an afterthought; from the very beginning, God designed humanity to find dignity, joy, and purpose in caring for the earth."
                        }
                    }
                ],
                # Card 2: Scripture & Theological Vocabulary
                [
                    {
                        "type": "concept_explanation",
                        "title": "Genesis 2:15-17 Scriptural Text",
                        "content": {
                            "text": "> *\"The Lord God took the man and put him in the Garden of Eden to work it and take care of it. And the Lord God commanded the man, 'You are free to eat from any tree in the garden; but you must not eat from the tree of the knowledge of good and evil, for when you eat from it you will certainly die.'\"*\n> — **Genesis 2:15-17**"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "The Dual Formula: Shabad & Shamar",
                        "content": {
                            "term": "Shabad & Shamar",
                            "definition": "The complementary Hebrew verbs in Genesis 2:15 defining the complete stewardship duty:\n1. Shabad (עָבַד): 'To work, serve, or till'—active cultivation and creative service to the soil.\n2. Shamar (שָׁמַר): 'To guard, keep, protect, or preserve'—acting as a protective watchman against decay and destruction.",
                            "synthesis": "True stewardship requires both working the land productively and preserving its long-term ecological vitality."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Genesis 2:15 Equilibrium: The Shabad-Shamar Balance Scale",
                        "content": {
                            "title": "Sustainable Development Balance Framework",
                            "caption": "A balance scale illustrating how productive cultivation (*Shabad*) and protective conservation (*Shamar*) maintain ecological equilibrium.",
                            "svg_content": SVG_SHABAD_SHAMAR_BALANCE
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Freedom with Moral Boundaries",
                        "content": {
                            "text": "In Genesis 2:16-17, God grants Adam immense freedom: *\"You are free to eat from any tree in the garden...\"*, but immediately establishes a clear moral limit: *\"...but you must not eat from the tree of the knowledge of good and evil.\"*\n\n### The Stewardship Principle\n- **Human authority is not absolute**: Humanity does not possess autonomy to exploit nature without restraint.\n- **Respecting Natural Limits**: Nature has boundaries established by God. Overfishing, deforestation, and water pollution exceed these boundaries and bring destruction.\n- **Accountability**: Accepting God's moral boundaries is the cornerstone of true stewardship."
                        }
                    }
                ],
                # Card 4: Curated Video & School Environmental Audit
                [
                    {
                        "type": "suggested_video",
                        "title": "Creation Care and Environmental Justice",
                        "content": {
                            "title": "Christian Care for Creation: Theology in Practice",
                            "youtube_id": "r8b-bO4wGkY",
                            "url": "https://www.youtube.com/watch?v=r8b-bO4wGkY",
                            "description": "Insightful documentary exploring practical Christian environmental projects in Africa, focusing on reforestation and clean water."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The School Compound Environmental Audit",
                        "content": {
                            "intro": "Apply the Genesis 2:15 formula (*Shabad* and *Shamar*) in your school this week:",
                            "steps": [
                                {"title": "Step 1: 'Working It' (Shabad)", "description": "Cultivate the school agriculture garden, tend flower beds, and maintain clean learning spaces."},
                                {"title": "Step 2: 'Guarding It' (Shamar) - Water Conservation", "description": "Inspect all school taps and storage tanks; immediately report or fix dripping valves to save clean water."},
                                {"title": "Step 3: 'Guarding It' (Shamar) - Waste Management", "description": "Sort school garbage into organic compost and recyclable plastics, preventing plastic burning."},
                                {"title": "Step 4: 'Guarding It' (Shamar) - Energy Stewardship", "description": "Switch off lights and computers in unoccupied classrooms to eliminate energy waste."}
                            ]
                        }
                    }
                ],
                # Card 5: Common Misconceptions & Case Application
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconceptions About Environmental Work",
                        "content": {
                            "misconception": "Physical agricultural work and picking up school litter are demeaning, low-status punishments.",
                            "correction": "In Genesis 2:15, manual labor and caring for the earth was humanity's very first noble, God-given calling before sin entered the world.",
                            "why_it_matters": "Understanding this elevates farm work, sanitation, and conservation into honorable acts of divine service."
                        }
                    }
                ],
                # Card 6: Knowledge Check & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Genesis 2:15 Terms",
                        "content": {
                            "question": "Which Hebrew word in Genesis 2:15 specifically emphasizes guarding, preserving, and protecting creation from destruction?",
                            "options": [
                                "Radah",
                                "Shabad",
                                "Shamar",
                                "Kabash"
                            ],
                            "correct_answer": 2,
                            "explanation": "Option C is correct. *Shamar* means to guard, protect, keep, or watch over, whereas *Shabad* means to work or serve, *Radah* means to rule/lead, and *Kabash* means to subdue."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 3 Summary: The Garden Mandate",
                        "content": {
                            "text": "- **Genesis 2:15 Core Formula:** Cultivate (*Shabad*) and Guard (*Shamar*).\n- **Work is a Divine Calling:** Caring for creation is a noble, sacred service.\n- **Bounded Freedom:** We must respect ecological and moral limits set by God."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Principles of Good Stewardship
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Principles of Good Stewardship",
            "unit_description": "The four foundational pillars of stewardship: God's Sovereign Ownership, Human Responsibility, Accountability to God, and Common Benefit / Sustainability.",
            "lesson_title": "The Four Principles of Good Stewardship",
            "pages": [
                # Card 1: Discovery Hook & Wikimedia Photographic Anchor
                [
                    {
                        "type": "suggested_image",
                        "title": "River Ecosystem Protection in Mount Kenya National Park",
                        "content": {
                            "title": "Preserving Water Towers for the Common Benefit",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Mount_Kenya_scenery.jpg",
                            "caption": "The pristine water towers of Mount Kenya provide fresh water to millions of citizens downstream, demonstrating that good stewardship safeguards resources for the benefit of all.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Four Pillars",
                        "content": {
                            "goals": [
                                "Identify and explain the **four key principles of good stewardship**.",
                                "Analyze **Psalm 24:1** as the scriptural bedrock for divine ownership.",
                                "Evaluate the relationship between **human responsibility and personal accountability**.",
                                "Apply the principle of **common benefit and intergenerational equity** to modern industrial and community challenges."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Pillars of a Strong Structure",
                        "content": {
                            "text": "If you wish to construct a durable, multi-story building, you must rest it upon solid, reinforced foundation pillars. If even one pillar is cracked or missing, the entire edifice collapses.\n\nIn the same way, the Christian practice of environmental and resource stewardship is built upon four unshakable biblical principles."
                        }
                    }
                ],
                # Card 2: Detailed Breakdown of the 4 Principles
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Pillars of Stewardship Explained",
                        "content": {
                            "text": "### Pillar 1: Sovereign Ownership Belongs to God\n- **The Biblical Truth:** God is the creator and perpetual titleholder of all reality (Psalm 24:1: *\"The earth is the Lord's, and everything in it...\"*).\n- **Practical Implication:** We are caretakers, not sovereign owners. We cannot treat land or water as disposable commodities.\n\n### Pillar 2: Responsibility Delegated to Humanity\n- **The Biblical Truth:** God did not automate creation's care; He entrusted it to human intelligence, conscience, and labor.\n- **Practical Implication:** When environments deteriorate due to litter or erosion, we cannot remain passive bystanders.\n\n### Pillar 3: Accountability to God\n- **The Biblical Truth:** Humanity does not operate without oversight. We will give an account of how we managed our resources (Romans 14:12).\n- **Practical Implication:** Greed, wastefulness, and environmental poisoning are moral sins against God.\n\n### Pillar 4: Common Benefit & Sustainability\n- **The Biblical Truth:** Resources were created to sustain all living creatures and future generations equitably.\n- **Practical Implication:** No corporation or individual has the right to poison shared water or destroy forests for selfish enrichment."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Architectural Framework: The Four Pillars of Stewardship",
                        "content": {
                            "title": "Four Pillars Supporting Christian Resource Ethics",
                            "caption": "A visual structural diagram showing Divine Ownership, Human Responsibility, Accountability, and Common Benefit.",
                            "svg_content": SVG_FOUR_PILLARS_STEWARDSHIP
                        }
                    }
                ],
                # Card 4: Video Integration & Ethical Scenario
                [
                    {
                        "type": "suggested_video",
                        "title": "Biblical Ecology and Intergenerational Justice",
                        "content": {
                            "title": "Stewardship and Sustainability: A Theological Perspective",
                            "youtube_id": "r8b-bO4wGkY",
                            "url": "https://www.youtube.com/watch?v=r8b-bO4wGkY",
                            "description": "Educational lecture on how biblical principles of ownership and accountability directly inform sustainable modern resource policies."
                        }
                    },
                    {
                        "type": "ethical_scenario",
                        "title": "Applied Scenario: The River Factory Violation",
                        "content": {
                            "scenario": "A textile dyeing factory upstream discharges untreated toxic chemical waste directly into the local river at night to save processing costs. Downstream, school children drink the water and become ill, while local fish die.",
                            "question": "Which of the four stewardship pillars has this company violated?",
                            "guided_resolution": "The factory violated ALL four pillars:\n1. Pillar 1 (God's Ownership): Disgraced and poisoned water created by God.\n2. Pillar 2 (Human Responsibility): Failed in their moral duty to manage industrial processes safely.\n3. Pillar 3 (Accountability): Ignored their moral accountability to God and society.\n4. Pillar 4 (Common Benefit): Sacrificed the health of downstream communities for selfish corporate profit."
                        }
                    }
                ],
                # Card 5: Common Misconceptions & Discussion
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconceptions on Private Property",
                        "content": {
                            "misconception": "If I hold a legal title deed to a plot of land, I have the moral right to destroy it or poison its soil.",
                            "correction": "Human title deeds are legal arrangements under civil law; before God, all land is held in sacred trusteeship and must not be destroyed to the detriment of neighbors or future generations.",
                            "why_it_matters": "Upholding God's sovereign ownership ensures environmental laws and community rights protect shared water, air, and soil."
                        }
                    }
                ],
                # Card 6: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Stewardship Pillars",
                        "content": {
                            "question": "A community youth group establishes a tree nursery, planting 5,000 indigenous trees along deforested riverbanks. Which stewardship principle is directly demonstrated?",
                            "options": [
                                "Human Responsibility and Common Benefit",
                                "Selfish exploitation of communal property",
                                "Passive withdrawal from environmental issues",
                                "Ignoring God's sovereign title over the river"
                            ],
                            "correct_answer": 0,
                            "explanation": "Option A is correct. Active reforestation directly embodies Pillar 2 (Human Responsibility to care for creation) and Pillar 4 (Common Benefit by restoring clean water and soil for the whole community)."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 4 Summary: The Four Pillars",
                        "content": {
                            "text": "- **Pillar 1:** God holds Sovereign Ownership (Psalm 24:1).\n- **Pillar 2:** Human Responsibility is active, intelligent, and non-negotiable.\n- **Pillar 3:** Moral Accountability is required of every person.\n- **Pillar 4:** Common Benefit protects current and future generations."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: Essential Qualities of a Good Steward
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Essential Qualities of a Good Steward",
            "unit_description": "Scriptural examination of six core moral virtues: Selflessness, Humility, Wisdom, Patience/Long-Suffering, Forbearance/Tolerance, and Cheerful Giving.",
            "lesson_title": "Essential Qualities of a Good Steward",
            "pages": [
                # Card 1: Discovery Hook & Wikimedia Photographic Anchor
                [
                    {
                        "type": "suggested_image",
                        "title": "Community Tree Planting Initiative in Western Kenya",
                        "content": {
                            "title": "Selfless Labor and Cheerful Service in Creation Care",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Tree_planting_activity.jpg",
                            "caption": "Volunteers working under the hot sun to plant seedlings for community schools, embodying cheerful giving, patience, and humility.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Character in Action",
                        "content": {
                            "goals": [
                                "Analyze the **six essential moral qualities** of a good steward from biblical scripture.",
                                "Connect specific scripture passages (**Philippians 2, Micah 6, Proverbs 3, Galatians 6, Colossians 3, 2 Corinthians 9**) to environmental actions.",
                                "Distinguish between superficial compliance and authentic, heartfelt Christian stewardship.",
                                "Resolve interpersonal and environmental conflicts through stewardship virtues."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Character Behind the Action",
                        "content": {
                            "text": "A person may possess all the scientific knowledge in the world about environmental biology, but if they lack moral character, they will still act out of selfish greed.\n\nGood stewardship is not merely a set of technical skills; it is a matter of the **heart, attitude, and moral virtues** we bring to our duties."
                        }
                    }
                ],
                # Card 2: Scripture Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Scriptural Matrix of Stewardship Qualities",
                        "content": {
                            "headers": ["Moral Quality", "Key Bible Verse", "Biblical Meaning", "Youth Practical Application"],
                            "rows": [
                                ["Selflessness", "Philippians 2:3-4", "Putting others' needs and creation's health ahead of selfish ambition.", "Sharing school lab equipment fairly without hoarding."],
                                ["Humility", "Micah 6:8", "Recognizing our place as caretakers rather than arrogant masters.", "Doing manual compound cleaning chores without pride."],
                                ["Wisdom", "Proverbs 3:19", "Applying foresight and sound judgment to preserve resources.", "Planning study time carefully and avoiding wasteful habits."],
                                ["Patience (Long-suffering)", "Galatians 6:9", "Persevering diligently even when results take long to appear.", "Watering and protecting tree seedlings for months until mature."],
                                ["Forbearance (Tolerance)", "Colossians 3:13", "Exercising restraint, forgiveness, and peace in group work.", "Resolving classroom project disputes amicably."],
                                ["Cheerful Giving", "2 Corinthians 9:7", "Gladly offering time, energy, and resources with a joyful heart.", "Volunteering joyfully during community clean-up days."]
                            ]
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Virtue Architecture: The 6 Qualities of a Steward Wheel",
                        "content": {
                            "title": "Six Core Virtues of the Christian Steward",
                            "caption": "A circular diagram mapping Selflessness, Humility, Wisdom, Patience, Forbearance, and Cheerful Giving around the Christian calling.",
                            "svg_content": SVG_QUALITIES_OF_STEWARD
                        }
                    }
                ],
                # Card 4: Educational Video & Character Vignette
                [
                    {
                        "type": "suggested_video",
                        "title": "Biblical Character and Virtues in Practice",
                        "content": {
                            "title": "The Fruit of the Spirit and Christian Virtues",
                            "youtube_id": "r8b-bO4wGkY",
                            "url": "https://www.youtube.com/watch?v=r8b-bO4wGkY",
                            "description": "Exploration of biblical virtues and how patience, humility, and selflessness transform daily interactions with people and nature."
                        }
                    },
                    {
                        "type": "ethical_scenario",
                        "title": "Classroom Case Study: Wamalwa vs. Atieno",
                        "content": {
                            "scenario": "During school agriculture practicals, the class is tasked with clearing weeds from the vegetable garden under hot sunshine.\n- **Wamalwa** grumbles loudly, only works when the teacher walks past, drops his dirty tools in the mud, and complains about the heat.\n- **Atieno** works diligently, assists a struggling classmate with their row, washes and stores all garden tools neatly, and remarks cheerfully: *'We will enjoy sweet cabbages in our dining hall next month!'*",
                            "question": "Analyze both students using the 6 qualities of a good steward.",
                            "guided_resolution": "Atieno demonstrated **Selflessness** (helping her classmate), **Patience** (persevering through physical labor), and **Cheerful Giving** (focusing on the future benefit for others). Wamalwa exhibited selfishness, impatience, and an absence of accountability."
                        }
                    }
                ],
                # Card 5: Common Misconceptions
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconceptions Regarding Stewardship Virtues",
                        "content": {
                            "misconception": "Humility means being weak, passive, and unable to take decisive environmental leadership.",
                            "correction": "Biblical humility is strength under control; it means acknowledging God's authority and fearlessly defending creation from injustice without pride or arrogance.",
                            "why_it_matters": "True humility inspires courageous environmental advocates like Wangari Maathai who protected Kenya's forests."
                        }
                    }
                ],
                # Card 6: Knowledge Check & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Stewardship Virtues",
                        "content": {
                            "question": "Which scripture explicitly urges believers not to grow weary in doing good, emphasizing patience and perseverance in stewardship responsibilities?",
                            "options": [
                                "Philippians 2:3-4",
                                "Galatians 6:9",
                                "Colossians 3:13",
                                "Proverbs 3:19"
                            ],
                            "correct_answer": 1,
                            "explanation": "Option B is correct. Galatians 6:9 states: 'Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up.'"
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 5 Summary: Character as the Core",
                        "content": {
                            "text": "- **Good Stewardship requires inward virtue**, not just outward compliance.\n- **The 6 Virtues:** Selflessness, Humility, Wisdom, Patience, Forbearance, and Cheerful Giving.\n- **Scriptural Rooting:** Grounded in the New and Old Testament teachings of Christ and the Prophets."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6: Expressing Stewardship Through Poetry & Creative Arts
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Expressing Stewardship Through Poetry",
            "unit_description": "Using creative writing and poetic expression to advocate for creation care, synthesize theological truths, and inspire community conservation.",
            "lesson_title": "Expressing Stewardship Through Poetry and Creative Arts",
            "pages": [
                # Card 1: Discovery Hook & Wikimedia Photographic Anchor
                [
                    {
                        "type": "suggested_image",
                        "title": "Majestic Kenyan Landscape: The Great Rift Valley",
                        "content": {
                            "title": "The Majesty of God's Natural World",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/0/05/Great_Rift_Valley_view_Kenya.jpg",
                            "caption": "The breathtaking vista of the Great Rift Valley in Kenya inspires poetic praise, celebrating divine creation as described in Psalm 104 and Psalm 24.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Power of Poetic Expression",
                        "content": {
                            "goals": [
                                "Explain how poetry and creative arts have been used historically in Christian worship to celebrate creation (e.g. Psalms).",
                                "Analyze the structural anatomy of a stewardship poem (Praise, Mandate, and Pledge).",
                                "Compose an original 3-stanza stewardship poem on the theme *'Guardians of the Earth: Our Sacred Trust'*.",
                                "Use creative expression to advocate for environmental justice in your community."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Art and Poetry Matter in Faith",
                        "content": {
                            "text": "Sometimes, factual lists and prose cannot fully express our deepest emotions of awe, thanksgiving, and grief over environmental degradation.\n\nThroughout biblical history, God's people used poetry, psalms, and hymns to express their devotion. King David, the prophets, and Christian writers composed poems to praise the Creator and call people back to righteous living."
                        }
                    }
                ],
                # Card 2: Guided Poetic Composition Framework
                [
                    {
                        "type": "step_process",
                        "title": "How to Structure a 3-Stanza Stewardship Poem",
                        "content": {
                            "intro": "Follow this 3-stanza theological blueprint when composing your poem:",
                            "steps": [
                                {"title": "Stanza 1: The Creator's Sovereign Majesty (Praise)", "description": "Celebrate the beauty, variety, and divine ownership of nature (Psalm 24:1). Highlight mountains, rivers, wildlife, and stars."},
                                {"title": "Stanza 2: The Sacred Mandate & The Wounded Earth (Lament & Duty)", "description": "Describe humanity's duty to cultivate (*Shabad*) and protect (*Shamar*), contrasting this with the sorrow of pollution, deforestation, and greed."},
                                {"title": "Stanza 3: The Steward's Solemn Pledge (Commitment)", "description": "Declare a personal and collective vow to rise as faithful caretakers, choosing wisdom, humility, and action."}
                            ]
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Poetic Architecture: 3-Stanza Stewardship Flow",
                        "content": {
                            "title": "Anatomy of an Advocacy Poem",
                            "caption": "A structured diagram illustrating the thematic progression from Divine Praise to The Mandate and The Pledge.",
                            "svg_content": SVG_POETIC_FRAMEWORK
                        }
                    }
                ],
                # Card 4: Curated Educational Poem & Analysis
                [
                    {
                        "type": "concept_explanation",
                        "title": "Model Poem: 'The Owner's Garden'",
                        "content": {
                            "text": "Read this model poem carefully:\n\n> **The Owner's Garden**\n>\n> *The hills of green, the rivers bright and clear,*\n> *Are leased to us by God, who holds them dear.*\n> *We own no stone, no leaf, no soaring bird,*\n> *All speak of Him, the Maker of the Word.*\n>\n> *He put us in the soil to work and keep,*\n> *To guard the fields before we go to sleep.*\n> *With Shamar's shield, and Shabad's serving hand,*\n> *To heal the wounds and beautify the land.*\n>\n> *No more of greed that strips the forest bare,*\n> *No more of waste that poisons clean, sweet air.*\n> *We pledge to rise, with wisdom, grace, and pride,*\n> *As faithful stewards, with the Lord our Guide.*"
                        }
                    },
                    {
                        "type": "real_world_example",
                        "title": "Group Activity: Poetry Recitation & Advocacy",
                        "content": {
                            "title": "Advocacy Through Spoken Word",
                            "text": "In pairs, recite *'The Owner's Garden'* aloud with dynamic rhythm and expressive vocal tone. Note how terms like *Shamar* and *Shabad* transform ancient Hebrew concepts into modern environmental passion."
                        }
                    }
                ],
                # Card 5: Common Misconceptions
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconceptions About Creative Expression in CRE",
                        "content": {
                            "misconception": "Poetry is merely entertainment and has no real impact on environmental conservation.",
                            "correction": "Poetry and creative arts stir human emotions, challenge cultural apathy, and inspire communities to take real-world action far more effectively than dry statistics alone.",
                            "why_it_matters": "Engaging the arts empowers young people to become passionate environmental ambassadors."
                        }
                    }
                ],
                # Card 6: Knowledge Check & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Poetic Structure",
                        "content": {
                            "question": "In the 3-stanza stewardship poetry framework, what is the primary thematic focus of the second stanza?",
                            "options": [
                                "Listing scientific names of plant species",
                                "Connecting human responsibility (Shabad and Shamar) to protecting the earth from greed and destruction",
                                "Expressing total hopelessness about the future of the planet",
                                "Asking for money to purchase commercial real estate"
                            ],
                            "correct_answer": 1,
                            "explanation": "Option B is correct. Stanza 2 focuses on the human mandate to cultivate and protect, contrasting faithful stewardship with the destructive impacts of pollution and greed."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 6 Summary: Art as Advocacy",
                        "content": {
                            "text": "- **Poetry connects theology to heart and action**.\n- **3-Part Structure:** Divine Praise (Ownership) -> Sacred Duty (Mandate) -> Moral Pledge (Commitment).\n- **Christian tradition** rich in poetic creation praise (Psalms 19, 24, 104)."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 7: Documenting Good Stewardship in Daily Life & Practicum
        # ---------------------------------------------------------------------
        {
            "unit_order": 7,
            "unit_name": "Documenting Good Stewardship in Daily Life",
            "unit_description": "Implementing and documenting daily stewardship through a structured One-Week Log across Resource Conservation, Environmental Care, Time/Gifts, and Community Service.",
            "lesson_title": "Documenting Good Stewardship in Daily Life and Practicum",
            "pages": [
                # Card 1: Discovery Hook & Wikimedia Photographic Anchor
                [
                    {
                        "type": "suggested_image",
                        "title": "Student Environmental Club Activity in Nairobi, Kenya",
                        "content": {
                            "title": "Hands-On Environmental Action in Kenyan Schools",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Clean_up_campaign_in_Kenya.jpg",
                            "caption": "Secondary school students in Kenya participating in an active compound clean-up and tree maintenance activity, transforming CRE lessons into lived reality.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Living the Stewardship Calling",
                        "content": {
                            "goals": [
                                "Establish a structured **One-Week Daily Stewardship Log** across 4 key life categories.",
                                "Record daily actions of resource conservation, environmental protection, time management, and community service.",
                                "Analyze personal progress and identify areas for ethical growth as a Christian steward.",
                                "Synthesize the complete learning outcomes of Topic 1.4: Stewardship over Creation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Living the Concept Daily",
                        "content": {
                            "text": "Stewardship is not an academic theory to be memorized for an examination and then forgotten. It is a lifelong, daily lifestyle that shapes our habits, choices, and treatment of others and the planet.\n\nTo bridge the gap between classroom theory and practical Christian living, each learner will maintain a structured one-week diary log."
                        }
                    }
                ],
                # Card 2: The 4-Category Diary Framework
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Categories of Daily Stewardship",
                        "content": {
                            "text": "### 1. Resource Management (God's Material Provision)\n- Closing dripping water taps; using water sparingly at home and school.\n- Switching off lights and electronics when leaving a room; avoiding food waste.\n\n### 2. Environmental Care (Earth Keeping)\n- Picking up and properly sorting plastic litter; planting, watering, or weeding plants.\n- Treating domestic and wild animals with gentleness and respect.\n\n### 3. Personal Responsibilities (Managing God-Given Gifts & Time)\n- Completing school assignments promptly; organizing personal study schedules.\n- Protecting personal school uniform, textbooks, and equipment.\n\n### 4. Cheerful Community Involvement (Selfless Service)\n- Assisting family with household chores (cooking, cleaning, washing dishes) without grumbling.\n- Helping a classmate or neighbor in need with a cheerful, loving attitude."
                        }
                    }
                ],
                # Card 3: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Daily Practicum: 4-Quadrant Stewardship Log Architecture",
                        "content": {
                            "title": "One-Week Stewardship Matrix",
                            "caption": "A 4-quadrant layout guiding daily reflection across Resource Conservation, Environmental Care, Time Management, and Community Service.",
                            "svg_content": SVG_DAILY_STEWARDSHIP_LOG
                        }
                    }
                ],
                # Card 4: Sample Student Diary & Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Practical Stewardship: Small Habits, Big Impact",
                        "content": {
                            "title": "Daily Stewardship in Action: Inspiring Youth Projects",
                            "youtube_id": "r8b-bO4wGkY",
                            "url": "https://www.youtube.com/watch?v=r8b-bO4wGkY",
                            "description": "Inspiring video case study showing how secondary students across East Africa lead practical conservation and community service initiatives."
                        }
                    },
                    {
                        "type": "real_world_example",
                        "title": "Authentic Student Diary Entry",
                        "content": {
                            "title": "Sample Log Entry: Moraa Kemunto (Grade 10)",
                            "text": "> **Date:** 31st August 2026 | **Grade:** 10 Green\n>\n> - **Resource Management:** I noticed the laboratory water tap was dripping. I tightened the valve securely, saving gallons of clean treated water.\n> - **Environmental Care:** During the afternoon break, I collected four plastic bottles scattered on the football pitch and placed them into the recycling bin.\n> - **Personal Responsibilities:** I organized my study desk immediately after school and spent 90 minutes completing my CRE and Biology homework before dinner.\n> - **Community Service:** I cheerfully helped my mother prepare supper and wash the dishes without being reminded or complaining."
                        }
                    }
                ],
                # Card 5: Comprehensive Topic 1.4 Synthesis
                [
                    {
                        "type": "comparison_table",
                        "title": "Comprehensive Topic 1.4 Synthesis Matrix",
                        "content": {
                            "headers": ["Unit Module", "Core Scripture", "Key Theological Concept", "Lived Practical Outcome"],
                            "rows": [
                                ["1. Defining Stewardship", "1 Corinthians 4:2, Psalm 24:1", "God is Owner; Humans are Trusted Managers", "Faithful management of school and family resources"],
                                ["2. Genesis 1:26-28", "Genesis 1:26-28", "Imago Dei & Benevolent Dominion (Radah)", "Protecting wildlife and ecosystems with loving leadership"],
                                ["3. Genesis 2:15-16", "Genesis 2:15-17", "Work (Shabad) and Guard (Shamar)", "Conducting school environmental audits & conserving water"],
                                ["4. Four Pillars", "Psalm 24:1, Rom 14:12", "Ownership, Responsibility, Accountability, Benefit", "Opposing pollution & promoting sustainable development"],
                                ["5. Steward Qualities", "Phil 2:3-4, Gal 6:9, Micah 6:8", "Selflessness, Humility, Wisdom, Patience", "Joyful teamwork and diligent agricultural practicals"],
                                ["6. Poetic Expression", "Psalm 104, Psalm 19", "Creative advocacy for creation care", "Composing and reciting stewardship advocacy poetry"],
                                ["7. Daily Documentation", "Colossians 3:23-24", "Daily lifestyle of holistic faithfulness", "Maintaining a 7-day multi-category stewardship journal"]
                            ]
                        }
                    }
                ],
                # Card 6: Summative Knowledge Check & Topic Mastery
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative Topic 1.4 Assessment",
                        "content": {
                            "question": "Which of the following actions best illustrates holistic Christian stewardship combining resource conservation, personal responsibility, and community service?",
                            "options": [
                                "Using up all household water quickly before anyone else can access it",
                                "Diligent time management to finish homework early, followed by cheerfully helping neighbors clean a choked drainage trench",
                                "Waiting for the government to pick up litter in front of your family home",
                                "Writing a beautiful poem about trees while actively dumping plastic waste into a river"
                            ],
                            "correct_answer": 1,
                            "explanation": "Option B is correct. Holistic stewardship seamlessly connects personal character (time management), environmental care (cleaning drainage), and cheerful community service."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 1.4 Final Mastery Summary",
                        "content": {
                            "text": "- **Stewardship is our Sacred Trust:** Rooted in God's creation design and human identity.\n- **Integrated Life:** Connects biblical theology, inward moral character, creative advocacy, and daily practical action.\n- **Eternal Value:** What we do with God's world matters to the Creator and to future generations."
                        }
                    }
                ]
            ]
        }
    ]

# =============================================================================
# DATABASE INGESTION CONTROLLER
# =============================================================================

def ingest_grade10_cre_topic_1_4(replace=True):
    """Ingests Grade 10 CRE Topic 1.4: Stewardship over Creation into the Django database."""
    print("=" * 80)
    print("STARTING INGESTION: Grade 10 CRE Topic 1.4: Stewardship over Creation")
    print("=" * 80)

    with transaction.atomic():
        # Validate Grade 10 (Curriculum CBC)
        try:
            grade = Grade.objects.get(id=5)
            print(f"Target Grade Resolved: {grade.name} (Curriculum: {grade.curriculum.name})")
        except Grade.DoesNotExist:
            print("ERROR: Grade with ID=5 does not exist. Aborting.")
            return

        # Validate CRE Subject (Subject ID: 46)
        try:
            subject = Subject.objects.get(id=46)
            print(f"Target Subject Resolved: {subject.name} (ID: {subject.id})")
        except Subject.DoesNotExist:
            # Fallback lookup by name under grade
            subject = Subject.objects.filter(grade=grade, name__icontains="Christian Religious Education").first() or \
                      Subject.objects.filter(grade=grade, name__icontains="CRE").first()
            if not subject:
                print("ERROR: CRE Subject not found for Grade 10. Aborting.")
                return
            print(f"Fallback Subject Resolved: {subject.name} (ID: {subject.id})")

        # Resolve or Create Topic 1.4: Stewardship over Creation (Order: 4)
        topic, t_created = Topic.objects.get_or_create(
            subject=subject,
            order=4,
            defaults={
                "name": "Topic 1.4: Stewardship over Creation",
                "description": "Exploration of the biblical call to stewardship, examining foundational commands in Genesis 1 and 2, core principles, moral qualities of a steward, poetic expression, and daily practical documentation.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Tea_plantations_in_Kericho%2C_Kenya.jpg"
            }
        )
        if not t_created:
            topic.name = "Topic 1.4: Stewardship over Creation"
            topic.description = "Exploration of the biblical call to stewardship, examining foundational commands in Genesis 1 and 2, core principles, moral qualities of a steward, poetic expression, and daily practical documentation."
            topic.image = "https://upload.wikimedia.org/wikipedia/commons/4/4e/Tea_plantations_in_Kericho%2C_Kenya.jpg"
            topic.save()
            print(f"Topic 1.4 Updated: {topic.name} (ID: {topic.id})")
        else:
            print(f"Topic 1.4 Created: {topic.name} (ID: {topic.id})")

        if replace:
            print("Replace mode active: Cleaning existing LearningUnits and Lessons under Topic 1.4...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()

        # Build curriculum dataset
        units_data = build_topic_1_4_curriculum()

        total_units_created = 0
        total_lessons_created = 0
        total_pages_created = 0
        total_blocks_created = 0

        for unit_def in units_data:
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
            total_units_created += 1

            # Create or resolve Lesson (Published, Version 1)
            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": l_title,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "author": "VLearn Grade 10 CRE Topic 1.4 Ingestion Agent",
                        "grade": "Grade 10",
                        "subject": "CRE",
                        "topic_order": 4,
                        "unit_order": u_order
                    }
                }
            )
            if not l_created:
                lesson.title = l_title
                lesson.status = "published"
                lesson.version = 1
                lesson.save()

            # Clean existing blocks for clean idempotent build
            lesson.blocks.all().delete()
            total_lessons_created += 1

            # Ingest Pages and Blocks
            block_order_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages_created += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t1_4_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_order_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 4, "unit_order": u_order, "page": page_idx}
                    )
                    block_order_counter += 1
                    total_blocks_created += 1

            print(f"  -> Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Cards, {block_order_counter - 1} Blocks)")

        print("=" * 80)
        print("INGESTION COMPLETED SUCCESSFULLY!")
        print(f"  Target Topic: {topic.name} (ID: {topic.id})")
        print(f"  Learning Units Created: {total_units_created}")
        print(f"  Published Lessons Created: {total_lessons_created}")
        print(f"  Total Lesson Pages (Cards): {total_pages_created}")
        print(f"  Total Lesson Blocks: {total_blocks_created}")
        print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_cre_topic_1_4(replace=True)
