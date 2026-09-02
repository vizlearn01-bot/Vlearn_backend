"""
VLearn CBC Grade 10 English — Topic 3: Grammar in Use
Custom Responsive Vector SVGs for Lessons 1 to 10
"""

# =============================================================================
# SVG 1: Lesson 1 — Nouns, Pronouns, and Determiners Matrix
# =============================================================================
SVG_NOUNS_PRONOUNS_DETERMINERS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l1HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="nounGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="pronounGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <linearGradient id="detGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#FDE68A"/>
    </linearGradient>
    <filter id="l1CardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Main Banner Header -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l1HeaderGrad)" filter="url(#l1CardShadow)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE ANCHORS OF THE SENTENCE</text>
  <text x="400" y="58" fill="#E0E7FF" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Nouns (Naming), Pronouns (Replacing), and Determiners (Specifying)</text>

  <!-- 3 Pillar Columns -->

  <!-- Column 1: NOUNS -->
  <g transform="translate(25, 88)" filter="url(#l1CardShadow)">
    <rect width="236" height="310" rx="12" fill="url(#nounGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#2563EB"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. NOUNS (Naming)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Classification Types:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Proper:</tspan> Nairobi, Mr. Omondi</text>
    <text x="20" y="102" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Common:</tspan> teacher, computer</text>
    <text x="20" y="118" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Concrete:</tspan> keyboard, router</text>
    <text x="20" y="134" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Abstract:</tspan> security, creativity</text>
    <text x="20" y="150" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Mass (Non-count):</tspan> software, info</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#1E3A8A"/>
    <text x="20" y="186" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Critical Rule (Count vs Mass):</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">❌ "many softwares / informations"</text>
    <text x="20" y="222" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9.5">✔ "software programs / information"</text>
    <text x="20" y="244" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Mass nouns have no plural '-s'</text>
    <text x="20" y="259" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="9" font-style="italic">and cannot take 'a/an' directly.</text>
  </g>

  <!-- Column 2: PRONOUNS -->
  <g transform="translate(282, 88)" filter="url(#l1CardShadow)">
    <rect width="236" height="310" rx="12" fill="url(#pronounGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#059669"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. PRONOUNS (Replacing)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Primary Categories:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Personal:</tspan> I, she, they, we, him</text>
    <text x="20" y="102" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Possessive:</tspan> mine, yours, theirs</text>
    <text x="20" y="118" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Demonstrative:</tspan> this, that, these</text>
    <text x="20" y="134" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Relative:</tspan> who, whom, which, that</text>
    <text x="20" y="150" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Reflexive:</tspan> myself, themselves</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#064E3B"/>
    <text x="20" y="186" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Antecedent Agreement Rule:</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">Pronoun MUST agree in number</text>
    <text x="20" y="220" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">&amp; gender with its antecedent noun.</text>
    <text x="20" y="242" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9.5">✔ "The team won its match."</text>
    <text x="20" y="258" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9.5">❌ "The team won their match."</text>
  </g>

  <!-- Column 3: DETERMINERS -->
  <g transform="translate(539, 88)" filter="url(#l1CardShadow)">
    <rect width="236" height="310" rx="12" fill="url(#detGrad)" stroke="#F59E0B" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#D97706"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. DETERMINERS (Signposts)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#92400E" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Signpost Subtypes:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Articles:</tspan> a, an (indef.), the (def.)</text>
    <text x="20" y="102" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Possessives:</tspan> my, your, his, their</text>
    <text x="20" y="134" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Demonstratives:</tspan> this, that, those</text>
    <text x="20" y="150" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Quantifiers:</tspan> some, few, little, all</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#78350F"/>
    <text x="20" y="186" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Crucial Contrast (Quantifiers):</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Few / Little:</tspan> Negative (hardly any)</text>
    <text x="20" y="220" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">A few / A little:</tspan> Positive (some)</text>
    <text x="20" y="242" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Count:</tspan> few laptops / many apps</text>
    <text x="20" y="258" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Mass:</tspan> little time / much data</text>
  </g>

  <!-- Bottom Architecture Integration Bar -->
  <g transform="translate(25, 412)" filter="url(#l1CardShadow)">
    <rect width="750" height="52" rx="10" fill="#1E293B"/>
    <text x="35" y="31" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">SENTENCE MODEL:</text>
    <text x="160" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11">
      [ <tspan fill="#FBBF24" font-weight="700">The</tspan> (Det) + <tspan fill="#93C5FD" font-weight="700">diligent teacher</tspan> (Noun) ] handed [ <tspan fill="#FBBF24" font-weight="700">her</tspan> (Det) + <tspan fill="#93C5FD" font-weight="700">students</tspan> ] [ <tspan fill="#FBBF24" font-weight="700">their</tspan> (Det) + <tspan fill="#93C5FD" font-weight="700">devices</tspan> ]. <tspan fill="#4ADE80" font-weight="700">They</tspan> (Pronoun) were pleased.
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 2: Lesson 2 — Verbs (Tense & Aspect) and Adverb Modification
# =============================================================================
SVG_VERBS_AND_ADVERBS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l2HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4C1D95"/>
      <stop offset="100%" stop-color="#7C3AED"/>
    </linearGradient>
    <linearGradient id="aspectGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F5F3FF"/>
      <stop offset="100%" stop-color="#EDE9FE"/>
    </linearGradient>
    <linearGradient id="adverbGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
    <filter id="l2Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Main Banner Header -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l2HeaderGrad)" filter="url(#l2Shadow)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">VERBS &amp; ADVERBS: ENGINES &amp; STEERING WHEELS</text>
  <text x="400" y="58" fill="#DDD6FE" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Tense (When) • Aspect (How Action Unfolds) • Adverbial Modification</text>

  <!-- Left: THE 4 ASPECTS OF ENGLISH VERBS -->
  <g transform="translate(25, 88)" filter="url(#l2Shadow)">
    <rect width="430" height="310" rx="12" fill="url(#aspectGrad)" stroke="#7C3AED" stroke-width="2"/>
    <rect x="14" y="12" width="402" height="30" rx="6" fill="#6D28D9"/>
    <text x="215" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">THE 4 VERB ASPECTS ACROSS TIME</text>
    
    <!-- 4 Aspect Rows -->
    <!-- Simple -->
    <rect x="14" y="50" width="402" height="56" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="20" y="56" width="95" height="20" rx="4" fill="#EDE9FE"/>
    <text x="67" y="70" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1. SIMPLE</text>
    <text x="125" y="68" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700">Focus:</tspan> Habitual, factual, or completed whole action.</text>
    <text x="125" y="86" fill="#6D28D9" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">"I study daily." / "He sprinted down the pitch."</text>

    <!-- Continuous / Progressive -->
    <rect x="14" y="112" width="402" height="56" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="20" y="118" width="95" height="20" rx="4" fill="#DBEAFE"/>
    <text x="67" y="132" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">2. CONTINUOUS</text>
    <text x="125" y="130" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700">Focus:</tspan> Ongoing, in-progress action [Be + Verb-ing].</text>
    <text x="125" y="148" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">"The striker is kicking the ball skillfully."</text>

    <!-- Perfect -->
    <rect x="14" y="174" width="402" height="56" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="20" y="180" width="95" height="20" rx="4" fill="#DCFCE7"/>
    <text x="67" y="194" fill="#166534" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">3. PERFECT</text>
    <text x="125" y="192" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700">Focus:</tspan> Completed prior to a reference point [Have + Past Part.].</text>
    <text x="125" y="210" fill="#166534" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">"By 5 PM, the server had crashed." (Past Perfect)</text>

    <!-- Perfect Continuous -->
    <rect x="14" y="236" width="402" height="64" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="20" y="244" width="95" height="28" rx="4" fill="#FEE2E2"/>
    <text x="67" y="256" fill="#991B1B" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">4. PERFECT</text>
    <text x="67" y="267" fill="#991B1B" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">CONTINUOUS</text>
    <text x="125" y="254" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700">Focus:</tspan> Duration leading up to a specific time point.</text>
    <text x="125" y="272" fill="#991B1B" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">"We will have been utilizing this lab for two years."</text>
  </g>

  <!-- Right: 5 ADVERB CATEGORIES -->
  <g transform="translate(470, 88)" filter="url(#l2Shadow)">
    <rect width="305" height="310" rx="12" fill="url(#adverbGrad)" stroke="#F59E0B" stroke-width="2"/>
    <rect x="12" y="12" width="281" height="30" rx="6" fill="#D97706"/>
    <text x="152" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">5 TYPES OF ADVERBS</text>
    
    <rect x="12" y="50" width="281" height="248" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    
    <text x="22" y="72" fill="#B45309" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Manner (How?):</text>
    <text x="22" y="88" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">sprinted <tspan font-weight="700" fill="#2563EB">powerfully</tspan>, listened <tspan font-weight="700" fill="#2563EB">attentively</tspan></text>
    
    <text x="22" y="112" fill="#B45309" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Time (When?):</text>
    <text x="22" y="128" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">arrived <tspan font-weight="700" fill="#2563EB">yesterday</tspan>, update <tspan font-weight="700" fill="#2563EB">now</tspan>, soon</text>
    
    <text x="22" y="152" fill="#B45309" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Place (Where?):</text>
    <text x="22" y="168" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">studied <tspan font-weight="700" fill="#2563EB">here</tspan>, gathered <tspan font-weight="700" fill="#2563EB">outside</tspan>, upstairs</text>
    
    <text x="22" y="192" fill="#B45309" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Frequency (How often?):</text>
    <text x="22" y="208" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">always</tspan> inspects, <tspan font-weight="700" fill="#2563EB">rarely</tspan> fails, regularly</text>
    
    <text x="22" y="232" fill="#B45309" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Degree (To what extent?):</text>
    <text x="22" y="248" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">extremely</tspan> fast, <tspan font-weight="700" fill="#2563EB">very</tspan> clear, rather</text>

    <line x1="22" y1="262" x2="283" y2="262" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="22" y="278" fill="#DC2626" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Placement Rule:</text>
    <text x="22" y="291" fill="#4B5563" font-family="system-ui, sans-serif" font-size="8.5">Never place adverb between Verb &amp; Direct Object!</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(25, 412)" filter="url(#l2Shadow)">
    <rect width="750" height="52" rx="10" fill="#1E1B4B"/>
    <text x="35" y="31" fill="#A78BFA" font-family="system-ui, sans-serif" font-size="11" font-weight="700">SYNTAX MODEL:</text>
    <text x="155" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      The striker [ <tspan fill="#FBBF24" font-weight="700">skilfully</tspan> (Adv) ] [ <tspan fill="#38BDF8" font-weight="700">had kicked</tspan> (Past Perfect VP) ] the ball [ <tspan fill="#4ADE80" font-weight="700">into the top corner</tspan> ] [ <tspan fill="#FBBF24" font-weight="700">yesterday</tspan> (Adv) ].
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 3: Lesson 3 — Adjectives, Conjunctions, and Sentence Connectors
# =============================================================================
SVG_ADJECTIVES_CONJUNCTIONS_CONNECTORS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l3HeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>
    <linearGradient id="adjGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5"/>
      <stop offset="100%" stop-color="#D1FAE5"/>
    </linearGradient>
    <linearGradient id="fanboysGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="connGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFF7ED"/>
      <stop offset="100%" stop-color="#FFEDD5"/>
    </linearGradient>
    <filter id="l3Shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l3HeaderGrad)" filter="url(#l3Shadow)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ADDING COLOR &amp; BUILDING LOGICAL BRIDGES</text>
  <text x="400" y="58" fill="#D1FAE5" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Adjectives (Collocations) • FANBOYS Coordinating Conjunctions • Sentence Connectors</text>

  <!-- 3 Column Cards -->

  <!-- Card 1: ADJECTIVES & COLLOCATIONS -->
  <g transform="translate(25, 88)" filter="url(#l3Shadow)">
    <rect width="236" height="310" rx="12" fill="url(#adjGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#059669"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">ADJECTIVES &amp; PAIRS</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Syntactic Positions:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Attributive:</tspan> before noun</text>
    <text x="20" y="100" fill="#047857" font-family="system-ui, sans-serif" font-size="9" font-style="italic">  "a <tspan font-weight="700">scenic</tspan> route"</text>
    <text x="20" y="118" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Predicative:</tspan> after linking verb</text>
    <text x="20" y="132" fill="#047857" font-family="system-ui, sans-serif" font-size="9" font-style="italic">  "the route is <tspan font-weight="700">scenic</tspan>"</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#064E3B"/>
    <text x="20" y="186" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Natural Collocations:</text>
    <text x="20" y="204" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9.5">✔ heavy rain</text>
    <text x="120" y="204" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9.5">❌ strong rain</text>
    <text x="20" y="222" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9.5">✔ bitter regret</text>
    <text x="120" y="222" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9.5">❌ sour regret</text>
    <text x="20" y="240" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9.5">✔ crucial decision</text>
    <text x="20" y="258" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9.5">✔ excruciating pain</text>
  </g>

  <!-- Card 2: FANBOYS CONJUNCTIONS -->
  <g transform="translate(282, 88)" filter="url(#l3Shadow)">
    <rect width="236" height="310" rx="12" fill="url(#fanboysGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#2563EB"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">FANBOYS CONJUNCTIONS</text>
    
    <rect x="12" y="50" width="212" height="152" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Coordinating 7:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">F</tspan>or (cause/reason)</text>
    <text x="20" y="102" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">A</tspan>nd (addition)</text>
    <text x="20" y="118" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">N</tspan>or (negative alternative)</text>
    <text x="20" y="134" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">B</tspan>ut (contrast)</text>
    <text x="20" y="150" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">O</tspan>r (choice)</text>
    <text x="20" y="166" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">Y</tspan>et (unexpected contrast)</text>
    <text x="20" y="182" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5"><tspan font-weight="700" fill="#2563EB">S</tspan>o (result)</text>

    <rect x="12" y="210" width="212" height="88" rx="6" fill="#1E3A8A"/>
    <text x="20" y="228" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The Comma Rule:</text>
    <text x="20" y="246" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9">[Clause 1] <tspan fill="#FBBF24" font-weight="700">,</tspan> + <tspan fill="#93C5FD" font-weight="700">FANBOYS</tspan> + [Clause 2]</text>
    <text x="20" y="264" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">"The work is hard<tspan font-weight="700" fill="#FBBF24">,</tspan> but it pays well."</text>
  </g>

  <!-- Card 3: SENTENCE CONNECTORS -->
  <g transform="translate(539, 88)" filter="url(#l3Shadow)">
    <rect width="236" height="310" rx="12" fill="url(#connGrad)" stroke="#EA580C" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#C2410C"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">SENTENCE CONNECTORS</text>
    
    <rect x="12" y="50" width="212" height="152" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#9A3412" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Conjunctive Adverbs:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Contrast:</tspan> however, nevertheless</text>
    <text x="20" y="104" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Result:</tspan> therefore, consequently</text>
    <text x="20" y="122" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Addition:</tspan> furthermore, in addition</text>
    <text x="20" y="140" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Exemplification:</tspan> for example</text>
    <text x="20" y="162" fill="#C2410C" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Crucial Punctuation:</text>
    <text x="20" y="178" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">Use <tspan font-weight="700">Semicolon + Comma</tspan>:</text>
    <text x="20" y="193" fill="#0369A1" font-family="system-ui, sans-serif" font-size="9"> [Clause 1]<tspan font-weight="700">; however,</tspan> [Clause 2]</text>

    <rect x="12" y="210" width="212" height="88" rx="6" fill="#7C2D12"/>
    <text x="20" y="228" fill="#FED7AA" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Common Error Warning:</text>
    <text x="20" y="246" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="9">❌ "Road blocked, therefore..." (Splice)</text>
    <text x="20" y="264" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9">✔ "Road blocked; therefore, we..."</text>
  </g>

  <!-- Bottom Synthesis Bar -->
  <g transform="translate(25, 412)" filter="url(#l3Shadow)">
    <rect width="750" height="52" rx="10" fill="#064E3B"/>
    <text x="35" y="31" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="11" font-weight="700">SYNTAX FORMULA:</text>
    <text x="165" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      The route was [ <tspan fill="#FDE68A" font-weight="700">scenic</tspan> ]<tspan fill="#FBBF24" font-weight="700">, yet</tspan> it was [ <tspan fill="#FDE68A" font-weight="700">demanding</tspan> ]<tspan fill="#FBBF24" font-weight="700">; therefore,</tspan> we drove with [ <tspan fill="#FDE68A" font-weight="700">extreme</tspan> ] caution.
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 4: Lesson 4 — Noun Phrases (NP) and Verb Phrases (VP) Architecture
# =============================================================================
SVG_NOUN_AND_VERB_PHRASES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 490" width="100%" height="100%">
  <defs>
    <linearGradient id="l4Head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#2563EB"/>
    </linearGradient>
    <linearGradient id="npGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="vpGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FDF2F8"/>
      <stop offset="100%" stop-color="#FCE7F3"/>
    </linearGradient>
    <filter id="l4Sh" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="490" rx="16" fill="#F8FAFC"/>

  <!-- Banner Header -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l4Head)" filter="url(#l4Sh)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PHRASE ARCHITECTURE: NOUN PHRASES &amp; VERB PHRASES</text>
  <text x="400" y="58" fill="#BAE6FD" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Deconstructing Head Words, Modifiers, Auxiliaries, and Complements</text>

  <!-- TOP CARD: NOUN PHRASE (NP) DECONSTRUCTION -->
  <g transform="translate(25, 88)" filter="url(#l4Sh)">
    <rect width="750" height="152" rx="12" fill="url(#npGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="16" y="12" width="220" height="26" rx="6" fill="#2563EB"/>
    <text x="126" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">NOUN PHRASE (NP) ANATOMY</text>
    
    <!-- 4 Sub-blocks of NP -->
    <!-- Determiner -->
    <g transform="translate(16, 48)">
      <rect width="130" height="88" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.5"/>
      <rect x="6" y="6" width="118" height="20" rx="4" fill="#DBEAFE"/>
      <text x="65" y="19" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">DETERMINER</text>
      <text x="65" y="46" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">"The"</text>
      <text x="65" y="68" fill="#6B7280" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Articles / Possessives</text>
    </g>

    <!-- Premodifiers -->
    <g transform="translate(156, 48)">
      <rect width="170" height="88" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.5"/>
      <rect x="6" y="6" width="158" height="20" rx="4" fill="#DBEAFE"/>
      <text x="85" y="19" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">PREMODIFIERS</text>
      <text x="85" y="46" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">"majestic migratory"</text>
      <text x="85" y="68" fill="#6B7280" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Adjectives / Noun Adjuncts</text>
    </g>

    <!-- Head Noun (Core) -->
    <g transform="translate(336, 48)">
      <rect width="170" height="88" rx="8" fill="#1E40AF" stroke="#1E3A8A" stroke-width="2"/>
      <rect x="6" y="6" width="158" height="20" rx="4" fill="#3B82F6"/>
      <text x="85" y="19" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">HEAD NOUN (ANCHOR)</text>
      <text x="85" y="46" fill="#FEF08A" font-family="system-ui, sans-serif" font-size="13" font-weight="900" text-anchor="middle">"BIRDS"</text>
      <text x="85" y="68" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Core syntactic center</text>
    </g>

    <!-- Postmodifiers -->
    <g transform="translate(516, 48)">
      <rect width="218" height="88" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.5"/>
      <rect x="6" y="6" width="206" height="20" rx="4" fill="#DBEAFE"/>
      <text x="109" y="19" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">POSTMODIFIER</text>
      <text x="109" y="46" fill="#1F2937" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">"[of East Africa]"</text>
      <text x="109" y="68" fill="#6B7280" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Prepositional / Relative Clause</text>
    </g>
  </g>

  <!-- BOTTOM CARD: VERB PHRASE (VP) DECONSTRUCTION -->
  <g transform="translate(25, 252)" filter="url(#l4Sh)">
    <rect width="750" height="152" rx="12" fill="url(#vpGrad)" stroke="#DB2777" stroke-width="2"/>
    <rect x="16" y="12" width="220" height="26" rx="6" fill="#BE185D"/>
    <text x="126" y="29" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">VERB PHRASE (VP) ANATOMY</text>
    
    <!-- 3 Sub-blocks of VP -->
    <!-- Modal / Auxiliaries -->
    <g transform="translate(16, 48)">
      <rect width="220" height="88" rx="8" fill="#FFFFFF" stroke="#F472B6" stroke-width="1.5"/>
      <rect x="6" y="6" width="208" height="20" rx="4" fill="#FCE7F3"/>
      <text x="110" y="19" fill="#9D174D" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">AUXILIARIES / HELPING VERBS</text>
      <text x="110" y="46" fill="#1F2937" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">"have been"</text>
      <text x="110" y="68" fill="#6B7280" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Aspect / Tense markers</text>
    </g>

    <!-- Main Verb (Head) -->
    <g transform="translate(246, 48)">
      <rect width="230" height="88" rx="8" fill="#831843" stroke="#500724" stroke-width="2"/>
      <rect x="6" y="6" width="218" height="20" rx="4" fill="#DBEAFE"/>
      <text x="115" y="19" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">MAIN VERB (HEAD)</text>
      <text x="115" y="46" fill="#FEF08A" font-family="system-ui, sans-serif" font-size="13" font-weight="900" text-anchor="middle">"FLYING"</text>
      <text x="115" y="68" fill="#FCE7F3" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Carries semantic action</text>
    </g>

    <!-- Complements / Adverbials -->
    <g transform="translate(486, 48)">
      <rect width="248" height="88" rx="8" fill="#FFFFFF" stroke="#F472B6" stroke-width="1.5"/>
      <rect x="6" y="6" width="236" height="20" rx="4" fill="#FCE7F3"/>
      <text x="124" y="19" fill="#9D174D" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ADVERBIAL MODIFIERS</text>
      <text x="124" y="46" fill="#1F2937" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">"swiftly southward"</text>
      <text x="124" y="68" fill="#6B7280" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Manner + Direction</text>
    </g>
  </g>

  <!-- Bottom Insight Bar -->
  <g transform="translate(25, 418)" filter="url(#l4Sh)">
    <rect width="750" height="56" rx="10" fill="#0F172A"/>
    <text x="35" y="25" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">THE PHRASE SUBSTITUTION TEST:</text>
    <text x="35" y="44" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10">
      Entire 7-word NP [<tspan fill="#93C5FD">The majestic migratory birds of East Africa</tspan>] can be replaced by 1 pronoun: <tspan fill="#4ADE80" font-weight="700">"They"</tspan>!
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 5: Lesson 5 — Adjective, Adverb, and Prepositional Phrases
# =============================================================================
SVG_ADJ_ADV_PREP_PHRASES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l5Head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <linearGradient id="pCard1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0FDFA"/>
      <stop offset="100%" stop-color="#CCFBF1"/>
    </linearGradient>
    <linearGradient id="pCard2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="pCard3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <filter id="l5Sh" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Banner Header -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l5Head)" filter="url(#l5Sh)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ADJECTIVE, ADVERB &amp; PREPOSITIONAL PHRASES</text>
  <text x="400" y="58" fill="#CCFBF1" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Adding Depth, Detail, and Precise Contextual Modifiers</text>

  <!-- 3 Phrase Columns -->

  <!-- 1. ADJECTIVE PHRASE -->
  <g transform="translate(25, 88)" filter="url(#l5Sh)">
    <rect width="236" height="310" rx="12" fill="url(#pCard1)" stroke="#0D9488" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#0F766E"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ADJECTIVE PHRASE (AdjP)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#115E59" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Target &amp; Structure:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Modifies:</tspan> Noun or Pronoun</text>
    <text x="20" y="102" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Head:</tspan> Adjective</text>
    <text x="20" y="120" fill="#0F766E" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"a <tspan font-weight="700">highly rewarding</tspan> career"</text>
    <text x="20" y="136" fill="#0F766E" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"candidate <tspan font-weight="700">eager for the job</tspan>"</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#134E4A"/>
    <text x="20" y="186" fill="#5EEAD4" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Formula:</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">[Degree Adv] + <tspan font-weight="700" fill="#5EEAD4">[Head Adj]</tspan></text>
    <text x="20" y="222" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">or <tspan font-weight="700" fill="#5EEAD4">[Head Adj]</tspan> + [PP Complement]</text>
    <text x="20" y="244" fill="#99F6E4" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Answers: "What kind?"</text>
    <text x="20" y="259" fill="#99F6E4" font-family="system-ui, sans-serif" font-size="9" font-style="italic">or "Which one?"</text>
  </g>

  <!-- 2. ADVERB PHRASE -->
  <g transform="translate(282, 88)" filter="url(#l5Sh)">
    <rect width="236" height="310" rx="12" fill="url(#pCard2)" stroke="#2563EB" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#1D4ED8"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ADVERB PHRASE (AdvP)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Target &amp; Structure:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Modifies:</tspan> Verb, Adj, or Adv</text>
    <text x="20" y="102" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Head:</tspan> Adverb</text>
    <text x="20" y="120" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"spoke <tspan font-weight="700">remarkably well</tspan>"</text>
    <text x="20" y="136" fill="#1D4ED8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"walked <tspan font-weight="700">rather slowly</tspan>"</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#1E3A8A"/>
    <text x="20" y="186" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Formula:</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5">[Degree Adv] + <tspan font-weight="700" fill="#93C5FD">[Head Adv]</tspan></text>
    <text x="20" y="226" fill="#BFDBFE" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Answers: "How?",</text>
    <text x="20" y="242" fill="#BFDBFE" font-family="system-ui, sans-serif" font-size="9" font-style="italic">"To what extent?",</text>
    <text x="20" y="258" fill="#BFDBFE" font-family="system-ui, sans-serif" font-size="9" font-style="italic">or "How frequently?"</text>
  </g>

  <!-- 3. PREPOSITIONAL PHRASE (DUAL ROLE) -->
  <g transform="translate(539, 88)" filter="url(#l5Sh)">
    <rect width="236" height="310" rx="12" fill="url(#pCard3)" stroke="#DC2626" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#B91C1C"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">PREPOSITIONAL PHRASE (PP)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Structure: Prep + NP Object</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• <tspan font-weight="700">Adjectival PP:</tspan> Modifies Noun</text>
    <text x="20" y="99" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">  "computers <tspan font-weight="700">[in the lab]</tspan>"</text>
    <text x="20" y="116" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• <tspan font-weight="700">Adverbial PP:</tspan> Modifies Verb</text>
    <text x="20" y="129" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">  "answered <tspan font-weight="700">[with confidence]</tspan>"</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#7F1D1D"/>
    <text x="20" y="186" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Testing Arrow Method:</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9">Draw arrow from PP to head:</text>
    <text x="20" y="222" fill="#FEF08A" font-family="system-ui, sans-serif" font-size="9">Arrow -> Noun = Adjectival PP</text>
    <text x="20" y="240" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="9">Arrow -> Verb = Adverbial PP</text>
    <text x="20" y="258" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="8.5">Avoid Misplaced Modifiers!</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(25, 412)" filter="url(#l5Sh)">
    <rect width="750" height="52" rx="10" fill="#042F2E"/>
    <text x="35" y="31" fill="#2DD4BF" font-family="system-ui, sans-serif" font-size="11" font-weight="700">SENTENCE ANATOMY:</text>
    <text x="170" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      The candidate [ <tspan fill="#5EEAD4" font-weight="700">eager for work</tspan> (AdjP) ] answered [ <tspan fill="#93C5FD" font-weight="700">exceptionally well</tspan> (AdvP) ] [ <tspan fill="#FCA5A5" font-weight="700">during the interview</tspan> (PP) ].
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 6: Lesson 6 — Relative and Adverbial Clauses Architecture
# =============================================================================
SVG_RELATIVE_AND_ADVERBIAL_CLAUSES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l6Head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4338CA"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="relGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EEF2FF"/>
      <stop offset="100%" stop-color="#E0E7FF"/>
    </linearGradient>
    <linearGradient id="advcGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FDF4FF"/>
      <stop offset="100%" stop-color="#FAE8FF"/>
    </linearGradient>
    <filter id="l6Sh" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l6Head)" filter="url(#l6Sh)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">COMPLEX CLAUSES: RELATIVE &amp; ADVERBIAL</text>
  <text x="400" y="58" fill="#E0E7FF" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Defining vs Non-Defining Relative Clauses • Subordinating Conjunctions • Comma Rules</text>

  <!-- Left: RELATIVE CLAUSES (ADJECTIVE CLAUSES) -->
  <g transform="translate(25, 88)" filter="url(#l6Sh)">
    <rect width="365" height="310" rx="12" fill="url(#relGrad)" stroke="#6366F1" stroke-width="2"/>
    <rect x="14" y="12" width="337" height="30" rx="6" fill="#4F46E5"/>
    <text x="182" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. RELATIVE (ADJECTIVE) CLAUSES</text>
    
    <!-- Defining -->
    <rect x="14" y="50" width="337" height="116" rx="8" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="22" y="58" width="160" height="20" rx="4" fill="#DCFCE7"/>
    <text x="102" y="72" fill="#166534" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">DEFINING (RESTRICTIVE)</text>
    <text x="22" y="94" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• <tspan font-weight="700">Purpose:</tspan> Essential info; identifies <tspan font-style="italic">which</tspan> noun.</text>
    <text x="22" y="109" fill="#15803D" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• NO COMMAS used!</text>
    <text x="22" y="124" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• Pronouns: <tspan font-weight="700">who, whom, whose, which, that</tspan></text>
    <text x="22" y="142" fill="#4338CA" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"The ritual <tspan font-weight="700">that marks adulthood</tspan> is sacred."</text>

    <!-- Non-Defining -->
    <rect x="14" y="174" width="337" height="124" rx="8" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="22" y="182" width="180" height="20" rx="4" fill="#FEE2E2"/>
    <text x="112" y="196" fill="#991B1B" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">NON-DEFINING (EXTRA INFO)</text>
    <text x="22" y="218" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• <tspan font-weight="700">Purpose:</tspan> Extra descriptive detail.</text>
    <text x="22" y="233" fill="#DC2626" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• COMMAS REQUIRED (enclosed in commas)!</text>
    <text x="22" y="248" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• Pronouns: <tspan font-weight="700">who, whom, which</tspan> (<tspan fill="#DC2626" font-weight="700">NEVER "that"</tspan>)</text>
    <text x="22" y="266" fill="#4338CA" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"The festival<tspan font-weight="700" fill="#DC2626">,</tspan> <tspan font-weight="700">which happens annually,</tspan><tspan font-weight="700" fill="#DC2626">,</tspan> is lively."</text>
  </g>

  <!-- Right: ADVERBIAL CLAUSES -->
  <g transform="translate(410, 88)" filter="url(#l6Sh)">
    <rect width="365" height="310" rx="12" fill="url(#advcGrad)" stroke="#C026D3" stroke-width="2"/>
    <rect x="14" y="12" width="337" height="30" rx="6" fill="#A21CAF"/>
    <text x="182" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. ADVERBIAL CLAUSES</text>
    
    <rect x="14" y="50" width="337" height="248" rx="8" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="24" y="70" fill="#86198F" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Functions &amp; Subordinators:</text>
    
    <text x="24" y="90" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700" fill="#C026D3">Time (When?):</tspan> when, while, before, after, since</text>
    <text x="32" y="105" fill="#701A75" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"When the harvest arrived, they celebrated."</text>
    
    <text x="24" y="125" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700" fill="#C026D3">Reason (Why?):</tspan> because, since, as</text>
    <text x="32" y="140" fill="#701A75" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"They listened because they respected the elder."</text>
    
    <text x="24" y="160" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700" fill="#C026D3">Condition:</tspan> if, unless, provided that</text>
    
    <text x="24" y="180" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700" fill="#C026D3">Concession:</tspan> although, even though</text>

    <line x1="24" y1="196" x2="330" y2="196" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="24" y="214" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Subordinate Clause Comma Rule:</text>
    <text x="24" y="232" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">✔ [Adv Clause]<tspan font-weight="700" fill="#DC2626">,</tspan> + [Independent Clause]</text>
    <text x="24" y="248" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">✔ [Independent Clause] + [Adv Clause] (no comma!)</text>
    <text x="24" y="268" fill="#047857" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"Because it rained, we stayed." vs "We stayed because..."</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(25, 412)" filter="url(#l6Sh)">
    <rect width="750" height="52" rx="10" fill="#1E1B4B"/>
    <text x="35" y="31" fill="#A5B4FC" font-family="system-ui, sans-serif" font-size="11" font-weight="700">SYNTAX SYNTHESIS:</text>
    <text x="180" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      We visited the elder [ <tspan fill="#F472B6" font-weight="700">whom the community admires</tspan> ] [ <tspan fill="#38BDF8" font-weight="700">because he preserves history</tspan> ].
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 7: Lesson 7 — Noun Clauses and Clause Functions
# =============================================================================
SVG_NOUN_CLAUSES_FUNCTIONS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l7Head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B45309"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
    <linearGradient id="ncCardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
    <filter id="l7Sh" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Header Banner -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l7Head)" filter="url(#l7Sh)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">NOUN CLAUSES: 5 SYNTACTIC ROLES</text>
  <text x="400" y="58" fill="#FEF3C7" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Embedded Clauses Functioning as Subjects, Objects, Complements, and Appositives</text>

  <!-- 5 Functional Pillars -->
  <!-- 1. Subject of Verb -->
  <g transform="translate(25, 88)" filter="url(#l7Sh)">
    <rect width="142" height="310" rx="10" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
    <rect x="8" y="10" width="126" height="32" rx="6" fill="#D97706"/>
    <text x="71" y="24" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">1. SUBJECT</text>
    <text x="71" y="36" fill="#FEF3C7" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">OF THE VERB</text>
    
    <text x="12" y="64" fill="#92400E" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Position:</text>
    <text x="12" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">Before main verb</text>
    
    <rect x="8" y="94" width="126" height="110" rx="6" fill="#FEF3C7"/>
    <text x="14" y="110" fill="#92400E" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Example:</text>
    <text x="14" y="126" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8" font-style="italic">"<tspan font-weight="700" fill="#B45309">What you said</tspan> was highly encouraging."</text>
    
    <rect x="8" y="214" width="126" height="86" rx="6" fill="#78350F"/>
    <text x="14" y="232" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Replacement Test:</text>
    <text x="14" y="250" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="8">"<tspan font-weight="700" fill="#86EFAC">It</tspan> was encouraging."</text>
  </g>

  <!-- 2. Direct Object -->
  <g transform="translate(177, 88)" filter="url(#l7Sh)">
    <rect width="142" height="310" rx="10" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
    <rect x="8" y="10" width="126" height="32" rx="6" fill="#2563EB"/>
    <text x="71" y="24" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">2. DIRECT</text>
    <text x="71" y="36" fill="#DBEAFE" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">OBJECT</text>
    
    <text x="12" y="64" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Position:</text>
    <text x="12" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">After transitive verb</text>
    
    <rect x="8" y="94" width="126" height="110" rx="6" fill="#DBEAFE"/>
    <text x="14" y="110" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Example:</text>
    <text x="14" y="126" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8" font-style="italic">"I heard <tspan font-weight="700" fill="#1E40AF">that our team won</tspan> the trophy."</text>
    
    <rect x="8" y="214" width="126" height="86" rx="6" fill="#1E3A8A"/>
    <text x="14" y="232" fill="#93C5FD" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Replacement Test:</text>
    <text x="14" y="250" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="8">"I heard <tspan font-weight="700" fill="#86EFAC">something</tspan>."</text>
  </g>

  <!-- 3. Subject Complement -->
  <g transform="translate(329, 88)" filter="url(#l7Sh)">
    <rect width="142" height="310" rx="10" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
    <rect x="8" y="10" width="126" height="32" rx="6" fill="#059669"/>
    <text x="71" y="24" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">3. SUBJECT</text>
    <text x="71" y="36" fill="#D1FAE5" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">COMPLEMENT</text>
    
    <text x="12" y="64" fill="#065F46" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Position:</text>
    <text x="12" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">After linking verb (is/was)</text>
    
    <rect x="8" y="94" width="126" height="110" rx="6" fill="#D1FAE5"/>
    <text x="14" y="110" fill="#065F46" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Example:</text>
    <text x="14" y="126" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8" font-style="italic">"Our concern is <tspan font-weight="700" fill="#047857">that we lack training</tspan>."</text>
    
    <rect x="8" y="214" width="126" height="86" rx="6" fill="#064E3B"/>
    <text x="14" y="232" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Replacement Test:</text>
    <text x="14" y="250" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="8">"Our concern is <tspan font-weight="700" fill="#86EFAC">this</tspan>."</text>
  </g>

  <!-- 4. Object of Preposition -->
  <g transform="translate(481, 88)" filter="url(#l7Sh)">
    <rect width="142" height="310" rx="10" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2"/>
    <rect x="8" y="10" width="126" height="32" rx="6" fill="#7C3AED"/>
    <text x="71" y="24" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">4. OBJECT OF</text>
    <text x="71" y="36" fill="#EDE9FE" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">PREPOSITION</text>
    
    <text x="12" y="64" fill="#6D28D9" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Position:</text>
    <text x="12" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">After preposition</text>
    
    <rect x="8" y="94" width="126" height="110" rx="6" fill="#EDE9FE"/>
    <text x="14" y="110" fill="#6D28D9" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Example:</text>
    <text x="14" y="126" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8" font-style="italic">"We focus on <tspan font-weight="700" fill="#6D28D9">how well they play</tspan>."</text>
    
    <rect x="8" y="214" width="126" height="86" rx="6" fill="#4C1D95"/>
    <text x="14" y="232" fill="#DDD6FE" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Replacement Test:</text>
    <text x="14" y="250" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="8">"We focus on <tspan font-weight="700" fill="#86EFAC">it</tspan>."</text>
  </g>

  <!-- 5. Appositive -->
  <g transform="translate(633, 88)" filter="url(#l7Sh)">
    <rect width="142" height="310" rx="10" fill="#FFFFFF" stroke="#EC4899" stroke-width="2"/>
    <rect x="8" y="10" width="126" height="32" rx="6" fill="#DB2777"/>
    <text x="71" y="24" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">5. APPOSITIVE</text>
    <text x="71" y="36" fill="#FCE7F3" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">RENAME NOUN</text>
    
    <text x="12" y="64" fill="#BE185D" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Position:</text>
    <text x="12" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">Renames prior noun</text>
    
    <rect x="8" y="94" width="126" height="110" rx="6" fill="#FCE7F3"/>
    <text x="14" y="110" fill="#BE185D" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Example:</text>
    <text x="14" y="126" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8" font-style="italic">"The rumor, <tspan font-weight="700" fill="#BE185D">that he resigned</tspan>, spread."</text>
    
    <rect x="8" y="214" width="126" height="86" rx="6" fill="#831843"/>
    <text x="14" y="232" fill="#FBCFE8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Statement Order:</text>
    <text x="14" y="250" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="8">Never use question order!</text>
  </g>

  <!-- Bottom Verification Rule -->
  <g transform="translate(25, 412)" filter="url(#l7Sh)">
    <rect width="750" height="52" rx="10" fill="#18181B"/>
    <text x="35" y="31" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">THE "SOMETHING / IT" TEST:</text>
    <text x="215" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      If an entire subordinate clause can be replaced by <tspan fill="#4ADE80" font-weight="700">"something"</tspan> or <tspan fill="#4ADE80" font-weight="700">"it"</tspan>, it is a <tspan fill="#38BDF8" font-weight="700">Noun Clause</tspan>!
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 8: Lesson 8 — Simple Sentence Structure and Sentence Parts
# =============================================================================
SVG_SIMPLE_SENTENCE_PARTS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l8Head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#065F46"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="elemGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4"/>
      <stop offset="100%" stop-color="#DCFCE7"/>
    </linearGradient>
    <filter id="l8Sh" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Banner Header -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l8Head)" filter="url(#l8Sh)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">SIMPLE SENTENCE STRUCTURE &amp; SENTENCE PARTS</text>
  <text x="400" y="58" fill="#A7F3D0" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Subject (S) • Verb (V) • Direct Object (DO) • Indirect Object (IO) • Complement (C) • Adjunct (A)</text>

  <!-- Top: 6 Sentence Elements Grid -->
  <g transform="translate(25, 88)" filter="url(#l8Sh)">
    <rect width="750" height="130" rx="12" fill="url(#elemGrad)" stroke="#10B981" stroke-width="2"/>
    <rect x="14" y="10" width="220" height="24" rx="6" fill="#047857"/>
    <text x="124" y="26" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">6 CORE SENTENCE ELEMENTS</text>

    <!-- Elements 6 boxes -->
    <!-- S -->
    <rect x="14" y="42" width="112" height="74" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="70" y="60" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Subject (S)</text>
    <text x="70" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Actor / Topic</text>
    <text x="70" y="96" fill="#047857" font-family="system-ui, sans-serif" font-size="8" font-style="italic" text-anchor="middle">"The teacher"</text>

    <!-- V -->
    <rect x="136" y="42" width="112" height="74" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="192" y="60" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Verb (V)</text>
    <text x="192" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Action / State</text>
    <text x="192" y="96" fill="#047857" font-family="system-ui, sans-serif" font-size="8" font-style="italic" text-anchor="middle">"handed"</text>

    <!-- IO -->
    <rect x="258" y="42" width="112" height="74" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="314" y="60" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Indirect Obj (IO)</text>
    <text x="314" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">To/for whom</text>
    <text x="314" y="96" fill="#047857" font-family="system-ui, sans-serif" font-size="8" font-style="italic" text-anchor="middle">"us"</text>

    <!-- DO -->
    <rect x="380" y="42" width="112" height="74" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="436" y="60" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Direct Obj (DO)</text>
    <text x="436" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Receiver of action</text>
    <text x="436" y="96" fill="#047857" font-family="system-ui, sans-serif" font-size="8" font-style="italic" text-anchor="middle">"the kit"</text>

    <!-- C -->
    <rect x="502" y="42" width="112" height="74" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="558" y="60" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Complement (C)</text>
    <text x="558" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Renames S or O</text>
    <text x="558" y="96" fill="#047857" font-family="system-ui, sans-serif" font-size="8" font-style="italic" text-anchor="middle">"head coach"</text>

    <!-- A -->
    <rect x="624" y="42" width="112" height="74" rx="6" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="680" y="60" fill="#065F46" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Adjunct (A)</text>
    <text x="680" y="78" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">When/Where/How</text>
    <text x="680" y="96" fill="#047857" font-family="system-ui, sans-serif" font-size="8" font-style="italic" text-anchor="middle">"yesterday"</text>
  </g>

  <!-- Bottom: 4 Primary Sentence Patterns -->
  <g transform="translate(25, 230)" filter="url(#l8Sh)">
    <rect width="750" height="172" rx="12" fill="#FFFFFF" stroke="#047857" stroke-width="2"/>
    <rect x="14" y="10" width="220" height="24" rx="6" fill="#065F46"/>
    <text x="124" y="26" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4 ESSENTIAL SENTENCE PATTERNS</text>

    <!-- 4 Pattern Cards -->
    <g transform="translate(14, 42)">
      <!-- Pattern 1: SVO -->
      <rect x="0" y="0" width="170" height="116" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect x="8" y="8" width="154" height="22" rx="4" fill="#DBEAFE"/>
      <text x="85" y="23" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">1. S - V - O</text>
      <text x="12" y="48" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">S:</tspan> We</text>
      <text x="12" y="64" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">V:</tspan> cleaned</text>
      <text x="12" y="80" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">O:</tspan> the laboratory</text>
      <text x="12" y="102" fill="#2563EB" font-family="system-ui, sans-serif" font-size="8" font-style="italic">Direct Action</text>

      <!-- Pattern 2: S-V-IO-DO -->
      <rect x="184" y="0" width="170" height="116" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect x="192" y="8" width="154" height="22" rx="4" fill="#DCFCE7"/>
      <text x="269" y="23" fill="#166534" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">2. S - V - IO - DO</text>
      <text x="196" y="48" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">S:</tspan> The nurse</text>
      <text x="196" y="64" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">V:</tspan> handed</text>
      <text x="196" y="80" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">IO/DO:</tspan> the patient medicine</text>
      <text x="196" y="102" fill="#166534" font-family="system-ui, sans-serif" font-size="8" font-style="italic">Double Object</text>

      <!-- Pattern 3: SVC -->
      <rect x="368" y="0" width="170" height="116" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect x="376" y="8" width="154" height="22" rx="4" fill="#FEF3C7"/>
      <text x="453" y="23" fill="#92400E" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">3. S - V - C</text>
      <text x="380" y="48" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">S:</tspan> Mental health</text>
      <text x="380" y="64" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">V:</tspan> is</text>
      <text x="380" y="80" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">C:</tspan> crucial (Subject Comp)</text>
      <text x="380" y="102" fill="#D97706" font-family="system-ui, sans-serif" font-size="8" font-style="italic">Linking / State</text>

      <!-- Pattern 4: SVOA -->
      <rect x="552" y="0" width="170" height="116" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect x="560" y="8" width="154" height="22" rx="4" fill="#FEE2E2"/>
      <text x="637" y="23" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">4. S - V - O - A</text>
      <text x="564" y="48" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">S:</tspan> He</text>
      <text x="564" y="64" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">V:</tspan> placed</text>
      <text x="564" y="80" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5"><tspan font-weight="700">O/A:</tspan> the kit [on the shelf]</text>
      <text x="564" y="102" fill="#DC2626" font-family="system-ui, sans-serif" font-size="8" font-style="italic">Action + Setting</text>
    </g>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(25, 414)" filter="url(#l8Sh)">
    <rect width="750" height="50" rx="10" fill="#064E3B"/>
    <text x="35" y="30" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="11" font-weight="700">STRUCTURE CHECK:</text>
    <text x="175" y="30" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      Every complete simple sentence expresses 1 complete thought with at least 1 Subject and 1 Finite Verb.
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 9: Lesson 9 — Sentence Fluency: Fragments, Run-ons, and Comma Splices
# =============================================================================
SVG_SENTENCE_FLUENCY_REPAIR = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l9Head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991B1B"/>
      <stop offset="100%" stop-color="#DC2626"/>
    </linearGradient>
    <linearGradient id="fragGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <linearGradient id="runGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
    <linearGradient id="spliceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4"/>
      <stop offset="100%" stop-color="#DCFCE7"/>
    </linearGradient>
    <filter id="l9Sh" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Banner Header -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l9Head)" filter="url(#l9Sh)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">SENTENCE FLUENCY &amp; BOUNDARY REPAIR</text>
  <text x="400" y="58" fill="#FECACA" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Diagnosing and Fixing Sentence Fragments, Run-ons, and Comma Splices</text>

  <!-- 3 Error Repair Columns -->

  <!-- Column 1: FRAGMENTS -->
  <g transform="translate(25, 88)" filter="url(#l9Sh)">
    <rect width="236" height="310" rx="12" fill="url(#fragGrad)" stroke="#DC2626" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#B91C1C"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">1. FRAGMENT (Incomplete)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">The Problem:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• Missing Subject, Verb, or</text>
    <text x="20" y="100" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">  stranded dependent clause.</text>
    <text x="20" y="120" fill="#DC2626" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">❌ "Because safety is first."</text>
    <text x="20" y="136" fill="#DC2626" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">❌ "Working late at night."</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#7F1D1D"/>
    <text x="20" y="186" fill="#FCA5A5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The Repair Toolkit:</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9">• Attach to main clause:</text>
    <text x="20" y="222" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">✔ "Because safety is first, we</text>
    <text x="20" y="236" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">  wear protective gear."</text>
    <text x="20" y="254" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9">• Add missing subject/verb:</text>
    <text x="20" y="270" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">✔ "<tspan font-weight="700">We were</tspan> working late."</text>
  </g>

  <!-- Column 2: RUN-ONS -->
  <g transform="translate(282, 88)" filter="url(#l9Sh)">
    <rect width="236" height="310" rx="12" fill="url(#runGrad)" stroke="#D97706" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#B45309"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">2. RUN-ON (Fused)</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#92400E" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">The Problem:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• Two independent clauses</text>
    <text x="20" y="100" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">  colliding with NO punctuation.</text>
    <text x="20" y="122" fill="#D97706" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">❌ "The wifi failed we had to</text>
    <text x="20" y="136" fill="#D97706" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">   restart the router."</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#78350F"/>
    <text x="20" y="186" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The Repair Toolkit:</text>
    <text x="20" y="204" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9">1. Full Stop: "...failed<tspan font-weight="700" fill="#FDE68A">.</tspan> We..."</text>
    <text x="20" y="222" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9">2. Semicolon: "...failed<tspan font-weight="700" fill="#FDE68A">;</tspan> we..."</text>
    <text x="20" y="240" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="9">3. Comma + FANBOYS:</text>
    <text x="20" y="258" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">✔ "...failed<tspan font-weight="700" fill="#FDE68A">, so</tspan> we restarted..."</text>
  </g>

  <!-- Column 3: COMMA SPLICES -->
  <g transform="translate(539, 88)" filter="url(#l9Sh)">
    <rect width="236" height="310" rx="12" fill="url(#spliceGrad)" stroke="#059669" stroke-width="2"/>
    <rect x="12" y="12" width="212" height="30" rx="6" fill="#047857"/>
    <text x="118" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">3. COMMA SPLICE</text>
    
    <rect x="12" y="50" width="212" height="110" rx="6" fill="#FFFFFF" fill-opacity="0.95"/>
    <text x="20" y="68" fill="#065F46" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">The Problem:</text>
    <text x="20" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">• Two independent clauses</text>
    <text x="20" y="100" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9">  joined ONLY by a comma.</text>
    <text x="20" y="122" fill="#059669" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">❌ "The server crashed, the</text>
    <text x="20" y="136" fill="#059669" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">   data was saved."</text>

    <rect x="12" y="168" width="212" height="130" rx="6" fill="#064E3B"/>
    <text x="20" y="186" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">The 3 Fix Formulas:</text>
    <text x="20" y="204" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">✔ "...crashed<tspan font-weight="700" fill="#FDE68A">, but</tspan> data was..."</text>
    <text x="20" y="222" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">✔ "...crashed<tspan font-weight="700" fill="#FDE68A">; however,</tspan> data..."</text>
    <text x="20" y="240" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">✔ "<tspan font-weight="700" fill="#FDE68A">Although</tspan> the server crashed,</text>
    <text x="20" y="254" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="8.5">   the data was saved."</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(25, 412)" filter="url(#l9Sh)">
    <rect width="750" height="52" rx="10" fill="#111827"/>
    <text x="35" y="31" fill="#F87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">GOLDEN RULE:</text>
    <text x="145" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      Never connect two complete thoughts with just a comma. Use: [ <tspan fill="#FBBF24" font-weight="700">, + FANBOYS</tspan> ] or [ <tspan fill="#60A5FA" font-weight="700">; (semicolon)</tspan> ] or [ <tspan fill="#4ADE80" font-weight="700">Subordination</tspan> ].
    </text>
  </g>
</svg>"""

# =============================================================================
# SVG 10: Lesson 10 — Active vs. Passive Voice and Subject-Verb Agreement
# =============================================================================
SVG_VOICE_AND_AGREEMENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="l10Head" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#4338CA"/>
    </linearGradient>
    <linearGradient id="voiceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
    <linearGradient id="svaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF2F2"/>
      <stop offset="100%" stop-color="#FEE2E2"/>
    </linearGradient>
    <filter id="l10Sh" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="480" rx="16" fill="#F8FAFC"/>

  <!-- Banner Header -->
  <rect x="25" y="16" width="750" height="58" rx="12" fill="url(#l10Head)" filter="url(#l10Sh)"/>
  <text x="400" y="39" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ACTIVE/PASSIVE VOICE &amp; SUBJECT–VERB AGREEMENT</text>
  <text x="400" y="58" fill="#C7D2FE" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">Transformational Voice Mechanics • Agreement with Complex Subjects, Collective &amp; Plural-Form Nouns</text>

  <!-- Left: ACTIVE VS PASSIVE VOICE -->
  <g transform="translate(25, 88)" filter="url(#l10Sh)">
    <rect width="365" height="310" rx="12" fill="url(#voiceGrad)" stroke="#3B82F6" stroke-width="2"/>
    <rect x="14" y="12" width="337" height="30" rx="6" fill="#2563EB"/>
    <text x="182" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">1. VOICE TRANSFORMATION MECHANICS</text>
    
    <!-- Active Box -->
    <rect x="14" y="50" width="337" height="116" rx="8" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="22" y="58" width="120" height="20" rx="4" fill="#DBEAFE"/>
    <text x="82" y="72" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">ACTIVE VOICE</text>
    <text x="22" y="94" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9"><tspan font-weight="700">Formula:</tspan> Subject (Actor) + Verb + Object</text>
    <text x="22" y="110" fill="#1E40AF" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"The security team <tspan font-weight="700">monitors</tspan> the main gate."</text>
    <text x="22" y="128" fill="#4B5563" font-family="system-ui, sans-serif" font-size="8.5">• Direct, energetic, clear accountability.</text>

    <!-- Passive Box -->
    <rect x="14" y="174" width="337" height="124" rx="8" fill="#FFFFFF" fill-opacity="0.95"/>
    <rect x="22" y="182" width="130" height="20" rx="4" fill="#EDE9FE"/>
    <text x="87" y="196" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">PASSIVE VOICE</text>
    <text x="22" y="218" fill="#1F2937" font-family="system-ui, sans-serif" font-size="9"><tspan font-weight="700">Formula:</tspan> Object + [Be + Past Part.] + (by Actor)</text>
    <text x="22" y="236" fill="#5B21B6" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"The main gate <tspan font-weight="700">is monitored</tspan> (by security)."</text>
    <text x="22" y="254" fill="#4B5563" font-family="system-ui, sans-serif" font-size="8.5">• Emphasizes action/result; useful in formal &amp; scientific reports.</text>
  </g>

  <!-- Right: SUBJECT-VERB AGREEMENT RULES -->
  <g transform="translate(410, 88)" filter="url(#l10Sh)">
    <rect width="365" height="310" rx="12" fill="url(#svaGrad)" stroke="#DC2626" stroke-width="2"/>
    <rect x="14" y="12" width="337" height="30" rx="6" fill="#B91C1C"/>
    <text x="182" y="32" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">2. SUBJECT–VERB AGREEMENT (SVA)</text>
    
    <rect x="14" y="50" width="337" height="248" rx="8" fill="#FFFFFF" fill-opacity="0.95"/>
    
    <text x="24" y="70" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Nouns Ending in '-s' (Singular):</text>
    <text x="24" y="86" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">Mathematics, News, Economics, Physics take <tspan font-weight="700" fill="#15803D">SINGULAR</tspan> verbs!</text>
    <text x="24" y="100" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="8" font-style="italic">✔ "Mathematics <tspan font-weight="700">is</tspan> essential for computing."</text>

    <text x="24" y="122" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Proximity Rule (Intervening Phrases):</text>
    <text x="24" y="138" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">Subject is the head noun, NOT the noun in prepositional phrase.</text>
    <text x="24" y="152" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="8" font-style="italic">✔ "The <tspan font-weight="700">cost</tspan> [of new computers] <tspan font-weight="700">has</tspan> risen."</text>

    <text x="24" y="174" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Either... Or / Neither... Nor:</text>
    <text x="24" y="190" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">Verb agrees with the <tspan font-weight="700" fill="#15803D">CLOSER</tspan> subject.</text>
    <text x="24" y="204" fill="#B91C1C" font-family="system-ui, sans-serif" font-size="8" font-style="italic">✔ "Either the manager or the <tspan font-weight="700">technicians are</tspan> guilty."</text>

    <text x="24" y="226" fill="#991B1B" font-family="system-ui, sans-serif" font-size="10" font-weight="700">4. Collective Nouns (Units):</text>
    <text x="24" y="242" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">"The committee <tspan font-weight="700">has</tspan> voted." (Acting as a single unit)</text>
    <text x="24" y="260" fill="#1F2937" font-family="system-ui, sans-serif" font-size="8.5">"The team <tspan font-weight="700">have</tspan> different opinions." (Acting individually)</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(25, 412)" filter="url(#l10Sh)">
    <rect width="750" height="52" rx="10" fill="#1E1B4B"/>
    <text x="35" y="31" fill="#C7D2FE" font-family="system-ui, sans-serif" font-size="11" font-weight="700">AGREEMENT &amp; VOICE HARMONY:</text>
    <text x="260" y="31" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5">
      Match verb number to true subject; choose Active for vitality, Passive for objective focus.
    </text>
  </g>
</svg>"""
