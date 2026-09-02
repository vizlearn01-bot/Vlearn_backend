"""
VLearn CBC Grade 10 Business Studies — Topic 8: Entrepreneurship
Full Structured Lesson Card Definitions (Lessons 1 to 6)
"""

from curriculum.cbc_grade10_business_studies_topic8_svgs import (
    SVG_ENTREPRENEURIAL_ENGINE_AND_SKILLS,
    SVG_TYPES_OF_ENTREPRENEURS_TAXONOMY,
    SVG_IDEA_VS_OPPORTUNITY_TRANSFORMATION,
    SVG_OPPORTUNITY_SCREENING_MATRIX_FRAMEWORK,
    SVG_BUSINESS_INCUBATION_ECOSYSTEM,
    SVG_SCHOOL_ENTERPRISE_COSTING_AND_PRICING
)

TOPIC_8_LESSONS = [
    # =========================================================================
    # LESSON 1: Entrepreneurial Skills for Economic Growth
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Entrepreneurial Skills for Economic Growth",
        "unit_description": "Core competencies of successful entrepreneurs, innovation mechanisms, calculated risk management, resource mobilization, and macroeconomic contributions to national development.",
        "lesson_title": "Entrepreneurial Skills for Economic Growth",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Micro-Enterprise Street Vendor in Kenya",
                    "content": {
                        "title": "Dynamic Entrepreneurship in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Banana_Street_Vendor_Kenya.jpg",
                        "caption": "An enterprising Kenyan street trader demonstrating resourcefulness, agility, and market opportunity recognition in everyday commerce.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define entrepreneurship, entrepreneur, innovation, and risk management\n- Analyze the key skills required for entrepreneurial success\n- Explain the distinction between calculated risk-taking and reckless gambling\n- Evaluate how entrepreneurship drives employment, GDP growth, and county development"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concept Explanation
            [
                {
                    "type": "definition_card",
                    "title": "Entrepreneurship and Enterprise Creation",
                    "content": {
                        "term": "Entrepreneurship",
                        "definition": "The ability, mindset, and process of identifying market opportunities, mobilizing and organizing factors of production (land, labor, and capital), innovating solutions, and undertaking calculated commercial risks to create a sustainable and profitable enterprise."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Pathfinder in the Dense Forest Analogy",
                    "content": {
                        "text": "Imagine a group of travelers lost in a dense, dark forest with no cleared road:\n\n- **Passive Observers:** Most people sit still, paralyzed by fear of wild animals, waiting for external rescue.\n- **The Pathfinder (The Entrepreneur):** Steps forward, reads the stars, crafts a compass from a leaf and magnetized needle, uses a panga to hack through thorny thickets, and paves a clear trail to safety.\n\nIn economics, the uncertain forest is the unpredictable market. The entrepreneur is the pathfinder—applying creativity, calculated risk-taking, and resourcefulness to forge commercial pathways where none existed, generating safety, employment, and wealth for society."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Engine of Entrepreneurship & Core Skills",
                    "content": {
                        "title": "The Entrepreneurial Engine Architecture",
                        "caption": "High-precision vector diagram illustrating the four pillars of entrepreneurship: Opportunity Recognition, Innovation & Design, Calculated Risk-Taking, and Resource Mobilization.",
                        "svg_content": SVG_ENTREPRENEURIAL_ENGINE_AND_SKILLS
                    }
                }
            ],
            # Card 4: Comparative Matrix of Core Entrepreneurial Skills
            [
                {
                    "type": "comparison_table",
                    "title": "Core Entrepreneurial Skills Matrix",
                    "content": {
                        "headers": ["Entrepreneurial Skill", "Operational Definition", "Business Manifestation", "Kenyan Real Example"],
                        "rows": [
                            ["Opportunity Recognition", "Detecting unmet needs and commercial market gaps", "Launching a service before competitors notice demand", "Setting up an estate shoe-cleaning kiosk outside muddy school gates"],
                            ["Creativity & Innovation", "Designing unique products or more efficient processes", "Disrupting existing high-cost supply chains", "Roy Allela inventing Sign-IO smart gloves for non-verbal communication"],
                            ["Calculated Risk-Taking", "Committing capital based on market research and contingency plans", "Hedging against potential downside losses", "Gradually expanding kiosk inventory based on proven sales data"],
                            ["Resourcefulness (Bootstrapping)", "Maximizing output using minimal available capital and networks", "Sharing space or recycling equipment to slash overheads", "Joseph partnering with a cyber-cafe owner to share desk space for PC repairs"],
                            ["Financial Literacy", "Tracking cash flows, pricing accurately, and managing expenses", "Maintaining positive working capital and liquidity", "Baraka Juice Bar computing unit costs and profit markup margins"],
                            ["Perseverance & Resilience", "Overcoming operational hurdles and recovering from failures", "Iterating business models following unexpected setbacks", "Mary replanting pest-resistant tomato crops after a harvest loss"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Economic Value Added (EVA) and Local Wealth Generation",
                    "content": {
                        "intro": "Wanja operates a local agro-processing micro-enterprise in Murang'a. In a single month, she purchases raw macadamia nuts from local smallholder farmers for $\\text{KES } 120,000$. She spends $\\text{KES } 25,000$ on roasting electricity, packaging foil, and transport. She employs two youths, paying total monthly wages of $\\text{KES } 30,000$, and sells the processed vacuum-packed nuts to Nairobi retail stores for $\\text{KES } 240,000$. The county government levies a $3\\%$ commercial turnover cess on gross sales.",
                        "steps": [
                            "**Step 1: Given Information:** Gross Sales Revenue ($TR$) = $\\text{KES } 240,000$. Raw Material Cost (Macadamia) = $\\text{KES } 120,000$. Operating Consumables (Energy, packaging, transport) = $\\text{KES } 25,000$. Direct Labor Wages = $\\text{KES } 30,000$. County Cess Rate = $3\\%$ on gross sales.",
                            "**Step 2: Formula & Economic Principle:** Gross Value Added ($GVA$) represents the wealth created by the enterprise over intermediate inputs: $$GVA = TR - \\text{Intermediate Material Costs}$$. Net Entrepreneurial Operating Profit ($\\Pi$) is: $$\\Pi = GVA - \\text{Wages} - \\text{County Tax}$$.",
                            "**Step 3: Substitution:** Calculate intermediate consumption: $$\\text{Intermediate Inputs} = \\text{KES } 120,000 + \\text{KES } 25,000 = \\text{KES } 145,000$$. Calculate Gross Value Added: $$GVA = \\text{KES } 240,000 - \\text{KES } 145,000$$. Calculate County Tax: $$\\text{Tax} = 0.03 \\times \\text{KES } 240,000$$.",
                            "**Step 4: Step-by-Step Calculation:** $$GVA = \\text{KES } 95,000$$. $$\\text{County Tax} = \\text{KES } 7,200$$. Calculate Net Operating Profit: $$\\Pi = \\text{KES } 95,000 - \\text{KES } 30,000 - \\text{KES } 7,200 = \\text{KES } 57,800$$.",
                            "**Step 5: Final Calculated Answer with Units:** Gross Value Added to the county economy is $\\text{KES } 95,000$. The enterprise distributed $\\text{KES } 30,000$ in youth wages, paid $\\text{KES } 7,200$ in local taxes, and yielded a net entrepreneurial surplus of $\\text{KES } 57,800$.",
                            "**Step 6: Economic Interpretation & Pitfall:** Entrepreneurship transforms low-value raw agricultural harvest into high-value packaged output, creating local jobs and public revenue. *Common Pitfall:* Confusing gross sales revenue with economic profit by neglecting intermediate costs and local regulatory fees."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Roy Allela's Sign-IO Smart Gloves",
                    "content": {
                        "title": "Solving Societal Communication Barriers through Technological Innovation",
                        "text": "When Kenyan micro-engineer Roy Allela observed that his young deaf niece struggled to communicate with family members fluent only in spoken languages, he recognized a critical problem. Allela integrated flex sensors into glove fingers to measure finger curl and map Kenyan Sign Language gestures. Connected via Bluetooth to a custom smartphone application, the gloves translate physical hand movements into clear spoken English and Swahili in real time.\n\nAllela transitioned from an inventor into an entrepreneur by patenting the design, securing seed prototyping grants, and organizing manufacturing partnerships. His enterprise demonstrates that the highest form of entrepreneurship pairs deep human empathy with technical innovation and calculated commercial risk-taking."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Entrepreneurship and Economic Transformation in Kenya",
                    "content": {
                        "title": "The Role of Innovation and Risk-Taking in Business Growth",
                        "youtube_id": "Bv_4kS5C5Z8",
                        "url": "https://www.youtube.com/watch?v=Bv_4kS5C5Z8",
                        "description": "Educational breakdown of core entrepreneurial competencies, resource mobilization, and how start-ups fuel national economic development."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Distinguishing Entrepreneurial Competencies",
                    "content": {
                        "question": "Wanja notices that primary school pupils in her estate arrive with mud-caked shoes every rainy morning. Within 48 hours, she leases a 2-meter space outside the school gate, buys cleaning brushes and shoe polish, and offers a KES 20 quick-shine service that serves 50 pupils daily. Which core entrepreneurial skill is Wanja primarily demonstrating?",
                        "options": [
                            "Passive Speculation",
                            "Opportunity Recognition",
                            "Corporate Intrapreneurship",
                            "Perpetual Succession"
                        ],
                        "correct": "B",
                        "explanation": "Opportunity recognition is the capacity to observe unmet everyday community pain points, recognize an underlying commercial market gap, and quickly organize resources into a profitable service."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Calculated Risk vs. Blind Gambling",
                    "content": {
                        "question": "Which of the following actions best illustrates 'calculated risk-taking' rather than reckless business gambling?",
                        "options": [
                            "Borrowing KES 500,000 at 24% interest to import winter coats into Mombasa without checking local weather preferences",
                            "Conducting a foot-traffic survey and pilot-testing 20 food bowls in a busy bus terminal before signing a full annual shop lease",
                            "Investing a family's entire life savings into a new cryptocurrency based solely on a social media tip",
                            "Opening a cyber-cafe with 15 desktop computers in an area where 95% of residents browse on smartphones"
                        ],
                        "correct": "B",
                        "explanation": "Calculated risk-taking involves gathering preliminary market data, testing customer demand with small pilot batches, and putting risk-mitigation measures in place before committing major financial capital."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "- **Core Definition:** Entrepreneurship is the dynamic process of identifying market opportunities, organizing resources (land, labor, capital), and undertaking calculated risks to build a viable enterprise.\n- **Essential Competencies:** Successful founders cultivate opportunity recognition, creative problem-solving, calculated risk management, financial literacy, resourcefulness (bootstrapping), and emotional grit.\n- **Calculated Risk vs. Gambling:** True entrepreneurs never gamble blindly; they test hypotheses, analyze customer feedback, and maintain contingency safety buffers.\n- **Macroeconomic Driver:** Enterprises create employment, expand the Gross Domestic Product (GDP), broaden county tax revenue, and convert idle local raw resources into commercial value."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Types of Entrepreneurs in Business
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Types of Entrepreneurs in Business",
        "unit_description": "Taxonomy of entrepreneurs based on motivation (opportunity vs. necessity), innovation style (innovative vs. imitative), societal mission (social entrepreneurs), and operational domain (technopreneurs, intrapreneurs, lifestyle founders).",
        "lesson_title": "Types of Entrepreneurs in Business",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Kenyan Agricultural Produce Market",
                    "content": {
                        "title": "Commercial Variety in Kenyan Markets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "Traders at Wangige Market exhibiting different entrepreneurial motivations, ranging from necessity-driven food kiosks to scalable wholesale distribution.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Classify entrepreneurs by motivation: Opportunity vs. Necessity entrepreneurs\n- Distinguish between Innovative Pioneers and Imitative (Adaptive) Entrepreneurs\n- Explain the 'Double Bottom Line' of Social Entrepreneurs in Kenyan communities\n- Identify Technopreneurs, Intrapreneurs, and Lifestyle Entrepreneurs in modern commerce"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Entrepreneurial Classifications",
                    "content": {
                        "term": "Social Entrepreneurship",
                        "definition": "A business model where commercial market principles and entrepreneurial strategies are deployed primarily to solve social, cultural, or environmental challenges while maintaining financial self-sufficiency."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Diverse Forest Ecosystem Analogy",
                    "content": {
                        "text": "A thriving forest ecosystem contains diverse plant species fulfilling specialized ecological roles:\n\n- **Canopy Trees (Innovative Pioneers):** Reach upward to break new ground and capture sunlight, creating fresh shelter below.\n- **Hardy Floor Shrubs (Imitative / Adaptive Traders):** Thrive in existing micro-climates, rapidly reproducing proven survival models.\n- **Nurturing Vines (Social Entrepreneurs):** Bind the soil together, enrich biodiversity, and ensure surrounding trees flourish.\n\nLikewise, the economy requires all entrepreneurial types: necessity traders provide immediate household resilience, imitative businesses stabilize retail distribution, technopreneurs drive global competitiveness, and social entrepreneurs heal environmental and social wounds."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Comprehensive Taxonomy of Entrepreneurs",
                    "content": {
                        "title": "Entrepreneurial Classification Matrix",
                        "caption": "Six-domain taxonomy categorizing entrepreneurs by motivation driver, innovation approach, social mission, digital technology usage, and corporate positioning.",
                        "svg_content": SVG_TYPES_OF_ENTREPRENEURS_TAXONOMY
                    }
                }
            ],
            # Card 4: Comparative Matrix of Entrepreneur Archetypes
            [
                {
                    "type": "comparison_table",
                    "title": "Entrepreneurial Types & Characteristics Matrix",
                    "content": {
                        "headers": ["Entrepreneur Type", "Primary Motivation", "Approach to Innovation", "Risk Profile", "Kenyan Benchmark Example"],
                        "rows": [
                            ["Opportunity Entrepreneur", "Spotted high-margin market gap; wealth creation", "Introduces improved or scaled business model", "Moderate, calculated capital risk", "Starting a commercial macadamia processing factory"],
                            ["Necessity Entrepreneur", "Lack of alternative employment; daily survival", "Replicates simple, familiar local activities", "High personal vulnerability; minimal capital", "Baking and selling mandazi along roadside stalls"],
                            ["Social Entrepreneur", "Solving social/environmental pain; community uplift", "Designs affordable community-centric solutions", "Balanced financial and social risk", "Baringo Gold Honey purchasing directly from beekeepers"],
                            ["Innovative Entrepreneur", "Creating disruptive breakthrough products", "High R&D; invents novel patented technologies", "High technological and market risk", "Sign-IO smart gloves translating sign language"],
                            ["Imitative Entrepreneur", "Entering proven markets with lower startup risk", "Refines customer service, packaging, or location", "Low to moderate commercial risk", "Opening a salon offering free home beauty visits"],
                            ["Technopreneur", "Scaling digital, software, or fintech solutions", "Leverages mobile apps, cloud computing, and AI", "Scalable tech risk; low marginal cost", "Agritech mobile app for instant crop disease diagnosis"],
                            ["Intrapreneur", "Driving corporate innovation from within", "Builds new internal divisions using firm capital", "Zero personal equity loss", "Safaricom engineers developing M-Pesa services"],
                            ["Lifestyle Entrepreneur", "Aligning work with personal passions and freedom", "Custom, boutique, or artistic services", "Low growth ambition; high personal joy", "Freelance wildlife and safari tour photographer"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Social Return on Investment (SROI) vs. Commercial Margins",
                    "content": {
                        "intro": "John operates *Baringo Gold Honey*, a social enterprise. Traditional traveling middlemen pay local beekeepers $\\text{KES } 200\\text{ per kg}$. John pays a guaranteed fair-trade price of $\\text{KES } 350\\text{ per kg}$ (a $\\text{KES } 150\\text{ premium}$ per kg) to 80 beekeeping families to stop deforestation. In one harvesting cycle, John buys $4,000\\text{ kg}$ of raw honey, incurs processing, testing, and bottling costs of $\\text{KES } 80\\text{ per kg}$, and sells the packaged jars to Nairobi supermarkets at $\\text{KES } 600\\text{ per kg}$.",
                        "steps": [
                            "**Step 1: Given Information:** Volume ($Q$) = $4,000\\text{ kg}$. Farmer Purchase Price ($P_{\\text{farm}}$) = $\\text{KES } 350/\\text{kg}$. Middleman Baseline Price ($P_{\\text{base}}$) = $\\text{KES } 200/\\text{kg}$. Processing Cost ($C_{\\text{proc}}$) = $\\text{KES } 80/\\text{kg}$. Retail Selling Price ($P_{\\text{sell}}$) = $\\text{KES } 600/\\text{kg}$.",
                            "**Step 2: Formula & Principles:** \n- Direct Social Value Injected to Farmers ($SV$) = $Q \\times (P_{\\text{farm}} - P_{\\text{base}})$\n- Total Commercial Enterprise Revenue ($TR$) = $Q \\times P_{\\text{sell}}$\n- Total Commercial Costs ($TC$) = $Q \\times (P_{\\text{farm}} + C_{\\text{proc}})$\n- Commercial Net Profit ($\\Pi$) = $TR - TC$",
                            "**Step 3: Substitution:** \n- Social Value = $4,000 \\times (\\text{KES } 350 - \\text{KES } 200)$\n- Total Revenue = $4,000 \\times \\text{KES } 600$\n- Total Costs = $4,000 \\times (\\text{KES } 350 + \\text{KES } 80) = 4,000 \\times \\text{KES } 430$",
                            "**Step 4: Step-by-Step Calculation:** \n- $SV = 4,000 \\times \\text{KES } 150 = \\text{KES } 600,000$\n- $TR = \\text{KES } 2,400,000$\n- $TC = \\text{KES } 1,720,000$\n- $\\Pi = \\text{KES } 2,400,000 - \\text{KES } 1,720,000 = \\text{KES } 680,000$",
                            "**Step 5: Final Calculated Answer with Units:** *Baringo Gold Honey* injected $\\text{KES } 600,000$ in premium social income directly into rural beekeeper households while generating $\\text{KES } 680,000$ in sustainable commercial net profit.",
                            "**Step 6: Economic Interpretation & Pitfall:** Social enterprises prove that commercial profitability and community impact can reinforce each other (the 'Double Bottom Line'). *Common Pitfall:* Assuming social enterprises are non-profit charities dependent on donations; viable social enterprises generate self-sustaining commercial trading margins."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Baringo Gold Honey & The Double Bottom Line",
                    "content": {
                        "title": "Transforming Forest Conservation into Commercial Agribusiness",
                        "text": "In Baringo County, recurring droughts previously forced rural families to fell indigenous acacia trees for charcoal burning. John, a native agribusiness graduate, founded *Baringo Gold Honey*. By offering modern modern beehives on credit and guaranteeing to buy honey at 75% above traveling broker rates, he made live acacia trees far more economically valuable to farmers than charcoal timber.\n\nJohn processes, tests for moisture compliance with KEBS standards, and bottles the honey under an attractive brand. The enterprise generates substantial annual profits while preserving over 5,000 hectares of indigenous woodland."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Classifications of Entrepreneurs and Social Enterprise",
                    "content": {
                        "title": "Understanding Entrepreneurial Types and the Double Bottom Line",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Exploration of opportunity vs necessity motivations, technopreneurship, intrapreneurship, and sustainable social business models in emerging markets."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Categorizing Business Motivations",
                    "content": {
                        "question": "Mercy loses her clerical job following a corporate restructuring. With rent due in five days and zero savings, she immediately starts frying and selling mandazi outside an Eldoret factory gate. How is Mercy classified?",
                        "options": [
                            "Corporate Intrapreneur",
                            "Necessity Entrepreneur",
                            "Technopreneur",
                            "Lifestyle Entrepreneur"
                        ],
                        "correct": "B",
                        "explanation": "A necessity entrepreneur starts a small venture out of urgent financial survival needs due to a lack of other employment options, rather than proactively pursuing an expansionary market opportunity."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Intrapreneurship in Corporate Structures",
                    "content": {
                        "question": "A senior software engineer employed at a commercial bank in Nairobi designs an internal digital micro-lending module. The bank funds the software rollout, bears all financial risks, and retains the patents. The engineer is acting as a(n):",
                        "options": [
                            "Imitative Entrepreneur",
                            "Intrapreneur",
                            "Necessity Entrepreneur",
                            "Social Activist"
                        ],
                        "correct": "B",
                        "explanation": "An intrapreneur behaves like an entrepreneur within an established corporation, developing innovative products using the company's financial capital and infrastructure without personally risking bankruptcy."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "- **Motivation Archetypes:** Opportunity entrepreneurs proactively pursue high-growth market openings; necessity entrepreneurs launch small trades for immediate survival.\n- **Innovation Spectrum:** Innovative pioneers invent novel products or tech (high R&D risk); imitative entrepreneurs adopt proven models with lower risk and incremental service upgrades.\n- **Social Entrepreneurship & Double Bottom Line:** Generates self-sustaining commercial profits while directly solving societal, educational, or environmental problems.\n- **Modern Categories:** Technopreneurs build scalable digital solutions; intrapreneurs innovate internally within large corporations; lifestyle entrepreneurs prioritize personal passion and work-life balance."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Evaluating Business Ideas and Opportunities for Start-Ups
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Evaluating Business Ideas and Opportunities for Start-Ups",
        "unit_description": "Distinguishing between raw business ideas and viable commercial opportunities, problem-solution fit, addressable market sizing, competitor moats, and start-up screening filters.",
        "lesson_title": "Evaluating Business Ideas and Opportunities for Start-Ups",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Bustling Urban Retail Market in Kenya",
                    "content": {
                        "title": "Market Demand in Urban Commercial Centers",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "City Market in Nairobi, demonstrating active consumer footfall, real-time purchasing power, and proven demand dynamics necessary for start-up viability.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish clearly between a raw business idea and a validated commercial opportunity\n- Explain the five critical opportunity evaluation filters\n- Assess problem-solution fit and customer willingness to pay\n- Apply market feasibility sizing to prevent premature start-up capital loss"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Business Idea vs. Commercial Opportunity",
                    "content": {
                        "term": "Commercial Opportunity",
                        "definition": "An attractive, feasible, durable, and commercially viable market opening where validated customer demand, problem-solution fit, and accessible resources allow an entrepreneur to deliver value and sustain profit."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Seed and the Fertile Soil Analogy",
                    "content": {
                        "text": "Consider planting an agricultural crop:\n\n- **The Seed (Business Idea):** A shiny, well-packaged seed exists as pure biological potential. If you scatter this seed onto dry, solid rock on a sun-scorched cliff, it shrivels and dies within days.\n- **The Fertile Soil (Commercial Opportunity):** Deep, nutrient-rich soil with moisture, sunlight, and compost. Even an ordinary seed planted in rich soil germinates, grows strong roots, and yields a bountiful harvest.\n\nIn business, a brilliant idea planted in a market with zero customer demand, poor pricing power, or inaccessible resources will fail. Seasoned entrepreneurs spend time testing the 'soil' before buying the 'seeds'."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Idea to Opportunity Transformation Pipeline",
                    "content": {
                        "title": "The Five Screening Filter Gates",
                        "caption": "Systematic pipeline filtering raw untested business ideas through Market Demand, Problem-Solution Fit, Resource Feasibility, Competitive Advantage, and Unit Profitability.",
                        "svg_content": SVG_IDEA_VS_OPPORTUNITY_TRANSFORMATION
                    }
                }
            ],
            # Card 4: Comparative Matrix: Business Idea vs. Opportunity
            [
                {
                    "type": "comparison_table",
                    "title": "Business Idea vs. Commercial Opportunity Matrix",
                    "content": {
                        "headers": ["Analytical Parameter", "Raw Business Idea", "Validated Commercial Opportunity", "Start-up Practical Implication"],
                        "rows": [
                            ["Origin & Focus", "Creator's imagination, passions, or unverified assumptions", "Observed customer pain point and active market gap", "Ideas start internally; opportunities are verified externally"],
                            ["Demand Validation", "Theoretical; assumes 'everyone will buy'", "Measured; verified through pre-orders, surveys, or pilot tests", "Validating demand prevents investing capital in unwanted goods"],
                            ["Financial Viability", "Costs unknown; pricing based on guesswork", "Clear unit economics, break-even targets, and margins", "Ensures selling price comfortably exceeds total cost per unit"],
                            ["Resource Fit", "May demand millions in unavailable machinery/skills", "Can be realistically launched with accessible capital and tech", "Prevents start-up stall caused by resource shortfalls"],
                            ["Competitive Moat", "Ignores established substitutes in the market", "Clear unique value proposition (cheaper, faster, better)", "Explains why customers will abandon current suppliers"],
                            ["Failure Rate", "Extremely high (>85% within 12 months)", "Low to moderate due to pre-launch market validation", "Rigorous screening protects founder equity and savings"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Addressable Market Sizing and Daily Feasibility Analysis",
                    "content": {
                        "intro": "Otieno is evaluating an opportunity to install a reverse-osmosis clean water refill station in a new gated estate in Kitengela. The estate has $600\\text{ households}$, none of which have piped municipal drinking water. A household survey reveals that each family consumes an average of two $20\\text{-liter}$ water dispensers weekly ($104\\text{ bottles/year}$) and currently buys them from traveling bowsers at $\\text{KES } 250\\text{ per bottle}$. Otieno plans to price his purified refill at $\\text{KES } 150\\text{ per bottle}$, with a direct purification and power cost of $\\text{KES } 40\\text{ per bottle}$. He conservatively estimates capturing a $30\\%$ market share ($SAM$) in Year 1. Monthly kiosk rent and operator salary total $\\text{KES } 22,000$.",
                        "steps": [
                            "**Step 1: Given Information:** Total Households ($N$) = $600$. Annual Consumption per Household ($C$) = $104\\text{ bottles}$. Total Addressable Market in Units ($TAM$) = $600 \\times 104 = 62,400\\text{ bottles/year}$. Target Market Share = $30\\%$. Serviceable Available Market ($SAM$) = $0.30 \\times 62,400 = 18,720\\text{ bottles/year}$. Selling Price ($P$) = $\\text{KES } 150$. Variable Cost per Bottle ($VC_{\\text{unit}}$) = $\\text{KES } 40$. Monthly Fixed Overhead ($FC_{\\text{month}}$) = $\\text{KES } 22,000$.",
                            "**Step 2: Formula & Principles:** \n- Annual Target Units ($Q_{\\text{annual}}$) = $18,720\\text{ bottles}$\n- Monthly Unit Target ($Q_{\\text{month}}$) = $Q_{\\text{annual}} \\div 12$\n- Monthly Contribution Margin ($CM_{\\text{unit}}$) = $P - VC_{\\text{unit}}$\n- Monthly Gross Contribution ($GC$) = $Q_{\\text{month}} \\times CM_{\\text{unit}}$\n- Monthly Net Operating Profit ($\\Pi_{\\text{month}}$) = $GC - FC_{\\text{month}}$",
                            "**Step 3: Substitution:** \n- $Q_{\\text{month}} = 18,720 \\div 12 = 1,560\\text{ bottles/month}$ ($52\\text{ bottles/day}$)\n- $CM_{\\text{unit}} = \\text{KES } 150 - \\text{KES } 40 = \\text{KES } 110\\text{ per bottle}$\n- $GC = 1,560 \\times \\text{KES } 110$\n- $\\Pi_{\\text{month}} = GC - \\text{KES } 22,000$",
                            "**Step 4: Step-by-Step Calculation:** \n- $GC = \\text{KES } 171,600\\text{ per month}$\n- $\\Pi_{\\text{month}} = \\text{KES } 171,600 - \\text{KES } 22,000 = \\text{KES } 149,600\\text{ per month}$",
                            "**Step 5: Final Calculated Answer with Units:** At a $30\\%$ market penetration ($52\\text{ bottles per day}$), Otieno's water refill station is a viable commercial opportunity, generating $\\text{KES } 171,600$ in monthly gross contribution and $\\text{KES } 149,600$ in net monthly operating surplus.",
                            "**Step 6: Economic Interpretation & Pitfall:** Quantifying market demand ($TAM \\rightarrow SAM$) transforms speculative ideas into bankable commercial opportunities with measurable unit economics. *Common Pitfall:* Assuming $100\\%$ market capture on Day 1 without accounting for competitor response or ramp-up periods."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: The Kakamega Cyber-Cafe Shift",
                    "content": {
                        "title": "Failing on an Idea vs. Thriving on Validated Market Opportunity",
                        "text": "In 2021, Otieno saved KES 150,000 and opened a traditional cyber-cafe with 10 desktop computers in Kakamega town, assuming that 'everyone needs internet.' However, local residents and university students already owned low-cost 4G smartphones and accessed mobile bundles from Safaricom and Airtel. With daily customer traffic below 4 people, the cafe shuttered after three months due to unpaid rent.\n\nReflecting on the loss, Otieno researched genuine local pain points. He discovered that while smartphones were ubiquitous, power blackouts frequently disrupted battery charging, and students required quick color-printing for research proposals. He pivoted: selling off the desktop terminals, installing a high-capacity solar inverter charging dock, and acquiring a fast laser multifunction printer. His revamped 'Student Power & Print Kiosk' reached profitability in 45 days."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Evaluating Business Ideas and Spotting Market Opportunities",
                    "content": {
                        "title": "How to Screen and Validate Start-Up Concepts",
                        "youtube_id": "V06fK2k6qGk",
                        "url": "https://www.youtube.com/watch?v=V06fK2k6qGk",
                        "description": "Techniques for assessing problem-solution fit, validating target customer demand, calculating market size, and evaluating start-up feasibility."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying a Genuine Opportunity",
                    "content": {
                        "question": "Which of the following scenarios describes a genuine, validated commercial opportunity rather than merely an untested business idea?",
                        "options": [
                            "Planning an upscale indoor ice-skating rink in a rural village that experiences frequent power outages",
                            "Designing a mobile application that translates Shakespearean poetry into classical Latin",
                            "Establishing a clean water refilling kiosk in a newly populated estate of 300 families lacking municipal piping",
                            "Opening a desktop computer cyber-cafe charging KES 2 per minute where 98% of people own 4G smartphones"
                        ],
                        "correct": "C",
                        "explanation": "Scenario C represents a genuine commercial opportunity because there is a verified, essential human need (clean drinking water), an unserved population (300 families without piped water), and affordable, feasible local technology."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Problem-Solution Fit Analysis",
                    "content": {
                        "question": "Why is achieving 'Problem-Solution Fit' critical before committing significant capital to a start-up?",
                        "options": [
                            "It automatically exempts the business from paying county business license fees",
                            "It confirms that customers experience a genuine pain point and are actively willing to pay for the proposed solution",
                            "It legally converts a sole proprietorship into a public limited liability corporation",
                            "It guarantees that no rival enterprise can ever enter the same market sector"
                        ],
                        "correct": "B",
                        "explanation": "Problem-Solution Fit validates that the entrepreneur's product directly alleviates a severe customer frustration at a price point customers are ready to pay, preventing costly investments in unwanted products."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "- **Idea vs. Opportunity:** An idea is an unproven mental concept; an opportunity is a validated commercial opening supported by paying customer demand and achievable economics.\n- **The 5 Screening Filters:** Start-ups must evaluate Market Demand Scale, Problem-Solution Fit, Resource & Skill Feasibility, Competitive Advantage, and Unit Profitability.\n- **Addressable Market Sizing:** Calculating TAM (Total Addressable Market) and realistic SAM (Serviceable Market) grounds financial forecasts in measurable reality.\n- **Early Validation:** Conducting customer surveys and running small pilot tests saves capital and prevents premature enterprise failure."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Evaluating an Opportunity Using a Simple Screening Matrix
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Evaluating an Opportunity Using a Simple Screening Matrix",
        "unit_description": "Objective quantitative scoring models, multi-criteria decision frameworks, scoring scales, ranking methodologies, and capital allocation across competing start-up options.",
        "lesson_title": "Evaluating an Opportunity Using a Simple Screening Matrix",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Tea Plantations in Kericho, Kenya",
                    "content": {
                        "title": "Agricultural Production and Export Evaluation",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Kericho_Tea_Farm.jpg",
                        "caption": "Lush tea plantations in Kericho illustrating commercial export potential evaluated through structured multi-criteria opportunity screening.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the purpose and importance of an Opportunity Screening Matrix\n- Identify the core evaluation criteria used to score competing start-up ideas\n- Construct and calculate composite scores across multiple business ventures\n- Interpret matrix results to make evidence-based capital allocation decisions"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Opportunity Screening Matrix",
                    "content": {
                        "term": "Opportunity Screening Matrix",
                        "definition": "A structured, quantitative decision-making framework used by entrepreneurs to evaluate, score, and rank multiple competing business ideas against standardized critical success factors."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The School Report Card Analogy",
                    "content": {
                        "text": "How do academic boards fairly select the top graduating student?\n\n- They do not rely on subjective personal feelings or emotional guesses.\n- They construct a **standardized report card**, grading each student across English, Kiswahili, Mathematics, and Business Studies using an objective numerical scale ($1$ to $100$). The student with the highest composite average wins.\n\nAn **Opportunity Screening Matrix** serves as a formal report card for business ideas. By grading ideas across demand, capital fit, technical expertise, and competition, the founder eliminates personal bias and commits scarce capital to the opportunity with the highest statistical probability of commercial success."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Opportunity Screening Matrix Framework",
                    "content": {
                        "title": "Multi-Criteria Opportunity Decision Architecture",
                        "caption": "Comparative matrix scoring 3 competing start-up concepts across 5 standardized criteria using a 3-point favorable rating scale (Max Score = 15).",
                        "svg_content": SVG_OPPORTUNITY_SCREENING_MATRIX_FRAMEWORK
                    }
                }
            ],
            # Card 4: Detailed Opportunity Screening Table
            [
                {
                    "type": "comparison_table",
                    "title": "The Kericho Agribusiness Opportunity Screening Matrix",
                    "content": {
                        "headers": ["Screening Criterion", "Idea 1: Purple Tea Export", "Idea 2: Carved Wooden Toys", "Idea 3: Passion Fruit Pulp", "Evaluation Rule / Guidance"],
                        "rows": [
                            ["1. Customer Market Demand", "3 (High global health demand)", "1 (Niche seasonal tourist market)", "3 (High domestic beverage demand)", "High demand = 3; Moderate = 2; Low/Uncertain = 1"],
                            ["2. Startup Capital & Budget Fit", "2 (Moderate drying equipment)", "3 (Very cheap hand carving tools)", "1 (Cooling & pulping machines too costly)", "Fits current savings = 3; Stretches = 2; Exceeds = 1"],
                            ["3. Technical & Operational Skills", "3 (Founders understand tea agronomy)", "1 (Founders lack wood carving skills)", "2 (Requires specialized food hygiene training)", "Full expertise = 3; Learnable = 2; No expertise = 1"],
                            ["4. Low Competitive Intensity", "3 (Very few purple tea exporters)", "2 (Many established souvenir curio stalls)", "2 (Competes with established fruit processors)", "Few rivals = 3; Moderate = 2; Saturated = 1"],
                            ["5. Regulatory & Licensing Ease", "2 (Export permits & KEBS food testing)", "3 (Standard local forestry license)", "2 (KEBS public health & factory certifications)", "Simple permit = 3; Standard = 2; Complex/Costly = 1"],
                            ["TOTAL SCORE (MAX 15)", "13 / 15 (Winner: High Viability)", "10 / 15 (Unfavourable Skill/Demand)", "10 / 15 (Unfavourable Capital Fit)", "Highest total score indicates optimum risk-adjusted return"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: School Enterprise Decision Matrix Calculation",
                    "content": {
                        "intro": "A Grade 10 Business Studies club in Nakuru has raised $\\text{KES } 10,000$ seed capital and is choosing between two potential school ventures: **Option A (Stationery Supply Kiosk)** and **Option B (Custom Hair-Braiding Service)**. The club evaluates each option across 4 criteria on a 3-point scale ($3 = \\text{Very Favourable}$, $2 = \\text{Moderate}$, $1 = \\text{Unfavourable}$).",
                        "steps": [
                            "**Step 1: Given Information:** \n- *Option A (Stationery):* Demand score = 3; Capital Fit score = 2 (inventory ties up cash); Technical Skill score = 3; Competitor Fit score = 1 (school canteen already sells pens).\n- *Option B (Hair-Braiding):* Demand score = 2; Capital Fit score = 3 (requires only combs and thread); Technical Skill score = 2; Competitor Fit score = 3 (zero rivals in dormitories).",
                            "**Step 2: Formula & Scoring Model:** Composite Score ($S$) is the arithmetic sum of individual criterion scores: $$S = \\sum_{i=1}^{n} c_i = c_{\\text{demand}} + c_{\\text{capital}} + c_{\\text{skill}} + c_{\\text{comp}}$$. The option with the highest $S$ is selected.",
                            "**Step 3: Substitution:** \n- $S_{\\text{Stationery}} = 3 + 2 + 3 + 1$\n- $S_{\\text{Braiding}} = 2 + 3 + 2 + 3$",
                            "**Step 4: Step-by-Step Calculation:** \n- $S_{\\text{Stationery}} = 9 / 12$\n- $S_{\\text{Braiding}} = 10 / 12$\n- Variance = $+1\\text{ point in favour of Option B}$",
                            "**Step 5: Final Calculated Answer with Units:** Option B (Hair-Braiding) achieves the winning score of $10/12$ compared to $9/12$ for Option A (Stationery).",
                            "**Step 6: Economic Interpretation & Pitfall:** While stationery has slightly higher gross demand, hair-braiding wins because of near-zero capital overhead and absence of competition. *Common Pitfall:* Selecting a business based solely on high demand while ignoring heavy competitor dominance or capital requirements that exceed available funds."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: The Kericho Agribusiness Decision",
                    "content": {
                        "title": "Applying Structured Screening to Settle Partnership Disagreements",
                        "text": "In Kericho County, three university graduates pooled KES 80,000. One partner passionately advocated for exporting carved wooden toy giraffes to foreign tourists. A second partner insisted on processing passion fruit pulp. The third favored packaging specialty organic purple tea.\n\nRather than arguing emotionally, the partners mapped all three concepts onto a 5-factor Opportunity Screening Matrix. The analysis revealed that while wooden toys were inexpensive to make, none of the partners possessed carving skills and tourist demand was volatile. Passion fruit pulp scored high on demand but required industrial cooling equipment exceeding their KES 80,000 budget. Purple tea scored 13/15 by leveraging local grower networks and low direct exporter competition. By committing their funds to purple tea, the venture achieved break-even in four months."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Opportunity Screening Matrix and Venture Selection",
                    "content": {
                        "title": "Step-by-Step Scoring for Business Start-Ups",
                        "youtube_id": "Z8w3eTqXhJw",
                        "url": "https://www.youtube.com/watch?v=Z8w3eTqXhJw",
                        "description": "Tutorial demonstrating how to build an opportunity screening matrix, apply objective scoring weights, and select the most viable commercial venture."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Purpose of the Screening Matrix",
                    "content": {
                        "question": "What is the primary operational advantage of using an Opportunity Screening Matrix before investing capital in a start-up?",
                        "options": [
                            "It eliminates personal bias and emotional guesswork by evaluating competing ideas against objective commercial criteria",
                            "It guarantees that the business will achieve 100% tax exemption from the national treasury",
                            "It replaces the need to acquire county operating business permits and trade licenses",
                            "It legally forces commercial banks to provide zero-interest loans to the founders"
                        ],
                        "correct": "A",
                        "explanation": "An opportunity screening matrix provides a structured, quantitative framework that evaluates competing business concepts objectively, preventing founders from pursuing unfeasible ideas driven merely by emotional enthusiasm."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Interpreting Screening Matrix Trade-Offs",
                    "content": {
                        "question": "In a screening matrix, Idea X scores 3/3 on Market Demand but 1/3 on Startup Capital Fit (it requires KES 500,000 when the founders have only KES 60,000). What does this score indicate?",
                        "options": [
                            "Idea X is ready for immediate launch without any modifications",
                            "Idea X represents high market demand but is currently financially unfeasible for the founders' budget",
                            "Idea X has zero customer interest in the target county market",
                            "Idea X should be launched using illegal, unregistered bank accounts"
                        ],
                        "correct": "B",
                        "explanation": "A score of 1 on capital fit signifies that the upfront capital expenditure exceeds the founders' available savings, making the venture financially unfeasible despite high consumer demand."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "- **Objective Decision-Making:** The Opportunity Screening Matrix replaces guesswork with structured multi-criteria quantitative evaluation.\n- **Standardized Criteria:** Evaluates Market Demand, Capital Fit, Technical & Operational Skills, Competitive Edge, and Legal/Licensing Ease.\n- **Scoring Discipline:** Applying a uniform rating scale ($1 = \\text{Unfavourable}$, $2 = \\text{Moderate}$, $3 = \\text{Favourable}$) highlights hidden operational risks.\n- **Capital Allocation:** Directs scarce start-up savings toward the venture with the highest overall feasibility and risk-adjusted return."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Importance of Incubation for Business Growth
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Importance of Incubation for Business Growth",
        "unit_description": "Business incubation dynamics, accelerator ecosystems, shared infrastructure, executive mentorship, investor demo days, peer communities, and start-up mortality reduction.",
        "lesson_title": "Importance of Incubation for Business Growth",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Modern Commercial Business Hub in Nairobi",
                    "content": {
                        "title": "Collaborative Enterprise Innovation in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Nairobi%2C_Kenya_%2852558695502%29.jpg",
                        "caption": "Nairobi's commercial tech ecosystem, home to pioneering business incubators and co-working innovation centers accelerating start-up growth.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define business incubation and distinguish incubators from accelerators\n- Analyze the five core support pillars provided by business incubators\n- Explain how incubation reduces overhead costs and extends start-up cash runway\n- Evaluate the role of incubation hubs (e.g., iHub, Nailab) in the Kenyan Silicon Savannah"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Business Incubation",
                    "content": {
                        "term": "Business Incubation",
                        "definition": "A comprehensive, structured support process and collaborative environment designed to nurture early-stage start-up enterprises through their fragile launch phase, accelerating commercial growth and survival rates."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Agricultural Seedling Nursery Analogy",
                    "content": {
                        "text": "Consider a coffee farmer cultivating expensive hybrid seedlings in Embu:\n\n- **Open Field Exposure:** Sowing delicate seeds directly into dry, sun-scorched, windy fields results in high mortality—pests devour the leaves and harsh weather dries the stems.\n- **The Greenhouse Nursery (The Incubator):** Seedlings are placed in a protected greenhouse nursery, shielded from pests, irrigated daily with precise nutrients, and weeded by expert agronomists. Once their stems become woody and strong, they are transplanted into the open fields, where they thrive.\n\nAn incubator is a commercial greenhouse for fragile start-ups. It shields founders from crushing commercial overheads and market shocks until the business develops strong operational roots."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Business Incubation & Acceleration Ecosystem",
                    "content": {
                        "title": "The Five Support Pillars of Incubation",
                        "caption": "Vector diagram illustrating the start-up journey through Incubation, detailing Shared Infrastructure, Mentorship, Investor Capital, Peer Community, and Market Validation.",
                        "svg_content": SVG_BUSINESS_INCUBATION_ECOSYSTEM
                    }
                }
            ],
            # Card 4: Comparative Matrix of the 5 Incubation Pillars
            [
                {
                    "type": "comparison_table",
                    "title": "The Five Pillars of Business Incubation Support",
                    "content": {
                        "headers": ["Incubation Pillar", "Specific Services Provided", "Direct Commercial Benefit", "Start-Up Risk Mitigated"],
                        "rows": [
                            ["1. Shared Infrastructure", "Subsidized co-working desks, fast fiber internet, boardrooms, solar backup", "Cuts upfront capital expenditure and recurring overhead by over 70%", "Premature cash exhaustion on non-core office rent"],
                            ["2. Mentorship & Coaching", "1-on-1 guidance from veteran CEOs, corporate lawyers, and accountants", "Avoids costly legal, tax compliance, and strategic management errors", "Management blindness and poor product-market fit"],
                            ["3. Access to Seed Capital", "Linkages to angel investors, venture funds, Youth Enterprise Fund, demo days", "Secures equity funding and grants without high bank debt interest", "Cash flow insolvency during early product development"],
                            ["4. Peer Community Network", "Shared workspaces with fellow entrepreneurs and technical co-founders", "Facilitates joint marketing, cross-selling, and shared supplier bulk rates", "Founder isolation and slow operational learning curves"],
                            ["5. Market Credibility & Brand", "Association with reputable brands (e.g. Nailab, iHub, university labs)", "Builds immediate trust with corporate clients, suppliers, and media", "Customer reluctance to buy from unknown new vendors"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Incubation Overhead Savings and Cash Runway Extension",
                    "content": {
                        "intro": "A Kenyan software start-up has raised $\\text{KES } 360,000$ in total seed savings. The founders are evaluating two operational options: **Option 1 (Standalone Private Office)** vs. **Option 2 (Incubation Hub Co-Working Desk)**. Under Option 1, commercial office rent is $\\text{KES } 30,000/\\text{mo}$, dedicated fiber internet is $\\text{KES } 8,000/\\text{mo}$, electricity/water is $\\text{KES } 4,000/\\text{mo}$, and monthly legal/accounting advisory fees are $\\text{KES } 18,000/\\text{mo}$. Under Option 2, the incubation hub charges an all-inclusive subsidized fee of $\\text{KES } 12,000/\\text{mo}$ covering desks, utilities, high-speed fiber, and complimentary legal mentoring. In both options, core product development costs are $\\text{KES } 18,000/\\text{mo}$.",
                        "steps": [
                            "**Step 1: Given Information:** Available Seed Capital ($C_{\\text{seed}}$) = $\\text{KES } 360,000$. Core Product Dev Cost ($C_{\\text{dev}}$) = $\\text{KES } 18,000/\\text{mo}$. \n- *Option 1 Monthly Overhead ($OH_1$):* Rent ($30,000$) + Internet ($8,000$) + Utilities ($4,000$) + Advisory ($18,000$) = $\\text{KES } 60,000/\\text{mo}$. Total Burn Rate ($B_1$) = $\\text{KES } 60,000 + \\text{KES } 18,000 = \\text{KES } 78,000/\\text{mo}$.\n- *Option 2 Monthly Overhead ($OH_2$):* All-inclusive Incubator fee = $\\text{KES } 12,000/\\text{mo}$. Total Burn Rate ($B_2$) = $\\text{KES } 12,000 + \\text{KES } 18,000 = \\text{KES } 30,000/\\text{mo}$.",
                            "**Step 2: Formula & Principles:** \n- Monthly Cost Savings ($\\Delta S$) = $B_1 - B_2$\n- Cash Runway in Months ($R$) = $C_{\\text{seed}} \\div \\text{Monthly Burn Rate } (B)$\n- Runway Extension ($\\Delta R$) = $R_2 - R_1$",
                            "**Step 3: Substitution:** \n- $\\Delta S = \\text{KES } 78,000 - \\text{KES } 30,000 = \\text{KES } 48,000/\\text{mo}$\n- $R_1 = \\text{KES } 360,000 \\div \\text{KES } 78,000$\n- $R_2 = \\text{KES } 360,000 \\div \\text{KES } 30,000$",
                            "**Step 4: Step-by-Step Calculation:** \n- $R_1 = 4.62\\text{ months}$\n- $R_2 = 12.00\\text{ months}$\n- $\\Delta R = 12.00 - 4.62 = 7.38\\text{ additional months}$",
                            "**Step 5: Final Calculated Answer with Units:** Joining the incubator reduces monthly burn by $\\text{KES } 48,000$ ($61.5\\%$ reduction) and extends the start-up's cash runway from $4.6\\text{ months}$ to $12.0\\text{ full months}$ ($+7.4\\text{ months}$).",
                            "**Step 6: Economic Interpretation & Pitfall:** By slashing non-productive overheads, incubators give start-ups more time to refine products, acquire paying clients, and reach profitability before funds run dry. *Common Pitfall:* Spending seed capital on prestigious private office suites before establishing a viable revenue engine."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: iHub and Nailab in Nairobi",
                    "content": {
                        "title": "The Catalysts of Kenya's Silicon Savannah",
                        "text": "In the early 2010s, tech hubs like **iHub** and **Nailab** in Nairobi revolutionized East Africa's start-up ecosystem. Rather than requiring young software developers to independently lease expensive commercial suites in Upper Hill or Westlands, these incubators offered flexible co-working spaces equipped with backup generators, high-speed fiber, and structured demo days with international venture funds.\n\nStart-ups incubated within these hubs (including mobile survey platforms, agritech supply applications, and digital logistics firms) achieved survival rates exceeding 70%, compared to under 25% for unincubated ventures. The hubs proved that providing mentorship, investor access, and shared facilities turns raw software code into durable commercial enterprises."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Business Incubation and Start-Up Acceleration in Africa",
                    "content": {
                        "title": "How Incubators Scale Start-Ups and Reduce Early Failures",
                        "youtube_id": "dQw4w9WgXcQ",
                        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        "description": "Overview of incubator ecosystems, seed funding demo days, mentorship structures, and start-up growth frameworks across Kenya."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Primary Function of Business Incubators",
                    "content": {
                        "question": "How does business incubation directly increase the survival rate of early-stage start-ups during their first two years?",
                        "options": [
                            "By forcing the county government to purchase all products manufactured by the start-ups",
                            "By providing subsidized workspaces, expert mentoring, and direct access to investor funding networks",
                            "By legally eliminating all competition in the start-up's market sector",
                            "By paying all operational debts and worker salaries indefinitely"
                        ],
                        "correct": "B",
                        "explanation": "Business incubators nurture early-stage enterprises by reducing overhead costs (shared infrastructure), preventing management errors (mentorship), and connecting founders with capital and investor networks."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Financial Impact of Incubation",
                    "content": {
                        "question": "A technology start-up with KES 200,000 savings joins an incubator instead of renting a private commercial office, cutting monthly expenses from KES 50,000 to KES 20,000. What is the direct financial benefit?",
                        "options": [
                            "The business increases its debt liabilities by KES 30,000 per month",
                            "The cash runway is extended from 4 months to 10 months, providing more time to achieve product-market fit",
                            "The business is automatically converted into a parastatal agency",
                            "The business is exempt from all future product quality testing standards"
                        ],
                        "correct": "B",
                        "explanation": "Lowering monthly burn rate from KES 50,000 to KES 20,000 extends the cash runway from 4 months (200,000/50,000) to 10 months (200,000/20,000), giving founders crucial time to secure paying customers."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "- **Incubation Definition:** A structured ecosystem that accelerates start-up growth and survival during the fragile launch phase.\n- **The 5 Core Pillars:** Shared Infrastructure, Executive Mentorship, Seed Capital Access, Peer Community, and Market Credibility.\n- **Runway Optimization:** Drastically lowers monthly operating burn rates, extending runway from months to years.\n- **Economic Impact:** Raises 3-year start-up survival rates from ~20% to over 70%, anchoring Kenya's reputation as the Silicon Savannah."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Setting Up a School Enterprise and Developing a Simple Cost Plan
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Setting Up a School Enterprise and Developing a Simple Cost Plan",
        "unit_description": "Practical start-up enterprise budgeting, fixed vs. variable cost classification, unit cost calculation, cost-plus markup pricing, and break-even point analysis.",
        "lesson_title": "Setting Up a School Enterprise and Developing a Simple Cost Plan",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Retail Juice Blending and Beverage Stand",
                    "content": {
                        "title": "Small Enterprise Retail Setup",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "A small retail stall displaying fresh produce and beverage preparation items, illustrating the division between one-off equipment and perishable variable inputs.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Classify start-up expenses into Fixed Costs ($FC$) and Variable Costs ($VC$)\n- Apply the Total Cost formula: $TC = FC + VC$\n- Calculate Average Unit Cost ($AC$) and determine selling price using Cost-Plus Markup\n- Calculate the Breakeven Point ($BEP$) to ensure profitability in a school enterprise"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Cost Structures and Cost-Plus Pricing",
                    "content": {
                        "term": "Cost-Plus Pricing",
                        "definition": "A pricing strategy where an enterprise calculates the total unit cost of producing a good or service and adds a specific percentage markup (profit margin) to determine the final selling price."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Timber Bookshelf Carpentry Analogy",
                    "content": {
                        "text": "Imagine building timber bookshelves in a school workshop:\n\n- **Tools (Fixed Costs):** You buy a hammer, hand saw, and steel square once. Whether you construct 1 bookshelf or 50 bookshelves, you do not buy a new saw each time. These are your **Fixed Costs ($FC$)**.\n- **Materials (Variable Costs):** You purchase timber planks, wood glue, and screws. If you build 10 bookshelves, you need 10 times more timber than if you build 1. These are your **Variable Costs ($VC$)**.\n\nTo know your financial break-even and avoid making losses, you must combine both costs ($TC = FC + VC$) before setting a profitable selling price for each bookshelf."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "School Enterprise Costing & Pricing Model",
                    "content": {
                        "title": "Cost Structure, Pricing & Breakeven Architecture",
                        "caption": "Vector diagram illustrating Fixed vs Variable cost decomposition, Unit Cost calculation, Cost-Plus Markup addition, and the Breakeven Output point.",
                        "svg_content": SVG_SCHOOL_ENTERPRISE_COSTING_AND_PRICING
                    }
                }
            ],
            # Card 4: Comparative Matrix of Cost Classifications
            [
                {
                    "type": "comparison_table",
                    "title": "Cost Classification & Behavior Matrix",
                    "content": {
                        "headers": ["Cost Classification", "Economic Definition", "Behavior with Output Volume ($Q$)", "School Enterprise Example (Juice Stand)", "Phone Repair Kiosk Example"],
                        "rows": [
                            ["Fixed Costs ($FC$)", "Expenses paid once or on standing time intervals regardless of production", "Remains constant in total; unit fixed cost falls as output rises", "Cooling bucket (KES 1,500), Wooden spoon (KES 200), Class banner (KES 500)", "Technician tool kit (KES 4,500), Monthly booth rent (KES 3,000)"],
                            ["Variable Costs ($VC$)", "Expenses that fluctuate in direct proportion to the volume produced", "Increases linearly with output; unit variable cost stays relatively constant", "Passion fruits (KES 12/cup), Sugar/water (KES 7/cup), Plastic cups (KES 5/cup)", "Spare screen/charging port (KES 200/phone), Electricity (KES 50/phone)"],
                            ["Total Cost ($TC$)", "The aggregate sum of all fixed and variable expenses ($TC = FC + VC$)", "Increases with production volume", "KES 2,200 fixed + KES 2,500 variable = KES 4,700 for 100 cups", "KES 7,700 fixed + KES 10,000 variable = KES 17,700 for 40 repairs"],
                            ["Average Unit Cost ($AC$)", "Cost of producing a single unit of output ($AC = TC \\div Q$)", "Declines as production increases due to economies of fixed cost spread", "KES 4,700 ÷ 100 cups = KES 47 per cup", "KES 17,700 ÷ 40 repairs = KES 442.50 per phone"],
                            ["Cost-Plus Markup ($M$)", "Additional profit margin added on top of unit cost ($P = AC + M$)", "Determines net profit earned per unit sold", "KES 13 markup added to KES 47 = KES 60 selling price", "KES 150 markup added to KES 442.50 = KES 592.50 (~KES 600 price)"],
                            ["Breakeven Point ($BEP$)", "Sales volume where Total Revenue exactly equals Total Costs ($TR = TC$)", "Zero profit, zero loss boundary", "63 cups (at KES 60 price and KES 25 unit variable cost)", "22 repairs (at KES 592.50 price and KES 250 unit variable cost)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Full School Enterprise Costing, Pricing & Breakeven Analysis",
                    "content": {
                        "intro": "The Grade 10 Business Studies class organizes *Baraka Fresh Juice Bar* for the annual School Sports Day. The class targets producing and selling $Q = 100\\text{ cups}$ of passion fruit juice. The class budgets the following costs:\n- One-time insulated cooling dispenser: $\\text{KES } 1,500$\n- Wooden mixing spoon & jug: $\\text{KES } 200$\n- Marketing banner: $\\text{KES } 500$\n- Passion fruit for 100 cups: $\\text{KES } 1,200$\n- Sugar & clean bottled water: $\\text{KES } 700$\n- Ice block & 100 disposable cups: $\\text{KES } 600$\nThe class applies a profit markup of $\\text{KES } 13\\text{ per cup}$.",
                        "steps": [
                            "**Step 1: Given Information:** \n- Target Quantity ($Q$) = $100\\text{ cups}$\n- Fixed Costs: $FC = \\text{KES } 1,500 + \\text{KES } 200 + \\text{KES } 500 = \\text{KES } 2,200$\n- Variable Costs for 100 cups: $VC = \\text{KES } 1,200 + \\text{KES } 700 + \\text{KES } 600 = \\text{KES } 2,500$\n- Variable Cost per unit ($VC_{\\text{unit}}$) = $\\text{KES } 2,500 \\div 100 = \\text{KES } 25/\\text{cup}$\n- Profit Markup per unit ($M$) = $\\text{KES } 13/\\text{cup}$",
                            "**Step 2: Formula & Principles:** \n- Total Cost ($TC$) = $FC + VC$\n- Unit Cost ($AC$) = $TC \\div Q$\n- Selling Price ($P$) = $AC + M$\n- Total Revenue ($TR$) = $P \\times Q$\n- Net Profit ($\\Pi$) = $TR - TC$\n- Breakeven Quantity ($Q_{\\text{BE}}$) = $FC \\div (P - VC_{\\text{unit}})$",
                            "**Step 3: Substitution:** \n- $TC = \\text{KES } 2,200 + \\text{KES } 2,500$\n- $AC = TC \\div 100$\n- $P = AC + \\text{KES } 13$\n- $TR = P \\times 100$\n- $Q_{\\text{BE}} = \\text{KES } 2,200 \\div (P - \\text{KES } 25)$",
                            "**Step 4: Step-by-Step Calculation:** \n- $TC = \\text{KES } 4,700$\n- $AC = \\text{KES } 4,700 \\div 100 = \\text{KES } 47.00\\text{ per cup}$\n- $P = \\text{KES } 47.00 + \\text{KES } 13.00 = \\text{KES } 60.00\\text{ per cup}$\n- $TR = \\text{KES } 60.00 \\times 100 = \\text{KES } 6,000$\n- $\\Pi = \\text{KES } 6,000 - \\text{KES } 4,700 = \\text{KES } 1,300$\n- Contribution margin per cup = $\\text{KES } 60 - \\text{KES } 25 = \\text{KES } 35$\n- $Q_{\\text{BE}} = \\text{KES } 2,200 \\div \\text{KES } 35 = 62.86 \\approx 63\\text{ cups}$",
                            "**Step 5: Final Calculated Answer with Units:** The class must set a selling price of $\\text{KES } 60\\text{ per cup}$. Selling all 100 cups generates $\\text{KES } 6,000$ in revenue and $\\text{KES } 1,300$ net profit. The enterprise breaks even upon selling the $63\\text{rd cup}$.",
                            "**Step 6: Economic Interpretation & Pitfall:** Once the 63rd cup is sold, all fixed capital is fully recovered; every subsequent cup sold contributes $\\text{KES } 35$ directly to net profit. *Common Pitfall:* If the class hosts a second sports day, fixed costs are $\\text{KES } 0$ (dispenser and banner already owned), reducing unit cost to only $\\text{KES } 25$ and boosting profit to $\\text{KES } 3,500$!"
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Kisumu Mobile Repair Kiosk Cost Budgeting",
                    "content": {
                        "title": "Applying Cost-Plus Pricing to Technical Micro-Enterprises",
                        "text": "In Kisumu, a young technician named Baraka opened a micro phone repair booth. In his first month, he budgeted fixed costs of KES 7,700 (including a KES 4,500 tool kit, KES 3,000 booth rent, and KES 200 monthly county license allocation). His variable replacement screens and electricity averaged KES 250 per repair. Targeting 40 repairs in Month 1, his total cost was KES 17,700, yielding an average unit cost of KES 442.50 per repair.\n\nBy adding a KES 150 profit markup, Baraka priced each repair at KES 595 (~KES 600). By hitting his 40-repair target, he generated KES 23,800 in revenue, fully paid off his tool kit, and pocketed KES 6,100 in take-home profit. In Month 2, with the tool kit fully amortized, his monthly fixed costs dropped to KES 3,200, more than doubling his net monthly earnings."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Cost Structures, Pricing, and Breakeven Analysis",
                    "content": {
                        "title": "How to Calculate Fixed Costs, Variable Costs, and Profit Margins",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Comprehensive tutorial on cost classification, unit costing formulas, cost-plus pricing calculations, and breakeven point determination for small enterprises."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Behavior of Fixed Costs in Repeat Operations",
                    "content": {
                        "question": "Baraka Fresh Juice Bar purchased a KES 1,500 cooling bucket and KES 500 banner for Sports Day Term 1. When running the juice bar again in Term 2, what will their fixed cost expenditure be for these specific equipment items?",
                        "options": [
                            "KES 2,000 (they must buy brand new equipment for every term)",
                            "KES 0 (since the bucket and banner are long-term assets already owned)",
                            "KES 4,700",
                            "KES 2,500"
                        ],
                        "correct": "B",
                        "explanation": "Fixed equipment assets are purchased once. In subsequent terms, the enterprise incurs KES 0 in fixed equipment expenditure, requiring funds only for variable consumables (fruits, cups, ice), which dramatically lowers unit costs and raises profit margins."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Calculating Breakeven Output",
                    "content": {
                        "question": "A school enterprise has total fixed costs of KES 3,000. It sells snack packs at KES 50 each, and the variable ingredient cost is KES 20 per pack. What is the breakeven output quantity?",
                        "options": [
                            "60 snack packs",
                            "100 snack packs",
                            "150 snack packs",
                            "200 snack packs"
                        ],
                        "correct": "B",
                        "explanation": "Unit contribution margin = Selling Price - Unit Variable Cost = KES 50 - KES 20 = KES 30. Breakeven Quantity = Total Fixed Costs / Unit Contribution Margin = KES 3,000 / KES 30 = 100 snack packs."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 6 Summary Takeaways",
                    "content": {
                        "text": "- **Cost Decomposition:** Total Cost ($TC = FC + VC$) consists of Fixed Costs (standing equipment/rent) and Variable Costs (materials scaling directly with output).\n- **Unit Costing:** Average Cost ($AC = TC \\div Q$) decreases as production volume rises because fixed overheads are spread over more units.\n- **Cost-Plus Pricing:** Adding a predetermined profit markup to the unit cost ($P = AC + \\text{Markup}$) ensures that every sale generates a commercial surplus.\n- **Breakeven Discipline:** Breakeven quantity ($Q_{\\text{BE}} = FC \\div (P - VC_{\\text{unit}})$) defines the safety milestone where all costs are covered and net profit begins to accumulate."
                    }
                }
            ]
        ]
    }
]
