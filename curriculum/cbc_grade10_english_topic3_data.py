"""
VLearn CBC Grade 10 English — Topic 3: Grammar in Use
Full Structured Lesson Card Definitions for Lessons 1 to 10
"""

from curriculum.cbc_grade10_english_topic3_svgs import (
    SVG_NOUNS_PRONOUNS_DETERMINERS,
    SVG_VERBS_AND_ADVERBS,
    SVG_ADJECTIVES_CONJUNCTIONS_CONNECTORS,
    SVG_NOUN_AND_VERB_PHRASES,
    SVG_ADJ_ADV_PREP_PHRASES,
    SVG_RELATIVE_AND_ADVERBIAL_CLAUSES,
    SVG_NOUN_CLAUSES_FUNCTIONS,
    SVG_SIMPLE_SENTENCE_PARTS,
    SVG_SENTENCE_FLUENCY_REPAIR,
    SVG_VOICE_AND_AGREEMENT,
)

TOPIC_3_LESSONS = [
    # =========================================================================
    # LESSON 1: Nouns, Pronouns, and Determiners
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Nouns, Pronouns, and Determiners",
        "unit_description": "Foundational anchors of English sentences: noun classifications, pronoun-antecedent agreement, and determiner signposts.",
        "lesson_title": "Nouns, Pronouns, and Determiners",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Working in Modern Computer Lab",
                    "content": {
                        "title": "Collaborative Digital Learning in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/African_Students_in_Computer_Lab.jpg/800px-African_Students_in_Computer_Lab.jpg",
                        "caption": "Students collaborating in a modern school IT laboratory, utilizing precise nouns, pronouns, and determiners to describe digital tools and tasks.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and correctly classify proper, common, concrete, abstract, and mass (non-count) nouns\n- Ensure perfect pronoun-antecedent agreement in number and gender across complex sentences\n- Use determiners (articles, possessives, demonstratives, quantifiers) accurately as noun signposts\n- Distinguish between count vs. non-count quantifiers (e.g., 'few' vs. 'little') in academic writing"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: The IT Lab Incident",
                    "content": {
                        "text": "Consider how meaning changes with single word shifts in this description:\n\n> *\"A teacher walked into **the** room. **She** saw **some** students working on **their** computers. **The computer lab** was quiet, but **it** was full of creative energy.\"*\n\n- Changing '**She**' to '**He**' introduces a completely different individual.\n- Changing '**the computer lab**' to '**a computer lab**' disconnects the sentence from the room the teacher just entered!\n- Nouns name the entities, pronouns prevent monotonous repetition, and determiners serve as indispensable navigational signposts."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Nouns, Pronouns & Determiners",
                    "content": {
                        "term": "Determiner & Antecedent Agreement",
                        "definition": "A **determiner** is a modifying word placed before a noun to clarify quantity, possession, or specificity (e.g., 'the', 'those', 'every'). **Antecedent agreement** requires a pronoun to match the exact grammatical number and gender of the noun it replaces."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Grammatical Classification Matrix",
                    "content": {
                        "headers": ["Element", "Primary Subtypes", "Key Functional Rule", "Correct Academic Example"],
                        "rows": [
                            ["Proper Noun", "Specific names of people, places, institutions", "Must always be capitalized", "Mr. Omondi visited Nairobi National Park."],
                            ["Abstract Noun", "Ideas, emotions, states of being, qualities", "Intangible; cannot be perceived by 5 senses", "Patience and integrity build long-term trust."],
                            ["Mass / Non-count Noun", "Indivisible entities (information, software, equipment)", "No plural '-s'; cannot directly take 'a/an'", "We gathered sufficient data and installed new software."],
                            ["Personal Pronoun", "Subject/Object replacements (I, she, they, us)", "Must match antecedent in number & gender", "The committee finalized its report yesterday."],
                            ["Demonstrative Determiner", "Pointing words (this, that, these, those)", "Matches noun number and proximity", "These laptops require immediate system updates."],
                            ["Quantifier", "Amounts (few/fewer for count; little/less for mass)", "Few = hardly any; A few = a small positive amount", "She experienced few difficulties during the test."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Nouns, Pronouns, and Determiners Matrix",
                    "content": {
                        "title": "The Anchors of the Sentence: Classification & Syntax Matrix",
                        "caption": "Architectural breakdown showing noun classifications, pronoun replacement mechanisms, and determiner signpost functions.",
                        "svg_content": SVG_NOUNS_PRONOUNS_DETERMINERS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Parsing Complex Noun Groups",
                    "content": {
                        "intro": "Analyze how determiners, nouns, and pronouns interact in this authentic school scenario:",
                        "steps": [
                            "**Original Sentence:** *'Each of the newly admitted students must present their registration forms to Mr. Omondi.'*",
                            "**Step 1: Identify Nouns & Number:** 'Students' (plural common noun), 'registration forms' (plural count noun phrase), 'Mr. Omondi' (singular proper noun).",
                            "**Step 2: Identify Determiners & Distribution:** 'Each' (distributive pronoun/determiner requiring singular agreement), 'the' (definite article), 'their' (plural possessive determiner).",
                            "**Step 3: Diagnose Agreement Conflict:** 'Each' is grammatically singular, yet 'their' is plural. This creates an antecedent agreement clash.",
                            "**Step 4: Formal CBC Correction:** *'Each student must present **his or her** registration form...'* OR *'All newly admitted **students** must present **their** registration forms to Mr. Omondi.'*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Determiners: Articles, Quantifiers & Possessives",
                    "content": {
                        "title": "Determiners and Noun Modifiers Explained",
                        "youtube_id": "pcYrmHrtLRY",
                        "url": "https://www.youtube.com/watch?v=pcYrmHrtLRY",
                        "description": "Comprehensive video guide covering articles, demonstratives, quantifiers, and common possessive determiner errors."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Contextual Editing Challenge",
                    "content": {
                        "title": "Analyzing Administrative Communication",
                        "text": "**Pre-Viewing Focus:** Note the critical distinction between *few* (negative: almost none) and *a few* (positive: some). Also observe how possessive determiners (*its*, *their*) differ from contractions (*it's*, *they're*).\n\n**Post-Viewing Task:** Why do mass nouns such as *software*, *evidence*, *baggage*, and *equipment* never take plural '-s'? In administrative writing, using 'pieces of equipment' or 'software applications' demonstrates grammatical competence."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Grammatical Pitfalls & Corrections",
                    "content": {
                        "text": "### Pitfall 1: Pluralizing Mass (Non-Count) Nouns\n- **Incorrect:** *\"The IT department bought new equipments and gathered multiple informations.\"*\n- **Correct:** *\"The IT department bought new **equipment** (or pieces of equipment) and gathered **information** (or data points).\"*\n\n### Pitfall 2: Ambiguous Pronoun Reference\n- **Incorrect:** *\"The doctor told the patient that **he** had made an error.\"* *(Who made the error?)*\n- **Correct:** *\"The doctor admitted to the patient, '**I** made an error,'\"* or *\"The doctor informed the patient of the **patient's** error.\"*\n\n### Pitfall 3: Possessive 'Its' vs. Contraction 'It's'\n- **Incorrect:** *\"The institution updated **it's** security protocols.\"*\n- **Correct:** *\"The institution updated **its** security protocols.\"* *('It's' = 'It is').*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Pronoun & Determiner Repair",
                    "content": {
                        "intro": "Work through these repair exercises step by step:",
                        "steps": [
                            {"title": "Item 1: 'Every passenger must collect their luggage upon arrival.'", "description": "Analysis: 'Every passenger' is singular. Repair: 'Every passenger must collect **his or her luggage**...' or pluralize the subject: '**Passengers** must collect **their luggage**...'"},
                            {"title": "Item 2: 'We have little computers remaining in the inventory.'", "description": "Analysis: 'Computers' is a countable noun. 'Little' applies only to mass nouns. Repair: 'We have **few** (or **a few**) computers remaining in the inventory.'"},
                            {"title": "Item 3: 'This is the application whom won first prize in Nairobi.'", "description": "Analysis: 'Whom' refers only to persons in object position. For things, use 'that' or 'which'. Repair: 'This is the application **that won** first prize in Nairobi.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Noun & Pronoun Agreement",
                    "content": {
                        "question": "Which of the following sentences adheres 100% to formal grammatical rules of noun classification and antecedent agreement?",
                        "options": [
                            "The jury reached their verdict after evaluating all the testimonies and softwares presented.",
                            "The committee finalized its recommendations, and it submitted the official report to the ministry.",
                            "Every doctor and nurse must renew their medical licenses before the end of this financial year.",
                            "The school purchased several new sports equipments for it's upcoming national tournament."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is fully correct. 'The committee' functions as a collective singular unit, taking the singular possessive determiner 'its' and singular pronoun 'it'. Option A incorrectly pluralizes the mass noun 'software'. Option C has a singular compound distributive subject ('Every doctor and nurse') clashing with plural 'their'. Option D incorrectly uses 'equipments' (mass noun) and 'it's' (contraction for 'it is')."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Quantifier and Determiner Selection",
                    "content": {
                        "question": "Select the sentence that uses count/mass quantifiers correctly:",
                        "options": [
                            "Due to the severe drought, the farming community had less cattle and little crops left.",
                            "Because of clear road signage, we encountered few delays and needed little guidance during the trip.",
                            "The research team gathered many equipments and fewer information than anticipated.",
                            "There are much students participating in the environmental symposium this afternoon."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: 'delays' is countable (modifying with 'few'), while 'guidance' is non-count (modifying with 'little'). Option A should use 'fewer cattle' and 'few crops'. Option C incorrectly pairs 'many' with 'equipments' (mass) and 'fewer' with 'information' (mass). Option D incorrectly uses 'much' with countable 'students' instead of 'many'."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Nouns** are categorical anchors: differentiate count vs. mass nouns to avoid invalid plurals (*softwares*, *equipments*).\n- **Pronouns** must align in person, number, and gender with their antecedent nouns without ambiguity.\n- **Determiners** (*articles, demonstratives, quantifiers*) set the syntactic boundaries and reference scopes of all noun phrases."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Verbs and Adverbs
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Verbs and Adverbs",
        "unit_description": "Engines and steering wheels of sentences: main vs. auxiliary verbs, tense-aspect systems, and adverbial modification types.",
        "lesson_title": "Verbs and Adverbs",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Athletes Competing in High-Intensity Football Match",
                    "content": {
                        "title": "Dynamic Athletic Movement on the Field",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_in_Equatorial_Guinea.jpg/800px-Football_in_Equatorial_Guinea.jpg",
                        "caption": "Athletes sprinting and striking the ball during a competitive match, illustrating dynamic verbs of action and adverbs of manner, time, and intensity.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between main verbs and primary/modal auxiliary verbs\n- Differentiate and apply the 4 verb aspects: Simple, Continuous, Perfect, and Perfect Continuous\n- Classify adverbs into manner, time, place, frequency, and degree\n- Apply correct adverb placement rules to avoid ambiguous or ungrammatical sentence structures"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: The Sports Commentary",
                    "content": {
                        "text": "Observe how verb and adverb choices alter meaning and mental imagery:\n\n- **Version 1:** *\"The striker **sprinted** down the pitch. He **kicked** the ball **powerfully** into the net.\"*\n- **Version 2:** *\"The striker **stumbled** down the pitch. He **kicked** the ball **clumsily** past the post.\"*\n\nBoth sentences share identical syntax, yet the verbs (*sprinted* vs. *stumbled*) and adverbs (*powerfully* vs. *clumsily*) create completely opposing realities!"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Tense, Aspect & Adverbs",
                    "content": {
                        "term": "Aspect & Adverbial Modification",
                        "definition": "**Tense** locates an event in time (Past, Present, Future), while **Aspect** describes *how the action unfolds or is viewed* (Simple = complete/habitual; Continuous = ongoing; Perfect = completed prior to a reference point; Perfect Continuous = ongoing duration). **Adverbs** modify verbs, adjectives, or other adverbs."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Verb Aspect and Adverb Classification",
                    "content": {
                        "headers": ["Grammatical Category", "Structural Formula", "Temporal/Syntactic Function", "Exemplar Sentence"],
                        "rows": [
                            ["Simple Aspect", "Base form / Past (-ed)", "Expresses habitual, permanent, or general truths", "The IT technician inspects the servers daily."],
                            ["Continuous Aspect", "Form of 'Be' + Verb-ing", "Depicts an ongoing, temporary action in progress", "She is currently troubleshooting the network router."],
                            ["Perfect Aspect", "Form of 'Have' + Past Participle", "Actions completed prior to a specified reference point", "By 10 AM, the students had submitted their scripts."],
                            ["Perfect Continuous", "Have + been + Verb-ing", "Highlights continuous duration leading up to a time", "They have been studying robotics for three years."],
                            ["Adverb of Manner", "Suffix '-ly' (usually)", "Answers 'How?' the action occurred", "The surgeon operated meticulously under pressure."],
                            ["Adverb of Frequency", "Always, seldom, rarely", "Answers 'How often?' action takes place", "The engineering team rarely postpones system audits."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Verbs and Adverbs: Dynamics and Modification",
                    "content": {
                        "title": "Verb Aspect Architecture & Adverbial Modification Grid",
                        "caption": "Structural visualization of the 4 verb aspects alongside the 5 functional categories and placement rules for adverbs.",
                        "svg_content": SVG_VERBS_AND_ADVERBS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Deconstructing Verb Sequences",
                    "content": {
                        "intro": "Analyze the complex tense, aspect, and adverb sequence in this statement:",
                        "steps": [
                            "**Exemplar Sentence:** *'By next December, the school **will have been utilizing** this computer lab for two full years.'*",
                            "**1. Modal Auxiliary:** 'will' establishes Future temporal reference.",
                            "**2. Perfect Auxiliary:** 'have' indicates completion before a future milestone.",
                            "**3. Continuous Auxiliary:** 'been' denotes ongoing in-progress action.",
                            "**4. Main Verb:** 'utilizing' (Present participle) carries the semantic core.",
                            "**Syntactic Verdict:** **Future Perfect Continuous Aspect** (will + have + been + -ing)."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Present Progressive & English Verb Tenses",
                    "content": {
                        "title": "Tense vs. Aspect: Progressive and Perfect Systems",
                        "youtube_id": "p1NbkB77QYY",
                        "url": "https://www.youtube.com/watch?v=p1NbkB77QYY",
                        "description": "Expert tutorial explaining the dynamic interplay between simple and continuous aspects, stative verbs, and time sequencing."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Stative vs. Dynamic Verbs",
                    "content": {
                        "title": "Investigating Progressive Restrictions",
                        "text": "**Pre-Viewing Focus:** Pay attention to stative verbs (verbs of state, emotion, perception, or possession like *know*, *believe*, *own*, *prefer*). Why are they rarely used in continuous aspects?\n\n**Post-Viewing Reflection:** Why is *'I understand the theorem'* grammatically superior to *'I am understanding the theorem'*? Notice how converting stative verbs into continuous forms often results in non-standard English."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Verb & Adverb Pitfalls",
                    "content": {
                        "text": "### Pitfall 1: Faulty Tense Sequencing in Past Events\n- **Incorrect:** *\"By the time the technician arrived, the database **already crashed**.\"*\n- **Correct:** *\"By the time the technician arrived, the database **had already crashed**.\"* *(Past Perfect is required for the earlier past event).*\n\n### Pitfall 2: Splitting Verb and Direct Object with an Adverb\n- **Incorrect:** *\"He spoke **fluently English** during the interview.\"*\n- **Correct:** *\"He spoke **English fluently** during the interview\"* OR *\"He **fluently spoke** English...\"*\n\n### Pitfall 3: Using Adjectives in Place of Adverbs of Manner\n- **Incorrect:** *\"The choir performed **exceptional good** at the national festival.\"*\n- **Correct:** *\"The choir performed **exceptionally well** at the national festival.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Tense, Aspect & Adverb Placement",
                    "content": {
                        "intro": "Complete and rectify these sentences:",
                        "steps": [
                            {"title": "Task 1: 'Since 2022, our county (construct) three modern libraries.'", "description": "Analysis: Action started in the past and connects to the present ('Since 2022'). Required: Present Perfect. Solution: '...our county **has constructed** three modern libraries.'"},
                            {"title": "Task 2: 'The athlete ran (quick) to assist his injured teammate.'", "description": "Analysis: Modifying the action verb 'ran' requires an adverb of manner. Solution: 'The athlete ran **quickly** to assist...'"},
                            {"title": "Task 3: 'She solved easily the mathematics problem.'", "description": "Analysis: Do not place adverb 'easily' between verb 'solved' and object 'the problem'. Solution: 'She solved the mathematics problem **easily**' or 'She **easily solved** the mathematics problem.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Verb Aspect",
                    "content": {
                        "question": "Identify the precise tense and aspect of the bolded verb phrase: 'By 8:00 PM tonight, the engineers **will have been testing** the backup generator for twelve hours straight.'",
                        "options": [
                            "Future Continuous",
                            "Future Perfect",
                            "Future Perfect Continuous",
                            "Present Perfect Continuous"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct. 'Will' (future) + 'have' (perfect) + 'been' (continuous marker) + 'testing' (present participle) forms the Future Perfect Continuous aspect, depicting an ongoing action that will continue up to a designated future milestone."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Adverb Positioning and Form",
                    "content": {
                        "question": "Which of the following sentences adheres correctly to English adverb placement and morphology rules?",
                        "options": [
                            "The debater articulated her points clear and persuaded easily the judges.",
                            "The debater articulated her points clearly and easily persuaded the judges.",
                            "The debater articulated clearly her points and persuaded the judges easy.",
                            "The debater clearly articulated her points and persuaded easily the judges."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: 'clearly' (adverb of manner modifying 'articulated') appears after the direct object, and 'easily' correctly precedes the verb 'persuaded'. All other options incorrectly place an adverb between the transitive verb and direct object or substitute the adjective 'clear'/'easy' for the required adverb."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Verbs** convey action and state through a combination of **Tense** (past/present/future) and **Aspect** (simple/continuous/perfect/perfect continuous).\n- **Adverbs** enrich discourse by modifying verbs, adjectives, and other adverbs across manner, time, place, frequency, and degree.\n- **Placement matters**: Never place an adverb between a transitive verb and its direct object."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Adjectives, Conjunctions, and Simple Connectors
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Adjectives, Conjunctions, and Simple Connectors",
        "unit_description": "Descriptive precision and logical coherence: adjective collocations, FANBOYS coordinating conjunctions, and conjunctive connectors.",
        "lesson_title": "Adjectives, Conjunctions, and Simple Connectors",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "View of the Great Rift Valley Escarpment in Kenya",
                    "content": {
                        "title": "Scenic Landscape and Transport Corridor",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Great_Rift_Valley_Viewpoint%2C_Kenya.jpg/800px-Great_Rift_Valley_Viewpoint%2C_Kenya.jpg",
                        "caption": "The scenic landscape of the Great Rift Valley, illustrating vivid descriptive adjectives, natural collocations, and connective pathways.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Position adjectives accurately in attributive and predicative syntactic slots\n- Use natural English adjective-noun collocations (e.g., 'heavy rain', 'crucial decision')\n- Connect independent clauses using the 7 FANBOYS coordinating conjunctions and standard comma rules\n- Punctuate conjunctive adverbs (e.g., 'however', 'therefore', 'consequently') with semicolons and commas"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: Elevating Choppy Sentences",
                    "content": {
                        "text": "Compare these two writing samples:\n\n- **Choppy Draft:** *\"I want a career. It is in public service. It is hard. It is rewarding. I want to help citizens. I want to make a difference.\"*\n- **Polished Draft:** *\"I seek a **highly rewarding** career in **public** service, **for** it is both challenging **and** impactful; **consequently,** I am prepared to dedicate my skills to community development.\"*\n\nAdjectives supply vibrant detail, while conjunctions and connectors build seamless logical bridges between ideas."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Connectors & Collocations",
                    "content": {
                        "term": "Coordinating Conjunctions vs. Conjunctive Connectors",
                        "definition": "**Coordinating conjunctions (FANBOYS)** join elements of equal grammatical rank. When joining two independent clauses, a comma precedes the conjunction. **Conjunctive connectors** (e.g., *however, therefore*) are transition adverbs that require a preceding semicolon (or period) and a succeeding comma."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Conjunctions and Connective Systems",
                    "content": {
                        "headers": ["Connective Tool", "Members / Acronym", "Syntactic Function", "Punctuation Rule & Example"],
                        "rows": [
                            ["FANBOYS Conjunctions", "For, And, Nor, But, Or, Yet, So", "Joins independent clauses or parallel phrases", "Clause 1, + FANBOYS + Clause 2: 'The task was arduous, but the team prevailed.'"],
                            ["Attributive Adjective", "Before noun (scenic, diligent)", "Directly qualifies following noun", "We explored a scenic valley during the expedition."],
                            ["Predicative Adjective", "After linking verb (is, seems)", "Complements the subject noun", "The winding escarpment road was treacherous."],
                            ["Adjective Collocation", "Heavy rain, bitter regret, crucial issue", "Natural idiomatic partnership", "They made a crucial decision under pressure."],
                            ["Conjunctive Connector", "However, therefore, consequently, furthermore", "Links independent ideas logically", "Clause 1; connector, Clause 2: 'The rain stopped; however, fog lingered.'"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Adjectives, Conjunctions, and Sentence Connectors Matrix",
                    "content": {
                        "title": "Syntactic Bridge Architecture: FANBOYS & Conjunctive Adverbs",
                        "caption": "Visual breakdown of adjective placement, FANBOYS comma conventions, and semicolon-comma connector punctuation formulas.",
                        "svg_content": SVG_ADJECTIVES_CONJUNCTIONS_CONNECTORS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Punctuation Blueprint: Joining Independent Clauses",
                    "content": {
                        "intro": "Examine the two distinct standard methods for connecting two complete thoughts:",
                        "steps": [
                            "**Clause 1:** *'The software installation was successful.'* | **Clause 2:** *'The user manual was missing.'*",
                            "**Method A (Coordinating Conjunction):** Use a comma before a FANBOYS word: *'The software installation was successful**, but** the user manual was missing.'*",
                            "**Method B (Conjunctive Connector):** Use a semicolon before and a comma after: *'The software installation was successful**; however,** the user manual was missing.'*",
                            "**Common Error (Comma Splice):** ❌ *'The software installation was successful, however the user manual was missing.'* (Never connect with only a comma!)."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "FANBOYS and Coordinating Conjunctions",
                    "content": {
                        "title": "Coordinating Conjunctions and Punctuation Mastery",
                        "youtube_id": "nMQEq5wq3bQ",
                        "url": "https://www.youtube.com/watch?v=nMQEq5wq3bQ",
                        "description": "Engaging visual lesson breaking down the 7 FANBOYS conjunctions and when to insert commas."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Collocation & Connection Workshop",
                    "content": {
                        "title": "Editing Professional Articles and Essays",
                        "text": "**Pre-Viewing Focus:** Note the comma rule: When FANBOYS connects two words (e.g., *bread and butter*), no comma is needed. When it connects two full clauses (*Subject + Verb*), a comma is mandatory.\n\n**Post-Viewing Task:** Practice natural adjective collocations. In English, we say *heavy rain* (not *strong rain*), *high probability* (not *big probability*), and *deep regret* (not *tall regret*)."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Conjunction & Adjective Errors",
                    "content": {
                        "text": "### Error 1: The 'However' Comma Splice\n- **Incorrect:** *\"The meeting was adjourned, however the delegates continued discussing.\"*\n- **Correct:** *\"The meeting was adjourned**; however,** the delegates continued discussing.\"* OR *\"The meeting was adjourned**, but** the delegates continued...\"*\n\n### Error 2: Unnatural Adjective Collocations\n- **Incorrect:** *\"The student committed a **tall mistake** and felt **sour disappointment**.\"*\n- **Correct:** *\"The student committed a **grave mistake** and felt **bitter disappointment**.\"*\n\n### Error 3: Semicolon Preceding Coordinating Conjunctions\n- **Incorrect:** *\"The team played brilliantly; but they lost the final match.\"*\n- **Correct:** *\"The team played brilliantly**, but** they lost the final match.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Punctuation and Collocation Repair",
                    "content": {
                        "intro": "Analyze and rewrite these sentences to perfection:",
                        "steps": [
                            {"title": "Sentence 1: 'The road was closed due to (strong/dense) fog, therefore we took a detour.'", "description": "Correction: 'The road was closed due to **dense** fog**; therefore,** we took a detour.' (Collocation: dense fog; Semicolon + comma with therefore)."},
                            {"title": "Sentence 2: 'She felt a (bitter/sour) cold wind blowing across the escarpment.'", "description": "Correction: 'She felt a **bitterly** cold wind blowing...' (or '**bitter** cold wind')."},
                            {"title": "Sentence 3: 'We submitted the project on time (and/for) all tests passed successfully.'", "description": "Correction: 'We submitted the project on time**, and** all tests passed successfully.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Punctuating Sentence Connectors",
                    "content": {
                        "question": "Which of the following sentences is punctuated and structured 100% correctly?",
                        "options": [
                            "The research paper was thoroughly documented, it was rejected due to late submission.",
                            "The research paper was thoroughly documented; however, it was rejected due to late submission.",
                            "The research paper was thoroughly documented, however, it was rejected due to late submission.",
                            "The research paper was thoroughly documented; but it was rejected due to late submission."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: it joins two independent clauses with a conjunctive adverb ('however') correctly preceded by a semicolon and followed by a comma. Option A is a comma splice. Option C is also a comma splice. Option D incorrectly places a semicolon before the coordinating conjunction 'but'."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Identifying Natural Collocations",
                    "content": {
                        "question": "Select the sentence that utilizes accurate, standard English adjective-noun collocations:",
                        "options": [
                            "The cabinet reached a crucial decision following the heavy downpour that caused severe damage.",
                            "The cabinet reached a high decision following the strong rain that caused big damage.",
                            "The cabinet reached a heavy decision following the tall rain that caused wide damage.",
                            "The cabinet reached an enormous decision following the powerful rain that caused thick damage."
                        ],
                        "correct_answer": 0,
                        "explanation": "Option A uses natural collocations: 'crucial decision', 'heavy downpour', and 'severe damage'. The other options combine non-standard pairings (e.g., 'high decision', 'strong rain', 'tall rain', 'big damage')."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Adjectives** operate attributively (*before noun*) or predicatively (*after linking verb*); always employ standard **collocations**.\n- **FANBOYS** (*For, And, Nor, But, Or, Yet, So*) join independent clauses with a preceding comma: `Clause, + FANBOYS + Clause`.\n- **Conjunctive adverbs** (*however, therefore, consequently*) require a semicolon and comma: `Clause; connector, Clause`."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Noun and Verb Phrases
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Noun and Verb Phrases",
        "unit_description": "Constituent architecture of sentences: Head words, pre/postmodifiers in Noun Phrases (NP), and auxiliary systems in Verb Phrases (VP).",
        "lesson_title": "Noun and Verb Phrases",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Migratory Birds Soaring Over Lake Nakuru",
                    "content": {
                        "title": "Majestic Avian Migration in East Africa",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Lesser_Flamingos_Lake_Nakuru.jpg/800px-Lesser_Flamingos_Lake_Nakuru.jpg",
                        "caption": "Lesser flamingos in flight over Lake Nakuru, embodying complex noun phrases ('The majestic migratory birds of East Africa') and verb phrases ('have been flying swiftly southward').",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the core Head Noun and Head Verb in multi-word syntactic structures\n- Deconstruct Noun Phrases into Determiners, Premodifiers, Head Noun, and Postmodifiers\n- Assemble complex Verb Phrases using modal, perfect, and continuous auxiliary verbs\n- Apply the Pronoun Substitution Test to determine Noun Phrase boundaries"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: Expanding the Sentence Skeleton",
                    "content": {
                        "text": "Look at how a basic two-word sentence expands into sophisticated prose:\n\n> Basic: *\"Birds fly.\"*  \n> Expanded: *\"[**The majestic migratory birds of East Africa**] / [**have been flying swiftly southward**].\"*\n\n- The subject became a 7-word **Noun Phrase (NP)** anchored by the head noun *birds*.\n- The predicate became a 5-word **Verb Phrase (VP)** anchored by the main verb *flying*.\n- The foundational sentence structure remains identical: `NP + VP`!"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Phrases and Head Words",
                    "content": {
                        "term": "Noun Phrase (NP) & Verb Phrase (VP)",
                        "definition": "A **phrase** is a syntactic cluster of related words acting as a single unit without a subject-verb pair. A **Noun Phrase (NP)** is built around a central **Head Noun** that functions as subject, object, or complement. A **Verb Phrase (VP)** consists of a **Main Verb** plus optional auxiliary verbs expressing tense, aspect, and mood."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Constituent Anatomy of NP and VP",
                    "content": {
                        "headers": ["Phrase Element", "Constituent Slot", "Grammatical Function", "Structural Example"],
                        "rows": [
                            ["NP Determiner", "Initial slot (The, a, our, those)", "Specifies reference scope of head noun", "[The] young innovators..."],
                            ["NP Premodifiers", "Before head noun (adjectives/nouns)", "Describes qualities or subclassifies noun", "The [talented Kenyan] innovators..."],
                            ["NP Head Noun", "Core anchor (innovators)", "Carries primary semantic identity", "The talented Kenyan [INNOVATORS]..."],
                            ["NP Postmodifier", "After head noun (PP / relative clause)", "Provides contextual elaboration", "...innovators [from our school]..."],
                            ["VP Auxiliaries", "Before main verb (should have been)", "Signals modal intent, tense, and aspect", "...[should have been] researching..."],
                            ["VP Main Verb", "Semantic core (researching)", "Specifies fundamental action or state", "...should have been [RESEARCHING]..."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Noun and Verb Phrase Architecture",
                    "content": {
                        "title": "Anatomy of Noun Phrases (NP) and Verb Phrases (VP)",
                        "caption": "Comprehensive blueprint deconstructing NP slots (Determiner, Premodifiers, Head Noun, Postmodifiers) and VP auxiliary systems.",
                        "svg_content": SVG_NOUN_AND_VERB_PHRASES
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Step-by-Step Structural Analysis of an NP & VP",
                    "content": {
                        "intro": "Deconstruct this complex senior secondary sentence into constituent phrases:",
                        "steps": [
                            "**Target Sentence:** *'A brilliant young student from our class has won the national competition.'*",
                            "**1. Subject Noun Phrase (NP):** 'A brilliant young student from our class'",
                            "   - Determiner: *A* | Premodifiers: *brilliant young* | **Head Noun:** *student* | Postmodifier: *from our class* (PP)",
                            "**2. Verb Phrase (VP):** 'has won'",
                            "   - Auxiliary: *has* (Present Perfect marker) | **Main Verb:** *won*",
                            "**3. Object Noun Phrase (NP):** 'the national competition'",
                            "   - Determiner: *the* | Premodifier: *national* | **Head Noun:** *competition*",
                            "**Verification:** Substitute Subject NP with 'She': *'She has won the national competition.'* -> Structure intact!"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Phrase, Head Word, Noun Phrase & Verb Phrase",
                    "content": {
                        "title": "Linguistic Breakdown of Phrases and Head Words",
                        "youtube_id": "U3MNPEus5OA",
                        "url": "https://www.youtube.com/watch?v=U3MNPEus5OA",
                        "description": "Tutorial explaining syntactic trees, head words, and modifier clustering in English sentences."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Syntactic Substitution Lab",
                    "content": {
                        "title": "Testing Phrase Integrity with Pronoun Replacement",
                        "text": "**Pre-Viewing Focus:** Observe how linguists identify the boundary of an NP: if an entire 10-word phrase can be replaced by a single pronoun (*it*, *they*, *she*), the phrase is a unified Noun Phrase.\n\n**Post-Viewing Reflection:** Why is identifying the Head Noun essential for subject-verb agreement? In *'The collection of rare postage stamps **is** valuable'*, the singular head noun is *collection*, NOT *stamps*!"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Phrase Structure Errors",
                    "content": {
                        "text": "### Error 1: Mismatched Auxiliaries in Complex Verb Phrases\n- **Incorrect:** *\"The hikers **might has been lost** in the dense forest.\"*\n- **Correct:** *\"The hikers **might have been lost** in the dense forest.\"* *(Modals like 'might' are always followed by the base auxiliary 'have', never 'has').*\n\n### Error 2: Flawed Adjective Ordering in Premodifiers\n- **Incorrect:** *\"They purchased a **wooden round large beautiful** table.\"*\n- **Correct:** *\"They purchased a **beautiful large round wooden** table.\"* *(Order: Opinion -> Size -> Shape -> Material).*\n\n### Error 3: Agreement Confusion from Postmodifying Phrases\n- **Incorrect:** *\"The leader of the opposition parties **have** addressed the press.\"*\n- **Correct:** *\"The **leader** [of the opposition parties] **has** addressed the press.\"* *(Head noun is singular 'leader').*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Phrase Parsing & Construction",
                    "content": {
                        "intro": "Complete these phrase analysis tasks:",
                        "steps": [
                            {"title": "Task 1: Identify Head Noun: 'The new digital curriculum guidelines issued by KICD'", "description": "The Head Noun is 'guidelines'. 'The' = Det; 'new digital curriculum' = Premodifiers; 'issued by KICD' = Postmodifying participial phrase."},
                            {"title": "Task 2: Build a 3-Auxiliary Verb Phrase with 'explore'", "description": "Solution: 'The researchers **should have been exploring** the cave system.' (Modal 'should' + Perfect 'have' + Continuous 'been' + Main verb 'exploring')."},
                            {"title": "Task 3: Determine Syntactic Role of Bolded NP: 'The principal awarded **the hardworking athlete** a trophy.'", "description": "Solution: 'the hardworking athlete' receives the direct object ('a trophy') -> **Indirect Object Noun Phrase**."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Noun Phrase Head Word Identification",
                    "content": {
                        "question": "In the sentence 'The newly appointed director of clinical research at Kenyatta National Hospital spoke eloquently', what is the Head Noun of the subject Noun Phrase?",
                        "options": [
                            "research",
                            "director",
                            "hospital",
                            "clinical"
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct. 'Director' is the core Head Noun of the entire subject noun phrase. 'The newly appointed' are determiners and premodifiers, while 'of clinical research at Kenyatta National Hospital' is a compound postmodifying prepositional phrase."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Verb Phrase Auxiliary Sequencing",
                    "content": {
                        "question": "Which of the following verb phrases demonstrates grammatically perfect auxiliary sequencing?",
                        "options": [
                            "The aviation cadets must have been practicing simulation maneuvers.",
                            "The aviation cadets must has been practicing simulation maneuvers.",
                            "The aviation cadets must been have practicing simulation maneuvers.",
                            "The aviation cadets must having been practiced simulation maneuvers."
                        ],
                        "correct_answer": 0,
                        "explanation": "Option A is correct: Modal auxiliary ('must') + base perfect auxiliary ('have') + past participle auxiliary ('been') + present participle main verb ('practicing'). Modals cannot take 'has' or inverted auxiliary orders."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Noun Phrases (NP)** assemble around a **Head Noun**, framed by determiners, premodifiers (adjectives/nouns), and postmodifiers (PPs/clauses).\n- **Verb Phrases (VP)** assemble around a **Main Verb**, calibrated by modal, perfect, and progressive auxiliaries.\n- **Pronoun Substitution Test**: An entire valid NP can be substituted by a single pronoun without destroying grammatical coherence."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Adjective, Adverb, and Prepositional Phrases
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Adjective, Adverb, and Prepositional Phrases",
        "unit_description": "Descriptive and circumstantial modifiers: Adjective Phrases (AdjP), Adverb Phrases (AdvP), and multi-functional Prepositional Phrases (PP).",
        "lesson_title": "Adjective, Adverb, and Prepositional Phrases",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Professional Panel Conducting Formal Job Interview",
                    "content": {
                        "title": "Structured Professional Communication in Career Settings",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Job_interview_panel.jpg/800px-Job_interview_panel.jpg",
                        "caption": "A candidate responding during a formal interview, demonstrating descriptive adjective phrases ('eager for the role') and adverbial prepositional phrases ('with great confidence').",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Construct and analyze Adjective Phrases (AdjP) modifying nouns and pronouns\n- Build Adverb Phrases (AdvP) modifying verbs, adjectives, or other adverbs\n- Distinguish between Prepositional Phrases acting as Adjectival Phrases vs. Adverbial Phrases\n- Eliminate misplaced and dangling modifier phrases to ensure absolute sentence clarity"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: Transforming a Lifeless Narrative",
                    "content": {
                        "text": "Observe how descriptive phrases enrich a bare sentence:\n\n- **Bare Statement:** *\"The candidate answered questions.\"*\n- **Detailed Narrative:** *\"The candidate [**eager for the position** (AdjP)] answered questions [**exceptionally well** (AdvP)] [**during the morning interview** (PP)].\"*\n\n- *'eager for the position'* describes *which* candidate (AdjP).\n- *'exceptionally well'* describes *how* she answered (AdvP).\n- *'during the morning interview'* specifies *when* the action took place (Adverbial PP)."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Modifier Phrases",
                    "content": {
                        "term": "Adjective, Adverb & Prepositional Phrases",
                        "definition": "An **Adjective Phrase (AdjP)** has an adjective as its head and modifies a noun. An **Adverb Phrase (AdvP)** has an adverb head and modifies an action or adjective. A **Prepositional Phrase (PP)** starts with a preposition and ends with a noun phrase; it acts as an **adjective** (modifying nouns) or an **adverb** (modifying verbs)."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Modifier Phrases Function Matrix",
                    "content": {
                        "headers": ["Phrase Category", "Head / Structure", "Target Word Modified", "Diagnostic Test & Example"],
                        "rows": [
                            ["Adjective Phrase (AdjP)", "Head Adjective + Modifiers", "Noun or Pronoun", "Answers 'What kind?': 'a student [remarkably gifted in mathematics]'"],
                            ["Adverb Phrase (AdvP)", "Head Adverb + Degree words", "Verb, Adjective, or Adverb", "Answers 'How/To what degree?': 'The train moved [rather slowly].'"],
                            ["Adjectival PP", "Preposition + NP Object", "Modifies a NOUN", "Answers 'Which one?': 'The computers [in the main library] are fast.'"],
                            ["Adverbial PP", "Preposition + NP Object", "Modifies a VERB", "Answers 'When/Where/Why?': 'We registered [with great enthusiasm].'"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Adjective, Adverb, and Prepositional Phrases",
                    "content": {
                        "title": "Descriptive & Contextual Phrase Architecture",
                        "caption": "Functional mapping of AdjP, AdvP, and the dual adjectival/adverbial roles of Prepositional Phrases (PP).",
                        "svg_content": SVG_ADJ_ADV_PREP_PHRASES
                    }
                },
                {
                    "type": "worked_example",
                    "title": "The Arrow Test: Determining PP Function",
                    "content": {
                        "intro": "Use the 'Arrow Test' to classify Prepositional Phrases accurately:",
                        "steps": [
                            "**Sentence 1:** *'The program [**with a focus on digital literacy**] is popular.'*",
                            "   - Draw arrow from phrase to modified word: Arrow points to **program** (Noun).",
                            "   - **Classification:** **Prepositional Phrase acting as an Adjective (Adjectival Phrase)**.",
                            "**Sentence 2:** *'The students connected to the server [**with high-speed fiber cables**].'*",
                            "   - Draw arrow from phrase to modified word: Arrow points to **connected** (Verb).",
                            "   - **Classification:** **Prepositional Phrase acting as an Adverb (Adverbial Phrase of Manner)**."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "5 Types of Phrases in English Grammar",
                    "content": {
                        "title": "Phrase Classification: Adjective, Adverb & Prepositional",
                        "youtube_id": "eZ0AbITNbZQ",
                        "url": "https://www.youtube.com/watch?v=eZ0AbITNbZQ",
                        "description": "Comprehensive video breakdown of English phrase structures and identifying prepositional phrase functions."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Eliminating Misplaced Modifiers",
                    "content": {
                        "title": "Fixing Ambiguous Modifiers in Formal Reports",
                        "text": "**Pre-Viewing Focus:** Notice how misplaced prepositional phrases create absurd meanings: *'The security guard chased the intruder with a flashlight.'* (Did the intruder have the flashlight, or was the guard using it?).\n\n**Post-Viewing Task:** Rewrite misplaced phrases so they sit directly adjacent to the exact word they modify: *'Using a flashlight, the security guard chased the intruder.'*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Phrase Errors & Misplaced Modifiers",
                    "content": {
                        "text": "### Error 1: The Dangling Prepositional / Participial Phrase\n- **Incorrect:** *\"Walking across the campus, the library appeared majestic.\"* *(The library wasn't walking!).*\n- **Correct:** *\"Walking across the campus, **we** saw the majestic library.\"*\n\n### Error 2: Misplaced Adjectival Phrases\n- **Incorrect:** *\"The technician repaired the smartphone for the customer **with a cracked screen**.\"* *(Did the customer have a cracked screen?).*\n- **Correct:** *\"The technician repaired the **smartphone with a cracked screen** for the customer.\"*\n\n### Error 3: Adjective/Adverb Confusion\n- **Incorrect:** *\"The administrative team responded to the inquiry **very quick**.\"*\n- **Correct:** *\"The administrative team responded to the inquiry **very quickly**.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Phrase Classification & Modifier Repair",
                    "content": {
                        "intro": "Classify and repair these modifier structures:",
                        "steps": [
                            {"title": "Item 1: Classify: 'The athletic team trained [in the early morning hours].'", "description": "Analysis: Modifies the verb 'trained', indicating when. Classification: **Prepositional Phrase acting as an Adverb of Time**."},
                            {"title": "Item 2: Classify: 'The student [full of self-confidence] won the debate.'", "description": "Analysis: Head word is adjective 'full', modifying noun 'student'. Classification: **Adjective Phrase (AdjP)**."},
                            {"title": "Item 3: Repair Misplaced Phrase: 'She served tea to the guests in plastic cups.'", "description": "Repair: 'She served tea **in plastic cups** to the guests' (clarifies the tea was in cups, not the guests!)."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Classifying Prepositional Phrases",
                    "content": {
                        "question": "In the sentence below, identify the grammatical type and function of the bolded phrase: 'The talented software programmer designed a breakthrough educational application **in a matter of hours**.'",
                        "options": [
                            "Adjective Phrase modifying 'application'",
                            "Adverb Phrase modifying 'designed'",
                            "Prepositional Phrase acting as an Adjective modifying 'application'",
                            "Prepositional Phrase acting as an Adverb modifying 'designed'"
                        ],
                        "correct_answer": 3,
                        "explanation": "Option D is correct. 'In a matter of hours' begins with the preposition 'in' and concludes with the NP 'a matter of hours'. It modifies the action verb 'designed', specifying the timeframe (when/how quickly), making it a Prepositional Phrase acting as an Adverb."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Identifying Dangling/Misplaced Modifiers",
                    "content": {
                        "question": "Which of the following sentences is free from misplaced or dangling modifier phrase errors?",
                        "options": [
                            "Eager to inspect the new equipment, the laboratory was opened early by the science teacher.",
                            "The science teacher, eager to inspect the new equipment, opened the laboratory early.",
                            "Opened early by the science teacher, the new equipment was eager to be inspected.",
                            "The science teacher opened the laboratory for the students with modern digital microscopes."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: the adjective phrase 'eager to inspect the new equipment' directly modifies 'The science teacher', who is the logical actor performing the action. In Option A, the phrase illogically modifies 'the laboratory'."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Adjective Phrases (AdjP)** modify nouns/pronouns; **Adverb Phrases (AdvP)** modify verbs/adjectives/adverbs.\n- **Prepositional Phrases (PP)** play dual roles: **Adjectival** when modifying a noun (*'the book [on the desk]'*), and **Adverbial** when modifying a verb (*'sat [on the desk]'*).\n- Always position modifiers directly adjacent to their target words to avoid **misplaced** or **dangling** modifiers."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Relative and Adverbial Clauses
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Relative and Adverbial Clauses",
        "unit_description": "Complex clause architecture: Defining vs. Non-defining Relative Clauses, Adverbial clauses of time/reason/condition, and comma mechanics.",
        "lesson_title": "Relative and Adverbial Clauses",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Maasai Elders and Youth at Cultural Heritage Celebration",
                    "content": {
                        "title": "Community Traditions and Storytelling in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Maasai_cultural_celebration_Kenya.jpg/800px-Maasai_cultural_celebration_Kenya.jpg",
                        "caption": "Maasai community members gathered for traditional ceremonies, illustrating relative clauses ('elders whom the community admires') and adverbial clauses ('when celebrations begin').",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Formulate Defining (Restrictive) and Non-defining (Non-restrictive) Relative Clauses\n- Apply mandatory comma punctuation rules for non-defining relative clauses\n- Differentiate between relative pronouns (*who, whom, whose, which, that*)\n- Construct Adverbial Clauses of Time, Reason, Condition, and Concession with proper comma conventions"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: Connecting Community Narratives",
                    "content": {
                        "text": "Compare these two descriptive passages:\n\n- **Repetitive Clauses:** *\"We visited a sacred grove. The grove is near Nairobi. We met a respected elder. The elder shared oral histories. We listened carefully. We wanted to understand our heritage.\"*\n- **Cohesive Complex Syntax:** *\"We visited a sacred grove **which is located near Nairobi**. There, we met a respected elder **whom the community deeply admires**. We listened carefully **because we wanted to understand our cultural heritage**.\"*\n\nRelative and adverbial clauses transform disconnected facts into fluent, professional prose."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Relative & Adverbial Clauses",
                    "content": {
                        "term": "Defining vs. Non-Defining Relative Clauses",
                        "definition": "A **Defining Relative Clause** provides essential information needed to identify the noun; it uses **no commas** and can use *that* or *who*. A **Non-Defining Relative Clause** adds non-essential, parenthetical information; it **must be enclosed in commas** and uses *which* or *who* (never *that*)."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Clause Types and Subordinator Matrix",
                    "content": {
                        "headers": ["Clause Type", "Introductory Subordinator", "Punctuation Convention", "Academic Exemplar"],
                        "rows": [
                            ["Defining Relative Clause", "who, whom, whose, which, that", "NO COMMAS around clause", "The traditions [that unite our community] endure."],
                            ["Non-Defining Relative Clause", "who, whom, whose, which (NO 'that')", "COMMAS REQUIRED (before & after)", "My grandfather, [who is an elder], shared histories."],
                            ["Adverbial Clause of Time", "when, while, after, before, since", "Comma if placed before main clause", "When the harvest arrived, the festival commenced."],
                            ["Adverbial Clause of Reason", "because, since, as", "Comma only if clause leads sentence", "We preserved the forest because it protects our water."],
                            ["Adverbial Clause of Condition", "if, unless, provided that", "Comma if dependent clause comes first", "If we protect our heritage, future generations benefit."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Relative and Adverbial Clauses Architecture",
                    "content": {
                        "title": "Complex Clause Architecture: Relative vs. Adverbial Systems",
                        "caption": "Comprehensive guide detailing defining vs. non-defining relative clause rules and subordinating adverbial comma mechanics.",
                        "svg_content": SVG_RELATIVE_AND_ADVERBIAL_CLAUSES
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Punctuating Relative Clauses",
                    "content": {
                        "intro": "Analyze why comma placement changes the fundamental meaning of relative clauses:",
                        "steps": [
                            "**Case A (Defining):** *'The students **who completed the assignment** received commendation.'*",
                            "   - Meaning: *Only* those specific students who finished the assignment got commendation. Others did not. (No commas!).",
                            "**Case B (Non-Defining):** *'The students**, who completed the assignment,** received commendation.'*",
                            "   - Meaning: *All* the students received commendation; the fact that they completed the assignment is extra descriptive detail. (Commas mandatory!).",
                            "**Golden Rule:** Never use 'that' with commas in non-defining relative clauses!"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Defining vs Non-Defining Clauses: English Grammar",
                    "content": {
                        "title": "Mastering Relative Clauses and Comma Rules",
                        "youtube_id": "7MrwGO6jH6U",
                        "url": "https://www.youtube.com/watch?v=7MrwGO6jH6U",
                        "description": "Clear grammar lesson demonstrating the distinction between essential identifying clauses and non-essential descriptive clauses."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Adverbial Clause Inversion Lab",
                    "content": {
                        "title": "Practicing Subordinate Clause Comma Mechanics",
                        "text": "**Pre-Viewing Focus:** Note the comma rule for adverbial clauses:\n- `[Adverbial Clause], + [Independent Clause]` -> **Comma required!** (*'Although it rained heavily, the match continued.'*)\n- `[Independent Clause] + [Adverbial Clause]` -> **No comma!** (*'The match continued although it rained heavily.'*)\n\n**Post-Viewing Reflection:** Why does inverting a sentence change punctuation? When the dependent subordinator leads, the comma signals to the reader where the main thought begins."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Relative & Adverbial Clause Errors",
                    "content": {
                        "text": "### Error 1: Using 'That' in Non-Defining Clauses\n- **Incorrect:** *\"Mount Kenya, that is an extinct volcano, is the highest peak in Kenya.\"*\n- **Correct:** *\"Mount Kenya**, which is an extinct volcano,** is the highest peak in Kenya.\"*\n\n### Error 2: Missing Commas in Non-Defining Clauses\n- **Incorrect:** *\"My mother who lives in Kisumu visited us yesterday.\"*\n- **Correct:** *\"My mother**, who lives in Kisumu,** visited us yesterday.\"* *(You have only one mother; her residence is extra info).*\n\n### Error 3: Superfluous Commas Before Subordinate Clauses at End\n- **Incorrect:** *\"The match was cancelled, because the pitch was flooded.\"*\n- **Correct:** *\"The match was cancelled **because** the pitch was flooded.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Clause Combination and Punctuation",
                    "content": {
                        "intro": "Combine and punctuate these clauses:",
                        "steps": [
                            {"title": "Item 1: Combine using a defining relative pronoun: 'This is the sacred shrine. Elders gather here.'", "description": "Solution: 'This is the sacred shrine **where** elders gather' OR 'This is the sacred shrine **that/which** elders gather at.' (No commas)."},
                            {"title": "Item 2: Insert commas: 'Nairobi National Park which borders the capital city contains diverse wildlife.'", "description": "Solution: 'Nairobi National Park**, which borders the capital city,** contains diverse wildlife.' (Non-defining; commas required)."},
                            {"title": "Item 3: Combine with Adverbial Clause of Reason (fronted): 'The drought was severe. Farmers adopted drip irrigation.'", "description": "Solution: '**Because the drought was severe,** farmers adopted drip irrigation.' (Comma after fronted clause)."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Relative Clause Punctuation",
                    "content": {
                        "question": "Choose the sentence that is punctuated with complete grammatical accuracy:",
                        "options": [
                            "The Great Rift Valley, that spans thousands of kilometers, is a UNESCO World Heritage site.",
                            "The Great Rift Valley which spans thousands of kilometers is a UNESCO World Heritage site.",
                            "The Great Rift Valley, which spans thousands of kilometers, is a UNESCO World Heritage site.",
                            "The Great Rift Valley which spans thousands of kilometers, is a UNESCO World Heritage site."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct. The Great Rift Valley is a unique, specific proper noun. The relative clause provides non-essential descriptive information (non-defining), requiring it to be enclosed in commas and introduced by 'which' (never 'that')."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Adverbial Clause Comma Rules",
                    "content": {
                        "question": "Which sentence follows the standard comma rules for adverbial clauses?",
                        "options": [
                            "Unless you submit the registration form by Friday, you cannot participate in the symposium.",
                            "You cannot participate in the symposium, unless you submit the registration form by Friday.",
                            "Unless you submit the registration form by Friday you cannot participate in the symposium.",
                            "Because the internet network failed, so we postponed the virtual webinar."
                        ],
                        "correct_answer": 0,
                        "explanation": "Option A is correct: when an adverbial conditional clause ('Unless you submit...') leads the sentence, a comma separates it from the independent clause. Option B incorrectly inserts a comma before an ending adverbial clause. Option D incorrectly pairs 'Because' with 'so'."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 6 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Defining relative clauses** identify *which* noun and take **no commas** (*that/who*).\n- **Non-defining relative clauses** provide parenthetical detail, **require commas**, and use *which/who* (never *that*).\n- **Adverbial clauses** leading a sentence require a comma: `[Adverbial clause], + [Main clause]`."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7: Noun Clauses and Clause Functions
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Noun Clauses and Clause Functions",
        "unit_description": "Subordinate clauses acting as nominals: Subject of Verb, Direct Object, Subject Complement, Object of Preposition, and Appositive.",
        "lesson_title": "Noun Clauses and Clause Functions",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Celebrating School Sports Championship",
                    "content": {
                        "title": "Academic and Athletic Achievements in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/African_Youth_Sports_Team_Championship.jpg/800px-African_Youth_Sports_Team_Championship.jpg",
                        "caption": "Students celebrating team victory, illustrating embedded noun clauses ('I heard that our school won the tournament' and 'What they accomplished was historic').",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify Noun Clauses and distinguish them from Relative and Adverbial Clauses\n- Analyze the 5 primary syntactic functions of Noun Clauses in sentences\n- Apply the 'Something / It' Replacement Test to verify Noun Clause identity\n- Maintain statement word order (Subject + Verb) in indirect question noun clauses"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: Replacing Single Nouns with Full Clauses",
                    "content": {
                        "text": "Observe how an entire clause can perform the role of a single noun:\n\n- **Single Noun as Object:** *\"I heard **the news**.\"*\n- **Noun Clause as Object:** *\"I heard [**that our school team won the championship**].\"*\n\nAlthough *'that our school team won the championship'* contains its own subject (*team*) and verb (*won*), the entire clause acts as a single noun—the **Direct Object** of the main verb *heard*!"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Noun Clauses",
                    "content": {
                        "term": "Noun Clause (Nominal Clause)",
                        "definition": "A **Noun Clause** is a dependent clause that performs the exact grammatical function of a noun in a sentence. It is introduced by subordinators such as *that, whether, if, what, how, why, who, whichever*."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The 5 Syntactic Roles of Noun Clauses",
                    "content": {
                        "headers": ["Syntactic Role", "Position in Sentence", "Diagnostic Replacement Test", "Academic Exemplar"],
                        "rows": [
                            ["Subject of the Verb", "Before the main predicate verb", "[Something] was inspiring.", "[What the guest speaker shared] inspired everyone."],
                            ["Direct Object", "After a transitive action verb", "I know [something].", "The principal announced [that school fees would remain unchanged]."],
                            ["Subject Complement", "After a linking verb (is, was, seems)", "Our goal is [this].", "The primary challenge is [that resources are limited]."],
                            ["Object of a Preposition", "Immediately following a preposition", "They spoke about [it].", "The committee debated on [how the funds should be allocated]."],
                            ["Appositive", "Renames preceding noun", "The rumor [something] spread.", "The news, [that we won first prize], delighted the class."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Noun Clauses: 5 Syntactic Functions",
                    "content": {
                        "title": "Noun Clause Architecture & 5 Syntactic Roles",
                        "caption": "Structural diagram illustrating Subject, Direct Object, Subject Complement, Object of Preposition, and Appositive functions alongside the 'Something/It' test.",
                        "svg_content": SVG_NOUN_CLAUSES_FUNCTIONS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Parsing Noun Clause Functions",
                    "content": {
                        "intro": "Determine the exact grammatical function of the bracketed clause in this sentence:",
                        "steps": [
                            "**Target Sentence:** *'The success of the environmental project depends largely on [**how effectively the community participates**].'*",
                            "**Step 1: Identify Preceding Word:** The clause immediately follows the preposition *'on'*.",
                            "**Step 2: Apply Replacement Test:** *'The success of the project depends largely on [**it / this factor**].'* -> Perfect grammatical match!",
                            "**Step 3: Internal Structure:** 'how effectively' (subordinator/adverb) + 'the community' (Subject) + 'participates' (Verb).",
                            "**Syntactic Verdict:** **Noun Clause functioning as the Object of the Preposition 'on'**."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Noun Clauses | Grammar Lesson",
                    "content": {
                        "title": "Understanding Nominal Clauses and Functions",
                        "youtube_id": "aVxN5FTUKwI",
                        "url": "https://www.youtube.com/watch?v=aVxN5FTUKwI",
                        "description": "Comprehensive guide illustrating how noun clauses operate across subjects, direct objects, and complements."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Indirect Question Word Order",
                    "content": {
                        "title": "Fixing Inverted Word Order in Noun Clauses",
                        "text": "**Pre-Viewing Focus:** Notice that when a question becomes a noun clause (an indirect question), it loses its auxiliary inversion and adopts regular statement word order (*Subject + Verb*):\n- Direct Question: *\"Where **is the library**?\"*\n- Noun Clause: *\"Can you tell me where **the library is**?\"* (NOT *\"where is the library\"*).\n\n**Post-Viewing Reflection:** Why is *'She asked what was the time'* incorrect in formal English? In indirect discourse, the noun clause requires statement syntax: *'She asked what the time was.'*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Noun Clause Pitfalls",
                    "content": {
                        "text": "### Error 1: Using Question Word Order in Indirect Noun Clauses\n- **Incorrect:** *\"The teacher asked me why **did I miss** yesterday's lesson.\"*\n- **Correct:** *\"The teacher asked me why **I had missed** yesterday's lesson.\"*\n\n### Error 2: Confusing Relative Clauses with Noun Clauses\n- **Relative Clause (modifies noun):** *\"I know the reason [**why she resigned**].\"* *(Modifies 'reason').*\n- **Noun Clause (is the object):** *\"I know [**why she resigned**].\"* *(Acts as direct object of 'know').*\n\n### Error 3: Omitting 'That' in Formal Academic Subjects\n- **Informal/Awkward:** *\"The climate is warming is undeniable.\"*\n- **Formal Noun Clause:** *\"**That the climate is warming** is undeniable.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Noun Clause Function & Word Order",
                    "content": {
                        "intro": "Analyze and correct these sentences:",
                        "steps": [
                            {"title": "Item 1: Correct Word Order: 'Could you explain how did you solve this calculus equation?'", "description": "Correction: 'Could you explain **how you solved** this calculus equation?' (Statement order: Subject + Verb)."},
                            {"title": "Item 2: Identify Function: '[That physical exercise enhances cognitive function] has been proven by medical research.'", "description": "Analysis: Precedes main verb 'has been proven'. Function: **Subject of the Verb**."},
                            {"title": "Item 3: Identify Function: 'The principal's major concern was [whether students had sufficient textbooks].'", "description": "Analysis: Follows linking verb 'was' and renames concern. Function: **Subject Complement**."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Noun Clause Syntactic Function",
                    "content": {
                        "question": "In the sentence 'The medical board reached a final verdict on what the primary cause of the outbreak was', what is the grammatical function of the bolded noun clause?",
                        "options": [
                            "Subject of the Verb",
                            "Direct Object of the Verb",
                            "Object of a Preposition",
                            "Subject Complement"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct. The noun clause 'what the primary cause of the outbreak was' immediately follows the preposition 'on', functioning as the Object of the Preposition."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Word Order in Embedded Noun Clauses",
                    "content": {
                        "question": "Select the sentence that uses correct statement word order in its embedded noun clause:",
                        "options": [
                            "The technician inquired where had the server backup files been stored.",
                            "The technician inquired where the server backup files had been stored.",
                            "The technician inquired where did they store the server backup files.",
                            "The technician inquired where was the server backup files stored."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct. An embedded noun clause requires statement word order: Subject ('the server backup files') + Verb ('had been stored'), avoiding inverted question auxiliaries ('where had...', 'where did...')."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 7 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Noun Clauses** function identically to single nouns across 5 positions: *Subject, Direct Object, Subject Complement, Object of Preposition, Appositive*.\n- **The 'Something / It' Test**: If an entire clause can be replaced by *'something'* or *'it'*, it is a Noun Clause.\n- **Indirect question word order**: Always utilize standard statement syntax (*Subject + Verb*) inside noun clauses."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8: Simple Sentence Structure and Sentence Parts
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Simple Sentence Structure and Sentence Parts",
        "unit_description": "Anatomy of the simple sentence: Subject, Verb, Direct/Indirect Objects, Complements, Adjuncts, and core patterns (SVO, SVIODO, SVC, SVOA).",
        "lesson_title": "Simple Sentence Structure and Sentence Parts",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "First Aid and Emergency Health Training in Kenya",
                    "content": {
                        "title": "Healthcare Training and Practical First Aid",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/First_aid_training_in_Kenya.jpg/800px-First_aid_training_in_Kenya.jpg",
                        "caption": "Students practicing emergency first aid procedures, illustrating clear simple sentence patterns ('The instructor demonstrated the technique' and 'She handed the patient medicine').",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the core constituents of a simple sentence: Subject (S), Verb (V), Direct Object (DO), Indirect Object (IO), Complement (C), and Adjunct (A)\n- Differentiate between Direct Objects, Indirect Objects, and Complements\n- Classify and construct the 4 primary sentence patterns: S-V-O, S-V-IO-DO, S-V-C, and S-V-O-A\n- Ensure every simple sentence expresses a grammatically complete, unified thought"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: The First Aid Incident",
                    "content": {
                        "text": "Look at how sentence parts assemble in a medical training scenario:\n\n- *\"[**The instructor** (S)] [**handed** (V)] [**the students** (IO)] [**the first-aid kit** (DO)] [**yesterday** (A)].\"*\n\n- **Subject (S):** Who performed the action? -> *The instructor*\n- **Verb (V):** What did they do? -> *handed*\n- **Indirect Object (IO):** To whom? -> *the students*\n- **Direct Object (DO):** What did they hand? -> *the first-aid kit*\n- **Adjunct (A):** When? -> *yesterday*"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Simple Sentence & Complements",
                    "content": {
                        "term": "Simple Sentence & Complement vs. Object",
                        "definition": "A **Simple Sentence** consists of a single independent clause with a subject and a finite verb. An **Object** receives the verb's action, while a **Complement** renames or describes the subject (*Subject Complement* after a linking verb) or the object (*Object Complement*)."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Core Sentence Patterns and Constituent Roles",
                    "content": {
                        "headers": ["Sentence Pattern", "Constituent Breakdown", "Verb Type Involved", "Exemplar Sentence"],
                        "rows": [
                            ["S - V - O", "Subject + Verb + Direct Object", "Monotransitive Verb", "The medical team cleaned the laboratory."],
                            ["S - V - IO - DO", "Subject + Verb + Indirect Obj + Direct Obj", "Ditransitive Verb", "The nurse gave the patient some clean water."],
                            ["S - V - C (Subject Comp)", "Subject + Linking Verb + Subject Complement", "Linking / Copular Verb (is, became)", "Mental health is crucial for overall wellness."],
                            ["S - V - O - C (Object Comp)", "Subject + Transitive Verb + Object + Complement", "Complex Transitive Verb", "The committee elected Mr. Omondi chairperson."],
                            ["S - V - O - A", "Subject + Verb + Object + Adjunct (Adverbial)", "Transitive Verb + Circumstance", "He placed the first-aid kit on the shelf."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Simple Sentence Structure and Patterns",
                    "content": {
                        "title": "Anatomy of the Simple Sentence & 4 Essential Patterns",
                        "caption": "Constituent breakdown of S, V, DO, IO, C, A and visual schematics for S-V-O, S-V-IO-DO, S-V-C, and S-V-O-A sentence patterns.",
                        "svg_content": SVG_SIMPLE_SENTENCE_PARTS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Parsing Sentence Constituents",
                    "content": {
                        "intro": "Break down and classify each constituent in this emergency response sentence:",
                        "steps": [
                            "**Target Sentence:** *'The emergency medical technician gave the injured athlete an ice pack immediately.'*",
                            "**1. Subject (S):** 'The emergency medical technician' (NP performing action).",
                            "**2. Verb (V):** 'gave' (Ditransitive action verb in Past Simple).",
                            "**3. Indirect Object (IO):** 'the injured athlete' (Answers: *To whom was the item given?*).",
                            "**4. Direct Object (DO):** 'an ice pack' (Answers: *What entity was given?*).",
                            "**5. Adjunct (A):** 'immediately' (Adverb of time modifying the action).",
                            "**Pattern Verdict:** **S - V - IO - DO - A**."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Sentence Organization and Paragraph Structure",
                    "content": {
                        "title": "Sentence Parts: Subject, Predicate & Objects",
                        "youtube_id": "2ftKIIJQjf0",
                        "url": "https://www.youtube.com/watch?v=2ftKIIJQjf0",
                        "description": "Video tutorial examining subjects, predicates, direct/indirect objects, and sentence building blocks."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Differentiating Complements and Objects",
                    "content": {
                        "title": "Object vs. Complement Diagnostic Lab",
                        "text": "**Pre-Viewing Focus:** Notice the difference between a Direct Object and a Subject Complement:\n- Object: *'The doctor treated **the patient**.'* (The doctor ≠ the patient; 'patient' receives the action).\n- Subject Complement: *'The doctor became **a specialist**.'* (The doctor = a specialist; 'specialist' renames the subject).\n\n**Post-Viewing Reflection:** Why can a linking verb never take a Direct Object? Because linking verbs express a state of being or equality, not an action passing across to a receiver."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Sentence Pattern Pitfalls",
                    "content": {
                        "text": "### Error 1: Confusing Indirect Objects with Prepositional Phrases\n- **S-V-IO-DO Form:** *\"The school gave **the students** textbooks.\"* *(No preposition).* \n- **S-V-DO-PP Form:** *\"The school gave textbooks **to the students**.\"* *('to the students' is a Prepositional Phrase, not a grammatical IO).* \n\n### Error 2: Treating Incomplete Clauses as Simple Sentences (Fragments)\n- **Incorrect Fragment:** *\"Because the road was blocked by landslides.\"* *(Dependent clause only).* \n- **Complete Simple Sentence:** *\"The road was blocked by landslides.\"* \n\n### Error 3: Mismatched Linking Verbs with Action Objects\n- **Incorrect:** *\"The patient felt **a medicine**.\"* *(Illogical object).* \n- **Correct:** *\"The patient felt **dizzy** (SVC)\"* OR *\"The patient took **the medicine** (SVO).\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Classifying Sentence Patterns",
                    "content": {
                        "intro": "Analyze and classify the structural pattern of each sentence:",
                        "steps": [
                            {"title": "Sentence 1: 'The clinical officer placed the sterilised instruments in the metal tray.'", "description": "Subject: 'The clinical officer' | Verb: 'placed' | Object: 'the sterilised instruments' | Adjunct: 'in the metal tray' -> Pattern: **S - V - O - A**."},
                            {"title": "Sentence 2: 'Proper hygiene remains essential in disease prevention.'", "description": "Subject: 'Proper hygiene' | Linking Verb: 'remains' | Subject Complement: 'essential' | Adjunct: 'in disease prevention' -> Pattern: **S - V - C - A**."},
                            {"title": "Sentence 3: 'The governing council appointed Dr. Mwangi chief medical superintendent.'", "description": "Subject: 'The governing council' | Verb: 'appointed' | Object: 'Dr. Mwangi' | Object Complement: 'chief medical superintendent' -> Pattern: **S - V - O - C**."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Sentence Pattern Identification",
                    "content": {
                        "question": "Identify the structural sentence pattern of the following statement: 'The head teacher awarded the disciplined learner a certificate of merit yesterday.'",
                        "options": [
                            "S - V - O - A",
                            "S - V - IO - DO - A",
                            "S - V - C - A",
                            "S - V - O - C"
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct. 'The head teacher' (Subject) + 'awarded' (Verb) + 'the disciplined learner' (Indirect Object) + 'a certificate of merit' (Direct Object) + 'yesterday' (Adjunct of time)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Direct Object vs. Subject Complement",
                    "content": {
                        "question": "Which of the following sentences follows the S - V - C (Subject-Verb-Complement) pattern?",
                        "options": [
                            "The paramedic examined the emergency kit thoroughly.",
                            "The paramedic handed the casualty a warm blanket.",
                            "The paramedic appeared exceptionally calm under pressure.",
                            "The paramedic placed the stretcher inside the ambulance."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: 'The paramedic' (Subject) + 'appeared' (Linking Verb) + 'exceptionally calm' (Subject Complement describing the subject) + 'under pressure' (Adjunct). Options A, B, and D involve action verbs with objects."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 8 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- Every **Simple Sentence** contains a single independent clause built around an essential **Subject** and **Finite Verb**.\n- Master the 4 core patterns: **SVO** (*Action + Object*), **SVIODO** (*Action + Recipient + Object*), **SVC** (*Linking + Complement*), and **SVOA** (*Action + Object + Setting*).\n- **Objects** receive action; **Complements** rename or describe states of being."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 9: Sentence Fluency: Fragments, Run-ons, Comma Splices, and Transformation
    # =========================================================================
    {
        "unit_order": 9,
        "unit_name": "Sentence Fluency: Fragments, Run-ons, Comma Splices, and Transformation",
        "unit_description": "Diagnosing and repairing sentence-boundary errors: Fragments, Fused Run-ons, and Comma Splices; transforming sentences for fluency and rhythm.",
        "lesson_title": "Sentence Fluency: Fragments, Run-ons, Comma Splices, and Transformation",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Secondary Students Editing Essays in Writing Workshop",
                    "content": {
                        "title": "Collaborative Peer Review and Editing",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Students_writing_in_classroom_Kenya.jpg/800px-Students_writing_in_classroom_Kenya.jpg",
                        "caption": "Students proofreading and revising composition drafts, identifying sentence fragments, run-ons, and comma splices to achieve stylistic fluency.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 9 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Diagnose and rectify Sentence Fragments by attaching missing subjects, verbs, or main clauses\n- Identify and resolve Run-on (Fused) sentences using punctuation and coordinating conjunctions\n- Eliminate Comma Splices using 3 standard grammatical repair methods\n- Transform repetitive, choppy sentences into fluent, rhythmically varied paragraphs"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: The Disjointed Essay Draft",
                    "content": {
                        "text": "Read this unedited student draft from an IT assignment:\n\n> *\"The computer lab was crowded. Because many students wanted to finish their IT assignments. They sat at the terminals, they typed furiously time was running out.\"*\n\n- *'Because many students...'*: **Fragment** (stranded dependent clause).\n- *'They sat at the terminals, they typed furiously'*: **Comma Splice** (two clauses joined only by a comma).\n- *'they typed furiously time was running out'*: **Run-on** (two clauses colliding without punctuation).\n\n**Polished Transformation:** *\"The computer lab was crowded **because** many students wanted to finish their IT assignments. They sat at the terminals **and** typed furiously **while** time was running out.\"*"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Sentence Boundary Errors",
                    "content": {
                        "term": "Fragments, Run-ons & Comma Splices",
                        "definition": "A **Sentence Fragment** is an incomplete sentence missing a subject, a finite verb, or a complete thought. A **Run-on (Fused) Sentence** joins two independent clauses with no punctuation. A **Comma Splice** attempts to join two independent clauses with only a comma."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Error Diagnosis and Repair Toolkit",
                    "content": {
                        "headers": ["Error Type", "Structural Flaw", "Standard Repair Strategy", "Before & After Example"],
                        "rows": [
                            ["Sentence Fragment", "Dependent clause or phrase standing alone without main clause", "Attach to adjacent main clause or add missing subject/verb", "❌ 'Since we arrived late.' -> ✔ 'Since we arrived late, we missed the introduction.'"],
                            ["Run-on (Fused) Sentence", "Two complete independent clauses with zero punctuation", "Insert period, semicolon, or comma + FANBOYS conjunction", "❌ 'The wifi failed we rebooted.' -> ✔ 'The wifi failed; we rebooted.'"],
                            ["Comma Splice", "Two independent clauses joined by only a weak comma", "1. Comma + FANBOYS\n2. Semicolon\n3. Subordinating clause", "❌ 'The server crashed, data was saved.' -> ✔ 'The server crashed, but data was saved.'"],
                            ["Conjunctive Adverb Splice", "Using 'however/therefore' with only commas", "Change first comma to a semicolon; keep comma after connector", "❌ 'It rained, therefore we stayed.' -> ✔ 'It rained; therefore, we stayed.'"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Sentence Fluency & Boundary Repair",
                    "content": {
                        "title": "Sentence Fluency Architecture: Diagnosing & Repairing Errors",
                        "caption": "Diagnostic framework and 3-formula repair matrix for fixing sentence fragments, run-on sentences, and comma splices.",
                        "svg_content": SVG_SENTENCE_FLUENCY_REPAIR
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: The 3 Comma Splice Repair Formulas",
                    "content": {
                        "intro": "Demonstrate the 3 distinct standard methods for repairing a comma splice:",
                        "steps": [
                            "**Faulty Sentence (Comma Splice):** *'The emergency siren sounded, the students evacuated the hall.'*",
                            "**Repair Formula 1 (Comma + FANBOYS):** *'The emergency siren sounded**, so** the students evacuated the hall.'*",
                            "**Repair Formula 2 (Semicolon):** *'The emergency siren sounded**;** the students evacuated the hall.'*",
                            "**Repair Formula 3 (Subordination):** *'**When** the emergency siren sounded, the students evacuated the hall.'*",
                            "All 3 formulas transform a grammatical defect into fluent, polished academic prose."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Run-on Sentences, Comma Splices, and Fragments",
                    "content": {
                        "title": "Diagnosing and Fixing Sentence Boundary Errors",
                        "youtube_id": "eHxgH_KLHko",
                        "url": "https://www.youtube.com/watch?v=eHxgH_KLHko",
                        "description": "Interactive video showing step-by-step techniques to detect and repair fragments, run-on sentences, and comma splices."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Sentence Variety and Rhythm",
                    "content": {
                        "title": "Transforming Monotonous Paragraphs",
                        "text": "**Pre-Viewing Focus:** Notice how consecutive short simple sentences sound robotic: *'We woke up. We ate breakfast. We walked to school. We entered the lab.'*\n\n**Post-Viewing Reflection:** Transform monotonous structures by combining simple, compound, and complex sentences: *'After eating a quick breakfast, we walked to school and entered the IT lab, eager to begin our robotics experiment.'*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Sentence Boundary Pitfalls",
                    "content": {
                        "text": "### Error 1: Participial Phrase Fragment\n- **Incorrect:** *\"Working late into the night on the coding project.\"* *(Missing subject and finite auxiliary).* \n- **Correct:** *\"**We were** working late into the night on the coding project.\"* OR *\"Working late into the night on the coding project, **the team completed the app**.\"* \n\n### Error 2: Fused Conjunctions\n- **Incorrect:** *\"Although she was fatigued, but she finished the race.\"* *(Double connector: never use 'although' and 'but' together!).* \n- **Correct:** *\"Although she was fatigued, she finished the race.\"* \n\n### Error 3: Splice with Transitional Adverbs\n- **Incorrect:** *\"The software is free, however you must register to download it.\"* \n- **Correct:** *\"The software is free**; however,** you must register to download it.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Diagnosing & Repairing Errors",
                    "content": {
                        "intro": "Diagnose the error in each item and provide the corrected version:",
                        "steps": [
                            {"title": "Item 1: 'The power went out during the exam many learners lost their unsaved work.'", "description": "Diagnosis: **Run-on (Fused) sentence**. Repair: 'The power went out during the exam**; consequently,** many learners lost their unsaved work.' (or use 'so')."},
                            {"title": "Item 2: 'Although the team practiced diligently for six months.'", "description": "Diagnosis: **Sentence Fragment**. Repair: 'Although the team practiced diligently for six months, **they were narrowly defeated in the finals**.'"},
                            {"title": "Item 3: 'The library is quiet, it provides an ideal study space.'", "description": "Diagnosis: **Comma Splice**. Repair: 'The library is quiet**, and** it provides an ideal study space' (or use semicolon ';')."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Comma Splices",
                    "content": {
                        "question": "Which of the following items represents a grammatically flawed Comma Splice?",
                        "options": [
                            "The database crashed unexpectedly, but all user records were successfully preserved.",
                            "The database crashed unexpectedly; however, all user records were successfully preserved.",
                            "The database crashed unexpectedly, all user records were successfully preserved.",
                            "Because the database crashed unexpectedly, the IT team initiated a complete restore."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is a classic comma splice: two complete independent clauses ('The database crashed unexpectedly' and 'all user records were successfully preserved') joined only with a comma, lacking a coordinating conjunction or semicolon."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Sentence Fragment Rectification",
                    "content": {
                        "question": "Choose the option that successfully rectifies the sentence fragment: 'Which has significantly enhanced our school internet connectivity.'",
                        "options": [
                            "Our school installed a modern fiber-optic cable. Which has significantly enhanced our school internet connectivity.",
                            "Our school installed a modern fiber-optic cable, which has significantly enhanced our school internet connectivity.",
                            "Our school installed a modern fiber-optic cable which, has significantly enhanced our school internet connectivity.",
                            "Which has significantly enhanced our school internet connectivity; our school installed fiber-optic cables."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: the stranded relative clause is properly connected as a non-defining relative clause modifying the entire preceding action, correctly preceded by a comma."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 9 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Sentence Fragments** lack an independent clause; attach them to main clauses or supply the missing subject/verb.\n- **Run-ons** fuse clauses with no punctuation; separate them with full stops, semicolons, or coordinating conjunctions.\n- **Comma Splices** weakly join independent clauses with only a comma; repair via: `[, + FANBOYS]`, `[; (semicolon)]`, or `[Subordination]`."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 10: Active/Passive Sentences and Subject–Verb Agreement
    # =========================================================================
    {
        "unit_order": 10,
        "unit_name": "Active/Passive Sentences and Subject–Verb Agreement",
        "unit_description": "Voice mechanics and grammatical harmony: Active vs. Passive transformations, tricky singulars ending in '-s', and proximity agreement rules.",
        "lesson_title": "Active/Passive Sentences and Subject–Verb Agreement",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Conducting Chemistry Laboratory Experiment",
                    "content": {
                        "title": "Scientific Investigation and Objective Reporting",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Science_Laboratory_Students_Kenya.jpg/800px-Science_Laboratory_Students_Kenya.jpg",
                        "caption": "Students conducting chemical titrations in a school science laboratory, demonstrating passive voice in formal lab reports ('The solution was heated') and strict subject-verb agreement.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 10 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Transform sentences accurately between Active and Passive Voice across various tenses\n- Identify appropriate stylistic contexts for active voice (directness) vs. passive voice (objective/formal)\n- Apply Subject-Verb Agreement rules for tricky singular nouns ending in '-s' (e.g., *mathematics, economics, news*)\n- Maintain subject-verb agreement across intervening prepositional phrases and correlative pairs (*either...or, neither...nor*)"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: Active vs. Passive Voice in Incident Reports",
                    "content": {
                        "text": "Consider how voice changes focus and tone in an institutional report:\n\n- **Active Voice:** *\"An unknown intruder **hacked** the server last night.\"*  \n  *(Focus is directly on the actor: 'An unknown intruder').*\n- **Passive Voice:** *\"The server **was hacked** last night.\"*  \n  *(Focus shifts to the receiver and the action; the actor is omitted or deprioritized).* \n\nActive voice is energetic and direct; passive voice is indispensable in formal incident reports, scientific procedures, and legal summaries."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Voice and Agreement",
                    "content": {
                        "term": "Passive Voice & Subject-Verb Agreement (SVA)",
                        "definition": "In **Active Voice**, the subject performs the action. In **Passive Voice**, the subject receives the action (`Object + Form of 'Be' + Past Participle`). **Subject-Verb Agreement** requires a finite verb to match the grammatical number (singular or plural) of its true head subject."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Subject-Verb Agreement Rules Matrix",
                    "content": {
                        "headers": ["Rule Category", "Grammatical Principle", "Common Pitfall", "Correct Exemplar"],
                        "rows": [
                            ["Nouns Ending in '-s'", "Singular subjects (economics, physics, news, mathematics)", "Treating as plural due to '-s'", "Mathematics [is] required for computer science."],
                            ["Intervening Phrase", "Head subject determines verb, NOT the noun in PP", "Agreeing with the nearest noun", "The cost [of new computers and routers] [has] risen."],
                            ["Correlative Conjunctions", "With 'Either...or' / 'Neither...nor', verb agrees with CLOSER subject", "Always choosing plural", "Neither the teacher nor the [students were] aware."],
                            ["Collective Nouns", "Singular when acting as 1 unit; plural when acting individually", "Inconsistent pronoun/verb shifts", "The committee [has] approved the annual budget."],
                            ["Titles & Company Names", "Titles of books, films, organizations are singular", "Pluralizing compound titles", "'Gulliver's Travels' [is] a famous satirical novel."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Voice and Agreement Mastery Matrix",
                    "content": {
                        "title": "Voice Transformation Mechanics & Subject-Verb Agreement Rules",
                        "caption": "Structural guide illustrating Active-to-Passive voice mechanics and 4 critical Subject-Verb Agreement rules.",
                        "svg_content": SVG_VOICE_AND_AGREEMENT
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Active to Passive Transformation",
                    "content": {
                        "intro": "Transform this active sentence through the standard 4-step passive algorithm:",
                        "steps": [
                            "**Active Sentence:** *'The school security team [Subject] monitors [Verb - Simple Present] the main gate [Object] 24 hours a day.'*",
                            "**Step 1: Move Object to Subject:** *'The main gate'* becomes the new subject.",
                            "**Step 2: Determine Tense & Insert 'Be':** Verb 'monitors' is Simple Present; singular subject requires *'is'*.",
                            "**Step 3: Convert Main Verb to Past Participle:** 'monitors' -> *'monitored'*.",
                            "**Step 4: Add Optional Agent by-Phrase:** *'by the school security team'*.",
                            "**Passive Result:** *'The main gate **is monitored** 24 hours a day (by the school security team).'*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Grammar Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Active and Passive Voice In English Grammar",
                    "content": {
                        "title": "Voice Transformation Rules Across All Tenses",
                        "youtube_id": "Pa8eZziCNrk",
                        "url": "https://www.youtube.com/watch?v=Pa8eZziCNrk",
                        "description": "Comprehensive video lesson explaining tense-specific transformations between active and passive voice."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Lab: Scientific & Formal Reporting",
                    "content": {
                        "title": "Stylistic Choice: When to Use Passive Voice",
                        "text": "**Pre-Viewing Focus:** Pay attention to how the auxiliary verb *be* shifts across tenses: Simple Present (*is/are*), Past (*was/were*), Present Perfect (*has/have been*), Future (*will be*).\n\n**Post-Viewing Reflection:** Why do laboratory reports favor passive voice (*'10 ml of acid was added to the solution'*) over active voice (*'I added 10 ml of acid'* )? Passive voice emphasizes objective methodology over personal identity."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Voice & Agreement Pitfalls",
                    "content": {
                        "text": "### Error 1: Proximity Agreement Error (Intervening Phrases)\n- **Incorrect:** *\"A large shipment of computers and laptops **have** arrived.\"*\n- **Correct:** *\"A large **shipment** [of computers and laptops] **has** arrived.\"* *(Subject is 'shipment', not 'computers').*\n\n### Error 2: Faulty Agreement with Plural-Form Academic Nouns\n- **Incorrect:** *\"Economics **are** my favorite subject in secondary school.\"*\n- **Correct:** *\"Economics **is** my favorite subject in secondary school.\"*\n\n### Error 3: Awkward/Unnecessary Passive Construction\n- **Awkward:** *\"A delicious dinner was prepared and eaten by me.\"*\n- **Natural Active:** *\"I prepared and ate a delicious dinner.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Agreement & Voice Transformation",
                    "content": {
                        "intro": "Complete these grammar practice items:",
                        "steps": [
                            {"title": "Item 1: Choose Verb: 'The news concerning the national examinations (is/are) encouraging.'", "description": "Analysis: 'News' is a singular mass noun ending in '-s'. Solution: 'The news... **is** encouraging.'"},
                            {"title": "Item 2: Transform to Passive: 'The IT technician has resolved the network issue.'", "description": "Analysis: Present Perfect ('has resolved'). Passive: 'The network issue **has been resolved** by the IT technician.'"},
                            {"title": "Item 3: Agreement with Correlative Conjunction: 'Either the principal or the teachers (is/are) responsible for the schedule.'", "description": "Analysis: Closer subject 'teachers' is plural. Solution: 'Either the principal or the teachers **are** responsible...'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Subject-Verb Agreement Error Detection",
                    "content": {
                        "question": "Which of the following sentences contains a Subject-Verb Agreement ERROR?",
                        "options": [
                            "Mathematics is compulsory for all students pursuing engineering careers.",
                            "The box of delicate scientific instruments was delivered intact yesterday.",
                            "Neither the lead researcher nor the laboratory assistants was aware of the gas leak.",
                            "The committee has reached unanimous agreement regarding the allocation of school resources."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C contains the agreement error. In 'Neither...nor' constructions, the verb must agree in number with the closer subject. The closer subject is plural ('laboratory assistants'), so the verb must be plural ('were aware', not 'was aware'). All other sentences are grammatically sound."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Active to Passive Transformation",
                    "content": {
                        "question": "What is the correct passive voice transformation of the active sentence: 'The engineering firm will construct a state-of-the-art computer center next term'?",
                        "options": [
                            "A state-of-the-art computer center will be constructed by the engineering firm next term.",
                            "A state-of-the-art computer center will have constructed by the engineering firm next term.",
                            "A state-of-the-art computer center was constructed by the engineering firm next term.",
                            "A state-of-the-art computer center is being constructed by the engineering firm next term."
                        ],
                        "correct_answer": 0,
                        "explanation": "Option A is correct: The future modal 'will construct' transforms into 'will be constructed' in the passive voice, maintaining accurate future tense and aspect."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 3 Lesson 10 Summary & Topic Synthesis",
                    "content": {
                        "text": "### Topic 3 Synthesis & Key Takeaways\n- **Active Voice** emphasizes agency and vitality; **Passive Voice** highlights the recipient and action, ideal for formal/scientific writing.\n- **Subject-Verb Agreement** requires matching the true head noun, navigating tricky singulars (*economics, news*) and proximity rules.\n- Across Topic 3, you have mastered the complete grammatical system: from word classes (*Nouns, Pronouns, Verbs, Adjectives, Adverbs, Determiners*), to phrases (*NP, VP, AdjP, AdvP, PP*), clauses (*Relative, Adverbial, Noun*), and sentence-level mechanics (*Patterns, Boundary Fluency, Voice & Agreement*)."
                    }
                }
            ]
        ]
    }
]
