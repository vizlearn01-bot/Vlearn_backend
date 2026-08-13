"""
Form 4 Agriculture — Topic 6 Data File
Topic: Agricultural Economics V (Agricultural Marketing and Organisations)
Curriculum: 844 (ID: 4) | Grade: Form 4 (ID: 4) | Subject: Agriculture (ID: 19) | Topic ID: 100 (Order: 6)

Contains 3 Learning Units:
1. Marketing Concepts, Functions, and Agencies
2. Price Theory, Demand, Supply, and Elasticity
3. Co-operatives and Statutory Organisations
"""

# =============================================================================
# CUSTOM DARK-MODE SVG DIAGRAMS FOR AGRICULTURAL MARKETING
# =============================================================================

# 1. 5-Stage Marketing Process Flowchart
SVG_MARKETING_PROCESS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">5-Stage Agricultural Marketing Channel</text>

  <!-- Stage 1: Assembling -->
  <rect x="40" y="90" width="125" height="100" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="10"/>
  <text x="102" y="125" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold" text-anchor="middle">1. Assembly</text>
  <text x="102" y="148" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Collect Small Lots</text>
  <text x="102" y="165" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">from Farm Gates</text>

  <line x1="165" y1="140" x2="190" y2="140" stroke="#38bdf8" stroke-width="3"/>

  <!-- Stage 2: Grading -->
  <rect x="190" y="90" width="125" height="100" fill="#1e293b" stroke="#4ade80" stroke-width="2.5" rx="10"/>
  <text x="252" y="125" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold" text-anchor="middle">2. Grading</text>
  <text x="252" y="148" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Sort by Size,</text>
  <text x="252" y="165" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Quality &amp; Weight</text>

  <line x1="315" y1="140" x2="340" y2="140" stroke="#4ade80" stroke-width="3"/>

  <!-- Stage 3: Packaging -->
  <rect x="340" y="90" width="125" height="100" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5" rx="10"/>
  <text x="402" y="125" font-family="Arial" font-size="13" fill="#f59e0b" font-weight="bold" text-anchor="middle">3. Packaging</text>
  <text x="402" y="148" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Bagging in 90kg</text>
  <text x="402" y="165" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Sisal / Net Packs</text>

  <line x1="465" y1="140" x2="490" y2="140" stroke="#f59e0b" stroke-width="3"/>

  <!-- Stage 4: Transport -->
  <rect x="490" y="90" width="125" height="100" fill="#1e293b" stroke="#a855f7" stroke-width="2.5" rx="10"/>
  <text x="552" y="125" font-family="Arial" font-size="13" fill="#a855f7" font-weight="bold" text-anchor="middle">4. Transport</text>
  <text x="552" y="148" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Haul Bulk Goods</text>
  <text x="552" y="165" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">to Urban Depots</text>

  <line x1="615" y1="140" x2="640" y2="140" stroke="#a855f7" stroke-width="3"/>

  <!-- Stage 5: Retail -->
  <rect x="640" y="90" width="125" height="100" fill="#1e293b" stroke="#f43f5e" stroke-width="2.5" rx="10"/>
  <text x="702" y="125" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold" text-anchor="middle">5. Retail</text>
  <text x="702" y="148" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Break Bulk for</text>
  <text x="702" y="165" font-family="Arial" font-size="10" fill="#f8fafc" text-anchor="middle">Final Consumers</text>

  <!-- Bottlenecks & Solutions Summary Box -->
  <rect x="40" y="230" width="725" height="210" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="12"/>
  <text x="402" y="262" font-family="Arial" font-size="15" fill="#f8fafc" font-weight="bold" text-anchor="middle">Post-Harvest Agricultural Bottlenecks &amp; Solutions</text>

  <text x="70" y="295" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold">1. High Perishability:</text>
  <text x="210" y="295" font-family="Arial" font-size="12" fill="#cbd5e1">Requires immediate cold storage or rapid pasteurization.</text>

  <text x="70" y="330" font-family="Arial" font-size="13" fill="#f59e0b" font-weight="bold">2. High Bulkiness:</text>
  <text x="200" y="330" font-family="Arial" font-size="12" fill="#cbd5e1">Requires specialized heavy transport and bulk processing.</text>

  <text x="70" y="365" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold">3. Poor Infrastructure:</text>
  <text x="230" y="365" font-family="Arial" font-size="12" fill="#cbd5e1">Rural impassable roads cause spoilage; requires feeder road upgrades.</text>

  <text x="70" y="400" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold">4. Price Asymmetry:</text>
  <text x="220" y="400" font-family="Arial" font-size="12" fill="#cbd5e1">Middlemen exploit rural farmers; solved via cooperative bargaining.</text>
</svg>"""


# 2. Demand and Supply Equilibrium Graph Diagram
SVG_EQUILIBRIUM_GRAPH = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Market Price Equilibrium, Surplus, and Shortage</text>

  <!-- Axes -->
  <line x1="100" y1="380" x2="680" y2="380" stroke="#94a3b8" stroke-width="3"/>
  <line x1="100" y1="380" x2="100" y2="80" stroke="#94a3b8" stroke-width="3"/>
  <text x="390" y="415" font-family="Arial" font-size="13" fill="#94a3b8" text-anchor="middle">Quantity (kg / bags)</text>
  <text x="50" y="230" font-family="Arial" font-size="13" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 50 230)">Price (KShs)</text>

  <!-- Demand Curve D-D (Sloping Down) -->
  <line x1="150" y1="100" x2="630" y2="350" stroke="#38bdf8" stroke-width="4"/>
  <text x="645" y="360" font-family="Arial" font-size="14" fill="#38bdf8" font-weight="bold">D</text>
  <text x="135" y="100" font-family="Arial" font-size="14" fill="#38bdf8" font-weight="bold">D</text>

  <!-- Supply Curve S-S (Sloping Up) -->
  <line x1="150" y1="350" x2="630" y2="100" stroke="#4ade80" stroke-width="4"/>
  <text x="645" y="100" font-family="Arial" font-size="14" fill="#4ade80" font-weight="bold">S</text>
  <text x="135" y="360" font-family="Arial" font-size="14" fill="#4ade80" font-weight="bold">S</text>

  <!-- Equilibrium Point E (x=390, y=225) -->
  <circle cx="390" cy="225" r="7" fill="#f59e0b"/>
  <line x1="390" y1="225" x2="390" y2="380" stroke="#f59e0b" stroke-dasharray="5,5" stroke-width="2"/>
  <line x1="390" y1="225" x2="100" y2="225" stroke="#f59e0b" stroke-dasharray="5,5" stroke-width="2"/>
  <text x="405" y="215" font-family="Arial" font-size="14" fill="#f59e0b" font-weight="bold">E (Equilibrium)</text>
  <text x="60" y="230" font-family="Arial" font-size="12" fill="#f59e0b" font-weight="bold">Pe</text>
  <text x="390" y="400" font-family="Arial" font-size="12" fill="#f59e0b" font-weight="bold">Qe</text>

  <!-- Surplus Zone (Above Equilibrium) -->
  <rect x="250" y="120" width="280" height="45" fill="#f43f5e" fill-opacity="0.15" stroke="#f43f5e" stroke-dasharray="3,3" rx="6"/>
  <text x="390" y="147" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold" text-anchor="middle">SURPLUS REGION (Supply &gt; Demand)</text>

  <!-- Shortage Zone (Below Equilibrium) -->
  <rect x="250" y="280" width="280" height="45" fill="#a855f7" fill-opacity="0.15" stroke="#a855f7" stroke-dasharray="3,3" rx="6"/>
  <text x="390" y="307" font-family="Arial" font-size="13" fill="#a855f7" font-weight="bold" text-anchor="middle">SHORTAGE REGION (Demand &gt; Supply)</text>
</svg>"""


# 3. 4-Tier Co-operative Hierarchy Diagram
SVG_COOP_HIERARCHY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">The 4-Tier Co-operative Structure in Kenya</text>

  <!-- Tier 4: Apex Body -->
  <polygon points="400,75 580,150 220,150" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
  <text x="400" y="125" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">Tier 4: Apex Body (KNFC)</text>

  <!-- Tier 3: Tertiary Unions -->
  <polygon points="220,155 580,155 640,235 160,235" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="400" y="200" font-family="Arial" font-size="14" fill="#f59e0b" font-weight="bold" text-anchor="middle">Tier 3: Tertiary Unions (KCC, Co-op Bank, KPCU)</text>

  <!-- Tier 2: District Unions -->
  <polygon points="160,240 640,240 700,320 100,320" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="400" y="285" font-family="Arial" font-size="14" fill="#4ade80" font-weight="bold" text-anchor="middle">Tier 2: District Co-operative Unions (Amalgamated)</text>

  <!-- Tier 1: Primary Societies -->
  <polygon points="100,325 700,325 760,410 40,410" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="365" font-family="Arial" font-size="14" fill="#38bdf8" font-weight="bold" text-anchor="middle">Tier 1: Primary Co-operative Societies (Village Level, Min 10 Members)</text>

  <!-- Upward Arrow -->
  <line x1="770" y1="400" x2="770" y2="80" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="770,70 762,85 778,85" fill="#38bdf8"/>
  <text x="755" y="240" font-family="Arial" font-size="11" fill="#38bdf8" font-weight="bold" text-anchor="middle" transform="rotate(-90 755 240)">Vertical Capital &amp; Representation Flow</text>
</svg>"""


# =============================================================================
# LESSON DATA DICTIONARIES
# =============================================================================

LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Marketing Concepts, Functions, and Agencies",
    "lesson_title": "Marketing Concepts, Functions, and Agencies",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Agricultural Marketing",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Distinguish between a market and agricultural marketing.\n"
                            "- Explain the twelve primary marketing functions.\n"
                            "- Compare marketing agencies (itinerant middlemen, wholesalers, retailers).\n"
                            "- Identify post-harvest marketing bottlenecks and execute a 6-step maize grading procedure."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Core Definitions",
                    "content": {
                        "text": (
                            "- **Market:** A physical location or institution where buyers and sellers meet to exchange goods and services.\n"
                            "- **Agricultural Marketing:** The complete flow of agricultural commodities from the point of production (farm) to final consumption.\n"
                            "- **Assembling:** Gathering small commodity lots from scattered smallholder farms into bulk collection centers.\n"
                            "- **Itinerant Middleman:** A mobile trader who buys small quantities directly from farm gates and sells to wholesalers."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Marketing Process Flowchart Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "5-Stage Agricultural Marketing Channel",
                    "content": {
                        "text": "Flowchart showing the 5 stages of the agricultural distribution channel from Assembly, Grading, Packaging, Transport, to Retail.",
                        "svg": SVG_MARKETING_PROCESS
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Twelve Primary Marketing Functions",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Summary of 12 Marketing Functions",
                    "content": {
                        "headers": ["Function Name", "Primary Purpose", "Value Added"],
                        "rows": [
                            ["1. Transportation", "Hauling bulky goods from farms to urban centers", "Place Utility"],
                            ["2. Buying & Selling", "Exchanging legal ownership between traders", "Possession Utility"],
                            ["3. Storage", "Holding seasonal harvests for off-season release", "Time Utility"],
                            ["4. Processing", "Transforming raw produce into flour, cheese, or butter", "Form Utility"],
                            ["5. Grading & Sorting", "Categorizing produce by quality, size, and weight", "Quality Standard"],
                            ["6. Assembling", "Aggregating small yields into commercial truckloads", "Bulk Scale"],
                            ["7. Market Information", "Gathering intelligence on daily market prices", "Pricing Accuracy"],
                            ["8. Advertising", "Promoting products to build buyer demand", "Market Awareness"],
                            ["9. Risk Bearing", "Absorbing spoilage, fire, or price collapse losses", "Financial Safety"],
                            ["10. Financing", "Providing capital for transport, storage, and packaging", "Capital Support"],
                            ["11. Packaging", "Enclosing goods in small retail-ready units", "Protection"],
                            ["12. Packing", "Placing packaged goods into shipping crates or bags", "Transport Ease"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Post-Harvest Marketing Bottlenecks in Kenya",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Key Challenges in Agricultural Marketing",
                    "content": {
                        "text": (
                            "- **High Perishability:** Fresh milk, meat, and vegetables decay quickly without cold storage.\n"
                            "- **High Bulkiness:** Sugarcane and cabbages have low value relative to their large transport volume.\n"
                            "- **Poor Rural Infrastructure:** Rainy seasons make feeder roads impassable, rotting harvests in transit.\n"
                            "- **Price Information Asymmetry:** Rural farmers lack urban price data, making them vulnerable to middleman exploitation."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Step-by-Step Procedure: Post-Harvest Processing & Grading",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "6 Steps for Maize Grain Processing & Grading",
                    "content": {
                        "text": (
                            "**Step 1: Winnowing & De-trashing**\n"
                            "Pour shelled grains on a breezy day to let wind remove chaff, cob dust, and foreign particles.\n\n"
                            "**Step 2: Solar Dehydration (Drying)**\n"
                            "Spread winnowed maize evenly on clean tarpaulins until moisture drops to 12.5% - 13% to prevent toxic aflatoxins.\n\n"
                            "**Step 3: Manual Inspection & Sorting**\n"
                            "Hand-pick and remove discolored, broken, insect-bored, or moldy kernels.\n\n"
                            "**Step 4: Grading by Grain Size & Color**\n"
                            "Sort into Grade 1 (plump, uniform white grains) and Grade 2 (smaller or mixed kernels).\n\n"
                            "**Step 5: Standard Bagging**\n"
                            "Fill clean sisal bags to exactly 90 kg and sew the top securely to allow grain respiration.\n\n"
                            "**Step 6: Labeling & Storage**\n"
                            "Stencil grade name and farm source on each bag before transporting to cool pallets."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Practical Scenario: Decision-Making Under Road Blockades",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Case Study: Managing Perishable Tomato Harvests",
                    "content": {
                        "text": (
                            "A farmer in Meru harvests 2,000 kg of fresh tomatoes during heavy rains when local roads are impassable.\n"
                            "An itinerant middleman offers KShs 15/kg at the farm gate, while Nairobi prices are KShs 50/kg.\n"
                            "**Optimal Economic Decision:** Accept the middleman's offer. Without cold storage or heavy trucks, waiting results in 100% spoilage loss. The middleman assumes the transport risk and spoilage burden."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Decision Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Evaluating Agricultural Marketing Decisions",
                    "content": {
                        "text": "Why do itinerant middlemen frequently offer low prices to rural smallholders?",
                        "options": [
                            "A: They bear transport risks, spoilage losses, and exploit farmers' lack of pricing data.",
                            "B: Government policy forces middlemen to charge low prices.",
                            "C: Middlemen only buy Grade 1 produce that requires no processing.",
                            "D: Middlemen are funded directly by statutory boards."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Middlemen absorb high transport risks and spoilage while taking advantage of rural price information gaps."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Marketing Agencies Overview",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Key Marketing Agencies",
                    "content": {
                        "text": (
                            "- **Itinerant Middlemen:** Farm-gate buyers providing immediate cash to remote farmers.\n"
                            "- **Wholesalers:** Commercial traders buying bulk lots from assembling depots and storing them.\n"
                            "- **Retailers:** Neighborhood stallholders and supermarkets breaking bulk into single consumer units."
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
                            "1. Marketing encompasses all value-adding activities moving produce from farm to plate.\n"
                            "2. The 12 marketing functions add form, place, time, and possession utility.\n"
                            "3. Proper grading and moisture control prevent post-harvest spoilage and command premium prices."
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
                    "title": "KCSE Model Essay: Fresh Milk Marketing Functions (5 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Outline five marketing functions involved in distributing fresh milk from a farm in Kiambu to a consumer in Mombasa. (5 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Assembling:** Collecting raw milk from scattered smallholder farms into a centralized chilling center.\n"
                            "2. **Processing:** Pasteurizing or heat-treating raw milk to kill pathogens and extend shelf life.\n"
                            "3. **Packaging:** Sealing pasteurized milk into sterile 500 ml paper cartons.\n"
                            "4. **Transportation:** Hauling packaged cartons in refrigerated trucks over 500 km to Mombasa.\n"
                            "5. **Buying & Selling:** Supermarkets purchasing bulk cartons and retailing individual units to buyers."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Price Theory, Demand, Supply, and Elasticity",
    "lesson_title": "Price Theory, Demand, Supply, and Elasticity",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Market Price Theory",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- State the Laws of Demand and Supply.\n"
                            "- Explain market equilibrium, surpluses, and shortages.\n"
                            "- Calculate Price Elasticity of Demand (PED) and Price Elasticity of Supply (PES).\n"
                            "- Explain the biological supply time-lag in agriculture."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Core Price Concepts",
                    "content": {
                        "text": (
                            "- **Demand:** The quantity of a commodity buyers are willing and able to purchase at a specific price.\n"
                            "- **Supply:** The quantity of a commodity producers are ready to offer for sale at a specific price.\n"
                            "- **Equilibrium Price:** The market price where quantity demanded matches quantity supplied exactly.\n"
                            "- **Price Elasticity:** The mathematical measure of quantity responsiveness to price changes."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Market Equilibrium Graph Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Demand and Supply Equilibrium Curve",
                    "content": {
                        "text": "Graph showing downward-sloping Demand D-D, upward-sloping Supply S-S, Equilibrium E, Surplus region, and Shortage region.",
                        "svg": SVG_EQUILIBRIUM_GRAPH
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Laws of Demand and Supply",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Economic Laws & Factors",
                    "content": {
                        "text": (
                            "- **Law of Demand:** Quantity demanded varies inversely with price (as price increases, demand drops).\n"
                            "- **Law of Supply:** Quantity supplied varies directly with price (as price increases, supply rises).\n"
                            "- **Demand Factors:** Consumer income, population, tastes, substitute prices (beef vs mutton).\n"
                            "- **Supply Factors:** Weather, input costs, production technology, number of producers."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Elasticity Formulas: PED and PES",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Elasticity Calculation Formulas",
                    "content": {
                        "text": (
                            "**Price Elasticity of Demand (PED):**\n"
                            "**PED = Percentage Change in Quantity Demanded / Percentage Change in Price**\n\n"
                            "**Price Elasticity of Supply (PES):**\n"
                            "**PES = Percentage Change in Quantity Supplied / Percentage Change in Price**\n\n"
                            "**Interpretation:**\n"
                            "- Elastic (Value > 1): Highly responsive to price changes.\n"
                            "- Inelastic (Value < 1): Low responsiveness to price changes."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Calculation 1: Price Elasticity of Demand (Beans)",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Calculating PED for Staple Beans",
                    "content": {
                        "text": (
                            "**Data:** Price rises from KShs 4,000 to KShs 5,000 per bag (+25%). Quantity demanded falls from 200 to 180 bags (-10%).\n\n"
                            "**Step 1: Percentage Change in Quantity** = (-20 / 200) * 100 = -10%\n"
                            "**Step 2: Percentage Change in Price** = (1,000 / 4,000) * 100 = +25%\n"
                            "**Step 3: PED Calculation** = |-10% / 25%| = **0.4**\n\n"
                            "**Agricultural Interpretation:** PED = 0.4 (< 1), meaning demand for dry beans is **inelastic**. Consumers must purchase staple food even when prices rise substantially."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Calculation 2: Price Elasticity of Supply (Eggs)",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Calculating PES for Poultry Eggs",
                    "content": {
                        "text": (
                            "**Data:** Tray price rises from KShs 300 to KShs 390 (+30%). Daily supply increases from 500 to 700 trays (+40%).\n\n"
                            "**Step 1: Percentage Change in Quantity** = (200 / 500) * 100 = +40%\n"
                            "**Step 2: Percentage Change in Price** = (90 / 300) * 100 = +30%\n"
                            "**Step 3: PES Calculation** = 40% / 30% = **1.33**\n\n"
                            "**Agricultural Interpretation:** PES = 1.33 (> 1), meaning egg supply is **elastic**. The farm rapidly increases output using reserve laying flocks."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Calculate Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Calculating Cabbage Demand Elasticity",
                    "content": {
                        "text": "When cabbage price falls from KShs 40 to KShs 30 (-25%), weekly hotel purchases rise from 100 to 150 bags (+50%). What is the PED?",
                        "options": [
                            "A: PED = 0.5 (Inelastic)",
                            "B: PED = 2.0 (Elastic)",
                            "C: PED = 1.0 (Unitary)",
                            "D: PED = 4.0 (Perfectly Elastic)"
                        ],
                        "correct_answer_index": 1,
                        "explanation": "PED = 50% / 25% = 2.0. Since 2.0 > 1, demand is elastic."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "The Agricultural Biological Supply Lag",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Agricultural Short-Run Supply is Inelastic",
                    "content": {
                        "text": (
                            "- **Biological Growth Cycle:** Crops and livestock require months or years to mature (e.g. maize requires 4-6 months).\n"
                            "- **Inability to Instantaneously Boost Output:** If crop prices double today, farmers cannot harvest immediately.\n"
                            "- **Contrast with Industry:** Factories can run extra shifts within hours to boost manufactured output."
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
                            "1. Free market prices stabilize where Demand and Supply curves intersect.\n"
                            "2. Elasticity measures quantity responsiveness to price changes.\n"
                            "3. Short-run agricultural supply is inelastic due to unavoidable biological growth lags."
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
                    "title": "KCSE Model Essay: Crop Supply Inelasticity (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Explain three reasons why short-run supply of agricultural crops like maize is inelastic compared to manufactured tractor spare parts. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Biological Growth Time-Lag:** Maize takes 4-6 months to mature. Farmers cannot speed up biology to increase supply when prices rise in the short run.\n"
                            "2. **Seasonality:** Crop production depends on rain seasons and weather windows, whereas factories produce continuously year-round.\n"
                            "3. **Perishability & Storage Limits:** Crop storage is restricted by silo capacity and rot risks, preventing long-term buffering."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Co-operatives and Statutory Organisations",
    "lesson_title": "Co-operatives and Statutory Organisations",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Agricultural Organisations",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define an agricultural cooperative and outline the 4-tier structural hierarchy.\n"
                            "- State functions and operational challenges of primary cooperatives.\n"
                            "- Identify statutory marketing boards and national support bodies (KNFU, ASK, 4-K Clubs, Women Groups).\n"
                            "- Execute a 5-step procedure to register a primary cooperative society."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Organisation Definitions",
                    "content": {
                        "text": (
                            "- **Co-operative:** A voluntary organization of farmers with common economic goals who pool resources.\n"
                            "- **Primary Co-operative:** Local village-level society registered directly by individual farmers (minimum 10 members).\n"
                            "- **Statutory Board:** A government organization established by an Act of Parliament to regulate an agricultural industry.\n"
                            "- **Amalgamation:** Combining primary societies to form district-level cooperative unions."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Co-operative Structure Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "The Four-Tier Co-operative Structure",
                    "content": {
                        "text": "Pyramid diagram showing Tier 1 Primary Societies, Tier 2 District Unions, Tier 3 Tertiary Unions (KCC, Co-op Bank), and Tier 4 Apex Body (KNFC).",
                        "svg": SVG_COOP_HIERARCHY
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Functions of Agricultural Co-operatives",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Key Co-operative Services",
                    "content": {
                        "text": (
                            "- **Bulk Marketing:** Assembling members' produce to negotiate higher export prices.\n"
                            "- **Input Supply:** Purchasing fertilizers and feeds in wholesale quantities and selling at discount rates.\n"
                            "- **Credit Facilities:** Providing soft loans and cash advances against delivered crops.\n"
                            "- **Processing & Transport:** Operating milk cooling plants and transport fleets."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Step-by-Step Procedure: Registering a Primary Co-operative",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "5 Steps to Form & Register a Primary Society",
                    "content": {
                        "text": (
                            "**Step 1: Convene Founders' Meeting**\n"
                            "Gather a minimum of 10 qualifying local farmers with common economic interests.\n\n"
                            "**Step 2: Draft Society By-Laws**\n"
                            "Formulate governing operational rules detailing membership, share capital, and dividend sharing.\n\n"
                            "**Step 3: Elect Management Committee**\n"
                            "Democratically elect executive officers: Chairman, Secretary, and Treasurer.\n\n"
                            "**Step 4: Submit Registration Application**\n"
                            "File draft by-laws and member registers with the District Cooperative Officer.\n\n"
                            "**Step 5: Obtain Certificate of Registration**\n"
                            "Receive formal government certificate granting corporate legal status."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Challenges Facing Agricultural Co-operatives",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Major Co-operative Bottlenecks",
                    "content": {
                        "text": (
                            "- **Managerial Incompetence:** Financial mismanagement, lack of accounting skills, and corruption.\n"
                            "- **Capital Shortages:** Inadequate funds to build modern processing factories.\n"
                            "- **Member Side-Selling:** Farmers selling produce to external middlemen for fast cash."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Statutory Marketing Boards in Kenya",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Kenyan Statutory Boards & Functions",
                    "content": {
                        "headers": ["Board Name", "Industry Managed", "Key Regulatory Function"],
                        "rows": [
                            ["National Cereals & Produce Board (NCPB)", "Grain & Maize", "Manages strategic grain reserves and price stabilization"],
                            ["Coffee Board of Kenya", "Coffee Sector", "Regulates coffee processing, licensing, and international auctions"],
                            ["Pyrethrum Board of Kenya", "Pyrethrum Flowers", "Processes flowers into pyrethrin insecticides for export"],
                            ["Kenya Meat Commission (KMC)", "Livestock & Meat", "Operates public abattoirs and purchases livestock during droughts"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "National Agricultural Support Bodies",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Non-Statutory Organisations",
                    "content": {
                        "text": (
                            "- **Kenya National Farmers' Union (KNFU):** Represents farmers' policy interests and negotiates input subsidies.\n"
                            "- **Agricultural Society of Kenya (ASK):** Organizes national trade shows and agricultural exhibitions.\n"
                            "- **Young Farmers & 4-K Clubs:** School clubs promoting youth agricultural skills and garden projects.\n"
                            "- **Women Groups:** Self-help groups pooling labor and micro-finance for rural farm projects."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Interactive Diagnostic Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Diagnosing Co-operative Failures",
                    "content": {
                        "text": "A primary dairy cooperative collapses because the elected Treasurer maintains no cash book and hires uncertified drivers. What is the core issue?",
                        "options": [
                            "A: Low international milk market prices.",
                            "B: Severe drought in pastures.",
                            "C: Managerial incompetence, lack of bookkeeping, and nepotism.",
                            "D: Excessive statutory board regulation."
                        ],
                        "correct_answer_index": 2,
                        "explanation": "Internal mismanagement and lack of proper accounting controls are primary causes of cooperative failure."
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
                            "1. Primary cooperatives pool smallholder capital to achieve economies of scale.\n"
                            "2. Kenya's 4-tier structure links village primary societies to national apex bodies.\n"
                            "3. Statutory boards manage specific industries while bodies like ASK and 4-K Clubs drive education."
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
                    "title": "KCSE Model Essay: Agricultural Support Bodies (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Identify four support organizations in Kenya other than cooperatives and statutory boards, stating one key function of each. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Kenya National Farmers' Union (KNFU):** Lobbies government for fair input prices and favorable agricultural policies.\n"
                            "2. **Agricultural Society of Kenya (ASK):** Organizes annual agricultural trade shows to demonstrate modern technologies.\n"
                            "3. **Young Farmers & 4-K Clubs:** Trains youth in schools on practical farming and leadership skills.\n"
                            "4. **Women Groups:** Micro-finance self-help groups pooling funds for rural livestock and crop projects."
                        )
                    }
                }
            ]
        }
    ]
}

TOPIC_6_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA
]
