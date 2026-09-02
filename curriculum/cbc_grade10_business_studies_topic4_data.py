"""
VLearn CBC Grade 10 Business Studies — Topic 4: Banking
Full Structured Lesson Card Definitions (Lessons 1 to 5)
"""

from curriculum.cbc_grade10_business_studies_topic4_svgs import (
    SVG_FINANCIAL_INTERMEDIATION,
    SVG_BANK_ACCOUNT_TYPES,
    SVG_BANKING_ETHICS_PILLARS,
    SVG_KENYA_BANKING_TRENDS,
    SVG_JUNIOR_ACCOUNT_PROCESS
)

TOPIC_4_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Importance of Banking in an Economy
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of Banking in an Economy",
        "unit_description": "The concept of commercial banking, financial intermediation, safe custody of funds, credit provision, and capital mobilization in Kenya.",
        "lesson_title": "Meaning and Importance of Banking in an Economy",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Tea Harvesting and Income Generation in Kericho, Kenya",
                    "content": {
                        "title": "Agricultural Income and Cash Mobilization",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Tea_farming_in_Kericho_09.JPG",
                        "caption": "Smallholder tea farmers picking leaves in Kericho, illustrating agricultural income generation and the vital role of local commercial banks in mobilizing cash into productive capital.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a bank, banking, and explain the core mechanism of financial intermediation\n- Explain the financial water reservoir analogy connecting savers and investors\n- Evaluate the 7 vital economic roles of commercial banks in Kenya's development\n- Calculate net interest margins and interest rate spreads earned by commercial banks"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Core Banking Terminology",
                    "content": {
                        "term": "Bank and Financial Intermediation",
                        "definition": "A bank is a licensed financial institution authorized by the Central Bank of Kenya (CBK) to receive deposits, provide safe custody, and extend credit. Financial intermediation is the process where banks act as middlemen, pooling savings from surplus units (depositors) and channeling them as loans to deficit units (investors)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Financial Water Reservoir Analogy",
                    "content": {
                        "text": "Think of a commercial bank as a giant **water reservoir**:\n\n- **Surplus Streams (Savers):** Thousands of individual citizens (like tea farmer Juma saving KES 40,000) contribute small trickles of surplus money into the bank.\n- **The Reservoir (The Bank):** The bank pools all these small deposits into a massive reservoir of capital, paying depositors a modest reward called **deposit interest**.\n- **Irrigation Pipes (Borrowers):** The bank opens large pipes to lend concentrated funds to entrepreneurs and infrastructure developers (e.g., buying industrial tea processing machines or building roads), charging a fee called **lending interest**.\n\nWithout banks, Juma's money would sit idle under a mattress exposed to theft and fire, while factories would remain unbuilt due to lack of capital."
                    }
                }
            ],
            # Card 3: Deep Dive & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Financial Intermediation Mechanism & Interest Spread",
                    "content": {
                        "title": "Flow of Funds in Commercial Banking",
                        "caption": "Comprehensive architectural diagram showing how commercial banks mobilize deposits from surplus households at 4.5% interest, maintain statutory CBK reserves, and disburse commercial loans at 13.5% interest to earn a 9.0% Net Interest Margin.",
                        "svg_content": SVG_FINANCIAL_INTERMEDIATION
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "How Intermediation Drives Capital Formation",
                    "content": {
                        "text": "Commercial banks perform three indispensable economic transformations:\n\n1. **Size Transformation:** Aggregating thousands of small deposits (e.g., KES 1,000 to KES 50,000) into multi-million shilling loans required for industrial expansion.\n2. **Maturity Transformation:** Converting short-term on-demand deposits into medium and long-term business loans (3 to 10 years).\n3. **Risk Diversification:** Spreading credit risk across thousands of diverse borrowers across agriculture, retail, manufacturing, and transport so that individual loan defaults do not endanger depositors' money."
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "The 7 Vital Roles of Commercial Banks in National Economic Development",
                    "content": {
                        "headers": ["Economic Role", "Mechanism / Activity", "Impact on Kenyan Businesses", "National Development Outcome"],
                        "rows": [
                            ["1. Mobilizing Savings", "Safe custody + interest rewards on deposits", "Protects cash from fire, theft, and domestic decay", "Builds national domestic capital pool"],
                            ["2. Providing Credit", "Disbursing working capital and asset loans", "Enables purchase of machinery, stock, and land", "Expands production capacity and creates jobs"],
                            ["3. Payment Processing", "Cheques, RTGS, PesaLink, mobile integrations", "Fast, traceable, low-risk commercial settlements", "Accelerates trade velocity across counties"],
                            ["4. Capital Mobilization", "Syndicated loans and bond issuances", "Funds large-scale infrastructure (ports, energy)", "Drives long-term Vision 2030 industrialization"],
                            ["5. Risk Management", "Credit scoring, hedging, and treasury desks", "Insulates businesses against default and price shocks", "Maintains macroeconomic financial stability"],
                            ["6. International Trade", "Letters of credit and foreign currency exchange", "Allows tea/flower exports and machinery imports", "Strengthens national foreign exchange reserves"],
                            ["7. Financial Inclusion", "Agency banking and mobile wallet links", "Brings rural farmers and informal MSMEs into banking", "Reduces poverty and broadens the tax base"]
                        ]
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 4-Stage Commercial Intermediation Cycle",
                    "content": {
                        "intro": "Every commercial loan follows this regulated operational cycle:",
                        "steps": [
                            {"title": "1. Deposit Collection", "description": "Mobilizing liquid funds from households and firms across savings, current, and term deposit accounts."},
                            {"title": "2. Statutory Reserve Compliance", "description": "Retaining the mandatory Cash Reserve Ratio (CRR) dictated by the Central Bank of Kenya to ensure liquidity."},
                            {"title": "3. Credit Risk Appraisal", "description": "Evaluating the borrower's character, cash flow capacity, capital, collateral, and business conditions (5 Cs of Credit)."},
                            {"title": "4. Loan Disbursement & Monitoring", "description": "Releasing funds for productive enterprise use and collecting monthly principal plus lending interest repayments."}
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Financial Intermediation & Net Interest Margin (Spread)",
                    "content": {
                        "intro": "Kericho Community Commercial Bank mobilizes KES 5,000,000 in customer deposits from local tea farmers, offering an average deposit interest rate of 4.5% per annum. The bank lends out 80% of these deposits (KES 4,000,000) to regional tea processing factories at a lending interest rate of 13.5% per annum. The remaining 20% is held as liquid reserves.",
                        "steps": [
                            "**Step 1 — Given Parameters:**\n- Total Customer Deposits ($D$) = $\\text{KES } 5,000,000$\n- Deposit Interest Rate ($r_d$) = $4.5\\% = 0.045\\text{ p.a.}$\n- Loan Portfolio Disbursed ($L = 0.80 \\times D$) = $\\text{KES } 4,000,000$\n- Lending Interest Rate ($r_l$) = $13.5\\% = 0.135\\text{ p.a.}$",
                            "**Step 2 — Mathematical Formulas:**\n$$\\text{Annual Interest Income from Loans } (I_{\\text{income}}) = L \\times r_l$$\n$$\\text{Annual Interest Expense to Depositors } (I_{\\text{expense}}) = D \\times r_d$$\n$$\\text{Net Interest Income } (\\text{NII}) = I_{\\text{income}} - I_{\\text{expense}}$$\n$$\\text{Interest Rate Spread} = r_l - r_d$$",
                            "**Step 3 — Substitution:**\n$$I_{\\text{income}} = 4,000,000 \\times 0.135$$\n$$I_{\\text{expense}} = 5,000,000 \\times 0.045$$",
                            "**Step 4 — Step-by-Step Calculation:**\n$$I_{\\text{income}} = \\text{KES } 540,000$$\n$$I_{\\text{expense}} = \\text{KES } 225,000$$\n$$\\text{Net Interest Income } (\\text{NII}) = 540,000 - 225,000 = \\text{KES } 315,000$$\n$$\\text{Interest Rate Spread} = 13.5\\% - 4.5\\% = 9.0\\%$$",
                            "**Step 5 — Final Stated Answer:**\n- Total Annual Loan Interest Earned by the Bank: **KES 540,000**\n- Total Annual Deposit Interest Paid to Farmers: **KES 225,000**\n- Net Interest Income (Gross Operating Margin): **KES 315,000** (a **9.0%** interest rate spread).",
                            "**Step 6 — Economic Interpretation & Common Pitfall:**\n- *Economic Interpretation:* The KES 315,000 interest spread represents the bank's core revenue engine. It covers administrative operating costs (teller salaries, branch rent, cybersecurity firewalls, taxes) and provides a capital buffer against bad debts.\n- *Common Pitfall:* Never calculate lending income on 100% of total deposits. Banks cannot lend out all deposits because central bank statutory reserve regulations mandate holding liquid reserves to satisfy daily cash withdrawals."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Commercial Banking in Kericho's Tea Belt",
                    "content": {
                        "title": "Transforming Harvest Cash into Industrial Processing Capital",
                        "text": "In Kericho County, over 60,000 smallholder tea farmers deliver green leaves to Kenya Tea Development Agency (KTDA) managed factories. Historically, paying farmers in physical cash led to widespread highway robbery and loss.\n\nToday, local commercial banks (such as Equity Bank, KCB, and Co-operative Bank) open direct savings accounts for farmers. The factory electronically transfers monthly tea earnings directly into farmers' accounts. The banks then aggregate these steady agricultural deposits to issue asset financing loans to local entrepreneurs who purchase modern tea sorting, CTC cutting, and packaging machinery. This virtuous cycle demonstrates financial intermediation powering real-world industrialization."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Commercial Banking and Financial Intermediation",
                    "content": {
                        "title": "How Commercial Banks Work: Financial Intermediation & The Money Cycle",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Comprehensive educational documentary explaining the fundamentals of commercial banking, the deposit-lending mechanism, and how banks lubricate national economic growth."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Primary Function of Financial Intermediation",
                    "content": {
                        "question": "What is the primary economic function of a commercial bank acting as a 'financial intermediary' in Kenya?",
                        "options": [
                            "Printing and issuing new banknote denominations for the national government",
                            "Collecting surplus cash from depositors and lending it out to enterprises with productive investment projects",
                            "Fixing the prices of consumer goods sold in local retail supermarkets",
                            "Manufacturing heavy security vaults for physical retail stores"
                        ],
                        "correct": "B",
                        "explanation": "Financial intermediation is the middleman function where banks mobilize idle savings from surplus units (depositors) and channel them as loans to deficit units (investors) to finance productive economic activities."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Bank Interest Spread Mechanics",
                    "content": {
                        "question": "A commercial bank pays 3.0% interest per annum on customer savings accounts and charges 14.0% interest per annum on business loans. What is the bank's interest rate spread?",
                        "options": [
                            "17.0%",
                            "11.0%",
                            "4.67%",
                            "8.5%"
                        ],
                        "correct": "B",
                        "explanation": "The interest rate spread is calculated as Lending Rate minus Deposit Rate: 14.0% - 3.0% = 11.0%. This spread represents the bank's gross margin to cover operating overheads and credit risk."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Financial Intermediation**: Banks bridge the gap between surplus economic units (savers) and deficit economic units (borrowing enterprises).\n2. **The Reservoir Model**: Small individual savings trickle into the bank, creating a massive pool of capital that finances large commercial investments and infrastructure.\n3. **Core Economic Roles**: Safe custody, credit provision, payment processing, risk diversification, foreign trade facilitation, and financial inclusion.\n4. **The Interest Spread**: Banks generate operating revenue from the spread between higher lending interest rates charged to borrowers and lower deposit interest rates paid to savers."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Types of Bank Accounts
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Types of Bank Accounts",
        "unit_description": "Analyzing features, interest yields, liquidity, cheque facilities, overdrafts, and operational rules of Savings, Current, Fixed Deposit, and Junior Accounts.",
        "lesson_title": "Types of Bank Accounts",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Banking Operations in Nairobi",
                    "content": {
                        "title": "Commercial Retail Banking Services",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Bank_House_%28Nairobi%29%2C_2025_%2801%29.jpg",
                        "caption": "A premier commercial banking house in Nairobi serving corporate, retail, and small enterprise customers with tailored deposit, cheque clearing, and credit accounts.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between Savings, Current, Fixed Deposit, and Junior bank accounts\n- Identify the unique features of Current Accounts (cheque books and overdraft facilities)\n- Compare interest yield calculations between standard savings and fixed term deposits\n- Explain the definition, protective rationale, and reactivation process for dormant accounts"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Classification of Bank Accounts",
                    "content": {
                        "term": "Bank Account Taxonomy",
                        "definition": "A bank account is a formal financial arrangement between a customer and a licensed bank allowing the deposit, custody, transfer, or borrowing of money. Accounts are categorized based on liquidity, transaction volume, interest earnings, and credit facilities."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Three Customers, Three Financial Profiles in Mombasa",
                    "content": {
                        "text": "To understand bank accounts, examine three customers at a bank in Mombasa:\n\n1. **Amina (16-Year-Old Student):** Saves KES 500 monthly from her allowance to buy a laptop next year $\\rightarrow$ Needs a **Junior / Student Savings Account** offering safe custody, no ledger fees, and modest interest.\n2. **James (Salaried Accountant):** Receives salary, pays rent, buys utility tokens, and pays school fees using cheques $\\rightarrow$ Needs a **Current (Checking) Account** offering unlimited transactions, cheque books, and overdraft facilities.\n3. **Wanjiku (Hardware Merchant):** Has surplus seasonal profits of KES 200,000 that she will not touch for 6 months $\\rightarrow$ Needs a **Fixed Deposit Account** to lock funds and earn maximum interest."
                    }
                }
            ],
            # Card 3: Deep Dive & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Taxonomy of Commercial Bank Accounts",
                    "content": {
                        "title": "Bank Account Taxonomy & Feature Comparison",
                        "caption": "High-precision vector diagram illustrating the 4 core banking accounts: Savings (wealth accumulation), Current (daily liquidity & cheques), Fixed Deposit (locked maximum yield), and Junior (student literacy & joint parental mandate).",
                        "svg_content": SVG_BANK_ACCOUNT_TYPES
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Liquidity vs. Return Trade-Off in Banking",
                    "content": {
                        "text": "Bank accounts follow the fundamental financial principle of the **Liquidity vs. Return Trade-Off**:\n\n- **Highest Liquidity (Current Account):** You can withdraw 100% of your funds anytime via ATM, cheques, or mobile apps without notice. Because the bank cannot safely lend these volatile funds long-term, it pays **0% interest** and charges maintenance ledger fees.\n- **Lowest Liquidity (Fixed Deposit):** You legally commit funds for a fixed maturity (3, 6, 12 months). The bank gains guaranteed liquidity to fund long-term commercial projects and rewards you with the **highest interest rates (8% to 12%)**."
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Side-by-Side Comparison Matrix of Bank Accounts",
                    "content": {
                        "headers": ["Account Feature", "Savings Account", "Current (Checking) Account", "Fixed Deposit Account", "Junior Savings Account"],
                        "rows": [
                            ["Primary Purpose", "Personal wealth accumulation", "Daily business trade & payments", "Maximizing return on idle capital", "Financial literacy for minors"],
                            ["Interest Rate", "Low to Moderate (3% – 5% p.a.)", "Nil / Zero (0%)", "Highest (8% – 12% p.a.)", "Competitive (4% – 7% p.a.)"],
                            ["Withdrawal Ease", "Moderate (limits on frequency)", "Unlimited / Instant access", "Strictly locked for tenor", "Parental supervision required"],
                            ["Cheque Book?", "No", "Yes (Official cheque book)", "No", "No"],
                            ["Overdraft Facility?", "No", "Yes (Temporary short-term credit)", "No", "No"],
                            ["Ledger / Maintenance Fees", "Nil or very low", "Monthly ledger & transaction fees", "No fees (penalty on early exit)", "Zero monthly ledger fees"],
                            ["Target Customer", "Households & individual savers", "Enterprises, traders & professionals", "Investors with surplus cash", "School students under 18 years"]
                        ]
                    }
                },
                {
                    "type": "step_process",
                    "title": "Dormant Account Protocol & Reactivation Procedure",
                    "content": {
                        "intro": "When an account experiences zero customer-initiated transactions for 6 to 12 months, banks enforce the following protocol:",
                        "steps": [
                            {"title": "1. Automatic Classification", "description": "The core banking system automatically flags and freezes the account to prevent unauthorized fraud or internal embezzlement."},
                            {"title": "2. Notification & Freezing", "description": "Outgoing debits (withdrawals, card charges, mobile transfers) are blocked, though incoming deposits may still be accepted."},
                            {"title": "3. In-Person Identity Verification", "description": "The customer must physically visit a bank branch with their original National ID/Passport and proof of residence."},
                            {"title": "4. Form Execution & Activation Deposit", "description": "The customer signs a formal Account Reactivation Mandate and deposits fresh cash to restore active status."}
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Fixed Deposit vs. Savings Account Yield & Overdraft Cost",
                    "content": {
                        "intro": "Wanjiku has KES 200,000 surplus profits from her Mombasa hardware store and compares two 1-year investment options: Option A (Savings Account at 3.5% simple annual interest) vs Option B (12-Month Fixed Deposit at 9.0% per annum compounded semi-annually). Meanwhile, her business associate James utilizes a KES 50,000 overdraft on his current account for 18 days at 16% annual interest plus a KES 500 ledger fee.",
                        "steps": [
                            "**Step 1 — Given Parameters:**\n- Principal Sum ($P$) = $\\text{KES } 200,000$, Time ($t$) = $1\\text{ year}$\n- Option A (Savings): Simple interest rate ($r_s$) = $3.5\\% = 0.035$\n- Option B (Fixed Deposit): Annual interest rate ($r_f$) = $9.0\\% = 0.09$, Compounding frequency ($n$) = $2\\text{ (semi-annually)}$\n- Overdraft: Principal ($P_{\\text{od}}$) = $\\text{KES } 50,000$, Rate ($r_{\\text{od}}$) = $16\\% = 0.16$, Days ($d$) = $18\\text{ days}$, Ledger Fee = $\\text{KES } 500$.",
                            "**Step 2 — Mathematical Formulas:**\n$$\\text{Option A Simple Interest } (I_{\\text{savings}}) = P \\times r_s \\times t$$\n$$\\text{Option B Compound Amount } (A_{\\text{fixed}}) = P \\left(1 + \\frac{r_f}{n}\\right)^{n \\times t}, \\quad I_{\\text{fixed}} = A_{\\text{fixed}} - P$$\n$$\\text{Overdraft Interest } (I_{\\text{od}}) = P_{\\text{od}} \\times r_{\\text{od}} \\times \\frac{d}{365}, \\quad \\text{Total Overdraft Cost} = I_{\\text{od}} + \\text{Fee}$$",
                            "**Step 3 — Substitution:**\n$$I_{\\text{savings}} = 200,000 \\times 0.035 \\times 1$$\n$$A_{\\text{fixed}} = 200,000 \\left(1 + \\frac{0.09}{2}\\right)^{2 \\times 1} = 200,000 (1 + 0.045)^2 = 200,000 (1.045)^2$$\n$$I_{\\text{od}} = 50,000 \\times 0.16 \\times \\frac{18}{365}$$",
                            "**Step 4 — Step-by-Step Calculation:**\n$$I_{\\text{savings}} = \\text{KES } 7,000$$\n$$A_{\\text{fixed}} = 200,000 \\times 1.092025 = \\text{KES } 218,405 \\implies I_{\\text{fixed}} = 218,405 - 200,000 = \\text{KES } 18,405$$\n$$\\text{Fixed Deposit Gain Differential} = 18,405 - 7,000 = \\text{KES } 11,405$$\n$$I_{\\text{od}} = 8,000 \\times \\frac{18}{365} = \\text{KES } 394.52 \\implies \\text{Total Overdraft Cost} = 394.52 + 500 = \\text{KES } 894.52$$",
                            "**Step 5 — Final Stated Answer:**\n- Option A (Savings Account 1-Year Earnings): **KES 7,000** (Total Balance: KES 207,000)\n- Option B (Fixed Deposit 1-Year Earnings): **KES 18,405** (Total Balance: KES 218,405)\n- Fixed Deposit Yield Advantage: **+KES 11,405** (+162.9% extra return)\n- Total Financing Cost for James's 18-Day Overdraft: **KES 894.52**.",
                            "**Step 6 — Economic Interpretation & Common Pitfall:**\n- *Economic Interpretation:* Wanjiku earns KES 11,405 more by committing her cash into a fixed deposit because she surrenders immediate liquidity. Overdrafts provide James essential short-term liquidity to clear urgent bills, but must be repaid promptly to prevent compounding interest charges.\n- *Common Pitfall:* Remember that breaking a fixed deposit contract before the 12-month maturity results in severe interest forfeiture penalties."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Port Logistics Financing in Mombasa",
                    "content": {
                        "title": "Strategic Account Management in Freight Forwarding",
                        "text": "Mombasa Port handles millions of tons of cargo destined for Kenya, Uganda, and Rwanda. Freight forwarding enterprises (like Bahari Logistics Ltd) manage intense daily cash cycles.\n\nBahari Logistics maintains a **Current Account** with an active KES 1,000,000 overdraft facility and customized cheque books. When a client's shipping container arrives at the port, Bahari uses its overdraft facility to immediately clear Kenya Ports Authority (KPA) wharfage and Kenya Revenue Authority (KRA) customs duties before the client pays. Meanwhile, the company locks its surplus year-end retained profits in a 6-month **Fixed Deposit Account**, earning 9.5% annual interest while awaiting new truck purchases."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Commercial Bank Accounts Explained",
                    "content": {
                        "title": "Types of Bank Accounts: Savings, Current, Fixed Deposit & Cheque Facilities",
                        "youtube_id": "e7zV2s4P0Xk",
                        "url": "https://www.youtube.com/watch?v=e7zV2s4P0Xk",
                        "description": "Educational guide exploring retail bank account categories, transaction liquidity, interest accrual methods, and business overdraft features."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Account Features for Trading Enterprises",
                    "content": {
                        "question": "Which type of bank account is specifically tailored for high-volume commercial traders requiring cheque books and bank overdraft facilities?",
                        "options": [
                            "Fixed Deposit Account",
                            "Current (Checking) Account",
                            "Junior Savings Account",
                            "Pure Savings Account"
                        ],
                        "correct": "B",
                        "explanation": "Current accounts are designed for business operations, providing unlimited daily withdrawals, official cheque books for traceable payments, and temporary credit via overdraft facilities."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Managing Dormant Accounts",
                    "content": {
                        "question": "A customer discovers their bank account has been marked as 'dormant' after 9 months of inactivity. Why did the bank take this action, and what must the customer do to reactivate it?",
                        "options": [
                            "The bank confiscated the balance as tax; the customer must open a completely new account in a different bank",
                            "The bank froze the account to protect the funds from unauthorized fraud; the customer must visit the branch with original ID to verify identity and make a deposit",
                            "The bank permanently closed the account due to lack of interest; the customer must file a court petition",
                            "The bank converted the account into a fixed deposit; the customer cannot access funds for 5 years"
                        ],
                        "correct": "B",
                        "explanation": "Banks automatically freeze dormant accounts after 6-12 months of inactivity to protect customer balances from internal fraud. Reactivation requires presenting official ID and executing an activation transaction at the bank branch."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Account Hierarchy**: Savings (personal wealth building), Current (transaction liquidity & credit), Fixed Deposit (locked high interest), Junior (supervised youth literacy).\n2. **Current Account Exclusives**: Only current accounts offer cheque books and bank overdraft facilities.\n3. **Liquidity-Yield Trade-Off**: Accounts with the highest liquidity (Current) pay zero interest, while accounts with the lowest liquidity (Fixed Deposit) pay maximum returns.\n4. **Dormant Protection**: Inactive accounts are frozen after 6-12 months to protect funds from fraudulent misappropriation."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Ethical Practices in Banking
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Ethical Practices in Banking",
        "unit_description": "Fiduciary responsibilities, customer confidentiality, transparency in lending, anti-discrimination, responsible lending, fair debt recovery, and AML compliance.",
        "lesson_title": "Ethical Practices in Banking",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Central Bank of Kenya Headquarters, Nairobi",
                    "content": {
                        "title": "Regulatory Oversight and Banking Ethics",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/1/14/Central_Bank_of_Kenya.jpg",
                        "caption": "The Central Bank of Kenya (CBK) building in Nairobi, the primary regulator enforcing strict prudential guidelines, confidentiality standards, and ethical codes of conduct across the financial sector.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the 6 fundamental ethical pillars governing commercial banking institutions\n- Analyze ethical dilemmas involving customer confidentiality and unauthorized data disclosure\n- Calculate Total Cost of Credit (TCC) and Effective Annual Percentage Rates (APR) to detect predatory lending\n- Describe legal compliance requirements including Anti-Money Laundering (AML) and Know Your Customer (KYC)"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Ethics in Financial Services",
                    "content": {
                        "term": "Banking Ethics & Fiduciary Duty",
                        "definition": "Banking ethics comprises the moral principles, professional standards, and legal duties that govern financial institutions. It requires bankers to act with utmost integrity, maintain strict customer confidentiality, practice full transparency, and uphold fiduciary trust."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Tempted Teller Mwangi in Eldoret",
                    "content": {
                        "text": "Imagine Mwangi, a young bank teller in Eldoret. A wealthy property developer whispers across the counter: *'Mwangi, my main competitor banks here. If you tell me his exact account balance right now, I will hand you KES 10,000 in cash!'*\n\nIf Mwangi takes the bribe, he commits a criminal offense, breaches bank confidentiality, and violates the Data Protection Act 2019. **Public trust is the foundation of banking.** If depositors believe their financial records are leaked or traded, they will withdraw their deposits, precipitating a systemic bank run."
                    }
                }
            ],
            # Card 3: Deep Dive & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 6 Core Ethical Pillars of Commercial Banking",
                    "content": {
                        "title": "CBK Prudential Ethical Framework",
                        "caption": "Architectural vector diagram detailing the 6 core ethical pillars: Confidentiality, Transparency, Fairness, Responsible Lending, Fair Debt Recovery, and AML/KYC Compliance supported by statutory financial regulations.",
                        "svg_content": SVG_BANKING_ETHICS_PILLARS
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Why Ethical Banking Protects Macroeconomic Stability",
                    "content": {
                        "text": "Ethical banking is not merely a philosophical preference—it is a legal and economic necessity:\n\n- **Confidentiality:** Protects business competitive advantages and individual safety from extortion.\n- **Transparency (Truth in Lending):** Empowers borrowers to make informed financial decisions without falling into hidden debt traps.\n- **Responsible Lending:** Prevents over-indebtedness and excessive non-performing loans (NPLs) that could trigger bank insolvency."
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Ethical Banking vs. Predatory & Unethical Practices",
                    "content": {
                        "headers": ["Ethical Dimension", "Standard Ethical Practice", "Predatory / Unethical Practice", "Regulatory & Economic Impact"],
                        "rows": [
                            ["1. Confidentiality", "Safeguards client records; restricts access via secure authentication", "Selling customer phone numbers or sharing balances with third parties", "Violation of Data Protection Act 2019; heavy fines and jail terms"],
                            ["2. Fee Transparency", "Full disclosure of interest rates, ledger charges, and legal fees upfront", "Hiding application fees, balloon payments, and exorbitant penalty clauses", "Consumer exploitation; CBK sanctions and license revocation"],
                            ["3. Fairness & Equity", "Uniform service delivery without tribal, gender, or religious bias", "Discriminatory loan approvals or redlining low-income neighborhoods", "Violates Constitution of Kenya; creates financial exclusion"],
                            ["4. Responsible Lending", "Rigorous repayment capacity appraisal to avoid over-indebtedness", "Pushing high-interest loans to desperate borrowers lacking repayment means", "Surge in default rates and collapse of enterprise working capital"],
                            ["5. Debt Recovery", "Dignified restructuring, counseling, and reasonable grace periods", "Harassment, public shaming, or illegal seizure of household assets", "Illegal under Consumer Protection Act; reputational destruction"],
                            ["6. AML / KYC Rules", "Mandatory customer identity verification and reporting suspicious cash", "Facilitating anonymous accounts or laundering illicit corrupt funds", "Inclusion on global FATF grey-lists; loss of international clearing"]
                        ]
                    }
                },
                {
                    "type": "step_process",
                    "title": "4-Stage Ethical Dilemma Resolution Framework",
                    "content": {
                        "intro": "When financial officers face ethical conflicts, they must apply this decision-making protocol:",
                        "steps": [
                            {"title": "1. Identify the Legal & Fiduciary Mandate", "description": "Review the Central Bank of Kenya Prudential Guidelines, Banking Act, and internal code of ethics."},
                            {"title": "2. Assess Customer Rights & Data Security", "description": "Ensure no customer data, PIN, or confidential financial record is compromised or released without valid court subpoenas."},
                            {"title": "3. Reject Corrupt Inducements", "description": "Immediately decline any bribes, kickbacks, or gifts offered in exchange for confidential information or loan favoritism."},
                            {"title": "4. Escalate to Compliance & Whistleblow", "description": "Formally document and report the incident to the bank's Chief Compliance Officer and internal audit committee."}
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Ethical Lending & Annual Percentage Rate (APR) vs. Hidden Fees",
                    "content": {
                        "intro": "Mwangi needs a KES 100,000 working capital loan for 1 year for his Eldoret agribusiness. He evaluates two offers: Bank Alpha (Transparent & Ethical) offering 14% flat annual interest with zero hidden processing fees and KES 1,000 credit insurance; versus Micro-Lender Beta (Predatory) advertising 'Only 1% per month (12% per year) interest!' but charging an upfront 5% processing fee, a 3% loan appraisal fee, and a monthly ledger fee of KES 300.",
                        "steps": [
                            "**Step 1 — Given Parameters:**\n- Loan Principal ($P$) = $\\text{KES } 100,000$, Loan Term = $1\\text{ year (12 months)}$\n- Bank Alpha: Nominal Interest = $14\\% \\times 100,000 = \\text{KES } 14,000$, Insurance = $\\text{KES } 1,000$, Other Fees = $\\text{KES } 0$\n- Lender Beta: Advertised Interest = $12\\% \\times 100,000 = \\text{KES } 12,000$, Upfront Processing Fee ($5\\%$) = $\\text{KES } 5,000$, Appraisal Fee ($3\\%$) = $\\text{KES } 3,000$, Monthly Ledger Fees ($12 \\times 300$) = $\\text{KES } 3,600$.",
                            "**Step 2 — Mathematical Formulas:**\n$$\\text{Total Cost of Credit } (\\text{TCC}) = \\text{Interest Amount} + \\sum \\text{Mandatory Fees & Charges}$$\n$$\\text{Effective Annual Percentage Rate } (\\text{APR}) = \\frac{\\text{Total Financing Cost}}{\\text{Principal}} \\times 100\\%$$",
                            "**Step 3 — Substitution:**\n$$\\text{Bank Alpha TCC} = 14,000 + 1,000 = \\text{KES } 15,000$$\n$$\\text{Lender Beta TCC} = 12,000 + 5,000 + 3,000 + 3,600 = \\text{KES } 23,600$$",
                            "**Step 4 — Step-by-Step Calculation:**\n$$\\text{Bank Alpha Effective APR} = \\frac{15,000}{100,000} \\times 100\\% = 15.0\\%$$\n$$\\text{Lender Beta Effective APR} = \\frac{23,600}{100,000} \\times 100\\% = 23.6\\%$$\n$$\\text{Predatory Excess Cost} = 23,600 - 15,000 = \\text{KES } 8,600$$",
                            "**Step 5 — Final Stated Answer:**\n- Bank Alpha Total Financing Cost: **KES 15,000** (Effective APR: **15.0%**)\n- Lender Beta Total Financing Cost: **KES 23,600** (Effective APR: **23.6%**)\n- Bank Alpha saves Mwangi **KES 8,600** despite having a higher nominal headline interest rate (14% vs 12%).",
                            "**Step 6 — Economic Interpretation & Common Pitfall:**\n- *Economic Interpretation:* Ethical banking mandates full Truth in Lending disclosure. Predatory lenders deceive consumers with low headline interest rates while extracting massive upfront and recurring fees that raise the true borrowing cost by +57.3%.\n- *Common Pitfall:* Never compare loans using only the advertised nominal interest rate. Always compute the comprehensive Total Cost of Credit (TCC) including all processing, appraisal, and monthly maintenance fees."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Ethical Data Protection in Eldoret Agribusiness",
                    "content": {
                        "title": "Safeguarding Farm Enterprises from Corporate Espionage",
                        "text": "In Uasin Gishu County, large-scale commercial seed maize producers negotiate annual grain supply contracts with the National Cereals and Produce Board (NCPB) and private millers. Contract pricing depends on grain inventory levels and available bank credit lines.\n\nWhen competing grain brokers attempted to bribe branch bank tellers in Eldoret to obtain confidential cash flow statements of local farmers, bank management enforced strict digital access logging. Under CBK regulations, tellers require multi-factor supervisor approvals to access client records, and all inquiries are audited. By maintaining customer confidentiality, the bank protected farmers' bargaining power and preserved fair market pricing."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Banking Ethics and Consumer Financial Protection",
                    "content": {
                        "title": "Ethics in Banking: Client Confidentiality, Truth in Lending & AML Laws",
                        "youtube_id": "0h6bXgW8VqM",
                        "url": "https://www.youtube.com/watch?v=0h6bXgW8VqM",
                        "description": "Professional training video covering fiduciary responsibility, predatory lending avoidance, customer data privacy, and global anti-money laundering compliance."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Telephone Data Disclosure Dilemma",
                    "content": {
                        "question": "An intern at a bank receives an urgent phone call from an individual claiming to be the son of a hospitalized customer, begging for the customer's account balance to settle emergency surgery bills. What is the correct ethical and professional response?",
                        "options": [
                            "Read out the balance immediately since medical emergencies supersede bank policies",
                            "Politely decline to disclose account details over the phone, explain confidentiality laws, and direct the caller to provide written power of attorney at the branch",
                            "Charge an emergency inquiry fee of KES 500 and send the balance via SMS",
                            "Post the query on the bank's social media page to verify family relations"
                        ],
                        "correct": "B",
                        "explanation": "Customer financial records are strictly protected under confidentiality guidelines and the Data Protection Act 2019. Disclosing details over the phone creates severe fraud risks (social engineering/phishing). The customer or authorized representative must present verified legal documentation in person."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Truth in Lending & Effective APR",
                    "content": {
                        "question": "Why does the Central Bank of Kenya require all commercial banks and micro-financiers to publish the Total Cost of Credit (TCC) alongside interest rates?",
                        "options": [
                            "To encourage commercial banks to charge higher appraisal fees",
                            "To prevent deceptive advertising where low headline rates conceal expensive hidden fees and charges",
                            "To eliminate the need for borrowers to sign loan contracts",
                            "To force all borrowers to repay loans in cash rather than mobile money"
                        ],
                        "correct": "B",
                        "explanation": "Publishing the Total Cost of Credit ensures transparency and truth in lending, preventing predatory lenders from advertising misleadingly low interest rates while disguising heavy upfront processing, insurance, and ledger charges."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **The Currency of Trust**: Banking institutions survive on public confidence; breaching client confidentiality destroys systemic trust and violates Kenyan law.\n2. **6 Ethical Pillars**: Confidentiality, Transparency, Fairness, Responsible Lending, Fair Debt Recovery, and AML Compliance.\n3. **Truth in Lending**: Always evaluate loans based on the Total Cost of Credit (TCC) and Effective APR rather than misleading headline interest rates.\n4. **AML & KYC**: Strict identification and transaction monitoring prevent financial institutions from being exploited for money laundering and fraud."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Trends in Banking in Kenya
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Trends in Banking in Kenya",
        "unit_description": "Analyzing digital transformation: mobile banking, agency banking networks, real-time interbank settlement (PesaLink), cybersecurity protocols, AI credit scoring, and green banking.",
        "lesson_title": "Trends in Banking in Kenya",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Mobile Money & Agency Banking Hub in Kenya",
                    "content": {
                        "title": "Agency and Mobile Banking Revolution",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/M-PESA_mobile_money_and_Equity_agent%2C_Nairobi%2C_Kenya.jpg",
                        "caption": "An authorized retail banking and mobile money agency in Kenya providing seamless cash deposits, withdrawals, and digital merchant payments directly within local neighborhood commercial centers.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the key modern trends transforming Kenya's banking sector\n- Explain how agency banking networks eliminate rural transport and opportunity costs\n- Calculate enterprise cost and time savings generated by digital and agency banking\n- Evaluate modern cybersecurity defenses including multi-factor authentication (MFA) and fraud prevention"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Modern Banking Trends & FinTech",
                    "content": {
                        "term": "Agency Banking & FinTech Transformation",
                        "definition": "Agency banking is a retail model where commercial banks contract third-party retail businesses (such as supermarkets, kiosks, and pharmacies) to deliver basic banking services on their behalf using Point-of-Sale (POS) terminals and mobile networks. FinTech integration encompasses digital wallets, USSD banking, and real-time interbank transfers."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Digital Revolution: Mary's Wholesale Shop in Rural Kitui",
                    "content": {
                        "text": "Meet Mary, who operates a rural wholesale shop in Kitui. Five years ago, to buy stock from her Nairobi suppliers, Mary had to:\n\n- Travel 15 km to Kitui town to withdraw physical cash from a crowded branch.\n- Board an overnight bus carrying envelopes of cash, risking highway robbery.\n\n**Today:** Mary stands inside her shop, dials a USSD shortcode (*667# or *247#), or walks 2 minutes to a neighboring *Equity Agent* or *Co-op Jirani*. She instantly transfers KES 50,000 to her supplier's account in Nairobi via PesaLink. Transactions that once took 12 hours now take under 30 seconds!"
                    }
                }
            ],
            # Card 3: Deep Dive & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Modern Kenyan Banking & FinTech Ecosystem",
                    "content": {
                        "title": "The 5 Pillars of Kenyan Digital Banking",
                        "caption": "Comprehensive vector diagram detailing Mobile Banking Dominance, Agency Banking Networks, Cybersecurity Defenses, Interoperable Real-Time Settlement (PesaLink), and Sustainable Green AI Banking.",
                        "svg_content": SVG_KENYA_BANKING_TRENDS
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Why Kenya Leads the Global FinTech Revolution",
                    "content": {
                        "text": "Kenya's banking sector is recognized globally for financial innovation through 5 key drivers:\n\n1. **Mobile-First Infrastructure:** Seamless two-way integration between bank accounts and mobile wallets (M-Pesa, Airtel Money).\n2. **De-branching via Agency Banking:** Over 100,000 authorized retail agents eliminating the capital expense of brick-and-mortar branches.\n3. **Real-Time Settlement (PesaLink & KE-QR):** Instant 24/7 account-to-account money transfers across competing banks.\n4. **Algorithmic Micro-Lending:** Instant automated credit scoring based on mobile transaction histories (e.g., M-Shwari, Fuliza, KCB M-Pesa).\n5. **Green & Sustainable Banking:** Paperless electronic statements and green credit lines for clean solar and geothermal energy."
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Traditional Branch Banking vs. Modern Digital & Agency Banking",
                    "content": {
                        "headers": ["Operational Factor", "Traditional Branch Banking", "Modern Digital & Agency Banking", "Enterprise Economic Impact"],
                        "rows": [
                            ["Accessibility & Hours", "Restricted (Mon-Fri 8:30 AM - 4:00 PM)", "24/7/365 via mobile apps, USSD & local agents", "Zero business disruption; continuous cash flow"],
                            ["Geographic Proximity", "Located in major urban centers and county towns", "Available in village trading centers and kiosks", "Eliminates long-distance rural travel"],
                            ["Transaction Speed", "Long physical queues (30 to 90 minutes)", "Instant execution (under 60 seconds)", "Maximizes entrepreneur productive labor time"],
                            ["Cash Handling Risk", "High risk of carrying large cash on public transport", "Digital electronic transfers / cashless QR payments", "Prevents highway robbery and theft"],
                            ["Direct Transaction Cost", "Zero branch fee but high travel expenses", "Small operator agent fee (KES 30 - KES 100)", "Massive net cost savings for rural MSMEs"],
                            ["Account Management", "Paper-based deposit slips and physical passbooks", "Instant SMS alerts, e-statements & mobile dashboards", "Real-time automated financial bookkeeping"]
                        ]
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 4-Layer Cybersecurity Defense Architecture",
                    "content": {
                        "intro": "As banking goes digital, commercial banks enforce this 4-layer defense against cybercrime:",
                        "steps": [
                            {"title": "1. Secret Customer PIN & Passwords", "description": "Confidential numerical codes known only to the user; never stored in plaintext or disclosed to staff."},
                            {"title": "2. Dynamic Multi-Factor Authentication (OTP)", "description": "Single-use 6-digit One-Time PINs sent to verified mobile numbers to authenticate high-value digital transactions."},
                            {"title": "3. Biometric Verification", "description": "Fingerprint and facial recognition validation on agency POS terminals and smartphone banking apps."},
                            {"title": "4. Automated AI Fraud Anomaly Monitoring", "description": "Algorithmic systems that instantly detect and freeze suspicious SIM-swap activities or unusual midnight withdrawals."}
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Cost & Time Efficiency: Agency Banking vs. Traditional Branch Visits",
                    "content": {
                        "intro": "Mary operates a wholesale shop in rural Kitui and conducts 4 banking transactions per month (depositing sales receipts and paying suppliers). She compares two operational models: Model 1 (Traditional Bank Branch in Town) vs Model 2 (Local Agency Banking in Neighborhood).",
                        "steps": [
                            "**Step 1 — Given Parameters:**\n- Monthly Transactions ($N$) = $4$\n- Model 1 (Town Branch): Matatu round-trip transport per visit = $\\text{KES } 400$, Travel & queue time = $3\\text{ hours}$ (valued at $\\text{KES } 250/\\text{hour}$ in lost shop sales), Bank direct fee = $\\text{KES } 0$.\n- Model 2 (Local Agency): Walking distance transport = $\\text{KES } 0$, Total time spent = $10\\text{ minutes}$ (valued at $\\text{KES } 40$ opportunity cost), Agent service fee = $\\text{KES } 65\\text{ per transaction}$.",
                            "**Step 2 — Mathematical Formulas:**\n$$\\text{Cost per Branch Visit } (C_{\\text{branch}}) = \\text{Transport Fare} + \\text{Opportunity Cost of Time} + \\text{Bank Fee}$$\n$$\\text{Cost per Agent Transaction } (C_{\\text{agent}}) = \\text{Transport Fare} + \\text{Opportunity Cost of Time} + \\text{Agent Fee}$$\n$$\\text{Total Monthly Cost} = N \\times C_{\\text{transaction}}$$\n$$\\text{Monthly Cost Savings} = \\text{Total Monthly } C_{\\text{branch}} - \\text{Total Monthly } C_{\\text{agent}}$$",
                            "**Step 3 — Substitution:**\n$$C_{\\text{branch}} = 400 + (3 \\times 250) + 0 = 400 + 750 + 0 = \\text{KES } 1,150\\text{ per trip}$$\n$$C_{\\text{agent}} = 0 + 40 + 65 = \\text{KES } 105\\text{ per transaction}$$\n$$\\text{Total Monthly Branch Cost} = 4 \\times 1,150$$\n$$\\text{Total Monthly Agent Cost} = 4 \\times 105$$",
                            "**Step 4 — Step-by-Step Calculation:**\n$$\\text{Total Monthly Branch Cost} = \\text{KES } 4,600$$\n$$\\text{Total Monthly Agent Cost} = \\text{KES } 420$$\n$$\\text{Net Monthly Savings} = 4,600 - 420 = \\text{KES } 4,180$$\n$$\\text{Annual Enterprise Savings} = 4,180 \\times 12 = \\text{KES } 50,160$$",
                            "**Step 5 — Final Stated Answer:**\n- Monthly Cost under Traditional Branch Banking: **KES 4,600**\n- Monthly Cost under Local Agency Banking: **KES 420**\n- Net Monthly Cost Savings for Mary: **KES 4,180** (**90.9%** operational cost reduction)\n- Annual Capital Saved: **KES 50,160**.",
                            "**Step 6 — Economic Interpretation & Common Pitfall:**\n- *Economic Interpretation:* Agency banking eliminates severe deadweight economic losses for rural micro-enterprises. The KES 50,160 saved annually can be reinvested into expanding Mary's inventory.\n- *Common Pitfall:* Do not focus solely on the direct agency fee (KES 65). Always account for the massive indirect costs of transport fares and lost trading hours caused by travel."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Equity Agent & Co-op Jirani in Rural Retail",
                    "content": {
                        "title": "Democratizing Banking Access in Kitui County",
                        "text": "In Kitui County, over 70% of households reside more than 20 kilometers from the nearest major urban bank branch. The introduction of agency banking programs—such as *Equity Bank Agents*, *Co-op Jirani*, and *KCB Mtaani*—empowered licensed local shopkeepers, chemists, and agrovets to serve as certified banking terminals.\n\nEquipped with secure biometric POS terminals, these agents process over 80,000 cash deposits and withdrawals daily across the county. Local farmers deposit their crop earnings immediately after market day, eliminating cash hoarding at home. The agency model has boosted financial inclusion in rural Kenya from under 30% in 2006 to over 84% today."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Mobile Money and Agency Banking in Kenya",
                    "content": {
                        "title": "The FinTech Revolution: How Mobile & Agency Banking Changed Kenya",
                        "youtube_id": "kwbE2qF48-c",
                        "url": "https://www.youtube.com/watch?v=kwbE2qF48-c",
                        "description": "Documentary exploring the rise of M-Pesa, agency banking networks, real-time interoperability, and digital inclusion across Kenya."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Economic Benefits of Agency Banking",
                    "content": {
                        "question": "How does the expansion of Agency Banking directly benefit smallholder agricultural farmers and rural enterprise owners in Kenya?",
                        "options": [
                            "By forcing all rural citizens to buy costly desktop computers",
                            "By bringing secure cash deposit and withdrawal services into local neighborhood shops, saving transport fares and productive working hours",
                            "By allowing local retail kiosks to issue their own private currency notes",
                            "By eliminating all national taxes on agricultural goods"
                        ],
                        "correct": "B",
                        "explanation": "Agency banking expands commercial banking into rural villages via licensed retail agents, eliminating the high transport costs, danger of carrying cash, and lost working hours associated with traveling to distant town branches."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Protecting Against Mobile Banking Fraud",
                    "content": {
                        "question": "A customer receives an SMS claiming to be from their bank's 'IT Security Department' asking them to dial a USSD string to prevent their account from being suspended. What is the safest course of action?",
                        "options": [
                            "Dial the USSD code immediately to avoid account suspension",
                            "Ignore the message, do not dial any codes or share PINs, and contact the official customer care number to report a phishing attempt",
                            "Forward the SMS to family members so they can test if the code works",
                            "Reply to the SMS with their secret ATM PIN to verify account ownership"
                        ],
                        "correct": "B",
                        "explanation": "This is a classic phishing and SIM-swap scam. Commercial banks will never request customers to dial secret USSD codes or provide PINs over SMS or phone calls. The only secure response is to refrain from dialing and report through verified bank customer care channels."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Global FinTech Leadership**: Kenya is a world leader in digital finance through mobile wallets, agency networks, and real-time interbank settlement.\n2. **Agency Banking Efficiency**: Local agents eliminate rural travel friction, cutting transaction time from hours to seconds and saving MSMEs significant operating capital.\n3. **Interoperability (PesaLink)**: Instant 24/7 account-to-account funds transfers across competing commercial banks.\n4. **Cybersecurity Discipline**: Protecting against fraud requires strict PIN secrecy, multi-factor OTP verification, and vigilance against phishing scams."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Opening and Using a Junior Savings Account
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Opening and Using a Junior Savings Account",
        "unit_description": "Legal capacity of minors, joint mandate requirements, KYC documentation, application form procedures, security guidelines, and compound savings growth.",
        "lesson_title": "Opening and Using a Junior Savings Account",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Secondary School Students Building Financial Literacy",
                    "content": {
                        "title": "Youth Financial Literacy and Junior Banking",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/06/Students_at_Shimo_la_Tewa_Secondary_School.jpg",
                        "caption": "Kenyan secondary school students developing personal financial discipline and learning how to open and manage junior savings accounts to achieve long-term educational goals.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the legal reason why minors require a parent or guardian to open a bank account\n- Identify the standard Know Your Customer (KYC) documents required to open a Junior Savings Account in Kenya\n- Accurately complete a bank account opening form avoiding common legal and security errors\n- Calculate 3-year compound interest growth on regular monthly student savings"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Junior Account & Legal Contractual Capacity",
                    "content": {
                        "term": "Junior Savings Account & Dual Mandate",
                        "definition": "A Junior Savings Account is a dedicated bank account designed for children and teenagers under 18 years of age. Because minors lack full legal capacity to enter binding financial contracts under Kenyan law, the account is operated under a joint mandate co-signed and supervised by a parent or legal guardian."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Halima's 15th Birthday Milestone in Garissa",
                    "content": {
                        "text": "For her 15th birthday in Garissa, Halima receives KES 2,000 in cash gifts from her family. Her father says: *'Halima, keeping this cash in a wooden box at home risks theft or impulse spending on sweets. Let's go to the bank and open your very first Junior Savings Account!'*\n\nHalima learns that opening an account introduces her to the formal financial sector. Her savings will earn monthly interest, remain protected in the bank's vault, and help her accumulate funds for her high school graduation and university education."
                    }
                }
            ],
            # Card 3: Deep Dive & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Junior Bank Account Opening & Security Lifecycle",
                    "content": {
                        "title": "Step-by-Step Junior Account Lifecycle",
                        "caption": "Comprehensive vector diagram illustrating the 4 lifecycle stages: Gathering KYC Documents, Form Execution & Joint Mandate, Activation Deposit, and Lifetime Security Prudence.",
                        "svg_content": SVG_JUNIOR_ACCOUNT_PROCESS
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 4 Pillars of Junior Account Management",
                    "content": {
                        "text": "Managing a junior account involves four key steps:\n\n1. **KYC Verification:** Establishing legal identity and residential proof to comply with CBK anti-fraud standards.\n2. **The Dual Mandate:** Clarifying signing authorities—parent as primary guarantor, child as minor beneficiary and co-signatory.\n3. **The Savings Habit:** Depositing pocket money regularly to benefit from monthly compounding interest.\n4. **Operational Prudence:** Protecting secret PINs, auditing SMS transaction receipts, and never trusting strangers near ATMs."
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Bank Account Opening Form Section Guide & Error Checklist",
                    "content": {
                        "headers": ["Form Section", "Required Information", "Common Mistakes to Avoid", "Security & Verification Standard"],
                        "rows": [
                            ["Section 1: Minor's Personal Details", "Full legal name as written on Birth Certificate, Date of Birth, School", "Using informal nicknames (e.g. 'Hali' instead of 'Halima Yusuf')", "Must exactly match Birth Certificate or Student ID"],
                            ["Section 2: Parent / Guardian Details", "Guardian legal name, National ID / Passport No, Phone Number, KRA PIN", "Writing someone else's ID or omitting the KRA PIN", "Must match physical National ID Card and KRA database"],
                            ["Section 3: Account Type & Currency", "Select 'Junior / Student Savings Account' (Currency: KES)", "Selecting 'Current Account' which incurs monthly ledger fees", "Ensures zero maintenance fees and interest entitlement"],
                            ["Section 4: Mandate & Specimen Signatures", "Parent signs as Primary Signatory; Minor signs in specimen box", "Parent signing on behalf of minor or sharing PIN with teller", "Scanned into bank database to authorize future withdrawals"],
                            ["Section 5: Initial Opening Deposit", "Cash deposit receipt (typically KES 500 to KES 1,000)", "Leaving opening balance at zero; account fails activation", "Official bank stamp and automated SMS confirmation receipt"]
                        ]
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 4 Golden Rules of Junior Account Security",
                    "content": {
                        "intro": "Every student account holder must adhere to these safety practices:",
                        "steps": [
                            {"title": "1. Absolute PIN Confidentiality", "description": "Never tell anyone your secret 4-digit PIN—not even bank tellers, friends, or teachers. Cover the keypad when entering PINs."},
                            {"title": "2. Instant SMS Alert Auditing", "description": "Check every automatic SMS notification received after deposits or withdrawals to immediately spot unauthorized transactions."},
                            {"title": "3. Safe Custody of Documents", "description": "Keep your passbook, account cards, and birth certificate safely stored at home; never leave them unattended in classrooms."},
                            {"title": "4. Disciplined Monthly Saving", "description": "Set a fixed monthly savings target from allowance or gifts to maximize the power of compound interest over time."}
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Junior Savings Growth & Monthly Compounding",
                    "content": {
                        "intro": "Halima opens a Junior Savings Account in Garissa on her 15th birthday with an initial opening deposit of KES 2,000. She commits to depositing KES 1,000 at the end of every month from her pocket money and chores. The junior account earns an annual interest rate of 6.0% compounded monthly ($r = 0.06, n = 12, i = \\frac{0.06}{12} = 0.005$ per month). Calculate her total accumulated funds after 3 years (36 months) when she turns 18 and graduates from high school.",
                        "steps": [
                            "**Step 1 — Given Parameters:**\n- Initial Opening Deposit ($P_0$) = $\\text{KES } 2,000$\n- Monthly Regular Deposit ($PMT$) = $\\text{KES } 1,000$\n- Annual Interest Rate ($r$) = $6.0\\% = 0.06$\n- Compounding Frequency ($n$) = $12\\text{ times/year}$\n- Monthly Interest Rate ($i = \\frac{r}{12}$) = $\\frac{0.06}{12} = 0.005\\text{ (0.5% per month)}$\n- Total Duration ($m = 3 \\times 12$) = $36\\text{ months}$.",
                            "**Step 2 — Mathematical Formulas:**\n$$\\text{Growth of Initial Deposit: } FV_{\\text{initial}} = P_0 \\times (1 + i)^m$$\n$$\\text{Future Value of Monthly Savings Annuity: } FV_{\\text{annuity}} = PMT \\times \\frac{(1 + i)^m - 1}{i}$$\n$$\\text{Total Accumulated Balance: } FV_{\\text{total}} = FV_{\\text{initial}} + FV_{\\text{annuity}}$$\n$$\\text{Total Personal Cash Deposited: } P_{\\text{total}} = P_0 + (PMT \\times 36)$$\n$$\\text{Total Compound Interest Earned: } I_{\\text{total}} = FV_{\\text{total}} - P_{\\text{total}}$$",
                            "**Step 3 — Substitution:**\n$$(1 + 0.005)^{36} = (1.005)^{36} \\approx 1.19668$$\n$$FV_{\\text{initial}} = 2,000 \\times 1.19668$$\n$$FV_{\\text{annuity}} = 1,000 \\times \\frac{1.19668 - 1}{0.005} = 1,000 \\times \\frac{0.19668}{0.005}$$",
                            "**Step 4 — Step-by-Step Calculation:**\n$$FV_{\\text{initial}} = \\text{KES } 2,393.36$$\n$$FV_{\\text{annuity}} = 1,000 \\times 39.336 = \\text{KES } 39,336.00$$\n$$FV_{\\text{total}} = 2,393.36 + 39,336.00 = \\text{KES } 41,729.36$$\n$$P_{\\text{total}} = 2,000 + (1,000 \\times 36) = 2,000 + 36,000 = \\text{KES } 38,000.00$$\n$$I_{\\text{total}} = 41,729.36 - 38,000.00 = \\text{KES } 3,729.36$$",
                            "**Step 5 — Final Stated Answer:**\n- Total Personal Cash Contributed by Halima: **KES 38,000.00**\n- Compound Interest Rewarded by the Bank: **KES 3,729.36**\n- Total Accumulated Bank Balance on 18th Birthday: **KES 41,729.36**.",
                            "**Step 6 — Economic Interpretation & Common Pitfall:**\n- *Economic Interpretation:* Compound interest acts as a financial multiplier. By consistently saving KES 1,000 monthly, Halima accumulates KES 41,729.36, earning KES 3,729.36 in 'free' interest growth to finance her tertiary education.\n- *Common Pitfall:* Missing monthly deposits breaks the compounding cycle and reduces the final accumulated balance significantly. Consistency is the secret to building capital."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Enterprise Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Student Savings Clubs in Garissa",
                    "content": {
                        "title": "Building Early Financial Independence in Secondary Schools",
                        "text": "In Garissa County, secondary school business clubs partnered with local commercial banks to introduce youth financial literacy programs. Over 400 students opened junior savings accounts (*KCB Cub Account* and *Co-op Jumbo Junior*).\n\nStudents deposited small earnings from school farm vegetable sales and holiday chores. By Form 4 graduation, the top student savers had accumulated between KES 30,000 and KES 50,000 each. This capital allowed them to pay university admission fees and purchase their first study laptops without placing financial strain on their parents."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Opening and Managing Your First Bank Account",
                    "content": {
                        "title": "How to Open and Manage a Bank Account for Beginners & Students",
                        "youtube_id": "F_f4yRzT9e0",
                        "url": "https://www.youtube.com/watch?v=F_f4yRzT9e0",
                        "description": "Step-by-step educational guide demonstrating how students can fill out bank account application forms, understand joint mandates, and manage savings securely."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Legal Capacity of Minors in Banking",
                    "content": {
                        "question": "Why does Kenyan banking law require a 15-year-old student to open a Junior Savings Account jointly with a parent or legal guardian?",
                        "options": [
                            "Because secondary school students are legally prohibited from holding cash",
                            "Because minors under 18 years lack full legal contractual capacity to enter independent commercial contracts, requiring a legal guardian to co-sign and supervise",
                            "Because commercial banks only issue bank accounts to individuals who own physical land",
                            "Because banks do not allow students to earn compound interest"
                        ],
                        "correct": "B",
                        "explanation": "Under the Law of Contract in Kenya, minors (under 18) lack full capacity to enter binding financial contracts independently. A parent or legal guardian must act as a joint signatory and legal guarantor."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Form Completion & Security Pitfalls",
                    "content": {
                        "question": "Which of the following represents an unsafe practice when filling out a bank account opening application form at a branch?",
                        "options": [
                            "Writing your full official legal name exactly as shown on your birth certificate",
                            "Providing your parent's genuine National ID card number",
                            "Saying your secret 4-digit mobile banking PIN out loud to a bank teller so they can write it down for you",
                            "Attaching two recent colored passport-sized photographs"
                        ],
                        "correct": "C",
                        "explanation": "A PIN is strictly confidential and must never be shared with anyone, including bank employees. Tellers will never ask for your PIN; you must enter it privately on a secure keypad or mobile screen."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Joint Guardian Mandate**: Minors under 18 open accounts jointly with a parent/guardian who co-signs as legal guarantor.\n2. **KYC Documentation**: Opening requires the minor's Birth Certificate, guardian's National ID, passport photos, proof of address, and opening deposit.\n3. **Form Accuracy**: Legal names must be written without nicknames to pass official banking audits and prevent identity fraud.\n4. **Security Discipline**: Secret PINs must never be disclosed to anyone; SMS alerts should be audited immediately.\n5. **Topic 4 Synthesis**: Commercial banks are the financial engines of the economy—mobilizing savings, providing credit, offering diverse accounts, upholding ethical fiduciary trust, and leveraging FinTech innovations to build national prosperity."
                    }
                }
            ]
        ]
    }
]
