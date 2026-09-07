"""
VLearn Grade 10 Aviation — Topic 365: Aviation Communication (Subject ID: 44, Topic ID: 365)
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aviation Communication (Topic ID: 365, Order: 7)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme #0f172a, Sanitized XML)
  - 5 Verified Educational YouTube Videos
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic365.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 365
# =============================================================================

# SVG 1: ICAO Phonetic Alphabet, Numerals, and Call Signs (Lesson 1)
SVG_PHONETIC_ALPHABET_NUMERALS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">ICAO Aviation Language Guide: Alphabet, Numerals &amp; Time</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Standardized Phonetic Spelling, Numeral Pronunciation, 24-Hour UTC, and Aircraft Call Signs</text>

  <!-- Left Column: ICAO Phonetic Alphabet -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#0284c7"/>
    <text x="115" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">ICAO PHONETIC ALPHABET</text>
    
    <g font-size="11" fill="#e2e8f0" transform="translate(15, 48)">
      <text y="0"><tspan font-weight="bold" fill="#38bdf8">A</tspan> — Alpha</text>
      <text y="20"><tspan font-weight="bold" fill="#38bdf8">B</tspan> — Bravo</text>
      <text y="40"><tspan font-weight="bold" fill="#38bdf8">C</tspan> — Charlie</text>
      <text y="60"><tspan font-weight="bold" fill="#38bdf8">D</tspan> — Delta</text>
      <text y="80"><tspan font-weight="bold" fill="#38bdf8">E</tspan> — Echo</text>
      <text y="100"><tspan font-weight="bold" fill="#38bdf8">F</tspan> — Foxtrot</text>
      <text y="120"><tspan font-weight="bold" fill="#38bdf8">G</tspan> — Golf</text>
      <text y="140"><tspan font-weight="bold" fill="#38bdf8">H</tspan> — Hotel</text>
      <text y="160"><tspan font-weight="bold" fill="#38bdf8">I</tspan> — India</text>
      <text y="180"><tspan font-weight="bold" fill="#38bdf8">J</tspan> — Juliet</text>
      <text y="200"><tspan font-weight="bold" fill="#38bdf8">K</tspan> — Kilo</text>
      <text y="220"><tspan font-weight="bold" fill="#38bdf8">L</tspan> — Lima</text>
    </g>
    <g font-size="11" fill="#e2e8f0" transform="translate(125, 48)">
      <text y="0"><tspan font-weight="bold" fill="#38bdf8">M</tspan> — Mike</text>
      <text y="20"><tspan font-weight="bold" fill="#38bdf8">N</tspan> — November</text>
      <text y="40"><tspan font-weight="bold" fill="#38bdf8">O</tspan> — Oscar</text>
      <text y="60"><tspan font-weight="bold" fill="#38bdf8">P</tspan> — Papa</text>
      <text y="80"><tspan font-weight="bold" fill="#38bdf8">Q</tspan> — Quebec</text>
      <text y="100"><tspan font-weight="bold" fill="#38bdf8">R</tspan> — Romeo</text>
      <text y="120"><tspan font-weight="bold" fill="#38bdf8">S</tspan> — Sierra</text>
      <text y="140"><tspan font-weight="bold" fill="#38bdf8">T</tspan> — Tango</text>
      <text y="160"><tspan font-weight="bold" fill="#38bdf8">U</tspan> — Uniform</text>
      <text y="180"><tspan font-weight="bold" fill="#38bdf8">V</tspan> — Victor</text>
      <text y="200"><tspan font-weight="bold" fill="#38bdf8">Y</tspan> — Yankee</text>
      <text y="220"><tspan font-weight="bold" fill="#38bdf8">Z</tspan> — Zulu</text>
    </g>
    
    <rect x="10" y="280" width="210" height="40" rx="6" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
    <text x="115" y="296" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">26 Acoustically Distinct Words</text>
    <text x="115" y="310" font-size="9" fill="#94a3b8" text-anchor="middle">Resistant to Static &amp; Language Accents</text>
  </g>

  <!-- Middle Column: ICAO Standard Numerals -->
  <g transform="translate(280, 80)">
    <rect x="0" y="0" width="240" height="330" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="240" height="30" rx="10" fill="#059669"/>
    <text x="120" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STANDARD AVIATION NUMERALS</text>

    <g font-size="11" fill="#e2e8f0" transform="translate(15, 45)">
      <rect x="0" y="0" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#34d399">0</tspan> : Nadazero <tspan fill="#94a3b8">[ZEE-RO]</tspan></text>
      
      <rect x="0" y="26" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="41"><tspan font-weight="bold" fill="#34d399">1</tspan> : Unaone <tspan fill="#94a3b8">[WUN]</tspan></text>

      <rect x="0" y="52" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="67"><tspan font-weight="bold" fill="#34d399">2</tspan> : Bissotwo <tspan fill="#94a3b8">[TOO]</tspan></text>

      <rect x="0" y="78" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="93"><tspan font-weight="bold" fill="#34d399">3</tspan> : Terrathree <tspan fill="#f59e0b">[TREE]</tspan></text>

      <rect x="0" y="104" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="119"><tspan font-weight="bold" fill="#34d399">4</tspan> : Kartefour <tspan fill="#f59e0b">[FOW-ER]</tspan></text>

      <rect x="0" y="130" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="145"><tspan font-weight="bold" fill="#34d399">5</tspan> : Pantafive <tspan fill="#f59e0b">[FIFE]</tspan></text>

      <rect x="0" y="156" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="171"><tspan font-weight="bold" fill="#34d399">6</tspan> : Soxisix <tspan fill="#94a3b8">[SIX]</tspan></text>

      <rect x="0" y="182" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="197"><tspan font-weight="bold" fill="#34d399">7</tspan> : Setteseven <tspan fill="#94a3b8">[SEV-EN]</tspan></text>

      <rect x="0" y="208" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="223"><tspan font-weight="bold" fill="#34d399">8</tspan> : Oktoeight <tspan fill="#94a3b8">[AIT]</tspan></text>

      <rect x="0" y="234" width="210" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="249"><tspan font-weight="bold" fill="#34d399">9</tspan> : Novenine <tspan fill="#f43f5e">[NIN-ER]</tspan></text>
    </g>

    <rect x="10" y="280" width="220" height="40" rx="6" fill="#1e293b" stroke="#059669" stroke-width="1"/>
    <text x="120" y="296" font-size="10" fill="#34d399" font-weight="bold" text-anchor="middle">Enunciate Every Digit Individually</text>
    <text x="120" y="310" font-size="9" fill="#94a3b8" text-anchor="middle">"9" = Novenine (avoids German "nein" = no)</text>
  </g>

  <!-- Right Column: Call Signs & UTC Time -->
  <g transform="translate(540, 80)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#d97706"/>
    <text x="115" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CALL SIGNS &amp; UTC TIME</text>

    <!-- Aircraft Tail Box -->
    <rect x="12" y="45" width="206" height="110" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="115" y="65" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">Kenyan Aircraft Call Sign</text>
    <rect x="40" y="75" width="150" height="26" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="115" y="93" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">5Y - KCA</text>
    <text x="115" y="118" font-size="9.5" fill="#38bdf8" text-anchor="middle">"Five Yankee Kilo Charlie Alpha"</text>
    <text x="115" y="132" font-size="8.5" fill="#94a3b8" text-anchor="middle">Commercial: "Kenya Airways 540"</text>

    <!-- 24-Hour UTC Box -->
    <rect x="12" y="170" width="206" height="100" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="115" y="190" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">24-Hour UTC (Zulu Time)</text>
    <text x="115" y="210" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">1430 Z</text>
    <text x="115" y="230" font-size="9.5" fill="#e2e8f0" text-anchor="middle">Spoken: "One four three zero"</text>
    <text x="115" y="246" font-size="8.5" fill="#f59e0b" text-anchor="middle">Eliminates time zone &amp; AM/PM errors</text>

    <rect x="12" y="280" width="206" height="40" rx="6" fill="#1e293b" stroke="#d97706" stroke-width="1"/>
    <text x="115" y="296" font-size="10" fill="#f59e0b" font-weight="bold" text-anchor="middle">Kenya Local Time vs UTC</text>
    <text x="115" y="310" font-size="9" fill="#94a3b8" text-anchor="middle">EAT = UTC + 3 hours (1500 EAT = 1200Z)</text>
  </g>
</svg>
""")

# SVG 2: Standard Phraseology Decision Flow & Roger vs Wilco (Lesson 2)
SVG_PHRASEOLOGY_FLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Phraseology Decision Flow: Roger vs. Wilco Protocol</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Regulatory Meanings, Mandatory Readbacks, and Aviation Vocabulary Matrix</text>

  <!-- Flowchart Container -->
  <g transform="translate(30, 80)">
    <!-- Step 1: Message Received -->
    <rect x="15" y="10" width="180" height="45" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="30" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">TRANSMISSION RECEIVED</text>
    <text x="105" y="44" font-size="9" fill="#94a3b8" text-anchor="middle">From Air Traffic Control</text>

    <!-- Down Arrow -->
    <line x1="105" y1="55" x2="105" y2="85" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <polygon points="105,90 100,80 110,80" fill="#38bdf8"/>

    <!-- Decision Diamond -->
    <polygon points="105,95 200,140 105,185 10,140" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="105" y="132" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">Does instruction require</text>
    <text x="105" y="146" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">active compliance</text>
    <text x="105" y="160" font-size="9" fill="#e2e8f0" text-anchor="middle">or control clearance?</text>

    <!-- Branch NO -> ROGER -->
    <line x1="10" y1="140" x2="-20" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="-20" y1="140" x2="-20" y2="215" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="-20" y1="215" x2="5" y2="215" stroke="#94a3b8" stroke-width="1.5"/>
    <polygon points="10,215 0,210 0,220" fill="#94a3b8"/>
    <text x="-15" y="135" font-size="10" font-weight="bold" fill="#94a3b8">NO</text>

    <rect x="10" y="195" width="180" height="55" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="100" y="215" font-size="13" font-weight="bold" fill="#94a3b8" text-anchor="middle">"ROGER"</text>
    <text x="100" y="230" font-size="9" fill="#cbd5e1" text-anchor="middle">Message received &amp; understood</text>
    <text x="100" y="242" font-size="8.5" fill="#ef4444" text-anchor="middle">(NO commitment to maneuver)</text>

    <!-- Branch YES -> WILCO / READBACK -->
    <line x1="200" y1="140" x2="235" y2="140" stroke="#34d399" stroke-width="2"/>
    <polygon points="240,140 230,135 230,145" fill="#34d399"/>
    <text x="210" y="132" font-size="10" font-weight="bold" fill="#34d399">YES</text>

    <rect x="240" y="105" width="220" height="70" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="350" y="127" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">"WILCO" or READBACK</text>
    <text x="350" y="145" font-size="9.5" fill="#ffffff" text-anchor="middle">"Will Comply — I am executing action"</text>
    <text x="350" y="162" font-size="8.5" fill="#38bdf8" text-anchor="middle">Mandatory for: Altitudes, Headings, Runways</text>
  </g>

  <!-- Right Panel: Standard Phraseology Matrix -->
  <g transform="translate(515, 80)">
    <rect x="0" y="0" width="255" height="235" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="255" height="28" rx="10" fill="#0284c7"/>
    <text x="127" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CORE PHRASEOLOGY VOCABULARY</text>

    <g font-size="10" fill="#e2e8f0" transform="translate(12, 38)">
      <text y="14"><tspan font-weight="bold" fill="#34d399">AFFIRM</tspan> : Yes (never say "yeah")</text>
      <text y="38"><tspan font-weight="bold" fill="#f43f5e">NEGATIVE</tspan> : No / Permission not granted</text>
      <text y="62"><tspan font-weight="bold" fill="#38bdf8">SAY AGAIN</tspan> : Repeat last transmission</text>
      <text y="86"><tspan font-weight="bold" fill="#f59e0b">CORRECTION</tspan> : An error was made, now correct</text>
      <text y="110"><tspan font-weight="bold" fill="#a855f7">STANDBY</tspan> : Wait and I will call you back</text>
      <text y="134"><tspan font-weight="bold" fill="#38bdf8">READ BACK</tspan> : Repeat all critical instructions</text>
      <text y="158"><tspan font-weight="bold" fill="#34d399">CLEARED</tspan> : Authorized to proceed as specified</text>
      <text y="182"><tspan font-weight="bold" fill="#f59e0b">UNABLE</tspan> : Cannot comply with request/clearance</text>
    </g>
  </g>

  <!-- Bottom Alert Bar: Prohibited Phraseology -->
  <g transform="translate(30, 340)">
    <rect x="0" y="0" width="740" height="70" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
    <text x="370" y="24" font-size="12" font-weight="bold" fill="#fca5a5" text-anchor="middle">CRITICAL SAFETY PROHIBITIONS IN RADIOTELEPHONY</text>
    <text x="370" y="44" font-size="10.5" fill="#ffffff" text-anchor="middle">1. NEVER say "Roger" to altitude, heading, or runway hold-short clearances — READ BACK REQUIRED!</text>
    <text x="370" y="60" font-size="10.5" fill="#fecaca" text-anchor="middle">2. NEVER say "Over and Out" together! "Over" invites a reply; "Out" closes the transmission. They are opposites!</text>
  </g>
</svg>
""")

# SVG 3: VHF Radio Technique and Push-To-Talk Protocol (Lesson 3)
SVG_RADIO_TECHNIQUE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">VHF Radio Transmission Technique &amp; Push-To-Talk (PTT) Protocol</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Cockpit Transceiver Operation, Microphone Boom Placement, and the 4 Ws Transmission Sequence</text>

  <!-- Left Column: Microphone & Headset Technique -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#0284c7"/>
    <text x="115" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">HEADSET &amp; MICROPHONE SETUP</text>

    <!-- Headset graphic representation -->
    <path d="M 65 95 C 65 50 165 50 165 95" fill="none" stroke="#64748b" stroke-width="8"/>
    <rect x="50" y="90" width="26" height="42" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="154" y="90" width="26" height="42" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Boom mic arm -->
    <path d="M 63 120 Q 90 145 115 140" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <ellipse cx="120" cy="140" rx="9" ry="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>

    <!-- Distance arrow -->
    <line x1="120" y1="155" x2="120" y2="185" stroke="#34d399" stroke-width="1.5"/>
    <text x="120" y="200" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">2.0 – 3.0 cm</text>
    <text x="120" y="215" font-size="9" fill="#94a3b8" text-anchor="middle">(One finger width from lips)</text>

    <g font-size="10" fill="#e2e8f0" transform="translate(15, 235)">
      <text y="0">• <tspan fill="#34d399">Too close</tspan>: Breath popping &amp; distortion</text>
      <text y="20">• <tspan fill="#f59e0b">Too far</tspan>: Cockpit noise cancels voice</text>
      <text y="40">• <tspan fill="#38bdf8">Tone</tspan>: Calm conversational volume</text>
      <text y="60">• <tspan fill="#38bdf8">Speed</tspan>: Measured 100 words/min</text>
    </g>
  </g>

  <!-- Middle Column: Cockpit VHF Radio -->
  <g transform="translate(280, 80)">
    <rect x="0" y="0" width="240" height="330" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="240" height="30" rx="10" fill="#059669"/>
    <text x="120" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">COCKPIT VHF TRANSCEIVER</text>

    <!-- Radio Box Faceplate -->
    <rect x="15" y="45" width="210" height="125" rx="6" fill="#1e293b" stroke="#475569" stroke-width="2"/>
    <rect x="25" y="55" width="85" height="34" rx="4" fill="#022c22" stroke="#059669" stroke-width="1"/>
    <text x="67" y="77" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">121.800</text>
    <text x="67" y="100" font-size="8" fill="#94a3b8" text-anchor="middle">ACTIVE (Ground)</text>

    <rect x="130" y="55" width="85" height="34" rx="4" fill="#1e1e24" stroke="#64748b" stroke-width="1"/>
    <text x="172" y="77" font-size="15" font-weight="bold" fill="#94a3b8" text-anchor="middle">118.100</text>
    <text x="172" y="100" font-size="8" fill="#64748b" text-anchor="middle">STANDBY (Tower)</text>

    <!-- Flip button -->
    <circle cx="120" cy="72" r="7" fill="#0284c7"/>
    <text x="120" y="75" font-size="8" fill="#ffffff" text-anchor="middle">⇄</text>

    <!-- Knobs -->
    <circle cx="50" cy="135" r="14" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <text x="50" y="158" font-size="8" fill="#94a3b8" text-anchor="middle">VOL/SQ</text>
    <circle cx="180" cy="135" r="16" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <text x="180" y="158" font-size="8" fill="#94a3b8" text-anchor="middle">FREQ TUNE</text>

    <!-- Simplex Warning -->
    <rect x="12" y="190" width="216" height="125" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="120" y="210" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">SIMPLEX FREQUENCY DYNAMICS</text>
    <text x="120" y="230" font-size="9" fill="#e2e8f0" text-anchor="middle">Shared channel across 100-mile radius</text>
    <text x="120" y="250" font-size="9.5" fill="#f87171" font-weight="bold" text-anchor="middle">Only ONE station transmits at once!</text>
    <text x="120" y="270" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Two transmitters at once = "STEPPING"</text>
    <text x="120" y="285" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Produces high-pitch squeal &amp; blocks calls</text>
    <text x="120" y="303" font-size="9" fill="#34d399" font-weight="bold" text-anchor="middle">ALWAYS LISTEN BEFORE SPEAKING!</text>
  </g>

  <!-- Right Column: PTT Cycle & 4 Ws -->
  <g transform="translate(540, 80)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#d97706"/>
    <text x="115" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">THE 5-STEP PTT CYCLE &amp; 4 Ws</text>

    <!-- 5 Steps -->
    <g font-size="9.5" fill="#e2e8f0" transform="translate(12, 45)">
      <text y="0"><tspan font-weight="bold" fill="#f59e0b">1.</tspan> <tspan font-weight="bold">LISTEN 3 SECONDS</tspan> (Verify clear)</text>
      <text y="18"><tspan font-weight="bold" fill="#f59e0b">2.</tspan> <tspan font-weight="bold">FORMULATE</tspan> message mentally</text>
      <text y="36"><tspan font-weight="bold" fill="#f59e0b">3.</tspan> <tspan font-weight="bold">PRESS PTT</tspan> &amp; pause 0.5 sec</text>
      <text y="54"><tspan font-weight="bold" fill="#f59e0b">4.</tspan> <tspan font-weight="bold">SPEAK</tspan> standard phraseology</text>
      <text y="72"><tspan font-weight="bold" fill="#f59e0b">5.</tspan> <tspan font-weight="bold">RELEASE PTT</tspan> to listen for reply</text>
    </g>

    <!-- The 4 Ws Box -->
    <rect x="10" y="135" width="210" height="180" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="115" y="155" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE 4 Ws STRUCTURE</text>

    <g font-size="9" fill="#e2e8f0" transform="translate(18, 172)">
      <text y="0" font-weight="bold" fill="#38bdf8">1. WHO ARE YOU CALLING?</text>
      <text y="14" fill="#94a3b8">"Wilson Ground..."</text>
      
      <text y="32" font-weight="bold" fill="#38bdf8">2. WHO ARE YOU?</text>
      <text y="46" fill="#94a3b8">"...Five Yankee Kilo Charlie Alpha..."</text>
      
      <text y="64" font-weight="bold" fill="#38bdf8">3. WHERE ARE YOU?</text>
      <text y="78" fill="#94a3b8">"...at light aircraft apron..."</text>
      
      <text y="96" font-weight="bold" fill="#38bdf8">4. WHAT DO YOU WANT?</text>
      <text y="110" fill="#94a3b8">"...request taxi to runway one four."</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Aircraft Marshalling Signals & Tower Light Gun Codes (Lesson 4)
SVG_MARSHALLING_LIGHTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aircraft Marshalling Signals &amp; Control Tower Light Gun Codes</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Standard Ground Handling Gestures with Wands and Emergency Optical Signaling Codes</text>

  <!-- Marshaller Card 1: Proceed Straight -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="165" height="190" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="24" rx="8" fill="#0284c7"/>
    <text x="82" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">PROCEED STRAIGHT</text>

    <!-- Figure -->
    <circle cx="82" cy="50" r="10" fill="#f59e0b"/>
    <rect x="74" y="62" width="16" height="38" rx="3" fill="#f97316"/>
    <!-- Arms up & wands -->
    <line x1="74" y1="68" x2="52" y2="45" stroke="#e2e8f0" stroke-width="3"/>
    <line x1="52" y1="45" x2="52" y2="28" stroke="#f59e0b" stroke-width="5"/>
    <line x1="90" y1="68" x2="112" y2="45" stroke="#e2e8f0" stroke-width="3"/>
    <line x1="112" y1="45" x2="112" y2="28" stroke="#f59e0b" stroke-width="5"/>
    <!-- Motion arrows -->
    <path d="M 45 35 L 45 45" stroke="#38bdf8" stroke-width="1.5"/>
    <path d="M 119 35 L 119 45" stroke="#38bdf8" stroke-width="1.5"/>
    <!-- Legs -->
    <line x1="77" y1="100" x2="72" y2="135" stroke="#475569" stroke-width="4"/>
    <line x1="87" y1="100" x2="92" y2="135" stroke="#475569" stroke-width="4"/>

    <text x="82" y="155" font-size="9" fill="#e2e8f0" text-anchor="middle">Raise wands &amp; move</text>
    <text x="82" y="170" font-size="9" fill="#38bdf8" font-weight="bold" text-anchor="middle">up and down steadily</text>
  </g>

  <!-- Marshaller Card 2: Turn Left / Right -->
  <g transform="translate(220, 80)">
    <rect x="0" y="0" width="165" height="190" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="24" rx="8" fill="#059669"/>
    <text x="82" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">STEERING TURNS</text>

    <!-- Figure -->
    <circle cx="82" cy="50" r="10" fill="#f59e0b"/>
    <rect x="74" y="62" width="16" height="38" rx="3" fill="#f97316"/>
    <!-- Left arm down pointing, right arm sweeping -->
    <line x1="74" y1="68" x2="48" y2="95" stroke="#e2e8f0" stroke-width="3"/>
    <line x1="48" y1="95" x2="40" y2="110" stroke="#f59e0b" stroke-width="5"/>
    <line x1="90" y1="68" x2="115" y2="50" stroke="#e2e8f0" stroke-width="3"/>
    <line x1="115" y1="50" x2="100" y2="35" stroke="#f59e0b" stroke-width="5"/>
    <!-- Legs -->
    <line x1="77" y1="100" x2="72" y2="135" stroke="#475569" stroke-width="4"/>
    <line x1="87" y1="100" x2="92" y2="135" stroke="#475569" stroke-width="4"/>

    <text x="82" y="155" font-size="9" fill="#e2e8f0" text-anchor="middle">Point arm toward wing</text>
    <text x="82" y="170" font-size="9" fill="#34d399" font-weight="bold" text-anchor="middle">Sweep other wand to face</text>
  </g>

  <!-- Marshaller Card 3: Emergency Stop -->
  <g transform="translate(410, 80)">
    <rect x="0" y="0" width="165" height="190" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="24" rx="8" fill="#dc2626"/>
    <text x="82" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">EMERGENCY STOP</text>

    <!-- Figure -->
    <circle cx="82" cy="50" r="10" fill="#f59e0b"/>
    <rect x="74" y="62" width="16" height="38" rx="3" fill="#f97316"/>
    <!-- Arms crossed overhead in X -->
    <line x1="74" y1="68" x2="105" y2="28" stroke="#ef4444" stroke-width="4"/>
    <line x1="90" y1="68" x2="59" y2="28" stroke="#ef4444" stroke-width="4"/>
    <circle cx="82" cy="38" r="4" fill="#ffffff"/>
    <!-- Legs -->
    <line x1="77" y1="100" x2="68" y2="135" stroke="#475569" stroke-width="4"/>
    <line x1="87" y1="100" x2="96" y2="135" stroke="#475569" stroke-width="4"/>

    <text x="82" y="155" font-size="9" fill="#e2e8f0" text-anchor="middle">Cross wands overhead</text>
    <text x="82" y="170" font-size="9.5" fill="#ef4444" font-weight="bold" text-anchor="middle">Rigid "X" Shape Rapidly</text>
  </g>

  <!-- Marshaller Card 4: Cut Engines -->
  <g transform="translate(600, 80)">
    <rect x="0" y="0" width="165" height="190" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="24" rx="8" fill="#d97706"/>
    <text x="82" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">CUT ENGINES</text>

    <!-- Figure -->
    <circle cx="82" cy="50" r="10" fill="#f59e0b"/>
    <rect x="74" y="62" width="16" height="38" rx="3" fill="#f97316"/>
    <!-- Slicing motion across throat -->
    <line x1="74" y1="68" x2="60" y2="70" stroke="#e2e8f0" stroke-width="3"/>
    <line x1="60" y1="70" x2="115" y2="58" stroke="#f59e0b" stroke-width="4"/>
    <line x1="90" y1="68" x2="95" y2="105" stroke="#e2e8f0" stroke-width="3"/>
    <!-- Legs -->
    <line x1="77" y1="100" x2="72" y2="135" stroke="#475569" stroke-width="4"/>
    <line x1="87" y1="100" x2="92" y2="135" stroke="#475569" stroke-width="4"/>

    <text x="82" y="155" font-size="9" fill="#e2e8f0" text-anchor="middle">Draw hand / wand</text>
    <text x="82" y="170" font-size="9" fill="#f59e0b" font-weight="bold" text-anchor="middle">across throat horizontally</text>
  </g>

  <!-- Bottom Panel: Control Tower Light Gun Signals -->
  <g transform="translate(30, 285)">
    <rect x="0" y="0" width="735" height="125" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="735" height="24" rx="8" fill="#1e293b"/>
    <text x="367" y="16" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">CONTROL TOWER LIGHT GUN CODES (RADIO FAILURE / NORDO AIRCRAFT)</text>

    <g font-size="9" transform="translate(15, 32)">
      <!-- Steady Green -->
      <circle cx="10" cy="12" r="7" fill="#22c55e"/>
      <text x="25" y="15" fill="#ffffff" font-weight="bold">Steady Green:</text>
      <text x="110" y="15" fill="#94a3b8">Ground: Cleared for Takeoff | Flight: Cleared to Land</text>

      <!-- Flashing Green -->
      <circle cx="10" cy="34" r="7" fill="#86efac" stroke="#22c55e" stroke-dasharray="2,2"/>
      <text x="25" y="37" fill="#ffffff" font-weight="bold">Flashing Green:</text>
      <text x="110" y="37" fill="#94a3b8">Ground: Cleared to Taxi | Flight: Return for Landing (await steady green)</text>

      <!-- Steady Red -->
      <circle cx="10" cy="56" r="7" fill="#ef4444"/>
      <text x="25" y="59" fill="#ffffff" font-weight="bold">Steady Red:</text>
      <text x="110" y="59" fill="#fca5a5" font-weight="bold">Ground: STOP IMMEDIATELY | Flight: Give Way, Continue Circling</text>

      <!-- Flashing Red -->
      <circle cx="10" cy="78" r="7" fill="#fca5a5" stroke="#ef4444" stroke-dasharray="2,2"/>
      <text x="25" y="81" fill="#ffffff" font-weight="bold">Flashing Red:</text>
      <text x="110" y="81" fill="#94a3b8">Ground: Taxi Clear of Runway | Flight: Airport Unsafe, Do Not Land</text>
    </g>
  </g>
</svg>
""")

# SVG 5: Integrated Airport Communication Simulation (Lesson 5)
SVG_INTEGRATED_SIMULATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Integrated Airport Communication Network: The Multi-Role Safety Web</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Synchronizing Control Tower, Flight Dispatch, Cockpit, Ground Crew, and Avionics Engineering</text>

  <!-- Top Center: Control Tower -->
  <g transform="translate(300, 80)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="200" height="22" rx="8" fill="#0284c7"/>
    <text x="100" y="15" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">CONTROL TOWER (ATC)</text>
    <text x="100" y="38" font-size="9.5" fill="#38bdf8" font-weight="bold" text-anchor="middle">Ground: 121.8 | Tower: 118.1</text>
    <text x="100" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">Runway Separation &amp; Taxi Routes</text>
    <text x="100" y="66" font-size="8.5" fill="#34d399" text-anchor="middle">Issues Clearances &amp; Verifies Readbacks</text>
  </g>

  <!-- Center: Cockpit (Cessna 5Y-KCA) -->
  <g transform="translate(300, 195)">
    <rect x="0" y="0" width="200" height="85" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="200" height="22" rx="8" fill="#d97706"/>
    <text x="100" y="15" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">AIRCRAFT COCKPIT (5Y-KCA)</text>
    <text x="100" y="38" font-size="9.5" fill="#f59e0b" font-weight="bold" text-anchor="middle">Pilot-in-Command</text>
    <text x="100" y="52" font-size="8.5" fill="#e2e8f0" text-anchor="middle">VHF Comm 1 &amp; Comm 2 Transceivers</text>
    <text x="100" y="66" font-size="8.5" fill="#38bdf8" text-anchor="middle">Mandatory Readback &amp; 4 Ws Calls</text>
    <text x="100" y="78" font-size="8" fill="#94a3b8" text-anchor="middle">Priority: Aviate, Navigate, Communicate</text>
  </g>

  <!-- Top Left: Flight Dispatch -->
  <g transform="translate(40, 120)">
    <rect x="0" y="0" width="190" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#7e22ce"/>
    <text x="95" y="15" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">FLIGHT DISPATCH / AOC</text>
    <text x="95" y="38" font-size="9" fill="#c084fc" font-weight="bold" text-anchor="middle">Operational Flight Plan</text>
    <text x="95" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">Weather Briefing &amp; Fuel Calculations</text>
    <text x="95" y="66" font-size="8" fill="#e2e8f0" text-anchor="middle">Datalink / Satellite Tracking</text>
  </g>

  <!-- Bottom Left: Ground Marshalling -->
  <g transform="translate(40, 240)">
    <rect x="0" y="0" width="190" height="75" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#059669"/>
    <text x="95" y="15" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">RAMP MARSHALLER &amp; CREW</text>
    <text x="95" y="38" font-size="9" fill="#34d399" font-weight="bold" text-anchor="middle">Visual Guidance Wands</text>
    <text x="95" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">Headset Cord to Nose Gear Interphone</text>
    <text x="95" y="66" font-size="8" fill="#e2e8f0" text-anchor="middle">FOD Sweeps &amp; Chock Placement</text>
  </g>

  <!-- Right: Avionics & Telecommunications Engineering -->
  <g transform="translate(570, 175)">
    <rect x="0" y="0" width="190" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#0284c7"/>
    <text x="95" y="15" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">AVIONICS ENGINEERING</text>
    <text x="95" y="38" font-size="9" fill="#38bdf8" font-weight="bold" text-anchor="middle">Radio &amp; Radar Maintenance</text>
    <text x="95" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">VHF Repeaters &amp; Antennas</text>
    <text x="95" y="66" font-size="8.5" fill="#94a3b8" text-anchor="middle">Light Gun Calibration &amp; Testing</text>
    <text x="95" y="82" font-size="8.5" fill="#34d399" font-weight="bold" text-anchor="middle">Guarantees 99.999% Reliability</text>
  </g>

  <!-- Connecting Lines & Vectors -->
  <!-- Tower to Cockpit -->
  <line x1="400" y1="155" x2="400" y2="195" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- Dispatch to Cockpit -->
  <path d="M 230 157 C 265 157 265 220 300 220" fill="none" stroke="#c084fc" stroke-width="2"/>
  <!-- Marshaller to Cockpit -->
  <line x1="230" y1="260" x2="300" y2="250" stroke="#34d399" stroke-width="2"/>
  <!-- Avionics to Tower & Cockpit -->
  <line x1="570" y1="210" x2="500" y2="210" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2"/>
  <path d="M 665 175 C 665 117 550 117 500 117" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2"/>

  <!-- Bottom Banner: Closed Loop Communication -->
  <g transform="translate(30, 345)">
    <rect x="0" y="0" width="740" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="370" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">CLOSED-LOOP COMMUNICATION: THE ACCIDENT PREVENTION SHIELD</text>
    <text x="370" y="44" font-size="10" fill="#ffffff" text-anchor="middle">1. SENDER TRANSMITS CLEARANCE  ➔  2. RECEIVER READS BACK IN FULL  ➔  3. SENDER CONFIRMS "READBACK CORRECT"</text>
    <text x="370" y="58" font-size="9" fill="#94a3b8" text-anchor="middle">Wilson Airport Simulation: Pilot (5Y-KCA) + Ground Controller + Tower Controller + Dispatcher + Marshaller</text>
  </g>
</svg>
""")

# =============================================================================
# ASSET DATA DEFINITIONS
# =============================================================================

PHOTO_HOOKS = {
    0: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Radiotelephony_Spelling_Alphabet_%281955%29.jpg",
        "title": "Historical ICAO Radiotelephony Spelling Alphabet Chart",
        "caption": "An official ICAO radiotelephony spelling alphabet reference sheet demonstrating the standardized pronunciation of international aviation letters and numerals to ensure clarity through radio static.",
        "author": "International Civil Aviation Organization (ICAO)",
        "license": "Public Domain"
    },
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Navcom_radio_Bendix_King.jpg",
        "title": "Aviation Nav/Comm Transceiver Control Unit",
        "caption": "A standard cockpit navigation and VHF communication radio console showing active frequency displays used by pilots to transmit standard phraseology and receive ATC clearances.",
        "author": "Wikimedia Commons Contributor",
        "license": "Creative Commons Attribution-Share Alike"
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/KOYO_KTR-1770.jpg",
        "title": "Cockpit VHF Aviation Transceiver Unit",
        "caption": "An aircraft very high frequency (VHF) transceiver operating within the 118.000 to 136.975 MHz band, equipped with frequency select knobs and transmit status indicators.",
        "author": "Wikimedia Commons Contributor",
        "license": "Creative Commons Attribution-Share Alike"
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/83/A_Polish_airman_marshals_a_U.S._Air_Force_C-130J_Super_Hercules_aircraft_March_13%2C_2014%2C_at_Lask_Air_Base%2C_Poland_140313-F-BH566-088.jpg",
        "title": "Aircraft Marshaller Guiding an Airplane on the Apron",
        "caption": "A certified ground operations marshaller holding high-visibility day-glo wands to direct a taxiing transport aircraft safely into its designated parking stand on the apron.",
        "author": "U.S. Air Force / Tech. Sgt. Matthew Hannen",
        "license": "Public Domain"
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Air_traffic_controller_Marines_keep_pilots_in_line_DVIDS447875.jpg",
        "title": "Air Traffic Controllers Operating Radar Displays and Radio Consoles",
        "caption": "Air traffic control specialists managing airspace sectors using live radar monitors and VHF radiotelephony to maintain separation and sequence arrivals and departures.",
        "author": "U.S. Marine Corps / Lance Cpl. Ronald E. Molyneux",
        "license": "Public Domain"
    }
}

SVG_MAP = {
    0: {
        "title": "The ICAO Aviation Language Guide: Alphabet, Numerals & Call Signs",
        "svg": SVG_PHONETIC_ALPHABET_NUMERALS,
        "page": 4
    },
    1: {
        "title": "Standard Phraseology Decision Flow: Roger vs. Wilco Protocol",
        "svg": SVG_PHRASEOLOGY_FLOW,
        "page": 4
    },
    2: {
        "title": "VHF Radio Setup & Push-To-Talk (PTT) Protocol",
        "svg": SVG_RADIO_TECHNIQUE,
        "page": 4
    },
    3: {
        "title": "Aircraft Marshalling Signals & Tower Light Gun Codes",
        "svg": SVG_MARSHALLING_LIGHTS,
        "page": 4
    },
    4: {
        "title": "Integrated Airport Communication Network: The Safety Web",
        "svg": SVG_INTEGRATED_SIMULATION,
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "url": "https://www.youtube.com/watch?v=-MpdaGEaHJE",
        "title": "Airspace and ATC Radiotelephony Communications",
        "description": "Watch how pilots adjust headsets, pronounce the ICAO phonetic alphabet, articulate numerals, and manage Coordinated Universal Time (Zulu Time) in active airspace."
    },
    1: {
        "url": "https://www.youtube.com/watch?v=8uRuqyJfJP4",
        "title": "Standard Phrases for Aviation Radio Communications",
        "description": "Learn the vital standard phraseology words used by pilots and air traffic controllers, demonstrating crisp pacing, clearance readbacks, and how to eliminate hesitation."
    },
    2: {
        "url": "https://www.youtube.com/watch?v=FViSA91DP-8",
        "title": "Human Factors in Aviation Safety and Communications",
        "description": "Examine how stress, workload, fatigue, and poor communication discipline contribute to aeronautical errors, and see how standardized procedures build a robust safety net."
    },
    3: {
        "url": "https://www.youtube.com/watch?v=XEo0q9-i4k0",
        "title": "Aircraft Marshalling Signals Explained — Hand Signals Every Pilot Must Know",
        "description": "Watch a certified ground handling professional demonstrate standard airport marshalling wand gestures next to aircraft, highlighting straight taxiing, turns, normal stop, emergency stop, and engine shutdown."
    },
    4: {
        "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs",
        "title": "Airport Operations and Airfield Communications Architecture",
        "description": "Explore the physical architecture of modern airports, illustrating how ground control, tower personnel, apron handlers, and flight crews synchronize operations across complex runway systems."
    }
}

def enrich_grade10_topic365():
    """Enriches Grade 10 Aviation Topic 365 with photographic hooks, SVGs, and videos."""
    print("=" * 80)
    print("VLEARN VISUAL ENRICHMENT: Grade 10 Aviation — Topic 365 (ID: 365)")
    print("Aviation Communication")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)
    topic = Topic.objects.get(id=365, subject=subject)

    print(f"[*] Topic: {topic.name} (ID: {topic.id})")

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} Lessons to enrich.")

    total_photos_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n--- Processing Lesson {u_order + 1}: {lesson.title} (ID: {lesson.id}) ---")

        # ---------------------------------------------------------------------
        # 1. First-Card Photographic Visual Hooks
        # ---------------------------------------------------------------------
        if u_order in PHOTO_HOOKS:
            img_def = PHOTO_HOOKS[u_order]
            img_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if img_block:
                b_content = img_block.content or {}
                b_content["resolved_image_url"] = img_def["url"]
                b_content["url"] = img_def["url"]
                b_content["caption"] = img_def["caption"]
                b_content["title"] = img_def["title"]
                img_block.content = b_content
                img_block.title = img_def["title"]
                img_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    asset_type="image",
                    url=img_def["url"],
                    defaults={
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "title": img_def["title"],
                        "description": img_def["caption"],
                        "metadata": {
                            "author": img_def["author"],
                            "licensing": img_def["license"],
                            "topic_order": 7,
                            "unit_order": u_order,
                            "page": 1
                        }
                    }
                )
                img_block.assets.add(asset)
                total_photos_attached += 1
                total_assets_persisted += 1
                print(f"  [Photo Hook Attached] {img_def['title']}")

        # ---------------------------------------------------------------------
        # 2. Custom Responsive Vector SVGs
        # ---------------------------------------------------------------------
        if u_order in SVG_MAP:
            svg_def = SVG_MAP[u_order]
            diag_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            if diag_block:
                diag_content = diag_block.content or {}
                diag_content["svg"] = svg_def["svg"]
                diag_content["svg_xml"] = svg_def["svg"]
                diag_content["title"] = svg_def["title"]
                diag_block.content = diag_content
                diag_block.title = svg_def["title"]
                diag_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    asset_type="diagram",
                    title=f"Lesson {u_order + 1} Diagram: {svg_def['title']}",
                    defaults={
                        "source_type": "ai_generated",
                        "storage_type": "embed",
                        "status": "attached",
                        "description": svg_def["title"],
                        "metadata": {
                            "topic_order": 7,
                            "unit_order": u_order,
                            "page": svg_def["page"],
                            "svg_content": svg_def["svg"]
                        }
                    }
                )
                diag_block.assets.add(asset)
                total_svgs_attached += 1
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Curated Instructional YouTube Videos
        # ---------------------------------------------------------------------
        if u_order in YOUTUBE_VIDEOS:
            vid_def = YOUTUBE_VIDEOS[u_order]
            vid_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            if vid_block:
                v_content = vid_block.content or {}
                v_content["url"] = vid_def["url"]
                v_content["title"] = vid_def["title"]
                v_content["description"] = vid_def["description"]
                vid_block.content = v_content
                vid_block.title = vid_def["title"]
                vid_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    asset_type="youtube",
                    url=vid_def["url"],
                    defaults={
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "title": f"Lesson {u_order + 1} Video: {vid_def['title']}",
                        "description": vid_def["description"],
                        "metadata": {
                            "topic_order": 7,
                            "unit_order": u_order,
                            "youtube_url": vid_def["url"]
                        }
                    }
                )
                vid_block.assets.add(asset)
                total_videos_attached += 1
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] {vid_def['title']}")

    print("\n" + "=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 365 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic365()
