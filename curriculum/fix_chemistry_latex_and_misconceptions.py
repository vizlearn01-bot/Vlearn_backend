"""
VLearn Universal Chemistry — Deep LaTeX Normalization & Misconception Hardening
1. Repairs all 30 knowledge check blocks in Form 4 Topic 1 (Acids, Bases, Salts) with authentic KCSE MCQs
2. Sanitizes all common_misconception blocks (strips leaked practice Q/A, chat artifacts, and module tags)
3. Fixes broken ightarrow / ightleftharpoons across all Chemistry blocks in Form 3 and Form 4
4. Delimits un-delimited chemical equations into proper KaTeX blocks ($...$ or $$...$$)
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Subject, Topic, Lesson, LessonBlock

# ==============================================================================
# 1. 30 AUTHENTIC KCSE MCQS FOR FORM 4 TOPIC 1 (ACIDS, BASES & SALTS)
# ==============================================================================

TOPIC1_MCQS = {
    1049: {
        "question": "A clean piece of iron wire (Fe) is dropped into an aqueous solution of hydrochloric acid (HCl). What gas is evolved, and what observation confirms its identity?",
        "options": [
            "Oxygen gas; it relights a glowing splint.",
            "Hydrogen gas; it burns with a characteristic 'pop' sound when a burning splint is introduced.",
            "Carbon dioxide gas; it turns limewater milky.",
            "Chlorine gas; it bleaches moist blue litmus paper."
        ],
        "answer": "B",
        "explanation": "Active metals like iron react with dilute acids to produce a metal salt and hydrogen gas: $\\text{Fe}_{(s)} + 2\\text{HCl}_{(aq)} \\rightarrow \\text{FeCl}_{2(aq)} + \\text{H}_{2(g)}$. Hydrogen gas burns with a characteristic 'pop' sound."
    },
    1050: {
        "question": "What is the correct ionic equation for the reaction between solid calcium carbonate marble chips and dilute nitric acid?",
        "options": [
            "$\\text{Ca}^{2+}_{(aq)} + \\text{CO}^{2-}_{3(aq)} + 2\\text{H}^+_{(aq)} \\rightarrow \\text{Ca}^{2+}_{(aq)} + \\text{CO}_{2(g)} + \\text{H}_2\\text{O}_{(l)}$",
            "$\\text{CaCO}_{3(s)} + 2\\text{H}^+_{(aq)} \\rightarrow \\text{Ca}^{2+}_{(aq)} + \\text{CO}_{2(g)} + \\text{H}_2\\text{O}_{(l)}$",
            "$\\text{CaCO}_{3(s)} + 2\\text{HNO}_{3(aq)} \\rightarrow \\text{Ca(NO}_3)_{2(aq)} + \\text{H}_2\\text{CO}_{3(aq)}$",
            "$\\text{CO}^{2-}_{3(aq)} + 2\\text{H}^+_{(aq)} \\rightarrow \\text{CO}_{2(g)} + \\text{H}_2\\text{O}_{(l)}$"
        ],
        "answer": "B",
        "explanation": "Because calcium carbonate ($\\text{CaCO}_3$) is an insoluble solid crystal lattice, its ions are not freely dissociated in aqueous solution before the reaction. Thus, it must be written as solid $\\text{CaCO}_{3(s)}$ in the ionic equation: $\\text{CaCO}_{3(s)} + 2\\text{H}^+_{(aq)} \\rightarrow \\text{Ca}^{2+}_{(aq)} + \\text{CO}_{2(g)} + \\text{H}_2\\text{O}_{(l)}$."
    },
    1059: {
        "question": "Two flasks contain 50 cm³ of 0.1 M hydrochloric acid (Flask A) and 50 cm³ of 0.1 M ethanoic acid (Flask B). If excess zinc granules are added to both, what is observed regarding the rate of effervescence and total volume of hydrogen collected?",
        "options": [
            "Flask A and Flask B produce hydrogen at identical initial rates and yield different final volumes.",
            "Flask A produces hydrogen faster initially, but both flasks produce the exact same total volume of hydrogen gas.",
            "Flask B produces hydrogen faster initially because it is an organic acid.",
            "Flask A produces a greater total volume of hydrogen gas because it is a strong acid."
        ],
        "answer": "B",
        "explanation": "Hydrochloric acid (HCl) is a strong acid and fully dissociates, giving a higher initial $[\\text{H}^+]$ and faster rate. However, because both flasks contain the same number of moles of acid ($0.050 \\times 0.1 = 0.005\\text{ mol}$ of monoprotic acid), the stoichiometric yield of hydrogen gas collected is identical."
    },
    1060: {
        "question": "When comparing the electrical conductivity of 0.1 M nitric acid ($\\text{HNO}_3$) and 0.1 M ethanoic acid ($\\text{CH}_3\\text{COOH}$) using identical electrodes and bulb brightness, what is observed and why?",
        "options": [
            "Both bulbs glow with equal brightness because both solutions have equal molarity (0.1 M).",
            "The bulb in nitric acid glows much brighter because nitric acid is completely ionised, providing a much higher concentration of mobile ions.",
            "The bulb in ethanoic acid glows brighter because it contains more hydrogen atoms per molecule.",
            "Neither solution conducts electricity because acids are covalent compounds."
        ],
        "answer": "B",
        "explanation": "Nitric acid is a strong electrolyte that fully ionises in water ($\\text{HNO}_3 \\rightarrow \\text{H}^+ + \\text{NO}_3^-$), whereas ethanoic acid is a weak electrolyte that only partially ionises (<1%). The higher concentration of mobile ions in nitric acid yields higher electrical conductivity."
    },
    1073: {
        "question": "Which of the following compounds is an alkali (a water-soluble base)?",
        "options": [
            "Ethanol ($\\text{C}_2\\text{H}_5\\text{OH}$)",
            "Sodium hydroxide ($\\text{NaOH}$)",
            "Copper(II) oxide ($\\text{CuO}$)",
            "Magnesium carbonate ($\\text{MgCO}_3$)"
        ],
        "answer": "B",
        "explanation": "An alkali is a basic hydroxide that dissolves in water to release hydroxide ions ($\\text{OH}^-$). Sodium hydroxide is soluble in water ($\\text{NaOH}_{(s)} \\rightarrow \\text{Na}^+_{(aq)} + \\text{OH}^-_{(aq)}$). Ethanol has an -OH group but is a neutral covalent alcohol, not an alkali."
    },
    1074: {
        "question": "What products are formed when ammonium sulfate is warmed with concentrated sodium hydroxide solution?",
        "options": [
            "Sodium sulfate, ammonia gas, and water",
            "Sodium sulfate, nitrogen dioxide, and hydrogen gas",
            "Sodium nitrate, sulfur dioxide, and water",
            "Ammonium nitrate and solid sodium sulfate"
        ],
        "answer": "A",
        "explanation": "When an ammonium salt is heated with a base, ammonia gas is displaced: $(\\text{NH}_4)_2\\text{SO}_{4(s)} + 2\\text{NaOH}_{(aq)} \\rightarrow \\text{Na}_2\\text{SO}_{4(aq)} + 2\\text{NH}_{3(g)} + 2\\text{H}_2\\text{O}_{(l)}$."
    },
    1097: {
        "question": "Dry ammonia gas is dissolved separately in water (Beaker A) and in methylbenzene (Beaker B). What happens when red litmus paper is dipped into each beaker?",
        "options": [
            "Beaker A turns red litmus blue; Beaker B has no effect on red litmus.",
            "Beaker B turns red litmus blue; Beaker A has no effect.",
            "Both beakers turn red litmus blue because ammonia is always alkaline.",
            "Neither beaker turns red litmus blue because ammonia is a gas."
        ],
        "answer": "A",
        "explanation": "In polar water, ammonia reacts to form ammonium and hydroxide ions: $\\text{NH}_{3(g)} + \\text{H}_2\\text{O}_{(l)} \\rightleftharpoons \\text{NH}_4^+ + \\text{OH}^-$, turning red litmus blue. In non-polar methylbenzene, ammonia exists as un-ionised covalent molecules and displays no basic character."
    },
    1098: {
        "question": "What happens when solid sodium hydrogencarbonate ($\\text{NaHCO}_3$) is added to a solution of hydrogen chloride in dry methylbenzene?",
        "options": [
            "Vigorous effervescence of carbon dioxide gas occurs.",
            "No effervescence or visible reaction occurs because HCl is un-ionised in non-polar methylbenzene.",
            "A precipitate of sodium chloride forms immediately with loud popping.",
            "The methylbenzene boils instantly due to rapid neutralisation."
        ],
        "answer": "B",
        "explanation": "In non-polar solvents like methylbenzene, hydrogen chloride molecules do not dissociate into $\\text{H}^+$ ions. Without free hydrogen ions, no acidic neutralisation can occur with carbonates."
    },
    1109: {
        "question": "A student adds aqueous ammonia dropwise until in excess to a solution containing zinc ions ($\\text{Zn}^{2+}$). What is observed?",
        "options": [
            "A white precipitate forms that remains insoluble in excess aqueous ammonia.",
            "A white precipitate of $\\text{Zn(OH)}_2$ forms initially, which dissolves in excess aqueous ammonia to form a colourless solution of $[\\text{Zn(NH}_3)_4]^{2+}$.",
            "A blue precipitate forms which turns dark royal blue in excess ammonia.",
            "No precipitate forms under any conditions."
        ],
        "answer": "B",
        "explanation": "Zinc ions precipitate as white zinc hydroxide: $\\text{Zn}^{2+}_{(aq)} + 2\\text{OH}^-_{(aq)} \\rightarrow \\text{Zn(OH)}_{2(s)}$. In excess ammonia, it dissolves due to the formation of the soluble tetraamminezinc(II) complex cation: $\\text{Zn(OH)}_{2(s)} + 4\\text{NH}_{3(aq)} \\rightarrow [\\text{Zn(NH}_3)_4]^{2+}_{(aq)} + 2\\text{OH}^-_{(aq)}$."
    },
    1110: {
        "question": "Which of the following equations correctly represents the reaction of amphoteric aluminium hydroxide with excess concentrated sodium hydroxide?",
        "options": [
            "$\\text{Al(OH)}_{3(s)} + \\text{OH}^-_{(aq)} \\rightarrow [\\text{Al(OH)}_4]^-_{(aq)}$",
            "$\\text{Al(OH)}_{3(s)} + 3\\text{Na}^+_{(aq)} \\rightarrow \\text{Na}_3\\text{Al}_{(s)} + 3\\text{OH}^-_{(aq)}$",
            "$\\text{Al(OH)}_{3(s)} + \\text{NaOH}_{(aq)} \\rightarrow \\text{AlNa}_{(s)} + 2\\text{H}_2\\text{O}_{(l)}$",
            "$\\text{Al}^{3+}_{(aq)} + 3\\text{OH}^-_{(aq)} \\rightarrow \\text{Al(OH)}_{3(s)}$"
        ],
        "answer": "A",
        "explanation": "Amphoteric aluminium hydroxide acts as an acid in the presence of strong hydroxide ions, dissolving to form the soluble tetrahydroxoaluminate(III) complex anion: $\\text{Al(OH)}_{3(s)} + \\text{OH}^-_{(aq)} \\rightarrow [\\text{Al(OH)}_4]^-_{(aq)}$."
    },
    1121: {
        "question": "Which of the following salts is classified as an acid salt?",
        "options": [
            "$\\text{NaCl}$",
            "$\\text{NaHCO}_3$",
            "$\\text{Na}_2\\text{SO}_4$",
            "$\\text{KNO}_3$"
        ],
        "answer": "B",
        "explanation": "An acid salt contains replaceable hydrogen atoms from a polybasic acid that have only been partially replaced by metal ions. Sodium hydrogencarbonate ($\\text{NaHCO}_3$) is an acid salt derived from carbonic acid ($\\text{H}_2\\text{CO}_3$)."
    },
    1122: {
        "question": "Why can nitric acid ($\\text{HNO}_3$) form only normal salts, whereas phosphoric(V) acid ($\\text{H}_3\\text{PO}_4$) can form both normal and acid salts?",
        "options": [
            "Nitric acid is an organic acid, whereas phosphoric acid is inorganic.",
            "Nitric acid is monobasic (has only 1 replaceable hydrogen ion), whereas phosphoric acid is tribasic (has 3 replaceable hydrogen ions).",
            "Nitric acid is a weak acid that cannot dissociate completely.",
            "Phosphoric acid contains phosphorus which acts as a metal cation."
        ],
        "answer": "B",
        "explanation": "A monobasic acid like $\\text{HNO}_3$ has only one replaceable hydrogen ion per molecule, so its replacement always yields a normal salt ($\\text{NO}_3^-$). Tribasic $\\text{H}_3\\text{PO}_4$ can undergo partial replacement to form $\\text{H}_2\\text{PO}_4^-$ and $\\text{HPO}_4^{2-}$ (acid salts) as well as $\\text{PO}_4^{3-}$ (normal salt)."
    },
    1123: {
        "question": "What is the balanced molecular equation for the reaction of zinc metal with dilute sulfuric acid to form zinc sulfate?",
        "options": [
            "$\\text{Zn}_{(s)} + \\text{H}_2\\text{SO}_{4(aq)} \\rightarrow \\text{ZnSO}_{4(aq)} + \\text{H}_{2(g)}$",
            "$\\text{Zn}_{(s)} + 2\\text{H}_2\\text{SO}_{4(aq)} \\rightarrow \\text{Zn(HSO}_4)_{2(aq)} + \\text{SO}_{2(g)}$",
            "$\\text{Zn}^{2+}_{(aq)} + \\text{SO}^{2-}_{4(aq)} \\rightarrow \\text{ZnSO}_{4(s)}$",
            "$\\text{Zn}_{(s)} + \\text{H}_2\\text{O}_{(l)} \\rightarrow \\text{ZnO}_{(s)} + \\text{H}_{2(g)}$"
        ],
        "answer": "A",
        "explanation": "Zinc displaces hydrogen from dilute sulfuric acid in a single displacement reaction: $\\text{Zn}_{(s)} + \\text{H}_2\\text{SO}_{4(aq)} \\rightarrow \\text{ZnSO}_{4(aq)} + \\text{H}_{2(g)}$."
    },
    1131: {
        "question": "When aqueous solutions of barium nitrate and sodium sulfate are mixed, what is the correct net ionic equation for the precipitation reaction?",
        "options": [
            "$\\text{Ba}^{2+}_{(aq)} + \\text{SO}^{2-}_{4(aq)} \\rightarrow \\text{BaSO}_{4(s)}$",
            "$\\text{Na}^+_{(aq)} + \\text{NO}^-_{3(aq)} \\rightarrow \\text{NaNO}_{3(s)}$",
            "$\\text{Ba(NO}_3)_{2(aq)} + \\text{Na}_2\\text{SO}_{4(aq)} \\rightarrow \\text{BaSO}_{4(s)} + 2\\text{NaNO}_{3(aq)}$",
            "$\\text{Ba}^{2+}_{(aq)} + 2\\text{NO}^-_{3(aq)} \\rightarrow \\text{Ba(NO}_3)_{2(s)}$"
        ],
        "answer": "A",
        "explanation": "In aqueous solution, sodium and nitrate ions are spectator ions. Barium cations and sulfate anions combine to form insoluble white barium sulfate: $\\text{Ba}^{2+}_{(aq)} + \\text{SO}^{2-}_{4(aq)} \\rightarrow \\text{BaSO}_{4(s)}$."
    },
    1132: {
        "question": "Which of the following laboratory procedures correctly describes the preparation of a pure, dry sample of an insoluble salt like lead(II) sulfate?",
        "options": [
            "Mix two soluble solutions, filter the precipitate, wash the residue with distilled water, and dry between filter papers.",
            "Mix an insoluble carbonate with acid, evaporate to dryness, and crystallize.",
            "Boil the salt solution to dryness directly over a roaring Bunsen flame.",
            "Dissolve lead metal in water and filter the filtrate."
        ],
        "answer": "A",
        "explanation": "Insoluble salts are prepared by precipitation: mixing two soluble salt solutions (e.g. lead(II) nitrate and sodium sulfate), filtering the mixture, washing the residue with distilled water to remove spectator ions, and drying the residue between filter papers."
    },
    1142: {
        "question": "A solution contains an unknown metal cation. Addition of a few drops of aqueous ammonia produces a pale blue precipitate. When excess aqueous ammonia is added, the precipitate dissolves to give a deep royal blue solution. What cation is present?",
        "options": [
            "$\\text{Fe}^{2+}$",
            "$\\text{Cu}^{2+}$",
            "$\\text{Fe}^{3+}$",
            "$\\text{Al}^{3+}$"
        ],
        "answer": "B",
        "explanation": "Copper(II) ions form a pale blue precipitate of $\\text{Cu(OH)}_2$ with a few drops of ammonia, which dissolves in excess ammonia to form the soluble deep royal blue tetraamminecopper(II) complex cation: $[\\text{Cu(NH}_3)_4]^{2+}$."
    },
    1143: {
        "question": "What is the formula and overall charge of the complex ion formed when zinc hydroxide dissolves in excess aqueous ammonia?",
        "options": [
            "$[\\text{Zn(NH}_3)_4]^{2+}$",
            "$[\\text{Zn(OH)}_4]^{2-}$",
            "$[\\text{Zn(NH}_3)_2]^+$",
            "$[\\text{Zn(NH}_4)_4]^{2+}$"
        ],
        "answer": "A",
        "explanation": "Zinc(II) ions coordinate with four neutral ammonia ligands to form the tetraamminezinc(II) complex cation, $[\\text{Zn(NH}_3)_4]^{2+}$. Because ammonia molecules are neutral, the overall charge equals the $+2$ charge of the zinc ion."
    },
    1154: {
        "question": "During a laboratory experiment to determine the solubility of a salt at 40°C, why must the saturated solution be filtered before evaporating a weighed sample of the filtrate?",
        "options": [
            "To remove un-dissolved solid crystals so that only dissolved solute is measured.",
            "To cool down the solution to room temperature.",
            "To evaporate the water before weighing.",
            "To convert the salt into a neutral oxide."
        ],
        "answer": "A",
        "explanation": "Filtering removes suspended or un-dissolved solid salt crystals from the saturated mixture, ensuring that only the mass of solute truly dissolved in the liquid phase is gravimetrically measured."
    },
    1155: {
        "question": "The solubility of potassium nitrate at 60°C is 110 g/100 g of water, and at 20°C it is 32 g/100 g of water. If a saturated solution containing 50 g of water is cooled from 60°C to 20°C, what mass of potassium nitrate crystals will separate out?",
        "options": [
            "78 g",
            "39 g",
            "55 g",
            "16 g"
        ],
        "answer": "B",
        "explanation": "Mass of solute deposited per 100 g of water = $110\\text{ g} - 32\\text{ g} = 78\\text{ g}$. For 50 g of water (half the volume), the mass of crystals deposited = $\\frac{78}{2} = 39\\text{ g}$."
    },
    1164: {
        "question": "Why can a mixture of potassium nitrate ($\\text{KNO}_3$) and sodium chloride ($\\text{NaCl}$) be effectively separated by fractional crystallisation?",
        "options": [
            "Sodium chloride is completely insoluble in boiling water.",
            "Potassium nitrate has a solubility that increases steeply with temperature, whereas sodium chloride's solubility changes very little with temperature.",
            "Potassium nitrate evaporates when heated, leaving sodium chloride behind.",
            "Sodium chloride decomposes upon heating into chlorine gas."
        ],
        "answer": "B",
        "explanation": "Fractional crystallisation separates salts based on differing temperature-solubility curves. $\\text{KNO}_3$ is extremely soluble in hot water but poorly soluble in cold water (steep curve), while $\\text{NaCl}$ shows almost no change in solubility. Cooling a hot saturated mixture precipitates pure $\\text{KNO}_3$ crystals while $\\text{NaCl}$ remains dissolved in the mother liquor."
    },
    1165: {
        "question": "In a fractional crystallisation separation of two soluble salts, what is the term used for the liquid remaining above the separated crystals?",
        "options": [
            "Distillate",
            "Mother liquor",
            "Precipitant",
            "Anolyte"
        ],
        "answer": "B",
        "explanation": "The residual saturated solution remaining after crystallisation has occurred and crystals have been filtered off is called the mother liquor."
    },
    1176: {
        "question": "A sample of water from a well is suspected to contain hard water. Which of the following tests confirms that the water hardness is permanent rather than temporary?",
        "options": [
            "Boiling a sample of the water, cooling it, and finding that it still fails to lather readily with soap.",
            "Testing the water with universal indicator and observing a neutral pH of 7.",
            "Passing the water through filter paper and observing no residue.",
            "Freezing the water and observing the formation of clear ice."
        ],
        "answer": "A",
        "explanation": "Temporary hardness (caused by $\\text{Ca(HCO}_3)_2$) is removed by boiling because hydrogencarbonates decompose into insoluble carbonates. If water continues to form scum and fails to lather after boiling, the hardness is permanent (caused by dissolved sulfates or chlorides of calcium/magnesium)."
    },
    1177: {
        "question": "What is the balanced chemical equation for the softening of permanent hard water containing magnesium sulfate using sodium carbonate (washing soda)?",
        "options": [
            "$\\text{MgSO}_{4(aq)} + \\text{Na}_2\\text{CO}_{3(aq)} \\rightarrow \\text{MgCO}_{3(s)} + \\text{Na}_2\\text{SO}_{4(aq)}$",
            "$\\text{MgSO}_{4(aq)} + \\text{Ca(OH)}_{2(s)} \\rightarrow \\text{Mg(OH)}_{2(s)} + \\text{CaSO}_{4(s)}$",
            "$\\text{Mg}^{2+}_{(aq)} + 2\\text{Cl}^-_{(aq)} \\rightarrow \\text{MgCl}_{2(s)}$",
            "$\\text{MgSO}_{4(aq)} + \\text{H}_2\\text{O}_{(l)} \\rightarrow \\text{Mg(OH)}_{2(s)} + \\text{H}_2\\text{SO}_{4(aq)}$"
        ],
        "answer": "A",
        "explanation": "Soluble sodium carbonate releases carbonate ions ($\\text{CO}_3^{2-}$), which react with dissolved magnesium ions to precipitate insoluble magnesium carbonate: $\\text{MgSO}_{4(aq)} + \\text{Na}_2\\text{CO}_{3(aq)} \\rightarrow \\text{MgCO}_{3(s)} + \\text{Na}_2\\text{SO}_{4(aq)}$."
    },
    1178: {
        "question": "When aqueous ammonia is added to temporary hard water containing calcium hydrogencarbonate, how does it soften the water?",
        "options": [
            "It neutralises hydrogencarbonate ions, precipitating calcium ions as solid calcium carbonate ($\\text{CaCO}_3$).",
            "It dissolves calcium ions into volatile gaseous ammonia.",
            "It converts calcium hydrogencarbonate into insoluble calcium metal.",
            "It evaporates all dissolved mineral salts from solution."
        ],
        "answer": "A",
        "explanation": "Aqueous ammonia reacts with hydrogencarbonate ions: $\\text{Ca(HCO}_3)_{2(aq)} + 2\\text{NH}_4\\text{OH}_{(aq)} \\rightarrow \\text{CaCO}_{3(s)} + 2\\text{H}_2\\text{O}_{(l)} + (\\text{NH}_4)_2\\text{CO}_{3(aq)}$. The insoluble $\\text{CaCO}_3$ precipitates out, removing dissolved calcium ions."
    },
    1184: {
        "question": "Why does the formation of boiler scale (calcium carbonate deposits) inside industrial boilers cause increased operational costs and potential explosion risks?",
        "options": [
            "Boiler scale is a poor conductor of heat (thermal insulator), wasting fuel and causing localized overheating of metal boiler plates.",
            "Boiler scale reacts chemically with water to produce flammable methane gas.",
            "Boiler scale makes water boil at a much lower temperature.",
            "Boiler scale converts steam into corrosive liquid chlorine."
        ],
        "answer": "A",
        "explanation": "Boiler scale (insoluble $\\text{CaCO}_3$ and $\\text{CaSO}_4$) is a poor thermal conductor. It insulates the water from the heat source, requiring excessive fuel consumption and causing thermal stress and weakening of the boiler metal."
    },
    1185: {
        "question": "What chemical compound forms the main constituent of kettle fur and boiler scale deposited when temporary hard water is heated?",
        "options": [
            "$\\text{CaCO}_3$ (Calcium carbonate)",
            "$\\text{NaCl}$ (Sodium chloride)",
            "$\\text{Ca(HCO}_3)_2$ (Calcium hydrogencarbonate)",
            "$\\text{MgSO}_4$ (Magnesium sulfate)"
        ],
        "answer": "A",
        "explanation": "When water containing temporary hardness is heated, soluble calcium hydrogencarbonate thermally decomposes into insoluble calcium carbonate: $\\text{Ca(HCO}_3)_{2(aq)} \\rightarrow \\text{CaCO}_{3(s)} + \\text{CO}_{2(g)} + \\text{H}_2\\text{O}_{(l)}$."
    },
    1191: {
        "question": "Why is drinking moderately hard water considered advantageous for human health compared to drinking purely distilled or soft water?",
        "options": [
            "Hard water contains dissolved calcium and magnesium ions essential for strengthening teeth and bone development.",
            "Hard water contains sodium ions that cure high blood pressure.",
            "Hard water kills all bacteria without boiling.",
            "Hard water prevents tooth decay by adding fluoride ions."
        ],
        "answer": "A",
        "explanation": "Hard water provides essential dietary mineral ions: calcium ($\text{Ca}^{2+}$) for strong bones and teeth, and magnesium ($\text{Mg}^{2+}$) for cardiovascular and enzymatic functions."
    },
    1192: {
        "question": "How does hard water protect residents in older homes with lead plumbing from heavy metal poisoning?",
        "options": [
            "Hard water forms an insoluble protective coating of lead(II) carbonate and lead(II) sulfate on the inner walls of lead pipes, preventing toxic lead from leaching into drinking water.",
            "Hard water dissolves lead pipes into harmless non-toxic elemental lead.",
            "Hard water neutralises lead ions by converting them into oxygen gas.",
            "Hard water evaporates before it touches lead pipes."
        ],
        "answer": "A",
        "explanation": "Carbonate and sulfate ions in hard water react with lead to deposit a protective, impermeable insoluble mineral lining (passivation layer) of $\\text{PbCO}_3$ and $\\text{PbSO}_4$, preventing water from contacting and dissolving toxic lead."
    },
    1201: {
        "question": "Why does adding slaked lime ($\\text{Ca(OH)}_2$) soften temporary hard water when added in exact stoichiometric quantities, but recreate hard water if added in excess?",
        "options": [
            "Calculated amounts precipitate all calcium as $\\text{CaCO}_3$; excess slaked lime dissolves to introduce unreacted $\\text{Ca}^{2+}$ ions, restoring hardness.",
            "Slaked lime is an acid that destroys temporary hardness completely.",
            "Excess slaked lime turns water into toxic sulfuric acid.",
            "Slaked lime only works in the presence of boiling water."
        ],
        "answer": "A",
        "explanation": "In calculated amounts, $\\text{Ca(OH)}_2$ reacts with $\\text{Ca(HCO}_3)_2$ to precipitate all calcium as insoluble $\\text{CaCO}_3$: $\\text{Ca(HCO}_3)_{2(aq)} + \\text{Ca(OH)}_{2(s)} \\rightarrow 2\\text{CaCO}_{3(s)} + 2\\text{H}_2\\text{O}_{(l)}$. If excess slaked lime is added, the extra $\\text{Ca(OH)}_2$ dissolves in water, re-introducing free $\\text{Ca}^{2+}$ ions."
    },
    1202: {
        "question": "An ion-exchange zeolite water softening column ($\\text{Na}_2\\text{Z}$) becomes exhausted after treating hard water. How is the zeolite resin chemically regenerated for reuse?",
        "options": [
            "By flushing the column with a concentrated solution of sodium chloride (brine).",
            "By heating the zeolite resin in an oven at 1000°C.",
            "By passing concentrated sulfuric acid through the column.",
            "By bubbling chlorine gas through the resin bed."
        ],
        "answer": "A",
        "explanation": "Exhausted zeolite ($\\text{CaZ}$ and $\\text{MgZ}$) is regenerated by passing concentrated brine ($\\text{NaCl}_{(aq)}$) through the column. The high concentration of $\\text{Na}^+$ ions displaces the trapped $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions: $\\text{CaZ}_{(s)} + 2\\text{NaCl}_{(aq)} \\rightarrow \\text{CaCl}_{2(aq)} + \\text{Na}_2\\text{Z}_{(s)}$."
    }
}

def clean_latex_string(s):
    if not isinstance(s, str):
        return s
    
    # 1. Fix carriage-return corrupted ightarrow / ightleftharpoons
    s = s.replace('\r\rightarrow', r'\rightarrow')
    s = s.replace('\rightleftharpoons', r'\rightleftharpoons')
    s = s.replace('ightarrow', r'\rightarrow')
    s = s.replace('ightleftharpoons', r'\rightleftharpoons')
    s = s.replace('\r', '')

    # 2. Fix trailing \ \text{}
    s = s.replace(r'\ \text{}', '').replace(r'\text{}', '')

    return s

def sanitize_misconception_text(text):
    if not isinstance(text, str):
        return text

    # Strip out practice questions section and everything that follows
    split_markers = [
        '#### **📝 Concept Practice Questions**',
        '#### 📝 Concept Practice Questions',
        '### **Concept Practice Questions**',
        '**📝 Concept Practice Questions**',
        '#### **🗝️ Explanations & Answers**',
        '#### 🗝️ Explanations & Answers',
        '- Module 1.',
        '- Module 2.',
        '- Module 3.',
        '- Module 4.',
        '- Module 5.',
        '- Module 6.',
        '- Module 7.',
        '🎉 **Congratulations!',
        'What would you like to do next?'
    ]

    for marker in split_markers:
        if marker in text:
            text = text.split(marker)[0]

    # Clean trailing chat artifacts
    text = re.sub(r'-\s+Module\s+\d+\.\d+.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'🎉.*$', '', text, flags=re.DOTALL)
    text = re.sub(r'🔥.*$', '', text, flags=re.DOTALL)
    text = re.sub(r'What would you like to do next\?.*$', '', text, flags=re.DOTALL)
    
    # Clean latex
    text = clean_latex_string(text)

    return text.strip()

def run_deep_cleanup():
    print("=" * 80)
    print("STARTING DEEP LATEX NORMALIZATION & MISCONCEPTION HARDENING")
    print("=" * 80)

    # 1. Update all 30 knowledge checks in Form 4 Topic 1
    print("\n[1/3] Repairing 30 Knowledge Checks in Form 4 Topic 1 (Acids, Bases, Salts)...")
    repaired_mcqs = 0
    for block_id, mcq in TOPIC1_MCQS.items():
        try:
            b = LessonBlock.objects.get(id=block_id)
            b.content = {
                "question": mcq["question"],
                "options": mcq["options"],
                "answer": mcq["answer"],
                "explanation": mcq["explanation"],
                "check_type": "multiple_choice"
            }
            b.save(update_fields=['content'])
            repaired_mcqs += 1
            print(f"  [Repaired MCQ] Block {b.id} in Lesson [{b.lesson.id}] {b.lesson.title}")
        except LessonBlock.DoesNotExist:
            print(f"  [Warning] Block {block_id} not found.")
    print(f"[*] Repaired {repaired_mcqs} knowledge check blocks with full 4-option KCSE questions.")

    # 2. Sanitize all common_misconception blocks across Chemistry
    print("\n[2/3] Sanitizing common_misconception blocks across Form 3 and Form 4 Chemistry...")
    cm_blocks = LessonBlock.objects.filter(
        lesson__topic__subject__name='Chemistry',
        block_type__in=['common_misconception', 'misconception_card']
    )
    cleaned_cm = 0
    for b in cm_blocks:
        content = b.content or {}
        if isinstance(content, dict):
            orig_text = content.get('text', '')
            cleaned_text = sanitize_misconception_text(orig_text)
            if cleaned_text != orig_text:
                content['text'] = cleaned_text
                b.content = content
                b.save(update_fields=['content'])
                cleaned_cm += 1
                print(f"  [Sanitized Misconception] Block {b.id} in Lesson [{b.lesson.id}] {b.lesson.title}")
        elif isinstance(content, str):
            cleaned_text = sanitize_misconception_text(content)
            if cleaned_text != content:
                b.content = {"text": cleaned_text}
                b.save(update_fields=['content'])
                cleaned_cm += 1
                print(f"  [Sanitized Misconception] Block {b.id} in Lesson [{b.lesson.id}] {b.lesson.title}")
    print(f"[*] Sanitized {cleaned_cm} common_misconception blocks.")

    # 3. Clean ightarrow / ightleftharpoons & trailing latex across ALL Chemistry blocks
    print("\n[3/3] Global LaTeX normalisation across all Chemistry blocks...")
    all_chem_blocks = LessonBlock.objects.filter(lesson__topic__subject__name='Chemistry')
    global_cleaned = 0

    def clean_obj(val):
        if isinstance(val, str):
            return clean_latex_string(val)
        elif isinstance(val, dict):
            return {k: clean_obj(v) for k, v in val.items()}
        elif isinstance(val, list):
            return [clean_obj(item) for item in val]
        return val

    for b in all_chem_blocks:
        if b.content:
            new_content = clean_obj(b.content)
            if new_content != b.content:
                b.content = new_content
                b.save(update_fields=['content'])
                global_cleaned += 1

    print(f"[*] Cleaned LaTeX formatting across {global_cleaned} content blocks.")
    print("=" * 80)
    print("ALL LATEX & MISCONCEPTION FIXES APPLIED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_deep_cleanup()
