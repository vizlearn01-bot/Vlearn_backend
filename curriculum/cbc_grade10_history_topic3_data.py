"""
VLearn CBC Grade 10 History — Topic 3: The Constitution of Kenya (2010) — Public Resources
Comprehensive Pedagogical Data Definitions (Lessons 1 to 4)
"""

from curriculum.cbc_grade10_history_topic3_svgs import (
    SVG_TIMELINE_RESOURCE_GOVERNANCE,
    SVG_THREE_PILLARS_RESOURCES,
    SVG_CAUSAL_CHAIN_RESOURCE_WASTE,
    SVG_SUSTAINABILITY_LOOP,
    SVG_MALI_YA_UMMA_POSTER,
    SVG_CONSTITUTIONAL_INQUIRY_FRAMEWORK
)

TOPIC_3_LESSONS = [
    # =========================================================================
    # LESSON 1: Public Resources and Constitutional Stewardship
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Public Resources and Constitutional Stewardship",
        "unit_description": "Constitutional definition of public wealth, historical shift from centralized allocation to devolution, three pillars of public resources, Article 69/201 stewardship, and mining benefit sharing.",
        "lesson_title": "Public Resources and Constitutional Stewardship",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "National Public Architecture and Civic Heritage in Nairobi",
                    "content": {
                        "title": "Kenyatta International Convention Centre (KICC) and Public Assets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/KICC_Nairobi.jpg",
                        "caption": "The Kenyatta International Convention Centre (KICC) in Nairobi, a prominent national public asset symbolizing Kenya's collective sovereignty and shared public wealth.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Wealth of the Nation — What Belongs to Us?",
                    "content": {
                        "text": (
                            "Imagine walking into a public library or a neighborhood community park. "
                            "Who owns the books on the shelves? Who owns the playground equipment and park benches? "
                            "They do not belong to any single private individual; they belong to **all of us**. "
                            "These are shared assets, built and maintained using taxpayer money so that every citizen enjoys equal access.\n\n"
                            "In the exact same way, the entire Republic of Kenya possesses vast wealth that belongs collectively to its people. "
                            "From the fertile agricultural soils of the Rift Valley to the mineral deposits in Kwale and Turkana, "
                            "the fresh water flowing through our rivers, and the tax revenues collected from businesses—these are **public resources** (*Mali ya Umma*).\n\n"
                            "Under the **Constitution of Kenya (2010)**, the government does not 'own' these resources as private property. "
                            "Instead, the state acts strictly as a **trustee** or **steward**, legally mandated to manage this common wealth "
                            "with utmost integrity on behalf of every Kenyan citizen, both present and future."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define the concept of **public resources** and explain the legal principle of **constitutional stewardship**\n"
                            "- Trace the historical transition of Kenyan resource governance from post-colonial centralization (1964) to Devolution (2010)\n"
                            "- Classify public wealth into the **Three Pillars**: Natural Resources, Financial Resources, and Public Assets\n"
                            "- Analyze **Article 69** and **Article 201** of the Constitution regarding equitable benefit sharing and public participation\n"
                            "- Apply the multi-stakeholder royalty formula in mineral extraction case studies (such as Kwale titanium mining)"
                        )
                    }
                }
            ],

            # Card 2: Historical Context (Centralization to Devolution)
            [
                {
                    "type": "concept_explanation",
                    "title": "From Centralization to Devolution: Why 2010 Was a Turning Point",
                    "content": {
                        "text": (
                            "Before the promulgation of the Constitution of Kenya on **August 27, 2010**, public resource management was intensely centralized. "
                            "For nearly five decades following independence in 1964, major decisions concerning where to build tarmac roads, locate national schools, "
                            "drill water boreholes, and allocate national revenues were made exclusively by the central executive in Nairobi.\n\n"
                            "This centralized framework—partly reinforced by historical policies such as **Sessional Paper No. 10 of 1965**—concentrated developmental "
                            "investments in high-potential agricultural and urban areas while leaving arid, semi-arid, and marginalized frontier regions severely underdeveloped.\n\n"
                            "The **Constitution of Kenya (2010)** revolutionized this architecture by establishing **Devolution**, creating **one national government** "
                            "and **47 county governments**. Crucially, it bound all state organs to strict principles of public finance, ensuring that public resources "
                            "are shared equitably to eradicate historical marginalization."
                        )
                    }
                },
                {
                    "type": "suggested_diagram",
                    "title": "Key Milestones in Kenyan Resource Governance (1964–2010)",
                    "content": {
                        "title": "Timeline of Resource Governance Evolution",
                        "caption": "Milestones illustrating the transition from post-independence centralized resource planning (1964/1965) through regional disparities to constitutional devolution and public trusteeship in 2010.",
                        "svg_content": SVG_TIMELINE_RESOURCE_GOVERNANCE
                    }
                }
            ],

            # Card 3: Core Knowledge (Classifying Public Wealth)
            [
                {
                    "type": "concept_explanation",
                    "title": "Classifying Our Public Wealth: Natural, Financial, and Public Assets",
                    "content": {
                        "text": (
                            "Under the Constitution, public resources are defined comprehensively to encompass all **revenues, physical assets, natural endowments, and liabilities** "
                            "of both national and county governments. They are systematically categorized into three foundational pillars:\n\n"
                            "1. **Natural Resources**: Inherited geographic and environmental wealth, including agricultural and trust lands, gazetted water towers (Mau Forest, Mt. Kenya), "
                            "rivers and lakes (River Tana, Lake Victoria), mineral and energy reserves (Turkana oil, Kwale titanium, Olkaria geothermal), and wildlife ecosystems.\n\n"
                            "2. **Financial Resources**: Liquid funds available for public service delivery, including tax revenues collected by the Kenya Revenue Authority (KRA), "
                            "sovereign loans, international development grants, and investment dividends earned from state-owned enterprises.\n\n"
                            "3. **Public Assets**: Physical infrastructure and institutional facilities built for public welfare, such as highways, bridges, the Standard Gauge Railway (SGR), "
                            "public universities, primary and secondary schools, and national referral hospitals (e.g., Kenyatta National Hospital)."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Three Pillars of Kenyan Public Wealth",
                    "content": {
                        "headers": ["Resource Pillar", "Constitutional Scope", "Key Kenyan Examples", "Primary Legal Custodian"],
                        "rows": [
                            ["Natural Resources", "Land, water basins, minerals, forests, and biodiversity", "Mau Forest, Turkana Oil, Lake Victoria, Maasai Mara Wildlife", "National Land Commission (NLC) & Ministry of Mining/Environment"],
                            ["Financial Resources", "Tax revenue, sovereign debt, grants, and parastatal profits", "Income Tax, VAT, World Bank development grants, Central Bank reserves", "National Treasury, KRA, and County Treasuries"],
                            ["Public Assets", "Built transport infrastructure, government buildings, public schools, and hospitals", "Standard Gauge Railway (SGR), Kenyatta National Hospital, KenGen dams, County Assembly halls", "National & County Ministries of Infrastructure, Education, and Health"]
                        ]
                    }
                },
                {
                    "type": "suggested_diagram",
                    "title": "Three Pillars of Kenyan Public Resources Architecture",
                    "content": {
                        "title": "Temple Architecture of Kenyan Public Resources",
                        "caption": "Vector diagram showing the three structural pillars—Natural Resources, Financial Resources, and Public Assets—supported by the constitutional bedrock of Article 201 and Article 69.",
                        "svg_content": SVG_THREE_PILLARS_RESOURCES
                    }
                }
            ],

            # Card 4: Critical Thinking / Principles of Stewardship
            [
                {
                    "type": "concept_explanation",
                    "title": "The Principle of Stewardship: Who is Accountable?",
                    "content": {
                        "text": (
                            "Under **Article 201** of the Constitution, public finance and resource management must strictly adhere to the principles of "
                            "**openness, accountability, and public participation**. \n\n"
                            "A public officer—whether a Cabinet Secretary, Governor, Member of Parliament, or civil servant—is not an owner of state property. "
                            "They are a **fiduciary steward**. Just as a bank manager cannot spend depositors' funds on personal luxury, a public officer cannot "
                            "divert public revenue or state assets for personal or partisan political gain.\n\n"
                            "To enforce this stewardship, the Constitution establishes robust independent oversight institutions:\n"
                            "- **The Controller of Budget (CoB)**: Authorizes and oversees all budget withdrawals, ensuring no public money leaves the exchequer without lawful parliamentary approval.\n"
                            "- **The Auditor-General**: Conducts annual physical and financial audits across all national and county government ministries, state corporations, and assemblies, reporting directly to Parliament.\n"
                            "- **The Sovereign Citizens**: Under Chapter One (Article 1), all sovereign power belongs to the people of Kenya, who exercise direct oversight through public participation."
                        )
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Checking Constitutional Principles: Owner vs. Trustee",
                    "content": {
                        "intro": "Consider the following scenario and identify whether the public officer is acting as a private owner or a constitutional trustee:",
                        "steps": [
                            "**Scenario:** A county official declares: 'This new tarmac road was funded by my office as a gift to my home village because they voted for me.'",
                            "**Constitutional Analysis:** The official is falsely acting as a **private owner/patron**. Under Article 201 and Article 10, public funds belong to the taxpayers of Kenya, not the individual politician. Expenditure must promote equitable development based on public need, not political reward.",
                            "**Correct Trustee Posture:** 'This road was constructed using public county funds approved through citizen public participation to enhance agricultural trade for our entire community.'"
                        ]
                    }
                }
            ],

            # Card 5: Source Analysis (Article 69 of the Constitution)
            [
                {
                    "type": "source_analysis",
                    "title": "Primary Source Analysis: Article 69 of the Constitution of Kenya (2010)",
                    "content": {
                        "source_title": "Article 69: Obligations of the State in respect of the Environment",
                        "source_type": "Supreme Constitutional Statute (Chapter Five: Land and Environment)",
                        "source_text": (
                            "1. The State shall—\n"
                            "   (a) ensure sustainable exploitation, utilisation, management and conservation of the environment and natural resources, and the equitable sharing of the accruing benefits;\n"
                            "   (b) work to achieve and maintain a tree cover of at least ten per cent of the land area of Kenya;\n"
                            "   (c) protect and enhance intellectual property in, and indigenous knowledge of, biodiversity and the genetic resources of the communities; and\n"
                            "   (d) encourage public participation in the management, protection and conservation of the environment."
                        ),
                        "prompts": [
                            {
                                "prompt": "1. What is it?",
                                "analysis": "This is an extract from Chapter Five (Land and Environment) of the Constitution of Kenya (2010), representing the supreme legal obligations governing environmental and natural resource management in the country."
                            },
                            {
                                "prompt": "2. Who created it?",
                                "analysis": "It was drafted through extensive public consultations by the Committee of Experts on Constitutional Review (CoE), approved by Kenyan citizens in the August 2010 national referendum, and promulgated into supreme law on August 27, 2010."
                            },
                            {
                                "prompt": "3. What does it tell us?",
                                "analysis": "It establishes a binding legal duty on the state to balance resource exploitation with environmental conservation, mandate at least 10% national tree cover, protect indigenous community knowledge, guarantee equitable benefit sharing, and enforce citizen public participation."
                            },
                            {
                                "prompt": "4. What are its limitations?",
                                "analysis": "While Article 69 establishes clear legal principles, it relies on subsidiary legislation (e.g., the Mining Act, EMCA, Forest Conservation Act) and state institutional capacity for daily enforcement. It does not automatically eliminate local community disputes over what percentage of revenue constitutes 'equitable sharing' unless explicitly defined in statutes."
                            }
                        ]
                    }
                }
            ],

            # Card 6: Real-World Application (Public Participation in Action)
            [
                {
                    "type": "real_world_example",
                    "title": "Public Participation in County Governance",
                    "content": {
                        "title": "Exercising Your Constitutional Right in County Budgeting",
                        "text": (
                            "When a county government plans to construct a fresh-produce market, sink a community borehole, or tarmac a feeder road, "
                            "the Constitution mandates that it must publish public notices inviting local residents to **public participation forums**.\n\n"
                            "At these civic hearings, citizens have the constitutional right under **Article 201** to ask:\n"
                            "- What is the total budget allocated for this public project, and what is the source of funding?\n"
                            "- Which contractor has been awarded the tender, and what is the scheduled completion timeline?\n"
                            "- Has an Environmental Impact Assessment (EIA) been conducted and approved by NEMA?\n\n"
                            "If a county government proceeds with a major capital project without genuine public participation, "
                            "citizens can challenge the expenditure in the High Court of Kenya, which has the power to declare the project null and void."
                        )
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Constitution of Kenya 2010 & Devolution of Public Resources",
                    "content": {
                        "title": "Understanding Devolution and Resource Stewardship in Kenya",
                        "youtube_id": "eGgGgZ0j9U4",
                        "url": "https://www.youtube.com/watch?v=eGgGgZ0j9U4",
                        "description": "An educational documentary examining the 2010 constitutional shift toward devolved governance, equitable resource distribution across 47 counties, and citizen empowerment."
                    }
                }
            ],

            # Card 7: Practice Case Study (Mining Titanium in Kwale County)
            [
                {
                    "type": "worked_example",
                    "title": "Case Study: Mineral Wealth & Royalty Sharing in Kwale County",
                    "content": {
                        "intro": "In Kwale County along the Kenyan coast, large-scale mining of titanium minerals (ilmenite, rutile, and zircon) has generated billions of shillings in export revenue. Examine how the Mining Act operationalizes Article 69 benefit sharing:",
                        "steps": [
                            "**The Royalty Distribution Formula:** Under the Mining Act (aligned with Article 69 of the Constitution), all mineral royalties collected by the state are distributed as follows:\n- **70%** $\\rightarrow$ National Government (General Exchequer for nationwide public services).\n- **20%** $\\rightarrow$ County Government of Kwale (for county development projects, roads, and healthcare).\n- **10%** $\\rightarrow$ Local Community hosting the mine (for local schools, bursaries, water projects, and clinics).",
                            "**Discussion Question 1 (Community Equity):** Why is the direct 10% allocation to the local mining community essential? *Answer:* Mining operations cause localized disruptions such as dust, noise, land displacement, and loss of grazing land. The 10% direct share compensates the host community and ensures they benefit directly from wealth extracted from their ancestral land.",
                            "**Discussion Question 2 (National Centralization Risk):** What would happen if the National Government retained 100% of mineral revenues? *Answer:* Local communities would feel exploited and marginalized, sparking social unrest, protests, and resource-based conflicts similar to historical pre-2010 grievances."
                        ]
                    }
                }
            ],

            # Card 8: Assessment & Misconception Remediation
            [
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 1: Constitutional Ownership of Public Resources",
                    "content": {
                        "question": "According to the Constitution of Kenya (2010), who is the primary owner of public resources, and what is the role of the government in managing them?",
                        "options": [
                            "The President owns them and distributes them as personal executive gifts",
                            "Public resources belong exclusively to county governors, and the national government has no authority",
                            "Public resources belong to all citizens of Kenya collectively; the government acts as a trustee or steward",
                            "Private multinational corporations own them, and the government collects a fixed 5% commission"
                        ],
                        "correct": "C",
                        "explanation": "Under Article 201 and Article 69 of the Constitution, public resources belong to the Kenyan people. The state and its officers serve as trustees (fiduciaries) tasked with managing public wealth transparently and equitably for current and future generations."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 2: Classification of Financial Public Resources",
                    "content": {
                        "question": "Which of the following is classified as a financial public resource in the Republic of Kenya?",
                        "options": [
                            "Kenyatta National Hospital main building",
                            "Tax revenue collected by the Kenya Revenue Authority (KRA)",
                            "The Mau Forest water catchment complex",
                            "The Standard Gauge Railway (SGR) track network"
                        ],
                        "correct": "B",
                        "explanation": "Tax revenue is a liquid financial resource. Kenyatta National Hospital and the SGR are physical public assets/infrastructure, while the Mau Forest is a natural resource."
                    }
                },
                {
                    "type": "remedial_misconception",
                    "title": "Common Misconception: Government Ownership vs. Public Stewardship",
                    "content": {
                        "misconception": "Public resources belong to the ruling government of the day, and politicians have the legal right to spend public funds however they wish without consulting anyone.",
                        "correction": "In reality, every shilling of tax revenue and every acre of public land belongs to the Kenyan people. The Constitution establishes independent watchdogs (the Auditor-General, Controller of Budget, EACC) and explicitly mandates public participation under Article 201 to ensure that leaders manage public wealth accountably."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Key Takeaways",
                    "content": {
                        "text": (
                            "1. **Public Stewardship**: Government is a trustee, not an owner; public wealth belongs to the citizens of Kenya.\n"
                            "2. **The 2010 Milestone**: Devolution divided governance into 1 national and 47 county governments, dismantling historical centralized marginalization.\n"
                            "3. **Three Pillars**: Public resources are classified into Natural Resources, Financial Resources, and Public Assets.\n"
                            "4. **Constitutional Anchors**: Article 69 enforces environmental protection and 10% tree cover; Article 201 enforces open, accountable, and participatory public finance."
                        )
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Challenges in Efficient Utilisation
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Challenges in Efficient Utilisation",
        "unit_description": "Analyzing the five structural leaks in resource management: corruption, mismanagement, environmental degradation, lack of transparency, and political interference.",
        "lesson_title": "Challenges in Efficient Utilisation",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Environmental Challenges and Resource Stress in Arid Kenya",
                    "content": {
                        "title": "Drought and Ecological Degradation in Arid Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/44/Continuing_Drought_in_Kenya_%285239%29.jpg",
                        "caption": "An arid landscape in northern Kenya illustrating how ecological degradation, deforestation, and climate stress exacerbate public resource scarcity.",
                        "author": "NASA Earth Observatory / Wikimedia Commons",
                        "licensing": "Public domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Leaking Bucket — Why Wealth Fails to Reach the Ground",
                    "content": {
                        "text": (
                            "Imagine carrying a heavy bucket of water from a river to your homestead to irrigate your family vegetable garden. "
                            "If the bucket is solid and sealed, all the water reaches your crops, helping them grow healthy and strong. "
                            "Now imagine carrying a bucket riddled with small cracks and holes. By the time you arrive home, the bucket is nearly empty. "
                            "The immense energy you spent fetching the water was wasted, and your crops remain parched.\n\n"
                            "In Kenya, our collective public resources can be compared to water in that bucket. "
                            "When tax revenues are collected by the KRA and natural wealth is extracted, they are meant to fund essential development: "
                            "building well-equipped maternity clinics, providing textbooks for schools, and paving roads so farmers can sell their produce. "
                            "However, serious **institutional leaks** prevent this wealth from benefiting ordinary citizens.\n\n"
                            "In this lesson, we will investigate the five critical leaks undermining Kenya's public wealth: "
                            "**corruption, mismanagement, environmental degradation, lack of transparency, and political interference**."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify and define the **five major challenges** affecting public resource utilization in Kenya\n"
                            "- Trace the **causal chain** from procurement fraud to local economic collapse and public distrust\n"
                            "- Analyze findings from an **Auditor-General audit report** using primary source evaluation techniques\n"
                            "- Distinguish between **unverified political allegations** and **audited empirical evidence** in civic discourse\n"
                            "- Evaluate the role of oversight bodies (EACC, DPP, Auditor-General) in blocking financial and physical resource waste"
                        )
                    }
                }
            ],

            # Card 2: Historical Context (Legacy of Weak Oversight)
            [
                {
                    "type": "concept_explanation",
                    "title": "A Legacy of Weak Oversight and Mismanagement",
                    "content": {
                        "text": (
                            "The challenge of managing public resources efficiently is not a recent phenomenon. "
                            "In the decades following independence in 1964, Kenya operated under an authoritarian centralized regime with limited institutional checks. "
                            "The executive branch held near-total control over budget allocations, land grants, and state appointments. "
                            "Watchdog bodies like the office of the Controller and Auditor-General lacked constitutional independence and adequate investigative funding.\n\n"
                            "Without mandatory citizen participation or robust anti-corruption commissions, public funds were routinely diverted, "
                            "state-funded infrastructure projects were abandoned midway, and gazetted public assets (such as water towers, research farm land, and school playgrounds) "
                            "were unlawfully grabbed by politically connected elites.\n\n"
                            "While the 2010 Constitution established powerful independent oversight institutions to seal these leaks, "
                            "entrenched habits of impunity, procurement inflation, and political patronage remain serious structural obstacles."
                        )
                    }
                }
            ],

            # Card 3: Core Knowledge (The Five Major Leaks)
            [
                {
                    "type": "comparison_table",
                    "title": "The Five Major Challenges to Efficient Resource Utilisation",
                    "content": {
                        "headers": ["Challenge", "Definition & Mechanism", "Kenyan Historical Example", "Impact on Everyday Citizens"],
                        "rows": [
                            ["Corruption", "Embezzlement, bribery, and fraudulent procurement schemes (e.g., inflated tender billing).", "Paying billions for non-existent medical equipment or phantom dam projects.", "Hospitals run out of essential drugs; public schools lack desks and laboratories."],
                            ["Mismanagement", "Incompetent planning, poor technical oversight, and execution of unviable 'white elephant' projects.", "Constructing a multi-million shilling market center in an isolated bush with no access road.", "Public tax money is wasted on idle structures while urgent community water needs are ignored."],
                            ["Environmental Degradation", "Unsustainable, illegal extraction of natural assets without reclamation or conservation.", "Illegal logging in the Mau Forest water tower and unregulated sand harvesting in dry riverbeds.", "Severe water shortages, flash floods, loss of agricultural topsoil, and climate vulnerability."],
                            ["Lack of Transparency", "Concealing budget allocations, tender awards, and revenue accounts from citizen inspection.", "Refusing to publish county expenditure reports or hiding procurement award documents.", "Prevents citizens from holding leaders accountable or detecting financial embezzlement early."],
                            ["Political Interference", "Diverting public resources to reward political loyalists, fund election campaigns, or punish rival regions.", "Paving tarmac roads exclusively in politically compliant wards while arid regions remain cut off.", "Deepens regional inequality and creates developmental injustice across the country."]
                        ]
                    }
                }
            ],

            # Card 4: Cause and Effect / Causal Chain
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Causal Chain of Resource Waste & Economic Mismanagement",
                    "content": {
                        "title": "Causal Flow of Resource Leakage",
                        "caption": "Step-by-step vector model demonstrating how a single governance leak triggers a cascading chain of infrastructure failure, service breakdown, farmer impoverishment, and systemic public distrust.",
                        "svg_content": SVG_CAUSAL_CHAIN_RESOURCE_WASTE
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Deconstructing the Chain Reaction of Mismanagement",
                    "content": {
                        "text": (
                            "Mismanagement and corruption never occur in isolation; they unleash a devastating chain reaction through the economy:\n\n"
                            "1. **Stage 1 (Governance Leak):** A corrupt procurement official inflates the cost of a rural feeder road tender and awards the contract to an unqualified, politically connected proxy company.\n"
                            "2. **Stage 2 (Direct Physical Failure):** The contractor uses substandard gravel, builds no drainage ditches, and abandons the site when the money runs out. The road washes away during the very first rainy season.\n"
                            "3. **Stage 3 (Socio-Economic Shock):** Local dairy and horticulture farmers cannot transport their fresh milk and cabbages to market. Produce rots on the farm, while emergency ambulances cannot reach sick patients in rural villages.\n"
                            "4. **Stage 4 (Systemic Crisis):** Rural household incomes plummet, urban food prices skyrocket due to supply shortages, and citizens lose faith in the legitimacy of the tax system."
                        )
                    }
                }
            ],

            # Card 5: Source Analysis (Auditor-General Audit Report)
            [
                {
                    "type": "source_analysis",
                    "title": "Primary Source Analysis: Extract from a National Audit Finding",
                    "content": {
                        "source_title": "Auditor-General Inspection Finding: Construction of Kwanza Health Centre",
                        "source_type": "Official Public Audit Finding (Fictionalized Case Study modeled on Auditor-General Reports)",
                        "source_text": (
                            "• Project Name: Construction and Equipping of Kwanza Level 3 Health Centre\n"
                            "• Approved Budget: KES 50,000,000\n"
                            "• Total Disbursed to Contractor: KES 45,000,000 (90% of contract sum)\n"
                            "• Verified Physical Progress: 40% complete. Site abandoned for over 12 months.\n"
                            "• Auditor Observations: Roofing trusses incomplete, walls unplastered, foundation exposed to waterlogging. "
                            "No bank performance guarantee was secured before disbursement. No public participation minutes were provided for the tender variation."
                        ),
                        "prompts": [
                            {
                                "prompt": "1. What is it?",
                                "analysis": "This is an official physical and financial audit finding compiled during a project inspection of a devolved public health facility."
                            },
                            {
                                "prompt": "2. Who created it?",
                                "analysis": "It was compiled by certified independent public auditors from the Office of the Auditor-General under the authority of Article 229 of the Constitution of Kenya."
                            },
                            {
                                "prompt": "3. What does it tell us?",
                                "analysis": "It exposes a massive financial and governance leak: 90% of the project funds (KES 45M) were paid out, but only 40% of the physical work was completed before the contractor abandoned the site, causing severe financial loss and depriving local residents of healthcare."
                            },
                            {
                                "prompt": "4. What are its limitations?",
                                "analysis": "An audit report establishes objective facts and quantifies financial loss, but the Auditor-General does not possess judicial powers to arrest, prosecute, or convict the guilty parties. Legal enforcement requires the Ethics and Anti-Corruption Commission (EACC) and the Director of Public Prosecutions (DPP)."
                            }
                        ]
                    }
                }
            ],

            # Card 6: Critical Thinking (Allegation vs. Verified Evidence)
            [
                {
                    "type": "concept_explanation",
                    "title": "Allegation vs. Verified Evidence in Civic Discourse",
                    "content": {
                        "text": (
                            "In daily civic life and on social media platforms, citizens frequently encounter sensational claims that public funds have been stolen. "
                            "As rigorous historians and responsible citizens, we must apply critical source evaluation to distinguish between unproven accusations and verified facts:\n\n"
                            "- **An Allegation**: An unproven claim, rumor, or political accusation made without verified supporting documentation (e.g., 'The Governor stole 200 million shillings from the borehole project').\n"
                            "- **Verified Evidence**: Audited, empirical proof established through verifiable records (e.g., an Auditor-General's report showing bank transaction statements of unauthorized cash withdrawals, or engineering inspection logs proving that foundation concrete failed standard safety tests).\n\n"
                            "Before drawing conclusions or participating in public debates, informed citizens must always ask: *Where is the audit report? What do the procurement records show? Has the evidence been independently verified?*"
                        )
                    }
                }
            ],

            # Card 7: Real-World Case Study / Video
            [
                {
                    "type": "real_world_example",
                    "title": "Environmental Degradation in Mining & Quarrying Sites",
                    "content": {
                        "title": "Unreclaimed Mineral Quarries and Community Hazards",
                        "text": (
                            "In many parts of Kenya where stone quarrying, sand harvesting, or gemstone mining takes place, "
                            "private contractors often abandon deep open pits without backfilling or planting trees. "
                            "During rainy seasons, these abandoned quarries turn into dangerous stagnant pools, causing fatal drownings "
                            "and breeding disease-carrying mosquitoes.\n\n"
                            "Under the **Environmental Management and Co-ordination Act (EMCA)** and Article 69 of the Constitution, "
                            "every mining company is legally required to submit an environmental restoration plan and post a restoration bond "
                            "to ensure the land is rehabilitated after mining operations conclude."
                        )
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Auditing Public Resources and Combating Mismanagement in Kenya",
                    "content": {
                        "title": "Public Resource Auditing and Anti-Corruption Oversight",
                        "youtube_id": "8YQ7Yx0bFMo",
                        "url": "https://www.youtube.com/watch?v=8YQ7Yx0bFMo",
                        "description": "An investigative report exploring how the Auditor-General tracks public expenditure, uncovers procurement irregularities, and helps safeguard taxpayer money."
                    }
                }
            ],

            # Card 8: Assessment & Misconception Remediation
            [
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 1: Identifying Environmental Degradation",
                    "content": {
                        "question": "Which of the following challenges is specifically characterized by the unsustainable exploitation of natural resources, such as illegal logging in major water towers?",
                        "options": [
                            "Political interference in civil service promotions",
                            "Environmental degradation",
                            "Lack of transparency in tax collection",
                            "Monetary inflation caused by high fuel prices"
                        ],
                        "correct": "B",
                        "explanation": "Unsustainable exploitation that damages ecosystems (like illegal logging in the Mau Forest or pollution of lakes) is environmental degradation. The other options refer to political, administrative, or macroeconomic issues."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 2: Consequences of Opacity in Procurement",
                    "content": {
                        "question": "What is the direct consequence of a 'lack of transparency' in county government procurement processes?",
                        "options": [
                            "It ensures that the most qualified and affordable local contractors are hired",
                            "It makes it extremely difficult for citizens and auditors to detect corruption, nepotism, and inflated billing",
                            "It automatically prevents environmental pollution across all 47 counties",
                            "It increases foreign direct investment and eliminates public sovereign debt"
                        ],
                        "correct": "B",
                        "explanation": "Transparency ensures that information is accessible to the public. When procurement is kept secret, public monitoring is blocked, enabling corrupt practices like tender rigging and price inflation to go undetected."
                    }
                },
                {
                    "type": "remedial_misconception",
                    "title": "Common Misconception: Automatic Blame vs. Root-Cause Analysis",
                    "content": {
                        "misconception": "If a public hospital runs out of antibiotics or a school runs out of textbooks, it is absolute, undeniable proof that the facility head stole the money.",
                        "correction": "While theft is a serious danger, shortages can also result from systemic delays at the National Treasury, supply chain disruptions at national medical depots (e.g., KEMSA), or sudden localized population surges. Responsible citizens and historians analyze verified evidence before assigning legal and moral blame."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Key Takeaways",
                    "content": {
                        "text": (
                            "1. **The 5 Leaks**: Corruption, Mismanagement, Environmental Degradation, Lack of Transparency, and Political Interference undermine public wealth.\n"
                            "2. **Cascading Causal Chain**: A single procurement leak leads directly to failed infrastructure, agricultural losses, and public distrust.\n"
                            "3. **Auditing Role**: The Auditor-General exposes discrepancies between disbursed funds and physical work on the ground.\n"
                            "4. **Evidence-Based Citizenship**: Critical citizens distinguish between unverified political allegations and audited empirical proof."
                        )
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Sustainable Utilisation and Ethical Advocacy
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Sustainable Utilisation and Ethical Advocacy",
        "unit_description": "Strategies for sustainable resource stewardship, NEMA Environmental Impact Assessments, Community Forest Associations, and active civic advocacy.",
        "lesson_title": "Sustainable Utilisation and Ethical Advocacy",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Forest Conservation and Sustainable Agro-Ecosystems in Kenya",
                    "content": {
                        "title": "Equatorial Rainforest Backdrop to Agro-Ecological Farms in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/ce/CSIRO_ScienceImage_4316_Equatorial_rainforest_is_the_backdrop_to_a_village_surrounded_by_a_maize_crop_in_Kenya_Africa_1981.jpg",
                        "caption": "A sustainable farming community bordered by protected equatorial forest in Kenya, demonstrating how responsible resource co-management preserves water towers while feeding the nation.",
                        "author": "CSIRO ScienceImage / Wikimedia Commons",
                        "licensing": "CC BY 3.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Plugging the Leaks — How We Protect Our Common Wealth",
                    "content": {
                        "text": (
                            "Discovering that our bucket of public resources has leaks is only the first diagnostic step. "
                            "If you find a crack in your water tank, you do not sit down and watch the water drain away into the dirt; "
                            "you immediately search for a strong plug, waterproof sealant, and repair tools to fix the damage.\n\n"
                            "As Kenyan citizens, we share a collective constitutional responsibility to protect our public wealth from being stolen, "
                            "squandered, or destroyed. **Sustainable utilization** means meeting the developmental needs of present Kenyans—using water, "
                            "land, minerals, and public revenues—without compromising or destroying the ability of future generations of Kenyans to meet their own needs.\n\n"
                            "Achieving sustainability requires a powerful combination of **institutional governance reforms** and **active civic advocacy**. "
                            "In this lesson, we examine the practical strategies used to manage Kenya's public wealth sustainably and ethically."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the constitutional mandate for **sustainable development** under Article 10 and Chapter Five\n"
                            "- Detail the **Four Pillar Strategies** for sustainable public resource management in Kenya\n"
                            "- Describe the role of **NEMA** in enforcing mandatory Environmental Impact Assessments (EIAs)\n"
                            "- Evaluate the success of **Community Forest Associations (CFAs)** in co-managing public natural assets\n"
                            "- Analyze civic advocacy media and apply ethical reporting channels (EACC, Ombudsman) to safeguard public funds"
                        )
                    }
                }
            ],

            # Card 2: Historical Context (The Constitutional Mandate for Sustainability)
            [
                {
                    "type": "concept_explanation",
                    "title": "The Constitutional Mandate for Sustainability",
                    "content": {
                        "text": (
                            "The principle of sustainability is not just a modern environmental slogan; it is a binding constitutional law in Kenya. "
                            "Under **Article 10(2)(d)** of the Constitution, **sustainable development** is explicitly designated as one of Kenya's national values "
                            "and principles of governance that bind all state organs, public officers, and citizens whenever they make or implement policy decisions.\n\n"
                            "Furthermore, Chapter Five establishes dedicated independent institutions to safeguard natural assets:\n"
                            "- **The National Land Commission (NLC)**: Manages public land on behalf of national and county governments, investigates historical land injustices, and prevents illegal land grabbing.\n"
                            "- **The National Environment Management Authority (NEMA)**: Established under EMCA to coordinate environmental policies, regulate pollution, and mandate that all major development projects undergo strict environmental scrutiny.\n\n"
                            "These institutions represent a decisive historical shift away from the pre-2010 era, when natural resource exploitation was dictated by political decrees rather than ecological science."
                        )
                    }
                }
            ],

            # Card 3: Core Knowledge (Four Strategies for Sustainable Management)
            [
                {
                    "type": "concept_explanation",
                    "title": "Four Strategies for Sustainable Resource Management",
                    "content": {
                        "text": (
                            "To ensure our public wealth is protected and preserved, Kenya utilizes four interconnected strategies:\n\n"
                            "1. **Strengthening Governance and Accountability**: Empowering independent watchdogs like the **Auditor-General** and the **Ethics and Anti-Corruption Commission (EACC)** to audit accounts and prosecute economic crimes, while strictly enforcing the leadership ethics in **Chapter Six**.\n\n"
                            "2. **Promoting Public Participation and Co-Management**: Involving citizens in reviewing county annual budgets and empowering grassroots organizations—such as **Community Forest Associations (CFAs)** and **Water Resource Users Associations (WRUAs)**—to co-manage local natural resources.\n\n"
                            "3. **Public Education and Civic Awareness**: Educating citizens about their constitutional rights under Article 35 (Access to Information) and Article 201, while promoting sustainable agro-forestry in schools.\n\n"
                            "4. **Enforcing Environmental Impact Assessments (EIAs)**: Requiring developers (public and private) to conduct comprehensive scientific EIAs approved by **NEMA** before commencing major infrastructure projects (such as highways, dams, factories, or mines)."
                        )
                    }
                },
                {
                    "type": "suggested_diagram",
                    "title": "The Kenyan Sustainability Loop",
                    "content": {
                        "title": "The Closed-Cycle Sustainability Loop",
                        "caption": "Vector diagram illustrating the continuous 5-stage loop: 1. Ethical Planning & EIA -> 2. Open Procurement -> 3. Independent Oversight -> 4. Equitable Benefit Sharing -> 5. Conservation & Reinvestment.",
                        "svg_content": SVG_SUSTAINABILITY_LOOP
                    }
                }
            ],

            # Card 4: Ethical Citizenship & Civic Action
            [
                {
                    "type": "real_world_example",
                    "title": "Civic Advocacy: How Citizens Protect Public Wealth",
                    "content": {
                        "title": "Practical Citizen Actions for Resource Integrity",
                        "text": (
                            "Citizens are not powerless bystanders; we are the primary owners of public wealth. "
                            "Ethical advocacy involves active, peaceful, and lawful participation:\n\n"
                            "- **Conserve Shared Resources**: Avoid wasting water at community taps, protect school infrastructure from vandalism, and stop illegal dumping in local rivers.\n"
                            "- **Participate in County Budgeting**: Attend ward public participation meetings to ensure public money is directed toward genuine priorities (such as clean water, rural health clinics, and schools).\n"
                            "- **Demand Accountability & Blow the Whistle**: When you observe public assets being misused (e.g., government vehicles used for private business, or shoddy road construction), report the matter through official channels: the **EACC Hotline (0800 720 123)** or the **Ombudsman (Commission on Administrative Justice)**."
                        )
                    }
                }
            ],

            # Card 5: Source Analysis (Advocacy Poster — "Mali ya Umma")
            [
                {
                    "type": "suggested_diagram",
                    "title": "Infographic Poster: Mali ya Umma — Ni Mali Yako!",
                    "content": {
                        "title": "National Civic Advocacy Poster",
                        "caption": "Civic advocacy poster illustrating the four pillars of citizen duty: Know Your Rights, Participate, Conserve, and Report.",
                        "svg_content": SVG_MALI_YA_UMMA_POSTER
                    }
                },
                {
                    "type": "source_analysis",
                    "title": "Primary Source Analysis: Civic Advocacy Poster on Public Wealth",
                    "content": {
                        "source_title": "Mali ya Umma, Ni Mali Yako! (Public Wealth is Your Wealth!)",
                        "source_type": "Civic Advocacy Poster / Visual Public Awareness Campaign",
                        "source_text": (
                            "• Header: 'MALI YA UMMA — NI MALI YAKO!'\n"
                            "• Slogan: 'Transparency is the key to locking out corruption. Protect your public wealth.'\n"
                            "• 4 Action Pillars: 1. Know Your Rights (Art. 201) | 2. Participate (Ward Forums) | 3. Conserve (Water Towers & Infrastructure) | 4. Report (EACC Toll-Free Hotline 0800 720 123)\n"
                            "• Core Symbol: A golden key securing the Public Treasury chest against leakage."
                        ),
                        "prompts": [
                            {
                                "prompt": "1. What is it?",
                                "analysis": "A public civic education poster designed for broad display in schools, county offices, and community centers across Kenya."
                            },
                            {
                                "prompt": "2. Who created it?",
                                "analysis": "Produced by civil society governance coalitions in partnership with the Ethics and Anti-Corruption Commission (EACC) to promote constitutional values."
                            },
                            {
                                "prompt": "3. What is its purpose?",
                                "analysis": "To inspire Kenyan citizens to abandon apathy, view public funds and assets as their personal collective property, and actively report resource mismanagement."
                            },
                            {
                                "prompt": "4. What are its limitations?",
                                "analysis": "A poster creates awareness and moral inspiration, but it cannot alone fix systemic corruption without citizen courage to whistleblow and responsive, uncorrupted law enforcement and judicial institutions."
                            }
                        ]
                    }
                }
            ],

            # Card 6: Practice Case Study (Karura Forest & CFAs)
            [
                {
                    "type": "worked_example",
                    "title": "Case Study: Prof. Wangari Maathai and the Rescue of Karura Forest",
                    "content": {
                        "intro": "Examine one of the most famous historical examples of ethical civic advocacy in Kenyan history:",
                        "steps": [
                            "**The Historical Crisis (Late 1990s):** Large tracts of Karura Forest in Nairobi were illegally de-gazetted and allocated to private developers by corrupt officials. Bull-dozers began clearing indigenous trees to build luxury private real estate.",
                            "**Civic Resistance:** Nobel Peace Prize Laureate **Prof. Wangari Maathai** and the Green Belt Movement organized peaceful protests, planted seedlings, mobilized university students, and rallied international media to resist the destruction of this vital urban water tower.",
                            "**The Outcome:** Due to relentless civic advocacy, the illegal allocations were revoked. Today, Karura Forest is protected and co-managed by the Kenya Forest Service (KFS) and the **Karura Community Forest Association (CFA)**, providing recreation, clean air, and water to millions of Nairobi residents.",
                            "**Historical Lesson:** Active, lawful civic advocacy by courageous citizens can successfully reverse the illegal grabbing of public wealth."
                        ]
                    }
                }
            ],

            # Card 7: Real-World Video & Reflection
            [
                {
                    "type": "concept_explanation",
                    "title": "The Role of NEMA and Environmental Impact Assessments",
                    "content": {
                        "text": (
                            "Before any major highway, geothermal plant, dam, or factory is constructed, "
                            "the developer must hire certified environmental experts to conduct an **Environmental Impact Assessment (EIA)**. "
                            "The EIA report evaluates potential hazards (soil erosion, chemical runoff, deforestation) and proposes mitigation measures. "
                            "NEMA publishes the EIA summary and invites public comments before issuing a license, ensuring development does not destroy ecosystems."
                        )
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Sustainable Resource Management and Environmental Protection in Kenya",
                    "content": {
                        "title": "Balancing Economic Development and Environmental Conservation",
                        "youtube_id": "1BfCnjr_Vjg",
                        "url": "https://www.youtube.com/watch?v=1BfCnjr_Vjg",
                        "description": "An educational overview examining Kenya's green energy investments (geothermal, wind, solar), reforestation initiatives, and NEMA's regulatory role."
                    }
                }
            ],

            # Card 8: Assessment & Misconception Remediation
            [
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 1: Citizen Co-Management of Resources",
                    "content": {
                        "question": "Which of the following strategies directly involves local citizens co-managing public resources and reviewing county annual budget proposals?",
                        "options": [
                            "Imposing total military control over all rural markets",
                            "Privatizing all gazetted national parks and selling them to foreign investors",
                            "Promoting Public Participation through forums, CFAs, and WRUAs",
                            "Abolishing the Office of the Auditor-General and eliminating public records"
                        ],
                        "correct": "C",
                        "explanation": "Public participation is the constitutional mechanism that empowers citizens to engage in budgeting and co-manage natural assets through Community Forest Associations (CFAs) and Water Resource Users Associations (WRUAs)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 2: Mandate of NEMA in Sustainable Governance",
                    "content": {
                        "question": "What is the primary function of the National Environment Management Authority (NEMA) in sustainable resource management?",
                        "options": [
                            "To collect national income taxes and customs duties on behalf of KRA",
                            "To ensure that development projects undergo rigorous Environmental Impact Assessments (EIAs) before licensing",
                            "To conduct national general elections across all 47 counties",
                            "To print and issue new generation banknotes for the Central Bank of Kenya"
                        ],
                        "correct": "B",
                        "explanation": "NEMA is mandated to supervise environmental management and enforce mandatory Environmental Impact Assessments (EIAs) before major development projects begin."
                    }
                },
                {
                    "type": "remedial_misconception",
                    "title": "Common Misconception: Peaceful Civic Advocacy vs. Violence",
                    "content": {
                        "misconception": "Civic advocacy means organizing violent riots and destroying public property whenever we are unhappy with government decisions.",
                        "correction": "True constitutional advocacy operates firmly within the rule of law. It involves attending public participation forums, writing formal petitions to county assemblies, reporting corruption to the EACC, and educating communities. Destroying public property harms the very assets we are striving to protect."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Key Takeaways",
                    "content": {
                        "text": (
                            "1. **Constitutional Sustainability**: Article 10 establishes sustainable development as a binding national value.\n"
                            "2. **Four Pillar Strategies**: Governance reform, public participation, civic education, and mandatory EIAs via NEMA.\n"
                            "3. **Co-Management**: Grassroots groups (CFAs and WRUAs) partner with state agencies to guard water towers and forests.\n"
                            "4. **Ethical Advocacy**: Citizens protect public wealth through lawful action: attending budget forums, conserving shared assets, and blowing the whistle to the EACC."
                        )
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Applied Constitutional Inquiry
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Applied Constitutional Inquiry",
        "unit_description": "Hands-on historical and civic inquiry applying Article 201, budget analysis, and community testimony to evaluate public resource decisions in county governance.",
        "lesson_title": "Applied Constitutional Inquiry",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Community Consultation and Citizen Voice in Rural Kenya",
                    "content": {
                        "title": "Grassroots Citizen Consultation in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/A_farmer_being_interviewed.jpg",
                        "caption": "A rural Kenyan farmer providing testimony during a field inquiry, representing the essential role of community voice in evaluating public resource decisions.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Becoming a Historical and Civic Detective",
                    "content": {
                        "text": (
                            "How do we know whether our constitution is truly working to protect our public wealth? "
                            "We cannot rely merely on political speeches, press releases, or social media rumors. "
                            "Instead, we must think like **historical detectives**: assembling empirical evidence dossiers, "
                            "evaluating primary statutory texts, analyzing conflicting stakeholder perspectives, and formulating reasoned, evidence-based conclusions.\n\n"
                            "In this capstone inquiry lesson, you will apply the historical and civic concepts learned across this topic "
                            "to evaluate a complex, real-world development controversy in a fictionalized Kenyan county. "
                            "You will analyze constitutional clauses, financial balance sheets, and grassroots community testimonies "
                            "to draft an authoritative citizen memorandum."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Apply the 4-step **Citizen Detective Inquiry Protocol** to evaluate complex public resource scenarios\n"
                            "- Deconstruct a multi-source **Evidence Dossier** containing legal statutes, financial balance sheets, and community testimonies\n"
                            "- Evaluate financial project plans against **Article 201(b)(iii)** (equitable development and special provision for marginalized areas)\n"
                            "- Draft a formal **Citizen Recommendation Memorandum** for presentation to a County Assembly Committee\n"
                            "- Consolidate all core concepts of Topic 1.3 (Constitutional Stewardship, 3 Pillars, 5 Leaks, and Sustainability)"
                        )
                    }
                }
            ],

            # Card 2: The Evidence Dossier (The Mara County Water Case)
            [
                {
                    "type": "concept_explanation",
                    "title": "The Evidence Dossier: The Proposed Mara County Water Project",
                    "content": {
                        "text": (
                            "Imagine you are the Lead Researcher on an independent Citizen Social Audit Committee in **Mara County**. "
                            "The County Executive has announced the multi-million shilling **Mara Phase 1 Water Pipeline Project**. "
                            "Your committee has assembled the following Evidence Dossier:"
                        )
                    }
                },
                {
                    "type": "source_analysis",
                    "title": "Evidence Dossier Source A: Article 201 of the Constitution of Kenya (2010)",
                    "content": {
                        "source_title": "Source A: Excerpt from Chapter 12 (Public Finance), Article 201",
                        "source_type": "Supreme Constitutional Statute",
                        "source_text": (
                            "The following principles shall guide all aspects of public finance in the Republic—\n"
                            "(a) there shall be openness and accountability, including public participation in financial matters;\n"
                            "(b) the public finance system shall promote an equitable society, and in particular—\n"
                            "    (i) the burden of taxation shall be shared fairly;\n"
                            "    (ii) revenue raised nationally shall be shared equitably between national and county governments; and\n"
                            "    (iii) expenditure shall promote the equitable development of the country, including by making special provision for marginalised groups and areas."
                        ),
                        "prompts": [
                            {
                                "prompt": "1. What is the core constitutional test in Source A?",
                                "analysis": "Article 201(b)(iii) establishes that public spending must promote equitable development across the entire territory and mandate affirmative action for marginalized, underserved areas."
                            }
                        ]
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Evidence Dossier Source B: Project Financial & Geographic Blueprint",
                    "content": {
                        "headers": ["Project Parameter", "Project Details", "Auditor Observations"],
                        "rows": [
                            ["Approved Project Budget", "KES 120,000,000", "Total capital expenditure over 18 months."],
                            ["Funding Structure", "60% County Revenue Fund (KES 72M)\n40% International Loan (KES 48M)", "Loan to be repaid over 15 years through water tariffs levied on all county residents."],
                            ["Target Coverage Area", "Exclusively Ward A (Urbanized)", "Ward A is the home ward of the County Governor and already has two functional boreholes."],
                            ["Excluded Communities", "Ward B and Ward C (Arid/Rural)", "Wards B and C have 80% water scarcity, no piped infrastructure, and were omitted from Phase 1 design."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Evidence Dossier Source C: Grassroots Community Testimony",
                    "content": {
                        "text": (
                            "> **Testimony of Mr. John Kepkemboi (Resident Elder of Ward B):**\n"
                            "> *'Our women and school children walk five kilometers every morning to fetch muddy water from seasonal ponds, "
                            "while Ward A already has two functional community boreholes and running water. "
                            "Now we discover the county is taking a 120 million shilling loan, and our families will be forced to pay water tariffs "
                            "for the next 15 years to repay this debt, yet we will not receive a single drop of water from this pipeline! "
                            "This is not fair development; it is political punishment!'*"
                        )
                    }
                }
            ],

            # Card 3: Inquiry Protocol & Vector Framework
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Historical & Civic Detective Inquiry Protocol",
                    "content": {
                        "title": "4-Step Evidence Evaluation Framework",
                        "caption": "Vector flowchart showing the 4-step inquiry process: 1. Assemble Dossier -> 2. Equity & Law Check -> 3. Detect Bias & Favoritism -> 4. Formulate Action Plan.",
                        "svg_content": SVG_CONSTITUTIONAL_INQUIRY_FRAMEWORK
                    }
                }
            ],

            # Card 4: Critical Thinking / Guided Analysis
            [
                {
                    "type": "worked_example",
                    "title": "Applying Constitutional Tests to the Mara Water Project",
                    "content": {
                        "intro": "Evaluate the Evidence Dossier using three critical historical inquiry lenses:",
                        "steps": [
                            "**Test 1 (The Equity Check):** Does the financial plan in Source B comply with Article 201(b)(iii) (Source A)?\n*Evaluation:* **No.** Allocating 100% of a KES 120M water project exclusively to an already advantaged ward (Ward A) while completely ignoring water-scarce, marginalized wards (Wards B and C) directly violates the constitutional requirement to make special provision for marginalized areas.",
                            "**Test 2 (The Intergenerational Debt Burden):** Is it ethical for residents of Wards B and C to repay a 15-year loan for a project they cannot access?\n*Evaluation:* **No.** Article 201(b)(i) dictates that the burden of taxation and public debt must be shared fairly. Compelling citizens in Wards B and C to repay KES 48M in sovereign debt for 15 years without receiving water infrastructure constitutes an unjust financial extraction.",
                            "**Test 3 (Detecting Political Favoritism):** What explains why Ward A was prioritized over Wards B and C?\n*Evaluation:* The project reflects **political interference and patronage** (allocating resources to the Governor's home ward) rather than an objective, needs-based technical assessment."
                        ]
                    }
                }
            ],

            # Card 5: Synthesis & Citizen Action (The County Assembly Memo)
            [
                {
                    "type": "concept_explanation",
                    "title": "Drafting the Citizen Recommendation Memorandum",
                    "content": {
                        "text": (
                            "As an informed citizen committee, you must draft a professional memorandum to the **County Assembly Committee on Water and Budget**. "
                            "Your report should be structured as follows:\n\n"
                            "1. **Acknowledge the Legitimate Objective:** Recognize that expanding clean piped water infrastructure is a vital public necessity.\n"
                            "2. **State the Constitutional Violations:** Cite explicit violations of **Article 201(b)(iii)** (equitable development) and **Article 10** (national values of equity and inclusiveness).\n"
                            "3. **Propose Actionable Revisions:**\n"
                            "   - *Redesign the Distribution Network:* Re-allocate the KES 120M budget to construct a shared central gravity pipeline with distribution trunk lines serving Wards A, B, and C simultaneously.\n"
                            "   - *Mandate Immediate Public Participation:* Direct the County Executive to hold genuine ward-level public participation hearings in Wards B and C within 21 days.\n"
                            "   - *Legal Notice:* State clearly that failure to revise the project will compel citizen groups to petition the High Court for an injunction halting the disbursement of loan funds."
                        )
                    }
                }
            ],

            # Card 6: Real-World Video & Simulation
            [
                {
                    "type": "real_world_example",
                    "title": "Simulation: The County Assembly Committee Hearing",
                    "content": {
                        "title": "Presenting Evidence Before the Legislative Committee",
                        "text": (
                            "In a democratic system, presenting evidence-based memorandums before parliamentary and county assembly committees "
                            "is a primary constitutional tool for social auditing. "
                            "When citizens present audited facts rather than emotional rhetoric, legislators are compelled to review executive budgets "
                            "and enforce constitutional compliance."
                        )
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Social Audits and Citizen Participation in County Governance",
                    "content": {
                        "title": "Empowering Communities Through Budget Tracking and Social Audits",
                        "youtube_id": "2X_2IdriMTc",
                        "url": "https://www.youtube.com/watch?v=2X_2IdriMTc",
                        "description": "A documentary tracking how grassroots community groups in Kenya use social audit methodologies to inspect public project sites, track county budgets, and demand accountability."
                    }
                }
            ],

            # Card 7: Topic Recap & Knowledge Consolidation
            [
                {
                    "type": "concept_explanation",
                    "title": "Comprehensive Summary: Topic 1.3 Public Resources Architecture",
                    "content": {
                        "text": (
                            "Let us review the historical journey and civic principles mastered in Topic 1.3:\n\n"
                            "- **The Historical Arc:** Kenya moved from post-colonial centralized resource control (1964–2010)—which created deep regional marginalization—to **Devolution** under the **Constitution of Kenya (2010)**.\n"
                            "- **Public Trusteeship:** Government does not own the wealth; it acts as a steward for all 50+ million citizens.\n"
                            "- **Three Pillars of Wealth:**\n"
                            "  1. *Natural Resources:* Land, water towers, minerals, wildlife.\n"
                            "  2. *Financial Resources:* KRA tax revenues, loans, grants, state enterprise dividends.\n"
                            "  3. *Public Assets:* Transport infrastructure (SGR/roads), public schools, hospitals, civic buildings.\n"
                            "- **Five Critical Leaks:** Corruption, Mismanagement, Environmental Degradation, Lack of Transparency, and Political Interference.\n"
                            "- **Four Sustainability Strategies:** Strong governance watchdogs (Auditor-General/EACC), public participation (CFAs/WRUAs), civic education, and mandatory EIAs via NEMA.\n"
                            "- **Constitutional Anchors:** Article 10 (Values), Article 69 (Environment & 10% tree cover), Article 201 (Public Finance), Article 229 (Auditor-General), and Chapter Six (Leadership & Integrity)."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Topic 1.3 Key Constitutional Provisions Matrix",
                    "content": {
                        "headers": ["Constitutional Provision", "Core Legal Mandate", "Civic Impact for Kenyans"],
                        "rows": [
                            ["Article 10", "National values including sustainable development, equity, integrity, and transparency.", "Binds all state officers in all policy decisions."],
                            ["Article 69", "State obligation to conserve environment, maintain 10% tree cover, and share resource benefits equitably.", "Protects water towers and mandates community mining royalties."],
                            ["Article 201", "Principles of public finance: openness, accountability, equitable burden sharing, and public participation.", "Guarantees citizen right to inspect budgets and challenge unequal spending."],
                            ["Article 229", "Independent office of the Auditor-General to audit all public entities.", "Exposes financial waste, corruption, and abandoned projects."],
                            ["Chapter Six", "Leadership and integrity standards for public officers.", "Prohibits conflicts of interest and establishes public office as a trust."]
                        ]
                    }
                }
            ],

            # Card 8: Assessment & Misconception Remediation
            [
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 1: Legal Basis for Challenging Spending Disparities",
                    "content": {
                        "question": "Which constitutional article would Mr. John Kepkemboi from Ward B use as the primary legal basis to challenge the unequal allocation of the county water project in court?",
                        "options": [
                            "Chapter One: Sovereignty of the People (General clause)",
                            "Article 201: Principles of Public Finance (Equitable Development and Special Provision for Marginalized Areas)",
                            "Article 6: Devolution of Government Offices",
                            "Article 81: General Principles of the Electoral System"
                        ],
                        "correct": "B",
                        "explanation": "Article 201(b)(iii) explicitly commands that public expenditure must promote equitable development across the country and make special provision for marginalized areas. This is the direct legal basis to challenge regional disparities in public spending."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Assessment Question 2: Defining a Sustainable Public Project",
                    "content": {
                        "question": "What makes a county infrastructure project genuinely sustainable according to constitutional principles of stewardship?",
                        "options": [
                            "Using quality engineering that prevents physical leaks, while ensuring benefits and debt burdens are shared equitably and ecosystems are protected",
                            "Restricting service delivery exclusively to politically loyal voters to secure the next election victory",
                            "Allowing industrial waste to be dumped untreated into rivers to save county operating expenses",
                            "Concealing all project financial records to prevent citizens from questioning the budget"
                        ],
                        "correct": "A",
                        "explanation": "True sustainability combines technical efficiency (high quality engineering), social and economic equity (fair sharing of benefits and debt), and environmental conservation."
                    }
                },
                {
                    "type": "remedial_misconception",
                    "title": "Common Misconception: Citizen Powerlessness in Budgeting",
                    "content": {
                        "misconception": "Ordinary high school students and citizens have zero power to influence multi-million shilling county government project budgets.",
                        "correction": "The Constitution gives every Kenyan citizen direct sovereignty. By attending ward public participation meetings, organizing social audits, submitting formal memorandums to county assemblies, or petitioning the courts under Article 201, ordinary citizens have repeatedly forced governments to redesign projects, halt unlawful spending, and equitably share public wealth."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Topic 1.3 Final Mastery Summary",
                    "content": {
                        "text": (
                            "1. **Public Resources Belong to You**: Government is a constitutional trustee, not a private owner.\n"
                            "2. **Auditing and Evidence**: Always demand verified audit reports and financial records when evaluating public spending.\n"
                            "3. **Equitable Devolution**: Public expenditure must reach marginalized communities and foster national unity.\n"
                            "4. **Active Civic Duty**: Protect our water towers, participate in budget forums, and hold leaders accountable under Article 201!"
                        )
                    }
                }
            ]
        ]
    }
]
