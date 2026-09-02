"""
VLearn CBC Grade 10 History — Topic 10: Great Revolutions — The French Revolution
Authoritative High-Structure Production Curriculum Data Definitions (Lessons 1 to 4)

Subject: History
Grade: Grade 10
Curriculum: CBC
Topic Order: 10
Topic Name: "Topic 3.1: Great Revolutions — The French Revolution"
"""

from curriculum.cbc_grade10_history_topic10_svgs import (
    SVG_THREE_ESTATES_PYRAMID,
    SVG_REVOLUTIONARY_TIMELINE,
    SVG_GLOBAL_RIPPLES_1789,
    SVG_PILLARS_CIVIC_STEWARDSHIP
)

TOPIC_10_LESSONS = [
    # =========================================================================
    # LESSON 1: Context and Causes of the Revolution
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Context and Causes of the Revolution",
        "unit_description": "The social hierarchy of the Ancien Régime, fiscal insolvency, Enlightenment philosophies, and systemic triggers of the 1789 crisis.",
        "lesson_title": "Context and Causes of the Revolution",
        "pages": [
            # Page 1: Learning Outcomes & Entry Spark
            [
                {
                    "type": "learning_goal",
                    "title": "Module 3.1.1 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the social structure of the **Ancien Régime** and the systemic inequalities among the three Estates\n"
                            "- Identify the economic, environmental, and fiscal factors that triggered royal insolvency in 1789\n"
                            "- Describe how **Enlightenment** philosophies challenged the divine right of absolute monarchs\n"
                            "- Critically evaluate the role of weak royal leadership in turning a financial crisis into a political revolution"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Spark: The Powder Keg of Pre-Revolutionary France",
                    "content": {
                        "text": (
                            "Imagine living in a society where 97% of the population does all the hard physical labor, produces all the food, and pays 100% of state taxes—yet possesses absolutely zero voice in how the country is governed.\n\n"
                            "Meanwhile, the remaining 3% owns over a third of all fertile land, enjoys exclusive legal immunities, and contributes nothing in direct taxation to the state. "
                            "This was the powder keg of pre-revolutionary France, known historically as the **Ancien Régime** (the Old Regime).\n\n"
                            "When catastrophic crop failures met national financial bankruptcy in the late 1780s, this rigid, centuries-old social pyramid collapsed into one of the most explosive upheavals in world history."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Caricature of the Three Estates of Pre-Revolutionary France",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Troisordres.jpg/800px-Troisordres.jpg",
                        "author": "M. P. (Anonymous 18th-century French Engraver)",
                        "licensing": "Public Domain (1789)",
                        "caption": "An 18th-century French caricature depicting a heavily burdened peasant (the Third Estate) crawling on all fours, carrying a wealthy clergyman (the First Estate) and a sword-bearing nobleman (the Second Estate) on his back—illustrating systemic tax burdens and social oppression."
                    }
                }
            ],

            # Page 2: The Three Estates Social Hierarchy
            [
                {
                    "type": "concept_explanation",
                    "title": "The Rigid Social Pyramid: The Three Estates",
                    "content": {
                        "text": (
                            "Pre-revolutionary French society was legally partitioned into three rigid classes or orders, known as **Estates**:\n\n"
                            "1. **The First Estate (The Clergy):** Numbering approximately 130,000 (~1% of the population), the Catholic clergy owned 10% of all land in France. They collected their own agricultural tax—the **tithe** (a 10% tax on crops)—and were completely exempt from paying direct royal taxes, offering only a small, voluntary negotiated gift (*don gratuit*) to the crown.\n\n"
                            "2. **The Second Estate (The Nobility):** Comprising roughly 350,000 aristocrats (~2% of the population), the nobility owned 25% to 30% of the land. They held absolute monopolies over high government offices, military commands, and royal courts (*Parlements*). They were fully exempt from the direct land tax (*Taille*) and extracted forced peasant labor and feudal dues.\n\n"
                            "3. **The Third Estate (The Commoners):** A massive, diverse majority of 26 million people (~97% of the population). Despite creating all national wealth, they bore the entire direct tax burden while having no political power."
                        )
                    }
                },
                {
                    "type": "suggested_diagram",
                    "title": "The Social Structure of the Ancien Régime",
                    "content": {
                        "caption": "Visual social pyramid demonstrating the extreme demographic, land ownership, and tax asymmetry between the privileged 3% (Clergy & Nobility) and the overburdened 97% (Third Estate Commoners).",
                        "svg_content": SVG_THREE_ESTATES_PYRAMID
                    }
                },
                {
                    "type": "definition_card",
                    "title": "Key Historical Terminology",
                    "content": {
                        "term": "Ancien Régime & Bourgeoisie",
                        "definition": "The Ancien Régime ('Old Regime') was the feudal political and social system of France before the 1789 Revolution. The Bourgeoisie were the educated, affluent middle-class commoners (merchants, lawyers, doctors, bankers) who drove the revolution's intellectual and institutional leadership."
                    }
                }
            ],

            # Page 3: The Confluence of Crises
            [
                {
                    "type": "concept_explanation",
                    "title": "The Confluence of Four Devastating Crises (1788–1789)",
                    "content": {
                        "text": (
                            "The collapse of the French monarchy was not caused by a single isolated event, but by four intersecting crises that struck simultaneously in the late 1780s:\n\n"
                            "- **1. The Fiscal & Debt Crisis:** France was completely insolvent. Centuries of foreign warfare, culminating in France's lavish financing of the American Revolutionary War (1775–1783), drained the royal treasury. Half of all national revenue went purely toward paying interest on royal loans.\n\n"
                            "- **2. The Agrarian & Climate Crisis:** Severe droughts, unseasonable hailstorms, and harsh winters in 1788–1789 decimated harvests. Grain supplies plummeted, and the price of bread skyrocketed to over 80% of an urban laborer's daily income, causing widespread famine and riots.\n\n"
                            "- **3. The Enlightenment Intellectual Shift:** Thinkers like Rousseau and Montesquieu dismantled the divine-right justification for royal absolutism, inspiring educated commoners to demand constitutional rule and popular sovereignty.\n\n"
                            "- **4. Weak & Indecisive Leadership:** King Louis XVI was vacillating and weak, repeatedly firing reformist ministers, while Queen Marie Antoinette's extravagant spending symbolized royal detachment."
                        )
                    }
                },
                {
                    "type": "step_process",
                    "title": "The Chain Reaction to Royal Insolvency",
                    "content": {
                        "steps": [
                            {
                                "step": 1,
                                "title": "War Spending & Ballooning Debt",
                                "description": "France borrows heavily to finance the Seven Years' War and the American Revolution, accumulating insurmountable interest payments."
                            },
                            {
                                "step": 2,
                                "title": "Noble Resistance to Tax Reform",
                                "description": "Royal finance ministers (Turgot, Necker, Calonne) propose taxing noble land, but the Second Estate fiercely blocks all reforms."
                            },
                            {
                                "step": 3,
                                "title": "Severe Harvest Failure & Bread Inflation",
                                "description": "The terrible winter of 1788–1789 leaves millions of peasants and urban workers starving across Paris and the provinces."
                            },
                            {
                                "step": 4,
                                "title": "Summoning of the Estates-General",
                                "description": "With bankers refusing further credit, Louis XVI is forced to summon the Estates-General for the first time in 175 years."
                            }
                        ]
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Three Estates: Population, Land, and Tax Comparison",
                    "content": {
                        "headers": ["Estate", "Population Share", "Land Ownership", "Direct Tax Burden", "Key Privileges / Burdens"],
                        "rows": [
                            [
                                "First Estate (Clergy)",
                                "~1% (130,000)",
                                "10% of fertile land",
                                "0% (Exempt from Taille)",
                                "Collected Church tithes; controlled education and censorship"
                            ],
                            [
                                "Second Estate (Nobility)",
                                "~2% (350,000)",
                                "25% – 30% of land",
                                "0% (Exempt from direct taxes)",
                                "Held top administrative and military posts; extracted feudal dues"
                            ],
                            [
                                "Third Estate (Commoners)",
                                "~97% (26 Million)",
                                "60% – 65% of land",
                                "100% of direct taxes",
                                "Paid Taille, Gabelle, Tithes, Feudal dues, and forced labor (Corvée)"
                            ]
                        ]
                    }
                }
            ],

            # Page 4: Enlightenment Ideals vs Divine Right Monarchy
            [
                {
                    "type": "concept_explanation",
                    "title": "The Philosophical Shift: The Enlightenment",
                    "content": {
                        "text": (
                            "For centuries, European kings claimed to rule by **Divine Right**—the belief that the monarch was chosen directly by God and was accountable to no earthly authority.\n\n"
                            "During the 18th-century **Enlightenment**, French philosophers (*philosophes*) applied rational inquiry to politics and human rights:\n\n"
                            "- **Jean-Jacques Rousseau (1712–1778):** In *The Social Contract*, Rousseau argued that legitimate political authority rests entirely on **Popular Sovereignty**—the general will and consent of the people, not royal blood.\n"
                            "- **Baron de Montesquieu (1689–1755):** In *The Spirit of the Laws*, he advocated the **Separation of Powers** (executive, legislative, judicial) to prevent tyranny.\n"
                            "- **Voltaire (1694–1778):** Promoted religious tolerance, freedom of speech, and fiercely criticized the corruption of the Catholic hierarchy and aristocracy.\n\n"
                            "These ideas provided the intellectual ammunition for the Bourgeoisie to demand a complete overhaul of French governance."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Divine Right Absolutism vs. Enlightenment Constitutionalism",
                    "content": {
                        "headers": ["Feature", "Divine Right Monarchy (Ancien Régime)", "Enlightenment Constitutionalism"],
                        "rows": [
                            [
                                "Source of Authority",
                                "God / Royal Hereditary Lineage",
                                "The People (Popular Sovereignty)"
                            ],
                            [
                                "Distribution of Power",
                                "Concentrated in the King's absolute will",
                                "Separated across Executive, Legislative, and Judiciary"
                            ],
                            [
                                "Legal Status of Citizens",
                                "Unequal subjects divided by hereditary birth",
                                "Free, equal citizens possessing natural, inalienable rights"
                            ],
                            [
                                "Taxation Principle",
                                "Arbitrary extraction imposed on the poor",
                                "Equitable taxation based on wealth, approved by citizens"
                            ]
                        ]
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Civic Thought Experiment: Popular Sovereignty",
                    "content": {
                        "instructions": (
                            "Reflect on Rousseau's quote: 'Man is born free, and everywhere he is in chains.'\n\n"
                            "1. Identify two modern 'chains' (systemic inequalities or injustices) that prevent citizens from fully enjoying their rights today.\n"
                            "2. Propose how modern constitutional public participation helps citizens exercise popular sovereignty peacefully."
                        )
                    }
                }
            ],

            # Page 5: Common Misconception & The Role of the Bourgeoisie
            [
                {
                    "type": "common_misconception",
                    "title": "Misconception: The Revolution Was Solely a Peasant Bread Riot",
                    "content": {
                        "misconception": "Many assume that the French Revolution was spontaneously sparked and led purely by starving rural peasants demanding bread.",
                        "reality": "While hungry peasants and urban workers provided the critical mass physical force, the revolution was conceived, organized, and politically led by the Bourgeoisie—the educated middle class of lawyers, merchants, and writers. Because the bourgeoisie had wealth and education but were shut out of power by noble birth requirements, they channeled popular economic grievances into a constitutional revolution."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Internal Divisions of the Third Estate",
                    "content": {
                        "text": (
                            "The Third Estate was far from monolithic. It was composed of three distinct socio-economic tiers:\n\n"
                            "- **1. The Bourgeoisie:** Wealthy bankers, merchants, lawyers, and civil servants who held immense financial assets but zero aristocratic privileges. They were deeply frustrated by noble monopolies on high office.\n"
                            "- **2. Urban Artisans & Wage Laborers (*Sans-Culottes*):** Blacksmiths, bakers, printers, and seamstresses living in Paris. Highly vulnerable to inflation, their anger over bread prices made them the shock troops of street demonstrations.\n"
                            "- **3. Rural Peasants:** Over 80% of France's total population. They were tied to the land, forced to perform unpaid road repairs (*corvée*), pay grinding feudal dues to local lords, give a tenth of their grain to the Church, and pay the hated salt tax (*gabelle*)."
                        )
                    }
                }
            ],

            # Page 6: Knowledge Check MCQs & Educational Video
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Social Structure of the Ancien Régime",
                    "content": {
                        "question": "Which Estate in pre-revolutionary France comprised the vast majority of the population and bore the entire direct tax burden?",
                        "options": {
                            "A": "The First Estate (Clergy)",
                            "B": "The Second Estate (Nobility)",
                            "C": "The Third Estate (Commoners)",
                            "D": "The Fourth Estate (Royal Court)"
                        },
                        "correct_answer": "C",
                        "explanation": "The Third Estate made up roughly 97% of France's population (~26 million people) and bore the entire burden of direct royal taxes, tithes, and feudal dues, while the privileged First and Second Estates enjoyed tax exemption."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Enlightenment Impact",
                    "content": {
                        "question": "How did Enlightenment ideas contribute to the outbreak of the French Revolution?",
                        "options": {
                            "A": "They encouraged the King to immediately increase taxes on the rural poor.",
                            "B": "They provided an intellectual framework that challenged the absolute divine right of monarchs, promoting liberty, equality, and popular sovereignty.",
                            "C": "They proved that absolute monarchies were the most efficient form of agricultural development.",
                            "D": "They called for the complete isolation of France from international trade."
                        },
                        "correct_answer": "B",
                        "explanation": "Philosophers such as Rousseau and Montesquieu argued that legitimate political authority derives from the consent of the governed (popular sovereignty) and that all men have natural rights, giving the Bourgeoisie the intellectual tools to challenge royal absolutism."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The French Revolution: Context and Causes",
                    "content": {
                        "youtube_id": "bO7FQsCcbD8",
                        "url": "https://www.youtube.com/watch?v=bO7FQsCcbD8",
                        "description": "Comprehensive video analysis exploring the social hierarchy of the Three Estates, the bankruptcy of Louis XVI, Enlightenment philosophy, and the initial spark of 1789."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Course and Turning Points of the Revolution
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Course and Turning Points of the Revolution",
        "unit_description": "Chronological sequence from the Estates-General and Tennis Court Oath to the Storming of the Bastille, Declaration of the Rights of Man, Reign of Terror, and Napoleonic Consolidation.",
        "lesson_title": "Course and Turning Points of the Revolution",
        "pages": [
            # Page 1: Learning Outcomes & Entry Spark
            [
                {
                    "type": "learning_goal",
                    "title": "Module 3.1.2 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Sequence the major political and military events of the revolution from 1789 to 1799\n"
                            "- Explain the historical significance of the **storming of the Bastille** and the **Tennis Court Oath**\n"
                            "- Analyze how the **Declaration of the Rights of Man and of the Citizen** redefined human rights\n"
                            "- Contrast the early moderate constitutional phase of the revolution with the radicalization of the **Reign of Terror**"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Spark: July 14, 1789 — The Storming of the Bastille",
                    "content": {
                        "text": (
                            "On July 14, 1789, thousands of angry Parisian commoners marched on the **Bastille**, a towering medieval stone fortress and royal prison.\n\n"
                            "The prison held only seven inmates at the time, so the crowd was not marching to liberate mass prisoners. They went because the Bastille was a dreaded symbol of royal tyranny and held 28,000 pounds of gunpowder.\n\n"
                            "By storming the fortress, overwhelming the royal garrison, and tearing down its massive stones with their bare hands, the people of Paris announced that physical sovereignty now belonged to the nation. "
                            "This decisive act saved the newly formed National Assembly from royal military suppression and became the eternal birthday of French liberty."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "The Storming of the Bastille (14 July 1789)",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Prise_de_la_Bastille.jpg/800px-Prise_de_la_Bastille.jpg",
                        "author": "Jean-Pierre Houël",
                        "licensing": "Public Domain (1789)",
                        "caption": "Jean-Pierre Houël's iconic painting of the storming of the Bastille on July 14, 1789, depicting smoke, combat, and armed citizens seizing the royal fortress—marking the popular military turning point of the French Revolution."
                    }
                }
            ],

            # Page 2: The Political Breakaway & Timeline
            [
                {
                    "type": "concept_explanation",
                    "title": "The Political Breakaway: May – June 1789",
                    "content": {
                        "text": (
                            "When the Estates-General met at Versailles on May 5, 1789, an immediate voting deadlock occurred:\n\n"
                            "- **The Unfair Voting System:** Under the traditional system, each Estate met separately and cast **one collective vote as a bloc**. This guaranteed that the First and Second Estates (clergy and nobles) could always combine to outvote the Third Estate 2-to-1, despite representing only 3% of the populace.\n"
                            "- **The Declaration of the National Assembly:** The Third Estate demanded voting 'by head' (one vote per individual delegate). When the King and nobles refused, the Third Estate delegates took a revolutionary step on **June 17, 1789**: they declared themselves the **National Assembly**, the sole legitimate legislative body representing the people of France.\n"
                            "- **The Tennis Court Oath (June 20, 1789):** Finding their meeting hall locked by royal troops, the delegates gathered on an indoor tennis court (*Jeu de Paume*) and swore a historic oath: never to disband until they had drafted a written constitution for France."
                        )
                    }
                },
                {
                    "type": "suggested_diagram",
                    "title": "Chronology & Turning Points of the French Revolution (1789–1799)",
                    "content": {
                        "caption": "Comprehensive chronological timeline illustrating the three major phases of the revolution: Moderate Constitutional Phase (1789–1792), Radical Reign of Terror (1792–1794), and Directory/Napoleonic Consolidation (1795–1799).",
                        "svg_content": SVG_REVOLUTIONARY_TIMELINE
                    }
                }
            ],

            # Page 3: Primary Source Analysis: Declaration of the Rights of Man
            [
                {
                    "type": "concept_explanation",
                    "title": "The Magna Carta of Modern Democracy (August 26, 1789)",
                    "content": {
                        "text": (
                            "On August 26, 1789, the National Assembly promulgated the **Declaration of the Rights of Man and of the Citizen**.\n\n"
                            "Drafted by the Marquis de Lafayette with advice from Thomas Jefferson, this landmark charter abolished feudalism, eliminated aristocratic tax immunities, and established universal civic equality."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Declaration of the Rights of Man and of the Citizen (1789)",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Declaration_of_the_Rights_of_man_1789.jpg/800px-Declaration_of_the_Rights_of_man_1789.jpg",
                        "author": "Jean-Jacques-François Le Barbier",
                        "licensing": "Public Domain (c. 1789)",
                        "caption": "The Declaration of the Rights of Man depicted on stone tablets with the Eye of Providence and the Phrygian cap of liberty, symbolizing the triumph of reason and natural law over monarchical tyranny."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Primary Source Analysis: Articles I, II, and III",
                    "content": {
                        "text": (
                            "> **Article I:** *Men are born and remain free and equal in rights. Social distinctions may be founded only upon the general good.*\n\n"
                            "> **Article II:** *The aim of all political association is the preservation of the natural and imprescriptible rights of man. These rights are liberty, property, security, and resistance to oppression.*\n\n"
                            "> **Article III:** *The principle of all sovereignty resides essentially in the nation. No body nor individual may exercise any authority which does not proceed directly from the nation.*\n\n"
                            "**Pedagogical Evaluation:**\n"
                            "- **What It Achieved:** It permanently dismantled the divine right of kings and hereditary nobility, declaring that government exists to serve citizen rights.\n"
                            "- **Historical Limitations:** Despite universal phrasing ('Men are born free'), it excluded women from political franchise (prompting Olympe de Gouges to write the *Declaration of the Rights of Woman*) and did not immediately outlaw slavery in France's sugar colonies."
                        )
                    }
                }
            ],

            # Page 4: The Radical Turn: War & The Reign of Terror
            [
                {
                    "type": "concept_explanation",
                    "title": "The Radical Turn: Foreign Invasion and the Reign of Terror (1793–1794)",
                    "content": {
                        "text": (
                            "By 1792, European absolute monarchies (Prussia, Austria, Britain) invaded France to restore King Louis XVI to the throne. "
                            "Faced with foreign invasion and internal royalist revolts, political power shifted from moderate constitutionalists to radical extremists known as the **Jacobins**, led by **Maximilien Robespierre**.\n\n"
                            "- **Execution of the King (January 21, 1793):** King Louis XVI was convicted of treason against the nation and executed publicly by the **guillotine**.\n"
                            "- **The Committee of Public Safety:** Robespierre established a 12-man emergency government with dictatorial powers. He declared that 'virtue without terror is fatal; terror without virtue is impotent.'\n"
                            "- **The Reality of the Terror:** Over 14 months, civil liberties were suspended. Special Revolutionary Tribunals executed over **40,000 citizens** without fair trials—including Queen Marie Antoinette, political rivals, and ordinary shopkeepers accused of high prices.\n"
                            "- **The Fall of Robespierre (July 1794):** Terrified of their own execution, fellow politicians united against Robespierre, arrested him, and executed him at the guillotine on July 28, 1794, bringing the Terror to an end."
                        )
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The Reign of Terror Targeted Only Royalty and Aristocrats",
                    "content": {
                        "misconception": "Popular films often portray the guillotine as an instrument used almost exclusively on wealthy kings, queens, and corrupt aristocrats.",
                        "reality": "Historical court records prove that over 80% of victims executed during the Reign of Terror were commoners—peasants, urban artisans, tavern keepers, and working-class citizens accused of minor infractions such as complaining about bread prices, avoiding the military draft, or possessing Catholic prayer books."
                    }
                }
            ],

            # Page 5: Moderate Phase vs Radical Phase Comparison
            [
                {
                    "type": "comparison_table",
                    "title": "Evolution of the Revolution: Moderate Phase vs. Radical Terror vs. Directory",
                    "content": {
                        "headers": ["Dimension", "Moderate Phase (1789–1792)", "Radical Phase / Terror (1792–1794)", "Directory & Consulate (1795–1799)"],
                        "rows": [
                            [
                                "Primary Goal",
                                "Constitutional monarchy and legal equality",
                                "Save the Republic at all costs; crush internal/external enemies",
                                "Restore social stability and consolidate bourgeois gains"
                            ],
                            [
                                "Dominant Leadership",
                                "National Assembly, Lafayette, Mirabeau",
                                "Maximilien Robespierre, Danton, Jacobins",
                                "The 5-Member Directory, Napoleon Bonaparte"
                            ],
                            [
                                "Status of the Monarchy",
                                "King retained with limited constitutional veto",
                                "Monarchy abolished; King Louis XVI executed for treason",
                                "Republic maintained until Napoleon declares Consulate (1799)"
                            ],
                            [
                                "Approach to Civil Rights",
                                "Protection of natural rights and due process",
                                "Suspension of rights; summary executions via Guillotine",
                                "Restricted voting franchise to property owners; military order"
                            ]
                        ]
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Civic Debate: Emergency Powers vs Constitutional Safeguards",
                    "content": {
                        "instructions": (
                            "Consider Robespierre's claim that civil liberties must be suspended during national crises to protect the nation.\n\n"
                            "1. What are the extreme dangers of allowing governments to suspend judicial trials during security emergencies?\n"
                            "2. How does Article 25 of the Constitution of Kenya (2010) ensure that certain rights (such as freedom from torture and fair trial) can NEVER be suspended, even during states of emergency?"
                        )
                    }
                }
            ],

            # Page 6: Knowledge Check MCQs & Educational Video
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: The Tennis Court Oath",
                    "content": {
                        "question": "What did the National Assembly swear in the historic Tennis Court Oath of June 1789?",
                        "options": {
                            "A": "To execute the King and queen immediately.",
                            "B": "Never to disband until they had written a new constitution for France.",
                            "C": "To return all colonized territories to their pre-colonial African rulers.",
                            "D": "To pay all outstanding royal debts to British bankers."
                        },
                        "correct_answer": "B",
                        "explanation": "Locked out of their official meeting hall, the delegates of the newly formed National Assembly gathered on an indoor tennis court at Versailles and swore never to separate until they had drafted a written constitution for France."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: The Reign of Terror",
                    "content": {
                        "question": "During the radical phase of the French Revolution (1793–1794), who led the Committee of Public Safety and oversaw the execution of over 40,000 citizens during the Reign of Terror?",
                        "options": {
                            "A": "Napoleon Bonaparte",
                            "B": "King Louis XVI",
                            "C": "Maximilien Robespierre",
                            "D": "Baron de Montesquieu"
                        },
                        "correct_answer": "C",
                        "explanation": "Maximilien Robespierre was the leader of the radical Jacobin faction and the Committee of Public Safety who directed the Reign of Terror, using the guillotine to eliminate perceived enemies before his own downfall in July 1794."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Course and Turning Points of the Revolution",
                    "content": {
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Documentary analysis of key milestones: The Tennis Court Oath, the Storming of the Bastille, the Declaration of Rights, and the radicalization under Robespierre."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Consequences and Global Legacies of the French Revolution
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Consequences and Global Legacies of the French Revolution",
        "unit_description": "Domestic restructuring in France, the rise of European nationalism, inspiration for the Haitian Revolution and Latin American independence, and global commercial transformation.",
        "lesson_title": "Consequences and Global Legacies of the French Revolution",
        "pages": [
            # Page 1: Learning Outcomes & Entry Spark
            [
                {
                    "type": "learning_goal",
                    "title": "Module 3.1.3 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify the immediate and long-term socio-economic consequences of the revolution within France\n"
                            "- Explain how the revolution fostered the rise of modern national identity and **nationalism** in Europe\n"
                            "- Analyze the revolution's global impact, specifically its role in inspiring anti-slavery struggles like the **Haitian Revolution**\n"
                            "- Evaluate how the Napoleonic Wars restructured global trade and Latin American independence"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Spark: When Revolutionary Ideals Crossed the Atlantic",
                    "content": {
                        "text": (
                            "In 1791, on the wealthy French sugar plantation island of Saint-Domingue (modern-day Haiti), half a million enslaved Africans rose in armed rebellion against their brutal colonial masters.\n\n"
                            "They did not invent their core demands out of thin air; they had received news from Paris that the National Assembly had proclaimed: *'All men are born free and equal in rights.'*\n\n"
                            "Taking those revolutionary words literally, they launched the **Haitian Revolution**—the first and only successful slave revolution in human history to establish a free, independent Black republic. "
                            "How did a revolution in the streets of Paris transform freedom across the globe? Let's analyze the ripple effects."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "General Toussaint Louverture, Leader of the Haitian Revolution",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Toussaint_Louverture_by_Maurin.jpg/800px-Toussaint_Louverture_by_Maurin.jpg",
                        "author": "Nicolas Eustache Maurin",
                        "licensing": "Public Domain (1838)",
                        "caption": "Portrait of General Toussaint Louverture, the brilliant military strategist and former enslaved African who led the Haitian Revolution, defeating French, British, and Spanish armies to abolish slavery and establish Haitian sovereignty."
                    }
                }
            ],

            # Page 2: Domestic Transformations in France
            [
                {
                    "type": "concept_explanation",
                    "title": "Domestic Transformations: Building a Modern Standardized State",
                    "content": {
                        "text": (
                            "The French Revolution wiped away centuries of medieval fragmentation and established a unified, modern nation-state:\n\n"
                            "- **1. Abolition of Feudalism:** Feudal tithes, noble hunting monopolies, lord courts, and hereditary class distinctions were permanently eradicated. All French citizens became subject to one common law.\n"
                            "- **2. Progressive & Standardized Taxation:** The arbitrary, corrupt tax farms of the Ancien Régime were replaced with an equitable tax system assessed fairly based on individual income and property.\n"
                            "- **3. Introduction of the Metric System:** Prior to 1789, France had over 250,000 conflicting local units of measurement, allowing feudal lords to cheat peasants in grain sales. The National Assembly introduced the universal **Metric System** (meters, kilograms, liters) based on scientific principles, revolutionizing global science and fair trade.\n"
                            "- **4. Secularization & Unified Education:** Church control over public administration and education was curtailed, creating the foundation for free, universal secular public schooling."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Pre-1789 Feudal Fragmentation vs. Post-Revolutionary Modern Standardization",
                    "content": {
                        "headers": ["Area", "Pre-Revolutionary France (Ancien Régime)", "Post-Revolutionary Modern France"],
                        "rows": [
                            [
                                "Legal System",
                                "Hundreds of contradictory regional customary laws and noble courts",
                                "Unified national legal code (Napoleonic Code) applying equally to all"
                            ],
                            [
                                "Weights & Measures",
                                "Over 250,000 chaotic local units manipulated by feudal lords",
                                "Universal Metric System (meter, gram, liter) facilitating fair commerce"
                            ],
                            [
                                "Internal Trade",
                                "Heavy internal tolls, tariffs, and customs barriers between provinces",
                                "Single free-trade national domestic market"
                            ],
                            [
                                "Social Mobility",
                                "Hereditary noble birth required for high military and civil office",
                                "Meritocracy: Career open to talent and education regardless of birth"
                            ]
                        ]
                    }
                }
            ],

            # Page 3: The Birth of Modern Nationalism
            [
                {
                    "type": "concept_explanation",
                    "title": "The Rise of Modern Nationalism: Loyalty to the Nation",
                    "content": {
                        "text": (
                            "Before 1789, a person's loyalty belonged to a king, a feudal lord, or a religious order. "
                            "The French Revolution created the revolutionary concept of the **Patrie** (the Fatherland) and the **Nation**—the collective body of citizens bound by shared laws and equal rights.\n\n"
                            "- **The Mass Citizen Army (*Levée en Masse*):** When foreign monarchs invaded France, the Republic mobilized all citizens. Ordinary people marched into battle singing *La Marseillaise* (the new national anthem) not to serve a king's ambition, but to defend their own liberty and homeland.\n"
                            "- **Exporting and Sparking Nationalism:** Under **Napoleon Bonaparte**, French armies swept across Europe, sweeping away feudalism and introducing the Napoleonic Code. However, French military occupation provoked a powerful nationalist counter-reaction: Spaniards, Germans, and Italians discovered their own national identities to resist French dominance."
                        )
                    }
                },
                {
                    "type": "step_process",
                    "title": "How Revolutionary Ideals Transformed European Geopolitics",
                    "content": {
                        "steps": [
                            {
                                "step": 1,
                                "title": "Popular Sovereignty Defined",
                                "description": "The state is redefined as belonging to its citizens rather than a monarch's personal property."
                            },
                            {
                                "step": 2,
                                "title": "Citizen Mobilization (Levée en Masse)",
                                "description": "National defense becomes the shared civic duty of all citizens, giving birth to the first modern citizen armies."
                            },
                            {
                                "step": 3,
                                "title": "Napoleonic Expansion",
                                "description": "Napoleon spreads legal equality and destroys feudal privileges across Europe while conquering neighboring crowns."
                            },
                            {
                                "step": 4,
                                "title": "Rise of European National Liberation",
                                "description": "Occupied peoples develop fierce national identities, laying the foundation for modern Germany, Italy, and sovereign European states."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Global Ripples: Haiti and Latin America
            [
                {
                    "type": "concept_explanation",
                    "title": "Global Ripples of 1789: Trans-Atlantic Liberation",
                    "content": {
                        "text": (
                            "The shockwaves of 1789 shattered colonial empires across the Atlantic:\n\n"
                            "1. **The Haitian Revolution (1791–1804):** Saint-Domingue was the most lucrative slave colony in the world. Led by **Toussaint Louverture** and later **Jean-Jacques Dessalines**, enslaved Africans crushed French, British, and Spanish expeditions. In 1804, they declared independence as **Haiti**, proving to the world that universal human rights applied to all human beings regardless of race.\n\n"
                            "2. **Latin American Wars of Independence:** In 1808, Napoleon invaded Spain and dethroned the Spanish King. This power vacuum in Madrid gave Creole leaders across the Americas—such as **Simón Bolívar** ('The Liberator') and **José de San Martín**—the opportunity to launch wars of independence, liberating Venezuela, Colombia, Ecuador, Peru, Bolivia, and Argentina from Spanish colonial rule.\n\n"
                            "3. **Global Commercial Restructuring:** The British naval blockade and Napoleonic trade wars forced nations to industrialize domestically and established Great Britain as the dominant 19th-century maritime empire."
                        )
                    }
                },
                {
                    "type": "suggested_diagram",
                    "title": "Global Ripples of 1789 Flow Diagram",
                    "content": {
                        "caption": "Cause-and-effect flow diagram connecting the collapse of monarchy in France to the Haitian Revolution, European nationalism, Latin American independence, and 21st-century human rights.",
                        "svg_content": SVG_GLOBAL_RIPPLES_1789
                    }
                }
            ],

            # Page 5: Comparative Revolutions Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Analysis: French, Haitian, and Latin American Revolutions",
                    "content": {
                        "headers": ["Feature", "French Revolution (1789–1799)", "Haitian Revolution (1791–1804)", "Latin American Revolutions (1808–1826)"],
                        "rows": [
                            [
                                "Core Catalyst",
                                "Fiscal bankruptcy, famine, and Ancien Régime social inequality",
                                "Brutal plantation slavery and French Declaration of Rights ideals",
                                "Napoleon's invasion of Spain and Creole exclusion from governance"
                            ],
                            [
                                "Primary Leaders",
                                "Bourgeoisie, National Assembly, Robespierre",
                                "Toussaint Louverture, Jean-Jacques Dessalines",
                                "Simón Bolívar, José de San Martín, Miguel Hidalgo"
                            ],
                            [
                                "Key Outcome",
                                "Abolition of feudalism, constitutionalism, rise of nationalism",
                                "Abolition of slavery, creation of first free Black Republic",
                                "Dismantling of the Spanish Empire and establishment of sovereign republics"
                            ],
                            [
                                "Global Significance",
                                "Established popular sovereignty as the benchmark of legitimacy",
                                "Proved universal human rights apply across all racial boundaries",
                                "Ended 300 years of European colonial rule in mainland South America"
                            ]
                        ]
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Critical Inquiry: Connecting 1789 to African Anti-Colonial Struggles",
                    "content": {
                        "instructions": (
                            "Consider how 20th-century African independence leaders (such as Jomo Kenyatta, Kwame Nkrumah, and Julius Nyerere) utilized the language of 'Self-Determination, Equality, and Human Dignity'.\n\n"
                            "Write a short paragraph analyzing how the ideals of the 1789 French and 1791 Haitian Revolutions provided the philosophical framework for dismantling 20th-century European colonial rule in Africa."
                        )
                    }
                }
            ],

            # Page 6: Knowledge Check MCQs & Educational Video
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: The Metric System",
                    "content": {
                        "question": "Which global standard of weights and measures was introduced during the French Revolution to replace chaotic, unequal local commercial systems?",
                        "options": {
                            "A": "The Imperial System (miles, pounds, gallons)",
                            "B": "The Metric System (meters, grams, liters)",
                            "C": "The Feudal System of noble measurements",
                            "D": "The American Standard System"
                        },
                        "correct_answer": "B",
                        "explanation": "The revolutionary National Assembly created and standardized the Metric System (meters, kilograms, liters) based on scientific constants to eliminate fraudulent local noble measures and promote fair trade."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Haitian Revolution Connection",
                    "content": {
                        "question": "How did the French Revolution directly contribute to the outbreak of the Haitian Revolution in 1791?",
                        "options": {
                            "A": "Enslaved populations in the Caribbean took the universal declaration that 'all men are born free and equal' literally, mobilizing to fight French colonial slave masters.",
                            "B": "King Louis XVI ordered French soldiers to arm the slaves against the bourgeoisie.",
                            "C": "Robespierre invaded the island of Saint-Domingue to establish a military dictatorship.",
                            "D": "The Haitian slave masters voluntarily freed all slaves to support the French noble army."
                        },
                        "correct_answer": "A",
                        "explanation": "When news of the Declaration of the Rights of Man reached Saint-Domingue, enslaved Africans applied the universal declaration of human freedom to their own reality, rising in rebellion under Toussaint Louverture."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Consequences and Global Legacies of the Revolution",
                    "content": {
                        "youtube_id": "rNu8XDBSn10",
                        "url": "https://www.youtube.com/watch?v=rNu8XDBSn10",
                        "description": "Video exploration of how the French Revolution birthed modern nationalism, triggered the Haitian Revolution, and reshaped global human rights standards."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Why the French Revolution Matters Today
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Why the French Revolution Matters Today",
        "unit_description": "Enduring democratic values, warnings against unchecked power, philosophical synthesis with the Constitution of Kenya (2010), and the Great Revolutions Lab inquiry task.",
        "lesson_title": "Why the French Revolution Matters Today",
        "pages": [
            # Page 1: Learning Outcomes & Entry Spark
            [
                {
                    "type": "learning_goal",
                    "title": "Module 3.1.4 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the modern civic values of *liberty*, *equality*, and *civic participation* as championed by the revolution\n"
                            "- Analyze the critical warning that the **Reign of Terror** provides regarding unchecked political power\n"
                            "- Connect revolutionary constitutional principles to the Bill of Rights in the **Constitution of Kenya (2010)**\n"
                            "- Formulate an evidence-grounded position on how citizens can hold governments accountable peacefully through the **Great Revolutions Lab**"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Spark: 'Liberté, Égalité, Fraternité' in the 21st Century",
                    "content": {
                        "text": (
                            "Look at the national motto of the modern French Republic: **'Liberté, Égalité, Fraternité'** (Liberty, Equality, Fraternity). "
                            "These three words are not merely historical relics; they represent the foundational architecture of modern constitutional democracy.\n\n"
                            "Every time you cast a secret ballot in an election, speak your mind peacefully, criticize a public policy, or attend school regardless of family wealth, you are enjoying freedoms that were fought and died for in 1789.\n\n"
                            "However, the French Revolution also teaches a sobering lesson: noble ideals can rapidly degenerate into bloody tyranny if political power is left unchecked. How do we safeguard these rights in Kenya and around the world today?"
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Modern Citizens Peacefully Protesting for Democratic Rights",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Demonstration_for_Democracy.jpg/800px-Demonstration_for_Democracy.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0 / Public Domain",
                        "caption": "Modern citizens peacefully assembling and marching in a democratic demonstration holding signs demanding equality, justice, and civic accountability—bridging 1789 Paris with contemporary civic movements."
                    }
                }
            ],

            # Page 2: The Four Pillars of Civic Stewardship
            [
                {
                    "type": "concept_explanation",
                    "title": "The Four Pillars of Civic Stewardship and Democratic Governance",
                    "content": {
                        "text": (
                            "The history of the French Revolution yields four enduring principles essential for sustaining a free, stable society:\n\n"
                            "1. **Universal Equality:** No individual, family, or social group possesses hereditary or legal privileges above the law. True national harmony requires equal economic opportunities and progressive, fair taxation.\n\n"
                            "2. **The Inalienable Value of Liberty:** Fundamental individual freedoms—speech, assembly, worship, press, and movement—must be guaranteed in a binding constitution that no government can arbitrarily revoke.\n\n"
                            "3. **The Imperative of Active Civic Participation:** A democracy cannot survive with a passive populace. Citizens must stay informed, participate in public forums, monitor public expenditures, and vote conscientiously.\n\n"
                            "4. **The Danger of Unchecked Power:** Robespierre's Reign of Terror serves as history's ultimate warning. When governments suspend due process or eliminate judicial checks under the pretext of 'national security,' freedom instantly collapses into dictatorship."
                        )
                    }
                },
                {
                    "type": "suggested_diagram",
                    "title": "The Four Pillars of Civic Stewardship",
                    "content": {
                        "caption": "Architectural diagram showing Universal Equality, Individual Liberty, Civic Participation, and Accountability of Power upholding a Democratic Society rooted in the Rule of Law.",
                        "svg_content": SVG_PILLARS_CIVIC_STEWARDSHIP
                    }
                }
            ],

            # Page 3: Connecting 1789 to Modern Kenya (Constitution 2010)
            [
                {
                    "type": "concept_explanation",
                    "title": "Connecting 1789 to Modern Kenya: The Constitution of Kenya (2010)",
                    "content": {
                        "text": (
                            "The revolutionary ideas born in 1789 are directly embedded in Kenya's supreme law today:\n\n"
                            "- **Sovereignty Belonging to the People:** Article 3 of the 1789 Declaration stated that sovereignty resides essentially in the nation. Similarly, **Article 1(1) of the Constitution of Kenya (2010)** declares: *'All sovereign power belongs to the people of Kenya and shall be exercised only in accordance with this Constitution.'*\n\n"
                            "- **Absolute Equality Before the Law:** The French abolished noble tax exemptions and class privileges. **Article 27 of the Kenyan Constitution** guarantees that *'Every person is equal before the law and has the right to equal protection and equal benefit of the law.'*\n\n"
                            "- **Public Participation & National Values:** **Article 10(2)** establishes democracy, public participation, human dignity, equity, and accountability as mandatory national values binding all public officers."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Philosophical Continuity: 1789 French Declaration vs. Constitution of Kenya (2010)",
                    "content": {
                        "headers": ["Democratic Principle", "1789 Declaration of the Rights of Man", "Constitution of Kenya (2010) — Bill of Rights"],
                        "rows": [
                            [
                                "Popular Sovereignty",
                                "Article 3: 'The principle of all sovereignty resides essentially in the nation.'",
                                "Article 1: 'All sovereign power belongs to the people of Kenya.'"
                            ],
                            [
                                "Equality & Non-Discrimination",
                                "Article 1: 'Men are born and remain free and equal in rights.'",
                                "Article 27: 'Every person is equal before the law and has the right to equal protection.'"
                            ],
                            [
                                "Freedom of Expression & Media",
                                "Article 11: 'The free communication of ideas and opinions is one of the most precious of the rights of man.'",
                                "Article 33 & 34: Guarantees freedom of expression and independence of electronic, print, and broadcast media."
                            ],
                            [
                                "Accountability & Taxation",
                                "Article 14: 'All citizens have the right to ascertain the necessity of public contribution.'",
                                "Article 201: Principles of public finance: openness, accountability, and equitable sharing of tax burdens."
                            ]
                        ]
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The French Revolution Was a Failure Because It Led to Napoleon",
                    "content": {
                        "misconception": "Some critics argue that because the French Revolution experienced the Reign of Terror and ended with Napoleon's military dictatorship, the entire revolution was a failure.",
                        "reality": "While the revolution suffered extreme violence and setbacks, its ideas transformed human history forever. It destroyed the divine right of kings, abolished feudalism throughout Europe, introduced modern legal equality, and established universal human rights as the universal moral standard for legitimate government."
                    }
                }
            ],

            # Page 4: Synthesis Inquiry: The Great Revolutions Lab
            [
                {
                    "type": "concept_explanation",
                    "title": "Synthesis Inquiry: The Great Revolutions Lab",
                    "content": {
                        "text": (
                            "### The County Constitutional Advisory Challenge\n\n"
                            "You have been appointed as a senior **Civic & Constitutional Advisor** to a Kenyan County Government to assist them in designing an effective, transparent **Public Participation Framework** for county budget allocations and tax policies.\n\n"
                            "Using your deep historical understanding of the French Revolution and the Constitution of Kenya (2010), prepare a structured 3-paragraph **Civic Advisory Brief** answering the following prompt:"
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "The Great Revolutions Lab: 3-Paragraph Civic Advisory Brief",
                    "content": {
                        "instructions": (
                            "Draft your 3-paragraph brief adhering to the following structure:\n\n"
                            "1. **Paragraph 1 (The Historical Warning):** Analyze how France's Ancien Régime collapsed because a privileged 3% elite paid no taxes while the overburdened 97% had no political voice. Warn the county leadership of the dangers of ignoring marginalized citizens or imposing unfair local tax burdens.\n\n"
                            "2. **Paragraph 2 (The Balance of Power & Security):** Examine how the French Revolution degenerated into the Reign of Terror when civil liberties and judicial checks were suspended in the name of emergency. Explain why the rule of law, transparency, and freedom of expression are non-negotiable, even during financial or administrative challenges.\n\n"
                            "3. **Paragraph 3 (The Modern Action Plan):** Propose two concrete institutional mechanisms grounded in **Article 10 and Article 201 of Kenya's Constitution** (such as open digital town halls, citizen audit committees, or ward-level participatory budgeting) to ensure genuine public oversight and equitable resource sharing."
                        )
                    }
                }
            ],

            # Page 5: Cumulative Topic Assessment & Key Takeaways
            [
                {
                    "type": "concept_explanation",
                    "title": "Topic Synthesis & Cumulative Historical Takeaways",
                    "content": {
                        "text": (
                            "As we conclude Topic 3.1, review the four universal principles derived from the French Revolution:\n\n"
                            "- **1. Systemic Inequality Destabilizes Nations:** A society where wealth and power are concentrated in a privileged minority while the majority carries the tax burden is inherently fragile and unsustainable.\n"
                            "- **2. Ideas Mobilize Human Action:** Enlightenment concepts of human dignity and popular sovereignty proved that ideas have the power to dismantle centuries-old imperial structures.\n"
                            "- **3. Extremism Destroys Liberty:** Suspending the rule of law and silencing dissenting voices—even with good intentions—inevitably leads to despotism.\n"
                            "- **4. Rights Require Eternal Vigilance:** Human rights and democratic constitutions are never permanently safe; they require active citizen participation, constitutional checks, and institutional integrity."
                        )
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Cumulative Assessment MCQ 1: Structural Causes",
                    "content": {
                        "question": "An agricultural historian in France is analyzing local land records from the early 1780s. Which of the following findings would provide direct evidence of the structural causes of the French Revolution?",
                        "options": {
                            "A": "Peasant farmers owning 90% of the land and paying no taxes to the King or Church.",
                            "B": "Noble estates being heavily taxed while the bourgeoisie enjoyed complete tax exemption.",
                            "C": "Peasant farmers being forced to pay heavy feudal dues and Church tithes while owning a minority of the fertile land.",
                            "D": "The complete abolition of the metric system by King Louis XVI."
                        },
                        "correct_answer": "C",
                        "explanation": "The fundamental structural injustice of the Ancien Régime was that peasant farmers, who comprised over 80% of France's population, owned very little fertile land yet were forced to pay heavy feudal dues to lords, tithes to the Church, and direct taxes to the King."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Cumulative Assessment MCQ 2: Symbolism of the Bastille",
                    "content": {
                        "question": "Why did the storming of the Bastille on July 14, 1789, become the supreme national symbol of the French Revolution?",
                        "options": {
                            "A": "Because it proved that the King's professional military was superior to urban crowds.",
                            "B": "Because it was the first time that King Louis XVI voluntarily abdicated his throne.",
                            "C": "Because the Bastille was a dreaded symbol of royal tyranny, and its capture proved that the popular mobilization of ordinary citizens could challenge absolute monarchy.",
                            "D": "Because it allowed the First Estate clergy to reclaim their lost Church tithes."
                        },
                        "correct_answer": "C",
                        "explanation": "The Bastille was the ultimate physical embodiment of royal tyranny and arbitrary arrest. Its capture and demolition by Parisian citizens proved that sovereignty had shifted from the King to the people, preventing the royal army from dissolving the National Assembly."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Cumulative Assessment MCQ 3: Long-Term Global Impact",
                    "content": {
                        "question": "Which of the following is a direct, long-term global legacy of the French Revolution?",
                        "options": {
                            "A": "The permanent restoration of divine-right absolute monarchies across all European nations.",
                            "B": "The global spread of democratic ideals, legal equality, and modern nationalism, inspiring liberation in Haiti and Latin America.",
                            "C": "The immediate economic collapse of the United States banking system.",
                            "D": "The total elimination of Kiswahili as a trade language in East Africa."
                        },
                        "correct_answer": "B",
                        "explanation": "The revolutionary principles of liberty, equality, and popular sovereignty inspired global liberation movements, including the Haitian Revolution led by Toussaint Louverture and Simón Bolívar's wars of independence across South America."
                    }
                }
            ],

            # Page 6: Knowledge Check MCQs & Educational Video
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Warning of the Reign of Terror",
                    "content": {
                        "question": "What critical warning does Maximilien Robespierre's Reign of Terror offer to modern democratic societies today?",
                        "options": {
                            "A": "Absolute monarchies are always more peaceful and stable than democratic assemblies.",
                            "B": "Governments should never collect taxes under any economic circumstances.",
                            "C": "Unchecked political power, the suspension of civil liberties, and the elimination of judicial accountability can quickly turn a struggle for liberty into a brutal dictatorship.",
                            "D": "Citizen participation in governance should be restricted strictly to members of the clergy and nobility."
                        },
                        "correct_answer": "C",
                        "explanation": "The Reign of Terror proves that when leaders claim extraordinary powers, suspend the rule of law, and eliminate judicial checks in the name of 'security', democracy rapidly transforms into violent authoritarianism."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Popular Sovereignty in Kenya's Constitution",
                    "content": {
                        "question": "How does Article 1 of the Constitution of Kenya (2010) mirror the core principles established by the French Revolution?",
                        "options": {
                            "A": "It establishes that all political power belongs to a single hereditary King.",
                            "B": "It states that all sovereign power belongs to the people of Kenya, mirroring the revolutionary principle of popular sovereignty.",
                            "C": "It requires all citizens to serve in a mandatory military draft.",
                            "D": "It mandates that Kiswahili be abolished as an administrative language."
                        },
                        "correct_answer": "B",
                        "explanation": "Both Article 3 of the 1789 French Declaration and Article 1 of the Constitution of Kenya (2010) establish the doctrine of Popular Sovereignty: that legitimate authority originates from the people, who hold the supreme power to govern themselves."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Why the French Revolution Still Matters Today",
                    "content": {
                        "youtube_id": "T_sGTspaF4Y",
                        "url": "https://www.youtube.com/watch?v=T_sGTspaF4Y",
                        "description": "Educational summary analyzing how the French Revolution established modern human rights, popular sovereignty, and active democratic citizenship around the world."
                    }
                }
            ]
        ]
    }
]
