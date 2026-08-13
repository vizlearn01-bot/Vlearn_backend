"""
Form 4 Agriculture — Topic 4 Data File
Topic: Agricultural Economics III (Production Economics)
Curriculum: 844 (ID: 4) | Grade: Form 4 (ID: 4) | Subject: Agriculture (ID: 19) | Topic ID: 98 (Order: 4)

Contains 5 Learning Units:
1. Agriculture, National Income, and Production Resources
2. Production Functions, Marginal Products, and Production Zones
3. Substitution, Equimarginal Returns, and Profit Maximisation
4. Farm Planning and Budgeting
5. Agricultural Support Services, Credit, and Risk Management
"""

# =============================================================================
# CUSTOM DARK-MODE SVG DIAGRAMS FOR AGRICULTURAL ECONOMICS III
# =============================================================================

# 1. Circular Flow of Income Diagram
SVG_CIRCULAR_FLOW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">The Circular Flow of Income in Agricultural Economy</text>
  
  <!-- Households Box -->
  <rect x="80" y="180" width="180" height="120" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="170" y="225" font-family="Arial" font-size="18" fill="#38bdf8" font-weight="bold" text-anchor="middle">HOUSEHOLDS</text>
  <text x="170" y="255" font-family="Arial" font-size="12" fill="#94a3b8" text-anchor="middle">(Farmers & Families)</text>
  <text x="170" y="275" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Provide Factors of Production</text>

  <!-- Firms Box -->
  <rect x="540" y="180" width="180" height="120" rx="12" fill="#1e293b" stroke="#4ade80" stroke-width="3"/>
  <text x="630" y="225" font-family="Arial" font-size="18" fill="#4ade80" font-weight="bold" text-anchor="middle">FIRMS</text>
  <text x="630" y="255" font-family="Arial" font-size="12" fill="#94a3b8" text-anchor="middle">(Processors & Factories)</text>
  <text x="630" y="275" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Produce Goods & Services</text>

  <!-- Government Center Box -->
  <rect x="330" y="200" width="140" height="80" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="400" y="235" font-family="Arial" font-size="14" fill="#f59e0b" font-weight="bold" text-anchor="middle">GOVERNMENT</text>
  <text x="400" y="258" font-family="Arial" font-size="11" fill="#94a3b8" text-anchor="middle">Public Services & Taxes</text>

  <!-- Top Flow: Factors of Production (Households -> Firms) -->
  <path d="M 260 200 Q 400 100 540 200" fill="none" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrow-blue)"/>
  <text x="400" y="130" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold" text-anchor="middle">1. Supply Factors of Production (Land, Labour, Capital)</text>

  <!-- Upper-Middle Flow: Factor Payments (Firms -> Households) -->
  <path d="M 540 230 Q 400 150 260 230" fill="none" stroke="#4ade80" stroke-width="3.5" stroke-dasharray="6,4"/>
  <text x="400" y="178" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold" text-anchor="middle">2. Factor Payments (Wages, Rent, Interest, Profits)</text>

  <!-- Lower-Middle Flow: Consumer Goods (Firms -> Households) -->
  <path d="M 540 250 Q 400 330 260 250" fill="none" stroke="#f43f5e" stroke-width="3.5"/>
  <text x="400" y="305" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold" text-anchor="middle">3. Consumer Goods & Services Delivered</text>

  <!-- Bottom Flow: Consumer Expenditure (Households -> Firms) -->
  <path d="M 260 280 Q 400 380 540 280" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-dasharray="6,4"/>
  <text x="400" y="355" font-family="Arial" font-size="13" fill="#fbbf24" font-weight="bold" text-anchor="middle">4. Consumer Expenditure (Payment for Goods)</text>

  <!-- Taxes to Government -->
  <line x1="220" y1="300" x2="350" y2="280" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="270" y="315" font-family="Arial" font-size="11" fill="#f59e0b">Taxes</text>

  <line x1="580" y1="300" x2="450" y2="280" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="520" y="315" font-family="Arial" font-size="11" fill="#f59e0b">Taxes</text>

  <!-- Legend -->
  <rect x="150" y="415" width="500" height="45" fill="#0284c7" rx="8" opacity="0.2"/>
  <text x="400" y="442" font-family="Arial" font-size="12" fill="#38bdf8" text-anchor="middle" font-weight="bold">Real Flow (Goods & Services) vs Money Flow (Income & Expenditure)</text>
</svg>"""


# 2. Production Functions & Three Zones Diagram
SVG_PRODUCTION_ZONES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Production Function Curves & Three Production Zones</text>

  <!-- Graph Axes -->
  <line x1="100" y1="420" x2="740" y2="420" stroke="#94a3b8" stroke-width="3"/>
  <line x1="100" y1="420" x2="100" y2="70" stroke="#94a3b8" stroke-width="3"/>
  
  <text x="420" y="460" font-family="Arial" font-size="14" fill="#cbd5e1" text-anchor="middle" font-weight="bold">Variable Input (e.g. Fertilizer in kg)</text>
  <text x="40" y="240" font-family="Arial" font-size="14" fill="#cbd5e1" text-anchor="middle" font-weight="bold" transform="rotate(-90 40 240)">Output / Product (Bags)</text>

  <!-- Zone Boundaries -->
  <line x1="320" y1="70" x2="320" y2="420" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="6,4"/>
  <line x1="560" y1="70" x2="560" y2="420" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="6,4"/>

  <!-- Zone Headers -->
  <rect x="110" y="85" width="200" height="35" fill="#ef4444" rx="6" opacity="0.2"/>
  <text x="210" y="108" font-family="Arial" font-size="14" fill="#fca5a5" font-weight="bold" text-anchor="middle">ZONE I (Irrational)</text>

  <rect x="330" y="85" width="220" height="35" fill="#22c55e" rx="6" opacity="0.2"/>
  <text x="440" y="108" font-family="Arial" font-size="14" fill="#86efac" font-weight="bold" text-anchor="middle">ZONE II (Rational)</text>

  <rect x="570" y="85" width="160" height="35" fill="#ef4444" rx="6" opacity="0.2"/>
  <text x="650" y="108" font-family="Arial" font-size="14" fill="#fca5a5" font-weight="bold" text-anchor="middle">ZONE III (Irrational)</text>

  <!-- Total Product (TP) Curve -->
  <path d="M 100 420 C 180 370, 260 250, 320 180 C 400 120, 500 110, 560 110 C 640 110, 700 180, 740 250" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="570" y="100" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold">TP (Total Product Max)</text>

  <!-- Average Product (AP) Curve -->
  <path d="M 100 420 C 180 340, 260 280, 320 260 C 420 240, 560 300, 740 370" fill="none" stroke="#f59e0b" stroke-width="3.5"/>
  <text x="330" y="250" font-family="Arial" font-size="13" fill="#f59e0b" font-weight="bold">AP (Average Product)</text>

  <!-- Marginal Product (MP) Curve -->
  <path d="M 100 420 C 160 260, 240 160, 320 260 C 420 360, 500 410, 560 420 C 620 430, 700 470, 740 480" fill="none" stroke="#4ade80" stroke-width="3.5"/>
  <text x="240" y="150" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold">MP Peak</text>
  <text x="570" y="440" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold">MP = 0</text>

  <!-- Key Intersection Notes -->
  <circle cx="320" cy="260" r="6" fill="#f59e0b"/>
  <text x="320" y="290" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Boundary 1: MP = AP</text>

  <circle cx="560" cy="420" r="6" fill="#4ade80"/>
  <text x="560" y="400" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Boundary 2: MP = 0</text>
</svg>"""


# 3. Least-Cost Combination & Isoquant Graph
SVG_LEAST_COST = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Least-Cost Input Combination (Isoquant & Isocost Line)</text>

  <!-- Axes -->
  <line x1="120" y1="400" x2="720" y2="400" stroke="#94a3b8" stroke-width="3"/>
  <line x1="120" y1="400" x2="120" y2="80" stroke="#94a3b8" stroke-width="3"/>

  <text x="420" y="445" font-family="Arial" font-size="14" fill="#cbd5e1" text-anchor="middle" font-weight="bold">Input X1 (Phosphate Fertilizer in Units)</text>
  <text x="50" y="240" font-family="Arial" font-size="14" fill="#cbd5e1" text-anchor="middle" font-weight="bold" transform="rotate(-90 50 240)">Input X2 (Farmyard Manure in Units)</text>

  <!-- Isocost Line (Budget constraint) -->
  <line x1="120" y1="120" x2="680" y2="400" stroke="#f43f5e" stroke-width="3.5"/>
  <text x="600" y="380" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold">Isocost Line (Price Ratio PX1/PX2)</text>

  <!-- Isoquant Curve (Constant output line) -->
  <path d="M 160 100 Q 240 320, 680 370" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="580" y="350" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold">Isoquant (20 Bags Output)</text>

  <!-- Tangency Point (Least Cost Combination) -->
  <circle cx="320" cy="232" r="8" fill="#4ade80" stroke="#ffffff" stroke-width="2"/>
  <line x1="320" y1="232" x2="320" y2="400" stroke="#4ade80" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="120" y1="232" x2="320" y2="232" stroke="#4ade80" stroke-width="2" stroke-dasharray="4,4"/>

  <text x="320" y="420" font-family="Arial" font-size="12" fill="#4ade80" font-weight="bold" text-anchor="middle">X1 = 2 Units</text>
  <text x="100" y="235" font-family="Arial" font-size="12" fill="#4ade80" font-weight="bold" text-anchor="end">X2 = 4 Units</text>

  <!-- Tangency Box Annotation -->
  <rect x="360" y="160" width="300" height="70" fill="#1e293b" stroke="#4ade80" stroke-width="2" rx="8"/>
  <text x="510" y="188" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold" text-anchor="middle">Least-Cost Point of Tangency</text>
  <text x="510" y="212" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">MRS (Delta X2 / Delta X1) = Price Ratio (PX1 / PX2)</text>
</svg>"""


# 4. Partial Budget 4-Quadrant Framework
SVG_PARTIAL_BUDGET = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Partial Budget Four-Quadrant Framework</text>

  <!-- Vertical & Horizontal Dividers -->
  <line x1="400" y1="70" x2="400" y2="400" stroke="#64748b" stroke-width="3"/>
  <line x1="60" y1="230" x2="740" y2="230" stroke="#64748b" stroke-width="2"/>

  <!-- Left Header: DEBITS (Negative Effects) -->
  <rect x="60" y="70" width="330" height="40" fill="#ef4444" rx="8" opacity="0.25"/>
  <text x="225" y="96" font-family="Arial" font-size="16" fill="#fca5a5" font-weight="bold" text-anchor="middle">DEBITS (Costs & Losses)</text>

  <!-- Right Header: CREDITS (Positive Effects) -->
  <rect x="410" y="70" width="330" height="40" fill="#22c55e" rx="8" opacity="0.25"/>
  <text x="575" y="96" font-family="Arial" font-size="16" fill="#86efac" font-weight="bold" text-anchor="middle">CREDITS (Savings & Gains)</text>

  <!-- Quadrant 1: Extra Costs -->
  <text x="80" y="145" font-family="Arial" font-size="15" fill="#f8fafc" font-weight="bold">1. Extra Costs Incurred</text>
  <text x="95" y="175" font-family="Arial" font-size="12" fill="#cbd5e1">• Fresh expenses for new enterprise</text>
  <text x="95" y="195" font-family="Arial" font-size="12" fill="#cbd5e1">• e.g. Seeds, fertilizers, sprays, extra labour</text>

  <!-- Quadrant 2: Revenue Forgone -->
  <text x="80" y="265" font-family="Arial" font-size="15" fill="#f8fafc" font-weight="bold">2. Revenue Forgone</text>
  <text x="95" y="295" font-family="Arial" font-size="12" fill="#cbd5e1">• Income lost from replacing old enterprise</text>
  <text x="95" y="315" font-family="Arial" font-size="12" fill="#cbd5e1">• e.g. Lost crop or milk sales value</text>

  <!-- Quadrant 3: Costs Saved -->
  <text x="430" y="145" font-family="Arial" font-size="15" fill="#f8fafc" font-weight="bold">3. Costs Saved</text>
  <text x="445" y="175" font-family="Arial" font-size="12" fill="#cbd5e1">• Expenses eliminated from old activity</text>
  <text x="445" y="195" font-family="Arial" font-size="12" fill="#cbd5e1">• e.g. No longer buying old feeds or spray</text>

  <!-- Quadrant 4: Extra Revenue -->
  <text x="430" y="265" font-family="Arial" font-size="15" fill="#f8fafc" font-weight="bold">4. Extra Revenue Gained</text>
  <text x="445" y="295" font-family="Arial" font-size="12" fill="#cbd5e1">• Fresh income generated by new enterprise</text>
  <text x="445" y="315" font-family="Arial" font-size="12" fill="#cbd5e1">• e.g. Expected sales value of new harvest</text>

  <!-- Bottom Result Box -->
  <rect x="150" y="415" width="500" height="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="10"/>
  <text x="400" y="445" font-family="Arial" font-size="14" fill="#38bdf8" font-weight="bold" text-anchor="middle">Net Economic Effect = Total Credits (3+4) - Total Debits (1+2)</text>
</svg>"""


# 5. Risk Management & Credit Classification Matrix
SVG_RISK_CREDIT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Agricultural Credit Terms & Risk Mitigation Framework</text>

  <!-- Three Credit Boxes -->
  <rect x="60" y="75" width="200" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="10"/>
  <text x="160" y="105" font-family="Arial" font-size="15" fill="#38bdf8" font-weight="bold" text-anchor="middle">SHORT-TERM CREDIT</text>
  <text x="160" y="130" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">Repayment: &lt; 1 Year</text>
  <text x="75" y="160" font-family="Arial" font-size="11" fill="#cbd5e1">• Seeds &amp; Fertilizers</text>
  <text x="75" y="180" font-family="Arial" font-size="11" fill="#cbd5e1">• Animal Feeds &amp; Fuel</text>
  <text x="75" y="200" font-family="Arial" font-size="11" fill="#cbd5e1">• Seasonal Hired Labour</text>

  <rect x="300" y="75" width="200" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5" rx="10"/>
  <text x="400" y="105" font-family="Arial" font-size="15" fill="#f59e0b" font-weight="bold" text-anchor="middle">MEDIUM-TERM CREDIT</text>
  <text x="400" y="130" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">Repayment: 2 to 5 Years</text>
  <text x="315" y="160" font-family="Arial" font-size="11" fill="#cbd5e1">• Grade Dairy Livestock</text>
  <text x="315" y="180" font-family="Arial" font-size="11" fill="#cbd5e1">• Paddock Fencing</text>
  <text x="315" y="200" font-family="Arial" font-size="11" fill="#cbd5e1">• Knapsack &amp; Light Tools</text>

  <rect x="540" y="75" width="200" height="150" fill="#1e293b" stroke="#4ade80" stroke-width="2.5" rx="10"/>
  <text x="640" y="105" font-family="Arial" font-size="15" fill="#4ade80" font-weight="bold" text-anchor="middle">LONG-TERM CREDIT</text>
  <text x="640" y="130" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">Repayment: Up to 15+ Yrs</text>
  <text x="555" y="160" font-family="Arial" font-size="11" fill="#cbd5e1">• Land Purchase</text>
  <text x="555" y="180" font-family="Arial" font-size="11" fill="#cbd5e1">• Tractor &amp; Heavy Machinery</text>
  <text x="555" y="200" font-family="Arial" font-size="11" fill="#cbd5e1">• Irrigation Schemes</text>

  <!-- Risk Mitigation Banner -->
  <rect x="60" y="260" width="680" height="185" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="12"/>
  <text x="400" y="295" font-family="Arial" font-size="16" fill="#f8fafc" font-weight="bold" text-anchor="middle">Core Risk &amp; Uncertainty Mitigation Strategies</text>

  <text x="90" y="330" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold">1. Diversification:</text>
  <text x="230" y="330" font-family="Arial" font-size="12" fill="#cbd5e1">Mixing crop and livestock enterprises to balance profits.</text>

  <text x="90" y="360" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold">2. Contracting:</text>
  <text x="230" y="360" font-family="Arial" font-size="12" fill="#cbd5e1">Locking in guaranteed selling prices before planting.</text>

  <text x="90" y="390" font-family="Arial" font-size="13" fill="#f59e0b" font-weight="bold">3. Insurance:</text>
  <text x="230" y="390" font-family="Arial" font-size="12" fill="#cbd5e1">Transferring hail, drought, or flood loss risks to underwriters.</text>

  <text x="90" y="420" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold">4. Input Rationing:</text>
  <text x="230" y="420" font-family="Arial" font-size="12" fill="#cbd5e1">Applying conservative input levels during high-risk seasons.</text>
</svg>"""


# =============================================================================
# LESSON DATA DICTIONARIES
# =============================================================================

LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Agriculture, National Income, and Production Resources",
    "lesson_title": "Agriculture, National Income, and Production Resources",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Agricultural Production Economics",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the concepts of national income (GDP, GNP, and per capita income).\n"
                            "- Detail the circular flow of income between households, firms, and the government.\n"
                            "- Describe the four primary factors of production (land, labour, capital, management).\n"
                            "- Evaluate factor productivity and state strategies to improve resource performance on a commercial farm."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "National Income Definitions",
                    "content": {
                        "text": (
                            "- **National Income:** The total monetary earnings from goods and services produced by a country over one year.\n"
                            "- **Gross Domestic Product (GDP):** The total value of all goods and services produced strictly within a country's borders in one year.\n"
                            "- **Gross National Product (GNP):** The sum of GDP plus net income earned from abroad (inflows minus foreign investor outflows).\n"
                            "- **Per Capita Income:** Gross National Income divided by the country's total population."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Understanding National Income & Per Capita Income",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Pedagogical Note: Limitations of Per Capita Income",
                    "content": {
                        "text": (
                            "Per Capita Income is calculated as:\n"
                            "**Per Capita Income = Gross National Income / Total Population**\n\n"
                            "**Critical Exam Note:** Students must understand that per capita income is **not** an accurate measure of individual economic well-being. "
                            "It represents a mathematical average that assumes wealth is distributed perfectly equally, completely concealing income inequality "
                            "and poverty levels between high and low earners."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Circular Flow of Income",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Circular Flow of Income Diagram",
                    "content": {
                        "text": "Schematic diagram illustrating the closed-loop financial and resource flow between Households, Processing Firms, and Government.",
                        "svg": SVG_CIRCULAR_FLOW
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Detailed Mechanism of Circular Flow",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Four Stages of Circular Flow",
                    "content": {
                        "text": (
                            "1. **Factor Supply:** Households supply raw productive resources (land, labour, capital) to processing firms.\n"
                            "2. **Factor Income:** Firms pay households wages, land rent, interest, and profits for these factors.\n"
                            "3. **Consumption Expenditure:** Households spend cash income to purchase manufactured goods and processed foods from firms.\n"
                            "4. **Public Reinvestment:** The government levies taxes on household income and firm profits to fund public infrastructure (roads, water, extension services)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "The Four Factors of Production",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Characteristics of Production Factors",
                    "content": {
                        "headers": ["Factor", "Primary Characteristics", "Measurement Unit", "Kenyan Agricultural Example"],
                        "rows": [
                            ["Land", "Geographically fixed, natural, variable fertility", "Acres/Hectares, Soil Tests", "Crop fields, river basins, pastures"],
                            ["Labour", "Perishable, cannot be stored, variable quality", "Man-hours, Man-days", "Tractor drivers, weeders, hand milkers"],
                            ["Capital", "Man-made, depreciates, fixed or working", "Shillings, Input Units", "Tractors, fertilizers, bank cash"],
                            ["Management", "Non-physical, coordinating force, risk-bearing", "Net Profit Output", "Farm manager budgeting and marketing"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Capital Types: Fixed, Working, and Liquid",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Classification of Capital Assets",
                    "content": {
                        "text": (
                            "- **Fixed (Durable) Capital:** Long-lasting assets used in multiple production cycles (e.g., tractors, permanent sheds, fences).\n"
                            "- **Working Capital:** Consumable inputs completely used up in a single production cycle (e.g., fertilizers, seeds, diesel fuel).\n"
                            "- **Liquid Capital:** Fluid financial assets readily usable for purchases (e.g., physical cash, bank deposits)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Improving Factor Productivity",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Strategies for Enhancing Factor Productivity",
                    "content": {
                        "text": (
                            "**Land Productivity:** Apply organic manure or chemical fertilizers based on soil testing, and establish irrigation systems.\n\n"
                            "**Labour Productivity:** Train workers on modern farming methods, provide proper healthcare and nutrition, and offer performance incentives.\n\n"
                            "**Capital Productivity:** Adopt efficient mechanical technologies (tractor implements) and service machinery regularly to prevent downtime.\n\n"
                            "**Management Productivity:** Keep accurate farm accounts, utilize partial and complete budgets, and enroll in agricultural extension courses."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Interactive Classification Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Classifying Factors of Production",
                    "content": {
                        "text": "Classify the following farm items into their correct Factor of Production category: (1) Soil fertility in a pasture, (2) A 100-watt brooder bulb, (3) A hired stockman, (4) A decision to switch crop enterprises.",
                        "options": [
                            "A: (1) Land, (2) Fixed Capital, (3) Labour, (4) Management",
                            "B: (1) Capital, (2) Working Capital, (3) Management, (4) Labour",
                            "C: (1) Land, (2) Liquid Capital, (3) Labour, (4) Land",
                            "D: (1) Management, (2) Fixed Capital, (3) Labour, (4) Capital"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Natural soil properties belong to Land. Durable equipment (bulb) is Fixed Capital. Human effort is Labour. Decision-making and risk-taking belong to Management."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. National income measures total annual economic output (GDP within borders, GNP including net foreign income).\n"
                            "2. Income flows continuously between households (factor suppliers) and firms (product providers).\n"
                            "3. Agricultural production requires combining Land, Labour, Capital, and Management in optimal proportions."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Essay Model Answer: Factors of Production (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Identify the four factors of production in agriculture, and for each factor, describe one specific way a farmer can improve its productivity. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Land:** Natural resource with fixed supply. *Productivity Improvement:* Apply organic manure or inorganic fertilizers based on soil testing, or install irrigation systems.\n"
                            "2. **Labour:** Human effort measured in man-hours. *Productivity Improvement:* Provide technical training on modern techniques, ensure good healthcare and nutrition, or pay performance incentives.\n"
                            "3. **Capital:** Man-made assets. *Productivity Improvement:* Mechanize farm operations using modern implements and maintain equipment regularly.\n"
                            "4. **Management:** Decision-making and risk-bearing. *Productivity Improvement:* Maintain accurate accounting records, construct farm budgets, and attend extension seminars."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Production Functions, Marginal Products, and Production Zones",
    "lesson_title": "Production Functions, Marginal Products, and Production Zones",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Input-Output Relationships",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define a production function and calculate Marginal Product (MP) and Average Product (AP).\n"
                            "- State and interpret the Law of Diminishing Returns.\n"
                            "- Identify the boundaries and economic characteristics of Zones I, II, and III.\n"
                            "- Determine the rational level of input application to maximize yields safely."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Key Production Function Terms",
                    "content": {
                        "text": (
                            "- **Production Function:** The physical relationship between variable inputs and final outputs.\n"
                            "- **Total Product (TP):** The total physical output produced from a given input quantity.\n"
                            "- **Marginal Product (MP):** The additional output resulting from adding one additional unit of variable input.\n"
                            "- **Average Product (AP):** Total Product divided by input quantity (TP / Input)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Law of Diminishing Returns",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Statement of the Law",
                    "content": {
                        "text": (
                            "**Law of Diminishing Returns:** If successive units of one variable input are added to fixed quantities of other inputs, "
                            "a point is eventually reached where the additional output (Marginal Product) per additional unit of input begins to decline.\n\n"
                            "**Example:** Adding fertilizer to a fixed 1-acre maize field boosts yield up to an optimal level; excess fertilizer eventually burns roots and reduces total yield."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Production Function Curves Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Production Curves & Three Production Zones",
                    "content": {
                        "text": "Detailed graphical representation showing Total Product (TP), Average Product (AP), and Marginal Product (MP) curves divided into Zones I, II, and III.",
                        "svg": SVG_PRODUCTION_ZONES
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Analyzing the Three Production Zones",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Characteristics of Production Zones",
                    "content": {
                        "headers": ["Zone", "Boundary Limits", "Physical Status", "Economic Decision"],
                        "rows": [
                            ["Zone I (Irrational)", "Origin (0) to MP = AP boundary", "Underutilized fixed resources; MP > AP", "Irrational to stop; keep adding input."],
                            ["Zone II (Rational)", "From MP = AP boundary to MP = 0", "Resource efficiency optimized; positive MP", "Economically rational zone to operate."],
                            ["Zone III (Irrational)", "Beyond MP = 0 boundary (MP < 0)", "Over-saturation/toxicity; total output falls", "Irrational; wasting money to destroy output."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Example: Pig Concentrate Feeding",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Calculating Marginal Product in Pig Feeding",
                    "content": {
                        "text": (
                            "**Formula:** MP = Change in Total Weight / Change in Feed Input\n\n"
                            "**Data Analysis:**\n"
                            "- Feed 0 to 10 kg: Weight 212 to 222 kg -> MP = (222 - 212) / (10 - 0) = 1.0 kg per feed unit\n"
                            "- Feed 10 to 20 kg: Weight 222 to 238 kg -> MP = (238 - 222) / (20 - 10) = 1.6 kg per feed unit (Peak MP)\n"
                            "- Feed 20 to 30 kg: Weight 238 to 251 kg -> MP = (251 - 238) / (30 - 20) = 1.3 kg per feed unit\n"
                            "- Feed 30 to 40 kg: Weight 251 to 261 kg -> MP = (261 - 251) / (40 - 30) = 1.0 kg per feed unit\n"
                            "- Feed 40 to 50 kg: Weight 261 to 269 kg -> MP = (269 - 261) / (50 - 40) = 0.8 kg per feed unit\n\n"
                            "**Observation:** Beyond 20 units of feed, Marginal Product steadily declines from 1.6 kg down to 0.8 kg, illustrating Diminishing Returns."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Example: NPK Fertilizer Trial on Maize",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Mapping NPK Trial into Production Zones",
                    "content": {
                        "text": (
                            "**Fertilizer Application Trial (1-Hectare Plot):**\n"
                            "- NPK 30 to 120 kg: Yield increases from 10 to 56 bags -> **Zone I (Irrational)**\n"
                            "- NPK 150 kg: Yield reaches 63 bags (MP = 7 bags) -> **Zone II (Rational Start)**\n"
                            "- NPK 180 kg: Yield reaches 65 bags (MP = 2 bags) -> **Zone II (Rational)**\n"
                            "- NPK 210 kg: Yield reaches 65 bags (MP = 0, Peak TP) -> **Zone II (Rational End)**\n"
                            "- NPK 240 kg: Yield drops to 60 bags (MP = -5 bags) -> **Zone III (Irrational)**\n\n"
                            "**Decision:** The farmer must operate strictly between 150 kg and 210 kg of NPK."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Calculation Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Marginal Product Calculation",
                    "content": {
                        "text": "A poultry farmer increases layers' mash from 80 kg to 90 kg daily. Total egg output rises from 400 eggs to 460 eggs. What is the Marginal Product per kg of added feed?",
                        "options": [
                            "A: 60 eggs per kg of feed",
                            "B: 6 eggs per kg of feed",
                            "C: 460 eggs",
                            "D: 0.15 kg per egg"
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Change in output = 460 - 400 = 60 eggs. Change in input = 90 - 80 = 10 kg. MP = 60 / 10 = 6 eggs per kg of added feed."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Zone Boundary Rules Summary",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Boundary Intersections",
                    "content": {
                        "text": (
                            "- **Boundary 1 (Zone I / Zone II transition):** Occurs at the point where Marginal Product equals Average Product (MP = AP). Average Product is at its maximum.\n"
                            "- **Boundary 2 (Zone II / Zone III transition):** Occurs at the point where Marginal Product equals Zero (MP = 0). Total Product is at its absolute maximum."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. Production functions map inputs to outputs.\n"
                            "2. The Law of Diminishing Returns causes MP to decline after an initial peak.\n"
                            "3. Commercial farmers must operate exclusively within Zone II (between MP = AP and MP = 0)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Analyzing Input Transitions (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Nitrogen fertilizer applied to wheat increases yield from 35 to 38 bags when increased from 120 kg to 150 kg, but drops to 36 bags when increased from 150 kg to 180 kg. Identify the zones and evaluate the economic outcomes. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Transition 1 (120 to 150 kg NPK):** Yield increases by 3 bags (MP = +3/30 = +0.1 bag/kg). Represents **Zone II (Rational Zone)** where total output rises efficiently.\n"
                            "2. **Transition 2 (150 to 180 kg NPK):** Yield drops by 2 bags (MP = -2/30 = -0.067 bag/kg). Represents **Zone III (Irrational Zone)**.\n"
                            "3. **Economic Evaluation:** Transition 2 is irrational. The farmer spent additional capital on fertilizer only to chemically damage wheat crops and reduce harvest by 2 bags."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Substitution, Equimarginal Returns, and Profit Maximisation",
    "lesson_title": "Substitution, Equimarginal Returns, and Profit Maximisation",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Economic Substitution",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Apply the Principle of Substitution to find least-cost input combinations.\n"
                            "- Calculate the Marginal Rate of Substitution (MRS) and compare it against the Price Ratio.\n"
                            "- Apply the Principle of Equimarginal Returns under capital rationing.\n"
                            "- State the conditions for farm profit maximisation."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Core Principles Defined",
                    "content": {
                        "text": (
                            "- **Principle of Substitution:** It is profitable to substitute a cheaper input for an expensive alternative if output remains constant.\n"
                            "- **Marginal Rate of Substitution (MRS):** The quantity of input X2 replaced per unit increase of input X1 (MRS = Change in X2 / Change in X1).\n"
                            "- **Price Ratio:** The price of input X1 divided by the price of input X2 (Price Ratio = Price of X1 / Price of X2).\n"
                            "- **Least-Cost Combination:** Achieved when MRS = Price Ratio."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Least-Cost Combination Principle",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Tangency Formula for Cost Minimisation",
                    "content": {
                        "text": (
                            "To minimize production costs for a fixed output target:\n"
                            "**MRS (Change in X2 / Change in X1) = Price Ratio (Price of X1 / Price of X2)**\n\n"
                            "Where X1 is the replacement input and X2 is the input being reduced."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Least-Cost Isoquant Graph Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Isoquant & Isocost Tangency Graph",
                    "content": {
                        "text": "Graphical representation showing the point of tangency between an Isoquant curve and an Isocost line for least-cost optimization.",
                        "svg": SVG_LEAST_COST
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Worked Example: Manure vs Phosphate Fertilizer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Calculating Least-Cost Combination",
                    "content": {
                        "text": (
                            "**Given:**\n"
                            "- Price of Phosphate Fertilizer (X1) = KSh 50 per unit\n"
                            "- Price of Farmyard Manure (X2) = KSh 10 per unit\n"
                            "- Price Ratio = 50 / 10 = 5.0\n\n"
                            "**Evaluating Combinations:**\n"
                            "- Combination 1 (1 unit X1, 9 units X2): Total Cost = (1 * 50) + (9 * 10) = KSh 140\n"
                            "- Combination 2 (2 units X1, 4 units X2): MRS = (9 - 4) / (2 - 1) = 5.0. Total Cost = (2 * 50) + (4 * 10) = KSh 140\n"
                            "- Combination 3 (3 units X1, 2.8 units X2): Total Cost = (3 * 50) + (2.8 * 10) = KSh 178\n\n"
                            "**Result:** Combination 2 (2 units X1 and 4 units X2) satisfies MRS = Price Ratio (5.0 = 5.0) and yields the minimum cost of KSh 140."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Principle of Equimarginal Returns",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Capital Rationing & Resource Allocation",
                    "content": {
                        "text": (
                            "When a farmer has limited capital, funds must be allocated among competing enterprises (e.g., dairy, maize, poultry) "
                            "such that the last shilling invested in each enterprise yields the **exact same marginal return**.\n\n"
                            "**Strategy:** Invest available cash step-by-step into the enterprise with the highest marginal return until its return drops (due to diminishing returns) to match the next enterprise."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Assumptions of Profit Maximisation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Three Profit Maximisation Assumptions",
                    "content": {
                        "text": (
                            "1. **Constant Input Costs:** Unit costs of inputs remain unchanged throughout the production cycle.\n"
                            "2. **Constant Produce Prices:** Selling market prices for agricultural products remain constant.\n"
                            "3. **Fixed Costs Ignored:** Only variable operational costs directly involved in the enterprise are considered."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Choose & Calculate Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Least-Cost Combination MRS Calculation",
                    "content": {
                        "text": "The price of Maize Germ (Input X1) is KSh 40 per bag, and Wheat Pollard (Input X2) is KSh 20 per bag. At what Marginal Rate of Substitution (MRS) will a farmer achieve least-cost combination?",
                        "options": [
                            "A: MRS = 0.5",
                            "B: MRS = 2.0",
                            "C: MRS = 800",
                            "D: MRS = 60"
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Least-cost combination occurs where MRS = Price Ratio (Price of X1 / Price of X2). Price Ratio = 40 / 20 = 2.0. Therefore, MRS must equal 2.0."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Net Revenue Optimization Formula",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Net Revenue & Marginal Concepts",
                    "content": {
                        "text": (
                            "- **Net Revenue Method:** Net Revenue = Total Revenue (TR) - Total Cost (TC). Maximum profit occurs where Net Revenue is largest.\n"
                            "- **Marginal Concept Method:** Production is expanded until Marginal Revenue (MR) equals Marginal Cost (MC)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. Least-cost input combination occurs where MRS = Price Ratio.\n"
                            "2. Under limited budgets, Equimarginal Returns requires equalizing the marginal return of the last shilling spent across all enterprises.\n"
                            "3. Profit is maximized when Net Revenue (TR - TC) is at its peak."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Equimarginal Returns Application (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Explain how a farmer with limited capital should utilize the Principle of Equimarginal Returns to allocate resources among poultry, sheep, and potato enterprises. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Definition:** Equimarginal Returns states that the last unit of capital spent in one enterprise must yield a marginal return equal to the last unit spent in all other enterprises.\n"
                            "2. **Step 1:** Calculate estimated marginal returns (profit per shilling spent) for incremental investments in poultry feed, sheep dewormers, and potato fertilizer.\n"
                            "3. **Step 2:** Allocate initial cash sequentially to the enterprise with the highest marginal return (e.g. potato fertilizer returning KSh 2.50 per shilling vs KSh 1.80 for poultry).\n"
                            "4. **Step 3:** As more funds enter potatoes, diminishing returns reduce its marginal return until it matches poultry.\n"
                            "5. **Final State:** Distribute remaining cash across enterprises so that the last shilling spent on potatoes, poultry, and sheep yields identical marginal returns."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Farm Planning and Budgeting",
    "lesson_title": "Farm Planning and Budgeting",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Farm Planning & Budgeting",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 4 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- State 10 essential factors evaluated when drawing up a farm plan.\n"
                            "- Distinguish between Partial Budgets and Complete Budgets.\n"
                            "- Construct a 4-quadrant Partial Budget and calculate Net Economic Effect.\n"
                            "- Prepare a Complete Budget template for credit acquisition."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Planning vs Budgeting Defined",
                    "content": {
                        "text": (
                            "- **Farm Planning:** Establishing farm objectives and outlining physical/economic pathways to achieve them.\n"
                            "- **Farm Budgeting:** Estimating future financial incomes and expenditures for a proposed farm plan."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Ten Essential Factors in Farm Planning",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "10 Key Factors for Farm Planning",
                    "content": {
                        "text": (
                            "1. **Farm Size:** Restricts potential crop and livestock scale.\n"
                            "2. **Environmental Conditions:** Climate, soil fertility, rainfall, terrain.\n"
                            "3. **Labour Availability:** Wages and local skilled labour supply.\n"
                            "4. **Farmer's Objectives:** Personal preferences and commercial targets.\n"
                            "5. **Possible Enterprises:** Competing crop and livestock options.\n"
                            "6. **Market Trends:** Produce demand and price stability.\n"
                            "7. **Input Costs & Availability:** Access to seed, fertilizer, and machinery.\n"
                            "8. **Government Policies:** Subsidies, tax laws, and land regulations.\n"
                            "9. **Security:** Protection against theft, vermin, and vandalism.\n"
                            "10. **Transport Infrastructure:** Road access to urban market centers."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Partial Budget 4-Quadrant Framework Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Partial Budgeting Framework",
                    "content": {
                        "text": "Four-quadrant structural template showing Debits (Extra Costs + Revenue Forgone) balancing against Credits (Costs Saved + Extra Revenue).",
                        "svg": SVG_PARTIAL_BUDGET
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Partial Budgeting Rules & Formula",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Net Economic Effect Calculation",
                    "content": {
                        "text": (
                            "A Partial Budget analyzes minor, localized farm changes (affecting variable costs only).\n\n"
                            "**Formula:**\n"
                            "**Net Economic Effect = Total Credits (Costs Saved + Extra Revenue) - Total Debits (Extra Costs + Revenue Forgone)**\n\n"
                            "**Decision Rule:** If Net Economic Effect is positive, the change is financially viable."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Example: Partial Budget for Pasture Change",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Replacing Natural Grazing with Rhodes Grass Hay",
                    "content": {
                        "text": (
                            "**Debits (Costs Incurred & Revenue Lost):**\n"
                            "- Extra Costs: Rhodes grass seed & land prep = KSh 12,000\n"
                            "- Revenue Forgone: Milk loss from 2 displaced cows = KSh 15,000\n"
                            "- **Total Debits = KSh 27,000**\n\n"
                            "**Credits (Costs Saved & Revenue Gained):**\n"
                            "- Costs Saved: Commercial hay purchases eliminated = KSh 18,000\n"
                            "- Extra Revenue: Surplus Rhodes hay bale sales = KSh 22,000\n"
                            "- **Total Credits = KSh 40,000**\n\n"
                            "**Net Economic Effect = 40,000 - 27,000 = +KSh 13,000 (Profitable Change)**"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Complete Farm Budgeting Structure",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Complete Farm Budgeting Overview",
                    "content": {
                        "headers": ["Category", "Expenditure Items (Debits)", "Receipt Items (Credits)"],
                        "rows": [
                            ["Fixed Capital Costs", "Land rent, permanent shed maintenance, machinery depreciation", "N/A"],
                            ["Variable Costs", "Seed, fertilizers, feeds, fuel, hired labour wages", "N/A"],
                            ["Revenues", "N/A", "Maize crop sales, milk sales, poultry egg sales, machine hire"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Choose Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Selecting Budget Type",
                    "content": {
                        "text": "A coffee estate in Kiambu plans to clear 50 hectares of coffee trees, construct greenhouses, and install pivot irrigation for cut flowers. What type of budget is required?",
                        "options": [
                            "A: Partial Budget",
                            "B: Complete Budget",
                            "C: Cash Book",
                            "D: Local Purchase Order"
                        ],
                        "correct_answer_index": 1,
                        "explanation": "A Complete Budget is mandatory when executing a major structural reorganization that affects both fixed and variable costs across the entire enterprise."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Importance of Budgeting in Securing Credit",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Financial Lenders Require Budgets",
                    "content": {
                        "text": (
                            "Commercial banks and the Agricultural Finance Corporation (AFC) mandate complete farm budgets prior to advancing loans because budgets:\n"
                            "1. Demonstrate estimated future farm revenues.\n"
                            "2. Prove the farm's cash flow capacity to service loan interest and principal.\n"
                            "3. Pinpoint unprofitable farm operations before capital is deployed."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. Farm planning establishes long-term physical and economic targets.\n"
                            "2. Partial budgeting evaluates localized minor changes using a 4-quadrant balance.\n"
                            "3. Complete budgeting inventories all fixed and variable costs for major reorganizations and credit applications."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Partial Budgeting Framework (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Outline the core structure of a partial farm budget, detailing the four specific types of financial changes analyzed. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Debit Quadrant 1 (Extra Costs):** Fresh expenses introduced by the new activity (e.g. new seeds, sprays).\n"
                            "2. **Debit Quadrant 2 (Revenue Forgone):** Existing income lost by stopping the old activity.\n"
                            "3. **Credit Quadrant 1 (Costs Saved):** Expenses eliminated from the old activity.\n"
                            "4. **Credit Quadrant 2 (Extra Revenue):** Fresh income generated by the new activity.\n"
                            "5. **Decision Rule:** Calculate Net Economic Effect = Total Credits (Costs Saved + Extra Revenue) - Total Debits (Extra Costs + Revenue Forgone). Implement change if result is positive."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Agricultural Support Services, Credit, and Risk Management",
    "lesson_title": "Agricultural Support Services, Credit, and Risk Management",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Institutional Support & Risk",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 5 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Categorize credit by repayment terms (Short, Medium, Long-Term) and list credit sources.\n"
                            "- Identify institutional support services (Extension, KALRO research, AI, Veterinary).\n"
                            "- Differentiate between Risk and Uncertainty.\n"
                            "- Describe 6 practical risk mitigation strategies used in commercial farming."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Key Terminology Defined",
                    "content": {
                        "text": (
                            "- **Credit:** Borrowed capital advanced to farmers for projects, repayable with interest.\n"
                            "- **Risk:** A situation where the probability of a loss can be calculated from past data.\n"
                            "- **Uncertainty:** Complete unpredictability where future outcomes cannot be calculated.\n"
                            "- **Diversification:** Engaging in multiple different enterprises to cushion losses."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Classification of Agricultural Credit",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Credit Categories by Repayment Term",
                    "content": {
                        "headers": ["Credit Category", "Repayment Timeline", "Primary Agricultural Purpose", "Specific Examples"],
                        "rows": [
                            ["Short-Term Credit", "Within 1 year", "Quick-turnover seasonal inputs", "Hybrid seeds, fertilizers, feeds, fuel"],
                            ["Medium-Term Credit", "2 to 5 years", "Semi-durable capital improvements", "Grade dairy cows, paddock fences, sprayers"],
                            ["Long-Term Credit", "Up to 15+ years", "Permanent high-value capital assets", "Buying land, tractors, commercial irrigation"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Risk & Credit Framework Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Credit Terms & Risk Mitigation Framework",
                    "content": {
                        "text": "Structural matrix mapping Short, Medium, and Long-Term credit terms alongside 4 core risk mitigation strategies.",
                        "svg": SVG_RISK_CREDIT
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Sources of Agricultural Credit in Kenya",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Major Credit Institutions",
                    "content": {
                        "text": (
                            "1. **Agricultural Finance Corporation (AFC):** Government parastatal providing specialized low-interest farm loans.\n"
                            "2. **Cooperative Societies & SACCOs:** Provide crop-advance loans and input credit to member farmers.\n"
                            "3. **Commercial Banks:** Advance short and medium-term loans against physical collateral.\n"
                            "4. **Commodity Boards:** Provide input credit deducted directly from produce payouts (e.g. KTDA, Pyrethrum Board)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Institutional Support Services",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Essential Agricultural Support Services",
                    "content": {
                        "text": (
                            "- **Extension Services:** On-farm field training by officers to disseminate scientific techniques.\n"
                            "- **Agricultural Research (KALRO):** Breeding high-yield, drought-tolerant crop varieties and disease-resistant livestock.\n"
                            "- **Artificial Insemination (AI):** Providing high-grade bull semen for genetic breed improvement.\n"
                            "- **Veterinary Services:** Disease vaccination, tick control, and clinical treatment."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Risk vs Uncertainty in Farming",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Differentiating Risk and Uncertainty",
                    "content": {
                        "text": (
                            "**Risk:** Measurable divergence between expected and actual outcome. Examples: Price fluctuations, pest outbreaks, weather variations.\n\n"
                            "**Uncertainty:** Unmeasurable unpredictability. Examples: Sudden global market collapse, new unknown crop virus, land tenure law changes."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Risk Adjustment & Mitigation Strategies",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Six Risk Mitigation Strategies",
                    "content": {
                        "text": (
                            "1. **Diversification:** Combining multiple crop and livestock enterprises to balance profits.\n"
                            "2. **Enterprise Selection:** Choosing drought-resistant or stable crops (cassava, sorghum).\n"
                            "3. **Contract Farming:** Signing fixed-price supply agreements prior to planting.\n"
                            "4. **Agricultural Insurance:** Transferring drought, hail, or flood losses to insurance underwriters.\n"
                            "5. **Input Rationing:** Applying conservative input rates in high-risk seasons to minimize capital exposure.\n"
                            "6. **Flexibility:** Constructing multi-purpose farm structures that can adapt to changing market trends."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Interactive Matching Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Matching Projects to Credit Terms",
                    "content": {
                        "text": "Match the farm project to its correct credit term: (1) Constructing a permanent concrete dip, (2) Buying layers' mash, (3) Purchasing grade dairy heifers.",
                        "options": [
                            "A: (1) Long-Term, (2) Short-Term, (3) Medium-Term",
                            "B: (1) Short-Term, (2) Medium-Term, (3) Long-Term",
                            "C: (1) Medium-Term, (2) Short-Term, (3) Long-Term",
                            "D: (1) Long-Term, (2) Medium-Term, (3) Short-Term"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Permanent concrete structures require Long-Term credit. Feed is a seasonal consumable needing Short-Term credit. Livestock purchases match Medium-Term credit (2-5 years)."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. Credit terms must match asset durability: Short-Term (<1yr), Medium-Term (2-5yrs), Long-Term (15+yrs).\n"
                            "2. Key support services include Extension, KALRO research, AI, and Veterinary care.\n"
                            "3. Risk and uncertainty are cushioned using Diversification, Contracting, Insurance, and Input Rationing."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Risk Mitigation Strategies (12 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Identify six management practices a farmer can implement to adjust to and minimize the impact of risks and uncertainties. (12 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Diversification:** Growing diverse crops and keeping livestock simultaneously so one failure is cushioned by another.\n"
                            "2. **Selecting Certain Enterprises:** Choosing drought-tolerant, reliable crops (cassava, sorghum) over sensitive cash crops.\n"
                            "3. **Contract Farming:** Signing legal forward contracts with processors to lock in guaranteed produce prices.\n"
                            "4. **Agricultural Insurance:** Purchasing crop/livestock policies to transfer weather or disease risks to insurers.\n"
                            "5. **Input Rationing:** Reducing variable capital expenditure in high-risk seasons to minimize total potential financial loss.\n"
                            "6. **Flexibility:** Designing multi-purpose farm facilities that can switch between enterprises as market demands shift."
                        )
                    }
                }
            ]
        }
    ]
}

TOPIC_4_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA
]
