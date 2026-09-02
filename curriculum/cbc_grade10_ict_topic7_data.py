"""
VLearn CBC Grade 10 ICT — Topic 7: Introduction to the Internet
Full Structured Lesson Card Definitions (Lessons 7.1.1 to 7.1.5)
"""

import re

def sanitize_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# HIGH PRECISION VECTOR SVGS FOR TOPIC 7: INTRODUCTION TO THE INTERNET
# =====================================================================

SVG_INTERNET_INTRANET_EXTRANET = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Network Boundary Architecture: Intranet vs. Extranet vs. Internet</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing organizational network accessibility, security perimeters, user roles, and authentication gateways</text>

  <!-- Left: Concentric Boundary Visualizer -->
  <g transform="translate(45, 95)">
    <rect width="430" height="385" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="215" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">CONCENTRIC SECURITY &amp; ACCESS ZONES</text>

    <!-- Zone 3 (Outermost): The Internet -->
    <circle cx="215" cy="210" r="165" fill="#0284c7" fill-opacity="0.12" stroke="#0ea5e9" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="215" y="72" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">ZONE 3: THE INTERNET (PUBLIC WAN)</text>
    <text x="215" y="86" font-size="9" fill="#94a3b8" text-anchor="middle">Global Public Network • Unrestricted Global Access • Billions of Nodes</text>

    <!-- Zone 2 (Middle): The Extranet -->
    <circle cx="215" cy="225" r="115" fill="#f59e0b" fill-opacity="0.12" stroke="#f59e0b" stroke-width="2"/>
    <text x="215" y="132" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">ZONE 2: EXTRANET (SEMI-PRIVATE)</text>
    <text x="215" y="146" font-size="9" fill="#cbd5e1" text-anchor="middle">Authorized External Partners, Suppliers &amp; Parents • Secure VPN / SSL</text>

    <!-- Zone 1 (Innermost): The Intranet -->
    <circle cx="215" cy="250" r="65" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="2.5"/>
    <text x="215" y="235" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">ZONE 1: INTRANET</text>
    <text x="215" y="250" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">(INTERNAL / PRIVATE)</text>
    <text x="215" y="266" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Staff &amp; Students Only</text>
    <text x="215" y="278" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Protected by Firewall</text>

    <!-- Traffic Arrows & Indicators -->
    <g transform="translate(60, 310)">
      <rect width="140" height="42" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="70" y="17" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">✓ Intranet ➔ Public Web</text>
      <text x="70" y="32" font-size="8" fill="#94a3b8" text-anchor="middle">Allowed via Proxy/NAT</text>
    </g>

    <g transform="translate(230, 310)">
      <rect width="140" height="42" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="70" y="17" font-size="8.5" font-weight="bold" fill="#f87171" text-anchor="middle">✗ Public ➔ Intranet</text>
      <text x="70" y="32" font-size="8" fill="#94a3b8" text-anchor="middle">Blocked by Firewall</text>
    </g>
  </g>

  <!-- Right: Detailed Architectural Comparison Matrix -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#0369a1"/>
    <text x="210" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">NETWORK CHARACTERISTICS &amp; ACCESS MATRIX</text>

    <!-- Intranet Card -->
    <g transform="translate(15, 42)">
      <rect width="390" height="95" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <rect x="10" y="8" width="80" height="20" rx="4" fill="#065f46"/>
      <text x="50" y="22" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">INTRANET</text>
      <text x="100" y="22" font-size="11" font-weight="bold" fill="#ffffff">Private Organizational Network</text>
      
      <text x="12" y="45" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#38bdf8">Audience:</tspan> Internal members only (teachers, students, employees).</text>
      <text x="12" y="62" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#38bdf8">Security:</tspan> Strict perimeter firewall, internal authentication, no public access.</text>
      <text x="12" y="79" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#38bdf8">Kenya Example:</tspan> School grading database &amp; internal staff noticeboard.</text>
    </g>

    <!-- Extranet Card -->
    <g transform="translate(15, 148)">
      <rect width="390" height="95" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <rect x="10" y="8" width="80" height="20" rx="4" fill="#78350f"/>
      <text x="50" y="22" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">EXTRANET</text>
      <text x="100" y="22" font-size="11" font-weight="bold" fill="#ffffff">Controlled Semi-Private Gateway</text>
      
      <text x="12" y="45" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#fbbf24">Audience:</tspan> Authorized external stakeholders (parents, suppliers, auditors).</text>
      <text x="12" y="62" font-size="9.5" fill="#fbbf24">• <tspan font-weight="bold" fill="#fbbf24">Security:</tspan> Multi-Factor Authentication (MFA), encrypted VPN tunnels.</text>
      <text x="12" y="79" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#fbbf24">Kenya Example:</tspan> School parent portal for fee payment &amp; student report cards.</text>
    </g>

    <!-- Internet Card -->
    <g transform="translate(15, 254)">
      <rect width="390" height="115" rx="8" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
      <rect x="10" y="8" width="80" height="20" rx="4" fill="#075985"/>
      <text x="50" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">INTERNET</text>
      <text x="100" y="22" font-size="11" font-weight="bold" fill="#ffffff">Global Public Network of Networks</text>
      
      <text x="12" y="45" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#38bdf8">Audience:</tspan> Global public across the world; any connected computing device.</text>
      <text x="12" y="62" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#38bdf8">Security:</tspan> Public routing protocols (TCP/IP, BGP), HTTPS encryption.</text>
      <text x="12" y="79" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#38bdf8">Kenya Example:</tspan> Public KICD educational portal (kicd.ac.ke) &amp; eCitizen.</text>
      <text x="12" y="96" font-size="9" fill="#94a3b8">Infrastructure: Undersea fiber optic cables, satellite links, and IXPs.</text>
    </g>
  </g>
</svg>
""")

SVG_URL_DECONSTRUCTION_ARCHITECTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Anatomy &amp; Deconstruction of a Uniform Resource Locator (URL)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Dissecting web address components, DNS resolution flow, and the HTTP request-response cycle</text>

  <!-- Top: URL Breakdown Visual Display -->
  <g transform="translate(45, 90)">
    <rect width="870" height="145" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="25" y="28" font-size="12" font-weight="bold" fill="#38bdf8">EXAMPLE URL: https://www.kicd.ac.ke:443/curriculum/grade10/syllabus.html?view=full#topic7</text>

    <!-- URL Component Badges Row -->
    <g transform="translate(20, 45)">
      <!-- Scheme/Protocol -->
      <g transform="translate(0, 0)">
        <rect width="85" height="34" rx="6" fill="#0284c7"/>
        <text x="42" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">https://</text>
        <text x="42" y="48" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Protocol</text>
        <text x="42" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Secure SSL)</text>
      </g>

      <!-- Subdomain -->
      <g transform="translate(90, 0)">
        <rect width="60" height="34" rx="6" fill="#d97706"/>
        <text x="30" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">www.</text>
        <text x="30" y="48" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Subdomain</text>
        <text x="30" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Host server)</text>
      </g>

      <!-- Domain Name -->
      <g transform="translate(155, 0)">
        <rect width="70" height="34" rx="6" fill="#059669"/>
        <text x="35" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">kicd</text>
        <text x="35" y="48" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Domain</text>
        <text x="35" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Entity Name)</text>
      </g>

      <!-- 2nd Level Domain (Category) -->
      <g transform="translate(230, 0)">
        <rect width="50" height="34" rx="6" fill="#7c3aed"/>
        <text x="25" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">.ac</text>
        <text x="25" y="48" font-size="9" font-weight="bold" fill="#a78bfa" text-anchor="middle">Category</text>
        <text x="25" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Academic)</text>
      </g>

      <!-- ccTLD -->
      <g transform="translate(285, 0)">
        <rect width="50" height="34" rx="6" fill="#db2777"/>
        <text x="25" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">.ke</text>
        <text x="25" y="48" font-size="9" font-weight="bold" fill="#f472b6" text-anchor="middle">ccTLD</text>
        <text x="25" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Kenya)</text>
      </g>

      <!-- Port -->
      <g transform="translate(340, 0)">
        <rect width="55" height="34" rx="6" fill="#475569"/>
        <text x="27" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">:443</text>
        <text x="27" y="48" font-size="9" font-weight="bold" fill="#94a3b8" text-anchor="middle">Port</text>
        <text x="27" y="60" font-size="8" fill="#cbd5e1" text-anchor="middle">(Default HTTPS)</text>
      </g>

      <!-- Directory Path -->
      <g transform="translate(400, 0)">
        <rect width="170" height="34" rx="6" fill="#0891b2"/>
        <text x="85" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">/curriculum/grade10/</text>
        <text x="85" y="48" font-size="9" font-weight="bold" fill="#22d3ee" text-anchor="middle">Path / Directory</text>
        <text x="85" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Server Folder Hierarchy)</text>
      </g>

      <!-- Resource / Filename -->
      <g transform="translate(575, 0)">
        <rect width="110" height="34" rx="6" fill="#ca8a04"/>
        <text x="55" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">syllabus.html</text>
        <text x="55" y="48" font-size="9" font-weight="bold" fill="#facc15" text-anchor="middle">Resource File</text>
        <text x="55" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Target Webpage)</text>
      </g>

      <!-- Query String -->
      <g transform="translate(690, 0)">
        <rect width="80" height="34" rx="6" fill="#65a30d"/>
        <text x="40" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">?view=full</text>
        <text x="40" y="48" font-size="9" font-weight="bold" fill="#a3e635" text-anchor="middle">Query String</text>
        <text x="40" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Parameters)</text>
      </g>

      <!-- Fragment / Anchor -->
      <g transform="translate(775, 0)">
        <rect width="65" height="34" rx="6" fill="#ea580c"/>
        <text x="32" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#topic7</text>
        <text x="32" y="48" font-size="9" font-weight="bold" fill="#fb923c" text-anchor="middle">Fragment</text>
        <text x="32" y="60" font-size="8" fill="#94a3b8" text-anchor="middle">(Page Section)</text>
      </g>
    </g>
  </g>

  <!-- Bottom Left: DNS Resolution Workflow -->
  <g transform="translate(45, 250)">
    <rect width="425" height="230" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="425" height="30" rx="8" fill="#059669"/>
    <text x="212" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. DOMAIN NAME SYSTEM (DNS) RESOLUTION FLOW</text>

    <g transform="translate(15, 40)">
      <text x="0" y="16" font-size="10" font-weight="bold" fill="#34d399">Step A: User enters URL</text>
      <text x="130" y="16" font-size="9.5" fill="#cbd5e1">➔ Browser queries Local DNS Resolver Cache.</text>

      <text x="0" y="42" font-size="10" font-weight="bold" fill="#34d399">Step B: Root Server Query</text>
      <text x="135" y="42" font-size="9.5" fill="#cbd5e1">➔ Queries Root Servers (.) for .ke TLD location.</text>

      <text x="0" y="68" font-size="10" font-weight="bold" fill="#34d399">Step C: ccTLD Registry</text>
      <text x="130" y="68" font-size="9.5" fill="#cbd5e1">➔ KeNIC Registry delegates to authoritative server.</text>

      <text x="0" y="94" font-size="10" font-weight="bold" fill="#34d399">Step D: Authoritative DNS</text>
      <text x="140" y="94" font-size="9.5" fill="#cbd5e1">➔ Returns exact IP address: 102.219.208.14.</text>

      <rect x="0" y="112" width="395" height="36" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="197" y="127" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">DNS translates human names (kicd.ac.ke) into machine IP addresses!</text>
      <text x="197" y="141" font-size="8.5" fill="#94a3b8" text-anchor="middle">Without DNS, users would have to memorize complex numerical IP addresses.</text>
    </g>
  </g>

  <!-- Bottom Right: Client-Server HTTP/HTTPS Cycle -->
  <g transform="translate(490, 250)">
    <rect width="425" height="230" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="425" height="30" rx="8" fill="#0284c7"/>
    <text x="212" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CLIENT-SERVER HTTP/HTTPS TRANSACTION CYCLE</text>

    <g transform="translate(15, 40)">
      <!-- Client box -->
      <rect x="10" y="10" width="100" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="60" y="32" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Client Device</text>
      <text x="60" y="50" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Web Browser</text>
      <text x="60" y="70" font-size="8.5" fill="#94a3b8" text-anchor="middle">(Chrome, Safari)</text>

      <!-- Arrows -->
      <g transform="translate(120, 25)">
        <line x1="0" y1="10" x2="140" y2="10" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="140,7 148,10 140,13" fill="#38bdf8"/>
        <text x="70" y="5" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. HTTP GET /syllabus.html</text>
      </g>

      <g transform="translate(120, 65)">
        <line x1="148" y1="10" x2="8" y2="10" stroke="#34d399" stroke-width="2"/>
        <polygon points="8,7 0,10 8,13" fill="#34d399"/>
        <text x="78" y="25" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">2. HTTP 200 OK (HTML/CSS)</text>
      </g>

      <!-- Server box -->
      <rect x="280" y="10" width="105" height="90" rx="8" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
      <text x="332" y="32" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Web Server</text>
      <text x="332" y="50" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Apache / Nginx</text>
      <text x="332" y="70" font-size="8.5" fill="#94a3b8" text-anchor="middle">Hosts Web Assets</text>

      <!-- Bottom Note -->
      <rect x="0" y="112" width="395" height="36" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="197" y="127" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">HTTPS encrypts payload data using TLS encryption certificates!</text>
      <text x="197" y="141" font-size="8.5" fill="#94a3b8" text-anchor="middle">Protects passwords, financial transactions, and school records from eavesdroppers.</text>
    </g>
  </g>
</svg>
""")

SVG_INTERNET_CONNECTION_CHAIN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">End-to-End Internet Connection Architecture &amp; Hardware Chain</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How client packets travel from local devices through routers, modems, ISP nodes, and undersea fiber to global servers</text>

  <!-- 5 Nodes Pipeline -->
  <!-- Node 1: Client Devices -->
  <g transform="translate(45, 95)">
    <rect width="150" height="230" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="150" height="30" rx="6" fill="#0284c7"/>
    <text x="75" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CLIENT DEVICE</text>
    
    <circle cx="75" cy="65" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="75" y="72" font-size="18" text-anchor="middle">💻</text>
    
    <text x="12" y="110" font-size="10" font-weight="bold" fill="#38bdf8">• Hardware:</text>
    <text x="12" y="125" font-size="8.5" fill="#cbd5e1">PC, Laptop, Phone.</text>
    
    <text x="12" y="150" font-size="10" font-weight="bold" fill="#38bdf8">• NIC Card:</text>
    <text x="12" y="165" font-size="8.5" fill="#cbd5e1">Wi-Fi (802.11) or</text>
    <text x="12" y="178" font-size="8.5" fill="#cbd5e1">Ethernet (RJ-45).</text>
    
    <rect x="10" y="195" width="130" height="22" rx="4" fill="#1e293b"/>
    <text x="75" y="210" font-size="8.5" fill="#94a3b8" text-anchor="middle">Unique MAC Address</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 200 210 L 225 210" stroke="#38bdf8" stroke-width="3" fill="none"/>

  <!-- Node 2: Wireless Router -->
  <g transform="translate(230, 95)">
    <rect width="150" height="230" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="150" height="30" rx="6" fill="#059669"/>
    <text x="75" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. LOCAL ROUTER</text>
    
    <circle cx="75" cy="65" r="22" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="75" y="72" font-size="18" text-anchor="middle">📶</text>
    
    <text x="12" y="110" font-size="10" font-weight="bold" fill="#34d399">• Traffic Control:</text>
    <text x="12" y="125" font-size="8.5" fill="#cbd5e1">Directs LAN data.</text>
    
    <text x="12" y="150" font-size="10" font-weight="bold" fill="#34d399">• DHCP Server:</text>
    <text x="12" y="165" font-size="8.5" fill="#cbd5e1">Assigns Local IPs</text>
    <text x="12" y="178" font-size="8.5" fill="#cbd5e1">(192.168.1.x).</text>
    
    <rect x="10" y="195" width="130" height="22" rx="4" fill="#1e293b"/>
    <text x="75" y="210" font-size="8.5" fill="#94a3b8" text-anchor="middle">NAT &amp; Local Firewall</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 385 210 L 410 210" stroke="#34d399" stroke-width="3" fill="none"/>

  <!-- Node 3: Modem / ONT -->
  <g transform="translate(415, 95)">
    <rect width="150" height="230" rx="10" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="150" height="30" rx="6" fill="#d97706"/>
    <text x="75" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. MODEM / ONT</text>
    
    <circle cx="75" cy="65" r="22" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="75" y="72" font-size="18" text-anchor="middle">📟</text>
    
    <text x="12" y="110" font-size="10" font-weight="bold" fill="#fbbf24">• Signal Translator:</text>
    <text x="12" y="125" font-size="8.5" fill="#cbd5e1">Modulates/Demodulates</text>
    <text x="12" y="138" font-size="8.5" fill="#cbd5e1">Digital ➔ Analog.</text>
    
    <text x="12" y="158" font-size="10" font-weight="bold" fill="#fbbf24">• Optical Terminal:</text>
    <text x="12" y="173" font-size="8.5" fill="#cbd5e1">Converts light pulses</text>
    <text x="12" y="186" font-size="8.5" fill="#cbd5e1">to digital Ethernet.</text>
    
    <rect x="10" y="195" width="130" height="22" rx="4" fill="#1e293b"/>
    <text x="75" y="210" font-size="8.5" fill="#94a3b8" text-anchor="middle">Physical Link Gateway</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 570 210 L 595 210" stroke="#fbbf24" stroke-width="3" fill="none"/>

  <!-- Node 4: ISP Gateway -->
  <g transform="translate(600, 95)">
    <rect width="150" height="230" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="150" height="30" rx="6" fill="#7e22ce"/>
    <text x="75" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. ISP GATEWAY</text>
    
    <circle cx="75" cy="65" r="22" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
    <text x="75" y="72" font-size="18" text-anchor="middle">🏢</text>
    
    <text x="12" y="110" font-size="10" font-weight="bold" fill="#a78bfa">• Service Provider:</text>
    <text x="12" y="125" font-size="8.5" fill="#cbd5e1">Safaricom, Faiba,</text>
    <text x="12" y="138" font-size="8.5" fill="#cbd5e1">Airtel, Telkom Kenya.</text>
    
    <text x="12" y="158" font-size="10" font-weight="bold" fill="#a78bfa">• Core Routing:</text>
    <text x="12" y="173" font-size="8.5" fill="#cbd5e1">Routes packets to</text>
    <text x="12" y="186" font-size="8.5" fill="#cbd5e1">Kenya IXP (KIXP).</text>
    
    <rect x="10" y="195" width="130" height="22" rx="4" fill="#1e293b"/>
    <text x="75" y="210" font-size="8.5" fill="#94a3b8" text-anchor="middle">Assigns Public IP</text>
  </g>

  <!-- Arrow 4 -> 5 -->
  <path d="M 755 210 L 780 210" stroke="#a855f7" stroke-width="3" fill="none"/>

  <!-- Node 5: Global Backbone -->
  <g transform="translate(785, 95)">
    <rect width="130" height="230" rx="10" fill="#0f172a" stroke="#f472b6" stroke-width="1.5"/>
    <rect width="130" height="30" rx="6" fill="#be185d"/>
    <text x="65" y="20" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5. GLOBAL CLOUD</text>
    
    <circle cx="65" cy="65" r="22" fill="#1e293b" stroke="#f472b6" stroke-width="1"/>
    <text x="65" y="72" font-size="18" text-anchor="middle">🌐</text>
    
    <text x="10" y="110" font-size="9.5" font-weight="bold" fill="#f472b6">• Undersea Cables:</text>
    <text x="10" y="125" font-size="8" fill="#cbd5e1">TEAMS, SEACOM,</text>
    <text x="10" y="138" font-size="8" fill="#cbd5e1">EASSy, DARE1.</text>
    
    <text x="10" y="158" font-size="9.5" font-weight="bold" fill="#f472b6">• Destinations:</text>
    <text x="10" y="173" font-size="8.5" fill="#cbd5e1">Cloud Web Servers,</text>
    <text x="10" y="186" font-size="8.5" fill="#cbd5e1">Datacenters, CDNs.</text>
    
    <rect x="10" y="195" width="110" height="22" rx="4" fill="#1e293b"/>
    <text x="65" y="210" font-size="8" fill="#94a3b8" text-anchor="middle">Global Internet Tier 1</text>
  </g>

  <!-- Bottom: Transmission Media Comparison Bar -->
  <g transform="translate(45, 345)">
    <rect width="870" height="140" rx="12" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="25" y="24" font-size="12" font-weight="bold" fill="#38bdf8">TRANSMISSION MEDIA COMPARISON: SPEED, LATENCY &amp; RELIABILITY</text>

    <!-- Fiber Optic -->
    <g transform="translate(20, 38)">
      <rect width="195" height="85" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="1"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">Fiber Optic (Glass Strands)</text>
      <text x="12" y="38" font-size="9" fill="#cbd5e1">• Speed: Up to 10+ Gbps</text>
      <text x="12" y="54" font-size="9" fill="#cbd5e1">• Transmission: Light pulses</text>
      <text x="12" y="70" font-size="9" fill="#34d399">✓ Immune to EMI interference</text>
    </g>

    <!-- Ethernet Copper -->
    <g transform="translate(230, 38)">
      <rect width="195" height="85" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#34d399">Ethernet Twisted Pair (UTP)</text>
      <text x="12" y="38" font-size="9" fill="#cbd5e1">• Speed: 100 Mbps - 1 Gbps</text>
      <text x="12" y="54" font-size="9" fill="#cbd5e1">• Transmission: Electrical pulses</text>
      <text x="12" y="70" font-size="9" fill="#fbbf24">✓ Ideal for local LAN lab wiring</text>
    </g>

    <!-- Cellular Wireless -->
    <g transform="translate(440, 38)">
      <rect width="195" height="85" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#fbbf24">Cellular Data (4G / 5G)</text>
      <text x="12" y="38" font-size="9" fill="#cbd5e1">• Speed: 20 Mbps - 300 Mbps</text>
      <text x="12" y="54" font-size="9" fill="#cbd5e1">• Transmission: Radio frequencies</text>
      <text x="12" y="70" font-size="9" fill="#38bdf8">✓ Mobile; broad rural coverage</text>
    </g>

    <!-- Satellite Link -->
    <g transform="translate(650, 38)">
      <rect width="195" height="85" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="1"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#f472b6">Satellite Link (LEO/GEO)</text>
      <text x="12" y="38" font-size="9" fill="#cbd5e1">• Speed: 50 Mbps - 200 Mbps</text>
      <text x="12" y="54" font-size="9" fill="#cbd5e1">• Transmission: Microwaves</text>
      <text x="12" y="70" font-size="9" fill="#f87171">✓ Remote areas; weather-sensitive</text>
    </g>
  </g>
</svg>
""")

SVG_NETWORK_CONFIGURATION_FLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mobile Hotspot Configuration &amp; Client Tethering Workflow</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-step procedure for turning a cellular smartphone into a secure wireless access point for client laptops</text>

  <!-- Left Column: Step-by-Step Configuration Flow -->
  <g transform="translate(45, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#0284c7"/>
    <text x="210" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SMARTPHONE HOTSPOT CONFIGURATION (6 PHASES)</text>

    <!-- Phase 1 -->
    <g transform="translate(15, 45)">
      <rect width="390" height="46" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="24" cy="23" r="12" fill="#0284c7"/>
      <text x="24" y="27" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="45" y="19" font-size="10.5" font-weight="bold" fill="#38bdf8">Enable Cellular Mobile Data</text>
      <text x="45" y="34" font-size="8.5" fill="#cbd5e1">Toggle Mobile Data ON; verify ISP signal (4G/5G) and active data balance.</text>
    </g>

    <!-- Phase 2 -->
    <g transform="translate(15, 98)">
      <rect width="390" height="46" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <circle cx="24" cy="23" r="12" fill="#059669"/>
      <text x="24" y="27" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="45" y="19" font-size="10.5" font-weight="bold" fill="#34d399">Set Unique SSID (Network Name)</text>
      <text x="45" y="34" font-size="8.5" fill="#cbd5e1">Settings ➔ Hotspot &amp; Tethering ➔ Rename SSID (e.g. Grade10_ICT_Hotspot).</text>
    </g>

    <!-- Phase 3 -->
    <g transform="translate(15, 151)">
      <rect width="390" height="46" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <circle cx="24" cy="23" r="12" fill="#d97706"/>
      <text x="24" y="27" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="45" y="19" font-size="10.5" font-weight="bold" fill="#fbbf24">Configure WPA2 / WPA3 Security</text>
      <text x="45" y="34" font-size="8.5" fill="#cbd5e1">Select WPA2-Personal (AES) encryption; NEVER leave hotspot 'Open' or 'None'.</text>
    </g>

    <!-- Phase 4 -->
    <g transform="translate(15, 204)">
      <rect width="390" height="46" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <circle cx="24" cy="23" r="12" fill="#7e22ce"/>
      <text x="24" y="27" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="45" y="19" font-size="10.5" font-weight="bold" fill="#a78bfa">Generate Strong Passphrase</text>
      <text x="45" y="34" font-size="8.5" fill="#cbd5e1">Create 8+ character key mixing uppercase, numbers, and symbols.</text>
    </g>

    <!-- Phase 5 -->
    <g transform="translate(15, 257)">
      <rect width="390" height="46" rx="6" fill="#1e293b" stroke="#f472b6" stroke-width="1"/>
      <circle cx="24" cy="23" r="12" fill="#be185d"/>
      <text x="24" y="27" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
      <text x="45" y="19" font-size="10.5" font-weight="bold" fill="#f472b6">Client Wi-Fi Scan &amp; Association</text>
      <text x="45" y="34" font-size="8.5" fill="#cbd5e1">On Laptop, open Wi-Fi menu, select SSID, enter WPA2 passphrase, click Connect.</text>
    </g>

    <!-- Phase 6 -->
    <g transform="translate(15, 310)">
      <rect width="390" height="60" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="24" cy="28" r="12" fill="#059669"/>
      <text x="24" y="32" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">6</text>
      <text x="45" y="22" font-size="10.5" font-weight="bold" fill="#34d399">DHCP Lease &amp; Connectivity Ping</text>
      <text x="45" y="37" font-size="8.5" fill="#cbd5e1">Phone assigns local IP (192.168.43.x). Laptop opens browser to test live web.</text>
      <text x="45" y="50" font-size="8" fill="#94a3b8">Turn hotspot OFF when finished to prevent background battery and data drain.</text>
    </g>
  </g>

  <!-- Right Column: Troubleshooting & Security Decision Tree -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#334155"/>
    <text x="210" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HOTSPOT TROUBLESHOOTING PROTOCOL</text>

    <!-- Issue 1: SSID Not Found -->
    <g transform="translate(15, 45)">
      <rect width="390" height="70" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#f87171">⚠️ Issue: Laptop cannot find Hotspot SSID in Wi-Fi list</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Cause:</tspan> Hotspot toggle disabled, 'Hide SSID' enabled, or 5GHz band issue.</text>
      <text x="12" y="52" font-size="9" fill="#34d399">• <tspan font-weight="bold" fill="#ffffff">Fix:</tspan> Switch AP Band from 5.0 GHz to 2.4 GHz (for older client compatibility).</text>
    </g>

    <!-- Issue 2: Incorrect Password -->
    <g transform="translate(15, 125)">
      <rect width="390" height="70" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#fbbf24">⚠️ Issue: "Authentication Failed" or "Incorrect Password"</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Cause:</tspan> Case-sensitivity typo or special character mismatch.</text>
      <text x="12" y="52" font-size="9" fill="#34d399">• <tspan font-weight="bold" fill="#ffffff">Fix:</tspan> Click 'Show Password' on phone; delete saved network on laptop &amp; re-enter.</text>
    </g>

    <!-- Issue 3: Connected, No Internet -->
    <g transform="translate(15, 205)">
      <rect width="390" height="70" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#38bdf8">⚠️ Issue: "Connected, No Internet" badge on client laptop</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ffffff">Cause:</tspan> Smartphone cellular data is turned off, or ISP data bundle exhausted.</text>
      <text x="12" y="52" font-size="9" fill="#34d399">• <tspan font-weight="bold" fill="#ffffff">Fix:</tspan> Check phone airtime/data balance (*544# in Kenya); toggle Airplane mode.</text>
    </g>

    <!-- Best Practice Banner -->
    <g transform="translate(15, 285)">
      <rect width="390" height="85" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <text x="12" y="20" font-size="11" font-weight="bold" fill="#34d399">🔒 Hotspot Security Best Practices:</text>
      <text x="12" y="40" font-size="9" fill="#cbd5e1">• Set 'Max Allowed Connections' to limit connected peer devices.</text>
      <text x="12" y="56" font-size="9" fill="#cbd5e1">• Set an automatic 'Turn off Hotspot when idle' timer (5-10 min).</text>
      <text x="12" y="72" font-size="9" fill="#cbd5e1">• Check 'Connected Devices' list on phone to spot unauthorized leeches.</text>
    </g>
  </g>
</svg>
""")

SVG_SEARCH_OPERATORS_CRAAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Advanced Search Refinement &amp; CRAAP Web Evaluation Framework</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Mastering Boolean operators, syntax filters, search engine algorithms, and critical evaluation of online sources</text>

  <!-- Left: Advanced Search Operators & Boolean Logic -->
  <g transform="translate(45, 95)">
    <rect width="425" height="385" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="425" height="32" rx="8" fill="#0284c7"/>
    <text x="212" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SEARCH QUERY REFINEMENT TOOLKIT</text>

    <!-- Exact Phrase -->
    <g transform="translate(15, 42)">
      <rect width="395" height="52" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#38bdf8">Exact Phrase Match: "..."</text>
      <text x="12" y="32" font-size="9" fill="#cbd5e1">Forces results containing exact sequence of words in precise order.</text>
      <text x="12" y="44" font-size="8.5" fill="#34d399">Example: "soil erosion in Kenya"</text>
    </g>

    <!-- Exclusion -->
    <g transform="translate(15, 100)">
      <rect width="395" height="52" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#f87171">Exclusion Operator: -keyword</text>
      <text x="12" y="32" font-size="9" fill="#cbd5e1">Hides all webpages containing the excluded word (no space after minus).</text>
      <text x="12" y="44" font-size="8.5" fill="#34d399">Example: renewable energy -solar</text>
    </g>

    <!-- Domain & Filetype -->
    <g transform="translate(15, 158)">
      <rect width="395" height="52" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#fbbf24">Site &amp; Filetype Filters: site: | filetype:</text>
      <text x="12" y="32" font-size="9" fill="#cbd5e1">Restricts to specific domain level or document format (pdf, docx, pptx).</text>
      <text x="12" y="44" font-size="8.5" fill="#34d399">Example: syllabus site:ac.ke filetype:pdf</text>
    </g>

    <!-- Boolean Operators Box -->
    <g transform="translate(15, 216)">
      <rect width="395" height="150" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="12" y="20" font-size="11" font-weight="bold" fill="#34d399">Boolean Logic Operators (AND / OR / NOT):</text>
      
      <!-- AND -->
      <text x="12" y="42" font-size="9.5" font-weight="bold" fill="#38bdf8">• AND (Intersection):</text>
      <text x="135" y="42" font-size="9" fill="#cbd5e1">Requires BOTH terms to appear on page.</text>
      <text x="135" y="55" font-size="8.5" fill="#94a3b8">Query: maize AND drought (Narrows search scope)</text>

      <!-- OR -->
      <text x="12" y="77" font-size="9.5" font-weight="bold" fill="#fbbf24">• OR (Union):</text>
      <text x="135" y="77" font-size="9" fill="#cbd5e1">Requires EITHER term or both to appear.</text>
      <text x="135" y="90" font-size="8.5" fill="#94a3b8">Query: python OR javascript (Broadens search scope)</text>

      <!-- NOT -->
      <text x="12" y="112" font-size="9.5" font-weight="bold" fill="#f87171">• NOT (Exclusion):</text>
      <text x="135" y="112" font-size="9" fill="#cbd5e1">Excludes pages mentioning second term.</text>
      <text x="135" y="125" font-size="8.5" fill="#94a3b8">Query: jaguar NOT car (Filters animal vs vehicle)</text>
    </g>
  </g>

  <!-- Right: The CRAAP Test for Information Evaluation -->
  <g transform="translate(490, 95)">
    <rect width="425" height="385" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="425" height="32" rx="8" fill="#059669"/>
    <text x="212" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. THE CRAAP WEB CREDIBILITY EVALUATION TEST</text>

    <!-- C - Currency -->
    <g transform="translate(15, 42)">
      <rect width="395" height="58" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <rect x="8" y="8" width="28" height="24" rx="4" fill="#0284c7"/>
      <text x="22" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C</text>
      <text x="45" y="20" font-size="11" font-weight="bold" fill="#38bdf8">Currency (Timeliness of Information)</text>
      <text x="45" y="36" font-size="9" fill="#cbd5e1">When was the page published or updated? Are links active?</text>
      <text x="45" y="48" font-size="8" fill="#94a3b8">Check for recent academic dates rather than decade-old broken blogs.</text>
    </g>

    <!-- R - Relevance -->
    <g transform="translate(15, 106)">
      <rect width="395" height="58" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <rect x="8" y="8" width="28" height="24" rx="4" fill="#059669"/>
      <text x="22" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">R</text>
      <text x="45" y="20" font-size="11" font-weight="bold" fill="#34d399">Relevance (Importance to Research Needs)</text>
      <text x="45" y="36" font-size="9" fill="#cbd5e1">Does the information directly answer your research inquiry?</text>
      <text x="45" y="48" font-size="8" fill="#94a3b8">Ensure the target depth matches Grade 10 academic requirements.</text>
    </g>

    <!-- A - Authority -->
    <g transform="translate(15, 170)">
      <rect width="395" height="58" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <rect x="8" y="8" width="28" height="24" rx="4" fill="#d97706"/>
      <text x="22" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">A</text>
      <text x="45" y="20" font-size="11" font-weight="bold" fill="#fbbf24">Authority (Source of the Information)</text>
      <text x="45" y="36" font-size="9" fill="#cbd5e1">Who is the author/publisher? What are their qualifications?</text>
      <text x="45" y="48" font-size="8" fill="#94a3b8">Prioritize official government (.go.ke) and university (.ac.ke) domains.</text>
    </g>

    <!-- A - Accuracy -->
    <g transform="translate(15, 234)">
      <rect width="395" height="58" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <rect x="8" y="8" width="28" height="24" rx="4" fill="#7e22ce"/>
      <text x="22" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">A</text>
      <text x="45" y="20" font-size="11" font-weight="bold" fill="#a78bfa">Accuracy (Reliability &amp; Truthfulness)</text>
      <text x="45" y="36" font-size="9" fill="#cbd5e1">Is the content supported by empirical evidence and citations?</text>
      <text x="45" y="48" font-size="8" fill="#94a3b8">Cross-reference claims across multiple independent reputable portals.</text>
    </g>

    <!-- P - Purpose -->
    <g transform="translate(15, 298)">
      <rect width="395" height="65" rx="6" fill="#1e293b" stroke="#f472b6" stroke-width="1"/>
      <rect x="8" y="8" width="28" height="24" rx="4" fill="#be185d"/>
      <text x="22" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">P</text>
      <text x="45" y="20" font-size="11" font-weight="bold" fill="#f472b6">Purpose (The Reason Info Exists)</text>
      <text x="45" y="36" font-size="9" fill="#cbd5e1">Is the intent to educate, inform, sell, or persuade?</text>
      <text x="45" y="50" font-size="8" fill="#94a3b8">Distinguish between objective educational data and commercial advertisements or bias.</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# FULL STRUCTURED 5-LESSON DATASET FOR TOPIC 7: INTRODUCTION TO THE INTERNET
# =====================================================================

TOPIC_7_LESSONS = [
    # =========================================================================
    # LESSON 7.1.1: Meaning, History, and Purpose of the Internet
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning, History, and Purpose of the Internet",
        "unit_description": "Foundations of global networking, historical evolution from ARPANET to WWW, Intranet vs Extranet vs Internet access models, URL structure, and societal impact.",
        "lesson_title": "Meaning, History, and Purpose of the Internet",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Global Interconnected Network of Computers",
                    "content": {
                        "title": "The Global Topology of the Internet",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Internet_map_4096.png",
                        "caption": "A high-density visualization of global internet routing paths, showing how decentralized computing nodes and autonomous systems link billions of users across continents.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Stepping onto the Global Digital Highway",
                    "content": {
                        "text": "Think about the last time you streamed an educational tutorial, checked national examination results online, or chatted with a friend across the country. In that single split second, your keystrokes were converted into digital data packets, routed through local fiber optic lines, dispatched across transoceanic undersea cables, and answered by a high-performance web server thousands of kilometers away.\n\nThe **Internet** is the grandest engineering achievement in human history: an open, decentralized public network linking billions of computing devices worldwide. Understanding how this global network operates transforms you from an ordinary user into an empowered digital citizen capable of navigating, analyzing, and building solutions on the web."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define the Internet, World Wide Web (WWW), Intranet, and Extranet from both functional and technical perspectives\n- Differentiate between the physical Internet infrastructure and the hypertext World Wide Web information system\n- Trace the historical evolution of computer networks from ARPANET in 1969 to Sir Tim Berners-Lee's WWW in 1989\n- Deconstruct the structural architecture of a Uniform Resource Locator (URL)\n- Explain how the Internet transforms communication, education, global trade, and governance"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Internet & Networking Terminology",
                    "content": {
                        "term": "The Internet & The World Wide Web",
                        "definition": "The Internet is a global network of interconnected computer networks using the TCP/IP protocol suite; the World Wide Web is an information system of interlinked hypertext documents accessed via the Internet.",
                        "simple": "The Internet is the global highway system of physical cables and routers; the World Wide Web is the collection of houses, libraries, and shops built alongside those highways.",
                        "technical": "The Internet is a packet-switched Wide Area Network (WAN) operating at Layers 3/4 (IP/TCP); the WWW is an Application Layer (Layer 7) distributed hypermedia framework utilizing HTTP/HTTPS and HTML.",
                        "example": "Using your browser to visit https://www.kicd.ac.ke loads a webpage on the WWW across the physical Internet."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Network Boundary Trinity: Intranet, Extranet, and Internet",
                    "content": {
                        "text": "Organizations structure their networks into three distinct security and access tiers based on who needs access:\n\n1. **Intranet (Private & Internal):** A strictly private network restricted to verified members of an organization (such as teachers and students in a school computer lab, or bank employees processing accounts). It is protected by internal firewalls, preventing anyone outside from reading confidential files.\n\n2. **Extranet (Controlled Semi-Private):** An extension of an intranet that grants secure, authenticated access to trusted external stakeholders. For example, a school portal where parents log in securely using personal passwords to view their children's term report cards or pay school fees.\n\n3. **Internet (Public & Global):** The unrestricted, publicly accessible worldwide network open to everyone. Anyone with an ISP connection can view public webpages (such as visiting an open news site or the official KICD curriculum portal)."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Network Boundary Architecture: Intranet vs. Extranet vs. Internet",
                    "content": {
                        "title": "Concentric Network Security Zones and Access Boundaries",
                        "caption": "Vector diagram illustrating the three network access tiers, firewall boundaries, encrypted VPN authentication gateways, and bidirectional packet routing permissions.",
                        "svg_content": SVG_INTERNET_INTRANET_EXTRANET
                    }
                },
                {
                    "type": "step_process",
                    "title": "Historical Evolution: From ARPANET to the World Wide Web",
                    "content": {
                        "intro": "The modern Internet evolved across four major technological milestones:",
                        "steps": [
                            {"title": "1. 1969: The Birth of ARPANET", "description": "The US Department of Defense funded ARPANET, creating a decentralized packet-switching network capable of rerouting data if individual military nodes were destroyed."},
                            {"title": "2. 1974-1983: TCP/IP Protocol Standardization", "description": "Vint Cerf and Bob Kahn developed Transmission Control Protocol / Internet Protocol (TCP/IP), creating a universal standard for diverse computer networks to communicate seamlessly."},
                            {"title": "3. 1989: Invention of the World Wide Web", "description": "British scientist Sir Tim Berners-Lee invented HTML, HTTP, and URLs at CERN, transforming the text-based academic network into an intuitive graphical web for everyone."},
                            {"title": "4. Modern Era: Global Commercial & Mobile Expansion", "description": "Undersea fiber optic backbones, mobile cellular data (3G/4G/5G), and cloud computing expanded web access to billions of smartphones worldwide."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: The School Multi-Tier Network System",
                    "content": {
                        "title": "How a Modern Secondary School Deploys Intranet, Extranet, and Internet",
                        "scenario": "A Kenyan secondary school in Machakos County operates a digital campus management system to handle student records, examinations, and communication.",
                        "impact": "If all systems were completely open to the public web, student grades and financial records would be vulnerable to tampering and cyber theft.",
                        "solution": "The school places the teachers' grading database on an internal Intranet, gives parents authenticated Extranet logins to pay school fees and inspect attendance, and hosts the public school website on the open Internet for public admissions information."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: 'The Internet' and 'The Web' are the exact same thing",
                    "content": {
                        "misconception": "When people open a browser, they often say they are 'opening the Internet', believing the Internet and the World Wide Web are identical.",
                        "correction": "The Internet is the vast physical infrastructure of cables, routers, servers, and satellites. The World Wide Web (WWW) is just one of many services running on top of the Internet, alongside email (SMTP/IMAP), file transfers (FTP), VoIP phone calls, and online gaming."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Deconstructing Complex URLs",
                    "content": {
                        "mistake": "Mistaking the directory path or file extension for the main domain name, leading to confusion during web navigation or falling for phishing scams.",
                        "why_it_happens": "Users often look at the entire address bar without identifying the core domain and security protocol.",
                        "fix_solution": "Always inspect the protocol ('https://' indicates encrypted communication), identify the domain ('kicd.ac.ke'), and recognize that everything following the slash ('/curriculum/syllabus.html') is simply a folder directory and filename on the web server."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Network Boundary Models",
                    "content": {
                        "question": "A hospital provides an online portal where registered patients can log in securely from home to check their lab results, while medical staff access patient health records internally. Which networking models describe the patient portal and the internal staff database respectively?",
                        "options": [
                            "Internet and Extranet",
                            "Extranet and Intranet",
                            "Intranet and Internet",
                            "Extranet and Public Cloud"
                        ],
                        "correct": "B",
                        "explanation": "A secure portal that allows authorized external users (patients) authenticated access is an Extranet, while the internal database restricted to hospital employees is an Intranet."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Historical Inventions",
                    "content": {
                        "question": "Who is credited with inventing the World Wide Web (WWW), HTML markup, and the HTTP protocol in 1989 at CERN?",
                        "options": [
                            "Alan Turing",
                            "Bill Gates",
                            "Sir Tim Berners-Lee",
                            "Vint Cerf"
                        ],
                        "correct": "C",
                        "explanation": "Sir Tim Berners-Lee invented the World Wide Web at CERN in 1989, designing HTML, HTTP, URLs, and the first web client and server."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: What is the Internet and How Does it Work?",
                    "content": {
                        "title": "Introduction to the Internet & World Wide Web Architecture",
                        "youtube_id": "Dxcc6ycZ73M",
                        "url": "https://www.youtube.com/watch?v=Dxcc6ycZ73M",
                        "description": "Engaging animated overview explaining packet switching, TCP/IP protocol routing, DNS resolution, and the global infrastructure of the internet."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **The Internet Defined:** A global, decentralized network of interconnected computer networks operating on TCP/IP.\n2. **Internet vs. WWW:** The Internet is the physical hardware highway; the World Wide Web is the hypertext information system accessed through web browsers.\n3. **Network Boundary Tiers:** Intranets are private and internal; Extranets grant controlled external partner access; the Internet is open to the global public.\n4. **URL Structure:** A standardized address comprising a protocol (https), subdomain (www), domain name, TLD/ccTLD (.ac.ke), directory path, and filename."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7.1.2: Common Services Offered Through the Internet
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Common Services Offered Through the Internet",
        "unit_description": "Exploration and analysis of modern web services: E-Commerce, Fintech/Mobile Money (M-Pesa), E-Learning (LMS), E-Governance (eCitizen/iTax), and cloud communications.",
        "lesson_title": "Common Services Offered Through the Internet",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Digital Financial Services & Mobile Money in Kenya",
                    "content": {
                        "title": "Mobile Money Transformation in East Africa",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/M-PESA_mobile_money_and_Equity_agent%2C_Nairobi%2C_Kenya.jpg",
                        "caption": "An authorized mobile financial agent in Nairobi providing instant digital financial services, demonstrating how internet and mobile networks power modern commerce.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Modern Ecosystem of Online Services",
                    "content": {
                        "text": "The Internet is far more than an electronic library of static text documents. Today, it functions as a vibrant global engine powering essential public and commercial services that touch every aspect of daily life.\n\nFrom purchasing groceries on an e-commerce platform and transferring funds via mobile banking, to taking online courses on a Learning Management System (LMS) and applying for a national passport on eCitizen, online services have eliminated geographical barriers, reduced operational costs, and transformed traditional society into an interconnected digital economy."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Categorize major internet services into E-Commerce, Fintech, E-Learning, E-Governance, and Cloud Communications\n- Analyze the socioeconomic benefits of mobile money (such as M-Pesa) and digital banking\n- Explain how Learning Management Systems (LMS) enable flexible, self-paced remote education\n- Evaluate how E-Governance platforms (eCitizen, KRA iTax) streamline citizen public services and eliminate bureaucratic corruption\n- Discuss security considerations when transacting across online commercial and governmental services"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Internet Services Terminology",
                    "content": {
                        "term": "E-Commerce & E-Governance",
                        "definition": "E-Commerce is the digital buying and selling of goods, services, and funds over the internet; E-Governance is the use of digital networks by government agencies to deliver public services to citizens.",
                        "simple": "E-Commerce is an online supermarket where you buy products; E-Governance is an online government office where you apply for official permits and certificates.",
                        "technical": "E-Commerce involves secure digital shopping carts, payment gateway integration (SSL/TLS, API webhooks), and electronic data interchange (EDI); E-Governance utilizes authenticated citizen identity portals and database transaction processing.",
                        "example": "Ordering school books on Jumia (E-Commerce) or renewing a driving license on eCitizen (E-Governance)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Main Pillars of Internet Services",
                    "content": {
                        "text": "Modern internet services fall into four primary categories:\n\n1. **Electronic Commerce (E-Commerce):** Digital storefronts where customers browse products, place orders in virtual carts, pay electronically, and arrange physical delivery or instant software downloads (e.g. Jumia, Amazon).\n\n2. **Digital Financial Services (Fintech & Mobile Banking):** Platforms enabling instant fund transfers, bill payments, digital savings, and currency conversions across mobile wallets and bank accounts (e.g. M-Pesa, online banking apps).\n\n3. **Electronic Learning (E-Learning & Virtual Classrooms):** Web-based Learning Management Systems (LMS) like Google Classroom and Moodle that allow teachers to post lecture notes, conduct video classes, receive homework assignments, and grade quizzes automatically.\n\n4. **Electronic Governance (E-Governance):** Digital public administration portals that allow citizens to register businesses, submit tax returns, apply for national IDs, and pay utility bills without visiting physical government offices (e.g. eCitizen, KRA iTax)."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Web Service Architecture & URL Deconstruction",
                    "content": {
                        "title": "Dissecting Web Service URLs, DNS Resolution, and HTTP Client-Server Requests",
                        "caption": "High-precision vector graphic deconstructing the ten elements of a secure URL and illustrating the Domain Name System (DNS) translation and HTTP request-response pipeline.",
                        "svg_content": SVG_URL_DECONSTRUCTION_ARCHITECTURE
                    }
                },
                {
                    "type": "step_process",
                    "title": "The Client-Server Request Pipeline for Internet Services",
                    "content": {
                        "intro": "Whenever you interact with an online service (such as loading your student dashboard), five sequential steps occur:",
                        "steps": [
                            {"title": "1. User Query / Action", "description": "You enter a URL or click a button in your web browser (the client application)."},
                            {"title": "2. DNS IP Translation", "description": "The Domain Name System looks up the human-readable domain name (e.g. ecitizen.go.ke) and resolves it to the server's numerical IP address."},
                            {"title": "3. Encrypted HTTPS Handshake", "description": "The client browser and web server establish an encrypted TLS/SSL session on port 443 to secure data against interception."},
                            {"title": "4. Server Database Processing", "description": "The application server receives your request (HTTP GET or POST), queries the central database, and prepares the requested information."},
                            {"title": "5. Response Rendering", "description": "The server returns an HTTP 200 OK response with structured HTML, CSS, and data, which your browser renders into an interactive screen."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Transforming Agriculture with Mobile Services",
                    "content": {
                        "title": "Empowering Rural Kenyan Farmers via Digital Marketplaces",
                        "scenario": "In rural Meru County, a cooperative of avocado and potato farmers previously relied on travelling middlemen who offered low prices for their crops.",
                        "impact": "Farmers lacked price transparency and frequently lost money on perishable produce due to delayed transport and unfair bargaining.",
                        "solution": "By connecting to digital agricultural platforms on their smartphones, farmers now monitor live wholesale commodity prices at Nairobi markets, negotiate directly with bulk buyers, and receive payments securely via mobile money upon delivery."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: All websites with a padlock icon are 100% trustworthy and safe",
                    "content": {
                        "misconception": "Many users believe that if a website URL starts with 'https://' and has a green padlock icon, the company behind it is completely honest and cannot be a scam.",
                        "correction": "The HTTPS padlock only means that the connection between your browser and that server is encrypted so third parties cannot intercept data in transit. It does NOT guarantee that the owner of the website is reputable. Anyone—including cyber criminals hosting fake phishing sites—can obtain a free SSL certificate."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Avoiding Digital Financial Traps",
                    "content": {
                        "mistake": "Sharing one-time PINs (OTPs) or clicking unsolicited SMS links claiming to be from mobile money customer care.",
                        "why_it_happens": "Social engineering and phishing attacks manipulate urgency, tricking users into revealing their financial authentication secrets.",
                        "fix_solution": "Never share your mobile money PIN or OTP with anyone. Always verify the official sender ID and access services only through verified apps or official government portals."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Categorizing Online Services",
                    "content": {
                        "question": "A citizen logs onto a national portal to file annual tax returns, renew their driving license, and apply for a business permit. Which category of internet service is being utilized?",
                        "options": [
                            "Electronic Commerce (E-Commerce)",
                            "Electronic Governance (E-Governance)",
                            "Digital Entertainment Streaming",
                            "Social Media Networking"
                        ],
                        "correct": "B",
                        "explanation": "E-Governance refers to the delivery of government public services and official administrative processes to citizens through digital web platforms."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Learning Management Systems",
                    "content": {
                        "question": "Which of the following software platforms is specifically designed as a Learning Management System (LMS) for delivering e-learning courses and tracking student grades?",
                        "options": [
                            "Moodle",
                            "Jumia",
                            "Apache HTTP Server",
                            "Faiba Router Portal"
                        ],
                        "correct": "A",
                        "explanation": "Moodle (along with Google Classroom and Canvas) is an LMS designed specifically for managing educational courses, assignments, quizzes, and student progress."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: How Web Services and Internet Applications Work",
                    "content": {
                        "title": "Modern Internet Services, APIs, and E-Commerce Ecosystems",
                        "youtube_id": "aO858HyFbKI",
                        "url": "https://www.youtube.com/watch?v=aO858HyFbKI",
                        "description": "Comprehensive visual breakdown of how web services, cloud infrastructure, and client-server architectures interact to deliver digital applications."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Service Categories:** Internet services include E-Commerce (retail), Fintech (mobile money/banking), E-Learning (LMS), and E-Governance (public administration).\n2. **Socioeconomic Impact:** Services like M-Pesa and agricultural portals empower communities by providing financial inclusion and market transparency.\n3. **Client-Server Transaction:** Web requests travel from client browsers via DNS resolution and encrypted HTTPS to server databases, returning processed data.\n4. **Security Awareness:** HTTPS encrypts transmission channels, but users must stay vigilant against phishing links and never share personal security PINs."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7.1.3: Fundamental Components of an Internet Connection
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Fundamental Components of an Internet Connection",
        "unit_description": "Hardware and communication infrastructure required for internet connectivity: NIC, routers, modems, ISP gateways, transmission media (fiber optic, Ethernet, cellular, satellite), and protocol stacks.",
        "lesson_title": "Fundamental Components of an Internet Connection",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Optical Fiber Infrastructure: The Speed of Light Backbone",
                    "content": {
                        "title": "Illuminated Optical Fiber Strands",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Fibreoptic.jpg",
                        "caption": "Bundles of ultra-thin glass fiber optic strands transmitting data as pulses of light at immense speeds across continental and undersea distances.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Physical Machinery Powering the Digital World",
                    "content": {
                        "text": "When you tap 'Connect' on a smartphone or plug an Ethernet cable into a desktop computer, what physical devices make that connection possible? An internet link does not exist out of thin air—it relies on a synchronized chain of specialized hardware components and physical transmission media working in perfect harmony.\n\nFrom Network Interface Cards inside your laptop and intelligent local routers directing traffic, to modems translating analog waves into digital bits and high-speed fiber optic cables carrying light pulses across ocean floors, every component plays a distinct role in keeping our world connected."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the core hardware devices required for an internet connection: NIC, Router, Modem/ONT, and Switch\n- Differentiate between the distinct functions of a Router (traffic director) and a Modem (signal translator)\n- Compare guided (wired) transmission media (Fiber Optic, UTP Ethernet) with unguided (wireless) media (Cellular 4G/5G, Wi-Fi, Satellite)\n- Explain the critical role of Internet Service Providers (ISPs) and Internet Exchange Points (IXPs) in routing global data\n- Diagnose and isolate basic hardware connection faults in a local school or home network"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Connection Hardware Terminology",
                    "content": {
                        "term": "Router vs. Modem (Modulator-Demodulator)",
                        "definition": "A modem converts analog signals from telecommunications lines into digital signals for computers (and vice versa); a router directs digital data packets between different networks and devices.",
                        "simple": "The modem is the digital translator that connects your home to the ISP line; the router is the traffic police officer that directs web traffic to your laptop, phone, or TV.",
                        "technical": "A modem operates at Physical/Data Link Layers (Layer 1/2) performing digital-analog modulation; a router operates at the Network Layer (Layer 3) inspecting IP headers, performing NAT, and routing packets.",
                        "example": "A fiber ONT modem converts light pulses into electrical Ethernet signals, while the Wi-Fi router assigns local IP addresses (192.168.1.x) to lab computers."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Five Essential Links in the Connection Chain",
                    "content": {
                        "text": "Every complete internet connection requires five fundamental hardware and service links:\n\n1. **Network Interface Card (NIC):** The internal circuit board or wireless chip in your device that allows it to communicate with a network. Every NIC has a permanent hardware address called a **MAC (Media Access Control) address**.\n\n2. **Wireless Router / Switch:** Establishes the Local Area Network (LAN). It assigns local IP addresses to devices using DHCP and ensures data packets sent from one device reach the correct recipient.\n\n3. **Modem or Optical Network Terminal (ONT):** The interface device that connects your local router to the external telecom line, translating incoming frequencies or light pulses into standard computer bits.\n\n4. **Transmission Medium:** The physical channel over which data travels, including **Fiber Optic Cables** (fastest, uses light pulses, immune to interference), **Ethernet UTP Cables** (reliable copper wiring for labs), **Cellular Radio** (3G/4G/5G mobile signals), and **Satellite** (radio waves beamed from space for remote regions).\n\n5. **Internet Service Provider (ISP):** The telecommunications company (e.g. Safaricom, Faiba, Airtel, Telkom) that maintains network routing exchanges and grants you access to the global internet backbone."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "End-to-End Internet Connection Architecture",
                    "content": {
                        "title": "The Complete Physical and Logical Internet Connection Chain",
                        "caption": "Detailed vector architecture illustrating packet flow from client NIC devices through local routers, modems, ISP nodes, and undersea fiber backbones.",
                        "svg_content": SVG_INTERNET_CONNECTION_CHAIN
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Packet Journey from Client to Web Server",
                    "content": {
                        "intro": "When you click a link in your web browser, your data packet traverses five infrastructure stages:",
                        "steps": [
                            {"title": "1. Device Packet Encapsulation", "description": "The browser creates an HTTP request. The operating system attaches TCP transport headers and the destination IP address, passing it to the wireless NIC."},
                            {"title": "2. Local Router Routing & NAT", "description": "The router receives the packet via Wi-Fi radio waves, replaces the private local IP with your public ISP IP via Network Address Translation (NAT), and forwards it to the modem."},
                            {"title": "3. Modem Light/Analog Modulation", "description": "The modem or ONT converts the electrical digital bitstream into laser light pulses and transmits it onto the fiber optic distribution line."},
                            {"title": "4. ISP & Internet Exchange Routing", "description": "The local ISP receives the light pulses at its Point of Presence (PoP) and routes them through the Kenya Internet Exchange Point (KIXP) onto national and undersea backbones (such as TEAMS and SEACOM)."},
                            {"title": "5. Destination Server Fulfillment", "description": "The destination server receives the packet, decapsulates the request, processes the query, and transmits the response back along the reverse pathway in milliseconds."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Undersea Fiber Cables Powering East Africa",
                    "content": {
                        "title": "How Undersea Fiber Cables Revolutionized Kenyan Internet Connectivity",
                        "scenario": "Prior to 2009, internet access in Kenya relied entirely on expensive, slow geostationary satellite links with high latency (lag) and limited bandwidth.",
                        "impact": "Webpages took seconds to load, video streaming was impossible, and international voice calls were prohibitively expensive.",
                        "solution": "The landing of submarine fiber optic cables in Mombasa (such as TEAMS, SEACOM, and EASSy) connected Kenya directly to global internet hubs via ultra-fast light conduits, dropping broadband costs by over 90% and sparking a digital innovation boom."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: 'Wi-Fi' is the exact same thing as 'The Internet'",
                    "content": {
                        "misconception": "Many people say 'the Wi-Fi is down' whenever a website fails to load, believing Wi-Fi and the Internet are the same entity.",
                        "correction": "Wi-Fi is simply a local wireless radio technology connecting your phone to your router within a 10-30 meter range. You can have a perfect 100% full-bar Wi-Fi signal to your router even if the router's external fiber cable is unplugged and has zero internet access."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: Diagnosing Lab Connection Outages",
                    "content": {
                        "mistake": "Restarting the client computer repeatedly when an entire computer lab loses internet connectivity simultaneously.",
                        "why_it_happens": "Failing to systematically isolate whether the problem is on the client device, local switch, router, modem, or the external ISP line.",
                        "fix_solution": "Follow the connection chain backwards: If one PC fails, check its cable/Wi-Fi. If all PCs can print locally but cannot browse, the router is fine, but the modem or ISP connection has dropped."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Hardware Roles in a Lab",
                    "content": {
                        "question": "In a school computer lab, students can share files and send print jobs to each other, but no computer can load external websites. Which component in the connection chain is most likely experiencing a failure?",
                        "options": [
                            "The network interface card (NIC) on every individual computer",
                            "The local network switch connecting the computers",
                            "The modem or the external ISP line connection",
                            "The operating system software on the client workstations"
                        ],
                        "correct": "C",
                        "explanation": "Because local communication (file sharing and printing) works perfectly, the internal LAN hardware (NICs and switch) is functioning. The failure is at the gateway connecting the local network to the outside world—the modem or ISP link."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Transmission Media Properties",
                    "content": {
                        "question": "Which transmission medium uses thin strands of glass to carry data as pulses of laser light, offering the highest bandwidth and complete immunity to electromagnetic interference?",
                        "options": [
                            "Unshielded Twisted Pair (UTP) copper cable",
                            "Fiber optic cable",
                            "Coaxial television cable",
                            "Cellular radio waves"
                        ],
                        "correct": "B",
                        "explanation": "Fiber optic cables transmit data as light pulses through glass or plastic cores, providing massive bandwidth, ultra-low latency, and complete immunity to electrical noise."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: Routers, Modems, and How Internet Infrastructure Works",
                    "content": {
                        "title": "Understanding Network Hardware: Routers vs. Switches vs. Modems",
                        "youtube_id": "1z0ULvg_pW8",
                        "url": "https://www.youtube.com/watch?v=1z0ULvg_pW8",
                        "description": "Clear, practical hardware tutorial explaining how modems, routers, switches, and network adapters work together to establish internet access."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Essential Hardware Chain:** Connection requires a Client Device (NIC) ➔ Local Switch/Router ➔ Modem/ONT ➔ ISP Gateway ➔ Global Backbone.\n2. **Router vs. Modem:** Modems translate analog/optical signals into digital data; routers manage local traffic and assign IP addresses.\n3. **Transmission Media:** Fiber optic cables carry light pulses at high speeds; Ethernet cables wire local labs; cellular and satellite provide wireless reach.\n4. **Systematic Troubleshooting:** Isolate faults by testing whether communication fails locally on the LAN or externally at the ISP gateway."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7.1.4: Establishing and Managing an Internet Connection
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Establishing and Managing an Internet Connection",
        "unit_description": "Practical procedures for configuring and securing wireless connections, mobile hotspots, Wi-Fi tethering, WPA2/WPA3 authentication, bandwidth management, and troubleshooting network dropouts.",
        "lesson_title": "Establishing and Managing an Internet Connection",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Configuring Wireless Routers and Mobile Devices",
                    "content": {
                        "title": "Wireless 4G Router and Smartphone Mobile Tethering",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/00/Ruter_Wi-Fi_Tenda_4G06_cu_conectare_prin_4G_%C8%99i_un_smartphone.jpg",
                        "caption": "A portable 4G wireless gateway connected alongside a smartphone, showing how mobile cellular connections are distributed wirelessly to local client workstations.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Connecting Anywhere: The Power of Wireless Tethering",
                    "content": {
                        "text": "Imagine you are working on an important school science project on your laptop, and the main school wired network suddenly drops due to maintenance. You have an active cellular data bundle on your smartphone, but how do you share that connection with your laptop and your group members' tablets?\n\nConfiguring a **Mobile Hotspot** is an essential practical digital skill. It turns your mobile device into a portable wireless access point, allowing multiple client computers to browse, research, and collaborate securely from anywhere."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Follow a step-by-step procedure to configure a secure Wi-Fi Mobile Hotspot on a smartphone\n- Connect a client laptop to a wireless hotspot and verify active data connectivity\n- Implement robust wireless security protocols (WPA2/WPA3-Personal) with strong cryptographic passphrases\n- Explain the dangers of open, unsecured public Wi-Fi networks\n- Apply troubleshooting protocols to resolve common connection errors (SSID not found, incorrect password, connected without internet access)\n- Manage data bundles and battery consumption effectively while tethering"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Wireless & Hotspot Terminology",
                    "content": {
                        "term": "SSID & WPA2/WPA3 Encryption",
                        "definition": "SSID (Service Set Identifier) is the human-readable broadcast name of a wireless network; WPA2/WPA3 is the security protocol that encrypts wireless radio transmissions to prevent eavesdropping.",
                        "simple": "SSID is the name tag of your Wi-Fi network; WPA2/WPA3 is the security lock that requires a password before letting anyone connect.",
                        "technical": "SSID is a 32-octet identifier included in 802.11 beacon frames; WPA2-Personal uses the Advanced Encryption Standard (AES) with CCMP and 4-way handshakes to derive session encryption keys.",
                        "example": "Setting your hotspot name as 'Grade10_ICT_Lab' (SSID) and securing it with WPA2-Personal password 'Keny@_2026_Sci!'."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Principles of Secure Wireless Tethering",
                    "content": {
                        "text": "When you activate a mobile hotspot, your smartphone performs three simultaneous networking roles:\n\n1. **Cellular Modem:** It maintains a 4G/5G data link with your telecom service provider's cell tower.\n\n2. **Wireless Access Point (AP):** It broadcasts an 802.11 Wi-Fi radio beacon on the 2.4 GHz or 5.0 GHz frequency band, allowing nearby devices to locate it.\n\n3. **Local DHCP & NAT Gateway:** It automatically assigns private IP addresses (such as `192.168.43.x`) to connected client laptops and routes their requests over its cellular data link.\n\n**Security Warning:** Never set hotspot security to 'Open' or 'None'. An open network allows strangers within radio range to connect silently, drain your expensive cellular data bundle, and potentially intercept unencrypted traffic."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Mobile Hotspot Configuration & Client Tethering Workflow",
                    "content": {
                        "title": "Step-by-Step Smartphone Hotspot Setup and Client Connection Flow",
                        "caption": "High-precision vector workflow showing mobile data activation, SSID naming, WPA2 encryption, client scanning, authentication, and troubleshooting decision paths.",
                        "svg_content": SVG_NETWORK_CONFIGURATION_FLOW
                    }
                },
                {
                    "type": "step_process",
                    "title": "Standard Operating Procedure: Setting Up and Connecting to a Hotspot",
                    "content": {
                        "intro": "Follow this standardized procedure to establish and join a secure mobile connection:",
                        "steps": [
                            {"title": "Phase 1: Activate Mobile Data", "description": "On your smartphone, swipe down to quick settings and enable 'Mobile Data'. Verify you have active airtime/data balance."},
                            {"title": "Phase 2: Open Hotspot Settings", "description": "Go to Settings ➔ Network & Internet ➔ Hotspot & Tethering ➔ Wi-Fi Hotspot."},
                            {"title": "Phase 3: Set SSID & Security", "description": "Enter a clear network name (e.g. 'Grade10_ICT_Hotspot'). Under Security, select 'WPA2-Personal' or 'WPA3-Personal'."},
                            {"title": "Phase 4: Set Strong Passphrase", "description": "Type an 8+ character password combining uppercase letters, numbers, and symbols (e.g. 'Sci_Lab#2026'). Toggle Hotspot to 'ON'."},
                            {"title": "Phase 5: Client Connection", "description": "On your laptop, click the Wi-Fi icon in the system tray, select the SSID from the list, click 'Connect', and enter the exact passphrase."},
                            {"title": "Phase 6: Verification & Cleanup", "description": "Open a browser and load an educational page. When finished researching, toggle the Hotspot OFF to conserve battery and data."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Field Research in the School Agro-Plot",
                    "content": {
                        "title": "Deploying Mobile Hotspots for Grade 10 Agricultural Fieldwork",
                        "scenario": "A Grade 10 agriculture class is collecting soil moisture and pH data in the school farm, 500 meters away from the main school building's Wi-Fi routers.",
                        "impact": "Students need to upload sensor readings and compare crop disease photos with online agricultural databases in real time.",
                        "solution": "The team leader configures a secure mobile hotspot on a smartphone, connects three student laptops, completes the online data logging, and turns off the hotspot immediately upon returning to the classroom."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Leaving a mobile hotspot running with no connected users does not consume battery or data",
                    "content": {
                        "misconception": "Many users leave their portable hotspot toggled ON all day in their pocket, thinking it only consumes power when someone is actively downloading files.",
                        "correction": "A running hotspot continuously powers the Wi-Fi transmitter to broadcast beacon frames 10 times every second. This significantly increases battery drain and device heat. Furthermore, background operating system updates on tethered laptops can silently consume gigabytes of data in minutes if 'Metered Connection' is not turned on."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The 'Connected, No Internet' Error",
                    "content": {
                        "mistake": "Repeatedly disconnecting and reconnecting Wi-Fi when the laptop says 'Connected, secured — No Internet access'.",
                        "why_it_happens": "The Wi-Fi radio link between laptop and phone is working, but the smartphone has run out of cellular data, mobile data is switched off, or the telecom APN is misconfigured.",
                        "fix_solution": "Check the smartphone directly: verify that cellular mobile data is enabled, check your balance with the ISP, or toggle Airplane mode on the phone to re-register with the cell tower."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Wireless Security Configurations",
                    "content": {
                        "question": "When configuring a mobile hotspot to share your cellular internet connection with classmates during a school project, which security setting is the most secure and appropriate?",
                        "options": [
                            "Security set to 'None / Open' so anyone can connect quickly without typing",
                            "Security set to 'WPA2-Personal' with a strong alphanumeric password",
                            "Security set to 'WEP' with the default phone name",
                            "Security set to 'Hidden SSID' with zero password protection"
                        ],
                        "correct": "B",
                        "explanation": "WPA2-Personal (or WPA3-Personal) with a strong, complex passphrase encrypts wireless radio signals with AES encryption, preventing unauthorized devices from intercepting traffic or draining your data."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Network Band Compatibility",
                    "content": {
                        "question": "A student configures a mobile hotspot on a modern smartphone set to 5.0 GHz broadcast, but an older school laptop cannot find the SSID in its Wi-Fi list. What is the most effective fix?",
                        "options": [
                            "Reinstall the operating system on the laptop",
                            "Switch the hotspot AP Band setting from 5.0 GHz to 2.4 GHz on the phone",
                            "Turn off the cellular data on the smartphone",
                            "Change the hotspot password to numbers only"
                        ],
                        "correct": "B",
                        "explanation": "Older laptops often possess legacy Wi-Fi network cards that only support the 2.4 GHz radio frequency band. Switching the phone's AP Band setting to 2.4 GHz ensures backward compatibility."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: How to Configure and Secure a Mobile Wi-Fi Hotspot",
                    "content": {
                        "title": "Smartphone Tethering, Wi-Fi Security, and Data Management",
                        "youtube_id": "qJpX3Q1iH5w",
                        "url": "https://www.youtube.com/watch?v=qJpX3Q1iH5w",
                        "description": "Step-by-step practical tutorial demonstrating hotspot configuration, WPA2/WPA3 password setup, metered connection settings, and tethering security."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Mobile Hotspot Role:** Transforms a smartphone into a portable wireless router distributing cellular data to client laptops and tablets.\n2. **Configuration Steps:** Enable Mobile Data ➔ Set unique SSID ➔ Choose WPA2/WPA3 Security ➔ Configure strong 8+ character password ➔ Connect client.\n3. **Security Imperative:** Never use open networks without encryption; protect your bandwidth and prevent packet snooping.\n4. **Resource Management:** Mark connections as 'Metered' on laptops to block heavy background updates, and turn hotspots OFF when finished."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7.1.5: Using Search Engines and Basic Web Navigation
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Using Search Engines and Basic Web Navigation",
        "unit_description": "Search engine mechanics (crawling, indexing, ranking algorithms), query formulation, exact match syntax, exclusion filters, domain/filetype restrictions, Boolean logic (AND/OR/NOT), and the CRAAP test for web source evaluation.",
        "lesson_title": "Using Search Engines and Basic Web Navigation",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Search Engine Results Page and Web Information Retrieval",
                    "content": {
                        "title": "Web Search Engine Results Page (SERP) Interface",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Search_Engine_Results_Page_%28SERP%29_Graphic_Illustration.png",
                        "caption": "A structured representation of modern search engine results, showing how search queries retrieve ranked organic results, knowledge panels, and verified academic links.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Navigating the Ocean of Digital Information",
                    "content": {
                        "text": "The World Wide Web contains over 50 billion indexed webpages. If you type a basic query like 'Kenya agriculture' into a search engine, you will receive hundreds of millions of results in less than half a second—ranging from tourist blogs and hotel advertisements to peer-reviewed scientific research.\n\nHow do search engines index billions of pages in advance? And more importantly, how can you refine your queries using advanced mathematical operators, Boolean logic, and domain filters so you find authoritative, trustworthy information without wasting hours sifting through commercial clutter?"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the 3-stage mechanics of search engines: Crawling (Spiders), Indexing (Databases), and Ranking (Algorithms)\n- Formulate refined search queries using exact phrase matching, exclusion operators, site filters, and filetype filters\n- Apply Boolean logic operators (AND, OR, NOT) to narrow or broaden web search results\n- Evaluate web source credibility, accuracy, and bias using the CRAAP Test framework\n- Differentiate between organic educational results, sponsored commercial ads, and clickbait"
                    }
                }
            ],
            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Core Search Engine Terminology",
                    "content": {
                        "term": "Web Crawler (Spider) & Search Index",
                        "definition": "A web crawler is an automated bot that systematically discovers and downloads webpages by following hyperlinks; a search index is a massive organized database of analyzed terms used to retrieve results instantly.",
                        "simple": "The web crawler is an automated digital librarian reading every book in the world; the search index is the comprehensive index at the back of the library catalog.",
                        "technical": "A crawler utilizes recursive graph-traversal algorithms to parse HTML links and submit document tokens to an inverted index database for multi-factor algorithmic ranking (e.g. PageRank, TF-IDF).",
                        "example": "Googlebot crawls university websites, indexing lecture PDFs so students can find them in milliseconds."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "How Search Engines Work: The Three Fundamental Phases",
                    "content": {
                        "text": "When you execute a web search, you are not scanning the live web in real time. Instead, you are searching a precompiled index database built through three continuous stages:\n\n1. **Crawling (Discovery):** Automated software programs (called spiders or bots, like Googlebot) traverse the web 24/7. They start with a known list of URLs, follow every hyperlink found on those pages, and download new and updated content.\n\n2. **Indexing (Categorization):** The downloaded pages are parsed and stored in massive data centers. The search engine extracts keywords, titles, headings, and images, building a structured **inverted index** (much like a giant digital encyclopedia index).\n\n3. **Ranking & Retrieval (Scoring):** When you type a query, proprietary ranking algorithms evaluate thousands of matching indexed pages within milliseconds. Pages are ranked based on keyword relevance, domain authority (e.g. `.ac.ke` vs unverified blogs), page load speed, and user location, presenting the most authoritative results on Page 1."
                    }
                }
            ],
            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Advanced Search Refinement & CRAAP Evaluation Framework",
                    "content": {
                        "title": "Advanced Query Operators, Boolean Logic, and the CRAAP Web Credibility Test",
                        "caption": "High-precision vector guide detailing syntax operators (exact match, exclusion, site, filetype), Boolean Venn logic, and the 5-point CRAAP test for evaluating web authority.",
                        "svg_content": SVG_SEARCH_OPERATORS_CRAAP
                    }
                },
                {
                    "type": "step_process",
                    "title": "The Advanced Search Refinement Toolkit",
                    "content": {
                        "intro": "Use these specialized search operators to filter out irrelevant results and target precise documents:",
                        "steps": [
                            {"title": "1. Exact Phrase Matching (\" \")", "description": "Enclosing keywords in quotation marks forces the engine to return only pages containing those exact words in that exact order (e.g. \"soil conservation methods\")."},
                            {"title": "2. Exclusion Operator (-)", "description": "Placing a minus sign immediately before a word excludes pages mentioning that topic (e.g. renewable energy -wind finds solar and geothermal while removing wind)."},
                            {"title": "3. Domain Filter (site:)", "description": "Restricts search results to a specific website or top-level domain (e.g. \"computer curriculum\" site:go.ke exclusively searches Kenyan government portals)."},
                            {"title": "4. Filetype Filter (filetype:)", "description": "Restricts results to specific document formats such as PDF, DOCX, or PPTX (e.g. \"climate policy\" site:ac.ke filetype:pdf returns downloadable academic research papers)."},
                            {"title": "5. Boolean Logic (AND, OR, NOT)", "description": "Use AND to require both terms, OR to find either term, and NOT to exclude terms (e.g. maize AND drought OR irrigation)."}
                        ]
                    }
                }
            ],
            # Page 4: Real-World Applications, Worked Examples & Misconceptions
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Application: Academic Research on Crop Management",
                    "content": {
                        "title": "Conducting Rigorous Secondary School Science Research",
                        "scenario": "A Grade 10 student is writing a science paper on organic pest control for Kenyan vegetable farmers, but standard searches return thousands of chemical pesticide advertisements.",
                        "impact": "Unrefined searches waste hours of study time and risk including commercial marketing claims in an academic paper.",
                        "solution": "The student formulates a refined query: '\"organic pest control\" Kenya site:ac.ke -chemical filetype:pdf'. This query immediately returns official, peer-reviewed PDF research papers from Kenyan agricultural universities without commercial ads."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The top result on a search page is always the most accurate and factual",
                    "content": {
                        "misconception": "Many students automatically click the very first link on a search results page, assuming it is guaranteed to be the most truthful answer.",
                        "correction": "The top entries on a Search Engine Results Page are frequently 'Sponsored Ads' paid for by commercial companies. Furthermore, ranking algorithms prioritize popular, highly-linked websites, which may not always be scientifically accurate. Always evaluate the source using the CRAAP test (Currency, Relevance, Authority, Accuracy, Purpose)."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Troubleshooting: The CRAAP Test for Information Verification",
                    "content": {
                        "mistake": "Citing unverified social media posts or anonymously edited wikis in academic school projects.",
                        "why_it_happens": "Students prioritize speed over verifying the author's credentials and evidence base.",
                        "fix_solution": "Apply the CRAAP test: Check **Currency** (is it recent?), **Relevance** (does it answer the topic?), **Authority** (is author qualified/from .ac.ke or .go.ke?), **Accuracy** (is it backed by data?), and **Purpose** (is it educational rather than selling a product?)."
                    }
                }
            ],
            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Formulating Search Queries",
                    "content": {
                        "question": "You need to locate an official PDF syllabus document on 'computer programming' from Kenyan academic institutions, while avoiding results that mention 'python'. Which search query string is the most accurate?",
                        "options": [
                            "computer programming Kenya academic no python PDF",
                            "\"computer programming\" site:ac.ke -python filetype:pdf",
                            "computer programming OR site:ac.ke AND filetype:pdf",
                            "\"computer programming\" + ac.ke + pdf - Kenya"
                        ],
                        "correct": "B",
                        "explanation": "This query uses exact phrase matching (\"computer programming\"), restricts search results to Kenyan academic institutions (site:ac.ke), excludes pages mentioning python (-python), and filters exclusively for PDF documents (filetype:pdf)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Web Evaluation Frameworks",
                    "content": {
                        "question": "Under the CRAAP test for evaluating online information sources, what does the letter 'A' for 'Authority' evaluate?",
                        "options": [
                            "The download speed of the webpage on a mobile phone",
                            "The credentials, qualifications, and organizational affiliation of the author or publisher",
                            "The number of advertisements displayed on the sidebar",
                            "Whether the document contains animated graphics and audio files"
                        ],
                        "correct": "B",
                        "explanation": "Authority evaluates the source of information: the author's expertise, institutional affiliations, reputation, and publisher domain (e.g. .ac.ke, .go.ke, university press)."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Video: How Search Engines Work & Advanced Search Tips",
                    "content": {
                        "title": "Search Engine Algorithms, Boolean Operators, and Web Research",
                        "youtube_id": "0UG0cx5kQqk",
                        "url": "https://www.youtube.com/watch?v=0UG0cx5kQqk",
                        "description": "Visual guide explaining how search engines crawl, index, and rank web pages, along with pro tips for using advanced search operators."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Search Engine Mechanics:** Spiders crawl hyperlinks ➔ Data centers build inverted keyword indexes ➔ Ranking algorithms score and return top results.\n2. **Precision Operators:** Use \"exact phrases\", -exclusion, site:domain, and filetype:extension to bypass commercial clutter.\n3. **Boolean Logic:** AND intersects concepts; OR broadens options; NOT removes unwanted terms.\n4. **CRAAP Framework:** Always evaluate web sources for Currency, Relevance, Authority, Accuracy, and Purpose before citing them in research."
                    }
                }
            ]
        ]
    }
]
