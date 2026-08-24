"""
VLearn CBC Grade 8 Home Science — Topic 2: Consumer Education
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (Level: 8)
Subject: Home Science (ID: 28)
Topic: Consumer Education (Topic Order: 2)

Decomposed into 2 Learning Units & 2 Published Lessons (16 Total Structured Pages):
  1. Consumer Awareness & Household Buying Habits (8 Pages)
  2. Market Competition & Consumer Protection (8 Pages)

Features:
  - Rich typography with bold key terms, phrases, and structured bullets.
  - Step-by-step process workflows and diagnostic audits.
  - Formatted comparison tables and practical callouts.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_home_science_topic2.py [--replace]
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Convert unicode bullets to markdown list items
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def build_topic2_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 2: Consumer Education."""
    return [
        # =====================================================================
        # LESSON 1: Consumer Awareness & Household Buying Habits
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Consumer Awareness & Household Buying Habits",
            "unit_description": "Consumer awareness meaning & importance, Needs vs Wants, 4-stage consumer behaviour cycle (Select, Buy, Use, Dispose), 5 buyer types, and 5 household consumer roles.",
            "lesson_title": "Consumer Awareness & Household Buying Habits",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Why Do We Shop the Way We Do?",
                        "content": {
                            "title": "Why Do We Shop the Way We Do?",
                            "caption": "A vibrant open-air marketplace where informed consumers compare prices, check quality, and make deliberate purchasing choices."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Consumer Awareness",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **consumer awareness** and explain why financial literacy protects household resources.",
                                "Distinguish clearly between basic survival **needs** and elective personal **wants**.",
                                "Trace the continuous **4-stage consumer behaviour cycle**: **Select**, **Buy**, **Use**, and **Dispose**.",
                                "Evaluate the **5 types of buyers** in the market and identify the **5 consumer roles** in household purchases."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Consumer Awareness Matters",
                        "content": {
                            "title": "Opening Your Eyes Before You Buy",
                            "text": "Imagine walking through a bustling shopping center with 500 shillings in your pocket. You are surrounded by enticing displays, loud vendor calls, and sweet snacks. How do you decide what to buy?\n\n• **Consumer Awareness**: Having full knowledge of your rights, responsibilities, and market facts to make smart, safe, and cost-effective purchasing decisions.\n• **Limited Household Resources**: Money is limited. Without consumer awareness, hard-earned family income is easily drained on impulse items, expired goods, or deceptive advertisements.\n• **Empowerment**: Being an aware buyer ensures you always get **true value for your money**!"
                        }
                    }
                ],
                # Page 2: Needs vs. Wants: The Wise Buyer's Secret
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Needs vs. Wants: The Wise Household Budgeting Balance",
                        "content": {
                            "title": "Needs vs. Wants: The Wise Household Budgeting Balance",
                            "caption": "Comparative balance scale showing essential survival needs on the left versus non-essential elective wants on the right."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Distinguishing Household Needs from Wants",
                        "content": {
                            "title": "Needs vs. Wants Comparison Matrix",
                            "headers": ["Aspect", "Household Needs (Essentials)", "Personal Wants (Desires)"],
                            "rows": [
                                ["Definition", "Items essential for physical survival, basic health, and everyday function", "Items that bring pleasure, luxury, or status but are not necessary for survival"],
                                ["Examples", "Maize flour, clean water, warm clothing, school books, medicine", "Video games, sweet sodas, designer sunglasses, luxury watches"],
                                ["Urgency & Delay", "Cannot be postponed without serious harm to health or wellbeing", "Can easily be postponed, reduced, or eliminated entirely"],
                                ["Budget Priority", "**First Priority**: Must be fully funded before any other spending", "**Second Priority**: Funded only when all basic needs and savings are secured"],
                                ["Nature of Supply", "Finite: You only need a specific amount to stay healthy and nourished", "Infinite: Human desires are limitless and can never be fully satisfied"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Common Misconception",
                        "content": {
                            "title": "'Anything That Makes Life Easier is a Need'",
                            "text": "A smartphone or bicycle may make communication or commuting convenient, but luxury models are elective **wants**, not survival requirements. A wise consumer always satisfies basic food, shelter, and health requirements before spending on convenience upgrades."
                        }
                    }
                ],
                # Page 3: The 4-Stage Consumer Behaviour Cycle
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 4-Stage Consumer Behaviour Cycle: Select, Buy, Use, Dispose",
                        "content": {
                            "title": "The 4-Stage Consumer Behaviour Cycle",
                            "caption": "Circular continuous loop showing the 4 active phases of the consumer journey: Select, Buy, Use, and Dispose."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Complete Consumer Journey",
                        "content": {
                            "title": "Consumerism Does Not Stop at the Cash Counter!",
                            "text": "Being a consumer is a four-step continuous cycle that governs every household purchase:\n\n• **1. Select (Comparison Phase)**: Identifying household needs, researching options, comparing prices across competitors, and checking product ingredients and expiry dates.\n• **2. Buy (Transaction Phase)**: Making the actual payment safely, demanding a genuine **receipt**, and checking change and warranty conditions.\n• **3. Use (Consumption Phase)**: Utilizing the product according to manufacturer instructions, avoiding wastage, and maximizing product lifespan.\n• **4. Dispose (End-of-Life Phase)**: Responsibly managing leftover packaging, bottles, and food scraps through **recycling**, **reusing**, or **organic composting** to protect the environment."
                        }
                    }
                ],
                # Page 4: 5 Types of Buyers in the Marketplace
                [
                    {
                        "type": "comparison_table",
                        "title": "Evaluation of 5 Buyer Types in the Market",
                        "content": {
                            "title": "The 5 Distinct Buyer Profiles",
                            "headers": ["Buyer Type", "Shopping Behaviour & Mindset", "Key Strength", "Financial Risk / Warning"],
                            "rows": [
                                ["1. Need-Based Customer", "Shops strictly with a written checklist to purchase pre-planned household essentials", "High financial discipline; avoids impulse traps and saves money", "May miss genuine opportunities or seasonal volume discounts"],
                                ["2. Impulse Shopper", "Buys items spontaneously on emotion or visual attraction without prior planning", "Quick decision maker; enjoys shopping excitement", "High risk of financial regret, wasted money, and neglected household needs"],
                                ["3. Discount Customer", "Shops exclusively during clearance sales, price cuts, and special promotional offers", "Actively seeks low prices; stretches the household shopping budget", "Risk of buying substandard or unneeded items merely because they are cheap"],
                                ["4. Loyal Customer", "Consistently purchases from a particular trusted shopkeeper or brand over time", "Enjoys reliable personalized service, trust, and potential seller credit", "May fail to notice better prices or newer innovations offered by rivals"],
                                ["5. Wandering Consumer", "Walks through markets with no specific purchase goal, driven by curiosity and leisure", "Gathers market trend knowledge and observes product varieties", "Frequently converts into an unplanned impulse buyer when exposed to attractive displays"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Financial Wisdom",
                        "content": {
                            "title": "The Discount Buyer's Trap",
                            "text": "Buying an item you do not need simply because it has a **'50% OFF'** sticker is not saving money—it is spending money you would have otherwise kept!"
                        }
                    }
                ],
                # Page 5: The 5 Roles of a Consumer in Household Purchases
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 5 Consumer Purchasing Roles in a Household",
                        "content": {
                            "title": "The 5 Consumer Purchasing Roles in a Household",
                            "caption": "Flowchart showing how a household purchase moves through Initiator, Influencer, Decision Maker, Buyer, and User."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Worked Example: The Family Textbook Purchase",
                        "content": {
                            "title": "How Different Household Members Play Purchasing Roles",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "The Initiator (Identifies Need)",
                                    "description": "**Zawadi (Grade 8 Student)** realizes her class is beginning Home Science projects and tells her family she needs a textbook."
                                },
                                {
                                    "step_number": 2,
                                    "title": "The Influencer (Guides Choice)",
                                    "description": "**Mr. Mwangi (Home Science Teacher)** advises the family to buy the KICD-approved syllabus edition because of its clear practical guides."
                                },
                                {
                                    "step_number": 3,
                                    "title": "The Decision Maker (Approves Purchase)",
                                    "description": "**Zawadi's Mother** reviews the household budget and authorizes the purchase of the recommended textbook edition."
                                },
                                {
                                    "step_number": 4,
                                    "title": "The Buyer (Executes Transaction)",
                                    "description": "**Zawadi's Father** walks to the local bookshop, pays 600 KES, inspects the pages, and collects the official receipt."
                                },
                                {
                                    "step_number": 5,
                                    "title": "The User (Consumes Product)",
                                    "description": "**Zawadi** reads the book, covers it neatly with plastic wrap, and completes her daily Home Science coursework."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On Shopping Audit Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: The 1-Week Household Shopping Audit",
                        "content": {
                            "title": "Activity: Audit Your Personal & Household Buying Habits",
                            "instructions": "In your notebook, create a 5-column ledger titled **'Household Consumer Audit'**:\n\n• **Column 1**: Date of Purchase\n• **Column 2**: Item Purchased\n• **Column 3**: Classification (**Need** vs. **Want**)\n• **Column 4**: Buyer Profile (**Need-Based**, **Impulse**, **Discount**, **Loyal**, **Wandering**)\n• **Column 5**: Consumer Role You Played (**Initiator**, **Influencer**, **Decision Maker**, **Buyer**, **User**)\n\nAudit 5 purchases made in your home this week and calculate the percentage spent on true essentials!"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Single-Person Multi-Roles",
                        "content": {
                            "title": "Can One Person Play All 5 Roles?",
                            "text": "Yes! When you feel hungry after school (**Initiator**), decide to buy roasted maize instead of candy (**Influencer**), choose Mama Sarah's stall (**Decision Maker**), pay 30 KES with your own pocket money (**Buyer**), and eat the maize (**User**), you have seamlessly executed all five consumer roles independently."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Summary
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Consumer Awareness & Buying Habits",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Consumer awareness** is knowing your rights and facts to make cost-effective, safe purchasing choices.",
                                "**Needs** are survival essentials that must be budgeted first; **wants** are elective desires that can be postponed.",
                                "The **4-stage consumer cycle** encompasses **Select → Buy → Use → Dispose** (responsible disposal protects our ecology).",
                                "Understanding **buyer profiles** and **household purchasing roles** prevents wasteful impulse spending."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Consumer Cycle Recall Helper",
                        "content": {
                            "title": "Remember 'S-B-U-D'",
                            "tip": "**S**elect choices carefully, **B**uy with a receipt, **U**se without waste, **D**ispose or recycle responsibly!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Consumer Awareness & Budgeting",
                        "content": {
                            "question": "Wanjiku has 500 shillings. She must buy cooking flour and milk for the family's dinner, but at the market, she notices an attractive, discounted plastic toy that costs 350 shillings. According to consumer awareness and wise buying principles, what should Wanjiku do?",
                            "options": [
                                "Buy the discounted toy immediately because clearance discounts are rare, and drink plain water for dinner.",
                                "Purchase the essential cooking flour and milk first to satisfy basic household survival needs, and save any remaining balance for future wants.",
                                "Spend 250 shillings on lottery tickets to try and double her money.",
                                "Wander around the market until the shops close without buying anything."
                            ],
                            "correct_index": 1,
                            "explanation": "Wise consumerism dictates that basic household survival needs (food staples like flour and milk) must always be secured and funded before any money is spent on elective wants (like toys or decorative items)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Market Competition & Consumer Protection
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Market Competition & Consumer Protection",
            "unit_description": "Meaning of market, competition & competitor, 5 factors influencing market competition (Price, Quality, Variety, Innovation, Promotion), Fair vs Unfair trade practices, benefits & consequences, and consumer protection.",
            "lesson_title": "Market Competition & Consumer Protection",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "The Battle of the Stalls: How Markets Work",
                        "content": {
                            "title": "The Battle of the Stalls: How Markets Work",
                            "caption": "Neighboring retail vegetable and grocery stalls competing to attract customers through fresh quality and fair prices."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Market Competition",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **market**, **competitor**, and **market competition**, explaining how competition prevents monopolies.",
                                "Analyze the **5 core factors** that drive marketplace competition: **Price**, **Quality**, **Variety**, **Innovation**, and **Promotion**.",
                                "Contrast **fair competition** practices with destructive **unfair trade practices** (counterfeiting, hoarding, false advertising).",
                                "Evaluate consumer rights and utilize **KEBS standardization marks** to safeguard family health."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Market and Market Competition?",
                        "content": {
                            "title": "The Dynamics of Trade",
                            "text": "• **Market**: Any medium or environment—physical (open-air market, supermarket) or digital (e-commerce app, SMS trading)—where buyers and sellers interact to exchange goods and services.\n• **Competitors**: Rival sellers offering identical or similar goods to the same target customers.\n• **Market Competition**: The continuous rivalry between businesses to win buyer patronage. Healthy competition is vital because it prevents **monopolies** (where a single seller dictates high prices and poor quality without consequence)."
                        }
                    }
                ],
                # Page 2: The 5 Core Factors Driving Market Competition
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 5 Core Factors Driving Market Competition (P-Q-V-I-P)",
                        "content": {
                            "title": "The 5 Core Factors Driving Market Competition",
                            "caption": "Interactive matrix showing the 5 competitive dimensions: Price, Quality, Variety, Innovation, and Promotion."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "How Businesses Compete: The 5 Core Factors",
                        "content": {
                            "title": "The 5 Factors Influencing Competition",
                            "headers": ["Competitive Factor", "How It Works", "Everyday Retail Example", "Benefit to the Consumer"],
                            "rows": [
                                ["1. Price", "Lowering prices or offering budget-friendly package sizes", "Selling a packet of salt for 25 KES instead of 30 KES", "Direct cost savings on household budgets"],
                                ["2. Quality", "Using superior, durable, hygienic, or organic ingredients", "Selling freshly picked, unblemished Grade 1 tomatoes", "Better nutrition, longer product lifespan, and safety"],
                                ["3. Variety", "Providing different flavors, colors, sizes, and dietary options", "Offering brown bread, white bread, and gluten-free bread", "Wider choices tailored to individual family preferences"],
                                ["4. Innovation", "Introducing novel features, easier packaging, or advanced tech", "Milk packaged in resealable screw-cap cartons instead of simple pouches", "Greater convenience, spill prevention, and extended freshness"],
                                ["5. Promotion", "Advertising, buy-one-get-one-free deals, and loyalty points", "Giving a free dishwashing sponge with every large detergent tub", "Extra value bonuses and awareness of new offerings"]
                            ]
                        }
                    }
                ],
                # Page 3: Fair vs. Unfair Market Competition
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Split-Screen: Fair Trade vs. Deceptive Unfair Competition",
                        "content": {
                            "title": "Split-Screen: Fair Trade vs. Deceptive Unfair Competition",
                            "caption": "Side-by-side comparison of an honest, rule-abiding retail stall versus a deceptive counterfeiting and hoarding stall."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Contrasting Fair Trade with Unfair Trade Practices",
                        "content": {
                            "title": "Fair vs. Unfair Competition",
                            "headers": ["Feature / Practice", "Fair Market Competition (Honest)", "Unfair Market Competition (Cheating)"],
                            "rows": [
                                ["Product Quality & Branding", "Authentic, genuine goods bearing legitimate standardization marks (KEBS)", "Selling **counterfeit or fake goods** with copied, misspelled brand logos (e.g. 'O0MO')"],
                                ["Advertising & Claims", "Truthful, accurate descriptions of product ingredients and performance", "**Misleading advertisements** making false claims (e.g. 'Cures all diseases in 2 days')"],
                                ["Supply & Availability", "Open stock distribution with honest pricing based on real costs", "**Artificial hoarding**: Secretly hiding basic necessities to force prices to double"],
                                ["Pricing Ethics", "Competitive, independent price setting reflecting fair market value", "**Price fixing / Collusion**: Rival sellers secretly agreeing to maintain artificially high prices"],
                                ["Long-Term Outcome", "Builds customer trust, economic growth, and high product standards", "Destroys honest local businesses, exploits buyers, and endangers public health"]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example — The Market Inspector's Trade Audit
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Diagnosing 3 Local Business Scenarios",
                        "content": {
                            "title": "The Market Inspector's Diagnostic Audit",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Scenario A: Mama Amani's Bakery",
                                    "description": "Mama Amani introduces a new whole-wheat flour recipe with fortified zinc and iron at 55 KES. **VERDICT: FAIR COMPETITION (Innovation & Quality)**. This provides healthy, genuine value to consumers."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Scenario B: Kiosk B's Hidden Sugar Bags",
                                    "description": "During a market delivery delay, Kiosk B hides 20 bags of sugar under the counter and tells customers: *'Sugar is completely out of stock in Kenya unless you pay triple price!'* **VERDICT: UNFAIR COMPETITION (Artificial Hoarding)**."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Scenario C: Stall C's Miracle Herbal Drink",
                                    "description": "Stall C sells bottled tap water mixed with brown food coloring labeled *'Instant Miracle Cure for Broken Bones & Toothache'*. **VERDICT: UNFAIR COMPETITION (Deceptive Advertising & Fraud)**."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Benefits of Fair Competition & KEBS Quality Assurance
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Consumer Protection & KEBS Quality Assurance Verification Flow",
                        "content": {
                            "title": "The Consumer Protection & KEBS Verification Flow",
                            "caption": "Flowchart showing how KEBS Standardization Marks, SMS Verification, and Expiry Checks protect consumers."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Benefits of Fair Competition vs. Consequences of Unfair Trade",
                        "content": {
                            "title": "Why Fair Markets Protect the Entire Community",
                            "text": "• **Benefits of Fair Competition**:\n  1. **Affordability**: Continuous rivalry drives lower, fairer prices.\n  2. **Superior Quality**: Businesses invest in durability, hygiene, and nutrition to retain buyers.\n  3. **Product Innovation**: Encourages new packaging designs, green biodegradable materials, and better recipes.\n  4. **Consumer Sovereignty**: Buyers enjoy wide choices and respectful customer service.\n\n• **Consequences of Unfair Competition**:\n  1. **Financial Exploitation**: Consumers pay high prices for substandard, diluted, or underweight goods.\n  2. **Health Hazards**: Counterfeit medicines, unpasteurized dairy, and adulterated food oils cause serious illnesses.\n  3. **Collapse of Honest Traders**: Cheating sellers undercut honest businesses with dangerous fakes."
                        }
                    }
                ],
                # Page 6: Hands-On Consumer Protection Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Package Label & Quality Inspection",
                        "content": {
                            "title": "Activity: The 4-Point Product Label Check",
                            "instructions": "Pick any 2 packaged food or hygiene products at home or school and inspect them for the **4 Essential Consumer Protection Markers**:\n\n1. **Standardization Mark**: Look for the official **KEBS (Kenya Bureau of Standards)** diamond mark.\n2. **Manufacturer Details**: Clear name, physical address, and customer care contact.\n3. **List of Ingredients**: Transparent breakdown of contents (check for allergens or artificial preservatives).\n4. **Date Markings**: Manufacturing date (**MFG**) and Best-Before / Expiry Date (**EXP**).\n\nRecord your findings in your Home Science project notebook."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Legal Consumer Right",
                        "content": {
                            "title": "Right to Redress and Genuine Receipts",
                            "text": "As a consumer, you have the legal right to return damaged, expired, or substandard goods for a replacement or full refund. **Always demand and keep your purchase receipt** as legal proof of transaction!"
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Market Competition & Fair Trade",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Market competition** prevents harmful monopolies and guarantees lower prices and higher quality for consumers.",
                                "The **5 competitive factors** are **Price**, **Quality**, **Variety**, **Innovation**, and **Promotion** (**P-Q-V-I-P**).",
                                "**Fair competition** relies on honest efficiency, while **unfair competition** uses counterfeits, hoarding, and deceptive claims.",
                                "Always check for **KEBS standardization marks**, intact seals, and **expiry dates** before purchasing packaged goods."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "5 Competitive Factors Helper",
                        "content": {
                            "title": "Remember 'P-Q-V-I-P'",
                            "tip": "**P**rice, **Q**uality, **V**ariety, **I**nnovation, **P**romotion!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Market Competition & Fair Trade",
                        "content": {
                            "question": "A neighborhood shopkeeper invents a new natural herbal washing powder that removes tough stains without harming hands, sells it in biodegradable paper bags at a fair price, and gives clear ingredient disclosures. What type of market practice is this?",
                            "options": [
                                "Unfair competition, because inventing new products confuses traditional buyers.",
                                "Fair market competition, because the seller uses genuine product innovation, quality improvement, and honest environmental packaging to win customers.",
                                "Predatory pricing and illegal counterfeiting.",
                                "Artificial hoarding of cleaning supplies."
                            ],
                            "correct_index": 1,
                            "explanation": "Fair market competition occurs when a business competes legitimately through product innovation, superior quality, honest packaging, and customer-focused value, which directly benefits consumers."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_home_science_topic2(replace=False):
    """Executes the atomic ingestion of CBC Grade 8 Home Science Topic 2."""
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 8 HOME SCIENCE — TOPIC 2: CONSUMER EDUCATION")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade 8
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 8").first()
    assert grade, "Grade 'Grade 8' not found under CBC!"
    print(f"[*] Grade 8: ID {grade.id} (Level {grade.level})")

    # 3. Resolve Subject: Home Science
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' not found under Grade 8!"
    print(f"[*] Subject: {subject.name} (ID {subject.id})")

    # 4. Resolve Topic: Consumer Education (Order: 2)
    topic_name = "Consumer Education"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=2,
            description="Comprehensive CBC Grade 8 module on consumer awareness, household needs vs wants, the 4-stage consumer behaviour cycle, buyer types, consumer roles, and market competition dynamics."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic2_curriculum()
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            unit_order = unit_data["unit_order"]
            unit_name = unit_data["unit_name"]
            unit_desc = unit_data["unit_description"]
            lesson_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            learning_unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name, "description": unit_desc}
            )

            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.version = 1
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"\n  [+] Ingesting Lesson {unit_order}: '{lesson.title}' (Lesson ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Page {page_idx}")
                for b_data in page_blocks:
                    b_type = b_data["type"]
                    b_title = b_data.get("title", first_block_title)
                    b_content = clean_dict(b_data.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_idx,
                        page_title=first_block_title,
                        title=b_title,
                        block_type=b_type,
                        component_type=b_type,
                        component_order=block_order,
                        order=block_order,
                        content=b_content,
                        metadata={}
                    )
                    block_order += 10
                    total_blocks += 1

            total_lessons += 1
            total_pages += lesson_page_count
            print(f"      [OK] Ingested {lesson_page_count} Pages ({len(lesson.blocks.all())} Blocks) for Unit {unit_order}.")

    print("\n" + "=" * 80)
    print("[SUCCESS] CBC Grade 8 Home Science Topic 2 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_cbc_grade8_home_science_topic2(replace=replace_flag)
