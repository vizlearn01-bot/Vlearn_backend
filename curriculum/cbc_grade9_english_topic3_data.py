"""
VLearn CBC Grade 9 English — Topic 3: Grammar in Use
Full Structured Lesson Card Definitions for Lessons 1 to 8 (Source Lessons 9 to 16)
"""

from curriculum.cbc_grade9_english_topic3_svgs import (
    SVG_GENDER_NEUTRAL_LANGUAGE,
    SVG_NOUN_FORMATION_QUANTIFIERS,
    SVG_PRONOUNS_RELATIVE_INTERROGATIVE,
    SVG_DOSASCOMP_ADJECTIVES_ADVERBS,
    SVG_PREPOSITIONS_CORRELATIVE_CONJUNCTIONS,
    SVG_MODAL_AUXILIARIES_SPECTRUM,
    SVG_PERFECT_ASPECTS_TIMELINE,
    SVG_REPORTED_SPEECH_ENGINE,
)

TOPIC_3_LESSONS = [
    # =========================================================================
    # LESSON 1 (Source Lesson 9): Gender-Neutral Language
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Gender-Neutral Language",
        "unit_description": "Promoting gender sensitivity, identifying biased terms, using neutral occupational titles, and mastering singular 'they' with proper verb agreement.",
        "lesson_title": "Gender-Neutral Language",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Inclusive Team Collaboration in Modern Workplace",
                    "content": {
                        "title": "Inclusive and Diverse Team Collaboration",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Diverse_group_of_people_in_a_meeting.jpg",
                        "caption": "A diverse group of professionals working collaboratively in a modern setting where gender-neutral communication fosters inclusion and respect.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify gender-biased words and phrases in oral and written texts\n- Replace biased titles with inclusive, neutral alternatives (e.g., *police officer*, *chairperson*)\n- Use singular 'they', 'them', and 'their' accurately with proper plural verb agreement\n- Appreciate the importance of gender-sensitive language in civic and digital communication"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The School Noticeboard Dilemma",
                    "content": {
                        "text": "Imagine reading a school notice that states:\n\n*\"Every teacher must submit his lesson plans by Friday. He must also ensure his classroom is tidy.\"*\n\nNotice the pronouns **he** and **his**. Do only male teachers work at your school? Of course not! By defaulting to male pronouns, the notice unintentionally makes female teachers invisible. Gender-neutral language ensures that everyone in our community feels respected, acknowledged, and valued."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Inclusive Communication",
                    "content": {
                        "term": "Gender-Neutral Language",
                        "definition": "Language that avoids bias toward a particular sex or gender identity, treating all individuals equally through inclusive terms, occupational titles, and pronouns."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Gender-Biased vs. Gender-Neutral Terminology",
                    "content": {
                        "headers": ["Gender-Biased Term", "Gender-Neutral Alternative", "Contextual Application"],
                        "rows": [
                            ["Policeman / Policewoman", "Police officer", "Law enforcement and public safety"],
                            ["Fireman", "Firefighter", "Emergency response services"],
                            ["Chairman / Chairwoman", "Chairperson / Chair", "Committee and board leadership"],
                            ["Steward / Stewardess", "Flight attendant", "Aviation and hospitality"],
                            ["Businessman / Businesswoman", "Business executive / Entrepreneur", "Commerce and industry"],
                            ["Mankind", "Humankind / Humanity", "General human species reference"],
                            ["Spokesman", "Spokesperson", "Public relations and media statements"],
                            ["Headmaster / Headmistress", "Principal / School head", "Educational institution leadership"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Gender-Neutral Language Transformation Matrix",
                    "content": {
                        "title": "Inclusive Transformation & Singular 'They' Protocol",
                        "caption": "Architectural guide showing biased term replacements and grammatical agreement rules when using singular 'they'.",
                        "svg_content": SVG_GENDER_NEUTRAL_LANGUAGE
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Sentence Parsing & Neutralization Model",
                    "content": {
                        "intro": "Examine how a biased administrative directive is systematically transformed into inclusive language:",
                        "steps": [
                            "**Original Sentence:** *\"If a candidate wants to run for head prefect, he must submit his application to the headmaster, and he is expected to demonstrate leadership.\"*",
                            "**Step 1 (Isolate Biased Elements):** Pronouns: *he*, *his*, *he*; Titles: *headmaster*.",
                            "**Step 2 (Apply Neutral Replacements):** Replace *headmaster* with *principal*; Replace *he/his* with singular *they/their*.",
                            "**Step 3 (Adjust Verb Agreement):** Change *\"he is expected\"* to *\"they are expected\"* (Singular 'they' grammatically takes a plural verb).",
                            "**Neutralized Sentence:** *\"If a candidate wants to run for head prefect, **they** must submit **their** application to the **principal**, and **they are** expected to demonstrate leadership.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Using Gender-Neutral Language in Writing",
                    "content": {
                        "title": "Gender-Neutral and Inclusive Language in Practice",
                        "youtube_id": "Xm4h4V0f-dI",
                        "url": "https://www.youtube.com/watch?v=Xm4h4V0f-dI",
                        "description": "An instructive guide on eliminating gender bias in academic, civic, and professional writing using neutral titles and singular 'they'."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Active Workbench: Drafting a School Constitution",
                    "content": {
                        "title": "Inclusive Drafting in Student Governance",
                        "text": "**Drafting Challenge:** Review the following clause from a club constitution:\n\n*\"The Chairman shall preside over all meetings. He shall cast his vote only in the event of a tie.\"*\n\n**Workbench Revision:** *\"The **Chairperson** shall preside over all meetings. **They** shall cast **their** vote only in the event of a tie.\"*\n\n**Civic Impact:** Clear, inclusive wording ensures all students feel equally eligible to aspire to leadership roles regardless of gender."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Singular 'They' Subject-Verb Agreement Pitfall",
                    "content": {
                        "incorrect": "Each doctor must check their patient because they is responsible for the diagnosis.",
                        "corrected": "Each doctor must check their patient because they are responsible for the diagnosis.",
                        "explanation": "Although singular 'they' refers to a single individual, it grammatically requires a plural verb ('they are', 'they have', 'they do'), exactly like singular 'you' takes 'you are'."
                    }
                },
                {
                    "type": "step_process",
                    "title": "3-Step Protocol for Eliminating Gender Bias",
                    "content": {
                        "title": "Text Inclusivity Protocol",
                        "steps": [
                            "**Audit:** Scan text for gendered occupational suffixes (-man, -woman, -ess) and default masculine pronouns (he, him, his).",
                            "**Select Strategy:** Either replace with gender-neutral alternatives (*firefighter*, *chair*) or recast the sentence using plural nouns (*All students must bring their books*).",
                            "**Verify Agreement:** Ensure pronouns agree syntactically with their verbs (e.g., *they have*, not *they has*)."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Neutral Occupational Titles & Agreement",
                    "content": {
                        "question": "Which of the following sentences is completely gender-neutral and grammatically correct?",
                        "options": [
                            "The policeman told the housewife to drive her car carefully.",
                            "The police officer told the driver to manage their speed carefully.",
                            "The police officer told the driver he must manage his speed carefully.",
                            "Each firefighter must check their uniform before they goes to work."
                        ],
                        "correct_answer": "The police officer told the driver to manage their speed carefully.",
                        "explanation": "Option B correctly uses the gender-neutral occupational title 'police officer' and the neutral singular possessive pronoun 'their'. Option A uses gender-biased titles ('policeman', 'housewife'); Option C reverts to masculine default pronouns ('he', 'his'); Option D incorrectly uses 'they goes' instead of 'they go'."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Singular 'They' Verb Concord",
                    "content": {
                        "question": "Select the sentence that demonstrates proper verb concord with singular 'they':",
                        "options": [
                            "If a customer calls, tell them that they is going to receive a callback.",
                            "When an applicant arrives, ensure they has their identification document.",
                            "A student forgot their jacket in the laboratory; they are asked to collect it.",
                            "Somebody left his bag in the bus because he was rushing."
                        ],
                        "correct_answer": "A student forgot their jacket in the laboratory; they are asked to collect it.",
                        "explanation": "Option C correctly uses singular 'they' referring to 'a student' and pairs it with the correct plural verb 'are'. Options A and B incorrectly pair 'they' with singular verbs ('is', 'has'). Option D uses exclusive masculine pronouns ('his', 'he') instead of neutral forms."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Gender-Neutral Language",
                    "content": {
                        "text": "Gender-neutral language fosters an equitable society by removing exclusionary assumptions from everyday communication. By replacing gender-specific titles with functional terms (e.g., *firefighter*, *chairperson*) and using singular 'they' with plural verb concord, we create communication that honors every individual."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2 (Source Lesson 10): Nouns (Formation) and Quantifiers
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Nouns (Formation) and Quantifiers",
        "unit_description": "Mastering noun derivation using suffixes (-ment, -tion, -ness) and accurately matching quantifiers with countable and uncountable nouns in scientific and everyday contexts.",
        "lesson_title": "Nouns (Formation) and Quantifiers",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Laboratory Equipment and Measured Quantities",
                    "content": {
                        "title": "Scientific Investigation and Quantitative Measurement",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Science_Laboratory_Equipment.jpg",
                        "caption": "A modern science laboratory where scientists measure countable tools (beakers, pipettes) and uncountable substances (water, chemical solutions) with exact precision.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Form abstract and concrete nouns from verbs and adjectives using suffixes (-ment, -tion, -ness)\n- Categorize nouns accurately into countable (count) and uncountable (non-count) types\n- Select and pair appropriate quantifiers (*few*, *little*, *many*, *much*, *plenty of*) with count and non-count nouns\n- Correct common quantifier and pluralization errors in academic writing"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Sci-Fi Storytelling Challenge",
                    "content": {
                        "text": "Imagine writing a science fiction story about planetary exploration. If you write:\n\n*\"The astronaut discovered that Mars had many water and little rocks.\"*\n\nYour reader will instantly spot the grammatical mismatch! *Water* cannot be counted individually, so it cannot take *many*; *rocks* are countable items, so they cannot take *little*. Correct quantifier pairing and precise noun formation give your writing clarity and authority."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Derivation & Quantification",
                    "content": {
                        "term": "Derivational Suffix & Quantifier",
                        "definition": "A derivational suffix is an affix added to the end of a root word to change its grammatical category (e.g., verb *invent* + *-tion* = noun *invention*). A quantifier is a determiner placed before a noun to express quantity or amount."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Quantifier Compatibility Matrix",
                    "content": {
                        "headers": ["Quantifier Type", "Applicable Nouns", "Quantifiers", "Example Sentences"],
                        "rows": [
                            ["Countable Only", "Count nouns (have singular & plural forms)", "A few, Few, Several, Many, A number of", "\"We spotted **several** new **stars** in the cluster.\""],
                            ["Uncountable Only", "Non-count nouns (mass, abstract, no plural)", "A little, Little, Much, A bit of, A great deal of", "\"The rover requires **much** electrical **energy**.\""],
                            ["Dual (Both Count & Non-count)", "Can precede both countable and non-count nouns", "Some, Any, A lot of, Lots of, Plenty of", "\"They brought **plenty of** **tools** (count) and **water** (uncount).\""]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Noun Formation & Quantifier Architecture",
                    "content": {
                        "title": "Derivational Suffixes & Quantifier Distribution System",
                        "caption": "Diagram showing how root verbs/adjectives transform into nouns via -ment, -tion, -ness, and the three-tiered quantifier compatibility system.",
                        "svg_content": SVG_NOUN_FORMATION_QUANTIFIERS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Noun Derivation & Quantifier Selection Model",
                    "content": {
                        "intro": "Demonstrating step-by-step noun derivation and quantifier pairing in technical writing:",
                        "steps": [
                            "**Target Prompt:** Convert the verb *develop* into a noun and quantify it with a word denoting an abundant amount.",
                            "**Step 1 (Suffix Addition):** *develop* (verb) + *-ment* (suffix) = **development** (noun).",
                            "**Step 2 (Determine Countability):** In this general context, *development* functions as an uncountable abstract noun.",
                            "**Step 3 (Select Quantifier):** Choose an uncountable or dual quantifier (*much*, *a lot of*, *plenty of*). Avoid countable quantifiers (*many*, *several*).",
                            "**Completed Sentence:** *\"The research team witnessed **a lot of development** in solar energy efficiency.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Countable vs. Uncountable Nouns and Quantifiers",
                    "content": {
                        "title": "Mastering Quantifiers: Few vs. Little, Many vs. Much",
                        "youtube_id": "bI6N-2xGgXk",
                        "url": "https://www.youtube.com/watch?v=bI6N-2xGgXk",
                        "description": "Visual breakdown of count vs. non-count nouns, suffix rules for noun formation, and accurate quantifier usage in English."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Grammar Workbench: Science Lab Inventory",
                    "content": {
                        "title": "Technical Reporting in a Research Station",
                        "text": "**Raw Lab Notes:** *\"We received 10 informings about the experiments. The generator has few fuel left, but we have much test tubes.\"*\n\n**Workbench Editing:**\n1. *Informings* ➔ Incorrect suffix and pluralization of non-count noun. Correct: **information**.\n2. *Few fuel* ➔ Mismatch (*fuel* is uncountable). Correct: **little fuel**.\n3. *Much test tubes* ➔ Mismatch (*test tubes* is countable). Correct: **many test tubes**.\n\n**Polished Technical Report:** *\"We received **information** about the experiments. The generator has **little fuel** left, but we have **many test tubes**.\"*"
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Pluralizing Non-Count Nouns and Quantifier Mismatch",
                    "content": {
                        "incorrect": "The scientist shared many informations and asked for few equipments.",
                        "corrected": "The scientist shared much information and asked for a few pieces of equipment.",
                        "explanation": "Uncountable nouns such as 'information', 'equipment', 'advice', and 'furniture' cannot take plural '-s' endings or countable quantifiers ('many'). Use 'much', 'a lot of', or partitive phrases ('pieces of equipment')."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Decision Tree for Quantifier Selection",
                    "content": {
                        "title": "Quantifier Pairing Protocol",
                        "steps": [
                            "**Test for Countability:** Ask: Can you count this item individually with numbers (1, 2, 3)? If yes ➔ Countable; If no ➔ Uncountable.",
                            "**Identify Quantity Degree:** Determine if the intended meaning is small (*few/little*), large (*many/much/a lot of*), or unspecified (*some/any*).",
                            "**Select Matching Quantifier:** For small count quantities, use *a few*; for small non-count amounts, use *a little*."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Noun Derivation and Quantifier Fit",
                    "content": {
                        "question": "Complete the following sentence with the correct noun form and quantifier:\n\n*\"The aerospace team made __________ in the __________ of the new propulsion engine.\"*",
                        "options": [
                            "many progress / developation",
                            "much progress / development",
                            "a few progresses / developness",
                            "several progress / developing"
                        ],
                        "correct_answer": "much progress / development",
                        "explanation": "Option B is correct because 'progress' is an uncountable noun and pairs with 'much', while 'development' is the correct noun formed from the verb 'develop' using the suffix '-ment'. 'Progress' cannot be pluralized ('progresses') nor paired with countable quantifiers ('many', 'several')."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Countable vs. Non-Count Quantifier Application",
                    "content": {
                        "question": "Which sentence correctly pairs quantifiers with their respective nouns?",
                        "options": [
                            "We have a little solar panels on the roof and much storage batteries.",
                            "We have a few solar panels on the roof and plenty of storage capacity.",
                            "We have several solar panel on the roof and a few energy available.",
                            "We have much solar panels on the roof and a little batteries."
                        ],
                        "correct_answer": "We have a few solar panels on the roof and plenty of storage capacity.",
                        "explanation": "Option B correctly pairs the countable noun 'solar panels' with 'a few' and the uncountable noun 'storage capacity' with the dual quantifier 'plenty of'. Option A incorrectly pairs 'a little' with 'solar panels' and 'much' with 'batteries'."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Nouns and Quantifiers",
                    "content": {
                        "text": "Derivational suffixes like *-ment*, *-tion*, and *-ness* systematically convert verbs and adjectives into nouns. Understanding the distinction between countable and uncountable nouns ensures you always pair them with their proper quantifiers (*few/many* for count; *little/much* for non-count; *some/plenty of* for dual use)."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3 (Source Lesson 11): Relative and Interrogative Pronouns
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Relative and Interrogative Pronouns",
        "unit_description": "Connecting clauses seamlessly using relative pronouns (who, whom, whose, which, that) and formulating structured research inquiries using interrogative pronouns in environmental contexts.",
        "lesson_title": "Relative and Interrogative Pronouns",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Marine Biologists Studying Coral Reef Ecosystems",
                    "content": {
                        "title": "Marine Conservation and Oceanic Research",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/Coral_Outcrop_Flynn_Reef.jpg",
                        "caption": "Marine researchers exploring a vibrant coral reef ecosystem, asking investigative questions and documenting species that require urgent protection.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish clearly between the syntactic roles of relative and interrogative pronouns\n- Combine separate simple clauses into complex sentences using *who*, *whom*, *whose*, *which*, and *that*\n- Formulate targeted interrogative questions (*Who*, *Which*, *What*, *Whose*) to conduct research on natural conservation\n- Eliminate redundancy and pronoun ambiguity in written essays"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Marine Research Reporter",
                    "content": {
                        "text": "Imagine writing a scientific article on marine life with choppy, separate sentences:\n\n*\"We observed a dolphin. The dolphin was swimming in the Indian Ocean. The dolphin was guiding its calf.\"*\n\nRepeating *the dolphin* makes the prose tedious. Instead, relative pronouns act as **connector bridges**:\n\n*\"We observed a dolphin **which** was swimming in the Indian Ocean and guiding its calf.\"*\n\nTo investigate further, we use interrogative pronouns: *\"**What** is threatening this dolphin's feeding grounds?\"*"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Clause Linking & Inquiries",
                    "content": {
                        "term": "Relative vs. Interrogative Pronoun",
                        "definition": "A relative pronoun connects a subordinate clause to a preceding noun (antecedent) to provide essential or additional detail. An interrogative pronoun stands at the beginning of a sentence to introduce a direct question asking for specific information."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Pronoun Reference and Functional Guide",
                    "content": {
                        "headers": ["Pronoun", "Referent / Category", "Relative Clause Role", "Interrogative Question Role"],
                        "rows": [
                            ["Who", "Persons (Subject)", "Refers to the person doing the action (\"The ranger **who** rescued the turtle...\")", "Asks about the subject person (\"**Who** discovered the nesting site?\")"],
                            ["Whom", "Persons (Object)", "Refers to the person receiving the action (\"The diver **whom** we interviewed...\")", "Asks about the object person (\"**Whom** did the warden contact?\")"],
                            ["Whose", "Possession (People/Animals)", "Shows ownership/belonging (\"Fishers **whose** boats were upgraded...\")", "Asks about possession (\"**Whose** diving gear is this?\")"],
                            ["Which", "Animals & Inanimate Objects / Choices", "Refers to non-human entities (\"The reef **which** was damaged...\")", "Asks for a choice from a specific set (\"**Which** of the two bays is cleaner?\")"],
                            ["That", "Persons, Animals, or Objects", "Introduces essential restrictive clauses (\"The law **that** bans trawling...\")", "Not used as an interrogative pronoun"],
                            ["What", "General Entities / Ideas", "Not typically used as a standard relative pronoun", "Asks for general information (\"**What** causes coral bleaching?\")"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Pronoun Function & Clause Architecture",
                    "content": {
                        "title": "Relative Clause Bridge vs. Interrogative Inquiry Engine",
                        "caption": "Structural blueprint illustrating how relative pronouns embed descriptive clauses into main clauses and how interrogative pronouns form precise questions.",
                        "svg_content": SVG_PRONOUNS_RELATIVE_INTERROGATIVE
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Clause Combination & Relative Embedding Model",
                    "content": {
                        "intro": "Watch how two disjointed statements about marine ecology are synthesized using relative pronouns:",
                        "steps": [
                            "**Statement A:** *\"The conservationist delivered an inspiring keynote on mangroves.\"*",
                            "**Statement B:** *\"The conservationist was awarded the National Ocean Prize.\"*",
                            "**Step 1 (Identify Common Noun / Antecedent):** *The conservationist* (refers to a human).",
                            "**Step 2 (Determine Grammatical Case):** In Statement B, *The conservationist* is the subject performing the action.",
                            "**Step 3 (Select Relative Pronoun):** Human subject ➔ **who**.",
                            "**Step 4 (Synthesize Clauses):** *\"The conservationist **who** was awarded the National Ocean Prize delivered an inspiring keynote on mangroves.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Relative Pronouns: Who, Whom, Whose, Which, That",
                    "content": {
                        "title": "Connecting Sentences with Relative Pronouns",
                        "youtube_id": "a-v40sJ2h40",
                        "url": "https://www.youtube.com/watch?v=a-v40sJ2h40",
                        "description": "Comprehensive explanation of restrictive and non-restrictive relative clauses, choosing between who vs. which, and using interrogative pronouns."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Editing Lab: Marine Research Journal Article",
                    "content": {
                        "title": "Refining Environmental Field Reports",
                        "text": "**Draft Sentence:** *\"We encountered a sea turtle who had swallowed plastic waste. What species did it belong to? We spoke to the officer which was on patrol.\"*\n\n**Grammar Analysis & Correction:**\n1. *Turtle who* ➔ Animals take *which* or *that*. Correction: *turtle **which** had swallowed plastic*.\n2. *Officer which* ➔ Humans require *who* or *whom*. Correction: *officer **who** was on patrol*.\n\n**Polished Field Report:** *\"We encountered a sea turtle **which** had swallowed plastic waste. **What** species did it belong to? We spoke to the officer **who** was on patrol.\"*"
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Confusing 'Who' with 'Which' and 'Whom' with 'Who'",
                    "content": {
                        "incorrect": "The marine biologist which discovered the reef spoke to the divers who we had trained.",
                        "corrected": "The marine biologist who discovered the reef spoke to the divers whom we had trained.",
                        "explanation": "Use 'who' for humans acting as subjects ('the biologist who discovered'). Use 'which' for non-humans. Use 'whom' when the human pronoun is the object of the verb ('the divers whom we had trained' = we had trained them)."
                    }
                },
                {
                    "type": "step_process",
                    "title": "3-Step Clause Coupling Method",
                    "content": {
                        "title": "Relative Sentence Integration Protocol",
                        "steps": [
                            "**Identify Antecedent:** Locate the repeated person, animal, or thing in both sentences.",
                            "**Select Pronoun:** Choose *who/whom* for persons, *which/that* for things/animals, and *whose* for possession.",
                            "**Embed Subordinate Clause:** Position the relative clause immediately after the antecedent to prevent misplaced modifiers."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Relative Pronoun Precision",
                    "content": {
                        "question": "Read the following dialogue and select the option that correctly inserts an **interrogative pronoun** followed by a **relative pronoun**:\n\n*Ecologist:* \"__________ of these two marine sanctuaries has a higher turtle population?\"\n*Ranger:* \"The sanctuary __________ protects the inner barrier reef.\"",
                        "options": [
                            "Who / who",
                            "Which / that",
                            "What / whose",
                            "Which / whom"
                        ],
                        "correct_answer": "Which / that",
                        "explanation": "Option B is correct. 'Which' is the appropriate interrogative pronoun when choosing from a specific, defined set of options (two sanctuaries). 'That' (or 'which') is the correct relative pronoun referring back to an inanimate place ('the sanctuary'). 'Who' and 'whom' are strictly reserved for humans."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Relative Clause Synthesis",
                    "content": {
                        "question": "Which of the following sentences correctly combines the two clauses: *'The artisanal fishers received new boats.'* and *'Their livelihoods were threatened by industrial trawling.'*?",
                        "options": [
                            "The artisanal fishers which livelihoods were threatened received new boats.",
                            "The artisanal fishers whom livelihoods were threatened received new boats.",
                            "The artisanal fishers whose livelihoods were threatened received new boats.",
                            "The artisanal fishers who livelihoods were threatened received new boats."
                        ],
                        "correct_answer": "The artisanal fishers whose livelihoods were threatened received new boats.",
                        "explanation": "Option C correctly uses the possessive relative pronoun 'whose' to refer to 'their livelihoods' belonging to the fishers. 'Which' is for things, 'whom' is for object pronouns, and 'who' is for subject pronouns."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Pronoun Fluency",
                    "content": {
                        "text": "Relative pronouns (*who, whom, whose, which, that*) turn disjointed sentences into unified, sophisticated prose by embedding descriptive clauses. Interrogative pronouns (*who, which, what, whose*) allow researchers and communicators to formulate precise, targeted inquiries about the world around them."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4 (Source Lesson 12): The Order of Adjectives and Comparison of Adverbs
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "The Order of Adjectives and Comparison of Adverbs",
        "unit_description": "Mastering the DOSASCOMP mnemonic for multiple adjective strings and applying positive, comparative, and superlative degrees of regular and irregular adverbs in tourism and descriptive contexts.",
        "lesson_title": "The Order of Adjectives and Comparison of Adverbs",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Tourist Safari Vehicle Exploring Maasai Mara",
                    "content": {
                        "title": "International Tourism and Landscape Exploration",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Game_drive_in_Masai_Mara.jpg",
                        "caption": "International tourists traveling in an open-roof safari vehicle across the savannah, admiring magnificent Kenyan wildlife and historic cultural artifacts.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Sequence multiple adjectives accurately before a noun using the standard DOSASCOMP rule\n- Form positive, comparative, and superlative degrees of regular and irregular adverbs\n- Distinguish between adjective and adverb functions in descriptive paragraphs\n- Diagnose and correct awkward modifier sequences in travel writing and storytelling"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Antique Table Description",
                    "content": {
                        "text": "Imagine describing a souvenir desk to an international tourist visiting Kenya:\n\n*\"I bought a wooden large old rectangular beautiful Kenyan writing table.\"*\n\nEven though all the describing words are correct individually, the sentence sounds completely unnatural! In English, native speakers unconsciously follow a strict, logical hierarchy when stacking adjectives. Learning **DOSASCOMP** unlocks the secret behind natural, elegant descriptive writing."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Modifiers in Sequence",
                    "content": {
                        "term": "DOSASCOMP & Adverb Degrees",
                        "definition": "DOSASCOMP is the foundational mnemonic governing English adjective order: Determiner, Opinion, Size, Age, Shape, Color, Origin, Material, Purpose. Adverbs modify verbs, adjectives, or other adverbs across three degrees: Positive (base), Comparative (comparing 2), and Superlative (comparing 3+)."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "DOSASCOMP Adjective Sequence & Adverb Degrees",
                    "content": {
                        "headers": ["Order / Degree", "Category / Form", "Description & Rules", "Example Words / Modifiers"],
                        "rows": [
                            ["1. D", "Determiner", "Articles, possessives, demonstratives, numbers", "A, the, three, several, my, those"],
                            ["2. O", "Opinion", "Subjective judgments, quality assessments", "Beautiful, elegant, magnificent, hideous, rare"],
                            ["3. S", "Size", "Physical dimensions, height, weight", "Huge, small, tiny, massive, gigantic"],
                            ["4. A", "Age", "Era, chronological age, freshness", "Ancient, antique, new, modern, teenage"],
                            ["5. S", "Shape", "Geometric configuration, contour", "Rectangular, round, oval, triangular, spherical"],
                            ["6. C", "Color", "Hue, shade, pigmentation", "Brown, golden, crimson, turquoise, emerald"],
                            ["7. O", "Origin", "Source, nationality, geographic origin", "Kenyan, African, French, Italian, Chinese"],
                            ["8. M", "Material", "Substance of composition", "Wooden, mahogany, silk, leather, metallic"],
                            ["9. P", "Purpose", "Function / intended use (often gerund)", "Writing (desk), sports (car), dining (table)"],
                            ["Adverb (Reg)", "Regular (-ly)", "Base / +more / +most", "Clearly / More clearly / Most clearly"],
                            ["Adverb (Irreg)", "Irregular", "Unique comparative & superlative stems", "Well ➔ Better ➔ Best | Badly ➔ Worse ➔ Worst"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "DOSASCOMP & Adverb Comparison Matrix",
                    "content": {
                        "title": "9-Stage Adjective Sequencing & Adverb Progression Architecture",
                        "caption": "Complete visual map of the DOSASCOMP hierarchy paired with regular and irregular comparative/superlative adverb progression.",
                        "svg_content": SVG_DOSASCOMP_ADJECTIVES_ADVERBS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Synthesizing a Complex Descriptive Noun Phrase",
                    "content": {
                        "intro": "Let us organize six scrambled adjectives modifying the noun *buses* for a tourism brochure:",
                        "steps": [
                            "**Scrambled Modifiers:** *[safari, new, three, Japanese, large, white]* + buses.",
                            "**Step 1 (Determiner - D):** *three*",
                            "**Step 2 (Opinion - O):** None provided.",
                            "**Step 3 (Size - S):** *large*",
                            "**Step 4 (Age - A):** *new*",
                            "**Step 5 (Shape - S):** None provided.",
                            "**Step 6 (Color - C):** *white*",
                            "**Step 7 (Origin - O):** *Japanese*",
                            "**Step 8 (Material - M):** None provided.",
                            "**Step 9 (Purpose - P):** *safari*",
                            "**Final Synthesized Phrase:** *\"**Three large new white Japanese safari** buses.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Order of Adjectives in English",
                    "content": {
                        "title": "Mastering the Order of Adjectives (DOSASCOMP)",
                        "youtube_id": "XFjM6nF4joc",
                        "url": "https://www.youtube.com/watch?v=XFjM6nF4joc",
                        "description": "Clear and engaging tutorial explaining how to order multiple adjectives naturally before nouns and avoid common sequencing errors."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Creative Lab: Travel Brochure Copywriting",
                    "content": {
                        "title": "Writing Vivid Tourism Descriptions",
                        "text": "**Drafting Challenge:** Enhance the following hotel advertisement using precise adjective sequences and comparative adverbs:\n\n*\"Guests will rest in a (wooden, cozy, old, Swiss) chalet and travel (more fast) across the reserve.\"*\n\n**Polished Copy:**\n*\"Guests will rest in a **cozy (O) old (A) Swiss (O) wooden (M)** chalet and travel **faster** across the reserve to view the wildlife.\"*\n\n**Impact:** Structuring modifiers correctly makes promotional descriptions immediately engaging and credible."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Double Comparatives and Inverted Adjective Order",
                    "content": {
                        "incorrect": "The tour guide explained the park rules more clearer than the driver in a leather red Kenyan jacket.",
                        "corrected": "The tour guide explained the park rules more clearly than the driver in a red Kenyan leather jacket.",
                        "explanation": "Adverbs ending in '-ly' take 'more clearly', never 'more clearer'. In adjective ordering, color ('red') and origin ('Kenyan') must precede material ('leather') (DOSASCOMP: C-O-M)."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Modifier Sequencing Verification Checklist",
                    "content": {
                        "title": "DOSASCOMP Audit Procedure",
                        "steps": [
                            "**Tag Every Modifier:** Label each adjective with its DOSASCOMP category code (D, O, S, A, S, C, O, M, P).",
                            "**Sort Numerically:** Arrange the tags in strict sequential ascending order from 1 to 9.",
                            "**Check Adverb Degrees:** Verify regular adverbs take *more/most* and irregular adverbs (*well ➔ better ➔ best*) follow their specific stems."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Adjective Order in Tourism Context",
                    "content": {
                        "question": "A luxury safari company is drafting a promotional feature. Which of the following sentences adheres strictly to the DOSASCOMP adjective order and uses the correct comparative adverb?",
                        "options": [
                            "Our tourists will travel more comfortablier in three large new red Japanese buses.",
                            "Our tourists will travel most comfortably in three new large red Japanese buses.",
                            "Our tourists will travel more comfortably in three large new red Japanese safari buses.",
                            "Our tourists will travel the best in Japanese red large three new sports buses."
                        ],
                        "correct_answer": "Our tourists will travel more comfortably in three large new red Japanese safari buses.",
                        "explanation": "Option C is correct because it follows the strict DOSASCOMP sequence: three (Determiner), large (Size), new (Age), red (Color), Japanese (Origin), safari (Purpose) buses, and uses the correct comparative adverb 'more comfortably'. Option A uses the non-word 'more comfortablier'; Option B puts Age before Size; Option D completely scrambles the hierarchy."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Irregular Adverb Comparison",
                    "content": {
                        "question": "Select the sentence that correctly utilizes an irregular adverb in the comparative degree:",
                        "options": [
                            "Sibling Sarah performed badlier than expected during the trial tour.",
                            "Sibling Sarah performed more badly than expected during the trial tour.",
                            "Sibling Sarah performed worse than expected during the trial tour.",
                            "Sibling Sarah performed worst than expected during the trial tour."
                        ],
                        "correct_answer": "Sibling Sarah performed worse than expected during the trial tour.",
                        "explanation": "Option C is correct because 'badly' is an irregular adverb whose comparative form is 'worse' (not 'badlier' or 'more badly'). 'Worst' is the superlative form and requires comparing three or more entities."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Ordering Modifiers with Elegance",
                    "content": {
                        "text": "Natural descriptive English relies on the **DOSASCOMP** hierarchy (Determiner, Opinion, Size, Age, Shape, Color, Origin, Material, Purpose). Combining structured adjective strings with accurate adverb degrees (*-er/-est* or *more/most*) ensures your narratives and descriptions are fluid, precise, and vivid."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5 (Source Lesson 13): Complex Prepositions and Correlative Conjunctions
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Complex Prepositions and Correlative Conjunctions",
        "unit_description": "Using multi-word prepositions (according to, in spite of, on account of, by means of) and mastering parallel structures with correlative conjunction pairs (either...or, neither...nor, both...and, not only...but also).",
        "lesson_title": "Complex Prepositions and Correlative Conjunctions",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Solar Panels and Wind Turbines in Clean Energy Project",
                    "content": {
                        "title": "Renewable Energy and Environmental Conservation",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Solar_panels_and_wind_turbines.jpg",
                        "caption": "A hybrid clean energy farm utilizing both solar panels and wind turbines, illustrating interconnected systems working together for environmental preservation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and define multi-word complex prepositions (*in spite of*, *on account of*, *by means of*, *with regard to*)\n- Construct balanced, parallel sentences using correlative conjunction pairs (*either...or*, *neither...nor*, *both...and*, *not only...but also*)\n- Correct unbalanced conjunction structures and mismatched prepositional phrases\n- Formulate persuasive environmental arguments using cohesive grammatical connectors"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Connecting Environmental Initiatives",
                    "content": {
                        "text": "Imagine communicating about a community conservation project:\n\n*\"We planted trees. Heavy rain fell. We also cleaned the river.\"*\n\nThese short statements sound disjointed. Notice how complex prepositions and correlative conjunctions weave ideas into a cohesive whole:\n\n*\"**In spite of** the torrential rain, our club **not only** planted indigenous trees **but also** cleaned the river stream.\"*\n\nThese advanced connectors express nuanced relationships like cause, concession, and mutual emphasis."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Complex Connectors & Paired Conjunctions",
                    "content": {
                        "term": "Complex Preposition & Correlative Conjunction",
                        "definition": "A complex preposition is a multi-word phrase functioning as a single preposition before a noun phrase (e.g., *according to*, *on account of*). Correlative conjunctions are matched word pairs that join grammatically equal, parallel sentence elements."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Connector Functions, Meanings, and Pairings",
                    "content": {
                        "headers": ["Connector Category", "Phrase / Pair", "Linguistic Meaning / Function", "Conservation Context Example"],
                        "rows": [
                            ["Complex Preposition", "According to", "As stated or reported by an authority", "\"**According to** the climatologist, rainfall will increase.\""],
                            ["Complex Preposition", "In spite of", "Concession / Regardless of opposing factors", "\"We installed solar panels **in spite of** budget cuts.\""],
                            ["Complex Preposition", "On account of", "Causal relationship / Because of", "\"The tree planting was rescheduled **on account of** floods.\""],
                            ["Complex Preposition", "By means of", "Instrumentality / Using the agency of", "\"They irrigate seedlings **by means of** drip piping.\""],
                            ["Complex Preposition", "With regard to", "Concerning / In connection with", "\"New bylaws were enacted **with regard to** wetland use.\""],
                            ["Correlative Pair", "Either ... or", "Presents an alternative choice of two options", "\"We must **either** reduce emissions **or** risk degradation.\""],
                            ["Correlative Pair", "Neither ... nor", "Excludes both options simultaneously", "\"**Neither** illegal logging **nor** poaching will be tolerated.\""],
                            ["Correlative Pair", "Both ... and", "Emphasizes mutual inclusion of two items", "\"**Both** community elders **and** students joined the cleanup.\""],
                            ["Correlative Pair", "Not only ... but also", "Emphasizes dual, additive occurrences", "\"**Not only** did we mulch the soil **but also** built terraces.\""]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Complex Prepositions & Correlative Conjunctions Matrix",
                    "content": {
                        "title": "Multi-Word Preposition Architecture & Parallel Conjunction Balancer",
                        "caption": "Diagram detailing complex preposition definitions and the structural parallelism rule governing correlative conjunction pairs.",
                        "svg_content": SVG_PREPOSITIONS_CORRELATIVE_CONJUNCTIONS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Synthesizing Sentences with Parallel Conjunctions",
                    "content": {
                        "intro": "Observe how two separate ideas are combined into a balanced, parallel correlative structure:",
                        "steps": [
                            "**Original Sentences:** *\"The school environment club planted 500 seedlings.\"* + *\"The club installed a rain harvesting tank.\"*",
                            "**Target Structure:** Use the correlative pair **not only ... but also**.",
                            "**Step 1 (Audit for Parallel Verbs):** Verb 1: *planted*; Verb 2: *installed* (both past simple transitive verbs).",
                            "**Step 2 (Position the Pair):** Place *not only* before Verb 1 and *but also* before Verb 2.",
                            "**Step 3 (Synthesize):** *\"The school environment club **not only planted** 500 seedlings **but also installed** a rain harvesting tank.\"*",
                            "**Parallelism Verification:** [Verb + Object] matches [Verb + Object]."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Correlative Conjunctions and Parallel Structure",
                    "content": {
                        "title": "Mastering Correlative Conjunctions: Either/Or, Neither/Nor, Not Only/But Also",
                        "youtube_id": "r-lF_yY76cE",
                        "url": "https://www.youtube.com/watch?v=r-lF_yY76cE",
                        "description": "Instructional video on keeping grammatical elements balanced and parallel when using correlative conjunction pairs."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Debate Lab: Crafting Environmental Policy Motions",
                    "content": {
                        "title": "Using Advanced Connectors in Formal Debate",
                        "text": "**Motion:** *\"This House would ban single-use plastics across all educational institutions.\"*\n\n**Debater's Script:**\n*\"Mr. Speaker, **according to** recent environmental audits, single-use plastics choke our drainage systems. **On account of** this crisis, we propose that schools **either** transition immediately to biodegradable bags **or** face statutory penalties. **In spite of** initial transition costs, **both** our students **and** local wildlife will benefit tremendously.\"*\n\n**Rhetorical Power:** The complex connectors establish logic, authority, and persuasive clarity."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Faulty Parallelism and Mismatched Conjunction Pairs",
                    "content": {
                        "incorrect": "Neither the forest guard or the local chief was able to stop logging on account that laws were weak.",
                        "corrected": "Neither the forest guard nor the local chief was able to stop logging on account of weak laws.",
                        "explanation": "'Neither' must always be paired with 'nor' (never 'or'). Furthermore, 'on account of' is a complex preposition that must be followed by a noun phrase ('weak laws'), not a clause with 'that'."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Correlative Parallelism Audit Protocol",
                    "content": {
                        "title": "Sentence Balance Checklist",
                        "steps": [
                            "**Check the Pair:** Ensure *either* matches *or*, *neither* matches *nor*, *both* matches *and*, and *not only* matches *but also*.",
                            "**Check Part of Speech:** What immediately follows the first conjunction must match what follows the second (e.g., [Noun] + [Noun] or [Verb] + [Verb]).",
                            "**Preposition Check:** Verify that multi-word prepositions take noun phrases or gerunds, not full clauses."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Balanced Conjunction Pairs",
                    "content": {
                        "question": "Which of the following sentences correctly utilizes a **complex preposition** and a balanced **correlative conjunction** pair?",
                        "options": [
                            "According to the ranger, neither we must waste water or pollute our soil.",
                            "On account of the prolonged dry season, both the reservoir and the local stream have dried up.",
                            "In spite of the rain, not only did we plant seedlings but also clean the drainage.",
                            "By means of teamwork, either we will save our forests nor we will suffer from severe drought."
                        ],
                        "correct_answer": "On account of the prolonged dry season, both the reservoir and the local stream have dried up.",
                        "explanation": "Option B correctly uses the complex preposition 'on account of' followed by a noun phrase, and the balanced correlative pair 'both...and' joining two parallel noun phrases ('the reservoir' and 'the local stream'). Option A incorrectly pairs 'neither' with 'or'; Option C has faulty parallelism in verb tenses; Option D incorrectly pairs 'either' with 'nor'."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Faulty Parallelism Detection",
                    "content": {
                        "question": "Identify the sentence that maintains strict grammatical parallelism across its correlative conjunctions:",
                        "options": [
                            "The green energy project will not only generate electricity but also creating jobs.",
                            "The green energy project will not only generate electricity but also create jobs.",
                            "The green energy project will not only electricity generation but also create jobs.",
                            "The green energy project will generate not only electricity but also creates jobs."
                        ],
                        "correct_answer": "The green energy project will not only generate electricity but also create jobs.",
                        "explanation": "Option B maintains strict parallelism because 'not only' is followed by base verb + noun ('generate electricity') and 'but also' is followed by base verb + noun ('create jobs'). All other options mix verb forms or parts of speech across the conjunction pair."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Cohesive Structural Connectors",
                    "content": {
                        "text": "Complex prepositions (*according to, in spite of, on account of, by means of*) express intricate relationships between actions and ideas. Paired correlative conjunctions (*both...and, neither...nor, either...or, not only...but also*) create balanced, parallel sentences that elevate the maturity and rhetorical impact of your writing."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6 (Source Lesson 14): Modal Auxiliaries
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Modal Auxiliaries",
        "unit_description": "Mastering the semantic nuances, degrees of obligation, and grammatical invariant rules of modal auxiliary verbs (can, could, may, might, will, would, shall, should, must) in formal and everyday communication.",
        "lesson_title": "Modal Auxiliaries",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Community Meeting and Civic Policy Deliberation",
                    "content": {
                        "title": "Civic Participation and Formal Discourse",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Community_Meeting_in_Kenya.jpg",
                        "caption": "Community members gathering in a civic hall to deliberate policies, where modal verbs regulate formality, permission, advice, and mandatory regulations.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify modal auxiliary verbs in written and spoken texts\n- Express varying degrees of attitude and mood: ability, possibility, permission, advice, and obligation\n- Distinguish between formal (*may*) and informal (*can*) modals of permission\n- Apply the invariant modal rule: Modal + Base Verb without 'to' or inflectional endings"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Classroom Request Scenario",
                    "content": {
                        "text": "Imagine asking your principal for permission to leave the hall. You could ask:\n\n*\"Can I leave?\"* or *\"May I leave?\"*\n\nWhat is the difference? While both ask for permission in everyday speech, **May** is formal, respectful, and polite, whereas **Can** focuses on physical capability. Changing a single modal verb adjusts your tone from a casual request to a polite plea, a gentle recommendation (*should*), or a binding legal command (*must*)."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Helper Verbs of Mood",
                    "content": {
                        "term": "Modal Auxiliary Verb",
                        "definition": "A helping verb that expresses the speaker's attitude, stance, or mood regarding an action—including ability, possibility, permission, necessity, advice, and obligation. Modals are grammatically invariant (never taking -s, -ed, or -ing)."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Modal Auxiliary Function & Spectrum Guide",
                    "content": {
                        "headers": ["Modal Verb", "Primary Function / Mood", "Level of Formality / Intensity", "Contextual Example"],
                        "rows": [
                            ["Can / Could", "Physical ability / Polite request", "Informal (Can) / Polite (Could)", "\"We **can** recycle plastic.\" / \"**Could** you please assist?\""],
                            ["May / Might", "Formal permission / Weak possibility", "High formality (May) / Speculative (Might)", "\"**May** I submit my report?\" / \"It **might** rain later today.\""],
                            ["Will / Would", "Future certainty / Polite conditional", "Definite certainty / Gentle request", "\"We **will** protect our wetlands.\" / \"**Would** you open the gate?\""],
                            ["Shall / Should", "Formal intention / Recommendation & advice", "Constitutional rule / Moral suggestion", "\"The council **shall** meet.\" / \"You **should** plant indigenous trees.\""],
                            ["Must / Have to", "Absolute necessity / Legal obligation", "Maximum intensity / Mandatory command", "\"All factories **must** treat toxic wastewater before discharge.\""]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Modal Auxiliaries Spectrum & Intensity Scale",
                    "content": {
                        "title": "The Volume Knob of Intent: Modal Auxiliaries Spectrum",
                        "caption": "Visual continuum arranging modals from low-intensity possibility (might/may) through ability (can/could), advice (should), to maximum obligation (must).",
                        "svg_content": SVG_MODAL_AUXILIARIES_SPECTRUM
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Deconstructing Modal Nuance in School Bylaws",
                    "content": {
                        "intro": "Examine how changing modal auxiliaries alters the legal force of school environmental rules:",
                        "steps": [
                            "**Version 1 (Gentle Advice):** *\"Students **should** pick up litter around the compound.\"* ➔ Recommended moral action; not strictly punished if missed.",
                            "**Version 2 (Permission):** *\"Students **may** pick up litter for extra environmental club points.\"* ➔ An allowed voluntary option.",
                            "**Version 3 (Absolute Obligation):** *\"Students **must** pick up litter around the compound.\"* ➔ A mandatory rule; failing to comply leads to disciplinary action.",
                            "**Syntax Check:** In all three sentences, the modal is followed directly by the base verb *pick* (never *to pick*, *picks*, or *picked*)."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Modal Verbs: Can, Could, May, Might, Should, Must",
                    "content": {
                        "title": "How to Use Modal Verbs in English",
                        "youtube_id": "Nk9nQwoCGuI",
                        "url": "https://www.youtube.com/watch?v=Nk9nQwoCGuI",
                        "description": "Comprehensive guide explaining the differences between modals of ability, permission, advice, and obligation with realistic spoken examples."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Policy Workbench: Drafting Club Regulations",
                    "content": {
                        "title": "Formulating School Environmental Club Rules",
                        "text": "**Drafting Challenge:** Assign appropriate modal verbs to complete the club charter:\n\n1. Attendance: *\"All registered members (must / may) attend weekly meetings.\"* ➔ **must** (Mandatory).\n2. Guest Policy: *\"Members (may / must) invite a guest if they notify the patron.\"* ➔ **may** (Permission).\n3. Badge: *\"Members (should / can) wear their club badges on assembly days.\"* ➔ **should** (Advice).\n\n**Result:** Clear modal distinction eliminates ambiguity between compulsory rules and voluntary privileges."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Double Modals and Inflection Errors",
                    "content": {
                        "incorrect": "We might will attend the clean-up, and she cans swim very well.",
                        "corrected": "We might attend the clean-up, and she can swim very well.",
                        "explanation": "In Standard English, never combine two modal verbs ('might will' is incorrect). Furthermore, modal verbs never take third-person '-s' ('she can', not 'she cans')."
                    }
                },
                {
                    "type": "step_process",
                    "title": "The Golden Rule of Modal Syntax",
                    "content": {
                        "title": "Modal Verb Verification Protocol",
                        "steps": [
                            "**Check Invariance:** Ensure the modal has no suffixes (no *-s*, *-ed*, *-ing*).",
                            "**Check Main Verb:** Verify the main verb following the modal is in its bare infinitive form without *to* (e.g., *must go*, not *must to go*).",
                            "**Audit Double Modals:** Ensure only one modal auxiliary accompanies a main verb clause."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Polite & Formal Requests",
                    "content": {
                        "question": "Sibling James wants to ask the school librarian for permission to borrow a rare encyclopaedia, wishing to sound formal and exceptionally polite. Which sentence should he use?",
                        "options": [
                            "I must borrow this encyclopaedia for my homework project.",
                            "Can you give me this encyclopaedia right now?",
                            "May I please borrow this encyclopaedia for my research?",
                            "Should I take this encyclopaedia for a few days?"
                        ],
                        "correct_answer": "May I please borrow this encyclopaedia for my research?",
                        "explanation": "Option C is correct because 'May' is the appropriate formal modal used to request permission politely. 'Must' is a demanding obligation, 'Can' is informal, and 'Should' asks for advice rather than permission."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Modal Syntax & Invariant Form",
                    "content": {
                        "question": "Which of the following sentences is grammatically flawless according to the rules of modal auxiliaries?",
                        "options": [
                            "Every citizen must to obey the environmental protection laws.",
                            "The community might can construct a sand dam before the rains.",
                            "All students should submit their conservation essays by Friday.",
                            "The ranger cans identify over fifty indigenous bird species."
                        ],
                        "correct_answer": "All students should submit their conservation essays by Friday.",
                        "explanation": "Option C is correct because 'should' is correctly followed by the bare base verb 'submit'. Option A incorrectly adds 'to' after 'must'; Option B incorrectly doubles modals ('might can'); Option D incorrectly inflects 'can' with '-s' ('cans')."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Precision with Modal Auxiliaries",
                    "content": {
                        "text": "Modal auxiliaries (*can, could, may, might, will, would, shall, should, must*) are the volume controls of communication. They allow speakers to nuance their statements from tentative possibilities to formal requests and binding legal obligations, always pairing directly with bare base verbs."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7 (Source Lesson 15): Present and Past Perfect Aspects
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Present and Past Perfect Aspects",
        "unit_description": "Constructing and distinguishing between present perfect (has/have + past participle) and past perfect (had + past participle) aspects to sequence past events and connect completed actions to present outcomes in consumer rights contexts.",
        "lesson_title": "Present and Past Perfect Aspects",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Customer Service and Commercial Transaction Review",
                    "content": {
                        "title": "Consumer Protection and Transaction Sequencing",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Supermarket_receipt_verification.jpg",
                        "caption": "A consumer reviewing purchase receipts and transaction records at a service counter, where establishing the exact chronology of past events is essential for resolving disputes.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between present perfect and past perfect aspects in speech and writing\n- Form the present perfect aspect using *has/have + past participle* for past actions relevant to the present\n- Form the past perfect aspect using *had + past participle* to sequence two completed past events\n- Articulate clear, chronological arguments in business correspondence and consumer complaints"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Returned Goods Dispute",
                    "content": {
                        "text": "Imagine you visit a store to return a defective radio. You say to the shopkeeper:\n\n*\"I came yesterday, but you closed the shop.\"*\n\nThis simple past sentence doesn't make the order clear. But if you say:\n\n*\"By the time I arrived, you **had closed** the shop.\"*\n\nThe past perfect aspect (**had closed**) clearly establishes that the shop closed *before* you arrived. Understanding perfect aspects allows you to sequence past actions with chronological precision."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Perfect Aspects",
                    "content": {
                        "term": "Present Perfect vs. Past Perfect Aspect",
                        "definition": "The present perfect aspect (*has/have + past participle*) connects a completed past action to the present moment. The past perfect aspect (*had + past participle*) functions as an anterior past tense, showing that one past event occurred before another past event."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Present Perfect vs. Past Perfect Structural Breakdown",
                    "content": {
                        "headers": ["Aspect", "Formula / Auxiliaries", "Participle Form", "Primary Temporal Focus", "Consumer Context Example"],
                        "rows": [
                            ["Present Perfect", "Subject + has/have", "Past Participle (V3: -ed / irregular)", "Past action with direct consequence right NOW", "\"I **have misplaced** my receipt (so I cannot get a refund now).\""],
                            ["Past Perfect", "Subject + had", "Past Participle (V3: -ed / irregular)", "Older of two past events; sets historical sequence", "\"The shop **had sold** the last item before we **arrived**.\""]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Present & Past Perfect Chronological Timeline",
                    "content": {
                        "title": "Chronological Anchoring & Action Sequencing Architecture",
                        "caption": "Timeline visual showing how Present Perfect links past events to the present moment, while Past Perfect sequences two distinct past actions.",
                        "svg_content": SVG_PERFECT_ASPECTS_TIMELINE
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Sequencing Two Past Events with Past Perfect",
                    "content": {
                        "intro": "Demonstrating how to combine two past events chronologically using Past Perfect and Simple Past:",
                        "steps": [
                            "**Event 1 (Occurred earlier at 2:00 PM):** The merchant updated the warranty terms.",
                            "**Event 2 (Occurred later at 4:00 PM):** The consumer signed the purchase contract.",
                            "**Step 1 (Identify Older Action):** Updating terms happened first ➔ Use Past Perfect (*had updated*).",
                            "**Step 2 (Identify Subsequent Action):** Signing contract happened second ➔ Use Simple Past (*signed*).",
                            "**Combined Sentence:** *\"The merchant **had updated** the warranty terms before the consumer **signed** the purchase contract.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Present Perfect vs. Past Perfect Tense",
                    "content": {
                        "title": "Mastering Present Perfect and Past Perfect Tenses",
                        "youtube_id": "b1keU_01Z0g",
                        "url": "https://www.youtube.com/watch?v=b1keU_01Z0g",
                        "description": "Clear timeline-based explanation of how to form and use the present perfect and past perfect tenses in English."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Consumer Rights Lab: Drafting a Formal Complaint Letter",
                    "content": {
                        "title": "Advocating Consumer Rights Through Precise Tenses",
                        "text": "**Complaint Scenario:** You bought a smartphone that broke within three days. Draft the core statement of fact:\n\n*\"Dear Manager, I write to inform you that I **have discovered** a defect in the phone purchased on Monday. Before I made the payment, your sales representative **had assured** me that the device was brand new. However, the battery **has failed** to hold a charge, so I **am requesting** an immediate replacement under consumer protection regulations.\"*\n\n**Chronological Accuracy:** Notice how *had assured* establishes the earlier promise that makes the present defect (*has failed*) actionable."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Using Past Perfect in Isolation without Past Anchor",
                    "content": {
                        "incorrect": "Yesterday afternoon, I had bought groceries at the supermarket.",
                        "corrected": "Yesterday afternoon, I bought groceries at the supermarket. (OR: I had bought groceries before the rain started.)",
                        "explanation": "Never use Past Perfect for a single, isolated past event. Past Perfect requires a second past event or a past time reference point to sequence against."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Perfect Aspect Selection Checklist",
                    "content": {
                        "title": "Chronological Audit Procedure",
                        "steps": [
                            "**Check Present Relevance:** Is the past action directly affecting the present moment? If yes ➔ Use Present Perfect (*has/have + V3*).",
                            "**Check for Dual Past Actions:** Are there two past actions in the sentence? If yes ➔ Put the older action in Past Perfect (*had + V3*) and the newer action in Simple Past (*V2*).",
                            "**Verify Irregular Participles:** Check irregular past participle forms (*eaten*, *bought*, *written*, *lost*)."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Past Perfect Action Sequencing",
                    "content": {
                        "question": "A consumer rights lawyer is presenting evidence. Which sentence correctly uses the **past perfect** aspect to sequence two past events?",
                        "options": [
                            "The client had buyed the product before they noticed the defect.",
                            "The client bought the product before they have noticed the defect.",
                            "The client had bought the product before they noticed the defect.",
                            "The client has bought the product before they had noticed the defect."
                        ],
                        "correct_answer": "The client had bought the product before they noticed the defect.",
                        "explanation": "Option C is correct because it uses the past perfect 'had bought' for the older past action (purchasing) and simple past 'noticed' for the later past action. Option A uses the incorrect participle 'buyed'; Options B and D mix present and past perfect incoherently."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Present Perfect vs. Simple Past",
                    "content": {
                        "question": "Which sentence correctly uses the **present perfect** aspect to show that a past action directly impacts the present situation?",
                        "options": [
                            "Sibling Mary has lost her warranty card, so she cannot request a refund today.",
                            "Sibling Mary had lost her warranty card, so she cannot request a refund today.",
                            "Sibling Mary losted her warranty card, so she cannot request a refund today.",
                            "Sibling Mary has lose her warranty card, so she cannot request a refund today."
                        ],
                        "correct_answer": "Sibling Mary has lost her warranty card, so she cannot request a refund today.",
                        "explanation": "Option A correctly uses 'has lost' (Present Perfect) to show that a past event continues to affect the present state ('cannot request a refund today'). Option B incorrectly uses past perfect without a past anchor; Options C and D use ungrammatical verb forms ('losted', 'has lose')."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Perfect Aspects in Action",
                    "content": {
                        "text": "The present perfect aspect (*has/have + past participle*) connects past actions directly to present reality. The past perfect aspect (*had + past participle*) acts as an anterior chronological anchor, allowing writers to sequence multiple past events with clarity."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8 (Source Lesson 16): Complex Sentences and Reported Speech
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Complex Sentences and Reported Speech",
        "unit_description": "Constructing complex sentences with subordinating conjunctions and converting direct speech into indirect (reported) speech by systematically adjusting pronouns, verb tenses, and time adverbials.",
        "lesson_title": "Complex Sentences and Reported Speech",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Sports Journalist Interviewing Football Player Post-Match",
                    "content": {
                        "title": "Sports Journalism and Post-Match Interviews",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/58/Post_match_press_conference.jpg",
                        "caption": "A sports journalist recording player quotes during a post-match conference, requiring direct speech to be converted accurately into reported speech for newspaper articles.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify independent and dependent clauses in complex sentences\n- Combine clauses using subordinating conjunctions (*although*, *because*, *unless*, *while*)\n- Convert direct speech into reported (indirect) speech while systematically backshifting tenses, pronouns, and time expressions\n- Write accurate journalistic summaries of interviews and speeches"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Post-Match Press Conference",
                    "content": {
                        "text": "Imagine you are a sports reporter interviewing a football striker after a tournament final. The striker says directly to you:\n\n*\"I am playing in the regional cup tomorrow.\"*\n\nWhen writing your newspaper article, you cannot write: *\"The striker said I am playing in the regional cup tomorrow,\"* because that would mean YOU are playing! Instead, you report:\n\n*\"The striker stated **that he was playing in the regional cup the next day**.\"*\n\nNotice how the pronoun (*I ➔ he*), the tense (*am playing ➔ was playing*), and the time word (*tomorrow ➔ the next day*) systematically shift."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Complex Syntax & Indirect Speech",
                    "content": {
                        "term": "Complex Sentence & Reported Speech",
                        "definition": "A complex sentence consists of one independent clause and at least one dependent clause introduced by a subordinating conjunction. Reported (indirect) speech conveys the meaning of a speaker's words without quoting verbatim, applying systematic backshifts to pronouns, tenses, and time expressions."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Reported Speech Shift Transformation Table",
                    "content": {
                        "headers": ["Grammatical Dimension", "Direct Speech Form", "Indirect (Reported) Shift", "Example Transformation"],
                        "rows": [
                            ["Pronouns", "I / We / You", "He, She / They / I, We", "\"I am ready\" ➔ He said **he** was ready"],
                            ["Present Simple", "Base / -s form (e.g., *play*)", "Past Simple (*played*)", "\"I play football\" ➔ She said she **played** football"],
                            ["Present Continuous", "am / is / are playing", "was / were playing", "\"We are training\" ➔ They said they **were training**"],
                            ["Present Perfect", "has / have played", "had played (Past Perfect)", "\"I have scored\" ➔ He said he **had scored**"],
                            ["Past Simple", "played", "had played (Past Perfect)", "\"I bought tickets\" ➔ She said she **had bought** tickets"],
                            ["Modals: will / can / may", "will / can / may", "would / could / might", "\"I will win\" ➔ He said he **would** win"],
                            ["Time: Today / Tomorrow", "today / tomorrow", "that day / the next (following) day", "\"today\" ➔ **that day** | \"tomorrow\" ➔ **the next day**"],
                            ["Time: Yesterday / Now", "yesterday / now", "the day before (previous day) / then", "\"yesterday\" ➔ **the previous day** | \"now\" ➔ **then**"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Complex Sentence & Reported Speech Transformation Engine",
                    "content": {
                        "title": "Reported Speech Shift & Complex Sentence Architecture",
                        "caption": "Visual breakdown of direct-to-indirect backshift rules alongside subordinating conjunction clause coupling.",
                        "svg_content": SVG_REPORTED_SPEECH_ENGINE
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Full Direct-to-Reported Speech Transformation Model",
                    "content": {
                        "intro": "Watch how a direct quote from a team captain is converted into reported speech for a news article:",
                        "steps": [
                            "**Direct Quote:** *The captain declared, \"We have trained hard today, and we will win the final tomorrow.\"*",
                            "**Step 1 (Adjust Pronouns):** *We* ➔ **they**.",
                            "**Step 2 (Backshift Tenses):** *have trained* (Present Perfect) ➔ **had trained** (Past Perfect); *will win* ➔ **would win**.",
                            "**Step 3 (Shift Time Adverbials):** *today* ➔ **that day**; *tomorrow* ➔ **the next day**.",
                            "**Step 4 (Remove Quotes & Insert 'that'):** Remove quotation marks.",
                            "**Reported Version:** *\"The captain declared that **they had trained** hard **that day**, and **they would win** the final **the next day**.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Direct and Indirect Speech in English",
                    "content": {
                        "title": "Reported Speech: Tense Shifts, Pronouns, and Time Markers",
                        "youtube_id": "rpnxR_uK_1M",
                        "url": "https://www.youtube.com/watch?v=rpnxR_uK_1M",
                        "description": "Comprehensive tutorial covering how to convert statements and questions from direct speech into reported speech."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Journalism Lab: Post-Match Match Report",
                    "content": {
                        "title": "Writing a Sports Tournament Article",
                        "text": "**Raw Interview Audio:** *The coach said, \"Although our striker was injured in the first half, I am proud of the team because they never surrendered.\"*\n\n**Journalistic Reporting:**\n*\"In his post-match conference, the coach remarked that **although their striker had been injured** in the first half, **he was proud** of the team **because they had never surrendered**.\"*\n\n**Complex Clause Analysis:** The sentence integrates two dependent clauses (*although...*, *because...*) smoothly within reported speech framework."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "common_mistake",
                    "title": "Forgetting Time Marker Backshifts and Inverted Comma Retention",
                    "content": {
                        "incorrect": "The referee said that \"he will issue a red card tomorrow\".",
                        "corrected": "The referee said that he would issue a red card the next day.",
                        "explanation": "When converting to reported speech, always remove quotation marks, backshift modal verbs ('will' ➔ 'would'), and adjust time adverbials ('tomorrow' ➔ 'the next day')."
                    }
                },
                {
                    "type": "step_process",
                    "title": "4-Step Direct-to-Reported Conversion Protocol",
                    "content": {
                        "title": "Reported Speech Protocol",
                        "steps": [
                            "**Drop Inverted Commas:** Remove quotation marks and insert the conjunction *that* (optional in spoken English, standard in formal writing).",
                            "**Shift Pronouns:** Change 1st and 2nd person pronouns (*I, we, you*) to 3rd person (*he, she, they*).",
                            "**Backshift Verb Tenses:** Step every present tense back into its corresponding past form.",
                            "**Adjust Time & Place Markers:** Convert *here ➔ there*, *now ➔ then*, *today ➔ that day*, *tomorrow ➔ the next day*, *yesterday ➔ the previous day*."
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 1: Direct-to-Reported Conversion",
                    "content": {
                        "question": "A sports reporter is writing an article. The goalkeeper told the media: *\"I will save the penalty kick today.\"* Which of the following is the correct reported speech version of this statement?",
                        "options": [
                            "The goalkeeper told the media that he will save the penalty kick today.",
                            "The goalkeeper told the media that I would save the penalty kick that day.",
                            "The goalkeeper told the media that he would save the penalty kick that day.",
                            "The goalkeeper told the media that he had saved the penalty kick yesterday."
                        ],
                        "correct_answer": "The goalkeeper told the media that he would save the penalty kick that day.",
                        "explanation": "Option C is correct because it systematically shifts the pronoun ('I' ➔ 'he'), backshifts the modal ('will' ➔ 'would'), and updates the time expression ('today' ➔ 'that day'). Option A fails to shift 'will' and 'today'; Option B fails to shift 'I'; Option D incorrectly changes 'will save' to past perfect 'had saved'."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Concept Check 2: Complex Sentence Clause Identification",
                    "content": {
                        "question": "In the complex sentence: *\"Although our star midfielder was injured, the school team secured the championship trophy.\"*, which part is the **dependent clause**?",
                        "options": [
                            "the school team secured the championship trophy",
                            "secured the championship trophy",
                            "Although our star midfielder was injured",
                            "our star midfielder was injured the school team"
                        ],
                        "correct_answer": "Although our star midfielder was injured",
                        "explanation": "Option C is the dependent (subordinate) clause because it begins with the subordinating conjunction 'Although' and cannot stand alone as a complete grammatical sentence. Option A is the independent clause."
                    }
                },
                {
                    "type": "summary",
                    "title": "Key Takeaway: Complex Syntax and Speech Reporting",
                    "content": {
                        "text": "Complex sentences use subordinating conjunctions (*although, because, unless, since*) to establish clear logical connections between ideas. Reported speech allows writers to recount spoken statements accurately through systematic shifts in **pronouns**, **verb tenses**, and **time markers**."
                    }
                }
            ]
        ]
    }
]
