"""
VLearn CBC Grade 7 Home Science — Topic 3: Cooking Food
Curriculum Ingestion Engine (Phase 1: Content, Pages & Blocks)

Curriculum: CBC (ID: 5)
Grade: Grade 7 (ID: 16, Level: 7)
Subject: Home Science (ID: 29)
Topic: Cooking Food (Order: 3)

Generates 4 Learning Units & 4 Published Lessons (32 Total Structured Pages, 48 Blocks):
  - Unit 1: Principles of Heat Transfer & Grilling Food (8 Pages)
  - Unit 2: Roasting & The Improvised Dual-Sufuria Sand Oven (8 Pages)
  - Unit 3: Steaming Food & Nutrient Preservation (8 Pages)
  - Unit 4: Fuel Conservation, Kitchen Safety & Creative Plating (8 Pages)

Formatting Standards Applied:
  - Standard markdown bullet lists (- ) with blank line prefixes
  - Prominent bold terms and key concepts
  - Step processes, comparison matrices, and worked examples
  - Zero bracket citations ([58], [59]) and zero prompt meta-language

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade7_home_science_topic3.py [--replace]
"""

import os
import sys
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def create_block(lesson, page_number, order, block_type, title, content):
    """Helper to create LessonBlock instances cleanly."""
    return LessonBlock.objects.create(
        lesson=lesson,
        page_number=page_number,
        order=order,
        block_type=block_type,
        title=title,
        content=content
    )

def ingest_cbc_grade7_home_science_topic3(replace=True):
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 7 HOME SCIENCE — TOPIC 3: COOKING FOOD")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade, _ = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Grade 7",
        defaults={"level": 7, "description": "Grade 7 Junior Secondary School"}
    )
    print(f"[*] Grade 7: ID {grade.id} (Level {grade.level})")

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Home Science",
        defaults={"description": "CBC Grade 7 Home Science"}
    )
    print(f"[*] Subject: {subject.name} (ID: {subject.id})")

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Cooking Food",
        defaults={
            "order": 3,
            "description": "Scientific principles of heat transfer, methods of cooking (grilling, roasting, steaming), equipment improvisation, fuel conservation, and creative food plating."
        }
    )
    if not created and replace:
        print(f"[*] Replacing existing content for Topic: '{topic.name}' (ID: {topic.id})")
        topic.lessons.all().delete()
        topic.learning_units.all().delete()
    elif created:
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # =========================================================================
    # LESSON 1: PRINCIPLES OF HEAT TRANSFER & GRILLING FOOD (8 Pages)
    # =========================================================================
    u1, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Principles of Heat Transfer & Grilling Food",
        defaults={
            "order": 1,
            "description": "Understanding why we cook food, mapping conduction, convection, and radiation, and executing safe grilling over glowing embers."
        }
    )
    l1 = Lesson.objects.create(
        topic=topic,
        learning_unit=u1,
        title="Principles of Heat Transfer & Grilling Food",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 1: '{l1.title}' (Lesson ID: {l1.id})")

    # Page 1: Hook & Introduction
    create_block(l1, 1, 1, "suggested_image", "The Fire's Secret: How Heat Travels in the Kitchen", {
        "caption": "A bubbling cooking pot over an active heat source demonstrates conduction, convection, and radiation at work.",
        "search_query": "pot cooking over open flame food"
    })
    create_block(l1, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Explain the primary reasons why we **cook food** (safety, digestion, flavor, appearance).\n- Differentiate between **conduction, convection, and radiation** in kitchen terms.\n- Classify cooking methods into **dry heat** and **moist heat** families.\n- Execute the **5-step procedure for grilling tender foods** safely over glowing embers."
    })
    create_block(l1, 1, 3, "concept_explanation", "Why We Cook Food & The 3 Heat Waves", {
        "text": "Welcome to the art and science of cooking! Raw foods like meat, cassava, or hard grains can be tough to chew, difficult to digest, and may carry harmful microbes that cause illness.\n\n- **Why We Cook**: Applying heat softens tough plant fibers, cooks animal proteins, destroys harmful bacteria, enhances rich aromas, and creates appetizing colors.\n- **Heat Transfer**: Heat energy always travels from hotter areas (burning charcoal or gas flame) to cooler areas (raw food). It moves in 3 distinct paths:\n\n- **1. Conduction**: Direct contact. Heat crawls through solid metal from the stove base directly into the pot bottom.\n- **2. Convection**: Liquid and air currents. Hot boiling soup rises, cools slightly at the top, and sinks, creating circular loops that cook evenly.\n- **3. Radiation**: Invisible heat waves. Heat radiates across space from glowing red coals directly into food without physical contact."
    })

    # Page 2: Heat Transfer Blueprint
    create_block(l1, 2, 1, "suggested_diagram", "Conduction, Convection & Radiation Heat Transfer Blueprint", {
        "caption": "Visual diagram showing conduction at the base, convection loops in the liquid, and radiation waves from the sides.",
        "diagram_type": "physics_cutaway"
    })
    create_block(l1, 2, 2, "concept_explanation", "Everyday Observations of Heat Transfer", {
        "text": "You experience all 3 forms of heat transfer daily in your home kitchen:\n\n- When you leave a metal spoon inside a hot pot of tea, the spoon handle becomes hot to touch (**Conduction**).\n- When you watch sweet potatoes boiling, the water bubbles circulate continuously (**Convection**).\n- When you sit beside a warm charcoal jiko on a cold morning, you feel warmth on your face (**Radiation**)."
    })

    # Page 3: Dry Heat vs. Moist Heat Table
    create_block(l1, 3, 1, "comparison_table", "Dry Heat Cooking vs. Moist Heat Cooking", {
        "headers": ["Cooking Family", "Heat Medium & Characteristics", "Primary Methods & Food Examples"],
        "rows": [
            ["Dry Heat Cooking", "Uses direct radiant heat waves, hot circulating oven air, or hot metal contact with NO added water. Reaches high temperatures (150°C - 250°C), caramelizing food surfaces to create crispy, brown crusts.", "Grilling (fish, maize cobs, meat skewers), Roasting (sweet potatoes, whole chickens), Baking (bread, cakes)"],
            ["Moist Heat Cooking", "Uses water, steam vapor, or culinary liquids to cook food at gentle temperatures (80°C - 100°C). Keeps foods soft, tender, and hydrated without browning.", "Steaming (kales, spinach, cassava), Boiling (beans, potatoes, rice), Stewing (meat and vegetable casseroles)"]
        ]
    })

    # Page 4: Grilling Setup & Direct Radiation
    create_block(l1, 4, 1, "suggested_diagram", "Grilling: Direct Radiant Heat over Glowing Embers", {
        "caption": "Cross-section of a wire mesh grill over red-hot charcoal showing upward radiant heat waves.",
        "diagram_type": "cross_section"
    })
    create_block(l1, 4, 2, "concept_explanation", "Principles of Grilling Over Red Embers", {
        "text": "Grilling is a fast, healthy dry-heat method where food rests on a wire grate directly above intense radiant heat:\n\n- **Suitable Foods**: Strictly for **thin, tender cuts** that cook quickly (fish fillets, thin meat strips, skewered vegetables, fresh green maize).\n- **The Glowing Ember Rule**: Always wait until charcoal turns into glowing red embers covered with a light gray ash coating. **Never grill over black smoking charcoal or active yellow flames!** Black smoke deposits bitter soot and toxic chemicals onto food."
    })

    # Page 5: Worked Example: Safe Grilling Sequence
    create_block(l1, 5, 1, "step_process", "Worked Example: The 5-Step Safe Grilling Sequence", {
        "steps": [
            {"number": 1, "title": "Clean & Oil the Wire Grate", "description": "Scrub the wire grill mesh clean and lightly rub it with cooking oil to prevent delicate food from sticking."},
            {"number": 2, "title": "Establish Steady Red Embers", "description": "Light the jiko and wait until coals glow red and flames die down into gray ash (uniform, soot-free heat)."},
            {"number": 3, "title": "Arrange Food with Space", "description": "Place thin food items flat on the grate with 1cm gaps to allow radiant heat to rise freely."},
            {"number": 4, "title": "Turn Carefully with Metal Tongs", "description": "Use long metal tongs to flip food once the underside is browned and firm. Never pierce with forks (prevents juice loss)."},
            {"number": 5, "title": "Extinguish Embers Safely", "description": "Remove cooked food to a clean warm plate, then sprinkle sand or a little water on coals outside to extinguish the fire."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l1, 6, 1, "mini_activity", "Hands-On Task: The Kitchen Heat Transfer Audit", {
        "instructions": "Observe your family cooking at home and record in your notebook:\n\n- Identify **1 example of Conduction** (e.g. pot touching burner, hot spoon handle).\n- Identify **1 example of Convection** (e.g. rising steam, boiling water loops).\n- Identify **1 example of Radiation** (e.g. glowing jiko embers, heat felt from oven side).\n- Explain why a fresh maize cob is grilled over red embers rather than boiled in a big pot."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l1, 7, 1, "key_takeaway", "Key Takeaways: Heat Transfer & Grilling", {
        "text": "Remember these essential culinary science rules:\n\n- **Conduction** is direct touch; **convection** is liquid/gas currents; **radiation** is heat waves across air.\n- **Grilling** is a dry-heat method strictly suited for **thin, tender foods**.\n- Always wait for **red embers with gray ash** before placing food on the grill mesh.\n- Use **metal tongs** to turn food to avoid piercing and losing juicy nutrients."
    })

    # Page 8: Knowledge Check
    create_block(l1, 8, 1, "knowledge_check", "Scenario Knowledge Check: Heat Transfer & Grilling", {
        "question": "A student attempts to grill a thick, 2-kilogram whole beef joint directly over an intense charcoal grill. What will happen to the meat?",
        "options": [
            "The beef joint will cook evenly to the bone in 5 minutes",
            "The outside will burn to black charred carbon while the inside remains completely raw and dangerous",
            "The meat will turn into a clear liquid soup",
            "The beef will absorb all the charcoal and become soft"
        ],
        "correct_index": 1,
        "explanation": "Correct! Grilling uses intense radiant heat that cooks fast surfaces. Thick, dense meats burn on the outside long before heat reaches the center. Grilling is strictly for thin, tender cuts."
    })

    # =========================================================================
    # LESSON 2: ROASTING & THE IMPROVISED DUAL-SUFURIA SAND OVEN (8 Pages)
    # =========================================================================
    u2, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Roasting & The Improvised Dual-Sufuria Sand Oven",
        defaults={
            "order": 2,
            "description": "Mastering oven convection roasting, constructing the dual-sufuria sand oven, and roasting thick tubers and meats."
        }
    )
    l2 = Lesson.objects.create(
        topic=topic,
        learning_unit=u2,
        title="Roasting & The Improvised Dual-Sufuria Sand Oven",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 2: '{l2.title}' (Lesson ID: {l2.id})")

    # Page 1: Hook & Introduction
    create_block(l2, 1, 1, "suggested_image", "The Sealed Oven: Circulating Hot Air Roasting", {
        "caption": "Cooking inside a closed compartment surrounds thick foods with circulating dry hot air for even roasting.",
        "search_query": "cooking with gas stove oven kitchen"
    })
    create_block(l2, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Define **roasting** and explain how circulating hot air (convection) cooks thick foods.\n- Identify suitable **dense, thick foods for roasting** (sweet potatoes, arrowroots, whole chicken).\n- Construct an **improvised dual-sufuria sand oven** using local kitchen pots and clean sand.\n- Explain the essential engineering role of **clean river sand as a heat buffer**."
    })
    create_block(l2, 1, 3, "concept_explanation", "How Roasting Works: Enclosed Convection", {
        "text": "While grilling heats food from one direction, **roasting** surrounds food with hot dry air inside a closed compartment (an oven) or rotates it over an open fire.\n\n- Inside an oven, hot air rises and cooler air falls, creating continuous **convection currents** that wrap around the food.\n- This slow, penetrating heat penetrates deep into **thick, dense foods** (like whole sweet potatoes, cassava, or chicken), breaking down tough starches into natural sugars and crisping the outer surface without burning."
    })

    # Page 2: Dual-Sufuria Sand Oven Blueprint
    create_block(l2, 2, 1, "suggested_diagram", "The Dual-Sufuria Sand Oven Engineering Blueprint", {
        "caption": "Cross-section engineering schematic of the dual-sufuria sand oven with top and bottom heat.",
        "diagram_type": "engineering_cutaway"
    })
    create_block(l2, 2, 2, "concept_explanation", "The Science of the Sand Buffer", {
        "text": "You do not need an expensive electric oven to roast delicious meals! You can engineer a highly efficient **dual-sufuria sand oven**:\n\n- **The Large Outer Sufuria**: Acts as the outer oven chamber holding the heat.\n- **The 2-Inch Clean Sand Layer**: Placed at the bottom of the outer pot. Sand absorbs intense direct heat from the jiko and distributes it evenly across the base, acting as a **thermal buffer** so the inner pot never burns.\n- **The Inner Covered Sufuria**: Holds the food safely, with its lid preventing sand dust from contaminating the meal.\n- **The Top Coals on Outer Lid**: Providing radiant heat from above, browning the top of the food while the bottom bakes."
    })

    # Page 3: Standard vs. Improvised Oven Table
    create_block(l2, 3, 1, "comparison_table", "Standard Modern Ovens vs. Improvised Dual-Sufuria Sand Ovens", {
        "headers": ["Feature", "Commercial Electric / Gas Oven", "Improvised Dual-Sufuria Sand Oven"],
        "rows": [
            ["Heat Source", "Electric heating coils or gas burners inside insulated steel walls", "Charcoal jiko from below + glowing charcoal embers placed on top of outer lid"],
            ["Heat Distribution", "Internal metal fan circulates convection air", "Hot dry air circulates naturally in the sealed cavity; sand buffers hot spots"],
            ["Cost & Accessibility", "High cost; requires electricity or piped LPG gas infrastructure", "Zero cost; constructed from standard household sufurias and clean river sand"],
            ["Culinary Result", "Even golden-brown crust and soft, baked interior", "Identical delicious roasted flavor, crispy crust, and caramelized sweet texture"]
        ]
    })

    # Page 4: Foods Suitable for Roasting
    create_block(l2, 4, 1, "concept_explanation", "Selecting Foods for Roasting", {
        "text": "Roasting is ideal for thick, solid foods that require long, gentle heat penetration:\n\n- **Root Tubers**: Whole sweet potatoes, arrowroots (nduma), and cassava.\n- **Dense Vegetables**: Whole butternut squash, large pumpkins, and whole onions.\n- **Meats & Poultry**: Whole chickens, thick beef roasts, and skewered meat cuts.\n\n*Rule*: Never roast delicate leafy greens (like spinach)—dry hot air will shrivel and scorch them in minutes!"
    })

    # Page 5: Worked Example: Constructing a Sand Oven
    create_block(l2, 5, 1, "step_process", "Worked Example: Step-by-Step Construction of the Sand Oven", {
        "steps": [
            {"number": 1, "title": "Spread Clean Dry Sand", "description": "Pour a 2-inch layer of washed, dry river sand evenly across the bottom of a large sufuria."},
            {"number": 2, "title": "Nest the Food Pot", "description": "Place your seasoned sweet potato slices inside a smaller sufuria, cover it with its lid, and nest it securely on top of the sand (ensure it does not touch outer pot walls)."},
            {"number": 3, "title": "Seal with Outer Lid & Top Coals", "description": "Cover the large sufuria with a flat tight lid. Place 4-6 glowing red charcoal embers on top of the lid."},
            {"number": 4, "title": "Roast over Moderate Jiko Fire", "description": "Place the assembled oven on a medium charcoal jiko and roast for 35-45 minutes until sweet potatoes are tender and golden."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l2, 6, 1, "mini_activity", "Hands-On Task: Designing a Sand Oven Recipe", {
        "instructions": "Plan an improvised sand oven roasting session in your notebook:\n\n- Choose a local root vegetable (e.g. sweet potatoes or arrowroots).\n- Write down the ingredients: vegetable slices, 1 teaspoon vegetable oil, a pinch of salt.\n- Sketch the dual-sufuria sand oven setup and label: outer pot, sand layer, inner pot, and top coals.\n- Explain to a classmate why the inner pot must never touch the metal walls of the outer pot."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l2, 7, 1, "key_takeaway", "Key Takeaways: Roasting & Sand Ovens", {
        "text": "Remember these oven principles:\n\n- **Roasting** surrounds food with circulating hot dry air (**convection**).\n- Best suited for **thick, dense foods** like sweet potatoes, arrowroots, and whole meats.\n- The **2-inch sand layer** spreads heat evenly and prevents the food pot from scorching.\n- **Charcoal on the top lid** ensures even browning from above."
    })

    # Page 8: Knowledge Check
    create_block(l2, 8, 1, "knowledge_check", "Scenario Knowledge Check: Roasting & Sand Oven Mechanics", {
        "question": "Why is clean river sand placed at the bottom of the large sufuria when building an improvised dual-sufuria oven?",
        "options": [
            "To absorb all the food aromas and make the room smell sweet",
            "To act as a heat buffer that distributes temperature evenly and prevents direct burning of the inner pot",
            "To add minerals and salt directly into the food",
            "To keep the pots permanently glued together"
        ],
        "correct_index": 1,
        "explanation": "Correct! The sand layer acts as a thermal buffer. It prevents intense direct metal conduction from scorching the bottom of the inner pot, ensuring gentle and uniform oven heat."
    })

    # =========================================================================
    # LESSON 3: STEAMING FOOD & NUTRIENT PRESERVATION (8 Pages)
    # =========================================================================
    u3, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Steaming Food & Nutrient Preservation",
        defaults={
            "order": 3,
            "description": "Mastering moist heat vapor cooking, nutrient conservation in local greens, improvised twig steamers, and steam shield safety."
        }
    )
    l3 = Lesson.objects.create(
        topic=topic,
        learning_unit=u3,
        title="Steaming Food & Nutrient Preservation",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 3: '{l3.title}' (Lesson ID: {l3.id})")

    # Page 1: Hook & Introduction
    create_block(l3, 1, 1, "suggested_image", "The Green Sukuma Wiki Challenge: Power of Steam!", {
        "caption": "Steaming vegetables over rising water vapor locks in bright natural green colors, fresh crispness, and vital vitamins.",
        "search_query": "fresh vegetable preparation greens"
    })
    create_block(l3, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Define **steaming** and explain how rising water vapor cooks food without water contact.\n- Explain why steaming **conserves water-soluble vitamins (B and C)** compared to boiling.\n- Construct an **improvised steamer** using clean crossed twigs or perforated metal cans.\n- Practice the **'Steam Shield' safety technique** when opening hot steamer lids."
    })
    create_block(l3, 1, 3, "concept_explanation", "The Nutritional Power of Steaming", {
        "text": "When you boil kales (sukuma wiki) or spinach in a pot full of water, the cooking water turns deep green while the leaves become dull and limp. That green water contains all the dissolved **Vitamin C, Vitamin B, and minerals** that get thrown down the drain!\n\n- **Steaming** is a moist-heat method where food rests on a perforated platform above boiling water. The food is cooked exclusively by hot **rising water vapor (steam)**.\n- Because the food never touches the liquid water, vital nutrients, natural flavors, and vibrant green chlorophyll pigments remain 100% trapped inside the food!"
    })

    # Page 2: Boiling vs. Steaming Blueprint
    create_block(l3, 2, 1, "suggested_diagram", "Nutrient Conservation: Boiling vs. Steaming Blueprint", {
        "caption": "Comparison diagram showing nutrient leaching in boiling versus nutrient retention in steaming.",
        "diagram_type": "comparison_split"
    })
    create_block(l3, 2, 2, "concept_explanation", "Why Steaming is the Nutritionist's Choice", {
        "text": "Steaming offers remarkable health and practical benefits:\n\n- **100% Nutrient Retention**: Protects delicate heat-sensitive Vitamin C from washing away.\n- **Natural Flavor & Texture**: Vegetables stay crisp and sweet without becoming waterlogged or soggy.\n- **Fuel Efficiency**: Requires only 1-2 inches of water, which boils in 2 minutes, saving 50% of charcoal or gas."
    })

    # Page 3: Improvised Steamer Options
    create_block(l3, 3, 1, "comparison_table", "Methods of Setting Up an Improvised Steamer", {
        "headers": ["Steamer Design", "Materials Required", "How It Works in the Kitchen"],
        "rows": [
            ["Crossed Twig Steamer", "Clean, non-toxic wooden twigs or banana leaf midribs + standard sufuria", "Twigs are crossed at the bottom of the pot above 1 inch of water, creating a natural raised platform for sweet potatoes or greens."],
            ["Perforated Can Steamer", "Clean 500g food can with punched nail holes + standard sufuria", "Inverted perforated can sits in shallow water, supporting a heatproof bowl of food above the boiling waterline."],
            ["Metal Colander Steamer", "Stainless steel colander nested inside a larger boiling pot + tight lid", "Colander rests on the pot rim; steam rises freely through the holes while food remains completely elevated."]
        ]
    })

    # Page 4: The Steam Shield Safety Technique
    create_block(l3, 4, 1, "suggested_diagram", "The Steam Shield Safety Technique", {
        "caption": "Infographic showing how tilting a pot lid away from the face deflects dangerous steam clouds safely.",
        "diagram_type": "safety_infographic"
    })
    create_block(l3, 4, 2, "concept_explanation", "Mastering the Steam Shield", {
        "text": "Steam carries immense latent heat and can cause devastating scalds in less than one second!\n\n- **The Rule of the Shield**: When opening any steamer or covered boiling pot, **always tilt the far edge of the lid upward first**, keeping the lid between the steam cloud and your face.\n- The lid acts as a physical shield, deflecting hot steam away from your eyes, face, and chest."
    })

    # Page 5: Worked Example: Steaming Cassava on Twigs
    create_block(l3, 5, 1, "step_process", "Worked Example: Steaming Cassava on a Clean Twig Platform", {
        "steps": [
            {"number": 1, "title": "Prepare Clean Twigs", "description": "Select 6-8 clean, non-toxic twigs (e.g. mango or banana leaf ribs), wash them thoroughly, and criss-cross them in the pot bottom."},
            {"number": 2, "title": "Add Shallow Water", "description": "Pour 1 inch of clean water into the pot (ensure water level remains 1cm below the top of the twig platform)."},
            {"number": 3, "title": "Arrange Cassava Pieces", "description": "Place peeled, washed cassava chunks on top of the twig platform without crowding."},
            {"number": 4, "title": "Cover with Weighted Lid", "description": "Cover tightly with a heavy lid and steam over medium jiko heat for 20-25 minutes until cassava is soft and fork-tender."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l3, 6, 1, "mini_activity", "Hands-On Task: Building a Twig Steamer Platform", {
        "instructions": "Practice setting up an improvised steamer platform at home or school:\n\n- Collect 6 clean, sturdy wooden twigs (or bamboo sticks).\n- Cut them to match the diameter of your cooking pot.\n- Arrange them in a criss-cross grid inside the pot base.\n- Pour water up to 1 inch depth and verify that the top of your twig rack remains completely dry above the water!"
    })

    # Page 7: Key Takeaways & Recall
    create_block(l3, 7, 1, "key_takeaway", "Key Takeaways: Steaming & Nutrient Protection", {
        "text": "Remember these steaming essentials:\n\n- **Steaming** cooks with rising water vapor without food touching boiling water.\n- Keeps **vegetables bright green** and locks in **Vitamins B and C**.\n- Only requires **1-2 inches of water**, saving household fuel.\n- Always use the **'Steam Shield'**: tilt the lid away from your face when opening."
    })

    # Page 8: Knowledge Check
    create_block(l3, 8, 1, "knowledge_check", "Scenario Knowledge Check: Steaming & Nutrient Protection", {
        "question": "Why does steaming sukuma wiki (kales) on a twig rack preserve more Vitamin C than boiling them in a pot full of water?",
        "options": [
            "Steaming adds artificial vitamins through the smoke",
            "Vitamin C is water-soluble; in steaming, the kales never touch water so the vitamins cannot dissolve and wash away",
            "Steaming removes all green pigments from the kales",
            "Steaming freezes the vegetables instantly"
        ],
        "correct_index": 1,
        "explanation": "Correct! Vitamin C dissolves easily in water. When vegetables are boiled, vitamins leach into the water and are discarded. In steaming, rising vapor cooks the food while keeping all nutrients inside."
    })

    # =========================================================================
    # LESSON 4: FUEL CONSERVATION, KITCHEN SAFETY & CREATIVE PLATING (8 Pages)
    # =========================================================================
    u4, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Fuel Conservation, Kitchen Safety & Creative Plating",
        defaults={
            "order": 4,
            "description": "Practicing energy conservation, managing cooking fuels responsibly, and presenting meals creatively using local edible garnishes."
        }
    )
    l4 = Lesson.objects.create(
        topic=topic,
        learning_unit=u4,
        title="Fuel Conservation, Kitchen Safety & Creative Plating",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 4: '{l4.title}' (Lesson ID: {l4.id})")

    # Page 1: Hook & Introduction
    create_block(l4, 1, 1, "suggested_image", "Cooking with Integrity: Saving Fuel & Safe Practices", {
        "caption": "Conserving cooking fuels and presenting meals with pride demonstrates responsible home management and cultural appreciation.",
        "search_query": "african village domestic cooking community"
    })
    create_block(l4, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Compare common **household cooking fuels** (charcoal, firewood, gas, electricity, solar).\n- Apply **energy-saving techniques** (tight lids, jiko draft-door control, multi-tier cooking).\n- Safely **extinguish hot charcoal embers** to prevent fires and conserve fuel.\n- Present cooked dishes attractively using **clean margins, portioning, and edible local garnishes**."
    })
    create_block(l4, 1, 3, "concept_explanation", "Cooking with Integrity and Resourcefulness", {
        "text": "Energy is not free! Every time we cook, we consume resources that impact our family budget and the natural environment. Cooking with integrity means using energy wisely and presenting food with care.\n\n- Conserving fuel saves money and protects forests from excessive wood harvesting.\n- Attractively presented food stimulates appetite, shows respect for diners, and celebrates local Kenyan culinary heritage."
    })

    # Page 2: Jiko Draft-Door Simulator Blueprint
    create_block(l4, 2, 1, "suggested_diagram", "Jiko Draft-Door & Fuel Efficiency Simulator Blueprint", {
        "caption": "Visual diagram comparing burning rates across 100% open, 30% open simmer, and closed draft door positions.",
        "diagram_type": "efficiency_simulator"
    })
    create_block(l4, 2, 2, "concept_explanation", "The Draft-Door Principle: Managing Airflow", {
        "text": "Fire requires oxygen to burn. You can control a traditional charcoal jiko with precision:\n\n- **100% Open Draft Door**: Maximizes oxygen flow. Coals burn white-hot; ideal for quickly boiling water, but burns through charcoal in 20 minutes (**High Waste**).\n- **30% Partially Closed Door**: Restricts oxygen to a steady level. Coals glow red, maintaining a gentle simmer that cooks food thoroughly while extending charcoal lifespan to 60 minutes (**60% Fuel Saved!**).\n- **Closed Door & Extinguishing**: Cutting off oxygen puts out the fire, allowing unburnt charcoal to be saved and reused for the next meal."
    })

    # Page 3: Household Cooking Fuels Comparison
    create_block(l4, 3, 1, "comparison_table", "Comparative Guide to Common Household Cooking Fuels", {
        "headers": ["Fuel Type", "Advantages & Efficiency", "Precautions & Environmental Impact"],
        "rows": [
            ["Charcoal", "Readily available, portable, provides steady radiant heat", "Requires ventilation (produces deadly carbon monoxide gas); contributes to tree cutting"],
            ["LPG Gas (Cylinder)", "Instant ignition, clean smokeless flame, highly controllable heat", "Higher initial cost; requires regular rubber hose checks for gas leaks"],
            ["Firewood", "Low cost in rural areas; burns hot for large communal pots", "Produces heavy smoke (causes respiratory issues); requires careful ember extinguishing"],
            ["Solar Cookers", "100% free renewable solar energy; zero smoke or air pollution", "Only works on bright sunny days; requires longer cooking time"]
        ]
    })

    # Page 4: Creative Food Presentation & Garnishing
    create_block(l4, 4, 1, "suggested_diagram", "The Art of Creative Food Presentation & Local Garnishing", {
        "caption": "Split-screen comparison showing an unappealing messy plate versus a professionally presented, garnished dish.",
        "diagram_type": "aesthetic_comparison"
    })
    create_block(l4, 4, 2, "concept_explanation", "Principles of Beautiful Meal Presentation", {
        "text": "We eat with our eyes before our mouth! Follow these 3 golden rules to make any simple home dish look delicious:\n\n- **1. Spotless Clean Margins**: Always wipe the rim and edges of the serving plate with a clean cloth before presenting. Food smudges look unhygienic.\n- **2. Color Contrast & Portioning**: Pair golden sweet potatoes with bright green steamed kales. Never overcrowd the plate in a messy heap.\n- **3. 100% Edible Local Garnishes**: Decorate with fresh coriander (dhania) sprigs, thin tomato rosettes, lemon wheels, or raw carrot curls. **Never use plastic decorations or non-edible plants!**"
    })

    # Page 5: Worked Example: Plating Steamed Cassava & Greens
    create_block(l4, 5, 1, "step_process", "Worked Example: Plating a Traditional Steamed Meal", {
        "steps": [
            {"number": 1, "title": "Select a Clean, Dry Plate", "description": "Choose a clean, plain ceramic or wooden plate that provides good visual contrast."},
            {"number": 2, "title": "Portion the Steamed Cassava", "description": "Arrange 3-4 neat, fork-tender cassava wedges in a gentle circular fan pattern on one side of the plate."},
            {"number": 3, "title": "Add Vibrant Green Vegetables", "description": "Place a neat, compact mound of freshly steamed bright green sukuma wiki alongside the cassava."},
            {"number": 4, "title": "Apply Edible Garnish & Wipe Rims", "description": "Place a sprig of fresh green coriander and a twisted lemon wheel on the center, then wipe the plate rim spotless."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l4, 6, 1, "mini_activity", "Hands-On Task: Crafting an Edible Tomato Rosette Garnish", {
        "instructions": "Practice knife control and plating aesthetics at home with an adult:\n\n- Take a firm ripe tomato and a small, sharp paring knife.\n- Carefully peel the tomato skin in one continuous thin ribbon from top to bottom (like peeling an apple).\n- Roll the tomato skin ribbon tightly around itself, then let it stand upright on a cutting board—it will blossom into a beautiful red tomato rose!\n- Place your tomato rose on a plate of food, add a green leaf of dhania, and take a photo for your class portfolio."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l4, 7, 1, "key_takeaway", "Key Takeaways: Fuel Efficiency & Plating", {
        "text": "Remember these culinary management rules:\n\n- Slide jiko draft doors **partially closed (30%)** to simmer food and save up to 60% fuel.\n- Always **extinguish hot coals outside** with sand or a little water to save fuel for next time.\n- Ensure all garnishes are **100% fresh, clean, and edible** (dhania, lemon, tomato).\n- Always **wipe plate margins spotless** before serving."
    })

    # Page 8: Knowledge Check
    create_block(l4, 8, 1, "knowledge_check", "Scenario Knowledge Check: Fuel Conservation & Creative Plating", {
        "question": "What is the primary safety and hygiene rule to follow when decorating a plate of grilled fish and steamed cassava for your family?",
        "options": [
            "Use brightly colored plastic artificial flowers to make it look fancy",
            "All garnishes must be 100% edible, clean, fresh, and made from safe local ingredients (like dhania, lemon, or tomato)",
            "Cover the entire plate with non-edible tree leaves to hide the food",
            "Never wipe the plate edges because sauce smudges show the food is hot"
        ],
        "correct_index": 1,
        "explanation": "Correct! Garnishes must always be 100% edible, hygienic, and non-toxic. Plastic decorations or non-edible plants pose severe choking and chemical contamination risks."
    })

    total_lessons = topic.lessons.count()
    total_pages = sum(len(set(l.blocks.values_list("page_number", flat=True))) for l in topic.lessons.all())
    total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 3 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CBC Grade 7 Home Science Topic 3: Cooking Food")
    parser.add_argument("--replace", action="store_true", default=True, help="Replace existing topic content")
    args = parser.parse_args()
    ingest_cbc_grade7_home_science_topic3(replace=args.replace)
