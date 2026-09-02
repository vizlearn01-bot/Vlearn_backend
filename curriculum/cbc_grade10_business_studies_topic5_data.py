"""
VLearn CBC Grade 10 Business Studies — Topic 5: Business Activities
Full Structured Lesson Card Definitions (Lessons 1 to 5)
"""

from curriculum.cbc_grade10_business_studies_topic5_svgs import (
    SVG_NEEDS_VS_WANTS,
    SVG_FACTORS_OF_PRODUCTION,
    SVG_SCARCITY_CHOICE_FLOW,
    SVG_BUSINESS_SECTORS_CHAIN,
    SVG_BUSINESS_ENVIRONMENT_PESTEL
)

TOPIC_5_LESSONS = [
    # =========================================================================
    # LESSON 1: Human Needs and Wants
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Human Needs and Wants",
        "unit_description": "The fundamental economic concepts of basic survival needs versus comfort wants, their distinguishing characteristics, and consumer decision-making.",
        "lesson_title": "Human Needs and Wants",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Everyday Consumer Transactions in a Kenyan Market",
                    "content": {
                        "title": "Household Shopping in Wangige Market, Kiambu",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "Shoppers in Wangige local market prioritizing staple foodstuffs and essential household goods before allocating remaining funds to non-essential items.",
                        "author": "Kristinabudiati",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define human needs, human wants, scarcity, and economic choice\n- Distinguish between essential survival needs and secondary comfort wants\n- Analyze key distinguishing characteristics of needs versus wants\n- Apply priority budgeting rules to real-world household and enterprise spending decisions"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Human Needs and Human Wants",
                    "content": {
                        "term": "Human Needs",
                        "definition": "The basic, essential goods and services that human beings must obtain in order to physically survive and maintain health."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Oxygen vs. Gold Analogy",
                    "content": {
                        "text": "Think of human survival:\n\n- **Oxygen** is something you absolutely must have. If deprived of oxygen for even five minutes, survival is impossible. Oxygen is a fundamental **need**.\n- **Gold**, on the other hand, is valuable, prestigious, and aesthetically pleasing. Wearing a gold ring enhances status and pleasure, but living without it causes zero physical harm. Gold is a **want**.\n\nIn economic life, **needs** (clean water, unga, shelter, primary healthcare) are limited and essential for survival, whereas **wants** (flagship smartphones, designer apparel, luxury entertainment) are unlimited desires that provide comfort, pleasure, or social prestige."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Human Needs vs. Human Wants Spectrum",
                    "content": {
                        "title": "Economic Spectrum of Needs and Wants",
                        "caption": "Vector diagram illustrating the fundamental divide between essential survival needs and unlimited comfort wants filtered through scarcity and budget constraints.",
                        "svg_content": SVG_NEEDS_VS_WANTS
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Table
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Analysis: Needs vs. Wants",
                    "content": {
                        "headers": ["Economic Feature", "Human Needs", "Human Wants", "Practical Kenyan Example"],
                        "rows": [
                            ["Essentiality", "Crucial for physical survival", "Desired for comfort, luxury & prestige", "Maize meal (Need) vs. Cold Soda (Want)"],
                            ["Quantity / Satiation", "Limited and definable per person", "Unlimited, insatiable, and recurring", "2 litres of water/day vs. unlimited shoe collections"],
                            ["Universality", "Universal to all human beings", "Subjective; varies with income & culture", "Basic shelter (All) vs. DStv Premium subscription"],
                            ["Urgency", "Immediate; cannot be postponed", "Can be delayed without physical injury", "Emergency medicine vs. Buying a sports watch"],
                            ["Consequence of Deprivation", "Physical suffering, illness, or death", "Disappointment or minor inconvenience", "Malnutrition vs. Missing a cinema movie"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Priority Budgeting
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Juma's Back-to-School Budget Allocation",
                    "content": {
                        "intro": "Juma is a Grade 10 student in Nakuru with a fixed budget $B = \\text{KES } 2,500$. He lists four desired purchases before Term 2: Business Studies Textbook ($\\text{KES } 800$), School Uniform & Leather Shoes ($\\text{KES } 1,500$), Stylish Sports Watch ($\\text{KES } 1,200$), and Cafe Soda & Fries ($\\text{KES } 350$). Total requested = $\\text{KES } 3,850$.",
                        "steps": [
                            "**Step 1: Given Information:** Fixed budget $B = \\text{KES } 2,500$. Competing items: Textbook ($\\text{KES } 800$, Need), Uniform ($\\text{KES } 1,500$, Need), Sports Watch ($\\text{KES } 1,200$, Want), Cafe Meal ($\\text{KES } 350$, Want). Total requested spending = $\\text{KES } 3,850$.",
                            "**Step 2: Formula & Decision Rule:** Total Need Expenditure: $$C_{\\text{needs}} = \\sum \\text{Needs}$$. Remaining Surplus for Wants: $$B_{\\text{rem}} = B - C_{\\text{needs}}$$. A rational consumer funds wants only if $B_{\\text{rem}} \\ge C_{\\text{wants}}$.",
                            "**Step 3: Substitution:** Calculate total cost of essential needs: $$C_{\\text{needs}} = 800 + 1,500 = \\text{KES } 2,300$$.",
                            "**Step 4: Calculation:** Compute remaining cash balance: $$B_{\\text{rem}} = \\text{KES } 2,500 - \\text{KES } 2,300 = \\text{KES } 200$$. Total cost of desired wants: $$C_{\\text{wants}} = 1,200 + 350 = \\text{KES } 1,550$$. Since $\\text{KES } 1,550 > \\text{KES } 200$, Juma cannot afford the wants.",
                            "**Step 5: Final Answer:** Juma buys the Business Studies Textbook and School Uniform for $\\text{KES } 2,300$, retains $\\text{KES } 200$ as contingency savings, and postpones the sports watch and cafe meal.",
                            "**Step 6: Economic Interpretation & Pitfall:** Priority spending ensures survival needs are met first under budget constraints. *Common Pitfall:* Satisfying luxury wants on impulse first, leaving inadequate capital for non-negotiable survival obligations."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Application: Supermarket Shelf Placement",
                    "content": {
                        "title": "Naivas and Quickmart Merchandising Strategy",
                        "text": "Kenyan retail giants like Naivas and Quickmart design their store layouts strictly around consumer needs and wants:\n\n- **Essential Needs Section:** High-turnover staple foodstuffs (flour, rice, cooking oil, milk, salt) and household hygiene goods are placed at the back or center of the supermarket. Customers must walk through the entire store to reach them.\n- **Impulse Wants Section:** Chocolates, sodas, luxury cosmetics, and fashion accessories are placed near the entrance and checkout queues to trigger impulse spending while shoppers wait in line."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Human Needs and Wants in Enterprise Economics",
                    "content": {
                        "title": "Needs vs Wants in Personal Finance & Business Economics",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Educational breakdown showing how businesses categorize consumer needs and wants to optimize pricing, stocking, and sales strategies."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Distinguishing Needs from Wants",
                    "content": {
                        "question": "Which of the following items represents a basic human need for an ordinary family in Kenya?",
                        "options": [
                            "A subscription to a premium digital satellite television service",
                            "Unprocessed maize flour (unga) and clean drinking water",
                            "A designer sports watch bought at an urban boutique",
                            "A high-end smartphone with a triple-lens camera"
                        ],
                        "correct": "B",
                        "explanation": "Maize flour and clean drinking water are essential nutritional requirements without which human physical health and survival cannot be maintained. Television subscriptions and designer accessories are comfort wants."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Characteristics of Human Wants",
                    "content": {
                        "question": "Why are human wants described by economists as 'insatiable' and 'unlimited'?",
                        "options": [
                            "Because they are fixed by nature and identical for all people across the world",
                            "Because failing to satisfy them immediately causes physical illness or death",
                            "Because as soon as one want is satisfied, new desires and higher living aspirations emerge",
                            "Because they require zero economic resources to produce"
                        ],
                        "correct": "C",
                        "explanation": "Human wants are unlimited because human desires constantly expand with income, technology, and lifestyle changes; satisfying one desire inevitably creates new ones."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Needs vs. Wants**: Needs are essential for physical survival and are limited in volume; wants are non-essential desires for comfort, prestige, and pleasure that are virtually unlimited.\n2. **Scarcity & Choice**: Limited income forces consumers and enterprises to prioritize urgent needs over postponable wants.\n3. **Commercial Implication**: Enterprises design their inventory and merchandising layouts based on the distinction between staple survival demand and impulse want-driven spending."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Economic Resources (Factors of Production)
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Economic Resources (Factors of Production)",
        "unit_description": "The four factors of production—Land, Labour, Capital, and Entrepreneurship—their unique characteristics, economic rewards, and role in value creation.",
        "lesson_title": "Economic Resources (Factors of Production)",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Agricultural Production in Rural Kenya",
                    "content": {
                        "title": "Smallholder Agricultural Enterprise in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Women_smallholder_farmers_in_Kenya.jpg",
                        "caption": "Kenyan smallholder agricultural producers combining fertile land, human manual labour, farming tools (capital), and enterprise management to produce fresh food crops.",
                        "author": "McKay Savage",
                        "licensing": "CC BY 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and define the four factors of production: Land, Labour, Capital, and Entrepreneurship\n- State and explain the corresponding economic rewards for each factor: Rent, Wages/Salaries, Interest, and Profit\n- Describe the distinctive physical and economic characteristics of each production factor\n- Calculate factor payments and entrepreneurial profit in commercial enterprises"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Economic Resources & Factors of Production",
                    "content": {
                        "term": "Factors of Production",
                        "definition": "The four primary economic inputs—Land, Labour, Capital, and Entrepreneurship—used by enterprises to produce goods and services."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Baking a Cake Analogy",
                    "content": {
                        "text": "Imagine baking a commercial cake for a customer:\n\n- **Flour, water, and sugar** represent the raw materials provided by nature (**Land**).\n- **The baker's physical mixing and baking effort** represents human work (**Labour**).\n- **The oven, mixing bowls, baking pans, and delivery van** represent man-made tools (**Capital**).\n- **The bakery owner** who came up with the business idea, rented the premises, hired the baker, took the financial risk, and manages customer orders represents **Entrepreneurship**.\n\nIf any one of these four ingredients is absent, no cake can ever reach the market. Producing any good or service requires combining all four factors of production."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Factors of Production & Factor Rewards",
                    "content": {
                        "title": "Architecture of the Four Factors of Production",
                        "caption": "Vector diagram illustrating Land (Rent), Labour (Wages), Capital (Interest), and Entrepreneurship (Profit) feeding into the Enterprise Engine.",
                        "svg_content": SVG_FACTORS_OF_PRODUCTION
                    }
                }
            ],
            # Card 4: Comparative Matrix & Characteristics Table
            [
                {
                    "type": "comparison_table",
                    "title": "The 4 Factors of Production: Comparative Matrix",
                    "content": {
                        "headers": ["Factor", "Nature of Supply", "Mobility", "Perishability", "Economic Reward", "Kenyan Enterprise Example"],
                        "rows": [
                            ["Land", "Fixed by nature; inelastic", "Geographically immobile", "Permanent / durable", "Rent", "Agricultural plot in Kiambu, Lake Victoria fishing waters"],
                            ["Labour", "Variable with population & skills", "Geographically & occupationally mobile", "Highly perishable (lost time cannot be saved)", "Wages / Salaries", "Poultry farm attendants, tea pickers, software coders"],
                            ["Capital", "Man-made; expandable through investment", "Mobile (tools/vehicles)", "Subject to physical depreciation & wear", "Interest", "Egg-grading machines, tractors, delivery vans, posho mills"],
                            ["Entrepreneurship", "Depends on business acumen & risk appetite", "Highly versatile & mobile across industries", "Tied to the owner's risk capacity", "Profit / (Loss)", "Farm founder Wanjiku, Equity Bank leader James Mwangi"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Factor Payment Breakdown
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Factor Payment & Profit Breakdown at Wanjiku's Poultry Farm",
                    "content": {
                        "intro": "Wanjiku operates a commercial poultry enterprise in Kiambu. In June, she generated a total revenue $TR = \\text{KES } 120,000$ from egg sales. Her monthly production costs are: Land lease payment = $\\text{KES } 15,000$, Wages for 3 farm attendants = $3 \\times \\text{KES } 18,000 = \\text{KES } 54,000$, and Loan interest on incubator machinery = $\\text{KES } 11,000$.",
                        "steps": [
                            "**Step 1: Given Information:** Total Revenue $TR = \\text{KES } 120,000$. Factor payments: Land (Rent $R = \\text{KES } 15,000$), Labour (Wages $W = \\text{KES } 54,000$), Capital (Interest $I = \\text{KES } 11,000$).",
                            "**Step 2: Formula:** Total Contractual Factor Costs: $$TC = R + W + I$$. Entrepreneurial Profit (Residual Reward): $$\\Pi = TR - TC$$.",
                            "**Step 3: Substitution:** Calculate total contractual factor payments: $$TC = 15,000 + 54,000 + 11,000 = \\text{KES } 80,000$$. Substitute into profit formula: $$\\Pi = 120,000 - 80,000$$.",
                            "**Step 4: Calculation:** $$\\Pi = \\text{KES } 40,000$$.",
                            "**Step 5: Final Answer:** Land earned $\\text{KES } 15,000$ (Rent), Labour earned $\\text{KES } 54,000$ (Wages), Capital earned $\\text{KES } 11,000$ (Interest), and Entrepreneur Wanjiku earned $\\text{KES } 40,000$ (Net Profit).",
                            "**Step 6: Economic Interpretation & Pitfall:** Entrepreneurship is the residual claimant that earns profit for bearing uncertainty. *Common Pitfall:* Assuming the entrepreneur's reward is guaranteed. If revenue falls below $\\text{KES } 80,000$, contractual payments (Rent, Wages, Interest) must still be paid, leaving the entrepreneur with a net loss."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Application: Agricultural Value Creation",
                    "content": {
                        "title": "Commercial Poultry Operations in Kiambu County",
                        "text": "Wanjiku's Kiambu poultry farm combines all four factors to sustain daily commercial output:\n\n- **Land:** A 1-acre plot leased near Kiambu town provides space for biosecure poultry houses and feed storage.\n- **Labour:** Three skilled attendants monitor poultry health, administer vaccinations, feed chickens, and clean sheds.\n- **Capital:** High-capacity automated incubation machines, insulated egg delivery crates, and an electric backup generator.\n- **Entrepreneurship:** Wanjiku herself, who negotiated hotel supply contracts, secured loan financing, and manages operational cash flow."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Four Factors of Production in Modern Enterprises",
                    "content": {
                        "title": "The 4 Factors of Production: Land, Labour, Capital, Entrepreneurship",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "Comprehensive explanation of how enterprises combine land, labour, capital, and entrepreneurship to generate value and earn factor rewards."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Factors of Production",
                    "content": {
                        "question": "A dairy farmer in Nyandarua purchases an automated electric milk-chilling tank. Under which factor of production is the chilling tank classified?",
                        "options": [
                            "Land",
                            "Labour",
                            "Capital",
                            "Entrepreneurship"
                        ],
                        "correct": "C",
                        "explanation": "The electric milk-chilling tank is a man-made, physical asset manufactured to increase production efficiency and prevent milk spoilage. Therefore, it is classified as Capital."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Economic Reward for Entrepreneurship",
                    "content": {
                        "question": "What is the specific economic reward received by an entrepreneur for organizing resources and taking business risks?",
                        "options": [
                            "Wages",
                            "Interest",
                            "Rent",
                            "Profit"
                        ],
                        "correct": "D",
                        "explanation": "Profit (or the risk of bearing a financial loss) is the residual economic reward for entrepreneurship. Rent pays for Land, Wages pay for Labour, and Interest pays for Capital."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **The 4 Factors**: Production requires Land (natural gifts), Labour (human effort), Capital (man-made physical tools), and Entrepreneurship (risk-bearing coordination).\n2. **Factor Rewards**: Land earns Rent, Labour earns Wages/Salaries, Capital earns Interest, and Entrepreneurship earns Profit.\n3. **Entrepreneurial Spark**: The entrepreneur acts as the coordinating catalyst that mobilizes the other three factors into an operating enterprise."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Scarcity, Choice, Opportunity Cost, and Scale of Preference
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Scarcity, Choice, Opportunity Cost, and Scale of Preference",
        "unit_description": "The fundamental economic chain of decision-making: how limited resources force rational prioritization, trade-offs, and opportunity cost evaluation.",
        "lesson_title": "Scarcity, Choice, Opportunity Cost, and Scale of Preference",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Consumer Decision-Making at Nairobi Maasai Market",
                    "content": {
                        "title": "Trade-offs and Consumer Choices in Kenyan Retail",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                        "caption": "Shoppers evaluating competing artisan goods at the Maasai Market in Nairobi, where limited pocket money forces buyers to prioritize purchases and forgo alternatives.",
                        "author": "khym54",
                        "licensing": "CC BY 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define scarcity, choice, opportunity cost, and scale of preference\n- Explain the logical sequence from scarcity to choice and opportunity cost\n- Construct an accurate scale of preference for personal and enterprise budgeting\n- Calculate and evaluate opportunity cost in real-world commercial scenarios"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Core Economic Decision Concepts",
                    "content": {
                        "term": "Opportunity Cost",
                        "definition": "The value of the next best alternative forgone or sacrificed when an economic choice is made."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Fork in the Road Analogy",
                    "content": {
                        "text": "Imagine walking along a road that splits into two paths: the left path leads to the football field, while the right path leads to the study library.\n\n- You have only one body and limited time (**Scarcity**).\n- You cannot walk down both paths simultaneously; you must choose one path (**Choice**).\n- If you choose to go to the football field, you automatically give up the quiet revision time and high test scores you would have earned at the library.\n- That forgone library revision value is your **Opportunity Cost**.\n\nEvery economic choice made by individuals, businesses, or governments involves a real sacrifice of the next best alternative."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Economic Decision Chain",
                    "content": {
                        "title": "From Scarcity to Opportunity Cost",
                        "caption": "Vector diagram illustrating the 4-stage pipeline: Scarcity forces a Scale of Preference, leading to Rational Choice and resulting in Opportunity Cost.",
                        "svg_content": SVG_SCARCITY_CHOICE_FLOW
                    }
                }
            ],
            # Card 4: Comparative Matrix & Decision Framework Table
            [
                {
                    "type": "comparison_table",
                    "title": "Decision-Making Framework Across Economic Actors",
                    "content": {
                        "headers": ["Economic Actor", "Scarce Resource", "Competing Desires", "Rational Choice", "Opportunity Cost (Sacrifice)"],
                        "rows": [
                            ["Student (Halima)", "Pocket money (KES 1,000)", "Calculator (KES 800) vs. Backpack (KES 750) vs. Novel (KES 450)", "Buy Calculator (KES 800) + Snacks (KES 200)", "New school backpack (next best alternative forgone)"],
                            ["Farmer (Narok)", "Capital budget (KES 25,000)", "Maize Seeds (15k), Fertilizer (12k), Labour (10k), Paint (6k)", "Buy Seeds (15k) + Casual Labour (10k)", "Organic fertilizer (highest-ranked sacrificed item)"],
                            ["Canteen Owner", "Surplus cash (KES 4,000)", "Beverage Cooler (+1.5k profit) vs. Stationery (+2.0k profit)", "Invest in Stationery stock (+KES 2,000 profit)", "Beverage Cooler and its +KES 1,500 profit boost"],
                            ["County Govt", "Development funds (KES 50M)", "Build Level-4 Hospital vs. Construct Tarmac Road", "Construct Level-4 Hospital in rural ward", "Upgraded tarmac road infrastructure forgone"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Scale of Preference Optimization
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Preparing a Scale of Preference for a Narok Maize Farmer",
                    "content": {
                        "intro": "A small-scale maize farmer in Narok has a working capital budget $B = \\text{KES } 25,000$. He needs to rank four competing farm expenses: Hybrid Maize Seeds ($\\text{KES } 15,000$), Organic Fertilizers ($\\text{KES } 12,000$), Casual Weeding Labour ($\\text{KES } 10,000$), and Barn Painting ($\\text{KES } 6,000$). Total cost of desires = $\\text{KES } 43,000$.",
                        "steps": [
                            "**Step 1: Given Information:** Available budget $B = \\text{KES } 25,000$. Desires: Seeds ($\\text{KES } 15,000$), Fertilizer ($\\text{KES } 12,000$), Casual Labour ($\\text{KES } 10,000$), Barn Paint ($\\text{KES } 6,000$). Total requested = $\\text{KES } 43,000$.",
                            "**Step 2: Construct the Scale of Preference (Priority Ranking):**\n1. Hybrid Maize Seeds ($\\text{KES } 15,000$) — Priority 1 (essential for planting)\n2. Organic Fertilizers ($\\text{KES } 12,000$) — Priority 2 (critical soil nutrition)\n3. Casual Weeding Labour ($\\text{KES } 10,000$) — Priority 3 (weed control)\n4. Repainting Storage Barn ($\\text{KES } 6,000$) — Priority 4 (cosmetic maintenance)",
                            "**Step 3: Budget Allocation Calculation:**\n- Allocate to Priority 1 (Seeds): Expenditure = $\\text{KES } 15,000$. Remaining Balance = $25,000 - 15,000 = \\text{KES } 10,000$.\n- Evaluate Priority 2 (Fertilizers): Cost is $\\text{KES } 12,000 > \\text{KES } 10,000$ (insufficient funds).\n- Evaluate Priority 3 (Casual Labour): Cost is $\\text{KES } 10,000 = \\text{KES } 10,000$ (exact fit).\n- Total Spent: $$15,000 + 10,000 = \\text{KES } 25,000$$. Remaining Balance = $\\text{KES } 0$.",
                            "**Step 4: Determine Final Choice:** The farmer purchases Hybrid Maize Seeds ($\\text{KES } 15,000$) and hires Casual Weeding Labour ($\\text{KES } 10,000$).",
                            "**Step 5: Identify Opportunity Cost:** The next best alternative that had to be forgone due to the budget constraint is **Organic Fertilizers ($\\text{KES } 12,000$)**.",
                            "**Step 6: Economic Interpretation & Pitfall:** Rational choice maximizes output under resource scarcity. *Common Pitfall:* Confusing opportunity cost with the total sum of all unchosen items (Fertilizer + Paint = $\\text{KES } 18,000$). Opportunity cost is strictly the single next best alternative sacrificed (Fertilizer = $\\text{KES } 12,000$)."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Application: Capital Allocation at a School Canteen",
                    "content": {
                        "title": "Opportunity Cost Decision at Nakuru Central Canteen",
                        "text": "A school canteen owner in Nakuru accumulated a cash surplus of $\\text{KES } 4,000$. She evaluated two mutually exclusive investment options:\n\n- **Option A (Beverage Cooler):** Purchase a second-hand mini-fridge for $\\text{KES } 4,000$ to sell chilled drinks, generating an expected net profit of $\\text{KES } 1,500$ per month.\n- **Option B (Stationery Stock):** Buy wholesale examination booklets, mathematical sets, and pens for $\\text{KES } 4,000$, generating an expected net profit of $\\text{KES } 2,000$ per month.\n\nApplying rational economics, she chose Option B because it yields a higher return on scarce capital. The **opportunity cost** of her decision is the forgone beverage cooler and its $\\text{KES } 1,500$ monthly profit."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Scarcity, Choice, and Opportunity Cost in Action",
                    "content": {
                        "title": "Scarcity, Opportunity Cost, and Choice Explained",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Educational animation showing how scarcity forces economic agents to rank wants on a scale of preference and evaluate the true opportunity cost of decisions."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Definition of Scale of Preference",
                    "content": {
                        "question": "What is a scale of preference in Business Studies?",
                        "options": [
                            "A legal scale used by supermarket cashiers to weigh vegetables",
                            "A list of unsatisfied wants arranged in descending order of urgency and importance",
                            "A government tax table that calculates business corporate taxes",
                            "A financial balance sheet showing total assets and liabilities"
                        ],
                        "correct": "B",
                        "explanation": "A scale of preference is a list of an individual's or business's unsatisfied wants arranged in order of priority, with the most urgent want at the top, enabling rational allocation of scarce resources."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Calculating Opportunity Cost",
                    "content": {
                        "question": "A carpenter has enough timber to build either a dining table (which sells for KES 15,000) or 4 study chairs (which sell for KES 14,000). He decides to build the dining table. What is the opportunity cost of his choice?",
                        "options": [
                            "The KES 15,000 revenue earned from the dining table",
                            "The 4 study chairs and their KES 14,000 market value that he sacrificed",
                            "The total combined value of both items (KES 29,000)",
                            "The cost of the timber used in building the table"
                        ],
                        "correct": "B",
                        "explanation": "The opportunity cost is the value of the next best alternative sacrificed when making a choice—in this case, the 4 study chairs valued at KES 14,000 that he gave up to make the dining table."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **The Decision Chain**: Scarcity $\\rightarrow$ Scale of Preference $\\rightarrow$ Choice $\\rightarrow$ Opportunity Cost.\n2. **Scale of Preference**: Prioritizes competing desires so that scarce funds are deployed to the highest-utility items first.\n3. **Real Cost of Choices**: Opportunity cost measures the value of the single next best alternative sacrificed, not the sum of all unchosen options."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Importance and Classification of Business Activities
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Importance and Classification of Business Activities",
        "unit_description": "Classifying business activities by economic sector (Primary, Secondary, Tertiary, Quaternary, Quinary), functional department, and scale, and their contributions to Kenya's economy.",
        "lesson_title": "Importance and Classification of Business Activities",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Manufacturing & Fabrication in Kenya's Jua Kali Sector",
                    "content": {
                        "title": "Secondary Sector Metal Fabrication in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Jua_Kali_cooking_pots.jpg",
                        "caption": "Jua Kali artisans manufacturing aluminium cooking pots from scrap metal in Nairobi, illustrating value addition in Kenya's secondary manufacturing sector.",
                        "author": "Leonard Kisuu",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define business activities and explain their role in satisfying human wants\n- Classify business activities across economic sectors: Primary, Secondary, Tertiary, and Quaternary\n- Differentiate business activities by internal function (production, marketing, finance, HR)\n- Calculate value addition across stages in a supply chain (e.g., the Kenyan tea industry)\n- Explain the socioeconomic importance of business activities to national development"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Business Activities and Economic Sectors",
                    "content": {
                        "term": "Business Activity",
                        "definition": "Any purposeful economic action involving the production, processing, distribution, or sale of goods and services to satisfy human needs and wants for profit."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Athletics Relay Race Analogy",
                    "content": {
                        "text": "Imagine a 4x100m athletics relay team:\n\n- **Runner 1** launches out of the blocks (extracting raw materials from the earth in the **Primary Sector**).\n- **Runner 2** takes the baton and runs the back curve (processing raw materials into finished physical goods in the **Secondary Sector**).\n- **Runner 3** carries the baton down the straight (transporting, financing, insuring, and retailing goods in the **Tertiary Sector**).\n- **Runner 4 / Coach** analyzes performance data and optimizes race splits (**Quaternary Sector**).\n\nIf any runner drops the baton or refuses to run, the team cannot finish the race. In the economy, businesses form an interconnected value chain that delivers finished goods to consumers."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Classification of Business Activities & The Value Chain",
                    "content": {
                        "title": "The 4 Economic Sectors and Value Addition",
                        "caption": "Vector diagram illustrating the progression from Primary Extraction to Secondary Manufacturing, Tertiary Distribution, and Quaternary Tech Analytics.",
                        "svg_content": SVG_BUSINESS_SECTORS_CHAIN
                    }
                }
            ],
            # Card 4: Comparative Matrix & Sector Taxonomy Table
            [
                {
                    "type": "comparison_table",
                    "title": "The Economic Sectors: Comparative Taxonomy",
                    "content": {
                        "headers": ["Economic Sector", "Core Focus", "Nature of Output", "Capital/Labour Intensity", "Key Kenyan Enterprise Examples"],
                        "rows": [
                            ["Primary Sector", "Direct extraction of natural resources", "Raw agricultural or mineral materials", "High land & labour intensity", "KTDA smallholder tea farms, Bamburi limestone quarry, Tiwi titanium mining"],
                            ["Secondary Sector", "Manufacturing, processing & construction", "Finished physical consumer & capital goods", "High capital & machinery intensity", "Bidia Oil Refineries, Del Monte pineapple canning, Dawa Pharmaceuticals"],
                            ["Tertiary Sector", "Commercial services, trade & logistics", "Intangible commercial services & retailing", "High labour & service skill intensity", "Naivas Supermarkets, Standard Gauge Railway (SGR), Equity Bank, Safaricom retail"],
                            ["Quaternary Sector", "Information tech, R&D, data analytics", "Intellectual property & digital software", "High intellectual & specialized skill", "Cellulant fintech, Twiga Foods supply analytics, Nairobi tech startups"],
                            ["Quinary Sector", "Highest-level policy & societal decisions", "Executive leadership & strategic governance", "Executive expertise & policy mandate", "Central Bank of Kenya (CBK) monetary policy committee, Cabinet ministries"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Value Addition in Supply Chains
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Value Addition Across the Kericho Black Tea Value Chain",
                    "content": {
                        "intro": "Trace the step-by-step value addition across economic sectors for $1\\text{ kg}$ of packaged Kericho black tea sold in a Nairobi supermarket:\n- Primary Sector (Farm gate green leaf harvest): $\\text{KES } 30\\text{/kg}$\n- Secondary Sector (Factory processing, drying, grading & packing): Sold to wholesaler at $\\text{KES } 180\\text{/kg}$\n- Tertiary Sector (Transport, warehousing, retail branding & shelf sale): Sold to final consumer at $\\text{KES } 300\\text{/kg}$",
                        "steps": [
                            "**Step 1: Given Information:** Selling price at each stage: Primary stage $P_1 = \\text{KES } 30$, Secondary stage $P_2 = \\text{KES } 180$, Tertiary stage $P_3 = \\text{KES } 300$. Initial raw material cost = $\\text{KES } 0$.",
                            "**Step 2: Formula:** Value Added at stage $i$: $$VA_i = \\text{Selling Price at Stage } i - \\text{Cost of Intermediate Inputs}$$. Total Final Value: $$V_{\\text{total}} = \\sum VA_i$$. Percentage Share: $$\\text{Share}_i = \\left(\\frac{VA_i}{V_{\\text{total}}}\\right) \\times 100\\%$$.",
                            "**Step 3: Substitution & Calculation of Value Added at each stage:**\n- Primary Sector Value Added: $$VA_1 = 30 - 0 = \\text{KES } 30$$\n- Secondary Sector Value Added: $$VA_2 = 180 - 30 = \\text{KES } 150$$\n- Tertiary Sector Value Added: $$VA_3 = 300 - 180 = \\text{KES } 120$$",
                            "**Step 4: Calculate Total Value & Sector Percentage Contributions:**\n- Total Economic Value: $$V_{\\text{total}} = 30 + 150 + 120 = \\text{KES } 300\\text{/kg}$$\n- Primary Share: $$\\frac{30}{300} \\times 100\\% = 10\\%$$\n- Secondary Share: $$\\frac{150}{300} \\times 100\\% = 50\\%$$\n- Tertiary Share: $$\\frac{120}{300} \\times 100\\% = 40\\%$$",
                            "**Step 5: Final Answer:** Total value created is $\\text{KES } 300\\text{/kg}$. Secondary manufacturing adds the largest value ($\text{KES } 150$, $50\\%$), followed by Tertiary commercial distribution ($\text{KES } 120$, $40\\%$), and Primary harvesting ($\text{KES } 30$, $10\\%$).",
                            "**Step 6: Economic Interpretation & Pitfall:** Raw commodity extraction captures minimal economic value; industrial processing and commercial distribution multiply GDP and wealth. *Common Pitfall:* Summing gross sales ($30 + 180 + 300 = \\text{KES } 510$) rather than net value added, causing double-counting in GDP accounting."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Application: The Tea Value Chain",
                    "content": {
                        "title": "The Economic Journey of Kericho Tea",
                        "text": "Every packet of Kenyan tea demonstrates cross-sector business synergy:\n\n- **Primary:** Smallholder farmers harvest green tea leaves on plantations across Kericho and Nandi counties.\n- **Secondary:** KTDA factories process, cut, ferment, dry, and package the tea into branded packets.\n- **Tertiary:** Logistics hauliers transport containers to Mombasa Port for international auction, while domestic distributors stock local supermarkets and kiosks.\n- **Quaternary:** Digital payment platforms and agricultural data systems track leaf weights, weather forecasts, and farmer payments via M-Pesa."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Sectors of the Economy and Business Activities",
                    "content": {
                        "title": "Sectors of the Economy: Primary, Secondary, Tertiary & Quaternary",
                        "youtube_id": "WqlX5z6k4eQ",
                        "url": "https://www.youtube.com/watch?v=WqlX5z6k4eQ",
                        "description": "Explains how the primary, secondary, tertiary, and quaternary sectors interact to create economic value and drive national GDP growth."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Classifying Manufacturing Enterprises",
                    "content": {
                        "question": "A company in Thika town buys fresh pineapples from local farmers, slices and cans them, and produces pineapple juice for export. Under which economic sector is this business classified?",
                        "options": [
                            "Primary Sector",
                            "Secondary Sector",
                            "Tertiary Sector",
                            "Quaternary Sector"
                        ],
                        "correct": "B",
                        "explanation": "Transforming raw agricultural commodities (fresh pineapples) into processed, packaged physical goods (canned fruit and juice) is a classic Secondary Sector (manufacturing/processing) activity."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Socioeconomic Importance of Business",
                    "content": {
                        "question": "Which of the following is a primary way that thriving business activities support government public spending in Kenya?",
                        "options": [
                            "By forcing the Central Bank to print more paper currency notes",
                            "By paying corporate taxes, customs duties, and VAT that fund public schools, roads, and hospitals",
                            "By eliminating all human wants across the entire population",
                            "By making all economic resources completely free and unlimited"
                        ],
                        "correct": "B",
                        "explanation": "Businesses generate tax revenue (Corporate Income Tax, Value Added Tax, Customs Duties) that the government uses to finance public infrastructure, education, and healthcare."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Sector Classification**: Primary (raw extraction), Secondary (manufacturing/processing), Tertiary (commercial services/trade), Quaternary (information/knowledge).\n2. **Value Addition**: Processing and marketing multiply raw commodity value, generating the largest shares of national wealth and employment.\n3. **Societal Value**: Businesses provide essential goods, create jobs, generate household incomes, and fund public infrastructure through tax contributions."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Micro and Macro Business Environment
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Micro and Macro Business Environment",
        "unit_description": "Internal micro environmental factors (controllable) versus external macro forces (PESTEL - uncontrollable) shaping enterprise performance and strategy.",
        "lesson_title": "Micro and Macro Business Environment",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Operating Environment in an Urban Kenyan Workshop",
                    "content": {
                        "title": "Artisan Enterprise in Kenya's Commercial Environment",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
                        "caption": "A metal fabricator in an urban Kenyan workshop interacting directly with clients and suppliers (micro environment) while adapting to steel price inflation and municipal licensing rules (macro environment).",
                        "author": "Harold Odhiambo Otieno",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define business environment and distinguish internal micro factors from external macro forces\n- Identify key micro environmental actors: customers, competitors, suppliers, employees, intermediaries, publics\n- Analyze the six PESTEL macro environmental forces (Political, Economic, Social, Tech, Environmental, Legal)\n- Calculate profit sensitivity under external macro shocks (inflation, import tariffs) and internal micro cost controls\n- Apply environmental scanning techniques to maintain enterprise viability in Kenya"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "The Business Environment & PESTEL Framework",
                    "content": {
                        "term": "Business Environment",
                        "definition": "The combination of internal direct factors (micro) and external surrounding forces (macro) that influence an enterprise's operations, decisions, and profitability."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Ship at Sea Analogy",
                    "content": {
                        "text": "Think of a commercial business as a cargo sailboat traversing the ocean:\n\n- **The Captain, crew, sails, rudder, engine, and cargo** represent the **Micro Environment**. They are inside the ship, and the captain exercises direct control over them.\n- **The ocean currents, gale winds, seasonal storms, and international maritime laws** represent the **Macro Environment (PESTEL)**. They are completely outside the ship. The captain cannot change the direction of the wind or stop a storm, but a skilled captain adjusts the sails to survive and steer the ship safely to port.\n\nIn business, entrepreneurs directly manage their internal micro relationships while scanning and adapting to uncontrollable macro PESTEL trends."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Business Environment: Micro vs. Macro Architecture",
                    "content": {
                        "title": "Concentric Rings of the Business Environment",
                        "caption": "Vector diagram illustrating the Enterprise Core surrounded by the Controllable Micro Environment and the Uncontrollable Macro PESTEL Perimeter.",
                        "svg_content": SVG_BUSINESS_ENVIRONMENT_PESTEL
                    }
                }
            ],
            # Card 4: Comparative Matrix & PESTEL Taxonomy Table
            [
                {
                    "type": "comparison_table",
                    "title": "Micro Environment vs. Macro Environment (PESTEL)",
                    "content": {
                        "headers": ["Environmental Dimension", "Micro Environment", "Macro Environment (PESTEL)", "Practical Kenyan Business Example"],
                        "rows": [
                            ["Scope of Influence", "Direct and immediate daily contact", "Broad industry-wide & economy-wide forces", "Otieno's tire supplier vs. Central Bank interest rates"],
                            ["Degree of Control", "High degree of managerial control", "Zero control (uncontrollable forces)", "Negotiating worker wages vs. Government import tariffs"],
                            ["Key Components", "Customers, Competitors, Suppliers, Employees, Intermediaries, Publics", "Political, Economic, Socio-Cultural, Technological, Environmental, Legal (PESTEL)", "Client feedback survey vs. National inflation rate"],
                            ["Strategic Action", "Direct operational management & contract negotiation", "Environmental scanning, forecasting & strategic adaptation", "Improving customer service vs. Adopting solar energy during power outages"],
                            ["Impact Speed", "Immediate impact on daily cash flow", "Gradual or sudden structural shifts", "A chief mechanic resigning vs. Introduction of KRA e-TIMS"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Environmental Sensitivity Analysis
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Profit Sensitivity Analysis at Otieno's Kisumu Bicycle Shop",
                    "content": {
                        "intro": "Otieno operates 'Otieno's Bikes' in Kisumu. Baseline monthly operations: Sells $Q_0 = 40$ bicycles at selling price $P = \\text{KES } 12,000$. Wholesale unit purchase cost from supplier is $V_0 = \\text{KES } 8,000$. Monthly fixed operating overheads $F_0 = \\text{KES } 80,000$.\n\n**Environmental Shifts Occur:**\n1. *Macro Legal/Economic Shift:* The government raises import tariffs on steel parts, increasing wholesale unit cost by $10\\%$ to $V_1 = 8,000 \\times 1.10 = \\text{KES } 8,800$.\n2. *Macro Economic Inflation:* Consumer disposable income contracts, reducing unit demand by $15\\%$ to $Q_1 = 40 \\times 0.85 = 34$ bicycles.\n3. *Micro Managerial Response:* Otieno cuts unnecessary store waste, reducing fixed overheads by $\\text{KES } 10,000$ to $F_1 = \\text{KES } 70,000$. Selling price is held at $\\text{KES } 12,000$.",
                        "steps": [
                            "**Step 1: Calculate Baseline Profit ($\\Pi_0$):**\n- Baseline Total Revenue: $$TR_0 = Q_0 \\times P = 40 \\times 12,000 = \\text{KES } 480,000$$\n- Baseline Total Variable Cost: $$TVC_0 = 40 \\times 8,000 = \\text{KES } 320,000$$\n- Baseline Total Cost: $$TC_0 = TVC_0 + F_0 = 320,000 + 80,000 = \\text{KES } 400,000$$\n- Baseline Net Profit: $$\\Pi_0 = TR_0 - TC_0 = 480,000 - 400,000 = \\text{KES } 80,000$$",
                            "**Step 2: Calculate New Revenue Under Macro Demand Contraction ($TR_1$):**\n$$TR_1 = Q_1 \\times P = 34 \\times 12,000 = \\text{KES } 408,000$$",
                            "**Step 3: Calculate New Costs Under Tariff Hike and Micro Cost Savings ($TC_1$):**\n- New Total Variable Cost: $$TVC_1 = Q_1 \\times V_1 = 34 \\times 8,800 = \\text{KES } 299,200$$\n- New Total Cost: $$TC_1 = TVC_1 + F_1 = 299,200 + 70,000 = \\text{KES } 369,200$$",
                            "**Step 4: Calculate New Profit ($\\Pi_1$) and Percentage Change:**\n$$\\Pi_1 = TR_1 - TC_1 = 408,000 - 369,200 = \\text{KES } 38,800$$\n$$\\Delta \\Pi = \\Pi_1 - \\Pi_0 = 38,800 - 80,000 = -\\text{KES } 41,200$$\n$$\\% \\text{ Drop} = \\left(\\frac{-41,200}{80,000}\\right) \\times 100\\% = -51.5\\%$$",
                            "**Step 5: Final Answer:** Otieno's monthly profit drops from $\\text{KES } 80,000$ to $\\text{KES } 38,800$ (a $51.5\\%$ contraction) as external macro tariff hikes and inflation squeeze margins, softened by internal overhead reductions.",
                            "**Step 6: Economic Interpretation & Pitfall:** Uncontrollable macro forces directly erode operating margins. Enterprises must proactively scan PESTEL trends to adjust pricing and cost structures before losses occur. *Common Pitfall:* Ignoring external macro indicators until working capital is completely depleted."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Application: Otieno's Kisumu Bicycle Shop",
                    "content": {
                        "title": "Navigating Environmental Pressures in Kisumu",
                        "text": "Otieno's bicycle sales and repair enterprise in Kisumu operates amid dynamic micro and macro pressures:\n\n- **Micro Management:** Otieno negotiates bulk discounts with local frame suppliers, trains his two mechanics in customer care, and runs loyalty discounts for local boda-boda riders.\n- **Macro Adaptation:** When the County Government introduced dedicated non-motorized cycling lanes (Political/Legal), bicycle commuting surged. Otieno capitalized on this trend by stocking affordable commuter helmets and safety lights."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding the Micro and Macro Business Environment",
                    "content": {
                        "title": "Business Environment: Micro Factors and PESTEL Macro Analysis",
                        "youtube_id": "7_j5N5V1N9c",
                        "url": "https://www.youtube.com/watch?v=7_j5N5V1N9c",
                        "description": "Explores how successful enterprises monitor internal micro stakeholders and adapt to external PESTEL macro factors to sustain profitability."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Categorizing Business Environmental Forces",
                    "content": {
                        "question": "The Central Bank of Kenya raises the benchmark interest rate, increasing commercial bank loan borrowing costs for all businesses across the country. Under which environmental category does this event fall?",
                        "options": [
                            "Internal Micro Environment",
                            "Macro Economic Environment",
                            "Micro Competitor Factor",
                            "Internal Corporate Culture"
                        ],
                        "correct": "B",
                        "explanation": "Central Bank interest rate adjustments represent an economy-wide monetary force over which individual businesses have zero control. Therefore, it is classified as a Macro Economic Factor."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Micro vs. Macro Control",
                    "content": {
                        "question": "Which of the following business factors is directly controllable by the management of a retail enterprise?",
                        "options": [
                            "National statutory changes in Value Added Tax (VAT) rates",
                            "Global crude oil price fluctuations affecting national fuel prices",
                            "The quality of customer service and staff training provided to store shoppers",
                            "Shifts in national demographic age distribution"
                        ],
                        "correct": "C",
                        "explanation": "Customer service quality and internal employee training are micro, internal factors that business management directly controls and manages. Tax rates, global oil prices, and demographic shifts are external macro forces."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Two Environmental Spheres**: Micro environment consists of direct, controllable factors (customers, suppliers, competitors, employees); Macro environment consists of broad, uncontrollable forces (PESTEL).\n2. **PESTEL Analysis**: Systematically tracks Political, Economic, Socio-Cultural, Technological, Environmental, and Legal trends.\n3. **Strategic Resilience**: Successful entrepreneurs actively manage internal micro operations while scanning the macro environment to seize opportunities and mitigate risks."
                    }
                }
            ]
        ]
    }
]
