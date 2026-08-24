"""
VLearn Curriculum Ingestion Script
CBC Grade 7 — Home Science
Topic 8: Household Cleaning Agents & Homemade Soap (Order: 8)

Creates:
- Topic 8: Household Cleaning Agents & Homemade Soap (Order: 8)
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

def ingest_cbc_grade7_home_science_topic8():
    print("=" * 80)
    print("INGESTING CBC GRADE 7 HOME SCIENCE — TOPIC 8: HOUSEHOLD CLEANING AGENTS & HOMEMADE SOAP")
    print("=" * 80)

    # 1. Resolve Curriculum, Grade, Subject
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    assert grade, "Grade 7 not found!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject Home Science not found!"

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}")

    # 2. Create or Get Topic 8
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Household Cleaning Agents & Homemade Soap",
        defaults={
            "order": 8,
            "description": "Mastering water properties, classifying soaps and soapless detergents, understanding saponification chemistry with wood ash and fats, safe laboratory soap making, and executing a Community Service Learning (CSL) soap project."
        }
    )
    if not created:
        topic.order = 8
        topic.description = "Mastering water properties, classifying soaps and soapless detergents, understanding saponification chemistry with wood ash and fats, safe laboratory soap making, and executing a Community Service Learning (CSL) soap project."
        topic.save()
    print(f"[+] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Clean existing units and lessons under this topic for idempotent ingestion
    topic.learning_units.all().delete()
    print("[*] Cleared existing learning units and lessons under Topic 8.")

    units_data = [
        {
            "order": 1,
            "title": "Water as a Cleaning Agent & Soaps vs. Detergents",
            "description": "Evaluating water hardness (soft vs. hard water, scum formation), water temperature effects, and classifying organic soaps vs. synthetic soapless detergents.",
            "lesson_title": "Water Properties, Lathering Science & Soaps vs. Detergents",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Mystery of the Borehole Water!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "washing hands with soap lather water",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Washing_hands_%28cropped%29.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Washing_hands_%28cropped%29.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "Hands washing with soap and water to produce a rich, cleansing lather that lifts dirt away."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Does Soap Fail in Borehole Water?",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Chemistry Happening in Your Wash Basin

Imagine you are back from the school farm with hands covered in red soil. You pump a bucket of fresh borehole water, rub a bar of laundry soap vigorously, and expect thick white bubbles.

Instead, something frustrating happens:
- The soap refuses to bubble up!
- A sticky, dull grey film forms over your fingers and floats on the water.
- You have to rub three times as much soap just to get a tiny bit of lather!

Why did the soap fail?
The answer lies in **water hardness** and the chemical differences between natural soaps and modern synthetic detergents!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "Mineral Flow Diagram: Soft vs. Hard Water",
                    "type": "diagram",
                    "content": {
                        "title": "Mineral Flow Diagram: Soft vs. Hard Water Chemistry Blueprint",
                        "description": "Comparative flow diagram showing rain-fed soft water lathering freely vs. borehole hard water forming scum due to dissolved calcium and magnesium minerals."
                    }
                },
                {
                    "page": 2,
                    "title": "Hard Water vs. Soft Water Explained",
                    "type": "rich_text",
                    "content": {
                        "text": """### Understanding Water Hardness & Scum

Water is our universal cleaning solvent, but its mineral content changes its cleaning power:

- **Soft Water (e.g. Rainwater)**: Contains very few dissolved minerals. Soap dissolves effortlessly, creating instant, rich white lather that lifts dirt quickly and saves money!
- **Hard Water (e.g. Borehole & Well Water)**: Contains high amounts of dissolved **calcium and magnesium minerals** washed from underground rocks.
- **The Scum Reaction**: In hard water, soap molecules react with calcium and magnesium to form an insoluble, sticky grey curd called **scum**. Scum wastes soap, dulls white fabrics, and clogs drain pipes!

> **Smart Household Rule**: When washing white school uniforms in hard water areas, collect clean rainwater or use soapless detergent powder to prevent grey scum stains!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Soaps vs. Soapless Detergents",
                    "type": "rich_text",
                    "content": {
                        "text": """### Natural Plant Soaps vs. Synthetic Detergents

Cleaning agents are divided into two chemically distinct families:

#### 1. Natural Soaps (Fat-Based)
- **Origin**: Made from natural plant oils (coconut, palm) or animal fats mixed with alkali.
- **Toilet Soaps**: Mild, scented bars with added glycerine for personal bathing and facial care.
- **Non-Toilet Soaps**: Coarser bars and flakes for hand-washing laundry and dishes.
- **Advantages**: 100% biodegradable, environmentally friendly, and gentle on human skin.
- **Limitation**: Forms sticky scum in hard water.

#### 2. Soapless Detergents (Petroleum-Based)
- **Origin**: Synthesized from petroleum chemicals.
- **Formats**: Powders (e.g. Omo, Ariel), liquid dishwashes, and heavy cleaning pastes.
- **Advantages**: Lathers instantly in both soft and hard water with **zero scum formation**!
- **Limitation**: Can be chemically harsh on hands, drying out skin if used without gloves."""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Molecular Architecture: Soap vs. Detergent",
                    "type": "diagram",
                    "content": {
                        "title": "Molecular Architecture: Natural Soap vs. Synthetic Detergent Blueprint",
                        "description": "Split diagram showing fat-based biodegradable soap molecules next to petroleum-based synthetic detergent molecules that ignore hard water minerals."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Water Temperature & Cleaning Misconceptions",
                    "type": "rich_text",
                    "content": {
                        "text": """### Water Temperature Rules & Common Traps

**Myth 1**: *"Boiling hot water is always best for washing any stained fabric."*
- **Fact**: Boiling water permanently ruins fabrics! Heat coagulates (cooks) protein stains (like fresh blood, milk, or raw egg) into the fabric fibers, locking them in forever. Extreme heat also shrinks wool and fades bright dyes.

#### Water Temperature Guidelines:
- **Warm Water (40°C–60°C)**: Essential for washing oily sufurias and greasy collars. Thermal energy melts fats and oils so soap can wash them away.
- **Cold Water**: Essential for rinsing clothes and washing protein stains (blood, egg, milk) before they set.

**Myth 2**: *"Liquid handwash is just melted bar soap."*
- **Fact**: Most commercial liquid handwashes are liquid soapless detergents formulated with synthetic surfactants so they lather fast in any water without clogging dispenser nozzles with scum!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Testing Water Hardness at Home",
                    "type": "rich_text",
                    "content": {
                        "text": """### The 4-Step Home Science Lather Test

You can test any water source in your village with this simple experiment:

- **Step 1: Prepare Two Clean Jars**: Fill Jar A with 200 ml of rainwater (soft water) and Jar B with 200 ml of borehole water (hard water).
- **Step 2: Add Equal Soap Shavings**: Grate 1 gram of natural bar soap into each jar using a knife.
- **Step 3: Shake for 15 Seconds**: Seal both jars tightly and shake them vigorously with equal force.
- **Step 4: Observe the Results**:
  - *Jar A (Rainwater)*: Filled with thick white foam bubbles extending to the top.
  - *Jar B (Borehole)*: Very few bubbles with floating grey curd flakes (scum) on the cloudy water surface!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Home Science Inspector: The Laundry Dilemma",
                    "type": "rich_text",
                    "content": {
                        "text": """### Solve the Family Cleaning Challenge

**The Situation**:
Moraa's family lives in a rural area where all water comes from a deep limestone borehole. Her mother complains that her bar soap finishes in just three days and white school shirts are turning dull yellow-grey.

**The Diagnosis**:
- The borehole water is **hard water**, rich in dissolved calcium and magnesium.
- Every time her mother rubs bar soap, most of it turns into useless **scum** instead of cleaning bubbles.
- The sticky scum settles into the white cotton weave, turning the shirts dingy grey!

**The Solution**:
- Switch to a **soapless detergent powder** for laundry, which lathers freely in hard water without forming scum.
- Collect clean **rainwater from the roof gutters** into a drum for washing delicate clothes with gentle soap!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Water & Cleansers Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why is a synthetic soapless detergent powder preferred over a natural laundry bar soap when washing heavy school clothes in mineral-rich borehole water?",
                        "options": [
                            "Because natural bar soap is toxic to cotton fabric",
                            "Because soapless detergents do not react with dissolved calcium and magnesium minerals, lathering freely without forming sticky scum",
                            "Because borehole water can only dissolve liquid pastes",
                            "Because soapless detergents are made of vegetable oils"
                        ],
                        "correct_index": 1,
                        "explanation": "Soapless detergents are synthesized from petroleum compounds that do not react with the dissolved calcium and magnesium minerals in hard borehole water, allowing them to lather freely and clean without wasting soap or forming sticky grey scum."
                    }
                }
            ]
        },
        {
            "order": 2,
            "title": "Forms of Cleaners & Soap-Making Ingredients",
            "description": "Classifying physical cleaner formats (powder, bar, liquid, paste) and exploring the 4 natural ingredients of saponification (wood ash alkali, fats/oils, water, salt).",
            "lesson_title": "Forms of Cleaning Agents & The 4 Ingredients of Saponification",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Right Cleaner for Every Surface!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "laundry detergent powder",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Laundry_detergent_1.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Laundry_detergent_1.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "Granular laundry detergent powder and scooper illustrating physical cleaning agent formats."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Are Cleaners Sold in So Many Shapes?",
                    "type": "rich_text",
                    "content": {
                        "text": """### Exploring the Household Cleaning Shelf

Walk into your kitchen or local kiosk. You will find cleaners in four distinct physical shapes:
- Solid hard bars and cakes.
- Free-flowing granular powders.
- Smooth pouring liquids.
- Thick, concentrated green pastes.

Why don't manufacturers just make everything into one single format?
Because each format has a unique chemical concentration, dissolving speed, and surface safety profile!

Furthermore, did you know you can make your own high-quality soap using simple natural ingredients found in every village? Let's discover the science!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 4 Physical Cleaner Formats 3D Grid",
                    "type": "diagram",
                    "content": {
                        "title": "The 4 Physical Cleaner Formats 3D Grid Blueprint",
                        "description": "3D-shaded bento grid displaying granular laundry powder, viscous pouring liquid detergent, solid bar soap, and thick concentrated paste gel."
                    }
                },
                {
                    "page": 2,
                    "title": "Physical Formats & Surface Compatibility",
                    "type": "rich_text",
                    "content": {
                        "text": """### Matching Cleaner Format to the Cleaning Task

- **1. Solid Bars & Cakes**: Solid compressed blocks. Economical, durable, and slow-melting. Perfect for hand-washing clothes on a wash-bench and personal bathing.
- **2. Granular Powders**: Concentrated dry crystals that dissolve in water. High cleaning power for large volumes of laundry and scrubbing concrete floors.
- **3. Pouring Liquids**: Viscous fluids that disperse instantly in water. Gentle and smooth, ideal for washing delicate glassware, ceramic plates, and liquid handwash dispensers.
- **4. Concentrated Pastes**: Thick abrasive gels that cling to vertical and greasy surfaces. Perfect for cutting through baked-on grease and black carbon soot on cooking sufurias!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "The Chemistry of Saponification",
                    "type": "rich_text",
                    "content": {
                        "text": """### Turning Kitchen Waste into Pure Soap

Making soap is a chemical reaction called **saponification**:

$$\\text{Fats / Oils (Fatty Acids)} + \\text{Wood Ash Filtrate (Alkali Lye)} \\rightarrow \\text{Solid Soap} + \\text{Glycerine}$$

To create soap at zero cost, you only need four sustainable raw materials:

- **1. Wood Ash (The Alkali Trigger)**: Burnt hardwood ash from cooking fires contains natural potassium carbonate/hydroxide. Mixing it with water and filtering produces **clear alkali filtrate (lye)**.
- **2. Fats and Oils (The Fatty Acids)**: Leftover animal fats (beef tallow) or plant oils (coconut, used cooking oil) provide the lipid chains that form the cleaning base and moisturize skin.
- **3. Water (The Solvent)**: Dissolves the alkali minerals from the ash and enables the chemical reaction.
- **4. Salt (Sodium Chloride - The Binder)**: Added at the end of the reaction (**salting out**) to cause the solid soap to separate from the water and harden firmly into bars!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The Saponification Chemistry & Recipe Scale",
                    "type": "diagram",
                    "content": {
                        "title": "The Saponification Chemistry & Recipe Scale Blueprint",
                        "description": "Vector diagram illustrating the chemical roles and proportions of wood ash alkali, fats/oils, water solvent, and salt solidifier in homemade soap production."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Ingredient Myths & Workshop Precautions",
                    "type": "rich_text",
                    "content": {
                        "text": """### Separating Soap-Making Myths from Facts

**Myth 1**: *"Wood ash filtrate is just dirty water and will make your clothes grey and muddy."*
- **Fact**: When wood ash settles, the solid grey ash sinks to the bottom. The clear filtered liquid on top is a pure chemical alkali solution (potassium hydroxide). It reacts completely with fat to create pure, white-lathering soap with zero ash residue!

**Myth 2**: *"You can use dry powder detergent directly on your hands to scrub off tough engine oil."*
- **Fact**: Never rub concentrated dry powder directly on your bare skin! The high alkalinity and concentrated surfactants will strip natural protective oils and cause chemical burning. Always dissolve cleaners in water first."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Preparing Wood Ash Filtrate",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Extract Natural Alkali Lye from Kitchen Ash

Follow these 4 scientific steps to prepare your natural alkali:

- **Step 1: Collect Hardwood Ash**: Collect 1 kg of clean, white wood ash from a charcoal jiko or firewood hearth (avoid plastic or painted wood ash).
- **Step 2: Mix with Warm Water**: Place the ash in a clean plastic bucket and stir in 3 liters of warm water.
- **Step 3: Let it Settle**: Allow the mixture to sit undisturbed for **24 to 48 hours**. The heavy grey charcoal particles will settle to the bottom.
- **Step 4: Filter Through Cloth**: Pour the top liquid carefully through a clean cotton cloth or sieve into a separate plastic container. The resulting clear, slippery liquid is your natural **alkali filtrate (lye)**!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Workshop Challenge: Sourcing Ingredients for Free",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Sustainable School Soap Project

**The Challenge**:
Mr. Omondi's Grade 7 class wants to make 30 bars of soap for the school handwashing stations, but the school club has a budget of zero shillings!

**How the Students Sourced Everything for Free**:
- **Alkali**: Collected clean hardwood ash from the school kitchen firewood hearth $\rightarrow$ **Cost: KES 0**
- **Fats**: Sourced clean leftover animal fat trimmings from the local village butcher $\rightarrow$ **Cost: KES 0**
- **Water**: Collected fresh rainwater from the science lab roof gutter $\rightarrow$ **Cost: KES 0**
- **Binder**: Brought a small cup of coarse table salt from home $\rightarrow$ **Cost: KES 0**

**Result**: The students produced 30 solid, rich-lathering soap bars with **100% sustainable local resources**!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Saponification Ingredients Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "What is the specific chemical function of table salt (sodium chloride) when added to the warm mixture of wood ash filtrate and fat during soap making?",
                        "options": [
                            "It acts as a perfume to give the soap a lemon scent",
                            "It acts as a precipitating binder that causes the solid soap molecules to separate from the excess water and harden firmly",
                            "It provides the strong alkali needed to dissolve the fat",
                            "It turns the soap transparent like glass"
                        ],
                        "correct_index": 1,
                        "explanation": "Salt (sodium chloride) is used in the 'salting out' phase of saponification. It increases the ionic strength of the solution, causing the solid soap curds to separate from the water/glycerine liquid and solidify into firm blocks."
                    }
                }
            ]
        },
        {
            "order": 3,
            "title": "Safe Lab Preparation, Saponification & Soap Additives",
            "description": "Mastering the 6-step cold soap-making procedure, mandatory laboratory safety gear, the 4-week curing process, and enriching soap with neem antiseptics and glycerine.",
            "lesson_title": "Safe Cold Soap-Making, 4-Week Curing & Premium Additives",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "From Raw Chemistry to Premium Artisan Soap!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "handmade soap bars herbal natural",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Handmade_soap.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Handmade_soap.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "Handmade natural soap bars cured in wooden molds and infused with herbal extracts."
                    }
                },
                {
                    "page": 1,
                    "title": "Kitchen Chemistry with Laboratory Safety!",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Thrill of Soap Making

Have you ever created something with your own hands that cleans, smells wonderful, and protects your family from disease?

Making soap is an exciting scientific craft, but it involves powerful chemical reactions:
- Raw wood ash filtrate is **caustic (corrosive)** and can cause chemical skin burns if splashed on bare hands!
- Mixing hot lye with oil requires the right containers, strict safety gear, and calm, steady hands.

Today, we put on our safety gear, learn the 6-step cold soap-making protocol, and discover how natural additives like neem extract turn plain soap into a premium antiseptic product!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 6-Step Safe Cold Soap-Making Storyboard",
                    "type": "diagram",
                    "content": {
                        "title": "The 6-Step Safe Cold Soap-Making Storyboard",
                        "description": "6-step laboratory sequence showing safety gear, filtering ash lye, warming oil, stirring to trace, salting out, and pouring into molds to cure for 4 weeks."
                    }
                },
                {
                    "page": 2,
                    "title": "The 6 Steps of Cold Soap Making",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Master Cold Method Protocol

Follow this exact sequence in your Home Science laboratory:

- **Step 1: Safety Gear First**: Put on rubber gloves, a plastic apron, and safety goggles before handling any ingredients.
- **Step 2: Filter Ash Lye**: Filter settled wood ash water through cotton cloth into a clean plastic container.
- **Step 3: Warm the Fats**: Gently warm your animal fat or vegetable oil in a plastic basin until completely melted.
- **Step 4: Slow Mixing to 'Trace'**: Slowly pour the clear alkali filtrate into the warm fat while stirring continuously in **one direction** with a wooden stick until the mixture thickens like porridge (this is called the **trace state**).
- **Step 5: Salt Out & Add Enhancers**: Stir in a small handful of salt, then add optional fragrances (lavender), natural dyes, or antiseptic extracts (neem).
- **Step 6: Mold & Cure**: Pour into paper-lined wooden molds, allow to harden for 48 hours, slice into bars, and **cure for 2 to 4 weeks** in a dry, ventilated room!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Mandatory Safety Rules & The Curing Period",
                    "type": "rich_text",
                    "content": {
                        "text": """### Critical Safety Protocols & Chemical Curing

#### 1. The 'No Aluminum' Rule
- **Never use aluminum pots or spoons for soap making!**
- Alkali lye reacts violently with aluminum metal, corroding the pot, producing hazardous flammable hydrogen gas, and ruining the soap.
- **Only use**: Thick plastic, heavy glass, or wooden utensils.

#### 2. The 2 to 4 Week Curing Period
- Why can't you wash your face with freshly molded homemade soap?
- **Fresh soap contains active, unreacted caustic alkali** that will cause painful skin burns and irritation.
- During the **2 to 4 week curing period**, saponification completes 100%, neutralizing all active alkali and allowing excess water to evaporate, creating a mild, rock-hard, long-lasting bar!

#### 3. First Aid for Chemical Splashes
- If alkali filtrate splashes onto skin or eyes, **flush immediately with abundant cold running water for 15 minutes**! Keep mild vinegar nearby to neutralize alkali spills on tables."""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The Soap Improvement & Quality Benchmarks",
                    "type": "diagram",
                    "content": {
                        "title": "The Soap Improvement & Quality Benchmarks Blueprint",
                        "description": "Infographic showing how basic grey soap is enhanced with neem antiseptics, glycerine moisturizers, and fragrances, matched to the 4-Star Quality Benchmarks."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Soap Additives & Quality Benchmarks",
                    "type": "rich_text",
                    "content": {
                        "text": """### Turning Basic Soap into a Premium Product

Basic soap made from fat and ash can look dull grey and smell like cooking grease. We improve it using four natural additives:

- **1. Antiseptics (e.g. Neem / Mwarobaini Extract)**: Squeezing juice from fresh neem leaves into the trace mixture adds powerful antibacterial properties that heal rashes and fight skin germs.
- **2. Glycerine (Humectant)**: Retains moisture on the skin, preventing dryness and keeping hands velvety soft.
- **3. Fragrances (Essential Oils)**: Adding lemon grass or lavender oil masks animal fat odors and provides a clean, invigorating scent.
- **4. Natural Dyes**: Adding beetroot juice (pink) or turmeric (yellow) creates visually attractive, commercial-grade bars.

#### The 4 Qualities of an Effective Cleaner:
- **Gentle on Skin**: Balanced pH with zero burning or dryness.
- **Lathers Easily**: Produces rich foam to trap and suspend dirt.
- **Fresh Fragrance**: Leaves articles and skin smelling clean.
- **Safe on Surfaces**: Cleans without corroding fabrics or scratching glass."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Making Neem Antiseptic Soap",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Create Organic Medicated Soap

Upgrade your homemade soap with this herbal formulation:

- **Step 1: Prepare Neem Extract**: Crush 200g of fresh green neem (*mwarobaini*) leaves in a mortar, add 50 ml of warm water, and strain the deep green juice through a fine sieve.
- **Step 2: Reach Trace State**: Stir warm coconut oil and wood ash filtrate until the mixture thickens like honey.
- **Step 3: Stir in Additives**: Pour in the green neem juice, 1 tablespoon of glycerine, and 10 drops of lemon grass essential oil. Stir vigorously for 2 minutes.
- **Step 4: Pour and Cure**: Pour the fragrant green mixture into recycled milk carton molds, let set for 2 days, cut into 100g bars, and cure on wooden slats for 4 weeks!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Workshop Quality Audit: The Impatient Student",
                    "type": "rich_text",
                    "content": {
                        "text": """### Spot the Dangerous Workshop Mistake!

**The Situation**:
Kiprono was so excited after pouring his homemade soap into molds that the very next morning (after only 12 hours), he took a piece to the bathroom and washed his face with it. 

Immediately, his facial skin began to sting, turn bright red, and burn painfully.

**The Diagnosis**:
- Kiprono failed to follow the **mandatory 2 to 4 week curing rule**!
- After only 12 hours, the soap was raw and filled with active, unreacted **caustic alkali (potassium hydroxide)**.
- The strong alkali reacted chemically with his facial skin, causing an alkali chemical burn.

**The Correct Action**:
- Flush Kiprono's face immediately with clean running water for 15 minutes.
- Store all soap batches on high, ventilated shelves labeled: *"CURING IN PROGRESS — DO NOT USE UNTIL [DATE]"*."""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Soap Safety & Additives Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why is it strictly forbidden to use aluminum cooking pots or aluminum spoons when preparing homemade soap with wood ash alkali filtrate?",
                        "options": [
                            "Because aluminum makes the soap smell like burnt charcoal",
                            "Because alkali lye chemically reacts with aluminum, corroding the pot, generating hazardous flammable hydrogen gas, and ruining the soap",
                            "Because aluminum makes the soap lather too much",
                            "Because aluminum cools down the fat too quickly"
                        ],
                        "correct_index": 1,
                        "explanation": "Alkali lye solutions (potassium or sodium hydroxide) react vigorously with aluminum metal, causing severe corrosion, producing hazardous flammable hydrogen gas, and contaminating the soap. Only inert materials like plastic, glass, or wood should be used."
                    }
                }
            ]
        },
        {
            "order": 4,
            "title": "Community Service Learning (CSL) Soap Project",
            "description": "Planning, executing, showcasing, and evaluating a 5-phase Community Service Learning (CSL) soap-making and public health hygiene campaign.",
            "lesson_title": "The JSS Community Soap Project: Health, Sanitation & Enterprise",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Power of Clean Hands in the Community!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "students washing hands school hygiene",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Wash_and_sanitize_hands_to_prevent_spread_-_DPLA_-_860bcec48f19b03b1e1fc7bfa67c4f9e.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Wash_and_sanitize_hands_to_prevent_spread_-_DPLA_-_860bcec48f19b03b1e1fc7bfa67c4f9e.jpg",
                        "author": "DPLA / Public Domain",
                        "licensing": "Public Domain",
                        "caption": "A public health campaign banner promoting handwashing with soap to prevent disease spread in schools and communities."
                    }
                },
                {
                    "page": 1,
                    "title": "Transforming Science into Community Action!",
                    "type": "rich_text",
                    "content": {
                        "text": """### Beyond the Classroom: Saving Lives with Soap

Did you know that washing hands with soap and clean water is the single most effective way to prevent diarrheal illnesses and respiratory infections in our communities?

In many public schools and village markets, handwashing stations sit empty because commercial soap is too expensive to buy every week.

Through our **Community Service Learning (CSL) Project**, Grade 7 learners step up as public health champions!
- You will work in teams to plan, budget, and make healthy antiseptic soap for zero cost.
- You will install soap at school wash taps and teach younger students how to wash hands properly.
- You will discover how science can create micro-enterprise opportunities!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 5-Phase CSL Soap Project Cycle",
                    "type": "diagram",
                    "content": {
                        "title": "The 5-Phase CSL Soap Project Cycle Infographic",
                        "description": "Circular 5-phase project management loop mapping out Investigate, Plan & Budget, Execute Production, Sensitize & Showcase, and Evaluate & Reflect."
                    }
                },
                {
                    "page": 2,
                    "title": "The 5 Phases of a Successful CSL Project",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Manage Your Community Soap Campaign

A successful CSL project follows five structured project management phases:

- **1. Investigate (Research)**: Survey the school and village to identify hygiene challenges (e.g. lack of soap at school latrines) and locate free, sustainable raw materials (ash and cooking fat).
- **2. Plan & Budget**: Hold group meetings, assign leadership roles, create a written action plan, establish a production timeline, and draft a zero-cost budget.
- **3. Execute (Production & Curing)**: Collect natural ingredients, safely manufacture batches of improved neem soap, let them cure for 4 weeks, and wrap them in clean paper.
- **4. Sensitize & Showcase (Public Health)**: Distribute soap to school handwashing stations and organize a school assembly or poster campaign teaching proper handwashing steps.
- **5. Evaluate (Feedback & Reflection)**: Distribute simple feedback surveys to teachers and students, analyze what worked well, and document recommendations for next term!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Why Handwashing with Soap Saves Lives",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Biological Weapon Against Pathogens

Why is washing with plain water not enough?

- Viruses and bacteria are coated in a protective fatty outer membrane (lipid bilayer) that clings tightly to the natural oils on human skin.
- Water alone cannot dissolve this oil—it just flows right over the germs.
- **The Soap Superpower**: Soap molecules have a dual nature:
  - *Hydrophilic head* (water-loving).
  - *Hydrophobic tail* (oil-loving).
- When you lather for 20 seconds, the soap tails pierce and rupture the bacteria's fatty membrane, destroying the germ, while the heads latch onto running water to flush the destroyed debris down the drain!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Zero-Cost Community Resource Flow Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "Zero-Cost Community Resource Flow Blueprint",
                        "description": "Visual flow diagram showing how waste wood ash from school kitchens and leftover cooking fat are transformed into healthy school soap bars."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "CSL Project Misconceptions & Enterprise Insights",
                    "type": "rich_text",
                    "content": {
                        "text": """### Understanding the True Meaning of CSL

**Myth 1**: *"A CSL project is just an ordinary practical exam marked inside the classroom."*
- **Fact**: A practical exam only tests personal technical skill. A CSL project requires teamwork, community problem-solving, public health education, and gathering real user feedback!

**Myth 2**: *"Soap making cannot be a real business because anyone can make it."*
- **Fact**: High-quality, attractively packaged neem and lavender herbal soaps sell for premium prices in urban shops and farmer's markets! Soap making is an excellent micro-enterprise that fosters youth self-reliance and financial literacy."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The 6-Step Handwashing Protocol",
                    "type": "rich_text",
                    "content": {
                        "text": """### Teaching the Community Proper Handwashing

Demonstrate these 6 steps during your CSL sensitization campaign:

- **Step 1: Wet Hands**: Wet hands with clean running water and apply enough soap to cover all surfaces.
- **Step 2: Palm to Palm**: Rub hands palm to palm to generate rich foam.
- **Step 3: Interlace Fingers**: Rub the back of each hand with the opposite palm, interlacing fingers.
- **Step 4: Clean Thumbs & Nails**: Rotational rubbing of left thumb clasped in right palm and vice versa. Rub fingertips in circular motions on palms.
- **Step 5: Wash for 20 Seconds**: Scrub continuously for at least **20 seconds** (the time it takes to sing the 'Happy Birthday' song twice).
- **Step 6: Rinse and Dry**: Rinse thoroughly under running water and air dry or pat with a clean single-use towel!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "CSL Evaluation Challenge: Analyzing Community Feedback",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Project Review Meeting

**The Survey Results**:
Group 3 distributed 40 bars of lemon-scented homemade soap across 8 school handwashing stations and gathered 50 survey responses:

- **Positive Feedback (92%)**: Students loved the rich lather and fresh lemon scent. Cases of stomach aches reported to the school dispensary dropped by 40%!
- **Constructive Feedback (8%)**: Two teachers noted that the soap bars melted quickly in water puddles on the wash sink.

**The Group's Next-Term Action Plan**:
- Design and construct **slotted wooden soap dishes** from upcycled timber scraps so the soap drains freely and stays dry between uses!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "CSL Soap Project Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "In the 5-phase Community Service Learning (CSL) soap project, what is the primary objective of the 'Evaluate (Reflection)' phase?",
                        "options": [
                            "To grade which student worked the fastest with scissors",
                            "To collect feedback from users, evaluate project achievements and challenges, and formulate recommendations for future health improvements",
                            "To sell remaining soap at double price to tourists",
                            "To destroy leftover wood ash"
                        ],
                        "correct_index": 1,
                        "explanation": "The 'Evaluate (Reflection)' phase allows learners to gather community feedback, analyze the real-world impact and effectiveness of their soap, identify challenges, and document recommendations to improve future community service initiatives."
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
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 8 Ingestion Complete!")
    print(f"[*] Total Lessons: {total_lessons}, Total Pages across lessons: {total_lessons * 8}, Total Blocks: {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_cbc_grade7_home_science_topic8()
