"""
VLearn Curriculum Ingestion Script
CBC Grade 6 — Home Science
Topic 2: Budgeting (Order: 2)
Module 2: Consumer Education (Strand 2.0 / Sub-strand 2.1)

Creates:
- Topic 2: Budgeting (Order: 2) under CBC -> Grade 6 -> Home Science
- 3 Learning Units
- 3 Published Lessons (24 Pages, 8 per lesson)
- 30 LessonBlocks (10 per lesson)
- Upper Primary (Grade 6) appropriate financial literacy, zero bracket citations, proper '- ' markdown lists.
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

def ingest_cbc_grade6_home_science_topic2():
    print("=" * 80)
    print("INGESTING CBC GRADE 6 HOME SCIENCE — TOPIC 2: BUDGETING")
    print("=" * 80)

    # 1. Resolve Hierarchy
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    assert grade, "Grade 6 not found!"
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Home Science", defaults={"description": "CBC Grade 6 Home Science Curriculum"})

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}")

    # 2. Create or Get Topic 2 (Budgeting)
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Budgeting",
        defaults={
            "order": 2,
            "description": "Equipping Grade 6 learners with personal financial literacy, understanding needs versus wants, balancing income and expenses, using shopping lists to avoid impulse buying, making personal pocket-money budgets, and creating a term-long budget portfolio."
        }
    )
    if not created:
        topic.order = 2
        topic.description = "Equipping Grade 6 learners with personal financial literacy, understanding needs versus wants, balancing income and expenses, using shopping lists to avoid impulse buying, making personal pocket-money budgets, and creating a term-long budget portfolio."
        topic.save()
    print(f"[+] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Clear existing units and lessons under this topic for idempotent ingestion
    topic.learning_units.all().delete()
    print("[*] Cleared existing learning units and lessons under Grade 6 Topic 2.")

    units_data = [
        {
            "order": 1,
            "title": "Discovering Needs, Wants & Budgets",
            "description": "Differentiating essential survival and school needs from elective personal wants, defining a budget, and understanding the core balance between income and expenses.",
            "lesson_title": "Discovering Needs, Wants, and Budgets",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Shiny Coin Dilemma!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "market vendor produce kenya shopping",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/A_beautiful_market_vendor.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/A_beautiful_market_vendor.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "A bustling open-air market vendor showcasing fresh produce where shoppers make smart daily budgeting choices."
                    }
                },
                {
                    "page": 1,
                    "title": "Welcome to the Money Maze!",
                    "type": "rich_text",
                    "content": {
                        "text": """### What Would You Buy First?

Imagine your favorite aunt visits your home and places a shiny **100-shilling coin** in your palm!
- You feel thrilled and walk towards the shopping center on Monday afternoon.
- In the shop window, you spot a brightly colored toy whistle that costs 70 shillings.
- But your Home Science exercise book is completely full, and you need a new 50-shilling exercise book to complete tonight's homework!

If you buy the toy whistle:
- You will have only 30 shillings left, which is not enough to buy your homework book!
- Tomorrow morning, you will have no book for class!

How do wise consumers decide where their money goes?
Welcome to the exciting world of **Consumer Education** and **Budgeting**!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "Needs vs. Wants Classification Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "Needs vs. Wants Classification Blueprint",
                        "description": "Comparative chart contrasting Essential Survival & School Needs (food, clean water, uniform, pencils) with Elective Personal Wants (soda, toys, candy, wristbands)."
                    }
                },
                {
                    "page": 2,
                    "title": "Needs vs. Wants: The Golden Rule",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Golden Rule of Wise Spending

Every item you buy falls into one of two groups:

- **1. Essential Needs**:
  - Things you **must have to survive, stay healthy, and do your schoolwork**.
  - *Examples*: Nutritious food, clean drinking water, school uniform, exercise books, pencils, and medicine when sick.
  - *Rule*: Needs must ALWAYS be bought first before spending on anything else!
- **2. Elective Wants**:
  - Things that are **nice to have for fun or fashion**, but you can easily live without.
  - *Examples*: Chewing gum, packaged sweets, shiny keychains, fizzy sodas, and toys.
  - *Rule*: Wants can always be delayed or skipped to save money!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "What is a Budget & Why Does it Balance?",
                    "type": "rich_text",
                    "content": {
                        "text": """### Your Money Map

A **Budget** is a written spending plan that shows how you will divide and spend your available money over a specific period of time (like a week or a month).

**Budgeting** is the active habit of balancing two sides:

#### The Two Sides of Every Budget:
- **Income (Money In)**: The total money you receive (such as pocket money, gifts from relatives, or earnings from small farm chores).
- **Expenses (Money Out)**: The total money you must pay out to buy goods and services.

#### The Golden Equation of Financial Peace:
$$\\text{Income} \\ge \\text{Expenses} + \\text{Savings}$$

If your expenses are bigger than your income:
- You run out of money and are forced to borrow, falling into **debt**!
- When your budget is balanced, you pay for your needs and keep leftover money for **savings**!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The Balanced Budget Scales Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "The Balanced Budget Scales Blueprint",
                        "description": "Illustrated balance scale showing Income (100/- KES) on the left pan balancing Expenses (Book: 50/-, Pen: 30/-) and Savings (20/-) on the right pan."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Budgeting Myths vs. Money Facts",
                    "type": "rich_text",
                    "content": {
                        "text": """### Common Money Myths Debunked

**Myth 1**: *"Budgeting is only for rich business people who have millions of shillings."*
- **Fact**: Budgeting is actually most important when you have very little money! Planning carefully ensures that your few coins cover your most essential school and survival needs without wasting a single shilling!

**Myth 2**: *"If my classmate has a fancy pencil case, it becomes a 'need' for me so I don't feel left out."*
- **Fact**: Peer pressure is normal, but a real need is strictly determined by health, survival, or school learning requirements. A simple, affordable pencil case or pouch does the exact same job!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: The 4-Question Spending Test",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Test Any Purchase Before Paying

Before handing over your money at a kiosk, ask yourself these 4 simple questions:

- **Question 1: Is this a Need or a Want?** Will this help me survive, stay healthy, or do my schoolwork?
- **Question 2: Do I have enough Income?** Can I afford this without borrowing from anyone?
- **Question 3: Have I covered my essential needs first?** Are my school books and lunch already secured?
- **Question 4: Can this purchase wait?** If it is a want, can I delay buying it until next month and save my coins today?"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Consumer Lab: Juma's 150-Shilling Decision",
                    "type": "rich_text",
                    "content": {
                        "text": """### Help Juma Make the Right Choice!

**The Situation**:
Juma has **150 shillings** pocket money for the school week. He visits the school bookshop with his friends:
- He must buy a geometry ruler (30 shillings) and a Home Science exercise book (80 shillings).
- He also spots an attractive cartoon sticker for 50 shillings.

**The Math & Decision**:
- Total essential needs: $30 + 80 = 110\\text{ shillings}$.
- Remaining money after needs: $150 - 110 = 40\\text{ shillings}$.
- The cartoon sticker costs 50 shillings.

**The Smart Choice**:
- Juma buys the ruler and exercise book (110/-), leaves the sticker at the shop, and puts the leftover **40 shillings** into his piggy bank savings!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Needs, Wants & Budgeting Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Which of the following correctly pairs an item with its correct financial classification for a Grade 6 learner?",
                        "options": [
                            "Exercise book $\\rightarrow$ Elective Want; Bubble gum $\\rightarrow$ Essential Need",
                            "School uniform $\\rightarrow$ Essential Need; Toy whistle $\\rightarrow$ Elective Want",
                            "Fizzy soda $\\rightarrow$ Essential Need; Clean drinking water $\\rightarrow$ Elective Want",
                            "Fashion sunglasses $\\rightarrow$ Essential Need; Geometry set $\\rightarrow$ Elective Want"
                        ],
                        "correct_index": 1,
                        "explanation": "A school uniform is an essential need required for attending school and protecting the body. A toy whistle is an elective want that is nice to have for fun but can be delayed or skipped to save money."
                    }
                }
            ]
        },
        {
            "order": 2,
            "title": "Why Budgeting Matters & Sticking to It",
            "description": "Examining the five major benefits of budgeting, recognizing factors that influence spending, and using shopping lists as a protective shield against impulse buying.",
            "lesson_title": "Why Budgeting Matters & Sticking to It",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Power of the Shopping List!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "Nairobi Kenya supermarket grocery shopping",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Vegetable_section_of_Carrefour_at_Westgate_Shopping_Mall%2C_Nairobi.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Vegetable_section_of_Carrefour_at_Westgate_Shopping_Mall%2C_Nairobi.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "Shoppers navigating organized grocery and vegetable aisles at a modern supermarket in Nairobi, Kenya, illustrating how a written shopping list guides disciplined purchasing."
                    }
                },
                {
                    "page": 1,
                    "title": "The Tale of Two Kiosks",
                    "type": "rich_text",
                    "content": {
                        "text": """### What Happened on Wednesday Night?

Meet two Grade 6 classmates, Kamau and Mwangi:
- On Monday, both boys received **200 shillings** from their parents to purchase weekly household fuel and cooking supplies.
- **Kamau** wrote a plan: he bought firewood (100/-), kales (50/-), and saved 50/- in his savings tin.
- **Mwangi** walked into the market without a plan. He saw colorful sweets, bought potato crisps, and bought a shiny keyholder.

By Wednesday evening:
- Kamau's family enjoyed a warm, delicious stew cooked over hot firewood under a bright lamp.
- Mwangi sat in a cold, dark kitchen with no firewood, no supper, and an empty pocket!

What makes the difference? Let's discover the **5 Budgeting Superpowers**!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 5 Budgeting Superpowers Infographic",
                    "type": "diagram",
                    "content": {
                        "title": "The 5 Budgeting Superpowers Infographic Blueprint",
                        "description": "5-part bento-grid infographic highlighting 1. Spend Wisely $\rightarrow$ 2. Avoid Debt $\rightarrow$ 3. Set Priorities $\rightarrow$ 4. Reduce Waste & Impulse Buying $\rightarrow$ 5. Know Future Requirements."
                    }
                },
                {
                    "page": 2,
                    "title": "The Five Big Benefits of Budgeting",
                    "type": "rich_text",
                    "content": {
                        "text": """### Why Wise Consumers Always Budget

Budgeting gives you 5 lifelong superpowers:

- **1. Spend Wisely**:
  - Gives every shilling a clear job, making sure your hard-earned money never vanishes on useless items.
- **2. Avoid Debt**:
  - Restricts your spending strictly to what you actually have, protecting you from borrowing or owing shopkeepers.
- **3. Set Priorities**:
  - Helps you focus on survival and education essentials first before spending on entertainment.
- **4. Reduce Wastage & Impulse Buying**:
  - Stops you from buying items suddenly on a whim just because they look attractive.
- **5. Know Future Requirements**:
  - Helps you calculate upcoming expenses (like term school requirements) well in advance!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Factors to Consider & The Shopping List Shield",
                    "type": "rich_text",
                    "content": {
                        "text": """### Two Factors & Your Shopping Shield

When creating a budget, you must always consider two major factors:

#### 1. Available Total Income
- You cannot plan to spend 500 shillings if your income is only 200 shillings. Your income sets the hard ceiling of your budget!

#### 2. Your Personal Spending Habits
- Knowing your behavioral weaknesses (like wanting to buy snacks when hungry after class) helps you plan realistic boundaries!

---

### The Shopping List: Your Budget Shield
A **Shopping List** is a written list of the exact items you need to buy and their estimated prices before you visit a shop.

- **How it Protects You**:
  - It acts like a protective shield against eye-catching advertisements, colorful shop packaging, and tempting treats!
  - You walk straight to the items on your list, pay the exact amount, and return home with your savings intact!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Shopping List Shield vs. Impulse Buying",
                    "type": "diagram",
                    "content": {
                        "title": "The Shopping List Shield vs. Impulse Buying Blueprint",
                        "description": "Split comparative storyboard contrasting shopping without a list (confused, tempted by junk food) with shopping with a list shield (confident, buying essential items, saving change)."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Shopping List Myths vs. Consumer Facts",
                    "type": "rich_text",
                    "content": {
                        "text": """### Common Shopping Traps

**Myth 1**: *"A shopping list is a waste of paper because I have a sharp memory and can remember 3 items."*
- **Fact**: Even with great memory, the physical act of holding a written checklist keeps your brain focused and stops impulsive desires from taking over when you see flashy sweets at the counter!

**Myth 2**: *"Budgeting means you can never buy anything fun or enjoy treats."*
- **Fact**: Budgeting actually lets you enjoy treats without guilt! Once all essential needs and savings are secured, you can safely allocate a small, planned amount to a treat knowing your school supplies are completely safe!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Writing an Unbeatable Shopping List",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Create a 3-Column Shopping List

Follow these 4 simple steps before heading to the market:

- **Step 1: Check Your Household/School Stock**: Look inside your school bag or kitchen pantry to see what is genuinely running low.
- **Step 2: List Essential Needs First**: Write down the exact items (e.g., 1 Bar of Soap, 1 Packet of Salt, 2 Pens).
- **Step 3: Estimate Unit Prices**: Write down the estimated price of each item next to its name.
- **Step 4: Calculate Total Cost**: Add the estimated prices to confirm the total cost fits comfortably inside your available pocket money!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Kiosk Challenge: Spotting the Impulse Buys",
                    "type": "rich_text",
                    "content": {
                        "text": """### Audit Atieno's Shopping Basket!

**The Situation**:
Atieno's mother gave her **300 shillings** and an official family shopping list containing 3 essential items:
- 1 Loaf of Bread (65/-)
- 1 Packet of Milk (60/-)
- 1 Bar of Laundry Soap (80/-)
- *Total Expected Cost*: $65 + 60 + 80 = 205\\text{ shillings}$.

**What Happened in the Shop**:
Atieno bought the Bread, Milk, and Soap, but also picked up a plastic toy bracelet (50/-) and a large chocolate bar (45/-).

**The Diagnosis**:
- Total spent: $205 + 50 + 45 = 300\\text{ shillings}$.
- Atieno spent all 300 shillings and returned with zero change! The bracelet and chocolate were **unplanned impulse buys** that consumed her family's savings!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Budget Benefits & Shopping Lists Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "What is the primary benefit of preparing and carrying a written shopping list when going to the market?",
                        "options": [
                            "It makes shopkeepers give you goods for free",
                            "It acts as a shield to help you focus on essential needs and avoid unplanned impulse buying",
                            "It doubles the amount of cash in your pocket automatically",
                            "It allows you to skip paying for items at the checkout counter"
                        ],
                        "correct_index": 1,
                        "explanation": "A written shopping list keeps a shopper focused on essential planned purchases, preventing wasteful impulse buys and ensuring spending stays strictly within the planned budget."
                    }
                }
            ]
        },
        {
            "order": 3,
            "title": "Building Your Personal Budget & The Portfolio Project",
            "description": "Mastering the 5 steps to creating a balanced personal budget, calculating income and expenses, and constructing a term-long budget portfolio from local materials.",
            "lesson_title": "Building Your Personal Budget & The Portfolio Project",
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Taking Control of Your Financial Future!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "budget ledger cash transaction financial accounting",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Businesswoman_making_a_payment_with_cash_while_using_a_smartphone_in_a_modern_office_setting.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Businesswoman_making_a_payment_with_cash_while_using_a_smartphone_in_a_modern_office_setting.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "Managing personal financial resources with disciplined calculation, recording, and record-keeping."
                    }
                },
                {
                    "page": 1,
                    "title": "Becoming a Master Budget Maker",
                    "type": "rich_text",
                    "content": {
                        "text": """### From Coins to Confidence!

Have you ever wondered how successful adults manage to pay for housing, food, electricity, and school fees every month without getting overwhelmed?
- They don't guess!
- They use a structured, written budget and keep a record of their financial journey!

You don't have to wait until you are an adult to build this superpower. In this lesson, you will:
- Construct your very own balanced **personal budget** in Kenya Shillings (KES).
- Build an improvised **Budget Portfolio Folder** to track your savings throughout the school term!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "Wamae's Balanced Weekly Pocket Money Ledger",
                    "type": "diagram",
                    "content": {
                        "title": "Wamae's Balanced Weekly Pocket Money Ledger Blueprint",
                        "description": "Itemized two-column student budget card showing Income (150/- KES) balanced against Expenses (Exercise book, pen, ruler, pencil = 115/-) and Savings (35/-)."
                    }
                },
                {
                    "page": 2,
                    "title": "The 5 Steps to Building a Personal Budget",
                    "type": "rich_text",
                    "content": {
                        "text": """### The 5-Step Budget Formula

Follow these 5 clear steps whenever creating a personal budget:

- **Step 1: Write Down Your Total Income**:
  - Identify exactly how much money you have available (e.g., Weekly pocket money = 150/-).
- **Step 2: List Your Essential Needs (Expenses)**:
  - Write down each item you must buy and its estimated price.
- **Step 3: Calculate Total Expenses**:
  - Add up the cost of all listed items ($50 + 30 + 20 + 15 = 115\\text{ KES}$).
- **Step 4: Compare & Adjust**:
  - Subtract expenses from income ($150 - 115 = 35\\text{ KES}$). If expenses exceed income, remove wants until it balances!
- **Step 5: Allocate Savings**:
  - Place leftover money into a safe piggy bank or savings tin!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "The Cardboard Budget Portfolio Project",
                    "type": "rich_text",
                    "content": {
                        "text": """### Why Keep a Term-Long Portfolio?

A **Budget Portfolio** is a special personal folder or binder where you safely store and organize all the weekly budgets and shopping logs you create across the school term:

#### The 3 Super Benefits of a Portfolio:
- **1. Track Savings Progress**: Watch your savings curve climb higher from Week 1 to Week 12!
- **2. Learn from Mistakes**: Compare past weeks to see where unplanned spending happened and improve your habits.
- **3. Evidence of Learning**: Show your parents and Home Science teacher your growing financial maturity and disciplined citizenship!

#### Improvised Materials:
- You don't need expensive store-bought files! You can easily craft a durable, beautiful portfolio using a clean carton box, manila paper, sisal string, and colorful markers!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "4-Step Cardboard Portfolio Project Storyboard",
                    "type": "diagram",
                    "content": {
                        "title": "4-Step Cardboard Budget Portfolio Project Storyboard",
                        "description": "Storyboard illustrating 1. Fold sturdy cardboard in half $\rightarrow$ 2. Secure side margins with string/glue $\rightarrow$ 3. Label cover 'MY BUDGET PORTFOLIO' $\rightarrow$ 4. File dated weekly budget sheets inside."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Budget Execution Myths vs. Realities",
                    "type": "rich_text",
                    "content": {
                        "text": """### Execution is Key!

**Myth 1**: *"Once a budget is written nicely in an exercise book, the job is completely done."*
- **Fact**: A budget is only useful if you actually follow it! If you write 30/- for a standard blue pen but buy a fancy 60/- gel pen instead, your budget is broken and your savings disappear.

**Myth 2**: *"If you make a spending mistake one week, you should throw away your portfolio and quit."*
- **Fact**: Financial literacy is a skill that improves with practice! Your portfolio exists so you can reflect on what went wrong, forgive yourself, and make a better plan for the following week!"""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Making Your Cardboard Portfolio",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Assemble Your Term Portfolio

Follow these 4 simple crafting steps:

- **Step 1: Obtain a Clean Sturdy Cardboard**: Cut a clean carton or large manila sheet ($40\\text{ cm} \\times 30\\text{ cm}$) and fold it in half.
- **Step 2: Secure the Side Margins**: Use wood glue or stitch the left and right edges with sisal string to create an open top pocket sleeve.
- **Step 3: Decorate & Label the Front**: Write **"MY BUDGET PORTFOLIO - GRADE 6"**, your name, and admission number neatly on the front cover.
- **Step 4: File Weekly Budget Sheets**: Slide your dated weekly budget tables into the pocket at the end of every week!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "The 120-Shilling Budget Challenge",
                    "type": "rich_text",
                    "content": {
                        "text": """### Build Your Personal Budget!

**The Challenge**:
You receive **120 shillings** pocket money for the week. Here are your options:
- School Lunch (60/-) — *Need*
- Homework Exercise Book (30/-) — *Need*
- Pencil Sharpener (15/-) — *Need*
- Plastic Toy Whistle (30/-) — *Want*
- Packet of Candy (20/-) — *Want*

**The Correct Balanced Plan**:
- **Income**: 120 KES
- **Expenses**: Lunch (60/-) + Book (30/-) + Sharpener (15/-) = **105 KES**
- **Leftover for Savings**: $120 - 105 = \\mathbf{15\\text{ KES}}$
- **Result**: All school needs secured, zero debt, and 15 shillings added to your piggy bank!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Personal Budget & Portfolio Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "If your weekly income is 200 shillings, and your planned essential school expenses total 160 shillings, how much money can you safely allocate to your savings?",
                        "options": [
                            "200 shillings",
                            "40 shillings",
                            "360 shillings",
                            "0 shillings"
                        ],
                        "correct_index": 1,
                        "explanation": "Savings are calculated by subtracting total expenses from total income ($200 - 160 = 40\\text{ shillings}$). This 40 shillings can be safely placed into a piggy bank or savings tin."
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
    print(f"[SUCCESS] CBC Grade 6 Home Science Topic 2 Ingestion Complete!")
    print(f"[*] Total Lessons: {total_lessons}, Total Pages across lessons: {total_lessons * 8}, Total Blocks: {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_cbc_grade6_home_science_topic2()
