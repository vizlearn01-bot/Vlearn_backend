import os
import sys
import django
import uuid

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_qa_refactor():
    try:
        topic = Topic.objects.get(id=16)
    except Topic.DoesNotExist:
        print("Topic 16 (Topic 5: Metals) not found!")
        return

    print(f"Starting QA audit and direct refactoring for Topic: {topic.name} (ID: {topic.id})")

    # Complete refactoring data dictionary for all 13 lessons in Topic 5: Metals
    topic_data = {
        103: {
            "title": "Chief Ores of Metals",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Chief Ores of Metals",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand what metal ores are, why most metals occur as chemical compounds in rocks, how chief ores are selected for industrial extraction, and the formulas of the 6 key metal ores."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Metals in Nature & The Concept of Ores",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Every day we use metals in thousands of ways—from copper wiring and aluminium food foil to iron and steel support beams. However, if you dig up soil in your school compound, you will not find shiny, pure metals.\n\nBecause most metals are chemically reactive, they bond with electronegative non-metals like oxygen, sulfur, or chlorine over geological time. Only unreactive metals like gold and platinum occur uncombined as free elements in nature.\n\nTo master metallurgy (the science of extracting metals), we define four core terms:\n* **Mineral**: A naturally occurring solid chemical compound of a metal found in the Earth's crust.\n* **Gangue**: Worthless rocky, sandy, or earthy impurities (such as silica, $\\text{SiO}_2$) mixed with minerals in rocks.\n* **Ore**: A mineral deposit from which a metal can be extracted commercially and profitably. If extracting the metal costs more than its market value, the mineral is not an ore.\n* **Chief Ore**: The most abundant, practical, and economically viable mineral source used industrially to extract a specific metal."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Chief Ores of Six Key Metals",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In secondary school Chemistry, you must know the chemical name, formula, and chief ore for six key metals:\n\n1. **Sodium ($\\text{Na}$)**:\n   - *Chief Ore*: Rock salt / Halite (Chemical formula: $\\text{NaCl}$)\n2. **Aluminium ($\\text{Al}$)**:\n   - *Chief Ore*: Bauxite (Chemical formula: hydrated aluminium oxide, $\\text{Al}_2\\text{O}_3 \\cdot 2\\text{H}_2\\text{O}$)\n3. **Iron ($\\text{Fe}$)**:\n   - *Chief Ore*: Haematite (Chemical formula: $\\text{Fe}_2\\text{O}_3$). Other ores include Magnetite ($\\text{Fe}_3\\text{O}_4$) and Siderite ($\\text{FeCO}_3$).\n4. **Zinc ($\\text{Zn}$)**:\n   - *Chief Ore*: Zinc Blende (Chemical formula: zinc sulfide, $\\text{ZnS}$). Another major ore is Calamine ($\\text{ZnCO}_3$).\n5. **Lead ($\\text{Pb}$)**:\n   - *Chief Ore*: Galena (Chemical formula: lead(II) sulfide, $\\text{PbS}$).\n6. **Copper ($\\text{Cu}$)**:\n   - *Chief Ore*: Copper Pyrites (Chemical formula: $\\text{CuFeS}_2$). Other ores include Malachite ($\\text{CuCO}_3 \\cdot \\text{Cu(OH)}_2$) and Cuprite ($\\text{Cu}_2\\text{O}$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Visualizing Chief Metal Ores",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Show visual samples of Bauxite, Haematite, Galena, and Copper Pyrites rock ores with labeled chemical formulas and physical appearances.",
                        "caption": "Comparison of major chief metal ores: Bauxite (reddish-brown clayish rock), Haematite (dark metallic red-black ore), Galena (shiny cubic gray mineral), and Copper Pyrites (brassy golden-yellow sulfide ore)."
                    },
                    "asset_info": {
                        "title": "Chief Ores Visual Guide",
                        "description": "Visual comparison chart showing hand samples of Bauxite (Al2O3.2H2O), Haematite (Fe2O3), Galena (PbS), and Copper Pyrites (CuFeS2) with chemical labels.",
                        "ai_instruction": "Create an instructional diagram showing high-resolution mineral specimens of Bauxite, Haematite, Galena, and Copper Pyrites. Clearly label each with its common name, chemical formula, and the metal extracted."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Understanding Check: Ore Economic Viability",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is Bauxite ($\\text{Al}_2\\text{O}_3 \\cdot 2\\text{H}_2\\text{O}$) classified as the chief ore of aluminium rather than ordinary clay minerals that also contain aluminium atoms?",
                        "options": [
                            "Bauxite is the only naturally occurring mineral on Earth that contains aluminium atoms.",
                            "Bauxite contains a high percentage of aluminium and allows commercial extraction at a profitable industrial scale.",
                            "Bauxite contains pure uncombined aluminium metal that does not require chemical reduction.",
                            "Bauxite naturally melts at room temperature without requiring electrical energy."
                        ],
                        "answer": "B",
                        "explanation": "An ore is not defined simply by containing an element, but by economic viability. While clay contains aluminium, extracting Al from clay is extremely difficult and financially unfeasible. Bauxite is the chief ore because it has a high metal concentration and can be purified and electrolyzed profitably on an industrial scale."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Elemental Composition of Ores",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A geology student analyzes a sample of Copper Pyrites ($\\text{CuFeS}_2$). Which of the following correctly identifies all the chemical elements present in this chief ore?",
                        "options": [
                            "Copper, Hydrogen, and Oxygen",
                            "Copper, Chlorine, and Silicon",
                            "Copper, Iron, and Sulfur",
                            "Copper, Zinc, and Lead"
                        ],
                        "answer": "C",
                        "explanation": "The chemical formula of Copper Pyrites is $\\text{CuFeS}_2$. Breaking down the chemical symbols: Cu = Copper, Fe = Iron, S = Sulfur. Therefore, Copper Pyrites is a mixed sulfide ore composed of copper, iron, and sulfur."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Chief Ores of Metals\n- **Ores vs Minerals**: All ores are minerals, but only minerals that permit commercial, profitable metal extraction are called ores.\n- **Gangue**: The unwanted sandy and rocky impurities mixed with minerals in the Earth's crust.\n- **Core Chemical Formulas to Remember**:\n  - Sodium: Rock Salt ($\\text{NaCl}$)\n  - Aluminium: Bauxite ($\\text{Al}_2\\text{O}_3 \\cdot 2\\text{H}_2\\text{O}$)\n  - Iron: Haematite ($\\text{Fe}_2\\text{O}_3$)\n  - Zinc: Zinc Blende ($\\text{ZnS}$)\n  - Lead: Galena ($\\text{PbS}$)\n  - Copper: Copper Pyrites ($\\text{CuFeS}_2$)"
                    }
                }
            ]
        },

        104: {
            "title": "General Methods of Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: General Methods of Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand how metal ores are concentrated by physical methods (such as Froth Flotation) and how a metal's position in the Reactivity Series dictates whether it is extracted by electrolysis, carbon reduction, or simple heating."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Stage 1: Ore Concentration & Gangue Removal",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Mining companies dig up raw ore as large boulders mixed with earthy gangue (clay, sand, silica). Before performing expensive chemical reduction reactions, the ore must be concentrated physically:\n\n1. **Hydraulic Washing**: Heavy metallic ore grains sink while running water washes away lighter earthy gangue.\n2. **Magnetic Separation**: Magnetic ores (such as Magnetite, $\\text{Fe}_3\\text{O}_4$) are separated from non-magnetic rocky waste using magnetic conveyor belts.\n3. **Froth Flotation (The Standard for Sulfide Ores)**:\n   - Used for sulfide ores like Zinc Blende ($\\text{ZnS}$), Galena ($\\text{PbS}$), and Copper Pyrites ($\\text{CuFeS}_2$).\n   - Ore is crushed into fine powder and mixed with water and pine oil in a large tank.\n   - Compressed air is vigorously blown through the slurry.\n   - Sulfide ore particles are **hydrophobic** (water-repelling) and cling to the pine oil bubbles, floating to the surface as a thick froth which is skimmed off.\n   - The earthy gangue is **hydrophilic** (water-attracting), gets wetted by water, and sinks to the bottom."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Diagram: Froth Flotation Process",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram of a Froth Flotation cell showing air inlet pipe, rotating agitator, oily froth layer at top carrying sulfide ore particles, and gangue sinking to the bottom.",
                        "caption": "Froth Flotation Cell: Air bubbles carry oil-coated hydrophobic sulfide ore to the surface froth, separating it from heavy gangue."
                    },
                    "asset_info": {
                        "title": "Froth Flotation Apparatus Diagram",
                        "description": "Schematic of industrial froth flotation tank highlighting air agitator, pine oil sulfide froth overflow, and gangue sediment outlet.",
                        "ai_instruction": "Illustrate a clean industrial cross-section of a froth flotation cell. Show compressed air creating bubbles, pine oil coated mineral particles rising to the top froth layer, and rocky gangue sinking."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Stage 2: Selecting the Chemical Reduction Method",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Chemical reduction converts positive metal ions in compounds into neutral metal atoms ($\\text{M}^{n+} + n e^- \\rightarrow \\text{M}$). The choice of reduction method depends strictly on the metal's position in the **Reactivity Series**:\n\n1. **High Reactivity Metals ($\\text{K}, \\text{Na}, \\text{Ca}, \\text{Mg}, \\text{Al}$)**:\n   - Form extremely stable compounds with very strong chemical bonds.\n   - Carbon is less reactive than these metals and cannot remove oxygen or chlorine from them.\n   - *Method*: **Electrolysis of molten salts** (requires powerful electrical energy).\n\n2. **Moderate Reactivity Metals ($\\text{Zn}, \\text{Fe}, \\text{Pb}$)**:\n   - Form moderately stable oxides.\n   - Carbon and Carbon Monoxide ($\\text{CO}$) are more reactive than these metals at high temperatures.\n   - *Method*: **Chemical reduction using Coke (Carbon) or Carbon Monoxide** in a furnace.\n\n3. **Low Reactivity Metals ($\\text{Cu}, \\text{Hg}, \\text{Ag}$)**:\n   - Form weak chemical bonds.\n   - *Method*: **Thermal decomposition / simple roasting in air** (e.g., heating copper sulfide directly)."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Understanding Check: Froth Flotation Mechanism",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is Froth Flotation specifically chosen to concentrate Copper Pyrites ($\\text{CuFeS}_2$) rather than hydraulic washing alone?",
                        "options": [
                            "Copper pyrites is magnetic and responds to electromagnetic fields.",
                            "Copper pyrites is a sulfide ore whose hydrophobic particles selectively adhere to pine oil air bubbles and float to the surface.",
                            "Pine oil chemically reacts with copper pyrites to produce pure copper metal in the flotation tank.",
                            "Copper pyrites dissolves completely in water, leaving rocky gangue behind as a solid."
                        ],
                        "answer": "B",
                        "explanation": "Froth flotation relies on differences in surface wettability. Sulfide ores like $\\text{CuFeS}_2$ are hydrophobic (water-repelling) and preferentially stick to pine oil droplets attached to rising air bubbles, forming a floatable froth. Earthy gangue is hydrophilic and sinks."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Method Selection via Reactivity",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why must Sodium ($\\text{Na}$) be extracted using electricity (electrolysis) of molten salt, whereas Iron ($\\text{Fe}$) is extracted by heating with Carbon in a blast furnace?",
                        "options": [
                            "Sodium is a liquid at room temperature and cannot be heated in a furnace.",
                            "Sodium is higher than Carbon in the reactivity series and forms extremely stable bonds, so Carbon cannot reduce its compounds.",
                            "Iron does not conduct electricity when molten, making electrolysis impossible for iron.",
                            "Electrolysis of iron would produce toxic chlorine gas, whereas sodium extraction produces oxygen."
                        ],
                        "answer": "B",
                        "explanation": "Sodium is near the top of the reactivity series, meaning it holds onto electrons and oxygen/chlorine much more strongly than carbon does. Carbon cannot displace or reduce sodium. Therefore, powerful electrical energy (electrolysis) is required. Iron is lower than carbon in reactivity, allowing carbon/CO to readily reduce iron oxides."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: General Extraction Methods\n- **Physical Cleaning**: Froth flotation concentrates sulfide ores ($\\text{ZnS}, \\text{PbS}, \\text{CuFeS}_2$) using pine oil and air bubbles.\n- **Reactivity Dictates Reduction**:\n  - Highly reactive ($\\text{Na}, \\text{Al}$): Electrolysis of molten salts.\n  - Moderately reactive ($\\text{Zn}, \\text{Fe}, \\text{Pb}$): Reduction with Carbon / Carbon Monoxide.\n  - Low reactivity ($\\text{Cu}$): Roasting / heating in air."
                    }
                }
            ]
        },

        105: {
            "title": "Sodium — Occurrence and Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Sodium Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand why sodium must be extracted by the Down's Cell electrolysis of molten $\\text{NaCl}$, the crucial role of $\\text{CaCl}_2$ flux, the anode and cathode half-equations, and how product recombination is prevented."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Why Aqueous NaCl Cannot Be Used",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Sodium is an alkali metal (Group 1) located near the top of the Reactivity Series. Its chief ore is Rock Salt ($\\text{NaCl}$).\n\nCan we extract sodium metal by electrolyzing an aqueous solution of sodium chloride (brine)? **NO!**\n\nIn aqueous $\\text{NaCl}$, water molecules dissociate into $\\text{H}^+$ and $\\text{OH}^-$ ions alongside $\\text{Na}^+$ and $\\text{Cl}^-$ ions:\n$$\\text{H}_2\\text{O}_{(l)} \\rightleftharpoons \\text{H}^+_{(aq)} + \\text{OH}^-_{(aq)}$$\nBecause $\\text{H}^+$ ions have a higher electrode potential than $\\text{Na}^+$ ions, $\\text{H}^+$ ions are **preferentially discharged** at the cathode to form Hydrogen gas:\n$$2\\text{H}^+_{(aq)} + 2e^- \\rightarrow \\text{H}_{2(g)}$$\nSodium ions remain in solution! To obtain pure sodium metal, we must eliminate water entirely and electrolyze **molten (fused) sodium chloride**, where $\\text{Na}^+$ is the only cation present."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Melting Point Obstacle & Calcium Chloride Flux",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Pure sodium chloride has an extremely high melting point of **$801^\\circ\\text{C}$**. Electrolyzing at $801^\\circ\\text{C}$ poses two major engineering problems:\n1. Consumes enormous electrical and thermal energy, making extraction expensive.\n2. Sodium metal boils at $883^\\circ\\text{C}$ and forms a dangerous sodium vapor fog at $801^\\circ\\text{C}$ that dissolves in the melt and shorts out the cell.\n\n**The Solution**: Calcium Chloride ($\\text{CaCl}_2$) is added as an impurity / flux to the electrolyte in a 2:3 ratio.\n\nThis impurity lowers the melting point of the salt mixture from **$801^\\circ\\text{C}$ down to about $600^\\circ\\text{C}$**! At $600^\\circ\\text{C}$, sodium remains a liquid metal without vaporizing, and energy costs are dramatically reduced."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "The Down's Cell Architecture & Half-Reactions",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "The industrial extraction takes place in a specialized vessel called the **Down's Cell**:\n* **Anode (Positive Electrode)**: A central cylindrical **carbon (graphite)** rod.\n* **Cathode (Negative Electrode)**: A ring-shaped **steel** electrode surrounding the anode.\n* **Iron Gauze Diaphragm**: Suspended between the anode and cathode to prevent explosive re-combination of liquid sodium and chlorine gas.\n\n**Electrode Reactions during Electrolysis**:\n1. **At the Cathode (Reduction)**:\n   $$\\text{Na}^+_{(l)} + e^- \\rightarrow \\text{Na}_{(l)}$$\n   *Macroscopic observation*: Silvery liquid sodium metal forms. Because liquid sodium is less dense than the molten salt mixture, it floats to the top and overflows into a collector pipe filled with dry oil to prevent oxidation by air.\n\n2. **At the Anode (Oxidation)**:\n   $$2\\text{Cl}^-_{(l)} \\rightarrow \\text{Cl}_{2(g)} + 2e^-$$\n   *Macroscopic observation*: Pale green chlorine gas bubbles off and is collected through an inverted iron hood at the top for use in manufacturing PVC and bleaching powder."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Down's Cell for Sodium Extraction",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Detailed cross-section diagram of the Down's Cell showing central graphite anode, surrounding cylindrical steel cathode, iron gauze diaphragm mesh, molten NaCl/CaCl2 electrolyte, top chlorine dome collector, and floating liquid sodium collector tube.",
                        "caption": "Down's Cell Cross-Section: Liquid sodium floats up the cathode collector while chlorine gas exits through the top anode hood. The cylindrical iron gauze prevents contact between products."
                    },
                    "asset_info": {
                        "title": "Down's Cell Technical Schematic",
                        "description": "Cross-sectional diagram of Down's Cell for molten NaCl electrolysis showing graphite anode, steel cathode, iron diaphragm, and product outlets.",
                        "ai_instruction": "Create a clear, labeled cross-sectional diagram of the Down's Cell. Label the graphite anode (+), steel cathode (-), central iron gauze diaphragm, molten salt electrolyte, liquid sodium outlet, and chlorine gas hood."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Aqueous vs Molten Electrolysis",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is sodium metal produced at the cathode during electrolysis of molten $\\text{NaCl}$, but hydrogen gas is produced when electrolyzing aqueous $\\text{NaCl}$ solution?",
                        "options": [
                            "Water neutralizes sodium ions, converting them into sodium hydroxide instantly.",
                            "In aqueous solution, $\\text{H}^+$ ions from water are preferentially discharged over $\\text{Na}^+$ ions because $\\text{H}^+$ is lower in the electrochemical series.",
                            "Sodium metal dissolves in water to form a gas at room temperature.",
                            "Graphite electrodes can only conduct electricity in molten environments."
                        ],
                        "answer": "B",
                        "explanation": "In aqueous solution, both $\\text{H}^+$ (from $\\text{H}_2\\text{O}$) and $\\text{Na}^+$ ions migrate to the cathode. $\\text{H}^+$ has a more positive electrode potential ($0.00\\text{ V}$) compared to $\\text{Na}^+$ ($-2.71\\text{ V}$), meaning $\\text{H}^+$ gains electrons much more readily, yielding $\\text{H}_{2(g)}$. Molten $\\text{NaCl}$ contains no water, forcing $\\text{Na}^+$ to be reduced."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Calcium Chloride Role in Down's Cell",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the primary industrial reason for adding calcium chloride ($\\text{CaCl}_2$) to sodium chloride ($\\text{NaCl}$) in the Down's Cell?",
                        "options": [
                            "To act as a catalyst that accelerates the rate of electron transfer at the carbon anode.",
                            "To lower the melting point of the salt mixture from $801^\\circ\\text{C}$ to $600^\\circ\\text{C}$, conserving energy and preventing sodium vaporization.",
                            "To prevent chlorine gas from reacting with the steel walls of the cell.",
                            "To increase the density of the electrolyte so liquid sodium sinks to the bottom."
                        ],
                        "answer": "B",
                        "explanation": "Adding $\\text{CaCl}_2$ forms an eutectic mixture that melts at $\\approx 600^\\circ\\text{C}$ instead of $801^\\circ\\text{C}$. This saves massive heating costs and keeps the operating temperature safely below the boiling point of sodium ($883^\\circ\\text{C}$), avoiding hazardous sodium vapor formation."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Sodium Extraction (Down's Process)\n- **Electrolyte**: Fused molten $\\text{NaCl} + \\text{CaCl}_2$ flux (lowers melting point from $801^\\circ\\text{C}$ to $600^\\circ\\text{C}$).\n- **Cathode (Steel)**: $\\text{Na}^+_{(l)} + e^- \\rightarrow \\text{Na}_{(l)}$ (silvery liquid metal floats and overflows).\n- **Anode (Graphite)**: $2\\text{Cl}^-_{(l)} \\rightarrow \\text{Cl}_{2(g)} + 2e^-$ (green gas collected at top hood).\n- **Iron Gauze Diaphragm**: Prevents explosive contact between $\\text{Na}_{(l)}$ and $\\text{Cl}_{2(g)}$."
                    }
                }
            ]
        },

        106: {
            "title": "Aluminium — Occurrence and Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Aluminium Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the two-stage industrial extraction of aluminium: Bayer Process (bauxite purification with hot conc. NaOH) and Hall-Héroult Process (electrolysis in molten cryolite)."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Stage 1: Bauxite Purification (The Bayer Process)",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Aluminium is the most abundant metal in the Earth's crust. Its chief ore is **Bauxite** ($\\text{Al}_2\\text{O}_3 \\cdot 2\\text{H}_2\\text{O}$), which contains iron(III) oxide ($\\text{Fe}_2\\text{O}_3$, giving it a reddish color) and silica ($\\text{SiO}_2$) impurities.\n\nBefore electrolysis, Bauxite must be purified into pure alumina ($\\text{Al}_2\\text{O}_3$) using the **Bayer Process**:\n1. **Dissolution in Concentrated $\\text{NaOH}$**: Crushed bauxite is heated under pressure with hot concentrated $\\text{NaOH}$ solution at $150^\\circ\\text{C}$. Because aluminium oxide is **amphoteric**, it dissolves forming soluble sodium aluminate:\n   $$\\text{Al}_2\\text{O}_3_{(s)} + 2\\text{NaOH}_{(aq)} + 3\\text{H}_2\\text{O}_{(l)} \\rightarrow 2\\text{NaAl(OH)}_{4(aq)}$$\n   Iron(III) oxide ($\\text{Fe}_2\\text{O}_3$) is basic and does not dissolve. It is filtered off as insoluble toxic **red mud**.\n2. **Precipitation**: The filtrate is seeded with pure $\\text{Al(OH)}_3$ crystals to precipitate aluminium hydroxide:\n   $$\\text{NaAl(OH)}_{4(aq)} \\rightarrow \\text{Al(OH)}_{3(s)} + \\text{NaOH}_{(aq)}$$\n3. **Calcination**: $\\text{Al(OH)}_3$ is filtered, washed, and heated strongly at $1000^\\circ\\text{C}$ in a rotary kiln to yield pure white **Alumina** ($\\text{Al}_2\\text{O}_3$):\n   $$2\\text{Al(OH)}_{3(s)} \\xrightarrow{1000^\\circ\\text{C}} \\text{Al}_2\\text{O}_{3(s)} + 3\\text{H}_2\\text{O}_{(g)}$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Stage 2: Hall-Héroult Electrolysis & Cryolite Flux",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Pure alumina ($\\text{Al}_2\\text{O}_3$) has an extremely high melting point of **$2050^\\circ\\text{C}$** and is a poor electrical conductor in solid state.\n\nTo overcome this, alumina is dissolved in molten **Cryolite** (sodium hexafluoroaluminate, **$\\text{Na}_3\\text{AlF}_6$**) at $950^\\circ\\text{C}$:\n* **Role of Cryolite ($\\text{Na}_3\\text{AlF}_6$)**:\n  1. Lowers the operating melting temperature from $2050^\\circ\\text{C}$ to $\\approx 950^\\circ\\text{C}$, dramatically reducing electricity and fuel costs.\n  2. Greatly improves the electrical conductivity of the molten mixture."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Electrode Reactions & Anode Replacement",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "The electrolysis is carried out in a steel tank lined with graphite:\n* **Cathode (Negative Electrode)**: The carbon/graphite lining of the steel cell.\n* **Anode (Positive Electrode)**: Blocks of graphite suspended down into the molten electrolyte.\n\n**Chemical Reactions at the Electrodes**:\n1. **At the Cathode (Reduction)**:\n   $$\\text{Al}^{3+}_{(l)} + 3e^- \\rightarrow \\text{Al}_{(l)}$$\n   *Macroscopic observation*: Dense molten aluminium metal forms and sinks to the bottom of the cell, where it is tapped off periodically.\n\n2. **At the Anode (Oxidation)**:\n   $$2\\text{O}^{2-}_{(l)} \\rightarrow \\text{O}_{2(g)} + 4e^-$$\n   *Critical Practical Detail*: At the high operating temperature ($950^\\circ\\text{C}$), the oxygen gas produced at the anode immediately reacts with the hot carbon/graphite anode blocks:\n   $$\\text{C}_{(s)} + \\text{O}_{2(g)} \\rightarrow \\text{CO}_{2(g)}$$\n   As a result, **the carbon anodes burn away continuously and must be replaced periodically**!"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Hall-Héroult Electrolytic Cell",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Schematic diagram of the Hall-Héroult cell for aluminium extraction showing suspended carbon anodes, carbon lining cathode, molten alumina in cryolite electrolyte layer, molten aluminium layer sinking at bottom, and tapping siphon pipe.",
                        "caption": "Hall-Héroult Cell Cross-Section: Suspended carbon anodes oxidise to CO2 while liquid aluminium collects at the carbon-lined cathode base."
                    },
                    "asset_info": {
                        "title": "Hall-Héroult Cell Schematic",
                        "description": "Technical diagram of Hall-Héroult aluminium electrolysis cell featuring graphite anodes, graphite cathode cell lining, molten electrolyte, and liquid Al layer.",
                        "ai_instruction": "Create an instructional diagram of the Hall-Héroult cell. Show carbon anodes hanging in electrolyte, carbon lining cathode, molten Al layer at bottom, tapping stream, and CO2 bubbles at anodes."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Role of Cryolite",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the primary industrial function of dissolving alumina ($\\text{Al}_2\\text{O}_3$) in molten cryolite ($\\text{Na}_3\\text{AlF}_6$) during the Hall-Héroult process?",
                        "options": [
                            "Cryolite reacts with alumina to form aluminium metal without requiring electricity.",
                            "Cryolite lowers the melting point of the alumina mixture from $2050^\\circ\\text{C}$ to $950^\\circ\\text{C}$ and enhances electrical conductivity.",
                            "Cryolite neutralizes toxic carbon dioxide gas emitted by carbon anodes.",
                            "Cryolite prevents aluminium from reacting with oxygen at the cathode."
                        ],
                        "answer": "B",
                        "explanation": "Pure alumina melts at an impractically high temperature ($2050^\\circ\\text{C}$). Dissolving it in molten cryolite ($\\text{Na}_3\\text{AlF}_6$) creates a solution that electrolyzes at $950^\\circ\\text{C}$, cutting energy costs significantly while providing mobile ions for electrical conduction."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Anode Consumption Mechanism",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why must the graphite anodes in the Hall-Héroult electrolytic cell be continuously replaced during industrial extraction of aluminium?",
                        "options": [
                            "Aluminium metal coats the anodes and stops electrical current.",
                            "Oxygen gas produced at the positive anode reacts with the hot graphite blocks at $950^\\circ\\text{C}$, forming carbon dioxide gas and burning away the anodes.",
                            "Cryolite dissolves graphite rapidly at room temperature.",
                            "The anodes melt because graphite has a lower melting point than aluminium."
                        ],
                        "answer": "B",
                        "explanation": "Oxidation of oxide ions at the anode generates oxygen gas ($2\\text{O}^{2-} \\rightarrow \\text{O}_2 + 4e^-$). At $950^\\circ\\text{C}$, oxygen reacts with the carbon anode ($\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2$), slowly consuming the graphite blocks as carbon dioxide gas."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Aluminium Extraction\n- **Stage 1 (Bayer Process)**: Bauxite purified with hot conc. $\\text{NaOH}$ (amphoteric $\\text{Al}_2\\text{O}_3$ dissolves; basic $\\text{Fe}_2\\text{O}_3$ filtered out as red mud).\n- **Stage 2 (Hall-Héroult Process)**: Electrolysis of $\\text{Al}_2\\text{O}_3$ dissolved in molten cryolite ($\\text{Na}_3\\text{AlF}_6$) at $950^\\circ\\text{C}$.\n- **Cathode (Graphite Lining)**: $\\text{Al}^{3+} + 3e^- \\rightarrow \\text{Al}_{(l)}$ (molten Al sinks to bottom).\n- **Anode (Graphite Blocks)**: $2\\text{O}^{2-} \\rightarrow \\text{O}_2 + 4e^-$; oxygen burns graphite anodes to $\\text{CO}_2$ gas."
                    }
                }
            ]
        },

        107: {
            "title": "Iron — Occurrence and Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Iron Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the extraction of iron from Haematite ($\\text{Fe}_2\\text{O}_3$) in the Blast Furnace, including the temperature gradient zones, carbon monoxide reduction reactions, and slag formation."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Raw Materials Charged into the Blast Furnace",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Iron is extracted from its chief ore **Haematite** ($\\text{Fe}_2\\text{O}_3$) in a tall steel tower lined with firebrick called a **Blast Furnace**.\n\nA mixture called the **charge** is continuously fed into the top of the furnace:\n1. **Haematite ($\\text{Fe}_2\\text{O}_3$)**: Source of iron metal.\n2. **Coke ($\\text{C}$)**: Fuel and precursor for the reducing agent.\n3. **Limestone ($\\text{CaCO}_3$)**: Flux used to remove silica impurities ($\\text{SiO}_2$).\n\nAt the bottom, blasts of hot air (oxygen) are blown in through pipes called **tuyeres**."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Temperature Zones & Reduction Reactions",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "As charge moves down and hot gases rise up, three distinct temperature zones drive the chemical reactions:\n\n1. **Zone 1: Combustion Zone (Bottom, $\\approx 1700^\\circ\\text{C}$)**:\n   Coke burns fiercely in hot air in a highly exothermic reaction that supplies heat to the furnace:\n   $$\\text{C}_{(s)} + \\text{O}_{2(g)} \\rightarrow \\text{CO}_{2(g)} \\quad (\\Delta H \\text{ negative})$$\n\n2. **Zone 2: Reducing Agent Formation (Middle, $\\approx 1000^\\circ\\text{C}$)**:\n   As $\\text{CO}_2$ gas rises through hot coke, it is reduced to **Carbon Monoxide ($\\text{CO}$)**:\n   $$\\text{CO}_{2(g)} + \\text{C}_{(s)} \\rightarrow 2\\text{CO}_{(g)}$$\n\n3. **Zone 3: Iron Reduction Zone (Upper, $400^\\circ\\text{C} - 700^\\circ\\text{C}$)**:\n   Carbon Monoxide is the **chief reducing agent**. It reduces Haematite step-by-step to molten iron metal:\n   $$\\text{Fe}_2\\text{O}_{3(s)} + 3\\text{CO}_{(g)} \\rightarrow 2\\text{Fe}_{(l)} + 3\\text{CO}_{2(g)}$$\n   Molten iron trickles down to the bottom of the furnace."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Removing Impurities: Slag Formation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Haematite ore contains rocky sandy impurities, mainly Silica (silicon dioxide, **$\\text{SiO}_2$**), which would contaminate the iron.\n\nLimestone ($\\text{CaCO}_3$) removes silica via a two-step process:\n1. **Thermal Decomposition of Limestone** (Middle zone, $\\approx 900^\\circ\\text{C}$):\n   $$\\text{CaCO}_{3(s)} \\xrightarrow{\\Delta} \\text{CaO}_{(s)} + \\text{CO}_{2(g)}$$\n2. **Neutralization Reaction to Form Slag**:\n   Calcium oxide (basic oxide) reacts with silica (acidic oxide) to form molten **Calcium Silicate (Slag)**:\n   $$\\text{CaO}_{(s)} + \\text{SiO}_{2(s)} \\rightarrow \\text{CaSiO}_{3(l)}$$\n\n**Dual Function of Molten Slag**:\n- Molten slag ($\\text{CaSiO}_3$) trickles to the bottom and **floats on top of molten iron** because slag is less dense than iron.\n- This floating layer protects the hot molten iron from being re-oxidized by the incoming blast of hot air!"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Blast Furnace Internal Zones",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Detailed diagram of Blast Furnace cross-section showing top charge hopper, temperature gradient zones (400C to 1700C), tuyere hot air pipes, floating molten slag layer, and bottom molten pig iron layer.",
                        "caption": "Blast Furnace Schematic: Iron ore is reduced by CO gas as it descends. Molten slag floats over molten iron at the base."
                    },
                    "asset_info": {
                        "title": "Blast Furnace Schematic Diagram",
                        "description": "Cross-sectional diagram of industrial Blast Furnace highlighting raw charge feed, temperature zones, reduction equations, and molten iron/slag outlets.",
                        "ai_instruction": "Create a clear cross-sectional diagram of a Blast Furnace. Label the top charge inlet, chemical equations at 400C, 1000C, and 1700C, tuyeres, waste gas exit, and separate taps for molten slag and pig iron."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Chief Reducing Agent in Blast Furnace",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which gaseous chemical substance acts as the primary reducing agent responsible for converting Haematite ($\\text{Fe}_2\\text{O}_3$) to molten iron in the upper reduction zone of the Blast Furnace?",
                        "options": [
                            "Carbon dioxide gas ($\\text{CO}_2$)",
                            "Carbon Monoxide gas ($\\text{CO}$)",
                            "Oxygen gas ($\\text{O}_2$)",
                            "Calcium oxide solid ($\\text{CaO}$)"
                        ],
                        "answer": "B",
                        "explanation": "Although solid coke (carbon) is added to the furnace, it reacts with rising $\\text{CO}_2$ at $1000^\\circ\\text{C}$ to form Carbon Monoxide gas ($\\text{CO}_2 + \\text{C} \\rightarrow 2\\text{CO}$). $\\text{CO}$ gas rises and intimately mixes with Haematite powder, reducing it according to: $\\text{Fe}_2\\text{O}_3 + 3\\text{CO} \\rightarrow 2\\text{Fe} + 3\\text{CO}_2$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Function of Molten Slag",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is the formation of molten slag ($\\text{CaSiO}_3$) essential during the Blast Furnace extraction of iron?",
                        "options": [
                            "Slag dissolves pure iron to prevent it from solidifying at furnace temperatures.",
                            "Slag removes acidic silica ($\\text{SiO}_2$) impurities and floats on top of molten iron, protecting it from re-oxidation by hot air blasts.",
                            "Slag acts as the primary fuel source that generates heat in the combustion zone.",
                            "Slag breaks down into carbon monoxide gas to speed up iron reduction."
                        ],
                        "answer": "B",
                        "explanation": "Slag ($\\text{CaSiO}_3$) is formed when basic $\\text{CaO}$ reacts with acidic silica ($\text{CaO} + \\text{SiO}_2 \\rightarrow \\text{CaSiO}_3$). Because molten slag is less dense than liquid iron, it forms a floating layer at the bottom, removing silica impurities while shielding the pure liquid iron from re-oxidizing in the incoming hot air stream."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Iron Extraction (Blast Furnace)\n- **Raw Materials**: Haematite ($\\text{Fe}_2\\text{O}_3$), Coke ($\\text{C}$), Limestone ($\\text{CaCO}_3$), Hot air blast.\n- **Chief Reducing Agent**: Carbon Monoxide ($\\text{CO}$ formed via $\\text{CO}_2 + \\text{C} \\rightarrow 2\\text{CO}$).\n- **Reduction Equation**: $\\text{Fe}_2\\text{O}_{3(s)} + 3\\text{CO}_{(g)} \\rightarrow 2\\text{Fe}_{(l)} + 3\\text{CO}_{2(g)}$.\n- **Slag Formation**: $\\text{CaCO}_3 \\rightarrow \\text{CaO} + \\text{CO}_2$; $\\text{CaO} + \\text{SiO}_2 \\rightarrow \\text{CaSiO}_{3(l)}$ (floats on molten iron)."
                    }
                }
            ]
        },

        108: {
            "title": "Zinc — Occurrence and Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Zinc Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand how zinc is extracted from Zinc Blende ($\\text{ZnS}$) via froth flotation, roasting to zinc oxide, and reduction using either carbon (coke) or electrolysis."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Step 1: Concentration & Roasting of Zinc Blende",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Zinc's chief ore is **Zinc Blende** (zinc sulfide, **$\\text{ZnS}$**). Another common ore is Calamine ($\\text{ZnCO}_3$).\n\n**Extraction Steps**:\n1. **Concentration**: The crushed ore is concentrated by **Froth Flotation** to remove gangue.\n2. **Roasting in Air**: The concentrated $\\text{ZnS}$ is strongly heated (roasted) in a furnace with excess air at $900^\\circ\\text{C}$ to convert sulfide into oxide:\n   $$2\\text{ZnS}_{(s)} + 3\\text{O}_{2(g)} \\xrightarrow{900^\\circ\\text{C}} 2\\text{ZnO}_{(s)} + 2\\text{SO}_{2(g)}$$\n   *Environmental Detail*: Sulfur dioxide gas ($\\text{SO}_{2}$) is a major pollutant. Industrial plants capture $\\text{SO}_2$ and use it to manufacture Sulfuric Acid ($\\text{H}_2\\text{SO}_4$) in the Contact Process."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Step 2: Reduction Route 1 — Carbon Reduction & Distillation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Zinc Oxide ($\\text{ZnO}$) can be reduced to zinc metal using carbon (coke):\n$$\\text{ZnO}_{(s)} + \\text{C}_{(s)} \\xrightarrow{1400^\\circ\\text{C}} \\text{Zn}_{(g)} + \\text{CO}_{(g)}$$\nAlternatively, carbon monoxide reduces it: $\\text{ZnO}_{(s)} + \\text{CO}_{(g)} \\rightarrow \\text{Zn}_{(g)} + \\text{CO}_{2(g)}$.\n\n**The Distillation Phenomenon**:\n- The furnace operates at **$1400^\\circ\\text{C}$**.\n- Zinc metal has a relatively low boiling point of **$907^\\circ\\text{C}$**.\n- Therefore, zinc is produced as **zinc vapor (gas)**! The vapor passes out of the furnace into a condenser, where it cools into liquid zinc and solidifies into solid zinc ingots."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Step 2: Reduction Route 2 — Electrolytic Reduction",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "To obtain high-purity zinc ($99.95\\%$), an electrolytic method is used:\n1. Roasted $\\text{ZnO}$ is dissolved in dilute sulfuric acid to form zinc sulfate solution:\n   $$\\text{ZnO}_{(s)} + \\text{H}_2\\text{SO}_{4(aq)} \\rightarrow \\text{ZnSO}_{4(aq)} + \\text{H}_2\\text{O}_{(l)}$$\n2. The solution is electrolyzed using **lead anodes** and **aluminium cathodes**:\n   - **At the Cathode (Reduction)**:\n     $$\\text{Zn}^{2+}_{(aq)} + 2e^- \\rightarrow \\text{Zn}_{(s)}$$\n     Pure zinc metal deposits as a solid sheet on the aluminium cathode, which is peeled off periodically."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Zinc Extraction Flowsheet",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Flowchart diagram showing Zinc Blende (ZnS) -> Froth Flotation -> Roasting Furnace (ZnO + SO2) -> Reduction Furnace with Coke (Zinc vapor at 1400C) -> Condenser -> Pure Zinc ingots.",
                        "caption": "Zinc Extraction Flowchart: Sulfide ore is concentrated, roasted to oxide, reduced by coke, and vapor-distilled."
                    },
                    "asset_info": {
                        "title": "Zinc Extraction Process Flowchart",
                        "description": "Block process diagram detailing stages of zinc extraction from raw ZnS ore to final condensed zinc ingots.",
                        "ai_instruction": "Create a clean industrial flowchart of zinc extraction. Show Froth Flotation, Roasting furnace generating SO2, Carbon reduction furnace producing zinc vapor at 1400C, and condenser unit."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Zinc Distillation Boiling Point",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is zinc metal collected as a gas/vapor from the carbon reduction furnace rather than as a liquid?",
                        "options": [
                            "Zinc reacts with carbon to form a volatile gaseous hydrocarbon compound.",
                            "The furnace operates at $1400^\\circ\\text{C}$, which is higher than zinc's boiling point of $907^\\circ\\text{C}$, causing reduced zinc to instantly vaporize.",
                            "Zinc metal sublimation occurs spontaneously at room temperature.",
                            "Carbon monoxide gas dissolves zinc liquid, carrying it away as a fog."
                        ],
                        "answer": "B",
                        "explanation": "Zinc has a boiling point of $907^\\circ\\text{C}$. Because the reduction furnace with coke operates at $1400^\\circ\\text{C}$, the newly reduced zinc metal immediately boils into zinc vapor gas. The vapor is piped to a condenser chamber where it cools and solidifies into zinc ingots."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Roasting Chemical Equation",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What are the chemical products formed when concentrated Zinc Blende ($\\text{ZnS}$) is roasted strongly in air?",
                        "options": [
                            "Zinc metal and sulfur trioxide gas",
                            "Zinc oxide solid and sulfur dioxide gas",
                            "Zinc carbonate solid and hydrogen sulfide gas",
                            "Zinc hydroxide solid and oxygen gas"
                        ],
                        "answer": "B",
                        "explanation": "Roasting a sulfide ore in excess oxygen converts metal sulfides into metal oxides while oxidizing sulfur to sulfur dioxide gas: $2\\text{ZnS}_{(s)} + 3\\text{O}_{2(g)} \\rightarrow 2\\text{ZnO}_{(s)} + 2\\text{SO}_{2(g)}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Zinc Extraction\n- **Chief Ore**: Zinc Blende ($\\text{ZnS}$).\n- **Roasting**: $2\\text{ZnS}_{(s)} + 3\\text{O}_{2(g)} \\rightarrow 2\\text{ZnO}_{(s)} + 2\\text{SO}_{2(g)}$ (byproduct $\\text{SO}_2$ captured for $\\text{H}_2\\text{SO}_4$).\n- **Reduction**: $\\text{ZnO}_{(s)} + \\text{C}_{(s)} \\xrightarrow{1400^\\circ\\text{C}} \\text{Zn}_{(g)} + \\text{CO}_{(g)}$ (zinc vapor distills off at $907^\\circ\\text{C}$ and condenses).\n- **Electrolytic Alternative**: $\\text{Zn}^{2+}_{(aq)} + 2e^- \\rightarrow \\text{Zn}_{(s)}$ on aluminium cathode."
                    }
                }
            ]
        },

        109: {
            "title": "Lead — Occurrence and Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Lead Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the extraction of lead from Galena ($\\text{PbS}$), controlled roasting to lead(II) oxide, carbon reduction, and environmental precautions regarding lead toxicity."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Chief Ore & Controlled Roasting of Galena",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "The chief ore of lead is **Galena** (lead(II) sulfide, **$\\text{PbS}$**), a dense, metallic gray mineral.\n\n**Extraction Steps**:\n1. **Concentration**: Crushed Galena is concentrated by **Froth Flotation**.\n2. **Controlled Roasting**: The concentrated $\\text{PbS}$ is heated in a controlled supply of air in a reverberatory furnace:\n   $$2\\text{PbS}_{(s)} + 3\\text{O}_{2(g)} \\rightarrow 2\\text{PbO}_{(s)} + 2\\text{SO}_{2(g)}$$\n   *Alternative Reaction*: If air supply is limited, partial roasting converts some $\\text{PbS}$ to lead(II) sulfate ($\\text{PbSO}_4$) or lead oxide ($\\text{PbO}$)."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Chemical Reduction & Self-Reduction Routes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Lead(II) oxide ($\\text{PbO}$) is reduced to molten lead metal via two industrial pathways:\n\n1. **Reduction with Coke / Carbon Monoxide in Blast Furnace**:\n   Roasted $\\text{PbO}$ is mixed with coke and limestone and heated in a small blast furnace:\n   $$\\text{PbO}_{(s)} + \\text{C}_{(s)} \\rightarrow \\text{Pb}_{(l)} + \\text{CO}_{(g)}$$\n   $$\\text{PbO}_{(s)} + \\text{CO}_{(g)} \\rightarrow \\text{Pb}_{(l)} + \\text{CO}_{2(g)}$$\n\n2. **Self-Reduction Route**:\n   Un-reacted Galena ($\\text{PbS}$) reacts directly with newly formed $\\text{PbO}$ without needing carbon:\n   $$\\text{PbS}_{(s)} + 2\\text{PbO}_{(s)} \\rightarrow 3\\text{Pb}_{(l)} + \\text{SO}_{2(g)}$$\n   Molten lead metal sinks to the bottom of the furnace and is tapped off into ingots."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Diagram: Lead Extraction Flowsheet",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Flowchart diagram showing Galena (PbS) -> Froth Flotation -> Roasting Furnace -> Lead Blast Furnace with Coke -> Molten Lead Tapping -> Softening Refinery.",
                        "caption": "Lead Extraction Process: Galena is concentrated by froth flotation, roasted to PbO, reduced by coke, and refined."
                    },
                    "asset_info": {
                        "title": "Lead Extraction Flowchart",
                        "description": "Schematic diagram detailing Galena ore processing, roasting, carbon reduction, and lead refining.",
                        "ai_instruction": "Create an industrial flowchart showing Galena flotation, roasting to PbO, coke reduction in blast furnace, and molten lead collection."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Understanding Check: Galena Roasting Reaction",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What chemical equation represents the initial roasting of Galena ($\\text{PbS}$) in excess air?",
                        "options": [
                            "$\\text{PbS} + \\text{O}_2 \\rightarrow \\text{Pb} + \\text{SO}_2$",
                            "$2\\text{PbS} + 3\\text{O}_2 \\rightarrow 2\\text{PbO} + 2\\text{SO}_2$",
                            "$\\text{PbS} + 2\\text{H}_2\\text{O} \\rightarrow \\text{Pb(OH)}_2 + \\text{H}_2\\text{S}$",
                            "$\\text{PbS} + \\text{CO}_2 \\rightarrow \\text{PbCO}_3 + \\text{S}$"
                        ],
                        "answer": "B",
                        "explanation": "Roasting Galena ($\text{PbS}$) in air oxidizes sulfur to $\\text{SO}_2$ gas and lead to lead(II) oxide solid: $2\\text{PbS} + 3\\text{O}_2 \\rightarrow 2\\text{PbO} + 2\\text{SO}_2$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Lead Self-Reduction Mechanism",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "How does un-reacted Galena ($\\text{PbS}$) achieve self-reduction when mixed with lead(II) oxide ($\\text{PbO}$) at high temperature?",
                        "options": [
                            "$\\text{PbS}$ donates sulfur to oxygen, reducing $\\text{PbO}$ and $\\text{PbS}$ to molten lead metal and $\\text{SO}_2$ gas without requiring coke.",
                            "$\\text{PbS}$ acts as a catalyst that decomposes $\\text{PbO}$ into lead metal and oxygen gas.",
                            "$\\text{PbS}$ absorbs lead metal, forming a soft lead alloy.",
                            "$\\text{PbS}$ reacts with water vapor to precipitate lead crystals."
                        ],
                        "answer": "A",
                        "explanation": "In self-reduction, sulfur in $\\text{PbS}$ acts as the reducing agent for $\\text{PbO}$: $\\text{PbS}_{(s)} + 2\\text{PbO}_{(s)} \\rightarrow 3\\text{Pb}_{(l)} + \\text{SO}_{2(g)}$. Both compounds are reduced to elemental molten lead."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Lead Extraction\n- **Chief Ore**: Galena ($\\text{PbS}$).\n- **Roasting**: $2\\text{PbS}_{(s)} + 3\\text{O}_{2(g)} \\rightarrow 2\\text{PbO}_{(s)} + 2\\text{SO}_{2(g)}$.\n- **Reduction**: $\\text{PbO}_{(s)} + \\text{C}_{(s)} \\rightarrow \\text{Pb}_{(l)} + \\text{CO}_{(g)}$ or self-reduction $\\text{PbS} + 2\\text{PbO} \\rightarrow 3\\text{Pb} + \\text{SO}_2$.\n- **Environmental Warning**: Lead fumes and $\\text{SO}_2$ are toxic heavy pollutants requiring strict flue gas filtration."
                    }
                }
            ]
        },

        110: {
            "title": "Copper — Occurrence and Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Copper Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the multi-step extraction of copper from Copper Pyrites ($\\text{CuFeS}_2$), including roasting, smelting with silica flux, converter self-reduction to blister copper, and electrolytic refining."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Step 1 & 2: Partial Roasting & Smelting with Silica",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Copper's chief ore is **Copper Pyrites** ($\\text{CuFeS}_2$), which contains both copper and iron sulfides.\n\n**Extraction Sequence**:\n1. **Concentration**: Concentrated by Froth Flotation.\n2. **Partial Roasting in Limited Air**:\n   The ore is roasted in a furnace with limited oxygen to selectively oxidize iron sulfide while keeping copper sulfide intact:\n   $$2\\text{CuFeS}_{2(s)} + 2\\text{O}_{2(g)} \\rightarrow \\text{Cu}_2\\text{S}_{(s)} + 2\\text{FeS}_{(s)} + \\text{SO}_{2(g)}$$\n3. **Smelting with Silica Flux ($\\text{SiO}_2$)**:\n   The roasted mixture is mixed with sand (Silica, $\\text{SiO}_2$) and heated in a blast furnace. Iron sulfide is oxidized to iron(II) oxide ($\\text{FeO}$), which reacts with silica flux to form molten slag:\n   $$\\text{FeO}_{(s)} + \\text{SiO}_{2(s)} \\rightarrow \\text{FeSiO}_{3(l)} \\quad (\\text{Iron Slag})$$\n   The molten slag floats on top and is poured off, leaving behind molten **Copper Matte** (a liquid mixture of $\\text{Cu}_2\\text{S}$ and trace $\\text{FeS}$)."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Step 3: Converter Self-Reduction to Blister Copper",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Molten Copper Matte ($\\text{Cu}_2\\text{S}$) is transferred into a Bessemer converter and blasts of air are blown through it:\n\n1. Part of the $\\text{Cu}_2\\text{S}$ is oxidized to copper(I) oxide:\n   $$2\\text{Cu}_2\\text{S}_{(l)} + 3\\text{O}_{2(g)} \\rightarrow 2\\text{Cu}_2\\text{O}_{(l)} + 2\\text{SO}_{2(g)}$$\n2. The newly formed $\\text{Cu}_2\\text{O}$ reacts with remaining $\\text{Cu}_2\\text{S}$ in a **self-reduction reaction**:\n   $$\\text{Cu}_2\\text{S}_{(l)} + 2\\text{Cu}_2\\text{O}_{(l)} \\rightarrow 6\\text{Cu}_{(l)} + \\text{SO}_{2(g)}$$\n\n**Why is it called 'Blister Copper'?**\nAs the molten copper cools and solidifies, escaping bubbles of sulfur dioxide gas ($\\text{SO}_2$) burst through the surface, leaving rough blister-like craters on the copper metal sheets ($98-99\\%$ pure)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Step 4: Electrolytic Refining to 99.99% Pure Copper",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Blister copper ($98\\%$) contains impurities (iron, nickel, silver, gold) that reduce its electrical conductivity. It must be refined to **$99.99\\%$ pure copper** via electrolysis:\n\n* **Anode (Positive)**: Thick slab of impure **Blister Copper**.\n* **Cathode (Negative)**: Thin sheet of **Pure Copper**.\n* **Electrolyte**: Aqueous Copper(II) Sulfate solution ($\\text{CuSO}_{4(aq)}$) acidified with $\\text{H}_2\\text{SO}_4$.\n\n**Electrode Reactions during Refining**:\n1. **At the Anode (Oxidation)**:\n   $$\\text{Cu}_{(s, \\text{impure})} \\rightarrow \\text{Cu}^{2+}_{(aq)} + 2e^-$$\n   Impure copper anode dissolves into copper ions. Noble impurities (gold, silver) do not dissolve and drop to the bottom as valuable **anode sludge**.\n\n2. **At the Cathode (Reduction)**:\n   $$\\text{Cu}^{2+}_{(aq)} + 2e^- \\rightarrow \\text{Cu}_{(s, \\text{pure})}$$\n   Pure copper ions deposit onto the pure copper cathode sheet, which grows thick."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Copper Electrolytic Refining Cell",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram of electrolytic refining of copper showing impure blister copper anode dissolving, pure copper cathode thickening, acidic CuSO4 electrolyte, and valuable anode sludge settling at the bottom.",
                        "caption": "Copper Electrolytic Refining: Impure anode dissolves while 99.99% pure copper deposits on cathode. Gold/silver collect in anode sludge."
                    },
                    "asset_info": {
                        "title": "Copper Refining Cell Schematic",
                        "description": "Technical diagram of copper electrolytic refining highlighting anode dissolution, cathode deposition, and precious metal anode sludge.",
                        "ai_instruction": "Create an instructional diagram of copper electrolytic refining. Label impure copper anode (+), pure copper cathode (-), CuSO4 electrolyte, Cu2+ ion migration arrows, and precious metal anode sludge."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Origin of Blister Copper",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What causes the characteristic 'blistered' surface appearance on crude copper metal produced in the Bessemer converter?",
                        "options": [
                            "Air bubbles trapped under molten copper during rapid water quenching.",
                            "Escaping sulfur dioxide gas ($\\text{SO}_2$) bubbling out of the molten metal as it cools and solidifies.",
                            "Steam generated when silica flux reacts with copper oxide.",
                            "Hydrogen gas bubbles released by iron impurities."
                        ],
                        "answer": "B",
                        "explanation": "During converter self-reduction ($\\text{Cu}_2\\text{S} + 2\\text{Cu}_2\\text{O} \\rightarrow 6\\text{Cu} + \\text{SO}_2$), large volumes of $\\text{SO}_2$ gas are generated. As liquid copper cools, escaping $\\text{SO}_2$ gas bubbles burst through the solidifying surface, leaving blister-like marks."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Copper Refining Electrodes",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "During the electrolytic refining of copper, what happens to the masses of the anode and cathode over time?",
                        "options": [
                            "Both anode and cathode gain mass equally.",
                            "The impure blister copper anode loses mass as it dissolves, while the pure copper cathode gains mass as pure $\\text{Cu}^{2+}$ ions deposit on it.",
                            "The anode gains mass from copper sulfate deposition, while the cathode dissolves.",
                            "Neither electrode changes mass because copper ions only cycle in solution."
                        ],
                        "answer": "B",
                        "explanation": "At the positive anode, impure copper oxidizes into solution ($\\text{Cu} \\rightarrow \\text{Cu}^{2+} + 2e^-$), causing the anode to lose mass. At the negative cathode, copper ions gain electrons and deposit as pure metal ($\\text{Cu}^{2+} + 2e^- \\rightarrow \\text{Cu}$), causing the cathode to gain mass."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Copper Extraction & Refining\n- **Chief Ore**: Copper Pyrites ($\\text{CuFeS}_2$).\n- **Roasting & Smelting**: $2\\text{CuFeS}_2 + 2\\text{O}_2 \\rightarrow \\text{Cu}_2\\text{S} + 2\\text{FeS} + \\text{SO}_2$; $\\text{FeO} + \\text{SiO}_2 \\rightarrow \\text{FeSiO}_3$ slag.\n- **Blister Copper Self-Reduction**: $\\text{Cu}_2\\text{S} + 2\\text{Cu}_2\\text{O} \\rightarrow 6\\text{Cu}_{(l)} + \\text{SO}_{2(g)}$ ($98\\%$ pure).\n- **Electrolytic Refining**: Anode = Blister copper; Cathode = Pure copper; Electrolyte = $\\text{CuSO}_{4(aq)}$. Yields $99.99\\%$ pure copper."
                    }
                }
            ]
        },

        111: {
            "title": "Physical Properties of Metals",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Physical Properties of Metals",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand metallic bonding using the 'Sea of Electrons' model and how it explains electrical/thermal conductivity, malleability, ductility, high density, and melting points."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The 'Sea of Electrons' Particle Model",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Why do metals conduct electricity, shine brightly, and bend under a hammer without shattering?\n\nTo understand metals at the submicroscopic particle level, we use the **Metallic Lattice & Delocalized Electron Model**:\n* Metal atoms lose their outer valence electrons to form a 3D giant lattice of positive metal cations ($\\text{M}^{n+}$).\n* The lost valence electrons are no longer tied to any single atom; they form a mobile **'sea' of delocalized electrons** that drift freely throughout the entire metallic structure.\n* **Metallic Bond**: The strong electrostatic force of attraction between positive metal cations and the surrounding delocalized electron cloud."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Explaining Conductivity: Electrical & Thermal",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Using the 'sea of electrons' particle model, we can explain key physical properties:\n\n1. **Electrical Conductivity**:\n   - When a voltage / potential difference is applied across a metal wire, the free delocalized electrons immediately drift toward the positive terminal, creating an electric current.\n   - *Comparison*: Ionic solids do NOT conduct electricity because their ions are fixed in rigid lattice positions."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Explaining Malleability and Ductility",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "2. **Malleability (Hammered into thin sheets) & Ductility (Drawn into long wires)**:\n   - In a metal lattice, positive cations are arranged in neat packed layers.\n   - When a mechanical force or hammer blow is applied, layers of metal cations **slide past one another**.\n   - Because the delocalized electron cloud is flexible and mobile, it instantly shifts to maintain electrostatic attraction between cations and electrons in their new positions. The metallic bond does NOT break, so the metal bends without shattering!\n   - *Contrast*: Ionic crystals (like $\\text{NaCl}$) are brittle because shifting layers forces like-charged ions adjacent to each other ($\\text{Na}^+$ next to $\\text{Na}^+$), causing intense electrostatic repulsion that shatters the crystal."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Malleability in Metallic Lattice",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Particle diagram contrasting metal cation layers sliding smoothly within delocalized electron sea vs ionic lattice shattering under mechanical force.",
                        "caption": "Malleability Particle Model: Layers of metal cations slide past each other while the delocalized electron sea maintains cohesion."
                    },
                    "asset_info": {
                        "title": "Metallic Malleability vs Ionic Brittleness",
                        "description": "Particle illustration demonstrating sliding cation layers in metals vs electrostatic repulsion shatter in ionic solids under force.",
                        "ai_instruction": "Create a 2-part particle diagram. Part A: Metal cation layers sliding smoothly within electron sea under hammer force. Part B: Ionic lattice shattering due to like-charge repulsion."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Malleability Particle Model",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why do metals bend cleanly when struck with a hammer (malleability), whereas ionic solids like sodium chloride shatter into pieces?",
                        "options": [
                            "Metal cations melt instantly upon impact, absorbing mechanical shock.",
                            "In metals, layers of positive cations slide past each other without breaking bonds because the flexible delocalized electron cloud shifts to hold them together.",
                            "Ionic solids contain gas pockets that explode under mechanical pressure.",
                            "Delocalized electrons absorb all mechanical energy, converting it into heat."
                        ],
                        "answer": "B",
                        "explanation": "Malleability relies on non-directional metallic bonding. When force is applied, layers of metal cations slide past one another. The mobile delocalized electron sea instantly adjusts around the shifted cations, preventing like-charge repulsion and holding the lattice together."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Electrical Conduction Mechanism",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What particle-level species is responsible for carrying electrical current through a solid copper wire?",
                        "options": [
                            "Positive copper cations ($\\text{Cu}^{2+}$) migrating toward the negative terminal.",
                            "Delocalized valence electrons drifting freely toward the positive terminal.",
                            "Protons moving through empty spaces in the atomic nuclei.",
                            "Copper oxide molecules sliding along the wire surface."
                        ],
                        "answer": "B",
                        "explanation": "In metallic bonding, valence electrons leave individual atoms and form a delocalized electron cloud. When a voltage is applied, these free-moving delocalized electrons drift toward the positive terminal, conducting electrical current."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Physical Properties of Metals\n- **Metallic Bond**: Electrostatic attraction between positive metal cations and delocalized valence electron sea.\n- **Electrical Conductivity**: Free delocalized electrons drift when potential difference is applied.\n- **Malleability/Ductility**: Cation layers slide past each other under force; electron sea adjusts without shattering.\n- **High Melting Points**: Requires large heat energy to break strong 3D metallic bonds."
                    }
                }
            ]
        },

        112: {
            "title": "Chemical Properties of Metals",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Chemical Properties of Metals",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand how metals react with oxygen, water/steam, dilute acids, and chlorine gas, and how these reactions reflect their position in the Reactivity Series."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Reaction 1: Metals with Oxygen (Air)",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Metals burn or tarnish in oxygen to form basic metal oxides:\n$$\\text{Metal} + \\text{Oxygen} \\rightarrow \\text{Metal Oxide}$$\n\n* **Sodium (High Reactivity)**: Burns fiercely with a yellow flame in air forming sodium oxide:\n  $$4\\text{Na}_{(s)} + \\text{O}_{2(g)} \\rightarrow 2\\text{Na}_2\\text{O}_{(s)}$$\n* **Magnesium (Moderate Reactivity)**: Burns with a dazzling white flame forming white powder:\n  $$2\\text{Mg}_{(s)} + \\text{O}_{2(g)} \\rightarrow 2\\text{MgO}_{(s)}$$\n* **Iron**: Does not burn as solid bar, but iron filings sparkle in a Bunsen flame to form triiron tetroxide:\n  $$3\\text{Fe}_{(s)} + 2\\text{O}_{2(g)} \\rightarrow \\text{Fe}_3\\text{O}_{4(s)}$$\n* **Copper (Low Reactivity)**: Does not burn; forms a black surface coating of copper(II) oxide on heating:\n  $$2\\text{Cu}_{(s)} + \\text{O}_{2(g)} \\rightarrow 2\\text{CuO}_{(s)}$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Reaction 2: Metals with Water and Steam",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "The reaction of metals with water depends critically on whether **cold water** or **steam** is used:\n\n1. **Reaction with Cold Water (Highly Reactive Metals: K, Na, Ca)**:\n   $$\\text{Metal} + \\text{Cold Water} \\rightarrow \\text{Metal Hydroxide} + \\text{Hydrogen Gas}$$\n   - Sodium darts on water surface with a fizzing sound, producing alkaline $\\text{NaOH}$ solution:\n     $$2\\text{Na}_{(s)} + 2\\text{H}_2\\text{O}_{(l)} \\rightarrow 2\\text{NaOH}_{(aq)} + \\text{H}_{2(g)}$$\n\n2. **Reaction with Steam (Moderately Reactive Metals: Mg, Zn, Fe)**:\n   $$\\text{Metal} + \\text{Steam} \\rightarrow \\text{Metal Oxide} + \\text{Hydrogen Gas}$$\n   - Magnesium reacts very slowly with cold water, but burns intensely in **steam** forming white magnesium oxide:\n     $$\\text{Mg}_{(s)} + \\text{H}_2\\text{O}_{(g)} \\rightarrow \\text{MgO}_{(s)} + \\text{H}_{2(g)}$$\n\n3. **Unreactive Metals (Cu, Ag, Au)**: Do not react with cold water or steam."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Reaction 3 & 4: Metals with Acids & Chlorine Gas",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "3. **Reaction with Dilute Hydrochloric Acid**:\n   $$\\text{Metal} + \\text{Dilute Acid} \\rightarrow \\text{Salt} + \\text{Hydrogen Gas}$$\n   - Magnesium effervesces rapidly: $\\text{Mg}_{(s)} + 2\\text{HCl}_{(aq)} \\rightarrow \\text{MgCl}_{2(aq)} + \\text{H}_{2(g)}$\n   - *Special Case (Lead)*: Lead reacts very briefly with dilute $\\text{HCl}$ or $\\text{H}_2\\text{SO}_4$, then stops effervescing! This is because an insoluble coating of lead(II) chloride ($\\text{PbCl}_2$) or lead(II) sulfate ($\\text{PbSO}_4$) forms on the lead surface, creating a protective barrier against further acid attack.\n\n4. **Reaction with Chlorine Gas**:\n   Metals react with chlorine to form ionic metal chlorides:\n   - Iron filings heated in dry chlorine gas form reddish-brown iron(III) chloride:\n     $$2\\text{Fe}_{(s)} + 3\\text{Cl}_{2(g)} \\rightarrow 2\\text{FeCl}_{3(s)}$$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Metal Reactivity Comparison Chart",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Comparative illustration of apparatus showing Na reacting with cold water in trough, Mg reacting with steam in combustion tube, and Cu unreactive with acid.",
                        "caption": "Reactivity Spectrum: Sodium reacts vigorously with cold water, magnesium requires steam, and copper remains unreactive."
                    },
                    "asset_info": {
                        "title": "Metal Chemical Reactivity Lab Setup",
                        "description": "Diagram comparing lab setups for metal reactions with cold water, steam tube, and dilute acids across the Reactivity Series.",
                        "ai_instruction": "Create a multi-panel diagram showing: Panel 1: Na floating on cold water with H2 evolution. Panel 2: Mg burning in steam generating H2 gas. Panel 3: Cu in acid with zero gas bubbles."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Cold Water vs Steam Products",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the key chemical difference between the product formed when Sodium reacts with cold water versus when Magnesium reacts with steam?",
                        "options": [
                            "Sodium forms sodium oxide + hydrogen, whereas magnesium forms magnesium hydroxide + oxygen.",
                            "Sodium forms a soluble metal hydroxide ($\\text{NaOH}$) + hydrogen gas, whereas magnesium forms a solid metal oxide ($\\text{MgO}$) + hydrogen gas.",
                            "Both metals form identical gaseous products without any solid residue.",
                            "Magnesium forms magnesium carbonate, while sodium forms sodium chloride."
                        ],
                        "answer": "B",
                        "explanation": "Cold water reactions with alkali metals yield metal hydroxides ($2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2$). High-temperature steam reactions with less reactive metals decompose steam to form solid metal oxides ($\text{Mg} + \\text{H}_2\\text{O}_{(g)} \\rightarrow \\text{MgO} + \\text{H}_2$)."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Lead Reaction with Dilute Acids",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why does the reaction between lead metal and dilute sulfuric acid quickly slow down and stop effervescing shortly after starting?",
                        "options": [
                            "Lead metal dissolves completely within seconds.",
                            "An insoluble layer of lead(II) sulfate ($\\text{PbSO}_4$) forms on the surface of lead, forming a protective barrier that prevents further acid contact.",
                            "Sulfuric acid oxidizes lead into a gas that escapes.",
                            "Lead absorbs all hydrogen gas produced, stopping bubble formation."
                        ],
                        "answer": "B",
                        "explanation": "Initial reaction produces lead(II) sulfate ($\text{Pb} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{PbSO}_4 + \\text{H}_2$). Because $\\text{PbSO}_4$ is insoluble in water, it adheres to the lead metal surface as a tight physical coating, shielding unreacted lead beneath from acid contact."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Chemical Properties of Metals\n- **With Oxygen**: Forms basic metal oxides ($\\text{Na}_2\\text{O}, \\text{MgO}, \\text{Fe}_3\\text{O}_4, \\text{CuO}$).\n- **With Water**: Cold water $\\rightarrow \\text{Hydroxide} + \\text{H}_2$ (Na, K, Ca); Steam $\\rightarrow \\text{Oxide} + \\text{H}_2$ (Mg, Zn, Fe).\n- **With Acid**: $\\text{Metal} + \\text{Acid} \\rightarrow \\text{Salt} + \\text{H}_2$ (Lead coated by insoluble $\\text{PbSO}_4$ barrier).\n- **With Chlorine**: Forms ionic metal chlorides (e.g., $2\\text{Fe} + 3\\text{Cl}_2 \\rightarrow 2\\text{FeCl}_3$)."
                    }
                }
            ]
        },

        113: {
            "title": "Uses of Common Metals",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Uses of Common Metals",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand how the physical and chemical properties of Sodium, Aluminium, Iron, Zinc, Lead, and Copper directly determine their specific commercial and industrial uses."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Uses of Light & Conductive Metals: Al & Cu",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Industrial application requires matching a metal's physical properties to its job:\n\n1. **Aluminium ($\\text{Al}$)**:\n   - *Property*: Low density ($2.7\\text{ g/cm}^3$), high strength-to-weight ratio, excellent corrosion resistance due to protective oxide film ($\\text{Al}_2\\text{O}_3$), good electrical conductor.\n   - *Uses*: Aircraft bodies, window frames, food packaging foil, overhead power transmission cables.\n   - *Why Al for overhead cables?* Although copper is a slightly better conductor, aluminium is much less dense. Copper cables would be too heavy and snap power pylons under their own weight.\n\n2. **Copper ($\\text{Cu}$)**:\n   - *Property*: Superior electrical and thermal conductivity, ductile, unreactive with water.\n   - *Uses*: Electrical wiring, printed circuit boards, water pipes, cooking vessel bases."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Uses of Structural & Battery Metals: Fe, Zn, Pb, Na",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "3. **Iron ($\\text{Fe}$)**:\n   - *Property*: High tensile strength, abundant, cheap.\n   - *Uses*: Structural steel frames for buildings, bridges, machinery, engine blocks.\n\n4. **Zinc ($\\text{Zn}$)**:\n   - *Property*: Sacrificial protection agent, corrosion resistant.\n   - *Uses*: **Galvanizing iron sheets** (coating roofing sheets with zinc to prevent rust), dry cell battery casings (anode), making Brass alloy ($\\text{Cu} + \\text{Zn}$).\n\n5. **Lead ($\\text{Pb}$)**:\n   - *Property*: High density, resists acid corrosion, absorbs radiation.\n   - *Uses*: Car lead-acid storage batteries, radiation shielding in X-ray rooms.\n\n6. **Sodium ($\\text{Na}$)**:\n   - *Property*: Low melting point, high heat capacity, emits yellow light when excited.\n   - *Uses*: Yellow vapor street lamps, liquid Na-K coolant in nuclear reactors."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Diagram: Metal Property-to-Use Matching",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Infographic diagram matching properties (low density, high conductivity, sacrificial protection) to applications (aircraft, power cables, galvanized roofs).",
                        "caption": "Property-Use Alignment: Aluminium's low density suits aircraft & overhead cables, while zinc's oxidation potential protects iron."
                    },
                    "asset_info": {
                        "title": "Metal Applications Property Matrix",
                        "description": "Visual grid mapping physical/chemical properties of Al, Cu, Fe, Zn, Pb, and Na to real-world commercial products.",
                        "ai_instruction": "Create an infographic mapping key properties (low density, conductivity, sacrificial protection) to real-world items (aircraft, wiring, galvanized iron)."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Understanding Check: Overhead Power Cables Choice",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is Aluminium preferred over Copper for long-distance high-voltage overhead power cables, even though Copper has a slightly higher electrical conductivity?",
                        "options": [
                            "Aluminium is completely transparent to electrical resistance.",
                            "Aluminium has a much lower density than copper, preventing heavy sagging and pylons collapsing under cable weight.",
                            "Copper melts when carrying high voltage currents.",
                            "Aluminium reacts with air to produce additional electric voltage."
                        ],
                        "answer": "B",
                        "explanation": "Overhead transmission spans long distances between pylons. Copper is very dense ($8.96\\text{ g/cm}^3$) and heavy, which would cause cables to sag excessively and tear down pylons. Aluminium is much lighter ($2.70\\text{ g/cm}^3$), providing excellent electrical conductivity per unit mass."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Galvanizing Protection Mechanism",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "How does coating iron roofing sheets with a thin layer of Zinc (galvanizing) protect the iron from rusting even if the zinc layer gets scratched?",
                        "options": [
                            "Zinc turns iron into stainless steel upon scratching.",
                            "Zinc is more reactive than iron and sacrificially corrodes first by donating electrons to prevent iron from oxidizing.",
                            "Zinc reacts with oxygen to form a waterproof rubber seal.",
                            "Scratched zinc absorbs all moisture from the air."
                        ],
                        "answer": "B",
                        "explanation": "Zinc is higher than iron in the reactivity series. In sacrificial protection, zinc oxidizes preferentially ($\\text{Zn} \\rightarrow \\text{Zn}^{2+} + 2e^-$), supplying electrons to any exposed iron so that iron cannot lose electrons to form rust ($\\text{Fe}^{3+}$)."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Uses of Common Metals\n- **Aluminium**: Aircraft, overhead cables (low density + oxide protection).\n- **Copper**: Wiring, plumbing (high electrical/thermal conductivity).\n- **Iron**: Bridges, construction (high tensile strength).\n- **Zinc**: Galvanizing iron sheets (sacrificial protection).\n- **Lead**: Car batteries, X-ray shielding (dense, acid resistant).\n- **Sodium**: Vapor street lamps, nuclear coolant."
                    }
                }
            ]
        },

        114: {
            "title": "Uses of Iron Alloys",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Uses of Iron Alloys",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand why pure iron is modified into alloys, how carbon content alters mechanical properties, and the compositions and uses of Pig Iron, Wrought Iron, Mild Steel, High Carbon Steel, and Stainless Steel."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "What is an Alloy & Why Modify Pure Iron?",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Pure iron metal is relatively soft, malleable, and rusts rapidly in moist air, making it unsuitable for heavy structural engineering.\n\n**What is an Alloy?**\nAn alloy is a homogeneous mixture of a metal with one or more other elements (metals or non-metals).\n\n**Particle-Level Explanation of Alloy Strength**:\n- In pure iron, identical iron atoms are arranged in uniform layers that slide easily over one another under stress.\n- When foreign atoms (like Carbon, Chromium, or Nickel) of different atomic radii are added, they **distort the regular iron lattice**.\n- This distortion locks the layers in place, preventing them from sliding easily. As a result, alloys are much harder and stronger than pure metals!"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Iron-Carbon Alloy Spectrum",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Varying the carbon percentage in iron creates distinct commercial alloys:\n\n1. **Pig Iron / Cast Iron ($3.5\\% - 4.5\\%$ Carbon)**:\n   - Direct product of the blast furnace.\n   - *Properties*: Hard, very brittle, low melting point ($1200^\\circ\\text{C}$), cannot be forged.\n   - *Uses*: Engine blocks, manhole covers, drainage pipes, heavy iron stoves.\n\n2. **Wrought Iron ($<0.1\\%$ Carbon)**:\n   - Purest commercial iron made by burning carbon out of pig iron.\n   - *Properties*: Soft, malleable, ductile, tough, resistant to corrosion.\n   - *Uses*: Decorative gates, iron chains, railway couplings, nails.\n\n3. **Mild Steel ($0.1\\% - 0.25\\%$ Carbon)**:\n   - *Properties*: Strong, malleable, ductile, easily welded.\n   - *Uses*: Car body panels, girders, ship hulls, roof trusses.\n\n4. **High Carbon Steel ($0.5\\% - 1.5\\%$ Carbon)**:\n   - *Properties*: Extremely hard, tough, less ductile, holds a sharp edge.\n   - *Uses*: Razor blades, drill bits, chisels, hammers, springs."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Stainless Steel: Corrosion-Resistant Alloy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "5. **Stainless Steel**:\n   - *Composition*: Iron ($74\\%$) + Chromium ($18\\%$) + Nickel ($8\\%$) + Carbon ($0.2\\%$).\n   - *Key Property*: **Rustless / Corrosion Resistant**.\n   - *Mechanism*: Chromium atoms react with atmospheric oxygen to form an invisible, ultra-thin, self-healing layer of **Chromium(III) Oxide ($\\text{Cr}_2\\text{O}_3$)** across the surface, completely blocking water and oxygen from touching iron.\n   - *Uses*: Kitchen cutlery, surgical instruments, watch cases, chemical plant reactors."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: Alloy Lattice Distortion Particle Model",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Particle diagram contrasting uniform sliding layers of pure iron atoms vs distorted iron lattice with carbon and chromium atoms locking layers in place.",
                        "caption": "Alloy Particle Model: Foreign atoms distort the iron atomic lattice, preventing cation layers from sliding easily under stress."
                    },
                    "asset_info": {
                        "title": "Alloy Lattice Distortion Diagram",
                        "description": "Particle-level illustration showing how carbon/chromium atoms distort iron lattice layers to increase hardness.",
                        "ai_instruction": "Create a 2-part particle diagram comparing uniform pure iron lattice layers sliding vs distorted alloy lattice with interstitial carbon atoms preventing layer slip."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Stainless Steel Corrosion Resistance",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What chemical element added to iron in Stainless Steel is primarily responsible for preventing it from rusting in moist air?",
                        "options": [
                            "Carbon, which consumes all oxygen in the metal.",
                            "Chromium, which forms an invisible self-healing oxide layer ($\\text{Cr}_2\\text{O}_3$) that shields iron from moisture.",
                            "Sulfur, which neutralizes water acid content.",
                            "Copper, which conducts rust away into the air."
                        ],
                        "answer": "B",
                        "explanation": "Chromium ($18\\%$) reacts with atmospheric oxygen to form an un-reactive, microscopic layer of chromium(III) oxide ($\text{Cr}_2\\text{O}_3$) over the steel. This barrier blocks moisture and oxygen from reaching iron atoms."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Steel Carbon Content & Hardness",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is High Carbon Steel ($1.0\\%$ Carbon) chosen for manufacturing drill bits and chisels rather than Mild Steel ($0.2\\%$ Carbon)?",
                        "options": [
                            "High carbon steel is much softer and easier to bend.",
                            "Higher carbon content distorts the iron lattice more severely, making the steel significantly harder and capable of holding a sharp cutting edge.",
                            "High carbon steel melts at room temperature during drilling.",
                            "Mild steel rusts 100 times faster than high carbon steel."
                        ],
                        "answer": "B",
                        "explanation": "Increasing the carbon percentage from $0.2\\%$ to $1.0\\%$ introduces more interstitial carbon atoms into the iron lattice. This creates greater lattice distortion, drastically increasing hardness and wear resistance needed for heavy cutting tools."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Uses of Iron Alloys\n- **Lattice Distortion**: Foreign atoms distort pure iron layers, stopping sliding and increasing hardness.\n- **Pig Iron ($3.5-4.5\\% \\text{ C}$)**: Brittle; used for drain covers, engine blocks.\n- **Wrought Iron ($<0.1\\% \\text{ C}$)**: Soft, malleable; used for decorative gates, chains.\n- **Mild Steel ($0.1-0.25\\% \\text{ C}$)**: Ductile; used for car bodies, girders.\n- **High Carbon Steel ($0.5-1.5\\% \\text{ C}$)**: Hard; used for drill bits, blades.\n- **Stainless Steel ($18\\% \\text{ Cr}, 8\\% \\text{ Ni}$)**: $\\text{Cr}_2\\text{O}_3$ layer prevents rust; cutlery, surgical tools."
                    }
                }
            ]
        },

        115: {
            "title": "Environmental Effects of Metal Extraction",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Introduction: Environmental Effects of Extraction",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will evaluate the environmental footprint of metallurgy—including open-cast mining habitat destruction, acid rain from $\\text{SO}_2$, global warming from $\\text{CO}_2$, toxic tailings, and how recycling saves up to $95\\%$ energy."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "1. Mining Land Degradation & Toxic Tailings",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Extracting metals provides essential society materials, but leaves a significant ecological footprint:\n\n1. **Open-Cast Mining & Habitat Destruction**:\n   - Stripping topsoil and vegetation creates massive open pits, leading to severe soil erosion, landslides, and loss of biodiversity.\n\n2. **Toxic Waste Tailings & Red Mud**:\n   - Physical ore washing and chemical leaching generate millions of tons of waste slurry (tailings).\n   - *Example*: The Bayer Process for aluminium produces alkaline **Red Mud** containing insoluble $\\text{Fe}_2\\text{O}_3$ and residual $\\text{NaOH}$. If tailing dams collapse, toxic red mud pollutes surrounding rivers and farmland."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "2. Air Pollution: Acid Rain & Greenhouse Gases",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "3. **Sulfur Dioxide ($\\text{SO}_2$) & Acid Rain**:\n   - Roasting sulfide ores ($\\text{ZnS}, \\text{PbS}, \\text{CuFeS}_2$) releases massive quantities of $\\text{SO}_2$ gas:\n     $$2\\text{MS}_{(s)} + 3\\text{O}_{2(g)} \\rightarrow 2\\text{MO}_{(s)} + 2\\text{SO}_{2(g)}$$\n   - In the atmosphere, $\\text{SO}_2$ oxidizes and dissolves in rainwater to form **Acid Rain** ($\\text{H}_2\\text{SO}_4$), which acidifies lakes, kills aquatic life, corrodes buildings, and defoliates forests.\n\n4. **Carbon Dioxide ($\\text{CO}_2$) & Global Warming**:\n   - Blast furnace reduction of iron and Hall-Héroult anode burning emit huge volumes of $\\text{CO}_2$ gas, contributing to global climate change."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "3. Pollution Control & The Recycling Solution",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "How do modern metallurgical plants mitigate environmental damage?\n\n1. **$\\text{SO}_2$ Scrubbing & Acid Production**:\n   - Flue gas scrubbers capture $\\text{SO}_2$ from furnace chimneys and pipe it into Contact Process plants to manufacture commercial Sulfuric Acid ($\\text{H}_2\\text{SO}_4$).\n\n2. **Land Reclamation**:\n   - Filling old open-cast mining pits with gangue waste, covering them with topsoil, and replanting indigenous trees.\n\n3. **Metal Recycling (The Aluminium Super-Saver)**:\n   - Recycling scrap metal eliminates mining, roasting, and smelting entirely!\n   - **Energy Comparison**: Extracting $1\\text{ kg}$ of fresh aluminium from bauxite via electrolysis consumes **$150\\text{ MJ}$** of electrical energy. Melting and recycling $1\\text{ kg}$ of scrap aluminium consumes only **$7.5\\text{ MJ}$**!\n   - **Recycling scrap aluminium saves $95\\%$ of the energy required for primary extraction!**"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Diagram: SO2 Flue Gas Scrubber & Recycling Cycle",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram showing SO2 gas scrubber converting roasting emissions to H2SO4 alongside bar chart comparing 100% bauxite energy vs 5% scrap aluminium energy.",
                        "caption": "Environmental Mitigation: SO2 scrubbers eliminate acid rain emissions while recycling saves 95% of extraction energy."
                    },
                    "asset_info": {
                        "title": "Metallurgical Environmental Protection Flow",
                        "description": "Schematic highlighting SO2 gas conversion to H2SO4 acid and energy conservation bar chart for aluminium recycling.",
                        "ai_instruction": "Create an environmental summary diagram showing furnace chimney SO2 scrubbers feeding a sulfuric acid plant, and a 95% energy savings chart for Al recycling."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Understanding Check: Acid Rain Source in Metallurgy",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which atmospheric pollutant gas released during the roasting of sulfide metal ores (such as Galena or Copper Pyrites) is directly responsible for causing acid rain?",
                        "options": [
                            "Carbon monoxide ($\\text{CO}$)",
                            "Sulfur dioxide ($\\text{SO}_2$)",
                            "Methane ($\\text{CH}_4$)",
                            "Chlorine gas ($\\text{Cl}_2$)"
                        ],
                        "answer": "B",
                        "explanation": "Roasting sulfide ores oxidizes sulfur to sulfur dioxide gas ($2\\text{MS} + 3\\text{O}_2 \\rightarrow 2\\text{MO} + 2\\text{SO}_2$). In the atmosphere, $\\text{SO}_2$ reacts with water vapor and oxygen to form sulfuric acid rain ($2\\text{SO}_2 + \\text{O}_2 + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{H}_2\\text{SO}_4$)."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Understanding Check: Energy Conservation in Recycling",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is recycling scrap aluminium beverage cans considered extremely environmentally beneficial compared to extracting fresh aluminium metal from Bauxite ore?",
                        "options": [
                            "Scrap aluminium contains more electrons than fresh aluminium.",
                            "Recycling scrap aluminium requires only $5\\%$ of the electrical energy needed to extract fresh aluminium from Bauxite by electrolysis.",
                            "Recycling aluminium produces pure oxygen gas that cleans polluted air.",
                            "Bauxite ore is completely extinct on Earth."
                        ],
                        "answer": "B",
                        "explanation": "Electrolyzing alumina in cryolite requires massive continuous electric currents at $950^\\circ\\text{C}$ ($150\\text{ MJ/kg}$). Melting scrap aluminium requires only low thermal heat ($7.5\\text{ MJ/kg}$), saving $95\\%$ of energy and dramatically reducing carbon footprint."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Summary & Key Takeaways",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Environmental Effects of Metallurgy\n- **Land Damage**: Open-cast mining causes erosion, deforestation, toxic red mud tailings.\n- **Acid Rain**: $\\text{SO}_2$ from sulfide roasting forms $\\text{H}_2\\text{SO}_4$ rain; mitigated by flue gas scrubbers making $\\text{H}_2\\text{SO}_4$.\n- **Greenhouse Gases**: $\\text{CO}_2$ from coke combustion & anode burning.\n- **Aluminium Recycling**: Saves **$95\\%$** of the energy needed for primary extraction from Bauxite."
                    }
                }
            ]
        }
    }

    # Execute database updates for all 13 lessons
    for lesson_id, data in topic_data.items():
        try:
            lesson = Lesson.objects.get(id=lesson_id, topic=topic)
            print(f"Refactoring Lesson {lesson.id}: {lesson.title}...")
            
            # Clear old blocks and assets
            LessonBlock.objects.filter(lesson=lesson).delete()
            LessonAsset.objects.filter(lesson=lesson).delete()
            
            for order, card in enumerate(data["cards"], start=1):
                block_id = f"block_{lesson.id}_{order}_{uuid.uuid4().hex[:6]}"
                b = LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=block_id,
                    order=order,
                    page_number=card["page_number"],
                    page_title=card["page_title"],
                    block_type=card["block_type"],
                    component_type=card["component_type"],
                    component_order=order,
                    title=card["page_title"],
                    content=card["content"]
                )
                
                # Check if asset info exists
                if "asset_info" in card:
                    info = card["asset_info"]
                    LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="diagram",
                        source_type="uploaded",
                        storage_type="local",
                        status="pending",
                        title=info["title"],
                        description=info["description"],
                        metadata={"ai_instruction": info["ai_instruction"], "block_id": b.block_id}
                    )
            
            lesson.status = "published"
            lesson.save()
            print(f"  Successfully refactored Lesson {lesson.id} with {len(data['cards'])} cards and assets.")
        except Lesson.DoesNotExist:
            print(f"Lesson ID {lesson_id} not found in database!")

if __name__ == "__main__":
    run_qa_refactor()
