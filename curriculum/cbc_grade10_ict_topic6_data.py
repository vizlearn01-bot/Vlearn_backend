"""
VLearn CBC Grade 10 ICT — Topic 6: Desktop Publishing
Full Structured Lesson Card Definitions (Lessons 6.1.1 to 6.1.6) with Responsive Custom SVGs

Topic: Desktop Publishing (Order: 6)
Lessons:
  6.1.1: Meaning, Importance, and Categories of DTP Tools (5 pages)
  6.1.2: Interface, Navigation, and Basic File Operations (5 pages)
  6.1.3: Inserting Shapes, Pictures, and WordArt (5 pages)
  6.1.4: Layout, Typography, and Design Principles (5 pages)
  6.1.5: Document Setup, Master Pages, and Template Design (5 pages)
  6.1.6: Finalizing, Printing, and Exporting Publications (5 pages)
"""

import re

def sanitize_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# HIGH PRECISION, RESPONSIVE, MOBILE-FRIENDLY VECTOR SVGS FOR TOPIC 6
# =====================================================================

SVG_DTP_VS_WORD_PROCESSING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Word Processing vs. Desktop Publishing Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Fundamental structural differences: Linear content-driven flow vs. Spatial frame-based layout design</text>

  <!-- Left Side: Word Processor (Content-Driven) -->
  <g transform="translate(45, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="415" height="36" rx="8" fill="#0284c7"/>
    <text x="207" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">WORD PROCESSOR (Content-Driven)</text>

    <!-- Simulated Document Page with Linear Flow -->
    <g transform="translate(20, 50)">
      <rect width="180" height="230" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
      <rect x="15" y="15" width="150" height="10" rx="2" fill="#0284c7"/>
      
      <!-- Text Lines -->
      <line x1="15" y1="35" x2="165" y2="35" stroke="#94a3b8" stroke-width="3"/>
      <line x1="15" y1="45" x2="165" y2="45" stroke="#94a3b8" stroke-width="3"/>
      <line x1="15" y1="55" x2="140" y2="55" stroke="#94a3b8" stroke-width="3"/>
      
      <!-- Embedded Image Displacing Text -->
      <rect x="15" y="70" width="150" height="45" rx="4" fill="#e2e8f0" stroke="#0284c7" stroke-width="1"/>
      <text x="90" y="96" font-size="9" fill="#0369a1" text-anchor="middle">Embedded Image Block</text>
      
      <!-- Displaced Text Below -->
      <line x1="15" y1="125" x2="165" y2="125" stroke="#ef4444" stroke-width="3"/>
      <line x1="15" y1="135" x2="165" y2="135" stroke="#ef4444" stroke-width="3"/>
      <line x1="15" y1="145" x2="120" y2="145" stroke="#ef4444" stroke-width="3"/>
      
      <!-- Overflow Arrow to Page 2 -->
      <path d="M 90 160 L 90 195" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
      <polygon points="90,205 85,195 95,195" fill="#ef4444"/>
      <text x="90" y="220" font-size="8" fill="#ef4444" text-anchor="middle">Auto Page Spillover</text>
    </g>

    <!-- Word Processor Feature Breakdown -->
    <g transform="translate(215, 50)">
      <rect width="180" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="25" font-size="11" font-weight="bold" fill="#38bdf8">Key Mechanics:</text>
      <text x="15" y="45" font-size="9.5" fill="#cbd5e1">• Linear Text Stream</text>
      <text x="15" y="65" font-size="8.5" fill="#94a3b8">Text flows like water from top to bottom margins.</text>
      
      <text x="15" y="90" font-size="9.5" fill="#cbd5e1">• Automatic Pagination</text>
      <text x="15" y="110" font-size="8.5" fill="#94a3b8">Spills onto page 2 automatically when buffer fills.</text>
      
      <text x="15" y="135" font-size="9.5" fill="#cbd5e1">• Inline Displacement</text>
      <text x="15" y="155" font-size="8.5" fill="#94a3b8">Images push body paragraphs downward awkwardly.</text>

      <rect x="10" y="180" width="160" height="40" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
      <text x="90" y="196" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Best For:</text>
      <text x="90" y="210" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Essays, reports, letters, memos</text>
    </g>

    <!-- Bottom Metric Card -->
    <rect x="15" y="295" width="385" height="80" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
    <text x="25" y="318" font-size="10.5" font-weight="bold" fill="#38bdf8">Primary Engine Characteristic:</text>
    <text x="25" y="338" font-size="9.5" fill="#cbd5e1">Text-driven data model with limited spatial placement controls. Objects anchored directly to paragraph stream.</text>
    <text x="25" y="360" font-size="9" fill="#94a3b8">Examples: Microsoft Word, Google Docs, LibreOffice Writer</text>
  </g>

  <!-- Right Side: Desktop Publisher (Layout-Driven) -->
  <g transform="translate(500, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="415" height="36" rx="8" fill="#059669"/>
    <text x="207" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">DESKTOP PUBLISHER (Layout-Driven)</text>

    <!-- Simulated Canvas with Independent Frames & Coordinates -->
    <g transform="translate(20, 50)">
      <rect width="180" height="230" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
      
      <!-- Dotted Margin & Column Guides -->
      <rect x="10" y="10" width="160" height="210" fill="none" stroke="#38bdf8" stroke-dasharray="2,2" stroke-width="1"/>
      <line x1="90" y1="10" x2="90" y2="220" stroke="#f472b6" stroke-dasharray="2,2" stroke-width="1"/>
      
      <!-- Independent Movable Text Frame -->
      <rect x="15" y="18" width="68" height="85" rx="3" fill="#dcfce7" stroke="#10b981" stroke-width="1.5"/>
      <text x="49" y="32" font-size="7.5" font-weight="bold" fill="#047857" text-anchor="middle">Text Frame A</text>
      <line x1="20" y1="42" x2="78" y2="42" stroke="#10b981" stroke-width="1.5"/>
      <line x1="20" y1="50" x2="78" y2="50" stroke="#10b981" stroke-width="1.5"/>
      <line x1="20" y1="58" x2="65" y2="58" stroke="#10b981" stroke-width="1.5"/>
      
      <!-- Coordinate Badge -->
      <rect x="18" y="70" width="62" height="15" rx="2" fill="#065f46"/>
      <text x="49" y="80" font-size="7" fill="#6ee7b7" text-anchor="middle">X:12mm Y:15mm</text>
      
      <!-- Circular Image Frame with Tight Text Wrap -->
      <circle cx="130" cy="60" r="28" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
      <text x="130" y="63" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Image</text>
      
      <!-- Linked Second Text Frame Below -->
      <rect x="15" y="115" width="150" height="75" rx="3" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
      <text x="90" y="130" font-size="8" font-weight="bold" fill="#0369a1" text-anchor="middle">Linked Text Frame B (Overflow)</text>
      <line x1="22" y1="142" x2="158" y2="142" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="22" y1="152" x2="158" y2="152" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="22" y1="162" x2="130" y2="162" stroke="#0284c7" stroke-width="1.5"/>
      
      <!-- Frame Link Pipeline -->
      <path d="M 83 60 C 95 60, 95 110, 85 115" fill="none" stroke="#10b981" stroke-width="2"/>
    </g>

    <!-- DTP Feature Breakdown -->
    <g transform="translate(215, 50)">
      <rect width="180" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="25" font-size="11" font-weight="bold" fill="#34d399">Key Mechanics:</text>
      <text x="15" y="45" font-size="9.5" fill="#cbd5e1">• Frame-Based Design</text>
      <text x="15" y="65" font-size="8.5" fill="#94a3b8">Text and images exist only inside movable frames.</text>
      
      <text x="15" y="90" font-size="9.5" fill="#cbd5e1">• Precise Coordinates</text>
      <text x="15" y="110" font-size="8.5" fill="#94a3b8">Millimeter-level placement on X and Y axes.</text>
      
      <text x="15" y="135" font-size="9.5" fill="#cbd5e1">• Manual Story Linking</text>
      <text x="15" y="155" font-size="8.5" fill="#94a3b8">Overset text buffers flow into linked target frames.</text>

      <rect x="10" y="180" width="160" height="40" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
      <text x="90" y="196" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Best For:</text>
      <text x="90" y="210" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Flyers, magazines, brochures, books</text>
    </g>

    <!-- Bottom Metric Card -->
    <rect x="15" y="295" width="385" height="80" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="25" y="318" font-size="10.5" font-weight="bold" fill="#34d399">Primary Engine Characteristic:</text>
    <text x="25" y="338" font-size="9.5" fill="#cbd5e1">Spatial coordinate architecture with master pages, bleed management, CMYK color separation, and preflight print packaging.</text>
    <text x="25" y="360" font-size="9" fill="#94a3b8">Examples: Adobe InDesign, Microsoft Publisher, Scribus, QuarkXPress</text>
  </g>
</svg>
""")

SVG_DTP_INTERFACE_ANATOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">DTP Workspace Anatomy &amp; Layout Geometry</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Navigating the pasteboard, rulers, layout guides, page canvas, and navigation sidebar</text>

  <!-- Left Section: Main DTP Window Simulation -->
  <g transform="translate(45, 90)">
    <rect width="550" height="385" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    
    <!-- Title Bar -->
    <rect width="550" height="26" rx="8" fill="#1e293b"/>
    <circle cx="15" cy="13" r="4.5" fill="#ef4444"/>
    <circle cx="30" cy="13" r="4.5" fill="#f59e0b"/>
    <circle cx="45" cy="13" r="4.5" fill="#10b981"/>
    <text x="275" y="18" font-size="11" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Community_Health_Brochure.pub - Microsoft Publisher</text>
    
    <!-- Menu / Ribbon Tabs -->
    <rect y="26" width="550" height="28" fill="#0284c7"/>
    <text x="20" y="44" font-size="10" font-weight="bold" fill="#ffffff">File</text>
    <text x="55" y="44" font-size="10" font-weight="bold" fill="#ffffff">Home</text>
    <text x="95" y="44" font-size="10" fill="#bae6fd">Insert</text>
    <text x="140" y="44" font-size="10" fill="#bae6fd">Page Design</text>
    <text x="215" y="44" font-size="10" fill="#bae6fd">Mailings</text>
    <text x="270" y="44" font-size="10" fill="#bae6fd">Review</text>
    <text x="320" y="44" font-size="10" fill="#bae6fd">View</text>
    
    <!-- Ribbon Tool Palette -->
    <rect y="54" width="550" height="36" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <rect x="10" y="58" width="130" height="28" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="20" y="76" font-size="10" fill="#38bdf8">Pointer</text>
    <text x="65" y="76" font-size="10" fill="#34d399">Text Frame</text>
    <text x="125" y="76" font-size="10" fill="#fbbf24">Picture</text>
    
    <!-- Left Navigation Sidebar: Page Thumbnails -->
    <rect x="0" y="90" width="75" height="265" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="37" y="108" font-size="9" font-weight="bold" fill="#94a3b8" text-anchor="middle">PAGES</text>
    
    <!-- Page 1 (Active) -->
    <rect x="10" y="118" width="55" height="42" rx="3" fill="#ffffff" stroke="#38bdf8" stroke-width="2"/>
    <text x="37" y="142" font-size="8" font-weight="bold" fill="#0284c7" text-anchor="middle">Page 1</text>
    
    <!-- Page 2 -->
    <rect x="10" y="168" width="55" height="42" rx="3" fill="#334155" stroke="#475569" stroke-width="1"/>
    <text x="37" y="192" font-size="8" fill="#94a3b8" text-anchor="middle">Page 2</text>
    
    <!-- Page 3 -->
    <rect x="10" y="218" width="55" height="42" rx="3" fill="#334155" stroke="#475569" stroke-width="1"/>
    <text x="37" y="242" font-size="8" fill="#94a3b8" text-anchor="middle">Page 3</text>
    
    <!-- Page 4 -->
    <rect x="10" y="268" width="55" height="42" rx="3" fill="#334155" stroke="#475569" stroke-width="1"/>
    <text x="37" y="292" font-size="8" fill="#94a3b8" text-anchor="middle">Page 4</text>

    <!-- Workspace Area: Grey Scratch Area / Pasteboard -->
    <rect x="75" y="90" width="475" height="265" fill="#475569"/>
    
    <!-- Horizontal Ruler -->
    <rect x="95" y="90" width="455" height="18" fill="#334155" stroke="#475569" stroke-width="1"/>
    <text x="120" y="103" font-size="8" fill="#cbd5e1">0</text>
    <text x="180" y="103" font-size="8" fill="#cbd5e1">50mm</text>
    <text x="260" y="103" font-size="8" fill="#cbd5e1">100mm</text>
    <text x="340" y="103" font-size="8" fill="#cbd5e1">150mm</text>
    <text x="420" y="103" font-size="8" fill="#cbd5e1">200mm</text>
    <line x1="220" y1="90" x2="220" y2="108" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Vertical Ruler -->
    <rect x="75" y="108" width="20" height="247" fill="#334155" stroke="#475569" stroke-width="1"/>
    <text x="85" y="130" font-size="8" fill="#cbd5e1" text-anchor="middle">0</text>
    <text x="85" y="180" font-size="8" fill="#cbd5e1" text-anchor="middle">50</text>
    <text x="85" y="240" font-size="8" fill="#cbd5e1" text-anchor="middle">100</text>
    <text x="85" y="300" font-size="8" fill="#cbd5e1" text-anchor="middle">150</text>

    <!-- Active Central Page Canvas (White A4 Sheet) -->
    <rect x="140" y="120" width="260" height="215" rx="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    
    <!-- Margin Guides (Blue dotted) -->
    <rect x="152" y="132" width="236" height="191" fill="none" stroke="#0284c7" stroke-dasharray="3,2" stroke-width="1"/>
    
    <!-- Column Guides (Pink dotted) -->
    <line x1="265" y1="132" x2="265" y2="323" stroke="#ec4899" stroke-dasharray="3,2" stroke-width="1"/>
    
    <!-- Staged Elements on Page -->
    <rect x="160" y="140" width="95" height="30" rx="3" fill="#0284c7"/>
    <text x="207" y="158" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">HEALTH TITLE</text>
    
    <rect x="160" y="178" width="95" height="135" rx="3" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="168" y1="190" x2="245" y2="190" stroke="#64748b" stroke-width="2"/>
    <line x1="168" y1="200" x2="245" y2="200" stroke="#64748b" stroke-width="2"/>
    <line x1="168" y1="210" x2="230" y2="210" stroke="#64748b" stroke-width="2"/>
    
    <!-- Column 2 Picture Frame -->
    <rect x="275" y="140" width="105" height="85" rx="3" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="327" y="185" font-size="9" font-weight="bold" fill="#854d0e" text-anchor="middle">Clinic Photo</text>

    <!-- Staging Assets in the Grey Scratch Area (Pasteboard) -->
    <rect x="420" y="135" width="115" height="55" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="477" y="155" font-size="8" font-weight="bold" fill="#fbbf24" text-anchor="middle">SCRATCH AREA</text>
    <text x="477" y="172" font-size="7.5" fill="#cbd5e1" text-anchor="middle">Logo Draft Staged</text>
    
    <rect x="420" y="210" width="115" height="65" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="477" y="235" font-size="8" font-weight="bold" fill="#34d399" text-anchor="middle">Extra Bio Text</text>
    <text x="477" y="252" font-size="7.5" fill="#94a3b8" text-anchor="middle">Non-Printing Holding</text>

    <!-- Status Bar -->
    <rect y="355" width="550" height="30" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="15" y="373" font-size="9" fill="#94a3b8">Page 1 of 4  •  A4 Portrait  •  X: 25.4mm  Y: 42.0mm</text>
    <text x="450" y="373" font-size="9" fill="#38bdf8">🔍 100% [—+—]</text>
  </g>

  <!-- Right Info Panel: Core Workspace Concepts -->
  <g transform="translate(615, 90)">
    <!-- Scratch Area Box -->
    <rect width="300" height="120" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="300" height="28" rx="8" fill="#d97706"/>
    <text x="150" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Scratch Area (Pasteboard)</text>
    <text x="15" y="46" font-size="9.5" font-weight="bold" fill="#fbbf24">• Purpose:</text>
    <text x="15" y="62" font-size="8.5" fill="#cbd5e1">Off-canvas staging area for holding photos, shapes, and draft text blocks.</text>
    <text x="15" y="85" font-size="9.5" font-weight="bold" fill="#fbbf24">• Non-Printing:</text>
    <text x="15" y="101" font-size="8.5" fill="#cbd5e1">Items placed in the scratch area NEVER appear in final print/PDF exports.</text>

    <!-- Layout & Snap Guides Box -->
    <rect y="130" width="300" height="120" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect y="130" width="300" height="28" rx="8" fill="#0284c7"/>
    <text x="150" y="148" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Rulers &amp; Magnetic Guides</text>
    <text x="15" y="176" font-size="9.5" font-weight="bold" fill="#38bdf8">• Ruler Guides:</text>
    <text x="15" y="192" font-size="8.5" fill="#cbd5e1">Drag guidelines from top/left rulers to align multiple elements.</text>
    <text x="15" y="215" font-size="9.5" font-weight="bold" fill="#38bdf8">• Snap-to-Guides:</text>
    <text x="15" y="231" font-size="8.5" fill="#cbd5e1">Objects magnetically lock onto guides for pixel-perfect precision.</text>

    <!-- File Management Strategy Box -->
    <rect y="260" width="300" height="125" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect y="260" width="300" height="28" rx="8" fill="#059669"/>
    <text x="150" y="278" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Dual File Format Rule</text>
    <text x="15" y="306" font-size="9" font-weight="bold" fill="#34d399">• Master Editable (.pub / .sla):</text>
    <text x="15" y="320" font-size="8" fill="#cbd5e1">Keeps layers, linked images, and scratch area objects for editing.</text>
    <text x="15" y="340" font-size="9" font-weight="bold" fill="#34d399">• Export Print (.pdf):</text>
    <text x="15" y="354" font-size="8" fill="#cbd5e1">Embeds fonts and flattens layouts for universal print shops.</text>
  </g>
</svg>
""")

SVG_GRAPHIC_FRAMES_TEXT_WRAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Graphic Frames, Aspect Ratio &amp; Text Wrapping Modes</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Mastering proportional scaling, non-destructive cropping, and automated text collision wrapping</text>

  <!-- Left: Scaling & Cropping Mechanics -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#0284c7"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">IMAGE SCALING VS. NON-DESTRUCTIVE CROPPING</text>

    <!-- Shift-Lock Rule vs Middle Handle Distortion -->
    <g transform="translate(20, 50)">
      <!-- Correct: Shift + Corner Handle -->
      <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <rect width="180" height="24" rx="6" fill="#059669"/>
      <text x="90" y="16" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">CORRECT: Shift + Corner</text>
      
      <!-- Proportionate Image Box -->
      <rect x="40" y="35" width="100" height="75" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
      <circle cx="90" cy="72" r="22" fill="#10b981" opacity="0.3"/>
      <text x="90" y="76" font-size="14" text-anchor="middle">🦁</text>
      
      <!-- Corner Handle Highlight -->
      <rect x="136" y="106" width="8" height="8" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
      <path d="M 144 114 L 160 130" stroke="#38bdf8" stroke-width="2"/>
      <text x="90" y="132" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">Locked Aspect Ratio (4:3)</text>
    </g>

    <!-- Incorrect: Middle Handle Stretch -->
    <g transform="translate(220, 50)">
      <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <rect width="180" height="24" rx="6" fill="#b91c1c"/>
      <text x="90" y="16" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">WRONG: Side Handle Drag</text>
      
      <!-- Distorted Stretched Box -->
      <rect x="25" y="35" width="130" height="75" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <ellipse cx="90" cy="72" rx="45" ry="22" fill="#ef4444" opacity="0.3"/>
      <text x="90" y="76" font-size="14" text-anchor="middle" transform="scale(1.5, 0.8) translate(-30, 18)">🦁</text>
      
      <!-- Middle Handle Drag Highlight -->
      <rect x="151" y="68" width="8" height="8" fill="#ef4444" stroke="#ffffff" stroke-width="1"/>
      <line x1="155" y1="72" x2="175" y2="72" stroke="#ef4444" stroke-width="2"/>
      <text x="90" y="132" font-size="8.5" font-weight="bold" fill="#f87171" text-anchor="middle">Lopsided Pixel Distortion</text>
    </g>

    <!-- Cropping Explanation Sub-Box -->
    <g transform="translate(20, 215)">
      <rect width="380" height="155" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#38bdf8">The Crop Masking Principle:</text>
      <text x="15" y="44" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Non-Destructive Trimming:</tspan> Slices outer unwanted borders without deleting pixels.</text>
      <text x="15" y="64" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Frame vs Content:</tspan> The outer frame acts as a window; the image can be panned inside.</text>
      <text x="15" y="84" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Fitting Options:</tspan> 'Fit Picture to Frame' vs 'Fill Frame Proportionally'.</text>
      
      <rect x="15" y="105" width="350" height="36" rx="4" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
      <text x="190" y="122" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Golden Rule: ALWAYS hold [Shift] and drag CORNERS to resize!</text>
      <text x="190" y="135" font-size="8" fill="#94a3b8" text-anchor="middle">Use Crop tool to adjust frame shape, never squeeze handles.</text>
    </g>
  </g>

  <!-- Right: 4 Primary Text Wrapping Modes -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#059669"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">TEXT WRAPPING FLOW FORMATTING MODES</text>

    <!-- Mode 1: Square Wrap -->
    <g transform="translate(20, 50)">
      <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="90" y="20" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Square Wrap</text>
      
      <!-- Graphic Box -->
      <rect x="60" y="35" width="60" height="50" rx="3" fill="#0284c7"/>
      <text x="90" y="64" font-size="8" fill="#ffffff" text-anchor="middle">Image</text>
      
      <!-- Surrounding Text Lines (Square Boundary) -->
      <line x1="15" y1="42" x2="52" y2="42" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="55" x2="52" y2="55" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="68" x2="52" y2="68" stroke="#94a3b8" stroke-width="2"/>
      <line x1="128" y1="42" x2="165" y2="42" stroke="#94a3b8" stroke-width="2"/>
      <line x1="128" y1="55" x2="165" y2="55" stroke="#94a3b8" stroke-width="2"/>
      <line x1="128" y1="68" x2="165" y2="68" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="98" x2="165" y2="98" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="110" x2="165" y2="110" stroke="#94a3b8" stroke-width="2"/>
      
      <text x="90" y="136" font-size="8" fill="#cbd5e1" text-anchor="middle">Flows around 4 straight edges</text>
    </g>

    <!-- Mode 2: Tight Wrap -->
    <g transform="translate(220, 50)">
      <rect width="180" height="150" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="90" y="20" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">2. Tight Contour Wrap</text>
      
      <!-- Circular Graphic -->
      <circle cx="90" cy="62" r="26" fill="#059669"/>
      <text x="90" y="66" font-size="8" fill="#ffffff" text-anchor="middle">Badge</text>
      
      <!-- Contoured Text Lines -->
      <line x1="15" y1="42" x2="58" y2="42" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="55" x2="52" y2="55" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="68" x2="52" y2="68" stroke="#94a3b8" stroke-width="2"/>
      <line x1="122" y1="42" x2="165" y2="42" stroke="#94a3b8" stroke-width="2"/>
      <line x1="128" y1="55" x2="165" y2="55" stroke="#94a3b8" stroke-width="2"/>
      <line x1="128" y1="68" x2="165" y2="68" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="98" x2="165" y2="98" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="110" x2="165" y2="110" stroke="#94a3b8" stroke-width="2"/>
      
      <text x="90" y="136" font-size="8" fill="#cbd5e1" text-anchor="middle">Hugs physical vector shape</text>
    </g>

    <!-- Mode 3: Top and Bottom Wrap -->
    <g transform="translate(20, 215)">
      <rect width="180" height="155" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="90" y="20" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. Top &amp; Bottom</text>
      
      <line x1="15" y1="36" x2="165" y2="36" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="48" x2="165" y2="48" stroke="#94a3b8" stroke-width="2"/>
      
      <!-- Full-Width Banner Image -->
      <rect x="25" y="58" width="130" height="42" rx="3" fill="#d97706"/>
      <text x="90" y="83" font-size="8.5" fill="#ffffff" text-anchor="middle">Banner Image</text>
      
      <line x1="15" y1="112" x2="165" y2="112" stroke="#94a3b8" stroke-width="2"/>
      <line x1="15" y1="124" x2="165" y2="124" stroke="#94a3b8" stroke-width="2"/>
      
      <text x="90" y="144" font-size="8" fill="#cbd5e1" text-anchor="middle">Blocks text on left and right</text>
    </g>

    <!-- Mode 4: Behind Text / WordArt Layering -->
    <g transform="translate(220, 215)">
      <rect width="180" height="155" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="90" y="20" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">4. Behind Text / WordArt</text>
      
      <!-- Watermark Background Shape -->
      <circle cx="90" cy="75" r="35" fill="#7c3aed" opacity="0.35"/>
      <text x="90" y="80" font-size="11" font-weight="bold" fill="#e9d5ff" text-anchor="middle">WATERMARK</text>
      
      <!-- Foreground Text Running Directly Over -->
      <line x1="15" y1="48" x2="165" y2="48" stroke="#ffffff" stroke-width="2"/>
      <line x1="15" y1="62" x2="165" y2="62" stroke="#ffffff" stroke-width="2"/>
      <line x1="15" y1="76" x2="165" y2="76" stroke="#ffffff" stroke-width="2"/>
      <line x1="15" y1="90" x2="165" y2="90" stroke="#ffffff" stroke-width="2"/>
      <line x1="15" y1="104" x2="165" y2="104" stroke="#ffffff" stroke-width="2"/>
      
      <text x="90" y="144" font-size="8" fill="#cbd5e1" text-anchor="middle">Used for subtle decorative fills</text>
    </g>
  </g>
</svg>
""")

SVG_CRAP_DESIGN_PRINCIPLES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The C.R.A.P. Design Principles &amp; Typographic Spacing</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Foundational layout science: Contrast, Repetition, Alignment, Proximity + Typographic Spacing</text>

  <!-- Principle 1: Contrast -->
  <g transform="translate(45, 90)">
    <rect width="205" height="215" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8"/>
    <rect width="205" height="30" rx="8" fill="#0284c7"/>
    <text x="102" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C — CONTRAST</text>
    
    <text x="12" y="48" font-size="10.5" font-weight="bold" fill="#38bdf8">• Purpose:</text>
    <text x="12" y="64" font-size="8.5" fill="#cbd5e1">Creates an unmistakable focal point so eyes know where to look first.</text>
    
    <!-- Visual Example -->
    <rect x="12" y="85" width="180" height="75" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="102" y="112" font-size="14" font-weight="900" fill="#38bdf8" text-anchor="middle">BIG BOLD TITLE</text>
    <text x="102" y="130" font-size="8" fill="#94a3b8" text-anchor="middle">Small, neutral body text contrast</text>
    <text x="102" y="146" font-size="7.5" fill="#64748b" text-anchor="middle">Dark background vs Bright text</text>

    <text x="12" y="178" font-size="8" font-weight="bold" fill="#38bdf8">Rule: Avoid timid subtle differences!</text>
    <text x="12" y="196" font-size="7.5" fill="#cbd5e1">Make contrast bold (Size, Weight, Color).</text>
  </g>

  <!-- Principle 2: Repetition -->
  <g transform="translate(265, 90)">
    <rect width="205" height="215" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
    <rect width="205" height="30" rx="8" fill="#059669"/>
    <text x="102" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">R — REPETITION</text>
    
    <text x="12" y="48" font-size="10.5" font-weight="bold" fill="#34d399">• Purpose:</text>
    <text x="12" y="64" font-size="8.5" fill="#cbd5e1">Unifies the entire document by repeating visual themes and styles.</text>
    
    <!-- Visual Example -->
    <rect x="12" y="85" width="180" height="75" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <rect x="20" y="95" width="165" height="12" rx="2" fill="#059669"/>
    <text x="102" y="104" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Header 1: Section Theme</text>
    <rect x="20" y="115" width="165" height="12" rx="2" fill="#059669"/>
    <text x="102" y="124" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Header 2: Same Styling</text>
    <circle cx="28" cy="144" r="3" fill="#34d399"/>
    <circle cx="85" cy="144" r="3" fill="#34d399"/>
    <circle cx="145" cy="144" r="3" fill="#34d399"/>

    <text x="12" y="178" font-size="8" font-weight="bold" fill="#34d399">Rule: Limit to 2 matching font families!</text>
    <text x="12" y="196" font-size="7.5" fill="#cbd5e1">Use consistent 3-color palette throughout.</text>
  </g>

  <!-- Principle 3: Alignment -->
  <g transform="translate(485, 90)">
    <rect width="205" height="215" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="205" height="30" rx="8" fill="#d97706"/>
    <text x="102" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">A — ALIGNMENT</text>
    
    <text x="12" y="48" font-size="10.5" font-weight="bold" fill="#fbbf24">• Purpose:</text>
    <text x="12" y="64" font-size="8.5" fill="#cbd5e1">Every item must connect visually with another item via invisible grid lines.</text>
    
    <!-- Visual Example -->
    <rect x="12" y="85" width="180" height="75" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <!-- Alignment Grid Line -->
    <line x1="30" y1="92" x2="30" y2="152" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>
    <text x="35" y="106" font-size="8" font-weight="bold" fill="#ffffff">Headline Left Aligned</text>
    <line x1="35" y1="116" x2="165" y2="116" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="35" y1="126" x2="165" y2="126" stroke="#94a3b8" stroke-width="1.5"/>
    <rect x="35" y="134" width="70" height="15" rx="2" fill="#d97706"/>
    <text x="70" y="144" font-size="7" fill="#ffffff" text-anchor="middle">Button Aligned</text>

    <text x="12" y="178" font-size="8" font-weight="bold" fill="#fbbf24">Rule: Avoid arbitrary unaligned boxes!</text>
    <text x="12" y="196" font-size="7.5" fill="#cbd5e1">Always snap frames to Column Guides.</text>
  </g>

  <!-- Principle 4: Proximity -->
  <g transform="translate(705, 90)">
    <rect width="205" height="215" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.8"/>
    <rect width="205" height="30" rx="8" fill="#7e22ce"/>
    <text x="102" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">P — PROXIMITY</text>
    
    <text x="12" y="48" font-size="10.5" font-weight="bold" fill="#c084fc">• Purpose:</text>
    <text x="12" y="64" font-size="8.5" fill="#cbd5e1">Groups related elements close together to form clear semantic units.</text>
    
    <!-- Visual Example -->
    <rect x="12" y="85" width="180" height="75" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <!-- Group A -->
    <rect x="18" y="92" width="168" height="26" rx="3" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="24" y="103" font-size="7.5" font-weight="bold" fill="#c084fc">Article Title + Byline</text>
    <text x="24" y="113" font-size="6.5" fill="#cbd5e1">Author: Joyce Mwangi | June 2026</text>
    
    <!-- White Space Gap -->
    <!-- Group B -->
    <rect x="18" y="125" width="168" height="26" rx="3" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="24" y="136" font-size="7.5" font-weight="bold" fill="#c084fc">Next Unrelated Section</text>
    <text x="24" y="146" font-size="6.5" fill="#cbd5e1">Separated by clean white space</text>

    <text x="12" y="178" font-size="8" font-weight="bold" fill="#c084fc">Rule: Embrace White Space!</text>
    <text x="12" y="196" font-size="7.5" fill="#cbd5e1">Empty space gives layout breathing room.</text>
  </g>

  <!-- Bottom Section: Typographic Spacing Fine-Tuning -->
  <g transform="translate(45, 320)">
    <rect width="865" height="160" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect width="865" height="28" rx="8" fill="#1e293b"/>
    <text x="432" y="19" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">TYPOGRAPHIC SPACING ANATOMY &amp; MECHANICS</text>
    
    <!-- Kerning Sub-Card -->
    <g transform="translate(20, 38)">
      <rect width="255" height="110" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="1"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#38bdf8">1. KERNING (Character Pair)</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">• Selective adjustment between 2 letters.</text>
      <text x="15" y="52" font-size="8.5" fill="#cbd5e1">• Fixes awkward optical gaps (e.g. AV, To, WA).</text>
      
      <!-- Visual Demonstration -->
      <rect x="15" y="62" width="225" height="38" rx="4" fill="#0f172a"/>
      <text x="40" y="86" font-size="16" font-weight="bold" fill="#ef4444">A<tspan dx="10">V</tspan></text>
      <text x="75" y="86" font-size="8" fill="#ef4444">(Unkerned Gap)</text>
      <text x="155" y="86" font-size="16" font-weight="bold" fill="#34d399">AV</text>
      <text x="180" y="86" font-size="8" fill="#34d399">(Kerned Pair)</text>
    </g>

    <!-- Tracking Sub-Card -->
    <g transform="translate(305, 38)">
      <rect width="255" height="110" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#34d399">2. TRACKING (Uniform Line)</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">• Uniform spacing across a whole word/line.</text>
      <text x="15" y="52" font-size="8.5" fill="#cbd5e1">• Used for elegant all-caps titles &amp; subtitles.</text>
      
      <!-- Visual Demonstration -->
      <rect x="15" y="62" width="225" height="38" rx="4" fill="#0f172a"/>
      <text x="25" y="84" font-size="10" font-weight="bold" letter-spacing="4" fill="#34d399">N E W S L E T T E R</text>
      <text x="180" y="84" font-size="8" fill="#94a3b8">(Loose)</text>
    </g>

    <!-- Leading Sub-Card -->
    <g transform="translate(590, 38)">
      <rect width="255" height="110" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#fbbf24">3. LEADING (Line Spacing)</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">• Vertical distance between text baselines.</text>
      <text x="15" y="52" font-size="8.5" fill="#cbd5e1">• Standard rule: 120% to 140% of font size.</text>
      
      <!-- Visual Demonstration -->
      <rect x="15" y="62" width="225" height="38" rx="4" fill="#0f172a"/>
      <text x="20" y="76" font-size="9" fill="#cbd5e1">Baseline 1: Senior Secondary ICT</text>
      <line x1="20" y1="78" x2="190" y2="78" stroke="#f59e0b" stroke-width="1"/>
      <text x="20" y="93" font-size="9" fill="#cbd5e1">Baseline 2: Editorial Page Layout</text>
      <line x1="20" y1="95" x2="190" y2="95" stroke="#f59e0b" stroke-width="1"/>
    </g>
  </g>
</svg>
""")

SVG_DOCUMENT_SETUP_BLEED = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Document Setup Anatomy: Bleed, Trim, Margins &amp; Master Pages</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Print production boundary geometry and background Master Page structural layering</text>

  <!-- Left Side: Print Production Boundary Geometry -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#0284c7"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">PRINT GEOMETRY: BLEED, TRIM &amp; SAFE MARGINS</text>

    <!-- Visual Diagram of Concentric Print Zones -->
    <g transform="translate(25, 50)">
      <!-- Outer Slug Area (Grey) -->
      <rect width="370" height="230" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
      <text x="185" y="16" font-size="8" fill="#94a3b8" text-anchor="middle">SLUG AREA (Printer Crop &amp; Registration Marks)</text>

      <!-- Crop Marks at 4 Corners -->
      <line x1="20" y1="10" x2="20" y2="25" stroke="#ffffff" stroke-width="1"/>
      <line x1="10" y1="25" x2="25" y2="25" stroke="#ffffff" stroke-width="1"/>
      <line x1="350" y1="10" x2="350" y2="25" stroke="#ffffff" stroke-width="1"/>
      <line x1="345" y1="25" x2="360" y2="25" stroke="#ffffff" stroke-width="1"/>
      <line x1="20" y1="205" x2="20" y2="220" stroke="#ffffff" stroke-width="1"/>
      <line x1="10" y1="205" x2="25" y2="205" stroke="#ffffff" stroke-width="1"/>
      <line x1="350" y1="205" x2="350" y2="220" stroke="#ffffff" stroke-width="1"/>
      <line x1="345" y1="205" x2="360" y2="205" stroke="#ffffff" stroke-width="1"/>

      <!-- 1. Bleed Area (Red dashed line +3mm outside trim) -->
      <rect x="25" y="25" width="320" height="180" fill="#fee2e2" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3"/>
      <text x="35" y="40" font-size="8" font-weight="bold" fill="#b91c1c">BLEED LINE (+3mm Outer Extension)</text>

      <!-- 2. Trim Line (Black solid: Exact physical page cut, e.g. A4 210x297mm) -->
      <rect x="40" y="40" width="290" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
      <text x="50" y="55" font-size="8.5" font-weight="bold" fill="#0f172a">TRIM LINE (Physical Cutting Blade)</text>

      <!-- 3. Safe Margin Zone (Blue dotted line 15mm inside trim) -->
      <rect x="60" y="60" width="250" height="110" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3,3"/>
      <text x="185" y="80" font-size="9" font-weight="bold" fill="#0369a1" text-anchor="middle">SAFE MARGIN ZONE (Live Content Area)</text>
      
      <text x="185" y="105" font-size="8" fill="#334155" text-anchor="middle">Keep all text, logos, and tables INSIDE this zone!</text>
      <text x="185" y="125" font-size="7.5" fill="#64748b" text-anchor="middle">Prevents text from being cut off if paper shifts in guillotine.</text>
      
      <!-- Full Bleed Background Example -->
      <rect x="25" y="140" width="130" height="65" fill="#0284c7" opacity="0.8"/>
      <text x="80" y="175" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">Full-Bleed Graphic</text>
    </g>

    <!-- Bottom Legend -->
    <g transform="translate(20, 295)">
      <rect width="380" height="80" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="20" font-size="9.5" font-weight="bold" fill="#ef4444">• Bleed (+3mm):</text>
      <text x="110" y="20" font-size="8.5" fill="#cbd5e1">Prevents white slivers when trimming color pages.</text>
      
      <text x="15" y="42" font-size="9.5" font-weight="bold" fill="#ffffff">• Trim Line:</text>
      <text x="110" y="42" font-size="8.5" fill="#cbd5e1">The exact dimensions of the finished cut publication.</text>
      
      <text x="15" y="64" font-size="9.5" font-weight="bold" fill="#38bdf8">• Safe Margin:</text>
      <text x="110" y="64" font-size="8.5" fill="#cbd5e1">12mm - 15mm cushion protecting essential editorial text.</text>
    </g>
  </g>

  <!-- Right Side: Master Page Architecture (Dual Layering) -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="36" rx="8" fill="#059669"/>
    <text x="210" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">MASTER PAGE INHERITANCE ARCHITECTURE</text>

    <!-- Isometric Layer Stack Simulation -->
    <g transform="translate(20, 50)">
      <!-- Background Layer (Master Page A) -->
      <rect x="40" y="110" width="320" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
      <rect x="40" y="110" width="320" height="22" rx="6" fill="#059669"/>
      <text x="200" y="125" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">LAYER 1: MASTER PAGE TEMPLATE (Locked Background)</text>
      
      <!-- Repeating Elements on Master -->
      <rect x="55" y="138" width="290" height="8" rx="2" fill="#34d399"/>
      <text x="60" y="160" font-size="8" fill="#a7f3d0">• Top Running Header Stripe: "Senior ICT Term 3"</text>
      <text x="60" y="178" font-size="8" fill="#a7f3d0">• School Logo in Left Margin Grid</text>
      <text x="60" y="196" font-size="8" font-weight="bold" fill="#fbbf24">• Dynamic Pagination Tag: [Page #]</text>

      <!-- Upward Projection Dotted Arrows -->
      <path d="M 100 110 L 100 75" stroke="#34d399" stroke-width="2" stroke-dasharray="3,2"/>
      <polygon points="100,68 95,76 105,76" fill="#34d399"/>
      <path d="M 300 110 L 300 75" stroke="#34d399" stroke-width="2" stroke-dasharray="3,2"/>
      <polygon points="300,68 295,76 305,76" fill="#34d399"/>

      <!-- Foreground Layer (Active Page 3) -->
      <rect x="40" y="0" width="320" height="65" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <rect x="40" y="0" width="320" height="20" rx="6" fill="#0284c7"/>
      <text x="200" y="14" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">LAYER 2: ACTIVE FOREGROUND (Editable Article Content)</text>
      <text x="55" y="36" font-size="8" fill="#cbd5e1">• Unique Article Story: "Robotics in Kenyan Agriculture"</text>
      <text x="55" y="50" font-size="8" fill="#cbd5e1">• Unique Photographs &amp; Specific Callout Boxes</text>
    </g>

    <!-- Master Page Operational Rules -->
    <g transform="translate(20, 275)">
      <rect width="380" height="100" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#34d399">Master Page Global Rules:</text>
      <text x="15" y="40" font-size="8.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">One Change Updates All:</tspan> Editing Master updates 50+ linked pages instantly.</text>
      <text x="15" y="58" font-size="8.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Foreground Lock:</tspan> Background master items cannot be clicked or shifted by accident.</text>
      <text x="15" y="76" font-size="8.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Cover Page Exception:</tspan> Apply 'Master: None' to suppress headers on front cover.</text>
      <text x="15" y="92" font-size="8" fill="#94a3b8">Save master structures as Templates (.pubt / .sct) for recurring publications.</text>
    </g>
  </g>
</svg>
""")

SVG_PREFLIGHT_PRINT_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Preflight Quality Control, Mail Merge &amp; Multi-Channel Export</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Pre-press diagnostic auditing, automated database personalization, and multi-channel publication pipelines</text>

  <!-- Section 1: Preflight Diagnostic Audit (Left) -->
  <g transform="translate(45, 90)">
    <rect width="260" height="390" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="260" height="34" rx="8" fill="#b91c1c"/>
    <text x="130" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. PREFLIGHT AUDIT</text>
    
    <!-- Audit Check 1: DPI Resolution -->
    <rect x="15" y="48" width="230" height="70" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="25" y="68" font-size="10" font-weight="bold" fill="#f87171">Image Density (DPI Check)</text>
    <text x="25" y="85" font-size="8.5" fill="#cbd5e1">• Web 72-96 DPI: <tspan fill="#ef4444">Pixelated Reject</tspan></text>
    <text x="25" y="100" font-size="8.5" fill="#cbd5e1">• Print 300 DPI: <tspan fill="#34d399">Crystal Clear Pass</tspan></text>
    
    <!-- Audit Check 2: Color Space Conversion -->
    <rect x="15" y="128" width="230" height="70" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="25" y="148" font-size="10" font-weight="bold" fill="#fbbf24">Color Space (RGB vs CMYK)</text>
    <text x="25" y="165" font-size="8.5" fill="#cbd5e1">• RGB: Screen light (3 channels)</text>
    <text x="25" y="180" font-size="8.5" fill="#cbd5e1">• CMYK: 4-color press ink separation</text>

    <!-- Audit Check 3: Font Embedding & Overset -->
    <rect x="15" y="208" width="230" height="75" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="25" y="228" font-size="10" font-weight="bold" fill="#38bdf8">Font Packaging &amp; Overset</text>
    <text x="25" y="245" font-size="8.5" fill="#cbd5e1">• Embed OpenType font subsets</text>
    <text x="25" y="260" font-size="8.5" fill="#cbd5e1">• Resolve [+] red text overflows</text>

    <rect x="15" y="295" width="230" height="75" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="130" y="318" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Preflight Verdict</text>
    <text x="130" y="338" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Zero missing links, zero low-res photos</text>
    <text x="130" y="355" font-size="8" fill="#94a3b8" text-anchor="middle">Ready for press compilation</text>
  </g>

  <!-- Section 2: Mail Merge Personalization Engine (Center) -->
  <g transform="translate(325, 90)">
    <rect width="290" height="390" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="290" height="34" rx="8" fill="#d97706"/>
    <text x="145" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MAIL MERGE ENGINE</text>

    <!-- Node A: Excel Data Source -->
    <g transform="translate(15, 48)">
      <rect width="260" height="75" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="20" font-size="9.5" font-weight="bold" fill="#34d399">DATA SOURCE (Spreadsheet Table):</text>
      <rect x="15" y="28" width="230" height="15" fill="#065f46"/>
      <text x="20" y="39" font-size="7.5" font-weight="bold" fill="#ffffff">First_Name | County_Group | Seat_No</text>
      <text x="20" y="54" font-size="7" fill="#cbd5e1">1. Grace Mwangi | Nakuru Youth | A12</text>
      <text x="20" y="65" font-size="7" fill="#cbd5e1">2. John Ombati  | Kisii Farmers | B05</text>
    </g>

    <!-- Downward Arrow to Template -->
    <path d="M 145 128 L 145 145" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="145,152 140,143 150,143" fill="#f59e0b"/>

    <!-- Node B: Master Layout with Placeholder Tags -->
    <g transform="translate(15, 155)">
      <rect width="260" height="85" rx="6" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
      <text x="15" y="20" font-size="9.5" font-weight="bold" fill="#38bdf8">MASTER LAYOUT WITH TOKENS:</text>
      <rect x="15" y="28" width="230" height="48" rx="3" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
      <text x="22" y="44" font-size="8" fill="#ffffff">Dear &lt;&lt;First_Name&gt;&gt;,</text>
      <text x="22" y="58" font-size="7.5" fill="#cbd5e1">Welcome &lt;&lt;County_Group&gt;&gt; to Seat &lt;&lt;Seat_No&gt;&gt;.</text>
      <text x="22" y="70" font-size="6.5" fill="#94a3b8">(Wide cushion space prevents long name wrap)</text>
    </g>

    <!-- Downward Arrow to Merged Output -->
    <path d="M 145 245 L 145 262" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="145,269 140,260 150,260" fill="#f59e0b"/>

    <!-- Node C: Batch Merged Output -->
    <g transform="translate(15, 272)">
      <rect width="260" height="98" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="15" y="20" font-size="9.5" font-weight="bold" fill="#34d399">MERGED OUTPUT (100+ Custom Cards):</text>
      <rect x="15" y="28" width="230" height="28" rx="2" fill="#0f172a"/>
      <text x="22" y="42" font-size="7.5" font-weight="bold" fill="#38bdf8">Card 1: Dear Grace Mwangi (Seat A12)</text>
      <rect x="15" y="60" width="230" height="28" rx="2" fill="#0f172a"/>
      <text x="22" y="74" font-size="7.5" font-weight="bold" fill="#38bdf8">Card 2: Dear John Ombati (Seat B05)</text>
    </g>
  </g>

  <!-- Section 3: Dual Multi-Channel Output (Right) -->
  <g transform="translate(635, 90)">
    <rect width="280" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="280" height="34" rx="8" fill="#059669"/>
    <text x="140" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. OUTPUT PIPELINE</text>

    <!-- Channel A: Commercial Offset Print -->
    <g transform="translate(15, 48)">
      <rect width="250" height="145" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="250" height="24" rx="6" fill="#0284c7"/>
      <text x="125" y="16" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">CHANNEL A: COMMERCIAL PRINT</text>
      
      <text x="15" y="42" font-size="9" font-weight="bold" fill="#38bdf8">• Format: PDF/X-1a (Press Quality)</text>
      <text x="15" y="58" font-size="8" fill="#cbd5e1">• 300 DPI CMYK color separation plates</text>
      <text x="15" y="74" font-size="8" fill="#cbd5e1">• Crop marks &amp; 3mm bleed included</text>
      <text x="15" y="90" font-size="8" fill="#cbd5e1">• Imposition: Printer spreads (booklet)</text>
      
      <rect x="15" y="105" width="220" height="28" rx="4" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
      <text x="125" y="122" font-size="8" fill="#38bdf8" text-anchor="middle">Target: Industrial Offset &amp; Digital Presses</text>
    </g>

    <!-- Channel B: Digital & Mobile Web -->
    <g transform="translate(15, 210)">
      <rect width="250" height="160" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
      <rect width="250" height="24" rx="6" fill="#7e22ce"/>
      <text x="125" y="16" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">CHANNEL B: DIGITAL &amp; MOBILE WEB</text>
      
      <text x="15" y="42" font-size="9" font-weight="bold" fill="#c084fc">• Format: Interactive PDF / ePub / Web</text>
      <text x="15" y="58" font-size="8" fill="#cbd5e1">• RGB color profile (vibrant on OLED/LCD)</text>
      <text x="15" y="74" font-size="8" fill="#cbd5e1">• Compressed file size for fast download</text>
      <text x="15" y="90" font-size="8" fill="#cbd5e1">• Live hyperlinks, video embeds &amp; forms</text>
      <text x="15" y="106" font-size="8" fill="#cbd5e1">• Responsive single-column scroll mode</text>
      
      <rect x="15" y="120" width="220" height="28" rx="4" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
      <text x="125" y="137" font-size="8" fill="#c084fc" text-anchor="middle">Target: Smartphones, Tablets, Portals</text>
    </g>
  </g>
</svg>
""")


# =====================================================================
# FULL STRUCTURED 6-LESSON DATASET FOR TOPIC 6: DESKTOP PUBLISHING
# =====================================================================

TOPIC_6_LESSONS = [
    # =========================================================================
    # LESSON 6.1.1: Meaning, Importance, and Categories of DTP Tools
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning, Importance, and Categories of DTP Tools",
        "unit_description": "Foundations of desktop publishing (DTP), comparison between content-driven word processing and layout-driven DTP, categories of DTP software (proprietary vs. open-source vs. cloud-native), and selection criteria.",
        "lesson_title": "Meaning, Importance, and Categories of DTP Tools",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "From Mechanical Typesetting to Modern Desktop Publishing Workstations",
                    "content": {
                        "title": "Evolution of Publication Design",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "A modern desktop publishing workstation featuring multi-column page spreads, vector layout tools, and color calibration displays used to design publication-grade media.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Power of Pixel-Perfect Visual Communication",
                    "content": {
                        "text": "Take a look at a glossy fashion magazine, a three-fold banking brochure, or a vibrant school sports poster. Have you ever tried creating a multi-column document with side-by-side images in a standard word processor? If you have, you know how frustrating it is: you insert a single picture, and suddenly all your text jumps to random places, ruining your entire layout!\n\nStandard word processors are **content-driven**—they are designed for typing continuous paragraphs where text flows like water from page to page. In contrast, **Desktop Publishing (DTP)** software is **layout-driven**. It treats the screen as an open architectural drafting board where every block of text, photograph, decorative shape, or logo lives in its own independent, movable frame with exact spatial coordinates."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define Desktop Publishing (DTP) using both functional and technical perspectives\n- Contrast content-driven word processing with layout-driven desktop publishing across page geometry, text flow, and object positioning\n- Categorize DTP software applications into proprietary/commercial, open-source, and cloud-native platforms\n- Evaluate strategic selection criteria (budget, learning curve, hardware specifications, team collaboration) when choosing DTP software for school, business, and community projects"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Desktop Publishing (DTP)",
                    "content": {
                        "term": "Desktop Publishing (DTP)",
                        "definition": "The use of specialized computer software to assemble text, graphics, and decorative elements into visually structured, print-ready or digital multi-page publications.",
                        "simple": "Designing professional page layouts (like magazines, brochures, flyers, and certificates) where every text box and picture can be positioned anywhere on the page without shifting other items.",
                        "technical": "A layout-centric software architecture that decouples textual content from page geometry, using independent coordinate-based frames (X/Y axis), vector geometry, typographic control, color separations, and prepress standards.",
                        "example": "Using Microsoft Publisher or Scribus to design a three-fold brochure with columns, background shapes, and text wrapping."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Core Architectural Differences & DTP Software Categories",
                    "content": {
                        "text": "Understanding when to use a word processor versus a desktop publisher is a critical ICT skill:\n\n1. **Word Processors (Content-Driven):**\n   - Built for typing long, continuous linear text (essays, novels, business letters).\n   - Text automatically flows from one page to the next when the margin boundary is reached.\n   - Inserting an image displaces surrounding text downward.\n\n2. **Desktop Publishers (Layout-Driven):**\n   - Built for precise spatial design (flyers, brochures, newspapers, certificates, catalogues).\n   - Text cannot simply be typed onto a blank page; it must be housed inside an explicit **Text Frame**.\n   - If text exceeds frame boundaries, it does not auto-spill onto a new page; it enters an **overset memory buffer** until linked to another frame.\n\n### The Three Major Software Categories:\n\n- **Proprietary Commercial Suites (e.g., Adobe InDesign, Microsoft Publisher, Affinity Publisher):** Industry-standard applications offering advanced prepress tools, CMYK color separation, and spot color management. Microsoft Publisher is intuitive with a familiar ribbon interface, while Adobe InDesign requires paid subscriptions.\n- **Open-Source Free Suites (e.g., Scribus, LibreOffice Draw):** Free, community-developed software released under the GPL license. Scribus offers professional CMYK and PDF/X preflight capabilities with zero licensing fees, making it ideal for budget-constrained schools and small businesses.\n- **Cloud-Native Collaborative Suites (e.g., Canva, Figma):** Browser-based design platforms enabling real-time remote team collaboration, thousands of pre-made templates, and instant cloud sharing."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Word Processor vs. Desktop Publisher Architecture",
                    "content": {
                        "title": "Comparative Architectural Layout: Content Flow vs Frame Control",
                        "caption": "High-precision vector diagram contrasting linear content-driven document flow with frame-based spatial layout design and coordinate positioning.",
                        "svg_content": SVG_DTP_VS_WORD_PROCESSING
                    }
                },
                {
                    "type": "step_process",
                    "title": "Systematic Framework for Selecting DTP Applications",
                    "content": {
                        "intro": "When selecting desktop publishing software for an educational institution, print bureau, or marketing firm, evaluate these four decision factors:",
                        "steps": [
                            {"title": "1. Assess Budget & Licensing Model", "description": "Determine if the organization can sustain monthly cloud subscriptions (Adobe Creative Cloud), prefer a one-time perpetual license (Affinity Publisher), or require zero-cost open-source tools (Scribus)."},
                            {"title": "2. Evaluate Hardware & Operating System Constraints", "description": "Verify workstation hardware specifications. Professional tools require modern multi-core processors and at least 8 GB to 16 GB of RAM, whereas open-source Scribus runs smoothly on basic legacy PCs."},
                            {"title": "3. Identify Production Target & Prepress Requirements", "description": "For high-volume commercial offset printing requiring CMYK plates and spot-color trapping, choose InDesign or Scribus. For simple classroom handouts, Microsoft Publisher or Canva is sufficient."},
                            {"title": "4. Assess Team Collaboration & Connectivity", "description": "If multiple remote designers must edit the same marketing poster simultaneously across locations, cloud-native collaborative tools like Canva or Figma provide real-time co-authoring."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Community Cooperative Publishing in Kenya",
                    "content": {
                        "scenario": "A dairy farmers' cooperative in Eldoret needs to produce monthly member newsletters, cattle feed advisory brochures, and milk delivery payment vouchers for 1,500 local farmers.",
                        "impact": "Initially, the cooperative staff tried designing three-fold brochures in simple word processors. Whenever they inserted livestock photos, column alignments shattered, text shifted unpredictably between computers, and printing shops rejected the raw files.",
                        "solution": "Deploying open-source DTP software (Scribus) allowed the cooperative to set up permanent three-column fold templates with locked image frames, professional margins, and direct PDF/X exports without paying expensive software subscription fees."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Word Processors and DTP Software are Interchangeable",
                    "content": {
                        "misconception": "A modern word processor like Microsoft Word can replace professional DTP software for any graphic design or publication task.",
                        "correction": "While word processors include basic drawing and shape tools, their core engine remains linear and flow-based. DTP applications provide frame-based spatial independence, master page templates, spot/CMYK color calibration, bleed margins, and preflight print diagnostic tools essential for professional publication."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The Overset Text Disappearance",
                    "content": {
                        "mistake": "Pasting a long news article into a DTP text box and assuming the remaining paragraphs were deleted because they did not appear on page 2.",
                        "why_it_happens": "Unlike word processors which spawn new pages automatically, DTP text boxes hold excess text in an 'overset' memory buffer indicated by a small red overflow icon [+] on the frame handle.",
                        "fix_solution": "Draw a second text frame on page 2, click the Link Text Frames tool on frame 1, and click inside frame 2 to allow the text to flow across pages seamlessly."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: DTP vs Word Processing Core Distinction",
                    "content": {
                        "question": "Which of the following describes the fundamental structural difference between desktop publishing software and word processing software?",
                        "options": [
                            "Word processors require dedicated graphics cards, while DTP tools do not use computer memory",
                            "Word processors are content-driven with linear text flow, while DTP tools are layout-driven with frame-based coordinate control",
                            "DTP tools strictly forbid the insertion of photographic images or decorative shapes",
                            "Word processors automatically generate CMYK color separation plates for commercial printing presses"
                        ],
                        "correct": "B",
                        "explanation": "Word processors manage linear text that flows continuously down pages, whereas DTP applications organize content into independent, movable frames placed at exact X/Y coordinates."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Software Category Selection",
                    "content": {
                        "question": "A rural school in Machakos with limited internet connectivity and older computer hardware wants to teach professional brochure design. Which DTP software category is most appropriate?",
                        "options": [
                            "Cloud-only subscription tools requiring constant high-speed broadband",
                            "Open-source offline DTP software (such as Scribus) that runs locally with zero licensing cost",
                            "Plain text editors like Windows Notepad",
                            "Online video rendering suites"
                        ],
                        "correct": "B",
                        "explanation": "Open-source tools like Scribus run locally without internet connections, operate efficiently on modest hardware, and require zero license fees, making them ideal for budget-constrained schools."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Introduction to Desktop Publishing & Layout Concepts",
                    "content": {
                        "title": "Desktop Publishing Fundamentals & Tool Selection",
                        "youtube_id": "Vb0y_1bQv3E",
                        "url": "https://www.youtube.com/watch?v=Vb0y_1bQv3E",
                        "description": "Comprehensive tutorial introducing desktop publishing concepts, comparing layout-driven tools with word processors, and exploring DTP software categories."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **DTP Defined:** The specialized digital process of combining typography, graphics, and layout geometry into print-ready or digital multi-page publications.\n2. **Frame-Based Architecture:** Unlike linear word processors, DTP applications place all text and images inside independent, coordinate-positioned frames.\n3. **Software Categories:** Options range from proprietary industry standards (InDesign, MS Publisher) to free open-source suites (Scribus) and cloud-native collaborative tools (Canva).\n4. **Selection Factors:** Match software choices to organizational budget, workstation hardware, internet connectivity, and the complexity of the final printing target."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6.1.2: Interface, Navigation, and Basic File Operations
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Interface, Navigation, and Basic File Operations",
        "unit_description": "Mastering the DTP workspace anatomy: canvas, scratch area, horizontal/vertical rulers, margin/column guides, zoom navigation, and managing native editable vs portable export file formats.",
        "lesson_title": "Interface, Navigation, and Basic File Operations",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "The Modern DTP Workspace Anatomy",
                    "content": {
                        "title": "Digital Layout Drafting Workspace",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Computer_classroom_in_Kenya.jpg",
                        "caption": "Students interacting with desktop publishing software, setting ruler guides, organizing document layers, and navigating multi-page spreads.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Digital Drafting Board",
                    "content": {
                        "text": "When you open a desktop publishing application like Microsoft Publisher or Scribus, the workspace feels like an architect's drafting table. Instead of a single white sheet filling your entire display, you see a central page canvas surrounded by an expansive grey staging zone called the **scratch area** (or pasteboard).\n\nIn DTP, precision is paramount. If a column guide is misaligned by even 1 millimeter, an entire three-fold brochure will fold unevenly when printed! Mastering the interface tools—horizontal and vertical rulers, magnetic snapping guides, navigation thumbnails, and zoom controls—is the essential foundation for creating publication-grade media."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify core DTP workspace components: Page Canvas, Scratch Area, Rulers, Layout Guides, and Navigation Pane\n- Configure margin guides, column guides, and ruler guides for precise layout alignment\n- Utilize magnetic snapping and zoom controls to stage assets accurately\n- Contrast native editable project file formats (.pub, .sla) with universal distribution formats (.pdf)\n- Establish structured project directory folders to manage linked image assets safely"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Scratch Area & Layout Guides",
                    "content": {
                        "term": "Scratch Area (Pasteboard)",
                        "definition": "The non-printing staging workspace surrounding the active page canvas in a desktop publishing application.",
                        "simple": "A virtual workbench around your page where you can place extra photos, text boxes, and logos while deciding where to put them, without them appearing on the final printed page.",
                        "technical": "An off-canvas coordinate memory space that preserves unassigned objects and temporary layout assets across multi-page document navigation.",
                        "example": "Placing three draft logos in the scratch area while testing which one fits best in a newsletter banner."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Interface Anatomy & File Management Strategy",
                    "content": {
                        "text": "A professional DTP interface comprises five integrated subsystems:\n\n1. **The Page Canvas:** The defined physical boundary of the document (e.g., A4 210 x 297 mm) that represents the printed sheet.\n2. **The Scratch Area (Pasteboard):** The non-printing grey perimeter used as a holding desk for staging images, alternative headlines, and color palettes.\n3. **Rulers & Hairline Trackers:** Calibrated in millimeters, centimeters, or inches along the top and left axes. As you move the mouse, dynamic hairline marks follow your cursor to indicate exact coordinates.\n4. **Layout & Snap Guides:** Non-printing colored lines (blue margin guides, pink column guides, green custom ruler guides). When **Snap to Guides** is activated, objects magnetically pull to the guide when dragged within 2 mm.\n5. **Page Navigation Pane:** A vertical sidebar displaying live thumbnail previews of every page in the document for instant jumping.\n\n### Dual-Format File Management Rule:\n\n- **Native Project Files (`.pub`, `.sla`, `.indd`):** Retain all individual layers, linked high-resolution graphics, text frames, and scratch area items. Always save your working master file in this format.\n- **Portable Distribution Files (`.pdf`):** Compress graphics, embed fonts permanently, and flatten vector layers so the publication prints identically on any machine worldwide. Never send raw native files to commercial printers without packaging!"
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "DTP Workspace Anatomy & Layout Geometry",
                    "content": {
                        "title": "Visual Schematic of DTP Application Interface",
                        "caption": "High-precision vector schematic displaying the central page canvas, scratch area pasteboard, horizontal/vertical rulers, guide overlays, and navigation sidebar.",
                        "svg_content": SVG_DTP_INTERFACE_ANATOMY
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step: Setting Up a 4-Page Publication & Managing Files",
                    "content": {
                        "intro": "Standard workflow for creating and structuring a multi-page publication:",
                        "steps": [
                            {"title": "1. Launch Application and Define Page Dimensions", "description": "Open Microsoft Publisher or Scribus. Select A4 Portrait (210 x 297 mm) with 15 mm default margins for standard Kenyan commercial print compatibility."},
                            {"title": "2. Insert and Index Additional Pages", "description": "Right-click the Page Navigation sidebar thumbnail, select 'Insert Page', specify 3 additional pages (creating a 4-page booklet), and verify thumbnail order."},
                            {"title": "3. Pull Ruler Guides for Uniform Headings", "description": "Click on the top horizontal ruler, drag downward, and release at the 50 mm mark. This creates a global horizontal guideline for aligning article titles across pages."},
                            {"title": "4. Stage Assets in the Scratch Area", "description": "Create a draft text frame containing the school motto and drag it completely off the white canvas into the grey scratch area for multi-page availability."},
                            {"title": "5. Save Native Master & Export PDF", "description": "Save the master file as 'School_Gazette_2026.pub' in a dedicated project directory. Then click File ➔ Export to generate 'School_Gazette_2026.pdf'."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Commercial Print Bureau Workflow in Nairobi",
                    "content": {
                        "scenario": "An event coordinator in Nairobi designed 500 VIP concert programmes in Microsoft Publisher using customized downloaded fonts and linked photos stored on her desktop.",
                        "impact": "She emailed the raw `.pub` file directly to a commercial printing bureau on River Road. When opened on the bureau computer, missing fonts were automatically replaced with standard system fonts, causing headings to wrap awkwardly and pictures to display 'Missing Image Link' errors.",
                        "solution": "By establishing a dedicated project folder structure with all linked assets and exporting a Press-Quality PDF with embedded font subsets, the bureau printed 500 flawless programmes on time."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Objects in the Scratch Area Will Print",
                    "content": {
                        "misconception": "Leaving text boxes or unused logos in the grey scratch area will cause them to appear on the edge of the printed page or generate printer errors.",
                        "correction": "The scratch area is strictly non-printing. The print engine crops and outputs only elements positioned within the defined page canvas boundaries (and bleed limits). Objects in the scratch area remain safe staging assets for future edits."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Broken Image Links on Project Transfer",
                    "content": {
                        "mistake": "Copying a DTP project file to a flash drive without its accompanying image folder, resulting in red 'X' missing link boxes when opened on another PC.",
                        "why_it_happens": "DTP programs link to high-resolution external images via file path references rather than embedding massive raster data directly into the project file.",
                        "fix_solution": "Always maintain a dedicated project folder with an `/Images` subfolder, or use the application's 'Pack and Go' / 'Collect for Output' tool to bundle the file and all linked assets together."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Purpose of the Scratch Area",
                    "content": {
                        "question": "What is the primary function of the scratch area (pasteboard) in desktop publishing software?",
                        "options": [
                            "To store temporary text and graphics off-canvas without them appearing on the final printed page",
                            "To automatically spell-check foreign language paragraphs",
                            "To permanently delete unwanted vector illustrations from the hard drive",
                            "To calculate numerical formulas in spreadsheet tables"
                        ],
                        "correct": "A",
                        "explanation": "The scratch area is a non-printing virtual workbench surrounding the page canvas where designers stage photos, text frames, and logos before placing them into active layouts."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: File Export Best Practices",
                    "content": {
                        "question": "Why should a finalized brochure always be exported to a PDF file before being sent to an external commercial printing press?",
                        "options": [
                            "PDF files convert all colorful vector graphics into black-and-white drawings",
                            "PDF files lock layout coordinates and embed fonts so the document renders identically on any machine",
                            "PDF files erase all images to reduce printing ink costs",
                            "Commercial printing presses are incapable of reading color documents"
                        ],
                        "correct": "B",
                        "explanation": "Exporting to PDF packages the layout, preserves exact coordinate geometry, and embeds font subsets, ensuring the publication prints exactly as designed without missing font substitutions."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: DTP Interface Navigation & Layout Precision",
                    "content": {
                        "title": "Mastering the DTP Workspace, Rulers, and Guides",
                        "youtube_id": "jYv88e5d0G0",
                        "url": "https://www.youtube.com/watch?v=jYv88e5d0G0",
                        "description": "Step-by-step video guide exploring DTP interface navigation, setting custom ruler guides, managing the scratch area, and exporting print-ready PDFs."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Workspace Anatomy:** The DTP interface combines a central printable page canvas, an off-canvas non-printing scratch area, metric rulers, and navigation thumbnails.\n2. **Layout Precision:** Pulling guides from rulers and enabling 'Snap to Guides' ensures millimeter-level alignment across multi-column spreads.\n3. **Dual File Strategy:** Save working master files in native format (.pub/.sla) to preserve layers, and export to PDF for universal distribution and commercial printing.\n4. **Asset Linking:** Always bundle linked photos within a structured project folder to prevent broken image references when transferring files."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6.1.3: Inserting Shapes, Pictures, and WordArt
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Inserting Shapes, Pictures, and WordArt",
        "unit_description": "Techniques for inserting, formatting, and manipulating vector shapes, bitmap pictures, aspect ratio locking, non-destructive cropping, text wrapping modes, and stylized WordArt.",
        "lesson_title": "Inserting Shapes, Pictures, and WordArt",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Graphic Frames and Visual Storytelling",
                    "content": {
                        "title": "Visual Framing and Asset Arrangement",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "Designers arranging vector background shapes, cropping photographic assets, and applying text wrapping to create visual harmony.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Building Pages with Modular Visual Blocks",
                    "content": {
                        "text": "In desktop publishing, you do not paint with brush strokes; you construct your publication using modular geometric blocks! Inserting solid color shapes establishes background sections, importing pictures brings storytelling to life, and styling key titles with WordArt creates visual punch.\n\nHowever, unmanaged graphics can ruin a design. Have you ever seen a flyer where a person's face was stretched horizontally like a balloon, or an advertisement where text ran directly across a dark photo, making it unreadable? Learning how to lock aspect ratios, crop pictures non-destructively, and configure text wrapping modes ensures your publications communicate cleanly and professionally."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Insert and customize vector shapes (fills, gradients, strokes, drop shadows)\n- Import raster images, scale them proportionately using the Shift-lock rule, and apply non-destructive cropping\n- Differentiate and apply the four primary text wrapping modes: Square, Tight, Top and Bottom, and Behind/In Front\n- Create readable WordArt display headings and manage visual layer stacking orders (Bring to Front, Send Backward)"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Text Wrapping & Aspect Ratio",
                    "content": {
                        "term": "Text Wrapping",
                        "definition": "A DTP formatting feature that determines how body text flows dynamically around intersecting graphic frames, shapes, and image boundaries.",
                        "simple": "Setting rules so that text wraps neatly around pictures, shapes, or logos instead of overlapping or getting hidden beneath them.",
                        "technical": "The spatial boundary collision algorithm that recalculates text frame paragraph line baselines based on the bounding box, alpha mask, or vector contour path of an intersecting graphic frame with configurable standoff cushions.",
                        "example": "Setting a circular school crest to 'Tight' text wrap with a 3mm cushion so article text flows smoothly around its perimeter."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Graphic Manipulation Principles & Text Wrap Modes",
                    "content": {
                        "text": "Mastering graphic assets in DTP requires strict adherence to three geometric rules:\n\n### 1. The Proportional Scaling Rule (Shift-Lock):\n- **Never drag middle handles** (left, right, top, or bottom). Doing so stretches or squashes pixels unevenly, creating distorted, unprofessional graphics.\n- **Always drag corner handles while holding the Shift key** to lock the original aspect ratio (width-to-height ratio).\n\n### 2. Non-Destructive Cropping:\n- Cropping does not erase pixels; it adjusts the outer bounding frame (acting like an adjustable window) to hide unwanted backgrounds or focus on a subject's face.\n\n### 3. The Four Primary Text Wrapping Modes:\n- **Square:** Flows text around the four straight rectangular edges of the graphic bounding box.\n- **Tight (Contour):** Wraps text lines closely around the physical curved contours of transparent PNGs or vector shapes with an adjustable cushion.\n- **Top and Bottom:** Prohibits text on either side, forcing paragraphs to start only above or beneath the graphic (ideal for wide banner charts).\n- **Behind Text / In Front of Text:** Places the graphic on an underlying or overlying layer (used for subtle watermarks or floating promotional badges)."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Graphic Frames, Aspect Ratio & Text Wrap Modes",
                    "content": {
                        "title": "Visual Anatomy of Image Scaling and Text Wrapping Modes",
                        "caption": "Detailed vector diagram showing corner scaling with locked aspect ratio, cropping boundaries, and comparison of Square, Tight, and Top/Bottom text wrapping.",
                        "svg_content": SVG_GRAPHIC_FRAMES_TEXT_WRAP
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step: Constructing a Multi-Asset Promotional Banner",
                    "content": {
                        "intro": "Practical procedure for assembling a layered promotional header banner:",
                        "steps": [
                            {"title": "1. Draw a Background Geometric Shape", "description": "Select the Rectangle tool from the Insert tab. Draw a wide shape across the top 50 mm of the page canvas. Set Fill to Deep Navy (#0284c7) and Outline to 'No Outline'."},
                            {"title": "2. Import and Crop Photographic Asset", "description": "Click Insert ➔ Picture. Select a high-resolution event photo. Activate the Crop tool and drag the black crop marks inward to trim distracting background elements."},
                            {"title": "3. Scale Proportionately with Shift-Lock", "description": "Click the top-right corner handle of the photo. Hold the Shift key down and drag inward to scale the image to 40 mm height without distorting facial proportions."},
                            {"title": "4. Insert and Style WordArt Heading", "description": "Click Insert ➔ WordArt. Choose a bold, readable style and type 'ANNUAL INNOVATION FAIR'. Apply Gold text fill and subtle drop shadow for strong visual contrast."},
                            {"title": "5. Configure Text Wrapping & Stacking Order", "description": "Right-click the imported image, set Wrap Text to 'Square' with a 3 mm offset, and use 'Bring Forward' / 'Send to Back' to position the WordArt over the Navy banner."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: School Sports Day Programme Design in Nakuru",
                    "content": {
                        "scenario": "Greenhill Academy in Nakuru is hosting an inter-school athletics championship. A student editor is designing a 2-page printed programme.",
                        "impact": "Initially, the student dragged the middle-right handle of the school crest to squeeze it into a narrow column, making the school emblem look squashed and unrecognisable. Furthermore, event schedules ran directly over the guest of honour's face.",
                        "solution": "Resetting the crest to its locked 1:1 aspect ratio, cropping the photo to an oval frame, and applying 'Tight' text wrapping created a clean, legible programme that drew praise from visiting school heads."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Cropping an Image Permanently Deletes Pixels",
                    "content": {
                        "misconception": "Cropping an image in DTP software permanently cuts away and destroys the hidden parts of the original image file.",
                        "correction": "DTP cropping is completely non-destructive. The crop tool acts as an adjustable visual window (mask). The full source image remains intact, and you can re-activate the crop tool anytime to pan the image or expand the visible frame boundaries."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The Balloon Distortion Trap",
                    "content": {
                        "mistake": "Dragging side or top/bottom handles of an image box to make it fit a gap, resulting in stretched faces and distorted logos.",
                        "why_it_happens": "Beginners often try to resize both width and height independently to fill available blank space on the canvas.",
                        "fix_solution": "Always hold the Shift key while dragging corner handles to lock the aspect ratio. If the photo does not fit the space, use the Crop tool to trim the sides rather than distorting proportions."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Image Aspect Ratio Protection",
                    "content": {
                        "question": "Which keyboard key must be held down while dragging a corner handle to resize an image without distorting its aspect ratio?",
                        "options": [
                            "The Shift key",
                            "The Tab key",
                            "The Caps Lock key",
                            "The Esc key"
                        ],
                        "correct": "A",
                        "explanation": "Holding down the Shift key while dragging any corner handle locks the width-to-height aspect ratio, preventing distorted or stretched images."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Text Wrapping Selection",
                    "content": {
                        "question": "Which text wrapping mode allows paragraph lines to flow smoothly along the natural curved contours of a circular vector shape or transparent badge?",
                        "options": [
                            "In Front of Text",
                            "Tight Wrap",
                            "Top and Bottom Wrap",
                            "No Wrapping"
                        ],
                        "correct": "B",
                        "explanation": "'Tight' text wrapping hugs the physical outline or alpha mask of an irregular or circular graphic, flowing text neatly around its perimeter."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Working with Shapes, Images, and Text Wrapping in DTP",
                    "content": {
                        "title": "Graphic Frames, Aspect Ratios, and Text Wrap Techniques",
                        "youtube_id": "k2KjU_w1hJk",
                        "url": "https://www.youtube.com/watch?v=k2KjU_w1hJk",
                        "description": "Demonstration of inserting vector shapes, scaling images proportionately, applying non-destructive cropping masks, and mastering text wrapping modes."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Shift-Lock Rule:** Never drag middle handles; always hold Shift and drag corner handles to maintain proportional aspect ratios.\n2. **Non-Destructive Cropping:** The crop tool trims visible framing without erasing the underlying source picture data.\n3. **Text Wrap Modes:** Choose Square for rectangular frames, Tight for contoured shapes, Top/Bottom for banners, and Behind for watermarks.\n4. **Layer Stacking:** Use 'Bring Forward' and 'Send Backward' to control overlapping shapes, text boxes, and WordArt titles."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6.1.4: Layout, Typography, and Design Principles
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Layout, Typography, and Design Principles",
        "unit_description": "Mastering the fundamental C.R.A.P. design principles (Contrast, Repetition, Alignment, Proximity), typographic anatomy, kerning, tracking, leading, and column grid systems.",
        "lesson_title": "Layout, Typography, and Design Principles",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Typographic Grids and Editorial Design Systems",
                    "content": {
                        "title": "Editorial Typography and Grid Systems",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Printed_documents_and_stationery.jpg",
                        "caption": "A collection of print publications demonstrating strong visual hierarchy, balanced white space, and consistent typographic systems.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Science and Psychology of Visual Communication",
                    "content": {
                        "text": "Good design is invisible. When a flyer or newsletter is beautifully laid out, your eyes glide effortlessly from the central headline down through columns of details without any conscious effort. But when a design is bad, you feel confused, your eyes get tired, and you toss the document into the recycling bin!\n\nGraphic design is not a collection of random artistic decorations—it is a cognitive science. By mastering the four golden **C.R.A.P. principles** (Contrast, Repetition, Alignment, Proximity) and understanding typographic spacing (kerning, tracking, leading), you can transform chaotic drafts into publication-grade documents that command attention and respect."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain and apply the four fundamental C.R.A.P. design principles (Contrast, Repetition, Alignment, Proximity)\n- Distinguish between character-level and paragraph-level typographic spacing (Kerning, Tracking, Leading)\n- Structure balanced multi-column grid layouts with consistent gutters and margins\n- Utilize white space (negative space) effectively to eliminate cognitive clutter and guide reader scanpaths"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "C.R.A.P. Design Principles & Typographic Spacing",
                    "content": {
                        "term": "Visual Hierarchy & C.R.A.P. Principles",
                        "definition": "A foundational framework of four design rules—Contrast, Repetition, Alignment, and Proximity—used to structure page layouts for maximum clarity, aesthetic balance, and reader engagement.",
                        "simple": "The four golden rules of design: make key items stand out (Contrast), keep styles consistent (Repetition), line elements up neatly (Alignment), and group related items together (Proximity).",
                        "technical": "An analytical design methodology that optimizes human cognitive scanpaths across two-dimensional surfaces through optical weight distribution, stylistic standardization, baseline grid adherence, and semantic spatial chunking.",
                        "example": "Pairing a large bold 28pt headline (Contrast) with 10pt body text aligned to a 3-column grid (Alignment), with author photo placed next to the byline (Proximity)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Deep Dive: The 4 Pillars and Typographic Fine-Tuning",
                    "content": {
                        "text": "Professional designers evaluate every page layout against four core principles:\n\n1. **Contrast:** Every page needs a distinct **Focal Point**. If two elements are not identical, make them boldly different! Use contrasting font weights (Bold vs Regular), sizes (32pt title vs 10pt body), or color pairings (Dark Navy on White).\n2. **Repetition:** Develop visual consistency by repeating design motifs—such as using the same header stripe, bullet style, 3-color palette, and standard font pairings across all pages.\n3. **Alignment:** Every item on a page must have a visual connection to something else. Never place elements arbitrarily. Snap text frames and picture boxes to column guides and margin baselines.\n4. **Proximity & White Space:** Group related items together (e.g., headline, date, author byline) to form a unified visual chunk. Use generous **White Space (Negative Space)** between unrelated sections to give the reader's eyes breathing room.\n\n### Typographic Spacing Controls:\n\n- **Kerning:** The selective adjustment of horizontal spacing between specific pairs of letters (e.g., reducing the awkward gap in 'AV', 'To', or 'WA') to create smooth display titles.\n- **Tracking:** The uniform adjustment of letter-spacing across an entire word, line, or paragraph (used to expand all-caps titles or tighten text to fit columns).\n- **Leading (Line Spacing):** The vertical distance between successive lines of text. Standard readable body text requires a leading of 120% to 140% of the font size (e.g., 10pt font with 14pt leading)."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "The C.R.A.P. Design Framework & Typographic Spacing Mechanics",
                    "content": {
                        "title": "Visual Anatomy of C.R.A.P. Principles, Kerning, Tracking, and Leading",
                        "caption": "Comprehensive visual matrix illustrating Contrast, Repetition, Alignment, Proximity, alongside Kerning, Tracking, and Leading anatomy.",
                        "svg_content": SVG_CRAP_DESIGN_PRINCIPLES
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step: Designing a Balanced 3-Column Newsletter Page",
                    "content": {
                        "intro": "Practical layout procedure applying design principles and typographic controls:",
                        "steps": [
                            {"title": "1. Establish the Column Grid System", "description": "Configure an A4 page with a 3-column layout grid. Set column widths to 55 mm with 5 mm gutters and 15 mm outer margins for balanced geometric structure."},
                            {"title": "2. Create the Primary Focal Point (Contrast)", "description": "Insert a full-width header banner at the top with a bold 32pt sans-serif headline in dark navy, establishing an immediate visual anchor."},
                            {"title": "3. Chunk Content via Proximity & White Space", "description": "Position article title, byline, and paragraph in close proximity (2 mm spacing) while leaving a 12 mm white space cushion before the next unrelated story."},
                            {"title": "4. Enforce Typographic Repetition (The 2-Font Rule)", "description": "Limit fonts strictly to 2 families: clean Sans-Serif (e.g., Arial/Montserrat) for headlines and readable Serif/Sans-Serif (e.g., Georgia/Calibri 10pt) for body text."},
                            {"title": "5. Fine-Tune Kerning, Tracking, and Leading", "description": "Apply subtle loose tracking to all-caps category tags (e.g., 'S P O R T S') and set body text line spacing to 1.3 lines (13pt leading) to eliminate line crowding."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Redesigning a Public Health Flyer in Kisumu",
                    "content": {
                        "scenario": "The County Public Health Department in Kisumu produced an emergency advisory flyer on clean water purification.",
                        "impact": "The original flyer used six different brightly colored fonts (Comic Sans, Impact, Courier, Brush Script), text covered 100% of the paper with zero margins, and warnings were scattered randomly. Residents found it confusing and discarded it.",
                        "solution": "Redesigning the flyer with C.R.A.P. principles—a single high-contrast red headline (Contrast), 2-font system (Repetition), left-aligned bulleted steps (Alignment), and 25% clean white space (Proximity)—doubled community comprehension and compliance."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: White Space is Wasted Space",
                    "content": {
                        "misconception": "A good designer should fill every single square centimeter of a page with text or graphics to maximize the value of the paper.",
                        "correction": "White space (negative space) is an active, essential design tool. It prevents cognitive overload, reduces eye fatigue, separates distinct topics, and directs the reader's attention directly to the most critical information."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The 'Ransom Note' Font Clutter",
                    "content": {
                        "mistake": "Using 5 or more decorative fonts with clashing colors in a single one-page flyer to make every sentence look 'unique'.",
                        "why_it_happens": "Beginners often get excited by extensive font menus and assume variety makes documents look more creative.",
                        "fix_solution": "Strictly adhere to the 2-Font Rule: Choose one clean font family for headings and one highly readable font family for body text. Vary weight (Bold/Regular) and size for contrast, not typefaces."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Kerning vs Tracking Distinction",
                    "content": {
                        "question": "What is the technical difference between Kerning and Tracking in typography?",
                        "options": [
                            "Kerning adjusts the space between two specific letters, while Tracking adjusts uniform spacing across an entire block of text",
                            "Kerning changes font colors, while Tracking converts text into 3D shapes",
                            "Kerning adds page numbers, while Tracking calculates document word counts",
                            "Kerning is used only for body paragraphs, while Tracking is used only for footers"
                        ],
                        "correct": "A",
                        "explanation": "Kerning selectively fine-tunes the optical space between individual character pairs (like 'AV'), whereas Tracking adjusts letter-spacing uniformly across a selected run of words or paragraphs."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: The Proximity Principle",
                    "content": {
                        "question": "A designer places an article's author byline 8 centimeters away from the article's headline, next to an unrelated photo caption. Which design principle is violated?",
                        "options": [
                            "Database normalization",
                            "Proximity",
                            "Hardware acceleration",
                            "Optical character recognition"
                        ],
                        "correct": "B",
                        "explanation": "The Proximity principle requires related elements (such as an article headline, date, and author byline) to be grouped physically close together to signal their semantic relationship."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Graphic Design & Typography Principles for Beginners",
                    "content": {
                        "title": "Mastering C.R.A.P. Design Rules & Typographic Hierarchy",
                        "youtube_id": "g4C3EFr_H5A",
                        "url": "https://www.youtube.com/watch?v=g4C3EFr_H5A",
                        "description": "Engaging visual tutorial breaking down Contrast, Repetition, Alignment, Proximity, Kerning, Tracking, and Leading in real-world publications."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **C.R.A.P. Framework:** Build strong focal points (Contrast), maintain stylistic unity (Repetition), connect elements via grids (Alignment), and group related items (Proximity).\n2. **The 2-Font Rule:** Restrict publications to 2 matching font families to prevent chaotic 'ransom note' typography.\n3. **Typographic Spacing:** Fine-tune character-pair gaps (Kerning), line tracking (Tracking), and baseline vertical spacing (Leading).\n4. **Power of White Space:** Treat empty negative space as an active design element that organizes information and reduces reader eye fatigue."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6.1.5: Document Setup, Master Pages, and Template Design
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Document Setup, Master Pages, and Template Design",
        "unit_description": "Configuring multi-page publication geometry: margins, bleed, slug, trim dimensions, facing pages (spreads), master page architecture, dynamic headers/footers, automated page numbering placeholders, and reusable template design.",
        "lesson_title": "Document Setup, Master Pages, and Template Design",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Multi-Page Document Architecture and Master Templates",
                    "content": {
                        "title": "Master Template Geometry and Page Spreads",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "A multi-page publication spread showing facing pages, master page backgrounds, margin guides, and automatic pagination.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Master Blueprint of Multi-Page Publications",
                    "content": {
                        "text": "Imagine you are tasked with designing a 24-page school yearbook. You need the school name, a navy blue header stripe, and the current page number to appear at the exact same coordinates on every single page. Do you manually copy and paste these elements onto all 24 pages?\n\nAbsolutely not! If you did, and later decided to change the navy stripe to forest green, you would have to make that change 24 separate times. Desktop publishing software solves this through **Master Pages**—the master background templates of layout design. By placing repeating elements on a Master Page, they automatically project onto every linked page, while you focus on typing unique article content in the foreground."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Configure document setup geometry: Trim size, Safe Margins, Bleed Area (+3mm), and Slug Area\n- Create, edit, and assign Master Pages across multi-page document spreads\n- Insert running headers, footers, and automatic page numbering placeholder tokens\n- Manage multi-master page configurations (e.g. Suppressing master items on Cover pages)\n- Save finalized publication structures as reusable templates (.pubt / .sct)"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Master Page & Bleed Area",
                    "content": {
                        "term": "Master Page",
                        "definition": "A background template page that hosts static repeating visual elements, grid structures, and dynamic metadata (like page numbers) across linked foreground pages.",
                        "simple": "A master background page where whatever you place (like headers, logos, or page numbers) automatically appears on every page in your document.",
                        "technical": "A non-rendering background canvas layer decoupled from the foreground content layer, providing global structural inheritance of vector objects, margin bounds, and system variable tokens (such as pagination tags) across assigned page spreads.",
                        "example": "Setting up Master Page A with a top green accent stripe, school crest, and dynamic page number footer for a 16-page syllabus handbook."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Print Production Anatomy & Master Page Operations",
                    "content": {
                        "text": "Setting up a commercial multi-page publication requires understanding four concentric print boundaries:\n\n1. **Trim Line:** The exact final dimension of the cut physical page (e.g., A4 210 x 297 mm).\n2. **Safe Margin Zone (12 mm - 15 mm inside trim):** The boundary where all critical text, logos, and tables must reside to avoid being clipped during guillotine cutting.\n3. **Bleed Area (+3 mm outside trim):** The extra 3 mm zone extending beyond the trim line. Any background color box or photo that reaches the edge of the paper MUST extend into the bleed area to prevent white paper slivers when trimmed.\n4. **Slug Area:** An outer technical margin holding printer crop marks, registration targets, job titles, and color calibration bars.\n\n### Master Page Global Architecture:\n\n- **Foreground vs Master Edit Mode:** Master page elements are locked in foreground mode to prevent accidental movement. To edit a header or page number, you must enter 'Master Page Edit Mode'.\n- **Dynamic Pagination Placeholders:** Inserting a page number token (e.g., `#` or `[Page]`) on a master page automatically evaluates to the integer page index (1, 2, 3...) on each foreground page.\n- **Multi-Master Configurations:** Documents can use multiple templates (e.g., Master A for content, Master B for chapter dividers, and 'Master: None' to keep cover pages completely blank)."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Document Setup Anatomy: Bleed, Trim, Margins & Master Page Layering",
                    "content": {
                        "title": "Print Production Boundaries and Master-to-Foreground Layering",
                        "caption": "High-precision vector diagram illustrating the Bleed Area, Trim Line, Safe Margin Zone, Slug Area, and dual-layer Master Page to Foreground inheritance.",
                        "svg_content": SVG_DOCUMENT_SETUP_BLEED
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step: Building a Master Template with Automatic Pagination",
                    "content": {
                        "intro": "Standard professional procedure for setting up a multi-page publication template:",
                        "steps": [
                            {"title": "1. Configure Document Setup with 3mm Bleed", "description": "Set page size to A4 Landscape (297 x 210 mm), margins to 15 mm, and outer Bleed to 3 mm on all four sides in the Document Setup dialog."},
                            {"title": "2. Enter Master Page Edit Mode", "description": "Navigate to Page Design ➔ Master Pages ➔ Edit Master Pages. Notice the green tab confirming you are working on the background layer."},
                            {"title": "3. Draw Running Header with Bleed Extension", "description": "Draw a rectangle across the top margin. Extend the top edge 3 mm into the red Bleed zone. Fill with Forest Green and add white text: 'Grade 10 ICT Handbook'."},
                            {"title": "4. Insert Dynamic Page Number Placeholder", "description": "Draw a small text frame in the bottom-right footer margin. Click Insert ➔ Page Number. A dynamic token tag (`[#]`) appears inside the frame."},
                            {"title": "5. Close Master Mode & Apply Cover Exception", "description": "Click 'Close Master Page'. Right-click the Page 1 thumbnail in the navigation sidebar, select Master Pages ➔ None to suppress headers on the cover."},
                            {"title": "6. Save as Reusable Publisher Template", "description": "Click File ➔ Save As ➔ Publisher Template (.pubt / .sct) to preserve the master layout for future annual publications."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: National Schools Drama Festival Booklet in Mombasa",
                    "content": {
                        "scenario": "The Kenya National Drama Festival organizing committee in Mombasa prepared a 24-page programme booklet containing stage schedules, team bios, and color photos.",
                        "impact": "Because the original designer manually typed page numbers onto each individual page, inserting a last-minute 2-page sponsor advertisement threw off the numbering, requiring manual re-typing across 20 pages! Furthermore, full-page stage photos left white borders after guillotine trimming.",
                        "solution": "Rebuilding the booklet with Master Pages automated pagination instantly across all 24 pages. Extending photos 3 mm into the Bleed area ensured flawless edge-to-edge full-bleed color printing."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: You Can Edit Master Page Elements on Foreground Pages",
                    "content": {
                        "misconception": "Clicking or double-clicking on a running header text on Page 4 will let you edit its text directly on the foreground page.",
                        "correction": "Master Page elements are locked in foreground mode to prevent accidental movement. To modify a master header, logo, or page number, you must enter Master Page Edit Mode. The change will then update globally across all linked pages."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The White Margin Sliver Trap (Missing Bleed)",
                    "content": {
                        "mistake": "Positioning a colored background shape exactly on the 0 mm trim line, resulting in uneven white slivers on the edge of the printed booklet.",
                        "why_it_happens": "Industrial paper-cutting guillotines vibrate and can shift by 0.5 mm during high-speed cutting. If background color stops exactly at the trim line, slight shifts expose raw white paper.",
                        "fix_solution": "Always extend background shapes and borderless photos 3 mm beyond the trim line into the Bleed zone. The blade will cut through pure color, ensuring a clean edge."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Purpose of the Bleed Area",
                    "content": {
                        "question": "Why must background colors and photographs extend 3mm into the Bleed Area in commercial desktop publishing?",
                        "options": [
                            "To make the software render text fonts in bold italics",
                            "To prevent unwanted white paper slivers along the edges when the physical cutting blade trims the pages",
                            "To increase the download speed of the PDF file on mobile phones",
                            "To compress high-resolution images into low-resolution icons"
                        ],
                        "correct": "B",
                        "explanation": "Extending backgrounds 3 mm beyond the trim line into the bleed area guarantees that physical guillotine blade shifts during trimming cut through ink rather than exposing white paper edges."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Suppressing Master Page on Cover",
                    "content": {
                        "question": "How can a designer ensure that running headers and page numbers defined on a Master Page do NOT appear on the front cover of a publication?",
                        "options": [
                            "Delete the Master Page completely from the document",
                            "Assign 'None' or a blank Master Page specifically to the Page 1 thumbnail",
                            "Cover the entire front page with white correction paint",
                            "Turn off the computer screen before printing page 1"
                        ],
                        "correct": "B",
                        "explanation": "Assigning 'Master: None' or applying a blank Master Page template to Page 1 suppresses running headers, footers, and page numbers on the cover while preserving them on interior pages."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Master Pages, Bleed, and Multi-Page Document Setup",
                    "content": {
                        "title": "Master Page Templates, Bleed Geometry, and Automatic Pagination",
                        "youtube_id": "j3v_p-9s5Z4",
                        "url": "https://www.youtube.com/watch?v=j3v_p-9s5Z4",
                        "description": "Comprehensive tutorial covering document setup geometry, configuring 3mm bleed margins, editing Master Pages, and inserting dynamic pagination placeholders."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Print Geometry:** Setup documents with a Trim line (cut boundary), Safe Margins (text cushion), and +3mm Bleed (edge-to-edge ink coverage).\n2. **Master Page Inheritance:** Placing headers, footers, and page number tokens on a Master Page globally populates all linked foreground pages.\n3. **Pagination Placeholders:** Dynamic page tokens (`[#]`) automatically evaluate to correct sequential page numbers throughout the publication.\n4. **Cover Exceptions:** Use multi-master configurations or assign 'Master: None' to keep cover pages clean of interior running metadata."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6.1.6: Finalizing, Printing, and Exporting Publications
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Finalizing, Printing, and Exporting Publications",
        "unit_description": "Quality assurance and preflight diagnostics (image resolution 300 DPI vs 72 DPI, RGB vs CMYK color spaces, font embedding, overset text checks), executing Mail Merge for personalized publications, commercial offset vs digital print output, and multi-channel PDF/digital export.",
        "lesson_title": "Finalizing, Printing, and Exporting Publications",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "High-Volume Commercial Printing & Multi-Channel Distribution",
                    "content": {
                        "title": "Preflight Inspection and Commercial Print Production",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Computer_classroom_in_Kenya.jpg",
                        "caption": "Students reviewing preflight diagnostics, executing mail merge data links, and compiling high-resolution PDF print files.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "From Screen Draft to Print Press Perfection",
                    "content": {
                        "text": "In desktop publishing, finishing your visual layout is only 80% of the journey. The final 20% is the **refinement and preflight phase**—where you verify technical integrity before sending your files to commercial printing presses or global web portals.\n\nImagine printing 2,000 copies of a full-color school magazine only to discover that the cover photo is pixelated and blurry, or that long student names were cut off in an invitation merge! Running **preflight diagnostic checks** catches low-resolution images (<300 DPI), RGB color shifts, and font substitution errors before expensive printing plates are created. Integrating **Mail Merge** links your layouts to databases to produce hundreds of customized certificates in seconds."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Execute a preflight diagnostic audit to detect low-resolution images (<300 DPI), RGB-to-CMYK color space shifts, font embedding issues, and overset text\n- Connect external database sources (Excel/CSV) and execute a multi-record Mail Merge for personalized publications\n- Contrast commercial offset printing (CMYK plates, imposition, printer spreads) with digital on-demand printing\n- Export standards-compliant PDF/X print files with crop marks and interactive digital PDFs for mobile/web distribution"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Preflight Check & Mail Merge",
                    "content": {
                        "term": "Preflight Inspection & Color Separation",
                        "definition": "The automated quality assurance analysis of a DTP publication file to identify technical errors (low resolution, RGB color spaces, missing fonts, overset text) prior to commercial printing or final distribution.",
                        "simple": "A digital safety inspection that checks your document for mistakes (like blurry photos, missing fonts, or text getting cut off) before you send it to the printer.",
                        "technical": "An automated diagnostic verification protocol assessing vector asset compliance, font glyph subsetting, overset frame states, spot color trapping, and CMYK (Cyan, Magenta, Yellow, Key/Black) raster density at 300 DPI.",
                        "example": "Running Publisher's Design Checker to catch a 96 DPI web logo and converting RGB graphics to CMYK for offset press printing."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Preflight Diagnostic Matrix & Mail Merge Integration",
                    "content": {
                        "text": "A professional publishing pipeline involves two essential finalizing systems:\n\n### 1. The 4-Point Preflight Diagnostic Audit:\n- **Image Resolution Check:** Web graphics (72 - 96 DPI) look sharp on screens but print blurry. Professional commercial print requires high-density raster images at **300 DPI** minimum.\n- **Color Space Separation (RGB vs. CMYK):** Computer monitors emit light using additive **RGB** (Red, Green, Blue). Commercial printing presses stamp subtractive inks using **CMYK** (Cyan, Magenta, Yellow, Key/Black). Preflight converts RGB graphics to CMYK to prevent dull, unexpected color shifts.\n- **Font Embedding:** Preflight packages font subsets into the PDF so the printer does not substitute delicate fonts with default system typefaces.\n- **Overset Text Verification:** Checks all text frames for hidden overflow text marked by red `[+]` icons.\n\n### 2. Database Integration via Mail Merge:\n- **Data Source:** A structured spreadsheet (Excel/CSV) with clean column headers (`First_Name`, `Award_Title`, `Seat_No`).\n- **Master Layout:** The publication template hosting dynamic merge field tokens (e.g. `<<First_Name>>`).\n- **Merged Publication Engine:** Compiles individual customized copies for every database row into a single print-ready file in seconds."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Preflight Quality Control, Mail Merge & Multi-Channel Export",
                    "content": {
                        "title": "Visual Architecture of Preflight Auditing, Mail Merge, and Multi-Channel Output",
                        "caption": "Comprehensive vector flowchart showing preflight quality verification, database mail merge generation, and dual-track output to CMYK offset print and interactive digital PDF.",
                        "svg_content": SVG_PREFLIGHT_PRINT_PIPELINE
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step: Running Preflight, Executing Mail Merge, and Exporting PDF",
                    "content": {
                        "intro": "Standard professional publishing workflow from final layout to multi-channel distribution:",
                        "steps": [
                            {"title": "1. Prepare and Clean the External Data Source", "description": "Open Excel and verify row 1 contains clean headers (`Full_Name`, `Certificate_ID`, `Grade`) with no special symbols or blank rows."},
                            {"title": "2. Connect Data Source and Insert Merge Fields", "description": "In MS Publisher, go to Mailings ➔ Select Recipients ➔ Use Existing List. Insert `<<Full_Name>>` and provide generous horizontal cushion space."},
                            {"title": "3. Execute Preflight Diagnostic Inspection", "description": "Run the Design Checker tool. Verify that all photos are at least 300 DPI, no overset text exists, and colors are configured for CMYK output."},
                            {"title": "4. Preview and Merge to New Publication", "description": "Click 'Preview Results' to cycle through recipient records. Click 'Finish & Merge' ➔ 'Merge to New Publication' to compile all customized cards."},
                            {"title": "5. Export Dual Output Formats (Print & Web)", "description": "Export a Press-Ready PDF/X file with crop marks for commercial printing, and export an optimized RGB PDF with live hyperlinks for website downloads."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Printing Personalized Certificates in Nyeri",
                    "content": {
                        "scenario": "The executive committee for the Kenya National Music Festival in Nyeri needed to issue 1,200 personalized merit certificates for winning choir students within 24 hours.",
                        "impact": "In previous years, manually typing student names into individual certificate files took 3 days and resulted in dozens of spelling errors and font inconsistencies.",
                        "solution": "Linking the master certificate template to the adjudicators' Excel database via Mail Merge allowed all 1,200 personalized certificates to be generated, checked via preflight, and exported to high-resolution print PDF in under 60 seconds with zero typographical errors."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Sharp Phone Images Print Sharply on Paper",
                    "content": {
                        "misconception": "If a photo downloaded from WhatsApp or Instagram looks crystal sharp on a high-definition smartphone screen, it will print with perfect clarity on an A4 poster.",
                        "correction": "Phone screens display at 72 to 120 DPI in additive RGB light. Commercial printing requires 300 DPI in subtractive CMYK ink. A 72 DPI web image will appear jagged, pixelated, and blurry when printed on physical paper."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The Truncated Long Name Merge Overflow",
                    "content": {
                        "mistake": "Printing 500 certificates and discovering that 30 students with long hyphenated names have their names cut off at the margins.",
                        "why_it_happens": "The merge field text frame was drawn tightly around short preview names like 'Ann Ali', failing to accommodate long names like 'Christopher-Mwenda Kipchoge'.",
                        "fix_solution": "Always design merge text boxes with extra width and activate 'AutoFit Text / Shrink Text on Overflow' to dynamically scale longer entries safely."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Color Space Conversion for Commercial Print",
                    "content": {
                        "question": "Which color space model must be used when preparing a desktop publishing file for commercial four-color offset printing presses?",
                        "options": [
                            "CMYK (Cyan, Magenta, Yellow, Key/Black)",
                            "RGB (Red, Green, Blue)",
                            "Monochrome Binary (0 and 1)",
                            "Hexadecimal Web Safe Colors"
                        ],
                        "correct": "A",
                        "explanation": "Commercial offset printing presses use four physical ink separation plates corresponding to the subtractive CMYK (Cyan, Magenta, Yellow, Black) color model."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Minimum Print Resolution Standard",
                    "content": {
                        "question": "What is the industry-standard minimum resolution (density) required for raster images to print sharply in high-quality publications?",
                        "options": [
                            "72 DPI",
                            "96 DPI",
                            "300 DPI",
                            "12 DPI"
                        ],
                        "correct": "C",
                        "explanation": "Commercial print standard requires a minimum raster density of 300 DPI (Dots Per Inch) to avoid pixelation and blurriness on paper."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Preflighting, Mail Merge, and Print Production in DTP",
                    "content": {
                        "title": "Preflight Checks, Color Separation, and Mail Merge Automation",
                        "youtube_id": "k9Z_3b-0wQY",
                        "url": "https://www.youtube.com/watch?v=k9Z_3b-0wQY",
                        "description": "Comprehensive tutorial explaining how to run preflight diagnostic audits, convert RGB to CMYK, execute database Mail Merge, and export press-ready PDF/X files."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 6 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Preflight Quality Control:** Always audit publications for 300 DPI image resolution, CMYK color spaces, embedded fonts, and overset text before printing.\n2. **Mail Merge Automation:** Integrate external database spreadsheets with template placeholders (`<<Name>>`) to batch-generate hundreds of personalized publications in seconds.\n3. **Print vs Web Channels:** Export Press-Quality PDF/X files with crop marks for commercial presses, and interactive RGB PDFs for web portals and mobile screens.\n4. **Text AutoFit Protection:** Apply auto-fit text attributes to merge frames to ensure long names never trigger overset text cutoff errors."
                    }
                }
            ]
        ]
    }
]
