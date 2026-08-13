"""
VLearn Form 4 Agriculture — Topic 2 Data File
Topic 2: Livestock Production VI (Cattle)

Contains structured data for all 6 Learning Modules / Lessons:
  Lesson 1: Calf Feeding and Colostrum (10 Pages)
  Lesson 2: Early and Late Weaning (10 Pages)
  Lesson 3: Replacement Stock and Calf Housing (10 Pages)
  Lesson 4: Milk Composition, Secretion, Let-Down and Udder Structure (10 Pages)
  Lesson 5: Clean Milk Production, Milking and Dry-Cow Therapy (10 Pages)
  Lesson 6: Milk and Beef Products and Marketing (8 Pages)
Total: 58 Pages, ~200 Granular Lesson Blocks
"""

# =============================================================================
# SVG DIAGRAM DEFINITIONS
# =============================================================================

SVG_CALF_PEN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" style="background-color: #0f172a; border-radius: 8px;">
  <title>Standard Slatted-Floor Permanent Calf Pen</title>

  <!-- Ground Concrete Base (Slanted) -->
  <polygon points="100,420 700,400 700,440 100,460" fill="#334155" stroke="#475569" stroke-width="2"/>
  <text x="350" y="445" font-family="Arial" font-size="12" fill="#cbd5e1">Slanted Concrete Base (Drainage Slope)</text>

  <!-- Drainage Channel -->
  <rect x="680" y="380" width="40" height="70" fill="#0284c7" opacity="0.6"/>
  <text x="682" y="370" font-family="Arial" font-size="10" fill="#38bdf8">Drain</text>

  <!-- Raised Slatted Wooden Floor (30cm Height) -->
  <g fill="#b45309" stroke="#78350f" stroke-width="2">
    <rect x="150" y="350" width="30" height="10" rx="2"/>
    <rect x="190" y="350" width="30" height="10" rx="2"/>
    <rect x="230" y="350" width="30" height="10" rx="2"/>
    <rect x="270" y="350" width="30" height="10" rx="2"/>
    <rect x="310" y="350" width="30" height="10" rx="2"/>
    <rect x="350" y="350" width="30" height="10" rx="2"/>
    <rect x="390" y="350" width="30" height="10" rx="2"/>
    <rect x="430" y="350" width="30" height="10" rx="2"/>
    <rect x="470" y="350" width="30" height="10" rx="2"/>
    <rect x="510" y="350" width="30" height="10" rx="2"/>
    <rect x="550" y="350" width="30" height="10" rx="2"/>
    <rect x="590" y="350" width="30" height="10" rx="2"/>
    <rect x="630" y="350" width="30" height="10" rx="2"/>
  </g>
  
  <!-- Support Legs (30cm Raised) -->
  <rect x="150" y="360" width="20" height="60" fill="#78350f"/>
  <rect x="640" y="360" width="20" height="45" fill="#78350f"/>
  <line x1="80" y1="360" x2="80" y2="420" stroke="#f8fafc" stroke-width="1.5"/>
  <text x="15" y="395" font-family="Arial" font-size="11" fill="#f8fafc" font-weight="bold">30cm Raised</text>

  <!-- Pen Walls & Roof -->
  <rect x="130" y="100" width="540" height="250" fill="none" stroke="#94a3b8" stroke-width="4"/>
  <polygon points="100,100 400,40 730,100" fill="#1e293b" stroke="#64748b" stroke-width="3"/>
  <text x="350" y="80" font-family="Arial" font-size="13" fill="#f8fafc" font-weight="bold">Corrugated Roof</text>

  <!-- Draught-Free Window (High Up) -->
  <rect x="160" y="130" width="100" height="50" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
  <text x="170" y="160" font-family="Arial" font-size="10" fill="#f8fafc">High Window (No Draughts)</text>

  <!-- Sunlight Entry Ray -->
  <polygon points="260,130 500,350 400,350 210,130" fill="#fde047" opacity="0.15"/>
  <text x="330" y="220" font-family="Arial" font-size="11" fill="#fde047">Direct Sunlight (Vitamin D)</text>

  <!-- Feed Trough -->
  <rect x="600" y="280" width="60" height="60" fill="#b45309" rx="4"/>
  <text x="605" y="315" font-family="Arial" font-size="10" fill="#ffffff">Feed Trough</text>
</svg>"""

SVG_UDDER_PATHWAY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" style="background-color: #0f172a; border-radius: 8px;">
  <title>Anatomical Pathway of Milk Secretion &amp; Udder Structure</title>

  <!-- Flowchart Nodes -->
  <g font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">
    <!-- Node 1: Alveolus -->
    <rect x="50" y="170" width="140" height="60" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="3"/>
    <text x="120" y="195" fill="#f97316">Alveolus Cells</text>
    <text x="120" y="215" fill="#94a3b8" font-weight="normal" font-size="10">(Milk Synthesis - Prolactin)</text>

    <!-- Arrow 1 -->
    <path d="M 190 200 L 230 200" stroke="#38bdf8" stroke-width="3"/>

    <!-- Node 2: Lobules & Lobes -->
    <rect x="230" y="170" width="140" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <text x="300" y="195" fill="#38bdf8">Lobules &amp; Lobes</text>
    <text x="300" y="215" fill="#94a3b8" font-weight="normal" font-size="10">(Alveoli Clusters)</text>

    <!-- Arrow 2 -->
    <path d="M 370 200 L 410 200" stroke="#38bdf8" stroke-width="3"/>

    <!-- Node 3: Lactiferous Ducts -->
    <rect x="410" y="170" width="140" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <text x="480" y="195" fill="#38bdf8">Lactiferous Ducts</text>
    <text x="480" y="215" fill="#94a3b8" font-weight="normal" font-size="10">(Drainage Channels)</text>

    <!-- Arrow 3 -->
    <path d="M 550 200 L 590 200" stroke="#38bdf8" stroke-width="3"/>

    <!-- Node 4: Cisterns & Teat -->
    <rect x="590" y="170" width="160" height="60" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="3"/>
    <text x="670" y="195" fill="#22c55e">Gland &amp; Teat Cisterns</text>
    <text x="670" y="215" fill="#94a3b8" font-weight="normal" font-size="10">(Teat Canal Output)</text>
  </g>

  <!-- Hormonal Trigger Callout -->
  <rect x="250" y="40" width="300" height="70" rx="8" fill="#334155" stroke="#fde047" stroke-width="2"/>
  <text x="400" y="65" font-family="Arial" font-size="13" fill="#fde047" font-weight="bold" text-anchor="middle">OXCYTOCIN LET-DOWN REFLEX</text>
  <text x="400" y="90" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Contracts Myoepithelial Cells (Active 7 - 10 Mins)</text>
  <line x1="400" y1="110" x2="400" y2="170" stroke="#fde047" stroke-width="2" stroke-dasharray="4,4"/>
</svg>"""

SVG_VALUE_CHAIN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; border-radius: 8px;">
  <title>Dairy and Beef Processing Value-Chain Mapping</title>

  <!-- Central Raw Milk Node -->
  <rect x="50" y="180" width="140" height="80" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
  <text x="120" y="215" font-family="Arial" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">Raw Bovine Milk</text>
  <text x="120" y="235" font-family="Arial" font-size="10" fill="#7dd3fc" text-anchor="middle">(Perishable Produce)</text>

  <!-- Output Branches -->
  <!-- Branch 1: Cream & Butter/Ghee -->
  <path d="M 190 200 L 280 100" stroke="#f59e0b" stroke-width="2"/>
  <rect x="280" y="70" width="160" height="50" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="360" y="95" font-family="Arial" font-size="12" fill="#fbbf24" font-weight="bold" text-anchor="middle">Cream -> Butter &amp; Ghee</text>
  <text x="360" y="110" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">(Churning &amp; Water Evaporation)</text>

  <!-- Branch 2: Pasteurized & UHT Milk -->
  <path d="M 190 210 L 280 180" stroke="#22c55e" stroke-width="2"/>
  <rect x="280" y="155" width="160" height="50" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <text x="360" y="180" font-family="Arial" font-size="12" fill="#4ade80" font-weight="bold" text-anchor="middle">UHT Milk (130-135°C)</text>
  <text x="360" y="195" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">(Long Shelf-Life Sterile Pack)</text>

  <!-- Branch 3: Cheese -->
  <path d="M 190 230 L 280 260" stroke="#38bdf8" stroke-width="2"/>
  <rect x="280" y="235" width="160" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="360" y="260" font-family="Arial" font-size="12" fill="#38bdf8" font-weight="bold" text-anchor="middle">Cheese (Casein/Whey)</text>
  <text x="360" y="275" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">(Coagulated &amp; Compressed)</text>

  <!-- Branch 4: Skim Milk -->
  <path d="M 190 240 L 280 340" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="280" y="315" width="160" height="50" rx="6" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
  <text x="360" y="340" font-family="Arial" font-size="12" fill="#f8fafc" font-weight="bold" text-anchor="middle">Skim Milk</text>
  <text x="360" y="355" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">(Butterfat Removed - Calf Feed)</text>

  <!-- Marketing Channels Box -->
  <rect x="490" y="70" width="260" height="300" rx="10" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="620" y="100" font-family="Arial" font-size="14" fill="#fde047" font-weight="bold" text-anchor="middle">KENYAN MARKETING CHANNELS</text>
  
  <g font-family="Arial" font-size="11" fill="#f8fafc">
    <text x="510" y="140" font-weight="bold">• Kenya Dairy Board (KDB)</text>
    <text x="525" y="160" fill="#cbd5e1">Statutory Quality Regulator</text>

    <text x="510" y="190" font-weight="bold">• Dairy Cooperatives &amp; Processors</text>
    <text x="525" y="210" fill="#cbd5e1">KCC, Brookside, Tuzo, Limuru</text>

    <text x="510" y="240" font-weight="bold">• Livestock Marketing Div. (LMD)</text>
    <text x="525" y="260" fill="#cbd5e1">Pastoralist Cattle Transport</text>

    <text x="510" y="290" font-weight="bold">• Kenya Meat Commission (KMC)</text>
    <text x="525" y="310" fill="#cbd5e1">Statutory Abattoirs &amp; Meat Canning</text>
  </g>
</svg>"""


# =============================================================================
# LESSON 1 DATA: Calf Feeding and Colostrum (10 Pages)
# =============================================================================

LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Calf Feeding and Colostrum",
    "lesson_title": "Calf Feeding and Colostrum",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Calf Management & Colostrum",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the physiological importance of colostrum for newborn calves.\n"
                            "- Compare natural (direct suckling) and artificial (bucket feeding) methods.\n"
                            "- Execute the 6-step bucket-training procedure for a calf.\n"
                            "- Identify root causes of calf scours and esophageal groove failure.\n"
                            "- Differentiate feeding methods in KCSE examination questions."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Biological Significance of Colostrum",
                    "content": {
                        "text": (
                            "Cattle production is a cornerstone of Kenya's agricultural economy. The newborn calf is born without an active immune system. "
                            "It relies entirely on colostrum — the first thick, yellowish milk secreted by the mother immediately after calving. "
                            "Colostrum is highly digestible, rich in antibodies (immunoglobulins), packed with vitamins (especially Vitamin A), and acts as a laxative to expel meconium."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Physiological Mechanism & Gut Closure",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Esophageal Groove & Passive Immunity Transfer",
                    "content": {
                        "text": (
                            "**Layer 1 (Simple Intuition):** A newborn calf arrives with an empty protective shield. Colostrum is the mother's starter kit, "
                            "delivering instant immune antibodies and clearing out the sticky dark first feces (meconium) accumulated during gestation.\n\n"
                            "**Layer 2 (Technical Terms):** Colostrum contains immunoglobulins for passive immunity. At birth, the calf's stomach is pre-ruminant; "
                            "the muscular esophageal groove folds to bypass the undeveloped rumen/reticulum/omasum, routing liquid milk straight to the abomasum.\n\n"
                            "**Layer 3 (Biological Mechanism):** The newborn intestinal lining is highly porous, allowing large antibody proteins to pass directly into the bloodstream intact. "
                            "However, 'gut closure' begins rapidly: antibody absorption drops by 50% after 12 hours and stops completely by 24–36 hours. "
                            "Feeding colostrum within the first 3–5 hours is critical.\n\n"
                            "**Layer 4 (Agricultural Application):** On a dairy farm in Githunguri, a farmer separates a Friesian calf immediately and feeds colostrum within 1 hour "
                            "via bucket feeding to maintain accurate cow milk yield records."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Technical Terms Reference",
                    "content": {
                        "text": (
                            "- **Colostrum:** First milk produced immediately after calving, rich in antibodies, nutrients, and laxative properties.\n"
                            "- **Direct Suckling:** Natural feeding method where the calf suckles directly from the cow's teats.\n"
                            "- **Bucket Feeding:** Artificial feeding method where the calf is trained to drink measured milk from a bucket.\n"
                            "- **Scouring:** Severe watery diarrhea in calves caused by cold milk, dirty buckets, or pathogens.\n"
                            "- **Esophageal Groove:** Muscular fold in young ruminants that channels liquid milk directly into the abomasum."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Natural vs Artificial Feeding Comparison Table",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Comparison of Natural (Suckling) vs Artificial (Bucket) Feeding",
                    "content": {
                        "text": (
                            "| Feature | Natural Feeding (Direct Suckling) | Artificial Feeding (Bucket Feeding) |\n"
                            "|---|---|---|\n"
                            "| Method | Calf suckles cow directly | Calf drinks measured warm milk from bucket |\n"
                            "| Milk Temperature | Always perfect body temp (37–39°C) | Risk of being fed cold if unmonitored |\n"
                            "| Contamination Risk | Extremely low (sterile teat) | High if buckets or hands are dirty |\n"
                            "| Scouring Incidence | Lower occurrence | Higher risk if hygiene is poor |\n"
                            "| Record Keeping | Difficult to measure cow yield | Easy and highly accurate milk recording |\n"
                            "| Ration Regulation | Hard to control | Precise regulation of milk volume |\n"
                            "| Milking Let-Down | Cow may refuse let-down if calf dies | Cow lets down milk without calf presence |\n"
                            "| Labor Requirement | Extremely low | Labor-intensive (training & washing) |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Step-by-Step Procedure: Bucket-Training a Calf",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Bucket-Training a Calf",
                    "content": {
                        "text": (
                            "**Purpose:** To train a newborn calf to drink warm milk independently from an open bucket.\n\n"
                            "**Step 1: Measure & Prepare Warm Milk**\n"
                            "Pour measured fresh, warm milk (37°C–39°C) into a thoroughly disinfected bucket.\n\n"
                            "**Step 2: Position Calf & Bucket**\n"
                            "Stand astride the calf's neck to restrain it, placing the bucket securely on the floor in front.\n\n"
                            "**Step 3: Introduce Sucking Reflex**\n"
                            "Dip clean index and middle fingers into warm milk and insert them gently into the calf's mouth to stimulate suckling.\n\n"
                            "**Step 4: Lower Head into Bucket**\n"
                            "Slowly guide the calf's head downward until its mouth is partially submerged in milk while it suckles your fingers.\n\n"
                            "**Step 5: Gradually Withdraw Fingers**\n"
                            "As the calf draws milk upward, slowly slide fingers out of its mouth so it drinks directly from the surface.\n\n"
                            "**Step 6: Repeat & Reinforce**\n"
                            "Repeat over 2–3 sessions until the calf drinks independently without needing fingers.\n\n"
                            "**Precautions:** Wash hands with soap to prevent E. coli scours; ensure milk is warm (37–39°C) to close the esophageal groove."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Visual Guide: Bucket Feeding Technique",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Bucket Feeding a Young Dairy Calf",
                    "content": {
                        "text": "Stockman bucket-training a young dairy calf using a clean, wide-mouthed bucket in an individual pen.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Bucket_feeding_calf.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Bucket_feeding_calf.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Precautions & Esophageal Groove Pathophysiology",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Cold Milk Pathophysiology & Scouring Risks",
                    "content": {
                        "text": (
                            "- **Cold Milk Pathophysiology:** Milk fed below body temperature (below 37°C) fails to stimulate the neural esophageal groove reflex. "
                            "The liquid milk flows into the undeveloped rumen instead of the abomasum, where it putrefies, multiplies bacteria, and causes severe bloat and fatal scouring.\n"
                            "- **Hygiene Risk:** Dirty hands or unwashed buckets introduce Escherichia coli and Salmonella, causing infectious scours.\n"
                            "- **Artificial Colostrum Recipe Flag:** Source lists a recipe (egg, warm water, cod liver oil, castor oil). Note: Source contains overlapping water volumes (0.86 L vs 1.0 L); both are preserved for exam alignment."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Learning: Scours Diagnosis",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Calf Scours Diagnostic Case",
                    "content": {
                        "text": "A 3-day-old calf suffers from severe watery scours. The buckets are washed daily, but milk sits on the counter for 3 hours before feeding. What is the cause?",
                        "options": [
                            "A: Hairballs swallowed from group housing.",
                            "B: Cold milk failed to stimulate esophageal groove, causing milk to ferment in the rumen.",
                            "C: Oxytocin inhibition in the cow.",
                            "D: Excess colostrum fed in week 1."
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Milk sitting for 3 hours cools down. Cold milk bypasses the esophageal groove and enters the rumen where it putrefies, triggering scours."
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
                    "title": "Kericho Dairy Farm Case Study",
                    "content": {
                        "text": (
                            "**Scenario:** Mrs. Chebet has a high-yielding Jersey cow that only lets down milk when the calf direct-suckles. "
                            "She has no record of milk yield or calf intake.\n\n"
                            "**Resolution:** Transition the calf to bucket feeding. This stabilizes milk let-down without calf presence, "
                            "enables exact daily milk yield recording, and ensures the calf receives a measured ration."
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
                    "title": "Colostrum Core Recall",
                    "content": {
                        "text": "1. Why is colostrum vital for a calf?\n2. Why must colostrum be fed within the first 3-5 hours?\n3. What is the function of the esophageal groove?",
                        "options": [
                            "A: Provides antibodies & laxative; Intestinal gut closure occurs within 24-36 hrs; Routes milk to abomasum.",
                            "B: Increases butterfat; Prevents mastitis; Digestion of grass.",
                            "C: Replaces water; Cures pneumonia; Stimulates rumen papillae.",
                            "D: Stops bloat; Increases live weight; Produces oxytocin."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Colostrum transfers passive immunity antibodies before gut closure (24-36h); esophageal groove routes milk directly to abomasum."
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
                    "title": "KCSE Model Question: Natural vs Artificial Feeding Trade-Offs",
                    "content": {
                        "text": (
                            "**Question:** Differentiate between natural and artificial calf feeding methods, stating two advantages and two disadvantages of the artificial method. (6 Marks)\n\n"
                            "**Model Answer:**\n"
                            "- **Difference:** Natural feeding involves the calf suckling directly from the cow's teats; artificial feeding involves training the calf to drink measured milk from a bucket.\n"
                            "- **Advantages of Artificial (Bucket):** (1) Enables accurate daily milk yield recording, (2) Allows precise regulation of milk intake to prevent over/underfeeding.\n"
                            "- **Disadvantages of Artificial (Bucket):** (1) Labor-intensive equipment washing and training, (2) Risk of scours if cold milk or dirty buckets are used."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 2 DATA: Early and Late Weaning (10 Pages)
# =============================================================================

LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Early and Late Weaning",
    "lesson_title": "Early and Late Weaning",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Physiological Principles of Weaning",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define weaning and differentiate Early Weaning (week 10) from Late Weaning (week 16).\n"
                            "- Explain how volatile fatty acids (VFAs) stimulate rumen papillae development.\n"
                            "- Execute an early weaning feed schedule protocol.\n"
                            "- Calculate milk and concentrate feed budgets for weaning calf herds.\n"
                            "- Apply KCSE weaning principles to solve farm economics problems."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Rumen Papillae Development & VFAs",
                    "content": {
                        "text": (
                            "Weaning is the physiological process of stopping liquid milk feeding and transitioning the calf to solid feeds. "
                            "At birth, the abomasum represents 70% of stomach capacity. Introducing solid concentrates (calf starter pellets) "
                            "produces volatile fatty acids (butyrate and propionate) during fermentation, which stimulate the growth of rumen papillae "
                            "and physically expand the rumen for forage digestion."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Early vs Late Weaning Systems",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "System Protocols & Economic Trade-Offs",
                    "content": {
                        "text": (
                            "- **Early Weaning:** Whole milk fed up to week 8, reduced gradually and cut off by week 10. Accelerates rumen papillae development using high-protein concentrates; saves whole milk for commercial sale.\n"
                            "- **Late Weaning:** Whole milk fed to week 3, gradually replaced with skim milk up to week 14, weaning completed by week 16. Highly economical for farms with cheap skim milk from creameries."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Step-by-Step Procedure: Early Weaning Schedule",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Early Weaning Protocol",
                    "content": {
                        "text": (
                            "**Purpose:** To transition a calf to solid feed by week 10.\n\n"
                            "**Step 1: Weeks 1–3 (Colostrum & Whole Milk)**\n"
                            "Colostrum ad libitum in week 1, then 5 kg/day whole milk in weeks 2–3.\n\n"
                            "**Step 2: Weeks 4–5 (Introduce Concentrates)**\n"
                            "Increase milk to 6 kg/day; introduce 0.25 kg/day calf starter pellets.\n\n"
                            "**Step 3: Weeks 6–7 (Concentrates & Soft Forage)**\n"
                            "Maintain 6 kg/day milk; increase concentrates to 0.50 kg/day + clean wilted lucerne forage.\n\n"
                            "**Step 4: Weeks 8–9 (Gradual Milk Reduction)**\n"
                            "Reduce milk to 5 kg/day; increase concentrates to 0.75 kg/day.\n\n"
                            "**Step 5: Weeks 10–11 (Final Milk Phase)**\n"
                            "Reduce milk to 4 kg/day; increase concentrates to 1.00 kg/day.\n\n"
                            "**Step 6: Weeks 12–16 (Complete Milk Withdrawal)**\n"
                            "Stop milk completely; feed 1.5–2.00 kg/day concentrates + forage & water ad libitum.\n\n"
                            "**Precautions:** Never change feed abruptly; ensure clean drinking water is continuously available for microbial fermentation."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Quantitative Milk Consumption Calculations",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Worked Example: Milk Budget for 4 Calves (Early Weaning)",
                    "content": {
                        "text": (
                            "**Scenario:** Calculate whole milk required for 4 calves on early weaning from Week 2 to Week 11.\n\n"
                            "**Calculations per calf:**\n"
                            "- Weeks 2–3 (14 days @ 5 kg/day) = 70 kg\n"
                            "- Weeks 4–7 (28 days @ 6 kg/day) = 168 kg\n"
                            "- Weeks 8–9 (14 days @ 5 kg/day) = 70 kg\n"
                            "- Weeks 10–11 (14 days @ 4 kg/day) = 56 kg\n"
                            "Total Milk per Calf = 70 + 168 + 70 + 56 = 364 kg.\n\n"
                            "**Total Herd Requirement (4 Calves):**\n"
                            "364 kg × 4 = 1,456 kg (approx 1,456 Liters of whole milk)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Quantitative Concentrate Feed Calculations",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Worked Example: Concentrate Budget for 3 Calves",
                    "content": {
                        "text": (
                            "**Scenario:** Calculate early-weaning concentrates required for 3 calves from Week 4 to Week 11.\n\n"
                            "**Calculations per calf:**\n"
                            "- Weeks 4–5 (14 days @ 0.25 kg/day) = 3.5 kg\n"
                            "- Weeks 6–7 (14 days @ 0.50 kg/day) = 7.0 kg\n"
                            "- Weeks 8–9 (14 days @ 0.75 kg/day) = 10.5 kg\n"
                            "- Weeks 10–11 (14 days @ 1.00 kg/day) = 14.0 kg\n"
                            "Total per Calf = 3.5 + 7.0 + 10.5 + 14.0 = 35.0 kg.\n\n"
                            "**Total Herd Requirement (3 Calves):**\n"
                            "35.0 kg × 3 = 105.0 kg (buy two 50-kg bags + one 5-kg bag)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Learning: Weaning System Selection",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Weaning Strategy Choice Exercise",
                    "content": {
                        "text": "Whole milk prices are very high on your dairy farm, but you have access to cheap skim milk from a creamery. Which weaning system maximizes profit?",
                        "options": [
                            "A: Early weaning using double concentrates.",
                            "B: Late weaning system replacing whole milk with cheap skim milk from week 4.",
                            "C: Natural direct suckling.",
                            "D: Whole milk ad libitum to week 16."
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Late weaning allows substituting whole milk with cheap skim milk from week 4 to week 16, freeing 100% of valuable whole milk for sale."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Precautionary Rules & Rumen Health",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Preventing 'Hay Belly' & Rumen Stagnation",
                    "content": {
                        "text": (
                            "- **Preventing Hay Belly:** Feeding coarse, poor-quality mature straw to young calves clogs the undeveloped stomach, causing abdominal distension ('hay belly') without nutrition. Feed soft, wilted legumes (lucerne).\n"
                            "- **Water Dependency:** Rumen microbes require an aqueous environment for concentrate fermentation; clean drinking water must be available continuous ad libitum."
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
                    "title": "Naivasha Commercial Dairy Case Study",
                    "content": {
                        "text": (
                            "**Scenario:** A Naivasha commercial farm adopted Early Weaning. By introducing starter pellets at week 4 "
                            "and reducing milk gradually from week 8, they successfully weaned calves by day 70 (week 10), saving over 300 liters of whole milk per calf for market sale."
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
                    "title": "Weaning Core Recall",
                    "content": {
                        "text": "1. At what week is early weaning completed?\n2. What milk type replaces whole milk in late weaning?\n3. What chemical products of concentrate fermentation stimulate rumen papillae?",
                        "options": [
                            "A: Week 10; Skim milk; Volatile fatty acids (butyrate/propionate).",
                            "B: Week 4; Colostrum; Lactic acid.",
                            "C: Week 20; Whey; Hydrochloric acid.",
                            "D: Week 2; Water; Glucose."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Early weaning completes at week 10; late weaning substitutes skim milk; VFAs (butyrate/propionate) stimulate papillae growth."
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
                    "title": "KCSE Model Essay: Early vs Late Weaning Program Comparison",
                    "content": {
                        "text": (
                            "**Question:** Differentiate between early weaning and late weaning programs in calf management. (6 Marks)\n\n"
                            "**Model Answer:**\n"
                            "- **Early Weaning:** Whole milk is fed up to week 8 and gradually reduced to complete weaning at week 10; high-protein calf pellets are introduced early to accelerate rumen papillae development.\n"
                            "- **Late Weaning:** Whole milk is fed for 3 weeks, then gradually substituted with skim milk from week 4 up to week 14, with complete weaning occurring at week 16."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 3 DATA: Replacement Stock and Calf Housing (10 Pages)
# =============================================================================

LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Replacement Stock and Calf Housing",
    "lesson_title": "Replacement Stock and Calf Housing",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Management of Replacement Stock",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define replacement stock and outline their vaccination/deworming schedule.\n"
                            "- Detail physiological operations: disbudding, castration, supernumerary teat clipping.\n"
                            "- Explain 7 structural requirements of calf housing.\n"
                            "- Compare permanent slatted-floor pens vs mobile pasture pens.\n"
                            "- Explain why calves under 3 weeks must be housed singly to prevent trichobezoars."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Vaccination & Health Timeline",
                    "content": {
                        "text": (
                            "Replacement stock are selected heifers and bulls kept to replace old, low-yielding cows. "
                            "Health management requires routine spraying against ticks (ECF vectors) and deworming. "
                            "Vaccination timeline: Blackquarter at 4 months, Anthrax & Blackquarter at 6 months, and Brucellosis (heifers) at 3–8 months to prevent contagious abortion."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Physiological Surgical Operations",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Disbudding, Castration & Teat Clipping",
                    "content": {
                        "text": (
                            "- **Disbudding/Dehorning:** Removal of horn buds using hot iron or chemical paste to prevent herd injury.\n"
                            "- **Castration:** Performed on non-breeding males (burdizzo/elastrator) to improve docility and beef fat cover.\n"
                            "- **Supernumerary Teats:** Extra teats clipped off early with teat clippers to prevent interference with milking machinery."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Seven Structural Requirements of Calf Housing",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Calf Housing Parameters",
                    "content": {
                        "text": (
                            "1. **Dryness & Warmth:** Prevents hypothermia and bacterial scours.\n"
                            "2. **Cleanliness:** Raised slatted floors for scrubbing.\n"
                            "3. **Space:** Adequate floor room for exercise.\n"
                            "4. **Proper Lighting:** Direct sunlight for Vitamin D synthesis (prevents rickets).\n"
                            "5. **Draught-Free Ventilation:** High windows remove ammonia while blocking direct cold wind.\n"
                            "6. **Proper Drainage:** Slanted concrete floors carry off liquid waste immediately.\n"
                            "7. **Single Housing (up to 3 wks):** Prevents hairball stomach blockages."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Single Housing Rationale & Trichobezoars",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Pathology of Indigestible Hairballs (Trichobezoars)",
                    "content": {
                        "text": (
                            "Calves under 3 weeks old have a strong natural suckling urge. If housed in groups, they suckle and lick each other's coats. "
                            "Swallowed hair accumulates in the abomasum as indigestible hairballs (trichobezoars), causing fatal digestive blockages. "
                            "Single housing up to week 3 completely eliminates this risk."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Permanent vs Mobile Calf Pen Comparison",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Comparison of Permanent vs Mobile Calf Pens",
                    "content": {
                        "text": (
                            "| Feature | Permanent Calf Pen | Mobile / Movable Calf Pen |\n"
                            "|---|---|---|\n"
                            "| Floor Type | Raised solid wooden slatted floor | Open floor on pasture ground |\n"
                            "| Location | Fixed near milking parlor | Moved regularly on pasture |\n"
                            "| Feeding | Feed/water brought to pen | Calf nibbles fresh pasture directly |\n"
                            "| Soiling Risk | Manual daily washing required | Moved daily to clean site |\n"
                            "| Climate Suitability | Cold, wet regions (Limuru) | Drier pasture regions (Nakuru) |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Architectural Diagram: Permanent Calf Pen",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Standard Slatted-Floor Permanent Calf Pen",
                    "content": {
                        "text": "Diagram showing 30cm raised wooden slatted floor, slanted concrete drainage base, high draught-free window, and direct sunlight path.",
                        "svg": SVG_CALF_PEN
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Step-by-Step Procedure: Pen Sanitation Check",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: Calf Pen Sanitation Check",
                    "content": {
                        "text": (
                            "**Purpose:** To audit calf housing against health parameters.\n\n"
                            "**Step 1: Check Floor Moisture**\n"
                            "Inspect slatted floor; verify it is completely dry to prevent hypothermia.\n\n"
                            "**Step 2: Evaluate Drainage Slant**\n"
                            "Pour water on empty concrete base; verify it flows immediately into the outer drain.\n\n"
                            "**Step 3: Inspect Sunlight Entry**\n"
                            "Verify direct sunlight reaches the interior for Vitamin D synthesis.\n\n"
                            "**Step 4: Test Draught-Free Ventilation**\n"
                            "Stand at calf resting height; verify air circulates without direct cold draughts.\n\n"
                            "**Step 5: Verify Housing Isolation**\n"
                            "Ensure all calves under 3 weeks are in single pens to prevent trichobezoars."
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
                    "title": "Limuru Cold Region Housing Case Study",
                    "content": {
                        "text": (
                            "**Scenario:** A Limuru farm experienced calf pneumonia outbreaks in ground-level concrete pens. "
                            "They retrofitted permanent pens with 30cm raised wooden slatted floors and high un-draughted windows, "
                            "eliminating dampness and reducing pneumonia mortality to zero."
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
                    "title": "Replacement Stock Core Recall",
                    "content": {
                        "text": "1. At what age is Brucellosis vaccine given to heifers?\n2. Why must calves under 3 weeks be housed singly?\n3. Why is sunlight required in calf pens?",
                        "options": [
                            "A: 3-8 months; Prevent licking/hairballs (trichobezoars); Vitamin D synthesis.",
                            "B: 12 months; Prevent mastitis; Heat source.",
                            "C: Day 1; Stop scours; Kills flies.",
                            "D: 2 years; Increase milk yield; Hardens horns."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Brucellosis vaccine is given at 3-8 months; single housing stops hairball formation; sunlight synthesizes Vitamin D."
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
                    "title": "KCSE Model Question: Calf Pen Structural Requirements",
                    "content": {
                        "text": (
                            "**Question:** State four structural requirements of a good calf pen and give a reason for each. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Raised Slatted Floor:** Keeps bedding completely dry to prevent hypothermia and scours.\n"
                            "2. **Slanted Base Drainage:** Directs urine and wash water into outer drains immediately.\n"
                            "3. **Proper Lighting/Sunlight:** Provides sunlight for Vitamin D synthesis to prevent rickets.\n"
                            "4. **Draught-Free Ventilation:** High windows remove toxic ammonia while blocking direct cold winds that cause pneumonia."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 4 DATA: Milk Composition, Secretion, Let-Down and Udder Structure (10 Pages)
# =============================================================================

LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Milk Composition, Secretion, Let-Down and Udder Structure",
    "lesson_title": "Milk Composition, Secretion, Let-Down and Udder Structure",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Milk Composition & Nutritional Factors",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 4 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- List components of bovine milk and factors affecting composition.\n"
                            "- Detail udder anatomical hierarchy from alveoli to teat canal.\n"
                            "- Explain Prolactin (lactogenesis) vs Oxytocin (let-down) hormonal systems.\n"
                            "- Apply the 8-Minute Golden Rule of oxytocin during milking.\n"
                            "- Identify stimuli triggers vs adrenaline inhibitors of milk let-down."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Milk Composition & Yield Variables",
                    "content": {
                        "text": (
                            "Milk is an emulsion of water, butterfat, proteins (casein, whey), lactose, and minerals. "
                            "Composition is influenced by: cow age, breed (Jersey higher fat than Friesian), stage of lactation, "
                            "completeness of milking (strippings have highest fat), diet (roughage increases fat), and mastitis disease."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Anatomical Hierarchy of the Udder",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Udder Secretory Structures",
                    "content": {
                        "text": (
                            "- **Alveolus Cells:** Microscopic spherical cells synthesizing milk from blood nutrients.\n"
                            "- **Lobules & Lobes:** Groups of alveoli drained by lactiferous ducts.\n"
                            "- **Gland Cistern:** Upper spacious chamber storing milk from ducts.\n"
                            "- **Teat Cistern & Teat Canal:** Lower cavity and output canal closed by sphincter muscle."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Endocrine Systems: Prolactin vs Oxytocin",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Lactogenesis vs Milk Let-Down Reflex",
                    "content": {
                        "text": (
                            "- **Prolactin (Lactogenesis):** Secreted by pituitary gland to drive continuous milk synthesis in alveoli cells.\n"
                            "- **Oxytocin (Milk Let-Down):** Secreted by posterior pituitary in response to milking stimuli. Travels via blood to contract myoepithelial cells around alveoli, squeezing milk into cisterns."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The 8-Minute Golden Rule of Oxytocin",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Oxytocin Half-Life & Milking Speed",
                    "content": {
                        "text": (
                            "Oxytocin has an active bloodstream half-life of only 7 to 10 minutes. "
                            "Milking must be completed rapidly within 8 minutes. If delayed beyond 8 minutes, oxytocin breaks down, "
                            "myoepithelial cells relax, and remaining high-fat milk is trapped in upper alveoli, causing yield loss and mastitis."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Triggers vs Adrenaline Inhibitors",
            "blocks": [
                {
                    "block_type": "table_block",
                    "component_type": "table_block",
                    "title": "Factors Influencing Milk Let-Down vs Inhibition",
                    "content": {
                        "text": (
                            "| Stimuli (Triggers Oxytocin Let-Down) | Inhibitors (Triggers Adrenaline Block) |\n"
                            "|---|---|\n"
                            "| Warm udder wash / massage | Physical pain / beating animal |\n"
                            "| Calf presence / suckling | Barking dogs / strangers in parlor |\n"
                            "| Sight of feed / rattling buckets | Rough milking technique / teat injury |\n"
                            "| Presence of familiar milkman | Loud sudden noises / fear |"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Anatomical Flowchart Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Anatomical Pathway of Milk Secretion & Udder Structure",
                    "content": {
                        "text": "Flowchart diagram showing milk pathway from alveolus cells to gland cistern and teat canal under oxytocin reflex.",
                        "svg": SVG_UDDER_PATHWAY
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Learning: Let-Down Reflex Sequence",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Milk Let-Down Endocrine Sequence",
                    "content": {
                        "text": "Order the steps of milk let-down:\n1. Sensory nerve signal to brain\n2. Warm udder wash stimulus\n3. Myoepithelial cells contract\n4. Oxytocin secreted into bloodstream\n5. Milk forced into cisterns",
                        "options": [
                            "A: 2 -> 1 -> 4 -> 3 -> 5",
                            "B: 1 -> 2 -> 3 -> 4 -> 5",
                            "C: 4 -> 3 -> 2 -> 1 -> 5",
                            "D: 5 -> 4 -> 3 -> 2 -> 1"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Correct order: Warm wash stimulus (2), nerve signal (1), oxytocin release (4), myoepithelial contraction (3), milk forced to cisterns (5)."
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
                    "title": "Kiambu Adrenaline Inhibition Case Study",
                    "content": {
                        "text": (
                            "**Scenario:** A stranger with a barking dog entered a Kiambu milking parlor. The cow panicked and withheld her milk.\n\n"
                            "**Pathophysiology:** Fear triggered adrenaline release, which constricted blood vessels, physically blocking oxytocin from reaching udder cells. "
                            "Result: Poor milk yield and trapped high-fat strippings."
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
                    "title": "Milk Physiology Recall",
                    "content": {
                        "text": "1. Which hormone stimulates milk synthesis (lactogenesis)?\n2. How long does oxytocin remain active in the bloodstream?\n3. Which hormone inhibits oxytocin during stress?",
                        "options": [
                            "A: Prolactin; 7-10 minutes; Adrenaline.",
                            "B: Oxytocin; 24 hours; Insulin.",
                            "C: Estrogen; 1 hour; Progesterone.",
                            "D: Thyroxine; 5 minutes; Cortisol."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Prolactin synthesizes milk; oxytocin lasts 7-10 mins; adrenaline inhibits let-down."
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
                    "title": "KCSE Model Essay: Factors Affecting Milk Composition (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Outline five factors that affect the composition of milk produced by a dairy herd. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Breed:** Jersey milk has higher butterfat than Friesian milk.\n"
                            "2. **Age:** Butterfat and protein percentages decline as cows age.\n"
                            "3. **Completeness of Milking:** Strippings (last milk) have much higher butterfat than foremilk.\n"
                            "4. **Diet:** High roughage feeds raise butterfat; high concentrates lower fat.\n"
                            "5. **Disease (Mastitis):** Alters composition, lowering lactose/casein while raising sodium/chloride."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 5 DATA: Clean Milk Production, Milking and Dry-Cow Therapy (10 Pages)
# =============================================================================

LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Clean Milk Production, Milking and Dry-Cow Therapy",
    "lesson_title": "Clean Milk Production, Milking and Dry-Cow Therapy",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Principles of Clean Milk Production",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 5 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- State 5 essential factors for clean milk production.\n"
                            "- Explain strip cup testing for early mastitis detection.\n"
                            "- Detail the protocol for dry-cow therapy.\n"
                            "- Execute the 10-step clean milking protocol.\n"
                            "- Identify biosecurity errors in parlor sanitation."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Five Factors of Clean Milk Production",
                    "content": {
                        "text": (
                            "Milk is sterile inside a healthy udder but highly perishable upon harvest. Clean milk production requires:\n"
                            "1. Healthy lactating cow (screened for TB & Brucellosis).\n"
                            "2. Healthy, clean milker (short nails, washed hands).\n"
                            "3. Clean concrete milking parlor (dust-free).\n"
                            "4. Clean disinfected seamless equipment.\n"
                            "5. Immediate cooling and filtration."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Mastitis Pathology & Strip Cup Diagnostics",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Foremilk Testing with Strip Cup",
                    "content": {
                        "text": (
                            "Foremilk (first 2-3 squirts) contains high bacterial counts. Squirting foremilk onto the black mesh of a strip cup "
                            "inspects for white clots, flakes, or blood — early clinical signs of mastitis. Infected foremilk is discarded safely."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Dry-Cow Therapy Protocol",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Dry Period Antibiotic Infusion",
                    "content": {
                        "text": (
                            "At the end of a 305-day lactation, a cow enters a 60-day dry period before calving. "
                            "During the last milking, long-acting antibiotics are infused into each teat canal (dry-cow therapy). "
                            "This creates a chemical barrier curing subclinical mastitis and protecting the non-lactating udder."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Step-by-Step Procedure: The Clean Milking Protocol",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "Step-by-Step Procedure: The Clean Milking Protocol",
                    "content": {
                        "text": (
                            "**Purpose:** To harvest clean milk and prevent mastitis.\n\n"
                            "**Step 1: Pre-Milking Relaxation (15-20 mins prior)**\n"
                            "Bring cows near parlor to rest and stimulate let-down.\n\n"
                            "**Step 2: Equipment Preparation**\n"
                            "Assemble clean buckets, salve, strip cup, and individual towels.\n\n"
                            "**Step 3: Restrain & Feed**\n"
                            "Tie legs gently and place concentrate feed in trough.\n\n"
                            "**Step 4: Wash Udder**\n"
                            "Wash udder with warm disinfected water to trigger oxytocin.\n\n"
                            "**Step 5: Dry Udder**\n"
                            "Wipe udder dry with a clean, individual towel.\n\n"
                            "**Step 6: Strip Cup Test**\n"
                            "Squirt foremilk onto black mesh screen to check for clots.\n\n"
                            "**Step 7: Apply Salve**\n"
                            "Rub petroleum salve on teats to prevent friction cracks.\n\n"
                            "**Step 8: Full-Hand Milking**\n"
                            "Milk hindquarters first using full-hand squeeze (within 8 mins).\n\n"
                            "**Step 9: Complete Stripping**\n"
                            "Drain last high-fat milk completely.\n\n"
                            "**Step 10: Record & Release**\n"
                            "Weigh milk, record data, and sanitize stall."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Visual Guide: Clean Milking Parlor",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Sanitary Commercial Milking Parlor Operation",
                    "content": {
                        "text": "Clean milking parlor showing washed cows, concrete floors, stainless steel buckets, and hygienic handlers.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Milking_parlor_clean.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY 3.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Milking_parlor_clean.jpg"
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Learning: Spot the Error",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Biosecurity Error Spotting",
                    "content": {
                        "text": "A milker washes 5 cows using warm water and a single cotton towel for all 5 udders. What is the critical error?",
                        "options": [
                            "A: Washing before feeding.",
                            "B: Using a single towel across multiple cows, spreading contagious mastitis pathogens.",
                            "C: Using warm water.",
                            "D: Milking within 8 minutes."
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Sharing a single wash towel rubs mastitis bacteria from infected cows onto healthy teats. Each cow requires a clean, individual towel."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Full-Hand Milking vs Teat Pulling",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Preventing Teat Canal Injury",
                    "content": {
                        "text": (
                            "Full-hand milking squeezes the teat from top to bottom, mimicking calf suckling without friction. "
                            "Pulling teats with fingers (stripping throughout) causes severe friction injuries, teat canal swelling, "
                            "and mastitis infections."
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
                    "title": "Githunguri Mastitis Isolation Case Study",
                    "content": {
                        "text": (
                            "**Scenario:** A milker detected white clots in the left rear quarter using a strip cup.\n\n"
                            "**Action:** Milked the infected quarter last, discarded its milk safely, and isolated the cow for veterinary treatment while saving clean milk from the other three quarters."
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
                    "title": "Milking Hygiene Recall",
                    "content": {
                        "text": "1. What tool tests foremilk for mastitis clots?\n2. What is dry-cow therapy?\n3. Why is full-hand milking preferred over teat pulling?",
                        "options": [
                            "A: Strip cup; Teat antibiotic infusion at drying off; Prevents teat friction injury.",
                            "B: Thermometer; Washing cows; Increases fat.",
                            "C: Lactometer; Feeding grain; Faster let-down.",
                            "D: Filter cloth; Deworming; Cleans milk."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Strip cup detects mastitis clots; dry-cow therapy infuses antibiotics at drying off; full-hand milking prevents teat injury."
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
                    "title": "KCSE Model Essay: Clean Milk Production Requirements (10 Marks)",
                    "content": {
                        "text": (
                            "**Question:** State five factors essential for clean milk production and explain the importance of each. (10 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Healthy Cow:** Free from TB and Brucellosis to prevent zoonotic disease transfer.\n"
                            "2. **Clean Milker:** Short nails, washed hands to prevent bacterial contamination.\n"
                            "3. **Clean Parlor:** Concrete dust-free floors to keep air clean during milking.\n"
                            "4. **Sanitized Equipment:** Hot detergent washing kills thermoduric bacteria.\n"
                            "5. **Fast Cooling:** Immediate chilling stops post-harvest bacterial multiplication."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 6 DATA: Milk and Beef Products and Marketing (8 Pages)
# =============================================================================

LESSON_6_DATA = {
    "unit_order": 6,
    "unit_name": "Milk and Beef Products and Marketing",
    "lesson_title": "Milk and Beef Products and Marketing",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Processing & Value Addition",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 6 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define dairy products: pasteurized milk, UHT milk, butter, ghee, cheese, skim milk.\n"
                            "- Detail slaughter age (1.5-2 yrs) and dressing standards for beef cattle.\n"
                            "- Identify Kenyan dairy & beef marketing institutions (KDB, KMC, LMD, Cooperatives, Brookside).\n"
                            "- Solve KCSE essays on dairy cooperative functions."
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Value Addition & Shelf-Life Extension",
                    "content": {
                        "text": (
                            "Raw milk and live cattle are perishable. Value addition converts raw produce into stable commodities:\n"
                            "- **Pasteurized Milk:** Heated and cooled quickly to kill pathogens.\n"
                            "- **UHT Milk:** Heated to 130°C–135°C, sterile-packed for months of room-temp storage.\n"
                            "- **Butter & Ghee:** Butter made by churning cream; Ghee made by heating butter to evaporate water.\n"
                            "- **Cheese:** Coagulated casein protein and whey separation."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Product Value-Chain Mapping",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Dairy and Beef Processing Value-Chain Mapping",
                    "content": {
                        "text": "Diagram mapping raw milk outputs to butter, ghee, UHT milk, cheese, and skim milk alongside Kenyan marketing channels.",
                        "svg": SVG_VALUE_CHAIN
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Dairy Marketing Channels & Institutions",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Kenyan Dairy Regulatory & Processing Bodies",
                    "content": {
                        "text": (
                            "- **Kenya Dairy Board (KDB):** Statutory regulatory body governing production, quality, and sales.\n"
                            "- **Dairy Cooperatives:** Farmer-owned societies collecting, chilling, and transporting bulk milk.\n"
                            "- **Major Processors:** KCC (Kenya Cooperative Creameries), Brookside Dairies, Tuzo, Delamere, Limuru Dairies."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Beef Marketing Channels & Institutions",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Pastoralist Transport & Meat Processing",
                    "content": {
                        "text": (
                            "- **Livestock Marketing Division (LMD):** Facilitates cattle purchasing and transport from pastoralist rangelands to feedlots.\n"
                            "- **Kenya Meat Commission (KMC):** State-owned statutory body operating abattoirs, canning beef, and supplying institutions.\n"
                            "- **Farmer's Choice:** Private processor producing value-added meats for retail markets."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Interactive Learning: Institutional Matching",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Marketing Institution Matching",
                    "content": {
                        "text": "Match the organization to its primary function:\n1. Kenya Dairy Board (KDB)\n2. Kenya Meat Commission (KMC)\n3. Livestock Marketing Division (LMD)",
                        "options": [
                            "A: 1->Dairy Regulator; 2->State Abattoir & Canning; 3->Pastoral Cattle Transport.",
                            "B: 1->Feed Manufacturer; 2->Vaccine Producer; 3->Artificial Insemination.",
                            "C: 1->Tractor Hire; 2->Soil Testing; 3->Water Rights.",
                            "D: 1->Fertilizer Import; 2->Grain Silos; 3->Forestry."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "KDB regulates dairy quality; KMC operates state abattoirs and meat canning; LMD transports pastoralist cattle."
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
                    "title": "Garissa Pastoralist to Nairobi Supply Chain",
                    "content": {
                        "text": (
                            "**Scenario:** A pastoralist in Garissa sells steers to LMD during drought. "
                            "LMD transports cattle to Nakuru feedlots for fattening to 1.5–2 years of age, then sells to KMC or Farmer's Choice for dressed retail packaging."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Module Summary & Knowledge Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Marketing & Processing Recall",
                    "content": {
                        "text": "1. What processing temperature defines UHT milk?\n2. How is butter converted into ghee?\n3. What statutory board regulates dairy quality in Kenya?",
                        "options": [
                            "A: 130°C–135°C; Heating butter to evaporate water; Kenya Dairy Board (KDB).",
                            "B: 60°C; Adding sugar; KCC.",
                            "C: 100°C; Freezing cream; LMD.",
                            "D: 200°C; Churning whey; KMC."
                        ],
                        "correct_answer_index": 0,
                        "explanation": "UHT is heated to 130-135°C; ghee is pure fat from heating butter; KDB regulates dairy quality."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Functions of Dairy Cooperatives (7 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Describe the functions of agricultural cooperative societies in dairy marketing in Kenya. (7 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Collection & Assembling:** Assembling milk at local hubs.\n"
                            "2. **Chilling & Processing:** Bulk cooling to prevent spoilage.\n"
                            "3. **Bulk Transport:** Transporting milk in insulated tankers to urban plants.\n"
                            "4. **Price Bargaining:** Negotiating fair bulk prices for members.\n"
                            "5. **Input & Credit Supply:** Supplying feeds and veterinary medicines on credit.\n"
                            "6. **Extension Training:** Training farmers on clean milking techniques.\n"
                            "7. **Bonus Payouts:** Distributing annual financial bonuses to member farmers."
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
    LESSON_5_DATA,
    LESSON_6_DATA
]
