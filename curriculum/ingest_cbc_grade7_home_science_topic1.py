"""
VLearn CBC Grade 7 Home Science — Topic 1: Kitchen Safety
Curriculum Ingestion Engine (Phase 1: Content, Pages & Blocks)

Curriculum: CBC (ID: 5)
Grade: Grade 7 (ID: 16, Level: 7)
Subject: Home Science (ID: 29)
Topic: Kitchen Safety (Order: 1)

Generates 3 Learning Units & 3 Published Lessons (24 Total Structured Pages, 45 Blocks):
  - Unit 1: Kitchen Hazards & Causes of Accidents (8 Pages)
  - Unit 2: Accident Prevention & Safe Work Habits (8 Pages)
  - Unit 3: Emergency First Aid & Kitchen Protective Apparel (8 Pages)

Formatting Standards Applied:
  - Standard markdown bullet lists (- ) with blank line prefixes
  - Prominent bold terms and key concepts
  - Step processes, comparison matrices, and worked examples
  - Zero bracket citations ([232], [234]) and zero prompt meta-language

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade7_home_science_topic1.py [--replace]
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

def ingest_cbc_grade7_home_science_topic1(replace=True):
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 7 HOME SCIENCE — TOPIC 1: KITCHEN SAFETY")
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
        name="Kitchen Safety",
        defaults={
            "order": 1,
            "description": "Foundational kitchen safety practices, hazard recognition, accident prevention, emergency first-aid responses, and protective apparel."
        }
    )
    if not created and replace:
        print(f"[*] Replacing existing content for Topic: '{topic.name}' (ID: {topic.id})")
        topic.lessons.all().delete()
        topic.learning_units.all().delete()
    elif created:
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # =========================================================================
    # LESSON 1: KITCHEN HAZARDS & CAUSES OF ACCIDENTS (8 Pages, 15 Blocks)
    # =========================================================================
    u1, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Kitchen Hazards & Causes of Accidents",
        defaults={
            "order": 1,
            "description": "Understanding kitchen hazards versus accidents, identifying latent danger zones, and analyzing the causes of falls, cuts, burns, scalds, and electric shocks."
        }
    )
    l1 = Lesson.objects.create(
        topic=topic,
        learning_unit=u1,
        title="Kitchen Hazards & Causes of Accidents",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 1: '{l1.title}' (Lesson ID: {l1.id})")

    # Page 1: Hook & Introduction
    create_block(l1, 1, 1, "suggested_image", "Welcome to the Kitchen: Spot the Hidden Dangers!", {
        "caption": "A bustling domestic kitchen environment where daily food preparation requires vigilance to avoid hidden hazards.",
        "search_query": "historic kitchen interior home cooking"
    })
    create_block(l1, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Define what a **kitchen hazard** is and distinguish it from an **accident**.\n- Identify the **5 common silent hazard zones** in home and school kitchens.\n- Differentiate scientifically between **dry heat burns** and **moist heat scalds**.\n- Explain the root causes of common kitchen **falls, cuts, and electric shocks**."
    })
    create_block(l1, 1, 3, "concept_explanation", "Hazards vs. Accidents: Developing Safety Eyes", {
        "text": "Welcome to **Grade 7 Home Science**! The kitchen is a wonderful space where delicious meals are created, but it also contains hidden dangers.\n\n- A **hazard** is any object, substance, or situation that has the potential to cause harm, injury, or damage (such as a puddle of cooking oil on the floor or a sharp knife balancing on the edge of a table).\n- An **accident** is the sudden, unplanned, and harmful event that occurs when a hazard is ignored (such as slipping on the oil puddle and breaking an arm).\n\n**Key Rule**: Hazards are the *causes*, while accidents are the painful *results*. If we learn to spot hazards early, we can eliminate accidents before they happen!"
    })

    # Page 2: The 5 Common Kitchen Hazards Blueprint
    create_block(l1, 2, 1, "suggested_diagram", "The 5 Common Kitchen Hazards Blueprint", {
        "caption": "Spatial overview of the 5 silent hazard zones in a home kitchen.",
        "diagram_type": "spatial_blueprint"
    })
    create_block(l1, 2, 2, "concept_explanation", "Diagnosing Silent Danger Zones", {
        "text": "A hazard does not have to be noisy or glowing red to be dangerous. In home and school kitchens, hazards often blend into normal surroundings:\n\n- **Slippery Floor Puddles**: Water splashing from wash basins or spilled cooking oil makes smooth tiles or polished cement dangerously slick.\n- **Exposed Knife Blades**: Placing a chef's knife near the counter edge or hiding it under a wet dishcloth leads to severe cuts when reaching blindly.\n- **Curtains Near Open Flames**: Hanging lightweight window curtains or kitchen cloths close to a gas burner or paraffin stove creates an immediate flash-fire risk.\n- **Outward-Pointing Cookware Handles**: Leaving saucepan handles sticking out into the walkway invites passersby or toddlers to accidentally knock over boiling pots.\n- **Accessible Matches & Fuel**: Storing matchboxes or kerosene bottles within reach of young children can trigger accidental poisonings or house fires."
    })

    # Page 3: Burns vs. Scalds (Dry Heat vs. Moist Heat)
    create_block(l1, 3, 1, "suggested_diagram", "Burns vs. Scalds: Dry Heat vs. Moist Heat Comparison", {
        "caption": "Visual contrast between dry heat burns from hot metal surfaces and moist heat scalds from escaping steam.",
        "diagram_type": "comparison_split"
    })
    create_block(l1, 3, 2, "comparison_table", "Comparing Burns and Scalds", {
        "headers": ["Comparison Feature", "Dry Heat Burns", "Moist Heat Scalds"],
        "rows": [
            ["Heat Source", "Dry contact: open flames, hot metal sufuria, glowing jiko charcoal, heated oven coils", "Moist contact: boiling water, hot tea, soup splashes, pressurized steam from boiling pots"],
            ["Physical Mechanism", "Direct thermal conduction from high-temperature solids or fire directly burning skin tissue", "Rapid heat transfer from boiling liquid or condensation of hot steam releasing latent heat"],
            ["Everyday Kitchen Scenario", "Accidentally grabbing a hot metal pot handle without using a thick dry cloth", "Lifting a boiling pot lid toward your face and allowing trapped steam to rush onto your skin"],
            ["Common Severity", "Can cause skin charring, deep tissue damage, and dry blistering", "Causes rapid, wide-surface redness, extreme stinging pain, and fluid-filled blisters"]
        ]
    })

    # Page 4: Falls, Cuts, and Electric Shocks
    create_block(l1, 4, 1, "concept_explanation", "Mechanisms of Falls, Cuts, and Electric Shocks", {
        "text": "Beyond heat injuries, three other mechanical and electrical accidents frequently occur in the kitchen:\n\n- **Falls & Slips**: Caused by liquid spills, food scraps (like banana or potato peelings) on the floor, or wearing smooth plastic slippers without traction.\n- **Cuts & Lacerations**: Frequently caused by using **dull knives** (which require excessive force and easily slip), slicing toward your body instead of away, or reaching into soapy sink water containing submerged broken glasses.\n- **Electric Shocks**: Occur when touching electrical appliance switches (like blenders or electric kettles) with **wet hands**, or operating appliances with frayed, cracked power cables."
    })

    # Page 5: Worked Example: 5-Point Hazard Audit
    create_block(l1, 5, 1, "step_process", "Worked Example: Conducting a 5-Point Kitchen Hazard Audit", {
        "steps": [
            {"number": 1, "title": "Check Floor Surfaces", "description": "Scan walkways and sink zones for water splashes, cooking oil drips, and stray food peelings."},
            {"number": 2, "title": "Inspect Cookware Handles", "description": "Ensure all sufuria and saucepan handles are turned inward toward the center or back of the stove."},
            {"number": 3, "title": "Audit Knife Storage", "description": "Verify that all sharp blades are stored in wooden blocks or slots, never balancing on counter edges or hidden under towels."},
            {"number": 4, "title": "Examine Fire & Fabric Clearances", "description": "Check that window curtains, dish drying cloths, and paper towels are tied back at least 1 meter away from heat sources."},
            {"number": 5, "title": "Inspect Electrical Cables & Outlets", "description": "Ensure cords are unbroken, kept away from wet sinks, and never handled with wet fingers."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l1, 6, 1, "mini_activity", "Hands-On Task: The Home Kitchen Safety Audit", {
        "instructions": "Conduct a safety inspection in your home kitchen using your notebook:\n\n- Walk slowly through the kitchen and record any **2 latent hazards** you observe (e.g. spilled water, outward pot handles, knives on edges).\n- Safely correct the hazards with permission from an adult (e.g. wipe the puddle dry with a mop, turn the pot handle inward).\n- Write a short 3-sentence summary in your Home Science notebook explaining how your action protected your family."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l1, 7, 1, "key_takeaway", "Key Takeaways: Kitchen Hazards & Accident Causes", {
        "text": "Remember these core safety principles:\n\n- A **hazard** is a potential danger; an **accident** is the harmful result when that hazard is neglected.\n- **Burns** come from dry heat (hot pots, jiko grates); **scalds** come from moist heat (boiling water, trapped steam).\n- **Dull knives** cause more cuts than sharp ones because they slip under force.\n- **Wet hands** on electrical switches invite severe electric shocks."
    })

    # Page 8: Knowledge Check
    create_block(l1, 8, 1, "knowledge_check", "Scenario Knowledge Check: Hazards, Burns & Scalds", {
        "question": "Achieng is boiling a large pot of sweet potatoes on a charcoal jiko. When she lifts the pot lid directly toward her face, a cloud of trapped vapor rushes out and painfully injures her cheek. What type of accident did Achieng experience, and what was the heat source?",
        "options": [
            "A dry heat burn caused by radiant charcoal fire",
            "A moist heat scald caused by pressurized steam condensation",
            "A mechanical laceration caused by the pot lid edge",
            "An electric shock caused by thermal conduction"
        ],
        "correct_index": 1,
        "explanation": "Correct! Scalds are injuries caused by moist heat, including hot steam and boiling liquids. When steam contacts cooler skin, it releases intense latent heat and causes a rapid scald."
    })

    # =========================================================================
    # LESSON 2: ACCIDENT PREVENTION & SAFE WORK HABITS (8 Pages, 15 Blocks)
    # =========================================================================
    u2, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Accident Prevention & Safe Work Habits",
        defaults={
            "order": 2,
            "description": "Mastering the Clean-as-You-Go rule, safe knife handling, cookware orientation, proper spatial organization, and gas/jiko safety."
        }
    )
    l2 = Lesson.objects.create(
        topic=topic,
        learning_unit=u2,
        title="Accident Prevention & Safe Work Habits",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 2: '{l2.title}' (Lesson ID: {l2.id})")

    # Page 1: Hook & Introduction
    create_block(l2, 1, 1, "suggested_image", "Clean-As-You-Go! The Golden Rules of Prevention", {
        "caption": "Cooking with organized work habits and clean surfaces ensures food hygiene and prevents accidents.",
        "search_query": "cooking food safely with clean gas stove"
    })
    create_block(l2, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Apply the **Clean-as-You-Go** principle during food preparation.\n- Demonstrate the correct method of **holding, carrying, and washing sharp knives**.\n- Position cookware handles correctly to prevent **severe knock-over spills**.\n- Implement essential safety precautions when operating **charcoal jikos and gas cookers** in Kenyan homes."
    })
    create_block(l2, 1, 3, "concept_explanation", "The Proactive Mindset: Prevention is Better Than Cure", {
        "text": "In a busy kitchen, accidents do not happen by bad luck—they happen when safety routines are skipped! Practicing proactive kitchen habits ensures that cooking remains enjoyable and injury-free.\n\n- The foundation of all kitchen safety is the **Clean-as-You-Go** rule: wipe up any liquid spill immediately, return tools to their storage spaces after use, and clear food peelings off the cutting board before starting the next step."
    })

    # Page 2: The Organized Stovetop Comparison
    create_block(l2, 2, 1, "suggested_diagram", "The Organized Stovetop: Hazard Zone vs. Safe Workspace", {
        "caption": "Comparison between a cluttered, hazardous stovetop and an organized, safe cooking station.",
        "diagram_type": "comparison_split"
    })
    create_block(l2, 2, 2, "concept_explanation", "Spatial Organization on the Stove & Counter", {
        "text": "Proper stovetop arrangement prevents devastating scalds and grease fires:\n\n- **Inward Handle Rule**: Always turn saucepan and skillet handles toward the back or center of the cooking stove. Never let handles stick out into the kitchen walkway where sleeves or passing children can catch them.\n- **Clear Work Zones**: Keep paper towels, plastic spice containers, and cloth pot holders at least 1 meter away from lit burners.\n- **Controlled Movement**: Walk deliberately; never run or play in a kitchen environment."
    })

    # Page 3: The 4 Golden Rules Table
    create_block(l2, 3, 1, "comparison_table", "The 4 Golden Rules of Kitchen Accident Prevention", {
        "headers": ["Safety Domain", "Dangerous Practice (Hazard)", "Safe Professional Practice (Prevention)"],
        "rows": [
            ["Knife Handling", "Walking with blade pointing forward; cutting toward your thumb; soaking knives in soapy water sinks", "Hold knife firmly by the handle pointing straight down to the floor; cut away from fingers on a stable board; wash knives individually"],
            ["Cookware Orientation", "Saucepan handles sticking out over the edge of the stove or counter walkway", "Turn all handles inward toward the stove center or parallel to the counter edge"],
            ["Spill Management", "Leaving water or oil on the floor to 'dry naturally' while continuing to cook", "Stop cooking for 30 seconds to wipe spills completely dry immediately using a designated floor mop"],
            ["Electrical Safety", "Touching appliance plugs with wet hands; pulling cords to disconnect plugs from wall sockets", "Ensure hands are completely dry before touching switches; pull gently on the plug head, not the cable"]
        ]
    })

    # Page 4: 4 Golden Rules Graphic
    create_block(l2, 4, 1, "suggested_diagram", "The 4 Golden Rules of Kitchen Accident Prevention", {
        "caption": "Illustrated infographic summarizing the 4 primary rules for kitchen accident prevention.",
        "diagram_type": "infographic_grid"
    })

    # Page 5: Charcoal Jiko & Gas Cooker Safety in Kenya
    create_block(l2, 5, 1, "concept_explanation", "Fuel & Stove Precautions in Kenyan Households", {
        "text": "Many Kenyan homes use charcoal jikos, gas cylinders (LPG), or kerosene stoves. Each fuel requires specific precautions:\n\n- **Charcoal Jiko Safety**: Never use a burning charcoal jiko in a completely closed room with shut windows. Smoldering charcoal produces **carbon monoxide**, an invisible, odorless gas that can cause fatal suffocation. Always ensure cross-ventilation.\n- **LPG Gas Cylinder Safety**: Always check rubber regulator hoses for cracks. If you smell the strong rotten-egg scent of leaking gas, **do not strike a match or turn on any electrical light switch**! Immediately open all windows and doors and shut off the cylinder regulator valve."
    })

    # Page 6: Hands-On Activity
    create_block(l2, 6, 1, "mini_activity", "Hands-On Task: Setting Up a Safe Chopping Station", {
        "instructions": "Practice setting up a safe cutting station at school or at home:\n\n- Place a damp dishcloth or rubber mat underneath your wooden cutting board to prevent it from sliding on the counter.\n- Select a firm vegetable (like a carrot or potato).\n- Practice the **'Claw Grip'**: curl your non-cutting fingertips inward like a tiger claw to hold the vegetable, resting the flat side of the knife blade against your knuckles.\n- Cut downward and away from your body."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l2, 7, 1, "key_takeaway", "Key Takeaways: Accident Prevention", {
        "text": "Remember these essential prevention rules:\n\n- **Clean-as-You-Go**: Immediate cleanup prevents 90% of kitchen slips and cross-contamination.\n- **Turn handles inward** to protect against painful boiling splashes.\n- **Carry knives pointing down** close to your side.\n- **Never sleep or cook with a jiko in an unventilated room** due to lethal carbon monoxide risks."
    })

    # Page 8: Knowledge Check
    create_block(l2, 8, 1, "knowledge_check", "Scenario Knowledge Check: Kitchen Accident Prevention", {
        "question": "Kamau is boiling tea in a saucepan on a two-burner gas cooker. Why is it dangerous for Kamau to let the saucepan handle stick out over the front edge of the cooker?",
        "options": [
            "It slows down the boiling speed of the tea",
            "A passerby or family member walking past could knock the handle, spilling boiling tea over themselves",
            "It causes the gas burner to consume twice as much fuel",
            "It damages the non-stick coating on the saucepan bottom"
        ],
        "correct_index": 1,
        "explanation": "Correct! Outward-pointing handles are easily caught by clothing or knocked by passersby, causing devastating boiling liquid scalds. Always turn handles inward toward the stove center."
    })

    # =========================================================================
    # LESSON 3: EMERGENCY FIRST AID & KITCHEN PROTECTIVE APPAREL (8 Pages, 15 Blocks)
    # =========================================================================
    u3, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Emergency First Aid & Kitchen Protective Apparel",
        defaults={
            "order": 3,
            "description": "Administering emergency first aid for burns, scalds, cuts, and electric shocks, debunking dangerous home myths, and wearing proper safety apparel."
        }
    )
    l3 = Lesson.objects.create(
        topic=topic,
        learning_unit=u3,
        title="Emergency First Aid & Kitchen Protective Apparel",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 3: '{l3.title}' (Lesson ID: {l3.id})")

    # Page 1: Hook & Introduction
    create_block(l3, 1, 1, "suggested_image", "Cold Water is Your Best Friend! Emergency Action", {
        "caption": "A well-stocked first aid kit and clean running water are the essential first responders to kitchen emergencies.",
        "search_query": "first aid kit medical box supplies"
    })
    create_block(l3, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Define **first aid** and list essential items in a kitchen first aid kit.\n- Execute the **4 critical steps** for treating minor burns and scalds using clean cold water.\n- Debunk dangerous home myths regarding applying toothpaste, butter, or mud on burns.\n- Identify and wear the **3 essential pieces of kitchen protective apparel** (apron, cooking cap, closed flat shoes)."
    })
    create_block(l3, 1, 3, "concept_explanation", "The Mission of First Aid in the Kitchen", {
        "text": "Even with great caution, emergencies can occur. When an injury happens, acting quickly and correctly saves lives and prevents permanent scarring.\n\n- **First Aid** is the immediate, temporary assistance given to an injured person before professional medical care or hospital treatment can be obtained.\n- In kitchen burn injuries, **every second counts**: the primary objective is to stop the burning process by cooling the tissue immediately!"
    })

    # Page 2: First Aid Sequence for Burns & Scalds
    create_block(l3, 2, 1, "suggested_diagram", "The 4 Critical First-Aid Steps for Minor Burns & Scalds", {
        "caption": "Sequential flowchart of the 4 life-saving first-aid steps for minor burns and scalds.",
        "diagram_type": "sequence_flowchart"
    })
    create_block(l3, 2, 2, "step_process", "The 4-Step Protocol for Burns and Scalds", {
        "steps": [
            {"number": 1, "title": "Cool with Cold Water Immediately", "description": "Place the burned or scalded area under cool running tap water for 10 to 15 continuous minutes. This draws heat out of deep flesh layers."},
            {"number": 2, "title": "Never Pierce or Pop Blisters", "description": "Blisters are natural biological bandages that shield raw tissue from bacteria. Breaking blisters introduces severe infections."},
            {"number": 3, "title": "Cover with a Clean, Loose Bandage", "description": "Wrap the area gently with a sterile gauze bandage or a clean, lint-free cloth without applying pressure."},
            {"number": 4, "title": "Seek Adult or Medical Assistance", "description": "Inform a teacher, parent, or health worker immediately, especially if the burn covers a large area or involves the face."}
        ]
    })

    # Page 3: First Aid Science vs. Dangerous Home Myths
    create_block(l3, 3, 1, "comparison_table", "First Aid Scientific Truths vs. Dangerous Home Myths", {
        "headers": ["Home Remedy Myth", "Why It Is Dangerous (Scientific Harm)", "Correct Scientific First-Aid Action"],
        "rows": [
            ["Smearing Toothpaste on Burns", "Toothpaste contains chemicals and abrasive minerals that irritate raw skin, seal in thermal heat, and cause severe bacterial infections", "Cool exclusively with clean, running cold tap water for 10-15 minutes"],
            ["Applying Butter, Fat, or Cooking Oil", "Oils form a thick heat-trapping barrier over skin, forcing the burn to cook deeper into tissue layers", "Never use grease or fats; allow flowing cool water to carry away the heat"],
            ["Putting Fresh Mud, Cow Dung, or Ash", "Contains millions of dangerous soil bacteria (like tetanus) that cause life-threatening sepsis in open burn wounds", "Keep the wound sterile; use clean water and cover loosely with a sterile dry bandage"],
            ["Popping Fluid-Filled Blisters with a Pin", "Tears away the skin's protective barrier, exposing delicate nerve endings and creating an open pathway for germs", "Leave blisters completely intact; do not prick or scratch them"]
        ]
    })

    # Page 4: Kitchen Protective Apparel Graphic
    create_block(l3, 4, 1, "suggested_diagram", "The Cook's Safety Armor: Kitchen Protective Apparel", {
        "caption": "Labeled student model showing the 3 essential protective kitchen garments and their safety functions.",
        "diagram_type": "labeled_diagram"
    })
    create_block(l3, 4, 2, "concept_explanation", "The 3 Pieces of Kitchen Protective Wear", {
        "text": "Before starting any cooking practical, students must wear their protective uniform:\n\n- **1. Thick Cotton Apron**: Shields your chest, torso, and lap from hot boiling water splashes, spitting grease, and food stains.\n- **2. Cooking Cap / Headgear**: Keeps stray hairs from falling into food (hygiene) and prevents loose hair from catching fire when leaning over a hot burner (safety).\n- **3. Flat, Closed-Toe Non-Slip Shoes**: Protects your toes and feet if a sharp knife or heavy pot drops, and provides firm grip on wet tiles to prevent slips."
    })

    # Page 5: First Aid for Bleeding Cuts & Electric Shock
    create_block(l3, 5, 1, "step_process", "First Aid for Bleeding Cuts & Electric Emergencies", {
        "steps": [
            {"number": 1, "title": "Direct Pressure for Cuts", "description": "Press a clean cotton pad or sterile cloth directly over the bleeding wound for 3-5 minutes until bleeding stops."},
            {"number": 2, "title": "Clean Gently with Water", "description": "Rinse the cut under clean water to remove surface dirt, then apply mild antiseptic solution."},
            {"number": 3, "title": "Dress with Sterile Plaster", "description": "Cover the cut with a dry, sterile adhesive bandage to seal it from kitchen microbes."},
            {"number": 4, "title": "Electric Shock Emergency Protocol", "description": "NEVER touch an electric shock victim with bare hands! Switch off the main circuit switch immediately, or use a dry wooden broomstick to push the victim away from the power source."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l3, 6, 1, "mini_activity", "Hands-On Task: First Aid Kit Assembly & Inspection", {
        "instructions": "Inspect your school or home first aid supplies with your classmates:\n\n- Check that the kit contains: sterile gauze rolls, adhesive plasters, mild antiseptic liquid, clean cotton wool, and a pair of blunt-ended scissors.\n- Practice demonstrating the cold-water burn cooling technique using a cool tap.\n- Role-play dressing a minor finger cut with a partner using sterile technique."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l3, 7, 1, "key_takeaway", "Key Takeaways: First Aid & Safety Armor", {
        "text": "Remember these life-saving first-aid and apparel rules:\n\n- **Cold running water (10-15 mins)** is the ONLY safe remedy for minor burns and scalds.\n- **NEVER apply toothpaste, butter, or mud** to a burn wound.\n- **Never touch an electric shock victim** with bare hands—shut off power or use dry wood.\n- Always wear your **apron, cooking cap, and closed flat shoes** before lighting any fire."
    })

    # Page 8: Knowledge Check
    create_block(l3, 8, 1, "knowledge_check", "Scenario Knowledge Check: Emergency First Aid & Protective Wear", {
        "question": "While frying mandazi in the home science lab, a splash of hot oil hits Mwangi's forearm. A student suggests smearing cold butter and toothpaste on the burn to cool it. What is the correct scientific action to take?",
        "options": [
            "Apply thick butter to seal the skin, then wrap tightly in plastic foil",
            "Smear mint toothpaste over the arm to give a cool tingling sensation",
            "Immediately place the forearm under cool running tap water for 10 to 15 minutes and avoid all greasy substances",
            "Prick any blisters that form with a hot sewing needle to release fluid"
        ],
        "correct_index": 2,
        "explanation": "Correct! Cool running water for 10 to 15 minutes is the only safe first aid for heat burns. Butter and toothpaste trap the heat inside the skin and introduce severe infection risks."
    })

    total_lessons = topic.lessons.count()
    total_pages = sum(len(set(l.blocks.values_list("page_number", flat=True))) for l in topic.lessons.all())
    total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 1 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CBC Grade 7 Home Science Topic 1: Kitchen Safety")
    parser.add_argument("--replace", action="store_true", default=True, help="Replace existing topic content")
    args = parser.parse_args()
    ingest_cbc_grade7_home_science_topic1(replace=args.replace)
