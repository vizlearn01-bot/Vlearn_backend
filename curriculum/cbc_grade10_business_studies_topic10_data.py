"""
VLearn CBC Grade 10 Business Studies — Topic 10: Consumer Satisfaction
Full Structured Lesson Card Definitions (Lessons 1 to 8)
"""

from curriculum.cbc_grade10_business_studies_topic10_svgs import (
    SVG_CONSUMER_SATISFACTION_SPECTRUM,
    SVG_TERMS_AND_CONDITIONS_FRAMEWORK,
    SVG_CAUSES_OF_DISSATISFACTION_TAXONOMY,
    SVG_CONSUMER_REMEDIES_HIERARCHY,
    SVG_SURVEY_DESIGN_ARCHITECTURE,
    SVG_SURVEY_TABULATION_AND_VISUALIZATION,
    SVG_CONTINUOUS_FEEDBACK_LOOP_CYCLE,
    SVG_SATISFACTION_TO_SUSTAINABILITY_CHAIN
)

TOPIC_10_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Importance of Consumer Satisfaction
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of Consumer Satisfaction",
        "unit_description": "Conceptual foundations of consumer satisfaction, customer vs consumer roles, expectation-disconfirmation dynamics, the leaky bucket model, CLTV, and enterprise retention economics.",
        "lesson_title": "Meaning and Importance of Consumer Satisfaction",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Vibrant Restaurant and Retail Service in Nairobi",
                    "content": {
                        "title": "Customer Service and Retail Dining in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "Customers engaging with polite, attentive staff in a Kenyan dining and retail marketplace, illustrating the positive commercial impact of superior consumer satisfaction.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between a 'consumer' and a 'customer' in everyday business transactions\n- Define consumer satisfaction using the expectation vs. perceived performance model\n- Explain the 'Leaky Bucket' analogy regarding customer acquisition versus customer retention\n- Analyze the 6 primary strategic and financial benefits of customer satisfaction for business longevity"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Consumer Satisfaction and Customer Retention",
                    "content": {
                        "term": "Consumer Satisfaction",
                        "definition": "The psychological and commercial state achieved when a product or service's perceived performance meets or surpasses the consumer's pre-purchase expectations."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Leaky Bucket Analogy & Core Roles",
                    "content": {
                        "text": "Understanding customer dynamics requires distinguishing roles and visualizing the revenue bucket:\n\n- **Customer vs. Consumer:** A *customer* purchases the good or service (e.g., a parent paying for school shoes), whereas the *consumer* is the end user who physically utilizes it (e.g., the student wearing the shoes).\n- **The Leaky Bucket Analogy:** Running a business is like keeping a bucket filled with water (active paying customers). Spending money on advertising is pouring water into the top (**Customer Acquisition**). Losing unhappy customers is a hole in the bottom (**Customer Churn**).\n- **Retention Efficiency:** If your bucket is leaky due to poor customer care, advertising money is wasted. Plugging the leaks through high satisfaction creates sustainable profit growth."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Consumer Satisfaction Spectrum and Leaky Bucket Model",
                    "content": {
                        "title": "The Expectation-Disconfirmation Spectrum & Retention Economics",
                        "caption": "Vector diagram illustrating the four psychological satisfaction zones (Dissatisfaction, Mere Satisfaction, Delight, Advocacy) and the Leaky Bucket customer retention mechanism.",
                        "svg_content": SVG_CONSUMER_SATISFACTION_SPECTRUM
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Expectation vs. Performance Satisfaction Matrix",
                    "content": {
                        "headers": ["Disconfirmation Level", "Psychological State", "Consumer Behavior", "Business Revenue Impact"],
                        "rows": [
                            ["Performance << Expectation", "Severe Dissatisfaction", "Complains loudly, posts negative reviews, defects to rivals", "High customer churn, destroyed reputation, lost CLTV"],
                            ["Performance == Expectation", "Mere Satisfaction", "Content with transaction, but easily swayed by competitor discounts", "Fragile customer loyalty, vulnerable to aggressive price wars"],
                            ["Performance > Expectation", "Customer Delight", "Repeats purchases willingly, praises business to close peers", "Predictable recurring sales, lower price sensitivity"],
                            ["Performance >>> Expectation", "Brand Advocacy", "Acts as an unpaid ambassador, vigorously defends the brand", "Viral word-of-mouth growth, highest Customer Lifetime Value"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Customer Churn Rate and Customer Lifetime Value (CLTV)",
                    "content": {
                        "intro": "'Shama Chicken House' in Nakuru starts the trading year with $N_0 = 500$ loyal regular lunch diners. During the year, $L = 50$ diners stop visiting due to slow table turnover. On average, each loyal diner spends $\\text{KES } 600$ per visit, eats lunch at Shama $F = 40\\text{ times per year}$, and remains an active customer for an average lifespan of $T = 3\\text{ years}$. Calculate the annual Churn Rate, the Customer Lifetime Value (CLTV) per patron, and the total revenue lost to customer churn over 3 years.",
                        "steps": [
                            "**Step 1: Given Information:** Initial customer base $N_0 = 500$ diners. Lost customers $L = 50$ diners. Average spend per visit $S = \\text{KES } 600$. Annual visit frequency $F = 40\\text{ visits/year}$. Customer relationship lifespan $T = 3\\text{ years}$.",
                            "**Step 2: Formula & Economic Rules:**\n$$\\text{Customer Churn Rate (\\%)} = \\left(\\frac{L}{N_0}\\right) \\times 100$$\n$$\\text{Annual Value per Customer (AV)} = S \\times F$$\n$$\\text{Customer Lifetime Value (CLTV)} = \\text{AV} \\times T$$\n$$\\text{Total Lost Revenue} = L \\times \\text{CLTV}$$",
                            "**Step 3: Substitution:**\n$$\\text{Churn Rate} = \\left(\\frac{50}{500}\\right) \\times 100$$\n$$\\text{AV} = \\text{KES } 600 \\times 40 = \\text{KES } 24,000$$\n$$\\text{CLTV} = \\text{KES } 24,000 \\times 3 = \\text{KES } 72,000$$\n$$\\text{Total Lost Revenue} = 50 \\times \\text{KES } 72,000$$",
                            "**Step 4: Calculation:**\n$$\\text{Churn Rate} = 0.10 \\times 100 = 10\\%$$\n$$\\text{CLTV} = \\text{KES } 72,000$$\n$$\\text{Total Lost Revenue} = \\text{KES } 3,600,000$$",
                            "**Step 5: Final Answer & Unit:** The annual customer churn rate is $10\\%$. The Customer Lifetime Value (CLTV) per loyal diner is $\\text{KES } 72,000$. The cumulative enterprise revenue lost due to losing 50 customers over 3 years is $\\text{KES } 3,600,000$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Losing just 10% of regular diners inflicts a devastating 3.6 million shilling loss over 3 years because acquiring replacement customers is 5x more costly. *Common Pitfall:* Looking only at single-day receipts (KES 600) rather than recognizing the compounding multi-year Customer Lifetime Value."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Shama Chicken House in Nakuru",
                    "content": {
                        "title": "Queue Management and Service Consistency in Nakuru City",
                        "text": "In Nakuru City, 'Shama Chicken House' consistently commands long lunchtime queues while competing eateries across the street with identical prices remain half-empty. Shama achieves this by standardizing five customer satisfaction touchpoints: serving steaming-hot kienyeji chicken within 8 minutes of seating, maintaining impeccably sanitized dining areas, training servers in warm hospitality, providing generous portions, and issuing instant polite apologies whenever a rare delay occurs. This high satisfaction turns everyday diners into active advocates who drive continuous word-of-mouth patronage."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Customer Satisfaction and Retention in Enterprise Economics",
                    "content": {
                        "title": "Understanding Customer Satisfaction, Retention, and CLTV",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Educational overview of customer satisfaction dynamics, the expectation-performance gap, and retention cost advantages in enterprise management."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Customer Retention vs. Acquisition Economics",
                    "content": {
                        "question": "Why is customer retention universally recognized as a far more profitable strategy than continuous customer acquisition for an established enterprise?",
                        "options": [
                            "Retained customers are legally prohibited from negotiating prices under Kenyan competition rules",
                            "Retaining a satisfied customer is approximately 5 times cheaper than spending money on marketing to acquire a new one",
                            "Acquiring new customers requires mandatory registration fees with County Revenue Authorities",
                            "Existing customers never demand receipts or warranties on purchased goods"
                        ],
                        "correct": "B",
                        "explanation": "Customer acquisition involves heavy advertising, sales commissions, and promotional discounts. Retained customers already trust the firm, resulting in repeat purchases with minimal marketing expenses."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Customer vs. Consumer Distinction",
                    "content": {
                        "question": "A high school headteacher visits an educational bookshop in Nairobi and pays KES 45,000 for 100 Grade 10 Business Studies textbooks to be used by the Grade 10 class. In commercial terms, how are the headteacher and the students correctly classified?",
                        "options": [
                            "The headteacher is the consumer and the students are the customers",
                            "Both the headteacher and the students are classified strictly as intermediate distributors",
                            "The headteacher is the customer who conducts the purchase, while the students are the consumers who utilize the books",
                            "The students are creditors and the headteacher is the sole proprietor"
                        ],
                        "correct": "C",
                        "explanation": "The 'customer' is the entity who executes the commercial purchase transaction (the headteacher), while the 'consumers' are the ultimate end-users who derive utility from the goods (the students)."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Expectation-Disconfirmation Model:** Satisfaction occurs when perceived product performance matches or exceeds prior consumer expectations.\n2. **Customer vs. Consumer:** The customer buys the good, while the consumer is the ultimate end-user.\n3. **The Leaky Bucket Principle:** Sustainable revenue depends on plugging customer churn leaks through excellent service rather than solely pouring acquisition advertising.\n4. **5x Cost Advantage:** Retaining an existing satisfied customer is five times cheaper than recruiting a new one and maximizes Customer Lifetime Value (CLTV)."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Terms and Conditions for the Supply of Goods and Services
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Terms and Conditions for the Supply of Goods and Services",
        "unit_description": "Contractual rules of commercial transactions, explicit vs implied terms, Sale of Goods Act, Kenya Consumer Protection Act, warranties, guarantees, and statutory consumer protections.",
        "lesson_title": "Terms and Conditions for the Supply of Goods and Services",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Transaction Documentation and Legal Contracts in Kenya",
                    "content": {
                        "title": "Commercial Business Documentation in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "An entrepreneur reviewing contract terms and conditions of supply, illustrating the legal framework governing commercial exchanges and consumer rights in Kenya.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the concept and purpose of Terms and Conditions of Supply in commercial contracts\n- Identify the 6 core explicit pillars of supply terms: description, price, delivery, warranties, returns, liability\n- Differentiate between Explicit Terms and Statutory Implied Terms under Kenyan law\n- Apply the Kenyan consumer rights trinity: 'Satisfactory Quality', 'Fit for Purpose', and 'As Described'"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Terms of Supply and Statutory Implied Rights",
                    "content": {
                        "term": "Terms and Conditions of Supply",
                        "definition": "The formal rules, obligations, and legal clauses that govern a sale transaction between a supplier and a buyer, establishing pricing, delivery, quality standards, and dispute remedies."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Rules of the Football Pitch & Explicit vs Implied Terms",
                    "content": {
                        "text": "Just as a sports match requires clear rules to prevent chaos, commercial transactions require binding terms of supply:\n\n- **Explicit Terms:** Clauses openly stated in written contracts, printed on receipts, or agreed verbally (e.g., price tag of KES 15,000, 30-day payment term).\n- **Statutory Implied Terms:** Legal guarantees automatically written into every transaction by the **Kenya Consumer Protection Act** and **Sale of Goods Act (Cap 31)**, regardless of what a seller writes on a receipt.\n- **The 'No Returns' Myth:** A retailer's signboard reading *'Goods once sold cannot be returned or refunded'* is legally invalid against statutory implied terms of quality and fitness."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Commercial Terms of Supply and Statutory Consumer Rights Framework",
                    "content": {
                        "title": "Contractual Architecture and Statutory Implied Consumer Rights Trinity",
                        "caption": "Vector diagram showcasing the 6 explicit pillars of supply contracts alongside Kenya's 3 mandatory implied terms (Satisfactory Quality, Fit for Purpose, As Described).",
                        "svg_content": SVG_TERMS_AND_CONDITIONS_FRAMEWORK
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Explicit Terms vs. Statutory Implied Terms Matrix",
                    "content": {
                        "headers": ["Dimension", "Explicit Contractual Terms", "Statutory Implied Terms", "Warranty vs. Guarantee"],
                        "rows": [
                            ["Origin & Basis", "Mutually negotiated or printed on invoices and receipts", "Automatically enacted by Kenyan Parliament under Consumer Protection Act", "Warranty is manufacturer promise; Guarantee is legal refund assurance"],
                            ["Flexibility", "Parties can adjust prices, payment dates, and transport terms", "Mandatory and non-negotiable; cannot be excluded by fine print", "Warranties usually specify repair; Guarantees often provide full refund"],
                            ["Core Standard", "Agreed unit price, delivery destination, and packaging", "Goods must be of Satisfactory Quality, Fit for Purpose, and As Described", "Warranty is limited in time (e.g., 1 yr); Guarantees cover immediate performance"],
                            ["Violation Consequence", "Breach of contract claim or agreed late payment interest", "Statutory offense; triggers mandatory refund, replacement, or damages", "Vendor must repair defect; failure allows consumer to demand full cash refund"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Warranty Repair vs. Statutory Non-Compliance Penalty Calculation",
                    "content": {
                        "intro": "'Mwangaza Solar Tech' in Nairobi sells a commercial solar inverter to a customer for $P = \\text{KES } 45,000$ with an explicit 12-month warranty. Within 4 months, a factory capacitor fails. Repairing the internal module under warranty costs the firm $C_{\\text{parts}} = \\text{KES } 6,500$ in components and $C_{\\text{labor}} = \\text{KES } 2,000$ in technician labor. If the firm unlawfully refuses warranty service citing a 'No Returns' fine print, the Consumer Protection Directorate enforces contract rescission (full refund) plus a mandatory $r = 20\\%$ statutory administrative compensation penalty. Calculate the standard warranty cost, the statutory penalty liability, and the net extra loss resulting from non-compliance.",
                        "steps": [
                            "**Step 1: Given Information:** Product retail price $P = \\text{KES } 45,000$. Replacement parts cost $C_{\\text{parts}} = \\text{KES } 6,500$. Labor cost $C_{\\text{labor}} = \\text{KES } 2,000$. Statutory penalty rate $r = 20\\% = 0.20$.",
                            "**Step 2: Formulas & Statutory Rules:**\n$$\\text{Standard Warranty Cost} = C_{\\text{repair}} = C_{\\text{parts}} + C_{\\text{labor}}$$\n$$\\text{Statutory Penalty Liability} = P \\times (1 + r)$$\n$$\\text{Net Extra Loss from Non-Compliance} = \\text{Statutory Penalty Liability} - C_{\\text{repair}}$$",
                            "**Step 3: Substitution:**\n$$C_{\\text{repair}} = \\text{KES } 6,500 + \\text{KES } 2,000 = \\text{KES } 8,500$$\n$$\\text{Statutory Penalty Liability} = \\text{KES } 45,000 \\times (1 + 0.20)$$\n$$\\text{Net Extra Loss} = (\\text{KES } 45,000 \\times 1.20) - \\text{KES } 8,500$$",
                            "**Step 4: Calculation:**\n$$C_{\\text{repair}} = \\text{KES } 8,500$$\n$$\\text{Statutory Penalty Liability} = \\text{KES } 54,000$$\n$$\\text{Net Extra Loss} = \\text{KES } 54,000 - \\text{KES } 8,500 = \\text{KES } 45,500$$",
                            "**Step 5: Final Answer & Unit:** The cost of honoring the standard warranty is $\\text{KES } 8,500$. The total statutory liability from unlawful refusal is $\\text{KES } 54,000$. Unlawful refusal inflicts a net extra loss of $\\text{KES } 45,500$ on the enterprise.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Respecting explicit warranties and statutory implied rights is financially prudent. *Common Pitfall:* Believing that fine print notices like 'Goods once sold cannot be returned' shield a vendor from statutory liability under Kenyan law."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Smartphone Retail and Consumer Rights in Nairobi",
                    "content": {
                        "title": "Resolving Retail Electronics Disputes under Kenyan Law",
                        "text": "A customer in Nairobi bought a new smartphone for KES 15,000 from an electronics dealer on Luthuli Avenue. After 3 weeks, the internal speaker malfunctioned. The dealer refused assistance, pointing to a receipt footnote stating 'No refunds after 7 days'. The customer lodged a complaint with the Competition Authority of Kenya (CAK) under the Consumer Protection Act. The CAK established that smartphones carry an implied term of Satisfactory Quality and durability for a reasonable lifespan (at least 1 year). The retailer was ordered to replace the phone with a brand-new sealed unit, demonstrating that statutory rights override receipt disclaimers."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Terms and Conditions of Supply and Consumer Protection Law",
                    "content": {
                        "title": "Understanding Commercial Supply Terms and Consumer Rights",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Comprehensive explanation of commercial contracts, warranties, guarantees, and statutory consumer protection rules governing goods and services."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Statutory Implied Term of Fitness for Purpose",
                    "content": {
                        "question": "A poultry farmer in Kiambu informs a hardware dealer: 'I need an automatic water pumping motor capable of pushing borehole water to a 10,000-litre tank elevated on a 4-storey tower.' The dealer sells her a specific motor model. When installed, the motor cannot push water past the 1st floor. What statutory implied term has been breached?",
                        "options": [
                            "Limitation of Liability clause",
                            "Implied term of Fitness for Purpose",
                            "Explicit payment credit terms",
                            "Free delivery terms"
                        ],
                        "correct": "B",
                        "explanation": "When a buyer expressly informs the seller of their specific need and relies on the seller's expertise, the law implies a non-negotiable term that the supplied good must be fit for that designated purpose."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Legal Validity of 'No Cash Refund' Notices",
                    "content": {
                        "question": "A customer buys an electric blender whose motor catches fire on the first day due to a factory wiring defect. The shopkeeper points to a wall sign stating: 'Goods once sold are not returnable.' Under Kenyan consumer law, how does this sign affect the buyer's rights?",
                        "options": [
                            "The sign is fully binding and the customer has zero legal remedy",
                            "The sign is legally null and void against the statutory implied term of Satisfactory Quality, entitling the buyer to a full refund or replacement",
                            "The customer must pay the shopkeeper a 50% penalty to inspect the broken blender",
                            "The shopkeeper is legally required to arrest the manufacturer"
                        ],
                        "correct": "B",
                        "explanation": "Under Section 12 of the Kenya Consumer Protection Act, statutory implied terms of satisfactory quality cannot be waived or negated by shop notices or fine print disclaimers."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Terms of Supply Framework:** Explicit terms define price, delivery, risk transfer, and payment schedules agreed between parties.\n2. **Statutory Trinity:** Every commercial sale implies 3 non-negotiable legal rights: Satisfactory Quality, Fit for Purpose, and As Described.\n3. **Warranties vs. Guarantees:** Warranties bind the seller to repair/replace defects within a period; guarantees assure money-back satisfaction.\n4. **Primacy of Law:** Retailer disclaimers like 'No Returns, No Refunds' are legally unenforceable against defective products under Kenyan consumer law."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Causes of Consumer Dissatisfaction
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Causes of Consumer Dissatisfaction",
        "unit_description": "Comprehensive analysis of commercial failure modes: product defects, service delays, misleading advertising, poor communication, unfair supply terms, and their impact on customer defection.",
        "lesson_title": "Causes of Consumer Dissatisfaction",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Retail Shopping and Product Inspection in Nairobi",
                    "content": {
                        "title": "Retail Marketplace Quality and Consumer Inspection",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                        "caption": "Customers inspecting goods in a retail market, highlighting where product defects, misleading descriptions, or service frictions can trigger severe consumer dissatisfaction.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define consumer dissatisfaction and identify the Expectation vs. Reality mismatch\n- Categorize the 5 major drivers of consumer dissatisfaction in commercial enterprises\n- Analyze real-world failure scenarios in Kenyan product, logistics, and communication systems\n- Calculate service delay rates and evaluate the financial cost of operational failure"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Consumer Dissatisfaction and Service Failure",
                    "content": {
                        "term": "Consumer Dissatisfaction",
                        "definition": "The negative emotional and cognitive reaction experienced by a buyer when the actual performance, quality, or delivery of a product falls short of promised or anticipated standards."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Broken Promise Analogy & 5 Failure Vectors",
                    "content": {
                        "text": "Consumer dissatisfaction is the direct consequence of a **broken business promise**:\n\n- **The Broken Promise Analogy:** If you promise to help a classmate study at 4:00 PM but arrive at 6:00 PM without books and browse your phone, you have created resentment through unreliability. Commercial failure works identically.\n- **The 5 Failure Vectors:**\n  1. **Product Defects:** Substandard materials, short shelf life, or broken parts.\n  2. **Service Delays:** Unfulfilled delivery deadlines and agonizing checkout queues.\n  3. **Misleading Claims:** False advertising, hidden fees, and exaggerated capabilities.\n  4. **Poor Communication:** Arrogant staff, unreturned calls, and defensive attitudes.\n  5. **Unfair Supply Terms:** Refusing legitimate warranty repairs or imposing arbitrary penalties."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Taxonomy of Consumer Dissatisfaction and Failure Vectors",
                    "content": {
                        "title": "The 5 Core Pillars of Commercial Failure and Dissatisfaction",
                        "caption": "Vector diagram detailing the five major failure modes (Defects, Delays, False Claims, Poor Communication, Unfair Terms) along with specific Kenyan enterprise failure examples.",
                        "svg_content": SVG_CAUSES_OF_DISSATISFACTION_TAXONOMY
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Classification Matrix of Consumer Dissatisfaction Causes",
                    "content": {
                        "headers": ["Failure Category", "Root Operational Cause", "Customer Experience Impact", "Kenyan Enterprise Example"],
                        "rows": [
                            ["Product Defect", "Poor quality control, cheap materials, expired stock", "Product breaks down quickly or poses safety hazard", "A bottle of fresh milk souring 3 days prior to expiry date stamp"],
                            ["Service Delay", "Under-staffing, poor logistics, stock-out bottlenecks", "Customer loses time, misses personal schedule", "Food delivery arriving 3 hours late after lunch break has ended"],
                            ["Misleading Claims", "Deceptive marketing, hidden fees, inaccurate sizing", "Customer feels cheated, distrusts business pricing", "Detergent marked '2.0 KG' weighing only 1.3 KG on verified scales"],
                            ["Poor Communication", "Untrained rude staff, unresponsiveness on digital channels", "Emotional frustration, escalation of minor disputes", "Online boutique blocking buyer's phone after sending wrong size"],
                            ["Unfair Supply Terms", "Rigid return policies, refusal to honor warranty rules", "Financial loss, forced legal arbitration", "Electronics shop refusing to repair television with factory screen fault"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Service Delay Rate and Total Operational Failure Cost",
                    "content": {
                        "intro": "'BodaBoda Swift Deliveries' in Kisumu completes $N = 400$ hot meal orders per week. The firm guarantees delivery within 30 minutes. If an order exceeds 45 minutes, the firm incurs a customer retention compensation voucher of $V = \\text{KES } 150$. If a delivered meal is physically spilled/damaged (defect), the firm provides a full free replacement costing the business $R = \\text{KES } 450$. During a severe rainy week, $D = 64$ orders were delayed beyond 45 minutes and $M = 12$ meals suffered physical damage. Calculate the Service Delay Rate (\\%), Defect Rate (\\%), and the Total Operational Failure Cost for that week.",
                        "steps": [
                            "**Step 1: Given Information:** Total weekly orders $N = 400$. Delayed deliveries $D = 64$. Defective/damaged deliveries $M = 12$. Delay compensation voucher cost $V = \\text{KES } 150$. Meal replacement cost $R = \\text{KES } 450$.",
                            "**Step 2: Formulas & Metric Rules:**\n$$\\text{Service Delay Rate (\\%)} = \\left(\\frac{D}{N}\\right) \\times 100$$\n$$\\text{Defect Rate (\\%)} = \\left(\\frac{M}{N}\\right) \\times 100$$\n$$\\text{Total Operational Failure Cost} = (D \\times V) + (M \\times R)$$",
                            "**Step 3: Substitution:**\n$$\\text{Delay Rate} = \\left(\\frac{64}{400}\\right) \\times 100$$\n$$\\text{Defect Rate} = \\left(\\frac{12}{400}\\right) \\times 100$$\n$$\\text{Total Failure Cost} = (64 \\times \\text{KES } 150) + (12 \\times \\text{KES } 450)$$",
                            "**Step 4: Calculation:**\n$$\\text{Delay Rate} = 0.16 \\times 100 = 16\\%$$\n$$\\text{Defect Rate} = 0.03 \\times 100 = 3\\%$$\n$$\\text{Total Failure Cost} = \\text{KES } 9,600 + \\text{KES } 5,400 = \\text{KES } 15,000$$",
                            "**Step 5: Final Answer & Unit:** The service delay rate is $16\\%$, the defect rate is $3\\%$, and the total failure cost incurred by the logistics enterprise for the week is $\\text{KES } 15,000$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** A 16% delay rate and 3% defect rate erode profit margins and drive customers to rival couriers. *Common Pitfall:* Viewing delay vouchers as a minor marketing expense rather than recognizing how operational failures create direct cash drain and churn."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: E-Commerce Apparel and Social Media Vendors",
                    "content": {
                        "title": "Addressing the 'What I Ordered vs. What I Got' Crisis in Digital Trade",
                        "text": "The rapid growth of social commerce in Kenya (Instagram and TikTok apparel boutiques) has highlighted the danger of consumer dissatisfaction. In Nairobi, several fashion boutiques faced public boycotts after advertising bespoke chiffon evening dresses using filtered internet photographs, but delivering poorly tailored synthetic garments with misaligned seams. Dissatisfied customers shared comparison photos on social media, leading to viral brand erosion. Sustainable online boutiques solved this by publishing authentic unedited videos of garments, offering Cash on Delivery (COD), and maintaining transparent 7-day exchange policies."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Causes of Consumer Dissatisfaction and Service Failure Analysis",
                    "content": {
                        "title": "Analyzing Commercial Failure Modes and Dissatisfaction Drivers",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "Educational breakdown of the root causes of customer dissatisfaction including product flaws, queue friction, misleading advertising, and rude customer support."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Misleading Advertising",
                    "content": {
                        "question": "A hotel in Mombasa advertises 'All-Inclusive Luxury Weekend Buffet with Unlimited Free Fresh Fruit Juice'. Upon arrival, guests are billed KES 400 for every glass of passion juice, with the manager claiming only tap water is free. What primary cause of consumer dissatisfaction does this illustrate?",
                        "options": [
                            "Uncontrollable weather disruption",
                            "Misleading information and deceptive pricing",
                            "Statutory force majeure",
                            "Alternative Dispute Resolution"
                        ],
                        "correct": "B",
                        "explanation": "Advertising a service as 'unlimited free fruit juice' while secretly charging extra fees at consumption constitutes deceptive marketing and misleading information, triggering severe customer resentment."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Impact of Employee Communication Attitude",
                    "content": {
                        "question": "When a customer visits a retail shop to report that a purchased solar lamp does not switch on, the attendant shouts aggressively: 'You broke it yourself because you do not know how to read manuals!' How does this reaction impact the enterprise?",
                        "options": [
                            "It successfully protects company profit margins by discouraging warranty claims",
                            "It destroys consumer trust, converts a simple product repair into acute brand hostility, and drives customer defection",
                            "It is legally required under standard commercial grievance procedures",
                            "It increases the Customer Lifetime Value of the shop"
                        ],
                        "correct": "B",
                        "explanation": "Aggressive, disrespectful employee communication exacerbates service failures, driving dissatisfied customers away permanently and triggering damaging negative word-of-mouth."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **Expectation Gap:** Dissatisfaction arises whenever perceived performance falls beneath promised standards.\n2. **5 Major Failure Vectors:** Operational flaws center on product defects, service delays, false claims, rude staff, and rigid terms.\n3. **Financial Drain of Failure:** High defect and delay rates directly trigger expensive voucher payouts, refund claims, and customer churn.\n4. **Reputational Risk:** In the digital era, single instances of deceptive marketing or arrogant communication can quickly destroy brand equity."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Remedies for Consumer Dissatisfaction
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Remedies for Consumer Dissatisfaction",
        "unit_description": "Legal, commercial, and relational redress pathways: repair, replacement, full/partial refund, consequential compensation, contract rescission, specific performance, sincere apologies, and ADR.",
        "lesson_title": "Remedies for Consumer Dissatisfaction",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Technical Repair and Hardware Service in Kenya",
                    "content": {
                        "title": "Equipment Repair and Grievance Resolution in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
                        "caption": "A technical artisan repairing mechanical components, representing prompt corrective remedies that restore consumer utility and rebuild market trust.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a consumer remedy and its role in commercial dispute resolution\n- Identify and explain the 8 primary remedies available to dissatisfied consumers in Kenya\n- Distinguish between goods-based remedies, service-based remedies, and relational remedies\n- Calculate total redress payouts involving both direct refunds and consequential financial compensation"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Consumer Remedy and Consequential Redress",
                    "content": {
                        "term": "Consumer Remedy",
                        "definition": "A legally enforceable or commercially agreed corrective measure provided by a supplier to restore a dissatisfied customer to their rightful economic and psychological position."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The First Aid Analogy & 8 Redress Channels",
                    "content": {
                        "text": "Resolving a customer failure is like administering first aid after an accidental injury:\n\n- **The Band-Aid Analogy:** If you accidentally hurt someone, you do not ignore it. You apologize sincerely (Relational remedy), apply antiseptic and a band-aid (Repair/Replacement), and verify they heal fully (Follow-up).\n- **The 8 Main Remedies:**\n  1. **Repair:** Restoring a defective good to full working order at zero buyer cost.\n  2. **Replacement:** Exchanging defective merchandise for a brand-new identical item.\n  3. **Refund (Full / Partial):** Returning the cash paid when goods are permanently unusable.\n  4. **Financial Compensation:** Reimbursing secondary losses directly caused by defective goods.\n  5. **Rescission of Contract:** Cancelling the agreement and restoring both parties to original positions.\n  6. **Specific Performance:** A legal order forcing a service provider to complete unfinished work.\n  7. **Sincere Apology:** Courteous acknowledgement of error that de-escalates anger.\n  8. **Alternative Dispute Resolution (ADR):** Out-of-court mediation through neutral arbiters."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 8 Legal and Commercial Remedies for Consumer Redress",
                    "content": {
                        "title": "Comprehensive Taxonomy of Consumer Remedies and Redress Pathways",
                        "caption": "Vector diagram illustrating the 8 consumer remedies organized into 4 functional quadrants: Physical Goods Restoration, Financial Redress, Contractual Remedies, and Relational ADR.",
                        "svg_content": SVG_CONSUMER_REMEDIES_HIERARCHY
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "The 8 Consumer Remedies Application Matrix",
                    "content": {
                        "headers": ["Remedy", "Category", "Trigger Condition", "Practical Kenyan Example"],
                        "rows": [
                            ["Repair", "Physical Goods", "Minor, fixable component failure within warranty", "Fixing loose solar charge controller wire at zero labor charge"],
                            ["Replacement", "Physical Goods", "Major unfixable defect or dead-on-arrival unit", "Swapping a factory-cracked solar battery for a new sealed box"],
                            ["Full / Partial Refund", "Financial Redress", "Product fundamentally useless or buyer retains minor flaw", "Refunding cash after supplying expired animal feed"],
                            ["Financial Compensation", "Financial Redress", "Defect caused provable secondary physical/financial damage", "Paying to replow farm after selling contaminated fake maize seeds"],
                            ["Rescission of Contract", "Contractual", "Total failure of consideration or fundamental breach", "Cancelling school water tanker contract after delivery of muddy water"],
                            ["Specific Performance", "Service-Based", "Incomplete, sub-standard artisan or contractor work", "Ordering painter to repaint unevenly coated classroom walls"],
                            ["Sincere Apology", "Relational", "Service delay, minor administrative mix-up, rude staff", "Manager writing a formal apology letter for delayed meal delivery"],
                            ["ADR Mediation", "Dispute Resolution", "Deadlock between buyer and vendor without going to court", "Village chief or Trade Association mediating solar panel dispute"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Contract Rescission and Consequential Redress Compensation",
                    "content": {
                        "intro": "'Baraka Agrovet' in Eldoret sells certified seed maize to farmer Kiprono for $P_{\\text{seed}} = \\text{KES } 12,000$. Kiprono incurs land preparation costs of $C_{\\text{land}} = \\text{KES } 8,000$ and fertilizer application costs of $C_{\\text{fert}} = \\text{KES } 6,000$. Because the seed was secretly contaminated with dead grain, the entire 2-acre plot fails to germinate. Under Kenyan consumer protection principles, the agrovet is liable for full contract rescission (complete seed refund) plus consequential financial compensation for the wasted input costs. Calculate the direct refund, the consequential compensation, and the total redress payout owed to Kiprono.",
                        "steps": [
                            "**Step 1: Given Information:** Defective seed purchase price $P_{\\text{seed}} = \\text{KES } 12,000$. Land preparation labor cost $C_{\\text{land}} = \\text{KES } 8,000$. Planting fertilizer cost $C_{\\text{fert}} = \\text{KES } 6,000$.",
                            "**Step 2: Formulas & Legal Redress Rules:**\n$$\\text{Direct Refund (Rescission)} = P_{\\text{seed}}$$\n$$\\text{Consequential Compensation} = C_{\\text{land}} + C_{\\text{fert}}$$\n$$\\text{Total Redress Payout} = \\text{Direct Refund} + \\text{Consequential Compensation}$$",
                            "**Step 3: Substitution:**\n$$\\text{Direct Refund} = \\text{KES } 12,000$$\n$$\\text{Consequential Compensation} = \\text{KES } 8,000 + \\text{KES } 6,000 = \\text{KES } 14,000$$\n$$\\text{Total Redress Payout} = \\text{KES } 12,000 + \\text{KES } 14,000$$",
                            "**Step 4: Calculation:**\n$$\\text{Direct Refund} = \\text{KES } 12,000$$\n$$\\text{Consequential Compensation} = \\text{KES } 14,000$$\n$$\\text{Total Redress Payout} = \\text{KES } 26,000$$",
                            "**Step 5: Final Answer & Unit:** Baraka Agrovet is legally required to pay Kiprono a direct refund of $\\text{KES } 12,000$ and consequential compensation of $\\text{KES } 14,000$, resulting in a total redress settlement of $\\text{KES } 26,000$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Direct refunds restore only the initial cash outlay, whereas consequential compensation covers secondary losses directly caused by defective products. *Common Pitfall:* Assuming seller liability ends at refunding the seed price when the defective good ruined further investments."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Solar Lighting Redress in Homabay County",
                    "content": {
                        "title": "Juma's Solar Lighting Dispute Resolution in Western Kenya",
                        "text": "Juma, a smallholder farmer in Homabay County, purchased a KES 12,000 home solar lighting kit from a local hardware store so his children could study at night. On day three, the battery unit failed to hold charge. Rather than disputing the claim or turning Juma away, the hardware proprietor promptly tested the battery on an in-shop multimeter, identified a dead internal cell, issued a sincere apology, and immediately handed Juma a brand-new sealed battery unit (Replacement). This professional remedy restored Juma's trust, leading him to purchase a solar water pump from the same store two months later."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Consumer Rights, Remedies, and Redress Mechanisms",
                    "content": {
                        "title": "Understanding Consumer Remedies, Repairs, Refunds, and ADR",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Educational guide on commercial remedies for dissatisfied consumers, covering repair, replacement, rescission, compensation, and out-of-court dispute resolution."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: School Water Supply Redress Selection",
                    "content": {
                        "question": "A boarding school orders 10,000 litres of clean drinking water for KES 8,000 from a water tanker company. Upon delivery into the school storage tank, the water is found to be muddy, smelly, and contaminated with river silt. What is the most legally sound and complete remedy the school should demand?",
                        "options": [
                            "Accept a simple written apology and keep the muddy water for cooking",
                            "Demand contract rescission: full KES 8,000 refund, pumping out of dirty water, and compensation for the cost of tank sanitization",
                            "Pay an extra KES 2,000 bonus to encourage cleaner delivery next time",
                            "Request a 10% discount on their next water delivery in 6 months"
                        ],
                        "correct": "B",
                        "explanation": "Because the delivered water is fundamentally unfit for human consumption, the school is entitled to complete contract rescission (full refund) plus consequential compensation to clean the contaminated infrastructure."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Specific Performance vs. Rescission",
                    "content": {
                        "question": "A tailor agrees to sew 50 school graduation gowns but delivers them with unhemmed sleeves and missing buttons two days before the ceremony. If the school principal insists that the tailor work overnight to finish all sleeves and attach buttons properly, what remedy is being applied?",
                        "options": [
                            "Rescission of contract",
                            "Specific performance",
                            "Full cash refund without returning garments",
                            "Alternative Dispute Resolution mediation"
                        ],
                        "correct": "B",
                        "explanation": "Specific performance is a remedy that compels a defaulting party to complete their agreed contractual obligations exactly as originally promised."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Role of Remedies:** Remedies provide justice, protect consumer rights, and restore confidence in commercial markets.\n2. **Goods Redress:** Physical product failures are corrected through free repair, replacement with new units, or full/partial cash refunds.\n3. **Services & Contracts:** Service failures trigger specific performance or total contract rescission.\n4. **Consequential Losses:** Defective products that cause secondary destruction require financial compensation beyond the original purchase price."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Customer Satisfaction Survey Design
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Customer Satisfaction Survey Design",
        "unit_description": "Principles of customer feedback measurement: population vs sample, Likert rating scale construction, closed vs open-ended question design, and elimination of survey bias.",
        "lesson_title": "Customer Satisfaction Survey Design",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Secondary School Students in Kenya Participating in Learning",
                    "content": {
                        "title": "Student Research and Survey Feedback in Kenyan Schools",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/06/Students_at_Shimo_la_Tewa_Secondary_School.jpg",
                        "caption": "Secondary school students engaging in collaborative evaluation, illustrating the collection of structured survey feedback to improve canteen and enterprise services.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a customer satisfaction survey and its role in objective decision-making\n- Differentiate between a target population and a representative sample\n- Structure balanced 5-point Likert rating scales for quantitative customer feedback\n- Formulate unbiased closed-ended and open-ended questions while avoiding leading bias"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Customer Satisfaction Survey and Likert Scale",
                    "content": {
                        "term": "Customer Satisfaction Survey",
                        "definition": "A structured market research instrument consisting of standardized questions administered to a sample of consumers to gather quantitative and qualitative data on service satisfaction."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Thermometer Analogy & Survey Terminology",
                    "content": {
                        "text": "Surveys convert subjective, silent feelings into objective, actionable data:\n\n- **The Clinical Thermometer Analogy:** A doctor does not guess whether a patient has a fever by looking at them; they use a thermometer to obtain an exact numerical temperature reading. A survey is an enterprise's diagnostic thermometer.\n- **Core Survey Terminology:**\n  - **Population ($N$):** The total universe of customers (e.g., all 800 students in a secondary school).\n  - **Sample ($n$):** A representative subset selected to give feedback without surveying every single individual.\n  - **Likert Scale:** A 5-point rating spectrum (1 = Very Dissatisfied, 2 = Dissatisfied, 3 = Neutral, 4 = Satisfied, 5 = Very Satisfied).\n  - **Survey Bias:** Flawed question design that nudges respondents toward a specific answer (e.g., *'Don't you agree that our snacks are delicious?'* is biased)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Customer Satisfaction Survey Architecture and Likert Scaling",
                    "content": {
                        "title": "Survey Design Architecture, Sampling Principles, and Bias Elimination",
                        "caption": "Vector diagram detailing the sampling pipeline (Population vs Sample), the balanced 5-point Likert rating spectrum, and comparison between biased and neutral questionnaire phrasing.",
                        "svg_content": SVG_SURVEY_DESIGN_ARCHITECTURE
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Closed-Ended vs. Open-Ended Survey Questions Matrix",
                    "content": {
                        "headers": ["Dimension", "Closed-Ended Questions (Likert / Multiple Choice)", "Open-Ended Questions (Free Text Feedback)", "Questionnaire Design Rule"],
                        "rows": [
                            ["Structure", "Predetermined choices (e.g., scale 1 to 5, Yes/No)", "Blank lines allowing respondents to write freely in own words", "Use 80% closed questions and 20% open questions"],
                            ["Data Output", "Quantitative numbers, tallies, and exact percentages", "Qualitative suggestions, emotional insights, complaints", "Closed questions provide statistics; open questions reveal root causes"],
                            ["Analysis Speed", "Fast; easily computed using formulas and charts", "Requires reading, categorizing, and qualitative summary", "Keep total survey length to 4-6 concise questions"],
                            ["Tuck Shop Example", "'Rate freshness of snacks: [1] [2] [3] [4] [5]'", "'What new healthy snack should we add next term?'", "Never ask leading questions that pressure respondents"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Stratified Sample Sizes for a School Canteen Survey",
                    "content": {
                        "intro": "'Kivali Secondary School' has a total student population of $N = 800$ students distributed across four academic forms: Form 1 ($N_1 = 220$), Form 2 ($N_2 = 200$), Form 3 ($N_3 = 190$), and Form 4 ($N_4 = 190$). The student canteen committee decides to draw a representative stratified sample of $n = 80$ students proportionate to each class population. Calculate the overall Sampling Fraction ($f$), and determine the exact number of questionnaires to distribute to Form 1 students ($n_1$) and Form 4 students ($n_4$).",
                        "steps": [
                            "**Step 1: Given Information:** Total school population $N = 800$. Target sample size $n = 80$. Form 1 population $N_1 = 220$. Form 4 population $N_4 = 190$.",
                            "**Step 2: Formulas & Sampling Rules:**\n$$\\text{Sampling Fraction } (f) = \\frac{n}{N}$$\n$$\\text{Stratified Sub-Sample for Group } i \\ (n_i) = N_i \\times f = N_i \\times \\left(\\frac{n}{N}\\right)$$",
                            "**Step 3: Substitution:**\n$$f = \\frac{80}{800}$$\n$$n_1 = 220 \\times \\left(\\frac{80}{800}\\right)$$\n$$n_4 = 190 \\times \\left(\\frac{80}{800}\\right)$$",
                            "**Step 4: Calculation:**\n$$f = 0.10\\text{ (or } 10\\%\\text{)}$$\n$$n_1 = 220 \\times 0.10 = 22\\text{ students}$$\n$$n_4 = 190 \\times 0.10 = 19\\text{ students}$$",
                            "**Step 5: Final Answer & Unit:** The sampling fraction is $10\\%$ ($0.10$). The canteen committee must administer exactly $22$ questionnaires to Form 1 and $19$ questionnaires to Form 4.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Proportionate stratified sampling ensures every class group is fairly represented without skewing feedback. *Common Pitfall:* Using convenience sampling (e.g., surveying only close friends in one class), which produces biased, unrepresentative survey results."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Kivali School Tuck Shop Survey Design",
                    "content": {
                        "title": "Designing a 5-Question Survey for Student Tuck Shop Operations in Machakos",
                        "text": "The student business club running the 'Kivali School Tuck Shop' in Machakos designed a concise 1-page paper survey before investing KES 10,000 in a new snack inventory. They formulated 4 closed-ended Likert questions assessing snack freshness, attendant politeness, break-time service speed, and notebook pricing, followed by 1 open-ended suggestion prompt ('What single snack would you like added?'). By administering this unbiased questionnaire to 50 students across all forms during break, they obtained accurate, representative data without disrupting classroom learning."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Designing Professional Customer Satisfaction Surveys and Questionnaires",
                    "content": {
                        "title": "Survey Design, Sampling Methods, and Likert Rating Scales",
                        "youtube_id": "qJ7v37s9yHk",
                        "url": "https://www.youtube.com/watch?v=qJ7v37s9yHk",
                        "description": "Step-by-step guide to questionnaire construction, Likert scale design, sample selection, and eliminating question bias in customer satisfaction research."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Survey Bias and Leading Phrasing",
                    "content": {
                        "question": "Which of the following questions is considered 'biased' and should be strictly avoided when drafting a professional customer satisfaction survey?",
                        "options": [
                            "Please rate the speed of our checkout counter on a scale of 1 to 5.",
                            "How satisfied are you with the freshness of our baked bread?",
                            "Don't you agree that our restaurant offers far superior food than other dirty kiosks in town?",
                            "What improvements would you suggest for our school tuck shop menu?"
                        ],
                        "correct": "C",
                        "explanation": "Starting with 'Don't you agree that...' actively pushes the respondent to agree and uses derogatory language against competitors, invalidating the objectivity of the research."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Optimal Use of Closed-Ended vs. Open-Ended Questions",
                    "content": {
                        "question": "Why should a customer satisfaction survey rely primarily on closed-ended Likert scale questions accompanied by a single open-ended question?",
                        "options": [
                            "Closed questions allow fast statistical calculation of percentages, while the open question captures unique, unprompted customer suggestions",
                            "Open-ended questions are illegal under Kenyan education curriculum guidelines",
                            "Closed questions guarantee that 100% of respondents give a 5-star rating",
                            "Open questions cannot be answered by secondary school students"
                        ],
                        "correct": "A",
                        "explanation": "Closed Likert questions generate quantifiable data for statistical analysis, while open-ended prompts provide rich qualitative context and unexpected customer ideas."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Objective Measurement:** Customer surveys convert silent consumer feelings into clear, quantifiable data.\n2. **Representative Sampling:** A well-chosen sample accurately reflects the larger population without surveying every individual.\n3. **Balanced Likert Scaling:** Using symmetric 1-to-5 scales (Very Dissatisfied to Very Satisfied) ensures fair sentiment measurement.\n4. **Neutral Phrasing:** Unbiased questions without leading prompts are essential to obtain honest, actionable feedback."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Conducting and Presenting the Survey
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Conducting and Presenting the Survey",
        "unit_description": "Data processing methodology: raw questionnaire tabulation, tally charts, frequency distribution tables, percentage calculations, visual dashboard construction, and business interpretation.",
        "lesson_title": "Conducting and Presenting the Survey",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Analyzing Financial and Survey Data in Kenya",
                    "content": {
                        "title": "Data Tabulation and Analysis in Business Administration",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
                        "caption": "Business analysts tabulating raw responses into structured frequency tables and calculating satisfaction percentages for management review.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Tabulate raw survey response forms into structured tally charts and frequency distribution tables\n- Calculate exact category percentages and compute the Net Satisfaction Score (NSS)\n- Construct visual representations (pie charts, bar graphs, summary tables) for business managers\n- Interpret quantitative survey findings to make evidence-based operational decisions"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Data Tabulation and Frequency Distribution",
                    "content": {
                        "term": "Data Tabulation",
                        "definition": "The systematic process of organizing raw, unformatted survey responses into orderly rows and columns of tally marks, frequencies, and percentages to enable statistical analysis."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Sorting Harvested Oranges & The Survey Pipeline",
                    "content": {
                        "text": "Converting raw forms into management insights follows an orderly pipeline:\n\n- **Sorting Harvested Oranges Analogy:** You cannot sell a messy heap of mixed oranges. You sort them into three boxes: Grade A (Large/Sweet), Grade B (Medium), and Grade C (Small/Sour). Counting oranges in each box allows you to tell buyers: *'70% of my crop is top-grade!'*\n- **The Survey Data Pipeline:**\n  1. **Raw Paper Forms:** Collect the completed questionnaires.\n  2. **Tallying:** Group responses into 5-mark bundles (||||).\n  3. **Frequency Table:** Count total tally counts ($f$) for each category.\n  4. **Percentage Calculation:** Divide category frequency by sample size ($N$) and multiply by 100.\n  5. **Visual Dashboard:** Display findings using pie charts and bar graphs for executive clarity."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Survey Data Tabulation, Percentage Calculation, and Visual Presentation",
                    "content": {
                        "title": "Survey Data Tabulation Pipeline, Formula Breakdown, and Dashboard Visuals",
                        "caption": "Vector diagram illustrating the conversion of raw tally marks into frequency distribution tables, KaTeX percentage calculations, and a pie/bar chart dashboard.",
                        "svg_content": SVG_SURVEY_TABULATION_AND_VISUALIZATION
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Master Survey Tabulation and Presentation Table (Sample N = 50)",
                    "content": {
                        "headers": ["Rating Category (Likert)", "Tally Marks", "Frequency (f)", "Percentage (%)", "Business Management Action"],
                        "rows": [
                            ["Satisfied / Very Satisfied (4 & 5)", "|||| |||| |||| |||| |||| |||| ||||", "35", "70.0%", "Maintain current supplier; quality and freshness meet high standard"],
                            ["Neutral (Rating 3)", "|||| ||||", "10", "20.0%", "Monitor closely; introduce minor flavor variations to win delight"],
                            ["Dissatisfied / Very Dissat. (1 & 2)", "||||", "5", "10.0%", "Investigate specific complaints regarding packaging or shelf storage"],
                            ["Total Sample Size (N)", "50 Tally Marks", "50", "100.0%", "Net Satisfaction Score (NSS) = 70% - 10% = +60.0% (Excellent)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Multi-Category Satisfaction Percentage & Net Satisfaction Score Calculation",
                    "content": {
                        "intro": "The student committee at 'Kivali Tuck Shop' administers a service speed survey to a sample of $N = 80$ students during 10:00 AM break. The raw questionnaire count reveals: Very Satisfied $= 16$, Satisfied $= 24$, Neutral $= 16$, Dissatisfied $= 16$, and Very Dissatisfied $= 8$. Calculate the Total Satisfied Percentage (\\%S), the Total Dissatisfied Percentage (\\%D), the Neutral Percentage (\\%N), and the Net Satisfaction Score ($\\text{NSS} = \\%S - \\%D$).",
                        "steps": [
                            "**Step 1: Given Information:** Total sample size $N = 80$ students. Satisfied frequency $f_S = 16 + 24 = 40$. Neutral frequency $f_N = 16$. Dissatisfied frequency $f_D = 16 + 8 = 24$.",
                            "**Step 2: Formulas & Statistical Rules:**\n$$\\%S = \\left(\\frac{f_S}{N}\\right) \\times 100$$\n$$\\%N = \\left(\\frac{f_N}{N}\\right) \\times 100$$\n$$\\%D = \\left(\\frac{f_D}{N}\\right) \\times 100$$\n$$\\text{Net Satisfaction Score (NSS)} = \\%S - \\%D$$",
                            "**Step 3: Substitution:**\n$$\\%S = \\left(\\frac{40}{80}\\right) \\times 100$$\n$$\\%N = \\left(\\frac{16}{80}\\right) \\times 100$$\n$$\\%D = \\left(\\frac{24}{80}\\right) \\times 100$$\n$$\\text{NSS} = 50.0\\% - 30.0\\%$$",
                            "**Step 4: Calculation:**\n$$\\%S = 0.50 \\times 100 = 50.0\\%$$\n$$\\%N = 0.20 \\times 100 = 20.0\\%$$\n$$\\%D = 0.30 \\times 100 = 30.0\\%$$\n$$\\text{NSS} = +20.0\\%$$",
                            "**Step 5: Final Answer & Unit:** Satisfied percentage is $50.0\\%$, Neutral is $20.0\\%$, and Dissatisfied is $30.0\\%$. The Net Satisfaction Score (NSS) is $+20.0\\%$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** A 30% dissatisfaction rate regarding speed is alarming for a school canteen where break time is limited. Immediate queue management is required. *Common Pitfall:* Forgetting to verify that total percentages sum to exactly $100\\%$ ($50\\% + 20\\% + 30\\% = 100\\%$)."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Presenting Canteen Survey Results in Machakos",
                    "content": {
                        "title": "Translating Tuck Shop Survey Data into a School Board Presentation",
                        "text": "The student tuck shop committee in Machakos compiled their 50-student survey results into a color-coded presentation for the School Board of Management. By presenting a pie chart showing 70% satisfaction in snack freshness alongside a bar chart showing a 40% dissatisfaction in service speed, the students secured administrative approval to install a second serving counter. This demonstrated how professional data presentation persuades stakeholders to fund operational upgrades."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Tabulating Survey Data, Frequency Distributions, and Calculating Percentages",
                    "content": {
                        "title": "Survey Data Tabulation, Percentages, and Visual Presentations",
                        "youtube_id": "X1Lp4mU4SjY",
                        "url": "https://www.youtube.com/watch?v=X1Lp4mU4SjY",
                        "description": "Practical tutorial on organizing survey responses, tallying frequencies, calculating category percentages, and presenting data using charts."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Calculating Percentage from Raw Frequencies",
                    "content": {
                        "question": "A school uniform supplier surveys 200 parents on uniform stitching quality. If 150 parents rate the quality as 'Satisfied', 30 as 'Neutral', and 20 as 'Dissatisfied', what is the exact percentage of satisfied parents?",
                        "options": [
                            "60%",
                            "75%",
                            "15%",
                            "80%"
                        ],
                        "correct": "B",
                        "explanation": "Percentage = (150 / 200) * 100 = 0.75 * 100 = 75%. Therefore, 75% of parents are satisfied with the uniform stitching."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Purpose of Visualizing Survey Data in Charts",
                    "content": {
                        "question": "Why do business executives convert tabulated survey numbers into visual pie charts and bar graphs before making investment decisions?",
                        "options": [
                            "Charts hide dissatisfied customer complaints from tax inspectors",
                            "Visual charts allow instant comparison of proportions, highlighting major operational strengths and urgent pain points at a glance",
                            "Pie charts are mandatory under Kenya Revenue Authority filing rules",
                            "Charts eliminate the need to collect questionnaires from consumers"
                        ],
                        "correct": "B",
                        "explanation": "Visual charts translate complex numeric tables into intuitive graphics that immediately illuminate key patterns, such as dominant customer satisfaction or alarming dissatisfaction bottlenecks."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 6 Summary Takeaways",
                    "content": {
                        "text": "1. **Data Tabulation:** Raw questionnaire markings must be organized into structured tally charts and frequency tables.\n2. **Percentage Calculation:** Divide category frequency by total sample size and multiply by 100 to determine proportions.\n3. **Summation Check:** Ensure all category percentages sum to exactly 100% to guarantee mathematical accuracy.\n4. **Visual Dashboard:** Clear pie and bar charts communicate operational findings effectively to management stakeholders."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7: Using Feedback for Service Improvement
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Using Feedback for Service Improvement",
        "unit_description": "Closing the customer feedback loop: the 5-stage continuous improvement cycle, prioritizing pain points, implementing operational adjustments, and conducting post-intervention re-surveys.",
        "lesson_title": "Using Feedback for Service Improvement",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Micro-Enterprise Retail and Customer Agility in Kenya",
                    "content": {
                        "title": "Operational Adaptation in Kenyan Retail Commerce",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Banana_Street_Vendor_Kenya.jpg",
                        "caption": "A small independent merchant adapting stock and service speed based on direct customer feedback, showcasing practical operational responsiveness.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the concept and strategic value of 'Closing the Customer Feedback Loop'\n- Outline the 5 sequential stages of the Continuous Service Improvement Cycle\n- Formulate cost-effective, actionable operational adjustments from survey data\n- Measure post-intervention service improvement and calculate the rate of dissatisfaction reduction"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Closed Feedback Loop and Continuous Service Improvement",
                    "content": {
                        "term": "Closed Feedback Loop",
                        "definition": "The circular managerial practice of collecting customer feedback, diagnosing root causes, implementing targeted operational changes, and re-surveying customers to confirm service resolution."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Water Thermostat Analogy & The 5-Stage Engine",
                    "content": {
                        "text": "Collecting survey feedback without taking action is useless. Enterprises must operate like an automated thermostat:\n\n- **The Water Heater Thermostat Analogy:** A water heater constantly senses water temperature. When the water gets too cold (customer complaints), the thermostat activates the heating element (operational fixes). Once optimal temperature is reached (satisfaction), it stabilizes and continues monitoring.\n- **The 5-Stage Continuous Loop:**\n  1. **Collect Feedback:** Gather opinions via surveys, suggestion boxes, and digital reviews.\n  2. **Analyze & Prioritize:** Identify the single highest friction point (e.g., 40% queue delay).\n  3. **Develop Action Plan:** Design practical, affordable operational solutions.\n  4. **Implement Adjustments:** Execute changes (e.g., add second cash drawer, train staff).\n  5. **Monitor & Re-Survey:** Administer a follow-up survey after 30 days to measure improvement."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Continuous Service Improvement and Closed Feedback Loop Cycle",
                    "content": {
                        "title": "The 5-Stage Closed Feedback Engine and Thermostat Model of Operations",
                        "caption": "Vector diagram detailing the circular 5-stage feedback engine (Collect -> Analyze -> Implement -> Monitor -> Re-Survey) that drives systematic service quality enhancement.",
                        "svg_content": SVG_CONTINUOUS_FEEDBACK_LOOP_CYCLE
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Service Improvement Action Plan Matrix",
                    "content": {
                        "headers": ["Identified Pain Point", "Survey Metric Trigger", "Immediate Operational Fix", "Long-Term Commercial Impact"],
                        "rows": [
                            ["Break-Time Queue Delays", "40% Dissatisfaction on speed of service", "Open a second cash register; split snacks and stationery into separate lines", "Average waiting time drops from 12 mins to 3 mins; zero missed lessons"],
                            ["Mobile Money PIN Privacy", "60% Dissatisfaction on transaction privacy", "Install counter privacy shield; place keypad away from waiting crowd", "Restores consumer confidence; boosts high-value transaction volume"],
                            ["Bread / Snack Freshness", "25% Dissatisfaction on product staleness", "Switch to daily morning bakery deliveries; enforce 24-hr shelf-life rule", "Stale product waste falls to zero; repeat breakfast snack sales double"],
                            ["Rude Cashier Communication", "30% Complaints regarding staff attitude", "Conduct customer service training; implement polite greeting protocol", "Positive word-of-mouth recommendations surge; complaint volume drops by 85%"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Measuring Service Improvement and Rate of Dissatisfaction Reduction",
                    "content": {
                        "intro": "Before making operational changes, the 'Kivali Tuck Shop' surveyed $100$ students regarding service speed and found $40$ students dissatisfied ($D_{\\text{before}} = 40.0\\%$). The committee implemented a dual-queue system (Snacks vs. Stationery) and added a second cashier. In a follow-up survey of $100$ students one month later, only $8$ students reported dissatisfaction ($D_{\\text{after}} = 8.0\\%$). Calculate the Absolute Reduction in dissatisfaction (percentage points) and the Relative Percentage Rate of Improvement ($R_{\\text{imp}}$).",
                        "steps": [
                            "**Step 1: Given Information:** Pre-intervention dissatisfaction rate $D_{\\text{before}} = 40.0\\%$. Post-intervention dissatisfaction rate $D_{\\text{after}} = 8.0\\%$.",
                            "**Step 2: Formulas & Improvement Metrics:**\n$$\\text{Absolute Reduction (points)} = D_{\\text{before}} - D_{\\text{after}}$$\n$$\\text{Relative Rate of Improvement (\\%)} = \\left(\\frac{D_{\\text{before}} - D_{\\text{after}}}{D_{\\text{before}}}\\right) \\times 100$$",
                            "**Step 3: Substitution:**\n$$\\text{Absolute Reduction} = 40.0\\% - 8.0\\%$$\n$$\\text{Relative Improvement} = \\left(\\frac{40.0 - 8.0}{40.0}\\right) \\times 100$$",
                            "**Step 4: Calculation:**\n$$\\text{Absolute Reduction} = 32.0\\text{ percentage points}$$\n$$\\text{Relative Improvement} = \\left(\\frac{32.0}{40.0}\\right) \\times 100 = 0.80 \\times 100 = 80.0\\%$$",
                            "**Step 5: Final Answer & Unit:** Dissatisfaction dropped by $32.0$ percentage points, representing an outstanding $80.0\\%$ relative improvement in customer service satisfaction.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Closing the feedback loop with tangible operational adjustments dramatically slashed dissatisfaction from 40% to 8%. *Common Pitfall:* Confusing absolute drop (32 percentage points) with the relative rate of improvement (80%)."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Mobile Money Agency Queue and Privacy Solutions",
                    "content": {
                        "title": "Operational Privacy Upgrades in a Busy M-PESA Kiosk in Machakos",
                        "text": "An M-PESA agency in Machakos town received feedback that 60% of customers felt uncomfortable because attendants read transaction phone numbers and withdrawal amounts aloud in front of crowded queues. Rather than ignoring the complaints, the agency installed tinted acrylic privacy booths, placed numeric keypads within reach of customers to enter PINs privately, and instituted a silent verification display screen. Within 30 days, high-value deposit transactions increased by 45% because customers felt secure and respected."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Closing the Customer Feedback Loop and Continuous Service Improvement",
                    "content": {
                        "title": "Service Improvement Strategies and Closed Feedback Loops",
                        "youtube_id": "sVKQn2v8KYQ",
                        "url": "https://www.youtube.com/watch?v=sVKQn2v8KYQ",
                        "description": "Educational guide on transforming survey data into actionable operational workflows, de-bottlenecking service queues, and verifying customer recovery."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Actionable Response to Survey Findings",
                    "content": {
                        "question": "A survey of a school canteen reveals that 45% of students are dissatisfied with long waiting times during the 15-minute morning break. What is the most immediate, cost-effective operational adjustment the management should execute?",
                        "options": [
                            "Close the canteen permanently and tell students to fast during the school day",
                            "Pre-pack popular snack bundles before break and set up a separate express cash collection desk",
                            "Triple the price of all snacks to discourage students from buying food",
                            "Ignore the survey results because students will buy snacks regardless"
                        ],
                        "correct": "B",
                        "explanation": "Pre-packaging high-demand items and creating dedicated express queues directly eliminates the operational bottleneck, cutting transaction time without substantial capital cost."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Purpose of Re-Surveying Customers",
                    "content": {
                        "question": "Why is 'Stage 5: Monitoring and Re-Surveying' critical in the continuous customer feedback cycle?",
                        "options": [
                            "It allows the business to print more paper forms to spend surplus club funds",
                            "It verifies whether the implemented operational changes actually solved the problem and reduced dissatisfaction",
                            "It proves that the business no longer needs to provide good customer service",
                            "It transfers legal liability for future failures to the customers"
                        ],
                        "correct": "B",
                        "explanation": "Re-surveying closes the loop by providing empirical proof that the operational adjustments succeeded in improving customer satisfaction."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 7 Summary Takeaways",
                    "content": {
                        "text": "1. **Action-Oriented Feedback:** Survey data is worthless unless translated into concrete operational adjustments.\n2. **The 5-Step Loop:** Continuous improvement requires collecting, analyzing, planning, executing, and re-evaluating.\n3. **Targeting Friction:** Focus immediate resources on the single biggest customer pain point to achieve maximum satisfaction gains.\n4. **Empirical Verification:** Post-intervention surveys confirm whether service upgrades successfully reduced churn."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8: Satisfaction and Business Sustainability
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Satisfaction and Business Sustainability",
        "unit_description": "The strategic link connecting consumer satisfaction to customer retention, brand equity capital, resilience during economic price wars, stable compounding revenues, and long-term enterprise longevity.",
        "lesson_title": "Satisfaction and Business Sustainability",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Sustainable Commercial Banking and Mobile Agency in Nairobi",
                    "content": {
                        "title": "Inclusive Banking and Enterprise Sustainability in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/M-PESA_mobile_money_and_Equity_agent%2C_Nairobi%2C_Kenya.jpg",
                        "caption": "A bustling financial services agent in Nairobi, demonstrating how consumer satisfaction and accessibility build enduring enterprise sustainability.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Analyze how consumer satisfaction directly drives long-term commercial sustainability\n- Trace the financial chain from customer satisfaction to high retention, recurring cash flows, and brand equity\n- Explain how customer loyalty acts as an economic buffer during price wars and recessions\n- Calculate the compounding profit advantages of low customer churn over multi-year periods"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Business Sustainability and Brand Equity",
                    "content": {
                        "term": "Business Sustainability",
                        "definition": "The capacity of an enterprise to generate stable, long-term profits, withstand economic shocks, and maintain enduring customer relationships over generations."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Avocado Tree Root Analogy & Sustainability Chain",
                    "content": {
                        "text": "Consumer satisfaction is the invisible anchor that secures an enterprise against market storms:\n\n- **The Avocado Tree Root Analogy:** Visible branches, leaves, and fruits represent current sales and quarterly profits. However, during harsh droughts or seasonal windstorms, the tree survives only because of its deep, sturdy root system anchored in the soil. In business, customer satisfaction is the deep root system. Without it, a shallow business withers at the first sign of competition.\n- **The 4-Link Value Chain:**\n  1. **Exceeded Expectations:** Consistently high quality and respectful service.\n  2. **High Customer Retention:** Loyal buyers return automatically without paid ads.\n  3. **Compounding Cash Flows:** Predictable recurring revenues fund bulk discounts and expansion.\n  4. **Brand Equity & Resilience:** Enduring goodwill shields the firm during price wars and recessions."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Customer Satisfaction to Long-Term Business Sustainability Chain",
                    "content": {
                        "title": "The Compounding Sustainability Chain and Enterprise Root System Metaphor",
                        "caption": "Vector diagram illustrating the 4-link compounding sustainability chain (Satisfaction -> Retention -> Compounding Revenue -> Brand Resilience) alongside the avocado tree root metaphor.",
                        "svg_content": SVG_SATISFACTION_TO_SUSTAINABILITY_CHAIN
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Short-Term Transactional vs. Long-Term Customer-Centric Enterprise Matrix",
                    "content": {
                        "headers": ["Operating Dimension", "Transactional Focus (Short-Term)", "Customer-Centric Focus (Sustainable)", "Long-Term Commercial Impact"],
                        "rows": [
                            ["Primary Objective", "Maximize immediate one-time sale profit", "Maximize Customer Lifetime Value (CLTV) and trust", "Sustainable firms achieve compounding multi-year revenue"],
                            ["Customer Service", "Viewed as an annoying operational cost to minimize", "Viewed as a high-return capital investment", "Customer-centric firms enjoy 5x lower acquisition marketing costs"],
                            ["Response to Defect", "Argues with buyer; cites 'No Return' receipt fine print", "Issues sincere apology, instant repair or replacement", "Builds deep brand advocacy and customer forgiveness"],
                            ["Resilience to Price War", "Vulnerable; customers immediately defect to cheaper rival", "Strong buffer; loyal customers value trusted service", "Withstands inflation, supply disruptions, and economic shocks"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Compounding 5-Year Profit Impact of Customer Retention vs. Churn",
                    "content": {
                        "intro": "'Baraka Grain Millers' in Nakuru serves $N = 1,000$ retail posho mill customers. Each active customer generates an average annual gross profit of $P = \\text{KES } 5,000$. The cost to acquire a replacement customer through marketing is $C_A = \\text{KES } 3,000$.\n- **Strategy A (Low Satisfaction / High Churn):** Churns $20\\%$ of its customer base annually ($L_A = 200\\text{ customers}$) and must replace them.\n- **Strategy B (High Satisfaction / Low Churn):** Churns only $2\\%$ of its customer base annually ($L_B = 20\\text{ customers}$) due to superior service.\nCalculate the annual customer acquisition cost for both strategies, the annual cost savings achieved by Strategy B, and the cumulative 5-year profit advantage generated by high customer satisfaction.",
                        "steps": [
                            "**Step 1: Given Information:** Customer base $N = 1,000$. Annual profit per customer $P = \\text{KES } 5,000$. Replacement acquisition cost $C_A = \\text{KES } 3,000$. Annual lost customers in Strategy A $L_A = 200$. Annual lost customers in Strategy B $L_B = 20$. Timeframe $T = 5\\text{ years}$.",
                            "**Step 2: Formulas & Economic Rules:**\n$$\\text{Annual Acquisition Cost (A)} = L_A \\times C_A$$\n$$\\text{Annual Acquisition Cost (B)} = L_B \\times C_A$$\n$$\\text{Annual Cost Savings} = \\text{Cost}_A - \\text{Cost}_B$$\n$$\\text{Cumulative 5-Year Profit Advantage} = \\text{Annual Cost Savings} \\times T$$",
                            "**Step 3: Substitution:**\n$$\\text{Cost}_A = 200 \\times \\text{KES } 3,000$$\n$$\\text{Cost}_B = 20 \\times \\text{KES } 3,000$$\n$$\\text{Annual Savings} = (200 \\times \\text{KES } 3,000) - (20 \\times \\text{KES } 3,000)$$\n$$\\text{5-Year Advantage} = \\text{Annual Savings} \\times 5$$",
                            "**Step 4: Calculation:**\n$$\\text{Cost}_A = \\text{KES } 600,000$$\n$$\\text{Cost}_B = \\text{KES } 60,000$$\n$$\\text{Annual Savings} = \\text{KES } 600,000 - \\text{KES } 60,000 = \\text{KES } 540,000$$\n$$\\text{5-Year Advantage} = \\text{KES } 540,000 \\times 5 = \\text{KES } 2,700,000$$",
                            "**Step 5: Final Answer & Unit:** Strategy A incurs an annual replacement cost of $\\text{KES } 600,000$, while Strategy B incurs only $\\text{KES } 60,000$. High customer satisfaction saves $\\text{KES } 540,000$ annually, generating a massive $\\text{KES } 2,700,000$ cumulative profit advantage over 5 years.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Minimizing customer churn through high satisfaction directly preserves $2.7$ million shillings in profit over 5 years. *Common Pitfall:* Viewing customer satisfaction programs as unnecessary expenses rather than wealth-preserving capital investments."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Equity Bank's Customer-Centric Transformation",
                    "content": {
                        "title": "Building Long-Term Banking Sustainability through Customer Dignity",
                        "text": "In the early 1990s, commercial banking in Kenya was exclusive, imposing high minimum ledger balances, strict dress codes, and punitive account maintenance fees that locked out ordinary smallholder farmers and micro-traders. Equity Building Society (now Equity Bank) transformed this model by eliminating minimum balances, welcoming ordinary rural citizens warmly, deploying mobile solar banking vans to remote weekly markets, and treating every customer with dignity. This generated intense consumer satisfaction and passionate loyalty. As rural farmers prospered, their repeat banking business turned Equity Bank into one of the largest, most sustainable financial institutions in East and Central Africa."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "How Customer Satisfaction and Brand Equity Drive Long-Term Enterprise Sustainability",
                    "content": {
                        "title": "Customer Satisfaction, Retention, and Sustainable Business Growth",
                        "youtube_id": "0h6bXgW8VqM",
                        "url": "https://www.youtube.com/watch?v=0h6bXgW8VqM",
                        "description": "Comprehensive analysis of how customer satisfaction builds brand equity, buffers against market shocks, and secures long-term enterprise sustainability."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Insulating Against Price Wars",
                    "content": {
                        "question": "How does maintaining an exceptionally high customer satisfaction score protect an established business when an aggressive new competitor opens across the street offering cheaper prices?",
                        "options": [
                            "It forces the County Government to revoke the new competitor's business license",
                            "Satisfied customers value the trusted service, reliability, and respect of the established brand and are less likely to defect for small price differences",
                            "It automatically doubles the profit margin on all existing inventory",
                            "It eliminates the business's obligation to pay supplier debts"
                        ],
                        "correct": "B",
                        "explanation": "Customer loyalty built on trust and consistent satisfaction creates price resilience. Consumers recognize that cut-price competitors often deliver inferior quality and poor service."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Customer Satisfaction as Enterprise Capital",
                    "content": {
                        "question": "Why is the goodwill generated by customer satisfaction considered an 'invisible economic buffer' during sudden national economic recessions?",
                        "options": [
                            "Commercial banks accept customer smiles as physical cash loan repayments",
                            "Loyal customers prioritize essential purchases with businesses they trust and forgive occasional minor disruptions due to past positive experiences",
                            "Satisfied customers are legally prohibited from reducing household spending",
                            "It exempts the enterprise from paying Value Added Tax (VAT)"
                        ],
                        "correct": "B",
                        "explanation": "During economic downturns, consumers restrict spending to trusted vendors who have demonstrated consistent fairness and quality, giving customer-centric businesses a vital survival buffer."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 8 Summary Takeaways",
                    "content": {
                        "text": "1. **Core of Sustainability:** Customer satisfaction is not an optional marketing tactic; it is the foundation of long-term business survival.\n2. **Financial Multiplication:** Low customer churn eliminates wasteful acquisition costs, compounding enterprise profits over time.\n3. **Price War Resilience:** Deep customer trust shields enterprises against competitors attempting to undercut prices.\n4. **Enduring Brand Equity:** Businesses that consistently delight consumers construct an enduring asset that survives economic cycles."
                    }
                }
            ]
        ]
    }
]
