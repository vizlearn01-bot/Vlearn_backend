import os
import sys
import uuid
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def ingest_form3_topic4_nitrogen():
    print("================================================================================")
    print("Starting VLearn Form 3 Chemistry Batch 4 Ingestion: Nitrogen & Compounds (4.1-4.6)")
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
        name="Topic 4: Nitrogen and its Compounds",
        defaults={
            "description": "Study of nitrogen isolation and preparation, oxides of nitrogen, ammonia and the Haber process, nitrogenous fertilisers, and the manufacture and properties of nitric(V) acid and nitrates.",
            "order": 4
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name} (Grade: {grade.name})")

    # 2. Define Clean, Student-Facing Content Data Dictionary (Modules 4.1 - 4.6)
    modules_data = [
        {
            "unit_name": "Module 4.1: Isolation and Laboratory Preparation of Nitrogen Gas",
            "unit_order": 1,
            "lesson_title": "Isolation and Laboratory Preparation of Nitrogen Gas",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Silent Ocean of Air",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will investigate how nitrogen is isolated from atmospheric air and prepared in the laboratory from sodium nitrite and ammonium chloride, exploring its physical properties and molecular bonding ($\\text{N}\\equiv\\text{N}$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Unreactive Majority of Our Atmosphere",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Standing outside in **Kakamega, Garissa, or Mombasa**, you are immersed in an invisible ocean of air. Nearly four-fifths (about **78% by volume**) of this air is **Nitrogen ($\\text{N}_2$)**.\n\nUnlike oxygen, which actively supports combustion and oxidizes metals into rust, nitrogen is remarkably unreactive at room temperature. It has no color, odor, or taste, and does not burn or support combustion."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Triple Covalent Bonding in Nitrogen",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Why is nitrogen gas so inert?\n\n* **Atomic Configuration**: Nitrogen (atomic number 7, electron configuration 2:5) requires 3 valence electrons to achieve a stable octet.\n* **Triple Covalent Bond ($\\text{N}\\equiv\\text{N}$)**: Two nitrogen atoms share three pairs of electrons, forming a triple covalent bond with a bond dissociation energy of $945\\text{ kJ mol}^{-1}$.\n* **Chemical Inertness**: Breaking this immense bond requires extreme thermal energy (e.g. atmospheric lightning strikes or high-temperature engines), rendering nitrogen completely unreactive under ordinary ambient conditions."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Fractional Distillation of Liquid Air",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Illustrate the industrial liquefaction and fractional distillation of air to isolate nitrogen gas.",
                        "instruction": "Flow diagram showing atmospheric air passing through KOH scrubber (removing CO2), cooling chamber at -25°C (freezing water), compressor at 200 atm (-200°C liquid air), and fractionating column warming to -196°C where nitrogen gas boils off, leaving liquid oxygen at -183°C.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    },
                    "asset_info": {
                        "title": "Industrial Air Distillation Flow",
                        "description": "Flowchart showing industrial liquefaction and separation of liquid nitrogen and oxygen.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Chemical Isolation and Laboratory Synthesis",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Methods of Obtaining Nitrogen",
                        "content": "### 1. Isolation from Air:\n* **Remove $\\text{CO}_2$**: Bubble air through concentrated $\\text{KOH}$ or $\\text{NaOH}$:\n  $$\\text{CO}_2\\text{(g)} + 2\\text{KOH(aq)} \\rightarrow \\text{K}_2\\text{CO}_3\\text{(aq)} + \\text{H}_2\\text{O(l)}$$\n* **Remove Moisture**: Pass through concentrated $\\text{H}_2\\text{SO}_4$ or anhydrous $\\text{CaCl}_2$.\n* **Remove $\\text{O}_2$**: Pass dry gas over heated copper turnings ($2\\text{Cu} + \\text{O}_2 \\rightarrow 2\\text{CuO}$).\n* *Note*: Isolated nitrogen contains inert **Argon ($\approx 1\\%$)**, making it slightly denser than pure nitrogen.\n\n### 2. Laboratory Preparation of Pure $\\text{N}_2$:\nHeating an in-situ mixture of sodium nitrite and ammonium chloride:\n$$\\text{NaNO}_2\\text{(aq)} + \\text{NH}_4\\text{Cl(aq)} \\rightarrow \\text{NH}_4\\text{NO}_2\\text{(aq)} + \\text{NaCl(aq)}$$\n$$\\text{NH}_4\\text{NO}_2\\text{(aq)} \\xrightarrow{\\text{heat}} \\text{N}_2\\text{(g)} + 2\\text{H}_2\\text{O(g)}$$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Industrial and Agricultural Applications in Kenya",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Cryopreservation and Food Preservation\n* **Livestock Genetics**: Liquid nitrogen (boiling point $-196^\\circ\\text{C}$) is used extensively at the **Kenya Animal Genetic Resources Centre (KAGRC) in Kabete** to cryopreserve bull semen for artificial insemination across dairy farms.\n* **Food Packaging**: Food processing industries flush potato crisp packets with nitrogen gas to displace oxygen, preventing oils from turning rancid."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Required Air Volume for Isolation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the minimum volume of atmospheric air (containing 78% nitrogen by volume) required to isolate $500\\text{ cm}^3$ of nitrogen gas.",
                        "steps": [
                            "**Step 1: Formula Relationship**:\n$$\\text{Volume of } \\text{N}_2 = \\frac{78}{100} \\times \\text{Volume of Air}$$",
                            "**Step 2: Solve for Air Volume**:\n$$500\\text{ cm}^3 = 0.78 \\times V_{\\text{air}} \\implies V_{\\text{air}} = \\frac{500}{0.78} = 641.03\\text{ cm}^3$$",
                            "**Interpretation**: A student must process at least $641.03\\text{ cm}^3$ of air through the alkali scrubbers, drying column, and hot copper turnings."
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Triple Bonds Make Nitrogen Inert",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does a triple bond mean higher chemical reactivity?\nIn organic chemistry, double and triple bonds between carbons are reactive due to exposed $\\pi$ bonds. However, in the diatomic nitrogen molecule ($\\text{N}\\equiv\\text{N}$), the triple covalent bond is extraordinarily strong ($945\\text{ kJ mol}^{-1}$).\n\nBecause so much energy is required to split the nitrogen atoms apart, $\\text{N}_2$ behaves like an inert gas under normal conditions."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Nitrogen Gas",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is nitrogen gas isolated from atmospheric air slightly denser than pure nitrogen prepared from ammonium nitrite in the laboratory?",
                        "options": [
                            "Isolated nitrogen contains unreacted oxygen and carbon dioxide",
                            "Isolated nitrogen contains noble gases such as Argon as impurities",
                            "Chemically prepared nitrogen contains lighter isotopes",
                            "Chemically prepared nitrogen is contaminated with hydrogen gas"
                        ],
                        "answer": "B",
                        "explanation": "Chemical scrubbers remove $\\text{CO}_2$, water, and $\\text{O}_2$, but unreactive Argon (atomic mass 40) passes through, making atmospheric nitrogen denser than pure chemically synthesized $\\text{N}_2$ (molecular mass 28)."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Nitrogen Gas",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Nitrogen Gas\n- **Structure**: Diatomic $\\text{N}_2$ held by a powerful triple covalent bond ($\\text{N}\\equiv\\text{N}$).\n- **Isolation**: Air treated with $\\text{KOH}$ (removes $\\text{CO}_2$), drying agent (removes $\\text{H}_2\\text{O}$), and hot $\\text{Cu}$ (removes $\\text{O}_2$).\n- **Lab Synthesis**: Gentle heating of in-situ $\\text{NaNO}_2 + \\text{NH}_4\\text{Cl} \\rightarrow \\text{N}_2 + 2\\text{H}_2\\text{O} + \\text{NaCl}$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 4.2: Oxides of Nitrogen (Dinitrogen oxide, Nitrogen monoxide, Nitrogen dioxide)",
            "unit_order": 2,
            "lesson_title": "Oxides of Nitrogen (Dinitrogen oxide, Nitrogen monoxide, Nitrogen dioxide)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Diverse Oxides of Nitrogen",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore the three principal oxides of nitrogen—dinitrogen(I) oxide ($\\text{N}_2\\text{O}$), nitrogen(II) oxide ($\\text{NO}$), and nitrogen(IV) oxide ($\\text{NO}_2$)—comparing their preparations, appearances, and chemical behaviors."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "From Dental Anaesthetic to Urban Smog",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In dental clinics, patients inhale **Dinitrogen(I) oxide ($\\text{N}_2\\text{O}$)**—laughing gas—to relieve pain.\n\nAlong urban highways like the **Nairobi Expressway and Thika Road**, vehicle exhausts release dense reddish-brown fumes of **Nitrogen(IV) oxide ($\\text{NO}_2$)**, an irritating and choking air pollutant. Exploring these oxides reveals how differing oxidation states transform chemical properties."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Comparison of Nitrogen Oxides",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Oxides of Nitrogen Matrix",
                        "content": "| Property | $\\text{N}_2\\text{O}$ (Nitrogen(I) oxide) | $\\text{NO}$ (Nitrogen(II) oxide) | $\\text{NO}_2$ (Nitrogen(IV) oxide) |\n| :--- | :--- | :--- | :--- |\n| **Oxidation State** | $+1$ | $+2$ | $+4$ |\n| **Color** | Colorless | Colorless | Reddish-brown |\n| **Odor** | Sweet, pleasant | Odorless | Choking, pungent |\n| **Litmus Effect** | Neutral | Neutral | Acidic (blue litmus $\\rightarrow$ red) |\n| **Water Solubility**| Soluble in cold water | Insoluble | Readily soluble |"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Laboratory Synthesis of Nitrogen Oxides",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### 1. Dinitrogen(I) oxide ($\\text{N}_2\\text{O}$):\n* **Preparation**: Gentle heating of solid ammonium nitrate:\n  $$\\text{NH}_4\\text{NO}_3\\text{(s)} \\xrightarrow{\\text{heat}} \\text{N}_2\\text{O(g)} + 2\\text{H}_2\\text{O(g)}$$\n* **Collection**: Collected over warm water.\n\n### 2. Nitrogen(II) oxide ($\\text{NO}$):\n* **Preparation**: Reacting copper turnings with dilute (50%) nitric(V) acid:\n  $$3\\text{Cu(s)} + 8\\text{HNO}_3\\text{(aq)} \\rightarrow 3\\text{Cu(NO}_3)_2\\text{(aq)} + 4\\text{H}_2\\text{O(l)} + 2\\text{NO(g)}$$\n* **Collection**: Collected over water.\n\n### 3. Nitrogen(IV) oxide ($\\text{NO}_2$):\n* **Preparation**: Reacting copper turnings with concentrated nitric(V) acid OR thermal decomposition of lead(II) nitrate:\n  $$\\text{Cu(s)} + 4\\text{HNO}_3\\text{(l)} \\rightarrow \\text{Cu(NO}_3)_2\\text{(aq)} + 2\\text{NO}_2\\text{(g)} + 2\\text{H}_2\\text{O(l)}$$\n  $$2\\text{Pb(NO}_3)_2\\text{(s)} \\xrightarrow{\\text{heat}} 2\\text{PbO(s)} + 4\\text{NO}_2\\text{(g)} + \\text{O}_2\\text{(g)}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Reversible Dimerization and Acid Formation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### $\\text{NO}_2 \\rightleftharpoons \\text{N}_2\\text{O}_4$ Equilibrium:\nPassing reddish-brown $\\text{NO}_2$ gas through an ice-cold U-tube condenses it into a pale-yellow liquid: **dinitrogen tetraoxide ($\\text{N}_2\\text{O}_4$)**:\n$$2\\text{NO}_2\\text{(g, brown)} \\underset{\\text{warm}}{\\overset{\\text{cool}}{\\rightleftharpoons}} \\text{N}_2\\text{O}_4\\text{(l, pale-yellow)}$$\n\n### Dissolution in Water:\n$\\text{NO}_2$ dissolves in water to produce a mixture of two acids:\n$$2\\text{NO}_2\\text{(g)} + \\text{H}_2\\text{O(l)} \\rightarrow \\text{HNO}_2\\text{(aq, nitric(III))} + \\text{HNO}_3\\text{(aq, nitric(V))}$$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Calculating Gas Volume from Nitrate Decomposition",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of nitrogen(IV) oxide ($\\text{NO}_2$) evolved at S.T.P. when $5.0\\text{ g}$ of dry lead(II) nitrate is decomposed completely ($Pb=207, N=14, O=16$, $V_m=22.4\\text{ dm}^3\\text{ mol}^{-1}$).",
                        "steps": [
                            "**Step 1: Balanced Equation**:\n$$2\\text{Pb(NO}_3)_2\\text{(s)} \\rightarrow 2\\text{PbO(s)} + 4\\text{NO}_2\\text{(g)} + \\text{O}_2\\text{(g)}$$",
                            "**Step 2: Calculate Moles of Lead(II) Nitrate**:\n- Molar mass of $\\text{Pb(NO}_3)_2 = 207 + 2(14 + 48) = 331\\text{ g mol}^{-1}$\n- Moles heated $= \\frac{5.0}{331} = 0.0151\\text{ mol}$",
                            "**Step 3: Moles and Volume of $\\text{NO}_2$**:\n- Moles of $\\text{NO}_2 = 2 \\times 0.0151 = 0.0302\\text{ mol}$\n- Volume at S.T.P. $= 0.0302\\text{ mol} \\times 22.4\\text{ dm}^3/\\text{mol} = 0.676\\text{ dm}^3$ ($676.5\\text{ cm}^3$)"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Diagnostic Tests to Distinguish Nitrogen Oxides",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Confirmatory Tests",
                        "content": "### Key Diagnostic Reactions:\n* **Distinguishing $\\text{O}_2$ and $\\text{N}_2\\text{O}$**: Both relight a glowing splint. Mixing with colorless $\\text{NO}$ produces brown $\\text{NO}_2$ fumes with $\\text{O}_2$, but no reaction with $\\text{N}_2\\text{O}$.\n* **Confirmatory Test for $\\text{NO}$**: Contact with atmospheric air instantly produces reddish-brown $\\text{NO}_2$ fumes.\n* **Brown Ring Test for $\\text{NO}$**: Bubbling through cold iron(II) sulphate forms a dark-brown complex: $\\text{FeSO}_4\\cdot\\text{NO}$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Glowing Splints with N2O",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does oxygen uniquely relight a glowing splint?\nNo! Dinitrogen(I) oxide ($\\text{N}_2\\text{O}$) also relights a glowing splint because the thermal energy of the glowing ember decomposes $\\text{N}_2\\text{O}$ into nitrogen and free oxygen gas ($2\\text{N}_2\\text{O} \\rightarrow 2\\text{N}_2 + \\text{O}_2$).\n\nTo distinguish them, mix the gas with colorless $\\text{NO}$ gas; only oxygen will produce brown fumes of $\\text{NO}_2$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Nitrogen Oxides",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which gas is colorless, neutral to litmus, and instantly turns reddish-brown when exposed to atmospheric air?",
                        "options": [
                            "Dinitrogen(I) oxide ($\\text{N}_2\\text{O}$)",
                            "Nitrogen(II) oxide ($\\text{NO}$)",
                            "Nitrogen(IV) oxide ($\\text{NO}_2$)",
                            "Ammonia ($\\text{NH}_3$)"
                        ],
                        "answer": "B",
                        "explanation": "Nitrogen(II) oxide ($\\text{NO}$) is colorless and neutral. It oxidizes spontaneously upon contact with atmospheric oxygen to form reddish-brown Nitrogen(IV) oxide ($\\text{NO}_2$)."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Nitrogen Oxides",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Oxides of Nitrogen\n- **$\\text{N}_2\\text{O}$ ($+1$)**: Colorless, sweet odor, neutral, relights glowing splint.\n- **$\\text{NO}$ ($+2$)**: Colorless, neutral, oxidizes in air to brown $\\text{NO}_2$.\n- **$\\text{NO}_2$ ($+4$)**: Reddish-brown, acidic, choking, condenses to liquid $\\text{N}_2\\text{O}_4$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 4.3: Ammonia and the Haber Process",
            "unit_order": 3,
            "lesson_title": "Ammonia and the Haber Process",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Alkaline Molecule That Feeds the World",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will study ammonia ($\\text{NH}_3$), its laboratory preparation and fountain solubility experiment, and master the industrial Haber process including Le Chatelier's optimal conditions."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Essential Chemistry of Ammonia",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Ammonia ($\\text{NH}_3$) possesses a pungent, choking odor familiar from smelling salts or decomposing organic wastes.\n\nAmmonia is arguably the most vital industrial chemical in human history: it is the primary precursor for all synthetic nitrogenous fertilisers that nourish global agriculture. In the laboratory, ammonia is unique as the **only common alkaline gas** in existence."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Molecular Structure & Dative Covalent Bonding",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Lone Pair and Polar Geometry:\n* **Pyramidal Shape**: Nitrogen forms three single covalent bonds with hydrogen atoms, leaving one **lone pair of electrons**.\n* **Dative (Coordinate) Bonding in $\\text{NH}_4^+$**:\n  When ammonia dissolves in water or reacts with acids, the lone pair is donated into the empty orbital of a hydrogen ion ($H^+$), forming a **dative covalent bond**:\n  $$\\text{NH}_3\\text{(g)} + \\text{H}^+\\text{(aq)} \\rightarrow \\text{NH}_4^+\\text{(aq)}$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Laboratory Preparation and Drying of Ammonia",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Preparation of Ammonia Gas",
                        "content": "### Reaction of Ammonium Salt with Alkali:\n$$\\text{Ca(OH)}_2\\text{(s)} + 2\\text{NH}_4\\text{Cl(s)} \\xrightarrow{\\text{heat}} \\text{CaCl}_2\\text{(s)} + 2\\text{H}_2\\text{O(l)} + 2\\text{NH}_3\\text{(g)}$$\n\n### Essential Setup Protocols:\n* **Slanting Flask**: The flask is tilted downwards to prevent condensed water droplets from running back into the hot base, which would crack the glass.\n* **Drying Agent**: Must be dried **only with Calcium Oxide (Quicklime, $\\text{CaO}$)**. Acidic drying agents ($\text{H}_2\\text{SO}_4$) or $\\text{CaCl}_2$ react chemically with alkaline ammonia.\n* **Collection**: Collected by **upward delivery** (downward displacement of air) due to its lower density than air."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "The Ammonia Fountain & Cation Precipitation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Fountain Experiment (Extreme Solubility):\nAmmonia is extraordinarily soluble in water ($1\\text{ Litre}$ of water dissolves $\\approx 700\\text{ Litres}$ of $\\text{NH}_3$). A drop of water introduced into an inverted ammonia flask dissolves the gas, creating a partial vacuum that pulls up water to form a purple/blue alkaline fountain.\n\n### Precipitation of Metal Hydroxides:\n* **$\\text{Cu}^{2+}$ (Copper)**: Pale blue precipitate $\\text{Cu(OH)}_2$, dissolving in excess ammonia to form a **deep blue solution** ($[\\text{Cu(NH}_3)_4]^{2+}$).\n* **$\\text{Zn}^{2+}$ (Zinc)**: White precipitate $\\text{Zn(OH)}_2$, dissolving in excess ammonia to form a **colorless solution** ($[\\text{Zn(NH}_3)_4]^{2+}$).\n* **$\\text{Fe}^{2+}$ / $\\text{Fe}^{3+}$**: Dirty green / rust-brown precipitates, both **insoluble in excess ammonia**."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Industrial Manufacture: The Haber Process",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Haber Process",
                        "content": "$$\\text{N}_2\\text{(g)} + 3\\text{H}_2\\text{(g)} \\rightleftharpoons 2\\text{NH}_3\\text{(g)} \\quad \\Delta H = -92\\text{ kJ mol}^{-1}$$\n\n### Optimum Industrial Compromise Conditions:\n* **Temperature**: $450^\\circ\\text{C}-500^\\circ\\text{C}$ (balances reaction rate against exothermic equilibrium yield).\n* **Pressure**: $200-500\\text{ atmospheres}$ (favors forward reaction by reducing gas volume).\n* **Catalyst**: Finely divided iron with aluminium oxide promoter.\n* **Recycling**: Unreacted $\\text{N}_2$ and $\\text{H}_2$ are continuously recycled."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Ammonia Yield from Haber Reactor",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "In an industrial Haber reactor, $120\\text{ Litres}$ of nitrogen gas was reacted with excess hydrogen at constant temperature and pressure. Calculate the maximum volume of ammonia gas obtained.",
                        "steps": [
                            "**Step 1: Balanced Equation**:\n$$\\text{N}_2\\text{(g)} + 3\\text{H}_2\\text{(g)} \\rightleftharpoons 2\\text{NH}_3\\text{(g)}$$",
                            "**Step 2: Volume Ratio (Gay-Lussac's Law)**:\n$$\\text{Volume Ratio: } \\text{N}_2 : \\text{NH}_3 = 1 : 2$$",
                            "**Step 3: Calculate Yield**:\n$$\\text{Volume of } \\text{NH}_3 = 2 \\times 120\\text{ Litres} = 240\\text{ Litres}$$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Aqueous Ammonia vs Strong Bases",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Is aqueous ammonia a strong base like sodium hydroxide?\nNo! Aqueous ammonia is a **weak base**. The formula \"$\\text{NH}_4\\text{OH}$\" does not exist as a fully dissociated species in solution.\n\nAqueous ammonia consists mostly of dissolved molecular $\\text{NH}_3$ in equilibrium with a small fraction of $\\text{NH}_4^+$ and $\\text{OH}^-$ ions."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Ammonia",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following drying agents is chemically suitable for drying ammonia gas in the laboratory?",
                        "options": [
                            "Concentrated sulphuric(VI) acid ($\\text{H}_2\\text{SO}_4$)",
                            "Anhydrous calcium chloride ($\\text{CaCl}_2$)",
                            "Calcium oxide (Quicklime, $\\text{CaO}$)",
                            "Phosphorus(V) oxide ($\\text{P}_2\\text{O}_5$)"
                        ],
                        "answer": "C",
                        "explanation": "Ammonia is an alkaline gas and reacts with acidic drying agents (forming ammonium salts) and forms complexes with $\\text{CaCl}_2$. Basic calcium oxide ($\\text{CaO}$) dries ammonia safely without reacting."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Ammonia & Haber Process",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Ammonia\n- **Properties**: Colorless, alkaline, pyramidal geometry with lone pair, extremely water-soluble.\n- **Preparation**: $\\text{Ca(OH)}_2 + 2\\text{NH}_4\\text{Cl} \\rightarrow \\text{CaCl}_2 + 2\\text{H}_2\\text{O} + 2\\text{NH}_3$ (slanting flask, $\\text{CaO}$ drying).\n- **Haber Process**: $\\text{N}_2 + 3\\text{H}_2 \\rightleftharpoons 2\\text{NH}_3$ at $450^\\circ\\text{C}$, $200\\text{ atm}$, Iron catalyst."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 4.4: Nitrogenous Fertilisers",
            "unit_order": 4,
            "lesson_title": "Nitrogenous Fertilisers",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Feeding Kenya's Crops",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will examine nitrogenous fertilisers (such as CAN, urea, and ammonium sulphate), calculate percentage nitrogen content by mass, and understand agricultural benefits and environmental eutrophication."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Agricultural Paradox",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In tea and maize farms across **Kiambu, Murang'a, Kericho, and Trans-Nzoia**, crop health depends on agricultural fertilisers like Urea, CAN, and Ammonium Sulphate.\n\nAlthough surrounded by an atmosphere of 78% nitrogen gas, plants cannot absorb atmospheric $\\text{N}_2$ directly due to its triple covalent bond. Plants can only absorb soluble **nitrate ions ($\\text{NO}_3^-$)** or **ammonium ions ($\\text{NH}_4^+$)** dissolved in soil water."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Synthesis & Properties of Nitrogenous Fertilisers",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Major Nitrogenous Fertilisers",
                        "content": "### 1. Urea [$\\text{CO(NH}_2)_2$]:\n* Prepared by reacting $\\text{CO}_2$ with ammonia at high pressure.\n* **Highest Nitrogen Content**: $\\mathbf{46.67\\%}$. Most economical to transport.\n\n### 2. Ammonium Nitrate [$\\text{NH}_4\\text{NO}_3$]:\n* Neutralisation of $\\text{HNO}_3$ with ammonia. **35.0% Nitrogen**.\n\n### 3. Calcium Ammonium Nitrate (CAN):\n* Blend of $\\text{NH}_4\\text{NO}_3$ and crushed limestone ($\\text{CaCO}_3$). **27.0% Nitrogen**.\n* *Benefit*: Non-acidifying; $\\text{CaCO}_3$ neutralizes soil acidity.\n\n### 4. Ammonium Sulphate [$(\\text{NH}_4)_2\\text{SO}_4$]:\n* Neutralisation of $\\text{H}_2\\text{SO}_4$ with ammonia. **21.21% Nitrogen**. Strongly acidifies soil with repeated use."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Environmental Impact: Eutrophication",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Eutrophication Mechanism:\n1. **Runoff**: Excessive soluble nitrate fertilisers wash into rivers and lakes (e.g. Lake Victoria) during heavy rains.\n2. **Algal Bloom**: Nutrient overload triggers explosive algal growth across the water surface.\n3. **Light Deprivation**: Algal mats block sunlight, killing submerged aquatic plants.\n4. **Oxygen Depletion**: Decomposing aerobic bacteria consume dissolved oxygen, suffocating fish and aquatic life."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Agricultural Practices in Kenya",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### CAN vs Urea in Kenyan Agriculture\n* **Maize Top-Dressing**: Farmers in Uasin Gishu and Trans-Nzoia use **CAN** to prevent seasonal soil acidification.\n* **Tea Plantations**: Tea bushes thrive in slightly acidic soils, making **Urea** ideal for delivering maximum nitrogen density while preserving optimal soil conditions."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Calculating Nitrogen Percentage by Mass",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the percentage of nitrogen by mass in Urea [$\\text{CO(NH}_2)_2$] and Ammonium Sulphate [$(\\text{NH}_4)_2\\text{SO}_4$] ($H=1, C=12, N=14, O=16, S=32$).",
                        "steps": [
                            "**Urea [$\\text{CO(NH}_2)_2$]**:\n- Formula Mass $= 12 + 16 + 2[14 + 2(1)] = 60.0\\text{ g mol}^{-1}$\n- Nitrogen Mass $= 2 \\times 14 = 28.0\\text{ g}$\n- $\\%\\text{ N} = \\frac{28.0}{60.0} \\times 100\\% = \\mathbf{46.67\\%}$",
                            "**Ammonium Sulphate [$(\\text{NH}_4)_2\\text{SO}_4$]**:\n- Formula Mass $= 2[14 + 4(1)] + 32 + 4(16) = 132.0\\text{ g mol}^{-1}$\n- Nitrogen Mass $= 2 \\times 14 = 28.0\\text{ g}$\n- $\\%\\text{ N} = \\frac{28.0}{132.0} \\times 100\\% = \\mathbf{21.21\\%}$",
                            "**Conclusion**: Urea is more than twice as nutrient-dense as ammonium sulphate."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Soil Acidification and Liming",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### What should a farmer do when ammonium fertiliser lowers soil pH?\nBacterial nitrification of ammonium salts releases $H^+$ ions, increasing soil acidity.\n\nTo restore soil fertility, farmers apply **agricultural lime (calcium carbonate, $\\text{CaCO}_3$)**, which neutralizes acidity and raises pH back to optimal levels."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Fertilisers",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following solid chemical fertilisers contains the highest percentage of nitrogen by mass?",
                        "options": [
                            "Ammonium Sulphate, $(\\text{NH}_4)_2\\text{SO}_4$",
                            "Urea, $\\text{CO(NH}_2)_2$",
                            "Ammonium Nitrate, $\\text{NH}_4\\text{NO}_3$",
                            "Calcium Ammonium Nitrate (CAN)"
                        ],
                        "answer": "B",
                        "explanation": "Urea contains 46.67% Nitrogen by mass, making it the most concentrated and nutrient-dense solid commercial nitrogen fertiliser."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Nitrogenous Fertilisers",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Fertilisers\n- **Nutrient Value**: Urea (46.67%) > Ammonium Nitrate (35.0%) > CAN (27.0%) > Ammonium Sulphate (21.21%).\n- **Soil Management**: Acidifying fertilisers require agricultural lime ($\text{CaCO}_3$) to restore pH.\n- **Eutrophication**: Soluble nitrate runoff causes algal blooms, bacterial oxygen consumption, and fish suffocation."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 4.5: Nitric(V) Acid (Laboratory Preparation and Industrial Manufacture)",
            "unit_order": 5,
            "lesson_title": "Nitric(V) Acid (Laboratory Preparation and Industrial Manufacture)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Dual Chemistry of Nitric(V) Acid",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore the laboratory preparation of nitric(V) acid ($\\text{HNO}_3$) using an all-glass retort, and master the industrial Ostwald process with its platinum-rhodium catalyst."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Acid That Dissolves Copper",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Pouring hydrochloric acid or dilute sulphuric acid onto copper turnings causes no reaction, as copper cannot displace hydrogen from typical acids.\n\nHowever, adding concentrated **Nitric(V) Acid ($\\text{HNO}_3$)** triggers an immediate, vigorous reaction, turning the solution emerald green and evolving reddish-brown $\\text{NO}_2$ fumes. Nitric(V) acid is both a strong acid and an aggressive **oxidising agent**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Preparation in an All-Glass Retort",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Reaction with Potassium Nitrate:\n$$\\text{KNO}_3\\text{(s)} + \\text{H}_2\\text{SO}_4\\text{(l)} \\xrightarrow{\\text{heat}} \\text{KHSO}_4\\text{(s)} + \\text{HNO}_3\\text{(g)}$$\n\n* **Why an All-Glass Retort?**\n  Hot $\\text{HNO}_3$ vapors are extraordinarily corrosive and rapidly dissolve rubber bungs, corks, and tubing. Glass apparatus resists this attack completely.\n* **Why Acid Salt ($\\text{KHSO}_4$) is Formed**:\n  Producing normal salt $\\text{K}_2\\text{SO}_4$ requires temperatures $>200^\\circ\\text{C}$, at which $\\text{HNO}_3$ decomposes and the glass retort cracks.\n* **Removal of Yellow Color**:\n  Condensed $\\text{HNO}_3$ appears yellow due to dissolved $\\text{NO}_2$ formed by thermal decomposition ($4\\text{HNO}_3 \\rightarrow 4\\text{NO}_2 + \\text{O}_2 + 2\\text{H}_2\\text{O}$). Bubbling dry air through the warm acid expels the $\\text{NO}_2$, restoring a pure colorless acid."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Nitric Acid Retort Apparatus",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Diagram of laboratory all-glass retort setup for nitric(V) acid preparation.",
                        "instruction": "Glass retort flask containing solid KNO3 and concentrated H2SO4 heated gently, with neck extending into a water-cooled glass receiver flask collecting liquid HNO3.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    },
                    "asset_info": {
                        "title": "All-Glass Retort Setup",
                        "description": "Apparatus diagram for laboratory preparation of nitric(V) acid.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Industrial Manufacture: The Ostwald Process",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Ostwald Process",
                        "content": "### Stage 1: Catalytic Ammonia Oxidation ($900^\\circ\\text{C}$)\n$$4\\text{NH}_3\\text{(g)} + 5\\text{O}_2\\text{(g)} \\xrightarrow[\\text{Pt-Rh Catalyst}]{900^\\circ\\text{C}} 4\\text{NO(g)} + 6\\text{H}_2\\text{O(g)} \\quad (\\text{Highly Exothermic})$$\n\n### Stage 2: Oxidation to $\\text{NO}_2$ ($< 45^\\circ\\text{C}$)\n$$2\\text{NO(g)} + \\text{O}_2\\text{(g)} \\xrightarrow{< 45^\\circ\\text{C}} 2\\text{NO}_2\\text{(g)}$$\n\n### Stage 3: Absorption Tower\n$$2\\text{NO}_2\\text{(g)} + \\text{H}_2\\text{O(l)} \\rightarrow \\text{HNO}_3\\text{(aq)} + \\text{HNO}_2\\text{(aq)}$$\n$$2\\text{HNO}_2\\text{(aq)} + \\text{O}_2\\text{(g)} \\rightarrow 2\\text{HNO}_3\\text{(aq)}$$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Calculating Gaseous Volumes in Ostwald Process",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "In Stage 1 of the Ostwald process, $1200\\text{ dm}^3$ of ammonia was oxidized completely by oxygen. Calculate the volume of nitrogen(II) oxide ($\\text{NO}$) produced under constant temperature and pressure.",
                        "steps": [
                            "**Step 1: Balanced Equation**:\n$$4\\text{NH}_3\\text{(g)} + 5\\text{O}_2\\text{(g)} \\rightarrow 4\\text{NO(g)} + 6\\text{H}_2\\text{O(g)}$$",
                            "**Step 2: Volume Ratio**:\n$$\\text{Ratio } \\text{NH}_3 : \\text{NO} = 4 : 4 = 1 : 1$$",
                            "**Step 3: Calculate Yield**:\n$$\\text{Volume of } \\text{NO} = 1200\\text{ dm}^3$$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Industrial Applications of Nitric(V) Acid",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Fertilisers, Explosives, and Metallurgy\n* **Fertilisers**: Neutralized with ammonia to produce ammonium nitrate fertiliser.\n* **Explosives**: Used in the manufacture of TNT and dynamite.\n* **Precious Metal Refining**: Dissolves copper and silver impurities while leaving pure gold unreacted."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Rubber Cannot Be Used with Nitric Acid",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why can't we use standard laboratory rubber stoppers?\nNitric(V) acid vapors are violently oxidizing. They oxidize and dissolve rubber, latex, and cork instantly, causing severe acid leaks and ruining experiments.\n\nAll-glass apparatus with ground glass joints is mandatory."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Nitric(V) Acid",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why must the apparatus used for the laboratory preparation of nitric(V) acid be made entirely of glass?",
                        "options": [
                            "Glass is a better conductor of heat than metals",
                            "Nitric(V) acid is a reducing agent that attacks copper",
                            "Nitric(V) acid vapor corrodes and destroys rubber and cork",
                            "Glass prevents the nitric(V) acid from evaporating"
                        ],
                        "answer": "C",
                        "explanation": "Nitric(V) acid vapor is a powerful oxidising agent that rapidly corrodes and dissolves rubber bungs and corks. An all-glass retort prevents chemical leaks."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Nitric(V) Acid",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Nitric(V) Acid\n- **Laboratory Preparation**: $\\text{KNO}_3\\text{(s)} + \\text{H}_2\\text{SO}_4\\text{(l)} \\rightarrow \\text{KHSO}_4\\text{(s)} + \\text{HNO}_3\\text{(g)}$ in all-glass retort.\n- **Ostwald Process**: $4\\text{NH}_3 + 5\\text{O}_2 \\xrightarrow{\\text{Pt-Rh, } 900^\\circ\\text{C}} 4\\text{NO} + 6\\text{H}_2\\text{O} \\rightarrow \\text{NO}_2 \\rightarrow \\text{HNO}_3$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 4.6: Chemical Reactions of Nitric(V) Acid and Nitrates",
            "unit_order": 6,
            "lesson_title": "Chemical Reactions of Nitric(V) Acid and Nitrates",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Chemical Reactions of Nitrates",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will investigate the oxidising and nitrating reactions of nitric(V) acid with metals and non-metals, examine the thermal decomposition of metal nitrates, and perform the brown-ring confirmatory test."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Acidic vs Oxidising Reactions",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Nitric(V) acid exhibits a remarkable dual nature:\n\n* **As a Typical Mineral Acid**: Neutralizes metal oxides and hydroxides into nitrate salts and water, and liberates $\\text{CO}_2$ from carbonates.\n* **As a Powerful Oxidising Agent**: Oxidizes metals (producing $\\text{NO}$ or $\\text{NO}_2$ instead of hydrogen gas), non-metals (sulphur to $\\text{H}_2\\text{SO}_4$), and $\\text{Fe}^{2+}$ to $\\text{Fe}^{3+}$."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Oxidising Reactions with Metals and Non-Metals",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Key Redox Reactions:\n* **With Dilute $\\text{HNO}_3$ (50%) and Copper**:\n  $$3\\text{Cu(s)} + 8\\text{HNO}_3\\text{(aq)} \\rightarrow 3\\text{Cu(NO}_3)_2\\text{(aq)} + 4\\text{H}_2\\text{O(l)} + 2\\text{NO(g)}$$\n* **With Concentrated $\\text{HNO}_3$ and Copper**:\n  $$\\text{Cu(s)} + 4\\text{HNO}_3\\text{(l)} \\rightarrow \\text{Cu(NO}_3)_2\\text{(aq)} + 2\\text{NO}_2\\text{(g)} + 2\\text{H}_2\\text{O(l)}$$\n* **Oxidation of Non-Metals**:\n  - Sulphur: $\\text{S} + 6\\text{HNO}_3 \\rightarrow \\text{H}_2\\text{SO}_4 + 6\\text{NO}_2 + 2\\text{H}_2\\text{O}$\n  - Carbon: $\\text{C} + 4\\text{HNO}_3 \\rightarrow \\text{CO}_2 + 4\\text{NO}_2 + 2\\text{H}_2\\text{O}$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Action of Heat on Metal Nitrates",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Action of Heat on Nitrates",
                        "content": "### Reactivity-Based Decomposition:\n* **Potassium & Sodium**: Form Metal Nitrite + $\\text{O}_2$\n  $$2\\text{KNO}_3\\text{(s)} \\xrightarrow{\\text{heat}} 2\\text{KNO}_2\\text{(s)} + \\text{O}_2\\text{(g)}$$\n* **Calcium to Copper**: Form Metal Oxide + $\\text{NO}_2$ (brown) + $\\text{O}_2$\n  $$2\\text{Pb(NO}_3)_2\\text{(s)} \\xrightarrow{\\text{heat}} 2\\text{PbO(s)} + 4\\text{NO}_2\\text{(g)} + \\text{O}_2\\text{(g)}$$\n* **Silver & Mercury**: Form Pure Metal + $\\text{NO}_2$ + $\\text{O}_2$\n  $$2\\text{AgNO}_3\\text{(s)} \\xrightarrow{\\text{heat}} 2\\text{Ag(s)} + 2\\text{NO}_2\\text{(g)} + \\text{O}_2\\text{(g)}$$\n* **Ammonium Nitrate**: Forms $\\text{N}_2\\text{O}$ + $\\text{H}_2\\text{O}$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "The Brown Ring Test for Nitrate Ions",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Brown Ring Test Protocol",
                        "content": "### Procedure:\n1. Add freshly prepared iron(II) sulphate ($\\text{FeSO}_4$) to the nitrate solution.\n2. Slant test tube and slowly trickle concentrated sulphuric acid down the inner wall.\n3. Dense $\\text{H}_2\\text{SO}_4$ forms a bottom layer.\n4. A **dark-brown ring of nitroso-iron(II) sulphate complex** forms at the boundary:\n$$\\text{FeSO}_4\\text{(aq)} + \\text{NO(g)} \\rightarrow \\text{FeSO}_4\\cdot\\text{NO(s)}$$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Calculating Gaseous Products from Nitrate Heating",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate total volume of gases evolved at S.T.P. when $6.62\\text{ g}$ of lead(II) nitrate is decomposed completely ($Pb=207, N=14, O=16$, $V_m=22.4\\text{ dm}^3\\text{ mol}^{-1}$).",
                        "steps": [
                            "**Step 1: Balanced Equation**:\n$$2\\text{Pb(NO}_3)_2 \\rightarrow 2\\text{PbO} + 4\\text{NO}_2\\text{(g)} + \\text{O}_2\\text{(g)}$$",
                            "**Step 2: Moles of Reactant**:\n- Molar mass $= 331\\text{ g mol}^{-1}$\n- Moles $= \\frac{6.62}{331} = 0.02\\text{ mol}$",
                            "**Step 3: Moles of Gaseous Products**:\n- $2\\text{ moles of nitrate} \\rightarrow 5\\text{ moles of gas } (4\\text{ NO}_2 + 1\\text{ O}_2)$\n- Moles of gas $= 0.02 \\times 2.5 = 0.05\\text{ mol}$",
                            "**Step 4: Total Volume at S.T.P.**:\n$$\\text{Volume} = 0.05\\text{ mol} \\times 22.4\\text{ dm}^3/\\text{mol} = 1.12\\text{ dm}^3 \\quad (1120\\text{ cm}^3)$$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Environmental Pollution and Catalytic Converters",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Acid Rain and Automotive Mitigation\n* **Acid Rain**: $\\text{NO}_2$ emissions dissolve in clouds, corroding buildings and leaching toxic aluminium into soil.\n* **Catalytic Converters**: Vehicle exhausts use platinum-rhodium converters to reduce nitrogen oxides to harmless nitrogen gas:\n  $$2\\text{NO}_2\\text{(g)} + 4\\text{CO(g)} \\rightarrow \\text{N}_2\\text{(g)} + 4\\text{CO}_2\\text{(g)}$$"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Think About This: Why Silver Nitrate Yields Pure Metal",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does silver nitrate decompose to pure silver instead of silver oxide?\nSilver is very low in the reactivity series. Silver oxide ($\\text{Ag}_2\\text{O}$) is thermally unstable at the high temperatures required for decomposition, breaking down immediately into **pure shiny silver metal** and oxygen."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Practice Questions: Reactions of Nitrates",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following nitrates decomposes on strong heating to produce a metal, a reddish-brown gas, and a colorless gas that relights a glowing splint?",
                        "options": [
                            "Sodium nitrate, $\\text{NaNO}_3$",
                            "Silver nitrate, $\\text{AgNO}_3$",
                            "Lead(II) nitrate, $\\text{Pb(NO}_3)_2$",
                            "Ammonium nitrate, $\\text{NH}_4\\text{NO}_3$"
                        ],
                        "answer": "B",
                        "explanation": "Silver nitrate decomposes into pure silver metal ($\\text{Ag}$), reddish-brown nitrogen(IV) oxide ($\\text{NO}_2$), and oxygen gas ($\\text{O}_2$). Lead(II) nitrate produces an oxide, not a metal."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Nitrates and Acid Reactions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Nitrates & Reactions\n- **Dual Nature**: Neutralizes bases (typical acid); oxidizes metals and non-metals without liberating hydrogen gas.\n- **Decomposition**: $K/Na \\rightarrow$ Nitrite; Heavy metals $\\rightarrow$ Oxide; $Ag/Hg \\rightarrow$ Metal; $\\text{NH}_4\\text{NO}_3 \\rightarrow \\text{N}_2\\text{O}$.\n- **Brown Ring Test**: Confirms $\\text{NO}_3^-$ via $\\text{FeSO}_4\\cdot\\text{NO}$ complex."
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
            block_id = f"f3_chem_t4_l{lesson.id}_b{order}_{uuid.uuid4().hex[:6]}"
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
    print("Ingestion Completed Successfully! All 6 Modules Published to Form 3 Topic 4.")
    print("================================================================================")

if __name__ == "__main__":
    ingest_form3_topic4_nitrogen()
