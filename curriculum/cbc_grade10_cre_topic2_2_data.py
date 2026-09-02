"""
VLearn CBC Grade 10 CRE — Sub-Strand 2.2: Infancy and Early Life of Jesus Christ
Comprehensive Structured Curriculum Data
"""

TOPIC_2_2_DATA = {
    "topic_order": 12,
    "topic_name": "Sub-Strand 2.2: Infancy and Early Life of Jesus Christ",
    "topic_description": "Explores the prophetic promises of the Messiah, the transitional ministry of John the Baptist, Jesus' birth, boyhood in Nazareth, baptism in the Jordan, and triumph over wilderness temptation.",
    "grade_name": "Grade 10",
    "subject_name": "CRE",
    "subject_id": 46,
}

TOPIC_2_2_LESSONS = [
    # -------------------------------------------------------------------------
    # UNIT 1: Fulfilment of Old Testament Prophecies
    # -------------------------------------------------------------------------
    {
        "unit_order": 1,
        "unit_name": "2.2.1 Fulfilment of Old Testament Prophecies",
        "unit_description": "Examine the Old Testament prophetic promises regarding the Messiah and their historical fulfillment in the birth and mission of Jesus Christ.",
        "lesson_title": "Fulfilment of Old Testament Prophecies",
        "pages": [
            # Page 1: Hook, Goals, Intro
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Hook: The Grotto of the Nativity in Bethlehem",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/The_Prophet_Isaiah_by_Michelangelo_Buonarroti.jpg/800px-The_Prophet_Isaiah_by_Michelangelo_Buonarroti.jpg",
                        "title": "Visual Hook: The Prophet Isaiah Foretelling the Messiah",
                        "author": "Michelangelo Buonarroti (Sistine Chapel)",
                        "licensing": "Public Domain",
                        "source": "Wikimedia Commons",
                        "caption": "Michelangelo's depiction of the Prophet Isaiah, who centuries before Christ foretold the Virgin Birth (Isaiah 7:14) and the Suffering Servant (Isaiah 53)."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Old Testament Prophetic Fulfilment",
                    "content": {
                        "goals": [
                            "Explain how the birth, infancy, and mission of Jesus Christ fulfilled specific Old Testament prophecies.",
                            "Analyze key prophecies from Isaiah and Micah concerning Immanuel, Bethlehem, and the Suffering Servant.",
                            "Evaluate the theological significance of the Incarnation and God's sovereign orchestration of history."
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Introduction: Connecting the Clues of Scripture",
                    "content": {
                        "markdown": "Have you ever read a mystery novel where a minor clue mentioned on page 10 suddenly unlocks the grand mystery on page 300? The relationship between the Old and New Testaments is designed in precisely that way.\n\nThe Old Testament is an inspired repository of divine promises, shadows, and specific prophetic markers pointing forward to a coming Redeemer—the **Messiah** (Hebrew: *Mashiach*, meaning 'The Anointed One'). The New Testament documents the historical reality of how those ancient promises were fulfilled in the person and life of **Jesus Christ**."
                    }
                }
            ],
            # Page 2: Core Scripture Study
            [
                {
                    "type": "concept_explanation",
                    "title": "Core Prophecies: From Ancient Promise to Historical Reality",
                    "content": {
                        "markdown": "Old Testament prophets spoke divine truth directly to their contemporary generation while simultaneously predicting future milestones in God's redemptive plan.\n\n### 1. Isaiah 7:14 — The Virgin Birth and Immanuel\n- **The Old Testament Promise:** God promised king Ahaz a miraculous sign: *'The virgin will conceive and give birth to a son, and will call him Immanuel.'*\n- **The New Testament Fulfilment:** In Luke 1:26-38 and Matthew 1:18-25, the Angel Gabriel announces to Mary that she will miraculously conceive through the power of the Holy Spirit while remaining a virgin.\n- **Theological Depth:** *Immanuel* translates to 'God with us'. This represents the **Incarnation**—the infinite Creator stepping into human history in human flesh.\n\n### 2. Micah 5:2 — The Obscurity of Bethlehem\n- **The Old Testament Promise:** The prophet Micah identified the humble village of Bethlehem Ephrathah as the specific birthplace of Israel's eternal ruler.\n- **The New Testament Fulfilment:** In Luke 2:1-7, Roman Emperor Caesar Augustus issued a decree for a worldwide census. Joseph and Mary were forced to travel from Nazareth to Bethlehem, where Jesus was born in a manger.\n\n### 3. Isaiah 9:1-7 — The Light in Galilee\n- **The Promise:** Galilee of the Gentiles, historically a region under oppression and darkness, was promised a great light and a righteous Prince of Peace.\n- **The Fulfilment:** In Luke 4:14-15, Jesus returned in the power of the Holy Spirit to Galilee, inaugurating His public ministry of teaching, healing, and kingdom transformation.\n\n### 4. Isaiah 53 — The Suffering Servant\n- **The Promise:** Isaiah portrayed a servant who would bear human griefs, be pierced for our transgressions, and bring healing through His wounds.\n- **The Fulfilment:** In Luke 22-23 and John 19, Jesus endured arrest, unjust trials, scourging, and crucifixion, offering His life as a redemptive sacrifice for humanity's sins."
                    }
                }
            ],
            # Page 3: Pedagogical Diagram & Deeper Insights
            [
                {
                    "type": "suggested_diagram",
                    "title": "Messianic Prophecy & Luke Fulfilment Matrix",
                    "content": {
                        "caption": "Pedagogical matrix illustrating the four foundational Old Testament prophecies and their exact historical fulfilment in the Gospel narratives.",
                        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="450" rx="12" fill="url(#bgGrad1)"/>
  <rect x="15" y="15" width="770" height="420" rx="10" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4"/>

  <!-- Header Section -->
  <rect x="40" y="30" width="720" height="50" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="55" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#f8fafc" text-anchor="middle">OLD TESTAMENT MESSIANIC PROPHECY &amp; GOSPEL FULFILMENT</text>
  <text x="400" y="72" font-family="Arial, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Connecting the Divine Blueprint to the Historical Incarnation</text>

  <!-- Column Headers -->
  <rect x="40" y="95" width="345" height="30" rx="6" fill="#3b82f6" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1"/>
  <text x="212" y="115" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">OLD TESTAMENT PROMISE (THE SHADOW)</text>

  <rect x="415" y="95" width="345" height="30" rx="6" fill="#10b981" fill-opacity="0.2" stroke="#34d399" stroke-width="1"/>
  <text x="587" y="115" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">GOSPEL FULFILMENT (THE REALITY)</text>

  <!-- Row 1: Virgin Birth -->
  <g transform="translate(40, 135)">
    <rect width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Isaiah 7:14</text>
    <text x="15" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">The Virgin shall conceive Immanuel ("God with us")</text>

    <!-- Connector Arrow -->
    <path d="M 345 30 L 375 30" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="360" cy="30" r="4" fill="#fbbf24"/>

    <rect x="375" width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#34d399" stroke-width="1"/>
    <text x="390" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Luke 1:26-38; Matthew 1:18-25</text>
    <text x="390" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Gabriel's annunciation; Mary conceives by Holy Spirit</text>
  </g>

  <!-- Row 2: Bethlehem Birthplace -->
  <g transform="translate(40, 205)">
    <rect width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Micah 5:2</text>
    <text x="15" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Ruler of Israel to emerge from tiny Bethlehem Ephrathah</text>

    <path d="M 345 30 L 375 30" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="360" cy="30" r="4" fill="#fbbf24"/>

    <rect x="375" width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#34d399" stroke-width="1"/>
    <text x="390" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Luke 2:1-7; Matthew 2:1-6</text>
    <text x="390" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Caesar's census brings Joseph &amp; Mary to Bethlehem birth</text>
  </g>

  <!-- Row 3: Light in Galilee -->
  <g transform="translate(40, 275)">
    <rect width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Isaiah 9:1-7</text>
    <text x="15" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Great light dawns upon Galilee; Prince of Peace promised</text>

    <path d="M 345 30 L 375 30" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="360" cy="30" r="4" fill="#fbbf24"/>

    <rect x="375" width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#34d399" stroke-width="1"/>
    <text x="390" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Luke 4:14-15; Matthew 4:12-17</text>
    <text x="390" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Jesus launches public ministry of light across Galilee</text>
  </g>

  <!-- Row 4: Suffering Servant -->
  <g transform="translate(40, 345)">
    <rect width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Isaiah 53:3-7</text>
    <text x="15" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Servant pierced for transgressions; quiet in suffering</text>

    <path d="M 345 30 L 375 30" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="360" cy="30" r="4" fill="#fbbf24"/>

    <rect x="375" width="345" height="60" rx="6" fill="url(#cardGrad1)" stroke="#34d399" stroke-width="1"/>
    <text x="390" y="25" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#f8fafc">Luke 22-23; John 19</text>
    <text x="390" y="45" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Christ's trial, crucifixion, and redemptive death on cross</text>
  </g>

  <!-- Central Badge Footer -->
  <rect x="260" y="415" width="280" height="22" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
  <text x="400" y="430" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#cbd5e1" text-anchor="middle">SOVEREIGN DESIGN: HARMONY OF SCRIPTURE</text>
</svg>"""
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Theological Insights: Sovereignty and Humility",
                    "content": {
                        "markdown": "### Key Theological Lessons from Prophetic Fulfilment:\n\n1. **God Rules Over Secular Empires:** Mary and Joseph did not choose to travel to Bethlehem as a planned vacation. An imperial Roman decree by Caesar Augustus forced them on a rigorous 140-kilometer journey. God sovereignly used secular political decrees to fulfill Micah 5:2 down to the exact geographical coordinates.\n\n2. **The Principle of Divine Humility:** When human rulers make announcements, they choose capitals like Rome or Jerusalem. God bypassed imperial palaces and selected an impoverished teenage girl in Nazareth and a rustic animal feeding trough in Bethlehem. God consistently exalts what the world deems humble and insignificant."
                    }
                }
            ],
            # Page 4: Video and Reflection
            [
                {
                    "type": "suggested_video",
                    "title": "BibleProject: Gospel of Luke Summary (Part 1)",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=26z_Khwaxyg",
                        "youtube_id": "26z_Khwaxyg",
                        "title": "BibleProject: Gospel of Luke Summary (Part 1)",
                        "description": "Visual walkthrough of Luke chapters 1-9 illustrating how Jesus' birth and arrival fulfilled Israel's messianic story."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Spiritual Reflection: God Keeps Every Promise",
                    "content": {
                        "markdown": "Between the final words of Malachi in the Old Testament and the opening events of Luke's Gospel, approximately 400 years of silence passed—often called the intertestamental period. Many in Israel wondered if God had forgotten His covenant promises.\n\nThe fulfillment of messianic prophecy proves that **God's timing is perfect**. Just as God remained faithful across centuries to bring forth the Messiah, Christians can trust God's promises in their personal lives today, even when circumstances seem silent or delayed."
                    }
                }
            ],
            # Page 5: Critical Thinking / Ethical Dilemma
            [
                {
                    "type": "step_process",
                    "title": "Critical Thinking Challenge: Refuting the Coincidence Argument",
                    "content": {
                        "title": "Critical Thinking Challenge: Refuting the Coincidence Argument",
                        "steps": [
                            "Identify the Skeptic's Claim: A skeptic argues that Jesus' birth in Bethlehem was merely a lucky geographical coincidence rather than divine prophecy.",
                            "Examine Historical Evidence: Analyze the historical circumstances in Luke 2:1-7—Joseph and Mary resided in Nazareth and had no personal reason to move, but were forced to Bethlehem due to Caesar Augustus' empire-wide census.",
                            "Synthesize Prophetic Convergence: Note how Micah 5:2 specified Bethlehem over 700 years prior, while Isaiah 7:14 specified a virgin mother, converging independently in one historical event.",
                            "Formulate Apologetic Defense: Conclude that God sovereignly orchestrates global political events to fulfill His redemptive promises exactly as foretold."
                        ]
                    }
                }
            ],
            # Page 6: Summary & Knowledge Check
            [
                {
                    "type": "key_takeaway",
                    "title": "Summary Takeaways: Old Testament Prophecies Fulfilled",
                    "content": {
                        "markdown": "The Old Testament contains precise prophetic markers foretelling the Messiah's virgin birth (Isaiah 7:14), Bethlehem birthplace (Micah 5:2), Galilean ministry of light (Isaiah 9:1-7), and suffering servant redemption (Isaiah 53). These converge perfectly in the Gospel narratives, confirming Jesus as the promised Savior."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Check Your Understanding: Prophetic Fulfilment",
                    "content": {
                        "question": "Which Old Testament prophet specifically identified the town of Bethlehem Ephrathah as the birthplace of Israel's future eternal Ruler?",
                        "options": [
                            "A) Isaiah 7:14",
                            "B) Micah 5:2",
                            "C) Malachi 3:1",
                            "D) Jeremiah 31:31"
                        ],
                        "answer": "B",
                        "explanation": "Micah 5:2 explicitly foretold that the ruler of Israel whose origins are from ancient times would come from Bethlehem Ephrathah, fulfilled when Jesus was born in Bethlehem (Luke 2:4-7)."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 2: The Role of John the Baptist as a Link
    # -------------------------------------------------------------------------
    {
        "unit_order": 2,
        "unit_name": "2.2.2 The Role of John the Baptist as a Covenant Link",
        "unit_description": "Analyze John the Baptist's unique position bridging the Old and New Testaments as the prophetic forerunner to the Messiah.",
        "lesson_title": "The Role of John the Baptist as a Covenant Link",
        "pages": [
            # Page 1: Hook, Goals, Intro
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Hook: The Wilderness of Judea",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Wadi_Qelt_in_the_Judean_Desert.jpg/800px-Wadi_Qelt_in_the_Judean_Desert.jpg",
                        "title": "Visual Hook: The Wilderness of Judea",
                        "author": "David Shankbone",
                        "licensing": "CC BY-SA 3.0",
                        "source": "Wikimedia Commons",
                        "caption": "The rugged terrain of the Judean Desert (Wadi Qelt), where John the Baptist lived in ascetic dedication, fulfilling the prophetic call of a voice in the wilderness."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: John the Baptist as the Covenant Link",
                    "content": {
                        "goals": [
                            "Explain the biblical concept of John the Baptist as the transitional bridge between the Old and New Testaments.",
                            "Identify Old Testament prophecies in Isaiah and Malachi that foretold John's identity and heraldic ministry.",
                            "Evaluate John's exemplary character traits of humility, courage, and singleness of purpose."
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Introduction: The Bridge Across Two Covenants",
                    "content": {
                        "markdown": "Imagine a massive bridge spanning a wide canyon. On the left cliff sits the **Old Testament** (the Old Covenant of the Mosaic Law, sacrificial rituals, and prophetic anticipation). On the right cliff sits the **New Testament** (the New Covenant of divine grace, forgiveness, and eternal salvation in Jesus Christ).\n\nStanding directly at the center of this monumental bridge is a rugged, fearless prophet clothed in camel's hair with a leather belt: **John the Baptist**. He stands on the borderline between the ages, bringing the Old Covenant era of anticipation to its climax and introducing the King of the New Covenant."
                    }
                }
            ],
            # Page 2: Prophetic Identity & Forerunner Role
            [
                {
                    "type": "concept_explanation",
                    "title": "Prophetic Identity: The Herald Foretold",
                    "content": {
                        "markdown": "John the Baptist was not merely an eccentric desert preacher; he was the specific herald ordained by God and predicted by ancient prophets centuries in advance.\n\n### 1. The Voice in the Wilderness (Isaiah 40:3-5)\n- Isaiah prophesied: *'A voice of one calling: In the wilderness prepare the way for the Lord; make straight in the desert a highway for our God.'*\n- In ancient Near Eastern culture, when an emperor visited a province, advance crews were dispatched to clear boulder-strewn roads and level valleys. John fulfilled this role spiritually by leveling the pride of hearts through a baptism of repentance.\n\n### 2. The Covenant Messenger (Malachi 3:1)\n- Malachi foretold: *'I will send my messenger, who will prepare the way before me.'*\n- John served as the direct ambassador sent immediately before Yahweh's personal arrival in the Messiah.\n\n### 3. The Elijah of Promise (Malachi 4:5-6 & Luke 1:17)\n- Malachi predicted that God would send 'Elijah the prophet' before the great day of the Lord to turn the hearts of fathers to their children.\n- The Angel Gabriel revealed to Zechariah that John would go forth *'in the spirit and power of Elijah'*. Jesus later confirmed in Luke 7:27-28 and Matthew 11:14 that John was the fulfillment of this spiritual Elijah."
                    }
                }
            ],
            # Page 3: Pedagogical Diagram & Deeper Insights
            [
                {
                    "type": "suggested_diagram",
                    "title": "John the Baptist as the Covenant Bridge",
                    "content": {
                        "caption": "Pedagogical diagram showing John the Baptist bridging the Old Covenant of Law and Prophecy to the New Covenant of Grace and Salvation in Jesus Christ.",
                        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="oldCovGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ef4444" />
      <stop offset="100%" stop-color="#991b1b" />
    </linearGradient>
    <linearGradient id="newCovGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#065f46" />
    </linearGradient>
    <linearGradient id="johnGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
  </defs>

  <rect width="800" height="450" rx="12" fill="url(#bgGrad2)"/>
  <rect x="15" y="15" width="770" height="420" rx="10" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4"/>

  <!-- Title -->
  <text x="400" y="55" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#f8fafc" text-anchor="middle">JOHN THE BAPTIST: THE COVENANT BRIDGE</text>
  <text x="400" y="78" font-family="Arial, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Bridging Old Testament Anticipation and New Testament Fulfilment</text>

  <!-- Left Pillar: Old Testament -->
  <g transform="translate(50, 120)">
    <rect width="210" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="210" height="45" rx="8" fill="url(#oldCovGrad)"/>
    <text x="105" y="28" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">OLD COVENANT</text>
    
    <text x="15" y="75" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#fca5a5">• The Mosaic Law</text>
    <text x="25" y="95" font-family="Arial, sans-serif" font-size="11" fill="#cbd5e1">Moral demands &amp; boundaries</text>
    
    <text x="15" y="125" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#fca5a5">• Sacrificial System</text>
    <text x="25" y="145" font-family="Arial, sans-serif" font-size="11" fill="#cbd5e1">Temporary animal blood</text>
    
    <text x="15" y="175" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#fca5a5">• Prophetic Longing</text>
    <text x="25" y="195" font-family="Arial, sans-serif" font-size="11" fill="#cbd5e1">Isaiah 40 &amp; Malachi 3/4</text>
    
    <rect x="15" y="210" width="180" height="20" rx="4" fill="#334155"/>
    <text x="105" y="224" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">ANTICIPATION</text>
  </g>

  <!-- Right Pillar: New Testament -->
  <g transform="translate(540, 120)">
    <rect width="210" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="210" height="45" rx="8" fill="url(#newCovGrad)"/>
    <text x="105" y="28" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">NEW COVENANT</text>
    
    <text x="15" y="75" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#6ee7b7">• Grace and Truth</text>
    <text x="25" y="95" font-family="Arial, sans-serif" font-size="11" fill="#cbd5e1">Incarnate in Jesus Christ</text>
    
    <text x="15" y="125" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#6ee7b7">• Permanent Atonement</text>
    <text x="25" y="145" font-family="Arial, sans-serif" font-size="11" fill="#cbd5e1">The Lamb of God sacrifice</text>
    
    <text x="15" y="175" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#6ee7b7">• Kingdom Reality</text>
    <text x="25" y="195" font-family="Arial, sans-serif" font-size="11" fill="#cbd5e1">Holy Spirit indwelling</text>
    
    <rect x="15" y="210" width="180" height="20" rx="4" fill="#334155"/>
    <text x="105" y="224" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">FULFILMENT</text>
  </g>

  <!-- Center Bridge Arch -->
  <path d="M 260 220 Q 400 130 540 220" stroke="#f59e0b" stroke-width="6" fill="none"/>
  <path d="M 260 240 Q 400 150 540 240" stroke="#64748b" stroke-width="3" stroke-dasharray="6 4" fill="none"/>

  <!-- Center Hub: John the Baptist -->
  <g transform="translate(325, 150)">
    <rect width="150" height="170" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="75" cy="45" r="30" fill="url(#johnGrad)"/>
    <text x="75" y="42" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">JOHN THE</text>
    <text x="75" y="55" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">BAPTIST</text>
    
    <text x="75" y="95" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">THE FORERUNNER</text>
    <text x="75" y="115" font-family="Arial, sans-serif" font-size="9" fill="#cbd5e1" text-anchor="middle">"Behold, the Lamb</text>
    <text x="75" y="128" font-family="Arial, sans-serif" font-size="9" fill="#cbd5e1" text-anchor="middle">of God!" (John 1:29)</text>
    <text x="75" y="148" font-family="Arial, sans-serif" font-size="9" font-style="italic" fill="#94a3b8" text-anchor="middle">"He must increase..."</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="180" y="390" width="440" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="410" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">TRANSITIONAL KEYSTONE: LAST OLD TESTAMENT PROPHET &amp; FIRST NEW TESTAMENT WITNESS</text>
</svg>"""
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "How John Fulfilled His Link Role",
                    "content": {
                        "markdown": "### Distinctive Aspects of John's Ministry:\n\n1. **A Radical Forerunner:** Unlike temple priests who operated within established institutions, John took his ministry to the wilderness. He challenged the presumption that biological descent from Abraham was sufficient for salvation, demanding inward moral repentance.\n\n2. **Deflecting Glory to the Messiah:** John maintained extraordinary humility. When crowds questioned if he was the Christ, John boldly declared: *'He who comes after me is mightier than I, whose sandals I am not worthy to carry.'* (Matthew 3:11) and *'He must increase, but I must decrease.'* (John 3:30).\n\n3. **Transferring His Own Disciples:** When Jesus appeared, John pointed his own disciples—including Andrew—directly to Jesus, declaring: *'Look, the Lamb of God, who takes away the sin of the world!'* (John 1:29)."
                    }
                }
            ],
            # Page 4: Video & Spiritual Reflection
            [
                {
                    "type": "suggested_video",
                    "title": "BibleProject: Gospel of Luke (Chapters 1-2)",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=26z_Khwaxyg",
                        "youtube_id": "26z_Khwaxyg",
                        "title": "BibleProject: Gospel of Luke (Chapters 1-2)",
                        "description": "Visual exposition exploring the parallel announcements and births of John the Baptist and Jesus Christ in Luke 1-2."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Spiritual Reflection: Humility in Divine Calling",
                    "content": {
                        "markdown": "In our modern culture dominated by follower counts, personal branding, and influencers striving for the spotlight, John the Baptist provides a countercultural model of **true servant leadership**.\n\nJohn's ultimate joy was fulfilled not when his own following grew, but when his followers left him to follow Jesus. True Christian ministry is never about building a personal empire; it is about pointing others faithfully to the Savior."
                    }
                }
            ],
            # Page 5: Values & Case Study
            [
                {
                    "type": "step_process",
                    "title": "Character Study: Emulating John the Baptist's Core Virtues",
                    "content": {
                        "title": "Character Study: Emulating John the Baptist's Core Virtues",
                        "steps": [
                            "Uncompromising Integrity: John spoke truth to power without fear of peer pressure or political retribution, confronting even King Herod regarding moral corruption.",
                            "Singleness of Purpose: John understood his God-given identity as a herald rather than the King, preventing jealousy or mission drift.",
                            "Exemplary Humility: John gladly decreased so that Christ could increase, prioritizing God's kingdom over personal ambition.",
                            "Practical Application: In student leadership and daily life, refuse to take credit for shared achievements and direct honor to God and peers."
                        ]
                    }
                }
            ],
            # Page 6: Summary & Knowledge Check
            [
                {
                    "type": "key_takeaway",
                    "title": "Summary Takeaways: John the Baptist as Covenant Link",
                    "content": {
                        "markdown": "John the Baptist holds a singular position in salvation history as the bridge between covenants. Foretold by Isaiah and Malachi, he prepared the way for Jesus in the spirit and power of Elijah and introduced Jesus as the Lamb of God with exemplary humility."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Check Your Understanding: John the Baptist",
                    "content": {
                        "question": "In what specific way did John the Baptist fulfill his role as the prophetic forerunner to Jesus Christ?",
                        "options": [
                            "A) By performing miraculous military victories to liberate Israel from Rome.",
                            "B) By preaching repentance, preparing hearts, and pointing his disciples to Jesus as the Lamb of God.",
                            "C) By rebuilding the physical temple walls in Jerusalem.",
                            "D) By authoring the books of the Old Testament law."
                        ],
                        "answer": "B",
                        "explanation": "John fulfilled his role as forerunner by preaching a baptism of repentance, preparing the people spiritually, and introducing Jesus to Israel while declaring 'He must increase, but I must decrease' (John 1:29, 3:30)."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 3: Infancy and Early Life of Jesus Christ
    # -------------------------------------------------------------------------
    {
        "unit_order": 3,
        "unit_name": "2.2.3 Infancy and Early Life of Jesus Christ",
        "unit_description": "Trace the chronological narrative of Jesus' infancy, temple presentation, and boyhood in Nazareth according to the Gospel of Luke.",
        "lesson_title": "Infancy and Early Life of Jesus Christ",
        "pages": [
            # Page 1: Hook, Goals, Intro
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Hook: The Historic Hills of Nazareth",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Nazareth_from_Mount_Precipice.jpg/800px-Nazareth_from_Mount_Precipice.jpg",
                        "title": "Visual Hook: The Landscape of Nazareth in Galilee",
                        "author": "Bernard Gagnon",
                        "licensing": "CC BY-SA 3.0",
                        "source": "Wikimedia Commons",
                        "caption": "Panoramic view of Nazareth from Mount Precipice. In this modest Galilean town, Jesus spent His childhood and grew in wisdom, stature, and favor with God and men (Luke 2:52)."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Infancy and Early Life of Jesus",
                    "content": {
                        "goals": [
                            "Sequence and describe the key historical events in the infancy and boyhood of Jesus according to Luke.",
                            "Analyze the prophetic testimonies of Simeon and Anna during the Temple presentation.",
                            "Evaluate Jesus' four-fold growth spectrum in Luke 2:52 (intellectual, physical, spiritual, social)."
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Introduction: The Revolutionary Birth of a King",
                    "content": {
                        "markdown": "When earthly rulers are born, palaces erupt in fanfare, gold carriages parade through capital streets, and dignitaries arrive bearing imperial tributes. \n\nContrast that with the arrival of the King of Kings, Jesus Christ: born in a rustic animal shelter, placed into a feeding trough (**manger**), and visited first not by royalty, but by poor, social outcasts—shepherds keeping watch over their flocks at night. Luke's infancy narrative unveils God's revolutionary kingdom where humility replaces worldly arrogance."
                    }
                }
            ],
            # Page 2: Chronological Timeline in Luke
            [
                {
                    "type": "concept_explanation",
                    "title": "Timeline of Luke's Infancy & Boyhood Narrative",
                    "content": {
                        "markdown": "The Gospel of Luke provides the most orderly, comprehensive historical account of Jesus' early years.\n\n### Step 1: The Annunciations (Luke 1:5-56)\n- Gabriel appears to the elderly priest Zechariah in the Temple, announcing the miraculous birth of John to Elizabeth.\n- Six months later, Gabriel appears to Mary in Nazareth (The **Annunciation**), announcing that she will conceive Jesus by the Holy Spirit. Mary responds in holy surrender: *'I am the Lord’s servant. May your word to me be fulfilled.'*\n- Mary visits Elizabeth; John leaps in Elizabeth's womb, and Mary sings the **Magnificat** (Luke 1:46-55), praising God for lifting up the humble.\n\n### Step 2: The Birth of John & The Benedictus (Luke 1:57-80)\n- John is born; Zechariah's speech is miraculously restored when he writes 'His name is John.' Zechariah sings the prophetic **Benedictus**.\n\n### Step 3: The Birth of Jesus in Bethlehem (Luke 2:1-20)\n- Joseph and Mary travel from Nazareth to Bethlehem due to Caesar Augustus' census. \n- Jesus is born and laid in a manger because there was no guest room in the inn. Angels announce 'good news of great joy' to shepherds on the hillsides.\n\n### Step 4: Circumcision & Temple Presentation (Luke 2:21-40)\n- On the 8th day, Jesus is circumcised and officially named Jesus (*Yeshua* = 'The Lord saves').\n- At 40 days, Mary and Joseph present Him in the Jerusalem Temple, offering the poor family's sacrifice of two turtledoves (Leviticus 12:8).\n- The elderly prophet **Simeon** takes the child into his arms, uttering the *Nunc Dimittis* (*'A light for revelation to the Gentiles, and the glory of your people Israel'*).\n- The elderly prophetess **Anna**, who fasted and prayed in the temple day and night, gives thanks and proclaims Jesus to all awaiting redemption.\n\n### Step 5: The Boy Jesus in the Temple at Age 12 (Luke 2:41-52)\n- During Passover, Jesus remains behind in Jerusalem. After three days of searching, His anxious parents find Him sitting among the rabbis, listening and asking profound questions.\n- When Mary asks why He caused them worry, Jesus delivers His first recorded words in Scripture: *'Why were you searching for me? Didn’t you know I had to be in my Father’s house?'* (Luke 2:49)."
                    }
                }
            ],
            # Page 3: Pedagogical Diagram & Holistic Growth
            [
                {
                    "type": "suggested_diagram",
                    "title": "Jesus' Early Life Milestones & Holistic Growth Spectrum",
                    "content": {
                        "caption": "Timeline of Luke's Infancy Narrative integrated with the four dimensions of holistic human growth outlined in Luke 2:52.",
                        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
  </defs>

  <rect width="800" height="450" rx="12" fill="url(#bgGrad3)"/>
  <rect x="15" y="15" width="770" height="420" rx="10" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4"/>

  <!-- Main Header -->
  <text x="400" y="48" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#f8fafc" text-anchor="middle">LUKE's NARRATIVE OF JESUS' INFANCY &amp; EARLY YOUTH</text>
  <text x="400" y="68" font-family="Arial, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Five Chronological Milestones &amp; The Luke 2:52 Holistic Growth Framework</text>

  <!-- Top 5 Chronological Step Boxes -->
  <g transform="translate(35, 90)">
    <!-- Step 1 -->
    <rect x="0" y="0" width="135" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="20" cy="20" r="12" fill="#38bdf8"/>
    <text x="20" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>
    <text x="75" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Annunciations</text>
    <text x="10" y="48" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Gabriel to Mary</text>
    <text x="10" y="65" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Elizabeth visit</text>
    <text x="10" y="82" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Magnificat</text>
    <text x="10" y="100" font-family="Arial, sans-serif" font-size="9" fill="#94a3b8">Luke 1:26-56</text>

    <!-- Arrow 1 -->
    <path d="M 140 55 L 148 55" stroke="#fbbf24" stroke-width="2"/>

    <!-- Step 2 -->
    <rect x="150" y="0" width="135" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="170" cy="20" r="12" fill="#38bdf8"/>
    <text x="170" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>
    <text x="225" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">John Born</text>
    <text x="160" y="48" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Speech restored</text>
    <text x="160" y="65" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Benedictus sung</text>
    <text x="160" y="82" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Forerunner ready</text>
    <text x="160" y="100" font-family="Arial, sans-serif" font-size="9" fill="#94a3b8">Luke 1:57-80</text>

    <!-- Arrow 2 -->
    <path d="M 290 55 L 298 55" stroke="#fbbf24" stroke-width="2"/>

    <!-- Step 3 -->
    <rect x="300" y="0" width="135" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="320" cy="20" r="12" fill="#38bdf8"/>
    <text x="320" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>
    <text x="375" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Birth in Manger</text>
    <text x="310" y="48" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Caesar's census</text>
    <text x="310" y="65" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Bethlehem travel</text>
    <text x="310" y="82" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Shepherd witness</text>
    <text x="310" y="100" font-family="Arial, sans-serif" font-size="9" fill="#94a3b8">Luke 2:1-20</text>

    <!-- Arrow 3 -->
    <path d="M 440 55 L 448 55" stroke="#fbbf24" stroke-width="2"/>

    <!-- Step 4 -->
    <rect x="450" y="0" width="135" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="470" cy="20" r="12" fill="#38bdf8"/>
    <text x="470" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>
    <text x="525" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Presentation</text>
    <text x="460" y="48" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• 8th day naming</text>
    <text x="460" y="65" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Simeon blessing</text>
    <text x="460" y="82" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Anna testimony</text>
    <text x="460" y="100" font-family="Arial, sans-serif" font-size="9" fill="#94a3b8">Luke 2:21-40</text>

    <!-- Arrow 4 -->
    <path d="M 590 55 L 598 55" stroke="#fbbf24" stroke-width="2"/>

    <!-- Step 5 -->
    <rect x="600" y="0" width="130" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="620" cy="20" r="12" fill="#38bdf8"/>
    <text x="620" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">5</text>
    <text x="670" y="24" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Age 12 Temple</text>
    <text x="610" y="48" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Passover visit</text>
    <text x="610" y="65" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• Astounds rabbis</text>
    <text x="610" y="82" font-family="Arial, sans-serif" font-size="10" fill="#e2e8f0">• "Father's house"</text>
    <text x="610" y="100" font-family="Arial, sans-serif" font-size="9" fill="#94a3b8">Luke 2:41-52</text>
  </g>

  <!-- Lower Section: Luke 2:52 Growth Spectrum -->
  <g transform="translate(35, 225)">
    <rect width="730" height="180" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect width="730" height="35" rx="8" fill="#334155"/>
    <text x="365" y="23" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">THE FOUR-FOLD GROWTH SPECTRUM OF JESUS (LUKE 2:52)</text>

    <!-- 4 Pillars -->
    <!-- Pillar 1: Wisdom -->
    <rect x="20" y="48" width="160" height="115" rx="6" fill="#0f172a" stroke="#818cf8" stroke-width="1"/>
    <text x="100" y="70" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#818cf8" text-anchor="middle">1. WISDOM</text>
    <text x="100" y="88" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">(Intellectual / Mental)</text>
    <text x="30" y="110" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Scriptural mastery</text>
    <text x="30" y="126" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Moral discernment</text>
    <text x="30" y="142" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Deep reflection</text>

    <!-- Pillar 2: Stature -->
    <rect x="200" y="48" width="160" height="115" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="280" y="70" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">2. STATURE</text>
    <text x="280" y="88" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">(Physical / Health)</text>
    <text x="210" y="110" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Carpenter tradesman</text>
    <text x="210" y="126" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Bodily stamina</text>
    <text x="210" y="142" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Healthy maturity</text>

    <!-- Pillar 3: Favor with God -->
    <rect x="380" y="48" width="160" height="115" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="460" y="70" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">3. FAVOR W/ GOD</text>
    <text x="460" y="88" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">(Spiritual Life)</text>
    <text x="390" y="110" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Intimate prayer</text>
    <text x="390" y="126" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Obedience to Father</text>
    <text x="390" y="142" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Holy devotion</text>

    <!-- Pillar 4: Favor with Men -->
    <rect x="560" y="48" width="150" height="115" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="1"/>
    <text x="635" y="70" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ec4899" text-anchor="middle">4. FAVOR W/ MEN</text>
    <text x="635" y="88" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">(Social / Relational)</text>
    <text x="570" y="110" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Respect to parents</text>
    <text x="570" y="126" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Integrity in town</text>
    <text x="570" y="142" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Loved by community</text>
  </g>

  <!-- Bottom Label -->
  <text x="400" y="430" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#94a3b8" text-anchor="middle">"And Jesus grew in wisdom and stature, and in favor with God and man." — Luke 2:52</text>
</svg>"""
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Theological Depth: Incarnation and Development",
                    "content": {
                        "markdown": "### Key Theological Dimensions:\n\n1. **The Genuine Humanity of Jesus:** Jesus was not a mythological figure who bypassed childhood. He experienced human growth, manual labor in Nazareth as a carpenter's son, and daily obedience to earthly parents (Luke 2:51).\n\n2. **Unique Divine Self-Awareness:** Even at age 12, Jesus demonstrated conscious awareness of His unique divine Sonship (*'I had to be in my Father's house'*), yet He submitted humbly to Mary and Joseph during His youth in Nazareth.\n\n3. **Holistic Model for Youth:** Luke 2:52 establishes God's blueprint for young people—growth must not be one-dimensional (academic only), but balanced across intellectual, physical, spiritual, and social spheres."
                    }
                }
            ],
            # Page 4: Video and Spiritual Reflection
            [
                {
                    "type": "suggested_video",
                    "title": "BibleProject: The Infancy and Early Life of Jesus",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=26z_Khwaxyg",
                        "youtube_id": "26z_Khwaxyg",
                        "title": "BibleProject: The Infancy and Early Life of Jesus",
                        "description": "Comprehensive visual overview tracing the infancy narrative, temple presentation, and youth of Jesus in Luke's Gospel."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Spiritual Reflection: God's Value of the Lowly",
                    "content": {
                        "markdown": "Consider the people God chose to witness the Messiah's arrival:\n- Shepherds (despised in 1st-century social hierarchy)\n- Simeon (an elderly, faithful servant waiting quietly in the temple)\n- Anna (an 84-year-old widow devoted to prayer and fasting)\n\nGod does not look at external status, academic prestige, or economic wealth. He reveals His deepest truths to those with pure, receptive, and humble hearts."
                    }
                }
            ],
            # Page 5: Applied Ethics / Youth Growth Plan
            [
                {
                    "type": "step_process",
                    "title": "Personal Growth Plan: Implementing Luke 2:52 in Daily Life",
                    "content": {
                        "title": "Personal Growth Plan: Implementing Luke 2:52 in Daily Life",
                        "steps": [
                            "Intellectual Growth (Wisdom): Commit to disciplined academic study, active reading of Scripture, and critical reflection on moral issues.",
                            "Physical Growth (Stature): Honor your body as the temple of the Holy Spirit through regular exercise, adequate rest, and avoiding harmful substances.",
                            "Spiritual Growth (Favor with God): Cultivate personal prayer, consistent Bible meditation, and active participation in worship.",
                            "Social Growth (Favor with Men): Practice kindness, respect parents and teachers, and maintain integrity in peer relationships."
                        ]
                    }
                }
            ],
            # Page 6: Summary & Knowledge Check
            [
                {
                    "type": "key_takeaway",
                    "title": "Summary Takeaways: Infancy and Early Life of Jesus",
                    "content": {
                        "markdown": "Luke's infancy narrative highlights Jesus' humble birth in Bethlehem, angelic announcements to outcast shepherds, faithful dedication in the Temple witnessed by Simeon and Anna, and wise boyhood in Nazareth where Jesus grew holistically in wisdom, stature, and favor with God and men."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Check Your Understanding: Boy Jesus in the Temple",
                    "content": {
                        "question": "What was Jesus' response when Mary and Joseph found Him in the Jerusalem Temple after three days of searching?",
                        "options": [
                            "A) 'I am forming a new army to overthrow Roman rule.'",
                            "B) 'Why were you searching for me? Didn’t you know I had to be in my Father’s house?'",
                            "C) 'I am returning to Bethlehem to build a sanctuary.'",
                            "D) 'I no longer need to obey earthly parents.'"
                        ],
                        "answer": "B",
                        "explanation": "In Luke 2:49, Jesus gave His first recorded words in Scripture, expressing His unique divine sonship and commitment to His Heavenly Father while remaining obedient to Mary and Joseph."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 4: Teachings of John the Baptist and Relevance Today
    # -------------------------------------------------------------------------
    {
        "unit_order": 4,
        "unit_name": "2.2.4 Moral Teachings of John the Baptist and Social Justice",
        "unit_description": "Analyze John the Baptist's ethical directives to crowds, tax collectors, and soldiers, and apply his social justice principles to modern youth.",
        "lesson_title": "Moral Teachings of John the Baptist and Social Justice",
        "pages": [
            # Page 1: Hook, Goals, Intro
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Hook: The Banks of the Jordan River",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Jordan_River_Qasr_al-Yahud_Baptism_Site.jpg/800px-Jordan_River_Qasr_al-Yahud_Baptism_Site.jpg",
                        "title": "Visual Hook: The Jordan River Baptismal Shore",
                        "author": "Gerd Eichmann",
                        "licensing": "CC BY-SA 4.0",
                        "source": "Wikimedia Commons",
                        "caption": "The banks of the River Jordan at Qasr al-Yahud, where crowds, corrupt tax collectors, and Roman soldiers came to John the Baptist demanding practical moral instructions."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Moral Teachings of John the Baptist",
                    "content": {
                        "goals": [
                            "Examine John the Baptist's specific moral directives to the crowds, tax collectors, and soldiers in Luke 3:1-20.",
                            "Explain the biblical doctrine of repentance as evidenced by visible, practical moral fruits.",
                            "Apply John's principles of social justice, financial integrity, and anti-bullying to modern youth challenges."
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Introduction: Preaching with Moral Authority",
                    "content": {
                        "markdown": "If John the Baptist stepped onto a modern university campus or went live on social media today, he would not tickle ears with feel-good slogans. He would confront our society's greed, corruption, and systemic injustice with unflinching moral clarity.\n\nIn Luke 3:1-20, John stood on the banks of the Jordan River and warned the religious elites not to rely on their lineage. He declared: *'Produce fruit in keeping with repentance... The ax is already at the root of the trees.'* (Luke 3:8-9). When the convicted crowds asked, *'What should we do then?'*, John provided clear, practical ethical standards."
                    }
                }
            ],
            # Page 2: Core Scripture & The Three Target Groups
            [
                {
                    "type": "concept_explanation",
                    "title": "Core Teachings: Specific Directives for Righteous Living",
                    "content": {
                        "markdown": "True repentance is not merely an emotional feeling; it requires a radical change of mind and direction demonstrated through concrete actions.\n\n### 1. Directives to the General Public (The Crowds)\n- **The Command:** *'Anyone who has two shirts should share with the one who has none, and anyone who has food should do the same.'* (Luke 3:11)\n- **Moral Principle:** **Active Compassion and Generosity.** Reject selfish hoarding; look out for vulnerable and impoverished neighbors.\n- **Contemporary Application:** Sharing revision materials, food, and clothes with disadvantaged classmates rather than indulging in excessive consumerism.\n\n### 2. Directives to Tax Collectors (Publicans)\n- **The Command:** *'Don’t collect any more than you are required to.'* (Luke 3:13)\n- **Context:** Tax collectors in Roman Judea were notorious for extortion, over-taxing citizens, and pocketing the surplus.\n- **Moral Principle:** **Professional Integrity and Honesty.** Reject bribery, fraud, and embezzlement.\n- **Contemporary Application:** Refusing to cheat in exams, rejecting bribery in student elections, and returning exact change when entrusted with family funds.\n\n### 3. Directives to Soldiers and Law Enforcers\n- **The Command:** *'Don’t extort money and don’t accuse people falsely—be content with your pay.'* (Luke 3:14)\n- **Context:** Roman soldiers frequently used military muscle to intimidate citizens, manufacture false charges, and extort bribes.\n- **Moral Principle:** **Justice, Contentment, and Anti-Bullying.** Never misuse power to oppress the weak.\n- **Contemporary Application:** Refusing to bully junior students, refraining from spreading malicious gossip online, and standing up against intimidation."
                    }
                }
            ],
            # Page 3: Pedagogical Diagram & Social Justice
            [
                {
                    "type": "suggested_diagram",
                    "title": "Moral Directives & Modern Social Justice Architecture",
                    "content": {
                        "caption": "Comparative visual architecture showing John the Baptist's 3 ethical mandates in Luke 3 and their direct modern youth applications.",
                        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="g1Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="g2Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="g3Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
  </defs>

  <rect width="800" height="450" rx="12" fill="url(#bgGrad4)"/>
  <rect x="15" y="15" width="770" height="420" rx="10" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4"/>

  <!-- Title -->
  <text x="400" y="48" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#f8fafc" text-anchor="middle">JOHN THE BAPTIST'S ETHICAL MANDATES &amp; SOCIAL JUSTICE</text>
  <text x="400" y="68" font-family="Arial, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">"Produce Fruit in Keeping with Repentance" (Luke 3:8)</text>

  <!-- 3 Columns -->
  <!-- Column 1: The Crowds -->
  <g transform="translate(35, 90)">
    <rect width="225" height="315" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <rect width="225" height="45" rx="8" fill="url(#g1Grad)"/>
    <text x="112" y="28" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. THE GENERAL CROWDS</text>

    <!-- Biblical Command -->
    <rect x="10" y="55" width="205" height="70" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="112" y="72" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#60a5fa" text-anchor="middle">BIBLICAL MANDATE</text>
    <text x="20" y="90" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Share spare tunic/shirt</text>
    <text x="20" y="108" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Share food with hungry</text>

    <!-- Core Principle -->
    <rect x="10" y="135" width="205" height="50" rx="5" fill="#0f172a" stroke="#3b82f6" stroke-width="1"/>
    <text x="112" y="152" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#93c5fd" text-anchor="middle">MORAL PRINCIPLE</text>
    <text x="112" y="172" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Generosity &amp; Compassion</text>

    <!-- Youth Application -->
    <rect x="10" y="195" width="205" height="105" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="112" y="212" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">YOUTH APPLICATION</text>
    <text x="20" y="232" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Reject selfish hoarding</text>
    <text x="20" y="250" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Support needy peers</text>
    <text x="20" y="268" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Share learning materials</text>
    <text x="20" y="286" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Community outreach</text>
  </g>

  <!-- Column 2: Tax Collectors -->
  <g transform="translate(285, 90)">
    <rect width="225" height="315" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="225" height="45" rx="8" fill="url(#g2Grad)"/>
    <text x="112" y="28" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. THE TAX COLLECTORS</text>

    <rect x="10" y="55" width="205" height="70" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="112" y="72" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">BIBLICAL MANDATE</text>
    <text x="20" y="90" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Collect only required sum</text>
    <text x="20" y="108" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Stop extortion and graft</text>

    <rect x="10" y="135" width="205" height="50" rx="5" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="112" y="152" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#6ee7b7" text-anchor="middle">MORAL PRINCIPLE</text>
    <text x="112" y="172" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Honesty &amp; Financial Integrity</text>

    <rect x="10" y="195" width="205" height="105" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="112" y="212" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">YOUTH APPLICATION</text>
    <text x="20" y="232" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Never cheat in exams</text>
    <text x="20" y="250" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Return correct shopping change</text>
    <text x="20" y="268" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Refuse bribes in student votes</text>
    <text x="20" y="286" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Transparent financial duties</text>
  </g>

  <!-- Column 3: Soldiers -->
  <g transform="translate(535, 90)">
    <rect width="225" height="315" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="225" height="45" rx="8" fill="url(#g3Grad)"/>
    <text x="112" y="28" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. THE SOLDIERS</text>

    <rect x="10" y="55" width="205" height="70" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="112" y="72" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">BIBLICAL MANDATE</text>
    <text x="20" y="90" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Do not extort money</text>
    <text x="20" y="108" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• No false accusations / Be content</text>

    <rect x="10" y="135" width="205" height="50" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="112" y="152" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#fcd34d" text-anchor="middle">MORAL PRINCIPLE</text>
    <text x="112" y="172" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Justice &amp; Contentment</text>

    <rect x="10" y="195" width="205" height="105" rx="5" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="112" y="212" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">YOUTH APPLICATION</text>
    <text x="20" y="232" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Never bully junior students</text>
    <text x="20" y="250" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Refrain from online slander</text>
    <text x="20" y="268" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Be content with what you have</text>
    <text x="20" y="286" font-family="Arial, sans-serif" font-size="9" fill="#e2e8f0">• Stand against abuse of power</text>
  </g>

  <!-- Footer Banner -->
  <text x="400" y="430" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#cbd5e1" text-anchor="middle">FAITH IN ACTION: TRUE SPIRITUALITY TRANSLATES INTO SOCIAL ETHICS AND INTEGRITY</text>
</svg>"""
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Analytic Insights: Faith and Social Justice",
                    "content": {
                        "markdown": "### Why John's Ethics Were Revolutionary:\n\n1. **No Secular-Sacred Divide:** John did not tell soldiers or tax collectors to resign from their jobs. Instead, he instructed them to **practice integrity within their vocations**. Godly ethics must transform everyday business, governance, and school life.\n\n2. **Confrontation of Systemic Abuse:** In first-century society, the powerful preyed upon the vulnerable. John condemned exploitation and affirmed that God evaluates our spiritual life by how we treat the marginalized and weak.\n\n3. **Contentment as an Antidote to Greed:** John identified lack of contentment as the root cause of corruption, extortion, and fraud. A contented heart is immune to bribery."
                    }
                }
            ],
            # Page 4: Video & Spiritual Reflection
            [
                {
                    "type": "suggested_video",
                    "title": "BibleProject: Biblical Justice",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=A14TH994kBQ",
                        "youtube_id": "A14TH994kBQ",
                        "title": "BibleProject: Biblical Justice",
                        "description": "Deep theological exploration of justice (Mishpat and Tzedakah) and how active righteousness demands standing up for the vulnerable."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Spiritual Reflection: Living Beyond Religious Slogans",
                    "content": {
                        "markdown": "It is easy to profess faith through songs and religious slogans, but John the Baptist reminds us that genuine faith is validated by tangible actions of justice, kindness, and truth.\n\nWhen we refuse to cheat on an exam, when we share lunch with a hungry classmate, or when we defend someone being bullied in school or on social media, we are demonstrating the true fruit of repentance."
                    }
                }
            ],
            # Page 5: Ethical Dilemma
            [
                {
                    "type": "step_process",
                    "title": "Ethical Case Study: The School Canteen Treasurer",
                    "content": {
                        "title": "Ethical Case Study: The School Canteen Treasurer",
                        "steps": [
                            "The Situation: Brian is elected treasurer of the school environmental club. The club raises funds by selling snacks during sports day.",
                            "The Compromise: A senior student approaches Brian, suggesting they inflate receipt totals by 20% and split the excess money, claiming 'everyone does it.'",
                            "John the Baptist's Mandate: In Luke 3:13, John warned tax collectors never to collect more than required and to uphold total honesty.",
                            "Action Plan: Brian firmly rejects the proposal, ensures transparent public bookkeeping, and reports the attempt to the club teacher sponsor."
                        ]
                    }
                }
            ],
            # Page 6: Summary & Knowledge Check
            [
                {
                    "type": "key_takeaway",
                    "title": "Summary Takeaways: Moral Teachings of John the Baptist",
                    "content": {
                        "markdown": "John the Baptist preached that true repentance produces visible fruit in personal integrity and social justice: the general public must share resources, tax collectors must reject fraud and extortion, and soldiers must refuse brutality, slander, and abuse of power."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Check Your Understanding: John's Directives to Soldiers",
                    "content": {
                        "question": "What specific ethical instructions did John the Baptist give to the soldiers who came to him for baptism?",
                        "options": [
                            "A) Resign immediately from the military and become wilderness hermits.",
                            "B) Don't extort money, don't accuse people falsely, and be content with your wages.",
                            "C) Double the tax rates on all non-Roman citizens.",
                            "D) Fast for forty days before going into battle."
                        ],
                        "answer": "B",
                        "explanation": "In Luke 3:14, John explicitly commanded the soldiers: 'Don't extort money and don't accuse people falsely—be content with your pay,' directly targeting abuse of power and extortion."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 5: Baptism of Jesus Christ and Its Relevance
    # -------------------------------------------------------------------------
    {
        "unit_order": 5,
        "unit_name": "2.2.5 Baptism of Jesus Christ and Theological Epiphany",
        "unit_description": "Examine the baptism of Jesus in the Jordan River, the Trinitarian epiphany, and its enduring theological significance for Christian believers.",
        "lesson_title": "Baptism of Jesus Christ and Theological Epiphany",
        "pages": [
            # Page 1: Hook, Goals, Intro
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Hook: The Jordan River at Al-Maghtas",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Qasr_al-Yahud_Jordan_River.jpg/800px-Qasr_al-Yahud_Jordan_River.jpg",
                        "title": "Visual Hook: The Jordan River Baptismal Site",
                        "author": "Gerd Eichmann",
                        "licensing": "CC BY-SA 4.0",
                        "source": "Wikimedia Commons",
                        "caption": "The tranquil waters of the River Jordan at Qasr al-Yahud / Al-Maghtas, the traditional site where Jesus was baptized by John, inaugurating His public ministry."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: The Baptism of Jesus Christ",
                    "content": {
                        "goals": [
                            "Explain the reasons why sinless Jesus submitted to baptism by John in the Jordan River.",
                            "Analyze the Trinitarian epiphany (Father's voice, Son in water, Spirit as dove) at Jesus' baptism in Luke 3:21-22.",
                            "Evaluate the relevance and theological meaning of water baptism for Christians today."
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Introduction: The Sinless Savior in the Water",
                    "content": {
                        "markdown": "Imagine a world-class Olympic swimmer lining up to take introductory lessons in the shallow pool with complete beginners. You would immediately ask: *'Why are you here?'*\n\nWhen Jesus—the completely holy, sinless Son of God—approached John the Baptist at the Jordan River to be baptized, John was astounded. In Matthew 3:14, John tried to deter Him, saying, *'I need to be baptized by you, and do you come to me?'* Yet Jesus insisted, saying: *'Let it be so now; it is proper for us to do this to fulfill all righteousness.'*"
                    }
                }
            ],
            # Page 2: Core Scripture & The Trinitarian Revelation
            [
                {
                    "type": "concept_explanation",
                    "title": "The Epiphany: Luke 3:21-22 and the Triune God",
                    "content": {
                        "markdown": "Luke records Jesus' baptism with distinctive theological emphasis:\n\n> *'When all the people were being baptized, Jesus was baptized too. And as he was praying, heaven was opened and the Holy Spirit descended on him in bodily form like a dove. And a voice came from heaven: \"You are my Son, whom I love; with you I am well pleased.\"*' (Luke 3:21-22)\n\n### The Four Theological Pillars of Jesus' Baptism:\n\n1. **Solidarity with Sinful Humanity:** Although Jesus possessed no personal sin requiring repentance, He willingly entered the waters to stand in complete solidarity with fallen humanity, identifying with the sinners He came to redeem.\n\n2. **Public Inauguration of Ministry:** Baptism served as the official public commissioning of Jesus' messianic mission as Prophet, Priest, and King.\n\n3. **Trinitarian Epiphany:** In this singular historical moment, the **Holy Trinity** was manifested simultaneously:\n   - **God the Father:** Spoke audibly from the opened heavens (*'You are my beloved Son'*).\n   - **God the Son:** Stood humbly in the waters of the Jordan.\n   - **God the Holy Spirit:** Descended visibly upon Jesus in bodily form like a dove.\n\n4. **Divine Anointing & Approval:** The Father publicly declared His divine delight and seal of approval upon the Son, empowering Jesus with the Holy Spirit for His earthly ministry."
                    }
                }
            ],
            # Page 3: Pedagogical Diagram & Epiphany Breakdown
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Trinitarian Epiphany at Jesus' Baptism",
                    "content": {
                        "caption": "Pedagogical vector diagram illustrating the simultaneous revelation of the Father, Son, and Holy Spirit at the baptism of Jesus in the Jordan River.",
                        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
    <linearGradient id="waterGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="beamGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.1"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" rx="12" fill="url(#bgGrad5)"/>
  <rect x="15" y="15" width="770" height="420" rx="10" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4"/>

  <!-- Left: Visual Illustration of Epiphany -->
  <g transform="translate(35, 35)">
    <rect width="360" height="380" rx="8" fill="url(#skyGrad)" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Light Rays from Heaven -->
    <polygon points="180,0 60,250 300,250" fill="url(#beamGrad)"/>

    <!-- Father's Voice Banner at Top -->
    <rect x="30" y="15" width="300" height="50" rx="6" fill="#0f172a" fill-opacity="0.85" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="180" y="34" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">GOD THE FATHER (THE VOICE)</text>
    <text x="180" y="52" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#ffffff" text-anchor="middle">"You are my Son, whom I love; with you I am well pleased."</text>

    <!-- Holy Spirit Dove at Center -->
    <g transform="translate(180, 115)">
      <circle cx="0" cy="0" r="28" fill="#ffffff" fill-opacity="0.95" stroke="#38bdf8" stroke-width="2"/>
      <path d="M -16 -4 C -8 -14 8 -14 16 -4 C 10 2 -10 2 -16 -4 Z" fill="#0284c7"/>
      <circle cx="0" cy="-6" r="4" fill="#0284c7"/>
      <path d="M -8 2 L 0 14 L 8 2 Z" fill="#0284c7"/>
      <rect x="-70" y="34" width="140" height="20" rx="4" fill="#0f172a" fill-opacity="0.8"/>
      <text x="0" y="48" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE HOLY SPIRIT (DOVE)</text>
    </g>

    <!-- River Jordan Water -->
    <rect x="0" y="240" width="360" height="140" rx="0" fill="url(#waterGrad)"/>
    <path d="M 0 240 Q 90 230 180 240 T 360 240 L 360 380 L 0 380 Z" fill="#0369a1"/>

    <!-- Jesus in Water -->
    <g transform="translate(180, 275)">
      <circle cx="0" cy="-30" r="16" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>
      <path d="M -15 -14 C -15 15 15 15 15 -14 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <ellipse cx="0" cy="15" rx="45" ry="10" fill="none" stroke="#ffffff" stroke-width="2" stroke-dasharray="4 2"/>
      <rect x="-65" y="32" width="130" height="20" rx="4" fill="#0f172a" fill-opacity="0.85"/>
      <text x="0" y="46" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#fed7aa" text-anchor="middle">GOD THE SON (JESUS)</text>
    </g>
  </g>

  <!-- Right: 4 Theological Pillars -->
  <g transform="translate(415, 35)">
    <rect width="350" height="380" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="175" y="30" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#f8fafc" text-anchor="middle">THEOLOGICAL SIGNIFICANCE</text>
    <line x1="20" y1="42" x2="330" y2="42" stroke="#475569" stroke-width="1"/>

    <!-- Pillar 1 -->
    <g transform="translate(15, 55)">
      <rect width="320" height="65" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="12" y="22" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Solidary Identification</text>
      <text x="12" y="40" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">Though sinless, Christ identified with fallen</text>
      <text x="12" y="54" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">humanity whom He came to save.</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(15, 130)">
      <rect width="320" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
      <text x="12" y="22" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#34d399">2. Public Inauguration</text>
      <text x="12" y="40" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">Marked the formal, public start of His earthly</text>
      <text x="12" y="54" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">ministry and messianic mission.</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(15, 205)">
      <rect width="320" height="65" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1"/>
      <text x="12" y="22" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#fbbf24">3. Trinitarian Revelation</text>
      <text x="12" y="40" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">Simultaneous epiphany of Father (voice), Son</text>
      <text x="12" y="54" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">(water), and Holy Spirit (dove).</text>
    </g>

    <!-- Pillar 4 -->
    <g transform="translate(15, 280)">
      <rect width="320" height="65" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="1"/>
      <text x="12" y="22" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ec4899">4. Divine Anointing &amp; Approval</text>
      <text x="12" y="40" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">Empowered by the Holy Spirit and affirmed by the</text>
      <text x="12" y="54" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">Father's audible blessing.</text>
    </g>
  </g>
</svg>"""
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Contemporary Relevance of Baptism for Christians",
                    "content": {
                        "markdown": "### What Baptism Means for Believers Today:\n\n1. **Obedience to the Great Commission:** In Matthew 28:19, Jesus commanded His followers: *'Go and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit.'*\n\n2. **Identification with Christ's Death and Resurrection:** As taught in Romans 6:3-4, immersion into water symbolizes dying to the old life of sin and being buried with Christ, while coming out of the water represents resurrection into a new, transformed life.\n\n3. **Public Declaration of Faith:** Baptism is an outward testimony of an inward spiritual transformation, boldly proclaiming personal allegiance to Jesus before the Church and the world.\n\n4. **Incorporation into the Global Body of Christ:** Baptism signifies unity across ethnic, economic, and social boundaries (Galatians 3:27-28: *'There is neither Jew nor Gentile, slave nor free, male nor female, for you are all one in Christ Jesus'*)."
                    }
                }
            ],
            # Page 4: Video and Spiritual Reflection
            [
                {
                    "type": "suggested_video",
                    "title": "BibleProject: The Baptism of Jesus",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=26z_Khwaxyg",
                        "youtube_id": "26z_Khwaxyg",
                        "title": "BibleProject: The Baptism of Jesus",
                        "description": "Visual study exploring Jesus' baptism in the Jordan River, the Holy Spirit's empowerment, and the divine declaration of Sonship."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Spiritual Reflection: Living Out Our Identity as God's Children",
                    "content": {
                        "markdown": "At His baptism, before Jesus had performed a single miracle, preached a single sermon, or healed a single sick person, the Father declared: *'You are my Son, whom I love; with you I am well pleased.'*\n\nJesus' worth was not based on performance or popularity; it was rooted in His relationship with the Father. Similarly, for Christians, our identity and dignity are anchored in being loved children of God through grace."
                    }
                }
            ],
            # Page 5: Applied Ethics / Youth Reflection
            [
                {
                    "type": "step_process",
                    "title": "Practical Steps: Living Out Your Baptismal Identity",
                    "content": {
                        "title": "Practical Steps: Living Out Your Baptismal Identity",
                        "steps": [
                            "Recognize Your New Life: Understand that in Christ, past failures and guilt are buried, and you are called to walk in newness of life.",
                            "Rely on the Holy Spirit: Do not attempt to live the Christian life through mere human willpower; daily seek the Spirit's guidance and fruit (Galatians 5:22-23).",
                            "Stand in Solidarity with Others: Following Jesus' example of stepping into the Jordan River, stand in empathy with those who are struggling or hurting.",
                            "Maintain Public Integrity: Ensure that your outward conduct aligns with the inward transformation you profess."
                        ]
                    }
                }
            ],
            # Page 6: Summary & Knowledge Check
            [
                {
                    "type": "key_takeaway",
                    "title": "Summary Takeaways: The Baptism of Jesus",
                    "content": {
                        "markdown": "Jesus was baptized by John in the Jordan River to fulfill all righteousness, identify with sinful humanity, and launch His public ministry. The event featured a profound Trinitarian epiphany (the Father's voice, the Son in the water, and the Holy Spirit as a dove) and provides the pattern for Christian baptism."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Check Your Understanding: Trinitarian Epiphany",
                    "content": {
                        "question": "How were all three persons of the Holy Trinity manifested at Jesus' baptism in Luke 3:21-22?",
                        "options": [
                            "A) The Father spoke from heaven, the Son was in the Jordan River, and the Holy Spirit descended like a dove.",
                            "B) The Father appeared as a burning bush, the Son fasted in the desert, and the Spirit blew as a strong wind.",
                            "C) Three angels blew trumpets from the temple roof in Jerusalem.",
                            "D) John the Baptist declared himself to be the third person of the Trinity."
                        ],
                        "answer": "A",
                        "explanation": "At Jesus' baptism, God the Father spoke audibly from heaven, God the Son stood in the waters of the Jordan, and God the Holy Spirit descended in bodily form like a dove (Luke 3:21-22)."
                    }
                }
            ]
        ]
    },

    # -------------------------------------------------------------------------
    # UNIT 6: Temptations of Jesus Christ and Overcoming Temptations
    # -------------------------------------------------------------------------
    {
        "unit_order": 6,
        "unit_name": "2.2.6 Temptations of Jesus Christ and Moral Victory",
        "unit_description": "Analyze the three temptations Jesus faced in the Judean wilderness, His scriptural defense strategies, and practical tools for youth overcoming peer pressure.",
        "lesson_title": "Temptations of Jesus Christ and Moral Victory",
        "pages": [
            # Page 1: Hook, Goals, Intro
            [
                {
                    "type": "suggested_image",
                    "title": "Visual Hook: The Mount of Temptation in Jericho",
                    "content": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mount_of_Temptation_Jericho.jpg/800px-Mount_of_Temptation_Jericho.jpg",
                        "title": "Visual Hook: The Mount of Temptation",
                        "author": "Gerd Eichmann",
                        "licensing": "CC BY-SA 4.0",
                        "source": "Wikimedia Commons",
                        "caption": "The Mount of Temptation (Jabal al-Qurunfal) in the Judean Desert overlooking Jericho, the traditional location of Jesus' 40-day wilderness fast and spiritual warfare against Satan."
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson Objectives: Temptations of Jesus Christ",
                    "content": {
                        "goals": [
                            "Outline the three specific temptations Jesus faced in the wilderness according to Luke 4:1-13.",
                            "Analyze the spiritual strategies and Scriptural weaponry Jesus used to defeat Satan's deception.",
                            "Develop practical three-step techniques for modern youth to overcome daily peer pressure and moral compromises."
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Introduction: Understanding Temptation vs Sin",
                    "content": {
                        "markdown": "Have you ever felt an intense, persistent urge to do something you knew was morally wrong—such as cheating to pass a test, telling a lie to escape punishment, or stealing a small amount of money? That experience is called **temptation**.\n\nIt is vital to understand a foundational truth: **Temptation itself is NOT a sin.** Even Jesus, the perfect and sinless Son of God, was intensely tempted in every way, just as we are, yet He did not sin (Hebrews 4:15). Sin only occurs when we surrender our will and yield to the temptation."
                    }
                }
            ],
            # Page 2: The Three Temptations in Luke 4
            [
                {
                    "type": "concept_explanation",
                    "title": "Core Scripture: The Wilderness Battle (Luke 4:1-13)",
                    "content": {
                        "markdown": "Immediately following His baptism, Jesus, full of the Holy Spirit, was led by the Spirit into the Judean wilderness, where He fasted for 40 days. In His state of extreme physical hunger, Satan launched three targeted attacks:\n\n### 1. First Temptation: Stones into Bread (Physical Appetites)\n- **The Lure:** *'If you are the Son of God, tell this stone to become bread.'* (Luke 4:3)\n- **Targeted Vulnerability:** Immediate physical hunger, bodily comfort, and using divine power selfishly outside God's timing.\n- **Jesus' Scriptural Weapon:** *'It is written: Man shall not live on bread alone, but on every word that comes from the mouth of God.'* (Quoting Deuteronomy 8:3).\n\n### 2. Second Temptation: Worshipping Satan for Worldly Power (Greed & Status)\n- **The Lure:** Satan showed Jesus all the kingdoms of the world in an instant and claimed: *'I will give you all their authority and splendor... if you worship me, it will all be yours.'* (Luke 4:5-7)\n- **Targeted Vulnerability:** Shortcut to power and avoidance of the cross through moral compromise and idol worship.\n- **Jesus' Scriptural Weapon:** *'It is written: Worship the Lord your God and serve him only.'* (Quoting Deuteronomy 6:13).\n\n### 3. Third Temptation: Jumping from the Temple Peak (Pride & Presumption)\n- **The Lure:** Satan placed Jesus on the highest pinnacle of the Jerusalem Temple and twisted Scripture (Psalm 91:11-12), saying: *'Throw yourself down from here. For it is written: He will command his angels concerning you to guard you carefully.'* (Luke 4:9-11)\n- **Targeted Vulnerability:** Spiritual pride, sensation-seeking, and manipulating God to prove His love on human terms.\n- **Jesus' Scriptural Weapon:** *'It is said: Do not put the Lord your God to the test.'* (Quoting Deuteronomy 6:16)."
                    }
                }
            ],
            # Page 3: Pedagogical Diagram & Scriptural Arsenal
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 3 Wilderness Temptations vs Scripture Weaponry Matrix",
                    "content": {
                        "caption": "Pedagogical matrix detailing the three wilderness temptations, targeted human vulnerabilities, and Jesus' precise Scriptural rebuttals from Deuteronomy.",
                        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
  </defs>

  <rect width="800" height="450" rx="12" fill="url(#bgGrad6)"/>
  <rect x="15" y="15" width="770" height="420" rx="10" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4"/>

  <!-- Title Header -->
  <text x="400" y="45" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#f8fafc" text-anchor="middle">THE THREE WILDERNESS TEMPTATIONS &amp; SCRIPTURE WEAPONRY</text>
  <text x="400" y="65" font-family="Arial, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Mastering the Armor of the Word to Defeat Deception (Luke 4:1-13)</text>

  <!-- Table Headers -->
  <rect x="35" y="85" width="220" height="28" rx="4" fill="#334155"/>
  <text x="145" y="103" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">SATAN'S TEMPTATION / LURE</text>

  <rect x="265" y="85" width="230" height="28" rx="4" fill="#334155"/>
  <text x="380" y="103" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">TARGETED VULNERABILITY</text>

  <rect x="505" y="85" width="260" height="28" rx="4" fill="#334155"/>
  <text x="635" y="103" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">JESUS' SCRIPTURE REBUTTAL</text>

  <!-- Row 1: Stones to Bread -->
  <g transform="translate(35, 120)">
    <rect width="730" height="85" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="8" height="85" rx="2" fill="#ef4444"/>

    <!-- Col 1 -->
    <text x="20" y="25" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#fca5a5">1. Stones to Bread</text>
    <text x="20" y="45" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#cbd5e1">"Tell this stone to become</text>
    <text x="20" y="60" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#cbd5e1">bread if you are God's Son."</text>

    <!-- Col 2 -->
    <text x="240" y="25" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">Physical Appetites &amp; Timing</text>
    <text x="240" y="45" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Extreme hunger (40 days)</text>
    <text x="240" y="60" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Selfish use of divine power</text>

    <!-- Col 3 -->
    <rect x="475" y="10" width="245" height="65" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="485" y="28" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#34d399">Deuteronomy 8:3</text>
    <text x="485" y="45" font-family="Arial, sans-serif" font-size="10" fill="#f8fafc">"Man shall not live on bread</text>
    <text x="485" y="60" font-family="Arial, sans-serif" font-size="10" fill="#f8fafc">alone, but on God's word."</text>
  </g>

  <!-- Row 2: Worshipping Satan -->
  <g transform="translate(35, 215)">
    <rect width="730" height="85" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="8" height="85" rx="2" fill="#f59e0b"/>

    <!-- Col 1 -->
    <text x="20" y="25" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#fde68a">2. Bow to Satan for Power</text>
    <text x="20" y="45" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#cbd5e1">"All worldly authority is yours</text>
    <text x="20" y="60" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#cbd5e1">if you bow and worship me."</text>

    <!-- Col 2 -->
    <text x="240" y="25" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">Worldly Clout &amp; Shortcuts</text>
    <text x="240" y="45" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Compromising values for fame</text>
    <text x="240" y="60" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Bypassing the suffering cross</text>

    <!-- Col 3 -->
    <rect x="475" y="10" width="245" height="65" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="485" y="28" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#34d399">Deuteronomy 6:13</text>
    <text x="485" y="45" font-family="Arial, sans-serif" font-size="10" fill="#f8fafc">"Worship the Lord your God</text>
    <text x="485" y="60" font-family="Arial, sans-serif" font-size="10" fill="#f8fafc">and serve him only."</text>
  </g>

  <!-- Row 3: Jump from Temple -->
  <g transform="translate(35, 310)">
    <rect width="730" height="85" rx="6" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="8" height="85" rx="2" fill="#8b5cf6"/>

    <!-- Col 1 -->
    <text x="20" y="25" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ddd6fe">3. Jump from Temple Peak</text>
    <text x="20" y="45" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#cbd5e1">"Throw yourself down; angels</text>
    <text x="20" y="60" font-family="Arial, sans-serif" font-size="10" font-style="italic" fill="#cbd5e1">will guard you safely."</text>

    <!-- Col 2 -->
    <text x="240" y="25" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">Spiritual Pride &amp; Presumption</text>
    <text x="240" y="45" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Testing God's love on our terms</text>
    <text x="240" y="60" font-family="Arial, sans-serif" font-size="10" fill="#cbd5e1">• Twisting Scripture out of context</text>

    <!-- Col 3 -->
    <rect x="475" y="10" width="245" height="65" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="485" y="28" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#34d399">Deuteronomy 6:16</text>
    <text x="485" y="45" font-family="Arial, sans-serif" font-size="10" fill="#f8fafc">"Do not put the Lord your</text>
    <text x="485" y="60" font-family="Arial, sans-serif" font-size="10" fill="#f8fafc">God to the test."</text>
  </g>

  <!-- Footer -->
  <text x="400" y="425" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">DEFENSE STRATEGY: SPIRIT EMPOWERMENT + PRAYER &amp; FASTING + PRECISION SCRIPTURAL MEMORIZATION</text>
</svg>"""
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Strategies Jesus Used to Overcome",
                    "content": {
                        "markdown": "### Jesus' Three-Fold Defense Framework:\n\n1. **Total Reliance on God's Word:** Notice that Jesus did not enter into an extended debate or negotiation with Satan. In every single encounter, He immediately deployed the authoritative written Word of God (*'It is written...'*, quoting from the Book of Deuteronomy).\n\n2. **Filled with and Guided by the Holy Spirit:** Jesus did not rely on raw human willpower. Luke 4:1 emphasizes that Jesus was *'full of the Holy Spirit'* and led by the Spirit.\n\n3. **Spiritual Discipline of Prayer & Fasting:** Forty days of focused prayer and fasting sharpened Jesus' spiritual discernment, keeping His desires completely aligned with the Father's sovereign will."
                    }
                }
            ],
            # Page 4: Video & Spiritual Reflection
            [
                {
                    "type": "suggested_video",
                    "title": "BibleProject: The Wilderness Testing of Jesus",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=k1t6_0l2a6s",
                        "youtube_id": "k1t6_0l2a6s",
                        "title": "BibleProject: The Wilderness Testing of Jesus",
                        "description": "Visual exploration comparing Israel's 40-year failure in the wilderness with Jesus' 40-day victory as the faithful Son of God."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Spiritual Reflection: The Faithful Son in the Wilderness",
                    "content": {
                        "markdown": "In the Old Testament, the nation of Israel spent 40 years in the wilderness and repeatedly failed through grumbling about food, worshipping the golden calf, and testing God at Massah.\n\nJesus went into the same wilderness for 40 days and triumphed where Israel had failed. He is the true, faithful Son who demonstrates that living in obedience to God's Word brings total victory over darkness."
                    }
                }
            ],
            # Page 5: Applied Technique / Overcoming Peer Pressure
            [
                {
                    "type": "step_process",
                    "title": "Youth Toolkit: Three Steps to Overcome Daily Peer Pressure",
                    "content": {
                        "title": "Youth Toolkit: Three Steps to Overcome Daily Peer Pressure",
                        "steps": [
                            "Step 1: Identify the Bait — Recognize immediately when friends, media, or inner impulses tempt you to compromise your moral values (e.g., 'Just cheat this once' or 'Try this drug, nobody will know').",
                            "Step 2: Quote Your Conviction Script — Pre-decide your moral boundaries rooted in Scripture (e.g., 'My body is the temple of the Holy Spirit' - 1 Cor 6:19; 'I will walk with integrity' - Psalm 101:2).",
                            "Step 3: Make an Assertive Exit — State your clear boundary with confidence without debating or wavering, and physically remove yourself from the compromising environment."
                        ]
                    }
                }
            ],
            # Page 6: Summary & Knowledge Check
            [
                {
                    "type": "key_takeaway",
                    "title": "Summary Takeaways: Overcoming Temptation",
                    "content": {
                        "markdown": "Temptation is not sin; yielding to it is. In the Judean wilderness, Jesus defeated Satan's attacks targeting physical appetites, worldly ambition, and spiritual pride by deploying the authoritative Word of God from Deuteronomy while empowered by the Holy Spirit."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Check Your Understanding: Wilderness Victory",
                    "content": {
                        "question": "Which specific Scripture from the Old Testament did Jesus quote when Satan tempted Him to bow down and worship him in exchange for all worldly kingdoms?",
                        "options": [
                            "A) 'Man shall not live on bread alone' (Deuteronomy 8:3)",
                            "B) 'Worship the Lord your God and serve him only' (Deuteronomy 6:13)",
                            "C) 'Do not put the Lord your God to the test' (Deuteronomy 6:16)",
                            "D) 'An eye for an eye and a tooth for a tooth' (Exodus 21:24)"
                        ],
                        "answer": "B",
                        "explanation": "When Satan offered Jesus worldly authority in exchange for worship, Jesus quoted Deuteronomy 6:13: 'It is written: Worship the Lord your God and serve him only' (Luke 4:8)."
                    }
                }
            ]
        ]
    }
]
