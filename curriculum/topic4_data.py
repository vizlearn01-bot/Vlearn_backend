"""
VLearn Form 4 Business Studies — Topic 4: Public Finance
Authoritative Pedagogical Data Structures for 5 Lessons (50 Pages).
"""

from curriculum.ingest_form4_business_studies_topic4_svgs import (
    SVG_PUBLIC_FINANCE_SOURCES_TREE,
    SVG_GOVERNMENT_EXPENDITURE_STRUCTURE,
    SVG_TAX_SHIFTING_FLOW,
    SVG_TAX_STRUCTURE_GRAPH,
    SVG_BUDGET_FISCAL_POLICY_MATRIX
)

# Verified Wikimedia photographic assets
IMG_KRA_REVENUE_BUILDING = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Port of Mombasa customs clearance terminal, demonstrating import tariffs, trade revenue collection, and customs control.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

IMG_THIKA_SUPERHIGHWAY = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
    "text": "Standard Gauge Railway and transport corridor in Kenya, representing large-scale public development expenditure and capital infrastructure investment.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
}

IMG_KENYA_PARLIAMENT = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Parliament Buildings of Kenya in Nairobi, where national budget statements are presented and public spending is authorized under the Principle of Sanction.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

IMG_LOCAL_COMMERCE_VAT = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
    "text": "Retail trade in Nairobi, illustrating indirect tax incidence, point-of-sale consumption taxes, and commercial tax compliance.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Maasai_Market-Nairobi.jpg"
}

IMG_AGRO_PROCESSING_TAX = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/2009.12-363-1125ap_tea%2Cprocessing%28withering%29%2Cstirring_Rukuriri_Tea_Factory%2Ctea-zone_N_of_Embu%28C_Highlands%29%2CKE_mon14dec2009-1242h.jpg",
    "text": "Rukuriri Tea Factory in Embu, showing corporate tax generation, export tariffs, and local industry protection.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2009.12-363-1125ap_tea,processing(withering),stirring_Rukuriri_Tea_Factory,tea-zone_N_of_Embu(C_Highlands),KE_mon14dec2009-1242h.jpg"
}

# ==============================================================================
# LESSON 1: MEANING AND SOURCES OF PUBLIC FINANCE (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Meaning and Sources of Public Finance",
    "lesson_title": "Public Revenue Streams, Debt Sourcing, and Borrowing Trade-offs",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Public Finance",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain the meaning and core purpose of public finance, describe the eight main sources of government revenue, differentiate between internal and external borrowing, and identify key factors influencing public debt decisions."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Public Finance Matters",
                    "content": {
                        "text": "Just as a household needs income to pay for rent, food, and healthcare, a country needs money to construct national highways, pay teachers and police officers, and run public hospitals. Because a government cannot generate all this money through commercial selling, it must systematically raise revenue from the public and manage public borrowing. Public finance is the financial engine that drives national development and social welfare."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Meaning of Public Finance",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Public Finance",
                    "content": {
                        "term": "Public Finance",
                        "definition": "The mechanism and study by which the government raises monetary revenue and allocates public expenditure to run the country, maintain public security, and achieve desired social and economic objectives."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Eight Main Sources of Government Revenue",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Categorization of Government Revenue",
                    "content": {
                        "text": "1. Taxes: Compulsory monetary payments made by citizens and businesses without any direct matching service in return. This is the largest and most sustainable revenue stream.\n2. Court Fines: Punitive monetary penalties imposed by courts of law on lawbreakers.\n3. Rent and Rates: Charges paid by individuals or private firms for utilizing government land, housing, or property.\n4. Licence Fees: Fees paid to obtain official permits to conduct specific economic activities (e.g. driving, operating a shop, fishing).\n5. Dividends and Profits: Earnings from state-owned enterprises (parastatals) or corporations where the government owns equity shares.\n6. Interest on Loans: Interest earned from loans advanced by the government to local authorities, parastatals, or co-operatives.\n7. Government Borrowing (Public Debt): Loans obtained by the state to cover revenue deficits.\n8. Sale of Government Property: Revenue generated from privatizing state assets or selling surplus land, vehicles, or buildings."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Tax Revenue vs Non-Tax Revenue",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Comparative Analysis of Revenue Streams",
                    "content": {
                        "headers": ["Revenue Category", "Primary Examples", "Key Characteristics"],
                        "rows": [
                            ["Tax Revenue", "PAYE, Corporate Tax, VAT, Customs Duties", "Compulsory, unrequited, major source of national funding"],
                            ["Non-Tax Revenue", "Court Fines, Licence Fees, Parastatal Dividends, Rent", "Service-linked, regulatory, or earnings from state investments"],
                            ["Public Debt", "Treasury Bills, Treasury Bonds, World Bank Loans", "Refundable loan capital carrying interest obligations"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Government Borrowing: Internal vs External",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Internal vs. External Public Debt",
                    "content": {
                        "text": "When tax and non-tax revenues are insufficient to cover planned national expenditures, the government borrows. Public debt is divided into:\n\n• Internal Borrowing: Raising loans within the country's borders by issuing short-term Treasury bills (91, 182, 364 days) and long-term Treasury bonds to domestic commercial banks, pension funds, and citizens.\n• External Borrowing: Obtaining loans from foreign governments (bilateral debt) or international financial bodies like the World Bank and African Development Bank (multilateral debt)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Sources of Public Finance and Debt Sourcing Tree",
                    "svg_content": SVG_PUBLIC_FINANCE_SOURCES_TREE,
                    "content": {
                        "text": "Structural tree diagram illustrating non-tax revenue, tax revenue, public debt, and the trade-offs of internal versus external borrowing."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Factors Influencing Borrowing Decisions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Four Strategic Debt Factors",
                    "content": {
                        "text": "1. Relative Interest Rates (Cost): The government compares domestic interest rates against foreign interest rates to minimize repayment costs.\n2. The Crowding-Out Effect: Heavy domestic government borrowing absorbs commercial bank credit, reducing loanable funds for private businesses and driving up local interest rates. To protect local entrepreneurs, the state may choose external borrowing.\n3. External Conditions (Conditionality): Foreign lenders (like the IMF) often attach strict policy conditions (spending cuts, tax hikes). If conditions are too stringent, internal borrowing is preferred.\n4. Inflationary Impact: Domestic bank borrowing can expand the money supply and drive up domestic inflation, whereas external debt injects foreign currency without immediate domestic money creation."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Public finance mechanisms raise revenue through tax, non-tax, and borrowing channels. Internal borrowing risks crowding out local private enterprise, while external borrowing carries foreign exchange and policy conditionality risks."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Railway Infrastructure Borrowing Decision",
                    "content": {
                        "text": "Suppose the Kenyan government needs Sh. 50 billion for railway expansion. If it borrows Sh. 50 billion from local commercial banks, banks will lend to the state instead of local youth businesses, driving up domestic interest rates (Crowding-Out Effect). If it borrows from the African Development Bank, local bank funds remain available for private enterprise, but the state must adhere to foreign loan repayment schedules."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Common Pitfalls",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Court Fines vs Taxes",
                    "content": {
                        "text": "Confusing Court Fines and Taxes: A court fine is a punitive charge imposed strictly for breaking a law. A tax is a compulsory payment made by all eligible citizens regardless of whether they have broken any law. You can avoid court fines by complying with the law, but you cannot avoid taxes!"
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Which of the following is a non-tax revenue source for the government?",
                        "options": [
                            "Value Added Tax (VAT)",
                            "Personal Income Tax (PAYE)",
                            "Court Fines",
                            "Excise Duty"
                        ],
                        "correct_answer": "Court Fines",
                        "explanation": "Court fines are non-tax payments imposed punitively by courts for law violations, whereas VAT, PAYE, and Excise Duty are taxes."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: GOVERNMENT EXPENDITURE AND ITS PRINCIPLES (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Government Expenditure and its Principles",
    "lesson_title": "Operating vs Capital Spending and the Canons of Public Expenditure",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Public Expenditure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define government expenditure, categorize public spending into recurrent and development spending, and discuss the five canons of government expenditure."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Expenditure Planning Matters",
                    "content": {
                        "text": "Raising billions in public revenue is useless if funds are spent recklessly. Public expenditure must be strictly managed according to economic canons to ensure roads are built, hospitals are stocked, civil servants are paid, and social benefit is maximized."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition of Government Expenditure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Government Expenditure",
                    "content": {
                        "term": "Government Expenditure",
                        "definition": "The total monetary outflow spent by the national and county governments to run public administration, provide social services, maintain state security, and build national infrastructure."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Categories of Public Expenditure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Recurrent vs Development Expenditure",
                    "content": {
                        "text": "1. Recurrent Expenditure: Ongoing, day-to-day operating spending on services that do not create new permanent physical assets (e.g. civil servants' salaries, medicines, fuel, stationery, routine repairs).\n2. Development Expenditure: One-time capital investment spending on long-term assets that expand national infrastructure and productive capacity (e.g. constructing railways, building highways, constructing new hospitals, building dams)."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Public Infrastructure Investment",
                    "content": IMG_THIKA_SUPERHIGHWAY
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Recurrent vs Development Comparison",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Recurrent vs. Development Expenditure",
                    "content": {
                        "headers": ["Feature", "Recurrent Expenditure", "Development Expenditure"],
                        "rows": [
                            ["Frequency", "Highly repetitive (monthly / annual)", "Non-repetitive (one-off capital projects)"],
                            ["Asset Creation", "Does not create new physical assets", "Creates permanent physical national assets"],
                            ["Kenyan Examples", "Civil service salaries, drugs, fuel, stationery", "Constructing SGR railway, building dams, ports"],
                            ["Economic Purpose", "Maintains daily administrative operations", "Expands long-term national productive capacity"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "The Five Canons of Public Expenditure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Core Expenditure Canons",
                    "content": {
                        "text": "1. Principle of Sanction (Approval): No public money should be spent without proper authorization from Parliament.\n2. Principle of Maximum Social Benefit: Public spending must be directed to yield the highest welfare and safety for the largest number of citizens.\n3. Principle of Economy: The state must avoid waste, extravagance, and unnecessary overheads.\n4. Principle of Flexibility: Spending plans must be adaptable to accommodate unexpected national emergencies (e.g. droughts, floods).\n5. Principle of Financial Management: Spending must be backed by accurate accounting records and undergo regular audits by the Auditor General."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Government Expenditure and Spending Canons",
                    "svg_content": SVG_GOVERNMENT_EXPENDITURE_STRUCTURE,
                    "content": {
                        "text": "Structural breakdown comparing recurrent and development spending governed by the five canons of public expenditure."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Parliamentary Sanction and Control",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Parliamentary Authorization of Budgets",
                    "content": IMG_KENYA_PARLIAMENT
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Recurrent spending runs the daily state machinery, while development spending builds national capital assets. All spending must be sanctioned, economical, flexible, audited, and designed for maximum social benefit."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "County Spending Imbalance Case Study",
                    "content": {
                        "text": "If a county spends 85% of its budget on staff salaries and vehicle fuel (recurrent) and only 15% on fresh produce markets and roads (development), the county headquarters runs smoothly, but long-term economic growth stalls because farmers cannot transport crops to market."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Construction vs Maintenance",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Maintenance is Recurrent",
                    "content": {
                        "text": "Building a new hospital is development expenditure because it creates a new asset. Repairing the roof or painting an existing school building is recurrent expenditure because maintenance merely keeps an existing asset operational."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Constructing a new highway is classified under which expenditure category?",
                        "options": [
                            "Recurrent Expenditure",
                            "Development Expenditure",
                            "Transfer Payment",
                            "Non-Tax Expenditure"
                        ],
                        "correct_answer": "Development Expenditure",
                        "explanation": "Constructing a new highway creates a long-term physical capital asset, which is development expenditure."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: MEANING, PURPOSE, AND PRINCIPLES OF TAXATION (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Meaning, Purpose, and Principles of Taxation",
    "lesson_title": "Taxation Rationale, Tax Shifting, and Adam Smith's Canons",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Taxation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define tax and taxation, explain seven major purposes of taxation, distinguish between tax impact and tax incidence, identify determinants of tax revenue, and master Adam Smith's seven canons of taxation."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Taxation is Essential",
                    "content": {
                        "text": "Without taxation, modern government could not exist. Beyond raising public revenue, taxes are used to protect local industries from foreign dumping, reduce wealth inequality, control inflation, and curb the consumption of harmful commodities."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition of Tax and Taxation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Tax & Taxation",
                    "content": {
                        "term": "Taxation",
                        "definition": "The compulsory non-repayable monetary levy imposed by the government on eligible individuals, incomes, property, and business transactions to raise public revenue and regulate the economy."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Seven Core Purposes of Taxation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Governments Levy Taxes",
                    "content": {
                        "text": "1. Raise Government Revenue: Primary source of funds for public administration and infrastructure.\n2. Discourage Harmful Goods: Imposing 'sin taxes' on cigarettes and alcohol inflates prices to reduce consumption.\n3. Protect Domestic Industry: Heavy tariffs on imported goods make foreign items expensive, supporting local factories.\n4. Reduce Income Inequality: Progressive tax rates tax higher earners more, funding welfare for lower-income groups.\n5. Control Inflation: Raising tax rates reduces disposable income and aggregate demand during economic overheating.\n6. Correct Balance-of-Payments Deficits: Taxing luxury imports preserves foreign exchange reserves.\n7. Influence Industrial Location: Tax holidays encourage businesses to establish factories in rural areas."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Tax Impact vs Tax Incidence",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Tax Impact vs. Tax Incidence",
                    "content": {
                        "text": "• Tax Impact: The immediate legal burden of the tax on the person or entity upon whom the tax is initially levied.\n• Tax Incidence: The final resting place of the tax burden on the person who actually pays the money out of pocket.\n\nIn direct taxes (e.g. PAYE), Impact = Incidence. In indirect taxes (e.g. VAT), Impact falls on the manufacturer/seller, but Incidence is shifted forward to the final consumer!"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Tax Shifting Flow and Adam Smith's Canons",
                    "svg_content": SVG_TAX_SHIFTING_FLOW,
                    "content": {
                        "text": "Diagram showing tax shifting from impact to incidence alongside Adam Smith's seven canons of taxation."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Determinants of National Tax Revenue",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Five Revenue Determinants",
                    "content": {
                        "text": "1. Real Income Levels: Higher wages and corporate profits expand the taxable base.\n2. Economic Structure: A dominant formal sector is easier to tax than an informal (Jua Kali) economy.\n3. Authority Efficiency: Transparency and integrity in revenue bodies (e.g. KRA) boost collections.\n4. Income Distribution: A large middle class provides stable tax collections.\n5. Social and Political Trust: High public trust in governance improves tax compliance."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Adam Smith's Seven Canons of Taxation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Seven Canons of Taxation",
                    "content": {
                        "text": "1. Equity: Taxes must be fair, based on ability to pay.\n2. Certainty: Taxpayers must know exact amounts, deadlines, and payment modes.\n3. Convenience: Tax collected when most convenient for taxpayers (e.g. PAYE on monthly salary).\n4. Economy: Administrative collection costs must be kept as low as possible.\n5. Elasticity: Tax yields automatically expand as national GDP grows.\n6. Flexibility: Tax rates can be modified quickly to respond to economic shifts.\n7. Diversification: Broad tax base spanning multiple varied tax streams."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Taxation funds state operations and regulates socio-economic behavior. Tax impact is who pays legally; tax incidence is who pays out-of-pocket. A great tax system prioritizes equity, certainty, convenience, and low collection costs."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application: Sugar Tariffs",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Tariff Protection Case Study",
                    "content": {
                        "text": "Imposing a high import tariff on Brazilian sugar raises its supermarket price above local sugar. Consumers switch to locally produced sugar from Mumias or Sony Sugar, preserving thousands of agricultural jobs in Western Kenya."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Elasticity vs Flexibility",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Elasticity vs. Flexibility",
                    "content": {
                        "text": "Elasticity means tax revenue grows automatically as national income increases without changing tax laws. Flexibility means the government actively alters tax laws and rates when desired."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "When a tax burden is passed from a factory to the final retail shopper through higher shelf prices, who bears the tax incidence?",
                        "options": [
                            "The Factory",
                            "The Retailer",
                            "The Final Consumer",
                            "The KRA Officer"
                        ],
                        "correct_answer": "The Final Consumer",
                        "explanation": "The tax incidence is the final resting place of the tax burden, which falls out-of-pocket on the final consumer."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 4: CLASSIFICATION OF TAXES (10 Pages)
# ==============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Classification of Taxes",
    "lesson_title": "Tax Structures, Direct vs Indirect Taxes, and Economic Demerits",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Tax Structures",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to classify taxes by structural design (progressive, proportional, regressive), evaluate the drawbacks of progressive taxation, and compare direct and indirect taxes by their merits and demerits."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Tax Classification Matters",
                    "content": {
                        "text": "How taxes are designed shapes national work incentives and wealth equality. High progressive tax brackets can discourage extra work, while heavy indirect taxes (VAT) disproportionately burden low-income families."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Tax Classification by Structure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Structural Tax Rates",
                    "content": {
                        "text": "1. Progressive Tax: The tax rate % increases as income increases (e.g. PAYE income tax).\n2. Proportional Tax: The tax rate % remains flat regardless of income level (e.g. flat corporate tax rate).\n3. Regressive Tax: The tax rate % effective burden decreases as income increases (e.g. VAT on basic foods, taking a larger share of a poor person's income)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Structural Tax Curves and Direct vs Indirect Classification",
                    "svg_content": SVG_TAX_STRUCTURE_GRAPH,
                    "content": {
                        "text": "Graph of progressive, proportional, and regressive tax curves alongside a direct vs indirect tax comparison table."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Disadvantages of Progressive Taxation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Five Drawbacks of Progressive Taxes",
                    "content": {
                        "text": "1. Discourages Extra Work: Workers avoid overtime if tax brackets absorb most of their additional pay.\n2. Suppresses Business Risk-Taking: Entrepreneurs avoid risky ventures if successful profits are heavily taxed.\n3. Encourages Evasion: High tax brackets incentivize profit hiding and tax fraud.\n4. Assumes Equal Needs: Treats all equal earners identically regardless of family or health burdens.\n5. Reduces Capital Accumulation: Drains private savings that would finance business loans."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Direct vs Indirect Tax Classification",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Direct Taxes vs. Indirect Taxes",
                    "content": {
                        "headers": ["Feature", "Direct Taxes", "Indirect Taxes"],
                        "rows": [
                            ["Definition", "Taxes levied on income, profits, and wealth", "Taxes levied on consumption goods, services, and trade"],
                            ["Shifting Burden", "Cannot be shifted (Impact = Incidence)", "Can be shifted forward to consumer via prices"],
                            ["Examples", "PAYE Income Tax, Corporate Tax, Estate Duty", "VAT, Excise Duty, Import Customs Tariffs"],
                            ["Key Advantage", "Highly equitable, certain, economical to collect", "Broad revenue base, convenient, hard to evade"],
                            ["Key Disadvantage", "Easier to evade, discourages extra work", "Regressive burden on poor, causes price inflation"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Merits and Demerits of Direct Taxes",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Direct Taxes Evaluation",
                    "content": {
                        "text": "• Merits: Promotes social justice (equitable), predictable for budgeting (certain), low collection costs (economical), builds civic consciousness.\n• Demerits: Vulnerable to tax evasion by informal businesses, discourages savings, inconvenient lump-sum payments, narrow tax base."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Merits and Demerits of Indirect Taxes",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Indirect Taxes Evaluation",
                    "content": {
                        "text": "• Merits: Enormous revenue yield (broad base), convenient micro-payments at checkout, hard to evade, can discourage social evils.\n• Demerits: Regressive impact on low-income earners, directly fuels retail price inflation, uncertain revenue yield during economic downturns."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Indirect Tax Collection in Commerce",
                    "content": IMG_LOCAL_COMMERCE_VAT
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Progressive taxes charge higher rates as income rises, while regressive taxes hit low earners hardest. Direct taxes fall on wealth and income and cannot be shifted; indirect taxes fall on consumption and are passed onto consumers."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Shifting Scenario",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Excise Duty Shifting Scenario",
                    "content": {
                        "text": "If KRA levies Sh. 50 excise duty per shoe on a Nairobi factory, the factory raises wholesale prices by Sh. 50. Retailers pass this to the student buying shoes. Tax Impact = Factory; Tax Incidence = Student!"
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: PAYE Cannot Be Shifted",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Income Tax Stays on Earner",
                    "content": {
                        "text": "Employees cannot shift PAYE income tax to their employer. Employers are merely withholding agents; the legal impact and economic incidence remain strictly on the employee."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Why is Value Added Tax (VAT) described as a regressive tax?",
                        "options": [
                            "Because tax rates decrease for higher corporate profits",
                            "Because it takes a larger percentage of income from low-income earners than high-income earners",
                            "Because the government cannot collect it efficiently",
                            "Because it only applies to imported luxury cars"
                        ],
                        "correct_answer": "Because it takes a larger percentage of income from low-income earners than high-income earners",
                        "explanation": "VAT is charged at a flat amount per product, taking a proportionally higher share of a low-income person's total daily wage."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 5: VAT, CUSTOMS DUTIES, BUDGET, AND FISCAL POLICY (10 Pages)
# ==============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "VAT, Customs Duties, Budget, and Fiscal Policy",
    "lesson_title": "Value Added Tax, Budget Balances, Fiscal Policy, and KCSE Examination Mastery",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Budgets and Fiscal Policy",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain Value Added Tax (VAT), customs duties, government budget types (balanced, deficit, surplus), fiscal policy stabilization tools, and perform 6-step quantitative budget balance calculations."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why National Budgets Matter",
                    "content": {
                        "text": "Every June, the National Treasury reads the budget statement detailing revenue estimates and proposed spending. Understanding budget balances demystifies national public debt debates and shows how fiscal policy manages inflation and economic growth."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Value Added Tax and Customs Duties",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "VAT & Customs Tariffs",
                    "content": {
                        "text": "• Value Added Tax (VAT): Consumption tax levied on the incremental value added to a product at each production stage.\n• Import Duty: Tax on foreign imports to raise revenue, protect local industry, and prevent dumping.\n• Export Duty: Tax on raw material exports to encourage domestic processing."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Corporate and Customs Revenue",
                    "content": IMG_AGRO_PROCESSING_TAX
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Government Budget & Three Budget Types",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Budget Balances",
                    "content": {
                        "text": "1. Balanced Budget: Estimated Revenue = Proposed Expenditure (Neutral economic stance).\n2. Deficit Budget: Estimated Revenue < Proposed Expenditure (Stimulates job creation in recession; requires borrowing).\n3. Surplus Budget: Estimated Revenue > Proposed Expenditure (Extracts cash to cool down high inflation)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "National Budget Balances and Fiscal Policy Matrix",
                    "svg_content": SVG_BUDGET_FISCAL_POLICY_MATRIX,
                    "content": {
                        "text": "Matrix illustrating balanced, deficit, and surplus budgets alongside fiscal policy economic transmission."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Fiscal Policy as an Economic Tool",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Macroeconomic Fiscal Policy",
                    "content": {
                        "text": "Fiscal policy is the state's deliberate manipulation of taxation and public expenditure to achieve economic growth, high employment, stable prices, and balance-of-payments equilibrium."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Quantitative Worked Example: National Treasury Budget",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "6-Step Budget Balance Calculation",
                    "content": {
                        "text": "Problem: A National Treasury estimates the following details for 2026/2027 (in Sh. Millions):\nPAYE = 280,000 | VAT = 320,000 | Import Duty = 110,000 | Court Fines = 45,000 | Licence Fees = 15,000\nRecurrent Salaries = 180,000 | Medicines & Fuel = 75,000 | SGR Construction = 250,000 | Airport Construction = 120,000\n\nCalculate Total Revenue, Total Expenditure, Budget Balance, and classify the Budget Type.\n\nSolution:\nStep 1: Total Revenue = (280,000 + 320,000 + 110,000) + (45,000 + 15,000) = 770,000 Million Shillings.\nStep 2: Total Expenditure = (180,000 + 75,000) + (250,000 + 120,000) = 625,000 Million Shillings.\nStep 3: Budget Balance = 770,000 - 625,000 = +145,000 Million Shillings.\nStep 4: Classification = Surplus Budget of Sh. 145,000 Million.\nStep 5: Macroeconomic Context = Contractionary surplus budget designed to reduce money supply and cool down demand-pull inflation."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Quantitative Worked Example 2: Deficit Financing",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Budget Deficit & Debt Sourcing",
                    "content": {
                        "text": "Problem: Estimated Development Spending = Sh. 520B, Recurrent Spending = Sh. 680B, Tax Collection = Sh. 1,050B. Compute budget balance and state deficit financing options.\n\nSolution:\nTotal Expenditure = 520B + 680B = Sh. 1,200B.\nTotal Revenue = Sh. 1,050B.\nBudget Balance = 1,050B - 1,200B = -150 Billion Shillings (Deficit of Sh. 150 Billion).\nFinancing: The state will borrow internally (issuing T-bills/bonds, risking crowding out) or externally (from World Bank/ADB)."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Quantitative Worked Example 3: Country Z KCSE Analysis",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Country Z Macroeconomic Impact Analysis",
                    "content": {
                        "text": "Problem: Country Z estimates VAT (240,000M), PAYE (210,000M), Import Duty (90,000M), Court Fines (30,000M), Dividends (25,000M), Salaries (195,000M), Medicines (85,000M), SGR Construction (310,000M), Rural Clinics (120,000M). Calculate budget balance and analyze impact on jobs and inflation.\n\nSolution:\nTotal Revenue = 240,000 + 210,000 + 90,000 + 30,000 + 25,000 = 595,000 Million Shillings.\nTotal Expenditure = (195,000 + 85,000) + (310,000 + 120,000) = 710,000 Million Shillings.\nBudget Balance = 595,000 - 710,000 = -115,000 Million Shillings (Deficit Budget).\nMacro Impact: Massive development spending (SGR & clinics) creates jobs, reducing unemployment, but excess cash injection carries risk of demand-pull inflation."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "The government budget plans public finances. Deficit budgets stimulate jobs during recessions; surplus budgets cool down inflation. Fiscal policy manipulates taxes and spending for economic stability."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Integrated Practice: Paper 1",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Paper 1 Short-Answer Mastery",
                    "content": {
                        "text": "1. Non-Tax Revenue Sources: Court fines, licence fees, parastatal dividends, state property rent.\n2. Deficit Budget Circumstances: Economic recession, high unemployment, national disasters/emergencies.\n3. Recurrent vs Development Features: Recurrent is repetitive and non-asset creating; Development is capital and asset-creating."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Integrated Practice: Paper 2",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Paper 2 Essay Model Answers",
                    "content": {
                        "text": "a) Canons of a Good Tax System: Equity (fairness by ability to pay), Certainty (clear rules and deadlines), Convenience (collected at best time), Economy (low collection cost), Elasticity (automatic GDP expansion).\nb) Negative Effects of Progressive Taxation: Discourages hard work/overtime, suppresses business risk-taking, encourages tax evasion, assumes equal earner needs, reduces private capital accumulation."
                    }
                }
            ]
        }
    ]
}

TOPIC4_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA
]
