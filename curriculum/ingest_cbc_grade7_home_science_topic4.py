"""
VLearn CBC Grade 7 Home Science — Topic 4: Consumer Education (Buying Goods & Services)
Curriculum Ingestion Engine (Phase 1: Content, Pages & Blocks)

Curriculum: CBC (ID: 5)
Grade: Grade 7 (ID: 16, Level: 7)
Subject: Home Science (ID: 29)
Topic: Consumer Education (Order: 4)

Generates 4 Learning Units & 4 Published Lessons (32 Total Structured Pages, 47 Blocks):
  - Unit 1: Household Needs: Tangible Goods vs. Paid Services (8 Pages)
  - Unit 2: Factors Influencing Buying Choices & Smart Saving (8 Pages)
  - Unit 3: Where We Shop, Payment Methods & The Market Survey (8 Pages)
  - Unit 4: Safe Transactions, Market Challenges & Consumer Integrity (8 Pages)

Formatting Standards Applied:
  - Standard markdown bullet lists (- ) with blank line prefixes
  - Prominent bold terms and key concepts
  - Step processes, comparison matrices, and worked examples
  - Zero bracket citations ([70], [71]) and zero prompt meta-language

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade7_home_science_topic4.py [--replace]
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

def ingest_cbc_grade7_home_science_topic4(replace=True):
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 7 HOME SCIENCE — TOPIC 4: CONSUMER EDUCATION")
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
        name="Consumer Education",
        defaults={
            "order": 4,
            "description": "Personal financial literacy, distinguishing goods vs. services, 5 purchase factors, sale outlets, payment methods, comparative shopping, safe checkout transactions, and defeating counterfeit scams."
        }
    )
    if not created and replace:
        print(f"[*] Replacing existing content for Topic: '{topic.name}' (ID: {topic.id})")
        topic.lessons.all().delete()
        topic.learning_units.all().delete()
    elif created:
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # =========================================================================
    # LESSON 1: HOUSEHOLD NEEDS: TANGIBLE GOODS VS. PAID SERVICES (8 Pages)
    # =========================================================================
    u1, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Household Needs: Tangible Goods vs. Paid Services",
        defaults={
            "order": 1,
            "description": "Understanding basic household survival needs, distinguishing physical goods from intangible services, and budgeting essentials."
        }
    )
    l1 = Lesson.objects.create(
        topic=topic,
        learning_unit=u1,
        title="Household Needs: Tangible Goods vs. Paid Services",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 1: '{l1.title}' (Lesson ID: {l1.id})")

    # Page 1: Hook & Introduction
    create_block(l1, 1, 1, "suggested_image", "Welcome to the Marketplace! Meeting Family Needs", {
        "caption": "Every household acquires goods and services daily to satisfy survival, health, education, and comfort needs.",
        "search_query": "african village domestic market community"
    })
    create_block(l1, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Explain the primary purpose of acquiring **household goods and services**.\n- Distinguish between **tangible goods** and **intangible services** with local examples.\n- Understand why **airtime cards and bus tickets** are tokens for underlying services.\n- Differentiate essential **survival needs** from non-essential **luxury wants**."
    })
    create_block(l1, 1, 3, "concept_explanation", "Household Needs, Goods, and Services", {
        "text": "Every family has basic needs to survive and live comfortably, including food, clothing, shelter, health care, and education.\n\n- **Household Goods**: Physical, tangible items that you can touch, hold, put in a basket, and take home (e.g. maize flour, textbooks, school uniform, bar soap, cooking pots).\n- **Household Services**: Non-physical work, labor, utilities, or expert assistance performed for us by others (e.g. matatu transport, doctor's clinic checkup, haircut by a barber, piped water supply, mobile phone network access)."
    })

    # Page 2: Goods vs Services Blueprint
    create_block(l1, 2, 1, "suggested_diagram", "Tangible Goods vs. Intangible Services Blueprint", {
        "caption": "Visual diagram contrasting touchable physical household goods with paid labor and utility services.",
        "diagram_type": "comparison_split"
    })
    create_block(l1, 2, 2, "concept_explanation", "The Token Misconception: Airtime & Bus Tickets", {
        "text": "Sometimes physical tokens represent paid services:\n\n- When you buy a mobile airtime scratch card or receive a paper bus receipt, the paper card is just a temporary voucher.\n- What you are actually purchasing is the **intangible telecommunication or transport service** that transmits your phone call or carries you safely down the road."
    })

    # Page 3: Comparison Table
    create_block(l1, 3, 1, "comparison_table", "Comparative Guide to Household Goods and Services", {
        "headers": ["Feature", "Household Goods", "Household Services"],
        "rows": [
            ["Tangibility & Touch", "Physical and tangible; can be held, weighed, and stored in cupboards", "Intangible; cannot be touched physically; consumed as it is performed"],
            ["Ownership", "Buyer takes full physical ownership of the product after payment", "Buyer pays for the benefit of the person's labor, time, or technical system"],
            ["Common Examples", "Maize flour, textbooks, washing soap, school shoes, cooking sufurias", "Matatu bus rides, tailor repair work, doctor consultations, electricity supply"],
            ["Storage & Transfer", "Can be stored for later use or passed on to others physically", "Cannot be stored in a box; once performed, the service is complete"]
        ]
    })

    # Page 4: Wants vs Needs
    create_block(l1, 4, 1, "concept_explanation", "Understanding Needs vs. Wants", {
        "text": "Money is limited for every household. A wise buyer prioritizes carefully:\n\n- **Needs**: Essential items required for survival, health, and schooling (e.g. nutritious food, exercise books, medical care). Without these, life becomes difficult or dangerous.\n- **Wants**: Things we desire for pleasure, entertainment, or luxury (e.g. soda, expensive video games, decorative fashion items). Wants should only be purchased after all essential needs are fully covered."
    })

    # Page 5: Worked Example
    create_block(l1, 5, 1, "step_process", "Worked Example: Classifying a Family's Weekly Shopping Basket", {
        "steps": [
            {"number": 1, "title": "2kg Packet of Maize Flour", "description": "Classification: Physical Good. Purpose: Essential food need to prepare family ugali."},
            {"number": 2, "title": "50 Shillings Paid for Tailor Zipper Repair", "description": "Classification: Paid Service. Purpose: Paying for the tailor's skilled labor to fix school trousers."},
            {"number": 3, "title": "Box of 12 Exercise Books", "description": "Classification: Physical Good. Purpose: Essential educational material for school assignments."},
            {"number": 4, "title": "Boda-Boda Fare to the Market", "description": "Classification: Paid Service. Purpose: Paying for transportation labor to carry heavy groceries home."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l1, 6, 1, "mini_activity", "Hands-On Task: The Household Goods & Services Audit", {
        "instructions": "Audit your home spending this week and record in your Home Science notebook:\n\n- List **3 Physical Goods** your family bought (e.g. soap, milk, salt).\n- List **3 Paid Services** your family used (e.g. electricity tokens, haircut, water vendor).\n- For each item, state whether it satisfied a basic **Need** or a luxury **Want**."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l1, 7, 1, "key_takeaway", "Key Takeaways: Goods, Services & Needs", {
        "text": "Remember these financial foundations:\n\n- **Goods** are touchable physical objects; **services** are paid actions and utilities.\n- **Needs** must always be funded before **wants** when budgeting.\n- Physical tokens (like airtime cards) represent **intangible services**."
    })

    # Page 8: Knowledge Check
    create_block(l1, 8, 1, "knowledge_check", "Scenario Knowledge Check: Goods, Services & Needs", {
        "question": "A student pays 50 shillings to a local shoe repairer (fundi) to stitch a torn school shoe. What has the student paid for?",
        "options": [
            "A physical manufacturing good",
            "A household service (skilled repair labor)",
            "A luxury want",
            "A commercial retail product"
        ],
        "correct_index": 1,
        "explanation": "Correct! The shoe fundi provides skilled labor and expertise to repair your shoe. You are paying for a service, not buying a new manufactured good."
    })

    # =========================================================================
    # LESSON 2: FACTORS INFLUENCING BUYING CHOICES & SMART SAVING (8 Pages)
    # =========================================================================
    u2, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Factors Influencing Buying Choices & Smart Saving",
        defaults={
            "order": 2,
            "description": "Evaluating the 5 buying factors, balancing price vs. quality, and calculating unit price savings through bulk purchasing."
        }
    )
    l2 = Lesson.objects.create(
        topic=topic,
        learning_unit=u2,
        title="Factors Influencing Buying Choices & Smart Saving",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 2: '{l2.title}' (Lesson ID: {l2.id})")

    # Page 1: Hook & Introduction
    create_block(l2, 1, 1, "suggested_image", "The Shopping Dilemma: Spending Family Income Wisely", {
        "caption": "Evaluating product durability, pricing, and family needs before spending money protects household wealth.",
        "search_query": "kitchen utensils shopping market retail"
    })
    create_block(l2, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Analyze the **5 Wise Buyer Evaluation Factors** before making any purchase.\n- Balance **Price against Quality & Durability** to achieve long-term value.\n- Calculate **unit price and bulk buying savings** using simple practical mathematics.\n- Formulate a **budget-saving shopping list** to prevent wasteful impulse buying."
    })
    create_block(l2, 1, 3, "concept_explanation", "The 5 Questions Every Wise Buyer Asks", {
        "text": "A smart consumer never buys impulsively. Before taking money out of your pocket, evaluate these 5 factors:\n\n- **1. Price**: Is the cost fair and competitive across local shops?\n- **2. Budget**: How much money do we have allocated? Can we afford this right now?\n- **3. Quality**: Is the item durable, well-stitched, fresh, and safe? Will it last?\n- **4. Need / Urgency**: Is this essential for our survival/health, or can it wait?\n- **5. Substitutes**: Is there a cheaper alternative brand or local item that does the same job?"
    })

    # Page 2: Price vs Quality Balance Scale Blueprint
    create_block(l2, 2, 1, "suggested_diagram", "The Price vs. Quality Balance Scale Blueprint", {
        "caption": "Visual diagram showing the balance between price, durability, and budget allocation.",
        "diagram_type": "balance_scale"
    })
    create_block(l2, 2, 2, "concept_explanation", "The True Cost of 'Cheap' Products", {
        "text": "The cheapest item is not always the best choice!\n\n- If you buy a brittle 20-shilling plastic ruler that snaps in your school bag on the first day, you must spend another 20 shillings to replace it.\n- If you buy a sturdy 25-shilling wooden ruler that lasts all year, you save money and reduce waste. **Wise consumers prioritize durable value over cheap fragility.**"
    })

    # Page 3: Comparison Table: The 5 Factors
    create_block(l2, 3, 1, "comparison_table", "The 5 Wise Buyer Purchase Evaluation Factors", {
        "headers": ["Factor", "Consumer Question", "Practical Application in the Market"],
        "rows": [
            ["Budget", "How much money is allocated for this category?", "Never spend family food or rent money on optional gadgets or luxury snacks."],
            ["Price", "Is the vendor offering a fair market rate?", "Survey 2-3 shops to compare rates before handing over cash."],
            ["Quality", "Is the material strong, hygienic, and long-lasting?", "Inspect stitching on shoes, thickness of sufurias, and freshness of vegetables."],
            ["Need / Urgency", "Do we require this item immediately?", "Buy school exercise books before buying optional decorative stickers."],
            ["Substitutes", "Is there a cheaper local alternative?", "Buy loose local tea or sweet potatoes instead of expensive imported brands."]
        ]
    })

    # Page 4: Bulk Buying Mathematics Blueprint
    create_block(l2, 4, 1, "suggested_diagram", "Bulk Buying & Unit Price Mathematics Blueprint", {
        "caption": "Comparative infographic demonstrating how buying larger units saves significant household income over time.",
        "diagram_type": "financial_infographic"
    })
    create_block(l2, 4, 2, "concept_explanation", "The Power of Unit Price Comparison", {
        "text": "Manufacturers often charge more per gram for small sachets and mini-packets:\n\n- Buying four small 250g packets of washing soap at 35 KES each costs **140 KES total** (1 kg).\n- Buying a single 1 kg box of the exact same soap costs **100 KES**.\n- **You save 40 KES** on just one household item! Over a year, small bulk savings add up to thousands of shillings."
    })

    # Page 5: Worked Example: Bulk Oil Math
    create_block(l2, 5, 1, "step_process", "Worked Example: Calculating Bulk vs. Small-Unit Savings", {
        "steps": [
            {"number": 1, "title": "Identify Small Unit Cost", "description": "A 1-litre bottle of cooking oil costs 180 KES at the kiosk. To get 2 litres, you would buy two bottles: 180 x 2 = 360 KES."},
            {"number": 2, "title": "Identify Bulk Unit Cost", "description": "A single 2-litre container of the same cooking oil costs 320 KES at the wholesale shop."},
            {"number": 3, "title": "Calculate the Direct Savings", "description": "Subtract bulk cost from small unit cost: 360 KES - 320 KES = 40 KES saved."},
            {"number": 4, "title": "Allocate the Savings", "description": "The 40 KES saved can buy a packet of salt and fresh coriander (dhania) for dinner!"}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l2, 6, 1, "mini_activity", "Hands-On Task: Designing a Family Shopping List", {
        "instructions": "Plan a budget-conscious shopping list for your home:\n\n- Divide your page into 3 columns: **Item Needed**, **Estimated Price**, **Possible Cheaper Substitute**.\n- List 5 essential grocery items (e.g. cooking oil, flour, vegetables, soap, salt).\n- Identify 2 items where buying a larger bulk size or local brand will save money."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l2, 7, 1, "key_takeaway", "Key Takeaways: Buying Factors & Saving", {
        "text": "Remember these consumer rules:\n\n- Evaluate **Price, Budget, Quality, Need, and Substitutes** before buying.\n- A slightly higher price for **high durability** saves money in the long run.\n- **Bulk buying and unit price comparison** save substantial family income.\n- Always prepare a **written shopping list** to stop impulse spending."
    })

    # Page 8: Knowledge Check
    create_block(l2, 8, 1, "knowledge_check", "Scenario Knowledge Check: Buying Factors & Bulk Savings", {
        "question": "A family needs 1 kilogram of washing powder. Four 250g small packets cost 35 shillings each (140/- total), while a 1kg box costs 100 shillings. Why should the family buy the 1kg box?",
        "options": [
            "The 1kg box is heavier to carry home",
            "Buying the 1kg box gives the same quantity while saving 40 shillings of family income",
            "Small packets clean clothes better than large boxes",
            "Small packets never expire"
        ],
        "correct_index": 1,
        "explanation": "Correct! Buying in bulk (the 1kg box) reduces packaging and unit costs, allowing the family to save 40 shillings ($140 - 100 = 40$ KES) on the exact same product."
    })

    # =========================================================================
    # LESSON 3: WHERE WE SHOP, PAYMENT METHODS & THE MARKET SURVEY (8 Pages)
    # =========================================================================
    u3, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Where We Shop, Payment Methods & The Market Survey",
        defaults={
            "order": 3,
            "description": "Exploring local sale outlets, comparing payment methods (cash, mobile money, credit, barter), and conducting market surveys."
        }
    )
    l3 = Lesson.objects.create(
        topic=topic,
        learning_unit=u3,
        title="Where We Shop, Payment Methods & The Market Survey",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 3: '{l3.title}' (Lesson ID: {l3.id})")

    # Page 1: Hook & Introduction
    create_block(l3, 1, 1, "suggested_image", "Navigating the Local Shopping Center", {
        "caption": "From neighborhood retail kiosks to bustling open-air markets and supermarkets, choosing the right outlet saves time and money.",
        "search_query": "african street market fresh vegetables"
    })
    create_block(l3, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Identify common **sale outlets** in your locality (kiosks, open-air markets, supermarkets, online).\n- Compare modern and traditional **payment methods** (cash, mobile money, credit, barter).\n- Recognize the severe financial risks of **buying on credit (deni)**.\n- Conduct a **comparative market survey** across 2-3 outlets before buying."
    })
    create_block(l3, 1, 3, "concept_explanation", "Where We Shop in Our Communities", {
        "text": "Consumers have access to diverse shopping outlets, each offering distinct advantages:\n\n- **Retail Kiosks**: Small neighborhood shops offering immediate convenience for quick daily purchases (matchboxes, single eggs, salt).\n- **Open-Air Markets**: Bustling open spaces where farmers sell fresh agricultural produce (tomatoes, kales, sweet potatoes) at negotiable prices.\n- **Supermarkets & Malls**: Large self-service shops with vast brand varieties and fixed prices.\n- **Online E-commerce**: Digital shops where orders are placed via smartphone and delivered to your doorstep."
    })

    # Page 2: Sale Outlets & Payment Systems Blueprint
    create_block(l3, 2, 1, "suggested_diagram", "Local Sale Outlets & Modern Payment Systems Blueprint", {
        "caption": "Interactive map showing local retail outlets connected to modern payment pathways.",
        "diagram_type": "town_map"
    })
    create_block(l3, 2, 2, "concept_explanation", "Modern & Traditional Payment Systems", {
        "text": "How we pay is just as important as where we shop:\n\n- **Cash**: Physical bank notes and coins. Instant, universally accepted, but carries risk of physical loss or theft.\n- **Mobile Money (e.g. M-Pesa)**: Instant digital money transfer via phone. Highly secure, eliminates carrying loose coins, and provides electronic SMS receipts.\n- **Credit (Deni)**: Taking goods now with an agreement to pay later. **Warning: Credit is a loan, not free money!** Excessive credit traps families in stressful debt.\n- **Barter Trade**: Directly swapping goods without money (e.g. trading a basket of sweet potatoes for a tin of beans)."
    })

    # Page 3: Comparison Table: Sale Outlets
    create_block(l3, 3, 1, "comparison_table", "Comparing Local Shopping Outlets", {
        "headers": ["Outlet Type", "Primary Advantages", "Limitations to Consider"],
        "rows": [
            ["Retail Kiosk", "Close to home, open late, sells in small accessible units", "Higher unit prices, limited brand choices"],
            ["Open-Air Market", "Freshest farm vegetables, lower prices, bargaining possible", "Crowded, weather-dependent, requires physical inspection"],
            ["Supermarket", "Vast variety under one roof, fixed printed prices, receipts provided", "Higher prices due to overheads, encourages impulse buying"],
            ["Online Store", "Convenient home delivery, easy price comparison on phone", "Delivery fees, delivery delays, cannot inspect goods physically before paying"]
        ]
    })

    # Page 4: Comparison Table: Payment Methods
    create_block(l3, 4, 1, "comparison_table", "Comparing Household Payment Methods", {
        "headers": ["Payment Method", "How It Operates", "Key Benefit & Risk Profile"],
        "rows": [
            ["Cash", "Handing physical currency notes and coins to the seller", "Instant exchange; Risk: Loss, theft, or counterfeit notes"],
            ["Mobile Money", "Sending money digitally from phone wallet (e.g. M-Pesa)", "Fast, safe, instant SMS proof; Risk: Wrong number entry or network failure"],
            ["Credit (Deni)", "Shopkeeper records debt in a ledger for payment at month-end", "Helps in emergencies; Extreme Risk: Debt accumulation & interest"],
            ["Barter Trade", "Exchanging goods directly with a neighbor without currency", "Zero cash needed; Limitation: Requires mutual need of items"]
        ]
    })

    # Page 5: Worked Example: Market Survey Dashboard
    create_block(l3, 5, 1, "suggested_diagram", "The Comparative Market Survey Dashboard", {
        "caption": "Market survey table evaluating maize flour price, quality, and expiry date across three outlets.",
        "diagram_type": "comparison_dashboard"
    })
    create_block(l3, 5, 2, "step_process", "Worked Example: Conducting a 3-Shop Comparative Survey", {
        "steps": [
            {"number": 1, "title": "Check Hustle Kiosk", "description": "2kg Maize Flour = 160 KES (Fresh stock, EXP: 10/2026, 1-minute walk from home)."},
            {"number": 2, "title": "Check Town Supermarket", "description": "2kg Maize Flour = 145 KES (Same brand, EXP: 11/2026, 10-minute walk)."},
            {"number": 3, "title": "Check Wholesale Depo", "description": "2kg Maize Flour = 135 KES (Bulk pack required, EXP: 08/2026)."},
            {"number": 4, "title": "Make the Informed Decision", "description": "Walking to the supermarket saves 15 KES per packet while providing fresh stock and a printed receipt!"}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l3, 6, 1, "mini_activity", "Hands-On Task: Mini Market Survey in Your Neighborhood", {
        "instructions": "Conduct a mini market survey with a parent or guardian:\n\n- Visit or check prices at **2 different local shops**.\n- Record the price for **1kg Sugar** and **500g Salt** at both shops.\n- Calculate the difference in shillings between the two shops.\n- Identify which shop offers the best combination of fair price and fresh stock."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l3, 7, 1, "key_takeaway", "Key Takeaways: Outlets & Market Surveys", {
        "text": "Remember these market skills:\n\n- **Open-air markets** offer fresh produce; **kiosks** offer convenience; **supermarkets** offer variety.\n- **Mobile money** is secure and gives instant SMS payment receipts.\n- Avoid **buying on credit (deni)** to protect your family from debt traps.\n- Conduct a **market survey** before big purchases to save family income."
    })

    # Page 8: Knowledge Check
    create_block(l3, 8, 1, "knowledge_check", "Scenario Knowledge Check: Outlets, Payments & Market Surveys", {
        "question": "A buyer purchases groceries on credit (deni) every week from a local kiosk without checking prices. What is the primary danger of this buying habit?",
        "options": [
            "The kiosk owner will give free groceries forever",
            "The family can easily lose track of spending, accumulate heavy debt, and pay higher prices",
            "The groceries will turn into plastic automatically",
            "Mobile money will stop working on their phone"
        ],
        "correct_index": 1,
        "explanation": "Correct! Buying on credit blinds consumers to daily spending totals. When the monthly bill arrives, families often struggle with severe debt, especially since kiosks often charge higher prices for credit items."
    })

    # =========================================================================
    # LESSON 4: SAFE TRANSACTIONS, MARKET CHALLENGES & INTEGRITY (8 Pages)
    # =========================================================================
    u4, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Safe Transactions, Market Challenges & Consumer Integrity",
        defaults={
            "order": 4,
            "description": "Mastering the 4-step safe transaction checklist, counting change accurately, demonstrating market integrity, and defeating counterfeit scams."
        }
    )
    l4 = Lesson.objects.create(
        topic=topic,
        learning_unit=u4,
        title="Safe Transactions, Market Challenges & Consumer Integrity",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 4: '{l4.title}' (Lesson ID: {l4.id})")

    # Page 1: Hook & Introduction
    create_block(l4, 1, 1, "suggested_image", "The Alert Consumer: Spotting Fakes & Safe Checkout", {
        "caption": "Practicing polite communication, counting change carefully, and inspecting factory seals protects consumer rights.",
        "search_query": "checking money transaction checkout market"
    })
    create_block(l4, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Execute the **4-step safe and polite market transaction checklist**.\n- Calculate and **verify correct cash change** accurately before leaving the counter.\n- Demonstrate **honesty and integrity** by returning extra change given by mistake.\n- Detect common marketplace tricks: **counterfeit branding, expired dates, broken seals, and deceptive ads**."
    })
    create_block(l4, 1, 3, "concept_explanation", "The Anatomy of a Safe Transaction", {
        "text": "A market transaction is a two-way exchange of value. As a responsible consumer, you must protect your health, money, and integrity during every purchase.\n\n- Polite communication builds community trust and mutual respect between buyers and sellers.\n- Counting change immediately at the counter is standard responsible behavior that prevents misunderstandings later."
    })

    # Page 2: 4-Step Transaction Storyboard Blueprint
    create_block(l4, 2, 1, "suggested_diagram", "The 4-Step Safe & Polite Transaction Storyboard", {
        "caption": "Step-by-step storyboard demonstrating greeting, inspecting, paying/calculating change, and requesting a receipt.",
        "diagram_type": "transaction_storyboard"
    })
    create_block(l4, 2, 2, "concept_explanation", "The 4-Step Transaction Checklist", {
        "text": "Always follow these 4 steps at the checkout counter:\n\n- **1. Greet Politely & Confirm Price**: Say 'Good morning' and confirm the exact price before handing over goods.\n- **2. Inspect Quality & Expiry**: Check for factory safety seals, intact packaging, and valid Expiry (EXP) dates.\n- **3. Pay & Calculate Change**: Hand over money, calculate the change mentally ($200 - 85 = 115$ KES), and count coins before stepping away.\n- **4. Request Receipt & Say Thank You**: A receipt is your legal proof of purchase if an item must be returned."
    })

    # Page 3: Change Math & Consumer Integrity
    create_block(l4, 3, 1, "comparison_table", "The Change Counter Mathematics Guide", {
        "headers": ["Amount Handed to Seller", "Total Cost of Goods", "Correct Change Calculation", "Integrity Action"],
        "rows": [
            ["100 KES Note", "65 KES (Milk)", "100 - 65 = 35 KES (One 20/- coin + One 10/- coin + One 5/- coin)", "Verify coins at counter; thank shopkeeper"],
            ["200 KES Note", "85 KES (Soap)", "200 - 85 = 115 KES (One 100/- note + One 10/- coin + One 5/- coin)", "Count carefully before placing in pocket"],
            ["500 KES Note", "380 KES (Flour + Sugar)", "500 - 380 = 120 KES (One 100/- note + One 20/- coin)", "If given 150/- by mistake, return 30/- immediately!"]
        ]
    })

    # Page 4: Genuine vs Counterfeit Blueprint
    create_block(l4, 4, 1, "suggested_diagram", "Spotting Market Tricks: Genuine vs. Counterfeit Blueprint", {
        "caption": "Split visual guide comparing genuine KEBS-approved products with misspelled counterfeit goods and broken seals.",
        "diagram_type": "counterfeit_detector"
    })
    create_block(l4, 4, 2, "concept_explanation", "Defeating Common Market Tricks", {
        "text": "Dishonest traders sometimes use deceitful tricks to sell unsafe goods:\n\n- **Counterfeit (Fake) Branding**: Look for misspelled names like 'Colgatte' instead of 'Colgate', or 'Areil' instead of 'Ariel'. Always look for the official **KEBS quality standardization mark**.\n- **Expired Goods**: Always inspect the 'Best Before' (BB) or 'Expiry Date' (EXP). Never consume expired dairy or canned food.\n- **Broken Seals & Bulging Cans**: Never buy bottles with broken security rings or canned foods with swollen, bulging lids (bulging cans harbor deadly food-poisoning toxins!).\n- **Misleading Advertisements**: Extreme claims (e.g. 'This juice cures all sickness!') are illegal and false. Practice critical thinking!"
    })

    # Page 5: Worked Example: Inspecting Products
    create_block(l4, 5, 1, "step_process", "Worked Example: The 4-Point Pre-Purchase Product Inspection", {
        "steps": [
            {"number": 1, "title": "Check the Expiry Date", "description": "Locate the stamped EXP date on the crimp or cap. Ensure the date is well into the future."},
            {"number": 2, "title": "Inspect the Security Seal", "description": "Verify that the plastic ring under the cap is unbroken and the foil seal has no punctures."},
            {"number": 3, "title": "Check Brand Spelling & KEBS Logo", "description": "Confirm correct brand spelling and check for the authentic diamond-shaped KEBS quality mark."},
            {"number": 4, "title": "Examine Physical Condition", "description": "Ensure packets are not torn, cans are not dented or rusted, and bottles are not leaking."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l4, 6, 1, "mini_activity", "Hands-On Task: The Product Detective Inspection", {
        "instructions": "Inspect 3 packaged items in your home kitchen (e.g. salt packet, milk carton, cooking oil bottle):\n\n- Find and write down the **Expiry Date (EXP)** or **Best Before Date** for each item.\n- Check if the **KEBS quality mark** is printed on the package.\n- Check if the brand name is spelled 100% correctly.\n- Share your findings with a family member to ensure all pantry items are safe to consume!"
    })

    # Page 7: Key Takeaways & Recall
    create_block(l4, 7, 1, "key_takeaway", "Key Takeaways: Safe Transactions & Integrity", {
        "text": "Remember these vital consumer safety rules:\n\n- Follow the 4 steps: **Greet $\\rightarrow$ Inspect $\\rightarrow$ Pay & Count Change $\\rightarrow$ Collect Receipt**.\n- Always practice **integrity**: return extra change given by accident.\n- Watch out for **counterfeit spellings, broken seals, and expired dates**.\n- Never buy **bulging or dented canned goods**."
    })

    # Page 8: Knowledge Check
    create_block(l4, 8, 1, "knowledge_check", "Scenario Knowledge Check: Safe Transactions & Defeating Fakes", {
        "question": "While shopping at a local kiosk, you buy soap for 85 shillings and hand the seller a 200-shilling note. The seller accidentally hands you 140 shillings in change (a 100/- note and two 20/- coins). What is the correct, honest action to take?",
        "options": [
            "Keep the extra money quietly and run away before the seller notices",
            "Calculate that correct change is 115 shillings (200 - 85), and politely return the extra 25 shillings immediately",
            "Demand a free packet of sweets as a reward",
            "Give the extra money to a friend outside"
        ],
        "correct_index": 1,
        "explanation": "Correct! Responsible consumer citizenship requires honesty and integrity. Correct change is 115 KES ($200 - 85 = 115$). Handing back the extra 25 KES demonstrates character and strengthens community trust."
    })

    total_lessons = topic.lessons.count()
    total_pages = sum(len(set(l.blocks.values_list("page_number", flat=True))) for l in topic.lessons.all())
    total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 4 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CBC Grade 7 Home Science Topic 4: Consumer Education")
    parser.add_argument("--replace", action="store_true", default=True, help="Replace existing topic content")
    args = parser.parse_args()
    ingest_cbc_grade7_home_science_topic4(replace=args.replace)
