"""
VLearn CBC Grade 10 ICT — Topic 1: Introduction to ICT
High-Precision Vector SVGs and Structured 5-Page Lesson Card Definitions

Topic: Introduction to ICT (Order: 1)
Lessons:
  1.1.1: What is Information and Communication Technology? (5 pages)
  1.2.1: Components of ICT Infrastructure (5 pages)
  1.3.1: Using ICT to Interact with Information (5 pages)
  1.4.1: Importance of ICT in Society (5 pages)
"""

# =============================================================================
# HIGH PRECISION, RESPONSIVE, MOBILE-FRIENDLY VECTOR SVGS
# =============================================================================

SVG_ICT_COMPONENTS_CYCLE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The ICT System Ecosystem &amp; Information Processing Cycle</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">Interaction of Data, Hardware, Software, Networks, People, and Procedures</text>

  <!-- Surrounding Environment: People, Networks, Procedures Outer Ring -->
  <rect x="40" y="90" width="880" height="395" rx="12" fill="#0f172a" stroke="#475569" stroke-dasharray="6,4" stroke-width="1.5"/>
  <text x="60" y="112" font-size="11" font-weight="bold" fill="#f59e0b">SURROUNDING ICT ENVIRONMENT: PEOPLE • NETWORKS • OPERATING PROCEDURES</text>

  <!-- Node 1: Raw Data Input -->
  <g transform="translate(60, 135)">
    <rect width="180" height="210" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="180" height="32" rx="8" fill="#0284c7"/>
    <text x="90" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. RAW DATA (INPUT)</text>
    <text x="15" y="55" font-size="10.5" font-weight="bold" fill="#38bdf8">• Definition:</text>
    <text x="15" y="72" font-size="9.5" fill="#cbd5e1">Unorganized facts, numbers, and symbols without context.</text>
    <text x="15" y="105" font-size="10.5" font-weight="bold" fill="#38bdf8">• Input Devices:</text>
    <text x="15" y="122" font-size="9.5" fill="#cbd5e1">Keyboard, barcode scanner, sensors, touch screen, mic.</text>
    <text x="15" y="155" font-size="10.5" font-weight="bold" fill="#38bdf8">• Example:</text>
    <text x="15" y="172" font-size="9.5" fill="#cbd5e1">Raw numbers: 38.5, 120, 80.</text>
    <rect x="15" y="185" width="150" height="18" rx="4" fill="#0f172a"/>
    <text x="90" y="198" font-size="8.5" fill="#38bdf8" text-anchor="middle">Needs Processing</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <g transform="translate(245, 230)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="35,-5 45,0 35,5" fill="#38bdf8"/>
    <text x="20" y="-10" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Input</text>
  </g>

  <!-- Node 2: Processing (Hardware + Software) -->
  <g transform="translate(295, 135)">
    <rect width="200" height="210" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="200" height="32" rx="8" fill="#059669"/>
    <text x="100" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PROCESSING (CPU &amp; SW)</text>
    <text x="15" y="55" font-size="10.5" font-weight="bold" fill="#34d399">• Hardware Engine:</text>
    <text x="15" y="72" font-size="9.5" fill="#cbd5e1">CPU (ALU, CU) &amp; RAM execute computational logic.</text>
    <text x="15" y="105" font-size="10.5" font-weight="bold" fill="#34d399">• Software Directives:</text>
    <text x="15" y="122" font-size="9.5" fill="#cbd5e1">OS &amp; applications calculate, filter, and structure data.</text>
    <text x="15" y="155" font-size="10.5" font-weight="bold" fill="#34d399">• Transformation:</text>
    <text x="15" y="172" font-size="9.5" fill="#cbd5e1">Applies formulas, thresholds, and clinical rules.</text>
    <rect x="15" y="185" width="170" height="18" rx="4" fill="#0f172a"/>
    <text x="100" y="198" font-size="8.5" fill="#34d399" text-anchor="middle">Algorithms &amp; Logic</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <g transform="translate(500, 230)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#10b981" stroke-width="3"/>
    <polygon points="35,-5 45,0 35,5" fill="#10b981"/>
    <text x="20" y="-10" font-size="9" font-weight="bold" fill="#10b981" text-anchor="middle">Output</text>
  </g>

  <!-- Node 3: Useful Information Output -->
  <g transform="translate(550, 135)">
    <rect width="180" height="210" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <rect width="180" height="32" rx="8" fill="#7c3aed"/>
    <text x="90" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. USEFUL INFORMATION</text>
    <text x="15" y="55" font-size="10.5" font-weight="bold" fill="#a78bfa">• Definition:</text>
    <text x="15" y="72" font-size="9.5" fill="#cbd5e1">Processed, organized, context-rich data for decisions.</text>
    <text x="15" y="105" font-size="10.5" font-weight="bold" fill="#a78bfa">• Output Channels:</text>
    <text x="15" y="122" font-size="9.5" fill="#cbd5e1">Monitors, digital charts, synthesizers, printed bills.</text>
    <text x="15" y="155" font-size="10.5" font-weight="bold" fill="#a78bfa">• Example:</text>
    <text x="15" y="172" font-size="9.5" fill="#cbd5e1">"Patient Fever Alert: 38.5°C with high blood pressure."</text>
    <rect x="15" y="185" width="150" height="18" rx="4" fill="#0f172a"/>
    <text x="90" y="198" font-size="8.5" fill="#a78bfa" text-anchor="middle">Enables Action</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <g transform="translate(735, 230)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#8b5cf6" stroke-width="3"/>
    <polygon points="35,-5 45,0 35,5" fill="#8b5cf6"/>
    <text x="20" y="-10" font-size="9" font-weight="bold" fill="#8b5cf6" text-anchor="middle">Save</text>
  </g>

  <!-- Node 4: Secondary Storage & Cloud -->
  <g transform="translate(775, 135)">
    <rect width="130" height="210" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="130" height="32" rx="8" fill="#d97706"/>
    <text x="65" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. STORAGE</text>
    <text x="10" y="55" font-size="9.5" font-weight="bold" fill="#fbbf24">• Retention:</text>
    <text x="10" y="70" font-size="8.5" fill="#cbd5e1">NVMe SSDs, SQL DBs, Cloud Archives.</text>
    <text x="10" y="105" font-size="9.5" font-weight="bold" fill="#fbbf24">• Persistence:</text>
    <text x="10" y="120" font-size="8.5" fill="#cbd5e1">Available for historical analysis.</text>
    <text x="10" y="155" font-size="9.5" font-weight="bold" fill="#fbbf24">• Feedback:</text>
    <text x="10" y="170" font-size="8.5" fill="#cbd5e1">Feeds future machine inputs.</text>
  </g>

  <!-- Bottom 3 Pillars: People, Networks, Procedures Cards -->
  <g transform="translate(60, 360)">
    <!-- Pillar: People -->
    <rect x="0" y="0" width="260" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#38bdf8">PEOPLE (Users &amp; Admins)</text>
    <text x="15" y="44" font-size="9.5" fill="#cbd5e1">• End-users who initiate requests and consume outputs.</text>
    <text x="15" y="60" font-size="9.5" fill="#cbd5e1">• Software developers &amp; database engineers who build.</text>
    <text x="15" y="76" font-size="9.5" fill="#cbd5e1">• Systems administrators who maintain uptime.</text>
    <text x="15" y="96" font-size="8.5" font-weight="bold" fill="#38bdf8">Human Guidance at the Center</text>

    <!-- Pillar: Networks -->
    <rect x="290" y="0" width="265" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="305" y="24" font-size="12" font-weight="bold" fill="#34d399">NETWORKS (Connectivity)</text>
    <text x="305" y="44" font-size="9.5" fill="#cbd5e1">• Telecommunication channels (Fiber, 5G, Wi-Fi 6).</text>
    <text x="305" y="60" font-size="9.5" fill="#cbd5e1">• Protocols (TCP/IP, HTTPS, MQTT) ensuring packet flow.</text>
    <text x="305" y="76" font-size="9.5" fill="#cbd5e1">• Enables distributed sharing across global servers.</text>
    <text x="305" y="96" font-size="8.5" font-weight="bold" fill="#34d399">Uniting Isolated Computers</text>

    <!-- Pillar: Procedures -->
    <rect x="585" y="0" width="260" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="600" y="24" font-size="12" font-weight="bold" fill="#fbbf24">PROCEDURES (Rules &amp; SOPs)</text>
    <text x="600" y="44" font-size="9.5" fill="#cbd5e1">• User authentication policies (Passwords, 2FA).</text>
    <text x="600" y="60" font-size="9.5" fill="#cbd5e1">• 3-2-1 backup schedules &amp; disaster recovery plans.</text>
    <text x="600" y="76" font-size="9.5" fill="#cbd5e1">• Data privacy regulations (Data Protection Act).</text>
    <text x="600" y="96" font-size="8.5" font-weight="bold" fill="#fbbf24">Governing Safe &amp; Ethical Operation</text>
  </g>
</svg>
""".strip()

SVG_INFRASTRUCTURE_LAYERS = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Enterprise ICT Infrastructure Layered Architecture</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">The 5-Tier Functional Hierarchy: From Physical Infrastructure to Governance</text>

  <!-- Left Dependency Axis Arrow -->
  <g transform="translate(45, 100)">
    <line x1="20" y1="360" x2="20" y2="10" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="15,15 20,0 25,15" fill="#f59e0b"/>
    <text x="-185" y="12" font-size="10.5" font-weight="bold" fill="#f59e0b" transform="rotate(-90)" text-anchor="middle">UPWARD DEPENDENCY STACK</text>
  </g>

  <!-- Stacked Layers Container -->
  <g transform="translate(85, 95)">
    <!-- Layer 5: People & Procedures -->
    <rect x="0" y="0" width="810" height="68" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.8"/>
    <rect x="0" y="0" width="190" height="68" rx="8" fill="#be185d"/>
    <text x="95" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LAYER 5</text>
    <text x="95" y="48" font-size="10" fill="#fbcfe8" text-anchor="middle">People &amp; Procedures</text>
    <text x="210" y="28" font-size="11" font-weight="bold" fill="#f472b6">Governance, Administration &amp; Operational SOPs</text>
    <text x="210" y="48" font-size="10" fill="#cbd5e1">• End users, IT engineers, password policies, access control lists (ACLs), audit logs &amp; disaster recovery plans.</text>

    <!-- Layer 4: Application Software -->
    <rect x="0" y="76" width="810" height="68" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.8"/>
    <rect x="0" y="76" width="190" height="68" rx="8" fill="#6d28d9"/>
    <text x="95" y="106" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LAYER 4</text>
    <text x="95" y="124" font-size="10" fill="#ddd6fe" text-anchor="middle">Application Software</text>
    <text x="210" y="104" font-size="11" font-weight="bold" fill="#a78bfa">User-Facing Productivity &amp; Enterprise Software</text>
    <text x="210" y="124" font-size="10" fill="#cbd5e1">• Office productivity suites, database management systems (DBMS), web portals, school management systems (SMS).</text>

    <!-- Layer 3: System Software -->
    <rect x="0" y="152" width="810" height="68" rx="8" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.8"/>
    <rect x="0" y="152" width="190" height="68" rx="8" fill="#0369a1"/>
    <text x="95" y="182" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LAYER 3</text>
    <text x="95" y="200" font-size="10" fill="#bae6fd" text-anchor="middle">System Software</text>
    <text x="210" y="180" font-size="11" font-weight="bold" fill="#38bdf8">Operating Systems &amp; Hardware Abstraction</text>
    <text x="210" y="200" font-size="10" fill="#cbd5e1">• Linux, Windows Server, macOS, device drivers, virtual memory managers, disk utilities, and firmware (BIOS/UEFI).</text>

    <!-- Layer 2: Hardware Infrastructure -->
    <rect x="0" y="228" width="810" height="68" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect x="0" y="228" width="190" height="68" rx="8" fill="#047857"/>
    <text x="95" y="258" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LAYER 2</text>
    <text x="95" y="276" font-size="10" fill="#a7f3d0" text-anchor="middle">Hardware Machinery</text>
    <text x="210" y="256" font-size="11" font-weight="bold" fill="#34d399">Physical Computing Units &amp; Storage Drives</text>
    <text x="210" y="276" font-size="10" fill="#cbd5e1">• Rack servers, client desktops, multi-core CPUs, ECC RAM, NVMe arrays, cooling systems, and redundant UPS power.</text>

    <!-- Layer 1: Network & Telecommunications -->
    <rect x="0" y="304" width="810" height="68" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect x="0" y="304" width="190" height="68" rx="8" fill="#b45309"/>
    <text x="95" y="334" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LAYER 1</text>
    <text x="95" y="352" font-size="10" fill="#fde68a" text-anchor="middle">Networks &amp; Telecom</text>
    <text x="210" y="332" font-size="11" font-weight="bold" fill="#fbbf24">Physical &amp; Wireless Communication Highway</text>
    <text x="210" y="352" font-size="10" fill="#cbd5e1">• Fiber backbones, Ethernet cables (Cat6a), Gigabit switches, hardware firewalls, Wi-Fi 6 access points, ISP gateways.</text>
  </g>

  <!-- Bottom Core Takeaway -->
  <rect x="85" y="472" width="810" height="22" rx="5" fill="#0f172a" stroke="#334155"/>
  <text x="490" y="487" font-size="9.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Fundamental Rule: A failure in underlying layers (e.g. power/network) immediately disables all dependent application and user operations.</text>
</svg>
""".strip()

SVG_NETWORK_TOPOLOGY = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">School Computer Lab &amp; Enterprise LAN Network Topology</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">Physical Layout Connecting Workstations, Dedicated Servers, Switches, and Internet Gateway</text>

  <!-- ISP Cloud -->
  <g transform="translate(60, 110)">
    <rect width="140" height="70" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="70" y="35" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">ISP CLOUD</text>
    <text x="70" y="52" font-size="9" fill="#94a3b8" text-anchor="middle">Fiber Internet Uplink</text>
  </g>

  <!-- Line Cloud to Router -->
  <line x1="200" y1="145" x2="250" y2="145" stroke="#38bdf8" stroke-width="2.5"/>

  <!-- Enterprise Router & Firewall -->
  <g transform="translate(250, 110)">
    <rect width="150" height="70" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.8"/>
    <text x="75" y="32" font-size="11.5" font-weight="bold" fill="#f87171" text-anchor="middle">GATEWAY ROUTER</text>
    <text x="75" y="48" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">&amp; FIREWALL</text>
    <text x="75" y="62" font-size="8.5" fill="#fca5a5" text-anchor="middle">NAT • DHCP • Packet Filter</text>
  </g>

  <!-- Line Router to Central Switch -->
  <line x1="400" y1="145" x2="460" y2="145" stroke="#10b981" stroke-width="3"/>

  <!-- Central Managed Gigabit Switch -->
  <g transform="translate(460, 100)">
    <rect width="210" height="90" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="105" y="32" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">CENTRAL SWITCH</text>
    <text x="105" y="50" font-size="10" fill="#ffffff" text-anchor="middle">24-Port Gigabit Managed</text>
    <text x="105" y="70" font-size="8.5" fill="#94a3b8" text-anchor="middle">VLAN Segmentation • Traffic Control</text>
    <!-- Switch Port Indicators -->
    <circle cx="30" cy="80" r="3" fill="#10b981"/>
    <circle cx="45" cy="80" r="3" fill="#10b981"/>
    <circle cx="60" cy="80" r="3" fill="#10b981"/>
    <circle cx="75" cy="80" r="3" fill="#10b981"/>
    <circle cx="90" cy="80" r="3" fill="#10b981"/>
    <circle cx="105" cy="80" r="3" fill="#10b981"/>
    <circle cx="120" cy="80" r="3" fill="#10b981"/>
    <circle cx="135" cy="80" r="3" fill="#10b981"/>
  </g>

  <!-- Right: Local Server & Backup -->
  <line x1="670" y1="145" x2="740" y2="145" stroke="#f59e0b" stroke-width="2.5"/>
  <g transform="translate(740, 105)">
    <rect width="160" height="80" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <text x="80" y="28" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">LOCAL LAB SERVER</text>
    <text x="80" y="46" font-size="9.5" fill="#ffffff" text-anchor="middle">File Share &amp; Domain Admin</text>
    <text x="80" y="64" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Daily Automated Backup</text>
  </g>

  <!-- Distribution Lines to Nodes Below -->
  <line x1="565" y1="190" x2="565" y2="240" stroke="#10b981" stroke-width="2"/>
  <line x1="140" y1="240" x2="820" y2="240" stroke="#10b981" stroke-width="2"/>

  <!-- Drops to Connected Devices -->
  <!-- Node A: Teacher Workstation & Projector -->
  <line x1="140" y1="240" x2="140" y2="270" stroke="#10b981" stroke-width="2"/>
  <g transform="translate(60, 270)">
    <rect width="160" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="80" y="24" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Teacher Station</text>
    <text x="80" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">Master Lab Console</text>
    <text x="80" y="62" font-size="9" fill="#cbd5e1" text-anchor="middle">+ Smart Projector</text>
    <text x="80" y="80" font-size="8.5" fill="#94a3b8" text-anchor="middle">IP: 192.168.1.10</text>
    <rect x="20" y="92" width="120" height="18" rx="4" fill="#0f172a"/>
    <text x="80" y="104" font-size="8" fill="#38bdf8" text-anchor="middle">Admin Controls</text>
  </g>

  <!-- Node B: Student Desktop Workstations -->
  <line x1="365" y1="240" x2="365" y2="270" stroke="#10b981" stroke-width="2"/>
  <g transform="translate(285, 270)">
    <rect width="160" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="80" y="24" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Student Pod A (1-15)</text>
    <text x="80" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">15 Client Workstations</text>
    <text x="80" y="62" font-size="9" fill="#cbd5e1" text-anchor="middle">Gigabit Cat6 Ethernet</text>
    <text x="80" y="80" font-size="8.5" fill="#94a3b8" text-anchor="middle">DHCP Assigned Range</text>
    <rect x="20" y="92" width="120" height="18" rx="4" fill="#0f172a"/>
    <text x="80" y="104" font-size="8" fill="#34d399" text-anchor="middle">Learner Workspace</text>
  </g>

  <!-- Node C: Student Pod B (16-30) -->
  <line x1="595" y1="240" x2="595" y2="270" stroke="#10b981" stroke-width="2"/>
  <g transform="translate(515, 270)">
    <rect width="160" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="80" y="24" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Student Pod B (16-30)</text>
    <text x="80" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">15 Client Workstations</text>
    <text x="80" y="62" font-size="9" fill="#cbd5e1" text-anchor="middle">Gigabit Cat6 Ethernet</text>
    <text x="80" y="80" font-size="8.5" fill="#94a3b8" text-anchor="middle">Shared Resource Access</text>
    <rect x="20" y="92" width="120" height="18" rx="4" fill="#0f172a"/>
    <text x="80" y="104" font-size="8" fill="#34d399" text-anchor="middle">Learner Workspace</text>
  </g>

  <!-- Node D: Shared Peripherals & Wi-Fi -->
  <line x1="820" y1="240" x2="820" y2="270" stroke="#10b981" stroke-width="2"/>
  <g transform="translate(740, 270)">
    <rect width="160" height="120" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="80" y="24" font-size="11" font-weight="bold" fill="#a78bfa" text-anchor="middle">Shared Peripherals</text>
    <text x="80" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">Network Laser Printer</text>
    <text x="80" y="62" font-size="9" fill="#cbd5e1" text-anchor="middle">+ Wi-Fi 6 Access Point</text>
    <text x="80" y="80" font-size="8.5" fill="#94a3b8" text-anchor="middle">Secure WPA3 Protocol</text>
    <rect x="20" y="92" width="120" height="18" rx="4" fill="#0f172a"/>
    <text x="80" y="104" font-size="8" fill="#a78bfa" text-anchor="middle">Shared Resources</text>
  </g>

  <!-- Bottom Legend -->
  <rect x="60" y="415" width="840" height="75" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="480" y="438" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">School Computer Lab SOP Enforcement</text>
  <text x="480" y="458" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• No food or liquids near equipment • Unique student login IDs • Clean logoff before departure • Automatic virus scan on inserted USB drives</text>
  <text x="480" y="476" font-size="8.5" fill="#94a3b8" text-anchor="middle">Hardware + Software + Network + Data + People + Procedures operating in unified harmony</text>
</svg>
""".strip()

SVG_COMMUNICATION_FLOW = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Digital Communication &amp; Information Transmission Model</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">Cybernetic Communication Loop: Sender, Encoding, Medium/Channel, Noise, Decoding, and Feedback</text>

  <!-- Sender -->
  <g transform="translate(50, 110)">
    <rect width="140" height="170" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="140" height="28" rx="8" fill="#0284c7"/>
    <text x="70" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SENDER (Source)</text>
    <text x="12" y="48" font-size="10" font-weight="bold" fill="#38bdf8">• Human / System</text>
    <text x="12" y="65" font-size="9" fill="#cbd5e1">Creates idea, text message, report, or video stream.</text>
    <text x="12" y="100" font-size="10" font-weight="bold" fill="#38bdf8">• Intent:</text>
    <text x="12" y="116" font-size="9" fill="#cbd5e1">Transfers knowledge or initiates a transaction.</text>
    <rect x="10" y="140" width="120" height="20" rx="4" fill="#1e293b"/>
    <text x="70" y="154" font-size="8.5" fill="#38bdf8" text-anchor="middle">Originator</text>
  </g>

  <!-- Arrow Sender -> Encoder -->
  <line x1="190" y1="195" x2="225" y2="195" stroke="#38bdf8" stroke-width="2.5"/>
  <polygon points="225,190 235,195 225,200" fill="#38bdf8"/>

  <!-- Encoder -->
  <g transform="translate(235, 110)">
    <rect width="140" height="170" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="140" height="28" rx="8" fill="#059669"/>
    <text x="70" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ENCODING</text>
    <text x="12" y="48" font-size="10" font-weight="bold" fill="#34d399">• Packetization:</text>
    <text x="12" y="65" font-size="9" fill="#cbd5e1">Transforms text/media into binary bits (0s &amp; 1s).</text>
    <text x="12" y="100" font-size="10" font-weight="bold" fill="#34d399">• Protocols:</text>
    <text x="12" y="116" font-size="9" fill="#cbd5e1">TCP/IP, SMTP (email), HTTPS, H.264 video codec.</text>
    <rect x="10" y="140" width="120" height="20" rx="4" fill="#1e293b"/>
    <text x="70" y="154" font-size="8.5" fill="#34d399" text-anchor="middle">Digital Modulation</text>
  </g>

  <!-- Arrow Encoder -> Channel -->
  <line x1="375" y1="195" x2="410" y2="195" stroke="#10b981" stroke-width="2.5"/>
  <polygon points="410,190 420,195 410,200" fill="#10b981"/>

  <!-- Medium / Channel & Noise Box -->
  <g transform="translate(420, 95)">
    <rect width="160" height="200" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="160" height="28" rx="8" fill="#d97706"/>
    <text x="80" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. MEDIUM &amp; CHANNEL</text>
    <text x="12" y="46" font-size="9.5" font-weight="bold" fill="#fbbf24">• Physical Transmission:</text>
    <text x="12" y="62" font-size="8.5" fill="#cbd5e1">Fiber optics, 5G wireless, satellite microwave links.</text>
    
    <!-- Noise / Interference Sub-Card -->
    <rect x="8" y="85" width="144" height="98" rx="6" fill="#0f172a" stroke="#ef4444" stroke-dasharray="3,3"/>
    <text x="80" y="103" font-size="9.5" font-weight="bold" fill="#f87171" text-anchor="middle">NOISE &amp; INTERFERENCE</text>
    <text x="15" y="122" font-size="8" fill="#fca5a5">• Packet loss &amp; jitter</text>
    <text x="15" y="136" font-size="8" fill="#fca5a5">• Signal attenuation / rain fade</text>
    <text x="15" y="150" font-size="8" fill="#fca5a5">• Bandwidth throttling</text>
    <text x="15" y="166" font-size="8" fill="#fca5a5">• Network latency</text>
  </g>

  <!-- Arrow Channel -> Decoder -->
  <line x1="580" y1="195" x2="615" y2="195" stroke="#8b5cf6" stroke-width="2.5"/>
  <polygon points="615,190 625,195 615,200" fill="#8b5cf6"/>

  <!-- Decoder -->
  <g transform="translate(625, 110)">
    <rect width="140" height="170" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="2"/>
    <rect width="140" height="28" rx="8" fill="#7c3aed"/>
    <text x="70" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. DECODING</text>
    <text x="12" y="48" font-size="10" font-weight="bold" fill="#a78bfa">• De-packetizing:</text>
    <text x="12" y="65" font-size="9" fill="#cbd5e1">Reassembles packets into chronological order.</text>
    <text x="12" y="100" font-size="10" font-weight="bold" fill="#a78bfa">• Decryption:</text>
    <text x="12" y="116" font-size="9" fill="#cbd5e1">TLS decryption &amp; browser HTML rendering.</text>
    <rect x="10" y="140" width="120" height="20" rx="4" fill="#1e293b"/>
    <text x="70" y="154" font-size="8.5" fill="#a78bfa" text-anchor="middle">Rendering Interface</text>
  </g>

  <!-- Arrow Decoder -> Receiver -->
  <line x1="765" y1="195" x2="800" y2="195" stroke="#8b5cf6" stroke-width="2.5"/>
  <polygon points="800,190 810,195 800,200" fill="#8b5cf6"/>

  <!-- Receiver -->
  <g transform="translate(810, 110)">
    <rect width="120" height="170" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect width="120" height="28" rx="8" fill="#be185d"/>
    <text x="60" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. RECEIVER</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#f472b6">• Destination:</text>
    <text x="10" y="65" font-size="8.5" fill="#cbd5e1">Student, doctor, or server host.</text>
    <text x="10" y="100" font-size="10" font-weight="bold" fill="#f472b6">• Action:</text>
    <text x="10" y="116" font-size="8.5" fill="#cbd5e1">Reads message &amp; understands intent.</text>
    <rect x="10" y="140" width="100" height="20" rx="4" fill="#1e293b"/>
    <text x="60" y="154" font-size="8.5" fill="#f472b6" text-anchor="middle">Message Consumed</text>
  </g>

  <!-- Bottom Return Feedback Arc -->
  <path d="M 870,285 L 870,330 L 120,330 L 120,285" fill="none" stroke="#10b981" stroke-width="2.5" stroke-dasharray="5,4"/>
  <polygon points="115,290 120,280 125,290" fill="#10b981"/>
  <rect x="400" y="318" width="200" height="24" rx="6" fill="#059669"/>
  <text x="500" y="334" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">6. FEEDBACK LOOP (ACK &amp; REPLY)</text>

  <!-- Channel Type Comparison Matrix -->
  <g transform="translate(50, 365)">
    <!-- Synchronous -->
    <rect x="0" y="0" width="410" height="115" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="15" y="24" font-size="11.5" font-weight="bold" fill="#38bdf8">SYNCHRONOUS COMMUNICATION (Real-Time)</text>
    <text x="15" y="44" font-size="9.5" fill="#cbd5e1">• Participants interact at the exact same time with low latency.</text>
    <text x="15" y="62" font-size="9.5" fill="#cbd5e1">• Examples: Zoom/Google Meet video calls, WhatsApp voice calls, live webinars.</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">• Strengths: Immediate clarification, dynamic brainstorming, active engagement.</text>
    <text x="15" y="98" font-size="8.5" font-weight="bold" fill="#38bdf8">Ideal for urgent collaboration and interactive classes</text>

    <!-- Asynchronous -->
    <rect x="450" y="0" width="410" height="115" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="465" y="24" font-size="11.5" font-weight="bold" fill="#fbbf24">ASYNCHRONOUS COMMUNICATION (Delayed)</text>
    <text x="465" y="44" font-size="9.5" fill="#cbd5e1">• Participants send and read messages at different times (store-and-forward).</text>
    <text x="465" y="62" font-size="9.5" fill="#cbd5e1">• Examples: Formal email (Gmail/Outlook), discussion boards, recorded lectures.</text>
    <text x="465" y="80" font-size="9.5" fill="#cbd5e1">• Strengths: Permanent documentation, thoughtful responses, schedule flexibility.</text>
    <text x="465" y="98" font-size="8.5" font-weight="bold" fill="#fbbf24">Standard professional response turnaround: up to 24 hours</text>
  </g>
</svg>
""".strip()

SVG_ICT_IMPACT_AREAS = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="510" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Societal Impact of ICT Across Key Economic &amp; Civic Sectors</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How Digital Infrastructure Powers National Transformation and Community Development</text>

  <!-- Central Hub Node -->
  <g transform="translate(380, 210)">
    <rect width="200" height="100" rx="16" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="100" y="42" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">ICT IN MODERN</text>
    <text x="100" y="62" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">SOCIETY</text>
    <text x="100" y="82" font-size="9.5" fill="#94a3b8" text-anchor="middle">Core Transformation Engine</text>
  </g>

  <!-- Top-Left: Education -->
  <g transform="translate(45, 90)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#38bdf8">1. EDUCATION (E-Learning)</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• Google Classroom, VLearn, virtual lab sims.</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• Remote study materials accessible 24/7.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#0ea5e9">Eliminates geographic distance to learning</text>
  </g>
  <line x1="305" y1="135" x2="380" y2="230" stroke="#0ea5e9" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Top-Center: Commerce & Mobile Money -->
  <g transform="translate(350, 90)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#34d399">2. COMMERCE &amp; FINTECH</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• M-Pesa mobile money &amp; cashless merchant pay.</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• E-commerce (Jumia, Amazon) global marketplaces.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#10b981">Democratizes financial inclusion</text>
  </g>
  <line x1="480" y1="180" x2="480" y2="210" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Top-Right: Healthcare & Telemedicine -->
  <g transform="translate(655, 90)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#fbbf24">3. HEALTHCARE &amp; MEDICINE</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• Telemedicine remote specialist consultations.</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• Electronic Medical Records (EMR) instant sharing.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#f59e0b">Saves lives in remote rural communities</text>
  </g>
  <line x1="655" y1="135" x2="580" y2="230" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Mid-Left: Government (e-Governance) -->
  <g transform="translate(45, 215)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#a78bfa">4. E-GOVERNMENT (eCitizen)</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• Passports, driving licenses, birth certs online.</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• KRA iTax electronic revenue filings.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#8b5cf6">Eliminates queues &amp; curtails corruption</text>
  </g>
  <line x1="305" y1="260" x2="380" y2="260" stroke="#8b5cf6" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Mid-Right: Smart Agriculture -->
  <g transform="translate(655, 215)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#4ade80">5. SMART AGRICULTURE</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• Mobile crop market prices (prevent middleman loss).</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• IoT soil moisture sensors &amp; drone crop spraying.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#22c55e">Maximizes food yields &amp; farmer profits</text>
  </g>
  <line x1="655" y1="260" x2="580" y2="260" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Bottom-Left: Transport & Logistics -->
  <g transform="translate(45, 340)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#f472b6">6. TRANSPORT &amp; LOGISTICS</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• GPS navigation (Google Maps), fleet telemetry.</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• Uber/Bolt ridesharing &amp; smart traffic lights.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#ec4899">Optimizes urban transit &amp; cargo dispatch</text>
  </g>
  <line x1="305" y1="385" x2="380" y2="290" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Bottom-Center: Digital Divide Challenge -->
  <g transform="translate(350, 340)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#f87171">7. THE DIGITAL DIVIDE</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• Inequality in broadband access, devices &amp; power.</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• Rural vs urban technological infrastructure gaps.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#ef4444">Requires national policy &amp; digital literacy</text>
  </g>
  <line x1="480" y1="340" x2="480" y2="310" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Bottom-Right: Communication & Media -->
  <g transform="translate(655, 340)">
    <rect width="260" height="90" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="1.8"/>
    <text x="15" y="24" font-size="12" font-weight="bold" fill="#22d3ee">8. COMMUNICATION &amp; MEDIA</text>
    <text x="15" y="44" font-size="9" fill="#cbd5e1">• Social networking, instant messaging, cloud video.</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• Digital news broadcasts &amp; emergency alerts.</text>
    <text x="15" y="78" font-size="8.5" font-weight="bold" fill="#06b6d4">Instant global citizen connectivity</text>
  </g>
  <line x1="655" y1="385" x2="580" y2="290" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="4,3"/>

  <!-- Bottom Banner -->
  <rect x="45" y="450" width="870" height="50" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="480" y="470" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Kenya's Global Leadership: M-Pesa Mobile Financial Technology &amp; eCitizen Digital Transformation</text>
  <text x="480" y="488" font-size="9.5" fill="#94a3b8" text-anchor="middle">ICT shifts society from physical friction and manual queues to instantaneous, transparent digital services.</text>
</svg>
""".strip()

SVG_DIGITAL_TRANSFORMATION_TIMELINE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Historical Timeline of Digital Transformation</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">From Isolated Mainframe Computers to Ubiquitous Cloud, Artificial Intelligence, and IoT</text>

  <!-- Glowing Horizontal Central Pipeline -->
  <line x1="50" y1="260" x2="910" y2="260" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="100" cy="260" r="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="250" cy="260" r="10" fill="#059669" stroke="#34d399" stroke-width="2"/>
  <circle cx="400" cy="260" r="10" fill="#7c3aed" stroke="#a78bfa" stroke-width="2"/>
  <circle cx="550" cy="260" r="10" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
  <circle cx="700" cy="260" r="10" fill="#be185d" stroke="#f472b6" stroke-width="2"/>
  <circle cx="850" cy="260" r="10" fill="#0891b2" stroke="#22d3ee" stroke-width="2"/>

  <!-- Milestone 1: 1960s Mainframes (Top) -->
  <g transform="translate(40, 100)">
    <rect width="130" height="130" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="130" height="24" rx="6" fill="#0284c7"/>
    <text x="65" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1960s-1970s</text>
    <text x="10" y="42" font-size="10" font-weight="bold" fill="#38bdf8">Mainframe Era</text>
    <text x="10" y="58" font-size="8.5" fill="#cbd5e1">• Centralized batch processing.</text>
    <text x="10" y="72" font-size="8.5" fill="#cbd5e1">• Punch cards &amp; magnetic tape.</text>
    <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Room-sized corporate systems.</text>
    <text x="10" y="112" font-size="8" font-weight="bold" fill="#38bdf8">Restricted Access</text>
  </g>
  <line x1="100" y1="230" x2="100" y2="250" stroke="#0ea5e9" stroke-width="2"/>

  <!-- Milestone 2: 1980s Personal Computers (Bottom) -->
  <g transform="translate(190, 290)">
    <rect width="130" height="130" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="130" height="24" rx="6" fill="#059669"/>
    <text x="65" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1980s</text>
    <text x="10" y="42" font-size="10" font-weight="bold" fill="#34d399">PC Revolution</text>
    <text x="10" y="58" font-size="8.5" fill="#cbd5e1">• Desktops for home/office.</text>
    <text x="10" y="72" font-size="8.5" fill="#cbd5e1">• Floppy disks &amp; local OS (MS-DOS).</text>
    <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Standalone spreadsheets.</text>
    <text x="10" y="112" font-size="8" font-weight="bold" fill="#34d399">Personal Autonomy</text>
  </g>
  <line x1="250" y1="270" x2="250" y2="290" stroke="#10b981" stroke-width="2"/>

  <!-- Milestone 3: 1990s World Wide Web (Top) -->
  <g transform="translate(340, 100)">
    <rect width="130" height="130" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="130" height="24" rx="6" fill="#7c3aed"/>
    <text x="65" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1990s</text>
    <text x="10" y="42" font-size="10" font-weight="bold" fill="#a78bfa">World Wide Web</text>
    <text x="10" y="58" font-size="8.5" fill="#cbd5e1">• Dial-up internet &amp; browsers.</text>
    <text x="10" y="72" font-size="8.5" fill="#cbd5e1">• HTML websites &amp; email.</text>
    <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Commercial online presence.</text>
    <text x="10" y="112" font-size="8" font-weight="bold" fill="#a78bfa">Global Information</text>
  </g>
  <line x1="400" y1="230" x2="400" y2="250" stroke="#8b5cf6" stroke-width="2"/>

  <!-- Milestone 4: 2000s Mobile Internet & M-Pesa (Bottom) -->
  <g transform="translate(490, 290)">
    <rect width="130" height="130" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="130" height="24" rx="6" fill="#d97706"/>
    <text x="65" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2000s</text>
    <text x="10" y="42" font-size="10" font-weight="bold" fill="#fbbf24">Mobile Revolution</text>
    <text x="10" y="58" font-size="8.5" fill="#cbd5e1">• 3G/4G broadband data.</text>
    <text x="10" y="72" font-size="8.5" fill="#cbd5e1">• M-Pesa mobile money (2007).</text>
    <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Smartphones &amp; social media.</text>
    <text x="10" y="112" font-size="8" font-weight="bold" fill="#fbbf24">Pocket Computing</text>
  </g>
  <line x1="550" y1="270" x2="550" y2="290" stroke="#f59e0b" stroke-width="2"/>

  <!-- Milestone 5: 2010s Cloud & Big Data (Top) -->
  <g transform="translate(640, 100)">
    <rect width="130" height="130" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="130" height="24" rx="6" fill="#be185d"/>
    <text x="65" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2010s</text>
    <text x="10" y="42" font-size="10" font-weight="bold" fill="#f472b6">Cloud Ecosystem</text>
    <text x="10" y="58" font-size="8.5" fill="#cbd5e1">• AWS, Azure, Google Drive.</text>
    <text x="10" y="72" font-size="8.5" fill="#cbd5e1">• SaaS &amp; streaming services.</text>
    <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Fiber to the home / 4G LTE.</text>
    <text x="10" y="112" font-size="8" font-weight="bold" fill="#f472b6">Universal Storage</text>
  </g>
  <line x1="700" y1="230" x2="700" y2="250" stroke="#ec4899" stroke-width="2"/>

  <!-- Milestone 6: 2020s+ AI, IoT & Smart Systems (Bottom) -->
  <g transform="translate(790, 290)">
    <rect width="130" height="130" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="130" height="24" rx="6" fill="#0891b2"/>
    <text x="65" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2020s &amp; Beyond</text>
    <text x="10" y="42" font-size="10" font-weight="bold" fill="#22d3ee">AI &amp; Smart Edge</text>
    <text x="10" y="58" font-size="8.5" fill="#cbd5e1">• Generative AI &amp; LLMs.</text>
    <text x="10" y="72" font-size="8.5" fill="#cbd5e1">• IoT smart agriculture &amp; 5G.</text>
    <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Autonomous systems &amp; robotics.</text>
    <text x="10" y="112" font-size="8" font-weight="bold" fill="#22d3ee">Intelligent Society</text>
  </g>
  <line x1="850" y1="270" x2="850" y2="290" stroke="#06b6d4" stroke-width="2"/>

  <!-- Bottom Legend -->
  <rect x="50" y="445" width="860" height="40" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="480" y="468" font-size="10.5" fill="#94a3b8" text-anchor="middle">The continuous acceleration of computing power, bandwidth, and distributed software reshaping human civilisation.</text>
</svg>
""".strip()

# =============================================================================
# TOPIC 1 LESSON DEFINITIONS (4 LESSONS, EXACTLY 5 PAGES EACH)
# =============================================================================

TOPIC_1_LESSONS = [
    # =========================================================================
    # LESSON 1.1.1: What is Information and Communication Technology?
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "What is Information and Communication Technology?",
        "unit_description": "Foundational principles of ICT: distinguishing data from information, the technological ecosystem, and the 5 essential components of an ICT system.",
        "lesson_title": "What is Information and Communication Technology?",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Modern Interactive Computing Environment",
                    "content": {
                        "title": "Computing Workstation in a Connected Learning Environment",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Desktop_computer_clipart_-_Yellow_theme.svg/800px-Desktop_computer_clipart_-_Yellow_theme.svg.png",
                        "caption": "A modern digital computing setup illustrating the interaction of hardware, software applications, and network connectivity in everyday learning.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Welcome to the World of ICT: Let's Connect",
                    "content": {
                        "text": "Think about the last time you sent a message on a smartphone, checked your school exam results online, or watched an instructional video. In that split second, your fingers triggered a complex sequence of electronic pulses, packet transfers, and database lookups.\n\nIn our modern digital world, being a passive consumer of technology is no longer enough. To innovate and solve community challenges, you must understand the underlying science of data, hardware, and networks. This topic empowers you to step behind the screen and become an active digital creator."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between raw data and processed, meaningful information with concrete examples.\n- Define and explain Data, Information, Communication, Technology, Information Technology (IT), and ICT.\n- Identify and describe the 5 core components of any ICT system: Hardware, Software, Networks, Data, and People.\n- Analyze the multi-component operation of real-world automated systems such as an Automatic Teller Machine (ATM)."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Foundational Terminology: Data vs Information",
                    "content": {
                        "term": "Data and Information",
                        "definition": "Data comprises raw, unprocessed facts, figures, and symbols lacking context. Information is data that has been structured, processed, and given contextual meaning for decision-making.",
                        "simple_explanation": "Think of data as individual unlaid bricks. Information is the completed, functional house built from those bricks.",
                        "technical_meaning": "Data consists of unformatted alphanumeric characters, binary bits, or raw sensor readings. Information is the structured output produced after filtering, aggregation, and computational logic.",
                        "example": "The numbers 24, 10, 2026 are raw data. Structuring them as 'School Science Fair Date: 24th October 2026' transforms them into useful information."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Technology, IT, and ICT Terminology",
                    "content": {
                        "term": "Information and Communication Technology (ICT)",
                        "definition": "The convergence of computing hardware and software (IT) with telecommunication networks (telephone lines, wireless signals, internet) that enables users and systems to access, store, transmit, and manipulate data globally.",
                        "simple_explanation": "IT is a computer managing your local files. ICT is that computer connected to global networks and cell towers to communicate with others worldwide.",
                        "technical_meaning": "An umbrella term integrating telecommunications, broadcast media, intelligent building management systems, and audiovisual processing networks with standard computer infrastructure.",
                        "example": "Checking your mobile bank balance via an app that connects through cell towers to a remote cloud server."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Five Core Pillars of an ICT System",
                    "content": {
                        "text": "An ICT system is never just a solitary laptop on a desk; it is a coordinated ecosystem of five interlinked pillars:\n\n1. **Hardware:** The tangible physical machinery and peripherals (processors, motherboards, input keyboards, displays, storage disks, network interface cards).\n2. **Software:** The programmed digital instructions and algorithms that direct hardware operations (operating systems, web browsers, specialized applications).\n3. **Network:** The communication pathways and protocols connecting devices (Wi-Fi 6, fiber-optic cables, cellular towers, satellite links, TCP/IP routing).\n4. **Data:** The digital payload processed by the system (patient medical records, customer bank balances, meteorological sensor readings).\n5. **People:** The human actors who design, administer, maintain, and interact with the system (software engineers, network technicians, end-users, students).\n\nIn addition, **Procedures** (security policies, backup rules, acceptable use guidelines) govern how people interact with the technology safely."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "The ICT System Ecosystem & Data Processing Cycle",
                    "content": {
                        "title": "The Interactive ICT Ecosystem Flow",
                        "caption": "High-precision architectural diagram showing the continuous transformation of raw data into information, enveloped by hardware, software, network transmission, human actors, and operational procedures.",
                        "svg_content": SVG_ICT_COMPONENTS_CYCLE
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 4-Stage Information Processing Cycle",
                    "content": {
                        "intro": "Every computer system processes data through an unyielding 4-stage operational cycle:",
                        "steps": [
                            {
                                "title": "1. Data Collection & Input",
                                "description": "Raw data is gathered from the physical environment or human users via input devices (keyboards, barcode scanners, touchscreen sensors, RFID readers, microphones)."
                            },
                            {
                                "title": "2. Processing & Computation",
                                "description": "The Central Processing Unit (CPU), guided by software instructions in RAM, transforms, calculates, sorts, filters, and organizes the raw binary data into structured form."
                            },
                            {
                                "title": "3. Output & Presentation",
                                "description": "Processed information is converted into human-intelligible or machine-actionable form on output devices (screens, sound synthesizers, braille terminals, printers, automated relays)."
                            },
                            {
                                "title": "4. Storage & Feedback",
                                "description": "Information is retained on secondary storage (NVMe SSDs, cloud storage arrays) for future retrieval, while feedback loops inform system adjustments."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Case Analysis: The Automated Teller Machine (ATM) System",
                    "content": {
                        "intro": "Consider an ATM transaction at a Kenyan commercial bank. Let us examine how the five ICT components operate in perfect synchrony:",
                        "steps": [
                            "**1. Hardware:** The rugged ATM terminal containing a numeric PIN pad, touch display, magnetic card reader, cash dispenser mechanism, receipt printer, and tamper-resistant cryptographic processor.",
                            "**2. Software:** The embedded banking operating system and transaction software client that displays user prompts, captures inputs, and enforces encryption protocols.",
                            "**3. Network:** A dedicated, encrypted leased line or secure VPN tunnel connecting the ATM terminal to the bank's central core banking servers and the national interbank clearing network.",
                            "**4. Data:** Account card identifiers, cryptographic PIN hashes, account balances, daily withdrawal limits, and real-time transaction ledger entries.",
                            "**5. People & Procedures:** The customer withdrawing money, the bank cash loader, and the system security administrator. Procedures include: maximum 3 PIN attempts before card retention, daily withdrawal limits, and automatic transaction rollback if cash is not dispensed."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Healthcare Digital Transformation: Hospital Patient Records",
                    "content": {
                        "title": "Transitioning from Paper Folders to Integrated Hospital Management Systems",
                        "text": "When a regional hospital in Kenya replaces physical paper folders with an Electronic Medical Records (EMR) system, patient blood types, allergies, and treatment histories (Data) are typed into touch monitors (Hardware) using hospital management software (Software). The local hospital network (Network) instantly shares this critical information between the emergency triage room, laboratory, and pharmacy, ensuring doctors (People) can administer life-saving treatments within seconds while respecting strict patient privacy protocols (Procedures)."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: ICT is Just Another Term for 'Using a Computer'",
                    "content": {
                        "misconception": "Many beginners believe ICT simply means typing a document or playing a game on a standalone desktop computer.",
                        "reality": "Stand-alone computing is basic Information Technology (IT). ICT explicitly emphasizes telecommunication networks and distributed connectivity. As soon as a device connects to local networks, cellular towers, cloud services, or remote databases to exchange information, it operates as an ICT system."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Trap: Treating Uncontextualized Numbers as Information",
                    "content": {
                        "mistake": "Presenting isolated raw figures (such as '38.5' or '102') without labels, units, or contextual metadata and expecting users to make accurate decisions.",
                        "correction": "Always pair raw data points with units of measurement, timestamps, baseline thresholds, and subject tags (e.g., 'Patient Core Body Temp: 38.5°C at 14:00 — Elevated Fever alert').",
                        "reasoning": "Without context and semantic structure, data is ambiguous and prone to dangerous misinterpretation."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Defining ICT",
                    "content": {
                        "question": "Which of the following statements best defines Information and Communication Technology (ICT)?",
                        "options": [
                            "A. The physical metal casing and silicon circuitry of a personal computer.",
                            "B. The convergence of computing systems (IT) and telecommunication networks that enables global data access, storage, and exchange.",
                            "C. The mechanical process of typing letters into a word processor.",
                            "D. An offline electronic calculator used for arithmetic operations."
                        ],
                        "correct": "B",
                        "explanation": "ICT represents the integration of computing technologies (IT) and telecommunication networks (such as the internet and cellular infrastructure), enabling seamless communication and data exchange across distributed systems."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: ICT Component Classification",
                    "content": {
                        "question": "In a digital school library system, which component is represented by the rule requiring students to log out of library terminals after 30 minutes?",
                        "options": [
                            "A. Hardware",
                            "B. Network",
                            "C. Software",
                            "D. Procedures"
                        ],
                        "correct": "D",
                        "explanation": "Procedures are the established rules, guidelines, policies, and operational protocols that govern how humans interact with and secure an ICT system."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Foundations of ICT: Data, Systems, and Networks",
                    "content": {
                        "title": "Introduction to Information and Communication Technology",
                        "youtube_id": "AkFi90lZmXA",
                        "url": "https://www.youtube.com/watch?v=AkFi90lZmXA",
                        "description": "An engaging overview exploring the fundamental difference between data and information, and how telecommunication networks unite computers into global ICT systems."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 1 Key Takeaways",
                    "content": {
                        "text": "- **Data vs Information:** Data is raw and unstructured; Information is processed, organized, contextual, and actionable.\n- **IT vs ICT:** IT centers on local computing, data storage, and processing; ICT expands this by integrating telecommunication channels and network connectivity.\n- **The 5 ICT Pillars:** Hardware (machinery), Software (code/instructions), Networks (connectivity channels), Data (raw payload), and People (users and admins).\n- **Procedures:** The operational rules and security policies that guarantee safe, ethical, and reliable system performance."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 1.2.1: Components of ICT Infrastructure
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Components of ICT Infrastructure",
        "unit_description": "The six foundational pillars of enterprise ICT infrastructure: hardware, system vs application software, networks, data storage, people, and operating procedures.",
        "lesson_title": "Components of ICT Infrastructure",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Enterprise Data Center & Server Infrastructure",
                    "content": {
                        "title": "High-Density Server Racks in an Enterprise Data Center",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/08/Server_room.jpg",
                        "caption": "A high-performance enterprise data center room showing server racks, high-speed fiber patch panels, and specialized cooling infrastructure.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Inside the Digital Engine Room: Let's Connect",
                    "content": {
                        "text": "Imagine entering a modern corporate headquarters or a regional university. Behind the glass windows lies a climate-controlled room with glowing LED indicators, hum of industrial cooling fans, and bundles of fiber-optic cabling connecting rows of server racks.\n\nThis is an organization's **ICT Infrastructure**. Just as a modern city depends on an unseen grid of roads, water mains, and power lines to function, every modern institution relies on its digital infrastructure to store records, process transactions, and communicate with the world."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define ICT Infrastructure and explain its role in modern organizations.\n- Distinguish clearly between System Software and Application Software.\n- Identify and explain the 6 pillars of ICT Infrastructure (Hardware, Software, Networks, Data Storage, People, Procedures).\n- Map out and analyze the complete ICT infrastructure setup of a school computer lab."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "ICT Infrastructure & Software Taxonomy",
                    "content": {
                        "term": "ICT Infrastructure",
                        "definition": "The integrated collection of hardware, software, network resources, data repositories, facilities, and human services required for the existence, operation, and management of an enterprise IT environment.",
                        "simple_explanation": "The entire digital backbone of an organization—computers, cables, programs, storage drives, and IT rules working together.",
                        "technical_meaning": "The composite hardware, software, network resources, and human services required to deliver IT solutions and services to employees, partners, and customers.",
                        "example": "A commercial bank's network of servers, automated teller machines, fiber backbones, database clusters, and cybersecurity policies."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "System Software vs Application Software",
                    "content": {
                        "term": "System vs Application Software",
                        "definition": "System Software manages and controls the computer hardware directly so that other programs can function. Application Software is designed to execute specific user-driven tasks.",
                        "simple_explanation": "System software runs the machine (like Windows or Android); application software helps you do your work (like MS Word, Chrome, or WhatsApp).",
                        "technical_meaning": "System software provides an abstraction layer (HAL, OS kernel, device drivers, UEFI) over physical circuitry. Application software utilizes system APIs to manipulate data for user objectives.",
                        "example": "Linux OS is system software; an accounting ERP package or video editing tool is application software."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Six Foundational Pillars of ICT Infrastructure",
                    "content": {
                        "text": "An enterprise ICT infrastructure is architected upon six interdependent pillars:\n\n1. **Hardware:** The physical computing machinery, client workstations, rackmount servers, uninterruptible power supplies (UPS), and cooling units.\n2. **Software:** The operating system kernels (Linux, Windows Server) and business application suites (databases, web servers, email daemons).\n3. **Networks:** The transmission media (Cat6a Ethernet, optical fiber) and routing devices (managed switches, firewalls, Wi-Fi 6 access points).\n4. **Data Storage:** High-availability local Storage Area Networks (SAN), Network Attached Storage (NAS), and redundant cloud backup archives.\n5. **People:** Certified systems administrators, database managers, cybersecurity analysts, helpdesk technicians, and end-users.\n6. **Procedures:** Documented Standard Operating Procedures (SOPs), access control matrices, password complexity requirements, and automated backup schedules."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Enterprise ICT Infrastructure Layered Architecture",
                    "content": {
                        "title": "The 5-Tier Functional Hierarchy of ICT Infrastructure",
                        "caption": "Multi-tier architectural stack illustrating the dependency flow from physical telecom and hardware up to application software and human governance.",
                        "svg_content": SVG_INFRASTRUCTURE_LAYERS
                    }
                },
                {
                    "type": "step_process",
                    "title": "Infrastructure Dependency Flow: How a User Request Travels the Stack",
                    "content": {
                        "intro": "When a student submits an assignment online, the transaction executes through every layer of the infrastructure stack:",
                        "steps": [
                            {
                                "title": "1. User Action & Governance (Layer 5)",
                                "description": "The student enters credentials into the school portal, authenticated by identity access management procedures."
                            },
                            {
                                "title": "2. Application Logic Execution (Layer 4)",
                                "description": "The School Management System (SMS) web app validates the file format, computes upload checksums, and updates the student ledger."
                            },
                            {
                                "title": "3. OS & System Call Translation (Layer 3)",
                                "description": "The server's Linux operating system handles disk I/O requests, encrypts the file on disk, and delegates memory buffers."
                            },
                            {
                                "title": "4. Hardware Processing & Storage (Layer 2)",
                                "description": "Multi-core server processors execute binary instructions and write data blocks across redundant NVMe storage arrays."
                            },
                            {
                                "title": "5. Network Transport & Telemetry (Layer 1)",
                                "description": "Packets traverse local managed Gigabit switches, through the hardware firewall, and across fiber backbones to cloud backup storage."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Infrastructure Case Study: The School Computer Lab",
                    "content": {
                        "intro": "Let us analyze how a standard 30-computer school laboratory represents a complete enterprise ICT infrastructure:",
                        "steps": [
                            "**1. Hardware:** 30 student desktop workstations, 1 teacher master console, a ceiling-mounted smart projector, and a central heavy-duty network laser printer.",
                            "**2. Software:** Windows 11 Education OS (System Software), Microsoft 365 productivity suite, Python IDEs, and centrally managed antivirus protection (Application Software).",
                            "**3. Network:** Overhead Cat6a Ethernet cabling running to a 48-port managed Gigabit switch, connected to an enterprise firewall router and dual-band Wi-Fi access point.",
                            "**4. Data Storage:** A dedicated local school server running RAID storage with automated overnight off-site cloud backups for student project folders.",
                            "**5. People:** The ICT teacher delivering lessons, 30 students collaborating, and the school IT technician monitoring network traffic.",
                            "**6. Procedures:** Lab rules prohibiting food/drinks, mandatory weekly password updates, USB drive scanning upon insertion, and Friday data backups."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Enterprise Redundancy & Disaster Recovery in Kenyan Banking",
                    "content": {
                        "title": "How Commercial Banks Ensure Zero Downtime",
                        "text": "Kenyan banks maintain primary data centers in Nairobi and secondary disaster recovery sites in other counties (such as Mombasa or Nakuru). If a power outage or physical fault occurs at the primary site, synchronous fiber links and automated failover procedures switch operations to the backup center within milliseconds, ensuring M-Pesa integrations, ATMs, and mobile banking remain available 24/7 without losing a single financial transaction record."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Buying Fast Computers Equals Having Good ICT Infrastructure",
                    "content": {
                        "misconception": "An institution assumes that buying the fastest computers available guarantees a world-class ICT setup.",
                        "reality": "Fast computers are useless if connected to an unmanaged, insecure network, lacking central backup storage, or operated without strict cybersecurity procedures. True ICT infrastructure requires balanced excellence across all six pillars: hardware, software, networks, storage, people, and procedures."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting Trap: Overlooking Backup Protocols and Single Points of Failure",
                    "content": {
                        "mistake": "Storing critical organizational files only on a single local hard drive without automated off-site backups.",
                        "correction": "Implement the industry-standard 3-2-1 backup rule: Maintain at least 3 copies of your data, on 2 different media types, with 1 copy stored securely off-site or in the cloud.",
                        "reasoning": "Hard drives inevitably suffer mechanical wear, power surges, malware encryption (ransomware), or physical theft. Without redundant backups, data loss is permanent."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Infrastructure Pillar Identification",
                    "content": {
                        "question": "Which component of an organization's ICT infrastructure is responsible for establishing password complexity rules, file backup schedules, and acceptable use policies?",
                        "options": [
                            "A. System Hardware",
                            "B. Operating Procedures",
                            "C. Application Software",
                            "D. Network Cabling"
                        ],
                        "correct": "B",
                        "explanation": "Operating Procedures comprise the documented rules, guidelines, protocols, and policies that govern how humans interact with and safeguard the technical infrastructure."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Software Classification",
                    "content": {
                        "question": "Which of the following pairings correctly classifies the software type?",
                        "options": [
                            "A. Linux OS — Application Software; Microsoft Excel — System Software",
                            "B. Google Chrome — System Software; Linux OS — Application Software",
                            "C. Windows 11 — System Software; Microsoft Word — Application Software",
                            "D. Device Driver — Application Software; WhatsApp — System Software"
                        ],
                        "correct": "C",
                        "explanation": "Windows 11 is System Software (operating system controlling the hardware), while Microsoft Word is Application Software (designed for end-user document creation)."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding Enterprise ICT Infrastructure & Networks",
                    "content": {
                        "title": "Inside Data Centers and Enterprise IT Infrastructure",
                        "youtube_id": "1z0ULvg_pW8",
                        "url": "https://www.youtube.com/watch?v=1z0ULvg_pW8",
                        "description": "A visual tour inside modern server rooms, data centers, and network closets explaining how switches, routers, servers, and cooling systems work together."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 2 Key Takeaways",
                    "content": {
                        "text": "- **ICT Infrastructure:** The complete technological backbone (hardware, software, networks, storage, people, procedures) supporting an organization.\n- **Software Taxonomy:** System Software manages hardware resources directly (OS, drivers); Application Software performs specific user tasks (spreadsheets, browsers).\n- **The 6 Pillars:** Hardware (machinery), Software (code), Networks (connectivity), Data Storage (archives), People (admins/users), Procedures (rules/SOPs).\n- **Resilience:** Systems must be designed with redundancy, backup protocols (3-2-1 rule), and strict security governance."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 1.3.1: Using ICT to Interact with Information
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Using ICT to Interact with Information",
        "unit_description": "Navigating digital communication channels, synchronous vs asynchronous platforms, professional email composition, and cloud-based file sharing.",
        "lesson_title": "Using ICT to Interact with Information",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Global Digital Collaboration & Video Conferencing",
                    "content": {
                        "title": "Interactive Remote Collaboration Across Digital Networks",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Video_conference_call_meeting.jpg",
                        "caption": "Professionals engaging in real-time synchronous video collaboration, sharing digital documents, and interacting across distributed network channels.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Navigating the Digital Information Space: Let's Connect",
                    "content": {
                        "text": "Whether you are submitting an assignment to your teacher, attending a virtual class, sharing large research datasets with classmates, or emailing a scholarship committee, you are using communication technology to manipulate and transmit information.\n\nMastering how digital channels operate allows you to convey your ideas with clarity, present yourself professionally, collaborate with peers anywhere on the planet, and troubleshoot communication bottlenecks effectively."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish clearly between Synchronous and Asynchronous digital communication channels.\n- Identify key components of formal digital communication (To, CC, BCC, Subject line, Attachments).\n- Execute a step-by-step procedure to compose and send a professional email with attachments.\n- Troubleshoot common digital file sharing challenges such as email attachment size limits."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Digital Communication Modes: Synchronous vs Asynchronous",
                    "content": {
                        "term": "Synchronous & Asynchronous Communication",
                        "definition": "Synchronous Communication occurs in real-time where all participants interact simultaneously. Asynchronous Communication is store-and-forward communication where participants exchange messages at different times.",
                        "simple_explanation": "Synchronous is like a live phone call or video conference; Asynchronous is like sending an email or posting on a classroom forum where people reply later.",
                        "technical_meaning": "Synchronous systems require concurrent session state and low latency packet delivery (RTP/WebRTC). Asynchronous systems rely on persistent message queues and store-and-forward mail transfer agents (SMTP/IMAP).",
                        "example": "A live Zoom lesson is synchronous; submitting questions to a Google Classroom discussion forum is asynchronous."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Email Protocols & Addressing Terminology",
                    "content": {
                        "term": "Email Header Components (To, CC, BCC)",
                        "definition": "Standardized metadata fields directing message delivery: 'To' indicates primary recipients; 'CC' (Carbon Copy) sends visible courtesy copies; 'BCC' (Blind Carbon Copy) sends invisible copies protecting recipient privacy.",
                        "simple_explanation": "'To' is for the person who needs to act; 'CC' is for people who just need to know; 'BCC' keeps email addresses secret from other recipients.",
                        "technical_meaning": "MIME header fields parsed by Mail Transfer Agents (MTAs). BCC headers are stripped before final envelope delivery to prevent recipient address disclosure.",
                        "example": "Sending a project to your teacher (To:), copying your study partner (CC:), while keeping parent emails confidential (BCC:)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Channels for Interacting with Digital Information",
                    "content": {
                        "text": "Modern ICT provides two primary operational modes for sharing and interacting with information:\n\n1. **Synchronous Channels (Real-Time):**\n- **Video Conferencing:** Zoom, Google Meet, Microsoft Teams for live interactive discussions, screen-sharing, and webinars.\n- **Instant Messaging & VoIP:** WhatsApp, Telegram, Slack for instant peer updates and immediate decision-making.\n- **Key Benefit:** Provides immediate verbal and visual feedback, high engagement, and rapid conflict resolution.\n\n2. **Asynchronous Channels (Time-Shifted):**\n- **Email:** Gmail, Outlook for formal requests, official documentation, and multi-party project handoffs.\n- **Discussion Boards & Portals:** Google Classroom, LMS forums for structured peer debate and recorded feedback.\n- **Cloud Document Collaboration:** Google Drive, OneDrive for version-controlled collaborative document authoring.\n- **Key Benefit:** Creates an archived paper trail, allows thoughtful editing, and accommodates different schedules and time zones."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Digital Information Communication & Transmission Model",
                    "content": {
                        "title": "The Shannon-Weaver Cybernetic Communication Loop",
                        "caption": "Detailed diagram illustrating packet encoding, transmission through noisy mediums, decoding, receiver consumption, and the return feedback loop.",
                        "svg_content": SVG_COMMUNICATION_FLOW
                    }
                },
                {
                    "type": "step_process",
                    "title": "Standard Operating Procedure: Composing a Professional Email",
                    "content": {
                        "intro": "Follow this rigorous 6-step professional procedure when sending academic or workplace emails:",
                        "steps": [
                            {
                                "title": "Step 1: Specify Recipients (To, CC, BCC)",
                                "description": "Type the primary recipient's address in the 'To' field. Add courtesy copies in 'CC' only if necessary. Use 'BCC' when sending to large groups to maintain privacy."
                            },
                            {
                                "title": "Step 2: Craft a Concise, Specific Subject Line",
                                "description": "Write a descriptive subject line containing topic and sender identity (e.g., 'Grade 10 ICT Term 1 Project Submission - Faith Mwangi'). Never leave the subject blank."
                            },
                            {
                                "title": "Step 3: Open with a Formal Salutation",
                                "description": "Begin with a respectful greeting (e.g., 'Dear Mr. Omondi,' or 'Good morning Ms. Kamau,'). Avoid informal slang like 'Hey' in academic communication."
                            },
                            {
                                "title": "Step 4: Write Clear, Structured Message Body",
                                "description": "State your purpose in the first sentence. Use short paragraphs or bullet points to explain details. State clearly if action or feedback is requested."
                            },
                            {
                                "title": "Step 5: Attach Files and Verify Upload Progress",
                                "description": "Click the paperclip attachment icon. Select your file, verify the file name and size, and wait for the upload progress indicator to turn complete."
                            },
                            {
                                "title": "Step 6: Professional Sign-Off & Send",
                                "description": "Close with a formal sign-off (e.g., 'Best regards, [Your Name] - Admission # 1042'). Proofread carefully before clicking the 'Send' button."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Troubleshooting Scenario: Overcoming Email Attachment Size Limits",
                    "content": {
                        "intro": "A student attempts to email a 180MB video presentation to their teacher, but the email client displays an error: 'Attachment exceeds the 25MB maximum limit.'",
                        "steps": [
                            "**Step 1 — Understand the Technical Constraint:** Most standard email servers (SMTP) restrict direct message attachments to 20MB - 25MB to prevent network saturation and mailbox storage overflow.",
                            "**Step 2 — Leverage Cloud Storage:** Open your authorized school cloud drive (such as Google Drive, Microsoft OneDrive, or Dropbox) and upload the 180MB video file.",
                            "**Step 3 — Configure Access Permissions:** Right-click the uploaded file, select 'Share', and configure access to 'Anyone with the link can view' or restrict access specifically to your teacher's email address.",
                            "**Step 4 — Embed the Cloud Link in Email Body:** Copy the secure shareable URL, return to your email composer, and insert the link into your message body text (e.g., 'Please access my 180MB video project via this secure Google Drive link: [Link]').",
                            "**Step 5 — Verify and Send:** Click the link in your draft to confirm it opens the correct file without requiring extra permission requests, then send the email."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Hybrid Workplace Collaboration: Combining Synchronous and Asynchronous ICT",
                    "content": {
                        "title": "How Distributed Software Engineering Teams Collaborate",
                        "text": "Global technology teams spread across Nairobi, London, and Tokyo coordinate complex software builds using a combination of channels. They use asynchronous platforms (GitHub code repositories and Jira tickets) so developers can write code and log documentation across different time zones, paired with a daily 15-minute synchronous video standup (Zoom/Google Meet) to resolve roadblocks in real time."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Email is Intended as an Instant Messaging Tool",
                    "content": {
                        "misconception": "Because emails arrive on smartphones quickly, many people treat email like a live chat and expect replies within minutes.",
                        "reality": "Email is architected as an asynchronous store-and-forward medium. Professional etiquette establishes a standard turnaround time of up to 24 to 48 business hours for email responses. If an urgent, immediate response is required, synchronous channels (phone call, direct message) should be utilized."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Sending Emails with Missing Attachments or Broken Links",
                    "content": {
                        "mistake": "Writing 'Please find attached my document' and clicking 'Send' without attaching the file or while cloud permissions are set to private.",
                        "correction": "Attach your document before writing the body text, and always test shared cloud links in a private/incognito browser window to ensure permissions are open.",
                        "reasoning": "Sending missing attachments wastes time, creates unnecessary back-and-forth communication, and projects an unprofessional image."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Communication Mode Classification",
                    "content": {
                        "question": "Which of the following represents an asynchronous digital communication platform?",
                        "options": [
                            "A. A live interactive Zoom video lecture.",
                            "B. A student posting a question on an LMS discussion board for peer replies.",
                            "C. A real-time WhatsApp voice phone call.",
                            "D. A live instant chat room active during a broadcast."
                        ],
                        "correct": "B",
                        "explanation": "An LMS discussion board is asynchronous because participants do not need to be online at the same time; messages are stored and read at the recipients' convenience."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Email Addressing Etiquette",
                    "content": {
                        "question": "When sending a project announcement to 50 parent email addresses, which field should be used to protect their private contact details from being exposed to each other?",
                        "options": [
                            "A. To field",
                            "B. CC (Carbon Copy) field",
                            "C. Subject field",
                            "D. BCC (Blind Carbon Copy) field"
                        ],
                        "correct": "D",
                        "explanation": "The BCC (Blind Carbon Copy) field conceals recipient email addresses from other recipients, preserving privacy and complying with data protection standards."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Mastering Professional Email & Digital Communication",
                    "content": {
                        "title": "How to Write Professional Emails and Share Digital Files",
                        "youtube_id": "gU_Q0f5mD5w",
                        "url": "https://www.youtube.com/watch?v=gU_Q0f5mD5w",
                        "description": "A practical tutorial covering professional email etiquette, structuring subject lines, managing CC vs BCC, and sharing large cloud storage attachments."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3 Key Takeaways",
                    "content": {
                        "text": "- **Communication Modes:** Synchronous occurs in real time (video calls, voice chat); Asynchronous is time-shifted (email, discussion boards, recorded media).\n- **Email Architecture:** 'To' for primary action, 'CC' for public copies, 'BCC' for private group mailings, and a mandatory descriptive subject line.\n- **Large File Sharing:** Bypassing 25MB email attachment limits by uploading to cloud storage (Google Drive/OneDrive) and embedding shareable links.\n- **Digital Etiquette:** Proofread drafts, maintain formal salutations, verify attachments, and respect professional response timeframes."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 1.4.1: Importance of ICT in Society
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Importance of ICT in Society",
        "unit_description": "Societal impact of ICT across key sectors (education, commerce, healthcare, governance, agriculture), Kenyan innovations (M-Pesa, eCitizen), and bridging the digital divide.",
        "lesson_title": "Importance of ICT in Society",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Digital Transformation & Mobile Money in Kenya",
                    "content": {
                        "title": "M-Pesa Agent & Mobile Financial Services in Everyday Kenyan Commerce",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/KICC_Nairobi.jpg",
                        "caption": "The Nairobi commercial skyline, symbolizing Kenya's regional leadership as Africa's 'Silicon Savannah' powered by digital innovation and mobile financial systems.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "A World Transformed by ICT: Let's Connect",
                    "content": {
                        "text": "Imagine waking up in a world with no mobile money, no internet, no online maps, and no digital portals. To pay an electricity bill, you would stand in a physical banking queue for three hours. To research a historical event, you would spend days browsing paper library cards.\n\nToday, you perform these tasks in milliseconds from the palm of your hand. ICT has restructured modern civilization, driving economic productivity, expanding access to essential public services, and opening unprecedented career opportunities worldwide."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Analyze the transformative impact of ICT across Education, Commerce, Healthcare, Governance, and Agriculture.\n- Explain landmark Kenyan ICT innovations including M-Pesa mobile money and the eCitizen government portal.\n- Define the Digital Divide and evaluate strategies to bridge socioeconomic technology gaps.\n- Formulate ICT-driven solutions to solve real-world community and agricultural challenges."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Socioeconomic ICT Terminology",
                    "content": {
                        "term": "The Digital Divide",
                        "definition": "The economic, educational, and social gap between individuals, households, and geographic areas that have access to modern digital technologies and internet connectivity, and those who do not.",
                        "simple_explanation": "The gap between people who have fast internet and modern computers, and people who are left behind without digital tools.",
                        "technical_meaning": "A multidimensional disparity encompassing physical access to high-speed broadband and computing hardware, digital literacy competencies, and the economic ability to leverage digital services.",
                        "example": "An urban student with high-speed fiber internet and a laptop compared to a rural student with no electricity and no computer access."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Electronic Service Models (E-Commerce, E-Gov, Telemedicine)",
                    "content": {
                        "term": "E-Commerce, E-Government & Telemedicine",
                        "definition": "The digital delivery of commercial trade, public government services, and clinical healthcare over telecommunication networks.",
                        "simple_explanation": "Using websites and apps to shop (e-commerce), renew driving licenses (e-government), or consult a remote doctor (telemedicine).",
                        "technical_meaning": "Network-enabled service architectures replacing physical counters with encrypted web interfaces, automated databases, and mobile payment gateways.",
                        "example": "Applying for a passport on the eCitizen platform, paying via M-Pesa, and receiving a digital appointment slip."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Transformative Impact Across Key Societal Sectors",
                    "content": {
                        "text": "ICT has fundamentally transformed the core pillars of society:\n\n1. **Education (E-Learning):** Digital learning systems (VLearn, Google Classroom, Wikipedia) dismantle geographical barriers, allowing students to access world-class textbooks, instructional videos, and virtual science laboratories anytime.\n2. **Financial Services & Commerce:** Mobile money platforms (**M-Pesa**) eliminated the need for physical bank branches, bringing financial inclusion to millions of unbanked citizens, while e-commerce platforms connect local craftsmen to global buyers.\n3. **Healthcare (Telemedicine):** Doctors in central hospitals conduct video consultations with patients in remote rural clinics, and centralized Electronic Health Records ensure patient history is instantly available during emergencies.\n4. **Public Governance (eCitizen):** Kenya's unified **eCitizen** portal allows citizens to apply for national IDs, passports, business registration, and driving licenses online, cutting bureaucratic bribery, paper loss, and transit costs.\n5. **Agriculture & Food Security:** Smart farming apps provide farmers with real-time weather forecasts, market crop prices, and automated soil sensor telemetry to optimize irrigation and fertilizer application."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Societal Impact of ICT Across Key Economic & Civic Sectors",
                    "content": {
                        "title": "The 8 Dimensions of ICT Impact in Modern Society",
                        "caption": "Comprehensive radial mind map illustrating how ICT accelerates education, healthcare, e-government, agriculture, transportation, and commerce while highlighting the digital divide.",
                        "svg_content": SVG_ICT_IMPACT_AREAS
                    }
                },
                {
                    "type": "step_process",
                    "title": "Digital Service Delivery Cycle: How eCitizen Processes Public Requests",
                    "content": {
                        "intro": "The modern digital public service model replaces manual queues with an automated 5-step transaction lifecycle:",
                        "steps": [
                            {
                                "title": "1. Single Sign-On Authentication",
                                "description": "The citizen logs in securely using their National ID number and Two-Factor Authentication (2FA) SMS code."
                            },
                            {
                                "title": "2. Digital Application Submission",
                                "description": "The applicant fills out standardized electronic forms and uploads digital passport photos and supporting documents."
                            },
                            {
                                "title": "3. Real-Time Payment Gateway (M-Pesa API)",
                                "description": "An automated prompt pushes an M-Pesa STK PIN prompt to the user's mobile phone, confirming payment instantly."
                            },
                            {
                                "title": "4. Automated Back-Office Verification",
                                "description": "Government database queries cross-reference birth records, tax compliance (KRA), and police clearance certificates."
                            },
                            {
                                "title": "5. Digital Credential Issuance",
                                "description": "A digitally signed, QR-code-verified permit or certificate is generated and sent to the citizen's profile within minutes."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Community Solutions: Empowering Smallholder Farmers with ICT",
                    "content": {
                        "intro": "A smallholder maize farmer in Trans-Nzoia County struggles with fluctuating crop prices, middlemen exploitation, and irregular rainfall. Let us design an ICT-driven intervention:",
                        "steps": [
                            "**1. Market Price Transparency via Mobile USSD/SMS:** The farmer dials a mobile USSD code (*#) or uses an agricultural mobile app to query real-time wholesale maize prices in Kitale, Eldoret, and Nairobi, preventing middlemen from underpaying.",
                            "**2. IoT Soil & Weather Telemetry:** Low-cost solar-powered soil moisture probes placed in the fields send SMS alerts to the farmer's phone indicating when irrigation or nitrogen top-dressing is needed based on satellite rain forecasts.",
                            "**3. Direct Cashless Payments (M-Pesa):** When selling produce to millers, payments are credited directly into the farmer's mobile wallet, eliminating the risks of carrying physical cash or travelling miles to bank branches.",
                            "**4. Impact Assessment:** Yields increase by 25% due to data-driven watering, and net profit margins improve by 30% through direct market pricing."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Kenyan Global Flagship: The M-Pesa Mobile Financial Revolution",
                    "content": {
                        "title": "From SMS Airtime Transfer to the World's Leading Mobile Money Network",
                        "text": "Launched in Kenya in 2007 by Safaricom, M-Pesa allowed mobile phone users to deposit, withdraw, and transfer funds using simple SMS technology without needing a traditional bank account. Today, M-Pesa processes billions of transactions annually across Africa, boosting financial inclusion from under 20% in 2006 to over 85% today, and serving as a global case study in technological empowerment."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Widespread Smartphone Use Means the Digital Divide is Solved",
                    "content": {
                        "misconception": "Because many people own low-cost mobile phones, people assume the digital divide no longer exists.",
                        "reality": "Owning a basic phone does not bridge the divide. Deep disparities remain in access to reliable high-speed broadband, personal laptops for complex coding/writing, uninterrupted electricity, and advanced digital literacy skills required for high-paying technical jobs."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Design Trap: Assuming All Community ICT Solutions Require High-Cost Hardware",
                    "content": {
                        "mistake": "Designing public community software that only works on high-end laptops or requires fast 5G broadband connections.",
                        "correction": "Adopt inclusive, low-bandwidth design principles: develop USSD (*#) codes, SMS gateways, and offline-first mobile applications that function seamlessly on basic 2G/3G feature phones.",
                        "reasoning": "Universal accessibility ensures that public services and agricultural tools reach every citizen, regardless of their economic status."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Understanding the Digital Divide",
                    "content": {
                        "question": "What is the 'Digital Divide'?",
                        "options": [
                            "A. The physical cable connecting a computer motherboard to the monitor.",
                            "B. The socioeconomic gap between communities that have full access to modern digital technologies and the internet, and those that do not.",
                            "C. The process of dividing large database files across multiple cloud storage drives.",
                            "D. A cybersecurity firewall that divides safe internal networks from untrusted public networks."
                        ],
                        "correct": "B",
                        "explanation": "The digital divide is the socioeconomic inequality separating those with reliable access to computing hardware, high-speed internet, and digital literacy from those without."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: ICT in Agricultural Value Chains",
                    "content": {
                        "question": "Which of the following is the most direct benefit of mobile market information platforms for smallholder farmers?",
                        "options": [
                            "A. They automatically harvest crops using robotic drones.",
                            "B. They eliminate the need for agricultural fertilizers.",
                            "C. They provide real-time crop market prices, preventing exploitation by predatory middlemen.",
                            "D. They replace physical seeds with synthetic digital seeds."
                        ],
                        "correct": "C",
                        "explanation": "Mobile price telemetry platforms empower rural farmers with real-time wholesale pricing data across urban centers, ensuring they receive fair market value for their harvests."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Power of ICT in Society: M-Pesa & Digital Transformation",
                    "content": {
                        "title": "How Mobile Money and Digital Platforms Changed Kenya and the World",
                        "youtube_id": "vJjL02xL3h4",
                        "url": "https://www.youtube.com/watch?v=vJjL02xL3h4",
                        "description": "An inspiring documentary highlighting how Kenyan innovations like M-Pesa and eCitizen revolutionized digital financial inclusion, public service delivery, and community empowerment."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 4 Key Takeaways",
                    "content": {
                        "text": "- **Societal Transformation:** ICT modernizes Education (e-learning), Commerce (fintech/M-Pesa), Healthcare (telemedicine), Governance (eCitizen), and Agriculture (smart farming).\n- **Kenyan Innovations:** M-Pesa pioneered global mobile financial inclusion; eCitizen replaced physical bureaucracy with transparent, instant public service delivery.\n- **The Digital Divide:** The gap in technology access and digital skills must be actively addressed through inclusive design (USSD, SMS, low-bandwidth tools) and universal rural connectivity.\n- **Empowerment:** Understanding ICT allows learners to become active creators of solutions that solve real community challenges."
                    }
                }
            ]
        ]
    }
]
