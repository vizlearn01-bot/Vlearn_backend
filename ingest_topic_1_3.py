"""
VLearn CBC Grade 10 CRE — Topic 1.3: Redemption after the Fall of Man
Production Ingestion Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: CRE (ID: 46)
Topic: Topic 1.3: Redemption after the Fall of Man (Topic Order: 3)

Decomposed into 6 Learning Units & 6 Published Lessons:
  1. Understanding Redemption (6 Pages, 12 Blocks)
  2. The Origin of Sin (Genesis 3) (6 Pages, 12 Blocks)
  3. The Consequences of Sin (Genesis 3 and Beyond) (6 Pages, 12 Blocks)
  4. God's Plan of Salvation After the Fall (6 Pages, 12 Blocks)
  5. Christian Responses to God's Redemptive Work (6 Pages, 12 Blocks)
  6. Embracing God's Redemptive Work in Daily Life (6 Pages, 12 Blocks)
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
    """Removes bracket citations and internal metadata markers."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [1.3], [223], [1.3, 1.1]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags e.g. [VISUAL: ...], [BIBLE PASSAGE: ...], [VALUES], etc.
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

SVG_LESSON_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="bondageGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="ransomGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="freedomGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="cardShadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad1)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="42" fill="#f8fafc" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Theological Concept of Redemption</text>
  <text x="400" y="68" fill="#94a3b8" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">From Bondage and Debt to Liberation and Full Divine Restoration</text>

  <!-- Connector Flow Lines -->
  <line x1="250" y1="210" x2="295" y2="210" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4"/>
  <polygon points="295,205 305,210 295,215" fill="#f59e0b"/>

  <line x1="505" y1="210" x2="545" y2="210" stroke="#10b981" stroke-width="3" stroke-dasharray="6,4"/>
  <polygon points="545,205 555,210 545,215" fill="#10b981"/>

  <!-- Card 1: State of Bondage -->
  <g filter="url(#cardShadow1)">
    <rect x="40" y="105" width="210" height="230" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect x="40" y="105" width="210" height="40" rx="10" fill="url(#bondageGrad)"/>
    <text x="145" y="130" fill="#ffffff" font-size="15" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">1. State of Bondage</text>
    
    <circle cx="145" cy="180" r="24" fill="#334155" stroke="#ef4444" stroke-width="1.5"/>
    <text x="145" y="186" fill="#fca5a5" font-size="18" text-anchor="middle">⛓️</text>
    
    <text x="145" y="225" fill="#f8fafc" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Spiritual Captivity</text>
    <text x="60" y="250" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Human debt of sin</text>
    <text x="60" y="270" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Powerless to escape</text>
    <text x="60" y="290" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Separation from God</text>
    <text x="60" y="310" fill="#ef4444" font-size="10" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Verdict: Eternal Forfeit</text>
  </g>

  <!-- Card 2: The Ransom Price -->
  <g filter="url(#cardShadow1)">
    <rect x="295" y="95" width="210" height="250" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="295" y="95" width="210" height="40" rx="10" fill="url(#ransomGrad)"/>
    <text x="400" y="120" fill="#ffffff" font-size="15" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">2. The Ransom Paid</text>
    
    <circle cx="400" cy="170" r="24" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="400" y="176" fill="#fde68a" font-size="18" text-anchor="middle">✝️</text>
    
    <text x="400" y="215" fill="#f8fafc" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Christ's Sacrifice</text>
    <text x="315" y="240" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Costly divine exchange</text>
    <text x="315" y="260" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Legal debt satisfied</text>
    <text x="315" y="280" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Precious blood of Jesus</text>
    <text x="315" y="300" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Not escape, but legal rescue</text>
    <text x="315" y="325" fill="#f59e0b" font-size="10" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Action: Paid in Full</text>
  </g>

  <!-- Card 3: Complete Restoration -->
  <g filter="url(#cardShadow1)">
    <rect x="550" y="105" width="210" height="230" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="550" y="105" width="210" height="40" rx="10" fill="url(#freedomGrad)"/>
    <text x="655" y="130" fill="#ffffff" font-size="15" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">3. Freedom &amp; Restored</text>
    
    <circle cx="655" cy="180" r="24" fill="#334155" stroke="#10b981" stroke-width="1.5"/>
    <text x="655" y="186" fill="#a7f3d0" font-size="18" text-anchor="middle">🕊️</text>
    
    <text x="655" y="225" fill="#f8fafc" font-size="13" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Total Liberation</text>
    <text x="570" y="250" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Chains of guilt broken</text>
    <text x="570" y="270" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Restored inheritance</text>
    <text x="570" y="290" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Reconciled with God</text>
    <text x="570" y="310" fill="#10b981" font-size="10" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Result: Adopted into Life</text>
  </g>

  <!-- Bottom Key Footer -->
  <rect x="40" y="370" width="720" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="392" fill="#38bdf8" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The 4 Dimensions: To Buy Back • To Rescue / Deliver • To Set Free • To Restore</text>
  <text x="400" y="410" fill="#94a3b8" font-size="11" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Redemption honors divine justice while demonstrating supreme, unconditional grace.</text>
</svg>"""

SVG_LESSON_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="step1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="step2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="step3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
    <linearGradient id="step4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad2)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="42" fill="#f8fafc" font-size="22" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Decision &amp; Consequence Chain of Genesis 3</text>
  <text x="400" y="66" fill="#94a3b8" font-size="13" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Anatomy of Temptation, Human Moral Agency, and the Genesis Fall</text>

  <!-- Connecting Line -->
  <line x1="100" y1="210" x2="700" y2="210" stroke="#334155" stroke-width="4"/>

  <!-- Step 1: The Tempter's Whisper -->
  <g filter="url(#shadow2)">
    <rect x="40" y="105" width="165" height="235" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="40" y="105" width="165" height="36" rx="10" fill="url(#step1Grad)"/>
    <text x="122" y="128" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">1. Deceptive Whisper</text>
    
    <circle cx="122" cy="175" r="20" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="122" y="181" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">01</text>
    
    <text x="122" y="215" fill="#38bdf8" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Sowing Doubt</text>
    <text x="52" y="240" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• "Did God really say?"</text>
    <text x="52" y="260" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Exaggerating limits</text>
    <text x="52" y="280" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Questioning God's love</text>
    <text x="52" y="305" fill="#94a3b8" font-size="9.5" font-style="italic" font-family="system-ui, -apple-system, sans-serif">Tactic: Intellectual doubt</text>
  </g>

  <!-- Step 2: Human Doubt & Desire -->
  <g filter="url(#shadow2)">
    <rect x="225" y="105" width="165" height="235" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="225" y="105" width="165" height="36" rx="10" fill="url(#step2Grad)"/>
    <text x="307" y="128" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">2. Internal Desire</text>
    
    <circle cx="307" cy="175" r="20" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="307" y="181" fill="#f59e0b" font-size="14" font-weight="700" text-anchor="middle">02</text>
    
    <text x="307" y="215" fill="#f59e0b" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Self-Exaltation</text>
    <text x="237" y="240" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Desirable for wisdom</text>
    <text x="237" y="260" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Pleasing to the eye</text>
    <text x="237" y="280" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Craving to "be like God"</text>
    <text x="237" y="305" fill="#94a3b8" font-size="9.5" font-style="italic" font-family="system-ui, -apple-system, sans-serif">Tactic: Pride &amp; appetite</text>
  </g>

  <!-- Step 3: Disobedient Act -->
  <g filter="url(#shadow2)">
    <rect x="410" y="105" width="165" height="235" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="410" y="105" width="165" height="36" rx="10" fill="url(#step3Grad)"/>
    <text x="492" y="128" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">3. The Rebellion</text>
    
    <circle cx="492" cy="175" r="20" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="492" y="181" fill="#ef4444" font-size="14" font-weight="700" text-anchor="middle">03</text>
    
    <text x="492" y="215" fill="#ef4444" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Willful Choice</text>
    <text x="422" y="240" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Eve takes and eats</text>
    <text x="422" y="260" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Adam silently consents</text>
    <text x="422" y="280" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Crossing God's line</text>
    <text x="422" y="305" fill="#94a3b8" font-size="9.5" font-style="italic" font-family="system-ui, -apple-system, sans-serif">Action: Moral defiance</text>
  </g>

  <!-- Step 4: Immediate Aftermath -->
  <g filter="url(#shadow2)">
    <rect x="595" y="105" width="165" height="235" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="595" y="105" width="165" height="36" rx="10" fill="url(#step4Grad)"/>
    <text x="677" y="128" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">4. Shattered State</text>
    
    <circle cx="677" cy="175" r="20" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="677" y="181" fill="#8b5cf6" font-size="14" font-weight="700" text-anchor="middle">04</text>
    
    <text x="677" y="215" fill="#c084fc" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Guilt &amp; Alienation</text>
    <text x="607" y="240" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Eyes opened to shame</text>
    <text x="607" y="260" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Fig-leaf coverings</text>
    <text x="607" y="280" fill="#cbd5e1" font-size="10.5" font-family="system-ui, -apple-system, sans-serif">• Hiding among trees</text>
    <text x="607" y="305" fill="#94a3b8" font-size="9.5" font-style="italic" font-family="system-ui, -apple-system, sans-serif">Result: Spiritual rupture</text>
  </g>

  <!-- Bottom Key Footer -->
  <rect x="40" y="370" width="720" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="392" fill="#fca5a5" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Core Lesson: Sin is not merely an accident; it is personal doubt, disobedience, and self-exaltation.</text>
  <text x="400" y="410" fill="#94a3b8" font-size="11" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Free will enabled genuine love, but misuse of freedom led directly to spiritual separation.</text>
</svg>"""

SVG_LESSON_3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="q1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="q2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="q3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="q4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad3)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="21" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Multi-Dimensional Consequences of the Fall</text>
  <text x="400" y="60" fill="#94a3b8" font-size="12.5" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">How Sin Fractured Every Dimension of Human Existence, Society, and Creation</text>

  <!-- Grid Layout: 4 Quadrants -->
  
  <!-- Quadrant 1: Spiritual Dimension -->
  <g filter="url(#shadow3)">
    <rect x="40" y="80" width="345" height="135" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="40" y="80" width="345" height="32" rx="10" fill="url(#q1Grad)"/>
    <text x="212" y="102" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">1. Spiritual Dimension (Humanity vs. God)</text>
    
    <text x="55" y="132" fill="#93c5fd" font-size="11.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Original: Direct Face-to-Face Communion in Eden</text>
    <text x="55" y="152" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Terror and hiding from God's presence among the trees</text>
    <text x="55" y="170" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Loss of spiritual fellowship and expulsion from the Garden</text>
    <text x="55" y="190" fill="#fca5a5" font-size="10.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Impact: Spiritual Death &amp; Separation (Genesis 3:8, 24)</text>
  </g>

  <!-- Quadrant 2: Psychological & Personal Dimension -->
  <g filter="url(#shadow3)">
    <rect x="415" y="80" width="345" height="135" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="415" y="80" width="345" height="32" rx="10" fill="url(#q2Grad)"/>
    <text x="587" y="102" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">2. Psychological Dimension (Internal Self)</text>
    
    <text x="430" y="132" fill="#c084fc" font-size="11.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Original: Total Innocence, Peace, and Security</text>
    <text x="430" y="152" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Acute awareness of nakedness, vulnerability, and guilt</text>
    <text x="430" y="170" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Inadequacy of fig leaves; inner turmoil and anxiety</text>
    <text x="430" y="190" fill="#fca5a5" font-size="10.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Impact: Shame, Guilt &amp; Internal Fear (Genesis 3:7, 10)</text>
  </g>

  <!-- Quadrant 3: Relational & Social Dimension -->
  <g filter="url(#shadow3)">
    <rect x="40" y="235" width="345" height="135" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="40" y="235" width="345" height="32" rx="10" fill="url(#q3Grad)"/>
    <text x="212" y="257" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">3. Relational Dimension (Interpersonal &amp; Social)</text>
    
    <text x="55" y="287" fill="#f472b6" font-size="11.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Original: Harmony, Trust ("Bone of my bones")</text>
    <text x="55" y="307" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Immediate blame-shifting: Adam blames Eve &amp; God</text>
    <text x="55" y="325" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Escalates to fratricide (Cain murders Abel) and Babel's pride</text>
    <text x="55" y="345" fill="#fca5a5" font-size="10.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Impact: Conflict, Blame &amp; Social Breakdown (Genesis 3:12; 4:8)</text>
  </g>

  <!-- Quadrant 4: Environmental & Physical Dimension -->
  <g filter="url(#shadow3)">
    <rect x="415" y="235" width="345" height="135" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="415" y="235" width="345" height="32" rx="10" fill="url(#q4Grad)"/>
    <text x="587" y="257" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">4. Environmental &amp; Physical Dimension</text>
    
    <text x="430" y="287" fill="#6ee7b7" font-size="11.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Original: Abundant Garden Stewardship &amp; Immortality</text>
    <text x="430" y="307" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Ground cursed: Thorns, thistles, and painful sweat in toil</text>
    <text x="430" y="325" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Multiplied pain in childbearing and inevitable physical mortality</text>
    <text x="430" y="345" fill="#fca5a5" font-size="10.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Impact: "Dust to dust" — Physical Decay (Genesis 3:17-19)</text>
  </g>

  <!-- Bottom Key Footer -->
  <rect x="40" y="385" width="720" height="48" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="405" fill="#38bdf8" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Comprehensive Scope: Sin broke communion with God, harmony with others, and peace within oneself.</text>
  <text x="400" y="422" fill="#94a3b8" font-size="11" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Only an all-encompassing divine redemption could restore this multi-layered devastation.</text>
</svg>"""

SVG_LESSON_4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="p1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="p2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="p3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#065f46"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad4)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="21" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Arc of Salvation: The 3 Pillars of Redemptive Fulfillment</text>
  <text x="400" y="60" fill="#94a3b8" font-size="12.5" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">From the Genesis 3:15 Protoevangelium Promise to the Glorious Resurrection</text>

  <!-- Protoevangelium Header Banner -->
  <rect x="40" y="80" width="720" height="44" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="400" y="100" fill="#fcd34d" font-size="12.5" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Genesis 3:15 (The Protoevangelium — The First Gospel)</text>
  <text x="400" y="116" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">"He will crush your head, and you will strike his heel." — The prophecy of Christ's victory over evil.</text>

  <!-- Step Connectors -->
  <line x1="265" y1="235" x2="295" y2="235" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
  <polygon points="295,230 305,235 295,240" fill="#f59e0b"/>

  <line x1="505" y1="235" x2="535" y2="235" stroke="#10b981" stroke-width="3" stroke-dasharray="4,4"/>
  <polygon points="535,230 545,235 535,240" fill="#10b981"/>

  <!-- Step 1: Incarnation -->
  <g filter="url(#shadow4)">
    <rect x="40" y="140" width="225" height="215" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="40" y="140" width="225" height="36" rx="10" fill="url(#p1Grad)"/>
    <text x="152" y="163" fill="#ffffff" font-size="13.5" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Step 1: The Incarnation</text>
    
    <text x="152" y="196" fill="#7dd3fc" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">John 1:14 — Word Made Flesh</text>
    <text x="55" y="222" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• God entered human history</text>
    <text x="55" y="242" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Identified with human sorrow</text>
    <text x="55" y="262" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Lived a sinless life of truth</text>
    <text x="55" y="282" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• The Second / Last Adam</text>
    <text x="55" y="330" fill="#38bdf8" font-size="10.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Significance: God With Us</text>
  </g>

  <!-- Step 2: The Atonement -->
  <g filter="url(#shadow4)">
    <rect x="287" y="140" width="225" height="215" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="287" y="140" width="225" height="36" rx="10" fill="url(#p2Grad)"/>
    <text x="400" y="163" fill="#ffffff" font-size="13.5" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Step 2: The Atonement</text>
    
    <text x="400" y="196" fill="#fca5a5" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Ephesians 1:7 — Ransom Price</text>
    <text x="302" y="222" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Substitutionary sacrifice</text>
    <text x="302" y="242" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Shed blood on the cross</text>
    <text x="302" y="262" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Divine justice satisfied</text>
    <text x="302" y="282" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Forgiveness purchased</text>
    <text x="302" y="330" fill="#ef4444" font-size="10.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Significance: Debt Cancelled</text>
  </g>

  <!-- Step 3: The Resurrection -->
  <g filter="url(#shadow4)">
    <rect x="535" y="140" width="225" height="215" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="535" y="140" width="225" height="36" rx="10" fill="url(#p3Grad)"/>
    <text x="647" y="163" fill="#ffffff" font-size="13.5" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Step 3: The Resurrection</text>
    
    <text x="647" y="196" fill="#86efac" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">1 Cor 15:45 — Life-Giving Spirit</text>
    <text x="550" y="222" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Defeated death &amp; the grave</text>
    <text x="550" y="242" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Crushed the serpent's power</text>
    <text x="550" y="262" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Offers new eternal life</text>
    <text x="550" y="282" fill="#cbd5e1" font-size="11" font-family="system-ui, -apple-system, sans-serif">• Guarantee of our restoration</text>
    <text x="550" y="330" fill="#10b981" font-size="10.5" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Significance: Complete Victory</text>
  </g>

  <!-- Bottom Key Footer -->
  <rect x="40" y="375" width="720" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="396" fill="#38bdf8" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The First Adam failed in Eden bringing death; The Last Adam (Christ) conquered on Calvary bringing life.</text>
  <text x="400" y="414" fill="#94a3b8" font-size="11" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Animal skin coverings in Genesis 3 foreshadowed the ultimate, unblemished sacrifice of Jesus Christ.</text>
</svg>"""

SVG_LESSON_5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="godGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="selfGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="othersGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad5)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="21" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The 9-Fold Christian Response to Redemption</text>
  <text x="400" y="60" fill="#94a3b8" font-size="12.5" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The Principle of the Seed (John 12:24): Surrender, Transformation, and Fruitful Service</text>

  <!-- 3 Major Pillars of Response -->
  
  <!-- Column 1: Toward God -->
  <g filter="url(#shadow5)">
    <rect x="40" y="85" width="225" height="275" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="40" y="85" width="225" height="36" rx="10" fill="url(#godGrad)"/>
    <text x="152" y="108" fill="#ffffff" font-size="13.5" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">A. In Relation to God</text>
    
    <!-- Item 1: Faith -->
    <rect x="52" y="132" width="201" height="58" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="62" y="152" fill="#93c5fd" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">1. Faith &amp; Belief</text>
    <text x="62" y="172" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Confident trust in Christ as Lord.</text>

    <!-- Item 2: Repentance -->
    <rect x="52" y="200" width="201" height="68" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="62" y="220" fill="#93c5fd" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">2. Repentance (Metanoia)</text>
    <text x="62" y="240" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Total change of mind &amp; turning</text>
    <text x="62" y="255" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">away from sin toward God.</text>

    <!-- Item 3: Gratitude -->
    <rect x="52" y="278" width="201" height="68" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="62" y="298" fill="#93c5fd" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">3. Gratitude &amp; Worship</text>
    <text x="62" y="318" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Continual thankfulness in</text>
    <text x="62" y="333" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">prayer, song, and devotion.</text>
  </g>

  <!-- Column 2: Personal Character -->
  <g filter="url(#shadow5)">
    <rect x="287" y="85" width="225" height="275" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="287" y="85" width="225" height="36" rx="10" fill="url(#selfGrad)"/>
    <text x="400" y="108" fill="#ffffff" font-size="13.5" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">B. Personal Character</text>
    
    <!-- Item 4: Transformation -->
    <rect x="299" y="132" width="201" height="58" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="309" y="152" fill="#c084fc" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">4. Transformed Life</text>
    <text x="309" y="172" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Renewed mind and clean habits.</text>

    <!-- Item 5: Self-Denial -->
    <rect x="299" y="200" width="201" height="68" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="309" y="220" fill="#c084fc" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">5. Self-Denial / Sacrifice</text>
    <text x="309" y="240" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Surrendering selfish desires</text>
    <text x="309" y="255" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">like the seed in the ground.</text>

    <!-- Item 6: Perseverance -->
    <rect x="299" y="278" width="201" height="68" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="309" y="298" fill="#c084fc" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">6. Hope &amp; Perseverance</text>
    <text x="309" y="318" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Enduring trials with assurance</text>
    <text x="309" y="333" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">of eternal life in Christ.</text>
  </g>

  <!-- Column 3: Toward Others -->
  <g filter="url(#shadow5)">
    <rect x="535" y="85" width="225" height="275" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="535" y="85" width="225" height="36" rx="10" fill="url(#othersGrad)"/>
    <text x="647" y="108" fill="#ffffff" font-size="13.5" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">C. In Relation to Others</text>
    
    <!-- Item 7: Obedience -->
    <rect x="547" y="132" width="201" height="58" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="557" y="152" fill="#6ee7b7" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">7. Obedience &amp; Integrity</text>
    <text x="557" y="172" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Active adherence to moral laws.</text>

    <!-- Item 8: Love & Service -->
    <rect x="547" y="200" width="201" height="68" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="557" y="220" fill="#6ee7b7" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">8. Unconditional Love</text>
    <text x="557" y="240" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Reflecting God's agape love</text>
    <text x="557" y="255" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">through compassionate service.</text>

    <!-- Item 9: Witness -->
    <rect x="547" y="278" width="201" height="68" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="557" y="298" fill="#6ee7b7" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif">9. Courageous Witness</text>
    <text x="557" y="318" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">Sharing redemption's message</text>
    <text x="557" y="333" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">in school and community.</text>
  </g>

  <!-- Bottom Key Footer -->
  <rect x="40" y="375" width="720" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="396" fill="#fcd34d" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Jesus in John 12:24: Unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit.</text>
  <text x="400" y="414" fill="#94a3b8" font-size="11" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Redemption is received by faith and demonstrated through sacrificial love, repentance, and practical witness.</text>
</svg>"""

SVG_LESSON_6 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="nodeGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="nodeGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="nodeGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="nodeGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="nodeGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bgGrad6)" rx="12"/>

  <!-- Title & Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="21" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">The 5-Step Daily Reflection &amp; Moral Action Loop</text>
  <text x="400" y="60" fill="#94a3b8" font-size="12.5" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Personalizing John 3:16 into Daily Christian Character, Integrity, and Service</text>

  <!-- 5 Cards arranged horizontally -->
  
  <!-- Step 1 -->
  <g filter="url(#shadow6)">
    <rect x="30" y="90" width="135" height="260" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="30" y="90" width="135" height="34" rx="10" fill="url(#nodeGrad1)"/>
    <text x="97" y="112" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">1. Repentance</text>
    
    <circle cx="97" cy="155" r="18" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="97" y="161" fill="#fca5a5" font-size="14" font-weight="700" text-anchor="middle">01</text>
    
    <text x="97" y="195" fill="#fca5a5" font-size="11" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Confession</text>
    <text x="40" y="220" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Confess specific mistakes</text>
    <text x="40" y="250" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Stop blame-shifting</text>
    <text x="40" y="280" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Seek forgiveness</text>
    <text x="40" y="325" fill="#ef4444" font-size="9" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Action: Humility</text>
  </g>

  <!-- Step 2 -->
  <g filter="url(#shadow6)">
    <rect x="180" y="90" width="135" height="260" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="180" y="90" width="135" height="34" rx="10" fill="url(#nodeGrad2)"/>
    <text x="247" y="112" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">2. Gratitude</text>
    
    <circle cx="247" cy="155" r="18" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="247" y="161" fill="#fde68a" font-size="14" font-weight="700" text-anchor="middle">02</text>
    
    <text x="247" y="195" fill="#fde68a" font-size="11" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Praise</text>
    <text x="190" y="220" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• List 3 blessings today</text>
    <text x="190" y="250" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Celebrate God's care</text>
    <text x="190" y="280" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Cultivate joyful heart</text>
    <text x="190" y="325" fill="#f59e0b" font-size="9" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Action: Contentment</text>
  </g>

  <!-- Step 3 -->
  <g filter="url(#shadow6)">
    <rect x="330" y="90" width="135" height="260" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="330" y="90" width="135" height="34" rx="10" fill="url(#nodeGrad3)"/>
    <text x="397" y="112" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">3. Neighbor Love</text>
    
    <circle cx="397" cy="155" r="18" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="397" y="161" fill="#a7f3d0" font-size="14" font-weight="700" text-anchor="middle">03</text>
    
    <text x="397" y="195" fill="#a7f3d0" font-size="11" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Service</text>
    <text x="340" y="220" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Show practical kindness</text>
    <text x="340" y="250" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Help a struggling peer</text>
    <text x="340" y="280" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Overcome selfishness</text>
    <text x="340" y="325" fill="#10b981" font-size="9" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Action: Compassion</text>
  </g>

  <!-- Step 4 -->
  <g filter="url(#shadow6)">
    <rect x="480" y="90" width="135" height="260" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="480" y="90" width="135" height="34" rx="10" fill="url(#nodeGrad4)"/>
    <text x="547" y="112" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">4. Step of Faith</text>
    
    <circle cx="547" cy="155" r="18" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="547" y="161" fill="#93c5fd" font-size="14" font-weight="700" text-anchor="middle">04</text>
    
    <text x="547" y="195" fill="#93c5fd" font-size="11" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Integrity</text>
    <text x="490" y="220" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Resist peer pressure</text>
    <text x="490" y="250" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Reject exam shortcuts</text>
    <text x="490" y="280" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Stand up for truth</text>
    <text x="490" y="325" fill="#3b82f6" font-size="9" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Action: Moral Courage</text>
  </g>

  <!-- Step 5 -->
  <g filter="url(#shadow6)">
    <rect x="630" y="90" width="135" height="260" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="630" y="90" width="135" height="34" rx="10" fill="url(#nodeGrad5)"/>
    <text x="697" y="112" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">5. Prayer &amp; Hope</text>
    
    <circle cx="697" cy="155" r="18" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="697" y="161" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">05</text>
    
    <text x="697" y="195" fill="#c084fc" font-size="11" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Witness</text>
    <text x="640" y="220" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Pray for Holy Spirit power</text>
    <text x="640" y="250" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Share hope with peers</text>
    <text x="640" y="280" fill="#cbd5e1" font-size="10" font-family="system-ui, -apple-system, sans-serif">• Walk in newness of life</text>
    <text x="640" y="325" fill="#8b5cf6" font-size="9" font-weight="600" font-family="system-ui, -apple-system, sans-serif">Action: Spiritual Power</text>
  </g>

  <!-- Bottom Key Footer -->
  <rect x="30" y="375" width="735" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="397" y="396" fill="#38bdf8" font-size="12" font-weight="600" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">John 3:16 is not just history; it is an active daily lifestyle of repentance, gratitude, love, and courage.</text>
  <text x="397" y="414" fill="#94a3b8" font-size="11" font-family="system-ui, -apple-system, sans-serif" text-anchor="middle">Maintaining a daily reflection journal equips Grade 10 learners to live out their Christian identity in contemporary society.</text>
</svg>"""


# =============================================================================
# TOPIC 1.3 CURRICULUM DEFINITION (6 Learning Units, 6 Lessons, 36 Pages)
# =============================================================================

def build_topic_1_3_curriculum():
    """Returns the pedagogical curriculum data for Topic 1.3: Redemption after the Fall of Man."""
    return [
        # =====================================================================
        # LESSON 1: Understanding Redemption
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Understanding Redemption",
            "unit_description": "Exploring the theological concept and four dimensions of redemption in Christian Religious Education: buying back, rescue from bondage, setting free, and restoration.",
            "lesson_title": "Understanding Redemption",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/%22The_Repentance_of_the_Prodigal_Son%22_from_a_set_of_six_of_The_Parable_of_the_Prodigal_Son_MET_DP329221.jpg/960px-%22The_Repentance_of_the_Prodigal_Son%22_from_a_set_of_six_of_The_Parable_of_the_Prodigal_Son_MET_DP329221.jpg",
            "image_caption": "Historical engraving depicting the repentance and restoration of the lost son, symbolizing redemption and return to divine fellowship.",
            "svg_content": SVG_LESSON_1,
            "youtube_id": "G_OlPRfxEAA",
            "youtube_title": "The Biblical Theology of Atonement and Redemption",
            "youtube_description": "Explores how biblical redemption involves paying a ransom price to rescue humanity from bondage and restore covenant communion with God.",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: The Repentance and Restoration of the Lost Son",
                        "content": {
                            "title": "Visual Hook: The Repentance and Restoration of the Lost Son",
                            "caption": "Historical engraving depicting the repentance and restoration of the lost son, symbolizing redemption and return to divine fellowship."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Meaning of Redemption",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define the theological meaning of **redemption** in Christian Religious Education.",
                                "Analyze the **four core dimensions** of biblical redemption: to buy back, to rescue/deliver, to set free, and to restore.",
                                "Distinguish clearly between legal **redemption** and merely escaping punishment.",
                                "Explain why the **Fall of Man** made divine redemption necessary."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Story of the Pawned Heirloom",
                        "content": {
                            "title": "The Price of Full Restoration",
                            "text": "Imagine you have lost an invaluable family heirloom—a beautiful, golden watch handed down through generations. You accidentally left it at a local pawn shop as collateral during a severe family financial crisis. To reclaim it, someone must walk into that shop, present the legal ownership receipt, and pay the exact ransom price required to restore it to your family.\n\nIn Christian theology, **redemption** is a very similar, beautifully dramatic story of rescue. It is not just about escaping punishment; it is about being bought back and restored to our original owner at an immense cost."
                        }
                    }
                ],
                # Card 2: Definitions & Everyday Connection
                [
                    {
                        "type": "concept_explanation",
                        "title": "Everyday Connections to Redemption",
                        "content": {
                            "title": "Where We Hear 'Redemption' in Daily Life",
                            "text": "You might have encountered the root word *redeem* in everyday situations:\n\n- **Redeeming a Voucher**: Exchanging a retail coupon or gift card at a supermarket to claim valuable goods.\n- **Redeeming Oneself in Sports**: When a striker who missed an easy goal earlier in the match works hard and scores the dramatic winning goal in the final minute.\n\nIn both instances, something of genuine value is exchanged, or a compromised, forfeited situation is transformed into restored victory."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "The Four Theological Dimensions of Biblical Redemption",
                        "content": {
                            "title": "The 4 Core Dimensions of Redemption",
                            "definition": "In Christian scripture and theology, redemption encompasses four profound, interconnected truths:",
                            "dimensions": [
                                "1. **To Buy Back**: A specific, costly purchase or ransom price was paid to reclaim what was lost or forfeited.",
                                "2. **To Rescue or Deliver**: Humanity was trapped in a state of spiritual bondage, slavery, and danger from which we were utterly powerless to escape on our own.",
                                "3. **To Set Free**: Complete liberation from captivity and sin's dominion, enabling the believer to live in true spiritual freedom.",
                                "4. **To Restore**: Reclaiming a lost identity, relationship, and inheritance that is fully reinstated by God."
                            ]
                        }
                    }
                ],
                # Card 3: Vector Blueprint & Critical Distinction
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The Theological Concept of Redemption",
                        "content": {
                            "title": "Vector Blueprint: The Theological Concept of Redemption",
                            "caption": "Diagram illustrating the transition from spiritual bondage through Christ's ransom price to full freedom and divine restoration.",
                            "svg": SVG_LESSON_1
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Critical Thinking: Redemption vs. Escape",
                        "content": {
                            "title": "Why Redemption Is Far Superior to Mere Escape",
                            "text": "Why is biblical redemption fundamentally different from simply breaking out of prison?\n\n- **An Escape**: Involves breaking rules illegally, leaves the legal debt unpaid, leaves the law unsatisfied, and turns the individual into an anxious fugitive constantly on the run.\n- **Biblical Redemption**: Fully satisfies the requirements of divine justice. The legal debt is paid in full by the Redeemer, the chains are legally removed, and the believer walks freely in broad daylight without fear of condemnation."
                        }
                    }
                ],
                # Card 4: Video Integration & Connection to the Fall
                [
                    {
                        "type": "suggested_video",
                        "title": "Educational Video: Sacrifice and Atonement",
                        "content": {
                            "title": "The Biblical Theology of Atonement and Redemption",
                            "description": "Explores how biblical redemption involves paying a ransom price to rescue humanity from bondage and restore covenant communion with God.",
                            "url": "https://www.youtube.com/watch?v=G_OlPRfxEAA"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Connecting Redemption to the Fall of Man",
                        "content": {
                            "title": "Why Was Divine Redemption Necessary?",
                            "text": "The message of redemption only makes sense against the backdrop of the tragedy of the **Fall of Man** recorded in Genesis 3.\n\nGod created human beings in perfect innocence, dignity, and unhindered fellowship with Himself. However, through an act of willful disobedience and mistrust, humanity fell into spiritual slavery, bringing guilt, death, and alienation into the world. Humanity could not bridge this infinite gap by human effort alone—requiring God Himself to initiate a divine rescue mission."
                        }
                    }
                ],
                # Card 5: Core Milestones & Reflection
                [
                    {
                        "type": "step_process",
                        "title": "The 4 Essential Milestones in Understanding Redemption",
                        "content": {
                            "title": "The Sequence of God's Redemptive Work",
                            "steps": [
                                "1. **Recognizing the Condition**: Acknowledging that sin introduced universal spiritual bankruptcy and captivity.",
                                "2. **Identifying the Redeemer**: Realizing that only Jesus Christ, as the sinless Son of God, could pay the required ransom price.",
                                "3. **Accepting the Substitution**: Understanding that Christ died in our place on the cross, taking our penalty upon Himself.",
                                "4. **Living in Restored Fellowship**: Walking as sons and daughters of God with renewed dignity, gratitude, and moral purpose."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Reflective Activity: Pondering Legal Liberation",
                        "content": {
                            "title": "Personal Reflection: The Cost of Your Freedom",
                            "task": "1. Write down one instance where someone sacrificed time, money, or comfort to help you out of a difficult problem.\n2. In what ways does that personal sacrifice help you understand the immense value God placed on you through the cross of Jesus Christ?\n3. Summarize the difference between 'earning' salvation and 'receiving' redemption."
                        }
                    }
                ],
                # Card 6: Key Takeaway & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary: Understanding Redemption",
                        "content": {
                            "title": "Core Takeaways on Biblical Redemption",
                            "text": "- **Redemption** is the divine rescue act of buying back, setting free, and restoring humanity from sin at an infinite cost.\n- Its **4 dimensions** are: buying back (ransom), rescuing from bondage, liberating for freedom, and restoring lost inheritance.\n- Unlike escape, redemption **fully satisfies divine justice** and eliminates condemnation.\n- Redemption is made necessary by humanity's tragic fall into sin in Genesis 3."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Meaning of Redemption",
                        "content": {
                            "question": "Which of the following best describes the biblical meaning of 'redemption' in Christian theology?",
                            "options": [
                                "Breaking out of prison through cunning human effort while remaining a fugitive",
                                "God overlooking human sin without addressing the demands of divine justice",
                                "Being bought back, rescued from spiritual bondage, set free, and restored to God at a great cost",
                                "Attaining financial independence and social prestige through individual hard work"
                            ],
                            "answer": "C",
                            "explanation": "Biblical redemption always involves being bought back from captivity through the payment of a ransom price, resulting in full liberation and restoration to God's original purpose."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: The Origin of Sin (Genesis 3)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "The Origin of Sin (Genesis 3)",
            "unit_description": "Analyzing the narrative of Genesis 3 to understand the origin, deceptive tactics, progressive anatomy, and core definition of sin.",
            "lesson_title": "The Origin of Sin (Genesis 3)",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Hugo_van_der_Goes_-_The_Fall_of_Man_and_The_Lamentation_-_Google_Art_Project.jpg/960px-Hugo_van_der_Goes_-_The_Fall_of_Man_and_The_Lamentation_-_Google_Art_Project.jpg",
            "image_caption": "Fifteenth-century masterpiece by Hugo van der Goes depicting the temptation in Eden and the resulting Fall of Man.",
            "svg_content": SVG_LESSON_2,
            "youtube_id": "KOUV7mW490s",
            "youtube_title": "Genesis 1-11 Overview: The Choice in the Garden",
            "youtube_description": "Explores the literary and theological structure of Genesis 3, tracing the serpent's deceptive whisper and the human choice to define good and evil autonomously.",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Hugo van der Goes - The Fall of Man",
                        "content": {
                            "title": "Visual Hook: Hugo van der Goes - The Fall of Man",
                            "caption": "Fifteenth-century masterpiece by Hugo van der Goes depicting the temptation in Eden and the resulting Fall of Man."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Origin and Nature of Sin",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Examine the Garden of Eden setting and God's protective boundary in **Genesis 2:15-17**.",
                                "Analyze the scriptural account of **Genesis 3:1-7** and the serpent's deceptive tactics.",
                                "Trace the progressive anatomy of sin: from doubt to physical desire, disobedient action, and shame.",
                                "Define the true theological nature of sin as **doubt, disobedience, and self-exaltation**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Boundary in Paradise",
                        "content": {
                            "title": "Freedom with a Single Moral Boundary",
                            "text": "In the Garden of Eden, Adam and Eve lived in perfect innocence, security, and uninterrupted fellowship with God. God gave them immense freedom and abundance, with only one clear moral boundary:\n\n> *'The Lord God took the man and put him in the Garden of Eden to work it and take care of it. And the Lord God commanded the man: You are free to eat from any tree in the garden; but you must not eat from the tree of the knowledge of good and evil, for when you eat from it you will certainly die.'* (Genesis 2:15-17)\n\nThis single boundary was not designed to restrict their happiness, but to provide a context for genuine love, trust, and willing obedience."
                        }
                    }
                ],
                # Card 2: Scripture & Deconstruct Tactics
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Scriptural Account: Genesis 3:1-7",
                        "content": {
                            "title": "The Dramatic Encounter in the Garden",
                            "text": "Let us read Genesis 3:1-6:\n\n> *'Now the serpent was more crafty than any of the wild animals the Lord God had made. He said to the woman: Did God really say, You must not eat from any tree in the garden? The woman said to the serpent: We may eat fruit from the trees in the garden, but God did say, You must not eat fruit from the tree that is in the middle of the garden, and you must not touch it, or you will die. You will not certainly die, the serpent said to the woman. For God knows that when you eat from it your eyes will be opened, and you will be like God, knowing good and evil. When the woman saw that the fruit of the tree was good for food and pleasing to the eye, and also desirable for gaining wisdom, she took some and ate it. She also gave some to her husband, who was with her, and he ate it.'*"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Deconstructing the Tempter's Tactics",
                        "content": {
                            "title": "How the Tempter Manipulated Human Thinking",
                            "text": "The narrative highlights three insidious psychological tactics used to induce rebellion:\n\n- **1. Exaggerating God's Restrictions**: The serpent asked, *'Did God really say you must not eat from ANY tree?'* making God appear stingy, unreasonable, and tyrannical.\n- **2. Contradicting God's Word**: The serpent boldly lied, *'You will not certainly die,'* denying the severe reality of moral and physical consequences.\n- **3. Sowing Suspicion Against God's Character**: The serpent claimed, *'God knows that when you eat... you will be like God,'* implying that God was selfishly withholding true enlightenment."
                        }
                    }
                ],
                # Card 3: Vector Blueprint & Anatomy of Sin
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Decision and Consequence Chain of Genesis 3",
                        "content": {
                            "title": "Vector Blueprint: Decision and Consequence Chain of Genesis 3",
                            "caption": "Flowchart demonstrating the progression from the tempter's whisper to internal doubt, willful rebellion, and immediate shame.",
                            "svg": SVG_LESSON_2
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Anatomy of Human Moral Failure",
                        "content": {
                            "title": "How Eve and Adam Consented to Rebellion",
                            "text": "The Fall was a deliberate human choice involving distinct steps:\n\n- **Entertaining the Lie**: Eve listened, added her own restriction (*'you must not touch it'*), and began evaluating God's command based on personal desire.\n- **Threefold Allure**: The fruit appealed to the senses (good for food), visual admiration (pleasing to the eye), and intellectual pride (desirable for gaining wisdom).\n- **Adam's Stewardship Failure**: The text notes Adam *'was with her.'* He failed to speak up, protect his wife, or uphold God's command, passively consenting and joining in direct disobedience."
                        }
                    }
                ],
                # Card 4: Video Integration & Core Definition
                [
                    {
                        "type": "suggested_video",
                        "title": "Educational Video: The Choice in Genesis 3",
                        "content": {
                            "title": "Genesis 1-11 Overview: The Choice in the Garden",
                            "description": "Explores the literary and theological structure of Genesis 3, tracing the serpent's deceptive whisper and the human choice to define good and evil autonomously.",
                            "url": "https://www.youtube.com/watch?v=KOUV7mW490s"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "The Core Theological Definition of Sin",
                        "content": {
                            "title": "What Is Sin at Its Deepest Level?",
                            "definition": "According to Christian theology, sin is far more than an accidental mistake or external rule-breaking. At its root, sin is:",
                            "dimensions": [
                                "1. **Doubt in God's Word**: Believing the falsehood that God is untrustworthy and withholding good.",
                                "2. **Willful Disobedience**: Consciously violating the righteous boundaries established by our Creator.",
                                "3. **Self-Exaltation and Pride**: The autonomous desire to 'be like God,' defining morality for ourselves rather than submitting to God."
                            ]
                        }
                    }
                ],
                # Card 5: Common Misconceptions & Ethical Scenario
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: 'The Snake Made Them Do It'",
                        "content": {
                            "misconception": "Adam and Eve were helpless, hypnotized victims with no choice other than to eat the fruit.",
                            "correction": "Adam and Eve possessed complete moral free will. The serpent could only suggest and tempt; it had no power to compel them. They made a conscious, responsible choice to distrust God and disobey."
                        }
                    },
                    {
                        "type": "ethical_scenario",
                        "title": "Modern Ethical Scenario: Mutua and the Cheating Temptation",
                        "content": {
                            "scenario": "Mutua, a Grade 10 student, has not prepared sufficiently for an upcoming national assessment. His friend whispers: 'I have the leaked exam paper on my phone. Why fail? Did the school rules really mean you can't use study aids? Everyone is doing it, and you will get an A!'",
                            "reflection": "How does this whisper mirror the serpent in Eden? It questions the validity of the rule ('Did they really mean...'), claims zero consequences ('Everyone is doing it'), and promises status and success through a dishonest shortcut.\n\n**Christian Response**: Mutua must exercise integrity, reject the shortcut, accept his current preparation honestly, and trust in God-honoring hard work."
                        }
                    }
                ],
                # Card 6: Key Takeaways & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary: The Origin of Sin",
                        "content": {
                            "title": "Core Takeaways on Genesis 3",
                            "text": "- God gave humanity **abundant freedom** protected by a single moral boundary in Eden.\n- The tempter used **doubt, exaggeration, and false promises** of autonomy to entice humanity.\n- Sin is fundamentally **doubt in God's goodness, willful disobedience, and prideful self-exaltation**.\n- Human beings possess **moral free will** and bear full responsibility for their choices."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Root of the Fall",
                        "content": {
                            "question": "What was the fundamental underlying motivation behind Adam and Eve's decision to eat the forbidden fruit in Genesis 3?",
                            "options": [
                                "They were starving and had no other food available in the Garden of Eden",
                                "They desired to be autonomous like God and determine good and evil on their own terms",
                                "The serpent physically forced them to swallow the fruit against their will",
                                "God forgot to inform them which tree was forbidden in the garden"
                            ],
                            "answer": "B",
                            "explanation": "At its root, the temptation was the promise that 'you will be like God, knowing good and evil'—a prideful desire for moral autonomy independent of God's authority."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: The Consequences of Sin (Genesis 3 and Beyond)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "The Consequences of Sin (Genesis 3 and Beyond)",
            "unit_description": "Examining the multi-dimensional consequences of the Fall—spiritual, psychological, relational, environmental, and physical—and tracing the spread of sin in the Old Testament.",
            "lesson_title": "The Consequences of Sin (Genesis 3 and Beyond)",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Cole_Thomas_Expulsion_from_the_Garden_of_Eden_1828.jpg/960px-Cole_Thomas_Expulsion_from_the_Garden_of_Eden_1828.jpg",
            "image_caption": "Thomas Cole's 1828 masterpiece 'Expulsion from the Garden of Eden', capturing the dramatic contrast between paradise and the fallen world.",
            "svg_content": SVG_LESSON_3,
            "youtube_id": "aNOZ7ocLD74",
            "youtube_title": "Word Study: Khata (Sin) and Its Consequences",
            "youtube_description": "Explores the biblical concept of sin as missing the mark of human purpose, resulting in fractured relationships, social destruction, and spiritual death.",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Cole Thomas - Expulsion from the Garden of Eden",
                        "content": {
                            "title": "Visual Hook: Cole Thomas - Expulsion from the Garden of Eden",
                            "caption": "Thomas Cole's 1828 masterpiece 'Expulsion from the Garden of Eden', capturing the dramatic contrast between paradise and the fallen world."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Multi-Dimensional Fallout of Sin",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Identify the immediate psychological, spiritual, and relational consequences of sin in **Genesis 3**.",
                                "Analyze the physical and environmental judgments pronounced upon humanity and creation.",
                                "Trace the rapid spread and escalation of sin through the Old Testament (**Cain and Abel, Noah's generation, Tower of Babel**).",
                                "Apply lessons of personal **accountability** to overcome the modern blame-game."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Shattered Crystal Glass",
                        "content": {
                            "title": "A Total Systemic Breakdown",
                            "text": "If you drop a fine crystal glass onto a concrete floor, it does not merely chip in one small spot—it shatters into hundreds of sharp fragments, completely ruining its structural integrity.\n\nSimilarly, the Fall of Man was not a minor blemish on human history; it was a catastrophic fracture that affected every dimension of human life: our relationship with God, our inner emotional health, our social relationships with one another, and our physical environment."
                        }
                    }
                ],
                # Card 2: Immediate Fallout & Comprehensive Matrix
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Immediate Fallout in Genesis 3",
                        "content": {
                            "title": "How Adam and Eve's Experience Changed Instantly",
                            "text": "Immediately following their disobedience, Adam and Eve experienced devastating changes:\n\n- **Shame and Guilt**: Their innocence was replaced by self-conscious vulnerability; they sewed fig leaves together to cover themselves (Genesis 3:7).\n- **Fear and Alienation**: When they heard God walking in the garden, they hid among the trees in terror instead of greeting Him with joy (Genesis 3:8-10).\n- **Blame-Shifting**: When confronted, Adam blamed Eve and subtly blamed God (*'The woman YOU put here with me'*), while Eve blamed the serpent (Genesis 3:12-13)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comprehensive Matrix: The Dimensions of the Fall",
                        "content": {
                            "headers": ["Dimension", "Original State in Eden", "Consequence of the Fall", "Scriptural Reference"],
                            "rows": [
                                ["Spiritual", "Face-to-face communion with God", "Fear, hiding, spiritual alienation, expulsion from Eden", "Genesis 3:8, 24"],
                                ["Psychological", "Pure innocence, peace, security", "Guilt, shame, self-consciousness, anxiety", "Genesis 3:7, 10"],
                                ["Relational", "Perfect harmony ('bone of my bones')", "Blame-shifting, conflict, resentment, fratricide", "Genesis 3:12; 4:8"],
                                ["Environmental", "Abundant garden, effortless stewardship", "Ground cursed, thorns, thistles, painful sweat in labor", "Genesis 3:17-18"],
                                ["Physical", "Created for unbroken vitality and life", "Pain in childbearing, physical decay, bodily death ('dust to dust')", "Genesis 3:16, 19"]
                            ]
                        }
                    }
                ],
                # Card 3: Vector Blueprint & Physical Expulsion
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Multi-Dimensional Consequences Matrix",
                        "content": {
                            "title": "Vector Blueprint: Multi-Dimensional Consequences Matrix",
                            "caption": "Interactive quadrant diagram summarizing the spiritual, psychological, relational, and environmental fallout of sin.",
                            "svg": SVG_LESSON_3
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Physical Judgments and Expulsion from Eden",
                        "content": {
                            "title": "The Solemn Reality of the Curse",
                            "text": "God's righteous judgment addressed every aspect of earthly existence:\n\n- **For the Woman**: Multiplied pain in childbearing and marital conflict (Genesis 3:16).\n- **For the Man**: The ground was cursed with thorns and thistles; agriculture became painful toil requiring the *'sweat of your brow'* (Genesis 3:17-19).\n- **Physical Death**: Access to the Tree of Life was blocked. God declared: *'For dust you are, and to dust you will return.'*\n- **Expulsion**: Humanity was driven out of Eden, with Cherubim and a flaming sword guarding the entrance, symbolizing the severed unhindered communion."
                        }
                    }
                ],
                # Card 4: Video Integration & Escalation in OT
                [
                    {
                        "type": "suggested_video",
                        "title": "Educational Video: Khata (Sin) and Its Rampant Growth",
                        "content": {
                            "title": "Word Study: Khata (Sin) and Its Consequences",
                            "description": "Explores the biblical concept of sin as missing the mark of human purpose, resulting in fractured relationships, social destruction, and spiritual death.",
                            "url": "https://www.youtube.com/watch?v=aNOZ7ocLD74"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Rapid Escalation of Sin in Old Testament History",
                        "content": {
                            "title": "From Eden to Fratricide, the Flood, and Babel",
                            "text": "The poison of sin quickly metastasized through early human generations:\n\n- **Brotherly Murder (Genesis 4:1-15)**: Jealousy and unchecked anger led Cain to brutally murder his righteous brother Abel, destroying family unity.\n- **Universal Corruption (Genesis 6:5-13)**: In Noah's time, *'every inclination of the thoughts of the human heart was only evil all the time,'* bringing the judgment of the Great Flood.\n- **Arrogance at Babel (Genesis 11:1-9)**: Humanity united in pride to build a monument to make a name for themselves, resulting in the confusion of languages and widespread dispersion."
                        }
                    }
                ],
                # Card 5: Real-World Blame-Game & Accountability
                [
                    {
                        "type": "mini_activity",
                        "title": "Real-World Application: Breaking the Blame-Game",
                        "content": {
                            "title": "Overcoming the Adam & Eve Reaction in Daily Life",
                            "task": "1. Identify a situation in school or at home where you made a mistake (e.g., missed an assignment, damaged property) and felt tempted to blame someone else.\n2. Write down what a 'Fallen Adam' response looks like (denial, blame-shifting, hiding).\n3. Write down what a 'Redeemed Christian' response looks like (humble confession, accepting consequences, making restitution)."
                        }
                    },
                    {
                        "type": "ethical_scenario",
                        "title": "Ethical Scenario: Group Work Sabotage",
                        "content": {
                            "scenario": "During a Grade 10 CRE group assignment, Brian failed to compile his assigned section, causing the whole group to receive a lower mark. When the teacher asks what happened, Brian quickly says, 'The library was locked, and anyway, Sarah didn't remind me!'",
                            "reflection": "Brian is repeating the exact blame-shifting behavior of Adam. **True Christian Maturity** requires taking full personal ownership of one's shortcomings, apologizing to teammates, and diligently making amends."
                        }
                    }
                ],
                # Card 6: Key Takeaways & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary: Consequences of Sin",
                        "content": {
                            "title": "Core Takeaways on the Consequences of the Fall",
                            "text": "- Sin produced **multi-dimensional devastation**: spiritual alienation, internal shame, relational conflict, and environmental toil.\n- Physical mortality entered creation (*'dust to dust'*), cutting off access to the Tree of Life.\n- Sin spread rapidly in history through **Cain's murder of Abel, the corruption of Noah's era, and the pride of Babel**.\n- Christian character rejects blame-shifting and embraces **courageous personal accountability**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Consequences of Sin",
                        "content": {
                            "question": "When God questioned Adam about eating from the forbidden tree in Genesis 3:12, what was Adam's immediate reaction?",
                            "options": [
                                "He fell on his knees, wept bitterly, and asked God for immediate mercy",
                                "He shifted the blame onto the woman God had placed with him",
                                "He denied that any tree in the garden had been touched",
                                "He courageously took full responsibility and defended his wife"
                            ],
                            "answer": "B",
                            "explanation": "Instead of confessing, Adam demonstrated relational brokenness by blaming both his wife and God: 'The woman you put here with me—she gave me some fruit from the tree, and I ate it.'"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: God's Plan of Salvation After the Fall
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "God's Plan of Salvation After the Fall",
            "unit_description": "Discovering God's immediate grace in Genesis 3, the Protoevangelium promise, and the three major pillars of redemptive fulfillment in Jesus Christ: Incarnation, Atonement, and Resurrection.",
            "lesson_title": "God's Plan of Salvation After the Fall",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Gustave_Dor%C3%A9_-_Crucifixion_of_Jesus.jpg/960px-Gustave_Dor%C3%A9_-_Crucifixion_of_Jesus.jpg",
            "image_caption": "Gustave Doré's dramatic engraving of the Crucifixion of Jesus Christ, the ultimate fulfillment of God's redemptive plan.",
            "svg_content": SVG_LESSON_4,
            "youtube_id": "3dGO-wHQV4U",
            "youtube_title": "The Promised Messiah: The Fulfillment of Salvation",
            "youtube_description": "Traces the golden thread of God's redemptive promise from the seed of the woman in Genesis 3:15 through the prophets to Jesus Christ.",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Gustave Doré - The Crucifixion of Jesus Christ",
                        "content": {
                            "title": "Visual Hook: Gustave Doré - The Crucifixion of Jesus Christ",
                            "caption": "Gustave Doré's dramatic engraving of the Crucifixion of Jesus Christ, the ultimate fulfillment of God's redemptive plan."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: God's Salvation Plan",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Identify the **four immediate signs of God's grace** in Genesis 3 following the Fall.",
                                "Analyze the theological significance of the **Protoevangelium (Genesis 3:15)** as the first gospel promise.",
                                "Examine the **three major historical steps of redemption** fulfilled in Jesus Christ: Incarnation, Atonement, and Resurrection.",
                                "Contrast the **First Adam** with Jesus Christ, the **Last Adam**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Search in the Dark",
                        "content": {
                            "title": "God Initiates the Search for His Lost Children",
                            "text": "Imagine you have disobeyed your parents' instructions and accidentally shattered an expensive television screen. In absolute panic and fear of punishment, you run and hide in the darkest corner of your bedroom closet. As you sit there shivering, you hear your father's footsteps approaching. But instead of an angry shout, you hear a calm, gentle voice calling: *'Where are you? Come out, let us talk and make this right.'*\n\nThis is precisely how God reacted in Eden. Even before pronouncing judgment, God walked through the garden calling out to His lost, terrified children: *'Where are you?'*"
                        }
                    }
                ],
                # Card 2: Immediate Grace & Protoevangelium
                [
                    {
                        "type": "concept_explanation",
                        "title": "Four Immediate Signs of God's Grace in Genesis 3",
                        "content": {
                            "title": "Mercy in the Midst of Judgment",
                            "text": "Even as humanity fell, God's redeeming heart was immediately on display:\n\n- **1. God Initiated the Search (Gen 3:9)**: God took the first step, seeking out Adam and Eve rather than waiting for them to plead.\n- **2. God Questioned Them with Patience (Gen 3:11)**: God provided an opportunity for truth-telling, self-reflection, and confession.\n- **3. The Protoevangelium Promise (Gen 3:15)**: God pronounced that the seed of the woman would ultimately crush the head of the serpent.\n- **4. Providing Garments of Skin (Gen 3:21)**: God replaced their flimsy, perishable fig leaves with animal skins, demonstrating that covering human shame requires a sacrificial offering."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "The Protoevangelium: The First Gospel Announcement",
                        "content": {
                            "title": "Genesis 3:15 — The Seed of the Woman",
                            "definition": "The term **Protoevangelium** (from Greek *protos* = first, *evangelion* = good news/gospel) refers to Genesis 3:15:",
                            "dimensions": [
                                "> *'And I will put enmity between you and the woman, and between your offspring and hers; he will crush your head, and you will strike his heel.'*",
                                "- **The Serpent's Blow ('strike his heel')**: Foretells the temporary suffering and crucifixion of Jesus Christ on Calvary.",
                                "- **The Redeemer's Triumph ('crush your head')**: Foretells Christ's total, fatal defeat of Satan, sin, and death through the Resurrection."
                            ]
                        }
                    }
                ],
                # Card 3: Vector Blueprint & The 3 Pillars of Redemption
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The Arc of Salvation and 3 Redemptive Pillars",
                        "content": {
                            "title": "Vector Blueprint: The Arc of Salvation and 3 Redemptive Pillars",
                            "caption": "Timeline diagram showing the promise of Genesis 3:15 culminating in the Incarnation, Atonement, and victorious Resurrection.",
                            "svg": SVG_LESSON_4
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Three Major Steps of God's Redemptive Plan in Christ",
                        "content": {
                            "title": "How God Fulfilled Salvation Through History",
                            "text": "The promise of Genesis 3:15 was completely accomplished through Jesus Christ in three massive milestones:\n\n- **Step 1: The Incarnation (John 1:14)**: *'The Word became flesh and made his dwelling among us.'* God took on human nature to walk in our shoes, live a sinless life, and bridge the infinite gap between God and humanity.\n- **Step 2: The Atonement (Ephesians 1:7; Colossians 1:13-14)**: *'In him we have redemption through his blood, the forgiveness of sins.'* Christ died voluntarily as our substitute, paying our ransom debt on the cross.\n- **Step 3: The Resurrection (1 Corinthians 15:20, 45)**: Christ physically rose from the dead, breaking the chains of the grave forever and becoming the life-giving *Last Adam*."
                        }
                    }
                ],
                # Card 4: Video Integration & The Two Adams
                [
                    {
                        "type": "suggested_video",
                        "title": "Educational Video: The Promised Messiah",
                        "content": {
                            "title": "The Promised Messiah: The Fulfillment of Salvation",
                            "description": "Traces the golden thread of God's redemptive promise from the seed of the woman in Genesis 3:15 through the prophets to Jesus Christ.",
                            "url": "https://www.youtube.com/watch?v=3dGO-wHQV4U"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The Two Adams: The First Adam vs. The Last Adam",
                        "content": {
                            "headers": ["Aspect", "The First Adam (Genesis)", "The Last Adam — Jesus Christ (Gospels)"],
                            "rows": [
                                ["Environment", "Tested in a lush, abundant Garden of Eden", "Tested in a harsh, barren wilderness and Gethsemane"],
                                ["Action", "Disobeyed God's command in pride and self-exaltation", "Obeyed the Father perfectly, even unto death on a cross"],
                                ["Result for Humanity", "Brought sin, guilt, condemnation, and death", "Brought righteousness, forgiveness, justification, and life"],
                                ["Legacy", "Became a natural living soul that forfeited life", "Became a life-giving Spirit who raises believers to eternity"]
                            ]
                        }
                    }
                ],
                # Card 5: Step Process & Scripture Analysis
                [
                    {
                        "type": "step_process",
                        "title": "The 3 Milestones of Christ's Redemptive Fulfillment",
                        "content": {
                            "title": "How the Gospel Unfolds",
                            "steps": [
                                "1. **Incarnation**: Christ arrives as true God and true man, revealing the Father's heart and living in perfect obedience.",
                                "2. **Crucifixion & Atonement**: Christ bears the curse of the broken law, offering His blood as the complete ransom price for sin.",
                                "3. **Resurrection & Ascension**: Christ conquers death, ascends to glory, and pours out the Holy Spirit to empower believers."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Scripture Analysis: Comparing Fig Leaves and Animal Skins",
                        "content": {
                            "title": "Reflecting on Genesis 3:21",
                            "task": "1. Why were human-made fig leaves inadequate to cover Adam and Eve's nakedness and guilt?\n2. What had to take place for God to provide garments of animal skin (Genesis 3:21)?\n3. How does this Genesis sacrifice point directly forward to the sacrifice of the Lamb of God on Calvary?"
                        }
                    }
                ],
                # Card 6: Key Takeaways & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary: God's Plan of Salvation",
                        "content": {
                            "title": "Core Takeaways on Redemption in Christ",
                            "text": "- God responded to the Fall with **proactive grace**: searching for humanity and promising a Savior.\n- **Genesis 3:15 (The Protoevangelium)** is the first gospel promise that the seed of the woman will crush evil.\n- God's plan is fulfilled through **Incarnation** (God with us), **Atonement** (debt paid), and **Resurrection** (death defeated).\n- Jesus Christ is the **Last Adam**, reversing Adam's failure and offering eternal life to all who believe."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Protoevangelium",
                        "content": {
                            "question": "What is the theological term used to describe the 'first announcement of the gospel' found in Genesis 3:15?",
                            "options": [
                                "The Decalogue",
                                "The Protoevangelium",
                                "The Transfiguration",
                                "The Epiphany"
                            ],
                            "answer": "B",
                            "explanation": "Protoevangelium (meaning 'first gospel') refers to Genesis 3:15, where God first prophesied that the seed of the woman would ultimately crush the head of the serpent."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Christian Responses to God's Redemptive Work
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Christian Responses to God's Redemptive Work",
            "unit_description": "Exploring personal and communal Christian responses to redemption: faith, repentance (metanoia), gratitude, self-denial, perseverance, obedience, love, and witness.",
            "lesson_title": "Christian Responses to God's Redemptive Work",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Jean-Fran%C3%A7ois_Millet_-_The_Sower_-_Google_Art_Project.jpg/960px-Jean-Fran%C3%A7ois_Millet_-_The_Sower_-_Google_Art_Project.jpg",
            "image_caption": "Jean-François Millet's iconic painting 'The Sower', illustrating the biblical principle of surrender and planting seeds for spiritual fruitfulness.",
            "svg_content": SVG_LESSON_5,
            "youtube_id": "slyevQ1LW7A",
            "youtube_title": "Word Study: Agape (Sacrificial Love)",
            "youtube_description": "Explores how God's redemptive love (Agape) compels believers to live lives of genuine surrender, humility, and selfless service toward others.",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Jean-François Millet - The Sower",
                        "content": {
                            "title": "Visual Hook: Jean-François Millet - The Sower",
                            "caption": "Jean-François Millet's iconic painting 'The Sower', illustrating the biblical principle of surrender and planting seeds for spiritual fruitfulness."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Responding to Redemption",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Understand the **Principle of the Seed** in John 12:24-25 as the foundation of Christian discipleship.",
                                "Analyze the **9 core responses to redemption** categorized into three areas: toward God, personal character, and toward others.",
                                "Define **metanoia** (biblical repentance) as a radical transformation of heart, mind, and action.",
                                "Apply Christian values of **self-denial, obedience, love, and witness** to youth community life."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Principle of the Grain of Wheat",
                        "content": {
                            "title": "Surrender Before Fruitfulness",
                            "text": "Consider the profound teaching of Jesus in John 12:24-25:\n\n> *'Very truly I tell you, unless a kernel of wheat falls to the ground and dies, it remains only a single seed. But if it dies, it produces many seeds. Anyone who loves their life will lose it, while anyone who hates their life in this world will keep it for eternal life.'*\n\nJesus uses the simple agricultural analogy of a grain of wheat to teach that receiving redemption is not passive. Just as a seed must yield its hard outer shell and bury itself in the soil to produce an abundant crop, a Christian must surrender selfish desires to bear the fruit of a redeemed life."
                        }
                    }
                ],
                # Card 2: Responses Toward God & Metanoia
                [
                    {
                        "type": "concept_explanation",
                        "title": "Category A: Responding in Relation to God",
                        "content": {
                            "title": "Faith, Repentance, and Gratitude",
                            "text": "When we comprehend what Christ suffered on our behalf, our first responses are directed toward God:\n\n- **1. Faith and Belief**: Placing wholehearted trust in Jesus Christ as Lord and personal Savior, relying entirely on His cross for justification.\n- **2. True Repentance (Metanoia)**: A complete change of mindset, turning 180 degrees away from sin with genuine sorrow and walking toward God.\n- **3. Heartfelt Gratitude and Worship**: Expressing continuous thanksgiving through prayer, praise, and a lifestyle that honors God's grace."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Understanding Metanoia: True Biblical Repentance",
                        "content": {
                            "title": "The Meaning of 'Metanoia'",
                            "definition": "The Greek word **Metanoia** (often translated as repentance) means a deep, radical transformation of the mind and heart:",
                            "dimensions": [
                                "- **It is not merely feeling bad** about getting caught.",
                                "- **It is recognizing sin as offensive to God** and destructive to self and others.",
                                "- **It involves a conscious decision** to forsake dishonest patterns and walk in God's righteousness with the help of the Holy Spirit."
                            ]
                        }
                    }
                ],
                # Card 3: Vector Blueprint & Personal Character
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The 9-Fold Christian Response to Redemption",
                        "content": {
                            "title": "Vector Blueprint: The 9-Fold Christian Response to Redemption",
                            "caption": "Infographic showing the 9 core Christian responses organized across three domains: toward God, personal character, and toward others.",
                            "svg": SVG_LESSON_5
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Category B: Transforming Personal Character",
                        "content": {
                            "title": "Transformation, Self-Denial, and Perseverance",
                            "text": "Redemption produces internal moral fruit in our personal lives:\n\n- **4. Living a Transformed Life**: Allowing the Holy Spirit to renew our thoughts, speech, and moral standards rather than conforming to worldly pressures.\n- **5. Self-Denial and Sacrifice**: Daily choosing God's will and the welfare of others over our selfish appetites.\n- **6. Hope and Perseverance**: Anchoring our confidence in the promise of eternal life, keeping our heads high with joy even during trials and persecutions."
                        }
                    }
                ],
                # Card 4: Video Integration & Outward Expression
                [
                    {
                        "type": "suggested_video",
                        "title": "Educational Video: Agape (Selfless Love)",
                        "content": {
                            "title": "Word Study: Agape (Sacrificial Love)",
                            "description": "Explores how God's redemptive love (Agape) compels believers to live lives of genuine surrender, humility, and selfless service toward others.",
                            "url": "https://www.youtube.com/watch?v=slyevQ1LW7A"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Category C: Responding in Relation to Others",
                        "content": {
                            "title": "Obedience, Love, and Courageous Witness",
                            "text": "Authentic faith must overflow into our communities and schools:\n\n- **7. Moral Obedience and Integrity**: Living out God's moral commandments in our academics, relationships, and digital interactions.\n- **8. Radical Love and Service**: Practicing *Agape* love by extending practical kindness, helping the poor, and defending the vulnerable.\n- **9. Courageous Witness**: Unashamedly testifying to Christ's saving power through both our spoken words and upright moral conduct."
                        }
                    }
                ],
                # Card 5: Practical Matching Exercise & Self-Audit
                [
                    {
                        "type": "comparison_table",
                        "title": "Matching Activity: Christian Responses to Real-World Situations",
                        "content": {
                            "headers": ["Christian Response", "Real-World Practical Scenario in School/Community"],
                            "rows": [
                                ["1. Repentance (Metanoia)", "Going back to a classmate you slandered, sincerely apologizing, and setting the record straight with others."],
                                ["2. Self-Denial", "Sacrificing part of your weekend leisure time to tutor a struggling peer or clean the local church/community center."],
                                ["3. Courageous Witness", "Respectfully declining to join peers in abusing drugs or cheating, and boldly explaining how Christ guides your choices."],
                                ["4. Gratitude", "Beginning each school morning with a sincere prayer of thanksgiving despite facing financial or academic pressures."]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Self-Reflection: Auditing Your Personal Responses",
                        "content": {
                            "title": "Personal Spiritual Audit",
                            "task": "1. Which of the 9 Christian responses do you find easiest to practice in your daily routine?\n2. Which response poses the greatest challenge when you are with your peer group at school?\n3. Write down a concrete step you will take this week to practice self-denial for the benefit of someone in need."
                        }
                    }
                ],
                # Card 6: Key Takeaways & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary: Responding to God's Redemption",
                        "content": {
                            "title": "Core Takeaways on Christian Responses",
                            "text": "- Redemption demands an active response modeled on the **Principle of the Seed** (surrender leading to fruitfulness).\n- **Responses toward God**: Faith, Repentance (*Metanoia*), and continuous Gratitude.\n- **Personal Character**: Transformed living, daily Self-Denial, and steadfast Hope.\n- **Responses toward Others**: Moral Obedience, sacrificial *Agape* Love, and courageous Witness."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Biblical Repentance",
                        "content": {
                            "question": "What is the primary biblical meaning of 'metanoia' in the context of responding to God's redemptive grace?",
                            "options": [
                                "Performing ritual animal sacrifices to appease God's anger",
                                "Feeling temporary emotional regret only because one was caught breaking a rule",
                                "A complete, genuine change of mind, heart, and direction that turns from sin toward God",
                                "Achieving flawless moral perfection without ever needing God's grace again"
                            ],
                            "answer": "C",
                            "explanation": "Metanoia signifies a transformative shift in mindset and heart, leading a person to turn away from sin and deliberately follow God in faith and obedience."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Embracing God's Redemptive Work in Daily Life
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Embracing God's Redemptive Work in Daily Life",
            "unit_description": "Personalizing redemption through John 3:16, maintaining a daily reflection journal, making ethical decisions, and integrating Christian values into 21st-century Kenyan society.",
            "lesson_title": "Embracing God's Redemptive Work in Daily Life",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/%28Venice%29_The_parable_of_the_Good_Samaritan_by_Domenico_Fetti_-_Gallerie_Accademia.jpg/960px-%28Venice%29_The_parable_of_the_Good_Samaritan_by_Domenico_Fetti_-_Gallerie_Accademia.jpg",
            "image_caption": "Domenico Fetti's painting of the Good Samaritan, capturing the active, sacrificial expression of Christ's love in everyday life.",
            "svg_content": SVG_LESSON_6,
            "youtube_id": "g_qLPgoqqxU",
            "youtube_title": "John 3:16 and the Meaning of Eternal Life",
            "youtube_description": "Explores how John 3:16 captures the heart of God's redemptive love and invites every individual into transformed daily living and eternal fellowship with God.",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Domenico Fetti - The Good Samaritan",
                        "content": {
                            "title": "Visual Hook: Domenico Fetti - The Good Samaritan",
                            "caption": "Domenico Fetti's painting of the Good Samaritan, capturing the active, sacrificial expression of Christ's love in everyday life."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Living the Redeemed Life",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Analyze **John 3:16** as the foundational heart and universal invitation of redemption.",
                                "Implement the **5-step Daily Reflection Journal** cycle into personal student life.",
                                "Apply redemptive values to real-world youth challenges: academic integrity, digital peer pressure, and family relationships.",
                                "Synthesize the complete theological arc of Topic 1.3."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction: The Heart of the Gospel (John 3:16)",
                        "content": {
                            "title": "The Greatest Demonstration of Love",
                            "text": "Let us reflect upon the central verse of the New Testament:\n\n> *'For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.'* (John 3:16)\n\nJohn 3:16 is the pinnacle of the redemption narrative. It reveals that the motive behind God's heavy rescue mission is pure, radical love, and the invitation is extended to *'whoever'* is willing to believe. Redemption is not an ancient relic; it is an active, daily reality."
                        }
                    }
                ],
                # Card 2: Moving from Theory to Daily Action
                [
                    {
                        "type": "concept_explanation",
                        "title": "Moving from Doctrine to Daily Practice",
                        "content": {
                            "title": "How Does Redemption Change a Student's Daily Reality?",
                            "text": "If redemption remains only a set of facts memorized for an exam, its transformative power is lost. A redeemed Grade 10 student displays tangible differences in daily life:\n\n- **In the Classroom**: Pursuing academic excellence through honest hard work, rejecting cheating and plagiarism.\n- **Among Friends**: Resisting toxic peer pressure, refusing to participate in cyberbullying or gossip, and standing up for the mistreated.\n- **At Home**: Honoring parents and guardians, contributing willingly to family chores, and offering quick apologies when mistakes happen.\n- **In the Community**: Looking for opportunities to serve those in need with humility and compassion."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The 5-Step Daily Reflection Journal Cycle",
                        "content": {
                            "title": "The Daily Personal Audit for Christian Growth",
                            "steps": [
                                "1. **Repentance & Confession**: Honestly identifying and confessing any wrongful words, dishonest actions, or unloving attitudes committed during the day.",
                                "2. **Gratitude Check**: Listing at least three specific blessings and moments of divine protection experienced today.",
                                "3. **Neighborly Love Check**: Reviewing how you practically demonstrated Christ's love to classmates, teachers, or family members.",
                                "4. **Step of Faith**: Recalling how you chose moral integrity over an easy compromise when tempted today.",
                                "5. **Prayer & Witness**: Praying for Holy Spirit strength and seeking opportunities to encourage someone tomorrow."
                            ]
                        }
                    }
                ],
                # Card 3: Vector Blueprint & Journal Prompts
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The 5-Step Daily Reflection Loop",
                        "content": {
                            "title": "Vector Blueprint: The 5-Step Daily Reflection Loop",
                            "caption": "Workflow diagram showing the continuous cycle of daily repentance, gratitude, neighborly love, steps of faith, and prayer.",
                            "svg": SVG_LESSON_6
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Daily Journaling Prompts for Students",
                        "content": {
                            "title": "Guiding Questions for Your Daily CRE Journal",
                            "text": "Every learner is encouraged to reflect on these five daily prompts:\n\n- **Prompt 1 (Integrity)**: *'Did I cut corners, tell a lie, or act pridefully today? Lord, forgive me and grant me strength to make it right.'*\n- **Prompt 2 (Praise)**: *'What three gifts of health, friendship, or provision am I deeply thankful for today?'*\n- **Prompt 3 (Service)**: *'Who was lonely, sad, or struggling around me, and how did I support them?'*\n- **Prompt 4 (Moral Courage)**: *'How did I uphold Christian values when faced with peer pressure today?'*\n- **Prompt 5 (Mission)**: *'How can I share the light and peace of Jesus with a friend tomorrow?'*"
                        }
                    }
                ],
                # Card 4: Video Integration & Modern Dilemmas
                [
                    {
                        "type": "suggested_video",
                        "title": "Educational Video: Eternal Life and Daily Living",
                        "content": {
                            "title": "John 3:16 and the Meaning of Eternal Life",
                            "description": "Explores how John 3:16 captures the heart of God's redemptive love and invites every individual into transformed daily living and eternal fellowship with God.",
                            "url": "https://www.youtube.com/watch?v=g_qLPgoqqxU"
                        }
                    },
                    {
                        "type": "ethical_scenario",
                        "title": "Modern Dilemma: Cyberbullying and Digital Integrity",
                        "content": {
                            "scenario": "A WhatsApp class group begins circulating humiliating memes and mocking comments about a quiet student whose family cannot afford the latest school uniform. Several classmates add laughing emojis and forwarding tags.",
                            "reflection": "As a redeemed Christian student, how should you respond? Silence and laughter make one an accomplice to cruelty. The redeemed response is to **refuse to forward the hurtful media, privately encourage the targeted classmate, and respectfully urge the group administrators to uphold human dignity and kindness**."
                        }
                    }
                ],
                # Card 5: Topic 1.3 Synthesis & Performance Task
                [
                    {
                        "type": "concept_explanation",
                        "title": "Topic 1.3 Synthesis: The Grand Story of Redemption",
                        "content": {
                            "title": "Connecting All Threads of Topic 1.3",
                            "text": "Let us summarize the core theological journey of Topic 1.3:\n\n- **1. Redemption Defined**: The costly divine rescue that buys back, delivers, liberates, and restores humanity from spiritual bondage.\n- **2. The Genesis Fall**: Humanity chose doubt, disobedience, and self-exaltation over trust in God's protective boundary.\n- **3. Shattered Creation**: Sin fractured our relationship with God, inner peace, interpersonal harmony, and the earth.\n- **4. God's Salvation Plan**: God took the initiative in Genesis 3:15, fulfilling the Protoevangelium through Christ's Incarnation, Atonement, and victorious Resurrection.\n- **5. The Active Response**: Discipleship requires dying to self like a grain of wheat, walking in repentance, gratitude, love, and courageous witness.\n- **6. Daily Application**: Living out John 3:16 through daily reflection, moral courage, and selfless community service."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: 7-Day Faith and Integrity Plan",
                        "content": {
                            "title": "Your Personal 7-Day Action Plan",
                            "task": "1. Create a dedicated section in your CRE exercise book titled 'My Daily Walk with God'.\n2. For the next 7 consecutive days, spend 5 minutes every evening writing short answers to the 5 Daily Prompts.\n3. Identify one specific classmate or neighbor to whom you will offer a concrete act of Christian kindness this week."
                        }
                    }
                ],
                # Card 6: Key Takeaways & Summative Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary: Embracing God's Redemption",
                        "content": {
                            "title": "Core Takeaways on Living the Redeemed Life",
                            "text": "- **John 3:16** anchors redemption in the unconditional, self-giving love of God for all people.\n- Daily Christian maturity is nurtured through the **5-step reflection loop** (Repentance, Gratitude, Love, Faith, Prayer).\n- Redeemed living transforms **school character, digital ethics, family relationships, and community service**.\n- Redemption is not merely a past event, but a living, everyday walk of faith and moral courage."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Topic Knowledge Check: God's Redemptive Plan",
                        "content": {
                            "question": "Which sequence correctly reflects the historical and theological fulfillment of God's redemptive plan from the Fall of Man to the Christian life?",
                            "options": [
                                "The Fall in Eden -> Building the Tower of Babel -> Complete human self-reformation -> Eternal life",
                                "The Fall in Eden -> Genesis 3:15 Protoevangelium -> Christ's Incarnation, Atonement & Resurrection -> Active Christian response in daily life",
                                "Human moral perfection -> Incarnation of Christ -> The Fall in Genesis 3 -> Animal sacrifices for salvation",
                                "Disobedience in Eden -> Ignoring sin's consequences -> Automatic universal salvation without faith or repentance"
                            ],
                            "answer": "B",
                            "explanation": "God's redemptive arc begins after the Fall with the Genesis 3:15 Protoevangelium promise, reaches its climactic fulfillment in the Incarnation, Atonement, and Resurrection of Jesus Christ, and is received through active faith, repentance, and daily discipleship."
                        }
                    }
                ]
            ]
        }
    ]


# =============================================================================
# DATABASE INGESTION CONTROLLER
# =============================================================================

def ingest_topic_1_3(replace=False):
    """Ingests Grade 10 CRE Topic 1.3 into the Django database with complete enrichment."""
    print("=" * 80)
    print("STARTING INGESTION: Grade 10 CRE Topic 1.3: Redemption after the Fall of Man")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' not found in database!")
    print(f"Resolved Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade 10
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC curriculum!")
    print(f"Resolved Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    # 3. Resolve Subject CRE (ID: 46)
    subject = Subject.objects.filter(grade=grade, name__icontains="CRE").first()
    if not subject:
        subject = Subject.objects.filter(id=46).first()
    if not subject:
        raise ValueError("Subject 'CRE' (ID: 46) not found under Grade 10!")
    print(f"Resolved Subject: {subject.name} (ID: {subject.id})")

    # 4. Resolve or Create Topic 1.3 (Order: 3)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=3,
        defaults={
            "name": "Topic 1.3: Redemption after the Fall of Man",
            "description": "Explores the introduction of sin into the world in Genesis 3, its multi-dimensional consequences, God's promise of salvation fulfilled through Jesus Christ, and Christian responses in daily life."
        }
    )
    if not t_created:
        topic.name = "Topic 1.3: Redemption after the Fall of Man"
        topic.description = "Explores the introduction of sin into the world in Genesis 3, its multi-dimensional consequences, God's promise of salvation fulfilled through Jesus Christ, and Christian responses in daily life."
        topic.save()
    print(f"Resolved Topic 1.3: {topic.name} (ID: {topic.id}, Created: {t_created})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 1.3...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic_1_3_curriculum()
    
    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for item in curriculum_data:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            pages = item["pages"]

            # Create or update LearningUnit
            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": u_desc}
            )
            if not u_created:
                unit.name = u_name
                unit.description = u_desc
                unit.save()
            total_units += 1

            # Create or update Lesson
            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": l_title,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "author": "VLearn Senior CRE Curriculum Agent",
                        "grade": "Grade 10",
                        "subject": "CRE",
                        "topic_order": 3,
                        "unit_order": u_order
                    }
                }
            )
            if not l_created:
                lesson.title = l_title
                lesson.status = "published"
                lesson.version = 1
                lesson.immutable_metadata = {
                    "author": "VLearn Senior CRE Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "CRE",
                    "topic_order": 3,
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
                url=item["image_url"],
                metadata={"caption": item["image_caption"], "source": "Wikimedia Commons"}
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
                metadata={"svg_content": item["svg_content"]}
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
                title=item["youtube_title"],
                url=f"https://www.youtube.com/watch?v={item['youtube_id']}",
                metadata={"youtube_id": item["youtube_id"], "description": item["youtube_description"]}
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
                        b_content["resolved_image_url"] = item["image_url"]
                        b_content["url"] = item["image_url"]
                        b_content["source"] = "Wikimedia Commons"
                    elif b_type == "suggested_diagram":
                        b_content["svg"] = item["svg_content"]
                        b_content["svg_xml"] = item["svg_content"]
                    elif b_type == "suggested_video":
                        b_content["url"] = f"https://www.youtube.com/watch?v={item['youtube_id']}"
                        b_content["youtube_id"] = item["youtube_id"]

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t1_3_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_order_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 3, "unit_order": u_order, "page": page_idx}
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

            print(f"  Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks, 3 Assets)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 1.3 '{topic.name}'")
    print(f"  Total Learning Units: {total_units}")
    print(f"  Total Published Lessons: {total_lessons}")
    print(f"  Total Progressive Pages: {total_pages}")
    print(f"  Total Enriched Blocks: {total_blocks}")
    print(f"  Total Attached Assets: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_topic_1_3(replace=replace_flag)
