"""
VLearn CBC Grade 10 English — Topic 1: Listening and Speaking
Custom Responsive Vector SVGs for Lessons 4, 5, 6, and 7
"""

# =============================================================================
# SVG 1: Lesson 4 — Critical Listening: Fact, Opinion, Evidence, and Bias Matrix
# =============================================================================
SVG_CRITICAL_LISTENING_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l4HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="factGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <linearGradient id="opinionGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#FDE68A"/>
    </linearGradient>
    <linearGradient id="evidenceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="biasGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEE2E2"/>
      <stop offset="100%" stop-color="#FECACA"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Main Banner Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l4HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CRITICAL LISTENING FRAMEWORK</text>
  <text x="400" y="64" fill="#E0E7FF" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Fact vs. Opinion vs. Evidence vs. Bias Analysis Architecture</text>

  <!-- 4 Pillar Grid -->
  
  <!-- 1. FACT PILLAR -->
  <g transform="translate(25, 100)" filter="url(#cardShadow)">
    <rect width="175" height="330" rx="12" fill="url(#factGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="12" y="14" width="151" height="32" rx="8" fill="#059669"/>
    <text x="87" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. FACT</text>
    
    <text x="87" y="68" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">OBJECTIVE TRUTH</text>
    
    <circle cx="87" cy="105" r="24" fill="#A7F3D0"/>
    <path d="M77 105 L84 112 L99 97" fill="none" stroke="#047857" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
    
    <rect x="12" y="140" width="151" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="20" y="158" fill="#065F46" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Verification Criteria:</text>
    <text x="20" y="176" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• 100% Verifiable</text>
    <text x="20" y="193" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Empirical data &amp; dates</text>
    <text x="20" y="210" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Independent of feelings</text>
    
    <rect x="12" y="235" width="151" height="80" rx="6" fill="#064E3B"/>
    <text x="20" y="253" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Spoken Example:</text>
    <text x="20" y="271" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"Kenya attained internal</text>
    <text x="20" y="286" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">self-rule on June 1,</text>
    <text x="20" y="301" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">1963 (Madaraka Day)."</text>
  </g>

  <!-- 2. OPINION PILLAR -->
  <g transform="translate(216, 100)" filter="url(#cardShadow)">
    <rect width="175" height="330" rx="12" fill="url(#opinionGrad)" stroke="#F59E0B" stroke-width="2"/>
    <rect x="12" y="14" width="151" height="32" rx="8" fill="#D97706"/>
    <text x="87" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. OPINION</text>
    
    <text x="87" y="68" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">VALUE JUDGMENT</text>
    
    <circle cx="87" cy="105" r="24" fill="#FDE68A"/>
    <text x="87" y="112" fill="#B45309" font-family="system-ui, sans-serif" font-size="22" font-weight="800" text-anchor="middle">💬</text>
    
    <rect x="12" y="140" width="151" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="20" y="158" fill="#92400E" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Verification Criteria:</text>
    <text x="20" y="176" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Subjective belief</text>
    <text x="20" y="193" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Uses value words</text>
    <text x="20" y="210" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Cannot be proven false</text>
    
    <rect x="12" y="235" width="151" height="80" rx="6" fill="#78350F"/>
    <text x="20" y="253" fill="#FCD34D" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Spoken Example:</text>
    <text x="20" y="271" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"Nairobi is the most</text>
    <text x="20" y="286" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">vibrant, thrilling city</text>
    <text x="20" y="301" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">in all of East Africa."</text>
  </g>

  <!-- 3. EVIDENCE PILLAR -->
  <g transform="translate(407, 100)" filter="url(#cardShadow)">
    <rect width="175" height="330" rx="12" fill="url(#evidenceGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="12" y="14" width="151" height="32" rx="8" fill="#2563EB"/>
    <text x="87" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. EVIDENCE</text>
    
    <text x="87" y="68" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SUPPORTING PROOF</text>
    
    <circle cx="87" cy="105" r="24" fill="#BFDBFE"/>
    <path d="M78 96 H96 M78 104 H96 M78 112 H90" stroke="#1D4ED8" stroke-width="3" stroke-linecap="round"/>
    
    <rect x="12" y="140" width="151" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="20" y="158" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Verification Criteria:</text>
    <text x="20" y="176" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Citations &amp; surveys</text>
    <text x="20" y="193" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Official statistics</text>
    <text x="20" y="210" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Expert testimony</text>
    
    <rect x="12" y="235" width="151" height="80" rx="6" fill="#1E3A8A"/>
    <text x="20" y="253" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Spoken Example:</text>
    <text x="20" y="271" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"According to the KNBS</text>
    <text x="20" y="286" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">2024 economic survey,</text>
    <text x="20" y="301" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">tourism grew by 14.2%."</text>
  </g>

  <!-- 4. BIAS PILLAR -->
  <g transform="translate(598, 100)" filter="url(#cardShadow)">
    <rect width="175" height="330" rx="12" fill="url(#biasGrad)" stroke="#EF4444" stroke-width="2"/>
    <rect x="12" y="14" width="151" height="32" rx="8" fill="#DC2626"/>
    <text x="87" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">4. BIAS</text>
    
    <text x="87" y="68" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">ONE-SIDED SLANT</text>
    
    <circle cx="87" cy="105" r="24" fill="#FECACA"/>
    <path d="M76 96 L98 114 M98 96 L76 114" stroke="#B91C1C" stroke-width="3" stroke-linecap="round"/>
    
    <rect x="12" y="140" width="151" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="20" y="158" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Verification Criteria:</text>
    <text x="20" y="176" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Loaded/polar words</text>
    <text x="20" y="193" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Omission of counter-facts</text>
    <text x="20" y="210" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• Commercial/ideological agenda</text>
    
    <rect x="12" y="235" width="151" height="80" rx="6" fill="#7F1D1D"/>
    <text x="20" y="253" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Spoken Example:</text>
    <text x="20" y="271" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"Our brand is flawless;</text>
    <text x="20" y="286" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">all rival products are</text>
    <text x="20" y="301" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">worthless and slow."</text>
  </g>
</svg>"""


# =============================================================================
# SVG 2: Lesson 5 — Intensive Listening and Viewing for Details Protocol
# =============================================================================
SVG_INTENSIVE_LISTENING_PROTOCOL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l5HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="boxShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Canvas -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Main Banner Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l5HeaderGrad)" filter="url(#boxShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">INTENSIVE LISTENING &amp; VIEWING PROTOCOL</text>
  <text x="400" y="64" fill="#CCFBF1" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">4-Stage Precision Detail Extraction &amp; Multi-Modal Synthesis</text>

  <!-- Process Steps Workflow -->

  <!-- Step 1 -->
  <g transform="translate(35, 105)" filter="url(#boxShadow)">
    <rect width="345" height="150" rx="12" fill="#FFFFFF" stroke="#0D9488" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#0D9488"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">1</text>
    <text x="65" y="32" fill="#0F766E" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Active Sound Filtering</text>
    <text x="65" y="48" fill="#64748B" font-family="system-ui, sans-serif" font-size="10.5">Isolating Signal from Acoustic Noise</text>
    
    <line x1="20" y1="65" x2="325" y2="65" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="20" y="85" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Focus on primary acoustic source</text>
    <text x="20" y="105" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Block out ambient room reverberation</text>
    <text x="20" y="125" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Screen for technical keywords &amp; nouns</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(420, 105)" filter="url(#boxShadow)">
    <rect width="345" height="150" rx="12" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#0284C7"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">2</text>
    <text x="65" y="32" fill="#0369A1" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Sequence &amp; Action Tracking</text>
    <text x="65" y="48" fill="#64748B" font-family="system-ui, sans-serif" font-size="10.5">Capturing Procedural Connectors</text>
    
    <line x1="20" y1="65" x2="325" y2="65" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="20" y="85" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Connectors: "First, Next, Then, Finally"</text>
    <text x="20" y="105" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Imperatives: "Press, connect, verify, enter"</text>
    <text x="20" y="125" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Warnings: "Do not exceed, ensure, caution"</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(35, 280)" filter="url(#boxShadow)">
    <rect width="345" height="150" rx="12" fill="#FFFFFF" stroke="#6366F1" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#6366F1"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">3</text>
    <text x="65" y="32" fill="#4338CA" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Selective Shorthand Notes</text>
    <text x="65" y="48" fill="#64748B" font-family="system-ui, sans-serif" font-size="10.5">Micro-Units &amp; Numerical Precision</text>
    
    <line x1="20" y1="65" x2="325" y2="65" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="20" y="85" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Record exact numbers, units &amp; times</text>
    <text x="20" y="105" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Use symbols: (&amp;, -&gt;, w/, @, #, %)</text>
    <text x="20" y="125" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Avoid verbatim sentence copying</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(420, 280)" filter="url(#boxShadow)">
    <rect width="345" height="150" rx="12" fill="#FFFFFF" stroke="#D97706" stroke-width="2"/>
    <circle cx="35" cy="35" r="18" fill="#D97706"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">4</text>
    <text x="65" y="32" fill="#B45309" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Multi-Modal Triangulation</text>
    <text x="65" y="48" fill="#64748B" font-family="system-ui, sans-serif" font-size="10.5">Correlating Audio with Visual Graphics</text>
    
    <line x1="20" y1="65" x2="325" y2="65" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="20" y="85" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Confirm spoken cues with on-screen slides</text>
    <text x="20" y="105" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Track presenter gestures &amp; pointers</text>
    <text x="20" y="125" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5">• Verify spelling of proper names &amp; codes</text>
  </g>
</svg>"""


# =============================================================================
# SVG 3: Lesson 6 — Non-verbal Communication & Conversational Repair Matrix
# =============================================================================
SVG_NONVERBAL_COMMUNICATION_REPAIR = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l6HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4C1D95"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
    <filter id="nvShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Main Banner Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l6HeaderGrad)" filter="url(#nvShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">NON-VERBAL CHANNELS &amp; CONVERSATIONAL REPAIR</text>
  <text x="400" y="64" fill="#EDE9FE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Integrating Kinesics, Paralanguage, and Real-Time Misunderstanding Resolution</text>

  <!-- Left Column: 4 Non-Verbal Modalities -->
  <g transform="translate(25, 95)" filter="url(#nvShadow)">
    <rect width="360" height="340" rx="12" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="15" y="12" width="330" height="32" rx="6" fill="#6D28D9"/>
    <text x="180" y="33" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">CORE NON-VERBAL CHANNELS</text>
    
    <!-- Channel 1 -->
    <g transform="translate(15, 55)">
      <rect width="330" height="60" rx="8" fill="#F5F3FF" stroke="#DDD6FE"/>
      <text x="12" y="24" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Eye Contact (Oculesics)</text>
      <text x="12" y="44" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Signals honesty, active interest; soft 4-5 sec pauses.</text>
    </g>
    
    <!-- Channel 2 -->
    <g transform="translate(15, 122)">
      <rect width="330" height="60" rx="8" fill="#F5F3FF" stroke="#DDD6FE"/>
      <text x="12" y="24" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Gestures &amp; Posture (Kinesics)</text>
      <text x="12" y="44" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Open hands reinforce points; avoid defensive crossed arms.</text>
    </g>

    <!-- Channel 3 -->
    <g transform="translate(15, 189)">
      <rect width="330" height="60" rx="8" fill="#F5F3FF" stroke="#DDD6FE"/>
      <text x="12" y="24" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Vocalics / Paralanguage</text>
      <text x="12" y="44" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Pitch, tone modulation, pace, and strategic pausing.</text>
    </g>

    <!-- Channel 4 -->
    <g transform="translate(15, 256)">
      <rect width="330" height="60" rx="8" fill="#F5F3FF" stroke="#DDD6FE"/>
      <text x="12" y="24" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Personal Space (Proxemics)</text>
      <text x="12" y="44" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Culturally respectful conversational distance (0.5m - 1.2m).</text>
    </g>
  </g>

  <!-- Right Column: Conversational Repair Engine -->
  <g transform="translate(415, 95)" filter="url(#nvShadow)">
    <rect width="360" height="340" rx="12" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
    <rect x="15" y="12" width="330" height="32" rx="6" fill="#047857"/>
    <text x="180" y="33" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">CONVERSATIONAL REPAIR ENGINE</text>
    
    <!-- Repair Step 1 -->
    <g transform="translate(15, 55)">
      <rect width="330" height="75" rx="8" fill="#ECFDF5" stroke="#A7F3D0"/>
      <text x="12" y="22" fill="#065F46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">1. Ask for Immediate Repetition</text>
      <text x="12" y="40" fill="#374151" font-family="system-ui, sans-serif" font-size="10">When audio is missed or muffled:</text>
      <text x="12" y="58" fill="#047857" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">"I apologize, could you please repeat that last point?"</text>
    </g>

    <!-- Repair Step 2 -->
    <g transform="translate(15, 140)">
      <rect width="330" height="75" rx="8" fill="#ECFDF5" stroke="#A7F3D0"/>
      <text x="12" y="22" fill="#065F46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">2. Request Explicit Clarification</text>
      <text x="12" y="40" fill="#374151" font-family="system-ui, sans-serif" font-size="10">When vocabulary or intent is ambiguous:</text>
      <text x="12" y="58" fill="#047857" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">"Could you clarify what you mean by 'procedural review'?"</text>
    </g>

    <!-- Repair Step 3 -->
    <g transform="translate(15, 225)">
      <rect width="330" height="95" rx="8" fill="#ECFDF5" stroke="#A7F3D0"/>
      <text x="12" y="22" fill="#065F46" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">3. Execute Speaker Self-Correction</text>
      <text x="12" y="40" fill="#374151" font-family="system-ui, sans-serif" font-size="10">When the speaker makes a factual slip:</text>
      <text x="12" y="58" fill="#047857" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">"The meeting is scheduled on Monday—pardon me,</text>
      <text x="12" y="73" fill="#047857" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">I meant Tuesday morning at 10:00 AM."</text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 4: Lesson 7 — Interactive and Responsive Listening Feedback Loop
# =============================================================================
SVG_INTERACTIVE_LISTENING_LOOP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l7HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C2410C"/>
      <stop offset="100%" stop-color="#F97316"/>
    </linearGradient>
    <filter id="loopShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Main Banner Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l7HeaderGrad)" filter="url(#loopShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">5-STAGE INTERACTIVE LISTENING FEEDBACK LOOP</text>
  <text x="400" y="64" fill="#FFEDD5" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Closing the Communication Gap via Empathy, Paraphrasing &amp; Validation</text>

  <!-- 5 Circular Workflow Stages -->

  <!-- Stage 1: Receive -->
  <g transform="translate(45, 110)" filter="url(#loopShadow)">
    <circle cx="65" cy="65" r="58" fill="#EFF6FF" stroke="#3B82F6" stroke-width="3"/>
    <text x="65" y="48" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">STAGE 1</text>
    <text x="65" y="68" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">RECEIVE</text>
    <text x="65" y="86" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Hear &amp; Observe</text>
    <rect x="-10" y="135" width="150" height="55" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="65" y="152" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Unbroken attention</text>
    <text x="65" y="168" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Read body posture</text>
  </g>

  <!-- Stage 2: Process -->
  <g transform="translate(195, 110)" filter="url(#loopShadow)">
    <circle cx="65" cy="65" r="58" fill="#FDF4FF" stroke="#A855F7" stroke-width="3"/>
    <text x="65" y="48" fill="#7E22CE" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">STAGE 2</text>
    <text x="65" y="68" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">PROCESS</text>
    <text x="65" y="86" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Analyze &amp; Empathize</text>
    <rect x="-10" y="135" width="150" height="55" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="65" y="152" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Extract core meaning</text>
    <text x="65" y="168" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Detect emotion/stress</text>
  </g>

  <!-- Stage 3: Paraphrase -->
  <g transform="translate(345, 110)" filter="url(#loopShadow)">
    <circle cx="65" cy="65" r="58" fill="#ECFDF5" stroke="#10B981" stroke-width="3"/>
    <text x="65" y="48" fill="#047857" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">STAGE 3</text>
    <text x="65" y="68" fill="#065F46" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700" text-anchor="middle">PARAPHRASE</text>
    <text x="65" y="86" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Restate Meaning</text>
    <rect x="-10" y="135" width="150" height="55" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="65" y="152" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• "So you are saying..."</text>
    <text x="65" y="168" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• "If I understand right"</text>
  </g>

  <!-- Stage 4: Clarify -->
  <g transform="translate(495, 110)" filter="url(#loopShadow)">
    <circle cx="65" cy="65" r="58" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
    <text x="65" y="48" fill="#B45309" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">STAGE 4</text>
    <text x="65" y="68" fill="#92400E" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CLARIFY</text>
    <text x="65" y="86" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Probe Gently</text>
    <rect x="-10" y="135" width="150" height="55" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="65" y="152" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Open-ended questions</text>
    <text x="65" y="168" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Resolve ambiguities</text>
  </g>

  <!-- Stage 5: Respond -->
  <g transform="translate(645, 110)" filter="url(#loopShadow)">
    <circle cx="65" cy="65" r="58" fill="#FFF1F2" stroke="#F43F5E" stroke-width="3"/>
    <text x="65" y="48" fill="#BE123C" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">STAGE 5</text>
    <text x="65" y="68" fill="#9F1239" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">RESPOND</text>
    <text x="65" y="86" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Support &amp; Validate</text>
    <rect x="-10" y="135" width="150" height="55" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="65" y="152" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Empathetic closure</text>
    <text x="65" y="168" fill="#1E293B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">• Constructive action</text>
  </g>

  <!-- Bottom Synthesis Card -->
  <g transform="translate(35, 330)" filter="url(#loopShadow)">
    <rect width="730" height="100" rx="12" fill="#1E293B"/>
    <text x="25" y="32" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">THE GOLDEN RULE OF RESPONSIVE LISTENING:</text>
    <text x="25" y="56" fill="#F1F5F9" font-family="system-ui, sans-serif" font-size="11.5">"Listen first to understand and validate the speaker's message, not merely to wait for your turn to reply."</text>
    <text x="25" y="80" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">Paraphrasing confirms mutual comprehension, reduces workplace friction, and builds psychological trust.</text>
  </g>
</svg>"""


# =============================================================================
# SVG 5: Lesson 8 — Syllabic and Emphatic Stress Architecture
# =============================================================================
SVG_LESSON_8_STRESS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" width="100%" height="100%" style="background:#0b132b; font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,Helvetica,Arial,sans-serif; border-radius:12px;">
  <defs>
    <linearGradient id="g8_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="g8_noun" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="g8_verb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="g8_emph" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <filter id="g8_shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Title Banner -->
  <rect x="20" y="16" width="880" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
  <text x="460" y="42" text-anchor="middle" fill="#38bdf8" font-size="20" font-weight="700" letter-spacing="0.5">Syllabic &amp; Emphatic Stress Architecture</text>
  <text x="460" y="58" text-anchor="middle" fill="#94a3b8" font-size="12">Mastering Pitch, Volume &amp; Syllable Prominence in Spoken English</text>

  <!-- SECTION 1: Syllabic Stress Shift (Nouns vs. Verbs) -->
  <g transform="translate(20, 80)">
    <!-- Container -->
    <rect x="0" y="0" width="430" height="435" rx="10" fill="#111827" stroke="#374151" stroke-width="1.5" filter="url(#g8_shadow)" />
    
    <!-- Section Header -->
    <rect x="0" y="0" width="430" height="40" rx="10" fill="#1f2937" />
    <path d="M0 30 h430 v10 h-430 z" fill="#1f2937" />
    <text x="215" y="25" text-anchor="middle" fill="#60a5fa" font-size="14" font-weight="700">1. Disyllabic Word Stress Shift (Noun vs. Verb)</text>

    <!-- Noun Rule Card -->
    <rect x="15" y="52" width="195" height="135" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" />
    <rect x="15" y="52" width="195" height="28" rx="8" fill="url(#g8_noun)" />
    <path d="M15 70 h195 v10 h-195 z" fill="#1d4ed8" />
    <text x="112" y="70" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">NOUN / ADJECTIVE</text>
    <text x="112" y="96" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="600">STRESS 1ST SYLLABLE</text>
    
    <!-- Visual Waveform Noun -->
    <rect x="30" y="106" width="75" height="30" rx="4" fill="#2563eb" />
    <text x="67" y="125" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">&#712;RE</text>
    <rect x="110" y="114" width="75" height="22" rx="4" fill="#334155" />
    <text x="147" y="129" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="600">cord</text>
    <text x="112" y="160" text-anchor="middle" fill="#cbd5e1" font-size="10.5">/ˈrɛk.ɔːd/ (noun: disc/file)</text>
    <text x="112" y="176" text-anchor="middle" fill="#93c5fd" font-size="10">High Pitch + Louder Volume</text>

    <!-- Verb Rule Card -->
    <rect x="220" y="52" width="195" height="135" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5" />
    <rect x="220" y="52" width="195" height="28" rx="8" fill="url(#g8_verb)" />
    <path d="M220 70 h195 v10 h-195 z" fill="#047857" />
    <text x="317" y="70" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">VERB (ACTION)</text>
    <text x="317" y="96" text-anchor="middle" fill="#34d399" font-size="11" font-weight="600">STRESS 2ND SYLLABLE</text>
    
    <!-- Visual Waveform Verb -->
    <rect x="235" y="114" width="75" height="22" rx="4" fill="#334155" />
    <text x="272" y="129" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="600">re</text>
    <rect x="315" y="106" width="75" height="30" rx="4" fill="#059669" />
    <text x="352" y="125" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">&#712;CORD</text>
    <text x="317" y="160" text-anchor="middle" fill="#cbd5e1" font-size="10.5">/rɪˈkɔːd/ (verb: capture audio)</text>
    <text x="317" y="176" text-anchor="middle" fill="#6ee7b7" font-size="10">Rising Pitch + Lengthened</text>

    <!-- Stress Contrast Table -->
    <rect x="15" y="198" width="400" height="224" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1" />
    <rect x="15" y="198" width="400" height="26" fill="#334155" rx="6" />
    <path d="M15 214 h400 v10 h-400 z" fill="#334155" />
    <text x="90" y="215" text-anchor="middle" fill="#e2e8f0" font-size="11" font-weight="700">Word Base</text>
    <text x="210" y="215" text-anchor="middle" fill="#93c5fd" font-size="11" font-weight="700">Noun Stress (1st)</text>
    <text x="335" y="215" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="700">Verb Stress (2nd)</text>

    <!-- Row 1 -->
    <line x1="15" y1="262" x2="415" y2="262" stroke="#334155" stroke-dasharray="3,3" />
    <text x="90" y="245" text-anchor="middle" fill="#ffffff" font-size="11.5" font-weight="600">conduct</text>
    <text x="210" y="245" text-anchor="middle" fill="#38bdf8" font-size="11.5">ˈCON-duct (behavior)</text>
    <text x="335" y="245" text-anchor="middle" fill="#34d399" font-size="11.5">con-ˈDUCT (lead/guide)</text>

    <!-- Row 2 -->
    <line x1="15" y1="300" x2="415" y2="300" stroke="#334155" stroke-dasharray="3,3" />
    <text x="90" y="283" text-anchor="middle" fill="#ffffff" font-size="11.5" font-weight="600">present</text>
    <text x="210" y="283" text-anchor="middle" fill="#38bdf8" font-size="11.5">ˈPRE-sent (gift)</text>
    <text x="335" y="283" text-anchor="middle" fill="#34d399" font-size="11.5">pre-ˈSENT (deliver)</text>

    <!-- Row 3 -->
    <line x1="15" y1="338" x2="415" y2="338" stroke="#334155" stroke-dasharray="3,3" />
    <text x="90" y="321" text-anchor="middle" fill="#ffffff" font-size="11.5" font-weight="600">export</text>
    <text x="210" y="321" text-anchor="middle" fill="#38bdf8" font-size="11.5">ˈEX-port (goods sent)</text>
    <text x="335" y="321" text-anchor="middle" fill="#34d399" font-size="11.5">ex-ˈPORT (to ship out)</text>

    <!-- Row 4 -->
    <line x1="15" y1="376" x2="415" y2="376" stroke="#334155" stroke-dasharray="3,3" />
    <text x="90" y="359" text-anchor="middle" fill="#ffffff" font-size="11.5" font-weight="600">contest</text>
    <text x="210" y="359" text-anchor="middle" fill="#38bdf8" font-size="11.5">ˈCON-test (match)</text>
    <text x="335" y="359" text-anchor="middle" fill="#34d399" font-size="11.5">con-ˈTEST (dispute)</text>

    <!-- Row 5 -->
    <text x="90" y="397" text-anchor="middle" fill="#ffffff" font-size="11.5" font-weight="600">produce</text>
    <text x="210" y="397" text-anchor="middle" fill="#38bdf8" font-size="11.5">ˈPRO-duce (crops)</text>
    <text x="335" y="397" text-anchor="middle" fill="#34d399" font-size="11.5">pro-ˈDUCE (manufacture)</text>
  </g>

  <!-- SECTION 2: Emphatic & Contrastive Sentence Stress -->
  <g transform="translate(470, 80)">
    <!-- Container -->
    <rect x="0" y="0" width="430" height="435" rx="10" fill="#111827" stroke="#374151" stroke-width="1.5" filter="url(#g8_shadow)" />
    
    <!-- Section Header -->
    <rect x="0" y="0" width="430" height="40" rx="10" fill="#1f2937" />
    <path d="M0 30 h430 v10 h-430 z" fill="#1f2937" />
    <text x="215" y="25" text-anchor="middle" fill="#fbbf24" font-size="14" font-weight="700">2. Emphatic Stress (Sentence Level Meaning)</text>

    <!-- Core Principle Banner -->
    <rect x="15" y="52" width="400" height="48" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1" />
    <text x="215" y="72" text-anchor="middle" fill="#fde68a" font-size="11.5" font-weight="700">Base Sentence: "I didn't say she stole my phone."</text>
    <text x="215" y="89" text-anchor="middle" fill="#94a3b8" font-size="10.5">Shifting focus word transforms contextual meaning completely</text>

    <!-- Emphatic Breakdown Rows -->
    <!-- Case 1: [I] -->
    <g transform="translate(15, 108)">
      <rect x="0" y="0" width="400" height="56" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1" />
      <rect x="8" y="10" width="36" height="22" rx="4" fill="#f59e0b" />
      <text x="26" y="25" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="800">I</text>
      <text x="50" y="25" fill="#e2e8f0" font-size="11.5">didn't say she stole my phone.</text>
      <text x="12" y="46" fill="#38bdf8" font-size="10.5" font-weight="600">&#10140; Implied:</text>
      <text x="72" y="46" fill="#cbd5e1" font-size="10.5">Someone else said it, not me!</text>
    </g>

    <!-- Case 2: [SAY] -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="400" height="56" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1" />
      <text x="12" y="25" fill="#e2e8f0" font-size="11.5">I didn't</text>
      <rect x="62" y="10" width="42" height="22" rx="4" fill="#f59e0b" />
      <text x="83" y="25" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="800">SAY</text>
      <text x="110" y="25" fill="#e2e8f0" font-size="11.5">she stole my phone.</text>
      <text x="12" y="46" fill="#38bdf8" font-size="10.5" font-weight="600">&#10140; Implied:</text>
      <text x="72" y="46" fill="#cbd5e1" font-size="10.5">I hinted or wrote it, but didn't utter it aloud.</text>
    </g>

    <!-- Case 3: [SHE] -->
    <g transform="translate(15, 232)">
      <rect x="0" y="0" width="400" height="56" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
      <text x="12" y="25" fill="#e2e8f0" font-size="11.5">I didn't say</text>
      <rect x="88" y="10" width="42" height="22" rx="4" fill="#f59e0b" />
      <text x="109" y="25" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="800">SHE</text>
      <text x="136" y="25" fill="#e2e8f0" font-size="11.5">stole my phone.</text>
      <text x="12" y="46" fill="#fbbf24" font-size="10.5" font-weight="700">&#10140; Implied:</text>
      <text x="72" y="46" fill="#fef08a" font-size="10.5" font-weight="600">Another specific person stole it, not her!</text>
    </g>

    <!-- Case 4: [STOLE] -->
    <g transform="translate(15, 294)">
      <rect x="0" y="0" width="400" height="56" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1" />
      <text x="12" y="25" fill="#e2e8f0" font-size="11.5">I didn't say she</text>
      <rect x="110" y="10" width="54" height="22" rx="4" fill="#f59e0b" />
      <text x="137" y="25" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="800">STOLE</text>
      <text x="170" y="25" fill="#e2e8f0" font-size="11.5">my phone.</text>
      <text x="12" y="46" fill="#38bdf8" font-size="10.5" font-weight="600">&#10140; Implied:</text>
      <text x="72" y="46" fill="#cbd5e1" font-size="10.5">She may have borrowed it without asking.</text>
    </g>

    <!-- Case 5: [PHONE] -->
    <g transform="translate(15, 356)">
      <rect x="0" y="0" width="400" height="56" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1" />
      <text x="12" y="25" fill="#e2e8f0" font-size="11.5">I didn't say she stole my</text>
      <rect x="165" y="10" width="60" height="22" rx="4" fill="#f59e0b" />
      <text x="195" y="25" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="800">PHONE</text>
      <text x="228" y="25" fill="#e2e8f0" font-size="11.5">.</text>
      <text x="12" y="46" fill="#38bdf8" font-size="10.5" font-weight="600">&#10140; Implied:</text>
      <text x="72" y="46" fill="#cbd5e1" font-size="10.5">She took my wallet or laptop, not my phone.</text>
    </g>
  </g>
</svg>"""


# =============================================================================
# SVG 6: Lesson 9 — Speaking Fluency Triangle & Signposting Architecture
# =============================================================================
SVG_LESSON_9_FLUENCY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" width="100%" height="100%" style="background:#091428; font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,Helvetica,Arial,sans-serif; border-radius:12px;">
  <defs>
    <linearGradient id="g9_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="g9_pillar1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0ea5e9" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
    <linearGradient id="g9_pillar2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" />
      <stop offset="100%" stop-color="#6d28d9" />
    </linearGradient>
    <linearGradient id="g9_pillar3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <filter id="g9_shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Title Banner -->
  <rect x="20" y="16" width="880" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
  <text x="460" y="42" text-anchor="middle" fill="#38bdf8" font-size="20" font-weight="700" letter-spacing="0.5">Speaking Fluency &amp; Discourse Signposting</text>
  <text x="460" y="58" text-anchor="middle" fill="#94a3b8" font-size="12">The 3 Core Pillars of High-Impact Presentations, Interviews &amp; Conversations</text>

  <!-- LEFT: The 3 Pillars of Fluency -->
  <g transform="translate(20, 80)">
    <rect x="0" y="0" width="430" height="435" rx="10" fill="#111827" stroke="#374151" stroke-width="1.5" filter="url(#g9_shadow)" />
    
    <rect x="0" y="0" width="430" height="40" rx="10" fill="#1f2937" />
    <path d="M0 30 h430 v10 h-430 z" fill="#1f2937" />
    <text x="215" y="25" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="700">The 3 Pillars of Spoken Fluency</text>

    <!-- Pillar 1: Controlled Pace & Pause Power -->
    <g transform="translate(15, 52)">
      <rect x="0" y="0" width="400" height="110" rx="8" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5" />
      <rect x="0" y="0" width="400" height="26" rx="8" fill="url(#g9_pillar1)" />
      <path d="M0 16 h400 v10 h-400 z" fill="#0284c7" />
      <text x="200" y="18" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">1. CONTROLLED PACE &amp; PAUSE POWER</text>
      
      <circle cx="30" cy="56" r="14" fill="#0284c7" />
      <text x="30" y="61" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">130</text>
      <text x="56" y="50" fill="#38bdf8" font-size="11" font-weight="700">Optimal Rate: 120-150 Words Per Minute</text>
      <text x="56" y="66" fill="#cbd5e1" font-size="10.5">Too fast creates slurring; too slow causes cognitive drift.</text>
      <text x="20" y="94" fill="#fef08a" font-size="10.5" font-weight="600">&#9888; Replace fillers ("um", "like", "you know") with 1-second silent pauses.</text>
    </g>

    <!-- Pillar 2: Signposting Roadmap -->
    <g transform="translate(15, 174)">
      <rect x="0" y="0" width="400" height="110" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5" />
      <rect x="0" y="0" width="400" height="26" rx="8" fill="url(#g9_pillar2)" />
      <path d="M0 16 h400 v10 h-400 z" fill="#6d28d9" />
      <text x="200" y="18" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">2. COHERENT DISCOURSE SIGNPOSTING</text>
      
      <text x="20" y="48" fill="#c4b5fd" font-size="11" font-weight="700">Linguistic Signposts Guide the Listener's Brain:</text>
      <text x="20" y="66" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#a78bfa" font-weight="600">Sequencing:</tspan> "First and foremost...", "Subsequently..."</text>
      <text x="20" y="82" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#a78bfa" font-weight="600">Contrasting:</tspan> "On the other hand...", "Conversely..."</text>
      <text x="20" y="98" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#a78bfa" font-weight="600">Concluding:</tspan> "In summary...", "To wrap up our findings..."</text>
    </g>

    <!-- Pillar 3: Audience Awareness & Body Language -->
    <g transform="translate(15, 296)">
      <rect x="0" y="0" width="400" height="118" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5" />
      <rect x="0" y="0" width="400" height="26" rx="8" fill="url(#g9_pillar3)" />
      <path d="M0 16 h400 v10 h-400 z" fill="#047857" />
      <text x="200" y="18" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">3. AUDIENCE ENGAGEMENT &amp; REGISTER</text>
      
      <text x="20" y="48" fill="#6ee7b7" font-size="11" font-weight="700">Non-Verbal &amp; Vocal Modulation:</text>
      <text x="20" y="66" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#34d399" font-weight="600">Eye Contact:</tspan> 3-second zone scanning across audience.</text>
      <text x="20" y="82" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#34d399" font-weight="600">Vocal Pitch &amp; Modulation:</tspan> Avoid flat robotic monotone.</text>
      <text x="20" y="98" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#34d399" font-weight="600">Formal Register:</tspan> Match vocabulary to panel or interview.</text>
    </g>
  </g>

  <!-- RIGHT: Presentation & Interview Signposting Flowchart -->
  <g transform="translate(470, 80)">
    <rect x="0" y="0" width="430" height="435" rx="10" fill="#111827" stroke="#374151" stroke-width="1.5" filter="url(#g9_shadow)" />
    
    <rect x="0" y="0" width="430" height="40" rx="10" fill="#1f2937" />
    <path d="M0 30 h430 v10 h-430 z" fill="#1f2937" />
    <text x="215" y="25" text-anchor="middle" fill="#a855f7" font-size="14" font-weight="700">Presentation Delivery Flowchart</text>

    <!-- Stage 1: The Hook & Introduction -->
    <g transform="translate(20, 52)">
      <rect x="0" y="0" width="390" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
      <circle cx="24" cy="30" r="14" fill="#0284c7" />
      <text x="24" y="35" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">01</text>
      <text x="48" y="24" fill="#38bdf8" font-size="12" font-weight="700">THE HOOK &amp; PURPOSE STATEMENT</text>
      <text x="48" y="42" fill="#cbd5e1" font-size="10.5">"Have you ever wondered...? Today, I will demonstrate..."</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M215 116 v16" stroke="#64748b" stroke-width="2" stroke-dasharray="3,3" />
    <polygon points="211,130 215,138 219,130" fill="#64748b" />

    <!-- Stage 2: Main Point 1 -->
    <g transform="translate(20, 142)">
      <rect x="0" y="0" width="390" height="60" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1.5" />
      <circle cx="24" cy="30" r="14" fill="#4f46e5" />
      <text x="24" y="35" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">02</text>
      <text x="48" y="24" fill="#818cf8" font-size="12" font-weight="700">SIGNPOST 1: CORE THESIS &amp; EVIDENCE</text>
      <text x="48" y="42" fill="#cbd5e1" font-size="10.5">"First and foremost, our empirical data indicates that..."</text>
    </g>

    <!-- Arrow 2 -->
    <path d="M215 206 v16" stroke="#64748b" stroke-width="2" stroke-dasharray="3,3" />
    <polygon points="211,220 215,228 219,220" fill="#64748b" />

    <!-- Stage 3: Counter-perspective or Secondary Point -->
    <g transform="translate(20, 232)">
      <rect x="0" y="0" width="390" height="60" rx="6" fill="#1e293b" stroke="#c084fc" stroke-width="1.5" />
      <circle cx="24" cy="30" r="14" fill="#9333ea" />
      <text x="24" y="35" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">03</text>
      <text x="48" y="24" fill="#c084fc" font-size="12" font-weight="700">SIGNPOST 2: CONTRAST / DEVELOPMENT</text>
      <text x="48" y="42" fill="#cbd5e1" font-size="10.5">"However, looking at the alternative viewpoint..."</text>
    </g>

    <!-- Arrow 3 -->
    <path d="M215 296 v16" stroke="#64748b" stroke-width="2" stroke-dasharray="3,3" />
    <polygon points="211,310 215,318 219,310" fill="#64748b" />

    <!-- Stage 4: Conclusion & Call to Action -->
    <g transform="translate(20, 322)">
      <rect x="0" y="0" width="390" height="66" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
      <circle cx="24" cy="33" r="14" fill="#059669" />
      <text x="24" y="38" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">04</text>
      <text x="48" y="25" fill="#34d399" font-size="12" font-weight="700">SIGNPOST 3: SYNTHESIS &amp; CLOSING</text>
      <text x="48" y="43" fill="#cbd5e1" font-size="10.5">"In conclusion, these factors demonstrate..."</text>
      <text x="48" y="58" fill="#93c5fd" font-size="10">"Thank you for your attention. I welcome your questions."</text>
    </g>

    <text x="215" y="416" text-anchor="middle" fill="#94a3b8" font-size="10.5">Signposts prevent mental fatigue &amp; anchor key arguments in memory.</text>
  </g>
</svg>"""


# =============================================================================
# SVG 7: Lesson 10 — Formal Meetings, Debate & Oral Decision-Making
# =============================================================================
SVG_LESSON_10_MEETINGS_DEBATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" width="100%" height="100%" style="background:#09111e; font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,Helvetica,Arial,sans-serif; border-radius:12px;">
  <defs>
    <linearGradient id="g10_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="g10_chair" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <linearGradient id="g10_sec" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="g10_deb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <filter id="g10_shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Title Banner -->
  <rect x="20" y="16" width="880" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
  <text x="460" y="42" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="700" letter-spacing="0.5">Formal Meetings, Debate &amp; Oral Decision-Making</text>
  <text x="460" y="58" text-anchor="middle" fill="#94a3b8" font-size="12">Parliamentary Governance, Role Responsibilities &amp; Diplomatic Rebuttal Protocol</text>

  <!-- LEFT: Role Architecture in Formal Meetings -->
  <g transform="translate(20, 80)">
    <rect x="0" y="0" width="430" height="435" rx="10" fill="#111827" stroke="#374151" stroke-width="1.5" filter="url(#g10_shadow)" />
    
    <rect x="0" y="0" width="430" height="40" rx="10" fill="#1f2937" />
    <path d="M0 30 h430 v10 h-430 z" fill="#1f2937" />
    <text x="215" y="25" text-anchor="middle" fill="#fcd34d" font-size="14" font-weight="700">Meeting Roles &amp; Responsibilities</text>

    <!-- Role 1: Chairperson -->
    <g transform="translate(15, 52)">
      <rect x="0" y="0" width="400" height="96" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
      <rect x="0" y="0" width="400" height="26" rx="8" fill="url(#g10_chair)" />
      <path d="M0 16 h400 v10 h-400 z" fill="#d97706" />
      <text x="200" y="18" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="800">CHAIRPERSON (THE CHAIR / SPEAKER)</text>
      
      <text x="16" y="46" fill="#fde68a" font-size="11" font-weight="700">&#8226; Presides over proceedings</text>
      <text x="195" y="46" fill="#cbd5e1" font-size="10.5">Calls meeting to order</text>
      <text x="16" y="64" fill="#fde68a" font-size="11" font-weight="700">&#8226; Controls turn-taking</text>
      <text x="195" y="64" fill="#cbd5e1" font-size="10.5">Grants or revokes floor</text>
      <text x="16" y="82" fill="#fde68a" font-size="11" font-weight="700">&#8226; Maintains decorum</text>
      <text x="195" y="82" fill="#cbd5e1" font-size="10.5">Ensures neutrality &amp; agenda</text>
    </g>

    <!-- Role 2: Secretary -->
    <g transform="translate(15, 158)">
      <rect x="0" y="0" width="400" height="96" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" />
      <rect x="0" y="0" width="400" height="26" rx="8" fill="url(#g10_sec)" />
      <path d="M0 16 h400 v10 h-400 z" fill="#1d4ed8" />
      <text x="200" y="18" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">SECRETARY (MINUTES RECORDER)</text>
      
      <text x="16" y="46" fill="#93c5fd" font-size="11" font-weight="700">&#8226; Distributes agenda</text>
      <text x="195" y="46" fill="#cbd5e1" font-size="10.5">Notice of meeting in advance</text>
      <text x="16" y="64" fill="#93c5fd" font-size="11" font-weight="700">&#8226; Records the Minutes</text>
      <text x="195" y="64" fill="#cbd5e1" font-size="10.5">Official written legal record</text>
      <text x="16" y="82" fill="#93c5fd" font-size="11" font-weight="700">&#8226; Tracks action items</text>
      <text x="195" y="82" fill="#cbd5e1" font-size="10.5">Documents votes &amp; assignees</text>
    </g>

    <!-- Role 3: Members & Debaters -->
    <g transform="translate(15, 264)">
      <rect x="0" y="0" width="400" height="155" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5" />
      <rect x="0" y="0" width="400" height="26" rx="8" fill="url(#g10_deb)" />
      <path d="M0 16 h400 v10 h-400 z" fill="#047857" />
      <text x="200" y="18" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">MEMBERS &amp; DEBATE DELEGATES</text>
      
      <text x="16" y="46" fill="#6ee7b7" font-size="11" font-weight="700">Parliamentary Motions &amp; Voting:</text>
      <text x="16" y="64" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#34d399" font-weight="600">Tabling a Motion:</tspan> "I move that this committee approve..."</text>
      <text x="16" y="82" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#34d399" font-weight="600">Seconding:</tspan> "I second the motion, Mr. Chairman."</text>
      <text x="16" y="100" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#34d399" font-weight="600">Consensus Building:</tspan> Synthesizing viewpoints for unanimity.</text>
      <text x="16" y="118" fill="#cbd5e1" font-size="10.5">&#8226; <tspan fill="#34d399" font-weight="600">Formal Voting:</tspan> Ayes (In favor) vs. Nays (Against).</text>
      <text x="16" y="140" fill="#fde68a" font-size="10.5" font-weight="600">&#9888; Always address the Chair: "Mr. Speaker, through you..."</text>
    </g>
  </g>

  <!-- RIGHT: 5-Stage Decision Cycle & Diplomatic Rebuttal -->
  <g transform="translate(470, 80)">
    <rect x="0" y="0" width="430" height="435" rx="10" fill="#111827" stroke="#374151" stroke-width="1.5" filter="url(#g10_shadow)" />
    
    <rect x="0" y="0" width="430" height="40" rx="10" fill="#1f2937" />
    <path d="M0 30 h430 v10 h-430 z" fill="#1f2937" />
    <text x="215" y="25" text-anchor="middle" fill="#60a5fa" font-size="14" font-weight="700">5-Stage Oral Decision Cycle</text>

    <!-- Stage 1 -->
    <g transform="translate(20, 50)">
      <rect x="0" y="0" width="390" height="44" rx="6" fill="#1e293b" stroke="#334155" />
      <circle cx="20" cy="22" r="11" fill="#3b82f6" />
      <text x="20" y="26" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="700">1</text>
      <text x="40" y="18" fill="#60a5fa" font-size="11" font-weight="700">Call to Order &amp; Agenda Confirmation</text>
      <text x="40" y="34" fill="#94a3b8" font-size="10">Adoption of previous minutes &amp; today's roadmap</text>
    </g>

    <!-- Stage 2 -->
    <g transform="translate(20, 100)">
      <rect x="0" y="0" width="390" height="44" rx="6" fill="#1e293b" stroke="#334155" />
      <circle cx="20" cy="22" r="11" fill="#8b5cf6" />
      <text x="20" y="26" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="700">2</text>
      <text x="40" y="18" fill="#a78bfa" font-size="11" font-weight="700">Motion Tabled &amp; Seconded</text>
      <text x="40" y="34" fill="#94a3b8" font-size="10">Formal proposal introduced for floor consideration</text>
    </g>

    <!-- Stage 3 -->
    <g transform="translate(20, 150)">
      <rect x="0" y="0" width="390" height="44" rx="6" fill="#1e293b" stroke="#334155" />
      <circle cx="20" cy="22" r="11" fill="#ec4899" />
      <text x="20" y="26" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="700">3</text>
      <text x="40" y="18" fill="#f472b6" font-size="11" font-weight="700">Structured Debate &amp; Turn-Taking</text>
      <text x="40" y="34" fill="#94a3b8" font-size="10">Proposition arguments alternate with Opposition</text>
    </g>

    <!-- Stage 4 -->
    <g transform="translate(20, 200)">
      <rect x="0" y="0" width="390" height="44" rx="6" fill="#1e293b" stroke="#334155" />
      <circle cx="20" cy="22" r="11" fill="#f59e0b" />
      <text x="20" y="26" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="800">4</text>
      <text x="40" y="18" fill="#fbbf24" font-size="11" font-weight="700">Polite Rebuttals &amp; Consensus Building</text>
      <text x="40" y="34" fill="#94a3b8" font-size="10">Countering claims with evidence, avoiding personal attacks</text>
    </g>

    <!-- Stage 5 -->
    <g transform="translate(20, 250)">
      <rect x="0" y="0" width="390" height="44" rx="6" fill="#1e293b" stroke="#334155" />
      <circle cx="20" cy="22" r="11" fill="#10b981" />
      <text x="20" y="26" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="700">5</text>
      <text x="40" y="18" fill="#34d399" font-size="11" font-weight="700">Voting, Resolutions &amp; Minutes Signed</text>
      <text x="40" y="34" fill="#94a3b8" font-size="10">Binding decision recorded, responsibilities assigned</text>
    </g>

    <!-- Diplomatic Rebuttal Formula Box -->
    <g transform="translate(20, 304)">
      <rect x="0" y="0" width="390" height="116" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
      <rect x="0" y="0" width="390" height="24" rx="8" fill="#b45309" />
      <path d="M0 14 h390 v10 h-390 z" fill="#b45309" />
      <text x="195" y="17" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">DIPLOMATIC REBUTTAL PROTOCOL</text>
      
      <text x="12" y="42" fill="#fef08a" font-size="10.5" font-weight="700">&#10004; Professional:</text>
      <text x="12" y="58" fill="#cbd5e1" font-size="10">"While I acknowledge my colleague's point, the evidence suggests..."</text>
      <line x1="12" y1="68" x2="378" y2="68" stroke="#334155" stroke-dasharray="2,2" />
      <text x="12" y="84" fill="#f87171" font-size="10.5" font-weight="700">&#10008; Unparliamentary (Rude):</text>
      <text x="12" y="100" fill="#cbd5e1" font-size="10">"That idea makes no sense; you don't know what you're talking about."</text>
    </g>
  </g>
</svg>"""

