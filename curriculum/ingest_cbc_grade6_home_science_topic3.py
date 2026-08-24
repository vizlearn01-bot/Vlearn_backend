"""
VLearn Curriculum Ingestion Script
CBC Grade 6 — Home Science
Topic 3: Foods and Nutrition (Order: 3)
Module 3: Foods and Nutrition (Strand 3.0 / Topics 3.1 to 3.8)

Creates:
- Topic 3: Foods and Nutrition (Order: 3) under CBC -> Grade 6 -> Home Science
- 4 Learning Units
- 4 Published Lessons (32 Pages, 8 per lesson)
- 40 LessonBlocks (10 per lesson)
- Upper Primary (Grade 6) appropriate domestic science, zero bracket citations, proper '- ' markdown lists.
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

def ingest_cbc_grade6_home_science_topic3():
    print("=" * 80)
    print("INGESTING CBC GRADE 6 HOME SCIENCE — TOPIC 3: FOODS AND NUTRITION")
    print("=" * 80)

    # 1. Resolve Hierarchy
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    assert grade, "Grade 6 not found!"
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Home Science", defaults={"description": "CBC Grade 6 Home Science Curriculum"})

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}")

    # 2. Create or Get Topic 3 (Foods and Nutrition)
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Foods and Nutrition",
        defaults={
            "order": 3,
            "description": "Equipping Grade 6 learners with core food literacy, understanding iron and iodine minerals, identifying nutritional deficiency disorders, mastering food preservation for meats, fruits, and vegetables, caring for household cookers, planning balanced family meals, and executing practical stewing and rubbed-in baking cookery."
        }
    )
    if not created:
        topic.order = 3
        topic.description = "Equipping Grade 6 learners with core food literacy, understanding iron and iodine minerals, identifying nutritional deficiency disorders, mastering food preservation for meats, fruits, and vegetables, caring for household cookers, planning balanced family meals, and executing practical stewing and rubbed-in baking cookery."
        topic.save()
    print(f"[+] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Clear existing units and lessons under this topic for idempotent ingestion
    topic.learning_units.all().delete()
    print("[*] Cleared existing learning units and lessons under Grade 6 Topic 3.")

    units_data = [
        {
            "order": 1,
            "title": "Essential Minerals & Deficiency Disorders",
            "description": "Discovering the biological importance of Iron and Iodine, identifying local plant and animal food sources, and diagnosing/preventing five major nutritional deficiency disorders.",
            "lesson_title": "Essential Minerals and Deficiency Disorders",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Tiny Trucks in Your Blood!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "healthy fresh food fruits vegetables fish meat",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg",
                        "author": "National Cancer Institute / Wikimedia Commons",
                        "licensing": "Public Domain",
                        "caption": "An abundant display of fresh fruits, vegetables, grains, and proteins that supply our bodies with vital minerals and nutrients."
                    }
                },
                {
                    "page": 1,
                    "title": "The Silent Engine Fuels of Your Body",
                    "type": "rich_text",
                    "content": {
                        "text": """### What Powers Your Physical Strength?

Have you ever sprinted across the school field during physical education games and felt your heart thumping and your breath racing?
- Inside your blood, a tiny fleet of microscopic delivery trucks called **haemoglobin** is speeding through your blood vessels!
- These trucks load up fresh oxygen from your lungs and deliver it straight to your brain, heart, and leg muscles so you have energy to sprint and study!

What raw material builds these oxygen trucks?
- The mineral **Iron**!

And what tells your brain how to think sharply and your neck gland to control body growth?
- The mineral **Iodine**!

Today, we discover the superhero minerals in our local Kenyan foods and learn how balanced eating protects us from dangerous deficiency diseases!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "Local Food Mineral Map: Iron & Iodine Sources",
                    "type": "diagram",
                    "content": {
                        "title": "Local Food Mineral Map: Iron & Iodine Sources Blueprint",
                        "description": "Split comparative infographic showing Iron sources (spinach, liver, lentils, pumpkin seeds) on the left and Iodine sources (iodized salt with KEBS logo, eggs, milk, fish) on the right."
                    }
                },
                {
                    "page": 2,
                    "title": "The Two Superhero Minerals",
                    "type": "rich_text",
                    "content": {
                        "text": """### Iron vs. Iodine: Functions & Sources

**Minerals** are natural protective elements found in foods that our bodies need in small amounts (called micronutrients) to develop properly:

- **1. Iron (Oxygen Carrier & Muscle Energy)**:
  - *Function*: Builds haemoglobin in red blood cells to transport oxygen throughout the body. Essential for adolescent girls to replace iron lost during menstruation.
  - *Local Sources*: Dark green leafy vegetables (sukuma wiki, spinach, terere), beef liver, red kidney beans, lentils, and roasted pumpkin seeds.
- **2. Iodine (Brain Sharpness & Thyroid Health)**:
  - *Function*: Fuels the thyroid gland (in your neck) to produce hormones that regulate growth and mental alertness.
  - *Local Sources*: Packaged iodized salt (with the official KEBS seal of quality), fresh sea and lake fish (tilapia, omena), eggs, and dairy milk."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "5 Major Nutritional Deficiency Disorders",
                    "type": "rich_text",
                    "content": {
                        "text": """### What Happens When Nutrients are Missing?

When a person consistently fails to eat a varied, balanced diet, the body suffers from nutritional disorders:

- **1. Nutritional Anaemia**:
  - *Cause*: Severe lack of Iron.
  - *Signs*: Extreme fatigue, dizziness, pale pink under-eyelids, and pale fingernails.
- **2. Goitre**:
  - *Cause*: Severe lack of Iodine.
  - *Signs*: Swelling or lump in the front part of the neck (enlarged thyroid gland).
- **3. Constipation**:
  - *Cause*: Lack of dietary fibre (whole grains/vegetables) and insufficient clean drinking water.
  - *Signs*: Hard, painful, and irregular bowel movements.
- **4. Kwashiorkor (Protein Deficiency)**:
  - *Cause*: Severe lack of body-building proteins.
  - *Signs*: Swollen face, hands, and belly (edema), thin reddish-brown hair, and weak muscles.
- **5. Marasmus (Total Energy Starvation)**:
  - *Cause*: Severe lack of all food groups (starvation).
  - *Signs*: Extreme muscle wasting, loose wrinkled skin, visible rib cage, and an elderly facial appearance."""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "5 Major Nutritional Deficiency Disorders Matrix",
                    "type": "diagram",
                    "content": {
                        "title": "5 Major Nutritional Deficiency Disorders Matrix",
                        "description": "5-panel diagnostic visual guide illustrating pale gums/eyelids (anaemia), neck swelling (goitre), hard stools/water drops (constipation), swollen belly (kwashiorkor), and ribbed frame (marasmus)."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Nutrition Myths vs. Biological Facts",
                    "type": "rich_text",
                    "content": {
                        "text": """### Common Dietary Misconceptions

**Myth 1**: *"Kwashiorkor only happens to families who cannot afford expensive beef or chicken."*
- **Fact**: Kwashiorkor is caused by a lack of protein awareness, not just money! Families can easily prevent and cure it using very cheap local plant proteins like yellow beans, green grams (ndengu), lentils, and groundnuts!

**Myth 2**: *"To get enough minerals, you must buy expensive vitamin and mineral pills from the chemist."*
- **Fact**: The human body absorbs minerals best when they come naturally from real food! Eating sukuma wiki, beans, eggs, and seasoned food with iodized salt provides all the minerals you need safely and cheaply!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Designing a Mineral-Packed Meal",
                    "type": "rich_text",
                    "content": {
                        "text": """### The 4-Step Nutrient Booster Protocol

Follow these 4 simple steps when helping prepare family meals:

- **Step 1: Choose an Iron Core**: Select cooked beef liver, red kidney beans, or stewed green grams.
- **Step 2: Add Dark Green Leaves**: Sauté a generous portion of spinach, terere, or kales.
- **Step 3: Add Vitamin C for Absorption**: Squeeze a wedge of fresh lemon juice over the cooked greens (Vitamin C multiplies iron absorption in the stomach!).
- **Step 4: Use Iodized Salt**: Always verify that your cooking salt packaging has the "Iodized Salt" label and KEBS quality mark!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Doctor's Clinic: Diagnosing Baby Baraka",
                    "type": "rich_text",
                    "content": {
                        "text": """### Clinical Case Study!

**The Situation**:
Baby Baraka is 2 years old. For the past six months, he has been fed only plain maize porridge and sweetened tea. His mother notices that his cheeks and belly are swollen, and his hair has turned a light rusty brown color.

**The Diagnosis**:
- Baby Baraka is suffering from **Kwashiorkor** caused by a severe lack of protein in his daily porridge!

**The Dietary Prescription**:
- Introduce mashed boiled eggs, cooked yellow beans, mashed avocado, and fresh dairy milk into his daily porridge to restore his protein levels and clear the swelling!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Minerals & Deficiencies Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "An adolescent student in Grade 6 feels constantly dizzy, unusually tired in class, and exhibits pale eyelids. What mineral should she increase in her diet?",
                        "options": [
                            "Iodine, by consuming more table salt",
                            "Iron, by eating foods like dark green spinach, beef liver, and beans",
                            "Calcium, by drinking more fizzy soda",
                            "Fibre, by eating white sugar candies"
                        ],
                        "correct_index": 1,
                        "explanation": "Dizziness, fatigue, and pale eyelids are classic signs of nutritional anaemia caused by iron deficiency. Eating iron-rich foods (spinach, liver, beans) restores haemoglobin levels and oxygen transport in the blood."
                    }
                }
            ]
        },
        {
            "order": 2,
            "title": "Food Preservation in the Home",
            "description": "Understanding food spoilage mechanisms, mastering 4 home meat preservation methods (refrigeration, sun drying, salting, smoking), and practicing hygienic fruit and vegetable drying on raised racks.",
            "lesson_title": "Food Preservation in the Home",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Stopping the Bacterial Spoilers!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "sun dried fish market food preservation",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Sun-dried_shark_minnows_and_snakehead_fish_in_Battambang.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Sun-dried_shark_minnows_and_snakehead_fish_in_Battambang.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "Fresh fish preserved by sun drying, an effective traditional moisture-removal method that prevents bacterial spoilage."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Does Fresh Food Spoil?",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Battle Against Food Decay

Imagine leaving a piece of fresh raw beef and a freshly sliced mango on a warm kitchen table uncovered for three days:
- What happens?
- The meat turns slimy, changes color to grey-green, and smells foul!
- The mango becomes soft, mouldy, and starts to rot!

Why?
- Microscopic bacteria and fungi thrive on the moisture and nutrients in fresh food!

**Food Preservation** is the science and art of treating food to slow down or completely stop the growth of microorganisms so that food stays safe, edible, and nutritious for weeks or months!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "4 Household Meat Preservation Methods",
                    "type": "diagram",
                    "content": {
                        "title": "4 Household Meat Preservation Methods Comparison Grid",
                        "description": "Comparative 4-quadrant chart detailing Refrigeration (cold slows bacteria), Sun Drying (dry heat dehydrates), Salting/Brining (sponge pulls water), and Smoking (warm smoke protective coat)."
                    }
                },
                {
                    "page": 2,
                    "title": "4 Methods of Preserving Meat at Home",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Keep Meat Fresh Without Waste

Because meat has high moisture and rich proteins, it is **highly perishable**. Here are the 4 household preservation methods:

- **1. Refrigeration & Freezing**:
  - *Principle*: Low temperatures put bacteria to sleep (slow down their multiplication).
  - *Trade-off*: Requires reliable electricity; does not kill bacteria permanently.
- **2. Sun Drying**:
  - *Principle*: Cutting meat into thin strips and using hot sun to evaporate all water. Bacteria cannot survive without moisture.
  - *Trade-off*: Free and natural; requires hot, sunny weather.
- **3. Salting (Dry Rub & Wet Brine)**:
  - *Principle*: Salt draws water out of meat cells and dehydrates bacteria to destroy them.
  - *Caution*: Unsuitable for family members with **high blood pressure (hypertension)**.
- **4. Smoking**:
  - *Principle*: Hanging meat strips over a controlled smoky wood fire. Warm smoke coats meat with protective chemical compounds and gives rich flavor."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Preserving Fruits and Vegetables Hygenically",
                    "type": "rich_text",
                    "content": {
                        "text": """### Saving Seasonal Garden Harvests

During rainy seasons, kitchen gardens produce massive surpluses of kales (sukuma wiki), traditional cowpea leaves (kunde), and sweet mangoes:

#### Why We Must Sun-Dry Crops:
- If not preserved, excess harvest rots in the garden, causing massive financial and food loss.
- Dried vegetables and fruits provide continuous nutrition during the dry, expensive months!

#### The 3 Golden Rules of Hygienic Fruit & Vegetable Drying:
- **1. Raised Food Drying Rack (1 Meter High)**: Always construct a wooden rack raised off the ground to keep food away from dust, mud, chickens, and crawling pests!
- **2. Clean Muslin Cloth or Wire Mesh Cover**: Cover the drying food to allow sun heat and breeze through while blocking flies and birds!
- **3. Airtight Glass Jar Storage**: Once completely dry and crispy, pack the produce into clean, airtight containers stored in a cool, dry place!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Raised Food Drying Rack & Muslin Cover Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "Hygienic Raised Food Drying Rack & Muslin Cover Blueprint",
                        "description": "Illustrated blueprint of a 1-meter raised wooden vegetable drying rack covered with a protective white muslin cloth, showing sunlight evaporation and pest exclusion."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Food Preservation Myths & Traps",
                    "type": "rich_text",
                    "content": {
                        "text": """### Preservation Traps to Avoid

**Myth 1**: *"Drying sliced vegetables directly on a bare mat on the ground is fine as long as the sun is hot."*
- **Fact**: Ground drying is dangerous! Wind blows dusty soil onto the food, while chickens, dogs, and insects walk over the food, contaminating it with disease-causing germs. Always use a raised rack!

**Myth 2**: *"Refrigerating meat kills all the bacteria inside."*
- **Fact**: Cold temperatures do not kill bacteria; they only pause their activity! If the power goes off and meat warms up, bacteria multiply quickly and spoil the meat."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The Vegetable Sun-Drying Protocol",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Sun-Dry Traditional Greens

Follow these 4 simple steps to preserve kales or indigenous greens:

- **Step 1: Wash & Inspect**: Wash freshly harvested leaves thoroughly in clean running water to remove garden dirt.
- **Step 2: Shred into Uniform Strips**: Slice leaves into thin, even ribbons so they dry evenly at the same speed.
- **Step 3: Spread on Raised Rack**: Spread the sliced greens thinly on a clean, raised rack covered with clean muslin cloth under bright sun.
- **Step 4: Pack in Airtight Jars**: When leaves are completely dry and crumble easily between fingers, seal them in clean, dry airtight jars!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Harvest Rescue: Saving Auma's Mangoes",
                    "type": "rich_text",
                    "content": {
                        "text": """### Practical Home Science Problem Solving!

**The Situation**:
Auma's family harvested three large sacks of ripe mangoes from their orchard. They can only eat half a sack before the rest turn overripe and rot.

**The Solution**:
- Peel and slice the ripe mangoes into thin, uniform strips.
- Place them on a clean, raised wooden drying rack covered with protective muslin cloth in direct sunlight for 3–4 days.
- Pack the chewy, dried mango slices into airtight containers. Auma's family now has delicious, nutritious fruit snacks that will last for six months!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Food Preservation Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why is it mandatory to place sliced vegetables on a raised rack covered with muslin cloth rather than drying them directly on the bare ground?",
                        "options": [
                            "To prevent the sun from making the vegetables too dry",
                            "To protect the food from ground dust, animal droppings, and insect contamination while allowing sun and air to dry it safely",
                            "To make the vegetables change color to purple",
                            "Because wood attracts bacteria away from the vegetables"
                        ],
                        "correct_index": 1,
                        "explanation": "Drying on a raised rack (1m high) covered with clean muslin cloth ensures strict hygiene by blocking ground dirt, domestic animal droppings, and flies while permitting solar heat and air currents to dehydrate the food safely."
                    }
                }
            ]
        },
        {
            "order": 3,
            "title": "Stoves, Kitchen Safety & Family Meal Planning",
            "description": "Identifying and maintaining 5 common cookers, creating improvised kitchen scrubbers, practicing safety, and applying the 7 key factors of balanced family meal planning.",
            "lesson_title": "Stoves, Kitchen Safety and Family Meal Planning",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Secrets of a Well-Managed Kitchen!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "food cooking on charcoal stove jiko",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Food_cooking_on_charcoal_stove.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Food_cooking_on_charcoal_stove.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "A traditional charcoal stove in active use, illustrating the daily care and fuel management required in household cooking."
                    }
                },
                {
                    "page": 1,
                    "title": "The Mystery of the Sooty Sufuria",
                    "type": "rich_text",
                    "content": {
                        "text": """### Stoves Have Personalities!

Have you ever helped prepare evening tea on a paraffin stove and noticed thick black smoke billowing out, turning the bottom of your shiny aluminium sufuria black with stubborn soot?
- Why did that happen?
- Because the paraffin stove's cotton wicks were dirty, uneven, or untrimmed!

In our homes, we rely on different types of cookers to feed our families:
- Charcoal Jikos
- Gas Cookers (LPG)
- Paraffin Stoves
- Electric Cookers
- Traditional Firewood Stoves

When stoves are kept clean, they burn efficiently with clean flames, save fuel money, and keep our lungs healthy! Today, we learn how to care for stoves and plan balanced family meals!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "Household Cookers Maintenance & Danger Zones",
                    "type": "diagram",
                    "content": {
                        "title": "Household Cookers Maintenance & Danger Zones Guide",
                        "description": "Infographic detailing the primary cleaning zones and safety protocols for Charcoal Jikos, Gas Cookers, Paraffin Stoves, and Electric Cookers."
                    }
                },
                {
                    "page": 2,
                    "title": "Daily Stove Care & Improvised Scrubbers",
                    "type": "rich_text",
                    "content": {
                        "text": """### Keeping Kitchen Cookers Clean & Safe

Each stove has specific cleaning requirements:

- **1. Charcoal Jiko**:
  - *Daily Care*: Empty cold grey ash from the ash door daily to maintain steady oxygen airflow. Wipe the metal frame clean.
- **2. Gas Cooker (LPG)**:
  - *Daily Care*: Wipe burners after cooking; use a fine wire pin to clear clogged gas nozzles for a clean blue flame.
- **3. Paraffin Stove**:
  - *Daily Care*: Trim cotton wicks straight and level to prevent toxic black soot; wipe off any spilled kerosene immediately.
- **4. Electric Cooker**:
  - *Daily Care*: Let hotplates cool completely before wiping with a damp cloth; NEVER immerse hotplates in water.

---

### Upcycling & Improvised Scrubbers
You don't need expensive store-bought steel wool to clean soot!
- **Maize Cob & Wood Ash**: Dip a dry, fibrous maize cob into fine kitchen wood ash (a natural abrasive soap) to scrub soot off metal sufurias until they shine!
- **Coconut Husks & Sisal Fibres**: Excellent natural scrubbing pads for clay and aluminium pots."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "The 7 Factors of Family Meal Planning",
                    "type": "rich_text",
                    "content": {
                        "text": """### Planning Nutritious Meals for the Family

**Meal Planning** is the process of deciding in advance what a family will eat for breakfast, lunch, and supper:

#### The 7 Essential Factors to Balance:
- **1. Money (Budget)**: How much can the household afford to spend on groceries?
- **2. Available Fuel**: What cooking fuel (gas, charcoal, firewood) is available, and how much does it cost?
- **3. Time**: How much time is available to prepare and cook the food?
- **4. Number of People**: How many family members are eating, and what are their portion sizes?
- **5. Special Dietary Needs**: Are there babies (needing soft foods), teenagers (needing iron and protein), or elders?
- **6. Variety**: Are we combining different food textures, colors, and flavors?
- **7. Seasonal Local Availability**: Using fresh local indigenous foods (like amaranth, beans, sweet potatoes) that are currently in season is much cheaper and highly nutritious!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The Family Meal Planner's Decision Wheel",
                    "type": "diagram",
                    "content": {
                        "title": "The Family Meal Planner's Decision Wheel Blueprint",
                        "description": "Circular decision wheel showing a centered family meal plate connected to the 6 radiating planning branches: Budget, Fuel, Time, Family Size, Nutrients, and Local Seasonality."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Meal Planning Myths vs. Facts",
                    "type": "rich_text",
                    "content": {
                        "text": """### Meal Planning Misconceptions

**Myth 1**: *"A meal is only nutritious and prestigious if it contains expensive imported canned meat."*
- **Fact**: Local traditional foods like kunde (cowpea leaves), yellow beans, brown ugali, and omena are fresher, cheaper, and packed with superior proteins, iron, and minerals than expensive processed canned foods!

**Myth 2**: *"Cooking with all burners on high heat is the fastest way to save fuel."*
- **Fact**: High heat burns food and boils away moisture. Simmering under moderate heat with tightly covered lids retains steam and saves significant cooking fuel!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Assembling an Improvised Scrubber",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Make a Maize Cob & Ash Scrubber

Follow these 4 simple steps:

- **Step 1: Collect Dry Materials**: Pick a clean, dry maize cob or a bundle of dry sisal fibres from your garden.
- **Step 2: Sift Clean Wood Ash**: Collect fine, cold wood ash from the fireplace and sift out any sharp charcoal chunks.
- **Step 3: Wet & Dip**: Dip the end of the maize cob in water, then press it into the fine wood ash to form an abrasive cleaning paste.
- **Step 4: Scrub & Rinse**: Scrub the blackened bottom of your sufuria firmly in circular motions, then rinse with clean water to reveal a sparkling shine!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Kitchen Challenge: Planning on a 300/- Budget",
                    "type": "rich_text",
                    "content": {
                        "text": """### Help Mutua Feed 6 Family Members!

**The Challenge**:
Mutua has **300 shillings** and one charcoal jiko to prepare supper for 6 family members.

**Menu A (Expensive & Unbalanced)**:
- 1/2 kg Beef (320/-) + Cooking Oil (80/-) = **400 KES** (Over budget, no vegetables or starch!).

**Menu B (Smart, Balanced & Budget-Friendly)**:
- 1/2 kg Yellow Beans (80/-) + Sukuma Wiki (30/-) + 1 kg Maize Flour (90/-) + Tomatoes & Onions (40/-) = **240 KES**!
- *Leftover Change*: 60 shillings saved for morning bread!
- *Result*: A hot, delicious, iron-packed supper prepared in a single stewing pot, saving charcoal fuel!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Stoves & Meal Planning Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why should cotton wicks in a paraffin stove be regularly trimmed straight and level across the top?",
                        "options": [
                            "To make the flame turn bright yellow and smoky",
                            "To ensure even paraffin combustion with a clean blue flame and stop toxic black soot from forming",
                            "To use up the kerosene faster",
                            "To make the metal chimney rattle loudly"
                        ],
                        "correct_index": 1,
                        "explanation": "Trimming paraffin stove wicks flat and level ensures clean, efficient combustion of kerosene, producing a steady blue flame and preventing toxic black smoke and soot from staining cookware and lungs."
                    }
                }
            ]
        },
        {
            "order": 4,
            "title": "Practical Cookery: Stewing & Baking",
            "description": "Mastering the science and technique of slow moist-heat stewing in clay pots, understanding convection currents, and executing rubbed-in baking using an improvised dual-sufuria hot-sand jiko oven.",
            "lesson_title": "Practical Cookery: Stewing and Baking",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Magic of Slow Simmering & Golden Baking!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "freshly baked homemade cake food cookery",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Homemade_butter_cake.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Homemade_butter_cake.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "A golden-brown homemade butter cake demonstrating successful execution of the rubbed-in baking method."
                    }
                },
                {
                    "page": 1,
                    "title": "From Raw Ingredients to Culinary Masterpieces",
                    "type": "rich_text",
                    "content": {
                        "text": """### Two World-Class Cooking Methods!

Have you ever tasted a bowl of green banana and beef stew so tender that the meat effortlessly melted in your mouth, bathed in rich, flavorful gravy?
- That is the art of **Stewing**!

Or have you enjoyed the aroma of a warm, crumbly cake fresh out of the oven with a golden crust?
- That is the magic of **Baking**!

You don't need fancy, expensive electrical appliances to achieve these culinary masterpieces. Today, we discover:
- How **convection currents** tenderize food inside traditional clay pots (nyungu).
- How to bake delicious cakes using the **rubbed-in method** and an improvised **dual-sufuria hot-sand jiko oven**!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "Clay Pot Stewing Convection Current Model",
                    "type": "diagram",
                    "content": {
                        "title": "Clay Pot Stewing Convection Current & Heat Simmer Model",
                        "description": "Cross-sectional blueprint of a covered clay pot on a jiko showing rising hot liquid arrows, sinking cool liquid arrows, trapped steam recycling, and gentle low-heat simmer bubbles."
                    }
                },
                {
                    "page": 2,
                    "title": "The Science of Stewing Cookery",
                    "type": "rich_text",
                    "content": {
                        "text": """### Slow Moist-Heat Simmering

**Stewing** is a slow, moist-heat cooking method where food is cut into uniform pieces and cooked gently in a small amount of liquid inside a tightly covered pot over low heat:

- **1. Why It Tenderizes Tough Cuts**:
  - Gentle, slow heat breaks down tough muscle fibers in meat and softens starch in green bananas (matoke).
- **2. Maximum Nutrient Conservation**:
  - The cooking liquid is never thrown away! All the water-soluble vitamins and minerals dissolve into the rich gravy and are eaten as part of the meal.
- **3. Convection Heat Currents**:
  - Heat from the bottom warms the gravy, which expands and rises. Cooler gravy at the surface sinks, creating a continuous circulating loop (convection current) that cooks the food evenly.
- **4. Traditional Clay Pots (Nyungu)**:
  - Clay pots retain heat exceptionally well, allowing food to simmer gently for hours using very little charcoal!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Baking: The Rubbed-In Method & Improvised Ovens",
                    "type": "rich_text",
                    "content": {
                        "text": """### Baking Cakes Without Electricity

**Baking** is the method of cooking food using dry, circulating hot air:

#### The Rubbed-In Method (Fingertip Magic!):
- Cold margarine or butter is rubbed into dry flour using **only your cool fingertips** (lifting the flour high above the bowl to let cool air circulate).
- Squeezing with warm palms melts the fat, making the cake oily and heavy. Fingertip rubbing wraps fat around starch grains until the mixture looks like **fine breadcrumbs**!

---

### The Dual-Sufuria Hot-Sand Jiko Oven
If your home does not have an electric oven, you can build a brilliant improvised oven using local equipment:
- **Base**: Place a large outer sufuria with a 2cm layer of clean, dry river sand on a lit charcoal jiko.
- **Middle**: Place your greased cake tin containing the batter onto the hot sand bed.
- **Top**: Cover the large sufuria with a flat metal lid and place **glowing red charcoal embers** on top of the lid.
- **How It Works**: Hot sand bakes the cake from below, while glowing embers bake it golden-brown from above!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The Dual-Sufuria Improvised Hot-Sand Oven",
                    "type": "diagram",
                    "content": {
                        "title": "The Dual-Sufuria Improvised Hot-Sand Jiko Oven Blueprint",
                        "description": "Cross-sectional engineering diagram showing a charcoal jiko, large outer sufuria with hot river sand, cake tin with batter, and top lid holding glowing red embers for dual-directional baking."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Culinary Myths vs. Kitchen Realities",
                    "type": "rich_text",
                    "content": {
                        "text": """### Kitchen Myths Debunked

**Myth 1**: *"The best way to stew food quickly is to keep the pot at a roaring, violent boil without a lid."*
- **Fact**: Violent boiling toughens meat fibers, boils away nutrient-rich steam, and dries out the stew! Stewing must be done under a tight lid at a quiet, gentle simmer.

**Myth 2**: *"You must use warm melted butter when mixing flour for a rubbed-in cake."*
- **Fact**: Melted butter turns flour into a sticky, greasy dough. The rubbed-in method strictly requires cold, firm fat rubbed with cool fingertips to achieve light, crumbly breadcrumbs!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Baking a Simple Rubbed-In Cake",
                    "type": "rich_text",
                    "content": {
                        "text": """### The 6-Step Cake Baking Formula

Follow these 6 precise steps:

- **Step 1: Measure & Sift**: Sift 200g flour and 1 teaspoon baking powder into a clean mixing bowl.
- **Step 2: Fingertip Rubbing-In**: Rub 100g cold margarine into the flour using cool fingertips until it resembles fine breadcrumbs.
- **Step 3: Stir in Sugar**: Add 100g sugar and mix evenly with a wooden spoon.
- **Step 4: Add Wet Ingredients**: Beat 2 eggs with 4 tablespoons of milk, pour into the bowl, and mix gently into a smooth, thick batter.
- **Step 5: Load Sand Oven**: Pour batter into a greased tin and place onto the preheated sand bed inside your dual-sufuria jiko oven.
- **Step 6: Bake & Test**: Cover with the ember-loaded lid and bake for 35–40 minutes until a clean toothpick inserted in the center comes out completely dry!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Master Chef: The Green Banana Stew Challenge",
                    "type": "rich_text",
                    "content": {
                        "text": """### Practical Cookery Execution!

**The Situation**:
Naliaka is preparing stewed matoke (green bananas) and beef for her family. She puts the pot on the jiko, removes the lid, and cranks the air gate wide open, creating roaring flames.

**The Critique**:
- Removing the lid allows all the steam and vitamin-rich moisture to evaporate, while high roaring heat will scorch the bottom and make the beef tough!

**The Correction**:
- Naliaka should cover the pot tightly with a well-fitting lid, close the jiko air gate halfway to lower the heat to a gentle simmer, and let the convection currents tenderize the beef and bananas slowly!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Practical Cookery Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why is cold fat rubbed into flour using only the fingertips (and never warm palms) during the rubbed-in cake baking method?",
                        "options": [
                            "To prevent the fat from melting, ensuring cool air is trapped to create light, crumbly breadcrumbs",
                            "To make the cake batter turn blue",
                            "Because fingertips are stronger than palms",
                            "To prevent flour from sticking to the bowl"
                        ],
                        "correct_index": 0,
                        "explanation": "Fingertips are the coolest part of the hand. Rubbing with fingertips and lifting the mixture traps cool air and prevents the margarine from melting into an oily paste, ensuring a light, tender, and crumbly baked cake."
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
    print(f"[SUCCESS] CBC Grade 6 Home Science Topic 3 Ingestion Complete!")
    print(f"[*] Total Lessons: {total_lessons}, Total Pages across lessons: {total_lessons * 8}, Total Blocks: {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_cbc_grade6_home_science_topic3()
