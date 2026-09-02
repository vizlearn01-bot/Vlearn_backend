"""
Validation script for Grade 10 Business Studies Topic 2 Lesson 3 JSON Object.
"""

import json
import re
import xml.etree.ElementTree as ET

# Sanitization helper
def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    return text.strip()

def sanitize_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# SVGs
SVG_GOAL_SETTING_10_STEPS = sanitize_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="890" height="510" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 10-Step Business Goal-Setting Cycle</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">A continuous, structured management loop from strategic vision to review and adaptive revision</text>

  <!-- Row 1: Steps 1 to 5 -->
  <!-- Step 1 -->
  <g transform="translate(35, 95)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#0284c7"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Vision &amp; Mission</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#38bdf8">Core Purpose:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Define long-term</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">aspirations &amp; why</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">the enterprise exists.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#38bdf8" text-anchor="middle">Strategic Compass</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(210, 95)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#0891b2"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SWOT Analysis</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#22d3ee">Environmental Audit:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Assess internal S/W</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">&amp; external market</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">O/T forces.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#22d3ee" text-anchor="middle">Situational Reality</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(385, 95)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#0d9488" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#0f766e"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Identify KRAs</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#2dd4bf">Key Result Areas:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Focus on vital domains</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">essential for survival</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">&amp; profitability.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#2dd4bf" text-anchor="middle">Priority Domains</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(560, 95)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#047857"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Brainstorm Goals</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#34d399">Creative Ideation:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Generate potential</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">targets openly</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">without initial filters.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#34d399" text-anchor="middle">Idea Generation</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(735, 95)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#16a34a" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#15803d"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Apply SMART</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#4ade80">Refinement Filter:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Make goals Specific,</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">Measurable, Achievable,</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">Relevant, Time-bound.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#4ade80" text-anchor="middle">Precision Filtering</text>
  </g>

  <!-- Connectors Row 1 -->
  <path d="M 190 177 L 210 177" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 365 177 L 385 177" stroke="#22d3ee" stroke-width="2"/>
  <path d="M 540 177 L 560 177" stroke="#2dd4bf" stroke-width="2"/>
  <path d="M 715 177 L 735 177" stroke="#34d399" stroke-width="2"/>

  <!-- Transition Curve from Step 5 to Step 6 -->
  <path d="M 812 260 L 812 300 Q 812 315 795 315 L 735 315" fill="none" stroke="#4ade80" stroke-width="2" stroke-dasharray="4"/>

  <!-- Row 2: Steps 6 to 10 -->
  <!-- Step 10 -->
  <g transform="translate(35, 305)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#c026d3" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#a21caf"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">10. Review &amp; Revise</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#e879f9">Adaptive Feedback:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Calculate variance,</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">adjust tactics, or</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">revise goals if needed.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#e879f9" text-anchor="middle">Continuous Learning</text>
  </g>

  <!-- Step 9 -->
  <g transform="translate(210, 305)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#6d28d9"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">9. Monitor Progress</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#a78bfa">Tracking &amp; Metrics:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Measure periodic</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">actual outcomes</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">against milestones.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#a78bfa" text-anchor="middle">Early Gap Detection</text>
  </g>

  <!-- Step 8 -->
  <g transform="translate(385, 305)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#e11d48" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#be123c"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">8. Action Plans</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#fb7185">Operational Roadmap:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Detail Who, What,</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">When (deadlines),</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">&amp; allocated Budget.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#fb7185" text-anchor="middle">Execution Engine</text>
  </g>

  <!-- Step 7 -->
  <g transform="translate(560, 305)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#ea580c" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#c2410c"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">7. Communicate</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#fb923c">Shared Alignment:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Share finalized targets</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">with team members</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">&amp; key stakeholders.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#fb923c" text-anchor="middle">Team Buy-In</text>
  </g>

  <!-- Step 6 -->
  <g transform="translate(735, 305)">
    <rect width="155" height="165" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.5"/>
    <rect width="155" height="28" rx="8" fill="#b45309"/>
    <text x="77.5" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Prioritize Goals</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#fbbf24">Focus Selection:</text>
    <text x="10" y="66" font-size="9.5" fill="#cbd5e1">Rank and pick top</text>
    <text x="10" y="82" font-size="9.5" fill="#cbd5e1">2 to 3 highest-impact</text>
    <text x="10" y="98" font-size="9.5" fill="#cbd5e1">vital goals.</text>
    <rect x="10" y="120" width="135" height="32" rx="4" fill="#1e293b"/>
    <text x="77.5" y="140" font-size="9" fill="#fbbf24" text-anchor="middle">Resource Focus</text>
  </g>

  <!-- Connectors Row 2 -->
  <path d="M 735 387 L 715 387" stroke="#fb923c" stroke-width="2"/>
  <path d="M 560 387 L 540 387" stroke="#fb7185" stroke-width="2"/>
  <path d="M 385 387 L 365 387" stroke="#a78bfa" stroke-width="2"/>
  <path d="M 210 387 L 190 387" stroke="#e879f9" stroke-width="2"/>

  <!-- Feedback Loop Arrow -->
  <path d="M 112 470 L 112 495 Q 112 505 100 505 L 20 505 Q 10 505 10 495 L 10 187 Q 10 177 20 177 L 35 177" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5"/>
  <text x="15" y="335" font-size="8.5" fill="#38bdf8" transform="rotate(-90 15,335)" text-anchor="middle">FEEDBACK &amp; REVISION LOOP</text>
</svg>""")

SVG_SWOT_MATRIX = sanitize_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="890" height="510" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">SWOT Strategic Environmental Matrix</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Framework for mapping internal capabilities against external market forces</text>

  <!-- Axis Header Labels -->
  <rect x="165" y="85" width="345" height="26" rx="5" fill="#065f46"/>
  <text x="337.5" y="102" font-size="11" font-weight="bold" fill="#a7f3d0" text-anchor="middle">HELPFUL (Supports Business Objectives)</text>

  <rect x="530" y="85" width="345" height="26" rx="5" fill="#881337"/>
  <text x="702.5" y="102" font-size="11" font-weight="bold" fill="#fecdd3" text-anchor="middle">HARMFUL (Obstructs Business Objectives)</text>

  <!-- Left Side Headers -->
  <g transform="translate(35, 120)">
    <rect width="115" height="185" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1"/>
    <text x="57.5" y="85" font-size="11" font-weight="bold" fill="#bfdbfe" text-anchor="middle">INTERNAL</text>
    <text x="57.5" y="102" font-size="9" fill="#93c5fd" text-anchor="middle">Within Control</text>
    <text x="57.5" y="118" font-size="8.5" fill="#cbd5e1" text-anchor="middle">(Assets, Staff,</text>
    <text x="57.5" y="132" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Processes)</text>
  </g>

  <g transform="translate(35, 320)">
    <rect width="115" height="185" rx="6" fill="#581c87" stroke="#a855f7" stroke-width="1"/>
    <text x="57.5" y="85" font-size="11" font-weight="bold" fill="#e9d5ff" text-anchor="middle">EXTERNAL</text>
    <text x="57.5" y="102" font-size="9" fill="#d8b4fe" text-anchor="middle">Outside Control</text>
    <text x="57.5" y="118" font-size="8.5" fill="#cbd5e1" text-anchor="middle">(Markets, Rivals,</text>
    <text x="57.5" y="132" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Govt, Trends)</text>
  </g>

  <!-- Quadrant 1: Strengths -->
  <g transform="translate(165, 120)">
    <rect width="345" height="185" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="345" height="32" rx="8" fill="#059669"/>
    <text x="172.5" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">STRENGTHS (S) — Internal Advantages</text>
    <text x="15" y="58" font-size="10.5" font-weight="bold" fill="#34d399">• Dedicated Infrastructure:</text>
    <text x="25" y="75" font-size="9.5" fill="#e2e8f0">High-speed fiber connectivity &amp; standby diesel generator.</text>
    <text x="15" y="98" font-size="10.5" font-weight="bold" fill="#34d399">• Technical Competence:</text>
    <text x="25" y="115" font-size="9.5" fill="#e2e8f0">Trained computer technicians &amp; reliable printing maintenance.</text>
    <text x="15" y="138" font-size="10.5" font-weight="bold" fill="#34d399">• Strategic Location:</text>
    <text x="25" y="155" font-size="9.5" fill="#e2e8f0">Situated near Kericho town center and bus terminal.</text>
  </g>

  <!-- Quadrant 2: Weaknesses -->
  <g transform="translate(530, 120)">
    <rect width="345" height="185" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="345" height="32" rx="8" fill="#d97706"/>
    <text x="172.5" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">WEAKNESSES (W) — Internal Constraints</text>
    <text x="15" y="58" font-size="10.5" font-weight="bold" fill="#fbbf24">• Low Workstation Capacity:</text>
    <text x="25" y="75" font-size="9.5" fill="#e2e8f0">Only 6 computers, causing long customer queues at peak hours.</text>
    <text x="15" y="98" font-size="10.5" font-weight="bold" fill="#fbbf24">• Limited Floor Space:</text>
    <text x="25" y="115" font-size="9.5" fill="#e2e8f0">Small room limits simultaneous desk and printing operations.</text>
    <text x="15" y="138" font-size="10.5" font-weight="bold" fill="#fbbf24">• Single Supplier Reliance:</text>
    <text x="25" y="155" font-size="9.5" fill="#e2e8f0">Dependent on one vendor for printing paper and toner cartridges.</text>
  </g>

  <!-- Quadrant 3: Opportunities -->
  <g transform="translate(165, 320)">
    <rect width="345" height="185" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="345" height="32" rx="8" fill="#0284c7"/>
    <text x="172.5" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">OPPORTUNITIES (O) — External Market Tailwinds</text>
    <text x="15" y="58" font-size="10.5" font-weight="bold" fill="#38bdf8">• University Policy Shift:</text>
    <text x="25" y="75" font-size="9.5" fill="#e2e8f0">Local university transitions coursework &amp; exams online.</text>
    <text x="15" y="98" font-size="10.5" font-weight="bold" fill="#38bdf8">• E-Government Growth:</text>
    <text x="25" y="115" font-size="9.5" fill="#e2e8f0">Surge in public demand for e-Citizen, KRA tax &amp; NTSA services.</text>
    <text x="15" y="138" font-size="10.5" font-weight="bold" fill="#38bdf8">• Student Subscription Packages:</text>
    <text x="25" y="155" font-size="9.5" fill="#e2e8f0">Opportunity to offer weekly/monthly study &amp; research bundles.</text>
  </g>

  <!-- Quadrant 4: Threats -->
  <g transform="translate(530, 320)">
    <rect width="345" height="185" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect width="345" height="32" rx="8" fill="#dc2626"/>
    <text x="172.5" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">THREATS (T) — External Market Headwinds</text>
    <text x="15" y="58" font-size="10.5" font-weight="bold" fill="#f87171">• New Competitor Entry:</text>
    <text x="25" y="75" font-size="9.5" fill="#e2e8f0">A large tech center opens across the street with 20 stations.</text>
    <text x="15" y="98" font-size="10.5" font-weight="bold" fill="#f87171">• Electricity Tariff Inflation:</text>
    <text x="25" y="115" font-size="9.5" fill="#e2e8f0">Higher commercial power bills increasing monthly overhead costs.</text>
    <text x="15" y="138" font-size="10.5" font-weight="bold" fill="#f87171">• Smartphone Internet Proliferation:</text>
    <text x="25" y="155" font-size="9.5" fill="#e2e8f0">Cheaper mobile data reducing casual web-browsing customer footfall.</text>
  </g>
</svg>""")

SVG_ACTION_PLAN_ROADMAP = sanitize_svg("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="890" height="510" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Action Plan Architecture &amp; The Performance Feedback Loop</text>
  <text x="460" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Bridging the gap between high-level SMART goals and day-to-day execution (Steps 8, 9, and 10)</text>

  <!-- Panel 1: The 4 Pillars of an Action Plan -->
  <g transform="translate(35, 85)">
    <rect width="850" height="200" rx="10" fill="#0f172a" stroke="#e11d48" stroke-width="1.5"/>
    <rect width="850" height="30" rx="10" fill="#be123c"/>
    <text x="425" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 8: THE FOUR CORE PILLARS OF A BUSINESS ACTION PLAN</text>

    <!-- Column 1: WHAT -->
    <g transform="translate(15, 45)">
      <rect width="190" height="140" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <rect width="190" height="24" rx="6" fill="#0284c7"/>
      <text x="95" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. WHAT (Action Tasks)</text>
      <text x="10" y="45" font-size="9.5" font-weight="bold" fill="#38bdf8">Specific Deliverables:</text>
      <text x="10" y="62" font-size="9" fill="#cbd5e1">• Procure 4 refurbished PCs</text>
      <text x="10" y="78" font-size="9" fill="#cbd5e1">• Install 8-port gigabit switch</text>
      <text x="10" y="94" font-size="9" fill="#cbd5e1">• Configure user billing software</text>
      <text x="10" y="110" font-size="9" fill="#cbd5e1">• Reconfigure desk layout</text>
    </g>

    <!-- Column 2: WHO -->
    <g transform="translate(225, 45)">
      <rect width="190" height="140" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <rect width="190" height="24" rx="6" fill="#059669"/>
      <text x="95" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. WHO (Responsibility)</text>
      <text x="10" y="45" font-size="9.5" font-weight="bold" fill="#34d399">Assigned Ownership:</text>
      <text x="10" y="62" font-size="9" fill="#cbd5e1">• Kiprotich (Managing Director)</text>
      <text x="10" y="78" font-size="9" fill="#cbd5e1">• Faith (Lead Technician)</text>
      <text x="10" y="94" font-size="9" fill="#cbd5e1">• Single point of accountability</text>
      <text x="10" y="110" font-size="9" fill="#cbd5e1">• Clear role delegation</text>
    </g>

    <!-- Column 3: WHEN -->
    <g transform="translate(435, 45)">
      <rect width="190" height="140" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <rect width="190" height="24" rx="6" fill="#d97706"/>
      <text x="95" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. WHEN (Deadlines)</text>
      <text x="10" y="45" font-size="9.5" font-weight="bold" fill="#fbbf24">Time Milestones:</text>
      <text x="10" y="62" font-size="9" fill="#cbd5e1">• Hardware Order: Day 5</text>
      <text x="10" y="78" font-size="9" fill="#cbd5e1">• LAN Cabling: Day 12</text>
      <text x="10" y="94" font-size="9" fill="#cbd5e1">• System Testing: Day 18</text>
      <text x="10" y="110" font-size="9" fill="#cbd5e1">• Full Launch: By 15th Oct</text>
    </g>

    <!-- Column 4: BUDGET -->
    <g transform="translate(645, 45)">
      <rect width="190" height="140" rx="6" fill="#1e293b" stroke="#a78bfa" stroke-width="1"/>
      <rect width="190" height="24" rx="6" fill="#7c3aed"/>
      <text x="95" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. BUDGET (Resources)</text>
      <text x="10" y="45" font-size="9.5" font-weight="bold" fill="#a78bfa">Financial &amp; Material:</text>
      <text x="10" y="62" font-size="9" fill="#cbd5e1">• 4 Refurbished PCs: KES 60,000</text>
      <text x="10" y="78" font-size="9" fill="#cbd5e1">• Switch &amp; Cabling: KES 15,000</text>
      <text x="10" y="94" font-size="9" fill="#cbd5e1">• Carpentry Desks: KES 20,000</text>
      <text x="10" y="110" font-size="9" fill="#cbd5e1">• Total Budget: KES 95,000</text>
    </g>
  </g>

  <!-- Downward Flow Arrows -->
  <path d="M 460 285 L 460 305" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/>

  <!-- Panel 2: Review & Variance Loop -->
  <g transform="translate(35, 305)">
    <rect width="850" height="200" rx="10" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
    <rect width="850" height="30" rx="10" fill="#6d28d9"/>
    <text x="425" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STEPS 9 &amp; 10: THE PERFORMANCE MONITORING &amp; ADAPTIVE REVISION LOOP</text>

    <!-- Stage A: Set Target -->
    <g transform="translate(20, 45)">
      <rect width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="90" y="24" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">A. Planned Target</text>
      <line x1="15" y1="32" x2="165" y2="32" stroke="#334155" stroke-width="1"/>
      <text x="12" y="55" font-size="9.5" fill="#cbd5e1">• Capacity: 10 stations</text>
      <text x="12" y="75" font-size="9.5" fill="#cbd5e1">• Daily Logins: 120 users</text>
      <text x="12" y="95" font-size="9.5" fill="#cbd5e1">• Revenue Target:</text>
      <text x="12" y="112" font-size="9.5" font-weight="bold" fill="#38bdf8">  KES 6,000 / day</text>
    </g>

    <!-- Flow Arrow A -> B -->
    <path d="M 205 112 L 225 112" stroke="#38bdf8" stroke-width="2"/>

    <!-- Stage B: Measure Actual -->
    <g transform="translate(230, 45)">
      <rect width="180" height="135" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="90" y="24" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">B. Actual Performance</text>
      <line x1="15" y1="32" x2="165" y2="32" stroke="#334155" stroke-width="1"/>
      <text x="12" y="55" font-size="9.5" fill="#cbd5e1">• Capacity: 10 stations</text>
      <text x="12" y="75" font-size="9.5" fill="#cbd5e1">• Daily Logins: 135 users</text>
      <text x="12" y="95" font-size="9.5" fill="#cbd5e1">• Actual Revenue:</text>
      <text x="12" y="112" font-size="9.5" font-weight="bold" fill="#34d399">  KES 6,750 / day</text>
    </g>

    <!-- Flow Arrow B -> C -->
    <path d="M 415 112 L 435 112" stroke="#34d399" stroke-width="2"/>

    <!-- Stage C: Calculate Variance -->
    <g transform="translate(440, 45)">
      <rect width="185" height="135" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="92.5" y="24" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">C. Variance Analysis</text>
      <line x1="15" y1="32" x2="170" y2="32" stroke="#334155" stroke-width="1"/>
      <text x="10" y="52" font-size="9" fill="#cbd5e1">Formula: Actual - Target</text>
      <text x="10" y="72" font-size="9" fill="#cbd5e1">Revenue Variance:</text>
      <text x="10" y="88" font-size="9" font-weight="bold" fill="#34d399">+KES 750 / day</text>
      <text x="10" y="108" font-size="9" fill="#e2e8f0">Interpretation:</text>
      <text x="10" y="122" font-size="9" font-weight="bold" fill="#34d399">Favorable (+12.5%)</text>
    </g>

    <!-- Flow Arrow C -> D -->
    <path d="M 630 112 L 650 112" stroke="#fbbf24" stroke-width="2"/>

    <!-- Stage D: Take Corrective Action -->
    <g transform="translate(655, 45)">
      <rect width="175" height="135" rx="6" fill="#1e293b" stroke="#f472b6" stroke-width="1"/>
      <text x="87.5" y="24" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">D. Adaptive Action</text>
      <line x1="15" y1="32" x2="160" y2="32" stroke="#334155" stroke-width="1"/>
      <text x="10" y="50" font-size="8.5" fill="#cbd5e1">• Upgrade fiber speed</text>
      <text x="10" y="68" font-size="8.5" fill="#cbd5e1">  to prevent throttling</text>
      <text x="10" y="86" font-size="8.5" fill="#cbd5e1">• Offer off-peak pricing</text>
      <text x="10" y="104" font-size="8.5" fill="#cbd5e1">  to balance traffic</text>
      <text x="10" y="122" font-size="8.5" font-weight="bold" fill="#f472b6">• Continuous Loop</text>
    </g>
  </g>
</svg>""")

print("SVGs created successfully.")
