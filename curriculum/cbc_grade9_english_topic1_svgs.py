"""
VLearn CBC Grade 9 English — Topic 1: Listening and Speaking
Custom Responsive Vector SVGs for Lessons 1 to 8
"""

# =============================================================================
# SVG 1: Lesson 1 — Euphemism Transformation Matrix & Courtesy Filter
# =============================================================================
SVG_EUPHEMISM_FRAMEWORK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l1HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="bluntGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <linearGradient id="filterGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="euphemismGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Main Banner Header -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l1HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">EUPHEMISM TRANSFORMATION &amp; COURTESY SPECTRUM</text>
  <text x="400" y="65" fill="#BFDBFE" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Transforming Blunt Statements into Empathetic, Respectful Language</text>

  <!-- 1. BLUNT DIRECT STATEMENT -->
  <g transform="translate(30, 100)" filter="url(#cardShadow)">
    <rect width="215" height="320" rx="12" fill="url(#bluntGrad)" stroke="#EF4444" stroke-width="2"/>
    <rect x="15" y="15" width="185" height="35" rx="8" fill="#DC2626"/>
    <text x="107" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. BLUNT / HARSH</text>
    
    <circle cx="107" cy="85" r="22" fill="#FCA5A5"/>
    <text x="107" y="93" fill="#7F1D1D" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">✖</text>

    <rect x="12" y="120" width="191" height="90" rx="6" fill="#FFFFFF"/>
    <text x="20" y="140" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Characteristics:</text>
    <text x="20" y="160" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Harsh &amp; aggressive</text>
    <text x="20" y="178" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Causes emotional hurt</text>
    <text x="20" y="196" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Breaks social harmony</text>

    <rect x="12" y="225" width="191" height="80" rx="6" fill="#7F1D1D"/>
    <text x="20" y="245" fill="#FECACA" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Direct Example:</text>
    <text x="20" y="265" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-style="italic">"The old man died and</text>
    <text x="20" y="282" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-style="italic">his son is in prison."</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M255 260 L280 260" stroke="#3B82F6" stroke-width="4" stroke-linecap="round"/>
  <polygon points="285,260 275,254 275,266" fill="#3B82F6"/>

  <!-- 2. THE EUPHEMISM SOFTENER FILTER -->
  <g transform="translate(290, 100)" filter="url(#cardShadow)">
    <rect width="220" height="320" rx="12" fill="url(#filterGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="15" y="15" width="190" height="35" rx="8" fill="#2563EB"/>
    <text x="110" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. THE COURTESY FILTER</text>
    
    <circle cx="110" cy="85" r="22" fill="#93C5FD"/>
    <text x="110" y="93" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">🛡</text>

    <rect x="12" y="120" width="196" height="90" rx="6" fill="#FFFFFF"/>
    <text x="20" y="140" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Softer Substitutions:</text>
    <text x="20" y="160" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Died ➔ Passed away</text>
    <text x="20" y="178" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Old ➔ Senior citizen</text>
    <text x="20" y="196" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Prison ➔ Correctional</text>

    <rect x="12" y="225" width="196" height="80" rx="6" fill="#1E3A8A"/>
    <text x="20" y="245" fill="#BFDBFE" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Analogy Mechanism:</text>
    <text x="20" y="265" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">Acts like a soft pillow</text>
    <text x="20" y="282" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">softening harsh realities.</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M515 260 L540 260" stroke="#10B981" stroke-width="4" stroke-linecap="round"/>
  <polygon points="545,260 535,254 535,266" fill="#10B981"/>

  <!-- 3. POLITE EUPHEMISTIC OUTPUT -->
  <g transform="translate(550, 100)" filter="url(#cardShadow)">
    <rect width="220" height="320" rx="12" fill="url(#euphemismGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="15" y="15" width="190" height="35" rx="8" fill="#059669"/>
    <text x="110" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. POLITE EXPRESSION</text>
    
    <circle cx="110" cy="85" r="22" fill="#6EE7B7"/>
    <text x="110" y="93" fill="#064E3B" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">✔</text>

    <rect x="12" y="120" width="196" height="90" rx="6" fill="#FFFFFF"/>
    <text x="20" y="140" fill="#047857" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Outcome &amp; Tone:</text>
    <text x="20" y="160" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Empathetic &amp; respectful</text>
    <text x="20" y="178" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Preserves human dignity</text>
    <text x="20" y="196" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Builds citizenship trust</text>

    <rect x="12" y="225" width="196" height="80" rx="6" fill="#064E3B"/>
    <text x="20" y="245" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Polite Version:</text>
    <text x="20" y="265" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-style="italic">"The senior citizen has passed</text>
    <text x="20" y="282" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-style="italic">away; son in correctional facility."</text>
  </g>
</svg>"""


# =============================================================================
# SVG 2: Lesson 2 — Empathetic Listening & Emotional Mirroring Loop
# =============================================================================
SVG_EMPATHETIC_LISTENING_LOOP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l2HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4C1D95"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l2HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">EMPATHETIC LISTENING &amp; EMOTIONAL MIRRORING ARCHITECTURE</text>
  <text x="400" y="65" fill="#DDD6FE" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">4-Stage Cycle for Validating Feelings and Building Mutual Trust</text>

  <!-- Step 1: Attend & Observe -->
  <g transform="translate(40, 110)" filter="url(#cardShadow)">
    <rect width="330" height="140" rx="12" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="15" y="15" width="40" height="40" rx="8" fill="#7C3AED"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">1</text>
    <text x="68" y="34" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="14" font-weight="700">ATTEND &amp; OBSERVE</text>
    <text x="68" y="50" fill="#6B7280" font-family="system-ui, sans-serif" font-size="11">Non-verbal cues &amp; emotional tone</text>
    <text x="20" y="80" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Maintain gentle eye contact &amp; nod</text>
    <text x="20" y="100" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Notice vocal pitch, pauses &amp; slumped posture</text>
    <text x="20" y="120" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Refrain from checking phone or interrupting</text>
  </g>

  <!-- Step 2: Decode & Validate -->
  <g transform="translate(430, 110)" filter="url(#cardShadow)">
    <rect width="330" height="140" rx="12" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="15" y="15" width="40" height="40" rx="8" fill="#7C3AED"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">2</text>
    <text x="68" y="34" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="14" font-weight="700">DECODE &amp; VALIDATE</text>
    <text x="68" y="50" fill="#6B7280" font-family="system-ui, sans-serif" font-size="11">Acknowledge underlying emotions</text>
    <text x="20" y="80" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Identify primary feeling (frustrated, sad, hurt)</text>
    <text x="20" y="100" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Avoid dismissing: "Don't cry / It's nothing"</text>
    <text x="20" y="120" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Validate: "I understand why that felt unfair"</text>
  </g>

  <!-- Step 3: Paraphrase & Mirror -->
  <g transform="translate(40, 280)" filter="url(#cardShadow)">
    <rect width="330" height="140" rx="12" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="15" y="15" width="40" height="40" rx="8" fill="#7C3AED"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">3</text>
    <text x="68" y="34" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="14" font-weight="700">PARAPHRASE &amp; MIRROR</text>
    <text x="68" y="50" fill="#6B7280" font-family="system-ui, sans-serif" font-size="11">Reflect meaning in your own words</text>
    <text x="20" y="80" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Use softeners: "It sounds like you felt..."</text>
    <text x="20" y="100" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Confirm accuracy: "...is that what happened?"</text>
    <text x="20" y="120" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Gives speaker room to clarify thoughts</text>
  </g>

  <!-- Step 4: Support & Collaborate -->
  <g transform="translate(430, 280)" filter="url(#cardShadow)">
    <rect width="330" height="140" rx="12" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="15" y="15" width="40" height="40" rx="8" fill="#7C3AED"/>
    <text x="35" y="41" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">4</text>
    <text x="68" y="34" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="14" font-weight="700">SUPPORT &amp; COLLABORATE</text>
    <text x="68" y="50" fill="#6B7280" font-family="system-ui, sans-serif" font-size="11">Offer partnership without imposing</text>
    <text x="20" y="80" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Ask: "How can I support you right now?"</text>
    <text x="20" y="100" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Distinguish between needing venting vs advice</text>
    <text x="20" y="120" fill="#374151" font-family="system-ui, sans-serif" font-size="11">• Solidifies interpersonal bond</text>
  </g>
</svg>"""


# =============================================================================
# SVG 3: Lesson 3 — Negotiation Skills: The Win-Win Consensus & BATNA Matrix
# =============================================================================
SVG_NEGOTIATION_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l3HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#065F46"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l3HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE WIN-WIN NEGOTIATION ARCHITECTURE</text>
  <text x="400" y="65" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Balancing Interests, Exploring ZOPA, and Securing BATNA</text>

  <!-- Column 1: Party A Interests -->
  <g transform="translate(35, 100)" filter="url(#cardShadow)">
    <rect width="210" height="320" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <rect x="15" y="15" width="180" height="32" rx="6" fill="#047857"/>
    <text x="105" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PARTY A (e.g. Buyer)</text>
    
    <text x="15" y="70" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Underlying Interests:</text>
    <text x="15" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Affordable purchase cost</text>
    <text x="15" y="110" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Reliable delivery date</text>
    <text x="15" y="130" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• High product quality</text>

    <rect x="15" y="160" width="180" height="65" rx="8" fill="#FFFFFF" stroke="#059669" stroke-width="1"/>
    <text x="25" y="180" fill="#047857" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Opening Position:</text>
    <text x="25" y="200" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">"I will pay 500 KES."</text>

    <rect x="15" y="240" width="180" height="65" rx="8" fill="#D1FAE5"/>
    <text x="25" y="260" fill="#065F46" font-family="system-ui, sans-serif" font-size="10" font-weight="700">BATNA (Fallback):</text>
    <text x="25" y="280" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">Buy from alternative vendor</text>
    <text x="25" y="295" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">at 600 KES standard price.</text>
  </g>

  <!-- Column 2: ZOPA & Concessions -->
  <g transform="translate(265, 100)" filter="url(#cardShadow)">
    <rect width="270" height="320" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <rect x="15" y="15" width="240" height="32" rx="6" fill="#1D4ED8"/>
    <text x="135" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ZOPA (Zone of Agreement)</text>
    
    <text x="15" y="70" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Mutual Value Exchange:</text>
    <text x="15" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Active Listening &amp; Empathy</text>
    <text x="15" y="110" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Conditional Concessions ("If you...")</text>
    <text x="15" y="130" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Trade-offs (Price vs Volume/Time)</text>

    <rect x="15" y="160" width="240" height="145" rx="8" fill="#1E3A8A"/>
    <text x="25" y="185" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Win-Win Consensus Outcome:</text>
    <text x="25" y="210" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">"We agree on 550 KES with free</text>
    <text x="25" y="228" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">delivery if you buy 3 units."</text>
    <text x="25" y="255" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">✔ Both parties gain value</text>
    <text x="25" y="275" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">✔ Relationship preserved</text>
  </g>

  <!-- Column 3: Party B Interests -->
  <g transform="translate(555, 100)" filter="url(#cardShadow)">
    <rect width="210" height="320" rx="12" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <rect x="15" y="15" width="180" height="32" rx="6" fill="#B45309"/>
    <text x="105" y="36" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PARTY B (e.g. Seller)</text>
    
    <text x="15" y="70" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Underlying Interests:</text>
    <text x="15" y="90" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Fair profit margin</text>
    <text x="15" y="110" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Bulk inventory clearance</text>
    <text x="15" y="130" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Long-term customer loyalty</text>

    <rect x="15" y="160" width="180" height="65" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="1"/>
    <text x="25" y="180" fill="#B45309" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Opening Position:</text>
    <text x="25" y="200" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">"Price is 650 KES."</text>

    <rect x="15" y="240" width="180" height="65" rx="8" fill="#FDE68A"/>
    <text x="25" y="260" fill="#78350F" font-family="system-ui, sans-serif" font-size="10" font-weight="700">BATNA (Fallback):</text>
    <text x="25" y="280" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">Keep item on shelf for</text>
    <text x="25" y="295" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">regular market traffic.</text>
  </g>
</svg>"""


# =============================================================================
# SVG 4: Lesson 4 — Job Interview STAR Method & Delivery Pyramid
# =============================================================================
SVG_INTERVIEW_STAR_METHOD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l4HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l4HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">JOB &amp; ACADEMIC INTERVIEW: THE STAR ANSWER METHOD</text>
  <text x="400" y="65" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Structuring Competency Answers with Evidence, Clarity, and Impact</text>

  <!-- S -->
  <g transform="translate(35, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <circle cx="82" cy="50" r="30" fill="#2563EB"/>
    <text x="82" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="24" font-weight="800" text-anchor="middle">S</text>
    
    <text x="82" y="110" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SITUATION</text>
    <rect x="12" y="130" width="141" height="175" rx="8" fill="#FFFFFF"/>
    <text x="20" y="155" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Set the Context:</text>
    <text x="20" y="175" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• When &amp; where</text>
    <text x="20" y="195" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Specific project/role</text>
    <text x="20" y="225" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Example:</text>
    <text x="20" y="245" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"Last year as class</text>
    <text x="20" y="260" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">prefect, textbook</text>
    <text x="20" y="275" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">losses rose by 20%."</text>
  </g>

  <!-- T -->
  <g transform="translate(225, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <circle cx="82" cy="50" r="30" fill="#D97706"/>
    <text x="82" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="24" font-weight="800" text-anchor="middle">T</text>
    
    <text x="82" y="110" fill="#92400E" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">TASK</text>
    <rect x="12" y="130" width="141" height="175" rx="8" fill="#FFFFFF"/>
    <text x="20" y="155" fill="#78350F" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Define the Goal:</text>
    <text x="20" y="175" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• What needed doing</text>
    <text x="20" y="195" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Expected standard</text>
    <text x="20" y="225" fill="#78350F" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Example:</text>
    <text x="20" y="245" fill="#B45309" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"My task was to build</text>
    <text x="20" y="260" fill="#B45309" font-family="system-ui, sans-serif" font-size="9" font-style="italic">a digital tracking sheet</text>
    <text x="20" y="275" fill="#B45309" font-family="system-ui, sans-serif" font-size="9" font-style="italic">for all 45 students."</text>
  </g>

  <!-- A -->
  <g transform="translate(415, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <circle cx="82" cy="50" r="30" fill="#059669"/>
    <text x="82" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="24" font-weight="800" text-anchor="middle">A</text>
    
    <text x="82" y="110" fill="#065F46" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ACTION</text>
    <rect x="12" y="130" width="141" height="175" rx="8" fill="#FFFFFF"/>
    <text x="20" y="155" fill="#047857" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Steps You Took:</text>
    <text x="20" y="175" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Use active 'I' verbs</text>
    <text x="20" y="195" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Show leadership</text>
    <text x="20" y="225" fill="#047857" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Example:</text>
    <text x="20" y="245" fill="#065F46" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"I organized weekly</text>
    <text x="20" y="260" fill="#065F46" font-family="system-ui, sans-serif" font-size="9" font-style="italic">audits and trained two</text>
    <text x="20" y="275" fill="#065F46" font-family="system-ui, sans-serif" font-size="9" font-style="italic">assistant librarians."</text>
  </g>

  <!-- R -->
  <g transform="translate(605, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#FDF2F8" stroke="#EC4899" stroke-width="2"/>
    <circle cx="82" cy="50" r="30" fill="#DB2777"/>
    <text x="82" y="60" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="24" font-weight="800" text-anchor="middle">R</text>
    
    <text x="82" y="110" fill="#9D174D" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">RESULT</text>
    <rect x="12" y="130" width="141" height="175" rx="8" fill="#FFFFFF"/>
    <text x="20" y="155" fill="#BE185D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Quantifiable Impact:</text>
    <text x="20" y="175" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Measurable outcome</text>
    <text x="20" y="195" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Lessons learned</text>
    <text x="20" y="225" fill="#BE185D" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Example:</text>
    <text x="20" y="245" fill="#9D174D" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"We achieved 0%</text>
    <text x="20" y="260" fill="#9D174D" font-family="system-ui, sans-serif" font-size="9" font-style="italic">losses and won school</text>
    <text x="20" y="275" fill="#9D174D" font-family="system-ui, sans-serif" font-size="9" font-style="italic">library commendation."</text>
  </g>
</svg>"""


# =============================================================================
# SVG 5: Lesson 5 — Impromptu Speeches & The PREP Method
# =============================================================================
SVG_IMPROMPTU_PREP_METHOD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l5HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C2D12"/>
      <stop offset="100%" stop-color="#EA580C"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l5HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">IMPROMPTU SPEAKING: THE PREP STRUCTURE ENGINE</text>
  <text x="400" y="65" fill="#FED7AA" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Organizing Thoughts Under Pressure in 30 Seconds</text>

  <!-- P1: Point -->
  <g transform="translate(35, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#FFF7ED" stroke="#F97316" stroke-width="2"/>
    <rect x="15" y="15" width="135" height="35" rx="6" fill="#EA580C"/>
    <text x="82" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">POINT (P)</text>
    
    <circle cx="82" cy="85" r="22" fill="#FDBA74"/>
    <text x="82" y="93" fill="#7C2D12" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">🎯</text>

    <rect x="12" y="125" width="141" height="90" rx="6" fill="#FFFFFF"/>
    <text x="18" y="145" fill="#C2410C" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Clear Stance:</text>
    <text x="18" y="165" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• State core message</text>
    <text x="18" y="185" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• No waffling</text>
    <text x="18" y="205" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Confident hook</text>

    <rect x="12" y="225" width="141" height="80" rx="6" fill="#7C2D12"/>
    <text x="18" y="245" fill="#FED7AA" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Starter Phrase:</text>
    <text x="18" y="265" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"I strongly believe</text>
    <text x="18" y="280" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">tree planting must</text>
    <text x="18" y="295" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">be mandatory."</text>
  </g>

  <!-- R: Reason -->
  <g transform="translate(225, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
    <rect x="15" y="15" width="135" height="35" rx="6" fill="#DC2626"/>
    <text x="82" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">REASON (R)</text>
    
    <circle cx="82" cy="85" r="22" fill="#FCA5A5"/>
    <text x="82" y="93" fill="#7F1D1D" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">💡</text>

    <rect x="12" y="125" width="141" height="90" rx="6" fill="#FFFFFF"/>
    <text x="18" y="145" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Logical 'Why':</text>
    <text x="18" y="165" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Explain the cause</text>
    <text x="18" y="185" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Connect to society</text>
    <text x="18" y="205" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Use 'because'</text>

    <rect x="12" y="225" width="141" height="80" rx="6" fill="#7F1D1D"/>
    <text x="18" y="245" fill="#FECACA" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Starter Phrase:</text>
    <text x="18" y="265" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"Because deforestation</text>
    <text x="18" y="280" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">causes severe soil</text>
    <text x="18" y="295" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">erosion in our county."</text>
  </g>

  <!-- E: Example -->
  <g transform="translate(415, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#F0FDF4" stroke="#22C55E" stroke-width="2"/>
    <rect x="15" y="15" width="135" height="35" rx="6" fill="#16A34A"/>
    <text x="82" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">EXAMPLE (E)</text>
    
    <circle cx="82" cy="85" r="22" fill="#86EFAC"/>
    <text x="82" y="93" fill="#14532D" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">📊</text>

    <rect x="12" y="125" width="141" height="90" rx="6" fill="#FFFFFF"/>
    <text x="18" y="145" fill="#15803D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Concrete Story:</text>
    <text x="18" y="165" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Real-world case</text>
    <text x="18" y="185" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Personal experience</text>
    <text x="18" y="205" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Memorable facts</text>

    <rect x="12" y="225" width="141" height="80" rx="6" fill="#14532D"/>
    <text x="18" y="245" fill="#BBF7D0" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Starter Phrase:</text>
    <text x="18" y="265" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"For example, last term</text>
    <text x="18" y="280" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">our school farm lost</text>
    <text x="18" y="295" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">crops to runoff."</text>
  </g>

  <!-- P2: Point Restated -->
  <g transform="translate(605, 100)" filter="url(#cardShadow)">
    <rect width="165" height="320" rx="12" fill="#F5F3FF" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="15" y="15" width="135" height="35" rx="6" fill="#7C3AED"/>
    <text x="82" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">POINT (P)</text>
    
    <circle cx="82" cy="85" r="22" fill="#C4B5FD"/>
    <text x="82" y="93" fill="#4C1D95" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">🏁</text>

    <rect x="12" y="125" width="141" height="90" rx="6" fill="#FFFFFF"/>
    <text x="18" y="145" fill="#6D28D9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Strong Conclusion:</text>
    <text x="18" y="165" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Reiterate message</text>
    <text x="18" y="185" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Call to action</text>
    <text x="18" y="205" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Final memorable punch</text>

    <rect x="12" y="225" width="141" height="80" rx="6" fill="#4C1D95"/>
    <text x="18" y="245" fill="#DDD6FE" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Starter Phrase:</text>
    <text x="18" y="265" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"Therefore, planting</text>
    <text x="18" y="280" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">trees protects our</text>
    <text x="18" y="295" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">future together."</text>
  </g>
</svg>"""


# =============================================================================
# SVG 6: Lesson 6 — Selective Listening & Noise Filtering Architecture
# =============================================================================
SVG_SELECTIVE_LISTENING_FILTER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l6HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l6HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SELECTIVE LISTENING: SIGNAL vs NOISE FILTERING</text>
  <text x="400" y="65" fill="#99F6E4" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Techniques for Targeted Detail Extraction in Complex Audio Environments</text>

  <!-- Step 1: Pre-Listening Target -->
  <g transform="translate(35, 100)" filter="url(#cardShadow)">
    <rect width="220" height="320" rx="12" fill="#F0FDFA" stroke="#14B8A6" stroke-width="2"/>
    <rect x="15" y="15" width="190" height="35" rx="6" fill="#0D9488"/>
    <text x="110" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. DEFINE TARGET</text>

    <text x="15" y="75" fill="#115E59" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Pre-Listening Prep:</text>
    <text x="15" y="95" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Set specific questions</text>
    <text x="15" y="115" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Identify keywords to hunt</text>
    <text x="15" y="135" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Example: Date, time, price</text>

    <rect x="15" y="160" width="190" height="145" rx="8" fill="#FFFFFF" stroke="#0D9488" stroke-width="1"/>
    <text x="25" y="185" fill="#0F766E" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Target Grid Example:</text>
    <text x="25" y="205" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">🔍 Batch No: [       ]</text>
    <text x="25" y="225" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">🔍 Date:     [       ]</text>
    <text x="25" y="245" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">🔍 Refund:   [       ]</text>
    <text x="25" y="275" fill="#0D9488" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Prepares brain for recognition</text>
  </g>

  <!-- Step 2: Active Acoustic Filter -->
  <g transform="translate(290, 100)" filter="url(#cardShadow)">
    <rect width="220" height="320" rx="12" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
    <rect x="15" y="15" width="190" height="35" rx="6" fill="#DC2626"/>
    <text x="110" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. FILTER OUT NOISE</text>

    <text x="15" y="75" fill="#991B1B" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Ignore Distractors:</text>
    <text x="15" y="95" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Background traffic noise</text>
    <text x="15" y="115" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Speaker throat clearings</text>
    <text x="15" y="135" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Irrelevant side stories</text>

    <rect x="15" y="160" width="190" height="145" rx="8" fill="#7F1D1D"/>
    <text x="25" y="185" fill="#FECACA" font-family="system-ui, sans-serif" font-size="10" font-weight="700">What to Block:</text>
    <text x="25" y="210" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">✖ "By the way, my cousin..."</text>
    <text x="25" y="230" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">✖ "As I was having breakfast..."</text>
    <text x="25" y="260" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Discards filler to preserve</text>
    <text x="25" y="275" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9" font-style="italic">working memory space.</text>
  </g>

  <!-- Step 3: Extract & Note -->
  <g transform="translate(545, 100)" filter="url(#cardShadow)">
    <rect width="220" height="320" rx="12" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
    <rect x="15" y="15" width="190" height="35" rx="6" fill="#059669"/>
    <text x="110" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. EXTRACT SIGNAL</text>

    <text x="15" y="75" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Record Data Points:</text>
    <text x="15" y="95" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Use shorthand symbols</text>
    <text x="15" y="115" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Numbers &amp; proper nouns</text>
    <text x="15" y="135" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Immediate verification</text>

    <rect x="15" y="160" width="190" height="145" rx="8" fill="#064E3B"/>
    <text x="25" y="185" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Verified Output:</text>
    <text x="25" y="210" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">✔ Batch: KF-99</text>
    <text x="25" y="230" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">✔ Mfg Date: Aug 12, 2026</text>
    <text x="25" y="250" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">✔ Refund: 250 KES</text>
    <text x="25" y="280" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="9" font-style="italic">100% precision achieved</text>
  </g>
</svg>"""


# =============================================================================
# SVG 7: Lesson 7 — Phonetics: Diphthongs & Semi-Vowels Gliding Engine
# =============================================================================
SVG_DIPHTHONGS_PHONETICS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l7HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312E81"/>
      <stop offset="100%" stop-color="#4F46E5"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l7HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PHONETICS: DIPHTHONGS &amp; SEMI-VOWELS GLIDE MAP</text>
  <text x="400" y="65" fill="#C7D2FE" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Articulating Smooth Glides Between Vowel Positions</text>

  <!-- Left: Diphthongs /aɪ/ vs /eɪ/ -->
  <g transform="translate(35, 100)" filter="url(#cardShadow)">
    <rect width="345" height="320" rx="12" fill="#EEF2FF" stroke="#4F46E5" stroke-width="2"/>
    <rect x="15" y="15" width="315" height="35" rx="8" fill="#3730A3"/>
    <text x="172" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">DIPHTHONGS: GLIDING VOWELS</text>

    <!-- /aɪ/ -->
    <rect x="15" y="65" width="315" height="115" rx="8" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="25" y="90" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="800">/aɪ/ : Open Front ➔ Close Front</text>
    <text x="25" y="110" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Starts with open mouth /a/ and glides smoothly to /ɪ/</text>
    <text x="25" y="130" fill="#4338CA" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Word Examples: <tspan font-style="italic" font-weight="400">b<tspan font-weight="700" fill="#1D4ED8">uy</tspan>, t<tspan font-weight="700" fill="#1D4ED8">ie</tspan>, f<tspan font-weight="700" fill="#1D4ED8">i</tspan>ne, h<tspan font-weight="700" fill="#1D4ED8">i</tspan>ke, l<tspan font-weight="700" fill="#1D4ED8">i</tspan>fe</tspan></text>
    <text x="25" y="150" fill="#047857" font-family="system-ui, sans-serif" font-size="9.5">Contrast Pair: <tspan font-style="italic">bite /baɪt/ vs bait /beɪt/</tspan></text>

    <!-- /eɪ/ -->
    <rect x="15" y="190" width="315" height="115" rx="8" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="25" y="215" fill="#312E81" font-family="system-ui, sans-serif" font-size="14" font-weight="800">/eɪ/ : Mid Front ➔ Close Front</text>
    <text x="25" y="235" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Starts with mid vowel /e/ and glides smoothly up to /ɪ/</text>
    <text x="25" y="255" fill="#4338CA" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Word Examples: <tspan font-style="italic" font-weight="400">b<tspan font-weight="700" fill="#1D4ED8">ai</tspan>t, p<tspan font-weight="700" fill="#1D4ED8">ay</tspan>, m<tspan font-weight="700" fill="#1D4ED8">a</tspan>ke, tr<tspan font-weight="700" fill="#1D4ED8">ai</tspan>n, g<tspan font-weight="700" fill="#1D4ED8">a</tspan>te</tspan></text>
    <text x="25" y="275" fill="#047857" font-family="system-ui, sans-serif" font-size="9.5">Contrast Pair: <tspan font-style="italic">pain /peɪn/ vs pine /paɪn/</tspan></text>
  </g>

  <!-- Right: Semi-Vowels /j/ & /w/ -->
  <g transform="translate(420, 100)" filter="url(#cardShadow)">
    <rect width="345" height="320" rx="12" fill="#FDF4FF" stroke="#C026D3" stroke-width="2"/>
    <rect x="15" y="15" width="315" height="35" rx="8" fill="#A21CAF"/>
    <text x="172" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SEMI-VOWELS: /j/ AND /w/</text>

    <!-- /j/ -->
    <rect x="15" y="65" width="315" height="115" rx="8" fill="#FFFFFF" stroke="#F0ABFC" stroke-width="1"/>
    <text x="25" y="90" fill="#701A75" font-family="system-ui, sans-serif" font-size="14" font-weight="800">/j/ : Palatal Glide (as in 'yes')</text>
    <text x="25" y="110" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Tongue raises toward hard palate without contact</text>
    <text x="25" y="130" fill="#86198F" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Word Examples: <tspan font-style="italic" font-weight="400"><tspan font-weight="700" fill="#C026D3">y</tspan>arn, <tspan font-weight="700" fill="#C026D3">y</tspan>ellow, <tspan font-weight="700" fill="#C026D3">y</tspan>outh, <tspan font-weight="700" fill="#C026D3">y</tspan>ear</tspan></text>
    <text x="25" y="150" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="9.5">Avoid Confusion: <tspan font-style="italic">year /jɪə/ vs ear /ɪə/</tspan></text>

    <!-- /w/ -->
    <rect x="15" y="190" width="315" height="115" rx="8" fill="#FFFFFF" stroke="#F0ABFC" stroke-width="1"/>
    <text x="25" y="215" fill="#701A75" font-family="system-ui, sans-serif" font-size="14" font-weight="800">/w/ : Labio-Velar Glide (as in 'wet')</text>
    <text x="25" y="235" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">Lips round into circle while tongue back raises</text>
    <text x="25" y="255" fill="#86198F" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Word Examples: <tspan font-style="italic" font-weight="400"><tspan font-weight="700" fill="#C026D3">w</tspan>est, <tspan font-weight="700" fill="#C026D3">w</tspan>ind, <tspan font-weight="700" fill="#C026D3">w</tspan>ater, <tspan font-weight="700" fill="#C026D3">w</tspan>ork</tspan></text>
    <text x="25" y="275" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="9.5">Avoid Confusion: <tspan font-style="italic">wet /wet/ vs vet /vet/</tspan></text>
  </g>
</svg>"""


# =============================================================================
# SVG 8: Lesson 8 — Sentence Stress & Question Tag Intonation Contours
# =============================================================================
SVG_STRESS_INTONATION_MAP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="l8HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#l8HeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SENTENCE STRESS &amp; QUESTION TAG INTONATION</text>
  <text x="400" y="65" fill="#BAE6FD" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Music of Spoken English: Pitch Contours and Emphatic Rhythms</text>

  <!-- Left: Falling Intonation ⤵ (Certainty) -->
  <g transform="translate(35, 100)" filter="url(#cardShadow)">
    <rect width="345" height="320" rx="12" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>
    <rect x="15" y="15" width="315" height="35" rx="8" fill="#15803D"/>
    <text x="172" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">FALLING INTONATION (⤵) : CERTAINTY</text>

    <!-- Pitch curve visualization -->
    <rect x="15" y="65" width="315" height="85" rx="8" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1"/>
    <path d="M40 95 Q 160 85 280 130" fill="none" stroke="#16A34A" stroke-width="4" stroke-linecap="round"/>
    <polygon points="285,130 273,122 277,135" fill="#16A34A"/>
    <text x="172" y="145" fill="#14532D" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Pitch Drops at the Tag (Expecting Agreement)</text>

    <!-- Details -->
    <rect x="15" y="165" width="315" height="140" rx="8" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1"/>
    <text x="25" y="185" fill="#14532D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Speaker Mindset:</text>
    <text x="25" y="205" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Speaker is confident and sure of the fact.</text>
    <text x="25" y="225" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Does not expect contradictory information.</text>
    <text x="25" y="255" fill="#15803D" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Model Sentence:</text>
    <text x="25" y="275" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="10" font-style="italic">"We won the tournament trophy, <tspan font-weight="700" fill="#15803D">didn't we? ⤵</tspan>"</text>
    <text x="25" y="295" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9">Expected Response: "Yes, we did!"</text>
  </g>

  <!-- Right: Rising Intonation ⤴ (Uncertainty / Query) -->
  <g transform="translate(420, 100)" filter="url(#cardShadow)">
    <rect width="345" height="320" rx="12" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
    <rect x="15" y="15" width="315" height="35" rx="8" fill="#B45309"/>
    <text x="172" y="38" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RISING INTONATION (⤴) : UNCERTAINTY</text>

    <!-- Pitch curve visualization -->
    <rect x="15" y="65" width="315" height="85" rx="8" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1"/>
    <path d="M40 130 Q 160 125 280 85" fill="none" stroke="#D97706" stroke-width="4" stroke-linecap="round"/>
    <polygon points="285,85 277,97 273,84" fill="#D97706"/>
    <text x="172" y="145" fill="#78350F" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Pitch Rises at the Tag (Genuinely Asking)</text>

    <!-- Details -->
    <rect x="15" y="165" width="315" height="140" rx="8" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1"/>
    <text x="25" y="185" fill="#78350F" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Speaker Mindset:</text>
    <text x="25" y="205" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Speaker is doubtful or checking memory.</text>
    <text x="25" y="225" fill="#374151" font-family="system-ui, sans-serif" font-size="10">• Invites listener to confirm or correct truth.</text>
    <text x="25" y="255" fill="#B45309" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Model Sentence:</text>
    <text x="25" y="275" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="10" font-style="italic">"The bus leaves at four o'clock, <tspan font-weight="700" fill="#B45309">doesn't it? ⤴</tspan>"</text>
    <text x="25" y="295" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9">Expected Response: "Yes, it leaves at 4:00." / "No, at 4:30."</text>
  </g>
</svg>"""
