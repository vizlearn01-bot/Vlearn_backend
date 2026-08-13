"""
Form 4 Agriculture — Topic 7 Data File
Topic: Agroforestry
Curriculum: 844 (ID: 4) | Grade: Form 4 (ID: 4) | Subject: Agriculture (ID: 19) | Topic ID: 101 (Order: 7)

Contains 4 Learning Units:
1. Definition, Forms, Importance, and Species Selection
2. Nursery Types, Seed Collection, and Dormancy Breaking
3. Nursery Management, Hardening Off, and Transplanting
4. Tree Maintenance, Grafting Mechanics, and Sustainable Harvesting
"""

# =============================================================================
# CUSTOM DARK-MODE SVG DIAGRAMS FOR AGROFORESTRY
# =============================================================================

# 1. 3 Biological Forms of Agroforestry Diagram
SVG_AGROFORESTRY_FORMS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Three Primary Biological Forms of Agroforestry</text>

  <!-- Form 1: Agrosilvicultural -->
  <rect x="50" y="80" width="210" height="360" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="12"/>
  <rect x="50" y="80" width="210" height="40" fill="#0284c7" rx="12"/>
  <text x="155" y="106" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">Agrosilvicultural</text>
  <text x="155" y="150" font-family="Arial" font-size="16" fill="#38bdf8" font-weight="bold" text-anchor="middle">TREES + CROPS</text>
  <text x="155" y="185" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Maize &amp; Grevillea</text>
  <text x="155" y="210" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Alley Cropping</text>
  <text x="155" y="235" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Contour Hedges</text>
  <text x="155" y="260" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Nutrient Pumping</text>
  <text x="155" y="285" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Windbreaks &amp; Shade</text>
  <rect x="75" y="340" width="160" height="70" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
  <text x="155" y="370" font-family="Arial" font-size="11" fill="#38bdf8" text-anchor="middle" font-weight="bold">Maximizes crop yields</text>

  <!-- Form 2: Silvopastoral -->
  <rect x="295" y="80" width="210" height="360" fill="#1e293b" stroke="#4ade80" stroke-width="2.5" rx="12"/>
  <rect x="295" y="80" width="210" height="40" fill="#16a34a" rx="12"/>
  <text x="400" y="106" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">Silvopastoral</text>
  <text x="400" y="150" font-family="Arial" font-size="16" fill="#4ade80" font-weight="bold" text-anchor="middle">TREES + PASTURE</text>
  <text x="400" y="185" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Grazing under Acacia</text>
  <text x="400" y="210" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Fodder Trees</text>
  <text x="400" y="235" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Animal Shade</text>
  <text x="400" y="260" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Pasture Protection</text>
  <text x="400" y="285" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• High Protein Feed</text>
  <rect x="320" y="340" width="160" height="70" fill="#0f172a" stroke="#4ade80" stroke-width="1.5" rx="8"/>
  <text x="400" y="370" font-family="Arial" font-size="11" fill="#4ade80" text-anchor="middle" font-weight="bold">Boosts livestock output</text>

  <!-- Form 3: Agrosilvopastoral -->
  <rect x="540" y="80" width="210" height="360" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5" rx="12"/>
  <rect x="540" y="80" width="210" height="40" fill="#d97706" rx="12"/>
  <text x="645" y="106" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">Agrosilvopastoral</text>
  <text x="645" y="150" font-family="Arial" font-size="16" fill="#f59e0b" font-weight="bold" text-anchor="middle">TREES+CROPS+ANIMALS</text>
  <text x="645" y="185" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Integrated Farm</text>
  <text x="645" y="210" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Zero-Grazing Unit</text>
  <text x="645" y="235" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Calliandra Fodder</text>
  <text x="645" y="260" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Manure Recycling</text>
  <text x="645" y="285" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Fuel &amp; Food Crops</text>
  <rect x="565" y="340" width="160" height="70" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
  <text x="645" y="370" font-family="Arial" font-size="11" fill="#f59e0b" text-anchor="middle" font-weight="bold">Complete integration</text>
</svg>"""


# 2. Nursery Types Comparison Diagram
SVG_NURSERY_TYPES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Bare-Root Swaziland Bed vs Containerized Nursery</text>

  <!-- Left: Bare-Root Swaziland Bed -->
  <rect x="50" y="75" width="330" height="365" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="10"/>
  <text x="215" y="105" font-family="Arial" font-size="16" fill="#38bdf8" font-weight="bold" text-anchor="middle">BARE-ROOT SWAZILAND BED</text>

  <rect x="75" y="125" width="280" height="110" fill="#0f172a" stroke="#64748b" stroke-width="1.5" rx="8"/>
  <text x="215" y="155" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">• Raised open soil bed bounded by timber/polythene.</text>
  <text x="215" y="180" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">• Seedlings grow directly in bed soil.</text>
  <text x="215" y="205" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">• Requires root pruning wire under bed.</text>

  <text x="75" y="265" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold">Advantages:</text>
  <text x="75" y="290" font-family="Arial" font-size="11" fill="#cbd5e1">• Low cost (no plastic sleeves needed).</text>
  <text x="75" y="310" font-family="Arial" font-size="11" fill="#cbd5e1">• Easy short-distance transport on-farm.</text>

  <text x="75" y="340" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold">Disadvantages:</text>
  <text x="75" y="365" font-family="Arial" font-size="11" fill="#cbd5e1">• High root damage when uprooting.</text>
  <text x="75" y="385" font-family="Arial" font-size="11" fill="#cbd5e1">• Cannot be transported long distances.</text>

  <!-- Right: Containerized Nursery -->
  <rect x="420" y="75" width="330" height="365" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5" rx="10"/>
  <text x="585" y="105" font-family="Arial" font-size="16" fill="#f59e0b" font-weight="bold" text-anchor="middle">CONTAINERIZED NURSERY</text>

  <rect x="445" y="125" width="280" height="110" fill="#0f172a" stroke="#64748b" stroke-width="1.5" rx="8"/>
  <text x="585" y="155" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">• Seedlings raised in individual plastic sleeves/pots.</text>
  <text x="585" y="180" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">• Soil root-ball remains 100% intact.</text>
  <text x="585" y="205" font-family="Arial" font-size="12" fill="#f8fafc" text-anchor="middle">• Sleeves removed right before planting.</text>

  <text x="445" y="265" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold">Advantages:</text>
  <text x="445" y="290" font-family="Arial" font-size="11" fill="#cbd5e1">• 100% root preservation during transport.</text>
  <text x="445" y="310" font-family="Arial" font-size="11" fill="#cbd5e1">• Easy long-distance transport without drying.</text>

  <text x="445" y="340" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold">Disadvantages:</text>
  <text x="445" y="365" font-family="Arial" font-size="11" fill="#cbd5e1">• High cost of plastic pots &amp; potting media.</text>
  <text x="445" y="385" font-family="Arial" font-size="11" fill="#cbd5e1">• Heavy weight during transport.</text>
</svg>"""


# 3. Root Pruning Mechanics Diagram
SVG_ROOT_PRUNING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Root Pruning Mechanics and Lateral Root Stimulus</text>

  <!-- Stage 1 -->
  <rect x="50" y="90" width="150" height="340" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="10"/>
  <text x="125" y="120" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold" text-anchor="middle">Stage 1: Unpruned</text>
  <text x="125" y="150" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Taproot grows down</text>
  <text x="125" y="170" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">out of container hole</text>
  <text x="125" y="190" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">into deep ground.</text>

  <!-- Stage 2 -->
  <rect x="230" y="90" width="150" height="340" fill="#1e293b" stroke="#f43f5e" stroke-width="2" rx="10"/>
  <text x="305" y="120" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold" text-anchor="middle">Stage 2: Cut Action</text>
  <text x="305" y="150" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Sharp knife cuts</text>
  <text x="305" y="170" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">protruding root at</text>
  <text x="305" y="190" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">container base.</text>

  <!-- Stage 3 -->
  <rect x="410" y="90" width="150" height="340" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="10"/>
  <text x="485" y="120" font-family="Arial" font-size="13" fill="#f59e0b" font-weight="bold" text-anchor="middle">Stage 3: Shift</text>
  <text x="485" y="150" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Apical dominance</text>
  <text x="485" y="170" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">broken; hormone</text>
  <text x="485" y="190" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">triggers side buds.</text>

  <!-- Stage 4 -->
  <rect x="590" y="90" width="160" height="340" fill="#1e293b" stroke="#4ade80" stroke-width="2" rx="10"/>
  <text x="670" y="120" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold" text-anchor="middle">Stage 4: Dense Mass</text>
  <text x="670" y="150" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Short, highly branched</text>
  <text x="670" y="170" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">strong lateral root</text>
  <text x="670" y="190" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">system develops.</text>
</svg>"""


# 4. Mechanical Methods of Grafting Diagram
SVG_GRAFTING_METHODS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Mechanical Grafting Methods &amp; Cambium Alignment</text>

  <!-- Method 1: Whip & Tongue -->
  <rect x="50" y="80" width="220" height="360" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="12"/>
  <rect x="50" y="80" width="220" height="40" fill="#0284c7" rx="12"/>
  <text x="160" y="106" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">1. Whip &amp; Tongue</text>
  <text x="160" y="150" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Equal stem diameters.</text>
  <text x="160" y="175" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Slanting cuts on both stems.</text>
  <text x="160" y="200" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Interlocking "tongues".</text>
  <text x="160" y="225" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Perfect cambium contact.</text>
  <rect x="70" y="280" width="180" height="130" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
  <text x="160" y="315" font-family="Arial" font-size="12" fill="#38bdf8" font-weight="bold" text-anchor="middle">Scion + Rootstock</text>
  <text x="160" y="340" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Bound tightly with</text>
  <text x="160" y="360" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">grafting tape &amp; wax.</text>

  <!-- Method 2: Side Grafting -->
  <rect x="290" y="80" width="220" height="360" fill="#1e293b" stroke="#4ade80" stroke-width="2.5" rx="12"/>
  <rect x="290" y="80" width="220" height="40" fill="#16a34a" rx="12"/>
  <text x="400" y="106" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">2. Side Grafting</text>
  <text x="400" y="150" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Scion smaller than stock.</text>
  <text x="400" y="175" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Slanting notch in side of stock.</text>
  <text x="400" y="200" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Wedge-shaped scion inserted.</text>
  <text x="400" y="225" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Stock head removed later.</text>
  <rect x="310" y="280" width="180" height="130" fill="#0f172a" stroke="#4ade80" stroke-width="1.5" rx="8"/>
  <text x="400" y="315" font-family="Arial" font-size="12" fill="#4ade80" font-weight="bold" text-anchor="middle">Side Insertion</text>
  <text x="400" y="340" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Vascular callus forms</text>
  <text x="400" y="360" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">along side notch.</text>

  <!-- Method 3: Approach Grafting -->
  <rect x="530" y="80" width="220" height="360" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5" rx="12"/>
  <rect x="530" y="80" width="220" height="40" fill="#d97706" rx="12"/>
  <text x="640" y="106" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">3. Approach Grafting</text>
  <text x="640" y="150" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Both plants rooted in soil.</text>
  <text x="640" y="175" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Bark sliced from both stems.</text>
  <text x="640" y="200" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Bound together while growing.</text>
  <text x="640" y="225" font-family="Arial" font-size="12" fill="#cbd5e1" text-anchor="middle">• Cut after full union.</text>
  <rect x="550" y="280" width="180" height="130" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
  <text x="640" y="315" font-family="Arial" font-size="12" fill="#f59e0b" font-weight="bold" text-anchor="middle">Independent Roots</text>
  <text x="640" y="340" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">Zero wilting risk</text>
  <text x="640" y="360" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">during union phase.</text>
</svg>"""


# =============================================================================
# LESSON DATA DICTIONARIES
# =============================================================================

LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Definition, Forms, Importance, and Species Selection",
    "lesson_title": "Definition, Forms, Importance, and Species Selection",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Agroforestry Systems",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define agroforestry and distinguish between its three biological forms.\n"
                            "- Explain the ecological and economic importance of agroforestry.\n"
                            "- Select appropriate multi-purpose tree species for specific farm needs.\n"
                            "- Identify species cautions (avoiding Eucalyptus near water/crops, Cypress acidity)."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Core Definitions",
                    "content": {
                        "text": (
                            "- **Agroforestry:** Integrating trees or shrubs with crops and/or livestock on the same unit of land.\n"
                            "- **Agrosilvicultural:** Combining trees/shrubs with agricultural crops.\n"
                            "- **Silvopastoral:** Combining trees/shrubs with pasture and livestock.\n"
                            "- **Agrosilvopastoral:** Combining trees/shrubs, crops, pasture, and livestock on a single holding.\n"
                            "- **Allelopathy:** Biochemical inhibition of surrounding plant growth by certain tree species."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Biological Forms Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Three Primary Biological Forms of Agroforestry",
                    "content": {
                        "text": "Diagram showing Agrosilvicultural (Trees+Crops), Silvopastoral (Trees+Pasture), and Agrosilvopastoral (Trees+Crops+Animals).",
                        "svg": SVG_AGROFORESTRY_FORMS
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Multi-Purpose Tree Species Selection",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Multi-Purpose Species & Farm Roles",
                    "content": {
                        "headers": ["Tree Species", "Common Name", "Primary Agricultural Uses"],
                        "rows": [
                            ["Grevillea robusta", "Silky Oak", "High-quality timber, windbreak, fuel wood, light fodder"],
                            ["Calliandra calothyrsus", "Calliandra", "High-protein dairy fodder, nitrogen fixation, fuel wood"],
                            ["Sesbania sesban", "Sesbania", "Rapid nitrogen fixation, fodder, light shade, soil enrichment"],
                            ["Croton megalocarpus", "Croton", "Durable tool handles, fuel wood, construction timber"],
                            ["Erythrina abyssinica", "Flame Tree", "Wood carvings, nitrogen fixation, bee forage"],
                            ["Cajanus cajan", "Pigeon Pea", "Edible protein grain, leaf fodder, fuel wood twigs"],
                            ["Eucalyptus Spp.", "Blue Gum", "Fast timber poles, fuel wood, medicinal oils (Avoid near water)"],
                            ["Markhamia lutea", "Markhamia", "Roof poles, timber, windbreak, soil protection"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Species Selection Cautions & Allelopathy",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Critical Spatial & Species Cautions",
                    "content": {
                        "text": (
                            "- **Eucalyptus near Water:** Eucalyptus roots absorb water aggressively, drying up nearby rivers and springs.\n"
                            "- **Eucalyptus on Arable Land:** Releases allelopathic chemicals that inhibit seed germination of food crops.\n"
                            "- **Cypress within Farm:** Cypress leaf litter releases acid that prevents crop undergrowth; plant only on boundary.\n"
                            "- **Tall Trees near Buildings:** Expanding roots crack foundations; falling branches damage roofs during storms."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Practical Application: Smallholder Agrosilvopastoral System",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Case Study: 2-Acre Kiambu Smallholding",
                    "content": {
                        "text": (
                            "A farmer in Kiambu integrates Calliandra along terrace edges, crops maize in the alleys, and feeds pruned leaves to zero-grazed dairy cows.\n"
                            "**Ecological & Economic Benefits:**\n"
                            "- Calliandra fixes nitrogen, boosting maize yields without chemical fertilizer.\n"
                            "- High-protein fodder increases daily milk production by 2 liters per cow.\n"
                            "- Woody stems provide household firewood, eliminating fuel purchases."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Matching Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Matching Trees to Agricultural Roles",
                    "content": {
                        "text": "Match the tree species to its primary agricultural role: (1) High-protein dairy fodder, (2) Durable tool handles, (3) Rapid nitrogen fixation, (4) Carvings & bee forage.",
                        "options": [
                            "A: (1) Calliandra, (2) Croton, (3) Sesbania, (4) Erythrina",
                            "B: (1) Eucalyptus, (2) Cypress, (3) Grevillea, (4) Mango",
                            "C: (1) Sesbania, (2) Calliandra, (3) Erythrina, (4) Croton",
                            "D: (1) Grevillea, (2) Croton, (3) Calliandra, (4) Sesbania"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Calliandra provides dairy fodder, Croton yields tool handles, Sesbania fixes nitrogen quickly, and Erythrina provides carving wood."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Nutrient Pumping Mechanism",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Understanding Nutrient Pumping",
                    "content": {
                        "text": (
                            "Deep taproots of agroforestry trees penetrate deep subsoil layers to absorb leached minerals.\n"
                            "These minerals are transported to the canopy and deposited on the surface via falling leaves (litterfall).\n"
                            "Decomposition recycles these nutrients into topsoil, making them available for shallow-rooted food crops."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Ecological Functions Overview",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Ecological Contributions of Agroforestry",
                    "content": {
                        "text": (
                            "- **Soil Conservation:** Tree roots bind soil on steep slopes and terraces, reducing water erosion.\n"
                            "- **Microclimate Regulation:** Canopies reduce wind speeds and moderate ambient temperatures.\n"
                            "- **Biodiversity:** Provides habitat for beneficial pollinators and birds."
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
                            "1. Agroforestry integrates trees, crops, and livestock to maximize land productivity.\n"
                            "2. Multi-purpose species provide timber, fodder, nitrogen fixation, and firewood.\n"
                            "3. Avoid planting Eucalyptus near water sources or crops due to water depletion and allelopathy."
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
                    "title": "KCSE Model Essay: Biological Forms & Cautions (5 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Define agroforestry, state its three biological forms, and explain one spatial caution when selecting species. (5 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Definition:** Integrating trees/shrubs with crops and/or livestock on the same unit of land.\n"
                            "2. **Biological Forms:** Agrosilvicultural (Trees+Crops), Silvopastoral (Trees+Pasture), Agrosilvopastoral (Trees+Crops+Animals).\n"
                            "3. **Spatial Caution:** Avoid planting Eucalyptus near rivers or crop fields because its roots drain water aggressively and release allelopathic chemicals that stunt crops."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Nursery Types, Seed Collection, and Dormancy Breaking",
    "lesson_title": "Nursery Types, Seed Collection, and Dormancy Breaking",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Tree Seedling Nurseries",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Compare bare-root (Swaziland beds) and containerized nurseries.\n"
                            "- Identify qualities of a good mother tree for seed collection.\n"
                            "- Explain causes of tree seed dormancy.\n"
                            "- Execute 4 seed dormancy breaking treatments (Hot water, Nicking, Light burning, Chemical)."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Core Nursery Terms",
                    "content": {
                        "text": (
                            "- **Swaziland Bed:** A raised open nursery bed where bare-root seedlings grow directly in soil.\n"
                            "- **Containerized Nursery:** Raising seedlings in individual plastic sleeves, pots, or tubes.\n"
                            "- **Mother Tree:** A healthy, high-yielding, mature tree selected for collecting quality seeds.\n"
                            "- **Seed Dormancy:** A biological state where viable seeds fail to germinate under favorable conditions."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Nursery Types Comparison Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Bare-Root Swaziland Bed vs Containerized Nursery",
                    "content": {
                        "text": "Comparison diagram showing structural differences, transport advantages, and root preservation factors.",
                        "svg": SVG_NURSERY_TYPES
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Nursery Bed Comparison Table",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Swaziland Beds vs Containerized Nurseries",
                    "content": {
                        "headers": ["Feature", "Bare-Root (Swaziland Bed)", "Containerized Nursery"],
                        "rows": [
                            ["Setup Cost", "Low (No plastic containers required)", "High (Requires purchasing plastic pots/sleeves)"],
                            ["Soil Media", "Uses existing bed soil", "Requires prepared potting mix (Soil+Manure+Sand)"],
                            ["Root Preservation", "Roots exposed when uprooting; high damage", "Root-ball remains 100% intact inside container"],
                            ["Short Transport", "Easy to carry in bundles on-farm", "Heavy due to container soil weight"],
                            ["Long Transport", "Difficult; roots dry out quickly", "Easy; root-ball stays hydrated during transport"],
                            ["Field Survival Rate", "Moderate (Requires favorable rain)", "High (Minimal transplanting shock)"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Seed Selection & Mother Tree Criteria",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Selecting High-Quality Mother Trees",
                    "content": {
                        "text": (
                            "To ensure high seedling vigor, seeds must be collected from superior mother trees:\n"
                            "- **Adaptability:** Tree grows vigorously in local soil and climate.\n"
                            "- **High Yield:** Produces abundant seeds, timber, or fodder.\n"
                            "- **Health & Vigor:** Straight trunk, free from pests, diseases, or physical deformities.\n"
                            "- **Maturity:** Collect seeds from fully ripe fruits on mature trees; avoid immature fallen seeds."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Seed Dormancy & Breaking Treatments",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "4 Seed Dormancy Breaking Methods",
                    "content": {
                        "text": (
                            "**Method 1: Hot Water Soaking (Calliandra & Acacia)**\n"
                            "Boil water, remove from fire, submerge hard seeds, and let soak for 12-24 hours to crack coat.\n\n"
                            "**Method 2: Mechanical Nicking / Scarification (Croton)**\n"
                            "Use a knife or nail clipper to nick or file the hard seed coat without damaging the embryo.\n\n"
                            "**Method 3: Light Burning (Wattle - Acacia mearnsii)**\n"
                            "Pass seeds quickly through a light flame or burn dry leaf litter over seeds to fracture tough coat.\n\n"
                            "**Method 4: Chemical Acid Soaking**\n"
                            "Immerse seeds briefly in dilute acid to dissolve thick waxy seed coats."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Matching Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Matching Seeds to Dormancy Treatments",
                    "content": {
                        "text": "Match the tree seed to its correct dormancy breaking treatment: (1) Calliandra, (2) Croton megalocarpus, (3) Wattle tree (Acacia mearnsii).",
                        "options": [
                            "A: (1) Hot water soaking, (2) Mechanical nicking, (3) Light burning",
                            "B: (1) Light burning, (2) Hot water soaking, (3) Mechanical nicking",
                            "C: (1) Mechanical nicking, (2) Light burning, (3) Hot water soaking",
                            "D: (1) Chemical acid, (2) Cold water, (3) Deep freezing"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Calliandra requires hot water soaking, Croton needs mechanical nicking, and Wattle requires light burning."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Seed Storage Precautions",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Storing Agroforestry Seeds",
                    "content": {
                        "text": (
                            "- Dry seeds to 8-10% moisture content before long-term storage.\n"
                            "- Store in airtight containers in a cool, dark, insect-proof environment.\n"
                            "- Label containers with species name, collection date, and origin."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Pedagogical Note: Bare-Root Transport",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Exam Prep: Bare-Root Transport Rules",
                    "content": {
                        "text": (
                            "- **Short Distance (On-Farm):** Bare-root seedlings are easy to transport in bundles directly to adjacent fields.\n"
                            "- **Long Distance:** Bare-root seedlings are difficult to transport because roots dry out rapidly without soil containers."
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
                            "1. Swaziland beds are low-cost for on-farm use; containerized pots preserve roots for long transport.\n"
                            "2. Collect seeds from mature, healthy mother trees.\n"
                            "3. Break hard seed coat dormancy using hot water, nicking, or light burning."
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
                    "title": "KCSE Model Essay: Seed Dormancy & Calliandra Treatment (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Explain why seeds of some agroforestry trees fail to germinate, and describe how a farmer can overcome this for Calliandra calothyrsus. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Cause of Failure:** Tree seeds possess seed coat dormancy due to thick, impermeable coats that block water and oxygen entry.\n"
                            "2. **Calliandra Treatment (Hot Water Soaking):**\n"
                            "   - Heat clean water until boiling.\n"
                            "   - Remove water from the heat source.\n"
                            "   - Submerge Calliandra seeds in the hot water.\n"
                            "   - Allow seeds to soak for 12 to 24 hours until they swell, softening the coat for rapid germination."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Nursery Management, Hardening Off, and Transplanting",
    "lesson_title": "Nursery Management, Hardening Off, and Transplanting",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Nursery Management",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Execute routine nursery practices (shading, mulching, watering, pricking out, root pruning).\n"
                            "- Describe the hardening-off procedure 1 to 2 weeks before planting.\n"
                            "- Perform the 7-step seedling transplanting procedure.\n"
                            "- Calculate seedling populations and nursery buffer budgets (+15% mortality)."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Key Operations Defined",
                    "content": {
                        "text": (
                            "- **Pricking Out:** Transferring crowded seedlings from germination beds to individual pots or wider beds.\n"
                            "- **Root Pruning:** Cutting roots extending out of containers or deep into Swaziland beds.\n"
                            "- **Hardening Off:** Preparing seedlings for field conditions by reducing shade and watering 1-2 weeks prior.\n"
                            "- **Ball of Soil:** Protective soil clump left around roots during bare-root transplanting."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Root Pruning Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Root Pruning Mechanics and Lateral Root Stimulus",
                    "content": {
                        "text": "Diagram showing 4 stages: Unpruned container root, Cutting action, Apical dominance shift, and Dense lateral root mass.",
                        "svg": SVG_ROOT_PRUNING
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Routine Nursery Care Practices",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Technical Nursery Care Protocols",
                    "content": {
                        "text": (
                            "- **Watering:** Apply water twice daily (morning & evening) using a fine rose watering can.\n"
                            "- **Shading:** Erect light grass thatch frames to protect tender seedlings from solar scorching.\n"
                            "- **Weeding:** Pull weeds using a sharp pointed stick to prevent root damage to close seedlings.\n"
                            "- **Root Pruning:** Cut protruding roots to stimulate a dense, strong lateral root system inside pots."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Hardening Off & Preparation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "The Hardening Off Protocol",
                    "content": {
                        "text": (
                            "Hardening off builds physical resilience to prevent transplanting shock in the field.\n"
                            "**Procedure (1-2 Weeks Before Planting):**\n"
                            "1. Gradually remove grass thatch shade to expose seedlings to full sunlight and wind.\n"
                            "2. Reduce watering frequency from twice daily to once every two days.\n"
                            "3. Stop nitrogen fertilizer applications."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Step-by-Step Procedure: Seedling Transplanting",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "7 Steps to Transplant Tree Seedlings",
                    "content": {
                        "text": (
                            "**Step 1: Early Hole Digging**\n"
                            "Dig wide, deep planting holes early, separating topsoil and subsoil piles.\n\n"
                            "**Step 2: Manure Mixing**\n"
                            "Mix topsoil with compost manure and fill the bottom of the hole.\n\n"
                            "**Step 3: Pre-Watering Seedlings**\n"
                            "Water nursery pots thoroughly the day before transplanting so soil holds roots tightly.\n\n"
                            "**Step 4: Sleeve Removal & Root Care**\n"
                            "Slice open and remove plastic sleeves carefully without breaking the soil root-ball.\n\n"
                            "**Step 5: Placement & Depth Control**\n"
                            "Position seedling in hole center at the exact depth it grew in the nursery.\n\n"
                            "**Step 6: Backfilling & Soil Firming**\n"
                            "Fill topsoil-manure mix and press soil firmly around stem base to eliminate air pockets.\n\n"
                            "**Step 7: Immediate Watering & Mulching**\n"
                            "Irrigate immediately and apply dry grass mulch around the base (clear of stem)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Calculations: Woodlot Population & Nursery Buffer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Woodlot Tree Population & Seedling Budgeting",
                    "content": {
                        "text": (
                            "**Scenario:** A farmer wants to plant a 1-Hectare Eucalyptus woodlot (100 m x 100 m = 10,000 m²) at 2 m x 2 m spacing, with an expected 15% nursery/field mortality rate.\n\n"
                            "**Step 1: Target Field Population** = Area / (Row Spacing * Tree Spacing) = 10,000 / (2 * 2) = **2,500 trees**\n"
                            "*(Using boundary row rule: 51 rows * 51 trees = 2,601 trees)*\n\n"
                            "**Step 2: Nursery Buffer Calculation (+15% Mortality)**\n"
                            "**Required Seedlings = Target Population / (100% - Mortality Rate)**\n"
                            "Required Seedlings = 2,601 / 0.85 = **3,060 seedlings**\n\n"
                            "**Result:** Raise 3,060 seedlings in the nursery to guarantee a fully stocked 1-hectare woodlot."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Sequence Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Chronological Order of Transplanting Steps",
                    "content": {
                        "text": "Arrange the transplanting sequence: (1) Dig hole & separate topsoil, (2) Pre-water pots, (3) Remove sleeve, (4) Firm soil & mulch.",
                        "options": [
                            "A: (1) Dig hole -> (2) Pre-water -> (3) Remove sleeve -> (4) Firm soil & mulch",
                            "B: (3) Remove sleeve -> (1) Dig hole -> (4) Firm soil -> (2) Pre-water",
                            "C: (2) Pre-water -> (4) Firm soil -> (1) Dig hole -> (3) Remove sleeve",
                            "D: (4) Firm soil -> (3) Remove sleeve -> (2) Pre-water -> (1) Dig hole"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Early hole digging is followed by pre-watering pots, sleeve removal during placement, and final soil firming/mulching."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Terrace Hedgerow Spacing Math",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Terrace Calliandra Population Calculation",
                    "content": {
                        "text": (
                            "Terrace Length = 150 meters. In-row Spacing = 0.75 meters.\n"
                            "**Formula:** Trees = (Length / Spacing) + 1\n"
                            "**Calculation:** (150 / 0.75) + 1 = 200 + 1 = **201 Calliandra seedlings** required for a continuous contour hedgerow."
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
                            "1. Root pruning stimulates dense lateral root growth inside containers.\n"
                            "2. Hardening off (1-2 weeks) reduces shade and watering to prevent field transplant shock.\n"
                            "3. Add a +15% seedling buffer when budgeting tree nursery production."
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
                    "title": "KCSE Model Essay: Root Pruning Benefits (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Explain five reasons why root pruning is carried out regularly on containerized tree seedlings in a nursery. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. Prevents single taproots from penetrating deep into unproductive nursery subsoil.\n"
                            "2. Stimulates development of a short, dense, and strong lateral root system inside pots.\n"
                            "3. Makes lifting of containers easy during transplanting.\n"
                            "4. Reduces physical root damage during transport to the field.\n"
                            "5. Encourages rapid field establishment and prevents root-bound transplant shock."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Tree Maintenance, Grafting Mechanics, and Sustainable Harvesting",
    "lesson_title": "Tree Maintenance, Grafting Mechanics, and Sustainable Harvesting",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Tree Management & Grafting",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 4 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Apply tree maintenance practices (protection, pruning, coppicing).\n"
                            "- Explain cambium alignment mechanics in grafting (Whip, Side, Approach).\n"
                            "- Compare agroforestry spatial layouts (Alley Cropping, Multi-Storey, Woodlots).\n"
                            "- Identify 6 sustainable tree harvesting methods (Pollarding, Coppicing, Lopping, Shaking, Cutting Back, Thinning)."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Core Maintenance & Grafting Terms",
                    "content": {
                        "text": (
                            "- **Grafting:** Vegetatively uniting a scion shoot with a rooted stock stem to grow as one plant.\n"
                            "- **Rootstock:** Lower rooted portion providing water and mineral absorption.\n"
                            "- **Scion:** Upper shoot or bud taken from a high-yielding tree to form the future canopy.\n"
                            "- **Alley Cropping:** Growing food crops in alleys between parallel hedgerows of nitrogen-fixing trees.\n"
                            "- **Pollarding:** Cutting the crown 2-3 meters high to harvest branches above livestock reach."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Mechanical Methods of Grafting Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Mechanical Methods of Grafting & Cambium Alignment",
                    "content": {
                        "text": "Diagram showing 1. Whip & Tongue grafting, 2. Side grafting, and 3. Approach grafting.",
                        "svg": SVG_GRAFTING_METHODS
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Grafting Mechanics & Cambium Union",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Science of Graft Unions",
                    "content": {
                        "text": (
                            "- **Cambium Layer:** Microscopic layer of dividing meristematic cells between wood and bark.\n"
                            "- **Vascular Contact:** Matching cuts on scion and rootstock bring cambium layers into tight contact.\n"
                            "- **Callus Tissue:** Cells divide rapidly to form callus tissue, reconnecting xylem and phloem vascular pathways."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Agroforestry Spatial Layouts",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Agroforestry Spatial Layouts",
                    "content": {
                        "headers": ["Spatial Layout", "Design Structure", "Primary Benefits"],
                        "rows": [
                            ["Alley Cropping", "Parallel hedgerows (4-6 m alleys) with crops between", "Green manure, weed suppression, windbreak, soil fertility"],
                            ["Multi-Storey Cropping", "Layered canopy (Tall trees + Medium trees + Low crops)", "Maximal solar/water efficiency, microclimate protection"],
                            ["Woodlots", "High-density plots (2 m x 2 m spacing) on steep/rocky sites", "Timber poles, firewood, land rehabilitation"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Sustainable Tree Harvesting Methods",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "6 Sustainable Tree Harvesting Methods",
                    "content": {
                        "text": (
                            "**1. Pollarding:** Cut crown 2-3 meters above ground; new shoots sprout out of livestock reach.\n"
                            "**2. Coppicing:** Cut stem 10-50 cm above ground at a slanting angle to drain rainwater.\n"
                            "**3. Lopping (Side Pruning):** Remove selected side branches for fuel/fodder, leaving main trunk straight.\n"
                            "**4. Shaking:** Vigorously shake branches to harvest mature seeds/pods without cutting wood.\n"
                            "**5. Cutting Back:** Cut trunk at base to stimulate youthful vegetative rejuvenation (e.g. coffee).\n"
                            "**6. Thinning:** Remove overcrowded intermediate trees to give remaining trees space and light."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Diagnostic Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Spotting Faults in Coppicing Procedure",
                    "content": {
                        "text": "A student cuts a tree stump 5 cm above ground with a flat horizontal cut. What are the two critical mechanical faults?",
                        "options": [
                            "A: Cut is too low (<10 cm) and flat (must be slanting to drain rainwater and prevent fungal rot).",
                            "B: Cut is too high (>2 meters) and made with a pruning saw.",
                            "C: Student failed to apply grease and paint.",
                            "D: Coppicing is forbidden on timber trees."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Coppicing cuts must be 10-50 cm high and made at a slanting angle to drain rainwater and prevent rot."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Tree Protection Protocols",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Protecting Young Field Trees",
                    "content": {
                        "text": (
                            "- Surround individual young trees with wooden guard posts or wire netting enclosures.\n"
                            "- Prevents destruction from browsing goats, sheep, and cattle.\n"
                            "- Construct firebreaks around woodlots to prevent wildfire damage."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Key Farm Sites for Agroforestry",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Target Planting Sites on Farms",
                    "content": {
                        "text": (
                            "- **Farm Boundaries:** Live fences marking borders and providing firewood.\n"
                            "- **River Banks:** Protective trees preventing riverbank erosion and safeguarding water catchments.\n"
                            "- **Steep Slopes & Terraces:** Contour hedgerows anchoring soil and slowing surface runoff."
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
                            "1. Grafting unites a scion and rootstock by aligning cambium layers.\n"
                            "2. Alley cropping and multi-storey systems optimize light and soil nutrients.\n"
                            "3. Sustainable harvesting (pollarding, coppicing at a slanting angle) allows continuous regeneration."
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
                    "title": "KCSE Model Essay: Alley Cropping Benefits (12 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Describe the spatial layout and five agronomic/economic benefits of Alley Cropping on a smallholder farm. (12 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Spatial Layout:** Food crops are grown in wide corridors (alleys 4-6 m wide) between parallel hedgerows of nitrogen-fixing trees.\n"
                            "2. **Five Benefits:**\n"
                            "   - **Soil Fertility:** Biological nitrogen fixation enriches the root zone.\n"
                            "   - **Green Manure:** Pruned leaves incorporated into soil supply organic matter.\n"
                            "   - **Windbreak:** Hedgerows protect food crops from physical wind damage.\n"
                            "   - **Weed Suppression:** Dense hedgerow shade suppresses weed growth.\n"
                            "   - **Wood Products:** Prunings provide fuel wood, stakes, and livestock fodder."
                        )
                    }
                }
            ]
        }
    ]
}

TOPIC_7_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA
]
