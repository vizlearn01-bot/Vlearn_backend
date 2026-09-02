"""
VLearn CBC Grade 10 CRE — Topic 1.7: Loyalty to God (Elijah)
Comprehensive Ingestion & Enrichment Script

Ingests:
  - Topic: Topic 1.7: Loyalty to God (Elijah) (Order: 7) under Grade 10 CRE (Subject ID: 46)
  - 6 Discrete Learning Units:
      1. Modern Forms of Idol Worship and Religious Extremism
      2. Discerning and Avoiding Ungodly Groups
      3. Elijah's Fight Against Baalism (Mount Carmel Showdown)
      4. Elijah's Flight to Mount Horeb and Divine Restoration
      5. Elijah's Defense of Social Justice (Naboth's Vineyard)
      6. Promoting Social Justice in Modern Society
  - 6 Published Lessons (status='published', version=1)
  - 6 Progressive Cards per Lesson with rich components:
      * Card 1: Verified Wikimedia Hook + Learning Goals + Context Hook
      * Card 2: Core Concept Explanation + Deep Explanations / Scripture Insights
      * Card 3: Responsive Vector SVG Diagram (viewBox 0 0 800 450, #0f172a theme) + Analytic Callout
      * Card 4: Curated YouTube Video + In-depth Theological/Societal Reflection
      * Card 5: Step Process / Ethical Scenario / Values Application
      * Card 6: Key Takeaway Summary + Knowledge Check MCQ (4 Options, Answer, Detailed Explanation)
  - Complete LessonAsset records linked to blocks for images, diagrams, and videos.
  - Full sanitization: 0 bracket citations, 0 internal tags.
"""

import os
import sys
import uuid
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from django.utils import timezone
from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

# -----------------------------------------------------------------------------
# SVGs Data (Sanitized, viewBox="0 0 800 450", #0f172a / dark theme, responsive)
# -----------------------------------------------------------------------------

SVG_1_IDOLATRY = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="cardAncient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991b1b" />
      <stop offset="100%" stop-color="#7f1d1d" />
    </linearGradient>
    <linearGradient id="cardModern" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e40af" />
      <stop offset="100%" stop-color="#1e3a8a" />
    </linearGradient>
    <filter id="shadow1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad1)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="45" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="22" fill="#f8fafc" text-anchor="middle">THE EVOLUTION OF IDOLATRY: ANCIENT VS. MODERN</text>
  <text x="400" y="70" font-family="Segoe UI, Inter, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">From External Statues to Inward Heart-Level Devotions (Matthew 6:24)</text>

  <!-- Ancient Idolatry Card -->
  <g filter="url(#shadow1)">
    <rect x="40" y="95" width="320" height="310" rx="10" fill="url(#cardAncient)" stroke="#f87171" stroke-width="1.5"/>
    <rect x="55" y="110" width="290" height="36" rx="6" fill="#450a0a"/>
    <text x="200" y="134" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="15" fill="#fca5a5" text-anchor="middle">ANCIENT IDOLATRY</text>

    <!-- Content Items -->
    <rect x="55" y="160" width="290" height="48" rx="6" fill="#5c1212"/>
    <text x="70" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff">Physical Objects</text>
    <text x="70" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#fecaca">Wood, stone, gold images (Baal, Asherah)</text>

    <rect x="55" y="218" width="290" height="48" rx="6" fill="#5c1212"/>
    <text x="70" y="238" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff">Localized Deity Cults</text>
    <text x="70" y="256" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#fecaca">Territorial gods of rain, storm, and war</text>

    <rect x="55" y="276" width="290" height="48" rx="6" fill="#5c1212"/>
    <text x="70" y="296" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff">Ritual Transactions</text>
    <text x="70" y="314" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#fecaca">Physical sacrifices &amp; sensual rituals for gain</text>

    <rect x="55" y="334" width="290" height="52" rx="6" fill="#450a0a" stroke="#f87171" stroke-width="1"/>
    <text x="200" y="354" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#fca5a5" text-anchor="middle">Root Motive: Control Nature</text>
    <text x="200" y="372" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#fee2e2" text-anchor="middle">Manipulating unseen powers for fertility &amp; wealth</text>
  </g>

  <!-- Central Bridge -->
  <g>
    <circle cx="400" cy="245" r="28" fill="#334155" stroke="#64748b" stroke-width="2"/>
    <path d="M 390 245 L 410 245 M 404 239 L 410 245 L 404 251" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <text x="400" y="290" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#38bdf8" text-anchor="middle">TRANSIT</text>
    <text x="400" y="306" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Heart Posture</text>
  </g>

  <!-- Modern Idolatry Card -->
  <g filter="url(#shadow1)">
    <rect x="440" y="95" width="320" height="310" rx="10" fill="url(#cardModern)" stroke="#60a5fa" stroke-width="1.5"/>
    <rect x="455" y="110" width="290" height="36" rx="6" fill="#0f172a"/>
    <text x="600" y="134" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="15" fill="#93c5fd" text-anchor="middle">MODERN HEART IDOLATRY</text>

    <!-- Content Items -->
    <rect x="455" y="160" width="290" height="48" rx="6" fill="#1e3a5f"/>
    <text x="470" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff">Materialism (Mammon)</text>
    <text x="470" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#bfdbfe">Wealth &amp; possessions as ultimate security</text>

    <rect x="455" y="218" width="290" height="48" rx="6" fill="#1e3a5f"/>
    <text x="470" y="238" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff">Self-Worship &amp; Social Clout</text>
    <text x="470" y="256" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#bfdbfe">Narcissism, digital fame, personal autonomy</text>

    <rect x="455" y="276" width="290" height="48" rx="6" fill="#1e3a5f"/>
    <text x="470" y="296" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff">Extremism &amp; Cultic Devotion</text>
    <text x="470" y="314" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#bfdbfe">Blind obedience to charismatic human leaders</text>

    <rect x="455" y="334" width="290" height="52" rx="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1"/>
    <text x="600" y="354" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#93c5fd" text-anchor="middle">Root Motive: Replacing God</text>
    <text x="600" y="372" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#dbeafe" text-anchor="middle">Good created gifts elevated to ultimate priorities</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="180" y="415" width="440" height="24" rx="4" fill="#1e293b"/>
  <text x="400" y="432" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Core Biblical Diagnosis: Idolatry is elevating anything above undivided loyalty to God.</text>
</svg>'''

SVG_2_DISCERNMENT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad2)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="22" fill="#f8fafc" text-anchor="middle">THE 4-PILLAR DISCERNMENT FILTER</text>
  <text x="400" y="68" font-family="Segoe UI, Inter, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Biblical Safeguards Against Deceptive &amp; Cultic Groups (1 John 4:1, Matthew 7:15-20)</text>

  <!-- 4 Pillars Container Grid -->
  <!-- Pillar 1: Sound Doctrine -->
  <g filter="url(#shadow2)">
    <rect x="35" y="95" width="165" height="315" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="45" y="105" width="145" height="35" rx="5" fill="#0369a1"/>
    <text x="117" y="128" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff" text-anchor="middle">1. DOCTRINE</text>
    
    <text x="117" y="165" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#7dd3fc" text-anchor="middle">Christology</text>
    <text x="117" y="185" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Confesses Jesus as</text>
    <text x="117" y="202" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Lord incarnate.</text>

    <line x1="50" y1="218" x2="185" y2="218" stroke="#334155" stroke-width="1"/>

    <text x="117" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#f87171" text-anchor="middle">Red Flag Check</text>
    <text x="117" y="260" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">Claims exclusive "new</text>
    <text x="117" y="276" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">revelations" that</text>
    <text x="117" y="292" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">override Scripture.</text>

    <rect x="45" y="340" width="145" height="55" rx="5" fill="#0f172a" stroke="#0369a1" stroke-width="1"/>
    <text x="117" y="360" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#38bdf8" text-anchor="middle">Reference</text>
    <text x="117" y="380" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">1 John 4:1-3</text>
  </g>

  <!-- Pillar 2: Fruit & Morals -->
  <g filter="url(#shadow2)">
    <rect x="225" y="95" width="165" height="315" rx="8" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
    <rect x="235" y="105" width="145" height="35" rx="5" fill="#15803d"/>
    <text x="307" y="128" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff" text-anchor="middle">2. FRUIT</text>

    <text x="307" y="165" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#86efac" text-anchor="middle">Moral Character</text>
    <text x="307" y="185" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Demonstrates love,</text>
    <text x="307" y="202" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">humility &amp; integrity.</text>

    <line x1="240" y1="218" x2="375" y2="218" stroke="#334155" stroke-width="1"/>

    <text x="307" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#f87171" text-anchor="middle">Red Flag Check</text>
    <text x="307" y="260" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">Greed, secret sins,</text>
    <text x="307" y="276" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">arrogance, financial</text>
    <text x="307" y="292" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">extortion of flock.</text>

    <rect x="235" y="340" width="145" height="55" rx="5" fill="#0f172a" stroke="#15803d" stroke-width="1"/>
    <text x="307" y="360" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#4ade80" text-anchor="middle">Reference</text>
    <text x="307" y="380" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Matthew 7:16-20</text>
  </g>

  <!-- Pillar 3: Accountability -->
  <g filter="url(#shadow2)">
    <rect x="415" y="95" width="165" height="315" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="425" y="105" width="145" height="35" rx="5" fill="#b45309"/>
    <text x="497" y="128" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff" text-anchor="middle">3. GOVERNANCE</text>

    <text x="497" y="165" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#fcd34d" text-anchor="middle">Accountability</text>
    <text x="497" y="185" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Open to elders,</text>
    <text x="497" y="202" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">law, and questions.</text>

    <line x1="430" y1="218" x2="565" y2="218" stroke="#334155" stroke-width="1"/>

    <text x="497" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#f87171" text-anchor="middle">Red Flag Check</text>
    <text x="497" y="260" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">Autocratic leader,</text>
    <text x="497" y="276" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">punishes questioning,</text>
    <text x="497" y="292" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">isolates from family.</text>

    <rect x="425" y="340" width="145" height="55" rx="5" fill="#0f172a" stroke="#b45309" stroke-width="1"/>
    <text x="497" y="360" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#f59e0b" text-anchor="middle">Reference</text>
    <text x="497" y="380" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">James 5:16</text>
  </g>

  <!-- Pillar 4: Handling Scripture -->
  <g filter="url(#shadow2)">
    <rect x="605" y="95" width="165" height="315" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
    <rect x="615" y="105" width="145" height="35" rx="5" fill="#7e22ce"/>
    <text x="687" y="128" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff" text-anchor="middle">4. SCRIPTURE</text>

    <text x="687" y="165" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#e9d5ff" text-anchor="middle">Contextual Truth</text>
    <text x="687" y="185" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Accurately handles</text>
    <text x="687" y="202" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">the Word of Truth.</text>

    <line x1="620" y1="218" x2="755" y2="218" stroke="#334155" stroke-width="1"/>

    <text x="687" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#f87171" text-anchor="middle">Red Flag Check</text>
    <text x="687" y="260" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">Twisting verses out</text>
    <text x="687" y="276" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">of context for fear,</text>
    <text x="687" y="292" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#cbd5e1" text-anchor="middle">money, or control.</text>

    <rect x="615" y="340" width="145" height="55" rx="5" fill="#0f172a" stroke="#7e22ce" stroke-width="1"/>
    <text x="687" y="360" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#c084fc" text-anchor="middle">Reference</text>
    <text x="687" y="380" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">2 Timothy 2:15</text>
  </g>

  <!-- Bottom Footer -->
  <text x="400" y="432" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Test every spiritual claim: Truth never fears honest biblical examination.</text>
</svg>'''

SVG_3_MOUNT_CARMEL = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="fireGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="40%" stop-color="#f97316" />
      <stop offset="100%" stop-color="#dc2626" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad3)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="22" fill="#f8fafc" text-anchor="middle">THE CONTEST ON MOUNT CARMEL (1 KINGS 18)</text>
  <text x="400" y="68" font-family="Segoe UI, Inter, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">The God Who Answers By Fire vs. The Ineffective Rites of Baal</text>

  <!-- Left Side: 450 Prophets of Baal -->
  <g>
    <rect x="40" y="95" width="320" height="310" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect x="55" y="110" width="290" height="34" rx="5" fill="#334155"/>
    <text x="200" y="133" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="14" fill="#cbd5e1" text-anchor="middle">450 PROPHETS OF BAAL</text>

    <!-- Altar / Sacrifice -->
    <rect x="70" y="160" width="260" height="40" rx="4" fill="#0f172a"/>
    <text x="200" y="184" font-family="Segoe UI, Inter, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">State-Funded Pagan Altar</text>

    <rect x="70" y="210" width="260" height="55" rx="4" fill="#0f172a"/>
    <text x="200" y="232" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#f87171" text-anchor="middle">Frantic Human Effort</text>
    <text x="200" y="250" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Morning to evening shouting, slashing</text>

    <rect x="70" y="275" width="260" height="50" rx="4" fill="#0f172a"/>
    <text x="200" y="297" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#f87171" text-anchor="middle">Prayer: "O Baal, hear us!"</text>
    <text x="200" y="313" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Senseless noise, repetitive chanting</text>

    <!-- Result -->
    <rect x="55" y="340" width="290" height="50" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="200" y="362" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="14" fill="#fca5a5" text-anchor="middle">RESULT: COMPLETE SILENCE</text>
    <text x="200" y="380" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#fee2e2" text-anchor="middle">"No voice, no answer, no one paid attention"</text>
  </g>

  <!-- Right Side: Elijah & Yahweh -->
  <g>
    <rect x="440" y="95" width="320" height="310" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="455" y="110" width="290" height="34" rx="5" fill="#78350f"/>
    <text x="600" y="133" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="14" fill="#fef08a" text-anchor="middle">ELIJAH &amp; YAHWEH</text>

    <!-- Altar of 12 Stones -->
    <rect x="470" y="160" width="260" height="40" rx="4" fill="#0f172a"/>
    <text x="600" y="178" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#38bdf8" text-anchor="middle">Rebuilt Altar of 12 Stones</text>
    <text x="600" y="193" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Covenant unity + 12 jars of soaking water</text>

    <!-- Simple Faithful Prayer -->
    <rect x="470" y="210" width="260" height="55" rx="4" fill="#0f172a"/>
    <text x="600" y="232" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#38bdf8" text-anchor="middle">Quiet 60-Word Prayer</text>
    <text x="600" y="250" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Appealing to God of Abraham, Isaac &amp; Israel</text>

    <!-- Fire from Heaven Graphic -->
    <path d="M 590 270 L 610 270 L 600 320 Z" fill="url(#fireGrad)" filter="url(#glow)"/>
    <text x="600" y="300" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">FIRE FALLS</text>

    <!-- Result -->
    <rect x="455" y="340" width="290" height="50" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
    <text x="600" y="362" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#86efac" text-anchor="middle">RESULT: SUPERNATURAL RESPONSE</text>
    <text x="600" y="380" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#dcfce7" text-anchor="middle">Consumes bull, stones, dust &amp; trench water</text>
  </g>

  <!-- Center Dynamic Badge -->
  <g>
    <circle cx="400" cy="245" r="26" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="400" y="243" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#fbbf24" text-anchor="middle">THE</text>
    <text x="400" y="256" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#f8fafc" text-anchor="middle">TEST</text>
  </g>

  <!-- Bottom Banner -->
  <text x="400" y="432" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">People's Confession: "The Lord—He is God! The Lord—He is God!" (1 Kings 18:39)</text>
</svg>'''

SVG_4_HOREB_RESTORATION = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="stepGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857" />
      <stop offset="100%" stop-color="#064e3b" />
    </linearGradient>
    <linearGradient id="stepGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0369a1" />
      <stop offset="100%" stop-color="#0c4a6e" />
    </linearGradient>
    <linearGradient id="stepGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#4c1d95" />
    </linearGradient>
    <filter id="shadow4" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad4)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="22" fill="#f8fafc" text-anchor="middle">GOD'S HOLISTIC CARE IN BURNOUT (1 KINGS 19)</text>
  <text x="400" y="68" font-family="Segoe UI, Inter, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">How God Responded to Elijah's Despair, Isolation, and Exhaustion</text>

  <!-- 3 Major Horizontal Steps -->
  <!-- Step 1: Physical Care -->
  <g filter="url(#shadow4)">
    <rect x="40" y="100" width="220" height="300" rx="10" fill="url(#stepGrad1)" stroke="#34d399" stroke-width="1.5"/>
    <rect x="55" y="115" width="190" height="32" rx="5" fill="#022c22"/>
    <text x="150" y="136" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#6ee7b7" text-anchor="middle">1. PHYSICAL REST</text>

    <rect x="55" y="160" width="190" height="50" rx="5" fill="#065f46"/>
    <text x="150" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Sleep &amp; Nourishment</text>
    <text x="150" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#d1fae5" text-anchor="middle">Angel provides baked bread</text>

    <rect x="55" y="220" width="190" height="50" rx="5" fill="#065f46"/>
    <text x="150" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">No Rebukes</text>
    <text x="150" y="258" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#d1fae5" text-anchor="middle">God respects human limits</text>

    <rect x="55" y="280" width="190" height="50" rx="5" fill="#065f46"/>
    <text x="150" y="300" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Renewed Strength</text>
    <text x="150" y="318" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#d1fae5" text-anchor="middle">Travels 40 days to Horeb</text>

    <text x="150" y="365" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#a7f3d0" text-anchor="middle">"The journey is too much for you"</text>
    <text x="150" y="382" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#ecfdf5" text-anchor="middle">(1 Kings 19:7)</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 270 250 L 285 250" stroke="#34d399" stroke-width="3" stroke-linecap="round" fill="none"/>

  <!-- Step 2: Spiritual Intimacy -->
  <g filter="url(#shadow4)">
    <rect x="290" y="100" width="220" height="300" rx="10" fill="url(#stepGrad2)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="305" y="115" width="190" height="32" rx="5" fill="#082f49"/>
    <text x="400" y="136" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#7dd3fc" text-anchor="middle">2. GENTLE PRESENCE</text>

    <rect x="305" y="160" width="190" height="50" rx="5" fill="#075985"/>
    <text x="400" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Not in the Storm</text>
    <text x="400" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e0f2fe" text-anchor="middle">Wind, earthquake, &amp; fire pass</text>

    <rect x="305" y="220" width="190" height="50" rx="5" fill="#075985"/>
    <text x="400" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">The Gentle Whisper</text>
    <text x="400" y="258" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e0f2fe" text-anchor="middle">Quiet, intimate communion</text>

    <rect x="305" y="280" width="190" height="50" rx="5" fill="#075985"/>
    <text x="400" y="300" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Honest Lament</text>
    <text x="400" y="318" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e0f2fe" text-anchor="middle">Elijah vents fear &amp; sorrow</text>

    <text x="400" y="365" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#bae6fd" text-anchor="middle">"After the fire came a gentle whisper"</text>
    <text x="400" y="382" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#f0f9ff" text-anchor="middle">(1 Kings 19:12)</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 520 250 L 535 250" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" fill="none"/>

  <!-- Step 3: Recommissioning & Community -->
  <g filter="url(#shadow4)">
    <rect x="540" y="100" width="220" height="300" rx="10" fill="url(#stepGrad3)" stroke="#c084fc" stroke-width="1.5"/>
    <rect x="555" y="115" width="190" height="32" rx="5" fill="#2e1065"/>
    <text x="650" y="136" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#d8b4fe" text-anchor="middle">3. RECOMMISSIONING</text>

    <rect x="555" y="160" width="190" height="50" rx="5" fill="#581c87"/>
    <text x="650" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Clear Strategic Tasks</text>
    <text x="650" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#f3e8ff" text-anchor="middle">Anoint kings Hazael &amp; Jehu</text>

    <rect x="555" y="220" width="190" height="50" rx="5" fill="#581c87"/>
    <text x="650" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Succession &amp; Partner</text>
    <text x="650" y="258" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#f3e8ff" text-anchor="middle">Call Elisha to join him</text>

    <rect x="555" y="280" width="190" height="50" rx="5" fill="#581c87"/>
    <text x="650" y="300" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Shattering Isolation</text>
    <text x="650" y="318" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#f3e8ff" text-anchor="middle">7,000 faithful remnant reserved</text>

    <text x="650" y="365" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#e9d5ff" text-anchor="middle">"Go back the way you came"</text>
    <text x="650" y="382" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#faf5ff" text-anchor="middle">(1 Kings 19:15)</text>
  </g>

  <!-- Bottom Summary -->
  <text x="400" y="432" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Spiritual exhaustion is resolved through physical rest, gentle communion with God, and purposeful action.</text>
</svg>'''

SVG_5_NABOTH_VINEYARD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="injusticeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#881337" />
      <stop offset="100%" stop-color="#4c0519" />
    </linearGradient>
    <filter id="shadow5" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad5)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="22" fill="#f8fafc" text-anchor="middle">NABOTH'S VINEYARD &amp; PROPHETIC JUSTICE (1 KINGS 21)</text>
  <text x="400" y="68" font-family="Segoe UI, Inter, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">The Crime of Royal Tyranny and Yahweh's Defense of the Vulnerable</text>

  <!-- Flowchart Container -->
  <!-- Box 1: Covetousness -->
  <g filter="url(#shadow5)">
    <rect x="35" y="95" width="220" height="310" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect x="45" y="105" width="200" height="32" rx="5" fill="#881337"/>
    <text x="145" y="126" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#fecdd3" text-anchor="middle">1. GREED &amp; REFUSAL</text>

    <text x="145" y="160" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#fda4af" text-anchor="middle">Ahab's Demand</text>
    <text x="145" y="180" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Wants Naboth's ancestral</text>
    <text x="145" y="196" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">vineyard for a garden.</text>

    <line x1="50" y1="210" x2="235" y2="210" stroke="#334155" stroke-width="1"/>

    <text x="145" y="235" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#38bdf8" text-anchor="middle">Naboth's Loyalty</text>
    <text x="145" y="255" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">"The Lord forbid that I</text>
    <text x="145" y="271" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">give you my ancestral</text>
    <text x="145" y="287" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">heritage" (Lev. 25:23).</text>

    <rect x="45" y="320" width="200" height="70" rx="5" fill="#0f172a"/>
    <text x="145" y="345" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Ahab sulks in bed,</text>
    <text x="145" y="365" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">refusing food.</text>
  </g>

  <!-- Flow Arrow 1 -->
  <path d="M 265 250 L 285 250" stroke="#f43f5e" stroke-width="3" stroke-linecap="round" fill="none"/>

  <!-- Box 2: Judicial Murder -->
  <g filter="url(#shadow5)">
    <rect x="290" y="95" width="220" height="310" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect x="300" y="105" width="200" height="32" rx="5" fill="#881337"/>
    <text x="400" y="126" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#fecdd3" text-anchor="middle">2. JUDICIAL MURDER</text>

    <text x="400" y="160" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#fda4af" text-anchor="middle">Jezebel's Plot</text>
    <text x="400" y="180" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Forges royal letters to</text>
    <text x="400" y="196" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">city elders &amp; nobles.</text>

    <line x1="305" y1="210" x2="490" y2="210" stroke="#334155" stroke-width="1"/>

    <text x="400" y="235" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#fda4af" text-anchor="middle">Weaponized Law</text>
    <text x="400" y="255" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">Hires 2 false witnesses to</text>
    <text x="400" y="271" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">claim Naboth cursed king.</text>

    <rect x="300" y="320" width="200" height="70" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
    <text x="400" y="345" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#fca5a5" text-anchor="middle">Naboth is Stoned</text>
    <text x="400" y="365" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#fee2e2" text-anchor="middle">Ahab takes possession.</text>
  </g>

  <!-- Flow Arrow 2 -->
  <path d="M 520 250 L 540 250" stroke="#f43f5e" stroke-width="3" stroke-linecap="round" fill="none"/>

  <!-- Box 3: Prophetic Confrontation -->
  <g filter="url(#shadow5)">
    <rect x="545" y="95" width="220" height="310" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="555" y="105" width="200" height="32" rx="5" fill="#0369a1"/>
    <text x="655" y="126" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#e0f2fe" text-anchor="middle">3. PROPHETIC REBUKE</text>

    <text x="655" y="160" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#7dd3fc" text-anchor="middle">Elijah's Verdict</text>
    <text x="655" y="180" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">"Have you murdered and</text>
    <text x="655" y="196" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">taken possession?"</text>

    <line x1="560" y1="210" x2="745" y2="210" stroke="#334155" stroke-width="1"/>

    <text x="655" y="235" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#7dd3fc" text-anchor="middle">Royal Accountability</text>
    <text x="655" y="255" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">God holds kings liable</text>
    <text x="655" y="271" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">for abuses against the poor.</text>

    <rect x="555" y="320" width="200" height="70" rx="5" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="655" y="345" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#38bdf8" text-anchor="middle">God's Justice Stands</text>
    <text x="655" y="365" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Ahab dynasty falls.</text>
  </g>

  <!-- Bottom Banner -->
  <text x="400" y="432" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Biblical Principle: Worship of God cannot be separated from defending economic and legal justice.</text>
</svg>'''

SVG_6_SOCIAL_JUSTICE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="level1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="level2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d9488" />
      <stop offset="100%" stop-color="#0f766e" />
    </linearGradient>
    <linearGradient id="level3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#16a34a" />
      <stop offset="100%" stop-color="#15803d" />
    </linearGradient>
    <filter id="shadow6" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad6)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="22" fill="#f8fafc" text-anchor="middle">THE 3 TIERS OF CHRISTIAN SOCIAL JUSTICE</text>
  <text x="400" y="68" font-family="Segoe UI, Inter, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Translating Faith into Action: "Act Justly, Love Mercy, Walk Humbly" (Micah 6:8)</text>

  <!-- Level 1: Personal Integrity -->
  <g filter="url(#shadow6)">
    <rect x="40" y="100" width="220" height="300" rx="10" fill="url(#level1Grad)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="55" y="115" width="190" height="32" rx="5" fill="#0c4a6e"/>
    <text x="150" y="136" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#bae6fd" text-anchor="middle">TIER 1: INTEGRITY</text>

    <rect x="55" y="160" width="190" height="50" rx="5" fill="#0369a1"/>
    <text x="150" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">The Personal Guardrail</text>
    <text x="150" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e0f2fe" text-anchor="middle">Refusing to cheat or bribe</text>

    <rect x="55" y="220" width="190" height="50" rx="5" fill="#0369a1"/>
    <text x="150" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Truthfulness</text>
    <text x="150" y="258" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e0f2fe" text-anchor="middle">Rejecting rumors &amp; deceit</text>

    <rect x="55" y="280" width="190" height="50" rx="5" fill="#0369a1"/>
    <text x="150" y="300" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Equal Respect</text>
    <text x="150" y="318" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#e0f2fe" text-anchor="middle">No ethnic or wealth bias</text>

    <text x="150" y="365" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#7dd3fc" text-anchor="middle">"Clean hands and a</text>
    <text x="150" y="382" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#f0f9ff" text-anchor="middle">pure heart" (Psalm 24:4)</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 270 250 L 285 250" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" fill="none"/>

  <!-- Level 2: Advocacy & Voice -->
  <g filter="url(#shadow6)">
    <rect x="290" y="100" width="220" height="300" rx="10" fill="url(#level2Grad)" stroke="#2dd4bf" stroke-width="1.5"/>
    <rect x="305" y="115" width="190" height="32" rx="5" fill="#134e4a"/>
    <text x="400" y="136" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#99f6e4" text-anchor="middle">TIER 2: ADVOCACY</text>

    <rect x="305" y="160" width="190" height="50" rx="5" fill="#0f766e"/>
    <text x="400" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">The Prophetic Voice</text>
    <text x="400" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#ccfbf1" text-anchor="middle">Speaking for the voiceless</text>

    <rect x="305" y="220" width="190" height="50" rx="5" fill="#0f766e"/>
    <text x="400" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Constructive Challenge</text>
    <text x="400" y="258" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#ccfbf1" text-anchor="middle">Addressing school bullying</text>

    <rect x="305" y="280" width="190" height="50" rx="5" fill="#0f766e"/>
    <text x="400" y="300" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Promoting Dialogue</text>
    <text x="400" y="318" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#ccfbf1" text-anchor="middle">Engaging teachers &amp; leaders</text>

    <text x="400" y="365" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#5eead4" text-anchor="middle">"Speak up for those who</text>
    <text x="400" y="382" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#f0fdfa" text-anchor="middle">cannot speak" (Prov. 31:8)</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 520 250 L 535 250" stroke="#2dd4bf" stroke-width="3" stroke-linecap="round" fill="none"/>

  <!-- Level 3: Concrete Action & Compassion -->
  <g filter="url(#shadow6)">
    <rect x="540" y="100" width="220" height="300" rx="10" fill="url(#level3Grad)" stroke="#4ade80" stroke-width="1.5"/>
    <rect x="555" y="115" width="190" height="32" rx="5" fill="#14532d"/>
    <text x="650" y="136" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#bbf7d0" text-anchor="middle">TIER 3: REFORM</text>

    <rect x="555" y="160" width="190" height="50" rx="5" fill="#15803d"/>
    <text x="650" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Hands-on Service</text>
    <text x="650" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#dcfce7" text-anchor="middle">Charity, tutoring, food aid</text>

    <rect x="555" y="220" width="190" height="50" rx="5" fill="#15803d"/>
    <text x="650" y="240" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Community Initiatives</text>
    <text x="650" y="258" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#dcfce7" text-anchor="middle">Stationery share boxes &amp; clubs</text>

    <rect x="555" y="280" width="190" height="50" rx="5" fill="#15803d"/>
    <text x="650" y="300" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">Sustainable Impact</text>
    <text x="650" y="318" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#dcfce7" text-anchor="middle">Institutional betterment</text>

    <text x="650" y="365" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#86efac" text-anchor="middle">"Learn to do right;</text>
    <text x="650" y="382" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#f0fdf4" text-anchor="middle">seek justice" (Isaiah 1:17)</text>
  </g>

  <!-- Bottom Summary -->
  <text x="400" y="432" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Authentic loyalty to God bridges inward holiness with courageous, tangible love for neighbors.</text>
</svg>'''


# -----------------------------------------------------------------------------
# Lessons Ingestion Definition
# -----------------------------------------------------------------------------

LESSONS_DATA = [
    # Lesson 1
    {
        "unit_order": 1,
        "unit_name": "Modern Forms of Idol Worship and Religious Extremism",
        "unit_desc": "Define biblical loyalty and identify contemporary heart-level idols and religious extremism.",
        "lesson_title": "Modern Forms of Idol Worship and Religious Extremism",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b2/The_Adoration_of_the_Golden_Calf_%E2%80%93_Nicolas_Poussin.jpg",
            "title": "Visual Hook: The Golden Calf and Human Idolatry",
            "author": "Nicolas Poussin (National Gallery)",
            "caption": "The historic worship of the golden calf demonstrates the perennial human temptation to replace the living God with tangible symbols of security.",
            "licensing": "Public Domain"
        },
        "svg": {
            "title": "Vector Blueprint: The Evolution of Idolatry (Ancient vs Modern)",
            "caption": "Visual contrast showing how physical statue idolatry transitions into subtle heart-level addictions and consumerism.",
            "svg_xml": SVG_1_IDOLATRY
        },
        "video": {
            "url": "https://www.youtube.com/watch?v=k1t6_0l2a6s",
            "title": "BibleProject: The Idolatry of the Human Heart",
            "description": "An engaging theological breakdown explaining why biblical idolatry centers on elevating good created things into ultimate priorities."
        },
        "objectives": [
            "Define biblical loyalty to God and differentiate between physical and heart-level idolatry.",
            "Identify contemporary modern idols such as materialism, self-worship, clout chasing, and substance abuse.",
            "Analyze the warning signs of religious extremism and destructive cults.",
            "Apply Matthew 6:24 to everyday ethical scenarios regarding money and status."
        ],
        "card1_hook": "When people think of idol worship, they often picture ancient stone statues in dusty temples. But what if the most powerful idols today are invisible, carried in our pockets, or worshipped in our bank accounts? True loyalty to God is tested not by statues, but by where we place our ultimate trust and devotion.",
        "card2_core": "True loyalty to God means unwavering devotion, obedience, and alignment of one's thoughts, values, and actions with God's character and commands. Modern idolatry is an inward posture of the heart where created things are turned into 'ultimate things.'\n\n### Modern Subrogated Idols:\n1. **Materialism (Mammon):** The excessive love of money and possessions, believing wealth guarantees safety and significance (Matthew 6:24).\n2. **Power, Influence, and Status:** The obsessive pursuit of clout, dominance, and social media popularity.\n3. **Self-Worship (Narcissism):** Prioritizing personal convenience and pleasure above the moral commandments of God.\n4. **Addictions:** Allowing digital devices, gambling, or substances to govern one's desires and time.\n5. **Religious Extremism:** Blind allegiance to manipulative leaders who exploit followers through fear and isolation.",
        "card3_analytic": "Notice the fundamental shift in how idolatry operates. In ancient Israel, idolatry was localized and tied to physical shrines. Today, modern idolatry operates within the subconscious architecture of consumerism, digital validation, and self-glorification. Discerning an idol requires asking: 'What do I fear losing the most, and where do I run for comfort when in crisis?'",
        "card4_reflection": "Consider Jesus' words in Matthew 6:24: 'No one can serve two masters.' Money, reputation, and talent are excellent servants but terrible masters. When our loyalty is divided, spiritual compromise becomes inevitable. Recognizing our modern idols is the first step toward genuine freedom and wholehearted devotion to Yahweh.",
        "card5_scenario": {
            "title": "Ethical Dilemma: The Clout Trap",
            "context": "Joseph, a talented Christian youth musician, is offered a lucrative sponsorship by a brand promoting heavy alcohol abuse and gambling. The contract would pay his school fees and double his followers.",
            "reflection_points": [
                "Which modern idol is competing for Joseph's loyalty?",
                "How can well-meaning friends rationalize compromise under the guise of 'success'?",
                "What practical steps can Joseph take to maintain unwavering integrity before God?"
            ]
        },
        "card6_summary": "Idol worship did not disappear with ancient history; it simply adapted into inward heart-level attachments like materialism, vanity, and extremism. True loyalty to God demands exclusive, undivided commitment.",
        "mcq": {
            "question": "Which of the following best contrasts ancient idolatry with modern idolatry?",
            "options": [
                "A) Ancient idolatry was purely spiritual, while modern idolatry is purely economic.",
                "B) Ancient idolatry targeted physical statues, whereas modern idolatry targets heart-level attachments like wealth, fame, and self-worship.",
                "C) Ancient idolatry was harmless, while modern idolatry is always violent.",
                "D) Modern idolatry only affects non-religious individuals in Western nations."
            ],
            "correct_answer": "B",
            "explanation": "Ancient idolatry used physical images (Baal, Asherah), but both ancient and modern idolatry share the core sin of replacing God's sovereignty with created things and human desires."
        }
    },

    # Lesson 2
    {
        "unit_order": 2,
        "unit_name": "Discerning and Avoiding Ungodly Groups",
        "unit_desc": "Equip learners with biblical criteria and critical thinking to identify, evaluate, and avoid destructive ungodly cults.",
        "lesson_title": "Discerning and Avoiding Ungodly Groups",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Kacou_Philippe.jpg",
            "title": "Visual Hook: Testing Charismatic Claims and Religious Movements",
            "author": "Wikimedia Commons Contributor",
            "caption": "Throughout modern religious history, charismatic figures have claimed exclusive prophetic authority, demanding rigorous biblical discernment.",
            "licensing": "Creative Commons Attribution-Share Alike"
        },
        "svg": {
            "title": "Vector Blueprint: The 4-Pillar Discernment Filter",
            "caption": "A structured framework to evaluate religious groups based on doctrine, moral fruit, governance, and handling of Scripture.",
            "svg_xml": SVG_2_DISCERNMENT
        },
        "video": {
            "url": "https://www.youtube.com/watch?v=o0c_tM8jN94",
            "title": "Understanding Spiritual Discernment & False Teachers",
            "description": "A biblical exploration of Jesus' warning in Matthew 7 regarding wolves in sheep's clothing and testing spiritual fruit."
        },
        "objectives": [
            "Explain biblical principles for testing spirits and recognizing false teachers (1 John 4:1, Matthew 7:15-20).",
            "Identify the psychological and organizational marks of destructive cultic groups.",
            "Distinguish between intellectual belief and authentic living faith (James 2:19-24).",
            "Develop personal safety guidelines for digital and social media religious interactions."
        ],
        "card1_hook": "Deceptive groups never label themselves as dangerous; they disguise themselves with charismatic preaching, warm praise, and promises of miraculous wealth. Jesus warned that wolves come dressed in sheep's clothing. How can young believers cultivate the spiritual discernment needed to spot deception before it traps them?",
        "card2_core": "Ungodly groups often utilize Christian terminology and emotional manipulation ('love bombing') to recruit unsuspecting youth.\n\n### Biblical Criteria for Discernment:\n1. **Sound Doctrine (1 John 4:1-3):** Does the group confess Jesus Christ as Lord and God incarnate? Cults often diminish Christ's divinity or add modern human leaders as co-mediators.\n2. **Moral Fruit (Matthew 7:16-20):** True spiritual leaders live with humility, sexual purity, and financial honesty. Greed and coercion reveal false prophets.\n3. **Accountability (James 5:16):** Healthy churches welcome scrutiny and parent involvement. Cults enforce secrecy and forbid questioning the leader.\n4. **Scripture in Context (2 Timothy 2:15):** Deceptive groups isolate verses out of context to enforce legalistic codes or extort money.",
        "card3_analytic": "Notice how ungodly groups use isolation as a weapon. They often tell young recruits: 'Your parents and teachers are spiritually dead; keep our meetings a secret.' This psychological manipulation severs natural support networks, leaving the individual dependent entirely on the cult leader for identity and validation.",
        "card4_reflection": "In 1 John 4:1, believers are commanded not to believe every spirit, but to test them. Testing is not a lack of faith; it is an act of obedience. God gave us His revealed Word and Christian community so that we are not tossed back and forth by every cunning wind of doctrine.",
        "card5_scenario": {
            "title": "Digital Safety Guidelines for Believers",
            "context": "A student is invited to a private WhatsApp prayer group promising 'exclusive prophecies on national exams' with instructions not to tell school authorities.",
            "reflection_points": [
                "Why is secrecy in religious groups a major red flag?",
                "How does 2 Timothy 2:15 help us evaluate promises of shortcut academic success?",
                "What immediate action should a student take when encountering secretive online groups?"
            ]
        },
        "card6_summary": "Spiritual discernment is a vital safeguard against deception. Believers evaluate all teachings and groups by comparing their doctrine, character fruit, accountability, and scriptural fidelity against the Bible.",
        "mcq": {
            "question": "A religious leader claims that he has received a special vision that forbids members from speaking to their parents or doctors. According to Matthew 7:15-20 and 1 Timothy 4:1-3, how should a Christian respond?",
            "options": [
                "A) Obey the leader because questioning authority is always a sin.",
                "B) Reject the leader's teachings immediately because isolation and unbiblical prohibitions are marks of false prophets.",
                "C) Follow the rules partially while attending meetings secretly.",
                "D) Wait until the leader performs a miracle before deciding."
            ],
            "correct_answer": "B",
            "explanation": "Scripture explicitly warns against false teachers who isolate believers, destroy family relationships, and introduce doctrines contrary to God's Word."
        }
    },

    # Lesson 3
    {
        "unit_order": 3,
        "unit_name": "Elijah's Fight Against Baalism (Mount Carmel Showdown)",
        "unit_desc": "Analyze the historic spiritual crisis under Ahab and Elijah's dramatic contest on Mount Carmel to vindicate Yahweh.",
        "lesson_title": "Elijah's Fight Against Baalism (Mount Carmel Showdown)",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/1/12/Keren_HaCarmel_%28997009157440605171.jpg",
            "title": "Visual Hook: Mount Carmel Ridge (Al-Muhraqa)",
            "author": "Israel Heritage Archive",
            "caption": "The commanding heights of Mount Carmel overlooking the Jezreel Valley, the historic location where Prophet Elijah challenged the prophets of Baal.",
            "licensing": "Creative Commons Attribution 2.5"
        },
        "svg": {
            "title": "Vector Blueprint: The Contest on Mount Carmel",
            "caption": "Visual breakdown comparing the frantic, silent rituals of Baal's prophets with Elijah's covenant prayer and God's consuming fire.",
            "svg_xml": SVG_3_MOUNT_CARMEL
        },
        "video": {
            "url": "https://www.youtube.com/watch?v=b0S8nUe2_s0",
            "title": "BibleProject: The Story of Elijah and 1 Kings",
            "description": "An illustrated overview of 1 Kings 18 highlighting the dramatic covenant showdown between Yahweh and Baal on Mount Carmel."
        },
        "objectives": [
            "Examine the socio-religious impact of Ahab and Jezebel's state-sponsored Baalism in Israel.",
            "Analyze Elijah's challenge against religious syncretism and 'limping between two opinions.'",
            "Detail the sequence of events during the Mount Carmel contest (1 Kings 18:17-40).",
            "Evaluate the theological significance of the altar of 12 stones and the divine consuming fire."
        ],
        "card1_hook": "When King Ahab and Queen Jezebel promoted Baalism, Israel tried to have it both ways: worshipping Yahweh for moral protection while praying to Baal for rain and crops. Elijah stood alone on Mount Carmel and challenged an entire nation: 'How long will you waver between two opinions?'",
        "card2_core": "King Ahab married Jezebel of Tyre, introducing state-sponsored fertility cults that slaughtered Yahweh's prophets and promoted syncretism.\n\n### The Mount Carmel Contest (1 Kings 18):\n* **The Challenge:** 1 prophet of God vs. 450 prophets of Baal. The terms: 'The God who answers by fire—He is God.'\n* **Baal's Prophets:** Shouted frantically from morning till evening, danced around their altar, and slashed themselves with knives. The result: absolute silence.\n* **Elijah's Preparation:** Rebuilt the ruined altar of Yahweh using **12 stones** (representing the indivisible covenant unity of the 12 tribes). He ordered **12 jars of water** poured over the sacrifice to make fire humanly impossible.\n* **The Prayer & Response:** A concise 60-word prayer appealing to the God of Abraham, Isaac, and Israel. Fire fell instantly from heaven, consuming the sacrifice, wood, stones, soil, and trench water.",
        "card3_analytic": "Consider why Elijah used 12 stones during a time when Israel was politically fractured into the Northern and Southern kingdoms. By using 12 stones, Elijah affirmed that in God's eyes, the covenant community remains united under Yahweh's sovereign law, transcending political borders.",
        "card4_reflection": "Syncretism—the blending of Christian truth with worldly compromises—remains a major danger today. Many believers attempt to balance moral faith with unethical shortcuts. The fire of Mount Carmel demonstrates that God does not share His glory with manufactured idols.",
        "card5_scenario": {
            "title": "Historical Sequence: Mount Carmel Showdown",
            "context": "Chronological milestones of 1 Kings 18:",
            "reflection_points": [
                "1. Elijah confronts Ahab and gathers Israel at Mount Carmel.",
                "2. Baal's prophets plead frantically in vain throughout the day.",
                "3. Elijah rebuilds Yahweh's altar with 12 stones and soaks it with water.",
                "4. God answers Elijah's quiet covenant prayer with supernatural fire.",
                "5. The nation falls prostrate confessing: 'The Lord—He is God!'"
            ]
        },
        "card6_summary": "The victory on Mount Carmel vindicated Yahweh as the sole sovereign creator and exposed Baal as an impotent myth. True loyalty requires decisive, uncompromising commitment to God.",
        "mcq": {
            "question": "What was the primary theological significance of Elijah rebuilding the altar of Yahweh with twelve stones?",
            "options": [
                "A) It was required by Phoenician architecture standards.",
                "B) It symbolized the unbroken covenant unity of all twelve tribes of Israel before God.",
                "C) It was designed to hold the maximum amount of water.",
                "D) It commemorated King Ahab's military victories."
            ],
            "correct_answer": "B",
            "explanation": "Despite the political division into Northern and Southern kingdoms, the twelve stones reaffirmed that Israel remained one covenant people accountable to Yahweh."
        }
    },

    # Lesson 4
    {
        "unit_order": 4,
        "unit_name": "Elijah's Flight to Mount Horeb and Divine Restoration",
        "unit_desc": "Examine Elijah's emotional burnout after victory, and evaluate God's compassionate holistic restoration on Mount Horeb.",
        "lesson_title": "Elijah's Flight to Mount Horeb and Divine Restoration",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Mount_Sinai_Egypt.jpg",
            "title": "Visual Hook: Mount Sinai / Horeb Mountain Range",
            "author": "Wikimedia Commons Contributor",
            "caption": "The rugged granite peaks of Mount Horeb (Sinai), where Elijah sought refuge in a cave and heard the still, small voice of God.",
            "licensing": "Creative Commons Attribution-Share Alike"
        },
        "svg": {
            "title": "Vector Blueprint: God's Holistic Care in Burnout",
            "caption": "A 3-stage model illustrating physical restoration, gentle intimate revelation, and purposeful recommissioning.",
            "svg_xml": SVG_4_HOREB_RESTORATION
        },
        "video": {
            "url": "https://www.youtube.com/watch?v=7hUs4dZ4q6E",
            "title": "Elijah at Mount Horeb: The Gentle Whisper",
            "description": "An insightful reflection on 1 Kings 19 showing how God ministers to His exhausted prophet not through noise, but in a gentle whisper."
        },
        "objectives": [
            "Analyze the causes of Elijah's sudden emotional and spiritual burnout following Jezebel's death threat.",
            "Evaluate God's sequential model of care: physical nourishment, honest lament, and gentle communion.",
            "Differentiate between sensational manifestations of power and the 'still, small voice' of intimate divine guidance.",
            "Apply lessons on mental wellness, rest, and community support to modern student life."
        ],
        "card1_hook": "Immediately after the greatest spiritual triumph of his life on Mount Carmel, Elijah plummeted into deep despair. Threatened by Queen Jezebel, he fled into the wilderness, sat under a broom tree, and prayed to die. How does God treat His faithful servants when they reach the breaking point of emotional exhaustion?",
        "card2_core": "Spiritual champions are not immune to depression, fear, and fatigue. Elijah suffered from acute burnout following intense crisis.\n\n### God’s 3-Fold Holistic Restoration Plan (1 Kings 19):\n1. **Physical Nourishment:** God did not lecture or punish Elijah. He sent an angel with baked bread and cool water, letting him sleep twice. God acknowledged: *'The journey is too much for you.'*\n2. **Gentle Spiritual Revelation:** At Mount Horeb, God sent wind that tore mountains, an earthquake, and a raging fire—but God was not in the chaos. God spoke in a **gentle whisper** (*'still, small voice'*), meeting Elijah in quiet intimacy.\n3. **Recommissioning & Allies:** God shattered Elijah's feeling of total isolation ('I alone am left') by revealing **7,000 faithful Israelites** who had not bowed to Baal, and giving him a successor: Elisha.",
        "card3_analytic": "Contrast the fire of Mount Carmel with the whisper of Mount Horeb. On Carmel, God used dramatic fire for a public nation in rebellion; at Horeb, God used a gentle whisper for an exhausted, hurting prophet. God adapts His communication to meet our deepest personal needs.",
        "card4_reflection": "When students experience academic stress, burnout, or family pressure, they often feel guilty for being exhausted. Elijah's story proves that feeling overwhelmed is not a sin; it is a signal to rest, nourish our bodies, and listen for God's gentle voice in quiet prayer.",
        "card5_scenario": {
            "title": "A Student Action Plan for Overcoming Burnout",
            "context": "Practical steps modeled after God's treatment of Elijah:",
            "reflection_points": [
                "1. Prioritize physical health: ensure adequate sleep, hydration, and nutrition.",
                "2. Express honest feelings: pour out raw emotions to God in prayer without fear.",
                "3. Step away from digital noise: find quiet moments of meditation and reflection.",
                "4. Connect with your community: confide in trusted mentors, parents, and friends."
            ]
        },
        "card6_summary": "God restores His exhausted servants not with condemnations, but with compassionate physical rest, intimate whispers of comfort, and renewed purpose within a supportive community.",
        "mcq": {
            "question": "What does God's encounter with Elijah on Mount Horeb teach about divine guidance during seasons of emotional exhaustion?",
            "options": [
                "A) God only reveals His presence through violent natural catastrophes.",
                "B) True prophets never need sleep or food when doing God's work.",
                "C) God's presence and direction are often found in quiet, intimate communion rather than noisy, sensational displays.",
                "D) Experiencing fear permanently disqualifies a believer from ministry."
            ],
            "correct_answer": "C",
            "explanation": "The progression from wind, earthquake, and fire to a gentle whisper showed Elijah that God ministers to wounded souls in quiet, intimate fellowship."
        }
    },

    # Lesson 5
    {
        "unit_order": 5,
        "unit_name": "Elijah's Defense of Social Justice (Naboth's Vineyard)",
        "unit_desc": "Analyze the theft of Naboth's vineyard and evaluate Elijah's fearless defense of covenant land rights and legal justice.",
        "lesson_title": "Elijah's Defense of Social Justice (Naboth's Vineyard)",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Jezreel_Valley_0674_%28520285868%29.jpg",
            "title": "Visual Hook: The Fertile Plain of Jezreel",
            "author": "Wikimedia Commons Contributor",
            "caption": "The lush landscape of the Jezreel Valley, where Naboth tended his ancestral vineyard near King Ahab's summer palace.",
            "licensing": "Creative Commons Attribution 2.0"
        },
        "svg": {
            "title": "Vector Blueprint: Naboth's Vineyard & Prophetic Injustice",
            "caption": "Flowchart illustrating Ahab's greed, Jezebel's weaponization of the legal system, and Elijah's fearless prophetic judgment.",
            "svg_xml": SVG_5_NABOTH_VINEYARD
        },
        "video": {
            "url": "https://www.youtube.com/watch?v=kYJzEwX_L6g",
            "title": "BibleProject: Naboth's Vineyard and Royal Injustice",
            "description": "A compelling overview of 1 Kings 21 explaining why biblical loyalty requires standing up against economic exploitation and state corruption."
        },
        "objectives": [
            "Explain the biblical laws governing ancestral land ownership in Israel (Leviticus 25:23, Numbers 36:7).",
            "Examine how Queen Jezebel manipulated the legal and judicial system to execute Naboth.",
            "Analyze Elijah's bold prophetic confrontation of King Ahab in the stolen vineyard.",
            "Synthesize the biblical principle that worship of God cannot be separated from social justice."
        ],
        "card1_hook": "Can a person be genuinely faithful to God while abusing political power and mistreating the vulnerable? When King Ahab coveted Naboth's family vineyard, Queen Jezebel framed Naboth using false witnesses and had him stoned to death. But God dispatched Prophet Elijah to deliver a terrifying verdict right inside the stolen field.",
        "card2_core": "Under covenant law (Leviticus 25:23), land belonged ultimately to God and was leased to families as an inalienable inheritance. Naboth's refusal to sell was an act of obedience to God.\n\n### Jezebel's Abuse of Power (1 Kings 21):\n1. **Religious Mask:** Jezebel declared a national fast, placing Naboth in a seat of prominence.\n2. **False Witnesses:** Hired two corrupt men to accuse Naboth of blaspheming God and the king.\n3. **Judicial Murder:** Naboth was stoned to death outside the city, and Ahab seized the vineyard.\n\n### Elijah's Fearless Confrontation:\nGod sent Elijah directly to meet Ahab in the stolen vineyard with a devastating indictment: *'Have you murdered and also taken possession?'* Elijah declared that God would hold the royal dynasty fully accountable for innocent blood.",
        "card3_analytic": "Notice the corruption of institutions in this narrative. Jezebel did not assassinate Naboth in secret; she used city elders, royal seals, and court trials to make murder appear legal. Elijah's prophecy established that divine justice stands above corrupt human legal systems.",
        "card4_reflection": "True loyalty to God requires defending human rights and standing with the oppressed. Whenever the powerful exploit the weak—whether in government, business, or schools—God hears the cry of the victim and demands moral accountability from those who remain silent.",
        "card5_scenario": {
            "title": "School-Life Case Study: Defending the Vulnerable",
            "context": "An influential student spreads fabricated rumors on social media to have a quiet classmate stripped of their scholarship.",
            "reflection_points": [
                "How does this scenario mirror Jezebel's conspiracy against Naboth?",
                "What moral responsibility falls upon peers who know the rumors are false?",
                "How can students embody Elijah's prophetic courage to restore fairness?"
            ]
        },
        "card6_summary": "Biblical faith is inseparable from social and economic justice. God holds all leaders accountable for how they treat the vulnerable, and commands His followers to speak truth to power.",
        "mcq": {
            "question": "Why did Naboth refuse to sell his vineyard to King Ahab?",
            "options": [
                "A) He wanted a much higher price from another buyer.",
                "B) Under Israelite covenant law, ancestral land belonged to God and could not be permanently transferred.",
                "C) He disliked King Ahab's choice of vegetables.",
                "D) Queen Jezebel had already offered to buy it for more money."
            ],
            "correct_answer": "B",
            "explanation": "According to Leviticus 25:23 and Numbers 36:7, land was God's covenant trust and an inalienable family inheritance that could not be permanently sold."
        }
    },

    # Lesson 6
    {
        "unit_order": 6,
        "unit_name": "Promoting Social Justice in Modern Society",
        "unit_desc": "Synthesize Elijah's prophetic heritage into practical pathways for promoting justice and equality in schools and communities.",
        "lesson_title": "Promoting Social Justice in Modern Society",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/5/56/Volunteerism_and_Community_Service_in_Ukraine_Photo_Contest_Volunteerism_and_Community_Service_in_Ukraine_Photo_Contest%2C_Sept-Nov%2C_2013_%2810959030576%29.jpg",
            "title": "Visual Hook: Youth Engaging in Community Care and Social Service",
            "author": "Wikimedia Commons Contributor",
            "caption": "Young people actively working together to meet community needs, embodying the biblical call to love and tangible service.",
            "licensing": "Creative Commons Attribution-Share Alike"
        },
        "svg": {
            "title": "Vector Blueprint: The 3 Tiers of Christian Social Justice",
            "caption": "Actionable pathway linking personal integrity, constructive advocacy, and community reform (Micah 6:8).",
            "svg_xml": SVG_6_SOCIAL_JUSTICE
        },
        "video": {
            "url": "https://www.youtube.com/watch?v=A14THPoc4-4",
            "title": "BibleProject: Justice (Mishpat & Tzedakah)",
            "description": "A profound exploration of biblical justice, showing how God calls His people to actively advocate for the poor, vulnerable, and oppressed."
        },
        "objectives": [
            "Synthesize the biblical mandate for social justice from the Old Testament prophets (Micah 6:8, Isaiah 1:17).",
            "Identify modern forms of injustice in educational institutions, workplaces, and local communities.",
            "Design concrete initiatives that promote fairness, integrity, and peer support.",
            "Demonstrate how Christian loyalty to God transforms personal morality into community reform."
        ],
        "card1_hook": "Prophet Micah asked: 'What does the Lord require of you? To act justly, to love mercy, and to walk humbly with your God.' True loyalty to God cannot be confined to church buildings on the weekend; it must overflow into the streets, schools, and communities as active love and systemic fairness.",
        "card2_core": "Biblical social justice combines *Tzedakah* (righteous ethical character) with *Mishpat* (active defense of rights and legal justice).\n\n### The 3 Tiers of Promoting Social Justice:\n1. **Personal Integrity (The Guardrail):** Refusing to participate in bribery, academic dishonesty, tribal bias, or cyberbullying.\n2. **Advocacy (The Voice):** Speaking up for peers who are scapegoated, marginalized, or living with disabilities.\n3. **Community Reform (The Hands):** Organizing practical student aid programs—such as stationery sharing boxes, peer tutoring, anti-bullying awareness, and charity drives.",
        "card3_analytic": "Notice that biblical justice is proactive, not merely reactive. It is not enough to simply avoid doing harm; believers are called by Isaiah 1:17 to actively 'learn to do good, seek justice, and defend the oppressed.'",
        "card4_reflection": "When we see classmates struggling in silence, our devotion to God calls us to step into the gap. Every act of kindness, every stand against dishonesty, and every effort to share resources reflects the compassionate heart of Christ to the world.",
        "card5_scenario": {
            "title": "Action Project: Designing a School Justice Initiative",
            "context": "Collaborative pathways for student impact:",
            "reflection_points": [
                "1. Identify an unaddressed need (e.g., students lacking exam materials, cafeteria food waste).",
                "2. Form a student coalition guided by teachers and school values.",
                "3. Draft a respectful proposal to school leadership offering solutions.",
                "4. Implement sustainable peer support networks that foster long-term dignity."
            ]
        },
        "card6_summary": "Social justice is the practical proof of authentic worship. By combining personal integrity with compassionate community advocacy, believers reflect God's righteous character in society.",
        "mcq": {
            "question": "Which of the following actions best illustrates a Christian exercising biblical social justice according to Micah 6:8?",
            "options": [
                "A) Donating money to charity while secretly mistreating domestic workers at home.",
                "B) Remaining completely silent during unfair school practices to avoid controversy.",
                "C) Maintaining personal honesty while actively organizing peer tutoring for struggling, underprivileged classmates.",
                "D) Criticizing government policies online without ever helping anyone in the local neighborhood."
            ],
            "correct_answer": "C",
            "explanation": "Biblical justice requires both personal moral integrity and active, compassionate engagement to assist and uplift those in need."
        }
    }
]


@transaction.atomic
def ingest_topic_1_7():
    print("================================================================================")
    print("Starting Ingestion: CBC Grade 10 CRE — Topic 1.7: Loyalty to God (Elijah)")
    print("================================================================================")

    # 1. Fetch Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' not found in database!")

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC!")

    subject = Subject.objects.filter(grade=grade, name__icontains="CRE").first()
    if not subject:
        raise ValueError("Subject 'CRE' not found under Grade 10!")

    print(f"Hierarchy Validated: {curriculum.name} -> {grade.name} (Level {grade.level}) -> {subject.name} (ID: {subject.id})")

    # 2. Get or Create Topic 1.7 (Order 7)
    topic_name = "Topic 1.7: Loyalty to God (Elijah)"
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=7,
        defaults={
            "name": topic_name,
            "description": "Examines unwavering loyalty to God versus idolatry through the life and ministry of Prophet Elijah."
        }
    )
    if not t_created and topic.name != topic_name:
        topic.name = topic_name
        topic.save()
    print(f"Topic configured: ID={topic.id}, Order={topic.order}, Name='{topic.name}'")

    # Clean existing lessons/units under Topic 1.7 to ensure clean idempotent ingestion
    existing_lessons = Lesson.objects.filter(topic=topic)
    for l in existing_lessons:
        l.blocks.all().delete()
        l.assets.all().delete()
    existing_lessons.delete()
    topic.learning_units.all().delete()
    print("Cleaned previous Topic 1.7 records for clean idempotent build.")

    total_units = 0
    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    for idx, ldata in enumerate(LESSONS_DATA, start=1):
        u_order = ldata["unit_order"]
        u_name = f"1.7.{u_order} {ldata['unit_name']}"
        unit = LearningUnit.objects.create(
            topic=topic,
            name=u_name,
            description=ldata["unit_desc"],
            order=u_order
        )
        total_units += 1

        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=ldata["lesson_title"],
            status="published",
            version=1,
            published_at=timezone.now(),
            immutable_metadata={
                "curriculum": "CBC",
                "grade": "Grade 10",
                "subject": "CRE",
                "topic_order": 7,
                "unit_order": u_order
            }
        )
        total_lessons += 1
        print(f"\n--- Ingesting Unit {u_order} / Lesson {idx}: '{lesson.title}' ---")

        # ---------------------------------------------------------------------
        # Card 1: Visual Hook + Objectives + Introductory Context
        # ---------------------------------------------------------------------
        b_img = LessonBlock.objects.create(
            lesson=lesson,
            page_number=1,
            component_order=1,
            block_type="suggested_image",
            component_type="suggested_image",
            title=ldata["image"]["title"],
            content={
                "url": ldata["image"]["url"],
                "resolved_image_url": ldata["image"]["url"],
                "title": ldata["image"]["title"],
                "author": ldata["image"]["author"],
                "caption": ldata["image"]["caption"],
                "licensing": ldata["image"]["licensing"],
                "source": "Wikimedia Commons",
                "verified": True
            }
        )
        asset_img = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            source_type="external",
            storage_type="url",
            status="attached",
            title=ldata["image"]["title"],
            description=ldata["image"]["caption"],
            url=ldata["image"]["url"],
            metadata={"source": "Wikimedia Commons", "author": ldata["image"]["author"]}
        )
        b_img.assets.add(asset_img)
        total_blocks += 1
        total_assets += 1

        b_obj = LessonBlock.objects.create(
            lesson=lesson,
            page_number=1,
            component_order=2,
            block_type="learning_goal",
            component_type="learning_goal",
            title=f"Lesson Objectives: {ldata['lesson_title']}",
            content={
                "goals": ldata["objectives"],
                "markdown": "### By the end of this lesson, you should be able to:\n" + "\n".join(f"* {g}" for g in ldata["objectives"])
            }
        )
        total_blocks += 1

        b_hook = LessonBlock.objects.create(
            lesson=lesson,
            page_number=1,
            component_order=3,
            block_type="concept_explanation",
            component_type="concept_explanation",
            title="Introduction: The Heart of the Matter",
            content={"markdown": ldata["card1_hook"]}
        )
        total_blocks += 1

        # ---------------------------------------------------------------------
        # Card 2: Core Concept Explanation & Biblical Foundations
        # ---------------------------------------------------------------------
        b_core = LessonBlock.objects.create(
            lesson=lesson,
            page_number=2,
            component_order=1,
            block_type="concept_explanation",
            component_type="concept_explanation",
            title=f"Core Content: {ldata['lesson_title']}",
            content={"markdown": ldata["card2_core"]}
        )
        total_blocks += 1

        # ---------------------------------------------------------------------
        # Card 3: Vector Blueprint SVG Diagram & Analytic Breakdown
        # ---------------------------------------------------------------------
        b_diag = LessonBlock.objects.create(
            lesson=lesson,
            page_number=3,
            component_order=1,
            block_type="suggested_diagram",
            component_type="suggested_diagram",
            title=ldata["svg"]["title"],
            content={
                "title": ldata["svg"]["title"],
                "caption": ldata["svg"]["caption"],
                "svg": ldata["svg"]["svg_xml"],
                "svg_xml": ldata["svg"]["svg_xml"],
                "svg_content": ldata["svg"]["svg_xml"]
            }
        )
        asset_diag = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="embed",
            status="attached",
            title=ldata["svg"]["title"],
            description=ldata["svg"]["caption"],
            metadata={"svg_xml": ldata["svg"]["svg_xml"]}
        )
        b_diag.assets.add(asset_diag)
        total_blocks += 1
        total_assets += 1

        b_analytic = LessonBlock.objects.create(
            lesson=lesson,
            page_number=3,
            component_order=2,
            block_type="concept_explanation",
            component_type="concept_explanation",
            title="Analytic Insights & Theological Significance",
            content={"markdown": ldata["card3_analytic"]}
        )
        total_blocks += 1

        # ---------------------------------------------------------------------
        # Card 4: Curated Educational Video & Practical Reflection
        # ---------------------------------------------------------------------
        v_url = ldata["video"]["url"]
        v_id = v_url.split("v=")[-1]
        b_vid = LessonBlock.objects.create(
            lesson=lesson,
            page_number=4,
            component_order=1,
            block_type="suggested_video",
            component_type="suggested_video",
            title=ldata["video"]["title"],
            content={
                "url": v_url,
                "youtube_url": v_url,
                "title": ldata["video"]["title"],
                "description": ldata["video"]["description"],
                "resolved_video_id": v_id
            }
        )
        asset_vid = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="youtube",
            source_type="external",
            storage_type="url",
            status="attached",
            title=ldata["video"]["title"],
            description=ldata["video"]["description"],
            url=v_url,
            metadata={"youtube_id": v_id}
        )
        b_vid.assets.add(asset_vid)
        total_blocks += 1
        total_assets += 1

        b_refl = LessonBlock.objects.create(
            lesson=lesson,
            page_number=4,
            component_order=2,
            block_type="concept_explanation",
            component_type="concept_explanation",
            title="Spiritual Reflection & Biblical Context",
            content={"markdown": ldata["card4_reflection"]}
        )
        total_blocks += 1

        # ---------------------------------------------------------------------
        # Card 5: Ethical Application & Step Process
        # ---------------------------------------------------------------------
        sc = ldata["card5_scenario"]
        sc_markdown = f"### {sc['title']}\n\n**Context:** {sc['context']}\n\n**Key Questions for Reflection & Action:**\n" + "\n".join(f"* {pt}" for pt in sc["reflection_points"])
        b_app = LessonBlock.objects.create(
            lesson=lesson,
            page_number=5,
            component_order=1,
            block_type="step_process",
            component_type="step_process",
            title=sc["title"],
            content={
                "title": sc["title"],
                "markdown": sc_markdown,
                "steps": sc["reflection_points"]
            }
        )
        total_blocks += 1

        # ---------------------------------------------------------------------
        # Card 6: Key Takeaway Summary & Knowledge Check MCQ
        # ---------------------------------------------------------------------
        b_sum = LessonBlock.objects.create(
            lesson=lesson,
            page_number=6,
            component_order=1,
            block_type="key_takeaway",
            component_type="key_takeaway",
            title=f"Summary Takeaways: {ldata['lesson_title']}",
            content={"markdown": ldata["card6_summary"]}
        )
        total_blocks += 1

        mcq_data = ldata["mcq"]
        b_mcq = LessonBlock.objects.create(
            lesson=lesson,
            page_number=6,
            component_order=2,
            block_type="knowledge_check",
            component_type="knowledge_check",
            title="Check Your Understanding",
            content={
                "question": mcq_data["question"],
                "options": mcq_data["options"],
                "answer": mcq_data["correct_answer"],
                "correct_answer": mcq_data["correct_answer"],
                "explanation": mcq_data["explanation"]
            }
        )
        total_blocks += 1

        print(f"  -> Ingested 6 pages, {lesson.blocks.count()} blocks, {lesson.assets.count()} assets.")

    print("\n================================================================================")
    print("INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Learning Units Ingested: {total_units}")
    print(f"Total Lessons Ingested:        {total_lessons}")
    print(f"Total Blocks Ingested:         {total_blocks}")
    print(f"Total Assets Ingested:         {total_assets}")
    print("================================================================================")

if __name__ == "__main__":
    ingest_topic_1_7()
