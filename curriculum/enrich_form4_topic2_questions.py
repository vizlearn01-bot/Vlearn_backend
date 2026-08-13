import os
import sys
import django

sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock

def enrich_form4_topic2():
    topic = Topic.objects.get(id=13) # Form 4 Chemistry Topic 2: Energy Changes in Chemical and Physical Processes
    print(f"=== Enriching Form 4 Topic 2: {topic.name} ===")

    # Define high quality, interactive Knowledge Check questions for each lesson in Topic 2
    lesson_questions = {
        16: {
            "title": "Check Your Understanding: Bond Energy & Energetics",
            "question": "During a chemical reaction, bonds in the reactant molecules are broken and new bonds are formed in the product molecules. Which statement correctly describes the energetic changes taking place?",
            "check_type": "multiple_choice",
            "options": [
                "Bond breaking is always endothermic (absorbs energy, $\\Delta H > 0$), while bond formation is always exothermic (releases energy, $\\Delta H < 0$).",
                "Bond breaking is always exothermic (releases energy), while bond formation is always endothermic (absorbs energy).",
                "Both bond breaking and bond formation absorb energy from the surroundings.",
                "Both bond breaking and bond formation release energy to the surroundings."
            ],
            "answer": "A",
            "explanation": "Energy must be supplied to overcome the electrostatic attractions between atoms (bond breaking is endothermic, $\\Delta H > 0$). When new bonds form, atoms reach a more stable, lower energy state, releasing energy to the surroundings (bond formation is exothermic, $\\Delta H < 0$)."
        },
        38: {
            "title": "Check Your Understanding: Exothermic & Endothermic Reactions",
            "question": "A student dissolves a spatula of solid ammonium nitrate ($\\text{NH}_4\\text{NO}_3$) in a beaker of water at room temperature ($22^\\circ\\text{C}$). The temperature of the mixture drops to $15^\\circ\\text{C}$. Which statement accurately classifies this process?",
            "check_type": "multiple_choice",
            "options": [
                "It is an endothermic process with a positive enthalpy change ($\\Delta H > 0$), because thermal energy is absorbed from the water.",
                "It is an exothermic process with a negative enthalpy change ($\\Delta H < 0$), because the system lost heat.",
                "It is an exothermic process because bonds were broken in the crystal lattice.",
                "It is a neutral physical process with zero net enthalpy change ($\\Delta H = 0$)."
            ],
            "answer": "A",
            "explanation": "A drop in thermometer temperature means the dissolving solute is absorbing heat energy from the water/surroundings. An energy-absorbing process is endothermic, meaning the enthalpy of products is greater than reactants ($\\Delta H > 0$)."
        },
        39: {
            "title": "Check Your Understanding: Thermochemical Equations & Enthalpy Notation",
            "question": "Consider the thermochemical equation:\n$$\\text{CH}_{4(g)} + 2\\text{O}_{2(g)} \\rightarrow \\text{CO}_{2(g)} + 2\\text{H}_2\\text{O}_{(l)} \\quad \\Delta H = -890\\text{ kJ mol}^{-1}$$\nWhat does the negative sign of $\\Delta H$ signify?",
            "check_type": "multiple_choice",
            "options": [
                "The reaction is exothermic; $890\\text{ kJ}$ of heat energy is released per mole of methane burned.",
                "The reaction is endothermic; $890\\text{ kJ}$ of heat energy must be continuously supplied to burn one mole of methane.",
                "The reaction has negative activation energy and occurs spontaneously at absolute zero.",
                "The mass of the products is $890\\text{ g}$ less than the mass of the reactants."
            ],
            "answer": "A",
            "explanation": "In thermodynamic notation, a negative sign for enthalpy change ($\\Delta H < 0$) indicates an exothermic reaction where the enthalpy of products is lower than reactants, releasing thermal energy to the surroundings."
        },
        40: {
            "title": "Check Your Understanding: Calorimetric Determination of Enthalpy",
            "question": "When $50.0\\text{ cm}^3$ of $1.0\\text{ M HCl}$ is mixed with $50.0\\text{ cm}^3$ of $1.0\\text{ M NaOH}$ in a plastic cup calorimeter, the temperature rises by $6.5^\\circ\\text{C}$. Why are expanded polystyrene or plastic cups preferred over metal beakers for this experiment?",
            "check_type": "multiple_choice",
            "options": [
                "Plastic cups have very low thermal conductivity and low heat capacity, minimizing heat loss to the surroundings.",
                "Plastic cups react chemically with the acid to accelerate the neutralization reaction.",
                "Metal beakers absorb all heat and prevent the thermometer from detecting any temperature change.",
                "Plastic cups increase the activation energy of the acid-base neutralization."
            ],
            "answer": "A",
            "explanation": "Calorimetry assumes no heat is exchanged with the environment. Plastic cups act as thermal insulators with negligible heat capacity, ensuring almost all released heat is transferred directly into the aqueous solution."
        },
        41: {
            "title": "Check Your Understanding: Standard Thermodynamic Reference Conditions",
            "question": "Standard enthalpy changes ($\\Delta H^\\circ$) are measured under globally agreed reference conditions. What are the standard temperature, pressure, and solution concentration values?",
            "check_type": "multiple_choice",
            "options": [
                "Temperature: $25^\\circ\\text{C}$ ($298\\text{ K}$), Pressure: $1\\text{ atmosphere}$ ($101.325\\text{ kPa}$), Concentration: $1.0\\text{ mol dm}^{-3}$.",
                "Temperature: $0^\\circ\\text{C}$ ($273\\text{ K}$), Pressure: $1\\text{ atmosphere}$ ($101.325\\text{ kPa}$), Concentration: $0.1\\text{ mol dm}^{-3}$.",
                "Temperature: $100^\\circ\\text{C}$ ($373\\text{ K}$), Pressure: $2\\text{ atmospheres}$ ($202.65\\text{ kPa}$), Concentration: $1.0\\text{ mol dm}^{-3}$.",
                "Temperature: $20^\\circ\\text{C}$ ($293\\text{ K}$), Pressure: $0.5\\text{ atmosphere}$, Concentration: $0.5\\text{ mol dm}^{-3}$."
            ],
            "answer": "A",
            "explanation": "Standard thermodynamic state conditions are defined as a temperature of $25^\\circ\\text{C}$ ($298.15\\text{ K}$), standard atmospheric pressure of $1\\text{ atm}$ ($101.325\\text{ kPa}$), and standard solution concentration of $1.0\\text{ mol dm}^{-3}$ ($1.0\\text{ M}$)."
        },
        42: {
            "title": "Check Your Understanding: Hess's Law of Constant Heat Summation",
            "question": "Hess’s Law states that the overall enthalpy change for converting reactants to products is identical regardless of the route taken. If Route 1 consists of direct combustion of carbon to $\\text{CO}_2$ ($\\Delta H_1 = -393.5\\text{ kJ}$), and Route 2 goes via $\\text{CO}$ with step A ($\\Delta H_A = -110.5\\text{ kJ}$) and step B ($\\Delta H_B$), what is $\\Delta H_B$?",
            "check_type": "multiple_choice",
            "options": [
                "$-283.0\\text{ kJ}$",
                "$+283.0\\text{ kJ}$",
                "$-504.0\\text{ kJ}$",
                "$+504.0\\text{ kJ}$"
            ],
            "answer": "A",
            "explanation": "By Hess's Law: $\\Delta H_1 = \\Delta H_A + \\Delta H_B \\implies -393.5 = -110.5 + \\Delta H_B \\implies \\Delta H_B = -393.5 - (-110.5) = -283.0\\text{ kJ}$."
        },
        43: {
            "title": "Check Your Understanding: Lattice Energy, Hydration & Heat of Solution",
            "question": "An ionic salt $\\text{MX}$ has a lattice energy of $+740\\text{ kJ mol}^{-1}$ and a total hydration enthalpy ($\\Delta H_{\\text{hyd}}(\\text{M}^+) + \\Delta H_{\\text{hyd}}(\\text{X}^-)$) of $-785\\text{ kJ mol}^{-1}$. What is the enthalpy of solution ($\\Delta H_{\\text{sol}}$), and will the dissolution be exothermic or endothermic?",
            "check_type": "multiple_choice",
            "options": [
                "$\\Delta H_{\\text{sol}} = -45\\text{ kJ mol}^{-1}$ (Exothermic)",
                "$\\Delta H_{\\text{sol}} = +45\\text{ kJ mol}^{-1}$ (Endothermic)",
                "$\\Delta H_{\\text{sol}} = -1525\\text{ kJ mol}^{-1}$ (Exothermic)",
                "$\\Delta H_{\\text{sol}} = +1525\\text{ kJ mol}^{-1}$ (Endothermic)"
            ],
            "answer": "A",
            "explanation": "Enthalpy of solution is calculated as $\\Delta H_{\\text{sol}} = \\Delta H_{\\text{lattice}} + \\Delta H_{\\text{hydration}} = (+740\\text{ kJ}) + (-785\\text{ kJ}) = -45\\text{ kJ mol}^{-1}$. Because $\\Delta H_{\\text{sol}} < 0$, the process is exothermic and releases heat."
        },
        44: {
            "title": "Check Your Understanding: Definition and Types of Fuels",
            "question": "Which of the following statements provides the most accurate and complete scientific definition of a fuel?",
            "check_type": "multiple_choice",
            "options": [
                "Any substance that releases useful, harnessable energy when it undergoes a chemical reaction (such as combustion) or a nuclear reaction.",
                "Any solid carbon compound that produces smoke when ignited in air.",
                "Any petroleum-derived liquid that powers motor vehicles and machinery.",
                "Any organic substance that contains hydrogen and carbon in equal proportions."
            ],
            "answer": "A",
            "explanation": "A fuel is defined scientifically as any combustible or nuclear substance that stores potential chemical or nuclear energy and converts it into useful heat or work during reactions."
        },
        45: {
            "title": "Check Your Understanding: Heating Value of Fuels",
            "question": "Ethanol ($\\text{C}_2\\text{H}_5\\text{OH}$, molar mass $= 46\\text{ g mol}^{-1}$) has a molar enthalpy of combustion of $-1368\\text{ kJ mol}^{-1}$. What is its heating value in $\\text{kJ g}^{-1}$?",
            "check_type": "multiple_choice",
            "options": [
                "$\\approx 29.74\\text{ kJ g}^{-1}$",
                "$\\approx 62.93\\text{ kJ g}^{-1}$",
                "$\\approx 13.68\\text{ kJ g}^{-1}$",
                "$\\approx 46.00\\text{ kJ g}^{-1}$"
            ],
            "answer": "A",
            "explanation": "Heating Value $= \\frac{|\\text{Molar Heat of Combustion}|}{\\text{Molar Mass}} = \\frac{1368\\text{ kJ mol}^{-1}}{46\\text{ g mol}^{-1}} \\approx 29.74\\text{ kJ g}^{-1}$."
        },
        46: {
            "title": "Check Your Understanding: Criteria for Selecting a Fuel",
            "question": "Methylhydrazine ($\\text{CH}_3\\text{NHNH}_2$) has an exceptionally high heating value and ignites instantly with oxidizers, making it ideal for rocket thrusters. Why is it completely unsuitable for domestic household cooking?",
            "check_type": "multiple_choice",
            "options": [
                "It is highly toxic, volatile, explosive, and prohibitively expensive for domestic use.",
                "Its heating value is too low to boil water under room conditions.",
                "It cannot burn in the presence of atmospheric oxygen.",
                "It produces non-combustible solid ash that clogs stove burners."
            ],
            "answer": "A",
            "explanation": "When selecting a fuel for domestic use, safety, non-toxicity, stability, and affordability are critical. While methylhydrazine is an exceptional rocket propellant, its extreme toxicity and explosive volatility make it lethal and unusable in homes."
        },
        47: {
            "title": "Check Your Understanding: Safety Precautions When Using Fuels",
            "question": "Why is burning charcoal (or using a jiko) inside a poorly ventilated, closed room extremely hazardous?",
            "check_type": "multiple_choice",
            "options": [
                "Incomplete combustion in limited oxygen produces carbon monoxide ($\\text{CO}$), a colourless, odourless, highly toxic gas that binds irreversibly to haemoglobin.",
                "Charcoal combustion produces excessive oxygen gas which causes hyperventilation.",
                "Charcoal turns into liquid carbon which dissolves concrete flooring.",
                "Charcoal absorbs all atmospheric nitrogen, causing rapid decompression."
            ],
            "answer": "A",
            "explanation": "In an enclosed space, oxygen is rapidly depleted, causing incomplete combustion of carbon to form carbon monoxide ($\\text{CO}$). $\\text{CO}$ is invisible and odourless; it binds to haemoglobin in red blood cells with $>200\\times$ the affinity of oxygen, leading to asphyxiation and death."
        },
        48: {
            "title": "Check Your Understanding: Environmental Effects of Fuel Combustion",
            "question": "Fossil fuel combustion in vehicle engines and industrial plants releases acidic pollutant gases. Which two gases are primary contributors to atmospheric acid rain?",
            "check_type": "multiple_choice",
            "options": [
                "Sulfur dioxide ($\\text{SO}_2$) and Nitrogen dioxide ($\\text{NO}_2$)",
                "Methane ($\\text{CH}_4$) and Helium ($\\text{He}$)",
                "Carbon monoxide ($\\text{CO}$) and Hydrogen gas ($\\text{H}_2$)",
                "Argon ($\\text{Ar}$) and Water vapour ($\\text{H}_2\\text{O}$)"
            ],
            "answer": "A",
            "explanation": "Sulfur impurities in fuels burn to form sulfur dioxide ($\\text{SO}_2$), and high cylinder temperatures oxidize atmospheric nitrogen to nitrogen dioxide ($\\text{NO}_2$). Both dissolve in rain droplets to form sulfuric and nitric acids (acid rain)."
        }
    }

    # Iterate over lessons and enrich blocks
    for lesson_id, q_data in lesson_questions.items():
        lesson = Lesson.objects.get(id=lesson_id)
        print(f"\nProcessing Lesson {lesson.id}: {lesson.title}")

        # Delete any dummy common_misconception header blocks with no real text
        dummy_misconceptions = LessonBlock.objects.filter(
            lesson=lesson,
            block_type='common_misconception'
        )
        for dmb in dummy_misconceptions:
            txt = str(dmb.content.get('text', '') if isinstance(dmb.content, dict) else dmb.content)
            if 'Check Your Understanding & Misconception Buster' in dmb.title and len(txt.strip()) < 80:
                print(f"  Deleting dummy misconception header block {dmb.id}: {dmb.title}")
                dmb.delete()

        # Update or create the interactive knowledge check block
        kc_blocks = LessonBlock.objects.filter(
            lesson=lesson,
            block_type='knowledge_check'
        ).order_by('order')

        if kc_blocks.exists():
            # Replace the first knowledge check with our rich interactive question
            primary_kc = kc_blocks.first()
            primary_kc.title = q_data['title']
            primary_kc.component_type = 'knowledge_check'
            primary_kc.content = {
                'title': q_data['title'],
                'question': q_data['question'],
                'check_type': q_data['check_type'],
                'options': q_data['options'],
                'answer': q_data['answer'],
                'explanation': q_data['explanation']
            }
            primary_kc.save()
            print(f"  Enriched primary KnowledgeCheck Block {primary_kc.id} -> '{primary_kc.title}'")

            # Remove any redundant dummy duplicate knowledge check blocks in the same lesson
            for extra_kc in kc_blocks[1:]:
                txt = str(extra_kc.content)
                if 'particle-level observations' in txt or 'Check Your Understanding' in extra_kc.title:
                    print(f"  Removing redundant placeholder KnowledgeCheck Block {extra_kc.id}")
                    extra_kc.delete()
        else:
            # Create a new knowledge check block
            max_order = (LessonBlock.objects.filter(lesson=lesson).order_by('-order').first().order or 0) + 1
            new_kc = LessonBlock.objects.create(
                lesson=lesson,
                order=max_order,
                page_number=max_order,
                block_type='knowledge_check',
                component_type='knowledge_check',
                title=q_data['title'],
                content={
                    'title': q_data['title'],
                    'question': q_data['question'],
                    'check_type': q_data['check_type'],
                    'options': q_data['options'],
                    'answer': q_data['answer'],
                    'explanation': q_data['explanation']
                }
            )
            print(f"  Created new KnowledgeCheck Block {new_kc.id} -> '{new_kc.title}'")

        # Now clean up broken/split practice question fragments (e.g. in lesson 46, 47, 48)
        # and normalize ordering and page numbers
        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by('order', 'id'))
        for idx, blk in enumerate(blocks, start=1):
            blk.order = idx
            # Clean authoring markers from titles if any
            if blk.title.startswith("Misconception Buster: 🧠 The Misconception Buster: "):
                blk.title = blk.title.replace("Misconception Buster: 🧠 The Misconception Buster: ", "Common Misconception: ")
            elif blk.title.startswith("Misconception Buster: "):
                blk.title = blk.title.replace("Misconception Buster: ", "Common Misconception: ")
            blk.save()

    print("\n=== Form 4 Topic 2 Ingestion & Question Enrichment Complete! ===")

if __name__ == '__main__':
    enrich_form4_topic2()
