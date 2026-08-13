"""
VLearn Form 4 Agriculture — Topic 3 Data File
Topic 3: Farm Power and Machinery

Contains structured data for all 5 Learning Modules / Lessons:
  Lesson 1: Sources and Uses of Farm Power (10 Pages)
  Lesson 2: Four-Stroke and Two-Stroke Internal Combustion Engines (10 Pages)
  Lesson 3: Tractor Systems, Lubrication, and Servicing (10 Pages)
  Lesson 4: Tractor-Drawn Implements (10 Pages)
  Lesson 5: Animal-Drawn Implements (10 Pages)
Total: 50 Pages, ~180 Granular Lesson Blocks
"""

# =============================================================================
# SVG DIAGRAM DEFINITIONS
# =============================================================================

SVG_BIOGAS_DIGESTER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Biogas Digester Process &amp; Structural Components</title>

  <!-- Underground Soil Line -->
  <line x1="50" y1="180" x2="750" y2="180" stroke="#a16207" stroke-width="4" stroke-dasharray="8,4"/>
  <text x="70" y="170" font-family="Arial" font-size="12" fill="#eab308" font-weight="bold">Ground Level</text>

  <!-- Mixing Inlet Tank -->
  <rect x="80" y="120" width="100" height="80" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="130" y="150" font-family="Arial" font-size="11" fill="#f8fafc" font-weight="bold" text-anchor="middle">Mixing Tank</text>
  <text x="130" y="170" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">(Manure + Water 1:1)</text>

  <!-- Inlet Pipe to Dome -->
  <path d="M 160 190 L 250 260" stroke="#64748b" stroke-width="12" fill="none"/>

  <!-- Subterranean Concrete Dome -->
  <path d="M 230 250 Q 400 120 570 250 L 570 380 Q 400 420 230 380 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="320" font-family="Arial" font-size="14" fill="#38bdf8" font-weight="bold" text-anchor="middle">Anaerobic Digestion Chamber</text>
  <text x="400" y="345" font-family="Arial" font-size="10" fill="#94a3b8" text-anchor="middle">(Methanogenic Bacteria at Work)</text>

  <!-- Gas Collector Chamber (Top Dome) -->
  <path d="M 320 185 Q 400 140 480 185 Z" fill="#eab308" opacity="0.3"/>
  <text x="400" y="175" font-family="Arial" font-size="12" fill="#fde047" font-weight="bold" text-anchor="middle">Methane Gas (CH4)</text>

  <!-- Gas Pipe Outlet -->
  <rect x="393" y="80" width="14" height="65" fill="#fde047"/>
  <path d="M 400 80 L 700 80" stroke="#fde047" stroke-width="4" fill="none"/>
  <text x="560" y="70" font-family="Arial" font-size="11" fill="#fde047" font-weight="bold">Piped Methane Gas to Farmhouse</text>

  <!-- Outlet Pipe to Slurry Pit -->
  <path d="M 550 270 L 640 190" stroke="#64748b" stroke-width="12" fill="none"/>

  <!-- Bio-Slurry Overflow Pit -->
  <rect x="620" y="140" width="100" height="70" fill="#334155" stroke="#22c55e" stroke-width="2"/>
  <text x="670" y="170" font-family="Arial" font-size="11" fill="#4ade80" font-weight="bold" text-anchor="middle">Bio-Slurry Pit</text>
  <text x="670" y="190" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">(Rich Organic Fertilizer)</text>
</svg>"""

SVG_FOUR_STROKE_ENGINE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Four-Stroke Engine Piston Cycle (Induction, Compression, Power, Exhaust)</title>

  <!-- Stage 1: Induction -->
  <g transform="translate(30, 40)">
    <rect x="20" y="40" width="120" height="180" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <!-- Valves: Intake Open, Exhaust Closed -->
    <line x1="40" y1="40" x2="40" y2="65" stroke="#22c55e" stroke-width="4"/> <!-- Open -->
    <line x1="120" y1="40" x2="120" y2="40" stroke="#ef4444" stroke-width="4"/> <!-- Closed -->
    <!-- Piston moving DOWN -->
    <rect x="30" y="110" width="100" height="50" fill="#38bdf8" rx="4"/>
    <path d="M 80 135 L 80 170" stroke="#f8fafc" stroke-width="3"/>
    <text x="80" y="240" font-family="Arial" font-size="12" fill="#38bdf8" font-weight="bold" text-anchor="middle">1. INDUCTION</text>
    <text x="80" y="260" font-family="Arial" font-size="10" fill="#94a3b8" text-anchor="middle">Intake Open | Piston ↓</text>
  </g>

  <!-- Stage 2: Compression -->
  <g transform="translate(220, 40)">
    <rect x="20" y="40" width="120" height="180" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
    <!-- Both Valves Closed -->
    <line x1="40" y1="40" x2="40" y2="40" stroke="#ef4444" stroke-width="4"/>
    <line x1="120" y1="40" x2="120" y2="40" stroke="#ef4444" stroke-width="4"/>
    <!-- Piston moving UP -->
    <rect x="30" y="60" width="100" height="50" fill="#eab308" rx="4"/>
    <path d="M 80 85 L 80 120" stroke="#f8fafc" stroke-width="3"/>
    <text x="80" y="240" font-family="Arial" font-size="12" fill="#fde047" font-weight="bold" text-anchor="middle">2. COMPRESSION</text>
    <text x="80" y="260" font-family="Arial" font-size="10" fill="#94a3b8" text-anchor="middle">Both Closed | Piston ↑</text>
  </g>

  <!-- Stage 3: Power -->
  <g transform="translate(410, 40)">
    <rect x="20" y="40" width="120" height="180" fill="#1e293b" stroke="#f97316" stroke-width="2"/>
    <!-- Spark / Explosion -->
    <circle cx="80" cy="45" r="8" fill="#f97316"/>
    <!-- Both Valves Closed -->
    <line x1="40" y1="40" x2="40" y2="40" stroke="#ef4444" stroke-width="4"/>
    <line x1="120" y1="40" x2="120" y2="40" stroke="#ef4444" stroke-width="4"/>
    <!-- Piston driven DOWN -->
    <rect x="30" y="130" width="100" height="50" fill="#f97316" rx="4"/>
    <path d="M 80 155 L 80 190" stroke="#f8fafc" stroke-width="3"/>
    <text x="80" y="240" font-family="Arial" font-size="12" fill="#f97316" font-weight="bold" text-anchor="middle">3. POWER</text>
    <text x="80" y="260" font-family="Arial" font-size="10" fill="#94a3b8" text-anchor="middle">Ignition | Piston ↓↓</text>
  </g>

  <!-- Stage 4: Exhaust -->
  <g transform="translate(600, 40)">
    <rect x="20" y="40" width="120" height="180" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <!-- Exhaust Open, Intake Closed -->
    <line x1="40" y1="40" x2="40" y2="40" stroke="#ef4444" stroke-width="4"/>
    <line x1="120" y1="40" x2="120" y2="65" stroke="#22c55e" stroke-width="4"/>
    <!-- Piston moving UP -->
    <rect x="30" y="70" width="100" height="50" fill="#ef4444" rx="4"/>
    <path d="M 80 95 L 80 130" stroke="#f8fafc" stroke-width="3"/>
    <text x="80" y="240" font-family="Arial" font-size="12" fill="#f87171" font-weight="bold" text-anchor="middle">4. EXHAUST</text>
    <text x="80" y="260" font-family="Arial" font-size="10" fill="#94a3b8" text-anchor="middle">Exhaust Open | Piston ↑</text>
  </g>
</svg>"""

SVG_PLOUGH_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Structural Comparison: Mouldboard vs Disc Plough</title>

  <!-- Left Side: Mouldboard Plough -->
  <g transform="translate(40, 40)">
    <rect x="10" y="10" width="340" height="370" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="180" y="40" font-family="Arial" font-size="15" fill="#38bdf8" font-weight="bold" text-anchor="middle">MOULDBOARD PLOUGH</text>
    
    <!-- Share & Mouldboard Curved Profile -->
    <path d="M 70 280 L 150 280 L 220 180 Q 250 140 180 140 L 100 220 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="110" y="295" font-family="Arial" font-size="10" fill="#f8fafc">Plough Share (Initial Cut)</text>
    <text x="180" y="160" font-family="Arial" font-size="10" fill="#f8fafc">Curved Mouldboard (Inverts Soil)</text>
    
    <text x="180" y="330" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">• Slices and completely inverts furrow</text>
    <text x="180" y="350" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">• Best for stone-free moist soils</text>
  </g>

  <!-- Right Side: Disc Plough -->
  <g transform="translate(420, 40)">
    <rect x="10" y="10" width="340" height="370" fill="#1e293b" stroke="#f97316" stroke-width="2" rx="8"/>
    <text x="180" y="40" font-family="Arial" font-size="15" fill="#f97316" font-weight="bold" text-anchor="middle">DISC PLOUGH</text>
    
    <!-- Concave Steel Disc Profile -->
    <path d="M 120 140 Q 220 200 120 280 L 150 280 Q 250 200 150 140 Z" fill="#ea580c" stroke="#f97316" stroke-width="2"/>
    <!-- Scraper -->
    <rect x="190" y="220" width="40" height="15" fill="#fde047" rx="2"/>
    <text x="240" y="232" font-family="Arial" font-size="10" fill="#fde047">Scraper</text>
    <text x="110" y="130" font-family="Arial" font-size="10" fill="#f8fafc">Concave Steel Disc</text>

    <text x="180" y="330" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">• Rolls over stones &amp; cuts heavy trash</text>
    <text x="180" y="350" font-family="Arial" font-size="11" fill="#cbd5e1" text-anchor="middle">• Ideal for hard, dry, or obstacles</text>
  </g>
</svg>"""

SVG_OX_PLOUGH = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Structural Anatomy of an Ox-Plough</title>

  <!-- Main Beam -->
  <path d="M 150 250 L 500 200 L 680 140" stroke="#94a3b8" stroke-width="8" fill="none"/>
  <text x="350" y="205" font-family="Arial" font-size="12" fill="#f8fafc" font-weight="bold">Main Beam</text>

  <!-- Handles -->
  <path d="M 150 250 L 80 100" stroke="#64748b" stroke-width="6" fill="none"/>
  <path d="M 150 250 L 110 90" stroke="#64748b" stroke-width="6" fill="none"/>
  <text x="60" y="80" font-family="Arial" font-size="12" fill="#f8fafc" font-weight="bold">Operator Handles</text>

  <!-- Share & Mouldboard -->
  <path d="M 130 320 L 220 320 L 260 250 L 180 250 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="140" y="340" font-family="Arial" font-size="11" fill="#38bdf8" font-weight="bold">Plough Share</text>
  <text x="210" y="240" font-family="Arial" font-size="11" fill="#38bdf8" font-weight="bold">Mouldboard</text>

  <!-- Land Wheel at Front -->
  <circle cx="580" cy="300" r="35" fill="none" stroke="#eab308" stroke-width="4"/>
  <line x1="580" y1="300" x2="580" y2="185" stroke="#eab308" stroke-width="4"/>
  <text x="540" y="355" font-family="Arial" font-size="11" fill="#fde047" font-weight="bold">Land Wheel (Depth Regulator)</text>

  <!-- Draft Rod at Front -->
  <path d="M 500 200 L 720 200" stroke="#22c55e" stroke-width="5"/>
  <circle cx="720" cy="200" r="8" fill="#4ade80"/>
  <text x="660" y="225" font-family="Arial" font-size="11" fill="#4ade80" font-weight="bold">Draft Rod &amp; Clevis</text>
</svg>"""


# =============================================================================
# LESSON 1 DATA: Sources and Uses of Farm Power (10 Pages)
# =============================================================================

LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Sources and Uses of Farm Power",
    "lesson_title": "Sources and Uses of Farm Power",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Farm Power & Mechanization",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define farm power and categorize biological, fossil, and renewable power sources.\n"
                            "- Compare uses, advantages, and limitations of 8 farm power sources.\n"
                            "- Detail the 4-stage anaerobic process of a farm biogas digester.\n"
                            "- Evaluate power source selection for steep vs flat agricultural terrains.\n"
                            "- Solve KCSE exam questions on farm energy limitations."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Definition & Scope of Farm Power",
                    "content": {
                        "text": (
                            "Farm power is defined as any form of energy used on the farm to perform agricultural work. "
                            "It is the physical rate at which tillage, harvesting, pumping, processing, or transport operations are executed. "
                            "Choosing an appropriate power source depends on capital cost, availability, efficiency, ease of control, and terrain suitability."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Biological & Fossil Power Sources",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Human, Animal & Fossil Energy",
                    "content": {
                        "text": (
                            "- **Human Power:** Highly versatile for light tasks (weeding, spraying, milking), requiring no tool capital, but limited by low power output and high fatigue.\n"
                            "- **Animal Power:** Utilizes draught animals (oxen, donkeys, camels) harnessed via wooden yokes. Ideal for primary land preparation on steep or narrow slopes where tractors cannot operate.\n"
                            "- **Fossil Fuels:** Petrol, diesel, and kerosene powering internal combustion engines. Highly concentrated, controllable energy, but non-renewable and capital-intensive."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Renewable & Natural Energy Sources",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Wind, Solar, Water, Geothermal & Biomass",
                    "content": {
                        "text": (
                            "- **Wind Power:** Used for pumping water from boreholes and winnowing grains. Clean and renewable, but highly unpredictable.\n"
                            "- **Solar Power:** Photovoltaic panels generate electricity for pumping and lighting; solar thermal collectors dry crops (maize, beans).\n"
                            "- **Biomass & Biogas:** Decomposing cattle manure anaerobically in a digester to yield methane (CH4) gas for cooking and lighting."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Comprehensive Power Sources Comparison Table",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Comparison of Farm Power Sources",
                    "content": {
                        "text": (
                            "| Power Source | Primary Farm Uses | Key Stated Advantages | Key Stated Limitations |\n"
                            "|---|---|---|---|\n"
                            "| Human Power | Manual weeding, spraying, milking | High versatility, no capital tools | Slow speed, low output |\n"
                            "| Animal Power | Ploughing, weeding, transport | Cheaper than tractors, works on steep slopes | Requires grazing land, animal fatigue |\n"
                            "| Wind Power | Water pumping, winnowing | Renewable, low running costs | Unpredictable, weather dependent |\n"
                            "| Water Power | Overhead irrigation, mills | High force output, zero fuel cost | Location restricted, seasonal |\n"
                            "| Biogas | Cooking, heating, lighting | Utilizes farm waste, clean methane | High labor for manure handling |\n"
                            "| Fossil Fuel | Tractor operations, engines | Highly concentrated & controllable | Non-renewable, high fuel cost |\n"
                            "| Solar Power | Crop drying, water pumping | Free infinite energy | Zero output on cloudy days/nights |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Architectural Diagram: Biogas Digester Unit",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Biogas Digester Process & Structural Components",
                    "content": {
                        "text": "Diagram showing manure mixing tank, subterranean concrete dome digester, gas collector pipe, and bio-slurry pit.",
                        "svg": SVG_BIOGAS_DIGESTER
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Visual Guide: Farm Biogas System",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Farm Biogas Digester Unit",
                    "content": {
                        "text": "Concrete dome biogas digester in a zero-grazing dairy farm showing manure inlet and gas delivery pipes.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/2/29/Biogas_digester_plant.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Biogas_digester_plant.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Learning: Terrain Power Choice",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Steep Terrain Power Choice",
                    "content": {
                        "text": "A smallholder dairy farmer on a 2.5-hectare plot in Meru with steep 25-degree slopes needs a primary tillage power source. Which option is best?",
                        "options": [
                            "A: A 70-HP heavy 4-wheel drive diesel tractor.",
                            "B: Hand jembes only.",
                            "C: A pair of trained draught oxen with an ox-plough.",
                            "D: A stationary electric grinding mill."
                        ],
                        "correct_answer_index": 2,
                        "explanation": "Oxen are affordable, easy to maintain, and can operate safely on steep slopes where heavy tractors risk overturning."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application Scenario",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Kuria Tobacco Curing Transition",
                    "content": {
                        "text": (
                            "**Scenario:** A Kuria farmer relies on wood fuel for tobacco curing, but deforestation restrictions are raising costs.\n\n"
                            "**Resolution:** Transition to solar thermal drying collectors. Provides clean, infinite heat for crop drying without wood fuel expenditure."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Farm Power Core Recall",
                    "content": {
                        "text": "1. Name two operations where wind power is used.\n2. Why is nuclear energy unfeasible for smallholder Kenyan farms?\n3. What gas is produced by anaerobic manure digestion?",
                        "options": [
                            "A: Pumping water & winnowing; Requires dangerous high-cost infrastructure; Methane (CH4).",
                            "B: Ploughing & planting; Too small; Carbon monoxide.",
                            "C: Milking & spraying; Causes rain; Nitrogen gas.",
                            "D: Transport & weeding; Illegal; Oxygen gas."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Wind power pumps water and winnows; nuclear energy requires complex high-cost plant infrastructure; biogas produces methane."
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
                    "title": "KCSE Model Essay: Limitations of Wood & Charcoal Fuel (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Explain four disadvantages of relying on wood and charcoal fuel as the primary energy source on a farm. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Exhaustibility:** Wood fuel is non-renewable; continuous cutting causes deforestation and fuel scarcity.\n"
                            "2. **Low Operational Versatility:** Cannot be used directly to run mechanical tillage, milking, or stationary farm machinery.\n"
                            "3. **Bulkiness:** Extremely bulky and expensive to transport and store on the farm.\n"
                            "4. **High Volume Consumption:** Requires huge quantities to generate heat, accelerating environmental degradation."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 2 DATA: Four-Stroke and Two-Stroke Internal Combustion Engines (10 Pages)
# =============================================================================

LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Four-Stroke and Two-Stroke Internal Combustion Engines",
    "lesson_title": "Four-Stroke and Two-Stroke Internal Combustion Engines",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Physics of Internal Combustion Engines",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain energy conversion in internal combustion (IC) engines.\n"
                            "- Detail the 4 strokes of a four-stroke engine (Induction, Compression, Power, Exhaust).\n"
                            "- Compare four-stroke vs two-stroke engine mechanical operation.\n"
                            "- Contrast petrol (spark ignition) and diesel (compression ignition) engine cycles.\n"
                            "- Calculate engine displacement volume and compression ratios."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Engine Kinematics & Terminology",
                    "content": {
                        "text": (
                            "An internal combustion engine converts chemical energy in fuel into thermal heat energy, "
                            "which expands gases inside a cylinder to drive a piston downward, converting linear motion into mechanical rotational motion via the crankshaft.\n\n"
                            "- **TDC (Top Dead Center):** Highest point of piston travel in cylinder.\n"
                            "- **BDC (Bottom Dead Center):** Lowest point of piston travel in cylinder.\n"
                            "- **Bore:** Internal diameter of cylinder.\n"
                            "- **Stroke:** Distance traveled by piston between TDC and BDC."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Four-Stroke Cycle Protocol",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Induction, Compression, Power, Exhaust",
                    "content": {
                        "text": (
                            "1. **Induction Stroke:** Piston moves down (TDC -> BDC). Intake valve opens; fuel-air mixture (petrol) or pure air (diesel) is sucked into cylinder.\n"
                            "2. **Compression Stroke:** Piston moves up (BDC -> TDC). Both valves closed; fuel-air mixture or air is compressed into tight clearance volume.\n"
                            "3. **Power Stroke:** Both valves closed. Spark plug fires (petrol) or diesel fuel injected into hot compressed air (diesel). Expanding gases force piston down (TDC -> BDC).\n"
                            "4. **Exhaust Stroke:** Piston moves up (BDC -> TDC). Exhaust valve opens; burnt gases are pushed out of cylinder."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Four-Stroke vs Two-Stroke Engines",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Comparison of Four-Stroke vs Two-Stroke Engines",
                    "content": {
                        "text": (
                            "| Feature | Four-Stroke Engine | Two-Stroke Engine |\n"
                            "|---|---|---|\n"
                            "| Cycles per Power Stroke | 4 piston strokes (2 crankshaft revs) | 2 piston strokes (1 crankshaft rev) |\n"
                            "| Valve Mechanism | Poppet valves operated by camshaft | Transfer & exhaust ports in cylinder wall |\n"
                            "| Fuel Efficiency | Highly efficient, clean exhaust | Less efficient, unburnt fuel escapes |\n"
                            "| Lubrication | Separate oil sump & oil pump | Oil mixed directly into petrol fuel |\n"
                            "| Weight & Complexity | Heavier, complex mechanical parts | Lightweight, compact, fewer moving parts |\n"
                            "| Primary Application | Tractors, cars, heavy pumps | Chainsaws, knapsack sprayers, lawnmowers |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Petrol (Spark) vs Diesel (Compression) Engines",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Ignition & Fuel Mixing Differences",
                    "content": {
                        "text": (
                            "- **Petrol Engine (Spark Ignition):** Sucks fuel-air mixture via carburetor during induction; uses electric spark plug to ignite mixture at lower compression ratios (7:1 to 10:1).\n"
                            "- **Diesel Engine (Compression Ignition):** Sucks pure air during induction; compresses air to extreme high pressure/heat (compression ratio 14:1 to 22:1); fuel injector sprays atomized diesel into hot air, triggering spontaneous combustion without a spark plug."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Technical Vector Diagram: Four-Stroke Cycle",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Four-Stroke Engine Piston Cycle",
                    "content": {
                        "text": "Diagram showing the 4 phases: Induction, Compression, Power, and Exhaust with piston positions and valve states.",
                        "svg": SVG_FOUR_STROKE_ENGINE
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Visual Guide: Diesel Engine Model",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Cutaway Model of a Four-Stroke Diesel Engine",
                    "content": {
                        "text": "Cutaway model showing cylinder bore, piston, connecting rod, camshaft, valves, and crankshaft.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Diesel_engine_cutaway.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY 3.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Diesel_engine_cutaway.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Step-by-Step Procedure: Engine Stroke Identification",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Diagnosing Engine Stroke Phase",
                    "content": {
                        "text": (
                            "**Purpose:** To determine valve position and stroke state during engine overhaul.\n\n"
                            "**Step 1: Rotate Crankshaft to TDC**\n"
                            "Turn crankshaft pulley manually until piston reaches Top Dead Center.\n\n"
                            "**Step 2: Observe Valve Clearance**\n"
                            "Check intake and exhaust rocker arms for clearance play.\n\n"
                            "**Step 3: Identify Compression vs Overlap**\n"
                            "If both valves have clearance, cylinder is at TDC Compression. If both rocker arms press valves, cylinder is at Exhaust/Induction overlap.\n\n"
                            "**Step 4: Rotate 180 Degrees Downward**\n"
                            "Rotate crankshaft to BDC; check if intake valve opened (Induction) or stayed closed (Power).\n\n"
                            "**Step 5: Verify Firing Order**\n"
                            "Match cylinder stroke phases against manufacturer firing order (e.g., 1-3-4-2)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Worked Calculation: Engine Displacement Volume",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Worked Example: Engine Displacement & Compression Ratio",
                    "content": {
                        "text": (
                            "**Scenario:** A 4-cylinder tractor engine has a bore of 10 cm and a stroke of 12 cm. Clearance volume per cylinder is 50 cm³.\n\n"
                            "**Calculations:**\n"
                            "1. Swept Volume per cylinder (Vs) = 3.1416 × 25 × 12 = 942.5 cm³.\n"
                            "2. Total Engine Displacement = 942.5 cm³ × 4 = 3,770 cm³ (3.77 Liters).\n"
                            "3. Total Cylinder Volume (Vt) = Vs + Vc = 942.5 + 50 = 992.5 cm³.\n"
                            "4. Compression Ratio = Vt / Vc = 992.5 / 50 = 19.85:1 (Standard Diesel Compression Ratio)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Engine Physics Core Recall",
                    "content": {
                        "text": "1. What valve state occurs during the Compression stroke?\n2. What component ignites fuel in a diesel engine?\n3. How many crankshaft revolutions produce 1 power stroke in a 4-stroke engine?",
                        "options": [
                            "A: Both valves closed; High compression heat (spontaneous ignition); 2 revolutions.",
                            "B: Intake valve open; Spark plug; 1 revolution.",
                            "C: Exhaust valve open; Carburetor; 4 revolutions.",
                            "D: Both valves open; Magneto; 0.5 revolutions."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Both valves are closed during compression; diesel relies on compression heat; 4-stroke requires 2 crankshaft revolutions per power stroke."
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
                    "title": "KCSE Model Essay: Four-Stroke vs Two-Stroke Engines (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Compare four-stroke and two-stroke internal combustion engines. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Strokes per Cycle:** 4-stroke requires 4 piston strokes (2 crank revs); 2-stroke requires 2 piston strokes (1 crank rev).\n"
                            "2. **Valves vs Ports:** 4-stroke uses poppet valves driven by camshaft; 2-stroke uses cylinder wall ports.\n"
                            "3. **Lubrication:** 4-stroke has separate oil sump; 2-stroke mixes oil into petrol fuel.\n"
                            "4. **Efficiency:** 4-stroke is cleaner and fuel-efficient; 2-stroke leaks unburnt fuel mixture through exhaust.\n"
                            "5. **Uses:** 4-stroke powers heavy tractors/cars; 2-stroke powers portable tools (chainsaws, mowers)."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 3 DATA: Tractor Systems, Lubrication, and Servicing (10 Pages)
# =============================================================================

LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Tractor Systems, Lubrication, and Servicing",
    "lesson_title": "Tractor Systems, Lubrication, and Servicing",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Major Tractor Systems Overview",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify 6 major tractor mechanical systems.\n"
                            "- Detail fuel system maintenance and bleeding air locks.\n"
                            "- Explain cooling, lubrication, electrical, transmission, and hydraulic systems.\n"
                            "- Execute an 8-step daily tractor servicing checklist.\n"
                            "- Calculate effective tractor field capacity (ha/hr) and fuel rates."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Overview of Functional Systems",
                    "content": {
                        "text": (
                            "A tractor is a mobile power unit comprising 6 integrated systems:\n"
                            "1. **Fuel System:** Stores, filters, and injects clean fuel into cylinders.\n"
                            "2. **Cooling System:** Maintains optimal operating temperature (water/radiator/thermostat).\n"
                            "3. **Lubrication System:** Reduces friction and wear (oil sump, filter, oil pump).\n"
                            "4. **Electrical System:** Battery, starter motor, alternator, lights.\n"
                            "5. **Transmission System:** Clutch, gearbox, differential gear, final drives.\n"
                            "6. **Hydraulic & PTO System:** Operates 3-point linkage and powers rotary implements."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Fuel System & Bleeding Air Locks",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Diesel Fuel Line Mechanics & Air Lock Bleeding",
                    "content": {
                        "text": (
                            "The diesel fuel system consists of fuel tank, sediment bowl, primary filter, lift pump, secondary fine filter, and high-pressure injection pump. "
                            "If air enters the fuel line (air lock), fuel flow stops and the engine stalls. "
                            "Bleeding procedure: loosen bleed screws on filter and injection pump, operate primer pump lever until bubble-free fuel flows out, then tighten screws."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Cooling & Lubrication Systems Maintenance",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Preventing Overheating & Engine Seizure",
                    "content": {
                        "text": (
                            "- **Cooling System:** Radiator, fan belt tension, water pump, and thermostat. Remove chaff from radiator fins daily; check coolant level.\n"
                            "- **Lubrication System:** Engine oil reduces metal friction, seals piston rings, and cools internal parts. Check dipstick oil level daily; replace oil filter at scheduled engine hours."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Transmission, Differential & PTO Mechanics",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Power Transmission to Wheels & Implements",
                    "content": {
                        "text": (
                            "- **Clutch:** Disengages engine power from transmission for smooth gear changes.\n"
                            "- **Differential Gear:** Allows outer rear wheel to rotate faster than inner wheel when turning corners.\n"
                            "- **Differential Lock:** Locks rear axles together to prevent wheel spin in muddy soils.\n"
                            "- **Power Take-Off (PTO):** Rotating spline shaft at rear of tractor driving rotary mowers and balers."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Step-by-Step Procedure: Daily Tractor Servicing",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Daily Tractor Pre-Start Checklist",
                    "content": {
                        "text": (
                            "**Purpose:** To perform daily preventative maintenance before tractor operation.\n\n"
                            "**Step 1: Check Engine Dipstick Oil Level**\n"
                            "Pull dipstick, wipe clean, re-insert; verify oil level is between MIN and MAX marks.\n\n"
                            "**Step 2: Check Radiator Coolant Level**\n"
                            "Inspect coolant expansion tank; top up with clean water if low.\n\n"
                            "**Step 3: Inspect Air Cleaner Dust Bowl**\n"
                            "Empty dust cap on oil-bath or dry-element air cleaner.\n\n"
                            "**Step 4: Check Fuel Sediment Bowl**\n"
                            "Inspect glass bowl under fuel tank for accumulated water or dirt; drain if necessary.\n\n"
                            "**Step 5: Check Tyre Inflation Pressure**\n"
                            "Inspect front and rear tyres for cracks, punctures, and correct pressure.\n\n"
                            "**Step 6: Check Fan Belt Tension**\n"
                            "Press fan belt midway; ensure finger deflection is within 12–19 mm.\n\n"
                            "**Step 7: Grease Lubrication NIPPLES**\n"
                            "Apply grease using grease gun to steering joints, 3-point linkage, and kingpins.\n\n"
                            "**Step 8: Test Brake & Clutch Pedal Free Play**\n"
                            "Verify pedals move smoothly before starting engine."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Visual Guide: Modern Farm Tractor",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Agricultural Farm Tractor",
                    "content": {
                        "text": "Four-wheel drive agricultural tractor showing engine housing, rear 3-point linkage, and PTO shaft.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Modern_farm_tractor.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Modern_farm_tractor.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Worked Calculation: Tractor Field Capacity",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Worked Example: Effective Field Capacity & Fuel Budget",
                    "content": {
                        "text": (
                            "**Scenario:** A tractor pulling a 3-disc plough with a total working width of 1.2 meters operates at a speed of 6 km/h with 80% field efficiency. Calculate field capacity in ha/hr.\n\n"
                            "**Calculations:**\n"
                            "1. Theoretical Field Capacity (TFC) = (Width in meters × Speed in km/h) / 10 = (1.2 × 6) / 10 = 0.72 ha/hr.\n"
                            "2. Effective Field Capacity (EFC) = TFC × Efficiency = 0.72 × 0.80 = 0.576 ha/hr.\n"
                            "3. Time to plough 10 hectares = 10 / 0.576 = 17.36 hours.\n"
                            "4. Fuel Budget (at 8 Liters/hr consumption) = 17.36 × 8 = 138.9 Liters of diesel."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application Scenario",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Narok Wheat Farm Troubleshooting",
                    "content": {
                        "text": (
                            "**Scenario:** A tractor stalled in a Narok wheat field after ran out of fuel. Refilling the tank failed to start the engine.\n\n"
                            "**Resolution:** The fuel system developed an air lock. The driver bled the secondary filter and injection pump bleed screws using the manual lift pump lever, clearing air bubbles and restoring engine start."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Tractor Maintenance Recall",
                    "content": {
                        "text": "1. What is the function of the differential lock?\n2. What causes an air lock in a diesel fuel system?\n3. What component powers rotary mowers at the rear of a tractor?",
                        "options": [
                            "A: Locks rear axles together to stop wheel spin in mud; Air entering fuel lines; Power Take-Off (PTO).",
                            "B: Increases speed; Water in radiator; Hydraulic lift.",
                            "C: Stops engine; Blown fuse; Alternator.",
                            "D: Changes gear ratio; Dirty oil filter; Clutch pedal."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Differential lock stops wheel spin; air entering lines causes air locks; PTO drives rear rotary equipment."
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
                    "title": "KCSE Model Essay: Daily Tractor Maintenance Checklist (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Outline five daily maintenance practices performed on a farm tractor before starting work. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Engine Oil:** Check dipstick level; top up if below MIN mark.\n"
                            "2. **Coolant Level:** Inspect radiator expansion tank; top up clean water.\n"
                            "3. **Air Cleaner:** Inspect and clean dust bowl of chaff and debris.\n"
                            "4. **Fuel Line Bowl:** Drain accumulated water from glass sediment bowl.\n"
                            "5. **Tyre Inflation & Fan Belt:** Check tyre pressures and verify fan belt deflection (12–19 mm)."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 4 DATA: Tractor-Drawn Implements (10 Pages)
# =============================================================================

LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Tractor-Drawn Implements",
    "lesson_title": "Tractor-Drawn Implements",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Classification of Implements",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 4 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Classify implements into primary, secondary, sowing, and harvesting tools.\n"
                            "- Compare mouldboard ploughs vs disc ploughs for different soil conditions.\n"
                            "- Detail secondary tillage tools: harrows, cultivators, rotavators.\n"
                            "- Execute disc plough leveling and angle adjustments.\n"
                            "- Select appropriate ploughs for stony, dry, or trashy fields."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Tillage Categories Overview",
                    "content": {
                        "text": (
                            "- **Primary Tillage Implements:** Break up virgin/compacted soil (Mouldboard plough, Disc plough, Subsoiler).\n"
                            "- **Secondary Tillage Implements:** Pulverize clods and level seedbed (Disc harrow, Spike-tooth harrow, Rotavator).\n"
                            "- **Sowing & Planting Implements:** Seed drills, precision planters.\n"
                            "- **Harvesting & Mowing Implements:** Combine harvesters, mowers, balers."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Primary Tillage: Mouldboard vs Disc Plough",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Comparison of Mouldboard vs Disc Ploughs",
                    "content": {
                        "text": (
                            "| Feature | Mouldboard Plough | Disc Plough |\n"
                            "|---|---|---|\n"
                            "| Cutting Component | Share & curved steel mouldboard | Concave rotating steel discs |\n"
                            "| Soil Inversion | Complete soil inversion & weed burial | Partial soil inversion & mixing |\n"
                            "| Stony / Obstacle Soil | Fails / share breaks on rocks | Disc rolls over rocks without breaking |\n"
                            "| Hard Dry Clay Soil | Cannot penetrate dry clay | Heavy disc weight chops hard clay |\n"
                            "| Heavy Surface Trash | Clogs standards & drags trash | Rotating disc slices through vines & trash |\n"
                            "| Field Suitability | Moist, stone-free arable land | Rough, dry, stony, or virgin land |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Secondary Tillage Mechanics & Implements",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Harrows, Cultivators & Rotavators",
                    "content": {
                        "text": (
                            "- **Disc Harrow:** Concave steel discs arranged in gangs (single-action, double-action, tandem) to break clods and pulverize soil.\n"
                            "- **Spike-Tooth Harrow:** Rigid steel spikes dragging through tilled soil to smooth seedbed and pull out roots.\n"
                            "- **Rotavator (Rotary Tiller):** PTO-driven rotating tines that pulverize soil into fine tilth in a single pass."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Sowing, Planting & Harvesting Implements",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Planters, Combine Harvesters & Balers",
                    "content": {
                        "text": (
                            "- **Seed Drill / Planter:** Opens furrow, meters seed at precise spacing, deposits seed, and covers furrow with press wheel.\n"
                            "- **Combine Harvester:** Cuts crop, threshes grain from straw, cleans grain, and deposits straw in windrows.\n"
                            "- **Hay Baler:** Picks up dry forage, compresses it into dense rectangular/round bales, and ties them with twine."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Technical Vector Diagram: Plough Comparison",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Structural Comparison: Mouldboard vs Disc Plough",
                    "content": {
                        "text": "Diagram showing cross-section profiles of mouldboard share and curved plate vs concave rotating disc and scraper.",
                        "svg": SVG_PLOUGH_COMPARISON
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Visual Guide: Tractor Disc Plough",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Three-Disc Tractor-Drawn Plough",
                    "content": {
                        "text": "Heavy 3-disc tractor plough mounted on a 3-point hydraulic linkage showing scrapers and disc standards.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Disc_plough_tractor.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Disc_plough_tractor.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Step-by-Step Procedure: Disc Plough Leveling",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Adjusting & Leveling a Disc Plough",
                    "content": {
                        "text": (
                            "**Purpose:** To achieve uniform ploughing depth and furrow width.\n\n"
                            "**Step 1: Front-to-Rear Leveling (Top Link Adjustment)**\n"
                            "Shorten or lengthen 3-point top link turnbuckle so front and rear discs cut to equal depth.\n\n"
                            "**Step 2: Side-to-Side Leveling (Lower Link Adjustment)**\n"
                            "Adjust right lift arm leveling crank so frame is parallel to tractor axle.\n\n"
                            "**Step 3: Disc Angle Adjustment**\n"
                            "Adjust disc angle (angle between disc plane and line of travel, usually 42°–45°) to regulate furrow width.\n\n"
                            "**Step 4: Tilt Angle Adjustment**\n"
                            "Adjust tilt angle (vertical inclination of disc, usually 15°–25°) to control soil penetration in hard land.\n\n"
                            "**Step 5: Scraper Positioning**\n"
                            "Set scraper close to concave disc surface to remove sticky clay soil during rotation."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application Scenario",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Laikipia Stony Field Selection Case Study",
                    "content": {
                        "text": (
                            "**Scenario:** A Laikipia farmer wants to clear a dry, stony field with heavy acacia brush.\n\n"
                            "**Decision:** Select a heavy disc plough instead of a mouldboard plough. "
                            "The rotating concave steel discs slice through brush roots and roll safely over subterranean rocks without breaking share points."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Implement Mechanics Recall",
                    "content": {
                        "text": "1. Why is a disc plough preferred over a mouldboard plough in stony soil?\n2. What angle controls penetration depth of a disc plough?\n3. What implement prepares a fine seedbed in a single pass?",
                        "options": [
                            "A: Discs roll over stones without breaking; Tilt angle (15°-25°); Rotavator.",
                            "B: Discs are cheaper; Disc angle; Mouldboard.",
                            "C: Discs turn faster; Hitch height; Subsoiler.",
                            "D: Discs do not rust; Draft angle; Spike harrow."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Discs roll over obstacles safely; tilt angle governs penetration depth; rotavator produces fine tilth in 1 pass."
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
                    "title": "KCSE Model Essay: Disc vs Mouldboard Suitability (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Give five reasons why a farmer would choose a disc plough over a mouldboard plough for primary tillage. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Stony / Rocky Soils:** Discs roll over buried obstacles without breaking shares.\n"
                            "2. **Hard Dry Soils:** Heavy disc mass penetrates hard clay where mouldboards fail.\n"
                            "3. **Heavy Surface Trash:** Rotating discs cut through thick vegetation without clogging.\n"
                            "4. **Sticky Clay Soils:** Scrapers keep discs clean in sticky conditions.\n"
                            "5. **Rough / Virgin Land:** Discs withstand uncultivated land conditions better than mouldboard frames."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 5 DATA: Animal-Drawn Implements (10 Pages)
# =============================================================================

LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Animal-Drawn Implements",
    "lesson_title": "Animal-Drawn Implements",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Intermediate Technology & Animal Power",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 5 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define intermediate technology and animal-drawn implements.\n"
                            "- Identify structural parts and functions of an ox-plough.\n"
                            "- Detail depth and width adjustment mechanisms on an ox-plough.\n"
                            "- Execute maintenance protocols for ox-ploughs and ox-drawn carts.\n"
                            "- Compare ox-ploughs vs tractor ploughs in KCSE essay questions."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Intermediate Technology Concept",
                    "content": {
                        "text": (
                            "Animal-drawn implements represent an essential intermediate technology between hand manual tools and heavy motorized machinery. "
                            "They are affordable, low-cost to maintain, and highly suited for smallholder farms and steep terraced fields where tractors cannot go."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Structural Anatomy of the Ox-Plough",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Components & Mechanical Roles",
                    "content": {
                        "text": (
                            "- **Main Beam:** Heavy steel chassis onto which all components are bolted.\n"
                            "- **Plough Share:** Sharp pointed front blade making initial horizontal soil cut.\n"
                            "- **Mouldboard:** Curved steel plate behind share that lifts, rolls, and flips soil furrow slice.\n"
                            "- **Land Wheel:** Front wheel rolling on unploughed land regulating cutting depth.\n"
                            "- **Draft Rod & Hake:** Steel attachment rod transmitting pulling force from yoke to plough."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Depth & Width Adjustment Mechanisms",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Regulating Furrow Dimensions",
                    "content": {
                        "text": (
                            "- **Depth Control:** Adjusted by sliding the land wheel up (deeper cut) or down (shallower cut), or by altering the draft chain attachment height on the draft rod notches.\n"
                            "- **Width Control:** Adjusted by shifting the hake connection left or right along the draft rod notches."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Ox-Drawn Carts & Cultivators",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Transport & Secondary Weeding",
                    "content": {
                        "text": (
                            "- **Ox-Drawn Cart:** Wooden or steel chassis on pneumatic tyres or wooden wheels. Hub bearings require weekly greasing; yoke must be inspected to prevent animal neck injury.\n"
                            "- **Ox-Drawn Cultivator:** Lightweight tine attachment used for weeding between wide crop rows (maize, cotton)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Technical Vector Diagram: Ox-Plough Anatomy",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Structural Anatomy of an Ox-Plough",
                    "content": {
                        "text": "Labelled diagram showing main beam, share, mouldboard, land wheel, draft rod, clevis, and operator handles.",
                        "svg": SVG_OX_PLOUGH
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Visual Guide: Ox-Plough Tillage",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Ox-Ploughing Team in Action",
                    "content": {
                        "text": "Pair of oxen harnessed via wooden yoke pulling a mouldboard ox-plough in a smallholder field.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Ox_ploughing_field.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY 3.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Ox_ploughing_field.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Step-by-Step Procedure: Ox-Plough Maintenance",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Ox-Plough Maintenance Protocol",
                    "content": {
                        "text": (
                            "**Purpose:** To extend ox-plough service life and prevent rust.\n\n"
                            "**Step 1: Wash After Daily Use**\n"
                            "Scrape off soil, mud, and grass roots from share and mouldboard using water.\n\n"
                            "**Step 2: Sharpen & Replace Share**\n"
                            "Sharpen share edge with a file if blunt; replace completely when severely worn.\n\n"
                            "**Step 3: Tighten Loose Bolts & Pins**\n"
                            "Inspect main beam bolts, land wheel lock, and draft rod pins; tighten securely.\n\n"
                            "**Step 4: Apply Greasing for Storage**\n"
                            "Coat polished share and mouldboard surface with spent engine oil or grease to prevent rust.\n\n"
                            "**Step 5: Paint Main Frame**\n"
                            "Periodically paint handles, main beam, and braces to stop atmospheric corrosion."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Ox-Plough vs Tractor-Plough Comparison Table",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Comparison of Ox-Drawn vs Tractor-Drawn Ploughs",
                    "content": {
                        "text": (
                            "| Feature | Ox-Drawn Plough | Tractor-Drawn Plough |\n"
                            "|---|---|---|\n"
                            "| Skill Required | Very low skill required | High skill & specialized mechanical training |\n"
                            "| Terrain Compatibility | Ideal for steep, narrow, terraced slopes | Strictly limited to flat or gentle slopes |\n"
                            "| Capital & Maintenance | Highly affordable, cheap purchase/repairs | Extremely high capital & repair costs |\n"
                            "| Speed & Work Output | Slow, tedious, physically demanding | Rapid, high-capacity, effortless |\n"
                            "| Overhead Needs | Requires grazing land & animal care | Requires dry fuel storage & spare parts |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Ox-Plough Mechanics Recall",
                    "content": {
                        "text": "1. How is ploughing depth adjusted on an ox-plough?\n2. What component transmits pulling force from the yoke to the plough?\n3. What maintenance prevents mouldboard rusting during storage?",
                        "options": [
                            "A: Moving land wheel up/down or altering draft rod hitch height; Draft rod; Coating face with grease/oil.",
                            "B: Changing handles; Yoke; Washing with soap.",
                            "C: Turning landside; Chain; Painting red.",
                            "D: Removing share; Harness; Freezing."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Land wheel and draft rod adjust depth; draft rod transmits pull; oil/grease coating prevents mouldboard rust."
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
                    "title": "KCSE Model Question: Ox-Plough Structural Components (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Identify five main structural components of an ox-plough, and state the specific function of each. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Main Beam:** Central chassis onto which all other components are bolted.\n"
                            "2. **Plough Share:** Sharp front blade making the initial horizontal soil cut.\n"
                            "3. **Mouldboard:** Curved steel plate that lifts, rolls, and inverts furrow slice to bury weeds.\n"
                            "4. **Land Wheel:** Front wheel rolling on unploughed soil to regulate ploughing depth.\n"
                            "5. **Draft Rod:** Attachment rod for draft chain transmitting pull from yoke to plough."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# ALL LESSONS LIST EXPORT
# =============================================================================

ALL_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA
]
