"""
VLearn CBC Grade 7 Home Science — Topic 5: Natural Textile Fibres
Curriculum Ingestion Engine (Phase 1: Content, Pages & Blocks)

Curriculum: CBC (ID: 5)
Grade: Grade 7 (ID: 16, Level: 7)
Subject: Home Science (ID: 29)
Topic: Natural Textile Fibres (Order: 5)

Generates 4 Learning Units & 4 Published Lessons (32 Total Structured Pages, 47 Blocks):
  - Unit 1: Classification & Sources of Natural Textile Fibres (8 Pages)
  - Unit 2: Physical Properties & Microscopic Shapes of Natural Fibres (8 Pages)
  - Unit 3: Everyday Household Uses & Sight/Feel Detection (8 Pages)
  - Unit 4: The Science of Burning Tests & Laboratory Safety (8 Pages)

Formatting Standards Applied:
  - Standard markdown bullet lists (- ) with blank line prefixes
  - Prominent bold terms and key concepts
  - Step processes, comparison matrices, and worked examples
  - Zero bracket citations ([83], [84]) and zero prompt meta-language

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade7_home_science_topic5.py [--replace]
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

def ingest_cbc_grade7_home_science_topic5(replace=True):
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 7 HOME SCIENCE — TOPIC 5: NATURAL TEXTILE FIBRES")
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
        name="Natural Textile Fibres",
        defaults={
            "order": 5,
            "description": "Scientific classification of natural textile fibres (plant, animal, mineral), physical properties, microscopic structures, household article applications, sight and feel diagnostics, burning tests, and laboratory fire safety."
        }
    )
    if not created and replace:
        print(f"[*] Replacing existing content for Topic: '{topic.name}' (ID: {topic.id})")
        topic.lessons.all().delete()
        topic.learning_units.all().delete()
    elif created:
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # =========================================================================
    # LESSON 1: CLASSIFICATION & SOURCES OF NATURAL FIBRES (8 Pages)
    # =========================================================================
    u1, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Classification & Sources of Natural Textile Fibres",
        defaults={
            "order": 1,
            "description": "Climbing the Natural Textile Tree, classifying plant, animal, and mineral sources, and understanding natural vs. synthetic fabrics."
        }
    )
    l1 = Lesson.objects.create(
        topic=topic,
        learning_unit=u1,
        title="Classification & Sources of Natural Textile Fibres",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 1: '{l1.title}' (Lesson ID: {l1.id})")

    # Page 1: Hook & Introduction
    create_block(l1, 1, 1, "suggested_image", "Where Do Our Clothes Grow? The Natural Textile Tree", {
        "caption": "Natural textile fibres originate directly from agricultural crops, animal fleece, and natural geological rocks.",
        "search_query": "african cotton field harvest farm"
    })
    create_block(l1, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Define a **textile fibre** as the fundamental hair-like unit of yarn and fabric.\n- Classify natural textile fibres into **plant, animal, and mineral** biological families.\n- Identify specific plant sources (**cotton seed bolls, flax stems, sisal leaves**).\n- Differentiate renewable **natural fibres** from petroleum-derived **synthetic plastics**."
    })
    create_block(l1, 1, 3, "concept_explanation", "From Soil and Animals to Fabric", {
        "text": "The clothes on your body have biological origins! A **textile fibre** is a tiny, hair-like strand that is spun into continuous yarn, which is then woven or knitted into fabric.\n\n- **Natural Textile Fibres**: Fibres obtained directly from nature without chemical synthesis. They split into 3 distinct families:\n\n- **1. Plant (Vegetable) Fibres**: Harvested from seed hairs (Cotton), bast plant stems (Linen from Flax), or tough leaves (Sisal and Jute).\n- **2. Animal (Protein) Fibres**: Harvested from animal fleece/hair (Wool from sheep/goats) or insect cocoon secretions (Silk from silkworms).\n- **3. Mineral Fibres**: Extracted from natural fibrous rocks (Asbestos - historically classified, but recognized today as a hazardous material)."
    })

    # Page 2: Natural Textile Tree Blueprint
    create_block(l1, 2, 1, "suggested_diagram", "The Natural Textile Tree Classification Blueprint", {
        "caption": "Classification flowchart dividing natural textile fibres into Plant, Animal, and Mineral branches.",
        "diagram_type": "classification_tree"
    })
    create_block(l1, 2, 2, "concept_explanation", "Natural vs. Synthetic Fibres", {
        "text": "Not all fabrics are natural:\n\n- **Natural Fibres**: Renewable, biodegradable, breathable, and come from farms or nature (Cotton, Wool, Silk, Linen).\n- **Synthetic Fibres**: Man-made in chemical factories from petroleum oils and plastics (Polyester, Nylon, Acrylic). When burned, synthetics melt into boiling plastic drops!"
    })

    # Page 3: Comparison Table
    create_block(l1, 3, 1, "comparison_table", "Comparative Guide to Natural Fibre Sources", {
        "headers": ["Biological Family", "Specific Natural Source", "Fibre Examples & Local Harvesting"],
        "rows": [
            ["Plant (Seed Hair)", "Fluffy protective seed hairs inside the fruit boll of cotton plants", "Cotton: Grown on farms, harvested after bolls burst open, spun into soft yarn"],
            ["Plant (Stem / Bast)", "Inner bark and fibrous bast tissues inside the stems of flax plants", "Linen: Harvested by soaking flax stems (retting) and beating fibers free"],
            ["Plant (Leaf)", "Long, coarse structural fibers extracted from fleshy plant leaves", "Sisal & Jute: Harvested from sisal leaves; spun into heavy-duty farm ropes & sacks"],
            ["Animal (Fleece)", "Thick, curly, protective hair coats sheared from live sheep or goats", "Wool: Sheared annually, washed, carded, and spun into warm knitting yarn"],
            ["Animal (Secretion)", "Continuous protein liquid spun by silkworm caterpillars for cocoons", "Silk: Unwound gently from silkworm cocoons; woven into lustrous luxury fabric"],
            ["Mineral (Geological)", "Naturally fibrous crystal rock minerals mined from the ground", "Asbestos: Fireproof rock fibre; no longer used in clothing due to health risks"]
        ]
    })

    # Page 4: From Field to Shirt
    create_block(l1, 4, 1, "concept_explanation", "The Journey of Cotton: Soil to Stitch", {
        "text": "How does a plant flower become your school shirt?\n\n- **1. Planting & Bursting**: Cotton seeds grow green bushes that produce white fluffy bolls in dry sunny weather.\n- **2. Harvesting & Ginning**: Cotton bolls are hand-picked; the seeds are removed in a ginning machine.\n- **3. Carding & Spinning**: The fluffy cotton fibers are aligned and twisted tightly into continuous cotton thread.\n- **4. Weaving & Sewing**: Cotton yarns are interlaced on a loom to create cotton fabric, which is dyed and sewn into shirts!"
    })

    # Page 5: Worked Example
    create_block(l1, 5, 1, "step_process", "Worked Example: Tracing a School Uniform from Soil to Stitch", {
        "steps": [
            {"number": 1, "title": "Plant Cultivation", "description": "Cotton shrubs are farmed in warm regions (e.g. Makueni, Kitui, Kisumu) until bolls ripen and burst."},
            {"number": 2, "title": "Ginning & Seed Removal", "description": "Ginning machines separate raw seed hairs from internal cottonseeds (used for cooking oil)."},
            {"number": 3, "title": "Spinning Cotton Yarn", "description": "Spinning frames draw out and twist raw fibers into strong, smooth cotton sewing threads."},
            {"number": 4, "title": "Weaving & Garment Construction", "description": "Weaving looms interlace warp and weft threads to create breathable school uniform fabric."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l1, 6, 1, "mini_activity", "Hands-On Task: The Natural Fibre Scrapbook Collection", {
        "instructions": "Create a natural textile reference page in your notebook:\n\n- Divide a clean page into 3 sections: **Plant Fibres**, **Animal Fibres**, and **Mineral Sources**.\n- Collect 2 small discarded fabric swatches from home (e.g. cotton scrap, piece of knitting wool).\n- Mount them with glue and write down their specific biological origin (e.g. 'Cotton: seed boll of Gossypium plant')."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l1, 7, 1, "key_takeaway", "Key Takeaways: Natural Fibre Classification", {
        "text": "Remember these classification rules:\n\n- **Plant fibres**: Cotton (seed), Linen (stem), Sisal (leaf).\n- **Animal fibres**: Wool (sheep fleece) and Silk (silkworm cocoon secretion).\n- **Mineral fibre**: Asbestos (natural rock).\n- Natural fibres are **renewable, breathable, and biodegradable**."
    })

    # Page 8: Knowledge Check
    create_block(l1, 8, 1, "knowledge_check", "Scenario Knowledge Check: Classification & Natural Sources", {
        "question": "A tailor is sewing a breathable summer shirt from pure Linen fabric. Which biological source did this natural textile raw material come from?",
        "options": [
            "Fleece sheared from sheep in cold highlands",
            "Bast fibers harvested from the stem of the flax plant",
            "Synthetic petroleum chemicals melted in a factory",
            "Cocoon secretions from silkworm caterpillars"
        ],
        "correct_index": 1,
        "explanation": "Correct! Linen is a natural plant (vegetable) fibre harvested from the inner bast stem tissues of the flax plant. Wool comes from sheep, and silk comes from silkworm cocoons."
    })

    # =========================================================================
    # LESSON 2: PHYSICAL PROPERTIES & MICROSCOPIC SHAPES (8 Pages)
    # =========================================================================
    u2, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Physical Properties & Microscopic Shapes of Natural Fibres",
        defaults={
            "order": 2,
            "description": "Investigating fiber absorbency, strength, elasticity, and thermal insulation through microscopic structures."
        }
    )
    l2 = Lesson.objects.create(
        topic=topic,
        learning_unit=u2,
        title="Physical Properties & Microscopic Shapes of Natural Fibres",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 2: '{l2.title}' (Lesson ID: {l2.id})")

    # Page 1: Hook & Introduction
    create_block(l2, 1, 1, "suggested_image", "Fabric Superpowers: Why Clothes Feel and Act Differently", {
        "caption": "Microscopic structural differences give cotton, linen, wool, and silk their unique fabric properties and comfort.",
        "search_query": "textile spinning wool yarn fabric"
    })
    create_block(l2, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Describe the physical properties of **Cotton, Linen, Wool, and Silk**.\n- Identify the **microscopic shapes** of the 4 key natural fibres.\n- Explain why **wool traps body heat** via the air-pocket insulation principle.\n- Explain why **cotton gets stronger when wet** while **wool becomes weak**."
    })
    create_block(l2, 1, 3, "concept_explanation", "How Microscopic Shapes Control Properties", {
        "text": "Every natural fibre possesses physical properties determined by its microscopic structure:\n\n- **Cotton**: High absorbency (drinks water), highly durable, **gets 20% stronger when wet**, cool to wear, low elasticity (creases easily).\n- **Linen**: Extremely strong (stronger than cotton), highly absorbent, stiff texture, natural lustre with uneven yarn bumps (slubs), wrinkles easily.\n- **Wool**: Outstanding warmth, **high elasticity (springs back, resists wrinkles)**, highly absorbent but slow to dry, **becomes weak when wet**, shrinks in hot water.\n- **Silk**: The strongest natural fibre, ultra-smooth and fine, highly lustrous, warm and lightweight, sensitive to high heat and strong sunlight."
    })

    # Page 2: Microscopic Fiber Shapes Blueprint
    create_block(l2, 2, 1, "suggested_diagram", "Microscopic Fiber Shapes Blueprint", {
        "caption": "Microscopic visual guide showing twisted ribbon cotton, bamboo-joint linen, scaly crimped wool, and smooth cylindrical silk.",
        "diagram_type": "microscopic_grid"
    })
    create_block(l2, 2, 2, "concept_explanation", "Reading Microscopic Shapes", {
        "text": "Look closely under a laboratory microscope:\n\n- **Cotton**: Looks like a **twisted, flat ribbon** with hollow lumen channels that suck in water.\n- **Linen**: Looks like straight **bamboo poles with cross-mark joints/nodes**.\n- **Wool**: Looks like a **wavy, scaly hair strand** with microscopic overlapping scales.\n- **Silk**: Looks like a **smooth, continuous double-glass cylinder** that reflects light for rich shine."
    })

    # Page 3: Comparison Table
    create_block(l2, 3, 1, "comparison_table", "Comprehensive Properties Matrix of the 4 Key Fibres", {
        "headers": ["Property", "Cotton (Plant)", "Linen (Plant)", "Wool (Animal)", "Silk (Animal)"],
        "rows": [
            ["Absorbency", "Very High (Instant water uptake)", "Very High (Dries faster than cotton)", "High (Absorbs up to 30% moisture)", "Moderate to High"],
            ["Warmth / Insulation", "Low (Cool & breathable)", "Low (Coolest natural fabric)", "Outstanding (Traps body heat)", "High (Warm yet lightweight)"],
            ["Elasticity & Creasing", "Low (Wrinkles easily; needs iron)", "Low (Creases heavily)", "Very High (Springs back; wrinkle-free)", "High (Moderate wrinkle recovery)"],
            ["Wet Strength", "Gains 20% strength when wet (Washable!)", "Stronger when wet (Highly durable)", "Loses 25% strength wet (Fragile!)", "Loses strength slightly when wet"],
            ["Washability & Heat", "Boilable, tolerates high heat", "Tolerates high ironing heat", "Shrinks in hot water; hand-wash cool", "Requires gentle cool hand-wash"]
        ]
    })

    # Page 4: Thermal Science Blueprint
    create_block(l2, 4, 1, "suggested_diagram", "Thermal Science: Why Wool Traps Heat (The Air Pocket Principle)", {
        "caption": "Diagram showing how wool crimp traps pockets of still air, creating an insulating barrier against heat loss.",
        "diagram_type": "thermal_physics"
    })
    create_block(l2, 4, 2, "concept_explanation", "The Air Pocket Principle", {
        "text": "Wool does not generate heat by itself! Instead:\n\n- Wool fibers have natural microscopic waves called **crimp** and overlapping scales.\n- When woven or knitted, these crimps trap millions of tiny pockets of **still dead air**.\n- Still air is one of the best thermal insulators on Earth! It creates a protective blanket that stops your warm body heat from escaping into the cold morning air."
    })

    # Page 5: Worked Example
    create_block(l2, 5, 1, "step_process", "Worked Example: The Squeeze Test for Wrinkle Recovery", {
        "steps": [
            {"number": 1, "title": "Take Two Fabric Swatches", "description": "Hold a pure cotton handkerchief in your left hand and a pure wool sweater sleeve in your right hand."},
            {"number": 2, "title": "Squeeze into Tight Fists", "description": "Crumple both fabric swatches tightly in your closed fists for 15 seconds."},
            {"number": 3, "title": "Release and Observe", "description": "Open both hands flat on a table. The cotton remains deeply creased and crumpled (low elasticity)."},
            {"number": 4, "title": "Inspect the Wool Swatch", "description": "The wool swatch immediately bounces and springs back to its smooth original shape (high elasticity!)."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l2, 6, 1, "mini_activity", "Hands-On Task: The Water Droplet Absorbency Experiment", {
        "instructions": "Test the absorbency superpower of natural fibres at home:\n\n- Place a flat piece of clean **cotton cloth** and a piece of **polyester/plastic fabric** side by side.\n- Use a teaspoon to place 3 drops of water on each fabric simultaneously.\n- Time how many seconds it takes for the water to soak in completely.\n- Notice how cotton drinks the water in 1 second, while water sits as a bead on polyester!"
    })

    # Page 7: Key Takeaways & Recall
    create_block(l2, 7, 1, "key_takeaway", "Key Takeaways: Properties & Shapes", {
        "text": "Remember these property rules:\n\n- **Cotton** is a flat twisted ribbon; highly absorbent and **stronger when wet**.\n- **Wool** is wavy and scaly; **traps still air for warmth** and resists wrinkles.\n- **Linen** has bamboo-like joints and uneven slubs; strong and cool.\n- **Silk** is a smooth double-cylinder; fine, lustrous, and strong."
    })

    # Page 8: Knowledge Check
    create_block(l2, 8, 1, "knowledge_check", "Scenario Knowledge Check: Physical Properties & Shapes", {
        "question": "Why is 100% cotton fabric universally chosen for making baby nappies, bath towels, and kitchen dishcloths?",
        "options": [
            "Cotton is highly elastic and shrinks into a tiny ball",
            "Cotton is exceptionally absorbent, soft on skin, and gets stronger when washed in hot soapy water",
            "Cotton traps heat better than thick animal wool",
            "Cotton is completely waterproof and repels all liquids"
        ],
        "correct_index": 1,
        "explanation": "Correct! Cotton has outstanding water absorbency, is soft and non-irritating on sensitive skin, and uniquely gains 20% extra tensile strength when wet, allowing it to withstand repeated washing."
    })

    # =========================================================================
    # LESSON 3: EVERYDAY HOUSEHOLD USES & SIGHT/FEEL DETECTION (8 Pages)
    # =========================================================================
    u3, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Everyday Household Uses & Sight/Feel Detection",
        defaults={
            "order": 3,
            "description": "Mapping natural fibres to household articles, conducting non-destructive sight and feel audits, and defeating retail fabric scams."
        }
    )
    l3 = Lesson.objects.create(
        topic=topic,
        learning_unit=u3,
        title="Everyday Household Uses & Sight/Feel Detection",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 3: '{l3.title}' (Lesson ID: {l3.id})")

    # Page 1: Hook & Introduction
    create_block(l3, 1, 1, "suggested_image", "Textiles in the Home: Matching Fabric to Function", {
        "caption": "From absorbent bathroom towels to cozy bedroom blankets and strong farm sacks, every textile serves a precise domestic role.",
        "search_query": "home textiles bedding kitchen towels"
    })
    create_block(l3, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Map natural fibres to specific **household articles and garments** based on utility.\n- Conduct a **non-destructive sight and feel audit** using your eyes and fingers.\n- Identify visual features like **lustre, fuzzy hairs, crimp, and slubs**.\n- Protect family income by spotting **synthetic counterfeit fabrics** in the market."
    })
    create_block(l3, 1, 3, "concept_explanation", "Matching Fibre Superpowers to Domestic Tasks", {
        "text": "Practical Home Science connects scientific properties to everyday household items:\n\n- **Cotton**: Absorbent and washable $\\rightarrow$ Bath towels, bedsheets, baby wear, school shirts, and kitchen cleaning cloths.\n- **Linen**: Stiff, smooth, and durable $\\rightarrow$ Tablecloths, dining napkins, luxury handkerchiefs, and sofa slipcovers.\n- **Wool**: Warm and springy $\\rightarrow$ Winter blankets, heavy cardigans, marvin caps, thick socks, and living room carpets.\n- **Silk**: Lustrous, fine, and elegant $\\rightarrow$ Evening dresses, neckties, bridal wear, and premium luxury curtains.\n- **Sisal & Jute**: Tough and coarse $\\rightarrow$ Farm sacks (gunia) for carrying maize, and heavy-duty ropes."
    })

    # Page 2: Household Scene Blueprint
    create_block(l3, 2, 1, "suggested_diagram", "Household Bedroom & Living Room Textiles Blueprint", {
        "caption": "Cutaway household blueprint illustrating the functional distribution of cotton, wool, linen, and silk articles.",
        "diagram_type": "household_scene"
    })
    create_block(l3, 2, 2, "concept_explanation", "The Sight and Feel Diagnostic Method", {
        "text": "You do not need a lab to audit fabrics when shopping—use your senses!\n\n- **Sight (Eyes)**: Look at the lustre (shine), surface texture, and thread consistency. Does it have fuzzy surface hairs (Cotton), irregular thick/thin bumps called slubs (Linen), wavy crimped yarn (Wool), or an ultra-fine glowing shine (Silk)?\n- **Feel (Hands)**: Squeeze and stroke the fabric. Does it feel cool and stay crumpled (Cotton), stiff and firm (Linen), warm and springy (Wool), or slippery and smooth (Silk)?"
    })

    # Page 3: Comparison Table: Sight & Feel
    create_block(l3, 3, 1, "comparison_table", "The Sight and Feel Diagnostic Guide", {
        "headers": ["Fibre", "Visual Appearance (Sight)", "Tactile Sensation (Touch / Feel)", "Wrinkle Reaction"],
        "rows": [
            ["Cotton", "Dull, low lustre, tiny fuzzy surface hairs", "Soft, cool, lightweight, comfortable", "Stays crumpled when squeezed in a fist"],
            ["Linen", "Slight natural sheen, visible uneven yarn slubs", "Cool, stiff, very firm, smooth", "Creases heavily; sharp wrinkle lines"],
            ["Wool", "Dull, thick, wavy/crimped threads, fuzzy surface", "Warm, springy, spongy, slightly coarse", "Bounces back immediately with zero wrinkles!"],
            ["Silk", "Highly lustrous, rich glowing shine, ultra-fine weave", "Incredibly smooth, soft, warm, slippery", "Light creasing; smooths out gently"]
        ]
    })

    # Page 4: Spotting Marketplace Scams
    create_block(l3, 4, 1, "suggested_diagram", "The Sight and Feel Diagnostic Guide", {
        "caption": "Comparative sensory guide for rapid fabric identification during market shopping.",
        "diagram_type": "sensory_grid"
    })
    create_block(l3, 4, 2, "concept_explanation", "Defeating Counterfeit Fabric Scams", {
        "text": "Dishonest market sellers often sell cheap synthetic polyester labeled as '100% Pure Wool':\n\n- **The Wool Squeeze Test**: Pure sheep wool feels naturally warm and springs back like a sponge when compressed. Cheap synthetic acrylic feels cold, squeaks when pinched, and lacks springy wool crimp.\n- **The Linen Slub Check**: Genuine linen always has natural, irregular thick bumps (slubs) in the weave. Synthetic fake linen has perfectly uniform plastic threads."
    })

    # Page 5: Worked Example
    create_block(l3, 5, 1, "step_process", "Worked Example: Auditing an Unmarked Textile Swatch", {
        "steps": [
            {"number": 1, "title": "Visual Inspection Under Light", "description": "Hold the swatch to the window. You observe thick, fuzzy, wavy yarns with a completely matte, dull surface."},
            {"number": 2, "title": "Tactile Temperature Check", "description": "Place the fabric against your forearm. It feels immediately warm and cozy to the skin."},
            {"number": 3, "title": "Perform the Squeeze Test", "description": "Crumple the swatch into a tight ball for 10 seconds and release. It instantly springs back into shape without creases."},
            {"number": 4, "title": "Confirm Diagnostic Verdict", "description": "Verdict: 100% Animal Wool! Ideal for winter sweaters and warm blankets."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l3, 6, 1, "mini_activity", "Hands-On Task: The Blindfolded Fabric Touch Challenge", {
        "instructions": "Test your tactile senses with a classmate or family member:\n\n- Blindfold your partner and hand them 3 different household fabric swatches (e.g. cotton towel, wool sock, silky scarf).\n- Have them describe the **temperature (warm/cool)**, **texture (fuzzy/smooth/stiff)**, and **springiness**.\n- Score their ability to identify the correct natural fibre based purely on touch!"
    })

    # Page 7: Key Takeaways & Recall
    create_block(l3, 7, 1, "key_takeaway", "Key Takeaways: Household Uses & Detection", {
        "text": "Remember these diagnostic rules:\n\n- Match fibres to jobs: **Cotton for towels**, **Wool for blankets**, **Linen for tablecloths**, **Sisal for sacks**.\n- **Cotton**: Dull and stays crumpled.\n- **Wool**: Warm, wavy, and **springs back wrinkle-free**.\n- **Linen**: Stiff with **natural slubs**.\n- **Silk**: **Ultra-smooth and lustrous**."
    })

    # Page 8: Knowledge Check
    create_block(l3, 8, 1, "knowledge_check", "Scenario Knowledge Check: Household Uses & Sensory Testing", {
        "question": "A farmer needs to buy durable, heavy-duty sacks (gunia) to transport 90kg bags of harvested dry maize safely. Which natural plant fibre is the strongest and most suitable choice?",
        "options": [
            "Delicate silkworm silk",
            "Coarse, tough plant leaf/stem fibres like Sisal or Jute",
            "Soft, fine cotton seed hairs",
            "Fluffy sheep wool"
        ],
        "correct_index": 1,
        "explanation": "Correct! Sisal and jute are coarse, tough, high-strength natural plant fibres specifically engineered by nature for heavy-duty agricultural sacks (gunia) and durable transport ropes."
    })

    # =========================================================================
    # LESSON 4: THE SCIENCE OF BURNING TESTS & LAB SAFETY (8 Pages)
    # =========================================================================
    u4, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="The Science of Burning Tests & Laboratory Safety",
        defaults={
            "order": 4,
            "description": "Conducting supervised chemical burning tests, analyzing flame behavior, smoke odor, and ash residue, and enforcing the 6 laboratory safety rules."
        }
    )
    l4 = Lesson.objects.create(
        topic=topic,
        learning_unit=u4,
        title="The Science of Burning Tests & Laboratory Safety",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 4: '{l4.title}' (Lesson ID: {l4.id})")

    # Page 1: Hook & Introduction
    create_block(l4, 1, 1, "suggested_image", "The Flame of Truth: Laboratory Identification of Fibres", {
        "caption": "When a tiny textile thread meets a flame under strict safety protocols, its chemical identity is revealed by flame color, odor, and ash.",
        "search_query": "laboratory candle flame science experiment"
    })
    create_block(l4, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Explain the chemical basis of fibre burning tests (**Cellulose vs. Protein**).\n- Distinguish **plant fibre burning reactions** (yellow flame, paper odor, soft grey ash).\n- Distinguish **animal fibre burning reactions** (sputtering flame, burnt hair odor, crushable dark bead).\n- Strictly enforce the **6 Golden Rules of Laboratory Fire Safety**."
    })
    create_block(l4, 1, 3, "concept_explanation", "The Chemistry of the Burning Test", {
        "text": "When sensory tests are inconclusive, a **burning test** provides definitive proof of a fibre's chemical makeup:\n\n- **Plant Fibres (Cotton, Linen)**: Made of **Cellulose** (the same plant polymer in wood and paper). They ignite easily, burn with a steady yellow flame, smell like **burning paper/leaves**, and leave **feather-soft grey/white ash**.\n- **Animal Fibres (Wool, Silk)**: Made of **Protein** (keratin, the same protein in human hair and fingernails). They burn slowly, sputter, tend to self-extinguish, smell strongly of **burning hair/feathers**, and leave a **dark, irregular, crushable bead**."
    })

    # Page 2: Burning Reactions Blueprint
    create_block(l4, 2, 1, "suggested_diagram", "Fibre Burning Reactions: Cellulose vs. Protein Blueprint", {
        "caption": "Split laboratory diagram illustrating the distinct flame colors, smoke odors, and residues of plant versus animal fibres.",
        "diagram_type": "chemical_burning_lab"
    })
    create_block(l2, 2, 2, "concept_explanation", "The Synthetic Hazard Warning", {
        "text": "Beware of synthetic fabrics in fire:\n\n- Unlike natural fibres that leave soft ash or crushable beads, **synthetic fibres (polyester/nylon) melt into boiling, sticky liquid chemical drops** that stick to human skin and harden into rock-solid, uncrushable plastic beads. Natural fibres are far safer around brief sparks!"
    })

    # Page 3: Comparison Table: Burning Reactions
    create_block(l4, 3, 1, "comparison_table", "Burning Test Chemical & Physical Reaction Matrix", {
        "headers": ["Fibre Type", "Approaching Flame", "In Flame Reaction", "Smoke Odor", "Residue / Ash Character"],
        "rows": [
            ["Cotton (Plant)", "Does not shrink from flame", "Ignites quickly, burns with bright yellow flame, continues burning", "Smells like burning paper or dry wood", "Light, soft, feather-like grey/white ash"],
            ["Linen (Plant)", "Does not shrink from flame", "Burns steadily with yellow flame, glows after flame out", "Smells like burning paper/grass", "Fine, soft, light grey ash"],
            ["Wool (Animal)", "Shrinks and curls away from flame", "Burns slowly, sputters, self-extinguishes when removed from flame", "Strong pungent smell of burning hair or feathers", "Dark, irregular, hollow bead that crumbles to powder easily"],
            ["Silk (Animal)", "Curls away from flame", "Burns slowly with gentle sputter, self-extinguishes", "Smells like burning hair / singed horn", "Dark, crushable bead / black friable ash"],
            ["Polyester (Synthetic)", "Melts and curls away rapidly", "Burns and melts with black chemical smoke", "Sweet chemical plastic smell", "Hard, round, black, uncrushable plastic bead"]
        ]
    })

    # Page 4: Lab Safety Blueprint
    create_block(l4, 4, 1, "suggested_diagram", "The 6 Golden Rules of Laboratory Fire Safety", {
        "caption": "Visual safety checklist illustrating metal forceps, candle on tin plate, water bowl, open ventilation, tied hair, and adult supervision.",
        "diagram_type": "safety_checklist"
    })
    create_block(l4, 4, 2, "concept_explanation", "The 6 Golden Rules of Laboratory Safety", {
        "text": "Fire is a serious hazard! Always follow these 6 mandatory safety rules:\n\n- **1. Adult Supervision**: Never conduct a burning test alone; always work under a teacher or parent's watch.\n- **2. Metal Forceps Only**: Always hold yarn samples with long metal tweezers. **NEVER hold burning samples with bare fingers!**\n- **3. Stable Candle Base**: Place your candle securely on a wide, non-flammable metal tin or ceramic saucer.\n- **4. Water Bowl Ready**: Keep a container of clean water beside you to immediately douse hot sparks.\n- **5. Adequate Ventilation**: Perform tests near open windows so chemical smoke and fumes disperse quickly.\n- **6. Personal Apparel**: Tie back long hair, roll up long sleeves, and tuck in loose ties or sweaters."
    })

    # Page 5: Worked Example
    create_block(l4, 5, 1, "step_process", "Worked Example: Step-by-Step Execution of a Safe Burning Test", {
        "steps": [
            {"number": 1, "title": "Secure Safety Station", "description": "Tuck in clothing, place candle on tin saucer, fill a cup with water, and invite the teacher to supervise."},
            {"number": 2, "title": "Grip Sample with Forceps", "description": "Grip a 3cm long dry yarn thread securely with metal forceps (holding it at the far end)."},
            {"number": 3, "title": "Introduce to Candle Flame Edge", "description": "Bring the fiber tip to the edge of the flame. Observe: Does it melt, ignite, or curl away? Note the flame color."},
            {"number": 4, "title": "Waft Odor & Test Residue", "description": "Gently waft smoke toward your nose. Blow out the flame, let the tip cool for 10 seconds, and press the residue between your fingers."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l4, 6, 1, "mini_activity", "Hands-On Task: Safety Audit of a Science Desk", {
        "instructions": "Audit a laboratory desk setup in your notebook before conducting a test:\n\n- Draw a sketch of your desk and verify the presence of: **Metal Forceps**, **Stable Candle on Tin**, and **Bowl of Water**.\n- List 3 hazards that must be removed (e.g. loose papers, flammable spirit bottles, open curtains).\n- Recite the 6 Golden Safety Rules to your teacher or group partner."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l4, 7, 1, "key_takeaway", "Key Takeaways: Burning Tests & Safety", {
        "text": "Remember these lab essentials:\n\n- **Plant fibres (Cellulose)**: Yellow flame, burning paper odor, **soft grey ash**.\n- **Animal fibres (Protein)**: Sputtering flame, burning hair odor, **crushable dark bead**.\n- **Always use metal forceps** and keep a **bowl of water** within reach.\n- Never perform fire experiments without **adult supervision**."
    })

    # Page 8: Knowledge Check
    create_block(l4, 8, 1, "knowledge_check", "Scenario Knowledge Check: Burning Tests & Lab Safety", {
        "question": "A Grade 7 student tests an unknown yarn sample using metal forceps over a candle. The thread burns slowly, self-extinguishes when removed from the flame, smells strongly of burnt hair, and leaves a dark, brittle bead that crumbles to powder when pressed. What fibre is this?",
        "options": [
            "Cotton (plant cellulose fibre)",
            "Linen (flax bast fibre)",
            "Wool (animal protein fibre)",
            "Synthetic polyester plastic"
        ],
        "correct_index": 2,
        "explanation": "Correct! Wool is an animal protein fibre. Its protein structure causes it to burn slowly, self-extinguish, emit the distinct odor of burning hair/feathers, and leave a crushable dark bead."
    })

    total_lessons = topic.lessons.count()
    total_pages = sum(len(set(l.blocks.values_list("page_number", flat=True))) for l in topic.lessons.all())
    total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 5 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CBC Grade 7 Home Science Topic 5: Natural Textile Fibres")
    parser.add_argument("--replace", action="store_true", default=True, help="Replace existing topic content")
    args = parser.parse_args()
    ingest_cbc_grade7_home_science_topic5(replace=args.replace)
