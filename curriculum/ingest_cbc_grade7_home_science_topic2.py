"""
VLearn CBC Grade 7 Home Science — Topic 2: Small Kitchen Tools and Equipment
Curriculum Ingestion Engine (Phase 1: Content, Pages & Blocks)

Curriculum: CBC (ID: 5)
Grade: Grade 7 (ID: 16, Level: 7)
Subject: Home Science (ID: 29)
Topic: Small Kitchen Tools and Equipment (Order: 2)

Generates 3 Learning Units & 3 Published Lessons (24 Total Structured Pages, 36 Blocks):
  - Unit 1: Classification & Functional Families of Kitchen Tools (8 Pages)
  - Unit 2: Smart Buying, Budgeting & Tool Care Protocols (8 Pages)
  - Unit 3: Creative Improvisation & Upcycling Projects (8 Pages)

Formatting Standards Applied:
  - Standard markdown bullet lists (- ) with blank line prefixes
  - Prominent bold terms and key concepts
  - Step processes, comparison matrices, and worked examples
  - Zero bracket citations ([47], [48]) and zero prompt meta-language

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade7_home_science_topic2.py [--replace]
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

def ingest_cbc_grade7_home_science_topic2(replace=True):
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 7 HOME SCIENCE — TOPIC 2: SMALL KITCHEN TOOLS & EQUIPMENT")
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
        name="Small Kitchen Tools and Equipment",
        defaults={
            "order": 2,
            "description": "Classification of traditional and modern kitchen tools, functional categories, smart purchasing factors, care and maintenance, and sustainable tool improvisation."
        }
    )
    if not created and replace:
        print(f"[*] Replacing existing content for Topic: '{topic.name}' (ID: {topic.id})")
        topic.lessons.all().delete()
        topic.learning_units.all().delete()
    elif created:
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # =========================================================================
    # LESSON 1: CLASSIFICATION & FUNCTIONAL FAMILIES OF KITCHEN TOOLS (8 Pages)
    # =========================================================================
    u1, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Classification & Functional Families of Kitchen Tools",
        defaults={
            "order": 1,
            "description": "Classifying utensils into traditional and modern tools, mapping the 10 functional families, and practicing tool-to-task safety."
        }
    )
    l1 = Lesson.objects.create(
        topic=topic,
        learning_unit=u1,
        title="Classification & Functional Families of Kitchen Tools",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 1: '{l1.title}' (Lesson ID: {l1.id})")

    # Page 1: Hook & Introduction
    create_block(l1, 1, 1, "suggested_image", "The Magic Kitchen: Clay vs. Steel!", {
        "caption": "A collection of domestic kitchen utensils combining traditional natural cookware with modern processed tools.",
        "search_query": "kitchen utensils collection display"
    })
    create_block(l1, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Classify kitchen tools into **traditional natural utensils** and **modern processed tools**.\n- Identify the **10 primary functional families** of small kitchen tools.\n- Match the correct tool to specific cooking tasks to ensure **safety and food hygiene**.\n- Protect cookware by choosing **non-scratch turning and mixing tools**."
    })
    create_block(l1, 1, 3, "concept_explanation", "Two Worlds in One Kitchen: Traditional vs. Modern", {
        "text": "Imagine stepping into your grandmother's kitchen in the village where pots are made of brown river clay, and cooking sticks are carved from smooth mango wood. Now step into a modern restaurant kitchen filled with stainless steel pots and heat-resistant silicone spatulas!\n\n- **Traditional Utensils**: Tools made from natural local resources like clay, wood, calabash gourds, and woven reed fibers. They are eco-friendly, do not scratch metal cookware, and have been perfected over generations.\n- **Modern Small Kitchen Tools**: Tools manufactured from processed materials such as stainless steel, glass, and food-grade plastics. They are lightweight, non-porous, and engineered for high-speed cooking.\n\nBoth traditional and modern tools have unique strengths that make them valuable in our homes!"
    })

    # Page 2: Traditional vs. Modern Blueprint
    create_block(l1, 2, 1, "suggested_diagram", "Traditional Utensils vs. Modern Kitchen Tools Blueprint", {
        "caption": "Comparative cabinet blueprint contrasting traditional natural tools with modern processed tools.",
        "diagram_type": "comparison_split"
    })
    create_block(l1, 2, 2, "concept_explanation", "Material Composition & Culinary Advantages", {
        "text": "Understanding what your tools are made of helps you use and care for them properly:\n\n- **Clay Pots (Nyungu)**: Retain heat evenly for slow-cooking traditional greens and stews without burning.\n- **Wooden Cooking Sticks (Mwiko)**: Sturdy and poor conductors of heat, keeping your hands safe from burns while stirring hot ugali.\n- **Calabash Bowls (Kihuri)**: Natural dried gourds ideal for serving sour milk (mursik) and porridge.\n- **Stainless Steel Pots (Sufuria)**: Highly durable, resist corrosion, and heat up quickly on modern gas stoves.\n- **Silicone Spatulas**: Flexible and heat-resistant up to 250°C, perfectly scraping bowls without scratching delicate surfaces."
    })

    # Page 3: The 10 Functional Tool Families
    create_block(l1, 3, 1, "suggested_diagram", "The 10 Functional Tool Families Blueprint", {
        "caption": "Visual breakdown of the 10 distinct functional tool families in the kitchen.",
        "diagram_type": "infographic_grid"
    })
    create_block(l1, 3, 2, "concept_explanation", "The 10 Primary Tool Families", {
        "text": "Every tool in the kitchen belongs to a functional family engineered for a specific cooking action:\n\n- **1. Cutting**: Kitchen knives, peeling knives, kitchen shears.\n- **2. Measuring & Weighing**: Measuring jugs, kitchen scales, measuring spoons.\n- **3. Separating**: Sieves, colanders, tea strainers.\n- **4. Mixing**: Wooden mwiko, rotary whisks.\n- **5. Lifting**: Kitchen tongs, slotted spoons.\n- **6. Turning**: Flat spatulas, fish slices.\n- **7. Scooping**: Soup ladles, ice-cream scoops.\n- **8. Shaping & Moulding**: Cookie cutters, jelly molds.\n- **9. Baking**: Cake tins, baking sheets, rolling pins.\n- **10. Pans & Pots**: Saucepans, frying pans, sufurias."
    })

    # Page 4: Tool-to-Task Safety Table
    create_block(l1, 4, 1, "comparison_table", "Matching Tools to Tasks for Safety and Cookware Protection", {
        "headers": ["Cooking Action", "Dangerous / Unsuitable Tool", "Correct Safe Tool & Rationale"],
        "rows": [
            ["Frying Mandazi in Boiling Oil", "Short table fork (splashes hot oil onto fingers and causes severe burns)", "Long metal tongs or a wire slotted spoon (safely lifts items while allowing hot oil to drain back)"],
            ["Stirring Hot Ugali", "Thin plastic spoon (bends under thick dough and melts against hot pot sides)", "Sturdy wooden mwiko (provides strong leverage without conducting heat to hands)"],
            ["Scraping Non-Stick Teflon Pans", "Metal fork or steel spoon (scratches and strips the delicate non-stick coating)", "Wooden or heat-resistant silicone spatula (glides smoothly without scratching surfaces)"],
            ["Draining Boiled Vegetables", "Holding a hot saucepan lid loose over a sink (slips easily and releases scalding steam)", "A wide colander placed in the sink (safely separates water while retaining greens)"]
        ]
    })

    # Page 5: Worked Example: Equipping a Cooking Station
    create_block(l1, 5, 1, "step_process", "Worked Example: Equipping a Beginner's Cooking Station", {
        "steps": [
            {"number": 1, "title": "Identify the Cooking Tasks", "description": "Review the recipe to determine needed actions (e.g. chopping onions, measuring water, boiling soup, turning chapati)."},
            {"number": 2, "title": "Select the Cutting Tools", "description": "Choose a sharp chef's knife and place a stable cutting board on a non-slip mat."},
            {"number": 3, "title": "Gather Measuring Tools", "description": "Set out a calibrated liquid measuring jug and dry measuring spoons for spices."},
            {"number": 4, "title": "Position Mixing and Turning Tools", "description": "Place a clean wooden mwiko and a flat spatula on a clean utensil rest near the stove."},
            {"number": 5, "title": "Prepare Lifting Tools for Hot Items", "description": "Keep a pair of long tongs and a heat-resistant pot holder ready next to the cooking zone."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l1, 6, 1, "mini_activity", "Hands-On Task: The Home Kitchen Utensil Audit", {
        "instructions": "Inspect your home kitchen with permission from an adult:\n\n- Find and list **5 different kitchen tools** in your notebook.\n- Classify each tool as either **Traditional** or **Modern** based on its material.\n- Assign each tool to one of the **10 Functional Families** (e.g. Mwiko = Traditional / Mixing; Chef's Knife = Modern / Cutting).\n- Share your classification chart with your study group or teacher."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l1, 7, 1, "key_takeaway", "Key Takeaways: Classification & Tool Functions", {
        "text": "Remember these essential tool concepts:\n\n- **Traditional tools** use natural materials (wood, clay, gourds); **modern tools** use processed materials (steel, plastic, silicone).\n- Never use metal tools on **non-stick Teflon pans**—always use wooden or silicone spatulas.\n- Always use **long slotted spoons or tongs** when lifting food from hot frying oil to prevent scalds.\n- Grouping tools into **10 functional families** helps organize a fast, safe kitchen."
    })

    # Page 8: Knowledge Check
    create_block(l1, 8, 1, "knowledge_check", "Scenario Knowledge Check: Tool Classification & Functions", {
        "question": "Wanjiku is preparing pancakes in a non-stick Teflon frying pan. Which tool should she use to flip the pancakes safely without damaging the pan?",
        "options": [
            "A sharp metal table fork to pierce and lift the pancake",
            "A flat wooden or heat-resistant silicone spatula",
            "A short stainless steel butter knife",
            "An iron tablespoon from the cutlery drawer"
        ],
        "correct_index": 1,
        "explanation": "Correct! Wooden and silicone spatulas are smooth and non-abrasive. Metal forks and spoons scratch and destroy the delicate non-stick Teflon coating."
    })

    # =========================================================================
    # LESSON 2: SMART BUYING, BUDGETING & TOOL CARE PROTOCOLS (8 Pages)
    # =========================================================================
    u2, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Smart Buying, Budgeting & Tool Care Protocols",
        defaults={
            "order": 2,
            "description": "Applying the 5 buying factors, practicing comparative shopping, executing the 4-step cleaning protocol, and material-specific maintenance."
        }
    )
    l2 = Lesson.objects.create(
        topic=topic,
        learning_unit=u2,
        title="Smart Buying, Budgeting & Tool Care Protocols",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 2: '{l2.title}' (Lesson ID: {l2.id})")

    # Page 1: Hook & Introduction
    create_block(l2, 1, 1, "suggested_image", "Shopping Day: Value for Money & Tool Care!", {
        "caption": "Selecting durable kitchen tools and maintaining them systematically ensures household financial prudence and food hygiene.",
        "search_query": "kitchen food preparation table"
    })
    create_block(l2, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Evaluate kitchen tools using the **5 Wise Buyer's Purchase Factors** (Budget, Price, Quality, Use, Substitutes).\n- Practice **comparative shopping** to maximize household financial value.\n- Execute the **4-step cleaning protocol** (Scrape -> Wash -> Dry -> Store).\n- Apply **material-specific maintenance** to prevent rust, mold, and warping."
    })
    create_block(l2, 1, 3, "concept_explanation", "The Smart Kitchen Consumer", {
        "text": "Every family has a household budget. When buying kitchen tools, purchasing the cheapest item is not always the best bargain! A low-quality plastic tool that melts on its first day ends up costing more than a durable wooden or steel tool that lasts years.\n\n- Being a **wise consumer** means balancing price with material durability and considering whether you already own a tool that can perform the same task."
    })

    # Page 2: The Wise Buyer's 5-Point Evaluation Matrix
    create_block(l2, 2, 1, "suggested_diagram", "The Wise Buyer's 5-Point Evaluation Matrix", {
        "caption": "The 5 critical factors to consider before purchasing any kitchen tool or equipment.",
        "diagram_type": "decision_matrix"
    })
    create_block(l2, 2, 2, "concept_explanation", "The 5 Factors for Choosing Kitchen Tools", {
        "text": "Before purchasing any tool, ask yourself these 5 questions:\n\n- **1. Budget**: How much money have you allocated for this item?\n- **2. Price**: Is the shopkeeper's price fair and competitive compared to other sellers?\n- **3. Quality**: Is the item durable, rust-resistant, and constructed from food-safe materials?\n- **4. Use & Frequency**: Will your household use this tool daily, or will it sit unused in a drawer?\n- **5. Available Substitutes**: Do you already own a tool (like a traditional woven basket or fork) that does the exact same job?"
    })

    # Page 3: Comparative Shopping Table
    create_block(l2, 3, 1, "comparison_table", "Comparative Shopping: Cheap Plastic vs. Durable Wood & Stainless Steel", {
        "headers": ["Evaluation Criteria", "Low-Quality Budget Plastic Spoon", "Durable Wooden Mwiko / Steel Spoon"],
        "rows": [
            ["Purchase Price", "50 Kenyan Shillings (Very cheap initial cost)", "120 Kenyan Shillings (Moderate initial cost)"],
            ["Material Durability", "Thin, flexible plastic; easily cracks, warps, and melts in hot stews", "Solid dense hardwood or stainless steel; resists heat and bending"],
            ["Lifespan & Replacement", "Lasts 2-4 weeks; must be replaced 6 times a year (Total cost: 300/=)", "Lasts 3-5 years without replacement (Total cost: 120/=)"],
            ["Safety & Hygiene", "Leaches micro-plastics when exposed to high heat; scratches easily", "Food-safe, non-toxic, and does not conduct burning heat to hands"],
            ["Consumer Verdict", "False economy: costs more money over time and creates plastic waste", "Best long-term value: saves household money and protects health"]
        ]
    })

    # Page 4: The 4-Step Care & Storage Flowchart
    create_block(l2, 4, 1, "suggested_diagram", "The 4-Step Hygienic Care & Storage Flowchart", {
        "caption": "Sequential flowchart of the 4 steps for cleaning and storing kitchen tools.",
        "diagram_type": "sequence_flowchart"
    })
    create_block(l2, 4, 2, "step_process", "The 4-Step Cleaning & Storage Sequence", {
        "steps": [
            {"number": 1, "title": "SCRAPE Food Scraps", "description": "Use a rubber scraper or cloth to clear excess grease, dough, and food crumbs into the organic waste bin immediately."},
            {"number": 2, "title": "WASH in Warm Soapy Water", "description": "Scrub gently using a soft sponge and mild detergent. Wash sharp knives individually with the cutting edge pointed away from your fingers."},
            {"number": 3, "title": "DRY Completely in Open Air", "description": "Place washed utensils on a slatted dish drying rack in direct sunlight or dry thoroughly with a clean lint-free towel to prevent bacterial growth and rusting."},
            {"number": 4, "title": "STORE in Dry Ventilated Spaces", "description": "Store dry wooden spoons in drawers, hang knives on magnetic strips or in wooden blocks, and stack pots inverted in ventilated cupboards."}
        ]
    })

    # Page 5: Material-Specific Maintenance
    create_block(l2, 5, 1, "concept_explanation", "Material-Specific Maintenance Rules", {
        "text": "Different materials require specialized cleaning and maintenance:\n\n- **Wooden Utensils**: **Never soak wooden spoons in water!** Soaking causes wood fibers to absorb moisture, swell, warp, and crack. Wash quickly, air-dry under the sun, and occasionally rub with food-grade mineral oil to preserve the grain.\n- **Stainless Steel & Iron Cookware**: Dry completely immediately after washing. Leaving carbon steel knives or iron pans damp triggers rapid red oxidation (**rust**).\n- **Plastics & Silicone**: Wash in warm soapy water. Keep far away from hot stove plates or open charcoal fires to prevent melting and dangerous chemical fumes."
    })

    # Page 6: Hands-On Activity
    create_block(l2, 6, 1, "mini_activity", "Hands-On Task: The Knife Washing & Storage Safety Drill", {
        "instructions": "Practice safe knife hygiene with your teacher or guardian:\n\n- Hold a dull butter knife by its handle under running water.\n- Sponge the blade with soapy water, wiping from the handle outward toward the tip, keeping the sharp edge facing **away from your palm**.\n- Dry the knife immediately with a clean towel.\n- Return the knife to a wooden block or designated drawer slot. Explain why knives should **never be soaked in a soapy sink**."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l2, 7, 1, "key_takeaway", "Key Takeaways: Smart Purchasing & Tool Care", {
        "text": "Remember these consumer and care rules:\n\n- Check the **5 Buying Factors**: Budget, Price, Quality, Use, and Substitutes.\n- **Never soak wooden tools** in water to prevent cracking and mold growth.\n- **Dry metal tools 100%** before storing to prevent rust.\n- Always follow the sequence: **Scrape -> Wash -> Dry -> Store**."
    })

    # Page 8: Knowledge Check
    create_block(l2, 8, 1, "knowledge_check", "Scenario Knowledge Check: Consumer Choice & Kitchen Care", {
        "question": "A student washes a wooden mwiko after cooking ugali and leaves it submerged in a basin of soapy water overnight. What negative effect will this have on the wooden tool?",
        "options": [
            "The wood will become as hard as stainless steel",
            "The wood will absorb water, swell, warp, crack, and become a breeding ground for mold and bacteria",
            "The wood will lose its brown color and turn completely transparent",
            "The wood will shrink to half its original size"
        ],
        "correct_index": 1,
        "explanation": "Correct! Soaking wooden utensils causes the wood fibers to absorb water, leading to swelling, cracking, and mold growth. Wooden tools should be washed quickly and air-dried in the sun."
    })

    # =========================================================================
    # LESSON 3: CREATIVE IMPROVISATION & UPCYCLING PROJECTS (8 Pages)
    # =========================================================================
    u3, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Creative Improvisation & Upcycling Projects",
        defaults={
            "order": 3,
            "description": "Designing, carving, and crafting safe, functional kitchen tools from sustainable local resources and upcycled materials."
        }
    )
    l3 = Lesson.objects.create(
        topic=topic,
        learning_unit=u3,
        title="Creative Improvisation & Upcycling Projects",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 3: '{l3.title}' (Lesson ID: {l3.id})")

    # Page 1: Hook & Introduction
    create_block(l3, 1, 1, "suggested_image", "You Are the Designer: Upcycling Kitchen Tools!", {
        "caption": "Handcrafting functional kitchen tools from fallen local hardwood branches demonstrates sustainable design and resourcefulness.",
        "search_query": "wood carving traditional craft artisan"
    })
    create_block(l3, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Define **improvisation** in the context of kitchen tools and sustainable household management.\n- Select **safe, non-toxic local materials** (like mango, jacaranda, and bamboo) for crafting utensils.\n- Execute the **4-step DIY wooden cooking stick process** (Sourcing -> Shaping -> Sanding -> Sanitizing).\n- Upcycle clean plastic containers into functional **seed sieves, funnels, and measuring cups**."
    })
    create_block(l3, 1, 3, "concept_explanation", "The Art of Sustainable Improvisation", {
        "text": "You do not always need to buy expensive store-bought kitchen tools! **Improvisation** is the creative ability to make functional, safe, and durable tools using locally available natural resources or recycled household items.\n\n- Upcycling saves money, reduces plastic pollution, and teaches valuable practical woodworking and craftsmanship skills."
    })

    # Page 2: 4-Step DIY Wooden Cooking Stick Storyboard
    create_block(l3, 2, 1, "suggested_diagram", "The 4-Step DIY Wooden Cooking Stick Storyboard", {
        "caption": "Sequential comic storyboard showing the 4 steps for safely carving and finishing an improvised wooden cooking stick.",
        "diagram_type": "storyboard_sequence"
    })
    create_block(l3, 2, 2, "step_process", "The 4 Steps of Crafting an Improvised Mwiko", {
        "steps": [
            {"number": 1, "title": "SOURCING Safe Hardwood", "description": "Select a dry, fallen branch of food-safe non-toxic wood (such as mango, jacaranda, guava, or bamboo). Ensure the wood has no rotting core or insect holes."},
            {"number": 2, "title": "SHAPING with Supervision", "description": "Under adult supervision, split the wood branch and use a carving knife or small panga to rough-out the handle and flat paddle shape, cutting away from your body."},
            {"number": 3, "title": "SANDING with Sandpaper", "description": "Rub the surface thoroughly with coarse sandpaper followed by fine sandpaper until all splinters, rough edges, and sharp corners are silky smooth."},
            {"number": 4, "title": "SANITIZING in Boiling Water", "description": "Wash the carved mwiko with warm soapy water, then submerge it in boiling water for 10 minutes to sterilize the wood before its first kitchen use."}
        ]
    })

    # Page 3: Safe vs. Hazardous Materials in Improvisation
    create_block(l3, 3, 1, "comparison_table", "Safe Food-Grade Materials vs. Hazardous Materials in Improvisation", {
        "headers": ["Material Type", "Safe Food-Grade Option", "Hazardous Unsafe Option (Strictly Avoid)"],
        "rows": [
            ["Wood for Spoons / Spatulas", "Dry mango, jacaranda, avocado, or seasoned bamboo (Dense, non-toxic, food-safe)", "Euphorbia, oleander, or cedar wood (Exudes poisonous white sap and toxic chemical resins that contaminate food)"],
            ["Metal for Cutters / Graters", "Food-grade stainless steel wire or clean new aluminum baking sheet strips", "Rusty tin cans or salvaged zinc roofing sheets (Presents fatal tetanus infection risks and shreds toxic rust particles into meals)"],
            ["Plastic for Sieves / Funnels", "Clean food-grade plastic margarine tubs or mineral water bottles with smooth edges", "Chemical detergent bottles, motor oil jugs, or unlabelled pesticide containers (Harbors toxic chemical residues that cannot be washed out)"]
        ]
    })

    # Page 4: Improvised Sieve & Funnel Guide
    create_block(l3, 4, 1, "suggested_diagram", "Safe Upcycled Projects: Improvised Sieve & Funnel Guide", {
        "caption": "Blueprints for upcycling clean food-grade plastic tubs and bottles into kitchen sieves and funnels.",
        "diagram_type": "project_blueprint"
    })
    create_block(l3, 4, 2, "concept_explanation", "Upcycling Clean Plastic Containers", {
        "text": "Common household items can easily be transformed into valuable kitchen aids:\n\n- **Improvised Seed Sieve**: Take an empty, washed 500g margarine tub. Using a heated small nail or sewing needle held with pliers, punch evenly spaced micro-holes in the bottom. Sand off any melted plastic burrs. Perfect for washing and draining millet or sesame seeds!\n- **Improvised Kitchen Funnel**: Cut off the top cone portion of a clean, dry 1-litre plastic mineral water bottle. Use fine sandpaper on the cut edge to make it smooth. Ideal for pouring grains or cooking oil into narrow-necked glass jars without spilling."
    })

    # Page 5: Worked Example: Finishing an Improvised Utensil
    create_block(l3, 5, 1, "step_process", "Worked Example: The 4-Point Quality Inspection for Improvised Tools", {
        "steps": [
            {"number": 1, "title": "Check Surface Smoothness", "description": "Rub your bare hand along all surfaces of the carved utensil. If you feel any splinter or rough grain, continue sanding with fine sandpaper."},
            {"number": 2, "title": "Inspect Balance and Grip", "description": "Hold the handle firmly. It should feel balanced, comfortable, and free of sharp edges that could cause blisters during long stirring sessions."},
            {"number": 3, "title": "Verify Chemical and Odor Safety", "description": "Sniff the wood. It should smell like clean dry timber, with zero chemical, pesticide, or toxic sap odors."},
            {"number": 4, "title": "Sterilize Thoroughly", "description": "Boil in clean water for 10 minutes, allow to sun-dry completely, and lightly season with a few drops of edible cooking oil."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l3, 6, 1, "mini_activity", "Hands-On Project: The Upcycled Container Kitchen Sieve", {
        "instructions": "Create a functional kitchen sieve using recycled home resources:\n\n- Collect an empty, thoroughly washed plastic food tub (e.g. yogurt or margarine container).\n- With assistance from a parent or teacher, use a hot nail or push-pin to pierce a grid of small drainage holes across the base.\n- Smooth down any rough plastic edges with sandpaper.\n- Wash the finished sieve in soapy water, test it by draining washed beans, and bring it to class for peer display!"
    })

    # Page 7: Key Takeaways & Recall
    create_block(l3, 7, 1, "key_takeaway", "Key Takeaways: Sustainable Improvisation", {
        "text": "Remember these golden upcycling principles:\n\n- Always use **safe, non-toxic woods** (mango, jacaranda, bamboo) and **never use poisonous euphorbia**.\n- **Never use rusty cans** for kitchen tools due to severe tetanus and rust contamination risks.\n- Sand all wooden tools **perfectly smooth** to eliminate splinters.\n- **Sanitize and boil** improvised tools before using them in food preparation."
    })

    # Page 8: Knowledge Check
    create_block(l3, 8, 1, "knowledge_check", "Scenario Knowledge Check: Sustainable Improvisation & Safety", {
        "question": "A student wants to carve an improvised wooden spatula for their Home Science cooking class. Which of the following woods is safe and suitable to use?",
        "options": [
            "Poisonous euphorbia tree branch with milky white sap",
            "A dry, non-toxic fallen branch from a local mango or jacaranda tree",
            "A painted timber plank treated with industrial chemical pesticides",
            "A rotting fence post infested with termites"
        ],
        "correct_index": 1,
        "explanation": "Correct! Mango and jacaranda are safe, non-toxic hardwoods ideal for kitchen utensils. Euphorbia has poisonous sap, while painted or pesticide-treated timber leaches lethal chemicals into food."
    })

    total_lessons = topic.lessons.count()
    total_pages = sum(len(set(l.blocks.values_list("page_number", flat=True))) for l in topic.lessons.all())
    total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 2 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CBC Grade 7 Home Science Topic 2: Small Kitchen Tools and Equipment")
    parser.add_argument("--replace", action="store_true", default=True, help="Replace existing topic content")
    args = parser.parse_args()
    ingest_cbc_grade7_home_science_topic2(replace=args.replace)
