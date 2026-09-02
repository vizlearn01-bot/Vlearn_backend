"""
VLearn CBC Grade 10 ICT — Topic 4: Word Processing
Full Structured Lesson Card Definitions (Lessons 4.1.1 to 4.1.10)
"""

import re

def sanitize_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# HIGH PRECISION VECTOR SVGS FOR TOPIC 4: WORD PROCESSING
# =====================================================================

SVG_WORD_PROCESSING_CYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Word Processing Lifecycle &amp; Digital Workflow</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How digital word processing transforms manual typing into a flexible, dynamic production pipeline</text>

  <!-- Step 1: Input & Data Entry -->
  <g transform="translate(45, 95)">
    <rect width="195" height="240" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="195" height="32" rx="8" fill="#0284c7"/>
    <text x="97" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. INPUT &amp; ENTRY</text>
    
    <circle cx="97" cy="75" r="24" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="97" y="81" font-size="18" text-anchor="middle">⌨️</text>
    
    <text x="15" y="125" font-size="11" font-weight="bold" fill="#38bdf8">• Text Capture:</text>
    <text x="15" y="142" font-size="9.5" fill="#cbd5e1">Keyboard typing, voice-to-text dictation, OCR scanning.</text>
    
    <text x="15" y="175" font-size="11" font-weight="bold" fill="#38bdf8">• Word Wrap:</text>
    <text x="15" y="192" font-size="9.5" fill="#cbd5e1">Automatic line breaking at right margin without manual Enter.</text>
    
    <rect x="15" y="212" width="165" height="18" rx="4" fill="#1e293b"/>
    <text x="97" y="224" font-size="9" fill="#94a3b8" text-anchor="middle">Non-destructive input</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 245 215 L 275 215" stroke="#38bdf8" stroke-width="3" fill="none"/>

  <!-- Step 2: Dynamic Processing & Formatting -->
  <g transform="translate(280, 95)">
    <rect width="195" height="240" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="195" height="32" rx="8" fill="#059669"/>
    <text x="97" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. EDIT &amp; FORMAT</text>
    
    <circle cx="97" cy="75" r="24" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="97" y="81" font-size="18" text-anchor="middle">🎨</text>
    
    <text x="15" y="125" font-size="11" font-weight="bold" fill="#34d399">• Styling &amp; Typography:</text>
    <text x="15" y="142" font-size="9.5" fill="#cbd5e1">Fonts, sizing, bold, color, line spacing, margins, styles.</text>
    
    <text x="15" y="175" font-size="11" font-weight="bold" fill="#34d399">• Automated Editing:</text>
    <text x="15" y="192" font-size="9.5" fill="#cbd5e1">Spell checker, grammar engine, thesaurus, Find &amp; Replace.</text>
    
    <rect x="15" y="212" width="165" height="18" rx="4" fill="#1e293b"/>
    <text x="97" y="224" font-size="9" fill="#94a3b8" text-anchor="middle">Real-time digital buffer</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 480 215 L 510 215" stroke="#34d399" stroke-width="3" fill="none"/>

  <!-- Step 3: Storage & Retrieval -->
  <g transform="translate(515, 95)">
    <rect width="195" height="240" rx="12" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="195" height="32" rx="8" fill="#d97706"/>
    <text x="97" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SAVE &amp; STORE</text>
    
    <circle cx="97" cy="75" r="24" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="97" y="81" font-size="18" text-anchor="middle">💾</text>
    
    <text x="15" y="125" font-size="11" font-weight="bold" fill="#fbbf24">• File Formats:</text>
    <text x="15" y="142" font-size="9.5" fill="#cbd5e1">Standard .docx, OpenDocument .odt, Plain text .txt.</text>
    
    <text x="15" y="175" font-size="11" font-weight="bold" fill="#fbbf24">• Persistence &amp; Cloud:</text>
    <text x="15" y="192" font-size="9.5" fill="#cbd5e1">Local SSD/HDD, Google Drive, OneDrive with version history.</text>
    
    <rect x="15" y="212" width="165" height="18" rx="4" fill="#1e293b"/>
    <text x="97" y="224" font-size="9" fill="#94a3b8" text-anchor="middle">Instant retrieval anytime</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 715 215 L 745 215" stroke="#fbbf24" stroke-width="3" fill="none"/>

  <!-- Step 4: Output & Distribution -->
  <g transform="translate(750, 95)">
    <rect width="165" height="240" rx="12" fill="#0f172a" stroke="#f472b6" stroke-width="1.5"/>
    <rect width="165" height="32" rx="8" fill="#db2777"/>
    <text x="82" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. OUTPUT &amp; SHARE</text>
    
    <circle cx="82" cy="75" r="24" fill="#1e293b" stroke="#f472b6" stroke-width="1.5"/>
    <text x="82" y="81" font-size="18" text-anchor="middle">🖨️</text>
    
    <text x="12" y="125" font-size="11" font-weight="bold" fill="#f472b6">• Print &amp; PDF:</text>
    <text x="12" y="142" font-size="9.5" fill="#cbd5e1">Physical hardcopy or fixed-layout PDF export.</text>
    
    <text x="12" y="175" font-size="11" font-weight="bold" fill="#f472b6">• Digital Sharing:</text>
    <text x="12" y="192" font-size="9.5" fill="#cbd5e1">Email, cloud link, web publication.</text>
    
    <rect x="12" y="212" width="141" height="18" rx="4" fill="#1e293b"/>
    <text x="82" y="224" font-size="9" fill="#94a3b8" text-anchor="middle">Zero quality loss</text>
  </g>

  <!-- Bottom Comparison Banner -->
  <g transform="translate(45, 355)">
    <rect width="870" height="130" rx="12" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="25" y="28" font-size="13" font-weight="bold" fill="#38bdf8">Mechanical Typewriter vs. Digital Word Processor</text>
    
    <line x1="25" y1="38" x2="845" y2="38" stroke="#334155" stroke-width="1"/>
    
    <text x="25" y="60" font-size="11" font-weight="bold" fill="#ef4444">❌ Mechanical Typewriter:</text>
    <text x="25" y="78" font-size="10" fill="#cbd5e1">• Fixed keystrokes directly onto paper • Spelling mistakes require full page re-typing • Single fixed font &amp; size • No digital saving</text>
    
    <text x="25" y="102" font-size="11" font-weight="bold" fill="#34d399">✅ Digital Word Processor:</text>
    <text x="25" y="120" font-size="10" fill="#cbd5e1">• Text stored dynamically in RAM buffer • Backspace/Delete corrections instantly • Unlimited typography, styling, tables, &amp; graphics</text>
  </g>
</svg>
""")

SVG_WORD_PLATFORMS_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Word Processing Applications Comparison Matrix</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Evaluating proprietary, open-source, cloud-native, and freemium productivity software</text>

  <!-- Platform 1: MS Word -->
  <g transform="translate(45, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#0284c7"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Microsoft Word</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Proprietary / Commercial</text>
    
    <text x="15" y="95" font-size="11" font-weight="bold" fill="#38bdf8">• Cost &amp; License:</text>
    <text x="15" y="112" font-size="9.5" fill="#cbd5e1">Paid license / M365 subscription.</text>
    
    <text x="15" y="145" font-size="11" font-weight="bold" fill="#38bdf8">• Connectivity:</text>
    <text x="15" y="162" font-size="9.5" fill="#cbd5e1">Full offline desktop suite + cloud sync.</text>
    
    <text x="15" y="195" font-size="11" font-weight="bold" fill="#38bdf8">• Strengths:</text>
    <text x="15" y="212" font-size="9.5" fill="#cbd5e1">Industry standard, advanced macros, mail merge, complex page layout.</text>
    
    <text x="15" y="260" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="277" font-size="9.5" fill="#cbd5e1">High licensing cost for school labs.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Corporate offices &amp; formal reports</text>
  </g>

  <!-- Platform 2: Google Docs -->
  <g transform="translate(265, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#059669"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Google Docs</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Cloud-Native Web App</text>
    
    <text x="15" y="95" font-size="11" font-weight="bold" fill="#34d399">• Cost &amp; License:</text>
    <text x="15" y="112" font-size="9.5" fill="#cbd5e1">100% Free with Google Account.</text>
    
    <text x="15" y="145" font-size="11" font-weight="bold" fill="#34d399">• Connectivity:</text>
    <text x="15" y="162" font-size="9.5" fill="#cbd5e1">Requires active browser / internet.</text>
    
    <text x="15" y="195" font-size="11" font-weight="bold" fill="#34d399">• Strengths:</text>
    <text x="15" y="212" font-size="9.5" fill="#cbd5e1">Real-time multi-user co-authoring, automatic cloud saving, zero install.</text>
    
    <text x="15" y="260" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="277" font-size="9.5" fill="#cbd5e1">Limited advanced desktop layout tools.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Group assignments &amp; team editing</text>
  </g>

  <!-- Platform 3: LibreOffice Writer -->
  <g transform="translate(485, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#d97706"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LibreOffice Writer</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Free &amp; Open-Source (FOSS)</text>
    
    <text x="15" y="95" font-size="11" font-weight="bold" fill="#fbbf24">• Cost &amp; License:</text>
    <text x="15" y="112" font-size="9.5" fill="#cbd5e1">100% Free (GPLv3), no ads or fees.</text>
    
    <text x="15" y="145" font-size="11" font-weight="bold" fill="#fbbf24">• Connectivity:</text>
    <text x="15" y="162" font-size="9.5" fill="#cbd5e1">Completely offline standalone app.</text>
    
    <text x="15" y="195" font-size="11" font-weight="bold" fill="#fbbf24">• Strengths:</text>
    <text x="15" y="212" font-size="9.5" fill="#cbd5e1">Full formatting suite, native .odt format, runs on Linux/Windows/macOS.</text>
    
    <text x="15" y="260" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="277" font-size="9.5" fill="#cbd5e1">Lacks built-in real-time co-authoring.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Budget school labs &amp; offline PCs</text>
  </g>

  <!-- Platform 4: WPS Office Writer -->
  <g transform="translate(705, 90)">
    <rect width="205" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#9333ea"/>
    <text x="102" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">WPS Office Writer</text>
    
    <rect x="15" y="48" width="175" height="22" rx="4" fill="#1e293b"/>
    <text x="102" y="63" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">Freemium / Cross-Platform</text>
    
    <text x="15" y="95" font-size="11" font-weight="bold" fill="#c084fc">• Cost &amp; License:</text>
    <text x="15" y="112" font-size="9.5" fill="#cbd5e1">Free tier (with ads) + VIP upgrade.</text>
    
    <text x="15" y="145" font-size="11" font-weight="bold" fill="#c084fc">• Connectivity:</text>
    <text x="15" y="162" font-size="9.5" fill="#cbd5e1">Offline app with cloud sync option.</text>
    
    <text x="15" y="195" font-size="11" font-weight="bold" fill="#c084fc">• Strengths:</text>
    <text x="15" y="212" font-size="9.5" fill="#cbd5e1">Tabbed multi-document bar, lightweight, great Android/iOS mobile app.</text>
    
    <text x="15" y="260" font-size="11" font-weight="bold" fill="#f87171">• Limitations:</text>
    <text x="15" y="277" font-size="9.5" fill="#cbd5e1">In-app ads and locked premium features.</text>
    
    <rect x="15" y="325" width="175" height="48" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
    <text x="102" y="343" font-size="9" font-weight="bold" fill="#c084fc" text-anchor="middle">Best Use Case:</text>
    <text x="102" y="359" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Mobile devices &amp; low-spec laptops</text>
  </g>
</svg>
""")

SVG_TYPING_NAVIGATION_WORKFLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Word Processor Window Anatomy &amp; Core Typing Mechanics</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Key interface components, automatic word wrap mechanics, and essential keyboard shortcuts</text>

  <!-- Main Window Frame Simulation -->
  <g transform="translate(45, 90)">
    <rect width="520" height="380" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    
    <!-- Title Bar -->
    <rect width="520" height="28" rx="8" fill="#1e293b"/>
    <circle cx="18" cy="14" r="5" fill="#ef4444"/>
    <circle cx="34" cy="14" r="5" fill="#f59e0b"/>
    <circle cx="50" cy="14" r="5" fill="#10b981"/>
    <text x="260" y="19" font-size="11" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Joyce_Intro_Paragraph.docx - Word</text>
    
    <!-- Ribbon Menu Bar -->
    <rect y="28" width="520" height="32" fill="#0284c7"/>
    <text x="20" y="49" font-size="10.5" font-weight="bold" fill="#ffffff">File</text>
    <text x="55" y="49" font-size="10.5" font-weight="bold" fill="#ffffff">Home</text>
    <text x="100" y="49" font-size="10.5" fill="#bae6fd">Insert</text>
    <text x="145" y="49" font-size="10.5" fill="#bae6fd">Layout</text>
    <text x="195" y="49" font-size="10.5" fill="#bae6fd">References</text>
    <text x="270" y="49" font-size="10.5" fill="#bae6fd">Review</text>
    <text x="325" y="49" font-size="10.5" fill="#bae6fd">View</text>
    
    <!-- Ribbon Tool Palette -->
    <rect y="60" width="520" height="42" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <rect x="15" y="66" width="140" height="30" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="25" y="85" font-size="11" fill="#38bdf8">Arial</text>
    <text x="90" y="85" font-size="11" fill="#38bdf8">12</text>
    <text x="120" y="85" font-size="11" font-weight="bold" fill="#ffffff">B</text>
    <text x="135" y="85" font-size="11" font-style="italic" fill="#ffffff">I</text>
    
    <rect x="165" y="66" width="130" height="30" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="175" y="85" font-size="11" fill="#ffffff">Left</text>
    <text x="205" y="85" font-size="11" fill="#34d399">Center</text>
    <text x="250" y="85" font-size="11" fill="#ffffff">Justify</text>

    <!-- Document Canvas Area -->
    <rect x="25" y="115" width="470" height="225" rx="6" fill="#ffffff"/>
    <text x="45" y="145" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle" transform="translate(190,0)">ICT MODULE NOTES</text>
    <text x="45" y="175" font-size="10.5" fill="#334155">Hello, my name is Joyce. I am a Grade 10 student at Greenhill</text>
    <text x="45" y="195" font-size="10.5" fill="#334155">Academy. I am learning how to use word processing tools to</text>
    <text x="45" y="215" font-size="10.5" fill="#334155">design clean and professional documents for my school portfolio.|</text>
    <line x1="392" y1="203" x2="392" y2="217" stroke="#0284c7" stroke-width="2"/>
    
    <!-- Status Bar -->
    <rect y="352" width="520" height="28" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="20" y="370" font-size="9.5" fill="#94a3b8">Page 1 of 1  •  32 words  •  English (Kenya)</text>
    <text x="440" y="370" font-size="9.5" fill="#94a3b8">🔍 100% [—+—]</text>
  </g>

  <!-- Right Info Panel: Core Mechanics & Shortcuts -->
  <g transform="translate(585, 90)">
    <!-- Word Wrap Mechanics Box -->
    <rect width="330" height="180" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="330" height="30" rx="8" fill="#059669"/>
    <text x="165" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Automatic Word Wrap Rule</text>
    
    <text x="15" y="52" font-size="11" font-weight="bold" fill="#34d399">How it Works:</text>
    <text x="15" y="70" font-size="9.5" fill="#cbd5e1">The software measures line length against margins. When a word overflows, it automatically shifts to the next line.</text>
    
    <text x="15" y="110" font-size="11" font-weight="bold" fill="#fbbf24">Golden Typing Rule:</text>
    <text x="15" y="128" font-size="9.5" fill="#cbd5e1">• DO NOT press Enter at the end of a line.</text>
    <text x="15" y="146" font-size="9.5" fill="#cbd5e1">• Press [Enter] ONLY to start a NEW paragraph.</text>
    <text x="15" y="164" font-size="9.5" fill="#cbd5e1">• Use [Shift + Enter] for a manual soft line break.</text>
  </g>

  <!-- Shortcuts Panel -->
  <g transform="translate(585, 290)">
    <rect width="330" height="180" rx="12" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="330" height="30" rx="8" fill="#d97706"/>
    <text x="165" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Essential Efficiency Shortcuts</text>
    
    <text x="20" y="55" font-size="10.5" font-weight="bold" fill="#38bdf8">Ctrl + N</text>
    <text x="110" y="55" font-size="10" fill="#cbd5e1">Create a New Blank Document</text>
    
    <text x="20" y="82" font-size="10.5" font-weight="bold" fill="#38bdf8">Ctrl + S</text>
    <text x="110" y="82" font-size="10" fill="#cbd5e1">Save Document (Press every 5 min!)</text>
    
    <text x="20" y="109" font-size="10.5" font-weight="bold" fill="#38bdf8">Ctrl + O</text>
    <text x="110" y="109" font-size="10" fill="#cbd5e1">Open / Retrieve an Existing File</text>
    
    <text x="20" y="136" font-size="10.5" font-weight="bold" fill="#38bdf8">Ctrl + P</text>
    <text x="110" y="136" font-size="10" fill="#cbd5e1">Print Document Hardcopy / PDF</text>
    
    <text x="20" y="163" font-size="10.5" font-weight="bold" fill="#38bdf8">Ctrl + Z / Y</text>
    <text x="110" y="163" font-size="10" fill="#cbd5e1">Undo / Redo Last Action</text>
  </g>
</svg>
""")

SVG_FORMATTING_HIERARCHY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Typographic &amp; Document Formatting Hierarchy</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Mastering the two structural levels of formatting: Character-Level vs. Paragraph-Level</text>

  <!-- Left Branch: Character Formatting -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#0284c7"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LEVEL 1: CHARACTER FORMATTING</text>
    
    <text x="20" y="62" font-size="10" fill="#94a3b8">Applies to selected letters, words, or individual characters</text>
    
    <!-- 1. Typeface -->
    <rect x="20" y="78" width="380" height="65" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="35" y="100" font-size="11.5" font-weight="bold" fill="#38bdf8">Font Family (Typeface):</text>
    <text x="35" y="118" font-size="10" fill="#cbd5e1">• <tspan font-family="serif">Serif (Times New Roman):</tspan> Formal print, books, thesis</text>
    <text x="35" y="134" font-size="10" fill="#cbd5e1">• <tspan font-family="sans-serif">Sans-Serif (Arial, Calibri):</tspan> Modern, clean screen readability</text>
    
    <!-- 2. Font Sizing & Weight -->
    <rect x="20" y="153" width="380" height="65" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="35" y="175" font-size="11.5" font-weight="bold" fill="#38bdf8">Size &amp; Styling Variations:</text>
    <text x="35" y="193" font-size="10" fill="#cbd5e1">• Title: 16-20pt | Headings: 14-16pt | Body: 11-12pt</text>
    <text x="35" y="209" font-size="10" fill="#cbd5e1">• <tspan font-weight="bold">Bold (B)</tspan> for emphasis, <tspan font-style="italic">Italics (I)</tspan> for terms, <tspan text-decoration="underline">Underline (U)</tspan></text>
    
    <!-- 3. Special Effects -->
    <rect x="20" y="228" width="380" height="65" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="35" y="250" font-size="11.5" font-weight="bold" fill="#38bdf8">Color, Highlight &amp; Scripts:</text>
    <text x="35" y="268" font-size="10" fill="#cbd5e1">• Subscript: H<tspan font-size="8">2</tspan>O  |  Superscript: x<tspan font-size="8">2</tspan> + y<tspan font-size="8">2</tspan></text>
    <text x="35" y="284" font-size="10" fill="#cbd5e1">• Font Color &amp; Text Highlight background</text>
    
    <rect x="20" y="305" width="380" height="65" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
    <text x="35" y="327" font-size="10.5" font-weight="bold" fill="#38bdf8">Design Rule of Thumb:</text>
    <text x="35" y="345" font-size="9.5" fill="#cbd5e1">Stick to a maximum of 2 complementary fonts per document (e.g. Arial for headings + Calibri for body text).</text>
  </g>

  <!-- Right Branch: Paragraph Formatting -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#059669"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LEVEL 2: PARAGRAPH FORMATTING</text>
    
    <text x="20" y="62" font-size="10" fill="#94a3b8">Applies to entire text blocks, alignments, and vertical spacing</text>
    
    <!-- 1. Alignments -->
    <rect x="20" y="78" width="380" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="35" y="98" font-size="11.5" font-weight="bold" fill="#34d399">The 4 Text Alignments:</text>
    <text x="35" y="115" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold">Left Align:</tspan> Ragged right edge; standard for letters/essays</text>
    <text x="35" y="130" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold">Center:</tspan> Symmetrical; best for titles, covers, certificates</text>
    <text x="35" y="145" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold">Justify:</tspan> Straight left &amp; right edges; newspapers &amp; books</text>
    
    <!-- 2. Spacing & Indents -->
    <rect x="20" y="163" width="380" height="65" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="35" y="185" font-size="11.5" font-weight="bold" fill="#34d399">Line &amp; Paragraph Spacing:</text>
    <text x="35" y="203" font-size="10" fill="#cbd5e1">• Line Spacing: 1.0 (single), 1.15 (clean), 1.5 (readable), 2.0 (double)</text>
    <text x="35" y="219" font-size="10" fill="#cbd5e1">• Space Before/After paragraphs prevents manual double Enters</text>
    
    <!-- 3. Lists & Bullets -->
    <rect x="20" y="238" width="380" height="65" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="35" y="260" font-size="11.5" font-weight="bold" fill="#34d399">Lists &amp; Structural Ordering:</text>
    <text x="35" y="278" font-size="10" fill="#cbd5e1">• Bulleted Lists: For unordered items, features, categories</text>
    <text x="35" y="294" font-size="10" fill="#cbd5e1">• Numbered Lists: For sequential procedures, recipes, rankings</text>
    
    <rect x="20" y="313" width="380" height="57" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1"/>
    <text x="35" y="333" font-size="10.5" font-weight="bold" fill="#34d399">Readability Standard:</text>
    <text x="35" y="351" font-size="9.5" fill="#cbd5e1">Use 1.15 or 1.5 line spacing with 6pt space after paragraphs for optimal reading comfort.</text>
  </g>
</svg>
""")

SVG_PAGE_ORIENTATION_COMPARISON = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Page Layout Architecture: Margins, Size &amp; Orientation</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Configuring the digital canvas: Portrait vs. Landscape, A4 standards, and column flow</text>

  <!-- Left: Portrait Layout Visual -->
  <g transform="translate(45, 95)">
    <rect width="260" height="385" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="260" height="32" rx="8" fill="#0284c7"/>
    <text x="130" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PORTRAIT ORIENTATION</text>
    
    <!-- Paper representation (Tall) -->
    <rect x="45" y="48" width="170" height="230" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Margin guide lines -->
    <rect x="60" y="63" width="140" height="200" fill="none" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1"/>
    
    <!-- Simulated text lines -->
    <line x1="70" y1="80" x2="190" y2="80" stroke="#64748b" stroke-width="3"/>
    <line x1="70" y1="95" x2="185" y2="95" stroke="#94a3b8" stroke-width="2"/>
    <line x1="70" y1="110" x2="190" y2="110" stroke="#94a3b8" stroke-width="2"/>
    <line x1="70" y1="125" x2="170" y2="125" stroke="#94a3b8" stroke-width="2"/>
    
    <line x1="70" y1="150" x2="190" y2="150" stroke="#94a3b8" stroke-width="2"/>
    <line x1="70" y1="165" x2="180" y2="165" stroke="#94a3b8" stroke-width="2"/>
    <line x1="70" y1="180" x2="190" y2="180" stroke="#94a3b8" stroke-width="2"/>
    
    <text x="130" y="295" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Dimensions: 210mm × 297mm (A4)</text>
    <text x="15" y="325" font-size="10" font-weight="bold" fill="#ffffff">• Best For:</text>
    <text x="15" y="342" font-size="9" fill="#cbd5e1">Official letters, essays, school reports, memos, novel manuscripts.</text>
    <text x="15" y="365" font-size="9" fill="#94a3b8">Height &gt; Width (Vertical Reading)</text>
  </g>

  <!-- Middle: Landscape Layout Visual -->
  <g transform="translate(330, 95)">
    <rect width="320" height="385" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="320" height="32" rx="8" fill="#059669"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LANDSCAPE ORIENTATION</text>
    
    <!-- Paper representation (Wide) -->
    <rect x="35" y="65" width="250" height="170" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Margin guide lines -->
    <rect x="50" y="80" width="220" height="140" fill="none" stroke="#34d399" stroke-dasharray="3,3" stroke-width="1"/>
    
    <!-- Simulated table grid -->
    <rect x="58" y="90" width="204" height="120" fill="#f8fafc" stroke="#334155" stroke-width="1"/>
    <line x1="58" y1="115" x2="262" y2="115" stroke="#334155" stroke-width="1"/>
    <line x1="58" y1="140" x2="262" y2="140" stroke="#334155" stroke-width="1"/>
    <line x1="58" y1="165" x2="262" y2="165" stroke="#334155" stroke-width="1"/>
    <line x1="58" y1="190" x2="262" y2="190" stroke="#334155" stroke-width="1"/>
    <line x1="110" y1="90" x2="110" y2="210" stroke="#334155" stroke-width="1"/>
    <line x1="160" y1="90" x2="160" y2="210" stroke="#334155" stroke-width="1"/>
    <line x1="210" y1="90" x2="210" y2="210" stroke="#334155" stroke-width="1"/>
    
    <text x="160" y="260" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Dimensions: 297mm × 210mm (A4)</text>
    <text x="15" y="295" font-size="10" font-weight="bold" fill="#ffffff">• Best For:</text>
    <text x="15" y="312" font-size="9" fill="#cbd5e1">Wide multi-column tables, timetables, certificates, project Gantt charts, wide diagrams.</text>
    <text x="15" y="340" font-size="10" font-weight="bold" fill="#ffffff">• Why it matters:</text>
    <text x="15" y="357" font-size="9" fill="#cbd5e1">Prevents squishing 10+ columns into unreadable narrow vertical strips.</text>
  </g>

  <!-- Right: Margins & Paper Size Standard -->
  <g transform="translate(675, 95)">
    <rect width="240" height="385" rx="12" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="240" height="32" rx="8" fill="#d97706"/>
    <text x="120" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MARGINS &amp; SIZING</text>
    
    <text x="15" y="58" font-size="11" font-weight="bold" fill="#fbbf24">• Standard Margins:</text>
    <text x="15" y="75" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold">Normal:</tspan> 2.54 cm (1 inch) all sides</text>
    <text x="15" y="92" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold">Narrow:</tspan> 1.27 cm (0.5 inch)</text>
    <text x="15" y="109" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold">Gutter:</tspan> Extra space for book binding</text>
    
    <text x="15" y="140" font-size="11" font-weight="bold" fill="#fbbf24">• Paper Sizes in Kenya:</text>
    <text x="15" y="158" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold">A4:</tspan> 21.0 × 29.7 cm (Standard)</text>
    <text x="15" y="175" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold">A3:</tspan> 29.7 × 42.0 cm (Double A4)</text>
    <text x="15" y="192" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold">Letter:</tspan> 21.6 × 27.9 cm (US default)</text>
    
    <text x="15" y="225" font-size="11" font-weight="bold" fill="#fbbf24">• Column Layouts:</text>
    <text x="15" y="243" font-size="9.5" fill="#cbd5e1">1-Column (Standard essay)</text>
    <text x="15" y="260" font-size="9.5" fill="#cbd5e1">2-Column (Research paper / flyer)</text>
    <text x="15" y="277" font-size="9.5" fill="#cbd5e1">3-Column (Tri-fold brochures)</text>
    
    <rect x="15" y="305" width="210" height="65" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="120" y="325" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">⚠️ Trap Alert:</text>
    <text x="120" y="343" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Always set paper size to A4 before</text>
    <text x="120" y="357" font-size="8.5" fill="#cbd5e1" text-anchor="middle">printing to avoid truncated margins!</text>
  </g>
</svg>
""")

SVG_PROOFREADING_FLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Automated Proofreading &amp; Intelligent Editing Engine</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How modern word processors analyze vocabulary, grammar, synonyms, and global substitutions</text>

  <!-- 1. Real-Time Squiggly Indicators -->
  <g transform="translate(45, 95)">
    <rect width="270" height="380" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="270" height="32" rx="8" fill="#dc2626"/>
    <text x="135" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. VISUAL ERROR SQUIGGLIES</text>
    
    <!-- Red Wavy Box -->
    <rect x="15" y="48" width="240" height="75" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
    <text x="25" y="70" font-size="11" font-weight="bold" fill="#f87171">🔴 Red Squiggly Line:</text>
    <text x="25" y="88" font-size="10" fill="#ffffff">Spelling Error: <tspan text-decoration="underline" stroke="#ef4444">lerning</tspan> ➔ <tspan fill="#34d399">learning</tspan></text>
    <text x="25" y="106" font-size="9" fill="#94a3b8">Word not in dictionary / typing typo</text>
    
    <!-- Blue/Green Wavy Box -->
    <rect x="15" y="133" width="240" height="75" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="25" y="155" font-size="11" font-weight="bold" fill="#38bdf8">🔵 Blue / Green Squiggly Line:</text>
    <text x="25" y="173" font-size="10" fill="#ffffff">Grammar: <tspan text-decoration="underline" stroke="#38bdf8">They is ready</tspan> ➔ <tspan fill="#34d399">They are ready</tspan></text>
    <text x="25" y="191" font-size="9" fill="#94a3b8">Punctuation, tense, or capitalization</text>
    
    <!-- Context Menu Simulation -->
    <rect x="15" y="218" width="240" height="145" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="25" y="238" font-size="10.5" font-weight="bold" fill="#fbbf24">Right-Click Context Menu:</text>
    <text x="35" y="258" font-size="9.5" fill="#34d399">✓ learning (Replace)</text>
    <text x="35" y="276" font-size="9.5" fill="#cbd5e1">⚡ Ignore All</text>
    <text x="35" y="294" font-size="9.5" fill="#cbd5e1">➕ Add to Dictionary (e.g. Swahili names)</text>
    <text x="35" y="312" font-size="9.5" fill="#cbd5e1">🌐 Set Proofing Language (English UK/KE)</text>
    <text x="35" y="340" font-size="9" fill="#94a3b8">• Eliminates red lines on "colour/organise"</text>
  </g>

  <!-- 2. Auto-Correct & Thesaurus -->
  <g transform="translate(345, 95)">
    <rect width="270" height="380" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="270" height="32" rx="8" fill="#059669"/>
    <text x="135" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. AUTO-CORRECT &amp; THESAURUS</text>
    
    <!-- Auto-Correct Box -->
    <rect x="15" y="48" width="240" height="150" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="25" y="70" font-size="11" font-weight="bold" fill="#34d399">Auto-Correct Engine:</text>
    <text x="25" y="88" font-size="9.5" fill="#cbd5e1">• Instant replacement on spacebar</text>
    <text x="25" y="106" font-size="9.5" fill="#ffffff">  "teh" ➔ "the"</text>
    <text x="25" y="124" font-size="9.5" fill="#ffffff">  "(c)" ➔ "©" | "(r)" ➔ "®"</text>
    <text x="25" y="144" font-size="9.5" fill="#cbd5e1">• Capitalizes first letter of sentence</text>
    <text x="25" y="162" font-size="9.5" fill="#cbd5e1">• Corrects accidental TWo INitial CAps</text>
    <text x="25" y="180" font-size="9" fill="#94a3b8">Runs silently in background</text>
    
    <!-- Thesaurus Box -->
    <rect x="15" y="208" width="240" height="155" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="25" y="230" font-size="11" font-weight="bold" fill="#34d399">Thesaurus &amp; Vocabulary:</text>
    <text x="25" y="250" font-size="9.5" fill="#cbd5e1">Lookup word: <tspan font-weight="bold" fill="#fbbf24">"Significant"</tspan></text>
    <text x="35" y="270" font-size="9" fill="#38bdf8">1. Important (adj)</text>
    <text x="35" y="288" font-size="9" fill="#38bdf8">2. Substantial (adj)</text>
    <text x="35" y="306" font-size="9" fill="#38bdf8">3. Notable (adj)</text>
    <text x="35" y="324" font-size="9" fill="#38bdf8">4. Meaningful (adj)</text>
    <text x="25" y="348" font-size="8.5" fill="#94a3b8">Prevents repetitive word fatigue in essays</text>
  </g>

  <!-- 3. Find & Replace Utility -->
  <g transform="translate(645, 95)">
    <rect width="270" height="380" rx="12" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="270" height="32" rx="8" fill="#d97706"/>
    <text x="135" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. FIND &amp; REPLACE (CTRL + H)</text>
    
    <rect x="15" y="48" width="240" height="230" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="25" y="72" font-size="11" font-weight="bold" fill="#fbbf24">Batch Substitution Dialog:</text>
    
    <text x="25" y="98" font-size="9.5" fill="#cbd5e1">Find what:</text>
    <rect x="25" y="104" width="220" height="24" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="35" y="120" font-size="10" fill="#f87171">Topic 3</text>
    
    <text x="25" y="148" font-size="9.5" fill="#cbd5e1">Replace with:</text>
    <rect x="25" y="154" width="220" height="24" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="35" y="170" font-size="10" fill="#34d399">Operating Systems</text>
    
    <!-- Action buttons -->
    <rect x="25" y="190" width="100" height="22" rx="4" fill="#0284c7"/>
    <text x="75" y="204" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Find Next</text>
    
    <rect x="135" y="190" width="110" height="22" rx="4" fill="#d97706"/>
    <text x="190" y="204" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Replace All</text>
    
    <text x="25" y="235" font-size="9" fill="#38bdf8">✓ Match case  ✓ Whole words only</text>
    <text x="25" y="255" font-size="9" fill="#34d399">Replaces 50 occurrences in 0.2s!</text>
    
    <rect x="15" y="290" width="240" height="75" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="25" y="310" font-size="10" font-weight="bold" fill="#fbbf24">Safety Protocol:</text>
    <text x="25" y="328" font-size="8.5" fill="#cbd5e1">Always use "Match case" and "Find whole words" when replacing short acronyms to avoid accidental word mutilation!</text>
  </g>
</svg>
""")

SVG_TABLE_GRID_DESIGN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Table Structural Anatomy &amp; Data Grid Formatting</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Organizing structured quantitative data into rows, columns, merged headers, and styled grids</text>

  <!-- Left: Table Grid Simulation -->
  <g transform="translate(45, 95)">
    <rect width="520" height="380" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="520" height="32" rx="8" fill="#0284c7"/>
    <text x="260" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STRUCTURED 3x4 DATA GRID EXAMPLE</text>
    
    <!-- Table Container -->
    <g transform="translate(20, 50)">
      <!-- Row 1: Main Merged Header -->
      <rect x="0" y="0" width="480" height="38" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="240" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WEEKLY GRADE 10 ICT LAB SCHEDULE (Merged Header)</text>
      
      <!-- Row 2: Column Headers -->
      <rect x="0" y="38" width="160" height="34" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="80" y="60" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Subject / Unit</text>
      
      <rect x="160" y="38" width="160" height="34" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="240" y="60" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Scheduled Day</text>
      
      <rect x="320" y="38" width="160" height="34" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="400" y="60" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Allocated Time</text>
      
      <!-- Row 3: Data Row 1 -->
      <rect x="0" y="72" width="160" height="32" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="80" y="93" font-size="10" fill="#cbd5e1" text-anchor="middle">Word Processing</text>
      
      <rect x="160" y="72" width="160" height="32" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="240" y="93" font-size="10" fill="#cbd5e1" text-anchor="middle">Monday</text>
      
      <rect x="320" y="72" width="160" height="32" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="400" y="93" font-size="10" fill="#34d399" text-anchor="middle">08:00 - 09:30 AM</text>
      
      <!-- Row 4: Data Row 2 -->
      <rect x="0" y="104" width="160" height="32" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text x="80" y="125" font-size="10" fill="#cbd5e1" text-anchor="middle">Spreadsheets</text>
      
      <rect x="160" y="104" width="160" height="32" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text x="240" y="125" font-size="10" fill="#cbd5e1" text-anchor="middle">Wednesday</text>
      
      <rect x="320" y="104" width="160" height="32" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <text x="400" y="125" font-size="10" fill="#34d399" text-anchor="middle">10:00 - 11:30 AM</text>
      
      <!-- Row 5: Data Row 3 -->
      <rect x="0" y="136" width="160" height="32" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="80" y="157" font-size="10" fill="#cbd5e1" text-anchor="middle">Database Systems</text>
      
      <rect x="160" y="136" width="160" height="32" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="240" y="157" font-size="10" fill="#cbd5e1" text-anchor="middle">Friday</text>
      
      <rect x="320" y="136" width="160" height="32" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="400" y="157" font-size="10" fill="#34d399" text-anchor="middle">02:00 - 03:30 PM</text>
    </g>

    <!-- Structural Callouts -->
    <g transform="translate(20, 240)">
      <rect width="480" height="110" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Key Structural Elements:</text>
      <text x="15" y="44" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Row:</tspan> Horizontal series of cells spanning across columns</text>
      <text x="15" y="62" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Column:</tspan> Vertical sequence of cells containing identical data category</text>
      <text x="15" y="80" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Cell:</tspan> Intersection box of a row &amp; column; holds text/numbers/images</text>
      <text x="15" y="98" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Navigation:</tspan> Press [Tab] to jump to next cell; [Shift+Tab] to jump backward</text>
    </g>
  </g>

  <!-- Right: Table Operations Panel -->
  <g transform="translate(585, 95)">
    <rect width="330" height="380" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="330" height="32" rx="8" fill="#059669"/>
    <text x="165" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">TABLE OPERATIONS &amp; TOOLS</text>
    
    <!-- 1. Merge & Split -->
    <rect x="15" y="48" width="300" height="85" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="25" y="70" font-size="11" font-weight="bold" fill="#34d399">Merge vs. Split Cells:</text>
    <text x="25" y="90" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Merge Cells:</tspan> Combines 2+ adjacent cells into 1 unified banner (used for main titles).</text>
    <text x="25" y="115" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Split Cells:</tspan> Subdivides 1 cell into multiple rows or columns for sub-metrics.</text>
    
    <!-- 2. Sizing & Alignment -->
    <rect x="15" y="143" width="300" height="85" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="25" y="165" font-size="11" font-weight="bold" fill="#34d399">Sizing &amp; Column Control:</text>
    <text x="25" y="185" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Column Drag:</tspan> Hover over grid line to see ↔ cursor.</text>
    <text x="25" y="205" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">AutoFit Window:</tspan> Adjusts table width to page margins.</text>
    <text x="25" y="220" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">AutoFit Contents:</tspan> Shrinks columns to fit longest word.</text>
    
    <!-- 3. Styling & Shading -->
    <rect x="15" y="238" width="300" height="120" rx="6" fill="#1e293b" stroke="#059669" stroke-width="1"/>
    <text x="25" y="260" font-size="11" font-weight="bold" fill="#34d399">Styling &amp; Design Guidelines:</text>
    <text x="25" y="280" font-size="9.5" fill="#cbd5e1">• Apply dark/accent shading to Header Row only</text>
    <text x="25" y="298" font-size="9.5" fill="#cbd5e1">• Use alternating row shading (Zebra striping) for long tables</text>
    <text x="25" y="316" font-size="9.5" fill="#cbd5e1">• Left-align text; Right-align numbers &amp; currency (KES)</text>
    <text x="25" y="334" font-size="9.5" fill="#cbd5e1">• Center column icons, codes, and dates</text>
  </g>
</svg>
""")

SVG_SECTION_BREAKS_STYLES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Section Breaks, Heading Styles &amp; Automated TOC</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Structuring multi-page documents, mixing portrait/landscape orientations, and generating dynamic contents</text>

  <!-- Left: Multi-Section Document Simulation -->
  <g transform="translate(45, 95)">
    <rect width="420" height="380" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#0284c7"/>
    <text x="210" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MULTI-SECTION DOCUMENT ARCHITECTURE</text>
    
    <!-- Mini Pages showing mixed layouts -->
    <g transform="translate(25, 45)">
      <!-- Page 1: Cover (No Header/Footer) -->
      <rect x="0" y="0" width="70" height="95" rx="3" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
      <text x="35" y="40" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Cover Page</text>
      <text x="35" y="55" font-size="6" fill="#64748b" text-anchor="middle">(No Page #)</text>
      <text x="35" y="110" font-size="8" fill="#38bdf8" text-anchor="middle">Section 1</text>
      
      <!-- Divider: Section Break Next Page -->
      <path d="M 75 47 L 95 47" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
      
      <!-- Page 2: Preface (Roman numerals) -->
      <rect x="100" y="0" width="70" height="95" rx="3" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
      <text x="135" y="40" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">TOC</text>
      <text x="135" y="85" font-size="7" fill="#64748b" text-anchor="middle">Page ii</text>
      <text x="135" y="110" font-size="8" fill="#38bdf8" text-anchor="middle">Section 2</text>
      
      <!-- Divider -->
      <path d="M 175 47 L 195 47" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
      
      <!-- Page 3: Main Essay (Portrait, Arabic 1, 2) -->
      <rect x="200" y="0" width="70" height="95" rx="3" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
      <text x="235" y="40" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Chapter 1</text>
      <text x="235" y="85" font-size="7" fill="#64748b" text-anchor="middle">Page 1</text>
      <text x="235" y="110" font-size="8" fill="#38bdf8" text-anchor="middle">Section 3</text>
      
      <!-- Divider -->
      <path d="M 275 47 L 295 47" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
      
      <!-- Page 4: Data Chart (Landscape!) -->
      <rect x="300" y="15" width="95" height="70" rx="3" fill="#ffffff" stroke="#10b981" stroke-width="1.5"/>
      <text x="347" y="48" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Wide Chart</text>
      <text x="347" y="62" font-size="6" fill="#059669" text-anchor="middle">[Landscape]</text>
      <text x="347" y="110" font-size="8" fill="#34d399" text-anchor="middle">Section 4</text>
    </g>

    <!-- Break Types Breakdown -->
    <g transform="translate(20, 180)">
      <rect width="380" height="175" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Break Types vs. Section Breaks:</text>
      <text x="15" y="46" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Page Break (Ctrl+Enter):</tspan> Jumps text to next page; preserves same headers, margins &amp; orientation.</text>
      <text x="15" y="80" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#f87171">Section Break (Next Page):</tspan> Creates independent formatting boundary! Allows different header, page numbering, or Landscape page in the middle of a Portrait report.</text>
      <text x="15" y="130" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#fbbf24">Continuous Break:</tspan> Changes column format (e.g. 1-column to 3-column) on the <tspan font-style="italic">same</tspan> page.</text>
    </g>
  </g>

  <!-- Right: Heading Styles & Automated TOC Panel -->
  <g transform="translate(495, 95)">
    <rect width="420" height="380" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#059669"/>
    <text x="210" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HEADING STYLES &amp; DYNAMIC TABLE OF CONTENTS</text>
    
    <!-- Styles Hierarchy Box -->
    <rect x="20" y="48" width="380" height="135" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="35" y="70" font-size="11" font-weight="bold" fill="#34d399">The Semantic Heading Tree:</text>
    <text x="35" y="92" font-size="10" fill="#38bdf8"><tspan font-weight="bold">Heading 1</tspan> (16pt Bold) ➔ Chapter 1: Introduction</text>
    <text x="55" y="112" font-size="10" fill="#34d399"><tspan font-weight="bold">Heading 2</tspan> (13pt Bold) ➔ 1.1 Purpose of Word Processing</text>
    <text x="75" y="132" font-size="10" fill="#fbbf24"><tspan font-weight="bold">Heading 3</tspan> (11pt Italic) ➔ 1.1.1 Efficiency Benefits</text>
    <text x="35" y="158" font-size="9" fill="#94a3b8">Applies programmatic semantic tags to document structure</text>
    
    <!-- Automated TOC Generation Box -->
    <rect x="20" y="195" width="380" height="160" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1"/>
    <text x="35" y="218" font-size="11" font-weight="bold" fill="#34d399">Automated Table of Contents (TOC):</text>
    <text x="35" y="238" font-size="9.5" fill="#cbd5e1">1. Go to <tspan font-weight="bold" fill="#ffffff">References Tab</tspan> ➔ Click <tspan font-weight="bold" fill="#ffffff">Table of Contents</tspan></text>
    <text x="35" y="258" font-size="9.5" fill="#cbd5e1">2. Word scans all <tspan font-weight="bold" fill="#38bdf8">Heading 1, 2, 3</tspan> tags and extracts page numbers.</text>
    <text x="35" y="278" font-size="9.5" fill="#cbd5e1">3. Inserts perfectly formatted dot leaders (`...... 12`).</text>
    <text x="35" y="302" font-size="10" font-weight="bold" fill="#fbbf24">⚡ Update Table Feature:</text>
    <text x="35" y="322" font-size="9" fill="#cbd5e1">If pages shift after editing, right-click TOC and select <tspan font-weight="bold" fill="#ffffff">"Update Entire Table"</tspan> — zero manual retyping needed!</text>
  </g>
</svg>
""")

SVG_TEXT_WRAP_HYPERLINK_FLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Graphics Integration, Text Wrapping &amp; Hyperlinks</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Embedding images with proportional scaling, text wrapping modes, and interactive web/document links</text>

  <!-- Left: 6 Text Wrapping Modes -->
  <g transform="translate(45, 95)">
    <rect width="435" height="380" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="435" height="32" rx="8" fill="#0284c7"/>
    <text x="217" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE 6 TEXT WRAPPING MODES</text>
    
    <!-- Mode 1: In Line with Text -->
    <rect x="15" y="45" width="195" height="70" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="25" y="64" font-size="10" font-weight="bold" fill="#38bdf8">1. In Line with Text:</text>
    <text x="25" y="80" font-size="8.5" fill="#cbd5e1">Acts like a giant single character; creates large empty gap above.</text>
    
    <!-- Mode 2: Square Wrap -->
    <rect x="225" y="45" width="195" height="70" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="235" y="64" font-size="10" font-weight="bold" fill="#34d399">2. Square Wrap (Standard):</text>
    <text x="235" y="80" font-size="8.5" fill="#cbd5e1">Text flows in a clean rectangular boundary around image sides.</text>
    
    <!-- Mode 3: Tight Wrap -->
    <rect x="15" y="125" width="195" height="70" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="25" y="144" font-size="10" font-weight="bold" fill="#38bdf8">3. Tight / Through:</text>
    <text x="25" y="160" font-size="8.5" fill="#cbd5e1">Text hugs the contour/edges of transparent PNG graphics.</text>
    
    <!-- Mode 4: Top & Bottom -->
    <rect x="225" y="125" width="195" height="70" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="235" y="144" font-size="10" font-weight="bold" fill="#38bdf8">4. Top and Bottom:</text>
    <text x="235" y="160" font-size="8.5" fill="#cbd5e1">Text stays strictly above and below; no text placed on sides.</text>
    
    <!-- Mode 5: Behind / In Front -->
    <rect x="15" y="205" width="405" height="55" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="25" y="225" font-size="10" font-weight="bold" fill="#fbbf24">5. Behind Text vs. In Front of Text:</text>
    <text x="25" y="243" font-size="8.5" fill="#cbd5e1"><tspan font-weight="bold">Behind:</tspan> Watermarks. <tspan font-weight="bold">In Front:</tspan> Floating badge (obscures underlying sentences).</text>
    
    <!-- Proportional Scaling Rule -->
    <g transform="translate(15, 270)">
      <rect width="405" height="95" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#f43f5e">⚠️ The Aspect Ratio Rule (Resizing Graphics):</text>
      <text x="15" y="44" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#34d399">ALWAYS drag Corner Handles (⚪):</tspan> Locks width-to-height aspect ratio.</text>
      <text x="15" y="62" font-size="9" fill="#f87171">• <tspan font-weight="bold" fill="#f87171">NEVER drag Side Handles (↔/↕):</tspan> Distorts image into ugly stretched oval.</text>
      <text x="15" y="80" font-size="8.5" fill="#94a3b8">Hold [Shift] while dragging to guarantee 100% geometric integrity.</text>
    </g>
  </g>

  <!-- Right: Hyperlinks & Cross-References Panel -->
  <g transform="translate(495, 95)">
    <rect width="420" height="380" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#059669"/>
    <text x="210" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HYPERLINKS &amp; CROSS-REFERENCING</text>
    
    <!-- Hyperlink Box -->
    <rect x="20" y="48" width="380" height="145" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="35" y="72" font-size="11" font-weight="bold" fill="#34d399">External Hyperlinks (Ctrl + K):</text>
    <text x="35" y="94" font-size="9.5" fill="#cbd5e1">• Connects typed text to an external URL, email, or local file.</text>
    
    <rect x="35" y="105" width="350" height="30" rx="4" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="45" y="124" font-size="10" fill="#38bdf8" text-decoration="underline">https://www.education.go.ke (Ministry of Education)</text>
    
    <text x="35" y="152" font-size="9" fill="#94a3b8">• Formats automatically as blue underlined text</text>
    <text x="35" y="168" font-size="9" fill="#94a3b8">• Open link by pressing [Ctrl + Left Click]</text>
    
    <!-- Cross-Referencing Box -->
    <rect x="20" y="205" width="380" height="150" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="35" y="228" font-size="11" font-weight="bold" fill="#34d399">Internal Cross-References &amp; Table of Figures:</text>
    <text x="35" y="248" font-size="9.5" fill="#cbd5e1">• Links text to an internal heading, table, or figure bookmark.</text>
    
    <rect x="35" y="258" width="350" height="28" rx="4" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="45" y="276" font-size="9.5" fill="#34d399">"Refer to Table 2: Lab Schedule on Page 4"</text>
    
    <text x="35" y="304" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#fbbf24">Dynamic Auto-Update:</tspan> If Table 2 shifts to Page 6, the cross-reference updates its page number automatically.</text>
    <text x="35" y="324" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Table of Figures:</tspan> Generates an index of all captioned illustrations.</text>
  </g>
</svg>
""")

SVG_MAIL_MERGE_ARCHITECTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mail Merge Pipeline &amp; Collaborative Review Engine</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Automating bulk personalized documents and collaborating via Track Changes and PDF distribution</text>

  <!-- Top 3-Part Mail Merge Engine Pipeline -->
  <g transform="translate(45, 90)">
    <!-- 1. Main Document Template -->
    <g transform="translate(0, 0)">
      <rect width="260" height="230" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="260" height="30" rx="6" fill="#0284c7"/>
      <text x="130" y="20" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MAIN TEMPLATE (.docx)</text>
      
      <rect x="15" y="42" width="230" height="140" rx="4" fill="#ffffff"/>
      <text x="25" y="62" font-size="9" font-weight="bold" fill="#0f172a">Dear «First_Name»,</text>
      <text x="25" y="80" font-size="8" fill="#334155">You are invited to the ICT Exhibition.</text>
      <text x="25" y="98" font-size="8" fill="#334155">Admission No: <tspan font-weight="bold" fill="#0284c7">«Adm_No»</tspan></text>
      <text x="25" y="116" font-size="8" fill="#334155">Top Subject: <tspan font-weight="bold" fill="#0284c7">«Top_Subject»</tspan></text>
      <text x="25" y="150" font-size="8" fill="#334155">Principal Signature: __________</text>
      
      <text x="130" y="202" font-size="9" fill="#38bdf8" text-anchor="middle">Static text + Dynamic Merge Fields</text>
    </g>

    <!-- Plus Icon -->
    <circle cx="288" cy="115" r="16" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="288" y="122" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">+</text>

    <!-- 2. Data Source Spreadsheet -->
    <g transform="translate(315, 0)">
      <rect width="260" height="230" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="260" height="30" rx="6" fill="#059669"/>
      <text x="130" y="20" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. DATA SOURCE (.xlsx / .csv)</text>
      
      <!-- Mini Spreadsheet Grid -->
      <g transform="translate(15, 42)">
        <rect width="230" height="140" fill="#1e293b" stroke="#334155" stroke-width="1"/>
        <!-- Header -->
        <rect width="230" height="24" fill="#047857"/>
        <text x="10" y="16" font-size="8" font-weight="bold" fill="#ffffff">First_Name</text>
        <text x="80" y="16" font-size="8" font-weight="bold" fill="#ffffff">Adm_No</text>
        <text x="150" y="16" font-size="8" font-weight="bold" fill="#ffffff">Top_Subject</text>
        
        <!-- Rows -->
        <text x="10" y="44" font-size="8" fill="#cbd5e1">Joyce</text>
        <text x="80" y="44" font-size="8" fill="#cbd5e1">1042</text>
        <text x="150" y="44" font-size="8" fill="#34d399">Computer Sci</text>
        
        <text x="10" y="68" font-size="8" fill="#cbd5e1">Mark</text>
        <text x="80" y="68" font-size="8" fill="#cbd5e1">1089</text>
        <text x="150" y="68" font-size="8" fill="#34d399">Mathematics</text>
        
        <text x="10" y="92" font-size="8" fill="#cbd5e1">Wanjiku</text>
        <text x="80" y="92" font-size="8" fill="#cbd5e1">1105</text>
        <text x="150" y="92" font-size="8" fill="#34d399">Physics</text>
        
        <text x="10" y="116" font-size="8" fill="#94a3b8">... (200 records)</text>
      </g>
      
      <text x="130" y="202" font-size="9" fill="#34d399" text-anchor="middle">Structured tabular recipient records</text>
    </g>

    <!-- Arrow -->
    <path d="M 590 115 L 625 115" stroke="#fbbf24" stroke-width="3" fill="none"/>

    <!-- 3. Merged Output -->
    <g transform="translate(640, 0)">
      <rect width="230" height="230" rx="10" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
      <rect width="230" height="30" rx="6" fill="#d97706"/>
      <text x="115" y="20" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. MERGED OUTPUT</text>
      
      <rect x="15" y="42" width="200" height="55" rx="4" fill="#ffffff"/>
      <text x="25" y="60" font-size="8" font-weight="bold" fill="#0f172a">Letter 1: Joyce (1042)</text>
      <text x="25" y="75" font-size="7.5" fill="#059669">Top Subject: Computer Sci</text>
      
      <rect x="15" y="105" width="200" height="55" rx="4" fill="#ffffff"/>
      <text x="25" y="123" font-size="8" font-weight="bold" fill="#0f172a">Letter 2: Mark (1089)</text>
      <text x="25" y="138" font-size="7.5" fill="#059669">Top Subject: Mathematics</text>
      
      <text x="115" y="185" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">⚡ 200 Unique Letters in 5 sec</text>
      <text x="115" y="202" font-size="8" fill="#cbd5e1" text-anchor="middle">Export to Individual PDFs / Print</text>
    </g>
  </g>

  <!-- Bottom: Collaboration & Review Engine (Track Changes) -->
  <g transform="translate(45, 335)">
    <rect width="870" height="150" rx="12" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="25" y="25" font-size="12.5" font-weight="bold" fill="#38bdf8">Peer Collaboration: Track Changes, Comments &amp; PDF Sharing</text>
    <line x1="25" y1="35" x2="845" y2="35" stroke="#334155" stroke-width="1"/>
    
    <!-- Left Column: Track Changes -->
    <g transform="translate(25, 45)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#f87171">• Track Changes Engine:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">Records every insertion (<tspan fill="#34d399">underlined in green</tspan>), deletion (<tspan fill="#ef4444" text-decoration="line-through">strikethrough in red</tspan>), and formatting shift.</text>
      <text x="0" y="52" font-size="9.5" fill="#cbd5e1">The document author reviews and clicks <tspan font-weight="bold" fill="#34d399">"Accept Change"</tspan> or <tspan font-weight="bold" fill="#ef4444">"Reject Change"</tspan>.</text>
      <text x="0" y="70" font-size="9" fill="#94a3b8">Prevents messy conflicting copies emailed across team members.</text>
    </g>

    <!-- Right Column: Comments & PDF -->
    <g transform="translate(460, 45)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#fbbf24">• Marginal Comments &amp; PDF Export:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#ffffff">Comments:</tspan> Sticky notes on side margin for peer feedback without altering body text.</text>
      <text x="0" y="52" font-size="9.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#ffffff">PDF Export (.pdf):</tspan> Locks fonts, vector graphics, and margins on all recipient devices.</text>
      <text x="0" y="70" font-size="9" fill="#94a3b8">Standard format for job applications, contracts, and final report submissions.</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# FULL STRUCTURED 10-LESSON DATASET FOR TOPIC 4: WORD PROCESSING
# =====================================================================

TOPIC_4_LESSONS = [
    # =========================================================================
    # LESSON 4.1.1: Meaning and Importance of Word Processing
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of Word Processing",
        "unit_description": "Foundations of word processing software, mechanical typewriter comparisons, digital text lifecycles, and eight primary organizational advantages.",
        "lesson_title": "Meaning and Importance of Word Processing",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "From Mechanical Typewriters to Modern Digital Word Processors",
                    "content": {
                        "title": "Evolution of Document Production",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Mechanical_typewriter_Adler_Junior_E.jpg",
                        "caption": "A vintage mechanical typewriter where errors required physical paper replacement, contrasting with modern digital word processors that enable non-destructive, real-time document creation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Digital Writing Revolution",
                    "content": {
                        "text": "Fifty years ago, creating an official document, legal contract, or school examination required a mechanical typewriter. If a typographical error occurred on the final paragraph of a page, the typist had to discard the physical sheet of paper and re-type the entire page from scratch. Formatting was strictly limited to fixed monospace characters, with zero capability for automated spell check or graphic embedding.\n\nToday, **word processing software** has revolutionized communication. The computer screen functions as an interactive digital writing canvas where text can be dynamically keyed in, styled, reorganized, stored, and shared across global networks with zero paper waste."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define word processing, formatting, and text editors using both functional and technical perspectives\n- Contrast digital word processors with mechanical typewriters across editing, storage, and typography\n- Explain the four stages of the word processing lifecycle: Input, Processing, Storage, and Output\n- Analyze the eight core advantages of word processing software in modern educational, medical, and commercial organizations"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Word Processing Terminology",
                    "content": {
                        "term": "Word Processing",
                        "definition": "The use of computer software to create, edit, format, store, retrieve, and output text-based digital documents.",
                        "simple": "Typing and designing letters, reports, and essays on a computer rather than writing with a pen or manual typewriter.",
                        "technical": "The programmatic capture, buffer manipulation, typographic styling, non-volatile file persistence, and multi-channel rendering of textual and embedded graphic data.",
                        "example": "Using Microsoft Word or Google Docs to type a school term report."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Eight Pillars of Word Processing Efficiency",
                    "content": {
                        "text": "Word processing software delivers eight strategic advantages over manual handwriting and typewriting:\n\n1. **Efficiency & Non-Destructive Editing:** Characters are held in dynamic RAM buffers. Mistakes are corrected instantaneously using Backspace or Delete without leaving physical blemishes.\n2. **Typographic Flexibility:** Users can switch font families (Serif vs. Sans-Serif), modify point sizes (10pt to 72pt), apply bolding, italics, underline, and color accents in real time.\n3. **Structural Organization:** Information is structured logically using bulleted lists, numbered outlines, multi-tier headings, and tabular grids.\n4. **Visual Professionalism:** Standardized margins, automated text alignment (Left, Center, Right, Justify), and page borders produce publication-grade layouts.\n5. **Seamless Collaboration:** Multiple co-authors can add marginal comments, record tracked edits, and collaborate concurrently on cloud documents.\n6. **Permanent Storage & Instant Retrieval:** Documents are saved to local disks or cloud repositories in standard formats (.docx, .odt) and retrieved in milliseconds.\n7. **Universal Electronic Distribution:** Files can be exported to fixed-layout PDFs, transmitted via email attachments, or published to websites instantly.\n8. **Intelligent Automation:** Integrated tools like spell checkers, grammar linters, automated tables of contents, and mail merge accelerate document workflows."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Word Processing Lifecycle & Production Pipeline",
                    "content": {
                        "title": "The 4-Stage Digital Word Processing Cycle",
                        "caption": "High-precision vector architecture illustrating the continuous digital flow from text capture and dynamic buffer formatting to cloud persistence and multi-channel publishing.",
                        "svg_content": SVG_WORD_PROCESSING_CYCLE
                    }
                },
                {
                    "type": "step_process",
                    "title": "Analyzing the 4-Stage Digital Workflow",
                    "content": {
                        "intro": "Every digital document passes through four sequential operational stages:",
                        "steps": [
                            {"title": "1. Input & Data Capture", "description": "Text is entered into the system via physical keyboards, touchscreen virtual keypads, voice recognition dictation, or Optical Character Recognition (OCR) scanners."},
                            {"title": "2. Real-Time Processing & Editing", "description": "The CPU holds keystrokes in a temporary memory buffer. Typographic formatting, line wrapping, automated spell checking, and paragraph styles are applied instantly."},
                            {"title": "3. Non-Volatile Storage", "description": "The digital text structure is encoded and saved permanently onto local SSDs/hard drives or remote cloud servers in standard file formats (.docx, .odt, .rtf)."},
                            {"title": "4. Output & Distribution", "description": "The finalized document is rendered for physical printing on paper, exported to portable document format (PDF), or shared electronically across networks."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Community & Enterprise Document Workflows",
                    "content": {
                        "title": "Word Processing in Kenyan Schools, Hospitals, and Law Firms",
                        "scenario": "In a busy county hospital in Nakuru, doctors and administrators draft medical discharge summaries, official referral letters, and patient care standard operating procedures (SOPs).",
                        "impact": "Before digital word processing, handwritten prescription charts and typewriter memos caused clerical errors, illegible notes, and lost patient files.",
                        "solution": "Adopting word processing templates standardizes medical reports, enables instant search across historical records, ensures clean legibility, and protects confidential patient data through encrypted storage."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Text Editors vs. Word Processors",
                    "content": {
                        "misconception": "A text editor (like Windows Notepad) and a full word processor (like MS Word) are the exact same type of software.",
                        "correction": "A text editor manipulates plain, unformatted text files (UTF-8 or ASCII encoding) without supporting font styling, tables, images, or page margins. A word processor is a rich document design suite capable of complex typography, paragraph styling, media embedding, and page layout configuration."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The Monospace Typewriter Habit",
                    "content": {
                        "mistake": "Pressing the spacebar multiple times to center a document title or pressing Enter repeatedly to jump to the next page.",
                        "why_it_happens": "Users accustomed to mechanical typewriters try to position text by inserting physical blank characters.",
                        "fix_solution": "Always use the 'Center Align' paragraph tool for titles and insert a formal 'Page Break' (Ctrl + Enter) to jump to a new page cleanly."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Typewriters vs. Word Processors",
                    "content": {
                        "question": "Which of the following represents the primary operational advantage of a digital word processor over a mechanical typewriter?",
                        "options": [
                            "It requires zero electrical power or battery backup to function",
                            "It stores text dynamically in memory, enabling instant editing and correction before printing",
                            "It physically imprints ink into paper fibers immediately upon pressing each key",
                            "It strictly restricts the typist to a single fixed monospace font"
                        ],
                        "correct": "B",
                        "explanation": "Word processors store text in a dynamic digital RAM buffer, allowing authors to delete, insert, re-arrange, and style text indefinitely without wasting paper."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Word Processor Capabilities",
                    "content": {
                        "question": "Which software application is classified as a simple plain text editor rather than a full-featured word processor?",
                        "options": [
                            "Microsoft Word",
                            "LibreOffice Writer",
                            "Windows Notepad",
                            "Google Docs"
                        ],
                        "correct": "C",
                        "explanation": "Windows Notepad is a lightweight plain text editor that lacks typographic styling, tables, images, and page formatting tools found in word processors."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Introduction to Word Processing & Productivity Tools",
                    "content": {
                        "title": "Word Processing Fundamentals & Document Creation",
                        "youtube_id": "Vb0y_1bQv3E",
                        "url": "https://www.youtube.com/watch?v=Vb0y_1bQv3E",
                        "description": "Comprehensive tutorial introducing digital word processing concepts, interface navigation, and the core benefits of electronic document workflows."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Word Processing Defined:** The digital system of creating, editing, formatting, storing, and distributing text documents.\n2. **Dynamic RAM Buffer:** Non-destructive editing allows instant error correction without re-typing entire pages.\n3. **Lifecycle Stages:** Documents transition seamlessly through Input ➔ Real-Time Editing ➔ Storage ➔ Output.\n4. **Text Editor vs. Word Processor:** Text editors handle plain code/text files; word processors provide rich typography, tables, graphics, and layout automation."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.2: Selection of Word Processing Applications
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Selection of Word Processing Applications",
        "unit_description": "Evaluation of proprietary, open-source, cloud-native, and freemium word processing platforms based on cost, connectivity, hardware, and collaboration.",
        "lesson_title": "Selection of Word Processing Applications",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Students Collaborating in a Modern School Computer Lab",
                    "content": {
                        "title": "Evaluating Software in Educational Environments",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Computer_classroom_in_Kenya.jpg",
                        "caption": "Students in a Kenyan school computer laboratory evaluating different word processing suites to determine the best tool for individual study, collaborative group work, and offline exams.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Choosing the Right Digital Pen",
                    "content": {
                        "text": "Just as an artist selects different brushes for watercolor, ink sketching, or acrylic painting, a computer user must choose the appropriate word processor for their specific technical and financial constraints.\n\nSome word processors are commercial enterprise suites requiring recurring paid subscriptions, while others are community-driven open-source projects available completely free of charge. Some require high-speed internet to operate in a web browser, whereas others function entirely offline on older hardware."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define and distinguish proprietary, open-source, cloud-native, and freemium word processing software\n- Compare Microsoft Word, Google Docs, LibreOffice Writer, and WPS Office Writer across key technical criteria\n- Evaluate organizational constraints including licensing costs, internet reliability, hardware specs, and collaboration needs\n- Formulate informed software selection recommendations for school computer labs, mobile students, and corporate workplaces"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Software Licensing Models",
                    "content": {
                        "term": "Open-Source Software (FOSS)",
                        "definition": "Software distributed with its source code accessible to the public, permitting free use, modification, and redistribution without licensing fees.",
                        "simple": "Free community-developed software that anyone can download and install without paying money.",
                        "technical": "Software released under OSI-approved licensing (such as GNU GPL or Apache), granting users rights to inspect, compile, customize, and redistribute the binary and source code.",
                        "example": "LibreOffice Writer and Apache OpenOffice Writer."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Software Archetypes",
                    "content": {
                        "text": "Modern word processors fall into four primary architectural categories:\n\n- **1. Proprietary Commercial Desktop (e.g., Microsoft Word):** Closed-source software requiring paid licenses. Offers deep industry-standard feature sets, complex macros, and advanced layout control.\n- **2. Cloud-Native Web Applications (e.g., Google Docs):** Web browser applications storing files on cloud servers. Offers real-time multi-user co-authoring, automatic version histories, and zero local installation.\n- **3. Free and Open-Source Desktop (e.g., LibreOffice Writer):** Fully free standalone suites with native OpenDocument (.odt) support. Operates 100% offline with zero subscription fees.\n- **4. Freemium & Cross-Platform (e.g., WPS Office Writer):** Provides free core editing features supported by advertisements or optional premium subscriptions, featuring excellent mobile apps."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Word Processing Applications Comparison Matrix",
                    "content": {
                        "title": "Comprehensive Platform Archetype & Evaluation Matrix",
                        "caption": "Vector comparison diagram evaluating Microsoft Word, Google Docs, LibreOffice Writer, and WPS Office Writer across cost, connectivity, collaboration, and use cases.",
                        "svg_content": SVG_WORD_PLATFORMS_MATRIX
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 4-Step Software Selection Evaluation Framework",
                    "content": {
                        "intro": "When selecting a word processor for an institution or project, follow this 4-step decision audit:",
                        "steps": [
                            {"title": "Step 1: Audit Financial Budget", "description": "Assess software acquisition and recurring subscription costs. If the budget is zero, prioritize LibreOffice Writer or Google Docs."},
                            {"title": "Step 2: Assess Internet Stability", "description": "Determine if the lab has reliable, uninterrupted high-speed internet. If connectivity is intermittent, deploy offline desktop suites (LibreOffice or MS Word Desktop)."},
                            {"title": "Step 3: Determine Collaboration Needs", "description": "If teams must co-author a single document concurrently from remote locations, choose cloud-native tools like Google Docs or Word Online."},
                            {"title": "Step 4: Check Hardware Specifications", "description": "Verify lab PC RAM, processor power, and OS compatibility (Linux, Windows, macOS, or mobile Android tablets)."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Case Study: Equipping a County School Lab",
                    "content": {
                        "title": "Software Deployment in a Rural Secondary School",
                        "scenario": "A secondary school in Machakos County receives 40 refurbished desktop computers running Ubuntu Linux with limited internet bandwidth.",
                        "impact": "Purchasing commercial software licenses would cost over KES 300,000 annually, which exceeds the school's ICT budget.",
                        "solution": "The school installs **LibreOffice Writer**. Students gain access to full word processing tools (margins, tables, styles, spell check) 100% offline, fully compatible with .docx files, with zero licensing fees."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Cloud-Only File Safety",
                    "content": {
                        "misconception": "Cloud word processors like Google Docs mean you never need to worry about internet outages or local file backups.",
                        "correction": "If your internet connection drops while working on a browser without offline sync enabled, you cannot load new files, export PDFs, or collaborate until the network is restored. Critical documents should always have offline cached backups."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Document Format Incompatibility",
                    "content": {
                        "mistake": "Saving a file in an obscure proprietary format that classmates or teachers cannot open.",
                        "why_it_happens": "Using non-standard default file extensions without checking recipient software.",
                        "fix_solution": "Save files in universally accepted standards: **.docx** (standard editable word document) or **.pdf** (fixed-layout final viewable document)."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Collaborative Software Selection",
                    "content": {
                        "question": "Four students living in different towns must simultaneously write and review a joint science symposium project report in real time. Which word processor is best suited for this task?",
                        "options": [
                            "Standalone Windows Notepad",
                            "Google Docs (or Word Online)",
                            "LibreOffice Writer installed on a single offline desktop",
                            "A manual mechanical typewriter"
                        ],
                        "correct": "B",
                        "explanation": "Google Docs and Word Online are cloud-native platforms engineered for simultaneous, real-time multi-user co-authoring and live commenting over the internet."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Open-Source Licensing",
                    "content": {
                        "question": "Which of the following is a primary characteristic of open-source word processing software such as LibreOffice Writer?",
                        "options": [
                            "It requires an expensive annual per-user subscription fee",
                            "Its source code is open to the public and it is completely free to install and distribute",
                            "It can only run inside an active web browser with high-speed internet",
                            "It blocks users from inserting tables and images"
                        ],
                        "correct": "B",
                        "explanation": "Open-source software is developed transparently, free to download, install, and distribute legally without commercial licensing restrictions."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Word Processor Comparison & Selection Guide",
                    "content": {
                        "title": "Microsoft Word vs. Google Docs vs. LibreOffice",
                        "youtube_id": "g6zJ3_VvW8w",
                        "url": "https://www.youtube.com/watch?v=g6zJ3_VvW8w",
                        "description": "Comprehensive comparative breakdown of leading word processing software suites, detailing feature sets, cloud capabilities, and cost considerations."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Software Archetypes:** Proprietary (MS Word), Cloud-Native (Google Docs), Open-Source (LibreOffice), and Freemium (WPS Office).\n2. **Decision Pillars:** Evaluate cost, internet stability, teamwork/collaboration requirements, and hardware specs.\n3. **FOSS Benefits:** Open-source tools like LibreOffice provide enterprise-grade offline formatting at zero licensing expense.\n4. **Standard Formats:** Always distribute editable files as .docx and final read-only submissions as .pdf."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.3: Fundamental Word Processing Tasks
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Fundamental Word Processing Tasks",
        "unit_description": "Essential word processing workflows: launching applications, window interface anatomy, typing ergonomics, automatic word wrap, saving (.docx), retrieving, and core keyboard shortcuts.",
        "lesson_title": "Fundamental Word Processing Tasks",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Professional Typing and Office Productivity",
                    "content": {
                        "title": "Everyday Office Document Creation",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "An administrative officer in Kenya executing core word processing tasks: launching the application, typing continuous text with automatic word wrap, and saving files securely in structured folder hierarchies.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Building Solid Digital Habits",
                    "content": {
                        "text": "Before an architect designs a skyscraper, they must first master drafting boards and scale rulers. In word processing, before you can construct complex brochures or automated thesis documents, you must master the fundamental operational foundations: navigating the window interface, typing fluidly with word wrap, and saving files safely to prevent catastrophic data loss."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify all major interface components: Title Bar, Ribbon Tabs, Canvas, Status Bar, and Zoom controls\n- Differentiate between automatic Word Wrap and manual paragraph breaks (Enter key)\n- Execute secure file storage protocols using 'Save As' versus 'Save' and navigate folder paths\n- Utilize essential efficiency keyboard shortcuts (Ctrl+N, Ctrl+O, Ctrl+S, Ctrl+P, Ctrl+Z, Ctrl+Y)"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Operational Terminology",
                    "content": {
                        "term": "Word Wrap",
                        "definition": "An automated text-flow feature in word processors that transfers a typed word to the beginning of the next line when it exceeds the right document margin.",
                        "simple": "The software automatically creates a new line as you type without you needing to press Enter.",
                        "technical": "A dynamic layout algorithm that calculates glyph metrics against current line margins and inserts soft line breaks automatically before exceeding horizontal bounding limits.",
                        "example": "Typing a continuous paragraph without pressing Enter until the paragraph concludes."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Window Interface Anatomy & File Operations",
                    "content": {
                        "text": "Mastering the word processing canvas requires understanding five primary interface zones:\n\n- **1. Title Bar:** Displays document name (`Joyce_Intro_Paragraph.docx`), application name, and window control buttons (Minimize, Maximize, Close).\n- **2. The Ribbon Palette:** Organized into functional tabs (**Home, Insert, Layout, References, Review, View**) grouping related formatting and editing icons.\n- **3. Document Canvas:** The central digital page where text, tables, and graphics are rendered.\n- **4. Status Bar:** Located at the bottom edge; provides real-time metrics including total page count, word count, proofing language, and zoom slider.\n- **5. Save vs. Save As:** Use **Save As** for naming a new file or choosing a new destination folder; use **Save (Ctrl + S)** to update existing files."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Word Processor Window Anatomy & Typing Mechanics",
                    "content": {
                        "title": "Application Interface Map & Ergonomic Typing Workflow",
                        "caption": "High-precision vector blueprint detailing window interface controls, word wrap behavior, blinking insertion point cursors, and essential productivity shortcuts.",
                        "svg_content": SVG_TYPING_NAVIGATION_WORKFLOW
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Launching, Typing, and Saving a Document",
                    "content": {
                        "intro": "Follow this standard procedure to create and securely store your first school portfolio document:",
                        "steps": [
                            {"title": "Step 1: Launch Application", "description": "Click OS Start menu or search bar, type 'Word' or 'Writer', and open the application. Select 'Blank Document'."},
                            {"title": "Step 2: Enter Paragraph Text", "description": "Type: 'Hello, my name is Joyce. I am a Grade 10 student at Greenhill Academy learning word processing.' Notice how words wrap automatically to line 2."},
                            {"title": "Step 3: Insert Paragraph Break", "description": "Press the [Enter] key ONCE only when you want to terminate the paragraph and begin a new topic block."},
                            {"title": "Step 4: Save As to Portfolio Folder", "description": "Click File ➔ Save As ➔ Browse. Navigate to 'Documents/VLearn_Portfolio'. Name the file 'Joyce_Intro_Paragraph' and select '.docx'. Click Save."},
                            {"title": "Step 5: Close & Retrieve", "description": "Close the software. Open your File Explorer, navigate to your portfolio folder, and double-click the file to verify successful retrieval."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Preventing Catastrophic Data Loss",
                    "content": {
                        "title": "The Power-Outage Disaster in a School Computer Lab",
                        "scenario": "A student in Mombasa spent 3 hours typing a comprehensive 10-page History assignment without once clicking Save. A sudden power blackout shut down the computer lab.",
                        "impact": "Because the text existed solely in volatile RAM, all 3 hours of work were completely lost.",
                        "solution": "Establish the **Ctrl + S Reflex**: Press `Ctrl + S` every 5 minutes and enable the word processor's AutoRecover interval (set to 5 minutes) to safeguard digital work."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The Enter Key Myth",
                    "content": {
                        "misconception": "You must press the Enter key whenever your typing gets close to the right edge of the computer screen.",
                        "correction": "Pressing Enter at the end of every line creates hard paragraph breaks. If you later change the font size or margins, your text will fracture into awkward, jagged, broken lines. Always let Word Wrap handle line breaks automatically."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Overwriting Files with 'Save'",
                    "content": {
                        "mistake": "Opening an existing assignment template, modifying it for a new project, and clicking 'Save' instead of 'Save As'.",
                        "why_it_happens": "Failing to distinguish between updating the existing file and saving under a new filename.",
                        "fix_solution": "Immediately upon opening a template, click **File ➔ Save As** and assign a new filename before typing any changes."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Automatic Word Wrap",
                    "content": {
                        "question": "While typing a paragraph, what occurs when a word reaches the right margin boundary in a standard word processor?",
                        "options": [
                            "The computer plays an alert sound and stops accepting keystrokes",
                            "The software automatically transfers the overflowing word to the next line without pressing Enter",
                            "The text overflows off the screen and gets permanently deleted",
                            "The font size automatically shrinks to 2pt to fit the line"
                        ],
                        "correct": "B",
                        "explanation": "Word Wrap is the automated line-breaking feature that smoothly transfers text to the next line when the right margin is reached."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Save As vs. Save",
                    "content": {
                        "question": "In which of the following scenarios is it MANDATORY to use 'Save As' rather than 'Save'?",
                        "options": [
                            "When saving a brand new document for the very first time to specify its name and folder path",
                            "When fixing a single spelling error in an existing saved document",
                            "When changing the text color from blue to black in an existing file",
                            "When closing the word processing window"
                        ],
                        "correct": "A",
                        "explanation": "'Save As' prompts the user to define the document filename, storage directory, and file format, which is required on first save or when creating copies."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Word Processor Window Anatomy & Basic Operations",
                    "content": {
                        "title": "Mastering the Word Processor Interface & Typing Mechanics",
                        "youtube_id": "r_wY5qY_9l0",
                        "url": "https://www.youtube.com/watch?v=r_wY5qY_9l0",
                        "description": "Step-by-step walkthrough demonstrating window navigation, ribbon usage, word wrap typing, folder organization, and essential keyboard shortcuts."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Interface Zones:** Title Bar (filename), Ribbon (tools), Canvas (typing), and Status Bar (metrics).\n2. **Word Wrap Principle:** Continuous typing flows naturally; press Enter ONLY to terminate a paragraph.\n3. **Storage Rules:** Use 'Save As' for new files/locations and 'Ctrl + S' regularly to update active files.\n4. **Key Shortcuts:** Master Ctrl+N (New), Ctrl+S (Save), Ctrl+O (Open), and Ctrl+P (Print)."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.4: Character and Paragraph Formatting
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Character and Paragraph Formatting",
        "unit_description": "Typographic design principles: character formatting (fonts, sizes, styles, colors), paragraph formatting (alignments, line spacing, indents), and bulleted/numbered lists.",
        "lesson_title": "Character and Paragraph Formatting",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Typographic Design in Professional Publishing",
                    "content": {
                        "title": "The Power of Typographic Layout",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "A publishing designer applying character typography and paragraph alignments to transform raw manuscript text into a visually balanced, highly readable publication.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Guiding the Reader's Eye",
                    "content": {
                        "text": "Imagine reading a newspaper where every single word—from the front-page breaking headline to the classified advertisements—was printed in 10-point, unbolded, centered text. You would find it virtually impossible to navigate! \n\nProfessional document design relies on **Character Formatting** (styling individual letters and words) and **Paragraph Formatting** (structuring text blocks, alignments, and vertical spacing) to establish clear visual hierarchy and effortless readability."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between character-level and paragraph-level formatting tools\n- Select appropriate font families (Serif vs. Sans-Serif) and size scales for formal and academic documents\n- Apply the four primary paragraph alignments: Left, Center, Right, and Justified\n- Configure line spacing (1.0, 1.15, 1.5, 2.0), paragraph spacing, and structured bulleted/numbered lists"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Formatting Hierarchy Definitions",
                    "content": {
                        "term": "Paragraph Formatting",
                        "definition": "The structural configuration of entire blocks of text, controlling horizontal alignment, line spacing, margins, indents, and bulleted lists.",
                        "simple": "Changing how an entire paragraph is positioned and spaced on the page.",
                        "technical": "The application of block-level layout attributes including alignment modes, inter-line vertical metrics, leading, paragraph indents, and tab stops.",
                        "example": "Setting an essay paragraph to Justified alignment with 1.5 line spacing."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Character vs. Paragraph Formatting Deep Dive",
                    "content": {
                        "text": "Document formatting operates across two distinct hierarchical tiers:\n\n#### A. Character Formatting (Inline Attributes)\n- **Font Family (Typeface):** **Serif** fonts (e.g., *Times New Roman, Georgia*) have decorative strokes on character ends, ideal for formal printed essays. **Sans-Serif** fonts (e.g., *Arial, Calibri*) feature clean geometric lines, ideal for modern digital displays.\n- **Font Size & Weight:** Body text is standard at **11pt or 12pt**; headings range from **14pt to 18pt**; titles range from **20pt to 24pt**. Use **Bold (B)** for keywords, *Italics (I)* for foreign/technical terms, and <u>Underline (U)</u> sparingly.\n- **Scripts:** Use *Subscript* ($H_2O$) for chemical formulas and *Superscript* ($x^2 + y^2$) for mathematical exponents.\n\n#### B. Paragraph Formatting (Block Attributes)\n- **Align Left:** Default mode; text aligns cleanly to the left margin with a ragged right edge.\n- **Center:** Text is balanced symmetrically between margins; reserved for main titles, covers, and certificates.\n- **Align Right:** Aligns to right margin; used for date headers and sender addresses.\n- **Justify:** Spacing between words is adjusted dynamically so text touches both left and right margins, forming straight vertical edges like textbooks.\n- **Line Spacing:** Standard academic formatting requires **1.15 or 1.5 line spacing** with 6pt space after paragraphs."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Typographic & Document Formatting Hierarchy",
                    "content": {
                        "title": "Two-Tier Formatting Architecture: Character vs. Paragraph",
                        "caption": "Comprehensive vector diagram illustrating font families, sizing scales, script formatting, paragraph alignment modes, line spacing, and structured list styles.",
                        "svg_content": SVG_FORMATTING_HIERARCHY
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Formatting a Professional Essay Header and List",
                    "content": {
                        "intro": "Follow these steps to format an unstyled document into an executive report:",
                        "steps": [
                            {"title": "Step 1: Style the Title", "description": "Highlight the title line 'ICT MODULE NOTES'. In the Home tab, change Font to Arial, Size to 16pt, and click Bold (B)."},
                            {"title": "Step 2: Center Align the Title", "description": "With the title highlighted, click the 'Center Align' icon in the Paragraph group (Ctrl + E)."},
                            {"title": "Step 3: Create a Bulleted Topic List", "description": "Type three topics on separate lines: 'Introduction to ICT', 'Operating Systems', 'Word Processing'. Highlight all three and click the 'Bullets' icon."},
                            {"title": "Step 4: Configure Line & Paragraph Spacing", "description": "Highlight the body text, click 'Line and Paragraph Spacing', and select '1.15'. Click 'Add 6pt Space After Paragraph'."},
                            {"title": "Step 5: Apply Justified Alignment", "description": "Select the main body paragraph and click 'Justify' (Ctrl + J) to create clean, straight magazine-style margins."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Corporate Job Application Letters",
                    "content": {
                        "title": "Professional Document Styling for Employment Resumes",
                        "scenario": "An applicant submits a curriculum vitae (CV) typed entirely in Comic Sans font, centered across all pages, with bright pink headings and zero bullet points.",
                        "impact": "Hiring managers immediately reject the CV due to unprofessional typography and difficult visual navigation.",
                        "solution": "Applying professional standards (Arial 11pt, Left Aligned body text, bold section headings, 1.15 line spacing, and clear bullet points) instantly conveys credibility, organization, and attention to detail."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: More Fonts Equal Better Design",
                    "content": {
                        "misconception": "Using four or five different fancy fonts in a single document makes it look creative and impressive.",
                        "correction": "Mixing more than two font families creates visual chaos and distracts the reader. Professional typographers recommend using at most two fonts: one for headings (e.g., Arial) and one for body text (e.g., Calibri or Times New Roman)."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Over-Justification Gaps ('Rivers of White')",
                    "content": {
                        "mistake": "Applying Justified alignment to very narrow columns, causing huge awkward white gaps between words.",
                        "why_it_happens": "Justify stretches word spacing to touch both margins; in narrow columns with long words, spacing becomes excessive.",
                        "fix_solution": "Use Left Alignment for narrow columns or enable hyphenation to break long words naturally."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Text Alignment Characteristics",
                    "content": {
                        "question": "Which paragraph alignment option adjusts word spacing so that text aligns evenly with BOTH the left and right margins, producing straight vertical borders on both sides?",
                        "options": [
                            "Left Align",
                            "Center Align",
                            "Justify",
                            "Right Align"
                        ],
                        "correct": "C",
                        "explanation": "Justify alignment stretches word spacing dynamically so text touches both margins evenly, creating clean vertical edges common in textbooks and newspapers."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Character vs. Paragraph Tools",
                    "content": {
                        "question": "Which of the following formatting actions is classified strictly as CHARACTER formatting rather than PARAGRAPH formatting?",
                        "options": [
                            "Setting line spacing to 1.5 lines",
                            "Applying Bold and Subscript to a chemical formula (H2O)",
                            "Aligning an essay block to the center of the page",
                            "Converting five sentences into a numbered list"
                        ],
                        "correct": "B",
                        "explanation": "Applying bold weight, font colors, and subscript/superscript targets individual characters and words directly, making it character-level formatting."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Character & Paragraph Formatting Mastery",
                    "content": {
                        "title": "Professional Formatting: Fonts, Spacing, Alignments & Lists",
                        "youtube_id": "S0kS6hPZ_9g",
                        "url": "https://www.youtube.com/watch?v=S0kS6hPZ_9g",
                        "description": "Comprehensive tutorial demonstrating how to use the Home ribbon font and paragraph tool groups to style executive documents, headings, and bulleted lists."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Two-Tier Hierarchy:** Character formatting alters individual letter appearance; paragraph formatting structures entire text blocks.\n2. **Typeface Selection:** Use Serif (Times New Roman) for formal print and Sans-Serif (Arial, Calibri) for clean digital screens.\n3. **The 4 Alignments:** Left (letters/essays), Center (titles/covers), Right (dates/addresses), and Justify (books/newspapers).\n4. **Readability Golden Standard:** Maintain 1.15 to 1.5 line spacing with 6pt space after paragraphs."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.5: Page Layout and Formatting
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Page Layout and Formatting",
        "unit_description": "Configuring document page boundaries: margins (normal, narrow, custom, gutter), orientation (portrait vs. landscape), paper sizing standards (A4 vs. Letter), and multi-column layouts.",
        "lesson_title": "Page Layout and Formatting",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Standard Paper Dimensions and Print Layouts",
                    "content": {
                        "title": "Physical Paper Sizing and Document Canvas Boundaries",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Printed_documents_and_stationery.jpg",
                        "caption": "Standard international A4 stationery and documents demonstrating the critical importance of aligning digital page margins, orientations, and dimensions with physical printer standards.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Setting Up Your Digital Canvas",
                    "content": {
                        "text": "Before an architect draws floorplans or a painter applies pigment, they establish the exact physical boundary of their paper. In word processing, before writing extended text, you must configure your page canvas: setting page margins, selecting paper size (A4), and choosing between tall (Portrait) and wide (Landscape) orientations to ensure your document prints and displays perfectly."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define page layout, margins, orientation, paper size, and column formatting\n- Compare Portrait and Landscape orientations and select the correct mode for specific content types\n- Distinguish between ISO standard A4 paper (210 × 297 mm) and North American Letter size\n- Configure standard, narrow, custom, and gutter margins for binding, and format multi-column newsletter pages"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Page Geometry Definitions",
                    "content": {
                        "term": "Page Orientation",
                        "definition": "The direction in which a rectangular page is displayed or printed, categorized as Portrait (vertical) or Landscape (horizontal).",
                        "simple": "Whether your page stands tall like a letter or lies wide like a television screen.",
                        "technical": "The aspect orientation of the rendering coordinate plane, defined as Portrait ($Height > Width$) or Landscape ($Width > Height$).",
                        "example": "Using Landscape orientation to fit a wide 12-month budget table without shrinking text."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Pillars of Page Setup",
                    "content": {
                        "text": "Configuring document layout in the **Layout / Page Layout tab** involves three critical parameters:\n\n#### A. Page Margins\nMargins are the blank border areas surrounding all four edges (top, bottom, left, right) of a page:\n- **Normal Margins:** 2.54 cm (1 inch) on all sides; standard for essays, official memos, and business letters.\n- **Narrow Margins:** 1.27 cm (0.5 inch); maximizes printable area to fit long text on fewer sheets.\n- **Gutter Margin:** An extra margin allowance added specifically to the inside edge (left or top) to accommodate spiral binding or book stitching without obscuring text.\n\n#### B. Paper Sizing Standards\n- **A4 (21.0 cm × 29.7 cm):** The universal standard paper size in Kenya, East Africa, and international Commonwealth countries.\n- **Letter (21.6 cm × 27.9 cm):** North American default size; slightly wider and shorter than A4. Setting a document to Letter when printing on A4 paper causes bottom margins and page numbers to clip off!\n\n#### C. Multi-Column Layouts\nSplits text flow into vertical streams across the page (2-column or 3-column), ideal for school newsletters, brochures, and academic journals."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Page Layout Architecture: Margins, Size & Orientation",
                    "content": {
                        "title": "Geometry of the Document Canvas: Portrait vs. Landscape",
                        "caption": "High-precision vector comparison detailing Portrait (210×297mm) vs Landscape (297×210mm) paper geometry, margin boundaries, gutter allowances, and column flows.",
                        "svg_content": SVG_PAGE_ORIENTATION_COMPARISON
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Configuring Page Setup for an Academic Report",
                    "content": {
                        "intro": "Follow these steps to establish correct regional page settings before typing:",
                        "steps": [
                            {"title": "Step 1: Open the Layout Tab", "description": "Click on the 'Layout' (or 'Page Layout') tab on the ribbon menu."},
                            {"title": "Step 2: Set Paper Size to A4", "description": "Click the 'Size' icon and select 'A4 (210 × 297 mm)' from the dropdown list."},
                            {"title": "Step 3: Configure Margins", "description": "Click the 'Margins' icon and select 'Normal (2.54 cm)' for standard reports, or 'Custom Margins' to add a 1.0 cm Gutter for binding."},
                            {"title": "Step 4: Select Page Orientation", "description": "Click 'Orientation' and select 'Portrait' for standard text essays, or 'Landscape' if preparing wide tabular schedules."},
                            {"title": "Step 5: Apply Multi-Columns (Optional)", "description": "To design a newsletter, click 'Columns' and select 'Two' or 'Three', adjusting the spacing gap to 0.5 cm."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Printing Kenyan National Examination Papers",
                    "content": {
                        "title": "Standardizing Examination Papers Across Schools",
                        "scenario": "A school in Eldoret formats end-term examination papers on computers set to American 'Letter' paper size.",
                        "impact": "When printed on standard Kenyan A4 paper reams, the bottom three questions on every page were cut off, disrupting the examination.",
                        "solution": "All school templates were permanently updated to ISO A4 paper size with 2.0 cm margins, guaranteeing 100% print accuracy across all school printers."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Zero Margins Fit More Content Safely",
                    "content": {
                        "misconception": "Setting margins to 0.0 cm is a great way to fit maximum text onto a single page without wasting paper.",
                        "correction": "Physical desktop printers have mechanical feed rollers that cannot print ink up to the absolute physical edge of paper (the non-printable hardware margin). Setting zero margins causes the outer words to clip off entirely."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Squishing Wide Tables in Portrait Mode",
                    "content": {
                        "mistake": "Inserting a 12-column financial table into a Portrait page, forcing table text to become squished and unreadable.",
                        "why_it_happens": "Attempting to fit horizontal data grids into narrow vertical page boundaries.",
                        "fix_solution": "Switch the table page to **Landscape Orientation** (or insert a Section Break) to provide 29.7 cm of horizontal breathing room."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Selecting Page Orientation",
                    "content": {
                        "question": "Which page orientation should an administrator select when designing a wide 10-column laboratory equipment inventory table?",
                        "options": [
                            "Portrait Orientation",
                            "Landscape Orientation",
                            "Justified Orientation",
                            "Narrow Orientation"
                        ],
                        "correct": "B",
                        "explanation": "Landscape orientation makes the page wider than it is tall (297 mm wide on A4), providing horizontal space to display multi-column data grids without compressing font size."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Gutter Margins",
                    "content": {
                        "question": "What is the purpose of adding a 'Gutter Margin' to a document page layout before printing?",
                        "options": [
                            "It changes the font color to dark blue automatically",
                            "It adds extra blank space to the binding side to ensure text is not obscured when spiral-bound or stapled",
                            "It automatically checks the document for spelling errors",
                            "It reduces the physical size of images inserted on the page"
                        ],
                        "correct": "B",
                        "explanation": "A gutter margin adds additional blank clearance along the inside spine edge of pages so that comb binding, book stitching, or stapling does not cover text."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Page Layout, Margins & Orientation in Word",
                    "content": {
                        "title": "Configuring Margins, A4 Sizing, Orientations & Column Breaks",
                        "youtube_id": "v6z8E5k1W3s",
                        "url": "https://www.youtube.com/watch?v=v6z8E5k1W3s",
                        "description": "Comprehensive tutorial covering page setup tools: configuring A4 dimensions, customizing margins, switching portrait/landscape, and building multi-column newsletters."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Page Setup Essentials:** Margins, paper size (A4), orientation, and column splits defined in the Layout tab.\n2. **Orientation Rules:** Portrait (height > width) for essays and letters; Landscape (width > height) for wide tables and certificates.\n3. **Paper Standards:** Always configure regional templates to A4 (210 × 297 mm) in Kenya.\n4. **Gutter Space:** Add gutter margin allowances to prevent binding staples and coils from hiding text."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.6: Automated Proofreading and Editing Tools
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Automated Proofreading and Editing Tools",
        "unit_description": "Intelligent writing tools: real-time spell checkers (red squiggly), grammar engines (blue squiggly), dictionary language localization, Auto-Correct, Thesaurus, and batch Find & Replace (Ctrl+H).",
        "lesson_title": "Automated Proofreading and Editing Tools",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Automated Language Processing and Document Proofreading",
                    "content": {
                        "title": "Digital Proofreading and Linguistic Quality Control",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "An editor utilizing automated proofreading linters, contextual spelling dictionaries, and linguistic thesaurus databases to ensure error-free document publication.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Your Built-In Digital Proofreader",
                    "content": {
                        "text": "In handwritten manuscripts, fixing a spelling error or replacing a repetitive word required messy correction fluid or crossed-out scribbles. Digital word processors feature an intelligent linguistic engine that constantly parses your sentences in the background—flagging typos, identifying grammatical issues, predicting words, and executing document-wide word substitutions in milliseconds."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Interpret visual proofreading indicators (red wavy lines for spelling, blue/green wavy lines for grammar)\n- Configure proofing dictionaries to regional standards (English Kenya / UK vs. US)\n- Leverage Auto-Correct and Auto-Complete for rapid, error-free typing\n- Utilize the integrated Thesaurus to enrich vocabulary and execute batch global Find & Replace operations (Ctrl + H)"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Automated Linguistic Tool Definitions",
                    "content": {
                        "term": "Find and Replace",
                        "definition": "A search and substitution utility that locates specific text strings throughout a document and replaces them with designated alternative text globally.",
                        "simple": "Telling the computer to find every time a word appears and change it to a new word in one second.",
                        "technical": "A string pattern matching algorithm with regex/wildcard support that scans document buffer memory to execute localized or global substring mutations.",
                        "example": "Replacing every occurrence of 'Form 4' with 'Grade 10' across a 50-page curriculum document."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 5 Intelligent Editing Assistants",
                    "content": {
                        "text": "Modern word processors equip authors with five automated editing tools:\n\n- **1. Spell Checker (Red Wavy Underline):** Compares typed words against built-in lexicon dictionaries. Right-clicking offers phonetically ranked corrections, 'Ignore All', or 'Add to Dictionary'.\n- **2. Grammar & Style Checker (Blue Wavy Underline):** Analyzes syntactic structure, flagging subject-verb disagreement, missing punctuation, capitalization errors, or passive voice.\n- **3. Proofing Language Localization:** Setting the language to **English (Kenya)** or **English (United Kingdom)** recognizes standard Commonwealth spellings (`colour`, `programme`, `centre`) without flagging false errors.\n- **4. Auto-Correct & Auto-Complete:** Automatically corrects common keystroke inversions on spacebar (`teh` ➔ `the`) and expands predefined shorthand symbols (`(c)` ➔ `©`).\n- **5. Integrated Thesaurus:** A comprehensive database of synonyms and antonyms that provides contextually rich vocabulary alternatives to prevent monotonous word repetition."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Automated Proofreading & Intelligent Editing Engine",
                    "content": {
                        "title": "Architecture of Linguistic Linters & Batch Search Tools",
                        "caption": "High-precision vector architecture detailing red/blue squiggly indicators, dictionary context menus, Auto-Correct triggers, Thesaurus lookup, and Ctrl+H Find & Replace dialogs.",
                        "svg_content": SVG_PROOFREADING_FLOW
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Executing Proofreading and Global Substitution",
                    "content": {
                        "intro": "Follow these steps to proofread an essay and replace terms globally:",
                        "steps": [
                            {"title": "Step 1: Type Sample Text with Errors", "description": "Type: 'Today we are lerning how to use editting tools in Topic 3.' Observe red squiggly lines under 'lerning' and 'editting'."},
                            {"title": "Step 2: Correct Spelling via Context Menu", "description": "Right-click 'lerning' and select 'learning'. Right-click 'editting' and select 'editing'."},
                            {"title": "Step 3: Enrich Vocabulary with Thesaurus", "description": "Highlight the word 'tools', go to the Review tab, and click 'Thesaurus'. Select and insert the synonym 'utilities'."},
                            {"title": "Step 4: Launch Find and Replace (Ctrl + H)", "description": "Press `Ctrl + H`. In 'Find what', type 'Topic 3'. In 'Replace with', type 'Operating Systems'."},
                            {"title": "Step 5: Execute Batch Replacement", "description": "Click 'Replace All'. Word replaces every instance across the entire document in under 0.2 seconds and reports the replacement count."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Corporate Rebranding Memos",
                    "content": {
                        "title": "Updating Commercial Documents During Company Mergers",
                        "scenario": "A Kenyan banking institution with a 200-page policy document rebrands from 'ABC Bank Kenya' to 'Apex Financial Group'.",
                        "impact": "Scanning 200 pages manually would take days and inevitably miss buried references in footnotes and tables.",
                        "solution": "Using **Find and Replace (`Ctrl + H`)** with 'Match case' enabled substituted all 450 instances in 1.2 seconds with 100% accuracy."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Spell Checkers Guarantee 100% Accuracy",
                    "content": {
                        "misconception": "If there are zero red wavy lines in my document, my essay is guaranteed to be 100% free of spelling errors.",
                        "correction": "Spell checkers only detect non-words. If you type 'their' instead of 'there', or 'from' instead of 'form', the word exists in the dictionary and will NOT be flagged with a red squiggly line! Human proofreading remains essential."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The 'US English' Red Squiggly Plague",
                    "content": {
                        "mistake": "Seeing red wavy squiggly lines under perfectly correct words like 'labour', 'favour', 'centre', and 'programme'.",
                        "why_it_happens": "The default proofreading language is set to 'English (United States)', which rejects Commonwealth spellings.",
                        "fix_solution": "Go to **Review ➔ Language ➔ Set Proofing Language**, select **English (United Kingdom)** or **English (Kenya)**, and click 'Set as Default'."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Find and Replace Tool",
                    "content": {
                        "question": "Which keyboard shortcut and tool should you use to search for all occurrences of 'Grade 9' throughout a 40-page school syllabus and replace them with 'Grade 10' instantly?",
                        "options": [
                            "Ctrl + P (Print Manager)",
                            "Ctrl + H (Find and Replace Tool)",
                            "Ctrl + Z (Undo Engine)",
                            "Ctrl + N (New Document Wizard)"
                        ],
                        "correct": "B",
                        "explanation": "Ctrl + H launches the Find and Replace dialog, enabling automated global search and substitution of text strings across an entire document."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Proofreading Indicators",
                    "content": {
                        "question": "In standard word processing suites, what does a RED wavy squiggly underline beneath a typed word indicate?",
                        "options": [
                            "A grammatical structure or punctuation error",
                            "A suspected spelling mistake not found in the active dictionary",
                            "An active hyperlink pointing to an external website",
                            "A paragraph break or section divider"
                        ],
                        "correct": "B",
                        "explanation": "A red wavy underline flags a spelling error (or unrecognized word); blue/green wavy lines indicate grammar, punctuation, or syntax errors."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Automated Editing & Proofreading Tools in Word",
                    "content": {
                        "title": "Spelling, Grammar, Thesaurus & Advanced Find and Replace",
                        "youtube_id": "9W-Z20A0v5g",
                        "url": "https://www.youtube.com/watch?v=9W-Z20A0v5g",
                        "description": "In-depth guide on utilizing proofing tools, configuring regional language dictionaries, resolving grammar flags, and mastering Ctrl+H batch replacements."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 6 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Linguistic Squigglies:** Red wavy lines indicate spelling errors; blue wavy lines indicate grammatical/syntax issues.\n2. **Language Localization:** Set proofing language to English (Kenya/UK) to validate Commonwealth spellings.\n3. **Thesaurus Power:** Expand essay vocabulary and avoid repetitive word fatigue using integrated synonym lookups.\n4. **Global Substitutions:** Use Ctrl+H Find & Replace with 'Match case' and 'Whole words only' for safe document-wide updates."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.7: Inserting and Formatting Tables
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Inserting and Formatting Tables",
        "unit_description": "Data grids in word processing: inserting tables (rows, columns, cells), structural operations (merging, splitting, inserting/deleting rows), column width resizing, and table styling.",
        "lesson_title": "Inserting and Formatting Tables",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Structured Data Organization and Tabular Summaries",
                    "content": {
                        "title": "Tabular Data Structures in School Administration",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "An educational administrator designing structured weekly timetables and student assessment rosters using word processor table grids.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Power of Structured Grids",
                    "content": {
                        "text": "Imagine reading a sports day report written as a single dense paragraph: *'In race 100m John got 12s, Mary got 13s, in race 200m John got 24s, Mary got 26s...'* It is exhausting to digest. \n\nOrganizing data into intersecting **rows and columns** forms a **Table**—the universal standard for presenting structured numerical data, school timetables, pricing schedules, and statistical comparisons."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a table, row, column, and cell in word processing\n- Insert tables using interactive grid selectors and the 'Insert Table' dialog\n- Execute structural table modifications: merging cells, splitting cells, and inserting/deleting rows and columns\n- Apply professional table formatting: header shading, border styles, column width adjustments, and cell text alignments"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Table Anatomy Definitions",
                    "content": {
                        "term": "Merge Cells",
                        "definition": "The operation of combining two or more adjacent table cells into a single, unified cell spanning across rows or columns.",
                        "simple": "Erasing the divider lines between neighboring boxes to turn them into one wide box.",
                        "technical": "A table layout transformation that coalesces multiple adjacent cell coordinate indices into a single compound bounding box entity.",
                        "example": "Merging three cells in the top row to make a centered main timetable title."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Table Anatomy and Structural Operations",
                    "content": {
                        "text": "A table is constructed from three fundamental structural elements:\n\n- **1. Row:** A horizontal series of cells running from left to right.\n- **2. Column:** A vertical sequence of cells containing identical data categories.\n- **3. Cell:** The intersecting rectangle formed where a row and column cross. Each cell acts as an independent mini-canvas holding text, numbers, or graphics.\n\n#### Key Table Operations\n- **Cell Navigation:** Press **[Tab]** to advance to the next cell to the right; press **[Shift + Tab]** to navigate backward. Pressing [Tab] in the very last bottom-right cell automatically creates a brand new row!\n- **Merging Cells:** Highlight multiple cells ➔ Right-click ➔ **Merge Cells** (ideal for main banners).\n- **Splitting Cells:** Divide a single cell into multiple sub-columns or sub-rows for detailed metric breakdowns.\n- **Resizing Columns:** Hover cursor over any vertical grid line until the **↔** double-headed arrow appears, then drag to adjust width."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Table Structural Anatomy & Data Grid Formatting",
                    "content": {
                        "title": "Anatomy of a Structured Data Grid & Table Tools",
                        "caption": "High-precision vector blueprint detailing row/column/cell anatomy, merged title banners, alternating row shading, column resizing handles, and alignment rules.",
                        "svg_content": SVG_TABLE_GRID_DESIGN
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Building a Weekly Study Schedule Table",
                    "content": {
                        "intro": "Follow these steps to insert, merge, and style a 3×4 schedule grid:",
                        "steps": [
                            {"title": "Step 1: Insert 3x4 Table Grid", "description": "Go to Insert tab ➔ Table. Highlight a 3-column by 4-row (3×4) grid and click to place it on the canvas."},
                            {"title": "Step 2: Merge the Top Header Row", "description": "Click and drag across all 3 cells in row 1. Right-click and select 'Merge Cells'. Type 'WEEKLY GRADE 10 STUDY SCHEDULE' in bold."},
                            {"title": "Step 3: Populate Column Headers", "description": "In row 2, type: 'Subject / Unit' in cell 1, press Tab, type 'Scheduled Day' in cell 2, press Tab, type 'Allocated Time' in cell 3."},
                            {"title": "Step 4: Enter Schedule Data", "description": "In row 3, enter 'Word Processing | Monday | 08:00 AM'. In row 4, enter 'Spreadsheets | Wednesday | 10:00 AM'."},
                            {"title": "Step 5: Apply Professional Styling", "description": "Highlight the header rows. In Table Design, choose a soft blue fill in 'Shading'. Center-align header text and adjust column widths."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Commercial Invoices and Quotations",
                    "content": {
                        "title": "Structured Invoicing in Retail Enterprises",
                        "scenario": "A hardware supplier in Kisumu drafts an official price quotation for school building materials.",
                        "impact": "Writing item quantities, unit prices, and total sums in plain paragraphs led to disputed totals and delayed payments.",
                        "solution": "Designing a professional table (Columns: Item No, Description, Quantity, Unit Price [KES], Total [KES]) with right-aligned numbers provided immediate financial clarity and eliminated payment disputes."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Manual Spacebars for Column Alignment",
                    "content": {
                        "misconception": "You can easily align text into columns using repeated spaces or tabs instead of inserting a table.",
                        "correction": "Because proportional fonts have variable character widths (e.g., 'W' is three times wider than 'i'), using spaces creates ragged, misaligned columns that collapse completely when opened on another computer or printed. Always use formal Tables."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Uneven Text Alignment in Number Columns",
                    "content": {
                        "mistake": "Left-aligning currency figures and decimal numbers in tables, making columns hard to compare.",
                        "why_it_happens": "Applying default left text alignment to financial data.",
                        "fix_solution": "Always **Right-Align** currency values (KES) and numeric quantities so that decimal points line up vertically."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Table Operations",
                    "content": {
                        "question": "What is the result of applying a 'Merge Cells' operation to four adjacent horizontal cells in a table header?",
                        "options": [
                            "The four cells are divided into sixteen smaller cells",
                            "The selected cells are combined into a single, unified wide cell spanning across the four columns",
                            "The table is permanently split into four independent tables",
                            "All text inside the selected cells is permanently deleted"
                        ],
                        "correct": "B",
                        "explanation": "Merging cells combines multiple adjacent cells into a single larger cell, ideal for creating unified main headings across multiple columns."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Table Keyboard Navigation",
                    "content": {
                        "question": "Which keyboard key allows you to advance smoothly from one table cell to the next adjacent cell, and creates a new row if pressed in the last cell?",
                        "options": [
                            "The Spacebar",
                            "The Tab Key",
                            "The Escape Key",
                            "The Caps Lock Key"
                        ],
                        "correct": "B",
                        "explanation": "Pressing the Tab key navigates forward through table cells sequentially; pressing Tab in the final bottom-right cell automatically creates a new row."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Inserting, Formatting & Designing Tables in Word",
                    "content": {
                        "title": "Mastering Tables: Rows, Columns, Merging & Custom Styling",
                        "youtube_id": "4kQ6Z8n9W20",
                        "url": "https://www.youtube.com/watch?v=4kQ6Z8n9W20",
                        "description": "Comprehensive tutorial demonstrating how to insert tables, merge/split cells, customize borders, apply header shading, and adjust column widths."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 7 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Table Structure:** Formed by rows (horizontal) and columns (vertical) intersecting into cells (data boxes).\n2. **Merge & Split:** Merge creates unified header banners; Split subdivides cells for detailed sub-metrics.\n3. **Navigation & Auto-Rows:** Use Tab to advance across cells; Tab in the last cell automatically spawns a new row.\n4. **Design Rules:** Left-align descriptive text, right-align numbers/currency, and shade header rows for visual contrast."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.8: Section Breaks, Styles, and Page Formatting
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Section Breaks, Styles, and Page Formatting",
        "unit_description": "Structuring complex multi-page documents: Section Breaks (Next Page, Continuous) vs Page Breaks, Headers/Footers, Heading Styles (H1, H2, H3), and automated Table of Contents (TOC) generation.",
        "lesson_title": "Section Breaks, Styles, and Page Formatting",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Multi-Chapter Book Publishing and Document Structuring",
                    "content": {
                        "title": "Structural Document Hierarchy and Section Management",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "An author structuring a multi-chapter book manuscript utilizing section breaks for independent headers and applying heading styles to automate table of contents generation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Structuring Long, Complex Publications",
                    "content": {
                        "text": "Think about reading a formal academic thesis or published textbook. The book has an unnumbered cover page, a preface numbered with lowercase Roman numerals (`i, ii, iii`), chapter pages numbered with Arabic numerals (`1, 2, 3`), and occasional fold-out wide charts in Landscape orientation.\n\nIf you attempted to build this layout manually using standard line spaces and tabs, any slight text addition would destroy the entire document layout. To build professional, multi-page publications, you must master **Section Breaks**, **Headers & Footers**, and **Heading Styles**."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between standard Page Breaks (Ctrl+Enter) and structural Section Breaks (Next Page, Continuous)\n- Configure independent Headers, Footers, and mixed page number formats across document sections\n- Apply semantic Heading Styles (Heading 1, Heading 2, Heading 3) to establish document hierarchy\n- Generate and automatically update dynamic, multi-tier Tables of Contents (TOC) with dot leaders"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Document Architecture Definitions",
                    "content": {
                        "term": "Section Break",
                        "definition": "A structural divider that partitions a document into independent segments, enabling unique page layout configurations (margins, headers, orientations) within each segment.",
                        "simple": "A divider that lets Page 1 be Portrait and Page 2 be Landscape in the exact same file.",
                        "technical": "A document partitioning delimiter that isolates layout property scopes (page geometries, running headers/footers, column counts, and numbering sequences).",
                        "example": "Inserting a 'Section Break (Next Page)' before an appendix to switch from Portrait to Landscape."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Section Breaks, Styles & Automated Tables of Contents",
                    "content": {
                        "text": "Mastering long publications requires understanding three core structural mechanisms:\n\n#### A. Page Break vs. Section Break\n- **Page Break (Ctrl + Enter):** Forces subsequent text to start on a new page, but preserves all identical margins, headers, and orientation.\n- **Section Break (Next Page):** Splits the document into an independent formatting zone. Required when you want to un-link headers/footers, restart page numbers (e.g. from Roman `iii` to Arabic `1`), or change orientation (Portrait ➔ Landscape ➔ Portrait).\n\n#### B. The Semantic Power of Heading Styles\nNever format chapter titles by manually clicking Bold and changing font size! Instead, apply **Heading 1, Heading 2, and Heading 3** from the Home tab Styles gallery. Styles tag text with semantic meaning, allowing the word processor to build navigation outlines and generate automated tables of contents.\n\n#### C. Dynamic Table of Contents (TOC)\nWhen Heading Styles are applied consistently, clicking **References ➔ Table of Contents** scans the entire document, compiles all tagged section titles, pairs them with current page numbers, and formats them with dot leaders automatically. If pages shift after editing, clicking **'Update Table'** refreshes all page numbers in one second!"
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Section Breaks, Heading Styles & Automated TOC",
                    "content": {
                        "title": "Multi-Section Document Architecture & Semantic Style Trees",
                        "caption": "High-precision vector blueprint detailing mixed section orientations, Roman vs Arabic page numbering, semantic heading style trees, and dynamic TOC compilation engines.",
                        "svg_content": SVG_SECTION_BREAKS_STYLES
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Structuring Chapters & Generating an Automated TOC",
                    "content": {
                        "intro": "Follow these steps to structure a multi-chapter report with an automated table of contents:",
                        "steps": [
                            {"title": "Step 1: Apply Heading Styles to Titles", "description": "Highlight 'CHAPTER 1: INTRODUCTION' and click 'Heading 1' in the Styles pane. Highlight subtopic '1.1 Background' and click 'Heading 2'."},
                            {"title": "Step 2: Insert Page Breaks Between Chapters", "description": "Place cursor immediately before 'CHAPTER 2: METHODOLOGY' and press [Ctrl + Enter] to jump Chapter 2 cleanly to Page 2."},
                            {"title": "Step 3: Insert Section Break for Landscape Table", "description": "Before a wide data table on Page 3, click Layout ➔ Breaks ➔ 'Section Break (Next Page)'. Set Page 3 orientation to Landscape."},
                            {"title": "Step 4: Generate Table of Contents", "description": "Place cursor on blank Page 1. Go to References tab ➔ click 'Table of Contents' ➔ select 'Automatic Table 1'. The full TOC renders instantly!"},
                            {"title": "Step 5: Test Dynamic Update", "description": "Add new paragraphs in Chapter 1. Right-click the Table of Contents, click 'Update Entire Table', and observe page numbers updating automatically."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Secondary School Project Portfolios",
                    "content": {
                        "title": "Formatting Formal Academic Term Projects",
                        "scenario": "A Grade 10 student submits a 30-page Agriculture project where the Table of Contents was typed manually with periods (......).",
                        "impact": "Adding two introductory paragraphs shifted all 30 pages down by two pages, making every single page number in the manual TOC completely wrong.",
                        "solution": "Applying standard **Heading 1 / 2 Styles** and generating an **Automated Table of Contents** allowed the student to update all 30 page references in a single click before final submission."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Manual Bolding is Just as Good as Styles",
                    "content": {
                        "misconception": "Manually making text 16pt and bold is identical to applying the 'Heading 1' style.",
                        "correction": "Manual formatting only changes visual appearance. It does NOT tag the text with structural metadata. The word processor cannot recognize manually bolded text when generating an automated Table of Contents or building navigation outlines."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Unwanted Headers on Cover Pages",
                    "content": {
                        "mistake": "Adding page numbers causes 'Page 1' to appear awkwardly across the formal project cover page.",
                        "why_it_happens": "Header and footer linking is enabled across the initial section.",
                        "fix_solution": "Double-click the header area on Page 1 and check the box for **'Different First Page'** in Header & Footer Tools to clear the cover page header cleanly."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Automated Table of Contents",
                    "content": {
                        "question": "Why is it essential to format document section titles using standard Heading Styles (Heading 1, Heading 2) rather than manual bolding when creating a long report?",
                        "options": [
                            "Manual bolding causes the computer processor to overheat",
                            "Heading styles apply semantic tags required by the word processor to automatically compile and update the Table of Contents",
                            "Manual bolding prevents the document from being saved to disk",
                            "Heading styles convert all typed words into non-editable images"
                        ],
                        "correct": "B",
                        "explanation": "The automated Table of Contents engine scans specifically for Heading 1, 2, and 3 style tags, mapping them and their current page numbers into the TOC."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Page Break vs. Section Break",
                    "content": {
                        "question": "Which break command should you insert if you want Page 3 of a report to be in Landscape orientation while Pages 1, 2, and 4 remain in Portrait orientation?",
                        "options": [
                            "Simple Page Break (Ctrl + Enter)",
                            "Line Break (Shift + Enter)",
                            "Section Break (Next Page)",
                            "Column Break"
                        ],
                        "correct": "C",
                        "explanation": "A Section Break (Next Page) creates an independent formatting segment, allowing unique page orientations, margins, and headers within that section."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Section Breaks, Styles & Automated Table of Contents",
                    "content": {
                        "title": "Mastering Heading Styles, Section Breaks & Dynamic TOC",
                        "youtube_id": "7uG0s2H5b0E",
                        "url": "https://www.youtube.com/watch?v=7uG0s2H5b0E",
                        "description": "Comprehensive tutorial demonstrating how to use section breaks for mixed page orientation, configure unlinked headers/footers, and build automated Tables of Contents."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 8 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Break Types:** Page Breaks jump text to new pages; Section Breaks create independent formatting segments for mixed orientations/headers.\n2. **Semantic Styles:** Heading 1, 2, and 3 tag section titles with structural meaning for automated document engines.\n3. **Dynamic TOC:** The Table of Contents compiles automatically from heading styles with dot leaders and updates instantly via 'Update Table'.\n4. **Cover Page Rule:** Use 'Different First Page' to suppress page numbers and headers on formal report covers."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.9: Graphics, Table of Figures, Hyperlinks, and Cross-Referencing
    # =========================================================================
    {
        "unit_order": 9,
        "unit_name": "Graphics, Table of Figures, Hyperlinks, and Cross-Referencing",
        "unit_description": "Enhancing documents with rich media: inserting images, proportional aspect ratio scaling, 6 text wrapping modes, captioned illustrations, automated Table of Figures, external hyperlinks, and internal cross-references.",
        "lesson_title": "Graphics, Table of Figures, Hyperlinks, and Cross-Referencing",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Media Integration and Hyperlinked Navigation",
                    "content": {
                        "title": "Multimedia Integration in Modern Publishing",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "A graphic designer embedding educational illustrations into text documents, configuring square text wrapping and inserting interactive web hyperlinks.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Beyond Plain Text: Interactive Media",
                    "content": {
                        "text": "Text alone cannot convey complex scientific apparatus setups, geographical maps, or mathematical geometries. Modern publications integrate high-resolution graphics, diagrams, and shapes seamlessly into body text using **Text Wrapping** rules.\n\nFurthermore, by embedding interactive **Hyperlinks** and dynamic internal **Cross-References**, digital documents transform from static sheets into interconnected, living informational hubs."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 9 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Insert images, shapes, and diagrams into word processing documents safely\n- Resize graphics proportionally using corner handles while preserving aspect ratios\n- Apply the six core Text Wrapping modes (In Line, Square, Tight, Through, Top & Bottom, Behind/In Front)\n- Add captions to illustrations, generate a Table of Figures, and insert external Hyperlinks (Ctrl+K) and internal Cross-References"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Media and Navigation Definitions",
                    "content": {
                        "term": "Text Wrapping",
                        "definition": "The layout rule that governs how body paragraph text flows around an inserted graphic, image, shape, or table.",
                        "simple": "Deciding whether text should wrap around the sides of an image or stay strictly above and below it.",
                        "technical": "The computational bounding polygon and exclusion zone configured around an embedded media object to dictate inline or floating paragraph reflow.",
                        "example": "Setting an image's text wrap to 'Square' so text flows in a neat rectangular boundary beside the picture."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Text Wrapping Modes & Linking Mechanics",
                    "content": {
                        "text": "Integrating visual media and digital links involves three essential technical skillsets:\n\n#### A. The Six Text Wrapping Modes\n- **1. In Line with Text:** Default mode; treats the image as a single massive letter. Causes large empty gaps if the picture is taller than the line.\n- **2. Square:** Text wraps in a clean rectangular border around the four sides of the image bounding box.\n- **3. Tight / Through:** Text hugs the exact contours of transparent PNG graphics or irregular shapes.\n- **4. Top and Bottom:** Text is restricted strictly to the areas above and below the graphic; side margins remain completely blank.\n- **5. Behind Text:** Places the graphic on the background plane beneath text (used for faint watermarks).\n- **6. In Front of Text:** Floats the graphic over text, obscuring underlying words (used for floating badges or stamps).\n\n#### B. Proportional Scaling (Aspect Ratio Lock)\n**Golden Rule:** Always drag from a **Corner Handle (⚪)** when resizing! Dragging side handles (↔ or ↕) stretches or squishes the image, distorting human faces and technical diagrams.\n\n#### C. Hyperlinks vs. Cross-References\n- **External Hyperlink (Ctrl + K):** Blue underlined text linking to an outside web URL (e.g. `https://www.education.go.ke`).\n- **Internal Cross-Reference:** Dynamic link pointing to an element within the same file (e.g., *'Refer to Table 1 on page 4'*). If Table 1 moves to Page 6, the cross-reference updates its page number automatically."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Graphics Integration, Text Wrapping & Hyperlinks",
                    "content": {
                        "title": "Visual Media Reflow Modes & Navigation Architecture",
                        "caption": "High-precision vector blueprint detailing all 6 text wrapping modes, corner proportional scaling vs side distortion, external hyperlinks, and dynamic cross-referencing.",
                        "svg_content": SVG_TEXT_WRAP_HYPERLINK_FLOW
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Inserting an Image with Square Wrap and Hyperlinks",
                    "content": {
                        "intro": "Follow these steps to insert an illustration, wrap text around it, and add links:",
                        "steps": [
                            {"title": "Step 1: Insert Image", "description": "Place cursor in paragraph. Go to Insert tab ➔ Pictures ➔ select a saved picture (e.g., school logo) and click Insert."},
                            {"title": "Step 2: Proportional Resize", "description": "Click the inserted image. Click and drag the bottom-right CORNER handle inward to reduce size while locking aspect ratio."},
                            {"title": "Step 3: Apply Square Text Wrapping", "description": "With image selected, click the 'Wrap Text' icon in Picture Format and select 'Square'. Drag image to the right side of the paragraph."},
                            {"title": "Step 4: Add Caption & Figure Tag", "description": "Right-click image ➔ select 'Insert Caption'. Type: 'Figure 1: Computer Lab Setup'. This tags the illustration for the Table of Figures."},
                            {"title": "Step 5: Insert Web Hyperlink", "description": "Highlight the words 'Greenhill Academy', press [Ctrl + K], enter 'https://www.greenhill.ac.ke' in the Address bar, and click OK."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Designing School Newsletters and Pamphlets",
                    "content": {
                        "title": "Publishing the Annual School Magazine",
                        "scenario": "The editorial club of a secondary school in Nakuru designs an 8-page newsletter featuring photographs of sports day and science fair winners.",
                        "impact": "Leaving images set to default 'In Line with Text' created giant blank gaps, splitting paragraphs across pages awkwardly.",
                        "solution": "Setting all images to **'Square Wrap'** or **'Tight Wrap'** allowed body text to flow gracefully around photos, creating a balanced, magazine-quality publication."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Side Handles are Fine for Resizing",
                    "content": {
                        "misconception": "Dragging the top, bottom, or side middle handles of a picture is a fast way to make it fit into a small space.",
                        "correction": "Dragging middle handles stretches or compresses the image along only one axis, destroying its geometric aspect ratio and making photos look distorted and amateurish. Always drag corner handles."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: In Front of Text Obscuring Paragraphs",
                    "content": {
                        "mistake": "Setting an image wrap to 'In Front of Text', causing the picture to float directly over words and block three full sentences from view.",
                        "why_it_happens": "'In Front of Text' disables text reflow, layering the graphic over the text plane.",
                        "fix_solution": "Change the text wrapping mode immediately to **'Square'** or **'Top and Bottom'** so paragraphs flow around the graphic cleanly."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Resizing Images Safely",
                    "content": {
                        "question": "Which handle should a user click and drag when resizing an inserted educational graphic to ensure it maintains its exact proportional aspect ratio without distortion?",
                        "options": [
                            "The top-center middle handle",
                            "The right-side middle handle",
                            "Any of the four corner circular handles",
                            "The green circular rotation handle"
                        ],
                        "correct": "C",
                        "explanation": "Dragging corner handles scales both height and width proportionally at the same time, locking the aspect ratio and preventing distortion."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Text Wrapping Modes",
                    "content": {
                        "question": "Which text wrapping mode causes body text to flow in a neat rectangular border around the sides of an inserted photograph?",
                        "options": [
                            "In Line with Text",
                            "Square",
                            "Behind Text",
                            "In Front of Text"
                        ],
                        "correct": "B",
                        "explanation": "Square text wrapping creates a clean rectangular boundary around the four sides of an image, reflowing adjacent body paragraphs neatly around it."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Images, Text Wrapping, Hyperlinks & Captions",
                    "content": {
                        "title": "Mastering Visual Media, Text Wrap & Interactive Links",
                        "youtube_id": "8Vw4T1K0p2Y",
                        "url": "https://www.youtube.com/watch?v=8Vw4T1K0p2Y",
                        "description": "Comprehensive tutorial demonstrating image insertion, proportional resizing, 6 text wrapping modes, captioning figures, and inserting hyperlinks."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 9 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Proportional Resizing:** Always drag corner handles to maintain image aspect ratio without horizontal or vertical distortion.\n2. **Text Wrapping Modes:** Use Square/Tight for clean paragraph flow; avoid accidental 'In Front of Text' overlaps.\n3. **Captions & Figures:** Right-click graphics to add figure captions for automated Table of Figures generation.\n4. **Interactive Links:** Use Ctrl+K for external hyperlinks and Cross-References for dynamic, auto-updating internal document links."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4.1.10: Collaborating with Peers, Mail Merge, and Sharing
    # =========================================================================
    {
        "unit_order": 10,
        "unit_name": "Collaborating with Peers, Mail Merge, and Sharing",
        "unit_description": "Enterprise and team workflows: Mail Merge (main template, data source, merge fields), collaborative Track Changes, marginal comments, and secure PDF export and cloud distribution.",
        "lesson_title": "Collaborating with Peers, Mail Merge, and Sharing",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Collaborative Team Editing and Cloud Co-Authoring",
                    "content": {
                        "title": "Teamwork and Automated Mass Communication",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Computer_classroom_in_Kenya.jpg",
                        "caption": "Students collaborating in a computer lab utilizing Track Changes to review peer essays, while executing a Mail Merge to generate personalized event invitation letters.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Power of Automation and Teamwork",
                    "content": {
                        "text": "Imagine you are the school president organizing the annual prize-giving gala. You need to produce 300 personalized invitation letters. Each letter must contain the student's exact name, admission number, and their academic award. Typing 300 individual letters manually would take three full days of tedious work.\n\nUsing **Mail Merge**, you can link a single letter template to a recipient spreadsheet and generate all 300 unique, personalized letters in under 30 seconds! Furthermore, with **Track Changes** and **PDF Export**, modern word processing makes teamwork seamless, traceable, and secure."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 10 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the components of a Mail Merge: Main Document Template, Data Source, and Merge Fields\n- Execute a step-by-step Mail Merge linking a letter to an Excel/CSV spreadsheet\n- Utilize Track Changes and Marginal Comments for collaborative peer editing and review workflows\n- Export and distribute finalized documents as secure, fixed-layout PDF files (.pdf)"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Mail Merge & Collaboration Definitions",
                    "content": {
                        "term": "Mail Merge",
                        "definition": "An automated document generation process that combines a static master template with a structured data source to produce multiple customized documents.",
                        "simple": "Merging one letter template with a list of names to create hundreds of personalized letters instantly.",
                        "technical": "A batch parameter substitution engine that iterates through tabular database records, interpolating merge field tokens into a document template to generate discrete output documents.",
                        "example": "Generating 200 student report cards with individual names and grades from an Excel spreadsheet."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Pillars of Mail Merge & Peer Collaboration",
                    "content": {
                        "text": "Mastering modern collaborative document production involves three core mechanisms:\n\n#### A. The 3 Components of Mail Merge\n- **1. Main Document Template:** The master file containing static body text and placeholder merge fields (e.g. `Dear «First_Name», your Adm No is «Adm_No»`).\n- **2. Data Source:** A structured spreadsheet (Excel `.xlsx` or `.csv`) containing rows of recipient records and column headers (`First_Name`, `Adm_No`, `Award`).\n- **3. Merged Document:** The final output created when the engine interpolates the data source records into the template, outputting a multi-page document or batch PDFs.\n\n#### B. Collaborative Review: Track Changes & Comments\n- **Track Changes:** Turns on a live revision recorder. Text added by a reviewer appears underlined in green/red; deleted text appears struck through. The document owner can right-click each revision and select **Accept Change** or **Reject Change**.\n- **Comments:** Marginal sticky notes that allow peers to suggest improvements without altering the actual body text.\n\n#### C. PDF Export (.pdf)\nPortable Document Format (PDF) freezes typography, fonts, tables, and vector images into a universal layout that displays identically on any phone, laptop, or printer."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Mail Merge Pipeline & Collaborative Review Engine",
                    "content": {
                        "title": "3-Tier Mail Merge Architecture & Collaborative Revision Flow",
                        "caption": "High-precision vector blueprint detailing template merge fields, tabular spreadsheet linking, batch document generation, Track Changes markup, and PDF export.",
                        "svg_content": SVG_MAIL_MERGE_ARCHITECTURE
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Executing a Complete Mail Merge",
                    "content": {
                        "intro": "Follow these steps to merge an invitation letter with a contact list of classmates:",
                        "steps": [
                            {"title": "Step 1: Create Master Letter Template", "description": "Type: 'Dear [Name], you are cordially invited to the ICT Exhibition on Friday.' Save as 'Invite_Template.docx'."},
                            {"title": "Step 2: Prepare the Data Source", "description": "In Excel, create a table with columns: 'First_Name', 'Adm_No', 'Class'. Enter 5 student rows and save as 'contacts.xlsx'."},
                            {"title": "Step 3: Link Data Source in Word", "description": "Open 'Invite_Template.docx'. Go to Mailings tab ➔ Select Recipients ➔ 'Use an Existing List...' ➔ Select 'contacts.xlsx'."},
                            {"title": "Step 4: Insert Merge Fields", "description": "Highlight '[Name]' in the letter. Click 'Insert Merge Field' on the ribbon and select 'First_Name'. It changes to «First_Name»."},
                            {"title": "Step 5: Preview & Complete Merge", "description": "Click 'Preview Results' to view classmate names. Click 'Finish & Merge' ➔ 'Edit Individual Documents' ➔ 'All' to generate 5 personalized letters."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Issuing National Examination Certificates",
                    "content": {
                        "title": "Automating County School Certificate Production",
                        "scenario": "A school in Nyeri needs to issue 450 graduation certificates, each requiring the student's full name, index number, overall grade, and principal signature.",
                        "impact": "Typing and aligning 450 certificates individually would take 25 hours with high risk of typographical name errors.",
                        "solution": "Executing a **Mail Merge** linked to the national examination database generated all 450 formatted certificates in 45 seconds, ready for immediate batch printing."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Track Changes Permanently Ruins Documents",
                    "content": {
                        "misconception": "Turning on Track Changes permanently damages your writing with messy red strike-through lines that cannot be removed.",
                        "correction": "Track Changes merely displays pending suggested revisions. The document owner maintains complete control: clicking 'Accept All Changes' adopts the suggestions cleanly, while 'Reject All Changes' restores the original text completely."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Data Source Locked / In Use Error",
                    "content": {
                        "mistake": "Word displays an error message stating 'The data source is locked or in use by another program' during Mail Merge.",
                        "why_it_happens": "The Excel spreadsheet `contacts.xlsx` is currently open in Microsoft Excel while Word is attempting to read it.",
                        "fix_solution": "Save and **close Microsoft Excel completely**, then return to Word and link the data source."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Mail Merge Requirements",
                    "content": {
                        "question": "Which two core components are strictly required to execute a successful Mail Merge in a word processor?",
                        "options": [
                            "A printer and a mechanical typewriter",
                            "A Main Document Template with merge fields and a structured recipient Data Source (spreadsheet/database)",
                            "A PDF reader and an active web browser",
                            "A graphics editor and a scanner"
                        ],
                        "correct": "B",
                        "explanation": "Mail Merge requires a main document template containing merge field placeholders and a structured tabular data source containing recipient records."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Collaborative Track Changes",
                    "content": {
                        "question": "How should a student author review suggested corrections made by a peer using Track Changes before printing the final assignment?",
                        "options": [
                            "Retype the entire document from scratch on a new page",
                            "Right-click the highlighted suggestions and choose 'Accept Change' or 'Reject Change'",
                            "Delete the word processing application from the computer",
                            "Change the page orientation to Landscape"
                        ],
                        "correct": "B",
                        "explanation": "Track Changes allows the document owner to evaluate each revision individually, choosing 'Accept Change' to keep the edit or 'Reject Change' to discard it."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Mail Merge, Track Changes & PDF Export",
                    "content": {
                        "title": "Mastering Mail Merge Automation, Collaboration & Sharing",
                        "youtube_id": "3N1J7T5b0w0",
                        "url": "https://www.youtube.com/watch?v=3N1J7T5b0w0",
                        "description": "Complete guide on linking Excel spreadsheets to Word templates, executing batch mail merges, managing collaborative revisions via Track Changes, and exporting to PDF."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 10 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Mail Merge Power:** Combines a single document template with an Excel data source to generate hundreds of personalized letters in seconds.\n2. **Merge Fields:** Placeholders (`«First_Name»`, `«Adm_No»`) dynamically populate recipient data during merge execution.\n3. **Track Changes Workflow:** Facilitates collaborative peer editing by visibly recording all additions and deletions for author approval.\n4. **PDF Distribution:** Exporting to .pdf guarantees fixed, unalterable visual layout across all recipient devices and operating systems."
                    }
                }
            ]
        ]
    }
]
