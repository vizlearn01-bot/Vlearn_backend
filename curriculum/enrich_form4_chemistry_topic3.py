"""
VLearn Form 4 Chemistry — Topic 3: Reaction Rates and Reversible Reactions
Enrichment Engine:
- Replaces all 18 placeholder / broken knowledge checks with rigorous KCSE MCQs
- Attaches verified YouTube videos to Lesson 75 (Haber Process) and Lesson 76 (Contact Process)
- Ensures all LessonAssets and LessonBlocks are synchronized
- Idempotent execution
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

MCQ_REPLACEMENTS = {
    1678: {
        "question": "Which of the following experimental procedures is most suitable for measuring the rate of reaction between marble chips (calcium carbonate) and dilute hydrochloric acid?",
        "options": [
            "Measuring the decrease in total mass of the flask and contents over time as CO2 gas escapes.",
            "Measuring the change in solution colour using a colorimeter.",
            "Measuring the change in electrical conductivity of the solution as ions remain unchanged.",
            "Measuring the volume of water produced using a measuring cylinder."
        ],
        "answer": "A",
        "explanation": "Because carbon dioxide gas escapes from the open flask during the reaction: CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + CO2(g), tracking mass loss per unit time on an electronic balance provides direct, accurate rate measurements."
    },
    1679: {
        "question": "If 40 cm³ of carbon dioxide gas is collected in 20 seconds during a reaction between zinc granules and hydrochloric acid, what is the average rate of reaction over this period?",
        "options": [
            "800 cm³/s",
            "2.0 cm³/s",
            "0.5 cm³/s",
            "20 cm³/s"
        ],
        "answer": "B",
        "explanation": "Average reaction rate = (Volume of gas produced) / (Time taken) = 40 cm³ / 20 s = 2.0 cm³/s."
    },
    1689: {
        "question": "According to collision theory, what two essential conditions must reacting particles satisfy for an effective collision to produce a chemical change?",
        "options": [
            "Particles must collide in an aqueous medium and maintain identical masses.",
            "Particles must possess kinetic energy equal to or greater than activation energy (Ea) and have correct spatial orientation.",
            "Particles must possess negative potential energy and collide in the presence of sunlight.",
            "Particles must be converted to gaseous ions prior to collision."
        ],
        "answer": "B",
        "explanation": "Only collisions where particles possess sufficient kinetic energy to overcome the activation energy (Ea) barrier and collide with appropriate geometric alignment break old bonds and form products."
    },
    1719: {
        "question": "Why does powdered calcium carbonate react much faster with dilute hydrochloric acid than an equal mass of large marble chips at the same temperature?",
        "options": [
            "Powdered calcium carbonate lowers the activation energy of the reaction.",
            "Powdered calcium carbonate has a much larger surface area, increasing collision frequency between acid particles and solid reactant.",
            "Powdered calcium carbonate increases the average kinetic energy of the acid molecules.",
            "Powdered calcium carbonate acts as a homogeneous catalyst in solution."
        ],
        "answer": "B",
        "explanation": "Subdividing a solid into fine powder greatly increases the exposed surface area per unit mass, providing more contact sites and dramatically increasing the frequency of effective collisions."
    },
    1728: {
        "question": "Increasing the pressure of a gaseous reaction mixture accelerates the rate of reaction primarily because:",
        "options": [
            "It decreases the activation energy required for bond cleavage.",
            "It compresses gas volume, increasing particle concentration and collision frequency per unit volume.",
            "It converts exothermic equilibrium states into endothermic reactions.",
            "It lowers the average temperature of the gaseous mixture."
        ],
        "answer": "B",
        "explanation": "Compressing gases into a smaller volume raises the concentration of reacting molecules (number of particles per unit volume), leading to more frequent collisions per second."
    },
    1739: {
        "question": "When blue hydrated copper(II) sulfate crystals (CuSO4·5H2O) are heated, they turn into a white anhydrous powder (CuSO4). What happens when water is added back to the cold white powder?",
        "options": [
            "The solid remains white and no temperature change occurs.",
            "The solid turns blue again and heat is evolved, demonstrating reversibility.",
            "The powder decomposes into copper metal and sulfur dioxide gas.",
            "The powder dissolves without regenerating hydrated crystals."
        ],
        "answer": "B",
        "explanation": "The hydration of anhydrous copper(II) sulfate: CuSO4(s) + 5H2O(l) <=> CuSO4·5H2O(s) is reversible. Adding water is exothermic, producing heat and restoring the characteristic blue crystalline structure."
    },
    1740: {
        "question": "Which symbol in a chemical equation indicates that a reaction is dynamic and reversible?",
        "options": [
            "-->",
            "<=> (or ⇌)",
            "==",
            "+/-"
        ],
        "answer": "B",
        "explanation": "The double half-arrow (⇌) signifies that forward and reverse reactions proceed simultaneously under the same reaction conditions."
    },
    1750: {
        "question": "A chemical system is said to have reached dynamic equilibrium in a closed vessel when:",
        "options": [
            "All reactants have been completely converted into products and reaction ceases.",
            "The rate of forward reaction equals the rate of backward reaction, and macroscopic concentrations remain constant.",
            "The concentrations of reactants and products become exactly equal.",
            "The activation energy of both forward and reverse paths drops to zero."
        ],
        "answer": "B",
        "explanation": "Dynamic equilibrium is reached when forward and reverse reactions proceed at equal rates, maintaining unchanging macroscopic properties (concentrations, color, pressure) in a closed system."
    },
    1751: {
        "question": "Why can dynamic chemical equilibrium only be established and maintained in a closed system?",
        "options": [
            "Closed systems prevent external heat transfer completely.",
            "Closed systems prevent volatile gaseous reactants or products from escaping into the surroundings.",
            "Open systems automatically destroy all catalytic activity.",
            "Closed systems force all reactions to become zero order."
        ],
        "answer": "B",
        "explanation": "If gaseous reactants or products escape into the environment, the backward reaction cannot proceed at a balanced rate, destroying the possibility of dynamic equilibrium."
    },
    1771: {
        "question": "State Le Chatelier's Principle regarding chemical systems at equilibrium:",
        "options": [
            "The rate of a chemical reaction is directly proportional to the product of reactant masses.",
            "When a system at equilibrium is subjected to an external change in concentration, temperature, or pressure, the system adjusts in a direction that opposes that change.",
            "Energy can neither be created nor destroyed in an isolated chemical system.",
            "Equal volumes of all gases at the same temperature and pressure contain equal numbers of molecules."
        ],
        "answer": "B",
        "explanation": "Le Chatelier's Principle governs dynamic equilibria: when an external constraint is applied, the equilibrium position shifts in the direction that counteracts the change."
    },
    1780: {
        "question": "Consider the chromate-dichromate equilibrium: 2CrO4²⁻(aq) [yellow] + 2H⁺(aq) <=> Cr2O7²⁻(aq) [orange] + H2O(l). What color change occurs when dilute hydrochloric acid is added to a yellow solution of potassium chromate?",
        "options": [
            "The solution turns colourless.",
            "The solution shifts from yellow to intense orange.",
            "The solution turns dark green as chromium is reduced.",
            "No colour change occurs because H⁺ is a spectator ion."
        ],
        "answer": "B",
        "explanation": "Adding HCl increases H⁺(aq) concentration. By Le Chatelier's Principle, the equilibrium shifts to the right (forward reaction) to consume excess H⁺, producing orange dichromate (Cr2O7²⁻)."
    },
    1787: {
        "question": "For the gaseous equilibrium: N2O4(g) [pale yellow, 1 mol] <=> 2NO2(g) [dark brown, 2 mol], what effect does increasing external pressure have on the color of the gas mixture?",
        "options": [
            "The gas turns darker brown because volume increases.",
            "The gas becomes lighter/paler yellow as equilibrium shifts to the left side having fewer gas molecules (1 mol vs 2 mol).",
            "The gas turns blue due to complete dissociation.",
            "The color does not change because pressure only affects reaction rate."
        ],
        "answer": "B",
        "explanation": "Increasing pressure shifts equilibrium toward the side with fewer gas molecules (1 mole of N2O4 vs 2 moles of NO2), reducing dark brown NO2 and making the mixture lighter."
    },
    1796: {
        "question": "For the exothermic equilibrium: 2SO2(g) + O2(g) <=> 2SO3(g) [ΔH = -197 kJ/mol], what happens to the yield of SO3 if the temperature is increased?",
        "options": [
            "The yield of SO3 increases because all reaction rates speed up.",
            "The yield of SO3 decreases because the equilibrium shifts in the endothermic backward direction to absorb added heat.",
            "The yield remains unaffected because catalysts dictate yield.",
            "The mixture instantly freezes into solid sulfur."
        ],
        "answer": "B",
        "explanation": "Since the forward reaction releases heat (exothermic), increasing temperature shifts the equilibrium in the endothermic reverse direction to absorb thermal energy, lowering SO3 yield."
    },
    1807: {
        "question": "What is the exact effect of adding a catalyst to a reversible reaction at equilibrium?",
        "options": [
            "It shifts the equilibrium position to the right, increasing product yield.",
            "It speeds up both forward and backward reaction rates equally, allowing equilibrium to be reached faster without changing the equilibrium yield.",
            "It converts an endothermic reaction into an exothermic reaction.",
            "It increases the activation energy of the reverse reaction only."
        ],
        "answer": "B",
        "explanation": "A catalyst lowers activation energy identically for both forward and reverse paths. It accelerates attainment of equilibrium without altering equilibrium position or final yield."
    },
    1821: {
        "question": "In the industrial synthesis of ammonia: N2(g) + 3H2(g) <=> 2NH3(g) [ΔH = -92 kJ/mol], why is a compromise temperature of 450°C chosen in modern chemical plants?",
        "options": [
            "At 450°C the equilibrium yield of ammonia is 100%.",
            "Lower temperatures give higher theoretical yield but an impractically slow reaction rate; 450°C provides an optimum balance between rate and economic yield in the presence of iron catalyst.",
            "Iron catalyst only functions above 800°C.",
            "450°C prevents nitrogen gas from liquefying."
        ],
        "answer": "B",
        "explanation": "Forward ammonia formation is exothermic (favoured by low T), but low temperatures result in sluggish reaction rates. 450°C provides an engineered balance between speed and yield."
    },
    1822: {
        "question": "Why are unreacted nitrogen and hydrogen gases recycled back into the catalyst chamber during the Haber Process?",
        "options": [
            "To prevent the catalyst from overheating.",
            "Because only 15-20% conversion occurs per pass; recycling unreacted gases increases overall plant conversion efficiency to over 95%.",
            "To neutralize acidic impurities before ammonia condensation.",
            "To decrease the operating pressure of the compressor."
        ],
        "answer": "B",
        "explanation": "Ammonia is separated by cooling and liquefaction, and unreacted N2 and H2 gases are recycled over the iron catalyst bed, boosting overall conversion to ~98%."
    },
    1832: {
        "question": "In the Contact Process, why is sulfur trioxide (SO3) absorbed in concentrated sulfuric acid (forming oleum) rather than dissolved directly in water?",
        "options": [
            "Sulfur trioxide does not react with pure water.",
            "Dissolving SO3 directly in water is violently exothermic and produces a dense, corrosive, unmanageable acid mist that is difficult to condense.",
            "Oleum is required to regenerate vanadium(V) oxide catalyst.",
            "Water causes sulfuric acid to decompose into sulfur dioxide and oxygen."
        ],
        "answer": "B",
        "explanation": "Direct absorption in water generates immense heat and forms an unmanageable acid fog. Absorbing SO3 in 98% H2SO4 forms liquid oleum (H2S2O7), which is safely diluted."
    },
    1834: {
        "question": "What catalyst and operating conditions are utilized in the catalytic converter chamber of the Contact Process for the reaction: 2SO2(g) + O2(g) <=> 2SO3(g)?",
        "options": [
            "Finely divided nickel catalyst at 200 atm pressure and 100°C.",
            "Vanadium(V) oxide (V2O5) catalyst at 450°C to 500°C and 1 to 2 atmospheres pressure.",
            "Platinum catalyst at 1000°C and 500 atmospheres.",
            "Iron catalyst with potassium oxide promoter at 450°C."
        ],
        "answer": "B",
        "explanation": "The catalytic oxidation of SO2 operates over vanadium(V) oxide (V2O5) at 450-500°C and near-atmospheric pressure (1-2 atm), achieving ~99.5% conversion."
    }
}

TOPIC3_VIDEOS = [
    {
        "lesson_id": 75,
        "title": "Video Resource: The Haber Process — Industrial Ammonia Synthesis",
        "url": "https://www.youtube.com/watch?v=NWhZ77Xi5gg",
        "youtube_id": "NWhZ77Xi5gg",
        "description": "Industrial demonstration and chemical engineering principles of the Haber Process: compromise temperature, pressure, iron catalyst, and gas recycling."
    },
    {
        "lesson_id": 76,
        "title": "Video Resource: The Contact Process — Sulfuric Acid Manufacture",
        "url": "https://www.youtube.com/watch?v=s1X3r5a133U",
        "youtube_id": "s1X3r5a133U",
        "description": "Step-by-step industrial animation of the Contact Process: sulfur burning, vanadium(V) oxide catalysis, oleum formation, and dilution."
    }
]

def enrich_topic3():
    topic = Topic.objects.get(id=14)
    print("=" * 80)
    print(f"ENRICHING TOPIC 3: {topic.name} (Subject: Form 4 Chemistry)")
    print("=" * 80)

    # 1. Update all 18 knowledge check blocks with authentic KCSE MCQs
    fixed_checks = 0
    for block_id, mcq_data in MCQ_REPLACEMENTS.items():
        try:
            b = LessonBlock.objects.get(id=block_id)
            b.content = {
                "question": mcq_data["question"],
                "options": mcq_data["options"],
                "answer": mcq_data["answer"],
                "explanation": mcq_data["explanation"],
                "check_type": "multiple_choice"
            }
            b.save(update_fields=['content'])
            fixed_checks += 1
            print(f"  [Repaired MCQ] Block {b.id} in Lesson [{b.lesson.id}] {b.lesson.title}")
        except LessonBlock.DoesNotExist:
            print(f"  [Warning] Block ID {block_id} not found.")

    print(f"[*] Repaired {fixed_checks} knowledge checks with comprehensive KCSE questions.")

    # 2. Add knowledge check to Lesson 74 if missing
    lesson_74 = Lesson.objects.get(id=74)
    if not LessonBlock.objects.filter(lesson=lesson_74, block_type="knowledge_check").exists():
        mcq_block = LessonBlock.objects.create(
            lesson=lesson_74,
            block_type="knowledge_check",
            component_type="knowledge_check",
            title="Check Your Understanding: Industrial Equilibria",
            page_number=5,
            page_title="Concept Practice",
            order=55,
            content={
                "question": "Which principle is universal to maximizing economic yields in both the Haber and Contact processes?",
                "options": [
                    "Operating at ultra-high temperatures above 1500°C to eliminate the need for catalysts.",
                    "Applying Le Chatelier's Principle to optimize temperature, pressure, and recycling while utilizing heterogeneous catalysts.",
                    "Carrying out reactions in open vats exposed to atmospheric air.",
                    "Adding water directly into catalytic chambers to absorb products."
                ],
                "answer": "B",
                "explanation": "Both the Haber and Contact processes utilize Le Chatelier's Principle to balance thermodynamics and kinetics, employing solid catalysts and recycling unreacted gases for maximum profit and safety.",
                "check_type": "multiple_choice"
            }
        )
        print(f"  [Created MCQ Block] ID {mcq_block.id} in Lesson [{lesson_74.id}] {lesson_74.title}")

    # 3. Attach verified YouTube videos
    for v in TOPIC3_VIDEOS:
        lesson = Lesson.objects.get(id=v["lesson_id"])
        existing_video_asset = LessonAsset.objects.filter(lesson=lesson, url=v["url"]).first()
        if not existing_video_asset:
            video_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="attached",
                title=v["title"],
                url=v["url"],
                description=v["description"],
                metadata={"youtube_id": v["youtube_id"]}
            )
            print(f"  [Created Video Asset] '{v['title']}' in Lesson [{lesson.id}]")
        else:
            video_asset = existing_video_asset

        video_block = LessonBlock.objects.filter(lesson=lesson, block_type="video_ref").first()
        if not video_block:
            video_block = LessonBlock.objects.create(
                lesson=lesson,
                block_type="video_ref",
                component_type="video_ref",
                title=v["title"],
                page_number=3,
                page_title="Industrial Process Video",
                order=35,
                content={
                    "url": v["url"],
                    "title": v["title"],
                    "description": v["description"]
                }
            )
            print(f"  [Created video_ref Block] ID {video_block.id} (Page 3) in Lesson [{lesson.id}]")
        else:
            video_block.content = {
                "url": v["url"],
                "title": v["title"],
                "description": v["description"]
            }
            video_block.save(update_fields=['content'])

        video_block.assets.add(video_asset)

    print("=" * 80)
    print("TOPIC 3 ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_topic3()
