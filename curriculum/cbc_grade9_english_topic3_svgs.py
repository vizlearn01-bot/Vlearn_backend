"""
VLearn CBC Grade 9 English — Topic 3: Grammar in Use
Custom Responsive Vector SVGs for Lessons 1 to 8 (Source Lessons 9 to 16)
"""

# =============================================================================
# SVG 1: Lesson 1 (Lesson 9) — Gender-Neutral Language Matrix & Pronoun Agreement
# =============================================================================
SVG_GENDER_NEUTRAL_LANGUAGE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="gHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4338CA"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="biasedCardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <linearGradient id="neutralCardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <linearGradient id="ruleGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#gHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">GENDER-NEUTRAL LANGUAGE TRANSFORMATION</text>
  <text x="400" y="64" fill="#E0E7FF" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Promoting Inclusivity, Neutral Occupational Titles &amp; Singular "They"</text>

  <!-- Side-by-Side Comparison -->
  <!-- Left: Biased Forms -->
  <g transform="translate(25, 100)" filter="url(#cardShadow)">
    <rect width="230" height="330" rx="12" fill="url(#biasedCardGrad)" stroke="#EF4444" stroke-width="2"/>
    <rect x="15" y="14" width="200" height="32" rx="8" fill="#DC2626"/>
    <text x="115" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">❌ GENDER-BIASED FORMS</text>
    
    <rect x="15" y="60" width="200" height="48" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="80" fill="#991B1B" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Policeman / Fireman</text>
    <text x="25" y="98" fill="#6B7280" font-family="system-ui, sans-serif" font-size="10.5">Assumes male occupancy</text>

    <rect x="15" y="120" width="200" height="48" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="140" fill="#991B1B" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Chairman / Spokesman</text>
    <text x="25" y="158" fill="#6B7280" font-family="system-ui, sans-serif" font-size="10.5">Excludes female leadership</text>

    <rect x="15" y="180" width="200" height="48" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="200" fill="#991B1B" font-family="system-ui, sans-serif" font-size="12" font-weight="700">"Every teacher must bring his"</text>
    <text x="25" y="218" fill="#6B7280" font-family="system-ui, sans-serif" font-size="10.5">Generic masculine pronoun</text>

    <rect x="15" y="240" width="200" height="70" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="260" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Impact on Society:</text>
    <text x="25" y="280" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Marginalizes female professionals</text>
    <text x="25" y="298" fill="#4B5563" font-family="system-ui, sans-serif" font-size="10">• Reinforces outdated gender roles</text>
  </g>

  <!-- Arrow Indicator -->
  <g transform="translate(265, 235)">
    <circle cx="20" cy="20" r="18" fill="#6366F1"/>
    <path d="M12 20 L24 20 M20 14 L26 20 L20 26" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Middle: Neutral Alternatives -->
  <g transform="translate(315, 100)" filter="url(#cardShadow)">
    <rect width="230" height="330" rx="12" fill="url(#neutralCardGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="15" y="14" width="200" height="32" rx="8" fill="#059669"/>
    <text x="115" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">✓ INCLUSIVE ALTERNATIVES</text>
    
    <rect x="15" y="60" width="200" height="48" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="80" fill="#065F46" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Police officer / Firefighter</text>
    <text x="25" y="98" fill="#047857" font-family="system-ui, sans-serif" font-size="10.5">Focuses on function, not sex</text>

    <rect x="15" y="120" width="200" height="48" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="140" fill="#065F46" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Chairperson / Spokesperson</text>
    <text x="25" y="158" fill="#047857" font-family="system-ui, sans-serif" font-size="10.5">Encompasses all leaders</text>

    <rect x="15" y="180" width="200" height="48" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="200" fill="#065F46" font-family="system-ui, sans-serif" font-size="12" font-weight="700">"Teachers must bring their..."</text>
    <text x="25" y="218" fill="#047857" font-family="system-ui, sans-serif" font-size="10.5">Singular 'they' / pluralization</text>

    <rect x="15" y="240" width="200" height="70" rx="6" fill="#FFFFFF" fill-opacity="0.9"/>
    <text x="25" y="260" fill="#047857" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Pedagogical Benefit:</text>
    <text x="25" y="280" fill="#065F46" font-family="system-ui, sans-serif" font-size="10">• Promotes equity and respect</text>
    <text x="25" y="298" fill="#065F46" font-family="system-ui, sans-serif" font-size="10">• Standard in modern professional texts</text>
  </g>

  <!-- Right: Grammar Rule - Singular "They" Agreement -->
  <g transform="translate(560, 100)" filter="url(#cardShadow)">
    <rect width="215" height="330" rx="12" fill="url(#ruleGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="12" y="14" width="191" height="32" rx="8" fill="#2563EB"/>
    <text x="107" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">SINGULAR "THEY" RULES</text>

    <rect x="12" y="60" width="191" height="90" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="80" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Verb Agreement Rule:</text>
    <text x="20" y="98" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">Even when referring to a</text>
    <text x="20" y="114" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10"><tspan font-weight="700">single person</tspan>, "they" takes</text>
    <text x="20" y="130" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10">a <tspan fill="#DC2626" font-weight="700">plural verb</tspan> form!</text>

    <rect x="12" y="160" width="191" height="70" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="180" fill="#DC2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">❌ "The doctor is ready; they is..."</text>
    <text x="20" y="200" fill="#059669" font-family="system-ui, sans-serif" font-size="10" font-weight="700">✓ "The doctor is ready; they ARE..."</text>
    <text x="20" y="218" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">(They + are / They + have / They + go)</text>

    <rect x="12" y="240" width="191" height="70" rx="6" fill="#EFF6FF"/>
    <text x="20" y="260" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Pro-Tip for Precision:</text>
    <text x="20" y="278" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">Use plural antecedents where</text>
    <text x="20" y="294" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">possible: "Consumers... they..."</text>
  </g>
</svg>"""

# =============================================================================
# SVG 2: Lesson 2 (Lesson 10) — Noun Suffixes & Quantifier Distribution Matrix
# =============================================================================
SVG_NOUN_FORMATION_QUANTIFIERS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="nHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>
    <linearGradient id="suffixGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F5F3FF"/>
      <stop offset="100%" stop-color="#EDE9FE"/>
    </linearGradient>
    <linearGradient id="countGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="uncountGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#FDE68A"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#nHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">NOUN FORMATION &amp; QUANTIFIER DISTRIBUTION</text>
  <text x="400" y="64" fill="#D1FAE5" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Derivational Suffixes (-ment, -tion, -ness) and Countable vs. Non-Count Pairings</text>

  <!-- Left: Suffix Derivation Engine -->
  <g transform="translate(25, 100)" filter="url(#cardShadow)">
    <rect width="260" height="330" rx="12" fill="url(#suffixGrad)" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="15" y="14" width="230" height="32" rx="8" fill="#7C3AED"/>
    <text x="130" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">DERIVATIONAL SUFFIXES</text>

    <!-- Suffix 1 -->
    <rect x="15" y="60" width="230" height="65" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="80" fill="#6D28D9" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Verb + -ment → Noun</text>
    <text x="25" y="98" fill="#374151" font-family="system-ui, sans-serif" font-size="11">Employ + <tspan fill="#7C3AED" font-weight="700">-ment</tspan> = <tspan font-weight="700">Employment</tspan></text>
    <text x="25" y="114" fill="#6B7280" font-family="system-ui, sans-serif" font-size="10">Develop → Development | Agree → Agreement</text>

    <!-- Suffix 2 -->
    <rect x="15" y="135" width="230" height="65" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="155" fill="#6D28D9" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Verb + -tion/-ation → Noun</text>
    <text x="25" y="173" fill="#374151" font-family="system-ui, sans-serif" font-size="11">Invent + <tspan fill="#7C3AED" font-weight="700">-tion</tspan> = <tspan font-weight="700">Invention</tspan></text>
    <text x="25" y="189" fill="#6B7280" font-family="system-ui, sans-serif" font-size="10">Inform → Information | Educate → Education</text>

    <!-- Suffix 3 -->
    <rect x="15" y="210" width="230" height="65" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="230" fill="#6D28D9" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Adj/Verb + -ness → Noun</text>
    <text x="25" y="248" fill="#374151" font-family="system-ui, sans-serif" font-size="11">Dark + <tspan fill="#7C3AED" font-weight="700">-ness</tspan> = <tspan font-weight="700">Darkness</tspan></text>
    <text x="25" y="264" fill="#6B7280" font-family="system-ui, sans-serif" font-size="10">Kind → Kindness | Aware → Awareness</text>

    <rect x="15" y="285" width="230" height="30" rx="6" fill="#EDE9FE"/>
    <text x="130" y="304" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">💡 Suffix changes lexical category</text>
  </g>

  <!-- Right: 3-Column Quantifier Chart -->
  <g transform="translate(305, 100)" filter="url(#cardShadow)">
    <rect width="470" height="330" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    
    <!-- Top banner -->
    <rect x="12" y="12" width="446" height="34" rx="8" fill="#0F172A"/>
    <text x="235" y="34" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">QUANTIFIER COMPATIBILITY MATRIX</text>

    <!-- Column 1: Countable Only -->
    <rect x="15" y="56" width="138" height="258" rx="8" fill="url(#countGrad)" stroke="#3B82F6" stroke-width="1.5"/>
    <rect x="22" y="64" width="124" height="24" rx="4" fill="#2563EB"/>
    <text x="84" y="80" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">COUNTABLE</text>
    
    <text x="28" y="110" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Many</text>
    <text x="28" y="128" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">many planets</text>
    <text x="28" y="152" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• A few / Few</text>
    <text x="28" y="170" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">a few discoveries</text>
    <text x="28" y="194" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Several</text>
    <text x="28" y="212" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">several stars</text>
    <text x="28" y="236" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• A number of</text>
    <text x="28" y="254" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">a number of tests</text>

    <!-- Column 2: Dual Use -->
    <rect x="163" y="56" width="144" height="258" rx="8" fill="#F1F5F9" stroke="#64748B" stroke-width="1.5"/>
    <rect x="171" y="64" width="128" height="24" rx="4" fill="#475569"/>
    <text x="235" y="80" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">BOTH (DUAL)</text>

    <text x="175" y="110" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Some</text>
    <text x="175" y="128" fill="#64748B" font-family="system-ui, sans-serif" font-size="9.5">some tools / data</text>
    <text x="175" y="152" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Any</text>
    <text x="175" y="170" fill="#64748B" font-family="system-ui, sans-serif" font-size="9.5">any books / water</text>
    <text x="175" y="194" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• A lot of / Lots of</text>
    <text x="175" y="212" fill="#64748B" font-family="system-ui, sans-serif" font-size="9.5">a lot of ideas / fuel</text>
    <text x="175" y="236" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Plenty of</text>
    <text x="175" y="254" fill="#64748B" font-family="system-ui, sans-serif" font-size="9.5">plenty of rocks / sand</text>

    <!-- Column 3: Uncountable Only -->
    <rect x="317" y="56" width="138" height="258" rx="8" fill="url(#uncountGrad)" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="324" y="64" width="124" height="24" rx="4" fill="#D97706"/>
    <text x="386" y="80" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">UNCOUNTABLE</text>

    <text x="330" y="110" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Much</text>
    <text x="330" y="128" fill="#78350F" font-family="system-ui, sans-serif" font-size="9.5">much energy</text>
    <text x="330" y="152" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• A little / Little</text>
    <text x="330" y="170" fill="#78350F" font-family="system-ui, sans-serif" font-size="9.5">a little patience</text>
    <text x="330" y="194" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• A bit of</text>
    <text x="330" y="212" fill="#78350F" font-family="system-ui, sans-serif" font-size="9.5">a bit of research</text>
    <text x="330" y="236" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• A great deal of</text>
    <text x="330" y="254" fill="#78350F" font-family="system-ui, sans-serif" font-size="9.5">a great deal of space</text>
  </g>
</svg>"""

# =============================================================================
# SVG 3: Lesson 3 (Lesson 11) — Relative & Interrogative Pronouns Architecture
# =============================================================================
SVG_PRONOUNS_RELATIVE_INTERROGATIVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="pHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0EA5E9"/>
    </linearGradient>
    <linearGradient id="relGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4"/>
      <stop offset="100%" stop-color="#DCFCE7"/>
    </linearGradient>
    <linearGradient id="intGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#pHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">RELATIVE &amp; INTERROGATIVE PRONOUNS</text>
  <text x="400" y="64" fill="#E0F2FE" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Connecting Clauses vs. Constructing Focused Inquiries (Marine Life Focus)</text>

  <!-- Left: Relative Pronouns as Clause Bridges -->
  <g transform="translate(25, 100)" filter="url(#cardShadow)">
    <rect width="360" height="330" rx="12" fill="url(#relGrad)" stroke="#16A34A" stroke-width="2"/>
    <rect x="15" y="14" width="330" height="32" rx="8" fill="#15803D"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🌉 RELATIVE PRONOUNS (CLAUSE BRIDGES)</text>

    <!-- Row 1: Who / Whom -->
    <rect x="15" y="58" width="330" height="52" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="78" fill="#15803D" font-family="system-ui, sans-serif" font-size="12" font-weight="700">WHO / WHOM (Humans)</text>
    <text x="25" y="96" fill="#374151" font-family="system-ui, sans-serif" font-size="10.5">"The scientist <tspan fill="#15803D" font-weight="700">who</tspan> tags dolphins..." [Subject: Who | Object: Whom]</text>

    <!-- Row 2: Which / That -->
    <rect x="15" y="118" width="330" height="52" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="138" fill="#15803D" font-family="system-ui, sans-serif" font-size="12" font-weight="700">WHICH / THAT (Animals &amp; Inanimate Objects)</text>
    <text x="25" y="156" fill="#374151" font-family="system-ui, sans-serif" font-size="10.5">"We saw a whale <tspan fill="#15803D" font-weight="700">which</tspan> breached near the coral reef."</text>

    <!-- Row 3: Whose -->
    <rect x="15" y="178" width="330" height="52" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="198" fill="#15803D" font-family="system-ui, sans-serif" font-size="12" font-weight="700">WHOSE (Possession)</text>
    <text x="25" y="216" fill="#374151" font-family="system-ui, sans-serif" font-size="10.5">"Fishers <tspan fill="#15803D" font-weight="700">whose</tspan> nets were damaged received compensation."</text>

    <!-- Syntax Blueprint -->
    <rect x="15" y="240" width="330" height="75" rx="6" fill="#DCFCE7"/>
    <text x="25" y="260" fill="#166534" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Sentence Coupling Formula:</text>
    <text x="25" y="278" fill="#14532D" font-family="system-ui, sans-serif" font-size="10">[Main Clause] + [Relative Pronoun] + [Subordinate Clause]</text>
    <text x="25" y="296" fill="#15803D" font-family="system-ui, sans-serif" font-size="10">Eliminates repetitive nouns to create smooth, complex syntax.</text>
  </g>

  <!-- Right: Interrogative Pronouns as Question Starters -->
  <g transform="translate(415, 100)" filter="url(#cardShadow)">
    <rect width="360" height="330" rx="12" fill="url(#intGrad)" stroke="#2563EB" stroke-width="2"/>
    <rect x="15" y="14" width="330" height="32" rx="8" fill="#1D4ED8"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">❓ INTERROGATIVE PRONOUNS (INQUIRIES)</text>

    <!-- Row 1: Who / Whom -->
    <rect x="15" y="58" width="330" height="52" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="78" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">WHO / WHOM (Asking about Person)</text>
    <text x="25" y="96" fill="#374151" font-family="system-ui, sans-serif" font-size="10.5">"<tspan fill="#1D4ED8" font-weight="700">Who</tspan> authorized the marine protected area boundary?"</text>

    <!-- Row 2: Which -->
    <rect x="15" y="118" width="330" height="52" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="138" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">WHICH (Selecting from Specific Set)</text>
    <text x="25" y="156" fill="#374151" font-family="system-ui, sans-serif" font-size="10.5">"<tspan fill="#1D4ED8" font-weight="700">Which</tspan> of these two turtle species is critically endangered?"</text>

    <!-- Row 3: What & Whose -->
    <rect x="15" y="178" width="330" height="52" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="198" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">WHAT (General) / WHOSE (Ownership)</text>
    <text x="25" y="216" fill="#374151" font-family="system-ui, sans-serif" font-size="10.5">"<tspan fill="#1D4ED8" font-weight="700">What</tspan> threatens coral reefs?" | "<tspan fill="#1D4ED8" font-weight="700">Whose</tspan> boat is patrolling?"</text>

    <!-- Common Error Alert -->
    <rect x="15" y="240" width="330" height="75" rx="6" fill="#DBEAFE"/>
    <text x="25" y="260" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Key Distinguishing Principle:</text>
    <text x="25" y="278" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="10">• Interrogatives stand at sentence front to ask a direct query.</text>
    <text x="25" y="296" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="10">• Relatives sit inside a sentence linking back to an antecedent.</text>
  </g>
</svg>"""

# =============================================================================
# SVG 4: Lesson 4 (Lesson 12) — DOSASCOMP Adjective Order & Adverb Comparison
# =============================================================================
SVG_DOSASCOMP_ADJECTIVES_ADVERBS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="dHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#dHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">DOSASCOMP ADJECTIVE ORDER &amp; ADVERB DEGREES</text>
  <text x="400" y="64" fill="#FEF3C7" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">The 9-Step Sequential Descriptive Formula &amp; Positive/Comparative/Superlative Adverbs</text>

  <!-- Top Area: DOSASCOMP 9-Pillars -->
  <g transform="translate(25, 95)" filter="url(#cardShadow)">
    <rect width="750" height="180" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="15" y="10" width="720" height="26" rx="6" fill="#78350F"/>
    <text x="375" y="28" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE STANDARD ADJECTIVE SEQUENCE: D-O-S-A-S-C-O-M-P</text>

    <!-- 9 Micro-Cards -->
    <!-- D -->
    <g transform="translate(15, 45)">
      <rect width="74" height="68" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>
      <text x="37" y="20" fill="#92400E" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">D</text>
      <text x="37" y="36" fill="#78350F" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Determiner</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">a, the, three</text>
    </g>
    <!-- O -->
    <g transform="translate(95, 45)">
      <rect width="74" height="68" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="1"/>
      <text x="37" y="20" fill="#065F46" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">O</text>
      <text x="37" y="36" fill="#047857" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Opinion</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">beautiful, fine</text>
    </g>
    <!-- S -->
    <g transform="translate(175, 45)">
      <rect width="74" height="68" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1"/>
      <text x="37" y="20" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">S</text>
      <text x="37" y="36" fill="#2563EB" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Size</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">large, tiny, tall</text>
    </g>
    <!-- A -->
    <g transform="translate(255, 45)">
      <rect width="74" height="68" rx="6" fill="#FDF4FF" stroke="#C084FC" stroke-width="1"/>
      <text x="37" y="20" fill="#6B21A8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">A</text>
      <text x="37" y="36" fill="#9333EA" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Age</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">new, ancient, old</text>
    </g>
    <!-- S -->
    <g transform="translate(335, 45)">
      <rect width="74" height="68" rx="6" fill="#FFF1F2" stroke="#FB7185" stroke-width="1"/>
      <text x="37" y="20" fill="#9F1239" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">S</text>
      <text x="37" y="36" fill="#E11D48" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Shape</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">round, square</text>
    </g>
    <!-- C -->
    <g transform="translate(415, 45)">
      <rect width="74" height="68" rx="6" fill="#F0FDF4" stroke="#4ADE80" stroke-width="1"/>
      <text x="37" y="20" fill="#166534" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">C</text>
      <text x="37" y="36" fill="#16A34A" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Color</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">red, brown, blue</text>
    </g>
    <!-- O -->
    <g transform="translate(495, 45)">
      <rect width="74" height="68" rx="6" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1"/>
      <text x="37" y="20" fill="#334155" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">O</text>
      <text x="37" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Origin</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">Kenyan, French</text>
    </g>
    <!-- M -->
    <g transform="translate(575, 45)">
      <rect width="74" height="68" rx="6" fill="#FEFCE8" stroke="#EAB308" stroke-width="1"/>
      <text x="37" y="20" fill="#854D0E" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">M</text>
      <text x="37" y="36" fill="#CA8A04" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Material</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">wooden, silk</text>
    </g>
    <!-- P -->
    <g transform="translate(655, 45)">
      <rect width="74" height="68" rx="6" fill="#F1F5F9" stroke="#64748B" stroke-width="1"/>
      <text x="37" y="20" fill="#0F172A" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">P</text>
      <text x="37" y="36" fill="#334155" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Purpose</text>
      <text x="37" y="52" fill="#4B5563" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">writing, sports</text>
    </g>

    <!-- Example Banner -->
    <rect x="15" y="125" width="720" height="42" rx="6" fill="#FEF3C7"/>
    <text x="25" y="145" fill="#92400E" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Master Example:</text>
    <text x="25" y="160" fill="#78350F" font-family="system-ui, sans-serif" font-size="10.5">"A (D) beautiful (O) small (S) old (A) rectangular (S) brown (C) French (O) wooden (M) writing (P) desk."</text>
  </g>

  <!-- Bottom Area: Adverb Comparison Degrees -->
  <g transform="translate(25, 290)" filter="url(#cardShadow)">
    <rect width="750" height="145" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="15" y="10" width="720" height="24" rx="4" fill="#0284C7"/>
    <text x="375" y="27" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">ADVERB COMPARISON: REGULAR (-ly) VS. IRREGULAR DEGREES</text>

    <g transform="translate(20, 42)">
      <rect width="225" height="85" rx="6" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1"/>
      <text x="15" y="20" fill="#0369A1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Regular Adverbs (-ly)</text>
      <text x="15" y="38" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Positive: <tspan font-weight="700">clearly</tspan></text>
      <text x="15" y="54" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Comparative: <tspan font-weight="700">more clearly</tspan></text>
      <text x="15" y="70" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Superlative: <tspan font-weight="700">most clearly</tspan></text>
    </g>

    <g transform="translate(262, 42)">
      <rect width="225" height="85" rx="6" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
      <text x="15" y="20" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Irregular: Well / Badly</text>
      <text x="15" y="38" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Positive: <tspan font-weight="700">well / badly</tspan></text>
      <text x="15" y="54" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Comparative: <tspan font-weight="700">better / worse</tspan></text>
      <text x="15" y="70" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Superlative: <tspan font-weight="700">best / worst</tspan></text>
    </g>

    <g transform="translate(505, 42)">
      <rect width="225" height="85" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
      <text x="15" y="20" fill="#15803D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Single-Syllable Adverbs</text>
      <text x="15" y="38" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Positive: <tspan font-weight="700">fast / early</tspan></text>
      <text x="15" y="54" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Comparative: <tspan font-weight="700">faster / earlier</tspan></text>
      <text x="15" y="70" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Superlative: <tspan font-weight="700">fastest / earliest</tspan></text>
    </g>
  </g>
</svg>"""

# =============================================================================
# SVG 5: Lesson 5 (Lesson 13) — Complex Prepositions & Correlative Conjunctions
# =============================================================================
SVG_PREPOSITIONS_CORRELATIVE_CONJUNCTIONS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="cHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>
    <linearGradient id="prepGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="corrGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FDF2F8"/>
      <stop offset="100%" stop-color="#FCE7F3"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#cHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">COMPLEX PREPOSITIONS &amp; CORRELATIVE CONJUNCTIONS</text>
  <text x="400" y="64" fill="#D1FAE5" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Multi-Word Relationship Modifiers &amp; Balanced Parallel Conjunction Pairs</text>

  <!-- Left: Complex Prepositions -->
  <g transform="translate(25, 100)" filter="url(#cardShadow)">
    <rect width="360" height="330" rx="12" fill="url(#prepGrad)" stroke="#2563EB" stroke-width="2"/>
    <rect x="15" y="14" width="330" height="32" rx="8" fill="#1D4ED8"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🔗 COMPLEX PREPOSITIONS (MULTI-WORD)</text>

    <rect x="15" y="56" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="75" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">According to</text>
    <text x="25" y="91" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">"As reported by..." (According to the climatic report...)</text>

    <rect x="15" y="108" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="127" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">In spite of</text>
    <text x="25" y="91" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">"Regardless of / Despite" (In spite of torrential rainfall...)</text>

    <rect x="15" y="160" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="179" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">On account of</text>
    <text x="25" y="195" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">"Because of / Due to" (Cleanups delayed on account of rain)</text>

    <rect x="15" y="212" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="231" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">By means of</text>
    <text x="25" y="247" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">"Via / Using the agency of" (Pumping water by means of solar)</text>

    <rect x="15" y="264" width="330" height="52" rx="6" fill="#DBEAFE"/>
    <text x="25" y="284" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Structural Rule:</text>
    <text x="25" y="302" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9.5">Followed by a noun phrase or gerund (-ing), never a full clause.</text>
  </g>

  <!-- Right: Correlative Conjunction Pairs -->
  <g transform="translate(415, 100)" filter="url(#cardShadow)">
    <rect width="360" height="330" rx="12" fill="url(#corrGrad)" stroke="#DB2777" stroke-width="2"/>
    <rect x="15" y="14" width="330" height="32" rx="8" fill="#BE185D"/>
    <text x="180" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">⚖️ CORRELATIVE CONJUNCTIONS (MATCHED PAIRS)</text>

    <rect x="15" y="56" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="75" fill="#9D174D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Either ... or</text>
    <text x="25" y="91" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">Choice: "We will <tspan font-weight="700">either</tspan> plant trees <tspan font-weight="700">or</tspan> clean wetlands."</text>

    <rect x="15" y="108" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="127" fill="#9D174D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Neither ... nor</text>
    <text x="25" y="143" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">Mutual Exclusion: "<tspan font-weight="700">Neither</tspan> logging <tspan font-weight="700">nor</tspan> poaching is allowed."</text>

    <rect x="15" y="160" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="179" fill="#9D174D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Both ... and</text>
    <text x="25" y="195" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">Inclusion: "<tspan font-weight="700">Both</tspan> the students <tspan font-weight="700">and</tspan> the chiefs joined."</text>

    <rect x="15" y="212" width="330" height="46" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="25" y="231" fill="#9D174D" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Not only ... but also</text>
    <text x="25" y="247" fill="#4B5563" font-family="system-ui, sans-serif" font-size="9.5">Emphasis: "<tspan font-weight="700">Not only</tspan> did they weed <tspan font-weight="700">but also</tspan> watered..."</text>

    <rect x="15" y="264" width="330" height="52" rx="6" fill="#FCE7F3"/>
    <text x="25" y="284" fill="#831843" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Parallelism Rule:</text>
    <text x="25" y="302" fill="#9D174D" font-family="system-ui, sans-serif" font-size="9.5">Both sides must match grammatically (Noun+Noun / Verb+Verb).</text>
  </g>
</svg>"""

# =============================================================================
# SVG 6: Lesson 6 (Lesson 14) — Modal Auxiliaries Spectrum & Nuance Scale
# =============================================================================
SVG_MODAL_AUXILIARIES_SPECTRUM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="mHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>
    <linearGradient id="volGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="35%" stop-color="#3B82F6"/>
      <stop offset="70%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#EF4444"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#mHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">MODAL AUXILIARIES: THE VOLUME KNOB OF INTENT</text>
  <text x="400" y="64" fill="#F3E8FF" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">From Weak Possibility to Polite Permission, Suggestion, and Absolute Obligation</text>

  <!-- Spectrum Bar -->
  <g transform="translate(45, 95)">
    <rect width="710" height="24" rx="12" fill="url(#volGrad)"/>
    <text x="15" y="16" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700">LOW INTENSITY / POSSIBILITY</text>
    <text x="695" y="16" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="end">MAXIMUM OBLIGATION</text>
  </g>

  <!-- 4 Step Columns -->
  <!-- Col 1: Possibility / Weak -->
  <g transform="translate(25, 135)" filter="url(#cardShadow)">
    <rect width="175" height="240" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
    <rect x="12" y="12" width="151" height="28" rx="6" fill="#059669"/>
    <text x="87" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. POSSIBILITY</text>
    
    <text x="87" y="62" fill="#065F46" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Might / May</text>
    
    <rect x="10" y="75" width="155" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="18" y="93" fill="#065F46" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Semantic Nuance:</text>
    <text x="18" y="110" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• 20-50% probability</text>
    <text x="18" y="126" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Speculative / gentle</text>
    <text x="18" y="145" fill="#059669" font-family="system-ui, sans-serif" font-size="9" font-weight="600">"It might rain today."</text>

    <rect x="10" y="170" width="155" height="55" rx="6" fill="#D1FAE5"/>
    <text x="16" y="188" fill="#047857" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Permission Role:</text>
    <text x="16" y="204" fill="#065F46" font-family="system-ui, sans-serif" font-size="8.5">"May I enter?" (Formal)</text>
  </g>

  <!-- Col 2: Ability & Requests -->
  <g transform="translate(215, 135)" filter="url(#cardShadow)">
    <rect width="175" height="240" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
    <rect x="12" y="12" width="151" height="28" rx="6" fill="#2563EB"/>
    <text x="87" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. ABILITY / REQUEST</text>

    <text x="87" y="62" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Can / Could</text>

    <rect x="10" y="75" width="155" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="18" y="93" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Semantic Nuance:</text>
    <text x="18" y="110" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Physical capability</text>
    <text x="18" y="126" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Polite inquiry (Could)</text>
    <text x="18" y="145" fill="#2563EB" font-family="system-ui, sans-serif" font-size="9" font-weight="600">"Could you assist me?"</text>

    <rect x="10" y="170" width="155" height="55" rx="6" fill="#DBEAFE"/>
    <text x="16" y="188" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Capability Role:</text>
    <text x="16" y="204" fill="#1E3A8A" font-family="system-ui, sans-serif" font-size="8.5">"He can swim across."</text>
  </g>

  <!-- Col 3: Advice / Expectation -->
  <g transform="translate(405, 135)" filter="url(#cardShadow)">
    <rect width="175" height="240" rx="10" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="12" y="12" width="151" height="28" rx="6" fill="#D97706"/>
    <text x="87" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. ADVICE / MORAL</text>

    <text x="87" y="62" fill="#92400E" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Should / Ought to</text>

    <rect x="10" y="75" width="155" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="18" y="93" fill="#92400E" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Semantic Nuance:</text>
    <text x="18" y="110" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Recommended action</text>
    <text x="18" y="126" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Moral responsibility</text>
    <text x="18" y="145" fill="#D97706" font-family="system-ui, sans-serif" font-size="9" font-weight="600">"You should plant trees."</text>

    <rect x="10" y="170" width="155" height="55" rx="6" fill="#FDE68A"/>
    <text x="16" y="188" fill="#92400E" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Guidance Role:</text>
    <text x="16" y="204" fill="#78350F" font-family="system-ui, sans-serif" font-size="8.5">Not legally binding.</text>
  </g>

  <!-- Col 4: Absolute Obligation -->
  <g transform="translate(595, 135)" filter="url(#cardShadow)">
    <rect width="175" height="240" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
    <rect x="12" y="12" width="151" height="28" rx="6" fill="#DC2626"/>
    <text x="87" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. OBLIGATION</text>

    <text x="87" y="62" fill="#991B1B" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Must / Have to</text>

    <rect x="10" y="75" width="155" height="85" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="18" y="93" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Semantic Nuance:</text>
    <text x="18" y="110" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Strict legal rule</text>
    <text x="18" y="126" fill="#374151" font-family="system-ui, sans-serif" font-size="9">• Mandatory command</text>
    <text x="18" y="145" fill="#DC2626" font-family="system-ui, sans-serif" font-size="9" font-weight="600">"We must protect water."</text>

    <rect x="10" y="170" width="155" height="55" rx="6" fill="#FECACA"/>
    <text x="16" y="188" fill="#991B1B" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Rule Enforcement:</text>
    <text x="16" y="204" fill="#7F1D1D" font-family="system-ui, sans-serif" font-size="8.5">Violating leads to sanction.</text>
  </g>

  <!-- Golden Syntax Banner -->
  <g transform="translate(25, 385)">
    <rect width="745" height="42" rx="8" fill="#0F172A"/>
    <text x="372" y="26" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">⚡ GOLDEN RULE: Modal + Base Verb (No "to", No "-s", No "-ed") | Never double up ("might will" ❌)</text>
  </g>
</svg>"""

# =============================================================================
# SVG 7: Lesson 7 (Lesson 15) — Present & Past Perfect Timeline Architecture
# =============================================================================
SVG_PERFECT_ASPECTS_TIMELINE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="tHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#tHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PRESENT PERFECT VS. PAST PERFECT TIMELINE</text>
  <text x="400" y="64" fill="#CCFBF1" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Chronological Anchoring &amp; Action Sequencing Architecture (Consumer Context)</text>

  <!-- Top Timeline Container: Present Perfect -->
  <g transform="translate(25, 95)" filter="url(#cardShadow)">
    <rect width="750" height="155" rx="12" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <rect x="15" y="10" width="720" height="26" rx="6" fill="#0F766E"/>
    <text x="375" y="28" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. PRESENT PERFECT (Has / Have + Past Participle) -> Past Action Relevant NOW</text>

    <!-- Visual Timeline Line -->
    <line x1="60" y1="80" x2="680" y2="80" stroke="#CBD5E1" stroke-width="4" stroke-linecap="round"/>
    
    <!-- Marker 1: Unspecified Past Action -->
    <circle cx="220" cy="80" r="14" fill="#0D9488"/>
    <text x="220" y="85" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">1</text>
    <text x="220" y="112" fill="#0F766E" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">"I have lost my receipt"</text>
    <text x="220" y="126" fill="#64748B" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Happened at unspecified past time</text>

    <!-- Connector Wave -->
    <path d="M 235 80 Q 420 40 540 76" fill="none" stroke="#0D9488" stroke-width="2.5" stroke-dasharray="4,4"/>
    <text x="380" y="55" fill="#0D9488" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Direct Present Impact</text>

    <!-- Marker 2: Present Moment (Now) -->
    <circle cx="560" cy="80" r="14" fill="#047857"/>
    <text x="560" y="85" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">NOW</text>
    <text x="560" y="112" fill="#047857" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">"I cannot get a refund today"</text>
    <text x="560" y="126" fill="#64748B" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Present state caused by past action</text>
  </g>

  <!-- Bottom Timeline Container: Past Perfect -->
  <g transform="translate(25, 265)" filter="url(#cardShadow)">
    <rect width="750" height="175" rx="12" fill="#FFFFFF" stroke="#2563EB" stroke-width="1.5"/>
    <rect x="15" y="10" width="720" height="26" rx="6" fill="#1E40AF"/>
    <text x="375" y="28" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. PAST PERFECT (Had + Past Participle) -> Older of Two Completed Past Events</text>

    <!-- Visual Timeline Line -->
    <line x1="60" y1="85" x2="680" y2="85" stroke="#CBD5E1" stroke-width="4" stroke-linecap="round"/>

    <!-- Step 1: Older Past Event -->
    <circle cx="170" cy="85" r="16" fill="#2563EB"/>
    <text x="170" y="90" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">1st</text>
    <text x="170" y="120" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PAST PERFECT (Had + V3)</text>
    <text x="170" y="136" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">"The store <tspan font-weight="700">had closed</tspan>..."</text>
    <text x="170" y="150" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Earlier action completed first</text>

    <!-- Arrow connecting to 2nd past event -->
    <path d="M 205 85 L 395 85 M 385 79 L 398 85 L 385 91" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-linecap="round"/>

    <!-- Step 2: Recent Past Event -->
    <circle cx="430" cy="85" r="16" fill="#3B82F6"/>
    <text x="430" y="90" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">2nd</text>
    <text x="430" y="120" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SIMPLE PAST (V2)</text>
    <text x="430" y="136" fill="#1F2937" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">"...by the time I <tspan font-weight="700">arrived</tspan>."</text>
    <text x="430" y="150" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Later past reference point</text>

    <!-- Step 3: Present Moment (Now) -->
    <circle cx="640" cy="85" r="12" fill="#94A3B8"/>
    <text x="640" y="89" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">NOW</text>
    <text x="640" y="120" fill="#64748B" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Present Day</text>
  </g>
</svg>"""

# =============================================================================
# SVG 8: Lesson 8 (Lesson 16) — Complex Sentences & Reported Speech Engine
# =============================================================================
SVG_REPORTED_SPEECH_ENGINE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="rHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#BE185D"/>
      <stop offset="100%" stop-color="#E11D48"/>
    </linearGradient>
    <linearGradient id="directGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <linearGradient id="indirectGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4"/>
      <stop offset="100%" stop-color="#DCFCE7"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="460" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="20" width="750" height="60" rx="12" fill="url(#rHeaderGrad)" filter="url(#cardShadow)"/>
  <text x="400" y="44" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">REPORTED SPEECH &amp; COMPLEX SENTENCE ENGINE</text>
  <text x="400" y="64" fill="#FFE4E6" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" text-anchor="middle">Direct Quote Deconstruction &amp; Systematic Tense / Pronoun / Time Backshifts</text>

  <!-- Left: Direct Speech Original Quote -->
  <g transform="translate(25, 95)" filter="url(#cardShadow)">
    <rect width="250" height="230" rx="12" fill="url(#directGrad)" stroke="#E11D48" stroke-width="2"/>
    <rect x="15" y="14" width="220" height="32" rx="8" fill="#BE185D"/>
    <text x="125" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">🎙️ DIRECT SPEECH</text>

    <!-- Speech bubble -->
    <rect x="15" y="60" width="220" height="150" rx="8" fill="#FFFFFF" stroke="#FDA4AF" stroke-width="1.5"/>
    <text x="25" y="82" fill="#9F1239" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">The Striker said:</text>
    <text x="25" y="105" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11.5" font-style="italic">" <tspan fill="#BE185D" font-weight="700">I</tspan> <tspan fill="#2563EB" font-weight="700">am playing</tspan></text>
    <text x="25" y="125" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11.5" font-style="italic">in the tournament</text>
    <text x="25" y="145" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11.5" font-style="italic"><tspan fill="#D97706" font-weight="700">tomorrow</tspan>. "</text>

    <text x="25" y="175" fill="#64748B" font-family="system-ui, sans-serif" font-size="9">• Exact spoken quote</text>
    <text x="25" y="192" fill="#64748B" font-family="system-ui, sans-serif" font-size="9">• Enclosed in inverted commas</text>
  </g>

  <!-- Middle: Backshift Transformation Hub -->
  <g transform="translate(290, 95)" filter="url(#cardShadow)">
    <rect width="220" height="230" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="26" rx="6" fill="#334155"/>
    <text x="110" y="27" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SHIFT RULES</text>

    <!-- Shift 1: Pronoun -->
    <rect x="10" y="45" width="200" height="48" rx="6" fill="#FDF2F8"/>
    <text x="16" y="62" fill="#BE185D" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. PRONOUN SHIFT</text>
    <text x="16" y="78" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">"I / We" ➔ <tspan font-weight="700" fill="#BE185D">He / She / They</tspan></text>

    <!-- Shift 2: Tense -->
    <rect x="10" y="100" width="200" height="48" rx="6" fill="#EFF6FF"/>
    <text x="16" y="117" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. TENSE BACKSHIFT</text>
    <text x="16" y="133" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">"am playing" ➔ <tspan font-weight="700" fill="#1D4ED8">was playing</tspan></text>

    <!-- Shift 3: Time -->
    <rect x="10" y="155" width="200" height="60" rx="6" fill="#FEF3C7"/>
    <text x="16" y="172" fill="#B45309" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. TIME ADVERBIAL</text>
    <text x="16" y="188" fill="#374151" font-family="system-ui, sans-serif" font-size="9.5">"tomorrow" ➔ <tspan font-weight="700" fill="#B45309">the next day</tspan></text>
    <text x="16" y="202" fill="#374151" font-family="system-ui, sans-serif" font-size="9">"today" ➔ that day</text>
  </g>

  <!-- Right: Reported Speech Output -->
  <g transform="translate(525, 95)" filter="url(#cardShadow)">
    <rect width="250" height="230" rx="12" fill="url(#indirectGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="15" y="14" width="220" height="32" rx="8" fill="#059669"/>
    <text x="125" y="35" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">📝 REPORTED SPEECH</text>

    <!-- Output Box -->
    <rect x="15" y="60" width="220" height="150" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="25" y="82" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Sports News Article:</text>
    <text x="25" y="105" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11">"The striker announced</text>
    <text x="25" y="125" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11">that <tspan fill="#BE185D" font-weight="700">he</tspan> <tspan fill="#1D4ED8" font-weight="700">was playing</tspan></text>
    <text x="25" y="145" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11">in the tournament</text>
    <text x="25" y="165" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11"><tspan fill="#B45309" font-weight="700">the next day</tspan>."</text>

    <text x="25" y="195" fill="#047857" font-family="system-ui, sans-serif" font-size="9" font-weight="600">✓ Fully aligned reported syntax</text>
  </g>

  <!-- Bottom: Complex Sentence Structural Blueprint -->
  <g transform="translate(25, 340)" filter="url(#cardShadow)">
    <rect width="750" height="95" rx="10" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5"/>
    <rect x="15" y="8" width="720" height="22" rx="4" fill="#0F172A"/>
    <text x="375" y="23" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">COMPLEX SENTENCE BLUEPRINT: SUBORDINATING CONJUNCTIONS</text>

    <text x="25" y="48" fill="#1E293B" font-family="system-ui, sans-serif" font-size="10.5"><tspan font-weight="700" fill="#2563EB">[Independent Clause]</tspan> ("Our team won the football championship") + <tspan font-weight="700" fill="#DC2626">[Subordinator]</tspan> ("although") + <tspan font-weight="700" fill="#059669">[Dependent Clause]</tspan> ("our striker was injured.")</text>
    <text x="25" y="68" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Inversion Rule: If the dependent clause comes first, insert a comma: <tspan font-style="italic">"Although our striker was injured, our team won the match."</tspan></text>
    <text x="25" y="84" fill="#64748B" font-family="system-ui, sans-serif" font-size="9">• Common Subordinating Conjunctions: although, because, since, unless, while, whereas, whenever, before, after.</text>
  </g>
</svg>"""
