"""
VLearn CBC Grade 10 History — Topic 5: Elections in Kenya
High Precision Vector Visualizations and Infographics
"""

# =============================================================================
# SVG 1: IEBC Core Functions Wheel (Lesson 1)
# =============================================================================
SVG_IEBC_CORE_FUNCTIONS_WHEEL = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="590" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <!-- Header -->
  <text x="480" y="50" font-size="22" font-weight="bold" fill="#38bdf8" text-anchor="middle">IEBC Constitutional Mandate &amp; Core Functions</text>
  <text x="480" y="74" font-size="13" fill="#94a3b8" text-anchor="middle">Article 88 of the Constitution of Kenya (2010) — Managing Free, Fair &amp; Verifiable Elections</text>

  <!-- Central Hub: IEBC -->
  <circle cx="480" cy="330" r="85" fill="#0f172a" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="480" cy="330" r="75" fill="#1e293b"/>
  <text x="480" y="318" font-size="20" font-weight="900" fill="#38bdf8" text-anchor="middle">IEBC</text>
  <text x="480" y="338" font-size="10.5" font-weight="bold" fill="#f8fafc" text-anchor="middle">ELECTORAL &amp; BOUNDARIES</text>
  <text x="480" y="354" font-size="9.5" fill="#94a3b8" text-anchor="middle">Article 88 Mandate</text>

  <!-- Connecting Rays / Spokes -->
  <line x1="480" y1="245" x2="480" y2="185" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4 4"/>
  <line x1="555" y1="285" x2="690" y2="205" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 4"/>
  <line x1="555" y1="375" x2="690" y2="455" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4 4"/>
  <line x1="480" y1="415" x2="480" y2="480" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 4"/>
  <line x1="405" y1="375" x2="270" y2="455" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="4 4"/>
  <line x1="405" y1="285" x2="270" y2="205" stroke="#06b6d4" stroke-width="2.5" stroke-dasharray="4 4"/>

  <!-- Sector 1: Top (Voter Registration) -->
  <g transform="translate(480, 130)">
    <rect x="-135" y="-45" width="270" height="90" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="-105" cy="0" r="18" fill="#0284c7"/>
    <text x="-105" y="6" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="15" y="-12" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">VOTER REGISTRATION</text>
    <text x="15" y="8" font-size="10" fill="#cbd5e1" text-anchor="middle">Continuous Biometric Registration (BVR)</text>
    <text x="15" y="24" font-size="9" fill="#94a3b8" text-anchor="middle">Maintains &amp; verifies National Voters Register</text>
  </g>

  <!-- Sector 2: Top-Right (Boundary Delimitation) -->
  <g transform="translate(740, 205)">
    <rect x="-130" y="-45" width="260" height="90" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <circle cx="-100" cy="0" r="18" fill="#059669"/>
    <text x="-100" y="6" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="15" y="-12" font-size="12.5" font-weight="bold" fill="#34d399" text-anchor="middle">BOUNDARY DELIMITATION</text>
    <text x="15" y="8" font-size="10" fill="#cbd5e1" text-anchor="middle">Constituencies &amp; County Wards</text>
    <text x="15" y="24" font-size="9" fill="#94a3b8" text-anchor="middle">Reviews borders based on population parity</text>
  </g>

  <!-- Sector 3: Bottom-Right (Election Supervision) -->
  <g transform="translate(740, 455)">
    <rect x="-130" y="-45" width="260" height="90" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="-100" cy="0" r="18" fill="#d97706"/>
    <text x="-100" y="6" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="15" y="-12" font-size="12.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">ELECTION SUPERVISION</text>
    <text x="15" y="8" font-size="10" fill="#cbd5e1" text-anchor="middle">Administering Polls &amp; Referenda</text>
    <text x="15" y="24" font-size="9" fill="#94a3b8" text-anchor="middle">Presidential, Parliamentary &amp; County races</text>
  </g>

  <!-- Sector 4: Bottom (Results Verification) -->
  <g transform="translate(480, 530)">
    <rect x="-135" y="-45" width="270" height="90" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <circle cx="-105" cy="0" r="18" fill="#dc2626"/>
    <text x="-105" y="6" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="15" y="-12" font-size="13" font-weight="bold" fill="#f87171" text-anchor="middle">RESULTS VERIFICATION</text>
    <text x="15" y="8" font-size="10" fill="#cbd5e1" text-anchor="middle">Form 34A Digital Transmission</text>
    <text x="15" y="24" font-size="9" fill="#94a3b8" text-anchor="middle">Tallying, public portal &amp; official declarations</text>
  </g>

  <!-- Sector 5: Bottom-Left (Campaign Finance Regulation) -->
  <g transform="translate(220, 455)">
    <rect x="-130" y="-45" width="260" height="90" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <circle cx="-100" cy="0" r="18" fill="#7e22ce"/>
    <text x="-100" y="6" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="15" y="-12" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">CAMPAIGN FINANCE REGULATION</text>
    <text x="15" y="8" font-size="10" fill="#cbd5e1" text-anchor="middle">Spending Limits &amp; Disclosure</text>
    <text x="15" y="24" font-size="9" fill="#94a3b8" text-anchor="middle">Prevents corrupt influence &amp; vote buying</text>
  </g>

  <!-- Sector 6: Top-Left (Voter Education) -->
  <g transform="translate(220, 205)">
    <rect x="-130" y="-45" width="260" height="90" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <circle cx="-100" cy="0" r="18" fill="#0891b2"/>
    <text x="-100" y="6" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">6</text>
    <text x="15" y="-12" font-size="13" font-weight="bold" fill="#22d3ee" text-anchor="middle">VOTER EDUCATION</text>
    <text x="15" y="8" font-size="10" fill="#cbd5e1" text-anchor="middle">Civic Rights &amp; Voting Literacy</text>
    <text x="15" y="24" font-size="9" fill="#94a3b8" text-anchor="middle">Educates public on peace, laws &amp; ballot use</text>
  </g>
</svg>
""".strip()


# =============================================================================
# SVG 2: The Democratic Accountability Cycle (Lesson 2)
# =============================================================================
SVG_DEMOCRATIC_ACCOUNTABILITY_CYCLE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 580" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="550" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="48" font-size="22" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Democratic Accountability Cycle in Kenya</text>
  <text x="480" y="72" font-size="13" fill="#94a3b8" text-anchor="middle">How Sovereign Power (Article 1) is Exercised, Monitored, and Renewed</text>

  <!-- Cycle Node 1: Citizens Sovereign Power (Top Center) -->
  <g transform="translate(480, 130)">
    <rect x="-150" y="-35" width="300" height="70" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="-8" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. CITIZENS' SOVEREIGN POWER</text>
    <text x="0" y="12" font-size="10.5" fill="#f8fafc" text-anchor="middle">Article 1: All sovereign power belongs to the people</text>
    <text x="0" y="26" font-size="9" fill="#94a3b8" text-anchor="middle">Exercised directly or through elected representatives</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 640 135 C 760 145, 800 200, 780 255" fill="none" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-cyan)"/>

  <!-- Cycle Node 2: Periodic Elections (Right) -->
  <g transform="translate(760, 310)">
    <rect x="-140" y="-35" width="280" height="70" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="0" y="-8" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">2. REGULAR FREE &amp; FAIR ELECTIONS</text>
    <text x="0" y="12" font-size="10.5" fill="#f8fafc" text-anchor="middle">Article 38 &amp; 81: Universal Adult Suffrage</text>
    <text x="0" y="26" font-size="9" fill="#94a3b8" text-anchor="middle">Secret ballot, multi-party competition every 5 years</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 740 365 C 720 420, 660 470, 590 485" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>

  <!-- Cycle Node 3: Governance & Representation (Bottom-Center Right) -->
  <g transform="translate(480, 500)">
    <rect x="-150" y="-35" width="300" height="70" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="0" y="-8" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. DEMOCRATIC GOVERNANCE &amp; POLICY</text>
    <text x="0" y="12" font-size="10.5" fill="#f8fafc" text-anchor="middle">Executive &amp; Parliament Enact Legislation</text>
    <text x="0" y="26" font-size="9" fill="#94a3b8" text-anchor="middle">Resource allocation, public services &amp; county devolution</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 370 485 C 300 470, 240 420, 220 365" fill="none" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow-amber)"/>

  <!-- Cycle Node 4: Citizen Evaluation & Feedback (Left) -->
  <g transform="translate(200, 310)">
    <rect x="-140" y="-35" width="280" height="70" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="0" y="-8" font-size="13" font-weight="bold" fill="#c084fc" text-anchor="middle">4. CITIZEN SCRUTINY &amp; PERFORMANCE REVIEW</text>
    <text x="0" y="12" font-size="10.5" fill="#f8fafc" text-anchor="middle">Public Participation &amp; Social Audit</text>
    <text x="0" y="26" font-size="9" fill="#94a3b8" text-anchor="middle">Rewarding deliverers or voting out non-performers</text>
  </g>

  <!-- Arrow 4 -> 1 -->
  <path d="M 180 255 C 160 200, 200 145, 320 135" fill="none" stroke="#a855f7" stroke-width="2.5" marker-end="url(#arrow-purple)"/>

  <!-- Center Core Box: The Check & Balance Engine -->
  <g transform="translate(480, 310)">
    <circle cx="0" cy="0" r="65" fill="#0f172a" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="0" y="-12" font-size="11" font-weight="bold" fill="#e2e8f0" text-anchor="middle">PEACEFUL</text>
    <text x="0" y="4" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">TRANSITION</text>
    <text x="0" y="20" font-size="9" fill="#94a3b8" text-anchor="middle">OF POWER</text>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrow-cyan" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981"/>
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#a855f7"/>
    </marker>
  </defs>
</svg>
""".strip()


# =============================================================================
# SVG 3: The Core Values of Electoral Integrity Star (Lesson 3)
# =============================================================================
SVG_CORE_VALUES_INTEGRITY_STAR = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="590" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="48" font-size="22" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5 Core Values of Electoral Integrity</text>
  <text x="480" y="72" font-size="13" fill="#94a3b8" text-anchor="middle">Cultivating Civic Character to Prevent Electoral Malpractice and Safeguard Democracy</text>

  <!-- Central Hub -->
  <circle cx="480" cy="330" r="75" fill="#0f172a" stroke="#e2e8f0" stroke-width="3"/>
  <circle cx="480" cy="330" r="65" fill="#1e293b"/>
  <text x="480" y="322" font-size="13" font-weight="bold" fill="#f8fafc" text-anchor="middle">CONSTITUTIONAL</text>
  <text x="480" y="338" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">INTEGRITY</text>
  <text x="480" y="354" font-size="9" fill="#94a3b8" text-anchor="middle">Article 81 Principles</text>

  <!-- Value 1: Top Point - INTEGRITY / HONESTY -->
  <line x1="480" y1="255" x2="480" y2="185" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(480, 135)">
    <rect x="-130" y="-40" width="260" height="80" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="-12" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. INTEGRITY (Honesty)</text>
    <text x="0" y="8" font-size="10" fill="#f8fafc" text-anchor="middle">Rejecting bribery &amp; unethical tactics</text>
    <text x="0" y="24" font-size="8.5" fill="#94a3b8" text-anchor="middle">Doing right even when unmonitored</text>
  </g>

  <!-- Value 2: Top Right Point - TRANSPARENCY -->
  <line x1="545" y1="290" x2="680" y2="225" stroke="#10b981" stroke-width="2"/>
  <g transform="translate(730, 215)">
    <rect x="-125" y="-40" width="250" height="80" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="0" y="-12" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">2. TRANSPARENCY (Openness)</text>
    <text x="0" y="8" font-size="10" fill="#f8fafc" text-anchor="middle">Verifiable tallying &amp; public portals</text>
    <text x="0" y="24" font-size="8.5" fill="#94a3b8" text-anchor="middle">Full access for observers &amp; party agents</text>
  </g>

  <!-- Value 3: Bottom Right Point - FAIRNESS -->
  <line x1="535" y1="380" x2="650" y2="470" stroke="#f59e0b" stroke-width="2"/>
  <g transform="translate(700, 500)">
    <rect x="-125" y="-40" width="250" height="80" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="0" y="-12" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. FAIRNESS (Justice)</text>
    <text x="0" y="8" font-size="10" fill="#f8fafc" text-anchor="middle">Equal campaign ground for all candidates</text>
    <text x="0" y="24" font-size="8.5" fill="#94a3b8" text-anchor="middle">Impartial security &amp; media coverage</text>
  </g>

  <!-- Value 4: Bottom Left Point - TOLERANCE -->
  <line x1="425" y1="380" x2="310" y2="470" stroke="#ef4444" stroke-width="2"/>
  <g transform="translate(260, 500)">
    <rect x="-125" y="-40" width="250" height="80" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <text x="0" y="-12" font-size="13" font-weight="bold" fill="#f87171" text-anchor="middle">4. TOLERANCE (Peace)</text>
    <text x="0" y="8" font-size="10" fill="#f8fafc" text-anchor="middle">Opponents are competitors, not enemies</text>
    <text x="0" y="24" font-size="8.5" fill="#94a3b8" text-anchor="middle">Zero tolerance for ethnic incitement</text>
  </g>

  <!-- Value 5: Top Left Point - CIVIC RESPONSIBILITY -->
  <line x1="415" y1="290" x2="280" y2="225" stroke="#a855f7" stroke-width="2"/>
  <g transform="translate(230, 215)">
    <rect x="-125" y="-40" width="250" height="80" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="0" y="-12" font-size="13" font-weight="bold" fill="#c084fc" text-anchor="middle">5. CIVIC DUTY (Responsibility)</text>
    <text x="0" y="8" font-size="10" fill="#f8fafc" text-anchor="middle">Informed voting &amp; protecting the peace</text>
    <text x="0" y="24" font-size="8.5" fill="#94a3b8" text-anchor="middle">Reporting malpractices to authorities</text>
  </g>
</svg>
""".strip()


# =============================================================================
# SVG 4: Election Peace Simulation & Dispute Resolution Map (Lesson 4)
# =============================================================================
SVG_ELECTION_PEACE_SIMULATION_MAP = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="530" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="46" font-size="21" font-weight="bold" fill="#38bdf8" text-anchor="middle">Amani County Election Simulation Arena</text>
  <text x="480" y="70" font-size="12.5" fill="#94a3b8" text-anchor="middle">Multi-Stakeholder Crisis Resolution &amp; Constitutional De-escalation Protocol</text>

  <!-- Four Stakeholder Pillars -->
  <!-- Pillar 1: Returning Officer (IEBC) -->
  <g transform="translate(145, 110)">
    <rect x="-85" y="0" width="170" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="-85" y="0" width="170" height="24" rx="8" fill="#0284c7"/>
    <text x="0" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">RETURNING OFFICER</text>
    <text x="0" y="42" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">IEBC Constitutional Role</text>
    <text x="0" y="58" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Verifies Form 34A</text>
    <text x="0" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Follows Elections Act</text>
    <text x="0" y="86" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Maintains neutrality</text>
  </g>

  <!-- Pillar 2: Party Agents (Candidates A & B) -->
  <g transform="translate(365, 110)">
    <rect x="-85" y="0" width="170" height="110" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="-85" y="0" width="170" height="24" rx="8" fill="#d97706"/>
    <text x="0" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PARTY AGENTS</text>
    <text x="0" y="42" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Candidate A &amp; B Teams</text>
    <text x="0" y="58" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Scrutinize tallying</text>
    <text x="0" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Audit ballot seals</text>
    <text x="0" y="86" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Calm supporters</text>
  </g>

  <!-- Pillar 3: Peace Monitors & Elders -->
  <g transform="translate(595, 110)">
    <rect x="-85" y="0" width="170" height="110" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="-85" y="0" width="170" height="24" rx="8" fill="#059669"/>
    <text x="0" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">NCIC &amp; PEACE MONITORS</text>
    <text x="0" y="42" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Community Observers</text>
    <text x="0" y="58" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Fact-check rumors</text>
    <text x="0" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Facilitate dialogue</text>
    <text x="0" y="86" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Moral arbitration</text>
  </g>

  <!-- Pillar 4: Police & Security -->
  <g transform="translate(815, 110)">
    <rect x="-85" y="0" width="170" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="-85" y="0" width="170" height="24" rx="8" fill="#7e22ce"/>
    <text x="0" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">SECURITY COMMAND</text>
    <text x="0" y="42" font-size="9" font-weight="bold" fill="#c084fc" text-anchor="middle">National Police Service</text>
    <text x="0" y="58" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Secures tally center</text>
    <text x="0" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Uses proportional force</text>
    <text x="0" y="86" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Protects ballot assets</text>
  </g>

  <!-- Crisis Center Box (Middle) -->
  <g transform="translate(480, 255)">
    <rect x="-380" y="0" width="760" height="75" rx="10" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
    <text x="0" y="24" font-size="13" font-weight="bold" fill="#fecaca" text-anchor="middle">CRITICAL INCIDENT AT POLLING STATION 03</text>
    <text x="0" y="44" font-size="10.5" fill="#ffffff" text-anchor="middle">Disputed Ballot Seal + Viral Fake News Image of Stolen Ballot Box on Social Media</text>
    <text x="0" y="60" font-size="9.5" fill="#fca5a5" text-anchor="middle">Tensions spike outside tallying center; youth groups mobilize on false rumors.</text>
  </g>

  <!-- 3-Stage Resolution Workflow (Bottom) -->
  <g transform="translate(180, 365)">
    <rect x="-110" y="0" width="220" height="135" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="-110" y="0" width="220" height="24" rx="8" fill="#0284c7"/>
    <text x="0" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PHASE 1: FACT-CHECKING</text>
    <text x="0" y="44" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">NCIC &amp; Media De-escalation</text>
    <text x="0" y="64" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Verify viral image provenance</text>
    <text x="0" y="80" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Prove photo is from 2018</text>
    <text x="0" y="96" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Issue joint press statement</text>
    <text x="0" y="112" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Quell social media panic</text>
  </g>

  <!-- Arrow Phase 1 -> 2 -->
  <path d="M 300 432 L 350 432" fill="none" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#sim-arrow)"/>

  <g transform="translate(480, 365)">
    <rect x="-110" y="0" width="220" height="135" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="-110" y="0" width="220" height="24" rx="8" fill="#059669"/>
    <text x="0" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PHASE 2: VERIFICATION</text>
    <text x="0" y="44" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Digital Form 34A Audit</text>
    <text x="0" y="64" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Cross-examine physical Form 34A</text>
    <text x="0" y="80" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Check KIEMS biometric scan</text>
    <text x="0" y="96" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Inspect broken seal logbook</text>
    <text x="0" y="112" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Transparent agent scrutiny</text>
  </g>

  <!-- Arrow Phase 2 -> 3 -->
  <path d="M 600 432 L 650 432" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#sim-arrow)"/>

  <g transform="translate(780, 365)">
    <rect x="-110" y="0" width="220" height="135" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="-110" y="0" width="220" height="24" rx="8" fill="#d97706"/>
    <text x="0" y="16" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PHASE 3: ACCORD &amp; COURTS</text>
    <text x="0" y="44" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Peace Accord &amp; Legal Path</text>
    <text x="0" y="64" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Candidates sign Peace Accord</text>
    <text x="0" y="80" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Direct supporters off streets</text>
    <text x="0" y="96" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Refer dispute to High Court</text>
    <text x="0" y="112" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Rule of law prevails</text>
  </g>

  <defs>
    <marker id="sim-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
  </defs>
</svg>
""".strip()
