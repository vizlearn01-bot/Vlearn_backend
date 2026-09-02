"""
VLearn CBC Grade 10 Business Studies — Topic 6: Types of Business Ownership
Full Structured Lesson Card Definitions (Lessons 1 to 16)
"""

from curriculum.cbc_grade10_business_studies_topic6_svgs import (
    SVG_SOLE_PROPRIETORSHIP_CHARACTERISTICS,
    SVG_SOLE_TRADER_FORMATION_WORKFLOW,
    SVG_SOLE_TRADER_FINANCE_SPECTRUM,
    SVG_SOLE_TRADER_TRADEOFFS_MATRIX,
    SVG_PARTNERSHIP_STRUCTURE_AND_LIABILITY,
    SVG_PARTNERSHIP_DEED_ARCHITECTURE,
    SVG_PARTNERSHIP_FINANCE_AND_EXPANSION,
    SVG_PARTNERSHIP_VS_SOLE_TRADER_MATRIX,
    SVG_COOPERATIVE_SEVEN_PRINCIPLES,
    SVG_TYPES_OF_COOPERATIVES_TAXONOMY,
    SVG_COOPERATIVE_GOVERNANCE_STRUCTURE,
    SVG_COOPERATIVE_FINANCE_CAPITAL_FLOW,
    SVG_COOPERATIVE_BENEFITS_AND_CHALLENGES,
    SVG_MASTER_OWNERSHIP_COMPARISON_MATRIX,
    SVG_LOCAL_ECONOMIC_DEVELOPMENT_ECOSYSTEM,
    SVG_OWNERSHIP_DECISION_TREE
)

TOPIC_6_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Characteristics of a Sole Proprietorship
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Sole Proprietorship: Meaning and Characteristics",
        "unit_description": "Single-owner enterprise structure, legal identity, unlimited liability, operational control, and profit retention in the Kenyan micro-enterprise sector.",
        "lesson_title": "Meaning and Characteristics of a Sole Proprietorship",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Micro-Enterprise Retail Kiosk in Kenya",
                    "content": {
                        "title": "Roadside Commercial Kiosk in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Banana_Street_Vendor_Kenya.jpg",
                        "caption": "A small independent sole trader operating an everyday retail venture, illustrating single-person ownership and localized commercial agility.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a sole proprietorship (sole trader) within the Kenyan business environment\n- Explain the concept of 'No Separate Legal Entity' and its direct relationship to unlimited liability\n- Analyze the defining operational and financial characteristics of a single-owner enterprise\n- Distinguish between personal assets and business liabilities in sole trader debt settlements"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Sole Proprietorship and Unlimited Liability",
                    "content": {
                        "term": "Sole Proprietorship",
                        "definition": "An unincorporated commercial enterprise owned, financed, controlled, and managed by a single individual who bears all risks and receives all net profits."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Solo Cyclist Analogy",
                    "content": {
                        "text": "Think of a sole proprietorship as a cyclist riding a bicycle alone:\n\n- **Complete Autonomy:** The rider steers in any direction, accelerates, or brakes without asking permission from anyone.\n- **Full Physical Effort:** All propulsion depends strictly on one person. If the rider tires or falls sick, the bicycle halts immediately.\n- **Direct Personal Impact:** If the bicycle crashes, the rider sustains 100% of the physical injuries directly. In business, this corresponds to **unlimited liability**—where personal assets (home, cattle, land) must settle unpaid business debts."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Sole Proprietorship Core Architecture",
                    "content": {
                        "title": "Core Defining Characteristics of a Sole Proprietor",
                        "caption": "Vector diagram illustrating the legal identity, unlimited personal liability, total operational autonomy, and profit retention mechanisms of single-owner firms.",
                        "svg_content": SVG_SOLE_PROPRIETORSHIP_CHARACTERISTICS
                    }
                }
            ],
            # Card 4: Characteristics Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Key Characteristics of a Sole Proprietorship",
                    "content": {
                        "headers": ["Characteristic", "Legal / Operational Mechanism", "Business Consequence", "Kenyan Real Example"],
                        "rows": [
                            ["Single Ownership", "One individual provides starting equity", "Owner holds 100% equity stake", "Kamau funding his Nakuru phone kiosk"],
                            ["No Separate Legal Entity", "Business and owner are legally identical", "Firm cannot sue or be sued in its own name", "Contracts signed under proprietor's personal name"],
                            ["Unlimited Liability", "No legal boundary on personal debt exposure", "Personal property can be attached by court bailiffs", "Auctioning personal household goods to pay stock debt"],
                            ["Sole Decision-Making", "Proprietor has absolute operational authority", "High market agility and instant price changes", "Adjusting vegetable prices during evening market rush"],
                            ["Lack of Continuity", "Enterprise tied strictly to owner's life", "Dissolves on owner's death or permanent incapacity", "Kiosk closes indefinitely when sole owner travels"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Sole Trader Debt Settlement Under Unlimited Liability",
                    "content": {
                        "intro": "Kamau operates 'Kamau Phone Clinic' as a sole proprietor in Nakuru. His business accumulates unpaid stock debts totaling $\\text{KES } 140,000$ to an electronics wholesaler. Due to an electrical fire, his kiosk stock and shop assets are liquidated for only $\\text{KES } 55,000$. The supplier secures a court order to recover the full debt.",
                        "steps": [
                            "**Step 1: Given Information:** Total business debt $D = \\text{KES } 140,000$. Liquidated business assets $A_{\\text{biz}} = \\text{KES } 55,000$. Owner's personal savings and private motorcycle value $A_{\\text{personal}} = \\text{KES } 120,000$.",
                            "**Step 2: Formula & Legal Rule:** Under the principle of unlimited liability (no separate legal entity), unrecovered business debt becomes personal debt: $$D_{\\text{personal}} = D - A_{\\text{biz}}$$. The owner must settle $D_{\\text{personal}}$ from personal wealth.",
                            "**Step 3: Substitution:** Calculate the remaining debt deficit: $$D_{\\text{personal}} = \\text{KES } 140,000 - \\text{KES } 55,000$$.",
                            "**Step 4: Calculation:** Compute the personal liability amount: $$D_{\\text{personal}} = \\text{KES } 85,000$$.",
                            "**Step 5: Final Answer & Settlement:** Kamau is legally required to pay $\\text{KES } 85,000$ from his personal savings or sell his personal motorcycle. Creditors cannot be turned away simply because the shop has zero remaining cash.",
                            "**Step 6: Economic Interpretation & Pitfall:** Unlimited liability means an entrepreneur risks personal bankruptcy for commercial failures. *Common Pitfall:* Assuming a registered business name protects personal assets from business creditors—only incorporated companies provide limited liability."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Kamau's Mobile Clinic in Nakuru",
                    "content": {
                        "title": "Operational Dynamics of a Transport Hub Phone Kiosk",
                        "text": "Kamau established 'Kamau Phone Clinic' near the Nakuru bus stage. By operating as a sole trader, he opens at 6:30 AM to catch early commuters, adjusts repair prices dynamically based on customer budgets, and keeps 100% of his daily surplus. However, during a 10-day illness, his kiosk remained completely shuttered, illustrating the acute lack of business continuity in single-owner enterprises."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Sole Proprietorship Characteristics and Legal Foundations",
                    "content": {
                        "title": "Understanding Sole Proprietorships in Business Economics",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Comprehensive explanation of sole proprietorship features, unlimited liability rules, and owner incentives in small enterprise management."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Unlimited Liability Application",
                    "content": {
                        "question": "A sole trader in Eldoret owes KES 80,000 to a grain supplier, but the shop account has only KES 15,000. Under Kenyan commercial law, what legal remedy does the supplier have?",
                        "options": [
                            "The supplier must write off the remaining KES 65,000 as a bad debt because the business has no cash",
                            "The supplier can legally obtain a court order to attach and sell the owner's personal household assets or vehicle to recover the KES 65,000",
                            "The County Government of Uasin Gishu is legally mandated to pay the balance on behalf of the trader",
                            "The supplier can convert the sole proprietorship into a public limited corporation"
                        ],
                        "correct": "B",
                        "explanation": "Because a sole proprietorship is not a separate legal entity, the owner has unlimited liability. Creditors have full legal right to seize personal property to satisfy outstanding commercial obligations."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Core Feature of Sole Trading",
                    "content": {
                        "question": "Which of the following is an inherent operational characteristic of a sole proprietorship?",
                        "options": [
                            "Decisions must be approved by an elected Board of Directors",
                            "Profits are shared among equity shareholders based on dividend votes",
                            "The business typically lacks perpetual succession and may dissolve upon the owner's death",
                            "The business is legally protected by the shield of limited liability"
                        ],
                        "correct": "C",
                        "explanation": "A sole proprietorship lacks perpetual succession because the existence of the enterprise is directly tied to the single owner. If the owner passes away or retires, the business dissolves unless formally re-established."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Single Equity Holder:** A sole proprietorship is owned, financed, and directed by exactly one person.\n2. **No Legal Persona:** There is no legal division between the entrepreneur and the enterprise.\n3. **Unlimited Liability:** The owner's personal wealth is fully exposed to settle commercial debts and legal claims.\n4. **Operational Agility vs. Fragility:** Total decision-making speed is balanced against heavy personal burden and zero permanent continuity."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Formation and Management of a Sole Proprietorship
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Sole Proprietorship: Formation and Management",
        "unit_description": "Legal formation procedures under the Business Names Act (Cap 499), digital eCitizen BRS registration, County Single Business Permits, and daily managerial workflows.",
        "lesson_title": "Formation and Management of a Sole Proprietorship",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Administrative Office in Kenya",
                    "content": {
                        "title": "Digital Business Registration in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "An entrepreneur submitting compliance documents online, showcasing the digital ease of business registration via the eCitizen portal in Kenya.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Outline the chronological steps required to legally register a sole proprietorship in Kenya\n- Explain the role of the Business Registration Service (BRS) on the eCitizen platform\n- Identify the necessity and procedure for acquiring a County Single Business Permit\n- Analyze the daily operational and management responsibilities of a sole trader"
                    }
                }
            ],
            # Card 2: Definitions & Legal Framework
            [
                {
                    "type": "definition_card",
                    "title": "Business Registration Service (BRS) & Single Business Permit",
                    "content": {
                        "term": "Single Business Permit",
                        "definition": "An official annual operating license issued by a County Government in Kenya authorizing a commercial enterprise to conduct lawful business within its jurisdiction."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Digital Formation under the Business Names Act (Cap 499)",
                    "content": {
                        "text": "Establishing a sole proprietorship in Kenya is fast and inexpensive:\n\n- **Business Name Registration:** If an entrepreneur trades under a name other than their official full legal name (e.g., 'Apex Mobile Solutions' instead of 'John Kamau'), they must register the name with the **Business Registration Service (BRS)** via **eCitizen**.\n- **County Licensing:** The entrepreneur must obtain a **Single Business Permit** from their respective County Government to ensure zoning and public health compliance.\n- **KRA Tax Compliance:** The proprietor uses their personal KRA PIN to declare income or pay monthly Turnover Tax (TOT)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Sole Trader Formation Workflow",
                    "content": {
                        "title": "Step-by-Step Legal Setup on eCitizen & County Level",
                        "caption": "Vector flowchart showing the 5 sequential stages from business concept to national name reservation, devolved licensing, tax setup, and store launch.",
                        "svg_content": SVG_SOLE_TRADER_FORMATION_WORKFLOW
                    }
                }
            ],
            # Card 4: Regulatory Stages Table
            [
                {
                    "type": "comparison_table",
                    "title": "Sole Proprietorship Formation Matrix in Kenya",
                    "content": {
                        "headers": ["Stage", "Regulatory Agency", "Statutory Requirement / Fee", "Typical Timeframe", "Key Compliance Outcome"],
                        "rows": [
                            ["1. Name Search", "BRS (eCitizen Portal)", "Online name availability check (KES 150)", "1 business day", "Name reservation confirmation"],
                            ["2. Name Registration", "BRS (eCitizen Portal)", "BN-2 registration application (KES 850)", "1 to 2 business days", "Certificate of Business Name"],
                            ["3. County Licensing", "County Revenue Department", "Single Business Permit (KES 3,000 - 10,000)", "1 to 3 business days", "Displayable Trade License"],
                            ["4. Public Health / Fire", "County Health Inspection", "Health certificate & fire inspection", "1 to 2 business days", "Safety & Hygiene Clearance"],
                            ["5. Tax Registration", "Kenya Revenue Authority (KRA)", "PIN linkage to iTax & TOT registration", "Instant online", "Tax Compliance Certificate (TCC)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Total Initial Compliance Costs for a Kiosk",
                    "content": {
                        "intro": "Wanjiku plans to open a fresh produce mini-grocery in Machakos Town. She needs to calculate the total statutory registration and compliance budget required before opening.",
                        "steps": [
                            "**Step 1: Given Information:** BRS Name Search fee $F_{\\text{search}} = \\text{KES } 150$. BRS Name Registration fee $F_{\\text{reg}} = \\text{KES } 850$. Machakos County Single Business Permit $F_{\\text{permit}} = \\text{KES } 4,500$. County Public Health Food Handler Certificate $F_{\\text{health}} = \\text{KES } 1,000$. County Signboard Mounting Levy $F_{\\text{sign}} = \\text{KES } 1,200$.",
                            "**Step 2: Formula:** Total Statutory Formation Outlay: $$C_{\\text{formation}} = F_{\\text{search}} + F_{\\text{reg}} + F_{\\text{permit}} + F_{\\text{health}} + F_{\\text{sign}}$$.",
                            "**Step 3: Substitution:** Calculate total compliance cost: $$C_{\\text{formation}} = 150 + 850 + 4,500 + 1,000 + 1,200$$.",
                            "**Step 4: Calculation:** Sum the individual statutory fees: $$C_{\\text{formation}} = \\text{KES } 7,700$$.",
                            "**Step 5: Final Answer:** Wanjiku requires exactly $\\text{KES } 7,700$ to achieve 100% legal compliance across national and county regulatory frameworks before purchasing retail inventory.",
                            "**Step 6: Economic Interpretation & Pitfall:** Low formation costs enable rapid formalization of informal businesses. *Common Pitfall:* Operating without a Single Business Permit to save cash, resulting in county enforcement penalties and business closure."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Fast eCitizen Setup for Naivasha Auto Spa",
                    "content": {
                        "title": "Transitioning from Informal Car Wash to Compliant Business",
                        "text": "Brian operated an informal roadside car wash in Naivasha. After facing county enforcement notices, he logged onto eCitizen, registered 'Naivasha Sparkle Auto Spa' for KES 1,000, paid for a devolved Single Business Permit (KES 5,000), and linked his merchant till to KRA. This formalization enabled him to secure corporate fleet washing contracts with local safari tour companies."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Registering a Business Name on eCitizen Kenya",
                    "content": {
                        "title": "Step-by-Step Guide to Business Name Registration in Kenya",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Practical demonstration of name reservation, BN-2 certificate acquisition, and county compliance for small business owners in Kenya."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Purpose of Name Registration",
                    "content": {
                        "question": "Why must an entrepreneur in Kenya register their trading name on eCitizen if it differs from their official baptismal and surname?",
                        "options": [
                            "To automatically convert the business into a limited liability corporate company",
                            "To comply with the Business Names Act (Cap 499) and protect the trading identity within national records",
                            "To avoid paying income tax to the Kenya Revenue Authority",
                            "To guarantee that the County Government will supply free electricity"
                        ],
                        "correct": "B",
                        "explanation": "Under the Business Names Act (Cap 499), any individual conducting business under a trade name other than their true full name must register it with the Business Registration Service (BRS) on eCitizen."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Single Business Permit Mandate",
                    "content": {
                        "question": "Which authority in Kenya is responsible for issuing the annual Single Business Permit required to operate a physical retail shop?",
                        "options": [
                            "The Central Bank of Kenya (CBK)",
                            "The respective County Government where the shop is located",
                            "The Ministry of Foreign Affairs",
                            "The Nairobi Securities Exchange (NSE)"
                        ],
                        "correct": "B",
                        "explanation": "Single Business Permits are devolved regulatory instruments issued annually by County Governments to license commercial operations within their geographical boundaries."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Digital Registration:** Business names are registered online via the BRS portal on eCitizen under the Business Names Act (Cap 499).\n2. **County Authorization:** A Single Business Permit is mandatory for physical retail trading in all 47 counties.\n3. **Managerial Multitasking:** The sole proprietor handles marketing, inventory, accounting, and customer service simultaneously.\n4. **Formalization Advantage:** Legal registration unlocks merchant bank accounts, Lipa Na M-Pesa merchant tills, and institutional contracts."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Sources of Finance for a Sole Proprietorship
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Sole Proprietorship: Sources of Finance",
        "unit_description": "Analyzing equity capital, personal savings, soft family loans, supplier trade credit, table banking/chamas, microfinance loans, and bank credit facilities.",
        "lesson_title": "Sources of Finance for a Sole Proprietorship",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Fresh Produce Retail Trader in Kenya",
                    "content": {
                        "title": "Micro-Capital Financing in Kenyan Local Markets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/06/Fruits_Vendor_Kenya.jpg",
                        "caption": "A small-scale fruit vendor managing daily inventory through personal savings and supplier trade credit in a busy market.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the primary internal and external sources of capital available to a sole proprietor\n- Compare personal savings, trade credit, microfinance loans, and commercial bank loans\n- Calculate weighted borrowing costs and effective repayment obligations for small enterprises\n- Evaluate the risk of debt financing against owner autonomy and cash flow stability"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Trade Credit and Microfinance Facilities",
                    "content": {
                        "term": "Trade Credit",
                        "definition": "A short-term commercial arrangement where a supplier allows a retail business to take goods immediately and pay at an agreed future date (typically 7 to 30 days)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Capital Spectrum: Equity vs. Debt",
                    "content": {
                        "text": "A sole proprietor must strategically construct their capital stack:\n\n- **Internal Equity (Personal Savings & Retained Cash):** Zero interest, 100% control, but slow to accumulate.\n- **Informal Debt (Family & Chamas):** Flexible terms, minimal collateral, but limited in size.\n- **Commercial Debt (MFIs & Banks):** Immediate large capital sums, but requires strict monthly repayments and pledges personal collateral."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Sole Trader Capital Spectrum",
                    "content": {
                        "title": "Hierarchy of Small Enterprise Financing Sources",
                        "caption": "Vector diagram mapping personal savings, soft loans, supplier credit, table banking, and commercial bank loans along risk, cost, and control axes.",
                        "svg_content": SVG_SOLE_TRADER_FINANCE_SPECTRUM
                    }
                }
            ],
            # Card 4: Comparative Sources Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Analysis of Sole Trader Finance Sources",
                    "content": {
                        "headers": ["Source of Finance", "Cost / Interest Rate", "Collateral Requirement", "Impact on Control", "Suitability for Sole Trader"],
                        "rows": [
                            ["Personal Savings", "0% (Opportunity cost)", "None required", "100% owner control retained", "Best for initial seed capital and tools"],
                            ["Family & Friends", "0% to 5% (Soft loan)", "None (Personal trust)", "Minimal (Risk to relationships)", "Emergency cash buffer and early stock"],
                            ["Supplier Trade Credit", "0% if paid on term", "Supplier relationship", "Zero loss of control", "Daily/weekly inventory restocking"],
                            ["Chama / Table Banking", "10% to 15% p.a.", "Group peer guarantee", "Peer oversight pressure", "Small equipment purchase and expansion"],
                            ["Microfinance (MFI)", "15% to 24% p.a.", "Household goods / Logbook", "Weekly repayment discipline", "High-turnover retail trading capital"],
                            ["Commercial Bank Loan", "14% to 20% + fees", "Land title deed / Car logbook", "Risk of asset foreclosure", "Large established expansion projects"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Capital Stack & Effective Interest Cost for an Electronics Stall",
                    "content": {
                        "intro": "Kevin needs $\\text{KES } 100,000$ to launch a phone accessories stall in Kisumu. He finances this using three distinct sources: Personal Savings ($\\text{KES } 40,000$), Interest-free Brother Loan ($\\text{KES } 25,000$), and a Microfinance Loan ($\\text{KES } 35,000$ at $14\\%$ flat annual interest repayable in 1 year).",
                        "steps": [
                            "**Step 1: Given Information:** Total capital $C = \\text{KES } 100,000$. Personal Savings $S = \\text{KES } 40,000$ at $0\\%$. Family Loan $L_{\\text{fam}} = \\text{KES } 25,000$ at $0\\%$. MFI Loan $P_{\\text{MFI}} = \\text{KES } 35,000$ at $r = 14\\%$ for $t = 1\\text{ year}$.",
                            "**Step 2: Formula:** MFI Interest Charge: $$I = P_{\\text{MFI}} \\times r \\times t$$. Total Repayment: $$R = P_{\\text{MFI}} + I$$. Effective Financing Cost over Total Capital: $$E = \\frac{I}{C} \\times 100\\%$$.",
                            "**Step 3: Substitution:** Calculate total MFI interest payable: $$I = \\text{KES } 35,000 \\times 0.14 \\times 1$$.",
                            "**Step 4: Calculation:** Compute interest and monthly instalment: $$I = \\text{KES } 4,900$$. Total MFI repayment = $35,000 + 4,900 = \\text{KES } 39,900$. Monthly MFI instalment = $\\frac{39,900}{12} = \\text{KES } 3,325$. Effective total capital cost = $\\frac{4,900}{100,000} \\times 100\\% = 4.9\\%$.",
                            "**Step 5: Final Answer:** Kevin successfully raises $\\text{KES } 100,000$, incurs an annual financing cost of only $\\text{KES } 4,900$, and must budget $\\text{KES } 3,325$ per month for loan service.",
                            "**Step 6: Economic Interpretation & Pitfall:** Blending zero-cost equity with modest debt minimizes borrowing drag on gross profits. *Common Pitfall:* Borrowing 100% of start-up capital from high-interest lenders before cash flow stabilizes."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Joyce's Tailoring Enterprise in Eldoret",
                    "content": {
                        "title": "Graduating from Table Banking to Commercial Equipment",
                        "text": "Joyce started an apparel repair shop in Eldoret using KES 15,000 in personal savings. To purchase an industrial overlock sewing machine (KES 45,000), she joined a women's table banking chama. The group provided an interest-friendly peer-guaranteed loan of KES 30,000 without requiring land title deeds. By repaying KES 2,800 monthly from increased tailoring revenues, she doubled her capacity without taking expensive commercial bank debt."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Sources of Finance for Micro and Small Enterprises in Kenya",
                    "content": {
                        "title": "How Small Businesses Fund Growth: Equity vs Debt in Kenya",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "Insightful breakdown of personal savings, supplier trade credit, chamas, and MFI borrowing strategies for small enterprise founders."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Trade Credit Suitability",
                    "content": {
                        "question": "A kiosk owner in Meru needs to restock maize flour and cooking oil every Monday but only receives cash when customers buy during the week. Which financing tool is most suitable?",
                        "options": [
                            "Taking a 5-year mortgage loan from a commercial bank",
                            "Utilizing 7-day supplier trade credit from a local wholesale distributor",
                            "Selling equity shares on the Nairobi Securities Exchange",
                            "Auctioning the shop's refrigeration equipment"
                        ],
                        "correct": "B",
                        "explanation": "Supplier trade credit provides short-term inventory financing without interest charges if settled on time, matching the fast cash conversion cycle of retail grocery sales."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Risk of High-Interest Debt",
                    "content": {
                        "question": "What is the primary danger when a sole proprietor finances a brand-new, unproven business entirely with high-interest microfinance loans?",
                        "options": [
                            "The business will automatically be nationalized by the government",
                            "Fixed weekly loan repayments must be made even if early revenues are zero, risking seizure of personal household collateral",
                            "The Central Bank of Kenya will ban the business from using mobile money",
                            "The owner will be forced to take on 20 partners"
                        ],
                        "correct": "B",
                        "explanation": "Microfinance loans demand strict weekly or monthly principal and interest repayments. In unproven start-ups with erratic initial revenues, debt service can force liquidation of personal assets."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **Equity Foundation:** Personal savings represent the safest start-up funding, eliminating debt pressure.\n2. **Working Capital via Trade Credit:** Supplier credit finances fast-moving inventory at zero interest if terms are respected.\n3. **Community Leverage:** Chamas and table banking provide accessible micro-credit backed by social peer guarantees.\n4. **Prudent Debt Sizing:** Commercial borrowing must be strictly aligned with verifiable cash flows to safeguard personal collateral."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Advantages and Disadvantages of a Sole Proprietorship
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Sole Proprietorship: Advantages and Disadvantages",
        "unit_description": "Comprehensive trade-off evaluation of operational autonomy, profit retention, and privacy against unlimited liability, capital constraints, and lack of continuity.",
        "lesson_title": "Advantages and Disadvantages of a Sole Proprietorship",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Vibrant Urban Market Stalls in Kenya",
                    "content": {
                        "title": "Everyday Trade-offs in Kenyan Commercial Hubs",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/48/Market_Kenya.jpg",
                        "caption": "Traders managing individual stalls in a bustling market, demonstrating direct customer engagement alongside long working hours.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Systematically evaluate the primary advantages and disadvantages of sole proprietorships\n- Explain how operational agility and business secrecy benefit micro-enterprises\n- Analyze the systemic risks of limited capital, sole risk-bearing, and lack of business continuity\n- Recommend strategic mitigation measures for sole traders facing burnout and expansion bottlenecks"
                    }
                }
            ],
            # Card 2: Definitions & Trade-off Principles
            [
                {
                    "type": "definition_card",
                    "title": "Business Secrecy and Operational Autonomy",
                    "content": {
                        "term": "Business Secrecy",
                        "definition": "The legal and practical ability of a sole trader to keep financial accounts, profit margins, recipe formulations, and business strategies entirely confidential without public reporting obligations."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Autonomy vs. Fragility Trade-off",
                    "content": {
                        "text": "The sole proprietorship is defined by powerful operational dualities:\n\n- **Maximum Motivation vs. Maximum Burden:** The owner keeps 100% of the profits, which drives extraordinary hard work, but this same owner must carry every administrative and physical burden alone.\n- **Complete Control vs. Limited Skills:** There is no boardroom friction or debate, but strategic decisions are constrained by the knowledge and experience of a single mind."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Sole Trader Trade-offs Matrix",
                    "content": {
                        "title": "Evaluating Strategic Strengths Against Core Vulnerabilities",
                        "caption": "High-contrast vector matrix contrasting 5 key operational advantages against 5 structural disadvantages of single-owner enterprises.",
                        "svg_content": SVG_SOLE_TRADER_TRADEOFFS_MATRIX
                    }
                }
            ],
            # Card 4: Trade-offs Matrix Table
            [
                {
                    "type": "comparison_table",
                    "title": "Detailed Strategic Trade-offs: Sole Proprietorship",
                    "content": {
                        "headers": ["Dimension", "Advantage (The Benefit)", "Disadvantage (The Cost)", "Practical Mitigation"],
                        "rows": [
                            ["Decision-Making", "Instant decisions; rapid market response", "Decisions lack peer scrutiny and debate", "Consult mentors and business advisors"],
                            ["Financial Reward", "100% of net profits kept by owner", "100% of losses and debts borne by owner", "Build dedicated cash contingency reserves"],
                            ["Confidentiality", "Complete privacy of books and trade secrets", "Private accounts make bank loan vetting harder", "Maintain audited management accounts"],
                            ["Customer Contact", "Direct personal touch creates loyal patrons", "Personal service means shop cannot open without owner", "Train and employ a trusted assistant"],
                            ["Capital Scalability", "Low initial capital required to open", "Severe ceiling on large asset expansion", "Form a partnership or incorporate later"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Opportunity Cost & Risk Evaluation for a Sole Trader",
                    "content": {
                        "intro": "Muthoni earns $\\text{KES } 55,000$ in monthly net profit running her standalone beauty salon in Thika. She is offered a formal employment job as a Senior Stylist at a major hotel earning $\\text{KES } 45,000$ per month with full health insurance. Last month, Muthoni experienced an equipment breakdown causing $\\text{KES } 30,000$ in repair costs that she had to absorb 100% from personal savings.",
                        "steps": [
                            "**Step 1: Given Information:** Monthly salon profit $Y_{\\text{salon}} = \\text{KES } 55,000$. Monthly job salary $Y_{\\text{job}} = \\text{KES } 45,000$. Annual salon baseline income $= 55,000 \\times 12 = \\text{KES } 660,000$. Annual job baseline income $= 45,000 \\times 12 = \\text{KES } 540,000$. Uninsured salon maintenance shock $L = \\text{KES } 30,000$.",
                            "**Step 2: Formula:** Net Annual Entrepreneurial Premium: $$P_{\\text{entrepreneur}} = Y_{\\text{salon,net}} - Y_{\\text{job}}$$, where $Y_{\\text{salon,net}} = (Y_{\\text{salon}} \\times 12) - L$.",
                            "**Step 3: Substitution:** Calculate net annual salon income after shock: $$Y_{\\text{salon,net}} = 660,000 - 30,000 = \\text{KES } 630,000$$.",
                            "**Step 4: Calculation:** Compute the entrepreneurial premium: $$P_{\\text{entrepreneur}} = \\text{KES } 630,000 - \\text{KES } 540,000 = \\text{KES } 90,000\\text{ / year}$$. Monthly net premium = $\\frac{90,000}{12} = \\text{KES } 7,500$.",
                            "**Step 5: Final Answer:** Muthoni earns a net entrepreneurial premium of $\\text{KES } 90,000$ annually over employment. This $\\text{KES } 7,500$ monthly premium compensates her for bearing full risk, unlimited liability, and operational stress.",
                            "**Step 6: Economic Interpretation & Pitfall:** Sole proprietors require higher earnings to justify personal risk-bearing. *Common Pitfall:* Calculating profit without deducting personal emergency losses or medical contingencies."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Overcoming Growth Bottlenecks in Gikomba",
                    "content": {
                        "title": "When Sole Proprietorship Growth Outpaces Single-Owner Capacity",
                        "text": "Mwangi operated a highly successful hardware stall in Gikomba Market as a sole trader. As demand grew to include major construction sites, he needed KES 2,000,000 for bulk cement purchases and delivery trucks. Banks refused to lend against his kiosk license without title deeds, and Mwangi suffered physical burnout working 14 hours daily. Realizing the structural limits of sole trading, he partnered with two colleagues to pool KES 3,000,000 and share managerial duties."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Pros and Cons of Sole Proprietorship Enterprises",
                    "content": {
                        "title": "Advantages and Disadvantages of Sole Proprietorships",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Detailed comparative analysis of small business agility, tax advantages, unlimited liability, and capital limitations in sole proprietorships."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Business Secrecy Value",
                    "content": {
                        "question": "Why is 'business secrecy' considered a major competitive advantage for a sole trader operating a localized bakery in Nakuru?",
                        "options": [
                            "The owner is legally exempt from paying county license fees",
                            "The owner is not legally required to publish audited financial records or disclose recipe margins to competing bakeries",
                            "The bakery is immune from public health inspections",
                            "The owner can secretly employ partners without their knowledge"
                        ],
                        "correct": "B",
                        "explanation": "Sole proprietorships are not required by law to publish or file public financial accounts, allowing proprietors to protect profit margins and operating strategies from competitors."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Identifying Core Structural Weakness",
                    "content": {
                        "question": "Which of the following scenarios represents the disadvantage of 'lack of continuity' in a sole proprietorship?",
                        "options": [
                            "The owner decides to raise prices by 10% without holding a board meeting",
                            "A successful retail shop closes permanently when the founder passes away because no legal succession framework exists",
                            "The owner obtains 14-day trade credit from a soft drink distributor",
                            "The business name is registered on the eCitizen platform"
                        ],
                        "correct": "B",
                        "explanation": "Lack of continuity means the life of the enterprise is inseparable from the proprietor; upon the owner's death or permanent incapacitation, the business legally and practically ceases to operate."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Autonomy & Incentive:** Direct decision control and 100% profit retention provide unparalleled motivation.\n2. **Privacy & Low Overhead:** Confidential financial books and minimal statutory filings protect local competitive edge.\n3. **Scale Ceiling:** Expansion is tightly bottlenecked by single-person savings and borrowing capacity.\n4. **Vulnerability Shield:** Transitioning into a partnership or limited company becomes vital once capital demands exceed single-owner limits."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Meaning and Characteristics of a Partnership
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Partnership: Meaning and Characteristics",
        "unit_description": "Co-ownership enterprise model (2 to 20/50 partners), mutual agency, joint and several unlimited liability, profit-sharing ratios, and partner typologies.",
        "lesson_title": "Meaning and Characteristics of a Partnership",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Medical Professionals in a Collaborative Clinic",
                    "content": {
                        "title": "Professional Medical Partnership in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Credit_Tojo_Andrianarivo_Safari_Doctors.jpg",
                        "caption": "Healthcare professionals collaborating in a clinic, representing the pooling of specialized skills and shared capital in a professional partnership.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a partnership under the Partnership Act of Kenya (Cap 29)\n- Explain the core principle of 'Mutual Agency' and its legal implications\n- Analyze the nature and high risks of 'Joint and Several Unlimited Liability'\n- Distinguish between active, dormant (sleeping), nominal, and limited partners"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Partnership and Mutual Agency",
                    "content": {
                        "term": "Partnership",
                        "definition": "A voluntary association of 2 or more persons (up to a maximum of 20, or 50 for designated professions) carrying on a lawful business in common with a view to making and sharing profits."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Tandem Bicycle Analogy",
                    "content": {
                        "text": "Think of a partnership as two riders pedaling a tandem (two-seater) bicycle:\n\n- **Double Power & Speed:** With two people pedaling, the bicycle climbs steep hills faster and carries heavier cargo (pooled capital and complementary skills).\n- **Shared Relief:** If Rider A needs a brief rest, Rider B continues pedaling to keep the bicycle moving (continuity during illness).\n- **Steering Friction:** Both riders must agree on direction. If Rider A turns left while Rider B turns right, the tandem wobbles and crashes (partner conflict and joint legal liability)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Partnership Structure and Liability Dynamics",
                    "content": {
                        "title": "Mutual Agency and Joint & Several Liability Flow",
                        "caption": "Vector diagram illustrating partner capital pooling, mutual agency contracts, and the creditor recovery mechanism under joint and several unlimited liability.",
                        "svg_content": SVG_PARTNERSHIP_STRUCTURE_AND_LIABILITY
                    }
                }
            ],
            # Card 4: Types of Partners Table
            [
                {
                    "type": "comparison_table",
                    "title": "Typology of Partners in Kenyan Commercial Law",
                    "content": {
                        "headers": ["Partner Type", "Capital Contribution", "Management Participation", "Profit / Loss Share", "Liability Exposure"],
                        "rows": [
                            ["General / Active Partner", "Contributes agreed capital", "Actively manages daily operations", "Shares profits & losses per ratio", "Unlimited Joint & Several"],
                            ["Sleeping / Dormant Partner", "Contributes capital", "Takes zero part in daily management", "Receives agreed profit share", "Unlimited Joint & Several"],
                            ["Nominal Partner", "Contributes NO capital", "Zero management (Lends name/reputation)", "Zero profits (May receive fee)", "Unlimited Liability to third parties"],
                            ["Limited Partner", "Contributes capital", "Legally barred from active management", "Shares profits per agreement", "Limited to capital contributed"],
                            ["Minor Partner", "May have capital invested", "Cannot participate in legal management", "Shares profits only; no loss liability", "Limited (Until reaching 18 years)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Joint and Several Liability Recovery Scenario",
                    "content": {
                        "intro": "Dr. Mary and Dr. Stephen operate 'Baraka Medical Clinic' as a general partnership in Kisumu. The clinic loses a supplier lawsuit and is ordered to pay $\\text{KES } 800,000$. The clinic's bank account has $\\text{KES } 0$. Dr. Stephen has only $\\text{KES } 50,000$ in personal assets, whereas Dr. Mary owns personal land and savings valued at $\\text{KES } 2,500,000$.",
                        "steps": [
                            "**Step 1: Given Information:** Total court judgment debt $D = \\text{KES } 800,000$. Firm bank balance = $\\text{KES } 0$. Partner Stephen personal assets $A_{\\text{Stephen}} = \\text{KES } 50,000$. Partner Mary personal assets $A_{\\text{Mary}} = \\text{KES } 2,500,000$. Profit-sharing ratio = $3:2$.",
                            "**Step 2: Formula & Legal Rule:** Under joint and several liability, creditors can sue both partners jointly or execute the entire debt against any single partner with personal wealth ($$\\text{Claim} \\le A_{\\text{partner}}$$).",
                            "**Step 3: Substitution & Creditor Action:** Creditor seizes all available cash from Stephen ($$\\text{KES } 50,000$$) and demands the remaining deficit from Mary: $$D_{\\text{rem}} = \\text{KES } 800,000 - \\text{KES } 50,000$$.",
                            "**Step 4: Calculation:** Compute Mary's forced personal payment: $$D_{\\text{rem}} = \\text{KES } 750,000$$. Total paid by Mary = $\\text{KES } 750,000$.",
                            "**Step 5: Final Answer:** Mary is legally forced to pay $\\text{KES } 750,000$ from her personal wealth immediately. She must later pursue Stephen internally for his agreed share ($40\\% \\times 800,000 = \\text{KES } 320,000$, of which he only paid $\\text{KES } 50,000$).",
                            "**Step 6: Economic Interpretation & Pitfall:** Joint and several liability means you are 100% financially liable for your partner's commitments. *Common Pitfall:* Believing you are only liable for your profit percentage in third-party lawsuits."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Baraka Medical Clinic in Kisumu",
                    "content": {
                        "title": "Combining Medical Specialization and Capital in Western Kenya",
                        "text": "Dr. Mary (pediatrician) and Dr. Stephen (general physician) combined KES 1,500,000 and KES 1,000,000 respectively to establish Baraka Medical Clinic. By operating as a partnership, they offered 24-hour outpatient and child health services, shared the burden of night calls, and qualified for a joint KES 500,000 equipment credit line from a commercial bank in Kisumu."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding Partnerships in Business Studies",
                    "content": {
                        "title": "Partnership Characteristics, Mutual Agency, and Liability",
                        "youtube_id": "WqlX5z6k4eQ",
                        "url": "https://www.youtube.com/watch?v=WqlX5z6k4eQ",
                        "description": "Comprehensive pedagogical video analyzing partnership definitions, mutual agency legal principles, and partner liability structures."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Mutual Agency Legal Effect",
                    "content": {
                        "question": "Partner A signs a contract with a pharmaceutical distributor to purchase KES 400,000 worth of medicine without informing Partner B. Is Partner B legally bound by this agreement?",
                        "options": [
                            "No, because Partner B did not sign the physical paper contract",
                            "Yes, because under the principle of mutual agency, every partner acts as an agent of the firm and binds all other partners",
                            "Only if the County Governor personally endorses the contract",
                            "No, because partnerships cannot enter commercial purchase agreements"
                        ],
                        "correct": "B",
                        "explanation": "Mutual agency establishes that each partner is both a principal and an agent of the firm. Any transaction carried out by one partner in the ordinary course of business legally binds the entire partnership."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Dormant Partner Liability",
                    "content": {
                        "question": "Which of the following statements accurately describes a 'dormant (sleeping) partner' in a general partnership in Kenya?",
                        "options": [
                            "They contribute zero capital and bear zero financial liability",
                            "They contribute capital and share in profits, but do not participate in daily management while retaining unlimited liability to creditors",
                            "They are legally exempt from all business debts and lawsuits",
                            "They must be a minor under 18 years of age"
                        ],
                        "correct": "B",
                        "explanation": "A dormant partner contributes capital and receives a share of profits but does not take part in daily management. However, in a general partnership, their liability to third-party creditors remains unlimited."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Co-Ownership Scale:** Partnerships unite 2 to 20 (or 50) co-owners pooling capital and professional talents.\n2. **Mutual Agency:** Every partner has legal power to commit the firm to binding contracts.\n3. **Joint & Several Liability:** Creditors can recover 100% of unpaid business debts from any partner with personal assets.\n4. **Typology Spectrum:** Active partners manage daily work, dormant partners invest passively, and nominal partners contribute reputation."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Formation and Management of a Partnership
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Partnership: Formation and Management",
        "unit_description": "Drafting the Partnership Deed (Articles of Partnership), statutory default provisions under the Partnership Act (Cap 29), and profit/loss calculation models.",
        "lesson_title": "Formation and Management of a Partnership",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Formal Partnership Agreement Signing in Kenya",
                    "content": {
                        "title": "Executing a Legal Partnership Deed in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/06/Korea_Kenya_Business_Partnership_03_%2827531512245%29.jpg",
                        "caption": "Business partners executing formal agreements, illustrating the legal drafting of a Partnership Deed to protect mutual interests.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- State the purpose and essential contents of a written Partnership Deed (Articles of Partnership)\n- Explain the default rules applied under the Partnership Act (Cap 29) when no written deed exists\n- Calculate proportional profit and loss shares based on unequal capital contributions\n- Describe the governance and decision-making mechanisms within a multi-partner enterprise"
                    }
                }
            ],
            # Card 2: Definitions & Legal Framework
            [
                {
                    "type": "definition_card",
                    "title": "Partnership Deed (Articles of Partnership)",
                    "content": {
                        "term": "Partnership Deed",
                        "definition": "A formal, legally binding written agreement that defines the rights, duties, capital contributions, profit-sharing ratios, and operating rules of all partners in a firm."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Written Deed vs. Default Partnership Act (Cap 29)",
                    "content": {
                        "text": "A partnership can technically be formed orally, in writing, or implied by conduct. However, operating without a written deed is highly dangerous:\n\n- **Default Rule on Profits:** If there is no written deed, the **Partnership Act (Cap 29)** dictates that all profits and losses **must be shared EQUALLY (1:1)**, even if one partner contributed 90% of the capital!\n- **Default Rule on Salaries:** Under Cap 29, **no partner is entitled to a salary** for working in the business unless explicitly written in the deed.\n- **Default Rule on Loans:** Advances/loans made by a partner to the firm earn **5% annual interest** by default."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Partnership Deed Architecture",
                    "content": {
                        "title": "The 6 Essential Pillars of a Partnership Agreement",
                        "caption": "Vector diagram detailing capital clauses, profit ratios, partner salaries, drawings rules, admission protocols, and dissolution procedures in a Partnership Deed.",
                        "svg_content": SVG_PARTNERSHIP_DEED_ARCHITECTURE
                    }
                }
            ],
            # Card 4: Deed Clauses vs Default Act Table
            [
                {
                    "type": "comparison_table",
                    "title": "Partnership Deed Clauses vs. Default Partnership Act Rules",
                    "content": {
                        "headers": ["Governance Dimension", "Standard Clause in Written Deed", "Default Rule under Partnership Act (Cap 29) (No Deed)", "Legal / Financial Implication"],
                        "rows": [
                            ["Profit & Loss Sharing", "Agreed ratio based on capital (e.g. 3:2:1)", "Strictly EQUAL share for all partners", "High-capital partner loses earnings if no deed"],
                            ["Partner Salaries", "Agreed executive salary for active partners", "NO partner is entitled to any salary", "Active managing partner works without wage"],
                            ["Interest on Capital", "Specified rate (e.g. 5% on equity)", "NO interest allowed on capital", "Capital receives only profit dividends"],
                            ["Interest on Partner Loans", "Commercial rate (e.g. 10% - 12%)", "Fixed at 5% per annum by law", "Partner loans yield modest statutory return"],
                            ["Admission of New Partner", "Agreed majority vote or special threshold", "Requires 100% UNANIMOUS consent", "A single partner can veto beneficial growth"],
                            ["Management Rights", "Assigned specialized functional roles", "Every partner has equal right to manage", "Risk of conflicting operational orders"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Multi-Partner Profit Distribution with Unequal Ratios",
                    "content": {
                        "intro": "Baraka Medical Clinic achieves a net annual profit of $\\text{KES } 1,200,000$ in Year 2. The partnership consists of three partners: Dr. Mary, Dr. Stephen, and Dr. Grace. Their capital contributions are $\\text{KES } 1,500,000$, $\\text{KES } 1,000,000$, and $\\text{KES } 500,000$ respectively, with an agreed profit-sharing ratio of $3:2:1$.",
                        "steps": [
                            "**Step 1: Given Information:** Net annual profit $\\Pi = \\text{KES } 1,200,000$. Agreed ratio = $3:2:1$ (Mary : Stephen : Grace). Total ratio parts $N = 3 + 2 + 1 = 6\\text{ parts}$.",
                            "**Step 2: Formula:** Value per single ratio part: $$V_{\\text{part}} = \\frac{\\Pi}{N}$$. Partner share: $$\\text{Share}_i = r_i \\times V_{\\text{part}}$$.",
                            "**Step 3: Substitution:** Calculate the monetary value of 1 ratio part: $$V_{\\text{part}} = \\frac{\\text{KES } 1,200,000}{6}$$.",
                            "**Step 4: Calculation:** Compute part value: $$V_{\\text{part}} = \\text{KES } 200,000$$.\n- Dr. Mary's share ($3\\text{ parts}$): $$3 \\times 200,000 = \\text{KES } 600,000$$\n- Dr. Stephen's share ($2\\text{ parts}$): $$2 \\times 200,000 = \\text{KES } 400,000$$\n- Dr. Grace's share ($1\\text{ part}$): $$1 \\times 200,000 = \\text{KES } 200,000$$\nTotal check: $600,000 + 400,000 + 200,000 = \\text{KES } 1,200,000$.",
                            "**Step 5: Final Answer:** Dr. Mary receives $\\text{KES } 600,000$, Dr. Stephen receives $\\text{KES } 400,000$, and Dr. Grace receives $\\text{KES } 200,000$ in exact accordance with their written Deed.",
                            "**Step 6: Economic Interpretation & Pitfall:** Proportional profit sharing rewards higher capital and risk exposure equitably. *Common Pitfall:* Failing to define profit ratios in writing, which forces equal $\\text{KES } 400,000$ splits under Cap 29 despite Mary contributing triple Grace's capital."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Resolving Partner Dispute in a Nairobi Law Firm",
                    "content": {
                        "title": "The Critical Role of Deed Clauses in Professional Practices",
                        "text": "Three advocates founded a legal partnership in Upper Hill, Nairobi. Two years later, one partner decided to relocate abroad and demanded an immediate cash payout of KES 4,000,000. Because their Partnership Deed contained a comprehensive 'Retirement & Goodwill Valuation Clause' specifying that outgoing capital must be paid in 4 equal quarterly instalments over 12 months, the firm avoided sudden insolvency and continued normal operations."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Drafting a Partnership Agreement in Business Economics",
                    "content": {
                        "title": "Partnership Deed Essentials and Default Legal Provisions",
                        "youtube_id": "7_j5N5V1N9c",
                        "url": "https://www.youtube.com/watch?v=7_j5N5V1N9c",
                        "description": "Comprehensive tutorial on partnership agreements, profit ratios, partner salaries, and dispute resolution under Kenyan commercial law."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Default Profit Rule under Cap 29",
                    "content": {
                        "question": "Amina contributes KES 800,000 and Brian contributes KES 200,000 to open a wholesale store, but they do NOT draft a written Partnership Deed. How must an annual profit of KES 500,000 be divided under Kenyan law?",
                        "options": [
                            "Amina gets KES 400,000 and Brian gets KES 100,000 based on their 4:1 capital ratio",
                            "Amina and Brian must receive exactly KES 250,000 each because the Partnership Act enforces equal sharing when no deed exists",
                            "Brian gets KES 0 because he contributed less than KES 500,000",
                            "The entire KES 500,000 must be surrendered to the Business Registration Service"
                        ],
                        "correct": "B",
                        "explanation": "Under the Partnership Act (Cap 29), in the absence of a written agreement specifying a different profit-sharing ratio, all partners share profits and losses equally regardless of capital contributions."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Partner Salary Entitlement",
                    "content": {
                        "question": "Partner Juma works 60 hours per week managing a clinic, while Partner Kiprono only visits once a month. There is no written Partnership Deed. Can Juma legally demand a monthly management salary under the Partnership Act?",
                        "options": [
                            "Yes, the law automatically assigns a minimum wage to the most active partner",
                            "No, under Cap 29, no partner is entitled to remuneration for acting in the partnership business unless explicitly agreed in a deed",
                            "Yes, but only if approved by the County Health Minister",
                            "Yes, Juma can unilaterally withdraw any salary amount from the firm's till"
                        ],
                        "correct": "B",
                        "explanation": "Section 28 of the Partnership Act explicitly provides that no partner is entitled to remuneration for acting in the partnership business unless the partners have formally agreed to salaries in their deed."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 6 Summary Takeaways",
                    "content": {
                        "text": "1. **Written Protection:** The Partnership Deed overrides the default, often disadvantageous, rules of the Partnership Act (Cap 29).\n2. **Equitable Ratios:** Capital-weighted profit ratios ensure fair financial rewards for larger equity contributors.\n3. **Salary Clauses:** Active working partners must include explicit remuneration clauses to be compensated for daily labour.\n4. **Exit & Dissolution Protocols:** Clear retirement and buyout terms prevent sudden firm liquidation during partner disputes."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7: Sources of Partnership Finance
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Partnership: Sources of Finance",
        "unit_description": "Capital contributions, ploughed-back retained profits, partner loan accounts, commercial bank facilities, asset leasing, and supplier credit lines.",
        "lesson_title": "Sources of Partnership Finance",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Medical Facility Expansion in Kenya",
                    "content": {
                        "title": "Institutional Capital Financing in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Kenya_Medical_Training_College_Karen_Campus_entrance.jpg",
                        "caption": "A modern health training institution in Nairobi, representing the scale of facility expansion unlocked through joint partnership finance and bank credit.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the primary internal and external sources of capital available to a partnership firm\n- Explain the legal and financial status of Partner Loan Accounts under the Partnership Act\n- Analyze how multi-partner collateral enhances commercial bank borrowing capacity\n- Calculate asset financing packages using combined equity, retained earnings, and debt"
                    }
                }
            ],
            # Card 2: Definitions & Financial Leverage
            [
                {
                    "type": "definition_card",
                    "title": "Partner Capital and Retained Earnings",
                    "content": {
                        "term": "Partner Loan Account",
                        "definition": "A debt facility where an individual partner advances funds to the firm beyond their agreed equity capital, ranking ahead of equity repayments upon firm dissolution."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Internal Equity vs. External Commercial Credit",
                    "content": {
                        "text": "Partnerships enjoy superior financing capabilities compared to sole proprietorships:\n\n- **Internal Synergy:** Multiple partners inject equity savings and can agree to retain annual profits (ploughing back) to fund machinery.\n- **External Credit Strength:** Commercial banks view partnerships favorably because multiple partners provide diversified collateral (e.g. 2 or 3 title deeds) and sign joint personal guarantees."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Partnership Capital Hierarchy",
                    "content": {
                        "title": "Internal Equity vs External Debt for Multi-Partner Firms",
                        "caption": "Vector diagram mapping partner equity contributions, ploughed-back reserves, partner loans, bank facilities, and asset leasing structures.",
                        "svg_content": SVG_PARTNERSHIP_FINANCE_AND_EXPANSION
                    }
                }
            ],
            # Card 4: Financing Instruments Table
            [
                {
                    "type": "comparison_table",
                    "title": "Sources of Capital for Partnerships in Kenya",
                    "content": {
                        "headers": ["Funding Source", "Capital Type", "Cost / Interest Terms", "Collateral & Security", "Firm Dissolution Rank"],
                        "rows": [
                            ["Initial Capital Contribution", "Internal Equity", "0% (Receives profit dividends)", "None (Owner investment)", "Refunded LAST after all creditors"],
                            ["Retained Earnings (Ploughed Back)", "Internal Equity", "0% (Reinvested surplus)", "None (Undistributed profits)", "Maintains firm reserve buffer"],
                            ["Partner Loan Account", "Internal Debt", "Agreed rate (Default 5% under Cap 29)", "Internal firm promissory note", "Paid BEFORE partner capital refunds"],
                            ["Commercial Bank Term Loan", "External Debt", "13% to 18% p.a. interest", "Joint personal guarantees + title deeds", "Senior claim; paid before partner funds"],
                            ["Asset Leasing / Hire Purchase", "External Asset Debt", "Monthly lease finance charges", "The leased asset itself (Machine/Van)", "Equipment repossessed on default"],
                            ["Supplier Trade Credit", "Short-term Working Capital", "0% if settled within 30-60 days", "Firm commercial reputation", "Unsecured trade creditor rank"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Mixed-Source Financing for an Ultrasound Machine",
                    "content": {
                        "intro": "Baraka Medical Clinic requires $\\text{KES } 1,500,000$ to purchase a digital color Doppler ultrasound machine. The partners finance the asset using three sources: Retained Clinic Earnings ($\\text{KES } 450,000$), Additional Partner Equity Infusion ($\\text{KES } 450,000$ split $3:2$ between Mary and Stephen), and a 3-Year Commercial Bank Equipment Loan ($\\text{KES } 600,000$ at $14\\%$ simple annual interest).",
                        "steps": [
                            "**Step 1: Given Information:** Total machine cost $C_{\\text{asset}} = \\text{KES } 1,500,000$. Retained earnings $E_{\\text{retained}} = \\text{KES } 450,000$. Partner equity $E_{\\text{equity}} = \\text{KES } 450,000$ (Mary : Stephen = $3:2$). Bank Loan $P = \\text{KES } 600,000$ at $r = 14\\%$ for $t = 3\\text{ years}$.",
                            "**Step 2: Formula:** Equity shares: Mary $= \\frac{3}{5} \\times E_{\\text{equity}}$, Stephen $= \\frac{2}{5} \\times E_{\\text{equity}}$. Total Bank Loan Interest: $$I = P \\times r \\times t$$. Total Bank Repayment: $$R = P + I$$. Monthly Loan Instalment: $$M = \\frac{R}{36}$$.",
                            "**Step 3: Substitution:**\n- Mary cash injection = $\\frac{3}{5} \\times 450,000 = \\text{KES } 270,000$\n- Stephen cash injection = $\\frac{2}{5} \\times 450,000 = \\text{KES } 180,000$\n- Total Bank Interest = $600,000 \\times 0.14 \\times 3$.",
                            "**Step 4: Calculation:** Compute bank interest and instalments: $$I = \\text{KES } 252,000$$.\n- Total loan repayment $R = 600,000 + 252,000 = \\text{KES } 852,000$\n- Monthly bank instalment $M = \\frac{852,000}{36} = \\text{KES } 23,667$.",
                            "**Step 5: Final Answer:** The clinic raises the full $\\text{KES } 1,500,000$ immediately, with Mary injecting $\\text{KES } 270,000$, Stephen injecting $\\text{KES } 180,000$, using $\\text{KES } 450,000$ in retained profits, and servicing $\\text{KES } 23,667$ per month in bank debt.",
                            "**Step 6: Economic Interpretation & Pitfall:** Partnerships leverage combined internal cash to borrow substantial capital prudently. *Common Pitfall:* Failing to account for monthly debt service ($M = \\text{KES } 23,667$) when calculating monthly profit distributions."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Baraka Clinic Diagnostic Expansion",
                    "content": {
                        "title": "Acquiring Advanced Diagnostic Equipment in Kisumu",
                        "text": "By pooling retained profits and injecting fresh partner equity, Baraka Medical Clinic installed their modern ultrasound unit without choking daily cash flows. The ultrasound service generated KES 95,000 in gross monthly diagnostic fees, easily covering the KES 23,667 bank instalment while adding KES 71,333 in net monthly surplus to the partnership."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Financing Business Partnerships and Commercial Loans",
                    "content": {
                        "title": "How Partnerships Raise Expansion Capital in Kenya",
                        "youtube_id": "4j2emMn7GEk",
                        "url": "https://www.youtube.com/watch?v=4j2emMn7GEk",
                        "description": "Educational breakdown of partnership capital structures, partner loan accounts, and asset financing models in commercial business."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Priority of Partner Loan Accounts",
                    "content": {
                        "question": "A partnership firm in Nakuru dissolves and sells its remaining assets. In what order must the liquidation proceeds be distributed under Kenyan commercial law?",
                        "options": [
                            "Partner equity capital first, partner loans second, outside creditors last",
                            "Outside third-party debts first, partner loan accounts second, and original partner equity capital refunded last",
                            "The funds must be divided equally among all employees regardless of debt",
                            "All proceeds are forfeited to the National Treasury"
                        ],
                        "correct": "B",
                        "explanation": "Upon firm dissolution, liquidation proceeds must settle outside third-party creditors first, partner loan advances second, and partner equity capital contributions last."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Bank Borrowing Advantage",
                    "content": {
                        "question": "Why do commercial banks in Kenya generally extend larger loan facilities to partnerships than to sole proprietorships?",
                        "options": [
                            "Partnerships are legally exempt from loan interest charges",
                            "Partners pool multiple personal assets, provide joint personal guarantees, and possess diversified professional expertise",
                            "The Central Bank of Kenya guarantees all partnership debts",
                            "Partnerships are legally forbidden from declaring bankruptcy"
                        ],
                        "correct": "B",
                        "explanation": "Commercial banks perceive lower credit risk because multiple partners combine their collateral assets, sign joint and several guarantees, and offer broader managerial capabilities."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 7 Summary Takeaways",
                    "content": {
                        "text": "1. **Multi-Source Capital:** Partnerships combine partner equity, retained earnings, partner debt, and commercial bank loans.\n2. **Partner Loan Status:** Advances from partners earn 5% interest under Cap 29 and take priority over equity refunds upon dissolution.\n3. **Collateral Synergy:** Joint personal guarantees allow partnerships to secure larger term loans for capital machinery.\n4. **Prudent Cash Flow Allocation:** Debt repayments must be budgeted as operational expenses before declaring partner profit drawings."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8: Advantages and Disadvantages of a Partnership
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Partnership: Advantages and Disadvantages",
        "unit_description": "Comprehensive comparative evaluation of specialization, capital scale, and risk-sharing against joint liability, decision friction, and structural instability.",
        "lesson_title": "Advantages and Disadvantages of a Partnership",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Professional Business Partnership Consultation",
                    "content": {
                        "title": "Strategic Partner Collaboration in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Korea_Kenya_Business_Partnership_02_%2826923130753%29.jpg",
                        "caption": "Executive business partners discussing corporate strategy, portraying the balance between collaborative strength and consensus-building.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Systematically analyze the major advantages and disadvantages of a partnership firm\n- Compare the operational efficiency of partnerships against sole proprietorships\n- Explain the risk of partner disputes, slow consensus, and joint unlimited liability exposure\n- Identify strategies for mitigating structural partnership instability"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Specialization and Partnership Instability",
                    "content": {
                        "term": "Division of Labour (Specialization)",
                        "definition": "The organizational strategy where partners divide operational responsibilities according to their distinct professional training, technical expertise, and natural talents."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Collaboration vs. Friction Matrix",
                    "content": {
                        "text": "Entering a partnership introduces major strategic trade-offs:\n\n- **Synergistic Power:** Combining a brilliant marketing mind with an expert accountant and a technical engineer creates an enterprise far stronger than any single founder.\n- **Friction and Fragility:** Every major policy requires agreement. If interpersonal trust breaks down, or if one partner acts recklessly, the entire firm faces immediate legal and financial ruin."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Partnership vs Sole Trader Matrix",
                    "content": {
                        "title": "Direct Comparison: Sole Proprietorship vs Partnership",
                        "caption": "Vector comparison matrix evaluating capital capacity, decision speed, division of labour, liability risk, and business continuity.",
                        "svg_content": SVG_PARTNERSHIP_VS_SOLE_TRADER_MATRIX
                    }
                }
            ],
            # Card 4: Advantages & Disadvantages Matrix Table
            [
                {
                    "type": "comparison_table",
                    "title": "Comprehensive Trade-offs of a Partnership Firm",
                    "content": {
                        "headers": ["Feature", "Advantage (The Strength)", "Disadvantage (The Vulnerability)", "Practical Management Rule"],
                        "rows": [
                            ["Capital Base", "Larger pooled capital & superior bank credit", "Still limited compared to joint-stock corporations", "Retain annual profits to build reserves"],
                            ["Management & Skills", "Specialization and shared workload", "Disagreements and slow decision-making", "Define distinct functional roles in deed"],
                            ["Risk Distribution", "Losses are distributed across multiple owners", "Joint & several unlimited liability for partner errors", "Maintain comprehensive professional indemnity insurance"],
                            ["Continuity", "Business continues if one partner is sick", "Legally dissolved upon death/bankruptcy of a partner", "Include continuation and buyout clauses in deed"],
                            ["Secrecy & Privacy", "Accounts remain private between partners", "Internal lack of secrecy among partners", "Enforce strict non-disclosure clauses"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Risk Sharing vs. Sole Burden under Unforeseen Losses",
                    "content": {
                        "intro": "A commercial fire causes an uninsured stock loss of $\\text{KES } 600,000$. Compare how this financial catastrophe is absorbed in Scenario A (Sole Proprietor) versus Scenario B (3-Partner Firm with agreed profit/loss ratio $3:2:1$).",
                        "steps": [
                            "**Step 1: Given Information:** Uninsured catastrophe loss $L = \\text{KES } 600,000$. Scenario A: Single owner. Scenario B: 3 Partners (A, B, C) with ratio $3:2:1$ (Total parts = 6).",
                            "**Step 2: Formula:** Sole Trader Burden: $$L_{\\text{sole}} = L$$. Partnership Partner Share: $$L_i = \\frac{r_i}{\\sum r} \\times L$$.",
                            "**Step 3: Substitution & Calculation Scenario A (Sole Trader):** The sole proprietor bears 100% of the shock: $$L_{\\text{sole}} = \\text{KES } 600,000$$. This may cause immediate personal bankruptcy.",
                            "**Step 4: Substitution & Calculation Scenario B (Partnership):** Loss per part = $\\frac{600,000}{6} = \\text{KES } 100,000$.\n- Partner A share ($3\\text{ parts}$): $$3 \\times 100,000 = \\text{KES } 300,000$$\n- Partner B share ($2\\text{ parts}$): $$2 \\times 100,000 = \\text{KES } 200,000$$\n- Partner C share ($1\\text{ part}$): $$1 \\times 100,000 = \\text{KES } 100,000$$\nTotal check: $300,000 + 200,000 + 100,000 = \\text{KES } 600,000$.",
                            "**Step 5: Final Answer:** In the partnership, the maximum individual burden is reduced from $\\text{KES } 600,000$ to $\\text{KES } 300,000$, preserving the solvency and operational continuity of the firm.",
                            "**Step 6: Economic Interpretation & Pitfall:** Risk pooling prevents catastrophic failure of small enterprises. *Common Pitfall:* Forgetting that if Partner C has no cash, Partners A and B remain legally liable to settle C's share under joint and several liability."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Resolving Partner Deadlock in Machakos",
                    "content": {
                        "title": "Managing Strategic Vision Friction in a Civil Engineering Firm",
                        "text": "Two civil engineers formed a partnership in Machakos to bid for county road tenders. Partner A wanted to reinvest all profits into buying heavy excavators, while Partner B wanted cash dividends to fund personal real estate. The resulting 6-month management deadlock stalled tender submissions. They resolved the impasse by appointing an independent senior consultant to arbitrate and amending their deed to mandate a 50% dividend payout and 50% equipment reserve policy."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Advantages and Disadvantages of Business Partnerships",
                    "content": {
                        "title": "Evaluating Partnerships: Capital Synergy vs Conflict Risks",
                        "youtube_id": "r7pdUswl8qM",
                        "url": "https://www.youtube.com/watch?v=r7pdUswl8qM",
                        "description": "Comprehensive comparative lesson exploring specialization, risk pooling, joint liability dangers, and dispute resolution in business partnerships."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Primary Advantage of Partnerships",
                    "content": {
                        "question": "Which of the following is the most significant operational advantage that a 3-person partnership has over a sole proprietorship?",
                        "options": [
                            "Partnerships are legally exempt from all national taxes",
                            "Partnerships combine complementary professional specializations and pool larger capital resources",
                            "Partnerships grant limited liability to all active general partners",
                            "Partnerships never experience management disagreements"
                        ],
                        "correct": "B",
                        "explanation": "The primary operational strengths of a partnership are specialization (division of labour across distinct expertise) and a larger pooled capital base."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Major Risk of General Partnerships",
                    "content": {
                        "question": "What is the most severe financial risk faced by an individual who joins a general partnership with an untrustworthy colleague?",
                        "options": [
                            "They will be required to change their legal name",
                            "They are personally liable for 100% of all debts and contractual damages incurred by their colleague in the firm's name",
                            "The County Government will seize their voter registration card",
                            "They cannot withdraw any profits for 20 years"
                        ],
                        "correct": "B",
                        "explanation": "Under joint and several unlimited liability and mutual agency, any partner's mistakes or unauthorized contracts bind all partners personally, putting their personal assets at risk."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 8 Summary Takeaways",
                    "content": {
                        "text": "1. **Collaborative Power:** Combining professional skills and capital creates an enterprise capable of larger commercial undertakings.\n2. **Shared Risk Burden:** Operating losses and catastrophic shocks are distributed proportionally across multiple equity holders.\n3. **Friction Hazard:** Slower consensus and interpersonal disputes represent the primary operational friction in partnerships.\n4. **High Trust Requirement:** Joint and several liability makes complete mutual integrity the indispensable foundation of partnership success."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 9: Meaning, Principles, and Economic Role of a Cooperative
    # =========================================================================
    {
        "unit_order": 9,
        "unit_name": "Cooperative Societies: Meaning, Principles, and Role",
        "unit_description": "Autonomous member-owned enterprises, the 7 universal ICA principles, democratic control (1M1V), and eliminating middlemen in Kenyan rural economies.",
        "lesson_title": "Meaning, Principles, and Economic Role of a Cooperative",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Smallholder Dairy Farming in Murang'a County",
                    "content": {
                        "title": "Community Dairy Production in Murang'a, Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/2/20/A_man_milks_a_cow_in_the_agricultural_rich_Murang%27a_county_Kenya.jpg",
                        "caption": "A small-scale farmer milking his dairy cow in Murang'a County, illustrating the grassroots producers empowered by cooperative marketing societies.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 9 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a cooperative society under the Cooperative Societies Act of Kenya (Cap 490)\n- Explain the 7 universal International Cooperative Alliance (ICA) principles\n- Distinguish the democratic 'One Member, One Vote' rule from corporate share-weighted voting\n- Analyze how agricultural cooperatives eliminate exploitative middlemen and empower rural communities"
                    }
                }
            ],
            # Card 2: Definitions & Core Principles
            [
                {
                    "type": "definition_card",
                    "title": "Cooperative Society and Democratic Control",
                    "content": {
                        "term": "Cooperative Society",
                        "definition": "An autonomous, voluntary association of persons united to meet their common economic, social, and cultural needs through a jointly owned and democratically controlled enterprise."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Bundle of Sticks Analogy",
                    "content": {
                        "text": "Think of small-scale producers in Kenya:\n\n- **A Single Stick:** A single thin wooden stick is easily snapped in half by a child. This represents an isolated smallholder farmer with 15 litres of milk who is forced to accept low prices from exploitative middlemen.\n- **The Bundle of Sticks:** Tie 50 or 200 of those exact same sticks together with a strong rope. Even the strongest athlete cannot bend or break the bundle!\n- In business economics, binding small producers into a **cooperative society** creates collective market bargaining power, bulk chilling facilities, and financial resilience."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 7 Universal ICA Cooperative Principles",
                    "content": {
                        "title": "International Cooperative Alliance Governance Architecture",
                        "caption": "Vector diagram detailing Open Membership, Democratic Control (1M1V), Economic Participation, Autonomy, Education, Inter-Cooperation, and Concern for Community.",
                        "svg_content": SVG_COOPERATIVE_SEVEN_PRINCIPLES
                    }
                }
            ],
            # Card 4: 7 Principles Matrix Table
            [
                {
                    "type": "comparison_table",
                    "title": "The 7 Universal Cooperative Principles (ICA Standards)",
                    "content": {
                        "headers": ["Principle", "Core Definition & Rule", "Kenyan Operational Practice", "Community Economic Impact"],
                        "rows": [
                            ["1. Voluntary & Open Membership", "Open to all persons able to use services without bias", "Open to all dairy or tea farmers in a sub-county", "Inclusivity and non-discrimination"],
                            ["2. Democratic Member Control", "One Member, One Vote (1M1V) regardless of shares", "Equal voting at AGMs; prevents wealthy domination", "Equal voice for small and large producers"],
                            ["3. Member Economic Participation", "Members contribute equitably and share surpluses", "Surplus paid as share dividends & patronage bonuses", "Equitable wealth redistribution to households"],
                            ["4. Autonomy & Independence", "Self-governing organizations controlled by members", "Elected member Board; independent from state control", "Self-reliant community governance"],
                            ["5. Education, Training & Info", "Providing training to members, leaders, and youth", "Farmer field days on veterinary care & fodder", "Boosts agricultural productivity and quality"],
                            ["6. Cooperation Among Co-ops", "Co-ops working with local and national unions", "Murang'a Dairy partnering with Cooperative Bank", "Strengthens national cooperative movement"],
                            ["7. Concern for Community", "Sustainable development policies approved by members", "Building local milk collection centers & water tanks", "Grassroots rural development and employment"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Individual Farmer vs. Cooperative Bulk Marketing Returns",
                    "content": {
                        "intro": "Maina is a small-scale dairy farmer in Murang'a with 2 cows producing $20\\text{ litres/day} = 600\\text{ litres/month}$. A local middleman offers $\\text{KES } 28\\text{ per litre}$ at farmgate. Alternatively, the Murang'a Dairy Cooperative Society collects milk daily, chills it in bulk, and sells directly to a Nairobi processor at $\\text{KES } 54\\text{ per litre}$, deducting $\\text{KES } 5\\text{ per litre}$ for transport, chilling, and society administration.",
                        "steps": [
                            "**Step 1: Given Information:** Monthly milk volume $Q = 600\\text{ litres}$. Middleman farmgate price $P_{\\text{middleman}} = \\text{KES } 28\\text{ / L}$. Cooperative gross bulk price $P_{\\text{coop,gross}} = \\text{KES } 54\\text{ / L}$. Cooperative operating deduction $C_{\\text{ops}} = \\text{KES } 5\\text{ / L}$.",
                            "**Step 2: Formula:** Middleman Monthly Revenue: $$R_{\\text{middleman}} = Q \\times P_{\\text{middleman}}$$. Cooperative Net Price: $$P_{\\text{coop,net}} = P_{\\text{coop,gross}} - C_{\\text{ops}}$$. Cooperative Monthly Revenue: $$R_{\\text{coop}} = Q \\times P_{\\text{coop,net}}$$. Net Monthly Cooperative Benefit: $$\\Delta R = R_{\\text{coop}} - R_{\\text{middleman}}$$.",
                            "**Step 3: Substitution:**\n- $R_{\\text{middleman}} = 600 \\times 28 = \\text{KES } 16,800$\n- $P_{\\text{coop,net}} = 54 - 5 = \\text{KES } 49\\text{ / L}$\n- $R_{\\text{coop}} = 600 \\times 49 = \\text{KES } 29,400$.",
                            "**Step 4: Calculation:** Compute additional monthly income earned by Maina: $$\\Delta R = \\text{KES } 29,400 - \\text{KES } 16,800 = \\text{KES } 12,600\\text{ / month}$$. Percentage income increase = $\\frac{12,600}{16,800} \\times 100\\% = 75\\%$.",
                            "**Step 5: Final Answer:** By selling through the cooperative, Maina earns an extra $\\text{KES } 12,600$ every month (a $75\\%$ boost in gross earnings) while securing guaranteed daily collection.",
                            "**Step 6: Economic Interpretation & Pitfall:** Cooperatives eliminate monopsonistic middleman margins through collective value addition. *Common Pitfall:* Selling to hawkers for quick cash on credit, risking total non-payment."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Murang'a County Dairy Farmers Co-op",
                    "content": {
                        "title": "Transforming Rural Livelihoods Through Collective Bulk Cooling",
                        "text": "Historically, smallholder dairy farmers in Murang'a suffered massive post-harvest spoilage and predatory farmgate prices as low as KES 20/L during peak rains. By uniting over 10,000 farmers into the Murang'a Dairy Farmers Cooperative Union, establishing 35 stainless-steel milk cooling plants across all sub-counties, and negotiating direct supply contracts with national processors, the union stabilized milk prices at over KES 45/L, generating over KES 2.5 billion annually for rural households."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Power of Cooperatives in the Kenyan Economy",
                    "content": {
                        "title": "Cooperative Principles and Rural Economic Transformation in Kenya",
                        "youtube_id": "v83s92y5Tq4",
                        "url": "https://www.youtube.com/watch?v=v83s92y5Tq4",
                        "description": "In-depth educational video exploring cooperative societies, the 7 ICA principles, democratic voting, and agricultural value addition in Kenya."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Democratic Member Control (1M1V)",
                    "content": {
                        "question": "In a registered coffee cooperative society in Nyeri, Farmer Kimani owns 2,000 shares while Farmer Wambui owns 20 shares. During the Annual General Meeting (AGM) vote to elect a new director, how many votes does Kimani have?",
                        "options": [
                            "Kimani has 2,000 votes and Wambui has only 20 votes",
                            "Kimani has exactly ONE vote, and Wambui has exactly ONE vote, under the 'One Member, One Vote' principle",
                            "Kimani has 100 votes because his shareholding exceeds 1,000 shares",
                            "Kimani automatically becomes the Chairman without any vote"
                        ],
                        "correct": "B",
                        "explanation": "Under the second universal ICA principle of 'Democratic Member Control', every member of a primary cooperative society possesses exactly one vote regardless of the number of shares they own."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Core Economic Role of Cooperatives",
                    "content": {
                        "question": "What is the primary economic mechanism by which agricultural marketing cooperatives improve the earnings of smallholder farmers in Kenya?",
                        "options": [
                            "They force farmers to abandon farming and seek urban employment",
                            "They aggregate small produce volumes, invest in bulk storage/cooling, eliminate exploitative middlemen, and negotiate premium prices",
                            "They print their own private paper currency to pay members",
                            "They prohibit members from opening commercial bank accounts"
                        ],
                        "correct": "B",
                        "explanation": "Cooperatives pool small individual harvests into commercial bulk volumes, invest in shared processing and storage infrastructure, and negotiate directly with major processors, capturing higher net returns for members."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 9 Summary Takeaways",
                    "content": {
                        "text": "1. **Autonomous Empowerment:** Cooperatives unite citizens to meet shared economic needs through joint democratic ownership.\n2. **Democratic Equality:** Governance is strictly founded on 'One Member, One Vote' (1M1V), preventing capital-based domination.\n3. **Middleman Elimination:** Bulk aggregation and cooling/processing capture premium market prices for smallholders.\n4. **Surplus Redistribution:** Financial surpluses are returned directly to members as dividends and patronage rebates."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 10: Types of Cooperatives
    # =========================================================================
    {
        "unit_order": 10,
        "unit_name": "Cooperative Societies: Types in Kenya",
        "unit_description": "Comprehensive taxonomy: SACCOs, Agricultural/Marketing, Consumer, Housing, and Producer/Artisan Cooperatives, their target memberships, and socio-economic impacts.",
        "lesson_title": "Types of Cooperatives",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Tea Harvesting Cooperative in Kenya",
                    "content": {
                        "title": "Agricultural Marketing Cooperatives in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Tea_picking.jpg",
                        "caption": "Smallholder tea farmers harvesting crops destined for collective cooperative factories, exemplifying agricultural producer cooperation in Kenya.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 10 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Classify cooperative societies in Kenya into five distinct functional categories\n- Explain the operations, savings mobilization, and loan mechanisms of SACCOs\n- Compare Agricultural Marketing, Consumer, Housing, and Producer cooperatives\n- Calculate SACCO dividend yields and loan multipliers for member development projects"
                    }
                }
            ],
            # Card 2: Definitions & Typology Framework
            [
                {
                    "type": "definition_card",
                    "title": "SACCO and Housing Cooperative Societies",
                    "content": {
                        "term": "Savings and Credit Cooperative (SACCO)",
                        "definition": "A specialized financial cooperative owned by members to mobilize regular monthly savings and provide affordable credit facilities at reasonable interest rates."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Diverse Landscape of Kenyan Cooperatives",
                    "content": {
                        "text": "Cooperatives in Kenya span five vital economic domains:\n\n- **1. SACCOs (Financial):** Mobilize billions in domestic savings; regulated by SASRA.\n- **2. Agricultural & Marketing:** Milk, tea, coffee, pyrethrum, and cereal processing/export.\n- **3. Consumer Cooperatives:** Wholesale bulk purchases of food and household commodities sold at fair prices.\n- **4. Housing Cooperatives:** Buying large land tracts collectively, subdividing, titling, and building affordable homes.\n- **5. Producer / Artisan Cooperatives:** Jua kali artisans, wood carvers, and soapstone crafters sharing raw materials and export marketing."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Taxonomy of Kenyan Cooperatives",
                    "content": {
                        "title": "Classification by Economic Function & Membership Base",
                        "caption": "Vector diagram detailing SACCOs, Agricultural, Consumer, Housing, and Producer Cooperatives with Kenyan institutional examples (Mwalimu, Stima, Murang'a Dairy).",
                        "svg_content": SVG_TYPES_OF_COOPERATIVES_TAXONOMY
                    }
                }
            ],
            # Card 4: 5 Cooperative Types Matrix Table
            [
                {
                    "type": "comparison_table",
                    "title": "Classification Matrix: Cooperative Types in Kenya",
                    "content": {
                        "headers": ["Type of Cooperative", "Target Membership", "Core Activity / Mandate", "Revenue & Surplus Stream", "Kenyan Real Example"],
                        "rows": [
                            ["SACCOs (Savings & Credit)", "Salaried employees, business owners, youth", "Mobilizing savings & issuing development loans", "Interest on member loans (e.g. 1% per month)", "Mwalimu National, Stima SACCO, Harambee SACCO"],
                            ["Agricultural / Marketing", "Smallholder farmers (dairy, coffee, tea)", "Bulk transport, processing, value addition & export", "Commission on bulk commodity sales", "Murang'a Dairy Co-op, Nyeri Coffee Union, KTDA"],
                            ["Consumer Cooperatives", "Household consumers, estate residents", "Wholesale food purchases & fair-price retail shops", "Retail markup margins over wholesale cost", "Estate Consumer Stores, Staff Canteens"],
                            ["Housing Cooperatives", "Home seekers, low-income earners", "Collective land acquisition, subdivision & building", "Member plot installments & development fees", "NACHU, Mwalimu Housing Union, Urithi Housing"],
                            ["Producer / Artisans", "Craftsmen, wood carvers, jua kali welders", "Joint raw material buying & collective craft export", "Sales commissions & craft market fees", "Wamunyu Wood Carvers, Kisii Soapstone Guild"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: SACCO Dividend Yield and Loan Multiplier Calculation",
                    "content": {
                        "intro": "Amina is a secondary school teacher in Kisii who has accumulated $\\text{KES } 180,000$ in non-withdrawable member deposits in Mwalimu National SACCO over 3 years. At the end of the financial year, the SACCO AGM declares a deposit dividend rebate of $10.5\\%$. Amina also applies for an emergency development loan, which allows a member to borrow up to $3\\times$ their total deposit balance.",
                        "steps": [
                            "**Step 1: Given Information:** Member cumulative deposits $D = \\text{KES } 180,000$. Declared dividend rebate rate $r = 10.5\\% = 0.105$. SACCO loan multiplier factor $M = 3\\times$.",
                            "**Step 2: Formula:** Annual Deposit Dividend Return: $$\\text{Dividend} = D \\times r$$. Maximum Qualifying Loan Eligibility: $$L_{\\text{max}} = D \\times M$$.",
                            "**Step 3: Substitution:** Calculate Amina's annual dividend earnings: $$\\text{Dividend} = \\text{KES } 180,000 \\times 0.105$$. Calculate maximum loan eligibility: $$L_{\\text{max}} = \\text{KES } 180,000 \\times 3$$.",
                            "**Step 4: Calculation:** Compute dividend payout: $$\\text{Dividend} = \\text{KES } 18,900$$. Compute maximum loan capacity: $$L_{\\text{max}} = \\text{KES } 540,000$$.",
                            "**Step 5: Final Answer:** Amina receives a direct annual cash dividend of $\\text{KES } 18,900$ and qualifies to borrow up to $\\text{KES } 540,000$ for personal housing construction backed by peer guarantors.",
                            "**Step 6: Economic Interpretation & Pitfall:** SACCOs offer superior dividend yields compared to commercial bank savings while multiplying borrowing power. *Common Pitfall:* Over-borrowing without assessing monthly loan deductions against net take-home salary."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Mwalimu National SACCO & Stima SACCO",
                    "content": {
                        "title": "Pioneering Financial Inclusion for Over 100,000 Kenyan Professionals",
                        "text": "Mwalimu National SACCO, founded by Kenyan teachers in 1974, has grown into the largest SACCO in Africa with assets exceeding KES 60 billion. By enabling teachers across all 47 counties to save monthly via payroll deductions, the SACCO has financed over 50,000 home constructions, land purchases, and university degrees at fair interest rates without demanding commercial bank collateral."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Types of Cooperative Societies in Kenya",
                    "content": {
                        "title": "SACCOs, Agricultural, and Housing Cooperatives in Kenya",
                        "youtube_id": "W8KCJ3w9cgE",
                        "url": "https://www.youtube.com/watch?v=W8KCJ3w9cgE",
                        "description": "Educational guide exploring SACCO operations, marketing cooperatives, housing societies, and SASRA regulatory oversight in Kenya."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying SACCO Function",
                    "content": {
                        "question": "A group of 30 boda boda operators in Nakuru want to pool KES 500 every week to create a fund that lends money to members to buy their own motorcycles. Which type of cooperative society should they form?",
                        "options": [
                            "A Consumer Cooperative Society",
                            "A Savings and Credit Cooperative Society (SACCO)",
                            "A Housing Cooperative Society",
                            "A Joint-Stock Public Corporation"
                        ],
                        "correct": "B",
                        "explanation": "A SACCO is specifically designed to mobilize regular member savings and provide affordable credit facilities to finance capital acquisitions like motorcycles."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Purpose of Housing Cooperatives",
                    "content": {
                        "question": "Why do low-income urban workers join Housing Cooperatives like NACHU to acquire residential land instead of buying individually?",
                        "options": [
                            "The government gives free land only to housing cooperatives",
                            "Housing cooperatives pool funds to purchase large agricultural tracts in bulk, subdivide, install roads/water, and issue genuine title deeds at wholesale prices",
                            "Members of housing cooperatives are exempt from paying water bills",
                            "Housing cooperatives do not require members to pay for land"
                        ],
                        "correct": "B",
                        "explanation": "Housing cooperatives achieve economies of scale by purchasing large land parcels in bulk, handling legal subdivision and titling, and developing infrastructure collectively at a fraction of individual retail costs."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 10 Summary Takeaways",
                    "content": {
                        "text": "1. **SACCO Financial Power:** Mobilizes member deposits and provides $3\\times$ loan leverage at competitive interest rates.\n2. **Agricultural Marketing:** Aggregates, processes, and markets cash crops and dairy to maximize farmer income.\n3. **Consumer & Producer Co-ops:** Eliminate retail inflation on foodstuffs and enable artisans to purchase raw materials in bulk.\n4. **Housing Empowerment:** Pools savings to acquire large land parcels and build affordable, titled family homes."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 11: Formation and Management of a Cooperative
    # =========================================================================
    {
        "unit_order": 11,
        "unit_name": "Cooperative Societies: Formation and Management",
        "unit_description": "Registration under Cooperative Societies Act (Cap 490), drafting By-Laws, AGM authority, Management Committee, Supervisory Committee, and limited liability.",
        "lesson_title": "Formation and Management of a Cooperative",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Cooperative House Corporate Headquarters in Nairobi",
                    "content": {
                        "title": "Cooperative Movement Architecture in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Extelcoms_House_%2B_Cooperative_House%2C_Nairobi%2C_2025_%2801%29.jpg",
                        "caption": "Cooperative House in Nairobi CBD, representing the institutional stature and legal foundation of the Kenyan cooperative sector.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 11 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Outline the legal registration steps for a primary cooperative under the Cooperative Societies Act (Cap 490)\n- Explain the essential contents and purpose of Cooperative By-Laws\n- Describe the governance hierarchy: AGM, Board of Directors, Supervisory Committee, and CEO\n- Contrast the limited liability status of cooperatives with sole traders and partnerships"
                    }
                }
            ],
            # Card 2: Definitions & Legal Personhood
            [
                {
                    "type": "definition_card",
                    "title": "Cooperative Societies Act (Cap 490) & Separate Legal Entity",
                    "content": {
                        "term": "Cooperative By-Laws",
                        "definition": "The registered internal constitution and operating rules of a cooperative society that govern membership qualifications, share capital limits, committee elections, and surplus distribution."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Shield of Corporate Legal Personality",
                    "content": {
                        "text": "Unlike sole traders and partnerships, a registered cooperative society is a **Separate Legal Entity (Body Corporate)**:\n\n- **Limited Liability:** Members risk only their invested share capital. If the cooperative's milk truck crashes or the society defaults on a bank loan, members' personal land and private cattle are **100% legally protected**!\n- **Perpetual Succession:** The cooperative exists permanently. It does not dissolve if members or committee directors pass away or resign."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Cooperative Governance Structure",
                    "content": {
                        "title": "Democratic Governance Hierarchy under Cap 490",
                        "caption": "Vector diagram detailing the AGM (Supreme Body), Board of Directors (Policy), Supervisory Committee (Internal Audit), and Professional Management.",
                        "svg_content": SVG_COOPERATIVE_GOVERNANCE_STRUCTURE
                    }
                }
            ],
            # Card 4: Formation Stages Table
            [
                {
                    "type": "comparison_table",
                    "title": "Step-by-Step Formation Process for a Cooperative in Kenya",
                    "content": {
                        "headers": ["Stage", "Legal Action Required", "Key Regulatory Actor", "Statutory Threshold", "Compliance Document Issued"],
                        "rows": [
                            ["1. Promoter Meeting", "Founding members meet to discuss objectives", "Provisional Promoter Committee", "Minimum 10 qualified persons", "Promoter Minutes & Attendance Register"],
                            ["2. Drafting By-Laws", "Formulating operating rules & share capital", "Promoter Committee & Legal Advisor", "Aligned with Cap 490 Model By-Laws", "Proposed Cooperative By-Laws (4 copies)"],
                            ["3. County Vetting", "County Cooperative Officer reviews feasibility", "County Director of Cooperatives", "Economic viability assessment", "County Recommendation Letter"],
                            ["4. Application Filing", "Formal submission to Commissioner for Co-ops", "Commissioner for Cooperative Development", "Payment of statutory registration fees", "Application Form CR-1"],
                            ["5. Full Registration", "Society incorporated as body corporate", "State Department for Cooperatives", "Issuance of official registration number", "Certificate of Registration & Official Seal"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Minimum Capital Mobilization for Cooperative Registration",
                    "content": {
                        "intro": "A group of 25 smallholder avocado farmers in Murang'a want to register an avocado marketing cooperative. Their feasibility study indicates they need $\\text{KES } 500,000$ in initial share capital to secure a collection shed and digital weighing scales. The By-Laws establish a share price of $\\text{KES } 500$ per share, with a minimum mandatory subscription of 20 shares per founding member.",
                        "steps": [
                            "**Step 1: Given Information:** Target initial share capital $C_{\\text{target}} = \\text{KES } 500,000$. Number of founding members $M = 25$. Nominal price per share $P_{\\text{share}} = \\text{KES } 500$. Mandatory minimum subscription $n_{\\text{min}} = 20\\text{ shares/member}$.",
                            "**Step 2: Formula:** Mandatory Base Equity per Member: $$E_{\\text{member}} = n_{\\text{min}} \\times P_{\\text{share}}$$. Total Mandatory Base Capital: $$C_{\\text{base}} = M \\times E_{\\text{member}}$$. Capital Deficit: $$\\Delta C = C_{\\text{target}} - C_{\\text{base}}$$. Additional Shares Needed per Member: $$\\Delta n = \\frac{\\Delta C}{M \\times P_{\\text{share}}}$$.",
                            "**Step 3: Substitution:** Calculate mandatory base capital: $$E_{\\text{member}} = 20 \\times 500 = \\text{KES } 10,000$$. Total base capital = $25 \\times 10,000 = \\text{KES } 250,000$. Capital deficit $\\Delta C = 500,000 - 250,000 = \\text{KES } 250,000$.",
                            "**Step 4: Calculation:** Compute additional shares required per founder: $$\\Delta n = \\frac{250,000}{25 \\times 500} = \\frac{250,000}{12,500} = 20\\text{ additional shares}$$. Total shares required per founder = $20 + 20 = 40\\text{ shares}$. Total cash per member = $40 \\times 500 = \\text{KES } 20,000$.",
                            "**Step 5: Final Answer:** Each of the 25 founding members must subscribe to 40 shares ($\\text{KES } 20,000$ total) to mobilize the exact $\\text{KES } 500,000$ capital required for registration and facility setup.",
                            "**Step 6: Economic Interpretation & Pitfall:** Equitably spreading share subscriptions ensures solid opening liquidity. *Common Pitfall:* Allowing a single wealthy member to buy 80% of shares, which risks internal conflict despite the 1M1V rule."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Registering a Coffee Co-op in Nyeri",
                    "content": {
                        "title": "Formalizing 500 Smallholder Coffee Growers Under Cap 490",
                        "text": "In Nyeri, 500 smallholder coffee growers organized an inaugural general meeting, adopted standardized cooperative by-laws, and submitted registration papers through the Nyeri County Cooperative Officer. Upon receiving their Certificate of Registration, the society acquired a corporate bank account, took out a limited liability processing loan, and installed an eco-pulper without putting any farmer's personal land title at risk."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "How to Register and Manage a Cooperative in Kenya",
                    "content": {
                        "title": "Cooperative Registration and Governance under Cap 490",
                        "youtube_id": "GiHB5aMGLSE",
                        "url": "https://www.youtube.com/watch?v=GiHB5aMGLSE",
                        "description": "Educational guide detailing cooperative registration requirements, By-Law drafting, AGM roles, and Supervisory Committee duties under Kenyan law."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Minimum Membership for Registration",
                    "content": {
                        "question": "What is the minimum number of qualified individuals required by the Cooperative Societies Act (Cap 490) to legally form and register a primary cooperative society in Kenya?",
                        "options": [
                            "Exactly 1 person",
                            "2 partners",
                            "At least 10 persons",
                            "At least 500 persons"
                        ],
                        "correct": "C",
                        "explanation": "Section 5 of the Cooperative Societies Act (Cap 490) mandates that a primary cooperative society must have a minimum of 10 qualified members for legal registration."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Role of the Supervisory Committee",
                    "content": {
                        "question": "What is the constitutional role of the Supervisory Committee in a registered cooperative society in Kenya?",
                        "options": [
                            "To handle daily milk transport and vehicle maintenance",
                            "To act as an internal audit watchdog, inspect financial records, and report directly to the AGM to check Board abuse",
                            "To set the retail price of consumer goods in local supermarkets",
                            "To dissolve the cooperative whenever profits decrease"
                        ],
                        "correct": "B",
                        "explanation": "The Supervisory Committee consists of 3 independent members elected by the AGM to serve as an internal oversight body, auditing books and reporting directly to members."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 11 Summary Takeaways",
                    "content": {
                        "text": "1. **Statutory Threshold:** A primary cooperative requires at least 10 founding members and registered By-Laws under Cap 490.\n2. **Corporate Protection:** Registration confers body corporate status with perpetual succession and limited liability.\n3. **Supreme AGM Authority:** The AGM makes ultimate policy decisions, approves budgets, and elects committee leaders.\n4. **Internal Governance Checks:** The Supervisory Committee audits financial records independently to protect member assets."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 12: Sources of Cooperative Finance
    # =========================================================================
    {
        "unit_order": 12,
        "unit_name": "Cooperative Societies: Sources of Finance",
        "unit_description": "Share capital, entrance fees, 20% statutory reserve fund, member deposits, Cooperative Bank loans, and patronage dividend allocations.",
        "lesson_title": "Sources of Cooperative Finance",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Co-operative Bank of Kenya Branch",
                    "content": {
                        "title": "Cooperative Banking Infrastructure in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Sign_for_Cooperative_Bank_of_Kenya_near_army_barracks_at_Nyali%2C_north_of_Mombasa%2C_24_October_2022.jpg",
                        "caption": "Cooperative Bank of Kenya branding, representing the dedicated financial institution established to provide institutional credit to Kenyan cooperative societies.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 12 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the core internal and external sources of capital for cooperative societies\n- Explain the mandatory 20% Statutory Reserve Fund requirement under Cap 490\n- Distinguish between share capital, non-refundable entrance fees, and member deposits\n- Calculate annual surplus distribution between statutory reserves, share dividends, and patronage rebates"
                    }
                }
            ],
            # Card 2: Definitions & Statutory Capital Rules
            [
                {
                    "type": "definition_card",
                    "title": "Statutory Reserve Fund and Patronage Rebate",
                    "content": {
                        "term": "Statutory Reserve Fund",
                        "definition": "A mandatory, non-distributable capital reserve where every registered cooperative in Kenya must legally transfer at least 20% of its net annual surplus to protect against unforeseen business losses."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Cooperative Capital Architecture",
                    "content": {
                        "text": "Cooperative financing is structured around democratic participation:\n\n- **1. Member Share Capital:** Core permanent equity; non-withdrawable but transferable within the society.\n- **2. Entrance Fees:** Small non-refundable fees paid upon admission to cover administrative setup.\n- **3. Retained Surplus (Reserves):** Ploughed-back earnings that finance machinery and chilling tanks.\n- **4. External Credit:** Institutional development loans from the **Cooperative Bank of Kenya**."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Cooperative Capital Flow and Allocation",
                    "content": {
                        "title": "Capital Inflows, Asset Pools, and Statutory Surplus Distribution",
                        "caption": "Vector diagram detailing member equity inflows, operating asset pools, mandatory 20% statutory reserves, share dividends, and patronage rebates.",
                        "svg_content": SVG_COOPERATIVE_FINANCE_CAPITAL_FLOW
                    }
                }
            ],
            # Card 4: Cooperative Finance Sources Table
            [
                {
                    "type": "comparison_table",
                    "title": "Capital Sources and Allocation Rules for Kenyan Cooperatives",
                    "content": {
                        "headers": ["Financial Source", "Category", "Legal / Operational Characteristic", "Statutory Rule under Cap 490", "Cost to Cooperative"],
                        "rows": [
                            ["Member Share Capital", "Internal Equity", "Permanent risk capital; non-withdrawable", "Individual shareholding capped at 20% of total", "Dividends paid from net surplus"],
                            ["Entrance / Joining Fees", "Internal Equity", "One-off non-refundable admission levy", "Credited to reserve or administrative account", "Zero cost (Non-refundable income)"],
                            ["Statutory Reserve Fund", "Internal Reserve", "Mandatory permanent safety cushion", "MINIMUM 20% of net annual surplus", "Zero cost (Retained internally)"],
                            ["Member Monthly Deposits", "Internal Debt/Savings", "Withdrawable savings backing loan multiplier", "Regulated by SASRA for deposit-taking SACCOs", "Interest paid on deposits (e.g. 8-12%)"],
                            ["Cooperative Bank Loans", "External Debt", "Long-term institutional credit for factories", "Approved by AGM and County Co-op Officer", "Commercial interest (e.g. 13-16% p.a.)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Annual Cooperative Surplus Allocation & Statutory Reserve",
                    "content": {
                        "intro": "Murang'a Dairy Cooperative Society generates a net operating surplus of $\\text{KES } 5,000,000$ in Year 3. Under the Cooperative Societies Act (Cap 490) and the society's By-Laws, the surplus must be allocated as follows: Mandatory Statutory Reserve Fund ($20\\%$), Member Share Capital Dividends ($40\\%$), Member Milk Patronage Bonus Rebate ($35\\%$), and Community Education Bursary Fund ($5\\%$).",
                        "steps": [
                            "**Step 1: Given Information:** Net operating surplus $S = \\text{KES } 5,000,000$. Statutory Reserve rate $r_{\\text{reserve}} = 20\\%$. Share Dividend rate $r_{\\text{div}} = 40\\%$. Patronage Rebate rate $r_{\\text{patron}} = 35\\%$. Community Fund rate $r_{\\text{comm}} = 5\\%$.",
                            "**Step 2: Formula:** Category Allocation: $$\\text{Amount}_i = S \\times r_i$$.",
                            "**Step 3: Substitution:**\n- Statutory Reserve: $$\\text{Reserve} = \\text{KES } 5,000,000 \\times 0.20$$\n- Share Dividends: $$\\text{Dividends} = \\text{KES } 5,000,000 \\times 0.40$$\n- Patronage Rebates: $$\\text{Patronage} = \\text{KES } 5,000,000 \\times 0.35$$\n- Community Fund: $$\\text{Community} = \\text{KES } 5,000,000 \\times 0.05$$.",
                            "**Step 4: Calculation:** Compute the respective allocations:\n- Statutory Reserve $= \\text{KES } 1,000,000$\n- Share Dividends $= \\text{KES } 2,000,000$\n- Patronage Rebates $= \\text{KES } 1,750,000$\n- Community Education Fund $= \\text{KES } 250,000$\nTotal check: $1,000,000 + 2,000,000 + 1,750,000 + 250,000 = \\text{KES } 5,000,000$.",
                            "**Step 5: Final Answer:** The society legally transfers $\\text{KES } 1,000,000$ to its permanent statutory reserve, pays $\\text{KES } 2,000,000$ in share dividends, distributes $\\text{KES } 1,750,000$ to farmers based on litres delivered, and allocates $\\text{KES } 250,000$ to local student bursaries.",
                            "**Step 6: Economic Interpretation & Pitfall:** Patronage bonuses reward economic loyalty, not just capital wealth. *Common Pitfall:* Attempting to distribute 100% of surplus as cash dividends without deducting the mandatory 20% statutory reserve, which violates Cap 490."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Financing a Milk Plant in Murang'a",
                    "content": {
                        "title": "Combining Statutory Reserves and Co-op Bank Asset Credit",
                        "text": "When Murang'a Dairy needed KES 15,000,000 to construct a modern UHT packaging plant, they did not rely on government hand-outs. They utilized KES 6,000,000 from their accumulated statutory reserve funds, raised KES 3,000,000 through a special member share capital drive, and secured a KES 6,000,000 equipment development loan from Cooperative Bank of Kenya at competitive cooperative rates."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Sources of Cooperative Finance and Surplus Distribution",
                    "content": {
                        "title": "How Cooperatives Raise Capital and Distribute Dividends",
                        "youtube_id": "ngCos392W4w",
                        "url": "https://www.youtube.com/watch?v=ngCos392W4w",
                        "description": "Comprehensive pedagogical video analyzing share capital, statutory reserves, patronage refunds, and Cooperative Bank loan structures."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Mandatory Statutory Reserve",
                    "content": {
                        "question": "Under the Cooperative Societies Act of Kenya (Cap 490), what minimum percentage of a society's net annual operating surplus must be transferred to the Statutory Reserve Fund?",
                        "options": [
                            "At least 5%",
                            "At least 20%",
                            "Exactly 50%",
                            "100% (No dividends allowed)"
                        ],
                        "correct": "B",
                        "explanation": "Section 47 of the Cooperative Societies Act (Cap 490) legally mandates that every registered cooperative society must transfer at least 20% of its annual net surplus to a statutory reserve fund."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Patronage Bonus Mechanism",
                    "content": {
                        "question": "How is a 'Patronage Bonus (Rebate)' calculated and distributed to members of a dairy cooperative society in Kenya?",
                        "options": [
                            "Equally to all registered members regardless of whether they own cows",
                            "In proportion to the volume of milk (litres) that each member delivered to the society during the year",
                            "Strictly based on who has the largest bank account",
                            "Only to the members of the Board of Directors"
                        ],
                        "correct": "B",
                        "explanation": "Patronage bonuses reward active business participation; they are calculated proportionally based on the volume of produce delivered or services utilized by each member."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 12 Summary Takeaways",
                    "content": {
                        "text": "1. **Permanent Member Equity:** Share capital forms the permanent equity base and cannot be withdrawn.\n2. **Mandatory 20% Reserve:** Statutory reserves are non-distributable safety funds mandated by Cap 490.\n3. **Dual Surplus Distribution:** Cooperatives reward both capital (share dividends) and active usage (patronage rebates).\n4. **Institutional Partnership:** The Cooperative Bank of Kenya serves as the dedicated financier for cooperative industrial expansion."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 13: Advantages and Disadvantages of a Cooperative
    # =========================================================================
    {
        "unit_order": 13,
        "unit_name": "Cooperative Societies: Advantages and Disadvantages",
        "unit_description": "Evaluating limited liability, bulk economies of scale, and democratic equality against slow consensus, managerial incompetence, and external capital barriers.",
        "lesson_title": "Advantages and Disadvantages of a Cooperative",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Community Gathering and Deliberation in Kenya",
                    "content": {
                        "title": "Democratic Member Deliberations in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Waiting_for_Safari_Doctors_to_Arrive_%28Credit_Tojo_Andrianarivo%29.jpg",
                        "caption": "Community members participating in collective decision-making, representing the democratic strength and consensus-building challenges of cooperative societies.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 13 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Systematically evaluate the core advantages and structural disadvantages of cooperative societies\n- Explain how limited liability and economies of scale protect and enrich smallholders\n- Analyze the causes of slow decision-making, political interference, and management weaknesses\n- Recommend governance reforms to safeguard cooperative enterprises against fraud and member apathy"
                    }
                }
            ],
            # Card 2: Definitions & Dual Evaluation
            [
                {
                    "type": "definition_card",
                    "title": "Economies of Scale and Member Apathy",
                    "content": {
                        "term": "Economies of Bulk Purchasing",
                        "definition": "The substantial cost savings achieved when a cooperative society buys large wholesale volumes of farm inputs (fertilizers, seeds, animal feeds) directly from manufacturers at discounted prices."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Democratic Promise vs. Operational Friction",
                    "content": {
                        "text": "Cooperative societies represent a powerful socio-economic model with distinct institutional trade-offs:\n\n- **The Democratic Promise:** Limited liability shields members' personal land; equal voting (1M1V) ensures fair representation; bulk marketing generates higher household returns.\n- **The Operational Friction:** Decision-making is slow because hundreds of members must approve major proposals; committee leaders are sometimes elected based on local popularity rather than business acumen."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Cooperative Benefits vs Challenges Matrix",
                    "content": {
                        "title": "Evaluating Institutional Strengths Against Operational Vulnerabilities",
                        "caption": "Vector balance matrix contrasting 5 key benefits (Limited Liability, Bulk Economies, Democratic Equality) against 5 core vulnerabilities (Slow Decisions, Political Interference, Capital Caps).",
                        "svg_content": SVG_COOPERATIVE_BENEFITS_AND_CHALLENGES
                    }
                }
            ],
            # Card 4: Advantages & Disadvantages Matrix Table
            [
                {
                    "type": "comparison_table",
                    "title": "Systematic Evaluation of Cooperative Societies in Kenya",
                    "content": {
                        "headers": ["Dimension", "Advantage (The Institutional Strength)", "Disadvantage (The Structural Vulnerability)", "Practical Governance Remedy"],
                        "rows": [
                            ["Liability Regime", "Limited Liability protects personal farm & home", "Risk of bad debt defaulting on society assets", "Rigorous credit vetting & loan guarantees"],
                            ["Governance", "Democratic control (One Member, One Vote)", "Slow consensus & political AGM interference", "Standardized AGM rules & quorum bylaws"],
                            ["Input Purchasing", "Massive economies of bulk purchasing (fertilizers)", "Inventory spoilage if demand miscalculated", "Hire qualified supply chain managers"],
                            ["Leadership Quality", "Leaders elected from local farming community", "Unskilled committee members managing complex funds", "Mandatory leadership training by County Officers"],
                            ["Capital Attraction", "Steady internal savings from thousands of members", "Big external investors avoid 1M1V voting caps", "Partner with development banks & Co-op Bank"],
                            ["Succession & Life", "Perpetual succession; society never dies", "Member apathy can lead to management capture", "Maintain transparent digital SMS financial updates"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Bulk Purchasing Economies of Scale for Fertilizer",
                    "content": {
                        "intro": "A coffee cooperative society in Nyeri comprises $200\\text{ smallholder farmers}$. Each farmer requires $8\\text{ bags}$ of planting fertilizer per season (Total $= 1,600\\text{ bags}$). Individually, local agro-vets charge $\\text{KES } 6,200\\text{ per bag}$. By purchasing an entire 1,600-bag truckload directly from a major fertilizer importer, the cooperative negotiates a wholesale price of $\\text{KES } 4,800\\text{ per bag}$ plus $\\text{KES } 150\\text{ per bag}$ for bulk transport to the society store.",
                        "steps": [
                            "**Step 1: Given Information:** Number of farmers $N_{\\text{farmers}} = 200$. Bags per farmer $b = 8\\text{ bags}$. Total bags $Q = 200 \\times 8 = 1,600\\text{ bags}$. Retail individual price $P_{\\text{retail}} = \\text{KES } 6,200\\text{ / bag}$. Co-op bulk wholesale price $P_{\\text{wholesale}} = \\text{KES } 4,800\\text{ / bag}$. Bulk transport cost $C_{\\text{trans}} = \\text{KES } 150\\text{ / bag}$.",
                            "**Step 2: Formula:** Total Individual Purchase Cost: $$C_{\\text{individual}} = Q \\times P_{\\text{retail}}$$. Total Cooperative Landed Cost: $$P_{\\text{coop}} = P_{\\text{wholesale}} + C_{\\text{trans}}$$; $$C_{\\text{coop}} = Q \\times P_{\\text{coop}}$$. Total Community Savings: $$\\Delta C = C_{\\text{individual}} - C_{\\text{coop}}$$. Per-Farmer Cash Savings: $$S_{\\text{farmer}} = \\frac{\\Delta C}{N_{\\text{farmers}}}$$.",
                            "**Step 3: Substitution:**\n- Individual total cost $= 1,600 \\times 6,200 = \\text{KES } 9,920,000$\n- Co-op unit landed cost $= 4,800 + 150 = \\text{KES } 4,950\\text{ / bag}$\n- Co-op total cost $= 1,600 \\times 4,950 = \\text{KES } 7,920,000$.",
                            "**Step 4: Calculation:** Compute total community savings: $$\\Delta C = \\text{KES } 9,920,000 - \\text{KES } 7,920,000 = \\text{KES } 2,000,000$$.\nPer-farmer savings: $$S_{\\text{farmer}} = \\frac{\\text{KES } 2,000,000}{200} = \\text{KES } 10,000\\text{ per farmer}$$. Unit savings per bag = $6,200 - 4,950 = \\text{KES } 1,250\\text{ / bag}$.",
                            "**Step 5: Final Answer:** The cooperative saves its community a staggering $\\text{KES } 2,000,000$ in cash, putting $\\text{KES } 10,000$ back into every farmer's household budget.",
                            "**Step 6: Economic Interpretation & Pitfall:** Bulk purchasing eliminates agro-dealer retail markups directly. *Common Pitfall:* Delayed fertilizer deliveries due to committee procurement arguments, causing farmers to miss the planting rains."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Overcoming Audit & Fraud Challenges in Nairobi Housing Co-op",
                    "content": {
                        "title": "Restoring Member Confidence Through Digital Transparency",
                        "text": "A 2,000-member urban transport cooperative in Nairobi suffered from financial mismanagement when manual receipt books allowed dishonest clerks to siphon member savings. Following an audit by the County Cooperative Officer, members elected a professional supervisory committee and implemented an automated mobile payment integration (Paybill to core banking). Real-time SMS receipts restored 100% financial transparency, and loan defaults dropped by 45%."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Advantages and Challenges of Cooperative Societies",
                    "content": {
                        "title": "Cooperative Economics: Strengths, Weaknesses, and Governance",
                        "youtube_id": "WqlX5z6k4eQ",
                        "url": "https://www.youtube.com/watch?v=WqlX5z6k4eQ",
                        "description": "Detailed lesson exploring limited liability protection, bulk bargaining power, managerial challenges, and SASRA regulatory oversight."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Capital Attraction Limitation",
                    "content": {
                        "question": "Why do large venture capital firms and wealthy private investors rarely invest millions of shillings in cooperative societies in Kenya?",
                        "options": [
                            "Cooperatives are legally barred from making any profit",
                            "Under the 'One Member, One Vote' principle and 20% shareholding caps, a wealthy investor who contributes 50% of the funds still gets only ONE vote and cannot control the Board",
                            "Cooperatives are only allowed to operate in rural areas",
                            "The law requires all cooperative profits to be given to the government"
                        ],
                        "correct": "B",
                        "explanation": "Wealthy commercial investors demand voting power proportional to their capital investment. The democratic 1M1V principle prevents external capital from controlling the cooperative."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Limited Liability Benefit",
                    "content": {
                        "question": "If a registered dairy cooperative society in Nyandarua goes bankrupt owing KES 10,000,000 to a commercial bank, what can the bank legally seize from an ordinary member?",
                        "options": [
                            "The member's personal family farm, residential house, and dairy cows",
                            "Only the member's invested share capital in the cooperative; the member's personal land and home are completely protected",
                            "The member's children's school certificates",
                            "The member's national identification card"
                        ],
                        "correct": "B",
                        "explanation": "A registered cooperative is a separate legal entity with limited liability. Members are liable only up to the unpaid value of their shares; their personal private assets cannot be seized."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 13 Summary Takeaways",
                    "content": {
                        "text": "1. **Limited Liability Shield:** Protects personal household land and wealth from commercial default.\n2. **Bulk Economies:** Unlocks millions in community savings on fertilizer, seeds, and animal feed purchases.\n3. **Democratic Friction:** Large AGMs and democratic consensus can cause operational and procurement delays.\n4. **Professional Management:** Hiring qualified executives and digital automation are essential to prevent management fraud."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 14: Comprehensive Ownership Comparison
    # =========================================================================
    {
        "unit_order": 14,
        "unit_name": "Integrated Ownership: Comprehensive Master Comparison",
        "unit_description": "Master 7-dimensional comparative analysis: Sole Proprietorship vs Partnership vs Cooperative Society across legal, financial, managerial, and risk parameters.",
        "lesson_title": "Comprehensive Ownership Comparison",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Multi-Tier Commercial Enterprise in Nairobi City Market",
                    "content": {
                        "title": "Commercial Enterprise Spectrum in Nairobi",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "Nairobi City Market showcasing sole retail traders, partnership wholesale dealers, and cooperative producer unions trading under one roof.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 14 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Compare Sole Proprietorships, Partnerships, and Cooperative Societies across 7 legal and operational dimensions\n- Evaluate differences in legal personality, liability, ownership limits, and decision speed\n- Calculate net retained profit and reserve allocations across all three ownership structures\n- Synthesize comparative trade-offs to guide professional business structuring decisions"
                    }
                }
            ],
            # Card 2: Definitions & Master Framework
            [
                {
                    "type": "definition_card",
                    "title": "Legal Personality and Corporate Persona",
                    "content": {
                        "term": "Corporate Personality (Separate Legal Entity)",
                        "definition": "The legal recognition that a business exists independently of its owners, allowing it to own property, enter contracts, sue, and be sued in its own registered name."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Master Tripartite Comparative Framework",
                    "content": {
                        "text": "The three forms of business ownership occupy distinct strategic tiers:\n\n- **Sole Proprietorship (Micro Agility):** 1 owner, no separate entity, unlimited liability, instant decisions, 100% profits, zero continuity.\n- **Partnership (Professional Synergy):** 2-20/50 partners, no separate entity, joint & several unlimited liability, shared management, profit ratio splits, low continuity.\n- **Cooperative Society (Community Power):** 10+ members, separate legal entity, limited liability, democratic 1M1V, 20% statutory reserve, permanent continuity."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Master Ownership Comparison Grid",
                    "content": {
                        "title": "Direct Systematic Comparison Across 7 Fundamental Dimensions",
                        "caption": "Comprehensive vector comparison grid analyzing Sole Proprietorships, Partnerships, and Cooperatives across Legal Status, Liability, Governance, and Profit Sharing.",
                        "svg_content": SVG_MASTER_OWNERSHIP_COMPARISON_MATRIX
                    }
                }
            ],
            # Card 4: Master 7-Dimension Comparative Table
            [
                {
                    "type": "comparison_table",
                    "title": "Master Comparative Matrix: Forms of Business Ownership",
                    "content": {
                        "headers": ["Comparative Dimension", "Sole Proprietorship", "Partnership", "Cooperative Society"],
                        "rows": [
                            ["1. Number of Owners", "Exactly 1 individual", "2 to 20 (up to 50 for professions)", "Minimum 10 (No upper limit)"],
                            ["2. Legal Status", "No separate legal entity", "No separate legal entity", "Separate Legal Entity (Body Corporate)"],
                            ["3. Liability Regime", "Unlimited (Personal assets exposed)", "Unlimited Joint & Several", "Limited (Shares at risk only)"],
                            ["4. Management & Control", "Sole owner (Total autonomy)", "Shared by active partners", "Democratic AGM & Management Committee"],
                            ["5. Voting Power", "100% owner authority", "Consensus or agreed deed majority", "One Member, One Vote (1M1V)"],
                            ["6. Business Continuity", "Very Low (Dissolves with owner)", "Low (Dissolved on death/exit)", "Permanent (Perpetual Succession)"],
                            ["7. Profit / Surplus Sharing", "Owner retains 100% of profit", "Shared based on agreed ratio (e.g. 3:2)", "20% Reserve + Dividends & Patronage"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Comparative Financial Returns Across Ownership Models",
                    "content": {
                        "intro": "Evaluate how a net profit / surplus of $\\text{KES } 1,000,000$ is distributed across three alternative business structures: Model A (Sole Trader), Model B (2-Partner Firm with $3:2$ ratio), and Model C (Cooperative with $20\\%$ statutory reserve, $40\\%$ dividends across 1,000 shares, and $40\\%$ patronage across 50,000 delivered units).",
                        "steps": [
                            "**Step 1: Given Information:** Net financial surplus $\\Pi = \\text{KES } 1,000,000$. Model A: 1 owner. Model B: Partner 1 ($60\\%$), Partner 2 ($40\\%$). Model C: 20% statutory reserve, 40% dividends, 40% patronage.",
                            "**Step 2: Model A Calculation (Sole Proprietorship):** The sole proprietor retains 100% of earnings: $$\\Pi_{\\text{sole}} = \\text{KES } 1,000,000$$.",
                            "**Step 3: Model B Calculation (Partnership):**\n- Partner 1 ($60\\%$): $$0.60 \\times 1,000,000 = \\text{KES } 600,000$$\n- Partner 2 ($40\\%$): $$0.40 \\times 1,000,000 = \\text{KES } 400,000$$\nTotal $= \\text{KES } 1,000,000$.",
                            "**Step 4: Model C Calculation (Cooperative Society):**\n- Mandatory Statutory Reserve ($20\\%$): $$0.20 \\times 1,000,000 = \\text{KES } 200,000\\text{ (Retained)}$$\n- Share Dividend Pool ($40\\%$): $$0.40 \\times 1,000,000 = \\text{KES } 400,000$$\n- Patronage Rebate Pool ($40\\%$): $$0.40 \\times 1,000,000 = \\text{KES } 400,000$$\n- Dividend per share $= \\frac{400,000}{1,000} = \\text{KES } 400\\text{ / share}$\n- Patronage per unit $= \\frac{400,000}{50,000} = \\text{KES } 8\\text{ / unit}$.",
                            "**Step 5: Final Answer:** Sole trader gets $\\text{KES } 1,000,000$ cash; partners receive $\\text{KES } 600,000$ and $\\text{KES } 400,000$; cooperative builds a $\\text{KES } 200,000$ permanent safety reserve while returning $\\text{KES } 800,000$ to members based on shares and production.",
                            "**Step 6: Economic Interpretation & Pitfall:** Individual profit incentives dominate private firms, while cooperatives balance member returns with permanent institutional capitalization."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Selecting the Right Vehicle in Eldoret",
                    "content": {
                        "title": "Tailoring Ownership Structures to Specific Commercial Missions",
                        "text": "In Eldoret, three distinct enterprises operate side-by-side: Kipchoge's tailoring shop operates as a sole proprietorship for instant daily customization; Eldoret Orthopedic Associates operates as a partnership to pool surgical skills and equipment debt; and the Uasin Gishu Grain Farmers Cooperative operates as a 3,000-member cooperative with 4 silo complexes and limited liability."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Comparing Types of Business Ownership",
                    "content": {
                        "title": "Sole Proprietorship vs Partnership vs Cooperative Societies",
                        "youtube_id": "yoY_uH8-l6Y",
                        "url": "https://www.youtube.com/watch?v=yoY_uH8-l6Y",
                        "description": "Comprehensive comparative lecture analyzing legal entity status, liability differences, capital mobilization, and governance structures."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Comparing Legal Status",
                    "content": {
                        "question": "Which of the following business ownership forms possesses 'Separate Legal Personality' (the business exists independently of its owners under law)?",
                        "options": [
                            "A Sole Proprietorship only",
                            "A General Partnership only",
                            "A Registered Cooperative Society",
                            "Both a Sole Proprietorship and a General Partnership"
                        ],
                        "correct": "C",
                        "explanation": "A registered cooperative society is incorporated as a body corporate with separate legal personality and perpetual succession, whereas sole proprietorships and general partnerships have no separate legal existence."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Decision Speed vs Capital Capacity",
                    "content": {
                        "question": "An entrepreneur prioritizes 100% decision-making speed, total business privacy, and keeping all profits, but only has KES 20,000 in capital. Which ownership form is best aligned?",
                        "options": [
                            "A Cooperative Society",
                            "A Sole Proprietorship",
                            "A Public Limited Company",
                            "A Housing Cooperative"
                        ],
                        "correct": "B",
                        "explanation": "The sole proprietorship provides absolute decision speed, complete privacy, and 100% profit retention, perfectly matching low capital and single-founder requirements."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 14 Summary Takeaways",
                    "content": {
                        "text": "1. **Entity Divide:** Sole traders and general partnerships lack separate legal personality; cooperatives are bodies corporate.\n2. **Liability Exposure:** Sole traders and partners bear unlimited debt liability; cooperative members enjoy limited liability.\n3. **Governance Model:** Sole traders control unilaterally, partners govern by deed consensus, and cooperatives vote by 1M1V.\n4. **Continuity Guarantee:** Only registered cooperatives possess permanent perpetual succession independent of founder life cycles."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 15: Ownership and Local Economic Development
    # =========================================================================
    {
        "unit_order": 15,
        "unit_name": "Integrated Ownership: Role in Local Economic Development",
        "unit_description": "Analyzing how sole traders, partnerships, and cooperatives drive grassroots employment, financial inclusion, wealth redistribution, and county GDP growth.",
        "lesson_title": "Ownership and Local Economic Development",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Kenyan Urban and Rural Economic Landscape",
                    "content": {
                        "title": "Economic Dynamism across Kenyan Counties",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Buffalo_Nairobi_Skyline_Savannah_Kenya_May19_R1600769.jpg",
                        "caption": "Kenya's vibrant commercial ecosystem, illustrating how diverse enterprise ownership forms drive national GDP and county development.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 15 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the specific economic contributions of Sole Proprietorships, Partnerships, and Cooperatives to Kenyan county economies\n- Analyze the role of micro-enterprises in self-employment and grassroots poverty reduction\n- Describe how professional partnerships build essential regional medical and legal infrastructure\n- Calculate local economic multiplier effects resulting from cooperative value addition"
                    }
                }
            ],
            # Card 2: Definitions & County Economic Engines
            [
                {
                    "type": "definition_card",
                    "title": "Local Economic Multiplier and Value Addition",
                    "content": {
                        "term": "Local Economic Multiplier",
                        "definition": "The economic phenomenon where revenue generated by local enterprises is spent and re-circulated within the county, generating multiple rounds of secondary income, employment, and trade."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Tripartite Engine of County Economic Growth",
                    "content": {
                        "text": "A thriving county economy requires an integrated ecosystem of all three ownership structures:\n\n- **1. Sole Proprietorships (The Grassroots Engine):** Create self-employment for millions of youth and women, provide neighborhood convenience, and sustain daily village liquidity.\n- **2. Partnerships (The Collaborative Builders):** Pool specialized human and financial capital to build regional medical clinics, audit firms, private academies, and engineering practices.\n- **3. Cooperative Societies (The Community Fortresses):** Mobilize billions in rural savings, eliminate exploitative agricultural middlemen, and redistribute processing profits back into farming households."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "County Economic Development Ecosystem",
                    "content": {
                        "title": "How Ownership Forms Catalyze Kenya Vision 2030",
                        "caption": "Vector ecosystem diagram illustrating how micro sole traders, collaborative partnerships, and community cooperatives drive employment, infrastructure, and wealth creation.",
                        "svg_content": SVG_LOCAL_ECONOMIC_DEVELOPMENT_ECOSYSTEM
                    }
                }
            ],
            # Card 4: County Impact Matrix Table
            [
                {
                    "type": "comparison_table",
                    "title": "Socio-Economic Contributions Matrix by Ownership Form",
                    "content": {
                        "headers": ["Ownership Structure", "Primary Economic Mandate", "Employment Impact", "Infrastructure Contribution", "County Revenue Source"],
                        "rows": [
                            ["Sole Proprietorship", "Grassroots trade & last-mile retail distribution", "Massive youth/women self-employment (Millions of jobs)", "Neighborhood kiosks, bodas & dukas", "County Single Business Permits & market cesses"],
                            ["Partnership", "Specialized professional & technical services", "High-value skilled jobs (Nurses, clerks, technicians)", "Private hospitals, legal firms, audit offices", "Commercial rates & professional county licensing"],
                            ["Cooperative Society", "Smallholder aggregation & financial inclusion", "Factory workers, drivers, agronomists & accountants", "Milk cooling plants, coffee pulpers, SACCO plazas", "Cooperative cesses & statutory county development levies"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating County Income Multiplier from Cooperative Processing",
                    "content": {
                        "intro": "A dairy cooperative society in Meru County establishes a modern milk chilling plant. The plant hires 12 local youths at a monthly wage of $\\text{KES } 25,000$ each (Monthly payroll $= 12 \\times 25,000 = \\text{KES } 300,000$). Economic research in Meru indicates a local marginal propensity to consume locally of $c = 0.625$, yielding an economic expenditure multiplier of $k = \\frac{1}{1 - c} = \\frac{1}{1 - 0.625} = 2.67$.",
                        "steps": [
                            "**Step 1: Given Information:** Initial monthly direct injection (payroll) $\\Delta J = \\text{KES } 300,000$. Local expenditure multiplier $k = 2.67$. Number of direct jobs $= 12$.",
                            "**Step 2: Formula:** Total County Economic Stimulus Generated: $$\\Delta Y = \\Delta J \\times k$$. Annual County Economic Stimulus: $$\\Delta Y_{\\text{annual}} = \\Delta Y \\times 12$$.",
                            "**Step 3: Substitution:** Calculate monthly total economic impact: $$\\Delta Y = \\text{KES } 300,000 \\times 2.67$$.",
                            "**Step 4: Calculation:** Compute monthly and annual stimulus:\n- Monthly total stimulus $$\\Delta Y = \\text{KES } 801,000$$\n- Annual total stimulus $$\\Delta Y_{\\text{annual}} = 801,000 \\times 12 = \\text{KES } 9,612,000$$.",
                            "**Step 5: Final Answer:** The cooperative's direct payroll injection of $\\text{KES } 300,000$ per month generates an estimated $\\text{KES } 801,000$ in total monthly business revenue (over $\\text{KES } 9.6\\text{ million}$ annually) for local grocers, landlords, bodas, and shops in the county.",
                            "**Step 6: Economic Interpretation & Pitfall:** Local enterprise wages create secondary demand across the entire county economy. *Common Pitfall:* Viewing factory payroll as a mere cost rather than an engine of community economic circulation."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Meru Central Dairy Co-operative Union",
                    "content": {
                        "title": "Catalyzing Regional Industrialization and Livelihoods in Mt. Kenya",
                        "text": "Meru Central Dairy Co-operative Union (producers of Mount Kenya Milk) processes over 300,000 litres of milk daily from over 150 primary dairy societies. Beyond paying billions in milk proceeds to farmers, the union operates animal feed processing mills, veterinary supply stores, and a SACCO, providing direct employment to over 600 staff and supporting over 100,000 rural families across Meru and Tharaka Nithi counties."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Enterprise Ownership and Kenyan Economic Development",
                    "content": {
                        "title": "How Business Ownership Drives County Economies in Kenya",
                        "youtube_id": "3jwAGWky98c",
                        "url": "https://www.youtube.com/watch?v=3jwAGWky98c",
                        "description": "Educational documentary examining how sole traders, professional partnerships, and agricultural cooperatives power Kenya Vision 2030."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Sole Traders and Employment",
                    "content": {
                        "question": "What is the primary contribution of sole proprietorship kiosks, salonists, and boda boda operators to Kenya's national economy?",
                        "options": [
                            "They manufacture large commercial airplanes for export",
                            "They absorb millions of job seekers through self-employment, provide essential last-mile goods, and generate daily household livelihoods",
                            "They print the official legal tender banknotes",
                            "They manage national monetary policy on behalf of the Central Bank"
                        ],
                        "correct": "B",
                        "explanation": "Sole proprietorships form the bedrock of the micro, small, and medium enterprise (MSME) sector, absorbing over 80% of Kenya's working population through self-employment."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Cooperatives and Wealth Redistribution",
                    "content": {
                        "question": "How do agricultural cooperative societies in Kenyan counties ensure that wealth is redistributed directly into rural community households?",
                        "options": [
                            "By transferring all profits to foreign stock markets",
                            "By paying annual surpluses back to member farmers as cash dividends and production-based patronage rebates",
                            "By converting all farms into national wildlife reserves",
                            "By legally banning farmers from spending cash locally"
                        ],
                        "correct": "B",
                        "explanation": "Cooperative surplus distribution returns economic gains directly to grassroots producers through patronage bonuses and share dividends, empowering local household purchasing power."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 15 Summary Takeaways",
                    "content": {
                        "text": "1. **Grassroots Absorption:** Sole traders provide immediate self-employment and essential last-mile consumer convenience.\n2. **Skilled Infrastructure:** Partnerships establish vital private healthcare, legal, auditing, and engineering clinics.\n3. **Rural Wealth Power:** Cooperatives aggregate farm produce, add industrial value, and distribute surpluses to households.\n4. **Integrated Multiplier:** The coexistence of all three ownership models maximizes county GDP and supports Kenya Vision 2030."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 16: Practical Case-Study Recommendation
    # =========================================================================
    {
        "unit_order": 16,
        "unit_name": "Integrated Ownership: Practical Business Structuring Case Study",
        "unit_description": "Applied enterprise structuring simulation: Evaluating founder skills, capital requirements, liability risk, and governance to select the optimal legal business form.",
        "lesson_title": "Practical Case-Study Recommendation",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Corporate Financial Institutions in Kenya",
                    "content": {
                        "title": "Enterprise Structuring and Corporate Advisory in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Bank_of_India_%28Kenya%29%2C_Nairobi_Branch%2C_2025_%2801%29.jpg",
                        "caption": "An institutional commercial banking branch in Nairobi, representing the corporate and legal structuring required for expanding enterprises.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 16 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Apply a structured decision protocol to select the optimal business ownership form for real-world entrepreneurial scenarios\n- Evaluate capital size, liability tolerance, founder count, and regulatory burden in entity structuring\n- Conduct multi-criteria feasibility analyses across Sole Proprietorship, Partnership, Cooperative, and Limited Company models\n- Formulate professional, legally sound business ownership recommendations"
                    }
                }
            ],
            # Card 2: Definitions & Strategic Advisory Protocol
            [
                {
                    "type": "definition_card",
                    "title": "Business Structuring and Limited Liability Company (LLC)",
                    "content": {
                        "term": "Limited Liability Company (LLC / Ltd)",
                        "definition": "An incorporated commercial business structure registered under the Companies Act where ownership is divided into shares, granting full limited liability protection to shareholders while pooling multi-founder capital."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Diagnostic Ownership Selection Protocol",
                    "content": {
                        "text": "When advising entrepreneurs on business ownership, follow a 4-step diagnostic protocol:\n\n- **Step 1 — Founder Count:** Exactly 1 (Sole Trader); 2 to 20/50 (Partnership / LLC); 10+ producers/savers (Cooperative).\n- **Step 2 — Liability & Asset Exposure:** Low risk (Sole Trader / Partnership); High risk with machinery/loans (Must have Limited Liability via LLC or Cooperative).\n- **Step 3 — Capital Scale:** Small localized (Personal savings / Trade credit); Large industrial (Pooled shares / Institutional credit).\n- **Step 4 — Governance Preference:** Full solo control (Sole Trader); Deed consensus (Partnership); Democratic 1M1V (Cooperative)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Entrepreneurial Ownership Decision Tree",
                    "content": {
                        "title": "Diagnostic Protocol for Selecting the Optimal Business Entity",
                        "caption": "Vector decision flowchart mapping founder count, liability tolerance, capital requirements, and governance structures to the optimal business ownership form.",
                        "svg_content": SVG_OWNERSHIP_DECISION_TREE
                    }
                }
            ],
            # Card 4: Decision Criteria Matrix Table
            [
                {
                    "type": "comparison_table",
                    "title": "Structured Ownership Selection Guide for Real-World Scenarios",
                    "content": {
                        "headers": ["Scenario Parameters", "Sole Proprietorship", "General Partnership", "Cooperative Society", "Limited Company (LLC)"],
                        "rows": [
                            ["Founders: Exactly 1 person", "OPTIMAL (Full control & speed)", "Not Feasible (Min 2 required)", "Not Feasible (Min 10 required)", "Feasible (Single-member company)"],
                            ["Founders: 2 to 5 professionals", "Not Feasible (Excludes founders)", "OPTIMAL if mutual trust exists", "Not Feasible (Min 10 required)", "OPTIMAL if high liability exists"],
                            ["Founders: 500 small farmers", "Not Feasible", "Not Feasible (Max 20/50 limit)", "OPTIMAL (Democratic 1M1V)", "Feasible but complex for farmers"],
                            ["High debt / machinery risk", "High Danger (Unlimited liability)", "High Danger (Joint & several debt)", "Protected (Limited liability)", "OPTIMAL (Full limited liability)"],
                            ["Startup budget under KES 10,000", "OPTIMAL (Low eCitizen fees)", "Feasible (Needs deed fee)", "Not Feasible (High base capital)", "Higher incorporation fees"],
                            ["Primary Goal: 100% secrecy", "OPTIMAL (Private records)", "OPTIMAL between partners", "Not Feasible (Audited accounts)", "Filing annual returns required"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Advisory Case Study — Narok Organic Animal Feed Enterprise",
                    "content": {
                        "intro": "Three young agricultural graduates in Narok—Amina (Animal Nutritionist), Brian (Marketer), and Chuma (Farmer with 5 acres)—want to launch 'Maasai Feed Mills' to manufacture cattle feed from local maize stalks. They need $\\text{KES } 1,500,000$ to purchase an industrial milling machine and hire a truck driver. Key Condition: All three founders insist that their personal family land and private savings must be $100\\%$ protected from any machine injury lawsuits or bank loan default.",
                        "steps": [
                            "**Step 1: Analyze Business Requirements:**\n- Number of founders $= 3$ individuals (Amina, Brian, Chuma)\n- Capital requirement $= \\text{KES } 1,500,000$ (Heavy machinery & operating capital)\n- Specialized complementary skills: Nutrition + Marketing + Land Asset\n- Non-negotiable condition: Mandatory **Limited Liability Protection** for personal wealth.",
                            "**Step 2: Feasibility Evaluation Option 1 (Sole Proprietorship):**\n- *Feasibility:* Failed. A sole proprietorship can have only 1 owner, excluding two founders. It carries dangerous unlimited liability.",
                            "**Step 3: Feasibility Evaluation Option 2 (General Partnership):**\n- *Feasibility:* High operational fit (3 founders pool skills and capital), but *Fails Non-Negotiable Condition* due to **joint and several unlimited liability** under the Partnership Act.",
                            "**Step 4: Feasibility Evaluation Option 3 (Cooperative Society):**\n- *Feasibility:* Failed. A primary cooperative legally requires a minimum of 10 members under Cap 490, but they are only 3 founders.",
                            "**Step 5: Feasibility Evaluation Option 4 (Limited Liability Company / LLP):**\n- *Feasibility:* Perfect Fit. A private limited company (or Limited Liability Partnership) accommodates 3 founders, pools specialized equity shares, and provides the shield of **limited liability** protecting personal family assets.",
                            "**Step 6: Final Recommendation & Rationale:** Amina, Brian, and Chuma must register 'Maasai Feed Mills Ltd' as a **Private Limited Liability Company (LLC)** on eCitizen. This structure pools their KES 1,500,000, allocates equity shares (e.g. $40\\%:30\\%:30\\%$), and ensures their personal assets remain 100% safe from business liabilities."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Nyandarua Potato Farmers Community Structuring",
                    "content": {
                        "title": "Advising 500 Smallholders to Transition from Informal Groups to a Cooperative",
                        "text": "In Nyandarua, 500 smallholder potato farmers were losing 40% of their harvest to post-harvest rotting and broker price exploitation. An enterprise advisory team evaluated their options: a partnership was illegal due to the 20-member cap, and a joint-stock company would allow wealthy outside investors to buy out the farmers. The farmers registered the 'Nyandarua Potato Growers Cooperative Society', installed cold storage silos, and secured supply contracts with national crisp manufacturers."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Choosing the Best Business Structure",
                    "content": {
                        "title": "How to Choose Between Sole Proprietorship, Partnership, and Limited Company",
                        "youtube_id": "qgVFkRn8f10",
                        "url": "https://www.youtube.com/watch?v=qgVFkRn8f10",
                        "description": "Comprehensive practical case-study tutorial guiding entrepreneurs on evaluating liability, tax, capital, and governance when structuring a new business."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Structuring Multi-Founder High-Risk Firm",
                    "content": {
                        "question": "Four software engineers want to launch a fintech app in Nairobi. They need KES 3,000,000 in server infrastructure and want to ensure their personal savings are completely protected if the app experiences a data breach. Which ownership form must they choose?",
                        "options": [
                            "A Sole Proprietorship",
                            "A General Partnership",
                            "A Private Limited Liability Company (LLC)",
                            "A Consumer Cooperative Society"
                        ],
                        "correct": "C",
                        "explanation": "A Private Limited Company (LLC) allows multiple founders (2 to 50) to pool capital while legally shielding their personal private assets through the protection of limited liability."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Structuring Community Producer Groups",
                    "content": {
                        "question": "A community of 400 small-scale sunflower seed farmers in Bungoma want to collectively purchase an oil extraction press and market sunflower oil. Why is a Cooperative Society their best ownership structure?",
                        "options": [
                            "Because partnerships are legally capped at 20/50 members, whereas a cooperative accommodates hundreds of members democratically under 1M1V and provides limited liability",
                            "Because cooperative societies do not need to register with the government",
                            "Because a sole proprietorship is legally required to have 400 owners",
                            "Because sunflower oil can only be sold by foreign companies"
                        ],
                        "correct": "A",
                        "explanation": "Partnerships have a maximum legal limit of 20 or 50 members. A cooperative society has no upper limit on membership, ensures democratic equality (1M1V), and provides limited liability protection for all 400 farmers."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 16 Summary Takeaways",
                    "content": {
                        "text": "1. **Systematic Diagnostics:** Evaluate founder count, capital scale, liability risk, and governance to select business ownership.\n2. **Sole Trader Niche:** Best for single founders seeking speed, low setup cost, and total operational autonomy.\n3. **Partnership Niche:** Best for 2 to 20 trusted professionals pooling skills in low-to-moderate liability practices.\n4. **Cooperative Niche:** The supreme model for large communities of producers and savers seeking democratic empowerment and limited liability."
                    }
                }
            ]
        ]
    }
]
