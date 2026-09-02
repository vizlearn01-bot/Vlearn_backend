"""
VLearn CBC Grade 10 History — Topic 16: Fourth-Generation Technologies and Historical Information
Authoritative Pedagogical Data Definitions (Lessons 1 to 3)
"""

from curriculum.cbc_grade10_history_topic16_svgs import (
    SVG_FOURTH_IR_WEB,
    SVG_DIGITAL_VERIFICATION_FLOWCHART
)

TOPIC_16_LESSONS = [
    # =========================================================================
    # LESSON 1: ICT and Fourth-Generation Change
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "ICT and Fourth-Generation Change",
        "unit_description": "Foundations of the Fourth Industrial Revolution (4IR), cyber-physical integration, AI, IoT, cloud computing, 3D printing, quantum computing, and ICT as the central nervous system.",
        "lesson_title": "ICT and Fourth-Generation Change",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The Fourth Industrial Revolution: Cyber-Physical Systems",
                    "content": {
                        "title": "Digital Transformation and Intelligent Automation",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Modern_data_center.jpg/800px-Modern_data_center.jpg",
                        "caption": "A high-performance cloud data center powering artificial intelligence algorithms, IoT data processing, and digital historical archives worldwide.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Dawn of the Fourth Industrial Revolution (4IR)",
                    "content": {
                        "text": (
                            "Imagine exploring an immersive virtual reality reconstruction of the 19th-century Buganda Kingdom, or using machine learning algorithms to model pre-colonial migration paths.\n\n"
                            "These breakthroughs are driven by the **Fourth Industrial Revolution (4IR)**—a profound era characterized by the fusion of physical, digital, and biological technologies.\n\n"
                            "Unlike the 3rd generation (which introduced basic personal computers and the internet), the 4th generation creates **intelligent, autonomous cyber-physical networks** linking AI, sensors, and global databases in real time."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Differentiate between the four generations of industrial revolutions\n"
                            "- Define the core pillars of 4IR: AI, IoT, Big Data, Cloud Computing, 3D Printing, and Quantum Computing\n"
                            "- Explain the role of Information and Communication Technology (ICT) as the central nervous system of automation"
                        )
                    }
                }
            ],

            # Card 2: 4IR Web SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Fourth Industrial Revolution (4IR) Connectivity Web",
                    "content": {
                        "title": "The 4IR Connectivity Web",
                        "caption": "Architectural model showing the central AI/Cloud/Big Data hub radiating outward to precision agriculture, telemedicine, smart manufacturing, and digital history archives.",
                        "svg_content": SVG_FOURTH_IR_WEB
                    }
                }
            ],

            # Card 3: Four Generations Comparison Table
            [
                {
                    "type": "comparison_table",
                    "title": "The Four Generations of Industrial Revolutions",
                    "content": {
                        "headers": ["Generation", "Historical Era", "Core Technology Breakthroughs", "Socio-Economic Impact"],
                        "rows": [
                            ["1st Generation (1IR)", "Late 18th Century (~1760–1840)", "Steam engine, coal power, mechanized textile looms", "Transition from agrarian handicraft to factory-based urban manufacturing"],
                            ["2nd Generation (2IR)", "Late 19th Century (~1870–1914)", "Electricity, assembly line, internal combustion engine", "Mass production, rapid urbanization, and early global corporate syndicates"],
                            ["3rd Generation (3IR)", "Late 20th Century (~1960–2000)", "Mainframe computers, microprocessors, early internet", "Automated computing, basic digitization, and digital communications"],
                            ["4th Generation (4IR)", "21st Century (Present Day)", "AI, Machine Learning, IoT, Cloud Computing, BioTech", "Intelligent cyber-physical integration, real-time automation, and VR/AR tools"]
                        ]
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "The Fourth Industrial Revolution Explained",
                    "content": {
                        "title": "Understanding the 4th Industrial Revolution",
                        "description": "Educational documentary analyzing how artificial intelligence, IoT, and cloud networks are reshaping global industry, healthcare, and education.",
                        "youtube_id": "fTTGALaRZoc"
                    }
                }
            ],

            # Card 5: Knowledge Check & Misconceptions
            [
                {
                    "type": "common_misconception",
                    "title": "Misconception vs Reality: 3rd vs 4th Generation",
                    "content": {
                        "misconception": "The 4th Industrial Revolution is just a faster version of the internet and basic desktop computers.",
                        "reality": "The 3rd IR brought basic digitization and standalone computers. The 4th IR is fundamentally distinct because it merges physical machines, digital intelligence (AI), and biological systems into autonomous, connected ecosystems."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: 3rd vs 4th Generation Breakthroughs",
                    "content": {
                        "question": "Which of the following describes the key distinction between the Third and Fourth Industrial Generations?",
                        "options": [
                            "A. The Third generation introduced steam engines, while the Fourth introduced coal electricity.",
                            "B. The Third generation introduced early computing and internet, while the Fourth represents the intelligent integration of cyber-physical systems, AI, and IoT.",
                            "C. The Third generation was based on manual farming, while the Fourth introduced assembly lines.",
                            "D. The Third generation was completely analog, while the Fourth is entirely offline."
                        ],
                        "correct_answer": "B",
                        "explanation": "The 3rd generation digitized processes with basic computers, while the 4th generation connects cyber-physical systems, AI, big data, and biological technologies."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Opportunities, Risks, and Sustainability
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Opportunities, Risks, and Sustainability",
        "unit_description": "Sustainability opportunities (precision agriculture, smart grids, telemedicine), systemic risks (job displacement, digital divide, cybersecurity, e-waste), and UN SDG 9 alignment.",
        "lesson_title": "Opportunities, Risks, and Sustainability",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Sustainable Technologies: Precision Agriculture Drone",
                    "content": {
                        "title": "Agricultural Drone Monitoring Crops",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Agriculture_drone.jpg/800px-Agriculture_drone.jpg",
                        "caption": "An agricultural drone equipped with multispectral sensors analyzing soil nutrients and crop moisture to minimize fertilizer waste and conserve water.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Balancing Growth with Ecological Sustainability",
                    "content": {
                        "text": (
                            "Can 4IR technologies feed growing populations and expand medical care without harming our planet?\n\n"
                            "When deployed ethically, fourth-generation technologies offer powerful opportunities for **sustainable development**:\n"
                            "- **Precision Farming:** IoT sensors and drones apply water and fertilizer only where needed, protecting rivers from chemical runoff.\n"
                            "- **Telemedicine:** High-speed networks connect rural dispensaries in Turkana or Kilifi directly to specialist doctors in Nairobi.\n\n"
                            "However, these advances bring real risks: **technological unemployment**, the **digital divide**, **cybersecurity threats**, and hazardous **e-waste**."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Evaluate the sustainability opportunities of 4IR in agriculture, energy, and healthcare\n"
                            "- Analyze the systemic risks: labor displacement, digital exclusion, e-waste, and privacy\n"
                            "- Connect 4IR applications to UN Sustainable Development Goal 9 (Industry, Innovation, & Infrastructure)"
                        )
                    }
                }
            ],

            # Card 2: Opportunities vs Risks Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "The Balancing Act of 4IR: Opportunities vs Systemic Risks",
                    "content": {
                        "headers": ["Domain", "Sustainability Opportunities (Benefits)", "Systemic Risks & Ethical Challenges"],
                        "rows": [
                            ["Agriculture & Food", "Precision drone irrigation, smart soil monitoring, reduced fertilizer waste", "High equipment costs risking the exclusion of smallholder subsistence farmers"],
                            ["Labor & Industry", "Smart zero-waste 3D printing, automated logistics, enhanced worker safety", "Automation and AI displacement of routine manufacturing and administrative jobs"],
                            ["Healthcare Access", "Telemedicine remote clinics, AI-assisted diagnosis, portable diagnostics", "Data privacy risks regarding sensitive personal medical and genomic records"],
                            ["Environment & Planet", "Smart renewable energy grids balancing solar/wind power in real time", "Rapid hardware obsolescence creating toxic electronic waste (e-waste) dumps"]
                        ]
                    }
                }
            ],

            # Card 3: Source Analysis (UN SDG 9)
            [
                {
                    "type": "concept_explanation",
                    "title": "Primary Source Analysis: UN Sustainable Development Goal 9",
                    "content": {
                        "text": (
                            "> *'Promote inclusive and sustainable industrialization and, by 2030, significantly raise industry's share of employment and gross domestic product... and double its share in least developed countries.'*\n\n"
                            "**Sustainable Policy Analysis:**\n"
                            "- **Leapfrogging:** Developing nations like Kenya can leapfrog 19th-century heavy fossil fuel industrialization by adopting clean solar microgrids, mobile money, and drone-based agriculture.\n"
                            "- **E-Waste Governance:** Requires extended producer responsibility policies where tech manufacturers must fund the safe recycling of obsolete digital devices."
                        )
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Technology, Sustainability, and the Future of Work in Africa",
                    "content": {
                        "title": "How Emerging Tech is Transforming African Development",
                        "description": "Educational documentary examining mobile innovations, agritech startups, renewable energy microgrids, and digital literacy programs across Africa.",
                        "youtube_id": "rNu8XDBSn10"
                    }
                }
            ],

            # Card 5: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Environmental Sustainability Applications",
                    "content": {
                        "question": "Which of the following is a direct environmental sustainability application of Fourth Industrial Revolution technologies?",
                        "options": [
                            "A. Producing cheap disposable smartphones that must be replaced every six months.",
                            "B. Drone-based precision agriculture that optimizes irrigation and minimizes chemical fertilizer runoff.",
                            "C. Powering manufacturing exclusively with coal-fired thermal generators.",
                            "D. Banning digital communications in all schools."
                        ],
                        "correct_answer": "B",
                        "explanation": "Precision agriculture utilizes drone multispectral sensors and IoT soil probes to apply water and fertilizer with high precision, protecting waterways from chemical contamination."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Technology and Historical Information
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Technology and Historical Information",
        "unit_description": "Digital archives, 3D artifact modeling, VR/AR historical simulations, Digital Historical Literacy, metadata analysis, detecting deepfakes, and unit-end synthesis assessment.",
        "lesson_title": "Technology and Historical Information",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Immersive Historical Reconstructions: Virtual Reality in Museums",
                    "content": {
                        "title": "Virtual Reality Museum Exhibition",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Virtual_reality_museum.jpg/800px-Virtual_reality_museum.jpg",
                        "caption": "Students using virtual reality headsets to interact with 3D models of historical artifacts and explore reconstructions of ancient archaeological sites.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Historian's Craft in the Digital Era",
                    "content": {
                        "text": (
                            "How does a historian reconstruct the past in the digital age?\n\n"
                            "Historically, historians spent months in physical archives reading paper manuscripts. Today, digital search tools allow researchers to query millions of digitized manuscripts in seconds.\n\n"
                            "However, this shift creates new challenges: digital images, audio, and documents can be easily manipulated, altered, or generated by AI. Modern historians must master **Digital Historical Literacy** to verify digital evidence."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain how digital archives, 3D scanning, and VR/AR transform historical preservation\n"
                            "- Apply the 4-step Digital Evidence Verification Protocol (Provenance, Metadata, Consistency, Corroboration)\n"
                            "- Detect historical anachronisms in AI-generated images\n"
                            "- Complete the Unit Assessment on 4IR and Historical Information"
                        )
                    }
                }
            ],

            # Card 2: Digital Verification Flowchart SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Digital Evidence Verification Protocol for Historians",
                    "content": {
                        "title": "Digital Verification Flowchart",
                        "caption": "Four-step inquiry protocol: Tracing Provenance, Analyzing File Metadata, Checking Visual Consistency/Anachronisms, and Corroborating with Physical Archives.",
                        "svg_content": SVG_DIGITAL_VERIFICATION_FLOWCHART
                    }
                }
            ],

            # Card 3: Digital Source Criticism Workshop
            [
                {
                    "type": "concept_explanation",
                    "title": "Source Criticism Case: Evaluating an 'AI-Enhanced' 1890 Photograph",
                    "content": {
                        "text": (
                            "**Scenario:** A viral social media post claims to show a 'newly discovered high-resolution color photograph' of Nabongo Mumia signing a treaty with British colonial agents in 1890.\n\n"
                            "**Historical Source Criticism Steps:**\n"
                            "1. **Provenance:** Check if the file is indexed in the Kenya National Archives or the British Museum, or if it originates from an anonymous blog.\n"
                            "2. **Metadata Inspection:** Look at file creation dates, camera software logs, and software tags indicating AI image generation tools (e.g., Midjourney, Stable Diffusion).\n"
                            "3. **Consistency / Anachronism Check:** In 1890, portable fast cameras in East Africa were rare black-and-white glass plates. Perfect studio lighting, synthetic cloth colors, or warped facial details reveal an artificial render.\n"
                            "4. **Corroboration:** Cross-reference with the written 1890 treaty text and oral accounts to see if a photographer was recorded as present."
                        )
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Digital Archives, AI, and the Future of Historical Research",
                    "content": {
                        "title": "Evaluating Digital Evidence and Historical Literacy",
                        "description": "Educational video explaining how digital humanities, online archival collections, and metadata analysis empower modern historical inquiry.",
                        "youtube_id": "T_sGTspaF4Y"
                    }
                }
            ],

            # Card 5: Knowledge Check & Topic-End Assessment
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Provenance and Metadata Verification",
                    "content": {
                        "question": "Why should a digitized historical document or image never be accepted as authentic without provenance and metadata verification?",
                        "options": [
                            "A. Because digital files cause eye strain on computer monitors.",
                            "B. Because digital files can be easily edited, mislabeled, or artificially manufactured by AI, requiring verification of origins and technical history.",
                            "C. Because physical documents were always written by completely neutral observers.",
                            "D. Because computers can only store European historical records."
                        ],
                        "correct_answer": "B",
                        "explanation": "Digital assets can be easily modified or generated by AI tools; historians must verify metadata and original provenance to guarantee historical authenticity."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Definition of Metadata",
                    "content": {
                        "question": "In the context of digital historical inquiry, what is 'metadata'?",
                        "options": [
                            "A. The physical chemical paper used to print 19th-century maps.",
                            "B. A form of heavy metal used in steam boilers.",
                            "C. The underlying data embedded in a digital file that provides information about its creation date, camera/scanner type, and edit history.",
                            "D. A traditional oral praise poem performed by community elders."
                        ],
                        "correct_answer": "C",
                        "explanation": "Metadata is the embedded technical information within a digital file recording timestamps, file type, device models, and modifications."
                    }
                }
            ]
        ]
    }
]
