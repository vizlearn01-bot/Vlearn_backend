"""
VLearn CBC Grade 10 English — Topic 2: Reading
Full Structured Lesson Card Definitions for Lessons 1 to 10
"""

from curriculum.cbc_grade10_english_topic2_svgs import (
    SVG_LESSON_1_FLUENCY_TRIAD,
    SVG_LESSON_2_EXTENSIVE_READING,
    SVG_LESSON_3_SKIMMING_SCANNING,
    SVG_LESSON_4_TEXT_ORGANIZATION,
    SVG_LESSON_5_INFERENCE_LOGIC,
    SVG_LESSON_6_VOCABULARY_CONTEXT,
    SVG_LESSON_7_SQ4R_METHOD,
    SVG_LESSON_8_CRITICAL_READING,
    SVG_LESSON_9_REFERENCE_RESEARCH,
    SVG_LESSON_10_SYNTHESIS_MATRIX,
)

TOPIC_2_LESSONS_ALL = [
    # =========================================================================
    # LESSON 1: Reading Fluency and Expressive Reading
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Reading Fluency and Expressive Reading",
        "unit_description": "Mastering oral reading accuracy, conversational pace, and expressive prosody with proper intonation, phrasing, and emotional resonance.",
        "lesson_title": "Reading Fluency and Expressive Reading",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Secondary Student Reading Aloud Expressively",
                    "content": {
                        "title": "Expressive Oral Reading and Fluency Mastery",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/African_Girl_at_Work.jpg",
                        "caption": "A senior secondary learner practicing expressive oral reading, integrating accurate decoding, rhythm, and prosody to bring written text to life.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define reading fluency and analyze its three core pillars: Accuracy, Rate, and Prosody (Expression)\n- Apply vocal inflections, pitch modulation, and punctuation pauses to communicate mood and tone\n- Chunk text into natural syntactic phrases rather than reading word-by-word\n- Self-monitor reading performance to correct pronunciation and decoding errors in real time"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Robot vs. The Storyteller",
                    "content": {
                        "text": "Have you ever listened to someone read a story aloud in a flat, monotone voice, sounding like a robot decoding one isolated word at a time?\n\n- **Option 1 (Choppy & Robotic):** *\"The... boy... went... to... the... dark... house... and... he... was... very... scared.\"*\n- **Option 2 (Expressive & Fluent):** *\"The boy went to the dark house [pause], and he was **very** scared!\"*\n\nIn the second version, the reader chunks words into natural phrases (*\"to the dark house\"*), observes a suspenseful pause at the conjunction (*\"and\"*), and emphasizes the intensifier (*\"very\"*) with higher pitch and volume. This is **expressive reading (prosody)** in action—it builds the bridge between simple word decoding and deep emotional comprehension."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Reading Fluency & Prosody",
                    "content": {
                        "term": "Prosody",
                        "definition": "The rhythmic and intonational aspect of spoken language when reading aloud, including pitch variation, stress, phrasing, and pausing that reflect the meaning and mood of the text."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Three Pillars of Reading Fluency",
                    "content": {
                        "headers": ["Pillar", "Definition", "Key Linguistic Mechanisms", "Common Problem", "Fluency Target"],
                        "rows": [
                            ["Accuracy", "Correct recognition and pronunciation of written words.", "Phonics decoding, root/prefix parsing, active self-correction.", "Misreading word endings, skipping words, guessing.", "98%+ accuracy on grade-level text."],
                            ["Rate (Pace)", "Reading speed measured in words per minute (WPM).", "Steady tempo, natural phrasing, automatic word recognition.", "Reading too slowly (halting) or racing too fast (garbled).", "130–160 WPM oral reading flow."],
                            ["Prosody (Expression)", "Using vocal melody and rhythm to convey emotional meaning.", "Pitch modulation, volume shifts, punctuation pausing, chunking.", "Monotone delivery, ignoring commas and full stops.", "Expressive phrasing matching speaker emotions."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Reading Fluency Architecture & Triad Matrix",
                    "content": {
                        "title": "The Three Pillars of Reading Fluency",
                        "caption": "Architectural breakdown showing how Accuracy, Rate, and Prosody combine to unlock working memory and achieve total comprehension.",
                        "svg_content": SVG_LESSON_1_FLUENCY_TRIAD
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Reading Passage Model: Phrasing Analysis",
                    "content": {
                        "intro": "Examine how a master reader annotates and performs this atmospheric descriptive excerpt:",
                        "steps": [
                            "**Original Text:** *\"The wind roared across the dark valley, while the rain drip-drip-dripped steadily on the iron roof.\"*",
                            "**Step 1: Identify Phrasing Boundaries:** *[The wind roared] / [across the dark valley], // [while the rain] / [drip-drip-dripped steadily] / [on the iron roof].*",
                            "**Step 2: Apply Pitch & Volume Modulation:** Lower pitch and increase volume on *'roared'* to evoke power. Use a sharp, rhythmic staccato cadence on *'drip-drip-dripped'* to mimic raindrops hitting iron.",
                            "**Step 3: Respect Punctuation Pauses:** Pause for two beats at the comma (*','*) before transitioning into the quiet, rhythmic rain clause."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Phrasing and Expressive Reading in Action",
                    "content": {
                        "title": "Mastering Prosody and Phrasing in Oral Reading",
                        "youtube_id": "i0cQu7vnDzs",
                        "url": "https://www.youtube.com/watch?v=i0cQu7vnDzs",
                        "description": "Educational masterclass demonstrating how chunking sentences into syntactic units and varying pitch dramatically boosts comprehension and audience engagement."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: Fluency & Prosody Workshop",
                    "content": {
                        "title": "Oral Performance & Cognitive Processing",
                        "text": "**Pre-Reading Task:** In your notebook, write down the three core components of fluency mentioned in the video (Accuracy, Rate, Prosody).\n\n**Post-Reading Discussion:** Why does reading with natural prosody actually help the reader understand the text better? Cognitive research reveals that expressive chunking groups words into meaningful grammatical units, freeing working memory to interpret themes instead of decoding individual letters."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Fluency Pitfalls & Cognitive Traps",
                    "content": {
                        "text": "### Trap 1: The 'Speed Equals Mastery' Fallacy\n- **The Pitfall:** Racing through text as fast as possible without pauses to appear smart.\n- **The Correction:** Speed-reading without comprehension is useless noise. True fluency maintains a controlled, conversational pace (130–160 WPM).\n\n### Trap 2: The Monotone 'Safe Mode' Delivery\n- **The Pitfall:** Speaking in an unvarying pitch to avoid making pronunciation errors.\n- **The Correction:** Monotone reading obscures sentence boundaries and bores listeners. Always raise pitch for questions (*?*), lower pitch for statements (*.*), and use emphasis on key emotive words."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Expressive Makeovers",
                    "content": {
                        "intro": "Practice reading this dramatic paragraph three times, applying the specific performance instructions:",
                        "steps": [
                            {"title": "Sentence 1: 'The door opened slowly...'", "description": "Lower your volume to a suspenseful whisper and stretch out the vowel in 'slowly'."},
                            {"title": "Sentence 2: 'A tall man stood in the shadows.'", "description": "Use a low pitch and a measured, deliberate pace; pause for two beats at the full stop."},
                            {"title": "Sentence 3: ''Who is there?' he demanded loudly.'", "description": "Raise your pitch sharply at the question mark, and project high volume with assertive authority."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Elements of Reading Fluency",
                    "content": {
                        "question": "Which of the three core elements of reading fluency refers specifically to 'reading with natural rhythm, appropriate pauses, pitch variation, and emotional expression'?",
                        "options": [
                            "Accuracy",
                            "Rate",
                            "Prosody",
                            "Decoding"
                        ],
                        "correct_answer": 2,
                        "explanation": "Prosody is the formal linguistic term for expressive reading that incorporates natural rhythm, intonation, pitch variation, and syntactic pausing. Accuracy refers to correct word decoding, Rate refers to speed, and Decoding refers to translating written letters into sound."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Oral Reading Mechanics",
                    "content": {
                        "question": "When reading aloud, what is the primary consequence of ignoring punctuation marks and reading in a monotone rush?",
                        "options": [
                            "It significantly improves the listener's reading speed.",
                            "It obscures sentence boundaries, distorts meaning, and impairs comprehension.",
                            "It demonstrates advanced mastery of extensive reading stamina.",
                            "It converts an argumentative text directly into an objective narrative."
                        ],
                        "correct_answer": 1,
                        "explanation": "Ignoring punctuation and rushing without prosody obscures grammatical sentence boundaries, turning the text into a confusing jumble of words that impairs both the reader's and the listener's comprehension."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Accuracy** ensures words are decoded and pronounced correctly (98%+ target).\n- **Rate** maintains a steady, conversational pace without rushing or dragging (130–160 WPM).\n- **Prosody** injects the 'music of language' through pitch variation, punctuation pauses, and emotional stress.\n- **Mastery Rule:** Read in meaningful syntactic phrases rather than isolated single words to maximize comprehension."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Extensive Reading and Reading Stamina
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Extensive Reading and Reading Stamina",
        "unit_description": "Developing independent reading stamina, applying the 95% comprehensibility rule, maintaining reflective reading logs, and choosing graded readers for lifelong literacy.",
        "lesson_title": "Extensive Reading and Reading Stamina",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Reading in Modern Secondary Library",
                    "content": {
                        "title": "Independent Extensive Reading and Stamina Development",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/Grace_Knox_Lecture_Hall%2C_University_at_Buffalo_%28Buffalo%2C_NY_-_12-10-08%29.jpg",
                        "caption": "Secondary school learners immersed in sustained independent extensive reading, training cognitive stamina to read longer and more complex texts with ease.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between Intensive Reading (micro-analysis) and Extensive Reading (macro-volume/pleasure)\n- Apply the '95% Comprehensibility Rule' to select appropriate graded readers and novels\n- Build sustained reading stamina from 10 minutes up to 45 minutes of distraction-free focus\n- Maintain a structured Reading Log to track independent reading volume, genre diversity, and personal reflections"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Scrolling Brain vs. The Deep Reader",
                    "content": {
                        "text": "Think about how we consume social media feeds: we glance at a 15-word post, scroll, watch a 10-second clip, and scroll again. Our brains get accustomed to 'fast food' snippets of text.\n\nWhen we open a 200-page novel or an in-depth textbook chapter, our brain experiences cognitive fatigue after just two pages! Reading stamina is like physical marathon training: you cannot run 20 kilometers on day one. You must progressively train your mental focus to sustain deep concentration over long periods."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Extensive Reading & Reading Stamina",
                    "content": {
                        "term": "Reading Stamina",
                        "definition": "The cognitive ability to maintain sustained focus, comprehension, and engagement while reading independently for an extended period without succumbing to distraction or mental fatigue."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Intensive vs. Extensive Reading Paradigms",
                    "content": {
                        "headers": ["Dimension", "Intensive Reading (Classroom Micro)", "Extensive Reading (Independent Macro)"],
                        "rows": [
                            ["Primary Purpose", "Detailed linguistic, grammatical, and syntactic analysis.", "Global comprehension, fluency, stamina, and reading pleasure."],
                            ["Text Volume", "Short texts (1–3 paragraphs, poems, or short extracts).", "Large volumes (entire novels, graded readers, biographies)."],
                            ["Difficulty Level", "Challenging (at or above current instructional level).", "Easy to moderate (comprehending 95%+ of words on page)."],
                            ["Dictionary Use", "Frequent lookup of unknown words and idioms.", "Minimal; infer from context to maintain reading flow."],
                            ["Assessment", "Comprehension questions, grammatical parsing.", "Reading logs, book reviews, personal response essays."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Extensive Reading Framework & Stamina Ladder",
                    "content": {
                        "title": "Intensive vs. Extensive Reading & 4-Week Stamina Ladder",
                        "caption": "Visual breakdown contrasting micro-linguistic study with macro-volume extensive reading, featuring the step-by-step 45-minute stamina ladder.",
                        "svg_content": SVG_LESSON_2_EXTENSIVE_READING
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Reading Log Framework: Structured Reflection",
                    "content": {
                        "intro": "Examine this model Grade 10 student reading log entry following an independent reading session:",
                        "steps": [
                            "**1. Basic Book Metadata:** Title: *The River and the Source* | Author: Margaret Ogola | Date: 24th August 2026 | Pages Read: 45–72 (28 pages) | Duration: 35 minutes.",
                            "**2. Key Narrative Developments:** Akoko leaves her marital village after false accusations from her mother-in-law and travels to the District Commissioner in Kisumu to seek justice.",
                            "**3. New Contextual Vocabulary:** *'Obdurate'* (inferred: stubborn, unyielding) | *'Matriarch'* (inferred: female head of a family).",
                            "**4. Personal Evaluative Response:** Akoko's courage to challenge traditional oppression demonstrates that true leadership requires moral integrity, not just traditional title."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Building Lifelong Extensive Reading Habits",
                    "content": {
                        "title": "The Science of Extensive Reading and Habit Formation",
                        "youtube_id": "lmEa9_WdpHo",
                        "url": "https://www.youtube.com/watch?v=lmEa9_WdpHo",
                        "description": "Educational guide exploring how daily extensive reading rewires the brain, accelerates vocabulary acquisition by 400%, and builds effortless academic writing skills."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: The 95% Five-Finger Rule",
                    "content": {
                        "title": "Testing Book Difficulty with the Five-Finger Test",
                        "text": "**Pre-Reading Protocol:** Open any book to a random page in the middle containing approximately 100 words. Begin reading. Every time you encounter a word you do not know, raise one finger.\n\n**Post-Reading Diagnosis:**\n- 0–1 Fingers: Too easy (great for quick relaxation).\n- 2–3 Fingers: **Just Right (Ideal for Extensive Reading & Stamina Growth)**.\n- 4 Fingers: Challenging (requires intensive study support).\n- 5+ Fingers: Too hard (will cause frustration; choose a graded reader instead!)."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Extensive Reading Mistakes to Avoid",
                    "content": {
                        "text": "### Mistake 1: Stopping for Every Unknown Word\n- **The Pitfall:** Halting reading every 30 seconds to look up a word in a dictionary.\n- **The Correction:** This breaks narrative immersion and kills reading enjoyment. Use context clues, underline the word lightly in pencil, and keep reading!\n\n### Mistake 2: The 'Grin and Bear It' Trap\n- **The Pitfall:** Forcing yourself to finish a book that is completely uninteresting or painfully difficult.\n- **The Correction:** In extensive reading, if a book does not engage you after 20 pages, close it and choose another title that matches your passions."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Setting Up Your Reading Schedule",
                    "content": {
                        "intro": "Follow these four steps to implement an effective independent reading routine:",
                        "steps": [
                            {"title": "Step 1: Choose Your Passion Genre", "description": "Select an engaging book (fiction, historical drama, science biography) using the 95% Five-Finger Rule."},
                            {"title": "Step 2: Create a Distraction-Free Sanctuary", "description": "Turn off your smartphone, find a well-lit quiet spot, and set a timer for your target duration (e.g., 15 minutes)."},
                            {"title": "Step 3: Read for Continuous Flow", "description": "Read smoothly without stopping to analyze grammar or consult dictionaries; follow the central narrative thread."},
                            {"title": "Step 4: Log and Reflect", "description": "Record the date, page span, and a 2-sentence reflection in your dedicated VLearn Reading Log."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Purpose of Extensive Reading",
                    "content": {
                        "question": "What is the primary pedagogical goal of extensive reading in the Senior Secondary English curriculum?",
                        "options": [
                            "To memorize complex grammatical formulas and analyze every single word.",
                            "To read a large volume of enjoyable, accessible texts for global comprehension, stamina, and fluency.",
                            "To search exclusively for phone numbers and departure times in directories.",
                            "To skim through books without understanding any of the central themes."
                        ],
                        "correct_answer": 1,
                        "explanation": "Extensive reading focuses on reading large quantities of easy, enjoyable texts to build vocabulary, cognitive stamina, and overall fluency. Memorizing grammar rules is the domain of intensive reading."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: The 95% Rule Application",
                    "content": {
                        "question": "According to the 95% Rule of extensive reading, what should a student do if they encounter 8 unknown words on a single 100-word page?",
                        "options": [
                            "Consult a bilingual dictionary for all 8 words immediately.",
                            "Select a simpler graded reader or book where they understand at least 95% of vocabulary.",
                            "Force themselves to read the entire 300 pages to build character.",
                            "Abandon independent reading altogether."
                        ],
                        "correct_answer": 1,
                        "explanation": "If a text has more than 5 unknown words per 100 words (below 95% comprehension), it causes cognitive overload and frustration. The student should choose a more accessible graded reader to maintain fluency and enjoyment."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Extensive reading** builds lifelong literacy through high-volume, pleasurable reading.\n- **The 95% Rule** ensures reading remains smooth, fluent, and cognitively rewarding.\n- **Reading Stamina** must be trained progressively (10 min → 20 min → 30 min → 45 min daily).\n- **Reading Logs** anchor memory, track literary volume, and stimulate critical personal synthesis."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Skimming, Scanning, and Locating Information
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Skimming, Scanning, and Locating Information",
        "unit_description": "Mastering high-speed selective reading strategies: skimming for global gist and topic sentences, and scanning for isolated keywords, dates, and tabular data.",
        "lesson_title": "Skimming, Scanning, and Locating Information",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Locating Information in Competition",
                    "content": {
                        "title": "Speed-Reading and Information Retrieval in Action",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/2019_SSSDC_Division_2_Finals.jpg",
                        "caption": "Secondary debaters and researchers rapidly locating evidence and dates using skimming and scanning to locate vital data within seconds.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between Skimming (reading for general gist) and Scanning (reading for specific target details)\n- Execute systematic skimming protocols using headings, introductory paragraphs, and topic sentences\n- Execute rapid zigzag eye movements to scan for dates, capitalized proper nouns, and numerical data\n- Locate critical information in complex non-continuous texts (bus timetables, charts, dictionary indices) in under 10 seconds"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: Searching Your Smartphone Contacts",
                    "content": {
                        "text": "Imagine looking up a classmate's phone number on your smartphone:\n- Do you read every single name from 'Aaron' all the way down to 'Zachary'? **Of course not!**\n- Your eyes jump instantly to the letter 'M', scroll rapidly looking only for the visual shape 'Mary', and ignore everything else.\n\nYou just performed **scanning**! In academic study and exams, trying to read every word of a 10-page report when you only need one date wastes 90% of your time. Skimming and scanning give you superpower speed to find what matters."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Skim vs. Scan",
                    "content": {
                        "term": "Skimming",
                        "definition": "A speed-reading technique where the reader glides rapidly across headings, introductions, and topic sentences to grasp the main idea or general gist of a text without reading every word."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Skimming vs. Scanning Strategic Comparison",
                    "content": {
                        "headers": ["Strategy", "Primary Objective", "Eye Movement Pattern", "Reading Target", "Typical Speed"],
                        "rows": [
                            ["Skimming", "Get the central theme / gist / overall structure.", "Horizontal sweeps across top of paragraphs.", "Titles, subheadings, 1st & last paragraphs, topic sentences.", "400–800 words per minute."],
                            ["Scanning", "Locate a specific, isolated fact or data point.", "Rapid diagonal / zigzag search down the page.", "Keywords, dates (1963), numbers (75%), capitalized names.", "Locate target in <10 seconds."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Speed-Reading Dual Pipeline Architecture",
                    "content": {
                        "title": "Skimming vs. Scanning Dual Strategy Pipeline",
                        "caption": "Visual diagram comparing the top-down horizontal sweep of skimming with the rapid zigzag eye tracking of scanning.",
                        "svg_content": SVG_LESSON_3_SKIMMING_SCANNING
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Scanning a Regional Bus Schedule",
                    "content": {
                        "intro": "Scan this regional transport timetable to answer two targeted questions in under 5 seconds:",
                        "steps": [
                            "**Timetable Data:**\n- Mombasa | Departure: 07:00 AM | Platform 3 | Status: On Time\n- Nakuru | Departure: 09:30 AM | Platform 1 | Status: Delayed\n- Kisumu | Departure: 11:15 AM | Platform 5 | Status: On Time\n- Eldoret | Departure: 02:00 PM | Platform 2 | Status: Cancelled",
                            "**Target Question 1:** *What time does the bus leave for Nakuru?*\n- **Scanning Method:** Formulate mental clue 'Nakuru' (capital 'N'). Zigzag eyes down column 1. Stop at 'Nakuru'. Slide right to column 2. **Answer: 09:30 AM**.",
                            "**Target Question 2:** *Which platform does the Kisumu bus depart from?*\n- **Scanning Method:** Scan for capital 'K' in column 1. Slide right to column 3. **Answer: Platform 5**."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Speed-Reading Strategies: Skimming and Scanning",
                    "content": {
                        "title": "Speed Reading for Comprehension Exams & Research",
                        "youtube_id": "nlSNLhD1L_I",
                        "url": "https://www.youtube.com/watch?v=nlSNLhD1L_I",
                        "description": "Comprehensive tutorial detailing eye tracking mechanics, peripheral vision utilization, and keyword locking to ace reading comprehension tests."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: The 30-Second Skim Drill",
                    "content": {
                        "title": "Extracting the Gist from an Editorial",
                        "text": "**Pre-Reading Protocol:** Open an editorial article from a daily newspaper. Set a timer for exactly 30 seconds.\n\n**During Reading:**\n1. Read the headline and subhead.\n2. Read the full first paragraph.\n3. Read only the first sentence of paragraphs 2, 3, and 4.\n4. Read the concluding sentence of the final paragraph.\n\n**Post-Reading Test:** Close the article and immediately state: (1) What is the main issue? (2) Is the author in favor or opposed?"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Speed-Reading Traps to Avoid",
                    "content": {
                        "text": "### Trap 1: Skimming Without Structure ('Careless Skipping')\n- **The Pitfall:** Skipping random sentences without reading topic sentences.\n- **The Correction:** Skimming is a disciplined technique. Always read the headline, the introduction, and the first sentence of body paragraphs.\n\n### Trap 2: Reading Surrounding Sentences While Scanning\n- **The Pitfall:** Getting distracted and reading interesting sentences around your target keyword.\n- **The Correction:** Maintain tunnel vision! Do not read sentences until your eye locks onto your specific target keyword or number."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Timed Keyword Retrieval",
                    "content": {
                        "intro": "Identify the target keyword and determine the scanning strategy for each inquiry:",
                        "steps": [
                            {"title": "Inquiry 1: 'In what year was Wangari Maathai awarded the Nobel Peace Prize?'", "description": "Target Clue: 4-digit number (e.g., 2004) and capital letters 'Nobel'. Scan rapidly for number patterns."},
                            {"title": "Inquiry 2: 'What is the boiling point of ethanol?'", "description": "Target Clue: Degree symbol '°C' or numerical temperature value near 'ethanol'."},
                            {"title": "Inquiry 3: 'Who is the current chairperson of the Kenya Wildlife Service?'", "description": "Target Clue: Capitalized proper nouns ('Dr.', 'Prof.', 'Chairperson', 'KWS')."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Strategy Selection",
                    "content": {
                        "question": "You are writing a history report and need to find the exact year the Uganda Railway reached Kisumu. Which reading strategy is most efficient?",
                        "options": [
                            "Intensive reading of the entire 300-page historical book from page 1.",
                            "Skimming only the introductory preface of the book.",
                            "Scanning the text specifically for four-digit numbers and capitalized words like 'Kisumu' or '1901'.",
                            "Extensive reading of a historical fiction novel set in East Africa."
                        ],
                        "correct_answer": 2,
                        "explanation": "Scanning is the designated strategy for locating isolated factual data, such as a four-digit year or capitalized proper noun, without reading surrounding text."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Skimming Protocol",
                    "content": {
                        "question": "When skimming an academic article for the general gist, what should the reader prioritize reading?",
                        "options": [
                            "Every statistical footnote and bibliographic citation.",
                            "The title, subheadings, introductory paragraph, concluding paragraph, and topic sentences.",
                            "Only the middle dialogue between minor characters.",
                            "Every adjective and adverb in reverse alphabetical order."
                        ],
                        "correct_answer": 1,
                        "explanation": "A structured skim targets the high-yield structural framework: title, subheadings, introduction, conclusion, and paragraph topic sentences."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Skimming** extracts the high-level gist by targeting titles, introductions, conclusions, and topic sentences.\n- **Scanning** retrieves isolated facts (dates, numbers, names) via rapid diagonal and zigzag eye movements.\n- **Efficiency Rule:** Scan first when searching for an isolated answer; skim first when evaluating a book's relevance for research."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Main Ideas, Details, Sequence, and Text Organization
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Main Ideas, Details, Sequence, and Text Organization",
        "unit_description": "Analyzing paragraph anatomy, isolating topic sentences from supporting evidence, and mastering the four foundational text patterns: Chronology, Cause-Effect, Compare-Contrast, and Problem-Solution.",
        "lesson_title": "Main Ideas, Details, Sequence, and Text Organization",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Students Analyzing Text Organization Patterns",
                    "content": {
                        "title": "Structural Text Analysis and Paragraph Mapping",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5c/TwoWomenTalkingBodyLanguage.jpg",
                        "caption": "Senior secondary learners mapping out expository text architecture, identifying how authors link topic sentences with logical supporting structures.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the Main Idea of a paragraph and differentiate it from supporting details (examples, statistics, proof)\n- Recognize and classify the four major text organization patterns: Chronological, Cause & Effect, Compare & Contrast, and Problem & Solution\n- Identify transition words and signposts that signal each organizational structure\n- Construct structured paragraph maps using graphic organizers to enhance study notes"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Architectural Blueprint of a Paragraph",
                    "content": {
                        "text": "Think of a well-written paragraph like a dining table:\n- The tabletop is the **Main Idea** (the core assertion or claim).\n- The legs holding up the tabletop are the **Supporting Details** (data, examples, explanations, and evidence).\n\nIf you remove the legs, the table collapses! If an author writes a paragraph with only details and no main idea, it is just a pile of wooden sticks. Understanding text organization allows you to immediately see how the author built their argument."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Main Idea & Text Organization",
                    "content": {
                        "term": "Text Organization",
                        "definition": "The logical framework or structural pattern an author uses to organize thoughts, sequence events, connect causes with effects, compare ideas, or resolve problems."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Four Patterns of Text Organization",
                    "content": {
                        "headers": ["Pattern", "Core Purpose", "Key Transitional Signposts", "Visual Organizer"],
                        "rows": [
                            ["Chronological (Sequence)", "Arranging events in temporal order or step-by-step procedure.", "First, next, then, previously, subsequently, in 1963, finally.", "Timeline / Process Flowchart"],
                            ["Cause and Effect", "Explaining reasons why an event occurred and its consequences.", "Because, since, as a result, consequently, therefore, led to.", "Cause-to-Effect Fishbone / Arrow Tree"],
                            ["Compare and Contrast", "Highlighting similarities (compare) and differences (contrast).", "Similarly, likewise, however, unlike, whereas, on the other hand.", "Venn Diagram / Matrix Table"],
                            ["Problem and Solution", "Presenting a dilemma or crisis followed by viable resolutions.", "The dilemma, obstacle, to solve this, a remedy, one solution.", "Problem-Action-Outcome Chain"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Patterns of Text Organization Architecture",
                    "content": {
                        "title": "Four Patterns of Expository Text Organization",
                        "caption": "Comprehensive 2x2 matrix showcasing Chronological, Cause-Effect, Compare-Contrast, and Problem-Solution blueprints with transitional signposts.",
                        "svg_content": SVG_LESSON_4_TEXT_ORGANIZATION
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Paragraph Deconstruction",
                    "content": {
                        "intro": "Read and deconstruct the text structure of this environmental science excerpt:",
                        "steps": [
                            "**Expository Text:** *\"Deforestation represents a severe environmental crisis in Kenya, leading to catastrophic topsoil erosion and prolonged drought cycles. To combat this pressing challenge, the Ministry of Environment has launched an aggressive national tree-growing campaign, mobilizing communities to plant 15 billion trees by 2032.\"*",
                            "**Step 1: Identify the Main Idea:** Kenya is actively addressing the severe crisis of deforestation through a massive national tree-planting initiative.",
                            "**Step 2: Identify Organizational Pattern:** **Problem and Solution** (woven with secondary Cause and Effect).",
                            "**Step 3: Map Structural Signposts:** *'crisis... leading to'* (identifies problem and consequence) -> *'To combat this pressing challenge'* (identifies transition into solution) -> *'planting 15 billion trees'* (concrete solution)."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Identifying Text Structures and Paragraph Mapping",
                    "content": {
                        "title": "Expository Text Structures in Non-Fiction",
                        "youtube_id": "u26Ng43ZhEY",
                        "url": "https://www.youtube.com/watch?v=u26Ng43ZhEY",
                        "description": "Visual guide demonstrating how to identify informational text patterns and use graphic organizers to summarize articles rapidly."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: Graphic Organizer Mapping",
                    "content": {
                        "title": "Deconstructing Compare and Contrast in Biology Texts",
                        "text": "**Pre-Reading Task:** Draw a two-circle Venn diagram in your exercise book labeled 'Leopards' and 'Cheetahs'.\n\n**Reading Passage:** *\"Both leopards and cheetahs are apex African felids that hunt in the savannah. However, unlike the cheetah, which has slender legs, solid round black spots, and distinctive black tear marks on its face for daytime speed, the leopard possesses a muscular frame, rosette-patterned rosettes, and hunts primarily at night from tree branches.\"*\n\n**Post-Reading Synthesis:** Fill in the overlapping center (apex African cat, savannah predator) and the outside differences."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Text Structure Pitfalls",
                    "content": {
                        "text": "### Pitfall 1: Assuming the First Sentence is ALWAYS the Main Idea\n- **The Trap:** Believing topic sentences can never appear in the middle or end of a paragraph.\n- **The Correction:** While many writers open with the topic sentence, skilled authors often begin with an engaging hook or anecdote and place the core main idea at the end as a climax.\n\n### Pitfall 2: Confusing Cause with Effect\n- **The Trap:** Mixing up what triggered the event (the Cause) with the resulting consequence (the Effect).\n- **The Correction:** Ask: *'Which event happened first?'* The cause always precedes the effect in logic, even if the sentence structure mentions the effect first."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Organizational Pattern Identification",
                    "content": {
                        "intro": "Classify the text organization pattern of each excerpt and justify your selection:",
                        "steps": [
                            {"title": "Passage 1: 'Because factory emissions surged, atmospheric greenhouse gases trapped excess heat, resulting in record global temperatures.'", "description": "Pattern: **CAUSE AND EFFECT** (Signposts: 'Because', 'resulting in')."},
                            {"title": "Passage 2: 'In 1914, World War I commenced. Three years later, in 1917, the US joined. Finally, in 1918, an armistice was declared.'", "description": "Pattern: **CHRONOLOGICAL / SEQUENCE** (Signposts: Historical dates '1914', '1917', '1918', 'Finally')."},
                            {"title": "Passage 3: 'Traffic congestion paralyzes city roads during rush hour. To resolve this, the county government built bypasses and expanded commuter rail.'", "description": "Pattern: **PROBLEM AND SOLUTION** (Signposts: 'congestion paralyzes', 'To resolve this')."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Text Pattern Analysis",
                    "content": {
                        "question": "Read this sentence: 'Since heavy torrential rains damaged the feeder roads, farmers were unable to transport their fresh milk to the processing factory.' What is the organizational pattern?",
                        "options": [
                            "Compare and Contrast",
                            "Problem and Solution",
                            "Cause and Effect",
                            "Chronological Sequence"
                        ],
                        "correct_answer": 2,
                        "explanation": "The sentence uses 'Since' to establish the cause (torrential rains damaging feeder roads) and describes the direct resulting consequence (inability to transport milk), which is the Cause and Effect pattern."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Topic Sentence Identification",
                    "content": {
                        "question": "What is the primary role of a topic sentence within an expository paragraph?",
                        "options": [
                            "To provide a complete bibliography and list of references.",
                            "To express the central main idea that all supporting details prove or explain.",
                            "To entertain the reader with an unrelated personal joke.",
                            "To summarize the entire 300-page book in five words."
                        ],
                        "correct_answer": 1,
                        "explanation": "The topic sentence articulates the primary claim or central main idea of the paragraph, which is subsequently reinforced and developed by supporting details."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Main Ideas** provide the central thesis; **Supporting Details** provide the empirical proof and illustrations.\n- **Chronological** patterns sequence events across time using temporal markers.\n- **Cause and Effect** connects catalysts with resultant outcomes.\n- **Compare and Contrast** explores points of similarity and divergence.\n- **Problem and Solution** identifies a crisis and details strategic remedies."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Comprehension, Inference, and Conclusions
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Comprehension, Inference, and Conclusions",
        "unit_description": "Mastering the three levels of reading comprehension (Literal, Inferential, Evaluative), applying the inference equation (Text Clues + Schema = Inference), and drawing textual evidence-backed conclusions.",
        "lesson_title": "Comprehension, Inference, and Conclusions",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Literary Detective Analyzing Text Clues",
                    "content": {
                        "title": "Deep Comprehension and Inferential Reasoning",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Dean_Rusk%2C_Lyndon_B._Johnson_and_Robert_McNamara_in_Cabinet_Room_meeting_February_1968.jpg",
                        "caption": "Critical thinkers examining underlying documents and subtext, combining explicit statements with contextual background knowledge to reach sound conclusions.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between Explicit Information (directly stated) and Implicit Information (implied/suggested)\n- Apply the Core Inference Formula: `Text Clues + Background Schema = Justified Inference`\n- Differentiate the three levels of comprehension: Literal (on the lines), Inferential (between the lines), and Evaluative (beyond the lines)\n- Cite specific textual evidence to defend all inferential conclusions against speculation"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Shivering Classmate",
                    "content": {
                        "text": "Imagine a classmate walks into the classroom at 8:00 AM. Their school uniform is soaked, water is dripping from their umbrella, and their teeth are chattering.\n\nDid they say a single word? **No.** Did anyone tell you the weather? **No.**\nYet you instantly know: *It is raining heavily outside, and the morning is freezing cold.*\n\nYou did not see the rain cloud yourself, but you observed **text clues** (soaked uniform, dripping umbrella, chattering teeth), combined them with your **background knowledge** (umbrellas and soaked clothes happen in rain), and made an **inference**!"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Inference & Conclusion",
                    "content": {
                        "term": "Inference",
                        "definition": "A logical conclusion drawn by combining explicit textual clues with the reader's background knowledge (schema) to uncover implicit, unstated meaning."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Three Levels of Reading Comprehension",
                    "content": {
                        "headers": ["Level", "Reading Focus", "Key Question Types", "Verification Method", "Sample Excerpt Analysis"],
                        "rows": [
                            ["Level 1: Literal", "\"On the Lines\" — Explicitly stated facts.", "Who, What, Where, When.", "Can point a finger directly at the exact words on the page.", "\"Juma arrived at the school gate at 8:15 AM.\""],
                            ["Level 2: Inferential", "\"Between the Lines\" — Implicit meaning & subtext.", "Why, How, Character Motives, Atmosphere.", "Combining text clues with real-world logic and schema.", "\"Juma is late for class and anxious about assembly.\""],
                            ["Level 3: Evaluative", "\"Beyond the Lines\" — Critical judgment & morals.", "Was the action right? How does this apply universally?", "Evaluating ethics, author purpose, and real-world relevance.", "\"Punctuality is vital for academic and career discipline.\""]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Inference Logic & 3-Level Comprehension Matrix",
                    "content": {
                        "title": "Inference Logic & Three Levels of Comprehension",
                        "caption": "Visual diagram demonstrating the scientific inference equation (Text Clues + Background Schema = Justified Inference) alongside Literal, Inferential, and Evaluative comprehension tiers.",
                        "svg_content": SVG_LESSON_5_INFERENCE_LOGIC
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Reading Passage Model: Drawing Conclusions",
                    "content": {
                        "intro": "Read this short narrative passage and trace how to build a rigorous, evidence-backed conclusion:",
                        "steps": [
                            "**Passage:** *\"The surgeon stepped out of the operating theatre, pulled down his mask, and slowly shook his head from side to side while staring silently at the floor. The family members in the waiting room gasped and began weeping.\"*",
                            "**Step 1: Extract Explicit Text Clues:** Surgeon removes mask, slowly shakes head, stares at floor, family gasps and weeps.",
                            "**Step 2: Connect Background Schema:** In medical contexts, a downcast head shake by a lead surgeon combined with family grief indicates an unsuccessful surgery or tragic loss of life.",
                            "**Step 3: State the Justified Inference:** The patient has either passed away or suffered severe surgical complications.",
                            "**Step 4: Formulate Evaluative Conclusion:** The author communicates profound tragedy through subtle character kinesics and non-verbal cues rather than explicit medical jargon."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Active Comprehension: Making Inferences",
                    "content": {
                        "title": "How to Make Supported Inferences in Literature",
                        "youtube_id": "jdtSQKkgHsE",
                        "url": "https://www.youtube.com/watch?v=jdtSQKkgHsE",
                        "description": "Engaging masterclass breaking down the boundary between literal facts and inferential deductions, featuring detective-style textual case studies."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: The 3-Tier Question Ladder",
                    "content": {
                        "title": "Constructing Literal, Inferential, and Evaluative Questions",
                        "text": "**Passage for Analysis:** *“The sky grew ominous and dark; the weaver birds abruptly ceased their singing. A cool breeze rustled the maize leaves, and Amina dashed into the compound to haul the dry washing off the line.”*\n\n- **Literal Question (Level 1):** What did Amina haul off the clothes line? *(Answer: The dry washing)*\n- **Inferential Question (Level 2):** Why did the birds stop singing and why did Amina rush? *(Answer: An imminent rainstorm is approaching)*\n- **Evaluative Question (Level 3):** Why is proactive preparation for weather changes essential for agrarian households? *(Answer: Protects harvest and resources)*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Inference Cognitive Traps",
                    "content": {
                        "text": "### Trap 1: Wild Speculation vs. Justified Inference\n- **The Pitfall:** Making an imaginative guess that has zero supporting words in the text.\n- **The Correction:** In examinations, an inference is only valid if you can cite explicit words from the passage to prove it. Always ask: *'Which sentence proves my inference?'*\n\n### Trap 2: Overlooking Subtle Body Language and Tone\n- **The Pitfall:** Expecting authors to state emotions directly (*'He was angry'*).\n- **The Correction:** Authors use 'show, don't tell' (clenched fists, tight jaw, slamming doors). Pay close attention to physical actions and descriptions."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Clue Hunting and Inference Deduction",
                    "content": {
                        "intro": "Analyze each scenario to extract explicit clues and state the justified inference:",
                        "steps": [
                            {"title": "Scenario 1: 'Karanja sat staring at the blank sheet of paper, drumming his fingers furiously and glancing every ten seconds at the wall clock.'", "description": "Inference: Karanja is experiencing acute exam anxiety and struggling to formulate answers under strict time pressure."},
                            {"title": "Scenario 2: 'After the principal announced the exam results, Auma leaped from her chair, embraced her desk mate, and wiped tears of relief from her cheeks.'", "description": "Inference: Auma achieved stellar examination marks that exceeded her anxious expectations."},
                            {"title": "Scenario 3: 'The customer took one sip of soup, immediately signaled the waiter, pushed the bowl away, and asked for the manager.'", "description": "Inference: The food was defective (cold, spoiled, or contaminated), causing severe customer dissatisfaction."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Inferring Environmental Context",
                    "content": {
                        "question": "Read this excerpt: 'The sky grew dark, birds abruptly fell silent, a sharp cool gust swept through the trees, and Mary sprinted outside to shutter the windows.' What can be inferred about the meteorological conditions?",
                        "options": [
                            "A desert dust drought is beginning.",
                            "A fierce rainstorm is about to break.",
                            "A mid-summer heatwave is reaching its peak.",
                            "Early morning sunrise is illuminating the sky."
                        ],
                        "correct_answer": 1,
                        "explanation": "Dark skies, abrupt silence among birds (a natural instinct before sudden barometric pressure drops), cool gusts, and shuttering windows are classic sensory text clues signaling an imminent rainstorm."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Comprehension Level Classification",
                    "content": {
                        "question": "When a student answers the question 'Was the protagonist justified in keeping the lost wallet or should they have returned it to the police?', which level of comprehension are they applying?",
                        "options": [
                            "Literal Comprehension",
                            "Phonetic Decoding",
                            "Evaluative Comprehension",
                            "Scanning Strategy"
                        ],
                        "correct_answer": 2,
                        "explanation": "Evaluating moral justification, ethics, and personal judgment based on a text operates at Level 3: Evaluative Comprehension ('beyond the lines')."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Inference Formula:** `Text Clues + Background Schema = Justified Inference`.\n- **Comprehension Levels:** Literal (explicit facts), Inferential (implicit subtext), Evaluative (critical value judgment).\n- **Evidence Mandate:** An inference is only valid if anchored in verifiable textual evidence.\n- **Mastery Rule:** Read between the lines by analyzing sensory details, character actions, and non-verbal cues."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Vocabulary in Context and Word Relationships
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Vocabulary in Context and Word Relationships",
        "unit_description": "Decoding unfamiliar words using the S.A.D.E. context clue strategy (Synonyms, Antonyms, Definitions, Examples) and mastering natural collocations and word partnerships.",
        "lesson_title": "Vocabulary in Context and Word Relationships",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Student Using Context Clues and Lexical Tools",
                    "content": {
                        "title": "Context Clues and Lexical Deduction in Reading",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Close_up_view_of_a_microphone_set_up_in_a_recording_studio.jpg",
                        "caption": "Secondary learners developing vocabulary decoding skills, analyzing surrounding sentence syntax and collocations to unlock advanced words without pausing.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Apply the S.A.D.E. Framework (Synonym, Antonym, Definition, Example) to deduce unfamiliar vocabulary\n- Recognize natural English collocations (Verb+Noun, Adjective+Noun, Adverb+Adjective)\n- Distinguish between literal denotation and emotional connotation in word selection\n- Replace awkward, unnatural word partnerships with authentic idiomatic collocations"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Ravenous Runner",
                    "content": {
                        "text": "Read this sentence:\n> *\"After completing the 15-kilometer marathon under the scorching midday sun, the athlete was completely **ravenous**, devouring three heaped plates of ugali and beef stew in ten minutes.\"*\n\nEven if you have never encountered the word **ravenous** before, you can deduce its meaning instantly!\n- Clue 1: Ran a grueling 15 km race (exhausting calories).\n- Clue 2: Devoured three heaped plates in ten minutes.\n\nTherefore, **ravenous** must mean *extremely hungry / famished*! You did not need a dictionary; the author provided all the clues you needed."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Context Clues & Collocation",
                    "content": {
                        "term": "Collocation",
                        "definition": "A predictable, natural combination of words that commonly occur together in a language (e.g., 'heavy rain' rather than 'thick rain', 'make a mistake' rather than 'do a mistake')."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The S.A.D.E. Context Clue Typology",
                    "content": {
                        "headers": ["Clue Type", "Mechanism", "Key Linguistic Markers", "Sentence Model"],
                        "rows": [
                            ["S - Synonym", "Author provides a similar familiar word nearby.", "Also known as, or, in other words, that is.", "\"The teacher's lecture was **lucid**; it was so **clear** that everyone passed.\""],
                            ["A - Antonym", "Author contrasts the target word with its direct opposite.", "Unlike, however, but, in contrast to, whereas.", "\"Unlike her **garrulous** sister who talks non-stop, Mary is **taciturn** and quiet.\""],
                            ["D - Definition", "Author explains the exact meaning within the sentence.", "Is defined as, commas (appositives), dashes, means.", "\"An **entomologist**, or **scientist who studies insects**, visited our school.\""],
                            ["E - Example", "Author provides concrete illustrations of the term.", "Such as, for instance, including, like.", "\"The savanna was full of **ungulates**, including **zebras, gazelles, and giraffes**.\""]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "S.A.D.E. Context Clues & Collocation Network",
                    "content": {
                        "title": "S.A.D.E. Context Clues & Natural Word Partnerships",
                        "caption": "Visual architecture mapping Synonym, Antonym, Definition, and Example clue categories alongside Verb+Noun, Adj+Noun, and Adv+Adj collocations.",
                        "svg_content": SVG_LESSON_6_VOCABULARY_CONTEXT
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Deconstructing Advanced Context Clues",
                    "content": {
                        "intro": "Analyze how to deduce the meanings of bolded academic words in these sentences:",
                        "steps": [
                            "**Sentence 1:** *\"The doctor administered a strong analgesic to **alleviate** the patient's acute pain, making it milder and easier to endure.\"*\n- **Clue Type:** Synonym/Restatement (*'making it milder and easier to endure'*).\n- **Deduction:** *Alleviate* = to reduce severity, relieve, ease.",
                            "**Sentence 2:** *\"Instead of adopting a **benevolent** attitude towards the displaced flood victims, the greedy landlord acted with immense cruelty and selfishness.\"*\n- **Clue Type:** Antonym/Contrast (*'Instead of... greedy, cruelty, selfishness'*).\n- **Deduction:** *Benevolent* = kind, generous, charitable.",
                            "**Sentence 3:** *\"The region is completely **arid**—an inhospitable, dry wasteland receiving less than 50 millimeters of rain annually.\"*\n- **Clue Type:** Direct Definition (*'an inhospitable, dry wasteland...'*).\n- **Deduction:** *Arid* = extremely dry, barren, lacking moisture."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Mastering Context Clues and Lexical Expansion",
                    "content": {
                        "title": "How to Use Context Clues to Expand Your Vocabulary",
                        "youtube_id": "CqgB2fDLwaA",
                        "url": "https://www.youtube.com/watch?v=CqgB2fDLwaA",
                        "description": "Engaging vocabulary masterclass demonstrating how advanced readers infer challenging words in literary and scientific passages."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: Collocation Makeover Workshop",
                    "content": {
                        "title": "Authentic English Collocations vs. Direct Mother-Tongue Translations",
                        "text": "**Why Literal Translation Fails:** In many local languages, one might literally say *'to do a crime'* or *'to drink a cigarette'*. In English, these sound unnatural because words partner in fixed collocations.\n\n**Transformative Collocation Pairs:**\n- ❌ *'He did a grave mistake.'* → ✔️ *'He **made** a grave mistake.'*\n- ❌ *'Strong rain fell on the village.'* → ✔️ *'**Heavy** rain fell on the village.'*\n- ❌ *'I will make an exam tomorrow.'* → ✔️ *'I will **sit / take** an exam tomorrow.'*\n- ❌ *'She was in heavy pain.'* → ✔️ *'She was in **excruciating / severe** pain.'*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Vocabulary Traps in Reading",
                    "content": {
                        "text": "### Trap 1: Word-for-Word Dictionary Dependency\n- **The Pitfall:** Halting reading to look up every single polysyllabic word.\n- **The Correction:** Use S.A.D.E. context clues first. 90% of the time, the sentence provides sufficient meaning to sustain comprehension without interrupting reading flow.\n\n### Trap 2: Ignoring Multiple Meanings (Polysemy)\n- **The Pitfall:** Assuming a word only has one fixed definition (e.g., *'bank'* as a financial building vs. *'bank of a river'*).\n- **The Correction:** Always test your inferred definition back into the sentence syntax to verify that it fits the context."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: S.A.D.E. Classification and Deduction",
                    "content": {
                        "intro": "Deduce the meaning of each bolded word and identify the specific clue type:",
                        "steps": [
                            {"title": "Item 1: 'The math competition was so formidable that even national champions struggled for hours.'", "description": "Meaning: Highly challenging, daunting, intimidating. Clue Type: Example/Cause-Effect ('even national champions struggled')."},
                            {"title": "Item 2: 'Unlike the ephemeral lifespan of a mayfly which lasts a single day, the tortoise is remarkably long-lived.'", "description": "Meaning: Short-lived, brief, fleeting. Clue Type: Antonym ('Unlike... remarkably long-lived')."},
                            {"title": "Item 3: 'Hydroponics, the agricultural practice of growing crops in nutrient-rich water without soil, is expanding.'", "description": "Meaning: Soil-less water farming. Clue Type: Definition (appositive phrase enclosed in commas)."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Context Clue Deduction",
                    "content": {
                        "question": "Read this sentence: 'The chemistry exam was so formidable that even the top-ranked students struggled to complete the complex calculations.' What does the word formidable mean in this context?",
                        "options": [
                            "Extremely easy and pleasant to complete.",
                            "Excessively long in page length.",
                            "Extremely challenging, daunting, and difficult.",
                            "Entertaining and humorous."
                        ],
                        "correct_answer": 2,
                        "explanation": "Context clues ('even top-ranked students struggled' and 'complex calculations') indicate that the examination was intimidatingly difficult and challenging (formidable)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Collocation Mastery",
                    "content": {
                        "question": "Which of the following sentences uses a natural, idiomatic English collocation?",
                        "options": [
                            "The reckless driver did a fatal crime on the highway.",
                            "The community suffered bitter disappointment when the project was delayed.",
                            "A thick rain fell over the mountain throughout the morning.",
                            "I will make a university test next Tuesday."
                        ],
                        "correct_answer": 1,
                        "explanation": "'Bitter disappointment' is an authentic adjective+noun collocation. Standard collocations for the others are 'commit a crime', 'heavy rain', and 'take/sit a test'."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 6 Summary & Key Takeaways",
                    "content": {
                        "text": "- **S.A.D.E. Clue Framework:** Synonyms, Antonyms, Definitions, and Examples provide instant in-text decoding.\n- **Collocations** are natural word partnerships (Verb+Noun, Adj+Noun, Adv+Adj) that ensure fluent, idiomatic communication.\n- **Contextual Fitting:** Always substitute your deduced meaning back into the sentence to verify coherence.\n- **Mastery Rule:** Read like a detective—use the author's surrounding vocabulary clues before reaching for a dictionary."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7: Study Skills: SQ4R, Note-Making, and Summarising
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Study Skills: SQ4R, Note-Making, and Summarising",
        "unit_description": "Mastering the 6-phase active SQ4R study method (Survey, Question, Read, Reflect, Recite, Review), creating structured two-column note frames, and drafting concise, objective summaries.",
        "lesson_title": "Study Skills: SQ4R, Note-Making, and Summarising",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Student Applying Active SQ4R Study Method",
                    "content": {
                        "title": "Active Note-Making and SQ4R Study Skills",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/African_Girl_at_Work.jpg",
                        "caption": "A senior secondary student practicing active note-making using the SQ4R study framework, transforming textbook subheadings into self-quizzing review charts.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Execute all six steps of the SQ4R study system: Survey, Question, Read, Reflect, Recite, and Review\n- Convert textbook subheadings into targeted self-inquiry questions\n- Distinguish between passive Note-Taking (copying) and active Note-Making (condensing and paraphrasing)\n- Write a concise, 50-word objective summary containing only essential main ideas and key transitions"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: Passive Highlighting vs. Active Mastery",
                    "content": {
                        "text": "Consider two students preparing for a biology exam on 'The Human Circulatory System':\n\n- **Student A (Passive Studying):** Reads the 20-page chapter line by line, highlighting 80% of every page in bright yellow ink. After two hours, they are exhausted and cannot recall the function of the pulmonary artery.\n- **Student B (Active SQ4R Studying):** Spends 3 minutes surveying headings and diagrams, turns headings into questions (*'What is the function of the pulmonary artery?'*), reads targeted sections to find answers, recites the answers aloud, and makes a 2-column note chart.\n\nStudent B spends less time, retains 300% more information, and aces the exam! This lesson equips you with Student B's exact active study system."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: SQ4R Active Study Method",
                    "content": {
                        "term": "SQ4R Method",
                        "definition": "A systematic, 6-phase active reading and study strategy consisting of Survey, Question, Read, Reflect, Recite, and Review, designed to maximize long-term memory encoding and critical comprehension."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Six Phases of SQ4R Method",
                    "content": {
                        "headers": ["Phase", "Action Protocol", "Cognitive Mechanism", "Time Allocation"],
                        "rows": [
                            ["1. S - Survey", "Skim titles, subheadings, diagrams, bold terms, chapter summary.", "Builds high-level mental roadmap of chapter structure.", "2–3 Minutes"],
                            ["2. Q - Question", "Convert each subheading into a specific, answerable question.", "Stimulates active curiosity and focuses visual search.", "1–2 Minutes / Section"],
                            ["3. R1 - Read", "Read text actively with the sole objective of answering your Q.", "Filters out non-essential filler; extracts key data.", "3–5 Minutes / Section"],
                            ["4. R2 - Reflect", "Connect new insights to prior knowledge and real-world examples.", "Deepens conceptual understanding and schema integration.", "1 Minute / Section"],
                            ["5. R3 - Recite", "Close book and summarize the answer aloud or write in 2-column notes.", "Locks concepts from working memory into long-term memory.", "2 Minutes / Section"],
                            ["6. R4 - Review", "Revisit notes weekly; cover answers and re-test questions.", "Prevents the forgetting curve; cements permanent mastery.", "5 Minutes / Week"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "SQ4R Active Study Cycle Architecture",
                    "content": {
                        "title": "The 6-Phase SQ4R Active Study Method Flow",
                        "caption": "Structural diagram illustrating the cyclic progression of Survey, Question, Read, Reflect, Recite, and Review with time allocations and memory retention mechanisms.",
                        "svg_content": SVG_LESSON_7_SQ4R_METHOD
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Structured Two-Column Note Frame & Summary Model",
                    "content": {
                        "intro": "Examine this structured Note-Making frame and subsequent 40-word objective summary of a geography text on soil erosion:",
                        "steps": [
                            "**Two-Column Note Frame:**\n- **Left Column (My Inquiry Questions):**\n  1. What are the primary human causes of soil erosion?\n  2. What are the most effective conservation methods?\n- **Right Column (Paraphrased Answers):**\n  1. Overgrazing, deforestation, and monoculture farming strip protective vegetative cover.\n  2. Terracing, contour plowing, and agroforestry restore soil stability.",
                            "**40-Word Objective Summary:**\n*\"Soil erosion is primarily driven by human activities like deforestation and overgrazing, which strip protective ground cover. To restore land productivity, farmers must implement sustainable conservation techniques, including terracing, contour plowing, and widespread agroforestry planting.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "The SQ4R Active Study Method in Action",
                    "content": {
                        "title": "How to Study Textbooks with the SQ4R Method",
                        "youtube_id": "eSqMZlPAJbg",
                        "url": "https://www.youtube.com/watch?v=eSqMZlPAJbg",
                        "description": "Comprehensive tutorial demonstrating how to turn passive reading into high-retention active recall using SQ4R and Cornell-style note frames."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: Transforming Headings into Inquiries",
                    "content": {
                        "title": "Self-Inquiry Practice Drill",
                        "text": "**Heading 1:** *'The Economic Consequences of Rural-Urban Migration in Kenya'*\n- **Transformed Question:** *'What are the positive and negative economic consequences of rural-urban migration in Kenya?'*\n\n**Heading 2:** *'Mechanisms of Transmission of Malaria Parasites'*\n- **Transformed Question:** *'How exactly do female Anopheles mosquitoes transmit malaria parasites to human bloodstreams?'*\n\n**Heading 3:** *'The Role of Tone in Oral Performance'*\n- **Transformed Question:** *'Why is vocal tone critical for communicating emotion in oral poetry?'*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Study & Note-Making Pitfalls",
                    "content": {
                        "text": "### Trap 1: The 'Coloring Book' Highlighting Trap\n- **The Pitfall:** Highlighting entire paragraphs word-for-word.\n- **The Correction:** If everything is highlighted, nothing stands out. Highlight no more than 10% of a page (key nouns, verbs, numbers, and definitions only).\n\n### Trap 2: Note-Taking (Copying) vs. Note-Making (Synthesizing)\n- **The Pitfall:** Writing down exact sentences from the textbook.\n- **The Correction:** Verbatim copying bypasses cognitive processing. Always close the book and paraphrase ideas in your own words."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Writing an Objective Summary",
                    "content": {
                        "intro": "Follow this 4-step checklist to write an impeccable academic summary:",
                        "steps": [
                            {"title": "Step 1: Draft the Central Main Idea Sentence", "description": "State what the overall passage is about in one clear topic sentence."},
                            {"title": "Step 2: Extract Essential Supporting Points", "description": "List only major supporting claims; completely delete minor examples, stories, and statistics."},
                            {"title": "Step 3: Connect with Transitional Signposts", "description": "Combine the extracted points using transitions ('Consequently', 'In addition', 'Furthermore')."},
                            {"title": "Step 4: Maintain Complete Objectivity", "description": "Do NOT include personal opinions or words like 'I think' or 'In my view'; reflect only the source text."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: SQ4R Step Identification",
                    "content": {
                        "question": "During which phase of the SQ4R method does a student skim headings, inspect graphs, and read the chapter summary BEFORE diving into the text?",
                        "options": [
                            "Read (R1)",
                            "Review (R4)",
                            "Survey (S)",
                            "Recite (R3)"
                        ],
                        "correct_answer": 2,
                        "explanation": "Survey (S) is the initial preview step where the learner skims structural elements to establish a mental roadmap before reading."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Summary Rules",
                    "content": {
                        "question": "Which of the following is a fundamental rule of writing an academic summary?",
                        "options": [
                            "Include all minor statistics, personal opinions, and biographical trivia.",
                            "Copy the first and last sentence of every paragraph word-for-word.",
                            "Be concise, paraphrase the core main ideas in your own words, and maintain complete objectivity.",
                            "Ensure the summary is at least twice as long as the original passage."
                        ],
                        "correct_answer": 2,
                        "explanation": "An academic summary must be concise, written in the student's own words (paraphrased), capture only essential main ideas, and remain strictly objective without personal commentary."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 7 Summary & Key Takeaways",
                    "content": {
                        "text": "- **SQ4R Active Cycle:** Survey → Question → Read → Reflect → Recite → Review.\n- **Active Note-Making:** Paraphrase into 2-column self-testing charts; avoid passive verbatim copying.\n- **Selective Highlighting:** Limit highlighting to key terms and definitions (<10% of text).\n- **Objective Summary:** Condense core main ideas without adding personal bias or extraneous examples."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8: Critical and Close Reading: Purpose, Audience, Attitude, and Argument
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Critical and Close Reading: Purpose, Audience, Attitude, and Argument",
        "unit_description": "Evaluating authorial intent, identifying target audience expectations, decoding emotive tone and connotation, and testing the logical strength of argumentative claims.",
        "lesson_title": "Critical and Close Reading: Purpose, Audience, Attitude, and Argument",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Parliamentary Debate and Critical Argument Evaluation",
                    "content": {
                        "title": "Close Reading of Rhetorical Arguments",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/dc/First_European_Parliament_Hemicycle%2C_Robert_Schuman_building%2C_1973.jpg",
                        "caption": "Critical discourse analysts evaluating political and legal texts, scrutinizing author purpose, persuasive tone, and the empirical validity of underlying arguments.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Determine an author's primary Purpose (to inform, persuade, entertain, warn, or satirize)\n- Analyze how target Audience expectations influence diction, tone, and register\n- Decode authorial Attitude and Tone through loaded diction, denotation, and connotation\n- Critically evaluate Argument Rigor by distinguishing empirical proof from emotional propaganda"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: Two Perspectives on One School Uniform Rule",
                    "content": {
                        "text": "Read these two descriptions of the exact same school uniform policy:\n\n- **Text A (Official School Bulletin):** *\"The Board of Management is proud to institute a structured uniform policy to foster community unity, eliminate socio-economic peer pressure, and promote academic focus among our dedicated scholars.\"*\n- **Text B (Student Editorial Blog):** *\"The administration has slapped us with a rigid, archaic dress code that suffocates our individuality and forces everyone to look like identical factory robots.\"*\n\nBoth texts describe the exact same blazer and tie! But notice how word choice (*'foster unity, scholars'* vs. *'slapped us, archaic, suffocates, robots'*) exposes the author's **attitude (tone)**, **bias**, and **target audience**."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Connotation & Critical Tone",
                    "content": {
                        "term": "Connotation",
                        "definition": "The emotional, cultural, or social association carried by a word beyond its literal dictionary definition (denotation). Connotations can be strongly positive, negative, or neutral."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Denotation vs. Connotation Spectrum",
                    "content": {
                        "headers": ["Literal Denotation", "Positive Connotation (+)", "Neutral Term (o)", "Negative Connotation (-)"],
                        "rows": [
                            ["Thin body weight", "Slender, Graceful, Svelte", "Thin, Lean", "Skinny, Scrawny, Skeletal"],
                            ["Firm in opinion", "Determined, Resolute", "Persistent", "Stubborn, Pigheaded, Obstinate"],
                            ["Costing little money", "Inexpensive, Economical", "Low-cost, Affordable", "Cheap, Flimsy, Low-grade"],
                            ["Curious about others", "Inquisitive, Interested", "Inquiring", "Nosy, Prying, Meddlesome"]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Critical Reading Quadrant Architecture",
                    "content": {
                        "title": "Critical Reading Quadrant: Purpose, Audience, Attitude & Argument",
                        "caption": "Comprehensive 4-pillar quadrant detailing authorial purpose classification, audience analysis, tone/connotation decoding, and argument strength verification.",
                        "svg_content": SVG_LESSON_8_CRITICAL_READING
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Deconstructing a Persuasive Campaign Flyer",
                    "content": {
                        "intro": "Critically analyze this political campaign flyer segment:",
                        "steps": [
                            "**Flyer Text:** *\"My opponent has completely ignored the safety of our children, letting crime run wild in our beloved streets. Unlike them, I am a family man who will protect our neighborhoods with tough-on-crime policies. Vote for progress—vote for peace!\"*",
                            "**1. Author's Purpose:** To persuade residents to vote for the candidate in the upcoming election.",
                            "**2. Target Audience:** Local voting citizens, parents, and community homeowners.",
                            "**3. Attitude / Tone:** Hostile and alarmist towards the opponent; protective and heroic towards self.",
                            "**4. Connotation Tricks:** Positive buzzwords (*'beloved streets', 'family man', 'progress', 'peace'*) vs. fear words (*'ignored safety', 'run wild'*).",
                            "**5. Argument Rigor Evaluation:** **Extremely Weak!** Contains zero empirical crime statistics, no specific policy budgets, and relies entirely on fear-mongering and emotional manipulation."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Decoding Word Choice, Tone, and Author Bias",
                    "content": {
                        "title": "Analyzing Tone, Connotation, and Author Bias in Texts",
                        "youtube_id": "SzyvICXoEFc",
                        "url": "https://www.youtube.com/watch?v=SzyvICXoEFc",
                        "description": "Educational guide demonstrating how to identify subjective authorial tone words (critical, optimistic, patronizing, neutral) and detect covert media bias."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: Editorial Tone Analysis",
                    "content": {
                        "title": "Identifying Loaded Diction in Commercial Media",
                        "text": "**Headline A:** *'County Assembly Approves Vital Infrastructure Investment Fund.'*\n- **Tone:** Supportive, approving, laudatory (*'vital investment'*).\n\n**Headline B:** *'County Assembly Rubber-Stamps Controversial Multi-Million Spending Spree.'*\n- **Tone:** Highly critical, cynical, skeptical (*'rubber-stamps, controversial spending spree'*).\n\n**Critical Question:** How do two journalists reporting on the exact same budget bill create opposite psychological impressions on the public solely through word choice?"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Critical Reading Pitfalls",
                    "content": {
                        "text": "### Trap 1: Confusing Author Tone with Personal Emotion\n- **The Pitfall:** Believing the author's tone is 'angry' just because YOU feel angry about the topic.\n- **The Correction:** Tone resides strictly in the author's choice of adjectives, verbs, and syntax—not your personal feelings.\n\n### Trap 2: Believing Text is Objective Simply Because It Appears in Print\n- **The Pitfall:** Accepting formal print or broadcast media as 100% unbiased truth.\n- **The Correction:** Every author writes from a specific perspective. Always check who funded the publication and what counter-evidence was omitted."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Tone Classification and Diction Decoding",
                    "content": {
                        "intro": "Classify the author's attitude/tone in each excerpt and identify the triggering loaded words:",
                        "steps": [
                            {"title": "Excerpt 1: 'The proposed dam is a disastrous ecological gamble that will lay waste to our pristine river valleys.'", "description": "Tone: **Strongly Critical / Disapproving / Alarmed** (Trigger words: 'disastrous', 'gamble', 'lay waste', 'pristine')."},
                            {"title": "Excerpt 2: 'The solar installation generated 450 megawatt-hours in July, operating at 94% theoretical efficiency.'", "description": "Tone: **Objective / Neutral / Factual** (Trigger words: numerical data, standard engineering metrics)."},
                            {"title": "Excerpt 3: 'Oh brilliant, another software update that takes four hours and deletes all my saved files!'", "description": "Tone: **Sarcastic / Ironic / Frustrated** (Trigger words: 'Oh brilliant' used ironically to mean terrible)."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Tone Identification",
                    "content": {
                        "question": "An environmental scientist writes: 'The proposed industrial zone is a catastrophic blunder that will poison our delicate aquifers and decimate endemic bird species.' What is the author's attitude toward the project?",
                        "options": [
                            "Enthusiastic and supportive",
                            "Objective, neutral, and dispassionate",
                            "Strongly critical, alarmed, and condemnatory",
                            "Indifferent and uninterested"
                        ],
                        "correct_answer": 2,
                        "explanation": "Loaded emotional diction ('catastrophic blunder', 'poison', 'decimate') conveys a passionately critical and alarmed attitude opposing the industrial zone."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Connotation Analysis",
                    "content": {
                        "question": "Which of the following words carries a strongly negative connotation compared to the neutral word 'persistent'?",
                        "options": [
                            "Resolute",
                            "Determined",
                            "Obstinate",
                            "Steadfast"
                        ],
                        "correct_answer": 2,
                        "explanation": "'Obstinate' carries a negative connotation implying unreasonable, stubborn refusal to change, whereas 'resolute', 'determined', and 'steadfast' have positive connotations."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 8 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Purpose:** Analyze WHY the text exists (inform, persuade, entertain, warn).\n- **Audience:** Determine WHO the text was crafted for and how that shapes vocabulary.\n- **Attitude / Tone:** Decode emotional stance through loaded words and connotation.\n- **Argument Rigor:** Scrutinize supporting evidence; separate empirical facts from emotional manipulation."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 9: Research Beginnings and Reference Materials
    # =========================================================================
    {
        "unit_order": 9,
        "unit_name": "Research Beginnings and Reference Materials",
        "unit_description": "Locating reliable sources using reference tools (Dictionaries, Encyclopedias, Atlases, Almanacs), applying the C.R.A.P. evaluation test, and executing academic citations to prevent plagiarism.",
        "lesson_title": "Research Beginnings and Reference Materials",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Research Scholar Consulting Reference Materials",
                    "content": {
                        "title": "Academic Research and Reference Tools",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/Grace_Knox_Lecture_Hall%2C_University_at_Buffalo_%28Buffalo%2C_NY_-_12-10-08%29.jpg",
                        "caption": "Students conducting rigorous secondary research, cross-referencing encyclopedias, peer-reviewed articles, and online repositories while practicing academic citation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 9 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Select appropriate reference materials (Dictionary, Encyclopedia, Atlas, Almanac) for specific research needs\n- Apply the C.R.A.P. Test (Currency, Reliability, Authority, Purpose) to evaluate online and print sources\n- Define plagiarism and understand its severe academic and ethical implications\n- Construct accurate APA-style in-text citations and reference list entries for books, websites, and articles"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The Lemon Juice Cure vs. Scientific Medicine",
                    "content": {
                        "text": "Imagine you are writing a Grade 10 health science report on asthma and discover these two sources online:\n\n- **Source A (Anonymous Personal Blog):** *\"I drank lemon juice every morning for 5 days, and it permanently cured my chronic asthma! Doctors hide this one simple secret to sell inhalers.\"*\n- **Source B (World Health Organization Website):** *\"While citrus fruits provide vitamin C supporting overall nutrition, peer-reviewed clinical research confirms that lemon juice cannot cure asthma and should never replace prescribed bronchodilators.\"*\n\nWhich source do you cite in your academic report? **Source B!** Source B has verified authority, peer-reviewed evidence, and an objective educational purpose. Professional researchers know how to filter out online myths using structured evaluation frameworks."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Reference Materials & Plagiarism",
                    "content": {
                        "term": "Plagiarism",
                        "definition": "The act of copying or using someone else's written words, ideas, data, or arguments and presenting them as your own original work without proper citation and attribution."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Reference Materials Typology",
                    "content": {
                        "headers": ["Reference Tool", "Core Function", "Contents", "Sample Research Application"],
                        "rows": [
                            ["Dictionary", "Word-level linguistic guidance.", "Definitions, spellings, pronunciations, parts of speech, etymology.", "Checking if 'accommodate' has one 'm' or two."],
                            ["Encyclopedia", "Comprehensive thematic overviews.", "In-depth, peer-reviewed factual articles on history, science, arts.", "Researching the history and architecture of Fort Jesus."],
                            ["Atlas", "Geographical and spatial data.", "Topographical maps, climate maps, political boundaries, coordinates.", "Locating national borders and river systems of Mozambique."],
                            ["Almanac", "Annual statistical calendars.", "Yearly climate records, economic indicators, agricultural data.", "Finding Kenya's average annual tea export tonnage for 2024."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The C.R.A.P. Source Evaluation Architecture",
                    "content": {
                        "title": "The C.R.A.P. Test & Reference Tools Framework",
                        "caption": "Visual breakdown of Currency, Reliability, Authority, and Purpose evaluation criteria alongside the reference materials matrix.",
                        "svg_content": SVG_LESSON_9_REFERENCE_RESEARCH
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Citation & Paraphrasing Protocol",
                    "content": {
                        "intro": "Trace how to transform a source passage into an ethically paraphrased, correctly cited academic sentence:",
                        "steps": [
                            "**Original Source:** *\"Malaria remains a life-threatening protozoan disease transmitted to human populations primarily via the nocturnal bites of infected female Anopheles mosquitoes.\"* (Author: Dr. Sarah Maina, Published: 2023, Page 42).",
                            "**Step 1: Understand the Core Meaning:** Malaria is a dangerous illness caused by a protozoan and spread by female Anopheles mosquitoes at night.",
                            "**Step 2: Paraphrase in Your Own Words:** *Humans can contract malaria, a potentially fatal illness, when they are bitten during nighttime hours by an infected female Anopheles mosquito.*",
                            "**Step 3: Insert In-Text Citation (APA Style):** *According to Maina (2023), humans can contract malaria, a potentially fatal illness, when they are bitten during nighttime hours by an infected female Anopheles mosquito.*",
                            "**Step 4: Add Reference List Entry:** *Maina, S. (2023). Tropical Infectious Diseases in East Africa. Nairobi: Longhorn Publishers.*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Academic Citations, Referencing, and Plagiarism Prevention",
                    "content": {
                        "title": "How to Cite Sources and Avoid Plagiarism",
                        "youtube_id": "ckdWsI_NFzI",
                        "url": "https://www.youtube.com/watch?v=ckdWsI_NFzI",
                        "description": "Step-by-step tutorial demonstrating standard in-text citations, paraphrasing protocols, and bibliographic formatting for student research papers."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: Applying the C.R.A.P. Test",
                    "content": {
                        "title": "Evaluating Website Credibility",
                        "text": "Before using any online source for a research paper, audit it against these four criteria:\n\n- **C - Currency:** Was this article published or updated within the last 3–5 years? (Crucial for scientific topics).\n- **R - Reliability:** Are the claims backed by data, statistics, and verifiable external citations?\n- **A - Authority:** Who wrote this? Does the author hold relevant academic degrees or represent a recognized research institution (.edu, .go.ke, .org)?\n- **P - Purpose:** Is the website trying to educate objectively, or are they attempting to sell a commercial product or push political propaganda?"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Research & Citation Mistakes",
                    "content": {
                        "text": "### Mistake 1: 'Patchwriting' / Pseudo-Paraphrasing\n- **The Pitfall:** Keeping the exact sentence structure of the original source and simply swapping 2–3 words with a thesaurus.\n- **The Correction:** This is still plagiarism! Close the original source, think about the core idea, and rewrite the entire structure in your own natural phrasing.\n\n### Mistake 2: Citing Wikipedia as a Primary Source\n- **The Pitfall:** Putting Wikipedia in your academic reference list.\n- **The Correction:** Wikipedia is a great starting point for overview reading, but you should scroll to the bottom references and cite the primary peer-reviewed sources directly."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Reference Tool Selection",
                    "content": {
                        "intro": "Select the optimal reference tool for each research scenario:",
                        "steps": [
                            {"title": "Task 1: 'Find the official land boundary and major rivers of Mozambique.'", "description": "Optimal Tool: **ATLAS** (Specialized for cartography, maps, borders, and spatial geography)."},
                            {"title": "Task 2: 'Check whether 'definitely' is spelled with an 'i' or an 'a' in the middle.'", "description": "Optimal Tool: **DICTIONARY** (Specialized for orthography, phonetic spelling, and definitions)."},
                            {"title": "Task 3: 'Write a detailed historical report on the construction of Fort Jesus in Mombasa.'", "description": "Optimal Tool: **ENCYCLOPEDIA** (Specialized for in-depth, structured historical and cultural overviews)."},
                            {"title": "Task 4: 'Determine Kenya's national coffee export volume and average rainfall for 2024.'", "description": "Optimal Tool: **ALMANAC** (Specialized for annual statistical records and meteorological data)."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Ethical Research Standards",
                    "content": {
                        "question": "What is the formal academic term for 'copying someone else's written words, ideas, or research data and presenting them as your own without citation'?",
                        "options": [
                            "Paraphrasing",
                            "Plagiarism",
                            "Synthesis",
                            "Prosody"
                        ],
                        "correct_answer": 1,
                        "explanation": "Plagiarism is the academic term for misappropriating another person's intellectual work or words and presenting them as your own without proper credit."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Reference Tool Application",
                    "content": {
                        "question": "Which reference tool is most appropriate if a researcher needs to examine the national borders, mountain ranges, and capital cities of South America?",
                        "options": [
                            "A monolingual dictionary",
                            "A geographic atlas",
                            "An annual economic almanac",
                            "A rhyming dictionary"
                        ],
                        "correct_answer": 1,
                        "explanation": "An atlas is a dedicated volume of geographical, physical, and political maps showing boundaries, terrain, and city coordinates."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 9 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Reference Matrix:** Dictionaries (words), Encyclopedias (themes/history), Atlases (maps), Almanacs (annual statistics).\n- **The C.R.A.P. Test:** Check Currency, Reliability, Authority, and Purpose before citing any source.\n- **Plagiarism Prevention:** Always paraphrase ideas in your own words and include structured in-text citations.\n- **Mastery Rule:** Strong academic research builds upon verified, peer-reviewed foundations with full attribution."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 10: Reading-to-Response and Synthesis
    # =========================================================================
    {
        "unit_order": 10,
        "unit_name": "Reading-to-Response and Synthesis",
        "unit_description": "Synthesizing evidence from multiple independent sources, organizing findings using a thematic synthesis matrix, and drafting unified, cited critical responses.",
        "lesson_title": "Reading-to-Response and Synthesis",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Collaborative Research Synthesis in Action",
                    "content": {
                        "title": "Multi-Source Research Synthesis and Response Writing",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/2019_SSSDC_Division_2_Finals.jpg",
                        "caption": "Senior secondary students synthesizing data from multiple texts, integrating diverse viewpoints into a unified, evidence-based academic response.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 10 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define Synthesis and distinguish it from isolated single-source summaries\n- Populate a Multi-Source Synthesis Matrix to map agreements, contradictions, and data gaps\n- Weave citations from multiple authors into cohesive, theme-based paragraphs\n- Draft a comprehensive Reading-to-Response essay addressing complex real-world policy dilemmas"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Relatable Scenario: The School Plastic Bottle Dilemma",
                    "content": {
                        "text": "Imagine your school administration is deciding whether to ban single-use plastic water bottles. You are asked to review three documents:\n\n- **Source A (Environmental Report):** Highlights that 80% of plastic bottles end up in landfills, clogging drains and harming wildlife.\n- **Source B (Health Ministry Advisory):** Emphasizes that students require 2 liters of water daily to maintain cognitive focus and prevent heat fatigue.\n- **Source C (School Board Proposal):** Recommends installing filtered water refill taps in every classroom wing and issuing reusable metal flasks.\n\nIf you only summarize Source A, you ignore student health. If you only summarize Source B, you ignore environmental damage. To **synthesize**, you combine all three: *\"While pupil hydration is critical for academic learning (Source B), disposable bottles cause severe ecological pollution (Source A); therefore, the school should install filtered hydration stations and provide reusable flasks (Source C).\"* That is synthesis in action!"
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Reading-to-Response & Synthesis",
                    "content": {
                        "term": "Synthesis",
                        "definition": "The advanced cognitive process of combining and integrating key ideas, data, and perspectives from multiple independent sources to formulate a new, cohesive argument or comprehensive understanding."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Summary List vs. Integrated Synthesis",
                    "content": {
                        "headers": ["Dimension", "Simple Summary List (Beginner)", "Integrated Synthesis (Advanced CBC Standard)"],
                        "rows": [
                            ["Structure", "Paragraph 1 = Source A; Paragraph 2 = Source B; Paragraph 3 = Source C.", "Paragraphs organized by THEMES (e.g., Economic Cost, Ecological Impact, Practical Solutions)."],
                            ["Author Relationship", "Sources treated in isolation as separate silos.", "Sources brought into direct conversation (comparing agreements & contrasts)."],
                            ["Sentence Integration", "One source mentioned per paragraph.", "Multiple citations woven together in the same sentence or paragraph."],
                            ["Cognitive Depth", "Passive reporting of what each author said.", "Active evaluation, critical comparison, and original unified thesis."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Synthesis Matrix & Multi-Source Argument Pipeline",
                    "content": {
                        "title": "The Synthesis Matrix & 4-Step Response Pipeline",
                        "caption": "Visual architecture illustrating the thematic synthesis matrix alongside the 4-step workflow: Unpack Prompt, Annotate Sources, Map Matrix, and Draft Thematic Response.",
                        "svg_content": SVG_LESSON_10_SYNTHESIS_MATRIX
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Synthesizing Multiple Sources into One Paragraph",
                    "content": {
                        "intro": "Review how two contrasting source excerpts are synthesized into a single cohesive paragraph:",
                        "steps": [
                            "**Source 1 (Economic Survey):** *\"Nairobi National Park generates over Ksh 500 million annually in foreign exchange and sustains 2,000 hospitality jobs.\"*",
                            "**Source 2 (Conservation Audit):** *\"Unregulated tourist vehicle traffic in Nairobi National Park causes severe acoustic pollution and disrupts predator hunting corridors.\"*",
                            "**Synthesis Paragraph Model (55 words):**\n*\"Although Nairobi National Park serves as an indispensable economic asset generating vital foreign revenue and local employment (Source 1), heavy vehicular congestion introduces dangerous noise pollution that disrupts wildlife hunting corridors (Source 2). Consequently, conservation authorities must implement strict vehicle quotas to balance economic benefits with ecological preservation.\"*",
                            "**Key Transition Markers Used:** *'Although'* (contrast), *'Consequently'* (cause-to-solution)."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Reading Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Synthesizing Multiple Sources in Research Writing",
                    "content": {
                        "title": "How to Synthesize Multiple Sources in Academic Writing",
                        "youtube_id": "xE1JbzWuEo4",
                        "url": "https://www.youtube.com/watch?v=xE1JbzWuEo4",
                        "description": "In-depth guide demonstrating how to use synthesis matrices to group research themes and cite multiple authors seamlessly in critical essays."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Reading Lab: Thematic Synthesis Matrix Workshop",
                    "content": {
                        "title": "Constructing a 3-Source Thematic Matrix",
                        "text": "When tasked with writing a multi-source response, construct a matrix table in your notebook:\n\n| Research Theme | Source A (Article) | Source B (Infographic) | Source C (Expert Interview) |\n| :--- | :--- | :--- | :--- |\n| **1. Environmental Cost** | High landfill accumulation | 80% single-use waste rate | Marine ecosystem destruction |\n| **2. Financial Impact** | Expensive family purchase | Save Ksh 500/week with flasks | High municipal disposal fees |\n| **3. Health & Utility** | Bottled water quality variable | Dehydration impairs focus | Tap filtration ensures hygiene |\n\n**Writing Directive:** Write one unified paragraph for each horizontal row!"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Synthesis Pitfalls to Avoid",
                    "content": {
                        "text": "### Trap 1: The 'Source-by-Source' Silo Trap\n- **The Pitfall:** Writing a paper structured as: *Paragraph 1 = Source A summary; Paragraph 2 = Source B summary; Paragraph 3 = Source C summary.*\n- **The Correction:** This is a list of summaries, NOT a synthesis! Group your writing around common THEMES and cite multiple sources within each paragraph.\n\n### Trap 2: Neglecting Contrasting Perspectives\n- **The Pitfall:** Quoting only the sources you agree with and pretending opposing data does not exist.\n- **The Correction:** Acknowledge counter-evidence using concession transitions (*'While Source A argues X, Source B demonstrates Y'*)."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Synthesizing Complex Claims",
                    "content": {
                        "intro": "Synthesize the two opposing arguments into a balanced 1-sentence statement:",
                        "steps": [
                            {"title": "Claim 1: 'Artificial Intelligence software automates administrative school grading, saving teachers 10 hours per week.'", "description": "Concession: AI increases efficiency and frees teacher time for student mentorship."},
                            {"title": "Claim 2: 'Over-reliance on automated grading algorithms can overlook creative nuance and introduce algorithmic bias in essay evaluations.'", "description": "Counter-Point: Automated systems lack human qualitative judgment and empathy."},
                            {"title": "Synthesized Balance Statement:", "description": "'While AI-assisted grading significantly reduces administrative workload for educators (Claim 1), it must be coupled with human teacher oversight to prevent qualitative bias and safeguard creative nuance in student evaluation (Claim 2).'"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 1: Synthesis Definition",
                    "content": {
                        "question": "Which of the following best describes the process of synthesis in reading-to-response writing?",
                        "options": [
                            "Copying the longest paragraph from the most prestigious source without alterations.",
                            "Combining and integrating ideas and evidence from multiple sources to formulate a single, cohesive argument.",
                            "Writing three separate summaries in alphabetical order without connecting them.",
                            "Writing personal opinions without reading any of the background reference texts."
                        ],
                        "correct_answer": 1,
                        "explanation": "Synthesis is the advanced skill of weaving together key concepts, evidence, and perspectives from multiple sources to construct a unified, original argument."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment 2: Structural Architecture",
                    "content": {
                        "question": "When organizing a synthesized multi-source response essay, how should body paragraphs be structured?",
                        "options": [
                            "Each paragraph should focus on one specific source in isolation (Source A, then Source B).",
                            "Each paragraph should be organized around a central theme, integrating evidence from multiple sources.",
                            "The entire essay should consist of bullet points with no transitional words.",
                            "All paragraphs should be written in chronological order based on the author's birth date."
                        ],
                        "correct_answer": 1,
                        "explanation": "In an effective synthesis essay, body paragraphs are organized by common thematic threads, with evidence and citations from multiple sources integrated into each paragraph."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 10 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Synthesis Definition:** Combining diverse texts to build an integrated, cohesive argument.\n- **Thematic Organization:** Organize by themes rather than summarizing authors in isolated silos.\n- **The Synthesis Matrix:** Use structured cross-reference tables to map agreements, contrasts, and gaps.\n- **Mastery Rule:** Weave multiple citations into unified paragraphs using precise transitional signposts."
                    }
                }
            ]
        ]
    }
]
