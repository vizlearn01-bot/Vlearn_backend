"""
VLearn CBC Grade 10 English — Topic 1: Listening and Speaking
Full Structured Lesson Card Definitions for Lessons 4 to 10
"""

from curriculum.cbc_grade10_english_topic1_svgs import (
    SVG_CRITICAL_LISTENING_MATRIX,
    SVG_INTENSIVE_LISTENING_PROTOCOL,
    SVG_NONVERBAL_COMMUNICATION_REPAIR,
    SVG_INTERACTIVE_LISTENING_LOOP,
    SVG_LESSON_8_STRESS,
    SVG_LESSON_9_FLUENCY,
    SVG_LESSON_10_MEETINGS_DEBATE
)

TOPIC_1_LESSONS_4_TO_7 = [
    # =========================================================================
    # LESSON 4: Critical Listening: Fact, Opinion, Evidence, and Bias
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Critical Listening: Fact, Opinion, Evidence, and Bias",
        "unit_description": "Techniques for evaluating spoken claims, distinguishing verifiable facts from subjective opinions, examining supporting evidence, and detecting speaker bias.",
        "lesson_title": "Critical Listening: Fact, Opinion, Evidence, and Bias",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Debaters Presenting Arguments in Formal Competition",
                    "content": {
                        "title": "Critical Discourse in Secondary School Debate",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/2019_SSSDC_Division_2_Finals.jpg",
                        "caption": "Secondary school debaters presenting competing arguments, requiring listeners to critically evaluate claims, test underlying evidence, and filter out emotional bias.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between verifiable facts and subjective opinions in spoken discourse\n- Evaluate the relevance, reliability, and strength of supporting evidence\n- Identify verbal markers and logical fallacies that signal speaker bias\n- Apply a 4-pillar critical listening framework to media announcements, debates, and advertisements"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: The Post-Match Debate",
                    "content": {
                        "text": "Imagine two football fans discussing a school tournament final:\n\n- **Speaker A:** *\"That match was fantastic! Our team is the absolute best in the entire county, and the referee was totally biased against us!\"*\n- **Speaker B:** *\"Our team had 60% possession and made five shots on goal, but we lost 1-0 because the opponent scored a penalty in the 88th minute.\"*\n\nWhich speaker shares objective truths that can be independently verified? **Speaker B!** Speaker A shares emotional judgments. Critical listening empowers you to separate facts from feelings."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Critical Listening",
                    "content": {
                        "term": "Critical Listening",
                        "definition": "The active process of analyzing, evaluating, and judging the quality, logic, and truthfulness of a spoken message before accepting or rejecting its claims."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Four Pillars of Spoken Analysis",
                    "content": {
                        "headers": ["Element", "Definition", "Key Linguistic Markers", "Verification Method", "Spoken Example"],
                        "rows": [
                            ["Fact", "A statement that can be proven true or false with objective data.", "Numbers, dates, scientific records, historical data.", "Empirical testing, archival records, measurement.", "\"Kenya attained internal self-rule on June 1, 1963.\""],
                            ["Opinion", "A personal belief, feeling, or judgment that cannot be proven.", "Adjectives: 'best', 'worst', 'ugly', 'boring', 'should'.", "Cannot be verified; reflects personal values.", "\"Nairobi is the most vibrant and exciting city in Africa.\""],
                            ["Evidence", "Data, statistics, or expert citations used to support a claim.", "\"According to...\", \"data shows\", \"research indicates\".", "Cross-checking citations against primary sources.", "\"According to KNBS 2024 data, inflation dropped by 1.8%.\""],
                            ["Bias", "A one-sided preference or prejudice that distorts objectivity.", "Loaded words, omission of counterarguments, stereotyping.", "Exposing omitted facts and assessing commercial motive.", "\"Our brand is flawless; all competitor items are worthless.\""]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Critical Listening Framework Architecture",
                    "content": {
                        "title": "4-Pillar Critical Evaluation Matrix",
                        "caption": "Structural breakdown of Fact, Opinion, Evidence, and Bias, detailing verification criteria and spoken models for active discourse analysis.",
                        "svg_content": SVG_CRITICAL_LISTENING_MATRIX
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Deconstructing a Radio Advertisement",
                    "content": {
                        "intro": "Read and critically analyze this transcript from a commercial radio broadcast:",
                        "steps": [
                            "**Spoken Script:** *\"Are you tired of slow internet? TurboNet is the ultimate internet provider in the region! Our fiber network is 10 times faster than standard connections, as certified by the National Communications Authority. Switch to TurboNet today—the only choice for smart people!\"*",
                            "**1. Identify Facts with Evidence:** *\"Our fiber network is 10 times faster... as certified by the National Communications Authority.\"* -> This claim cites an independent regulatory body and can be checked against official speed audit registries.",
                            "**2. Identify Subjective Opinions:** *\"TurboNet is the ultimate provider\"* and *\"the only choice for smart people.\"* -> These are persuasive slogans designed to flatter the listener without factual proof.",
                            "**3. Detect Underlying Bias:** The commercial uses loaded words (*'terrible'*, *'ultimate'*, *'smart'*) while omitting subscription prices, installation fees, and regional coverage limits to present a purely one-sided benefit."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Listening Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Facts vs. Opinions in Media Discussions",
                    "content": {
                        "title": "Distinguishing Fact from Opinion in Broadcast Media",
                        "youtube_id": "LrHhkfkNdqE",
                        "url": "https://www.youtube.com/watch?v=LrHhkfkNdqE",
                        "description": "Educational guide demonstrating how speakers in news debates, commercials, and talk shows combine objective evidence with persuasive opinions."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Listening Lab: Media Literacy in the Digital Age",
                    "content": {
                        "title": "Analyzing Digital Broadcasts and Podcasts",
                        "text": "**Pre-Viewing Focus:** As you listen to informational videos or podcasts, listen for qualifying phrases like *'In my view'*, *'It seems that'*, or *'Statistics reveal'*.\n\n**Post-Viewing Reflection:** Why do advertisers intentionally weave verifiable statistics into emotional opinion statements? A critical listener isolates the statistic and examines whether the evidence actually proves the emotional claim."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Critical Listening Mistakes to Avoid",
                    "content": {
                        "text": "### Mistake 1: Equating Speaker Confidence with Factual Truth\n- **The Pitfall:** Believing a claim simply because the speaker is loud, charismatic, or confident.\n- **The Correction:** Confidence is a vocal technique, not evidence. Always probe for data, verifiable sources, and logical consistency.\n\n### Mistake 2: Dismissing All Opinions as Useless\n- **The Pitfall:** Rejecting every opinion as invalid.\n- **The Correction:** An **informed opinion** supported by verifiable evidence and expert logic is highly valuable. Distinguish between arbitrary prejudice and evidence-backed conclusions."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Fact vs. Opinion Classification",
                    "content": {
                        "intro": "Classify each spoken statement and review the analytical justification:",
                        "steps": [
                            {"title": "Statement 1: 'Mathematics is the most challenging subject in the curriculum.'", "description": "Classification: **OPINION** (Subjective feeling; learning difficulty varies among individual students)."},
                            {"title": "Statement 2: 'The school science lab contains 24 compound light microscopes.'", "description": "Classification: **FACT** (Objective; can be verified by counting the equipment in the laboratory)."},
                            {"title": "Statement 3: 'Our volleyball coach played in the national premier league for five years.'", "description": "Classification: **FACT** (Verifiable by examining official national sports association records)."},
                            {"title": "Statement 4: 'He is an incompetent school prefect because he speaks quietly.'", "description": "Classification: **OPINION / BIAS** (Subjective value judgment linking voice volume directly to leadership ability)."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Identifying Factual Discourse",
                    "content": {
                        "question": "Which of the following spoken statements represents an objective Fact?",
                        "options": [
                            "The keynote speaker delivered a wonderfully inspiring address yesterday.",
                            "The academic board meeting lasted for exactly two hours and forty-five minutes.",
                            "Students who prefer humanities subjects are more creative than science students.",
                            "Our school compound provides the absolute best learning environment in Kenya."
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is an objective fact because the duration of a meeting can be measured precisely with a clock and confirmed by everyone present. Options A, C, and D contain subjective evaluations ('wonderfully inspiring', 'more creative', 'absolute best') that cannot be empirically measured or universally proven."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Facts** are objective, empirical, and verifiable statements independent of human emotion.\n- **Opinions** reflect personal beliefs, values, and judgments and frequently rely on evaluative adjectives.\n- **Evidence** provides the foundational proof (statistics, surveys, official records) supporting claims.\n- **Bias** introduces one-sided slant through loaded wording and intentional omission of counter-facts.\n- **Mastery Rule:** When listening to any persuasive presentation, separate the emotional tone from the verifiable data."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Intensive Listening and Viewing for Details
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Intensive Listening and Viewing for Details",
        "unit_description": "Techniques for extracting precise data, following multi-step instructional sequences, and correlating acoustic speech with on-screen visual cues.",
        "lesson_title": "Intensive Listening and Viewing for Details",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Student Recording Detailed Notes in Classroom",
                    "content": {
                        "title": "Focused Note-Taking in Secondary Education",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/African_Girl_at_Work.jpg",
                        "caption": "A secondary school student demonstrating focused intensive listening and note-taking, extracting exact instructions, numbers, and sequence markers during a lesson.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate intensive listening from extensive listening based on purpose and focus\n- Extract precise figures, technical terms, and sequence steps from spoken texts\n- Synthesize spoken instructions with on-screen visual cues and diagrams\n- Execute accurate shorthand note-taking for multi-step processes and safety protocols"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: Following Critical Road Directions",
                    "content": {
                        "text": "Imagine asking a resident for directions to the county hospital:\n\n> *\"Walk straight for 200 meters. When you reach the red brick building on your left, turn right onto Tembo Lane. Pass the pharmacy, and the hospital gate is the third entrance on your right, directly opposite the post office.\"*\n\nCan you navigate successfully using only 'gist' listening? **No!** If you only remember *'walk straight and turn somewhere near a brick building'*, you will get lost. Intensive listening ensures you capture every single parameter: **200m, red brick on left, turn right, Tembo Lane, pass pharmacy, 3rd entrance on right, opposite post office**."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Intensive Listening & Viewing",
                    "content": {
                        "term": "Intensive Listening and Viewing",
                        "definition": "The focused, analytical processing of short spoken or audiovisual texts to extract specific details, precise data, linguistic forms, and sequential instructions."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Intensive vs. Extensive Listening Compared",
                    "content": {
                        "headers": ["Dimension", "Intensive Listening", "Extensive Listening"],
                        "rows": [
                            ["Primary Goal", "Detailed precision, following steps, capturing exact data.", "Global understanding, overall gist, main idea."],
                            ["Text Length", "Short, dense spoken passages (30 sec – 3 min).", "Longer audio/video passages (5 – 30 min)."],
                            ["Focus Area", "Sequence markers, numbers, specific multiword units.", "Major themes, narrative flow, general mood."],
                            ["Visual Integration", "Scrutinizing screen diagrams, gestures, step numbers.", "Broad context tracking and general scene awareness."],
                            ["Typical Context", "Lab experiments, software setups, first aid protocols.", "Listening to radio news stories, audiobooks, casual chats."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Intensive Listening & Viewing Protocol",
                    "content": {
                        "title": "4-Stage Detail Extraction Workflow",
                        "caption": "Procedural model detailing Sound Filtering, Sequence Tracking, Shorthand Recording, and Multi-Modal Triangulation for flawless comprehension.",
                        "svg_content": SVG_INTENSIVE_LISTENING_PROTOCOL
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Analysis: Logging into a School Digital Portal",
                    "content": {
                        "intro": "Analyze these spoken instructions given by an IT teacher to new students:",
                        "steps": [
                            "**Spoken Instruction:** *\"To begin, open your browser and navigate to the portal. First, enter your student admission number as username. Next, type your temporary password, which is 'Learn2026' with a capital 'L'. Finally, click the blue 'Submit' button. Make sure you do not hit enter on your keyboard—you must click the button on screen.\"*",
                            "**Step 1 — Identify Goal:** Authenticate and access the school digital portal.",
                            "**Step 2 — Sequence Extraction:**\n- 1. Launch browser -> navigate to portal address.\n- 2. Username = Student admission number.\n- 3. Password = 'Learn2026' (Key Detail: Case-sensitive capital 'L').\n- 4. Final Action = Click blue 'Submit' button on-screen.",
                            "**Step 3 — Critical Warning Detail:** Explicit instruction: Do NOT press the 'Enter' key; use the on-screen mouse click."
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Listening Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Intensive vs Extensive Listening in English",
                    "content": {
                        "title": "Mastering Detail Extraction in Spoken English",
                        "youtube_id": "p8lQ_40tq_c",
                        "url": "https://www.youtube.com/watch?v=p8lQ_40tq_c",
                        "description": "Video tutorial demonstrating how to train your ear for micro-details, acoustic cues, and sentence structure without becoming overwhelmed."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Listening Lab: Multi-Modal Audio & Visual Synthesis",
                    "content": {
                        "title": "Correlating Audio Cues with Visual Diagrams",
                        "text": "When watching an instructional or science video:\n\n1. **Audio Channel:** Listen for sequence transitions (*'After this reaction occurs...'*).\n2. **Visual Channel:** Track pointers, highlighted labels, and on-screen metric values.\n3. **Synthesis:** When the speaker says *'Connect port A to input 2'*, confirm the exact physical port geometry on the visual graphic."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Intensive Listening Mistakes to Avoid",
                    "content": {
                        "text": "### Mistake 1: Attempting Verbatim Transcription\n- **The Pitfall:** Trying to write down every spoken word word-for-word.\n- **The Correction:** Your handwriting cannot match spoken speech rate (150 words/minute). Record only key nouns, action verbs, numbers, and sequence markers.\n\n### Mistake 2: Disregarding Visual Cues on Screen\n- **The Pitfall:** Listening with eyes closed or ignoring slides during a video lecture.\n- **The Correction:** Presenters place definitions, spelling of proper nouns, and warnings on slides to reinforce speech. Triangulate ears and eyes."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Emergency First Aid Note-Taking",
                    "content": {
                        "intro": "Read the emergency first aid audio transcript and review the extracted precision notes:",
                        "steps": [
                            {"title": "Audio Text", "description": "\"If someone cuts their finger, first, wash the wound under cool running tap water for exactly 2 minutes. Next, apply gentle pressure with a clean cloth to stop the bleeding. After bleeding stops, apply a thin layer of antiseptic cream. Finally, wrap a sterile bandage firmly around the finger. If bleeding continues past 10 minutes, seek urgent medical help.\""},
                            {"title": "Note 1: Wash Duration", "description": "**2 minutes** under cool running tap water."},
                            {"title": "Note 2: Bleeding Control", "description": "**Gentle pressure** using a **clean cloth**."},
                            {"title": "Note 3: Medication", "description": "Apply thin layer of **antiseptic cream**."},
                            {"title": "Note 4: Dressing", "description": "Firmly wrap with **sterile bandage**."},
                            {"title": "Note 5: Critical Threshold", "description": "Seek hospital help if bleeding persists **> 10 minutes**."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Sequence Markers in Instructional Discourse",
                    "content": {
                        "question": "Which of the following transition markers explicitly indicates the terminal or final step in a spoken instructional sequence?",
                        "options": [
                            "First and foremost",
                            "Meanwhile",
                            "Consequently",
                            "Finally"
                        ],
                        "correct_answer": 3,
                        "explanation": "Option D ('Finally') is the standard sequence discourse marker indicating the last step in a chronological procedure. 'First and foremost' marks the beginning, 'Meanwhile' indicates simultaneous action, and 'Consequently' marks a cause-and-effect relationship."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Intensive listening** is required whenever accuracy, sequential steps, or numerical data are critical.\n- **Discourse markers** (*First, Then, Next, Prior to, Finally*) map the structure of multi-step processes.\n- **Shorthand note-taking** captures critical content words (nouns, verbs, figures) while discarding filler.\n- **Visual triangulation** pairs acoustic speech with on-screen graphics to guarantee 100% precision."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Non-verbal Communication and Conversational Skills
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Non-verbal Communication and Conversational Skills",
        "unit_description": "Principles of body language, paralanguage, kinesics, proxemics, eye contact, and conversational repair techniques to resolve communication breakdowns.",
        "lesson_title": "Non-verbal Communication and Conversational Skills",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "Body Language and Interpersonal Communication",
                    "content": {
                        "title": "Non-Verbal Dynamics in Interpersonal Discourse",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5c/TwoWomenTalkingBodyLanguage.jpg",
                        "caption": "Two people engaged in conversational dialogue displaying vital non-verbal signals: open posture, responsive facial expressions, and natural eye contact.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify and interpret key non-verbal communication channels (kinesics, paralanguage, proxemics, oculesics)\n- Demonstrate culturally appropriate eye contact, open posture, and active backchanneling\n- Apply conversational repair strategies to quickly resolve acoustic or conceptual misunderstandings\n- Harmonize verbal messages with non-verbal delivery for maximum clarity and impact"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: The Assembly Presentation",
                    "content": {
                        "text": "Consider two student leaders speaking during a school assembly:\n\n- **Speaker A:** Stands with shoulders slumped, stares down at his shoes, mumbles without vocal inflection, and holds his hands rigidly in his pockets.\n- **Speaker B:** Stands tall with an upright posture, smiles warmly, maintains comfortable eye contact across the hall, uses open hand gestures, and projects with dynamic vocal variation.\n\nWho inspires confidence and captivates the audience? **Speaker B!** Even with identical speech scripts, Speaker B's non-verbal delivery reinforces trust, authority, and engagement."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Non-Verbal Channels & Repair",
                    "content": {
                        "term": "Non-Verbal Communication & Conversational Repair",
                        "definition": "The transmission of meaning through body movement, facial expressions, vocal tone, and space, accompanied by self-correction techniques to maintain fluent understanding."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "The Four Channels of Non-Verbal Communication",
                    "content": {
                        "headers": ["Channel / Term", "Scientific Domain", "Physical Manifestation", "Positive Conversational Impact"],
                        "rows": [
                            ["Kinesics", "Body Movement & Gestures", "Hand gestures, head nods, upright posture.", "Emphasizes key points, signals enthusiasm and approachability."],
                            ["Oculesics", "Eye Behavior", "Direct, soft eye contact (4–5 sec intervals).", "Builds mutual trust, conveys honesty, and verifies listener focus."],
                            ["Paralanguage", "Vocalics (Voice Dynamics)", "Pitch, volume, pace, emphasis, strategic pauses.", "Adds emotional nuance, prevents monotone delivery, highlights key words."],
                            ["Proxemics", "Spatial Distance", "Conversational distance (0.5m – 1.2m).", "Respects personal space and aligns with cultural etiquette."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Non-Verbal Architecture & Conversational Repair",
                    "content": {
                        "title": "Non-Verbal Modalities & Repair Engine",
                        "caption": "Integrated diagram illustrating Kinesics, Oculesics, Vocalics, and Proxemics on the left, paired with the 3-step Conversational Repair Engine on the right.",
                        "svg_content": SVG_NONVERBAL_COMMUNICATION_REPAIR
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Protocols: Executing Conversational Repair",
                    "content": {
                        "intro": "When a communication breakdown occurs, use these three professional repair strategies:",
                        "steps": [
                            "**1. Request for Repetition (Acoustic Breakdown):**\n- *Trigger:* Loud ambient noise or muffled pronunciation.\n- *Phrasing:* *\"I beg your pardon, could you please repeat the last sentence? The room was a bit noisy.\"*",
                            "**2. Request for Clarification (Semantic Breakdown):**\n- *Trigger:* Unfamiliar vocabulary or ambiguous directions.\n- *Phrasing:* *\"Could you please clarify what you mean by 'inter-house allocation'?\"*",
                            "**3. Speaker Self-Correction (Slip of the Tongue):**\n- *Trigger:* Mistaken date, name, or figure.\n- *Phrasing:* *\"We will meet on Friday—excuse me, I meant Thursday afternoon at 2:00 PM.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Listening Lab
            [
                {
                    "type": "suggested_video",
                    "title": "Non-verbal Communication & Active Listening",
                    "content": {
                        "title": "Body Language and Active Listening in Practice",
                        "youtube_id": "_vhQBFf4z3E",
                        "url": "https://www.youtube.com/watch?v=_vhQBFf4z3E",
                        "description": "Demonstration showing how non-verbal feedback loops, head nodding, and posture directly influence conversational rapport."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Listening Lab: Backchanneling in Live Dialogue",
                    "content": {
                        "title": "Deploying Subtle Backchannel Signals",
                        "text": "**Backchanneling** refers to the subtle verbal and non-verbal signals a listener provides while another person is speaking to indicate active engagement without interrupting:\n\n- **Non-Verbal:** Frequent gentle head nods, eyebrow movement showing surprise or interest, leaning slightly forward.\n- **Verbal:** Low-volume acknowledgment tokens: *'Mm-hmm'*, *'I see'*, *'Right'*, *'Exactly'*, *'That makes sense'*."
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Non-Verbal Communication Pitfalls",
                    "content": {
                        "text": "### Mistake 1: Crossing Arms Defensively\n- **The Pitfall:** Folding arms tightly across the chest while listening to teachers, interviewers, or peers.\n- **The Correction:** Crossed arms create an unconscious psychological barrier, projecting defensiveness or boredom. Keep arms relaxed at sides or use open-palm desk resting.\n\n### Mistake 2: Aggressive Staring or Complete Eye Avoidance\n- **The Pitfall:** Unblinking intense staring or staring permanently at the floor.\n- **The Correction:** Natural eye contact involves holding gaze for 4 to 5 seconds, glancing briefly away to think, and returning gaze comfortably."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Interpreting Classroom Body Language",
                    "content": {
                        "intro": "Match the observed physical behavior to its psychological interpretation:",
                        "steps": [
                            {"title": "Behavior 1: Student leans forward and nods continuously.", "description": "Interpretation: **High Engagement & Agreement** (The listener is actively following the thought and affirming the speaker)."},
                            {"title": "Behavior 2: Student looks down and avoids eye contact when a question is asked.", "description": "Interpretation: **Anxiety / Unpreparedness** (The student feels unsure and is attempting to avoid selection)."},
                            {"title": "Behavior 3: Rapid drumming of fingers on the desk while checking wristwatch.", "description": "Interpretation: **Impatience / Agitation** (The listener feels restless or hurried)."}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Positive Non-Verbal Signals",
                    "content": {
                        "question": "Which of the following behaviors is recognized as a positive, encouraging non-verbal signal during an academic conversation?",
                        "options": [
                            "Checking your smartphone notifications while nodding periodically",
                            "Nodding your head gently while maintaining comfortable, intermittent eye contact",
                            "Standing with arms tightly crossed and leaning backward against a wall",
                            "Looking past the speaker's shoulder to observe people walking in the hallway"
                        ],
                        "correct_answer": 1,
                        "explanation": "Option B is correct because nodding accompanied by steady, soft eye contact is the universal non-verbal signal of active attention and respectful engagement. Options A, C, and D exhibit distracting, closed, or disengaged body language that disrupts communication."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 6 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Non-verbal communication** comprises kinesics (body), oculesics (eyes), vocalics (voice), and proxemics (space).\n- **Active backchanneling** (nodding, *'I see'*, *'Mm-hmm'*) validates the speaker in real-time.\n- **Conversational repair** provides polite verbal formulas to request repetition, clarify terms, or execute instant self-correction.\n- **Consistency:** Ensure your facial expressions and body posture align with your spoken message."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7: Interactive and Responsive Listening
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Interactive and Responsive Listening",
        "unit_description": "Advanced interpersonal communication skills: paraphrasing, formulating clarifying questions, empathetic validation, and closing the communication loop.",
        "lesson_title": "Interactive and Responsive Listening",
        "pages": [
            # Page 1: Discovery & Objectives
            [
                {
                    "type": "suggested_image",
                    "title": "High-Level Collaborative Dialogue and Responsive Listening",
                    "content": {
                        "title": "Strategic Communication and Responsive Dialogue",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Dean_Rusk%2C_Lyndon_B._Johnson_and_Robert_McNamara_in_Cabinet_Room_meeting_February_1968.jpg",
                        "caption": "A formal meeting setting illustrating responsive listening: processing complex information, paraphrasing proposals, clarifying ambiguity, and validating colleague perspectives.",
                        "author": "Wikimedia Commons / National Archives",
                        "licensing": "Public domain"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate passive listening from interactive and responsive listening\n- Formulate accurate, respectful paraphrasing stems to confirm understanding\n- Construct targeted clarifying questions without interrupting speaker flow\n- Execute the 5-stage interactive listening feedback loop in academic and professional settings"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Familiar Scenario: A Classmate in Crisis",
                    "content": {
                        "text": "Imagine a classmate rushes up to you visibly distressed:\n\n> *\"I spent three hours finishing my English project, and then my computer crashed and deleted the file! The submission deadline is in two hours and I don't know what to do!\"*\n\n- **Passive / Poor Response:** *\"That's too bad. Are you coming to football practice later?\"*\n- **Responsive / Interactive Response:** *\"Oh no, that's terrible! So, if I understand correctly, you lost your completed draft and are worried you'll miss the 2:00 PM deadline? Let's go explain the situation to Mr. Omondi together right now.\"*\n\nNotice how the responsive listener **restates the core problem**, **acknowledges the stress**, and **collaborates on a solution**."
                    }
                }
            ],
            # Page 2: Core Concepts & Terminology
            [
                {
                    "type": "definition_card",
                    "title": "Core Terminology: Interactive Listening & Paraphrasing",
                    "content": {
                        "term": "Interactive and Responsive Listening",
                        "definition": "A collaborative communication process where the listener actively reflects, checks, clarifies, and responds to both the factual content and emotional tone of the speaker."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Passive Listening vs. Interactive Responsive Listening",
                    "content": {
                        "headers": ["Feature", "Passive Listening", "Interactive Responsive Listening"],
                        "rows": [
                            ["Listener Role", "Silent, passive receiver of acoustic sound.", "Active conversational partner in a two-way feedback loop."],
                            ["Cognitive Effort", "Minimal; focuses on waiting for one's turn to speak.", "High; decodes facts, emotional subtext, and intent."],
                            ["Verification", "None; assumes understanding without proof.", "Uses paraphrasing: 'So what you are saying is...'"],
                            ["Clarification", "Avoids asking questions or pretends to understand.", "Asks targeted probing questions to eliminate ambiguity."],
                            ["Interpersonal Outcome", "Frequent misunderstandings and emotional distance.", "High trust, psychological safety, and procedural accuracy."]
                        ]
                    }
                }
            ],
            # Page 3: Model & Structured Analysis / Visual Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "5-Stage Interactive Listening Feedback Loop",
                    "content": {
                        "title": "The Interactive Listening Cycle",
                        "caption": "Visual diagram detailing the continuous 5-step cycle: 1. Receive, 2. Process, 3. Paraphrase, 4. Clarify, and 5. Respond with Validation.",
                        "svg_content": SVG_INTERACTIVE_LISTENING_LOOP
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Dialogue: Clarifying an Academic Assignment",
                    "content": {
                        "intro": "Study this structured model dialogue between a teacher and a student negotiating meaning:",
                        "steps": [
                            "**Teacher:** *\"For next week's history assignment, you must submit a concise analytical summary of a national monument, supplemented by a creative visual aid.\"*",
                            "**Student (Step 4 - Clarification):** *\"Excuse me, Teacher. Could you please clarify what length you mean by a 'concise summary'? How many words should it be?\"*",
                            "**Teacher:** *\"Good question! It should be strictly between 150 and 200 words.\"*",
                            "**Student (Step 3 - Paraphrase):** *\"So, if I understand correctly, we need to write a one-page summary under 200 words and bring in either an original drawing, model, or photograph of the monument?\"*",
                            "**Teacher (Step 5 - Validation):** *\"Exactly! That is precisely what is required. Well done.\"*"
                        ]
                    }
                }
            ],
            # Page 4: Media Integration & Listening Lab
            [
                {
                    "type": "suggested_video",
                    "title": "The Art of Active & Responsive Listening",
                    "content": {
                        "title": "Responsive Listening and Empathy in Communication",
                        "youtube_id": "aCutWBCCMaA",
                        "url": "https://www.youtube.com/watch?v=aCutWBCCMaA",
                        "description": "Educational video exploring the psychology of active listening, empathetic reflection, and avoiding conversational narcissism."
                    }
                },
                {
                    "type": "real_world_example",
                    "title": "Listening Lab: Standard Paraphrasing Sentence Stems",
                    "content": {
                        "title": "Mastering Professional Paraphrasing Formulas",
                        "text": "Never copy the speaker's exact words like a parrot. Use these sentence stems to reframe their ideas in your own words:\n\n- *\"So, what you are essentially saying is that...\"*\n- *\"If I understand your main point correctly, you mean...\"*\n- *\"In other words, from your perspective...\"*\n- *\"It sounds like you are feeling concerned about... Is that right?\"*"
                    }
                }
            ],
            # Page 5: Common Mistakes & Guided Practice
            [
                {
                    "type": "concept_explanation",
                    "title": "Common Interactive Listening Mistakes",
                    "content": {
                        "text": "### Mistake 1: Conversational Hijacking (Me-First Listening)\n- **The Pitfall:** Responding to someone's problem by immediately talking about your own experience (*\"Oh, you think that's bad? Let me tell you what happened to me!\"*).\n- **The Correction:** Keep the focus on the speaker until their message is fully validated before sharing your perspective.\n\n### Mistake 2: Robotic or Verbatim Repetition\n- **The Pitfall:** Repeating the speaker's exact words back to them word-for-word.\n- **The Correction:** Paraphrasing requires cognitive synthesis—translate their thoughts into fresh vocabulary to prove true comprehension."
                    }
                },
                {
                    "type": "step_process",
                    "title": "Guided Practice: Paraphrasing Makeovers",
                    "content": {
                        "intro": "Transform these speaker statements into professional, empathetic paraphrases:",
                        "steps": [
                            {"title": "Speaker Statement 1: 'I really want to attend university, but my family's financial situation is strained and I worry about the tuition fees.'", "description": "Professional Paraphrase: *\"So, if I understand correctly, you are strongly motivated to pursue higher education, but you feel anxious about the financial burden of tuition on your family.\"*"},
                            {"title": "Speaker Statement 2: 'The school computer lab is always overcrowded after classes, and I can never find an open machine to complete my typing project.'", "description": "Professional Paraphrase: *\"So what you're saying is that high lab congestion after hours is preventing you from accessing the hardware you need to finish your assignments on time.\"*"}
                        ]
                    }
                }
            ],
            # Page 6: Knowledge Check & Summary
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Formulating Effective Paraphrases",
                    "content": {
                        "question": "Which of the following introductory phrases is the most effective and polite way to begin a paraphrase to verify understanding?",
                        "options": [
                            "You are wrong about that, because in my opinion...",
                            "Let me explain how I handled a much bigger problem than yours...",
                            "So, if I understand you correctly, what you are saying is that...",
                            "Why would you ever think something like that?"
                        ],
                        "correct_answer": 2,
                        "explanation": "Option C is correct because it introduces a polite, structured reflection of the speaker's message without judgment, allowing the speaker to confirm or adjust the listener's comprehension. Option A is argumentative, Option B is conversational hijacking, and Option D is an aggressive interrogation."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Lesson 7 Summary & Key Takeaways",
                    "content": {
                        "text": "- **Interactive listening** transforms communication from a one-way monologue into a shared understanding.\n- **The 5-Stage Feedback Loop:** 1. Receive -> 2. Process -> 3. Paraphrase -> 4. Clarify -> 5. Respond.\n- **Paraphrasing stems** (*'If I understand correctly...'*) verify facts and build psychological trust.\n- **Empathetic validation** acknowledges speaker emotions before jumping to solutions."
                    }
                }
            ]
        ]
    }
]


# =============================================================================
# LESSONS 8, 9, AND 10 DEFINITIONS
# =============================================================================
TOPIC_1_LESSONS_8_TO_10 = [
    # =========================================================================
    # LESSON 8: Syllabic and Emphatic Stress
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Syllabic and Emphatic Stress",
        "unit_description": "Word-level stress shifting in two-syllable noun/verb pairs, and sentence-level emphatic/contrastive stress to convey specific meaning and nuance.",
        "lesson_title": "Syllabic and Emphatic Stress",
        "pages": [
            # -----------------------------------------------------------------
            # Page 1: Discovery & Objectives
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_image",
                    "title": "Acoustic Vocal Recording Studio Microphone",
                    "content": {
                        "title": "Acoustic Vocal Recording Studio Microphone",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Close_up_view_of_a_microphone_set_up_in_a_recording_studio.jpg",
                        "caption": "A studio condenser microphone set up in an acoustic recording studio, representing the acoustic pitch, volume, and syllable stress dynamics that shape spoken English.",
                        "author": "Lance Anderson / Wikimedia Commons",
                        "licensing": "CC BY 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define syllabic and emphatic stress in spoken English communication\n- Apply the disyllabic stress rule to distinguish between nouns/adjectives (first-syllable stress) and verbs (second-syllable stress)\n- Use sentence-level emphatic stress to shift focus, correct misunderstandings, and highlight contrastive meaning\n- Differentiate between stressed content words and unstressed function words in connected speech"
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 2: Core Concepts & Terminology
            # -----------------------------------------------------------------
            [
                {
                    "type": "definition_card",
                    "title": "Core Phonetic Terminology",
                    "content": {
                        "term": "Stress in English Speech",
                        "definition": "The extra acoustic force, higher musical pitch, lengthened duration, and full vowel quality given to a specific syllable in a word or a specific word in an utterance."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Syllabic vs. Emphatic Stress Principles",
                    "content": {
                        "text": "### 1. Acoustic Properties of Stress\nA stressed syllable or word in English is characterized by four simultaneous phonetic features:\n- **Pitch:** The voice tone jumps higher on the stressed syllable.\n- **Volume / Loudness:** Greater respiratory energy produces a louder sound.\n- **Duration / Length:** The vowel sound is held longer compared to unstressed syllables.\n- **Vowel Quality:** Stressed syllables maintain pure vowel sounds, while unstressed vowels often reduce to the weak schwa /ə/ or /ɪ/.\n\n### 2. Disyllabic Word Stress-Shift Rule\nMany English two-syllable words spelled identically shift stress according to grammatical function:\n- **Nouns & Adjectives:** Stress falls on the **first syllable** (e.g., *ˈRE-cord*, *ˈCON-duct*, *ˈPRE-sent*, *ˈOB-ject*).\n- **Verbs:** Stress falls on the **second syllable** (e.g., *re-ˈCORD*, *con-ˈDUCT*, *pre-ˈSENT*, *ob-ˈJECT*).\n\n### 3. Content vs. Function Words in Connected Speech\n- **Content Words (Stressed):** Nouns, main verbs, adjectives, adverbs, and demonstratives carry primary information.\n- **Function Words (Unstressed):** Prepositions, auxiliary verbs, articles, conjunctions, and personal pronouns are reduced to create English speech rhythm."
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 3: Model & Structured Analysis / Visual Diagram
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_diagram",
                    "title": "Syllabic & Emphatic Stress Architecture",
                    "content": {
                        "title": "Syllabic & Emphatic Stress Interactive Visualizer",
                        "caption": "Comprehensive diagram demonstrating the disyllabic noun-verb stress shift waveforms and the semantic transformation caused by moving emphatic focus in connected speech.",
                        "svg_content": SVG_LESSON_8_STRESS
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Disyllabic Stress Shift Reference Matrix",
                    "content": {
                        "headers": ["Word Base", "Noun Pattern (ˈ1st Syllable)", "Noun Example", "Verb Pattern (2nd ˈSyllable)", "Verb Example"],
                        "rows": [
                            ["conduct", "ˈCON-duct /ˈkɒn.dʌkt/", "His conduct in the laboratory was exemplary.", "con-ˈDUCT /kənˈdʌkt/", "She will conduct the student orchestra tonight."],
                            ["present", "ˈPRE-sent /ˈprɛz.ənt/", "He received a thoughtful birthday present.", "pre-ˈSENT /prɪˈzɛnt/", "The committee will present their findings tomorrow."],
                            ["export", "ˈEX-port /ˈɛks.pɔːt/", "Coffee is Kenya's primary agricultural export.", "ex-ˈPORT /ɪkˈspɔːt/", "Farmers export fresh cut flowers to Europe."],
                            ["contest", "ˈCON-test /ˈkɒn.tɛst/", "She won first prize in the national essay contest.", "con-ˈTEST /kənˈtɛst/", "The defense lawyer decided to contest the verdict."],
                            ["produce", "ˈPRO-duce /ˈprɒd.juːs/", "The market sells fresh organic farm produce.", "pro-ˈDUCE /prəˈdjuːs/", "The local solar plant will produce clean electricity."],
                            ["object", "ˈOB-ject /ˈɒb.dʒɪkt/", "A spherical object was discovered near the crater.", "ob-ˈJECT /əbˈdʒɛkt/", "Citizens object strongly to illegal logging."]
                        ]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 4: Media Integration & Listening Lab
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_video",
                    "title": "Mastering Emphatic Sentence Stress",
                    "content": {
                        "title": "How Sentence Stress Changes Meaning in English",
                        "youtube_id": "0VWvBk1fxuM",
                        "url": "https://www.youtube.com/watch?v=0VWvBk1fxuM",
                        "description": "Demonstration of how shifting emphatic pitch and volume on specific words creates contrast, emphasis, and dramatic communicative nuance.",
                        "pre_viewing_task": "Pre-Viewing Task: Before playing the video, read the sentence 'I never said she took the keys' and identify how stressing each individual word shifts the sentence meaning.",
                        "post_viewing_discussion": "Post-Viewing Discussion: Discuss with a partner how shifting emphatic stress on auxiliary verbs (e.g. 'I *did* submit the assignment') resolves ambiguity during formal disagreements."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Listening Lab & Contrastive Discrimination",
                    "content": {
                        "text": "### Listening Lab: The 5-Meaning Sentence Experiment\n**Pre-Viewing Focus:** Listen attentively to the demonstration and repeat each sentence below, placing extra pitch and volume on the capitalized word:\n\n1. ***I*** didn't say she stole my phone. *(Meaning: Someone else made the claim, not me.)*\n2. *I didn't **SAY** she stole my phone.* *(Meaning: I may have implied or written it, but never uttered it aloud.)*\n3. *I didn't say **SHE** stole my phone.* *(Meaning: Someone else took it, not that specific woman.)*\n4. *I didn't say she **STOLE** my phone.* *(Meaning: She might have borrowed or misplaced it, without criminal intent.)*\n5. *I didn't say she stole my **PHONE**.* *(Meaning: She took my tablet or money, but not my phone.)*\n\n**Post-Viewing Acoustic Practice & Discussion:** Partner with a classmate. Speaker A delivers one version with distinct emphatic stress; Speaker B identifies which of the 5 interpretations was intended without looking at the text. Discuss how emphatic stress resolves real-world courtroom and service ambiguities."
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 5: Common Mistakes & Guided Practice
            # -----------------------------------------------------------------
            [
                {
                    "type": "common_mistakes",
                    "title": "Common Stress Mistakes & Corrections",
                    "content": {
                        "mistakes": [
                            {
                                "incorrect": "Pronouncing every syllable with equal volume and duration (syllable-timed robotic cadence).",
                                "explanation": "English is a stress-timed language. Equal stress flattens rhythm, eliminates contrast, and strains listener comprehension.",
                                "correction": "Linger on stressed syllables with higher pitch, and smoothly glide through unstressed syllables using the weak schwa /ə/ sound."
                            },
                            {
                                "incorrect": "Stressing the first syllable of two-syllable verbs (e.g., saying 'ˈPRE-sent' when delivering a speech).",
                                "explanation": "Using noun stress for verbs signals grammatical confusion and distracts listeners during formal oral presentations.",
                                "correction": "Say 'pre-ˈSENT' for the action of giving or delivering, and reserve 'ˈPRE-sent' for the gift or current time."
                            },
                            {
                                "incorrect": "Over-stressing grammatical function words like 'to', 'of', 'and', 'the' in normal connected sentences.",
                                "explanation": "Function words serve syntactic linkage, not core semantic focus. Over-stressing them disrupts natural phrasing.",
                                "correction": "Keep function words unaccented (e.g., 'a cup of tea' pronounced /ə ˈkʌp əv ˈtiː/)."
                            }
                        ]
                    }
                },
                {
                    "type": "guided_practice",
                    "title": "Guided Practice: Stress Marking & Meaning Deduction",
                    "content": {
                        "instructions": "Read each sentence, determine whether the target word functions as a Noun or Verb, and mark the stressed syllable in bold capital letters:",
                        "tasks": [
                            {
                                "prompt": "1. The factory owners plan to [export / ex-port] horticultural goods to overseas markets.",
                                "solution": "Function: Verb. Correct Stress: ex-ˈPORT (/ɪkˈspɔːt/). Second syllable stressed."
                            },
                            {
                                "prompt": "2. Tea is the country's most valuable agricultural [export / ex-port].",
                                "solution": "Function: Noun. Correct Stress: ˈEX-port (/ˈɛks.pɔːt/). First syllable stressed."
                            },
                            {
                                "prompt": "3. The debate club will [contest / con-test] the adjudicator's preliminary score.",
                                "solution": "Function: Verb. Correct Stress: con-ˈTEST (/kənˈtɛst/). Second syllable stressed."
                            },
                            {
                                "prompt": "4. In the sentence 'MARY baked chocolate cookies yesterday', explain what the emphatic stress on 'MARY' implies.",
                                "solution": "Implied Meaning: Mary (and nobody else, such as Peter or Jane) was the person who baked the cookies."
                            }
                        ]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 6: Knowledge Check & Summary
            # -----------------------------------------------------------------
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Emphatic Contrastive Stress",
                    "content": {
                        "question": "Read this dialogue:\n\nSpeaker A: 'Did you purchase a blue blazer for the debate tournament?'\nSpeaker B: 'No, I purchased a green blazer.'\n\nWhich word in Speaker B's response carries the emphatic (contrastive) stress?",
                        "options": [
                            "No",
                            "I",
                            "green",
                            "blazer"
                        ],
                        "correct": "C",
                        "explanation": "'green' carries the emphatic/contrastive stress because it provides the vital new, corrective information that contrasts directly with Speaker A's erroneous assertion ('blue'). 'Blazer' is shared context and does not require focal stress."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Noun vs. Verb Stress Distinction",
                    "content": {
                        "question": "Choose the option that correctly identifies the stress placement in the following sentence:\n'The research team will [present] their [project] to the regional council.'",
                        "options": [
                            "pre-ˈSENT (verb, 2nd syllable) and ˈPRO-ject (noun, 1st syllable)",
                            "ˈPRE-sent (noun, 1st syllable) and pro-ˈJECT (verb, 2nd syllable)",
                            "ˈPRE-sent (verb, 1st syllable) and ˈPRO-ject (noun, 1st syllable)",
                            "pre-ˈSENT (verb, 2nd syllable) and pro-ˈJECT (verb, 2nd syllable)"
                        ],
                        "correct": "A",
                        "explanation": "'present' is functioning as a main verb in the predicate ('will present'), requiring second-syllable stress (pre-ˈSENT). 'project' functions as a direct object noun ('their project'), requiring first-syllable stress (ˈPRO-ject)."
                    }
                },
                {
                    "type": "summary_card",
                    "title": "Lesson 8 Key Takeaways",
                    "content": {
                        "text": "### Summary of Key Principles\n- **Stress Markers:** Characterized by higher pitch, greater volume, lengthened vowel duration, and full vowel articulation.\n- **Disyllabic Shift Rule:** Nouns and adjectives receive first-syllable stress (ˈRE-record), while corresponding verbs receive second-syllable stress (re-ˈCORD).\n- **Emphatic Sentence Stress:** Placing prominent pitch and loudness on a specific word directs listener attention, resolves ambiguity, and conveys exact pragmatic intent.\n- **Rhythm Mastery:** Stressed content words anchor the message, while unstressed function words maintain natural English cadence."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 9: Speaking Fluency: Conversation, Presentation, and Interview
    # =========================================================================
    {
        "unit_order": 9,
        "unit_name": "Speaking Fluency: Conversation, Presentation, and Interview",
        "unit_description": "The three pillars of spoken fluency—controlled pace, structured signposting, and active audience engagement—in casual, presentation, and interview settings.",
        "lesson_title": "Speaking Fluency: Conversation, Presentation, and Interview",
        "pages": [
            # -----------------------------------------------------------------
            # Page 1: Discovery & Objectives
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_image",
                    "title": "Academic Lecture Hall and Presentation Arena",
                    "content": {
                        "title": "Academic Lecture Hall and Presentation Arena",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/Grace_Knox_Lecture_Hall%2C_University_at_Buffalo_%28Buffalo%2C_NY_-_12-10-08%29.jpg",
                        "caption": "An academic lecture hall and stage environment where speakers apply fluency, structured signposting, and audience engagement to deliver impactful presentations.",
                        "author": "University at Buffalo / Wikimedia Commons",
                        "licensing": "CC BY 3.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 9 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define spoken fluency and differentiate between speed and communicative coherence\n- Apply the Three Pillars of Fluency: controlled pace, discourse signposting, and audience engagement\n- Structure presentations and interview responses using opening hooks, developmental transitions, and memorable conclusions\n- Eliminate verbal fillers ('um', 'uh', 'you know') using deliberate pauses and cohesive connectors"
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 2: Core Concepts & Terminology
            # -----------------------------------------------------------------
            [
                {
                    "type": "definition_card",
                    "title": "Fluency & Discourse Coherence",
                    "content": {
                        "term": "Spoken Fluency",
                        "definition": "The ability to produce spoken language easily, smoothly, and expressively without unnatural hesitation, stumbling, or cognitive disruption, maintaining clear logical flow and audience rapport."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Pillars of Speaking Fluency",
                    "content": {
                        "text": "### 1. Controlled Cadence & Pacing\n- **Target Speed:** 120 to 150 words per minute (WPM). Speaking too fast causes articulation slurring; speaking too slowly risks listener cognitive disengagement.\n- **The Strategic Pause:** Intentional 1-to-2 second pauses before key insights signal confidence, allow listeners to absorb complex ideas, and replace involuntary filler words.\n\n### 2. Discourse Signposting (Linguistic Roadmaps)\nSignposting words function like traffic signs guiding the listener through your line of reasoning:\n- **Introduction & Hooks:** *'Today, I would like to address...', 'Have you ever wondered why...?'*\n- **Sequencing & Addition:** *'First and foremost...', 'Furthermore...', 'In addition to this...'* \n- **Contrasting & Counter-arguments:** *'On the other hand...', 'However, from a practical standpoint...', 'Conversely...'* \n- **Synthesis & Concluding:** *'In conclusion...', 'To summarize our core findings...', 'Ultimately, the solution lies in...'* \n\n### 3. Audience Awareness & Register Calibration\n- **Register:** Adjusting linguistic formality (formal for panels/interviews, consultative for meetings, informal for peers).\n- **Paralanguage & Body Language:** Sustaining 3-second eye contact intervals, upright open posture, and animated vocal pitch modulation."
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 3: Model & Structured Analysis / Visual Diagram
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_diagram",
                    "title": "Speaking Fluency Triangle & Delivery Flowchart",
                    "content": {
                        "title": "The Fluency Architecture and Presentation Delivery Model",
                        "caption": "Diagram detailing the three pillars of spoken fluency alongside a step-by-step presentation delivery flowchart with concrete signposting phrases.",
                        "svg_content": SVG_LESSON_9_FLUENCY
                    }
                },
                {
                    "type": "worked_example",
                    "title": "Model Structured Response: School Prefect Selection Interview",
                    "content": {
                        "intro": "Compare the unprepared vs. signposted response to the panel prompt: 'Why are you the most suitable candidate for Senior School Academic Prefect?'",
                        "steps": [
                            "**Poor Response (Filler-Laden & Disorganized):** 'Uh... well... I think... like... I should be chosen because... um... I love books and... you know... my friends say I am smart and... uh... yeah, I will do my best.' *(Result: Unstructured, low credibility, excessive fillers.)*",
                            "**Stage 1 — The Hook & Direct Assertion:** 'Good morning, esteemed panel. I am eager to serve as Academic Prefect because I possess both the organizational discipline and peer-mentorship experience required to elevate our school's academic standards.'",
                            "**Stage 2 — Signposted Point 1 (Organization):** 'First and foremost, over the past year, I successfully coordinated the Grade 10 peer-study circles, which improved average science performance by 15%.'",
                            "**Stage 3 — Signposted Point 2 (Bridge-Building):** 'Second, I am a committed active listener who can bridge communication between students and faculty regarding study timetables and library resources.'",
                            "**Stage 4 — Signposted Conclusion:** 'In conclusion, my proven track record and collaborative mindset make me ready to serve our school community effectively. Thank you for your consideration.'"
                        ]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 4: Media Integration & Listening Lab
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_video",
                    "title": "Public Speaking & Fluency Delivery Masterclass",
                    "content": {
                        "title": "How to Speak with Confidence and Fluency",
                        "youtube_id": "XAIoSYqzGkY",
                        "url": "https://www.youtube.com/watch?v=XAIoSYqzGkY",
                        "description": "Techniques for controlling breath support, pacing, eliminating verbal crutches, and structuring live presentations with authority.",
                        "pre_viewing_task": "Pre-Viewing Task: Identify 3 verbal crutches (e.g. 'um', 'like', 'you know') you personally use when speaking under pressure.",
                        "post_viewing_discussion": "Post-Viewing Discussion: Analyze how professional speakers use a 2-second silent pause rather than filler words to command audience attention."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Fluency Lab: The Speech Shadowing Technique",
                    "content": {
                        "text": "### Practice Protocol: Speech Shadowing\n**Speech Shadowing** is a scientifically proven technique where learners listen to an expert orator and repeat what they say in real time with a delay of only a fraction of a second.\n\n1. **Step 1 (Pre-Viewing Ear Tuning):** Listen to a 60-second audio excerpt of a professional speech twice without speaking. Note the cadence, breathing pauses, and pitch peaks.\n2. **Step 2 (Simultaneous Shadowing):** Play the audio a third time and speak along aloud immediately behind the speaker, matching their speed, rhythm, and stress.\n3. **Step 3 (Independent Production & Post-Viewing Discussion):** Record yourself delivering the same paragraph from memory. Check for clear signposting and zero filler sounds. Discuss your recording with a peer."
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 5: Common Mistakes & Guided Practice
            # -----------------------------------------------------------------
            [
                {
                    "type": "common_mistakes",
                    "title": "Fluency Traps & How to Overcome Them",
                    "content": {
                        "mistakes": [
                            {
                                "incorrect": "Speaking in a flat, monotone pitch throughout an entire speech or interview.",
                                "explanation": "Monotone delivery signals disinterest and causes listener auditory fatigue, regardless of how strong the content is.",
                                "correction": "Modulate your pitch upwards for exciting points and downward for decisive, authoritative conclusions."
                            },
                            {
                                "incorrect": "Memorizing full paragraphs verbatim, leading to panic and complete mental blocks if one word is forgotten.",
                                "explanation": "Verbatim recitation sounds mechanical and leaves the speaker vulnerable to catastrophic freezing under anxiety.",
                                "correction": "Memorize only your outline skeleton and signposting transition words; formulate the exact sentences dynamically."
                            },
                            {
                                "incorrect": "Rushing through sentences without pausing in order to finish speaking quickly.",
                                "explanation": "Rapid-fire speech causes mispronunciation, swallows consonant endings, and communicates severe nervousness.",
                                "correction": "Embrace the silent pause. Take a calm breath between major points to reset pacing."
                            }
                        ]
                    }
                },
                {
                    "type": "guided_practice",
                    "title": "Guided Practice: Filler Word Elimination & 1-Minute Challenge",
                    "content": {
                        "instructions": "Transform disorganized statements and execute the timed fluency exercise:",
                        "tasks": [
                            {
                                "prompt": "1. Revise this filler-laden sentence: 'I... um... want to study engineering because... like... building bridges is... you know... really cool and... uh... helps Kenya.'",
                                "solution": "Revision: 'I aspire to study civil engineering because designing modern infrastructure directly transforms our national transport networks and uplifts local communities.'"
                            },
                            {
                                "prompt": "2. Identify three distinct signposting transition words used to contrast opposing viewpoints.",
                                "solution": "Transitions: (1) 'However...', (2) 'On the contrary / Conversely...', (3) 'On the other hand...'"
                            },
                            {
                                "prompt": "3. The 1-Minute Impromptu Challenge Protocol:",
                                "solution": "Select a topic ('The Power of Tree Planting', 'Why Mathematics is Essential', 'The Value of Teamwork'). Speak continuously for 60 seconds without saying 'um', 'uh', or 'like'. Use at least three formal signposts ('First...', 'Moreover...', 'In summary...')."
                            }
                        ]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 6: Knowledge Check & Summary
            # -----------------------------------------------------------------
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Signposting Function Identification",
                    "content": {
                        "question": "A student begins their speech section with: 'Having examined the ecological benefits of renewable solar energy, let us now turn our attention to the financial costs of installation.'\n\nWhich signposting function does this statement perform?",
                        "options": [
                            "Opening Hook & Purpose Statement",
                            "Discourse Transition & Internal Summary",
                            "Aggressive Opposition Rebuttal",
                            "Final Call to Action"
                        ],
                        "correct": "B",
                        "explanation": "The statement acts as an internal transition and roadmap connector: it briefly summarizes what was just discussed ('Having examined...') and explicitly directs the audience's attention to the next developmental sub-topic ('...let us now turn our attention to...')."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Best Strategy for Spoken Fluency in Interviews",
                    "content": {
                        "question": "During a senior school leadership interview, a candidate is asked an unexpected, complex question. What is the most fluent and professional course of action?",
                        "options": [
                            "Immediately begin talking rapidly without stopping, filling all pauses with 'um' and 'like' to show quickness.",
                            "Remain completely silent for 30 seconds with downcast eyes while feeling embarrassed.",
                            "Take a calm breath, pause for two seconds to formulate key points, and use a structured signpost to begin.",
                            "Recite a memorized poem about leadership to avoid answering the specific question asked."
                        ],
                        "correct": "C",
                        "explanation": "Confident, fluent speakers utilize deliberate 1-to-2 second pauses to organize their thoughts mentally and then open with clear signposting ('That is a thoughtful question; I would approach this issue from two perspectives...'). This demonstrates emotional composure and intellectual clarity."
                    }
                },
                {
                    "type": "summary_card",
                    "title": "Lesson 9 Key Takeaways",
                    "content": {
                        "text": "### Summary of Key Principles\n- **Fluency vs. Speed:** Fluency is about smoothness, structural coherence, and audience clarity, not rapid speech.\n- **Signposting Power:** Using transition markers (*First*, *However*, *In conclusion*) guides listener understanding and prevents cognitive fatigue.\n- **Pause Control:** Replacing fillers (*um, like, you know*) with deliberate 1-second silent pauses projects composure and authority.\n- **Active Delivery:** Maintain purposeful eye contact, upright posture, and expressive vocal modulation across conversations, presentations, and interviews."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 10: Meetings, Discussions, Debate, and Oral Decision-making
    # =========================================================================
    {
        "unit_order": 10,
        "unit_name": "Meetings, Discussions, Debate, and Oral Decision-making",
        "unit_description": "Parliamentary procedures, agenda-driven formal meetings, minutes recording, debate motions, polite rebuttals, and consensus-building.",
        "lesson_title": "Meetings, Discussions, Debate, and Oral Decision-making",
        "pages": [
            # -----------------------------------------------------------------
            # Page 1: Discovery & Objectives
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_image",
                    "title": "Parliamentary Hemicycle Chamber and Debate Assembly",
                    "content": {
                        "title": "Parliamentary Hemicycle Chamber and Debate Assembly",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/dc/First_European_Parliament_Hemicycle%2C_Robert_Schuman_building%2C_1973.jpg",
                        "caption": "A formal parliamentary assembly chamber showing structured seating, chairperson moderation, and formal debate proceedings for collective oral decision-making.",
                        "author": "Archivio Ceccarelli / Wikimedia Commons",
                        "licensing": "CC BY-SA 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 10 Learning Objectives",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the core governance roles in formal meetings (Chairperson, Secretary, Members)\n- Follow parliamentary meeting procedures, including agenda adherence and minutes compilation\n- Table, second, and debate formal motions using standard diplomatic terminology\n- Formulate persuasive, evidence-based rebuttals without resorting to ad hominem attacks\n- Facilitate oral decision-making through voting and consensus-building"
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 2: Core Concepts & Terminology
            # -----------------------------------------------------------------
            [
                {
                    "type": "definition_card",
                    "title": "Parliamentary Governance & Meeting Terminology",
                    "content": {
                        "term": "Formal Meeting & Debate Procedure",
                        "definition": "A structured, rules-based oral forum governed by parliamentary etiquette where participants deliberate over an agenda, evaluate competing motions, and make binding collective decisions."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Key Governance Roles & Parliamentary Vocabulary",
                    "content": {
                        "text": "### 1. Key Meeting Roles\n- **Chairperson (The Chair):** Leads the session, enforces the agenda, maintains order, grants speaking turns, and remains neutral during debate.\n- **Secretary:** Circulates notice and agenda in advance, records attendances, compiles official **Minutes**, and documents resolutions and voting tallies.\n- **Members / Delegates:** Propose motions, participate in structured turn-taking, present arguments with evidence, and cast votes.\n\n### 2. Core Parliamentary Vocabulary\n- **Agenda:** The sequential schedule of business items distributed prior to the meeting.\n- **Minutes:** The legal, written record summarizing discussions, motions passed, and action items assigned.\n- **Motion:** A formal proposal moved by a member for debate and vote (e.g., *'I move that the club allocate KES 5,000 for library books'*).\n- **Seconding:** Formal verbal support from a second member (*'I second the motion'*), without which a motion cannot be debated.\n- **Consensus:** A collective unanimous or broad agreement achieved through negotiation rather than division.\n- **Rebuttal:** A logical, evidence-based counter-argument designed to disprove an opponent's claim in a debate."
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 3: Model & Structured Analysis / Visual Diagram
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_diagram",
                    "title": "Formal Meeting Roles & 5-Stage Decision Cycle",
                    "content": {
                        "title": "Parliamentary Governance and Oral Decision Architecture",
                        "caption": "Diagram illustrating the division of responsibilities among the Chair, Secretary, and Members, alongside the 5-stage parliamentary decision-making cycle.",
                        "svg_content": SVG_LESSON_10_MEETINGS_DEBATE
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 5-Stage Meeting & Debate Procedure",
                    "content": {
                        "intro": "Standard parliamentary procedure follows five sequential stages to ensure fair, transparent, and binding decisions:",
                        "steps": [
                            {
                                "title": "Stage 1: Call to Order & Agenda Adoption",
                                "description": "The Chairperson calls the meeting to order, confirms quorum, reviews previous minutes, and adopts today's agenda."
                            },
                            {
                                "title": "Stage 2: Tabling and Seconding the Motion",
                                "description": "A member introduces a formal motion ('I move that...'). Another member seconds it ('I second the motion'). If unseconded, the motion lapses."
                            },
                            {
                                "title": "Stage 3: Controlled Floor Debate",
                                "description": "The Chair opens the floor, alternating speaking turns between proposition supporters and opposition skeptics. Speakers always address the Chair ('Mr. Chair, through you...')."
                            },
                            {
                                "title": "Stage 4: Diplomatic Rebuttals & Amendments",
                                "description": "Members challenge premises with facts, proposing amendments if necessary to forge a middle ground or consensus."
                            },
                            {
                                "title": "Stage 5: Voting, Resolution & Minutes Signing",
                                "description": "The Chair calls for a vote ('All those in favor say Aye...'). The Secretary records the outcome, and the Chair signs the approved resolutions."
                            }
                        ]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 4: Media Integration & Listening Lab
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_video",
                    "title": "Mastering Meeting Etiquette and Disagreement",
                    "content": {
                        "title": "How to Disagree Politely and Lead Effective Meetings",
                        "youtube_id": "lO1gpzakbik",
                        "url": "https://www.youtube.com/watch?v=lO1gpzakbik",
                        "description": "Strategies for de-escalating interpersonal tension, using active listening in team debates, and reaching consensus.",
                        "pre_viewing_task": "Pre-Viewing Task: Note down the specific diplomatic phrasing used to disagree with a colleague without being offensive.",
                        "post_viewing_discussion": "Post-Viewing Discussion: Debate with a classmate why parliamentary procedure mandates addressing the Chairperson rather than the opposing debater directly."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Debate Lab: Parliamentary Dialogue Model",
                    "content": {
                        "text": "### Model Debate: Should AI Writing Tools Be Permitted in Schoolwork?\nStudy how debaters address the Chair and present polite, structured arguments:\n\n*   **Speaker 1 (Proposition):** *'Madam Speaker, integrating AI writing tools fosters 21st-century digital literacy. First, AI acts as an accessible grammar tutor that provides instant feedback to developing writers. Second, learning to evaluate AI suggestions cultivates critical editing skills.'*\n*   **Speaker 2 (Opposition / Rebuttal):** *'Madam Speaker, while I acknowledge my colleague's vision for digital literacy, I respectfully counter that unchecked AI reliance erodes foundational writing capabilities. First, learners bypass the cognitive effort required to synthesize arguments independently. Second, it creates unequal access for students without reliable internet connections.'*\n\n**Pre-Viewing Analysis:** Note how Speaker 2 acknowledged the opponent's premise before presenting counter-evidence, maintaining total respect and formal register.\n\n**Post-Viewing Debate Discussion:** In pairs, stage a 2-minute mock debate using parliamentary address ('Mr./Madam Speaker') on a contemporary school issue."
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 5: Common Mistakes & Guided Practice
            # -----------------------------------------------------------------
            [
                {
                    "type": "common_mistakes",
                    "title": "Meeting & Debate Misconceptions to Avoid",
                    "content": {
                        "mistakes": [
                            {
                                "incorrect": "Interrupting a speaker while they are holding the floor.",
                                "explanation": "Cross-talking and interruptions cause meeting chaos, disrespect the speaker, and violate parliamentary decorum.",
                                "correction": "Wait until the speaker concludes, raise your hand, and wait for the Chairperson to grant you the floor."
                            },
                            {
                                "incorrect": "Using ad hominem attacks (attacking the person instead of the argument, e.g., 'You don't understand anything').",
                                "explanation": "Personal attacks destroy professional credibility and provoke defensive emotional confrontations.",
                                "correction": "Focus exclusively on data and logical analysis: 'I respectfully disagree with the projected cost because government tax reports show a lower estimate.'"
                            },
                            {
                                "incorrect": "Speaking directly to an opposing debater in an aggressive tone.",
                                "explanation": "Direct arguments between delegates cause emotional friction and undermine the neutrality of the forum.",
                                "correction": "Always channel remarks through the presiding officer: 'Mr. Chairman, in response to the point raised by delegate Sarah...'"
                            }
                        ]
                    }
                },
                {
                    "type": "guided_practice",
                    "title": "Guided Practice: Diplomatic Rebuttal Maker & Meeting Simulation",
                    "content": {
                        "instructions": "Transform offensive, unparliamentary statements into diplomatic, professional rebuttals:",
                        "tasks": [
                            {
                                "prompt": "1. Unparliamentary: 'Your budget proposal is ridiculous and a total waste of school funds.'",
                                "solution": "Diplomatic Rebuttal: 'Mr. Chairman, while I appreciate the intent behind the proposal, I am concerned that the projected expenditures exceed our available reserve fund. I recommend we explore a phased implementation.'"
                            },
                            {
                                "prompt": "2. Unparliamentary: 'Be quiet and let me speak; you've talked too much.'",
                                "solution": "Diplomatic Rebuttal: 'Point of order, Madam Chair. I believe my speaking time has not yet elapsed. May I please finish my statement before comments are invited from the floor?'"
                            },
                            {
                                "prompt": "3. Roleplay Scenario (The Environmental Club Meeting):",
                                "solution": "Form a 4-person panel: Chair, Secretary, Proposition Delegate, Opposition Delegate. Agenda: 'Motion to ban single-use plastic bottles on school campus'. Execute a 3-minute debate following parliamentary stages, and record final resolutions in writing."
                            }
                        ]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Page 6: Knowledge Check & Summary
            # -----------------------------------------------------------------
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Primary Responsibility of the Secretary",
                    "content": {
                        "question": "What is the primary official responsibility of the secretary during a formal committee meeting?",
                        "options": [
                            "To make all final policy decisions on behalf of the committee",
                            "To accurately record the proceedings, motions, votes, and resolutions in the official minutes",
                            "To argue in favor of every motion tabled by members",
                            "To interrupt members whenever they speak for more than two minutes"
                        ],
                        "correct": "B",
                        "explanation": "The secretary's primary constitutional duty is to maintain the official legal record of the meeting by drafting clear, accurate, and objective minutes documenting attendances, motions tabled, voting outcomes, and action assignments."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Diplomatic Parliamentary Protocol",
                    "content": {
                        "question": "During a debate on the school budget, a delegate wishes to challenge an opponent's statistical claim. Which of the following represents the most appropriate parliamentary language?",
                        "options": [
                            "'Hey, everyone knows your numbers are completely fake!'",
                            "'Mr. Chairman, through you, I would like to present recent audit figures that contradict my colleague's estimates.'",
                            "'You have no idea how economics works, so please sit down.'",
                            "'I refuse to listen to this speaker because I dislike their attitude.'"
                        ],
                        "correct": "B",
                        "explanation": "Option B exemplifies correct parliamentary protocol: it addresses the Chairperson formally ('Mr. Chairman, through you...'), maintains professional courtesy toward the colleague, and introduces objective empirical evidence ('recent audit figures') rather than resorting to emotional insults."
                    }
                },
                {
                    "type": "summary_card",
                    "title": "Lesson 10 Key Takeaways",
                    "content": {
                        "text": "### Summary of Key Principles\n- **Governance Roles:** The Chairperson directs order and turn-taking; the Secretary records legal minutes and action items; members deliberate motions.\n- **Parliamentary Steps:** Meetings strictly adhere to the 5 stages: Call to Order -> Tabling & Seconding Motions -> Controlled Debate -> Rebuttals & Amendments -> Voting & Resolution.\n- **Diplomatic Protocol:** Debate the idea, never attack the person. Address all comments through the Chair using polite, evidence-based language.\n- **Oral Decision-Making:** Strive for collaborative consensus, and enforce transparent voting for binding collective outcomes."
                    }
                }
            ]
        ]
    }
]

