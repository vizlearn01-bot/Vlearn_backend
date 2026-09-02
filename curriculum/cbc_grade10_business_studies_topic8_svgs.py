"""
VLearn CBC Grade 10 Business Studies — Topic 8: Entrepreneurship
Vector SVG Diagram Definitions
"""

SVG_ENTREPRENEUR_SKILLS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="entGrad1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4F46E5" /><stop offset="100%" stop-color="#7C3AED" /></linearGradient>
    <filter id="entShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.15" /></filter>
  </defs>

  <rect width="800" height="500" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">The 6 Core Entrepreneurial Skill Competencies</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Personal and Managerial Attributes Driving Enterprise Creation and Growth</text>

  <!-- Central Badge -->
  <circle cx="400" cy="265" r="65" fill="url(#entGrad1)" filter="url(#entShadow)" />
  <text x="400" y="260" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">SUCCESSFUL</text>
  <text x="400" y="278" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FDE047" text-anchor="middle">ENTREPRENEUR</text>

  <!-- Skill 1: Opportunity Identification -->
  <g transform="translate(60, 105)" filter="url(#entShadow)">
    <rect width="200" height="65" rx="8" fill="#FFFFFF" stroke="#6366F1" stroke-width="2" />
    <text x="100" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#4338CA" text-anchor="middle">1. Opportunity Spotting</text>
    <text x="100" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Detecting unmet market gaps</text>
  </g>

  <!-- Skill 2: Calculated Risk Taking -->
  <g transform="translate(540, 105)" filter="url(#entShadow)">
    <rect width="200" height="65" rx="8" fill="#FFFFFF" stroke="#EC4899" stroke-width="2" />
    <text x="100" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#BE185D" text-anchor="middle">2. Calculated Risk-Taking</text>
    <text x="100" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Investing under uncertainty</text>
  </g>

  <!-- Skill 3: Innovation & Creativity -->
  <g transform="translate(560, 235)" filter="url(#entShadow)">
    <rect width="200" height="65" rx="8" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2" />
    <text x="100" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#B45309" text-anchor="middle">3. Innovation &amp; Creativity</text>
    <text x="100" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Creating unique value solutions</text>
  </g>

  <!-- Skill 4: Resilience & Persistence -->
  <g transform="translate(540, 365)" filter="url(#entShadow)">
    <rect width="200" height="65" rx="8" fill="#FFFFFF" stroke="#10B981" stroke-width="2" />
    <text x="100" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#047857" text-anchor="middle">4. Resilience &amp; Grit</text>
    <text x="100" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Overcoming startup failures</text>
  </g>

  <!-- Skill 5: Resource Mobilization -->
  <g transform="translate(60, 365)" filter="url(#entShadow)">
    <rect width="200" height="65" rx="8" fill="#FFFFFF" stroke="#06B6D4" stroke-width="2" />
    <text x="100" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0891B2" text-anchor="middle">5. Resource Mobilization</text>
    <text x="100" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Pooling capital, labor, tech</text>
  </g>

  <!-- Skill 6: Financial Literacy -->
  <g transform="translate(40, 235)" filter="url(#entShadow)">
    <rect width="200" height="65" rx="8" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="2" />
    <text x="100" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#6D28D9" text-anchor="middle">6. Financial Management</text>
    <text x="100" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Cash flow, costing &amp; pricing</text>
  </g>

  <!-- Connecting Lines -->
  <line x1="260" y1="150" x2="340" y2="230" stroke="#CBD5E1" stroke-width="2" />
  <line x1="540" y1="150" x2="460" y2="230" stroke="#CBD5E1" stroke-width="2" />
  <line x1="560" y1="265" x2="470" y2="265" stroke="#CBD5E1" stroke-width="2" />
  <line x1="540" y1="380" x2="460" y2="300" stroke="#CBD5E1" stroke-width="2" />
  <line x1="260" y1="380" x2="340" y2="300" stroke="#CBD5E1" stroke-width="2" />
  <line x1="240" y1="265" x2="330" y2="265" stroke="#CBD5E1" stroke-width="2" />
</svg>"""

SVG_ENTREPRENEUR_TYPES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="typGrad1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#3B82F6" /><stop offset="100%" stop-color="#1D4ED8" /></linearGradient>
    <linearGradient id="typGrad2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#10B981" /><stop offset="100%" stop-color="#047857" /></linearGradient>
    <linearGradient id="typGrad3" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#F59E0B" /><stop offset="100%" stop-color="#B45309" /></linearGradient>
    <linearGradient id="typGrad4" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#EC4899" /><stop offset="100%" stop-color="#BE185D" /></linearGradient>
    <filter id="typShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="480" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">Classification of Entrepreneurs in Modern Business</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Comparing Key Categories Based on Innovation, Risk Tolerance &amp; Objectives</text>

  <!-- 1. Innovative Entrepreneur -->
  <g transform="translate(50, 100)" filter="url(#typShadow)">
    <rect width="330" height="160" rx="8" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2" />
    <rect width="330" height="40" rx="8" fill="url(#typGrad1)" />
    <text x="165" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. Innovative Entrepreneur</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#1D4ED8">Characteristics:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Introduces completely new products or methods</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• High risk tolerance; heavy R&amp;D focus</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Example: Roy Allela (Sign-IO smart gloves)</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#059669">Outcome: Disrupts and expands markets</text>
  </g>

  <!-- 2. Imitative / Adoptive Entrepreneur -->
  <g transform="translate(420, 100)" filter="url(#typShadow)">
    <rect width="330" height="160" rx="8" fill="#FFFFFF" stroke="#10B981" stroke-width="2" />
    <rect width="330" height="40" rx="8" fill="url(#typGrad2)" />
    <text x="165" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. Imitative / Adoptive Entrepreneur</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#047857">Characteristics:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Copies successful innovations suited to local context</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Moderate risk; lower development expenditure</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Example: Localizing mobile delivery apps to Kenyan towns</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#059669">Outcome: Rapid technology diffusion</text>
  </g>

  <!-- 3. Fabian & Drone Entrepreneurs -->
  <g transform="translate(50, 285)" filter="url(#typShadow)">
    <rect width="330" height="160" rx="8" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2" />
    <rect width="330" height="40" rx="8" fill="url(#typGrad3)" />
    <text x="165" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. Fabian &amp; Drone Entrepreneurs</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#B45309">Characteristics:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Fabian: Very cautious; adopts changes only when forced</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Drone: Completely resists innovation even when failing</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Example: Obsolete manual typewriter repair shops</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#DC2626">Outcome: High risk of business closure</text>
  </g>

  <!-- 4. Social Entrepreneur -->
  <g transform="translate(420, 285)" filter="url(#typShadow)">
    <rect width="330" height="160" rx="8" fill="#FFFFFF" stroke="#EC4899" stroke-width="2" />
    <rect width="330" height="40" rx="8" fill="url(#typGrad4)" />
    <text x="165" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4. Social Entrepreneur</text>
    <text x="15" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#BE185D">Characteristics:</text>
    <text x="15" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Prioritizes solving societal/environmental problems</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Reinvests commercial profits into community mission</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Example: Clean cookstoves replacing charcoal</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#059669">Outcome: Sustainable social empowerment</text>
  </g>
</svg>"""

SVG_IDEA_VS_OPPORTUNITY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="ivGrad1" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#94A3B8" /><stop offset="100%" stop-color="#64748B" /></linearGradient>
    <linearGradient id="ivGrad2" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#10B981" /><stop offset="100%" stop-color="#047857" /></linearGradient>
    <filter id="ivShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="450" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">Business Idea vs. Genuine Business Opportunity</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Transforming Raw Concept into a Commercially Viable &amp; Profitable Enterprise</text>

  <!-- Left: Raw Business Idea -->
  <g transform="translate(60, 105)" filter="url(#ivShadow)">
    <rect width="300" height="300" rx="8" fill="#FFFFFF" stroke="#94A3B8" stroke-width="2" />
    <rect width="300" height="45" rx="8" fill="url(#ivGrad1)" />
    <text x="150" y="28" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Raw Business Idea (The Seed)</text>
    
    <text x="20" y="75" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#475569">• Mental Thought / Conception</text>
    <text x="20" y="95" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">"I want to sell hot fresh fruit smoothies."</text>
    
    <text x="20" y="130" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#475569">• Unverified Demand</text>
    <text x="20" y="150" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">No proof that buyers have purchasing power.</text>
    
    <text x="20" y="185" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#475569">• Low Economic Value Alone</text>
    <text x="20" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">Anyone can think of an idea; zero execution.</text>

    <rect x="20" y="240" width="260" height="45" rx="6" fill="#F1F5F9" />
    <text x="150" y="267" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#64748B" text-anchor="middle">Status: Unproven Concept</text>
  </g>

  <!-- Arrow Transition -->
  <path d="M 375 255 L 425 255 M 415 245 L 425 255 L 415 265" stroke="#3B82F6" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
  <text x="400" y="235" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#2563EB" text-anchor="middle">VALIDATE &amp;</text>
  <text x="400" y="280" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#2563EB" text-anchor="middle">SCREEN</text>

  <!-- Right: Genuine Business Opportunity -->
  <g transform="translate(440, 105)" filter="url(#ivShadow)">
    <rect width="300" height="300" rx="8" fill="#FFFFFF" stroke="#10B981" stroke-width="2" />
    <rect width="300" height="45" rx="8" fill="url(#ivGrad2)" />
    <text x="150" y="28" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Business Opportunity (The Tree)</text>
    
    <text x="20" y="75" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#047857">• Verified Paying Market</text>
    <text x="20" y="95" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">Customers are ready and willing to pay KES 50.</text>
    
    <text x="20" y="130" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#047857">• Financial Feasibility</text>
    <text x="20" y="150" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">Cost = KES 30; Profit margin = KES 20 (40%).</text>
    
    <text x="20" y="185" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#047857">• Sustainable Competitive Edge</text>
    <text x="20" y="205" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">Direct farm supply gives cost advantage.</text>

    <rect x="20" y="240" width="260" height="45" rx="6" fill="#ECFDF5" />
    <text x="150" y="267" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#059669" text-anchor="middle">Status: Bankable &amp; Investable</text>
  </g>
</svg>"""

SVG_SCREENING_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="scGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#1E40AF" /><stop offset="100%" stop-color="#3B82F6" /></linearGradient>
    <filter id="scShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="480" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">Opportunity Screening &amp; Decision Matrix</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Quantitative Multi-Factor Evaluation for School Enterprise Selection</text>

  <!-- Table Box -->
  <g transform="translate(40, 95)" filter="url(#scShadow)">
    <rect width="720" height="350" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2" />
    
    <!-- Table Header -->
    <rect width="720" height="45" rx="8" fill="url(#scGrad)" />
    <text x="30" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">Evaluation Criteria (Weight)</text>
    <text x="300" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Project A: Juice Bar</text>
    <text x="480" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Project B: Poultry</text>
    <text x="640" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Project C: Bakery</text>

    <!-- Row 1: Market Demand (25%) -->
    <text x="30" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#1E293B">1. Market Demand (25%)</text>
    <text x="300" y="80" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">9/10 (Score: 2.25)</text>
    <text x="480" y="80" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">7/10 (Score: 1.75)</text>
    <text x="640" y="80" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">8/10 (Score: 2.00)</text>
    <line x1="20" y1="95" x2="700" y2="95" stroke="#F1F5F9" stroke-width="1.5" />

    <!-- Row 2: Startup Capital (25%) -->
    <text x="30" y="125" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#1E293B">2. Capital Affordability (25%)</text>
    <text x="300" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">8/10 (Score: 2.00)</text>
    <text x="480" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">5/10 (Score: 1.25)</text>
    <text x="640" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">6/10 (Score: 1.50)</text>
    <line x1="20" y1="140" x2="700" y2="140" stroke="#F1F5F9" stroke-width="1.5" />

    <!-- Row 3: Technical Skills (20%) -->
    <text x="30" y="170" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#1E293B">3. Technical Skills (20%)</text>
    <text x="300" y="170" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">9/10 (Score: 1.80)</text>
    <text x="480" y="170" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">6/10 (Score: 1.20)</text>
    <text x="640" y="170" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">7/10 (Score: 1.40)</text>
    <line x1="20" y1="185" x2="700" y2="185" stroke="#F1F5F9" stroke-width="1.5" />

    <!-- Row 4: Profit Margin (20%) -->
    <text x="30" y="215" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#1E293B">4. Profit Margin (20%)</text>
    <text x="300" y="215" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">8/10 (Score: 1.60)</text>
    <text x="480" y="215" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">8/10 (Score: 1.60)</text>
    <text x="640" y="215" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">7/10 (Score: 1.40)</text>
    <line x1="20" y1="230" x2="700" y2="230" stroke="#F1F5F9" stroke-width="1.5" />

    <!-- Row 5: Risk Level (10%) -->
    <text x="30" y="260" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#1E293B">5. Risk Manageability (10%)</text>
    <text x="300" y="260" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">8/10 (Score: 0.80)</text>
    <text x="480" y="260" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">4/10 (Score: 0.40)</text>
    <text x="640" y="260" font-family="system-ui, sans-serif" font-size="11" fill="#334155" text-anchor="middle">6/10 (Score: 0.60)</text>
    <line x1="20" y1="275" x2="700" y2="275" stroke="#CBD5E1" stroke-width="2" />

    <!-- Total Score Row -->
    <rect x="10" y="285" width="700" height="50" rx="6" fill="#EFF6FF" />
    <text x="30" y="315" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#1E40AF">TOTAL WEIGHTED SCORE:</text>
    <text x="300" y="315" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle">8.45 / 10 (WINNER)</text>
    <text x="480" y="315" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">6.20 / 10</text>
    <text x="640" y="315" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">6.90 / 10</text>
  </g>
</svg>"""

SVG_INCUBATION_PILLARS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="incGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0284C7" /><stop offset="100%" stop-color="#0369A1" /></linearGradient>
    <filter id="incShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="460" fill="#F0F9FF" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0C4A6E" text-anchor="middle">The Business Incubation Ecosystem</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#0369A1" text-anchor="middle">Nurturing Early-Stage Startups into Sustainable Commercial Enterprises</text>

  <!-- 4 Pillars -->
  <!-- 1. Infrastructure -->
  <g transform="translate(50, 100)" filter="url(#incShadow)">
    <rect width="160" height="320" rx="8" fill="#FFFFFF" stroke="#38BDF8" stroke-width="2" />
    <rect width="160" height="45" rx="8" fill="url(#incGrad)" />
    <text x="80" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. Physical Space</text>
    <text x="15" y="80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#0369A1">Facilities Provided:</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Co-working desks</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• High-speed internet</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Meeting rooms</text>
    <text x="15" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• 3D printing labs</text>
    <rect x="10" y="240" width="140" height="65" rx="6" fill="#F0F9FF" />
    <text x="80" y="265" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#0369A1" text-anchor="middle">Benefit:</text>
    <text x="80" y="285" font-family="system-ui, sans-serif" font-size="8" fill="#0284C7" text-anchor="middle">Cuts startup overheads</text>
  </g>

  <!-- 2. Mentorship -->
  <g transform="translate(225, 100)" filter="url(#incShadow)">
    <rect width="160" height="320" rx="8" fill="#FFFFFF" stroke="#38BDF8" stroke-width="2" />
    <rect width="160" height="45" rx="8" fill="url(#incGrad)" />
    <text x="80" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. Mentorship</text>
    <text x="15" y="80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#0369A1">Guidance Offered:</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Seasoned founders</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Legal &amp; IP advice</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Marketing coaching</text>
    <text x="15" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Product refinement</text>
    <rect x="10" y="240" width="140" height="65" rx="6" fill="#F0F9FF" />
    <text x="80" y="265" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#0369A1" text-anchor="middle">Benefit:</text>
    <text x="80" y="285" font-family="system-ui, sans-serif" font-size="8" fill="#0284C7" text-anchor="middle">Prevents costly errors</text>
  </g>

  <!-- 3. Capital Access -->
  <g transform="translate(400, 100)" filter="url(#incShadow)">
    <rect width="160" height="320" rx="8" fill="#FFFFFF" stroke="#38BDF8" stroke-width="2" />
    <rect width="160" height="45" rx="8" fill="url(#incGrad)" />
    <text x="80" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. Seed Funding</text>
    <text x="15" y="80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#0369A1">Financial Access:</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Angel investor pitches</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Micro-grant awards</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• VC networking</text>
    <text x="15" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Demo Day exposure</text>
    <rect x="10" y="240" width="140" height="65" rx="6" fill="#F0F9FF" />
    <text x="80" y="265" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#0369A1" text-anchor="middle">Benefit:</text>
    <text x="80" y="285" font-family="system-ui, sans-serif" font-size="8" fill="#0284C7" text-anchor="middle">Fuels scale &amp; runway</text>
  </g>

  <!-- 4. Market Linkages -->
  <g transform="translate(575, 100)" filter="url(#incShadow)">
    <rect width="160" height="320" rx="8" fill="#FFFFFF" stroke="#38BDF8" stroke-width="2" />
    <rect width="160" height="45" rx="8" fill="url(#incGrad)" />
    <text x="80" y="28" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4. Market Links</text>
    <text x="15" y="80" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#0369A1">Network Reach:</text>
    <text x="15" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Corporate partnerships</text>
    <text x="15" y="125" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Trade fair access</text>
    <text x="15" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Regulatory fast-track</text>
    <text x="15" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#334155">• Export channel intros</text>
    <rect x="10" y="240" width="140" height="65" rx="6" fill="#F0F9FF" />
    <text x="80" y="265" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#0369A1" text-anchor="middle">Benefit:</text>
    <text x="80" y="285" font-family="system-ui, sans-serif" font-size="8" fill="#0284C7" text-anchor="middle">Accelerates revenue</text>
  </g>
</svg>"""

SVG_COST_PRICING_MODEL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%">
  <defs>
    <linearGradient id="cGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#059669" /><stop offset="100%" stop-color="#10B981" /></linearGradient>
    <filter id="cShadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" /></filter>
  </defs>

  <rect width="800" height="460" fill="#F8FAFC" rx="12" />
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" fill="#0F172A" text-anchor="middle">School Enterprise Cost Plan &amp; Cost-Plus Pricing Breakdown</text>
  <text x="400" y="70" font-family="system-ui, sans-serif" font-size="13" fill="#64748B" text-anchor="middle">Step-by-Step Unit Costing, Mark-Up Addition &amp; Selling Price Determination</text>

  <!-- Formula Visual Blocks -->
  <g transform="translate(60, 100)" filter="url(#cShadow)">
    <rect width="680" height="80" rx="8" fill="#FFFFFF" stroke="#10B981" stroke-width="2" />
    <rect width="680" height="30" rx="8" fill="url(#cGrad)" />
    <text x="340" y="20" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Core Costing Formula</text>
    <text x="340" y="58" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#065F46" text-anchor="middle">Total Cost (TC) = Total Fixed Cost (TFC) + Total Variable Cost (TVC)</text>
  </g>

  <!-- Step Breakdown -->
  <g transform="translate(60, 200)" filter="url(#cShadow)">
    <rect width="320" height="230" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2" />
    <text x="20" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Cost Breakdown (100 Juice Cups):</text>
    <text x="20" y="60" font-family="system-ui, sans-serif" font-size="11" fill="#475569">• Fruit Ingredients (Mangos, Passion): KES 1,800</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#475569">• Disposable Cups &amp; Straws: KES 400</text>
    <text x="20" y="110" font-family="system-ui, sans-serif" font-size="11" fill="#475569">• Blender Rental (Fixed Cost): KES 500</text>
    <text x="20" y="135" font-family="system-ui, sans-serif" font-size="11" fill="#475569">• Stall Hygiene License: KES 300</text>
    <line x1="20" y1="150" x2="300" y2="150" stroke="#CBD5E1" stroke-width="1.5" />
    <text x="20" y="175" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#047857">Total Batch Cost = KES 3,000</text>
    <text x="20" y="205" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#1E40AF">Unit Cost (CPU) = KES 30 / cup</text>
  </g>

  <g transform="translate(420, 200)" filter="url(#cShadow)">
    <rect width="320" height="230" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2" />
    <text x="20" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Cost-Plus Pricing (40% Mark-Up):</text>
    <text x="20" y="60" font-family="system-ui, sans-serif" font-size="11" fill="#475569">• Cost Per Unit (CPU): KES 30.00</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#475569">• Target Profit Mark-up: 40% (0.40)</text>
    <text x="20" y="110" font-family="system-ui, sans-serif" font-size="11" fill="#475569">• Profit Margin per Cup = KES 30 × 0.40 = KES 12</text>
    <line x1="20" y1="130" x2="300" y2="130" stroke="#CBD5E1" stroke-width="1.5" />
    <text x="20" y="155" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#047857">Selling Price = CPU + Profit Mark-up</text>
    <text x="20" y="180" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#15803D">Selling Price = KES 42.00 / cup</text>
    <text x="20" y="210" font-family="system-ui, sans-serif" font-size="11" fill="#64748B">Batch Total Revenue (100 cups) = KES 4,200</text>
  </g>
</svg>"""
