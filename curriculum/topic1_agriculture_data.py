"""
VLearn Form 4 Agriculture — Topic 1 Data File
Topic 1: Livestock Production V (Poultry)

Contains structured data for all 7 Learning Modules / Lessons:
  Lesson 1: Poultry Eggs — Structure, Quality, and Candling (10 Pages)
  Lesson 2: Incubation — Natural and Artificial Methods (10 Pages)
  Lesson 3: Brooding and Rearing of Chicks (10 Pages)
  Lesson 4: Growers, Layers, and Broilers (10 Pages)
  Lesson 5: Poultry Rearing Systems (10 Pages)
  Lesson 6: Stress, Vices, and Diagnosis in Poultry (9 Pages)
  Lesson 7: Marketing Poultry Products (9 Pages)
Total: 68 Pages, ~220 Granular Lesson Blocks
"""

# =============================================================================
# SVG DIAGRAM DEFINITIONS
# =============================================================================

SVG_EGG_ANATOMY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" style="background-color: #0f172a; border-radius: 8px;">
  <defs>
    <radialGradient id="yolkGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </radialGradient>
    <linearGradient id="albumenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(241, 245, 249, 0.25)"/>
      <stop offset="100%" stop-color="rgba(203, 213, 225, 0.15)"/>
    </linearGradient>
  </defs>
  <title>Internal Anatomy of a Poultry Egg (Sagittal Cross-Section)</title>
  
  <!-- Outer Shell -->
  <path d="M 120 250 C 120 100, 320 60, 520 60 C 680 60, 720 160, 720 250 C 720 340, 680 440, 520 440 C 320 440, 120 400, 120 250 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="4"/>
  
  <!-- Shell Membranes -->
  <path d="M 125 250 C 125 105, 322 65, 518 65 C 675 65, 715 163, 715 250 C 715 337, 675 435, 518 435 C 322 435, 125 395, 125 250 Z" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
  
  <!-- Air Sac at Broad End (Left) -->
  <path d="M 120 200 C 155 215, 155 285, 120 300 C 120 250, 120 250, 120 200 Z" fill="#38bdf8" opacity="0.3"/>
  <line x1="120" y1="200" x2="120" y2="300" stroke="#38bdf8" stroke-width="3"/>

  <!-- Albumen (Egg White) -->
  <path d="M 160 250 C 160 120, 330 85, 510 85 C 650 85, 690 170, 690 250 C 690 330, 650 415, 510 415 C 330 415, 160 380, 160 250 Z" fill="url(#albumenGrad)" stroke="#cbd5e1" stroke-width="1.5"/>

  <!-- Yolk -->
  <circle cx="460" cy="250" r="95" fill="url(#yolkGrad)" stroke="#b45309" stroke-width="3"/>
  
  <!-- Vitelline Membrane -->
  <circle cx="460" cy="250" r="96" fill="none" stroke="#f59e0b" stroke-width="2"/>

  <!-- Germinal Disc -->
  <circle cx="460" cy="155" r="10" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>

  <!-- Chalazae (Twisted Protein Cords) -->
  <path d="M 160 250 Q 230 230, 300 250 T 365 250" fill="none" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>
  <path d="M 555 250 Q 610 270, 650 250 T 690 250" fill="none" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>

  <!-- Labels and Leader Lines -->
  <g font-family="Arial, sans-serif" font-size="13" fill="#f8fafc">
    <line x1="135" y1="250" x2="70" y2="150" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="10" y="145" fill="#38bdf8" font-weight="bold">Air Sac (Broad End)</text>

    <line x1="300" y1="62" x2="300" y2="25" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="250" y="20" font-weight="bold">Calcium Carbonate Shell</text>

    <line x1="400" y1="64" x2="430" y2="30" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="435" y="25" fill="#7dd3fc">Inner &amp; Outer Shell Membranes</text>

    <line x1="460" y1="155" x2="520" y2="110" stroke="#fef08a" stroke-width="1.5"/>
    <text x="525" y="105" fill="#fef08a" font-weight="bold">Germinal Disc (Blastoderm)</text>

    <line x1="460" y1="280" x2="460" y2="370" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="415" y="385" fill="#fbbf24" font-weight="bold">Yolk (Nutrient Pantry)</text>

    <line x1="550" y1="280" x2="590" y2="340" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="595" y="345" fill="#f59e0b">Vitelline Membrane</text>

    <line x1="250" y1="245" x2="220" y2="320" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="140" y="335" font-weight="bold">Chalaza (Twisted Cord)</text>

    <line x1="620" y1="200" x2="710" y2="120" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="660" y="110" font-weight="bold">Albumen (Egg White)</text>
  </g>
</svg>"""

SVG_INCUBATOR_SCHEMATIC = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" style="background-color: #0f172a; border-radius: 8px;">
  <title>Functional Mechanics of an Artificial Incubator Cabinet</title>
  
  <rect x="100" y="40" width="600" height="420" rx="12" fill="#1e293b" stroke="#475569" stroke-width="4"/>
  <rect x="115" y="55" width="570" height="390" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2"/>

  <rect x="130" y="70" width="60" height="20" fill="#38bdf8" rx="4"/>
  <text x="135" y="85" font-family="Arial" font-size="10" fill="#0f172a" font-weight="bold">AIR IN</text>

  <rect x="610" y="70" width="60" height="20" fill="#ef4444" rx="4"/>
  <text x="615" y="85" font-family="Arial" font-size="10" fill="#ffffff" font-weight="bold">CO2 OUT</text>

  <circle cx="400" cy="110" r="30" fill="#334155" stroke="#f97316" stroke-width="3"/>
  <path d="M 400 90 L 400 130 M 380 110 L 420 110" stroke="#f97316" stroke-width="4"/>
  <text x="445" y="115" font-family="Arial" font-size="12" fill="#f97316" font-weight="bold">Heater &amp; Fan (37.5°C - 39.4°C)</text>

  <g stroke="#94a3b8" stroke-width="2" fill="#1e293b">
    <rect x="200" y="170" width="400" height="30" rx="4"/>
    <ellipse cx="250" cy="185" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="320" cy="185" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="390" cy="185" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="460" cy="185" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="530" cy="185" rx="10" ry="12" fill="#f8fafc"/>

    <rect x="200" y="230" width="400" height="30" rx="4"/>
    <ellipse cx="250" cy="245" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="320" cy="245" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="390" cy="245" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="460" cy="245" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="530" cy="245" rx="10" ry="12" fill="#f8fafc"/>

    <rect x="200" y="290" width="400" height="30" rx="4"/>
    <ellipse cx="250" cy="305" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="320" cy="305" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="390" cy="305" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="460" cy="305" rx="10" ry="12" fill="#f8fafc"/>
    <ellipse cx="530" cy="305" rx="10" ry="12" fill="#f8fafc"/>
  </g>

  <path d="M 610 230 Q 640 230, 640 260 T 610 290" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="620" y="220" font-family="Arial" font-size="11" fill="#38bdf8">180° Turning Arm</text>

  <rect x="250" y="370" width="300" height="40" fill="#0284c7" rx="6" stroke="#38bdf8" stroke-width="2"/>
  <text x="315" y="395" font-family="Arial" font-size="13" fill="#ffffff" font-weight="bold">Water Tray (60% Relative Humidity)</text>
</svg>"""

SVG_BROODER_DIAGNOSTIC = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Chick Distribution Diagnostic Patterns Inside a Brooder Guard</title>

  <g transform="translate(50, 40)">
    <circle cx="120" cy="120" r="100" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="120" cy="120" r="20" fill="#ef4444"/>
    <circle cx="120" cy="120" r="45" fill="#fde047" opacity="0.8"/>
    <text x="50" y="240" font-family="Arial" font-size="13" fill="#ef4444" font-weight="bold">TOO COLD: Huddled Under Heat</text>
  </g>

  <g transform="translate(430, 40)">
    <circle cx="120" cy="120" r="100" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="120" cy="120" r="20" fill="#ef4444"/>
    <circle cx="120" cy="120" r="90" fill="none" stroke="#fde047" stroke-width="16" stroke-dasharray="8,6"/>
    <text x="45" y="240" font-family="Arial" font-size="13" fill="#f97316" font-weight="bold">TOO HOT: Pushed to Outer Edges</text>
  </g>

  <g transform="translate(50, 260)">
    <circle cx="120" cy="120" r="100" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="120" cy="120" r="20" fill="#ef4444"/>
    <path d="M 60 70 A 70 70 0 0 1 60 170 Z" fill="#fde047"/>
    <path d="M 230 120 L 170 120" stroke="#38bdf8" stroke-width="4"/>
    <text x="35" y="240" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold">DRAUGHT: Huddled Away from Wind</text>
  </g>

  <g transform="translate(430, 260)">
    <circle cx="120" cy="120" r="100" fill="#1e293b" stroke="#22c55e" stroke-width="3"/>
    <circle cx="120" cy="120" r="20" fill="#ef4444"/>
    <circle cx="70" cy="90" r="7" fill="#fde047"/>
    <circle cx="170" cy="90" r="7" fill="#fde047"/>
    <circle cx="70" cy="160" r="7" fill="#fde047"/>
    <circle cx="170" cy="160" r="7" fill="#fde047"/>
    <circle cx="120" cy="65" r="7" fill="#fde047"/>
    <circle cx="120" cy="180" r="7" fill="#fde047"/>
    <circle cx="90" cy="120" r="7" fill="#fde047"/>
    <circle cx="150" cy="120" r="7" fill="#fde047"/>
    <text x="30" y="240" font-family="Arial" font-size="13" fill="#22c55e" font-weight="bold">IDEAL (35°C): Evenly Distributed</text>
  </g>
</svg>"""

SVG_FOLD_UNIT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Structural Specifications of a Portable Fold Unit (3.5m x 1.5m x 1.5m)</title>
  
  <polygon points="100,320 250,150 700,150 550,320" fill="none" stroke="#b45309" stroke-width="4"/>
  <line x1="100" y1="320" x2="550" y2="320" stroke="#b45309" stroke-width="4"/>
  
  <polygon points="100,320 250,150 400,150 250,320" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="175" y="240" font-family="Arial" font-size="13" fill="#f8fafc" font-weight="bold">Roofed Shelter (1/3)</text>
  
  <polygon points="250,320 400,150 700,150 550,320" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="440" y="240" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold">Open Wire-Mesh Run (2/3)</text>

  <rect x="60" y="310" width="40" height="15" rx="3" fill="#b45309"/>
  <rect x="550" y="310" width="40" height="15" rx="3" fill="#b45309"/>

  <g font-family="Arial" font-size="12" fill="#f8fafc">
    <line x1="100" y1="360" x2="550" y2="360" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="290" y="380" font-weight="bold">Total Length = 3.5 meters</text>

    <line x1="70" y1="320" x2="70" y2="150" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="15" y="240" font-weight="bold">Height = 1.5m</text>
  </g>
</svg>"""

SVG_BATTERY_CAGE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Cross-Section of a Battery Cage Unit</title>

  <rect x="200" y="80" width="400" height="260" fill="none" stroke="#94a3b8" stroke-width="4"/>

  <line x1="200" y1="280" x2="630" y2="330" stroke="#38bdf8" stroke-width="4"/>
  <text x="350" y="270" font-family="Arial" font-size="12" fill="#38bdf8">Slanting Wire Mesh Floor</text>

  <path d="M 630 330 Q 660 330, 650 300" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="635" cy="315" r="12" fill="#f8fafc" stroke="#b45309" stroke-width="2"/>
  <text x="640" y="285" font-family="Arial" font-size="11" fill="#f8fafc" font-weight="bold">Egg Roll-Out Tray</text>

  <rect x="590" y="160" width="70" height="40" fill="#b45309" rx="4"/>
  <text x="600" y="185" font-family="Arial" font-size="11" fill="#ffffff" font-weight="bold">Feed Trough</text>

  <rect x="590" y="110" width="50" height="25" fill="#0284c7" rx="4"/>
  <text x="595" y="127" font-family="Arial" font-size="10" fill="#ffffff" font-weight="bold">Water Trough</text>

  <line x1="200" y1="340" x2="600" y2="340" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="250" y="370" font-family="Arial" font-size="12" fill="#ef4444">Manure Droppings Fall Through Mesh Below</text>
</svg>"""


# =============================================================================
# LESSON DATA DICTIONARIES
# =============================================================================

LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Poultry Eggs — Structure, Quality, and Candling",
    "lesson_title": "Poultry Eggs — Structure, Quality, and Candling",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Poultry Production & Egg Selection",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify and state the functions of the internal and external parts of a poultry egg.\n"
                            "- Describe the purpose and step-by-step procedure of egg candling.\n"
                            "- Identify selection criteria for eggs intended for incubation.\n"
                            "- Calculate the exact weight proportions of egg components and interpret nutritional defects.\n"
                            "- Apply KCSE examination techniques to score maximum marks on egg selection questions."
                        )
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "External Egg Quality Comparison for Incubation",
                    "content": {
                        "text": "Side-by-side comparison showing a clean, smooth incubation-grade egg versus defective cracked and dirty eggs.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Egg_comparison_quality.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Egg_comparison_quality.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Agricultural Significance of Egg Structure",
                    "content": {
                        "text": (
                            "Poultry production is a major agricultural enterprise in Kenya, serving as a rapid source of income and high-quality protein (meat and eggs) "
                            "for both rural and urban communities. Before a poultry farmer can begin incubation or market eggs, they must understand the biological "
                            "structure of the egg. This understanding enables the identification of fertile, healthy eggs suitable for hatching, as well as high-quality "
                            "eggs that meet market demands, thereby reducing financial losses from low hatchability or rejected market consignments."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Biological Anatomy of the Poultry Egg",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Layered Explanation of Egg Structure & Quality",
                    "content": {
                        "text": (
                            "**Layer 1 (Simple Intuition):** Think of an egg as a self-contained biological space suit. The hard outer shell protects the delicate contents inside, "
                            "while the egg white (albumen) and yellow yolk act as a rich food and water pantry that feeds the chick as it grows. An air pocket at the broad end acts as "
                            "a tiny oxygen tank for the chick's first breath before it hatches.\n\n"
                            "**Layer 2 (Technical Terms):** The outer shell is a semi-permeable barrier made of calcium and phosphorus, constituting 10–12% of the total egg weight. "
                            "Lining the shell are the inner and outer shell membranes (1% of the egg). The egg white or albumen (55–60%) is divided into thick and thin layers, containing "
                            "twisted protein bands called chalaza which anchor the yolk (30–33%) in the center. The yolk is enveloped by the vitelline membrane. The active genetic site "
                            "is the germinal disc. At the broad end, the air sac allows gaseous exchange.\n\n"
                            "**Layer 3 (Biological Mechanism):** If the egg is fertilized, the germinal disc becomes the active site of embryonic cell division. The vitelline membrane "
                            "maintains the spherical shape of the yolk, preventing it from mixing with the albumen. The chalaza acts like suspension springs; as the egg is turned, "
                            "they keep the yolk suspended in the center to prevent the embryo from sticking to the shell membranes, which would cause physical deformities or death. "
                            "The air sac is formed as the egg cools after laying, causing the inner and outer membranes to separate at the broad end. Its size increases over time as "
                            "moisture evaporates through the shell pores, making it an excellent indicator of egg freshness.\n\n"
                            "**Layer 4 (Agricultural Application):** On a poultry farm in Nakuru, a farmer selects eggs for hatching. By understanding that the shell is porous, the farmer "
                            "ensures eggs are never washed with water (which forces bacteria into the pores) but are dry-cleaned gently if slightly dirty. Eggs are stored with the broad end "
                            "facing upwards so that the air sac remains at the top, preventing the yolk from rising and pressing the germinal disc against the shell membranes."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Technical Terms Reference",
                    "content": {
                        "text": (
                            "- **Albumen:** The egg white, making up 55–60% of the egg, which serves as the primary food and water source for the developing embryo.\n"
                            "- **Chalaza:** Twisted, spring-like protein cords within the albumen that hold the egg yolk in a central position.\n"
                            "- **Germinal Disc:** The tiny blastoderm or embryo on the yolk surface which develops into a chick if the egg is fertilized.\n"
                            "- **Vitelline Membrane:** The thin, delicate membrane that surrounds and contains the yolk, keeping it round.\n"
                            "- **Candling:** The practice of determining the internal qualities of an egg by examining it against a light source in a darkened space."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Internal Anatomy Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Internal Anatomy of a Poultry Egg (Sagittal Cross-Section)",
                    "content": {
                        "text": "Detailed structural map of a poultry egg showing shell, membranes, albumen, chalaza, yolk, vitelline membrane, germinal disc, and air sac.",
                        "svg": SVG_EGG_ANATOMY
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Quantitative Analysis of Egg Components",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Worked Example: Analyzing Egg Component Weights",
                    "content": {
                        "text": (
                            "**Scenario:** A poultry research station in Kenya weighs a freshly laid Rhode Island Red egg and finds its total mass is exactly 60.0 g.\n\n"
                            "**Given:** Total Egg Weight = 60.0 g\n"
                            "Source Percentages: Shell = 10%–12%, Membrane = 1%, Albumen = 55%–60%, Yolk = 30%–33%.\n\n"
                            "**Required:** Calculate the expected weight of each component and interpret what a deviation means for a breeding farmer.\n\n"
                            "**Formula:** Component Weight = Total Egg Weight × (Percentage / 100)\n\n"
                            "**Calculations:**\n"
                            "1. Shell Weight (11% avg) = 60.0 g × (11 / 100) = 6.6 g (Range: 6.0 g to 7.2 g)\n"
                            "2. Membrane Weight (1%) = 60.0 g × (1 / 100) = 0.6 g\n"
                            "3. Albumen Weight (57.5% avg) = 60.0 g × (57.5 / 100) = 34.5 g (Range: 33.0 g to 36.0 g)\n"
                            "4. Yolk Weight (31.5% avg) = 60.0 g × (31.5 / 100) = 18.9 g (Range: 18.0 g to 19.8 g)\n\n"
                            "**Agricultural Interpretation:** If a flock consistently yields eggs with a shell percentage of only 8% (below the 10–12% range), "
                            "the shells will be thin, brittle, and prone to cracking. This indicates a calcium or phosphorus deficiency in the layer feed, "
                            "requiring immediate supplementation with soluble oyster shell grit."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Practical Procedure: Egg Candling",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Internal Egg Candling",
                    "content": {
                        "text": (
                            "**Purpose:** To inspect internal egg quality, freshness, fertility, and structural defects prior to incubation or marketing.\n\n"
                            "**Step 1: Preparation of Environment**\n"
                            "Place a cool light source inside a sturdy box with a 3 cm circular hole. Darken the inspection room completely so light rays pass directly through the egg shell.\n\n"
                            "**Step 2: Required Tools & Materials**\n"
                            "Candling box, cool high-efficiency bulb, test eggs, clean hands.\n\n"
                            "**Step 3: Execution Procedure**\n"
                            "Hold the egg by its ends, place it over the aperture with the broad end tilted slightly upward, and gently rotate the egg 180° along its long axis.\n\n"
                            "**Step 4: Observation**\n"
                            "Observe the air sac size, check yolk stability held by chalazae, look for dark embryonic spots with branching blood vessels (fertile) or clear yellow yolk (infertile), and check for hairline cracks or blood/meat spots.\n\n"
                            "**Step 5: Explanation**\n"
                            "Light rays make the shell translucent. Rotation spins the yolk, revealing hidden internal defects.\n\n"
                            "**Step 6: Expected Result**\n"
                            "Optimal incubation eggs show clean internal structures, a small stable air sac, and distinct embryonic vessels if fertile.\n\n"
                            "**Step 7: Precautions**\n"
                            "Do not leave the egg over a hot bulb for more than a few seconds to avoid thermal death of the embryo. Handle with clean, dry hands.\n\n"
                            "**Step 8: Application**\n"
                            "Set only clean, fertile, crack-free eggs for hatching; send remaining clean non-fertile eggs to market."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Video Demonstration: Practical Candling",
            "blocks": [
                {
                    "block_type": "suggested_video",
                    "component_type": "suggested_video",
                    "title": "Practical Egg Candling & Internal Diagnostic Demonstration",
                    "content": {
                        "text": "Demonstration of egg candling showing fresh vs stale air sac size and fertile vs infertile embryonic development.",
                        "url": "https://www.youtube.com/embed/candling_demo_vlearn_01",
                        "youtube_id": "candling_demo_vlearn_01"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Learning: Diagnostic Exercises",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Egg Selection Choice Exercise",
                    "content": {
                        "text": "A farmer collects eggs for incubation. One egg weighs 58 g, is oval, but has a small dry mud smear. Another weighs 72 g with a slight shell ridge. Which egg should be selected?",
                        "options": [
                            "A: The 72 g ridged egg because it is larger and clean.",
                            "B: The 58 g egg after gently dry-cleaning the mud smear.",
                            "C: Neither egg is suitable for incubation.",
                            "D: Both eggs are equally suitable."
                        ],
                        "correct_answer_index": 1,
                        "explanation": "The ideal incubation weight is 55–60 g. Dry-cleaning safely opens pores. Oversized (72g) or ridged eggs indicate double yolks or structural abnormalities that give poor hatchability."
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
                    "title": "Kiambu County Hatching Failure Case Study",
                    "content": {
                        "text": (
                            "**Context:** Mr. Kamau bought 50 expensive hatching eggs but only 15 hatched under his broody hen after 21 days.\n\n"
                            "**Observation & Candling Findings:**\n"
                            "- 10 eggs had oversized air sacs filling half the egg.\n"
                            "- 12 eggs had micro-cracks leaking dried yolk.\n"
                            "- 8 eggs were completely clear (infertile).\n"
                            "- 5 eggs contained dead fully-formed embryos stuck to the shell membrane.\n\n"
                            "**Diagnostic Analysis:**\n"
                            "1. *Oversized Air Sacs:* Eggs were stored for 12 days near a warm kitchen stove, causing severe desiccation. Hatching eggs must be under 5 days old.\n"
                            "2. *Micro-cracks:* Lack of pre-candling allowed cracked eggs to break under the hen's weight, causing bacterial infection.\n"
                            "3. *Clear Eggs:* Infertile eggs should have been candled and removed on Day 7.\n"
                            "4. *Stuck Embryos:* Parasitized, restless hen stood up frequently, failing to provide uniform turning and heat."
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
                    "title": "Core Recall Questions",
                    "content": {
                        "text": "1. State the average weight proportion (%) of albumen and yolk in a fresh egg.\n2. Name the mineral elements forming the egg shell.\n3. Explain the function of the air sac.",
                        "options": [
                            "A: Albumen 55-60%, Yolk 30-33%; Calcium & Phosphorus; Gaseous exchange/oxygen source.",
                            "B: Albumen 30-33%, Yolk 55-60%; Iron & Zinc; Keeps yolk centered.",
                            "C: Albumen 80%, Yolk 10%; Sodium & Potassium; Protects from shock.",
                            "D: Albumen 40%, Yolk 40%; Magnesium & Sulfur; Stores waste products."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Albumen makes up 55-60%, yolk 30-33%. Shell is made of Calcium and Phosphorus. The air sac provides oxygen for respiration during hatching."
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
                    "title": "KCSE Model Essay: Selection of Eggs for Incubation (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Describe the selection criteria for poultry eggs intended for incubation. (8 Marks)\n\n"
                            "**Model Answer (1 Mark per valid point with justification):**\n"
                            "1. **Fertility:** Must be fertile, laid by hens mated with a cock.\n"
                            "2. **Ideal Weight:** Medium size between 55 and 60 grams.\n"
                            "3. **Normal Shape:** Oval-shaped with distinct broad and narrow ends.\n"
                            "4. **Shell Condition:** Smooth, free from ridges, deposits, or roughness.\n"
                            "5. **No Cracks:** Shell must be intact to prevent evaporation and bacterial entry.\n"
                            "6. **Cleanliness:** Clean shells keep gas-exchange pores open.\n"
                            "7. **Freshness:** Freshly laid, stored for no more than 5 days.\n"
                            "8. **Absence of Internal Defects:** Verified by candling to be free of blood/meat spots or double yolks."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Incubation — Natural and Artificial Methods",
    "lesson_title": "Incubation — Natural and Artificial Methods",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Incubation Methods",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Distinguish between natural and artificial incubation.\n"
                            "- Detail the four critical environmental parameters required for artificial incubation.\n"
                            "- Compare structural advantages and disadvantages of natural vs artificial incubation.\n"
                            "- Execute the 8-step protocol for natural incubation management.\n"
                            "- Score full marks on KCSE incubator failure essay questions."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Biological Concept of Incubation",
                    "content": {
                        "text": (
                            "Incubation provides fertile eggs with the precise environmental conditions required for embryonic development over 20–21 days in chicken. "
                            "This can be achieved biologically using a broody hen (natural incubation) or mechanically using a heated incubator (artificial incubation)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Physical Parameters of Incubation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Four Critical Environmental Parameters",
                    "content": {
                        "text": (
                            "1. **Temperature:** Maintained strictly between 37.5°C and 39.4°C. Heat above 39.4°C is lethal; below 37.5°C delays development.\n"
                            "2. **Relative Humidity:** Maintained at 60%. Excess humidity causes 'marshy' chicks that drown during hatching; low humidity causes chicks to dry and stick to shell membranes.\n"
                            "3. **Ventilation:** Good air circulation maintaining a CO2 to O2 ratio of 0.03% : 21% to prevent embryonic asphyxiation.\n"
                            "4. **Egg Turning:** Turned 3–4 times daily through 180° clockwise to prevent the embryo from sticking to shell membranes."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Natural vs Artificial Incubation Comparison",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Structural Comparison Table: Incubation Systems",
                    "content": {
                        "text": (
                            "| Parameter | Natural Incubation | Artificial Incubation |\n"
                            "|---|---|---|\n"
                            "| Primary Agent | Broody hen | Mechanical incubator |\n"
                            "| Capacity | 10–15 eggs per hen | 50 to thousands of eggs |\n"
                            "| Temperature | Hen's body heat | Heaters & thermostat (37.5–39.4°C) |\n"
                            "| Humidity | Hen-regulated soil contact | Water trays (60% RH) |\n"
                            "| Turning | Hen's beak (3-4x daily) | Automatic/manual 180° turning |\n"
                            "| Key Advantage | Cheap, low technical skill | Mass production, hens keep laying |\n"
                            "| Key Disadvantage | Low egg output, disease risk | High capital cost, electricity reliance |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Visualizing the Artificial Incubator",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Commercial Electric Cabinet Incubator",
                    "content": {
                        "text": "Electric cabinet incubator showing trays of hatching eggs, digital temperature monitors, and humidity controls.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Cabinet_incubator.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Cabinet_incubator.jpg"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Functional Mechanics of an Artificial Incubator Cabinet",
                    "content": {
                        "text": "Diagram showing airflow, heating elements, fan, water tray, stacked tilting egg trays, and exhaust vents.",
                        "svg": SVG_INCUBATOR_SCHEMATIC
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Practical Procedure: Natural Incubation",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Managing Natural Incubation",
                    "content": {
                        "text": (
                            "**Purpose:** To safely set and manage 10–15 hatching eggs under a broody hen.\n\n"
                            "**Step 1: Confirm Broodiness**\n"
                            "Place 2–3 dummy 'China eggs' under the hen for 1–2 days in an isolation coop to confirm her sitting behavior.\n\n"
                            "**Step 2: Nest Construction**\n"
                            "Scoop a saucer-shaped nest in dry ground or a wooden box and line it with clean, soft dry grass or shavings.\n\n"
                            "**Step 3: Parasite Dusting**\n"
                            "Thoroughly dust the hen's feathers and nest bedding with pyrethroid pesticide dust to eliminate lice and mites.\n\n"
                            "**Step 4: Setting Fertile Eggs**\n"
                            "Replace dummy eggs with 10–15 selected fertile eggs at night to reduce hen panic and shell breakage.\n\n"
                            "**Step 5: Daily Exercise Routine**\n"
                            "Allow the hen exactly 1 hour outside daily for feeding, watering, and dust-bathing.\n\n"
                            "**Step 6: Nest Inspection**\n"
                            "Inspect daily for broken eggs; clean soiled shells immediately to prevent pore clogging.\n\n"
                            "**Step 7: Precautions**\n"
                            "Keep nesting area dark and quiet; avoid loud noises.\n\n"
                            "**Step 8: Expected Result**\n"
                            "High hatchability of healthy chicks after 20–21 days."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Learning: Sequence Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Natural Incubation Sequence Order",
                    "content": {
                        "text": "What is the correct sequence for preparing natural incubation?\n1. Dust hen with pesticide\n2. Confirm broodiness with China eggs\n3. Set fertile eggs at night\n4. Scoop saucer-shaped nest\n5. Allow 1 hr daily feeding",
                        "options": [
                            "A: 2 -> 4 -> 1 -> 3 -> 5",
                            "B: 4 -> 1 -> 2 -> 3 -> 5",
                            "C: 1 -> 2 -> 3 -> 4 -> 5",
                            "D: 3 -> 4 -> 2 -> 1 -> 5"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Correct order: Confirm broodiness (2), construct saucer nest (4), dust for parasites (1), set fertile eggs at night (3), and manage daily 1-hr feeding (5)."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Deviation Consequences & Diagnostics",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Biological Consequences of Parameter Deviations",
                    "content": {
                        "text": (
                            "- **Excess Temperature (>39.4°C):** Lethal cell death or deformed early hatching.\n"
                            "- **Low Temperature (<37.5°C):** Delayed hatch rate or embryonic death.\n"
                            "- **High Humidity (>60%):** Restricted moisture loss leading to 'marshy' drowned chicks.\n"
                            "- **Low Humidity (<60%):** Desiccation causing chicks to stick to shell membranes.\n"
                            "- **Inadequate Ventilation:** CO2 buildup causing embryonic asphyxiation.\n"
                            "- **Failure to Turn:** Embryo adheres to inner shell membrane, causing vascular rupture and death."
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
                    "title": "Eldoret Hatchery Operational Troubleshooting",
                    "content": {
                        "text": (
                            "**Scenario:** An Eldoret commercial hatchery reports a drop in hatchability from 90% to 55%. "
                            "Inspection reveals: 25% of chicks drowned in unabsorbed egg fluids ('marshy chicks'), and 20% died stuck to shell membranes.\n\n"
                            "**Diagnosis:**\n"
                            "1. *Marshy Chicks:* Humidity in Setter Room 1 was running at 80% (far above 60%).\n"
                            "2. *Stuck Dead Embryos:* The automatic turning arm motor had failed, leaving trays untilted for 4 days.\n\n"
                            "**Corrective Action:** Recalibrate humidifiers to 60% and repair turning arm mechanism."
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
                    "title": "Incubation Core Concepts",
                    "content": {
                        "text": "1. What is the incubation period for chicken?\n2. What is the target relative humidity in an incubator?\n3. What chemical is used to sanitize incubators before setting?",
                        "options": [
                            "A: 20-21 days; 60%; Formaldehyde.",
                            "B: 14 days; 40%; Chlorine.",
                            "C: 28 days; 80%; Alcohol.",
                            "D: 30 days; 50%; Iodine."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Incubation takes 21 days in chicken; relative humidity is 60%; Formaldehyde gas is used for sanitation."
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
                    "title": "KCSE Model Essay: Environmental Conditions for Artificial Hatching (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Outline the environmental conditions necessary for the successful artificial hatching of poultry eggs, and explain the biological consequence of a deviation in each condition. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Temperature (37.5°C–39.4°C):** High temp causes early death or heat stroke; low temp delays hatch or kills embryos.\n"
                            "2. **Relative Humidity (60%):** High RH leads to marshy drowned chicks; low RH causes chicks to stick to shell membranes.\n"
                            "3. **Ventilation (CO2:O2 ratio 0.03%:21%):** Poor air flow causes oxygen starvation and asphyxiation.\n"
                            "4. **Egg Turning (3–4 times daily through 180°):** Prevents embryo from sticking to inner shell membranes.\n"
                            "5. **Cleanliness/Hygiene:** Pre-sanitation with Formaldehyde prevents bacterial entry through shell pores."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Brooding and Rearing of Chicks",
    "lesson_title": "Brooding and Rearing of Chicks",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Brooding Principles & Physiological Dynamics",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define brooding and state brooding durations for layers (8 wks) vs broilers (2 wks).\n"
                            "- Explain why day-old chicks are poikilothermic and require artificial heat.\n"
                            "- Calculate floor space, heater numbers, and feed budgets for chick rearing.\n"
                            "- Execute brooder setup protocols and diagnose chick spatial distribution behaviors.\n"
                            "- Detail vaccination schedules and debeaking timelines."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Poikilothermic Nature of Day-Old Chicks",
                    "content": {
                        "text": (
                            "Brooding is the rearing of day-old chicks up to 8 weeks for layers and 2 weeks for broilers. "
                            "Newly hatched chicks are poikilothermic (unable to regulate internal body temperature) and require artificial warmth starting at 35°C in week 1, "
                            "decreasing gradually by 2°C per week down to 21°C by week 8."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Brooder Setup & Structural Components",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Essential Brooder Components",
                    "content": {
                        "text": (
                            "- **Chick Guard:** Circular hardboard barrier 25 cm high. Circular shape eliminates 90° corners, preventing chicks from piling and suffocating.\n"
                            "- **Litter:** 5–10 cm layer of dry wood shavings (not sawdust) to insulate floor and absorb droppings.\n"
                            "- **Newspaper Cover:** Placed over litter for first 3–4 days to prevent chicks from eating wood shavings.\n"
                            "- **Heat Sources:** Infrared bulbs (1 per 100 chicks), hurricane lamps (1 per 100 chicks), or charcoal jikos.\n"
                            "- **Glucose Water:** Supplied immediately upon arrival to provide rapid cellular energy to stressed chicks."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Quantitative Brooder Calculations",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Worked Example: Brooder Requirements for 500 Layer Chicks",
                    "content": {
                        "text": (
                            "**Scenario:** A farmer in Nakuru wants to raise 500 layer chicks from day-old to 8 weeks.\n\n"
                            "**1. Floor Space Calculation:**\n"
                            "Parameter: 1 m² per 25 chicks.\n"
                            "Space Required = 500 chicks / 25 chicks/m² = 20 m².\n\n"
                            "**2. Heater Capacity Calculation:**\n"
                            "Parameter: 1 infrared bulb (240W) or hurricane lamp per 100 chicks.\n"
                            "Heaters Required = 500 / 100 = 5 infrared bulbs or 5 hurricane lamps.\n\n"
                            "**3. Feed Budget Calculation:**\n"
                            "Parameter: 1.5 kg to 2.2 kg chick mash per chick by week 8.\n"
                            "Min Feed = 500 × 1.5 kg = 750 kg (15 bags of 50 kg).\n"
                            "Max Feed = 500 × 2.2 kg = 1,100 kg (22 bags of 50 kg)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Step-by-Step Procedure: Brooder Setup",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Brooder Preparation & Management",
                    "content": {
                        "text": (
                            "**Part A: Pre-Arrival Preparation (2–3 Days Before)**\n"
                            "1. Clean & disinfect brooder house floor and walls.\n"
                            "2. Lay 5–10 cm dry wood shavings; cover with newspaper.\n"
                            "3. Set circular chick guard (25 cm high) and position feeders/waterers.\n"
                            "4. Pre-heat brooder exactly 6 hours before arrival to achieve 35°C.\n\n"
                            "**Part B: Management Upon Arrival**\n"
                            "5. Introduce chicks during daytime; provide glucose solution immediately.\n"
                            "6. Feed chick mash ad libitum; perform debeaking at 10 days.\n"
                            "7. Administer vaccines: Gumboro (wk 2), Newcastle (wks 3-4), Fowl Typhoid (wk 7).\n"
                            "8. Transition to growers' mash at week 7; remove newspapers on day 4."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Visual Diagnostic Guide: Chick Behavior",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Comfortable Chicks in a Well-Managed Brooder",
                    "content": {
                        "text": "Yellow chicks evenly distributed around feeders and waterers under infrared lamps in a circular brooder.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Brooder_chicks.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Brooder_chicks.jpg"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Chick Distribution Diagnostic Patterns Inside a Brooder Guard",
                    "content": {
                        "text": "Diagram showing 4 diagnostic chick distribution patterns: Huddled under heat (too cold), pushed to edges (too hot), one side (draught), and evenly spread (ideal 35°C).",
                        "svg": SVG_BROODER_DIAGNOSTIC
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Learning: Diagnostic Case",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Brooder Overheating Diagnosis",
                    "content": {
                        "text": "On Day 5, all 100 chicks are pushed to the outer edge of the circular hardboard, panting with open beaks near a charcoal jiko. What is the problem and solution?",
                        "options": [
                            "A: Chicks are cold; add more charcoal and close windows.",
                            "B: Brooder is overheated; open ventilators, widen chick guard, and reduce heat.",
                            "C: Chicks are hungry; add more chick mash.",
                            "D: Cold wind draft; seal air gaps."
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Panting and outer-edge crowding indicate overheating. Lower temperature by opening vents and widening the guard space."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Health & Vaccination Schedule",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Standard Vaccination Timeline for Chick Rearing",
                    "content": {
                        "text": (
                            "- **Week 2:** Gumboro Vaccine (Infectious Bursal Disease) administered in drinking water.\n"
                            "- **Weeks 3–4:** Newcastle Disease Vaccine administered via eye drops or drinking water.\n"
                            "- **Week 7:** Fowl Typhoid Vaccine administered via intramuscular injection.\n"
                            "- **Day 10:** Debeaking performed using hot blade debeaker to trim 1/3 of upper beak to prevent cannibalism."
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
                    "title": "Kakamega Smallholder Mortality Audit",
                    "content": {
                        "text": (
                            "**Scenario:** A farmer lost 40 out of 100 chicks in week 1. Investigation shows: chicks were kept in a square wooden box with fine sawdust litter, "
                            "and no pre-heating was done.\n\n"
                            "**Failure Points:**\n"
                            "1. *Square Box:* Chicks piled into 90° corners at night and suffocated.\n"
                            "2. *Sawdust Litter:* Chicks ate sawdust instead of feed, causing fatal crop impaction.\n"
                            "3. *No Pre-Heating:* Chicks entered cold 18°C air and suffered hypothermia."
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
                    "title": "Brooding Core Recall",
                    "content": {
                        "text": "1. What is the height of a standard chick guard?\n2. At what age is debeaking performed?\n3. Why is glucose solution given to day-old chicks?",
                        "options": [
                            "A: 25 cm; Day 10; Rapid energy for transport stress.",
                            "B: 50 cm; Week 8; Parasite control.",
                            "C: 10 cm; Day 1; Shell formation.",
                            "D: 100 cm; Week 4; Coccidiosis cure."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Chick guards are 25 cm high; debeaking occurs at Day 10; glucose provides instant energy."
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
                    "title": "KCSE Model Question: Brooder Management Rules",
                    "content": {
                        "text": (
                            "**Question:** State four management practices carried out in a brooder house to ensure healthy chick development. (4 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. Pre-heat brooder to 35°C 6 hours prior to chick arrival.\n"
                            "2. Provide fresh chick mash ad libitum and glucose water on arrival.\n"
                            "3. Maintain a circular chick guard (25 cm high) to eliminate sharp corners.\n"
                            "4. Execute vaccination schedule (Gumboro at 2 wks, Newcastle at 3–4 wks)."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Growers, Layers, and Broilers",
    "lesson_title": "Growers, Layers, and Broilers",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Overview of Poultry Production Lines",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 4 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Differentiate between growers, layers, and broilers by age and feed requirements.\n"
                            "- Detail calcium dynamics and eggshell formation in layers.\n"
                            "- Explain Feed Conversion Ratio (FCR) and coccidiostats in broiler production.\n"
                            "- Calculate daily feed budgets, bag durations, and nest box ratios for layer flocks.\n"
                            "- Apply KCSE principles to solve flock feeding problems."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Physiological Needs Across Production Stages",
                    "content": {
                        "text": (
                            "Poultry management is divided into three distinct production lines based on age and final product:\n"
                            "- **Growers (9–18 wks):** Replacement pullets developing skeletal frame without excess fat.\n"
                            "- **Layers (18 wks+):** Egg-producing hens requiring high calcium for shell synthesis.\n"
                            "- **Broilers (0–8 wks):** Meat birds selected for rapid growth and high Feed Conversion Ratio (FCR)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Comparative Production Stage Reference Table",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Stage-by-Stage Management Reference Table",
                    "content": {
                        "text": (
                            "| Stage | Age Range | Feed Type | Daily Ration | Key Operations |\n"
                            "|---|---|---|---|---|\n"
                            "| Growers | 9–18 weeks | Growers' Mash | 115 g / bird / day | Deworming, move to main house, dim light |\n"
                            "| Layers | 18–21 wks+ | Layers' Mash + Grain | 120 g mash + 65 g grain | Laying nests (1 per 5 layers), oyster shells, greens |\n"
                            "| Broilers | 0–8 weeks | Starter -> Finisher | Ad libitum | Deep litter, coccidiostats, target 1.5–2.0 kg weight |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Layer Nutrition & Calcium Dynamics",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Calcium Mobilization & Yolk Pigmentation",
                    "content": {
                        "text": (
                            "Producing an eggshell requires continuous calcium mobilization. If soluble oyster shell grit is omitted, "
                            "hens mobilize calcium from their own bones, causing cage fatigue and soft-shelled eggs.\n\n"
                            "Hanging green cabbage leaves serves two purposes: providing carotenoid pigments that darken yolk color to deep yellow, "
                            "and keeping birds occupied to prevent feather pecking."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Broiler Nutrition & Feed Conversion Ratio (FCR)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "FCR & Coccidiostat Formulations",
                    "content": {
                        "text": (
                            "Broilers are evaluated by Feed Conversion Ratio (FCR) — the mass of feed needed to produce 1 kg of meat. "
                            "A lower FCR indicates high efficiency. Starter mash contains coccidiostats to protect young intestinal walls from coccidiosis, "
                            "while finisher pellets provide high metabolisable energy for rapid muscle and fat deposition."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Quantitative Layer Feed Budgeting",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Worked Example: Feed & Nest Calculations for 400 Layers",
                    "content": {
                        "text": (
                            "**Scenario:** A farmer runs a flock of 400 active layers in Nakuru.\n\n"
                            "**1. Daily Feed Requirement:**\n"
                            "Ration: 120 g (0.12 kg) layers' mash per bird daily.\n"
                            "Daily Feed = 400 × 0.12 kg = 48 kg / day.\n\n"
                            "**2. Bag Duration (70 kg bag):**\n"
                            "Duration = 70 kg / 48 kg/day = 1.46 days per bag.\n\n"
                            "**3. Laying Nest Requirement:**\n"
                            "Parameter: 1 nest per 5 layers.\n"
                            "Minimum Nests = 400 / 5 = 80 nesting boxes."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Visual Guide to Laying Nests",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Individual Darkened Laying Box",
                    "content": {
                        "text": "Wooden individual laying nest with clean straw bedding, containing a fresh brown egg in a dimly lit house.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Laying_nest_box.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY 2.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Laying_nest_box.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Learning: Grower Feed Calculation",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Grower Flock Feed Budget",
                    "content": {
                        "text": "How much growers' mash is needed to feed 200 growers (115g/bird/day) for 1 week (7 days)?",
                        "options": [
                            "A: 23.0 kg",
                            "B: 161.0 kg",
                            "C: 120.0 kg",
                            "D: 80.5 kg"
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Daily feed = 200 × 0.115 kg = 23 kg/day. Weekly feed = 23 kg × 7 days = 161 kg."
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
                    "title": "Naivasha Egg Quality Optimization",
                    "content": {
                        "text": (
                            "**Scenario:** A Naivasha layer farm produced pale yellow yolks and thin-shelled eggs that cracked during transport.\n\n"
                            "**Interventions:**\n"
                            "1. Provided free-choice oyster shell grit in split troughs (restored shell thickness).\n"
                            "2. Suspended fresh kale/cabbage leaves daily (darkened yolk color to golden orange and stopped feather pecking)."
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
                    "title": "Production Line Recall",
                    "content": {
                        "text": "1. At what age do pullets begin laying?\n2. What feed is given to broilers from 0 to 4 weeks?\n3. Why are greens hung in layer houses?",
                        "options": [
                            "A: 18-21 weeks; Broiler Starter; Prevent pecking & darken yolks.",
                            "B: 8 weeks; Growers' mash; Increase body weight.",
                            "C: 30 weeks; Finisher pellets; Control coccidiosis.",
                            "D: 12 weeks; Layers' mash; Stop broodiness."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Layers start laying at 18-21 weeks; broilers get Starter mash for first 4 weeks; greens provide yolk pigment and prevent pecking."
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
                    "title": "KCSE Model Question: Feed Formulation Differences",
                    "content": {
                        "text": (
                            "**Question:** Differentiate between broiler starter mash and broiler finisher pellets in terms of age given, composition, and objective. (6 Marks)\n\n"
                            "**Model Answer:**\n"
                            "- **Broiler Starter:** Given from 0 to 4 weeks; high protein content with coccidiostats; objective is rapid skeletal growth and coccidiosis protection.\n"
                            "- **Broiler Finisher:** Given from 4 to 8 weeks; high metabolisable energy pellets; objective is fat deposition and rapid muscle weight gain before slaughter."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Poultry Rearing Systems",
    "lesson_title": "Poultry Rearing Systems",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Overview of Rearing Systems",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 5 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Compare extensive (free-range), semi-intensive (fold), and intensive (deep litter, battery cage) systems.\n"
                            "- Detail structural dimensions of fold units (3.5m x 1.5m x 1.5m) and battery cages.\n"
                            "- Evaluate disease risks, parasite cycles, stocking densities, and egg cleanliness across systems.\n"
                            "- Select the appropriate system for breeding stock vs commercial egg production."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Spectrum of Housing Systems",
                    "content": {
                        "text": (
                            "Poultry rearing systems range from extensive (low input, free range) to semi-intensive (mobile folds) "
                            "and intensive (deep litter and battery cages). System selection depends on land size, capital, labor, and production goals."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Structural Specifications: Portable Fold Unit",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Structural Specifications of a Portable Fold Unit",
                    "content": {
                        "text": "Diagram of fold unit (3.5m long x 1.5m wide x 1.5m high) showing 1/3 roofed shelter and 2/3 wire-mesh run with handles.",
                        "svg": SVG_FOLD_UNIT
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Architectural Layout: Battery Cage System",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Cross-Section of a Battery Cage Unit",
                    "content": {
                        "text": "Diagram showing slanting wire floor, front roll-out egg tray, feed/water troughs, and dropping gap at rear.",
                        "svg": SVG_BATTERY_CAGE
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "System Comparison Table",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Comparison of Deep Litter vs Battery Cage Systems",
                    "content": {
                        "text": (
                            "| Parameter | Deep Litter System | Battery Cage System |\n"
                            "|---|---|---|\n"
                            "| Stocking Density | Moderate (1 m² / 2-3 birds) | Extremely High |\n"
                            "| Egg Cleanliness | Poor (litter staining) | Excellent (rolls out immediately) |\n"
                            "| Culling Records | Difficult | Easy (individual cage records) |\n"
                            "| Vices Risk | High (cannibalism, egg eating) | Low (isolation) |\n"
                            "| Parasite Risk | High (coccidiosis in litter) | Low (wire floor isolates manure) |\n"
                            "| Breeding Use | Excellent (allows natural mating) | Unusable (mating impossible) |\n"
                            "| Welfare Issues | Dust, crop impaction | Cage fatigue, toe/comb bruises |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Visual Exploration of Intensive Systems",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Commercial Battery Cage Installation",
                    "content": {
                        "text": "Multi-tier battery cage system showing brown layers, front feeding troughs, and automated egg roll-out trays.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Battery_cage_system.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Battery_cage_system.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Learning: System Selection",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "System Choice for Pedigree Breeding Stock",
                    "content": {
                        "text": "Which rearing system MUST be selected for a farm producing fertile hatching eggs from pedigree cocks and hens?",
                        "options": [
                            "A: Battery Cage System because of high stocking density.",
                            "B: Free Range because it is cheapest.",
                            "C: Deep Litter System because it allows natural mating.",
                            "D: Fold System because it spreads manure."
                        ],
                        "correct_answer_index": 2,
                        "explanation": "Natural mating is physically impossible in battery cages. Pedigree breeding requires deep litter communal housing where cocks run with hens."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Epidemiology & Biosecurity Across Systems",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Pathogen Transmission Dynamics",
                    "content": {
                        "text": (
                            "- **Free Range:** Zero biosecurity; high exposure to wild birds (avian flu) and soil roundworms.\n"
                            "- **Fold System:** Mobile pens moved daily to clean ground, breaking parasite life cycles.\n"
                            "- **Deep Litter:** Accumulating droppings in damp litter cause rapid sporulation of coccidial oocysts.\n"
                            "- **Battery Cage:** Wire mesh isolates birds from manure, completely breaking coccidiosis and worm cycles."
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
                    "title": "Uasin Gishu System Selection Audit",
                    "content": {
                        "text": (
                            "**Scenario:** An investor with a 1/4 acre plot near Eldoret wants to maximize commercial egg sales without breeding.\n\n"
                            "**Recommendation:** Install triple-tier battery cages. This maximizes vertical space, eliminates egg eating, "
                            "provides clean eggs, and simplifies individual culling."
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
                    "title": "Rearing System Recall",
                    "content": {
                        "text": "1. What are the dimensions of a standard fold unit?\n2. What metabolic disorder affects caged layers?\n3. What is the stocking density of the deep litter system?",
                        "options": [
                            "A: 3.5m x 1.5m x 1.5m; Cage fatigue; 1 m² per 2-3 birds.",
                            "B: 1m x 1m x 1m; Newcastle; 1 m² per 10 birds.",
                            "C: 10m x 5m x 2m; Gumboro; 1 m² per 1 bird.",
                            "D: 2m x 2m x 2m; Coccidiosis; 1 m² per 5 birds."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Fold units measure 3.5m x 1.5m x 1.5m; lack of exercise in cages causes cage fatigue; deep litter holds 2-3 birds per m²."
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
                    "title": "KCSE Model Essay: Deep Litter Evaluation (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** State five advantages and five disadvantages of the Deep Litter System. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "**Advantages:** (1) High stocking rate, (2) Low labor requirement, (3) Manure accumulation, (4) Protection from predators/weather, (5) Eggs laid in indoor nests.\n"
                            "**Disadvantages:** (1) High prevalence of vices (cannibalism, egg eating), (2) Pathogen/coccidiosis accumulation in litter, (3) Impossible to keep individual production records, (4) Litter supply cost, (5) Rapid disease spread via communal waterers."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_6_DATA = {
    "unit_order": 6,
    "unit_name": "Stress, Vices, and Diagnosis in Poultry",
    "lesson_title": "Stress, Vices, and Diagnosis in Poultry",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Physiological Stress & Behavioral Vices",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 6 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Differentiate between physiological stress and behavioral vices.\n"
                            "- Identify root causes of feather pecking, vent/toe cannibalism, and egg eating.\n"
                            "- Explain the pathological link between rectal prolapse and cannibalism.\n"
                            "- Execute diagnostic workflows to stop vice outbreaks in layer houses."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Definitions of Stress & Vices",
                    "content": {
                        "text": (
                            "- **Stress:** A physiological state of discomfort caused by external factors (overcrowding, noise, sudden routine change, high temp) that lowers production.\n"
                            "- **Vice:** An abnormal, destructive habit developed by birds (cannibalism, egg eating) that spreads rapidly through imitation."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Pathology of Cannibalism & Vent Pecking",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Rectal Prolapse & Blood Attraction",
                    "content": {
                        "text": (
                            "Rectal prolapse occurs when the lower oviduct remains inverted and exposed after laying a large egg. "
                            "Chickens are naturally attracted to bright red tissue and blood. Once pecking begins and blood is drawn, "
                            "the habit escalates into fatal vent cannibalism. Bright light in laying boxes accelerates this trigger."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Diagnostic Matrix: Causes, Effects & Prevention",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Poultry Vices Diagnostic Matrix",
                    "content": {
                        "text": (
                            "| Vice Observed | Diagnostic Causes | Economic Effects | Preventive Actions |\n"
                            "|---|---|---|---|\n"
                            "| Feather Pecking & Cannibalism | Overcrowding, high temp, bright light, parasite itch, protein deficiency | Mortality, carcass damage, high culling rate | Debeaking, dim lights, darken nests, hang greens, apply pine tar |\n"
                            "| Egg Eating | Soft shells, bright nests, insufficient nest boxes (1 per 5), idleness | Loss of saleable eggs, vice spreads by imitation | Collect eggs 2x daily, raise boxes, darken nests, oyster shell grit |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Visual Diagnostic Flowchart",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Diagnostic Workflow for Poultry Vice Interventions",
                    "content": {
                        "text": "Flowchart mapping symptoms (bleeding vents vs broken shells) to root causes and corrective farm actions.",
                        "svg": SVG_BROODER_DIAGNOSTIC
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Interactive Scenario Diagnosis",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Vent Pecking Outbreak Intervention",
                    "content": {
                        "text": "You find three dead layers with pecked vents in a bright, hot layer house with only 40 nests for 500 birds. What are your three immediate corrective actions?",
                        "options": [
                            "A: Add charcoal, close windows, and add more feed.",
                            "B: Darken nests/windows, add nests to reach 100 boxes (1:5 ratio), isolate injured birds and hang greens.",
                            "C: Move birds to battery cages immediately.",
                            "D: Vaccinate for Newcastle disease."
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Vent pecking is triggered by bright nest light and nest competition. Darken nests, increase nests to 1:5 ratio (100 boxes), isolate victims, and hang greens."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Preventive & Surgical Modifications",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Debeaking & Chemical Treatments",
                    "content": {
                        "text": (
                            "- **Debeaking:** Performed at 10 days using a heated cauterizing blade to trim 1/3 of upper beak.\n"
                            "- **Pine Tar Application:** Applied to pecked wounds; its dark color and bitter taste deter further pecking.\n"
                            "- **Greens Suspension:** Cabbages hung at head height keep birds physically occupied."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Real-World Application Scenario",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Nyeri Layer Farm Case Study",
                    "content": {
                        "text": (
                            "**Scenario:** A farmer in Nyeri reported 15% egg losses due to egg eating. "
                            "Investigation revealed: nest boxes were facing direct sunlight and eggs were collected only once in the evening.\n\n"
                            "**Resolution:** Shaded nest boxes, added oyster shell grit to harden shells, and increased egg collection to twice daily (noon and 4 PM)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Stress & Vice Core Recall",
                    "content": {
                        "text": "1. What is a rectal prolapse?\n2. Name two causes of egg eating.\n3. How does hanging greens prevent vices?",
                        "options": [
                            "A: Protrusion of lower oviduct after laying; Soft shells & bright nests; Reduces idleness.",
                            "B: Bacterial infection; Overfeeding; Provides protein.",
                            "C: Parasite itch; High humidity; Cures coccidiosis.",
                            "D: Leg paralysis; Cold weather; Hardens egg shells."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Prolapse is exposed oviduct tissue; egg eating is caused by soft shells/bright nests; hanging greens occupies birds."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Causes & Control of Cannibalism (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Explain four causes of cannibalism in a flock of layers, and state one control measure for each. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Overcrowding:** Control by adhering to recommended stocking density (1 m² per 2-3 birds).\n"
                            "2. **Bright Light in Nests:** Control by darkening laying boxes and shading windows.\n"
                            "3. **Dietary Protein/Mineral Deficiency:** Control by providing balanced layers' mash and oyster shell grit.\n"
                            "4. **Prolapse/Injuries:** Control by isolating injured birds and applying pine tar."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_7_DATA = {
    "unit_order": 7,
    "unit_name": "Marketing Poultry Products",
    "lesson_title": "Marketing Poultry Products",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Marketing Standards for Eggs & Meat",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 7 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Distinguish between sorting and grading of poultry products.\n"
                            "- Detail six key grading parameters for market eggs (weight 57g, shape, cleanliness, color, texture, candling).\n"
                            "- State slaughter age (1-2.5 months) and live weight (1.5-2.0 kg) targets for broilers.\n"
                            "- Solve KCSE marketing scenario questions to prevent transport losses."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Sorting vs Grading Definitions",
                    "content": {
                        "text": (
                            "- **Sorting:** Initial clearance step separating eggs or carcasses based on visible defects or dirt.\n"
                            "- **Grading:** Categorizing sorted high-quality products into uniform lots based on weight class and market standards."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Egg Sorting & Grading Reference Table",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Egg Grading Parameters Table",
                    "content": {
                        "text": (
                            "| Grading Factor | Market Standard | Practical Reason |\n"
                            "|---|---|---|\n"
                            "| Size / Weight | Average 57 grams | Large uniform eggs fetch premium prices |\n"
                            "| Shape | Oval (distinct broad/narrow ends) | Abnormal shapes break easily in trays |\n"
                            "| Cleanliness | Clean shell, free from dung | Consumers reject dirty eggs; bacteria risk |\n"
                            "| Shell Color | Uniform brown color | Strong consumer preference |\n"
                            "| Shell Texture | Smooth, no cracks | Rough shells break in transit |\n"
                            "| Candling Quality | Small air sac, stable yolk | Verifies freshness & absence of blood spots |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Broiler Meat Processing & Marketing",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Broiler Slaughter & Dressing Standards",
                    "content": {
                        "text": (
                            "Broilers are slaughtered at 1 to 2.5 months of age when they reach a target live weight of 1.5 to 2.0 kg. "
                            "Dressing involves slaughtering, defeathering, eviscerating, and chilling the carcass before vacuum packing for retail delivery."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Visualizing Market-Grade Eggs",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Graded and Packed Brown Eggs",
                    "content": {
                        "text": "Cardboard egg trays filled with uniform, clean, brown oval eggs sorted by weight class.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Graded_brown_eggs.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Graded_brown_eggs.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Interactive Learning: Market Specification Matching",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Poultry Marketing Specification Matching",
                    "content": {
                        "text": "Match the metric to its standard:\n1. Average egg weight\n2. Broiler slaughter age\n3. Broiler live weight target\n4. Preferred shell color",
                        "options": [
                            "A: 1->57g; 2->1-2.5 months; 3->1.5-2.0 kg; 4->Brown.",
                            "B: 1->100g; 2->6 months; 3->5.0 kg; 4->White.",
                            "C: 1->30g; 2->2 weeks; 3->0.5 kg; 4->Blue.",
                            "D: 1->75g; 2->4 months; 3->3.0 kg; 4->Green."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Average egg weight is 57g; broiler slaughter age is 1-2.5 months; live weight is 1.5-2.0 kg; preferred shell color is brown."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Real-World Application Scenario",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Kiambu Cooperative 10,000 Egg Operations",
                    "content": {
                        "text": (
                            "**Scenario:** Kiambu Farmers Cooperative collects 10,000 eggs daily. By installing an automatic candling and grading machine, "
                            "they sort eggs into 57g weight classes and eliminate blood-spotted eggs.\n\n"
                            "**Economic Result:** Premium supermarket contracts were secured at a 35% higher price per tray."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Economic Value of On-Farm Grading",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Preventing Transport Loss",
                    "content": {
                        "text": (
                            "Transporting unsorted eggs results in cracked eggs leaking onto healthy ones, ruining entire crates. "
                            "On-farm candling and sorting ensures only intact, fresh eggs incur transport costs."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Marketing Core Recall",
                    "content": {
                        "text": "1. What is the average market egg weight?\n2. What is dressing in poultry marketing?\n3. State the slaughter weight of broilers.",
                        "options": [
                            "A: 57g; Slaughtering, defeathering, and eviscerating; 1.5-2.0 kg.",
                            "B: 80g; Feeding layers; 4.0 kg.",
                            "C: 40g; Incubating eggs; 0.5 kg.",
                            "D: 65g; Debeaking chicks; 3.0 kg."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Standard egg weight is 57g; dressing is carcass processing; broiler live weight is 1.5-2.0 kg."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: On-Farm Egg Grading Scenario (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** A farmer transported 1,000 unsorted eggs to a merchant who rejected 300 eggs due to poor quality. Explain how on-farm grading could have prevented this loss. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "On-farm grading separates defective eggs before transport, saving freight costs. The farmer should have applied:\n"
                            "1. **Weight Grading:** Sorted to 57g standard to command uniform prices.\n"
                            "2. **Cleanliness:** Dry-cleaned dirty shells to prevent consumer rejection.\n"
                            "3. **Shape Inspection:** Rejected abnormal shapes that break in transit.\n"
                            "4. **Texture & Soundness:** Removed cracked shells to prevent leakage onto healthy eggs.\n"
                            "5. **Candling Quality:** Checked freshness (small air sac) and eliminated blood spots."
                        )
                    }
                }
            ]
        }
    ]
}

ALL_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA,
    LESSON_6_DATA,
    LESSON_7_DATA
]
