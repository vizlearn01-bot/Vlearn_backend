"""
VLearn Curriculum Ingestion Script
CBC Grade 6 — Home Science
Topic 1: Adolescence (Order: 1)

Creates:
- Topic 1: Adolescence (Order: 1) under CBC -> Grade 6 -> Home Science
- 4 Learning Units
- 4 Published Lessons (32 Pages, 8 per lesson)
- 40 LessonBlocks (10 per lesson)
- Upper Primary (Grade 6) appropriate language, zero bracket citations, proper '- ' markdown lists.
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

def ingest_cbc_grade6_home_science_topic1():
    print("=" * 80)
    print("INGESTING CBC GRADE 6 HOME SCIENCE — TOPIC 1: ADOLESCENCE")
    print("=" * 80)

    # 1. Resolve Curriculum, Grade, Subject
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    if not grade:
        grade = Grade.objects.create(curriculum=curriculum, name="Grade 6", level=6, description="CBC Grade 6 (Upper Primary)")
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Home Science", defaults={"description": "CBC Grade 6 Home Science Curriculum"})

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}")

    # 2. Create or Get Topic 1
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Adolescence",
        defaults={
            "order": 1,
            "description": "Understanding the physical, emotional, and social transitions of puberty, practicing daily personal grooming and menstrual hygiene, eating balanced iron-rich meals, engaging in daily exercise, and staying safe in physical and digital environments."
        }
    )
    if not created:
        topic.order = 1
        topic.description = "Understanding the physical, emotional, and social transitions of puberty, practicing daily personal grooming and menstrual hygiene, eating balanced iron-rich meals, engaging in daily exercise, and staying safe in physical and digital environments."
        topic.save()
    print(f"[+] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Clear existing units and lessons under this topic for idempotent ingestion
    topic.learning_units.all().delete()
    print("[*] Cleared existing learning units and lessons under Grade 6 Topic 1.")

    units_data = [
        {
            "order": 1,
            "title": "Meaning of Adolescence & Puberty Changes",
            "description": "Discovering adolescence as the bridge between childhood and adulthood, identifying physical changes in boys and girls, and understanding emotional and social growth.",
            "lesson_title": "The Story of Adolescence: Physical, Emotional & Social Changes",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Shrinking Uniform Mystery!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "school uniform kenya",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/3/32/AHS_Uniform.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/32/AHS_Uniform.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "A classic school uniform blazer and shirt symbolizing the rapid growth and transition during adolescent school years."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Is My Uniform Getting Shorter?",
                    "type": "rich_text",
                    "content": {
                        "text": """### Welcome to the Bridge of Growth!

Have you noticed something surprising when getting ready for school recently?
- That school uniform shirt that fit you loosely last year suddenly feels tight across your shoulders!
- Your school skirt or trousers look shorter, showing your ankles!
- Your voice sounds a bit different, or your skin is getting a little more oily!

Did your clothes shrink in the wash?
**No, your clothes didn't shrink at all—YOU are growing taller and stronger!**

You are entering a wonderful, exciting stage called **adolescence**. In this lesson, we discover the natural physical, emotional, and social changes that happen as we grow from children into teenagers!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The Puberty Changes Classification Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "The Puberty Changes Classification Blueprint",
                        "description": "Comparative anatomical chart showing physical puberty changes unique to boys, unique to girls, and shared by both."
                    }
                },
                {
                    "page": 2,
                    "title": "What Happens During Puberty?",
                    "type": "rich_text",
                    "content": {
                        "text": """### Natural Physical Transformations

**Adolescence** is the natural bridge of rapid growth between childhood and adulthood (usually between ages 13 and 19). A person in this stage is called a **teenager**.

During **puberty**, your body experiences specific physical changes:

- **Changes in Boys**:
  - Voice "breaks" and becomes deeper.
  - Shoulders broaden and chest widens.
  - Facial hair begins to grow on the chin and upper lip (beards and mustache).
  - May experience wet dreams during sleep.
- **Changes in Girls**:
  - Hips broaden and become rounder.
  - Breasts develop.
  - The voice becomes melodious.
  - Monthly **menstruation cycle** begins.
- **Shared Changes (Both Boys & Girls)**:
  - Rapid growth spurt in height and body size.
  - Hair grows under armpits and in pubic areas.
  - Sweat glands become more active, producing more sweat.
  - Skin produces more oil, sometimes causing acne (pimples)."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Emotional & Social Changes in Adolescents",
                    "type": "rich_text",
                    "content": {
                        "text": """### Feelings and Friendships Are Growing Too!

Growth is not just about getting taller on the outside. Inside your mind and heart, two other major changes take place:

#### 1. Emotional Changes (Your Feelings)
- You may experience **mood swings**—feeling joyful and energetic one moment, and quiet, thoughtful, or sensitive the next.
- You begin to value personal privacy.
- You develop a strong desire to explore who you are and build personal self-confidence!

#### 2. Social Changes (Your Relationships)
- You enjoy spending more time with classmates and peer groups.
- You take on more leadership responsibilities at school and home (like helping younger siblings or caring for pets).
- You learn how to communicate respectfully with parents, teachers, and peers!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Physical, Emotional & Social Growth Matrix",
                    "type": "diagram",
                    "content": {
                        "title": "Physical, Emotional & Social Growth Matrix",
                        "description": "Three-pillar matrix diagram mapping Physical (visible body), Emotional (feelings & self-identity), and Social (peers & family responsibility) changes."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Puberty Myths vs. Biological Facts",
                    "type": "rich_text",
                    "content": {
                        "text": """### Truths Every Grade 6 Learner Should Know

**Myth 1**: *"If my voice has not broken yet, but my friend's voice has, something is wrong with my body."*
- **Fact**: Every person has their own unique biological growth clock! Some boys and girls start their growth spurt early at age 11 or 12, while others start at 14 or 15. Both timelines are completely normal and healthy!

**Myth 2**: *"Acne (pimples) on the face is a disease caused by eating ripe bananas or mangoes."*
- **Fact**: Acne is not a disease! During puberty, sweat and oil glands in the skin become super-active. Washing your face daily with clean water and mild soap removes excess oil and keeps your skin clean and healthy!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The Adolescent Self-Care Routine",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Care for Your Changing Body Every Day

Follow these 4 healthy daily habits:

- **Step 1: Wash Your Face Twice Daily**: Wash gently with clean water and mild soap in the morning and evening to keep skin pores clean and prevent pimples.
- **Step 2: Practice Daily Full-Body Bathing**: Take a warm bath with soap every day, paying special attention to your underarms and neck.
- **Step 3: Wear Clean Undergarments**: Always change your undergarments and socks daily to prevent sweat buildup.
- **Step 4: Talk to a Trusted Adult**: If you feel confused, worried, or have questions about body changes, speak to your parent, guardian, or Home Science teacher!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Home Science Challenge: Supporting a Friend",
                    "type": "rich_text",
                    "content": {
                        "text": """### Help Wanjiku Build Confidence!

**The Situation**:
Wanjiku noticed small pimples on her forehead this week. She felt shy, covered her face with her sweater, and refused to play netball with her classmates during break time because she thought she had a contagious illness.

**The Explanation**:
- Wanjiku's skin oil glands are simply waking up as part of normal puberty growth. She is not sick, and acne is never contagious!

**The Advice to Give Wanjiku**:
- Reassure her that pimples are a normal sign of growing up that almost all teenagers experience.
- Encourage her to wash her face gently twice daily with clean water and mild soap.
- Invite her back to the netball court—active play and exercise actually improve skin blood flow and mood!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Adolescence Changes Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Which of the following physical changes during puberty is experienced by BOTH boys and girls?",
                        "options": [
                            "Voice breaking and growing facial beards",
                            "Broadening of the hips and breast development",
                            "Increased sweating, underarm hair growth, and developing acne (pimples)",
                            "Beginning of the monthly menstruation cycle"
                        ],
                        "correct_index": 2,
                        "explanation": "During puberty, both boys and girls experience active sweat glands, hair growth under the armpits, and increased skin oil production leading to acne. Voice deepening is unique to boys, while breast development and menstruation are unique to girls."
                    }
                }
            ]
        },
        {
            "order": 2,
            "title": "Good Grooming & Personal Hygiene Habits",
            "description": "Mastering daily bathing routines, underarm hair care, neat hair maintenance, clean clothes, and proper menstrual hygiene with safe sanitary towel disposal.",
            "lesson_title": "Daily Grooming, Menstrual Hygiene & Personal Care",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Clean, Fresh & Ready for the Day!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "hand washing soap hygiene",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Use_of_a_touchless_hand_washing_tap_and_solid_bar_soap_dispenser.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Use_of_a_touchless_hand_washing_tap_and_solid_bar_soap_dispenser.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "Washing hands thoroughly with soap and running water to maintain pristine personal hygiene and health."
                    }
                },
                {
                    "page": 1,
                    "title": "The Power of Great Personal Grooming",
                    "type": "rich_text",
                    "content": {
                        "text": """### Looking Neat, Smelling Fresh!

Imagine walking into class on a warm morning:
- One student took a refreshing bath, put on clean socks, combed their hair, and wears a clean, well-ironed uniform.
- Another student woke up late, skipped their bath, sprayed heavy perfume over stale sweat, and wore yesterday's dirty socks.

Who feels more confident, cheerful, and comfortable throughout the school day?

**Good grooming** is the daily practice of keeping your body, hair, teeth, and clothes clean and neat. Let's master the essential grooming habits that protect our health and dignity!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "4-Step Daily Personal Grooming Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "4-Step Daily Personal Grooming Storyboard Blueprint",
                        "description": "Illustrated storyboard showing 1. Bathing daily with soap $\rightarrow$ 2. Underarm care & neat hair $\rightarrow$ 3. Menstrual hygiene $\rightarrow$ 4. Wearing clean, decent clothes."
                    }
                },
                {
                    "page": 2,
                    "title": "The Pillars of Daily Personal Hygiene",
                    "type": "rich_text",
                    "content": {
                        "text": """### Core Hygiene Routines for Adolescents

Because sweat and oil glands work extra hard during puberty, daily hygiene is essential:

- **1. Daily Full-Body Bathing**:
  - Bathing with clean water and mild soap every day removes sweat, dead skin cells, and surface bacteria.
- **2. Underarm Care & Body Odor Prevention**:
  - Shaving or trimming underarm hair prevents sweat and bacteria from getting trapped, which is the main cause of body odor!
- **3. Hair & Oral Hygiene**:
  - Keep hair clean, combed, shaved, or neatly braided. Brush your teeth twice daily (morning and before bedtime).
- **4. Foot Hygiene**:
  - Wash between your toes, dry thoroughly, and always wear clean cotton socks to prevent fungal infections (like athlete's foot)."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Menstrual Hygiene Management (MHM)",
                    "type": "rich_text",
                    "content": {
                        "text": """### Safe, Dignified Menstrual Self-Care

For adolescent girls, the start of menstruation is a natural sign of healthy reproductive development. Practicing proper menstrual hygiene keeps girls comfortable, confident, and active in school:

#### The 5 Golden Rules of Menstrual Hygiene:
- **1. Wash Hands Before and After**: Always wash your hands with clean water and soap before touching or placing a clean sanitary towel.
- **2. Change Regularly**: Change your sanitary pad every **4 to 6 hours** (or more often on heavy flow days) to prevent bacterial growth and stay fresh.
- **3. Wear Comfortable Cotton Undergarments**: Clean, breathable cotton underwear holds the pad securely and prevents chafing.
- **4. Wrap Securely for Disposal**: After removing a used pad, fold it neatly, wrap it securely in old newspaper or clean waste paper.
- **5. THE BIN RULE (NO FLUSHING!)**: Throw wrapped pads into a sanitary disposal bin or pit latrine. **NEVER flush pads down a flush toilet**—they will block sewer pipes!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Menstrual Hygiene & Safe Waste Disposal Flowchart",
                    "type": "diagram",
                    "content": {
                        "title": "Menstrual Hygiene & Safe Waste Disposal Flowchart",
                        "description": "5-step flowchart showing 1. Wash hands $\rightarrow$ 2. Secure clean pad $\rightarrow$ 3. Change every 4-6 hours $\rightarrow$ 4. Wrap in waste paper $\rightarrow$ 5. Place in sanitary bin (No toilet flush)."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Grooming Myths & Hygiene Traps",
                    "type": "rich_text",
                    "content": {
                        "text": """### Common Hygiene Traps to Avoid

**Myth 1**: *"Spraying strong perfume or body spray over your clothes can replace taking a bath."*
- **Fact**: Deodorant or perfume only masks smell temporarily. When sprayed over stale sweat and bacteria, it creates a much worse, unpleasant odor! Nothing can replace washing with soap and clean water.

**Myth 2**: *"Girls should stay home from school and rest in bed during their monthly period."*
- **Fact**: Menstruation is a completely normal biological process. With proper sanitary towels, good hygiene, and a balanced diet, girls can attend classes, study, and participate in everyday school activities with full confidence!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The Morning Grooming Checklist",
                    "type": "rich_text",
                    "content": {
                        "text": """### Your 5-Minute Morning Success Checklist

Follow these 5 steps every morning before school:

- **Step 1: Take a Refreshing Bath**: Wash your entire body with clean water and soap, lathering underarms, feet, and neck.
- **Step 2: Dry Thoroughly**: Use a clean, dry personal towel to dry yourself completely, especially between toes and under arms.
- **Step 3: Apply Gentle Skin Lotion**: Rub a small amount of petroleum jelly or body lotion to keep skin soft and prevent dryness.
- **Step 4: Neaten Your Hair & Brush Teeth**: Brush teeth for two minutes with fluoride toothpaste and comb or brush your hair neatly.
- **Step 5: Put on Clean, Decent Uniform**: Wear clean underwear, fresh socks, and a neatly pressed school uniform!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Hygiene Hero: Solving the Sports Day Dilemma",
                    "type": "rich_text",
                    "content": {
                        "text": """### Practical Decision Making!

**The Situation**:
After an energetic physical education (PE) football match in the hot sun, Brian was soaked in sweat. His friend told him: *"Just put on your blazer and spray your body spray, we need to hurry to math class!"*

**The Problem**:
- Leaving sweat on the skin causes bacteria to multiply rapidly, producing strong body odor and soaking sweat into the school blazer!

**The Proper Action**:
- Brian should wipe off sweat with a clean small towel, wash his face and hands at the school tap, change out of his sweaty PE shirt into his clean uniform shirt, and air his PE kit to dry!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Grooming & Hygiene Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "What is the correct, environmentally safe procedure for disposing of a used sanitary towel after changing?",
                        "options": [
                            "Flush it down a modern flush toilet to make it disappear quickly",
                            "Fold the used pad, wrap it securely in clean waste paper or newspaper, and dispose of it in a designated sanitary bin or pit latrine",
                            "Throw it open into the school flower garden",
                            "Leave it on the bathroom window sill"
                        ],
                        "correct_index": 1,
                        "explanation": "Sanitary pads should always be folded, wrapped tightly in paper, and placed in a sanitary waste bin or pit latrine. Flushing pads down flush toilets causes severe pipe blockages, while leaving them exposed is unhygienic and spreads germs."
                    }
                }
            ]
        },
        {
            "order": 3,
            "title": "Adolescent Nutrition & Iron for Energy",
            "description": "Understanding nutritional needs during growth spurts, balancing the 3 food groups, the vital role of iron in preventing anemia, and choosing healthy local snacks.",
            "lesson_title": "Adolescent Nutrition: Balanced Diet, Iron Power & Healthy Snacks",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Feeding Your Fast-Growing Body!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "healthy balanced meal dinner",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/NCI_Visuals_Food_Meal_Dinner.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/NCI_Visuals_Food_Meal_Dinner.jpg",
                        "author": "National Cancer Institute / Wikimedia Commons",
                        "licensing": "Public Domain",
                        "caption": "A colorful balanced meal plate combining fresh vegetables, energy grains, and lean proteins for optimal adolescent health."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Food is Your Body's Super-Fuel",
                    "type": "rich_text",
                    "content": {
                        "text": """### Fueling Your Growth Engine!

Think of your body during adolescence as a high-speed sports car being assembled and upgraded:
- Your bones are stretching longer every month.
- Your muscles are getting stronger.
- Your brain is solving complex math and science puzzles every day at school!

What kind of fuel does a fast-growing sports car need?
- Premium, high-quality fuel!

If you feed your body only sugary sodas, oily crisps, and candy:
- You feel sluggish, tired in morning lessons, and lack energy for play!

Today, we discover the **Balanced Adolescent Plate** and the superhero mineral called **Iron**!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The Adolescent Balanced Plate & Iron Power",
                    "type": "diagram",
                    "content": {
                        "title": "The Adolescent Balanced Plate & Iron Power Blueprint",
                        "description": "Divided plate showing 1/2 protective vegetables & fruits, 1/4 carbohydrates, 1/4 body-building proteins, clean water, and highlighted iron sources."
                    }
                },
                {
                    "page": 2,
                    "title": "The 3 Food Groups for Adolescents",
                    "type": "rich_text",
                    "content": {
                        "text": """### Building a Balanced Daily Diet

A healthy adolescent meal combines all three essential food groups:

- **1. Energy-Giving Foods (Carbohydrates & Healthy Fats)**:
  - *Examples*: Brown rice, whole maize ugali, sweet potatoes, arrowroots (nduma), and oats.
  - *Purpose*: Provides sustained energy for studying, walking to school, and playing sports.
- **2. Body-Building Foods (Proteins)**:
  - *Examples*: Beans, lentils, green grams (ndengu), eggs, milk, fish, chicken, and beef.
  - *Purpose*: Builds strong muscles, repairs tissues, and supports rapid growth spurts.
- **3. Protective Foods (Vitamins & Minerals)**:
  - *Examples*: Sukuma wiki (kales), spinach, managu, carrots, oranges, mangoes, and papayas.
  - *Purpose*: Boosts the immune system to fight infections and keeps eyes and skin glowing!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "The Super-Mineral: Why Iron Matters Most",
                    "type": "rich_text",
                    "content": {
                        "text": """### Understanding Iron & Anemia Prevention

**Iron** is a vital mineral that helps your red blood cells carry oxygen from your lungs to your brain and muscles:

#### Why Adolescents Need Extra Iron:
- **For Girls**: Monthly menstrual blood loss removes iron from the body. Eating iron-rich foods replaces this lost iron and prevents **iron-deficiency anemia** (which causes severe dizziness, pale palms, weakness, and poor concentration).
- **For Boys**: Rapid growth of muscle mass and blood volume requires high amounts of iron.

#### Top Local Iron-Rich Foods:
- Dark green leafy vegetables (spinach, terere, managu, stinging nettle).
- Beef liver and organ meats.
- Legumes (red kidney beans, lentils, chickpeas).
- Eggs and roasted groundnuts."""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Healthy Snacks vs. Junk Food Comparison",
                    "type": "diagram",
                    "content": {
                        "title": "Healthy Adolescent Snacks vs. Unhealthy Junk Food Comparison Matrix",
                        "description": "Comparison chart contrasting nutrient-rich local snacks (boiled maize, groundnuts, fruit) with processed junk foods (deep-fried crisps, fizzy sodas, sweets)."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Adolescent Nutrition Myths & Facts",
                    "type": "rich_text",
                    "content": {
                        "text": """### Nutrition Myths Debunked

**Myth 1**: *"Skipping breakfast helps you stay slim and fit."*
- **Fact**: Skipping breakfast starves your brain of morning glucose, making you feel weak, dizzy, and unable to pay attention in class. It often causes intense hunger later, leading to overeating unhealthy junk snacks!

**Myth 2**: *"Packaged potato crisps and fizzy sodas give you fast energy for sports."*
- **Fact**: Sodas and sweets cause a rapid 'sugar spike' followed by an immediate energy crash, leaving you feeling exhausted and dehydrated. Fresh fruit and boiled water give long-lasting energy!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Choosing Smart School Snacks",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Smart Snacking Protocol

When choosing break-time snacks at school or home, follow these 4 smart steps:

- **Step 1: Choose Whole, Natural Foods**: Pick a sweet banana, roasted groundnuts, boiled maize, or a boiled egg.
- **Step 2: Avoid High-Sugar Sodas**: Drink clean, safe boiled water or fresh homemade fruit juice instead of packaged sodas.
- **Step 3: Watch the Salt & Oil**: Avoid deep-fried, heavily salted snacks (like fried mandazis or packaged potato crisps).
- **Step 4: Eat at Regular Times**: Eat 3 balanced meals daily plus 1 or 2 healthy light snacks to keep your energy steady!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Nutrition Lab: Fixing Achieng's Diet",
                    "type": "rich_text",
                    "content": {
                        "text": """### Help Achieng Beat Afternoon Fatigue!

**The Situation**:
Achieng often feels dizzy and sleepy during afternoon English lessons. Her daily routine: skips breakfast, buys a bottle of sugary soda and a packet of potato crisps for lunch, and drinks no water.

**The Diagnosis**:
- Achieng's body is suffering from low iron and dehydration. Sugary soda and oily crisps provide no proteins, iron, or vitamins!

**The Meal Plan Upgrade**:
- **Breakfast**: A cup of hot milk with a boiled sweet potato or boiled egg.
- **Lunch**: Rice or ugali with stewed beans and dark green spinach (rich in iron).
- **Hydration**: A refillable bottle of clean boiled drinking water!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Adolescent Nutrition Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why are adolescent girls specifically encouraged to eat plenty of iron-rich foods such as spinach, beans, and liver?",
                        "options": [
                            "To make their hair grow curly",
                            "To replace the iron lost in blood during their monthly menstrual periods and prevent iron-deficiency anemia",
                            "Because iron turns carbohydrates into water",
                            "To reduce the amount of sleep they need"
                        ],
                        "correct_index": 1,
                        "explanation": "Adolescent girls lose blood and iron during menstruation. Eating iron-rich foods (like liver, spinach, and beans) replenishes body iron stores, supporting red blood cell formation and preventing tiredness, weakness, and anemia."
                    }
                }
            ]
        },
        {
            "order": 4,
            "title": "Physical Exercise, Environmental & Digital Safety",
            "description": "Understanding the physical and mental benefits of daily active exercise, identifying physical environmental hazards, and practicing safe digital behavior online.",
            "lesson_title": "Daily Exercise Fitness, Environmental Hazards & Digital Safety",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Active, Strong & Staying Safe!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "children skipping rope exercise",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Ghanaian_kid_%28skipping_rope%29_05.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Ghanaian_kid_%28skipping_rope%29_05.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "A young learner energetically skipping rope outdoors, showcasing active physical exercise for cardiovascular health and strong bones."
                    }
                },
                {
                    "page": 1,
                    "title": "Moving Your Body & Protecting Yourself",
                    "type": "rich_text",
                    "content": {
                        "text": """### Strong Bodies, Alert Minds!

Have you ever noticed how great you feel after playing an energetic game of chase, skipping rope, or football with friends during break time?
- Your heart pumps briskly, your cheeks are warm, and your mind feels alert and happy!

At the same time, as you grow older and spend more time outside or exploring phones and tablets, the world opens up:
- You walk to school independently.
- You explore new neighborhoods and use digital educational apps.

How do we build a strong, active body while keeping ourselves safe from physical, social, and online dangers? Let's discover the rules of an **Active & Safe Adolescent**!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "Daily Physical Exercise & Mental Mood Boost",
                    "type": "diagram",
                    "content": {
                        "title": "Daily Physical Exercise & Mental Mood Boost Model",
                        "description": "Comparative diagram illustrating the benefits of daily active exercise (bone density, heart fitness, happy mood, sound sleep) vs sedentary inactivity."
                    }
                },
                {
                    "page": 2,
                    "title": "Why Daily Exercise is Essential",
                    "type": "rich_text",
                    "content": {
                        "text": """### 4 Big Benefits of Daily Active Movement

Engaging in at least **30 to 60 minutes** of physical activity daily transforms your health:

- **1. Strengthens Bones & Muscles**:
  - Running, jumping, and skipping rope place healthy stress on growing bones, building high bone density and strong muscles.
- **2. Boosts Heart & Lung Health**:
  - Aerobic exercise trains your heart pump to deliver oxygen efficiently throughout your body.
- **3. Maintains Healthy Body Weight**:
  - Physical play burns off excess calories from food, protecting against childhood obesity.
- **4. Lifts Mood & Reduces Stress**:
  - Exercise releases natural body chemicals called endorphins that relieve school stress, improve mood, and help you sleep peacefully!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Physical Environmental Safety Rules",
                    "type": "rich_text",
                    "content": {
                        "text": """### Staying Safe in Your Community

As you travel to school and explore your neighborhood, follow these vital safety rules:

#### 1. Avoid Dangerous Places
- Never play near unfenced deep water dams, quarries, construction sites, or railway tracks.
- Always swim only in designated, supervised swimming areas with an adult present.

#### 2. The Buddy System & Safe Pathways
- Always walk to and from school in groups along well-lit, busy main roads. Never take isolated shortcuts through dark forests or abandoned buildings.

#### 3. Personal Body Boundaries & Stranger Safety
- **Refuse Gifts from Strangers**: Never accept gifts, rides, money, or snacks from people you do not know.
- **Say NO to Unwanted Touch**: Your body belongs to you. If anyone touches you in a way that makes you uncomfortable, say "NO" loudly and report immediately to your parent or teacher!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Environmental Hazard Awareness & Digital Safety",
                    "type": "diagram",
                    "content": {
                        "title": "Environmental Hazard Awareness & Digital Safety Shield Blueprint",
                        "description": "Dual safety infographic showing physical community safety rules on the left and digital private data protection rules on the right."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Digital Safety & Social Media Myths",
                    "type": "rich_text",
                    "content": {
                        "text": """### Online Safety Truths for Adolescents

**Myth 1**: *"An online profile on social media with a friendly student picture is always safe to chat with."*
- **Fact**: Anyone can download a photo and create a fake profile! Never assume someone online is who they claim to be. Never agree to meet someone in person whom you only met on the internet!

**Myth 2**: *"Sharing my school name and daily timetable online is harmless."*
- **Fact**: Sharing your school name, home address, or phone number online exposes you and your family to strangers. Always keep personal details strictly private!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The Smart Digital Safety Code",
                    "type": "rich_text",
                    "content": {
                        "text": """### 4 Rules for Safe Digital Learning

Follow these 4 rules whenever using phones, tablets, or computers:

- **Rule 1: Keep Personal Information Private**: Never post your full name, phone number, home address, or school location online.
- **Rule 2: Protect Your Passwords**: Keep your passwords secret and never share them with friends or classmates.
- **Rule 3: Tell a Trusted Adult**: If you receive a strange, threatening, or uncomfortable message online, do not reply—show your parent or teacher right away.
- **Rule 4: Limit Screen Time**: Balance phone/screen time with real outdoor physical play and family time!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Safety Champion: The Online Stranger Challenge",
                    "type": "rich_text",
                    "content": {
                        "text": """### Spot the Online Hazard!

**The Situation**:
While playing an online quiz game, Kamau receives a private message from a user named "CoolTeen25": *"You are so smart! Send me your phone number, school name, and home address, and I will courier you a free gaming watch!"*

**The Diagnosis**:
- This is a classic online stranger danger attempting to obtain Kamau's private personal information using a gift bribe!

**The Correct Action**:
- Kamau must NOT share his phone number, school, or address.
- He should block the user immediately.
- He must inform his parent or teacher about the suspicious message!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Exercise & Safety Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Which of the following represents a safe practice when using digital devices and interacting online?",
                        "options": [
                            "Sharing your school name and home address with friendly strangers in online games",
                            "Keeping your personal details, home address, and passwords strictly private and reporting strange messages to a trusted adult",
                            "Meeting up alone in a quiet park with a person you only met on social media",
                            "Sending family photos to strangers who promise free gifts"
                        ],
                        "correct_index": 1,
                        "explanation": "Digital safety requires keeping private personal information (like your home address, school, and passwords) secret and reporting suspicious messages or strangers to parents or teachers."
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
    print(f"[SUCCESS] CBC Grade 6 Home Science Topic 1 Ingestion Complete!")
    print(f"[*] Total Lessons: {total_lessons}, Total Pages across lessons: {total_lessons * 8}, Total Blocks: {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_cbc_grade6_home_science_topic1()
