"""
VLearn CBC Grade 10 History — Topic 5: Elections in Kenya
Comprehensive Pedagogical Data Definitions (Lessons 1 to 4)
"""

from curriculum.cbc_grade10_history_topic5_svgs import (
    SVG_IEBC_CORE_FUNCTIONS_WHEEL,
    SVG_DEMOCRATIC_ACCOUNTABILITY_CYCLE,
    SVG_CORE_VALUES_INTEGRITY_STAR,
    SVG_ELECTION_PEACE_SIMULATION_MAP
)

TOPIC_5_LESSONS = [
    # =========================================================================
    # LESSON 1: How Elections Work
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "How Elections Work",
        "unit_description": "The constitutional and statutory framework of Kenyan elections, the constitutional mandate and core functions of the IEBC, and the six consecutive phases of the Kenyan electoral cycle.",
        "lesson_title": "How Elections Work",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The Heartbeat of Democracy: Citizens Exercising Sovereign Choice",
                    "content": {
                        "title": "Kenyan Citizens Queuing to Vote on Polling Day",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg",
                        "caption": "Kenyan citizens participating in universal adult suffrage on election day, exercising sovereign power under Article 38 of the Constitution of Kenya (2010).",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain / CC BY-SA"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Representative Democracy and the Electoral Mandate",
                    "content": {
                        "text": (
                            "Imagine a secondary school with over a thousand students. If the entire school needs to choose "
                            "a student council president or determine school development priorities, having all 1,000 students "
                            "gather in a single room to debate every minor administrative decision would be impossible. "
                            "Instead, students **delegate** their decision-making authority by voting for representatives.\n\n"
                            "In a sovereign republic of over fifty million citizens, this delegating mechanism is called "
                            "**representative democracy**. In Kenya, elections are the formal, constitutionally protected mechanism "
                            "through which citizens exercise their sovereign power—either directly or through their democratically "
                            "elected leaders."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the constitutional and statutory hierarchy governing Kenyan elections (Article 38, Chapter 7, Elections Act)\n"
                            "- Analyze the historical transition from the defunct ECK to the Independent Electoral and Boundaries Commission (IEBC)\n"
                            "- Identify and evaluate the six core constitutional functions of the IEBC under Article 88\n"
                            "- Outline the six consecutive chronological phases of the Kenyan electoral cycle\n"
                            "- Describe the role of technology (BVR and KIEMS) in modern biometric voting administration"
                        )
                    }
                }
            ],

            # Card 2: Legal and Constitutional Framework
            [
                {
                    "type": "concept_explanation",
                    "title": "The Four Pillars of Kenyan Electoral Law",
                    "content": {
                        "text": (
                            "Elections in Kenya do not occur in an arbitrary manner; they are strictly anchored in a robust "
                            "statutory hierarchy designed to guarantee fairness, transparency, and legal predictability:\n\n"
                            "1. **The Constitution of Kenya (2010):** The supreme law of the Republic. Article 38 guarantees political rights "
                            "and universal adult suffrage, while Chapter Seven (Articles 81–92) establishes the foundational electoral principles.\n"
                            "2. **The Elections Act (2011):** Provides the granular statutory operational rules for voter registration, "
                            "campaign regulations, nomination procedures, polling administration, and dispute resolution.\n"
                            "3. **The Independent Electoral and Boundaries Commission (IEBC) Act (2011):** Outlines the appointment, structure, "
                            "qualifications, powers, and operational independence of electoral commissioners.\n"
                            "4. **The Electoral Code of Conduct:** A legally binding covenant enforceable by law, signed by all political parties "
                            "and candidates, committing them to peaceful campaigning, non-violence, and adherence to democratic ethics."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Hierarchy of Kenyan Electoral Legislation",
                    "content": {
                        "headers": ["Legal Instrument", "Constitutional / Statutory Mandate", "Primary Electoral Focus"],
                        "rows": [
                            ["Constitution (2010)", "Supreme Law (Articles 38, 81, 88)", "Guarantees voting rights, gender rule, and independence of IEBC"],
                            ["Elections Act (2011)", "Statutory Legislation", "Regulates nomination, polling stations, tallying, and election petitions"],
                            ["IEBC Act (2011)", "Institutional Governance", "Governs the secretariat, commissioner selection, and commission autonomy"],
                            ["Electoral Code of Conduct", "Binding Administrative Covenant", "Enforces non-violence, ethical campaigning, and sanctions against misconduct"]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Historical Reform: From ECK to IEBC",
                    "content": {
                        "text": (
                            "Before the promulgation of the Constitution of Kenya (2010), Kenya's electoral management body was the "
                            "**Electoral Commission of Kenya (ECK)**. The disputed presidential results of the **2007 General Election** "
                            "revealed catastrophic institutional vulnerabilities, including lack of tallying transparency, executive interference, "
                            "and fragile dispute resolution procedures, leading to widespread post-election violence.\n\n"
                            "Following the recommendations of the **Kriegler Independent Review Commission (IREC)** and the enactment of the "
                            "2010 Constitution, the ECK was disbanded. In its place, the IEBC was established as an independent Chapter Fifteen "
                            "constitutional commission, protected from executive control and empowered with full financial and administrative autonomy."
                        )
                    }
                }
            ],

            # Card 3: Mandate and Core Functions of the IEBC
            [
                {
                    "type": "suggested_diagram",
                    "title": "IEBC Core Functions Wheel (Article 88)",
                    "content": {
                        "title": "IEBC Constitutional Mandate Wheel",
                        "svg_content": SVG_IEBC_CORE_FUNCTIONS_WHEEL,
                        "caption": "The six constitutional functions of the Independent Electoral and Boundaries Commission (IEBC) under Article 88 of the Constitution of Kenya (2010)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Deep Dive: The Six Constitutional Functions of the IEBC",
                    "content": {
                        "text": (
                            "Under **Article 88(4)** of the Constitution of Kenya, the IEBC is responsible for managing every aspect "
                            "of electoral democracy:\n\n"
                            "1. **Continuous Voter Registration:** Registering all eligible Kenyan citizens aged 18 and above and maintaining an "
                            "up-to-date Biometric Voters Register (BVR).\n"
                            "2. **Delimitation of Electoral Boundaries:** Reviewing constituency and ward boundaries periodically (between 8 and 12 years) "
                            "to ensure population equity and fair geographic representation.\n"
                            "3. **Supervising and Conducting Elections:** Administering general elections every five years for six elective seats "
                            "(President, Governor, Senator, MP, Woman Representative, MCA) as well as national referenda and by-elections.\n"
                            "4. **Continuous Voter and Civic Education:** Sensitizing citizens on their political rights, the electoral process, and peaceful participation.\n"
                            "5. **Results Verification and Declaration:** Accurately counting, transparently transmitting (Form 34A), tallying, and announcing verified results.\n"
                            "6. **Regulating Campaign Financing:** Monitoring campaign expenditures to prevent illicit money from compromising democratic outcomes."
                        )
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Key Electoral Terminology",
                    "content": {
                        "term": "Universal Adult Suffrage & Boundary Delimitation",
                        "definition": "**Universal Adult Suffrage** is the constitutional right of every adult citizen, regardless of wealth, gender, or ethnicity, to cast one vote of equal weight. **Boundary Delimitation** is the periodic review and adjustment of constituency and county ward geographical borders to reflect population changes while respecting historical and community ties."
                    }
                }
            ],

            # Card 4: The Kenyan Electoral Cycle and Timeline
            [
                {
                    "type": "step_process",
                    "title": "The Six Phases of the Kenyan Electoral Cycle",
                    "content": {
                        "steps": [
                            {
                                "step": 1,
                                "name": "Voter Registration & Register Audit",
                                "description": "Continuous and enhanced voter registration where eligible citizens register using biometric data. The IEBC opens the register for public inspection and forensic audit."
                            },
                            {
                                "step": 2,
                                "name": "Candidate Nomination & Party Primaries",
                                "description": "Political parties conduct primaries to nominate contenders. The IEBC clears party-sponsored and independent candidates who meet constitutional and Chapter 6 integrity criteria."
                            },
                            {
                                "step": 3,
                                "name": "Official Campaign Period",
                                "description": "A strictly scheduled campaign period where candidates present their policy manifestos through public rallies, media, and debates, bound by the Electoral Code of Conduct."
                            },
                            {
                                "step": 4,
                                "name": "Polling Day (Voting)",
                                "description": "Registered voters present their national ID and are biometrically verified using the KIEMS kit before casting secret paper ballots in marked ballot boxes."
                            },
                            {
                                "step": 5,
                                "name": "Counting, Tallying & Results Declaration",
                                "description": "Ballots are counted publicly at each polling station in the presence of candidate agents and observers. Form 34A is signed, scanned, electronically transmitted, and published on a public portal."
                            },
                            {
                                "step": 6,
                                "name": "Judicial Dispute Resolution",
                                "description": "Dissatisfied contenders file election petitions before designated courts (High Court for county/parliamentary; Supreme Court for presidential) within statutory deadlines."
                            }
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Elections as a Continuous Cycle",
                    "content": {
                        "text": (
                            "A common misconception is that an election is a single-day event. In reality, democratic governance "
                            "relies on an unbroken **electoral cycle**. The post-election dispute resolution and institutional review "
                            "phases directly feed into legal reforms, voter education, and voter registration for the subsequent general election."
                        )
                    }
                }
            ],

            # Card 5: Technology & Video Masterclass
            [
                {
                    "type": "suggested_video",
                    "title": "Video: How Elections Work in Kenya",
                    "content": {
                        "title": "Understanding the Electoral Process and IEBC Operations",
                        "youtube_id": "bO7FQsCcbD8",
                        "description": "An educational overview of how elections are structured, organized, and executed in Kenya by the Independent Electoral and Boundaries Commission.",
                        "url": "https://www.youtube.com/watch?v=bO7FQsCcbD8"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Technological Safeguards: BVR, KIEMS, and Digital Transmission",
                    "content": {
                        "text": (
                            "To eliminate historical vulnerabilities such as dead voters casting ballots ('ghost voters') and ballot box stuffing, "
                            "Kenya introduced comprehensive electoral technology under Section 44 of the Elections Act:\n\n"
                            "- **Biometric Voter Registration (BVR):** Captures ten fingerprints and digital facial photos to prevent duplicate registrations.\n"
                            "- **Kenya Integrated Elections Management System (KIEMS):** Electronic tablet kits deployed at every polling station on election day "
                            "to verify voters biometrically before issuing ballot papers.\n"
                            "- **Public Web Portal Transmission:** The presiding officer snaps an encrypted digital image of the signed physical Form 34A "
                            "and transmits it directly from the polling station via satellite or cellular network to the national tallying center and public portal."
                        )
                    }
                }
            ],

            # Card 6: Source Analysis & Applied Exercise
            [
                {
                    "type": "source_analysis",
                    "title": "Source Analysis: Article 88 of the Constitution",
                    "content": {
                        "source_text": (
                            "\"There is established the Independent Electoral and Boundaries Commission. "
                            "The Commission is responsible for conducting or supervising referenda and elections to any elective body or office "
                            "established by this Constitution, and any other elections as prescribed by an Act of Parliament... "
                            "The Commission shall exercise its functions in accordance with this Constitution and national legislation, "
                            "and is not subject to direction or control by any person or authority.\""
                        ),
                        "provenance": "Constitution of Kenya (2010), Article 88(1), (4), and (5).",
                        "context": "Enacted after the 2007-2008 electoral crisis to ensure institutional neutrality and operational independence.",
                        "questions": [
                            "Why is institutional autonomy ('not subject to direction or control') essential for an electoral commission?",
                            "How does the constitutional mandate of the IEBC protect minority communities during boundary delimitation?"
                        ]
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Civic Mapping Exercise: Electoral Offices in Kenya",
                    "content": {
                        "instructions": (
                            "In your notebook or small discussion group, map the six elective offices chosen during a Kenyan General Election. "
                            "Classify them into two distinct levels of government: National Government (President, Senator, MP, Woman Representative) "
                            "and County Government (Governor, Member of County Assembly)."
                        )
                    }
                }
            ],

            # Card 7: Formative Assessment & Misconceptions
            [
                {
                    "type": "misconception_card",
                    "title": "Electoral Misconception vs. Reality",
                    "content": {
                        "misconception": "The IEBC has the final legal authority to resolve presidential election outcome disputes and declare a disputed election null and void.",
                        "correction": "While the IEBC resolves nomination and campaign conduct disputes, the Constitution vests exclusive original jurisdiction in the Supreme Court of Kenya (Article 140) to determine petitions challenging presidential election results."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: IEBC Constitutional Role",
                    "content": {
                        "question": "Which of the following is a primary constitutional function of the Independent Electoral and Boundaries Commission (IEBC) under Article 88 of the Constitution?",
                        "options": [
                            "A. Appointing judges to hear parliamentary election petitions in the High Court",
                            "B. Delimiting electoral boundaries for constituencies and county wards",
                            "C. Drafting statutory legislation to govern political party financing in Parliament",
                            "D. Settling constitutional disputes regarding the validity of a presidential election"
                        ],
                        "correct_answer": "B",
                        "explanation": "Option B is correct because boundary delimitation (reviewing and establishing constituency and ward borders) is explicitly assigned to the IEBC under Article 88(4)(c) of the Constitution of Kenya. Option A is handled by the Judicial Service Commission, Option C is the mandate of Parliament, and Option D is the exclusive jurisdiction of the Supreme Court under Article 140."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Sequence of the Electoral Cycle",
                    "content": {
                        "question": "What is the correct chronological sequence of the phases in the Kenyan electoral process?",
                        "options": [
                            "A. Voter Registration → Candidate Nomination → Campaigning → Polling Day → Tallying and Announcement",
                            "B. Candidate Nomination → Voter Registration → Campaigning → Polling Day → Tallying and Announcement",
                            "C. Voter Registration → Campaigning → Candidate Nomination → Polling Day → Tallying and Announcement",
                            "D. Candidate Nomination → Campaigning → Voter Registration → Polling Day → Tallying and Announcement"
                        ],
                        "correct_answer": "A",
                        "explanation": "Option A is correct. The electoral cycle begins with establishing the voters' roll through biometric voter registration, followed by party primaries and candidate clearance (nomination), official campaigning, voting on polling day, and transparent counting, tallying, and declaration of results."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Why Elections Matter
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Why Elections Matter",
        "unit_description": "The democratic necessity of regular elections, sovereign power under Article 1, the democratic accountability cycle, and constitutional principles under Article 81.",
        "lesson_title": "Why Elections Matter",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Democratic Governance and Representation: The Voice of the Sovereign",
                    "content": {
                        "title": "Parliament of Kenya in Nairobi",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Parliament_of_Kenya_building.jpg/800px-Parliament_of_Kenya_building.jpg",
                        "caption": "The Parliament of Kenya in Nairobi, where elected representatives exercise delegated sovereign authority on behalf of the Kenyan people.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Voice of the Sovereign: Article 1 of the Constitution",
                    "content": {
                        "text": (
                            "What would happen if a government could remain in power indefinitely without ever seeking the consent of its citizens? "
                            "Throughout world history, regimes lacking public accountability have inevitably collapsed into authoritarianism, corruption, "
                            "and economic decay.\n\n"
                            "In Kenya, **Article 1 of the Constitution** explicitly declares that **all sovereign power belongs to the people of Kenya**. "
                            "Citizens may exercise this sovereign power either directly through referenda and civic participation, or indirectly through "
                            "democratically elected representatives chosen in regular, free, and fair elections."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain why periodic, competitive elections are vital to democratic governance and national stability\n"
                            "- Diagram and analyze the five stages of the **Democratic Accountability Cycle**\n"
                            "- Evaluate the general principles for the electoral system established under **Article 81 of the Constitution**\n"
                            "- Discuss how the secret ballot protects individual voters from coercion, intimidation, and bribery\n"
                            "- Formulate practical strategies for practicing informed, policy-driven voting"
                        )
                    }
                }
            ],

            # Card 2: Foundational Purposes of Democratic Elections
            [
                {
                    "type": "concept_explanation",
                    "title": "The Five Foundational Pillars of Democratic Elections",
                    "content": {
                        "text": (
                            "Elections are far more than administrative logistics; they serve foundational political and social functions:\n\n"
                            "1. **Legitimizing Public Authority:** Leaders derive their moral and legal right to govern directly from the freely expressed consent of the governed.\n"
                            "2. **Ensuring Government Accountability:** Periodic elections act as an institutional 'performance audit.' Performing leaders are rewarded with re-election, while ineffective leaders are peacefully voted out.\n"
                            "3. **Facilitating Peaceful Transitions of Power:** Elections provide a predictable, rule-bound mechanism for transferring state power without recourse to military coups or civil strife.\n"
                            "4. **Inclusive Representation for Diverse Voices:** Campaigns and proportional representation mechanisms ensure women, youth, persons with disabilities, and marginalized groups participate in national decision-making.\n"
                            "5. **Deepening the Rule of Law and Civic Trust:** Free, fair, and credible polls strengthen institutional legitimacy and public trust in democratic state organs."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Democratic Elections vs. Authoritarian Governance",
                    "content": {
                        "headers": ["Governance Dimension", "Constitutional Democratic Elections", "Authoritarian / One-Party Rule"],
                        "rows": [
                            ["Source of Power", "Sovereign citizens through universal adult suffrage", "Coercion, elite decree, or military force"],
                            ["Accountability Mechanism", "Regular 5-year competitive performance review", "No independent performance audits or recall mechanism"],
                            ["Power Transition", "Peaceful, institutional transfer via ballot box", "Violent upheavals, palace coups, or lifetime presidencies"],
                            ["Civic Participation", "Open manifestos, multi-party debate, free press", "Suppressed opposition, state propaganda, censored dissent"],
                            ["Human Rights Protection", "Protected under a robust, enforceable Bill of Rights", "Subordinated to executive power and regime survival"]
                        ]
                    }
                }
            ],

            # Card 3: The Democratic Accountability Engine
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Democratic Accountability Cycle",
                    "content": {
                        "title": "Democratic Accountability Loop",
                        "svg_content": SVG_DEMOCRATIC_ACCOUNTABILITY_CYCLE,
                        "caption": "The closed-loop cycle illustrating how citizens' sovereign power is translated into policy through periodic free elections."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Mechanism of the Accountability Cycle",
                    "content": {
                        "text": (
                            "The **Democratic Accountability Cycle** functions as a self-correcting feedback mechanism in a constitutional republic:\n\n"
                            "- **Stage 1: Sovereign Power:** Citizens hold supreme authority under Article 1.\n"
                            "- **Stage 2: Periodic Elections:** Every five years, citizens delegate authority through universal adult suffrage.\n"
                            "- **Stage 3: Governance & Legislation:** Elected leaders form government, manage public funds, and enact laws.\n"
                            "- **Stage 4: Policy Delivery:** Public services (healthcare, roads, education, security) are implemented at national and county levels.\n"
                            "- **Stage 5: Citizen Evaluation & Feedback:** Citizens audit performance, leading back to Stage 1 where non-performers are voted out and performers are renewed."
                        )
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Sovereign Power & Social Contract",
                    "content": {
                        "term": "The Social Contract in Modern Constitutionalism",
                        "definition": "The philosophical and legal understanding that citizens grant state officials the authority to govern, collect taxes, and maintain order in exchange for the protection of fundamental human rights, public welfare, and transparent accountability."
                    }
                }
            ],

            # Card 4: Primary Source Analysis: Article 81
            [
                {
                    "type": "source_analysis",
                    "title": "Primary Source Analysis: Article 81 of the Constitution",
                    "content": {
                        "source_text": (
                            "\"The electoral system shall comply with the following principles—\n"
                            "(a) freedom of citizens to exercise their political rights under Article 38;\n"
                            "(b) not more than two-thirds of the members of elective public bodies shall be of the same gender;\n"
                            "(c) fair representation of persons with disabilities;\n"
                            "(d) universal suffrage based on the aspiration for fair representation and equality of vote; and\n"
                            "(e) free and fair elections, which are—\n"
                            "  (i) by secret ballot;\n"
                            "  (ii) free from violence, intimidation, improper influence or corruption;\n"
                            "  (iii) conducted by an independent body;\n"
                            "  (iv) transparent; and\n"
                            "  (v) administered in an impartial, neutral, efficient, accurate and accountable manner.\""
                        ),
                        "provenance": "Constitution of Kenya (2010), Chapter Seven, Article 81.",
                        "context": "The constitutional benchmark governing all elective offices and electoral administration in Kenya.",
                        "questions": [
                            "Why does Article 81(e)(i) explicitly mandate voting by 'secret ballot'?",
                            "How does the two-thirds gender principle in Article 81(b) address historical marginalization in Kenya's legislature?",
                            "What does 'equality of vote' mean for voters across different constituencies?"
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Critical Role of the Secret Ballot",
                    "content": {
                        "text": (
                            "The **secret ballot** is an indispensable safeguard of voter autonomy. When a voter marks their ballot in a private, "
                            "shielded voting booth, no employer, landlord, community leader, or politician can verify how that individual voted.\n\n"
                            "This privacy eliminates the threat of post-election retaliation, prevents voter intimidation, and renders vote-buying "
                            "ineffective, because a candidate cannot guarantee that a bribed voter actually voted for them in the secrecy of the booth."
                        )
                    }
                }
            ],

            # Card 5: Video Masterclass & Civic Empowerment
            [
                {
                    "type": "suggested_video",
                    "title": "Video: Why Every Vote Matters in a Democracy",
                    "content": {
                        "title": "The Power of Civic Participation and Electoral Accountability",
                        "youtube_id": "fTTGALaRZoc",
                        "description": "An inspiring breakdown of how democratic voting transforms communities, holds public leaders accountable, and secures future generations.",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Youth Civic Engagement and Combating Voter Apathy",
                    "content": {
                        "text": (
                            "Voter apathy—the belief that 'my single vote will not change anything'—is one of the greatest dangers facing modern democracies. "
                            "In Kenya, youth constitute over 60% of the population. When young citizens fail to register or turn out to vote, they surrender "
                            "their constitutional power to make crucial decisions about youth employment, education funding, healthcare, and national debt."
                        )
                    }
                }
            ],

            # Card 6: Real-World Application: The Informed Voter's Checklist
            [
                {
                    "type": "step_process",
                    "title": "The 4-Step Checklist for Informed Voting",
                    "content": {
                        "steps": [
                            {
                                "step": 1,
                                "name": "Analyze Policy Manifestos",
                                "description": "Read the written manifestos of candidates. Check whether policy proposals are realistic, costed, sustainable, and aligned with public interest rather than empty slogans."
                            },
                            {
                                "step": 2,
                                "name": "Audit Leadership Track Records",
                                "description": "Examine candidates' past public conduct, Chapter Six integrity compliance, professional background, and commitment to anti-corruption."
                            },
                            {
                                "step": 3,
                                "name": "Fact-Check Campaign Claims",
                                "description": "Verify political statements and social media allegations using credible news outlets, fact-checking platforms, and official government audit reports."
                            },
                            {
                                "step": 4,
                                "name": "Practice Political Tolerance",
                                "description": "Respect the constitutional right of fellow citizens to support different candidates and engage in peaceful, respectful democratic debate."
                            }
                        ]
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Classroom Activity: Manifesto Evaluation Matrix",
                    "content": {
                        "instructions": (
                            "Form pairs and evaluate two hypothetical school council manifestos: Candidate X promises 'Free snacks every Friday' "
                            "with no budget plan, while Candidate Y proposes 'A peer-tutoring academic library program funded by student recycling.' "
                            "Which candidate exhibits sustainable leadership, and why?"
                        )
                    }
                }
            ],

            # Card 7: Formative Assessment & Misconceptions
            [
                {
                    "type": "misconception_card",
                    "title": "Misconception: Apathy vs. Democratic Power",
                    "content": {
                        "misconception": "In a constituency with hundreds of thousands of voters, one person's vote is insignificant and has no effect on governance.",
                        "correction": "Numerous parliamentary and civic elections in Kenya have been decided by margins as thin as one or two votes. Furthermore, collective voter turnout determines the legitimacy and policy priorities of the elected administration."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Constitutional Principles (Article 81)",
                    "content": {
                        "question": "Under Article 81 of the Constitution of Kenya (2010), which of the following is an explicit constitutional requirement for the electoral system?",
                        "options": [
                            "A. General elections must be conducted strictly via online electronic voting platforms",
                            "B. Not more than two-thirds of the members of elective public bodies shall be of the same gender",
                            "C. Political parties must receive equal campaign financing from the national exchequer",
                            "D. Presidential term limits are automatically extended during economic emergencies"
                        ],
                        "correct_answer": "B",
                        "explanation": "Option B is correct because Article 81(b) explicitly establishes the two-thirds gender principle, mandating that not more than two-thirds of the members of elective public bodies shall be of the same gender. Options A, C, and D are factually and constitutionally incorrect."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Purpose of the Secret Ballot",
                    "content": {
                        "question": "How does the constitutional requirement of a 'secret ballot' directly safeguard a citizen's democratic rights?",
                        "options": [
                            "A. It ensures that the tallying process is hidden from international election observers",
                            "B. It keeps the final election results secret until the President approves them",
                            "C. It prevents employers, politicians, or community actors from coercing, intimidating, or punishing a voter for their choice",
                            "D. It allows the IEBC to alter ballot results without public scrutiny"
                        ],
                        "correct_answer": "C",
                        "explanation": "Option C is correct. The secret ballot ensures that an individual voter marks their ballot in complete privacy, eliminating the risk of intimidation, retribution, or coercion by powerful actors or political figures. Options A, B, and D violate the constitutional principles of transparency and public accountability."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Malpractice, Integrity, and Prevention
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Malpractice, Integrity, and Prevention",
        "unit_description": "Forms and root causes of electoral malpractices, technological and institutional safeguards, and the five core ethical values of electoral integrity.",
        "lesson_title": "Malpractice, Integrity, and Prevention",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Biometric Verification: Technology Safeguarding the Ballot",
                    "content": {
                        "title": "IEBC Official Utilizing Biometric Verification",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Kenyan_elections_2013.jpg/800px-Kenyan_elections_2013.jpg",
                        "caption": "An IEBC election official verifying a voter biometrically at a polling station, deploying technological safeguards to prevent impersonation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Poison in the Well: Understanding Electoral Malpractice",
                    "content": {
                        "text": (
                            "What happens when an athlete in an Olympic race takes illegal performance-enhancing drugs, or a student cheats "
                            "on a national examination? The entire competition loses its legitimacy, and the results are rightly rejected.\n\n"
                            "Similarly, **electoral malpractices** are illegal, fraudulent, or unethical actions that corrupt the voting process. "
                            "Malpractices rob citizens of their true democratic voice, distort governance, and create deep social grievances "
                            "that can ignite violent civil conflict if left unaddressed."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify and classify the major forms of electoral malpractice (bribery, intimidation, rigging, disinformation)\n"
                            "- Trace the causal chain connecting electoral fraud to post-election violence and socio-economic breakdown\n"
                            "- Evaluate the technological and institutional safeguards deployed by the IEBC and law enforcement\n"
                            "- Examine the five core ethical values of electoral integrity depicted in the Integrity Star\n"
                            "- Apply critical thinking to identify and counter digital campaign disinformation ('fake news')"
                        )
                    }
                }
            ],

            # Card 2: Typology and Consequences of Malpractices
            [
                {
                    "type": "concept_explanation",
                    "title": "Major Forms of Electoral Malpractice",
                    "content": {
                        "text": (
                            "Electoral malpractices occur across all stages of the electoral cycle:\n\n"
                            "1. **Voter Bribery & Coercion:** Handing out cash, food, or alcohol to induce voters to vote for a specific candidate, exploiting economic vulnerability.\n"
                            "2. **Intimidation & Violence:** Deploying youth gangs or state organs to threaten opponents and suppress voter turnout in rival strongholds.\n"
                            "3. **Voter Impersonation & Multiple Voting:** Attempting to vote using another person's national identity card or deceased persons' names.\n"
                            "4. **Tallying Manipulation (Rigging):** Forging signatures, tampering with ballot boxes, altering Form 34A entries, or hacking electronic transmission systems.\n"
                            "5. **Campaign Disinformation & Hate Speech:** Weaponizing tribal sentiments, spreading falsified videos, and inciting ethnic hostility on digital platforms."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Electoral Malpractices, Modus Operandi, and Legal Consequences",
                    "content": {
                        "headers": ["Malpractice Type", "Modus Operandi", "Statutory Sanctions under Elections Offences Act"],
                        "rows": [
                            ["Voter Bribery", "Distributing money, gifts, or favors to voters during campaigns", "Fine up to KES 2,000,000, 6 years imprisonment, disqualification"],
                            ["Electoral Violence", "Hiring gangs, disrupting rallies, harassing female contenders", "Criminal prosecution, disqualification of candidate, jail term"],
                            ["Vote Impersonation", "Voting under a stolen or deceased voter's ID credentials", "Immediate arrest, prosecution, and imprisonment up to 5 years"],
                            ["Form Tampering", "Altering figures on statutory results forms (Form 34A/34B)", "Disqualification of returning officer, heavy fines, criminal record"],
                            ["Hate Speech / Fake News", "Broadcasting ethnic slurs and fabricated stories online", "Prosecution under NCIC Act and Computer Misuse & Cybercrimes Act"]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Causal Chain of Malpractice: Lessons from 2007",
                    "content": {
                        "text": (
                            "When electoral integrity fails, the consequences for a nation are catastrophic. The tragic aftermath of the "
                            "**2007 General Election in Kenya** demonstrated how electoral malpractices, coupled with inflammatory rhetoric "
                            "and ethnic polarization, can lead to the loss of over 1,000 lives, the displacement of over 600,000 citizens, "
                            "and immense economic disruption. Preventing electoral fraud is therefore a matter of supreme national security."
                        )
                    }
                }
            ],

            # Card 3: Institutional & Technological Safeguards
            [
                {
                    "type": "concept_explanation",
                    "title": "Institutional and Technological Safeguards",
                    "content": {
                        "text": (
                            "To systematically dismantle opportunities for electoral malpractice, Kenya has instituted rigorous institutional safeguards:\n\n"
                            "- **KIEMS Biometric De-duplication:** On election day, the KIEMS kit identifies voters biometrically. Once a voter's biometric "
                            "record is verified, the kit immediately locks their status, preventing double-voting.\n"
                            "- **Public Web Portal Transparency:** Every Form 34A scanned at polling stations is transmitted directly to a public website, "
                            "allowing media houses, political parties, observers, and citizens to independently compute tallies.\n"
                            "- **Multi-Party Agents at Every Station:** By law, each political party and independent candidate has accredited agents "
                            "present inside the polling room from ballot opening through counting and signing.\n"
                            "- **Judicial Specialization:** The Judiciary establishes specialized Election Dispute Resolution (EDR) benches to arbitrate "
                            "petitions within constitutionally mandated time limits (e.g., 14 days for presidential petitions under Article 140)."
                        )
                    }
                },
                {
                    "type": "definition_card",
                    "title": "BVR vs. KIEMS in Kenya's Electoral Architecture",
                    "content": {
                        "term": "BVR vs. KIEMS Systems",
                        "definition": "**BVR (Biometric Voter Registration)** is the database system used prior to elections to record voter biometrics and eliminate ghost voters. **KIEMS (Kenya Integrated Elections Management System)** is the integrated software and hardware kit used on polling day to verify voters, manage logistics, and transmit scanned results forms."
                    }
                }
            ],

            # Card 4: The Core Values of Electoral Integrity
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Core Values of Electoral Integrity Star",
                    "content": {
                        "title": "Electoral Integrity Star",
                        "svg_content": SVG_CORE_VALUES_INTEGRITY_STAR,
                        "caption": "The five core civic values required to eliminate electoral malpractices and protect democratic legitimacy."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Five Pillars of Civic Character",
                    "content": {
                        "text": (
                            "While technology is a powerful deterrent, the ultimate defense of free elections is the **ethical character of citizens and leaders**:\n\n"
                            "1. **Integrity (Honesty):** Refusing to offer or receive bribes, and standing firm for truthful counting even when unmonitored.\n"
                            "2. **Transparency (Openness):** Administering all counting, tallying, and procurement openly in full public view.\n"
                            "3. **Fairness (Justice):** Providing equal campaign ground, impartial security, and objective media coverage for all contenders.\n"
                            "4. **Tolerance (Peace):** Recognizing that political opponents are fellow citizens with differing ideas, not enemies to be destroyed.\n"
                            "5. **Civic Duty (Responsibility):** Actively participating in elections, fact-checking information, and reporting irregularities to law enforcement."
                        )
                    }
                }
            ],

            # Card 5: Video Masterclass & Investigative Inquiry
            [
                {
                    "type": "suggested_video",
                    "title": "Video: Combating Electoral Malpractice and Disinformation",
                    "content": {
                        "title": "Detecting Electoral Fraud, Hate Speech, and Fake News",
                        "youtube_id": "rNu8XDBSn10",
                        "description": "An investigative look into the methods used to detect electoral malpractices, counter fake news, and protect community peace during heated national elections.",
                        "url": "https://www.youtube.com/watch?v=rNu8XDBSn10"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Digital Literacy: Spotting Political Disinformation",
                    "content": {
                        "text": (
                            "In modern elections, **disinformation** has emerged as a dangerous form of malpractice. Unscrupulous political actors use "
                            "manipulated images, out-of-context videos ('cheapfakes'), and bot networks to incite tribal animosity or spread false tally numbers.\n\n"
                            "Informed citizens must practice digital hygiene: verify image sources using reverse-image search, check multiple credible media outlets, "
                            "and never share unverified sensational claims during vote counting."
                        )
                    }
                }
            ],

            # Card 6: Ethical Dilemmas & Mini-Activity
            [
                {
                    "type": "source_analysis",
                    "title": "Source Analysis: The Elections Offences Act",
                    "content": {
                        "source_text": (
                            "\"A person who directly or indirectly, by himself or by any other person on his behalf, "
                            "gives, lends or agrees to give or lend, or offers, promises, or promises to procure or to endeavour to procure, "
                            "any money or valuable consideration to or for any voter... in order to induce any voter to vote or refrain from voting, "
                            "commits the offence of bribery and is liable on conviction to a fine not exceeding two million shillings or to imprisonment for a term not exceeding six years or to both.\""
                        ),
                        "provenance": "Elections Offences Act No. 37 of 2016, Section 9(1).",
                        "context": "Strict statutory penalties established by Parliament to criminalize voter bribery and protect electoral integrity.",
                        "questions": [
                            "Why does the law penalize both the candidate who gives a bribe and the voter who accepts it?",
                            "How does voter bribery undermine economic development in a constituency over a 5-year term?"
                        ]
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Interactive Case Study: The Midnight Delivery",
                    "content": {
                        "instructions": (
                            "Scenario: On the eve of polling day, a local campaign team arrives in your neighborhood distributing bags of maize "
                            "flour and 1,000-shilling notes stamped with a candidate's portrait. In groups of three, discuss: (1) Which specific "
                            "law is being violated? (2) What is the responsible civic action for a citizen to take?"
                        )
                    }
                }
            ],

            # Card 7: Formative Assessment & Misconceptions
            [
                {
                    "type": "misconception_card",
                    "title": "Misconception: 'Eat Their Money but Vote Your Choice'",
                    "content": {
                        "misconception": "If a corrupt candidate offers you money or food during a campaign, it is acceptable to take the gift as long as you secretly vote for your preferred ethical candidate.",
                        "correction": "Accepting a bribe is a serious criminal offense under the Elections Offences Act and Bribery Act. Taking bribes normalizes money-driven politics, encourages wealthy corrupt actors to run, and excludes honest leaders who refuse to buy votes."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Technology in Polling Verification",
                    "content": {
                        "question": "Which electronic system is deployed by the IEBC at polling stations on election day to verify voters biometrically and prevent double-voting?",
                        "options": [
                            "A. Integrated Financial Management Information System (IFMIS)",
                            "B. Kenya Integrated Elections Management System (KIEMS)",
                            "C. National Transport and Safety Authority Portal (TIMS)",
                            "D. National Integrated Identity Management System (NIIMS)"
                        ],
                        "correct_answer": "B",
                        "explanation": "Option B is correct. The KIEMS kit is the specialized electronic tablet deployed to each polling station on polling day to verify registered voters biometrically using fingerprints/facial photos and transmit scanned Form 34A results. IFMIS is for public financial accounting, TIMS is for transport licensing, and NIIMS was a civil registration project."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Social Consequences of Malpractice",
                    "content": {
                        "question": "What is the primary danger posed by political actors spreading hate speech and unverified election disinformation during campaigns?",
                        "options": [
                            "A. It triggers ethnic polarization, undermines civic trust, and can provoke violent civil conflict",
                            "B. It automatically forces the IEBC to extend the voting period across the country",
                            "C. It increases voter turnout and improves public scrutiny of government spending",
                            "D. It legally obligates the Supreme Court to cancel the national voters register"
                        ],
                        "correct_answer": "A",
                        "explanation": "Option A is correct. Disinformation and hate speech exploit ethnic and political divisions, eroding public trust in democratic institutions and creating dangerous conditions for post-election violence. Options B, C, and D are factually and legally incorrect."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Election Peace Simulation (Inquiry Lab)
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Election Peace Simulation (Inquiry Lab)",
        "unit_description": "Collaborative dispute resolution simulation in contested constituency 'Amani County', multi-stakeholder roleplay, evidence dossier analysis, and peace accord drafting.",
        "lesson_title": "Election Peace Simulation (Inquiry Lab)",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "National Peace and Constitutional Order: The Amani Simulation",
                    "content": {
                        "title": "National Coat of Arms of Kenya: Harambee and Justice",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg",
                        "caption": "The sovereign symbols of Kenya represent national unity, peace, justice, and the rule of law during moments of democratic contestation.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain / CC BY-SA"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Welcome to the Amani County Simulation Arena",
                    "content": {
                        "text": (
                            "Welcome to the VLearn **Election Peace Simulation**. In this collaborative inquiry lab, you will step into the shoes "
                            "of critical stakeholders in a simulated Kenyan constituency called **Amani County**.\n\n"
                            "A fiercely contested parliamentary election has just concluded. Preliminary counts show Candidate A leading Candidate B "
                            "by a razor-thin margin of only 150 votes. At that moment, a rumor explodes on social media alleging that ballot boxes "
                            "at **Polling Station 03** were stuffed and that the ballot box seal was broken. Agitated youths are gathering outside "
                            "the tallying center. As stakeholders, your mission is to de-escalate tension and resolve the crisis lawfully."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Simulation Inquiry Outcomes",
                    "content": {
                        "text": (
                            "By the end of this collaborative simulation, you will be able to:\n\n"
                            "- Embody one of four key stakeholder roles (Returning Officer, Party Agent, Peace Monitor, Security Commander)\n"
                            "- Analyze a multi-source **Evidence Dossier** to separate verifiable facts from inflammatory rumors\n"
                            "- Apply Articles 81, 82, and 88 of the Constitution to resolve polling station discrepancies lawfully\n"
                            "- Execute a 3-phase crisis de-escalation workflow\n"
                            "- Draft a binding **Amani County Multi-Party Peace Accord**"
                        )
                    }
                }
            ],

            # Card 2: Stakeholder Roles and Mandates
            [
                {
                    "type": "comparison_table",
                    "title": "Amani County Stakeholder Profiles and Constraints",
                    "content": {
                        "headers": ["Stakeholder Group", "Core Mission & Primary Mandate", "Key Operational Constraint / Concern"],
                        "rows": [
                            ["IEBC Constituency Returning Officer", "Maintain tally integrity, enforce Elections Act, and ensure transparency", "Cannot announce unverified figures, but must avoid delays that spark riots"],
                            ["Candidate A Party Agents (Incumbent)", "Protect narrow lead, ensure valid votes are credited, keep supporters calm", "Fears opponent is inventing false claims to overturn a legitimate win"],
                            ["Candidate B Party Agents (Challenger)", "Examine Polling Station 03 irregularities, demand verification of broken seal", "Supporters are emotional and distrustful of IEBC officials"],
                            ["NCIC Peace Monitors & Community Elders", "Diffuse public tensions, fact-check rumors, mediate between candidate teams", "Have moral authority but no legal power to alter or certify vote counts"],
                            ["National Police Service Commander", "Secure tallying center perimeter, protect officials and ballot materials", "Must maintain crowd control using de-escalation, avoiding excessive force"]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Understanding Competing Pressures in High-Stakes Tallying",
                    "content": {
                        "text": (
                            "During election tallying, every stakeholder operates under severe emotional and political pressures. "
                            "The Returning Officer must strictly follow the statutory verification steps laid down in the Elections Act. "
                            "Party agents must be vigilant without obstructing the process, and community peace monitors must provide "
                            "objective verification to prevent street mobilization."
                        )
                    }
                }
            ],

            # Card 3: The Evidence Dossier (Inquiry Lab)
            [
                {
                    "type": "source_analysis",
                    "title": "Evidence Dossier: Card 1 — Disputed Form 34A",
                    "content": {
                        "source_text": (
                            "FORM 34A — POLLING STATION 03 (AMANI CONSTITUENCY):\n"
                            "• Registered Voters at Station: 450\n"
                            "• Total Valid Ballots Cast: 442\n"
                            "• Candidate A Votes: 398\n"
                            "• Candidate B Votes: 44\n"
                            "• Rejected / Spoilt Ballots: 3\n"
                            "• Total Ballots in Box: 445\n"
                            "• Signatures: Presiding Officer (Signed), Candidate A Agent (Signed).\n"
                            "• Candidate B Agent Note: 'REFUSED TO SIGN — Box seal #0482 was broken during transit from river crossing.'"
                        ),
                        "provenance": "Official Physical Form 34A, Polling Station 03, Amani Constituency.",
                        "context": "Primary statutory document under dispute at the constituency tallying center.",
                        "questions": [
                            "Does the total number of ballots cast (445) exceed the registered voter total (450)?",
                            "What explains the broken seal according to the Presiding Officer's logbook?"
                        ]
                    }
                },
                {
                    "type": "source_analysis",
                    "title": "Evidence Dossier: Card 2 & 3 — Fact-Check & Constitutional Mandate",
                    "content": {
                        "source_text": (
                            "NCIC FACT-CHECK REPORT (EVIDENCE CARD 3):\n"
                            "Viral social media image showing an open ballot box on a motorbike was verified via reverse-image search. "
                            "Finding: The photo is from a 2018 municipal poll in another country and is completely fabricated in relation to Amani County.\n\n"
                            "CONSTITUTIONAL MANDATE (EVIDENCE CARD 2 - ARTICLE 82):\n"
                            "The voting process must be simple, accurate, verifiable, secure, transparent, and accountable. Discrepancies must be audited using verifiable digital records."
                        ),
                        "provenance": "National Cohesion and Integration Commission (NCIC) Field Report & Article 82 of Constitution.",
                        "context": "Crucial evidence establishing the falsity of the viral rumor and the legal requirement for transparent verification.",
                        "questions": [
                            "How should the fact-check result be communicated to the crowd outside?",
                            "What digital record can be compared against the physical Form 34A?"
                        ]
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Form 34A vs. Form 34B",
                    "content": {
                        "term": "Form 34A & Form 34B",
                        "definition": "**Form 34A** is the primary statutory results form filled and signed at each individual polling station. **Form 34B** is the constituency collation summary form where the Returning Officer aggregates all Form 34As from all stations within the constituency."
                    }
                }
            ],

            # Card 4: Simulation Map and Dispute Resolution Framework
            [
                {
                    "type": "suggested_diagram",
                    "title": "Amani County Peace Simulation Map",
                    "content": {
                        "title": "Simulation Arena Resolution Map",
                        "svg_content": SVG_ELECTION_PEACE_SIMULATION_MAP,
                        "caption": "The multi-stakeholder dispute resolution protocol deployed to de-escalate crisis in Amani County."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Multi-Track De-escalation Protocol",
                    "content": {
                        "text": (
                            "Resolving an election crisis requires three simultaneous tracks working in harmony:\n\n"
                            "1. **Information Track:** Quelling viral disinformation immediately with verified facts presented jointly by all sides.\n"
                            "2. **Administrative Track:** Auditing the physical Form 34A against the encrypted digital scan transmitted by the KIEMS kit in full view of candidate agents.\n"
                            "3. **Legal Track:** Directing any unresolved grievances to the High Court election petition process, completely removing conflict from the streets."
                        )
                    }
                }
            ],

            # Card 5: Video Masterclass on Electoral Dispute Resolution
            [
                {
                    "type": "suggested_video",
                    "title": "Video: Constitutional Dispute Resolution in Kenya",
                    "content": {
                        "title": "How the Judiciary Resolves Contested Elections Peacefully",
                        "youtube_id": "T_sGTspaF4Y",
                        "description": "An in-depth look at Kenya's election dispute resolution mechanisms, judicial petitions, and how the rule of law safeguards national stability.",
                        "url": "https://www.youtube.com/watch?v=T_sGTspaF4Y"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Supremacy of Judicial Petitions Over Violence",
                    "content": {
                        "text": (
                            "Under Kenya's constitutional framework, no candidate or political party has the right to use violence or civil unrest "
                            "to contest an election result. The Constitution establishes specialized election courts:\n\n"
                            "- **High Court:** Hears and determines petitions for parliamentary seats (National Assembly & Senate) and County Governors within 6 months.\n"
                            "- **Resident Magistrate Courts:** Hear petitions challenging Member of County Assembly (MCA) elections.\n"
                            "- **Supreme Court:** Hears and determines petitions challenging the election of the President within 14 days under Article 140."
                        )
                    }
                }
            ],

            # Card 6: Interactive Simulation Tasks (Action Plan)
            [
                {
                    "type": "step_process",
                    "title": "The 3-Step Simulation Resolution Action Plan",
                    "content": {
                        "steps": [
                            {
                                "step": 1,
                                "name": "Step 1: Fact-Checking & Joint Public Briefing",
                                "description": "The NCIC Monitor and Returning Officer present the reverse-image fact-check to Candidates A and B. Candidates issue a joint live broadcast to their supporters outside debunking the fake photo."
                            },
                            {
                                "step": 2,
                                "name": "Step 2: Transparent Digital Form 34A Audit",
                                "description": "The Returning Officer projects the encrypted Form 34A scanned directly from the KIEMS kit at Polling Station 03. Party agents inspect the polling logbook explaining that the seal broke during heavy rain river transport but the serial tally matches perfectly."
                            },
                            {
                                "step": 3,
                                "name": "Step 3: Signing the Amani County Peace Accord",
                                "description": "Both candidate teams sign a binding Peace Accord pledging to accept the verified tally and pursue any lingering legal challenges exclusively through the High Court."
                            }
                        ]
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Simulation Exercise: Drafting the Peace Accord",
                    "content": {
                        "instructions": (
                            "In your stakeholder teams, draft the 3 key clauses of the Amani County Peace Accord: "
                            "Clause 1: Public commitment to non-violence; "
                            "Clause 2: Respect for the verified constitutional tally; "
                            "Clause 3: Pledge to file grievances exclusively in the High Court within statutory deadlines."
                        )
                    }
                }
            ],

            # Card 7: Reflection, Debrief, & Formative Assessment
            [
                {
                    "type": "misconception_card",
                    "title": "Misconception: Settling Disputes on the Street",
                    "content": {
                        "misconception": "If an election outcome is disputed by a candidate's supporters, staging street riots and blocking tallying centers is a legitimate way to force a recount.",
                        "correction": "Street protests that disrupt tallying or destroy property are illegal under the Elections Act and Penal Code. The Constitution establishes peaceful, transparent judicial channels (Election Dispute Resolution) with the power to order recounts, scrutinize ballot boxes, or nullify tainted elections."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Lawful Dispute Resolution",
                    "content": {
                        "question": "What is the constitutionally mandated method for a parliamentary candidate in Kenya to challenge a disputed election result declared by the IEBC?",
                        "options": [
                            "A. Mobilizing armed youth to storm the national tallying center and seize the ballot boxes",
                            "B. Filing a formal election petition in the High Court of Kenya within 28 days of declaration",
                            "C. Declaring themselves the winner in an unofficial parallel swearing-in ceremony",
                            "D. Requesting the National Police Service to arrest the Returning Officer immediately"
                        ],
                        "correct_answer": "B",
                        "explanation": "Option B is correct. Under Article 105 of the Constitution and the Elections Act, any dispute concerning parliamentary election results must be resolved by filing an election petition in the High Court within 28 days of the official declaration. Options A, C, and D are illegal, unconstitutional, and subvert the rule of law."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Countering Disinformation",
                    "content": {
                        "question": "In the Amani County simulation, why was it vital for the NCIC Monitor and IEBC Returning Officer to conduct an immediate reverse-image fact-check of the viral social media post?",
                        "options": [
                            "A. To prove that social media platforms should be permanently shut down nationwide",
                            "B. To prevent fabricated rumors from inciting street panic and violence among rival party supporters",
                            "C. To allow the police commander to shoot protesters without legal accountability",
                            "D. To alter the official figures on Form 34A without party agent supervision"
                        ],
                        "correct_answer": "B",
                        "explanation": "Option B is correct. Rapid fact-checking debunked the fabricated 2018 image, preventing false rumors from inflaming public emotion and triggering destructive street clashes outside the tallying center. Options A, C, and D are factually and ethically incorrect."
                    }
                }
            ]
        ]
    }
]
