"""
VLearn CBC Grade 10 ICT — Topic 3: Operating Systems
Full Structured Lesson Card Definitions (Lessons 1 to 6) with Responsive Custom SVGs
"""

# =============================================================================
# HIGH-DETAIL RESPONSIVE SVG VECTOR GRAPHICS
# =============================================================================

SVG_COMPUTER_SYSTEM_LAYERS = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 560" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="userGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
    <linearGradient id="appGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#8b5cf6"/>
    </linearGradient>
    <linearGradient id="osGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
    <linearGradient id="hwGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-10%" width="110%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="900" height="560" rx="16" fill="url(#bgGrad)"/>
  <rect x="2" y="2" width="896" height="556" rx="14" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header Section -->
  <text x="450" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#f8fafc" text-anchor="middle" letter-spacing="1">COMPUTER SYSTEM ARCHITECTURAL LAYERS</text>
  <text x="450" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">The Operating System as the Indispensable Intermediary Bridge</text>

  <!-- Left Side Flow Indicator (Downwards: User Commands) -->
  <g transform="translate(45, 100)">
    <rect x="0" y="0" width="60" height="390" rx="8" fill="#1e293b" stroke="#334155" stroke-dasharray="4 4"/>
    <text x="30" y="30" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">USER</text>
    <text x="30" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">INPUT</text>
    <path d="M 30 70 L 30 320" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
    <polygon points="30,335 23,315 37,315" fill="#38bdf8"/>
    <text x="30" y="360" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">System</text>
    <text x="30" y="375" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Calls</text>
  </g>

  <!-- Layer 1: Users (Top) -->
  <g transform="translate(130, 95)" filter="url(#shadow)">
    <rect width="640" height="75" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
    <rect x="0" y="0" width="12" height="75" rx="4" fill="url(#userGrad)"/>
    <circle cx="45" cy="37" r="18" fill="#0369a1"/>
    <!-- User Icon -->
    <path d="M 45 27 A 6 6 0 1 0 45 39 A 6 6 0 1 0 45 27 Z M 35 48 C 35 43 40 42 45 42 C 50 42 55 43 55 48 Z" fill="#ffffff"/>
    <text x="75" y="32" font-family="system-ui, sans-serif" font-size="16" font-weight="700" fill="#e0f2fe">1. USER LAYER (Human Interaction)</text>
    <text x="75" y="54" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8">Students, Programmers, Professionals, Gamers &amp; System Administrators</text>
    <rect x="520" y="24" width="105" height="26" rx="13" fill="#0c4a6e"/>
    <text x="572" y="41" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#38bdf8" text-anchor="middle">Direct Input</text>
  </g>

  <!-- Layer 2: Application Software -->
  <g transform="translate(130, 185)" filter="url(#shadow)">
    <rect width="640" height="75" rx="10" fill="#1e293b" stroke="#7c3aed" stroke-width="2"/>
    <rect x="0" y="0" width="12" height="75" rx="4" fill="url(#appGrad)"/>
    <circle cx="45" cy="37" r="18" fill="#5b21b6"/>
    <!-- App Window Icon -->
    <rect x="36" y="28" width="18" height="18" rx="2" fill="none" stroke="#ffffff" stroke-width="2"/>
    <line x1="36" y1="34" x2="54" y2="34" stroke="#ffffff" stroke-width="1.5"/>
    <text x="75" y="32" font-family="system-ui, sans-serif" font-size="16" font-weight="700" fill="#ede9fe">2. APPLICATION SOFTWARE LAYER</text>
    <text x="75" y="54" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8">Web Browsers (Chrome), Word Processors (Word), Spreadsheets, Games, Media Players</text>
    <rect x="520" y="24" width="105" height="26" rx="13" fill="#4c1d95"/>
    <text x="572" y="41" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#c084fc" text-anchor="middle">User Apps</text>
  </g>

  <!-- Layer 3: Operating System (THE BRIDGE - Highlighted) -->
  <g transform="translate(130, 275)" filter="url(#shadow)">
    <rect width="640" height="95" rx="10" fill="#291e0a" stroke="#f59e0b" stroke-width="2.5"/>
    <rect x="0" y="0" width="14" height="95" rx="4" fill="url(#osGrad)"/>
    <circle cx="45" cy="47" r="22" fill="#b45309"/>
    <!-- OS Gear Icon -->
    <path d="M 45 35 L 47 38 L 51 38 L 49 42 L 51 46 L 47 46 L 45 49 L 43 46 L 39 46 L 41 42 L 39 38 L 43 38 Z" fill="#ffffff"/>
    <circle cx="45" cy="42" r="3" fill="#b45309"/>
    <text x="75" y="34" font-family="system-ui, sans-serif" font-size="17" font-weight="800" fill="#fef3c7">3. OPERATING SYSTEM (System Platform &amp; Kernel)</text>
    <text x="75" y="56" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">Windows, macOS, Linux (Ubuntu), Android, iOS — Resource Coordinator &amp; Translator</text>
    <text x="75" y="76" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#f59e0b">&#x25C6; Process Scheduling  &#x25C6; Memory Management  &#x25C6; Device Drivers  &#x25C6; File System</text>
    <rect x="505" y="34" width="120" height="28" rx="14" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="565" y="52" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#fef3c7" text-anchor="middle">THE BRIDGE</text>
  </g>

  <!-- Layer 4: Computer Hardware -->
  <g transform="translate(130, 385)" filter="url(#shadow)">
    <rect width="640" height="75" rx="10" fill="#1e293b" stroke="#059669" stroke-width="2"/>
    <rect x="0" y="0" width="12" height="75" rx="4" fill="url(#hwGrad)"/>
    <circle cx="45" cy="37" r="18" fill="#047857"/>
    <!-- CPU / Microchip Icon -->
    <rect x="37" y="29" width="16" height="16" rx="2" fill="#ffffff"/>
    <rect x="41" y="33" width="8" height="8" fill="#047857"/>
    <text x="75" y="32" font-family="system-ui, sans-serif" font-size="16" font-weight="700" fill="#d1fae5">4. PHYSICAL HARDWARE LAYER</text>
    <text x="75" y="54" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8">CPU (Processor), Main Memory (RAM), SSD/HDD Storage, GPU, Keyboard, Display, NIC</text>
    <rect x="520" y="24" width="105" height="26" rx="13" fill="#064e3b"/>
    <text x="572" y="41" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#6ee7b7" text-anchor="middle">Raw Silicon</text>
  </g>

  <!-- Right Side Flow Indicator (Upwards: Execution Feedback) -->
  <g transform="translate(795, 100)">
    <rect x="0" y="0" width="60" height="390" rx="8" fill="#1e293b" stroke="#334155" stroke-dasharray="4 4"/>
    <text x="30" y="30" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#10b981" text-anchor="middle">DATA</text>
    <text x="30" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#10b981" text-anchor="middle">OUTPUT</text>
    <path d="M 30 320 L 30 70" stroke="#10b981" stroke-width="2.5" stroke-linecap="round"/>
    <polygon points="30,55 23,75 37,75" fill="#10b981"/>
    <text x="30" y="360" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Binary</text>
    <text x="30" y="375" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Signals</text>
  </g>

  <!-- Footer Banner -->
  <rect x="130" y="485" width="640" height="48" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="450" y="514" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1" text-anchor="middle">Key Rule: Users and Applications <tspan font-weight="700" fill="#f59e0b">cannot talk directly</tspan> to Hardware circuits. The OS coordinates all data flow safely.</text>
</svg>"""


SVG_OS_CORE_FUNCTIONS = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 560" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e1a"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1a2236"/>
    </linearGradient>
    <linearGradient id="centerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="900" height="560" rx="16" fill="url(#bgGrad2)"/>
  <rect x="2" y="2" width="896" height="556" rx="14" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="450" y="38" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#f8fafc" text-anchor="middle" letter-spacing="1">THE 5 CORE FUNCTIONS OF AN OPERATING SYSTEM</text>
  <text x="450" y="60" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Coordinated Resource Management Engine</text>

  <!-- Connecting Spoke Lines (Dashed glow) -->
  <line x1="450" y1="280" x2="180" y2="145" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 4"/>
  <line x1="450" y1="280" x2="720" y2="145" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="6 4"/>
  <line x1="450" y1="280" x2="750" y2="350" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6 4"/>
  <line x1="450" y1="280" x2="450" y2="465" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 4"/>
  <line x1="450" y1="280" x2="150" y2="350" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6 4"/>

  <!-- Central Hub: Operating System Engine -->
  <circle cx="450" cy="280" r="72" fill="#0284c7" opacity="0.15" filter="url(#glow)"/>
  <circle cx="450" cy="280" r="64" fill="url(#centerGrad)" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="450" cy="280" r="54" fill="#0c4a6e"/>
  <!-- Central Gear Icon -->
  <path d="M 450 258 L 454 264 L 462 264 L 458 272 L 462 280 L 454 280 L 450 286 L 446 280 L 438 280 L 442 272 L 438 264 L 446 264 Z" fill="#38bdf8"/>
  <circle cx="450" cy="272" r="5" fill="#0c4a6e"/>
  <text x="450" y="304" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#f8fafc" text-anchor="middle">OPERATING</text>
  <text x="450" y="318" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#38bdf8" text-anchor="middle">SYSTEM</text>

  <!-- Pillar 1: Processor Management (Top-Left) -->
  <g transform="translate(70, 95)">
    <rect width="220" height="100" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#0369a1"/>
    <text x="110" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">1. PROCESSOR (CPU)</text>
    <text x="15" y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#38bdf8">&#x2022; Multitasking &amp; Scheduling</text>
    <text x="15" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Time-slicing between active apps</text>
    <text x="15" y="84" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Prevents app monopolies</text>
  </g>

  <!-- Pillar 2: Memory Management (Top-Right) -->
  <g transform="translate(610, 95)">
    <rect width="220" height="100" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#7e22ce"/>
    <text x="110" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">2. MEMORY (RAM)</text>
    <text x="15" y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#c084fc">&#x2022; Dynamic RAM Allocation</text>
    <text x="15" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Memory space isolation</text>
    <text x="15" y="84" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Reclaims RAM on app close</text>
  </g>

  <!-- Pillar 3: File System Management (Right) -->
  <g transform="translate(640, 300)">
    <rect width="220" height="100" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#047857"/>
    <text x="110" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">3. FILE &amp; STORAGE</text>
    <text x="15" y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#34d399">&#x2022; Hierarchical Folders &amp; Files</text>
    <text x="15" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Master storage directory</text>
    <text x="15" y="84" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Tracks size, dates &amp; paths</text>
  </g>

  <!-- Pillar 4: Device Management (Bottom-Center) -->
  <g transform="translate(340, 415)">
    <rect width="220" height="100" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#b45309"/>
    <text x="110" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">4. DEVICE I/O CONTROL</text>
    <text x="15" y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#fbbf24">&#x2022; Device Drivers Translation</text>
    <text x="15" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Keyboard, Mouse &amp; Printer links</text>
    <text x="15" y="84" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Plug-and-Play automation</text>
  </g>

  <!-- Pillar 5: Security & Access Control (Left) -->
  <g transform="translate(40, 300)">
    <rect width="220" height="100" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#b91c1c"/>
    <text x="110" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">5. SECURITY &amp; ACCESS</text>
    <text x="15" y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#f87171">&#x2022; User Login Authentication</text>
    <text x="15" y="66" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; File permissions (Read/Write)</text>
    <text x="15" y="84" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Protection against malware</text>
  </g>

  <!-- Diagnostic Note Box -->
  <rect x="250" y="522" width="400" height="28" rx="6" fill="#0f172a" stroke="#475569"/>
  <text x="450" y="541" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Monitor these live with <tspan fill="#38bdf8" font-weight="700">Windows Task Manager</tspan> or <tspan fill="#a855f7" font-weight="700">macOS Activity Monitor</tspan></text>
</svg>"""


SVG_OS_PLATFORMS_MATRIX = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 560" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>

  <rect width="900" height="560" rx="16" fill="url(#bgGrad3)"/>
  <rect x="2" y="2" width="896" height="556" rx="14" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="450" y="38" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#f8fafc" text-anchor="middle" letter-spacing="1">OPERATING SYSTEM PLATFORMS MATRIX</text>
  <text x="450" y="60" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Tailored for Specific Hardware Architectures and Usage Contexts</text>

  <!-- Quadrant 1: Desktop Operating Systems -->
  <g transform="translate(45, 80)">
    <rect width="385" height="210" rx="12" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect x="0" y="0" width="385" height="36" rx="10" fill="#1d4ed8"/>
    <text x="20" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">A. DESKTOP &amp; LAPTOP OS</text>
    <rect x="290" y="6" width="80" height="24" rx="12" fill="#1e40af"/>
    <text x="330" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#93c5fd" text-anchor="middle">Workstations</text>
    
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60a5fa">Primary Input:</text>
    <text x="120" y="65" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Keyboard, Mouse, Touchpad, Multi-Screen</text>
    
    <text x="20" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60a5fa">Core Focus:</text>
    <text x="120" y="95" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Heavy Multitasking, Productivity, File Systems</text>
    
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60a5fa">Key Examples:</text>
    <text x="120" y="125" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Microsoft Windows (10/11)  &#x2022; Apple macOS</text>
    <text x="120" y="145" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Linux (Ubuntu, Fedora - Open Source)</text>
    
    <rect x="20" y="165" width="345" height="32" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="192" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Best for: School labs, offices, software development, creative design</text>
  </g>

  <!-- Quadrant 2: Mobile Operating Systems -->
  <g transform="translate(470, 80)">
    <rect width="385" height="210" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="385" height="36" rx="10" fill="#047857"/>
    <text x="20" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">B. MOBILE OPERATING SYSTEMS</text>
    <rect x="290" y="6" width="80" height="24" rx="12" fill="#065f46"/>
    <text x="330" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#6ee7b7" text-anchor="middle">Handheld</text>
    
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">Primary Input:</text>
    <text x="120" y="65" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Capacitive Touchscreen, Voice, GPS, Gyro</text>
    
    <text x="20" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">Core Focus:</text>
    <text x="120" y="95" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Portability, Battery Life, Cellular &amp; App Sandbox</text>
    
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34d399">Key Examples:</text>
    <text x="120" y="125" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Google Android (Open Source / Broad OEM)</text>
    <text x="120" y="145" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Apple iOS (Exclusive to iPhones / iPads)</text>
    
    <rect x="20" y="165" width="345" height="32" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="192" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Best for: Smartphones, tablets, portable communication</text>
  </g>

  <!-- Quadrant 3: Server Operating Systems -->
  <g transform="translate(45, 310)">
    <rect width="385" height="210" rx="12" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <rect x="0" y="0" width="385" height="36" rx="10" fill="#6d28d9"/>
    <text x="20" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">C. SERVER OPERATING SYSTEMS</text>
    <rect x="290" y="6" width="80" height="24" rx="12" fill="#5b21b6"/>
    <text x="330" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#c4b5fd" text-anchor="middle">Network</text>
    
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#a78bfa">Primary Input:</text>
    <text x="120" y="65" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Remote Network SSH, Command Line (CLI)</text>
    
    <text x="20" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#a78bfa">Core Focus:</text>
    <text x="120" y="95" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">99.999% Uptime, Multi-User Concurrency &amp; Security</text>
    
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#a78bfa">Key Examples:</text>
    <text x="120" y="125" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Red Hat Enterprise Linux (RHEL), Ubuntu Server</text>
    <text x="120" y="145" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Windows Server (Active Directory, IIS)</text>
    
    <rect x="20" y="165" width="345" height="32" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="192" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Best for: Cloud data centers, school portals, hospital EHR databases</text>
  </g>

  <!-- Quadrant 4: Embedded / Dedicated OS -->
  <g transform="translate(470, 310)">
    <rect width="385" height="210" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="385" height="36" rx="10" fill="#b45309"/>
    <text x="20" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">D. EMBEDDED &amp; DEDICATED OS</text>
    <rect x="290" y="6" width="80" height="24" rx="12" fill="#78350f"/>
    <text x="330" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fde68a" text-anchor="middle">Specialized</text>
    
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#fbbf24">Primary Input:</text>
    <text x="120" y="65" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Hardware Keypads, Sensors, Fixed Touch Screen</text>
    
    <text x="20" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#fbbf24">Core Focus:</text>
    <text x="120" y="95" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Instant Response, Locked App Environment, Zero Lag</text>
    
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#fbbf24">Key Examples:</text>
    <text x="120" y="125" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Embedded Linux, VxWorks, Android Automotive</text>
    <text x="120" y="145" font-family="system-ui, sans-serif" font-size="12" fill="#fde68a">&#x2022; Supermarket POS Terminals &amp; Bank ATMs</text>
    
    <rect x="20" y="165" width="345" height="32" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="192" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Best for: ATMs, smart TVs, cash registers, traffic lights, medical monitors</text>
  </g>

  <!-- Bottom Legend -->
  <text x="450" y="542" font-family="system-ui, sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Rule of Thumb: Hardware constraints (RAM, CPU, Power) dictate the type of Operating System chosen.</text>
</svg>"""


SVG_GUI_CLI_COMPARISON = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 560" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
  </defs>

  <rect width="900" height="560" rx="16" fill="url(#bgGrad4)"/>
  <rect x="2" y="2" width="896" height="556" rx="14" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="450" y="38" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#f8fafc" text-anchor="middle" letter-spacing="1">OPERATING SYSTEM USER INTERFACES</text>
  <text x="450" y="60" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Graphical User Interface (GUI) vs Command Line Interface (CLI) vs Menu-Driven</text>

  <!-- Left Column: GUI Interface -->
  <g transform="translate(45, 80)">
    <rect width="385" height="340" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
    <rect x="0" y="0" width="385" height="36" rx="10" fill="#0369a1"/>
    <text x="20" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">GRAPHICAL USER INTERFACE (GUI)</text>
    <rect x="295" y="6" width="75" height="24" rx="12" fill="#075985"/>
    <text x="332" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#7dd3fc" text-anchor="middle">WIMP</text>
    
    <!-- GUI Window Mockup -->
    <g transform="translate(20, 50)">
      <rect width="345" height="150" rx="8" fill="#0f172a" stroke="#334155"/>
      <!-- Window Title Bar -->
      <rect width="345" height="26" rx="6" fill="#1e293b"/>
      <circle cx="15" cy="13" r="4.5" fill="#ef4444"/>
      <circle cx="28" cy="13" r="4.5" fill="#f59e0b"/>
      <circle cx="41" cy="13" r="4.5" fill="#10b981"/>
      <text x="172" y="17" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">File Explorer - Senior School ICT</text>
      
      <!-- Visual Icons -->
      <g transform="translate(20, 45)">
        <rect width="40" height="32" rx="4" fill="#f59e0b"/>
        <path d="M 0 6 L 15 6 L 20 12 L 40 12 L 40 32 L 0 32 Z" fill="#d97706"/>
        <text x="20" y="46" font-family="system-ui, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Topic3_OS</text>
      </g>
      <g transform="translate(85, 45)">
        <rect width="40" height="32" rx="4" fill="#3b82f6"/>
        <text x="20" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">DOC</text>
        <text x="20" y="46" font-family="system-ui, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Notes.docx</text>
      </g>
      <g transform="translate(150, 45)">
        <rect width="40" height="32" rx="4" fill="#10b981"/>
        <text x="20" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">PNG</text>
        <text x="20" y="46" font-family="system-ui, sans-serif" font-size="9" fill="#e2e8f0" text-anchor="middle">Chart.png</text>
      </g>
      
      <!-- Mouse Cursor Icon -->
      <polygon points="120,95 120,115 125,110 132,118 135,116 128,107 134,107" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
      <text x="20" y="135" font-family="system-ui, sans-serif" font-size="10" fill="#38bdf8">&#x25B6; Windows, Icons, Menus &amp; Pointers (WIMP)</text>
    </g>

    <!-- GUI Characteristics -->
    <text x="20" y="225" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#38bdf8">&#x2714; Highly intuitive &amp; easy for beginners</text>
    <text x="20" y="245" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">&#x2714; Visual drag-and-drop feedback</text>
    <text x="20" y="270" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#f87171">&#x2716; High RAM &amp; CPU consumption</text>
    <text x="20" y="290" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">&#x2716; Slow for repetitive batch tasks (e.g. 500 files)</text>
    <text x="20" y="320" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Used in: Windows 11 Desktop, Apple macOS, Android</text>
  </g>

  <!-- Right Column: CLI Interface -->
  <g transform="translate(470, 80)">
    <rect width="385" height="340" rx="12" fill="#1e293b" stroke="#059669" stroke-width="2"/>
    <rect x="0" y="0" width="385" height="36" rx="10" fill="#047857"/>
    <text x="20" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#ffffff">COMMAND LINE INTERFACE (CLI)</text>
    <rect x="295" y="6" width="75" height="24" rx="12" fill="#065f46"/>
    <text x="332" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#6ee7b7" text-anchor="middle">Shell / Text</text>
    
    <!-- CLI Terminal Mockup -->
    <g transform="translate(20, 50)">
      <rect width="345" height="150" rx="8" fill="#000000" stroke="#334155"/>
      <!-- Terminal Header -->
      <rect width="345" height="22" rx="6" fill="#111827"/>
      <text x="15" y="15" font-family="monospace" font-size="10" fill="#9ca3af">bash - 80x24</text>
      
      <!-- Terminal Commands -->
      <text x="15" y="45" font-family="monospace" font-size="11" fill="#4ade80">student@vlearn:~$ <tspan fill="#ffffff">mkdir Senior_School</tspan></text>
      <text x="15" y="65" font-family="monospace" font-size="11" fill="#4ade80">student@vlearn:~$ <tspan fill="#ffffff">cd Senior_School &amp;&amp; ls -la</tspan></text>
      <text x="15" y="85" font-family="monospace" font-size="10" fill="#9ca3af">drwxr-xr-x 2 student student 4096 Aug 31 10:00 .</text>
      <text x="15" y="100" font-family="monospace" font-size="10" fill="#9ca3af">-rw-r--r-- 1 student student 1024 Aug 31 10:05 Notes.txt</text>
      <text x="15" y="125" font-family="monospace" font-size="11" fill="#4ade80">student@vlearn:~/Senior_School$ <tspan fill="#ffffff">_</tspan></text>
    </g>

    <!-- CLI Characteristics -->
    <text x="20" y="225" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#4ade80">&#x2714; Incredibly fast with near-zero RAM usage</text>
    <text x="20" y="245" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">&#x2714; Powerful batch scripting &amp; automation</text>
    <text x="20" y="270" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#f87171">&#x2716; Steep learning curve (commands memorized)</text>
    <text x="20" y="290" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">&#x2716; Strict syntax: typo causes execution failure</text>
    <text x="20" y="320" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Used in: Linux Bash, Windows PowerShell, Cloud Servers</text>
  </g>

  <!-- Bottom Strip: Menu-Driven Interface (ATMs / USSD) -->
  <g transform="translate(45, 435)">
    <rect width="810" height="95" rx="10" fill="#1e293b" stroke="#7c3aed" stroke-width="1.5"/>
    <rect x="0" y="0" width="8" height="95" rx="4" fill="#8b5cf6"/>
    <text x="25" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#c084fc">C. MENU-DRIVEN INTERFACES (Safe &amp; Restricted Selection)</text>
    <text x="25" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Presents users with numbered, pre-defined options. Users cannot type custom commands, eliminating user syntax errors entirely.</text>
    <rect x="25" y="58" width="760" height="26" rx="4" fill="#0f172a"/>
    <text x="40" y="75" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fde68a">ATM Display Example: <tspan fill="#ffffff">1. Withdraw Cash   2. Check Account Balance   3. Mini-Statement   4. Change PIN</tspan></text>
  </g>
</svg>"""


SVG_FILE_SYSTEM_TREE = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 560" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e1a"/>
      <stop offset="100%" stop-color="#172033"/>
    </linearGradient>
  </defs>

  <rect width="900" height="560" rx="16" fill="url(#bgGrad5)"/>
  <rect x="2" y="2" width="896" height="556" rx="14" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="450" y="38" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#f8fafc" text-anchor="middle" letter-spacing="1">HIERARCHICAL FILE SYSTEM ARCHITECTURE</text>
  <text x="450" y="60" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Root Directories, Folders, Subfolders, File Extensions &amp; File Paths</text>

  <!-- Top Path Bar -->
  <g transform="translate(45, 80)">
    <rect width="810" height="42" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="15" y="26" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60a5fa">FILE PATH:</text>
    <rect x="95" y="8" width="700" height="26" rx="4" fill="#0f172a"/>
    <text x="110" y="25" font-family="monospace" font-size="12" fill="#fde68a">C:\ <tspan fill="#94a3b8">Senior_School \ </tspan><tspan fill="#38bdf8">ICT_Term_3 \ </tspan><tspan fill="#4ade80">OperatingSystems_Notes.txt</tspan></text>
  </g>

  <!-- Directory Tree Diagram -->
  <g transform="translate(45, 140)">
    <!-- Root Drive C:\ -->
    <g transform="translate(30, 10)">
      <rect width="180" height="40" rx="8" fill="#1d4ed8" stroke="#60a5fa" stroke-width="2"/>
      <!-- HDD Icon -->
      <rect x="12" y="10" width="20" height="20" rx="3" fill="#ffffff"/>
      <circle cx="22" cy="20" r="4" fill="#1d4ed8"/>
      <text x="42" y="25" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#ffffff">Local Disk (C:\)</text>
      <text x="42" y="35" font-family="system-ui, sans-serif" font-size="9" fill="#bfdbfe">Root Directory</text>
    </g>

    <!-- Branch Lines from Root -->
    <path d="M 120 50 L 120 90 L 170 90" stroke="#3b82f6" stroke-width="2" fill="none"/>
    <path d="M 120 50 L 120 310 L 170 310" stroke="#3b82f6" stroke-width="2" fill="none"/>

    <!-- Parent Folder: Senior_School -->
    <g transform="translate(170, 70)">
      <rect width="210" height="42" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
      <rect x="10" y="8" width="26" height="26" rx="4" fill="#d97706"/>
      <text x="14" y="24" font-family="system-ui, sans-serif" font-size="14" fill="#ffffff">&#x1F4C1;</text>
      <text x="45" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#fef3c7">Senior_School</text>
      <text x="150" y="25" font-family="system-ui, sans-serif" font-size="10" fill="#fbbf24">[Parent]</text>
    </g>

    <!-- Sub-Branches from Senior_School -->
    <path d="M 275 112 L 275 155 L 320 155" stroke="#f59e0b" stroke-width="1.8" fill="none"/>
    <path d="M 275 112 L 275 220 L 320 220" stroke="#f59e0b" stroke-width="1.8" fill="none"/>

    <!-- Subfolder 1: Mathematics -->
    <g transform="translate(320, 135)">
      <rect width="180" height="38" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <text x="12" y="24" font-family="system-ui, sans-serif" font-size="12" fill="#f59e0b">&#x1F4C1;</text>
      <text x="35" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#e2e8f0">Mathematics</text>
    </g>
    <!-- File inside Math -->
    <path d="M 410 173 L 410 190 L 440 190" stroke="#64748b" stroke-width="1.5" fill="none"/>
    <g transform="translate(440, 175)">
      <rect width="160" height="30" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
      <text x="10" y="19" font-family="monospace" font-size="11" fill="#fca5a5">Formulae.pdf</text>
      <rect x="115" y="5" width="38" height="20" rx="3" fill="#7f1d1d"/>
      <text x="134" y="18" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#fca5a5" text-anchor="middle">.pdf</text>
    </g>

    <!-- Subfolder 2: ICT_Term_3 (Target) -->
    <g transform="translate(320, 200)">
      <rect width="180" height="38" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="12" y="24" font-family="system-ui, sans-serif" font-size="12" fill="#38bdf8">&#x1F4C2;</text>
      <text x="35" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#38bdf8">ICT_Term_3</text>
    </g>

    <!-- Files inside ICT_Term_3 -->
    <path d="M 410 238 L 410 260 L 440 260" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
    <path d="M 410 238 L 410 295 L 440 295" stroke="#38bdf8" stroke-width="1.5" fill="none"/>

    <g transform="translate(440, 245)">
      <rect width="260" height="30" rx="4" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
      <text x="10" y="20" font-family="monospace" font-size="11" fill="#86efac">OperatingSystems_Notes.txt</text>
      <rect x="215" y="5" width="38" height="20" rx="3" fill="#14532d"/>
      <text x="234" y="18" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#86efac" text-anchor="middle">.txt</text>
    </g>

    <g transform="translate(440, 280)">
      <rect width="260" height="30" rx="4" fill="#0f172a" stroke="#3b82f6" stroke-width="1"/>
      <text x="10" y="20" font-family="monospace" font-size="11" fill="#93c5fd">Architecture_Diagram.png</text>
      <rect x="215" y="5" width="38" height="20" rx="3" fill="#1e3a8a"/>
      <text x="234" y="18" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#93c5fd" text-anchor="middle">.png</text>
    </g>

    <!-- Other Root Subfolder: Windows / Program Files -->
    <g transform="translate(170, 290)">
      <rect width="210" height="40" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <text x="12" y="25" font-family="system-ui, sans-serif" font-size="13" fill="#64748b">&#x1F4C1;</text>
      <text x="40" y="25" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8">Windows (System Files)</text>
    </g>
  </g>

  <!-- Extension Guide Legend Box on Right -->
  <g transform="translate(680, 80)">
    <rect width="175" height="150" rx="8" fill="#1e293b" stroke="#475569"/>
    <text x="87" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#f8fafc" text-anchor="middle">Common Extensions</text>
    <line x1="10" y1="30" x2="165" y2="30" stroke="#334155"/>
    <text x="15" y="50" font-family="system-ui, sans-serif" font-size="11" fill="#93c5fd"><tspan font-weight="700">.docx</tspan> : Word Doc</text>
    <text x="15" y="72" font-family="system-ui, sans-serif" font-size="11" fill="#fca5a5"><tspan font-weight="700">.pdf</tspan>  : Acrobat Doc</text>
    <text x="15" y="94" font-family="system-ui, sans-serif" font-size="11" fill="#86efac"><tspan font-weight="700">.txt</tspan>  : Plain Text</text>
    <text x="15" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#c084fc"><tspan font-weight="700">.png</tspan>  : Raster Image</text>
    <text x="15" y="138" font-family="system-ui, sans-serif" font-size="11" fill="#fde68a"><tspan font-weight="700">.mp3</tspan>  : Audio File</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="45" y="505" width="810" height="35" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="450" y="527" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan fill="#f59e0b" font-weight="700">&#x26A0; Warning:</tspan> Renaming a file without its extension can prevent the OS from recognizing the correct application.</text>
</svg>"""


SVG_THREE_SHIELDS_SECURITY = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 560" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050a14"/>
      <stop offset="50%" stop-color="#0c1322"/>
      <stop offset="100%" stop-color="#161f30"/>
    </linearGradient>
  </defs>

  <rect width="900" height="560" rx="16" fill="url(#bgGrad6)"/>
  <rect x="2" y="2" width="896" height="556" rx="14" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="450" y="38" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#f8fafc" text-anchor="middle" letter-spacing="1">THE 3 SHIELDS OF OPERATING SYSTEM SECURITY</text>
  <text x="450" y="60" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Protecting Digital Information Against Loss, Theft &amp; Unauthorized Modification</text>

  <!-- Shield 1: Access Controls & Strong Passwords -->
  <g transform="translate(45, 85)">
    <rect width="250" height="420" rx="12" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="40" rx="10" fill="#0891b2"/>
    <text x="125" y="26" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">SHIELD 1</text>
    
    <!-- Shield Emblem Icon -->
    <g transform="translate(95, 55)">
      <polygon points="30,0 60,10 60,40 30,60 0,40 0,10" fill="#0e7490" stroke="#22d3ee" stroke-width="2"/>
      <!-- Keyhole -->
      <circle cx="30" cy="25" r="5" fill="#ffffff"/>
      <polygon points="28,25 32,25 34,42 26,42" fill="#ffffff"/>
    </g>

    <text x="125" y="145" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#22d3ee" text-anchor="middle">User Access Control</text>
    <text x="125" y="165" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#a5f3fc" text-anchor="middle">&amp; Strong Passwords</text>

    <!-- Details -->
    <g transform="translate(20, 185)">
      <text x="0" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">&#x25C6; Multi-User Accounts:</text>
      <text x="10" y="32" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Isolates each user's files and desktop environment.</text>
      
      <text x="0" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">&#x25C6; Strong Password Rules:</text>
      <text x="10" y="82" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Minimum 8–12 characters</text>
      <text x="10" y="98" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Uppercase, lowercase, numbers</text>
      <text x="10" y="114" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; Special symbols (@, #, $)</text>
      
      <text x="0" y="145" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">&#x25C6; UAC Prompts:</text>
      <text x="10" y="162" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Admin confirmation before software installation.</text>
    </g>

    <rect x="15" y="375" width="220" height="28" rx="6" fill="#083344"/>
    <text x="125" y="393" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#22d3ee" text-anchor="middle">Prevents Unauthorized Login</text>
  </g>

  <!-- Shield 2: File Permissions (Read / Write / Execute) -->
  <g transform="translate(325, 85)">
    <rect width="250" height="420" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="40" rx="10" fill="#d97706"/>
    <text x="125" y="26" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">SHIELD 2</text>
    
    <!-- Shield Emblem Icon -->
    <g transform="translate(95, 55)">
      <polygon points="30,0 60,10 60,40 30,60 0,40 0,10" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>
      <!-- Sliders / Perms -->
      <rect x="15" y="20" width="30" height="4" rx="2" fill="#ffffff"/>
      <circle cx="22" cy="22" r="4" fill="#ffffff"/>
      <rect x="15" y="32" width="30" height="4" rx="2" fill="#ffffff"/>
      <circle cx="38" cy="34" r="4" fill="#ffffff"/>
    </g>

    <text x="125" y="145" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#fbbf24" text-anchor="middle">File Permissions</text>
    <text x="125" y="165" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#fde68a" text-anchor="middle">&amp; Attribute Controls</text>

    <!-- Details -->
    <g transform="translate(20, 185)">
      <text x="0" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fef3c7">&#x25C6; Read-Only (R):</text>
      <text x="10" y="32" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Users can view data, but cannot edit, overwrite or delete.</text>
      
      <text x="0" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fef3c7">&#x25C6; Write / Modify (W):</text>
      <text x="10" y="82" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Users can edit, save changes, and delete files.</text>
      
      <text x="0" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fef3c7">&#x25C6; Execute (X):</text>
      <text x="10" y="132" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Allows running executable scripts.</text>
      
      <text x="0" y="155" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#fef3c7">&#x25C6; No Access / Hidden:</text>
      <text x="10" y="172" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Completely blocks folder visibility.</text>
    </g>

    <rect x="15" y="375" width="220" height="28" rx="6" fill="#451a03"/>
    <text x="125" y="393" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#fbbf24" text-anchor="middle">Prevents Data Modification</text>
  </g>

  <!-- Shield 3: Automated Redundant Backups -->
  <g transform="translate(605, 85)">
    <rect width="250" height="420" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="40" rx="10" fill="#059669"/>
    <text x="125" y="26" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">SHIELD 3</text>
    
    <!-- Shield Emblem Icon -->
    <g transform="translate(95, 55)">
      <polygon points="30,0 60,10 60,40 30,60 0,40 0,10" fill="#047857" stroke="#34d399" stroke-width="2"/>
      <!-- Cloud Arrow -->
      <path d="M 22 35 C 18 35 15 32 15 28 C 15 24 18 22 22 22 C 23 18 27 15 32 15 C 37 15 41 18 42 22 C 45 22 48 24 48 28 C 48 32 45 35 42 35 Z" fill="#ffffff"/>
      <path d="M 32 40 L 32 28 M 28 32 L 32 28 L 36 32" stroke="#047857" stroke-width="2" stroke-linecap="round"/>
    </g>

    <text x="125" y="145" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#34d399" text-anchor="middle">Automated Backups</text>
    <text x="125" y="165" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#a7f3d0" text-anchor="middle">&amp; Redundancy</text>

    <!-- Details -->
    <g transform="translate(20, 185)">
      <text x="0" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#d1fae5">&#x25C6; The 3-2-1 Rule:</text>
      <text x="10" y="32" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; <tspan font-weight="700" fill="#ffffff">3</tspan> total copies of data</text>
      <text x="10" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; <tspan font-weight="700" fill="#ffffff">2</tspan> different media (SSD + USB)</text>
      <text x="10" y="64" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">&#x2022; <tspan font-weight="700" fill="#ffffff">1</tspan> offsite in Cloud storage</text>
      
      <text x="0" y="95" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#d1fae5">&#x25C6; Built-In OS Utilities:</text>
      <text x="10" y="112" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Windows File History &amp; Backup</text>
      <text x="10" y="128" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">macOS Time Machine snapshot</text>
      
      <text x="0" y="155" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#d1fae5">&#x25C6; Cloud Sync:</text>
      <text x="10" y="172" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Google Drive, OneDrive sync.</text>
    </g>

    <rect x="15" y="375" width="220" height="28" rx="6" fill="#064e3b"/>
    <text x="125" y="393" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#34d399" text-anchor="middle">Protects Against Drive Failure</text>
  </g>

  <!-- Bottom Summary Note -->
  <text x="450" y="535" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1" text-anchor="middle">Combined Defense: Strong Passwords prevent intrusion, Permissions prevent tampering, and Backups survive disaster.</text>
</svg>"""


# =============================================================================
# TOPIC 3 STRUCTURED LESSONS DEFINITIONS (6 LESSONS, 5 PAGES EACH)
# =============================================================================

TOPIC_3_LESSONS = [
    # =========================================================================
    # LESSON 1: Definition and Importance of Operating Systems (Unit Order 1)
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Definition and Importance of Operating Systems",
        "unit_description": "Understanding operating systems as the vital conductor and intermediary interface between hardware, applications, and users.",
        "lesson_title": "Definition and Importance of Operating Systems",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Computer Hardware and Software Integration",
                    "content": {
                        "title": "Computer Hardware System Awaiting Software Orchestration",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Motherboard_with_components.jpg/800px-Motherboard_with_components.jpg",
                        "caption": "A modern computer motherboard with CPU, RAM slots, and interface controllers—a powerful collection of hardware circuits that remains inoperable without an Operating System to coordinate execution.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Orchestra Conductor of the Digital World",
                    "content": {
                        "text": "Imagine entering a grand concert hall where an orchestra is about to perform. You see violins, cellos, flutes, trumpets, and drums. If every musician played whatever they wanted whenever they felt like it, the result would be chaotic noise.\n\nTo make beautiful music, the orchestra needs a **conductor**. The conductor signals the violinists when to start, tells the drummers when to play softly, and ensures every section plays in perfect harmony.\n\nIn a computer or smartphone, the hardware components—such as the processor, RAM, solid-state drive, screen, and keyboard—are the musicians. Without a conductor, they cannot coordinate. The **Operating System (OS)** is that conductor. It coordinates all physical parts of your device so they work together to run your favorite applications and games smoothly."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3.1.1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define an Operating System (OS) and explain why it is classified as system software\n- Distinguish between system software, application software, and hardware\n- Describe the intermediary role of the OS in translating user commands to machine operations\n- Explain why computers cannot run application programs without an installed operating system\n- Understand resource allocation across competing active tasks"
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Operating System (OS)",
                    "content": {
                        "term": "Operating System (OS)",
                        "definition": "The primary system software that manages a computer's hardware and software resources.",
                        "simple_explanation": "The main program that runs on your device, allowing you to interact with the computer and letting other apps run.",
                        "technical_meaning": "A low-level system platform that acts as an intermediary interface between computer hardware, application software, and the user.",
                        "example": "Microsoft Windows 11, Apple macOS, Ubuntu Linux, Google Android, or Apple iOS."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "System Software vs Application Software",
                    "content": {
                        "term": "System Software vs Application Software",
                        "definition": "System software controls basic computer operations, while application software performs specific user tasks.",
                        "simple_explanation": "System software makes the computer work in the background; application software consists of the apps you open to do work or have fun.",
                        "technical_meaning": "System software provides the runtime platform, kernel scheduling, and hardware drivers; application software consists of user-facing programs built on top of OS system calls.",
                        "example": "Operating System & Device Drivers (System Software) vs Google Chrome, Microsoft Word & WhatsApp (Application Software)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Ultimate Intermediary and Translator",
                    "content": {
                        "text": "When you open an app like a web browser, you see a friendly screen where you can type search terms and click buttons. However, the computer's CPU does not understand 'buttons' or 'websites'—it only understands binary electrical pulses (ones and zeros).\n\nThe operating system acts as a multi-tier translator:\n\n1. **For the User**: It provides an intuitive interface (such as a desktop with icons or a mobile touchscreen) so you never need to type machine code to use your device.\n2. **For Applications**: When an application wants to print a document or display an image, it requests the OS ('Please print this document'), and the OS handles all peripheral communication.\n3. **For Hardware**: The OS manages physical circuits, sending electrical signals to start the printer or render display pixels.\n\nWithout an operating system, computer hardware is just an uncoordinated pile of metal, plastic, and silicon chips unable to run any software."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Computer System Architectural Layers",
                    "content": {
                        "title": "The 4-Layer Computer System Architecture",
                        "caption": "Concentric layer diagram illustrating how users interact with applications, applications communicate with the Operating System, and the OS manages physical hardware.",
                        "svg_content": SVG_COMPUTER_SYSTEM_LAYERS
                    }
                },
                {
                    "type": "step_process",
                    "title": "The Communication Pipeline: From User Click to Hardware Execution",
                    "content": {
                        "intro": "How an action flows through all four layers of the computer system when saving a document:",
                        "steps": [
                            {"title": "1. User Action (Layer 1)", "description": "The user clicks the 'Save' icon in a word processing program or presses Ctrl+S."},
                            {"title": "2. Application Request (Layer 2)", "description": "The word processor creates a standardized write request and passes it to the Operating System via a system call."},
                            {"title": "3. OS Translation & Scheduling (Layer 3)", "description": "The Operating System checks disk space, verifies file permissions, locates free physical clusters, and schedules the write operation."},
                            {"title": "4. Hardware Execution (Layer 4)", "description": "The OS storage driver sends electrical signals to the SSD/HDD storage controller to commit the binary bits to non-volatile memory permanently."}
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Purchasing Hardware Without an OS",
                    "content": {
                        "title": "The 'FreeDOS / No OS' Laptop Dilemma",
                        "text": "Computer retailers frequently sell laptops with powerful specifications (e.g. Intel Core i7, 16GB RAM, 1TB SSD) at a lower price labeled 'FreeDOS' or 'No OS Installed'. If a student buys this computer expecting to start writing school projects immediately, the computer will only display a blank command prompt upon booting. Application programs (like office suites and browsers) cannot be installed until a full operating system (such as Windows 11 or Ubuntu Linux) is properly installed and configured."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Common Misconception: 'Web Apps Don't Need an OS'",
                    "content": {
                        "misconception": "Because modern cloud applications (like Google Docs or Canva) run inside a web browser, our digital devices no longer need an operating system.",
                        "correction": "Web browsers are application software. They rely entirely on the local operating system to access Wi-Fi hardware, allocate RAM, draw graphics on the display panel, and receive keyboard/mouse input events."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting Unresponsive and Frozen Devices",
                    "content": {
                        "mistake": "Repeatedly clicking or tapping on a frozen screen when an app stops responding, which overwhelms the OS event queue.",
                        "fix": "Allow the OS a few seconds to process background memory paging. If completely frozen, press Ctrl+Shift+Esc (Windows) to open Task Manager and end the frozen task, or hold down the physical power button for 10 seconds to force a hardware reboot."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: The Core Role of an Operating System",
                    "content": {
                        "question": "Which of the following acts as the primary intermediary bridge between computer hardware and application software?",
                        "options": [
                            "The Web Browser",
                            "The Operating System",
                            "The Word Processor",
                            "The Computer Keyboard"
                        ],
                        "correct": "B",
                        "explanation": "The Operating System manages physical hardware resources and provides a stable runtime platform for application software to run."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: System Software vs Application Software",
                    "content": {
                        "question": "Which of the following is classified as System Software rather than Application Software?",
                        "options": [
                            "Microsoft Word",
                            "Google Chrome",
                            "Linux Ubuntu Kernel & Device Drivers",
                            "WhatsApp Desktop"
                        ],
                        "correct": "C",
                        "explanation": "Linux Ubuntu and its device drivers are System Software that operate and manage computer hardware, whereas Word, Chrome, and WhatsApp are Application Software."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Crash Course Computer Science: Operating Systems",
                    "content": {
                        "title": "Introduction to Operating Systems",
                        "youtube_id": "26QPDBe-NB8",
                        "url": "https://www.youtube.com/watch?v=26QPDBe-NB8",
                        "description": "An engaging overview of what an operating system is, how it evolved to prevent software conflicts, and how it manages hardware resources."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3.1.1 Summary Takeaways",
                    "content": {
                        "text": "1. **Conductor Role**: The Operating System is the primary system software that coordinates all hardware and software components.\n2. **4-Layer Architecture**: User -> Application Software -> Operating System -> Physical Hardware.\n3. **Resource Manager**: The OS translates high-level requests into binary operations, manages device drivers, and allocates CPU and memory to running programs."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Functions of an Operating System (Unit Order 2)
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Functions of an Operating System",
        "unit_description": "The core functions of an OS including processor scheduling, memory management, device control, file organization, and security.",
        "lesson_title": "Functions of an Operating System",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Processor and Memory Coordination",
                    "content": {
                        "title": "High-Speed Processor and RAM Modules on Motherboard",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/RAM_module_SDRAM_1GB.jpg/800px-RAM_module_SDRAM_1GB.jpg",
                        "caption": "High-speed RAM modules and multi-core CPU hardware on a motherboard, actively managed by the operating system during multitasking.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Master Coordinator: Like a School Principal",
                    "content": {
                        "text": "Think of a busy school principal's office. At any given moment, the principal has to sign official letters, answer phone calls, meet parents, coordinate teachers, and allocate classrooms. If the principal fails to organize these tasks, the school quickly falls into chaos.\n\nYour computer's operating system does the exact same job, but at lightning speed! It allocates time on the CPU, space in RAM, access to storage, and communication with peripherals so that multiple programs run smoothly at once."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3.1.2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and explain the 5 core functions of an Operating System\n- Explain how processor scheduling enables multitasking on digital devices\n- Describe memory management and how RAM allocation prevents application crashes\n- Explain the role of device drivers in input/output device management\n- Analyze system diagnostics (e.g. Task Manager / Activity Monitor) to optimize performance"
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Processor & Memory Management",
                    "content": {
                        "term": "Processor & Memory Management",
                        "definition": "The core OS functions that allocate CPU execution time and temporary RAM storage space to active applications.",
                        "simple_explanation": "Deciding which app gets to use the computer's 'brain' (CPU) and memory (RAM) so that programs run fast and do not crash.",
                        "technical_meaning": "The dynamic scheduling of process threads (CPU time-slicing) and tracking of physical/virtual address spaces in RAM, preventing memory leaks and boundary violations.",
                        "example": "Allowing a music streaming app to play audio in the background while typing an essay in a word processor."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Device Drivers & File Systems",
                    "content": {
                        "term": "Device Drivers & File Systems",
                        "definition": "Software translators that communicate with peripheral hardware and structured directory systems that organize drive storage.",
                        "simple_explanation": "Programs that let your computer talk to printers and keyboards, and the filing system that saves your files neatly.",
                        "technical_meaning": "Kernel modules providing hardware abstraction interfaces for I/O devices, alongside hierarchical metadata index structures for secondary storage.",
                        "example": "Installing a printer driver to print documents, or formatting a drive with NTFS/FAT32."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Five Core Pillars of Operating System Operations",
                    "content": {
                        "text": "The operating system executes five primary management responsibilities simultaneously:\n\n1. **Processor (CPU) Management**: Implements multitasking through rapid time-slicing, switching execution between active programs billions of times per second.\n2. **Memory (RAM) Management**: Allocates distinct memory blocks to each open application. Ensures Application A cannot write into the memory space of Application B.\n3. **Device (I/O) Management**: Uses specialized device drivers to translate standardized OS commands into device-specific electrical signals for printers, mice, and webcams.\n4. **File System Management**: Maintains a master directory tracking file locations, timestamps, access permissions, and storage clusters.\n5. **Security & User Access**: Controls login authentication, user permission boundaries, and safeguards critical system files against unauthorized changes."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Operating System Core Functions Architecture",
                    "content": {
                        "title": "The 5 Core Functions of an Operating System",
                        "caption": "Hub-and-spoke diagram detailing CPU scheduling, RAM management, File organization, Device control, and User security.",
                        "svg_content": SVG_OS_CORE_FUNCTIONS
                    }
                },
                {
                    "type": "step_process",
                    "title": "Investigating System Resource Allocation with Task Manager / Activity Monitor",
                    "content": {
                        "intro": "How to inspect and manage operating system resource allocation on your computer:",
                        "steps": [
                            {"title": "1. Open Resource Monitor", "description": "Press Ctrl + Shift + Esc (Windows) or Cmd + Space, then type 'Activity Monitor' (macOS) to launch the system monitor."},
                            {"title": "2. Inspect CPU Utilization", "description": "Observe the CPU column to see what percentage of processor cycles are allocated to each running process."},
                            {"title": "3. Monitor RAM Allocation", "description": "Check the Memory column to identify how much RAM is occupied by each open application and background service."},
                            {"title": "4. Manage Overloaded Tasks", "description": "Identify unresponsive or high-consumption apps, select the process, and click 'End Task' to safely reclaim system resources."}
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Diagnosing Low Memory and Peripheral Warnings",
                    "content": {
                        "intro": "A student encounters two different system notifications during a digital multimedia class:",
                        "steps": [
                            "**Scenario A — Plug and Play Device Recognition:** The student plugs a USB drawing tablet into the computer. A notification appears: *'Setting up device... Device is ready to use.'* **Function:** Device Management. The OS recognized the hardware ID, loaded the matching device driver into the kernel, and bound it to the input subsystem.",
                            "**Scenario B — Low RAM Alert During Video Rendering:** While editing video with 20 browser tabs open, the OS warns: *'Your system is low on memory.'* **Function:** Memory Management. The physical RAM is fully allocated. The OS began swapping memory to the storage disk (virtual memory/paging) and alerts the user to close unused apps."
                        ]
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Common Misconception: 'Multitasking Means CPU Does Everything Simultaneously'",
                    "content": {
                        "misconception": "A single CPU core literally processes hundreds of applications at the exact same split-nanosecond.",
                        "correction": "On a single CPU core, only one machine instruction executes at any instantaneous moment. The OS creates the illusion of simultaneous multitasking through rapid time-slicing and context switching."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Unplugging Hardware Without Safe Ejection",
                    "content": {
                        "mistake": "Yanking out a USB flash drive or external drive while the OS is still writing buffered data.",
                        "fix": "Always right-click the drive icon and select 'Safely Remove / Eject'. This signals the OS File Management subsystem to flush all temporary write caches in RAM to the physical drive before power is disconnected."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Memory Space Protection",
                    "content": {
                        "question": "When you run multiple applications simultaneously, which OS function ensures they do not overwrite each other's memory space?",
                        "options": [
                            "Device Management",
                            "File System Management",
                            "Memory Management",
                            "User Interface Management"
                        ],
                        "correct": "C",
                        "explanation": "Memory Management establishes isolated memory address boundaries for each running application in RAM to prevent system crashes."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Device Drivers Role",
                    "content": {
                        "question": "What is the primary role of a device driver in an operating system?",
                        "options": [
                            "To design graphic icons on the desktop",
                            "To act as a software translator between the OS and external hardware peripherals",
                            "To format storage drives and delete old files",
                            "To connect the computer to the internet without Wi-Fi"
                        ],
                        "correct": "B",
                        "explanation": "Device drivers are specialized programs that enable the OS to communicate with specific hardware devices such as printers, mice, and webcams."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "How Operating Systems Work & Core Functions",
                    "content": {
                        "title": "Operating System Functions and Resource Allocation",
                        "youtube_id": "pv24_m6n8pE",
                        "url": "https://www.youtube.com/watch?v=pv24_m6n8pE",
                        "description": "Comprehensive breakdown of the 5 key functions of operating systems with clear animated examples."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3.1.2 Summary Takeaways",
                    "content": {
                        "text": "1. **5 Functions**: CPU scheduling, RAM management, Device I/O control, File management, and Security.\n2. **Multitasking**: The OS coordinates CPU time-slices so multiple applications run smoothly.\n3. **Device Drivers**: Act as translators allowing the OS to talk to any brand of peripheral hardware."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Types of Operating Systems (Unit Order 3)
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Types of Operating Systems",
        "unit_description": "Exploring desktop, mobile, server, and embedded operating systems, their characteristics, and practical deployment environments.",
        "lesson_title": "Types of Operating Systems",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Diverse Computing Platforms and Form Factors",
                    "content": {
                        "title": "Various Computing Devices: Laptops, Tablets, and Smartphones",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Various_computing_devices.jpg/800px-Various_computing_devices.jpg",
                        "caption": "From pocket-sized smartphones to multi-monitor desktop workstations and server data centers, diverse devices require specialized operating systems.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Vehicles for Different Terrains",
                    "content": {
                        "text": "Think about the vehicles in your town: motorcycles, personal saloon cars, heavy cargo trucks, and giant buses. They all have engines and wheels, but they are built for entirely different purposes. You would not use a saloon car to transport tons of building stones, nor would you use a massive cargo truck to commute to school.\n\nIn the digital world, different devices need different types of operating systems. A pocket-sized smartphone has very different operating needs compared to a desktop workstation or a massive enterprise banking server."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3.2.1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Categorize operating systems into Desktop, Mobile, Server, and Embedded types\n- Identify leading examples of each OS category (Windows, macOS, Linux, Android, iOS)\n- Compare the architectural focus of mobile devices vs desktop PCs vs network servers\n- Explain the role of embedded operating systems in dedicated devices like ATMs and POS terminals\n- Select the appropriate operating system for specific school, business, and enterprise requirements"
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Desktop vs Mobile Operating Systems",
                    "content": {
                        "term": "Desktop & Mobile Operating Systems",
                        "definition": "Desktop OS powers personal computers with multi-window productivity; Mobile OS is optimized for touchscreen portability and battery efficiency.",
                        "simple_explanation": "Desktop OS is for laptops and PCs with keyboards and mice; Mobile OS is for smartphones and tablets with touchscreens.",
                        "technical_meaning": "Desktop OS supports heavy multitasking, extensive peripherals, and file systems; Mobile OS emphasizes power management, mobile app sandboxing, and touch/sensor input.",
                        "example": "Windows 11, macOS Sonoma, Ubuntu (Desktop) vs Android 14, Apple iOS 17 (Mobile)."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Server vs Embedded Operating Systems",
                    "content": {
                        "term": "Server & Embedded Operating Systems",
                        "definition": "Server OS handles multi-user network services and databases; Embedded OS is built into dedicated appliances to perform specific hardware control.",
                        "simple_explanation": "Server OS runs websites and school databases for hundreds of users; Embedded OS runs smart TVs, microwave ovens, or car dashboards.",
                        "technical_meaning": "Server OS optimizes high-throughput network I/O, concurrency, and headless CLI control; Embedded OS (RTOS) runs in read-only ROM with deterministic, real-time responses.",
                        "example": "Windows Server, Red Hat Enterprise Linux (Server) vs Embedded Linux in Smart TVs or ATMs (Embedded)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Operating System Family Tree",
                    "content": {
                        "text": "Different computing platforms demand distinct design trade-offs:\n\n- **Desktop OS (Windows, macOS, Linux)**: Prioritizes computational power, broad software support, multi-window multitasking, and precise mouse/keyboard input.\n- **Mobile OS (Android, iOS)**: Prioritizes touch gestures, cellular data management, location sensors, power conservation, and secure app-store sandboxing.\n- **Server OS (Windows Server, Linux/RHEL, Ubuntu Server)**: Engineered for 99.999% uptime, multi-user authentication, hosting web services, and remote command-line administration.\n- **Embedded & Dedicated Systems (POS, ATMs, Smart TVs)**: Compact, locked-down operating systems running dedicated applications (e.g. transaction software at a supermarket cash register or bank ATM)."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Operating System Platforms Comparison Matrix",
                    "content": {
                        "title": "The 4 Major Operating System Categories",
                        "caption": "Matrix comparing Desktop, Mobile, Server, and Embedded operating systems by input method, core focus, and primary platforms.",
                        "svg_content": SVG_OS_PLATFORMS_MATRIX
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Operating System Types Comparison",
                    "content": {
                        "headers": ["Category", "Primary Input", "Core Focus", "Leading Examples", "Typical Hardware"],
                        "rows": [
                            ["Desktop OS", "Keyboard & Mouse", "Productivity & Multitasking", "Microsoft Windows, Apple macOS, Ubuntu Linux", "Desktops, Laptops, Workstations"],
                            ["Mobile OS", "Touchscreen & Voice", "Portability & Battery Life", "Google Android, Apple iOS", "Smartphones, Tablets, Smartwatches"],
                            ["Server OS", "Headless CLI / Network", "Multi-user Concurrency & Uptime", "Red Hat Linux, Ubuntu Server, Windows Server", "Enterprise Rack Servers, Cloud Data Centers"],
                            ["Embedded OS", "Sensors, Keypads, Touch", "Real-Time & Dedicated Function", "Embedded Linux, VxWorks, Android TV", "ATMs, POS Terminals, Smart TVs, Appliances"]
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Deployment: Hospital Network vs Supermarket POS",
                    "content": {
                        "title": "Choosing Operating Systems in Community Infrastructure",
                        "text": "In a county referral hospital, doctors and nurses need access to 50,000 Electronic Health Records (EHR). The hospital installs a **Server Operating System** on its central mainframe to manage concurrent database access and data backups. Meanwhile, at the hospital pharmacy, the cash registers run an **Embedded / Dedicated OS** locked to a Point-of-Sale billing app, preventing staff from browsing the internet or installing unauthorized programs."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Common Misconception: 'Linux is Only for Programmers'",
                    "content": {
                        "misconception": "Linux is an obscure, complex operating system that ordinary people never use.",
                        "correction": "Linux is the most widely deployed OS kernel on Earth! Google Android is built on the Linux kernel (running on billions of phones), and the vast majority of the World Wide Web, cloud servers, and supercomputers run on Linux distributions."
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Worked Example: Selecting an OS for a School Computer Lab",
                    "content": {
                        "intro": "A school principal has a budget to equip 30 workstations in the computer laboratory for ICT lessons:",
                        "steps": [
                            "**Requirement 1 — Student Workstations:** Needs an intuitive GUI, compatibility with office software, coding tools, and typing tutors. **Selection:** Desktop OS (Windows 11 or Ubuntu Desktop).",
                            "**Requirement 2 — Central School File Server:** Needs to store all student portfolios, share printers, and manage student network logins. **Selection:** Server OS (Ubuntu Server or Windows Server).",
                            "**Requirement 3 — School Library Tablet Readers:** Lightweight touch devices for digital storybooks. **Selection:** Mobile OS (Android tablets)."
                        ]
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Open-Source Operating Systems",
                    "content": {
                        "question": "Which of the following operating systems is open-source, free to customize, and distributed in versions like Ubuntu, Fedora, and Debian?",
                        "options": [
                            "Microsoft Windows",
                            "Apple macOS",
                            "Linux",
                            "Apple iOS"
                        ],
                        "correct": "C",
                        "explanation": "Linux is an open-source operating system whose source code is freely available for anyone to inspect, modify, and distribute."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Central Server OS Selection",
                    "content": {
                        "question": "What type of operating system should be installed on a central database computer that serves 200 users concurrently over a local school network?",
                        "options": [
                            "Embedded Operating System",
                            "Mobile Operating System",
                            "Server Operating System",
                            "Single-User Desktop OS"
                        ],
                        "correct": "C",
                        "explanation": "Server Operating Systems are specifically designed for multi-user security, high network traffic, and continuous server database services."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Types of Operating Systems Explained",
                    "content": {
                        "title": "Desktop, Mobile, Server, and Embedded Operating Systems",
                        "youtube_id": "9pNgE5_U4v0",
                        "url": "https://www.youtube.com/watch?v=9pNgE5_U4v0",
                        "description": "Clear comparison of the main operating system categories and how hardware constraints shape OS design."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3.2.1 Summary Takeaways",
                    "content": {
                        "text": "1. **4 Categories**: Desktop (Windows/macOS/Linux), Mobile (Android/iOS), Server (Windows Server/Linux Server), Embedded (ATMs/Smart Devices).\n2. **Platform Focus**: Desktop optimizes productivity; Mobile optimizes battery and touch; Server optimizes multi-user uptime.\n3. **Open vs Closed**: Linux and Android offer open-source flexibility; Windows and Apple provide integrated proprietary ecosystems."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Operating System Interfaces (Unit Order 4)
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Operating System Interfaces",
        "unit_description": "Comparing Graphical User Interfaces (GUI), Command Line Interfaces (CLI), and Menu-Driven Interfaces in speed, usability, and resource usage.",
        "lesson_title": "Operating System Interfaces",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Interfaces vs Text Commands",
                    "content": {
                        "title": "Command Line Interface Terminal on Linux Desktop",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Gnome-terminal-screenshot.png/800px-Gnome-terminal-screenshot.png",
                        "caption": "Side-by-side view of a modern desktop GUI with colorful icons next to a high-speed Command Line Interface terminal.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Restaurant Menu vs Speaking to the Chef",
                    "content": {
                        "text": "Imagine you want to order food at a restaurant. There are two ways you could do it:\n\n1. **Method 1 (The Menu)**: The waiter gives you an illustrated menu with pictures of burgers and drinks. You look at the pictures and point to what you want (GUI).\n2. **Method 2 (The Chef)**: There is no menu. You speak directly to the chef using precise culinary terms and exact ingredient measurements (CLI).\n\nMethod 1 is friendly, visual, and intuitive. Method 2 requires technical training but gives you absolute precision and speed. These reflect the two main ways we communicate with computer operating systems!"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3.2.2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define User Interface (UI) and differentiate GUI, CLI, and Menu-Driven interfaces\n- Describe the WIMP paradigm (Windows, Icons, Menus, Pointers) of Graphical User Interfaces\n- Explain the speed, automation, and resource efficiency advantages of Command Line Interfaces\n- Execute basic CLI commands for directory navigation and file creation\n- Choose the most suitable interface type for beginners, power users, and public terminals"
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Graphical User Interface (GUI)",
                    "content": {
                        "term": "Graphical User Interface (GUI)",
                        "definition": "A visual interface utilizing Windows, Icons, Menus, and Pointers (WIMP) to enable user interaction through pointing devices or touch.",
                        "simple_explanation": "An interface where you click on pictures, icons, and menus instead of typing code.",
                        "technical_meaning": "A visual abstraction layer where system commands are triggered by graphical event handlers responding to mouse, stylus, or capacitive touchscreen inputs.",
                        "example": "Double-clicking a folder icon in Windows File Explorer or tapping an app icon on an Android smartphone."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Command Line Interface (CLI)",
                    "content": {
                        "term": "Command Line Interface (CLI)",
                        "definition": "A text-based user interface where users type structured textual commands at a terminal prompt to execute operating system operations.",
                        "simple_explanation": "A black screen where you type exact text commands using your keyboard to instruct the computer.",
                        "technical_meaning": "A shell interpreter (e.g. bash, zsh, PowerShell) that parses text strings into system calls, providing high scriptability with near-zero graphic memory overhead.",
                        "example": "Typing `mkdir Term3_Projects` in Windows Command Prompt or Linux Bash."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Comparing GUI, CLI, and Menu-Driven Interfaces",
                    "content": {
                        "text": "Operating systems offer different user interfaces depending on user expertise and device purpose:\n\n- **GUI (Graphical User Interface)**:\n  - *Strengths*: Highly intuitive, visual feedback, zero command memorization, ideal for general computing and creative work.\n  - *Trade-offs*: High RAM and CPU resource consumption, slower for repetitive batch tasks.\n- **CLI (Command Line Interface)**:\n  - *Strengths*: Incredibly fast, ultra-low resource footprint, powerful scripting and automation (e.g. renaming 1,000 files in one second).\n  - *Trade-offs*: Steep learning curve; syntax errors occur if commands are mistyped.\n- **Menu-Driven Interface**:\n  - *Strengths*: Safe and restricted. Users choose from a numbered list of options (e.g. ATM screens: *1. Withdraw, 2. Check Balance, 3. Mini-Statement*).\n  - *Trade-offs*: Rigid navigation with no ability to execute custom commands."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "GUI vs CLI Architecture & Workflow Comparison",
                    "content": {
                        "title": "Graphical User Interface vs Command Line Interface",
                        "caption": "Comparative architectural diagram showing WIMP visual elements and the text shell execution pipeline.",
                        "svg_content": SVG_GUI_CLI_COMPARISON
                    }
                },
                {
                    "type": "step_process",
                    "title": "Performing Core Tasks: GUI vs CLI Comparison",
                    "content": {
                        "intro": "How identical file management tasks are performed in GUI vs CLI:",
                        "steps": [
                            {"title": "1. Creating a New Folder", "description": "**GUI:** Right-click desktop -> New -> Folder -> Type name.\n**CLI:** Type `mkdir SchoolWork` and press Enter."},
                            {"title": "2. Listing Directory Contents", "description": "**GUI:** Double-click folder to view graphical icons.\n**CLI:** Type `dir` (Windows) or `ls` (Linux/Mac) and press Enter."},
                            {"title": "3. Navigating Directories", "description": "**GUI:** Double-click subfolder icon.\n**CLI:** Type `cd SchoolWork` (Change Directory) and press Enter."},
                            {"title": "4. Batch Renaming 500 Files", "description": "**GUI:** Click each file individually and rename (takes 30+ minutes).\n**CLI:** Run a one-line shell command `ren *.txt *.bak` (takes 0.1 seconds)."}
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Why Cybersecurity and Network Engineers Rely on CLI",
                    "content": {
                        "title": "Command Line Power in Enterprise IT and Cloud Computing",
                        "text": "When managing servers located across the world in cloud data centers (e.g. Amazon Web Services or Microsoft Azure), transmitting a heavy graphical desktop interface over the internet wastes bandwidth and introduces latency. Network administrators and cybersecurity analysts use SSH (Secure Shell) to send lightweight text commands over CLI, managing thousands of remote servers simultaneously with maximum speed and security."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Common Misconception: 'The CLI is Obsolete and Outdated'",
                    "content": {
                        "misconception": "Because GUIs are visually modern, the Command Line is an outdated remnant of the 1970s that is no longer useful.",
                        "correction": "Every major operating system (Windows 11, macOS, Linux) actively develops powerful modern CLI shells (PowerShell, Zsh, Bash). Software developers, data scientists, and cloud architects perform the vast majority of professional engineering work through the command line."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Syntax and Spacing Errors in CLI",
                    "content": {
                        "mistake": "Typing commands without spaces or with incorrect path slashes (e.g. typing `cdSchoolWork` instead of `cd SchoolWork`).",
                        "fix": "Remember that the CLI requires exact syntax. Always include a space between the command name and its argument, and use the Tab key for automatic file/folder path completion."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: WIMP Elements in User Interfaces",
                    "content": {
                        "question": "Which user interface paradigm uses Windows, Icons, Menus, and Pointers (WIMP) as its primary elements?",
                        "options": [
                            "Command Line Interface (CLI)",
                            "Menu-Driven Interface",
                            "Graphical User Interface (GUI)",
                            "Text Terminal Shell"
                        ],
                        "correct": "C",
                        "explanation": "WIMP (Windows, Icons, Menus, Pointers) is the foundational design paradigm of Graphical User Interfaces."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Efficiency and Automation",
                    "content": {
                        "question": "Why do systems administrators prefer Command Line Interfaces (CLI) for managing remote server networks?",
                        "options": [
                            "CLI displays colorful animations",
                            "CLI requires very low system resources and enables powerful script automation",
                            "CLI prevents users from using a keyboard",
                            "CLI is only available on smartphones"
                        ],
                        "correct": "B",
                        "explanation": "CLI uses minimal RAM/bandwidth and allows administrators to automate complex batch tasks through shell scripts."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "GUI vs CLI: Understanding Operating System Interfaces",
                    "content": {
                        "title": "Graphical User Interface vs Command Line Interface",
                        "youtube_id": "bY_9sXFfD6s",
                        "url": "https://www.youtube.com/watch?v=bY_9sXFfD6s",
                        "description": "Demonstrating how GUI and CLI interact with the operating system kernel and when to use each interface."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3.2.2 Summary Takeaways",
                    "content": {
                        "text": "1. **3 Interfaces**: GUI (visual WIMP), CLI (text commands), Menu-Driven (numbered selections).\n2. **GUI**: Intuitive and friendly for everyday users; higher resource overhead.\n3. **CLI**: Ultra-fast, scriptable, and resource-efficient for technical professionals and server administration."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: File and Folder Management (Unit Order 5)
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "File and Folder Management",
        "unit_description": "Organizing digital storage using hierarchical directories, file paths, extensions, and executing file manipulation procedures.",
        "lesson_title": "File and Folder Management",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Physical Storage and Logical Organization",
                    "content": {
                        "title": "Hard Disk Drive Internal Mechanical Platter and Storage Arm",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Hard_disk_drive_storage_mechanism.jpg/800px-Hard_disk_drive_storage_mechanism.jpg",
                        "caption": "Hard disk drive and SSD storage media, where the operating system organizes millions of data sectors into structured files and folders.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Digital School Locker",
                    "content": {
                        "text": "Imagine you have a big physical locker at school. Every day, you receive worksheets, textbooks, drawing pencils, and receipts. If you throw everything into the bottom of the locker in a random pile, you won't be able to find your math homework within a week.\n\nTo stay organized, you place plastic folders in your locker: one labeled 'Mathematics', one labeled 'ICT', and a box for 'Art Supplies'.\n\nA computer's hard drive is a giant digital locker. To keep our files from turning into a chaotic pile, our operating system provides file management tools like **File Explorer** (in Windows) or **Finder** (in macOS)."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3.3.1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define files, folders (directories), file paths, and file extensions\n- Understand hierarchical tree structures and root directories\n- Execute file manipulation procedures: Create, Rename, Copy, Move, Search, and Delete\n- Explain the role of the Recycle Bin / Trash in data recovery\n- Avoid file corruption and extension errors during daily file management"
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "File & Folder (Directory)",
                    "content": {
                        "term": "File & Folder (Directory)",
                        "definition": "A file is a named collection of stored digital data; a folder is a virtual container used to organize and group files.",
                        "simple_explanation": "A file is a single digital document, picture, or song; a folder is a container where you keep related files together.",
                        "technical_meaning": "A file is a discrete byte stream stored on secondary media indexed by metadata; a folder is a directory file containing pointer records to child inodes/files.",
                        "example": "`Project_Report.docx` (File) stored inside `Senior_School_ICT` (Folder)."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "File Path & File Extension",
                    "content": {
                        "term": "File Path & File Extension",
                        "definition": "A file path is the complete hierarchical address of a file; a file extension is the suffix identifying its format and associated application.",
                        "simple_explanation": "The file path is the full roadmap of folders to find your file; the file extension (.docx, .png, .pdf) tells the computer what type of file it is.",
                        "technical_meaning": "The path specifies the absolute directory tree traversal from root; the extension is a metadata tag used by the OS shell to bind MIME types and default application launchers.",
                        "example": "`C:\\Users\\Student\\Documents\\ICT\\LessonNotes.docx` (Path) ending in `.docx` (Extension)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Hierarchical File Systems and Organization",
                    "content": {
                        "text": "Operating systems organize storage using an upside-down tree structure:\n\n1. **Root Directory**: The base of the storage hierarchy (`C:\\` on Windows, `/` on Linux/macOS).\n2. **Parent Folders & Subfolders**: Directories nested within other directories, creating logical grouping (e.g. `SchoolWork` -> `Grade_10` -> `ICT`).\n3. **Files & Metadata**: Each file possesses attributes tracked by the OS: File Name, File Size, File Extension, Date Created, Date Modified, and Author Permissions.\n4. **Copy vs Move (Cut)**:\n   - **Copy**: Creates an identical duplicate file in the target folder while leaving the original untouched.\n   - **Move (Cut)**: Transfers the file to the new destination and removes it from the original location."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Hierarchical File System Directory Tree",
                    "content": {
                        "title": "File System Tree Structure & Path Breakdown",
                        "caption": "Hierarchical diagram showing Root Directory, Parent Folders, Subfolders, Files with extension badges, and the complete File Path.",
                        "svg_content": SVG_FILE_SYSTEM_TREE
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Creating and Organizing a Student Portfolio",
                    "content": {
                        "intro": "Follow this procedure to build an organized folder hierarchy on your desktop:",
                        "steps": [
                            {"title": "1. Create Master Portfolio Folder", "description": "Right-click empty desktop space -> New -> Folder. Type `VLearn_Portfolio` and press Enter."},
                            {"title": "2. Create Topic Subfolders", "description": "Double-click `VLearn_Portfolio` to open it. Right-click inside -> New -> Folder. Create `Topic_3_OS`, `Topic_4_Word`, and `Images`."},
                            {"title": "3. Create and Save a Document", "description": "Open `Topic_3_OS`. Right-click -> New -> Text Document. Name it `lesson_summary.txt`."},
                            {"title": "4. Copy and Backup Files", "description": "Right-click `lesson_summary.txt` -> Copy. Navigate to `VLearn_Portfolio\\Images` -> Right-click -> Paste. Verify you now have two independent copies."},
                            {"title": "5. Search and Locate Files", "description": "Click the search bar in the top-right corner of File Explorer. Type `summary` and press Enter to instantly locate the file across all folders."}
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Practical Activity: Professional File Organization Audit",
                    "content": {
                        "intro": "A student has 200 unorganized files on their desktop named `doc1.docx`, `img_12.jpg`, `essay_final_v2.docx`:",
                        "steps": [
                            "**Step 1 — Establish Consistent Naming Conventions:** Rename files using meaningful dates and subjects (e.g. `2026_09_ICT_Topic3_Summary.docx`). Avoid ambiguous names like `final_final.docx`.",
                            "**Step 2 — Implement Subject-Based Hierarchy:** Create high-level folders for each academic term, with subfolders for each subject and project.",
                            "**Step 3 — Clean Temporary Downloads:** Move completed downloads to appropriate subfolders and delete outdated installation files.",
                            "**Step 4 — Verify File Extensions:** Ensure file extensions remain intact during renaming so applications can open them without errors."
                        ]
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Common Misconception: 'Deleting a File Erases it Instantly from the Hard Drive'",
                    "content": {
                        "misconception": "Clicking Delete immediately destroys the file data forever.",
                        "correction": "The OS moves deleted files to the Recycle Bin (or Trash), allowing instant recovery. Even when emptied from the Recycle Bin, the OS simply marks those drive sectors as 'available for reuse' until overwritten with new data."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: The Double-Extension Error",
                    "content": {
                        "mistake": "Typing `.txt` or `.docx` when renaming a file while Windows is set to 'Hide known file extensions'.",
                        "fix": "The file gets named `Project.docx.docx`. Only type the extension if your operating system view settings are explicitly set to show file name extensions."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Copy vs Cut File Operations",
                    "content": {
                        "question": "When you Copy a file from Folder A and Paste it into Folder B, what is the resulting state of the file?",
                        "options": [
                            "The file is removed from Folder A and appears only in Folder B",
                            "The file exists in both Folder A and Folder B as two separate, identical copies",
                            "A blank shortcut is created in Folder B and the original is deleted",
                            "The file is deleted from both folders"
                        ],
                        "correct": "B",
                        "explanation": "Copying creates an exact duplicate file in the target directory while leaving the original file in the source directory untouched."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: File Extensions",
                    "content": {
                        "question": "Which file extension is standard for Portable Document Format documents?",
                        "options": [
                            ".docx",
                            ".pdf",
                            ".mp3",
                            ".xlsx"
                        ],
                        "correct": "B",
                        "explanation": "The `.pdf` extension represents Portable Document Format files, used for universally readable documents across all operating systems."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "File and Folder Management Best Practices",
                    "content": {
                        "title": "How File Systems Organize and Structure Data",
                        "youtube_id": "KN8YgJnShPM",
                        "url": "https://www.youtube.com/watch?v=KN8YgJnShPM",
                        "description": "A visual guide to mastering folders, subfolders, file extensions, and search indexing."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3.3.1 Summary Takeaways",
                    "content": {
                        "text": "1. **Hierarchy**: Storage is organized in directory trees originating from the Root (`C:\\` or `/`).\n2. **File Paths**: Full addresses specifying exact folder chains to a file.\n3. **File Extensions**: Identify file format and link files to default applications.\n4. **Operations**: Create, Rename, Copy (duplicate), Move (transfer), Search, and Delete (Recycle Bin)."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Implementing Security Control Measures (Unit Order 6)
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Implementing Security Control Measures on Files and Folders",
        "unit_description": "Securing data through file permissions, user access controls, strong password authentication, and external backup strategies.",
        "lesson_title": "Implementing Security Control Measures on Files and Folders",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Securing Digital Assets and Confidential Data",
                    "content": {
                        "title": "Digital Padlock and Security Access Encryption Concept",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Padlock_and_digital_key_concept.jpg/800px-Padlock_and_digital_key_concept.jpg",
                        "caption": "Digital padlock and encrypted network concept, representing access controls, file permissions, and backup protection on operating systems.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Locked Journal and the Safety Photocopy",
                    "content": {
                        "text": "Imagine you keep a personal journal at home. To make sure no one else reads it, you might lock it in a drawer or use a journal with a combination lock. You might also make a photocopy of your most important school notes and keep them at your grandmother's house, just in case a fire or flood damages your room.\n\nIn our computing devices, our files and folders are vulnerable to similar risks: unauthorized access by siblings or hackers, accidental deletion, or drive hardware failure. To protect our digital information, our operating system provides built-in **security control measures**."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3.3.2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the Three Shields of Operating System Security (Access Controls, Permissions, Backups)\n- Configure Read-Only, Write, and Execute file permissions on folders\n- Describe User Access Control (UAC) and multi-user authentication\n- Formulate strong password policies to protect user accounts\n- Implement 3-2-1 backup strategies using external drives and secure cloud storage"
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "File Permissions",
                    "content": {
                        "term": "File Permissions",
                        "definition": "Operating system access rules defining which users or groups can read, modify, or execute specific files and directories.",
                        "simple_explanation": "Settings that decide who is allowed to view, edit, or delete a file on the computer.",
                        "technical_meaning": "Access Control Lists (ACLs) and POSIX permission bits (rwx) that enforce Read, Write, and Execute constraints per user ID and group ID.",
                        "example": "Setting a student grade sheet to 'Read-Only' so students can see grades but cannot edit them."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "User Access Control & Data Backup",
                    "content": {
                        "term": "User Access Control (UAC) & Data Backup",
                        "definition": "UAC requires admin elevation before executing system-level changes; data backup replicates files to independent storage media for disaster recovery.",
                        "simple_explanation": "UAC is the security pop-up asking permission before installing apps; backup is saving extra copies of files to a USB drive or cloud.",
                        "technical_meaning": "UAC implements privilege separation (least privilege principle); backup involves automated replication to external media or remote cloud repositories.",
                        "example": "Windows UAC prompt before driver installation, and backing up project folders to Google Drive or an external SSD."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Shields of File and Folder Security",
                    "content": {
                        "text": "The operating system provides three complementary layers of defense:\n\n1. **Shield 1: Access Controls & Strong Passwords**:\n   - User account passwords and biometric authentication (fingerprint/face recognition) block physical unauthorized access.\n   - Strong passwords must be at least 8–12 characters, combining uppercase, lowercase, numbers, and symbols (e.g. `Sch00l@2026!`).\n2. **Shield 2: File Permissions (Read, Write, Execute)**:\n   - **Read-Only**: Users can view the contents but cannot modify, overwrite, or delete the file.\n   - **Write / Modify**: Users can edit, save changes, and delete the file.\n   - **No Access / Deny**: The folder is completely hidden or access is blocked for specified accounts.\n3. **Shield 3: Automated Backups & The 3-2-1 Rule**:\n   - Maintain **3** total copies of your data on **2** different storage media (e.g. internal SSD + external USB drive), with **1** copy stored offsite in the cloud."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Three Shields of Operating System Security",
                    "content": {
                        "title": "OS Security: Access Controls, Permissions, and Backups",
                        "caption": "Architectural security diagram illustrating user authentication, file permission levels, and external backup redundancy.",
                        "svg_content": SVG_THREE_SHIELDS_SECURITY
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Protecting a Folder with Read-Only Permissions",
                    "content": {
                        "intro": "How to lock a personal folder to prevent accidental editing or deletion:",
                        "steps": [
                            {"title": "1. Open Folder Properties", "description": "Right-click your `VLearn_Portfolio` folder -> Click **Properties** at the bottom of the context menu."},
                            {"title": "2. Locate Folder Attributes", "description": "In the General tab of the Properties dialog, locate the bottom section labeled **Attributes**."},
                            {"title": "3. Enable Read-Only Attribute", "description": "Check the box next to **Read-only (Only applies to files in folder)**."},
                            {"title": "4. Apply to Subfolders and Files", "description": "Click **Apply**. In the confirmation dialog, select *'Apply changes to this folder, subfolders, and files'* and click **OK**."},
                            {"title": "5. Test Protection", "description": "Open `lesson_summary.txt` inside the folder, type new text, and click Save. The OS will block the direct overwrite and prompt for 'Save As', confirming read-only protection!"}
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Risk Analysis: The 'USB Drive in Pocket' Fallacy",
                    "content": {
                        "title": "Real-World Security Scenario: Mark's Flash Drive",
                        "text": "A student keeps all term project files exclusively on a single USB flash drive, claiming: *'I don't need passwords or backups because my USB drive stays in my pocket.'*\n\n**Security Risks Identified**:\n1. **Physical Loss & Damage**: Flash drives are easily lost, dropped in water, or washed in laundry, causing total permanent data loss.\n2. **Zero Access Control**: Unencrypted flash drives can be plugged into any computer by a stranger to instantly view private files.\n3. **Remediation**: Set up automatic sync to cloud storage (Google Drive / OneDrive) and password-protect sensitive archive folders."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Common Misconception: 'Copying Files on the Same Drive is a Backup'",
                    "content": {
                        "misconception": "Copying a document from Documents to a folder named 'Backup' on drive C:\\ provides complete backup security.",
                        "correction": "If the physical hard drive fails, is infected with ransomware, or the laptop is stolen, both the original file and the 'backup' folder are destroyed simultaneously. A genuine backup must reside on an independent physical device or remote cloud server."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Weak Passwords and Shared Accounts",
                    "content": {
                        "mistake": "Using easily guessable passwords like `password123`, `12345678`, or sharing administrator accounts with other students.",
                        "fix": "Always use dedicated standard user accounts for daily tasks, keep administrator privileges restricted, and use complex passphrases with multi-factor authentication where supported."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Setting Permissions for Report Cards",
                    "content": {
                        "question": "Which file permission level should a teacher apply to a folder of student report cards so students can view results without changing any scores?",
                        "options": [
                            "Write-Only",
                            "Read-Only",
                            "Full Control",
                            "Execute-Only"
                        ],
                        "correct": "B",
                        "explanation": "Read-Only permission allows users to open and view the document contents while preventing them from editing, overwriting, or deleting data."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Genuine Data Backup Practice",
                    "content": {
                        "question": "Which of the following represents a secure, genuine data backup practice?",
                        "options": [
                            "Copying files to a new folder on the exact same internal hard drive",
                            "Renaming the file with the word 'BACKUP' at the end of the name",
                            "Replicating files to an external hard drive and syncing to encrypted cloud storage",
                            "Minimizing the file window to the desktop taskbar"
                        ],
                        "correct": "C",
                        "explanation": "A valid backup requires storing data copies on physically separate storage media or remote cloud services to survive local hardware failure."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "File Security, Permissions, and Backup Best Practices",
                    "content": {
                        "title": "Implementing Operating System Security Controls",
                        "youtube_id": "TqZkC0pQ0aY",
                        "url": "https://www.youtube.com/watch?v=TqZkC0pQ0aY",
                        "description": "Demonstration of managing user permissions, password policies, and automating backups."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3.3.2 Summary & Topic 3 Wrap-Up",
                    "content": {
                        "text": "1. **Three Shields**: Access Controls (passwords/UAC), File Permissions (Read/Write), and Automated Backups.\n2. **Permissions**: Read-only prevents accidental edits; Full Control is reserved for administrators.\n3. **3-2-1 Backup Rule**: 3 copies of data, on 2 different media types, with 1 copy offsite/cloud.\n4. **Topic 3 Mastery**: The Operating System is the master conductor that bridges hardware, apps, and users, manages resources, provides user interfaces, and safeguards digital information."
                    }
                }
            ]
        ]
    }
]
