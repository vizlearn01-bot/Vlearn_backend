"""
VLearn CBC Grade 9 English — Topic 2: Reading and Literature
Custom Responsive Vector SVGs for Lessons 1 to 7
"""

# =============================================================================
# SVG 1: Lesson 1 — Reading Fluency & Speed Strategies Matrix
# =============================================================================
SVG_LESSON_1_FLUENCY_STRATEGIES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g9l1HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0369A1"/>
    </linearGradient>
    <linearGradient id="fluencyPillarGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0F9FF"/>
      <stop offset="100%" stop-color="#E0F2FE"/>
    </linearGradient>
    <linearGradient id="strategyPillarGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <filter id="g9l1Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="64" rx="12" fill="url(#g9l1HeaderGrad)" filter="url(#g9l1Shadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">READING FLUENCY &amp; SPEED STRATEGIES MATRIX</text>
  <text x="400" y="68" fill="#BAE6FD" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Balancing Decoding Accuracy, Conversational Pace, Expression, Skimming, and Scanning</text>

  <!-- Top Row: 3 Pillars of Fluency -->
  <!-- 1. Accuracy -->
  <g transform="translate(25, 100)" filter="url(#g9l1Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#fluencyPillarGrad)" stroke="#0284C7" stroke-width="1.5"/>
    <rect x="12" y="12" width="211" height="28" rx="6" fill="#0284C7"/>
    <text x="117" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. ACCURACY</text>
    
    <text x="20" y="62" fill="#0369A1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Correct Decoding:</text>
    <text x="20" y="82" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Pronouncing words correctly</text>
    <text x="20" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Phonics &amp; word breakdown</text>
    <text x="20" y="118" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Ignore unknown words to flow</text>
    <rect x="12" y="134" width="211" height="34" rx="6" fill="#0C4A6E"/>
    <text x="117" y="155" fill="#BAE6FD" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Target: 98%+ Word Accuracy</text>
  </g>

  <!-- 2. Rate (Pace) & Phrasing -->
  <g transform="translate(282, 100)" filter="url(#g9l1Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#fluencyPillarGrad)" stroke="#0284C7" stroke-width="1.5"/>
    <rect x="12" y="12" width="211" height="28" rx="6" fill="#0284C7"/>
    <text x="117" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. RATE &amp; PHRASING</text>
    
    <text x="20" y="62" fill="#0369A1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Conversational Speed:</text>
    <text x="20" y="82" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Chunk words into phrases</text>
    <text x="20" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Avoid choppy word-by-word</text>
    <text x="20" y="118" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Maintain steady rhythm</text>
    <rect x="12" y="134" width="211" height="34" rx="6" fill="#0C4A6E"/>
    <text x="117" y="155" fill="#BAE6FD" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Target: 120–150 Words / Min</text>
  </g>

  <!-- 3. Prosody (Expression) -->
  <g transform="translate(540, 100)" filter="url(#g9l1Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#fluencyPillarGrad)" stroke="#0284C7" stroke-width="1.5"/>
    <rect x="12" y="12" width="211" height="28" rx="6" fill="#0284C7"/>
    <text x="117" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. PROSODY (EXPRESSION)</text>
    
    <text x="20" y="62" fill="#0369A1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Vocal Inflection:</text>
    <text x="20" y="82" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Pitch modulation (rising / falling)</text>
    <text x="20" y="100" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Observe punctuation pauses</text>
    <text x="20" y="118" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Echo reading emulation</text>
    <rect x="12" y="134" width="211" height="34" rx="6" fill="#0C4A6E"/>
    <text x="117" y="155" fill="#BAE6FD" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Target: Expressive Emotion</text>
  </g>

  <!-- Bottom Row: Speed Reading Strategies: Skimming vs Scanning vs Intensive -->
  <!-- Skimming Card -->
  <g transform="translate(25, 300)" filter="url(#g9l1Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#strategyPillarGrad)" stroke="#10B981" stroke-width="1.5"/>
    <rect x="12" y="12" width="211" height="28" rx="6" fill="#059669"/>
    <text x="117" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SKIMMING (GIST)</text>
    
    <text x="20" y="62" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Read for the Big Picture:</text>
    <text x="20" y="82" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">• Titles, headings &amp; subheadings</text>
    <text x="20" y="100" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">• First &amp; last sentences of ¶</text>
    <text x="20" y="118" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">• Visuals, charts &amp; summaries</text>
    <rect x="12" y="134" width="211" height="34" rx="6" fill="#064E3B"/>
    <text x="117" y="155" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Use: Quick overview / preview</text>
  </g>

  <!-- Scanning Card -->
  <g transform="translate(282, 300)" filter="url(#g9l1Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#strategyPillarGrad)" stroke="#10B981" stroke-width="1.5"/>
    <rect x="12" y="12" width="211" height="28" rx="6" fill="#059669"/>
    <text x="117" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SCANNING (DETAILS)</text>
    
    <text x="20" y="62" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Search for Specific Facts:</text>
    <text x="20" y="82" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">• Eye darts across lines</text>
    <text x="20" y="100" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">• Target numbers, dates, names</text>
    <text x="20" y="118" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">• Ignore unrelated paragraphs</text>
    <rect x="12" y="134" width="211" height="34" rx="6" fill="#064E3B"/>
    <text x="117" y="155" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Use: Answering specific questions</text>
  </g>

  <!-- Phrase Chunking Model Card -->
  <g transform="translate(540, 300)" filter="url(#g9l1Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#strategyPillarGrad)" stroke="#10B981" stroke-width="1.5"/>
    <rect x="12" y="12" width="211" height="28" rx="6" fill="#059669"/>
    <text x="117" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">PHRASE CHUNKING</text>
    
    <text x="20" y="62" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Syntactic Chunking Model:</text>
    <text x="20" y="82" fill="#DC2626" font-family="system-ui, sans-serif" font-size="9.5">✗ [The] [tourist] [arrived] [late]</text>
    <text x="20" y="102" fill="#16A34A" font-family="system-ui, sans-serif" font-size="9.5">✓ [The tourist arrived] / [at night]</text>
    <text x="20" y="120" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">• Frees working memory</text>
    <rect x="12" y="134" width="211" height="34" rx="6" fill="#064E3B"/>
    <text x="117" y="155" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Result: Flawless Comprehension</text>
  </g>
</svg>"""

# =============================================================================
# SVG 2: Lesson 2 — The SQ4R Study Architecture & Visual Summarizing Cycle
# =============================================================================
SVG_LESSON_2_SQ4R_NOTE_MAKING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g9l2HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#4338CA"/>
    </linearGradient>
    <linearGradient id="stepGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EEF2FF"/>
      <stop offset="100%" stop-color="#E0E7FF"/>
    </linearGradient>
    <filter id="g9l2Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="64" rx="12" fill="url(#g9l2HeaderGrad)" filter="url(#g9l2Shadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE SQ4R STUDY &amp; NOTE-MAKING FRAMEWORK</text>
  <text x="400" y="68" fill="#C7D2FE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Survey → Question → Read → Recite → Relate → Review (Active Information Processing)</text>

  <!-- 6 Step Hexagonal / Box Flow -->
  <!-- S: Survey -->
  <g transform="translate(25, 100)" filter="url(#g9l2Shadow)">
    <rect width="235" height="175" rx="10" fill="url(#stepGrad1)" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="36" cy="32" r="18" fill="#4F46E5"/>
    <text x="36" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">S</text>
    <text x="64" y="36" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="700">SURVEY</text>
    <text x="16" y="68" fill="#4338CA" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Scan headings &amp; structure:</text>
    <text x="16" y="88" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Titles, bold headings, graphics</text>
    <text x="16" y="106" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Chapter summaries &amp; captions</text>
    <text x="16" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Builds a mental road map</text>
    <rect x="12" y="136" width="211" height="28" rx="5" fill="#312E81"/>
    <text x="117" y="154" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action: 2-minute text preview</text>
  </g>

  <!-- Q: Question -->
  <g transform="translate(282, 100)" filter="url(#g9l2Shadow)">
    <rect width="235" height="175" rx="10" fill="url(#stepGrad1)" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="36" cy="32" r="18" fill="#4F46E5"/>
    <text x="36" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">Q</text>
    <text x="64" y="36" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="700">QUESTION</text>
    <text x="16" y="68" fill="#4338CA" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Turn headings into questions:</text>
    <text x="16" y="88" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• "What causes marine pollution?"</text>
    <text x="16" y="106" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• "How does social media affect us?"</text>
    <text x="16" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Creates active curiosity</text>
    <rect x="12" y="136" width="211" height="28" rx="5" fill="#312E81"/>
    <text x="117" y="154" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action: Write 5W + H questions</text>
  </g>

  <!-- R1: Read -->
  <g transform="translate(540, 100)" filter="url(#g9l2Shadow)">
    <rect width="235" height="175" rx="10" fill="url(#stepGrad1)" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="36" cy="32" r="18" fill="#4F46E5"/>
    <text x="36" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">R1</text>
    <text x="64" y="36" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="700">READ (ACTIVE)</text>
    <text x="16" y="68" fill="#4338CA" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Read to answer questions:</text>
    <text x="16" y="88" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Hunt for answers to your Qs</text>
    <text x="16" y="106" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Visualize sensory descriptions</text>
    <text x="16" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Re-read confusing passages</text>
    <rect x="12" y="136" width="211" height="28" rx="5" fill="#312E81"/>
    <text x="117" y="154" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action: Focused, active search</text>
  </g>

  <!-- Bottom Row: R2, R3, R4 -->
  <!-- R2: Recite -->
  <g transform="translate(25, 295)" filter="url(#g9l2Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#stepGrad1)" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="36" cy="32" r="18" fill="#4F46E5"/>
    <text x="36" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">R2</text>
    <text x="64" y="36" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="700">RECITE &amp; RECORD</text>
    <text x="16" y="68" fill="#4338CA" font-family="system-ui, sans-serif" font-size="11" font-weight="600">State in own words &amp; write:</text>
    <text x="16" y="88" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Speak answers without looking</text>
    <text x="16" y="106" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Write bullet notes / summaries</text>
    <text x="16" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Do NOT copy word-for-word</text>
    <rect x="12" y="138" width="211" height="30" rx="5" fill="#312E81"/>
    <text x="117" y="157" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action: Paraphrased bullet notes</text>
  </g>

  <!-- R3: Relate -->
  <g transform="translate(282, 295)" filter="url(#g9l2Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#stepGrad1)" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="36" cy="32" r="18" fill="#4F46E5"/>
    <text x="36" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">R3</text>
    <text x="64" y="36" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="700">RELATE (CONNECT)</text>
    <text x="16" y="68" fill="#4338CA" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Connect to prior knowledge:</text>
    <text x="16" y="88" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Link new facts to real life</text>
    <text x="16" y="106" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• How does this apply in Kenya?</text>
    <text x="16" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Embeds into long-term memory</text>
    <rect x="12" y="138" width="211" height="30" rx="5" fill="#312E81"/>
    <text x="117" y="157" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action: Real-life contextualization</text>
  </g>

  <!-- R4: Review -->
  <g transform="translate(540, 295)" filter="url(#g9l2Shadow)">
    <rect width="235" height="180" rx="10" fill="url(#stepGrad1)" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="36" cy="32" r="18" fill="#4F46E5"/>
    <text x="36" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">R4</text>
    <text x="64" y="36" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="700">REVIEW (TEST)</text>
    <text x="16" y="68" fill="#4338CA" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Periodic self-testing:</text>
    <text x="16" y="88" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Cover notes and self-quiz</text>
    <text x="16" y="106" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Review 1-day &amp; 1-week later</text>
    <text x="16" y="124" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Prevents forgetting curve</text>
    <rect x="12" y="138" width="211" height="30" rx="5" fill="#312E81"/>
    <text x="117" y="157" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Action: Spaced active recall</text>
  </g>
</svg>"""

# =============================================================================
# SVG 3: Lesson 3 — The Triad of Short Oral Literature Forms
# =============================================================================
SVG_LESSON_3_ORAL_LITERATURE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g9l3HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#B45309"/>
    </linearGradient>
    <linearGradient id="riddleGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#FDE68A"/>
    </linearGradient>
    <linearGradient id="proverbGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFEDD5"/>
      <stop offset="100%" stop-color="#FED7AA"/>
    </linearGradient>
    <linearGradient id="twisterGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#A7F3D0"/>
    </linearGradient>
    <filter id="g9l3Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="64" rx="12" fill="url(#g9l3HeaderGrad)" filter="url(#g9l3Shadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SHORT FORMS OF ORAL LITERATURE</text>
  <text x="400" y="68" fill="#FEF3C7" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Functions, Linguistic Structures, and Performance Dynamics in African Heritage</text>

  <!-- 3 Main Columns -->
  <!-- 1. RIDDLES (Kitendawili) -->
  <g transform="translate(25, 100)" filter="url(#g9l3Shadow)">
    <rect width="235" height="375" rx="12" fill="url(#riddleGrad)" stroke="#D97706" stroke-width="2"/>
    <rect x="14" y="14" width="207" height="34" rx="8" fill="#B45309"/>
    <text x="117" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. RIDDLES</text>
    
    <text x="117" y="68" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">INTELLECTUAL PUZZLES</text>
    
    <!-- Icon: Question Bulb -->
    <circle cx="117" cy="104" r="22" fill="#FDE68A"/>
    <text x="117" y="112" fill="#B45309" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">?</text>
    
    <rect x="12" y="136" width="211" height="106" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="20" y="154" fill="#92400E" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Characteristics &amp; Structure:</text>
    <text x="20" y="172" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Call and response format</text>
    <text x="20" y="190" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Cryptic imagery &amp; metaphors</text>
    <text x="20" y="208" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Prize (mji) given if unsolved</text>
    <text x="20" y="226" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Sharpens observation skills</text>
    
    <rect x="12" y="250" width="211" height="110" rx="6" fill="#78350F"/>
    <text x="20" y="270" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Worked Model:</text>
    <text x="20" y="290" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">Challenge: "Father's endless path"</text>
    <text x="20" y="308" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="9.5">Answer: "A road / river"</text>
    <text x="20" y="330" fill="#FCD34D" font-family="system-ui, sans-serif" font-size="9.5">Function: Trains mental agility &amp;</text>
    <text x="20" y="346" fill="#FCD34D" font-family="system-ui, sans-serif" font-size="9.5">creative problem-solving.</text>
  </g>

  <!-- 2. PROVERBS (Methali) -->
  <g transform="translate(282, 100)" filter="url(#g9l3Shadow)">
    <rect width="235" height="375" rx="12" fill="url(#proverbGrad)" stroke="#EA580C" stroke-width="2"/>
    <rect x="14" y="14" width="207" height="34" rx="8" fill="#C2410C"/>
    <text x="117" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. PROVERBS</text>
    
    <text x="117" y="68" fill="#9A3412" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">METAPHORICAL WISDOM</text>
    
    <!-- Icon: Seed / Tree of wisdom -->
    <circle cx="117" cy="104" r="22" fill="#FED7AA"/>
    <path d="M117 92 C110 98, 106 106, 117 118 C128 106, 124 98, 117 92 Z" fill="#C2410C"/>
    
    <rect x="12" y="136" width="211" height="106" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="20" y="154" fill="#9A3412" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Characteristics &amp; Structure:</text>
    <text x="20" y="172" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Brief, memorable, poetic</text>
    <text x="20" y="190" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Deep metaphorical meaning</text>
    <text x="20" y="208" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Passed across generations</text>
    <text x="20" y="226" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Non-literal life lessons</text>
    
    <rect x="12" y="250" width="211" height="110" rx="6" fill="#7C2D12"/>
    <text x="20" y="270" fill="#FFEDD5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Worked Model:</text>
    <text x="20" y="290" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">"One finger cannot kill a louse."</text>
    <text x="20" y="308" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="9.5">Meaning: Unity &amp; cooperation</text>
    <text x="20" y="330" fill="#FDBA74" font-family="system-ui, sans-serif" font-size="9.5">Function: Moral guidance, conflict</text>
    <text x="20" y="346" fill="#FDBA74" font-family="system-ui, sans-serif" font-size="9.5">resolution &amp; ethical norms.</text>
  </g>

  <!-- 3. TONGUE TWISTERS -->
  <g transform="translate(540, 100)" filter="url(#g9l3Shadow)">
    <rect width="235" height="375" rx="12" fill="url(#twisterGrad)" stroke="#059669" stroke-width="2"/>
    <rect x="14" y="14" width="207" height="34" rx="8" fill="#047857"/>
    <text x="117" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. TONGUE TWISTERS</text>
    
    <text x="117" y="68" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">ARTICULATION AGILITY</text>
    
    <!-- Icon: Speech Soundwaves -->
    <circle cx="117" cy="104" r="22" fill="#D1FAE5"/>
    <path d="M107 104 C110 96, 114 96, 117 104 C120 112, 124 112, 127 104" fill="none" stroke="#047857" stroke-width="2.5" stroke-linecap="round"/>
    
    <rect x="12" y="136" width="211" height="106" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="20" y="154" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Characteristics &amp; Structure:</text>
    <text x="20" y="172" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Heavy alliteration &amp; consonance</text>
    <text x="20" y="190" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Minimal phonetic contrast (/s/ vs /sh/)</text>
    <text x="20" y="208" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Rapid repetitive delivery</text>
    <text x="20" y="226" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Speech muscle training</text>
    
    <rect x="12" y="250" width="211" height="110" rx="6" fill="#064E3B"/>
    <text x="20" y="270" fill="#D1FAE5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Worked Model:</text>
    <text x="20" y="290" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">"She sells sea shells by seashore."</text>
    <text x="20" y="308" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="9.5">Focus: Contrasts /s/ and /ʃ/</text>
    <text x="20" y="330" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="9.5">Function: Trains vocal clarity,</text>
    <text x="20" y="346" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="9.5">fluency, and speech precision.</text>
  </g>
</svg>"""

# =============================================================================
# SVG 4: Lesson 4 — Anatomy of a Poem & Rhyme Scheme Analysis
# =============================================================================
SVG_LESSON_4_POETRY_ANATOMY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g9l4HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#6D28D9"/>
    </linearGradient>
    <linearGradient id="schemeGradA" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F5F3FF"/>
      <stop offset="100%" stop-color="#EDE9FE"/>
    </linearGradient>
    <filter id="g9l4Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="64" rx="12" fill="url(#g9l4HeaderGrad)" filter="url(#g9l4Shadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">POETRY ANATOMY &amp; RHYME SCHEME ARCHITECTURE</text>
  <text x="400" y="68" fill="#DDD6FE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Lines, Stanzas, Rhyme Patterns (AABB vs. ABAB), Personification, and the Persona</text>

  <!-- Left Card: Structural Breakdown -->
  <g transform="translate(25, 100)" filter="url(#g9l4Shadow)">
    <rect width="360" height="375" rx="12" fill="url(#schemeGradA)" stroke="#7C3AED" stroke-width="1.5"/>
    <rect x="14" y="14" width="332" height="32" rx="6" fill="#7C3AED"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RHYME SCHEME PATTERNS</text>
    
    <!-- AABB Couplets -->
    <rect x="14" y="56" width="332" height="142" rx="8" fill="#FFFFFF"/>
    <text x="24" y="76" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Pattern 1: AABB (Couplet Rhyme)</text>
    <text x="24" y="98" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">"The leopard ran across the sand,</text>
    <rect x="305" y="86" width="26" height="16" rx="4" fill="#6D28D9"/>
    <text x="318" y="98" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">A</text>
    
    <text x="24" y="120" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">It was the fastest in the land.</text>
    <rect x="305" y="108" width="26" height="16" rx="4" fill="#6D28D9"/>
    <text x="318" y="120" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">A</text>
    
    <text x="24" y="142" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">It looked up at the sunny sky,</text>
    <rect x="305" y="130" width="26" height="16" rx="4" fill="#0284C7"/>
    <text x="318" y="142" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">B</text>
    
    <text x="24" y="164" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">And saw an eagle flying high."</text>
    <rect x="305" y="152" width="26" height="16" rx="4" fill="#0284C7"/>
    <text x="318" y="164" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">B</text>

    <rect x="14" y="174" width="332" height="18" rx="4" fill="#EDE9FE"/>
    <text x="180" y="187" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Pairs adjacent ending sounds: sand/land, sky/high</text>

    <!-- ABAB Alternate -->
    <rect x="14" y="210" width="332" height="152" rx="8" fill="#FFFFFF"/>
    <text x="24" y="230" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Pattern 2: ABAB (Alternate Rhyme)</text>
    <text x="24" y="252" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">"The golden sun begins to rise,</text>
    <rect x="305" y="240" width="26" height="16" rx="4" fill="#D97706"/>
    <text x="318" y="252" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">A</text>
    
    <text x="24" y="274" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">The birds begin to sing their song.</text>
    <rect x="305" y="262" width="26" height="16" rx="4" fill="#059669"/>
    <text x="318" y="274" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">B</text>
    
    <text x="24" y="296" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">The light ascends across the skies,</text>
    <rect x="305" y="284" width="26" height="16" rx="4" fill="#D97706"/>
    <text x="318" y="296" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">A</text>
    
    <text x="24" y="318" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10.5">The day is bright and very long."</text>
    <rect x="305" y="306" width="26" height="16" rx="4" fill="#059669"/>
    <text x="318" y="318" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">B</text>

    <rect x="14" y="336" width="332" height="18" rx="4" fill="#EDE9FE"/>
    <text x="180" y="349" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Alternates ending rhymes: rise/skies, song/long</text>
  </g>

  <!-- Right Card: Poetic Devices & Persona -->
  <g transform="translate(415, 100)" filter="url(#g9l4Shadow)">
    <rect width="360" height="375" rx="12" fill="url(#schemeGradA)" stroke="#7C3AED" stroke-width="1.5"/>
    <rect x="14" y="14" width="332" height="32" rx="6" fill="#6D28D9"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">POETIC DEVICES &amp; PERSONA</text>

    <!-- Personification Box -->
    <rect x="14" y="56" width="332" height="142" rx="8" fill="#FFFFFF"/>
    <text x="24" y="78" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Personification (Living Qualities)</text>
    <text x="24" y="98" fill="#334155" font-family="system-ui, sans-serif" font-size="10">Giving human feelings/actions to nature or objects.</text>
    <rect x="24" y="108" width="312" height="42" rx="5" fill="#F3F4F6"/>
    <text x="32" y="124" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10">Example: <tspan fill="#7C3AED" font-weight="700">"The ancient trees beckoned us with arms."</tspan></text>
    <text x="32" y="142" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">Trees cannot wave arms; creates a welcoming mood.</text>
    <text x="24" y="168" fill="#047857" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">✓ Transforms dry description into vivid imagination.</text>

    <!-- Persona vs Author Box -->
    <rect x="14" y="210" width="332" height="152" rx="8" fill="#FFFFFF"/>
    <text x="24" y="230" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Persona vs. Author</text>
    <text x="24" y="250" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700">Author:</tspan> The real human who wrote the poem.</text>
    <text x="24" y="268" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700">Persona:</tspan> The fictional speaker telling the poem.</text>
    <rect x="24" y="278" width="312" height="50" rx="5" fill="#FEF3C7"/>
    <text x="32" y="295" fill="#92400E" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Key Insight:</text>
    <text x="32" y="312" fill="#78350F" font-family="system-ui, sans-serif" font-size="9.5">An adult author can speak through the voice of an</text>
    <text x="32" y="324" fill="#78350F" font-family="system-ui, sans-serif" font-size="9.5">elephant calf, a soldier, or a rushing mountain river.</text>

    <rect x="14" y="342" width="332" height="24" rx="4" fill="#6D28D9"/>
    <text x="180" y="358" fill="#DDD6FE" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Goal: Critical interpretation of perspective &amp; tone</text>
  </g>
</svg>"""

# =============================================================================
# SVG 5: Lesson 5 — Dramatic Structure & Freytag's Narrative Plot Arc
# =============================================================================
SVG_LESSON_5_DRAMA_STRUCTURE_PLOT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g9l5HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B91C1C"/>
      <stop offset="100%" stop-color="#991B1B"/>
    </linearGradient>
    <linearGradient id="plotGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <filter id="g9l5Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="64" rx="12" fill="url(#g9l5HeaderGrad)" filter="url(#g9l5Shadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">DRAMATIC STRUCTURE &amp; FREYTAG'S PLOT PYRAMID</text>
  <text x="400" y="68" fill="#FECACA" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Script Formatting (Acts, Scenes, Stage Directions) and the 5 Stages of Dramatic Plot</text>

  <!-- Script Architecture Card (Top Half / Mini Box) -->
  <g transform="translate(25, 95)" filter="url(#g9l5Shadow)">
    <rect width="750" height="115" rx="10" fill="#FFFFFF" stroke="#DC2626" stroke-width="1.5"/>
    <rect x="12" y="10" width="726" height="24" rx="4" fill="#B91C1C"/>
    <text x="375" y="26" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">DRAMATIC SCRIPT ARCHITECTURE (THE BLUEPRINT)</text>
    
    <!-- 4 Script Pillars -->
    <g transform="translate(20, 42)">
      <rect width="165" height="60" rx="6" fill="#FEF2F2" stroke="#FCA5A5"/>
      <text x="82" y="20" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. ACTS &amp; SCENES</text>
      <text x="82" y="38" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Major divisions (Acts)</text>
      <text x="82" y="50" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">&amp; time/place units (Scenes)</text>
    </g>

    <g transform="translate(200, 42)">
      <rect width="165" height="60" rx="6" fill="#FEF2F2" stroke="#FCA5A5"/>
      <text x="82" y="20" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. CHARACTER NAMES</text>
      <text x="82" y="38" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">BOLD ALL CAPS on left</text>
      <text x="82" y="50" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Identifies speaker explicitly</text>
    </g>

    <g transform="translate(380, 42)">
      <rect width="165" height="60" rx="6" fill="#FEF2F2" stroke="#FCA5A5"/>
      <text x="82" y="20" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. STAGE DIRECTIONS</text>
      <text x="82" y="38" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">(Italics in brackets)</text>
      <text x="82" y="50" fill="#DC2626" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">NEVER spoken aloud!</text>
    </g>

    <g transform="translate(560, 42)">
      <rect width="165" height="60" rx="6" fill="#FEF2F2" stroke="#FCA5A5"/>
      <text x="82" y="20" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. SETTING</text>
      <text x="82" y="38" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Time &amp; physical location</text>
      <text x="82" y="50" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Establishes mood &amp; context</text>
    </g>
  </g>

  <!-- Freytag Plot Pyramid (Bottom Half) -->
  <g transform="translate(25, 220)" filter="url(#g9l5Shadow)">
    <rect width="750" height="255" rx="10" fill="url(#plotGrad)" stroke="#B91C1C" stroke-width="1.5"/>
    
    <!-- Pyramid line graph -->
    <path d="M 60 210 L 210 130 L 375 40 L 540 130 L 690 210" fill="none" stroke="#DC2626" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    
    <!-- Stage 1: Exposition -->
    <circle cx="60" cy="210" r="14" fill="#B91C1C"/>
    <text x="60" y="215" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1</text>
    <rect x="10" y="145" width="105" height="52" rx="5" fill="#FFFFFF" stroke="#B91C1C"/>
    <text x="62" y="162" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">EXPOSITION</text>
    <text x="62" y="176" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Introduces setting</text>
    <text x="62" y="188" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">&amp; characters</text>

    <!-- Stage 2: Rising Action -->
    <circle cx="210" cy="130" r="14" fill="#B91C1C"/>
    <text x="210" y="135" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2</text>
    <rect x="155" y="65" width="115" height="52" rx="5" fill="#FFFFFF" stroke="#B91C1C"/>
    <text x="212" y="82" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">RISING ACTION</text>
    <text x="212" y="96" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Conflict emerges &amp;</text>
    <text x="212" y="108" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">tension escalates</text>

    <!-- Stage 3: Climax (Peak) -->
    <circle cx="375" cy="40" r="16" fill="#7F1D1D"/>
    <text x="375" y="45" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3</text>
    <rect x="315" y="-12" width="120" height="42" rx="5" fill="#991B1B"/>
    <text x="375" y="6" fill="#FEF2F2" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. CLIMAX (PEAK)</text>
    <text x="375" y="20" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Turning point of crisis</text>

    <!-- Stage 4: Falling Action -->
    <circle cx="540" cy="130" r="14" fill="#B91C1C"/>
    <text x="540" y="135" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4</text>
    <rect x="480" y="65" width="120" height="52" rx="5" fill="#FFFFFF" stroke="#B91C1C"/>
    <text x="540" y="82" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">FALLING ACTION</text>
    <text x="540" y="96" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Consequences of climax</text>
    <text x="540" y="108" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">unravel</text>

    <!-- Stage 5: Resolution -->
    <circle cx="690" cy="210" r="14" fill="#B91C1C"/>
    <text x="690" y="215" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5</text>
    <rect x="630" y="145" width="115" height="52" rx="5" fill="#FFFFFF" stroke="#B91C1C"/>
    <text x="687" y="162" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">RESOLUTION</text>
    <text x="687" y="176" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Conflict resolved &amp;</text>
    <text x="687" y="188" fill="#334155" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">new balance created</text>
  </g>
</svg>"""

# =============================================================================
# SVG 6: Lesson 6 — Characterisation Matrix & Dramatic Conflict Engine
# =============================================================================
SVG_LESSON_6_CHARACTERISATION_CONFLICT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g9l6HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891B2"/>
      <stop offset="100%" stop-color="#0E7490"/>
    </linearGradient>
    <linearGradient id="charCardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFEFF"/>
      <stop offset="100%" stop-color="#CFFAFE"/>
    </linearGradient>
    <filter id="g9l6Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="64" rx="12" fill="url(#g9l6HeaderGrad)" filter="url(#g9l6Shadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CHARACTERISATION METHODS &amp; DRAMATIC CONFLICT</text>
  <text x="400" y="68" fill="#CFFAFE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Direct vs. Indirect Characterisation, Protagonist vs. Antagonist Dynamics, and Trait Inference</text>

  <!-- Left: Direct vs Indirect Matrix -->
  <g transform="translate(25, 100)" filter="url(#g9l6Shadow)">
    <rect width="360" height="375" rx="12" fill="url(#charCardGrad)" stroke="#0891B2" stroke-width="1.5"/>
    <rect x="14" y="14" width="332" height="32" rx="6" fill="#0891B2"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">CHARACTERISATION TECHNIQUES</text>

    <!-- Direct Box -->
    <rect x="14" y="56" width="332" height="142" rx="8" fill="#FFFFFF"/>
    <text x="24" y="78" fill="#0E7490" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Direct Characterisation (Explicit)</text>
    <text x="24" y="98" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Playwright explicitly states personality in script</text>
    <text x="24" y="114" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• Found in narrator lines or stage directions</text>
    <rect x="24" y="124" width="312" height="42" rx="5" fill="#F0FDFA"/>
    <text x="32" y="140" fill="#0F766E" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Example (Stage direction):</text>
    <text x="32" y="156" fill="#134E4A" font-family="system-ui, sans-serif" font-size="9.5">*(Peter, a greedy and dishonest shopkeeper, enters)*</text>
    <text x="24" y="184" fill="#059669" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">✓ No deduction needed; direct author declaration.</text>

    <!-- Indirect Box -->
    <rect x="14" y="210" width="332" height="152" rx="8" fill="#FFFFFF"/>
    <text x="24" y="230" fill="#0E7490" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Indirect Characterisation (STEAL Model)</text>
    <text x="24" y="250" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700">S</tspan>peech: What they say and how they speak</text>
    <text x="24" y="266" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700">T</tspan>houghts: Monologues revealing inner motives</text>
    <text x="24" y="282" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700">E</tspan>ffect on others: How others react to them</text>
    <text x="24" y="298" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700">A</tspan>ctions: What physical choices they make</text>
    <text x="24" y="314" fill="#334155" font-family="system-ui, sans-serif" font-size="10">• <tspan font-weight="700">L</tspan>ooks: Appearance, posture, and costumes</text>
    <rect x="14" y="332" width="332" height="24" rx="4" fill="#0E7490"/>
    <text x="180" y="348" fill="#CFFAFE" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Audience uses inference &amp; clues to judge morality</text>
  </g>

  <!-- Right: Protagonist vs Antagonist Conflict -->
  <g transform="translate(415, 100)" filter="url(#g9l6Shadow)">
    <rect width="360" height="375" rx="12" fill="url(#charCardGrad)" stroke="#0891B2" stroke-width="1.5"/>
    <rect x="14" y="14" width="332" height="32" rx="6" fill="#0E7490"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">PROTAGONIST VS. ANTAGONIST CLASH</text>

    <!-- Protagonist Box -->
    <rect x="14" y="56" width="332" height="135" rx="8" fill="#FFFFFF"/>
    <text x="24" y="76" fill="#0369A1" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Protagonist (Hero / Central Figure)</text>
    <text x="24" y="94" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Drives the main story goals</text>
    <text x="24" y="108" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Typical Traits: Assertive, honest, courageous</text>
    <text x="24" y="122" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Adverbs of Action: Speaks *gently*, acts *fairly*</text>
    <rect x="24" y="132" width="312" height="48" rx="5" fill="#EFF6FF"/>
    <text x="32" y="148" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9.5">Consumer Example: Sibling Peter demanding an</text>
    <text x="32" y="162" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9.5">official receipt with polite, unyielding firmness.</text>

    <!-- Conflict Arrow -->
    <rect x="14" y="198" width="332" height="30" rx="6" fill="#DC2626"/>
    <text x="180" y="218" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">⚡ DRAMATIC CONFLICT (OPPOSING GOALS) ⚡</text>

    <!-- Antagonist Box -->
    <rect x="14" y="235" width="332" height="130" rx="8" fill="#FFFFFF"/>
    <text x="24" y="255" fill="#991B1B" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Antagonist (Opposing Force)</text>
    <text x="24" y="273" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Obstructs protagonist's goals</text>
    <text x="24" y="287" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Typical Traits: Greedy, aggressive, dismissive</text>
    <text x="24" y="301" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Adverbs of Action: Shouts *angrily*, behaves *rudely*</text>
    <rect x="24" y="311" width="312" height="44" rx="5" fill="#FEF2F2"/>
    <text x="32" y="327" fill="#991B1B" font-family="system-ui, sans-serif" font-size="9.5">Consumer Example: Fraudulent merchant refusing</text>
    <text x="32" y="341" fill="#991B1B" font-family="system-ui, sans-serif" font-size="9.5">to refund expired goods and intimidating buyers.</text>
  </g>
</svg>"""

# =============================================================================
# SVG 7: Lesson 7 — Dramatic Themes, Stylistic Devices & Life Lessons
# =============================================================================
SVG_LESSON_7_THEMES_AND_STYLE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="g9l7HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="themePillarGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <filter id="g9l7Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="64" rx="12" fill="url(#g9l7HeaderGrad)" filter="url(#g9l7Shadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THEMES, STYLISTIC DEVICES &amp; MORAL LESSONS</text>
  <text x="400" y="68" fill="#A7F3D0" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Extracting Universal Messages, Analysing Monologue, Flashback &amp; Humour, and Real-World Application</text>

  <!-- 3 Pillars Grid -->
  <!-- Pillar 1: Monologue -->
  <g transform="translate(25, 100)" filter="url(#g9l7Shadow)">
    <rect width="235" height="375" rx="12" fill="url(#themePillarGrad)" stroke="#059669" stroke-width="1.5"/>
    <rect x="14" y="14" width="207" height="32" rx="6" fill="#059669"/>
    <text x="117" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. MONOLOGUE</text>
    
    <text x="117" y="66" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SOLITARY TRUTH</text>
    
    <!-- Circle Icon -->
    <circle cx="117" cy="102" r="22" fill="#A7F3D0"/>
    <path d="M110 102 C110 97, 114 93, 117 93 C120 93, 124 97, 124 102 C124 107, 120 111, 117 111" fill="none" stroke="#047857" stroke-width="2.5"/>
    
    <rect x="12" y="132" width="211" height="110" rx="6" fill="#FFFFFF"/>
    <text x="20" y="152" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Function &amp; Mechanics:</text>
    <text x="20" y="170" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Actor speaks alone on stage</text>
    <text x="20" y="188" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Unveils private conscience</text>
    <text x="20" y="206" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Bares moral dilemmas &amp; guilt</text>
    <text x="20" y="224" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Deep audience empathy</text>
    
    <rect x="12" y="252" width="211" height="110" rx="6" fill="#064E3B"/>
    <text x="20" y="272" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Example in Drama:</text>
    <text x="20" y="292" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">Peter agonizing over reporting</text>
    <text x="20" y="308" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">his reckless cousin vs. saving</text>
    <text x="20" y="324" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">innocent passenger lives.</text>
    <text x="20" y="346" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Theme: Conscience vs Loyalty</text>
  </g>

  <!-- Pillar 2: Flashback -->
  <g transform="translate(282, 100)" filter="url(#g9l7Shadow)">
    <rect width="235" height="375" rx="12" fill="url(#themePillarGrad)" stroke="#059669" stroke-width="1.5"/>
    <rect x="14" y="14" width="207" height="32" rx="6" fill="#059669"/>
    <text x="117" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. FLASHBACK</text>
    
    <text x="117" y="66" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">TIME INTERRUPT</text>
    
    <!-- Circle Icon: Rewind -->
    <circle cx="117" cy="102" r="22" fill="#A7F3D0"/>
    <path d="M125 94 L113 102 L125 110 Z M113 94 L101 102 L113 110 Z" fill="#047857"/>
    
    <rect x="12" y="132" width="211" height="110" rx="6" fill="#FFFFFF"/>
    <text x="20" y="152" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Function &amp; Mechanics:</text>
    <text x="20" y="170" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Interrupts present chronology</text>
    <text x="20" y="188" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Shows past events &amp; memories</text>
    <text x="20" y="206" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Lighting/music shifts on stage</text>
    <text x="20" y="224" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Explains character motives</text>
    
    <rect x="12" y="252" width="211" height="110" rx="6" fill="#064E3B"/>
    <text x="20" y="272" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Example in Drama:</text>
    <text x="20" y="292" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">James remembering his late</text>
    <text x="20" y="308" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">grandmother's advice when</text>
    <text x="20" y="324" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">tempted to quit schooling.</text>
    <text x="20" y="346" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Theme: Value of Education</text>
  </g>

  <!-- Pillar 3: Humour & Universal Lessons -->
  <g transform="translate(540, 100)" filter="url(#g9l7Shadow)">
    <rect width="235" height="375" rx="12" fill="url(#themePillarGrad)" stroke="#059669" stroke-width="1.5"/>
    <rect x="14" y="14" width="207" height="32" rx="6" fill="#059669"/>
    <text x="117" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. HUMOUR &amp; LESSONS</text>
    
    <text x="117" y="66" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">COMEDY &amp; MORAL VALUE</text>
    
    <!-- Circle Icon: Smile -->
    <circle cx="117" cy="102" r="22" fill="#A7F3D0"/>
    <path d="M107 100 C110 110, 124 110, 127 100" fill="none" stroke="#047857" stroke-width="2.5" stroke-linecap="round"/>
    
    <rect x="12" y="132" width="211" height="110" rx="6" fill="#FFFFFF"/>
    <text x="20" y="152" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Function &amp; Mechanics:</text>
    <text x="20" y="170" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Relieves dramatic tension</text>
    <text x="20" y="188" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Satirizes human greed &amp; pride</text>
    <text x="20" y="206" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Engages audience enjoyment</text>
    <text x="20" y="224" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Universal life takeaways</text>
    
    <rect x="12" y="252" width="211" height="110" rx="6" fill="#064E3B"/>
    <text x="20" y="272" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Example in Drama:</text>
    <text x="20" y="292" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">Mocking corrupt bribery with</text>
    <text x="20" y="308" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">a rotten banana, proving</text>
    <text x="20" y="324" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">dishonesty is ridiculous.</text>
    <text x="20" y="346" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Theme: Integrity &amp; Justice</text>
  </g>
</svg>"""
