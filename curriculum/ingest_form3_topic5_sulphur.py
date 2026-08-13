import os
import sys
import uuid
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def ingest_form3_topic5_sulphur():
    print("================================================================================")
    print("Starting VLearn Form 3 Chemistry Batch 5 Ingestion: Sulphur & Compounds (5.1-5.5)")
    print("================================================================================")

    # 1. Verify Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        curriculum = Curriculum.objects.create(name="844", description="Kenyan 8-4-4 Secondary Curriculum")

    grade, _ = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Form 3",
        defaults={"level": 3, "description": "Form 3 Secondary Level"}
    )

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Chemistry",
        defaults={"description": "Form 3 Chemistry (KLB Syllabus)"}
    )

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 5: Sulphur and its Compounds",
        defaults={
            "description": "Comprehensive study of sulphur extraction (Frasch process), allotropes, heating behaviour, sulphur(IV) oxide, the Contact process for sulphuric(VI) acid, hydrogen sulphide, and environmental acid rain mitigation.",
            "order": 5
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name} (Grade: {grade.name})")

    # 2. Define Clean, Student-Facing Content Data Dictionary (Modules 5.1 - 5.5)
    modules_data = [
        {
            "unit_name": "Module 5.1: Extraction of Sulphur (Frasch Process) and Allotropes",
            "unit_order": 1,
            "lesson_title": "Extraction of Sulphur (Frasch Process) and Allotropes",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Mining Without Digging Shafts",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore the underground extraction of sulphur using the Frasch process, and study the crystalline allotropes (rhombic and monoclinic sulphur) and non-crystalline plastic sulphur."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of Deep Underground Mining",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Beneath layers of loose sand and wet clay hundreds of metres underground lie massive deposits of elemental sulphur.\n\nTraditional human shaft mining would trigger catastrophic cave-ins. The solution is an engineering triumph known as the **Frasch Process**, which exploits sulphur's relatively low melting point ($113^\\circ\\text{C}-119^\\circ\\text{C}$) to liquefy and pump the mineral to the surface."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Crystalline Allotropes and Molecular Structure",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Puckered $S_8$ Crown Molecule:\nAt room temperature, sulphur exists as crown-shaped, puckered 8-atom rings ($S_8$). Packing these rings into different geometric lattices creates distinct **allotropes**:\n\n* **Rhombic Sulphur ($\\alpha$-sulphur)**:\n  - Octahedral crystals (double pyramid).\n  - Bright yellow, density $2.06\\text{ g cm}^{-3}$, melting point $113^\\circ\\text{C}$.\n  - Stable below $96^\\circ\\text{C}$.\n\n* **Monoclinic Sulphur ($\\beta$-sulphur)**:\n  - Needle-like crystals (hexagonal prisms).\n  - Pale yellow, density $1.98\\text{ g cm}^{-3}$, melting point $119^\\circ\\text{C}$.\n  - Stable between $96^\\circ\\text{C}$ and $119^\\circ\\text{C}$."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Frasch Concentric Pipe System",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Diagram illustrating the three concentric pipes of the Frasch sulphur extraction process.",
                        "instruction": "Three concentric vertical pipes sunk into underground sulphur bed: Outermost pipe (15 cm) pumping superheated water at 170°C (10 atm), innermost pipe (2 cm) pumping hot compressed air at 15 atm, and middle pipe (8 cm) carrying upward molten sulphur froth to surface cooling tanks.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    },
                    "asset_info": {
                        "title": "Frasch Process Concentric Pipes",
                        "description": "Cross-sectional diagram of the three concentric pipes used in the Frasch Process.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Transition Temperature & Allotropic Interconversion",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Transition Temperature ($96^\\circ\\text{C}$)",
                        "content": "### Definition\nThe specific temperature at which one allotropic form of an element interconverts reversibly into another:\n$$\\text{Rhombic Sulphur } (\\alpha\\text{-S}) \\underset{< 96^\\circ\\text{C}}{\\overset{> 96^\\circ\\text{C}}{\\rightleftharpoons}} \\text{ Monoclinic Sulphur } (\\beta\\text{-S})$$\n\n* **Below $96^\\circ\\text{C}$**: Monoclinic crystals slowly reorganize their crystal lattice to form rhombic crystals.\n* **Above $96^\\circ\\text{C}$**: Rhombic crystals transform into needle-shaped monoclinic crystals."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Volcanic Sulphur Deposits in East Africa",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Volcanism in the Great Rift Valley\nIn Kenya, sulphur deposits and volcanic fumaroles are found around **Mount Longonot, Menengai Crater, and Olkaria in Naivasha**.\n\nWhile shallow volcanic crusts can be mined by surface quarrying, deep underground sulphur deposits globally rely on the Frasch Process to yield over 99.5% pure solid sulphur without smelting or refining."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Energy Requirements in Frasch Extraction",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the minimum heat energy required to melt $1.0\\text{ kg}$ ($1000\\text{ g}$) of solid rhombic sulphur initially at ground temperature ($25^\\circ\\text{C}$) to molten liquid at its melting point ($113^\\circ\\text{C}$). ($c = 0.71\\text{ J g}^{-1\\circ}\\text{C}^{-1}, L_f = 45.0\\text{ J g}^{-1}$)",
                        "steps": [
                            "**Step 1: Heating Solid Sulphur ($25^\\circ\\text{C} \\rightarrow 113^\\circ\\text{C}$)**:\n$$\\Delta T = 113 - 25 = 88^\\circ\\text{C}$$\n$$Q_1 = m \\times c \\times \\Delta T = 1000\\text{ g} \\times 0.71\\text{ J g}^{-1\\circ}\\text{C}^{-1} \\times 88^\\circ\\text{C} = 62,480\\text{ J} = 62.48\\text{ kJ}$$",
                            "**Step 2: Latent Heat of Fusion at $113^\\circ\\text{C}$**:\n$$Q_2 = m \\times L_f = 1000\\text{ g} \\times 45.0\\text{ J g}^{-1} = 45,000\\text{ J} = 45.00\\text{ kJ}$$",
                            "**Step 3: Total Energy Required**:\n$$Q_T = Q_1 + Q_2 = 62.48 + 45.00 = \\mathbf{107.48\\text{ kJ}}$$\n*Interpretation*: The superheated water at $170^\\circ\\text{C}$ must deliver at least $107.48\\text{ kJ}$ per kilogram of underground sulphur."
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Compressed Air Does Not Burn Sulphur",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does compressed air combust the sulphur underground?\nNo! The hot compressed air ($15\\text{ atm}$) does not burn the sulphur into sulphur dioxide.\n\nIts sole function is physical aeration: whipping the heavy molten liquid into a lightweight, low-density foam (froth) that easily ascends the middle pipe under pressure."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Sulphur Extraction",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is water pumped down the outermost pipe in the Frasch Process heated to 170°C at 10 atmospheres instead of 100°C?",
                        "options": [
                            "To vaporize the water into steam to power underground turbines",
                            "Because sulphur melts between 113°C and 119°C, so water at 100°C cannot melt it",
                            "To oxidise the underground sulphur to sulphur(IV) oxide gas",
                            "To dissolve the underground clay and sand layers"
                        ],
                        "answer": "B",
                        "explanation": "Sulphur has a melting point of 113°C-119°C. Liquid water at 100°C is below this melting point and cannot melt the mineral. Superheating it to 170°C under 10 atm pressure keeps it liquid while ensuring rapid thermal melting."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Extraction & Allotropes",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Sulphur Extraction\n- **Allotropes**: Rhombic (octahedral, stable $<96^\\circ\\text{C}$) and Monoclinic (needle-like, stable $96^\\circ-119^\\circ\\text{C}$).\n- **Transition Temperature**: $96^\\circ\\text{C}$ is the reversible allotropic boundary.\n- **Frasch System**: Superheated water ($170^\\circ\\text{C}$) in outer pipe melts sulphur; hot compressed air ($15\\text{ atm}$) in inner pipe lifts molten froth up middle pipe."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 5.2: Physical and Chemical Properties of Sulphur",
            "unit_order": 2,
            "lesson_title": "Physical and Chemical Properties of Sulphur",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Unique Behavior of Molten Sulphur",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will observe the physical and chemical properties of sulphur, exploring its anomalous temperature-viscosity behavior when melted and its combination reactions with metals and non-metals."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Anomalous Viscosity of Liquid Sulphur",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When solid yellow sulphur is heated gently, it melts at $113^\\circ\\text{C}$ into a clear, runny amber liquid.\n\nRemarkably, heating it further past $160^\\circ\\text{C}$ causes the liquid to darken into a thick, reddish-black jelly so viscous that the test-tube can be inverted without a single drop flowing out. Near its boiling point ($444^\\circ\\text{C}$), it thins out into a runny liquid again."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Molecular Mechanism of Heating Transformations",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Microscopic Structural Stages:\n1. **$113^\\circ\\text{C}-160^\\circ\\text{C}$ (Mobile Liquid)**: Weak intermolecular van der Waals forces between individual $S_8$ rings break, allowing rings to roll past one another freely.\n2. **$160^\\circ\\text{C}-200^\\circ\\text{C}$ (Viscosity Spike)**: Thermal energy breaks covalent bonds within $S_8$ rings, forming open chains with free-radical ends. These link into giant, tangled polymer chains ($S_x$, $>100,000\\text{ atoms}$) that entangle like spaghetti.\n3. **$>200^\\circ\\text{C}-444^\\circ\\text{C}$ (Mobile Liquid Again)**: Intense thermal agitation snaps the long covalent polymer chains into shorter, mobile fragments.\n4. **$444^\\circ\\text{C}$ (Boiling)**: Vapour consists of $S_8, S_6,$ and $S_2$ molecules."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Chemical Reactions with Oxygen and Metals",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Combination Reactions of Sulphur",
                        "content": "### 1. Combustion in Oxygen:\nSulphur burns with a brilliant blue flame forming choking sulphur(IV) oxide ($SO_2$) and traces of $SO_3$:\n$$\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$$\n\n### 2. Combination with Metals:\n* **With Iron**: Highly exothermic reaction; once initiated, a bright red glow spreads spontaneously through the solid mass forming black iron(II) sulphide:\n  $$\\text{Fe}(s) + \\text{S}(s) \\xrightarrow{\\text{heat}} \\text{FeS}(s) \\quad (\\Delta H < 0)$$\n* **With Copper**: Forms blue-black copper(II) sulphide ($\\text{CuS}$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Redox Reactions with Concentrated Acids",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Sulphur does not react with dilute acids or non-oxidising acids like $HCl$. However, it is oxidized by hot concentrated oxidising acids:\n\n* **With Hot Concentrated Nitric(V) Acid**:\n  Oxidises sulphur to sulphuric(VI) acid while evolving brown $NO_2$ gas:\n  $$\\text{S}(s) + 6\\text{HNO}_3(aq) \\rightarrow \\text{H}_2\\text{SO}_4(aq) + 6\\text{NO}_2(g) + 2\\text{H}_2\\text{O}(l)$$\n  *Verification*: Adding $BaCl_2(aq)$ yields a white precipitate of $BaSO_4(s)$.\n\n* **With Hot Concentrated Sulphuric(VI) Acid**:\n  $$\\text{S}(s) + 2\\text{H}_2\\text{SO}_4(l) \\rightarrow 3\\text{SO}_2(g) + 2\\text{H}_2\\text{O}(l)$$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Vulcanisation of Rubber and Agricultural Fungicides",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Industrial and Farm Applications\n* **Vulcanisation of Rubber**: Natural rubber is soft and sticky. Heating it with sulphur creates covalent cross-links between polymer chains, producing durable, elastic rubber for vehicle tyres and industrial belts.\n* **Crop Protection**: Sulphur dust is widely sprayed across tea, coffee, and horticultural farms in **Kiambu, Kericho, and Naivasha** to eradicate fungal powdery mildew and mites."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Balancing Redox Half-Equations for Sulphur",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Derive the balanced overall ionic equation for the oxidation of sulphur by hot concentrated nitric(V) acid.",
                        "steps": [
                            "**Step 1: Oxidation Half-Equation ($S^0 \\rightarrow S^{+6}$)**:\n$$\\text{S}(s) + 4\\text{H}_2\\text{O}(l) \\rightarrow \\text{SO}_4^{2-}(aq) + 8\\text{H}^+(aq) + 6e^-$$",
                            "**Step 2: Reduction Half-Equation ($N^{+5} \\rightarrow N^{+4}$)**:\n$$\\text{NO}_3^-(aq) + 2\\text{H}^+(aq) + e^- \\rightarrow \\text{NO}_2(g) + \\text{H}_2\\text{O}(l)$$",
                            "**Step 3: Equalize Electrons ($6e^-$)**:\n$$6\\text{NO}_3^-(aq) + 12\\text{H}^+(aq) + 6e^- \\rightarrow 6\\text{NO}_2(g) + 6\\text{H}_2\\text{O}(l)$$",
                            "**Step 4: Combine and Simplify**:\n$$\\text{S}(s) + 6\\text{NO}_3^-(aq) + 4\\text{H}^+(aq) \\rightarrow \\text{SO}_4^{2-}(aq) + 6\\text{NO}_2(g) + 2\\text{H}_2\\text{O}(l)$$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Viscosity Rises With Temperature",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Do liquids always become thinner when heated?\nIn everyday life (like water or cooking oils), liquids thin out as temperature rises.\n\nSulphur is a dramatic exception: between $160^\\circ\\text{C}$ and $200^\\circ\\text{C}$, the $S_8$ rings open and polymerise into giant entangled chains, causing viscosity to skyrocket before thermal fragmentation thins it out near $444^\\circ\\text{C}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Sulphur Properties",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why does hydrochloric acid (HCl) fail to react with solid sulphur powder even when heated?",
                        "options": [
                            "Sulphur forms an insoluble chloride layer",
                            "Hydrochloric acid is a non-oxidising acid and cannot accept electrons from sulphur",
                            "Hydrochloric acid is too volatile and boils before reacting",
                            "Sulphur sublimes into gas before acid contact"
                        ],
                        "answer": "B",
                        "explanation": "Oxidizing sulphur requires a strong oxidising agent (like hot conc. $HNO_3$ or conc. $H_2SO_4$). Hydrochloric acid is non-oxidising and cannot oxidize sulphur from oxidation state 0 to +4 or +6."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Properties of Sulphur",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Sulphur Properties\n- **Viscosity Curve**: Mobile liquid ($113^\\circ\\text{C}$) $\\rightarrow$ viscous polymer jelly ($160^\\circ-200^\\circ\\text{C}$) $\\rightarrow$ mobile liquid ($>200^\\circ\\text{C}$).\n- **Exothermic Combination**: Burns with blue flame ($SO_2$); reacts with $Fe$ with self-sustaining red glow ($FeS$).\n- **Oxidation**: Hot conc. $HNO_3$ oxidises $S$ to $H_2SO_4$ with brown $NO_2$ gas."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 5.3: Sulphur(IV) Oxide: Preparation, Properties, and Reactions",
            "unit_order": 3,
            "lesson_title": "Sulphur(IV) Oxide: Preparation, Properties, and Reactions",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Reversible Bleaching Agent",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will study the laboratory preparation and properties of sulphur(IV) oxide ($\\text{SO}_2$), contrasting its temporary reduction bleaching with permanent oxidation bleaching."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Bleaching That Creeps Back Over Time",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Placing a damp red flower petal into a gas jar of **sulphur(IV) oxide ($SO_2$)** bleaches the petal to white within seconds.\n\nHowever, leaving that bleached petal in open sunlight for several days causes the reddish colour to slowly return! Unlike chlorine (which bleaches permanently by oxidation), $SO_2$ bleaches **temporarily by reduction**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Synthesis and Bleaching Mechanism",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### 1. Laboratory Preparation:\nReacting sodium sulphite with dilute hydrochloric acid:\n$$\\text{Na}_2\\text{SO}_3(s) + 2\\text{HCl}(aq) \\rightarrow 2\\text{NaCl}(aq) + \\text{H}_2\\text{O}(l) + \\text{SO}_2(g)$$\n* **Drying**: Dried by bubbling through concentrated sulphuric(VI) acid.\n* **Collection**: Collected by **downward delivery** (denser than air, highly soluble in water).\n\n### 2. The Bleaching Mechanism (Reduction):\n$SO_2$ dissolves in water forming sulphurous acid ($H_2SO_3$), which removes oxygen from the dye:\n$$\\text{H}_2\\text{SO}_3(aq) + \\text{Dye}(\\text{coloured}) \\rightarrow \\text{H}_2\\text{SO}_4(aq) + \\text{Bleached Dye}(\\text{colourless})$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Reducing and Oxidising Properties of SO2",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Redox Behavior of SO2",
                        "content": "### 1. Powerful Reducing Actions:\n* **Acidified $KMnO_4$**: Decolourises purple solution to colourless ($Mn^{2+}$).\n* **Acidified $K_2Cr_2O_7$**: Turns orange solution to **green ($Cr^{3+}$)** (Confirmatory test for $SO_2$!).\n* **Bromine Water**: Decolourises reddish-brown $Br_2(aq)$ to colourless $Br^-$.\n* **Iron(III) Chloride**: Reduces yellow-brown $Fe^{3+}$ to pale green $Fe^{2+}$.\n\n### 2. Oxidising Actions:\n* **With $H_2S$**: Forms yellow deposit of sulphur in presence of moisture:\n  $$2\\text{H}_2\\text{S}(g) + \\text{SO}_2(g) \\xrightarrow{\\text{Moisture}} 3\\text{S}(s) + 2\\text{H}_2\\text{O}(l)$$\n* **With Burning Magnesium**: Continues burning to form white $MgO$ and yellow specks of sulphur ($2\\text{Mg} + \\text{SO}_2 \\rightarrow 2\\text{MgO} + \\text{S}$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Distinguishing Sulphite and Sulphate Ions",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Sulphate vs Sulphite Identification Tree",
                        "content": "### Two-Step Analytical Test:\n1. **Step 1 (Precipitation)**: Add $BaCl_2(aq)$ or $Ba(NO_3)_2(aq)$. Both form a white precipitate ($BaSO_4$ or $BaSO_3$).\n2. **Step 2 (Acidification)**: Add dilute $HCl(aq)$:\n   - **Sulphate ($SO_4^{2-}$)**: White precipitate **does NOT dissolve**.\n   - **Sulphite ($SO_3^{2-}$)**: White precipitate **dissolves completely with effervescence**, releasing choking $SO_2$ gas:\n     $$\\text{BaSO}_3(s) + 2\\text{H}^+(aq) \\rightarrow \\text{Ba}^{2+}(aq) + \\text{SO}_2(g) + \\text{H}_2\\text{O}(l)$$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Industrial Bleaching & Food Preservation",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Wood Pulp and Fruit Preservation\n* **Paper Industry**: $SO_2$ is used to bleach delicate wood pulp into white writing paper without degrading cellulose fibers. Re-oxidation explains why old newspapers turn yellow-brown over time.\n* **Food Additive**: Regulated amounts of $SO_2$ are added to commercial fruit juices, jams, and dried fruits across East Africa to inhibit bacterial growth and prevent enzymatic browning."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Gas Volume from Sulphite Reaction",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of sulphur(IV) oxide ($SO_2$) gas evolved at s.t.p. when $12.6\\text{ g}$ of sodium sulphite ($Na_2SO_3$) reacts with excess dilute hydrochloric acid ($Na=23, S=32, O=16$, Molar Gas Volume $= 22.4\\text{ dm}^3\\text{ mol}^{-1}$).",
                        "steps": [
                            "**Step 1: Balanced Equation**:\n$$\\text{Na}_2\\text{SO}_3(s) + 2\\text{HCl}(aq) \\rightarrow 2\\text{NaCl}(aq) + \\text{H}_2\\text{O}(l) + \\text{SO}_2(g)$$",
                            "**Step 2: Formula Mass and Moles**:\n- $\\text{R.F.M. of } Na_2SO_3 = 2(23.0) + 32.0 + 3(16.0) = 126.0\\text{ g mol}^{-1}$\n- $\\text{Moles} = \\frac{12.6\\text{ g}}{126.0\\text{ g mol}^{-1}} = 0.10\\text{ moles}$",
                            "**Step 3: Calculate Gas Volume at S.T.P.**:\n- Stoichiometric ratio $Na_2SO_3 : SO_2 = 1 : 1 \\implies 0.10\\text{ moles } SO_2$\n- $\\text{Volume} = 0.10\\text{ mol} \\times 22.4\\text{ dm}^3/\\text{mol} = \\mathbf{2.24\\text{ dm}^3} \\quad (2240\\text{ cm}^3)$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Chlorine vs Sulphur Dioxide Bleaching",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does colour return after SO2 bleaching but not chlorine bleaching?\n* **Chlorine**: Bleaches by **oxidation** ($Cl_2 + H_2O + \\text{Dye} \\rightarrow 2HCl + [\\text{Dye}+O]$). The added oxygen creates a permanent chemical change.\n* **Sulphur Dioxide**: Bleaches by **reduction**. Exposure to atmospheric oxygen gradually re-oxidises the dye, restoring its original colour."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Sulphur(IV) Oxide",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "When sulphur(IV) oxide gas is bubbled into acidified potassium dichromate(VI) solution, the color changes from orange to green. What transition causes this change?",
                        "options": [
                            "Orange dichromate(VI) ions are reduced to green chromium(III) ions",
                            "Sulphur(IV) ions are reduced to yellow elemental sulphur",
                            "Sulphurous acid is dehydrated to dinitrogen oxide",
                            "Chromium(II) ions are oxidised to chromium(VI) ions"
                        ],
                        "answer": "A",
                        "explanation": "Sulphur(IV) oxide is a strong reducing agent. It reduces orange dichromate(VI) ions ($Cr_2O_7^{2-}$, where Cr is +6) to green chromium(III) ions ($Cr^{3+}$, where Cr is +3)."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Sulphur(IV) Oxide",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Sulphur(IV) Oxide\n- **Preparation**: $Na_2SO_3 + 2HCl \\rightarrow 2NaCl + H_2O + SO_2$ (downward delivery).\n- **Diagnostic Test**: Turns acidified $K_2Cr_2O_7$ from orange to green ($Cr^{3+}$).\n- **Bleaching**: Temporary reduction bleaching (sulphurous acid removes oxygen from dye).\n- **Analysis**: $Ba^{2+}$ white precipitate dissolves in dilute $HCl$ for sulphite ($SO_3^{2-}$), but remains insoluble for sulphate ($SO_4^{2-}$)."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 5.4: Sulphuric(VI) Acid and the Contact Process",
            "unit_order": 4,
            "lesson_title": "Sulphuric(VI) Acid and the Contact Process",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The King of Chemicals",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master the industrial Contact process for manufacturing sulphuric(VI) acid ($\\text{H}_2\\text{SO}_4$), and compare the acid's dilute versus concentrated oxidising and dehydrating properties."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Economic Barometer of Modern Industry",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Sulphuric(VI) acid ($H_2SO_4$) is often hailed as the \"King of Chemicals\" because its annual consumption directly measures a nation's industrial output.\n\nPouring concentrated sulphuric acid onto white table sugar causes a violent dehydration: a steaming, expanding column of black elemental carbon erupts from the beaker. Today, we study the Contact Process used to manufacture this indispensable compound."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The 5 Stages of the Contact Process",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Contact Process Flow",
                        "content": "### 1. Burner: Combustion of Sulphur\n$$\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$$\n\n### 2. Purification & Drying:\nDust particles are scrubbed electrostatically to prevent **catalyst poisoning**. Gas is dried with concentrated $H_2SO_4$.\n\n### 3. Catalytic Oxidation ($450^\\circ\\text{C}, 2-3\\text{ atm}$):\n$$2\\text{SO}_2(g) + \\text{O}_2(g) \\underset{V_2O_5}{\\rightleftharpoons} 2\\text{SO}_3(g) \\quad (\\Delta H = -197\\text{ kJ mol}^{-1})$$\n* **Catalyst**: Vanadium(V) oxide ($V_2O_5$) is preferred over platinum (cheaper, resistant to poisoning).\n\n### 4. Absorption Tower (Oleum Formation):\n$$\\text{SO}_3(g) + \\text{H}_2\\text{SO}_4(l) \\rightarrow \\text{H}_2\\text{S}_2\\text{O}_7(l) \\quad (\\text{Oleum})$$\n\n### 5. Controlled Dilution:\n$$\\text{H}_2\\text{S}_2\\text{O}_7(l) + \\text{H}_2\\text{O}(l) \\rightarrow 2\\text{H}_2\\text{SO}_4(l) \\quad (98\\%\\text{ Pure Acid})$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Why Direct Dissolution in Water is Prohibited",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Preventing Acid Mist Aerosol Explosions:\nDissolving $SO_3$ gas directly into water is extraordinarily exothermic. The intense heat boils the water instantly, generating a dense, choking aerosol mist of sulphuric acid droplets that escapes into the atmosphere and cannot be condensed safely.\n\nDissolving $SO_3$ in concentrated $H_2SO_4$ to produce oleum ($H_2S_2O_7$) bypasses this hazard cleanly."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Dehydrating & Oxidising Actions of Concentrated Acid",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Reactions of Concentrated H2SO4",
                        "content": "### 1. Powerful Dehydrating Agent:\n* **Sugar (Sucrose)**: Strips hydrogen and oxygen ($2:1$ ratio), leaving porous black carbon:\n  $$\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}(s) \\xrightarrow{\\text{conc. } H_2SO_4} 12\\text{C}(s) + 11\\text{H}_2\\text{O}(l)$$\n* **Hydrated Copper(II) Sulphate**: Blue crystals turn into white anhydrous powder:\n  $$\\text{CuSO}_4\\cdot5\\text{H}_2\\text{O}(s) \\xrightarrow{\\text{conc. } H_2SO_4} \\text{CuSO}_4(s) + 5\\text{H}_2\\text{O}(l)$$\n\n### 2. Hot Oxidising Agent:\n* **With Copper**: $\\text{Cu} + 2\\text{H}_2\\text{SO}_4 \\rightarrow \\text{CuSO}_4 + \\text{SO}_2 + 2\\text{H}_2\\text{O}$\n* **With Carbon**: $\\text{C} + 2\\text{H}_2\\text{SO}_4 \\rightarrow \\text{CO}_2 + 2\\text{SO}_2 + 2\\text{H}_2\\text{O}$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Industrial Manufacture in Thika & Acid Accumulators",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Industrial Infrastructure in Kenya\n* **Kel Chemicals in Thika**: Large-scale Contact plant manufacturing sulphuric acid used to produce ammonium sulphate and calcium phosphate fertilisers for agricultural regions in the Rift Valley and Central Kenya.\n* **Automotive Lead-Acid Batteries**: Standard vehicle batteries use a 35% dilute sulphuric acid solution as the active electrolyte."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Limiting Reactant Calculation with Sulphuric Acid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of carbon(IV) oxide ($CO_2$) gas produced at r.t.p. when $5.0\\text{ g}$ of anhydrous sodium carbonate ($Na_2CO_3$) reacts with $100\\text{ cm}^3$ of $0.5\\text{ M}$ dilute sulphuric(VI) acid ($Na=23, C=12, O=16, H=1, S=32$, Molar Volume $= 24.0\\text{ dm}^3$).",
                        "steps": [
                            "**Step 1: Balanced Equation**:\n$$\\text{Na}_2\\text{CO}_3(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{Na}_2\\text{SO}_4(aq) + \\text{H}_2\\text{O}(l) + \\text{CO}_2(g)$$",
                            "**Step 2: Determine Limiting Reactant**:\n- Moles of $Na_2CO_3 = \\frac{5.0}{106.0} = 0.0472\\text{ mol}$\n- Moles of $H_2SO_4 = 0.5\\text{ mol/dm}^3 \\times 0.100\\text{ dm}^3 = 0.050\\text{ mol}$\n- $Na_2CO_3$ is the limiting reactant ($0.0472 < 0.050$).",
                            "**Step 3: Calculate Volume of $CO_2$ at r.t.p.**:\n- Mole ratio $Na_2CO_3 : CO_2 = 1 : 1 \\implies 0.0472\\text{ mol } CO_2$\n- $\\text{Volume} = 0.0472\\text{ mol} \\times 24.0\\text{ dm}^3/\\text{mol} = \\mathbf{1.133\\text{ dm}^3} \\quad (1132.8\\text{ cm}^3)$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Dilute H2SO4 Stops on Limestone",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does limestone stop reacting with dilute H2SO4 after a few seconds?\nAdding dilute $HCl$ dissolves limestone ($CaCO_3$) completely because $CaCl_2$ is soluble.\n\nHowever, dilute $H_2SO_4$ forms **calcium sulphate ($CaSO_4$)**, which is insoluble and coats the unreacted carbonate particles like an impermeable shield, stopping further acid contact."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Sulphuric(VI) Acid",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "During the Contact Process, why is sulphur(VI) oxide (SO3) dissolved in concentrated sulphuric acid to form oleum rather than directly in water?",
                        "options": [
                            "The vanadium(V) oxide catalyst requires oleum to remain active",
                            "Direct reaction with water is violently exothermic and creates an uncontrollable acid mist",
                            "Sulphur(VI) oxide is insoluble in pure water",
                            "Water reverses the oxidation reaction"
                        ],
                        "answer": "B",
                        "explanation": "Dissolving $SO_3$ directly in water generates intense heat that vaporizes water into a dense, dangerous aerosol acid mist that is difficult to condense safely. Oleum formation avoids this hazard."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Contact Process & H2SO4",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Sulphuric(VI) Acid\n- **Contact Process**: $S \\rightarrow SO_2 \\xrightarrow{V_2O_5, 450^\\circ\\text{C}} SO_3 \\xrightarrow{\\text{conc. } H_2SO_4} \\text{Oleum } (H_2S_2O_7) \\xrightarrow{H_2O} 2H_2SO_4$.\n- **Concentrated Properties**: Powerful dehydrating agent (chars sucrose to carbon) and hot oxidising agent.\n- **Dilute Properties**: Strong dibasic acid; forms insoluble sulphate coatings on $CaCO_3$ and $PbCO_3$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 5.5: Hydrogen Sulphide and Sulphur-Based Environmental Pollution",
            "unit_order": 5,
            "lesson_title": "Hydrogen Sulphide and Sulphur-Based Environmental Pollution",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of Rotten Eggs and Acid Rain",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will investigate hydrogen sulphide ($\\text{H}_2\\text{S}$), its preparation and analytical metal sulphide precipitation tests, and examine sulphur dioxide emissions and acid rain prevention."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Rotten Eggs and Geothermal Steam",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Around swamps and geothermal vents like **Olkaria in Naivasha**, you encounter the pungent, putrid stench of rotten eggs.\n\nThis is **hydrogen sulphide ($H_2S$)**, a poisonous gas containing sulphur in its lowest oxidation state ($-2$). In the laboratory, it serves as a powerful reducing agent and a precise analytical tool for precipitating distinct metal sulphides."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Synthesis & Safe Drying Protocols",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Reaction of Iron(II) Sulphide with Dilute Acid:\n$$\\text{FeS}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{FeCl}_2(aq) + \\text{H}_2\\text{S}(g)$$\n\n* **Why Anhydrous $CaCl_2$ Drying is Mandatory**:\n  $H_2S$ is a strong reducing agent. Concentrated sulphuric acid ($H_2SO_4$) is an oxidising agent and would violently oxidise $H_2S$ to solid yellow sulphur ($H_2S + H_2SO_4 \\rightarrow S + SO_2 + 2H_2O$), destroying the product.\n* **Collection**: Collected over warm water (less soluble) or by downward delivery (denser than air)."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Reducing Action and Sulphur Deposition",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Reducing Properties of H2S",
                        "content": "Because sulphur is in its lowest oxidation state ($-2$), $H_2S$ loses electrons readily, forming a **yellow precipitate of elemental sulphur ($S^0$)** in almost all redox reactions:\n\n* **Acidified $KMnO_4$**: Decolourises purple to colourless with yellow sulphur deposit.\n* **Acidified $K_2Cr_2O_7$**: Turns orange to green ($Cr^{3+}$) with yellow sulphur deposit.\n* **Chlorine Gas**: Greenish-yellow gas turns colourless ($HCl$) with yellow sulphur deposit ($H_2S + Cl_2 \\rightarrow S + 2HCl$).\n* **Iron(III) Chloride**: Yellow-brown $Fe^{3+}$ reduced to pale green $Fe^{2+}$ with yellow sulphur."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Qualitative Metal Cation Precipitation",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Metal Sulphide Precipitates",
                        "content": "Bubbling $H_2S$ through aqueous metal salt solutions yields diagnostic insoluble precipitates:\n\n* **Lead(II) ($Pb^{2+}$)**: Forms dense **black precipitate of Lead(II) sulphide ($PbS$)**.\n* **Copper(II) ($Cu^{2+}$)**: Forms dense **black precipitate of Copper(II) sulphide ($CuS$)**.\n* **Zinc(II) ($Zn^{2+}$)**: Forms **white precipitate of Zinc sulphide ($ZnS$)**."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Acid Rain and Environmental Mitigation in Kenya",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Acid Rain and Geothermal Power Plants\n* **Acid Rain Chemistry**: Industrial $SO_2$ emissions oxidize to $SO_3$ and dissolve in clouds, dropping rain pH to $3.0-4.0$. This strips magnesium from leaf chlorophyll (**chlorosis**), leaches nutrients from soil, and corrodes stone buildings and metal bridges.\n* **Geothermal Scrubbing at Olkaria**: Geothermal steam vents in Naivasha release $H_2S$ and $SO_2$. Engineers spray alkaline calcium hydroxide slurries ($Ca(OH)_2$) in scrubbers to capture these gases as solid $CaSO_3$, protecting turbines and the surrounding ecosystem in Hell's Gate National Park."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Mass of Calcium Hydroxide for Scrubbing",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "An industrial chimney releases $4.8\\text{ kg}$ ($4800\\text{ g}$) of sulphur dioxide ($SO_2$) gas per hour. Calculate the mass of calcium hydroxide ($Ca(OH)_2$) required per hour to completely scrub this waste gas ($Ca=40, O=16, H=1, S=32$).",
                        "steps": [
                            "**Step 1: Balanced Neutralisation Equation**:\n$$\\text{Ca(OH)}_2(aq) + \\text{SO}_2(g) \\rightarrow \\text{CaSO}_3(s) + \\text{H}_2\\text{O}(l)$$",
                            "**Step 2: Calculate Moles of $SO_2$**:\n- Molar mass of $SO_2 = 32.0 + 2(16.0) = 64.0\\text{ g mol}^{-1}$\n- $\\text{Moles of } SO_2 = \\frac{4800\\text{ g}}{64.0\\text{ g mol}^{-1}} = 75.0\\text{ moles}$",
                            "**Step 3: Calculate Mass of $Ca(OH)_2$ Required**:\n- Mole ratio $Ca(OH)_2 : SO_2 = 1 : 1 \\implies 75.0\\text{ moles } Ca(OH)_2$\n- Molar mass of $Ca(OH)_2 = 40.0 + 2(16.0 + 1.0) = 74.0\\text{ g mol}^{-1}$\n- $\\text{Mass required} = 75.0\\text{ mol} \\times 74.0\\text{ g mol}^{-1} = 5550\\text{ g} = \\mathbf{5.55\\text{ kg}}$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Conc. H2SO4 Cannot Dry H2S",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why can't we dry H2S with concentrated sulphuric acid?\nEven though $H_2S$ is acidic, it is a powerful reducing agent ($S^{-2}$). Concentrated $H_2SO_4$ is an oxidising agent.\n\nBringing them together causes a violent redox reaction that oxidises $H_2S$ into solid yellow sulphur, destroying the gas. Anhydrous $CaCl_2$ must be used."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Hydrogen Sulphide & Pollution",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following drying agents is chemically appropriate for drying hydrogen sulphide gas in the laboratory?",
                        "options": [
                            "Concentrated sulphuric(VI) acid (H2SO4)",
                            "Anhydrous calcium chloride (CaCl2)",
                            "Calcium oxide (Quicklime, CaO)",
                            "Phosphorus(V) oxide (P2O5)"
                        ],
                        "answer": "B",
                        "explanation": "Hydrogen sulphide ($H_2S$) is a strong reducing agent. Concentrated sulphuric acid oxidises it to solid sulphur, and basic $CaO$ reacts with it. Anhydrous $CaCl_2$ is neutral and non-oxidising, drying the gas safely."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: H2S and Pollution",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: H2S & Pollution\n- **Preparation**: $FeS + 2HCl \\rightarrow FeCl_2 + H_2S$ (dried with anhydrous $CaCl_2$).\n- **Redox Action**: Powerful reducing agent; always deposits yellow elemental sulphur precipitate.\n- **Qualitative Analysis**: Forms black $PbS$, black $CuS$, and white $ZnS$ precipitates.\n- **Pollution Mitigation**: $SO_2$ causes acid rain and chlorosis; neutralised by alkaline industrial scrubbing with $Ca(OH)_2$."
                    }
                }
            ]
        }
    ]

    # 3. Execute Ingestion & Publishing for Each Module
    for m_data in modules_data:
        unit_name = m_data["unit_name"]
        unit_order = m_data["unit_order"]
        lesson_title = m_data["lesson_title"]
        cards = m_data["cards"]

        print(f"\n--- Ingesting {unit_name} ---")

        # Create or update LearningUnit
        unit, unit_created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=unit_name,
            defaults={"order": unit_order, "description": f"Curriculum module for {lesson_title}"}
        )
        if not unit_created:
            unit.order = unit_order
            unit.save()
        print(f"  Learning Unit: {unit.name} (ID: {unit.id})")

        # Create or retrieve Lesson
        lesson, lesson_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": lesson_title,
                "status": "published",
                "version": 1
            }
        )
        lesson.title = lesson_title
        lesson.status = "published"
        lesson.save()
        print(f"  Lesson: {lesson.title} (ID: {lesson.id}, Status: {lesson.status})")

        # Clean existing blocks and assets for this lesson to prevent duplicates
        LessonBlock.objects.filter(lesson=lesson).delete()
        LessonAsset.objects.filter(lesson=lesson).delete()

        # Ingest each block
        for order, card in enumerate(cards, start=1):
            block_id = f"f3_chem_t5_l{lesson.id}_b{order}_{uuid.uuid4().hex[:6]}"
            block = LessonBlock.objects.create(
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

            # Ingest attached LessonAsset if specified
            if "asset_info" in card:
                info = card["asset_info"]
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    title=info["title"],
                    description=info["description"],
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    url=info.get("url", ""),
                    status="attached"
                )
                asset.blocks.add(block)

        print(f"  Successfully created {len(cards)} structured LessonBlocks across 8 natural concept pages.")

    print("\n================================================================================")
    print("Ingestion Completed Successfully! All 5 Modules Published to Form 3 Topic 5.")
    print("================================================================================")

if __name__ == "__main__":
    ingest_form3_topic5_sulphur()
