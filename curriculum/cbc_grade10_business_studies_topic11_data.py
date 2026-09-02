"""
VLearn CBC Grade 10 Business Studies — Topic 11: Public Finance
Full Structured Lesson Card Definitions (Lessons 1 to 6)
"""

from curriculum.cbc_grade10_business_studies_topic11_svgs import (
    SVG_PUBLIC_FINANCE_ARCHITECTURE,
    SVG_CANONS_OF_TAXATION_FRAMEWORK,
    SVG_TAX_STRUCTURE_AND_PROGRESSION,
    SVG_CUSTOMS_DUTY_AND_PROTECTIONISM,
    SVG_TAX_ETHICS_AND_ACCOUNTABILITY,
    SVG_BUDGET_BALANCE_AND_DEFICIT_FINANCING
)

TOPIC_11_LESSONS = [
    # =========================================================================
    # LESSON 1: Introduction to Public Finance and Government Expenditure
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Introduction to Public Finance and Government Expenditure",
        "unit_description": "Foundational concepts of public finance, differences between public and private finance, national budget sequencing, and classification of recurrent versus development expenditures.",
        "lesson_title": "Introduction to Public Finance and Government Expenditure",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Thika Superhighway Infrastructure in Nairobi",
                    "content": {
                        "title": "Modern Public Infrastructure in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Thika_Road_super_highway.jpeg",
                        "caption": "Panoramic view of the multi-lane Thika Superhighway in Kenya, illustrating capital development expenditure funded through public finance to unlock economic productivity.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define public finance and government expenditure in macroeconomic management\n- Compare and contrast public finance with private (household/business) finance across 5 core dimensions\n- Explain the inverse budget sequence adopted by sovereign governments compared to private entities\n- Categorize government spending into recurrent expenditure and development expenditure with relevant Kenyan examples"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Public Finance & Expenditure Foundations",
                    "content": {
                        "term": "Public Finance",
                        "definition": "The branch of economics and statecraft that deals with how national and county governments identify societal needs, mobilize revenues (through taxes, fees, and debt), allocate public expenditures, and manage sovereign debt to achieve economic growth and social welfare."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Inverse Budget Sequence & Expenditure Taxonomy",
                    "content": {
                        "text": "Public finance operates through distinct structural mechanisms:\n\n- **The Inverse Budget Sequence:** Unlike a family or private firm that calculates income first and caps spending to match that income, the sovereign government first evaluates the total public expenditure required (security, health, CBC education, transport) and subsequently determines the taxation, fees, and borrowing required to fund those needs.\n- **Recurrent Expenditure:** Ongoing operational spending required for day-to-day government administration that does not generate permanent capital assets (e.g., paying teachers' and doctors' salaries, fueling police cruisers, purchasing hospital medicine).\n- **Development Expenditure:** Long-term capital investment spending dedicated to creating durable productive infrastructure and national assets (e.g., constructing the Standard Gauge Railway, building modern county markets, electrifying schools, constructing dams)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Public Finance System and Budget Flow Architecture",
                    "content": {
                        "title": "Macroeconomic Public Finance Architecture in Kenya",
                        "caption": "High-precision vector SVG diagram depicting the National Treasury's central role, revenue mobilization streams (taxes, non-tax fees, public debt), and expenditure allocation channels (recurrent vs development).",
                        "svg_content": SVG_PUBLIC_FINANCE_ARCHITECTURE
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Public Finance vs. Private Finance Structural Matrix",
                    "content": {
                        "headers": ["Dimension", "Public Finance (National & County Government)", "Private Finance (Individual & Commercial Enterprise)"],
                        "rows": [
                            ["Primary Objective", "Maximizing collective social welfare, public goods provision, and macroeconomic stability", "Maximizing individual utility, household consumption, or commercial enterprise profits"],
                            ["Budget Formulation Sequence", "Determines required expenditures first based on national needs, then mobilizes revenue", "Determines earned income first, then rations household or operational expenditures to fit"],
                            ["Revenue Mobilization Power", "Compulsory taxation enforced by statutory authority (KRA), customs tariffs, sovereign debt", "Voluntary market transactions: wages, profits, crop sales, personal bank loans"],
                            ["Borrowing & Currency Authority", "Can issue sovereign Treasury Bonds, access IMF/World Bank facilities, and regulate legal tender", "Constrained by personal collateral, credit bureau scores, commercial banks, and SACCOs"],
                            ["Auditing & Public Transparency", "Mandatory oversight by the Auditor-General; reports tabled publicly before Parliament and Senate", "Private financial records and internal audits reviewed solely by owners or shareholders"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Categorizing County Government Expenditure and Calculating Development Ratio",
                    "content": {
                        "intro": "The County Government of Machakos prepares its annual fiscal budget of $\\text{KES } 12.0\\text{ billion}$. The County Treasury allocates funds across several vital budget line items: Teacher and Health Worker Salaries = $\\text{KES } 4.5\\text{ billion}$; Fuel and Hospital Pharmaceuticals = $\\text{KES } 1.5\\text{ billion}$; Construction of Sub-County Earth Dams = $\\text{KES } 2.4\\text{ billion}$; Tarmacking County Access Roads = $\\text{KES } 2.1\\text{ billion}$; County Assembly Administration and Office Rent = $\\text{KES } 1.0\\text{ billion}$; and Installation of Solar-Powered Streetlights = $\\text{KES } 0.5\\text{ billion}$. Under the Public Finance Management (PFM) Act, county governments are legally required to allocate at least $30\\%$ of their total budget to development expenditure. Calculate the total Recurrent Expenditure, total Development Expenditure, and determine whether Machakos County satisfies the legal $30\\%$ PFM threshold.",
                        "steps": [
                            {
                                "step_number": 1,
                                "instruction": "Identify and classify all given budget line items into Recurrent ($E_r$) and Development ($E_d$) Expenditures.",
                                "math": "\\begin{aligned} \\text{Recurrent Items } (E_r): & \\\\ & \\text{Salaries} = \\text{KES } 4.5\\text{B} \\\\ & \\text{Fuel \\& Pharmaceuticals} = \\text{KES } 1.5\\text{B} \\\\ & \\text{Administration \\& Rent} = \\text{KES } 1.0\\text{B} \\\\[6pt] \\text{Development Items } (E_d): & \\\\ & \\text{Earth Dams Construction} = \\text{KES } 2.4\\text{B} \\\\ & \\text{Road Tarmacking} = \\text{KES } 2.1\\text{B} \\\\ & \\text{Solar Streetlighting} = \\text{KES } 0.5\\text{B} \\end{aligned}"
                            },
                            {
                                "step_number": 2,
                                "instruction": "State the formula for Total Recurrent Expenditure, Total Development Expenditure, and Development Share Ratio.",
                                "math": "\\begin{aligned} E_{\\text{recurrent}} &= \\sum \\text{Recurrent Operational Allocations} \\\\[4pt] E_{\\text{development}} &= \\sum \\text{Capital Asset Allocations} \\\\[4pt] \\text{Development Ratio } (D_R) &= \\left( \\frac{E_{\\text{development}}}{E_{\\text{total}}} \\right) \\times 100\\% \\end{aligned}"
                            },
                            {
                                "step_number": 3,
                                "instruction": "Substitute the classified values into the summation formulas.",
                                "math": "\\begin{aligned} E_{\\text{recurrent}} &= 4.5\\text{B} + 1.5\\text{B} + 1.0\\text{B} \\\\[4pt] E_{\\text{development}} &= 2.4\\text{B} + 2.1\\text{B} + 0.5\\text{B} \\\\[4pt] E_{\\text{total}} &= 7.0\\text{B} + 5.0\\text{B} = \\text{KES } 12.0\\text{ billion} \\end{aligned}"
                            },
                            {
                                "step_number": 4,
                                "instruction": "Perform the exact mathematical calculations.",
                                "math": "\\begin{aligned} E_{\\text{recurrent}} &= \\text{KES } 7.0\\text{ billion} \\\\[4pt] E_{\\text{development}} &= \\text{KES } 5.0\\text{ billion} \\\\[4pt] D_R &= \\left( \\frac{5.0\\text{ billion}}{12.0\\text{ billion}} \\right) \\times 100\\% = 0.416667 \\times 100\\% = 41.67\\% \\end{aligned}"
                            },
                            {
                                "step_number": 5,
                                "instruction": "State the final calculated numerical answers clearly.",
                                "math": "\\begin{aligned} \\mathbf{E_{\\text{recurrent}}} &= \\mathbf{\\text{KES } 7.0\\text{ Billion }} (58.33\\%) \\\\[4pt] \\mathbf{E_{\\text{development}}} &= \\mathbf{\\text{KES } 5.0\\text{ Billion }} (41.67\\%) \\end{aligned}"
                            },
                            {
                                "step_number": 6,
                                "instruction": "Provide the economic interpretation and common analytical pitfall.",
                                "math": "\\begin{aligned} &\\textbf{Economic Interpretation:} \\\\ &\\text{Machakos County allocates } 41.67\\% \\text{ of its budget to long-term capital assets, easily} \\\\ &\\text{exceeding the statutory } 30\\% \\text{ PFM Act minimum threshold by } 11.67\\%\\text{ points.} \\\\[6pt] &\\textbf{Common Pitfall:} \\\\ &\\text{Confusing operational maintenance (recurrent) with initial asset construction} \\\\ &\\text{(development). E.g., buying spare parts or fuel for county tractors is recurrent.} \\end{aligned}"
                            }
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "case_study",
                    "title": "Kenyan Enterprise Case Study: KENHA and Public Infrastructure Capital Financing",
                    "content": {
                        "company_name": "Kenya National Highways Authority (KeNHA) & The National Treasury",
                        "industry": "Public Sector Infrastructure Development & Transport Logistics",
                        "summary": "KeNHA oversees over 18,000 kilometers of national trunk roads in Kenya. Flagship projects like the Nairobi Expressway (public-private partnership) and the Thika Superhighway required massive initial development expenditures funded through national tax allocations, infrastructure bonds, and concessional loans. These development assets reduce transit times, lower vehicle wear-and-tear for private haulers, cut logistics costs for agricultural produce from Mount Kenya to Nairobi, and stimulate real estate growth across Kiambu and Murang'a counties. Without coordinated public finance, private logistics firms alone could never afford to build such capital assets.",
                        "discussion_questions": [
                            "Why is capital spending on national highways categorized as development expenditure rather than recurrent expenditure?",
                            "How does public infrastructure spending create positive spillover effects for private small and medium enterprises (SMEs) in surrounding towns?",
                            "What fiscal challenges arise if recurrent expenditures (like administrative overheads) consume more than 80% of a country's total tax revenues?"
                        ]
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding Public Finance and National Budgeting",
                    "content": {
                        "title": "Introduction to Public Finance, Taxes, and Government Spending",
                        "youtube_id": "7Qtr_vA3Prw",
                        "url": "https://www.youtube.com/watch?v=7Qtr_vA3Prw",
                        "description": "Educational lecture breaking down the core functions of public finance, how governments formulate national budgets, and the difference between recurrent administrative operations and capital development projects."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 1: Budget Sequence Logic",
                    "content": {
                        "question": "A county finance committee is preparing its annual fiscal budget. Unlike a private business enterprise, which sequence best describes how the county government must plan its finances?",
                        "options": {
                            "A": "It records past profit reserves first, then pays private dividends to voters",
                            "B": "It estimates the total societal needs and required expenditures first, then plans how to mobilize matching tax revenues and borrowings",
                            "C": "It waits until the end of the year to see what voluntary donations it receives before providing essential medical supplies",
                            "D": "It limits its spending strictly to the cash balance held in its commercial bank accounts without estimating future needs"
                        },
                        "correct_answer": "B",
                        "explanation": "In public finance, governments operate on an inverse budget sequence: they determine the societal necessity for public services (roads, schools, health, security) first, and then design the tax policies, statutory rates, and sovereign loans needed to finance those expenditures."
                    }
                },
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 2: Recurrent vs. Development Expenditure",
                    "content": {
                        "question": "Which of the following government expenditures in Kenya is correctly classified as Development Expenditure?",
                        "options": {
                            "A": "Paying monthly salary allowances and pensions to medical doctors in county referral hospitals",
                            "B": "Purchasing diesel fuel and engine oil for police patrol cars in Nairobi",
                            "C": "Financing the construction of the Konza Technopolis digital data center and fiber backbone",
                            "D": "Settling monthly electricity bills for national ministry offices at Harambee House"
                        },
                        "correct_answer": "C",
                        "explanation": "Development expenditure refers to long-term capital investments that create permanent, productive physical or digital assets (such as Konza Technopolis data center and fiber optic infrastructure). Salaries, vehicle fuel, and office utility bills are recurrent operational expenses consumed within the current financial year."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary",
                    "title": "Lesson 1 Synthesis: Foundations of Public Finance",
                    "content": {
                        "text": "### Key Conceptual Takeaways\n\n1. **Core Purpose of Public Finance:** While private entities focus on individual profit and utility, public finance focuses on maximizing social welfare, correcting market failures, and supplying essential public goods.\n2. **The Sovereign Budgeting Order:** Governments formulate budgets by evaluating total public spending requirements first, followed by structuring tax policies and sovereign debt to fund the deficit.\n3. **Dual Expenditure Taxonomy:** Public spending is split into **Recurrent Expenditure** (short-term operational overheads like civil service salaries and medical consumables) and **Development Expenditure** (long-term wealth-creating capital assets like railways, highways, and dams).\n4. **Statutory Fiscal Rules:** In Kenya, the Public Finance Management (PFM) Act mandates that at least $30\\%$ of national and county budgets must be allocated toward development expenditure to guarantee future economic growth."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Government Revenue and Principles of Taxation
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Government Revenue and Principles of Taxation",
        "unit_description": "Comprehensive analysis of sovereign revenue streams, statutory tax bases, the KRA PIN system, and Adam Smith's four classical canons of taxation: Equity, Certainty, Convenience, and Economy.",
        "lesson_title": "Government Revenue and Principles of Taxation",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Times Tower Nairobi: Headquarters of Kenya Revenue Authority",
                    "content": {
                        "title": "Kenya Revenue Authority (KRA) Times Tower",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Times_Tower_from_KICC.jpg",
                        "caption": "Times Tower in Nairobi, the central operational headquarters of the Kenya Revenue Authority (KRA), where national tax revenue mobilization and compliance systems are administered.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define tax, taxation, and tax base in commercial legal frameworks\n- Explain the significance of the KRA PIN requirement in commercial transactions and national revenue monitoring\n- Analyze Adam Smith's four Canons of Taxation (Equity, Certainty, Convenience, and Economy)\n- Evaluate real-world tax policies and identify violations of specific taxation principles"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Tax, Taxation and the Tax Base",
                    "content": {
                        "term": "Tax & Tax Base",
                        "definition": "A Tax is a compulsory financial levy imposed by a sovereign government on individuals, businesses, or transactions to finance public spending without a direct, specific quid pro quo return. The Tax Base is the collective monetary value of economic assets, incomes, sales, or wealth transactions legally subject to taxation."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The KRA PIN & The Welfare Club Analogy",
                    "content": {
                        "text": "Taxation can be understood through institutional and social lenses:\n\n- **The Welfare Club Analogy:** Think of a country as a large community welfare association. To install perimeter fencing, hire security guards, and maintain water pumps, every resident must contribute a mandatory monthly fee. If residents refuse to contribute, security collapses and all suffer. Taxes are the compulsory civic contributions that maintain the state.\n- **The KRA Personal Identification Number (PIN):** In Kenya, the KRA PIN is a unique 11-character alphanumeric identifier required to open bank accounts, buy real estate, import goods, apply for government tenders, or register motor vehicles. It links all formal economic transactions directly to the national tax base, minimizing under-reporting and tax leakage."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Adam Smith's 4 Canons of Taxation Framework",
                    "content": {
                        "title": "The 4 Canons of Modern Taxation Architecture",
                        "caption": "Vector SVG diagram illustrating the 4 core principles of taxation (Equity, Certainty, Convenience, Economy) alongside their operational rules and Kenyan tax administration applications.",
                        "svg_content": SVG_CANONS_OF_TAXATION_FRAMEWORK
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Adam Smith's Canons of Taxation Detailed Matrix",
                    "content": {
                        "headers": ["Canon (Principle)", "Core Economic Rule", "Practical Implementation", "Real-World Kenyan Example"],
                        "rows": [
                            ["Principle of Equity (Fairness)", "Taxes must be assessed according to ability-to-pay. Wealthier citizens pay more; poorer citizens pay less.", "Graduated income tax brackets ensure vertical equity; equal income brackets ensure horizontal equity.", "Graduated PAYE income tax rates ranging from 10% to 35% based on monthly taxable income tiers"],
                            ["Principle of Certainty", "The tax liability, calculation method, and payment deadline must be clear, transparent, and non-arbitrary.", "Tax laws must be enacted by Parliament and published in statutory finance acts before enforcement.", "Finance Acts and published KRA tax tables specifying exact filing deadlines (e.g., 9th or 20th of every month)"],
                            ["Principle of Convenience", "Taxes should be levied and collected at a time and manner most effortless and accessible for taxpayers.", "Deducting taxes at the point of income receipt or point of sale avoids complex manual filing.", "VAT added seamlessly at supermarket cash registers; PAYE deducted directly from monthly payrolls"],
                            ["Principle of Economy (Efficiency)", "The administrative cost of assessing and collecting the tax must be significantly lower than the revenue collected.", "Automating compliance through digital portals reduces paper processing, staff travel, and collection overhead.", "KRA iTax and eTIMS electronic invoicing systems minimizing operational collection expenses"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Evaluating Tax Collection Efficiency Ratio under the Principle of Economy",
                    "content": {
                        "intro": "The County Government of Bungoma evaluates two distinct revenue collection methods for agricultural trade licenses. **System A (Manual Physical Collection)** collects $\\text{KES } 50.0\\text{ million}$ in licensing fees but incurs $\\text{KES } 32.5\\text{ million}$ in expenses for physical revenue inspectors, motor vehicle fuel, manual paper receipts, and cash transport security. **System B (Digital USSD & Paybill System)** collects $\\text{KES } 75.0\\text{ million}$ in licensing fees and incurs only $\\text{KES } 3.0\\text{ million}$ in automated software hosting, telecom network fees, and SMS alerts. Calculate the Collection Cost Ratio ($C_R$) and Net Revenue Harvested ($R_{net}$) for each system, and determine which system complies with Adam Smith's Principle of Economy.",
                        "steps": [
                            {
                                "step_number": 1,
                                "instruction": "Identify given revenue ($R_{gross}$) and administrative collection cost ($C_{admin}$) for both systems.",
                                "math": "\\begin{aligned} \\text{System A (Manual):} & \\quad R_{\\text{gross}} = \\text{KES } 50.0\\text{M}, \\quad C_{\\text{admin}} = \\text{KES } 32.5\\text{M} \\\\[4pt] \\text{System B (Digital):} & \\quad R_{\\text{gross}} = \\text{KES } 75.0\\text{M}, \\quad C_{\\text{admin}} = \\text{KES } 3.0\\text{M} \\end{aligned}"
                            },
                            {
                                "step_number": 2,
                                "instruction": "State the formulas for Collection Cost Ratio ($C_R$) and Net Revenue Harvested ($R_{\\text{net}}$).",
                                "math": "\\begin{aligned} C_R &= \\left( \\frac{C_{\\text{admin}}}{R_{\\text{gross}}} \\right) \\times 100\\% \\\\[6pt] R_{\\text{net}} &= R_{\\text{gross}} - C_{\\text{admin}} \\end{aligned}"
                            },
                            {
                                "step_number": 3,
                                "instruction": "Substitute values for System A (Manual) and calculate.",
                                "math": "\\begin{aligned} C_{R(A)} &= \\left( \\frac{32.5\\text{ million}}{50.0\\text{ million}} \\right) \\times 100\\% = 0.65 \\times 100\\% = 65.0\\% \\\\[4pt] R_{\\text{net}(A)} &= 50.0\\text{M} - 32.5\\text{M} = \\text{KES } 17.5\\text{ million} \\end{aligned}"
                            },
                            {
                                "step_number": 4,
                                "instruction": "Substitute values for System B (Digital) and calculate.",
                                "math": "\\begin{aligned} C_{R(B)} &= \\left( \\frac{3.0\\text{ million}}{75.0\\text{ million}} \\right) \\times 100\\% = 0.04 \\times 100\\% = 4.0\\% \\\\[4pt] R_{\\text{net}(B)} &= 75.0\\text{M} - 3.0\\text{M} = \\text{KES } 72.0\\text{ million} \\end{aligned}"
                            },
                            {
                                "step_number": 5,
                                "instruction": "State the comparative results clearly.",
                                "math": "\\begin{aligned} \\mathbf{\\text{System A:}} & \\quad C_R = 65.0\\%, \\quad R_{\\text{net}} = \\text{KES } 17.5\\text{ Million (Highly Inefficient)} \\\\[4pt] \\mathbf{\\text{System B:}} & \\quad C_R = 4.0\\%, \\quad R_{\\text{net}} = \\text{KES } 72.0\\text{ Million (Highly Economical)} \\end{aligned}"
                            },
                            {
                                "step_number": 6,
                                "instruction": "Provide the economic interpretation and common analytical pitfall.",
                                "math": "\\begin{aligned} &\\textbf{Economic Interpretation:} \\\\ &\\text{System B satisfies the Principle of Economy by spending only } 4\\% \\text{ of revenue} \\\\ &\\text{on collection, yielding KES } 72\\text{M net for public services. System A consumes } 65\\% \\\\ &\\text{of its proceeds in administrative overhead, severely violating the canon of economy.} \\\\[6pt] &\\textbf{Common Pitfall:} \\\\ &\\text{Looking only at gross revenue without deducting administrative collection costs.} \\end{aligned}"
                            }
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "case_study",
                    "title": "Kenyan Enterprise Case Study: KRA iTax and eTIMS Digital Transformation",
                    "content": {
                        "company_name": "Kenya Revenue Authority (KRA)",
                        "industry": "National Revenue Administration & Digital Tax Systems",
                        "summary": "Before the introduction of the digital iTax system and electronic Tax Invoice Management System (eTIMS), Kenyan taxpayers had to physically line up for hours at Times Tower and Huduma Centres with stacks of printed paperwork to file tax returns and pay PAYE or VAT. KRA spent millions of shillings annually printing forms and hiring manual data-entry clerks. By deploying iTax and mobile USSD paybills (*222#), KRA digitized compliance: citizens can file returns and generate payment slips in minutes from smartphones. Administrative collection costs plummeted from over 3.5% of gross revenue to below 1.2%, exemplifying Adam Smith's Canons of Convenience and Economy in action.",
                        "discussion_questions": [
                            "How does the integration of mobile money (M-Pesa) payments with KRA systems promote the Canon of Convenience?",
                            "Why does digital tax filing reduce opportunities for corruption and improve the Principle of Certainty?",
                            "In what ways does electronic tax invoice tracking (eTIMS) help broaden the national tax base?"
                        ]
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Adam Smith's Canons of Taxation and Modern Public Revenue",
                    "content": {
                        "title": "Principles and Canons of Good Taxation Explained",
                        "youtube_id": "rS_33F-J7_Y",
                        "url": "https://www.youtube.com/watch?v=rS_33F-J7_Y",
                        "description": "Comprehensive walkthrough of Adam Smith's four canons of taxation (Equity, Certainty, Convenience, Economy) with practical real-world applications in developing economies."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 1: Canon of Economy Violation",
                    "content": {
                        "question": "A municipality introduces a property parking levy that generates KES 10,000,000 annually. However, hiring manual fee collectors, printing duplicate carbon receipts, and fueling surveillance vehicles costs KES 8,500,000 each year. Which canon of taxation is most severely violated?",
                        "options": {
                            "A": "Principle of Convenience",
                            "B": "Principle of Economy",
                            "C": "Principle of Equity",
                            "D": "Principle of Certainty"
                        },
                        "correct_answer": "B",
                        "explanation": "The Principle of Economy dictates that the administrative cost of assessing and collecting a tax should be kept as low as possible relative to the revenue collected. Spending 85% of total collections on administrative costs makes the tax wasteful and economically inefficient."
                    }
                },
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 2: Canon of Convenience in Practice",
                    "content": {
                        "question": "Supermarkets in Kenya automatically calculate and incorporate 16% Value Added Tax (VAT) into the printed item shelf prices and cash register receipts at the point of sale. Which canon of taxation is directly demonstrated by this mechanism?",
                        "options": {
                            "A": "Principle of Convenience",
                            "B": "Principle of Proportionality",
                            "C": "Principle of Fiscal Neutrality",
                            "D": "Principle of Elasticity"
                        },
                        "correct_answer": "A",
                        "explanation": "The Principle of Convenience requires taxes to be collected at a time and in a manner easiest and most effortless for the taxpayer. Collecting VAT automatically at checkout without requiring consumers to complete separate tax forms ensures effortless compliance."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary",
                    "title": "Lesson 2 Synthesis: Principles of Sovereign Taxation",
                    "content": {
                        "text": "### Key Conceptual Takeaways\n\n1. **Nature of Taxation:** Taxes are compulsory statutory levies that expand the state's capacity to build infrastructure and protect social welfare without providing a direct 1-to-1 personal return.\n2. **The 4 Golden Canons:** Formulated by Adam Smith, the four essential principles are:\n   - **Equity:** Fairness through ability to pay (wealthy contribute higher proportions).\n   - **Certainty:** Transparent rates, clear deadlines, and predictable assessments.\n   - **Convenience:** Frictionless payment timing and effortless collection channels.\n   - **Economy:** Minimal administrative collection overheads relative to revenue harvested.\n3. **Modern Digital Enablers:** Platforms such as KRA iTax, eTIMS, and mobile payment gateways operationalize the canons of convenience and economy by cutting paperwork and slashing collection costs."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Types of Taxes and Their Impact
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Types of Taxes and Their Impact",
        "unit_description": "Tax taxonomy: Direct vs. Indirect taxes, tax shifting dynamics, impact vs. incidence, and progressive, proportional, and regressive tax rate structures.",
        "lesson_title": "Types of Taxes and Their Impact",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Retail Shopping and VAT Invoicing in Nairobi",
                    "content": {
                        "title": "Retail Commerce and Consumption Tax Breakdown",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "Vibrant commercial trade in a Kenyan marketplace, highlighting the daily application of indirect consumption taxes (VAT and Excise Duty) alongside direct income taxes.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between Direct Taxes and Indirect Taxes based on tax incidence and shifting mechanisms\n- Identify key examples of direct taxes (PAYE, Corporate Tax, Capital Gains Tax) and indirect taxes (VAT, Excise Duty, Customs)\n- Analyze the three primary tax rate structures: Progressive, Proportional, and Regressive tax systems\n- Explain why flat-rate consumption taxes (such as VAT) exhibit regressive economic effects on low-income households"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Direct Taxes vs. Indirect Taxes",
                    "content": {
                        "term": "Direct & Indirect Taxes",
                        "definition": "A Direct Tax is a levy assessed directly on the income, profits, or wealth of an individual or legal corporation, where the tax burden cannot be shifted to another party (Impact = Incidence). An Indirect Tax is a levy assessed on the consumption, manufacture, or sale of goods and services, where the initial tax burden can be shifted forward to the final consumer (Impact ≠ Incidence)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Arrow vs. The Net Analogy & Tax Shifting",
                    "content": {
                        "text": "The distinction between direct and indirect taxes is readily understood through two visual concepts:\n\n- **The Arrow (Direct Tax):** The government aims an arrow directly at an identified earner (e.g., an employee's salary or a bank's corporate profit). The person or firm struck by the arrow must pay the tax out-of-pocket; they cannot dodge or pass the arrow along.\n- **The Net (Indirect Tax):** The government casts a net across the entire marketplace of consumer transactions. When a consumer purchases a soda, mobile airtime, or imported shoes, they swim into the net and pay the tax. The retailer merely acts as a collection agent who shifts the tax burden forward to the consumer in the form of higher shelf prices."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Tax Classification: Direct vs Indirect and Rate Progression Spectrum",
                    "content": {
                        "title": "Tax Taxonomy, Incidence Shifting & Rate Structures",
                        "caption": "Vector SVG diagram illustrating the flow of direct vs indirect taxes, tax incidence shifting, and the economic comparison of progressive, proportional, and regressive tax models.",
                        "svg_content": SVG_TAX_STRUCTURE_AND_PROGRESSION
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Comprehensive Tax System Classification Matrix",
                    "content": {
                        "headers": ["Tax Structure", "Rate Mechanics with Respect to Income", "Who Bears Relative Burden?", "Kenyan Real-World Example", "Macroeconomic Purpose"],
                        "rows": [
                            ["Progressive Tax", "Tax rate (%) increases as the taxpayer's income increases.", "Higher-income earners pay a higher proportion of income.", "PAYE personal income tax (10% on lowest bracket up to 35% on high earners)", "Reduces national income inequality and acts as an automatic economic stabilizer."],
                            ["Proportional (Flat) Tax", "Tax rate (%) remains constant regardless of total income.", "Equal percentage burden across all income earners.", "Standard Corporate Income Tax (flat 30% on net profits of resident firms)", "Ensures administrative simplicity and avoids penalizing capital investment growth."],
                            ["Regressive Tax", "Effective tax rate (% of income) decreases as income rises.", "Lower-income households bear a heavier relative burden.", "Flat 16% VAT on basic consumer goods and flat Excise Duty on kerosene", "Yields broad, predictable revenue but disproportionately burdens low-income budgets."]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Progressive PAYE and Demonstrating Regressive VAT Impact",
                    "content": {
                        "intro": "Consider two citizens living in Eldoret: **Taxpayer A (Teacher)** earning a gross taxable monthly income of $\\text{KES } 50,000$, and **Taxpayer B (Senior Director)** earning a gross taxable monthly income of $\\text{KES } 500,000$. \n\n1. Calculate the direct PAYE tax paid by both under a progressive tax schedule (assume simplified effective rates: $12\\%$ for Teacher, $30\\%$ for Director).\n2. If both purchase an identical smartphone costing $\\text{KES } 25,000$ (with $16\\%$ VAT included, meaning $\\text{KES } 3,448.28$ VAT amount), calculate the percentage of each citizen's monthly income consumed by that identical VAT levy to mathematically prove the regressive nature of flat consumption taxes.",
                        "steps": [
                            {
                                "step_number": 1,
                                "instruction": "Identify the income and tax parameters for both taxpayers.",
                                "math": "\\begin{aligned} \\text{Taxpayer A (Teacher):} & \\quad Y_A = \\text{KES } 50,000, \\quad t_{\\text{eff}} = 12\\% \\\\[4pt] \\text{Taxpayer B (Director):} & \\quad Y_B = \\text{KES } 500,000, \\quad t_{\\text{eff}} = 30\\% \\\\[4pt] \\text{VAT on Smartphone:} & \\quad T_{\\text{vat}} = \\text{KES } 3,448.28 \\end{aligned}"
                            },
                            {
                                "step_number": 2,
                                "instruction": "State the formulas for Direct PAYE Tax ($T_{\\text{paye}}$) and Effective VAT Burden Ratio ($B_{\\text{vat}}$).",
                                "math": "\\begin{aligned} T_{\\text{paye}} &= Y \\times t_{\\text{eff}} \\\\[6pt] B_{\\text{vat}} &= \\left( \\frac{T_{\\text{vat}}}{Y} \\right) \\times 100\\% \\end{aligned}"
                            },
                            {
                                "step_number": 3,
                                "instruction": "Calculate the direct PAYE income tax for both taxpayers.",
                                "math": "\\begin{aligned} T_{\\text{paye}(A)} &= 50,000 \\times 0.12 = \\text{KES } 6,000 \\\\[4pt] T_{\\text{paye}(B)} &= 500,000 \\times 0.30 = \\text{KES } 150,000 \\end{aligned}"
                            },
                            {
                                "step_number": 4,
                                "instruction": "Calculate the effective VAT income burden ratio ($B_{\\text{vat}}$) for both taxpayers.",
                                "math": "\\begin{aligned} B_{\\text{vat}(A)} &= \\left( \\frac{3,448.28}{50,000} \\right) \\times 100\\% = 6.8966\\% \\approx 6.90\\% \\\\[6pt] B_{\\text{vat}(B)} &= \\left( \\frac{3,448.28}{500,000} \\right) \\times 100\\% = 0.6896\\% \\approx 0.69\\% \\end{aligned}"
                            },
                            {
                                "step_number": 5,
                                "instruction": "State the final calculated outputs clearly.",
                                "math": "\\begin{aligned} \\mathbf{\\text{Direct PAYE:}} & \\quad \\text{Teacher: KES } 6,000 \\; (12\\%) \\quad \\text{vs.} \\quad \\text{Director: KES } 150,000 \\; (30\\%) \\\\[4pt] \\mathbf{\\text{VAT Burden:}} & \\quad \\text{Teacher: } 6.90\\% \\text{ of income} \\quad \\text{vs.} \\quad \\text{Director: } 0.69\\% \\text{ of income} \\end{aligned}"
                            },
                            {
                                "step_number": 6,
                                "instruction": "Provide the economic interpretation and common analytical pitfall.",
                                "math": "\\begin{aligned} &\\textbf{Economic Interpretation:} \\\\ &\\text{Direct PAYE is progressive because the director pays a higher percentage (30\\% vs 12\\%).} \\\\ &\\text{However, the flat VAT is regressive in economic impact because the identical KES 3,448 tax} \\\\ &\\text{absorbs } 10\\times \\text{ more of the teacher's income (6.90\\%) than the director's (0.69\\%).} \\\\[6pt] &\\textbf{Common Pitfall:} \\\\ &\\text{Assuming that because VAT is charged at a flat 16\\%, it treats everyone equally in} \\\\ &\\text{economic terms. Flat nominal rates always place a heavier real burden on the poor.} \\end{aligned}"
                            }
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "case_study",
                    "title": "Kenyan Enterprise Case Study: East African Breweries (EABL) and Excise Duty Escalation",
                    "content": {
                        "company_name": "East African Breweries PLC (EABL)",
                        "industry": "Consumer Goods & Beverage Manufacturing",
                        "summary": "EABL is one of Kenya's largest corporate taxpayers, paying billions of shillings annually in Corporate Tax (direct), VAT (indirect), and Excise Duty ('sin tax' on alcoholic beverages). When the National Treasury increases excise duty on beer and spirits by 10% to 20% in annual Finance Acts, EABL cannot absorb the massive cost increases without collapsing its operating margins. Instead, EABL shifts the tax burden forward by increasing retail shelf prices for consumers across bars and supermarkets. While this increases state revenue and discourages excessive consumption, steep price hikes can inadvertently drive low-income consumers toward illicit, unregulated, and dangerous moonshine brews.",
                        "discussion_questions": [
                            "Why is excise duty classified as an indirect tax rather than a direct tax?",
                            "How do excise tax increases illustrate forward tax shifting from manufacturers to retail consumers?",
                            "What unintended social and economic risks arise when indirect sin taxes are increased too aggressively?"
                        ]
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Direct vs Indirect Taxes & Progressive Tax Systems",
                    "content": {
                        "title": "Direct vs Indirect Taxes: Macroeconomics & Tax Incidence",
                        "youtube_id": "r-xW36G1088",
                        "url": "https://www.youtube.com/watch?v=r-xW36G1088",
                        "description": "Clear macroeconomic visual breakdown showing the difference between direct taxes on income and indirect taxes on consumer spending, including progressive and regressive tax incidence."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 1: Tax Incidence and Shifting",
                    "content": {
                        "question": "A business in Nakuru pays 30% corporate income tax on its annual net profits and also collects 16% VAT from retail shoppers buying electronic accessories. Which statement correctly describes the tax incidence in these two cases?",
                        "options": {
                            "A": "Both the corporate tax and the VAT are shifted forward to the retail shoppers",
                            "B": "The corporate tax cannot be shifted and is borne directly by the business owners, whereas the VAT burden is shifted to the shoppers",
                            "C": "The VAT is paid entirely out of the business's profits, while the corporate tax is deducted from the shoppers' salaries",
                            "D": "Neither tax can be shifted; both must be paid personally by the company's directors"
                        },
                        "correct_answer": "B",
                        "explanation": "Corporate income tax is a direct tax levied on company profits, meaning the impact and incidence rest entirely on the firm and its shareholders. VAT is an indirect consumption tax where the business acts as a collecting agent, passing the economic burden directly onto consumers through retail prices."
                    }
                },
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 2: Regressive Tax Structure",
                    "content": {
                        "question": "Why is a flat-rate consumption tax (such as VAT on paraffin or cooking flour) considered regressive in economic terms?",
                        "options": {
                            "A": "Because high-income earners pay a higher percentage of their monthly income on the tax",
                            "B": "Because the total amount of money collected decreases every year",
                            "C": "Because the tax consumes a significantly higher proportion of a low-income person's income than that of a wealthy person",
                            "D": "Because the government spends the money only in rural counties"
                        },
                        "correct_answer": "C",
                        "explanation": "A tax is regressive when lower-income earners spend a larger fraction of their total income paying that tax than higher-income earners, even though the nominal statutory percentage is identical for everyone."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary",
                    "title": "Lesson 3 Synthesis: Tax Classifications and Incidence",
                    "content": {
                        "text": "### Key Conceptual Takeaways\n\n1. **Direct Taxes (The Arrow):** Levied directly on income, wealth, and corporate profits (e.g., PAYE, Corporate Tax). The statutory taxpayer bears the entire economic burden (cannot be shifted).\n2. **Indirect Taxes (The Net):** Levied on expenditure, manufacturing, and consumption (e.g., VAT, Excise Duty). Businesses shift the tax burden forward to final consumers in higher shelf prices.\n3. **Progressive vs. Regressive Effects:**\n   - **Progressive (PAYE):** Percentage rate rises with income, promoting vertical equity and reducing inequality.\n   - **Proportional (Corporate Tax):** Flat constant percentage applied across all income tiers.\n   - **Regressive (VAT):** Flat consumption levies absorb a much larger share of low-income household earnings, placing a heavier real burden on the poor."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Customs Duties and International Trade Taxes
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Customs Duties and International Trade Taxes",
        "unit_description": "Cross-border trade tariffs: Import and export duties, infant industry protection, anti-dumping measures, foreign exchange conservation, and the economic trade-offs of protectionism.",
        "lesson_title": "Customs Duties and International Trade Taxes",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Port of Mombasa Container Shipping Terminal",
                    "content": {
                        "title": "International Trade Cargo and Customs Clearance at Mombasa",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Port_of_Mombasa.jpg",
                        "caption": "Container cargo ships and gantry cranes at the Port of Mombasa, the primary maritime gateway where Kenya Revenue Authority customs officers inspect cargo, verify invoices, and collect import duties.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define customs duty, import duty, and export duty in international trade\n- Explain the concept of protectionism and the Infant Industry Argument\n- Analyze the 4 primary strategic reasons governments impose customs tariffs (protection, revenue, curbing harmful imports, FX conservation)\n- Calculate customs duties and evaluate the economic trade-offs between shielding local jobs and consumer price inflation"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Customs Duties & Protectionism",
                    "content": {
                        "term": "Customs Duty & Protectionism",
                        "definition": "Customs Duty is a statutory tax levied by the government on goods imported into (Import Duty) or exported out of (Export Duty) a sovereign customs territory. Protectionism is the strategic economic policy of restricting foreign imports via tariffs, quotas, and quality standards to shield domestic industries from foreign competition."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Speed Bump Analogy & Infant Industries",
                    "content": {
                        "text": "Customs tariffs function as targeted economic barriers:\n\n- **The Speed Bump Analogy:** Imagine local runners racing against foreign competitors who drive powerful sports cars built with foreign government subsidies. To level the competition, the race marshals place speed bumps (customs tariffs) exclusively on the foreign lanes. By making foreign goods artificially more expensive, local producers get a fair opportunity to sell their products.\n- **Infant Industry Argument:** Newly established domestic factories (e.g., local textile mills, edible oil refiners, automotive assemblers) have not yet achieved large economies of scale or operational efficiency. Without temporary tariff protection against cheap mass-produced imports, these infant industries would collapse before maturing."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Customs Duty Tariff Wall and Infant Industry Protection",
                    "content": {
                        "title": "Customs Tariff Wall and Domestic Production Equilibrium",
                        "caption": "Vector SVG diagram illustrating the arrival of subsidized foreign imports at the Port of Mombasa, the application of KRA customs tariffs, and the resulting price competitiveness of local Kenyan factories.",
                        "svg_content": SVG_CUSTOMS_DUTY_AND_PROTECTIONISM
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Motivations for Imposing International Trade Taxes Matrix",
                    "content": {
                        "headers": ["Policy Objective", "Economic Mechanism", "Kenyan Real-World Case", "Potential Economic Risk / Trade-Off"],
                        "rows": [
                            ["Protecting Infant Domestic Industries", "Imposing high tariffs makes foreign substitutes expensive, directing domestic demand to local producers.", "High import duties on finished furniture and plastic goods to protect Gikomba and local carpentry firms", "Local manufacturers may become complacent and produce substandard goods if protected indefinitely."],
                            ["Mobilizing Sovereign Revenue", "Collecting ad valorem tariffs on billions worth of consumer imports at Mombasa Port and JKIA Airport.", "East African Community Common External Tariff (EAC-CET) raising hundreds of billions annually for Treasury", "High tariffs increase the landing cost of industrial capital machinery, slowing modernization."],
                            ["Curtailing Harmful & Luxury Goods", "Applying punitive tariffs to discourage consumption of luxury goods, polluting items, or toxic waste.", "Heavy duties on luxury motor vehicles (above 3000cc) and used electronics to curb e-waste", "Excessively punitive tariffs create strong incentives for border smuggling and black-market trade."],
                            ["Conserving Foreign Exchange Reserves", "Dampening national import demand keeps scarce US Dollars within the domestic banking system.", "Restricting non-essential agricultural imports (e.g., eggs, onions) to support the Kenyan Shilling (KES)", "May invite retaliatory tariffs from neighboring trading partners, harming Kenya's agricultural exports."]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Multi-Tier Customs Clearance (CIF, Duty, IDF, and VAT)",
                    "content": {
                        "intro": "An entrepreneur in Nairobi imports a commercial industrial solar water pump from Germany with a Cost, Insurance, and Freight (CIF) value of $\\text{KES } 200,000$ at the Port of Mombasa. The customs clearance schedule applies the following statutory rates: **Customs Import Duty = $25\\%$** (calculated on CIF value); **Import Declaration Fee (IDF) = $3.5\\%$** (calculated on CIF value); **Railway Development Levy (RDL) = $2.0\\%$** (calculated on CIF value); and **Value Added Tax (VAT) = $16\\%$** (calculated on the combined total of CIF + Customs Duty + IDF + RDL). Calculate the Customs Duty, IDF, RDL, VAT, and the Total Landed Clearance Cost paid to clear the cargo.",
                        "steps": [
                            {
                                "step_number": 1,
                                "instruction": "Identify the base CIF value and statutory tariff rates.",
                                "math": "\\begin{aligned} \\text{Base CIF Value} &= \\text{KES } 200,000 \\\\[4pt] \\text{Customs Duty Rate } (r_d) &= 25\\% = 0.25 \\\\[4pt] \\text{IDF Rate } (r_{\\text{idf}}) &= 3.5\\% = 0.035 \\\\[4pt] \\text{RDL Rate } (r_{\\text{rdl}}) &= 2.0\\% = 0.020 \\\\[4pt] \\text{VAT Rate } (r_{\\text{vat}}) &= 16\\% = 0.16 \\end{aligned}"
                            },
                            {
                                "step_number": 2,
                                "instruction": "State the clearance formulas for Duty, IDF, RDL, Taxable VAT Base ($V_{\\text{base}}$), VAT, and Total Clearance Cost ($C_{\\text{total}}$).",
                                "math": "\\begin{aligned} \\text{Duty} &= \\text{CIF} \\times r_d \\\\[4pt] \\text{IDF} &= \\text{CIF} \\times r_{\\text{idf}}, \\quad \\text{RDL} = \\text{CIF} \\times r_{\\text{rdl}} \\\\[4pt] V_{\\text{base}} &= \\text{CIF} + \\text{Duty} + \\text{IDF} + \\text{RDL} \\\\[4pt] \\text{VAT} &= V_{\\text{base}} \\times r_{\\text{vat}} \\\\[4pt] C_{\\text{total}} &= V_{\\text{base}} + \\text{VAT} \\end{aligned}"
                            },
                            {
                                "step_number": 3,
                                "instruction": "Calculate the primary import levies based on CIF.",
                                "math": "\\begin{aligned} \\text{Customs Duty} &= 200,000 \\times 0.25 = \\text{KES } 50,000 \\\\[4pt] \\text{IDF} &= 200,000 \\times 0.035 = \\text{KES } 7,000 \\\\[4pt] \\text{RDL} &= 200,000 \\times 0.020 = \\text{KES } 4,000 \\end{aligned}"
                            },
                            {
                                "step_number": 4,
                                "instruction": "Determine the compounded VAT Taxable Base ($V_{\\text{base}}$) and calculate the VAT amount.",
                                "math": "\\begin{aligned} V_{\\text{base}} &= 200,000 + 50,000 + 7,000 + 4,000 = \\text{KES } 261,000 \\\\[6pt] \\text{VAT} &= 261,000 \\times 0.16 = \\text{KES } 41,760 \\end{aligned}"
                            },
                            {
                                "step_number": 5,
                                "instruction": "Sum all components to find the final Total Landed Clearance Cost.",
                                "math": "\\begin{aligned} C_{\\text{total}} &= 261,000 + 41,760 = \\mathbf{\\text{KES } 302,760} \\\\[4pt] \\text{Total Taxes Paid to KRA} &= 50,000 + 7,000 + 4,000 + 41,760 = \\mathbf{\\text{KES } 102,760} \\end{aligned}"
                            },
                            {
                                "step_number": 6,
                                "instruction": "Provide the economic interpretation and common analytical pitfall.",
                                "math": "\\begin{aligned} &\\textbf{Economic Interpretation:} \\\\ &\\text{Taxes and duties add KES } 102,760 \\text{ (a } 51.38\\% \\text{ markup) to the base CIF cost,} \\\\ &\\text{raising the domestic price to KES } 302,760. \\text{ This raises KRA revenue while} \\\\ &\\text{shielding local solar equipment assemblers from direct price undercutting.} \\\\[6pt] &\\textbf{Common Pitfall:} \\\\ &\\text{Calculating VAT directly on the CIF value alone, rather than on the compounded} \\\\ &\\text{base inclusive of customs duty, IDF, and RDL as mandated by Kenyan tax law.} \\end{aligned}"
                            }
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "case_study",
                    "title": "Kenyan Enterprise Case Study: Athi River Cement and Anti-Dumping Protection",
                    "content": {
                        "company_name": "Kenyan Domestic Cement & Steel Manufacturers (Athi River)",
                        "industry": "Heavy Manufacturing & Building Materials",
                        "summary": "In the construction boom of the last decade, large overseas producers began shipping excess clinker and bagged cement to Mombasa at prices significantly below local production costs—a practice known as 'dumping'. Local cement factories in Athi River and Mombasa that employed thousands of Kenyans and paid billions in local power bills faced severe financial distress. In response, the Kenyan National Treasury and EAC ministers adjusted the Common External Tariff to impose a 35% duty on imported finished cement and clinker. This tariff barrier saved local manufacturing jobs, stimulated domestic quarrying in Machakos and Kajiado, and generated substantial import duty revenues for the national government.",
                        "discussion_questions": [
                            "What is trade 'dumping', and why does it threaten domestic manufacturing firms?",
                            "How did imposing a 35% import tariff help preserve Kenyan jobs in Athi River cement mills?",
                            "What are the risks to home builders if domestic manufacturers fail to improve efficiency despite tariff protection?"
                        ]
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Customs Duties, Tariffs and International Trade Economics",
                    "content": {
                        "title": "Tariffs, Import Duties and Protectionism Explained",
                        "youtube_id": "Y2X3KPilAtQ",
                        "url": "https://www.youtube.com/watch?v=Y2X3KPilAtQ",
                        "description": "Educational breakdown of how customs tariffs work, why governments implement import duties to protect domestic industries, and how trade barriers impact global supply chains."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 1: Infant Industry Protection",
                    "content": {
                        "question": "A newly formed Kenyan leather processing cooperative in Kitale is struggling to sell school shoes because cheap imported synthetic shoes are flooding the market at half the price. Which policy action by the National Treasury would best protect this infant domestic industry?",
                        "options": {
                            "A": "Abolishing all export duties on raw cattle hides leaving Kenya",
                            "B": "Imposing a substantial customs import tariff on cheap synthetic foreign footwear",
                            "C": "Removing all KRA PIN requirements for foreign shoe importers",
                            "D": "Increasing corporate taxes on the domestic shoe cooperative"
                        },
                        "correct_answer": "B",
                        "explanation": "Imposing customs import tariffs raises the domestic landing price of cheap foreign footwear, leveling the playing field and allowing the young domestic leather cooperative (an infant industry) to gain market share and build economies of scale."
                    }
                },
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 2: Compounded VAT Customs Base",
                    "content": {
                        "question": "Under Kenyan customs tax procedures, on which base amount is Value Added Tax (VAT at 16%) calculated when clearing imported commercial goods at the Port of Mombasa?",
                        "options": {
                            "A": "Exclusively on the exporter's factory price before shipping",
                            "B": "Only on the customs duty amount alone",
                            "C": "On the combined total of the CIF value plus Customs Duty plus IDF and RDL levies",
                            "D": "On the profit margin the Kenyan importer hopes to earn after selling the items"
                        },
                        "correct_answer": "C",
                        "explanation": "Under the VAT Act and East African Community Customs Management Act, import VAT is charged on the compounded base value consisting of the Cost, Insurance, and Freight (CIF) value plus all statutory border import duties and levies."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary",
                    "title": "Lesson 4 Synthesis: Customs Duties & Border Tariffs",
                    "content": {
                        "text": "### Key Conceptual Takeaways\n\n1. **Nature of Customs Duties:** Taxes levied at borders (airports, seaports, overland posts) on imported or exported goods.\n2. **The 4 Strategic Drivers:**\n   - **Infant Industry Protection:** Shielding young domestic producers from being crushed by mature foreign multinationals.\n   - **Revenue Mobilization:** Generating hundreds of billions of shillings for the National Treasury at entry points like Mombasa Port.\n   - **Curbing Harmful Goods & Dumping:** Discouraging imports of hazardous goods, pollutants, and under-priced dumped products.\n   - **Foreign Exchange Conservation:** Reducing import demand to stabilize foreign exchange reserves (USD) and defend the Kenya Shilling.\n3. **Calculation Mechanics:** Import clearance involves compounded calculations where VAT applies to the full taxable sum of CIF + Customs Duty + IDF + RDL."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Tax Compliance and Ethical Issues in Public Finance
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Tax Compliance and Ethical Issues in Public Finance",
        "unit_description": "Ethics in public finance: Tax compliance vs. Tax avoidance vs. Tax evasion, citizen civic duties, government stewardship, Auditor-General oversight, and the social contract.",
        "lesson_title": "Tax Compliance and Ethical Issues in Public Finance",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Public Education Funding Impact in Kenya",
                    "content": {
                        "title": "Taxpayer Funded Public Education and School Facilities",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Jinsi_Kodi_ya_Serikali_Inavyotumiwa_%28how_Government_Tax_is_Used%29_Art.IWMPST15384.jpg",
                        "caption": "Historical public information illustration depicting how national tax revenues are utilized to fund public schools, hospitals, agricultural extension, and community social services across Kenya.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between Tax Compliance, Tax Avoidance (legal minimization), and Tax Evasion (illegal crime)\n- Explain the 'Leaky Bucket' analogy regarding public corruption, procurement fraud, and tax evasion\n- Analyze the civic responsibilities of citizens in paying taxes and exercising active budget oversight\n- Evaluate the constitutional institutions safeguarding public funds in Kenya (Auditor-General, Controller of Budget, Parliament)"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Tax Compliance, Avoidance, and Evasion",
                    "content": {
                        "term": "Compliance, Avoidance & Evasion",
                        "definition": "Tax Compliance is the degree to which taxpayers voluntarily adhere to tax legislation by registering, accurately declaring income, and remitting taxes on time. Tax Avoidance is the legal arrangement of financial affairs using allowable statutory exemptions, deductions, and reliefs to minimize tax liabilities. Tax Evasion is the deliberate, illegal non-payment or under-reporting of taxes through fraud, concealment of income, or falsification of records, which constitutes a serious criminal offense."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Leaky Bucket of Public Ethics & The Social Contract",
                    "content": {
                        "text": "Public finance integrity relies on a two-sided social contract:\n\n- **The Leaky Bucket Analogy:** Picture a village community carrying a bucket of water from a river to irrigate their shared crop field. If some villagers refuse to carry the bucket but expect to harvest crops, that is **Tax Evasion**. If the leaders carry the bucket but punch holes in the bottom so water leaks out to their private compounds, that is **Public Misappropriation (Corruption)**. For the village to thrive, everyone must contribute, and the bucket must be sealed!\n- **The Social Contract Equilibrium:** Citizens pay taxes willingly when they observe tangible value: tarmac roads, stocked hospitals, quality CBC schools, and reliable security. When public funds are squandered, public trust erodes, fueling tax resistance. Ethical governance and civic honesty are symbiotic."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Tax Ethics, Compliance and Public Accountability Contract",
                    "content": {
                        "title": "Taxpayer Behavioral Spectrum & Sovereign Stewardship Pillars",
                        "caption": "Vector SVG diagram illustrating the legal and ethical spectrum (Compliance, Avoidance, Evasion) alongside constitutional oversight institutions (Auditor-General, Controller of Budget, Parliament).",
                        "svg_content": SVG_TAX_ETHICS_AND_ACCOUNTABILITY
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Tax Avoidance vs. Tax Evasion Structural Comparison",
                    "content": {
                        "headers": ["Feature / Dimension", "Tax Avoidance", "Tax Evasion"],
                        "rows": [
                            ["Legal Status", "100% Legal; operates strictly within the letter of the law", "Illegal; a criminal offense under the Tax Procedures Act"],
                            ["Methodology Used", "Utilizing tax allowances, capital deductions, mortgage reliefs, and tax-free infrastructure bonds", "Concealing cash sales, inflating fictitious business expenses, running parallel account books, and smuggling"],
                            ["Ethical Perception", "Prudent financial planning, though aggressive schemes may face moral scrutiny", "Unethical, anti-social, and damages public social welfare"],
                            ["Legal Consequences", "None; accepted by KRA upon audit review", "Heavy fines (up to 200% penalty), seizure of assets, revocation of business licenses, and prison sentences"],
                            ["Kenyan Real-World Example", "A business purchasing machinery to claim 100% investment capital allowance", "A nightclub trader refusing to issue eTIMS electronic receipts to conceal sales from KRA"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Statutory Tax Avoidance via Allowable Pension and Insurance Reliefs",
                    "content": {
                        "intro": "Dr. Wanjala, a private medical practitioner in Kisumu, earns a gross annual taxable income of $\\text{KES } 3,600,000$. Under standard flat rate assessment without planning, his tax liability would be $30\\%$ of gross earnings ($\\text{KES } 1,080,000$). Working with a certified tax consultant, Dr. Wanjala implements three fully legal tax avoidance measures authorized under the Income Tax Act: \n1. Contributes the statutory maximum of $\\text{KES } 240,000\\text{ per year}$ to a registered retirement pension scheme (fully tax-deductible).\n2. Takes out a qualifying post-retirement medical health insurance cover paying annual premiums of $\\text{KES } 120,000$ (qualifying for a $15\\%$ insurance tax relief on premiums paid).\n3. Invests in a tax-exempt sovereign infrastructure bond paying $\\text{KES } 200,000$ interest (which is exempt from withholding tax). \nCalculate his new Taxable Income, Gross Tax Payable at $30\\%$, Net Tax Payable after applying Insurance Relief, and the Total Legally Saved Tax Amount.",
                        "steps": [
                            {
                                "step_number": 1,
                                "instruction": "Identify given financial parameters and statutory deductions.",
                                "math": "\\begin{aligned} \\text{Gross Annual Income } (Y) &= \\text{KES } 3,600,000 \\\\[4pt] \\text{Allowable Pension Deduction } (D_{\\text{pension}}) &= \\text{KES } 240,000 \\\\[4pt] \\text{Medical Insurance Premium } (P_{\\text{ins}}) &= \\text{KES } 120,000 \\quad (15\\% \\text{ tax relief}) \\\\[4pt] \\text{Tax Rate } (t) &= 30\\% = 0.30 \\end{aligned}"
                            },
                            {
                                "step_number": 2,
                                "instruction": "State the formulas for Adjusted Taxable Income ($Y_{\\text{adj}}$), Gross Tax ($T_{\\text{gross}}$), Insurance Tax Relief ($R_{\\text{ins}}$), and Net Tax Payable ($T_{\\text{net}}$).",
                                "math": "\\begin{aligned} Y_{\\text{adj}} &= Y - D_{\\text{pension}} \\\\[4pt] T_{\\text{gross}} &= Y_{\\text{adj}} \\times t \\\\[4pt] R_{\\text{ins}} &= P_{\\text{ins}} \\times 0.15 \\\\[4pt] T_{\\text{net}} &= T_{\\text{gross}} - R_{\\text{ins}} \\end{aligned}"
                            },
                            {
                                "step_number": 3,
                                "instruction": "Calculate Adjusted Taxable Income and Gross Tax Payable.",
                                "math": "\\begin{aligned} Y_{\\text{adj}} &= 3,600,000 - 240,000 = \\text{KES } 3,360,000 \\\\[6pt] T_{\\text{gross}} &= 3,360,000 \\times 0.30 = \\text{KES } 1,008,000 \\end{aligned}"
                            },
                            {
                                "step_number": 4,
                                "instruction": "Calculate Insurance Relief and Net Tax Payable.",
                                "math": "\\begin{aligned} R_{\\text{ins}} &= 120,000 \\times 0.15 = \\text{KES } 18,000 \\\\[6pt] T_{\\text{net}} &= 1,008,000 - 18,000 = \\mathbf{\\text{KES } 990,000} \\end{aligned}"
                            },
                            {
                                "step_number": 5,
                                "instruction": "Calculate Total Legally Saved Tax Amount compared to the unoptimized liability.",
                                "math": "\\begin{aligned} \\text{Unoptimized Tax} &= 3,600,000 \\times 0.30 = \\text{KES } 1,080,000 \\\\[4pt] \\text{Total Legal Tax Saved} &= 1,080,000 - 990,000 = \\mathbf{\\text{KES } 90,000} \\end{aligned}"
                            },
                            {
                                "step_number": 6,
                                "instruction": "Provide the economic interpretation and common analytical pitfall.",
                                "math": "\\begin{aligned} &\\textbf{Economic Interpretation:} \\\\ &\\text{By utilizing legal statutory pension deductions and insurance reliefs, Dr. Wanjala} \\\\ &\\text{reduces his tax liability by KES } 90,000 \\text{ completely legally. This is Tax Avoidance,} \\\\ &\\text{which encourages long-term retirement savings and healthcare stability.} \\\\[6pt] &\\textbf{Common Pitfall:} \\\\ &\\text{Confusing tax deductions (which reduce taxable income) with tax reliefs (which} \\\\ &\\text{directly subtract from the final tax payable). E.g., pension reduces } Y, \\text{ relief reduces } T. \\end{aligned}"
                            }
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "case_study",
                    "title": "Kenyan Enterprise Case Study: Office of the Auditor-General (OAG) & Public Accountability",
                    "content": {
                        "company_name": "Office of the Auditor-General (OAG Kenya)",
                        "industry": "Independent Constitutional Oversight & Public Financial Audit",
                        "summary": "Under Article 229 of the Constitution of Kenya, the Auditor-General audits and reports on the accounts of all 47 county governments, the national government, the judiciary, and parliament. Annual audit reports identify instances of pending bills, unapproved expenditures, stalled development projects, and revenue leakages. When citizens, civil society groups, and parliamentary committees (PAC and PIC) scrutinize these reports, they hold accounting officers accountable, compel restitution of stolen funds, and ensure that public taxes genuinely improve schools, hospitals, and local roads.",
                        "discussion_questions": [
                            "Why is the constitutional independence of the Office of the Auditor-General crucial for public financial accountability?",
                            "How does citizen participation in county budget public hearings reinforce ethical public finance?",
                            "What is the difference between an unspent budget allocation and misappropriated public funds?"
                        ]
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Tax Evasion vs Tax Avoidance & Ethical Public Finance",
                    "content": {
                        "title": "Tax Avoidance vs Tax Evasion: Legal and Ethical Distinctions",
                        "youtube_id": "r-6dJg1Wv3w",
                        "url": "https://www.youtube.com/watch?v=r-6dJg1Wv3w",
                        "description": "Clear explainer contrasting legal tax avoidance strategies (allowances, deductions) with illegal tax evasion schemes (fraud, concealment), highlighting the ethical imperative of public financial stewardship."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 1: Tax Avoidance vs Evasion Classification",
                    "content": {
                        "question": "A tea exporting company in Kericho invests in modern eco-friendly solar processing boilers. The Kenya Income Tax Act specifically allows companies to claim a 100% Capital Investment Allowance on such machinery, reducing the company's taxable profit and cutting its corporate tax bill by KES 4,000,000. How is this financial action classified?",
                        "options": {
                            "A": "Tax Evasion (Illegal criminal act)",
                            "B": "Tax Avoidance (Lawful tax minimization)",
                            "C": "Money Laundering (Illegal concealment)",
                            "D": "Bribery and Fraud (Illegal offense)"
                        },
                        "correct_answer": "B",
                        "explanation": "Because the company utilized allowances explicitly provided for in Kenyan tax legislation, its actions are 100% lawful. This is a classic example of Tax Avoidance, where the state uses tax incentives to promote desirable investments like renewable green energy."
                    }
                },
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 2: Constitutional Oversight Roles",
                    "content": {
                        "question": "Which independent constitutional office in Kenya is mandated to scrutinize government expenditure accounts after funds have been spent and table annual public audit reports before Parliament?",
                        "options": {
                            "A": "The Kenya Revenue Authority (KRA)",
                            "B": "The Office of the Auditor-General (OAG)",
                            "C": "The Central Bank of Kenya (CBK)",
                            "D": "The Capital Markets Authority (CMA)"
                        },
                        "correct_answer": "B",
                        "explanation": "The Office of the Auditor-General (OAG), established under Article 229 of the Constitution of Kenya, is the supreme independent audit institution responsible for reviewing whether public funds were spent lawfully, effectively, and transparently."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary",
                    "title": "Lesson 5 Synthesis: Ethics and Integrity in Public Finance",
                    "content": {
                        "text": "### Key Conceptual Takeaways\n\n1. **Avoidance vs. Evasion Distinction:**\n   - **Tax Avoidance:** Lawful financial structuring taking advantage of statutory deductions, tax reliefs, and incentives.\n   - **Tax Evasion:** Criminal intentional non-payment, income concealment, or falsification of books punishable by heavy fines and imprisonment.\n2. **The Social Contract Equilibrium:** A prosperous state requires a dual commitment: citizens faithfully register, file returns, and pay taxes; while the government stewards funds transparently to deliver high-quality public services.\n3. **Institutional Accountability Pillars:** Constitutional bodies including the Office of the Auditor-General (OAG), the Controller of Budget (OCOB), and Parliamentary Oversight Committees ensure that public taxes are protected from misappropriation."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Practical Calculations of Tax and Budget Balance
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Practical Calculations of Tax and Budget Balance",
        "unit_description": "Comprehensive practical computation of VAT, excise duties, customs tariffs, fiscal budget surplus/deficit equations, and debt sustainability analysis.",
        "lesson_title": "Practical Calculations of Tax and Budget Balance",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "City Hall and National Treasury in Nairobi",
                    "content": {
                        "title": "Government Financial Administration in Nairobi",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/Nairobi_showing_KICC_Times_Tower_and_City_Hall.jpg",
                        "caption": "Panoramic skyline of Nairobi showing City Hall, Times Tower, and the National Treasury, the nerve centers where national and county fiscal budgets are formulated, balanced, and executed.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Calculate Value Added Tax (VAT) amounts, Net Prices, and Gross Selling Prices with precision\n- Compute compound customs import duties and clear multi-tiered commercial cargo transactions\n- Calculate total government revenues, total expenditures, and determine Budget Surpluses or Budget Deficits\n- Analyze the three primary channels governments use to finance fiscal deficits (Domestic Debt, External Debt, Fiscal Reforms)"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Fiscal Budget Balance & Deficits",
                    "content": {
                        "term": "Budget Balance & Deficit",
                        "definition": "The National Budget Balance is the mathematical difference between total sovereign revenue collected and total government expenditures over a financial year: $\\text{Budget Balance} = \\text{Total Revenue} - \\text{Total Expenditure}$. When revenue exceeds expenditure, a Budget Surplus exists; when expenditure exceeds revenue, a Budget Deficit occurs, creating a financing gap that requires borrowing or debt issuance."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Mathematical Mechanics of Public Finance",
                    "content": {
                        "text": "Mathematical modeling of public finance covers two primary analytical areas:\n\n- **Microeconomic Tax Calculations:** Everyday business calculations including Net-to-Gross VAT pricing ($P_{\\text{gross}} = P_{\\text{net}} \\times (1 + r_{\\text{vat}})$), extracting VAT from gross inclusive amounts ($T_{\\text{vat}} = P_{\\text{gross}} \\times \\frac{r_{\\text{vat}}}{1 + r_{\\text{vat}}}$), and compounding border tariffs (CIF + Duty + Levies + VAT).\n- **Macroeconomic Fiscal Budget Equations:** Balancing national and county revenue pools ($R = \\text{Taxes} + \\text{Non-Tax Fees} + \\text{Grants}$) against expenditure commitments ($G = E_{\\text{recurrent}} + E_{\\text{development}}$) to determine the sovereign fiscal deficit and debt sustainability."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "National Budget Balance and Deficit Financing Anatomy",
                    "content": {
                        "title": "Budget Balance Dynamics & Deficit Financing Channels",
                        "caption": "Vector SVG diagram illustrating the mathematical states of a government budget (Surplus, Balanced, Deficit) and the structural channels used to finance fiscal deficits.",
                        "svg_content": SVG_BUDGET_BALANCE_AND_DEFICIT_FINANCING
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Deficit Financing Channels Comparative Matrix",
                    "content": {
                        "headers": ["Financing Channel", "Mechanisms & Instruments", "Primary Advantages", "Inherent Macroeconomic Risks"],
                        "rows": [
                            ["Domestic Debt Market", "Issuing Treasury Bills (91, 182, 364-day tenors) and Treasury Bonds (2 to 25 years) to local banks and citizens", "Denominated in KES; zero foreign currency exchange risk; stimulates domestic capital markets", "Can crowd out private sector borrowing if commercial banks prefer lending to government rather than SMEs."],
                            ["External Concessional Borrowing", "Low-interest loans from multilateral institutions (World Bank, IMF, African Development Bank)", "Very low interest rates (e.g., 1-2%), long repayment tenors (20-40 years), and multi-year grace periods", "Often comes with strict macroeconomic conditionalities and policy reform requirements."],
                            ["External Commercial Debt (Eurobonds)", "Issuing sovereign sovereign bonds on international capital markets in foreign currencies (USD, Euros)", "Access to massive capital sums quickly without domestic banking liquidity constraints", "Subject to foreign exchange volatility: if the KES depreciates against USD, debt service costs escalate rapidly."],
                            ["Domestic Fiscal Reforms & Discipline", "Expanding tax base through eTIMS, rationalizing public spending, cutting non-essential recurrent waste", "Permanently closes the fiscal deficit without adding debt liabilities or future interest payments", "Spending cuts or new tax levies may encounter short-term public resistance and political friction."]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Comprehensive National Fiscal Deficit and Financing Plan",
                    "content": {
                        "intro": "The National Treasury of Kenya compiles its fiscal projections for the upcoming Financial Year. \n\n**1. Projected Revenue Inflows:**\n- Direct Income Taxes (PAYE and Corporate Tax) = $\\text{KES } 1.20\\text{ Trillion}$\n- Value Added Tax (VAT) = $\\text{KES } 650\\text{ Billion}$\n- Excise Duties = $\\text{KES } 300\\text{ Billion}$\n- Customs and Import Duties = $\\text{KES } 180\\text{ Billion}$\n- Non-Tax Fees and Commercial Dividends = $\\text{KES } 120\\text{ Billion}$\n\n**2. Planned Expenditure Outflows:**\n- Recurrent Expenditure (Civil Service Salaries, Pensions, Office Operations) = $\\text{KES } 1.85\\text{ Trillion}$\n- Consolidated Fund Services (Public Debt Interest Payments) = $\\text{KES } 600\\text{ Billion}$\n- Capital Development Expenditure (Highways, CBC Schools, Dams, Energy Grid) = $\\text{KES } 800\\text{ Billion}$\n\nCalculate the Total Sovereign Revenue ($R_{\\text{total}}$), Total Government Expenditure ($G_{\\text{total}}$), determine the Fiscal Budget Balance, and outline the Deficit Financing Gap assuming the government plans to finance $60\\%$ of the deficit through domestic borrowing and $40\\%$ through external concessional loans.",
                        "steps": [
                            {
                                "step_number": 1,
                                "instruction": "Sum all projected sovereign revenue streams to obtain $R_{\\text{total}}$.",
                                "math": "\\begin{aligned} R_{\\text{total}} &= 1,200\\text{B (Direct)} + 650\\text{B (VAT)} + 300\\text{B (Excise)} + 180\\text{B (Customs)} + 120\\text{B (Non-Tax)} \\\\[6pt] R_{\\text{total}} &= \\text{KES } 2,450\\text{ Billion} = \\mathbf{\\text{KES } 2.45\\text{ Trillion}} \\end{aligned}"
                            },
                            {
                                "step_number": 2,
                                "instruction": "Sum all planned expenditure allocations to obtain $G_{\\text{total}}$.",
                                "math": "\\begin{aligned} G_{\\text{total}} &= 1,850\\text{B (Recurrent)} + 600\\text{B (Debt Interest)} + 800\\text{B (Development)} \\\\[6pt] G_{\\text{total}} &= \\text{KES } 3,250\\text{ Billion} = \\mathbf{\\text{KES } 3.25\\text{ Trillion}} \\end{aligned}"
                            },
                            {
                                "step_number": 3,
                                "instruction": "Calculate the Fiscal Budget Balance ($B_{\\text{budget}}$).",
                                "math": "\\begin{aligned} B_{\\text{budget}} &= R_{\\text{total}} - G_{\\text{total}} \\\\[4pt] B_{\\text{budget}} &= 2.45\\text{ Trillion} - 3.25\\text{ Trillion} = -\\text{KES } 0.80\\text{ Trillion} \\\\[6pt] \\text{Deficit Financing Gap } (D) &= \\mathbf{\\text{KES } 800\\text{ Billion (Fiscal Deficit)}} \\end{aligned}"
                            },
                            {
                                "step_number": 4,
                                "instruction": "Calculate the Domestic Borrowing Allocation ($60\\%$ of Deficit).",
                                "math": "\\begin{aligned} \\text{Domestic Debt Target} &= 800\\text{ Billion} \\times 0.60 = \\mathbf{\\text{KES } 480\\text{ Billion}} \\\\ &\\text{(Raised via Treasury Bills and Treasury Bonds)} \\end{aligned}"
                            },
                            {
                                "step_number": 5,
                                "instruction": "Calculate the External Concessional Borrowing Allocation ($40\\%$ of Deficit).",
                                "math": "\\begin{aligned} \\text{External Concessional Target} &= 800\\text{ Billion} \\times 0.40 = \\mathbf{\\text{KES } 320\\text{ Billion}} \\\\ &\\text{(Raised via World Bank, IMF, and AfDB facility loans)} \\end{aligned}"
                            },
                            {
                                "step_number": 6,
                                "instruction": "Provide the economic interpretation and common analytical pitfall.",
                                "math": "\\begin{aligned} &\\textbf{Economic Interpretation:} \\\\ &\\text{The government runs a fiscal deficit of KES } 800\\text{B (representing } 24.62\\% \\text{ of its} \\\\ &\\text{total budget). By splitting borrowing 60:40 between domestic bonds and concessional} \\\\ &\\text{loans, the National Treasury bridges the infrastructure gap while managing FX risk.} \\\\[6pt] &\\textbf{Common Pitfall:} \\\\ &\\text{Counting borrowed debt loans as regular tax revenues in step 1. Borrowing is a} \\\\ &\\text{financing mechanism for the deficit, not sovereign revenue earned!} \\end{aligned}"
                            }
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "case_study",
                    "title": "Kenyan Enterprise Case Study: M-Akiba and Treasury Infrastructure Bonds",
                    "content": {
                        "company_name": "Central Bank of Kenya (CBK) & The National Treasury",
                        "industry": "Sovereign Debt Issuance & Retail Capital Markets",
                        "summary": "To finance national development deficits without relying exclusively on expensive foreign commercial loans, the National Treasury and the Central Bank of Kenya launched innovative domestic debt instruments like tax-free Infrastructure Bonds (IFBs) and the mobile-phone-based M-Akiba retail bond. M-Akiba allowed ordinary Kenyan citizens to lend money to the government starting from as little as KES 3,000 using M-Pesa. Meanwhile, long-term Infrastructure Bonds attract hundreds of billions from local pension funds and insurance companies. This provides non-inflationary financing for national roads, ports, and energy grids while paying attractive, guaranteed interest returns directly back to Kenyan citizens.",
                        "discussion_questions": [
                            "Why are sovereign Infrastructure Bonds issued with tax-free interest status in Kenya?",
                            "How does borrowing from domestic citizens through M-Akiba differ from borrowing in USD via Eurobonds?",
                            "What role does the Central Bank of Kenya play as the fiscal agent of the National Treasury?"
                        ]
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Government Budget Deficits, Debt and Fiscal Policy",
                    "content": {
                        "title": "Budget Deficits, National Debt and Fiscal Policy Explained",
                        "youtube_id": "3sTC3BmVWng",
                        "url": "https://www.youtube.com/watch?v=3sTC3BmVWng",
                        "description": "Comprehensive economics tutorial explaining how government budget balances work, why fiscal deficits happen, and how nations manage public debt sustainability."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 1: Extracting Net Price from VAT-Inclusive Price",
                    "content": {
                        "question": "A student in Nakuru buys a commercial scientific calculator for school at a supermarket for a total VAT-inclusive retail price of KES 2,320. If the standard rate of VAT is 16%, what was the original Net Price of the calculator before tax was added?",
                        "options": {
                            "A": "KES 1,948.80",
                            "B": "KES 2,000.00",
                            "C": "KES 1,856.00",
                            "D": "KES 2,120.00"
                        },
                        "correct_answer": "B",
                        "explanation": "Since $\\text{Gross Price} = \\text{Net Price} \\times 1.16$, we find the Net Price by dividing: $\\text{Net Price} = \\frac{\\text{KES } 2,320}{1.16} = \\text{KES } 2,000.00$. (The VAT amount included is KES 320.00)."
                    }
                },
                {
                    "type": "multiple_choice_question",
                    "title": "Formative Assessment Question 2: Deficit Financing Classification",
                    "content": {
                        "question": "When a country's total annual budget expenditure exceeds its total collected tax revenues, creating a fiscal budget deficit, which of the following is considered a sustainable domestic method for bridging this deficit?",
                        "options": {
                            "A": "Canceling all public secondary school education across the country",
                            "B": "Issuing long-term Treasury Infrastructure Bonds to local institutional and retail investors",
                            "C": "Printing paper currency uncontrollably without economic asset backing",
                            "D": "Refusing to service past sovereign debt obligations"
                        },
                        "correct_answer": "B",
                        "explanation": "Issuing domestic Treasury Bonds mobilizes idle domestic savings into productive capital investments without causing exchange rate risk or runaway inflation."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary",
                    "title": "Lesson 6 Synthesis: Practical Public Finance & Budget Calculus",
                    "content": {
                        "text": "### Key Conceptual Takeaways\n\n1. **Core Tax Formulas:**\n   - $\\text{Gross Price} = \\text{Net Price} \\times (1 + r_{\\text{vat}})$\n   - $\\text{Net Price} = \\frac{\\text{Gross Price}}{1 + r_{\\text{vat}}}$\n   - $\\text{VAT Amount} = \\text{Net Price} \\times r_{\\text{vat}} = \\text{Gross Price} \\times \\left(\\frac{r_{\\text{vat}}}{1 + r_{\\text{vat}}}\\right)$\n2. **The Sovereign Budget Balance Equation:**\n   $$\\text{Budget Balance} = \\text{Total Revenue } (R) - \\text{Total Expenditure } (G)$$\n   - $R > G \\implies \\textbf{Surplus}$ (excess savings, debt retirement).\n   - $R = G \\implies \\textbf{Balanced}$ (exact equilibrium).\n   - $R < G \\implies \\textbf{Deficit}$ (financing gap requires borrowing).\n3. **Prudent Debt Management:** Fiscal deficits must be channeled into high-return **Development Expenditures** (infrastructure, dams, energy) that expand future GDP, rather than being consumed by recurrent administrative overheads."
                    }
                }
            ]
        ]
    }
]
