"""
VLearn CBC Grade 10 Business Studies — Topic 7: Social Responsibility of Business
Full Structured Lesson Card Definitions (Lessons 1 to 6)
"""

from curriculum.cbc_grade10_business_studies_topic7_svgs import (
    SVG_STAKEHOLDER_ECOSYSTEM,
    SVG_COMMUNITY_CSR_PILLARS,
    SVG_CSR_CHALLENGES_MATRIX,
    SVG_SCHOOL_PROJECT_DESIGN_FRAMEWORK,
    SVG_PROJECT_IMPLEMENTATION_LIFECYCLE,
    SVG_CSR_MONITORING_EVALUATION_MATRIX
)

TOPIC_7_LESSONS = [
    # =========================================================================
    # LESSON 1: Justifying the Need for Social Responsibility of a Business
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Justifying the Need for Social Responsibility",
        "unit_description": "The ethical imperative, stakeholder interconnectedness, brand equity, talent retention, and mitigation of negative externalities in modern business practice.",
        "lesson_title": "Justifying the Need for Social Responsibility of a Business",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Educational CSR Sponsorship in Kenya",
                    "content": {
                        "title": "Kenyan Secondary School Students in Class",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Kenyan_Samburu_children_in_a_classroom.jpg",
                        "caption": "Secondary school students in a learning session, illustrating human capital development and educational CSR initiatives such as Equity Bank's Wings to Fly.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define Social Responsibility (SR), stakeholders, sustainability, and externalities\n- Distinguish between a firm's legal obligations and voluntary social responsibilities\n- Explain the 'Good Neighbor' and 'Shared Value' economic principles\n- Analyze the six core business justifications for investing in community social responsibility"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Social Responsibility and Stakeholder Interconnectedness",
                    "content": {
                        "term": "Social Responsibility (SR)",
                        "definition": "A business enterprise's ethical obligation to make decisions and take actions that positively benefit society, stakeholders, and the natural environment, going beyond what is strictly mandated by law or short-term economic profit."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Good Neighbor and the Shared Well Analogy",
                    "content": {
                        "text": "Imagine living in a village with a single shared water well:\n\n- **The Bad Neighbor:** Draws water only for their compound, dumps household trash near the well, and refuses to contribute timber or labor when the bucket breaks. Soon, the water turns foul, the community turns hostile, and the neighbor's own household suffers.\n- **The Good Neighbor:** Keeps the surrounding soil clean, contributes to repairs, and assists elderly villagers. When this neighbor's roof is damaged by wind, the entire community rushes to help repair it.\n\nIn the commercial world, a business operates like a neighbor inside a society. An enterprise cannot flourish sustainably in a community stricken by poverty, poor health, environmental collapse, or hostility. By investing in its stakeholders, a business secures its own long-term operating license and commercial future."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Enterprise Stakeholder Ecosystem Architecture",
                    "content": {
                        "title": "The Enterprise Stakeholder Ecosystem",
                        "caption": "Vector diagram illustrating the bidirectional value exchanges between the enterprise and its internal and external stakeholders, filtered through ethical duty and externalities.",
                        "svg_content": SVG_STAKEHOLDER_ECOSYSTEM
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Justification Matrix: Business Drivers for Social Responsibility",
                    "content": {
                        "headers": ["Justification Driver", "Core Economic Rationale", "Risk of Inaction", "Kenyan Enterprise Example"],
                        "rows": [
                            ["Ethical Duty & Resource Reciprocity", "Enterprises consume societal resources (infrastructure, labor, water) and must replenish them", "Public hostility, community blockades, and loss of operating legitimacy", "BAMBURI CEMENT rehabilitating limestone quarries into Haller Park ecological sanctuary"],
                            ["Long-Term Commercial Sustainability", "Healthy, prosperous communities form resilient consumer markets for company outputs", "Market contraction, declining disposable income, and rising local poverty", "EQUITY BANK sponsoring Wings to Fly scholars who become future depositors and leaders"],
                            ["Brand Equity & Reputation", "Consumers actively reward ethical, transparent, and community-conscious enterprises", "Customer boycotts, negative social media backlash, and loss of market share", "SAFARICOM Foundation funding county hospital maternity wings and clean water boreholes"],
                            ["Talent Attraction & Retention", "Top-tier professionals prefer working for mission-driven, socially responsible firms", "High employee turnover, low workforce morale, and recruitment brain drain", "EABL offering comprehensive staff wellness, parental leave, and university tuition support"],
                            ["Mitigating Negative Externalities", "Proactively eliminating pollution prevents costly litigation, fines, and regulatory clampdowns", "Heavy National Environment Management Authority (NEMA) penalties and factory shutdown orders", "KENCHIC installing bio-digesters to convert poultry waste into clean biogas and organic fertilizer"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Cost-Benefit Analysis of Shared Value Investment",
                    "content": {
                        "intro": "Oasis Dairy Processor in Limuru evaluates a proposal to invest in a solar-powered milk cooling and collection center for 120 local dairy smallholders. The capital outlay is $C_0 = \\text{KES } 200,000$. Without the cooler, milk spoilage causes an average quarterly loss of $L_{\\text{spoil}} = \\text{KES } 70,000$, and farmer defection to competitors costs $\\text{KES } 80,000$ in lost quarterly revenue. Installing the cooler reduces spoilage to zero and expands supplier milk volume, generating an additional net quarterly revenue gain of $\\Delta R = \\text{KES } 50,000$. Calculate the Total Net Quarterly Economic Benefit ($B_{\\text{net}}$) and the Investment Payback Period ($T$).",
                        "steps": [
                            "**Step 1: Given Information:** Initial capital expenditure $C_0 = \\text{KES } 200,000$. Spoilage loss avoided per quarter $L_{\\text{spoil}} = \\text{KES } 70,000$. Retained revenue from prevented supplier defection $R_{\\text{retained}} = \\text{KES } 80,000$. New revenue gain from increased milk delivery $\\Delta R = \\text{KES } 50,000$.",
                            "**Step 2: Formula:** Total Net Quarterly Economic Benefit: $$B_{\\text{net}} = L_{\\text{spoil}} + R_{\\text{retained}} + \\Delta R$$. Payback Period (in quarters): $$T = \\frac{C_0}{B_{\\text{net}}}$$.",
                            "**Step 3: Substitution:** Compute the quarterly benefit: $$B_{\\text{net}} = \\text{KES } 70,000 + \\text{KES } 80,000 + \\text{KES } 50,000$$. Payback ratio: $$T = \\frac{\\text{KES } 200,000}{\\text{KES } 200,000}$$.",
                            "**Step 4: Calculation:** $$B_{\\text{net}} = \\text{KES } 200,000\\text{ per quarter}$$. $$T = 1.0\\text{ quarter } (3\\text{ months})$$.",
                            "**Step 5: Final Answer:** The social investment delivers a net economic benefit of $\\text{KES } 200,000$ every quarter and fully repays its initial $\\text{KES } 200,000$ capital expenditure within exactly 1 quarter (3 months). After Month 3, the project yields $\\text{KES } 800,000$ in annual ongoing value.",
                            "**Step 6: Economic Interpretation & Pitfall:** Investing in community milk cooling represents 'Shared Value'—solving a community challenge (preventing milk spoilage for smallholders) simultaneously solves an enterprise problem (securing reliable raw milk supply). *Common Pitfall:* Viewing CSR expenditures solely as unrecoverable financial overhead rather than strategic capital investments that yield measurable operational returns."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Equity Bank's 'Wings to Fly' Program",
                    "content": {
                        "title": "Human Capital Development and Strategic Shared Value",
                        "text": "Equity Group Foundation established the 'Wings to Fly' scholarship program in partnership with Mastercard Foundation and the German Government (KfW). To date, the program has funded complete secondary school tuition, books, uniforms, and mentorship for over 30,000 academically gifted but financially disadvantaged Kenyan youth.\n\nBeyond humanitarian philanthropy, 'Wings to Fly' has created immense strategic value: it produces high-caliber university graduates who enter Equity Bank's executive leadership pipeline, strengthens brand loyalty among millions of Kenyan families, and positions Equity Bank as Kenya's most admired financial brand."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Corporate Social Responsibility and Business Ethics",
                    "content": {
                        "title": "Understanding Corporate Social Responsibility in Modern Economics",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Comprehensive pedagogical video analyzing the economic foundations of CSR, stakeholder theory, shared value, and mitigating business externalities."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Concept of Shared Value",
                    "content": {
                        "question": "A tea processing factory in Kericho invests KES 500,000 to construct an all-weather feeder road connecting remote smallholder tea farms to its factory. Which of the following best describes this business action?",
                        "options": [
                            "A wasteful expenditure of company funds that only serves county government responsibilities",
                            "An example of creating shared value, where community mobility improves while the factory reduces tea leaf transport spoilage and collection delays",
                            "A mandatory tax paid directly to the Kenya Revenue Authority (KRA)",
                            "An illegal financial transaction that violates the Companies Act"
                        ],
                        "correct": "B",
                        "explanation": "Creating shared value involves policies and practices that enhance the competitiveness of a business while simultaneously advancing the economic and social conditions in the communities in which it operates."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Externalities and Ethical Duty",
                    "content": {
                        "question": "A textile factory in Thika dumps untreated dye effluents into the Chania River, polluting downstream farming water. In business economics, this is classified as:",
                        "options": [
                            "A positive financial externality that maximizes shareholder dividend returns",
                            "A negative environmental externality that the enterprise has an ethical and legal duty to eliminate and remediate",
                            "A standard commercial practice exempted from NEMA regulatory oversight",
                            "An internal stakeholder conflict between factory managers and machine operators"
                        ],
                        "correct": "B",
                        "explanation": "A negative externality is an unintended harmful side-effect of commercial activity imposed on third parties (the local farming community and river ecosystem). Ethical business practice mandates neutralizing such harm."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 1 Synthesis & Key Takeaways",
                    "content": {
                        "text": "### Summary of Core Principles\n\n- **Beyond the Bottom Line:** Social Responsibility requires enterprises to look beyond short-term financial profit ($$\\text{Profit}$$) to embrace social ($$\\text{People}$$) and environmental ($$\\text{Planet}$$) stewardship.\n- **Stakeholder Reciprocity:** Businesses rely on public infrastructure, human labor, and natural resources; they hold a moral and commercial duty to reinvest in societal well-being.\n- **Commercial Payoffs:** Proactive CSR enhances brand reputation, attracts high-performing employees, builds customer loyalty, and mitigates severe regulatory fines.\n- **Shared Value:** The most effective social investments solve community challenges while strengthening the business's core supply chain and market stability."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Social Responsibility Activities in the Community
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Social Responsibility Activities in the Community",
        "unit_description": "Core pillars of community social responsibility: philanthropy, environmental conservation, ethical labor, fair sourcing, health and education, and local economic development.",
        "lesson_title": "Social Responsibility Activities in the Community",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Ethical Sourcing & Smallholder Empowerment in Kenya",
                    "content": {
                        "title": "Tea Picking and Smallholder Farmer Empowerment",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Tea_picking.jpg",
                        "caption": "Agricultural tea picking and smallholder farmer empowerment in Kenya, demonstrating ethical sourcing, fair trade, and rural economic development partnerships.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and categorize the six major pillars of community social responsibility\n- Differentiate between pure philanthropic donations and structural economic empowerment\n- Explain how ethical labor practices and ethical sourcing build sustainable supply chains\n- Analyze real Kenyan enterprise initiatives across environmental conservation and health"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Community Social Responsibility Pillars",
                    "content": {
                        "term": "Community Social Responsibility",
                        "definition": "The multi-faceted operational framework through which a commercial enterprise actively contributes to community welfare, environmental protection, fair labor standards, and inclusive economic growth."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Shared Umbrella Analogy",
                    "content": {
                        "text": "Picture a sudden heavy downpour at a bus stage in Nakuru. You have a large, sturdy golf umbrella:\n\n- **Selfish Isolation:** You stand alone under the canopy while children and elders next to you get drenched. You remain dry, but resentment and isolation grow around you.\n- **Sharing the Umbrella:** You step closer and invite three others under the shelter. Your canopy still shields you, but you have created a warm, cooperative haven.\n\nIn business, 'sharing the umbrella' means deploying your capital, technological tools, logistical networks, and skills to shield vulnerable members of the community from poverty, illiteracy, and environmental degradation."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Six Pillars of Community Social Responsibility",
                    "content": {
                        "title": "Six Core Pillars of Community Social Responsibility",
                        "caption": "Vector taxonomy outlining philanthropy, environmental sustainability, ethical labor, ethical sourcing, health/education, and local economic development.",
                        "svg_content": SVG_COMMUNITY_CSR_PILLARS
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Detailed Taxonomy of Community CSR Activities",
                    "content": {
                        "headers": ["CSR Pillar", "Primary Focus", "Key Operational Actions", "Kenyan Business Application"],
                        "rows": [
                            ["1. Philanthropy & Donations", "Immediate charitable aid and emergency relief", "Cash grants, disaster relief food, building school libraries, donating desks", "BARAKA CEMENT donating KES 50,000 to build a public community library in Athi River"],
                            ["2. Environmental Conservation", "Minimizing ecological damage and conserving nature", "Tree planting, solar energy adoption, zero plastic packaging, water recycling", "LIMURU TEA switching from synthetic plastic wrappers to 100% biodegradable paper pouches"],
                            ["3. Ethical Labor Practices", "Internal workplace justice, safety, and equity", "Paying living wages above statutory minimums, comprehensive medical cover, safety gear", "FLOWER FARMS in Naivasha providing on-site daycare, subsidized housing, and protective respirators"],
                            ["4. Ethical Sourcing & Trade", "Supply chain fairness and anti-exploitation", "Purchasing from certified fair-trade cooperatives, prohibiting child labor, local sourcing", "A leading supermarket chain purchasing 100% of honey from youth beekeeping SACCOs in Kitui"],
                            ["5. Health & Education Support", "Developing human capability and community vitality", "Secondary school scholarships, maternal health clinics, community wellness screenings", "A private hospital in Eldoret hosting free monthly diabetes and hypertension checkups"],
                            ["6. Economic Development", "Stimulating grassroots commerce and enterprise", "Micro-loans for women traders, youth vocational apprenticeships, vendor coaching", "KAKUZI PLC providing avocado grafting seedlings, agronomic training, and global export access"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Economic Impact of Ethical Smallholder Sourcing",
                    "content": {
                        "intro": "Kakuzi PLC operates an ethical smallholder avocado sourcing program in Murang'a County covering $N = 250$ smallholder farming households. Under predatory local middlemen, farmers received a farm-gate price of $P_{\\text{broker}} = \\text{KES } 25\\text{ per kg}$. Under Kakuzi's direct ethical procurement scheme, farmers receive a guaranteed fair-trade price of $P_{\\text{ethical}} = \\text{KES } 42\\text{ per kg}$. Each farmer harvests and delivers an average seasonal yield of $Q = 800\\text{ kg}$. Calculate: (a) The additional seasonal income earned by each individual farmer ($\\Delta I_{\\text{farmer}}$), and (b) The total direct economic injection delivered into the Murang'a rural community ($I_{\\text{community}}$).",
                        "steps": [
                            "**Step 1: Given Information:** Number of smallholder farmers $N = 250$. Average avocado yield per farmer $Q = 800\\text{ kg}$. Broker price $P_{\\text{broker}} = \\text{KES } 25\\text{/kg}$. Ethical direct price $P_{\\text{ethical}} = \\text{KES } 42\\text{/kg}$.",
                            "**Step 2: Formula:** Additional Income per Farmer: $$\\Delta I_{\\text{farmer}} = Q \\times (P_{\\text{ethical}} - P_{\\text{broker}})$$. Total Community Economic Injection: $$I_{\\text{community}} = N \\times \\Delta I_{\\text{farmer}}$$.",
                            "**Step 3: Substitution:** Compute price premium: $$\\Delta P = \\text{KES } 42 - \\text{KES } 25 = \\text{KES } 17\\text{/kg}$$. Compute individual gain: $$\\Delta I_{\\text{farmer}} = 800\\text{ kg} \\times \\text{KES } 17$$. Total injection: $$I_{\\text{community}} = 250 \\times \\Delta I_{\\text{farmer}}$$.",
                            "**Step 4: Calculation:** $$\\Delta I_{\\text{farmer}} = \\text{KES } 13,600\\text{ per farmer}$$. $$I_{\\text{community}} = 250 \\times \\text{KES } 13,600 = \\text{KES } 3,400,000$$.",
                            "**Step 5: Final Answer:** (a) Each smallholder farmer earns an additional $\\text{KES } 13,600$ per season. (b) The ethical sourcing program injects a total of $\\text{KES } 3,400,000$ directly into rural households, funding school fees, improved housing, and local commerce.",
                            "**Step 6: Economic Interpretation & Pitfall:** Ethical sourcing creates lasting wealth creation rather than dependency. By bypassing exploitative intermediaries, the enterprise guarantees consistent export-grade quality while revitalizing the rural economy. *Common Pitfall:* Confusing one-off cash handouts (philanthropy) with structural market-access programs (economic development)."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Kakuzi PLC Smallholder Avocado Outgrower Scheme",
                    "content": {
                        "title": "Transforming Rural Livelihoods Through Commercial Integration",
                        "text": "In Murang'a County, agricultural exporter Kakuzi PLC established a formal smallholder avocado outgrower program. Smallholders receive certified disease-free Hass avocado seedlings, field training from qualified agronomists on global chemical residue standards (GlobalGAP), and direct access to European and Asian export markets.\n\nThis initiative bridges the gap between commercial agribusiness and family farming, ensuring high export revenues for farmers while securing stable fruit supply volumes for Kakuzi's packhouses."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Community Social Responsibility Pillars in Action",
                    "content": {
                        "title": "Sustainable Supply Chains and Community CSR in Kenya",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "Exploration of fair trade sourcing, environmental sustainability, ethical labor, and local enterprise development across East Africa."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Classifying CSR Pillars",
                    "content": {
                        "question": "A supermarket chain in Nairobi signs a multi-year contract to purchase all its fresh vegetables directly from a certified women's organic farming cooperative in Kiambu, paying prices 20% above local broker rates. Under which CSR pillar does this fall?",
                        "options": [
                            "Philanthropy and charitable donations",
                            "Ethical sourcing and local economic development",
                            "Government tax compliance",
                            "Internal corporate restructuring"
                        ],
                        "correct": "B",
                        "explanation": "Ethical sourcing involves fair trade purchasing practices that eliminate predatory brokers, guarantee fair producer prices, and empower grassroots producers."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Environmental Sustainability",
                    "content": {
                        "question": "Limuru Tea Factory replaces heavy furnace oil boilers with solar thermal arrays and biomass briquettes made from compressed agricultural waste. What primary CSR benefit is achieved?",
                        "options": [
                            "Increasing the statutory excise tax payable to the national treasury",
                            "Reducing the factory's carbon footprint and mitigating negative environmental externalities",
                            "Forcing competitor factories to halt production immediately",
                            "Eliminating the need for employee medical insurance"
                        ],
                        "correct": "B",
                        "explanation": "Adopting renewable energy and recycling agricultural waste is a core environmental sustainability practice that protects air quality, reduces greenhouse emissions, and conserves forest resources."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 2 Synthesis & Key Takeaways",
                    "content": {
                        "text": "### Summary of Core Principles\n\n- **Six Pillars of Impact:** Community CSR encompasses Philanthropy, Environmental Care, Ethical Labor, Ethical Sourcing, Health/Education, and Local Economic Development.\n- **Internal Precedes External:** A business must uphold ethical labor standards and fair wages internally before claiming credit for external community charity.\n- **Empowerment Over Charity:** Initiatives that build skills, provide fair market access, and enhance rural producer incomes create permanent economic transformation.\n- **Ecosystem Health:** When businesses protect local rivers, forests, and smallholders, they ensure the perpetual sustainability of their own raw material supply."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Challenges Faced by Businesses in Social Responsibility
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Challenges Faced by Businesses in Social Responsibility",
        "unit_description": "Financial costs, social ROI measurement difficulties, conflicting stakeholder demands, greenwashing risks, and supply chain ethical governance.",
        "lesson_title": "Challenges Faced by Businesses in Social Responsibility",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Industrial Manufacturing Costs and Operational Tradeoffs",
                    "content": {
                        "title": "Local Manufacturing and Fabrication in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
                        "caption": "Local industrial and manufacturing operations in Kenya, illustrating the cost and operational tradeoffs businesses face when adopting green production practices.",
                        "author": "Harold Odhiambo Otieno",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Analyze the financial burdens and margin pressures created by CSR adoption\n- Explain the challenge of measuring intangible social Return on Investment (ROI)\n- Evaluate conflicts between short-term shareholder profit demands and long-term community expectations\n- Define 'Greenwashing' and explain why cosmetic PR destroys corporate credibility"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "CSR Challenges and Greenwashing",
                    "content": {
                        "term": "Greenwashing",
                        "definition": "The deceptive or misleading practice of exaggerating or fabricating an enterprise's environmental or social contributions for public relations (PR) benefit, while failing to address or actively concealing core negative operational impacts."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Heavy Pack on Mount Longonot Analogy",
                    "content": {
                        "text": "Imagine hiking up Mount Longonot with a hiking group:\n\n- **The Light Hiker:** Carries only a small water bottle. They move briskly, expend minimal energy, and reach the summit effortlessly. This represents a firm focused solely on short-term profit with zero social spending.\n- **The Dedicated Hiker:** Carries a heavy 25-kilogram backpack loaded with emergency stretchers, oxygen tanks, blankets, and extra food for everyone. Their noble mission slows their pace, drains their physical stamina, and risks physical collapse if they lack sufficient endurance.\n\nIn business, carrying the extra cost of solar transitions, fair wages, and school donations requires robust capital reserves and strategic stamina. If a small business overextends itself without adequate revenue, it risks insolvency."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Managerial and Financial Hurdles in Social Responsibility",
                    "content": {
                        "title": "Strategic & Operational Challenges in Social Responsibility",
                        "caption": "Vector diagram illustrating financial margin squeeze, social ROI intangibility, stakeholder conflict balancing, greenwashing risks, and mitigation strategies.",
                        "svg_content": SVG_CSR_CHALLENGES_MATRIX
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Analysis: The 5 Major CSR Challenges",
                    "content": {
                        "headers": ["Challenge Area", "Root Operational Cause", "Direct Commercial Consequence", "Managerial Mitigation Solution"],
                        "rows": [
                            ["1. High Financial Outlays & Margin Squeeze", "Eco-friendly raw materials (e.g., organic oils, solar kits) cost 30-50% more than synthetic alternatives", "Higher production costs force price hikes, risking customer defection to unethical competitors", "Implement lean manufacturing, seek green energy subsidies, and negotiate volume supplier discounts"],
                            ["2. Intangible Social ROI Measurement", "Brand goodwill, employee pride, and community harmony take years to reflect on balance sheets", "Short-term investors and creditors question CSR budgets during cash crunches", "Establish Social Return on Investment (SROI) frameworks and non-financial ESG milestone tracking"],
                            ["3. Conflicting Stakeholder Demands", "Shareholders want maximum immediate dividends; workers want raises; community wants public amenities", "Management deadlock, prolonged labor strikes, or hostile community protests", "Conduct structured stakeholder mapping and transparent multi-party priority dialogues"],
                            ["4. The Temptation of Greenwashing", "Pressure to look ethical leads firms to run superficial PR campaigns without cleaning up core waste", "Public exposure leads to brand boycotts, viral social media ridicule, and severe loss of trust", "Adopt radical transparency, undergo independent third-party audits, and fix core pollution first"],
                            ["5. Supply Chain Complexity", "Auditing hundreds of rural outgrowers or multi-tier suppliers for labor and environmental compliance is costly", "Undetected child labor or environmental infractions at supplier farms damage parent brand", "Introduce supplier codes of conduct, digital traceability, and collaborative outgrower training"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Break-Even Analysis of Green Input Transition",
                    "content": {
                        "intro": "Bora Soap Manufacturers in Nakuru produces laundry bar soap. Under conventional synthetic production, monthly fixed costs are $F = \\text{KES } 350,000$, variable cost per bar is $V_1 = \\text{KES } 50$, and selling price is $P_1 = \\text{KES } 85$. The firm transitions to 100% biodegradable organic coconut oil to protect river ecosystems, raising variable cost to $V_2 = \\text{KES } 70$ per bar. To recover costs, Bora Soap adjusts selling price to $P_2 = \\text{KES } 110$. Calculate: (a) Original Break-Even Volume ($Q_1$), (b) New Break-Even Volume ($Q_2$), and (c) The Change in Break-Even Output ($\\Delta Q$).",
                        "steps": [
                            "**Step 1: Given Information:** Fixed costs $F = \\text{KES } 350,000$. Conventional scenario: $P_1 = \\text{KES } 85$, $V_1 = \\text{KES } 50$. Green production scenario: $P_2 = \\text{KES } 110$, $V_2 = \\text{KES } 70$.",
                            "**Step 2: Formula:** Break-Even Volume: $$Q = \\frac{F}{P - V} = \\frac{F}{\\text{Unit Contribution Margin}}$$. Change in Break-Even Output: $$\\Delta Q = Q_2 - Q_1$$.",
                            "**Step 3: Substitution:** Compute original contribution: $$\\text{CM}_1 = \\text{KES } 85 - \\text{KES } 50 = \\text{KES } 35$$. Original Break-Even: $$Q_1 = \\frac{\\text{KES } 350,000}{\\text{KES } 35}$$. Compute green contribution: $$\\text{CM}_2 = \\text{KES } 110 - \\text{KES } 70 = \\text{KES } 40$$. Green Break-Even: $$Q_2 = \\frac{\\text{KES } 350,000}{\\text{KES } 40}$$.",
                            "**Step 4: Calculation:** $$Q_1 = 10,000\\text{ bars per month}$$. $$Q_2 = 8,750\\text{ bars per month}$$. $$\\Delta Q = 8,750 - 10,000 = -1,250\\text{ bars}$$.",
                            "**Step 5: Final Answer:** (a) Original Break-Even = $10,000\\text{ bars}$. (b) New Green Break-Even = $8,750\\text{ bars}$. (c) Break-even output decreases by $1,250\\text{ bars}$ ($12.5\\%$ reduction in operational sales risk).",
                            "**Step 6: Economic Interpretation & Pitfall:** By pricing the eco-friendly soap at $\\text{KES } 110$, unit contribution margin rose from $\\text{KES } 35$ to $\\text{KES } 40$. Consequently, the firm needs to sell fewer bars to cover its fixed overhead. *Common Pitfall:* Assuming green transitions always increase financial risk—if consumers value eco-friendly products and accept a modest price premium, commercial margins and resilience can actually improve."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: The Dilemma of Nakuru Soap Manufacturers",
                    "content": {
                        "title": "Balancing Environmental Ethics with Consumer Price Sensitivity",
                        "text": "Bora Soap Manufacturers in Nakuru faced a dilemma: switching from petroleum-based detergents to organic coconut oil would prevent chemical lather from entering Lake Nakuru, protecting flamingo habitats and aquatic life. However, doing so increased wholesale costs by 40%.\n\nIn price-sensitive open-air retail markets in Nakuru, low-income shoppers initially resisted the higher price and bought cheaper synthetic detergent bars. Bora Soap overcame this challenge by introducing smaller 100g 'kadogo' economy packs priced at KES 25, educating consumers on garment preservation benefits, and partnering with local green tourism hotels that bought eco-soap in bulk."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Challenges and Tradeoffs in Corporate Social Responsibility",
                    "content": {
                        "title": "Financial Dilemmas, Greenwashing, and Stakeholder Governance",
                        "youtube_id": "7_j5N5V1N9c",
                        "url": "https://www.youtube.com/watch?v=7_j5N5V1N9c",
                        "description": "Critical analysis of the real-world obstacles businesses face when implementing ethical practices, managing cost pressures, and avoiding greenwashing."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Understanding Greenwashing",
                    "content": {
                        "question": "A beverage bottling firm in Kenya spends KES 2,000,000 on billboard advertisements highlighting its sponsorship of a high-school drama festival, while secretly dumping 10,000 litres of toxic acid wash into a local river every week. This behavior is a textbook example of:",
                        "options": [
                            "Sustainable circular economy leadership",
                            "Corporate greenwashing and superficial public relations deception",
                            "Strict compliance with NEMA industrial guidelines",
                            "Maximizing positive community externalities"
                        ],
                        "correct": "B",
                        "explanation": "Greenwashing occurs when a company uses high-profile charitable donations or advertising to present an ethical public image while continuing destructive environmental or labor practices."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Small Enterprise Constraints",
                    "content": {
                        "question": "Why do small informal micro-enterprises and sole proprietorships find it significantly more challenging to execute large-scale CSR projects compared to multinational corporations?",
                        "options": [
                            "Micro-enterprise owners are legally prohibited from doing good deeds",
                            "Micro-enterprises operate on thin profit margins and lack dedicated CSR budgets, reserve capital, and specialized compliance personnel",
                            "County governments exempt large corporations from paying income taxes",
                            "Small businesses are not affected by local community conditions"
                        ],
                        "correct": "B",
                        "explanation": "Small businesses lack the economies of scale, deep financial reserves, and specialized staff enjoyed by large corporations, making large unrecoverable cash donations a threat to daily survival."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 3 Synthesis & Key Takeaways",
                    "content": {
                        "text": "### Summary of Core Principles\n\n- **Real Economic Costs:** Social responsibility is not costless; it introduces genuine cost-price tradeoffs, capital demands, and managerial complexity.\n- **Social ROI Measurement:** Because benefits like brand trust and goodwill are intangible and long-term, businesses must track holistic performance metrics.\n- **Balancing Stakeholders:** Management must balance the immediate dividend expectations of owners with the welfare of workers and the community.\n- **Authenticity is Paramount:** Superficial CSR (greenwashing) is quickly exposed and inflicts catastrophic brand damage. Genuine social responsibility begins by eliminating core operational harm."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Designing a Social Responsibility Project in the School
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Designing a Social Responsibility Project in the School",
        "unit_description": "Structured 4-stage project design framework: needs assessment, SMART goal setting, operational roadmap planning, and community resource mobilization.",
        "lesson_title": "Designing a Social Responsibility Project in the School",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Secondary School Students Designing Community Projects",
                    "content": {
                        "title": "Kenyan Secondary School Students Collaborating",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/06/Students_at_Shimo_la_Tewa_Secondary_School.jpg",
                        "caption": "Secondary school students collaborating in school, representing teamwork in designing a structured school-based social responsibility activity.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Apply the 4-stage project design framework to school-based social initiatives\n- Conduct a confidential, stigma-free student needs assessment\n- Formulate SMART project objectives for school resource drives\n- Plan committee roles, operational logistics, and creative community fundraising activities"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "School Social Responsibility Project Design",
                    "content": {
                        "term": "Project Design Framework",
                        "definition": "The systematic, structured planning process through which student entrepreneurs identify real community needs, set measurable targets, assign operational responsibilities, and mobilize resources to execute a social intervention ethically."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Bridge Building Analogy",
                    "content": {
                        "text": "Imagine your community needs to cross a wide, fast-flowing river:\n\n- **Haphazard Action:** You randomly toss wooden planks into the raging water and try to run across. The timber floats away, and anyone attempting to cross falls into the river.\n- **Engineered Project Design:** You first measure the river's width, survey the soil on both banks, calculate how many concrete pillars and steel cables are required, draw detailed architectural blueprints, assign specialized construction roles, and gather materials systematically.\n\nDesigning a school social responsibility project is exactly like building a bridge. Without structured needs identification, SMART goals, clear committee roles, and strict budgeting, well-intentioned efforts collapse into waste and confusion."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Four-Stage School Project Design Roadmap",
                    "content": {
                        "title": "Four-Stage School CSR Project Design Framework",
                        "caption": "Vector diagram detailing Step 1: Identify Need (Survey), Step 2: Define SMART Objectives, Step 3: Plan Details (Committees), and Step 4: Mobilize Resources.",
                        "svg_content": SVG_SCHOOL_PROJECT_DESIGN_FRAMEWORK
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "The 4-Stage School Project Design Blueprint",
                    "content": {
                        "headers": ["Project Stage", "Core Activities", "Critical Safeguard / Tool", "Expected Output"],
                        "rows": [
                            ["Stage 1: Needs Identification", "Consult class teachers, guidance counselors, and student leaders to identify essential unmet student needs", "Absolute anonymity: No student names are made public to protect recipient dignity", "Prioritized inventory of required items (e.g., 40 math sets, 160 exercise books, sanitary wear)"],
                            ["Stage 2: SMART Goal Formulation", "Convert identified gaps into a Specific, Measurable, Achievable, Relevant, and Time-bound target", "SMART Criteria Filter: Avoid vague aspirations like 'let us help poor learners'", "Written project mission statement with clear quantitative metrics and Week 6 Term 3 deadline"],
                            ["Stage 3: Logistics & Committee Planning", "Establish student committees: (1) Finance & Accounting, (2) Sourcing & Procurement, (3) Distribution", "Separation of Duties: Cash collectors cannot independently spend funds without teacher sign-off", "Detailed operational roadmap with weekly milestones and assigned student responsibilities"],
                            ["Stage 4: Resource Mobilization", "Launch class donation boxes for surplus pens/books, organize Friday Class Bake Sale, seek bookshop discounts", "Official Receipting: Every cash donation is recorded with an official paper receipt", "Accumulated stock of donated items and cash fund ready for wholesale purchasing"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: School Project Resource Mobilization & Deficit Budgeting",
                    "content": {
                        "intro": "Grade 10 Business Studies class at Shimo la Tewa Secondary School designs a project to assemble $N = 40$ Back-to-School learning kits for needy learners. Each kit contains: 4 exercise books at $\\text{KES } 65$ each, 1 Oxford mathematical set at $\\text{KES } 180$, and 2 ballpoint pens at $\\text{KES } 25$ each. Through a class donation drive, students contribute 60 exercise books and 30 pens in-kind. The class organizes a Friday School Talent Show to raise the remaining cash deficit, charging an entry ticket of $T = \\text{KES } 100$ per student. Calculate: (a) Total Gross Project Cost ($C_{\\text{gross}}$), (b) The In-Kind Value of Donated Stock ($V_{\\text{donated}}$), (c) The Net Cash Deficit to be Raised ($D_{\\text{cash}}$), and (d) The Minimum Number of Talent Show Tickets ($S_{\\text{min}}$) the class must sell.",
                        "steps": [
                            "**Step 1: Given Information:** Number of kits $N = 40$. Unit requirements per kit: 4 books @ $\\text{KES } 65$, 1 set @ $\\text{KES } 180$, 2 pens @ $\\text{KES } 25$. In-kind donations: 60 books, 30 pens. Ticket price $T = \\text{KES } 100$.",
                            "**Step 2: Formula:** Kit Unit Cost: $$c_{\\text{kit}} = (4 \\times 65) + 180 + (2 \\times 25)$$. Total Gross Cost: $$C_{\\text{gross}} = N \\times c_{\\text{kit}}$$. In-Kind Value: $$V_{\\text{donated}} = (60 \\times 65) + (30 \\times 25)$$. Net Cash Deficit: $$D_{\\text{cash}} = C_{\\text{gross}} - V_{\\text{donated}}$$. Minimum Tickets: $$S_{\\text{min}} = \\lceil \\frac{D_{\\text{cash}}}{T} \\rceil$$.",
                            "**Step 3: Substitution:** Compute unit cost: $$c_{\\text{kit}} = 260 + 180 + 50 = \\text{KES } 490$$. Gross cost: $$C_{\\text{gross}} = 40 \\times 490 = \\text{KES } 19,600$$. Donated value: $$V_{\\text{donated}} = (60 \\times 65) + (30 \\times 25) = 3,900 + 750 = \\text{KES } 4,650$$. Cash deficit: $$D_{\\text{cash}} = \\text{KES } 19,600 - \\text{KES } 4,650$$.",
                            "**Step 4: Calculation:** $$D_{\\text{cash}} = \\text{KES } 14,950$$. Ticket count: $$S_{\\text{min}} = \\frac{14,950}{100} = 149.5 \\rightarrow 150\\text{ tickets}$$.",
                            "**Step 5: Final Answer:** (a) Gross Project Cost = $\\text{KES } 19,600$. (b) Donated Value = $\\text{KES } 4,650$. (c) Net Cash Deficit = $\\text{KES } 14,950$. (d) The class must sell a minimum of 150 talent show tickets at $\\text{KES } 100$ to fully fund the remaining supplies.",
                            "**Step 6: Economic Interpretation & Pitfall:** Blending in-kind item drives with cash fundraising reduces the total cash burden by $23.7\\%$ ($\\text{KES } 4,650$), making the project highly achievable for high school learners. *Common Pitfall:* Overestimating cash collections without confirming ticket sales targets in advance, resulting in procurement deficits on distribution day."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Designing a Class-Based Stationery Project",
                    "content": {
                        "title": "Student Enterprise and Peer Solidarity at Shimo la Tewa",
                        "text": "Grade 10 Business Studies students at Shimo la Tewa Secondary School observed that several classmates frequently fell behind in Mathematics and Geography due to lacking geometrical sets and graph exercise books. Instead of making individual ad-hoc contributions, the class formed a formal 'CSR Project Steering Committee.'\n\nThey conducted a confidential survey through their class patron, set a SMART objective to equip 40 students with complete kits within four weeks, and ran a 'Friday Snack Kiosk' selling mandazis baked by students. By applying formal business planning, the class fully funded their target without relying on external donations."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Project Design and Resource Mobilization in Schools",
                    "content": {
                        "title": "How to Plan, Budget, and Fund Community Social Projects",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Step-by-step tutorial on designing community projects, setting SMART milestones, building team committees, and mobilizing grassroots resources."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Formulating SMART Project Objectives",
                    "content": {
                        "question": "Which of the following statements represents a correctly formulated SMART objective for a school social responsibility project?",
                        "options": [
                            "To help all needy students in Kenya get stationery whenever money is available",
                            "To purchase and distribute 40 complete mathematical sets and 160 exercise books to 40 verified needy learners in Grade 10 by Friday of Week 6, Term 3",
                            "To make our school the cleanest and most famous secondary school in the county",
                            "To collect money from parents without keeping financial records"
                        ],
                        "correct": "B",
                        "explanation": "Option B is Specific (40 sets, 160 books), Measurable (exact item quantities and 40 learners), Achievable, Relevant to academic success, and Time-bound (Friday of Week 6, Term 3)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Protecting Student Dignity",
                    "content": {
                        "question": "When conducting a school needs assessment to identify classmates who lack school supplies, what is the most important ethical guideline to follow?",
                        "options": [
                            "Read out the names of needy students during the morning school assembly to encourage donations",
                            "Maintain strict confidentiality and consult class teachers privately to protect student privacy and prevent social stigma",
                            "Post the names and photos of needy students on public social media pages",
                            "Force needy students to wear special badges during school hours"
                        ],
                        "correct": "B",
                        "explanation": "Human dignity and empathy are core ethical principles of social responsibility. Identifying beneficiaries must remain strictly confidential to prevent embarrassment, discrimination, or social stigma."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 4 Synthesis & Key Takeaways",
                    "content": {
                        "text": "### Summary of Core Principles\n\n- **Structured Design:** Effective school social projects follow a 4-step framework: Identify Need ➔ Define SMART Goals ➔ Plan Logistics & Roles ➔ Mobilize Resources.\n- **Confidentiality & Dignity:** Identifying needy beneficiaries must always protect student identity and prevent social stigma.\n- **Committee Specialization:** Splitting tasks into Finance, Sourcing, and Distribution committees enforces separation of duties and operational efficiency.\n- **Creative Mobilization:** Blending in-kind item donation drives with school-approved fundraising events (bake sales, talent shows) ensures 100% project financing."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Implementing a School Social Responsibility Project
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Implementing a School Social Responsibility Project",
        "unit_description": "Execution of ethical procurement, sorting and assembly of student support kits, confidential and dignified distribution, and financial receipt accounting.",
        "lesson_title": "Implementing a School Social Responsibility Project",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Procurement Accounting and Supply Assembly",
                    "content": {
                        "title": "Systematic Financial Record Keeping and Office Organization",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/The_Accountants_desks_%283817577217%29.jpg",
                        "caption": "Systematic procurement record keeping, receipt verification, and stationery pack preparation during school CSR project implementation.",
                        "author": "Kristin Dos Santos",
                        "licensing": "CC BY-SA 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Execute bulk purchasing and negotiate wholesale discounts with suppliers\n- Implement strict financial record-keeping using official stamped receipts\n- Assemble and quality-verify standardized student learning packages\n- Execute confidential, stigma-free distribution through school counselors and teachers"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Project Implementation and Financial Accountability",
                    "content": {
                        "term": "Project Implementation",
                        "definition": "The operational execution phase where planned project activities are carried out through ethical wholesale procurement, quality-controlled kit assembly, confidential distribution, and transparent financial record keeping."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Checking the Compass at Sea Analogy",
                    "content": {
                        "text": "Imagine sailing a dhow from Mombasa to Malindi across choppy ocean waters:\n\n- **Blind Navigation:** You raise the sails at the harbor, lock the rudder, and fall asleep. Unseen crosswinds and currents pull your boat off course, driving you directly into sharp coral reefs.\n- **Disciplined Navigation:** The experienced captain consults the compass every half hour, checks nautical charts against coastal landmarks, trims the sails to changing winds, and logs every nautical mile traveled.\n\nIn social project implementation, **financial monitoring, official receipts, and quality checks** serve as your navigational compass. They guarantee that every shilling donated reaches the intended beneficiaries without diversion, waste, or accounting leakage."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Project Implementation, Receipt Auditing and Handover",
                    "content": {
                        "title": "Project Implementation & Ethical Accountability Lifecycle",
                        "caption": "Vector diagram detailing Phase 1: Wholesale Sourcing & Receipts, Phase 2: Assembly & Quality Sorting, and Phase 3: Dignified & Confidential Distribution.",
                        "svg_content": SVG_PROJECT_IMPLEMENTATION_LIFECYCLE
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Implementation Phase Execution Protocol",
                    "content": {
                        "headers": ["Execution Phase", "Operational Task", "Integrity & Quality Mandate", "Commercial Value"],
                        "rows": [
                            ["Phase 1: Sourcing & Buying", "Sourcing Committee accompanies teacher to wholesale bookstore to buy deficit books and sets", "Demand official stamped paper receipt containing date, unit prices, and store VAT PIN", "Negotiating wholesale pricing saves 15-20% compared to local neighborhood retail prices"],
                            ["Phase 2: Quality Inspection", "Inspect all donated and purchased items, verifying paper binding, ruler calibration, and pen ink", "Reject torn, substandard, or unusable items to ensure student kits offer genuine utility", "Guarantees that recipient students receive top-quality educational tools that boost confidence"],
                            ["Phase 3: Standard Packaging", "Assemble standardized 'Back-to-School Packs' placed inside discreet, identical bags", "Every pack contains identical contents: 4 exercise books, 1 math set, 2 pens, 1 ruler", "Eliminates perceived favoritism and ensures equal assistance across all recipient learners"],
                            ["Phase 4: Dignified Distribution", "Hand over assembled kits directly to class teachers and school guidance counselors", "Distribution occurs privately inside counseling offices; zero photos, zero assembly announcements", "Upholds Section 28 of the Kenyan Constitution guaranteeing personal dignity and self-worth"],
                            ["Phase 5: Financial Reconciliation", "Finance Committee totals receipts, counts unspent cash surplus, and prepares audit report", "Surplus cash is banked or handed to the teacher patron for next term's project phase", "Ensures 100% financial transparency and eliminates suspicion of theft or fraud"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Wholesale Procurement Optimization & Receipt Auditing",
                    "content": {
                        "intro": "The school project Sourcing Committee visits a wholesale educational distributor in Kisumu with an allocated cash budget of $B = \\text{KES } 15,000$. The retail catalog value of required stationery is $V_{\\text{retail}} = \\text{KES } 17,500$. The wholesaler offers a bulk institutional discount structure: $10\\%$ discount on purchases between $\\text{KES } 5,000$ and $\\text{KES } 10,000$, and $16\\%$ discount on purchases exceeding $\\text{KES } 10,000$. Calculate: (a) The applicable wholesale discount percentage and monetary savings ($D_{\\text{saving}}$), (b) The net invoice payable on the official receipt ($P_{\\text{invoice}}$), (c) The unspent cash surplus to be returned to the class treasurer ($S_{\\text{surplus}}$), and (d) The percentage savings achieved compared to the original budget ($S_{\\%}$).",
                        "steps": [
                            "**Step 1: Given Information:** Allocated cash budget $B = \\text{KES } 15,000$. Retail catalog price $V_{\\text{retail}} = \\text{KES } 17,500$. Applicable discount tier for $V_{\\text{retail}} > \\text{KES } 10,000$ is $d = 16\\% = 0.16$.",
                            "**Step 2: Formula:** Monetary Discount: $$D_{\\text{saving}} = V_{\\text{retail}} \\times d$$. Net Invoice Payable: $$P_{\\text{invoice}} = V_{\\text{retail}} - D_{\\text{saving}}$$. Cash Surplus Returned: $$S_{\\text{surplus}} = B - P_{\\text{invoice}}$$. Budget Savings Percentage: $$S_{\\%} = \\frac{S_{\\text{surplus}}}{B} \\times 100$$.",
                            "**Step 3: Substitution:** Compute discount: $$D_{\\text{saving}} = \\text{KES } 17,500 \\times 0.16$$. Compute invoice: $$P_{\\text{invoice}} = \\text{KES } 17,500 - D_{\\text{saving}}$$. Compute surplus: $$S_{\\text{surplus}} = \\text{KES } 15,000 - P_{\\text{invoice}}$$.",
                            "**Step 4: Calculation:** $$D_{\\text{saving}} = \\text{KES } 2,800$$. $$P_{\\text{invoice}} = \\text{KES } 17,500 - \\text{KES } 2,800 = \\text{KES } 14,700$$. $$S_{\\text{surplus}} = \\text{KES } 15,000 - \\text{KES } 14,700 = \\text{KES } 300$$. $$S_{\\%} = \\frac{300}{15,000} \\times 100 = 2.0\\%$$.",
                            "**Step 5: Final Answer:** (a) Discount savings = $\\text{KES } 2,800$ ($16\\%$). (b) Net invoice paid with official stamped receipt = $\\text{KES } 14,700$. (c) Cash surplus returned to treasurer = $\\text{KES } 300$. (d) The project executed $2.0\\%$ under its cash budget while securing items originally worth $\\text{KES } 17,500$.",
                            "**Step 6: Economic Interpretation & Pitfall:** Buying in bulk directly from wholesale distributors stretches donor funds, enabling the committee to secure $\\text{KES } 17,500$ worth of books within a $\\text{KES } 15,000$ budget with a $\\text{KES } 300$ surplus. *Common Pitfall:* Buying small quantities from neighborhood retail kiosks at full retail price, which depletes funds prematurely and reduces the number of students helped."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Project Rollout and Receipt Auditing at Eldoret High",
                    "content": {
                        "title": "Financial Transparency and Dignified Distribution in Action",
                        "text": "At an Eldoret secondary school, a Grade 10 Business Studies class completed a project to support 35 boarders who lacked personal hygiene supplies and revision materials. The Sourcing Committee obtained three competing quotations from wholesale stationers, selected the most cost-effective vendor, and insisted on receiving a VAT-compliant ETR receipt.\n\nThe assembled packages were handed over to the school's Guidance and Counseling department, who distributed them individually during evening guidance sessions. The class treasurer prepared a one-page financial summary displaying every receipt number, reconciling total cash raised (KES 18,200) with total purchases (KES 17,650) and banking the KES 550 surplus. The school principal commended the class for demonstrating corporate-level integrity."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Project Implementation and Procurement Auditing",
                    "content": {
                        "title": "Executing Community Initiatives with Financial Integrity",
                        "youtube_id": "v83s92y5Tq4",
                        "url": "https://www.youtube.com/watch?v=v83s92y5Tq4",
                        "description": "Practical guide on wholesale negotiation, managing cash receipts, inventory assembly, and maintaining ethical standards during project delivery."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Official Receipt Mandate",
                    "content": {
                        "question": "Why is it absolutely mandatory for the school CSR Sourcing Committee to obtain and file official stamped cash receipts for every stationery purchase?",
                        "options": [
                            "To show local shop owners how much money the students have collected",
                            "To prove to classmates, teachers, and donors that all funds were spent honestly, transparently, and strictly as authorized",
                            "To enable students to sell the stationery on the open market at a profit",
                            "Because the Central Bank of Kenya conducts daily spot-checks on school stationery boxes"
                        ],
                        "correct": "B",
                        "explanation": "Financial receipts provide an unalterable audit trail proving that donated funds were used exclusively for authorized project supplies, preventing suspicion of financial mismanagement or theft."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Distribution Protocol and Ethics",
                    "content": {
                        "question": "During the distribution of learning packs, why should items be handed over privately through guidance counselors rather than during a whole-school parade?",
                        "options": [
                            "Guidance counselors need to test the ballpoint pens before distribution",
                            "Private handover preserves the self-worth and dignity of needy students, preventing embarrassment and peer teasing",
                            "Whole-school parades are legally forbidden from taking place on weekdays",
                            "To ensure that wealthy students receive the packages first"
                        ],
                        "correct": "B",
                        "explanation": "Respecting human dignity is a core value of social responsibility. Private handover ensures needy learners receive educational support without public exposure or social stigma."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 5 Synthesis & Key Takeaways",
                    "content": {
                        "text": "### Summary of Core Principles\n\n- **Wholesale Efficiency:** Bulk purchasing from wholesalers maximizes the purchasing power of donated funds through institutional discounts.\n- **Receipt Auditing:** Transparent accounting requires filing official stamped cash receipts for every transaction, reconciling total cash received against total spent.\n- **Quality Standards:** Every assembled kit must contain identical, top-grade educational supplies to provide true learning support.\n- **Confidential Handover:** Distributing supplies privately through counselors upholds student dignity and eliminates social stigma."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Monitoring, Evaluating, and Reporting on Social Responsibility Projects
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Monitoring, Evaluating, and Reporting on Social Responsibility Projects",
        "unit_description": "Variance analysis, impact metrics, stakeholder accountability reporting, ethical evaluation, and addressing business externalities (Maji Mazuri case study).",
        "lesson_title": "Monitoring, Evaluating, and Reporting on Social Responsibility Projects",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Community Outreach, Health and Project Evaluation",
                    "content": {
                        "title": "Community Health and Welfare Outreach Program in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Waiting_for_Safari_Doctors_to_Arrive_%28Credit_Tojo_Andrianarivo%29.jpg",
                        "caption": "Community health and welfare outreach program in Kenya, illustrating project monitoring, impact evaluation, and stakeholder accountability.",
                        "author": "Tojo Andrianarivo",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Calculate and interpret Financial Budget Variances ($$\\text{Variance} = \\text{Budget} - \\text{Actual}$$$)\n- Measure qualitative and quantitative social impact indicators (Beneficiary Reach & SROI)\n- Compile a professional, transparent Social Responsibility Project Report\n- Evaluate complex real-world ethical dilemmas and negative externalities (Maji Mazuri Water Bottlers case)"
                    }
                }
            ],
            # Card 2: Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Monitoring, Evaluation, and Social Auditing",
                    "content": {
                        "term": "Monitoring and Evaluation (M&E)",
                        "definition": "The structured assessment process of tracking project implementation progress, measuring achieved social outputs against initial objectives, calculating financial variances, and documenting lessons learned to enhance future community impact."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Post-Match Analysis Analogy",
                    "content": {
                        "text": "Think of a professional Kenyan Premier League football team:\n\n- **Amateur Approach:** The final whistle blows, players walk home, and nobody discusses what happened. The same defensive blunders and missed passes are repeated in the next match.\n- **Professional Approach:** The coach and players gather in the video room on Monday morning. They review match footage, analyze pass completion rates, track distance covered, examine defensive errors, celebrate successful tactics, and formulate a refined game plan for the next tournament.\n\nIn social responsibility, **Project Review and Evaluation** is your post-match analysis. It reveals whether donor money was spent efficiently, highlights operational bottlenecks, celebrates community victories, and establishes institutional knowledge for future initiatives."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "CSR Project Evaluation, Variance Audit & Externalities Review",
                    "content": {
                        "title": "CSR Evaluation, Variance Audit & Externalities Review Matrix",
                        "caption": "Vector diagram illustrating financial variance auditing, impact reach metrics, Social Return on Investment (SROI), and ethical externality remediation.",
                        "svg_content": SVG_CSR_MONITORING_EVALUATION_MATRIX
                    }
                }
            ],
            # Card 4: Comparative Matrix & Structured Flow
            [
                {
                    "type": "comparison_table",
                    "title": "Evaluation Framework: Quantitative vs Qualitative Metrics",
                    "content": {
                        "headers": ["Evaluation Dimension", "Metric / Indicator Formula", "Target vs Actual Example", "Management Decision Implication"],
                        "rows": [
                            ["1. Financial Budget Variance", "$$V = \\text{Budget} - \\text{Actual}$$$", "Budget: KES 10,000 | Actual: KES 8,800 ➔ Variance: +KES 1,200 (Favourable)", "Favourable variance proves procurement efficiency; surplus funds carry forward to Term 1 drive"],
                            ["2. Beneficiary Reach Rate", "$$\\text{Reach \\%} = \\frac{\\text{Actual Learners}}{\\text{Targeted Learners}} \\times 100$$$", "Target: 25 Learners | Reached: 32 Learners ➔ Reach Rate: 128%", "Exceeded goal by 28%; confirms that bulk wholesale discounts enabled equipping 7 additional learners"],
                            ["3. Social Efficiency Ratio (SER)", "$$\\text{SER} = \\frac{\\text{Market Value of Goods}}{\\text{Actual Cash Spent}}$$$", "Market Value: KES 15,360 | Cash Spent: KES 8,800 ➔ SER: 1.75x Multiplier", "Every KES 1.00 of donor cash yielded KES 1.75 in educational value due to wholesale discounts and in-kind items"],
                            ["4. Academic & Attendance Impact", "$$\\Delta \\text{Homework} \\& \\Delta \\text{Absenteeism}$$$", "Zero homework penalties in Math; class attendance among beneficiaries rose from 82% to 98%", "Proves direct correlation between adequate basic learning tools and student academic performance"],
                            ["5. Externalities & Ethics Review", "Assessment of operational side-effects (e.g., waste, water depletion, greenwashing)", "Maji Mazuri: KES 100k soccer sponsor vs community borehole water depletion", "Sponsoring sports does not justify depleting drinking water; firm must install water-recycling plant"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations & Examples
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Comprehensive Project Variance and Social Efficiency Audit",
                    "content": {
                        "intro": "Grade 10 Business Studies class completes its Term 3 social responsibility project. The class treasurer presents the final project ledger: Planned project budget was $B = \\text{KES } 10,000$ to assist $N_{\\text{target}} = 25$ needy learners. Through aggressive wholesale price negotiation, total actual project expenditure was $A = \\text{KES } 8,800$, and the team successfully assembled and distributed learning packs to $N_{\\text{actual}} = 32$ learners. The open-market retail value of all distributed supplies is $V_{\\text{market}} = \\text{KES } 15,360$. Calculate: (a) Financial Budget Variance ($V_{\\text{budget}}$) and classify as Favourable or Adverse, (b) Beneficiary Reach Rate ($R_{\\text{reach}}$), (c) Social Efficiency Ratio ($\\text{SER}$), and (d) The Cost per Learner Assisted ($C_{\\text{unit}}$) compared to original budgeted cost per learner ($C_{\\text{budgeted}}$).",
                        "steps": [
                            "**Step 1: Given Information:** Budgeted spend $B = \\text{KES } 10,000$. Actual spend $A = \\text{KES } 8,800$. Target learners $N_{\\text{target}} = 25$. Actual learners $N_{\\text{actual}} = 32$. Market value delivered $V_{\\text{market}} = \\text{KES } 15,360$.",
                            "**Step 2: Formula:** Budget Variance: $$V_{\\text{budget}} = B - A$$. Beneficiary Reach Rate: $$R_{\\text{reach}} = \\frac{N_{\\text{actual}}}{N_{\\text{target}}} \\times 100$$. Social Efficiency Ratio: $$\\text{SER} = \\frac{V_{\\text{market}}}{A}$$. Actual Cost per Learner: $$C_{\\text{unit}} = \\frac{A}{N_{\\text{actual}}}$$. Budgeted Cost per Learner: $$C_{\\text{budgeted}} = \\frac{B}{N_{\\text{target}}}$$.",
                            "**Step 3: Substitution:** Compute variance: $$V_{\\text{budget}} = \\text{KES } 10,000 - \\text{KES } 8,800$$. Compute reach: $$R_{\\text{reach}} = \\frac{32}{25} \\times 100$$. Compute SER: $$\\text{SER} = \\frac{\\text{KES } 15,360}{\\text{KES } 8,800}$$. Compute unit costs: $$C_{\\text{unit}} = \\frac{\\text{KES } 8,800}{32}$$, $$C_{\\text{budgeted}} = \\frac{\\text{KES } 10,000}{25}$$.",
                            "**Step 4: Calculation:** $$V_{\\text{budget}} = +\\text{KES } 1,200\\text{ (Favourable)}$$. $$R_{\\text{reach}} = 128.0\\%$$. $$\\text{SER} = 1.745 \\approx 1.75\\text{x}$$. $$C_{\\text{unit}} = \\text{KES } 275.00\\text{ per learner}$$. $$C_{\\text{budgeted}} = \\text{KES } 400.00\\text{ per learner}$$.",
                            "**Step 5: Final Answer:** (a) Budget Variance = $+\\text{KES } 1,200$ (Favourable). (b) Beneficiary Reach Rate = $128.0\\%$ (7 extra learners helped). (c) Social Efficiency Ratio = $1.75\\text{x}$ (every KES 1.00 spent generated KES 1.75 in educational value). (d) Actual cost per learner dropped from $\\text{KES } 400.00$ to $\\text{KES } 275.00$ (a $31.25\\%$ cost efficiency improvement).",
                            "**Step 6: Economic Interpretation & Pitfall:** Excellent project execution combines financial frugality with maximum humanitarian reach. The committee spent less than budgeted while helping $28\\%$ more students. *Common Pitfall:* Measuring project success solely by the amount of money spent rather than the tangible number of people empowered and value delivered."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Maji Mazuri Water Bottlers and Externalities",
                    "content": {
                        "title": "The Tradeoff Between Public Relations and Environmental Harm",
                        "text": "Maji Mazuri Water Bottlers operates in a semi-arid Kenyan county. The factory pumps 20,000 litres of groundwater daily from a community borehole to wash bottles, causing local water tables to drop and forcing local women to queue for hours.\n\nTo build public goodwill, the company employs 50 local youths and sponsors an annual high-school football tournament with KES 100,000. County leaders praise the firm as 'socially responsible.' However, a rigorous social audit reveals this is superficial CSR: funding a football tournament does not erase or compensate for depleting the community's drinking water.\n\nTo achieve authentic social responsibility, Maji Mazuri must install an industrial water-recycling plant and drill deep dedicated geothermal boreholes that supply free piped drinking water to public community kiosks."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Monitoring, Evaluation and Business Externalities",
                    "content": {
                        "title": "Evaluating Social Impact, Measuring SROI, and Auditing Externalities",
                        "youtube_id": "3jwAGWky98c",
                        "url": "https://www.youtube.com/watch?v=3jwAGWky98c",
                        "description": "In-depth guide to monitoring and evaluation in business social responsibility, variance auditing, SROI calculations, and resolving negative externalities."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Financial Budget Variance Analysis",
                    "content": {
                        "question": "A school project committee budgets KES 12,000 to purchase revision textbooks. Through bulk wholesale discounts, they purchase all required books for KES 10,500. How is this financial result classified in project accounting?",
                        "options": [
                            "An Adverse Variance of KES 1,500 indicating financial mismanagement",
                            "A Favourable Variance of KES 1,500 indicating efficient procurement below budgeted cost",
                            "A Net Loss of KES 1,500 payable to the school administration",
                            "A greenwashing penalty assessed by the Ministry of Education"
                        ],
                        "correct": "B",
                        "explanation": "When actual expenditure is lower than the budgeted estimate ($$V = \\text{Budget} - \\text{Actual} > 0$$$), the variance is Favourable (F), indicating capital savings and cost efficiency."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Ethical Audit of Externalities",
                    "content": {
                        "question": "Why are county leaders mistaken when they label Maji Mazuri Water Bottlers 'highly responsible' solely because it sponsors a KES 100,000 high-school soccer tournament?",
                        "options": [
                            "Because secondary school students should not participate in sports competitions",
                            "Because superficial philanthropy does not compensate for the factory's severe negative externality of depleting the community's vital groundwater resources",
                            "Because the football tournament prize money should have been paid directly to the county governor",
                            "Because water bottling factories are exempt from corporate social responsibility"
                        ],
                        "correct": "B",
                        "explanation": "True corporate social responsibility requires an enterprise to eliminate and remediate its core negative externalities first before claiming credit for discretionary philanthropic donations."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 6 Synthesis & Key Takeaways",
                    "content": {
                        "text": "### Summary of Core Principles\n\n- **Variance & Efficiency:** Regular monitoring compares actual expenditure against budgets ($$\\text{Variance} = \\text{Budget} - \\text{Actual}$$) to maintain fiscal discipline.\n- **Holistic Impact Metrics:** Project success is measured through beneficiary reach, social efficiency ratios (SER), and improvements in student academic outcomes.\n- **Authentic Reporting:** Preparing a comprehensive project report documenting cash receipts, challenges, and lessons learned builds institutional memory and stakeholder trust.\n- **Eliminate Harm First:** True business social responsibility prioritizes neutralizing negative environmental and social externalities over cosmetic public relations gestures."
                    }
                }
            ]
        ]
    }
]
