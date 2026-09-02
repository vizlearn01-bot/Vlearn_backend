"""
VLearn CBC Grade 10 Business Studies — Topic 10: Consumer Satisfaction
Vector SVG Diagram Definitions
"""

SVG_LEAKY_BUCKET_MODEL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bktGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#3B82F6" /><stop offset="100%" stop-color="#1D4ED8" /></linearGradient>
    <filter id="bktShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="480" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">The Leaky Bucket Theory of Customer Retention</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Why Customer Satisfaction is More Profitable Than Constant Acquisition</text>

  <!-- Left: Dissatisfaction Leak (Leaky Bucket) -->
  <g transform="translate(60, 100)" filter="url(#bktShadow)">
    <rect width="320" height="340" rx="8" fill="#FEF2F2" stroke="#F87171" stroke-width="2" />
    <text x="160" y="30" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#991B1B" text-anchor="middle">A. High Dissatisfaction (Leaky)</text>
    
    <!-- Water Tap (Acquisition) -->
    <rect x="135" y="50" width="50" height="20" fill="#94A3B8" rx="4" />
    <path d="M 160 70 L 160 110" stroke="#38BDF8" stroke-width="6" stroke-dasharray="4" />
    <text x="160" y="100" font-family="system-ui, sans-serif" font-size="9" fill="#0369A1" text-anchor="middle">New Inflow (+100)</text>

    <!-- Bucket Graphic -->
    <path d="M 100 120 L 220 120 L 200 240 L 120 240 Z" fill="#EF4444" opacity="0.2" stroke="#DC2626" stroke-width="2" />
    
    <!-- Leaks -->
    <path d="M 120 200 L 70 230" stroke="#DC2626" stroke-width="4" stroke-dasharray="3" />
    <text x="50" y="245" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#B91C1C">Poor Service (-40)</text>

    <path d="M 200 200 L 250 230" stroke="#DC2626" stroke-width="4" stroke-dasharray="3" />
    <text x="260" y="245" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#B91C1C">Bad Quality (-45)</text>

    <rect x="20" y="270" width="280" height="50" rx="6" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="160" y="290" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#991B1B" text-anchor="middle">Retained Customers = ONLY 15</text>
    <text x="160" y="308" font-family="system-ui, sans-serif" font-size="9" fill="#7F1D1D" text-anchor="middle">High acquisition costs; zero long-term profit.</text>
  </g>

  <!-- Right: Mastered Retention (Sealed Bucket) -->
  <g transform="translate(420, 100)" filter="url(#bktShadow)">
    <rect width="320" height="340" rx="8" fill="#ECFDF5" stroke="#34D399" stroke-width="2" />
    <text x="160" y="30" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#065F46" text-anchor="middle">B. High Satisfaction (Sealed)</text>
    
    <!-- Water Tap -->
    <rect x="135" y="50" width="50" height="20" fill="#94A3B8" rx="4" />
    <path d="M 160 70 L 160 110" stroke="#10B981" stroke-width="6" stroke-dasharray="4" />
    <text x="160" y="100" font-family="system-ui, sans-serif" font-size="9" fill="#047857" text-anchor="middle">New Inflow (+100)</text>

    <!-- Sealed Bucket Graphic -->
    <path d="M 100 120 L 220 120 L 200 240 L 120 240 Z" fill="#10B981" opacity="0.3" stroke="#059669" stroke-width="2" />
    <text x="160" y="185" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#065F46" text-anchor="middle">NO LEAKS</text>

    <rect x="20" y="270" width="280" height="50" rx="6" fill="#FFFFFF" stroke="#6EE7B7" />
    <text x="160" y="290" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#065F46" text-anchor="middle">Retained Customers = 95+</text>
    <text x="160" y="308" font-family="system-ui, sans-serif" font-size="9" fill="#047857" text-anchor="middle">High repeat sales + organic word-of-mouth.</text>
  </g>
</svg>"""

SVG_CONSUMER_REMEDIES_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="remGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#4338CA" /><stop offset="100%" stop-color="#6366F1" /></linearGradient>
    <filter id="remShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="480" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">Statutory Remedies for Consumer Dissatisfaction (CPA 2012)</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Legal and Commercial Options When Supplied Goods or Services Fail Standards</text>

  <!-- 4 Remedy Blocks -->
  <!-- 1. Free Repair -->
  <g transform="translate(50, 100)" filter="url(#remShadow)">
    <rect width="330" height="155" rx="8" fill="#FFFFFF" stroke="#6366F1" stroke-width="2" />
    <rect width="330" height="38" rx="8" fill="url(#remGrad)" />
    <text x="165" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. Prompt Free Repair</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#4338CA">When Applicable:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Minor mechanical or electrical fault under warranty</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Seller repairs at zero cost within reasonable time</text>
    <text x="15" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#059669">Example: Fixing loose solar inverter connector</text>
  </g>

  <!-- 2. Full Replacement -->
  <g transform="translate(420, 100)" filter="url(#remShadow)">
    <rect width="330" height="155" rx="8" fill="#FFFFFF" stroke="#6366F1" stroke-width="2" />
    <rect width="330" height="38" rx="8" fill="url(#remGrad)" />
    <text x="165" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. Direct Product Replacement</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#4338CA">When Applicable:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Irreparable defect or recurring breakdown</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Supplier swaps item for identical brand-new unit</text>
    <text x="15" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#059669">Example: Replacing defective dead smartphone screen</text>
  </g>

  <!-- 3. Full / Partial Refund -->
  <g transform="translate(50, 280)" filter="url(#remShadow)">
    <rect width="330" height="155" rx="8" fill="#FFFFFF" stroke="#6366F1" stroke-width="2" />
    <rect width="330" height="38" rx="8" fill="url(#remGrad)" />
    <text x="165" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. Full Cash Refund</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#4338CA">When Applicable:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Fundamental breach of contract; out-of-stock replacement</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Complete return of purchase money to buyer</text>
    <text x="15" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#059669">Example: Refunding payment for expired milk delivery</text>
  </g>

  <!-- 4. Damages & CAK Complaint -->
  <g transform="translate(420, 280)" filter="url(#remShadow)">
    <rect width="330" height="155" rx="8" fill="#FFFFFF" stroke="#6366F1" stroke-width="2" />
    <rect width="330" height="38" rx="8" fill="url(#remGrad)" />
    <text x="165" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4. Legal Damages / CAK Escalation</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#4338CA">When Applicable:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Defective good caused personal injury or property loss</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Filing complaint with Competition Authority of Kenya</text>
    <text x="15" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#059669">Example: Compensation for laptop fried by faulty charger</text>
  </g>
</svg>"""

SVG_SURVEY_ANALYSIS_CHART = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <filter id="chrtShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="480" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">Customer Satisfaction Survey Results: School Canteen</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Frequency Distribution &amp; Relative Percentage Breakdown (Sample Size N = 200 Students)</text>

  <!-- Chart Container -->
  <g transform="translate(60, 95)" filter="url(#chrtShadow)">
    <rect width="680" height="350" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
    
    <!-- Bar 1: Very Satisfied (5) -->
    <text x="30" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#15803D">Very Satisfied (5★)</text>
    <rect x="200" y="45" width="280" height="25" rx="4" fill="#22C55E" />
    <text x="490" y="62" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#15803D">70 students (35.0%)</text>

    <!-- Bar 2: Satisfied (4) -->
    <text x="30" y="115" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#059669">Satisfied (4★)</text>
    <rect x="200" y="100" width="340" height="25" rx="4" fill="#34D399" />
    <text x="550" y="117" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#059669">85 students (42.5%)</text>

    <!-- Bar 3: Neutral (3) -->
    <text x="30" y="170" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#D97706">Neutral (3★)</text>
    <rect x="200" y="155" width="100" height="25" rx="4" fill="#FBBF24" />
    <text x="310" y="172" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#D97706">25 students (12.5%)</text>

    <!-- Bar 4: Dissatisfied (2) -->
    <text x="30" y="225" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#EA580C">Dissatisfied (2★)</text>
    <rect x="200" y="210" width="48" height="25" rx="4" fill="#FB923C" />
    <text x="260" y="227" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#EA580C">12 students (6.0%)</text>

    <!-- Bar 5: Very Dissatisfied (1) -->
    <text x="30" y="280" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#DC2626">Very Dissatisfied (1★)</text>
    <rect x="200" y="265" width="32" height="25" rx="4" fill="#EF4444" />
    <text x="245" y="282" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#DC2626">8 students (4.0%)</text>

    <!-- Summary Box -->
    <rect x="20" y="300" width="640" height="35" rx="6" fill="#EFF6FF" />
    <text x="340" y="322" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#1D4ED8" text-anchor="middle">OVERALL SATISFACTION RATE (4★ + 5★) = 77.5% (High Customer Approval)</text>
  </g>
</svg>"""

SVG_CONTINUOUS_FEEDBACK_LOOP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="lpGrad1" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#2563EB" /><stop offset="100%" stop-color="#3B82F6" /></linearGradient>
    <linearGradient id="lpGrad2" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#059669" /><stop offset="100%" stop-color="#10B981" /></linearGradient>
    <linearGradient id="lpGrad3" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#D97706" /><stop offset="100%" stop-color="#F59E0B" /></linearGradient>
    <linearGradient id="lpGrad4" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#7C3AED" /><stop offset="100%" stop-color="#8B5CF6" /></linearGradient>
    <filter id="lpShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="480" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">The Continuous Service Improvement Feedback Loop</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Systematic 4-Step Cycle to Convert Consumer Complaints into Operational Excellence</text>

  <!-- Quadrant 1: Collect -->
  <g transform="translate(60, 100)" filter="url(#lpShadow)">
    <rect width="320" height="155" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2" />
    <rect width="320" height="38" rx="8" fill="url(#lpGrad1)" />
    <text x="160" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Stage 1: Multi-Channel Feedback Collection</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#1D4ED8">Collection Channels:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Physical suggestion boxes in shop</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Digital QR code survey at checkout</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Dedicated WhatsApp customer desk</text>
  </g>

  <!-- Quadrant 2: Analyze -->
  <g transform="translate(420, 100)" filter="url(#lpShadow)">
    <rect width="320" height="155" rx="8" fill="#FFFFFF" stroke="#10B981" stroke-width="2" />
    <rect width="320" height="38" rx="8" fill="url(#lpGrad2)" />
    <text x="160" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Stage 2: Root Cause Rooting &amp; Triage</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#047857">Analytical Actions:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Categorizing complaints (Quality vs Speed)</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Calculating monthly defect percentages</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Identifying recurring operational bottlenecks</text>
  </g>

  <!-- Quadrant 3: Implement -->
  <g transform="translate(420, 280)" filter="url(#lpShadow)">
    <rect width="320" height="155" rx="8" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2" />
    <rect width="320" height="38" rx="8" fill="url(#lpGrad3)" />
    <text x="160" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Stage 3: Corrective Process Remediation</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#B45309">Implementation:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Retraining frontline staff in courtesy</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Switching to reliable wholesale suppliers</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Upgrading packaging to prevent spillage</text>
  </g>

  <!-- Quadrant 4: Communicate -->
  <g transform="translate(60, 280)" filter="url(#lpShadow)">
    <rect width="320" height="155" rx="8" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2" />
    <rect width="320" height="38" rx="8" fill="url(#lpGrad4)" />
    <text x="160" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Stage 4: Closing the Loop with Consumers</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#6D28D9">Communication:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• "You Spoke, We Listened" notices</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Direct compensation/apology to aggrieved</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Re-surveying customers to confirm satisfaction</text>
  </g>
</svg>"""
