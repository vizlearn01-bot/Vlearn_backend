"""
VLearn Curriculum Ingestion Script
CBC Grade 7 — Home Science
Topic 9: Special Treatments in Laundrywork (Order: 9)

Creates:
- Topic 9: Special Treatments in Laundrywork (Order: 9)
- 4 Learning Units
- 4 Published Lessons (32 Pages, 8 per lesson)
- 40 LessonBlocks (10 per lesson)
- Clean, student-friendly content with zero bracket citations, proper '- ' list formatting.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def ingest_cbc_grade7_home_science_topic9():
    print("=" * 80)
    print("INGESTING CBC GRADE 7 HOME SCIENCE — TOPIC 9: SPECIAL TREATMENTS IN LAUNDRYWORK")
    print("=" * 80)

    # 1. Resolve Curriculum, Grade, Subject
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    assert grade, "Grade 7 not found!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject Home Science not found!"

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}")

    # 2. Create or Get Topic 9
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Special Treatments in Laundrywork",
        defaults={
            "order": 9,
            "description": "Mastering specialized fabric care procedures: spotting tough stains, extracting homemade starch from potatoes and grains, starching cottons, sponging structured blazers, safe home dry-cleaning, and practicing eco-friendly chemical disposal."
        }
    )
    if not created:
        topic.order = 9
        topic.description = "Mastering specialized fabric care procedures: spotting tough stains, extracting homemade starch from potatoes and grains, starching cottons, sponging structured blazers, safe home dry-cleaning, and practicing eco-friendly chemical disposal."
        topic.save()
    print(f"[+] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Clean existing units and lessons under this topic for idempotent ingestion
    topic.learning_units.all().delete()
    print("[*] Cleared existing learning units and lessons under Topic 9.")

    units_data = [
        {
            "order": 1,
            "title": "Understanding Special Treatments in Laundrywork",
            "description": "Differentiating standard immersion washing from specialized fabric care methods: spotting, sponging, starching, and home dry-cleaning.",
            "lesson_title": "The 4 Special Treatments: Spotting, Sponging, Starching & Dry-Cleaning",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Monday Morning Wardrobe Dilemma!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "wardrobe clothes hangers",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Wardrobe_with_clothes_hangers_and_gap_illuminated_from_window_light_01.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Wardrobe_with_clothes_hangers_and_gap_illuminated_from_window_light_01.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "A household wardrobe with garments organized on hangers, showcasing proper textile care and garment preservation."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Standard Washing Isn't Always Enough",
                    "type": "rich_text",
                    "content": {
                        "text": """### Beyond the Bucket of Water

It is Sunday evening, and you are preparing your school uniform for Monday morning:
- Your white cotton shirt looks floppy, limp, and wrinkly.
- There is a dark spot of grease on your sleeve.
- Your heavy dark woolen school blazer smells dusty and has surface sweat marks.

If you throw everything into a tub of hot soapy water:
- The grease stain on your sleeve will spread and set permanently!
- Your woolen blazer will absorb massive amounts of water, shrink, and lose its shape!

Standard washing cannot solve every problem. Today, we unlock the **Four Special Treatments** in laundrywork that keep our clothes crisp, fresh, and long-lasting!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 4 Special Laundry Treatments Wardrobe",
                    "type": "diagram",
                    "content": {
                        "title": "The 4 Special Laundry Treatments Wardrobe Care Blueprint",
                        "description": "Illustrated wardrobe mapping different garments (cotton shirt, woolen blazer, silk scarf, stained trousers) to their matching special laundry treatments."
                    }
                },
                {
                    "page": 2,
                    "title": "The 4 Special Treatments Defined",
                    "type": "rich_text",
                    "content": {
                        "text": """### Matching Fabric Properties to Specialized Care

Special treatments are targeted fabric care procedures applied to clothes and household articles to solve specific fabric needs:

- **1. Spotting**: The targeted, localized treatment and removal of stubborn blemishes (such as ink, tea, grease, or blood) before the whole garment is washed.
- **2. Sponging**: Reviving heavy, dark, or structured non-washable garments (like woolen school blazers or coats) by brushing off dust and wiping the surface with a damp soapy sponge without soaking the inner linings.
- **3. Starching**: Dipping washed white cottons or linens in a natural starch solution to give them a crisp, smooth, stiff finish and a dirt-repelling shield when ironed.
- **4. Home Dry-Cleaning**: Cleaning delicate fabrics (such as pure silk scarves or fine ties) using liquid chemical dry solvents instead of water to prevent shrinkage, color loss, or fabric distortion."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Why Special Treatments Matter to Families",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Economic & Aesthetic Value of Special Care

Applying the correct special treatments provides three major household benefits:

#### 1. Extends Garment Lifespan
- Harsh tub washing breaks delicate wool fibers and tears delicate silks.
- Sponging and dry-cleaning preserve original tailoring, shoulder pads, and fibers for years!

#### 2. Huge Financial Savings
- Commercial dry-cleaning a school blazer or suit costs hundreds of shillings.
- Sponging blazers and making homemade potato starch at home costs virtually **KES 0**, saving significant family income!

#### 3. Smart & Professional Presentation
- Starched school collars stand upright, sharp, and resist wrinkling throughout long school days, giving students pride and confidence!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Fabric Structure & Special Care Decision Matrix",
                    "type": "diagram",
                    "content": {
                        "title": "Fabric Structure & Special Care Decision Matrix",
                        "description": "Decision flowchart guiding learners on how to inspect garment fabric type (Cotton, Wool, Silk, Stained) and select the exact correct laundry treatment."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Wardrobe Care Misconceptions & Traps",
                    "type": "rich_text",
                    "content": {
                        "text": """### Common Laundry Traps to Avoid

**Myth 1**: *"Every dirty garment should be soaked in a tub of soapy water to get truly clean."*
- **Fact**: Soaking structured woolen school blazers or delicate silks in water is disastrous! Wool fibers shrink and felt together, while inner canvas pads and shoulder linings warp and separate, permanently ruining the blazer's fit.

**Myth 2**: *"Starching is only for fancy hotel tablecloths, not for school uniforms."*
- **Fact**: Starching school uniforms forms a smooth microscopic shield that stops red soil and sweat from soaking deep into cotton fibers. On the next wash day, dirt washes away twice as easily!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The Wardrobe Care Audit",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Sort Your Laundry Like a Professional

Follow these 4 inspection steps before doing laundry:

- **Step 1: Check for Localized Stains**: Inspect collars, cuffs, and pockets for ink, tea, or grease stains $\rightarrow$ Tag for **Spotting** before general wash.
- **Step 2: Inspect Structured & Woolen Garments**: Check blazers, winter coats, and ties $\rightarrow$ Tag for **Sponging** (or dry-cleaning) without water immersion.
- **Step 3: Identify White Cottons & Linens**: Select school shirts, pillowcases, and handkerchiefs $\rightarrow$ Tag for **Starching** after regular washing.
- **Step 4: Separate Delicate Water-Sensitive Fabrics**: Identify pure silk scarves or pleated dresses $\rightarrow$ Tag for **Home Dry-Cleaning** under adult supervision!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Home Science Challenge: Saving the School Blazer",
                    "type": "rich_text",
                    "content": {
                        "text": """### Solve the Sunday Laundry Crisis!

**The Situation**:
Mwangi came home from a school debate with dust on his dark woolen blazer cuffs and slight sweat under the arms. His younger brother suggests: *"Let's dump the blazer into a bucket of boiling water with detergent and scrub it with a hard brush!"*

**The Diagnosis**:
- Soaking and scrubbing the wool blazer in hot water will felt the wool fibers, shrink the jacket by two sizes, and destroy the shoulder pads!

**The Correct Special Treatment**:
- Perform **Sponging**:
  1. Brush off all dry dust downwards with a clothes brush.
  2. Wipe the collar and cuffs with a sponge wrung out of warm soapy water until barely damp.
  3. Wipe off soap with a clean damp cloth.
  4. Hang on a hanger in the shade to dry!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Special Treatments Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why should a structured dark woolen school blazer be cleaned by 'sponging' rather than being soaked and washed in a tub of hot soapy water?",
                        "options": [
                            "Because sponging makes the blazer change into a brighter color",
                            "Because soaking and agitating wool in hot water causes the fibers to shrink, felt, and distort the internal shoulder pads and linings",
                            "Because wool can only dissolve in pure alcohol",
                            "Because hot soapy water makes the blazer too heavy to hang"
                        ],
                        "correct_index": 1,
                        "explanation": "Wool fibers are delicate and scale-covered; immersion in hot water combined with mechanical agitation causes the scales to interlock (felting and shrinkage) and permanently ruins internal pads and canvas linings. Sponging cleans the surface without soaking internal structures."
                    }
                }
            ]
        },
        {
            "order": 2,
            "title": "Stains and Spotting Procedures",
            "description": "Identifying stain categories (protein, grease, chemical ink, tannin tea), matching them to household reagents, and executing the outside-in spotting protocol.",
            "lesson_title": "Stain Chemistry & Precision Spotting Techniques",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Spot on the Sleeve!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "stain on white cotton fabric",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Perspiration_stain_on_white_cotton_T-shirt.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Perspiration_stain_on_white_cotton_T-shirt.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "A localized stain on white cotton fabric requiring targeted spotting treatment before general washing."
                    }
                },
                {
                    "page": 1,
                    "title": "Don't Wash That Stain Yet!",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Science of Fabric Stains

A **stain** is an uninvited blemish on your fabric caused by a foreign substance that has physically or chemically bonded with the threads.

Imagine you accidentally cut your finger in agriculture class and get a drop of fresh blood on your white cotton sleeve.
Your friend screams: *"Quick, boil water in a sufuria and pour it over the blood to melt it away!"*

**STOP! That single mistake will permanently ruin your shirt!**
Why? Because heat **cooks** the protein in blood, permanently locking it into the cotton threads!

To remove stains like a scientist, you must understand stain chemistry and practice precision **spotting**!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 4 Common Stain Categories & Reagents",
                    "type": "diagram",
                    "content": {
                        "title": "The 4 Common Stain Categories & Household Reagent Repertoire",
                        "description": "Illustrated chemical chart showing Protein stains (blood), Grease stains (oil), Chemical stains (ink), and Tannin stains (tea) matched to their safe household reagents."
                    }
                },
                {
                    "page": 2,
                    "title": "Stain Categories & Household Reagents",
                    "type": "rich_text",
                    "content": {
                        "text": """### Matching Stain Chemistry to Household Reagents

Different stains require different chemical mechanisms to dissolve or release:

- **1. Protein Stains (Fresh Blood, Raw Egg, Milk)**:
  - *Reagent*: **Cold water + Table Salt**.
  - *Golden Rule*: **NEVER USE HOT WATER!** Heat coagulates (solidifies) protein molecules, binding them permanently into the weave.
- **2. Grease & Oil Stains (Cooking Fat, Engine Oil, Butter)**:
  - *Reagent*: **Chalk / Talcum powder** (to absorb oil), followed by **warm detergent water**.
- **3. Chemical & Dye Stains (Ballpoint Pen Ink, Fruit Juice)**:
  - *Reagent*: **Fresh lemon juice** or **sour milk** (mild acid breaks down chemical dye bonds).
- **4. Tannin Stains (Black Tea, Coffee)**:
  - *Reagent*: **Boiling water flushed from a height** (for white cottons) or **glycerine** to soften dried tannin rings."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "The 'Outside-In' Technique & Blotting",
                    "type": "rich_text",
                    "content": {
                        "text": """### Precision Spotting Technique Rules

When treating a localized stain, improper rubbing will make a tiny dot spread into a massive blemish! Follow these two golden physical rules:

#### 1. The 'Outside-In' Circular Rubbing Rule
- Always start rubbing at the **outer boundary edges** of the stain and work inwards toward the center!
- *Why?* Rubbing from the center outward pushes the dissolved dye into clean surrounding threads, creating an ugly, giant stain ring!

#### 2. The Clean Blotter Underneath
- Always place a folded clean white cloth, paper towel, or absorbent pad directly beneath the stained area.
- *Why?* As your reagent dissolves the stain, the blotter absorbs the lifted pigment immediately, preventing it from soaking through to the back of the shirt!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The 4-Step Precision Spotting Sequence",
                    "type": "diagram",
                    "content": {
                        "title": "The 4-Step Precision Spotting Sequence Blueprint",
                        "description": "Step-by-step storyboard demonstrating 1. Cold salt soak $\rightarrow$ 2. Blotter placement underneath $\rightarrow$ 3. Outside-in rubbing with soft sponge $\rightarrow$ 4. Cold water flush."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Stain Removal Myths & Critical Cautions",
                    "type": "rich_text",
                    "content": {
                        "text": """### Spotting Myths vs. Scientific Facts

**Myth 1**: *"Bleach should be poured directly on every stain to make it disappear instantly."*
- **Fact**: Concentrated chlorine bleach weakens and corrodes cotton threads, eats holes into delicate fabrics, and strips color from non-white garments. Always try mild natural reagents (lemon juice, salt, chalk) first!

**Myth 2**: *"If a stain is dry, just iron it flat and it will flake off."*
- **Fact**: Ironing a stained garment applies intense heat that chemically bakes (sets) the stain into the fabric forever. Never iron a garment until all stains are completely removed!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Removing a Fresh Grease Stain",
                    "type": "rich_text",
                    "content": {
                        "text": """### The 5-Step Grease Eraser Protocol

Follow this exact procedure to remove cooking oil from a tablecloth or uniform:

- **Step 1: Scrape Excess Surface Oil**: Use the back of a blunt table knife to gently lift off thick surface grease without pressing it deeper into threads.
- **Step 2: Place an Absorbent Blotter**: Slide a clean white cloth or paper towel directly under the stained patch.
- **Step 3: Apply Absorbent Powder**: Sprinkle white blackboard chalk dust or talcum powder over the stain and let it sit for **5 minutes** to draw out the liquid oil.
- **Step 4: Dab with Warm Detergent**: Using a soft cloth dipped in warm soapy water, rub gently from the **outside-in** towards the center.
- **Step 5: Rinse & Inspect**: Flush with clean warm water and check the fabric before hanging to dry!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Spotting Expert: The Red Ink Disaster",
                    "type": "rich_text",
                    "content": {
                        "text": """### Spot the Chemist's Solution!

**The Situation**:
During an English exam, a ballpoint pen leaked red ink onto Amani's white school pocket. Her classmate advised her to rub it vigorously with hot bath soap under a hot tap.

**The Result**:
- The hot soap caused the ink pigments to spread across the entire pocket, creating a dark pink ring!

**The Proper Spotting Procedure**:
- Place a clean white blotting cloth inside the pocket under the stain.
- Squeeze fresh **lemon juice** directly onto the ink mark.
- Dab gently with a cotton bud from the **outside-in**.
- Rinse with cold water and repeat until the red ink is completely lifted!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Stains & Spotting Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "When removing a localized ink or grease stain on a garment, why is it mandatory to rub gently from the 'outside edges toward the center' rather than from the center outward?",
                        "options": [
                            "Because rubbing inward makes the fabric dry much faster",
                            "Because rubbing from the center outward pushes dissolved stain pigments into clean surrounding fibers, spreading the stain into a larger blemish",
                            "Because the center of a stain is always made of hot water",
                            "Because rubbing inward changes the chemical formula of cotton into silk"
                        ],
                        "correct_index": 1,
                        "explanation": "Rubbing from the outside-in confines the dissolved stain pigments to the original blemish area and prevents the stain from spreading outwards into clean surrounding fabric fibers."
                    }
                }
            ]
        },
        {
            "order": 3,
            "title": "Preparing Homemade Starch & Starching Procedures",
            "description": "Extracting pure raw starch from kitchen potatoes and grains, understanding starch dilution ratios, and mastering the heat-gelatinization protective barrier.",
            "lesson_title": "Zero-Cost Homemade Starch Extraction & Fabric Starching",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Pure Starch from Your Kitchen Garden!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "potato starch",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Potato_Starch.JPG",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Potato_Starch.JPG",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "Pure white potato laundry starch extracted cleanly from kitchen root vegetables."
                    }
                },
                {
                    "page": 1,
                    "title": "The Secret of Crisp, Dirt-Repelling Clothes",
                    "type": "rich_text",
                    "content": {
                        "text": """### Discovering Kitchen Starch

Have you ever cut an Irish potato and noticed a white, slippery paste left on your fingers?
Or noticed how cloudy the water becomes when your parents wash rice or soak maize before cooking?

That white cloudiness is **natural starch**—a carbohydrate powerhouse found in abundance in our local foods!

Instead of spending family money on expensive synthetic aerosol spray starch at the supermarket, you can extract pure, organic laundry starch right in your kitchen for **zero shillings**!

Let's master the 6 steps of potato starch extraction and learn how starching gives your school uniform a superhero shield against dirt!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 6-Step Potato Starch Extraction Flowchart",
                    "type": "diagram",
                    "content": {
                        "title": "The 6-Step Potato Starch Kitchen Extraction Flowchart",
                        "description": "Step-by-step process flowchart showing 1. Peel & Wash $\rightarrow$ 2. Grate finely $\rightarrow$ 3. Soak & Stir $\rightarrow$ 4. Strain through cloth $\rightarrow$ 5. Settle sediment $\rightarrow$ 6. Decant water."
                    }
                },
                {
                    "page": 2,
                    "title": "The 6 Steps of Extracting Potato Starch",
                    "type": "rich_text",
                    "content": {
                        "text": """### Extracting Raw Cold Starch at Home

Follow this exact 6-step laboratory procedure:

- **Step 1: Peel & Wash**: Peel two medium Irish potatoes and wash them thoroughly in clean cold water to remove all surface soil.
- **Step 2: Grate Finely**: Grate the raw potatoes finely into a clean bowl using the small holes of a kitchen grater.
- **Step 3: Soak in Cold Water**: Add 500 ml of clean cold water to the grated shreds and stir vigorously to release microscopic starch granules.
- **Step 4: Strain Through Cloth**: Pour the mixture through a clean cotton cloth or fine sieve, squeezing the pulp tightly to extract all milky starchy liquid while keeping solid potato shreds behind.
- **Step 5: Let Sediment Settle**: Leave the milky liquid undisturbed for **10 to 15 minutes**. The heavy, pure white starch granules will sink to the bottom.
- **Step 6: Decant Excess Water**: Slowly pour off (decant) the top yellowish water, leaving pure, thick white **potato starch paste** at the bottom!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "How Starch Protects Fabrics: The Shield Effect",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Science of Heat Gelatinization

When you dip a washed cotton shirt into diluted starch water and iron it damp with a hot iron:

1. **Absorption**: Microscopic starch granules penetrate into the tiny microscopic gaps between cotton fibers.
2. **Gelatinization (Cooking)**: The heat of the hot iron cooks the damp starch grains, causing them to burst, swell, and melt into a clear, continuous, smooth film.
3. **The Dirt Shield**:
   - The starch film smooths down all fuzzy thread hairs.
   - When you walk in dusty school fields, **dust sits on top of the starch film** rather than getting trapped inside the weave!
4. **Effortless Next Wash**: On the next laundry day, dipping the shirt in water instantly dissolves the old starch film, carrying 100% of the surface dirt away with it!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Microscopic Fiber Model: Starched vs. Unstarched",
                    "type": "diagram",
                    "content": {
                        "title": "Microscopic Fiber Model: Starched vs. Unstarched Cotton Shield",
                        "description": "Comparative microscopic view of unstarched cotton fibers with deeply embedded red dust particles vs. smooth starched cotton fibers with a protective barrier layer holding dirt on the surface."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Starch Concentration Ratios & Common Errors",
                    "type": "rich_text",
                    "content": {
                        "text": """### Starch Dilution Levels & Traps to Avoid

**Myth 1**: *"The more starch you add, the better the clothes will look."*
- **Fact**: Over-starching makes fabric as stiff as wood, uncomfortable, scratchy against skin, and causes the cotton fibers to crack and tear along folded collar lines!

#### The 3 Starch Concentration Levels:
- **Light Starching (1 part starch : 6 parts water)**: Used for thin, delicate items like handkerchiefs and lightweight blouses.
- **Medium Starching (1 part starch : 3 parts water)**: The gold standard for daily school shirts, shorts, aprons, and pillowcases.
- **Heavy Starching (1 part starch : 1 part water)**: Used only for chef's hats and formal dining table napkins that must stand upright on plates!

**Myth 2**: *"You can sprinkle dry maize flour directly onto your clothes while ironing."*
- **Fact**: Dry flour will scorch into brown burnt flakes and leave messy white dust. Starch must always be extracted as liquid or boiled into a smooth paste first!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The Complete Starching Protocol",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Starch and Iron a School Uniform

Follow these 5 professional steps:

- **Step 1: Dilute the Starch**: Mix 1 cup of your potato starch paste with 3 cups of clean cold water in a wide basin until completely smooth.
- **Step 2: Dip Washed Uniform**: Submerge the clean, damp school shirt into the starch basin, ensuring all collars, cuffs, and panels are evenly soaked.
- **Step 3: Squeeze Gently**: Squeeze out excess starch water without twisting or wringing roughly.
- **Step 4: Dry in Shade Until Damp**: Hang the shirt on a plastic hanger in the shade until it is **evenly damp** (neither soaking wet nor bone dry).
- **Step 5: Iron with Hot Iron**: Iron with a moderately hot iron. The steam and heat instantly gelatinize the starch, producing a crisp, smooth, dirt-resistant finish!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Kitchen Lab Challenge: The Starch Math",
                    "type": "rich_text",
                    "content": {
                        "text": """### Solve the Starching Dilution Problem!

**The Challenge**:
Nekesa extracted 200 ml of thick potato starch paste. She wants to starch her school shirt and two pillowcases using the **Medium Starching** ratio (1 part starch to 3 parts water).

**The Calculation**:
- *Starch Paste*: $200\\text{ ml}$
- *Water Required*: $200\\text{ ml} \\times 3 = 600\\text{ ml}$ of clean cold water.
- *Total Starch Solution*: $800\\text{ ml}$ of smooth medium starch water!

**Result**:
- Her school shirt and pillowcases come out perfectly crisp, comfortable on the skin, and protected from dust for the entire week!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Homemade Starch Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why is a starched white cotton school uniform significantly easier to wash on subsequent laundry days compared to an unstarched uniform?",
                        "options": [
                            "Because starch acts as a bleach that dissolves colors",
                            "Because the smooth gelatinized starch film forms a protective surface barrier that prevents dirt from penetrating deep into the cotton fibers, allowing the dirt to wash away easily when the starch dissolves",
                            "Because starch turns cotton fabric into waterproof plastic",
                            "Because starched clothes never get dusty"
                        ],
                        "correct_index": 1,
                        "explanation": "Starching forms a smooth microscopic barrier over the cotton weave. Airborne dust and dirt sit on top of this starch layer rather than penetrating deep into the fiber cores. When washed again, the starch dissolves, taking all the surface dirt with it effortlessly."
                    }
                }
            ]
        },
        {
            "order": 4,
            "title": "Sponging, Home Dry-Cleaning & Eco-Friendly Disposal",
            "description": "Mastering the 4-step sponging procedure for structured blazers, practicing safe home dry-cleaning with open-window ventilation, and executing eco-friendly chemical waste disposal.",
            "lesson_title": "Sponging Structured Blazers, Safe Dry-Cleaning & Eco-Disposal",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Freshening Your Winter Coat & Blazer!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "dry cleaner shop",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/6/60/A_dry_cleaner_shop.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/60/A_dry_cleaner_shop.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "Dry-cleaned and sponged structured wool suits and garments hanging on hangers to preserve tailored shapes."
                    }
                },
                {
                    "page": 1,
                    "title": "When Water is the Enemy of Fabric!",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Mystery of Waterless Cleaning

Did you know that for some of our most expensive clothes, water is their greatest enemy?

- Heavy woolen school blazers, church suits, and winter coats have internal shoulder pads, canvas interfacings, and tailored seams.
- Delicate pure silk scarves and fine woolen ties lose their shape and bleed dyes when submerged in water.

How do we clean these valuable garments without a single bucket of wash water?
- We give structured blazers a precision **sponging** treatment!
- We use safe **home dry-cleaning solvents** under strict adult supervision!

And crucially, once our cleaning is done, how do we dispose of used chemical reagents to protect our garden soil and earthworms? Let's discover the science!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 4-Step Blazer Sponging Protocol",
                    "type": "diagram",
                    "content": {
                        "title": "The 4-Step Blazer Sponging Protocol Blueprint",
                        "description": "Step-by-step storyboard showing 1. Brush off dry dust downwards $\rightarrow$ 2. Wipe dirty areas with damp soapy sponge $\rightarrow$ 3. Rinse with clean damp cloth $\rightarrow$ 4. Hang on hanger in shade."
                    }
                },
                {
                    "page": 2,
                    "title": "The 4 Steps of Sponging a Blazer",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Master Sponging Protocol

Follow this exact procedure to clean a dark school blazer or heavy coat:

- **Step 1: Brush Downwards**: Hang the blazer on a hanger and use a stiff clothes brush to brush all dry dust downwards from shoulders to hem.
  - *Rule*: Never apply wet soap to dusty wool! Dry dust turns into mud, staining the jacket deeper!
- **Step 2: Wipe with Damp Soapy Sponge**: Dip a clean sponge or lint-free cloth into warm water mixed with mild detergent. **Squeeze it tightly until it is only damp (not dripping!)**. Wipe dirty zones (collar, cuffs, underarms) gently.
- **Step 3: Rinse with Clean Damp Cloth**: Dip a second clean cloth in pure warm water, wring it tightly, and wipe the blazer surface to remove all soap residues.
- **Step 4: Dry on a Hanger in Shade**: Hang the blazer on a shaped plastic or wooden hanger in a well-ventilated, shaded area to dry naturally without distortion!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Safe Home Dry-Cleaning Procedures",
                    "type": "rich_text",
                    "content": {
                        "text": """### Working with Dry Solvents Safely

Home dry-cleaning uses liquid chemical solvents (such as mineral spirits or specialized cleaning fluids) that dissolve grease instantly without water swelling the fibers.

#### Mandatory Dry-Cleaning Safety Protocols:
- **1. Direct Adult Supervision**: Never attempt dry-cleaning alone. A parent or teacher must supervise every step!
- **2. Wide-Open Windows**: Dry solvents evaporate into volatile fumes that can cause dizziness, nausea, and headaches. Always work near open windows with maximum cross-ventilation!
- **3. Protective Apparel**: Wear rubber gloves to protect skin from chemical drying and cracking.
- **4. STRICT NO-FLAME RULE**: Dry solvents are **highly flammable**! Never work near a jiko, gas cooker, fireplace, or open flame! Never heat solvents!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Dry-Cleaning Safety & Eco-Disposal Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "Home Dry-Cleaning Safety & Eco-Friendly Chemical Disposal Blueprint",
                        "description": "Safety diagram showing open-window lab setup, rubber gloves, and crossed-out flame next to eco-friendly chemical disposal (decanting into sealed waste bottles vs toxic soil dumping)."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Eco-Friendly Chemical Disposal",
                    "type": "rich_text",
                    "content": {
                        "text": """### Protecting Our Environment from Chemical Waste

When our spotting and dry-cleaning procedures are finished, we must manage our chemical waste responsibly:

#### 1. Why Chemical Dumping is Dangerous:
- Pouring used dry solvents or strong chemicals directly onto the ground causes **environmental degradation**.
- Chemicals soak into soil, killing beneficial earthworms, destroying soil fertility, and leaching into underground borehole water that your community drinks!

#### 2. The Eco-Friendly Disposal Rules:
- **Decant Dry Solvents**: Pour used dry-cleaning solvents into a clear glass jar, seal the cap tightly, label it *"WASTE CHEMICAL SOLVENT"*, and let heavy dirt settle to the bottom for reuse or safe municipal disposal.
- **Dilute Acidic Spotting Wastes**: Always dilute used lemon juice or vinegar solutions with **ten times the volume of clean water** before pouring down designated household sinks!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Dry-Cleaning a Silk Tie",
                    "type": "rich_text",
                    "content": {
                        "text": """### Safe Home Dry-Cleaning in 5 Steps

Follow these 5 steps under teacher or parent supervision:

- **Step 1: Set Up Near Open Window**: Work on a clean table directly beside an open window, far away from all kitchen stoves and flames.
- **Step 2: Wear Protective Gear**: Put on rubber gloves and a plastic apron.
- **Step 3: Pour Solvent into Glass Bowl**: Pour 100 ml of dry solvent into a heavy, stable glass or ceramic bowl (never use soft plastic or aluminum).
- **Step 4: Dip and Squeeze Gently**: Submerge the silk tie for 1 minute, squeezing gently with gloved hands without twisting or wringing.
- **Step 5: Blot and Air Dry in Shade**: Blot the tie between clean dry towels, then hang it on a hanger outdoors in a shaded, ventilated area until the solvent evaporates completely!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Eco-Auditor Challenge: The Garden Mistake",
                    "type": "rich_text",
                    "content": {
                        "text": """### Spot the Environmental Hazard!

**The Situation**:
After dry-cleaning a silk scarf, Otieno was about to empty the bowl of leftover chemical solvent into his mother's sukuma wiki (kale) vegetable garden patch behind the kitchen.

**The Diagnosis**:
- Dumping toxic, non-biodegradable solvent onto the garden will kill the earthworms, poison the soil nutrients, and contaminate the vegetables that the family eats!

**The Eco-Champion Action**:
- Pour the used solvent into a sealable glass bottle.
- Fasten the lid securely and write on the label: *"WASTE SOLVENT — DO NOT DRINK"*.
- Store in a locked chemical cupboard or take it to a designated community hazardous waste collection center!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Sponging & Eco-Care Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why is it strictly forbidden to pour leftover liquid dry-cleaning solvents directly onto garden soil or into rainwater drainage gutters?",
                        "options": [
                            "Because solvents make the grass grow too quickly",
                            "Because chemical solvents are toxic, non-biodegradable pollutants that cause severe environmental degradation, kill beneficial soil earthworms, and contaminate local groundwater and rivers",
                            "Because solvents will instantly evaporate into pure oxygen",
                            "Because drainage gutters only accept hot soapy water"
                        ],
                        "correct_index": 1,
                        "explanation": "Chemical dry solvents are non-biodegradable and hazardous; pouring them onto soil poisons soil organisms (like earthworms), degrades soil fertility, and can leach into underground aquifers or rivers, contaminating drinking water."
                    }
                }
            ]
        }
    ]

    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    for u_idx, u_data in enumerate(units_data, start=1):
        unit, _ = LearningUnit.objects.get_or_create(
            topic=topic,
            name=u_data["title"],
            defaults={
                "order": u_data["order"],
                "description": u_data["description"]
            }
        )
        unit.name = u_data["title"]
        unit.order = u_data["order"]
        unit.description = u_data["description"]
        unit.save()

        lesson, _ = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": u_data["lesson_title"],
                "status": "published"
            }
        )
        lesson.title = u_data["lesson_title"]
        lesson.status = "published"
        lesson.save()

        # Clear existing blocks
        lesson.blocks.all().delete()

        # Ingest blocks
        block_order = 1
        for p_data in u_data["pages"]:
            b = LessonBlock.objects.create(
                lesson=lesson,
                order=block_order,
                page_number=p_data["page"],
                block_type=p_data["type"],
                title=p_data["title"],
                content=p_data["content"]
            )
            block_order += 1
            total_blocks += 1
            total_pages = max(total_pages, p_data["page"])

        total_lessons += 1
        print(f"  [+] Ingested Unit {unit.order}: '{unit.name}' -> Lesson: '{lesson.title}' (8 Pages, {block_order-1} Blocks)")

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 9 Ingestion Complete!")
    print(f"[*] Total Lessons: {total_lessons}, Total Pages across lessons: {total_lessons * 8}, Total Blocks: {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_cbc_grade7_home_science_topic9()
