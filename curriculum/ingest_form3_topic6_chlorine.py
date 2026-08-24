import os
import sys
import uuid
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def ingest_form3_topic6_chlorine():
    print("================================================================================")
    print("Starting VLearn Form 3 Chemistry Batch 6 Ingestion: Chlorine & Compounds (6.1-6.4)")
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
        defaults={"description": "Form 3 Chemistry (Secondary Chemistry Curriculum)"}
    )

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 6: Chlorine and its Compounds",
        defaults={
            "description": "Comprehensive study of chlorine laboratory preparation and properties, bleaching and redox reactions, hydrogen chloride gas and hydrochloric acid solvent behavior, analytical chloride testing, industrial chlorination, and environmental impacts of CFCs and DDT.",
            "order": 6
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name} (Grade: {grade.name})")

    # 2. Define Clean, Student-Facing Content Data Dictionary (Modules 6.1 - 6.4)
    modules_data = [
        {
            "unit_name": "Module 6.1: Laboratory Preparation and Physical Properties of Chlorine",
            "unit_order": 1,
            "lesson_title": "Laboratory Preparation and Physical Properties of Chlorine",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Halogen of Cleanliness",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will describe the electronic structure and single covalent bonding of diatomic chlorine ($Cl_2$), explore its laboratory preparation using $MnO_2, KMnO_4,$ and $PbO_2$, and examine the purifying and drying train."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of Bleach and Clean Water",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When you use household bleach like **Jik** to whiten school uniforms or visit a public swimming pool in **Nairobi or Mombasa**, you immediately encounter a sharp, pungent, choking smell.\n\nThat characteristic odor belongs to **chlorine ($Cl_2$)**, a highly reactive non-metal from Group VII (the Halogens). In its pure state, chlorine is a dense, toxic, greenish-yellow gas with immense industrial and sanitizing value."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diatomic Covalent Bonding in Chlorine",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Microscopic Particle Model of $Cl_2$:\n* **Valence Structure**: Chlorine (atomic number 17, electron configuration 2.8.7) has 7 valence electrons.\n* **Single Covalent Bond ($\\text{Cl}-\\text{Cl}$)**: Two chlorine atoms share a single pair of electrons, with each atom retaining three lone pairs (6 non-bonding electrons):\n  $$\\text{Cl} - \\text{Cl}$$\n* **Intermolecular Forces**: Weak intermolecular van der Waals forces hold diatomic $Cl_2$ molecules together, making chlorine a gas at room temperature and pressure ($RMM = 71.0$)."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Chlorine Laboratory Preparation & Purification Setup",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Diagram of the complete laboratory preparation, purification, drying, and collection train for chlorine gas.",
                        "instruction": "Round-bottomed flask containing black solid MnO2 heated gently with conc. HCl added via dropping funnel. Delivery tube enters Wash Bottle 1 (water to absorb HCl gas), then Wash Bottle 2 (concentrated H2SO4 to dry gas), and finally leads downward to the bottom of an upright gas jar (downward delivery).",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    },
                    "asset_info": {
                        "title": "Chlorine Laboratory Apparatus",
                        "description": "Apparatus diagram showing the generation, scrubbing, drying, and downward delivery collection of chlorine gas.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Oxidation of Hydrochloric Acid & The Scrubbing Train",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Laboratory Synthesis of Chlorine",
                        "content": "### 1. Preparation Reactions:\n* **With Manganese(IV) Oxide ($MnO_2$, Requires Heat)**:\n  $$\\text{MnO}_2(s) + 4\\text{HCl}(aq) \\xrightarrow{\\text{heat}} \\text{MnCl}_2(aq) + 2\\text{H}_2\\text{O}(l) + \\text{Cl}_2(g)$$\n* **With Potassium Manganate(VII) ($KMnO_4$, Cold Reaction / No Heat)**:\n  $$2\\text{KMnO}_4(s) + 16\\text{HCl}(aq) \\rightarrow 2\\text{KCl}(aq) + 2\\text{MnCl}_2(aq) + 8\\text{H}_2\\text{O}(l) + 5\\text{Cl}_2(g)$$\n* **With Lead(IV) Oxide ($PbO_2$, Requires Heat)**:\n  $$\\text{PbO}_2(s) + 4\\text{HCl}(aq) \\xrightarrow{\\text{heat}} \\text{PbCl}_2(s) + 2\\text{H}_2\\text{O}(l) + \\text{Cl}_2(g)$$\n\n### 2. Purifying and Drying Train:\n* **Wash Bottle 1 (Water)**: Absorbs vaporized hydrogen chloride gas ($HCl(g)$) impurities.\n* **Wash Bottle 2 (Conc. $H_2SO_4$)**: Absorbs water vapor to deliver dry gas.\n* **Collection**: Collected by **downward delivery** (upward displacement of air) because chlorine is $\\approx 2.5$ times denser than air."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Physical Properties & Safety Handling",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Properties and Safe Laboratory Handling\n* **Appearance & Density**: Dense, greenish-yellow gas ($RMM = 71.0$), sinking quickly in air.\n* **Odor & Toxicity**: Pungent, suffocating, and highly toxic to lung tissue. Always prepared in a fume chamber or well-ventilated laboratory.\n* **Solubility**: Moderately soluble in water forming pale-yellow **chlorine water**; highly soluble in non-polar organic solvents like tetrachloromethane ($CCl_4$)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Yield of Chlorine Gas at S.T.P.",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of dry chlorine gas produced at s.t.p. when $8.70\\text{ g}$ of Manganese(IV) oxide ($MnO_2$) reacts completely with excess concentrated hydrochloric acid ($Mn = 55.0, O = 16.0, V_m = 22.4\\text{ dm}^3\\text{ mol}^{-1}$).",
                        "steps": [
                            "**Step 1: Balanced Chemical Equation**:\n$$\\text{MnO}_2(s) + 4\\text{HCl}(aq) \\xrightarrow{\\text{heat}} \\text{MnCl}_2(aq) + 2\\text{H}_2\\text{O}(l) + \\text{Cl}_2(g)$$",
                            "**Step 2: Formula Mass and Moles of $MnO_2$**:\n- $\\text{R.F.M. of } MnO_2 = 55.0 + 2(16.0) = 87.0\\text{ g mol}^{-1}$\n- $\\text{Moles of } MnO_2 = \\frac{8.70\\text{ g}}{87.0\\text{ g mol}^{-1}} = 0.10\\text{ moles}$",
                            "**Step 3: Calculate Gas Volume at S.T.P.**:\n- Stoichiometric mole ratio $MnO_2 : Cl_2 = 1 : 1 \\implies 0.10\\text{ moles } Cl_2$\n- $\\text{Volume at s.t.p.} = 0.10\\text{ mol} \\times 22.4\\text{ dm}^3/\\text{mol} = \\mathbf{2.24\\text{ dm}^3} \\quad (2240\\text{ cm}^3)$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Water Scrubs HCl Without Losing Cl2",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### If chlorine is soluble in water, why bubble it through water to remove HCl?\nHydrogen chloride ($HCl$) gas is violently soluble in water (1 volume of water dissolves $\\approx 500$ volumes of $HCl$), dissolving instantly into hydrochloric acid.\n\nIn contrast, chlorine is only moderately soluble. The water absorbs 100% of the $HCl$ gas impurity while allowing over 95% of the chlorine gas to pass through safely into the drying bottle."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Chlorine Preparation",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following drying agents is chemically appropriate for drying chlorine gas in the laboratory?",
                        "options": [
                            "Anhydrous calcium chloride (CaCl2)",
                            "Quicklime (Calcium oxide, CaO)",
                            "Concentrated sulphuric(VI) acid (H2SO4)",
                            "Solid sodium hydroxide (NaOH)"
                        ],
                        "answer": "C",
                        "explanation": "Concentrated sulphuric(VI) acid is acidic and non-reactive toward chlorine gas, making it the standard laboratory drying agent. Basic drying agents like CaO and NaOH react chemically with acidic chlorine gas."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Chlorine Preparation",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Chlorine Preparation\n- **Bonding**: Diatomic molecule ($Cl_2$) with single covalent bond ($\\text{Cl}-\\text{Cl}$) and 3 lone pairs per atom.\n- **Preparation**: Oxidation of concentrated $HCl$ with $MnO_2$ (heat), $PbO_2$ (heat), or $KMnO_4$ (cold).\n- **Purification**: Water wash bottle (removes $HCl$) $\\rightarrow$ conc. $H_2SO_4$ bottle (removes moisture) $\\rightarrow$ downward delivery."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 6.2: Chemical Reactions, Bleaching, and Oxidising Properties of Chlorine",
            "unit_order": 2,
            "lesson_title": "Chemical Reactions, Bleaching, and Oxidising Properties of Chlorine",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Power of Halogen Oxidation",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will investigate the bleaching mechanism of chlorine via chloric(I) acid ($HClO$), contrast permanent oxidation bleaching with temporary reduction bleaching, and study reactions with metals, alkalis, and halide salt solutions."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Shattering Color Molecules Permanently",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Spilling household bleach onto a bright cotton **Kitenge or Khanga** fabric creates an immediate, permanent white patch.\n\nThe bleach does not simply wash the pigment away: it launches an aggressive oxidation attack that irreversibly shatters the complex colored dye molecules into tiny, colorless fragments."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Bleaching Mechanism: Chloric(I) Acid ($HClO$)",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Reversible Dissolution in Water:\nChlorine dissolves in water to form an equilibrium mixture of two acids:\n$$\\text{Cl}_2(g) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{HCl}(aq) + \\text{HClO}(aq)$$\n* **Hydrochloric Acid ($\\text{HCl}$)**: Responsible for the initial acidic red litmus color.\n* **Chloric(I) Acid ($\\text{HClO}$)**: Highly unstable oxidising agent that transfers its oxygen atom directly to dye molecules:\n  $$\\text{HClO}(aq) + \\text{Dye}(\\text{colored}) \\rightarrow \\text{HCl}(aq) + \\text{Dye-O}(\\text{colorless})$$\n* **Why Dry Chlorine Cannot Bleach**: Without moisture, unstable $HClO$ cannot form, so dry chlorine has zero bleaching power."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Reactions with Metals and Non-Metals",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Combination Reactions of Chlorine",
                        "content": "Because chlorine has high electronegativity, it oxidises elements to their highest oxidation states:\n\n* **With Burning Magnesium**: Burns brilliantly forming white magnesium chloride:\n  $$\\text{Mg}(s) + \\text{Cl}_2(g) \\rightarrow \\text{MgCl}_2(s)$$\n* **With Hot Iron Wire**: Glows red-hot without burning, forming reddish-brown iron(III) chloride ($FeCl_3$, not $FeCl_2$!):\n  $$2\\text{Fe}(s) + 3\\text{Cl}_2(g) \\rightarrow 2\\text{FeCl}_3(s)$$\n* **With Phosphorus**: Limited chlorine forms liquid $PCl_3$; excess chlorine forms solid $PCl_5$ ($P_4 + 10Cl_2 \\rightarrow 4PCl_5$).\n* **With Hydrogen**: Burns with blue-white flame forming $HCl(g)$ ($H_2 + Cl_2 \\rightarrow 2HCl$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Reactions with Alkalis & Bleach Synthesis",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Chlorine + Alkali Reactions",
                        "content": "### 1. With Cold Dilute Sodium Hydroxide ($NaOH$, Household Bleach):\n$$\\text{Cl}_2(g) + 2\\text{NaOH}(aq) \\rightarrow \\text{NaCl}(aq) + \\text{NaOCl}(aq) + \\text{H}_2\\text{O}(l)$$\n* **Active Ingredient**: **Sodium chlorate(I) ($NaOCl$)** is the disinfectant and bleaching agent in commercial Jik.\n\n### 2. With Hot Concentrated Sodium Hydroxide ($NaOH$):\n$$3\\text{Cl}_2(g) + 6\\text{NaOH}(aq) \\xrightarrow{\\text{heat}} 5\\text{NaCl}(aq) + \\text{NaClO}_3(aq) + 3\\text{H}_2\\text{O}(l)$$\n* **Product**: **Sodium chlorate(V) ($NaClO_3$)**, used in herbicides and weedkillers."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Halide Displacement & Redox Reactions",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Chlorine is more electronegative than bromine and iodine, displacing them from aqueous salt solutions:\n\n* **Displacement of Bromide ($Br^-$)**: Solution turns golden-orange:\n  $$\\text{Cl}_2(g) + 2\\text{Br}^-(aq) \\rightarrow 2\\text{Cl}^-(aq) + \\text{Br}_2(aq)$$\n* **Displacement of Iodide ($I^-$)**: Solution turns dark brown / black:\n  $$\\text{Cl}_2(g) + 2\\text{I}^-(aq) \\rightarrow 2\\text{Cl}^-(aq) + \\text{I}_2(aq)$$\n* **Oxidation of Hydrogen Sulphide**: Deposits yellow elemental sulphur ($Cl_2 + H_2S \\rightarrow S + 2HCl$).\n* **With Ammonia Gas**: Dense white fumes of ammonium chloride ($3Cl_2 + 8NH_3 \\rightarrow 6NH_4Cl + N_2$)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Mass of Displaced Iodine",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the mass of iodine ($I_2$) precipitated when excess chlorine gas is bubbled through $250\\text{ cm}^3$ of $0.20\\text{ M}$ potassium iodide ($KI$) solution ($K=39.0, I=127.0, Cl=35.5$).",
                        "steps": [
                            "**Step 1: Balanced Displacement Equation**:\n$$\\text{Cl}_2(g) + 2\\text{KI}(aq) \\rightarrow 2\\text{KCl}(aq) + \\text{I}_2(aq)$$",
                            "**Step 2: Moles of Potassium Iodide Reacted**:\n$$\\text{Moles of } KI = \\frac{0.20\\text{ mol dm}^{-3} \\times 250\\text{ cm}^3}{1000\\text{ cm}^3\\text{/dm}^3} = 0.050\\text{ moles}$$",
                            "**Step 3: Moles and Mass of Displaced Iodine**:\n- Mole ratio $KI : I_2 = 2 : 1 \\implies \\text{Moles of } I_2 = \\frac{0.050}{2} = 0.025\\text{ moles}$\n- Molar mass of $I_2 = 2 \\times 127.0 = 254.0\\text{ g mol}^{-1}$\n- $\\text{Mass of } I_2 = 0.025\\text{ mol} \\times 254.0\\text{ g mol}^{-1} = \\mathbf{6.35\\text{ g}}$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Chlorine vs Sulphur Dioxide Bleaching",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why is chlorine bleaching permanent while SO2 bleaching is temporary?\n* **Chlorine**: Bleaches by **oxidation** ($HClO$ adds oxygen to dye molecules). This chemical alteration is permanent and cannot be reversed by air exposure.\n* **Sulphur Dioxide**: Bleaches by **reduction** ($H_2SO_3$ removes oxygen from dye). Atmospheric oxygen gradually re-oxidises the dye over time, restoring the color."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Chlorine Reactions",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A piece of dry red litmus paper is lowered into a gas jar containing dry chlorine gas. What is the observed result?",
                        "options": [
                            "The litmus paper turns blue then white",
                            "The litmus paper turns white immediately",
                            "The litmus paper remains red",
                            "The litmus paper turns yellow"
                        ],
                        "answer": "C",
                        "explanation": "Dry chlorine gas cannot bleach because bleaching requires water to form chloric(I) acid ($HClO$), which donates the active bleaching oxygen. Without moisture, no chemical color change occurs."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Chlorine Reactions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Chlorine Reactions\n- **Bleaching**: $Cl_2 + H_2O \\rightleftharpoons HCl + HClO$; chloric(I) acid oxidises dye permanently.\n- **Metals**: Oxidises hot iron wire directly to reddish-brown iron(III) chloride ($FeCl_3$).\n- **Alkalis**: Cold dilute $NaOH \\rightarrow NaOCl$ (bleach); Hot concentrated $NaOH \\rightarrow NaClO_3$.\n- **Displacement**: Displaces $Br^-$ (orange $Br_2$) and $I^-$ (dark brown $I_2$) from salt solutions."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 6.3: Hydrogen Chloride Gas and Hydrochloric Acid",
            "unit_order": 3,
            "lesson_title": "Hydrogen Chloride Gas and Hydrochloric Acid",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Solvent Mystery of Hydrogen Chloride",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore hydrogen chloride gas ($HCl$), contrast its behavior in polar water (ionisation into hydronium and chloride ions) versus non-polar methylbenzene, and understand the inverted funnel safety arrangement."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "An Acid in Water, Unreactive in Oil",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Dissolving hydrogen chloride ($HCl$) gas in water creates an aggressively corrosive acid that conducts electricity and vigorously dissolves magnesium metal with effervescence.\n\nHowever, dissolving the exact same gas in **methylbenzene (toluene)** produces a completely neutral liquid that does not conduct electricity and leaves magnesium metal untouched. Acidity is not a property of the molecule alone—it depends entirely on **solvent polarity**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Polar Covalent Bonding & Solvent Ionisation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Polar Molecule: $\\overset{\\delta+}{\\text{H}} - \\overset{\\delta-}{\\text{Cl}}$\nChlorine is much more electronegative than hydrogen, creating a permanent dipole.\n\n* **In Polar Water**: Polar water molecules pull the dipole apart, causing complete **ionisation** into hydronium and chloride ions:\n  $$\\text{HCl}(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_3\\text{O}^+(aq) + \\text{Cl}^-(aq)$$\n  Free mobile ions conduct electricity and turn blue litmus red.\n\n* **In Non-Polar Methylbenzene**: Methylbenzene has no partial charges and cannot break the $H-Cl$ covalent bond. The gas remains as intact neutral molecules, unable to conduct electricity or exhibit acidity."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Laboratory Preparation & Downward Delivery",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Preparation of Hydrogen Chloride Gas",
                        "content": "### Reaction with Rock Salt ($NaCl$):\n$$\\text{NaCl}(s) + \\text{H}_2\\text{SO}_4(l) \\xrightarrow{\\text{mild warm}} \\text{NaHSO}_4(s) + \\text{HCl}(g)$$\n\n* **Why Acid Salt ($NaHSO_4$) Forms**: Producing normal salt $Na_2SO_4$ requires temperatures $>200^\\circ\\text{C}$ that would crack the glass flask.\n* **Drying & Collection**: Dried with concentrated $H_2SO_4$ wash bottle; collected by **downward delivery** ($RMM = 36.5$ vs air 29.0, highly water-soluble)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "The Fountain Experiment & Inverted Funnel Safety",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### 1. The Fountain Experiment (Extreme Solubility):\n1 volume of water dissolves over $500\\text{ volumes}$ of $HCl$ gas. Injecting water into an inverted $HCl$ flask creates a vacuum, drawing water up into a spectacular red fountain.\n\n### 2. Preventing Back-Suction (Inverted Funnel Setup):\n* **The Hazard**: Dissolving $HCl$ through a narrow delivery tube creates rapid vacuum suction that draws water back into the hot $H_2SO_4$ preparation flask, causing glass explosions.\n* **The Solution**: An **inverted glass funnel** dipped just 1-2 mm below the water surface provides a wide surface area for dissolution. If water rises into the funnel, the water level in the beaker drops below the rim, breaking contact with water and allowing the liquid to drain back down safely under gravity."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Typical Reactions of Hydrochloric Acid",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Reactions of Hydrochloric Acid",
                        "content": "In aqueous solution, hydrochloric acid behaves as a strong monobasic acid:\n\n* **With Reactive Metals**: $\\text{Mg} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2(g)$ (Copper does not react).\n* **With Bases (Neutralisation)**: $\\text{CuO} + 2\\text{HCl} \\rightarrow \\text{CuCl}_2 + \\text{H}_2\\text{O}$ (Black solid forms blue-green solution).\n* **With Carbonates**: $\\text{Na}_2\\text{CO}_3 + 2\\text{HCl} \\rightarrow 2\\text{NaCl} + \\text{H}_2\\text{O} + \\text{CO}_2(g)$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Titration Analysis of Hydrochloric Acid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$25.0\\text{ cm}^3$ of hydrochloric acid was titrated against $0.10\\text{ M}$ sodium carbonate ($Na_2CO_3$), requiring exactly $20.0\\text{ cm}^3$ of $Na_2CO_3$ for complete neutralisation. Calculate: (a) Molarity of $HCl$, (b) Concentration in $\\text{g dm}^{-3}$ ($H=1.0, Cl=35.5$).",
                        "steps": [
                            "**Step 1: Balanced Neutralisation Equation**:\n$$\\text{Na}_2\\text{CO}_3(aq) + 2\\text{HCl}(aq) \\rightarrow 2\\text{NaCl}(aq) + \\text{H}_2\\text{O}(l) + \\text{CO}_2(g)$$",
                            "**Step 2: Calculate Moles of $Na_2CO_3$**:\n$$\\text{Moles} = \\frac{0.10\\text{ mol dm}^{-3} \\times 20.0\\text{ cm}^3}{1000} = 0.0020\\text{ moles}$$",
                            "**Step 3: Calculate Molarity and Concentration of $HCl$**:\n- Mole ratio $Na_2CO_3 : HCl = 1 : 2 \\implies \\text{Moles of } HCl = 0.0040\\text{ moles}$\n- $\\text{Molarity} = \\frac{0.0040\\text{ mol} \\times 1000}{25.0\\text{ cm}^3} = \\mathbf{0.16\\text{ M (mol dm}^{-3}\\text{)}}$\n- $\\text{Molar mass of } HCl = 36.5\\text{ g mol}^{-1}$\n- $\\text{Concentration} = 0.16\\text{ mol dm}^{-3} \\times 36.5\\text{ g mol}^{-1} = \\mathbf{5.84\\text{ g dm}^{-3}}$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Acidity Requires a Polar Solvent",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Is HCl always an acid?\nNo! Acidity is a collaborative property between the solute and the solvent.\n\n$HCl$ only acts as an acid when dissolved in polar solvents like water that can pull the molecule apart into free hydrogen ions ($H_3O^+$). In non-polar solvents like methylbenzene, it remains as intact, neutral covalent molecules with zero acidic properties."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Hydrogen Chloride",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is an inverted glass funnel used to dissolve hydrogen chloride gas in water instead of a simple delivery tube?",
                        "options": [
                            "To increase the pressure of the gas during dissolution",
                            "To provide a larger surface area for dissolution and prevent dangerous back-suction of water into the hot flask",
                            "To filter out sodium sulphate impurities",
                            "To act as a catalyst for ionisation"
                        ],
                        "answer": "B",
                        "explanation": "HCl dissolves so rapidly that vacuum suction would pull water back into the hot reaction flask, cracking the glass. The inverted funnel provides a large dissolving surface area and automatically breaks water contact when water rises, preventing back-suction."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Hydrogen Chloride & HCl",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Hydrogen Chloride\n- **Preparation**: $NaCl(s) + H_2SO_4(l) \\xrightarrow{\\text{warm}} NaHSO_4(s) + HCl(g)$ (dried with conc. $H_2SO_4$).\n- **Solvent Effect**: Ionises completely to $H_3O^+ + Cl^-$ in water (acidic); remains covalent in methylbenzene (neutral).\n- **Safety Setup**: Inverted funnel prevents back-suction during aqueous dissolution."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 6.4: Analytical Testing for Chloride Ions, Industrial Uses, and Environmental Impacts of Halogens",
            "unit_order": 4,
            "lesson_title": "Analytical Testing for Chloride Ions, Industrial Uses, and Environmental Impacts of Halogens",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Forensic Analysis & Environmental Halogens",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master analytical precipitation tests for chloride ions ($Cl^-$) using silver nitrate and lead(II) nitrate, examine the mandatory nitric acid step, and analyze the environmental impacts of CFCs and DDT."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Analytical Chemistry & Global Environmental Protection",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "How do water quality analysts in **Nairobi, Kisumu, or Mombasa** confirm that municipal tap water is free of contamination and contains safe levels of chloride ions?\n\nThey use analytical precipitation tests. Beyond testing, chlorine shapes modern materials (PVC plastics) and water safety, but halogenated pollutants (CFCs and DDT) pose severe ecological challenges."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Analytical Precipitation Tests for Chloride Ions",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Chloride Ion Identification Tests",
                        "content": "### 1. The Silver Nitrate Test:\n1. Acidify test solution with **dilute nitric(V) acid ($HNO_3$)**.\n2. Add silver nitrate solution ($AgNO_3$).\n3. **Observation**: A dense white precipitate of silver chloride forms:\n   $$\\text{Ag}^+(aq) + \\text{Cl}^-(aq) \\rightarrow \\text{AgCl}(s)$$\n4. **Confirmation**: Precipitate is insoluble in dilute $HNO_3$, but **dissolves completely in excess aqueous ammonia** forming diamminesilver(I) complex ion ($[\\text{Ag}(\\text{NH}_3)_2]^+$).\n\n### 2. The Lead(II) Nitrate Test:\n1. Add lead(II) nitrate solution ($Pb(NO_3)_2$) $\\rightarrow$ white precipitate of lead(II) chloride forms ($Pb^{2+} + 2Cl^- \\rightarrow PbCl_2$).\n2. **Warm and Cool Confirmation**: White $PbCl_2$ **dissolves on warming** to form a colorless solution, and **recrystallises as shiny needle-like crystals on cooling**."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Ozone Destruction Catalytic Cycle",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Diagram illustrating how free chlorine radicals from CFCs catalytically destroy stratospheric ozone molecules.",
                        "instruction": "Catalytic cycle showing UV light breaking CF2Cl2 into CF2Cl radical and Cl radical. The Cl radical attacks O3 to form ClO and O2. A free oxygen atom collides with ClO, releasing O2 and regenerating the Cl radical to destroy more ozone molecules.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    },
                    "asset_info": {
                        "title": "Ozone Depletion Catalytic Cycle",
                        "description": "Flowchart showing catalytic chain reaction of chlorine radicals destroying ozone.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Industrial Applications of Chlorine",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Water Purification, Polymers, and Solvents\n* **Municipal Water Treatment**: Chlorine added to water generates chloric(I) acid ($HClO$), which oxidises bacterial cell membranes and enzymes, rendering water safe across Kenyan cities.\n* **PVC Plastics**: Monomer chloroethene ($CH_2=CHCl$) is polymerised into Polyvinyl chloride (PVC) for construction drainage pipes and electrical wire insulation.\n* **Industrial Solvents**: Synthesis of trichloromethane (chloroform, $CHCl_3$) and tetrachloromethane ($CCl_4$) for degreasing."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Environmental Impacts: CFCs and DDT",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### 1. Chlorofluorocarbons (CFCs) & Stratospheric Ozone Depletion:\nCFCs (e.g. $\\text{CF}_2\\text{Cl}_2$) diffuse into the stratosphere where solar UV radiation breaks them, releasing reactive **chlorine free radicals ($Cl^\\bullet$)**:\n$$\\text{CF}_2\\text{Cl}_2 \\xrightarrow{\\text{UV}} \\text{CF}_2\\text{Cl}^\\bullet + \\text{Cl}^\\bullet$$\n$$\\text{Cl}^\\bullet + \\text{O}_3 \\rightarrow \\text{ClO}^\\bullet + \\text{O}_2 \\quad ; \\quad \\text{ClO}^\\bullet + \\text{O} \\rightarrow \\text{Cl}^\\bullet + \\text{O}_2$$\nA single chlorine radical catalytically destroys over $100,000\\text{ ozone}$ molecules, allowing harmful UV-B radiation to cause skin cancer and eye cataracts.\n\n### 2. DDT and Bioaccumulation / Biomagnification:\nDDT is a non-biodegradable, fat-soluble chlorinated pesticide. It accumulates in fatty tissues (**bioaccumulation**) and amplifies up the food chain (**biomagnification**), causing eggshell thinning in birds. Kenya's **NEMA** enforces bans on DDT, promoting biodegradable pyrethroids from local pyrethrum flowers."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Gravimetric Calculation of Chloride Concentration",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A $50.0\\text{ cm}^3$ factory effluent sample was acidified with dilute $HNO_3$ and treated with excess silver nitrate. The resulting silver chloride ($AgCl$) precipitate weighed exactly $1.435\\text{ g}$. Calculate: (a) Moles of $AgCl$ precipitated, (b) Molarity of chloride ions in effluent ($Ag=108.0, Cl=35.5$).",
                        "steps": [
                            "**Step 1: Calculate Moles of $AgCl$**:\n- $\\text{R.F.M. of } AgCl = 108.0 + 35.5 = 143.5\\text{ g mol}^{-1}$\n- $\\text{Moles of } AgCl = \\frac{1.435\\text{ g}}{143.5\\text{ g mol}^{-1}} = 0.010\\text{ moles}$",
                            "**Step 2: Relate to Chloride Ions**:\n$$\\text{Ag}^+(aq) + \\text{Cl}^-(aq) \\rightarrow \\text{AgCl}(s) \\implies \\text{Moles of } Cl^- = 0.010\\text{ moles}$$",
                            "**Step 3: Calculate Molarity in Effluent**:\n$$\\text{Molarity of } Cl^- = \\frac{0.010\\text{ mol} \\times 1000}{50.0\\text{ cm}^3} = \\mathbf{0.20\\text{ M (mol dm}^{-3}\\text{)}}$$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Only Dilute Nitric Acid is Used",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why can't we acidify with HCl or H2SO4 before adding silver nitrate?\n* **Hydrochloric acid ($HCl$)**: Adds foreign chloride ions that react with silver nitrate to form a false-positive white $AgCl$ precipitate.\n* **Sulphuric acid ($H_2SO_4$)**: Adds sulphate ions ($SO_4^{2-}$) that can form sparingly soluble white silver sulphate ($Ag_2SO_4$).\n* **Nitric acid ($HNO_3$)**: Destroys interfering carbonate ($CO_3^{2-}$) and sulphite ($SO_3^{2-}$) ions without forming any precipitates, because all nitrates are soluble."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Chloride Testing & Halogens",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A student acidified an unknown halide solution with dilute hydrochloric acid and added silver nitrate solution, observing a dense white precipitate. What conclusion can be made?",
                        "options": [
                            "The unknown solution definitely contains chloride ions",
                            "The unknown solution contains bromide ions",
                            "The white precipitate was caused by the hydrochloric acid added, so no valid conclusion can be drawn",
                            "The unknown solution contains lead(II) ions"
                        ],
                        "answer": "C",
                        "explanation": "Acidifying with hydrochloric acid introduces external chloride ions ($Cl^-$) into the solution, which instantly precipitate with silver nitrate as white $AgCl$. This invalidates the test for the unknown substance."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Analytical Chloride & Pollution",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Chloride & Environment\n- **Analysis**: $AgNO_3 + HNO_3 \\rightarrow$ white $AgCl$ (dissolves in aqueous ammonia); $Pb(NO_3)_2 \\rightarrow$ white $PbCl_2$ (dissolves on warming, recrystallises on cooling).\n- **Uses**: Water purification ($HClO$ disinfectant), PVC pipes, organic chlorinated solvents.\n- **Pollution**: CFCs destroy ozone catalytically via $Cl^\\bullet$ radicals; DDT bioaccumulates up the food chain."
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
            block_id = f"f3_chem_t6_l{lesson.id}_b{order}_{uuid.uuid4().hex[:6]}"
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
    print("Ingestion Completed Successfully! All 4 Modules Published to Form 3 Topic 6.")
    print("================================================================================")

if __name__ == "__main__":
    ingest_form3_topic6_chlorine()
