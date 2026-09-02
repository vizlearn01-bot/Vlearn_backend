import json
import re

SVG_BUDGET_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Personal Budgeting &amp; Opportunity Cost Decision Matrix</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Akinyi's KES 500 Weekly Resource Constraint Case Study</text>

  <!-- Left: Resource Inflow -->
  <g transform="translate(40, 95)">
    <rect width="250" height="150" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="250" height="30" rx="8" fill="#059669"/>
    <text x="125" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">TOTAL AVAILABLE INCOME</text>
    <text x="125" y="75" font-size="28" font-weight="bold" fill="#34d399" text-anchor="middle">KES 500</text>
    <text x="125" y="105" font-size="10" fill="#cbd5e1" text-anchor="middle">Weekly Student Allowance</text>
    <text x="125" y="125" font-size="9.5" fill="#94a3b8" text-anchor="middle">Fixed Resource Constraint</text>
  </g>

  <!-- Right: The Competing Demands Matrix (Total KES 620 -> Deficit!) -->
  <g transform="translate(320, 95)">
    <rect width="600" height="150" rx="10" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="600" height="30" rx="8" fill="#e11d48"/>
    <text x="300" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">UNCONSTRAINED COMPETING DEMANDS (TOTAL = KES 620)</text>

    <text x="25" y="58" font-size="10.5" fill="#e2e8f0">• School Transport: <tspan font-weight="bold" fill="#38bdf8">KES 250</tspan> (Basic Need)</text>
    <text x="25" y="82" font-size="10.5" fill="#e2e8f0">• School Lunch: <tspan font-weight="bold" fill="#38bdf8">KES 150</tspan> (Basic Need)</text>
    <text x="25" y="106" font-size="10.5" fill="#e2e8f0">• Notebook: <tspan font-weight="bold" fill="#38bdf8">KES 70</tspan> (Basic Need)</text>

    <text x="320" y="58" font-size="10.5" fill="#e2e8f0">• Fancy Hair Clip: <tspan font-weight="bold" fill="#f43f5e">KES 100</tspan> (Non-essential Want)</text>
    <text x="320" y="82" font-size="10.5" fill="#e2e8f0">• Trip Savings: <tspan font-weight="bold" fill="#fbbf24">KES 50</tspan> (Future Goal)</text>
    <text x="320" y="125" font-size="11" font-weight="bold" fill="#fda4af">Deficit: KES 120 (Exceeds Budget!)</text>
  </g>

  <!-- Bottom Balanced Allocation Decision -->
  <g transform="translate(40, 270)">
    <rect width="880" height="220" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="880" height="32" rx="10" fill="#0284c7"/>
    <text x="440" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">BALANCED BUDGET ALLOCATION &amp; OPPORTUNITY COST RESOLUTION</text>

    <g transform="translate(20, 50)">
      <!-- Item 1 -->
      <rect x="0" y="0" width="155" height="100" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="77" y="25" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">1. TRANSPORT</text>
      <text x="77" y="50" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">KES 250</text>
      <text x="77" y="75" font-size="9" fill="#10b981" text-anchor="middle">✓ Approved (Need)</text>

      <!-- Item 2 -->
      <rect x="175" y="0" width="155" height="100" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="252" y="25" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">2. LUNCH</text>
      <text x="252" y="50" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">KES 150</text>
      <text x="252" y="75" font-size="9" fill="#10b981" text-anchor="middle">✓ Approved (Need)</text>

      <!-- Item 3 -->
      <rect x="350" y="0" width="155" height="100" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="427" y="25" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">3. NOTEBOOK</text>
      <text x="427" y="50" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">KES 70</text>
      <text x="427" y="75" font-size="9" fill="#10b981" text-anchor="middle">✓ Approved (Need)</text>

      <!-- Item 4 -->
      <rect x="525" y="0" width="155" height="100" rx="6" fill="#1e293b" stroke="#fbbf24"/>
      <text x="602" y="25" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">4. SAVINGS</text>
      <text x="602" y="50" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">KES 30</text>
      <text x="602" y="75" font-size="9" fill="#fbbf24" text-anchor="middle">✓ Adjusted (Goal)</text>

      <!-- Item 5: Sacrificed -->
      <rect x="700" y="0" width="140" height="100" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-dasharray="4"/>
      <text x="770" y="25" font-size="10.5" font-weight="bold" fill="#f43f5e" text-anchor="middle">HAIR CLIP</text>
      <text x="770" y="50" font-size="13" font-weight="bold" fill="#f43f5e" text-anchor="middle">KES 0 (Rejected)</text>
      <text x="770" y="75" font-size="8.5" fill="#fda4af" text-anchor="middle">Opportunity Cost!</text>
    </g>

    <text x="440" y="185" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Total Balanced Allocation: KES 250 + 150 + 70 + 30 = KES 500 (100% Balanced with Zero Debt)</text>
  </g>
</svg>"""

SVG_NEEDS_VS_WANTS_SPECTRUM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Economic Spectrum: Basic Needs vs. Secondary Wants</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Distinguishing Essential Survival Commodities from Discretionary Comforts and Luxuries</text>

  <!-- Left Column: Basic Needs -->
  <g transform="translate(50, 95)">
    <rect width="410" height="380" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="410" height="36" rx="10" fill="#059669"/>
    <text x="205" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. BASIC NEEDS (ESSENTIAL FOR SURVIVAL)</text>

    <g transform="translate(20, 55)">
      <rect width="370" height="60" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#34d399">• Food, Clean Water &amp; Nutrition</text>
      <text x="15" y="44" font-size="9.5" fill="#cbd5e1">Biological fuel necessary for metabolism, growth, and living.</text>
    </g>

    <g transform="translate(20, 125)">
      <rect width="370" height="60" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#34d399">• Shelter &amp; Physical Protection</text>
      <text x="15" y="44" font-size="9.5" fill="#cbd5e1">Housing and safety against environmental hazards and weather.</text>
    </g>

    <g transform="translate(20, 195)">
      <rect width="370" height="60" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#34d399">• Clothing, Healthcare &amp; Sanitation</text>
      <text x="15" y="44" font-size="9.5" fill="#cbd5e1">Bodily warmth, dignity, medical treatment, and disease prevention.</text>
    </g>

    <g transform="translate(20, 270)">
      <rect width="370" height="85" rx="6" fill="#064e3b" stroke="#10b981"/>
      <text x="185" y="22" font-size="10.5" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Core Economic Characteristic</text>
      <text x="15" y="45" font-size="9.5" fill="#ffffff">• Non-negotiable and limited in physical quantity.</text>
      <text x="15" y="65" font-size="9.5" fill="#ffffff">• Failure to satisfy leads to illness, malnutrition, or death.</text>
    </g>
  </g>

  <!-- Right Column: Secondary Wants -->
  <g transform="translate(500, 95)">
    <rect width="410" height="380" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="410" height="36" rx="10" fill="#d97706"/>
    <text x="205" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SECONDARY WANTS (COMFORTS &amp; LUXURY)</text>

    <g transform="translate(20, 55)">
      <rect width="370" height="60" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#fbbf24">• Entertainment &amp; Gaming Devices</text>
      <text x="15" y="44" font-size="9.5" fill="#cbd5e1">Video games, movie streaming subscriptions, and leisure outings.</text>
    </g>

    <g transform="translate(20, 125)">
      <rect width="370" height="60" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#fbbf24">• Designer Fashion &amp; Accessories</text>
      <text x="15" y="44" font-size="9.5" fill="#cbd5e1">Branded clothing, luxury jewelry, fancy hair clips, and perfume.</text>
    </g>

    <g transform="translate(20, 195)">
      <rect width="370" height="60" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#fbbf24">• Gourmet Snacks &amp; Luxury Treats</text>
      <text x="15" y="44" font-size="9.5" fill="#cbd5e1">Sodas, confectionery, restaurant dining, and convenience snacks.</text>
    </g>

    <g transform="translate(20, 270)">
      <rect width="370" height="85" rx="6" fill="#78350f" stroke="#f59e0b"/>
      <text x="185" y="22" font-size="10.5" font-weight="bold" fill="#fde68a" text-anchor="middle">Core Economic Characteristic</text>
      <text x="15" y="45" font-size="9.5" fill="#ffffff">• Unlimited, dynamic, and expand with income levels.</text>
      <text x="15" y="65" font-size="9.5" fill="#ffffff">• Enhances comfort, but failure to satisfy does NOT threaten life.</text>
    </g>
  </g>
</svg>"""

lesson_6_data = {
    "unit_order": 1,
    "unit_name": "The Role of Money in Day-to-Day Life",
    "unit_description": "Evaluating how money shapes daily household, consumer, and enterprise decisions, mastering basic needs versus wants, calculating opportunity cost, and constructing balanced personal budgets under scarcity constraints.",
    "lesson_title": "The Role of Money in Day-to-Day Life",
    "pages": [
        # Page 1: Hook & Core Learning Goals
        {
            "page_number": 1,
            "page_title": "Money in Daily Life: Scarcity, Choice, and Financial Foundations",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Consumer Decision-Making: Purchasing School Stationery and Books",
                    "content": {
                        "title": "Consumer Decision-Making: Purchasing School Stationery and Books",
                        "caption": "A student purchasing exercise books and revision stationery in a local shop. Because personal money is always limited, every daily purchasing decision requires balancing essential needs against discretionary wants.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/2/29/Stationery_Wholesale_Shop_notebooks.jpg",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Lesson Objectives: Navigating Daily Financial Decisions",
                    "content": {
                        "title": "What We Will Master in This Lesson",
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish rigorously between **Basic Needs** (survival essentials) and **Secondary Wants** (comfort, luxury, and entertainment).\n- Define the economic concept of **Opportunity Cost** and identify real-life spending trade-offs.\n- Construct a balanced **Personal Budget** under fixed income constraints using systematic prioritization.\n- Apply the 6-step mathematical worked calculation framework to solve student pocket-money allocation problems.\n- Connect individual financial discipline to large-scale commercial and corporate enterprise budget management."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Ubiquitous Role of Money in Day-to-Day Life",
                    "content": {
                        "title": "Why Daily Money Management Matters",
                        "text": "Every single day, from the moment you wake up to the time you sleep, money touches every facet of modern life. Whether it is paying bus fare to school, buying lunch, purchasing an exercise book, or saving a few coins for a future school trip, money acts as the bridge connecting human desires with scarce economic resources.\n\nHowever, money is **always limited and finite**—for students, households, and multi-billion-shilling enterprises alike. Because financial resources cannot satisfy unlimited human desires, every individual is forced to make deliberate economic choices. Understanding the role of money in day-to-day life is not merely an academic topic; it is the foundational life skill that establishes financial security and prevents debt distress."
                    }
                }
            ]
        },
        # Page 2: Basic Needs vs. Wants
        {
            "page_number": 2,
            "page_title": "Basic Needs vs. Wants: Prioritizing Survival and Comfort",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Basic Needs",
                    "content": {
                        "term": "Basic Needs",
                        "definition": "Essential goods and services indispensable for human survival, physical health, and minimum human dignity (such as clean drinking water, nutritious food, adequate shelter, protective clothing, and basic healthcare)."
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Secondary Wants",
                    "content": {
                        "term": "Secondary Wants",
                        "definition": "Desires for goods, services, or experiences that go beyond biological survival to provide comfort, entertainment, prestige, or luxury (such as designer footwear, high-end smartphones, video games, and fancy hair accessories)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "The Economic Spectrum: Basic Needs vs. Secondary Wants",
                    "content": {
                        "svg_content": SVG_NEEDS_VS_WANTS_SPECTRUM,
                        "caption": "Comparison of Basic Needs (essential, finite, life-sustaining) versus Secondary Wants (discretionary, expandable, comfort-enhancing)."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Golden Rule of Resource Allocation",
                    "content": {
                        "title": "Biological Survival Takes Precedence Over Comfort",
                        "text": "Human demands fall along a strict hierarchy:\n\n- **Basic Needs (Non-Negotiable)**:\n  - **Food & Clean Water**: Fuel cellular metabolism and sustain life.\n  - **Shelter & Housing**: Protect against the elements and ensure physical safety.\n  - **Clothing & Healthcare**: Prevent illness, provide dignity, and sustain productive daily activity.\n\n- **Wants (Negotiable & Expandable)**:\n  - Wants are unlimited, recurring, and heavily stimulated by marketing and peer pressure.\n  - Satisfying a want makes life more enjoyable, but omitting a want does **not** threaten biological existence.\n\n*The Golden Rule of Personal Finance*: When allocating limited cash inflows, **Basic Needs must always be fully funded before any money is allocated to Wants**."
                    }
                }
            ]
        },
        # Page 3: Opportunity Cost
        {
            "page_number": 3,
            "page_title": "Opportunity Cost: The Hidden Price of Every Financial Decision",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Opportunity Cost",
                    "content": {
                        "term": "Opportunity Cost",
                        "definition": "The value of the next best alternative forgone or sacrificed when a decision is made to allocate scarce economic resources (money, time, or labour) to one chosen alternative over another."
                    }
                },
                {
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "title": "The Trade-Off Relationship",
                    "content": {
                        "formula": "\\text{Opportunity Cost} = \\text{Value of Next Best Alternative Sacrificed}",
                        "text": "* **Income Constraint**: Total Expenditure $\\le$ Available Income ($E \\le Y$)\n* **Decision Rule**: Choosing to spend cash on Item $A$ with price $P_A$ means you forfeit the utility of Item $B$ with price $P_B$.\n* **Economic Reality**: Money spent on an impulse want is cash that can no longer fund an essential academic need or yield future compound interest in savings."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "There is No Such Thing as a Free Choice",
                    "content": {
                        "title": "Explicit Price vs. Implicit Economic Cost",
                        "text": "Whenever you hold a KES 100 note, you possess purchasing power over multiple competing goods. If you spend that KES 100 on a soda, the true economic cost is not just the paper banknote—it is the school notebook, bus ticket, or savings balance that you had to forfeit.\n\nEvery economic transaction carries two costs:\n1. **The Explicit Monetary Cost ($P_m$)**: The exact cash deducted from your wallet.\n2. **The Implicit Opportunity Cost ($C_{opp}$)**: The alternative satisfaction, learning utility, or safety buffer you surrendered.\n\nMastering financial discipline means constantly asking: *'If I spend this money now on a short-term desire, what critical future benefit am I sacrificing?'*"
                    }
                }
            ]
        },
        # Page 4: Visualizing the Budget Matrix (SVG)
        {
            "page_number": 4,
            "page_title": "Personal Budget Architecture & Spending Optimization",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Personal Budgeting & Opportunity Cost Decision Matrix",
                    "content": {
                        "svg_content": SVG_BUDGET_MATRIX,
                        "caption": "Decision-making matrix showing how Akinyi balances her KES 500 weekly allowance: Essential needs (transport, lunch, notebook) are funded first, savings are adjusted, and the non-essential hair clip is rejected as the opportunity cost."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Anatomy of a Personal Spending Plan",
                    "content": {
                        "title": "The Structural Pillars of a Resilient Personal Budget",
                        "text": "A **Personal Budget** is a structured financial schedule that matches expected income inflows against planned expenditure outflows over a specific timeframe (weekly, monthly, or termly).\n\nA well-structured budget contains five key components:\n1. **Fixed Income Inflows ($Y$)**: Allowance, pocket money, or small-enterprise earnings.\n2. **Essential Fixed Needs ($N_f$)**: Mandatory survival expenditures (e.g., commute transport, staple lunch).\n3. **Essential Variable Needs ($N_v$)**: Critical academic supplies (e.g., exercise books, pens, geometry sets).\n4. **Targeted Savings Buffer ($S$)**: Funds set aside for emergencies or long-term goals *before* discretionary spending.\n5. **Discretionary Wants ($W$)**: Non-essential leisure and comfort items, funded *only* when a budgetary surplus exists."
                    }
                }
            ]
        },
        # Page 5: 6-Step Worked Example (Akinyi's Case Study)
        {
            "page_number": 5,
            "page_title": "Worked Calculation: Akinyi's KES 500 Weekly Budget Allocation",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Balancing a Student Budget Under Resource Constraints",
                    "content": {
                        "problem": "Akinyi receives a weekly allowance of $\\text{KES } 500$ from her parents to cover all her school-week expenditures. Her competing demands for the week are:\n- School transport: $\\text{KES } 250$\n- School lunch: $\\text{KES } 150$\n- Revision notebook for Business Studies: $\\text{KES } 70$\n- Fancy decorative hair clip: $\\text{KES } 100$\n- Planned savings for upcoming educational trip: $\\text{KES } 50$\n\nPrepare a prioritized, balanced budget matrix for Akinyi. Determine her total expenditure, identify the opportunity cost incurred to balance the budget, and verify that her net budget balance is zero without incurring debt.",
                        "steps": [
                            "**1. Step 1: Identify Given Data & Quantify Initial Deficit**\n- Available Income ($Y$) $= \\text{KES } 500$\n- Total Unconstrained Demands $= 250 + 150 + 70 + 100 + 50 = \\text{KES } 620$\n- Unconstrained Deficit $= \\text{KES } 500 - \\text{KES } 620 = -\\text{KES } 120$ (Budget Exceeded by $\\text{KES } 120$!).",
                            "**2. Step 2: Formulate the Budget Constraint Equations**\n- General Budget Constraint:\n  $$Y \\ge \\sum \\text{Needs} + \\sum \\text{Savings} + \\sum \\text{Wants}$$\n- Balanced Net Equation:\n  $$\\text{Net Balance} = Y - \\text{Total Approved Expenses} = 0$$",
                            "**3. Step 3: Prioritize and Fund Essential Needs First**\n- Item 1: School Transport (Need) $= \\text{KES } 250$\n- Item 2: School Lunch (Need) $= \\text{KES } 150$\n- Item 3: Business Revision Notebook (Need) $= \\text{KES } 70$\n$$\\text{Total Essential Needs} = 250 + 150 + 70 = \\text{KES } 470$$\n- Remaining Disposable Balance $= \\text{KES } 500 - \\text{KES } 470 = \\text{KES } 30$.",
                            "**4. Step 4: Adjust Savings and Evaluate Discretionary Wants**\n- Requested Trip Savings $= \\text{KES } 50$. Since only $\\text{KES } 30$ remains, adjust approved savings to $\\text{KES } 30$.\n- Remaining Balance after Savings $= \\text{KES } 30 - \\text{KES } 30 = \\text{KES } 0$.\n- Fancy Hair Clip (Want, $\\text{KES } 100$) $\\rightarrow$ **REJECTED** due to zero remaining funds.",
                            "**5. Step 5: Calculate Final Balanced Expenditure & Opportunity Cost**\n$$\\text{Total Approved Outflows} = \\text{KES } 250 + \\text{KES } 150 + \\text{KES } 70 + \\text{KES } 30 + \\text{KES } 0 = \\text{KES } 500$$\n$$\\text{Net Budget Balance} = \\text{KES } 500 - \\text{KES } 500 = \\text{KES } 0$$\n- **Final Answer**: Total expenditure is $\\text{KES } 500$ (100% balanced).\n- **Opportunity Cost**: The fancy hair clip ($\\text{KES } 100$) and $\\text{KES } 20$ of trip savings forgone.",
                            "**6. Step 6: Economic Interpretation & Common Mistake**\n- **Economic Interpretation**: By strictly applying economic prioritization, Akinyi satisfies 100% of her physical and academic survival needs, preserves a positive savings habit ($\\text{KES } 30$), and maintains complete solvency with zero debt.\n- **Common Mistake**: Treating non-essential wants as mandatory needs or borrowing money to finance luxury impulses, leading to personal financial distress."
                        ]
                    }
                },
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "The 6-Step Personal Budgeting Algorithm",
                    "content": {
                        "title": "Systematic Algorithm for Personal Spending Decisions",
                        "steps": [
                            "**1. Quantify Inflows**: Determine your exact available cash or allowance for the period.",
                            "**2. Itemize Outflows**: Write down all expected expenses and desires without omission.",
                            "**3. Classify Categories**: Categorize each item as an 'Essential Need', 'Savings Goal', or 'Discretionary Want'.",
                            "**4. Fund Needs First**: Allocate money to essential survival and educational necessities in full.",
                            "**5. Allocate Savings**: Set aside planned savings from the remaining balance before buying wants.",
                            "**6. Reconcile to Zero**: Eliminate or postpone low-priority wants until Total Expenses $\\le$ Total Income."
                        ]
                    }
                }
            ]
        },
        # Page 6: Real-World Application & Video Enrichment
        {
            "page_number": 6,
            "page_title": "Real-World Application & Financial Literacy Masterclass",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Enterprise Budgeting: Scaling Personal Discipline to Corporations",
                    "content": {
                        "title": "From Pocket Money to Corporate Balance Sheets",
                        "text": "The principles governing personal pocket money are identical to the financial management of large commercial corporations such as Safaricom, Equity Bank, or East African Breweries:\n\n- **Operating Expenses vs. Capital Luxuries (Needs vs. Wants)**: A commercial enterprise must first fund its critical operating necessities (raw material procurement, employee payroll, factory power, license fees, taxes) before board members can approve luxury office refurbishments or executive retreats.\n- **Corporate Opportunity Cost**: When a firm allocates KES 50 million to an advertising campaign, the opportunity cost is the modern machinery or employee training software it chose not to purchase.\n- **Cash Flow Solvency**: Businesses that overspend on non-productive 'corporate wants' face severe liquidity crunches, default on loan obligations, and collapse into insolvency—mirroring individuals who overspend on consumer credit.\n\n*Mastering your pocket money today prepares you to lead corporate finance departments, build profitable commercial ventures, and manage national development budgets tomorrow.*"
                    }
                },
                {
                    "block_type": "suggested_video",
                    "component_type": "suggested_video",
                    "title": "Needs vs. Wants and Teen Budgeting Masterclass",
                    "content": {
                        "title": "Needs vs. Wants and Teen Budgeting Masterclass",
                        "video_id": "yvA1Xv0t-9k",
                        "platform": "YouTube",
                        "duration": "08:24",
                        "description": "An educational guide exploring practical youth financial literacy, overcoming peer pressure, distinguishing daily essentials from lifestyle wants, and building automated savings habits.",
                        "key_takeaways": [
                            "Visualizing the 50/30/20 budgeting framework: 50% Needs, 30% Wants, 20% Savings.",
                            "Identifying psychological triggers that cause retail impulse spending.",
                            "The compounding wealth advantage of establishing consistent savings early in life."
                        ]
                    }
                }
            ]
        },
        # Page 7: Formative Scenario-Based MCQs
        {
            "page_number": 7,
            "page_title": "Formative Assessment: Applying Budgeting and Opportunity Cost",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Knowledge Check 1: Opportunity Cost in Budgeting",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Akinyi has a weekly pocket money budget of $\\text{KES } 500$. After funding her mandatory school transport ($\\text{KES } 250$), school lunch ($\\text{KES } 150$), and a required revision notebook ($\\text{KES } 70$), she decides not to purchase a fancy hair clip costing $\\text{KES } 100$ so that she can allocate the remaining $\\text{KES } 30$ to savings. In economics, the fancy hair clip represents Akinyi's:",
                        "options": [
                            "A. Capital deposit",
                            "B. Precautionary cash motive",
                            "C. Opportunity cost",
                            "D. Fixed operational expense"
                        ],
                        "answer": "C",
                        "explanation": "Opportunity cost is defined as the value of the next best alternative forgone when making a financial choice under a resource constraint. By choosing to balance her budget and prioritize essential school items and savings, Akinyi sacrificed the fancy hair clip, making it her explicit opportunity cost."
                    }
                },
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Knowledge Check 2: Classification of Basic Needs",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following items represents a **basic biological need** essential for human survival and physical health?",
                        "options": [
                            "A. A high-end smartphone with unlimited internet data",
                            "B. Safe, clean drinking water and balanced daily nutrition",
                            "C. A designer wristwatch and imported leather jacket",
                            "D. A monthly subscription to an online video streaming service"
                        ],
                        "answer": "B",
                        "explanation": "Basic needs are physiological requirements indispensable for biological survival and health, including clean drinking water, nutritious food, protective shelter, basic clothing, and healthcare. Smartphones, designer accessories, and video streaming subscriptions are secondary wants and comforts that enhance lifestyle but are not essential to preserve life."
                    }
                }
            ]
        },
        # Page 8: Summary & Key Takeaways
        {
            "page_number": 8,
            "page_title": "Lesson Summary: The Principles of Daily Monetary Management",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Summary of Core Economic Principles",
                    "content": {
                        "title": "Core Takeaways: Money in Day-to-Day Life",
                        "text": "- **Scarcity & Choice**: Money is a limited economic tool; every expenditure requires deliberate trade-offs.\n- **Needs vs. Wants**: Always secure survival and educational necessities (Needs) prior to indulging in discretionary luxuries (Wants).\n- **Opportunity Cost**: Every monetary choice carries the implicit cost of the sacrificed alternative.\n- **Zero-Deficit Budgeting**: Structure spending so that $\\text{Total Expenses} \\le \\text{Income}$ ($\\sum \\text{Needs} + \\sum \\text{Savings} \\le Y$).\n- **Financial Discipline**: Consistent personal budgeting lays the direct foundation for professional accounting, entrepreneurship, and long-term financial security."
                    }
                }
            ]
        }
    ]
}

# Validate JSON serialization and structure
json_str = json.dumps(lesson_6_data, indent=2)
print("JSON length:", len(json_str))
print("Page count:", len(lesson_6_data["pages"]))
total_blocks = sum(len(p["blocks"]) for p in lesson_6_data["pages"])
print("Total blocks:", total_blocks)

# Check for bracket citations
citations = re.findall(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', json_str)
print("Bracket citations found:", citations)
