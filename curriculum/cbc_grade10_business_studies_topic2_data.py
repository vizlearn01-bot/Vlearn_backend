"""
VLearn CBC Grade 10 Business Studies — Topic 2: Business Goals
Full Structured Lesson Card Definitions (Lessons 1 to 6)
"""

from curriculum.cbc_grade10_business_studies_topic2_svgs import (
    SVG_PLANNING_HIERARCHY,
    SVG_FACTORS_INFLUENCING_GOALS,
    SVG_SWOT_AND_GOAL_CYCLE,
    SVG_SMART_GOAL_FRAMEWORK,
    SVG_GOAL_ALIGNMENT_LADDER,
    SVG_VARIANCE_ANALYSIS
)

TOPIC_2_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Importance of Business Goals
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of Business Goals",
        "unit_description": "Vision, Mission, Goals, Objectives, and analyzing how goal setting provides direction, motivation, and performance control.",
        "lesson_title": "Meaning and Importance of Business Goals",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Enterprise Operations in Kenya",
                    "content": {
                        "title": "Strategic Direction in Small Enterprise",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Nairobi_City_Market%2C_2025_%2801%29.jpg",
                        "caption": "A retail business operating in an urban Kenyan commercial center, illustrating how clear strategic goals provide focus and guide daily sales activities.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define vision, mission, business goals, operational objectives, and routine activities\n- Distinguish strategic business goals from daily routine operational tasks\n- Explain the primary benefits of setting clear goals for enterprise success"
                    }
                }
            ],
            # Card 2: Core Concept & Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Business Goals and Mission Statements",
                    "content": {
                        "term": "Business Goal",
                        "definition": "A broad, high-level target or strategic outcome that an enterprise aims to achieve over a specified period to guide decisions and measure success."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Football Match Without Goalposts Analogy",
                    "content": {
                        "text": "Running a business without clear goals is like playing a football match without goalposts: players run and sweat, but there is no way to score, track progress, or coordinate victory.\n\nSetting goals provides **direction**, **employee motivation**, **disciplined resource allocation**, and a **benchmark for performance measurement**."
                    }
                }
            ],
            # Card 3: Vector SVG — Planning Hierarchy Ladder
            [
                {
                    "type": "suggested_diagram",
                    "title": "Hierarchy of Business Planning",
                    "content": {
                        "title": "From Vision to Daily Operations",
                        "caption": "Vector diagram illustrating the hierarchical planning ladder from Vision and Mission down to Business Goals, Operational Objectives, and Routine Tasks.",
                        "svg_content": SVG_PLANNING_HIERARCHY
                    }
                }
            ],
            # Card 4: Distinguishing Goals from Routine Activities
            [
                {
                    "type": "comparison_table",
                    "title": "Strategic Goals vs. Routine Daily Activities",
                    "content": {
                        "headers": ["Planning Level", "Time Horizon", "Primary Purpose", "Practical Business Example"],
                        "rows": [
                            ["Vision", "10+ Years", "Aspirational dream for the ultimate future", "'To be Kenya's cleanest and most trusted dairy cooperative.'"],
                            ["Mission", "Ongoing", "Core purpose and daily reason for existence", "'Providing fresh, high-protein organic milk to local schools daily.'"],
                            ["Business Goal", "1–5 Years", "Broad strategic outcome to achieve", "'Increase total annual sales revenue by 20% in the county.'"],
                            ["Operational Objective", "Months / Quarter", "Specific, measurable action milestone", "'Secure milk supply contracts with 10 new schools by March 31st.'"],
                            ["Routine Activity", "Daily / Weekly", "Repetitive operational maintenance tasks", "Milking dairy cattle, sterilizing cooling tanks, delivering milk crates."]
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Mwende's Bakery in Machakos
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Decomposing Mwende's Bakery Enterprise Plan",
                    "content": {
                        "intro": "Mwende operates a commercial bakery in Machakos. Categorize her business statements into the correct level of the planning hierarchy:",
                        "steps": [
                            "**Statement 1:** 'To bake fresh, affordable, whole-wheat bread for primary school students in Machakos County.' $\\rightarrow$ **Mission Statement** (defines core purpose and target market).",
                            "**Statement 2:** 'To expand bakery sales into neighboring Kitui and Makueni counties over the next two years.' $\\rightarrow$ **Business Goal** (broad strategic growth target).",
                            "**Statement 3:** 'Sign supply agreements with 5 new boarding schools by the end of next month.' $\\rightarrow$ **Operational Objective** (specific measurable milestone).",
                            "**Statement 4:** 'Purchasing 20 bags of flour, mixing dough, and firing the brick oven every morning at 4:00 AM.' $\\rightarrow$ **Routine Activities** (operational tasks required to execute the objectives)."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Transitioning from Daily Survival to Enterprise Growth",
                        "text": "A youth boda-boda transport group that operates without goals merely survives day-to-day. When they set an explicit goal to 'save KES 2,500 every week to acquire a second motorcycle in 18 months,' their daily rides gain strategic purpose, enabling business expansion and capital accumulation."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Power of Goal Setting in Business",
                    "content": {
                        "title": "Entrepreneurial Strategic Planning",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Real-world entrepreneurs explaining how explicit goal setting maintains team alignment, avoids bankruptcy, and drives sustainable profitability."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Mission Statement Definition",
                    "content": {
                        "question": "Which of the following describes a formal statement defining the core purpose of a business and why it exists?",
                        "options": [
                            "Routine activity checklist",
                            "Business target",
                            "Mission statement",
                            "Operating expense budget"
                        ],
                        "correct": "C",
                        "explanation": "A mission statement defines the fundamental purpose, activities, values, and target audience of an enterprise, answering why the business exists."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Goal Setting and Employee Motivation",
                    "content": {
                        "question": "Why does setting clear, well-defined business goals motivate company employees?",
                        "options": [
                            "It eliminates the need to pay wages and salaries",
                            "It provides clear benchmarks to strive toward, creating a sense of achievement and accountability when targets are met",
                            "It exempts the business from national tax obligations",
                            "It encourages staff to focus only on non-essential wants"
                        ],
                        "correct": "B",
                        "explanation": "Clear goals give employees a defined direction, clarify performance expectations, and boost morale through recognized milestone achievements."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Planning Hierarchy**: Vision (10+ yrs) $\\rightarrow$ Mission (Purpose) $\\rightarrow$ Goals (Broad Targets) $\\rightarrow$ Objectives (Milestones) $\\rightarrow$ Routine Activities (Daily Tasks).\n2. **Core Benefits**: Direction, motivation, resource prioritization, and performance measurement.\n3. **Routine vs. Strategy**: Daily operational chores maintain the business but must not be confused with forward-looking goals."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Factors Considered When Setting Goals
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Factors Considered When Setting Goals",
        "unit_description": "Evaluating internal capabilities and external market/legal environments to set feasible business goals.",
        "lesson_title": "Factors Considered When Setting Goals",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Corporate Boardroom Strategic Planning Session",
                    "content": {
                        "title": "Evaluating Internal and External Business Factors",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5e/The_Prime_Minister%2C_Shri_Narendra_Modi_addressing_at_the_India-Kenya_Business_Forum%2C_in_Nairobi%2C_Kenya_on_July_11%2C_2016.jpg",
                        "caption": "Business leaders and executives analyzing economic conditions, market demand, and internal resources during strategic planning forums in Nairobi.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and explain key internal factors that constrain or enable business goals\n- Identify and explain key external environmental factors (competition, laws, ethics)\n- Evaluate enterprise feasibility by aligning internal resources with external market opportunities"
                    }
                }
            ],
            # Card 2: Core Concept & Environmental Classification
            [
                {
                    "type": "definition_card",
                    "title": "Internal vs. External Business Factors",
                    "content": {
                        "term": "Business Environment Factors",
                        "definition": "The internal organizational strengths/resources and external market/legal conditions that dictate the realism and feasibility of business goals."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The School T-Shirt Business Trap",
                    "content": {
                        "text": "If a student business club with KES 1,000 cash and no printing press sets a goal to 'print 10,000 custom T-shirts for their 800-student school in two weeks,' the goal is doomed to fail.\n\nFeasible goals require balancing **internal capabilities** (available cash, machinery, staff skills) with **external reality** (market size, competitor pricing, legal regulations)."
                    }
                }
            ],
            # Card 3: Vector SVG — Internal & External Factors Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Internal and External Factors Influencing Goals",
                    "content": {
                        "title": "Enterprise Capabilities vs. Market Conditions",
                        "caption": "Vector diagram illustrating the dual-pillar framework of internal controllable resources vs. external uncontrollable market and legal factors.",
                        "svg_content": SVG_FACTORS_INFLUENCING_GOALS
                    }
                }
            ],
            # Card 4: Summary Table of Internal & External Factors
            [
                {
                    "type": "comparison_table",
                    "title": "Analysis of Internal vs. External Business Factors",
                    "content": {
                        "headers": ["Dimension", "Factor Category", "Key Evaluative Question", "Impact on Goal Formulation"],
                        "rows": [
                            ["Financial Capital", "Internal", "How much cash reserves and credit are available?", "Prevents setting expansion goals that exceed budget"],
                            ["Human Skills & Tech", "Internal", "Do employees possess the required technical expertise?", "Ensures operational goals match workforce capability"],
                            ["Risk Appetite", "Internal", "How much financial risk is the owner willing to bear?", "Determines aggressive vs conservative growth pace"],
                            ["Market & Competition", "External", "What are competitors charging and what do buyers want?", "Guides realistic sales volumes and pricing targets"],
                            ["Legal & Regulatory", "External", "What health, tax, and licensing laws apply?", "Prevents illegal operations and regulatory fines"],
                            ["Ethical & Environmental", "External", "Does the goal protect community welfare and ecology?", "Builds customer trust and prevents legal penalties"]
                        ]
                    }
                }
            ],
            # Card 5: Step Process — Feasibility Checklist
            [
                {
                    "type": "step_process",
                    "title": "3-Point Feasibility Alignment Protocol",
                    "content": {
                        "intro": "Managers apply this 3-step test before finalizing any enterprise goal:",
                        "steps": [
                            {"title": "1. Resource Fit Test (Internal)", "description": "Verify that cash capital, staff skills, equipment, and production capacity can support the target volume."},
                            {"title": "2. Market & Legal Fit Test (External)", "description": "Confirm customer demand is sufficient and all county/national regulatory permits are secured."},
                            {"title": "3. Ethical & Environmental Check", "description": "Ensure goal execution causes no environmental pollution, labor exploitation, or community harm."}
                        ]
                    }
                }
            ],
            # Card 6: Worked Example — Tomato Project Feasibility
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Feasibility Audit for a School Tomato Enterprise",
                    "content": {
                        "intro": "A Grade 10 agriculture project team proposes a goal: 'To cultivate and sell 500 kg of fresh tomatoes to the school canteen in 3 months.' Audit the goal's feasibility:",
                        "steps": [
                            "**Step 1 — Internal Resource Audit:** The team has an allocated school garden plot, reliable borehole water, certified seeds, and 5 committed members. $\\rightarrow$ **Internal Resource Fit: Excellent**.",
                            "**Step 2 — External Market Demand Audit:** The school canteen purchases 150–180 kg of fresh tomatoes monthly (totaling ~500 kg over 3 months). $\\rightarrow$ **External Demand Fit: Excellent**.",
                            "**Step 3 — Technical Agronomic Timeline:** Tomato crops reach harvest maturity within 75–90 days. $\\rightarrow$ **Timeline Fit: Realistic**.",
                            "**Step 4 — Final Feasibility Verdict:** The goal is realistic, achievable, and fully aligned with internal resources and external market demand."
                        ]
                    }
                }
            ],
            # Card 7: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Safaricom 5G Rollout Feasibility Analysis",
                        "text": "Before Safaricom set its corporate goal to roll out 5G high-speed internet across Kenyan cities, it had to evaluate internal capital expenditure budgets for new fiber base stations (internal resource) and secure national radio frequency spectrum licenses from the Communications Authority of Kenya (external legal factor)."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Internal vs External Business Environment Analysis",
                    "content": {
                        "title": "Strategic Business Environment Scanning",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "How enterprise executives evaluate internal capabilities and external market trends to formulate realistic commercial targets."
                    }
                }
            ],
            # Card 8: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying External Factors",
                    "content": {
                        "question": "Which of the following is an external factor that an enterprise must analyze when formulating its pricing and sales goals?",
                        "options": [
                            "The company's own factory machinery",
                            "Competitor pricing strategies and consumer market demand",
                            "The financial capital contributed by the owner",
                            "The customer service skills of the sales team"
                        ],
                        "correct": "B",
                        "explanation": "Competitor actions, market demand, inflation, and government laws originate outside the business and represent external environmental factors."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Ethical Responsibility in Goal Setting",
                    "content": {
                        "question": "Why must ethical and social responsibilities be considered when formulating corporate business goals?",
                        "options": [
                            "To eliminate all market competition",
                            "To ensure business activities do not harm the community or natural environment, safeguarding long-term brand trust",
                            "To avoid paying taxes legally",
                            "To maximize short-term profits regardless of public consequences"
                        ],
                        "correct": "B",
                        "explanation": "Ethical goal setting prevents pollution, worker exploitation, and legal penalties, building sustainable stakeholder trust."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Internal Factors**: Financial capital, human skills, machinery, strengths/weaknesses, and risk tolerance.\n2. **External Factors**: Consumer demand, competitor moves, government regulations, and environmental ethics.\n3. **Feasibility Rule**: Sustainable business goals occur only where internal capabilities align with external market opportunities."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Steps in Setting Business Goals
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Steps in Setting Business Goals",
        "unit_description": "Mastering the 10-step goal-setting cycle, performing SWOT analysis, and establishing Key Result Areas.",
        "lesson_title": "Steps in Setting Business Goals",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Business Strategic Planning Workshop in Kenya",
                    "content": {
                        "title": "Executing the 10-Step Goal-Setting Process",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Prime_Minister%2C_Shri_Narendra_Modi_addressing_at_the_India-Kenya_Business_Forum%2C_in_Nairobi%2C_Kenya_on_July_11%2C_2016_%281%29.jpg",
                        "caption": "Enterprise executives and managers collaborating on market analysis, SWOT assessments, and action plans in a business development forum.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Outline and sequence the 10 steps of the formal business goal-setting process\n- Conduct a comprehensive SWOT analysis (Strengths, Weaknesses, Opportunities, Threats)\n- Identify Key Result Areas (KRAs) and develop actionable operational plans"
                    }
                }
            ],
            # Card 2: Core Concept & SWOT Definition
            [
                {
                    "type": "definition_card",
                    "title": "SWOT Analysis and Key Result Areas",
                    "content": {
                        "term": "SWOT Analysis",
                        "definition": "A strategic management framework used to evaluate an enterprise's internal Strengths and Weaknesses alongside external Opportunities and Threats."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Logical Roadmap to Setting Goals",
                    "content": {
                        "text": "Managers do not pick random numbers when setting goals. Goal setting is a disciplined 10-step circular process that maps where the enterprise is starting from, where it wants to go, and the precise tasks needed to get there."
                    }
                }
            ],
            # Card 3: Vector SVG — 10-Step Cycle & SWOT Matrix
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 10-Step Goal-Setting Cycle & SWOT Quadrants",
                    "content": {
                        "title": "Goal Formulation and SWOT Architecture",
                        "caption": "Vector diagram detailing the 10 sequential goal-setting steps mapped against internal Strengths/Weaknesses and external Opportunities/Threats.",
                        "svg_content": SVG_SWOT_AND_GOAL_CYCLE
                    }
                }
            ],
            # Card 4: Step Process — The 10 Sequential Steps
            [
                {
                    "type": "step_process",
                    "title": "The 10 Steps of Business Goal Setting",
                    "content": {
                        "intro": "Follow this sequential workflow to establish enterprise goals:",
                        "steps": [
                            {"title": "1. Define Vision & Mission", "description": "Anchor all goals in the company's long-term dream and core purpose."},
                            {"title": "2. Conduct SWOT Analysis", "description": "Audit internal Strengths & Weaknesses against external Opportunities & Threats."},
                            {"title": "3. Identify Key Result Areas (KRAs)", "description": "Pinpoint critical departments (sales, quality, customer retention, cost reduction)."},
                            {"title": "4. Brainstorm Potential Goals", "description": "Generate a wide list of creative strategic targets without premature filtering."},
                            {"title": "5. Apply SMART Criteria", "description": "Refine brainstormed ideas to make them specific, measurable, achievable, relevant, and time-bound."},
                            {"title": "6. Prioritize Goals", "description": "Select top 2–3 high-impact goals to avoid spreading resources too thin."},
                            {"title": "7. Communicate Goals", "description": "Share targets clearly with all staff, suppliers, and partners to ensure alignment."},
                            {"title": "8. Develop Action Plans", "description": "Specify exact tasks, individual responsibilities, budgets, and milestone dates."},
                            {"title": "9. Monitor Progress", "description": "Track actual operational performance continuously against target milestones."},
                            {"title": "10. Review & Revise", "description": "Calculate variance and adjust plans dynamically as market conditions shift."}
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Kiprotich Cyber Café in Kericho
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: SWOT Analysis & Goal Formulation for a Cyber Café",
                    "content": {
                        "intro": "Kiprotich operates a cyber café in Kericho. Perform a SWOT analysis and formulate an actionable strategic goal:",
                        "steps": [
                            "**Internal Strengths (S):** High-speed optical fiber internet connection and an automatic backup diesel generator.",
                            "**Internal Weaknesses (W):** Cramped shop with only 6 computer terminals, causing long customer queues during rush hours.",
                            "**External Opportunities (O):** The nearby university campus has made all coursework submissions online-only.",
                            "**External Threats (T):** A new commercial business center is opening across the road.",
                            "**Formulated Strategic SMART Goal:** 'To expand computer workstation capacity from 6 to 10 terminals within the next 90 days to capture university assignment demand (Opportunity) and retain market leadership ahead of new competitors (Threat).'"
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Dairy Cooperatives Annual Strategic Review",
                        "text": "When agricultural cooperatives (like Brookside or New KCC suppliers) plan annual collection targets, they systematically conduct SWOT analysis: reviewing climate rainfall forecasts (Threat), cold-chain transport truck capacity (Weakness/Strength), and urban milk consumption trends (Opportunity) before setting collection volumes."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "How to Perform a SWOT Analysis in Business",
                    "content": {
                        "title": "Practical SWOT Analysis Framework",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Step-by-step tutorial demonstrating how small businesses map internal strengths/weaknesses and external opportunities/threats into strategic action plans."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: SWOT Classification",
                    "content": {
                        "question": "A business owner notes during an audit that their cyber café owns a 'high-capacity automatic diesel backup generator.' In a SWOT matrix, this is classified as an:",
                        "options": [
                            "External Opportunity",
                            "Internal Strength",
                            "External Threat",
                            "Internal Weakness"
                        ],
                        "correct": "B",
                        "explanation": "A backup generator is an asset owned and controlled internally by the business, providing an operational advantage (Internal Strength)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Purpose of Action Plans",
                    "content": {
                        "question": "What is the primary function of Step 8 (Developing Action Plans) in the goal-setting process?",
                        "options": [
                            "To change the company's long-term vision completely",
                            "To translate strategic goals into concrete daily tasks, assigning responsibilities, budgets, and deadlines",
                            "To brainstorm unrestricted creative ideas",
                            "To conceal financial records from tax auditors"
                        ],
                        "correct": "B",
                        "explanation": "Action plans operationalize high-level SMART goals by detailing who will do what, with what resources, and by what specific deadline."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **Systematic 10 Steps**: Vision $\\rightarrow$ SWOT $\\rightarrow$ KRAs $\\rightarrow$ Brainstorm $\\rightarrow$ SMART $\\rightarrow$ Prioritize $\\rightarrow$ Communicate $\\rightarrow$ Action Plan $\\rightarrow$ Monitor $\\rightarrow$ Review.\n2. **SWOT Framework**: Internal Strengths/Weaknesses vs. External Opportunities/Threats.\n3. **Action Plans**: Ensure strategic goals are executed through concrete tasks, budgets, and accountable staff."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: SMART Short-Term Goals
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "SMART Short-Term Goals",
        "unit_description": "Converting vague desires into precise, actionable short-term goals (< 1 year) using the SMART criteria.",
        "lesson_title": "SMART Short-Term Goals",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Retail Store Sales Tracking and Metrics",
                    "content": {
                        "title": "Tracking Short-Term Operational Targets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/48/Nairobi_City_Market%2C_2025_%2803%29.jpg",
                        "caption": "Retail business owners monitoring daily inventory and sales figures, demonstrating the precision of short-term quantifiable targets in retail management.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define each component of the SMART acronym (Specific, Measurable, Achievable, Relevant, Time-bound)\n- Contrast vague, ambiguous wishes with well-structured SMART goals\n- Formulate and repair realistic short-term SMART goals for diverse business scenarios"
                    }
                }
            ],
            # Card 2: Core Concept & SMART Definitions
            [
                {
                    "type": "definition_card",
                    "title": "SMART Goals and Short-Term Horizons",
                    "content": {
                        "term": "SMART Goal",
                        "definition": "A goal that is Specific, Measurable, Achievable, Relevant, and Time-bound, designed to provide clear operational focus within a timeframe of under one year."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Why Vague Goals Fail",
                    "content": {
                        "text": "Statements like *'I want to make more money'* or *'We need to increase sales'* are weak because they lack numbers, deadlines, and accountability.\n\nThe **SMART criteria** convert ambiguous desires into quantifiable operational targets that allow employees to measure daily progress."
                    }
                }
            ],
            # Card 3: Vector SVG — SMART Framework & Carpenter Repair Model
            [
                {
                    "type": "suggested_diagram",
                    "title": "The SMART Goal Formulation Framework",
                    "content": {
                        "title": "SMART Conversion Architecture",
                        "caption": "Vector diagram detailing each SMART element (S, M, A, R, T) and illustrating the step-by-step transformation of a vague wish into a high-precision business target.",
                        "svg_content": SVG_SMART_GOAL_FRAMEWORK
                    }
                }
            ],
            # Card 4: Comparison Table — Vague vs. SMART Goals
            [
                {
                    "type": "comparison_table",
                    "title": "Comparison of Vague Wishes vs. SMART Goals",
                    "content": {
                        "headers": ["Vague Wish", "Missing SMART Elements", "Corrected SMART Goal", "Managerial Advantage"],
                        "rows": [
                            ["'I want to get more customers.'", "No numbers, no deadline, no specific channel", "'To enroll 50 new regular home-delivery milk clients by June 30th.'", "Provides exact sales targets and timeline"],
                            ["'We must cut business expenses.'", "No percentage, no department specified", "'To reduce packaging material costs by 10% in the production unit over the next 3 months.'", "Enables cost-center accountability"],
                            ["'I want to expand my shop.'", "No specific location or metric", "'To establish one new retail kiosk in Machakos Town by December 31st.'", "Guides capital budgeting and lease scouting"]
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Repairing the Carpenter's Goal
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: 5-Step Repair of a Vague Carpentry Goal",
                    "content": {
                        "intro": "Help a local furniture maker repair the vague statement: 'I want to make more chairs.'",
                        "steps": [
                            "**Step 1 — S (Specific):** What exact product? $\\rightarrow$ 'Handcrafted mahogany dining chairs.'",
                            "**Step 2 — M (Measurable):** How much volume? $\\rightarrow$ 'Increase output by **20 units per month**.'",
                            "**Step 3 — A (Achievable):** Is it possible? $\\rightarrow$ 'Yes, workshop floor space and seasoned timber supplies are available.'",
                            "**Step 4 — R (Relevant):** Does it align with strategy? $\\rightarrow$ 'Yes, dining furniture represents the highest-margin product line.'",
                            "**Step 5 — T (Time-bound):** By when? $\\rightarrow$ '**By September 30th** (end of third quarter).'",
                            "**Final SMART Goal Formulation:** 'To increase the production of handcrafted mahogany dining chairs by 20 units per month by September 30th.'"
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "School Enterprise Inventory and Sales Targets",
                        "text": "School business clubs and student canteen stores use short-term SMART goals (such as 'selling 150 exercise books and 200 pens during the first two weeks of Term 1') to calculate exact working capital requirements, negotiate bulk supplier discounts, and avoid stock wastage."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Setting SMART Goals for Small Businesses",
                    "content": {
                        "title": "Practical SMART Goal Implementation",
                        "youtube_id": "WqlX5z6k4eQ",
                        "url": "https://www.youtube.com/watch?v=WqlX5z6k4eQ",
                        "description": "How small business managers convert broad ambitions into quantifiable monthly milestones that drive team productivity and profits."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Missing SMART Elements",
                    "content": {
                        "question": "Which element of the SMART acronym is missing from the following goal: 'To increase our customer satisfaction score from 7.5 to 9.0 out of 10'?",
                        "options": [
                            "Specific",
                            "Measurable",
                            "Achievable",
                            "Time-bound"
                        ],
                        "correct": "D",
                        "explanation": "While specific and measurable, the goal lacks a target deadline or completion date, meaning it is not Time-bound."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Relevance in Goal Setting",
                    "content": {
                        "question": "Why is the goal 'To purchase an agricultural tractor for our small retail electronics repair kiosk' considered weak under SMART criteria?",
                        "options": [
                            "It is not Measurable",
                            "It is not Relevant to the core business operations",
                            "It is not Time-bound",
                            "It is not Specific"
                        ],
                        "correct": "B",
                        "explanation": "A farm tractor is an agricultural machine and is completely irrelevant to the operational mission and commercial activities of an electronics repair shop."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **SMART Components**: Specific (clear), Measurable (numbers), Achievable (feasible), Relevant (mission-aligned), Time-bound (deadline).\n2. **Short-Term Scope**: Targets designed for completion within 1 year or less.\n3. **Clarity**: Quantified SMART goals provide unambiguous daily operational targets and accountability."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: SMART Long-Term Goals and Alignment
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "SMART Long-Term Goals and Alignment",
        "unit_description": "Formulating 3-to-5-year strategic goals and cascading them into aligned yearly, quarterly, and monthly milestones.",
        "lesson_title": "SMART Long-Term Goals and Alignment",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Industrial Manufacturing and Processing Facility",
                    "content": {
                        "title": "Long-Term Strategic Capital Investment",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Nairobi_Skyline_Savannah_Kenya_May19_R1600687.jpg",
                        "caption": "The expanding commercial and industrial skyline of Nairobi, representing long-term corporate vision, multi-year capital investment, and strategic market expansion.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define long-term strategic goals and describe their 3-to-5-year scope\n- Explain the critical concept of goal alignment across organizational departments\n- Construct a cascading goal alignment ladder connecting a 5-year strategic goal to yearly, quarterly, and monthly workplans"
                    }
                }
            ],
            # Card 2: Core Concept & Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Long-Term Goals and Goal Alignment",
                    "content": {
                        "term": "Goal Alignment",
                        "definition": "The organizational process of ensuring that short-term milestones, departmental targets, and daily tasks directly support and lead to the realization of the enterprise's long-term strategic goals."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Mountain Climbing Cascade Analogy",
                    "content": {
                        "text": "Climbing a high mountain peak (a 5-year strategic goal) cannot be achieved in a single leap. Climbers must establish intermediate camps (yearly and quarterly milestones) and take disciplined steps each day (weekly tasks).\n\nIf daily activities do not align with the mountain peak, the enterprise wastes capital on misdirected efforts."
                    }
                }
            ],
            # Card 3: Vector SVG — Goal Alignment Ladder
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4-Tier Cascading Goal Alignment Ladder",
                    "content": {
                        "title": "Connecting Vision to Frontline Action",
                        "caption": "Vector diagram illustrating the 4-tier strategic cascading hierarchy connecting a 5-year corporate vision to daily frontline workplans.",
                        "svg_content": SVG_GOAL_ALIGNMENT_LADDER
                    }
                }
            ],
            # Card 4: Comparison Table — Short-Term vs. Long-Term Goals
            [
                {
                    "type": "comparison_table",
                    "title": "Short-Term Tactical Goals vs. Long-Term Strategic Goals",
                    "content": {
                        "headers": ["Dimension", "Short-Term Goals", "Long-Term Goals", "Strategic Rationale"],
                        "rows": [
                            ["Time Horizon", "Less than 1 year (weeks, months)", "3 to 5+ years", "Short-term delivers quick wins; long-term builds sustained market power"],
                            ["Strategic Focus", "Operational tactics & immediate cash flow", "Market expansion, new factories, corporate leadership", "Long-term requires substantial capital accumulation"],
                            ["Uncertainty & Risk", "Low uncertainty; predictable variables", "High uncertainty; shifting economic trends", "Long-term goals require flexibility and periodic review"],
                            ["Resource Funding", "Financed from routine operating cash flow", "Requires retained profits, equity, or bank loans", "Capital budgeting must be planned years in advance"],
                            ["Example", "'Increase sales by 10% this quarter.'", "'Establish a modern processing plant in Kisumu by 2030.'", "Intermediate milestones bridge the gap to the 5-year vision"]
                        ]
                    }
                }
            ],
            # Card 5: Step Process — The Cascading Goal Alignment Ladder
            [
                {
                    "type": "step_process",
                    "title": "The 4-Tier Goal Alignment Cascade",
                    "content": {
                        "intro": "Align organizational efforts using this structured 4-tier cascade:",
                        "steps": [
                            {"title": "Tier 1: 5-Year Strategic Goal (The Peak)", "description": "e.g., 'Become Kenya's leading exporter of packaged organic tea, reaching 50 tons per year by 2030.'"},
                            {"title": "Tier 2: Yearly Milestone", "description": "e.g., 'Year 1: Obtain international organic certifications and upgrade packaging to European standards.'"},
                            {"title": "Tier 3: Quarterly Target", "description": "e.g., 'Quarter 1: Complete comprehensive laboratory soil tests to verify chemical-free status.'"},
                            {"title": "Tier 4: Monthly & Weekly Workplan", "description": "e.g., 'This Week: Contract an agricultural organic auditor and conduct farm fertilization inspection.'"}
                        ]
                    }
                }
            ],
            # Card 6: Worked Example — Kericho Tea Exporters Alignment Ladder
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Constructing Kericho Tea Exporters Goal Ladder",
                    "content": {
                        "intro": "Kericho Tea Exporters sets a 5-year strategic vision. Trace how their strategic goal cascades down to this week's frontline tasks:",
                        "steps": [
                            "**5-Year Strategic Goal (Peak):** 'Export 50 tons of certified organic packaged tea annually to the United Kingdom by 2030.'",
                            "**Year 1 Milestone:** 'Secure UK organic agricultural certification and re-engineer recyclable packaging.'",
                            "**Quarter 1 Target:** 'Conduct certified laboratory chemical residue tests on tea leaf samples from all 50 contracted outgrower farms.'",
                            "**This Week's Task:** 'Draft the contract for the lead agronomist to audit farm compost fertilizer preparation.'",
                            "**Alignment Check:** Every single task performed this week connects directly to the 5-year export milestone, eliminating wasted effort!"
                        ]
                    }
                }
            ],
            # Card 7: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "SACCO 5-Year Commercial Plaza Project",
                        "text": "When a local transport SACCO targets a long-term goal of 'building a 5-story commercial rental plaza in 5 years,' their Year 1 milestone is purchasing a land parcel, their monthly milestone is collecting KES 1,000,000 from members, and their daily action is issuing deposit receipts. Daily thrift constructs the 5-year plaza."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Strategic Planning: Aligning Short-Term Actions with Long-Term Vision",
                    "content": {
                        "title": "Cascading Strategic Goals",
                        "youtube_id": "7_j5N5V1N9c",
                        "url": "https://www.youtube.com/watch?v=7_j5N5V1N9c",
                        "description": "How corporate organizations build cascading goal alignment from multi-year strategic visions down to frontline weekly workplans."
                    }
                }
            ],
            # Card 8: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Strategic Long-Term Goal Identification",
                    "content": {
                        "question": "Which of the following is the best example of an aligned long-term strategic goal for an agricultural processing cooperative?",
                        "options": [
                            "Purchasing 5 bags of fertilizer tomorrow morning",
                            "Increasing milk collection volume by 2% next week",
                            "Becoming the dominant national distributor of processed cheese and yogurt within the next 5 years",
                            "Repairing the water pipe in the milk intake dock today"
                        ],
                        "correct": "C",
                        "explanation": "Strategic long-term goals address multi-year market leadership, infrastructure, and enterprise expansion over a 3-to-5-year horizon."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Consequences of Misalignment",
                    "content": {
                        "question": "When daily employee tasks and monthly department targets fail to support the enterprise's long-term vision, the business is suffering from a failure in:",
                        "options": [
                            "Government taxation",
                            "Market competition",
                            "Goal alignment",
                            "Precautionary liquidity"
                        ],
                        "correct": "C",
                        "explanation": "Goal alignment ensures that short-term milestones and daily frontline workplans are directly connected to and support the primary strategic outcomes."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Long-Term Strategic Scope**: 3-to-5-year roadmaps that guide market expansion and capital investment.\n2. **Goal Alignment Cascade**: 5-Year Goal $\\rightarrow$ Yearly Milestone $\\rightarrow$ Quarterly Target $\\rightarrow$ Weekly Action.\n3. **Resource Efficiency**: Proper alignment ensures every shilling and staff hour contributes toward the strategic peak."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Monitoring, Review, and Appreciation of Goal Setting
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Monitoring, Review, and Appreciation of Goal Setting",
        "unit_description": "Performance tracking, calculating variance (Favorable vs. Unfavorable), and implementing corrective feedback loops.",
        "lesson_title": "Monitoring, Review, and Appreciation of Goal Setting",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Business Manager Reviewing Performance Variance Reports",
                    "content": {
                        "title": "Performance Monitoring and Feedback",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "Business professionals evaluating monthly revenue variance reports, auditing operational expenditures, and taking corrective managerial actions.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the importance of performance monitoring and the managerial feedback loop\n- Calculate variance using the standard formula: $\\text{Variance} = \\text{Actual Result} - \\text{Target Amount}$\n- Correctly distinguish between Favorable (F) and Unfavorable (U) variances for Revenue vs. Cost items\n- Formulate data-driven corrective managerial actions to resolve performance shortfalls"
                    }
                }
            ],
            # Card 2: Core Concept & The Variance Formula
            [
                {
                    "type": "definition_card",
                    "title": "Performance Monitoring and Variance",
                    "content": {
                        "term": "Variance",
                        "definition": "The mathematical difference between the actual results achieved by a business and its planned budget or target amount."
                    }
                },
                {
                    "type": "formula_breakdown",
                    "title": "The Standard Business Variance Formula",
                    "content": {
                        "formula": "\\text{Variance} = \\text{Actual Result} - \\text{Target (Budgeted) Amount}",
                        "breakdown": "- **Actual Result**: The real monetary or unit figure achieved during operations.\n- **Target (Budgeted) Amount**: The planned benchmark figure established during goal setting.\n- **Variance**: The deviation showing whether performance exceeded or lagged behind plans."
                    }
                }
            ],
            # Card 3: Vector SVG — Variance Analysis & Feedback Loop
            [
                {
                    "type": "suggested_diagram",
                    "title": "Business Performance Monitoring & Variance Analysis",
                    "content": {
                        "title": "Variance Analysis Architecture",
                        "caption": "Vector diagram detailing the variance calculation for Revenue (Sales) vs Expenses (Costs) and illustrating the corrective managerial feedback loop.",
                        "svg_content": SVG_VARIANCE_ANALYSIS
                    }
                }
            ],
            # Card 4: Critical Interpretation Rule — Revenue vs. Expense Items
            [
                {
                    "type": "comparison_table",
                    "title": "Interpreting Variance: Revenue/Sales vs. Cost/Expenses",
                    "content": {
                        "headers": ["Financial Category", "Condition", "Mathematical Sign", "Variance Classification", "Business Meaning"],
                        "rows": [
                            ["Revenue / Sales / Profit", "Actual > Target", "Positive (+)", "FAVORABLE (F)", "Enterprise generated more income than planned; profit expands!"],
                            ["Revenue / Sales / Profit", "Actual < Target", "Negative (-)", "UNFAVORABLE (U)", "Enterprise fell short of sales target; cash inflow is lower than planned."],
                            ["Costs / Operating Expenses", "Actual > Budget", "Positive (+)", "UNFAVORABLE (U)", "Enterprise overspent beyond budget; profits are reduced!"],
                            ["Costs / Operating Expenses", "Actual < Budget", "Negative (-)", "FAVORABLE (F)", "Enterprise saved money on expenses; profit margin increases!"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculations
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: 6-Step Variance Calculations (Sales vs Costs)",
                    "content": {
                        "intro": "The management of Kiprono's Poultry Enterprise evaluates the following monthly performance records:",
                        "steps": [
                            "**Step 1 — Understand Given Information:**\n- **Case A (Sales Revenue):** Planned Target = $\\text{KES } 20,000$; Actual Sales = $\\text{KES } 23,500$.\n- **Case B (Operating Costs):** Budgeted Cost = $\\text{KES } 5,000$; Actual Costs = $\\text{KES } 5,800$.",
                            "**Step 2 — Identify What is Required:** Calculate variance and assign Favorable (F) or Unfavorable (U) status for both cases.",
                            "**Step 3 — State the Relevant Formula:** $\\text{Variance} = \\text{Actual Result} - \\text{Target Amount}$.",
                            "**Step 4 — Substitute and Compute Values:**\n- **Case A (Sales):** $\\text{Variance} = 23,500 - 20,000 = \\mathbf{+ \\text{KES } 3,500}$.\n- **Case B (Costs):** $\\text{Variance} = 5,800 - 5,000 = \\mathbf{+ \\text{KES } 800}$.",
                            "**Step 5 — Classify and Interpret:**\n- **Case A (Sales):** **+ KES 3,500 (FAVORABLE / F)** because actual sales exceeded the planned target, increasing gross profit.\n- **Case B (Costs):** **+ KES 800 (UNFAVORABLE / U)** because actual expenses exceeded budget, reducing net profits.",
                            "**Step 6 — Common Mistake Callout:** *Watch out!* A positive variance on expenses is **Unfavorable** because overspending reduces business profits!"
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Matatu Transport SACCO Fleet Monitoring",
                        "text": "In Kenyan public transport SACCOs, fleet controllers track daily fare collections per vehicle. If a matatu reports an unfavorable variance (e.g. collecting KES 6,000 against an KES 8,000 target), the SACCO immediately investigates mechanical delays, traffic jams, or fare pilferage, implementing prompt corrective actions."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Preparing a Business Variance Analysis Report",
                    "content": {
                        "title": "Variance Analysis and Corrective Control",
                        "youtube_id": "4j2emMn7GEk",
                        "url": "https://www.youtube.com/watch?v=4j2emMn7GEk",
                        "description": "Demonstrating how retail managers compare actual revenues and expenses against budgeted targets to detect operational leakage early."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Expense Variance Calculation",
                    "content": {
                        "question": "A bakery budgets KES 4,000 for monthly electricity but actually spends KES 4,500. Calculate the variance and interpret the business performance.",
                        "options": [
                            "KES 500 (Favorable)",
                            "KES -500 (Unfavorable)",
                            "KES 500 (Unfavorable)",
                            "KES -500 (Favorable)"
                        ],
                        "correct": "C",
                        "explanation": "Variance = Actual (4,500) - Budgeted (4,000) = KES 500. Because electricity is an expense item, spending more than budgeted is Unfavorable for enterprise profitability."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Purpose of the Feedback Loop",
                    "content": {
                        "question": "Why is a continuous performance review feedback loop vital in enterprise management?",
                        "options": [
                            "It exempts the company from local business licenses",
                            "It identifies operational performance gaps early, allowing management to take timely corrective actions before losses accumulate",
                            "It forces the enterprise to shut down immediately",
                            "It guarantees 100% error-free decision making at all times"
                        ],
                        "correct": "B",
                        "explanation": "The feedback loop detects deviations from targets early, enabling managers to adjust pricing, reduce costs, or modify workplans before business survival is threatened."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 6 Summary Takeaways",
                    "content": {
                        "text": "1. **Variance Formula**: $\\text{Variance} = \\text{Actual Result} - \\text{Target Amount}$.\n2. **Interpretation Rules**: Higher revenue is Favorable; higher expense is Unfavorable.\n3. **Feedback Loop**: Detect deviations $\\rightarrow$ Analyze root causes $\\rightarrow$ Execute corrective actions."
                    }
                }
            ]
        ]
    }
]
