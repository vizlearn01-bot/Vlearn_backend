"""
VLearn CBC Grade 10 ICT — Topic 5: Presentation Software
Full Structured Lesson Card Definitions (Lessons 5.1.1 to 5.1.5)
"""

import re

def sanitize_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# HIGH PRECISION VECTOR SVGS FOR TOPIC 5: PRESENTATION SOFTWARE
# =====================================================================

SVG_PRESENTATION_COMMUNICATION_LOOP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Visual Oral Communication Loop &amp; Dual-Coding Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How presentation software synchronizes auditory narration and visual anchors to maximize comprehension</text>

  <!-- Node 1: The Speaker -->
  <g transform="translate(45, 95)">
    <rect width="250" height="245" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="34" rx="8" fill="#0284c7"/>
    <text x="125" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. THE SPEAKER (PRESENTER)</text>
    
    <circle cx="125" cy="72" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="125" y="78" font-size="18" text-anchor="middle">🎙️</text>
    
    <text x="15" y="118" font-size="11" font-weight="bold" fill="#38bdf8">• Auditory Channel:</text>
    <text x="15" y="135" font-size="9.5" fill="#cbd5e1">Delivers verbal storytelling, context, nuances, pacing, and vocal inflection.</text>
    
    <text x="15" y="168" font-size="11" font-weight="bold" fill="#38bdf8">• Interaction &amp; Guidance:</text>
    <text x="15" y="185" font-size="9.5" fill="#cbd5e1">Maintains eye contact, reads room reactions, and answers live questions.</text>
    
    <rect x="15" y="212" width="220" height="22" rx="4" fill="#1e293b"/>
    <text x="125" y="227" font-size="9.5" fill="#94a3b8" text-anchor="middle">The human communicator &amp; guide</text>
  </g>

  <!-- Connector 1 -> 2 -->
  <g transform="translate(295, 185)">
    <path d="M 5 15 L 45 15" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <polygon points="45,10 55,15 45,20" fill="#38bdf8"/>
    <text x="28" y="5" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Controls</text>
    <text x="28" y="32" font-size="8.5" fill="#94a3b8" text-anchor="middle">Clicker/Notes</text>
  </g>

  <!-- Node 2: Presentation Interface (Visual Anchor) -->
  <g transform="translate(355, 95)">
    <rect width="250" height="245" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="250" height="34" rx="8" fill="#059669"/>
    <text x="125" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PRESENTATION INTERFACE</text>
    
    <circle cx="125" cy="72" r="22" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="125" y="78" font-size="18" text-anchor="middle">📊</text>
    
    <text x="15" y="118" font-size="11" font-weight="bold" fill="#34d399">• Visual Anchor Canvas:</text>
    <text x="15" y="135" font-size="9.5" fill="#cbd5e1">High-impact charts, key terms, diagrams, and photos projected clearly.</text>
    
    <text x="15" y="168" font-size="11" font-weight="bold" fill="#34d399">• 6x6 Modular Structure:</text>
    <text x="15" y="185" font-size="9.5" fill="#cbd5e1">Prevents information overload with succinct bullet anchors and hierarchy.</text>
    
    <rect x="15" y="212" width="220" height="22" rx="4" fill="#1e293b"/>
    <text x="125" y="227" font-size="9.5" fill="#94a3b8" text-anchor="middle">Supportive digital bridge</text>
  </g>

  <!-- Connector 2 -> 3 -->
  <g transform="translate(605, 185)">
    <path d="M 5 15 L 45 15" stroke="#34d399" stroke-width="3" fill="none"/>
    <polygon points="45,10 55,15 45,20" fill="#34d399"/>
    <text x="28" y="5" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Projects</text>
    <text x="28" y="32" font-size="8.5" fill="#94a3b8" text-anchor="middle">Visual Data</text>
  </g>

  <!-- Node 3: The Audience -->
  <g transform="translate(665, 95)">
    <rect width="250" height="245" rx="12" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="250" height="34" rx="8" fill="#d97706"/>
    <text x="125" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. THE AUDIENCE</text>
    
    <circle cx="125" cy="72" r="22" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="125" y="78" font-size="18" text-anchor="middle">👥</text>
    
    <text x="15" y="118" font-size="11" font-weight="bold" fill="#fbbf24">• Dual-Coding Synergy:</text>
    <text x="15" y="135" font-size="9.5" fill="#cbd5e1">Ears hear spoken explanation while eyes scan concise graphical anchors.</text>
    
    <text x="15" y="168" font-size="11" font-weight="bold" fill="#fbbf24">• 6x Memory Retention:</text>
    <text x="15" y="185" font-size="9.5" fill="#cbd5e1">Cognitive load remains low; concepts are synthesized and remembered long-term.</text>
    
    <rect x="15" y="212" width="220" height="22" rx="4" fill="#1e293b"/>
    <text x="125" y="227" font-size="9.5" fill="#94a3b8" text-anchor="middle">Engaged and attentive listeners</text>
  </g>

  <!-- Bottom Core Principle Banner -->
  <g transform="translate(45, 360)">
    <rect width="870" height="125" rx="12" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="25" y="26" font-size="12.5" font-weight="bold" fill="#38bdf8">The Dual-Coding Principle &amp; Golden Presentation Rule</text>
    <line x1="25" y1="36" x2="845" y2="36" stroke="#334155" stroke-width="1"/>
    
    <text x="25" y="58" font-size="11" font-weight="bold" fill="#ef4444">❌ Death by PowerPoint (Single Overloaded Channel):</text>
    <text x="25" y="74" font-size="10" fill="#cbd5e1">Pasting full textbook paragraphs on slides forces the audience to read instead of listen, causing immediate cognitive fatigue and total disconnect.</text>
    
    <text x="25" y="98" font-size="11" font-weight="bold" fill="#34d399">✅ Dual-Coding Mastery (Synchronized Dual Channels):</text>
    <text x="25" y="114" font-size="10" fill="#cbd5e1">Slides provide clean visual anchors (diagrams, keywords, statistics); the speaker provides depth, context, and emotion. Slides SUPPORT the speaker, not REPLACE them!</text>
  </g>
</svg>
""")

SVG_PRESENTATION_SOFTWARE_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Presentation Software Comparison &amp; Deployment Matrix</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Evaluating proprietary, cloud-native, open-source, and freemium presentation platforms</text>

  <!-- Platform 1: Microsoft PowerPoint -->
  <g transform="translate(45, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#0284c7"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Microsoft PowerPoint</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Proprietary / Commercial</text>
    
    <text x="15" y="93" font-size="11" font-weight="bold" fill="#38bdf8">• Deployment:</text>
    <text x="15" y="108" font-size="9.5" fill="#cbd5e1">Offline Desktop App + Cloud M365.</text>
    
    <text x="15" y="138" font-size="11" font-weight="bold" fill="#38bdf8">• Core Strengths:</text>
    <text x="15" y="153" font-size="9.5" fill="#cbd5e1">Advanced animation sequencing, 3D model support, deep charting, Presenter View.</text>
    
    <text x="15" y="210" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="225" font-size="9.5" fill="#cbd5e1">Paid subscription/license required.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">High-stakes corporate &amp; data decks</text>
  </g>

  <!-- Platform 2: Google Slides -->
  <g transform="translate(265, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#059669"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Google Slides</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Cloud-Native / Free Tier</text>
    
    <text x="15" y="93" font-size="11" font-weight="bold" fill="#34d399">• Deployment:</text>
    <text x="15" y="108" font-size="9.5" fill="#cbd5e1">Web Browser + Mobile Apps.</text>
    
    <text x="15" y="138" font-size="11" font-weight="bold" fill="#34d399">• Core Strengths:</text>
    <text x="15" y="153" font-size="9.5" fill="#cbd5e1">Real-time group collaboration, version history, automatic saving, link sharing.</text>
    
    <text x="15" y="210" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="225" font-size="9.5" fill="#cbd5e1">Requires internet; simpler animations.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">School group projects &amp; co-authoring</text>
  </g>

  <!-- Platform 3: LibreOffice Impress -->
  <g transform="translate(485, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#d97706"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LibreOffice Impress</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Free &amp; Open-Source (FOSS)</text>
    
    <text x="15" y="93" font-size="11" font-weight="bold" fill="#fbbf24">• Deployment:</text>
    <text x="15" y="108" font-size="9.5" fill="#cbd5e1">100% Offline Desktop (Linux/Win/Mac).</text>
    
    <text x="15" y="138" font-size="11" font-weight="bold" fill="#fbbf24">• Core Strengths:</text>
    <text x="15" y="153" font-size="9.5" fill="#cbd5e1">Zero cost, runs on low-spec PCs, ODF standard (.odp), no ads, fully offline.</text>
    
    <text x="15" y="210" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="225" font-size="9.5" fill="#cbd5e1">Traditional UI; no live web collaboration.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Offline school computer labs &amp; Linux</text>
  </g>

  <!-- Platform 4: Canva & Apple Keynote -->
  <g transform="translate(705, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#db2777"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Canva &amp; Apple Keynote</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#f472b6" text-anchor="middle">Design-Centric / Cloud / Mac</text>
    
    <text x="15" y="93" font-size="11" font-weight="bold" fill="#f472b6">• Deployment:</text>
    <text x="15" y="108" font-size="9.5" fill="#cbd5e1">Canva (Web/Freemium), Keynote (Apple OS).</text>
    
    <text x="15" y="138" font-size="11" font-weight="bold" fill="#f472b6">• Core Strengths:</text>
    <text x="15" y="153" font-size="9.5" fill="#cbd5e1">Stunning pre-built graphic templates, cinematic transitions, drag-and-drop visuals.</text>
    
    <text x="15" y="210" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="225" font-size="9.5" fill="#cbd5e1">Keynote is Apple-only; Canva needs net.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#f472b6" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Visual marketing, pitches, &amp; Apple users</text>
  </g>
</svg>
""")

SVG_SLIDE_LAYOUT_HIERARCHY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Slide Master Architecture &amp; Typographic Layout Hierarchy</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Enforcing global visual consistency and applying the 6x6 text legibility rule</text>

  <!-- Left: Slide Master Architecture -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#0284c7"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">SLIDE MASTER INHERITANCE SYSTEM</text>
    
    <!-- Primary Master Slide Node -->
    <g transform="translate(20, 50)">
      <rect width="380" height="75" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="10" y="10" width="80" height="55" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="50" y="40" font-size="11" fill="#38bdf8" text-anchor="middle">👑 MASTER</text>
      
      <text x="105" y="28" font-size="11.5" font-weight="bold" fill="#ffffff">Primary Slide Master (Theme Parent)</text>
      <text x="105" y="46" font-size="9.5" fill="#cbd5e1">• Global Font: Arial / Calibri (Sans-Serif)</text>
      <text x="105" y="62" font-size="9.5" fill="#cbd5e1">• Global Palette, Dark Navy Title, Logo in Corner</text>
    </g>

    <!-- Branching Downward Arrows -->
    <path d="M 210 130 L 210 155" stroke="#38bdf8" stroke-width="2" fill="none"/>
    <path d="M 75 155 L 345 155" stroke="#38bdf8" stroke-width="2" fill="none"/>
    <path d="M 75 155 L 75 170" stroke="#38bdf8" stroke-width="2" fill="none"/>
    <path d="M 210 155 L 210 170" stroke="#38bdf8" stroke-width="2" fill="none"/>
    <path d="M 345 155 L 345 170" stroke="#38bdf8" stroke-width="2" fill="none"/>

    <!-- Layout 1: Title Layout -->
    <g transform="translate(20, 175)">
      <rect width="115" height="110" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <rect x="10" y="12" width="95" height="24" rx="3" fill="#0284c7"/>
      <text x="57" y="28" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Title Slide</text>
      <rect x="15" y="46" width="85" height="10" fill="#334155"/>
      <rect x="25" y="62" width="65" height="8" fill="#475569"/>
      <text x="57" y="98" font-size="8" fill="#94a3b8" text-anchor="middle">Intro deck opening</text>
    </g>

    <!-- Layout 2: Title & Content -->
    <g transform="translate(152, 175)">
      <rect width="115" height="110" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <rect x="10" y="12" width="95" height="20" rx="3" fill="#059669"/>
      <text x="57" y="26" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Title &amp; Content</text>
      <circle cx="18" cy="45" r="3" fill="#34d399"/>
      <rect x="26" y="42" width="75" height="6" fill="#cbd5e1"/>
      <circle cx="18" cy="60" r="3" fill="#34d399"/>
      <rect x="26" y="57" width="65" height="6" fill="#cbd5e1"/>
      <circle cx="18" cy="75" r="3" fill="#34d399"/>
      <rect x="26" y="72" width="70" height="6" fill="#cbd5e1"/>
      <text x="57" y="98" font-size="8" fill="#34d399" text-anchor="middle">Standard 6x6 layout</text>
    </g>

    <!-- Layout 3: Comparison Layout -->
    <g transform="translate(285, 175)">
      <rect width="115" height="110" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <rect x="10" y="12" width="95" height="20" rx="3" fill="#0284c7"/>
      <text x="57" y="26" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Two Content</text>
      <rect x="12" y="42" width="40" height="38" rx="2" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <rect x="62" y="42" width="40" height="38" rx="2" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="57" y="98" font-size="8" fill="#94a3b8" text-anchor="middle">Side-by-side view</text>
    </g>

    <!-- Master Slide Benefit Box -->
    <g transform="translate(20, 300)">
      <rect width="380" height="70" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">Global Synchronization Benefit:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Updating the Master Slide title font or logo instantly cascades</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">across all 50 slides in a deck without touching individual pages!</text>
    </g>
  </g>

  <!-- Right: 6x6 Legibility & Hierarchy Mockup -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#059669"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">THE 6x6 RULE &amp; TYPOGRAPHIC HIERARCHY</text>
    
    <!-- Slide Screen Simulation -->
    <g transform="translate(20, 50)">
      <rect width="380" height="230" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
      
      <!-- Slide Title -->
      <rect x="20" y="15" width="340" height="32" rx="4" fill="#0284c7"/>
      <text x="190" y="36" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Solar Energy in Kenya (36-44pt)</text>
      
      <!-- Bullet 1 -->
      <circle cx="35" cy="70" r="4" fill="#0284c7"/>
      <text x="48" y="74" font-size="10.5" font-weight="bold" fill="#0f172a">Abundant sunshine across arid counties (20-24pt)</text>
      
      <!-- Bullet 2 -->
      <circle cx="35" cy="98" r="4" fill="#0284c7"/>
      <text x="48" y="102" font-size="10.5" font-weight="bold" fill="#0f172a">Powers off-grid solar irrigation pumps</text>
      
      <!-- Bullet 3 -->
      <circle cx="35" cy="126" r="4" fill="#0284c7"/>
      <text x="48" y="130" font-size="10.5" font-weight="bold" fill="#0f172a">Reduces farm diesel generator emissions</text>
      
      <!-- Bullet 4 -->
      <circle cx="35" cy="154" r="4" fill="#0284c7"/>
      <text x="48" y="158" font-size="10.5" font-weight="bold" fill="#0f172a">Mobile pay-as-you-go financing models</text>
      
      <!-- Footer -->
      <line x1="20" y1="195" x2="360" y2="195" stroke="#cbd5e1" stroke-width="1"/>
      <text x="25" y="212" font-size="8.5" fill="#64748b">VLearn Senior ICT • Grade 10</text>
      <text x="350" y="212" font-size="8.5" fill="#64748b" text-anchor="end">Slide 4</text>
    </g>

    <!-- Design Rules Summary Box -->
    <g transform="translate(20, 295)">
      <rect width="380" height="75" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#34d399">Four Mandatory Slide Design Rules:</text>
      <text x="15" y="34" font-size="9" fill="#cbd5e1">1. The 6x6 Rule: Max 6 bullet points per slide, max 6 words per bullet.</text>
      <text x="15" y="48" font-size="9" fill="#cbd5e1">2. Contrast Ratio: Dark text on light BG, or crisp white text on navy BG.</text>
      <text x="15" y="62" font-size="9" fill="#cbd5e1">3. Legibility: Never use body text smaller than 20pt (invisible in back row).</text>
    </g>
  </g>
</svg>
""")

SVG_MULTIMEDIA_ANIMATION_FLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Multimedia, Animation Sequencing &amp; Interactive Hyperlinks</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Controlling audience attention with paced entrance animations and non-linear interactive branching</text>

  <!-- Left: Animation Sequencing Timeline -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#9333ea"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ANIMATION SEQUENCING &amp; PACING</text>
    
    <!-- Timeline Event 1 -->
    <g transform="translate(20, 55)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <circle cx="30" cy="30" r="14" fill="#9333ea"/>
      <text x="30" y="35" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="60" y="25" font-size="11" font-weight="bold" fill="#c084fc">Title Entrance (Fade / Wipe)</text>
      <text x="60" y="42" font-size="9" fill="#cbd5e1">Start: With Previous • Duration: 0.50s • Smooth introduction</text>
    </g>

    <!-- Timeline Event 2 -->
    <g transform="translate(20, 125)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <circle cx="30" cy="30" r="14" fill="#0284c7"/>
      <text x="30" y="35" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="60" y="25" font-size="11" font-weight="bold" fill="#38bdf8">Bullet Point 1 Entrance (Fade In)</text>
      <text x="60" y="42" font-size="9" fill="#cbd5e1">Start: On Click • Speaker explains point 1 before revealing point 2</text>
    </g>

    <!-- Timeline Event 3 -->
    <g transform="translate(20, 195)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <circle cx="30" cy="30" r="14" fill="#059669"/>
      <text x="30" y="35" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="60" y="25" font-size="11" font-weight="bold" fill="#34d399">Bullet Point 2 Entrance (Fade In)</text>
      <text x="60" y="42" font-size="9" fill="#cbd5e1">Start: On Click • Keeps audience eyes synchronized with voice</text>
    </g>

    <!-- Golden Rule Box -->
    <g transform="translate(20, 275)">
      <rect width="380" height="95" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#c084fc">Golden Rules of Animation &amp; Media:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Speed: Keep transitions between 0.5s and 1.0s (fast &amp; crisp).</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Style: Use subtle Fade or Push; avoid distracting spinning/chimes.</text>
      <text x="15" y="66" font-size="9" fill="#cbd5e1">• Aspect Ratio: Always hold Shift while dragging corner handles to</text>
      <text x="15" y="80" font-size="9" fill="#cbd5e1">  prevent stretching and squishing photos!</text>
    </g>
  </g>

  <!-- Right: Non-Linear Hyperlink Branching -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#0284c7"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">NON-LINEAR INTERACTIVE HYPERLINKING</text>
    
    <!-- Main Menu Hub Slide -->
    <g transform="translate(130, 55)">
      <rect width="160" height="90" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="5" y="5" width="150" height="18" rx="3" fill="#0284c7"/>
      <text x="80" y="17" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Slide 2: Main Menu Hub</text>
      
      <!-- Interactive Buttons inside Slide -->
      <rect x="15" y="30" width="130" height="15" rx="3" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
      <text x="80" y="41" font-size="7.5" fill="#34d399" text-anchor="middle">🔗 1. Solar Energy</text>
      
      <rect x="15" y="49" width="130" height="15" rx="3" fill="#0f172a" stroke="#fbbf24" stroke-width="1"/>
      <text x="80" y="60" font-size="7.5" fill="#fbbf24" text-anchor="middle">🔗 2. Wind Power</text>
      
      <rect x="15" y="68" width="130" height="15" rx="3" fill="#0f172a" stroke="#f472b6" stroke-width="1"/>
      <text x="80" y="79" font-size="7.5" fill="#f472b6" text-anchor="middle">🔗 3. Geothermal</text>
    </g>

    <!-- Branching Lines -->
    <path d="M 150 145 L 80 185" stroke="#34d399" stroke-width="2" stroke-dasharray="4" fill="none"/>
    <path d="M 210 145 L 210 185" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4" fill="none"/>
    <path d="M 270 145 L 340 185" stroke="#f472b6" stroke-width="2" stroke-dasharray="4" fill="none"/>

    <!-- Destination Slide 1: Solar -->
    <g transform="translate(20, 195)">
      <rect width="115" height="80" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <rect x="5" y="5" width="105" height="16" rx="2" fill="#059669"/>
      <text x="57" y="16" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Slide 3: Solar</text>
      <text x="10" y="36" font-size="7" fill="#cbd5e1">• Solar irradiance</text>
      <text x="10" y="48" font-size="7" fill="#cbd5e1">• Battery banks</text>
      <!-- Return Button -->
      <rect x="10" y="58" width="95" height="14" rx="2" fill="#0284c7"/>
      <text x="57" y="68" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">↩ Return to Menu</text>
    </g>

    <!-- Destination Slide 2: Wind -->
    <g transform="translate(152, 195)">
      <rect width="115" height="80" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
      <rect x="5" y="5" width="105" height="16" rx="2" fill="#d97706"/>
      <text x="57" y="16" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Slide 4: Wind</text>
      <text x="10" y="36" font-size="7" fill="#cbd5e1">• Lake Turkana site</text>
      <text x="10" y="48" font-size="7" fill="#cbd5e1">• Grid feed-in</text>
      <!-- Return Button -->
      <rect x="10" y="58" width="95" height="14" rx="2" fill="#0284c7"/>
      <text x="57" y="68" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">↩ Return to Menu</text>
    </g>

    <!-- Destination Slide 3: Geothermal -->
    <g transform="translate(285, 195)">
      <rect width="115" height="80" rx="6" fill="#1e293b" stroke="#f472b6" stroke-width="1.5"/>
      <rect x="5" y="5" width="105" height="16" rx="2" fill="#db2777"/>
      <text x="57" y="16" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Slide 5: Geo</text>
      <text x="10" y="36" font-size="7" fill="#cbd5e1">• Olkaria plant</text>
      <text x="10" y="48" font-size="7" fill="#cbd5e1">• Clean baseload</text>
      <!-- Return Button -->
      <rect x="10" y="58" width="95" height="14" rx="2" fill="#0284c7"/>
      <text x="57" y="68" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">↩ Return to Menu</text>
    </g>

    <!-- Interactive Navigation Benefit Box -->
    <g transform="translate(20, 290)">
      <rect width="380" height="80" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#38bdf8">Interactive Presentation Architecture:</text>
      <text x="15" y="34" font-size="9" fill="#cbd5e1">• Hyperlinks transform linear slide decks into dynamic kiosk apps.</text>
      <text x="15" y="48" font-size="9" fill="#cbd5e1">• Presenters can jump directly to specific topics based on audience</text>
      <text x="15" y="62" font-size="9" fill="#cbd5e1">  inquiries and return seamlessly using Action Buttons (Ctrl + K).</text>
    </g>
  </g>
</svg>
""")

SVG_PRESENTATION_DELIVERY_MODES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Presenter View Dual-Monitor Architecture &amp; Live Delivery Controls</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Extending screens to manage secret notes, live timers, and digital ink while projecting full-screen slides</text>

  <!-- Left: Presenter's Secret Dashboard (Laptop Screen) -->
  <g transform="translate(45, 90)">
    <rect width="490" height="280" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    
    <!-- Title Bar -->
    <rect width="490" height="28" rx="8" fill="#1e293b"/>
    <circle cx="18" cy="14" r="5" fill="#ef4444"/>
    <circle cx="34" cy="14" r="5" fill="#f59e0b"/>
    <circle cx="50" cy="14" r="5" fill="#10b981"/>
    <text x="245" y="19" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Presenter View Dashboard (Display: EXTEND)</text>
    
    <!-- Top Bar: Timer & Tools -->
    <g transform="translate(15, 38)">
      <rect width="460" height="26" rx="4" fill="#1e293b"/>
      <text x="15" y="18" font-size="10.5" font-weight="bold" fill="#34d399">⏱️ Elapsed: 04:15</text>
      <text x="140" y="18" font-size="10.5" fill="#cbd5e1">Slide 3 of 12</text>
      <text x="340" y="18" font-size="10.5" fill="#38bdf8">🖋️ Pen  🔦 Laser  🔍 Grid</text>
    </g>

    <!-- Sub-Pane 1: Current Slide Visible to Audience -->
    <g transform="translate(15, 72)">
      <rect width="250" height="150" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
      <rect x="10" y="8" width="230" height="22" rx="3" fill="#0284c7"/>
      <text x="125" y="23" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Renewable Wind Energy</text>
      <text x="15" y="48" font-size="8.5" fill="#0f172a">• Lake Turkana Wind Farm (310 MW)</text>
      <text x="15" y="65" font-size="8.5" fill="#0f172a">• Powers 1+ million Kenyan homes</text>
      <text x="15" y="82" font-size="8.5" fill="#0f172a">• Zero carbon emissions generated</text>
      <line x1="15" y1="120" x2="235" y2="120" stroke="#cbd5e1" stroke-width="1"/>
      <text x="125" y="138" font-size="8" font-weight="bold" fill="#0284c7" text-anchor="middle">CURRENT SLIDE (AUDIENCE VIEW)</text>
    </g>

    <!-- Sub-Pane 2: Next Slide Preview -->
    <g transform="translate(275, 72)">
      <rect width="200" height="65" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="100" y="18" font-size="8.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">NEXT SLIDE PREVIEW</text>
      <text x="15" y="38" font-size="8" fill="#cbd5e1">Slide 4: Geothermal Power in Naivasha</text>
      <text x="15" y="52" font-size="7.5" fill="#94a3b8">Ready to transition...</text>
    </g>

    <!-- Sub-Pane 3: Speaker Notes Area -->
    <g transform="translate(275, 145)">
      <rect width="200" height="77" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="100" y="16" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">SECRET SPEAKER NOTES (A+ / A-)</text>
      <text x="10" y="32" font-size="7.5" font-weight="bold" fill="#38bdf8">• FACT:</text>
      <text x="45" y="32" font-size="7.5" fill="#cbd5e1">Cost was KSh 70 billion.</text>
      <text x="10" y="47" font-size="7.5" font-weight="bold" fill="#38bdf8">• BRIDGE:</text>
      <text x="50" y="47" font-size="7.5" fill="#cbd5e1">Connect wind to geothermal next.</text>
      <text x="10" y="62" font-size="7.5" font-weight="bold" fill="#fbbf24">• CUE:</text>
      <text x="40" y="62" font-size="7.5" fill="#cbd5e1">Pause &amp; ask: Who has visited Loyangalani?</text>
    </g>

    <!-- Navigation Control Bar -->
    <g transform="translate(15, 230)">
      <rect width="460" height="36" rx="6" fill="#1e293b"/>
      <text x="35" y="23" font-size="12" fill="#38bdf8">⏮️ Previous</text>
      <text x="210" y="23" font-size="11" font-weight="bold" fill="#ffffff">Slide 3 of 12</text>
      <text x="375" y="23" font-size="12" fill="#38bdf8">Next ⏭️</text>
    </g>
  </g>

  <!-- Right: Projector / Big Screen (Audience View) -->
  <g transform="translate(560, 90)">
    <rect width="355" height="280" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    
    <rect width="355" height="28" rx="8" fill="#059669"/>
    <text x="177" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Audience Projector Screen (Full 1080p)</text>
    
    <g transform="translate(20, 45)">
      <rect width="315" height="215" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
      
      <rect x="15" y="15" width="285" height="32" rx="4" fill="#0284c7"/>
      <text x="157" y="36" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Renewable Wind Energy</text>
      
      <circle cx="28" cy="72" r="3" fill="#0284c7"/>
      <text x="38" y="76" font-size="10" font-weight="bold" fill="#0f172a">Lake Turkana Wind Farm (310 MW)</text>
      
      <circle cx="28" cy="102" r="3" fill="#0284c7"/>
      <text x="38" y="106" font-size="10" font-weight="bold" fill="#0f172a">Powers 1+ million Kenyan households</text>
      
      <circle cx="28" cy="132" r="3" fill="#0284c7"/>
      <text x="38" y="136" font-size="10" font-weight="bold" fill="#0f172a">Zero carbon greenhouse gas emissions</text>
      
      <line x1="15" y1="180" x2="300" y2="180" stroke="#cbd5e1" stroke-width="1"/>
      <text x="20" y="198" font-size="8.5" fill="#64748b">VLearn Senior ICT • Grade 10</text>
      <text x="295" y="198" font-size="8.5" fill="#64748b" text-anchor="end">Slide 3</text>
    </g>
  </g>

  <!-- Bottom Delivery Best Practices Bar -->
  <g transform="translate(45, 385)">
    <rect width="870" height="100" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="20" y="24" font-size="11.5" font-weight="bold" fill="#38bdf8">Presentation Delivery &amp; Digital Accessibility Pillars:</text>
    <line x1="20" y1="32" x2="850" y2="32" stroke="#334155" stroke-width="1"/>
    
    <text x="20" y="52" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#38bdf8">1. Display Settings:</tspan> Always use <tspan font-weight="bold" fill="#ffffff">Extend (Win + P)</tspan> instead of Duplicate so private notes remain completely invisible to the audience.</text>
    <text x="20" y="70" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#34d399">2. 3-Part Speaker Notes:</tspan> Write concise anchors: <tspan font-weight="bold" fill="#38bdf8">[FACT]</tspan> specific metrics, <tspan font-weight="bold" fill="#38bdf8">[BRIDGE]</tspan> transitions, and <tspan font-weight="bold" fill="#fbbf24">[CUE]</tspan> audience interactive prompts.</text>
    <text x="20" y="88" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#f472b6">3. Accessibility (WCAG):</tspan> Add descriptive Alt-Text to charts and enable real-time closed captioning for inclusive audience participation.</text>
  </g>
</svg>
""")

# =====================================================================
# FULL STRUCTURED LESSON CARD DEFINITIONS: TOPIC 5 (5 LESSONS)
# =====================================================================

TOPIC_5_LESSONS = [
    # =========================================================================
    # LESSON 5.1.1: Meaning and Purpose of Presentation Software
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Purpose of Presentation Software",
        "unit_description": "Foundations of visual oral communication, the dual-coding cognitive theory, slide deck architecture, and the fundamental principle of supporting rather than replacing the speaker.",
        "lesson_title": "Meaning and Purpose of Presentation Software",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Communication in Modern Presentations",
                    "content": {
                        "title": "Oral and Visual Synergy in Public Speaking",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Video_conference_call_meeting.jpg",
                        "caption": "A presenter engaging an audience using digital visual slides to reinforce oral explanations, demonstrating how dual sensory channels boost memory retention.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Power of Visual Oral Communication",
                    "content": {
                        "text": "Think about the last time you listened to a speaker. What made their message memorable? Was it a long, monotone speech full of dense text, or did they use striking images, clear charts, and structured slides that helped you instantly grasp their points?\n\n**Presentation software** is designed to transform dry, dense information into a multisensory communication experience. It provides a visual canvas that helps you tell compelling stories, support logical arguments, and connect deeply with your audience. Rather than acting as an electronic teleprompter, presentation slides serve as cognitive visual anchors that reinforce your spoken words."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define presentation software, slides, slideshows, and visual aids using functional and technical terms\n- Explain the Dual-Coding Theory and how visual and auditory channels work together to boost retention\n- Describe the 3 core functions of presentation software: Enhancing Retention, Directing Focus, and Structuring Messages\n- Contrast effective visual-anchor slide decks with text-overloaded 'Death by PowerPoint' presentations"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Presentation Terminology",
                    "content": {
                        "term": "Presentation Software",
                        "definition": "An application program designed to structure, format, and display multimedia digital slides to support visual oral communication.",
                        "simple": "A computer program used to create slides with text, pictures, and charts that you project on a screen while speaking.",
                        "technical": "A productivity software suite providing tools for slide layout design, vector graphics, typography, media integration, and full-screen sequenced playback.",
                        "example": "Using Microsoft PowerPoint, Google Slides, or LibreOffice Impress to pitch a school science project."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 3 Pillars of Presentation Software",
                    "content": {
                        "text": "Presentation software performs three vital pedagogical and communication functions:\n\n1. **Enhancing Cognitive Retention (The Dual-Coding Theory):** Human working memory possesses two independent channels: visual and auditory. When a speaker talks while projecting clear visual anchors, both channels process the message simultaneously. Studies show this dual-channel reinforcement makes information **up to six times easier to remember** than speech alone.\n2. **Directing Audience Focus:** Well-designed slides use contrast, font size, and spatial layout to guide viewer attention. An audience member should be able to glance at a slide, understand the key takeaway in **3 seconds**, and immediately return their focus to the speaker.\n3. **Structuring the Speaker's Narrative:** Slide decks force the speaker to organize ideas modularly into a logical four-part progression:\n   - **Introduction:** Defining the core problem or theme\n   - **Evidence & Analysis:** Presenting facts, data, and charts\n   - **Proposed Solution:** Outlining actionable steps\n   - **Call to Action / Conclusion:** Summarizing key takeaways and inspiring next steps."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Visual Oral Communication Loop",
                    "content": {
                        "title": "The 3-Node Dual-Coding Communication Pipeline",
                        "caption": "High-precision vector architecture showing how the speaker's vocal narrative and the software's visual anchors combine to deliver synchronized learning to the audience.",
                        "svg_content": SVG_PRESENTATION_COMMUNICATION_LOOP
                    }
                },
                {
                    "type": "step_process",
                    "title": "Structuring a High-Impact Presentation Deck",
                    "content": {
                        "intro": "Follow this standard 4-phase pedagogical framework when building any academic or professional slide deck:",
                        "steps": [
                            {"title": "1. Hook & Introduction (Slides 1-2)", "description": "State the title, introduce your team, and grab attention with a provocative question, striking statistic, or real-world problem statement."},
                            {"title": "2. Data & Problem Analysis (Slides 3-4)", "description": "Present evidence using clean charts and diagrams rather than dense text paragraphs. Explain the causes and effects clearly."},
                            {"title": "3. Solution & Recommendations (Slides 5-6)", "description": "Outline your proposed solution, project roadmap, or experimental findings in clear, sequential bullet points."},
                            {"title": "4. Conclusion & Call to Action (Slide 7)", "description": "Synthesize main conclusions, invite questions from the audience, and leave viewers with a memorable final thought."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Community Agriculture Pitch in Nakuru",
                    "content": {
                        "title": "Pitching Solar-Powered Drip Irrigation to County Investors",
                        "scenario": "A youth farming group in Nakuru prepared a 6-slide presentation to request funding for solar water pumps from the county enterprise fund.",
                        "impact": "In their initial draft, they copied entire pages from agricultural textbooks onto the slides. The evaluators became tired of reading and missed the core pitch.",
                        "solution": "They redesigned the deck: replacing paragraphs with photos of their test farm, a bar graph showing a 40% water savings metric, and 3-word bullet anchors. The revised pitch won unanimous approval."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: 'Death by PowerPoint'",
                    "content": {
                        "misconception": "A good slide deck should contain every single word the speaker intends to say so nothing is forgotten.",
                        "correction": "When full paragraphs are displayed, the human brain cannot read the text and listen to the voice simultaneously. The audience stops listening, experiences cognitive overload, and tunes out. Slides must provide visual anchors; the speaker provides the narration."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Converting Text Walls into Visual Anchors",
                    "content": {
                        "mistake": "Pasting full sentences (50+ words) into slide body placeholders.",
                        "why_it_happens": "Presenters lack confidence in memorizing their speech and use slides as an electronic script.",
                        "fix_solution": "Apply the 6x6 rule: summarize each paragraph into a short 4-word keyword bullet point, and place your detailed speaking cues in the private Speaker Notes pane."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Cognitive Role of Slides",
                    "content": {
                        "question": "According to the Dual-Coding Theory, why are visual slides with minimal text more effective than oral-only speeches?",
                        "options": [
                            "Visual slides allow the speaker to leave the room while the audience reads alone",
                            "They engage both auditory and visual cognitive channels simultaneously, increasing retention up to six times",
                            "Slide software automatically translates speech into foreign languages in real time",
                            "Digital projectors consume less electrical power when displaying minimal text"
                        ],
                        "correct": "B",
                        "explanation": "Dual-Coding Theory explains that when auditory narration is synchronized with concise visual anchors, the brain processes information across separate channels, boosting comprehension and memory retention."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Avoiding Cognitive Overload",
                    "content": {
                        "question": "A student copies three full paragraphs from a geography textbook onto a single presentation slide. What pedagogical problem does this cause?",
                        "options": [
                            "The presentation software will crash due to character memory limits",
                            "The audience will try to read the screen instead of listening, causing cognitive overload and fatigue",
                            "The projector bulb will overheat due to high character density",
                            "The font color will automatically invert to black"
                        ],
                        "correct": "B",
                        "explanation": "Displaying dense text blocks forces the audience to read instead of listening to the speaker, resulting in cognitive overload and loss of focus ('Death by PowerPoint')."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Introduction to Presentation Software & Visual Communication",
                    "content": {
                        "title": "Visual Presentation Fundamentals & Audience Engagement",
                        "youtube_id": "Vl0H-qTclOg",
                        "url": "https://www.youtube.com/watch?v=Vl0H-qTclOg",
                        "description": "Comprehensive tutorial introducing presentation software tools, slide deck structure, and effective visual communication strategies."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Support, Not Replace:** Slides exist to support the speaker with high-impact visual anchors, never to act as a teleprompter.\n2. **Dual-Coding Power:** Synchronizing vocal narration with clear graphics engages dual brain channels, multiplying memory retention.\n3. **3-Second Rule:** Slides must be simple enough for the audience to digest within 3 seconds before returning their eyes to the presenter.\n4. **Modular Narrative:** Effective presentations follow a structured sequence: Hook ➔ Analysis ➔ Solution ➔ Call to Action."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5.1.2: Common Presentation Software and Selection
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Common Presentation Software and Selection",
        "unit_description": "Comparative evaluation of proprietary, open-source, and cloud-native presentation platforms (PowerPoint, Google Slides, LibreOffice Impress, Keynote, Canva) and key hardware/connectivity selection criteria.",
        "lesson_title": "Common Presentation Software and Selection",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Evaluating Modern Presentation Software Platforms",
                    "content": {
                        "title": "Digital Productivity Suites in the Computer Lab",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Computer_classroom_in_Kenya.jpg",
                        "caption": "Students in a computer lab exploring diverse presentation applications, highlighting the importance of selecting the right software for specific connectivity and hardware environments.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Choosing the Right Digital Canvas",
                    "content": {
                        "text": "When you set out to build a slide deck, which program should you open? You might have Microsoft PowerPoint installed on your desktop, or you might prefer Google Slides because it allows you to collaborate with classmates in real time over the web. Other situations might require free, open-source tools like LibreOffice Impress or graphic design platforms like Canva.\n\nSelecting the wrong tool can lead to severe technical problems: files failing to open on school computers, missing internet connections during presentations, or broken font styling. Mastering the strengths, licensing models, and system requirements of each platform ensures smooth, stress-free presentations."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Classify presentation applications into proprietary, open-source, cloud-native, and freemium categories\n- Compare Microsoft PowerPoint, Google Slides, LibreOffice Impress, Apple Keynote, and Canva\n- Apply four critical selection criteria: Connectivity, Collaboration, Host Hardware, and Data Complexity\n- Prevent presentation file format incompatibility issues across different operating systems"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Software Licensing & Deployment Models",
                    "content": {
                        "term": "Proprietary vs. Open-Source vs. Cloud-Native Software",
                        "definition": "The legal licensing structure and operational deployment architecture governing how presentation software is accessed, executed, and stored.",
                        "simple": "Proprietary software is paid; open-source is completely free to modify and download; cloud-native runs in your web browser.",
                        "technical": "Proprietary software enforces closed source licenses (e.g. M365); FOSS (Free and Open-Source Software) uses open licenses (e.g. GPL/ODF); Cloud-native tools execute on remote web servers over HTTPS.",
                        "example": "PowerPoint (Proprietary), LibreOffice Impress (Open-Source), Google Slides (Cloud-Native)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 4 Selection Decision Criteria",
                    "content": {
                        "text": "When choosing presentation software for a project, evaluate these four operational factors:\n\n1. **Network Connectivity & Reliability:**\n   - If presenting in a venue with **no internet or unstable Wi-Fi**, use offline desktop suites like **PowerPoint** or **LibreOffice Impress**.\n   - If fast, reliable internet is guaranteed, cloud tools like **Google Slides** or **Canva** provide instant accessibility.\n2. **Team Collaboration Requirements:**\n   - For group projects where multiple students must edit different slides simultaneously, **Google Slides** is the gold standard, eliminating confusing email versioning (`project_final_v4.pptx`).\n3. **Presentation Room Hardware & Operating System:**\n   - If the venue computer runs Linux, use **LibreOffice Impress** or export to universal PDF.\n   - If designing on a Mac using **Apple Keynote**, always export a copy as `.pptx` or `.pdf` before presenting on a Windows machine.\n4. **Data Complexity & Advanced Animation:**\n   - For intricate financial models, embedded 3D objects, or advanced trigger animations, **Microsoft PowerPoint** offers the deepest feature set."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Presentation Software Comparison Matrix",
                    "content": {
                        "title": "Comprehensive Presentation Software Platforms Matrix",
                        "caption": "Comparative analysis mapping PowerPoint, Google Slides, LibreOffice Impress, Keynote, and Canva across licensing, deployment, strengths, and optimal use cases.",
                        "svg_content": SVG_PRESENTATION_SOFTWARE_MATRIX
                    }
                },
                {
                    "type": "step_process",
                    "title": "Decision Framework for Software Selection",
                    "content": {
                        "intro": "Follow this 4-step decision sequence before starting your next presentation project:",
                        "steps": [
                            {"title": "1. Audit Internet & Venue Infrastructure", "description": "Check if the delivery hall has reliable Wi-Fi and projector connections (HDMI/VGA). If offline, choose a local desktop application."},
                            {"title": "2. Determine Collaboration Needs", "description": "If co-authoring with 3+ classmates across different locations, create a shared Google Slides document with edit permissions."},
                            {"title": "3. Evaluate Visual & Template Needs", "description": "If creating a visual marketing pitch or graphic poster, utilize Canva's pre-built template libraries."},
                            {"title": "4. Generate Universal Backup Formats", "description": "Always export a fixed-layout .pdf and a standard .pptx backup copy to a USB drive to ensure compatibility on any host PC."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Rural School Exhibition in Turkana",
                    "content": {
                        "title": "Deploying LibreOffice Impress on Linux Laptops",
                        "scenario": "A secondary school in Lodwar prepared for a regional science fair using donated low-specification laptops running Ubuntu Linux with zero internet access.",
                        "impact": "Commercial software subscriptions were unaffordable and cloud-based tools failed to load without network connectivity.",
                        "solution": "The ICT teacher installed LibreOffice Impress on all laptops. Students designed clean, formatted presentations locally in OpenDocument (.odp) format and presented flawlessly."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The Universal Cloud Assumption",
                    "content": {
                        "misconception": "Cloud presentation software is always superior because you don't need to carry a USB flash drive.",
                        "correction": "Relying purely on cloud presentations during live events is a major risk. School auditoriums, conference centers, and rural venues frequently experience Wi-Fi drops, bandwidth choking, or login firewalls. Always maintain an offline desktop backup."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Cross-Platform Font & Format Breakage",
                    "content": {
                        "mistake": "Designing a presentation in Apple Keynote with custom Mac fonts and expecting it to open natively on a Windows podium computer.",
                        "why_it_happens": "Keynote `.key` files are unsupported on standard Windows PCs, and non-standard fonts will substitute unpredictably.",
                        "fix_solution": "In Keynote, select File ➔ Export To ➔ PowerPoint (.pptx) or PDF. Standardize on universal fonts like Arial, Calibri, or Times New Roman."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Software Selection for Offline Linux Labs",
                    "content": {
                        "question": "A school computer lab contains computers running Linux OS with no internet connection. Which presentation software is the most suitable choice?",
                        "options": [
                            "Google Slides",
                            "Canva Web App",
                            "LibreOffice Impress",
                            "Apple Keynote"
                        ],
                        "correct": "C",
                        "explanation": "LibreOffice Impress is free, open-source, runs natively on Linux, and functions completely offline without requiring internet access or subscription licenses."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Real-Time Team Collaboration",
                    "content": {
                        "question": "Four Grade 10 students need to collaborate simultaneously on a single presentation from their respective homes. Which platform best supports real-time concurrent editing?",
                        "options": [
                            "LibreOffice Impress Desktop",
                            "Google Slides",
                            "Microsoft PowerPoint 2007 (Local Installation)",
                            "Windows Notepad"
                        ],
                        "correct": "B",
                        "explanation": "Google Slides is a cloud-native platform specifically engineered for real-time concurrent multi-user editing, automatic cloud saving, and version tracking."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Comparing Presentation Software: PowerPoint vs Google Slides vs Canva",
                    "content": {
                        "title": "Presentation Software Features & Workflow Comparison",
                        "youtube_id": "M6kUjU2U2f0",
                        "url": "https://www.youtube.com/watch?v=M6kUjU2U2f0",
                        "description": "In-depth comparison exploring feature sets, collaboration mechanics, offline capabilities, and design strengths across major presentation platforms."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Platform Diversity:** Presentation tools range from full desktop suites (PowerPoint) and open-source packages (Impress) to cloud-native platforms (Google Slides, Canva).\n2. **Selection Drivers:** Pick your software based on network availability, collaboration needs, host operating systems, and media complexity.\n3. **Offline Resilience:** Never rely exclusively on web tools in live halls without an offline `.pptx` or `.pdf` backup copy.\n4. **Cross-Platform Safety:** Stick to universal sans-serif fonts and export to standard formats when switching between Mac, Windows, and Linux."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5.1.3: Creating Slides and Structuring Content
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Creating Slides and Structuring Content",
        "unit_description": "Slide layout architectures, Slide Master/Theme inheritance, visual hierarchy, typography contrast, sizing standards, and the 6x6 rule for readable decks.",
        "lesson_title": "Creating Slides and Structuring Content",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "The Architecture of Clean Slide Design",
                    "content": {
                        "title": "Structured Digital Typography and Slide Layouts",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "A professional workspace demonstrating structured digital slide deck formatting, consistent typographic hierarchy, and clean spatial layout design.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Structuring Slides with Professional Precision",
                    "content": {
                        "text": "When you open a presentation program, you are greeted by a blank canvas. It is tempting to immediately type text boxes, pick random neon colors, and paste clipart everywhere. However, professional designers never start this way.\n\nThey plan structural layout first, enforce global design consistency using **Master Slides**, and adhere strictly to **visual hierarchy** and typography rules. Learning how to structure your content cleanly ensures that your audience can read, understand, and remember your ideas without visual strain or confusion."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define slide layouts, placeholders, Slide Masters, and visual hierarchy\n- Apply the 6x6 Rule to eliminate wordy slides and maintain high legibility\n- Configure typography standards (36-44pt titles, 20-24pt bullets) and high-contrast color schemes\n- Use Slide Master / Theme Builder to apply global branding and formatting changes across an entire presentation"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Master Slides & Layout Architecture",
                    "content": {
                        "term": "Slide Master (Master Slide / Theme Builder)",
                        "definition": "The top-level template in a presentation hierarchy that stores default formatting, background styles, color schemes, font choices, and placeholder positions for all slides.",
                        "simple": "A master control slide where any change you make (like adding a logo or changing the title font) automatically updates every slide in the presentation.",
                        "technical": "A hierarchical root template specifying XML styling attributes, layout inheritance trees, and placeholder bounding boxes across an entire presentation document.",
                        "example": "Adding your school badge to the Slide Master so it appears in the top corner of all 25 slides simultaneously."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 4 Pillars of Clean Slide Design",
                    "content": {
                        "text": "To ensure your slides look polished and readable from the back of a large classroom or auditorium, follow these four design pillars:\n\n1. **The 6x6 Rule (Text Minimization):**\n   - Never write complete paragraphs.\n   - Restrict each slide to a maximum of **6 bullet points**.\n   - Restrict each bullet point to a maximum of **6 words**.\n   - Slides should feature **conceptual keywords**, not your spoken script!\n2. **High Color Contrast Ratio:**\n   - **Light backgrounds** (white, light grey) require **dark text** (navy blue, charcoal black).\n   - **Dark backgrounds** (deep navy, dark slate) require **light text** (crisp white, soft gold).\n   - Never use low-contrast combinations like yellow text on white, or dark grey on black.\n3. **Typographic Hierarchy & Minimum Sizes:**\n   - **Slide Titles:** 36pt to 44pt (Bold, clean sans-serif typeface like Arial or Calibri).\n   - **Body Bullets:** 20pt to 24pt (Regular weight).\n   - **Captions & Footers:** 14pt to 16pt.\n   - *Rule of Thumb:* Any text smaller than 18pt is completely invisible to audience members seated beyond row three!\n4. **Slide Master Automation:**\n   - Avoid manually styling individual slides. Use **View ➔ Slide Master** to set font styles, colors, and logos once, ensuring 100% pixel-perfect uniformity across the deck."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Slide Master Architecture & Layout Hierarchy",
                    "content": {
                        "title": "Slide Master Inheritance and 6x6 Design Rules",
                        "caption": "Vector visual illustrating hierarchical template inheritance from the primary Slide Master down to specific child layouts, paired with typographic hierarchy benchmarks.",
                        "svg_content": SVG_SLIDE_LAYOUT_HIERARCHY
                    }
                },
                {
                    "type": "step_process",
                    "title": "Creating a Structured Master Slide Deck",
                    "content": {
                        "intro": "Follow these practical steps to build a unified 3-slide presentation deck using Slide Master:",
                        "steps": [
                            {"title": "1. Launch & Enter Slide Master View", "description": "Open your software (PowerPoint, Google Slides, or Impress). In PowerPoint, click View ➔ Slide Master; in Google Slides, click Slide ➔ Edit Theme."},
                            {"title": "2. Apply Master Styling to Parent Slide", "description": "Select the large top-most slide in the left hierarchy tree. Format the title placeholder to Arial 40pt Bold in Dark Navy, and apply a light grey background fill."},
                            {"title": "3. Add Global Branding Elements", "description": "Insert your school badge or project logo in the top-right corner of the master slide. Close Slide Master view to return to standard editing."},
                            {"title": "4. Build Content Slides Using Standard Layouts", "description": "Create Slide 1 with Title layout ('ICT in Agriculture'). Insert Slide 2 with Title & Content layout, and add three 6x6-compliant bullet points."},
                            {"title": "5. Save Your Structured File", "description": "Save the file as a standard presentation (.pptx or .odp) in your designated project folder."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: County Assembly Reporting in Machakos",
                    "content": {
                        "title": "Standardizing Departmental Decks with a Master Template",
                        "scenario": "The Machakos County ICT Department needed 12 different sub-county teams to report on rural internet connectivity projects.",
                        "impact": "Without a master template, each team used mismatched fonts, neon color schemes, and distorted county seals, creating an unprofessional and confusing report.",
                        "solution": "The lead ICT officer designed a single Master Template (.potx) with pre-locked branding, approved color palettes, and 6x6 layouts. All 12 reports merged into one cohesive, executive deck."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Manual Copy-Paste Formatting",
                    "content": {
                        "misconception": "It is just as fast to paste a logo manually onto 30 slides as it is to use the Slide Master.",
                        "correction": "Manual pasting causes subtle alignment shifts from slide to slide, making the logo 'jump' distractingly during transitions. Furthermore, if the logo needs updating or resizing, you must manually edit 30 slides instead of making a single 5-second adjustment on the Slide Master."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Illegible Micro-Fonts & Low Contrast",
                    "content": {
                        "mistake": "Using decorative script fonts in 14pt size with light blue text on a white background.",
                        "why_it_happens": "Presenters design slides on high-resolution laptop screens sitting 40cm away, forgetting that the audience is seated 10 meters away from a projector.",
                        "fix_solution": "Always use clean sans-serif fonts (Arial, Calibri, Trebuchet MS), maintain a minimum 20pt size for body text, and ensure high contrast between text and background."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Slide Master Efficiency",
                    "content": {
                        "question": "What is the primary technical benefit of adding an institutional logo to the Slide Master rather than pasting it on individual slides?",
                        "options": [
                            "It permanently locks the presentation file with password encryption",
                            "It guarantees pixel-perfect position consistency and allows one-click global updates across all slides",
                            "It converts bitmap images into vector SVGs automatically",
                            "It allows the presentation to run without consuming any CPU power"
                        ],
                        "correct": "B",
                        "explanation": "Placing branding on the Slide Master ensures identical alignment across every slide and enables immediate global edits without having to modify individual pages."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: The 6x6 Design Standard",
                    "content": {
                        "question": "Which of the following slide designs adheres correctly to the 6x6 rule and professional typography standards?",
                        "options": [
                            "A single slide containing 12 bullet points with 15 words each in 12pt font",
                            "A slide containing 4 concise bullet points of 5 words each in 24pt high-contrast text",
                            "A full 100-word paragraph styled in yellow text on a white background",
                            "A slide featuring animated flashing text in decorative script font at 10pt size"
                        ],
                        "correct": "B",
                        "explanation": "The 6x6 rule limits text to a maximum of 6 bullets per slide and 6 words per bullet, rendered in a large, readable font (20-24pt) with high visual contrast."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Mastering Slide Layouts and Slide Master View in Presentation Software",
                    "content": {
                        "title": "Slide Master View, Typography, and Layout Architecture",
                        "youtube_id": "8pEcz4T8750",
                        "url": "https://www.youtube.com/watch?v=8pEcz4T8750",
                        "description": "Practical tutorial demonstrating how to customize Slide Masters, configure theme layouts, enforce font hierarchies, and apply the 6x6 design standard."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Slide Master Power:** Define fonts, color schemes, and branding once on the Slide Master to cascade formatting across all child slides.\n2. **The 6x6 Standard:** Limit slides to 6 bullet points of 6 words each to eliminate cognitive fatigue and maintain audience engagement.\n3. **Typography Sizing:** Use 36-44pt for titles and 20-24pt for bullet points; text smaller than 18pt cannot be read in auditorium settings.\n4. **High Contrast:** Ensure sharp contrast between background and text colors to guarantee readability under varying projector lighting conditions."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5.1.4: Enhancing Slides with Multimedia and Animation
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Enhancing Slides with Multimedia and Animation",
        "unit_description": "Slide transitions, object animations (entrance, emphasis, exit), aspect ratio image scaling (Shift-drag), action buttons, and hyperlinked non-linear interactive menus.",
        "lesson_title": "Enhancing Slides with Multimedia and Animation",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Multimedia and Interactivity in Modern Presentations",
                    "content": {
                        "title": "Interactive Digital Visual Media and Motion",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Mechanical_typewriter_Adler_Junior_E.jpg",
                        "caption": "Modern interactive digital media contrasts with rigid static communication, enabling dynamic animations, audio/video embedding, and non-linear hyperlinked navigation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Bringing Presentations to Life with Motion & Interactivity",
                    "content": {
                        "text": "A presentation without visual variety or controlled pacing can feel like a dry textbook. To truly capture and hold an audience's attention, you can introduce subtle motion and interactive pathways!\n\nBy incorporating relevant images, applying clean **slide transitions**, pacing bullet points with **entrance animations**, and creating clickable **hyperlink action buttons**, you transform linear lectures into dynamic, interactive experiences. However, motion must be used purposefully: subtle animation directs attention, whereas excessive effects create chaotic distraction."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between slide transitions (page-to-page) and object animations (element-level)\n- Apply entrance animations to control the pace of information delivery on bulleted slides\n- Resize and crop graphics properly while locking the aspect ratio (holding Shift key)\n- Construct non-linear, interactive presentations using shapes, hyperlinks, and action buttons"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Transitions, Animations & Hyperlinks",
                    "content": {
                        "term": "Slide Transitions vs. Object Animations vs. Hyperlinks",
                        "definition": "Dynamic multimedia mechanisms used to control slide movement, animate individual canvas elements, and create interactive navigation links.",
                        "simple": "A transition happens between slides; an animation happens to elements on a slide; a hyperlink jumps to another slide when clicked.",
                        "technical": "Transitions are full-frame rendering effects triggered during slide index shifts; Animations are timeline keyframe effects applied to element DOM nodes; Hyperlinks are event-driven URI/index anchors.",
                        "example": "Using a 0.5s Fade transition between slides, animating bullet points to appear on click, and adding a 'Home' button linking back to Slide 2."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Golden Rules of Motion & Media",
                    "content": {
                        "text": "Apply these professional media standards to maintain elegance and clarity:\n\n1. **Subtle Transitions (0.5s – 1.0s):**\n   - Use clean, understated transitions such as **Fade** or **Push (from right)**.\n   - Avoid distracting, theatrical effects like 'Curtains', 'Origami', or 'Vortex' in academic and business settings.\n   - Keep durations under 1 second so the audience never has to wait for content to appear.\n2. **Pacing with Entrance Animations:**\n   - Animate bullet points with **Fade In** or **Wipe** set to 'Start On Click'.\n   - Revealing bullet points one by one prevents the audience from reading ahead while you are still explaining the first concept.\n3. **Locking Aspect Ratio When Resizing Graphics:**\n   - Always drag **corner handles** while holding the **Shift key** (or ensuring 'Lock Aspect Ratio' is enabled).\n   - Never drag top, bottom, or side middle handles, which squishes or stretches photos unnaturally.\n4. **Non-Linear Navigation with Hyperlinks (Ctrl + K):**\n   - Standard presentations run linearly (Slide 1 ➔ 2 ➔ 3).\n   - By inserting **Action Buttons** linked to specific slide indices, you can build interactive kiosks, multi-topic dashboards, and interactive quiz games."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Multimedia Sequences & Hyperlink Architecture",
                    "content": {
                        "title": "Animation Sequence Timeline and Non-Linear Hyperlink Network",
                        "caption": "Vector visual demonstrating paced animation triggers in the Animation Pane alongside an interactive main menu branching diagram with return action buttons.",
                        "svg_content": SVG_MULTIMEDIA_ANIMATION_FLOW
                    }
                },
                {
                    "type": "step_process",
                    "title": "Building an Interactive Non-Linear Menu Deck",
                    "content": {
                        "intro": "Follow these steps to create an interactive multi-topic presentation with clickable action buttons:",
                        "steps": [
                            {"title": "1. Set Up Slides", "description": "Create Slide 1 (Title), Slide 2 (Main Menu Hub), Slide 3 (Topic A: Solar Energy), and Slide 4 (Topic B: Wind Power)."},
                            {"title": "2. Insert Interactive Menu Shapes", "description": "On Slide 2, insert two rounded rectangle shapes. Add text: 'Explore Solar Energy' on Button 1 and 'Explore Wind Power' on Button 2."},
                            {"title": "3. Link Buttons to Specific Slides", "description": "Right-click Button 1, select Link (or press Ctrl + K), choose 'Place in This Document', and select Slide 3. Link Button 2 to Slide 4."},
                            {"title": "4. Insert Return Action Buttons", "description": "On Slide 3 and Slide 4, insert a small arrow shape in the bottom corner and hyperlink it back to Slide 2 (Main Menu Hub)."},
                            {"title": "5. Test Full-Screen Slideshow", "description": "Press F5 to run the slideshow. Advance to Slide 2 and click the buttons to verify seamless non-linear jumping and returning."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Interactive Science Museum Kiosk in Kisumu",
                    "content": {
                        "title": "Self-Guided Interactive Presentation on Lake Victoria Ecology",
                        "scenario": "High school students in Kisumu designed a touchscreen kiosk presentation for visitors at an environmental science exhibition.",
                        "impact": "A linear slideshow would require visitors to sit and watch 40 slides in fixed order, causing people to walk away.",
                        "solution": "They built a hub-and-spoke interactive menu with touchable action buttons linked to specific fish species, pollution data, and conservation tips, complete with 'Back to Menu' buttons on every slide."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The Flashy Animation Fallacy",
                    "content": {
                        "misconception": "Adding loud sound effects, spinning 3D transitions, and bouncing text makes a presentation look advanced and impressive.",
                        "correction": "Excessive animations and sound effects scream 'beginner,' distract the audience from your message, break the presenter's rhythm, and appear deeply unprofessional in academic and business settings. Motion should be subtle, fast, and functional."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Distorted Photos & Broken Aspect Ratios",
                    "content": {
                        "mistake": "Dragging the side handle of a portrait photo to make it fit a wide horizontal box, resulting in a squished, distorted image.",
                        "why_it_happens": "Users try to force an image into an arbitrary placeholder box without cropping.",
                        "fix_solution": "Always drag corner handles while holding Shift to maintain original proportions. Use the software's 'Crop ➔ Fill' tool to trim excess image areas cleanly."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Slide Transition Standards",
                    "content": {
                        "question": "A presenter uses a 5-second 3D spinning transition with a loud chime sound effect between every slide. Why is this considered poor presentation practice?",
                        "options": [
                            "Projectors automatically mute any slide audio exceeding 3 seconds",
                            "Slow, noisy transitions distract the audience, interrupt speaking flow, and look unprofessional",
                            "Operating systems automatically skip slides with animations longer than 2 seconds",
                            "Spinning animations corrupt the presentation file format permanently"
                        ],
                        "correct": "B",
                        "explanation": "Slide transitions should be subtle, silent, and brief (0.5s - 1.0s). Dramatic effects and noisy sound effects distract the audience and disrupt the presenter's narrative flow."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Aspect Ratio Preservation",
                    "content": {
                        "question": "What keyboard modifier key should you hold while dragging the corner handle of an image to resize it without distorting its proportions?",
                        "options": [
                            "Tab key",
                            "Shift key",
                            "Alt key",
                            "Caps Lock key"
                        ],
                        "correct": "B",
                        "explanation": "Holding the Shift key while dragging corner sizing handles locks the image's aspect ratio, preventing vertical or horizontal stretching and squishing."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Transitions, Animations, and Interactive Hyperlinks in Presentation Software",
                    "content": {
                        "title": "Animation Sequencing, Motion Timing, and Hyperlinked Menus",
                        "youtube_id": "d71qPzG6nU0",
                        "url": "https://www.youtube.com/watch?v=d71qPzG6nU0",
                        "description": "Step-by-step masterclass covering entrance animations, subtle slide transitions, image cropping, and building interactive hyperlink menus."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Transitions vs. Animations:** Transitions apply to full slide page changes; object animations apply to individual text, shapes, or images on a slide.\n2. **Information Pacing:** Use subtle 0.5s entrance animations on bullet points to reveal ideas in step with your vocal delivery.\n3. **Aspect Ratio Discipline:** Always hold the Shift key when dragging corner handles to preserve image proportions without distortion.\n4. **Interactive Hyperlinks:** Leverage action buttons and hyperlinks (Ctrl + K) to create non-linear navigation menus, dashboards, and self-paced kiosks."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5.1.5: Running and Delivering a Presentation
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Running and Delivering a Presentation",
        "unit_description": "Mastering Presenter View (Extend vs Duplicate), 3-part bullet Speaker Notes, rehearsal timers, digital annotation ink, accessible presentation standards (WCAG/captions), and AI presentation trends.",
        "lesson_title": "Running and Delivering a Presentation",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Delivering Presentations with Authority & Presenter View",
                    "content": {
                        "title": "Dual-Display Presenter Command and Delivery",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/KICC_Nairobi.jpg",
                        "caption": "A major conference auditorium in Nairobi where presenters utilize dual-monitor Presenter View to track notes, timing, and upcoming slides while projecting clean visual decks to the audience.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Delivering with Authority, Polish & Confidence",
                    "content": {
                        "text": "Your slides are structured, the colors are balanced, and the animations are timed. Now comes the most vital component of any presentation: **You, the presenter!**\n\nEven the most beautifully designed slide deck will fall flat if the speaker turns their back to the audience, reads text aloud like a robot, or loses track of time. Fortunately, modern presentation software includes built-in copilot tools specifically engineered to build confidence: **Presenter View**, **Speaker Notes**, **Rehearsal Timers**, and **Digital Ink Tools**. Mastering these features empowers you to present with poise, authority, and engagement."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Configure dual-monitor display settings (Extend vs. Duplicate) to activate Presenter View\n- Utilize the 3-part bullet structure (Fact, Bridge, Cue) to write effective Speaker Notes\n- Operate Presenter View controls: live stopwatch timer, next slide preview, digital pen/laser, and slide zoom\n- Apply digital accessibility standards (Alt-Text, high contrast, live captions) and explore modern AI presentation tools"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Presenter View & Speaker Notes",
                    "content": {
                        "term": "Presenter View & Speaker Notes",
                        "definition": "A dual-monitor display architecture where the audience sees only the full-screen slide deck on the projector, while the presenter sees a secret control dashboard on their laptop.",
                        "simple": "A private laptop screen showing your current slide, next slide, secret reminder notes, and a running timer while the audience sees only the slides.",
                        "technical": "A multi-pane dual-display configuration operating over extended desktop video outputs (HDMI/DisplayPort), rendering presentation telemetry, thumbnail streams, and notes to the primary console.",
                        "example": "Using PowerPoint Presenter View during a competition defense to keep your speech strictly within the 10-minute limit."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Delivery Command: Display Modes, Notes & Accessibility",
                    "content": {
                        "text": "To deliver like a seasoned professional, master these three operational pillars:\n\n1. **Display Configuration (Windows Key + P ➔ Extend):**\n   - **Extend Mode:** Treats the projector as a separate secondary monitor. This is **mandatory** for Presenter View. Your laptop shows your private dashboard; the projector shows full-screen slides.\n   - **Duplicate Mode:** Clones your laptop screen onto the projector. If used, the audience will see your private notes, mouse movements, and desktop icons!\n2. **The 3-Part Bullet Rule for Speaker Notes:**\n   - Never write a full script in your notes, or you will end up reading down at your screen.\n   - Structure each slide note with three quick anchors:\n     - **Fact Anchor:** Specific statistics or names hard to memorize (e.g. `Budget: KSh 4.2 million`).\n     - **Transition Bridge:** A phrase connecting to the next slide (e.g. `Having reviewed costs, let us explore timeline...`).\n     - **Engagement Cue:** A prompt to interact with the room (e.g. `[PAUSE - Ask for a show of hands]`).\n3. **Digital Accessibility & Emerging AI Trends:**\n   - **Accessibility (WCAG):** Add Alt-Text to images so screen readers can describe charts to visually impaired students, and enable real-time **Automated Subtitles / Closed Captions**.\n   - **AI Presentation Tools:** Generative AI tools (Copilot, Gamma) help draft outlines and layouts, while AI presentation coaches analyze pacing and filler words ('um', 'ah') during rehearsal."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Presenter View Architecture & Delivery Controls",
                    "content": {
                        "title": "Dual-Monitor Presenter View and Live Projector Setup",
                        "caption": "Vector visual illustrating the dual-display architecture comparing the presenter's private laptop dashboard (notes, timer, next slide preview) with the audience's clean full-screen view.",
                        "svg_content": SVG_PRESENTATION_DELIVERY_MODES
                    }
                },
                {
                    "type": "step_process",
                    "title": "Setting Up and Rehearsing with Presenter View",
                    "content": {
                        "intro": "Follow this procedure to configure Presenter View and rehearse before going on stage:",
                        "steps": [
                            {"title": "1. Write 3-Part Speaker Notes", "description": "Open your completed slide deck. Click the 'Notes' pane below Slide 2 and add Fact, Bridge, and Engagement cue bullets."},
                            {"title": "2. Connect & Set Display to Extend", "description": "Connect your laptop to the projector. Press Windows Key + P and select 'Extend' (or adjust display settings on Mac)."},
                            {"title": "3. Launch Presenter View", "description": "Press Alt + F5 in PowerPoint (or click Slide Show ➔ Use Presenter View). Verify your notes appear on your laptop while the projector displays only the slide."},
                            {"title": "4. Rehearse with the Live Timer", "description": "Click 'Start Timer' and rehearse speaking your points aloud. Check the 'Next Slide' preview to make smooth verbal transitions."},
                            {"title": "5. Practice Live Annotations", "description": "Click the Pen / Laser Pointer tool below the slide preview to highlight a key chart line, and press 'B' on your keyboard to black out the screen when focusing attention on yourself."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Senior School Innovation Defense in Nairobi",
                    "content": {
                        "title": "Managing High-Stakes Q&A with Slide Navigator in Presenter View",
                        "scenario": "A student team presented their mobile water-testing app at a national science congress with strict 8-minute speaking limits.",
                        "impact": "During Q&A, a judge asked about a chemical formula on Slide 3. An amateur presenter would rapidly click backward through 15 slides, looking disorganized.",
                        "solution": "The team used Presenter View's 'Slide Grid Navigator' to jump directly to Slide 3 in one click, answered the query with specific data from their speaker notes, and won first place."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The Duplicate Mode Blunder",
                    "content": {
                        "misconception": "Setting display mode to 'Duplicate' is safer because both screens show the exact same thing.",
                        "correction": "Duplicate mode exposes your private speaker notes, upcoming slides, and desktop notifications to the entire auditorium. It prevents you from using Presenter View. Always use 'Extend' mode to keep your notes confidential."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Reading Word-for-Word from Notes",
                    "content": {
                        "mistake": "Typing an essay into the speaker notes pane and reading it aloud with head down.",
                        "why_it_happens": "Speakers get anxious and want an exact script to read.",
                        "fix_solution": "Use large font bullets in the notes pane with 3-word trigger phrases. Keep your chin up, maintain eye contact with the room, and use the notes only as quick glance anchors."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Extend vs. Duplicate Display Modes",
                    "content": {
                        "question": "Why is 'Extend' display mode required when using Presenter View with an external projector?",
                        "options": [
                            "It extends the projector lamp lifespan by decreasing brightness",
                            "It treats the projector as an independent second monitor, keeping secret notes on the laptop while projecting slides to the audience",
                            "It automatically speeds up the presentation to finish in half the time",
                            "It converts 2D presentation slides into 3D holographic projections"
                        ],
                        "correct": "B",
                        "explanation": "'Extend' mode configures the external projector as an independent secondary screen, allowing the presenter to view private timers and notes on their laptop while the audience views full-screen slides."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Digital Presentation Accessibility",
                    "content": {
                        "question": "Which of the following practices directly supports digital accessibility for audience members with hearing or visual impairments during a presentation?",
                        "options": [
                            "Using flashing neon background colors on every slide",
                            "Enabling real-time closed captions and adding descriptive Alt-Text to diagrams",
                            "Removing all text and using only abstract background sounds",
                            "Setting the slide transition duration to 10 seconds"
                        ],
                        "correct": "B",
                        "explanation": "Enabling real-time closed captions assists participants with hearing challenges, while adding Alt-Text to images enables screen readers to describe visual diagrams to visually impaired learners."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Mastering Presenter View, Speaker Notes, and Confident Presentation Delivery",
                    "content": {
                        "title": "Presenter View Setup, Timing, and Public Speaking Delivery",
                        "youtube_id": "qU3fQv4R90A",
                        "url": "https://www.youtube.com/watch?v=qU3fQv4R90A",
                        "description": "Comprehensive guide on configuring dual monitors, utilizing Presenter View, organizing speaker notes, and presenting with confidence."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Extend Mode Mastery:** Press Windows + P and select 'Extend' to enable Presenter View without revealing notes to the audience.\n2. **3-Part Speaker Notes:** Structure notes using Fact Anchors, Transition Bridges, and Engagement Cues rather than full essays.\n3. **Live Rehearsal:** Use the built-in stopwatch timer to pace your delivery and practice with digital pen annotations and slide grid zoom.\n4. **Accessibility & AI:** Enable live subtitles and Alt-Text for inclusive learning, and leverage modern AI tools to streamline slide authoring."
                    }
                }
            ]
        ]
    }
]
