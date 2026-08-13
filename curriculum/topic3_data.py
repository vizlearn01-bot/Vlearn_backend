"""
VLearn Form 4 Business Studies — Topic 3: Money and Banking
Authoritative Pedagogical Data Structures for 8 Lessons (77 Pages).
"""

from curriculum.ingest_form4_business_studies_topic3_svgs import (
    SVG_BARTER_VS_MONEY_FLOW,
    SVG_MONEY_EVOLUTION_TIMELINE,
    SVG_LIQUIDITY_PREFERENCE_TREE,
    SVG_KENYAN_BANKING_PYRAMID,
    SVG_MONETARY_POLICY_TRANSMISSION
)

# Verified Wikimedia photographic assets
IMG_TRADITIONAL_MARKET = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Traditional open-air commercial market in Kiambu, Kenya, illustrating physical commodity trade and decentralized agricultural exchange.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_NAIROBI_FINANCIAL_DISTRICT = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Port of Mombasa cargo shipping terminal, demonstrating large-scale commercial transactions and international trade financing.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

IMG_LOCAL_COMMERCE = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
    "text": "Maasai Market in Nairobi, demonstrating monetary exchange, unit pricing, and cash transactions in local handicraft commerce.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Maasai_Market-Nairobi.jpg"
}

IMG_TEA_FACTORY_PROCESSING = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/2009.12-363-1125ap_tea%2Cprocessing%28withering%29%2Cstirring_Rukuriri_Tea_Factory%2Ctea-zone_N_of_Embu%28C_Highlands%29%2CKE_mon14dec2009-1242h.jpg",
    "text": "Rukuriri Tea Processing Factory in Embu, illustrating agro-industrial enterprise financing and commercial banking payroll management.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2009.12-363-1125ap_tea,processing(withering),stirring_Rukuriri_Tea_Factory,tea-zone_N_of_Embu(C_Highlands),KE_mon14dec2009-1242h.jpg"
}

IMG_JUA_KALI_ENTERPRISE = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "Artisans in an informal Jua Kali workshop, illustrating working capital requirements, cash liquidity needs, and microfinance.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

IMG_TRANSPORT_LOGISTICS = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
    "text": "Standard Gauge Railway freight train in Kenya, showing capital investment financed through institutional bank syndications and treasury funds.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
}

# ==============================================================================
# LESSON 1: BARTER TRADE AND ITS LIMITATIONS (9 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Barter Trade and its Limitations",
    "lesson_title": "The Barter Economy, Structural Bottlenecks, and Trade Friction",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Exchange Systems",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define barter trade, state its historical advantages, and explain the six fundamental limitations of barter that necessitated the development of money."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Exchange Systems Matter",
                    "content": {
                        "text": "Before money existed, human survival depended on direct commodity exchange. If you grew maize and needed milk, you had to find a cattle keeper who desired maize. Understanding barter helps us appreciate how money transformed commerce from exhausting physical swaps into frictionless global trade."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Meaning of Barter Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Barter Trade",
                    "content": {
                        "term": "Barter Trade",
                        "definition": "The direct exchange of goods and services for other goods and services without the use of money as an intermediary medium of exchange."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Traditional Commodity Exchange",
                    "content": IMG_TRADITIONAL_MARKET
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Advantages of Barter Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Five Historical Benefits of Barter",
                    "content": {
                        "text": "1. Immediate Acquisition: Traders acquired what they needed immediately without waiting for financial intermediaries.\n2. Disposal of Surplus: Farmers exchanged perishable agricultural surpluses before spoilage occurred.\n3. Social Cohesion: Barter required personal interaction and lengthy negotiation, strengthening tribal and community bonds.\n4. Encouraged Specialization: Individuals specialized in specific crafts (e.g. blacksmithing, pottery) knowing they could barter their output for food.\n5. Broadened Living Standards: Enabled communities to consume goods they could not produce locally."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The Double Coincidence of Wants",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Primary Bottleneck of Barter",
                    "content": {
                        "text": "For a barter transaction to take place, there must be a 'Double Coincidence of Wants'. This means Trader A must possess what Trader B desires, and Trader B must simultaneously possess what Trader A desires. If preferences do not match exactly, trade is blocked."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Barter Bottleneck vs. Monetary Exchange",
                    "svg_content": SVG_BARTER_VS_MONEY_FLOW,
                    "content": {
                        "text": "Visual comparison illustrating how the double coincidence requirement creates deadlock in barter trade, whereas money acts as a frictionless universal exchange token."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Indivisibility and Perishability",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Physical Asset Constraints",
                    "content": {
                        "text": "1. Indivisibility of Certain Goods: Many large assets cannot be divided without destroying their value. For instance, a live cow cannot be divided into pieces to buy a single clay pot without killing the animal.\n2. Perishability of Commodities: Agricultural commodities like fish, vegetables, and milk rot quickly, making them useless as long-term stores of wealth."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Valuation, Bulkiness, and Deferred Payments",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Further Institutional Inconveniences",
                    "content": {
                        "text": "1. Lack of Standard Measure of Value: There was no common unit to price goods. Determining how many baskets of millet equaled one sheep required exhaustive separate negotiations.\n2. Transportation of Bulky Goods: Moving heavy goods (such as cattle, grain, or timber) across long distances for trade was physically exhausting and unsafe.\n3. Lack of Standard for Deferred Payments: Debt and credit contracts could not be recorded reliably due to commodity price fluctuations and deterioration over time."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Barter Limitations Comparative Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Summary of Barter Trade Limitations",
                    "content": {
                        "headers": ["Barter Limitation", "Core Economic Problem", "Real-World Impact"],
                        "rows": [
                            ["Double Coincidence of Wants", "Requires exact simultaneous matching of consumer needs", "High search costs; many trades aborted"],
                            ["Indivisibility of Goods", "Assets lose value when partitioned (e.g. livestock)", "Inability to conduct small-value transactions"],
                            ["Perishability", "Commodities decay and spoil rapidly", "Impossible to store wealth for future use"],
                            ["Lack of Unit of Account", "No standard monetary denominator", "Every trade requires independent ratio bargaining"],
                            ["Bulkiness / Portability", "High weight relative to economic value", "High physical transport costs and risks"],
                            ["No Deferred Payment Unit", "No stable asset for debt contracts", "Credit transactions virtually non-existent"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application & Diagnostic Case",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Diagnosing Barter Friction",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Scenario", "description": "Otieno has 5 sacks of potatoes and wants 1 dairy cow. Mwangi has dairy cows but only wants sheep. Juma has sheep but wants maize."},
                            {"title": "Step 2: Required Diagnostic", "description": "Identify the exact barter limitation preventing Otieno from securing a cow directly from Mwangi."},
                            {"title": "Step 3: Economic Rule", "description": "Barter trade requires a double coincidence of wants; otherwise triangular or multi-party swaps must occur."},
                            {"title": "Step 4: Substitution & Analysis", "description": "Otieno has potatoes; Mwangi wants sheep. There is no coincidence of wants between Otieno and Mwangi."},
                            {"title": "Step 5: Alternative Verification", "description": "Trade fails because potatoes cannot be transformed into sheep directly without an intermediate token."},
                            {"title": "Step 6: Economic Conclusion", "description": "The transaction suffers from a lack of double coincidence of wants, generating excessive transaction friction."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Barter Trade",
                    "content": {
                        "question": "Which of the following limitations of barter trade made it impossible for early traders to accumulate wealth for future retirement?",
                        "options": [
                            {"id": "a", "text": "Indivisibility of livestock assets"},
                            {"id": "b", "text": "Perishability of agricultural commodities", "correct": True, "feedback": "Correct! Perishable commodities decay rapidly, preventing traders from storing purchasing power over time."},
                            {"id": "c", "text": "Social cohesion between community elders"},
                            {"id": "d", "text": "Specialization in blacksmithing"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 1 Summary",
                    "content": {
                        "text": "Barter trade facilitated early societal exchange but was severely constrained by the double coincidence of wants, indivisibility, perishability, lack of standard measure of value, bulkiness, and lack of deferred payment standards."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: MEANING, CHARACTERISTICS & EVOLUTION OF MONEY (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Meaning, Characteristics & Evolution of Money",
    "lesson_title": "Monetary Essentials, Physical Attributes, and Stages of Development",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Money and Currency",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define money, explain the 8 essential characteristics of a good monetary item, and outline the 5 chronological stages of monetary evolution."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Nature of Money",
                    "content": {
                        "text": "A modern banknote is simply a printed piece of polymer or paper, yet it purchases valuable food, clothing, and machinery. Money works because of collective societal trust backed by government decree (legal tender)."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition of Money",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Money",
                    "content": {
                        "term": "Money",
                        "definition": "Anything that is generally accepted by law and custom as a medium of exchange for goods and services, and for the settlement of debts in a given economy."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Commercial Exchange in Kenya",
                    "content": IMG_LOCAL_COMMERCE
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Characteristics of Good Money (Part 1)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Physical & Institutional Attributes",
                    "content": {
                        "text": "1. General Acceptability: Money must be readily accepted by everyone in the economy as payment without hesitation.\n2. Portability: It must have high value relative to weight and size so it can be carried around easily.\n3. Divisibility: It must be capable of being divided into smaller fractions (e.g. shillings into cents, 1,000 note into 100 notes) without losing proportionate value.\n4. Durability: It must withstand frequent handling, folding, and environmental wear without quickly tearing or rotting."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Characteristics of Good Money (Part 2)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Stability & Quality Attributes",
                    "content": {
                        "text": "5. Homogeneity: Units of the same denomination must be identical in appearance, weight, and quality to prevent confusion.\n6. Relative Scarcity: Money supply must be limited relative to demand to preserve its purchasing power. If money grew on trees, it would have zero value.\n7. Cognizability (Recognizability): It must be easily distinguishable by sight and touch so genuine currency is recognized and counterfeits detected.\n8. Malleability / Stability of Value: Capable of receiving official security stamps and maintaining relatively stable purchasing power over time."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Characteristics of Money Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Eight Essential Characteristics of Money",
                    "content": {
                        "headers": ["Characteristic", "Definition & Explanation", "Why It Is Crucial"],
                        "rows": [
                            ["General Acceptability", "Universally trusted by buyers and sellers", "Eliminates barter search friction"],
                            ["Portability", "Lightweight with concentrated economic value", "Enables daily mobility of purchasing power"],
                            ["Divisibility", "Can be split into smaller exact denominations", "Facilitates small-scale and large-scale purchases"],
                            ["Durability", "Withstands physical friction and time", "Allows money to act as a store of value"],
                            ["Homogeneity", "Identical within each denomination", "Prevents discrimination between currency notes"],
                            ["Relative Scarcity", "Supply strictly controlled by central bank", "Guarantees value and prevents hyperinflation"],
                            ["Cognizability", "Instantly identifiable by sight and touch", "Stops counterfeit proliferation"],
                            ["Malleability", "Can be cast, printed, and officially embossed", "Allows official legal markings and security watermarks"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Evolution of Money: 5 Historical Stages",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "From Physical Swaps to Digital Bytes",
                    "content": {
                        "text": "Money progressed across 5 major evolutionary stages:\n1. Barter Stage: Direct goods-for-goods exchange.\n2. Commodity Money Stage: Standard items like cowrie shells, salt blocks, and cattle.\n3. Metallic Money Stage: Gold, silver, and copper coins stamped by monarchs.\n4. Paper Money Stage: Banknotes originating from goldsmith safe-custody receipts.\n5. Electronic / Digital Money: Cashless transfers via credit cards, EFT, and mobile banking (M-Pesa)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "The Five Stages of Monetary Evolution",
                    "svg_content": SVG_MONEY_EVOLUTION_TIMELINE,
                    "content": {
                        "text": "Vector timeline illustrating the historical progression from barter and commodity tokens to modern electronic and mobile funds."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Commodity vs Metallic vs Paper Money",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Each Stage Advanced Over the Prior",
                    "content": {
                        "text": "Commodity money solved double coincidence but failed on durability and portability. Metallic coins provided durability and divisibility, but carrying large chests of heavy gold was dangerous. Paper money emerged when merchants realized they could trade goldsmith safe-custody receipts directly, establishing the foundation of modern central bank currency."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Modern Digital & Mobile Money",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Cashless Revolution in Kenya",
                    "content": {
                        "text": "In the modern era, physical paper is increasingly supplemented by electronic money. In Kenya, mobile money platforms (such as M-Pesa) and Electronic Funds Transfer (EFT) allow instantaneous settlement of transactions across the country, reducing the risks of cash theft and drastically cutting commercial transaction costs."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Worked Analysis: Evaluating Monetary Items",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Evaluating Asset Suitability as Money",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Asset", "description": "A rural community proposes using large clay pots as currency."},
                            {"title": "Step 2: Required Evaluation", "description": "Assess whether clay pots fulfill the required characteristics of good money."},
                            {"title": "Step 3: Criteria", "description": "Test against portability, divisibility, durability, and homogeneity."},
                            {"title": "Step 4: Evaluation", "description": "Clay pots are bulky (poor portability), brittle (poor durability), and cannot be broken into fractions without breaking (zero divisibility)."},
                            {"title": "Step 5: Comparative Check", "description": "Unlike metallic coins or paper notes, clay pots fail three foundational physical criteria."},
                            {"title": "Step 6: Economic Conclusion", "description": "Clay pots make unacceptable money because they lack portability, durability, and divisibility."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Characteristics of Money",
                    "content": {
                        "question": "If a government prints currency notes that are easily torn by daily use, which characteristic of money has been violated?",
                        "options": [
                            {"id": "a", "text": "Homogeneity"},
                            {"id": "b", "text": "Durability", "correct": True, "feedback": "Correct! Durability ensures that money withstands frequent handling without physical decay."},
                            {"id": "c", "text": "Divisibility"},
                            {"id": "d", "text": "Scarcity"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 2 Summary",
                    "content": {
                        "text": "Money is anything generally accepted as a medium of exchange. It must possess acceptability, portability, divisibility, durability, homogeneity, scarcity, cognizability, and malleability, evolving from barter to digital money."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: FUNCTIONS OF MONEY (9 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Functions of Money",
    "lesson_title": "The Four Core Economic Functions of Money",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Monetary Functions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to identify and explain the four core functions of money (medium of exchange, measure of value, store of value, and standard for deferred payments) and link each function to the specific barter limitation it resolves."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Money as an Economic Engine",
                    "content": {
                        "text": "Money acts as an economic multi-tool. Rather than just being cash in your pocket, money performs four distinct structural functions that allow markets to clear, prices to coordinate resources, and savings to fund investment."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "1. Medium of Exchange",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Primary Facilitator of Trade",
                    "content": {
                        "text": "Money acts as an intermediary token in transactions. You sell your labor or goods for money, and then use that money to purchase goods from anyone else. This completely eliminates the need for a double coincidence of wants."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "2. Measure of Value / Unit of Account",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Common Economic Denominator",
                    "content": {
                        "text": "Money provides a standard common yardstick to price all goods and services in the economy. A loaf of bread is Sh. 65; a textbook is Sh. 600; a laptop is Sh. 45,000. This enables accounting, price comparisons, and business bookkeeping."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "3. Store of Value",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Preserving Purchasing Power",
                    "content": {
                        "text": "Money allows individuals and businesses to save current purchasing power for future consumption. Unlike perishable agricultural produce (e.g. tomatoes or milk), money can be kept in a bank account and spent years later."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "4. Standard for Deferred Payments",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Enabling Credit and Debt Contracts",
                    "content": {
                        "text": "Money serves as a reliable unit in which debts and credit contracts are denominated. A firm can borrow Sh. 5,000,000 today and agree to repay in fixed monthly installments over 5 years. This provides certainty to both borrowers and lenders."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Functions of Money vs Barter Limitations",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "How Money Resolves Barter Friction",
                    "content": {
                        "headers": ["Function of Money", "Barter Limitation Resolved", "Mechanism of Resolution"],
                        "rows": [
                            ["Medium of Exchange", "Double Coincidence of Wants", "Separates the act of selling from buying; any item can be sold for cash"],
                            ["Measure of Value / Unit of Account", "No Standard Measure of Value", "Establishes a uniform price tag for every good and service in the market"],
                            ["Store of Value", "Perishability of Physical Goods", "Allows wealth to be accumulated safely in banks without physical rot"],
                            ["Standard for Deferred Payments", "Lack of Debt / Credit Units", "Provides a stable legal unit to record and settle future financial obligations"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Real-World Application & Function Mapping",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Classifying Real-World Functions",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Cases", "description": "Case A: A supermarket price tag shows 'Sh. 200'. Case B: A farmer deposits Sh. 50,000 in a fixed account. Case C: A company takes a 3-year bank loan."},
                            {"title": "Step 2: Required Task", "description": "Identify the primary function of money active in each case."},
                            {"title": "Step 3: Function Definitions", "description": "Price tagging = Measure of Value; Savings = Store of Value; Loan repayment = Standard for Deferred Payments."},
                            {"title": "Step 4: Case Matching", "description": "Case A: Measure of value; Case B: Store of value; Case C: Standard for deferred payments."},
                            {"title": "Step 5: Verification", "description": "Each case matches the distinct role of money in pricing, saving, or credit contracting."},
                            {"title": "Step 6: Economic Takeaway", "description": "Money performs complementary functions simultaneously across everyday commerce."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Inflation and Store of Value Impairment",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "When Money Fails as a Store of Value",
                    "content": {
                        "text": "While money is physically durable, rapid inflation erodes its real purchasing power. If prices double in one year, Sh. 1,000 saved buys only half as many goods. Therefore, to serve effectively as a store of value, money requires price stability maintained by the central bank."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Functions of Money",
                    "content": {
                        "question": "Which function of money is exercised when a wholesaler agrees to supply goods to a retailer on 30-day credit terms?",
                        "options": [
                            {"id": "a", "text": "Store of value"},
                            {"id": "b", "text": "Standard for deferred payments", "correct": True, "feedback": "Correct! A credit transaction relies on money as a standard unit for future deferred payment."},
                            {"id": "c", "text": "Indivisibility of capital"},
                            {"id": "d", "text": "Commodity token exchange"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 3 Summary",
                    "content": {
                        "text": "Money performs four core functions: medium of exchange, measure of value, store of value, and standard for deferred payments, resolving all fundamental inefficiencies of barter."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 4: DEMAND AND SUPPLY OF MONEY (9 Pages)
# ==============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Demand and Supply of Money",
    "lesson_title": "Liquidity Preference Motives and Monetary Supply Components",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Monetary Demand",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define demand for money (liquidity preference), explain the transaction, precautionary, and speculative motives for holding cash, and define the components of the national money supply."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Hold Cash?",
                    "content": {
                        "text": "Why do individuals and firms hold onto physical cash in wallets and current accounts instead of investing all their wealth in interest-earning shares or real estate? This economic behavior is known as liquidity preference."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Demand for Money (Liquidity Preference)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Demand for Money",
                    "content": {
                        "term": "Demand for Money (Liquidity Preference)",
                        "definition": "The desire or tendency of individuals and business enterprises to hold wealth in liquid cash form (notes, coins, and checking deposits) rather than in illiquid or interest-earning assets."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Daily Cash Liquidity in Small Enterprises",
                    "content": IMG_JUA_KALI_ENTERPRISE
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Three Motives for Holding Cash",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Keynesian Liquidity Motives",
                    "content": {
                        "text": "According to economic theory, cash is held for three distinct motives:\n1. Transaction Motive: Money held to settle day-to-day foreseeable operational and living expenses.\n2. Precautionary Motive: Money held as an emergency buffer for unforeseen events.\n3. Speculative Motive: Money held in cash waiting for profitable future investment opportunities."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Liquidity Preference Motives and Money Supply",
                    "svg_content": SVG_LIQUIDITY_PREFERENCE_TREE,
                    "content": {
                        "text": "Structural diagram illustrating the transaction, precautionary, and speculative motives alongside the components of the national money supply."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The Transaction Motive (Income & Business)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Breakdown of the Transaction Motive",
                    "content": {
                        "text": "The transaction motive is subdivided into:\n- Income Motive: Households holding cash between paydays to buy daily groceries, pay commuter bus fares, and settle electricity bills.\n- Business Motive: Enterprises holding cash to purchase daily raw materials, pay casual wages, and settle delivery fuel costs.\nDeterminant: The transaction demand for money depends directly on one's level of income or business turnover."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "The Precautionary & Speculative Motives",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Emergencies vs Market Timing",
                    "content": {
                        "text": "1. Precautionary Motive: Held to guard against unpredictable emergencies such as sudden medical bills, unexpected vehicle breakdown, or legal costs.\n2. Speculative Motive: Held by investors anticipating market price changes. When interest rates are low and bond/share prices are expected to drop, investors hold cash so they can buy securities cheaply when prices hit bottom."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Supply of Money: Meaning and Components",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Supply of Money",
                    "content": {
                        "term": "Supply of Money",
                        "definition": "The total stock of monetary items in active circulation in an economy at a specific point in time, consisting of currency in circulation and demand deposits."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Two Core Components of Money Supply",
                    "content": {
                        "text": "1. Currency in Circulation: Total physical banknotes and coins circulating outside the banking system in hands of the public.\n2. Demand Deposits: Customer balances held in commercial bank current accounts that can be withdrawn or transferred immediately on demand using cheques or EFT."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Liquidity Motive Classification Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Comparative Analysis of Liquidity Motives",
                    "content": {
                        "headers": ["Holding Motive", "Purpose of Holding Cash", "Primary Determinant", "Real-World Kenyan Example"],
                        "rows": [
                            ["Transaction (Income)", "Regular household living expenses", "Income level & pay interval", "Keeping Sh. 500 for daily food and matatu fare"],
                            ["Transaction (Business)", "Daily commercial working capital", "Volume of sales / turnover", "Supermarket keeping float cash in checkout tills"],
                            ["Precautionary", "Unforeseen emergencies & shocks", "Level of risk & family size", "Keeping Sh. 10,000 emergency fund for sickness"],
                            ["Speculative", "Timing financial / real estate investments", "Prevailing interest rates", "Holding Sh. 500,000 cash waiting for share prices to drop"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Worked Classification: Identifying Motives",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Classifying Motives for Holding Cash",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Actions", "description": "Action A: Wanjiku keeps Sh. 2,000 to buy fuel tomorrow. Action B: Kamau retains Sh. 100,000 in cash because he believes land prices will drop next month."},
                            {"title": "Step 2: Required Classification", "description": "Identify the liquidity motive for Wanjiku and Kamau."},
                            {"title": "Step 3: Economic Principles", "description": "Routine expense = Transaction motive; Asset price anticipation = Speculative motive."},
                            {"title": "Step 4: Classification", "description": "Wanjiku: Transaction (income) motive. Kamau: Speculative motive."},
                            {"title": "Step 5: Diagnostic Check", "description": "Wanjiku's expense is certain and routine; Kamau is timing an asset market opportunity."},
                            {"title": "Step 6: Economic Conclusion", "description": "Proper classification distinguishes consumption liquidity from investment timing liquidity."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Demand and Supply of Money",
                    "content": {
                        "question": "Which of the following represents the speculative motive for holding money?",
                        "options": [
                            {"id": "a", "text": "Holding cash to buy lunch at work"},
                            {"id": "b", "text": "Keeping money to settle unexpected hospital bills"},
                            {"id": "c", "text": "Holding cash waiting for share prices on the Nairobi Securities Exchange to fall", "correct": True, "feedback": "Correct! The speculative motive involves holding cash to exploit profitable future investment opportunities."},
                            {"id": "d", "text": "Depositing statutory cash reserves at the Central Bank"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 4 Summary",
                    "content": {
                        "text": "Demand for money (liquidity preference) is driven by transaction, precautionary, and speculative motives. Money supply comprises physical currency in active circulation plus commercial bank demand deposits."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 5: THE KENYAN BANKING SYSTEM HIERARCHY (9 Pages)
# ==============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "The Kenyan Banking System Hierarchy",
    "lesson_title": "Institutional Structure, The Financial Pyramid, and Fractional Reserves",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Banking Systems",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define banking, describe the 4-tier structural hierarchy of the Kenyan banking system, and explain how fractional reserve banking evolved from early goldsmiths."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Financial Plumbing of Kenya",
                    "content": {
                        "text": "The banking system acts as the financial heart of the nation, pumping funds from surplus units (savers) to deficit units (investors and entrepreneurs). It is organized in a disciplined regulatory hierarchy supervised by the Central Bank of Kenya."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Meaning of Banking",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Banking",
                    "content": {
                        "term": "Banking",
                        "definition": "All financial activities conducted by specialized financial institutions involving money, including accepting customer deposits, advancing loans, creating credit, and facilitating payment transfers."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Financial Capital Infrastructure",
                    "content": IMG_NAIROBI_FINANCIAL_DISTRICT
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The 4-Tier Kenyan Banking Hierarchy",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Four Layers of Kenya's Financial System",
                    "content": {
                        "text": "The Kenyan banking system is structured in four clear tiers:\n1. The Central Bank of Kenya (CBK): Apex regulatory and monetary authority.\n2. Commercial Banks: Profit-seeking deposit-taking institutions (e.g. KCB, Equity Bank, Co-operative Bank, Absa).\n3. Specialized Development Banks (DFIs): State-backed long-term financing institutions (e.g. IDB, KIE, DFCK, AFC).\n4. Non-Bank Financial Institutions (NBFIs): Sectoral intermediaries like SACCOs, Insurance companies, and Building Societies."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "The Kenyan Financial Hierarchy",
                    "svg_content": SVG_KENYAN_BANKING_PYRAMID,
                    "content": {
                        "text": "Pyramid diagram showing the regulatory hierarchy from the Central Bank of Kenya down through commercial banks, development finance institutions, and NBFIs."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Tier 1: Central Bank of Kenya (CBK)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Apex Monetary Regulator",
                    "content": {
                        "text": "The CBK occupies the summit of the monetary system. It does not deal with ordinary citizens or retail businesses for day-to-day banking. Instead, it regulates all other banks, issues currency, and executes monetary policy to stabilize inflation and protect the value of the Kenya Shilling."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Tier 2: Commercial Banks",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Primary Intermediaries for the Public",
                    "content": {
                        "text": "Commercial banks are licensed corporations that interface directly with the general public and business corporations. They accept demand and time deposits, process cheque clearances, provide overdrafts, and generate profit through interest rate spreads."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Tier 3: Specialized Development Banks (DFIs)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Long-Term Strategic Financing",
                    "content": {
                        "text": "Development Finance Institutions (such as the Industrial Development Bank - IDB, Kenya Industrial Estates - KIE, and Agricultural Finance Corporation - AFC) provide long-term capital loans for manufacturing, agro-processing, and national development projects that commercial banks consider too risky or long-term."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Tier 4: Non-Bank Financial Institutions (NBFIs)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Sectoral Savings and Credit Mobilization",
                    "content": {
                        "text": "NBFIs mobilize savings within specific communities or sectors (e.g. teachers' SACCOs, farmer co-operatives, housing building societies, insurance firms). Unlike commercial banks, they cannot offer current accounts withdrawable by cheque and cannot create credit."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Historical Evolution: Goldsmiths to Modern Banks",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Origin of Fractional Reserve Banking",
                    "content": {
                        "text": "In 17th-century London, merchants deposited gold in goldsmiths' secure vaults. Goldsmiths issued paper receipts for the gold. Over time, depositors began trading the receipts directly instead of collecting physical gold. Goldsmiths noticed only a small fraction of depositors withdrew gold simultaneously, leading them to lend out the remaining gold at interest—inventing fractional reserve banking."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Banking Hierarchy",
                    "content": {
                        "question": "Which institution sits at the apex of the Kenyan banking system with regulatory authority over monetary policy?",
                        "options": [
                            {"id": "a", "text": "Industrial Development Bank (IDB)"},
                            {"id": "b", "text": "Central Bank of Kenya (CBK)", "correct": True, "feedback": "Correct! The CBK is the apex monetary regulator governing all commercial banks and financial institutions."},
                            {"id": "c", "text": "Kenya Commercial Bank (KCB)"},
                            {"id": "d", "text": "Agricultural Finance Corporation (AFC)"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 5 Summary",
                    "content": {
                        "text": "The Kenyan banking hierarchy comprises CBK at the apex, followed by commercial banks, specialized development banks, and NBFIs, operating on the principle of fractional reserve intermediation."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 6: COMMERCIAL BANKS, ACCOUNTS & PROFIT SOURCES (10 Pages)
# ==============================================================================
LESSON_6_DATA = {
    "unit_order": 6,
    "unit_name": "Commercial Banks, Accounts & Profit Sources",
    "lesson_title": "Commercial Banking Operations, Account Types, and Profit Channels",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Commercial Banking",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain how commercial banks generate profits, distinguish between Current, Savings, and Fixed Deposit accounts, and describe key banking services."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Commercial Banking Model",
                    "content": {
                        "text": "Commercial banks are profit-seeking business corporations. They provide a safe haven for depositors' funds while channeling those funds into profitable loans and investments."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "How Commercial Banks Make Profits",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Profit Generation Channels",
                    "content": {
                        "text": "1. Interest Spread (Margin): Charging higher interest rates on loans (e.g. 14% p.a.) than the interest paid to savers (e.g. 4% p.a.). The net difference is the bank's gross interest margin.\n2. Investments in Government Securities: Purchasing Treasury bills and Treasury bonds that pay reliable semi-annual interest yields.\n3. Operational Fees and Commissions: Levying fees for ledger maintenance, international money transfers, safe deposit lockers, and ATM card services."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Industrial Enterprise Credit Financing",
                    "content": IMG_TEA_FACTORY_PROCESSING
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "1. Current Accounts (Demand Deposits)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Features of a Current Account",
                    "content": {
                        "text": "- Purpose: Operational transactional tool for businesses and traders.\n- Withdrawal Method: Withdrawable on demand using cheques, debit cards, or electronic transfers without prior notice.\n- Interest: No interest is earned on credit balances.\n- Charges: Ledger fees and monthly transaction service charges are debited.\n- Overdraft Facility: Account holders can negotiate overdraft facilities to overdraw their balance temporarily."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "2. Savings Accounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Features of a Savings Account",
                    "content": {
                        "text": "- Purpose: Designed to encourage thrift and regular personal savings for individuals.\n- Withdrawal Method: Withdrawable using ATM debit cards or over-the-counter slips (no cheque books issued).\n- Interest: Balances above a specified threshold earn a modest rate of interest.\n- Minimum Balance: Requires an active minimum balance to keep the account open.\n- No Overdraft: Overdraft facilities are strictly not available on savings accounts."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "3. Fixed / Time Deposit Accounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Features of a Fixed Deposit Account",
                    "content": {
                        "text": "- Purpose: An investment vehicle for surplus funds not needed for immediate daily transactions.\n- Fixed Period: Funds are locked in for an agreed term (e.g. 3, 6, 12, or 24 months).\n- High Interest: Earns the highest interest rate among bank accounts.\n- Early Withdrawal Penalty: Early withdrawal before the maturity date attracts a financial penalty or complete forfeiture of earned interest."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Comparative Account Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Current vs Savings vs Fixed Deposit Accounts",
                    "content": {
                        "headers": ["Feature", "Current Account", "Savings Account", "Fixed Deposit Account"],
                        "rows": [
                            ["Primary Purpose", "Daily business transactions", "Personal thrift and savings", "Medium-term investment"],
                            ["Withdrawal Mode", "Cheque book, ATM, EFT", "ATM card, passbook, counter slip", "Withdrawn at agreed maturity"],
                            ["Interest Earned", "Zero interest", "Modest / moderate interest", "High agreed interest rate"],
                            ["Bank Charges", "Ledger fees debited", "Zero or minimal ledger fees", "No operational ledger fees"],
                            ["Overdraft Access", "Available to qualified traders", "Strictly NOT available", "Strictly NOT available"],
                            ["Minimum Balance", "No strict minimum", "Mandatory minimum balance", "High minimum opening deposit"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Services Provided by Commercial Banks",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Core Services to Businesses and Individuals",
                    "content": {
                        "text": "1. Mobilizing Deposits: Providing secure savings and current accounts.\n2. Advancing Credit: Granting term loans and overdrafts.\n3. Safekeeping of Valuables: Safe deposit vaults for title deeds, wills, and jewelry.\n4. Fund Remittance: Processing telegraphic transfers, bank drafts, and standing orders.\n5. Financial Advisory: Guiding clients on investments and financial feasibility.\n6. Acting as Referees / Guarantors: Providing creditworthiness certificates for international trade."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Overdraft vs Bank Loan",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Crucial Distinction: Overdraft vs Loan",
                    "content": {
                        "text": "- Overdraft: A flexible permission on a Current Account allowing a customer to draw funds beyond their credit balance up to an agreed ceiling. Interest is charged only on the exact daily overdrawn amount.\n- Bank Loan: A lump sum credited into a customer's account for a fixed duration, with fixed monthly repayment installments and interest charged on the entire disbursed principal."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Worked Calculation: Bank Interest Spread",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Calculation: Computing Net Interest Spread",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Information", "description": "Bank X has total deposits of Sh. 100,000,000 paying depositors 4% interest p.a. It lends Sh. 80,000,000 out as commercial loans at 13% interest p.a."},
                            {"title": "Step 2: Required", "description": "Calculate Bank X's annual interest income, interest expense, and gross net interest spread profit."},
                            {"title": "Step 3: Formula", "description": "Interest Income = Loans × Lending Rate; Interest Expense = Deposits × Deposit Rate; Net Spread = Interest Income - Interest Expense."},
                            {"title": "Step 4: Substitute & Compute", "description": "Interest Income = 80,000,000 × 0.13 = Sh. 10,400,000. Interest Expense = 100,000,000 × 0.04 = Sh. 4,000,000. Net Interest Spread = 10,400,000 - 4,000,000 = Sh. 6,400,000."},
                            {"title": "Step 5: Alternative Verification", "description": "Net Margin Percentage on lent funds = 13% - (4% × 100M/80M) = 13% - 5% = 8%. 8% of 80M = Sh. 6,400,000."},
                            {"title": "Step 6: Economic Interpretation", "description": "The interest rate spread of Sh. 6.4 million represents the bank's core operational earnings before administrative costs."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Commercial Bank Accounts",
                    "content": {
                        "question": "Which type of bank account allows an account holder to overdraw their balance and issue cheques to third parties?",
                        "options": [
                            {"id": "a", "text": "Fixed Deposit Account"},
                            {"id": "b", "text": "Current Account", "correct": True, "feedback": "Correct! Current accounts provide cheque books and allow overdraft facilities to qualified business holders."},
                            {"id": "c", "text": "Savings Account"},
                            {"id": "d", "text": "Treasury Bond Custody Account"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 6 Summary",
                    "content": {
                        "text": "Commercial banks generate profits through interest rate spreads, government securities, and fees, providing current, savings, and fixed deposit accounts alongside safe custody and money remittance services."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 7: MONEY TRANSFER FACILITIES & NBFIs (10 Pages)
# ==============================================================================
LESSON_7_DATA = {
    "unit_order": 7,
    "unit_name": "Money Transfer Facilities & Non-Bank Financial Institutions",
    "lesson_title": "Cheques, Transfer Mechanisms, and Comparative Analysis of NBFIs",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Payment Systems & NBFIs",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain cheque instruments and money transfer facilities (standing orders, credit transfers, telegraphic transfers), identify NBFIs in Kenya, and distinguish between commercial banks and NBFIs."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Payment Facilitation & Sectoral Credit",
                    "content": {
                        "text": "Without reliable money transfer tools, trade would grind to a halt. Commercial banks operate sophisticated payment conduits, while Non-Bank Financial Institutions step in to finance specialized long-term investments like home mortgages and agricultural cooperatives."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Cheques as Payment Instruments",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of a Cheque",
                    "content": {
                        "term": "Cheque",
                        "definition": "An unconditional written order drawn by a current account holder (the Drawer) directing their bank (the Drawee) to pay on demand a specified sum of money to a named person or bearer (the Payee)."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Parties to a Cheque",
                    "content": {
                        "text": "1. Drawer: The account holder writing and signing the cheque.\n2. Drawee: The commercial bank holding the drawer's account and instructed to pay.\n3. Payee: The recipient named on the cheque who receives the funds."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Commercial Bank Transfer Facilities",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Key Money Transfer Methods",
                    "content": {
                        "text": "1. Standing Order: A written instruction by an account holder authorizing the bank to pay a fixed specified sum of money to a named person/firm at regular intervals (e.g. monthly rent or loan repayment).\n2. Credit Transfer: A method where a single payment slip is used to pay multiple individuals simultaneously (e.g. an employer paying monthly salaries to 50 employees).\n3. Telegraphic Transfer (TT): An electronic method of transferring funds rapidly between banks across cities or internationally, requiring details of sender, payee, amount, and receiving branch.\n4. Electronic Funds Transfer (EFT) / RTGS: Instant inter-bank digital clearance system."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "What are Non-Bank Financial Institutions (NBFIs)?",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of NBFIs",
                    "content": {
                        "term": "Non-Bank Financial Institutions (NBFIs)",
                        "definition": "Financial organizations that mobilize savings from specific groups or the general public and provide specialized credit, but are legally prohibited from offering checking accounts or creating credit."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "National Infrastructure Supported by Long-Term Finance",
                    "content": IMG_TRANSPORT_LOGISTICS
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Examples of NBFIs in Kenya",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Major Categories of NBFIs in Kenya",
                    "content": {
                        "text": "1. SACCOs (Savings and Credit Co-operative Societies): Member-owned societies (e.g. Mwalimu SACCO, Stima SACCO) mobilizing savings to provide low-interest loans.\n2. Housing Finance / Building Societies: Specialized in providing long-term mortgages for residential and commercial construction (e.g. HFCK).\n3. Insurance Companies: Pool policyholder premiums to underwrite risks and invest surplus capital in long-term infrastructure and government bonds.\n4. Pension Funds: Manage retirement contributions (e.g. NSSF) and invest in real estate and blue-chip shares."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Specialized Development Finance Institutions (DFIs)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Strategic Industrial Development",
                    "content": {
                        "text": "Development finance institutions are specialized bodies established to accelerate economic development in critical sectors:\n- Industrial Development Bank (IDB): Medium and long-term financing for manufacturing.\n- Kenya Industrial Estates (KIE): Supporting micro, small, and medium industrial workshops (SMEs).\n- Agricultural Finance Corporation (AFC): Providing credit to farmers for agricultural machinery and inputs.\n- Development Finance Company of Kenya (DFCK): Financing tourism and industrial ventures."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Commercial Banks vs. NBFIs Comparative Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Distinguishing Commercial Banks from NBFIs",
                    "content": {
                        "headers": ["Dimension", "Commercial Banks", "Non-Bank Financial Institutions (NBFIs)"],
                        "rows": [
                            ["Cheque Accounts", "Offer Current Accounts withdrawable by cheque", "Legally prohibited from offering cheque accounts"],
                            ["Credit Creation", "Actively create credit via fractional reserves", "Cannot create credit; lend only deposited funds"],
                            ["Loan Duration", "Mainly short-term and medium-term working capital", "Specialized medium-term and long-term capital"],
                            ["Purpose of Finance", "Unrestricted commercial and personal loans", "Specified sectoral purpose (e.g. mortgages, agriculture)"],
                            ["Foreign Exchange", "Authorized foreign exchange dealers", "Generally cannot engage in foreign currency trading"],
                            ["Governing Statute", "Governed under the Banking Act by the CBK", "Governed by specific statutes (e.g. SACCO Act, Insurance Act)"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Worked Analysis: Selecting Transfer Facilities",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Selecting the Appropriate Payment Tool",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Scenarios", "description": "Scenario A: A tenant wants to pay monthly rent of Sh. 25,000 on the 1st of every month automatically. Scenario B: An importer in Mombasa must send Sh. 2,000,000 urgently to a supplier in Germany today."},
                            {"title": "Step 2: Required Selection", "description": "Identify the most suitable bank transfer facility for each scenario."},
                            {"title": "Step 3: Transfer Rules", "description": "Recurring fixed payments = Standing Order; Urgent international transfers = Telegraphic Transfer (TT / SWIFT)."},
                            {"title": "Step 4: Application", "description": "Scenario A: Standing Order. Scenario B: Telegraphic Transfer (TT)."},
                            {"title": "Step 5: Operational Verification", "description": "Standing order automates recurring deductions; TT provides same-day verified international settlement."},
                            {"title": "Step 6: Economic Takeaway", "description": "Using the appropriate payment tool minimizes transaction costs and prevents default."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "The Role of SACCOs in Financial Inclusion",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Community-Based Credit Mobilization",
                    "content": {
                        "text": "SACCOs play a massive role in the Kenyan economy by pooling small monthly savings from members who might not qualify for commercial bank loans. By using member guarantors instead of rigid land title deeds, SACCOs provide accessible low-interest credit for school fees, agriculture, and small businesses."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Transfer Facilities & NBFIs",
                    "content": {
                        "question": "Which of the following is a primary distinction between commercial banks and Non-Bank Financial Institutions (NBFIs)?",
                        "options": [
                            {"id": "a", "text": "Commercial banks accept deposits, while NBFIs do not accept any money"},
                            {"id": "b", "text": "Commercial banks can offer current accounts withdrawable by cheque, while NBFIs cannot", "correct": True, "feedback": "Correct! NBFIs are legally barred from offering cheque-operated current accounts."},
                            {"id": "c", "text": "NBFIs are regulated directly by the Ministry of Foreign Affairs"},
                            {"id": "d", "text": "Commercial banks only provide housing mortgage loans"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 7 Summary",
                    "content": {
                        "text": "Cheques, standing orders, credit transfers, and telegraphic transfers facilitate payments. NBFIs provide specialized long-term and sectoral financing, distinguished from commercial banks by the absence of cheque accounts and credit creation."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 8: THE CENTRAL BANK, MONETARY POLICY & MODERN TRENDS (11 Pages)
# ==============================================================================
LESSON_8_DATA = {
    "unit_order": 8,
    "unit_name": "The Central Bank of Kenya, Monetary Policy & Modern Trends",
    "lesson_title": "Central Banking, Credit Control Tools, Currency Conversions, and Digital Trends",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Central Banking",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to state the functions of the Central Bank of Kenya, explain the five monetary policy tools used to control credit, solve multi-currency exchange rate problems, and discuss modern trends in banking."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Economic Thermostat of Kenya",
                    "content": {
                        "text": "The Central Bank of Kenya (CBK) acts as the economic thermostat of the nation. When inflation threatens living standards, CBK cools down the economy by tightening credit. When business activity slows, CBK eases monetary policy to stimulate growth."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Functions of the Central Bank of Kenya (CBK)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Six Primary Functions of CBK",
                    "content": {
                        "text": "1. Sole Issuer of Currency: Exclusive legal right to print banknotes and mint coins in Kenya.\n2. Banker to the Government: Manages Treasury bank accounts, receives revenue, and services public debt.\n3. Banker to Commercial Banks: Holds statutory reserve deposits and operates the national Cheque Clearing House.\n4. Lender of Last Resort: Advances emergency liquidity loans to commercial banks facing temporary cash shortages.\n5. Custodian of Foreign Exchange Reserves: Manages official national reserves of USD, Euros, etc., to stabilize the Kenya Shilling.\n6. Formulates & Executes Monetary Policy: Regulates money supply to maintain price stability and low inflation."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Monetary Policy & Credit Control Tools",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "How CBK Manages Inflation (Credit Squeeze)",
                    "content": {
                        "text": "To reduce money supply and control demand-pull inflation, the CBK utilizes five key monetary policy tools:\n1. Bank Rate (Discount Rate): Raising the interest rate charged to commercial banks.\n2. Open Market Operations (OMO): Selling Treasury bills and bonds to absorb bank cash.\n3. Cash / Liquidity Reserve Ratio: Raising the percentage of deposits banks must lock up with CBK.\n4. Moral Suasion: Directly requesting bank executives to restrict credit expansion.\n5. Direct Action / Directives: Imposing mandatory ceilings on commercial bank lending."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Central Bank Monetary Policy Transmission",
                    "svg_content": SVG_MONETARY_POLICY_TRANSMISSION,
                    "content": {
                        "text": "Transmission flowchart showing how CBK credit control tools pass through commercial banks to regulate aggregate demand and stabilize inflation."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Detailed Monetary Policy Tools",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Monetary Policy Tools and Inflation Response",
                    "content": {
                        "headers": ["Policy Tool", "CBK Action to Fight Inflation", "Mechanism on Commercial Banks", "Final Macro Outcome"],
                        "rows": [
                            ["Bank Rate", "Raise the bank rate", "Borrowing from CBK costlier; banks hike loan rates", "Public borrowing and spending fall"],
                            ["Open Market Operations (OMO)", "Sell Treasury bills/bonds", "Drains liquid cash reserves from commercial banks", "Banks have less money to advance as loans"],
                            ["Cash Reserve Ratio (CRR)", "Increase statutory cash ratio", "More customer cash is locked up at CBK vaults", "Credit multiplier and lending capacity shrink"],
                            ["Moral Suasion", "Persuade bank CEOs to limit credit", "Banks voluntarily tighten loan qualification criteria", "Growth of consumer credit decelerates"],
                            ["Direct Directives", "Issue mandatory credit ceilings", "Banks legally prohibited from lending above quota", "Strict cap placed on money supply growth"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Recent Trends in Modern Banking",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Technological & Operational Modernization",
                    "content": {
                        "text": "1. Computerization: Complete automation of bank ledgers, accounts, and central databases.\n2. Mobile Banking (M-Banking): Performing deposits, withdrawals, and bill payments instantly via smartphones.\n3. Agency Banking: Accrediting retail shops, supermarkets, and pharmacies as bank agents to provide basic deposit/withdrawal services in rural communities.\n4. Plastic Cards: Debit cards (ATM Visa/Mastercard) and credit cards enabling cashless point-of-sale payments.\n5. Automated Teller Machines (ATMs): 24/7 self-service kiosks for cash withdrawals, deposits, and statement inquiries."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "6-Step Calculation: Foreign Exchange Conversion (Standard Case)",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Example: Multi-Currency Vehicle Importation (200,000 Dirams)",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Identify Given Information", "description": "Cost of imported car = 200,000 UAE Dirams. Exchange Rate 1: 4 Dirams = 1 US Dollar (USD). Exchange Rate 2: 1 USD = Kshs. 70."},
                            {"title": "Step 2: Identify What is Required", "description": "Calculate the total cost that the importer (Wambua) must pay in Kenya Shillings (Kshs)."},
                            {"title": "Step 3: State the Formula", "description": "Cost in USD = Cost in Dirams ÷ 4; Cost in Kshs = Cost in USD × 70."},
                            {"title": "Step 4: Substitute & Compute", "description": "Cost in USD = 200,000 ÷ 4 = 50,000 USD. Cost in Kshs = 50,000 × 70 = Kshs. 3,500,000."},
                            {"title": "Step 5: Check via Cross Rate", "description": "Direct Exchange Rate = 70 ÷ 4 = Kshs. 17.5 per Diram. Total Cost = 200,000 × 17.5 = Kshs. 3,500,000."},
                            {"title": "Step 6: Economic Interpretation", "description": "Wambua must pay exactly Kshs. 3,500,000 (3.5 million shillings) to purchase and clear the vehicle from Dubai."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "6-Step Calculation: Foreign Exchange (Literal Digit Variant)",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Example: Equipment Spare Part Conversion (20,000 Dirams)",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Identify Given Information", "description": "Spare part cost = 20,000 Dirams. Exchange rates: 4 Dirams = 1 USD; 1 USD = Kshs. 70."},
                            {"title": "Step 2: Identify What is Required", "description": "Calculate the cost in Kenya Shillings under the 20,000 Dirams figure."},
                            {"title": "Step 3: State the Formula", "description": "Cost in USD = Dirams ÷ 4; Cost in Kshs = USD × 70."},
                            {"title": "Step 4: Substitute & Compute", "description": "USD = 20,000 ÷ 4 = 5,000 USD. Kshs = 5,000 × 70 = Kshs. 350,000."},
                            {"title": "Step 5: Check via Cross Rate", "description": "20,000 Dirams × Kshs. 17.5/Diram = Kshs. 350,000."},
                            {"title": "Step 6: Economic Interpretation", "description": "Under this value, the imported part costs Kshs. 350,000 in local currency."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Intermediate & KCSE Budget Deficit Calculation",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "KCSE Examination Problem: Foreign Exchange & Budget Deficit",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Information", "description": "Luxury SUV price = 240,000 Dirams. Wambua's bank balance = Kshs. 4,000,000. Exchange rates: 4 Dirams = 1 USD; 1 USD = Kshs. 70."},
                            {"title": "Step 2: Required", "description": "a) Calculate SUV cost in Kshs. b) Determine if Wambua has sufficient funds and calculate surplus or deficit."},
                            {"title": "Step 3: Formula", "description": "Cost in Kshs = (Dirams ÷ 4) × 70; Balance Difference = Bank Balance - Cost in Kshs."},
                            {"title": "Step 4: Substitute & Compute", "description": "Cost in Kshs = (240,000 ÷ 4) × 70 = 60,000 × 70 = Kshs. 4,200,000. Difference = 4,000,000 - 4,200,000 = -Kshs. 200,000."},
                            {"title": "Step 5: Verification", "description": "Cross rate check: 240,000 × 17.5 = 4,200,000. Required funds exceed bank balance by 200,000."},
                            {"title": "Step 6: Economic Conclusion", "description": "Wambua does not have enough funds; he faces a financial deficit of Kshs. 200,000."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Paper 1 Short-Answer Practice",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Paper 1 Short-Answer Questions & Model Answers",
                    "content": {
                        "text": "Question 1: Highlight four differences between a savings account and a current account.\n- Model Answer: (1) Current accounts use cheques, savings use cards/slips; (2) Current accounts offer overdrafts, savings do not; (3) Savings accounts earn interest, current accounts do not; (4) Current accounts incur ledger fees, savings accounts require minimum balances.\n\nQuestion 2: State four functions of the Central Bank of Kenya.\n- Model Answer: (1) Sole issuer of currency; (2) Banker to the government; (3) Banker to commercial banks; (4) Formulating and implementing monetary policy."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Paper 2 Essay Model Answers",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Paper 2 Essay Questions & Model Answers",
                    "content": {
                        "text": "Essay Question: Discuss five monetary measures the Central Bank of Kenya can implement to curb demand-pull inflation.\n\nModel Answer:\n1. Raise the Bank Rate: CBK increases the rate at which it lends to commercial banks. Banks pass this cost to borrowers by hiking loan rates, reducing public borrowing and consumer spending.\n2. Open Market Operations (OMO): CBK sells Treasury bills/bonds to the public. Savers purchase these with bank deposits, draining liquidity from banks and shrinking lending capacity.\n3. Increase the Cash Reserve Ratio (CRR): CBK raises the percentage of deposits banks must keep as cash reserves at CBK vaults, restricting the credit multiplier.\n4. Apply Moral Suasion: CBK appeals to and persuades commercial bank managers to voluntarily freeze or restrict speculative credit expansion.\n5. Issue Directives (Credit Ceilings): CBK sets mandatory maximum lending limits on commercial banks to cap total money supply."
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Central Banking & Foreign Exchange",
                    "content": {
                        "question": "If 4 UAE Dirams = 1 USD and 1 USD = Kshs. 70, how much will an imported generator priced at 40,000 Dirams cost in Kenya Shillings?",
                        "options": [
                            {"id": "a", "text": "Kshs. 160,000"},
                            {"id": "b", "text": "Kshs. 700,000", "correct": True, "feedback": "Correct! 40,000 ÷ 4 = 10,000 USD. 10,000 × 70 = Kshs. 700,000."},
                            {"id": "c", "text": "Kshs. 2,800,000"},
                            {"id": "d", "text": "Kshs. 400,000"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 8 Summary",
                    "content": {
                        "text": "The Central Bank of Kenya regulates currency, acts as banker to the government and banks, and controls credit using bank rates, OMO, and cash ratios. Modern banking has been revolutionized by mobile money, agency banking, and electronic transfers."
                    }
                }
            ]
        }
    ]
}
