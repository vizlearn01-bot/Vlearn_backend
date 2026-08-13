"""
VLearn Form 4 Business Studies — Topic 5: Inflation
Authoritative Pedagogical Data Structures for 3 Lessons (30 Pages).
"""

from curriculum.ingest_form4_business_studies_topic5_svgs import (
    SVG_CPI_CALCULATION_PIPELINE,
    SVG_INFLATION_LEVELS_GAUGE,
    SVG_DEMAND_PULL_VS_COST_PUSH_PATHWAYS,
    SVG_INFLATION_WINNERS_LOSERS_MATRIX,
    SVG_INFLATION_CONTROL_POLICIES_TREE
)

# Verified Wikimedia photographic assets
IMG_FRESH_PRODUCE_MARKET = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Wangige open-air vegetable market in Kiambu, illustrating retail food pricing, household consumption baskets, and Consumer Price Index (C.P.I.) monitoring.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_CENTRAL_BANK_MONETARY = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Central Bank of Kenya regulatory operations, illustrating bank lending rate adjustments, open market bond sales, and monetary credit control.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

IMG_FUEL_LOGISTICS_TRANSPORT = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
    "text": "Transport and logistics network in Kenya, demonstrating fuel input costs, freight tariffs, and cost-push inflation transmission.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
}

IMG_JUA_KALI_MANUFACTURING = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "Jua Kali manufacturing workshop in Nairobi, illustrating raw material expenses, wage pressures, and production margin squeezes.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

# ==============================================================================
# LESSON 1: MEANING AND MEASUREMENT OF INFLATION (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Meaning and Measurement of Inflation",
    "lesson_title": "Purchasing Power Erosion, Consumer Price Index, and Standard of Living Math",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define inflation and deflation, explain the purpose and construction steps of the Consumer Price Index (C.P.I.), calculate relative price indices and simple average C.P.I., and interpret C.P.I. calculations in terms of purchasing power and real income."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Measuring Inflation Matters",
                    "content": {
                        "text": "If you had Sh. 100 in Kenya ten years ago, that note could buy a substantial basket of household goods. Today, that exact same Sh. 100 note might only buy a loaf of bread and a small packet of milk. The physical paper note is identical, but its real value has shrunk. This erosion of what your money can buy is called inflation. Measuring inflation is vital for households planning budgets, trade unions negotiating wages, and governments setting national economic policies."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Meaning of Inflation and Deflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Inflation and Deflation",
                    "content": {
                        "term": "Inflation",
                        "definition": "A persistent or continuous rise in the general price level of goods and services in an economy over a given period of time, leading to a decline in the purchasing power of money."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Deflation",
                    "content": {
                        "term": "Deflation",
                        "definition": "The exact opposite of inflation; a situation where the general price levels of goods and services in an economy are persistently falling over time."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Consumer Price Index (C.P.I.)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "What is the C.P.I.?",
                    "content": {
                        "text": "Because prices do not all rise at the exact same rate—some double, others rise slightly, and a few fall—economists use the Consumer Price Index (C.P.I.) to measure average price movements. The C.P.I. compares the cost of a representative consumer basket of goods between a base year and a current year, tracking changes in consumer purchasing power."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Retail Commodity Basket Monitoring",
                    "content": IMG_FRESH_PRODUCE_MARKET
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Five Steps in Constructing the C.P.I.",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Procedural Steps for Constructing the C.P.I.",
                    "content": {
                        "text": "1. Selection of Commodities: Pick a representative basket of goods consumed by average households (e.g. maize flour, rent, fuel, transport, soap).\n2. Selection of the Base Year: Choose a normal, economically stable year (free of severe droughts, wars, or election crises) and assign it a base index of 100.\n3. Collection of Current Market Prices: Gather current retail prices across major national markets.\n4. Calculation of Relative Price Indices: For each item, compute Price Index = (Current Price / Base Price) * 100.\n5. Calculation of Simple Average C.P.I.: Sum individual price indices and divide by the number of commodities (N)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Procedural Pipeline for C.P.I. Construction",
                    "svg_content": SVG_CPI_CALCULATION_PIPELINE,
                    "content": {
                        "text": "5-step procedural pipeline diagram for constructing and calculating the Consumer Price Index."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Mathematical Formulas for C.P.I.",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "C.P.I. & Inflation Rate Formulas",
                    "content": {
                        "text": "• Individual Commodity Relative Price Index:\n  Index = (Price in Current Year / Price in Base Year) * 100\n\n• Simple Average Consumer Price Index (C.P.I.):\n  Simple Average C.P.I. = Sum of Individual Price Indices / Number of Commodities (N)\n\n• Average Inflation Rate (%):\n  Inflation Rate = Simple Average C.P.I. - 100"
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Calculation 1: Five Household Commodities",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "6-Step C.P.I. Calculation (Five Commodities)",
                    "content": {
                        "text": "Problem: Market prices of five commodities in Base Year and Current Year are:\nBread: Base Sh. 16 | Current Sh. 20\nSugar: Base Sh. 40 | Current Sh. 60\nSalt: Base Sh. 10 | Current Sh. 12\nRice: Base Sh. 20 | Current Sh. 40\nMaize: Base Sh. 48 | Current Sh. 60\nCalculate the Simple Average C.P.I. and interpret the inflation rate.\n\nSolution:\nStep 1: Relative Price Indices:\n- Bread = (20 / 16) * 100 = 125\n- Sugar = (60 / 40) * 100 = 150\n- Salt = (12 / 10) * 100 = 120\n- Rice = (40 / 20) * 100 = 200\n- Maize = (60 / 48) * 100 = 125\nStep 2: Sum of Indices = 125 + 150 + 120 + 200 + 125 = 720.\nStep 3: Simple Average C.P.I. = 720 / 5 = 144.\nStep 4: Inflation Rate = 144 - 100 = 44%.\nStep 5: Interpretation = A consumer now requires Sh. 144 to buy the exact same basket that cost Sh. 100 in the base year. Purchasing power has fallen by 44%."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Worked Calculation 2: Township Real Income Drop",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "C.P.I. Impact on Fixed Salary Earner",
                    "content": {
                        "text": "Problem: Prices of three commodities between 2022 and 2025:\nItem A: Base Sh. 80 | Current Sh. 104\nItem B: Base Sh. 150 | Current Sh. 180\nItem C: Base Sh. 200 | Current Sh. 300\nCompute C.P.I. and explain the economic implication for a worker earning a fixed monthly salary of Sh. 20,000.\n\nSolution:\nStep 1: Indices: Item A = (104/80)*100 = 130; Item B = (180/150)*100 = 120; Item C = (300/200)*100 = 150.\nStep 2: Sum = 130 + 120 + 150 = 400.\nStep 3: Simple Average C.P.I. = 400 / 3 = 133.33.\nStep 4: Inflation Rate = 33.33%.\nStep 5: Implication = Prices rose by 33.33% while the salary remained Sh. 20,000. To maintain the 2022 standard of living, the worker needs Sh. 26,666 (20,000 * 1.3333). Since salary is still Sh. 20,000, real purchasing power drops by 25%."
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
                        "text": "Inflation is a persistent general price rise, while deflation is a persistent fall. We measure inflation using the Consumer Price Index (C.P.I.), setting the base year index to 100. A C.P.I. of 144 means general prices rose by 44% and purchasing power declined."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: C.P.I. Calculation Errors",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Never Add Prices Directly",
                    "content": {
                        "text": "1. Do NOT add current prices directly and divide by base prices! You must calculate the individual relative price index for EACH commodity first, and then find the simple average of those indices.\n2. A C.P.I. of 144 does NOT mean every single commodity rose by 44%. Some items (like Rice) rose by 100% (index 200), while others (like Salt) rose by 20% (index 120). The C.P.I. represents average economic pressure."
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
                        "question": "If an economy's simple average Consumer Price Index (C.P.I.) for 2024 is calculated as 165 using 2020 as the base year, what is the rate of inflation?",
                        "options": [
                            "165%",
                            "65%",
                            "35%",
                            "100%"
                        ],
                        "correct_answer": "65%",
                        "explanation": "The inflation rate is C.P.I. minus base year index (165 - 100 = 65%). General prices have risen by 65% since the base year."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: TYPES AND CAUSES OF INFLATION (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Types and Causes of Inflation",
    "lesson_title": "Inflation Strains, Demand-Pull Drivers, and Cost-Push Factors",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Inflation Types",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to distinguish between three levels of inflation (mild, galloping, hyper-inflation), define demand-pull inflation and identify its causes, and define cost-push inflation and identify its causes."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Diagnosing Causes Matters",
                    "content": {
                        "text": "Just as a doctor must diagnose whether a patient has a viral infection or bacterial illness before prescribing medicine, governments must diagnose whether inflation is caused by excess money (demand-pull) or rising production expenses (cost-push). Applying the wrong policy will worsen the crisis!"
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Three Levels (Strains) of Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Strains of Inflation",
                    "content": {
                        "text": "1. Creeping / Mild Inflation: Slow, gradual price rise with an annual rate below 10%. Low disruption; motivates businesses to produce more.\n2. Galloping / Rapid Inflation: Rapid rise in tens or hundreds of percent annually (e.g. 20%, 50%, 150%). Money loses purchasing power rapidly; severe consumer strain.\n3. Hyper-inflation: Astronomical runaway price increases climbing into thousands or millions of percent per year. Currency becomes worthless; monetary system collapses!"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Levels of Inflation Gauge",
                    "svg_content": SVG_INFLATION_LEVELS_GAUGE,
                    "content": {
                        "text": "Gauge diagram visualizing mild, galloping, and hyper-inflation levels."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Demand-Pull Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "What is Demand-Pull Inflation?",
                    "content": {
                        "text": "Demand-pull inflation occurs when aggregate demand for goods and services exceeds aggregate supply under full employment: 'Too much money chasing too few goods.' When consumers have cash but shops have limited stock, consumers bid against one another, pulling prices upward."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Main Causes of Demand-Pull Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Four Demand-Pull Causes",
                    "content": {
                        "text": "1. Excessive Credit Creation: Cheap commercial bank lending floods the economy with credit, expanding consumer spending.\n2. Increased Government Spending: State expenditure on infrastructure or civil service wages injects massive cash without immediate tax increases.\n3. Increased Disposable Income: Wage increases or income tax cuts leave more cash in consumer pockets.\n4. General Supply Shortages: Droughts, floods, hoarding by speculative traders, or industrial technology breakdowns drop aggregate supply."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Cost-Push Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "What is Cost-Push Inflation?",
                    "content": {
                        "text": "Cost-push inflation occurs when general price levels rise because the costs of production inputs increase. Even if consumer demand is flat, businesses are forced to raise selling prices to cover higher expenses and maintain profit margins."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Demand-Pull vs Cost-Push Pathways",
                    "svg_content": SVG_DEMAND_PULL_VS_COST_PUSH_PATHWAYS,
                    "content": {
                        "text": "Flowchart contrasting demand-pull and cost-push macroeconomic pathways."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Main Causes of Cost-Push Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Five Cost-Push Causes",
                    "content": {
                        "text": "1. Rising Labor Costs (Wages): Trade union wage hikes exceeding worker productivity pass labor costs to consumers.\n2. Increased Indirect Taxes: VAT or excise duty increases are treated as business operating costs and passed to retail shelf prices.\n3. Rising Non-Labor Input Costs: Skyrocketing prices of imported crude oil, fertilizers, or industrial machinery raise transport and factory costs.\n4. Monopoly Profit Margins: Monopolistic cartels collude to hike profit margins directly.\n5. Reduced Government Subsidies: Withdrawing subsidies on electricity or fuel forces producers to face full market costs."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Fuel and Transport Cost Transmission",
                    "content": IMG_FUEL_LOGISTICS_TRANSPORT
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Demand-Pull vs Cost-Push Comparison",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Demand-Pull vs. Cost-Push Inflation",
                    "content": {
                        "headers": ["Feature", "Demand-Pull Inflation", "Cost-Push Inflation"],
                        "rows": [
                            ["Primary Trigger", "Excessive aggregate demand and spending cash", "Skyrocketing costs of production inputs"],
                            ["State of Supply", "Limited supply relative to high demand", "Decreased supply due to high production expenses"],
                            ["Typical Drivers", "Cheap credit creation, government spending, tax cuts", "Rising crude oil prices, VAT hikes, wage demands, subsidy cuts"],
                            ["Key Mechanism", "Consumers bid prices up", "Producers push prices up to cover costs and margins"]
                        ]
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
                        "text": "Mild inflation (<10%) motivates business expansion; hyper-inflation causes monetary collapse. Demand-pull is driven by excess consumer spending ('too much money chasing too few goods'); cost-push is driven by rising production expenses."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Dual Role of Wages",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Wages in Inflation",
                    "content": {
                        "text": "Wages appear under BOTH types of inflation! If rising wages give consumers more cash to spend (pulling demand up), it is Demand-Pull. If rising wage bills make factory operations expensive (forcing factory owners to raise wholesale prices), it is Cost-Push."
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
                        "question": "When petrol and diesel prices jump due to a new fuel levy, causing matatu fares and retail food prices to rise across Kenya, what type of inflation is occurring?",
                        "options": [
                            "Demand-Pull Inflation",
                            "Cost-Push Inflation",
                            "Hyper-inflation",
                            "Deflation"
                        ],
                        "correct_answer": "Cost-Push Inflation",
                        "explanation": "Rising fuel prices increase non-labor input and transport costs for producers and transporters, who pass the expenses forward through higher fares and prices."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: EFFECTS AND CONTROL OF INFLATION (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Effects and Control of Inflation",
    "lesson_title": "Stakeholder Distribution, Policy Mitigation, and KCSE Examination Mastery",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Inflation Effects and Policies",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to discuss negative and positive effects of inflation on stakeholders, explain monetary, fiscal, and direct cost-control policy measures, and match policy tools to specific types of inflation."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Policy Choice Matters",
                    "content": {
                        "text": "Persistent inflation eats away savings, devalues salaries, and ruins business planning. However, because mild inflation can stimulate employment and benefit debtors, control policies must be targeted carefully to stabilize prices without choking economic growth."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Nine Negative Effects of Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Negative Macroeconomic Consequences",
                    "content": {
                        "text": "1. Loss of Confidence in Money: Citizens refuse to hold devalued cash.\n2. Growth Retardation: Unpredictable future costs cause investors to postpone capital projects.\n3. Reduced Profits: Margin squeezes when input costs rise faster than consumer spending power.\n4. Time Wastage: Consumers waste time searching for lower prices ('shoe-leather costs').\n5. Wage Disputes: Real wage drops trigger labor strikes and wage-price spirals.\n6. Losses to Creditors: Lenders are repaid in devalued cash.\n7. Discouraged Savings: Inflation rates exceeding bank deposit interest rates erode real savings.\n8. Adverse Balance of Payments: Expensive domestic exports fall while cheap imports rise, worsening trade deficits.\n9. System Collapse: Extreme hyperinflation leads to total breakdown of the monetary system."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Four Positive Effects of Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Positive Effects & Beneficiaries",
                    "content": {
                        "text": "1. Debtors Gain: Borrowers repay fixed loans in 'cheaper' devalued currency.\n2. Traders / Stockists Gain: Stockists holding pre-bought inventory earn windfall profits by selling at new higher market prices.\n3. Motivation to Work: Rising prices motivate individuals to work harder or take extra jobs to maintain living standards.\n4. Job Expansion: Mild inflation stimulates aggregate demand, encouraging short-term factory employment expansion."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Inflation Distribution: Losers vs Winners",
                    "svg_content": SVG_INFLATION_WINNERS_LOSERS_MATRIX,
                    "content": {
                        "text": "Matrix comparing net losers (creditors, savers, fixed earners) vs net winners (debtors, stockists, asset owners)."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Three Policy Pillars for Controlling Inflation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Policy Control Pillars",
                    "content": {
                        "text": "1. Monetary Policies (Managed by CBK): Reduce money supply to curb Demand-Pull inflation (raise bank lending rates, Open Market Operations bond sales, raise cash reserve ratio, moral suasion).\n2. Fiscal Policies (Managed by Treasury): Reduce aggregate demand (raise direct income taxes, cut non-essential government spending, restrict hire purchase credit).\n3. Direct Cost Controls (Target Input Expenses): Control Cost-Push inflation (enforce wage freezes/restraints, lower VAT and tariffs on raw materials/fuel, restrict costly imports)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Three Policy Pillars Tree",
                    "svg_content": SVG_INFLATION_CONTROL_POLICIES_TREE,
                    "content": {
                        "text": "Tree diagram mapping monetary policies, fiscal policies, and direct cost controls."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Monetary Policy in Practice",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Central Bank Credit Control Operations",
                    "content": IMG_CENTRAL_BANK_MONETARY
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Matching Policies to Inflation Types",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Policy Tool Matching Matrix",
                    "content": {
                        "headers": ["Inflation Type", "Target Problem", "Primary Policy Tools"],
                        "rows": [
                            ["Demand-Pull Inflation", "Excess money supply & spending", "CBK Bank rate hikes, OMO bond sales, Cash ratio hikes, Income tax increases, Govt spending cuts"],
                            ["Cost-Push Inflation", "Rising production input costs", "Wage freezes/restraints, Subsidizing inputs, Lowering VAT on raw materials, Restricting costly imports"]
                        ]
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
                        "text": "Inflation harms creditors, savers, and fixed earners while benefiting debtors and stockists. Monetary and fiscal contraction curbs Demand-Pull inflation; direct cost controls and input tax cuts target Cost-Push inflation."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Real-World Application: Fuel Cost Inflation Policy",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Policy Choice Case Study",
                    "content": {
                        "text": "If Kenya faces inflation driven by skyrocketing imported crude oil, raising income taxes (fiscal contraction) is ineffective because consumers are not driving the price rise. The correct policy is Direct Cost Control: lowering fuel import tariffs or subsidizing diesel to lower production and transport expenses!"
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
                        "text": "1. Base Year Selection Criteria: Stable prices, normal climatic conditions, political stability, recent year.\n2. Demand-Pull vs Cost-Push: Demand-pull is driven by excess money demand; Cost-push is driven by input expense increases.\n3. Monetary Tools: Bank rate hikes, OMO bond sales, cash ratio increases, liquidity ratio increases.\n4. Victims of Inflation: Fixed-wage earners, creditors, cash savers, pensioners."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Which group of economic stakeholders gains positive windfall benefits during a period of high inflation?",
                        "options": [
                            "Creditors and Lenders",
                            "Debtors and Stockists with pre-bought inventory",
                            "Fixed-salary Civil Servants",
                            "Retirees living on fixed monthly pensions"
                        ],
                        "correct_answer": "Debtors and Stockists with pre-bought inventory",
                        "explanation": "Debtors repay fixed loans in cheaper devalued money, while stockists sell pre-bought inventory at new higher market prices."
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
                    "component_type": "worked_example",
                    "title": "KCSE Paper 2 4-Commodity C.P.I. & Economic Analysis",
                    "content": {
                        "text": "Problem: Commodity prices between 2021 and 2024:\nCooking Oil: 150 -> 180 | Laundry Soap: 100 -> 130 | Charcoal: 80 -> 120 | Wheat Flour: 120 -> 156.\na) Calculate relative price indices. b) Determine Simple Average C.P.I. c) Discuss three negative macroeconomic effects.\n\nSolution:\na) Indices: Cooking Oil = (180/150)*100 = 120; Soap = (130/100)*100 = 130; Charcoal = (120/80)*100 = 150; Flour = (156/120)*100 = 130.\nb) Sum = 120 + 130 + 150 + 130 = 530. C.P.I. = 530 / 4 = 132.5. Inflation Rate = 32.5%.\nc) Negative Effects:\n1. Retardation of Growth: High energy (charcoal) and food costs create business cost uncertainty, slowing long-term capital investment.\n2. Adverse Balance of Payments: 32.5% domestic inflation makes exports expensive, worsening the trade deficit.\n3. Discouraged Domestic Savings: Inflation (32.5%) exceeds bank deposit interest rates, eroding real savings."
                    }
                }
            ]
        }
    ]
}

TOPIC5_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA
]
