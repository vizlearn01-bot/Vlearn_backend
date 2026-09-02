"""
VLearn CBC Grade 10 English — Topic 2: Reading
Custom Responsive Vector SVGs for Lessons 1 to 10
"""

# =============================================================================
# SVG 1: Lesson 1 — Reading Fluency Triad & Prosody Matrix
# =============================================================================
SVG_LESSON_1_FLUENCY_TRIAD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l1HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#0D9488"/>
    </linearGradient>
    <linearGradient id="accGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <linearGradient id="rateGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="prosGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FAF5FF"/>
      <stop offset="100%" stop-color="#F3E8FF"/>
    </linearGradient>
    <filter id="l1Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Canvas -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l1HeaderGrad)" filter="url(#l1Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE THREE PILLARS OF READING FLUENCY</text>
  <text x="400" y="64" fill="#CCFBF1" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Accuracy + Rate (Pacing) + Expression (Prosody) = True Comprehension</text>

  <!-- 3 Pillars Grid -->
  <!-- 1. ACCURACY -->
  <g transform="translate(25, 100)" filter="url(#l1Shadow)">
    <rect width="235" height="330" rx="12" fill="url(#accGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="14" y="14" width="207" height="32" rx="8" fill="#059669"/>
    <text x="117" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. ACCURACY</text>
    
    <text x="117" y="68" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CORRECT WORD DECODING</text>
    
    <circle cx="117" cy="108" r="26" fill="#A7F3D0"/>
    <path d="M106 108 L114 116 L130 98" fill="none" stroke="#047857" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
    
    <rect x="14" y="148" width="207" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="24" y="168" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Core Mechanisms:</text>
    <text x="24" y="188" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Phonetic pronunciation</text>
    <text x="24" y="206" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Morphological decoding (prefixes/roots)</text>
    <text x="24" y="224" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Active self-correction of errors</text>
    
    <rect x="14" y="245" width="207" height="72" rx="6" fill="#064E3B"/>
    <text x="24" y="265" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Benchmark Target:</text>
    <text x="24" y="284" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">98%+ accuracy on grade-level</text>
    <text x="24" y="300" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">independent reading texts.</text>
  </g>

  <!-- 2. RATE (PACE) -->
  <g transform="translate(282, 100)" filter="url(#l1Shadow)">
    <rect width="235" height="330" rx="12" fill="url(#rateGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="14" y="14" width="207" height="32" rx="8" fill="#2563EB"/>
    <text x="117" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. RATE (PACE)</text>
    
    <text x="117" y="68" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CONVERSATIONAL SPEED</text>
    
    <circle cx="117" cy="108" r="26" fill="#BFDBFE"/>
    <circle cx="117" cy="108" r="18" fill="none" stroke="#1D4ED8" stroke-width="2.5"/>
    <path d="M117 96 L117 108 L126 114" fill="none" stroke="#1D4ED8" stroke-width="2.5" stroke-linecap="round"/>
    
    <rect x="14" y="148" width="207" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="24" y="168" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Core Mechanisms:</text>
    <text x="24" y="188" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Steady, natural tempo</text>
    <text x="24" y="206" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Avoiding robot/choppy reading</text>
    <text x="24" y="224" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Avoiding speed-racing without meaning</text>
    
    <rect x="14" y="245" width="207" height="72" rx="6" fill="#1E3A8A"/>
    <text x="24" y="265" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Benchmark Target:</text>
    <text x="24" y="284" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">130–160 words per minute (WPM)</text>
    <text x="24" y="300" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">oral conversational flow.</text>
  </g>

  <!-- 3. PROSODY (EXPRESSION) -->
  <g transform="translate(540, 100)" filter="url(#l1Shadow)">
    <rect width="235" height="330" rx="12" fill="url(#prosGrad)" stroke="#A855F7" stroke-width="2"/>
    <rect x="14" y="14" width="207" height="32" rx="8" fill="#9333EA"/>
    <text x="117" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. PROSODY</text>
    
    <text x="117" y="68" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">THE MUSIC OF LANGUAGE</text>
    
    <circle cx="117" cy="108" r="26" fill="#E9D5FF"/>
    <path d="M103 118 C108 100, 114 98, 117 114 C120 126, 126 120, 131 100" fill="none" stroke="#7E22CE" stroke-width="3" stroke-linecap="round"/>
    
    <rect x="14" y="148" width="207" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="24" y="168" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Core Mechanisms:</text>
    <text x="24" y="188" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Pitch inflection for ?, ! and .</text>
    <text x="24" y="206" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Punctuation pauses (commas/stops)</text>
    <text x="24" y="224" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Phrase chunking &amp; emotional stress</text>
    
    <rect x="14" y="245" width="207" height="72" rx="6" fill="#581C87"/>
    <text x="24" y="265" fill="#D8B4FE" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Benchmark Target:</text>
    <text x="24" y="284" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">Expressive phrasing matching</text>
    <text x="24" y="300" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">character emotion &amp; text tone.</text>
  </g>
</svg>"""


# =============================================================================
# SVG 2: Lesson 2 — Extensive vs. Intensive Reading & Stamina Ladder
# =============================================================================
SVG_LESSON_2_EXTENSIVE_READING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l2HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E40AF"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="intGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#FDE68A"/>
    </linearGradient>
    <linearGradient id="extGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#BFDBFE"/>
    </linearGradient>
    <filter id="l2Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l2HeaderGrad)" filter="url(#l2Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">INTENSIVE VS. EXTENSIVE READING &amp; STAMINA BUILDING</text>
  <text x="400" y="64" fill="#DBEAFE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Deep Linguistic Analysis vs. High-Volume Fluency &amp; Habit Formation</text>

  <!-- Left: Intensive Reading Card -->
  <g transform="translate(25, 95)" filter="url(#l2Shadow)">
    <rect width="365" height="195" rx="12" fill="url(#intGrad)" stroke="#F59E0B" stroke-width="2"/>
    <rect x="14" y="14" width="337" height="30" rx="6" fill="#D97706"/>
    <text x="182" y="34" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🔍 INTENSIVE READING (Micro-Focus)</text>
    
    <text x="24" y="65" fill="#78350F" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Goal: Grammatical precision, syntax &amp; vocabulary analysis</text>
    <text x="24" y="85" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Text Length: Short (1–3 paragraphs or excerpts)</text>
    <text x="24" y="103" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Difficulty: Challenging (at or above current reading level)</text>
    <text x="24" y="121" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Dictionary Use: Frequent lookup of unknown words</text>
    <text x="24" y="139" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Setting: Classroom lessons, close textual analysis</text>
    
    <rect x="14" y="152" width="337" height="30" rx="6" fill="#B45309"/>
    <text x="182" y="171" fill="#FEF3C7" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Key Rule: 100% Comprehension of every word &amp; structure</text>
  </g>

  <!-- Right: Extensive Reading Card -->
  <g transform="translate(410, 95)" filter="url(#l2Shadow)">
    <rect width="365" height="195" rx="12" fill="url(#extGrad)" stroke="#2563EB" stroke-width="2"/>
    <rect x="14" y="14" width="337" height="30" rx="6" fill="#1D4ED8"/>
    <text x="182" y="34" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">📖 EXTENSIVE READING (Macro-Volume)</text>
    
    <text x="24" y="65" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Goal: Reading fluency, stamina, joy &amp; global meaning</text>
    <text x="24" y="85" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Text Length: Long (novels, graded readers, magazines)</text>
    <text x="24" y="103" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Difficulty: Easy (The 95% Rule: understand 95%+ of words)</text>
    <text x="24" y="121" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Dictionary Use: Minimal (infer from context; keep moving)</text>
    <text x="24" y="139" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">• Setting: Independent reading, home reading log</text>
    
    <rect x="14" y="152" width="337" height="30" rx="6" fill="#1E40AF"/>
    <text x="182" y="171" fill="#DBEAFE" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Key Rule: Stop and change book if &gt;5 unknown words/page</text>
  </g>

  <!-- Bottom: Stamina Growth Ladder -->
  <g transform="translate(25, 305)" filter="url(#l2Shadow)">
    <rect width="750" height="135" rx="12" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
    <rect x="14" y="12" width="722" height="26" rx="6" fill="#059669"/>
    <text x="375" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4-WEEK READING STAMINA PROGRESSION LADDER</text>
    
    <g transform="translate(20, 50)">
      <!-- Step 1 -->
      <rect x="0" y="24" width="165" height="48" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="82" y="44" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">WEEK 1: Foundation</text>
      <text x="82" y="60" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">10 Mins / Day (3–5 pages)</text>

      <path d="M172 48 L188 48" stroke="#10B981" stroke-width="3" stroke-linecap="round"/>
      <polygon points="188,44 195,48 188,52" fill="#10B981"/>

      <!-- Step 2 -->
      <rect x="200" y="20" width="165" height="52" rx="8" fill="#D1FAE5" stroke="#10B981" stroke-width="1.5"/>
      <text x="282" y="42" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">WEEK 2: Building</text>
      <text x="282" y="58" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">20 Mins / Day (8–12 pages)</text>

      <path d="M372 48 L388 48" stroke="#10B981" stroke-width="3" stroke-linecap="round"/>
      <polygon points="388,44 395,48 388,52" fill="#10B981"/>

      <!-- Step 3 -->
      <rect x="400" y="14" width="165" height="58" rx="8" fill="#A7F3D0" stroke="#059669" stroke-width="1.5"/>
      <text x="482" y="38" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">WEEK 3: Expansion</text>
      <text x="482" y="54" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">30 Mins / Day (15–20 pages)</text>

      <path d="M572 48 L588 48" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
      <polygon points="588,44 595,48 588,52" fill="#059669"/>

      <!-- Step 4 -->
      <rect x="600" y="6" width="110" height="66" rx="8" fill="#059669"/>
      <text x="655" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">WEEK 4+</text>
      <text x="655" y="47" fill="#CCFBF1" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">45 Mins Focus</text>
      <text x="655" y="62" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Independent Reader</text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 3: Lesson 3 — Skimming vs. Scanning Dual Speed-Reading Pipeline
# =============================================================================
SVG_LESSON_3_SKIMMING_SCANNING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l3HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4338CA"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="skimGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EEF2FF"/>
      <stop offset="100%" stop-color="#E0E7FF"/>
    </linearGradient>
    <linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <filter id="l3Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l3HeaderGrad)" filter="url(#l3Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SPEED-READING STRATEGIES: SKIMMING VS. SCANNING</text>
  <text x="400" y="64" fill="#E0E7FF" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Top-Down Gist Extraction vs. Targeted Keyword &amp; Data Retrieval</text>

  <!-- Left: SKIMMING Column -->
  <g transform="translate(25, 95)" filter="url(#l3Shadow)">
    <rect width="365" height="340" rx="12" fill="url(#skimGrad)" stroke="#4F46E5" stroke-width="2"/>
    <rect x="14" y="14" width="337" height="34" rx="8" fill="#4338CA"/>
    <text x="182" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">🦅 SKIMMING (Reading for Gist)</text>
    
    <!-- Visual Representation of Skimming (Top-down sweep) -->
    <rect x="14" y="58" width="337" height="110" rx="8" fill="#FFFFFF"/>
    <text x="24" y="78" fill="#312E81" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Eye Movement: High-Level Horizontal Glides</text>
    
    <!-- Diagram of lines read -->
    <rect x="24" y="88" width="180" height="10" rx="3" fill="#4338CA"/>
    <text x="210" y="97" fill="#4338CA" font-family="system-ui, sans-serif" font-size="9" font-weight="700">← Title &amp; Headings</text>
    
    <rect x="24" y="104" width="300" height="7" rx="3" fill="#818CF8"/>
    <text x="210" y="121" fill="#4338CA" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600">← 1st Paragraph (Intro)</text>
    <rect x="24" y="114" width="260" height="7" rx="3" fill="#818CF8"/>
    
    <rect x="24" y="128" width="220" height="7" rx="3" fill="#C7D2FE"/>
    <text x="250" y="135" fill="#6B7280" font-family="system-ui, sans-serif" font-size="8">← Topic Sentences</text>
    
    <rect x="24" y="142" width="300" height="7" rx="3" fill="#818CF8"/>
    <text x="210" y="157" fill="#4338CA" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600">← Final Paragraph (Conclusion)</text>
    <rect x="24" y="152" width="240" height="7" rx="3" fill="#818CF8"/>

    <!-- Operational Rules -->
    <rect x="14" y="180" width="337" height="145" rx="8" fill="#312E81"/>
    <text x="24" y="202" fill="#A5B4FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Skimming Protocol:</text>
    <text x="24" y="222" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">1. Read title, subheadings, and bold text.</text>
    <text x="24" y="240" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">2. Read entire 1st and final paragraphs.</text>
    <text x="24" y="258" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">3. Read only 1st sentence of body paragraphs.</text>
    <text x="24" y="276" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">4. Ignore dates, statistics, and examples.</text>
    <text x="24" y="302" fill="#FDE047" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Speed: 400–800 words per minute</text>
  </g>

  <!-- Right: SCANNING Column -->
  <g transform="translate(410, 95)" filter="url(#l3Shadow)">
    <rect width="365" height="340" rx="12" fill="url(#scanGrad)" stroke="#DC2626" stroke-width="2"/>
    <rect x="14" y="14" width="337" height="34" rx="8" fill="#B91C1C"/>
    <text x="182" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">🎯 SCANNING (Reading for Specific Data)</text>
    
    <!-- Visual Representation of Scanning (Zigzag path) -->
    <rect x="14" y="58" width="337" height="110" rx="8" fill="#FFFFFF"/>
    <text x="24" y="78" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Eye Movement: Rapid Diagonal / Zigzag Search</text>
    
    <path d="M40 92 L300 108 L50 126 L280 142 L160 156" fill="none" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="4,4"/>
    <circle cx="160" cy="156" r="14" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>
    <text x="160" y="160" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">2026</text>
    <text x="185" y="160" fill="#DC2626" font-family="system-ui, sans-serif" font-size="9" font-weight="700">← Target Hit!</text>

    <!-- Operational Rules -->
    <rect x="14" y="180" width="337" height="145" rx="8" fill="#7F1D1D"/>
    <text x="24" y="202" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Scanning Protocol:</text>
    <text x="24" y="222" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">1. Formulate clear target clue (year, name, capital).</text>
    <text x="24" y="240" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">2. Move eyes rapidly in zigzag down the page.</text>
    <text x="24" y="258" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">3. Do NOT read sentences; search for clue shapes.</text>
    <text x="24" y="276" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">4. Stop immediately when target clue is spotted.</text>
    <text x="24" y="302" fill="#FDE047" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Goal: Locate exact answer in &lt;10 seconds</text>
  </g>
</svg>"""


# =============================================================================
# SVG 4: Lesson 4 — The 4 Patterns of Text Organization Architecture
# =============================================================================
SVG_LESSON_4_TEXT_ORGANIZATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l4HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <filter id="l4Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l4HeaderGrad)" filter="url(#l4Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE FOUR PATTERNS OF TEXT ORGANIZATION</text>
  <text x="400" y="64" fill="#CCFBF1" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Structural Blueprints, Transitional Signposts &amp; Visual Logic</text>

  <!-- 2x2 Matrix Grid -->

  <!-- Card 1: Chronological / Sequence -->
  <g transform="translate(25, 95)" filter="url(#l4Shadow)">
    <rect width="365" height="160" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <rect x="12" y="12" width="341" height="28" rx="6" fill="#1D4ED8"/>
    <text x="182" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">1. CHRONOLOGICAL (SEQUENCE)</text>
    
    <text x="20" y="58" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Function: Events ordered across time or step-by-step.</text>
    <text x="20" y="76" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#1D4ED8">Signposts:</tspan> First, next, then, after, subsequently, in 1963, finally.</text>
    
    <!-- Mini Graphic -->
    <rect x="20" y="88" width="325" height="34" rx="6" fill="#DBEAFE"/>
    <circle cx="50" cy="105" r="10" fill="#1D4ED8"/>
    <text x="50" y="109" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">1</text>
    <path d="M65 105 L115 105" stroke="#1D4ED8" stroke-width="2" stroke-linecap="round"/>
    <circle cx="130" cy="105" r="10" fill="#1D4ED8"/>
    <text x="130" y="109" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">2</text>
    <path d="M145 105 L195 105" stroke="#1D4ED8" stroke-width="2" stroke-linecap="round"/>
    <circle cx="210" cy="105" r="10" fill="#1D4ED8"/>
    <text x="210" y="109" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">3</text>
    <path d="M225 105 L275 105" stroke="#1D4ED8" stroke-width="2" stroke-linecap="round"/>
    <circle cx="290" cy="105" r="10" fill="#1D4ED8"/>
    <text x="290" y="109" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">4</text>
    
    <text x="20" y="142" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Example: Recipes, historical timelines, scientific procedures.</text>
  </g>

  <!-- Card 2: Cause & Effect -->
  <g transform="translate(410, 95)" filter="url(#l4Shadow)">
    <rect width="365" height="160" rx="12" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <rect x="12" y="12" width="341" height="28" rx="6" fill="#D97706"/>
    <text x="182" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">2. CAUSE AND EFFECT</text>
    
    <text x="20" y="58" fill="#92400E" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Function: Explains reasons why and resulting outcomes.</text>
    <text x="20" y="76" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#D97706">Signposts:</tspan> Because, since, as a result, consequently, therefore.</text>
    
    <!-- Mini Graphic -->
    <rect x="20" y="88" width="325" height="34" rx="6" fill="#FDE68A"/>
    <rect x="35" y="94" width="100" height="22" rx="4" fill="#B45309"/>
    <text x="85" y="109" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">CAUSE (Action)</text>
    
    <path d="M145 105 L185 105" stroke="#B45309" stroke-width="3" stroke-linecap="round"/>
    <polygon points="185,100 193,105 185,110" fill="#B45309"/>
    
    <rect x="200" y="94" width="120" height="22" rx="4" fill="#78350F"/>
    <text x="260" y="109" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">EFFECT (Result)</text>
    
    <text x="20" y="142" fill="#78350F" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Example: Climate change causing rising ocean temperatures.</text>
  </g>

  <!-- Card 3: Compare & Contrast -->
  <g transform="translate(25, 270)" filter="url(#l4Shadow)">
    <rect width="365" height="165" rx="12" fill="#FAF5FF" stroke="#A855F7" stroke-width="2"/>
    <rect x="12" y="12" width="341" height="28" rx="6" fill="#9333EA"/>
    <text x="182" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">3. COMPARE AND CONTRAST</text>
    
    <text x="20" y="58" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Function: Highlights similarities and differences.</text>
    <text x="20" y="76" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#9333EA">Signposts:</tspan> Similarly, likewise, unlike, however, whereas, in contrast.</text>
    
    <!-- Mini Graphic: Venn Diagram -->
    <rect x="20" y="88" width="325" height="40" rx="6" fill="#F3E8FF"/>
    <circle cx="130" cy="108" r="16" fill="#C084FC" fill-opacity="0.6"/>
    <text x="110" y="112" fill="#581C87" font-size="8" font-weight="700">Item A</text>
    
    <circle cx="160" cy="108" r="16" fill="#A855F7" fill-opacity="0.6"/>
    <text x="180" y="112" fill="#581C87" font-size="8" font-weight="700">Item B</text>
    <text x="145" y="112" fill="#3B0764" font-size="7.5" font-weight="800">Overlap</text>
    
    <text x="20" y="148" fill="#581C87" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Example: Comparing cheetah vs. leopard physical adaptations.</text>
  </g>

  <!-- Card 4: Problem & Solution -->
  <g transform="translate(410, 270)" filter="url(#l4Shadow)">
    <rect width="365" height="165" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <rect x="12" y="12" width="341" height="28" rx="6" fill="#059669"/>
    <text x="182" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">4. PROBLEM AND SOLUTION</text>
    
    <text x="20" y="58" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Function: Poses an issue/challenge and provides resolutions.</text>
    <text x="20" y="76" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700" fill="#059669">Signposts:</tspan> The dilemma, challenge, to resolve this, one solution is.</text>
    
    <!-- Mini Graphic -->
    <rect x="20" y="88" width="325" height="40" rx="6" fill="#D1FAE5"/>
    <rect x="35" y="96" width="105" height="24" rx="4" fill="#DC2626"/>
    <text x="87" y="112" fill="#FFFFFF" font-size="8.5" font-weight="700" text-anchor="middle">⚠️ PROBLEM</text>
    
    <path d="M150 108 L180 108" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
    <polygon points="180,103 188,108 180,113" fill="#059669"/>
    
    <rect x="195" y="96" width="130" height="24" rx="4" fill="#059669"/>
    <text x="260" y="112" fill="#FFFFFF" font-size="8.5" font-weight="700" text-anchor="middle">💡 SOLUTION</text>
    
    <text x="20" y="148" fill="#064E3B" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Example: Deforestation crisis solved by planting 15B trees.</text>
  </g>
</svg>"""


# =============================================================================
# SVG 5: Lesson 5 — Inference & Conclusion Deduction Logic Matrix
# =============================================================================
SVG_LESSON_5_INFERENCE_LOGIC = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l5HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="formulaGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="50%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#ECFDF5"/>
    </linearGradient>
    <filter id="l5Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l5HeaderGrad)" filter="url(#l5Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">INFERENCE &amp; CONCLUSION LOGIC FRAMEWORK</text>
  <text x="400" y="64" fill="#DBEAFE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">The Scientific Formula for Reading Between the Lines</text>

  <!-- The Master Inference Formula Banner -->
  <g transform="translate(25, 95)" filter="url(#l5Shadow)">
    <rect width="750" height="110" rx="12" fill="url(#formulaGrad)" stroke="#3B82F6" stroke-width="2"/>
    <text x="375" y="26" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE CORE INFERENCE FORMULA</text>
    
    <!-- Box 1: Text Clues -->
    <rect x="20" y="40" width="185" height="55" rx="8" fill="#2563EB"/>
    <text x="112" y="62" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">TEXT CLUES</text>
    <text x="112" y="80" fill="#DBEAFE" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Explicit facts on the page</text>

    <!-- Symbol + -->
    <text x="228" y="75" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="28" font-weight="900" text-anchor="middle">+</text>

    <!-- Box 2: Background Schema -->
    <rect x="250" y="40" width="200" height="55" rx="8" fill="#D97706"/>
    <text x="350" y="62" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BACKGROUND SCHEMA</text>
    <text x="350" y="80" fill="#FEF3C7" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Prior knowledge &amp; real-world logic</text>

    <!-- Symbol = -->
    <text x="475" y="75" fill="#065F46" font-family="system-ui, sans-serif" font-size="28" font-weight="900" text-anchor="middle">=</text>

    <!-- Box 3: Valid Inference -->
    <rect x="500" y="40" width="230" height="55" rx="8" fill="#059669"/>
    <text x="615" y="62" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">JUSTIFIED INFERENCE</text>
    <text x="615" y="80" fill="#D1FAE5" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Logically proven deduction</text>
  </g>

  <!-- Bottom 3-Level Comprehension Matrix -->
  <g transform="translate(25, 220)" filter="url(#l5Shadow)">
    <rect width="750" height="215" rx="12" fill="#FFFFFF" stroke="#0F172A" stroke-width="1.5"/>
    <rect x="12" y="12" width="726" height="26" rx="6" fill="#0F172A"/>
    <text x="375" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">THREE LEVELS OF READING COMPREHENSION</text>

    <!-- Level 1: Literal -->
    <g transform="translate(20, 50)">
      <rect width="220" height="145" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
      <rect x="10" y="10" width="200" height="24" rx="4" fill="#2563EB"/>
      <text x="110" y="26" fill="#FFFFFF" font-size="11" font-weight="700" text-anchor="middle">LEVEL 1: LITERAL</text>
      
      <text x="14" y="52" fill="#1E40AF" font-size="10" font-weight="700">"On the Lines"</text>
      <text x="14" y="70" fill="#374151" font-size="9.5">• What the author stated directly</text>
      <text x="14" y="88" fill="#374151" font-size="9.5">• Who, what, when, where</text>
      <text x="14" y="106" fill="#374151" font-size="9.5">• 100% directly found on page</text>
      <text x="14" y="128" fill="#1E3A8A" font-size="9" font-style="italic">Ex: "Juma ran to the locked gate."</text>
    </g>

    <!-- Level 2: Inferential -->
    <g transform="translate(265, 50)">
      <rect width="220" height="145" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="10" y="10" width="200" height="24" rx="4" fill="#D97706"/>
      <text x="110" y="26" fill="#FFFFFF" font-size="11" font-weight="700" text-anchor="middle">LEVEL 2: INFERENTIAL</text>
      
      <text x="14" y="52" fill="#92400E" font-size="10" font-weight="700">"Between the Lines"</text>
      <text x="14" y="70" fill="#374151" font-size="9.5">• Implied meaning from clues</text>
      <text x="14" y="88" fill="#374151" font-size="9.5">• Why, how, character feelings</text>
      <text x="14" y="106" fill="#374151" font-size="9.5">• Backed by textual evidence</text>
      <text x="14" y="128" fill="#78350F" font-size="9" font-style="italic">Ex: "Juma is late and classes began."</text>
    </g>

    <!-- Level 3: Evaluative -->
    <g transform="translate(510, 50)">
      <rect width="220" height="145" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <rect x="10" y="10" width="200" height="24" rx="4" fill="#059669"/>
      <text x="110" y="26" fill="#FFFFFF" font-size="11" font-weight="700" text-anchor="middle">LEVEL 3: EVALUATIVE</text>
      
      <text x="14" y="52" fill="#065F46" font-size="10" font-weight="700">"Beyond the Lines"</text>
      <text x="14" y="70" fill="#374151" font-size="9.5">• Judging author's claims &amp; morals</text>
      <text x="14" y="88" fill="#374151" font-size="9.5">• Synthesizing big-picture truth</text>
      <text x="14" y="106" fill="#374151" font-size="9.5">• Forming personal stance</text>
      <text x="14" y="128" fill="#064E3B" font-size="9" font-style="italic">Ex: "Punctuality affects performance."</text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 6: Lesson 6 — S.A.D.E. Context Clues & Collocation Architecture
# =============================================================================
SVG_LESSON_6_VOCABULARY_CONTEXT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l6HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>
    <filter id="l6Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l6HeaderGrad)" filter="url(#l6Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">S.A.D.E. CONTEXT CLUES &amp; COLLOCATION ARCHITECTURE</text>
  <text x="400" y="64" fill="#D1FAE5" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Four Detective Clue Types + Natural Word Partnerships</text>

  <!-- Top: S.A.D.E. 4-Box Grid -->
  <g transform="translate(25, 95)" filter="url(#l6Shadow)">
    <!-- 1. Synonym -->
    <g transform="translate(0, 0)">
      <rect width="175" height="175" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <rect x="10" y="10" width="155" height="26" rx="6" fill="#2563EB"/>
      <text x="87" y="27" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">S - SYNONYM</text>
      
      <text x="14" y="54" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Restatement:</text>
      <text x="14" y="70" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Uses similar word nearby.</text>
      <text x="14" y="86" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Marker: "also known as", "or".</text>
      
      <rect x="10" y="100" width="155" height="65" rx="4" fill="#DBEAFE"/>
      <text x="14" y="116" fill="#1E3A8A" font-size="8.5" font-weight="700">Model:</text>
      <text x="14" y="130" fill="#1E3A8A" font-size="8">"The explanation was <tspan font-weight="700">lucid</tspan>;</text>
      <text x="14" y="144" fill="#1E3A8A" font-size="8">it was so <tspan font-weight="700">clear</tspan> that all</text>
      <text x="14" y="158" fill="#1E3A8A" font-size="8">students understood."</text>
    </g>

    <!-- 2. Antonym -->
    <g transform="translate(191, 0)">
      <rect width="175" height="175" rx="10" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <rect x="10" y="10" width="155" height="26" rx="6" fill="#D97706"/>
      <text x="87" y="27" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">A - ANTONYM</text>
      
      <text x="14" y="54" fill="#92400E" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Contrast:</text>
      <text x="14" y="70" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Contrasts with opposite word.</text>
      <text x="14" y="86" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Marker: "unlike", "however".</text>
      
      <rect x="10" y="100" width="155" height="65" rx="4" fill="#FDE68A"/>
      <text x="14" y="116" fill="#78350F" font-size="8.5" font-weight="700">Model:</text>
      <text x="14" y="130" fill="#78350F" font-size="8">"Unlike his <tspan font-weight="700">talkative</tspan> peer,</text>
      <text x="14" y="144" fill="#78350F" font-size="8">Juma was <tspan font-weight="700">taciturn</tspan> and</text>
      <text x="14" y="158" fill="#78350F" font-size="8">spoke very few words."</text>
    </g>

    <!-- 3. Definition -->
    <g transform="translate(382, 0)">
      <rect width="175" height="175" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <rect x="10" y="10" width="155" height="26" rx="6" fill="#059669"/>
      <text x="87" y="27" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">D - DEFINITION</text>
      
      <text x="14" y="54" fill="#065F46" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Direct Meaning:</text>
      <text x="14" y="70" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Stated right in sentence.</text>
      <text x="14" y="86" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Marker: "is defined as", commas.</text>
      
      <rect x="10" y="100" width="155" height="65" rx="4" fill="#A7F3D0"/>
      <text x="14" y="116" fill="#064E3B" font-size="8.5" font-weight="700">Model:</text>
      <text x="14" y="130" fill="#064E3B" font-size="8">"A <tspan font-weight="700">dermatologist</tspan>, or</text>
      <text x="14" y="144" fill="#064E3B" font-size="8"><tspan font-weight="700">medical skin doctor</tspan>,</text>
      <text x="14" y="158" fill="#064E3B" font-size="8">prescribed the cream."</text>
    </g>

    <!-- 4. Example -->
    <g transform="translate(575, 0)">
      <rect width="175" height="175" rx="10" fill="#FAF5FF" stroke="#A855F7" stroke-width="2"/>
      <rect x="10" y="10" width="155" height="26" rx="6" fill="#9333EA"/>
      <text x="87" y="27" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">E - EXAMPLE</text>
      
      <text x="14" y="54" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Illustrations:</text>
      <text x="14" y="70" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Concrete items listed.</text>
      <text x="14" y="86" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Marker: "such as", "for instance".</text>
      
      <rect x="10" y="100" width="155" height="65" rx="4" fill="#E9D5FF"/>
      <text x="14" y="116" fill="#581C87" font-size="8.5" font-weight="700">Model:</text>
      <text x="14" y="130" fill="#581C87" font-size="8">"The forest had <tspan font-weight="700">conifers</tspan>,</text>
      <text x="14" y="144" fill="#581C87" font-size="8">such as <tspan font-weight="700">pines, firs,</tspan></text>
      <text x="14" y="158" fill="#581C87" font-size="8">and cedar trees."</text>
    </g>
  </g>

  <!-- Bottom: Collocation Partnerships Card -->
  <g transform="translate(25, 285)" filter="url(#l6Shadow)">
    <rect width="750" height="155" rx="12" fill="#FFFFFF" stroke="#047857" stroke-width="2"/>
    <rect x="12" y="10" width="726" height="26" rx="6" fill="#047857"/>
    <text x="375" y="27" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">COLLOCATIONS: WORDS THAT NATURALLY PARTNER TOGETHER</text>
    
    <g transform="translate(20, 45)">
      <!-- Collocation 1 -->
      <rect x="0" y="0" width="225" height="95" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1"/>
      <text x="112" y="18" fill="#065F46" font-size="10.5" font-weight="700" text-anchor="middle">Verb + Noun</text>
      <text x="10" y="38" fill="#065F46" font-size="9.5">✓ <tspan font-weight="700">make a mistake</tspan> (not "do")</text>
      <text x="10" y="56" fill="#065F46" font-size="9.5">✓ <tspan font-weight="700">commit a crime</tspan> (not "make")</text>
      <text x="10" y="74" fill="#065F46" font-size="9.5">✓ <tspan font-weight="700">take a risk</tspan> (not "do")</text>

      <!-- Collocation 2 -->
      <rect x="245" y="0" width="225" height="95" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1"/>
      <text x="357" y="18" fill="#1E40AF" font-size="10.5" font-weight="700" text-anchor="middle">Adjective + Noun</text>
      <text x="255" y="38" fill="#1E40AF" font-size="9.5">✓ <tspan font-weight="700">bitter disappointment</tspan></text>
      <text x="255" y="56" fill="#1E40AF" font-size="9.5">✓ <tspan font-weight="700">heavy rain</tspan> (not "thick")</text>
      <text x="255" y="74" fill="#1E40AF" font-size="9.5">✓ <tspan font-weight="700">excruciating pain</tspan></text>

      <!-- Collocation 3 -->
      <rect x="490" y="0" width="220" height="95" rx="8" fill="#FAF5FF" stroke="#A855F7" stroke-width="1"/>
      <text x="600" y="18" fill="#6B21A8" font-size="10.5" font-weight="700" text-anchor="middle">Adverb + Adjective</text>
      <text x="500" y="38" fill="#6B21A8" font-size="9.5">✓ <tspan font-weight="700">deeply concerned</tspan></text>
      <text x="500" y="56" fill="#6B21A8" font-size="9.5">✓ <tspan font-weight="700">strictly prohibited</tspan></text>
      <text x="500" y="74" fill="#6B21A8" font-size="9.5">✓ <tspan font-weight="700">highly recommended</tspan></text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 7: Lesson 7 — SQ4R Active Study Method 6-Phase Cycle
# =============================================================================
SVG_LESSON_7_SQ4R_METHOD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l7HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#2563EB"/>
    </linearGradient>
    <filter id="l7Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l7HeaderGrad)" filter="url(#l7Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE SQ4R ACTIVE STUDY &amp; NOTE-MAKING SYSTEM</text>
  <text x="400" y="64" fill="#DBEAFE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Survey → Question → Read → Reflect → Recite → Review</text>

  <!-- 6 Step Hexagonal Flow Layout -->
  <g transform="translate(25, 95)" filter="url(#l7Shadow)">
    
    <!-- Step 1: SURVEY -->
    <g transform="translate(0, 0)">
      <rect width="235" height="155" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <rect x="10" y="10" width="215" height="28" rx="6" fill="#2563EB"/>
      <text x="117" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. S - SURVEY</text>
      
      <text x="16" y="56" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Preview Structure (2-3 Mins):</text>
      <text x="16" y="74" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Skim titles, headings, summaries</text>
      <text x="16" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Inspect diagrams, charts &amp; maps</text>
      <text x="16" y="106" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Activate brain roadmap</text>
      <rect x="10" y="118" width="215" height="24" rx="4" fill="#DBEAFE"/>
      <text x="117" y="134" fill="#1E3A8A" font-size="8.5" font-weight="600" text-anchor="middle">Goal: High-level overview</text>
    </g>

    <!-- Step 2: QUESTION -->
    <g transform="translate(257, 0)">
      <rect width="235" height="155" rx="10" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <rect x="10" y="10" width="215" height="28" rx="6" fill="#D97706"/>
      <text x="117" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. Q - QUESTION</text>
      
      <text x="16" y="56" fill="#92400E" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Turn Headings into Inquiries:</text>
      <text x="16" y="74" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• "Causes of Erosion" →</text>
      <text x="16" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="9">  "What causes soil erosion?"</text>
      <text x="16" y="106" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Creates target for the eyes</text>
      <rect x="10" y="118" width="215" height="24" rx="4" fill="#FDE68A"/>
      <text x="117" y="134" fill="#78350F" font-size="8.5" font-weight="600" text-anchor="middle">Goal: Purposeful curiosity</text>
    </g>

    <!-- Step 3: READ -->
    <g transform="translate(515, 0)">
      <rect width="235" height="155" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <rect x="10" y="10" width="215" height="28" rx="6" fill="#059669"/>
      <text x="117" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. R1 - READ</text>
      
      <text x="16" y="56" fill="#065F46" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Targeted Active Search:</text>
      <text x="16" y="74" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Read specifically to answer Q</text>
      <text x="16" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Ignore irrelevant trivia</text>
      <text x="16" y="106" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Highlight max 10% of text</text>
      <rect x="10" y="118" width="215" height="24" rx="4" fill="#A7F3D0"/>
      <text x="117" y="134" fill="#064E3B" font-size="8.5" font-weight="600" text-anchor="middle">Goal: Extract answers</text>
    </g>

    <!-- Step 4: REFLECT -->
    <g transform="translate(0, 175)">
      <rect width="235" height="155" rx="10" fill="#FAF5FF" stroke="#A855F7" stroke-width="2"/>
      <rect x="10" y="10" width="215" height="28" rx="6" fill="#9333EA"/>
      <text x="117" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. R2 - REFLECT</text>
      
      <text x="16" y="56" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Synthesize &amp; Connect:</text>
      <text x="16" y="74" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Link new info to prior knowledge</text>
      <text x="16" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• "How does this apply to Kenya?"</text>
      <text x="16" y="106" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Construct mental models</text>
      <rect x="10" y="118" width="215" height="24" rx="4" fill="#E9D5FF"/>
      <text x="117" y="134" fill="#581C87" font-size="8.5" font-weight="600" text-anchor="middle">Goal: Deep cognitive meaning</text>
    </g>

    <!-- Step 5: RECITE -->
    <g transform="translate(257, 175)">
      <rect width="235" height="155" rx="10" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
      <rect x="10" y="10" width="215" height="28" rx="6" fill="#DC2626"/>
      <text x="117" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">5. R3 - RECITE</text>
      
      <text x="16" y="56" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Close Book &amp; Verbalize:</text>
      <text x="16" y="74" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• State answer in your own words</text>
      <text x="16" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Write summary in 2-column chart</text>
      <text x="16" y="106" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• 300% boost in retention</text>
      <rect x="10" y="118" width="215" height="24" rx="4" fill="#FECACA"/>
      <text x="117" y="134" fill="#7F1D1D" font-size="8.5" font-weight="600" text-anchor="middle">Goal: Working memory lock</text>
    </g>

    <!-- Step 6: REVIEW -->
    <g transform="translate(515, 175)">
      <rect width="235" height="155" rx="10" fill="#F0FDF4" stroke="#22C55E" stroke-width="2"/>
      <rect x="10" y="10" width="215" height="28" rx="6" fill="#16A34A"/>
      <text x="117" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">6. R4 - REVIEW</text>
      
      <text x="16" y="56" fill="#14532D" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Spaced Self-Testing:</text>
      <text x="16" y="74" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Review 2-column notes weekly</text>
      <text x="16" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Cover right column; re-answer Qs</text>
      <text x="16" y="106" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Long-term exam mastery</text>
      <rect x="10" y="118" width="215" height="24" rx="4" fill="#BBF7D0"/>
      <text x="117" y="134" fill="#14532D" font-size="8.5" font-weight="600" text-anchor="middle">Goal: Permanent long-term memory</text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 8: Lesson 8 — The Critical Reading Quad: Purpose, Audience, Attitude, Argument
# =============================================================================
SVG_LESSON_8_CRITICAL_READING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l8HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4C1D95"/>
      <stop offset="100%" stop-color="#7C3AED"/>
    </linearGradient>
    <filter id="l8Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l8HeaderGrad)" filter="url(#l8Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE CRITICAL READING QUADRANT</text>
  <text x="400" y="64" fill="#EDE9FE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Analyzing Purpose, Audience, Attitude (Tone) &amp; Argument Rigor</text>

  <!-- 4 Quadrants Grid -->
  <g transform="translate(25, 95)" filter="url(#l8Shadow)">
    
    <!-- Quad 1: PURPOSE -->
    <g transform="translate(0, 0)">
      <rect width="365" height="160" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
      <rect x="12" y="10" width="341" height="28" rx="6" fill="#2563EB"/>
      <text x="182" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">🎯 1. AUTHOR'S PURPOSE</text>
      
      <text x="20" y="58" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Why was this written?</text>
      <text x="20" y="78" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">To Inform:</tspan> Objective data, news, historical records.</text>
      <text x="20" y="96" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">To Persuade:</tspan> Editorials, advertisements, political speeches.</text>
      <text x="20" y="114" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">To Entertain / Warn:</tspan> Creative fiction, safety advisories.</text>
      <text x="20" y="140" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Always ask: "Does the author profit or gain power from this?"</text>
    </g>

    <!-- Quad 2: AUDIENCE -->
    <g transform="translate(385, 0)">
      <rect width="365" height="160" rx="10" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
      <rect x="12" y="10" width="341" height="28" rx="6" fill="#D97706"/>
      <text x="182" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">👥 2. TARGET AUDIENCE</text>
      
      <text x="20" y="58" fill="#92400E" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Who is the intended reader?</text>
      <text x="20" y="78" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Demographics:</tspan> Secondary students, voters, scientists, parents.</text>
      <text x="20" y="96" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Register &amp; Tone:</tspan> Formal academic vs. informal slang.</text>
      <text x="20" y="114" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Assumed Knowledge:</tspan> Introductory vs. highly specialized.</text>
      <text x="20" y="140" fill="#B45309" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Always ask: "How does the audience shape vocabulary choices?"</text>
    </g>

    <!-- Quad 3: ATTITUDE (TONE & CONNOTATION) -->
    <g transform="translate(0, 175)">
      <rect width="365" height="160" rx="10" fill="#FAF5FF" stroke="#A855F7" stroke-width="2"/>
      <rect x="12" y="10" width="341" height="28" rx="6" fill="#9333EA"/>
      <text x="182" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">🎭 3. ATTITUDE &amp; CONNOTATION</text>
      
      <text x="20" y="58" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">What is the author's emotional stance?</text>
      <text x="20" y="78" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Tone Spectrum:</tspan> Critical, laudatory, sarcastic, objective, urgent.</text>
      <text x="20" y="96" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Denotation:</tspan> Literal dictionary definition ("slender").</text>
      <text x="20" y="114" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Connotation:</tspan> Emotional weight ("skinny" vs. "graceful").</text>
      <text x="20" y="140" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Loaded adjectives reveal unspoken author bias.</text>
    </g>

    <!-- Quad 4: ARGUMENT & EVIDENCE -->
    <g transform="translate(385, 175)">
      <rect width="365" height="160" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <rect x="12" y="10" width="341" height="28" rx="6" fill="#059669"/>
      <text x="182" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">⚖️ 4. ARGUMENT RIGOR</text>
      
      <text x="20" y="58" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Is the claim logically justified?</text>
      <text x="20" y="78" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Strong Evidence:</tspan> Peer-reviewed data, statistics, verified tests.</text>
      <text x="20" y="96" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Weak Evidence:</tspan> Anecdotes, emotional appeals, ad hominem.</text>
      <text x="20" y="114" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Omissions:</tspan> Ignoring counter-arguments to present a false case.</text>
      <text x="20" y="140" fill="#065F46" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Separate charismatic delivery from verifiable facts.</text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 9: Lesson 9 — The C.R.A.P. Source Evaluation Test & Reference Tools
# =============================================================================
SVG_LESSON_9_REFERENCE_RESEARCH = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l9HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E7490"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="l9Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l9HeaderGrad)" filter="url(#l9Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">RESEARCH EVALUATION &amp; REFERENCE MATERIALS</text>
  <text x="400" y="64" fill="#CFFAFE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">The C.R.A.P. Reliability Test + Reference Tools Typology + Citation Rules</text>

  <!-- Left: The C.R.A.P. Test (4 Pillars) -->
  <g transform="translate(25, 95)" filter="url(#l9Shadow)">
    <rect width="450" height="340" rx="12" fill="#FFFFFF" stroke="#0891B2" stroke-width="2"/>
    <rect x="14" y="12" width="422" height="28" rx="6" fill="#0891B2"/>
    <text x="225" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE C.R.A.P. TEST FOR SOURCE EVALUATION</text>
    
    <!-- C - Currency -->
    <g transform="translate(14, 48)">
      <rect width="422" height="60" rx="6" fill="#ECFEFF" stroke="#06B6D4" stroke-width="1"/>
      <circle cx="30" cy="30" r="18" fill="#0891B2"/>
      <text x="30" y="36" fill="#FFFFFF" font-size="14" font-weight="800" text-anchor="middle">C</text>
      <text x="60" y="24" fill="#164E63" font-size="11" font-weight="700">CURRENCY (Timeliness)</text>
      <text x="60" y="40" fill="#374151" font-size="9.5">• When was the information published or updated?</text>
      <text x="60" y="54" fill="#374151" font-size="9.5">• Are links and citations still active and current?</text>
    </g>

    <!-- R - Reliability -->
    <g transform="translate(14, 116)">
      <rect width="422" height="60" rx="6" fill="#F0FDF4" stroke="#22C55E" stroke-width="1"/>
      <circle cx="30" cy="30" r="18" fill="#16A34A"/>
      <text x="30" y="36" fill="#FFFFFF" font-size="14" font-weight="800" text-anchor="middle">R</text>
      <text x="60" y="24" fill="#14532D" font-size="11" font-weight="700">RELIABILITY (Evidence &amp; Accuracy)</text>
      <text x="60" y="40" fill="#374151" font-size="9.5">• Is the claim supported by peer-reviewed data?</text>
      <text x="60" y="54" fill="#374151" font-size="9.5">• Can details be cross-checked in external verified databases?</text>
    </g>

    <!-- A - Authority -->
    <g transform="translate(14, 184)">
      <rect width="422" height="60" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1"/>
      <circle cx="30" cy="30" r="18" fill="#2563EB"/>
      <text x="30" y="36" fill="#FFFFFF" font-size="14" font-weight="800" text-anchor="middle">A</text>
      <text x="60" y="24" fill="#1E40AF" font-size="11" font-weight="700">AUTHORITY (Creator Credentials)</text>
      <text x="60" y="40" fill="#374151" font-size="9.5">• Who wrote this? (Scholar, university, WHO, government)?</text>
      <text x="60" y="54" fill="#374151" font-size="9.5">• Is it an anonymous blog post or commercial ad?</text>
    </g>

    <!-- P - Purpose -->
    <g transform="translate(14, 252)">
      <rect width="422" height="60" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>
      <circle cx="30" cy="30" r="18" fill="#D97706"/>
      <text x="30" y="36" fill="#FFFFFF" font-size="14" font-weight="800" text-anchor="middle">P</text>
      <text x="60" y="24" fill="#92400E" font-size="11" font-weight="700">PURPOSE (Objective vs. Commercial Bias)</text>
      <text x="60" y="40" fill="#374151" font-size="9.5">• Is the goal to educate objectively or sell a product?</text>
      <text x="60" y="54" fill="#374151" font-size="9.5">• Does the creator disclose conflicts of interest?</text>
    </g>
  </g>

  <!-- Right: Reference Material Typology -->
  <g transform="translate(490, 95)" filter="url(#l9Shadow)">
    <rect width="285" height="340" rx="12" fill="#FFFFFF" stroke="#0E7490" stroke-width="2"/>
    <rect x="12" y="12" width="261" height="28" rx="6" fill="#0E7490"/>
    <text x="142" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">REFERENCE TOOLS MATRIX</text>
    
    <g transform="translate(12, 48)">
      <!-- 1. Dictionary -->
      <rect x="0" y="0" width="261" height="58" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <text x="10" y="18" fill="#0F172A" font-size="10.5" font-weight="700">📖 DICTIONARY</text>
      <text x="10" y="34" fill="#475569" font-size="9">• Definitions, spelling, pronunciation</text>
      <text x="10" y="48" fill="#475569" font-size="9">• Etymology, parts of speech</text>

      <!-- 2. Encyclopedia -->
      <rect x="0" y="65" width="261" height="58" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <text x="10" y="83" fill="#0F172A" font-size="10.5" font-weight="700">📚 ENCYCLOPEDIA</text>
      <text x="10" y="99" fill="#475569" font-size="9">• Comprehensive thematic overviews</text>
      <text x="10" y="113" fill="#475569" font-size="9">• History, science, biographic entries</text>

      <!-- 3. Atlas -->
      <rect x="0" y="130" width="261" height="58" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <text x="10" y="148" fill="#0F172A" font-size="10.5" font-weight="700">🗺️ ATLAS</text>
      <text x="10" y="164" fill="#475569" font-size="9">• Geographic maps, boundaries, cities</text>
      <text x="10" y="178" fill="#475569" font-size="9">• Physical topography &amp; coordinates</text>

      <!-- 4. Almanac -->
      <rect x="0" y="195" width="261" height="80" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <text x="10" y="213" fill="#0F172A" font-size="10.5" font-weight="700">📊 ALMANAC</text>
      <text x="10" y="229" fill="#475569" font-size="9">• Annual statistical calendars</text>
      <text x="10" y="243" fill="#475569" font-size="9">• Climate, crop yields, annual records</text>
      <text x="10" y="262" fill="#0E7490" font-size="8.5" font-weight="700">Rule: Always Cite Sources (APA/MLA)</text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 10: Lesson 10 — Synthesis Matrix & Multi-Source Argument Pipeline
# =============================================================================
SVG_LESSON_10_SYNTHESIS_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l10HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#4338CA"/>
    </linearGradient>
    <filter id="l10Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l10HeaderGrad)" filter="url(#l10Shadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">READING-TO-RESPONSE: SYNTHESIS MATRIX PIPELINE</text>
  <text x="400" y="64" fill="#E0E7FF" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Transforming Multiple Independent Sources into a Unified Thematic Argument</text>

  <!-- Left: Multi-Source Synthesis Matrix Table -->
  <g transform="translate(25, 95)" filter="url(#l10Shadow)">
    <rect width="450" height="340" rx="12" fill="#FFFFFF" stroke="#4338CA" stroke-width="2"/>
    <rect x="12" y="12" width="426" height="28" rx="6" fill="#4338CA"/>
    <text x="225" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THEMATIC SYNTHESIS MATRIX</text>
    
    <!-- Table Header -->
    <rect x="12" y="46" width="105" height="24" rx="3" fill="#EEF2FF"/>
    <text x="64" y="62" fill="#312E81" font-size="9.5" font-weight="700" text-anchor="middle">Core Theme</text>

    <rect x="120" y="46" width="105" height="24" rx="3" fill="#EEF2FF"/>
    <text x="172" y="62" fill="#312E81" font-size="9.5" font-weight="700" text-anchor="middle">Source A (Article)</text>

    <rect x="228" y="46" width="105" height="24" rx="3" fill="#EEF2FF"/>
    <text x="280" y="62" fill="#312E81" font-size="9.5" font-weight="700" text-anchor="middle">Source B (Data)</text>

    <rect x="336" y="46" width="102" height="24" rx="3" fill="#EEF2FF"/>
    <text x="387" y="62" fill="#312E81" font-size="9.5" font-weight="700" text-anchor="middle">Source C (Voice)</text>

    <!-- Row 1: Environmental Impact -->
    <rect x="12" y="74" width="105" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="64" y="104" fill="#0F172A" font-size="9" font-weight="700" text-anchor="middle">1. Environment</text>
    <text x="64" y="120" fill="#0F172A" font-size="9" font-weight="700" text-anchor="middle">&amp; Ecosystem</text>

    <rect x="120" y="74" width="105" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="125" y="92" fill="#334155" font-size="8">Plastic pollution</text>
    <text x="125" y="106" fill="#334155" font-size="8">harms marine</text>
    <text x="125" y="120" fill="#334155" font-size="8">life &amp; wildlife.</text>

    <rect x="228" y="74" width="105" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="233" y="92" fill="#334155" font-size="8">80% of single-use</text>
    <text x="233" y="106" fill="#334155" font-size="8">bottles end in</text>
    <text x="233" y="120" fill="#334155" font-size="8">local landfills.</text>

    <rect x="336" y="74" width="102" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="341" y="92" fill="#334155" font-size="8">Community waste</text>
    <text x="341" y="106" fill="#334155" font-size="8">clean-up costs</text>
    <text x="341" y="120" fill="#334155" font-size="8">escalate yearly.</text>

    <!-- Row 2: Financial & Practical -->
    <rect x="12" y="153" width="105" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="64" y="183" fill="#0F172A" font-size="9" font-weight="700" text-anchor="middle">2. Economic</text>
    <text x="64" y="199" fill="#0F172A" font-size="9" font-weight="700" text-anchor="middle">&amp; Health</text>

    <rect x="120" y="153" width="105" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="125" y="171" fill="#334155" font-size="8">Bottled water</text>
    <text x="125" y="185" fill="#334155" font-size="8">imposes high</text>
    <text x="125" y="199" fill="#334155" font-size="8">family expense.</text>

    <rect x="228" y="153" width="105" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="233" y="171" fill="#334155" font-size="8">Saving Ksh 500/</text>
    <text x="233" y="185" fill="#334155" font-size="8">wk with reusable</text>
    <text x="233" y="199" fill="#334155" font-size="8">metal containers.</text>

    <rect x="336" y="153" width="102" height="75" rx="3" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="341" y="171" fill="#334155" font-size="8">Hydration is vital</text>
    <text x="341" y="185" fill="#334155" font-size="8">for student focus</text>
    <text x="341" y="199" fill="#334155" font-size="8">and energy.</text>

    <!-- Synthesis Summary Box -->
    <rect x="12" y="234" width="426" height="92" rx="6" fill="#EEF2FF"/>
    <text x="20" y="252" fill="#312E81" font-size="9.5" font-weight="700">Synthesized Argument Statement:</text>
    <text x="20" y="270" fill="#1E1B4B" font-size="8.5" font-style="italic">"While pupil hydration is indispensable for academic focus (Source C),</text>
    <text x="20" y="284" fill="#1E1B4B" font-size="8.5" font-style="italic">disposable plastic bottles inflict heavy landfill costs (Source B) and</text>
    <text x="20" y="298" fill="#1E1B4B" font-size="8.5" font-style="italic">ecological degradation (Source A). Therefore, schools should install</text>
    <text x="20" y="312" fill="#1E1B4B" font-size="8.5" font-style="italic">filtered hydration taps and provide reusable metal bottles."</text>
  </g>

  <!-- Right: 4-Step Synthesis Pipeline -->
  <g transform="translate(490, 95)" filter="url(#l10Shadow)">
    <rect width="285" height="340" rx="12" fill="#FFFFFF" stroke="#4338CA" stroke-width="2"/>
    <rect x="12" y="12" width="261" height="28" rx="6" fill="#312E81"/>
    <text x="142" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SYNTHESIS WORKFLOW</text>
    
    <g transform="translate(12, 48)">
      <!-- Step 1 -->
      <rect x="0" y="0" width="261" height="58" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <text x="10" y="18" fill="#1E1B4B" font-size="10.5" font-weight="700">1. UNPACK PROMPT</text>
      <text x="10" y="34" fill="#475569" font-size="9">• Identify the core thesis or policy dilemma.</text>
      <text x="10" y="48" fill="#475569" font-size="9">• Define research criteria.</text>

      <!-- Step 2 -->
      <rect x="0" y="65" width="261" height="58" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <text x="10" y="83" fill="#1E1B4B" font-size="10.5" font-weight="700">2. ANNOTATE SOURCES</text>
      <text x="10" y="99" fill="#475569" font-size="9">• Highlight statistics &amp; expert citations.</text>
      <text x="10" y="113" fill="#475569" font-size="9">• Note author credibility &amp; angle.</text>

      <!-- Step 3 -->
      <rect x="0" y="130" width="261" height="58" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <text x="10" y="148" fill="#1E1B4B" font-size="10.5" font-weight="700">3. MAP SYNTHESIS MATRIX</text>
      <text x="10" y="164" fill="#475569" font-size="9">• Group evidence under common themes.</text>
      <text x="10" y="178" fill="#475569" font-size="9">• Cross-reference agreements &amp; contrasts.</text>

      <!-- Step 4 -->
      <rect x="0" y="195" width="261" height="80" rx="6" fill="#312E81"/>
      <text x="10" y="215" fill="#E0E7FF" font-size="10.5" font-weight="700">4. WRITE THEMATIC RESPONSE</text>
      <text x="10" y="233" fill="#FFFFFF" font-size="9">• NEVER summarize A then B separately!</text>
      <text x="10" y="248" fill="#FFFFFF" font-size="9">• Weave multiple citations into each point.</text>
      <text x="10" y="264" fill="#FDE047" font-size="9" font-weight="700">Mastery: Synthesis = Creative Integration</text>
    </g>
  </g>
</svg>"""
