"""
VLearn CBC Grade 9 English — Topic 2: Reading and Literature
Full Structured Lesson Card Definitions for Lessons 1 to 7
"""

from curriculum.cbc_grade9_english_topic2_svgs import (
    SVG_LESSON_1_FLUENCY_STRATEGIES,
    SVG_LESSON_2_SQ4R_NOTE_MAKING,
    SVG_LESSON_3_ORAL_LITERATURE,
    SVG_LESSON_4_POETRY_ANATOMY,
    SVG_LESSON_5_DRAMA_STRUCTURE_PLOT,
    SVG_LESSON_6_CHARACTERISATION_CONFLICT,
    SVG_LESSON_7_THEMES_AND_STYLE,
)

TOPIC_2_LESSONS_ALL = [
    # =========================================================================
    # LESSON 1 (Unit 1): Reading Fluency and Comprehension Strategies
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Reading Fluency and Comprehension Strategies",
        "unit_description": "Mastering oral reading accuracy, conversational pace, expressive prosody, phrase chunking, skimming for gist, scanning for specific facts, and ignore-unknown-word strategies.",
        "lesson_title": "Reading Fluency and Comprehension Strategies",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Junior School Student Reading Aloud Expressively",
                    "content": {
                        "title": "Expressive Oral Reading and Fluency Mastery",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/African_Girl_at_Work.jpg",
                        "caption": "A junior school learner practicing fluent oral reading, combining accurate pronunciation, natural pacing, and expressive prosody.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Read a variety of texts at an appropriate speed with natural phrasing and expressive prosody\n- Group words into meaningful syntactic phrases rather than reading word-by-word\n- Apply skimming to extract the main idea (gist) of a passage rapidly\n- Use scanning to locate specific factual details, dates, and numbers with high speed\n- Practice the ignore-unknown-word strategy to maintain comprehension flow without unnecessary pauses"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Analogy: The Bumpy Bicycle vs. Smooth Gliding",
                    "content": {
                        "text": "Imagine riding a bicycle along a smooth road. If you pedal once, slam on the brakes, pedal once, and brake again, your ride is choppy, exhausting, and very slow.\n\nNow compare these two ways of reading:\n\n- **Word-by-Word (Choppy):** *\"The... sun... was... setting... over... the... horizon.\"*\n- **Phrased (Smooth Glide):** *\"The sun was setting / over the horizon.\"*\n\nWhen you group words into meaningful **phrases**, your mind glides across sentences effortlessly. **Reading fluency** is the smooth ride of learning—it frees your brain from laboring over individual letters so you can focus entirely on understanding what you read."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Reading Fluency",
                    "content": {
                        "term": "Reading Fluency",
                        "definition": "The ability to read text accurately, quickly, and with appropriate expression (prosody) so that cognitive resources can be dedicated entirely to comprehension rather than word decoding."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Speed-Reading Strategies & Fluency Techniques",
                    "content": {
                        "headers": ["Strategy", "Action / Technique", "Primary Purpose", "When to Use"],
                        "rows": [
                            ["Phrase Reading", "Grouping 3 to 5 words into meaningful syntactic chunks.", "Eliminates robotic word-by-word halting; boosts speed.", "All general reading and comprehension tasks."],
                            ["Skimming", "Rapidly glancing over titles, headings, and topic sentences.", "Extracts the overall gist or main idea in seconds.", "Previewing a chapter or deciding if an article is relevant."],
                            ["Scanning", "Moving eyes quickly down the page hunting for keywords or numbers.", "Locates specific facts, dates, prices, or names.", "Answering specific exam questions or finding a bus schedule."],
                            ["Echo Reading", "Repeating a phrase immediately after a fluent reader performs it.", "Emulates correct pacing, pitch, and punctuation pauses.", "Practicing difficult literature or dramatic dialogue."],
                            ["Ignoring Unknown Words", "Continuing past difficult vocabulary using overall context.", "Maintains reading momentum and working memory flow.", "First pass reading of unfamiliar descriptive texts."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Fluency Triad & Common Misconceptions",
                    "content": {
                        "text": "True reading fluency is built on three equal pillars:\n\n1. **Accuracy:** Decoding words correctly without frequent mispronunciations.\n2. **Rate (Pacing):** Reading at a natural conversational speed (120–150 words per minute), neither dragging nor rushing.\n3. **Prosody (Expression):** Using vocal pitch modulation, volume changes, and punctuation pauses to communicate mood.\n\n> **Key Rule:** Fast reading does not equal fluent reading. Shouting words at breakneck speed without pauses or expression destroys comprehension."
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Reading Fluency & Speed Strategies Matrix",
                    "content": {
                        "title": "The Pillars of Reading Fluency and Speed Strategies",
                        "caption": "Architectural breakdown of Accuracy, Rate, Prosody, Skimming, Scanning, and Phrase Chunking.",
                        "svg_content": SVG_LESSON_1_FLUENCY_STRATEGIES
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Reading Analysis: Phrasing & Scanning Model",
                    "content": {
                        "intro": "Observe how an expert reader analyzes phrasing and scans for critical data in this passage on road safety:",
                        "steps": [
                            "**Original Passage:** *\"Kenyan national parks recorded 45,000 international tourists in 2025. Sibling James, the tourism director, confirmed that the average visitor spent five days exploring our diverse heritage sites.\"*",
                            "**Step 1: Phrase Boundary Chunking:** *[Kenyan national parks] / [recorded 45,000 international tourists] / [in 2025]. // [Sibling James, the tourism director,] / [confirmed that the average visitor] / [spent five days] / [exploring our diverse heritage sites].*",
                            "**Step 2: Scanning for Specific Details:**",
                            "- *Target 1 (Number of tourists):* Eye scans for digits → **45,000**",
                            "- *Target 2 (Year of report):* Eye scans for 4-digit date → **2025**",
                            "- *Target 3 (Average duration of stay):* Eye scans for time unit → **five days**",
                            "**Step 3: Synthesis:** Skimming tells us this text is about tourism statistics in Kenya; scanning extracts the exact numbers in less than 3 seconds."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Mastering Reading Fluency and Prosody",
                    "content": {
                        "title": "Phrasing, Pacing, and Expressive Reading",
                        "youtube_id": "i0cQu7vnDzs",
                        "url": "https://www.youtube.com/watch?v=i0cQu7vnDzs",
                        "description": "Educational masterclass demonstrating how syntactic phrase chunking and pitch variation dramatically enhance reading comprehension."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: 1-Minute Timed Fluency & Scanning Workshop",
                    "content": {
                        "title": "Active Oral Reading Practice",
                        "text": "**Activity 1: 1-Minute Phrasing Sprint**\nSet a timer for 60 seconds. Read the following passage aloud to a study partner. Focus on smooth phrasing without stopping for unknown words:\n\n*\"The ocean was calm and beautiful. Blue waves lapped gently against the white sandy shore. In the distance, a group of international tourists was boarding a wooden boat for a sea travel adventure. They were eager to observe coral reefs and marine wildlife.\"*\n\n**Activity 2: Rapid Scanning Drill**\nAsk your partner to name one keyword from the text (e.g. *'coral'*, *'wooden'*, *'waves'*). Scan the text and touch the word within 2 seconds."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Reading Pitfalls & How to Avoid Them",
                    "content": {
                        "text": "### Pitfall 1: The 'Dictionary Stumble' Trap\n- **Incorrect:** Stopping for two minutes in the middle of a sentence to look up a word like *'archipelago'* in a dictionary.\n- **Correction:** This breaks your comprehension train of thought. **Ignore the word**, finish the paragraph, and infer its meaning from the surrounding context.\n\n### Pitfall 2: The 'Speed-Demon' Fallacy\n- **Incorrect:** Reading at maximum possible speed without pausing at periods or modulating pitch.\n- **Correction:** Speed without expression is useless noise. Maintain a controlled, conversational tempo (120–150 WPM) and pause at punctuation."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: 3-Step Scanning Protocol",
                    "content": {
                        "intro": "Follow this 3-step protocol whenever you need to find specific facts in a long text:",
                        "steps": [
                            {"title": "Step 1: Identify Target Clue Types", "description": "Determine if you are looking for a number (e.g. 500), a capitalized proper noun (e.g. Nairobi), or a specific technical term (e.g. ecosystem)."},
                            {"title": "Step 2: Zigzag Eye Pattern", "description": "Glide your eyes in a smooth 'S' or 'Z' pattern down the center of the page without reading full sentences."},
                            {"title": "Step 3: Lock and Verify", "description": "Once your eyes hit the keyword or number, read the single sentence surrounding it to verify that it answers your question."}
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Reading Strategies in Action",
                    "content": {
                        "question": "You are preparing for an examination and have a 10-page report on consumer protection laws. You need to find the exact penalty fee for selling expired goods. Which reading strategy should you use first?",
                        "options": [
                            "Skimming through all 10 pages from start to finish to understand the history of consumer protection.",
                            "Scanning the pages rapidly, searching specifically for currency symbols ('KES' or 'shillings') and numbers.",
                            "Intensive reading of pages 1 to 3, analyzing every single word and looking up definitions in a dictionary.",
                            "Echo reading the summary section aloud with a classmate."
                        ],
                        "correct_answer": 1,
                        "explanation": "Scanning is the designated strategy for locating specific facts, numbers, dates, or symbols quickly without reading the entire text. Skimming gives only a general overview, intensive reading is too slow for locating a single isolated fact, and echo reading is an oral fluency exercise."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Pillars of Reading Fluency",
                    "content": {
                        "question": "Which of the following best describes the essential components of true reading fluency?",
                        "options": [
                            "Reading as fast as possible while ignoring all punctuation marks.",
                            "A balanced combination of decoding accuracy, conversational rate, and expressive prosody.",
                            "Stopping at every unfamiliar word to write its full dictionary definition in a notebook.",
                            "Reading silently without chunking words into grammatical phrases."
                        ],
                        "correct_answer": 1,
                        "explanation": "True reading fluency is defined by the triad of Accuracy (correct decoding), Rate (conversational pace), and Prosody (expressive phrasing, pitch, and punctuation pauses). Rushing or stopping excessively destroys comprehension."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 1 Summary: Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n\n- **Fluency Triad:** Reading fluency balances accuracy, pacing, and expressive prosody.\n- **Phrase Chunking:** Reading in syntactic groups frees working memory for comprehension.\n- **Skimming vs. Scanning:** Skim for the overall gist; scan for specific numbers, names, and facts.\n- **Ignore Unknown Words:** Maintain momentum by using context clues rather than stopping constantly."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2 (Unit 2): Visualising, Summarising, and Note-Making
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Visualising, Summarising, and Note-Making",
        "unit_description": "Developing sensory mental imagery during reading, writing concise one-sentence summaries, and mastering the SQ4R study note-making method (Survey, Question, Read, Recite, Relate, Review).",
        "lesson_title": "Visualising, Summarising, and Note-Making",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students in Library Making Structured Study Notes",
                    "content": {
                        "title": "Active Note-Making and Information Processing",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Students_in_classroom_Kenya.jpg/800px-Students_in_classroom_Kenya.jpg",
                        "caption": "Junior secondary students practicing active note-making and summarization during independent library study.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Create vivid mental images from descriptive sensory texts using sight, sound, smell, touch, and taste\n- Condense extended paragraphs into precise, one-sentence summaries in your own words\n- Apply the 6-step SQ4R method (Survey, Question, Read, Recite, Relate, Review) to study complex texts\n- Distinguish active note-making from passive verbatim copying"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Analogy: Packing Your Travel Bag",
                    "content": {
                        "text": "Imagine you are packing a bag for a three-day school trip. If you try to stuff your entire wardrobe into the bag, the zipper will break and the bag will burst.\n\nTo pack effectively, you select only the **essential clothes**, fold them neatly, and arrange them in order.\n\n**Summarizing and note-making** work the exact same way. When reading textbooks or media articles, trying to memorize every sentence overloads your brain. You must extract the core ideas, condense them into your own words, and organize them into neat, structured notes."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: The SQ4R Study Method",
                    "content": {
                        "term": "SQ4R Method",
                        "definition": "A systematic, 6-step study and note-making procedure—Survey, Question, Read, Recite, Relate, Review—that transforms passive reading into active, long-term cognitive retention."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The 6 Steps of the SQ4R Study Method",
                    "content": {
                        "headers": ["Step", "Action", "Cognitive Purpose", "Example from Media Lesson"],
                        "rows": [
                            ["1. Survey", "Preview titles, bold headings, diagrams, and summaries.", "Builds a mental roadmap before deep reading.", "Noticing title 'Impact of Social Media' and two subheadings."],
                            ["2. Question", "Turn headings into active questions (5W + H).", "Creates active curiosity and targeted focus.", "Converting 'Risks of Social Media' into 'What are the main risks?'"],
                            ["3. Read", "Read text actively to hunt for answers to questions.", "Engages deep comprehension and mental visualization.", "Reading to identify cyberbullying, screen addiction, sleep loss."],
                            ["4. Recite & Record", "Speak key points aloud in own words and write notes.", "Transfers temporary sensory input into working memory.", "Writing concise bullet notes: 'Causes sleep loss and distraction.'"],
                            ["5. Relate", "Connect new facts to personal life and prior knowledge.", "Anchors information into long-term memory schemes.", "Connecting screen addiction to one's own study habits."],
                            ["6. Review", "Periodically self-quiz over notes at spaced intervals.", "Prevents the forgetting curve and solidifies mastery.", "Reviewing bullet notes 24 hours and 7 days after reading."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Visualising Sensory Details in Descriptive Text",
                    "content": {
                        "text": "**Visualising** means creating movie-like pictures in your imagination as you read. Writers trigger this using the five senses:\n\n- **Sight:** *\"Golden sunlight shimmering over turquoise ocean waves.\"*\n- **Sound:** *\"The deafening roar of thunder and howling winds.\"*\n- **Smell & Taste:** *\"The sharp, salty tang of sea breeze and roasting maize.\"*\n- **Touch:** *\"The cold, stinging ocean spray splashing against the wooden deck.\"*\n\nEngaging all five senses makes reading immersive, memorable, and enjoyable."
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "SQ4R Note-Making Architecture",
                    "content": {
                        "title": "The SQ4R Active Study and Note-Making Cycle",
                        "caption": "Step-by-step visual diagram illustrating the 6 stages of SQ4R information processing.",
                        "svg_content": SVG_LESSON_2_SQ4R_NOTE_MAKING
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Model: Paragraph to 1-Sentence Summary & SQ4R Notes",
                    "content": {
                        "intro": "Examine how a learner processes an argumentative paragraph into SQ4R notes and a precision summary:",
                        "steps": [
                            "**Original Text:** *\"Social and mass media have transformed how we communicate. While they allow for instant global connectivity and let us share family news with siblings across counties, they also carry risks like cyberbullying, misinformation, and screen addiction that harms study habits.\"*",
                            "**Step 1: SQ4R Question:** *\"What are the positive and negative effects of social media?\"*",
                            "**Step 2: Bullet Notes (Recite & Record):**",
                            "- *Benefits:* Instant global communication; sharing news across long distances.",
                            "- *Drawbacks:* Cyberbullying, false information, study distractions, and screen addiction.",
                            "**Step 3: Omit Minor Details & Compress:** Remove specific examples (*'family news'*, *'across counties'*) to isolate the central thesis.",
                            "**Step 4: Precision 1-Sentence Summary:** *\"Although social media enables instantaneous global communication, it also introduces serious hazards including misinformation and screen addiction.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Active Note-Making and the SQ4R Strategy",
                    "content": {
                        "title": "How to Take Efficient Study Notes Using SQ4R",
                        "youtube_id": "0bfHg24r4x4",
                        "url": "https://www.youtube.com/watch?v=0bfHg24r4x4",
                        "description": "Step-by-step instructional guide showing how to use the SQ4R method to boost reading comprehension and exam revision efficiency."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Study Lab: Transforming a Travel Text into SQ4R Notes",
                    "content": {
                        "title": "Independent Study Workshop",
                        "text": "**Read the following excerpt on coastal tourism:**\n\n*\"Tourism is a major economic pillar for Kenya. International tourists spend money on hotel accommodations, local transport, and craft souvenirs, creating thousands of jobs. However, unregulated tourism can cause severe environmental damage, such as coral reef destruction and plastic waste on beaches.\"*\n\n**Your Task:**\n1. Formulate 1 SQ4R Question from the text.\n2. Write 2 bullet points of recorded notes.\n3. Write 1 single summary sentence connecting economic benefits to environmental protection."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Note-Making Pitfalls",
                    "content": {
                        "text": "### Pitfall 1: Verbatim Copying ('The Photocopy Fallacy')\n- **Incorrect:** Copying entire sentences word-for-word from the textbook into your notebook and calling it 'notes'.\n- **Correction:** Copying requires zero brain processing. True note-making requires **paraphrasing**—rephrasing core ideas in your own words with bullet points and abbreviations.\n\n### Pitfall 2: Skipping the Question Step\n- **Incorrect:** Jumping straight into reading without surveying or asking questions.\n- **Correction:** Without questions, your mind wanders passively. Generating questions primes your brain to actively search for answers."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: 3-Step 1-Sentence Summary Method",
                    "content": {
                        "intro": "Use these 3 steps to turn any paragraph into a powerful one-sentence summary:",
                        "steps": [
                            {"title": "Step 1: Identify Key Concepts", "description": "Highlight the main subject and the primary claim or conflict (e.g. sports improve physical health; reading improves mental imagination)."},
                            {"title": "Step 2: Strip Away Minor Details", "description": "Delete examples, statistics, descriptive adjectives, and repetitive words (e.g. remove 'football', 'cardiovascular muscles')."},
                            {"title": "Step 3: Combine with Connecting Words", "description": "Use transitional conjunctions (e.g. 'While', 'Although', 'Because', 'Therefore') to link the main ideas into a single coherent sentence."}
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: The SQ4R Sequence",
                    "content": {
                        "question": "A Grade 9 learner is studying an environmental science article. She has surveyed the text and turned the heading 'Threats to Marine Wildlife' into the question: 'What specific human activities threaten sea animals?' According to SQ4R, what is her immediate next step?",
                        "options": [
                            "Write a 200-word creative story about sea turtles.",
                            "Read the section actively to locate specific answers to her question.",
                            "Skip directly to the chapter review questions without reading.",
                            "Close the book and recite from memory."
                        ],
                        "correct_answer": 1,
                        "explanation": "In the SQ4R method, after formulating a Question (Q), the next sequential step is to Read (R1) actively to locate the answers to that question. Writing stories, skipping reading, or reciting prematurely skips vital cognitive steps."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Effective Summarization",
                    "content": {
                        "question": "Which of the following is the most accurate rule for writing an effective summary of an informational text?",
                        "options": [
                            "Copy every sentence verbatim to preserve the original author's exact style.",
                            "Include all minor examples, statistics, and personal opinions.",
                            "Condense the central thesis and main points into your own words while omitting minor details.",
                            "Double the length of the original text by adding external commentary."
                        ],
                        "correct_answer": 2,
                        "explanation": "An effective summary condenses the main points into the reader's own words while omitting minor details, statistics, and examples. Verbatim copying or adding external commentary violates summarization principles."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 2 Summary: Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n\n- **Visualising:** Generating sensory mental pictures deepens reading comprehension.\n- **Summarising:** Condensing paragraphs into precise one-sentence summaries isolates core concepts.\n- **SQ4R Power:** Surveying, Questioning, Reading, Reciting, Relating, and Reviewing locks knowledge into long-term memory.\n- **Active Notes:** Paraphrased bullet notes dramatically outperform passive word-for-word copying."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3 (Unit 3): Oral Literature: Riddles, Proverbs, and Tongue Twisters
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Oral Literature: Riddles, Proverbs, and Tongue Twisters",
        "unit_description": "Analyzing the characteristics, cultural functions, metaphorical meanings, and performance techniques of short oral literature forms in African cultural heritage.",
        "lesson_title": "Oral Literature: Riddles, Proverbs, and Tongue Twisters",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "African Storytelling Gathering Around Village Fire",
                    "content": {
                        "title": "Oral Literature Performance and Cultural Heritage",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Storytelling_in_Africa.jpg/800px-Storytelling_in_Africa.jpg",
                        "caption": "Community elders and youth engaged in interactive oral storytelling, sharing riddles, proverbs, and verbal traditions.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the core characteristics, structures, and cultural roles of riddles, proverbs, and tongue twisters\n- Interpret the deep metaphorical and symbolic meanings of traditional proverbs\n- Distinguish literal meaning from metaphorical wisdom in cultural sayings\n- Perform tongue twisters and riddles with clear articulation, correct pacing, and interactive engagement"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Hook: The Fireside Challenge",
                    "content": {
                        "text": "Imagine sitting around a warm fireside with family and community elders in the evening. An elder announces: *\"I have a riddle!\"* Everyone eagerly responds: *\"Let it come!\"*\n\nThe elder poses the puzzle: *\"I have no legs, but I travel across mountains and valleys without ever stopping. What am I?\"*\n\nYou pause, ponder, and shout: *\"A river!\"*\n\nLong before books and digital screens existed in Kenya, our ancestors used riddles, proverbs, and tongue twisters to sharpen young minds, teach moral values, train speech articulation, and entertain the community. These are the **short forms of oral literature**."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Short Forms of Oral Literature",
                    "content": {
                        "term": "Oral Literature (Short Forms)",
                        "definition": "Compact, spoken verbal art forms—including riddles, proverbs, and tongue twisters—transmitted orally across generations to instruct, entertain, cultivate speech agility, and preserve cultural philosophy."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Comparison of Short Oral Literature Genres",
                    "content": {
                        "headers": ["Genre", "Linguistic Structure", "Primary Cultural Function", "Performance Dynamics"],
                        "rows": [
                            ["Riddle (Kitendawili)", "Two-part puzzle with cryptic imagery (Challenge & Response).", "Stimulates creative thinking, keen observation, and wit.", "Competitive, playful game between challenger and audience; prize offered if unsolved."],
                            ["Proverb (Methali)", "Short, fixed, poetic saying packed with metaphor.", "Provides moral guidance, settles disputes, and teaches wisdom.", "Spoken solemnly by elders and leaders in speeches and discussions."],
                            ["Tongue Twister", "Phrases packed with rapid alliteration and similar consonants.", "Develops articulatory fluency, pronunciation clarity, and speech speed.", "Fast, repetitive individual recitation to test vocal agility."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Metaphorical Interpretation of Proverbs",
                    "content": {
                        "text": "A **proverb** is never meant to be taken literally. It uses physical objects as symbols for human behavior:\n\n- **Literal Symbol (Vehicle):** *\"A rolling stone gathers no moss.\"*\n- **Metaphorical Meaning (Tenor):** A person who constantly moves around without settling into a career or community will never build lasting relationships, stability, or wealth.\n\n- **Literal Symbol:** *\"One finger cannot kill a louse.\"*\n- **Metaphorical Meaning:** An individual working alone cannot solve massive community problems; success requires collective unity and teamwork."
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Short Forms of Oral Literature Matrix",
                    "content": {
                        "title": "The Triad of Short Forms: Riddles, Proverbs, and Tongue Twisters",
                        "caption": "Comparison of linguistic mechanics, cultural functions, and worked models for short oral literature genres.",
                        "svg_content": SVG_LESSON_3_ORAL_LITERATURE
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Analysis: Deconstructing a Proverb & Tongue Twister",
                    "content": {
                        "intro": "Analyze the linguistic mechanics and cultural application of these two oral forms:",
                        "steps": [
                            "**Proverb Analysis: 'Hurry, hurry has no blessing' (Haraka, haraka haina baraka)**",
                            "- *Step 1 (Literal Analysis):* Rushing frantically does not bring good fortune.",
                            "- *Step 2 (Metaphorical Translation):* Hasty, impulsive decision-making leads to avoidable errors, financial losses, or physical accidents.",
                            "- *Step 3 (Real-World Application):* Applied when advising drivers against speeding or cautioning students against rushing through exam questions without reading.",
                            "**Tongue Twister Articulation: 'She sells sea shells by the seashore'**",
                            "- *Phonetic Focus:* Trains the speaker to sharply differentiate between the alveolar fricative /s/ and the post-alveolar fricative /ʃ/.",
                            "- *Vocal Delivery:* Begin slowly with exaggerated lip and tongue placement; gradually accelerate tempo without slurring consonant sounds."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Oral Literature: Proverbs, Riddles, and Speech Articulation",
                    "content": {
                        "title": "Exploring African Oral Literature and Proverbs",
                        "youtube_id": "p6xYkG1yZ3E",
                        "url": "https://www.youtube.com/watch?v=p6xYkG1yZ3E",
                        "description": "Engaging cultural documentary examining how traditional African communities used riddles, proverbs, and oral performance to educate youth and preserve heritage."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Oral Literature Lab: Performance & Articulation Workshop",
                    "content": {
                        "title": "Classroom Performance Activities",
                        "text": "**Activity 1: Tongue Twister Agility Sprint**\nRecite this tongue twister three times consecutively at high speed without stumbling:\n\n*\"Peter Piper picked a peck of pickled peppers. If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?\"*\n\n**Activity 2: Cultural Proverb Matching**\nWith your study group, identify three local proverbs from your community and explain how each can be applied to promote honesty and teamwork in school clubs."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Pitfalls in Oral Literature",
                    "content": {
                        "text": "### Pitfall 1: Literal Interpretation Trap\n- **Incorrect:** Thinking the proverb *\"Do not put all your eggs in one basket\"* is advice exclusively for chicken farmers.\n- **Correction:** Metaphorically, 'eggs' represent your resources, investments, or plans. The proverb warns against risking everything on a single venture.\n\n### Pitfall 2: Sacrificing Clarity for Speed in Tongue Twisters\n- **Incorrect:** Reciting tongue twisters at maximum speed while slurring and blurring the consonant sounds.\n- **Correction:** The primary purpose is **speech articulation precision**. Precision must always precede speed."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: 3-Step Proverb Deconstruction",
                    "content": {
                        "intro": "Follow these 3 steps to unpack any proverb in reading or composition:",
                        "steps": [
                            {"title": "Step 1: Identify the Concrete Image", "description": "Pinpoint the physical objects, animals, or nature elements used in the saying (e.g. stones, chickens, rivers, fingers)."},
                            {"title": "Step 2: Identify the Natural Rule / Physical Action", "description": "Ask what happens in the physical world (e.g. rolling stones don't allow plant growth; unhatched eggs can break)."},
                            {"title": "Step 3: Transfer to Human Life & Society", "description": "Translate the physical principle into moral advice, interpersonal relationships, or character development."}
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Interpreting Proverb Metaphors",
                    "content": {
                        "question": "During a family discussion, your uncle notices two siblings quarreling over a minor spilled glass of water. He remarks: 'Do not make a mountain out of a molehill.' What is the metaphorical meaning of his proverb?",
                        "options": [
                            "You should avoid mountain climbing during the rainy season.",
                            "Do not build large architectural houses when money is scarce.",
                            "Do not exaggerate a small, minor inconvenience into a massive, dramatic crisis.",
                            "Children should let community elders resolve all household chores."
                        ],
                        "correct_answer": 2,
                        "explanation": "Metaphorically, a 'molehill' represents a tiny, insignificant issue, while a 'mountain' represents a huge crisis. The proverb cautions against overreacting and exaggerating minor problems. The other choices are literal or unrelated."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Functions of Oral Genres",
                    "content": {
                        "question": "What is the primary linguistic and pedagogical purpose of practicing tongue twisters?",
                        "options": [
                            "To teach the history of ancient kingdoms through narrative songs.",
                            "To train speech muscle coordination, articulatory precision, and vocal clarity.",
                            "To provide legal codes for punishing community wrongdoers.",
                            "To explain the geographical origins of river basins."
                        ],
                        "correct_answer": 1,
                        "explanation": "Tongue twisters feature repetitive, contrasting consonant sounds specifically engineered to exercise vocal muscles, sharpen phonetic articulation, and cultivate speech clarity."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 3 Summary: Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n\n- **Riddles:** Call-and-response puzzles that stimulate critical observation and intellectual wit.\n- **Proverbs:** Metaphorical gems of wisdom that provide timeless moral guidance and conflict resolution.\n- **Tongue Twisters:** Phonetic gymnastics that build articulatory clarity and vocal agility.\n- **Metaphorical Mastery:** Moving beyond literal objects to unlock deep human and cultural truths."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4 (Unit 4): Analysing Simple and Oral Poems
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Analysing Simple and Oral Poems",
        "unit_description": "Examining poetic structures, lines, stanzas, quatrains, rhyme schemes (AABB vs. ABAB), personification, figurative devices, and the distinction between author and persona.",
        "lesson_title": "Analysing Simple and Oral Poems",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "African Wildlife and Savannah Landscape",
                    "content": {
                        "title": "Poetry and the Beauty of Natural Imagery",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/African_Elephants_in_Amboseli.jpg/800px-African_Elephants_in_Amboseli.jpg",
                        "caption": "Majestic African elephants in Amboseli, inspiring rich poetic imagery, personification, and creative verse.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the structural components of poetry: lines, stanzas, and quatrains\n- Analyze end rhymes and code standard rhyme schemes (such as AABB and ABAB)\n- Identify and explain personification in nature and wildlife poems\n- Distinguish between the real-life author and the fictional poetic persona"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Analogy: The Decorated House",
                    "content": {
                        "text": "Think of a poem as a beautifully decorated house:\n\n- The **lines** are the individual bricks.\n- The **stanzas** are the distinct rooms in the house.\n- The **rhyme scheme** is the matching color pattern painted across the walls.\n\nJust as an architect organizes rooms to make a house elegant and balanced, a poet arranges lines, rhythms, and sounds to create music in the reader's mind."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Rhyme Scheme & Quatrain",
                    "content": {
                        "term": "Rhyme Scheme",
                        "definition": "The ordered pattern of rhyming sounds at the ends of poetic lines, represented by sequential letters of the alphabet (e.g. AABB, ABAB)."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Poetic Structures & Rhyme Patterns",
                    "content": {
                        "headers": ["Element / Pattern", "Structural Definition", "Rhyme Pattern Example", "Musical Effect"],
                        "rows": [
                            ["Line", "A single row of words within a poem.", "N/A", "Creates rhythmic pauses and meter."],
                            ["Stanza (Quatrain)", "A unified group of 4 poetic lines separated by white space.", "4-line stanza block", "Functions like a paragraph in prose."],
                            ["AABB (Couplets)", "Lines 1 & 2 rhyme together; lines 3 & 4 rhyme together.", "sand (A) / land (A), sky (B) / high (B)", "Punchy, fast-paced, memorable pairs."],
                            ["ABAB (Alternate)", "Lines 1 & 3 rhyme together; lines 2 & 4 rhyme together.", "rise (A) / skies (A), song (B) / long (B)", "Flowing, melodic, alternating cadence."],
                            ["Persona", "The invented character / speaker telling the poem.", "N/A", "Establishes perspective, mood, and tone."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Personification & The Persona Concept",
                    "content": {
                        "text": "Two core concepts elevate poetry analysis:\n\n1. **Personification:** A figure of speech where animals, natural forces, or inanimate objects are given human traits, emotions, or behaviors.\n   - *Example:* *\"The ancient mountain stood tall and proud, while the river giggled down the hill.\"* (Mountains cannot feel pride; rivers cannot giggle).\n\n2. **Persona vs. Author:** The **author** is the actual person who penned the words. The **persona** is the fictional voice speaking in the poem. An adult author can speak through the persona of a frightened bird, an ancient tree, or a young child."
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Poetry Anatomy and Rhyme Scheme Architecture",
                    "content": {
                        "title": "Poetic Structure, Rhyme Patterns, and Literary Devices",
                        "caption": "Detailed visual breakdown comparing AABB vs. ABAB rhyme schemes, personification, and the author-persona distinction.",
                        "svg_content": SVG_LESSON_4_POETRY_ANATOMY
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Model: Annotating an Environmental Quatrain",
                    "content": {
                        "intro": "Observe how to code rhyme schemes and annotate personification in this stanza:",
                        "steps": [
                            "**Poem Stanza:**\n*The wild elephant stood beneath the shade, (Line 1)*\n*He watched the tourists from his quiet tree. (Line 2)*\n*In silent beauty, the great forest played, (Line 3)*\n*A song of peace that set our spirits free. (Line 4)*",
                            "**Step 1: Code End Rhymes:**",
                            "- *shade* (Line 1) → Sound **A**",
                            "- *tree* (Line 2) → Sound **B**",
                            "- *played* (Line 3) → Rhymes with *shade* → Sound **A**",
                            "- *free* (Line 4) → Rhymes with *tree* → Sound **B**",
                            "- **Resulting Rhyme Scheme:** **ABAB** (Alternate Rhyme).",
                            "**Step 2: Identify Personification:**",
                            "- *'the great forest played a song of peace'* → A forest cannot play a musical instrument or song like a human musician.",
                            "**Step 3: Identify the Persona:**",
                            "- A wildlife visitor or tourist observing nature with deep awe and tranquility."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "How to Analyze Poetry: Structure and Devices",
                    "content": {
                        "title": "Poetry Analysis: Rhyme Scheme and Personification",
                        "youtube_id": "POO_8Y5HqgM",
                        "url": "https://www.youtube.com/watch?v=POO_8Y5HqgM",
                        "description": "Comprehensive tutorial demonstrating how to map rhyme schemes, identify figurative language, and interpret poetic tone."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Poetry Studio: Composing and Performing an ABAB Quatrain",
                    "content": {
                        "title": "Creative Composition Lab",
                        "text": "**Task:** In your exercise book, compose a single 4-line quatrain about Kenya's wildlife or landscapes adhering to these three rules:\n\n1. Use an **ABAB** alternate rhyme scheme.\n2. Include at least **one instance of personification** (e.g. whispering wind, dancing waves, weeping sky).\n3. Recite your quatrain to your study partner with clear prosody and rhythmic emphasis on the rhyming end words."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Poetry Analysis Pitfalls",
                    "content": {
                        "text": "### Pitfall 1: Confusing Persona with Author\n- **Incorrect:** Assuming that when a poem says *\"I carried my heavy ivory tusks through the savannah\"*, the human author has tusks.\n- **Correction:** The author created an animal **persona** to narrate the experience from an elephant's point of view.\n\n### Pitfall 2: Treating Poetry Like Prose\n- **Incorrect:** Ignoring line breaks and reading poetry continuously without pauses at stanza boundaries.\n- **Correction:** Line breaks and stanzas dictate rhythm and suspense. Always observe natural pauses at line ends."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Step-by-Step Rhyme Scheme Coding",
                    "content": {
                        "intro": "Follow these steps to determine the rhyme scheme of any poem on an exam:",
                        "steps": [
                            {"title": "Step 1: Circle the Final Word in Each Line", "description": "Highlight the very last word of every line in the stanza."},
                            {"title": "Step 2: Assign Alphabetical Letters by Sound", "description": "Assign 'A' to the first end-word. If line 2 rhymes with line 1, mark it 'A'; if it has a new sound, mark it 'B'."},
                            {"title": "Step 3: Compare Subsequent Lines", "description": "Check if line 3 rhymes with line 1 (A), line 2 (B), or introduces a new sound (C). Write out the final 4-letter sequence (e.g. AABB or ABAB)."}
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Rhyme Scheme & Personification",
                    "content": {
                        "question": "Read this quatrain:\n'The ocean swallowed up the shore,\nShe roared with fury, wild and free.\nSibling, let us explore once more,\nThis deep, mysterious, blue sea.'\nWhat is the rhyme scheme and what literary device is used in line 2?",
                        "options": [
                            "Rhyme Scheme: AABB; Hyperbole.",
                            "Rhyme Scheme: ABAB; Personification ('She roared with fury').",
                            "Rhyme Scheme: ABCB; Onomatopoeia.",
                            "Rhyme Scheme: ABAB; Simile."
                        ],
                        "correct_answer": 1,
                        "explanation": "The end words are shore (A), free (B), more (A), sea (B), creating an ABAB rhyme scheme. Calling the ocean 'She' and describing her as 'roaring with fury' gives human gender and emotion to a body of water, which is personification."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: The Poetic Persona",
                    "content": {
                        "question": "In literary analysis, what is the key distinction between the author of a poem and the persona?",
                        "options": [
                            "The author is always a character inside the story, while the persona prints the book.",
                            "The author is the actual biographical writer, whereas the persona is the fictional speaker invented to narrate the poem.",
                            "The persona is the title of the poem, while the author is the publisher.",
                            "There is no difference; the speaker in a poem is always the real-life author."
                        ],
                        "correct_answer": 1,
                        "explanation": "The author is the real-world individual who wrote the poem, while the persona is the fictional mask or invented speaker whose voice narrates the poem."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 4 Summary: Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n\n- **Poetic Architecture:** Poems are built from lines organized into stanzas and 4-line quatrains.\n- **Rhyme Schemes:** AABB pairs adjacent lines; ABAB alternates rhyming lines.\n- **Personification:** Animates natural elements with human emotions and physical actions.\n- **Persona:** The distinct fictional speaker through whose eyes the poem unfolds."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5 (Unit 5): Play Structure, Setting, and Plot
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Play Structure, Setting, and Plot",
        "unit_description": "Navigating dramatic script formatting (acts, scenes, character tags, stage directions), understanding the impact of setting, and tracing Freytag's 5-stage dramatic plot arc.",
        "lesson_title": "Play Structure, Setting, and Plot",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Junior Secondary Theatre Drama Performance",
                    "content": {
                        "title": "Dramatic Literature and Stage Performance",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Student_theatre_performance.jpg/800px-Student_theatre_performance.jpg",
                        "caption": "Junior secondary students staging a dramatic performance, bringing script dialogue, stage directions, and plot conflict to life.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the structural components of a play script: acts, scenes, character cues, and stage directions\n- Analyze how stage directions guide actors' movements, vocal tones, and physical interactions\n- Evaluate the role of setting (time and place) in establishing dramatic mood and conflict\n- Sequence and trace the 5 stages of dramatic plot: exposition, rising action, climax, falling action, and resolution"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Analogy: The Architect's Blueprint",
                    "content": {
                        "text": "When you read a storybook, the author describes everything in full paragraphs. But when you look at a play script, you see bold names, short lines of dialogue, and instructions in brackets:\n\n> **MARIA:** *(gently, holding a seedling)* Sibling James, hold this bucket.\n> **JAMES:** *(smiling)* Of course! Let's plant our tree here.\n\nA play script is like an **architect's blueprint for a building**. The writer doesn't tell a finished story; they provide the blueprint so actors, directors, and set designers know exactly where to stand, how to move, and what emotions to project on stage."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Stage Directions",
                    "content": {
                        "term": "Stage Directions",
                        "definition": "Instructions enclosed in brackets and italics within a dramatic script that guide actors' physical movements, facial expressions, vocal tone, and lighting/sound effects—never to be spoken aloud during a performance."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Dramatic Script Architecture",
                    "content": {
                        "headers": ["Component", "Script Formatting", "Primary Function", "Rule of Performance"],
                        "rows": [
                            ["Act", "Major header: ACT 1", "Major division of the play (like a book volume).", "Signals major shifts in time or narrative chapters."],
                            ["Scene", "Sub-header: SCENE 2", "Subdivision of an act taking place in one location/time.", "Lights dim or curtain closes between scene shifts."],
                            ["Character Tag", "BOLD ALL CAPS on left", "Identifies who is speaking the dialogue.", "Clarifies speaker turns without 'he said/she said'."],
                            ["Stage Directions", "*Italics in brackets ( )*", "Instructs actions, emotional tone, and stage movements.", "Performed physically; NEVER spoken aloud."],
                            ["Dialogue", "Regular font following name", "The actual spoken words exchanged on stage.", "Delivered with natural prosody and appropriate volume."],
                            ["Setting", "Descriptive scene intro", "Establishes physical location, time of day, and weather.", "Directs backdrop scenery and lighting setup."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Freytag's 5 Stages of Dramatic Plot Arc",
                    "content": {
                        "text": "Every well-structured dramatic plot follows a five-stage narrative arc:\n\n1. **Exposition:** Introduces the setting, main characters, and normal state of affairs.\n2. **Rising Action:** The core conflict or obstacle emerges, causing tension and complications to escalate.\n3. **Climax (The Peak):** The highest point of dramatic intensity and suspense—a decisive turning point.\n4. **Falling Action:** The consequences of the climax unfold; characters deal with the fallout.\n5. **Resolution (Denouement):** The central conflict is resolved, and a new normal or moral equilibrium is established."
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Dramatic Structure & Freytag's Plot Pyramid",
                    "content": {
                        "title": "Script Formatting Architecture and Narrative Plot Stages",
                        "caption": "Visual breakdown of script elements (Acts, Scenes, Directions) and the 5-stage Freytag Plot Pyramid.",
                        "svg_content": SVG_LESSON_5_DRAMA_STRUCTURE_PLOT
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Script Analysis: Extracting Setting and Directions",
                    "content": {
                        "intro": "Examine this dramatic scene on public transport safety and citizenship:",
                        "steps": [
                            "**Script Excerpt:**\n*ACT 1, SCENE 2: Inside a crowded local public bus. Heavy rain is pouring outside. (Setting)*\n**DRIVER:** *(shouting angrily over the roaring engine)* Move to the back of the bus!\n**PASSENGER:** *(gently, holding a wet umbrella)* Sibling, please slow down, the road is very slippery.",
                            "**Step 1: Setting Analysis:**",
                            "- *Physical Location:* Inside a crowded public transport bus.",
                            "- *Atmosphere / Weather:* Pouring rain and a slippery road, creating immediate danger and tension.",
                            "**Step 2: Stage Direction Deconstruction:**",
                            "- *(shouting angrily over the roaring engine)* → Tells the driver's actor to project a harsh, irritated vocal tone and compete with background engine noise.",
                            "- *(gently, holding a wet umbrella)* → Tells the passenger's actor to use a calm, polite posture and hold a prop.",
                            "**Step 3: Plot Stage:**",
                            "- This is **Rising Action**—the clash between the reckless driver and the safety-conscious passenger builds dramatic conflict."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Dramatic Structure: Script Format and Plot Arcs",
                    "content": {
                        "title": "Understanding Play Scripts and Dramatic Plot",
                        "youtube_id": "WH5jlkK4aUI",
                        "url": "https://www.youtube.com/watch?v=WH5jlkK4aUI",
                        "description": "Educational guide detailing script formatting conventions, interpreting stage directions, and navigating dramatic plot structure."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Drama Lab: Staging an Environmental Action Scene",
                    "content": {
                        "title": "Interactive Script Staging Workshop",
                        "text": "**Script Excerpt for Staging:**\n\n**SCENE 1: School garden stream. Morning.**\n**PETER:** *(gasping, wipes sweat from forehead)* Look at all this plastic waste choking the stream!\n**MARIA:** *(hands him gloves with an encouraging smile)* Let's clear the blockage before the rain starts.\n\n**Directions for Actors:**\n1. Actor playing Peter must physically wipe sweat and express genuine fatigue before speaking.\n2. Actor playing Maria must hand over real or mimed gloves while speaking warmly.\n3. Neither actor may read the bracketed words aloud."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Mistakes in Reading and Acting Plays",
                    "content": {
                        "text": "### Pitfall 1: Reading Stage Directions Aloud\n- **Incorrect:** An actor stepping onto the stage and saying aloud: *\"Gasping, wipes sweat from forehead, Look at all this plastic waste!\"*\n- **Correction:** Stage directions are **action prompts**, not spoken dialogue. You must act out the gasping and wiping, speaking only the actual dialogue words.\n\n### Pitfall 2: Confusing Setting with Dialogue\n- **Incorrect:** Thinking setting is just background decoration with no impact on the story.\n- **Correction:** Setting creates mood and fuels conflict. A stormy night on a slippery road immediately heightens danger and character anxiety."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Chronological Plot Sequencing",
                    "content": {
                        "intro": "Arrange these jumbled plot events into their proper 5-stage chronological order:",
                        "steps": [
                            {"title": "1. Exposition", "description": "Peter notices plastic waste accumulating along the school stream during morning leisure time."},
                            {"title": "2. Rising Action", "description": "Peter mobilizes his classmates, but heavy rain starts falling and some students want to quit."},
                            {"title": "3. Climax (Turning Point)", "description": "The stream overflows; Peter makes a courageous stand to secure the main drainage pipe despite the storm."},
                            {"title": "4. Falling Action", "description": "The stream clears, the flooding recedes, and the school grounds are saved from erosion."},
                            {"title": "5. Resolution", "description": "The principal honors the environment club, establishing a permanent school conservation policy."}
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Executing Stage Directions",
                    "content": {
                        "question": "A Grade 9 learner is reading a drama script and encounters this line:\n'MARIA: (excitedly, pointing at a nesting bird) Look! The eggs are hatching!'\nDuring the live school drama performance, how should the actor portray Maria?",
                        "options": [
                            "She must say aloud: 'excitedly, pointing at a nesting bird.'",
                            "She must stand motionless, fold her arms, and whisper the line in a monotone voice.",
                            "She must physically point toward the prop bird, project an excited facial expression, and speak only the dialogue words with energetic tone.",
                            "She should skip the line and let the next character speak."
                        ],
                        "correct_answer": 2,
                        "explanation": "Stage directions are physical and emotional instructions for the actor. Maria must perform the action (pointing excitedly) while speaking only the actual dialogue text. Stage directions must never be spoken aloud."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: The Climax of a Play",
                    "content": {
                        "question": "In Freytag's plot structure, which stage represents the decisive turning point of highest emotional intensity and conflict?",
                        "options": [
                            "The Exposition",
                            "The Climax",
                            "The Falling Action",
                            "The Setting Description"
                        ],
                        "correct_answer": 1,
                        "explanation": "The Climax is the pinnacle of the dramatic plot arc—the turning point of greatest intensity where the central conflict reaches its peak and forces a resolution."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 5 Summary: Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n\n- **Script Architecture:** Organized into Acts, Scenes, Character tags, and Stage directions.\n- **Stage Directions:** Physical and emotional cues for performance; never read aloud.\n- **Setting Power:** Establishes time, physical environment, and emotional atmosphere.\n- **5-Stage Plot:** Drives narrative from Exposition through Rising Action, Climax, Falling Action, to Resolution."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6 (Unit 6): Characterisation and Conflict
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Characterisation and Conflict",
        "unit_description": "Analyzing direct vs. indirect characterisation (the STEAL model), identifying protagonist vs. antagonist dynamics, and describing character traits and actions with rich adjectives and adverbs.",
        "lesson_title": "Characterisation and Conflict",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Youth Engaging in Expressive Debate and Dialogue",
                    "content": {
                        "title": "Character Traits and Interpersonal Conflict in Drama",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Youth_debate_discussion.jpg/800px-Youth_debate_discussion.jpg",
                        "caption": "Students practicing dynamic dramatic dialogue, illustrating contrasting character personalities, goals, and conflicts.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between direct and indirect characterisation techniques in dramatic texts\n- Apply the STEAL framework (Speech, Thoughts, Effect, Actions, Looks) to infer character traits\n- Identify protagonists, antagonists, and supporting characters in a play\n- Use precise adjectives and adverbs to describe character morals, motivations, and stage behaviors"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Analogy: Painting with Words and Deeds",
                    "content": {
                        "text": "Imagine an artist painting a portrait of an impatient person. The artist doesn't write the word *'IMPATIENT'* on the subject's forehead. Instead, they paint the person constantly glancing at their watch, tapping their foot rapidly, and frowning at a slow queue.\n\nIn dramatic literature, playwrights paint characters through their **words, body language, and reactions**. As an active reader and audience member, you look at these behavioral clues to deduce whether a character is honest, greedy, cowardly, or courageous."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Indirect Characterisation",
                    "content": {
                        "term": "Indirect Characterisation",
                        "definition": "The literary method of revealing a character's personality, values, and traits through what they say, do, think, look like, and how other characters react to them, requiring the audience to draw inferences."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Direct vs. Indirect Characterisation & Character Roles",
                    "content": {
                        "headers": ["Method / Role", "Definition & Mechanism", "Script Example", "Audience Task"],
                        "rows": [
                            ["Direct Characterisation", "The playwright explicitly declares a trait in text or directions.", "*(Peter, a greedy and dishonest trader, enters)*", "Accept fact directly; no inference required."],
                            ["Indirect Characterisation", "Traits are shown through dialogue, actions, and reactions (STEAL).", "'Take this bribe and shut your mouth!'", "Infer that the character is corrupt, deceitful, and manipulative."],
                            ["Protagonist", "The central character who drives the story and faces the core conflict.", "Sibling Mary asserting consumer rights calmly.", "Empathize with their struggle and values."],
                            ["Antagonist", "The opposing character or force creating obstacles for the protagonist.", "Corrupt shopkeeper refusing legitimate refunds.", "Analyze their negative traits and opposition."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The STEAL Character Inference Framework",
                    "content": {
                        "text": "When analyzing characters in plays, use the **STEAL** acronym:\n\n- **S — Speech:** What does the character say, and what tone do they use? (e.g. polite vs aggressive)\n- **T — Thoughts:** What do their private monologues reveal about their secret motives?\n- **E — Effect on Others:** How do other characters react when this person enters the room? (e.g. do they smile or cower in fear?)\n- **A — Actions:** What physical choices do they make under pressure?\n- **L — Looks:** What does their posture, clothing, and appearance signal about their lifestyle?"
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Characterisation Matrix & Dramatic Conflict Engine",
                    "content": {
                        "title": "Characterisation Methods and Protagonist vs. Antagonist Dynamics",
                        "caption": "Visual matrix showing Direct vs. Indirect Characterisation and the clash between Protagonists and Antagonists.",
                        "svg_content": SVG_LESSON_6_CHARACTERISATION_CONFLICT
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Model: Consumer Protection Dialogue Deconstruction",
                    "content": {
                        "intro": "Analyze how character traits and dramatic conflict are revealed in this consumer dispute:",
                        "steps": [
                            "**Script Excerpt:**\n**SHOPKEEPER:** *(slams counter, laughs dismissively)* Only fools expect things to work forever! Get out of my shop before I call security!\n**MARY:** *(takes a steady breath, presents her official receipt)* According to Consumer Protection Law Section 12, I am entitled to a refund for a defective radio. I will remain here quietly until you comply.",
                            "**Step 1: Analyze Shopkeeper (Antagonist):**",
                            "- *Action & Speech:* Slams counter, laughs dismissively, threatens security.",
                            "- *Trait Adjectives:* Aggressive, arrogant, deceitful, intimidating.",
                            "- *Adverbs of Action:* Acts *harshly*, speaks *rudely*.",
                            "**Step 2: Analyze Mary (Protagonist):**",
                            "- *Action & Speech:* Steady breath, presents documentation, cites legal consumer rights calmly.",
                            "- *Trait Adjectives:* Assertive, knowledgeable, courageous, disciplined.",
                            "- *Adverbs of Action:* Speaks *calmly*, acts *firmly*.",
                            "**Step 3: Nature of Conflict:** Consumer rights and integrity vs. fraudulent commercial exploitation."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Direct vs. Indirect Characterisation in Literature",
                    "content": {
                        "title": "Characterization: STEAL Method and Protagonist Dynamics",
                        "youtube_id": "sQzTssw6O58",
                        "url": "https://www.youtube.com/watch?v=sQzTssw6O58",
                        "description": "Engaging video tutorial breaking down how authors build complex, three-dimensional characters using the STEAL framework and dramatic conflict."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Drama Workshop: Building Three-Dimensional Characters",
                    "content": {
                        "title": "Character Design Workshop",
                        "text": "**Activity: The Lost Wallet Scenario**\nWrite a 6-line dialogue between two classmates who find a lost wallet containing KES 5,000 on the school playground:\n\n- **Character A (Honest Protagonist):** Wants to hand the wallet to the deputy principal immediately.\n- **Character B (Tempted Antagonist):** Wants to split the cash and hide the wallet.\n\nUse stage directions and dialogue clues (STEAL) to reveal Character A's integrity and Character B's rationalization without writing the words 'honest' or 'greedy'."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Characterisation Pitfalls",
                    "content": {
                        "text": "### Pitfall 1: Confusing Assertiveness with Aggressiveness\n- **Misconception:** Thinking that because a protagonist stands firm, they are being rude or aggressive.\n- **Clarification:** **Assertiveness** means standing up for rights calmly, respectfully, and clearly. **Aggressiveness** involves shouting, insults, and physical intimidation.\n\n### Pitfall 2: One-Dimensional 'Flat' Characters\n- **Misconception:** Believing protagonists never feel fear or make mistakes.\n- **Clarification:** Great drama features realistic characters with genuine human doubts, fears, and growth."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: 3-Step Character Trait Inference",
                    "content": {
                        "intro": "Use these 3 steps to extract precise character traits from script excerpts:",
                        "steps": [
                            {"title": "Step 1: Highlight Actions and Dialogue Cues", "description": "Identify specific verbs and tone markers in the character's speech and stage directions."},
                            {"title": "Step 2: Ask 'Why did they do that?'", "description": "Determine the underlying motive behind the action (e.g. self-preservation, greed, justice, compassion)."},
                            {"title": "Step 3: Assign Specific Adjectives", "description": "Select descriptive vocabulary (e.g. 'assertive', 'empathetic', 'evasive') rather than generic words like 'good' or 'bad'."}
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Inferring Character Traits",
                    "content": {
                        "question": "In a school play, Sibling John finds an examination paper left on the teacher's desk. In stage directions, John *(hesitates, looks at the door, then firmly places the paper inside the teacher's locked drawer)*. What trait is John demonstrating?",
                        "options": [
                            "Cowardice and confusion.",
                            "Integrity and moral responsibility.",
                            "Dishonesty and arrogance.",
                            "Timidness and indifference."
                        ],
                        "correct_answer": 1,
                        "explanation": "John's choice to overcome temptation and secure the examination paper in the teacher's drawer demonstrates integrity, self-discipline, and moral responsibility."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Indirect Characterisation via STEAL",
                    "content": {
                        "question": "Which of the following is an example of INDIRECT characterisation?",
                        "options": [
                            "The narrator states: 'Peter was an extremely greedy merchant.'",
                            "The stage direction reads: 'Scene 1 opens on Peter, a cruel man.'",
                            "Peter snatches the last loaf of bread from a hungry child and hides it in his coat.",
                            "The character description list reads: 'Peter — antagonist, selfish.'"
                        ],
                        "correct_answer": 2,
                        "explanation": "Peter snatching bread from a hungry child is an action (A in STEAL) that allows the audience to infer his selfishness indirectly. The other choices are direct statements made by the author or narrator."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 6 Summary: Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n\n- **Direct vs. Indirect:** Direct characterisation tells; indirect characterisation shows through actions, words, and effects (STEAL).\n- **Protagonist vs. Antagonist:** Protagonists drive noble goals; antagonists create obstacles and dramatic tension.\n- **Assertiveness vs. Aggression:** Assertive characters uphold rights with calm dignity; aggressive characters use force and insults.\n- **Precise Vocabulary:** Rich adjectives and adverbs capture nuanced moral motivations."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7 (Unit 7): Themes, Style, and Lessons Learnt
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Themes, Style, and Lessons Learnt",
        "unit_description": "Extracting universal themes, analyzing dramatic stylistic devices (monologue, flashback, humour), and relating literary lessons to modern community life.",
        "lesson_title": "Themes, Style, and Lessons Learnt",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Kenyan Students Reflecting on Literature in Classroom",
                    "content": {
                        "title": "Literary Themes, Stylistic Devices, and Life Lessons",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/School_children_reading_in_Kenya.jpg/800px-School_children_reading_in_Kenya.jpg",
                        "caption": "Students analyzing dramatic themes, evaluating characters' moral dilemmas, and connecting literature to community ethics.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Formulate central universal themes from dramatic scripts and literary texts\n- Distinguish a thematic statement from a simple plot summary\n- Analyze the functions of key dramatic stylistic devices: monologue, flashback, and humour\n- Connect the moral lessons learnt from dramatic literature to real-world community challenges"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Analogy: The Sweet Fruit and the Seed",
                    "content": {
                        "text": "Think of a great play as a sweet fruit:\n\n- The **plot** is the sweet, juicy flesh that you chew for immediate entertainment.\n- The **theme and lessons** are the nutrient-dense seed inside that stays with you long after the fruit is eaten.\n- The **stylistic devices** (humour, monologues, flashbacks) are the beautiful presentation of the fruit that makes it irresistible to taste.\n\nLiterature is a mirror of society. When you finish reading a drama, the true measure of your understanding is extracting the moral wisdom that guides your daily life."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Dramatic Monologue",
                    "content": {
                        "term": "Dramatic Monologue",
                        "definition": "An extended speech delivered by a single character alone on stage that exposes their innermost thoughts, moral conflicts, guilt, and motivations directly to the audience."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Stylistic Devices in Dramatic Literature",
                    "content": {
                        "headers": ["Stylistic Device", "Dramatic Mechanism", "Primary Function", "Example in Play"],
                        "rows": [
                            ["Monologue", "Character speaks alone on stage at length.", "Unveils deep internal moral conflict and conscience.", "Peter debating whether to report his cousin's reckless driving."],
                            ["Flashback", "Chronological flow halts; past scene is re-enacted.", "Explains character backstory and deep motivations.", "James remembering his grandmother's advice about education."],
                            ["Humour (Satire)", "Amusing dialogue, comic irony, or physical comedy.", "Relieves tension while gently mocking societal vices.", "Mocking a corrupt official demanding bribes for basic public services."],
                            ["Dramatic Irony", "Audience knows a secret that characters on stage do not.", "Heightens suspense, anticipation, and emotional investment.", "Audience seeing the hidden will while greedy relatives search for it."]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Distinguishing Theme from Plot Summary",
                    "content": {
                        "text": "A common student error is confusing what happens (plot) with what the story means (theme):\n\n- **Plot Summary (What happens):** *\"James worked hard on his farm during vacation and saved money to buy textbooks for his siblings.\"*\n- **Universal Theme (What it means):** *\"Integrity, industrious work ethic, and family solidarity are vital foundations for personal and community advancement.\"*\n\nA theme is always expressed as a **broad, universal statement** about human nature and society."
                    }
                }
            ],
            # Page 3: Model & Structured Analysis
            [
                {
                    "type": "suggested_diagram",
                    "title": "Themes, Stylistic Devices & Life Lessons Architecture",
                    "content": {
                        "title": "Dramatic Themes, Stylistic Devices, and Universal Moral Lessons",
                        "caption": "Visual architecture illustrating the three pillars: Monologue, Flashback, and Humour leading to universal themes.",
                        "svg_content": SVG_LESSON_7_THEMES_AND_STYLE
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Model: Deconstructing a Dramatic Monologue",
                    "content": {
                        "intro": "Examine this dramatic monologue on academic integrity and civic conscience:",
                        "steps": [
                            "**Monologue Excerpt:**\n**PETER:** *(alone on stage, clutching a stolen exam paper; dim blue spotlight)* \"If I use this paper tomorrow, I will score an A. My parents will be proud, and James will look like a fool for burning the midnight oil. But... what will I see when I look in the mirror? A fraudulent cheat. Peter, you are worth more than a stolen grade!\" *(throws paper into brazier)*",
                            "**Step 1: Identify the Stylistic Device:**",
                            "- Peter is alone under a spotlight sharing his internal thoughts → **Dramatic Monologue**.",
                            "**Step 2: Trace the Internal Conflict:**",
                            "- The temptation of unearned glory vs. personal self-respect and integrity.",
                            "**Step 3: Formulate the Universal Theme:**",
                            "- *\"True success and honor cannot be achieved through deception; authentic self-respect requires unwavering integrity.\"*",
                            "**Step 4: Extract the Practical Lesson Learnt:**",
                            "- Shortcuts in school or career corrupt one's conscience and destroy trust; ethical hard work is the only sustainable path to honor."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Active Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Identifying Themes and Literary Style in Drama",
                    "content": {
                        "title": "Themes, Flashbacks, and Dramatic Style",
                        "youtube_id": "p4qME64SkxM",
                        "url": "https://www.youtube.com/watch?v=p4qME64SkxM",
                        "description": "Educational masterclass teaching students how to identify central themes, interpret flashbacks, and connect literary devices to the author's message."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Literature Workshop: Connecting Set-Play Themes to Kenyan Society",
                    "content": {
                        "title": "Theme Application Workshop",
                        "text": "**Reflect on the theme of Road Safety and Civic Duty:**\n\nIn our class reader, Peter faces the dilemma of reporting a reckless bus driver who is also a close family relative.\n\n**Discussion Questions:**\n1. How does this dilemma mirror real-world road safety issues in our counties?\n2. Why is protecting innocent public passengers more important than covering up a relative's lawbreaking?\n3. Write a 3-sentence statement summarizing the civic duty of Kenyan youth when witnessing corruption or road violations."
                    }
                }
            ],
            # Page 5: Pitfalls & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Pitfalls in Theme and Style Analysis",
                    "content": {
                        "text": "### Pitfall 1: Stating a One-Word Topic instead of a Theme\n- **Incorrect:** Writing *\"The theme is honesty\"* or *\"The theme is money.\"*\n- **Correction:** A single word is a **topic**, not a theme. A theme must be a full, complete assertion (e.g. *\"Honesty builds community trust, while greed inevitably brings ruin.\"*)\n\n### Pitfall 2: Misunderstanding Humour in Drama\n- **Incorrect:** Assuming humour is only present to make people laugh like a clown show.\n- **Correction:** In serious literature, humour and satire are used to expose foolishness, critique corruption politely, and provoke deep reflection."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: 4-Step Method for Formulating a Theme Statement",
                    "content": {
                        "intro": "Follow these 4 steps to craft an outstanding theme analysis for any literary text:",
                        "steps": [
                            {"title": "Step 1: Identify the Central Big Idea (Topic)", "description": "Choose the core concept explored (e.g. justice, greed, forgiveness, citizenship)."},
                            {"title": "Step 2: Analyze What the Characters Do", "description": "Examine what choices the protagonist and antagonist made regarding this topic."},
                            {"title": "Step 3: Analyze the Consequences", "description": "What were the results of their choices? Did dishonesty lead to disgrace? Did courage bring freedom?"},
                            {"title": "Step 4: Craft a Universal Assertion", "description": "Write a complete sentence stating what the author believes about this human experience."}
                        ]
                    }
                }
            ],
            # Page 6: Formative Assessment & Synthesis
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Analyzing Dramatic Devices",
                    "content": {
                        "question": "In a play about road safety, Peter delivers a monologue where he says: 'He is my beloved cousin... but if I keep silent, innocent school children might lose their lives tomorrow.' What is the primary function of this monologue?",
                        "options": [
                            "To demonstrate Peter's physical fitness to the audience.",
                            "To reveal Peter's agonizing internal conflict between family loyalty and civic responsibility.",
                            "To describe the rainy weather conditions of the highway.",
                            "To provide comic relief and entertain the crowd with laughter."
                        ],
                        "correct_answer": 1,
                        "explanation": "The monologue allows the audience to directly witness Peter's internal ethical struggle between his personal loyalty to his relative and his higher moral duty to protect human lives and uphold civic safety."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Formulating Theme Statements",
                    "content": {
                        "question": "Which of the following represents a properly formulated universal theme statement?",
                        "options": [
                            "The play is about Peter and his cousin.",
                            "Consumer protection in Nairobi.",
                            "Unchecked corporate greed endangers public health, while vigilant citizenship preserves community well-being.",
                            "The driver drove the bus quickly in Act 2 Scene 1."
                        ],
                        "correct_answer": 2,
                        "explanation": "A universal theme is a complete analytical assertion about life or society that applies broadly beyond the specific characters of the plot. The other options are plot summaries, topics, or isolated actions."
                    }
                },
                {
                    "type": "summary",
                    "title": "Lesson 7 Summary: Key Takeaways",
                    "content": {
                        "text": "### Key Takeaways\n\n- **Theme vs. Plot:** Plot is what happens; theme is the deeper universal truth about human nature.\n- **Dramatic Monologue:** Lifts the curtain on a character's deepest conscience and moral struggles.\n- **Flashback & Humour:** Flashbacks provide vital historical context; humour critiques social vices with wit.\n- **Transformative Lessons:** Literary study empowers learners to apply ethical values like integrity, justice, and active citizenship in daily life."
                    }
                }
            ]
        ]
    }
]
