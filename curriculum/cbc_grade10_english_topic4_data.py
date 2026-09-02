"""
VLearn CBC Grade 10 English — Topic 4: Writing
Full Structured Lesson Card Definitions for Lessons 1 to 10
"""

from curriculum.cbc_grade10_english_topic4_svgs import (
    SVG_LESSON_1_PARAGRAPH_FOUNDATIONS,
    SVG_LESSON_2_SPELLING_ACRONYMS,
    SVG_LESSON_3_EFFECTIVE_WRITING_ELEMENTS,
    SVG_LESSON_4_PUNCTUATION_CAPITALIZATION,
    SVG_LESSON_5_WRITING_PROCESS_PIPELINE,
    SVG_LESSON_6_NARRATIVE_DESCRIPTIVE_FRAMEWORK,
    SVG_LESSON_7_FORMAL_LETTER_ANATOMY,
    SVG_LESSON_8_REPORTS_MEMOS_EMAILS,
    SVG_LESSON_9_MEETING_GOVERNANCE_MINUTES,
    SVG_LESSON_10_INTEGRATED_PORTFOLIO_PUBLICATION,
)

TOPIC_4_LESSONS = [
    # =========================================================================
    # LESSON 1: Sentence Fluency and Paragraph Foundations
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Sentence Fluency and Paragraph Foundations",
        "unit_description": "Building blocks of cohesive writing: topic sentence construction, controlling ideas, paragraph unity, and logical transitions.",
        "lesson_title": "Sentence Fluency and Paragraph Foundations",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Writing in Classroom in Kenya",
                    "content": {
                        "title": "Collaborative Composition and Paragraph Drafting",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Students_writing_in_classroom_Kenya.jpg/800px-Students_writing_in_classroom_Kenya.jpg",
                        "caption": "Secondary school students drafting and structuring cohesive academic paragraphs using clear topic sentences and logical transition markers.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define the architecture of a paragraph (topic sentence, supporting details, concluding sentence)\n- Craft effective topic sentences with clear subjects and limiting controlling ideas\n- Maintain paragraph unity by identifying and eliminating off-topic 'drift' sentences\n- Enhance sentence fluency and paragraph coherence using organic logical transitions"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Choppy Sports Report",
                    "content": {
                        "text": "Consider the difference between a disconnected pile of sentences and a cohesive paragraph:\n\n> *\"Sports are great. I like football. It is healthy. We played yesterday. The pitch was muddy. Our team won. Exercise helps mental wellness too.\"*\n\nWhile each individual sentence is grammatically correct, the passage feels choppy and robotic. Now observe the restructured version:\n\n> *\"Participating in team sports offers incredible benefits for physical and mental wellness. First and foremost, regular matches build cardiovascular stamina and muscle strength. In addition to physical vitality, on-field collaboration reduces stress and elevates mood. Consequently, dedicating time to athletics is an indispensable strategy for personal well-being.\"*\n\nThe second passage succeeds because it anchors around a central **topic sentence**, provides **unified supporting details**, and concludes with a resonant synthesis."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Paragraph Foundations",
                    "content": {
                        "term": "Paragraph Architecture & The 4 Pillars",
                        "definition": "A **paragraph** is a cohesive group of related sentences focused on a single central idea. The **Topic Sentence** establishes the subject and a limiting **Controlling Idea**. The **4 Pillars** are: **Unity** (all sentences support one point), **Completeness** (sufficient evidence), **Coherence** (logical flow and signposting), and **Order** (purposeful organization)."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Four Pillars of Paragraph Architecture",
                    "content": {
                        "headers": ["Pillar", "Definition", "Common Flaw to Avoid", "Correct Practice"],
                        "rows": [
                            ["Unity", "Every sentence directly reinforces the topic sentence's controlling idea.", "Drifting into unrelated or tangentially related sub-topics.", "Omit off-topic sentences or move them into distinct paragraphs."],
                            ["Completeness", "Sufficient elaboration, concrete facts, data, or illustrative examples.", "Leaving assertions unsupported or ending abruptly after one fact.", "Provide at least 2-3 substantive supporting details with depth."],
                            ["Coherence", "Smooth, seamless connection between thoughts using logical transitions.", "Robotic repetitive listing ('Firstly, Secondly, Thirdly, Lastly').", "Use varied conjunctive adverbs (*furthermore, consequently, conversely*)."],
                            ["Order", "A deliberate organizational pattern (chronological, spatial, emphatic).", "Scattering facts randomly without a recognizable progression.", "Arrange details by chronological sequence or order of importance."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Paragraph Architecture Diagram",
                    "content": {
                        "title": "The Architecture of a Cohesive Paragraph",
                        "caption": "Structural diagram illustrating the topic sentence foundation, supporting pillars (Unity, Development, Coherence), and concluding anchor.",
                        "svg_content": SVG_LESSON_1_PARAGRAPH_FOUNDATIONS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Dissecting an Exemplary Paragraph",
                    "content": {
                        "intro": "Examine the anatomical breakdown of this formal academic paragraph:",
                        "steps": [
                            "**Exemplar Text:** *'Deforestation in the Mau Forest complex poses severe ecological threats to Kenya's water towers. To begin with, indiscriminate tree clearing accelerates soil erosion, silting major rivers that feed Lake Victoria and Lake Nakuru. Furthermore, the loss of dense canopy cover disrupts localized rainfall cycles, leading to prolonged agricultural droughts across surrounding counties. Consequently, strict conservation enforcement and aggressive reforestation are imperative to secure Kenya's freshwater future.'*",
                            "**Topic Sentence:** *'Deforestation in the Mau Forest complex poses severe ecological threats to Kenya's water towers.'* (Subject: Mau Forest deforestation; Controlling idea: severe ecological threats to water towers).",
                            "**Supporting Detail 1 (Erosion & Silting):** *'To begin with, indiscriminate tree clearing accelerates soil erosion...'* (Introduced by initial signpost).",
                            "**Supporting Detail 2 (Rainfall disruption):** *'Furthermore, the loss of dense canopy cover disrupts localized rainfall cycles...'* (Linked by additive transition).",
                            "**Concluding Synthesis:** *'Consequently, strict conservation enforcement... are imperative to secure Kenya's freshwater future.'* (Signals logical outcome and closure)."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "How to Write Supporting and Concluding Sentences",
                    "content": {
                        "title": "Mastering Paragraph Development and Cohesion",
                        "youtube_id": "YFZo2cQh5kg",
                        "url": "https://www.youtube.com/watch?v=YFZo2cQh5kg",
                        "description": "Video lesson covering topic sentence formulation, eliminating paragraph drift, and crafting powerful concluding sentences."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Unity and Flow Diagnostic",
                    "content": {
                        "title": "Analyzing Paragraph Coherence and Sentence Signposts",
                        "text": "**Pre-Viewing Focus:** Pay attention to how the instructor distinguishes between an *elaboration sentence* (which develops the controlling idea) and a *drift sentence* (which distracts the reader).\n\n**Post-Viewing Writing Challenge:** In your notebooks, write a 5-sentence paragraph on **'The Role of Digital Learning in Secondary Education'**. Highlight your topic sentence in green, your transitional connectors (*furthermore, consequently*) in yellow, and verify that 0% of your sentences drift off-topic."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Paragraph Pitfalls & Repairs",
                    "content": {
                        "text": "### Pitfall 1: Topic Sentence Without a Controlling Idea\n- **Flawed:** *\"Global warming is something that exists in the world today.\"* *(Vague, lacks purpose or limit)*\n- **Repaired:** *\"Rising global temperatures threaten coastal agricultural ecosystems in East Africa through saltwater intrusion.\"*\n\n### Pitfall 2: Paragraph Drift (Violating Unity)\n- **Flawed:** *\"Establishing regular morning study routines improves student retention. Morning hours offer quiet concentration and fresh energy. **Moreover, our school cafeteria recently upgraded its breakfast menu.** This consistent scheduling reduces exam-week anxiety.\"*\n- **Repaired:** Eliminate the cafeteria sentence immediately to preserve 100% thematic unity.\n\n### Pitfall 3: Mechanical / Robotic Transition Stacking\n- **Flawed:** *\"Firstly, he ran. Secondly, he jumped. Thirdly, he scored. Fourthly, we celebrated.\"*\n- **Repaired:** *\"After sprinting past the defender, he executed a clean leap and scored; immediately, the entire stadium erupted in celebration.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Paragraph Editing and Unity Check",
                    "content": {
                        "intro": "Work through these guided paragraph repair challenges:",
                        "steps": [
                            {"title": "Challenge 1: Controlling Idea Identification", "description": "Prompt: 'Mobile payment platforms have democratized access to financial services for rural Kenyan entrepreneurs.' Subject = Mobile payment platforms; Controlling Idea = Democratizing financial access for rural entrepreneurs."},
                            {"title": "Challenge 2: Spot the Drift Sentence", "description": "Prompt: 'Traveling broadens cultural empathy. It exposes learners to diverse languages and traditions. Airline ticket prices fluctuate depending on global fuel rates. These intercultural encounters dismantle stereotypes.' The airline ticket sentence breaks unity and must be removed."},
                            {"title": "Challenge 3: Transition Optimization", "description": "Prompt: Replace the repetitive phrase 'Also' with sophisticated connectors such as 'In addition', 'Furthermore', or 'Equally important'."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Topic Sentence Selection",
                    "content": {
                        "question": "Which of the following sentences represents the most effective topic sentence for an academic paragraph?",
                        "options": [
                            "Pollution is a massive problem that many people across the world talk about regularly.",
                            "In this paragraph, I will explain why electric vehicles reduce urban greenhouse gas emissions.",
                            "The adoption of solar-powered drip irrigation has significantly stabilized crop yields in arid Kenyan counties.",
                            "Solar energy and farming are both very interesting modern topics for students to study."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: it contains a specific subject ('The adoption of solar-powered drip irrigation') and a clear, limiting controlling idea ('has significantly stabilized crop yields in arid Kenyan counties'). Option A is too vague; Option B uses amateur meta-language ('In this paragraph, I will...'); Option D is an unfocused generic statement."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Paragraph Unity Evaluation",
                    "content": {
                        "question": "Read the draft paragraph: '(1) Regular cardiovascular exercise strengthens the heart and enhances lung capacity. (2) Daily jogging triggers the release of endorphins, reducing mental anxiety. (3) Many sporting goods stores offer discounts on running shoes during December holidays. (4) Consequently, integrating active movement into one's daily routine fosters comprehensive wellness.' Which sentence breaks paragraph unity?",
                        "options": [
                            "Sentence 1",
                            "Sentence 2",
                            "Sentence 3",
                            "Sentence 4"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C (Sentence 3) is correct. While sentences 1, 2, and 4 focus strictly on the physiological and psychological benefits of exercise, Sentence 3 drifts into retail shoe sales and holiday discounts, violating paragraph unity."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Topic Sentences** require both a specific subject and a limiting controlling idea that charts the paragraph's boundaries.\n- **Paragraph Unity** mandates that every single supporting sentence directly backs the central thesis—ruthlessly cut drifting details.\n- **Coherence** is achieved through organic signpost transitions (*consequently, furthermore, conversely*) rather than robotic numbered lists."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Spelling, Abbreviations, and Acronyms
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Spelling, Abbreviations, and Acronyms",
        "unit_description": "Mechanical precision in writing: spelling rules, homophone disambiguation, abbreviation conventions, and the First-Mention Rule.",
        "lesson_title": "Spelling, Abbreviations, and Acronyms",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Open Dictionary and Scholarly Reference Material",
                    "content": {
                        "title": "Lexical Precision and Orthographic Accuracy",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Open_dictionary_with_glasses.jpg/800px-Open_dictionary_with_glasses.jpg",
                        "caption": "Consulting dictionaries and reference guides to verify correct orthography, double consonant rules, and abbreviation standards in academic writing.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Master tricky English spelling patterns (silent letters, double consonants, suffix additions)\n- Correctly distinguish and deploy easily confused homophone pairs (e.g., *principal/principle, affect/effect*)\n- Differentiate between abbreviations, initialisms, and true acronyms\n- Apply the First-Mention Rule for institutional acronyms and abbreviations in formal documents"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Informal Banking Alert",
                    "content": {
                        "text": "Imagine receiving the following message from your local branch:\n\n> *\"Dear Client, we need **u** to update ur **acc** info **ASAP** so we can fix the **probs** with the **IT** sys.\"*\n\nYou would likely flag it as fraudulent or unprofessional! Contrast that with the formal, standardized version:\n\n> *\"Dear Valued Client, we kindly request that you update your account **information as soon as possible** to enable our **information technology (IT)** department to resolve the system discrepancies.\"*\n\nAccurate spelling and disciplined abbreviation protocols build immediate institutional trust, clarity, and authority."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Spelling & Short-Forms",
                    "content": {
                        "term": "Orthography, Initialisms, Acronyms & The First-Mention Rule",
                        "definition": "An **Abbreviation** is a shortened word form (e.g., *Dr., Jan., e.g.*). An **Acronym** is formed from initial letters and pronounced as a single word (e.g., *UNESCO, NASA, NEMA*). An **Initialism** is pronounced letter-by-letter (e.g., *IT, BBC, NGO*). The **First-Mention Rule** requires writing out the full title on initial appearance, followed by the acronym in parentheses."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Orthographic and Short-Form Taxonomy",
                    "content": {
                        "headers": ["Category", "Definition & Mechanism", "Standard Form", "Misuse / Error Trap"],
                        "rows": [
                            ["Double Consonants", "Silent prefix/suffix junctions requiring doubled letters", "ne-ces-sa-ry, oc-cur-rence, com-mit-tee", "Writing *neccessary* or *occurance*"],
                            ["Silent Letters", "Etymological letters preserved in spelling but unvoiced", "en-vi-ron-ment (n), go-vern-ment (n)", "Omitting the internal 'n' in *environment*"],
                            ["Homophones", "Identical phonetics, distinct etymology and spelling", "principal (leader/fund) vs. principle (rule)", "Confusing *stationery* (paper) with *stationary* (fixed)"],
                            ["Acronym", "Initial letters pronounced as a unified word", "UNESCO, KRA, NEMA", "Using informal slang abbreviations in formal prose"],
                            ["Initialism", "Initial letters voiced individually", "KICD, TSC, NGO, ICT", "Failing to define on first mention"],
                            ["Latin Abbreviations", "Scholarly Latin short-forms", "e.g. (*exempli gratia* = for example); i.e. (*id est* = that is)", "Using *e.g.* when *i.e.* is required for exact restatement"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Spelling and Short-Forms Mechanics Matrix",
                    "content": {
                        "title": "Mechanics Matrix: Spelling, Short-Forms & Protocols",
                        "caption": "Architectural quadrant mapping spelling traps, homophone pairs, acronym vs. initialism taxonomies, and the First-Mention workflow.",
                        "svg_content": SVG_LESSON_2_SPELLING_ACRONYMS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Applying the First-Mention Rule",
                    "content": {
                        "intro": "Observe how an institutional document introduces and deploys acronyms across consecutive sentences:",
                        "steps": [
                            "**First Mention (Sentence 1):** *'The **Kenya Institute of Curriculum Development (KICD)** conducted a comprehensive review of senior school competencies.'* (Full institutional title written out in title case, immediately followed by the abbreviation in parentheses).",
                            "**Subsequent Mention (Sentence 2):** *'During the stakeholder briefing, **KICD** officials highlighted the integration of digital literacy across all learning areas.'* (Acronym used independently without repeated definitions).",
                            "**Multiple Acronym Coordination:** *'The **Teachers Service Commission (TSC)** and the **Ministry of Education (MoE)** collaborated with **KICD** to finalize teacher orientations.'* (Each distinct entity introduced with full expansion upon its first appearance)."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "5 Spelling Rules to Improve Your English",
                    "content": {
                        "title": "Mastering English Spelling Patterns and Suffix Rules",
                        "youtube_id": "A2ABK_EB_UM",
                        "url": "https://www.youtube.com/watch?v=A2ABK_EB_UM",
                        "description": "Essential orthographic guidelines covering silent E drops, doubling final consonants, and the 'i before e' rule."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Orthography and Acronym Audit",
                    "content": {
                        "title": "Proofreading Official School Circulars",
                        "text": "**Pre-Viewing Focus:** Note the suffix rules governing silent final 'e' (*hope -> hoping*, *care -> careful*) and when the final consonant is doubled (*occur -> occurred* vs. *open -> opened*).\n\n**Post-Viewing Writing Challenge:** Examine this draft sentence from a school board report: *'It is truely neccessary that the comittee updates it's enviromental policy ASAP.'* Identify and rectify all 5 mechanical errors."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Spelling & Abbreviation Traps",
                    "content": {
                        "text": "### Trap 1: Confusing 'Principal' and 'Principle'\n- **Incorrect:** *\"The school **principle** addressed the moral **principals** of the students.\"*\n- **Correct:** *\"The school **principal** (school head) addressed the moral **principles** (fundamental truths/rules) of the students.\"*\n\n### Trap 2: Suffix Dropping Errors ('Truly' and 'Definitely')\n- **Incorrect:** *\"We are **truely** grateful and **definitly** committed.\"*\n- **Correct:** *\"We are **truly** grateful and **definitely** committed.\"* *(Drop 'e' in 'true + ly'; retain root in 'definite + ly').*\n\n### Trap 3: Possessive 'Its' vs. Contraction 'It's'\n- **Incorrect:** *\"The organization celebrated **it's** silver jubilee.\"*\n- **Correct:** *\"The organization celebrated **its** silver jubilee.\"* *('Its' is possessive; 'it's' = 'it is').*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Precision Editing",
                    "content": {
                        "intro": "Execute orthographic corrections on these authentic sentences:",
                        "steps": [
                            {"title": "Item 1: Homophone Disambiguation", "description": "Draft: 'The economic policy had a severe (affect/effect) on currency valuation.' Solution: Use 'effect' (noun indicating result). 'Affect' is the verb meaning to influence."},
                            {"title": "Item 2: Double Consonant Repair", "description": "Draft: 'The hotel provides luxurious (accomodation/accommodation) for delegates.' Solution: 'Accommodation' has double 'c' and double 'm' (ac-com-mo-da-tion)."},
                            {"title": "Item 3: First-Mention Application", "description": "Draft: 'NEMA inspected the riverbanks.' Solution: Expand to 'The **National Environment Management Authority (NEMA)** inspected the riverbanks.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Orthographic Accuracy",
                    "content": {
                        "question": "Which of the following sentences is free of all spelling and mechanics errors?",
                        "options": [
                            "It is neccessary to protect our natural enviornment from industrial waste.",
                            "It is necessary to protect our natural environment from industrial waste.",
                            "It is necessary to protect our natural enviornment from industrial waste.",
                            "It is neccessary to protect our natural environment from industrial waste."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: 'necessary' is spelled with one 'c' and double 's' (remember: 1 Collar, 2 Sleeves), and 'environment' retains the silent internal 'n' before '-ment'. Options A, C, and D contain spelling errors."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: First-Mention Acronym Protocol",
                    "content": {
                        "question": "Which option demonstrates the correct application of the First-Mention Rule in formal prose?",
                        "options": [
                            "WHO (World Health Organization) released new adolescent wellness guidelines yesterday.",
                            "The World Health Organization (WHO) released new adolescent wellness guidelines yesterday.",
                            "The World Health Organization released new guidelines, also known by everyone as WHO.",
                            "The WHO (which stands for World Health Organization) released new adolescent wellness guidelines."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: the full official institutional title is written first in title case, followed immediately by the acronym enclosed in parentheses. Option A reverses the order; Options C and D introduce conversational wordiness."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Spelling Precision** safeguards professional credibility: master double-consonant roots (*necessary, accommodation*) and silent letters (*environment*).\n- **Homophones** demand contextual scrutiny: remember *principal* (head of school / chief capital) vs. *principle* (ethical rule).\n- **Acronyms and Initialisms** must always be fully expanded on first mention before standalone usage."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Elements of Effective Writing
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Elements of Effective Writing",
        "unit_description": "Strategic composition: adapting purpose, audience, register, tone, and lexical cohesion across formal and informal contexts.",
        "lesson_title": "Elements of Effective Writing",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students in Formal Academic Debate",
                    "content": {
                        "title": "Audience Adaptation and Rhetorical Register",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Students_discussing_in_library.jpg/800px-Students_discussing_in_library.jpg",
                        "caption": "Learners analyzing purpose, target audience, and formal register to calibrate tone and vocabulary for persuasive academic discourse.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Analyze writing situations using the core elements: Purpose, Audience, Register, Tone, and Cohesion\n- Distinguish clearly between formal and informal registers in vocabulary, syntax, and contraction usage\n- Select tone and connotative diction appropriate to specific communicative objectives\n- Avoid inappropriate register clash and maintain smooth textual cohesion"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Textbook Replacement Request",
                    "content": {
                        "text": "Compare two approaches to requesting a textbook replacement after accidental water damage:\n\n*   **Draft A (Text message to a friend):**\n    > *\"Hey! Guess what? My dog completely shredded my English book lol. I need a new one so bad!\"*\n\n*   **Draft B (Formal letter to the school principal):**\n    > *\"Dear Principal, I am writing to formally request a replacement copy of the Grade 10 English coursebook. Regrettably, my copy was damaged in an unavoidable domestic accident. I am prepared to defray any associated replacement costs.\"*\n\nDraft B succeeds in a formal institutional context because the writer consciously adapted **purpose** (formal request), **audience** (school principal), **register** (formal standard English), and **tone** (respectful and accountable)."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Elements of Writing",
                    "content": {
                        "term": "Purpose, Audience, Register, Tone & Cohesion",
                        "definition": "**Purpose** is the communicative objective (to inform, persuade, request, entertain). **Audience** is the intended readership. **Register** refers to the level of formality dictated by social distance. **Tone** is the writer's attitude conveyed through word connotations. **Cohesion** is the structural glue connecting sentences logically."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Formal vs. Informal Register Spectrum",
                    "content": {
                        "headers": ["Dimension", "Formal Register (Academic / Professional)", "Informal Register (Casual / Peer)"],
                        "rows": [
                            ["Vocabulary", "Precise, sophisticated, Latinate (*generate revenue, investigate, facilitate*)", "Colloquial, phrasal verbs, slang (*make money, look into, help out*)"],
                            ["Contractions", "Strictly prohibited (*do not, cannot, it is, will not*)", "Widely utilized (*don't, can't, it's, won't*)"],
                            ["Sentence Structure", "Complex, varied clauses, nominalizations, passive when objective", "Short, simple, conversational, active fragments"],
                            ["Pronouns & Person", "Objective third person (*the applicant, the researcher*) or formal first person", "Subjective first/second person (*I, you, we, guys*)"],
                            ["Punctuation", "Standard punctuation (semicolons, colons, commas)", "Exclamation marks, ellipses (...), emojis, dashes"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Elements of Effective Writing Diagram",
                    "content": {
                        "title": "The Rhetorical Pentagram: Purpose, Audience & Register",
                        "caption": "Interactive framework mapping Purpose, Audience, Register, Tone, and Cohesion into balanced, effective written discourse.",
                        "svg_content": SVG_LESSON_3_EFFECTIVE_WRITING_ELEMENTS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Register Calibration",
                    "content": {
                        "intro": "Observe how an informal message is transformed into formal institutional prose:",
                        "steps": [
                            "**Informal Baseline:** *\"We got a ton of cash from our online store last month so we can buy some cool new gear.\"*",
                            "**Step 1: Replace Slang/Colloquialisms:** Replace 'got a ton of cash' with *'generated substantial revenue'*; replace 'cool new gear' with *'state-of-the-art equipment'*.",
                            "**Step 2: Elevate Syntax & Connectors:** Replace 'so we can buy' with *'which enables the acquisition of'*.",
                            "**Step 3: Formal Re-synthesis:** *'The e-commerce platform generated substantial revenue during the previous month, facilitating the procurement of modern laboratory equipment.'*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Purpose, Audience, and Tone in Writing",
                    "content": {
                        "title": "Analyzing Rhetorical Context Before Writing",
                        "youtube_id": "iB9zXXlzwTc",
                        "url": "https://www.youtube.com/watch?v=iB9zXXlzwTc",
                        "description": "Video tutorial examining how audience expectations shape tone, vocabulary selection, and persuasive effectiveness."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Dual-Register Composition Challenge",
                    "content": {
                        "title": "Contextual Register Adaptation",
                        "text": "**Pre-Viewing Focus:** Identify the three core questions every writer must ask before drafting: *1. Who is my reader? 2. What action do I want them to take? 3. What emotional tone will best achieve this outcome?*\n\n**Post-Viewing Writing Challenge:** A minor water pipe leak flooded part of your classroom. Draft two distinct 2-sentence texts: (1) An informal text message to a classmate, and (2) A formal email report to the Deputy Principal requesting maintenance."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Register & Tone Errors",
                    "content": {
                        "text": "### Error 1: Register Clash (Incongruous Slang in Formal Text)\n- **Flawed:** *\"We are pleased to inform you that your scholarship application has been approved, **so you can chill out now**.\"*\n- **Repaired:** *\"We are pleased to inform you that your scholarship application has been approved; **consequently, you may proceed with enrollment**.\"*\n\n### Error 2: Aggressive / Demanding Tone in Complaints\n- **Flawed:** *\"Your cafeteria food is completely disgusting and your cooks are lazy. Fix this right now!\"*\n- **Repaired:** *\"I am writing to express concern regarding food hygiene and preparation standards in the dining facility, and I request a formal review by the health committee.\"*\n\n### Error 3: Contraction Infiltration in Academic Writing\n- **Flawed:** *\"The data **doesn't** prove that temperature **won't** rise.\"*\n- **Repaired:** *\"The data **does not** prove that temperature **will not** rise.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Register Transformation",
                    "content": {
                        "intro": "Transform these sentences to achieve a formal academic register:",
                        "steps": [
                            {"title": "Sentence 1: Casual Phrasal Verb", "description": "Informal: 'The committee looked into the problem.' Formal: 'The committee **investigated the issue**.'"},
                            {"title": "Sentence 2: Exclamation & Colloquialism", "description": "Informal: 'It was super obvious that the plan was bad!' Formal: 'It was **readily apparent that the strategy possessed critical shortcomings**.'"},
                            {"title": "Sentence 3: Conversational Fillers", "description": "Informal: 'You know, like, trees help stop flooding.' Formal: '**Afforestation plays an indispensable role in flood mitigation**.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Register and Tone Discerning",
                    "content": {
                        "question": "Imagine you are drafting a formal inquiry to an environmental research foundation. Which option exhibits the most appropriate register and tone?",
                        "options": [
                            "Hey guys, I wanna know what bursaries you have for wildlife conservation, hit me back ASAP!",
                            "I am writing to respectfully inquire about the criteria and application procedures for the wildlife conservation fellowship.",
                            "Give me the information about the conservation grants right now because I need the money.",
                            "I would love it if you could graciously bestow upon me the marvelous details of your funding program."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: it employs formal vocabulary ('respectfully inquire', 'application procedures'), avoids contractions, and maintains a respectful, professional tone. Option A is colloquial/slang; Option C is demanding/aggressive; Option D is overly dramatic and melodramatic."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Identifying Register Clash",
                    "content": {
                        "question": "Which of the following sentences exhibits a 'register clash' (mixing formal academic style with informal colloquialisms)?",
                        "options": [
                            "The board resolved to allocate additional capital to support digital infrastructure.",
                            "The researchers discovered that prolonged droughts severely impair crop productivity.",
                            "The institution conducted a comprehensive financial audit and found out the accounts were totally messed up.",
                            "Regular physical conditioning fosters both cardiovascular endurance and psychological resilience."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C contains a severe register clash: it opens with formal terminology ('institution conducted a comprehensive financial audit') but abruptly descends into casual slang ('found out the accounts were totally messed up')."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Effective Writing** requires aligning Purpose, Audience, Register, Tone, and Cohesion.\n- **Formal Registers** eliminate contractions, avoid conversational slang, and deploy precise Latinate vocabulary.\n- **Tone** must remain objective, courteous, and constructive—even when communicating complaints or grievances."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Punctuation and Capitalization
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Punctuation and Capitalization",
        "unit_description": "Traffic signs of written language: capitalization rules, commas, semicolons, colons, apostrophes, and comma splice remediation.",
        "lesson_title": "Punctuation and Capitalization",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Handwritten Manuscript with Fountain Pen",
                    "content": {
                        "title": "Precision Punctuation and Calligraphic Clarity",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Handwriting_with_fountain_pen.jpg/800px-Handwriting_with_fountain_pen.jpg",
                        "caption": "A writer meticulously applying commas, semicolons, and capitalization rules to ensure unambiguous sentence boundaries and syntactical elegance.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Apply capitalization rules to proper nouns, proper adjectives, titles of works, and sentence beginnings\n- Deploy commas accurately to separate clauses, list items, and introductory adverbial elements\n- Use semicolons and colons to join related independent clauses and introduce structured lists\n- Differentiate possessive apostrophes (singular vs. plural) from contraction apostrophes"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Power of a Single Comma",
                    "content": {
                        "text": "Observe how a single punctuation mark transforms meaning entirely:\n\n> *Sentence A:* **\"Let's eat Grandpa!\"**\n> *Sentence B:* **\"Let's eat, Grandpa!\"**\n\n- In Sentence A, the lack of a comma turns 'Grandpa' into the direct object of the verb 'eat'—suggesting cannibalism!\n- In Sentence B, the comma correctly indicates direct address, politely inviting Grandpa to dinner.\n\nPunctuation marks are the vital traffic lights and road signs of written English. They dictate pacing, group thoughts, and prevent catastrophic misunderstandings."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Punctuation & Mechanics",
                    "content": {
                        "term": "Punctuation Marks & Capitalization Rules",
                        "definition": "**Punctuation** is the standardized system of symbols used to clarify meaning, separate syntactical units, and indicate pauses. **Capitalization** marks sentence beginnings, the pronoun 'I', proper nouns, proper adjectives, and major words in titles. A **Semicolon (;)** connects closely related independent clauses; a **Colon (:)** introduces lists, explanations, or quotes."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Punctuation Marks and Functional Rules",
                    "content": {
                        "headers": ["Symbol", "Name", "Primary Function", "Correct Model Sentence"],
                        "rows": [
                            [".", "Full Stop / Period", "Terminates declarative and imperative sentences", "The research team completed the environmental audit."],
                            [",", "Comma", "Separates items in lists, introductory clauses, and parenthetical elements", "Although the weather was harsh, we continued our fieldwork."],
                            [";", "Semicolon", "Joins independent clauses without coordinating conjunctions", "The experiment was successful; the results matched our hypothesis."],
                            [":", "Colon", "Introduces an enumeration, formal explanation, or block quote", "The kit contains three essentials: bandages, antiseptic, and sterile gauze."],
                            ["'", "Apostrophe", "Indicates possession or marks omitted letters in contractions", "The teacher's desk (singular) vs. The teachers' lounge (plural)."],
                            ["\" \"", "Quotation Marks", "Encloses exact spoken dialogue or direct textual citations", "\"Safety must remain our top priority,\" declared the director."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Punctuation & Capitalization Rules Map",
                    "content": {
                        "title": "Traffic Signs of Writing: Punctuation & Capitalization Rules",
                        "caption": "Comprehensive blueprint outlining capitalization rules, comma pause functions, semicolon clause linking, and apostrophe possession mechanics.",
                        "svg_content": SVG_LESSON_4_PUNCTUATION_CAPITALIZATION
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Resolving Comma Splices and Capitalization",
                    "content": {
                        "intro": "Analyze how punctuation and capitalization errors are methodically diagnosed and resolved:",
                        "steps": [
                            "**Flawed Sentence:** *'last friday i visited nairobi national park, the wildlife was breathtaking.'*",
                            "**Step 1: Capitalize Proper Nouns & Sentence Openers:** Capitalize 'Last', 'I', and 'Nairobi National Park'.",
                            "**Step 2: Diagnose the Comma Splice:** Joining two complete independent clauses (*'...national park'* and *'the wildlife was...'*) with only a comma creates a run-on error.",
                            "**Step 3: Apply Semicolon or Period:** Join with a semicolon followed by an organic connector, or separate into two distinct sentences.",
                            "**Polished Output:** *'**Last Friday**, **I** visited **Nairobi National Park**; the wildlife was breathtaking.'*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Punctuation and Capitalization Quiz",
                    "content": {
                        "title": "Interactive Punctuation and Mechanics Workshop",
                        "youtube_id": "uHStlZJimSc",
                        "url": "https://www.youtube.com/watch?v=uHStlZJimSc",
                        "description": "Video challenge testing comma placements, apostrophe usage, semicolon boundaries, and proper noun capitalization."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Editorial Proofreading Challenge",
                    "content": {
                        "title": "Punctuation Diagnostic in School Publications",
                        "text": "**Pre-Viewing Focus:** Pay special attention to how conjunctive adverbs (*however, therefore, consequently*) require a semicolon before them and a comma immediately after when linking independent clauses.\n\n**Post-Viewing Writing Challenge:** Punctuate and capitalize this unedited passage in your exercise books: *'on monday mr omondi said the kenyan athletes trained hard therefore they deserved their victory.'*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Punctuation Traps & Solutions",
                    "content": {
                        "text": "### Trap 1: The 'Greengrocer's Apostrophe' (Pluralizing with Apostrophes)\n- **Incorrect:** *\"The **student's** submitted their **essay's** on time.\"*\n- **Correct:** *\"The **students** submitted their **essays** on time.\"* *(Never use apostrophes to make standard nouns plural!).*\n\n### Trap 2: Semicolon Followed by a Capital Letter\n- **Incorrect:** *\"The storm passed; **However** damage remained.\"*\n- **Correct:** *\"The storm passed; **however,** damage remained.\"* *(Do not capitalize after a semicolon unless the word is a proper noun or 'I').*\n\n### Trap 3: Over-Capitalization of General Nouns\n- **Incorrect:** *\"We saw a **Cheetah** and a **Lion** in the **National Park**.\"*\n- **Correct:** *\"We saw a **cheetah** and a **lion** in the **national park**.\"* *(Only capitalize specific official titles: 'Nairobi National Park').*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Sentence Repair Workshop",
                    "content": {
                        "intro": "Execute precision punctuation and capitalization corrections:",
                        "steps": [
                            {"title": "Sentence 1: Possessive Apostrophe Placement", "description": "Draft: 'The (teachers/teacher's/teachers') staffroom was renovated last term.' Solution: Plural possessive = 'The **teachers\'** staffroom was renovated last term.'"},
                            {"title": "Sentence 2: Conjunctive Adverb Boundary", "description": "Draft: 'The laboratory was closed consequently we postponed the experiment.' Solution: 'The laboratory was closed**; consequently,** we postponed the experiment.'"},
                            {"title": "Sentence 3: Title of Work Capitalization", "description": "Draft: 'We read the book things fall apart by chinua achebe.' Solution: 'We read the book **_Things Fall Apart_** by **Chinua Achebe**.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Punctuation and Capitalization Mastery",
                    "content": {
                        "question": "Which of the following sentences exhibits flawless punctuation and capitalization?",
                        "options": [
                            "The Kenyan runners won gold medals, consequently, they were celebrated nationwide.",
                            "The Kenyan runners won gold medals; consequently, they were celebrated nationwide.",
                            "The kenyan runners won gold medals; consequently they were celebrated nationwide.",
                            "The Kenyan runners won gold medals: consequently, they were celebrated nationwide."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: 'Kenyan' is capitalized as a proper adjective, the semicolon connects two independent clauses, and 'consequently' is followed immediately by a comma. Option A is a comma splice; Option C fails to capitalize 'kenyan' and misses the comma after 'consequently'; Option D misuses a colon."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Apostrophe Usage Diagnostic",
                    "content": {
                        "question": "Select the sentence that uses apostrophes with 100% grammatical correctness:",
                        "options": [
                            "The students' books were stored in the teacher's cabinet, but its lock was broken.",
                            "The student's books were stored in the teachers cabinet, but it's lock was broken.",
                            "The students books were stored in the teacher's cabinet, but it's lock was broken.",
                            "The students' book's were stored in the teacher's cabinet, but its lock was broken."
                        ],
                        "correct_answer": 0,
                        "explanation": "Option A is correct: 'students\'' correctly marks plural possession; 'teacher\'s' marks singular possession; 'its' is the correct possessive determiner (without an apostrophe). Options B, C, and D contain erroneous contractions ('it\'s') or plural apostrophes ('book\'s')."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Punctuation** defines grammatical boundaries: master the semicolon + conjunctive adverb + comma pattern (*; consequently,*).\n- **Apostrophes** indicate either possession (*student's / students'*) or contractions (*it's = it is*)—never standard plurals.\n- **Capitalize** proper nouns, proper adjectives (*Kenyan, Swahili*), the pronoun 'I', and major title words."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: The Writing Process and Editing
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "The Writing Process and Editing",
        "unit_description": "The recursive writing workflow: prewriting, structured outlining, drafting, content revision, mechanical proofreading, and publishing.",
        "lesson_title": "The Writing Process and Editing",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Student Drafting and Revising in Study Notebook",
                    "content": {
                        "title": "The Step-by-Step Writing Pipeline",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Student_drafting_essay_notebook.jpg/800px-Student_drafting_essay_notebook.jpg",
                        "caption": "A Grade 10 student executing the recursive stages of writing—moving from brainstorm outlines to drafting, peer editing, and final manuscript publication.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Navigate the 5 recursive stages of writing: Planning, Drafting, Revising, Editing, and Publishing\n- Distinguish between substantive structural revision (ideas/organization) and mechanical editing (spelling/grammar)\n- Apply the standard Editorial Correction Code (SP, GR, P, WC, RO, CS) for peer review\n- Develop self-editing routines to elevate raw drafts into publication-ready manuscripts"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: Baking a Cake Without a Recipe",
                    "content": {
                        "text": "Imagine attempting to bake an intricate cake without measuring ingredients, checking the oven temperature, or tasting the batter. The outcome would likely be disastrous!\n\nSimilarly, trying to produce an academic essay in a single rushed session without prewriting (the recipe), drafting (mixing), revising (tasting and adjusting spices), and editing (frosting and decoration) yields chaotic results.\n\nWriting is not an instantaneous stroke of magic; it is a **recursive, multi-stage craft** where raw ideas are systematically refined into polished communication."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: The Writing Process",
                    "content": {
                        "term": "The 5-Stage Writing Pipeline & Editorial Coding",
                        "definition": "The **Writing Process** consists of: **1. Planning/Prewriting** (outlining, brain-mapping), **2. Drafting** (freely generating sentences), **3. Revising** (reorganizing content, strengthening thesis/evidence), **4. Editing/Proofreading** (fixing mechanical errors in spelling, grammar, punctuation), and **5. Publishing** (final formatting and distribution). It is *recursive*, meaning writers loop back between stages as ideas evolve."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Revising vs. Editing: The Crucial Distinction",
                    "content": {
                        "headers": ["Dimension", "Revising (Substantive / Macro-Level)", "Editing & Proofreading (Mechanical / Micro-Level)"],
                        "rows": [
                            ["Focus", "Ideas, thesis strength, logical organization, paragraph unity", "Spelling, punctuation, grammar, capitalization, formatting"],
                            ["Key Questions", "Is the thesis well-supported? Do paragraphs flow logically?", "Are words spelled correctly? Are there run-ons or comma splices?"],
                            ["Typical Actions", "Adding evidence, deleting off-topic paragraphs, restructuring", "Correcting homophones, fixing subject-verb agreement, inserting commas"],
                            ["Timing", "Stage 3 (Always performed BEFORE mechanical proofreading)", "Stage 4 (Performed once structure and arguments are finalized)"],
                            ["Analogy", "Remodeling the architectural walls and foundation of a house", "Polishing the windows and painting the trim"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Writing Process Pipeline Diagram",
                    "content": {
                        "title": "The Recursive Writing & Editing Pipeline",
                        "caption": "Flowchart visualizing the 5 stages of writing and the feedback loop between drafting, substantive revision, and mechanical proofreading.",
                        "svg_content": SVG_LESSON_5_WRITING_PROCESS_PIPELINE
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Applying the Editorial Correction Code",
                    "content": {
                        "intro": "Examine how standard editorial marks are applied to a raw student draft:",
                        "steps": [
                            "**Raw Draft with Marks:** *'Although [P] we were tired we continued our journey. Because [FRAG] we wanted to reach camp before sunset. The guide told us he knew the way, however [CS] he looked confused [SP].'*",
                            "**Editorial Annotations:**\n- `[P]` Misplaced comma after subordinating conjunction 'Although'.\n- `[FRAG]` 'Because we wanted...' is a dependent clause fragment.\n- `[CS]` 'way, however' creates a comma splice between two independent clauses.\n- `[SP]` Check ending mechanics.",
                            "**Polished Revision:** *'**Although we were tired, we** continued our journey **because** we wanted to reach the campsite before sunset. The guide told us that he knew the way**; however,** he looked confused.'*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "The Writing Process: Rhetoric and Composition",
                    "content": {
                        "title": "Navigating Prewriting, Drafting, Revising, and Proofreading",
                        "youtube_id": "wEe7WZnEj60",
                        "url": "https://www.youtube.com/watch?v=wEe7WZnEj60",
                        "description": "Comprehensive video guide explaining why drafting must be separated from editing and how to conduct substantive revision."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: The 4-Phase Process Portfolio",
                    "content": {
                        "title": "Developing an Authentic Writing Portfolio",
                        "text": "**Pre-Viewing Focus:** Observe why the presenter calls writing a *recursive process* and why trying to edit grammar while drafting paralyzes creativity.\n\n**Post-Viewing Writing Challenge:** Select the topic **'Environmental Conservation in Our Community'**. Execute: (1) A 3-point brainstorm outline (Plan), (2) A fast 4-sentence rough draft (Draft), (3) A revised version with enhanced evidence (Revise), and (4) A mechanically proofread final text (Edit)."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Writing Process Errors",
                    "content": {
                        "text": "### Error 1: The 'One-and-Done' Trap\n- **Flawed:** Drafting an essay 30 minutes before the deadline and submitting it without cooling-off time or proofreading.\n- **Repaired:** Allow at least 24 hours between drafting and revising. Read the text aloud to identify awkward syntax and missing words.\n\n### Error 2: Editing Before Revising\n- **Flawed:** Spending an hour fixing commas in a paragraph that ends up being completely deleted because it lacks relevance.\n- **Repaired:** Always finalize thesis support and structural organization (Revising) *before* checking mechanics (Editing).\n\n### Error 3: Ignoring Sentence Fragments\n- **Flawed:** *\"We arrived at the campsite. After driving for six hours on rough roads.\"*\n- **Repaired:** *\"We arrived at the campsite **after driving for six hours on rough roads**.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Editorial Code Diagnostic",
                    "content": {
                        "intro": "Decode the editorial markings and execute repairs:",
                        "steps": [
                            {"title": "Mark 1: [RO] (Run-on Sentence)", "description": "Draft: 'The whistle blew the game began.' Repair: Insert a semicolon or period: 'The whistle blew; the game began.'"},
                            {"title": "Mark 2: [WC] (Word Choice / Register)", "description": "Draft: 'The principal gave a super cool speech.' Repair: 'The principal delivered an **inspiring and eloquent address**.'"},
                            {"title": "Mark 3: [AGR] (Subject-Verb Agreement)", "description": "Draft: 'A collection of rare artifacts were displayed.' Repair: Subject is singular 'collection': 'A collection of rare artifacts **was** displayed.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Stages of the Writing Process",
                    "content": {
                        "question": "At which stage of the writing process should a writer focus on reorganizing body paragraphs, adding concrete evidence, and refining the thesis statement?",
                        "options": [
                            "Planning / Prewriting",
                            "Drafting",
                            "Revising",
                            "Proofreading / Editing"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: Revising is the substantive stage dedicated to evaluating content, argument flow, paragraph order, and evidence strength. Planning precedes writing; Drafting focuses on getting ideas down; Proofreading/Editing focuses on mechanics (spelling/punctuation)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Editorial Code Interpretation",
                    "content": {
                        "question": "A peer editor places the code '[CS]' between two clauses in your draft. What specific error did they identify?",
                        "options": [
                            "A capitalization error on a proper noun",
                            "A comma splice (two independent clauses joined only by a comma)",
                            "A missing concluding sentence",
                            "A word choice that violates formal register"
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: '[CS]' is the standard editorial correction code for a 'Comma Splice'—joining two complete independent clauses with a comma without an accompanying coordinating conjunction."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **The Writing Process** is recursive and structured: Plan -> Draft -> Revise -> Edit -> Publish.\n- **Revising** addresses macro-level content and organization; **Editing** polishes micro-level mechanics and spelling.\n- **The Editorial Code** (*SP, GR, P, WC, CS, RO*) enables objective, actionable peer and self-assessment."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Descriptive and Narrative Essays
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Descriptive and Narrative Essays",
        "unit_description": "Creative and expressive composition: sensory imagery, figurative devices, narrative plot architecture (Freytag's Pyramid), and 'show, don't tell'.",
        "lesson_title": "Descriptive and Narrative Essays",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Elephants in Amboseli National Park with Kilimanjaro",
                    "content": {
                        "title": "Vivid Landscape and Sensory Imagery",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Elephants_in_Amboseli_National_Park_with_Kilimanjaro.jpg/800px-Elephants_in_Amboseli_Park_with_Kilimanjaro.jpg",
                        "caption": "The Amboseli savannah with Mount Kilimanjaro in the background, providing rich sensory material (sight, sound, tactile atmosphere) for descriptive and narrative prose.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between descriptive essays (sensory focus) and narrative essays (sequential plot focus)\n- Incorporate the 5 sensory details (sight, sound, touch, smell, taste) and figurative imagery\n- Structure narrative essays using Freytag's Pyramid (Exposition, Rising Action, Climax, Falling Action, Resolution)\n- Apply the 'Show, Don't Tell' principle and maintain consistent verb tense throughout storytelling"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: Showing vs. Telling a Storm",
                    "content": {
                        "text": "Compare these two accounts of a sudden tropical thunderstorm:\n\n*   **Telling (Flat and Uninspired):**\n    > *\"It was raining very hard and the storm was scary. I heard thunder and felt frightened in my room.\"*\n\n*   **Showing (Sensory and Immersive):**\n    > *\"The howling wind rattled my windowpane as sheets of torrential rain drummed against the iron roof. Without warning, a blinding flash of lightning split the midnight sky, followed by a deafening crack of thunder that vibrated through the floorboards.\"*\n\nThe second passage captivates the reader because it appeals to multiple **senses** (sound of howling wind and drumming rain, sight of blinding lightning, tactile vibration of floorboards) and uses **dynamic action verbs**."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Creative Essay Genres",
                    "content": {
                        "term": "Descriptive vs. Narrative Essays & Freytag's Pyramid",
                        "definition": "A **Descriptive Essay** paints a vivid sensory picture of a person, place, object, or scene using imagery and figurative language. A **Narrative Essay** recounts a sequential story based on personal or imagined experience, structured around **Freytag's Pyramid** (Exposition, Rising Action, Climax, Falling Action, Resolution) and anchored by a central **narrative thesis/moral**."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Descriptive vs. Narrative Essay Framework",
                    "content": {
                        "headers": ["Feature", "Descriptive Essay", "Narrative Essay"],
                        "rows": [
                            ["Primary Focus", "Spatial or sensory immersion of a single subject/scene", "Chronological plot sequence with conflict and resolution"],
                            ["Organizational Structure", "Spatial order (top-to-bottom, near-to-far) or thematic impressions", "Freytag's Pyramid: Exposition -> Complication -> Climax -> Resolution"],
                            ["Core Devices", "Sensory diction (5 senses), similes, metaphors, personification", "Dialogue, pacing, character development, narrative tension"],
                            ["Thesis Function", "Dominant impression (the overall mood or essence of the subject)", "Narrative thesis (the underlying insight, epiphany, or moral lesson)"],
                            ["Tense Convention", "Present or past tense (kept strictly consistent)", "Past tense standard for recounted events"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Narrative and Descriptive Framework Diagram",
                    "content": {
                        "title": "Creative Writing Architecture: Descriptive & Narrative Framework",
                        "caption": "Visual dual-model showing sensory descriptive layering on the left and Freytag's narrative plot pyramid on the right.",
                        "svg_content": SVG_LESSON_6_NARRATIVE_DESCRIPTIVE_FRAMEWORK
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Plotting Freytag's Pyramid",
                    "content": {
                        "intro": "Analyze how an authentic narrative essay is structured across the 5 narrative phases:",
                        "steps": [
                            "**1. Exposition:** Setting the scene at Mount Longonot trailhead; introducing the hiking club and clear morning weather.",
                            "**2. Rising Action:** The trail steepens; sudden rain clouds gather; a team member slips and sprains an ankle near the crater rim.",
                            "**3. Climax (Highest Tension):** Darkness approaches as heavy fog rolls in; the team must decide whether to attempt descending in the dark or construct an emergency shelter.",
                            "**4. Falling Action:** Applying first aid, signaling with whistles, and safely guiding the injured hiker as rangers arrive with stretchers.",
                            "**5. Resolution & Narrative Thesis:** Safe return to base camp; the author reflects that true leadership emerges not during easy triumphs, but during moments of collective adversity."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Essay Writing: Narrative Essay",
                    "content": {
                        "title": "Mastering Plot Development, Dialogue, and Character Arc",
                        "youtube_id": "LAuok5Dx0qg",
                        "url": "https://www.youtube.com/watch?v=LAuok5Dx0qg",
                        "description": "Comprehensive video exploring narrative essay structure, writing captivating opening hooks, and developing authentic dialogue."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Sensory Description & Narrative Drafting",
                    "content": {
                        "title": "Creative Composition Workshop",
                        "text": "**Pre-Viewing Focus:** Pay attention to how the presenter distinguishes between an essay that simply lists sequential events (*'Then we did this, then we went there'*) and a true narrative with dramatic tension and sensory immersion.\n\n**Post-Viewing Writing Challenge:** Write a 150-word descriptive paragraph on the prompt **'Sunrise over the Great Rift Valley'**. Incorporate at least 3 sensory domains (visual color, morning sounds, crisp air temperature) and one metaphor."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Creative Essay Pitfalls",
                    "content": {
                        "text": "### Pitfall 1: Unintentional Tense Shifting\n- **Flawed:** *\"I **walked** through the forest path and suddenly I **see** a massive leopard staring at me.\"*\n- **Repaired:** *\"I **walked** through the forest path and suddenly I **saw** a massive leopard staring at me.\"* *(Maintain consistent past tense throughout narrative recounting).*\n\n### Pitfall 2: Overusing Vague Emotional Adjectives\n- **Flawed:** *\"The view was very nice, beautiful, and exciting.\"*\n- **Repaired:** *\"Emerald tea plantations stretched across the rolling hills beneath a tapestry of golden morning sunlight.\"*\n\n### Pitfall 3: Plot Without a Central Conflict or Climax\n- **Flawed:** Listing routine actions without any tension, challenge, or learning moment.\n- **Repaired:** Ensure every narrative incorporates an obstacle, a turning point (climax), and a clear insight."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: 'Show, Don't Tell' Transformation",
                    "content": {
                        "intro": "Transform these flat 'telling' statements into evocative 'showing' descriptions:",
                        "steps": [
                            {"title": "Item 1: Telling -> Showing (Fear)", "description": "Telling: 'He was extremely frightened.' Showing: 'His hands trembled, cold sweat beaded on his forehead, and his pulse raced like a trapped bird.'"},
                            {"title": "Item 2: Telling -> Showing (Heat)", "description": "Telling: 'The afternoon was hot.' Showing: 'Heat waves shimmered above the melting tarmac as the relentless midday sun scorched the dry savannah.'"},
                            {"title": "Item 3: Telling -> Showing (Silence)", "description": "Telling: 'The library was very quiet.' Showing: 'Dust motes drifted through the sunlit silence, broken only by the rhythmic rustle of turning pages.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: 'Show, Don't Tell' Evaluation",
                    "content": {
                        "question": "Which of the following excerpts represents the most effective application of the 'Show, Don't Tell' technique in descriptive prose?",
                        "options": [
                            "The old market was very busy, noisy, and crowded with a lot of people buying items.",
                            "I loved visiting the marketplace because it was such an exciting and energetic place to spend time.",
                            "The pungent aroma of roasting maize mingled with the din of shouting vendors bargaining over crates of ripe mangoes.",
                            "The marketplace is located in town and contains many stalls that sell various fresh fruits."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: it engages multiple senses (olfactory: 'pungent aroma of roasting maize', auditory: 'din of shouting vendors', visual: 'crates of ripe mangoes') without lazily telling the reader that the market was 'busy' or 'exciting'."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Narrative Arc Structure",
                    "content": {
                        "question": "In Freytag's Pyramid, which narrative phase represents the decisive turning point or peak moment of emotional/dramatic tension?",
                        "options": [
                            "Exposition",
                            "Rising Action",
                            "Climax",
                            "Resolution (Denouement)"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: the Climax is the turning point and pinnacle of dramatic tension where the central conflict reaches its peak and forces a decisive resolution."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 6 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Descriptive Writing** relies on rich sensory imagery and figurative language to immerse the reader in a scene.\n- **Narrative Essays** follow Freytag's Pyramid (*Exposition, Rising Action, Climax, Falling Action, Resolution*) with a clear narrative thesis.\n- **Show, Don't Tell** by replacing generic abstract adjectives (*nice, scary, busy*) with concrete sensory evidence and active verbs."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7: Letters of Complaint, Request, and Inquiry
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Letters of Complaint, Request, and Inquiry",
        "unit_description": "Functional business correspondence: formal block layout, salutations, RE: subject lines, polite assertiveness, and valediction rules.",
        "lesson_title": "Letters of Complaint, Request, and Inquiry",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Formal Business Letter on Writing Desk",
                    "content": {
                        "title": "Official Correspondence and Block Letter Layout",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Business_letter_writing_desk.jpg/800px-Business_letter_writing_desk.jpg",
                        "caption": "A formal business letter drafted according to standard block format, featuring sender and recipient address blocks, clear subject lines, and appropriate valedictions.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Format formal letters using standard Block Layout (sender address, date, recipient address, salutation, RE:, body, sign-off)\n- Distinguish between Letters of Complaint, Letters of Request, and Letters of Inquiry\n- Apply polite, assertive language and modal verbs (*could, would, may*) without emotional aggression\n- Pair salutations (*Dear Sir/Madam* vs. *Dear Mr. Omondi*) with correct valedictions (*Yours faithfully* vs. *Yours sincerely*)"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Defective Sports Equipment",
                    "content": {
                        "text": "Imagine your school sports club purchased 10 footballs, but 4 deflated within 15 minutes of first use. Consider two letters to the supplier:\n\n*   **Draft A (Emotional & Aggressive):**\n    > *\"Your balls are complete garbage! You cheated us and your store is terrible. Give us our money back immediately!\"*\n\n*   **Draft B (Professional & Factual):**\n    > *\"Dear Store Manager, I am writing on behalf of the Grade 10 Sports Committee to formally lodge a complaint regarding four defective match footballs purchased on 12th August (Invoice #4028). The items failed to retain air pressure during our initial session. We kindly request an immediate exchange or full refund.\"*\n\nDraft B is far more likely to achieve a swift refund because it provides **factual evidence**, maintains **polite assertiveness**, and follows **formal business conventions**."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Formal Correspondence",
                    "content": {
                        "term": "Block Layout, Salutation & Valediction Rules",
                        "definition": "In standard **Block Format**, all elements align to the left margin without paragraph indentation. The **Salutation** opens the letter (*Dear Sir/Madam* when name is unknown; *Dear Dr. Mutua* when named). The **Subject Line (RE:)** states the purpose in bold/caps. The **Valediction** closes the letter: use **'Yours faithfully'** for anonymous recipients and **'Yours sincerely'** for named recipients."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Functional Letter Types and Functional Structures",
                    "content": {
                        "headers": ["Letter Type", "Primary Purpose", "Key Body Paragraph Elements", "Appropriate Phrasing"],
                        "rows": [
                            ["Letter of Complaint", "Report a grievance, service defect, or product failure", "Para 1: Incident statement & invoice details\nPara 2: Exact defect description\nPara 3: Desired remedy (refund/replacement)", "I am writing to express my dissatisfaction with...\nI request a formal investigation..."],
                            ["Letter of Request", "Solicit assistance, resources, permissions, or sponsorship", "Para 1: Formal request statement\nPara 2: Justification and benefits\nPara 3: Call to action and gratitude", "We kindly request permission to...\nWe would be immensely grateful if..."],
                            ["Letter of Inquiry", "Seek specific information, catalog pricing, or clarifications", "Para 1: Background & reason for inquiry\nPara 2: Specific numbered queries\nPara 3: Timeline for response", "I am writing to inquire regarding the available packages...\nCould you kindly clarify whether..."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Formal Letter Anatomy Diagram",
                    "content": {
                        "title": "Anatomy of a Formal Business Letter",
                        "caption": "Complete structural blueprint of standard block letter layout, illustrating the 8 core components from sender address to signature block.",
                        "svg_content": SVG_LESSON_7_FORMAL_LETTER_ANATOMY
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Dissecting a Model Letter of Request",
                    "content": {
                        "intro": "Examine the component-by-component construction of this official request letter:",
                        "steps": [
                            "**1. Sender Address & Date:** Top left: *'The Environment Club, Uhuru High School, P.O. Box 40100, Kisumu. 28th August 2026.'*",
                            "**2. Recipient Address:** *'The County Director of Forestry, Ministry of Environment, P.O. Box 502, Kisumu.'*",
                            "**3. Salutation:** *'Dear Sir/Madam,'*",
                            "**4. Subject Line:** *'**RE: REQUEST FOR TREE SEEDLINGS FOR SCHOOL REFORESTATION PROJECT**'*",
                            "**5. Body (3 Paragraphs):** Opening purpose -> Project details (500 indigenous seedlings) -> Appreciation and timeline.",
                            "**6. Valediction & Signature:** *'Yours faithfully,'* -> [Signature] -> *'Brian Kiprop, Secretary, Environment Club'*."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "How To Write Complaint Letter with Sample and Explanation",
                    "content": {
                        "title": "Mastering the Tone and Structure of Complaint Letters",
                        "youtube_id": "189YRFLrC7o",
                        "url": "https://www.youtube.com/watch?v=189YRFLrC7o",
                        "description": "Video walkthrough demonstrating block formatting, evidence presentation, polite tone, and specific remedy formulation."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Drafting a Formal Letter of Inquiry",
                    "content": {
                        "title": "Institutional Correspondence Workshop",
                        "text": "**Pre-Viewing Focus:** Note the critical rule: A complaint letter must never sound insulting or abusive; it must remain strictly factual, unemotional, and clear regarding the requested resolution.\n\n**Post-Viewing Writing Challenge:** Draft a formal **Letter of Inquiry** to the Kenya National Library Service requesting information regarding mobile library visits for your sub-county school. Ensure 100% adherence to Block Layout and the Salutation-Valediction rule."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Formal Letter Pitfalls",
                    "content": {
                        "text": "### Pitfall 1: Mismatched Salutation and Valediction\n- **Incorrect:** Opening with *\"Dear Sir/Madam\"* and signing off with *\"Yours sincerely\"*.\n- **Correct:** *\"Dear Sir/Madam\"* -> **\"Yours faithfully\"**; *\"Dear Mr. Omondi\"* -> **\"Yours sincerely\"**.\n\n### Pitfall 2: Including the Sender's Name in the Address Block\n- **Incorrect:** Putting *\"John Doe, P.O. Box 123...\"* at the very top of the letter.\n- **Correct:** The top address block contains *only* the institution/address. The sender's name appears *only* beneath the final signature!\n\n### Pitfall 3: Vague or Missing Subject Line\n- **Incorrect:** *\"RE: Complaint\"* or *\"RE: Hello\"*.\n- **Correct:** *\"RE: COMPLAINT REGARDING DEFECTIVE LABORATORY GLASSWARE (INVOICE #9812)\"*."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Letter Alignment Diagnostic",
                    "content": {
                        "intro": "Resolve layout and tone errors in these correspondence scenarios:",
                        "steps": [
                            {"title": "Scenario 1: Salutation-Valediction Match", "description": "Salutation is 'Dear Ms. Achieng'. Required sign-off: 'Yours sincerely,' followed by signature and full name in block letters."},
                            {"title": "Scenario 2: Subject Line Optimization", "description": "Draft: 'RE: We need some help with sports day.' Optimization: 'RE: REQUEST FOR FIRST-AID VOLUNTEER SUPPORT DURING ANNUAL SPORTS DAY'."},
                            {"title": "Scenario 3: Tone Elevation", "description": "Draft: 'I want you to tell me how much the tickets cost.' Elevation: 'I would be grateful if you could kindly furnish us with the current ticket pricing schedule.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Salutation and Valediction Pairing",
                    "content": {
                        "question": "If you address a formal business letter to a specific recipient by surname, such as 'Dear Dr. Kariuki,', which valediction sign-off is mandatory?",
                        "options": [
                            "Yours faithfully,",
                            "Yours sincerely,",
                            "Warmest regards,",
                            "Yours truly,"
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: when the recipient's name is known and used in the salutation ('Dear Dr. Kariuki'), standard formal British/CBC convention dictates 'Yours sincerely,'. 'Yours faithfully,' is reserved strictly for anonymous salutations ('Dear Sir/Madam')."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Block Layout Mechanics",
                    "content": {
                        "question": "Which of the following statements regarding standard Block Format in formal letters is accurate?",
                        "options": [
                            "Paragraphs must be indented by five character spaces from the left margin.",
                            "The sender's full legal name must be written at the top of the sender's address block.",
                            "All text elements, headings, addresses, and sign-offs align flush with the left margin.",
                            "The subject line (RE:) should appear before the sender's address."
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: in standard modern block format, all elements (addresses, date, salutation, subject line, paragraphs, and valediction) align flush against the left margin with blank lines separating sections."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 7 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Block Layout** requires strict left-alignment with zero paragraph indentations.\n- **Salutation Pairing Rule:** *Dear Sir/Madam* -> *Yours faithfully*; *Dear [Name]* -> *Yours sincerely*.\n- **Tone in Functional Letters** must remain factual, respectful, and assertively solution-oriented."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8: Reports, Memos, and Emails
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Reports, Memos, and Emails",
        "unit_description": "Workplace and institutional formats: factual report architecture, internal memo headers, email etiquette, and digital attachments.",
        "lesson_title": "Reports, Memos, and Emails",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Working in Modern Computer Lab",
                    "content": {
                        "title": "Digital Communication and Workplace Documentation",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/African_Students_in_Computer_Lab.jpg/800px-African_Students_in_Computer_Lab.jpg",
                        "caption": "Students drafting structured investigative reports, internal memorandums, and professional emails in a modern school ICT facility.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Structure investigative/simple reports (Title, Introduction, Findings, Conclusion, Recommendations)\n- Format internal memorandums using standard header blocks (TO, FROM, DATE, SUBJECT)\n- Draft professional digital emails with descriptive subject lines, polite salutations, and clear attachment mentions\n- Maintain objective, third-person factual reporting in institutional communication"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The First-Aid Kit Safety Audit",
                    "content": {
                        "text": "Consider the difference between a casual chat message and a formal internal memo regarding a classroom safety audit:\n\n*   **Casual Message:**\n    > *\"Hey everyone, someone got hurt yesterday during sports, we gotta check the first aid box.\"*\n\n*   **Formal Institutional Memorandum:**\n    > **MEMORANDUM**\n    > **TO:** All Department Heads and Sports Coaches\n    > **FROM:** Chairperson, School Health & Safety Committee\n    > **DATE:** 28th August 2026\n    > **SUBJECT: MANDATORY FIRST-AID KIT INSPECTION & RESTOCKING**\n    > Following a minor injury during yesterday's training session, all faculty members are directed to inspect classroom first-aid kits by Friday, 4th September. Submit all supply requisition lists to the school nurse immediately.\n\nThe memo format provides instant clarity, administrative authority, and clear deadlines."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Reports, Memos & Emails",
                    "content": {
                        "term": "Simple Report, Memorandum (Memo) & Professional Email",
                        "definition": "A **Simple Report** is a factual, structured document presenting investigation results under numbered subheadings (*Findings, Recommendations*). A **Memorandum (Memo)** is a concise internal organizational notice featuring a four-part header block (*TO, FROM, DATE, SUBJECT*) without salutations or sign-offs. A **Professional Email** is formal digital correspondence featuring a descriptive subject line, polite greeting, body, and attachment references."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Structural Matrix: Reports vs. Memos vs. Emails",
                    "content": {
                        "headers": ["Document Type", "Primary Audience & Scope", "Standard Header / Opening", "Key Structural Sections", "Closing / Sign-off Protocol"],
                        "rows": [
                            ["Simple Report", "Committees, administrators, external stakeholders", "Title / Terms of Reference", "1. Introduction\n2. Methodology / Findings\n3. Conclusion\n4. Recommendations", "Compiler's Name, Title, and Date"],
                            ["Memorandum (Memo)", "Internal colleagues, staff, club members", "TO: ...\nFROM: ...\nDATE: ...\nSUBJECT: ...", "Concise message paragraphs (often bulleted for action points)", "No salutation or formal sign-off; ends after final sentence"],
                            ["Professional Email", "Internal or external professional contacts", "To: / Cc: / Subject Line\nDear Mr./Ms. [Name],", "Body paragraphs with explicit mention of attachments (*Please find attached...*)", "Sign-off (*Kind regards / Sincerely*), Full Name, Role"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Reports, Memos, and Emails Framework Diagram",
                    "content": {
                        "title": "Functional Triad: Reports, Memos & Professional Emails",
                        "caption": "Architectural breakdown comparing the structural layouts of simple reports, internal memos, and professional emails.",
                        "svg_content": SVG_LESSON_8_REPORTS_MEMOS_EMAILS
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Anatomy of a Simple Report",
                    "content": {
                        "intro": "Analyze the formal subheadings and objective style of this school library report:",
                        "steps": [
                            "**Title:** *REPORT ON THE CONDITION AND UTILIZATION OF GRADE 10 SCIENCE LABORATORY EQUIPMENT*",
                            "**1. Introduction:** *'This report investigates the current adequacy of physics and chemistry apparatus following increased enrollment in Senior Secondary.'*",
                            "**2. Findings:** *'An audit conducted on 20th August revealed: (a) 40% of microscopes require lens calibration; (b) Glassware supply is sufficient for 80 students; (c) Safety goggles are depleted.'*",
                            "**3. Conclusion:** *'While basic glassware is adequate, optical equipment and safety gear require immediate replenishment.'*",
                            "**4. Recommendations:** *'It is recommended that: (1) The Board of Management allocate KES 50,000 for optical servicing; (2) 50 pairs of protective goggles be procured prior to Term 3 exams.'*",
                            "**Sign-off:** *'Report compiled by: Mercy Chebet, Laboratory Prefect. Date: 28th August 2026.'*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Guidelines for Writing Email and Business Memos",
                    "content": {
                        "title": "Mastering Workplace Email Etiquette and Formatting",
                        "youtube_id": "wnF71PiMT9c",
                        "url": "https://www.youtube.com/watch?v=wnF71PiMT9c",
                        "description": "Video guide exploring descriptive subject line formulation, email salutations, professional body clarity, and attachment protocols."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Cross-Channel Communication",
                    "content": {
                        "title": "Administrative Writing Challenge",
                        "text": "**Pre-Viewing Focus:** Note the difference between a vague subject line (*'Help'* or *'Report'*) and an actionable, professional subject line (*'Submission of Grade 10 Science Laboratory Audit Report (PDF)'*).\n\n**Post-Viewing Writing Challenge:** Imagine you conducted an inspection of your school sports field. Write: (1) A 4-line **Memo header** notifying team captains of scheduled maintenance, and (2) A 3-sentence **Email** to your teacher attaching the full field inspection report."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Institutional Writing Flaws",
                    "content": {
                        "text": "### Flaw 1: Adding Salutations and Sign-offs to Memos\n- **Incorrect:** Writing *\"Dear All Coaches... Yours sincerely\"* inside an internal memo.\n- **Correct:** Memos rely entirely on the header block (*TO, FROM, DATE, SUBJECT*) and terminate immediately after the message.\n\n### Flaw 2: Uninformative / Blank Email Subject Lines\n- **Incorrect:** Subject: *(blank)* OR Subject: *\"Hey\"* OR Subject: *\"important\"*.\n- **Correct:** Subject: *\"Request for Clarification on Grade 10 Term Dates\"*.\n\n### Flaw 3: Subjective / Biased Language in Reports\n- **Incorrect:** *\"The cafeteria staff were terribly rude and made disgusting food.\"*\n- **Correct:** *\"Interviews with 50 students indicated dissatisfaction with meal portion sizes and service wait times.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Report & Email Optimization",
                    "content": {
                        "intro": "Perform structural and stylistic corrections on these functional documents:",
                        "steps": [
                            {"title": "Item 1: Memo Header Formatting", "description": "Format: TO: All Club Members | FROM: Club Patron | DATE: 28th August 2026 | SUBJECT: ANNUAL TREE PLANTING EXERCISE."},
                            {"title": "Item 2: Professional Attachment Phrasing", "description": "Replace 'See my file attached' with 'Please find attached the **Grade 10 Budget Requisition Report (PDF)** for your review and approval.'"},
                            {"title": "Item 3: Objective Finding Formulation", "description": "Convert 'Nobody likes the library books' into 'Survey data revealed that 72% of respondents requested updated reference materials in STEM subjects.'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Memorandum Header Rules",
                    "content": {
                        "question": "Which of the following elements is strictly OMITTED from a standard internal memorandum (memo)?",
                        "options": [
                            "The SUBJECT line identifying the memo's core theme",
                            "The TO and FROM header routing fields",
                            "A formal closing valediction (e.g., 'Yours sincerely,')",
                            "The DATE field indicating when the memo was issued"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: internal memorandums are concise administrative routing documents that do NOT include formal salutations (*Dear...*) or valedictions (*Yours sincerely*). Options A, B, and D are standard components of the 4-part memo header block."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Simple Report Section Identification",
                    "content": {
                        "question": "In a formal investigative report, under which specific section should the author present proposed actionable solutions to the problems uncovered?",
                        "options": [
                            "Terms of Reference",
                            "Methodology",
                            "Findings",
                            "Recommendations"
                        ],
                        "correct_answer": 3,
                        "explanation": "Option D is correct: the 'Recommendations' section is specifically dedicated to presenting proposed actionable steps and solutions derived from the factual evidence gathered in the 'Findings'."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 8 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Simple Reports** follow a 5-part architecture (*Title, Introduction, Findings, Conclusion, Recommendations*) with strict objective evidence.\n- **Memorandums (Memos)** utilize standard header blocks (*TO, FROM, DATE, SUBJECT*) without salutations or valedictions.\n- **Professional Emails** demand actionable subject lines and precise references to digital attachments."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 9: Meeting Notices, Agendas, and Minutes
    # =========================================================================
    {
        "unit_order": 9,
        "unit_name": "Meeting Notices, Agendas, and Minutes",
        "unit_description": "Institutional governance: convening meetings via formal notices, structured chronological agendas, objective minute recording, and action points.",
        "lesson_title": "Meeting Notices, Agendas, and Minutes",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Student Council Meeting in Progress",
                    "content": {
                        "title": "Democratic Deliberation and Governance Documentation",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Student_council_meeting.jpg/800px-Student_council_meeting.jpg",
                        "caption": "Student council representatives conducting an orderly meeting guided by an official notice and agenda, while the secretary records formal minutes.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 9 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Draft a formal Notice of Meeting specifying date, time, venue, and purpose\n- Formulate a chronological standard Agenda (Quorum, Minutes Confirmation, Matters Arising, Main Business, AOB, Adjournment)\n- Record objective, legally sound Minutes in the third person and past tense\n- Structure clear Action Points identifying responsible individuals and firm deadlines"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Chaotic Club Meeting",
                    "content": {
                        "text": "Imagine attending a school club meeting where nobody knows what is to be discussed, members talk over one another, no votes are counted, and no record is made. A week later, everyone disagrees on what was decided!\n\nNow imagine a meeting where members receive a clear **Notice and Agenda** three days in advance, the Chairperson guides discussion item-by-item, and the Secretary records concise **Minutes** with explicit **Action Points**.\n\nMeeting documentation ensures institutional memory, accountability, and smooth execution."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Meeting Governance",
                    "content": {
                        "term": "Notice, Agenda, Quorum, Motions & Minutes",
                        "definition": "A **Notice of Meeting** is a formal invitation issued in advance stating venue, date, time, and agenda. The **Agenda** is the ordered list of business items. A **Quorum** is the minimum number of members required to conduct valid business. A **Motion** is a formal proposal moved by a proposer and supported by a seconder. **Minutes** are the permanent, objective record of proceedings, resolutions, and action items."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Standard Chronological Agenda Architecture",
                    "content": {
                        "headers": ["Item Number", "Agenda Component", "Purpose & Procedure"],
                        "rows": [
                            ["Item 1", "Opening / Constitution of Meeting", "Chairperson calls meeting to order; verifies presence of a Quorum."],
                            ["Item 2", "Apologies for Absence", "Secretary records members who submitted valid written apologies."],
                            ["Item 3", "Reading & Confirmation of Previous Minutes", "Reviewing previous record; proposing and seconding accuracy; Chairperson signs."],
                            ["Item 4", "Matters Arising", "Updates on unfinished business or pending action points from previous meeting."],
                            ["Item 5", "Main Business (Substantive Agenda Items)", "Discussion of new business items listed specifically (e.g., *Budget, Sports Day*)."],
                            ["Item 6", "Any Other Business (AOB)", "Minor miscellaneous items raised with permission of the Chairperson."],
                            ["Item 7", "Date of Next Meeting & Adjournment", "Setting the next convening date; formal close of proceedings."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Meeting Governance and Minutes Architecture",
                    "content": {
                        "title": "Meeting Governance: Notice, Agenda & Minutes Lifecycle",
                        "caption": "Complete lifecycle diagram showing pre-meeting notices and agendas, during-meeting deliberation, and post-meeting minutes and action points.",
                        "svg_content": SVG_LESSON_9_MEETING_GOVERNANCE_MINUTES
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Anatomy of a Minutes Entry",
                    "content": {
                        "intro": "Examine how discussions and resolutions are professionally documented in meeting minutes:",
                        "steps": [
                            "**Heading:** *'MINUTES OF THE 3RD EXECUTIVE COMMITTEE MEETING OF THE UHURU HIGH SCHOOL JOURNALISM CLUB HELD IN ROOM 4 ON 28TH AUGUST 2026 AT 4:00 PM'*\n\n**Present / Apologies:** List of attendees and official apologies.",
                            "**Sample Minute (Min 14/26: Newsletter Publication):**\n- *Discussion:* Members reviewed cost estimates for printing the term newsletter.\n- *Resolution:* It was proposed by Brian Ochieng and seconded by Faith Mwangi that 200 copies be printed.\n- *Action Point:* **(Action: Treasurer to disburse funds by 4th September 2026)**.",
                            "**Language Analysis:** Note the strict use of third person ('It was proposed by...'), simple past tense ('reviewed', 'resolved'), and clear assignment of accountability."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Notice, Agenda & Minutes of Meeting: Structure and Example",
                    "content": {
                        "title": "Comprehensive Meeting Governance Workshop",
                        "youtube_id": "ZRokMlIQ9Cg",
                        "url": "https://www.youtube.com/watch?v=ZRokMlIQ9Cg",
                        "description": "Step-by-step video guide covering notice drafting, standard agenda order, minute writing conventions, and action tracking."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Drafting Meeting Governance Documents",
                    "content": {
                        "title": "Club Leadership Documentation Challenge",
                        "text": "**Pre-Viewing Focus:** Pay attention to why minutes must never record emotional arguments or direct hearsay dialogue (*'Mary shouted that Peter was wrong'*), but rather objective institutional summaries (*'Members deliberated on alternative procurement options'*).\n\n**Post-Viewing Writing Challenge:** You are the secretary of the Grade 10 Sports Committee. Draft: (1) A 3-sentence **Notice of Meeting** for a football tournament planning session, and (2) A sample **Minute entry** recording the decision to buy two new match balls with a specific action point."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Meeting Documentation Errors",
                    "content": {
                        "text": "### Error 1: Transcribing Verbatim Dialogue\n- **Flawed:** *\"Mr. Omondi said he hated the budget and Jane argued back for ten minutes.\"*\n- **Correct:** *\"The committee deliberated extensively on the proposed budgetary allocations, noting concerns regarding equipment expenditure.\"*\n\n### Error 2: Vague Action Points Without Ownership\n- **Flawed:** *\"It was agreed that somebody should buy the refreshments before Friday.\"*\n- **Correct:** *\"It was resolved that the Social Secretary would procure refreshments by Thursday, 3rd September (Action: Social Secretary).\"*\n\n### Error 3: First-Person Tense Shifting in Minutes\n- **Flawed:** *\"We discussed the upcoming elections and I suggested we change the voting day.\"*\n- **Correct:** *\"The committee discussed the upcoming elections. It was proposed that the voting date be rescheduled.\"*"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Minutes Formulation",
                    "content": {
                        "intro": "Convert informal meeting notes into formal secretarial minutes entries:",
                        "steps": [
                            {"title": "Note 1: Venue Change", "description": "Informal: 'We decided to move the meeting to the hall.' Minutes: 'It was resolved that subsequent committee meetings be convened in the Main Hall.'"},
                            {"title": "Note 2: Proposer & Seconder", "description": "Informal: 'David suggested buying chess sets and Mary agreed.' Minutes: 'It was proposed by David Kiprop and seconded by Mary Wanjiku that five chess sets be procured.'"},
                            {"title": "Note 3: Action Point Assignment", "description": "Minutes: 'The Equipment Prefect was mandated to obtain price quotations from suppliers by 1st September (Action: Equipment Prefect).'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Action Point Construction",
                    "content": {
                        "question": "Which of the following represents the most professional and accountable minutes entry for an action point?",
                        "options": [
                            "We agreed that the sports field needs to be cleaned up very soon by the team.",
                            "It was resolved that the Sports Secretary would organize the pitch marking by Friday, 4th September (Action: Sports Secretary).",
                            "The coach told the captain that he should mark the field whenever he finds free time.",
                            "Field marking was discussed and everyone thought it was a great idea to do it sometime this week."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: it uses formal passive phrasing ('It was resolved that...'), assigns clear personal responsibility ('Sports Secretary'), sets a firm deadline ('Friday, 4th September'), and appends a standard '(Action: ...)' tag."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Agenda Sequence Protocol",
                    "content": {
                        "question": "In a standard formal meeting agenda, which item immediately follows the reading and confirmation of the previous meeting's minutes?",
                        "options": [
                            "Any Other Business (AOB)",
                            "Matters Arising",
                            "Adjournment",
                            "Apologies for Absence"
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: 'Matters Arising' (reviewing actions and progress from the previous meeting) always directly follows the confirmation of the previous minutes. Apologies precede confirmation; AOB and Adjournment conclude the meeting."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 9 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **Meeting Notices** must clearly specify Date, Time, Venue, and Purpose.\n- **Agendas** adhere to a strict chronological progression from Quorum verification to Matters Arising, Main Business, and AOB.\n- **Minutes** are permanent legal records written in the **third person** and **past tense**, with explicit action points and deadlines."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 10: Integrated Writing Performance and Publication
    # =========================================================================
    {
        "unit_order": 10,
        "unit_name": "Integrated Writing Performance and Publication",
        "unit_description": "Capstone synthesis: writing portfolio curation, rubric-based evaluation, peer assessment, and professional publication formatting.",
        "lesson_title": "Integrated Writing Performance and Publication",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Graduation and Academic Achievement Celebration",
                    "content": {
                        "title": "Publishing and Showcasing Academic Portfolios",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/High_School_Graduation_and_Achievement.jpg/800px-High_School_Graduation_and_Achievement.jpg",
                        "caption": "Senior school students celebrating the completion and publication of their curated writing portfolios, demonstrating mastery across creative and functional genres.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 10 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Assemble and curate a comprehensive Grade 10 Writing Portfolio (creative essay + functional business document)\n- Evaluate writing against four standard CBC rubric dimensions (Content/Relevance, Organization/Cohesion, Language Use, Mechanics)\n- Conduct constructive peer reviews and apply editorial feedback systematically\n- Prepare and publish final polished manuscripts for school newsletters, anthologies, or digital publication"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Final Manuscript Publication",
                    "content": {
                        "text": "Consider how a professional book or magazine reaches the printing press:\n\nAn author never rushes their initial draft to print. Instead, the manuscript undergoes rigorous **peer review**, **editorial formatting**, **rubric cross-checking**, and **meticulous proofreading**.\n\nBy polishing your best creative essay (e.g., from Lesson 6) and your finest functional correspondence (e.g., from Lesson 7 or 8), you transition from an apprentice writer to a published author—ready to share your written voice with clarity, authority, and pride!"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Portfolio & Publication",
                    "content": {
                        "term": "Writing Portfolio, Rubric-Based Assessment & Publication",
                        "definition": "A **Writing Portfolio** is a curated collection of student compositions demonstrating growth, versatility, and mastery across diverse genres. **Rubric-Based Assessment** evaluates writing across four distinct dimensions: Content, Organization, Language, and Mechanics. **Publication** is the final presentation of error-free, formatted text to an authentic audience."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Four-Dimensional CBC Writing Assessment Rubric",
                    "content": {
                        "headers": ["Rubric Dimension", "Core Criteria", "Exemplary Performance (Level 4)", "Emerging Performance (Level 1)"],
                        "rows": [
                            ["1. Content & Relevance", "Prompt adherence, depth of thought, insightful thesis", "Fully addresses prompt with profound depth and original insight", "Superficial, off-topic, or fails to address core requirements"],
                            ["2. Organization & Cohesion", "Paragraph unity, logical ordering, seamless transitions", "Flawless paragraph architecture; organic signpost connectors", "Disorganized; lacking topic sentences; severe paragraph drift"],
                            ["3. Language & Vocabulary", "Register control, lexical range, figurative/precise diction", "Sophisticated vocabulary; precise collocations; perfect register", "Colloquial slang; monotone vocabulary; severe register clashes"],
                            ["4. Mechanics & Conventions", "Spelling, punctuation, capitalization, layout adherence", "Zero spelling/grammar errors; immaculate block layout/margins", "Pervasive spelling errors, comma splices, and faulty punctuation"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Integrated Portfolio & Publication Pipeline",
                    "content": {
                        "title": "Mastery Matrix: Integrated Writing Portfolio & Publication",
                        "caption": "Holistic capstone diagram mapping the 4-stage publication cycle from multi-genre curation to rubric evaluation and multi-channel publication.",
                        "svg_content": SVG_LESSON_10_INTEGRATED_PORTFOLIO_PUBLICATION
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structural Analysis: Rubric-Based Self-Assessment",
                    "content": {
                        "intro": "Examine how a student evaluates their own draft against the 4-dimensional rubric:",
                        "steps": [
                            "**Sample Text Excerpt:** *'The school security team [WC] completed their audit [GR]; consequently, the gates were locked and security was restored.'*",
                            "**Rubric Evaluation:**\n- *Dimension 1 (Content):* Score 4/4 — Fully addresses the security incident.\n- *Dimension 2 (Organization):* Score 4/4 — Smooth logical flow linked by semicolon + 'consequently'.\n- *Dimension 3 (Language/WC):* Score 3/4 — 'security team' could be elevated to 'security personnel'.\n- *Dimension 4 (Mechanics/GR):* Score 3/4 — 'team' is a collective noun requiring singular agreement ('its audit').",
                            "**Polished Output:** *'The school **security personnel** completed **its** audit; consequently, the gates were locked and safety was fully restored.'*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Writing Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Writing, Editing, and Proofreading Your Essay",
                    "content": {
                        "title": "Publication-Quality Essay Polishing and Proofreading",
                        "youtube_id": "vWQESpoQbnk",
                        "url": "https://www.youtube.com/watch?v=vWQESpoQbnk",
                        "description": "Video workshop exploring the final publication checklist, visual layout proofreading, and incorporating peer review feedback."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Writing Lab: Capstone Portfolio Publishing",
                    "content": {
                        "title": "The Final Publication Showcase",
                        "text": "**Pre-Viewing Focus:** Note the 'Three-Pass Proofreading Strategy': Pass 1 for formatting and margins; Pass 2 for sentence fluency and connectors; Pass 3 for micro-spelling and punctuation.\n\n**Post-Viewing Writing Challenge:** Assemble your **Grade 10 Topic 4 Writing Portfolio**. Include: (1) Your revised Descriptive/Narrative Essay from Lesson 6, (2) Your polished Formal Letter from Lesson 7, and (3) A 3-sentence self-reflection detailing the greatest writing skill you mastered during this topic."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Publication and Portfolio Errors",
                    "content": {
                        "text": "### Error 1: Neglecting Visual Layout and Formatting\n- **Flawed:** Submitting a formal letter or essay with uneven margins, messy handwriting, or missing document headings.\n- **Correct:** Adhere to clean standard formatting: left-aligned block layout, clear titles, neat paragraph spacing, and consistent font/ink.\n\n### Error 2: Treating Peer Review Defensively\n- **Flawed:** Resisting constructive peer criticism and refusing to modify flawed sentences.\n- **Correct:** Embrace peer feedback as an indispensable tool to detect 'writer blindness' and elevate quality.\n\n### Error 3: Incomplete Portfolios\n- **Flawed:** Submitting only one genre and failing to demonstrate versatility across functional and creative writing.\n- **Correct:** Ensure your portfolio showcases both creative narrative/descriptive depth and disciplined functional correspondence."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Comprehensive Peer Review Protocol",
                    "content": {
                        "intro": "Follow this structured 4-step peer review checklist:",
                        "steps": [
                            {"title": "Step 1: The First Read-Through (Content & Flow)", "description": "Read the entire manuscript aloud without stopping to check if the overall message is engaging, logical, and unified."},
                            {"title": "Step 2: Structural Verification (Paragraphs & Transitions)", "description": "Highlight topic sentences and check that transition words (*furthermore, consequently, however*) link ideas smoothly."},
                            {"title": "Step 3: Mechanical Scan (Editorial Coding)", "description": "Use the Editorial Code to flag spelling errors [SP], comma splices [CS], and informal vocabulary [WC]."},
                            {"title": "Step 4: Constructive Commendation & Recommendation", "description": "Provide two specific compliments on strong writing techniques and one actionable recommendation for improvement."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Rubric Dimension Discerning",
                    "content": {
                        "question": "When assessing an essay against a formal evaluation rubric, which dimension specifically measures the smooth logical linking of ideas, paragraph unity, and the effective use of transition signposts?",
                        "options": [
                            "Mechanics & Conventions",
                            "Content & Relevance",
                            "Organization & Cohesion",
                            "Language Use & Diction"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct: 'Organization & Cohesion' evaluates paragraph architecture, logical progression of thoughts, topic sentence focus, and transition markers. Content assesses thesis depth; Language assesses vocabulary/register; Mechanics assesses spelling/punctuation."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Effective Peer Review Practice",
                    "content": {
                        "question": "Which of the following represents the most effective and constructive peer review feedback for an academic essay?",
                        "options": [
                            "Your essay was great, I really liked everything about it.",
                            "Your second paragraph drifts into unrelated shoe prices; eliminating that sentence will strengthen your paragraph unity around cardiovascular wellness.",
                            "This essay is boring and you need to rewrite the entire thing.",
                            "Everything looks okay to me, you don't need to change anything."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct: it provides specific, constructive, and actionable feedback by identifying an exact flaw (paragraph drift in paragraph 2) and explaining how resolving it strengthens paragraph unity. Options A, C, and D are vague, unhelpful, or unconstructively harsh."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 4 Lesson 10 Summary & Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n- **A Writing Portfolio** synthesizes creative and functional genres to showcase comprehensive language mastery.\n- **Rubric Assessment** evaluates Content, Organization, Language, and Mechanics systematically.\n- **Publication** represents the culmination of the writing journey—presenting polished, error-free compositions to an authentic audience."
                    }
                }
            ]
        ]
    }
]
