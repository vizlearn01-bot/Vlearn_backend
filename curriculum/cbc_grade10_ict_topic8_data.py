"""
VLearn CBC Grade 10 ICT — Topic 8: Digital Communication Platforms
High-Precision Vector SVGs and Structured 5-Page Lesson Card Definitions

Topic: Digital Communication Platforms (Order: 8)
Lessons:
  8.1.1: Meaning and Importance of Digital Communication (5 pages)
  8.1.2: Online Platforms for Digital Communication (5 pages)
  8.1.3: Key Features of Online Platforms (5 pages)
  8.1.4: Creating Accounts and Safe Profile Configuration (5 pages)
  8.1.5: Using Email to Send and Receive Messages (5 pages)
  8.1.6: Ethical Issues in Digital Communication (5 pages)
  8.1.7: Cloud Collaboration and AI in Digital Communication (5 pages)
"""

# =============================================================================
# HIGH PRECISION, RESPONSIVE, MOBILE-FRIENDLY VECTOR SVGS
# =============================================================================

SVG_SYNCHRONOUS_VS_ASYNCHRONOUS = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Synchronous vs Asynchronous Digital Communication Paradigms</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing Real-Time Interactive Channels with Store-and-Forward Message Systems</text>

  <!-- Left Side: Synchronous Communication -->
  <g transform="translate(45, 95)">
    <rect width="415" height="260" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="415" height="36" rx="10" fill="#0284c7"/>
    <text x="207" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SYNCHRONOUS COMMUNICATION (Real-Time)</text>
    
    <!-- User A Endpoint -->
    <g transform="translate(30, 60)">
      <circle cx="35" cy="30" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="35" y="35" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">User A</text>
      <text x="35" y="65" font-size="9" fill="#94a3b8" text-anchor="middle">Sender (Live)</text>
    </g>

    <!-- Interactive Bidirectional Wave -->
    <g transform="translate(130, 75)">
      <line x1="10" y1="5" x2="140" y2="5" stroke="#38bdf8" stroke-width="3"/>
      <polygon points="140,0 150,5 140,10" fill="#38bdf8"/>
      <line x1="140" y1="25" x2="10" y2="25" stroke="#10b981" stroke-width="3"/>
      <polygon points="10,20 0,25 10,30" fill="#10b981"/>
      <rect x="35" y="-12" width="80" height="18" rx="4" fill="#0369a1"/>
      <text x="75" y="0" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Zero Latency</text>
      <text x="75" y="45" font-size="8.5" fill="#34d399" text-anchor="middle">Instant Feedback</text>
    </g>

    <!-- User B Endpoint -->
    <g transform="translate(310, 60)">
      <circle cx="35" cy="30" r="22" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
      <text x="35" y="35" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">User B</text>
      <text x="35" y="65" font-size="9" fill="#94a3b8" text-anchor="middle">Receiver (Live)</text>
    </g>

    <!-- Properties Box -->
    <g transform="translate(20, 145)">
      <rect width="375" height="100" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#38bdf8">• Operational State:</text>
      <text x="135" y="22" font-size="9.5" fill="#cbd5e1">Both parties concurrently connected and active.</text>
      <text x="15" y="42" font-size="10" font-weight="bold" fill="#38bdf8">• Primary Channels:</text>
      <text x="135" y="42" font-size="9.5" fill="#cbd5e1">Zoom, Google Meet, Teams, Live Phone/VoIP Calls.</text>
      <text x="15" y="62" font-size="10" font-weight="bold" fill="#38bdf8">• Core Strength:</text>
      <text x="135" y="62" font-size="9.5" fill="#cbd5e1">Dynamic brainstorming, immediate conflict resolution.</text>
      <text x="15" y="82" font-size="10" font-weight="bold" fill="#38bdf8">• Key Limitation:</text>
      <text x="135" y="82" font-size="9.5" fill="#cbd5e1">Requires simultaneous scheduling across timezones.</text>
    </g>
  </g>

  <!-- Right Side: Asynchronous Communication -->
  <g transform="translate(500, 95)">
    <rect width="415" height="260" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="415" height="36" rx="10" fill="#d97706"/>
    <text x="207" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ASYNCHRONOUS COMMUNICATION (Store &amp; Forward)</text>

    <!-- User A Endpoint -->
    <g transform="translate(25, 60)">
      <circle cx="30" cy="30" r="20" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
      <text x="30" y="34" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">User A</text>
      <text x="30" y="62" font-size="8.5" fill="#94a3b8" text-anchor="middle">Sends 08:00 AM</text>
    </g>

    <!-- Arrow to Server -->
    <g transform="translate(90, 75)">
      <line x1="0" y1="15" x2="45" y2="15" stroke="#fbbf24" stroke-width="2.5"/>
      <polygon points="45,10 55,15 45,20" fill="#fbbf24"/>
    </g>

    <!-- Intermediary Server -->
    <g transform="translate(160, 50)">
      <rect width="95" height="60" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
      <text x="47" y="24" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Mail / Cloud</text>
      <text x="47" y="38" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Server</text>
      <text x="47" y="52" font-size="8" fill="#94a3b8" text-anchor="middle">Stored in Queue</text>
    </g>

    <!-- Arrow from Server -->
    <g transform="translate(265, 75)">
      <line x1="0" y1="15" x2="45" y2="15" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4,3"/>
      <polygon points="45,10 55,15 45,20" fill="#fbbf24"/>
      <text x="25" y="8" font-size="8" fill="#94a3b8" text-anchor="middle">Hours Later</text>
    </g>

    <!-- User B Endpoint -->
    <g transform="translate(330, 60)">
      <circle cx="30" cy="30" r="20" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
      <text x="30" y="34" font-size="10" font-weight="bold" fill="#a78bfa" text-anchor="middle">User B</text>
      <text x="30" y="62" font-size="8.5" fill="#94a3b8" text-anchor="middle">Reads 02:00 PM</text>
    </g>

    <!-- Properties Box -->
    <g transform="translate(20, 145)">
      <rect width="375" height="100" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#fbbf24">• Operational State:</text>
      <text x="135" y="22" font-size="9.5" fill="#cbd5e1">Sender and receiver active at completely separate times.</text>
      <text x="15" y="42" font-size="10" font-weight="bold" fill="#fbbf24">• Primary Channels:</text>
      <text x="135" y="42" font-size="9.5" fill="#cbd5e1">Email (Gmail/Outlook), Discussion Forums, Wikis.</text>
      <text x="15" y="62" font-size="10" font-weight="bold" fill="#fbbf24">• Core Strength:</text>
      <text x="135" y="62" font-size="9.5" fill="#cbd5e1">Permanent paper trail, deep reflection before answering.</text>
      <text x="15" y="82" font-size="10" font-weight="bold" fill="#fbbf24">• Key Limitation:</text>
      <text x="135" y="82" font-size="9.5" fill="#cbd5e1">Inappropriate for urgent crises or emergency triage.</text>
    </g>
  </g>

  <!-- Bottom Synthesis Framework -->
  <g transform="translate(45, 370)">
    <rect width="870" height="115" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="435" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">DECISION MATRIX: WHEN TO USE SYNCHRONOUS VS ASYNCHRONOUS CHANNELS</text>
    
    <g transform="translate(20, 35)">
      <rect width="260" height="65" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
      <text x="130" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Use Synchronous When:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Fast interactive debates are vital</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• High emotional nuance / live demos</text>
    </g>

    <g transform="translate(305, 35)">
      <rect width="260" height="65" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="130" y="20" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Use Asynchronous When:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Written proof or audit trail required</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Detailed research or deep focus needed</text>
    </g>

    <g transform="translate(590, 35)">
      <rect width="260" height="65" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="130" y="20" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Hybrid Workflow (Modern Best Practice):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Email agenda before the meeting</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Quick 15-min call, then email recap</text>
    </g>
  </g>
</svg>
""".strip()

SVG_COMMUNICATION_PLATFORMS_MATRIX = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="510" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Taxonomy of Modern Online Communication Platforms</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Categorization by Formality, Latency, Interaction Density, and Collaboration Capability</text>

  <!-- 4 Quadrants Container -->
  <g transform="translate(45, 85)">
    <!-- Quadrant 1: Electronic Mail (Top Left) -->
    <g transform="translate(0, 0)">
      <rect width="420" height="195" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8"/>
      <rect width="420" height="32" rx="8" fill="#0284c7"/>
      <text x="210" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ELECTRONIC MAIL (EMAIL)</text>
      <text x="15" y="55" font-size="10" font-weight="bold" fill="#38bdf8">• Paradigm &amp; Nature:</text>
      <text x="145" y="55" font-size="9.5" fill="#cbd5e1">Formal, Asynchronous, Structured, Legally binding.</text>
      <text x="15" y="75" font-size="10" font-weight="bold" fill="#38bdf8">• Underlying Protocols:</text>
      <text x="145" y="75" font-size="9.5" fill="#cbd5e1">SMTP (Send), IMAP/POP3 (Retrieve), MIME (Files).</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#38bdf8">• Leading Examples:</text>
      <text x="145" y="95" font-size="9.5" fill="#cbd5e1">Gmail, Microsoft Outlook, ProtonMail, Apple Mail.</text>
      <text x="15" y="115" font-size="10" font-weight="bold" fill="#38bdf8">• Ideal Enterprise Use:</text>
      <text x="145" y="115" font-size="9.5" fill="#cbd5e1">Contracts, official grades, inquiries, policy notices.</text>
      <rect x="15" y="135" width="390" height="45" rx="6" fill="#1e293b"/>
      <text x="25" y="152" font-size="9" fill="#94a3b8">Key Advantage: Permanent institutional paper trail and universal accessibility</text>
      <text x="25" y="168" font-size="9" fill="#94a3b8">without requiring both parties to use the exact same app vendor.</text>
    </g>

    <!-- Quadrant 2: Instant Messaging (Top Right) -->
    <g transform="translate(450, 0)">
      <rect width="420" height="195" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
      <rect width="420" height="32" rx="8" fill="#059669"/>
      <text x="210" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. INSTANT MESSAGING (CHAT APPS)</text>
      <text x="15" y="55" font-size="10" font-weight="bold" fill="#34d399">• Paradigm &amp; Nature:</text>
      <text x="145" y="55" font-size="9.5" fill="#cbd5e1">Informal/Semi-formal, Near-Synchronous, Rapid.</text>
      <text x="15" y="75" font-size="10" font-weight="bold" fill="#34d399">• Underlying Protocols:</text>
      <text x="145" y="75" font-size="9.5" fill="#cbd5e1">XMPP, WebSockets, Signal Protocol (E2EE).</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#34d399">• Leading Examples:</text>
      <text x="145" y="95" font-size="9.5" fill="#cbd5e1">WhatsApp, Telegram, Signal, iMessage.</text>
      <text x="15" y="115" font-size="10" font-weight="bold" fill="#34d399">• Ideal Enterprise Use:</text>
      <text x="145" y="115" font-size="9.5" fill="#cbd5e1">Urgent operational alerts, quick peer clarifications.</text>
      <rect x="15" y="135" width="390" height="45" rx="6" fill="#1e293b"/>
      <text x="25" y="152" font-size="9" fill="#94a3b8">Key Advantage: Low friction, instant delivery/read receipts, rich media sharing,</text>
      <text x="25" y="168" font-size="9" fill="#94a3b8">and high engagement across mobile devices.</text>
    </g>

    <!-- Quadrant 3: Video Conferencing (Bottom Left) -->
    <g transform="translate(0, 215)">
      <rect width="420" height="195" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.8"/>
      <rect width="420" height="32" rx="8" fill="#7c3aed"/>
      <text x="210" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. VIDEO CONFERENCING PLATFORMS</text>
      <text x="15" y="55" font-size="10" font-weight="bold" fill="#a78bfa">• Paradigm &amp; Nature:</text>
      <text x="145" y="55" font-size="9.5" fill="#cbd5e1">Synchronous, High Sensory Richness, Interactive.</text>
      <text x="15" y="75" font-size="10" font-weight="bold" fill="#a78bfa">• Core Technologies:</text>
      <text x="145" y="75" font-size="9.5" fill="#cbd5e1">WebRTC, H.264/AV1 Video Codecs, Opus Audio.</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#a78bfa">• Leading Examples:</text>
      <text x="145" y="95" font-size="9.5" fill="#cbd5e1">Zoom, Google Meet, Cisco Webex, Microsoft Teams.</text>
      <text x="15" y="115" font-size="10" font-weight="bold" fill="#a78bfa">• Ideal Enterprise Use:</text>
      <text x="145" y="115" font-size="9.5" fill="#cbd5e1">Virtual classes, webinars, interviews, live demos.</text>
      <rect x="15" y="135" width="390" height="45" rx="6" fill="#1e293b"/>
      <text x="25" y="152" font-size="9" fill="#94a3b8">Key Advantage: Transmits non-verbal facial cues, supports multi-user screen sharing,</text>
      <text x="25" y="168" font-size="9" fill="#94a3b8">breakout brainstorming rooms, and automated live transcriptions.</text>
    </g>

    <!-- Quadrant 4: Enterprise Collaboration (Bottom Right) -->
    <g transform="translate(450, 215)">
      <rect width="420" height="195" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
      <rect width="420" height="32" rx="8" fill="#d97706"/>
      <text x="210" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. ENTERPRISE COLLABORATION HUBS</text>
      <text x="15" y="55" font-size="10" font-weight="bold" fill="#fbbf24">• Paradigm &amp; Nature:</text>
      <text x="145" y="55" font-size="9.5" fill="#cbd5e1">Unified Hub, Asynchronous &amp; Synchronous Hybrid.</text>
      <text x="15" y="75" font-size="10" font-weight="bold" fill="#fbbf24">• Key Capabilities:</text>
      <text x="145" y="75" font-size="9.5" fill="#cbd5e1">Channel threads, file repository, bot automations.</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#fbbf24">• Leading Examples:</text>
      <text x="145" y="95" font-size="9.5" fill="#cbd5e1">Slack, Microsoft Teams, Discord, Basecamp.</text>
      <text x="15" y="115" font-size="10" font-weight="bold" fill="#fbbf24">• Ideal Enterprise Use:</text>
      <text x="145" y="115" font-size="9.5" fill="#cbd5e1">Project management, dev teams, cross-department sync.</text>
      <rect x="15" y="135" width="390" height="45" rx="6" fill="#1e293b"/>
      <text x="25" y="152" font-size="9" fill="#94a3b8">Key Advantage: Eliminates fragmented email clutter by centralizing topical conversations,</text>
      <text x="25" y="168" font-size="9" fill="#94a3b8">file storage, and third-party software integrations in one place.</text>
    </g>
  </g>
</svg>
""".strip()

SVG_PLATFORM_SECURITY_ARCHITECTURE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Architectural Layers of Digital Communication Platforms</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">The 6 Core Functional Modules Powering User Experience, Interoperability, and Security</text>

  <g transform="translate(60, 95)">
    <!-- Layer 1: Identity & Profile -->
    <g transform="translate(0, 0)">
      <rect width="840" height="52" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
      <rect width="180" height="52" rx="8" fill="#0284c7"/>
      <text x="90" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. IDENTITY &amp; PROFILE</text>
      <text x="200" y="24" font-size="10.5" font-weight="bold" fill="#38bdf8">Digital Persona Management:</text>
      <text x="200" y="40" font-size="9.5" fill="#cbd5e1">Handles avatars, display names, job titles, bio credentials, online presence status, and user directory indexes.</text>
    </g>

    <!-- Layer 2: Search & Indexing -->
    <g transform="translate(0, 62)">
      <rect width="840" height="52" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="180" height="52" rx="8" fill="#059669"/>
      <text x="90" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SEARCH &amp; INDEXING</text>
      <text x="200" y="24" font-size="10.5" font-weight="bold" fill="#34d399">Information Discovery Engine:</text>
      <text x="200" y="40" font-size="9.5" fill="#cbd5e1">Full-text message searching, date/channel filters, attached file content indexing, and conversational history retrieval.</text>
    </g>

    <!-- Layer 3: Customization & UI -->
    <g transform="translate(0, 124)">
      <rect width="840" height="52" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
      <rect width="180" height="52" rx="8" fill="#7c3aed"/>
      <text x="90" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. UI CUSTOMIZATION</text>
      <text x="200" y="24" font-size="10.5" font-weight="bold" fill="#a78bfa">User Experience Controls:</text>
      <text x="200" y="40" font-size="9.5" fill="#cbd5e1">Theme styling (Dark/Light mode), notification frequency rules, sidebar organization, and layout modularity.</text>
    </g>

    <!-- Layer 4: Integration & APIs -->
    <g transform="translate(0, 186)">
      <rect width="840" height="52" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="180" height="52" rx="8" fill="#d97706"/>
      <text x="90" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. API INTEGRATIONS</text>
      <text x="200" y="24" font-size="10.5" font-weight="bold" fill="#fbbf24">Interoperability &amp; Automation:</text>
      <text x="200" y="40" font-size="9.5" fill="#cbd5e1">Webhooks and REST APIs connecting Google Calendar, GitHub, Trello, cloud drives, and automated chatbot assistants.</text>
    </g>

    <!-- Layer 5: Accessibility (a11y) -->
    <g transform="translate(0, 248)">
      <rect width="840" height="52" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
      <rect width="180" height="52" rx="8" fill="#be185d"/>
      <text x="90" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. ACCESSIBILITY (a11y)</text>
      <text x="200" y="24" font-size="10.5" font-weight="bold" fill="#f472b6">Universal Inclusion Standards (WCAG):</text>
      <text x="200" y="40" font-size="9.5" fill="#cbd5e1">Live speech-to-text captions, screen-reader compatibility (ARIA), high-contrast modes, and keyboard navigation shortcuts.</text>
    </g>

    <!-- Layer 6: Privacy & Security Shield -->
    <g transform="translate(0, 310)">
      <rect width="840" height="52" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
      <rect width="180" height="52" rx="8" fill="#0891b2"/>
      <text x="90" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6. PRIVACY &amp; SECURITY</text>
      <text x="200" y="24" font-size="10.5" font-weight="bold" fill="#22d3ee">Data Protection &amp; Access Controls:</text>
      <text x="200" y="40" font-size="9.5" fill="#cbd5e1">Two-Factor Authentication (2FA), End-to-End Encryption (E2EE), Role-Based Access Controls (RBAC), and audit logs.</text>
    </g>
  </g>

  <!-- Bottom Note -->
  <g transform="translate(60, 465)">
    <rect width="840" height="28" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="420" y="18" font-size="9.5" fill="#94a3b8" text-anchor="middle">Enterprise platforms build these modular layers into microservice architectures to guarantee 99.99% uptime and compliance.</text>
  </g>
</svg>
""".strip()

SVG_ACCOUNT_SECURITY_LIFECYCLE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Secure Account Creation &amp; Profile Hardening Lifecycle</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">5-Step Framework for Establishing Credibility, Strong Cryptographic Defense, and Data Privacy</text>

  <!-- 5 Sequential Pipeline Stages -->
  <g transform="translate(35, 95)">
    <!-- Stage 1: Professional Identity -->
    <g transform="translate(0, 0)">
      <rect width="170" height="240" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
      <rect width="170" height="34" rx="8" fill="#0284c7"/>
      <text x="85" y="22" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. IDENTITY</text>
      <text x="12" y="55" font-size="9.5" font-weight="bold" fill="#38bdf8">Professional Handle:</text>
      <text x="12" y="72" font-size="8.5" fill="#cbd5e1">• first.last@domain.com</text>
      <text x="12" y="88" font-size="8.5" fill="#cbd5e1">• jane.doe2026@school.ke</text>
      <text x="12" y="120" font-size="9.5" font-weight="bold" fill="#ef4444">Avoid Casual Handles:</text>
      <text x="12" y="137" font-size="8.5" fill="#fca5a5">• cool_gamer99@...</text>
      <text x="12" y="153" font-size="8.5" fill="#fca5a5">• bad_boy_ke@...</text>
      <rect x="10" y="185" width="150" height="42" rx="6" fill="#1e293b"/>
      <text x="85" y="202" font-size="8" fill="#38bdf8" text-anchor="middle">Builds Academic &amp;</text>
      <text x="85" y="216" font-size="8" fill="#38bdf8" text-anchor="middle">Career Credibility</text>
    </g>

    <!-- Arrow 1 -> 2 -->
    <g transform="translate(172, 110)">
      <line x1="0" y1="0" x2="6" y2="0" stroke="#38bdf8" stroke-width="2"/>
    </g>

    <!-- Stage 2: Password Entropy -->
    <g transform="translate(180, 0)">
      <rect width="170" height="240" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
      <rect width="170" height="34" rx="8" fill="#059669"/>
      <text x="85" y="22" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PASSWORD</text>
      <text x="12" y="55" font-size="9.5" font-weight="bold" fill="#34d399">Entropy Standards:</text>
      <text x="12" y="72" font-size="8.5" fill="#cbd5e1">• Minimum 12+ chars</text>
      <text x="12" y="88" font-size="8.5" fill="#cbd5e1">• Mixed uppercase (A-Z)</text>
      <text x="12" y="104" font-size="8.5" fill="#cbd5e1">• Mixed lowercase (a-z)</text>
      <text x="12" y="120" font-size="8.5" fill="#cbd5e1">• Numerals &amp; Symbols</text>
      <rect x="10" y="138" width="150" height="35" rx="4" fill="#064e3b"/>
      <text x="85" y="152" font-size="8" font-weight="bold" fill="#34d399" text-anchor="middle">KeN_Lab#8!2026</text>
      <text x="85" y="165" font-size="7.5" fill="#a7f3d0" text-anchor="middle">High Cryptographic Entropy</text>
      <rect x="10" y="185" width="150" height="42" rx="6" fill="#1e293b"/>
      <text x="85" y="202" font-size="8" fill="#34d399" text-anchor="middle">Resists Dictionary &amp;</text>
      <text x="85" y="216" font-size="8" fill="#34d399" text-anchor="middle">Brute-Force Attacks</text>
    </g>

    <!-- Stage 3: Two-Factor Auth -->
    <g transform="translate(360, 0)">
      <rect width="170" height="240" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="2"/>
      <rect width="170" height="34" rx="8" fill="#7c3aed"/>
      <text x="85" y="22" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. 2FA DEFENSE</text>
      <text x="12" y="55" font-size="9.5" font-weight="bold" fill="#a78bfa">Multi-Factor Layers:</text>
      <text x="12" y="72" font-size="8.5" fill="#cbd5e1">• Authenticator App (TOTP)</text>
      <text x="12" y="88" font-size="8.5" fill="#cbd5e1">• Hardware Security Keys</text>
      <text x="12" y="104" font-size="8.5" fill="#cbd5e1">• SMS / Prompt Tokens</text>
      <text x="12" y="130" font-size="9.5" font-weight="bold" fill="#a78bfa">Mechanism:</text>
      <text x="12" y="147" font-size="8.5" fill="#cbd5e1">Something you know (PW) +</text>
      <text x="12" y="163" font-size="8.5" fill="#cbd5e1">Something you have (Phone)</text>
      <rect x="10" y="185" width="150" height="42" rx="6" fill="#1e293b"/>
      <text x="85" y="202" font-size="8" fill="#a78bfa" text-anchor="middle">Blocks 99.9% of</text>
      <text x="85" y="216" font-size="8" fill="#a78bfa" text-anchor="middle">Automated Breaches</text>
    </g>

    <!-- Stage 4: Account Recovery -->
    <g transform="translate(540, 0)">
      <rect width="170" height="240" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
      <rect width="170" height="34" rx="8" fill="#d97706"/>
      <text x="85" y="22" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. RECOVERY</text>
      <text x="12" y="55" font-size="9.5" font-weight="bold" fill="#fbbf24">Recovery Protocols:</text>
      <text x="12" y="72" font-size="8.5" fill="#cbd5e1">• Secondary email address</text>
      <text x="12" y="88" font-size="8.5" fill="#cbd5e1">• Verified mobile number</text>
      <text x="12" y="104" font-size="8.5" fill="#cbd5e1">• Offline backup codes</text>
      <text x="12" y="130" font-size="9.5" font-weight="bold" fill="#fbbf24">Key Safety Rule:</text>
      <text x="12" y="147" font-size="8.5" fill="#cbd5e1">Store backup codes in a</text>
      <text x="12" y="163" font-size="8.5" fill="#cbd5e1">secure, physical locker.</text>
      <rect x="10" y="185" width="150" height="42" rx="6" fill="#1e293b"/>
      <text x="85" y="202" font-size="8" fill="#fbbf24" text-anchor="middle">Guarantees Lockout</text>
      <text x="85" y="216" font-size="8" fill="#fbbf24" text-anchor="middle">Restoration</text>
    </g>

    <!-- Stage 5: Privacy Lockdown -->
    <g transform="translate(720, 0)">
      <rect width="170" height="240" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
      <rect width="170" height="34" rx="8" fill="#0891b2"/>
      <text x="85" y="22" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5. PRIVACY LOCK</text>
      <text x="12" y="55" font-size="9.5" font-weight="bold" fill="#22d3ee">Hardening Settings:</text>
      <text x="12" y="72" font-size="8.5" fill="#cbd5e1">• Visibility to Restricted</text>
      <text x="12" y="88" font-size="8.5" fill="#cbd5e1">• Opt-out ad tracking</text>
      <text x="12" y="104" font-size="8.5" fill="#cbd5e1">• Disable web history logs</text>
      <text x="12" y="120" font-size="8.5" fill="#cbd5e1">• Restrict data scraping</text>
      <rect x="10" y="185" width="150" height="42" rx="6" fill="#1e293b"/>
      <text x="85" y="202" font-size="8" fill="#22d3ee" text-anchor="middle">Shields Personal Data</text>
      <text x="85" y="216" font-size="8" fill="#22d3ee" text-anchor="middle">from Public Harvesting</text>
    </g>
  </g>

  <!-- Bottom Summary Card -->
  <g transform="translate(35, 350)">
    <rect width="890" height="135" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="445" y="26" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">SUMMARY: THE 3 GOLDEN RULES OF ACCOUNT HYGIENE</text>
    
    <g transform="translate(20, 42)">
      <rect width="270" height="75" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
      <text x="135" y="22" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Rule 1: Unique Credentials</text>
      <text x="15" y="42" font-size="9" fill="#cbd5e1">• Never reuse passwords across portals</text>
      <text x="15" y="58" font-size="9" fill="#cbd5e1">• Use a secure password manager</text>
    </g>

    <g transform="translate(310, 42)">
      <rect width="270" height="75" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="135" y="22" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Rule 2: Mandatory 2FA</text>
      <text x="15" y="42" font-size="9" fill="#cbd5e1">• Always enable 2FA on primary email</text>
      <text x="15" y="58" font-size="9" fill="#cbd5e1">• Protect recovery codes offline</text>
    </g>

    <g transform="translate(600, 42)">
      <rect width="270" height="75" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="135" y="22" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Rule 3: Privacy by Default</text>
      <text x="15" y="42" font-size="9" fill="#cbd5e1">• Audit connected apps quarterly</text>
      <text x="15" y="58" font-size="9" fill="#cbd5e1">• Revoke unnecessary 3rd party access</text>
    </g>
  </g>
</svg>
""".strip()

SVG_EMAIL_HEADER_ROUTING_STRUCTURE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="510" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="44" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">RFC 5322 Email Header Routing &amp; Message Envelope Architecture</text>
  <text x="480" y="66" font-size="12" fill="#94a3b8" text-anchor="middle">Anatomy of Routing Fields (To, Cc, Bcc), MIME Attachments, and SMTP/IMAP Delivery Flow</text>

  <!-- Left: Email Header & Envelope Anatomy -->
  <g transform="translate(45, 85)">
    <rect width="470" height="420" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="470" height="32" rx="10" fill="#0284c7"/>
    <text x="235" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">COMPOSE MESSAGE (CLIENT INTERFACE)</text>

    <!-- Header Fields -->
    <g transform="translate(15, 45)">
      <!-- To Field -->
      <rect width="440" height="30" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">To:</text>
      <text x="40" y="20" font-size="9.5" fill="#ffffff">treasurer@school.ac.ke</text>
      <rect x="260" y="6" width="170" height="18" rx="4" fill="#0369a1"/>
      <text x="345" y="18" font-size="8" fill="#ffffff" text-anchor="middle">Primary Action Item Recipient</text>
    </g>

    <g transform="translate(15, 80)">
      <!-- Cc Field -->
      <rect width="440" height="30" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#34d399">Cc:</text>
      <text x="40" y="20" font-size="9.5" fill="#ffffff">patron.teacher@school.ac.ke</text>
      <rect x="260" y="6" width="170" height="18" rx="4" fill="#065f46"/>
      <text x="345" y="18" font-size="8" fill="#34d399" text-anchor="middle">Carbon Copy (Public Visibility)</text>
    </g>

    <g transform="translate(15, 115)">
      <!-- Bcc Field -->
      <rect width="440" height="30" rx="4" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#fbbf24">Bcc:</text>
      <text x="45" y="20" font-size="9.5" fill="#ffffff">principal@school.ac.ke</text>
      <rect x="260" y="6" width="170" height="18" rx="4" fill="#78350f"/>
      <text x="345" y="18" font-size="8" fill="#fbbf24" text-anchor="middle">Blind Copy (Hidden Confidential)</text>
    </g>

    <g transform="translate(15, 150)">
      <!-- Subject Field -->
      <rect width="440" height="30" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#a78bfa">Subject:</text>
      <text x="68" y="20" font-size="9.5" font-weight="bold" fill="#ffffff">Annual Club Budget Proposal - Grade 10 ICT</text>
    </g>

    <!-- Message Body -->
    <g transform="translate(15, 190)">
      <rect width="440" height="140" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#cbd5e1">Dear Treasurer,</text>
      <text x="15" y="42" font-size="9.5" fill="#94a3b8">Please find attached the draft budget report for our upcoming</text>
      <text x="15" y="58" font-size="9.5" fill="#94a3b8">science exhibition. Please review Section 3 and reply by Friday.</text>
      <text x="15" y="85" font-size="9.5" fill="#cbd5e1">Kind regards,</text>
      <text x="15" y="102" font-size="9.5" font-weight="bold" fill="#38bdf8">Jane Doe — Environmental Club Chairperson</text>
      <text x="15" y="118" font-size="8.5" fill="#64748b">Greenwood Secondary School | Student ID: G10-2026</text>
    </g>

    <!-- Attachment Envelope -->
    <g transform="translate(15, 340)">
      <rect width="440" height="36" rx="6" fill="#1e293b" stroke="#10b981" stroke-dasharray="4,3"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#34d399">Attachment (MIME):</text>
      <text x="145" y="22" font-size="9.5" fill="#ffffff">annual_budget_v2.pdf (2.4 MB)</text>
      <rect x="360" y="8" width="65" height="20" rx="4" fill="#059669"/>
      <text x="392" y="21" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">VERIFIED</text>
    </g>

    <!-- Send Button -->
    <g transform="translate(15, 385)">
      <rect width="100" height="26" rx="4" fill="#0284c7"/>
      <text x="50" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">SEND NOW</text>
    </g>
  </g>

  <!-- Right: Technical Routing Lifecycle -->
  <g transform="translate(535, 85)">
    <rect width="380" height="420" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="380" height="32" rx="10" fill="#d97706"/>
    <text x="190" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SMTP &amp; IMAP TRANSMISSION PROTOCOL FLOW</text>

    <!-- Step 1: Client to Outgoing SMTP -->
    <g transform="translate(20, 48)">
      <rect width="340" height="60" rx="8" fill="#1e293b" stroke="#0ea5e9"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">1. Client Dispatch (SMTP TLS - Port 587)</text>
      <text x="15" y="36" font-size="8.5" fill="#cbd5e1">Sender's mail app encrypts message and submits to</text>
      <text x="15" y="50" font-size="8.5" fill="#cbd5e1">outgoing Simple Mail Transfer Protocol (SMTP) server.</text>
    </g>

    <!-- Step 2: DNS MX Record Lookup -->
    <g transform="translate(20, 118)">
      <rect width="340" height="60" rx="8" fill="#1e293b" stroke="#10b981"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#34d399">2. DNS MX Record Resolution</text>
      <text x="15" y="36" font-size="8.5" fill="#cbd5e1">Sending server queries global DNS for recipient domain's</text>
      <text x="15" y="50" font-size="8.5" fill="#cbd5e1">Mail Exchange (MX) IP address (e.g., mail.school.ac.ke).</text>
    </g>

    <!-- Step 3: Server-to-Server Relay -->
    <g transform="translate(20, 188)">
      <rect width="340" height="60" rx="8" fill="#1e293b" stroke="#8b5cf6"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#a78bfa">3. Server-to-Server SMTP Transfer (Port 25)</text>
      <text x="15" y="36" font-size="8.5" fill="#cbd5e1">Encrypted relay across internet routers to receiving mail</text>
      <text x="15" y="50" font-size="8.5" fill="#cbd5e1">server; Bcc headers stripped to preserve privacy.</text>
    </g>

    <!-- Step 4: Spam Filter & Mailbox Sorting -->
    <g transform="translate(20, 258)">
      <rect width="340" height="60" rx="8" fill="#1e293b" stroke="#f59e0b"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fbbf24">4. Anti-Spam &amp; Automated Rules Engine</text>
      <text x="15" y="36" font-size="8.5" fill="#cbd5e1">Receiving server checks SPF/DKIM keys, scans MIME</text>
      <text x="15" y="50" font-size="8.5" fill="#cbd5e1">attachments for malware, and applies user inbox filters.</text>
    </g>

    <!-- Step 5: IMAP Sync to Recipient -->
    <g transform="translate(20, 328)">
      <rect width="340" height="60" rx="8" fill="#1e293b" stroke="#06b6d4"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#22d3ee">5. Recipient Retrieval (IMAP - Port 993)</text>
      <text x="15" y="36" font-size="8.5" fill="#cbd5e1">Recipient's device synchronizes folders across all phones</text>
      <text x="15" y="50" font-size="8.5" fill="#cbd5e1">and laptops in real time without deleting server copy.</text>
    </g>
  </g>
</svg>
""".strip()

SVG_DIGITAL_ETHICS_NETIQUETTE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 4 Pillars of Digital Ethics, Netiquette, and Online Safety</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Legal, Moral, and Professional Responsibilities in Cyber Environments</text>

  <!-- 4 Pillars Grid Container -->
  <g transform="translate(45, 90)">
    <!-- Pillar 1: Netiquette & Tone -->
    <g transform="translate(0, 0)">
      <rect width="415" height="180" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8"/>
      <rect width="415" height="30" rx="8" fill="#0284c7"/>
      <text x="207" y="20" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PILLAR 1: NETIQUETTE &amp; PROFESSIONAL TONE</text>
      <text x="15" y="52" font-size="9.5" font-weight="bold" fill="#38bdf8">• No ALL CAPS:</text>
      <text x="120" y="52" font-size="9" fill="#cbd5e1">ALL CAPS is perceived as aggressive yelling.</text>
      <text x="15" y="70" font-size="9.5" font-weight="bold" fill="#38bdf8">• Constructive Tone:</text>
      <text x="120" y="70" font-size="9" fill="#cbd5e1">Address issues politely; avoid emotional flaming.</text>
      <text x="15" y="88" font-size="9.5" font-weight="bold" fill="#38bdf8">• Cultural Empathy:</text>
      <text x="120" y="88" font-size="9" fill="#cbd5e1">Respect diverse global backgrounds in public forums.</text>
      <rect x="15" y="110" width="385" height="55" rx="6" fill="#1e293b"/>
      <text x="25" y="128" font-size="8.5" fill="#94a3b8">Golden Rule: Remember the human behind the screen. If you would</text>
      <text x="25" y="144" font-size="8.5" fill="#94a3b8">not speak those words in person, never type them digitally.</text>
    </g>

    <!-- Pillar 2: Phishing & Social Engineering Defense -->
    <g transform="translate(455, 0)">
      <rect width="415" height="180" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.8"/>
      <rect width="415" height="30" rx="8" fill="#b91c1c"/>
      <text x="207" y="20" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PILLAR 2: PHISHING &amp; SOCIAL ENGINEERING DEFENSE</text>
      <text x="15" y="52" font-size="9.5" font-weight="bold" fill="#f87171">• Verify Sender Domains:</text>
      <text x="155" y="52" font-size="9" fill="#cbd5e1">Check for spoofing (e.g. gmai1.com vs gmail.com).</text>
      <text x="15" y="70" font-size="9.5" font-weight="bold" fill="#f87171">• False Urgency Flags:</text>
      <text x="155" y="70" font-size="9" fill="#cbd5e1">"Account suspended in 10 mins!" is a trap.</text>
      <text x="15" y="88" font-size="9.5" font-weight="bold" fill="#f87171">• Never Disclose Passwords:</text>
      <text x="155" y="88" font-size="9" fill="#cbd5e1">Legitimate platforms never ask for credentials via email.</text>
      <rect x="15" y="110" width="385" height="55" rx="6" fill="#1e293b"/>
      <text x="25" y="128" font-size="8.5" fill="#94a3b8">Protocol: STOP, INSPECT the raw URL header, and REPORT suspicious</text>
      <text x="25" y="144" font-size="8.5" fill="#94a3b8">messages to your system administrator immediately.</text>
    </g>

    <!-- Pillar 3: Digital Footprint & Privacy -->
    <g transform="translate(0, 195)">
      <rect width="415" height="180" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
      <rect width="415" height="30" rx="8" fill="#d97706"/>
      <text x="207" y="20" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PILLAR 3: DIGITAL FOOTPRINT &amp; DATA PERMANENCE</text>
      <text x="15" y="52" font-size="9.5" font-weight="bold" fill="#fbbf24">• Data Permanence:</text>
      <text x="135" y="52" font-size="9" fill="#cbd5e1">Screenshots and server caches archive content forever.</text>
      <text x="15" y="70" font-size="9.5" font-weight="bold" fill="#fbbf24">• Protect Private PII:</text>
      <text x="135" y="70" font-size="9" fill="#cbd5e1">Never publish national ID, home address, or phone info.</text>
      <text x="15" y="88" font-size="9.5" font-weight="bold" fill="#fbbf24">• Respect Peer Consent:</text>
      <text x="135" y="88" font-size="9" fill="#cbd5e1">Obtain explicit permission before tagging or posting photos.</text>
      <rect x="15" y="110" width="385" height="55" rx="6" fill="#1e293b"/>
      <text x="25" y="128" font-size="8.5" fill="#94a3b8">Career Impact: Universities and employers routinely conduct background</text>
      <text x="25" y="144" font-size="8.5" fill="#94a3b8">audits of social media footprints prior to hiring or admissions.</text>
    </g>

    <!-- Pillar 4: Intellectual Property & Copyright -->
    <g transform="translate(455, 195)">
      <rect width="415" height="180" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
      <rect width="415" height="30" rx="8" fill="#059669"/>
      <text x="207" y="20" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PILLAR 4: INTELLECTUAL PROPERTY &amp; COPYRIGHT</text>
      <text x="15" y="52" font-size="9.5" font-weight="bold" fill="#34d399">• Attribution Mandatory:</text>
      <text x="150" y="52" font-size="9" fill="#cbd5e1">Always cite authors when quoting digital publications.</text>
      <text x="15" y="70" font-size="9.5" font-weight="bold" fill="#34d399">• Creative Commons:</text>
      <text x="150" y="70" font-size="9" fill="#cbd5e1">Utilize CC-licensed media (CC BY-SA) with proper tags.</text>
      <text x="15" y="88" font-size="9.5" font-weight="bold" fill="#34d399">• Legal Framework:</text>
      <text x="150" y="88" font-size="9" fill="#cbd5e1">Kenya Copyright Act &amp; Computer Misuse Act compliance.</text>
      <rect x="15" y="110" width="385" height="55" rx="6" fill="#1e293b"/>
      <text x="25" y="128" font-size="8.5" fill="#94a3b8">Anti-Plagiarism: Copying online text without citation is academic dishonesty</text>
      <text x="25" y="144" font-size="8.5" fill="#94a3b8">and violates intellectual property laws worldwide.</text>
    </g>
  </g>

  <!-- Bottom Legal Strip -->
  <g transform="translate(45, 475)">
    <rect width="870" height="24" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="435" y="16" font-size="9" fill="#94a3b8" text-anchor="middle">Governed by the Kenya Computer Misuse and Cybercrimes Act (2018) &amp; Kenya Data Protection Act (2019).</text>
  </g>
</svg>
""".strip()

SVG_CLOUD_COLLABORATION_AI_WORKFLOW = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="510" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cloud Team Collaboration &amp; AI-Driven Media Pipeline</text>
  <text x="480" y="66" font-size="12" fill="#94a3b8" text-anchor="middle">Integrating Cloud Storage, Real-Time Co-Authoring, Kanban Tracking, Streaming, and Artificial Intelligence</text>

  <!-- 5 Interlinked Modules -->
  <g transform="translate(35, 85)">
    <!-- Stage 1: Cloud Storage & Access Tiers -->
    <g transform="translate(0, 0)">
      <rect width="170" height="270" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8"/>
      <rect width="170" height="32" rx="8" fill="#0284c7"/>
      <text x="85" y="21" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CLOUD STORAGE</text>
      <text x="10" y="52" font-size="9.5" font-weight="bold" fill="#38bdf8">Drive / Dropbox:</text>
      <text x="10" y="70" font-size="8.5" fill="#cbd5e1">• Centralized repos</text>
      <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Device sync 24/7</text>
      <text x="10" y="112" font-size="9.5" font-weight="bold" fill="#38bdf8">Access Control Tiers:</text>
      <rect x="8" y="122" width="154" height="22" rx="4" fill="#1e293b"/>
      <text x="15" y="137" font-size="8" fill="#38bdf8">Viewer: Read-only safe</text>
      <rect x="8" y="148" width="154" height="22" rx="4" fill="#1e293b"/>
      <text x="15" y="163" font-size="8" fill="#fbbf24">Commenter: Suggest only</text>
      <rect x="8" y="174" width="154" height="22" rx="4" fill="#1e293b"/>
      <text x="15" y="189" font-size="8" fill="#34d399">Editor: Full modify rights</text>
      <rect x="8" y="208" width="154" height="50" rx="6" fill="#1e293b"/>
      <text x="85" y="226" font-size="8" fill="#94a3b8" text-anchor="middle">Eliminates lost USB</text>
      <text x="85" y="240" font-size="8" fill="#94a3b8" text-anchor="middle">drives &amp; duplicate files</text>
    </g>

    <!-- Stage 2: Concurrent Co-Authoring -->
    <g transform="translate(180, 0)">
      <rect width="170" height="270" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
      <rect width="170" height="32" rx="8" fill="#059669"/>
      <text x="85" y="21" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. LIVE CO-AUTHORING</text>
      <text x="10" y="52" font-size="9.5" font-weight="bold" fill="#34d399">Google Docs / 365:</text>
      <text x="10" y="70" font-size="8.5" fill="#cbd5e1">• Concurrent cursors</text>
      <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Simultaneous typing</text>
      <text x="10" y="102" font-size="8.5" fill="#cbd5e1">• Inline comment threads</text>
      <text x="10" y="118" font-size="8.5" fill="#cbd5e1">• Instant chat sidebar</text>
      <text x="10" y="145" font-size="9.5" font-weight="bold" fill="#34d399">Version History:</text>
      <text x="10" y="163" font-size="8.5" fill="#cbd5e1">• Infinite revision log</text>
      <text x="10" y="179" font-size="8.5" fill="#cbd5e1">• One-click rollback</text>
      <rect x="8" y="208" width="154" height="50" rx="6" fill="#1e293b"/>
      <text x="85" y="226" font-size="8" fill="#34d399" text-anchor="middle">Zero conflict loss:</text>
      <text x="85" y="240" font-size="8" fill="#34d399" text-anchor="middle">Team writes in unison</text>
    </g>

    <!-- Stage 3: Visual Kanban Board -->
    <g transform="translate(360, 0)">
      <rect width="170" height="270" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.8"/>
      <rect width="170" height="32" rx="8" fill="#7c3aed"/>
      <text x="85" y="21" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. KANBAN TRACKING</text>
      <text x="10" y="52" font-size="9.5" font-weight="bold" fill="#a78bfa">Trello / Asana:</text>
      <text x="10" y="70" font-size="8.5" fill="#cbd5e1">• Visual task cards</text>
      <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Member assignments</text>
      <text x="10" y="102" font-size="8.5" fill="#cbd5e1">• Automated due dates</text>
      <text x="10" y="130" font-size="9.5" font-weight="bold" fill="#a78bfa">Column Progression:</text>
      <rect x="8" y="140" width="154" height="18" rx="3" fill="#1e293b"/>
      <text x="85" y="153" font-size="8" fill="#cbd5e1" text-anchor="middle">To Do -> In Progress</text>
      <rect x="8" y="162" width="154" height="18" rx="3" fill="#1e293b"/>
      <text x="85" y="175" font-size="8" fill="#34d399" text-anchor="middle">Completed / Verified</text>
      <rect x="8" y="208" width="154" height="50" rx="6" fill="#1e293b"/>
      <text x="85" y="226" font-size="8" fill="#a78bfa" text-anchor="middle">Prevents bottleneck</text>
      <text x="85" y="240" font-size="8" fill="#a78bfa" text-anchor="middle">confusion &amp; missed dates</text>
    </g>

    <!-- Stage 4: Streaming & Podcasts -->
    <g transform="translate(540, 0)">
      <rect width="170" height="270" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
      <rect width="170" height="32" rx="8" fill="#d97706"/>
      <text x="85" y="21" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. PODCAST &amp; STREAM</text>
      <text x="10" y="52" font-size="9.5" font-weight="bold" fill="#fbbf24">Production Cycle:</text>
      <text x="10" y="70" font-size="8.5" fill="#cbd5e1">1. Pre: Script writing</text>
      <text x="10" y="86" font-size="8.5" fill="#cbd5e1">2. Prod: Voice recording</text>
      <text x="10" y="102" font-size="8.5" fill="#cbd5e1">3. Post: Audio edit/trim</text>
      <text x="10" y="130" font-size="9.5" font-weight="bold" fill="#fbbf24">Streaming Tech:</text>
      <text x="10" y="148" font-size="8.5" fill="#cbd5e1">• Continuous packet flow</text>
      <text x="10" y="164" font-size="8.5" fill="#cbd5e1">• Zero full download wait</text>
      <text x="10" y="180" font-size="8.5" fill="#cbd5e1">• RSS feed broadcasting</text>
      <rect x="8" y="208" width="154" height="50" rx="6" fill="#1e293b"/>
      <text x="85" y="226" font-size="8" fill="#fbbf24" text-anchor="middle">Global publishing &amp;</text>
      <text x="85" y="240" font-size="8" fill="#fbbf24" text-anchor="middle">educational broadcasts</text>
    </g>

    <!-- Stage 5: AI Enhancements -->
    <g transform="translate(720, 0)">
      <rect width="170" height="270" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="1.8"/>
      <rect width="170" height="32" rx="8" fill="#0891b2"/>
      <text x="85" y="21" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5. AI ACCELERATORS</text>
      <text x="10" y="52" font-size="9.5" font-weight="bold" fill="#22d3ee">AI Automations:</text>
      <text x="10" y="70" font-size="8.5" fill="#cbd5e1">• Live Speech-to-Text</text>
      <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Real-time translations</text>
      <text x="10" y="102" font-size="8.5" fill="#cbd5e1">• Audio noise cleanup</text>
      <text x="10" y="118" font-size="8.5" fill="#cbd5e1">• Smart summaries</text>
      <text x="10" y="145" font-size="9.5" font-weight="bold" fill="#22d3ee">Recommendation:</text>
      <text x="10" y="163" font-size="8.5" fill="#cbd5e1">• Predictive algorithms</text>
      <text x="10" y="179" font-size="8.5" fill="#cbd5e1">• Tailored learning paths</text>
      <rect x="8" y="208" width="154" height="50" rx="6" fill="#1e293b"/>
      <text x="85" y="226" font-size="8" fill="#22d3ee" text-anchor="middle">Supercharges speed &amp;</text>
      <text x="85" y="240" font-size="8" fill="#22d3ee" text-anchor="middle">universal accessibility</text>
    </g>
  </g>

  <!-- Bottom Integration Workflow -->
  <g transform="translate(35, 375)">
    <rect width="890" height="130" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="445" y="24" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">END-TO-END COLLABORATIVE PROJECT WORKFLOW</text>
    
    <g transform="translate(20, 38)">
      <rect width="195" height="75" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
      <text x="97" y="20" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Phase A: Setup &amp; Research</text>
      <text x="10" y="38" font-size="8.5" fill="#cbd5e1">• Create Google Drive folder</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">• Set permissions to Viewer/Editor</text>
      <text x="10" y="66" font-size="8.5" fill="#cbd5e1">• Upload PDF reference sources</text>
    </g>

    <g transform="translate(235, 38)">
      <rect width="195" height="75" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="97" y="20" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Phase B: Script Co-Authoring</text>
      <text x="10" y="38" font-size="8.5" fill="#cbd5e1">• Open shared Google Doc</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">• Write script concurrently</text>
      <text x="10" y="66" font-size="8.5" fill="#cbd5e1">• Use comments for peer review</text>
    </g>

    <g transform="translate(450, 38)">
      <rect width="195" height="75" rx="6" fill="#1e293b" stroke="#8b5cf6"/>
      <text x="97" y="20" font-size="10" font-weight="bold" fill="#a78bfa" text-anchor="middle">Phase C: Kanban Tracking</text>
      <text x="10" y="38" font-size="8.5" fill="#cbd5e1">• Create cards on Trello</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">• Assign roles and due dates</text>
      <text x="10" y="66" font-size="8.5" fill="#cbd5e1">• Move tasks to In Progress</text>
    </g>

    <g transform="translate(665, 38)">
      <rect width="205" height="75" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="102" y="20" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Phase D: Media &amp; AI Polish</text>
      <text x="10" y="38" font-size="8.5" fill="#cbd5e1">• Record audio podcast episode</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">• Apply AI noise cancellation</text>
      <text x="10" y="66" font-size="8.5" fill="#cbd5e1">• Publish to streaming channel</text>
    </g>
  </g>
</svg>
""".strip()


# =============================================================================
# TOPIC 8 LESSON DEFINITIONS (7 LESSONS, EXACTLY 5 PAGES EACH)
# =============================================================================

TOPIC_8_LESSONS = [
    # =========================================================================
    # LESSON 8.1.1: Meaning and Importance of Digital Communication
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of Digital Communication",
        "unit_description": "Core concepts of digital communication, synchronous vs asynchronous communication paradigms, and the societal and economic impact of global connectivity.",
        "lesson_title": "Meaning and Importance of Digital Communication",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Connected Digital Learning and Global Communication",
                    "content": {
                        "title": "Students Interacting Through Modern Digital Communication Devices",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Computer_classroom_in_Kenya.jpg",
                        "caption": "Students in a modern digital computing environment connecting to global networks to share information, collaborate, and communicate across distances.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Welcome to Digital Communication Platforms",
                    "content": {
                        "text": "Think about the last time you needed to send a message to a relative in another town. Decades ago, you would write a physical letter on paper, purchase a postage stamp, travel to a post office, and wait days or weeks for a reply. Today, you type a message on a smartphone or computer, hit send, and receive a reply in seconds.\n\nThis transformation is powered by **Digital Communication Platforms**. In modern academic institutions and professional workplaces, you will rarely work alone. Teams are distributed across different campuses, cities, and countries. Mastering digital communication empowers you to correspond professionally, collaborate in real time, and share knowledge across the globe."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define digital communication and distinguish it from traditional postal and analog methods.\n- Differentiate between synchronous (real-time) and asynchronous (store-and-forward) communication channels with practical examples.\n- Analyze the 5 core societal and economic benefits of digital communication (Global Connectivity, Speed, Multimedia Integration, Cost-Effectiveness, and Workspace Collaboration).\n- Classify academic and corporate communication scenarios into appropriate synchronous or asynchronous channels."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Digital Communication Terminology",
                    "content": {
                        "term": "Digital Communication",
                        "definition": "The electronic transmission of digitized text, audio, video, and data packets across network channels between two or more computing endpoints.",
                        "simple_explanation": "Sending and receiving messages, pictures, or voice notes using phones and computers over the internet instead of physical paper mail.",
                        "technical_meaning": "The encoding of human information into binary data packets (TCP/IP), transmitted over physical or wireless telecommunication media, and decoded by destination endpoints.",
                        "example": "Sending a PDF assignment to a teacher via an online learning portal or email client."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Synchronous vs Asynchronous Paradigms",
                    "content": {
                        "term": "Synchronous & Asynchronous Communication",
                        "definition": "Synchronous communication occurs in real time with all participants actively engaged concurrently. Asynchronous communication occurs with a time delay, where messages are stored on intermediary servers until recipients retrieve them.",
                        "simple_explanation": "Synchronous is a live phone or video call where you talk back and forth immediately. Asynchronous is sending an email or text that the recipient reads and answers later.",
                        "technical_meaning": "Synchronous transmission requires low-latency concurrent session establishment between endpoints. Asynchronous transmission utilizes store-and-forward message queuing protocols (e.g., SMTP/IMAP).",
                        "example": "A live Google Meet video conference (Synchronous) versus an email sent on Gmail (Asynchronous)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Five Societal Pillars of Digital Communication",
                    "content": {
                        "text": "Digital communication has fundamentally transformed modern society across five core pillars:\n\n1. **Global Connectivity:** Bridges geographical distances, enabling students and researchers in Kenya to collaborate instantly with institutions across Africa and the world.\n2. **Speed and Efficiency:** Complex documents and multimedia packets travel across fiber and satellite links in milliseconds rather than days.\n3. **Multimedia Integration:** Communication is no longer limited to plain text; voice notes, high-definition videos, interactive charts, and datasets are integrated seamlessly.\n4. **Cost-Effectiveness:** Sending high-volume digital messages across continents costs pennies compared to physical courier logistics and international telephone tolls.\n5. **Enhanced Workspace Collaboration:** Enables remote learning and decentralized workplaces, allowing teams to co-author files concurrently and manage projects from anywhere."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Synchronous vs Asynchronous Communication Flows",
                    "content": {
                        "title": "Comparing Real-Time and Store-and-Forward Paradigms",
                        "caption": "Architectural comparison illustrating bidirectional zero-latency synchronous connections versus intermediate server-queued asynchronous message routing.",
                        "svg_content": SVG_SYNCHRONOUS_VS_ASYNCHRONOUS
                    }
                },
                {
                    "type": "step_process",
                    "title": "Framework for Selecting the Right Communication Channel",
                    "content": {
                        "intro": "Follow this 4-step decision process to choose the ideal communication mode for any academic or professional scenario:",
                        "steps": [
                            {
                                "title": "Step 1: Evaluate Time Sensitivity and Urgency",
                                "description": "If an emergency requires immediate real-time coordination (e.g., server outage, immediate scheduling clash), select a synchronous channel (voice/video call). If non-urgent, choose asynchronous (email)."
                            },
                            {
                                "title": "Step 2: Assess the Need for Documentation and Paper Trail",
                                "description": "When official contracts, assignment grades, policy directives, or financial quotes must be permanently recorded and referenced, use asynchronous email."
                            },
                            {
                                "title": "Step 3: Analyze Information Complexity and Emotional Nuance",
                                "description": "Complex debates, delicate feedback, or dynamic brainstorming sessions benefit from synchronous video meetings where facial expressions and tone prevent misunderstandings."
                            },
                            {
                                "title": "Step 4: Check Participant Timezones and Availability",
                                "description": "If team members reside across different timezones or have conflicting schedules, asynchronous tools allow thoughtful replies without scheduling burdens."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Scenario Analysis: Organizing a National Science Fair",
                    "content": {
                        "intro": "A high school science department in Nairobi is organizing an inter-school science fair with 15 participating schools. Let us analyze how they combine communication modes:",
                        "steps": [
                            "**1. Official Invitation & Rules (Asynchronous):** The lead teacher drafts a formal circular with competition guidelines and emails it to all 15 school principals. This provides an official, verifiable paper trail.",
                            "**2. Final Logistics & Judges' Briefing (Synchronous):** The night before the fair, the organizing committee convenes a 30-minute Zoom video conference to address last-minute judging criteria and answer live questions.",
                            "**3. Live Event Day Coordination (Instant Chat):** Student marshals and lab technicians use a dedicated WhatsApp group to exchange real-time status updates on projector setups and electrical power sockets.",
                            "**4. Post-Event Results & Certificates (Asynchronous):** Official score sheets and digital certificates are emailed to participating schools as PDF attachments."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Telemedicine Consultations in Rural Health Centers",
                    "content": {
                        "title": "Connecting Specialized Doctors with Remote Clinics",
                        "text": "In rural health dispensaries across Kenya, specialist doctors are often miles away. Using telemedicine platforms, a rural clinical officer can conduct a live synchronous video consultation with a cardiologist in Nairobi to examine an ultrasound stream in real time. Following the call, lab reports and high-resolution X-ray scans are transmitted asynchronously to the hospital's electronic health record server for deep specialist review."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Synchronous Communication is Always Superior to Asynchronous",
                    "content": {
                        "misconception": "Many students and workers believe that holding frequent live meetings is always more productive than sending structured written emails.",
                        "reality": "Excessive synchronous meetings lead to meeting fatigue, interrupt deep focus, and often fail to produce permanent records. Asynchronous communication gives recipients time to research, verify data, and formulate structured, high-quality responses."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Using Real-Time Calls for Detailed Technical Directives",
                    "content": {
                        "mistake": "Explaining complex 10-step instructions, account numbers, or software configurations solely over a phone call without written follow-up.",
                        "correction": "Always document technical requirements, financial numbers, and step-by-step procedures in an asynchronous written message (email or project board).",
                        "reasoning": "Human memory is imperfect; verbal instructions given over calls are easily forgotten or misremembered without written documentation."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Channel Classification",
                    "content": {
                        "question": "A school principal sends a revised term calendar to teachers via email on Monday morning, asking for feedback by Thursday. Which communication paradigm does this demonstrate?",
                        "options": [
                            "A. Synchronous communication, because all teachers received it at once.",
                            "B. Asynchronous communication, because the message is stored on a server and teachers read and respond at different times.",
                            "C. Simplex broadcast communication with zero feedback capability.",
                            "D. Peer-to-peer ad-hoc mesh networking."
                        ],
                        "correct": "B",
                        "explanation": "Email is a classic asynchronous communication channel where messages are stored on intermediary mail servers, allowing recipients to retrieve and reply on their own schedules."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Advantages of Digital Channels",
                    "content": {
                        "question": "Which of the following is a primary advantage of digital communication over traditional physical mail?",
                        "options": [
                            "A. It guarantees that the sender does not need an internet connection.",
                            "B. It allows multimedia integration (video, audio, data) and delivers messages globally in milliseconds at minimal cost.",
                            "C. It completely eliminates the need for any digital security or privacy precautions.",
                            "D. It prevents the receiver from storing or saving previous correspondence."
                        ],
                        "correct": "B",
                        "explanation": "Digital communication enables near-instantaneous global data packet transmission, integrates rich multimedia formats, and drastically lowers transmission costs compared to physical logistics."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Foundations of Digital Communication Systems",
                    "content": {
                        "title": "How Digital Communication Connects the World",
                        "youtube_id": "AkFi90lZmXA",
                        "url": "https://www.youtube.com/watch?v=AkFi90lZmXA",
                        "description": "An engaging visual breakdown of synchronous versus asynchronous communication channels, network transmission paths, and the evolution of global connectivity."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 1 Key Takeaways",
                    "content": {
                        "text": "- **Digital Communication:** The electronic transmission of digitized text, audio, video, and data packets over networked computing channels.\n- **Synchronous Communication:** Real-time, concurrent interaction requiring simultaneous participation (e.g., video calls, voice calls, live chats).\n- **Asynchronous Communication:** Time-delayed, store-and-forward interaction providing permanent documentation and scheduling flexibility (e.g., email, forums).\n- **Five Societal Pillars:** Global connectivity, rapid speed, multimedia richness, cost efficiency, and flexible remote collaboration.\n- **Channel Selection Rule:** Choose synchronous for urgency and interactive nuance; choose asynchronous for documentation, complex detail, and schedule autonomy."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8.1.2: Online Platforms for Digital Communication
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Online Platforms for Digital Communication",
        "unit_description": "Taxonomy of online digital communication platforms: email services, instant messaging chat apps, video conferencing, and enterprise collaboration hubs.",
        "lesson_title": "Online Platforms for Digital Communication",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Modern Multi-Platform Workspace",
                    "content": {
                        "title": "Professional Workspace with Digital Communication Tools",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "A modern computing workstation displaying multiple communication platforms: email inboxes, video conferencing suites, and instant collaboration channels.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Matching the Digital Tool to the Objective",
                    "content": {
                        "text": "When you look at your smartphone or computer screen, you see distinct application icons: an envelope for email, speech bubbles for chat apps, a video camera for conference calls, and workspace icons for team channels. Each of these represents a specialized **Online Communication Platform**.\n\nJust as you would not use a hammer to drive a screw, you should not use an informal chat app to submit a formal university application or an email to alert a teammate that you are outside the classroom door. Mastering the taxonomy of online platforms ensures you communicate with maximum professional impact and operational efficiency."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Categorize digital communication platforms into the 4 primary archetypes: Email, Instant Messaging, Video Conferencing, and Enterprise Collaboration Hubs.\n- Compare platforms by formality, response latency, multimedia capability, and documentation permanence.\n- Evaluate the technical features and protocols powering each platform archetype (SMTP, WebSockets, WebRTC, E2EE).\n- Select the most appropriate platform for diverse academic, corporate, and social scenarios."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Email and Instant Messaging Archetypes",
                    "content": {
                        "term": "Electronic Mail vs Instant Messaging",
                        "definition": "Electronic Mail (Email) is an asynchronous, formal communication system providing a permanent legal record. Instant Messaging (Chat Apps) is a rapid, near-synchronous platform designed for quick text and media exchanges with delivery receipts.",
                        "simple_explanation": "Email is like sending an official typed letter with an envelope. Instant messaging is like having a rapid chat with a friend or colleague on your phone.",
                        "technical_meaning": "Email relies on standardized RFC internet protocols (SMTP/IMAP) for cross-provider message transfer. Instant messaging uses persistent WebSockets and proprietary server push networks with End-to-End Encryption (E2EE).",
                        "example": "Submitting a scholarship application via Gmail (Email) versus texting a group project member on WhatsApp (Instant Messaging)."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Video Conferencing and Enterprise Hubs",
                    "content": {
                        "term": "Video Conferencing & Enterprise Collaboration Hubs",
                        "definition": "Video Conferencing platforms provide real-time audio/video transmission and screen-sharing for virtual meetings. Enterprise Collaboration Hubs are unified workspaces that organize topical team conversations into channels, integrate cloud files, and automate workflows.",
                        "simple_explanation": "Video conferencing is a live virtual meeting room. Collaboration hubs (like Slack or Teams) are digital office headquarters where teams chat in topic channels, share files, and track tasks.",
                        "technical_meaning": "Video conferencing utilizes WebRTC and dynamic bitrate video codecs (AV1/H.264). Collaboration hubs combine message bus architectures, REST APIs, and role-based access control.",
                        "example": "Hosting a virtual guest lecture on Zoom (Video Conferencing) versus managing a software project in Microsoft Teams or Slack (Collaboration Hub)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "In-Depth Analysis of the Four Platform Archetypes",
                    "content": {
                        "text": "Modern digital communication platforms fall into four distinct functional categories:\n\n1. **Electronic Mail (Email - e.g., Gmail, Outlook, ProtonMail):** The cornerstone of official correspondence. It provides structured addressing (To, Cc, Bcc), attachment support up to 25MB, and permanent archiving. It is cross-platform and vendor-agnostic.\n2. **Instant Messaging (Chat Apps - e.g., WhatsApp, Telegram, Signal):** Optimized for low latency, mobile convenience, group chats, and instant voice notes. Features end-to-end encryption to safeguard private conversations.\n3. **Video Conferencing (e.g., Zoom, Google Meet, Cisco Webex):** Delivers rich audiovisual communication, screen sharing, interactive whiteboards, and breakout rooms, effectively simulating physical face-to-face meetings.\n4. **Enterprise Collaboration Hubs (e.g., Slack, Microsoft Teams, Discord):** Replaces messy email threads with organized, thematic channels (e.g., `#general`, `#project-budget`, `#design`). Integrates third-party tools like calendars, cloud drives, and task trackers."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Taxonomy Matrix of Online Communication Platforms",
                    "content": {
                        "title": "Comparative Architecture of Communication Tools",
                        "caption": "Quadrant matrix mapping Email, Chat Apps, Video Conferencing, and Enterprise Hubs across formality, latency, and collaborative power.",
                        "svg_content": SVG_COMMUNICATION_PLATFORMS_MATRIX
                    }
                },
                {
                    "type": "step_process",
                    "title": "Multi-Tier Platform Selection Framework for Organizations",
                    "content": {
                        "intro": "When initiating a new communication stream, follow this systematic evaluation framework:",
                        "steps": [
                            {
                                "title": "1. Determine the Legal and Organizational Formality",
                                "description": "If the communication involves contracts, official complaints, academic admissions, or financial quotes, dispatch it through formal Email."
                            },
                            {
                                "title": "2. Assess the Need for Topic Organization and File Centralization",
                                "description": "If coordinating a long-term group project with multiple sub-tasks and shared files, set up a dedicated channel inside an Enterprise Collaboration Hub (Slack/Teams)."
                            },
                            {
                                "title": "3. Evaluate Visual Demonstration Requirements",
                                "description": "If the task requires demonstrating software, walking through a slide deck, or conducting an interview, schedule a Video Conference (Zoom/Meet)."
                            },
                            {
                                "title": "4. Handle Quick Operational Queries and Field Alerts",
                                "description": "For immediate logistical queries, quick status updates, or time-sensitive travel notices, use Instant Messaging chat groups."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Coordinating a School Mobile App Development Team",
                    "content": {
                        "intro": "A team of four Grade 10 students is building a revision quiz app for their school. Let us observe how they map their tasks to the appropriate platforms:",
                        "steps": [
                            "**Task 1: Project Sponsorship Approval (Email):** The team writes a formal proposal letter and emails it to the school principal and ICT head to obtain official approval and lab access.",
                            "**Task 2: Daily Developer Collaboration (Slack / Teams):** The team sets up a workspace with channels `#ui-design`, `#coding`, and `#testing`. They post daily code snippets and share icons directly in the channels.",
                            "**Task 3: Weekly Code Review & Live Demo (Google Meet):** Every Saturday morning, the team hosts a 45-minute video call where the lead programmer shares their screen to demonstrate working app features.",
                            "**Task 4: Quick Morning Lab Alerts (WhatsApp):** When a team member arrives early at the computer lab, they send a quick text: 'Lab room 3 is open and projectors are set up!'"
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Corporate Hybrid Workplaces in Kenya's Tech Hub",
                    "content": {
                        "title": "Silicon Savannah: How Kenyan Tech Firms Communicate",
                        "text": "In Nairobi's technology ecosystem, companies like Safaricom, Twiga Foods, and software development agencies operate hybrid teams across multiple counties. Software engineers discuss API documentation in Slack channels, executives review financial contracts via Microsoft Outlook email, customer support teams coordinate field dispatches on WhatsApp Business, and all-hands quarterly meetings are held over Zoom with hundreds of participants."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: A Single Chat App (like WhatsApp) Can Replace All Enterprise Tools",
                    "content": {
                        "misconception": "Many small business owners and student clubs believe they can run entire organizations exclusively using WhatsApp group chats.",
                        "reality": "Chat apps quickly suffer from message clutter, lack threaded file indexing, mix personal and professional notifications, and provide weak project management capabilities compared to dedicated enterprise hubs."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Sending Sensitive Formal Requests via Ephemeral Chat Messages",
                    "content": {
                        "mistake": "Sending an official scholarship request, fee waiver appeal, or employment resignation via a casual text message on an instant chat app.",
                        "correction": "Always draft official appeals, legal notices, and formal requests using structured Email or official document submission portals.",
                        "reasoning": "Email provides an immutable, timestamped paper trail and maintains appropriate professional etiquette."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Platform Selection Scenario",
                    "content": {
                        "question": "Which platform is best suited for an engineering team that needs to organize conversations into thematic topic channels, integrate automated GitHub notifications, and centralize project files?",
                        "options": [
                            "A. A personal SMS text messaging service.",
                            "B. An Enterprise Collaboration Hub like Slack or Microsoft Teams.",
                            "C. A basic telephone voice call.",
                            "D. A single personal email inbox without folders."
                        ],
                        "correct": "B",
                        "explanation": "Enterprise Collaboration Hubs (like Slack or Microsoft Teams) are specifically engineered to structure team communications into thematic channels, integrate software tools, and centralize shared resources."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Formality and Legal Records",
                    "content": {
                        "question": "Why is Electronic Mail (Email) preferred over instant chat apps when sending signed contracts and official academic certificates?",
                        "options": [
                            "A. Because email does not require a computer to view.",
                            "B. Because email provides a formal, structured, vendor-neutral paper trail recognized legally in professional and academic institutions.",
                            "C. Because email guarantees that the recipient must respond within 5 seconds.",
                            "D. Because chat apps cannot send any files."
                        ],
                        "correct": "B",
                        "explanation": "Email provides an immutable, standardized, vendor-agnostic record with detailed cryptographic headers (DKIM/SPF) and formal structure, making it the globally accepted standard for legal and official correspondence."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Navigating Digital Communication Platforms",
                    "content": {
                        "title": "Choosing the Right Communication Platform for Work and Study",
                        "youtube_id": "7_LPdttKXPc",
                        "url": "https://www.youtube.com/watch?v=7_LPdttKXPc",
                        "description": "A comprehensive tour comparing modern digital communication tools: email architectures, chat ecosystems, video conferencing suites, and enterprise collaboration hubs."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 2 Key Takeaways",
                    "content": {
                        "text": "- **Four Platform Archetypes:** Electronic Mail (formal record), Instant Messaging (quick chat), Video Conferencing (live audiovisual meeting), and Enterprise Hubs (channel-based team workspaces).\n- **Email Strengths:** Vendor-neutral, structured, formal paper trail, ideal for contracts and official inquiries.\n- **Chat Strengths:** Low friction, instant delivery notifications, end-to-end encrypted, ideal for operational field alerts.\n- **Video Conferencing Strengths:** Rich non-verbal cues, screen sharing, breakout rooms, interactive whiteboards.\n- **Enterprise Hub Strengths:** Eliminates cluttered email threads by organizing topics into channels with API automations."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8.1.3: Key Features of Online Platforms
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Key Features of Online Platforms",
        "unit_description": "Core architectural features of digital communication software: user profile identity, search indexing, customizable layouts, API integration modules, accessibility compliance, and privacy controls.",
        "lesson_title": "Key Features of Online Platforms",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "User Interface and Feature Architecture",
                    "content": {
                        "title": "Navigating Modern Online Application Features and Settings",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Desktop_computer_clipart_-_Yellow_theme.svg/800px-Desktop_computer_clipart_-_Yellow_theme.svg.png",
                        "caption": "A modern graphical computing interface illustrating user identity profiles, search filters, accessibility options, and privacy security controls.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Unified Anatomy of Digital Interfaces",
                    "content": {
                        "text": "Whether you are logging into Google Classroom, Microsoft Teams, Slack, or an online academic portal, you will notice consistent design patterns across all of them. You almost always find a profile picture in the top-right corner, a universal search bar at the top, a settings gear icon, notification toggles, and accessibility options.\n\nThese common **Platform Features** are not random design choices; they are deliberate software engineering standards designed to make communication systems intuitive, inclusive, customizable, and secure. Once you understand the core functions of these six architectural layers, you can open any new digital communication application and navigate it fluently."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and explain the 6 standard architectural features of modern communication platforms: User Profiles, Search Indexing, UI Customization, API Integrations, Accessibility (a11y), and Privacy Controls.\n- Explain how Application Programming Interfaces (APIs) and integration modules connect communication platforms with external services.\n- Describe how digital accessibility features (closed captions, screen readers, high-contrast modes) empower diverse users under Web Content Accessibility Guidelines (WCAG).\n- Configure platform settings to optimize productivity while protecting personal privacy."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "API Integrations and Interoperability",
                    "content": {
                        "term": "Application Programming Interface (API) & Integrations",
                        "definition": "An API is a software intermediary that allows two distinct applications to communicate and share data automatically. Integration modules use APIs to embed external calendars, cloud drives, and automated bots directly inside communication workspaces.",
                        "simple_explanation": "An API is like a digital waiter who takes a request from your chat app to a calendar app and brings back the meeting schedule automatically.",
                        "technical_meaning": "A defined set of HTTP REST/GraphQL endpoints and JSON serialization formats enabling programmatic interoperability between disparate cloud microservices.",
                        "example": "Connecting Google Calendar to Microsoft Teams so upcoming class reminders pop up in your chat channel automatically."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Digital Accessibility (a11y) Terminology",
                    "content": {
                        "term": "Digital Accessibility (a11y) & Assistive Technologies",
                        "definition": "The inclusive software design practice of ensuring that digital platforms, interfaces, and media are completely usable by individuals with diverse visual, auditory, cognitive, and motor abilities.",
                        "simple_explanation": "Building software with tools like subtitles, large clear fonts, and voice readers so everyone, including people with disabilities, can communicate easily.",
                        "technical_meaning": "Compliance with Web Content Accessibility Guidelines (WCAG 2.2 Level AA), implementing Accessible Rich Internet Applications (ARIA) attributes, semantic HTML, keyboard-only tab navigation, and live speech-to-text engines.",
                        "example": "Turning on live closed captions in Google Meet for a hearing-impaired classmate during a video lecture."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Six Core Architectural Layers of Communication Platforms",
                    "content": {
                        "text": "Every enterprise communication platform is constructed upon six foundational functional layers:\n\n1. **User Identity & Profile Management:** Manages user avatars, display names, contact info, job roles, and real-time status indicators (Available, Busy, Away, Offline).\n2. **Search and Indexing Engine:** Indexes text messages, PDF attachments, and member directories, enabling users to locate specific conversations in milliseconds using keywords and boolean filters.\n3. **Customizable User Interface (UI):** Provides layout adaptability, including Dark Mode/Light Mode toggles, font scaling, sidebar folding, and customized notification frequencies.\n4. **API Integration Modules:** Allows third-party tools (e.g., Trello task boards, Google Drive, automated survey bots) to plug directly into communication channels.\n5. **Universal Accessibility (a11y):** Incorporates real-time speech transcription, screen-reader compatibility, keyboard shortcuts, and alternative text (alt-text) for images.\n6. **Privacy & Security Shield:** Enforces Two-Factor Authentication (2FA), end-to-end encryption, user blocking, and granular role-based access permissions (Admin, Member, Guest)."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Architectural Layers of Modern Communication Platforms",
                    "content": {
                        "title": "The 6 Structural Functional Layers of Communication Platforms",
                        "caption": "Architectural diagram showing how user profiles, search engines, UI customizers, API integrations, accessibility engines, and security shields integrate.",
                        "svg_content": SVG_PLATFORM_SECURITY_ARCHITECTURE
                    }
                },
                {
                    "type": "step_process",
                    "title": "Configuring Accessibility and Focus Settings on a Communication App",
                    "content": {
                        "intro": "Follow these steps to optimize an online communication platform for accessibility and focused productivity:",
                        "steps": [
                            {
                                "title": "Step 1: Access Platform Preferences",
                                "description": "Click your Profile avatar in the top-right corner and select **Settings** or **Preferences** (represented by a gear icon)."
                            },
                            {
                                "title": "Step 2: Configure Display and Accessibility (a11y)",
                                "description": "Navigate to the **Accessibility / Appearance** tab. Enable **High Contrast Mode** or **Dark Theme** to reduce eye strain. Turn on **Closed Captions** and test **Screen Reader Optimization**."
                            },
                            {
                                "title": "Step 3: Tune Notification Frequencies",
                                "description": "Open **Notifications**. Set alerts to 'Direct Mentions Only' (@your_name) rather than 'All Messages'. Configure a 'Do Not Disturb' schedule during revision hours to prevent distractions."
                            },
                            {
                                "title": "Step 4: Audit Connected Application Permissions",
                                "description": "Open **Integrations / Connected Apps**. Review all third-party bots and external tools connected to your profile, revoking access for any outdated or unused services."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Integrating an Automated Calendar Bot in a Student Study Group",
                    "content": {
                        "intro": "A study group uses Microsoft Teams or Slack to prepare for Kenya National Examinations. Let us examine how they use platform features:",
                        "steps": [
                            "**1. Linking Calendar via API:** The group administrator connects Google Calendar to their `#study-schedule` channel using an integration webhook.",
                            "**2. Automated Reminders:** 15 minutes before every virtual study session, the bot automatically posts: 'Reminder: Mathematics revision session starts at 4:00 PM on Google Meet! Click here to join.'",
                            "**3. Search Indexing Retrieval:** When a member forgets a past physics formula, they type `has:file physics revision formulas` into the search bar, instantly retrieving the exact PDF uploaded three weeks prior.",
                            "**4. Accessibility Activation:** A student with low vision turns on 150% font scaling and keyboard navigation (Tab + Enter) to participate comfortably without a mouse."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Inclusive Digital Classrooms in Kenyan Secondary Schools",
                    "content": {
                        "title": "Bridging Learning Barriers with Assistive Technologies",
                        "text": "When schools integrate platforms like VLearn or Google Classroom, built-in accessibility features ensure no student is left behind. Visually impaired students navigate lesson cards using NVDA or TalkBack screen readers that read semantic headers and image alt-text aloud. In virtual video classes, AI-driven real-time speech-to-text subtitles assist students who are deaf or hard-of-hearing, ensuring equitable access to quality education."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Accessibility Features Only Benefit People with Permanent Disabilities",
                    "content": {
                        "misconception": "Many people assume features like closed captions, high contrast, and text-to-speech are only for individuals with certified disabilities.",
                        "reality": "Accessibility features benefit everyone. For example, subtitles allow students to study in noisy environments without earphones, high contrast reduces eye fatigue during late-night revision, and voice-to-text enables rapid note-taking on the move."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Leaving Notification Alerts Set to 'All Messages'",
                    "content": {
                        "mistake": "Allowing sound and banner notifications for every single post across 10 large public channels and group chats.",
                        "correction": "Configure notification filters to alert you only when you are directly mentioned or assigned a high-priority direct message.",
                        "reasoning": "Constant notification pings cause cognitive fragmentation, severely degrading concentration, learning retention, and academic productivity."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: API Integrations",
                    "content": {
                        "question": "What is the primary role of an Application Programming Interface (API) integration module in a communication workspace like Microsoft Teams or Slack?",
                        "options": [
                            "A. To physically increase the processing speed of the user's CPU chip.",
                            "B. To allow external software services (like calendars, cloud storage, and task planners) to exchange data and automate workflows within the workspace.",
                            "C. To prevent the user from changing their account password.",
                            "D. To permanently block all incoming internet connections."
                        ],
                        "correct": "B",
                        "explanation": "API integration modules enable seamless interoperability between different software platforms, allowing automated notifications, calendar syncing, and file sharing directly inside communication channels."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Digital Accessibility (a11y)",
                    "content": {
                        "question": "Which platform feature directly assists a student with visual impairment in understanding an instructional image posted in a digital classroom?",
                        "options": [
                            "A. Dark Mode theme toggle.",
                            "B. Image Alternative Text (Alt-Text) read aloud by a screen reader.",
                            "C. Muting channel notifications.",
                            "D. Changing the account display name."
                        ],
                        "correct": "B",
                        "explanation": "Alternative Text (Alt-Text) provides a concise, descriptive text explanation of an image, which assistive screen readers (like NVDA or TalkBack) read aloud for visually impaired users."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Platform Architecture and Accessibility Standards",
                    "content": {
                        "title": "Understanding Modern Software Features and Accessibility",
                        "youtube_id": "kJQP7kiw5Fk",
                        "url": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
                        "description": "An insightful exploration of modern user interface components, API integrations, and universal accessibility features designed according to international standards."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3 Key Takeaways",
                    "content": {
                        "text": "- **Six Architectural Pillars:** User Profiles (identity), Search & Indexing (discovery), UI Customization (themes), API Integrations (interoperability), Accessibility (inclusion), and Security Shield (protection).\n- **APIs & Webhooks:** Connect communication platforms to external tools like Google Calendar, GitHub, and cloud storage for automated workflows.\n- **Accessibility (a11y):** Empowers diverse users through closed captions, screen reader compatibility (ARIA/Alt-text), high contrast, and keyboard navigation.\n- **Notification Management:** Filter alerts to direct mentions only to prevent cognitive overload and protect academic focus."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8.1.4: Creating Accounts and Safe Profile Configuration
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Creating Accounts and Safe Profile Configuration",
        "unit_description": "Registering digital identities, professional username conventions, robust password entropy, two-factor authentication (2FA), account recovery options, and privacy lockdown.",
        "lesson_title": "Creating Accounts and Safe Profile Configuration",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Digital Security and Identity Management",
                    "content": {
                        "title": "Secure Account Creation and Two-Factor Authentication Setup",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "A user setting up a secure online account, configuring strong passwords, multi-factor authentication, and privacy settings on a computing workstation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Your Virtual Handshake and Digital Identity",
                    "content": {
                        "text": "Before you can send an email on Gmail, join a class on VLearn, or contribute to an open-source project on GitHub, you must create an account. This registration process establishes your **Digital Identity**.\n\nYour online profile serves as your virtual handshake. Long before an employer, teacher, or scholarship board meets you in person, they see your username, profile image, and email address. Configuring your profile professionally establishes credibility, while applying rigorous cybersecurity controls (like high-entropy passwords and Two-Factor Authentication) protects your identity from cybercriminals and data harvesting."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Craft professional, credible username and email handle conventions for academic and career platforms.\n- Evaluate password strength and apply entropy principles (12+ characters, mixed case, numbers, special symbols).\n- Implement Two-Factor Authentication (2FA) and configure secure account recovery protocols.\n- Adjust account privacy settings to restrict public data harvesting, tracking, and identity theft."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Two-Factor and Multi-Factor Authentication",
                    "content": {
                        "term": "Two-Factor Authentication (2FA) & MFA",
                        "definition": "A security defense mechanism requiring users to provide two distinct authentication factors before gaining access to an account: something you know (password) plus something you have (phone/security key) or something you are (biometrics).",
                        "simple_explanation": "Like needing both a physical door key and a secret code to unlock your house, making it impossible for a thief with just the key to enter.",
                        "technical_meaning": "Time-based One-Time Password (TOTP) cryptographic algorithms (RFC 6238) or FIDO2/WebAuthn public-key credentials verifying identity beyond single-factor passwords.",
                        "example": "Entering your password on Google and confirming the login via a prompt on your smartphone or an authenticator code."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Personally Identifiable Information (PII)",
                    "content": {
                        "term": "Personally Identifiable Information (PII) & Privacy",
                        "definition": "Any data that could potentially identify a specific individual (e.g., national ID number, home GPS coordinates, phone number, biometric records, date of birth).",
                        "simple_explanation": "Private personal details that criminals can use to impersonate you, steal your money, or track where you live.",
                        "technical_meaning": "Protected data categories regulated under legal frameworks (such as the Kenya Data Protection Act 2019) requiring strict encryption and restricted public disclosure.",
                        "example": "Your full legal name paired with your birth certificate number and residential address."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Anatomy of a Safe, Professional Online Profile",
                    "content": {
                        "text": "When registering on communication platforms, follow two essential principles: Professional Credibility and Security Hardening:\n\n1. **Professional Naming Conventions:** Always use clear combinations of your real name (e.g., `jane.doe@gmail.com` or `j.doe2026@school.ac.ke`). Never use informal slang handles (e.g., `cool_kid99@...` or `bad_boy_ke@...`) for academic or professional platforms.\n2. **High-Entropy Passwords:** Passwords must be at least 12 characters long and combine uppercase letters, lowercase letters, numbers, and special symbols (e.g., `KeN_Lab#8!2026`). Never use personal dates, phone numbers, or simple dictionary words.\n3. **Multi-Factor Authentication (2FA):** Always activate 2FA using an authenticator app (Google Authenticator) or security prompt. This stops 99.9% of unauthorized automated account takeovers.\n4. **Secure Recovery Channels:** Provide an active recovery phone number and backup secondary email to restore access during emergencies.\n5. **Privacy Lockdown:** Set profile visibility to 'Restricted/Private' and opt out of third-party advertising data sharing."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Secure Account Creation & Profile Hardening Lifecycle",
                    "content": {
                        "title": "The 5-Stage Identity Security Lifecycle",
                        "caption": "Step-by-step security pipeline from professional handle selection and password entropy to 2FA activation, recovery setup, and privacy lockdown.",
                        "svg_content": SVG_ACCOUNT_SECURITY_LIFECYCLE
                    }
                },
                {
                    "type": "step_process",
                    "title": "Step-by-Step Procedure: Registering a Professional Email Account",
                    "content": {
                        "intro": "Follow these 8 steps to register a new account on a standard platform (such as Gmail or Outlook) following secure best practices:",
                        "steps": [
                            {
                                "title": "Step 1: Navigate to Secure Portal",
                                "description": "Open a secure web browser (verify the padlock and `https://` prefix) and go to the official portal (e.g., `https://accounts.google.com`). Click **Create Account**."
                            },
                            {
                                "title": "Step 2: Enter Legal First & Last Name",
                                "description": "Select 'For work/school' or 'For personal use'. Type your accurate legal First Name and Last Name to ensure proper record indexing."
                            },
                            {
                                "title": "Step 3: Select a Professional Username",
                                "description": "Choose a clean, professional handle such as `first.last@domain.com` or `f.last2026@domain.com`. Avoid informal nicknames or gaming tags."
                            },
                            {
                                "title": "Step 4: Create a High-Entropy Password",
                                "description": "Generate a unique password containing at least 12 characters, mixing uppercase, lowercase, numerals, and symbols (e.g., `Gr10_Ict#Secure26!`)."
                            },
                            {
                                "title": "Step 5: Configure Backup Recovery Options",
                                "description": "Provide a secondary email address and verified mobile phone number. These ensure you can regain access if locked out."
                            },
                            {
                                "title": "Step 6: Complete Multi-Factor Verification",
                                "description": "Type the verification code sent to your phone or backup email to prove ownership of the recovery channel."
                            },
                            {
                                "title": "Step 7: Enforce Privacy & Tracking Opt-Outs",
                                "description": "During onboarding, opt out of personalized ad tracking, disable location history storage, and set profile visibility to 'Private'."
                            },
                            {
                                "title": "Step 8: Verify Dashboard & Enable 2FA",
                                "description": "Once inside the dashboard, navigate to **Security Settings** and activate **2-Step Verification** with an authenticator app."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Password Strength Evaluation: Weak vs Strong Formats",
                    "content": {
                        "intro": "Let us compare three candidate passwords against modern automated brute-force attack tools:",
                        "steps": [
                            "**Candidate 1: `jason2010` (Extremely Weak):** Only 9 characters, uses a common first name and year. An automated cracker using a standard word dictionary cracks this in under 0.02 seconds.",
                            "**Candidate 2: `Password123!` (Weak):** Predictable dictionary word with standard sequential numbers. Included in top leaked password lists; cracked in under 1 second.",
                            "**Candidate 3: `K3ny@_G10#Sec2026!` (Extremely Strong):** 18 characters, mixes uppercase, lowercase, numbers, underscores, hashes, and exclamation marks. Would take automated supercomputers centuries to brute-force.",
                            "**Recommendation:** Always combine 3-4 unrelated words with symbols and numbers (Passphrase method) or use a secure password manager to generate random strings."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Defending Against SIM-Swap and Credential Stuffing in Kenya",
                    "content": {
                        "title": "Securing Mobile Banking and Academic Portals",
                        "text": "Cybercriminals in Kenya often use 'Credential Stuffing'—taking leaked email/password pairs from compromised gaming websites and testing them against school portals and M-Pesa linked accounts. Citizens who use app-based 2FA (like Google Authenticator) rather than simple SMS codes remain completely protected, because hackers cannot generate the time-based token even if they execute an unauthorized SIM-swap."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Using the Same Strong Password Across All Accounts is Safe",
                    "content": {
                        "misconception": "Many users create one complex password and reuse it for their school email, social media, online banking, and gaming platforms.",
                        "reality": "If just one insecure website gets breached, attackers obtain your master password and unlock every other account you own. Every account must have a unique password."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Disclosing Account Verification Codes (OTPs) Over Phone Calls",
                    "content": {
                        "mistake": "Reading aloud a 6-digit SMS verification code to a caller claiming to be 'customer support' or 'portal administrator'.",
                        "correction": "Never share verification codes, OTPs, or recovery keys with anyone. Real administrators will never ask for your code.",
                        "reasoning": "Scammers use social engineering to trigger a password reset on your account and trick you into giving them the authorization code."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Professional Username Selection",
                    "content": {
                        "question": "Which of the following email addresses is the most appropriate for submitting a formal scholarship application to a university?",
                        "options": [
                            "A. `dank_memes_king2026@gmail.com`",
                            "B. `jane.wanjiku.academic@gmail.com`",
                            "C. `fast_runner_ke_101@yahoo.com`",
                            "D. `anonymous_student_x@hotmail.com`"
                        ],
                        "correct": "B",
                        "explanation": "Professional email usernames should clearly incorporate combinations of your real legal name (e.g., `jane.wanjiku.academic@gmail.com`) to establish credibility and clear identity in formal correspondence."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Multi-Factor Authentication Mechanics",
                    "content": {
                        "question": "How does Two-Factor Authentication (2FA) protect an online account even if a hacker discovers the correct password?",
                        "options": [
                            "A. It deletes the account immediately after one failed login attempt.",
                            "B. It requires a second independent verification factor (such as a time-based code from an authenticator app on the user's physical phone) that the hacker does not possess.",
                            "C. It automatically changes the user's password every 5 minutes.",
                            "D. It restricts internet access to daylight hours only."
                        ],
                        "correct": "B",
                        "explanation": "Two-Factor Authentication pairs 'something you know' (password) with 'something you have' (physical phone/authenticator token), preventing unauthorized login even if the password is stolen."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Account Security, Passwords, and 2FA Defense",
                    "content": {
                        "title": "Protecting Your Digital Identity and Accounts Online",
                        "youtube_id": "f_Q0K2qK8vA",
                        "url": "https://www.youtube.com/watch?v=f_Q0K2qK8vA",
                        "description": "A practical guide to creating unbreakable passphrases, setting up Two-Factor Authentication (2FA), and configuring privacy settings to prevent identity theft."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 4 Key Takeaways",
                    "content": {
                        "text": "- **Digital Identity:** Your online profile and email handle serve as your virtual handshake; use clear, professional naming conventions (`first.last@domain.com`).\n- **Password Entropy:** Use at least 12+ characters mixing uppercase, lowercase, numbers, and special symbols; never reuse passwords across platforms.\n- **Two-Factor Authentication (2FA):** Combines a password with an independent physical token (authenticator app) to stop 99.9% of unauthorized logins.\n- **Account Recovery:** Always configure backup secondary emails and phone numbers, and store emergency recovery keys in a safe physical place.\n- **Privacy Lockdown:** Set profile visibility to restricted and opt out of public ad tracking to defend against data harvesting."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8.1.5: Using Email to Send and Receive Messages
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Using Email to Send and Receive Messages",
        "unit_description": "Email architecture and routing (To, Cc, Bcc), formal composition etiquette, attachment management, automated inbox filters, folders/labels, and digital signatures.",
        "lesson_title": "Using Email to Send and Receive Messages",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Professional Email and Document Correspondence",
                    "content": {
                        "title": "Formal Digital Correspondence and Electronic Mail Management",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Printed_documents_and_stationery.jpg",
                        "caption": "Professional office correspondence, illustrating formal letter structure, digital attachments, and structured communication protocols.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Digital Postal System: Mastering Email",
                    "content": {
                        "text": "Have you ever examined a traditional physical letter? It contains a 'To' address, a 'Return' address, and a postage stamp. Inside, there is a date, a formal salutation, body paragraphs, a polite sign-off, and a physical signature. The architecture of **Electronic Mail (Email)** was designed directly from this time-tested communication system.\n\nEmail remains the universal standard for business, legal, and academic correspondence worldwide. Whether you are submitting a research project, communicating with a university professor, or applying for an internship, structuring your email properly and mastering inbox automation (folders, filters, and signatures) is an essential digital literacy skill."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between email addressing fields: To (primary action), Cc (carbon copy visibility), and Bcc (blind carbon copy confidentiality).\n- Compose a structured, formal email with a clear subject line, salutation, body paragraphs, and professional signature.\n- Attach documents safely within MIME file size limits (25MB) and verify outgoing delivery.\n- Automate inbox organization using labels/folders, incoming filter rules, and automatic email signatures."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Email Routing Fields: To, Cc, and Bcc",
                    "content": {
                        "term": "To, Cc (Carbon Copy), and Bcc (Blind Carbon Copy)",
                        "definition": "The standard routing header fields defined in RFC 5322 that govern message distribution and recipient visibility.",
                        "simple_explanation": "'To' is for the person who must reply. 'Cc' is for people who just need to see the message. 'Bcc' is for secretly copying someone without anyone else knowing.",
                        "technical_meaning": "'To' and 'Cc' headers are transmitted in plain text in the message envelope. The 'Bcc' header is processed by the sending SMTP server to route copies, then stripped from the delivered message header to maintain confidentiality.",
                        "example": "Sending a budget report To: Treasurer, Cc: Teacher Patron, Bcc: School Principal."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Automated Inbox Filters and Signatures",
                    "content": {
                        "term": "Email Filters & Automated Signatures",
                        "definition": "Email filters are server-side or client-side rules that automatically categorize, label, forward, or archive incoming emails based on criteria. An email signature is a standardized block of identity text appended to the bottom of all outgoing correspondence.",
                        "simple_explanation": "Filters are automatic sorters that put emails into colored folders without you touching them. A signature is your automatic digital business card at the bottom of every email.",
                        "technical_meaning": "Rule engines executing pattern-matching algorithms against incoming MIME headers and appending configured HTML/text signature footers to outgoing payloads.",
                        "example": "A filter that automatically tags any email from `teacher@school.ac.ke` with the label `ICT_Class` and marks it as important."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Structural Anatomy of a Professional Email",
                    "content": {
                        "text": "A professional formal email consists of six mandatory components:\n\n1. **Subject Line:** Concise, actionable, and specific (e.g., `Grade 10 ICT Project Submission - Jane Doe`). Never leave this blank or write vague words like `Hey` or `Important`.\n2. **Formal Salutation (Greeting):** Professional opening address (e.g., `Dear Mrs. Wanjiku,` or `Dear Dr. Kamau,`). Avoid overly casual greetings like `Hey dude`.\n3. **Opening & Purpose Statement:** A direct first sentence stating who you are and why you are writing (e.g., `I am writing to submit my completed research report on renewable energy`).\n4. **Body Paragraphs:** Concise, structured text broken into short paragraphs with double returns for visual readability.\n5. **MIME Attachments:** Appropriately named files (e.g., `jane_doe_topic8_report.pdf`), formatted in standard cross-platform types (PDF/DOCX) within the 25MB limit.\n6. **Professional Sign-Off & Signature:** A formal closing (e.g., `Kind regards,` or `Sincerely,`) followed by your full name, student ID, and school."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "RFC 5322 Email Routing & Message Envelope Architecture",
                    "content": {
                        "title": "Anatomy of Email Headers and SMTP/IMAP Transmission",
                        "caption": "Architectural breakdown illustrating To, Cc, Bcc routing visibility, message envelope structure, and the 5-step SMTP to IMAP transmission pipeline.",
                        "svg_content": SVG_EMAIL_HEADER_ROUTING_STRUCTURE
                    }
                },
                {
                    "type": "step_process",
                    "title": "Composing, Attaching, and Dispatching a Formal Email",
                    "content": {
                        "intro": "Follow this step-by-step procedure to submit an assignment or professional inquiry via email:",
                        "steps": [
                            {
                                "title": "Step 1: Open New Compose Window",
                                "description": "Click **Compose** or **New Message** in your email dashboard (Gmail, Outlook, etc.)."
                            },
                            {
                                "title": "Step 2: Enter Recipient Addresses (To, Cc, Bcc)",
                                "description": "Type the primary recipient's address in **To**. If stakeholders need informational copies, add them to **Cc**. If sending to a large mailing list where addresses must remain private, use **Bcc**."
                            },
                            {
                                "title": "Step 3: Craft a Descriptive Subject Line",
                                "description": "Type a structured subject line following the convention: `[Topic/Course] - [Subject Purpose] - [Your Name]`."
                            },
                            {
                                "title": "Step 4: Draft Salutation and Body Text",
                                "description": "Type a polite greeting, state your purpose concisely, format paragraphs cleanly, and close with a polite sign-off."
                            },
                            {
                                "title": "Step 5: Attach and Verify Files (MIME)",
                                "description": "Click the paperclip icon (**Attach files**). Select your document (prefer PDF format), wait for the upload progress bar to finish, and check file size limits."
                            },
                            {
                                "title": "Step 6: Proofread, Send, and Verify",
                                "description": "Check for typos and verified recipient addresses. Click **Send**, then check your **Sent** folder to confirm the message left the outbox."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Routing Scenario: Club Budget Approval Proposal",
                    "content": {
                        "intro": "Jane Doe is the Environmental Club Chairperson. She needs to send a proposal. Let us configure the routing fields correctly:",
                        "steps": [
                            "**To: `treasurer@school.ac.ke`** — The treasurer must review the figures and calculate allocations (Primary action required).",
                            "**Cc: `patron.teacher@school.ac.ke`** — The teacher patron needs to stay informed of club correspondence (Public visibility).",
                            "**Bcc: `principal@school.ac.ke`** — The school principal requested a confidential copy without alerting the treasurer (Confidential visibility).",
                            "**Subject:** `Environmental Club 2026 Budget Proposal - Jane Doe`",
                            "**Attachment:** `env_club_budget_draft.pdf` (Clean, standardized file naming)."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Automating 50+ Daily Emails with Inbox Filters and Labels",
                    "content": {
                        "title": "Zero-Inbox Management for High School Students",
                        "text": "A student receiving dozens of daily emails from various teachers sets up automated Gmail filters. Emails containing the keyword 'Assignment' from `@school.ac.ke` are automatically tagged with a yellow `Assignments` label and starred. Newsletters are automatically routed into a `Reading_List` folder, bypassing the primary inbox. This automated workflow saves 30 minutes daily and guarantees no critical deadline is missed."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Bcc Recipients Can Reply to Everyone Anonymously",
                    "content": {
                        "misconception": "Many users think that if they are BCC'd on an email and click 'Reply All', they remain completely anonymous.",
                        "reality": "If a BCC recipient clicks 'Reply All', their email address is immediately revealed in the reply header to all original recipients, blowing their confidential status."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Hitting 'Reply All' on Large Broadcast Announcements",
                    "content": {
                        "mistake": "Replying 'Thank you!' or 'Noted' using 'Reply All' on an announcement sent to 500 students and staff.",
                        "correction": "Always click 'Reply' (single sender) unless every single person on the thread genuinely requires your specific response.",
                        "reasoning": "Hitting Reply All on mass emails floods hundreds of inboxes with unnecessary clutter, wasting server bandwidth and human attention."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Email Routing Fields",
                    "content": {
                        "question": "You are sending a newsletter to 200 parents. To protect their privacy and prevent parents from seeing each other's email addresses, which addressing field must you use?",
                        "options": [
                            "A. Put all 200 addresses in the 'To' field.",
                            "B. Put all 200 addresses in the 'Cc' field.",
                            "C. Put all 200 addresses in the 'Bcc' field.",
                            "D. Put all 200 addresses in the Subject line."
                        ],
                        "correct": "C",
                        "explanation": "The Bcc (Blind Carbon Copy) field hides all recipient addresses from one another, preventing unauthorized disclosure of private contact information when emailing large groups."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Automated Inbox Filters",
                    "content": {
                        "question": "Which email feature allows you to automatically apply a label and move all incoming messages from your ICT teacher into a dedicated folder without manual sorting?",
                        "options": [
                            "A. An automated Inbox Filter/Rule.",
                            "B. An outgoing email signature.",
                            "C. Changing your account profile picture.",
                            "D. Deleting your outbox cache."
                        ],
                        "correct": "A",
                        "explanation": "Automated Filters (or Rules) execute predefined actions (such as labeling, starring, or moving to folders) on incoming messages matching specific criteria (like sender address or keywords)."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Mastering Professional Email and Inbox Automation",
                    "content": {
                        "title": "Email Etiquette, Routing Headers, and Inbox Filters",
                        "youtube_id": "V4mP_4YQ24w",
                        "url": "https://www.youtube.com/watch?v=V4mP_4YQ24w",
                        "description": "A comprehensive guide to professional email formatting, distinguishing To, Cc, and Bcc routing, and automating inbox workflows with labels, filters, and digital signatures."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 5 Key Takeaways",
                    "content": {
                        "text": "- **Routing Header Roles:** 'To' is for action recipients; 'Cc' is for public informational copies; 'Bcc' is for hidden confidentiality and mass privacy protection.\n- **Six Elements of Formal Email:** Descriptive subject line, polite greeting, clear opening purpose, concise body paragraphs, verified attachments, and professional signature.\n- **Attachment Limits:** Keep files within standard 25MB limits and use universally readable formats like PDF.\n- **Inbox Automation:** Use folders/labels to categorize messages and automated filter rules to organize incoming emails automatically.\n- **Reply vs Reply All:** Never hit 'Reply All' on mass announcements to avoid flooding hundreds of inboxes with clutter."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8.1.6: Ethical Issues in Digital Communication
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Ethical Issues in Digital Communication",
        "unit_description": "Digital ethics, netiquette principles, cyberbullying prevention, phishing and social engineering defenses, intellectual property/copyright, and digital footprint management.",
        "lesson_title": "Ethical Issues in Digital Communication",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Cyber Ethics, Safety, and Digital Citizenship",
                    "content": {
                        "title": "Students Practicing Safe and Ethical Digital Communication",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Computer_classroom_in_Kenya.jpg",
                        "caption": "Students collaborating responsibly online, adhering to digital ethics, cyber safety protocols, and respectful netiquette standards.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Being a Responsible Digital Citizen",
                    "content": {
                        "text": "The internet connects billions of human beings across the planet. However, because we interact through computer screens rather than face-to-face, people sometimes forget that their words and actions have real emotional, legal, and professional consequences.\n\n**Digital Ethics** and **Netiquette** (network etiquette) govern how we behave in cyber spaces. From preventing cyberbullying and recognizing sophisticated phishing scams to managing your permanent digital footprint and respecting copyright laws, acting ethically online is just as important as being a law-abiding citizen in the physical world."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define Netiquette and apply core rules of professional and empathetic online behavior.\n- Recognize and defend against cyberbullying, online harassment, phishing scams, and social engineering attacks.\n- Analyze the permanent nature of a Digital Footprint and its long-term impact on university admissions and career prospects.\n- Apply copyright laws, Creative Commons licensing, and academic citation standards to avoid plagiarism."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Netiquette and Tone in Cyber Spaces",
                    "content": {
                        "term": "Netiquette (Network Etiquette)",
                        "definition": "The customary code of polite, ethical, and respectful behavior practiced by users when communicating on online platforms, forums, and networks.",
                        "simple_explanation": "Good manners and respect for others when talking, posting, or emailing on the internet.",
                        "technical_meaning": "The established cultural and procedural norms governing written typography (e.g., avoiding all-caps shouting), conflict resolution, data privacy, and conversational etiquette in networked environments.",
                        "example": "Refraining from typing angry messages in ALL CAPS and addressing peers politely in class discussion forums."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Phishing and Social Engineering",
                    "content": {
                        "term": "Phishing & Social Engineering",
                        "definition": "A fraudulent cybercrime where attackers deceive users into revealing sensitive credentials, passwords, or financial data by masquerading as a trustworthy entity.",
                        "simple_explanation": "Fake emails or messages designed to trick you into clicking a malicious link or giving away your password.",
                        "technical_meaning": "Deceptive electronic communications utilizing spoofed SMTP sender headers, homograph domain lookups, and artificial urgency heuristics to extract cryptographic credentials or install malware payloads.",
                        "example": "An email claiming to be from 'Google Security' with the address `security@gmai1-support.com` asking you to verify your password immediately."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Pillars of Ethical Digital Communication",
                    "content": {
                        "text": "Ethical digital communication is anchored upon four core pillars:\n\n1. **Netiquette & Professional Tone:** Avoid typing in ALL CAPS (perceived as yelling). Use constructive language, respect cultural differences, and practice the golden rule: if you would not say it to someone's face, never type it online.\n2. **Cybersecurity & Phishing Awareness:** Scrutinize incoming emails for spoofed sender domains, suspicious attachments, and false urgency. Never disclose passwords or 2FA codes.\n3. **Digital Footprint & Data Permanence:** Remember that anything posted online—including deleted posts and private group chats—can be screenshotted and archived permanently on remote servers. Maintain a clean digital reputation.\n4. **Intellectual Property & Academic Integrity:** Always attribute sources when quoting articles or using online graphics. Respect Creative Commons licenses and avoid plagiarism."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Pillars of Digital Ethics and Online Safety",
                    "content": {
                        "title": "Framework for Responsible Digital Citizenship",
                        "caption": "Architectural grid outlining Netiquette, Phishing Defense, Digital Footprint Management, and Intellectual Property Compliance.",
                        "svg_content": SVG_DIGITAL_ETHICS_NETIQUETTE
                    }
                },
                {
                    "type": "step_process",
                    "title": "The STOP & VERIFY Protocol for Suspected Scams or Harassment",
                    "content": {
                        "intro": "When encountering a suspicious message, phishing attempt, or cyberbullying incident, execute this 4-step protocol:",
                        "steps": [
                            {
                                "title": "1. STOP: Do Not React Emotionally or Click Links",
                                "description": "Pause immediately. Do not click any embedded hyperlinks, do not download file attachments, and do not reply with angry words that escalate conflict."
                            },
                            {
                                "title": "2. INSPECT: Check the Technical Headers and Sender Domain",
                                "description": "Look at the actual email address behind the sender name. Check for subtle misspellings (e.g., `@kcb-bank-alerts.com` instead of `@kcbgroup.com`). Check for artificial urgency triggers."
                            },
                            {
                                "title": "3. DOCUMENT: Capture Unalterable Evidence",
                                "description": "Take clear screenshots showing the date, timestamp, sender address, and message content. In harassment cases, preserve the evidence before blocking the user."
                            },
                            {
                                "title": "4. REPORT: Notify Administrators and Block the Threat",
                                "description": "Flag the email as Phishing in your mail client. In cases of cyberbullying or financial extortion, report the incident to school authorities or the National CERT (Kenya Cybersecurity Emergency Response Team)."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Dissecting a Real-World Phishing Email Attempt",
                    "content": {
                        "intro": "Let us analyze a fraudulent email received by a high school student and identify the 4 red flags:",
                        "steps": [
                            "**Red Flag 1: Spoofed Sender Address:** Display name says 'Google Security Team', but the actual address is `alert-admin@google-security-verify2026.net` (Fake domain).",
                            "**Red Flag 2: Artificial Panic / Urgency:** Message states: 'WARNING: Your Google account will be permanently deleted in 15 minutes unless you verify your password!'",
                            "**Red Flag 3: Generic Salutation:** Begins with 'Dear Valued Customer' instead of the student's actual name.",
                            "**Red Flag 4: Deceptive Hyperlink Target:** The button text says 'Verify Password', but hovering over it reveals a malicious URL: `http://192.168.4.12/steal-login.php`."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Legal Accountability: The Kenya Computer Misuse and Cybercrimes Act",
                    "content": {
                        "title": "Legal Consequences of Online Harassment and Defamation",
                        "text": "Under Kenya's Computer Misuse and Cybercrimes Act (2018), cyber harassment, sharing non-consensual private images, cyberstalking, and publishing false information intended to ruin a person's reputation are criminal offenses punishable by heavy fines and imprisonment. Digital anonymity is a myth; law enforcement agencies and cyber forensic investigators trace IP addresses and digital footprints back to individual devices."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Content Posted in 'Disappearing' Stories or Private Chats is Completely Gone",
                    "content": {
                        "misconception": "Many teenagers believe that sending hurtful comments or private photos on platforms with 24-hour disappearing timers leaves zero trace.",
                        "reality": "Any recipient can easily take a screenshot, record the screen with another device, or retrieve cached files. Furthermore, server databases retain logs of message transmissions long after deletion."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Copying Text from Wikipedia into an Assignment Without Attribution",
                    "content": {
                        "mistake": "Copying paragraphs from web articles or AI chatbots directly into a school paper without quoting or citing the source.",
                        "correction": "Always paraphrase in your own words and provide full citations (Author, Title, Year, URL) using formal referencing styles.",
                        "reasoning": "Submitting uncredited work is plagiarism, which violates intellectual property ethics and leads to automatic academic penalties."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Phishing Scams",
                    "content": {
                        "question": "Which of the following is the most reliable warning sign that an incoming email is a fraudulent phishing attempt?",
                        "options": [
                            "A. The email contains a formal greeting and your exact student ID number.",
                            "B. The sender address uses a slightly misspelled domain (e.g. `support@gmai1.com`) and creates artificial panic demanding immediate password verification.",
                            "C. The email comes from your verified school domain `@school.ac.ke`.",
                            "D. The email includes a link to an official government portal `https://ecitizen.go.ke`."
                        ],
                        "correct": "B",
                        "explanation": "Phishing emails frequently use spoofed lookalike domains (e.g., replacing 'l' with '1') and use artificial panic/urgency threats to pressure victims into giving up credentials."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Netiquette Best Practices",
                    "content": {
                        "question": "In digital communication netiquette, why is it strongly recommended to avoid typing entire messages in ALL CAPITAL LETTERS?",
                        "options": [
                            "A. Because uppercase text uses double the internet bandwidth.",
                            "B. Because typing in ALL CAPS is widely interpreted as aggressive shouting and is difficult to read.",
                            "C. Because computers automatically delete messages written in uppercase.",
                            "D. Because screen readers cannot pronounce uppercase letters."
                        ],
                        "correct": "B",
                        "explanation": "In internet netiquette, typing in ALL CAPS is universally perceived as shouting or anger, and the lack of variable character height makes it harder for the human eye to scan comfortably."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Digital Citizenship, Netiquette, and Cyber Ethics",
                    "content": {
                        "title": "Cyber Safety, Netiquette, and Protecting Your Digital Footprint",
                        "youtube_id": "y_8N_a899jI",
                        "url": "https://www.youtube.com/watch?v=y_8N_a899jI",
                        "description": "An engaging guide to practicing ethical netiquette, identifying phishing traps, respecting copyright laws, and building a positive, permanent digital reputation."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 6 Key Takeaways",
                    "content": {
                        "text": "- **Netiquette Rules:** Treat online humans with empathy and respect; avoid aggressive ALL CAPS shouting and emotional flame wars.\n- **Phishing Defense:** Scrutinize sender domains, ignore artificial panic triggers, and never disclose passwords or verification codes.\n- **Digital Footprint:** Digital records and screenshots are permanent; maintain a clean, professional online presence for future career and academic success.\n- **Legal Frameworks:** Cyberbullying, harassment, and identity theft are punishable under Kenya's Computer Misuse and Cybercrimes Act (2018).\n- **Intellectual Property:** Always attribute sources and respect copyright to avoid plagiarism and uphold academic integrity."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8.1.7: Cloud Collaboration and AI in Digital Communication
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Cloud Collaboration and AI in Digital Communication",
        "unit_description": "Cloud storage sharing tiers (Viewer, Commenter, Editor), concurrent document co-authoring, visual Kanban project boards (Trello), streaming media podcasts, and AI-driven communication automations.",
        "lesson_title": "Cloud Collaboration and AI in Digital Communication",
        "pages": [
            # Page 1: Visual Hook & Learning Outcomes
            [
                {
                    "type": "suggested_image",
                    "title": "Cloud Collaboration and AI-Powered Workspace",
                    "content": {
                        "title": "Team Collaborating in Real Time Using Cloud Software and AI Tools",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Desktop_publishing_workspace.jpg",
                        "caption": "A modern digital team workspace utilizing cloud storage drives, concurrent document editing, Kanban task boards, and AI productivity tools.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Modern Connected Workspace",
                    "content": {
                        "text": "Imagine working on a group presentation with three classmates. In the past, you would type your section on a computer, save it to a physical USB drive, walk to your friend's house, wait for them to copy it, and manually merge drafts. This led to lost files and conflicting versions.\n\nToday, **Cloud Collaboration** allows entire teams to co-author live documents simultaneously from different locations. Combined with visual project management boards (Kanban), streaming audio podcasts, and **Artificial Intelligence (AI)** tools that automate live captions and clean audio, modern digital collaboration has transformed how humans work, learn, and create together."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Configure cloud storage sharing permissions across the 3 access tiers: Viewer (read-only), Commenter (suggest only), and Editor (full modify rights).\n- Execute real-time concurrent document co-authoring using colored cursors, inline comments, and Version History restoration.\n- Manage team workflows using visual Kanban project boards (To Do, In Progress, Completed).\n- Produce and publish educational audio podcasts and analyze the transformative impact of AI on digital communication platforms."
                    }
                }
            ],

            # Page 2: Core Concept Explanation & Key Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Cloud Collaboration and Concurrent Editing",
                    "content": {
                        "term": "Cloud Collaboration & Concurrent Co-Authoring",
                        "definition": "The practice of using internet-hosted cloud platforms to store, share, and simultaneously edit digital files in real time across multiple computing endpoints.",
                        "simple_explanation": "Multiple people writing and editing the exact same online document at the same time without overwriting each other's work.",
                        "technical_meaning": "Real-time document synchronization utilizing Operational Transformation (OT) or Conflict-free Replicated Data Types (CRDTs) over WebSockets to merge edits concurrently.",
                        "example": "Two students typing different paragraphs simultaneously inside a shared Google Doc."
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Kanban Management and AI Communication",
                    "content": {
                        "term": "Kanban Project Boards & AI Communication Engines",
                        "definition": "Kanban is a visual project management framework that tracks tasks across stage columns (To Do, In Progress, Done). AI communication engines utilize machine learning algorithms to automate transcription, translation, noise removal, and content recommendations.",
                        "simple_explanation": "Kanban is moving sticky cards across columns to track who is doing what. AI engines are smart algorithms that clean up audio, add subtitles, and suggest relevant videos.",
                        "technical_meaning": "Kanban models discrete workflow state transitions. AI tools utilize Natural Language Processing (NLP) models, Convolutional Neural Networks (CNNs) for audio filtering, and collaborative filtering algorithms for recommendation feeds.",
                        "example": "Dragging a 'Record Podcast Audio' card to 'Completed' on Trello while using an AI tool to remove background microphone noise."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Modern Digital Teamwork & AI Collaboration Stack",
                    "content": {
                        "text": "Modern digital projects rely on an integrated five-part technology stack:\n\n1. **Cloud Storage Drives (Google Drive, Dropbox, OneDrive):** Centralized cloud repositories that synchronize files across laptops and smartphones 24/7 with granular sharing permissions (Viewer, Commenter, Editor).\n2. **Concurrent Document Editors (Google Docs, Office 365, Zoho):** Real-time co-authoring tools featuring colored user cursors, inline feedback comments, and complete Version History rollback capabilities.\n3. **Visual Kanban Boards (Trello, Asana, Jira):** Visual card-based trackers organizing work across `To Do`, `In Progress`, and `Completed` columns with assigned deadlines and member tags.\n4. **Media Streaming & Podcasts:** Continuous audio/video packet delivery allowing instant on-demand playback without full-file download delays.\n5. **Artificial Intelligence Enhancements:** Machine learning models that generate live subtitles (Speech-to-Text), cancel background noise, translate languages in real time, and recommend tailored educational content."
                    }
                }
            ],

            # Page 3: Visual Enrichment Diagram & Procedures
            [
                {
                    "type": "suggested_diagram",
                    "title": "Cloud Collaboration & AI-Driven Media Pipeline",
                    "content": {
                        "title": "The 5-Component Cloud Collaboration and AI Pipeline",
                        "caption": "Comprehensive architectural flow from Cloud Storage and Concurrent Editing to Kanban Project Tracking, Media Podcasting, and AI Automations.",
                        "svg_content": SVG_CLOUD_COLLABORATION_AI_WORKFLOW
                    }
                },
                {
                    "type": "step_process",
                    "title": "End-to-End Workflow: Executing a Collaborative Team Project",
                    "content": {
                        "intro": "Follow this 4-phase workflow to execute a collaborative school or business project from concept to publication:",
                        "steps": [
                            {
                                "title": "Phase 1: Setup Cloud Resource Repository",
                                "description": "Create a new folder on Google Drive named `Team_Project_Resources`. Upload background research PDFs. Share with teammates, configuring access to **Viewer** for external readers or **Editor** for co-workers."
                            },
                            {
                                "title": "Phase 2: Real-Time Script Co-Authoring",
                                "description": "Launch a shared Google Doc named `Project_Script`. Co-author sections simultaneously. Use the **Add Comment** feature to suggest revisions and resolve peer feedback."
                            },
                            {
                                "title": "Phase 3: Visual Kanban Task Tracking",
                                "description": "Set up a Trello board with columns `To Do`, `In Progress`, and `Completed`. Create task cards (e.g., 'Record Audio', 'Edit Poster'), assign member names, and set due dates."
                            },
                            {
                                "title": "Phase 4: Podcast Recording & AI Enhancement",
                                "description": "Record a 2-minute audio episode in a quiet room following the script. Apply AI-based noise cancellation to remove microphone hum, export as MP3, and upload to the cloud repository."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Real-World Applications, Worked Examples, Troubleshooting & Misconceptions
            [
                {
                    "type": "worked_example",
                    "title": "Capstone Project: 'E-Waste Management Campaign in Kenya'",
                    "content": {
                        "intro": "Two students collaborate on a school environmental podcast campaign. Let us observe how they apply cloud tools and permissions:",
                        "steps": [
                            "**Step 1 (Google Drive Access Control):** Jane creates a cloud folder for reference PDFs on Kenyan e-waste recycling centers. She sets John's permission to **Editor** and the class link to **Viewer** so peers cannot accidentally delete sources.",
                            "**Step 2 (Google Docs Co-Writing):** Both students open the script document simultaneously. John types Section 1 on electronic hazards while Jane writes Section 2 on recycling drop-off points.",
                            "**Step 3 (Trello Task Tracking):** They create cards for 'Script Approval', 'Voice Recording', and 'Soundtrack Mixing'. As Jane records the voiceover, she moves the card to 'In Progress'.",
                            "**Step 4 (AI Podcast Production):** They record audio using a smartphone, run an AI background-noise filter to remove room echo, and upload the final 2-minute MP3 to their shared folder."
                        ]
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Global Open-Source Software Development and Remote Teams",
                    "content": {
                        "title": "How Distributed Engineering Teams Build Global Software",
                        "text": "Major software projects like the Linux kernel, Android OS, and Python are developed by thousands of programmers who never meet in person. They use cloud collaboration tools: GitHub for code version history, Slack/Discord for team communication, Trello/Jira for tracking software bug tickets, and AI code assistants to analyze performance and write automated tests."
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Granting 'Editor' Access to Everyone is the Best Way to Share Files",
                    "content": {
                        "misconception": "Many students generate a public share link with 'Editor' permissions and post it in large group chats so anyone can see it.",
                        "reality": "Giving full Editor access to a public link allows anyone with the URL to overwrite text, inject malicious content, or delete the entire folder. Always default to 'Viewer' permissions for general sharing."
                    }
                },
                {
                    "type": "common_mistake",
                    "title": "Common Mistake: Forgetting to Check Version History When Content is Accidentally Deleted",
                    "content": {
                        "mistake": "Panicking and re-typing an entire 5-page report after a teammate accidentally highlights and deletes a large section.",
                        "correction": "Click **File -> Version history -> See version history** in Google Docs, locate the timestamp before the deletion occurred, and click **Restore this version**.",
                        "reasoning": "Cloud collaboration suites continuously record immutable snapshots of all document changes, making recovery effortless."
                    }
                }
            ],

            # Page 5: Knowledge Checks, Video Resource & Lesson Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Cloud Storage Access Tiers",
                    "content": {
                        "question": "You have uploaded the final school exam timetable to Google Drive. You want all 300 students to download and read it, but you must guarantee that no student can alter or delete the schedule. Which permission level should you configure?",
                        "options": [
                            "A. Editor",
                            "B. Co-Owner",
                            "C. Viewer",
                            "D. System Administrator"
                        ],
                        "correct": "C",
                        "explanation": "The 'Viewer' access tier permits users to view and download files while strictly preventing them from making edits, renaming files, or deleting content from the shared folder."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Artificial Intelligence in Digital Media",
                    "content": {
                        "question": "Which of the following video streaming platform features is driven directly by Artificial Intelligence (AI) algorithms?",
                        "options": [
                            "A. The physical plastic power button on your monitor.",
                            "B. Automated real-time speech-to-text closed captioning and personalized sidebar content recommendations.",
                            "C. The HDMI cable connecting the computer to a screen.",
                            "D. The manual audio volume slider knob."
                        ],
                        "correct": "B",
                        "explanation": "Artificial Intelligence algorithms power automated speech-to-text transcription (for accessibility captions), natural language translation, and recommendation engines that analyze user viewing behavior."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Cloud Collaboration, Google Workspace, and AI Tools",
                    "content": {
                        "title": "Collaborating in the Cloud: Docs, Drive, Kanban, and AI",
                        "youtube_id": "P6FfE_T_H7o",
                        "url": "https://www.youtube.com/watch?v=P6FfE_T_H7o",
                        "description": "A comprehensive practical guide to cloud file permissions, real-time concurrent editing, visual Kanban project boards, and utilizing AI tools in team collaboration."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 7 Key Takeaways",
                    "content": {
                        "text": "- **Cloud Access Tiers:** Viewer (read-only safety), Commenter (suggest revisions only), and Editor (full modify and delete authority).\n- **Concurrent Co-Authoring:** Real-time editing with live colored cursors, inline comments, and instant Version History restoration.\n- **Visual Kanban Tracking:** Organizes project progress across To Do, In Progress, and Completed cards with assigned members and due dates.\n- **Podcast Production:** Follows a 3-step cycle (Pre-production script, Audio recording, Post-production editing/streaming).\n- **AI in Communication:** Drives real-time speech-to-text captions, automated noise cancellation, language translation, and personalized content recommendations."
                    }
                }
            ]
        ]
    }
]
