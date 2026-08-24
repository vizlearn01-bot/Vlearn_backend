"""
VLearn Content Presentation Enhancement Pass
CBC Grade 6 — Home Science (Topics 1, 2, 3, 4)

Applies:
1. Structured Presentation: Transforms monotonous paragraphs into high-clarity GFM Tables, Numbered Step Sequences, and Bulleted Lists.
2. Semantic Color & Callouts: Embeds purposeful callouts (> 💡 Key Concept, > ⚠️ Safety Alert, > 🔬 Science in Action, > 💰 Money Rule, > 🧵 Mending Rule).
3. Real-World Visuals & Blueprints: Preserves all 17 live-verified photographic visual hooks (Card 1) and 34 custom responsive SVGs (Cards 2 & 4) with student-centered captions.
4. Zero Bracket Citations and Zero Meta-Language Leaks.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, LessonBlock

def run_enhancement_pass():
    print("=" * 80)
    print("STARTING VLEARN CONTENT PRESENTATION ENHANCEMENT PASS (GRADE 6 HOME SCIENCE)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()

    assert subject, "Grade 6 Home Science subject not found!"
    topics = Topic.objects.filter(subject=subject).order_by("order")

    enhanced_blocks_count = 0

    # -------------------------------------------------------------------------
    # TOPIC 1: ADOLESCENCE
    # -------------------------------------------------------------------------
    t1 = topics.filter(name="Adolescence").first()
    if t1:
        print(f"\n[+] Enhancing Topic 1: {t1.name}...")
        l1 = t1.lessons.filter(learning_unit__order=1).first()
        if l1:
            # Lesson 1 Page 2: Physical Changes Table
            b = l1.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Puberty is the period of rapid physical growth and biological maturation when a child's body transitions into that of a young adult.\n\n"
                        "### Physical Changes During Puberty\n\n"
                        "| Category | Changes in Adolescent Girls | Changes in Adolescent Boys |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Growth & Height** | Sudden rapid growth spurt; hips broaden and round | Sudden rapid growth spurt; shoulders and chest broaden |\n"
                        "| **Body & Skin** | Breasts develop; sweat & oil glands become active | Adam's apple enlarges; sweat & oil glands active |\n"
                        "| **Hair Growth** | Hair grows under armpits and in pubic region | Hair grows on face (beard/mustache), armpits, chest, and pubic area |\n"
                        "| **Voice** | Voice becomes slightly fuller and melodious | Voice breaks (deepens significantly) |\n"
                        "| **Reproductive** | Onset of menstruation (monthly period) | Production of sperm (wet dreams / nocturnal emissions) |\n\n"
                        "> 💡 **Key Concept:** Puberty changes are 100% natural and normal biological milestones. Everyone starts and progresses at their own unique pace!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 1 Page 3: Emotional & Social Changes
            b = l1.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "As your body changes physically, your brain and hormones also cause important emotional and social developments:\n\n"
                        "### 1. Emotional Changes\n\n"
                        "- **Mood Swings:** Feeling joyful one moment and irritable or anxious the next due to fluctuating hormone levels.\n"
                        "- **Self-Consciousness:** Becoming extra observant and sensitive about your appearance, height, and skin.\n"
                        "- **Desire for Independence:** Wanting to make your own decisions, take on personal responsibilities, and have privacy.\n\n"
                        "### 2. Social Changes\n\n"
                        "- **Peer Influence:** Spending more time with age-mates and valuing friendships deeply.\n"
                        "- **Identity Exploration:** Discovering your talents, values, career dreams, and personal interests.\n\n"
                        "> 🌟 **Growing Up Tip:** When feeling overwhelmed or confused, always talk to a trusted adult, parent, teacher, or school counselor for guidance."
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l2 = t1.lessons.filter(learning_unit__order=2).first()
        if l2:
            # Lesson 2 Page 2: Grooming Pillars
            b = l2.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Personal hygiene is the practice of keeping your body and clothing clean to maintain health and prevent body odor.\n\n"
                        "### The 4 Pillars of Daily Adolescent Hygiene\n\n"
                        "| Hygiene Pillar | Daily Action Protocol | Health Benefit |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Daily Bathing** | Wash entire body with clean water and soap twice daily | Removes sweat, dead skin cells, and odor-causing bacteria |\n"
                        "| **Hair Care** | Wash, oil, comb, and keep hair neatly trimmed | Prevents dandruff, lice, and scalp infections |\n"
                        "| **Oral Hygiene** | Brush teeth thoroughly after breakfast and before bed | Prevents tooth decay, cavities, and bad breath (halitosis) |\n"
                        "| **Clean Clothes** | Wash school uniform and change underwear daily | Keeps you smelling fresh, smart, and confident |\n\n"
                        "> ⚠️ **Hygiene Rule:** Never wear damp or unwashed underwear, as trapped moisture encourages fungal and skin infections."
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 2 Page 3: Menstrual Hygiene
            b = l2.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Menstruation is the normal, healthy monthly shedding of the uterine lining in adolescent girls and women.\n\n"
                        "### Menstrual Hygiene Management (MHM) Protocol\n\n"
                        "1. **Use Clean Absorbent Materials:** Use commercially packaged sanitary pads or clean, reusable cotton pads.\n"
                        "2. **Regular Changing:** Change sanitary pads every 4 to 6 hours, or sooner if heavy, to prevent leaks, discomfort, and bacterial growth.\n"
                        "3. **Gentle Cleansing:** Wash the genital area with clean warm water from front to back to avoid spreading bacteria.\n"
                        "4. **Hygienic Disposal:** Wrap used disposable pads neatly in old newspaper or wrapper and place in a sanitary bin or pit latrine. NEVER flush pads down flush toilets!\n"
                        "5. **Reusable Pad Care:** Wash reusable cotton pads thoroughly with soap and warm water, dry completely in direct sunshine, and press with a hot iron.\n\n"
                        "> 💡 **Community Fact:** Boys and girls should both understand menstruation with maturity, kindness, and respect, eliminating teasing and stigma."
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l3 = t1.lessons.filter(learning_unit__order=3).first()
        if l3:
            # Lesson 3 Page 2: 3 Food Groups
            b = l3.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "A balanced diet provides all essential nutrients in the correct proportions to fuel your rapid adolescent growth spurt:\n\n"
                        "### The 3 Essential Food Groups for Adolescents\n\n"
                        "| Food Group | Primary Nutrient | Biological Function | Local Kenyan Food Examples |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Energy-Giving** | Carbohydrates & Healthy Fats | Powers daily physical activity, sports, and brain study | Ugali, sweet potatoes, brown rice, arrowroots (nduma), cassava |\n"
                        "| **Body-Building** | Proteins | Builds new muscles, organs, blood cells, and tissues | Beans, lentils (kamande), eggs, milk, fish (omena/tilapia), lean beef |\n"
                        "| **Protective** | Vitamins & Minerals | Boosts immunity, fights diseases, and sharpens vision | Sukuma wiki, spinach, kales, carrots, ripe mangoes, oranges |\n\n"
                        "> 💧 **Hydration Fact:** Drink at least 8 glasses of clean, boiled or filtered water daily to assist digestion and clear skin!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l4 = t1.lessons.filter(learning_unit__order=4).first()
        if l4:
            # Lesson 4 Page 3: Environmental Hazards
            b = l4.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Adolescents must recognize and avoid potential physical and environmental dangers in their surroundings:\n\n"
                        "### Physical Safety & Hazard Prevention Matrix\n\n"
                        "| Environmental Hazard | High-Risk Zone | Safety Rule to Follow |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Traffic & Road Accidents** | Road crossings, busy highways | Always use designated pedestrian crossings (zebra crossings); look right, left, right before crossing |\n"
                        "| **Open Water Bodies** | Swollen rivers, quarries, dams | Never swim alone in deep rivers or unattended quarry pits; avoid flooded bridges |\n"
                        "| **Fallen Power Lines** | Wet pathways during storms | Stay at least 10 metres away from fallen electric cables and report immediately to adults |\n"
                        "| **Sharp Tools & Debris** | Farm compounds, construction sites | Wear closed shoes and handle knives, pangas, and hoes with adult supervision |\n\n"
                        "> ⚠️ **Safety Alert:** In any emergency situation, prioritize your personal safety first and call for assistance from a trusted adult or emergency services!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

    # -------------------------------------------------------------------------
    # TOPIC 2: BUDGETING
    # -------------------------------------------------------------------------
    t2 = topics.filter(name="Budgeting").first()
    if t2:
        print(f"\n[+] Enhancing Topic 2: {t2.name}...")
        l1 = t2.lessons.filter(learning_unit__order=1).first()
        if l1:
            # Lesson 1 Page 2: Needs vs Wants Table
            b = l1.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Wise financial management begins with knowing the vital difference between a need and a want:\n\n"
                        "### Needs vs. Wants Comparison\n\n"
                        "| Classification | Definition | Characteristics | School & Household Examples |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **NEEDS (Essential)** | Goods and services indispensable for human survival and basic health | Cannot be postponed without serious harm; non-negotiable | Nutritious food, clean drinking water, school uniforms, exercise books, medical care |\n"
                        "| **WANTS (Desires)** | Goods and services that bring pleasure or comfort but are not essential | Can be postponed or omitted; nice to have | Video games, candy, soda, designer sneakers, trendy sunglasses |\n\n"
                        "> 💰 **Smart Money Rule:** Always allocate your money to satisfy 100% of your essential **Needs** before spending a single shilling on non-essential **Wants**!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 1 Page 3: Balanced Budget
            b = l1.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "A budget is a written financial plan that estimates expected income and balances it against planned expenditures over a specific time period.\n\n"
                        "### The 3 Types of Household Budgets\n\n"
                        "- **Balanced Budget (Ideal):** Total Income equals Total Expenditure ($$\\text{Income} = \\text{Expenditure}$$). Every shilling has a planned job, including savings.\n"
                        "- **Surplus Budget (Healthy):** Total Income exceeds Total Expenditure ($$\\text{Income} > \\text{Expenditure}$$). Leaves extra money to boost emergency savings.\n"
                        "- **Deficit Budget (Dangerous):** Total Expenditure exceeds Total Income ($$\\text{Expenditure} > \\text{Income}$$). Forces borrowing, debts, and financial distress.\n\n"
                        "> 💡 **Key Takeaway:** A balanced budget gives you control over your money, prevents impulsive overspending, and builds emergency savings for the future!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l2 = t2.lessons.filter(learning_unit__order=2).first()
        if l2:
            # Lesson 2 Page 3: Shopping List
            b = l2.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "A shopping list is a written inventory of required items prepared in advance before visiting a market, kiosk, or supermarket.\n\n"
                        "### Shopping with a List vs. Shopping Without a List\n\n"
                        "| Comparison Factor | Shopping WITH a Written List | Shopping WITHOUT a List |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Impulse Buying** | Shielded; you stick strictly to planned items | High risk; tempted by colorful displays, sweets, and snacks |\n"
                        "| **Budget Control** | Stays within available pocket money | Easily overspends and runs out of bus fare or food money |\n"
                        "| **Time Spent** | Fast and organized market trip | Wanders aimlessly through aisles, wasting time |\n"
                        "| **Forgotten Essentials** | Zero; all needed exercise books bought | Forgets vital school items, requiring duplicate trips |\n\n"
                        "> 🛡️ **The Consumer Shield:** Never enter a shop or open-air market without a clear, prioritized shopping list in your pocket!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l3 = t2.lessons.filter(learning_unit__order=3).first()
        if l3:
            # Lesson 3 Page 2: 5 Steps to Personal Budget
            b = l3.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Follow this 5-step blueprint in your exercise book to create an unbeatable personal budget:\n\n"
                        "### The 5-Step Budgeting Blueprint\n\n"
                        "1. **Identify Total Income:** Calculate all money you expect to receive (pocket money, gifts, small chore allowances).\n"
                        "2. **List Essential Needs First:** Write down compulsory expenses (pens, geometry set, sanitary pads, transport fare) with accurate local prices.\n"
                        "3. **Set Aside Dedicated Savings:** Dedicate at least 10% to 20% of your income into savings before considering any wants.\n"
                        "4. **List Optional Wants Last:** If any money remains, allocate a modest portion to treats or leisure.\n"
                        "5. **Balance & Review:** Ensure Total Expenses + Savings do not exceed Total Income ($$\\text{Income} \\ge \\text{Expenses} + \\text{Savings}$$).\n\n"
                        "> 💰 **Golden Habit:** Pay yourself first by putting savings in a secure piggy bank or savings box before spending on daily treats!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

    # -------------------------------------------------------------------------
    # TOPIC 3: FOODS AND NUTRITION
    # -------------------------------------------------------------------------
    t3 = topics.filter(name="Foods and Nutrition").first()
    if t3:
        print(f"\n[+] Enhancing Topic 3: {t3.name}...")
        l1 = t3.lessons.filter(learning_unit__order=1).first()
        if l1:
            # Lesson 1 Page 3: 5 Deficiency Disorders Table
            b = l1.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "When the body lacks essential macronutrients or micronutrients, specific nutritional deficiency disorders occur:\n\n"
                        "### 5 Major Nutritional Deficiency Disorders Matrix\n\n"
                        "| Disorder | Missing Nutrient | Key Signs & Symptoms | Preventive Local Foods |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Anaemia** | Iron | Pale inner eyelids/gums, extreme fatigue, breathlessness, dizziness | Liver, beef, spinach, kales, beans, lentils, plus lemon juice |\n"
                        "| **Goitre** | Iodine | Painless swelling or large lump in front of neck (enlarged thyroid) | Packaged iodized table salt, lake fish (omena/tilapia), milk, eggs |\n"
                        "| **Constipation** | Dietary Fibre & Water | Hard dry stools, painful infrequent bowel movements, stomach cramps | Whole maize ugali, ripe pawpaws, kales, and 8 glasses clean water |\n"
                        "| **Kwashiorkor** | Protein | Swollen protruding belly ('potbelly'), swollen face/feet, thin brown hair | Beans, peas, green grams, eggs, milk, peanuts (groundnuts) |\n"
                        "| **Marasmus** | Total Energy / Starvation | Severe wasting, ribs visible like a xylophone, wrinkled 'old-man' face | High-energy balanced meals: ugali, porridge, potatoes, milk, beans |\n\n"
                        "> 💡 **Science in Action:** Always pair iron-rich plant foods (like spinach and beans) with Vitamin C (like fresh lemon or orange juice) to double iron absorption!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l2 = t3.lessons.filter(learning_unit__order=2).first()
        if l2:
            # Lesson 2 Page 2: 4 Meat Preservation Methods
            b = l2.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Meat is highly perishable because of its high moisture and protein content. Bacteria and fungi multiply rapidly unless preserved:\n\n"
                        "### 4 Household Meat Preservation Methods\n\n"
                        "| Preservation Method | Scientific Principle | Key Practical Advantage | Critical Caution / Limitation |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **1. Refrigeration & Freezing** | Cold temperatures slow down or suspend microbial multiplication | Preserves natural fresh meat texture, flavor, and color | Requires reliable, uninterrupted electricity supply |\n"
                        "| **2. Sun Drying** | Solar heat evaporates moisture; bacteria cannot live without water | Zero fuel cost; dried meat strips last for months | Dependent on hot, dry weather; must be protected from flies |\n"
                        "| **3. Salting & Brining** | High salt concentration draws out water through osmosis | Inexpensive, highly effective traditional cure | Excess salt increases risk of high blood pressure; soak before cooking |\n"
                        "| **4. Smoking** | Warm wood smoke dries meat and deposits antibacterial chemical films | Adds rich, distinctive savory aroma and appetizing brown color | Requires continuous fire monitoring to avoid over-cooking meat |\n\n"
                        "> ⚠️ **Health Warning:** People with hypertension (high blood pressure) should limit salted meat intake and thoroughly soak salted meat in fresh water before cooking!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 2 Page 3: Fruit & Veg Preservation
            b = l2.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Fruits and vegetables are rich in vitamins but spoil rapidly after harvest due to enzyme action and moisture.\n\n"
                        "### Hygienic Solar Sun-Drying Protocol\n\n"
                        "1. **Sort & Wash:** Select fresh, undamaged kales, cowpea leaves (kunde), or mangoes. Wash thoroughly in clean running water.\n"
                        "2. **Slice Uniformly:** Cut leaves or fruit into even, thin slices so that they dry at the same rate.\n"
                        "3. **Blanching Leaves:** Dip leafy vegetables in boiling salted water for 1 to 2 minutes, then plunge into cold water to lock color and vitamins.\n"
                        "4. **Raised Drying Racks (1 Metre High):** Spread sliced produce on clean wire mesh or reed trays raised at least 1 metre off the ground away from dust, chickens, and pets.\n"
                        "5. **Clean Muslin Cloth Cover:** Cover the drying rack with a clean, light white muslin cloth. It allows solar heat and breeze through while blocking flies, wasps, and birds.\n"
                        "6. **Airtight Storage:** Once crispy-dry, pack into clean, dry glass jars or airtight plastic containers and store in a cool, dark pantry.\n\n"
                        "> 🚫 **Golden Hygiene Rule:** NEVER dry food directly on bare ground, tarpaulins, or roadsides where dust, animal droppings, and insects cause contamination!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l3 = t3.lessons.filter(learning_unit__order=3).first()
        if l3:
            # Lesson 3 Page 2: Stove Care Table
            b = l3.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Keeping kitchen cooking equipment clean and well-maintained ensures fuel efficiency, clean air, and household safety:\n\n"
                        "### Household Stoves Care & Safety Matrix\n\n"
                        "| Cooker Type | Common Fuel | Daily Cleaning & Maintenance Protocol | Safety Danger Zone |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Charcoal Jiko** | Charcoal | Empty cold ash from the bottom grate daily to maintain oxygen airflow; wipe metal exterior | Never burn charcoal in an unventilated room (carbon monoxide poisoning risk!) |\n"
                        "| **Gas Cooker (LPG)** | Bottled Gas | Unclog burner nozzles with a needle to maintain a clean blue flame; wipe top tray clean | Check rubber hose for gas leaks using soapy water; never search with fire! |\n"
                        "| **Paraffin Stove** | Kerosene | Trim wicks flat and level to prevent smoky yellow flames; wipe chimney soot daily | Never refill kerosene while the stove is burning; wipe oil spills immediately |\n"
                        "| **Electric Cooker** | Electricity | Wipe cooled heating plates with a damp cloth; avoid scratching with steel wool | Never clean while hot; never immerse electrical plugs or switches in water |\n\n"
                        "> 🌿 **Improvised Scrubbers:** You can clean greasy sufurias using free local materials: crushed wood ash, dry maize cobs, coconut husks, and sisal fibers!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 3 Page 3: Meal Planning Factors
            b = l3.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Planning family meals in advance ensures nutritious, delicious, and budget-friendly dining every day:\n\n"
                        "### The 7 Key Meal Planning Factors\n\n"
                        "- **1. Available Household Budget:** Plan menus strictly within available family money to avoid overspending.\n"
                        "- **2. Nutritional Requirements:** Combine energy-giving, body-building, and protective foods to satisfy dietary needs.\n"
                        "- **3. Special Dietary Needs:** Cater to infants, adolescents, pregnant mothers, the elderly, or sick family members.\n"
                        "- **4. Seasonal Food Availability:** Purchase locally grown fruits and vegetables in season when they are freshest and cheapest.\n"
                        "- **5. Available Time:** Choose quick-cooking meals on busy school days and more elaborate stews on weekends.\n"
                        "- **6. Available Fuel & Cookers:** Prepare one-pot meals (like beef and potato stew) to economize on gas or charcoal.\n"
                        "- **7. Variety in Texture & Color:** Combine colorful vegetables, tender proteins, and staple grains for appetizing appeal.\n\n"
                        "> 🍽️ **Meal Planner's Rule:** A well-planned meal satisfies the stomach, nourishes the body, delights the eyes, and respects the wallet!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l4 = t3.lessons.filter(learning_unit__order=4).first()
        if l4:
            # Lesson 4 Page 2: Stewing Cookery
            b = l4.blocks.filter(page_number=2, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Stewing is a gentle, moist-heat cooking method where food is simmered slowly in a small amount of liquid inside a tightly covered pot:\n\n"
                        "### The 3 Core Scientific Principles of Stewing\n\n"
                        "1. **Convection Current Simmering:** Heat transfers through circulating liquid currents ($S$-pattern loops), cooking food evenly without needing constant stirring.\n"
                        "2. **Tenderizing Tough Fibers:** Gentle simmering over low heat slowly breaks down tough collagen in meat fibers and softens green bananas (matoke) until melt-in-the-mouth tender.\n"
                        "3. **100% Nutrient Conservation:** Water-soluble vitamins (B and C) and minerals that dissolve into the cooking liquid remain in the thick gravy and are eaten with the meal.\n\n"
                        "> 🍲 **Culinary Secret:** Traditional clay pots (*nyungu*) retain heat evenly, economize charcoal, and impart a delicious earthy flavor to stews!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 4 Page 3: Baking & Improvised Sand Oven
            b = l4.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Baking is dry-heat cooking inside an enclosed heated oven chamber:\n\n"
                        "### 1. The Rubbed-In Baking Method\n\n"
                        "- **Cool Fingertip Rubbing:** Rub cold margarine into flour using only your cool fingertips, lifting the mixture high to aerate it until it resembles fine breadcrumbs.\n"
                        "- **Batter Formation:** Stir in sugar, followed by beaten eggs and milk, to create a smooth, thick dropping consistency.\n\n"
                        "### 2. Constructing an Improvised Hot-Sand Jiko Oven\n\n"
                        "- **Bottom Heat Bed:** Place a 2 cm layer of clean river sand at the bottom of a large outer aluminium sufuria to distribute jiko heat evenly.\n"
                        "- **Baking Chamber:** Place your greased cake tin resting securely on the hot sand bed.\n"
                        "- **Top Heat Lid:** Cover the outer sufuria with a flat metal lid and place glowing red charcoal embers on top to brown the cake crust.\n\n"
                        "> 🎂 **Baker's Test:** Insert a clean wooden toothpick into the cake centre; if it comes out completely clean and dry, your cake is baked to perfection!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

    # -------------------------------------------------------------------------
    # TOPIC 4: CLOTHING AND LAUNDRY
    # -------------------------------------------------------------------------
    t4 = topics.filter(name="Clothing and Laundry").first()
    if t4:
        print(f"\n[+] Enhancing Topic 4: {t4.name}...")
        l1 = t4.lessons.filter(learning_unit__order=1).first()
        if l1:
            # Lesson 1 Page 3: 5 Sewing Tools Table
            b = l1.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "A sewing kit contains specialized tools designed for specific needlework and pressing tasks:\n\n"
                        "### The 5 Essential Home Sewing Tools\n\n"
                        "| Tool Name | Distinguishing Feature | Primary Practical Function | Key Care / Safety Rule |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Bodkin** | Flat, blunt rounded tip with large eye | Slides elastic bands, ribbons, or cords safely through fabric casings | Wipe dry after use; store in sewing tin to prevent rust |\n"
                        "| **Iron Box** | Heavy metal sole plate (electric/charcoal) | Relaxes wrinkled fibers with heat/weight; flattens sharp seams | Always rest upright on metal stand; never facedown on cloth |\n"
                        "| **Ironing Board** | Padded, heat-resistant cloth top | Provides safe, cushioned support for pressing clothes | Keep cover clean, dry, and free of scorch marks |\n"
                        "| **Spraying Can** | Fine mist nozzle or trigger pump | Mists clean water to soften stiff dry cotton/linen fibers | Empty leftover water after pressing; store dry |\n"
                        "| **Sleeve Board** | Miniature narrow tapered board | Slides inside shirt sleeves and trouser legs to iron without double creases | Hang up or fold neatly in a dry storage cupboard |\n\n"
                        "> 🪡 **Needlework Fact:** Unlike sharp sewing needles, a bodkin's blunt tip glides smoothly inside waistband channels without piercing or snagging the inner cloth!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l2 = t4.lessons.filter(learning_unit__order=2).first()
        if l2:
            # Lesson 2 Page 3: Plain vs Basket Weave Table
            b = l2.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Weaving is the process of interlacing two sets of yarns at right angles to construct fabric:\n\n"
                        "### Plain Weave (1x1) vs. Basket Weave (2x2)\n\n"
                        "| Feature | Plain Weave ($1 \\times 1$) | Basket Weave ($2 \\times 2$) |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Yarn Arrangement** | Single weft thread over single warp thread | Paired weft threads over paired warp threads |\n"
                        "| **Weaving Pathway** | Over 1 warp, Under 1 warp (alternating) | Over 2 warps, Under 2 warps (alternating pairs) |\n"
                        "| **Fabric Appearance** | Uniform, tight, flat chessboard grid | Checkered, textured pattern resembling a woven basket |\n"
                        "| **Durability & Feel** | Very firm, strong, and smooth | Thicker, flexible, and softly textured |\n"
                        "| **Common Uses** | School shirts, bedsheets, dishcloths | Heavy blankets, floor rugs, table coasters, doormats |\n\n"
                        "> 🧵 **Weaving Principle:** Warp threads form the taut vertical backbone, while weft threads swim horizontally across to build solid cloth!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l3 = t4.lessons.filter(learning_unit__order=3).first()
        if l3:
            # Lesson 3 Page 3: Knitting vs Crocheting Table
            b = l3.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Knitting and crocheting both create warm, springy loop fabrics, but use distinct tools and techniques:\n\n"
                        "### Knitting vs. Crocheting Comparison\n\n"
                        "| Feature | Hand Knitting | Crocheting |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Tools Used** | Two long pointed needles (plastic, steel, or bamboo) | Single hooked needle (crochet hook) |\n"
                        "| **Active Loops** | Dozens of open loops held across both needles | Exactly **one active loop** at a time on the hook |\n"
                        "| **Unraveling Risk** | High; dropping a needle can cause a 'ladder' run | Low; dropping the hook only leaves one secure loop |\n"
                        "| **Primary Stitches** | Knit stitch (front-to-back) and Purl stitch (back-to-front) | Single crochet (short/dense) and Double crochet (tall/airy) |\n"
                        "| **Best Articles** | Warm stretchy cardigans, socks, winter scarves | Table doilies, sturdy bags, hot-pads, baby hats |\n\n"
                        "> 💡 **Crafting Secret:** You can easily improvise smooth knitting needles and crochet hooks from local bamboo, wooden twigs, or sturdy reeds!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l4 = t4.lessons.filter(learning_unit__order=4).first()
        if l4:
            # Lesson 4 Page 3: Patch Pocket vs Pocket-in-Seam Table
            b = l4.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Pockets are essential garment pouches that hold items safely during daily school activities:\n\n"
                        "### Patch Pocket vs. Pocket-in-Seam\n\n"
                        "| Pocket Type | Structural Construction | Common Garments | Typical Damage |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Patch Pocket** | Separate fabric pouch stitched directly onto garment exterior | School shirts, blouses, coats, blazer chests | Snapped stitching at top high-strain corners |\n"
                        "| **Pocket-in-Seam** | Concealed pocket bag sewn inside structural side seams | School shorts, trousers, skirts | Ripped bottom pouch seams or separated side seam |\n\n"
                        "> 🧵 **Mending Master Rule:** When repairing a pocket, always match your sewing thread color exactly to the fabric—invisible repairs look professional and neat!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 4 Page 5: 5 Factors & Mending Steps
            b = l4.blocks.filter(page_number=5, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Follow this professional mending protocol to fix loose pocket corners neatly and permanently:\n\n"
                        "### 5 Factors Before Starting Repair\n\n"
                        "- **1. Type of Damage:** Is the stitching unraveled or is the fabric torn?\n"
                        "- **2. Size of Damage:** Measure how far the seam has separated.\n"
                        "- **3. Position of Damage:** Is the rip at a high-strain corner or along the bottom?\n"
                        "- **4. Thread Match:** Select thread matching garment color and weight exactly.\n"
                        "- **5. Choice of Stitches:** Use tight backstitches for machine-strength durability.\n\n"
                        "### Step-by-Step Patch Pocket Mending Procedure\n\n"
                        "1. **Thread Needle:** Thread needle with matching color thread and tie a secure knot at the end.\n"
                        "2. **Overlap Start:** Insert needle from underside, starting **3 to 4 stitches before** the loose section to lock intact factory threads.\n"
                        "3. **Sew Backstitches:** Sew along original seam line with neat, small backstitches (1 step forward, sew back into previous exit hole).\n"
                        "4. **Corner Anchor:** At the top edge, reinforce the corner by sewing **3 tight anchor stitches** in the exact same spot.\n"
                        "5. **Fasten & Snip:** Pull thread to garment inside, tie a double knot, and snip thread ends neatly.\n\n"
                        "> ✂️ **Grooming Benefit:** Mending your own uniform promptly keeps you looking sharp and saves your family money on tailor fees!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l5 = t4.lessons.filter(learning_unit__order=5).first()
        if l5:
            # Lesson 5 Page 3: Stain Removal Chemistry Table
            b = l5.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Tough playground stains require targeted chemical or temperature treatments before regular laundering:\n\n"
                        "### The 4-Quadrant Playground Stain Removal Guide\n\n"
                        "| Stain Type | Chemical Nature | Safe Household Reagent | Crucial Scientific Rule |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Fresh Blood** | Protein-based (haemoglobin) | **Cold Salt Water** | NEVER use hot water! Heat coagulates (bakes) blood proteins permanently into cloth |\n"
                        "| **Grass Stain** | Plant pigment (chlorophyll) | **Methylated Spirit / Lemon Juice** | Alcohol dissolves chlorophyll molecules; wash in warm soapy water to finish |\n"
                        "| **Pen Ink** | Chemical dye-based pigment | **Lemon Juice + Salt / Fresh Milk** | Citric acid lifts chemical dye pigments gently from cotton fibers |\n"
                        "| **Chewing Gum** | Sticky adhesive polymer | **Ice Cubes Freezing Method** | Rub ice until gum is rock hard and brittle; gently scrape off with blunt knife |\n\n"
                        "> ⚠️ **Safety Alert:** Always spot-treat stains promptly when fresh; older dried stains become much more stubborn and difficult to remove!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 5 Page 5: Special Laundry Treatments Table
            b = l5.blocks.filter(page_number=5, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Special laundry treatments solve specific fabric, hygiene, and brightness challenges:\n\n"
                        "### Overview of Special Laundry Treatments\n\n"
                        "| Special Treatment | Reagents / Materials Used | Primary Purpose | Safety / Application Rule |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Disinfecting** | Boiling water or antiseptic liquid (Dettol) | Destroys bacteria and fungi on sickroom bedding and underwear | Immerse in hot boiling or antiseptic rinse water |\n"
                        "| **Bleaching** | Diluted chemical bleach (sodium hypochlorite) | Whitens discolored white cottons and removes mildew | ONLY for white cottons; NEVER on coloreds or wool |\n"
                        "| **Fabric Conditioning** | Liquid fabric softener | Softens stiff fibers, reduces static, adds fresh fragrance | Add to final rinse water; do not pour directly on dry fabric |\n"
                        "| **Laundry Blue** | Minute drop of blue powder/liquid | Counteracts natural yellowing on white clothes | Dissolve thoroughly in final rinse; avoid blue streaks |\n\n"
                        "> 🧤 **Chemical Safety:** Wear rubber gloves, work in well-ventilated rooms, and NEVER mix bleach with other household cleaning chemicals!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

        l6 = t4.lessons.filter(learning_unit__order=6).first()
        if l6:
            # Lesson 6 Page 3: 7-Step Wool Care Table
            b = l6.blocks.filter(page_number=3, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Wool is a delicate animal fiber whose overlapping surface scales lock together and shrink under heat and friction:\n\n"
                        "### The 7-Step Wool-Care Laundry Protocol\n\n"
                        "1. **Mending:** Inspect and mend any loose seams or buttons before wetting the garment.\n"
                        "2. **Trace Size Map:** Lay dry sweater flat on brown paper and trace its outline with a pencil.\n"
                        "3. **Lukewarm Squeeze Wash:** Wash in lukewarm water with mild soap by gently kneading and squeezing—**NEVER scrub or wring!**\n"
                        "4. **Lukewarm Rinse:** Rinse thoroughly in clean lukewarm water until the water is completely clear.\n"
                        "5. **Towel Roll Extraction:** Place wet sweater on a dry cotton towel and roll up like a mat to press out water gently.\n"
                        "6. **Flat Shade Drying:** Lay flat in shade on your brown paper size map, easing the sweater back to match the pencil outline.\n"
                        "7. **Flat Storage:** Fold neatly and store flat in a drawer—**NEVER hang on coat hangers!**\n\n"
                        "> 🚫 **Gravity Alert:** Hanging wet sweaters on a clothesline pulls the heavy wet loops downward, permanently stretching sleeves to your knees!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

            # Lesson 6 Page 5: Loose-Coloured Garments Table
            b = l6.blocks.filter(page_number=5, block_type="rich_text").first()
            if b:
                b.content = {
                    "text": (
                        "Brightly dyed cotton garments often contain unstable dyes that bleed and transfer color into wash water:\n\n"
                        "### The 3 Laundry Sorting Basins\n\n"
                        "| Basin Setup | Garments Included | Water Treatment | Special Drying Protocol |\n"
                        "| :--- | :--- | :--- | :--- |\n"
                        "| **Basin 1: Whites** | White school shirts, white socks, sheets | Clean warm soapy water; laundry blue optional | Hang in bright sunshine for natural bleaching |\n"
                        "| **Basin 2: Colorfast** | Tested color-stable jeans, blue trousers | Normal lukewarm soapy water | Hang inside out in the shade |\n"
                        "| **Basin 3: Loose Dyes** | Bleeding red T-shirts, bright kitenge wraps | Cold water + **handful of kitchen salt** (mordant) | Dry inside out in shade; never expose to direct sun |\n\n"
                        "> 🧂 **The Salt Shield:** Kitchen salt contains sodium chloride, which acts as a mordant to chemically bind and lock loose dye molecules back into fabric fibers!"
                    )
                }
                b.save()
                enhanced_blocks_count += 1

    print(f"\n" + "=" * 80)
    print(f"[SUCCESS] Content Presentation Enhancement Pass Complete!")
    print(f"[*] Total Core Content Blocks Enhanced with Tables, Step Sequences & Callouts: {enhanced_blocks_count}")
    print("=" * 80)

if __name__ == "__main__":
    run_enhancement_pass()
