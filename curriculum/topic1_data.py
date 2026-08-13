"""
VLearn Form 4 Business Studies — Topic 1: National Income
Pedagogical Lesson & Page Data Definitions
8 Lessons, 78 Pages, ~240 Granular Blocks
"""

from curriculum.ingest_form4_business_studies_topic1_svgs import (
    SVG_NATIONAL_INCOME_HIERARCHY,
    SVG_CIRCULAR_FLOW_MODEL,
    SVG_EQUILIBRIUM_SCALE,
    SVG_VALUE_ADDED_CHAIN,
    SVG_FACTORS_INFLUENCING_NI
)

# =============================================================================
# LESSON 1: Meaning and Related National-Income Terms (10 Pages)
# =============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Meaning and Related National-Income Terms",
    "lesson_title": "National Income Concepts, Measures, and Per Capita Income",
    "pages": [
        # Page 1: Introduction & Learning Goals
        {
            "page_number": 1,
            "page_title": "The Economic Cake: What is National Income?",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define the term **National Income** and explain why it equals national output and national product\n"
                            "- Distinguish between **Domestic** and **National** economic boundaries\n"
                            "- Distinguish between **Gross** and **Net** economic measures\n"
                            "- Compute and interpret **GDP, NDP, GNP, NNP, and Per Capita Income** using standard 6-step working\n"
                            "- Apply the concepts to solve KCSE examination questions"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why National Income Matters",
                    "content": {
                        "text": (
                            "Imagine you are managing a household. To plan your annual budget, you need to know exactly how much income your family earns. "
                            "Similarly, the government needs to know the total monetary value of all goods and services produced in the country to make decisions "
                            "about healthcare, infrastructure, education, and social amenities.\n\n"
                            "National income statistics reveal the true size of a country's **economic cake** and show whether the economy is expanding or contracting over time."
                        )
                    }
                }
            ]
        },
        # Page 2: Definition of National Income & Equivalence
        {
            "page_number": 2,
            "page_title": "Core Definition and the Threefold Equivalence",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "National Income",
                    "content": {
                        "term": "National Income",
                        "definition": "The total monetary value of all final goods and services produced in an economy over a given period, usually one year, or the total income received by the owners of the factors of production."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Fundamental Triple Equivalence",
                    "content": {
                        "text": (
                            "In national accounting, the following three expressions refer to the exact same total sum:\n\n"
                            "$$\\text{National Income} \\equiv \\text{National Output} \\equiv \\text{National Product}$$\n\n"
                            "**Why are they equivalent?**\n"
                            "1. **National Output:** What the country physically produces (tea, maize, banking services, manufactured goods).\n"
                            "2. **National Product / Expenditure:** The market value of all goods and services purchased by consumers, firms, and the government.\n"
                            "3. **National Income:** The factor rewards (rent, wages, interest, profit) paid out to the owners of land, labour, capital, and entrepreneurship who produced that output.\n\n"
                            "Because every shilling spent on final output becomes income for the producers, total output must equal total income."
                        )
                    }
                }
            ]
        },
        # Page 3: Real-World Visual
        {
            "page_number": 3,
            "page_title": "The Commercial Engine of National Output",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Commercial and Financial Center in Nairobi",
                    "content": {
                        "text": "The Nairobi commercial and financial skyline, representing the hub of corporate services, banking, and commercial output contributing to Kenya's Gross Domestic Product.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                        "author": "Wikimedia Commons / CC-BY-SA",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Maasai_Market-Nairobi.jpg"
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Key Accounting Principle",
                    "content": {
                        "text": "National income measures current economic activity over a specified period (normally 12 months). It only includes newly produced goods and services and strictly excludes purely financial transfers or sales of second-hand goods."
                    }
                }
            ]
        },
        # Page 4: Two Key Distinctions: Domestic vs National, Gross vs Net
        {
            "page_number": 4,
            "page_title": "Two Core Distinctions: Boundaries and Wear-and-Tear",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Domestic vs National, Gross vs Net Dimensions",
                    "content": {
                        "headers": ["Dimension", "First Concept", "Second Concept", "Key Distinguishing Rule"],
                        "rows": [
                            ["Geographic vs Citizenship", "Domestic (e.g. GDP, NDP)", "National (e.g. GNP, NNP)", "Domestic is based on geography (inside Kenyan borders). National is based on citizenship/ownership (Kenyan residents anywhere)."],
                            ["Wear-and-Tear (Depreciation)", "Gross (e.g. GDP, GNP)", "Net (e.g. NDP, NNP)", "Gross includes total production before capital consumption. Net deducts the value of depreciation (wear and tear on machines/buildings)."]
                        ]
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Connecting the Concepts: Net Factor Income from Abroad",
                    "content": {
                        "text": (
                            "To move from **Domestic** to **National**, we adjust for international cross-border factor income flows:\n\n"
                            "$$\\text{GNP} = \\text{GDP} + \\text{Net Factor Income from Abroad}$$"
                            "\n\nWhere **Net Factor Income from Abroad (NFIA)** is:\n"
                            "$$\\text{NFIA} = \\text{Factor Income Earned by Citizens Abroad} - \\text{Factor Income Paid to Foreigners Locally}$$\n\n"
                            "If foreign investors in Kenya take out more profits than Kenyans working abroad send back home, NFIA is **negative**, making GNP smaller than GDP."
                        )
                    }
                }
            ]
        },
        # Page 5: Diagrammatic Flow
        {
            "page_number": 5,
            "page_title": "Visualizing the National Income Aggregates",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "National Income Aggregates Hierarchy and Formula Transitions",
                    "svg_content": SVG_NATIONAL_INCOME_HIERARCHY,
                    "content": {
                        "text": "Diagram showing formula transitions between GDP, GNP, NDP, NNP, and Per Capita Income."
                    }
                },
                {
                    "block_type": "memory_tip",
                    "component_type": "memory_tip",
                    "title": "Memory Rule for Formulas",
                    "content": {
                        "text": "• To switch from Domestic to National: Add Net Factor Income from Abroad (+ NFIA).\n• To switch from Gross to Net: Subtract Depreciation (- Depreciation)."
                    }
                }
            ]
        },
        # Page 6: Per Capita Income Explained
        {
            "page_number": 6,
            "page_title": "Per Capita Income: Measuring the Average Slice",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Per Capita Income",
                    "content": {
                        "term": "Per Capita Income",
                        "definition": "The average income per head of population in a country in a given year, calculated by dividing the national income by the total population."
                    }
                },
                {
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "title": "Per Capita Income Formula",
                    "content": {
                        "formula": "\\text{Per Capita Income} = \\frac{\\text{National Income (NNP)}}{\\text{Total Population}}",
                        "breakdown": "- **National Income (NNP)**: Total net output produced by citizens of the country (in KSh).\n- **Total Population**: Total number of citizens living in the country.\n- **Result**: Average annual income earned per citizen."
                    }
                },
                {
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "title": "Misconception: Per Capita Income Equals Actual Income",
                    "content": {
                        "text": "Per capita income is purely a mathematical average. It does NOT mean that every person receives this exact amount. In economies with severe income inequality, a tiny wealthy elite may earn billions while the vast majority live below the calculated per capita figure."
                    }
                }
            ]
        },
        # Page 7: Worked Calculation 1 (Guided)
        {
            "page_number": 7,
            "page_title": "Worked Example 1: Calculating NDP, GNP, and NNP",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Guided Step-by-Step National Income Calculation",
                    "content": {
                        "intro": "The following economic figures are provided for a country in the year 2025 (all figures in KSh millions):",
                        "steps": [
                            "**Step 1 — Identify Given Information:**\n- $\\text{Gross Domestic Product (GDP)} = \\text{KSh } 800,000\\text{ million}$\n- $\\text{Depreciation} = \\text{KSh } 50,000\\text{ million}$\n- $\\text{Factor Income Received from Abroad} = \\text{KSh } 30,000\\text{ million}$\n- $\\text{Factor Income Paid to Foreigners} = \\text{KSh } 50,000\\text{ million}$\n- $\\text{Total Population} = 40\\text{ million people}$",
                            "**Step 2 — Identify What is Required:**\nCalculate:\na) Net Domestic Product (NDP)\nb) Gross National Product (GNP)\nc) Net National Product (NNP)\nd) Per Capita Income",
                            "**Step 3 — State the Relevant Relationships:**\n- $\\text{NDP} = \\text{GDP} - \\text{Depreciation}$\n- $\\text{NFIA} = \\text{Income from Abroad} - \\text{Income Paid Abroad}$\n- $\\text{GNP} = \\text{GDP} + \\text{NFIA}$\n- $\\text{NNP} = \\text{GNP} - \\text{Depreciation}$\n- $\\text{Per Capita Income} = \\text{NNP} \\div \\text{Population}$",
                            "**Step 4 — Substitute Values & Compute:**\na) $\\text{NDP} = 800,000 - 50,000 = \\mathbf{750,000\\text{ million KSh}}$\nb) $\\text{NFIA} = 30,000 - 50,000 = -20,000\\text{ million KSh}$\n   $\\text{GNP} = 800,000 + (-20,000) = \\mathbf{780,000\\text{ million KSh}}$\nc) $\\text{NNP} = 780,000 - 50,000 = \\mathbf{730,000\\text{ million KSh}}$\nd) $\\text{Per Capita Income} = \\frac{730,000\\text{ million}}{40\\text{ million}} = \\mathbf{\\text{KSh } 18,250}$",
                            "**Step 5 — Check Using Alternative Accounting Path:**\n$\\text{NNP} = \\text{NDP} + \\text{NFIA} = 750,000 + (-20,000) = 730,000\\text{ million KSh}$. Both calculation paths yield identical results!",
                            "**Step 6 — Economic Interpretation:**\nThe country produced KSh 730,000 million worth of net value for its citizens after accounting for capital wear and tear and international payments. On average, each citizen shares KSh 18,250 of this annual national income."
                        ]
                    }
                }
            ]
        },
        # Page 8: Worked Calculation 2 (KCSE Exam Scenario)
        {
            "page_number": 8,
            "page_title": "Worked Example 2: KCSE Multi-Variable Problem",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Multi-Step Examination Problem",
                    "content": {
                        "intro": "The following data relates to the national income records of Country Z for the year ended 31 December 2025:\n\n- Net Domestic Product (NDP) = KSh 600,000 million\n- Depreciation = KSh 45,000 million\n- Exports of factor services = KSh 80,000 million\n- Imports of factor services = KSh 95,000 million\n- Total Population = 50 million people\n\nCalculate GDP, GNP, NNP, and Per Capita Income.",
                        "steps": [
                            "**Step 1: Calculate Gross Domestic Product (GDP):**\nSince $\\text{NDP} = \\text{GDP} - \\text{Depreciation}$, rearranging gives:\n$$\\text{GDP} = \\text{NDP} + \\text{Depreciation} = 600,000 + 45,000 = \\mathbf{645,000\\text{ million KSh}}$$",
                            "**Step 2: Calculate Gross National Product (GNP):**\n$$\\text{Net Factor Income from Abroad} = \\text{Exports} - \\text{Imports} = 80,000 - 95,000 = -15,000\\text{ million KSh}$$\n$$\\text{GNP} = \\text{GDP} + \\text{NFIA} = 645,000 + (-15,000) = \\mathbf{630,000\\text{ million KSh}}$$",
                            "**Step 3: Calculate Net National Product (NNP):**\n$$\\text{NNP} = \\text{GNP} - \\text{Depreciation} = 630,000 - 45,000 = \\mathbf{585,000\\text{ million KSh}}$$",
                            "**Step 4: Calculate Per Capita Income:**\n$$\\text{Per Capita Income} = \\frac{585,000\\text{ million}}{50\\text{ million}} = \\mathbf{\\text{KSh } 11,700}$$",
                            "**Step 5: Interpretation:**\nBecause Country Z paid KSh 15,000 million more to foreign factor owners than its citizens earned abroad, its Gross National Product (KSh 630,000M) is lower than its domestic geographical output (KSh 645,000M)."
                        ]
                    }
                }
            ]
        },
        # Page 9: Formative Knowledge Check
        {
            "page_number": 9,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "National Income Concepts Check",
                    "content": {
                        "question": "A foreign multi-national company manufactures soda in Nairobi and sends all its net profits back to its parent headquarters in the United Kingdom. How is this transaction treated in Kenya's national accounts?",
                        "options": [
                            "It is included in Kenya's GDP and included in Kenya's GNP",
                            "It is included in Kenya's GDP but excluded (subtracted) from Kenya's GNP",
                            "It is excluded from Kenya's GDP but included in Kenya's GNP",
                            "It is excluded from both Kenya's GDP and Kenya's GNP"
                        ],
                        "answer": "B",
                        "explanation": "Because the factory is physically located inside Kenya, the soda production is part of Kenya's Gross Domestic Product (GDP). However, because the profits belong to foreign owners, they represent an outflow of factor income and are deducted from Kenya's Gross National Product (GNP)."
                    }
                },
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Formula True/False Check",
                    "content": {
                        "check_type": "true_false",
                        "question": "True or False: Gross Domestic Product (GDP) minus Depreciation equals Net National Product (NNP).",
                        "answer": "False",
                        "explanation": "False. GDP minus Depreciation equals Net Domestic Product (NDP). To obtain Net National Product (NNP), you must subtract Depreciation from Gross National Product (GNP), or add Net Factor Income from Abroad to NDP."
                    }
                }
            ]
        },
        # Page 10: Lesson Summary & Concept Takeaway
        {
            "page_number": 10,
            "page_title": "Lesson 1 Summary & Key Takeaways",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Key Takeaways: National Income Aggregates",
                    "content": {
                        "text": (
                            "1. National Income equals National Output and National Product due to the circular flow of factor earnings and spending.\n"
                            "2. Domestic measures (GDP, NDP) focus on geographic borders; National measures (GNP, NNP) focus on citizen ownership.\n"
                            "3. Gross measures include wear and tear; Net measures deduct depreciation ($NNP = GNP - \\text{Depreciation}$).\n"
                            "4. Per Capita Income ($NNP \\div \\text{Population}$) is an average indicator and does not reflect individual income distribution."
                        )
                    }
                },
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Mastery Checklist",
                    "content": {
                        "text": (
                            "You have now mastered the foundational vocabulary and mathematical bridges connecting GDP, NDP, GNP, NNP, and Per Capita Income. "
                            "In the next lesson, we will explore how income and resources circulate continuously between households and business firms."
                        )
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# LESSON 2: Circular Flow of Income, Injections and Withdrawals (10 Pages)
# =============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Circular Flow of Income, Injections and Withdrawals",
    "lesson_title": "The Circular Flow Model, Real vs Money Flows, and Leakages & Injections",
    "pages": [
        # Page 1: Introduction & Goals
        {
            "page_number": 1,
            "page_title": "The Circulatory System of the Economy",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Describe the circular flow of income between households and business firms\n"
                            "- Distinguish between the **Real Flow** (factor services & goods) and the **Money Flow** (factor incomes & consumption spending)\n"
                            "- State the five core assumptions of a simple two-sector economy\n"
                            "- Identify and explain the three **Leakages** (Savings, Taxation, Imports) and three **Injections** (Investment, Government Expenditure, Exports)\n"
                            "- Evaluate the macroeconomic impact of changes in injections and withdrawals"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Economic Analogy: Money as Blood",
                    "content": {
                        "text": (
                            "Money in an economy behaves just like blood in a human body: it must circulate continuously between different organs to sustain life. "
                            "If money is pumped into new production, the economy thrives and jobs are created. If money is hoarded or drained out without returning, "
                            "the economic body suffocates into recession and unemployment.\n\n"
                            "The **Circular Flow of Income** model explains how resources, goods, and money continuously move through an economic system."
                        )
                    }
                }
            ]
        },
        # Page 2: Two-Sector Circular Flow (Real Flow vs Money Flow)
        {
            "page_number": 2,
            "page_title": "Real Flow vs. Money Flow in a Two-Sector Economy",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Two Opposing Flows in the Economic Circle",
                    "content": {
                        "text": (
                            "In any modern economy, there are two distinct circular flows moving in opposite directions:\n\n"
                            "1. **The Real Flow (Physical Flow):**\n"
                            "- **Households** supply factor services (land, labour, capital, entrepreneurship) to **Firms**.\n"
                            "- **Firms** use these factors to produce physical goods and services, which flow back to **Households**.\n\n"
                            "2. **The Money Flow (Financial Flow):**\n"
                            "- **Firms** pay factor rewards (wages, rent, interest, profit) to **Households**.\n"
                            "- **Households** spend this income as **Consumption Expenditure ($C$)** buying goods from **Firms**, returning sales revenue."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Circular Flow of Income",
                    "content": {
                        "term": "Circular Flow of Income",
                        "definition": "The continuous movement of income and expenditure between households and firms in an economy through the factor market and product market."
                    }
                }
            ]
        },
        # Page 3: Visual Model of Circular Flow
        {
            "page_number": 3,
            "page_title": "Process Diagram: The Circular Flow of Income",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Circular Flow of Income with Real and Money Flows",
                    "svg_content": SVG_CIRCULAR_FLOW_MODEL,
                    "content": {
                        "text": "Process diagram showing the circular movement of goods, factor services, factor rewards, and consumption spending between households and firms."
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Core Insight",
                    "content": {
                        "text": "The outer financial loop (Money Flow) mirrors the inner physical loop (Real Flow). The total monetary value of factor incomes paid out equals the total market value of goods produced."
                    }
                }
            ]
        },
        # Page 4: Assumptions of the Simple Model
        {
            "page_number": 4,
            "page_title": "Assumptions of the Simple Two-Sector Model",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Five Strict Theoretical Assumptions",
                    "content": {
                        "text": (
                            "To establish the pure circular relationship, economists make five simplified assumptions:\n\n"
                            "1. **Two Sectors Only:** The economy consists only of Households and Business Firms.\n"
                            "2. **Complete Household Spending:** Households spend all their income on goods and services; there are no savings ($S = 0$).\n"
                            "3. **Complete Firm Factor Payout:** Firms spend all their sales revenue paying for factor services supplied by households.\n"
                            "4. **No Government Intervention:** There is no government sector (no taxes collected, no public spending).\n"
                            "5. **Closed Economy:** There is no international trade (no exports or imports with the outside world).\n\n"
                            "**Why these assumptions do not hold in reality:**\n"
                            "- Every modern economy has a government that taxes citizens and spends on public infrastructure.\n"
                            "- Households save money in banks, and firms borrow to invest.\n"
                            "- All countries engage in international trade through imports and exports."
                        )
                    }
                }
            ]
        },
        # Page 5: Leakages / Withdrawals
        {
            "page_number": 5,
            "page_title": "Withdrawals (Leakages) from the Circular Flow",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Withdrawals (Leakages)",
                    "content": {
                        "term": "Withdrawals (Leakages)",
                        "definition": "Any economic diversion or withdrawal of funds from the circular flow of income that reduces the volume of domestic consumption expenditure."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Three Major Leakages ($W = S + T + M$)",
                    "content": {
                        "text": (
                            "1. **Savings ($S$):** Income earned by households that is kept in bank accounts or investments rather than spent on goods produced by firms. This directly reduces sales revenue received by domestic businesses.\n\n"
                            "2. **Taxation ($T$):** Compulsory payments extracted by the government (such as PAYE income tax or VAT) from household earnings, reducing disposable income available for spending.\n\n"
                            "3. **Imports ($M$):** Money spent by domestic citizens buying foreign-made goods (e.g. purchasing electronics from Japan). This money leaks out of the domestic circular flow into foreign economies."
                        )
                    }
                }
            ]
        },
        # Page 6: Injections into the Circular Flow
        {
            "page_number": 6,
            "page_title": "Injections into the Circular Flow",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Injections",
                    "content": {
                        "term": "Injections",
                        "definition": "Any addition of income or spending into the circular flow from sources other than domestic household consumption, which increases the total volume of economic activity."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Three Major Injections ($J = I + G + X$)",
                    "content": {
                        "text": (
                            "1. **Investment ($I$):** Capital expenditure by business firms on new machinery, factories, and equipment using borrowed savings. This pumps income directly to capital goods producers and construction workers.\n\n"
                            "2. **Government Expenditure ($G$):** Public spending on development projects (roads, schools, hospitals) and civil servant salaries, which injects purchasing power directly into households and firms.\n\n"
                            "3. **Exports ($X$):** Revenue earned when foreigners purchase locally produced goods (e.g. Kenyan tea, coffee, flowers). This injects foreign currency into local producers' accounts."
                        )
                    }
                }
            ]
        },
        # Page 7: Comparison Table
        {
            "page_number": 7,
            "page_title": "Comparative Summary: Leakages vs. Injections",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Comparison Matrix: Leakages vs. Injections",
                    "content": {
                        "headers": ["Feature", "Withdrawals / Leakages ($W$)", "Injections ($J$)"],
                        "rows": [
                            ["Definition", "Funds removed from the circular flow of spending.", "New funds added into the circular flow of spending."],
                            ["Core Components", "Savings ($S$), Taxes ($T$), Imports ($M$)", "Investment ($I$), Government Spending ($G$), Exports ($X$)"],
                            ["Effect on Circular Flow", "Contracts the flow of income and reduces national output.", "Expands the flow of income and increases national output."],
                            ["Source of Funds", "Drained from household income and firm revenue.", "Added from financial borrowing, public budgets, and foreign buyers."],
                            ["Economic Implication", "If $W > J$, national income contracts (recession risk).", "If $J > W$, national income expands (boom / inflation risk)."]
                        ]
                    }
                }
            ]
        },
        # Page 8: Real-World Kenyan Business Application
        {
            "page_number": 8,
            "page_title": "Realistic Application: Business Transactions in Kenya",
            "blocks": [
                {
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "title": "Business Decisions in Eldoret and Mombasa",
                    "content": {
                        "text": (
                            "Consider a large bakery business operating in Eldoret:\n\n"
                            "• **Scenario A (Import Leakage):** The bakery spends KSh 5,000,000 importing computerized baking ovens from Germany. "
                            "This represents an **Import Leakage ($M$)**, as the KSh 5M exits Kenya's circular flow and pays German factory workers.\n\n"
                            "• **Scenario B (Investment Injection):** The bakery uses KSh 2,000,000 from accumulated savings to hire local carpenters, masons, and electricians "
                            "to expand its local distribution depot. This represents an **Investment Injection ($I$)**, pumping KSh 2M directly into local household incomes.\n\n"
                            "• **Scenario C (Export Injection):** A tea cooperative in Kericho sells processed black tea worth KSh 10,000,000 to an auction buyer in the UK. "
                            "This represents an **Export Injection ($X$)**, injecting fresh foreign revenue into Kenyan tea farmers' pockets."
                        )
                    }
                },
                {
                    "block_type": "common_mistake",
                    "component_type": "common_mistake",
                    "title": "Watch Out: Confusing Saving with Investment",
                    "content": {
                        "text": "In everyday speech, people say 'I invested KSh 100,000 in a fixed deposit account.' In economics, that is merely **Saving ($S$)**—a leakage. **Investment ($I$)** occurs only when money is actively spent on physical capital goods (tractors, machinery, factories) that create new goods."
                    }
                }
            ]
        },
        # Page 9: Formative Assessment
        {
            "page_number": 9,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Classification of Injections and Leakages",
                    "content": {
                        "question": "Which of the following sets consists EXCLUSIVELY of injections into the circular flow of income?",
                        "options": [
                            "Savings, Government Expenditure, and Exports",
                            "Investments, Government Expenditure, and Exports",
                            "Taxation, Imports, and Investments",
                            "Savings, Taxation, and Imports"
                        ],
                        "answer": "B",
                        "explanation": "Investments ($I$), Government Expenditure ($G$), and Exports ($X$) are all additions to the spending stream that expand the circular flow of income. Savings, taxes, and imports are leakages."
                    }
                },
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Macroeconomic Impact Check",
                    "content": {
                        "question": "If Kenyan citizens drastically increase their spending on imported luxury cars while local business investment remains unchanged, what is the immediate effect on the circular flow of income?",
                        "options": [
                            "The circular flow of income expands because total spending has increased",
                            "The circular flow of income contracts because money is leaking out to foreign producers",
                            "National income remains unaffected because imports equal investments",
                            "Government expenditure automatically increases to balance the flow"
                        ],
                        "answer": "B",
                        "explanation": "Imports are a leakage. When spending on imports rises, purchasing power is drained out of the domestic economy into foreign countries, leaving domestic firms with lower sales revenue and causing national income to contract."
                    }
                }
            ]
        },
        # Page 10: Summary
        {
            "page_number": 10,
            "page_title": "Lesson 2 Summary & Takeaways",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Key Takeaways: Circular Flow",
                    "content": {
                        "text": (
                            "1. The circular flow links households (resource owners) and firms (producers) through real and money flows.\n"
                            "2. In the real flow, factor services flow to firms and final goods flow to households; in the money flow, factor rewards flow to households and consumption spending flows to firms.\n"
                            "3. Leakages ($S + T + M$) pull spending out of the circle; Injections ($I + G + X$) pump spending into the circle.\n"
                            "4. When Injections match Leakages ($J = W$), the circular flow achieves macroeconomic equilibrium."
                        )
                    }
                },
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Looking Ahead",
                    "content": {
                        "text": "In Lesson 3, we will examine the mathematical condition for economic equilibrium and learn how governments calculate the precise spending required to balance the economy."
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# LESSON 3: Equilibrium National Income (9 Pages)
# =============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Equilibrium National Income",
    "lesson_title": "Macroeconomic Equilibrium Condition and Solving Missing Variables",
    "pages": [
        # Page 1: Goals & Meaning
        {
            "page_number": 1,
            "page_title": "Macroeconomic Balance: The Equilibrium State",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define **Equilibrium National Income**\n"
                            "- State the mathematical equilibrium formula ($S + T + M = I + G + X$)\n"
                            "- Explain the economic consequences when leakages exceed injections or vice versa\n"
                            "- Calculate unknown leakage or injection values using algebraic substitution\n"
                            "- Analyze treasury planning decisions using equilibrium conditions"
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Equilibrium National Income",
                    "content": {
                        "term": "Equilibrium National Income",
                        "definition": "The state of balance in an economy where the total volume of intended injections equals the total volume of intended withdrawals (leakages), resulting in a stable level of national output and income."
                    }
                }
            ]
        },
        # Page 2: Mathematical Condition
        {
            "page_number": 2,
            "page_title": "The Fundamental Equilibrium Equation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Master Balance Formula",
                    "content": {
                        "text": (
                            "For an open economy with government participation to achieve equilibrium, total leakages must perfectly balance total injections:\n\n"
                            "$$\\text{Total Withdrawals (Leakages)} = \\text{Total Injections}$$\n"
                            "$$S + T + M = I + G + X$$\n\n"
                            "**Variables Breakdown:**\n"
                            "- $S$: Private Savings by households and businesses\n"
                            "- $T$: Total Government Taxes collected\n"
                            "- $M$: Total Import expenditure\n"
                            "- $I$: Private Capital Investment\n"
                            "- $G$: Total Government Expenditure\n"
                            "- $X$: Total Export revenue"
                        )
                    }
                }
            ]
        },
        # Page 3: Visual Scale Diagram
        {
            "page_number": 3,
            "page_title": "The Macroeconomic Balance Scale",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Equilibrium Balance Scale Diagram",
                    "svg_content": SVG_EQUILIBRIUM_SCALE,
                    "content": {
                        "text": "Diagram depicting a balance scale with Leakages (S + T + M) on the left pan and Injections (I + G + X) on the right pan."
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Disequilibrium Conditions",
                    "content": {
                        "text": "• **When $S + T + M > I + G + X$ (Contraction):** Total withdrawals exceed injections. Money drains out faster than it is replaced. Output falls, firms lay off workers, and national income shrinks.\n• **When $I + G + X > S + T + M$ (Expansion):** Injections exceed withdrawals. Extra demand stimulates production, businesses hire more workers, and if the economy reaches full capacity, prices rise (inflation)."
                    }
                }
            ]
        },
        # Page 4: Progressive Worked Example 1 (Basic)
        {
            "page_number": 4,
            "page_title": "Worked Example 1: Finding Missing Export Value",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Basic Equilibrium Calculation",
                    "content": {
                        "intro": "In a small open economy, the following economic figures are recorded for the year (in KSh millions):\n- Savings ($S$) = KSh 10M\n- Taxes ($T$) = KSh 15M\n- Imports ($M$) = KSh 8M\n- Investment ($I$) = KSh 12M\n- Government Spending ($G$) = KSh 11M\n\nCalculate the required value of Exports ($X$) for this economy to be in equilibrium.",
                        "steps": [
                            "**Step 1 — Identify Given Information:**\n$S = 10$, $T = 15$, $M = 8$, $I = 12$, $G = 11$.",
                            "**Step 2 — Identify What is Required:**\nFind the value of Exports ($X$) needed for equilibrium.",
                            "**Step 3 — State the Relevant Relationship:**\n$$S + T + M = I + G + X$$",
                            "**Step 4 — Substitute and Simplify:**\n$$\\text{Total Leakages} = 10 + 15 + 8 = 33\\text{ million KSh}$$\n$$\\text{Known Injections} = 12 + 11 = 23\\text{ million KSh}$$\n$$33 = 23 + X$$\n$$X = 33 - 23 = \\mathbf{10\\text{ million KSh}}$$",
                            "**Step 5 — Check:**\n$$\\text{Total Injections} = 12 + 11 + 10 = 33\\text{ million KSh}$$\nSince Leakages ($33\\text{M}$) = Injections ($33\\text{M}$), equilibrium is confirmed.",
                            "**Step 6 — Interpretation:**\nThe country must earn KSh 10 million from foreign exports to ensure total injections match the KSh 33 million drained by savings, taxes, and imports."
                        ]
                    }
                }
            ]
        },
        # Page 5: Progressive Worked Example 2 (Government Planning Case)
        {
            "page_number": 5,
            "page_title": "Worked Example 2: Treasury Budget Planning Scenario",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Applied Treasury Expenditure Policy Problem",
                    "content": {
                        "intro": "The Ministry of Finance in a developing country compiles the following economic forecasts for the upcoming fiscal year (figures in KSh billions):\n\n- Household Savings ($S$) = KSh 30B\n- Projected Tax Revenue ($T$) = KSh 50B\n- Estimated Imports ($M$) = KSh 40B\n- Private Sector Investment ($I$) = KSh 35B\n- Projected Export Earnings ($X$) = KSh 45B\n\na) Calculate the required Government Expenditure ($G$) to maintain macroeconomic equilibrium.\nb) Explain what would happen to the economy if the government decides to spend only KSh 20 billion.",
                        "steps": [
                            "**Step 1: Calculate Total Leakages:**\n$$\\text{Total Withdrawals (Leakages)} = S + T + M = 30 + 50 + 40 = \\mathbf{120\\text{ billion KSh}}$$",
                            "**Step 2: Calculate Known Injections:**\n$$\\text{Known Injections} = I + X = 35 + 45 = \\mathbf{80\\text{ billion KSh}}$$",
                            "**Step 3: Solve for Government Expenditure ($G$):**\n$$S + T + M = I + G + X$$\n$$120 = 80 + G$$\n$$G = 120 - 80 = \\mathbf{40\\text{ billion KSh}}$$",
                            "**Step 4: Answer Part (b) — Policy Consequence:**\nIf the government spends only KSh 20B, total injections will be $35 + 20 + 45 = 100\\text{ billion KSh}$.\nSince Leakages (KSh 120B) exceed Injections (KSh 100B) by KSh 20B, there is a net drain on purchasing power. Domestic businesses will experience unsold inventories, reduce orders, and lay off workers, causing national income to contract into a recession."
                        ]
                    }
                }
            ]
        },
        # Page 6: Worked Example 3 (KCSE Advanced Challenge)
        {
            "page_number": 6,
            "page_title": "Worked Example 3: Multi-Variable Disequilibrium Analysis",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Level Multi-Step Disequilibrium Problem",
                    "content": {
                        "intro": "An economic report presents the following data for an economy:\n- Exports = KSh 50B\n- Government Spending = KSh 60B\n- Private Investment = KSh 40B\n- Taxes Collected = KSh 45B\n- Imports = KSh 55B\n\na) Determine whether the economy is in equilibrium.\nb) Calculate the level of private savings ($S$) required to establish macroeconomic equilibrium.",
                        "steps": [
                            "**Step 1: Calculate Total Injections:**\n$$\\text{Total Injections} = I + G + X = 40 + 60 + 50 = \\mathbf{150\\text{ billion KSh}}$$",
                            "**Step 2: Calculate Known Leakages:**\n$$\\text{Known Leakages} = T + M = 45 + 55 = \\mathbf{100\\text{ billion KSh}}$$",
                            "**Step 3: Determine State of Equilibrium:**\nInjections (150B) > Known Leakages (100B). The economy is **NOT** in equilibrium; it is currently expanding due to excess injection stimulus.",
                            "**Step 4: Calculate Required Savings ($S$):**\n$$S + T + M = I + G + X$$\n$$S + 100 = 150$$\n$$S = 150 - 100 = \\mathbf{50\\text{ billion KSh}}$$\nHouseholds must save KSh 50 billion to balance the 150 billion of injections."
                        ]
                    }
                }
            ]
        },
        # Page 7: Real-World Policy Connection
        {
            "page_number": 7,
            "page_title": "Real-World Context: Fiscal and Monetary Balancing",
            "blocks": [
                {
                    "block_type": "real_world_connection",
                    "component_type": "real_world_connection",
                    "title": "Managing Economic Growth in Kenya",
                    "content": {
                        "text": (
                            "In Kenya, when the government embarks on massive infrastructure projects (such as the Standard Gauge Railway or highway construction), "
                            "this represents a huge increase in **Government Expenditure ($G$)**—an injection. "
                            "If this is not matched by increased tax revenue ($T$) or domestic savings ($S$), the excess injection can lead to high import demand ($M$) for foreign construction equipment, "
                            "causing balance of payments pressure and inflation.\n\n"
                            "To maintain stability, the Treasury and Central Bank of Kenya continuously adjust tax rates, interest rates, and public borrowing to steer the circular flow toward equilibrium."
                        )
                    }
                }
            ]
        },
        # Page 8: Knowledge Check
        {
            "page_number": 8,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Equilibrium Calculation Check",
                    "content": {
                        "question": "An economy has Savings = KSh 25B, Imports = KSh 40B, Investment = KSh 30B, Government Spending = KSh 45B, and Exports = KSh 35B. If the economy is in equilibrium, what is the amount of taxes (T) collected?",
                        "options": [
                            "KSh 35 billion",
                            "KSh 45 billion",
                            "KSh 50 billion",
                            "KSh 65 billion"
                        ],
                        "answer": "B",
                        "explanation": "Total Injections = I + G + X = 30 + 45 + 35 = KSh 110B. For equilibrium: S + T + M = 110. Substituting known leakages: 25 + T + 40 = 110 -> 65 + T = 110 -> T = 110 - 65 = KSh 45 billion."
                    }
                }
            ]
        },
        # Page 9: Summary
        {
            "page_number": 9,
            "page_title": "Lesson 3 Summary & Takeaways",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Key Takeaways: Equilibrium National Income",
                    "content": {
                        "text": (
                            "1. Equilibrium occurs when Total Withdrawals equal Total Injections: $S + T + M = I + G + X$.\n"
                            "2. If Withdrawals > Injections, national income contracts and unemployment rises.\n"
                            "3. If Injections > Withdrawals, economic activity expands and inflation pressure builds.\n"
                            "4. Policy makers adjust government spending ($G$) and taxation ($T$) to stabilize the circular flow at optimal employment levels."
                        )
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# LESSON 4: Expenditure Approach to Measuring National Income (10 Pages)
# =============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "The Expenditure Approach to Measuring National Income",
    "lesson_title": "Expenditure Components, Market Price to Factor Cost Adjustments, and Limitations",
    "pages": [
        # Page 1: Goals & Concept
        {
            "page_number": 1,
            "page_title": "Measuring Wealth Through What We Spend",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 4.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the meaning and four main components of the **Expenditure Approach**\n"
                            "- Calculate Gross National Expenditure using $GNE = C + I + G + (X - M)$\n"
                            "- Adjust expenditure from **Market Prices** to **Factor Cost** by deducting indirect taxes and adding subsidies\n"
                            "- Deduct depreciation to compute Net National Expenditure (National Income)\n"
                            "- Identify and explain the practical problems encountered when measuring national income via expenditure"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Expenditure Concept",
                    "content": {
                        "text": (
                            "If you want to measure the total value of all goods and services produced in an economy, one direct method is to add up the money spent "
                            "by all sectors of the economy purchasing those newly produced final goods.\n\n"
                            "When you buy a packet of milk, your private expenditure becomes the income of the shopkeeper, the dairy processor, and the dairy farmer. "
                            "By summing all final expenditures across households, firms, government, and foreign buyers, we obtain the total gross output of the nation."
                        )
                    }
                }
            ]
        },
        # Page 2: The Four Components of Expenditure
        {
            "page_number": 2,
            "page_title": "The Four Main Components of Expenditure",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Breaking Down Total National Spending",
                    "content": {
                        "text": (
                            "Total expenditure is divided into four major categories:\n\n"
                            "1. **Personal Consumption Expenditure ($C$):** Spending by individuals and households on durable and non-durable consumer goods and services (food, clothing, transport, rent, school fees).\n\n"
                            "2. **Gross Capital Expenditure / Investment ($I$):** Spending by private businesses on capital assets (machinery, factory buildings, transport vehicles, additions to stock).\n\n"
                            "3. **Government Expenditure ($G$):** Spending by the national and county governments on public administration, security, public healthcare, education, and civil servant salaries.\n\n"
                            "4. **Net Exports ($(X - M)$):** Total export earnings from foreign buyers ($X$) minus total import spending paid to foreign sellers ($M$)."
                        )
                    }
                },
                {
                    "block_type": "formula_breakdown",
                    "component_type": "formula_breakdown",
                    "title": "Gross National Expenditure Formula",
                    "content": {
                        "formula": "\\text{GNE at Market Prices} = C + I + G + (X - M)",
                        "breakdown": "- **$C$**: Private household consumption\n- **$I$**: Private business investment\n- **$G$**: Government consumption and capital spending\n- **$(X - M)$**: Net foreign expenditure (Exports minus Imports)"
                    }
                }
            ]
        },
        # Page 3: Real World Asset (Port of Mombasa)
        {
            "page_number": 3,
            "page_title": "International Trade: Net Exports at Kilindini Harbour",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Container Cargo Operations at Mombasa Port",
                    "content": {
                        "text": "The Port of Mombasa handling international container shipping, illustrating how exports of tea and agricultural goods generate foreign revenue (X) while imported machinery and oil represent payments abroad (M).",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
                        "author": "Wikimedia Commons / CC-BY-SA",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Exclusion Rule: Second-Hand Goods",
                    "content": {
                        "text": "Only expenditure on **newly produced** goods is included. Spending on second-hand goods (e.g. buying a used car or a 10-year-old house) is strictly excluded because no new production occurred this year—it represents only a transfer of ownership of existing wealth."
                    }
                }
            ]
        },
        # Page 4: Market Prices vs Factor Cost Adjustments
        {
            "page_number": 4,
            "page_title": "Converting from Market Prices to Factor Cost",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Market Prices Distort Production Costs",
                    "content": {
                        "text": (
                            "Raw expenditure is recorded at **Market Prices** (the retail price paid in stores). However, market prices do not reflect the true cost of resources used in production because of two government interventions:\n\n"
                            "1. **Indirect Taxes (e.g. VAT, Excise Duty):** Taxes added to goods artificially **raise** the market price above the actual production cost.\n"
                            "2. **Subsidies:** Government financial grants to producers (such as fertilizer subsidies) artificially **lower** the market price below the actual production cost.\n\n"
                            "To find the true resource cost (**Factor Cost**), we reverse these distortions:\n\n"
                            "$$\\text{GNE at Factor Cost} = \\text{GNE at Market Prices} + \\text{Subsidies} - \\text{Indirect Taxes}$$"
                        )
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Market Price vs Factor Cost Adjustments",
                    "content": {
                        "headers": ["Item", "Effect on Market Price", "Adjustment to Reach Factor Cost"],
                        "rows": [
                            ["Indirect Taxes (VAT)", "Increases price above resource cost", "SUBTRACT (- Indirect Taxes)"],
                            ["Government Subsidies", "Reduces price below resource cost", "ADD (+ Subsidies)"],
                            ["Depreciation (Capital Consumption)", "Represents wear and tear of assets", "SUBTRACT (- Depreciation to reach Net NI)"]
                        ]
                    }
                }
            ]
        },
        # Page 5: Progressive Worked Example 1 (Guided)
        {
            "page_number": 5,
            "page_title": "Worked Example 1: Full Adjustment Sequence",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Step-by-Step Expenditure Approach Calculation",
                    "content": {
                        "intro": "The following economic data was collected from the national accounts of a country in 2025 (all figures in KSh millions):\n- Consumer Expenditure ($C$) = KSh 450,000M\n- Investment Expenditure ($I$) = KSh 120,000M\n- Government Expenditure ($G$) = KSh 180,000M\n- Exports ($X$) = KSh 60,000M\n- Imports ($M$) = KSh 75,000M\n- Indirect Taxes = KSh 30,000M\n- Subsidies = KSh 15,000M\n- Depreciation = KSh 25,000M",
                        "steps": [
                            "**Step 1 — Calculate Net Exports ($X - M$):**\n$$\\text{Net Exports} = 60,000 - 75,000 = -15,000\\text{ million KSh}$$",
                            "**Step 2 — Calculate GNE at Market Prices:**\n$$\\text{GNE at Market Prices} = C + I + G + (X - M)$$\n$$\\text{GNE at Market Prices} = 450,000 + 120,000 + 180,000 + (-15,000) = \\mathbf{735,000\\text{ million KSh}}$$",
                            "**Step 3 — Adjust from Market Prices to Factor Cost:**\n$$\\text{GNE at Factor Cost} = \\text{GNE at Market Prices} + \\text{Subsidies} - \\text{Indirect Taxes}$$\n$$\\text{GNE at Factor Cost} = 735,000 + 15,000 - 30,000 = 750,000 - 30,000 = \\mathbf{720,000\\text{ million KSh}}$$",
                            "**Step 4 — Calculate National Income (Net National Expenditure):**\n$$\\text{National Income} = \\text{GNE at Factor Cost} - \\text{Depreciation}$$\n$$\\text{National Income} = 720,000 - 25,000 = \\mathbf{695,000\\text{ million KSh}}$$",
                            "**Step 5 — Economic Interpretation:**\nThe country produced final goods and services whose true factor production cost was KSh 720,000 million. After deducting KSh 25,000 million to replace worn-out machinery, the net value of production available to the nation is KSh 695,000 million."
                        ]
                    }
                }
            ]
        },
        # Page 6: KCSE Level Examination Problem
        {
            "page_number": 6,
            "page_title": "Worked Example 2: KCSE Traps and Second-Hand Exclusions",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Examination Problem with Filter Items",
                    "content": {
                        "intro": "The following economic data was extracted from the national records of Country Y in 2025 (in KSh millions):\n\n- Private consumption ($C$) = KSh 520,000M\n- Investment expenditure ($I$) = KSh 150,000M\n- Government spending ($G$) = KSh 165,000M\n- Exports ($X$) = KSh 90,000M\n- Imports ($M$) = KSh 110,000M\n- Subsidies = KSh 12,000M\n- Indirect Taxes = KSh 28,000M\n- Depreciation = KSh 30,000M\n- Second-hand motor vehicle sales = KSh 15,000M\n\nCalculate the Net National Expenditure (National Income).",
                        "steps": [
                            "**Step 1: Rule Check on Second-Hand Goods:**\nWe must **strictly exclude** the second-hand vehicle sales of KSh 15,000M. Second-hand transactions represent a transfer of ownership of existing goods rather than new production in 2025.",
                            "**Step 2: Calculate GNE at Market Prices:**\n$$\\text{GNE at Market Prices} = 520,000 + 150,000 + 165,000 + (90,000 - 110,000)$$\n$$\\text{GNE at Market Prices} = 835,000 + (-20,000) = \\mathbf{815,000\\text{ million KSh}}$$",
                            "**Step 3: Convert to Factor Cost:**\n$$\\text{GNE at Factor Cost} = 815,000 + 12,000 - 28,000 = \\mathbf{799,000\\text{ million KSh}}$$",
                            "**Step 4: Deduct Depreciation to obtain National Income:**\n$$\\text{National Income} = 799,000 - 30,000 = \\mathbf{769,000\\text{ million KSh}}$$"
                        ]
                    }
                }
            ]
        },
        # Page 7: Practical Problems of the Expenditure Approach
        {
            "page_number": 7,
            "page_title": "Practical Problems of the Expenditure Approach",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Five Challenges in Measuring National Expenditure",
                    "content": {
                        "text": (
                            "According to the syllabus, national statisticians face major obstacles when computing national expenditure:\n\n"
                            "1. **Inaccurate Private Expenditure Records:** Many individuals and small businesses in the informal (Jua Kali) sector do not keep written receipts or books of accounts, forcing statisticians to rely on inaccurate estimations.\n\n"
                            "2. **Valuing the Subsistence Sector:** A substantial share of production in developing economies is produced and consumed within households (e.g. subsistence farmers eating their own maize). Because no money changes hands, this spending is omitted or grossly estimated.\n\n"
                            "3. **Double Counting:** It is difficult to separate intermediate expenditure from final expenditure. For example, if a statistician counts money spent buying timber and also counts money spent buying the finished furniture made from that timber, the timber is counted twice.\n\n"
                            "4. **Fluctuating Exchange Rates:** Rapid fluctuations in foreign currency exchange rates make it difficult to determine the stable domestic value of imports and exports.\n\n"
                            "5. **Distinguishing Consumption from Investment:** Some household purchases (such as motor vehicles or personal computers) serve both private consumption and business investment, making categorization difficult."
                        )
                    }
                }
            ]
        },
        # Page 8: Real-World Asset: Subsistence Agriculture
        {
            "page_number": 8,
            "page_title": "The Informal and Subsistence Accounting Challenge",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Local Agricultural Market in Kenya",
                    "content": {
                        "text": "A vibrant local agricultural and vegetable market in Kenya, illustrating the substantial volume of daily commercial transactions that operate without formal computerized receipts.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "author": "Wikimedia Commons / CC-BY-SA",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Accounting Principle",
                    "content": {
                        "text": "To prevent double counting in the expenditure approach, statisticians must record only final retail purchases and exclude all intermediate goods purchased by manufacturers."
                    }
                }
            ]
        },
        # Page 9: Formative Knowledge Check
        {
            "page_number": 9,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Adjustment Factor Cost Question",
                    "content": {
                        "question": "Why are government subsidies ADDED to Gross National Expenditure when converting from Market Prices to Factor Cost?",
                        "options": [
                            "Because subsidies represent government taxes that must be recovered",
                            "Because subsidies artificially lower the market selling price below the true cost of resources used in production",
                            "Because subsidies are paid directly to foreign importers",
                            "Because subsidies increase the rate of capital depreciation"
                        ],
                        "answer": "B",
                        "explanation": "Subsidies are government grants that reduce the price paid by consumers in shops. Therefore, the market price is lower than the actual resource cost incurred by producers. Adding back subsidies restores the figure to its true factor cost."
                    }
                },
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Expenditure Calculation Question",
                    "content": {
                        "question": "An economy has C = KSh 300B, I = KSh 80B, G = KSh 100B, X = KSh 50B, M = KSh 60B, Subsidies = KSh 10B, Indirect Taxes = KSh 25B, and Depreciation = KSh 15B. What is the National Income?",
                        "options": [
                            "KSh 440 billion",
                            "KSh 455 billion",
                            "KSh 470 billion",
                            "KSh 485 billion"
                        ],
                        "answer": "A",
                        "explanation": "GNE at Market Prices = 300 + 80 + 100 + (50 - 60) = KSh 470B. GNE at Factor Cost = 470 + 10 (subsidies) - 25 (taxes) = KSh 455B. National Income = 455 - 15 (depreciation) = KSh 440 billion."
                    }
                }
            ]
        },
        # Page 10: Summary
        {
            "page_number": 10,
            "page_title": "Lesson 4 Summary & Takeaways",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Key Takeaways: Expenditure Approach",
                    "content": {
                        "text": (
                            "1. The expenditure approach sums spending on new final goods: $GNE = C + I + G + (X - M)$.\n"
                            "2. Second-hand goods and intermediate purchases are strictly excluded to avoid double counting.\n"
                            "3. To convert from Market Prices to Factor Cost: Add Subsidies and Subtract Indirect Taxes.\n"
                            "4. Deduct Depreciation from GNE at factor cost to obtain true National Income."
                        )
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# LESSON 5: Income Approach to Measuring National Income (10 Pages)
# =============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "The Income Approach to Measuring National Income",
    "lesson_title": "Factor Incomes, Transfer Payments, Adjustments, and Limitations",
    "pages": [
        # Page 1: Goals & Concept
        {
            "page_number": 1,
            "page_title": "Measuring Wealth Through What We Earn",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 5.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define the **Income Approach** and identify the four factor rewards (rent, wages, interest, profit)\n"
                            "- Distinguish between productive **Factor Incomes** and non-productive **Transfer Payments**\n"
                            "- Explain why transfer payments and stock appreciation are excluded from national income\n"
                            "- Compute Gross and Net National Income using algebraic formulas\n"
                            "- Explain the practical problems encountered when measuring national income via the income approach"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Income Concept",
                    "content": {
                        "text": (
                            "Every single shilling spent by a consumer or business firm becomes the income of someone who helped produce that good or service. "
                            "Instead of standing at the shop counter counting expenditures, the **Income Approach** approaches the economic equation from the earning side: "
                            "it sums all incomes received by the owners of the factors of production."
                        )
                    }
                }
            ]
        },
        # Page 2: Factor Incomes Categorization
        {
            "page_number": 2,
            "page_title": "The Four Factor Rewards & Additional Incomes",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Factor Incomes Included in National Income",
                    "content": {
                        "text": (
                            "The income approach groups all earned incomes into factor rewards:\n\n"
                            "1. **Wages and Salaries:** Income earned by labour (including bonuses, allowances, and employers' contributions to pension funds).\n"
                            "2. **Rent:** Income earned by owners of land and residential or commercial buildings.\n"
                            "3. **Interest:** Income earned by owners of capital who lend financial funds to businesses or the government.\n"
                            "4. **Profits:** Earnings made by entrepreneurs and companies, which include:\n"
                            "   - **Personal profits / Dividends:** Distributed profits received by sole proprietors, partners, and shareholders.\n"
                            "   - **Retained Profits:** Undistributed profits kept by companies to reinvest in future growth.\n"
                            "   - **Public Income:** Profits earned by state corporations (parastatals) and government enterprises."
                        )
                    }
                }
            ]
        },
        # Page 3: Factor Incomes vs Transfer Payments
        {
            "page_number": 3,
            "page_title": "Crucial Distinction: Factor Incomes vs. Transfer Payments",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Transfer Payments",
                    "content": {
                        "term": "Transfer Payments",
                        "definition": "Payments received by individuals for which no current productive goods or services have been provided in return, representing merely a redistribution of existing income."
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Included Factor Incomes vs Excluded Transfer Payments",
                    "content": {
                        "headers": ["Category", "Factor Incomes (INCLUDED)", "Transfer Payments (EXCLUDED)"],
                        "rows": [
                            ["Definition", "Income earned by actively supplying a factor of production.", "Income received without providing any current goods or services."],
                            ["Examples", "Teacher's salary, landlord's rent, bank loan interest, farmer's profit.", "Student bursaries, retirement pensions, pocket money, unemployment relief, gifts."],
                            ["Reason for Treatment", "Directly rewards current economic production.", "Merely redistributes income from taxpayers; counting it would cause double counting."]
                        ]
                    }
                }
            ]
        },
        # Page 4: Stock Appreciation and Formula Relationships
        {
            "page_number": 4,
            "page_title": "Formula Adjustments and Stock Appreciation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Stock Appreciation is Deducted",
                    "content": {
                        "text": (
                            "**Stock Appreciation:** When the value of a business firm's unsold inventory rises purely because of inflation (general price increases) "
                            "rather than any physical increase in goods produced, this paper profit must be **deducted** to avoid artificially inflating national income.\n\n"
                            "**Master Formulas for Income Approach:**\n\n"
                            "$$\\text{Gross National Income (GNI)} = \\text{Personal Incomes} + \\text{Retained Profits} - (\\text{Transfer Payments} + \\text{Stock Appreciation})$$\n\n"
                            "$$\\text{Net National Income (National Income)} = \\text{GNI} - \\text{Depreciation}$$"
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Factor Cost vs Market Price in Income Approach",
                    "content": {
                        "text": "The income approach naturally arrives at **Factor Cost** because it sums direct factor rewards. To convert National Income from Factor Cost to Market Prices, we do the reverse: Add Indirect Taxes and Subtract Subsidies."
                    }
                }
            ]
        },
        # Page 5: Progressive Worked Example 1 (Guided)
        {
            "page_number": 5,
            "page_title": "Worked Example 1: Full Income Approach Calculation",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Step-by-Step Income Approach Calculation",
                    "content": {
                        "intro": "The statistical bureau of a nation records the following annual earnings (in KSh millions):\n- Wages and Salaries = KSh 280,000M\n- Rental Incomes = KSh 75,000M\n- Net Interest Incomes = KSh 45,000M\n- Sole Traders' Profits = KSh 90,000M\n- Retained Corporate Profits = KSh 30,000M\n- Government Pension Payments = KSh 20,000M\n- Stock Appreciation = KSh 10,000M\n- Depreciation = KSh 15,000M",
                        "steps": [
                            "**Step 1 — Calculate Total Gross Factor Incomes:**\n$$\\text{Factor Incomes} = \\text{Wages} + \\text{Rent} + \\text{Interest} + \\text{Personal Profits}$$\n$$\\text{Factor Incomes} = 280,000 + 75,000 + 45,000 + 90,000 = \\mathbf{490,000\\text{ million KSh}}$$",
                            "**Step 2 — Calculate Gross National Income (GNI):**\nWe add retained company profits and deduct the transfer payments (pensions) and stock appreciation:\n$$\\text{GNI} = \\text{Factor Incomes} + \\text{Retained Profit} - (\\text{Transfer Payments} + \\text{Stock Appreciation})$$\n$$\\text{GNI} = 490,000 + 30,000 - (20,000 + 10,000)$$\n$$\\text{GNI} = 520,000 - 30,000 = \\mathbf{490,000\\text{ million KSh}}$$",
                            "**Step 3 — Calculate Net National Income (National Income):**\n$$\\text{Net National Income} = \\text{GNI} - \\text{Depreciation}$$\n$$\\text{Net National Income} = 490,000 - 15,000 = \\mathbf{475,000\\text{ million KSh}}$$",
                            "**Step 4 — Economic Interpretation:**\nThe net total earnings generated by all owners of land, labour, capital, and entrepreneurship across the nation in 2025 amounted to KSh 475,000 million."
                        ]
                    }
                }
            ]
        },
        # Page 6: Realistic Kenyan Business Scenario
        {
            "page_number": 6,
            "page_title": "Realistic Application: Household Income Classification",
            "blocks": [
                {
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "title": "Classifying Incomes in a Kenyan Household",
                    "content": {
                        "text": (
                            "Consider a multi-generational household in Nakuru:\n\n"
                            "1. **Father (Secondary School Principal):** Earns a monthly salary of KSh 80,000. -> **INCLUDED** (Wage reward for labour).\n"
                            "2. **Mother (Hardware Store Owner):** Generates KSh 50,000 in monthly net profit. -> **INCLUDED** (Entrepreneurial profit).\n"
                            "3. **Grandfather (Retired Civil Servant):** Receives a government monthly pension of KSh 15,000. -> **EXCLUDED** (Transfer payment; no current work done this month).\n"
                            "4. **Daughter (University Student):** Receives a KSh 10,000 government bursary grant and KSh 3,000 pocket money from her father. -> **EXCLUDED** (Transfer payments).\n\n"
                            "Total contribution of this household to national income = $80,000 + 50,000 = \\mathbf{\\text{KSh } 130,000\\text{ per month}}$."
                        )
                    }
                }
            ]
        },
        # Page 7: Practical Problems of the Income Approach
        {
            "page_number": 7,
            "page_title": "Practical Problems of the Income Approach",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Four Major Obstacles in Measuring Incomes",
                    "content": {
                        "text": (
                            "Statisticians encounter four severe challenges when compiling national income statistics using the income method:\n\n"
                            "1. **Tax Evasion and Inaccurate Declarations:** Many individuals and businesses deliberately understate their earnings or maintain two sets of accounting books to minimize their income tax liability.\n\n"
                            "2. **Unrecorded and Illegal Incomes:** Incomes earned from illegal activities (e.g. smuggling, counterfeit goods, black-market dealing) or untracked cash transactions are never declared to the tax authorities.\n\n"
                            "3. **Fluctuating Incomes and Price Changes:** Incomes in agriculture and seasonal industries fluctuate wildly depending on weather and world commodity prices, making annual income computation complex.\n\n"
                            "4. **Difficulty in Separating Transfer Payments:** In practice, it is often technically difficult to distinguish pure transfer payments from legitimate allowances paid for casual services."
                        )
                    }
                }
            ]
        },
        # Page 8: Real World Asset: Formal vs Informal Incomes
        {
            "page_number": 8,
            "page_title": "Informal Sector (Jua Kali) Income Accounting",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Artisans and Fabricators in Kenya",
                    "content": {
                        "text": "Kenyan metal fabricators in the informal Jua Kali manufacturing sector, illustrating economic value creation where transactions are predominantly cash-based and difficult to capture in formal income tax records.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
                        "author": "Wikimedia Commons / CC-BY-SA",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
                    }
                }
            ]
        },
        # Page 9: Formative Knowledge Check
        {
            "page_number": 9,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Transfer Payment Identification Check",
                    "content": {
                        "question": "Which one of the following items is a transfer payment that MUST be excluded when calculating national income using the income approach?",
                        "options": [
                            "Salaries paid to nurses in public hospitals",
                            "Dividends distributed to shareholders of a commercial bank",
                            "National Social Security Fund (NSSF) monthly retirement benefits paid to elderly citizens",
                            "Rental income received by commercial property landlords"
                        ],
                        "answer": "C",
                        "explanation": "NSSF retirement pensions are transfer payments. They represent a redistribution of past savings and taxpayer funds rather than a reward for current goods or services produced in the current year."
                    }
                }
            ]
        },
        # Page 10: Summary
        {
            "page_number": 10,
            "page_title": "Lesson 5 Summary & Takeaways",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Key Takeaways: Income Approach",
                    "content": {
                        "text": (
                            "1. The income approach sums earned factor rewards: Wages + Rent + Interest + Profits + Retained Earnings.\n"
                            "2. Transfer payments (pensions, student grants, gifts) and stock appreciation are strictly excluded.\n"
                            "3. The income approach yields output at Factor Cost.\n"
                            "4. Major practical challenges include tax evasion, hidden illegal incomes, and undocumented informal earnings."
                        )
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# LESSON 6: The Output (Value-Added) Approach (10 Pages)
# =============================================================================
LESSON_6_DATA = {
    "unit_order": 6,
    "unit_name": "The Output (Value-Added) Approach",
    "lesson_title": "Final Product Method, Multi-Stage Value Addition, and Double-Counting Avoidance",
    "pages": [
        # Page 1: Goals & Concept
        {
            "page_number": 1,
            "page_title": "Measuring Wealth Through Physical Value Created",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 6.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define the **Output Approach** (Product Approach) to measuring national income\n"
                            "- Distinguish between the **Final Product Method** and the **Value-Added Method**\n"
                            "- Calculate value added across multi-stage production chains\n"
                            "- Explain how government non-market services (health, security, education) are valued\n"
                            "- Explain the practical problems of the output approach (subsistence valuation, double counting, intermediate goods)"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Output Approach Concept",
                    "content": {
                        "text": (
                            "The **Output Approach** (also known as the Net Output or Value-Added Approach) measures national income by finding the total monetary value "
                            "of all final physical goods and services produced by all industrial sectors (agriculture, manufacturing, construction, commerce, transport, services) over one year."
                        )
                    }
                }
            ]
        },
        # Page 2: Two Methods to Avoid Double Counting
        {
            "page_number": 2,
            "page_title": "Final Product Method vs. Value-Added Method",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "How to Avoid the Double Counting Trap",
                    "content": {
                        "text": (
                            "If we simply sum the gross sales turnover of every company in the country, we will count the same raw materials multiple times. "
                            "To ensure each item is counted exactly once, economists use two equivalent techniques:\n\n"
                            "1. **The Final Product Method:**\n"
                            "Count only the market price of the finished product when sold to the ultimate end-user for consumption. Strictly ignore all previous sales of intermediate raw materials.\n\n"
                            "2. **The Value-Added Method:**\n"
                            "Record the incremental economic value added by each firm at every individual stage of the production process:\n\n"
                            "$$\\text{Value Added} = \\text{Gross Value of Output (Sales Price)} - \\text{Cost of Intermediate Inputs Purchased}$$"
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Value Added",
                    "content": {
                        "term": "Value Added",
                        "definition": "The net increase in the market value of a product created by a business firm at a specific stage of production, calculated as the firm's sales revenue minus the cost of raw materials and intermediate goods purchased from other firms."
                    }
                }
            ]
        },
        # Page 3: Visual Flow of Value Added Chain
        {
            "page_number": 3,
            "page_title": "Process Diagram: Multi-Stage Bread Production Chain",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Multi-Stage Value Addition Production Chain",
                    "svg_content": SVG_VALUE_ADDED_CHAIN,
                    "content": {
                        "text": "Diagram showing how summing value added across 4 stages of bread production (Farmer Sh.10 + Miller Sh.8 + Baker Sh.7 + Retailer Sh.5) equals the final loaf price of Sh.30."
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Why Double Counting Is Dangerous",
                    "content": {
                        "text": "If a statistician naively added the gross sales of all 4 businesses ($10 + 18 + 25 + 30 = \\text{Sh. 83}$), the recorded output would be inflated by Sh. 53! Summing only the value added ($10 + 8 + 7 + 5 = \\text{Sh. 30}$) ensures 100% accuracy."
                    }
                }
            ]
        },
        # Page 4: Government Output Valuation
        {
            "page_number": 4,
            "page_title": "Valuation of Non-Market Government Services",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "How Are Public Services Valued Without Market Prices?",
                    "content": {
                        "text": (
                            "Unlike private companies, the government provides critical public services that are not sold in a commercial market:\n\n"
                            "- National defense and police security\n"
                            "- Public primary and secondary school education\n"
                            "- Public referral healthcare in hospitals\n"
                            "- Judicial court systems and road maintenance\n\n"
                            "**How are they valued in National Income?**\n"
                            "According to national accounting rules, government services are valued at the **cost to the government of providing them**.\n"
                            "This equals the total wages, salaries, and allowances paid to public officers (teachers, police officers, doctors) plus the direct operational costs of materials used."
                        )
                    }
                }
            ]
        },
        # Page 5: Progressive Worked Example (Sectoral Output)
        {
            "page_number": 5,
            "page_title": "Worked Example: Multi-Sector Output Approach",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Step-by-Step Sectoral Value-Added Calculation",
                    "content": {
                        "intro": "The national statistics bureau of a country records the following gross outputs and intermediate purchases across economic sectors (in KSh millions):\n\n- Primary Sector (Agriculture & Mining): Gross Output = KSh 150,000M (Zero intermediate inputs purchased)\n- Secondary Sector (Manufacturing & Construction): Gross Output = KSh 280,000M; Intermediate Inputs = KSh 120,000M\n- Tertiary Sector (Commercial & Financial Services): Gross Output = KSh 320,000M; Intermediate Inputs = KSh 90,000M\n- Net Factor Income from Abroad = KSh -15,000M\n- Depreciation = KSh 20,000M\n\nCalculate GDP, GNP, and National Income.",
                        "steps": [
                            "**Step 1 — Calculate Value Added for Each Sector:**\n- $\\text{Primary Sector Value Added} = 150,000 - 0 = \\mathbf{150,000\\text{ million KSh}}$\n- $\\text{Secondary Sector Value Added} = 280,000 - 120,000 = \\mathbf{160,000\\text{ million KSh}}$\n- $\\text{Tertiary Sector Value Added} = 320,000 - 90,000 = \\mathbf{230,000\\text{ million KSh}}$",
                            "**Step 2 — Calculate Gross Domestic Product (GDP):**\n$$\\text{GDP} = 150,000 + 160,000 + 230,000 = \\mathbf{540,000\\text{ million KSh}}$$",
                            "**Step 3 — Calculate Gross National Product (GNP):**\n$$\\text{GNP} = \\text{GDP} + \\text{NFIA} = 540,000 + (-15,000) = \\mathbf{525,000\\text{ million KSh}}$$",
                            "**Step 4 — Calculate National Income (NNP):**\n$$\\text{National Income} = \\text{GNP} - \\text{Depreciation} = 525,000 - 20,000 = \\mathbf{505,000\\text{ million KSh}}$$",
                            "**Step 5 — Economic Interpretation:**\nThe net value created across primary, industrial, and service sectors by the citizens of this country in 2025 is KSh 505,000 million."
                        ]
                    }
                }
            ]
        },
        # Page 6: Real World Asset: Tea Processing Value Chain
        {
            "page_number": 6,
            "page_title": "Real-World Case: Kenyan Tea Value Addition Chain",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Industrial Tea Processing Factory in Kenya",
                    "content": {
                        "text": "Tea leaves undergoing industrial withering, cutting, fermenting, and drying inside a Kenyan tea factory, converting raw green leaves into high-grade packaged export tea.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/2009.12-363-1125ap_tea%2Cprocessing%28withering%29%2Cstirring_Rukuriri_Tea_Factory%2Ctea-zone_N_of_Embu%28C_Highlands%29%2CKE_mon14dec2009-1242h.jpg",
                        "author": "Wikimedia Commons / CC-BY-SA",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:2009.12-363-1125ap_tea,processing(withering),stirring_Rukuriri_Tea_Factory,tea-zone_N_of_Embu(C_Highlands),KE_mon14dec2009-1242h.jpg"
                    }
                },
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "The Kenyan Tea Value Chain",
                    "content": {
                        "steps": [
                            "**Smallholder Farmer (Kericho/Embu):** Plucks raw green leaf and sells to factory for KSh 25/kg. (Value added = KSh 25).",
                            "**KTDA Factory:** Withers, cuts, ferments, dries, and grades black tea; sells bulk tea at Mombasa auction for KSh 120/kg. (Value added = $120 - 25 = \\text{KSh } 95$).",
                            "**Tea Packaging Exporter:** Blends, packages into branded retail boxes, and exports to the UK for KSh 250/kg. (Value added = $250 - 120 = \\text{KSh } 130$).",
                            "**Total Value Added:** $25 + 95 + 130 = \\mathbf{\\text{KSh } 250\\text{/kg}}$, matching the final export sale price."
                        ]
                    }
                }
            ]
        },
        # Page 7: Practical Problems of the Output Approach
        {
            "page_number": 7,
            "page_title": "Practical Problems of the Output Approach",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Seven Key Limitations of the Output Method",
                    "content": {
                        "text": (
                            "According to the source, the output approach faces several critical challenges:\n\n"
                            "1. **Valuing Subsistence Sector Output:** In agricultural regions, families consume their own food crops (maize, beans, cassava). Because this output is not sold in a market, estimating its monetary value is prone to large inaccuracies.\n\n"
                            "2. **Valuing Non-Market Government Services:** Valuing public healthcare, security, and education at the cost of civil servant salaries may fail to reflect the true quality and economic benefit of those services.\n\n"
                            "3. **Danger of Double Counting:** It is difficult to strictly distinguish primary inputs from intermediate inputs, creating continuous risks of double counting.\n\n"
                            "4. **Frequent Price Fluctuations:** Inflation and volatile commodity prices distort physical output values over time.\n\n"
                            "5. **Unrecorded Illegal Activities:** Substantial output generated in illegal activities (e.g. drug trafficking, poaching, unlicensed brewing) is hidden and omitted from official GDP.\n\n"
                            "6. **Unpaid Household Labour:** Productive services provided by homemakers (cooking, cleaning, childcare) are excluded from national output calculations."
                        )
                    }
                }
            ]
        },
        # Page 8: Real World Asset: Mechanized Rice Agriculture
        {
            "page_number": 8,
            "page_title": "Agricultural Output Accounting: Mwea Rice Scheme",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Irrigated Rice Farming at Mwea Scheme",
                    "content": {
                        "text": "Paddy fields at the Mwea Rice Irrigation Scheme in Kirinyaga County, demonstrating commercial cereal production that feeds directly into national agricultural output records.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Mwea_Rice_Plantation.jpg",
                        "author": "Wikimedia Commons / CC-BY-SA",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Mwea_Rice_Plantation.jpg"
                    }
                }
            ]
        },
        # Page 9: Formative Knowledge Check
        {
            "page_number": 9,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Value Added Calculation Check",
                    "content": {
                        "question": "A timber merchant sells logs to a sawmill for KSh 5,000. The sawmill cuts timber into boards and sells to a carpenter for KSh 12,000. The carpenter makes a table and sells to a furniture showroom for KSh 22,000. The showroom sells to a homeowner for KSh 30,000. What is the total value added in this production chain?",
                        "options": [
                            "KSh 69,000",
                            "KSh 30,000",
                            "KSh 25,000",
                            "KSh 18,000"
                        ],
                        "answer": "B",
                        "explanation": "Total value added equals the sum of incremental values: Merchant (5,000) + Sawmill (12,000 - 5,000 = 7,000) + Carpenter (22,000 - 12,000 = 10,000) + Showroom (30,000 - 22,000 = 8,000) = KSh 30,000. This is always equal to the final consumer retail price."
                    }
                }
            ]
        },
        # Page 10: Summary
        {
            "page_number": 10,
            "page_title": "Lesson 6 Summary & Takeaways",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Key Takeaways: Output Approach",
                    "content": {
                        "text": (
                            "1. The output approach measures national income by summing the value added by all sectors of the economy.\n"
                            "2. Value Added = Gross Sales Revenue minus purchases of intermediate inputs from other firms.\n"
                            "3. Non-market government services are valued at the cost of providing them (wages and materials).\n"
                            "4. Major problems include valuing subsistence agriculture, omitting unrecorded/illegal production, and avoiding double counting."
                        )
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# LESSON 7: National Income Statistics: Uses and Limitations (9 Pages)
# =============================================================================
LESSON_7_DATA = {
    "unit_order": 7,
    "unit_name": "National Income Statistics: Uses and Limitations",
    "lesson_title": "Uses in Economic Planning, Growth Measurement, and Limitations in Standard of Living Comparisons",
    "pages": [
        # Page 1: Goals & Concept
        {
            "page_number": 1,
            "page_title": "Economic Scorecards: What the Statistics Tell Us",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 7.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- State and explain the five key **Uses of National Income Statistics**\n"
                            "- Analyze the limitations of using national income and per capita figures to compare standards of living across different countries\n"
                            "- Explain why a rise in per capita income may NOT necessarily lead to a rise in citizens' living standards\n"
                            "- Evaluate KCSE questions regarding economic welfare vs economic growth"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Compile National Statistics?",
                    "content": {
                        "text": (
                            "National income statistics are not just theoretical figures—they serve as the fundamental economic dashboard of a sovereign nation. "
                            "Without accurate national accounts, the government cannot forecast tax revenues, identify dying industries, or allocate budgetary resources."
                        )
                    }
                }
            ]
        },
        # Page 2: Five Key Uses of National Income Statistics
        {
            "page_number": 2,
            "page_title": "Five Key Uses of National Income Statistics",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "How National Accounts Drive Economic Policy",
                    "content": {
                        "text": (
                            "According to the syllabus, national income data serves five primary functions:\n\n"
                            "1. **Measuring Economic Growth:** By comparing real national income across successive years, economists determine whether the economy is expanding, stagnating, or contracting.\n\n"
                            "2. **Government Economic Planning:** Planners use output and income figures to forecast tax yields, plan annual budgets, and allocate capital to infrastructure and social services.\n\n"
                            "3. **Comparing Standards of Living:** Per capita income figures provide an approximate benchmark for comparing average economic welfare between different nations or historical eras.\n\n"
                            "4. **Analyzing Sectoral Contributions:** Shows the relative output share of agriculture, manufacturing, and services, highlighting sectors requiring policy intervention or investment.\n\n"
                            "5. **Attracting Foreign Investment & Aid:** International institutions (World Bank, IMF) and multinational corporations rely on national income statistics to assess creditworthiness and investment opportunities."
                        )
                    }
                }
            ]
        },
        # Page 3: Comparison Table of Uses
        {
            "page_number": 3,
            "page_title": "Summary Matrix: Uses of National Income Data",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Summary of Uses of National Income Data",
                    "content": {
                        "headers": ["User / Stakeholder", "Specific Purpose", "Practical Example"],
                        "rows": [
                            ["Government Planners", "Resource Allocation & Budgeting", "Allocating funds between rural roads vs urban hospitals based on sectoral output."],
                            ["Central Bank", "Monetary Policy Formulation", "Adjusting lending interest rates based on economic growth speed."],
                            ["Private Investors", "Market Size Evaluation", "Evaluating consumer purchasing power before building new factories."],
                            ["International Lenders", "Credit Risk & Aid Assessment", "Determining eligibility for concessional development loans."]
                        ]
                    }
                }
            ]
        },
        # Page 4: Limitations in International Comparisons
        {
            "page_number": 4,
            "page_title": "Limitations in Comparing Standards of Living Across Countries",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Four Reasons Why International Comparisons Can Be Misleading",
                    "content": {
                        "text": (
                            "Comparing the standard of living between two countries using per capita income figures is subject to four major limitations:\n\n"
                            "1. **Different Currencies and Exchange Rate Distortions:** Converting national incomes to a common currency (like US Dollars) creates distortions because official exchange rates do not reflect actual local purchasing power.\n\n"
                            "2. **Different Tastes, Climates, and Needs:** Citizens in cold countries must spend heavily on domestic heating, snow clearance, and winter clothing, which inflates their GDP without making them happier than tropical citizens who enjoy free natural warmth.\n\n"
                            "3. **Differences in Composition of Output:** A country with high GDP may spend its wealth manufacturing military weaponry, tanks, and ammunition, while a lower-GDP country spends its wealth on public education, parks, and healthcare.\n\n"
                            "4. **Unequal Income Distribution:** Two countries may report the exact same per capita income of $2,000, yet in Country A the income is shared equitably, while in Country B 95% of the wealth is held by 5 families while the majority starve."
                        )
                    }
                }
            ]
        },
        # Page 5: Why Per Capita Growth != Living Standards
        {
            "page_number": 5,
            "page_title": "Why Per Capita Income Growth Does Not Guarantee Better Living",
            "blocks": [
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "The Illusion of Averages (Per Capita Fallacy)",
                    "content": {
                        "text": "An increase in per capita income does not guarantee improved living standards if:\n• **Income Disparity:** The entire income increase goes to the top 1% wealthy elite.\n• **Inflation:** High prices erode purchasing power faster than nominal income rises.\n• **Pollution & Working Hours:** Economic output was achieved by forcing workers to work 16-hour days in toxic, polluted factories.\n• **Population Growth:** If population grows faster than national income, the average real share per person actually drops."
                    }
                }
            ]
        },
        # Page 6: Real World Case Study
        {
            "page_number": 6,
            "page_title": "Case Study: GDP Growth vs Citizen Welfare",
            "blocks": [
                {
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "title": "Country X vs Country Y Scenario",
                    "content": {
                        "text": (
                            "Consider two hypothetical economies:\n\n"
                            "• **Country X:** Reported an astounding 12% GDP growth rate over three years. However, this growth was driven entirely by petroleum extraction owned by foreign billionaires. "
                            "Oil spills contaminated drinking water in rural villages, inflation caused food prices to triple, and slum populations expanded.\n\n"
                            "• **Country Y:** Reported a modest 3% GDP growth rate. However, the government invested in universal primary healthcare, clean piped water in all towns, and paved farm-to-market roads for smallholders.\n\n"
                            "**Conclusion:** Despite Country X's superior GDP figures, the actual standard of living and human welfare in Country Y is vastly superior."
                        )
                    }
                }
            ]
        },
        # Page 7: KCSE Examination Model
        {
            "page_number": 7,
            "page_title": "KCSE Examination Structure: Income Disparity Factors",
            "blocks": [
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "Factors Contributing to Income Disparity in Kenya",
                    "content": {
                        "steps": [
                            "**Unequal Ownership of Productive Resources:** Individuals who inherit fertile land, commercial buildings, and financial capital earn substantial rents, dividends, and interest, whereas resource-poor citizens rely entirely on low-wage manual labour.",
                            "**Differences in Education and Skills:** Highly educated professionals (engineers, surgeons, IT specialists) command high market salaries, whereas uneducated workers are trapped in subordinate, low-paying jobs.",
                            "**Differences in Entrepreneurial Ability:** Innovative individuals willing to take calculated business risks can build highly profitable enterprises, accumulating immense personal wealth.",
                            "**Regional and Infrastructure Disparities:** Concentration of factories, paved roads, and electricity in urban centers provides urban dwellers with far greater economic opportunities than remote rural populations.",
                            "**Corruption and Political Patronage:** Unfair allocation of public tenders and illegal acquisition of state assets unjustly concentrates public wealth in the hands of a politically connected few."
                        ]
                    }
                }
            ]
        },
        # Page 8: Knowledge Check
        {
            "page_number": 8,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Living Standards Limitation Check",
                    "content": {
                        "question": "Outline why a comparison of per capita income between Kenya and a European country with a cold climate may not give a true picture of relative living standards.",
                        "options": [
                            "Because European countries do not record Gross National Product",
                            "Because cold European countries are forced to spend heavily on heating and winter clothing, which inflates their GDP figures without necessarily providing superior welfare",
                            "Because Kenya does not have an active banking system",
                            "Because European currencies are not convertible into Kenyan Shillings"
                        ],
                        "answer": "B",
                        "explanation": "Different climates create different basic needs. A high expenditure on indoor heating and heavy winter gear in Europe inflates their GDP statistics to satisfy a basic survival need that Kenyan citizens receive freely from their natural tropical climate."
                    }
                }
            ]
        },
        # Page 9: Summary
        {
            "page_number": 9,
            "page_title": "Lesson 7 Summary & Takeaways",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Key Takeaways: Uses & Limitations",
                    "content": {
                        "text": (
                            "1. National income statistics are essential for measuring growth, economic planning, and analyzing sectoral performance.\n"
                            "2. Per capita income is an average that conceals income inequality, negative environmental externalities, and inflation.\n"
                            "3. Comparing standards of living across countries is distorted by currency exchange rates, climate differences, and output composition.\n"
                            "4. True economic development requires improvements in health, education, and equality, not merely rising GDP figures."
                        )
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# LESSON 8: Factors Influencing the Level of National Income & KCSE Applications (10 Pages)
# =============================================================================
LESSON_8_DATA = {
    "unit_order": 8,
    "unit_name": "Factors Influencing the Level of National Income & KCSE Applications",
    "lesson_title": "Determinants of National Output, Resource Endowments, and KCSE Examination Mastery",
    "pages": [
        # Page 1: Goals & Concept
        {
            "page_number": 1,
            "page_title": "Why Are Some Nations Rich and Others Poor?",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 8.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify and explain the seven fundamental **Factors Influencing the Level of National Income**\n"
                            "- Describe how labour skills, capital technology, natural resources, entrepreneurship, political stability, and work ethic drive economic capacity\n"
                            "- Master the VLearn Point-Explanation-Context model for KCSE Business Studies essay questions\n"
                            "- Complete an integrated review of the entire National Income topic"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Determinants of National Output",
                    "content": {
                        "text": (
                            "Why is the national income of the United States or Japan so much larger than that of Kenya? Why do some economies grow rapidly while others stagnate? "
                            "National income is not a matter of luck. It is determined by how effectively a nation mobilizes and combines its human, physical, technological, and institutional resources."
                        )
                    }
                }
            ]
        },
        # Page 2: The Seven Determinants of National Income
        {
            "page_number": 2,
            "page_title": "The Seven Key Determinants of National Income",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Detailed Breakdown of the Seven Factors",
                    "content": {
                        "text": (
                            "According to the syllabus, seven primary factors determine the volume of a country's national output:\n\n"
                            "1. **Labour Supply and Skills:** A country with a large, healthy, and highly trained labour force produces high volumes of high-quality goods and services.\n\n"
                            "2. **Capital Equipment and Modern Technology:** Economies equipped with modern automated machinery, tractors, and industrial plants have far higher output per worker than those relying on manual hand tools (jembes).\n\n"
                            "3. **Entrepreneurship:** An abundance of creative, risk-taking entrepreneurs who can effectively organize the other factors of production leads to expanded business creation and higher output.\n\n"
                            "4. **Natural Resource Availability:** Countries richly endowed with fertile soils, reliable rainfall, minerals, deep-sea ports, and forests have a strong natural base for primary and secondary production.\n\n"
                            "5. **Level of Technology:** Advanced scientific methods and digital technology enable more output to be generated from the same amount of physical resources.\n\n"
                            "6. **Political Stability:** A peaceful, secure environment with the rule of law allows long-term investments to flourish. Civil wars and political unrest destroy infrastructure and halt production.\n\n"
                            "7. **Citizens' Attitude Towards Work:** A hard-working, disciplined, time-conscious, and honest workforce generates high productivity, whereas laziness, absenteeism, and corruption drag national income down."
                        )
                    }
                }
            ]
        },
        # Page 3: Visual Network Diagram
        {
            "page_number": 3,
            "page_title": "Visual Model: Determinants of Economic Capacity",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Network Diagram of Factors Influencing National Income",
                    "svg_content": SVG_FACTORS_INFLUENCING_NI,
                    "content": {
                        "text": "Diagram showing how labour skills, capital, entrepreneurship, natural resources, technology, political stability, and work ethic all feed into determining the level of National Income."
                    }
                }
            ]
        },
        # Page 4: Real World Asset: Mechanized Transport & Infrastructure
        {
            "page_number": 4,
            "page_title": "Capital Infrastructure in Kenya: SGR and Logistics",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Modern Transport Infrastructure in Kenya",
                    "content": {
                        "text": "The Standard Gauge Railway passenger and freight train operating between Nairobi and Mombasa, demonstrating modern capital investment that reduces freight transit times and lowers transport costs across the national economy.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
                        "author": "Wikimedia Commons / CC-BY-SA",
                        "licensing": "CC BY-SA 4.0",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
                    }
                }
            ]
        },
        # Page 5: Master KCSE Model Question 1
        {
            "page_number": 5,
            "page_title": "KCSE Examination Question 1: Output Approach Inaccuracies",
            "blocks": [
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "Explain 5 reasons why the output approach may yield inaccurate results (10 Marks)",
                    "content": {
                        "steps": [
                            "**1. Inaccuracy of the Subsistence Sector:** In agricultural countries like Kenya, a large proportion of farm produce is consumed directly by the farming households and never passes through the formal market, leading to significant underestimation of total national output.",
                            "**2. The Danger of Double Counting:** It is difficult to separate primary raw materials from intermediate inputs, creating a constant risk of counting the same good twice (e.g. counting sugarcane sold to a factory and the sugar sold to consumers).",
                            "**3. Difficulty in Valuing Non-Market Public Services:** Essential government services like state healthcare, security, and public education are not sold at commercial market prices; valuing them at the cost of civil servant salaries may overstate or understate their true economic worth.",
                            "**4. Distortion from Rapid Price Fluctuations (Inflation):** Rapid inflation artificially inflates the nominal value of output over time without any real increase in the physical quantity of goods produced.",
                            "**5. Unrecorded Output from Illegal and Black Market Activities:** Economic output generated in illegal activities (e.g. smuggling, drug trafficking, unlicensed operations) is intentionally concealed from official government records, resulting in understated national income."
                        ]
                    }
                }
            ]
        },
        # Page 6: Master KCSE Model Question 2
        {
            "page_number": 6,
            "page_title": "KCSE Examination Question 2: Per Capita Income Limitations",
            "blocks": [
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "Explain 4 reasons why a rise in per capita income may not raise living standards (8 Marks)",
                    "content": {
                        "steps": [
                            "**1. Disparity in Income Distribution:** Per capita income is purely a mathematical average; if the increased income is concentrated in the hands of a small wealthy minority, the living standards of ordinary citizens remain low or worsen.",
                            "**2. High Inflation Rate:** If general commodity prices rise faster than nominal income, real purchasing power drops, meaning citizens can afford fewer goods and services despite a higher statistical per capita income.",
                            "**3. Negative Externalities (Pollution & Environmental Damage):** Higher output achieved through severe factory pollution, deforestation, or exhausting working hours degrades public health and overall quality of life.",
                            "**4. Production of Capital or Military Goods:** If the extra national output consists of military armaments or heavy machinery rather than essential consumer goods (food, shelter, healthcare), current consumer living standards will not improve."
                        ]
                    }
                }
            ]
        },
        # Page 7: Master Summary Table
        {
            "page_number": 7,
            "page_title": "Comprehensive Topic Review Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Master Synthesis of the Three Measurement Approaches",
                    "content": {
                        "headers": ["Feature", "Expenditure Approach", "Income Approach", "Output Approach"],
                        "rows": [
                            ["What it Sums", "Total final spending by all sectors.", "Total factor rewards earned in production.", "Total value added across all industrial sectors."],
                            ["Master Formula", "$GNE = C + I + G + (X - M)$", "$GNI = \\text{Factor Incomes} + \\text{Retained Profit} - (\\text{Transfers} + \\text{Stock Appr})$", "$\\text{GDP} = \\sum \\text{Value Added by Sectors}$"],
                            ["Valuation Base", "Market Prices (adjust to Factor Cost by $+ \\text{Subsidies} - \\text{Taxes}$)", "Naturally arrives at Factor Cost", "Naturally arrives at Factor Cost"],
                            ["Major Challenge", "Double counting intermediate goods & tracking informal cash spending", "Tax evasion and separating transfer payments", "Valuing subsistence farming & illegal unrecorded output"]
                        ]
                    }
                }
            ]
        },
        # Page 8: Comprehensive Integrated Calculation
        {
            "page_number": 8,
            "page_title": "Master Review: Comprehensive KCSE Calculation",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Integrated National Income Examination Synthesis",
                    "content": {
                        "intro": "The following figures were extracted from the economic accounts of Country M for the year ended 2025 (in KSh billions):\n\n- Consumer Expenditure ($C$) = KSh 400B\n- Private Capital Investment ($I$) = KSh 90B\n- Government Expenditure ($G$) = KSh 110B\n- Total Exports ($X$) = KSh 60B\n- Total Imports ($M$) = KSh 80B\n- Indirect Taxes = KSh 18B\n- Government Subsidies = KSh 8B\n- Depreciation = KSh 15B\n- Total Population = 25 million people\n\nCalculate GNE at Market Prices, GNE at Factor Cost, National Income, and Per Capita Income.",
                        "steps": [
                            "**Step 1: Calculate GNE at Market Prices:**\n$$\\text{GNE at Market Prices} = C + I + G + (X - M)$$\n$$\\text{GNE at Market Prices} = 400 + 90 + 110 + (60 - 80) = 600 - 20 = \\mathbf{580\\text{ billion KSh}}$$",
                            "**Step 2: Convert to Factor Cost:**\n$$\\text{GNE at Factor Cost} = \\text{GNE at Market Prices} + \\text{Subsidies} - \\text{Indirect Taxes}$$\n$$\\text{GNE at Factor Cost} = 580 + 8 - 18 = \\mathbf{570\\text{ billion KSh}}$$",
                            "**Step 3: Calculate National Income (Net National Expenditure):**\n$$\\text{National Income} = \\text{GNE at Factor Cost} - \\text{Depreciation}$$\n$$\\text{National Income} = 570 - 15 = \\mathbf{555\\text{ billion KSh}}$$",
                            "**Step 4: Calculate Per Capita Income:**\n$$\\text{Per Capita Income} = \\frac{555,000\\text{ million}}{25\\text{ million}} = \\mathbf{\\text{KSh } 22,200}$$"
                        ]
                    }
                }
            ]
        },
        # Page 9: Final Formative Assessment
        {
            "page_number": 9,
            "page_title": "Final Topic Mastery Check",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Comprehensive Topic Mastery Check",
                    "content": {
                        "question": "Which of the following would cause Kenya's National Income to increase in real terms?",
                        "options": [
                            "An increase in the general prices of basic commodities due to inflation",
                            "An increase in the number of second-hand cars sold between Kenyan citizens",
                            "Adoption of modern mechanized agricultural technology and enhanced technical training for workers",
                            "An increase in the total student bursary grants distributed by the government"
                        ],
                        "answer": "C",
                        "explanation": "Adoption of modern technology and skilled labour directly increases the physical production efficiency and productivity of the economy, expanding real national output. Inflation only increases nominal values, second-hand sales are not new production, and bursaries are transfer payments."
                    }
                }
            ]
        },
        # Page 10: Topic 1 Completion
        {
            "page_number": 10,
            "page_title": "Topic 1 Complete: National Income Mastered!",
            "blocks": [
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Topic 1 Final Summary",
                    "content": {
                        "text": (
                            "Congratulations! You have completed Form 4 Business Studies Topic 1: National Income.\n\n"
                            "**What You Have Mastered:**\n"
                            "- The core definitions: National Income, GDP, NDP, GNP, NNP, and Per Capita Income.\n"
                            "- The circular flow model, real vs money flows, and the equilibrium condition ($S + T + M = I + G + X$).\n"
                            "- The Expenditure Approach, market price to factor cost adjustments ($+ \\text{subsidies} - \\text{taxes}$), and exclusions.\n"
                            "- The Income Approach, factor rewards vs transfer payments, and inventory adjustments.\n"
                            "- The Output Approach, multi-stage value-added chains, and avoiding double counting.\n"
                            "- The uses of national accounts in planning and limitations in comparing international living standards.\n"
                            "- The key determinants that drive national economic wealth."
                        )
                    }
                }
            ]
        }
    ]
}
