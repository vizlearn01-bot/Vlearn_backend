"""
VLearn CBC Grade 10 CRE — Topic 2.1: The New Testament Books
Comprehensive Ingestion & Enrichment Script

Ingests:
  - Topic: Sub-Strand 2.1: The New Testament Books (Order: 11) under Grade 10 CRE (Subject ID: 46)
  - 4 Discrete Learning Units:
      1. Listing the New Testament Books & Canonical Order
      2. Categorizing the New Testament Books into Five Genres
      3. The Bible as a Divine Library and Its Use in Contemporary Society
      4. Desiring Daily Bible Reading and Structured Journaling
  - 4 Published Lessons (status='published', version=1)
  - 6 Progressive Cards per Lesson with rich components:
      * Card 1: Verified Wikimedia Hook + Learning Goals + Context Hook (LessonAsset linked)
      * Card 2: Core Concept Explanation + Detailed Scriptural / Theological Breakdown
      * Card 3: Custom Responsive Vector SVG Diagram (viewBox 0 0 800 450, #0f172a theme) + Analytic Callout (LessonAsset linked)
      * Card 4: Curated Educational YouTube Video + Spiritual Reflection & Biblical Context (LessonAsset linked)
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
# SVGs Data (Sanitized, viewBox="0 0 800 450", #0f172a dark theme, responsive)
# -----------------------------------------------------------------------------

SVG_1_CANONICAL_ORDER = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="gospelsGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#065f46" />
    </linearGradient>
    <linearGradient id="historyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ea580c" />
      <stop offset="100%" stop-color="#9a3412" />
    </linearGradient>
    <linearGradient id="paulGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1e40af" />
    </linearGradient>
    <linearGradient id="genGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#9333ea" />
      <stop offset="100%" stop-color="#6b21a8" />
    </linearGradient>
    <linearGradient id="revGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#e11d48" />
      <stop offset="100%" stop-color="#9f1239" />
    </linearGradient>
    <filter id="shadow1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad1)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="20" fill="#f8fafc" text-anchor="middle">CANONICAL ARCHITECTURE OF THE 27 NEW TESTAMENT BOOKS</text>
  <text x="400" y="66" font-family="Segoe UI, Inter, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">A Theologically and Historically Structured Progression from Christ's Incarnation to Cosmic Consummation</text>

  <!-- Shelf 1: Gospels & History -->
  <g filter="url(#shadow1)">
    <!-- Gospels Container -->
    <rect x="35" y="85" width="340" height="150" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="45" y="95" width="320" height="28" rx="4" fill="url(#gospelsGrad)"/>
    <text x="205" y="114" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">1. THE 4 GOSPELS (Eyewitness Accounts)</text>
    
    <!-- 4 Gospel Books -->
    <rect x="45" y="132" width="75" height="90" rx="4" fill="#047857" stroke="#34d399" stroke-width="1"/>
    <text x="82" y="172" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">MATTHEW</text>
    <text x="82" y="190" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#a7f3d0" text-anchor="middle">Messiah King</text>

    <rect x="127" y="132" width="75" height="90" rx="4" fill="#047857" stroke="#34d399" stroke-width="1"/>
    <text x="164" y="172" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">MARK</text>
    <text x="164" y="190" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#a7f3d0" text-anchor="middle">Suffering Servant</text>

    <rect x="209" y="132" width="75" height="90" rx="4" fill="#047857" stroke="#34d399" stroke-width="1"/>
    <text x="246" y="172" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">LUKE</text>
    <text x="246" y="190" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#a7f3d0" text-anchor="middle">Son of Man</text>

    <rect x="290" y="132" width="75" height="90" rx="4" fill="#047857" stroke="#34d399" stroke-width="1"/>
    <text x="327" y="172" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">JOHN</text>
    <text x="327" y="190" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#a7f3d0" text-anchor="middle">Son of God</text>
  </g>

  <!-- Church History Container -->
  <g filter="url(#shadow1)">
    <rect x="390" y="85" width="375" height="150" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <rect x="400" y="95" width="355" height="28" rx="4" fill="url(#historyGrad)"/>
    <text x="577" y="114" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">2. CHURCH HISTORY (The Acts of the Apostles)</text>
    
    <rect x="400" y="132" width="355" height="90" rx="4" fill="#7c2d12" stroke="#fb923c" stroke-width="1"/>
    <text x="577" y="162" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#ffffff" text-anchor="middle">THE ACTS OF THE APOSTLES (1 Book)</text>
    <text x="577" y="182" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#fdba74" text-anchor="middle">Sequel to Luke: The Holy Spirit Empowers the Church</text>
    <text x="577" y="200" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#fed7aa" text-anchor="middle">Jerusalem -> Judea &amp; Samaria -> Ends of the Earth (Rome)</text>
  </g>

  <!-- Shelf 2: Pauline Epistles, General Epistles, Apocalypse -->
  <g filter="url(#shadow1)">
    <!-- Pauline Epistles -->
    <rect x="35" y="248" width="370" height="155" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="45" y="258" width="350" height="26" rx="4" fill="url(#paulGrad)"/>
    <text x="220" y="275" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">3. PAULINE EPISTLES (13 Books)</text>
    
    <rect x="45" y="290" width="350" height="102" rx="4" fill="#172554" stroke="#60a5fa" stroke-width="1"/>
    <text x="220" y="310" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#93c5fd" text-anchor="middle">Church Epistles (9 Books) &amp; Pastoral/Personal (4 Books)</text>
    <text x="220" y="332" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">Romans, 1 &amp; 2 Cor., Gal., Eph., Phil., Col., 1 &amp; 2 Thess.</text>
    <text x="220" y="352" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">1 &amp; 2 Timothy, Titus, Philemon</text>
    <text x="220" y="374" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#bfdbfe" text-anchor="middle">Theological foundations, pastoral order, and ethical conduct</text>
  </g>

  <g filter="url(#shadow1)">
    <!-- General Epistles -->
    <rect x="420" y="248" width="220" height="155" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="430" y="258" width="200" height="26" rx="4" fill="url(#genGrad)"/>
    <text x="530" y="275" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">4. GENERAL EPISTLES (8)</text>
    
    <rect x="430" y="290" width="200" height="102" rx="4" fill="#3b0764" stroke="#c084fc" stroke-width="1"/>
    <text x="530" y="310" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#d8b4fe" text-anchor="middle">Catholic / Universal Letters</text>
    <text x="530" y="332" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#f3e8ff" text-anchor="middle">Hebrews, James,</text>
    <text x="530" y="348" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#f3e8ff" text-anchor="middle">1 &amp; 2 Peter, 1, 2, 3 John, Jude</text>
    <text x="530" y="374" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e9d5ff" text-anchor="middle">Perseverance in trials &amp; holy living</text>
  </g>

  <g filter="url(#shadow1)">
    <!-- Prophecy / Apocalypse -->
    <rect x="655" y="248" width="110" height="155" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect x="663" y="258" width="94" height="26" rx="4" fill="url(#revGrad)"/>
    <text x="710" y="275" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#ffffff" text-anchor="middle">5. PROPHECY</text>
    
    <rect x="663" y="290" width="94" height="102" rx="4" fill="#4c0519" stroke="#fb7185" stroke-width="1"/>
    <text x="710" y="325" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#fda4af" text-anchor="middle">REVELATION</text>
    <text x="710" y="345" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#ffe4e6" text-anchor="middle">(Apocalypse)</text>
    <text x="710" y="372" font-family="Segoe UI, Inter, sans-serif" font-size="8" fill="#fecdd3" text-anchor="middle">Cosmic Victory</text>
  </g>

  <!-- Footer Banner -->
  <text x="400" y="426" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Total: 27 Canonical Books | Sealed in Christ's New Covenant (2 Timothy 3:16-17)</text>
</svg>'''

SVG_2_GENRE_TAXONOMY = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad2)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="20" fill="#f8fafc" text-anchor="middle">THE 5 DISTINCT LITERARY GENRES OF THE NEW TESTAMENT</text>
  <text x="400" y="66" font-family="Segoe UI, Inter, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Navigating the Canonical Library by Genre, Style, Target Audience, and Theological Role</text>

  <!-- 5 Genre Columns -->
  <!-- Column 1: Gospels -->
  <g filter="url(#shadow2)">
    <rect x="25" y="85" width="140" height="325" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="33" y="93" width="124" height="35" rx="5" fill="#047857"/>
    <text x="95" y="115" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">GOSPELS</text>
    <text x="95" y="130" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#a7f3d0" text-anchor="middle">4 Books</text>

    <text x="95" y="155" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#34d399" text-anchor="middle">Literary Type</text>
    <text x="95" y="172" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Ancient Biography /</text>
    <text x="95" y="186" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Eyewitness Memoir</text>

    <line x1="35" y1="198" x2="155" y2="198" stroke="#334155" stroke-width="1"/>

    <text x="95" y="218" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#34d399" text-anchor="middle">Key Authors</text>
    <text x="95" y="235" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Matthew, Mark,</text>
    <text x="95" y="249" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Luke, John</text>

    <line x1="35" y1="261" x2="155" y2="261" stroke="#334155" stroke-width="1"/>

    <text x="95" y="281" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#34d399" text-anchor="middle">Primary Purpose</text>
    <text x="95" y="298" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Proclaim the life,</text>
    <text x="95" y="312" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">cross, resurrection,</text>
    <text x="95" y="326" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&amp; kingdom of Jesus.</text>

    <rect x="33" y="348" width="124" height="50" rx="5" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="95" y="368" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#6ee7b7" text-anchor="middle">Hermeneutic Rule</text>
    <text x="95" y="386" font-family="Segoe UI, Inter, sans-serif" font-size="8" fill="#94a3b8" text-anchor="middle">Read in Gospel context</text>
  </g>

  <!-- Column 2: History -->
  <g filter="url(#shadow2)">
    <rect x="175" y="85" width="140" height="325" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="2"/>
    <rect x="183" y="93" width="124" height="35" rx="5" fill="#c2410c"/>
    <text x="245" y="115" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">HISTORY</text>
    <text x="245" y="130" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#fed7aa" text-anchor="middle">1 Book (Acts)</text>

    <text x="245" y="155" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#fb923c" text-anchor="middle">Literary Type</text>
    <text x="245" y="172" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Historical Narrative</text>
    <text x="245" y="186" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">&amp; Theological Sequel</text>

    <line x1="185" y1="198" x2="305" y2="198" stroke="#334155" stroke-width="1"/>

    <text x="245" y="218" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#fb923c" text-anchor="middle">Key Author</text>
    <text x="245" y="235" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Luke the Physician</text>
    <text x="245" y="249" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">&amp; Missionary</text>

    <line x1="185" y1="261" x2="305" y2="261" stroke="#334155" stroke-width="1"/>

    <text x="245" y="281" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#fb923c" text-anchor="middle">Primary Purpose</text>
    <text x="245" y="298" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Record Holy Spirit's</text>
    <text x="245" y="312" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">work from Pentecost</text>
    <text x="245" y="326" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">to the Roman capital.</text>

    <rect x="183" y="348" width="124" height="50" rx="5" fill="#0f172a" stroke="#c2410c" stroke-width="1"/>
    <text x="245" y="368" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#fdba74" text-anchor="middle">Hermeneutic Rule</text>
    <text x="245" y="386" font-family="Segoe UI, Inter, sans-serif" font-size="8" fill="#94a3b8" text-anchor="middle">Descriptive vs Prescriptive</text>
  </g>

  <!-- Column 3: Pauline Epistles -->
  <g filter="url(#shadow2)">
    <rect x="325" y="85" width="150" height="325" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect x="333" y="93" width="134" height="35" rx="5" fill="#1d4ed8"/>
    <text x="400" y="115" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">PAULINE EPISTLES</text>
    <text x="400" y="130" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#bfdbfe" text-anchor="middle">13 Books</text>

    <text x="400" y="155" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#60a5fa" text-anchor="middle">Literary Type</text>
    <text x="400" y="172" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Occasional Epistles</text>
    <text x="400" y="186" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">(Congregational/Pastoral)</text>

    <line x1="335" y1="198" x2="465" y2="198" stroke="#334155" stroke-width="1"/>

    <text x="400" y="218" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#60a5fa" text-anchor="middle">Key Author</text>
    <text x="400" y="235" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Apostle Paul</text>
    <text x="400" y="249" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">(with co-senders)</text>

    <line x1="335" y1="261" x2="465" y2="261" stroke="#334155" stroke-width="1"/>

    <text x="400" y="281" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#60a5fa" text-anchor="middle">Primary Purpose</text>
    <text x="400" y="298" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Clarify doctrine, solve</text>
    <text x="400" y="312" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">church conflicts, &amp;</text>
    <text x="400" y="326" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">guide pastoral leaders.</text>

    <rect x="333" y="348" width="134" height="50" rx="5" fill="#0f172a" stroke="#1d4ed8" stroke-width="1"/>
    <text x="400" y="368" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#93c5fd" text-anchor="middle">Hermeneutic Rule</text>
    <text x="400" y="386" font-family="Segoe UI, Inter, sans-serif" font-size="8" fill="#94a3b8" text-anchor="middle">Understand historical context</text>
  </g>

  <!-- Column 4: General Epistles -->
  <g filter="url(#shadow2)">
    <rect x="485" y="85" width="145" height="325" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <rect x="493" y="93" width="129" height="35" rx="5" fill="#7e22ce"/>
    <text x="557" y="115" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">GENERAL EPISTLES</text>
    <text x="557" y="130" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e9d5ff" text-anchor="middle">8 Books</text>

    <text x="557" y="155" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#c084fc" text-anchor="middle">Literary Type</text>
    <text x="557" y="172" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Circular Apostolic</text>
    <text x="557" y="186" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Letters (Catholic)</text>

    <line x1="495" y1="198" x2="615" y2="198" stroke="#334155" stroke-width="1"/>

    <text x="557" y="218" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#c084fc" text-anchor="middle">Key Authors</text>
    <text x="557" y="235" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Hebrews author, James,</text>
    <text x="557" y="249" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Peter, John, Jude</text>

    <line x1="495" y1="261" x2="615" y2="261" stroke="#334155" stroke-width="1"/>

    <text x="557" y="281" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#c084fc" text-anchor="middle">Primary Purpose</text>
    <text x="557" y="298" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Encourage scattered</text>
    <text x="557" y="312" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Christians facing trials</text>
    <text x="557" y="326" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&amp; false teachers.</text>

    <rect x="493" y="348" width="129" height="50" rx="5" fill="#0f172a" stroke="#7e22ce" stroke-width="1"/>
    <text x="557" y="368" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#d8b4fe" text-anchor="middle">Hermeneutic Rule</text>
    <text x="557" y="386" font-family="Segoe UI, Inter, sans-serif" font-size="8" fill="#94a3b8" text-anchor="middle">Apply universal ethical truths</text>
  </g>

  <!-- Column 5: Prophecy / Apocalypse -->
  <g filter="url(#shadow2)">
    <rect x="640" y="85" width="135" height="325" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect x="648" y="93" width="119" height="35" rx="5" fill="#be123c"/>
    <text x="707" y="115" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">PROPHECY</text>
    <text x="707" y="130" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#fecdd3" text-anchor="middle">1 Book (Revelation)</text>

    <text x="707" y="155" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#fb7185" text-anchor="middle">Literary Type</text>
    <text x="707" y="172" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Apocalypse &amp; Prophecy</text>
    <text x="707" y="186" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">(Symbolic Visions)</text>

    <line x1="650" y1="198" x2="765" y2="198" stroke="#334155" stroke-width="1"/>

    <text x="707" y="218" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#fb7185" text-anchor="middle">Key Author</text>
    <text x="707" y="235" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Apostle John</text>
    <text x="707" y="249" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">(Exiled on Patmos)</text>

    <line x1="650" y1="261" x2="765" y2="261" stroke="#334155" stroke-width="1"/>

    <text x="707" y="281" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="10" fill="#fb7185" text-anchor="middle">Primary Purpose</text>
    <text x="707" y="298" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Reveal Jesus' cosmic</text>
    <text x="707" y="312" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">victory, end of evil, &amp;</text>
    <text x="707" y="326" font-family="Segoe UI, Inter, sans-serif" font-size="8.5" fill="#cbd5e1" text-anchor="middle">New Creation.</text>

    <rect x="648" y="348" width="119" height="50" rx="5" fill="#0f172a" stroke="#be123c" stroke-width="1"/>
    <text x="707" y="368" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#fda4af" text-anchor="middle">Hermeneutic Rule</text>
    <text x="707" y="386" font-family="Segoe UI, Inter, sans-serif" font-size="8" fill="#94a3b8" text-anchor="middle">Interpret symbols biblically</text>
  </g>

  <!-- Bottom Footer -->
  <text x="400" y="426" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Recognizing literary genres prevents interpretive errors and unlocks deeper biblical understanding.</text>
</svg>'''

SVG_3_BIBLE_LIBRARY = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="hubGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad3)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="20" fill="#f8fafc" text-anchor="middle">THE BIBLE AS A DIVINE LIBRARY (TA BIBLIA) &amp; ITS SOCIETAL ROLES</text>
  <text x="400" y="66" font-family="Segoe UI, Inter, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">66 Books, 40+ Authors, 1,500 Years, 3 Continents — One Redemptive Masterpiece</text>

  <!-- Central Hub: Divine Library -->
  <g filter="url(#shadow3)">
    <circle cx="400" cy="225" r="75" fill="url(#hubGrad)" stroke="#fef3c7" stroke-width="2.5"/>
    <text x="400" y="210" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="15" fill="#ffffff" text-anchor="middle">THE BIBLE</text>
    <text x="400" y="228" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="13" fill="#fef08a" text-anchor="middle">"TA BIBLIA"</text>
    <text x="400" y="246" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">66 Books (39 OT + 27 NT)</text>
    <text x="400" y="260" font-family="Segoe UI, Inter, sans-serif" font-size="9.5" fill="#fef3c7" text-anchor="middle">One Unified Redemptive Story</text>
  </g>

  <!-- Connecting Lines -->
  <line x1="335" y1="180" x2="190" y2="125" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
  <line x1="465" y1="180" x2="610" y2="125" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
  <line x1="328" y1="235" x2="185" y2="235" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
  <line x1="472" y1="235" x2="615" y2="235" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
  <line x1="345" y1="280" x2="200" y2="340" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
  <line x1="455" y1="280" x2="600" y2="340" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>

  <!-- Node 1: Diverse Authorship & Origins (Top Left) -->
  <g filter="url(#shadow3)">
    <rect x="30" y="90" width="165" height="75" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="112" y="112" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#38bdf8" text-anchor="middle">DIVERSE ORIGINS</text>
    <text x="112" y="130" font-family="Segoe UI, Inter, sans-serif" font-size="9.5" fill="#e2e8f0" text-anchor="middle">40+ Human Authors</text>
    <text x="112" y="145" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Kings, Shepherds, Scholars</text>
  </g>

  <!-- Node 2: Multi-Genre Depth (Top Right) -->
  <g filter="url(#shadow3)">
    <rect x="605" y="90" width="165" height="75" rx="8" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
    <text x="687" y="112" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#4ade80" text-anchor="middle">RICH GENRES</text>
    <text x="687" y="130" font-family="Segoe UI, Inter, sans-serif" font-size="9.5" fill="#e2e8f0" text-anchor="middle">History, Laws, Poetry,</text>
    <text x="687" y="145" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Epistles, Prophecy &amp; Parables</text>
  </g>

  <!-- Node 3: Moral & Ethical Guide (Mid Left) -->
  <g filter="url(#shadow3)">
    <rect x="25" y="195" width="165" height="75" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="107" y="217" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#fbbf24" text-anchor="middle">MORAL COMPASS</text>
    <text x="107" y="235" font-family="Segoe UI, Inter, sans-serif" font-size="9.5" fill="#e2e8f0" text-anchor="middle">Foundational Ethics</text>
    <text x="107" y="250" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Integrity, Justice, Compassion</text>
  </g>

  <!-- Node 4: Legal & Social Reform (Mid Right) -->
  <g filter="url(#shadow3)">
    <rect x="610" y="195" width="165" height="75" rx="8" fill="#1e293b" stroke="#f472b6" stroke-width="1.5"/>
    <text x="692" y="217" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#f472b6" text-anchor="middle">SOCIAL TRANSFORMATION</text>
    <text x="692" y="235" font-family="Segoe UI, Inter, sans-serif" font-size="9.5" fill="#e2e8f0" text-anchor="middle">Human Rights &amp; Justice</text>
    <text x="692" y="250" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Pioneered MLK &amp; Abolitionists</text>
  </g>

  <!-- Node 5: Cultural & Linguistic Impact (Bottom Left) -->
  <g filter="url(#shadow3)">
    <rect x="35" y="305" width="170" height="75" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <text x="120" y="327" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#a78bfa" text-anchor="middle">CULTURE &amp; LANGUAGE</text>
    <text x="120" y="345" font-family="Segoe UI, Inter, sans-serif" font-size="9.5" fill="#e2e8f0" text-anchor="middle">Idioms, Art &amp; Literature</text>
    <text x="120" y="360" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Symphonies, Masterpieces</text>
  </g>

  <!-- Node 6: Spiritual Devotion & Communion (Bottom Right) -->
  <g filter="url(#shadow3)">
    <rect x="595" y="305" width="170" height="75" rx="8" fill="#1e293b" stroke="#2dd4bf" stroke-width="1.5"/>
    <text x="680" y="327" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="11" fill="#2dd4bf" text-anchor="middle">PERSONAL DEVOTION</text>
    <text x="680" y="345" font-family="Segoe UI, Inter, sans-serif" font-size="9.5" fill="#e2e8f0" text-anchor="middle">Daily Spiritual Nourishment</text>
    <text x="680" y="360" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Prayer, Hope, Character Growth</text>
  </g>

  <!-- Footer Banner -->
  <text x="400" y="426" font-family="Segoe UI, Inter, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">The Bible is not a dusty historic relic, but a living guide actively shaping individual lives and global societies.</text>
</svg>'''

SVG_4_SPIRITUAL_GROWTH = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <filter id="shadow4" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bgGrad4)" rx="12"/>

  <!-- Title Header -->
  <text x="400" y="42" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="20" fill="#f8fafc" text-anchor="middle">THE DAILY BIBLE STUDY &amp; SPIRITUAL GROWTH ENGINE</text>
  <text x="400" y="66" font-family="Segoe UI, Inter, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Structured 4-Step Inductive Loop: Pray -> Read -> Meditate -> Journal &amp; Apply</text>

  <!-- 4 Step Flow Cards -->
  <!-- Step 1: Pray -->
  <g filter="url(#shadow4)">
    <rect x="35" y="95" width="165" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="117" cy="135" r="24" fill="#0284c7"/>
    <text x="117" y="142" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="15" fill="#ffffff" text-anchor="middle">1</text>
    
    <text x="117" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="14" fill="#38bdf8" text-anchor="middle">PRAY</text>
    <text x="117" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="10.5" fill="#93c5fd" text-anchor="middle">Seek Illumination</text>

    <line x1="45" y1="210" x2="190" y2="210" stroke="#334155" stroke-width="1"/>

    <text x="117" y="232" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">Invite the Holy Spirit</text>
    <text x="117" y="248" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">to open your spiritual eyes</text>
    <text x="117" y="264" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">and soften your heart.</text>
    
    <rect x="47" y="288" width="141" height="50" rx="5" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="117" y="308" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#7dd3fc" text-anchor="middle">Scripture Anchor</text>
    <text x="117" y="324" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Psalm 119:18</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 205 225 L 225 225" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Step 2: Read -->
  <g filter="url(#shadow4)">
    <rect x="230" y="95" width="165" height="260" rx="8" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
    <circle cx="312" cy="135" r="24" fill="#16a34a"/>
    <text x="312" y="142" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="15" fill="#ffffff" text-anchor="middle">2</text>
    
    <text x="312" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="14" fill="#4ade80" text-anchor="middle">READ</text>
    <text x="312" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="10.5" fill="#86efac" text-anchor="middle">Observation</text>

    <line x1="240" y1="210" x2="385" y2="210" stroke="#334155" stroke-width="1"/>

    <text x="312" y="232" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">Read a short passage</text>
    <text x="312" y="248" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">slowly twice. Ask:</text>
    <text x="312" y="264" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">"What does it say?"</text>
    
    <rect x="242" y="288" width="141" height="50" rx="5" fill="#0f172a" stroke="#16a34a" stroke-width="1"/>
    <text x="312" y="308" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#86efac" text-anchor="middle">Scripture Anchor</text>
    <text x="312" y="324" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">1 Timothy 4:13</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 400 225 L 420 225" stroke="#4ade80" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Step 3: Meditate -->
  <g filter="url(#shadow4)">
    <rect x="425" y="95" width="165" height="260" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="507" cy="135" r="24" fill="#d97706"/>
    <text x="507" y="142" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="15" fill="#ffffff" text-anchor="middle">3</text>
    
    <text x="507" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="14" fill="#fbbf24" text-anchor="middle">MEDITATE</text>
    <text x="507" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="10.5" fill="#fde68a" text-anchor="middle">Interpretation</text>

    <line x1="435" y1="210" x2="580" y2="210" stroke="#334155" stroke-width="1"/>

    <text x="507" y="232" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">Reflect deeply on meaning.</text>
    <text x="507" y="248" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">Ask: "What does this</text>
    <text x="507" y="264" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">reveal about God?"</text>
    
    <rect x="437" y="288" width="141" height="50" rx="5" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="507" y="308" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#fcd34d" text-anchor="middle">Scripture Anchor</text>
    <text x="507" y="324" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">Joshua 1:8</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 595 225 L 615 225" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Step 4: Journal & Apply -->
  <g filter="url(#shadow4)">
    <rect x="620" y="95" width="165" height="260" rx="8" fill="#1e293b" stroke="#f472b6" stroke-width="2"/>
    <circle cx="702" cy="135" r="24" fill="#db2777"/>
    <text x="702" y="142" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="15" fill="#ffffff" text-anchor="middle">4</text>
    
    <text x="702" y="180" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="14" fill="#f472b6" text-anchor="middle">APPLY</text>
    <text x="702" y="198" font-family="Segoe UI, Inter, sans-serif" font-size="10.5" fill="#fbcfe8" text-anchor="middle">Journal &amp; Obey</text>

    <line x1="630" y1="210" x2="775" y2="210" stroke="#334155" stroke-width="1"/>

    <text x="702" y="232" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">Write key verse &amp; action:</text>
    <text x="702" y="248" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">"How will I live this out</text>
    <text x="702" y="264" font-family="Segoe UI, Inter, sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">at school and home today?"</text>
    
    <rect x="632" y="288" width="141" height="50" rx="5" fill="#0f172a" stroke="#db2777" stroke-width="1"/>
    <text x="702" y="308" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="9" fill="#f472b6" text-anchor="middle">Scripture Anchor</text>
    <text x="702" y="324" font-family="Segoe UI, Inter, sans-serif" font-size="9" fill="#94a3b8" text-anchor="middle">James 1:22</text>
  </g>

  <!-- Bottom Habit Tracker Banner -->
  <rect x="35" y="375" width="750" height="55" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="398" font-family="Segoe UI, Inter, sans-serif" font-weight="bold" font-size="12" fill="#38bdf8" text-anchor="middle">7-Day Character &amp; Reading Journal: Read 5-10 verses daily from Luke's Gospel</text>
  <text x="400" y="416" font-family="Segoe UI, Inter, sans-serif" font-size="10.5" fill="#94a3b8" text-anchor="middle">Consistency over volume: Regular spiritual feeding produces lasting Christian transformation and moral integrity.</text>
</svg>'''

# -----------------------------------------------------------------------------
# Curated Lessons Data (4 Units / Lessons)
# -----------------------------------------------------------------------------

LESSONS_DATA = [
    {
        "unit_order": 1,
        "unit_name": "Listing the New Testament Books & Canonical Order",
        "unit_desc": "Explore the 27 books of the New Testament, understanding their canonical sequence and theological progression.",
        "lesson_title": "Listing the New Testament Books",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Codex_Washingtonianus_%28Freer_Gospels%29_-_Mark_16.12-17_-_Freer_Gallery_of_Art.jpg",
            "title": "Codex Washingtonianus: Ancient New Testament Gospels",
            "caption": "Codex Washingtonianus (circa 4th-5th century AD), containing the four Gospels in early Greek script. Preserved in the Smithsonian Institution, Freer Gallery of Art.",
            "source": "Wikimedia Commons / Smithsonian Freer Gallery of Art"
        },
        "learning_goals": [
            "List all 27 books of the New Testament in their exact canonical sequence.",
            "Define 'Canon' and explain why the canonical order follows a theological rather than strictly chronological order.",
            "Understand the concept of the 'New Covenant' sealed through Jesus Christ."
        ],
        "card1_hook": (
            "Imagine walking into a library containing 27 uniquely bound volumes, written across several decades by different eyewitnesses, yet all telling a single, cohesive, breathtaking story. "
            "This is the New Testament—the second major division of the Holy Bible. The word 'Testament' translates to 'Covenant', meaning that these 27 books center entirely on the New Covenant established between God and humanity through the life, death, resurrection, and teachings of Jesus Christ."
        ),
        "card2_explanation": (
            "### The Divine Progression of the 27 Books\n\n"
            "The 27 books of the New Testament are arranged in a specific, logical sequence that reflects their theological and historical progression:\n\n"
            "1. **The 4 Gospels (Matthew, Mark, Luke, John):** The foundational eyewitness accounts and testimonies of the life, ministry, sacrificial death, and resurrection of Jesus Christ.\n"
            "2. **Church History (Acts of the Apostles):** The narrative of the Holy Spirit's empowerment of the early church, carrying the Gospel from Jerusalem to Rome.\n"
            "3. **The 13 Pauline Epistles (Romans to Philemon):** Letters written by Paul to specific churches and leaders to address doctrine, Christian ethics, and church order.\n"
            "4. **The 8 General Epistles (Hebrews to Jude):** Pastoral letters written by other apostles to encourage scattered believers facing trials.\n"
            "5. **Prophecy / Apocalypse (Revelation):** John's apocalyptic vision assuring believers of Christ's cosmic victory.\n\n"
            "### Core Scripture\n"
            "> *'All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness, so that the servant of God may be thoroughly equipped for every good work.'* — 2 Timothy 3:16-17"
        ),
        "svg": {
            "svg_xml": SVG_1_CANONICAL_ORDER,
            "title": "Canonical Architecture of the 27 New Testament Books",
            "caption": "Pedagogical blueprint illustrating the structured shelves of the New Testament Canon from Gospels to Revelation."
        },
        "card3_analytic": (
            "### Canonical Order vs. Chronological Order\n\n"
            "A vital analytic insight in New Testament studies is understanding why the books are arranged canonically rather than chronologically:\n\n"
            "* **Theological Priority:** The Gospels appear first because Christ's life and atonement are the historical and theological foundation upon which everything else rests.\n"
            "* **Chronological Reality:** Historically, several of Paul's letters (such as Galatians and 1 Thessalonians) were written before the written Gospels were finalized in their current form.\n"
            "* **Logical Flow:** The arrangement moves from the historical foundation (Gospels) to historical expansion (Acts), doctrinal application (Epistles), and ultimate consummation (Revelation)."
        ),
        "video": {
            "url": "https://www.youtube.com/watch?v=Q0BrP8KQZO0",
            "title": "BibleProject: New Testament Overview",
            "description": "An engaging visual overview explaining how the 27 books of the New Testament fit together into a unified redemptive narrative."
        },
        "card4_reflection": (
            "### Reflection: Navigating the Canonical Map\n\n"
            "Just as an index helps you locate a specific topic in an encyclopedia, knowing the canonical order of the New Testament allows you to find scriptural guidance without hesitation. "
            "When facing challenges—whether seeking peace in the Gospels, ethical direction in Paul's letters, or perseverance in James—the Holy Scriptures provide timely wisdom for every season of life."
        ),
        "card5_scenario": {
            "title": "Mastering the Canonical Sequence",
            "context": "A student in your CRE class struggles to locate the Epistle to the Colossians during class discussions because they do not know whether it is in the Old or New Testament, or where it sits among the Epistles.",
            "reflection_points": [
                "1. Memorize the 5 core divisions: Gospels (4), History (1), Pauline Epistles (13), General Epistles (8), and Prophecy (1).",
                "2. Use mnemonic associations for the Pauline letters: General Church letters are ordered generally from longest to shortest (Romans to Thessalonians) followed by Pastoral letters (Timothy, Titus, Philemon).",
                "3. Practice rapid book lookups during personal study to build navigation fluency."
            ]
        },
        "card6_summary": (
            "- The **New Testament** comprises **27 books** centered on the **New Covenant** established through Jesus Christ.\n"
            "- The books are arranged in **5 major sections**: Gospels (4), Church History (1), Pauline Epistles (13), General Epistles (8), and Prophecy (1).\n"
            "- Canonical arrangement follows **theological and historical logic** (Foundation -> Expansion -> Instruction -> Consummation) rather than writing date."
        ),
        "mcq": {
            "question": "Which of the following represents the correct canonical sequence of the New Testament divisions?",
            "options": [
                "Pauline Epistles, Gospels, Acts, General Epistles, Revelation",
                "Gospels, Acts, Pauline Epistles, General Epistles, Revelation",
                "Gospels, Pauline Epistles, General Epistles, Acts, Revelation",
                "Acts, Gospels, General Epistles, Pauline Epistles, Revelation"
            ],
            "correct_answer": "B",
            "explanation": "The canonical order opens with the 4 Gospels (foundation), followed by Acts (history/expansion), Pauline Epistles (church doctrine), General Epistles (universal pastoral letters), and Revelation (apocalyptic prophecy)."
        }
    },
    {
        "unit_order": 2,
        "unit_name": "Categorizing the New Testament Books into Five Genres",
        "unit_desc": "Classify the New Testament books across the 5 distinct literary genres: Gospels, History, Pauline Epistles, General Epistles, and Prophecy.",
        "lesson_title": "Categorizing the New Testament Books",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Papyrus_46_-_2_Corinthians_11.33-12.9_-_Chester_Beatty_Library_BP_II.jpg",
            "title": "Papyrus 46: The Chester Beatty Pauline Epistles",
            "caption": "Papyrus 46 (circa 200 AD), one of the oldest surviving Greek manuscripts of the Pauline Epistles, displaying 2 Corinthians. Preserved in the Chester Beatty Library.",
            "source": "Wikimedia Commons / Chester Beatty Library"
        },
        "learning_goals": [
            "Classify all 27 New Testament books into their 5 distinct literary genres.",
            "Distinguish between the Synoptic Gospels (Matthew, Mark, Luke) and the Gospel of John.",
            "Differentiate between descriptive historical narratives and prescriptive apostolic epistles."
        ],
        "card1_hook": (
            "If you were organizing a home library, you wouldn't toss poetry, science textbooks, cooking recipes, and historical biographies into an unorganized pile. You would group them by genre so you know how to read each one. "
            "Similarly, the 27 books of the New Testament fall into five distinct literary categories, each with its unique style, audience, and theological purpose."
        ),
        "card2_explanation": (
            "### Detailed Breakdown of the 5 Categories\n\n"
            "1. **The Gospels (4 Books):**\n"
            "   * *Synoptic Gospels (Matthew, Mark, Luke):* 'Synoptic' means 'seeing together'. They share a common narrative outline and parallel accounts of Jesus' Galilean ministry.\n"
            "   * *The Gospel of John:* Highly theological and thematic, highlighting Jesus' divine identity through profound discourses and 'I AM' statements.\n\n"
            "2. **Church History (1 Book - Acts):**\n"
            "   * Written by Luke as a sequel to his Gospel, documenting the birth of the Church at Pentecost and the spread of Christianity under the leadership of Peter and Paul.\n\n"
            "3. **Pauline Epistles (13 Books):**\n"
            "   * *Church Epistles (9):* Romans, 1 & 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 & 2 Thessalonians.\n"
            "   * *Pastoral Epistles (3):* 1 & 2 Timothy, Titus (guidelines for pastoral leadership and sound doctrine).\n"
            "   * *Personal Epistle (1):* Philemon (appeal for reconciliation and Christian brotherhood).\n\n"
            "4. **General Epistles (8 Books):**\n"
            "   * Hebrews, James, 1 & 2 Peter, 1, 2, 3 John, Jude. Known as 'Catholic' (universal) letters sent to wider Christian audiences.\n\n"
            "5. **Prophecy / Apocalypse (1 Book - Revelation):**\n"
            "   * Written by the Apostle John on Patmos, employing vivid apocalyptic imagery to reveal Christ's ultimate victory over evil."
        ),
        "svg": {
            "svg_xml": SVG_2_GENRE_TAXONOMY,
            "title": "The 5 Distinct Literary Genres of the New Testament",
            "caption": "Taxonomy diagram breaking down each New Testament genre by author, literary characteristics, and hermeneutical rules."
        },
        "card3_analytic": (
            "### Genre-Aware Interpretation: Descriptive vs. Prescriptive\n\n"
            "A critical principle of biblical hermeneutics is distinguishing between genre roles:\n\n"
            "* **Descriptive Texts (e.g., Acts):** Record *what happened* historically in a specific context. Not every event or pattern (such as communal property sharing or specific travel routes) is an absolute command for all believers in all eras.\n"
            "* **Prescriptive Texts (e.g., Romans, James):** Directly instruct *how believers must live* and define universal moral and doctrinal standards.\n"
            "* **Apocalyptic Symbolism (e.g., Revelation):** Employs cosmic figurative language (beasts, trumpets, seals) that must not be read with crude wooden literalism, but decoded through the lens of Old Testament imagery."
        ),
        "video": {
            "url": "https://www.youtube.com/watch?v=b-b4s2Dk6Qo",
            "title": "BibleProject: How to Read the New Testament Epistles",
            "description": "Learn how the New Testament letters were written as situational documents and how to trace their theological arguments."
        },
        "card4_reflection": (
            "### Reflection: Living Out the Epistles\n\n"
            "The New Testament Epistles were written to real people wrestling with real cultural pressures, interpersonal conflicts, and spiritual questions. "
            "When we read Paul's admonitions on unity in Ephesians or James' call for practical faith backed by good works, we receive timeless wisdom for our homes, schools, and communities."
        ),
        "card5_scenario": {
            "title": "Resolving a Genre Misunderstanding",
            "context": "During a youth fellowship discussion, a member insists that because Christians in Acts sold their houses and laid money at the Apostles' feet, any Christian today who owns private property is committing a sin.",
            "reflection_points": [
                "1. Clarify the distinction between descriptive historical narrative (what early Jerusalem Christians chose to do in their specific crisis) and prescriptive moral law.",
                "2. Note that elsewhere in the Epistles (e.g., 1 Timothy 6:17-19, 2 Thessalonians 3:10-12), believers are instructed to work diligently and practice generous hospitality with their resources.",
                "3. Emphasize that the core virtue demonstrated in Acts was radical love and generosity, which can be expressed in various practical ways today."
            ]
        },
        "card6_summary": (
            "- The NT contains **5 genres**: Gospels (4), History (1), Pauline Epistles (13), General Epistles (8), and Prophecy (1).\n"
            "- **Matthew, Mark, and Luke** are **Synoptic Gospels**, while **John** offers distinct theological and spiritual discourses.\n"
            "- **Acts** is descriptive history; the **Epistles** are prescriptive instructions; **Revelation** is symbolic apocalyptic prophecy."
        ),
        "mcq": {
            "question": "How many books in the New Testament are categorized as Pauline Epistles?",
            "options": [
                "4",
                "8",
                "13",
                "27"
            ],
            "correct_answer": "C",
            "explanation": "There are exactly 13 Pauline Epistles in the New Testament Canon, spanning from the Epistle to the Romans to the Epistle to Philemon."
        }
    },
    {
        "unit_order": 3,
        "unit_name": "The Bible as a Divine Library and Its Use in Contemporary Society",
        "unit_desc": "Analyze why the Bible is called 'Ta Biblia' (a library of books) and examine its profound ethical, social, and cultural impacts today.",
        "lesson_title": "The Bible as a Library and Its Use in Today's Society",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Saint_Jerome_in_His_Study_by_Domenico_Ghirlandaio.jpg",
            "title": "Saint Jerome in His Scriptorium Study",
            "caption": "Saint Jerome in His Study (1480 fresco by Domenico Ghirlandaio in Ognissanti, Florence), depicting the scholarly translation and preservation of the Holy Scriptures.",
            "source": "Wikimedia Commons / Church of Ognissanti Florence"
        },
        "learning_goals": [
            "Explain the etymological origin of the word 'Bible' ('Ta Biblia') and why Scripture is described as a library.",
            "Analyze the 4 core reasons the Bible functions as a unified library (diversity of authors, genres, timeline, and singular redemptive theme).",
            "Evaluate the multi-faceted roles of the Bible in modern society (ethics, justice, law, culture, and personal devotion)."
        ],
        "card1_hook": (
            "When we hold the Holy Bible, we hold a single book with a cover and spine. But did you know that the word 'Bible' comes from the Greek word 'Ta Biblia', which literally means 'The Books'? "
            "The Bible is not an isolated single volume—it is a divine library of 66 inspired books (39 Old Testament and 27 New Testament) composed over 1,500 years across three continents."
        ),
        "card2_explanation": (
            "### Why the Bible is Referred to as a 'Library'\n\n"
            "1. **Collection of Diverse Writings:** It contains multiple genres including historical narratives, legal codes, pastoral letters, poetry, proverbs, and apocalyptic visions.\n"
            "2. **Diverse Human Authors:** Written by over 40 human authors from vastly different backgrounds—from monarchs (David, Solomon) and scholars (Paul) to shepherds (Amos) and fishermen (Peter, John).\n"
            "3. **Spans Generations & Cultures:** Composed over approximately 1,500 years across Asia, Africa, and Europe in three ancient languages (Hebrew, Aramaic, and Greek).\n"
            "4. **Unified Redemptive Theme:** Despite extraordinary diversity, all 66 books weave together one non-contradictory grand narrative: God's redemptive plan to restore fallen humanity through Jesus Christ.\n\n"
            "### Uses of the Bible in Society Today\n\n"
            "* **Source of Christian Doctrine:** Provides the supreme rule for faith, preaching, and church guidance.\n"
            "* **Moral & Ethical Compass:** Universal principles of honesty, fidelity, justice, and compassion.\n"
            "* **Basis for Social & Legal Reform:** Inspired champions of justice (like Martin Luther King Jr. and William Wilberforce) to fight slavery and discrimination.\n"
            "* **Influence on Language & Arts:** Countless literary masterpieces, idioms ('the good Samaritan', 'extra mile'), and classical musical works trace directly to biblical scripture."
        ),
        "svg": {
            "svg_xml": SVG_3_BIBLE_LIBRARY,
            "title": "The Bible as a Divine Library & Its Societal Roles",
            "caption": "Concept map highlighting the 4 pillars of the Bible Library and its 6 major spheres of societal influence."
        },
        "card3_analytic": (
            "### The Divine Unity Behind Human Diversity\n\n"
            "If forty authors of different professions, centuries, and cultures were asked today to write essays on politics, morality, or religion, their opinions would sharply conflict. "
            "Yet the Bible's 66 books maintain complete harmony regarding the nature of God, the predicament of human sin, and the way of salvation through Christ. "
            "This supernatural coherence underscores the doctrine of divine inspiration (2 Peter 1:21: *'Prophets spoke from God as they were carried along by the Holy Spirit'*).\n"
        ),
        "video": {
            "url": "https://www.youtube.com/watch?v=ak06MSETeo4",
            "title": "BibleProject: The Story of the Bible",
            "description": "Discover how the diverse books of the Old and New Testaments unite to tell one epic story leading to Jesus Christ."
        },
        "card4_reflection": (
            "### Reflection: The Bible as a Living Agent of Change\n\n"
            "The Bible is not an antique museum display. In our schools, judicial courts, and daily lives, it serves as a plumbline for justice, human dignity, and moral integrity. "
            "When we allow Scripture to mold our thinking, we become ambassadors of truth and peacemaking in our communities."
        ),
        "card5_scenario": {
            "title": "Ethical Decision-Making: The Exam Leak Dilemma",
            "context": "Your classmate Joseph acquires leaked copies of the final national assessment answers and urges you to review them together so both of you can secure top grades and please your families.",
            "reflection_points": [
                "1. Apply biblical ethical principles: Exodus 20:16 ('Do not bear false witness') and Proverbs 11:1 ('The Lord detests dishonest scales').",
                "2. Recognize that cheating undermines genuine competence, erodes character, and violates academic justice.",
                "3. Firmly refuse the offer, explain the value of earned integrity, and encourage your friend to join an honest revision group."
            ]
        },
        "card6_summary": (
            "- The word **'Bible'** originates from **'Ta Biblia'** ('The Books'), representing a **divine library of 66 books**.\n"
            "- It was written by **40+ authors** over **1,500 years** in **3 languages**, yet exhibits a **single unified redemptive theme**.\n"
            "- In today's society, the Bible serves as a **moral compass, legal inspiration, cultural foundation**, and guide for **personal spiritual life**."
        ),
        "mcq": {
            "question": "Why is the Holy Bible accurately described as a 'divine library'?",
            "options": [
                "Because it was written by a single author in a single year inside a physical monastery",
                "Because it comprises 66 distinct books spanning diverse genres, authors, and eras, united by one redemptive message",
                "Because it is kept exclusively in academic university libraries and church vaults",
                "Because it only contains historical records of ancient governments"
            ],
            "correct_answer": "B",
            "explanation": "The Bible is a library ('Ta Biblia') because it brings together 66 diverse books written across 1,500 years by over 40 authors, harmonized by the Holy Spirit into one message of salvation in Christ."
        }
    },
    {
        "unit_order": 4,
        "unit_name": "Desiring Daily Bible Reading and Structured Journaling",
        "unit_desc": "Cultivate a personal, disciplined daily Bible reading routine and maintain a character reflection journal for spiritual growth.",
        "lesson_title": "Desiring Daily Bible Reading and Spiritual Growth",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Old_man_reading_the_Bible_by_Gerard_Dou_in_Louvre.jpg",
            "title": "An Old Man Reading the Bible (Gerard Dou)",
            "caption": "An Old Man Reading the Bible (1631 painting by Gerard Dou in the Musée du Louvre, Paris), illustrating focused daily meditation on the Holy Scriptures.",
            "source": "Wikimedia Commons / Musée du Louvre"
        },
        "learning_goals": [
            "Develop a vibrant personal desire for daily Scripture engagement as essential spiritual nourishment.",
            "Master the 4-step inductive reading method: Pray, Read (Observation), Meditate (Interpretation), and Apply (Obedience).",
            "Create and maintain a structured 7-day Bible reading and character reflection journal."
        ],
        "card1_hook": (
            "Have you ever tried to grow a seedling? If you water it once a month, it will quickly wither and die. It requires regular, daily nourishment and sunlight to grow strong. "
            "The same is true of your spiritual life. Daily reading of the Holy Scriptures is the primary way Christians nourish their souls, build character resilience, and grow in Christ-likeness."
        ),
        "card2_explanation": (
            "### The Biblical Blueprint for Daily Reading\n\n"
            "> *'Your word is a lamp for my feet, a light on my path.'* — Psalm 119:105\n\n"
            "### Benefits of Daily Scripture Engagement\n"
            "1. **Transformation of Character:** Scripture acts as a spiritual mirror, exposing flaws and encouraging virtues like patience, humility, self-control, and integrity.\n"
            "2. **Protection Against Deception & Extremism:** Thorough familiarity with biblical truth equips young people to identify false teachings, ungodly cults, and religious radicalism.\n"
            "3. **Wisdom in Daily Decision-Making:** Imparts divine insight to navigate modern peer pressure, ethical dilemmas, and academic choices with moral confidence.\n\n"
            "### The 4-Step Inductive Reading Process\n"
            "* **1. Pray:** Ask the Holy Spirit for spiritual illumination and receptive understanding.\n"
            "* **2. Read (Observation):** Read a short passage slowly twice. Ask: *'What does the text say?'*\n"
            "* **3. Meditate (Interpretation):** Reflect on the core truth. Ask: *'What does this reveal about God and His will?'*\n"
            "* **4. Apply (Obedience):** Write a concrete takeaway. Ask: *'How must I put this virtue into practice today?'*"
        ),
        "svg": {
            "svg_xml": SVG_4_SPIRITUAL_GROWTH,
            "title": "The Daily Bible Study & Spiritual Growth Engine",
            "caption": "Interactive workflow illustrating the 4-step loop from prayer to practical daily journaling and character habit formation."
        },
        "card3_analytic": (
            "### Quality over Quantity: Inductive Depth\n\n"
            "A common pitfall in spiritual disciplines is rushing through chapters simply to check off a reading box without internalizing the message. "
            "Reading **5 to 10 verses with deep inductive reflection and obedience** produces far greater character transformation than skimming several chapters passively. "
            "Scripture calls believers to be *'doers of the word, and not hearers only, deceiving yourselves'* (James 1:22)."
        ),
        "video": {
            "url": "https://www.youtube.com/watch?v=7hUs4TXRUWs",
            "title": "BibleProject: How to Read the Bible / Inductive Meditation",
            "description": "Discover the ancient art of biblical meditation and how daily engagement with Scripture renews our minds."
        },
        "card4_reflection": (
            "### Reflection: Building an Unshakeable Habit\n\n"
            "Spiritual growth is not accidental—it is cultivated through intentional daily choices. "
            "Choosing a specific time (early morning or before bed) and setting aside distractions allows the Word of God to renew your thoughts and guard your character against negative peer influences."
        ),
        "card5_scenario": {
            "title": "Setting Up Your 7-Day Gospel Reflection Journal",
            "context": "You decide to commit to a structured 7-day study plan focused on the Gospel of Luke to deepen your daily Christian walk.",
            "reflection_points": [
                "1. Choose a quiet time and consistent study space daily.",
                "2. Read 5 to 10 verses from Luke's Gospel using the 4-step loop.",
                "3. Record: Date, Passage, Key Verse, What it teaches about Jesus, and one Specific Action Step to practice at home or school."
            ]
        },
        "card6_summary": (
            "- Daily Bible reading is **essential spiritual food** that transforms character, protects against falsehood, and imparts divine wisdom.\n"
            "- Follow the **4-step inductive loop**: **Pray -> Read (Observation) -> Meditate (Interpretation) -> Apply (Obedience)**.\n"
            "- Maintain a **structured reflection journal** to translate scriptural insights into daily moral action."
        ),
        "mcq": {
            "question": "Which of the following is the most effective approach for developing a sustainable daily Bible reading habit?",
            "options": [
                "Rushing through ten chapters every week without taking notes or reflecting",
                "Reading only when preparing for CRE examinations or Sunday church services",
                "Setting a consistent daily time, praying for illumination, reading short passages inductively, and recording actionable reflection takeaways",
                "Relying solely on social media sermon snippets without ever opening a physical Bible"
            ],
            "correct_answer": "C",
            "explanation": "A sustainable habit combines a regular quiet time, prayer for understanding, careful inductive study of manageable passages, and recording practical life applications."
        }
    }
]

# -----------------------------------------------------------------------------
# Main Ingestion Function
# -----------------------------------------------------------------------------

@transaction.atomic
def ingest_topic_2_1():
    print("================================================================================")
    print("STARTING INGESTION: CBC Grade 10 CRE Topic 2.1: The New Testament Books")
    print("================================================================================")

    # 1. Fetch Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise RuntimeError("Curriculum 'CBC' not found in database!")

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        raise RuntimeError("Grade 10 not found under CBC!")

    subject = Subject.objects.filter(grade=grade, name__icontains="CRE").first()
    if not subject:
        raise RuntimeError("Subject 'CRE' not found under Grade 10!")

    print(f"Verified Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name} (Subject ID: {subject.id})")

    # 2. Get or Create Topic 2.1 (Order: 11)
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        order=11,
        defaults={
            "name": "Sub-Strand 2.1: The New Testament Books",
            "description": "Introduction to the 27 New Testament books, their canonical order, 5 distinct genres, the Bible as a divine library, and daily spiritual habits."
        }
    )
    if not created:
        topic.name = "Sub-Strand 2.1: The New Testament Books"
        topic.description = "Introduction to the 27 New Testament books, their canonical order, 5 distinct genres, the Bible as a divine library, and daily spiritual habits."
        topic.save()
        print(f"Updated existing Topic (ID: {topic.id}, Order: {topic.order})")
    else:
        print(f"Created new Topic (ID: {topic.id}, Order: {topic.order})")

    # Clean existing units/lessons for this topic to ensure idempotent freshness
    existing_units = LearningUnit.objects.filter(topic=topic)
    for u in existing_units:
        Lesson.objects.filter(learning_unit=u).delete()
    existing_units.delete()
    print("Cleaned existing LearningUnits, Lessons, and Blocks for Topic 2.1.")

    total_units = 0
    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    # 3. Ingest Lessons and Units
    for ldata in LESSONS_DATA:
        print(f"\nProcessing Unit {ldata['unit_order']}: {ldata['unit_name']}")

        # Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            name=ldata["unit_name"],
            description=ldata["unit_desc"],
            order=ldata["unit_order"]
        )
        total_units += 1

        # Create Lesson
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=ldata["lesson_title"],
            status="published",
            version=1,
            published_at=timezone.now()
        )
        total_lessons += 1

        # ---------------------------------------------------------------------
        # Card 1: Visual Hook + Learning Goals + Context Hook
        # ---------------------------------------------------------------------
        # Component 1: Photographic Image Hook
        img_data = ldata["image"]
        b_img = LessonBlock.objects.create(
            lesson=lesson,
            page_number=1,
            component_order=1,
            block_type="suggested_image",
            component_type="suggested_image",
            title=f"Visual Hook: {img_data['title']}",
            content={
                "url": img_data["url"],
                "resolved_image_url": img_data["url"],
                "title": img_data["title"],
                "caption": img_data["caption"],
                "source": img_data["source"]
            }
        )
        asset_img = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            source_type="external",
            storage_type="url",
            status="attached",
            title=img_data["title"],
            description=img_data["caption"],
            url=img_data["url"],
            metadata={"source": img_data["source"]}
        )
        b_img.assets.add(asset_img)
        total_blocks += 1
        total_assets += 1

        # Component 2: Learning Goals
        b_goals = LessonBlock.objects.create(
            lesson=lesson,
            page_number=1,
            component_order=2,
            block_type="learning_goal",
            component_type="learning_goal",
            title=f"Lesson Objectives: {ldata['lesson_title']}",
            content={"goals": ldata["learning_goals"]}
        )
        total_blocks += 1

        # Component 3: Introduction & Hook
        b_hook = LessonBlock.objects.create(
            lesson=lesson,
            page_number=1,
            component_order=3,
            block_type="concept_explanation",
            component_type="concept_explanation",
            title="Introduction: Walking into the New Testament",
            content={"markdown": ldata["card1_hook"]}
        )
        total_blocks += 1

        # ---------------------------------------------------------------------
        # Card 2: Core Concept Explanation & Detailed Content
        # ---------------------------------------------------------------------
        b_core = LessonBlock.objects.create(
            lesson=lesson,
            page_number=2,
            component_order=1,
            block_type="concept_explanation",
            component_type="concept_explanation",
            title=f"Core Content: {ldata['lesson_title']}",
            content={"markdown": ldata["card2_explanation"]}
        )
        total_blocks += 1

        # ---------------------------------------------------------------------
        # Card 3: Pedagogical Responsive Vector SVG Diagram & Analytic Callout
        # ---------------------------------------------------------------------
        svg_data = ldata["svg"]
        b_diag = LessonBlock.objects.create(
            lesson=lesson,
            page_number=3,
            component_order=1,
            block_type="suggested_diagram",
            component_type="suggested_diagram",
            title=f"Vector Blueprint: {svg_data['title']}",
            content={
                "svg": svg_data["svg_xml"],
                "svg_xml": svg_data["svg_xml"],
                "title": svg_data["title"],
                "caption": svg_data["caption"],
                "svg_content": svg_data["svg_xml"]
            }
        )
        asset_diag = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="embed",
            status="attached",
            title=svg_data["title"],
            description=svg_data["caption"],
            metadata={"svg_xml": svg_data["svg_xml"]}
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
        # Card 4: Curated Educational YouTube Video & Spiritual Reflection
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
        # Card 5: Step Process / Ethical Scenario / Values Application
        # ---------------------------------------------------------------------
        sc = ldata["card5_scenario"]
        sc_markdown = f"### {sc['title']}\n\n**Context:** {sc['context']}\n\n**Key Steps for Reflection & Action:**\n" + "\n".join(f"* {pt}" for pt in sc["reflection_points"])
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

        print(f"  -> Successfully Ingested 6 pages, {lesson.blocks.count()} blocks, {lesson.assets.count()} assets.")

    print("\n================================================================================")
    print("INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Learning Units Ingested: {total_units}")
    print(f"Total Lessons Ingested:        {total_lessons}")
    print(f"Total Blocks Ingested:         {total_blocks}")
    print(f"Total Assets Ingested:         {total_assets}")
    print("================================================================================")

if __name__ == "__main__":
    ingest_topic_2_1()
