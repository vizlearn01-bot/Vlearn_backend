"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 9 (The Electoral Process and Functions of Government in Other Parts of the World)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 9: The Electoral Process and Functions of Government in Other Parts of the World (Order: 9)
  - Unit 1: The Kenyan Electoral Process, IEBC, and Candidate Administration (Lesson 1: 16 Pages)
  - Unit 2: The 2007 Electoral Crisis, Kriegler Commission Findings, and Post-Crisis Reforms (Lesson 2: 15 Pages)
  - Unit 3: The British Government and Electoral System: Parliamentary Democracy and Unwritten Constitutionalism (Lesson 3: 16 Pages)
  - Unit 4: The United States Government and Electoral System: Federalism, Separation of Powers, and Checks & Balances (Lesson 4: 16 Pages)
  - Unit 5: The Indian Government, Global Comparative Governance, and Master Synthesis (Lesson 5: 18 Pages)

Total: 5 Learning Units, 5 Lessons, 81 Pages, 92+ Blocks, 9 Media Assets (4 Wikimedia Photos + 5 Verified YouTube Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic9.py --replace
"""

import os
import sys
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

# ---------------------------------------------------------------------------
# Citation & Metadata Cleaner Helper
# ---------------------------------------------------------------------------
BRACKET_CITATION_RE = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')

def clean_text(val):
    if not isinstance(val, str):
        return val
    cleaned = BRACKET_CITATION_RE.sub('', val)
    cleaned = re.sub(r' +', ' ', cleaned)
    cleaned = re.sub(r' \.', '.', cleaned)
    cleaned = re.sub(r' ,', ',', cleaned)
    cleaned = re.sub(r' ;', ';', cleaned)
    cleaned = re.sub(r'\( \)', '', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# ===========================================================================
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 9
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Kenyan Electoral Process, IEBC, and Candidate Administration",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Kenyan Electoral System",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define an electoral system and trace the historical evolution of voting in Kenya (Acclamation, Mlolongo, Secret Ballot)\n"
                        "- Describe the composition, appointment, security of tenure, and 12 functions of the IEBC\n"
                        "- Explain the qualifications and disqualifications for Parliamentary candidates and circumstances under which an MP vacates office\n"
                        "- Detail the hierarchy and duties of election officials (Returning Officers, Presiding Officers, Polling Clerks)"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Electoral System",
                "content": {
                    "term": "Electoral System",
                    "definition": (
                        "The constitutional and legislative framework through which a democratic state translates the political will of its citizens "
                        "into representative legislative seats and executive leadership mandates."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Historical Evolution of Voting Methods in Kenya",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Evolution of Voting Methods in Kenya",
                "content": {
                    "headers": ["Voting Method", "Mechanism", "Democratic Vulnerabilities / Merits"],
                    "rows": [
                        ["Acclamation (Voice / Show of Hands)", "Non-secret oral shout or raising hands at barazas.", "Extremely vulnerable to intimidation and peer pressure; no secrecy."],
                        ["Mlolongo (Queuing System - 1988)", "Voters queued in broad daylight behind photographs of preferred candidates.", "Severely compromised: widespread intimidation by chiefs, blatant rigging where shorter queues were declared winners."],
                        ["Secret Ballot (Modern Standard)", "Voters mark ballots in private polling booths and cast them into sealed, color-coded ballot boxes.", "Protects voter freedom of choice, confidentiality, and prevents electoral coercion."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Anniversary Towers: Headquarters of the IEBC",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Anniversary Towers Nairobi",
                "content": {
                    "text": "Anniversary Towers on University Way, Nairobi, the national headquarters of the Independent Electoral and Boundaries Commission (IEBC).",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Anniversery_towers.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Anniversery_towers.jpg"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Educational Documentary: Structure and Powers of the IEBC",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Legal Analysis: The Independent Electoral and Boundaries Commission (IEBC) Explained",
                "content": {
                    "url": "https://www.youtube.com/watch?v=R9jNMLtMGbo",
                    "text": "Examine the constitutional structure, powers, appointment process, and core operational mandates of the IEBC under Chapter 15 of the Constitution.",
                    "author": "Kenya Law Explained / Civic Series",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Structure and Appointment of the IEBC",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "IEBC Structure and Constitutional Safeguards",
                "content": {
                    "steps": [
                        "1. Composition: A Chairperson and up to eight other commissioners (typically 7 members total).",
                        "2. Selection Panel: Commissioners are selected through a multi-stakeholder, competitive selection panel.",
                        "3. Parliamentary Vetting: Nominees are vetted and approved by the National Assembly before presidential appointment.",
                        "4. Security of Tenure: Appointed for a single, non-renewable term of six (6) years to insulate them from political pressure.",
                        "5. Secretariat: Headed by a Commission Secretary / CEO who manages daily administrative operations and logistics."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Twelve Functions of the IEBC (High-Yield KCSE)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Functions of the IEBC (Point-Form)",
                "content": {
                    "steps": [
                        "1. Continuous Registration of Voters: Registers eligible adult citizens and maintains the national voters' register.",
                        "2. Regular Revision of the Voters' Roll: Inspects, verifies, and purges the register of deceased voters before polls.",
                        "3. Review of Names and Boundaries: Delimits constituencies and wards every 8 to 12 years based on population and geography.",
                        "4. Regulation of Party Nominations: Supervises and monitors internal political party primaries.",
                        "5. Clearance and Registration of Candidates: Registers party-sponsored and independent candidates.",
                        "6. Settlement of Nomination Disputes: Resolves candidate nomination disputes before polling day (excluding post-election petitions).",
                        "7. Conducting and Supervising Elections: Manages polling logistics, printing ballots, tallying, and declaration of winners.",
                        "8. Continuous Voter Education: Conducts civic education to inform citizens on voting rights and procedures.",
                        "9. Formulation of Electoral Code of Conduct: Enforces rules preventing political violence, intimidation, and bribery.",
                        "10. Regulation of Campaign Spending: Monitors and regulates the amount of campaign funds spent by candidates.",
                        "11. Accreditation of Election Observers: Accredits local and international monitors to observe election transparency.",
                        "12. Official Announcement of Results: Tallies, verifies, and officially declares the winners of elections and referenda."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Types of Elections in Kenya",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Types of Elections under the 2010 Constitution",
                "content": {
                    "headers": ["Election Type", "Timing & Trigger", "Seats Contested / Scope"],
                    "rows": [
                        ["General Elections", "Held on the second Tuesday of August every fifth year.", "Six elective seats: President, MP (National Assembly), County Woman Representative, Senator, Governor, MCA."],
                        ["By-Elections", "Held within 90 days of an elective seat falling vacant.", "Triggered by death, resignation, court annulment, bankruptcy, or prison sentence of an incumbent MP/MCA."],
                        ["Re-Run / Fresh Presidential Election", "Held within 60 days if Supreme Court annuls election, or within 30 days if no candidate hits 50%+1 and 25% in 24 counties.", "President and Deputy President only."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Qualifications and Disqualifications for Parliamentary Candidates",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "MP Candidates: Qualifications vs. Disqualifications",
                "content": {
                    "headers": ["Category", "Constitutional Requirements (Article 99)"],
                    "rows": [
                        ["Qualifications", "• Must be a registered voter.\n• Must have been a Kenyan citizen for at least 10 years.\n• Must satisfy prescribed educational standards.\n• Must be nominated by a registered party OR supported by 1,000 voter signatures (NA) / 2,000 signatures (Senate).\n• Must satisfy Chapter 6 (Leadership & Integrity)."],
                        ["Disqualifications", "• Serving as a state/public officer (except MP/Governor).\n• Served as an IEBC commissioner within the past 5 years.\n• Declared of unsound mind or legally bankrupt.\n• Serving a prison sentence of at least 6 months without option of fine.\n• Removed from public office for corruption/misconduct.\n• Holds dual citizenship or owes allegiance to a foreign state."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Circumstances Under Which an MP Vacates Office",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Vacation of a Parliamentary Seat (Article 103)",
                "content": {
                    "steps": [
                        "1. Death: If the member passes away.",
                        "2. Resignation: If the member resigns in writing to the Speaker of the respective House.",
                        "3. Consecutive Absence: Absent from 8 consecutive sittings without written permission from the Speaker.",
                        "4. Loss of Citizenship: If the member ceases to be a Kenyan citizen.",
                        "5. Prison Sentence: Sentenced to imprisonment for a term of six (6) months or more.",
                        "6. Bankruptcy: Declared bankrupt by a court of competent jurisdiction.",
                        "7. Mental Incapacity: Certified to be of unsound mind.",
                        "8. Party Defection: Resigns from the sponsoring political party, or an independent member joins a political party."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Hierarchy and Roles of Election Officials",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "IEBC Field Officials and Their Duties",
                "content": {
                    "headers": ["Official", "Jurisdiction", "Core Responsibilities"],
                    "rows": [
                        ["Returning Officer (RO)", "Constituency or County", "Receives candidate nomination papers; distributes materials; supervises all polling stations; tallies votes and officially declares winning MPs/MCAs."],
                        ["Presiding Officer (PO)", "Specific Polling Station", "Conducts voting in an orderly manner; marks voters with indelible ink; assists PWDs/illiterate voters; seals ballot boxes; counts votes and announces station results."],
                        ["Polling Clerks", "Polling Station", "Verify voter identity on electronic register; issue stamped ballots; guide voters to polling booths."],
                        ["Counting Clerks", "Tallying Hall", "Sort, count, and tally ballots under direct supervision of the Presiding Officer."],
                        ["Party Agents", "Station & Tallying Hall", "Observe the transparency of voting, counting, and sealing of ballot boxes on behalf of candidates."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Check Your Understanding: Module 9.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 9.1 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is the term of office for an IEBC commissioner under the 2010 Constitution?",
                            "options": [
                                "A renewable term of 5 years",
                                "A single, non-renewable term of 6 years",
                                "Life appointment until age 70",
                                "A term of 10 years"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under Chapter 15, IEBC commissioners serve a single, non-renewable term of six (6) years."
                        },
                        {
                            "question": "How many consecutive parliamentary sittings can an MP miss without Speaker permission before losing their seat?",
                            "options": [
                                "4 sittings",
                                "8 sittings",
                                "12 sittings",
                                "20 sittings"
                            ],
                            "correct_answer": 1,
                            "explanation": "Article 103(1)(b) specifies that missing 8 consecutive sittings without written permission leads to loss of seat."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Functions of the IEBC",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Functions of the IEBC in Kenya (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Continuous Registration of Voters:** Registers eligible Kenyan citizens who attain 18 years and maintains an up-to-date national voters' roll. (2 marks)\n\n"
                        "2. **Delimitation of Boundaries:** Regularly reviews the names and boundaries of constituencies and wards every 8 to 12 years based on population and geography. (2 marks)\n\n"
                        "3. **Regulation of Political Party Nominations:** Supervises party primaries to ensure internal democratic compliance. (2 marks)\n\n"
                        "4. **Registration of Candidates:** Clears party-sponsored and independent candidates contesting presidential, parliamentary, and county seats. (2 marks)\n\n"
                        "5. **Conducting Civic and Voter Education:** Sensitizes the public on voting procedures, ballot secrecy, and democratic participation. (2 marks)\n\n"
                        "6. **Conducting and Declaring Election Results:** Manages polling logistics, tallies votes, and officially declares winners of elections and referenda. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Kenyan Electoral System",
                "content": {
                    "text": (
                        "• **Electoral System:** Framework translating votes into representative seats.\n"
                        "• **IEBC Mandate:** 12 core functions; 6-year non-renewable tenure for commissioners.\n"
                        "• **Candidate Rules:** Strict qualifications under Article 99 and vacation triggers under Article 103.\n"
                        "• **Field Administration:** Returning Officers (constituency), Presiding Officers (station), Polling Clerks, and Party Agents."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Electoral integrity relies on independent election management and transparent polling procedures.\n"
                        "- Constitutional safeguards ensure candidates meet strict ethical and legal qualifications."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: Kenyan Elections",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Evolution from acclamation and mlolongo to the secret ballot.",
                        "2. Twelve functions of the IEBC under the Constitution.",
                        "3. Three types of elections (General, By-election, Fresh Presidential).",
                        "4. Qualifications and disqualifications for parliamentary candidates.",
                        "5. Roles of Returning Officers and Presiding Officers."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Quick Knowledge Check: Election Officials",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Identify the official responsible for each duty:",
                    "items": [
                        "1. Distributes election materials across a constituency and declares the winning MP -> **Returning Officer**",
                        "2. Manages a polling station and marks voters' fingers with indelible ink -> **Presiding Officer**",
                        "3. Observes the counting of ballots on behalf of a political party -> **Party Agent**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Constitutional Thresholds for Presidential Elections",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "The Double Constitutional Threshold (Article 138)",
                "content": {
                    "text": (
                        "**To be declared validly elected as President of Kenya, a candidate MUST secure:**\n"
                        "1. More than **50% of the total votes cast** nationally (50% + 1 vote).\n"
                        "2. At least **25% of the votes cast** in each of more than half of the 47 counties (at least 24 counties).\n\n"
                        "**Democratic Purpose:** Ensures the President enjoys broad national legitimacy and regional support, preventing narrow ethnic rule."
                    )
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "The 2007 Electoral Crisis, Kriegler Commission, and Post-Crisis Reforms",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Kriegler Commission and 2010 Reforms",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Identify the structural weaknesses and failures of the 2007 electoral process reported by the Kriegler Commission (IREC)\n"
                        "- Analyze the causes and consequences of the 2007 post-election crisis\n"
                        "- Explain the six fundamental electoral principles established under Chapter 7 of the 2010 Constitution\n"
                        "- Detail the key election legislation governing modern Kenyan elections (Elections Act, Election Offences Act)"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Kriegler Commission (IREC)",
                "content": {
                    "term": "Kriegler Commission (IREC)",
                    "definition": (
                        "The Independent Electoral Review Committee chaired by retired South African Judge Johann Kriegler, established "
                        "under the National Accord to investigate the administrative failures of the 2007 elections and recommend comprehensive reforms."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Documentary: Adoption of Kriegler Recommendations",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: Adoption of Kriegler Commission Recommendations",
                "content": {
                    "url": "https://www.youtube.com/watch?v=Lb2A-UyRPtA",
                    "text": "Examine how the Kenyan Cabinet and Parliament adopted the Kriegler Commission report, dissolving the ECK and establishing the modern IEBC and biometric voter registration.",
                    "author": "Citizen TV Kenya / Historical Archives",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Weaknesses in the 2007 Electoral Process (Kriegler Findings)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Eight Major Weaknesses of the 2007 Elections (Point-Form)",
                "content": {
                    "steps": [
                        "1. Inaccurate Voters' Register: Contained over 1.2 million deceased voters ('ghost voters') and excluded over 30% of eligible youth and women.",
                        "2. Extreme Constituency Population Disparities: Disproportionate voter populations (Embakasi >200,000 vs. Mandera East <20,000) violated the 'one person, one vote' principle.",
                        "3. Ballot Stuffing and Turnout Inaccuracies: Recorded voter turnouts exceeded 100% of registered voters in several political strongholds.",
                        "4. Exclusive Political Strongholds: Zones of intimidation where rival political parties were denied access and independent monitoring was impossible.",
                        "5. Defective Results Transmission: Lack of secure, transparent electronic tallying led to conflicting numbers, delayed results, and intense public suspicion.",
                        "6. Incompetence of ECK Staff: Temporary polling staff and permanent commissioners lacked technical competence and training.",
                        "7. Partisan ECK Appointments: Unilateral appointment of commissioners by the President shortly before the election eroded public trust.",
                        "8. Biased Media and Hate Speech: Partisan vernacular media amplified ethnic hostility and propagated hate speech."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Phenomenon of 'Ghost Voting' and Ballot Stuffing",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "How Inaccurate Registers Corrupted the Vote",
                "content": {
                    "text": (
                        "- **Ghost Voting:** Because over 1.2 million deceased citizens remained on the manual paper roll, corrupt polling clerks and party agents marked ballots in their names in unmonitored stations.\n"
                        "- **Turnout Exceeding 100%:** In some constituencies, the number of cast ballots exceeded the total registered voters, proving ballot stuffing.\n"
                        "- **Modern Solution:** The implementation of the **Kenya Integrated Elections Management System (KIEMS)** utilizing biometric fingerprint and facial verification."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Electoral Principles Under the 2010 Constitution (Chapter 7)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Chapter 7 Constitutional Electoral Principles",
                "content": {
                    "headers": ["Constitutional Principle", "Legal Requirement", "Practical Implementation"],
                    "rows": [
                        ["Freedom of Choice", "Citizens exercise political rights without coercion.", "Secret ballot voting in enclosed private booths."],
                        ["Two-Thirds Gender Rule", "No elective public body shall have more than 2/3 of one gender.", "47 County Woman Representatives and party nomination lists."],
                        ["Fair Representation of Minorities", "Inclusion of PWDs, youth, and marginalized groups.", "Special nomination seats in Senate, National Assembly, and MCAs."],
                        ["Universal Suffrage", "Equal value of the vote ('one person, one vote').", "Boundary reviews to balance constituency population densities."],
                        ["Free and Fair Elections", "Elections free from violence, intimidation, and bribery.", "Enforcement of the Electoral Code of Conduct and Election Offences Act."],
                        ["Independent Administration", "Elections conducted transparently and accurately.", "Autonomous IEBC with biometric voter verification and public portal results."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Key Election Legislation in Kenya",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Three Pillars of Kenyan Electoral Law",
                "content": {
                    "steps": [
                        "1. The Constitution of Kenya 2010: Establishes the right to vote, the IEBC under Chapter 15, and electoral principles under Chapter 7.",
                        "2. The Elections Act (Cap 7): Regulates procedures for voter registration, party nominations, polling, tallying, and resolving election petitions.",
                        "3. The Election Offences Act: Imposes severe criminal penalties for voter bribery, ballot box destruction, hate speech, and abuse of state resources."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Primary Evidence Activity: The Kriegler Report Analysis",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Documentary Analysis: Excerpt from the Kriegler Report (2008)",
                "content": {
                    "text": (
                        "*> 'The voter register was so severely compromised that it contained the names of over one million dead people. "
                        "This allowed for ghost voting where corrupt polling clerks could easily issue ballots in the names of the deceased.'*\n\n"
                        "**Critical Analysis Questions:**\n"
                        "1. Why was a manual paper register vulnerable to phantom voting?\n"
                        "2. How does biometric electronic verification (KIEMS) eliminate ghost voting?\n"
                        "3. Why must party agents verify the physical serial numbers of sealed ballot boxes?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Interactive Classification: Electoral Failures vs. Modern Reforms",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the 2007 Failure to Its 2010 Reform",
                "content": {
                    "instruction": "Match each 2007 weakness with its constitutional remedy:",
                    "items": [
                        "1. 1.2 million deceased voters on roll -> **Biometric Voter Registration & Periodic Register Purges**",
                        "2. President unilaterally appoints commissioners -> **Bipartisan Selection Panel & Parliamentary Vetting**",
                        "3. Embakasi (200K) vs. Mandera East (20K) disparity -> **Mandatory Boundary Reviews (8–12 Years)**",
                        "4. Opaque results transmission causing suspicion -> **Public Web Results Portal & Scanned Form 34A Transmission**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "KCSE Examination Coaching: Kriegler Commission Weaknesses",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Weaknesses in the 2007 Electoral Process Identified by the Kriegler Commission (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Gross Inaccuracies in the Voter Register:** The register contained over 1.2 million deceased persons which facilitated ghost voting and excluded 30% of eligible voters. (2 marks)\n\n"
                        "2. **Severe Constituency Population Disparities:** Huge population imbalances between constituencies violated the principle of equal vote value. (2 marks)\n\n"
                        "3. **Defective Results Tallying and Transmission:** The ECK lacked an electronic, transparent system for transmitting results, causing conflicting counts and public distrust. (2 marks)\n\n"
                        "4. **Partisan and Unilateral Appointment of Commissioners:** The President appointed commissioners without consulting opposition stakeholders shortly before elections, destroying neutrality. (2 marks)\n\n"
                        "5. **Widespread Ballot Stuffing:** In several strongholds, voter turnouts officially recorded exceeded 100% of registered voters. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: Chapter 7 Principles",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: State Six Principles Governing the Electoral System in Kenya Under the 2010 Constitution (6 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (1 Mark per Point):**\n"
                        "1. Freedom of citizens to exercise their political rights without intimidation. (1 mark)\n"
                        "2. Not more than two-thirds of the members of elective public bodies shall be of the same gender. (1 mark)\n"
                        "3. Fair representation of persons with disabilities, youth, and marginalized communities. (1 mark)\n"
                        "4. Universal suffrage based on the aspiration for fair representation and equality of the vote. (1 mark)\n"
                        "5. Free and fair elections by secret ballot, free from violence and bribery. (1 mark)\n"
                        "6. Conducted by an independent body in a transparent, accountable, and accurate manner. (1 mark)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Check Your Understanding: Module 9.2",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 9.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Who chaired the Independent Electoral Review Committee (IREC) that investigated the 2007 general elections in Kenya?",
                            "options": [
                                "Justice Philip Waki",
                                "Justice Johann Kriegler",
                                "Kofi Annan",
                                "Samuel Kivuitu"
                            ],
                            "correct_answer": 1,
                            "explanation": "Retired South African Judge Johann Kriegler chaired the IREC (Kriegler Commission)."
                        },
                        {
                            "question": "What is the maximum proportion of members of the same gender permitted in elective public bodies under the Constitution?",
                            "options": [
                                "Half (50%)",
                                "Two-thirds (66.7%)",
                                "Three-quarters (75%)",
                                "One-third (33.3%)"
                            ],
                            "correct_answer": 1,
                            "explanation": "Article 81(b) establishes the two-thirds gender rule: no more than two-thirds of elective bodies may be of the same gender."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: 2007 Crisis & Post-Crisis Reforms",
                "content": {
                    "text": (
                        "• **2007 Failures:** Inaccurate register (1.2M dead), population disparities, ballot stuffing, defective tallying, partisan appointments.\n"
                        "• **Kriegler Report Impact:** Dissolution of ECK, creation of autonomous IEBC, transition to biometric verification.\n"
                        "• **Chapter 7 Principles:** Freedom of choice, 2/3 gender rule, inclusion of PWDs/youth, universal suffrage, secret ballot, independent administration."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Democratic elections require neutral administration, transparent counting, and verifiable biometric rolls.\n"
                        "- Post-conflict legal reforms transformed Kenya's electoral architecture into a constitutionally anchored system."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Revision Checklist: 2007 Crisis and Reforms",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Eight findings of the Kriegler Commission regarding the 2007 elections.",
                        "2. Six electoral principles under Chapter 7 of the 2010 Constitution.",
                        "3. Three main electoral statutes in Kenya.",
                        "4. Meaning and application of the two-thirds gender rule."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Quick Knowledge Check: Electoral Principles",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. The Kriegler Commission recommended maintaining the manual paper voter register -> **False (recommended electronic biometric register)**",
                        "2. In 2007, some polling stations recorded voter turnouts exceeding 100% -> **True**",
                        "3. The Election Offences Act penalizes voter bribery and ballot destruction -> **True**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "The Waki Commission vs. The Kriegler Commission",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Distinguishing the Two 2008 Post-Crisis Inquiries",
                "content": {
                    "headers": ["Inquiry Commission", "Chairperson", "Specific Mandate & Focus"],
                    "rows": [
                        ["Kriegler Commission (IREC)", "Judge Johann Kriegler", "Investigated the electoral process, ECK administrative failures, tallying, and voter register flaws."],
                        ["Waki Commission (CIPEV)", "Justice Philip Waki", "Investigated the post-election violence, ethnic clashes, state security failures, and recommended prosecution of perpetrators."]
                    ]
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "The British Government and Electoral System",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The British Constitutional Monarchy",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain the concept of an unwritten constitution and identify its written and unwritten sources (Statutes, Common Law, Conventions)\n"
                        "- Describe the British electoral process, voter/candidate qualifications, and factors influencing election dates\n"
                        "- Analyze the structure and functions of the Monarchy, House of Commons, House of Lords, Executive, and Judiciary\n"
                        "- Discuss the doctrine of Parliamentary Supremacy and its practical limitations"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Constitutional Monarchy & Parliamentary System",
                "content": {
                    "term": "Constitutional Monarchy",
                    "definition": (
                        "A system of governance where a hereditary monarch serves as the symbolic Head of State, while political and executive "
                        "power is exercised by an elected Prime Minister and Cabinet drawn from the legislature."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Palace of Westminster: The Seat of British Democracy",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Palace of Westminster London",
                "content": {
                    "text": "The Palace of Westminster in London, meeting place of the House of Commons and the House of Lords, embodying Britain's parliamentary democracy.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/Palace_of_Westminster%2C_London_-_Feb_2007.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Palace_of_Westminster,_London_-_Feb_2007.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Educational Documentary: How the UK Parliament Works",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Official Guide: How the UK Parliament Works",
                "content": {
                    "url": "https://www.youtube.com/watch?v=SlPSAOa4vR4",
                    "text": "Explore the structural relationship between the Monarch, the House of Commons, and the House of Lords, and how legislation and government oversight are conducted.",
                    "author": "UK Parliament / Civic Series",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Concept and Sources of the Unwritten British Constitution",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Five Primary Sources of the British Constitution",
                "content": {
                    "steps": [
                        "1. Statutes (Acts of Parliament): Historic written laws including Magna Carta (1215), Petition of Right (1628), Habeas Corpus (1679), Bill of Rights (1689), and Representation of the People Acts.",
                        "2. Common Law (Case Law): Judicial rulings made by senior British courts over centuries that establish binding legal precedents.",
                        "3. Conventions: Unwritten traditions and customs followed as law (e.g., the monarch always assents to bills passed by Parliament).",
                        "4. Parliamentary Customs & Standing Orders: Internal procedures recorded in Hansard and Erskine May's treatise.",
                        "5. Authoritative Commentaries: Respected writings by legal scholars (Blackstone, Bagehot, Dicey)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The British Electoral Process and Voting System",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Features of British Elections",
                "content": {
                    "steps": [
                        "1. Multiparty Competition: Historically contested by the Conservative Party, Labour Party, and Liberal Democrats.",
                        "2. First-Past-The-Post (FPTP): The candidate with the most votes in a single-member constituency wins (plurality system).",
                        "3. Flexible Election Dates: The Prime Minister historically determined the election date within a 5-year limit, influenced by economic health, legislative progress, and popularity polls.",
                        "4. Government Formation: The monarch invites the leader of the majority party in the House of Commons to become Prime Minister and form a government."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Qualifications and Disqualifications in Great Britain",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "British Voters and Parliamentary Candidates",
                "content": {
                    "headers": ["Category", "Qualifications", "Disqualifications"],
                    "rows": [
                        ["Voters", "• British, Commonwealth, or Irish citizen resident in UK.\n• At least 18 years of age.\n• Registered on local electoral roll.", "• Peers in the House of Lords.\n• Certified persons of unsound mind.\n• Convicts serving prison terms.\n• Persons convicted of election fraud (5-year ban)."],
                        ["Candidates (House of Commons)", "• British, Commonwealth, or Irish citizen.\n• At least 21 years of age (historically).\n• Nominated by party or independent.\n• Deposit £500 (refunded if >5% vote secured).", "• Peers of the Realm (House of Lords members).\n• Clergy of Anglican, Scottish, Irish, and Catholic churches.\n• Foreign aliens.\n• Bankrupts and serving convicts.\n• Active military and police personnel."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The Monarchy (The Crown) and Royal Prerogatives",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Functions of the British Monarchy",
                "content": {
                    "steps": [
                        "1. Appoints the Prime Minister: Formally invites the majority leader in the House of Commons to form a government.",
                        "2. Summons and Dissolves Parliament: Prorogues and dissolves Parliament on the Prime Minister's advice.",
                        "3. Grants Royal Assent: Signs bills passed by both Houses of Parliament to make them law.",
                        "4. Head of the Commonwealth: Serves as the symbolic leader of the 56-member Commonwealth.",
                        "5. Appoints Senior Officials: Formally appoints judges, military commanders, and Church of England bishops.",
                        "6. Confers National Honours: Awards peerages, knighthoods, and medals for distinguished public service."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "The Legislature: House of Commons vs. House of Lords",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Bicameral Parliament: Commons vs. Lords",
                "content": {
                    "headers": ["Feature", "House of Commons (Lower House)", "House of Lords (Upper House)"],
                    "rows": [
                        ["Membership", "650 directly elected Members of Parliament (MPs).", "~1,200 non-elected members: Hereditary Peers, Life Peers, Spiritual Peers (Bishops), Law Lords."],
                        ["Primary Power", "Supreme legislative power; introduces and amends all public bills.", "Scrutinizes and revises bills passed by the Commons."],
                        ["Financial Control", "Exclusive power to approve taxes and government expenditure (budget).", "Cannot veto or alter financial/money bills."],
                        ["Checking Executive", "Can pass a vote of no confidence to force the Prime Minister and Cabinet to resign.", "Can delay non-financial legislation to allow public debate, but cannot defeat the Commons."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "The Executive and the British Civil Service",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Executive Principles and Civil Service Norms",
                "content": {
                    "steps": [
                        "1. The Prime Minister: Head of Government, leader of the House of Commons, appoints and dismisses Cabinet ministers.",
                        "2. Collective Cabinet Responsibility: All ministers must publicly support cabinet decisions, maintain confidentiality, and resign if they cannot support government policy.",
                        "3. Civil Service Anonymity: Civil servants remain behind the scenes; ministers take all public praise or censure for policies.",
                        "4. Civil Service Impartiality: Civil servants serve whatever political party is in power with absolute professional neutrality.",
                        "5. Civil Service Permanence: Civil servants do not lose their jobs when the governing political party changes."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Doctrine of Parliamentary Supremacy and Its Limitations",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Parliamentary Supremacy vs. Practical Limitations",
                "content": {
                    "headers": ["Doctrine of Parliamentary Supremacy", "Practical Real-World Limitations"],
                    "rows": [
                        ["1. Parliament can make, amend, or repeal any law whatsoever.", "1. Public Opinion: Unpopular laws risk mass protest and defeat at the next general election."],
                        ["2. No court of law can declare an Act of Parliament unconstitutional or void.", "2. Moral Standards: Laws must conform to the prevailing cultural and moral values of society."],
                        ["3. A sitting Parliament cannot bind future Parliaments; all Parliaments have equal sovereign power.", "3. International Law: Domestic laws must align with international treaties and obligations ratified by Britain."],
                        ["4. Parliament has unlimited legal authority over all state institutions.", "4. Institutional Consultation: Major bodies (trade unions, churches, business federations) must be consulted before laws are passed."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Check Your Understanding: Module 9.3",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 9.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which historic British statute in 1215 forced King John to respect the legal privileges of the nobility and refrain from arbitrary taxation?",
                            "options": [
                                "The Bill of Rights",
                                "The Magna Carta",
                                "The Habeas Corpus Act",
                                "The Act of Settlement"
                            ],
                            "correct_answer": 1,
                            "explanation": "Magna Carta (1215) is the foundation of British constitutional liberty and parliamentary consent for taxation."
                        },
                        {
                            "question": "What happens if the House of Commons passes a vote of no confidence against the Prime Minister?",
                            "options": [
                                "The monarch assumes total dictatorial power",
                                "The Prime Minister and Cabinet must resign or dissolve Parliament for a general election",
                                "The House of Lords takes over the government",
                                "The Supreme Court appoints a new cabinet"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under parliamentary democracy, losing a vote of no confidence forces the government to resign or call a general election."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Functions of the House of Commons",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Functions of the House of Commons in Great Britain (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Making and Amending Laws:** Debates, reviews, and passes all primary legislation and statutory instruments for the United Kingdom. (2 marks)\n\n"
                        "2. **Financial Control (Budget Approval):** Controls government taxation and public expenditure. No tax can be levied without the consent of the Commons. (2 marks)\n\n"
                        "3. **Checking the Executive:** Holds the Prime Minister and Cabinet accountable through Prime Minister's Questions (PMQs), committee inquiries, and parliamentary debates. (2 marks)\n\n"
                        "4. **Power of Removal (Vote of No Confidence):** Has the constitutional power to pass a vote of no confidence, forcing the ruling government to resign. (2 marks)\n\n"
                        "5. **Representing Public Grievances:** Elected MPs represent constituency interests, presenting petitions and debating issues affecting citizens. (2 marks)\n\n"
                        "6. **Directing National Policy:** Provides a platform for debating major domestic development programs, defense policies, and foreign relations. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: British Government and Elections",
                "content": {
                    "text": (
                        "• **Unwritten Constitution:** Derived from statutes (Magna Carta, Bill of Rights), common law, conventions, and customs.\n"
                        "• **Elections:** First-Past-The-Post in single-member seats; £500 deposit; disqualification of peers, clergy, convicts.\n"
                        "• **Government Organs:** Monarch (ceremonial Head of State), Commons (supreme legislature & budget), Lords (revising chamber), Executive (PM & Cabinet under collective responsibility).\n"
                        "• **Parliamentary Supremacy:** Unlimited legal authority, practically constrained by public opinion, morality, and international treaties."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Britain pioneered the parliamentary model where the executive is drawn directly from and accountable to the legislature.\n"
                        "- Conventions and historical traditions possess binding constitutional authority in the absence of a single codified text."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: British Governance",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Five sources of the unwritten British constitution.",
                        "2. Qualifications and disqualifications for voters and MPs in Great Britain.",
                        "3. Six functions of the British Monarchy.",
                        "4. Differences between the House of Commons and House of Lords.",
                        "5. Concept of Parliamentary Supremacy and four practical limitations."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Quick Knowledge Check: British Parliament",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Identify the institution or concept:",
                    "items": [
                        "1. Upper house in Britain comprising hereditary and life peers -> **House of Lords**",
                        "2. Principle that all cabinet ministers must publicly stand together behind policy -> **Collective Responsibility**",
                        "3. Legal doctrine stating no court can strike down an Act of Parliament -> **Parliamentary Supremacy**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Comparison: Constitutional Supremacy vs. Parliamentary Supremacy",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Constitutional Supremacy (Kenya/USA) vs. Parliamentary Supremacy (UK)",
                "content": {
                    "headers": ["Feature", "Constitutional Supremacy (Kenya & USA)", "Parliamentary Supremacy (Great Britain)"],
                    "rows": [
                        ["Supreme Authority", "The written, codified Constitution is the supreme law.", "The Parliament is the supreme legal lawmaker."],
                        ["Judicial Review", "Courts can declare any Act of Parliament unconstitutional and void.", "No court has the power to strike down or invalidate an Act of Parliament."],
                        ["Amendment Process", "Rigid; requires special parliamentary majorities or national referenda.", "Flexible; Parliament amends constitutional laws through ordinary legislative majority."]
                    ]
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "The United States Government and Electoral System",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: American Federalism and Checks & Balances",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define a federal system and explain the advantages and disadvantages of federalism in the USA\n"
                        "- Detail the US presidential electoral process (Primaries, National Conventions, Running Mate, Electoral College, Inauguration)\n"
                        "- Describe the composition and powers of Congress (Senate vs. House of Representatives)\n"
                        "- Analyze the doctrine of Separation of Powers and the mechanism of Checks and Balances among the three arms"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Federal Presidential Republic",
                "content": {
                    "term": "Federal System",
                    "definition": (
                        "A governance structure where constitutional sovereignty is divided between a central national (federal) government "
                        "and 50 autonomous state governments, each with its own executive, legislature, and judicial system."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "United States Capitol: The Heart of US Legislation",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "United States Capitol Washington DC",
                "content": {
                    "text": "The United States Capitol building in Washington, D.C., meeting place of the US Congress (the Senate and House of Representatives).",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/0/0e/United_States_Capitol_-_west_front_edit.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:United_States_Capitol_-_west_front_edit.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Educational Video: The US Electoral College Explained",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Educational Documentary: The US Electoral College and Presidential Elections",
                "content": {
                    "url": "https://www.youtube.com/watch?v=ajavsMbCapY",
                    "text": "Understand how the US indirect presidential election system works, how electors are allocated per state, and the winner-take-all rule.",
                    "author": "Vox / Educational Explainer",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Division of Powers in the US Federal System",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Federal Government vs. State Governments",
                "content": {
                    "headers": ["Level of Government", "Exclusive Constitutional Powers", "Prohibitions & Restrictions"],
                    "rows": [
                        ["Federal Government (Washington, D.C.)", "• National defense & armed forces\n• Foreign policy and international treaties\n• Printing and coining currency\n• Regulating interstate and foreign commerce", "Cannot infringe upon powers reserved to the states under the 10th Amendment."],
                        ["50 State Governments", "• Headed by elected Governors\n• State police and state court systems\n• Local education, public health, and roads\n• Administering state and federal elections", "• Cannot sign foreign treaties or alliances\n• Cannot coin money or print currency\n• Cannot levy import/export tariffs\n• Cannot maintain independent armies"]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Advantages and Disadvantages of a Federal System (High-Yield KCSE)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Advantages vs. Disadvantages of Federalism",
                "content": {
                    "headers": ["Advantages of Federalism (6 Points)", "Disadvantages of Federalism"],
                    "rows": [
                        ["1. Protection of Smaller States: Equal Senate representation prevents domination by large states.", "1. Secessionist Threats: Sharp regional divisions can spark secessionist conflicts."],
                        ["2. Separate Identities with Unity: Allows diverse states to maintain local laws while uniting under one flag.", "2. Leadership Complexity: Requires delicate statesmanship to manage state-federal tensions."],
                        ["3. Enhanced Collective Security: Common defense forces protect all states from external aggression.", "3. Regional Disparities: Wealthy states develop faster than poorer, resource-scarce states."],
                        ["4. Resource Pooling: Combines industrial and natural resources into a powerful national economy.", "4. Duplication of Costs: Maintaining 50 state governments plus the federal tier is expensive."],
                        ["5. Tariff Elimination: Free interstate commerce drives rapid domestic market expansion.", "5. Conflicting Laws: Different state criminal/civil laws can create legal confusion across state borders."],
                        ["6. Amplified Global Influence: The nation speaks with a single, influential diplomatic voice.", ""]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "The US Presidential Election Process",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Six Stages of US Presidential Elections",
                "content": {
                    "steps": [
                        "1. Primary Elections & Caucuses (Jan–June): Voters across 50 states vote for party delegates pledged to presidential candidates.",
                        "2. National Party Conventions (July/August): Major parties officially endorse their presidential nominee.",
                        "3. Running Mate Selection: Presidential nominee chooses a Vice-Presidential running mate.",
                        "4. National Campaign & Debates (Sept–Oct): Candidates engage in nationwide campaigns and televised presidential debates.",
                        "5. Polling Day & Electoral College (Nov): General election held on the first Tuesday after the first Monday of November; voters vote for electors under the winner-take-all rule.",
                        "6. Inauguration (January 20): President is officially sworn into office by the Chief Justice on the steps of the US Capitol."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The US Congress: Senate vs. House of Representatives",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Bicameral Congress: Senate vs. House of Representatives",
                "content": {
                    "headers": ["Feature", "The Senate (Upper House)", "The House of Representatives (Lower House)"],
                    "rows": [
                        ["Total Membership", "100 Senators (2 Senators per state, regardless of population).", "435 Representatives (allocated based strictly on state population)."],
                        ["Term of Office", "6-year term (1/3 of Senate elected every 2 years).", "2-year term (entire House elected every 2 years)."],
                        ["Candidate Qualifications", "Must be at least 30 years old, 9 years a US citizen, and resident of state.", "Must be at least 25 years old, 7 years a US citizen, and resident of state."],
                        ["Exclusive Constitutional Powers", "• Approves presidential appointments (judges, cabinet, ambassadors)\n• Ratifies international treaties by 2/3 majority\n• Tries impeachment cases", "• Initiates all revenue/tax bills\n• Initiates impeachment charges against the President or judges"]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "The Executive Branch: The US President",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Key Functions of the President of the United States",
                "content": {
                    "steps": [
                        "1. Head of State and Government: Chief executive responsible for enforcing federal laws.",
                        "2. Commander-in-Chief: Supreme commander of all US Army, Navy, Air Force, and Marines.",
                        "3. Chief Diplomat: Negotiates treaties with foreign nations and appoints ambassadors (subject to Senate approval).",
                        "4. Legislative Role: Delivers the State of the Union address, proposes legislation, and has the power to sign or veto bills passed by Congress.",
                        "5. Judicial Powers: Appoints Supreme Court and federal judges (with Senate approval) and grants presidential pardons for federal crimes.",
                        "6. Appoints the Cabinet: Appoints heads of federal executive departments (Cabinet Secretaries are drawn from outside Congress)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "The Judicial Branch and Judicial Review",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The US Supreme Court and Constitutional Adjudication",
                "content": {
                    "steps": [
                        "1. Structure: Comprises a Chief Justice and eight (8) Associate Justices appointed for life by the President with Senate confirmation.",
                        "2. Supreme Court of Appeal: Final appellate court for all federal and state constitutional cases.",
                        "3. Dispute Resolution: Resolves legal disputes between different states, or between the federal government and state governments.",
                        "4. Judicial Review: Has the supreme constitutional power to declare Acts of Congress or Executive Orders of the President unconstitutional and void."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "System of Checks and Balances in the USA",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "How the Three Branches Check Each Other",
                "content": {
                    "headers": ["Branch Checked", "Checked By", "Constitutional Check Mechanism"],
                    "rows": [
                        ["The President (Executive)", "Congress (Legislature)", "• Can override presidential veto by 2/3 vote in both Houses.\n• Senate must approve presidential appointments and treaties.\n• Can withhold budget funds or impeach the President."],
                        ["Congress (Legislature)", "The President (Executive)", "• President can veto bills passed by Congress.\n• President can call special sessions of Congress."],
                        ["Congress & President", "Supreme Court (Judiciary)", "• Supreme Court can declare Acts of Congress or Executive Orders unconstitutional (Judicial Review)."],
                        ["Supreme Court (Judiciary)", "President & Congress", "• President appoints judges with Senate approval.\n• Congress can amend the Constitution or impeach judges."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Check Your Understanding: Module 9.4",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 9.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "How many Senators represent each US state in the Senate?",
                            "options": [
                                "Proportional to population size",
                                "Two (2) Senators per state",
                                "Four (4) Senators per state",
                                "One (1) Senator per state"
                            ],
                            "correct_answer": 1,
                            "explanation": "Each of the 50 US states is represented by exactly 2 Senators, ensuring equality between states."
                        },
                        {
                            "question": "What proportion of Congress must vote to override a presidential veto?",
                            "options": [
                                "Simple majority (50% + 1)",
                                "Two-thirds (2/3) majority in both Houses",
                                "Three-quarters (3/4) majority in the Senate",
                                "Unanimous vote"
                            ],
                            "correct_answer": 1,
                            "explanation": "Article I of the US Constitution requires a two-thirds majority in both the House and Senate to override a veto."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Advantages of Federalism",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Advantages of a Federal System of Government in the USA (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Protects Smaller States from Domination:** Equal representation in the Senate ensures small states have equal legislative power with large states. (2 marks)\n\n"
                        "2. **Maintains Separate Regional Identities with Unity:** Allows diverse states to retain local laws and customs while united under one nation. (2 marks)\n\n"
                        "3. **Provides Enhanced Collective Security:** Unites state resources under a single powerful federal defense force against external enemies. (2 marks)\n\n"
                        "4. **Facilitates Resource Pooling:** Combines natural, agricultural, and industrial resources from 50 states into a rich national economy. (2 marks)\n\n"
                        "5. **Eliminates Trade Barriers (Free Interstate Commerce):** Removes internal tariffs and customs duties between states, expanding commerce. (2 marks)\n\n"
                        "6. **Amplifies International Influence:** Enables 50 states to negotiate and act with a single powerful voice on the world diplomatic stage. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: US Government and Elections",
                "content": {
                    "text": (
                        "• **Federalism:** Divided sovereignty between Federal government and 50 states; protects small states and pools resources.\n"
                        "• **Presidential Elections:** Primaries, National Conventions, Electoral College indirect election, Jan 20 Inauguration.\n"
                        "• **Congress:** Senate (100 members, 2 per state, 6-yr term) vs. House of Representatives (435 members, population-based, 2-yr term).\n"
                        "• **Checks & Balances:** Presidential veto, Congressional veto override (2/3), Senate confirmations, Supreme Court Judicial Review."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- The US system is anchored in strict separation of powers between executive, legislative, and judicial branches.\n"
                        "- Federalism allows extensive local self-governance while creating a formidable unified superpower."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: US Governance",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Six advantages and three disadvantages of federalism in the USA.",
                        "2. Six stages of the US presidential election cycle.",
                        "3. Differences between the US Senate and House of Representatives.",
                        "4. Functions of the US President as Commander-in-Chief and Chief Diplomat.",
                        "5. Checks and balances mechanism operating among the three arms."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Quick Knowledge Check: US Government",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Identify the US office or term:",
                    "items": [
                        "1. The date on which the US President is inaugurated -> **January 20th**",
                        "2. Minimum age required to run for US President -> **35 years old**",
                        "3. The power of the Supreme Court to declare laws unconstitutional -> **Judicial Review**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Comparison: US President vs. British Prime Minister",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "US President vs. British Prime Minister",
                "content": {
                    "headers": ["Feature", "US President", "British Prime Minister"],
                    "rows": [
                        ["Head of State / Govt", "Both Head of State and Head of Government.", "Head of Government only (Monarch is Head of State)."],
                        ["Cabinet Selection", "Appointed from outside Congress (strict separation).", "Appointed from within Parliament (Commons/Lords)."],
                        ["Legislative Veto", "Has direct constitutional veto power over congressional bills.", "Has no veto; relies on party majority in Commons."],
                        ["Removal from Office", "Through impeachment by Congress for high crimes.", "Through a vote of no confidence by House of Commons."]
                    ]
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Indian Government, Global Comparative Governance, and Master Synthesis",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Indian Governance and Master Synthesis",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Describe the structure of the Indian federal parliamentary republic and functions of the Election Commission of India\n"
                        "- Explain the composition and functions of Sansad (Lok Sabha and Rajya Sabha)\n"
                        "- Compare the executive roles of the President of India and the Prime Minister of India\n"
                        "- Synthesize the four governance models (Kenya, Great Britain, USA, India) across all constitutional dimensions"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Federal Parliamentary Republic",
                "content": {
                    "term": "Federal Parliamentary Republic",
                    "definition": (
                        "A hybrid system combining a federal division of powers between union and state governments (like the USA) with a "
                        "parliamentary executive where the Prime Minister leads the majority in the legislature (like Great Britain)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Sansad Bhavan: The Indian Parliament in New Delhi",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Sansad Bhavan New Delhi",
                "content": {
                    "text": "Sansad Bhavan in New Delhi, the parliament house of India, seating the Lok Sabha and Rajya Sabha in the world's largest democracy.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Sansad_Bhavan%2C_Delhi%2C_BNK.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sansad_Bhavan,_Delhi,_BNK.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Educational Documentary: Structure of the Indian Parliament",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Academic Analysis: Indian Parliament (Lok Sabha & Rajya Sabha) Explained",
                "content": {
                    "url": "https://www.youtube.com/watch?v=pb8b87e1re4",
                    "text": "Explore the bicameral structure of Sansad, the composition of the Lok Sabha and Rajya Sabha, and the constitutional role of the President of India.",
                    "author": "BYJU'S IAS / Political Science Series",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Indian Federal System: Union vs. State Governments",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Structure of the Indian Federation",
                "content": {
                    "steps": [
                        "1. The Union Government (New Delhi): Holds exclusive authority over defense, foreign affairs, atomic energy, and railways.",
                        "2. State Governments: Headed by Governors (appointed by the President) and administered by Chief Ministers (leaders of the majority in state assemblies).",
                        "3. State Powers: Maintain public order, local police forces, state healthcare, agriculture, and local infrastructure.",
                        "4. President's Rule: Unlike the US, the central Union Government can suspend a state administration during emergencies or breakdown of constitutional order."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Eight Functions of the Election Commission of India (High-Yield KCSE)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mandate of the Election Commission of India",
                "content": {
                    "steps": [
                        "1. Preparing and Updating Electoral Rolls: Registers eligible voters across all states and union territories.",
                        "2. Scheduling Election Timetables: Sets official dates and multi-phase polling schedules for national and state elections.",
                        "3. Establishing Polling Stations: Sets up hundreds of thousands of secure polling stations utilizing schools and civil servants.",
                        "4. Allocating Party Symbols: Registers and assigns distinct graphical symbols to political parties (essential for illiterate voters).",
                        "5. Scrutinizing Candidate Nominations: Accepts or rejects candidate nomination papers based on legal criteria.",
                        "6. Counting Votes and Announcing Winners: Superintends the counting of electronic ballots and officially declares winners.",
                        "7. Delimiting Boundaries: Reviews and adjusts parliamentary and assembly constituency boundaries.",
                        "8. Publishing Official Reports: Compiles and publishes comprehensive statistical reports on election outcomes."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Structure of the Indian Parliament (Sansad)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Lok Sabha vs. Rajya Sabha",
                "content": {
                    "headers": ["Feature", "Lok Sabha (House of the People - Lower House)", "Rajya Sabha (Council of States - Upper House)"],
                    "rows": [
                        ["Membership", "545 members (543 directly elected in single-member seats + 2 nominated Anglo-Indians).", "Max 250 members (238 elected by State Legislative Assemblies + 12 nominated by President)."],
                        ["Term of Office", "5-year term (can be dissolved earlier by President on PM's advice).", "Permanent body; 6-year term for members (1/3 retires every 2 years)."],
                        ["Candidate Age", "Minimum 25 years of age.", "Minimum 30 years of age."],
                        ["Financial Powers", "Exclusive control over Money/Budget Bills; initiates revenue legislation.", "Cannot reject or amend Money Bills (can only suggest amendments within 14 days)."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Executive Leadership in India: President vs. Prime Minister",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "President of India vs. Prime Minister of India",
                "content": {
                    "headers": ["Feature", "The President of India (Rashtrapati)", "The Prime Minister of India"],
                    "rows": [
                        ["Constitutional Role", "Ceremonial Head of State and Commander-in-Chief.", "Real Head of Government and Chief Executive."],
                        ["Election Method", "Elected indirectly by an Electoral College (Parliament + State Assemblies).", "Appointed by President as leader of the majority party in Lok Sabha."],
                        ["Powers & Duties", "• Formally appoints PM and state Governors\n• Nominates 12 Rajya Sabha members\n• Declares national/state emergency\n• Acts strictly on PM's binding advice.", "• Leads the Cabinet and Lok Sabha\n• Formulates domestic and foreign policies\n• Advises the President on all key state appointments\n• Directs federal administration."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Master Global Comparative Matrix: Kenya, UK, USA, India",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Global Comparison of Governance Systems",
                "content": {
                    "headers": ["Country", "Constitution Type", "Executive System", "Legislative Structure", "Head of Judiciary", "Supremacy Doctrine"],
                    "rows": [
                        ["Kenya", "Written, rigid", "Presidential (President & Deputy President)", "Bicameral (National Assembly & Senate)", "Supreme Court (Chief Justice)", "Constitutional Supremacy"],
                        ["Great Britain", "Unwritten, flexible", "Parliamentary (Monarch Head of State; PM Head of Govt)", "Bicameral (House of Commons & House of Lords)", "Supreme Court (historically Law Lords)", "Parliamentary Supremacy"],
                        ["United States", "Written, rigid", "Presidential (President & Vice President)", "Bicameral (Senate & House of Representatives)", "Supreme Court (Chief Justice)", "Constitutional Supremacy"],
                        ["India", "Written, rigid", "Parliamentary Federal (President Head of State; PM Head of Govt)", "Bicameral (Lok Sabha & Rajya Sabha)", "Supreme Court (Chief Justice)", "Constitutional Supremacy"]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Master KCSE Examination Paper 1 (Section C, 10 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 1: Functions of the Election Commission of India (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Prepares and Updates Electoral Rolls:** Continuously registers eligible voters and purges registers across all states and union territories. (2 marks)\n\n"
                        "2. **Schedules Election Timetables:** Formulates and officially announces dates and phases for parliamentary and state assembly elections. (2 marks)\n\n"
                        "3. **Allocates Party Symbols:** Assigns unique graphical symbols to registered political parties to aid illiterate voters in identifying candidates. (2 marks)\n\n"
                        "4. **Scrutinizes Candidate Nominations:** Verifies candidate affidavits, declarations of assets, and legal eligibility to clear or disqualify candidates. (2 marks)\n\n"
                        "5. **Conducts and Supervises Polling:** Manages polling stations, electronic voting machines (EVMs), tallies ballots, and declares winners. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Master KCSE Examination Paper 2 (Section C, 12 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 2: Compare the Legislative Systems of India and Great Britain (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer:**\n\n"
                        "- **Similarities (6 Marks):**\n"
                        "  1. Both parliaments are bicameral, comprising an elected lower house and a revising upper house.\n"
                        "  2. In both nations, the lower house (Lok Sabha in India, House of Commons in the UK) holds exclusive supremacy over money and budget bills.\n"
                        "  3. In both countries, the Prime Minister and Cabinet are drawn from the legislature and are answerable to the lower house.\n\n"
                        "- **Differences (6 Marks):**\n"
                        "  1. In Great Britain, the upper house (House of Lords) includes hereditary peers and church bishops, whereas India's upper house (Rajya Sabha) consists of state representatives and nominated experts.\n"
                        "  2. In India, Parliament operates under a written constitution with Judicial Review, whereas the British Parliament operates under Parliamentary Supremacy (no court can strike down an Act of Parliament).\n"
                        "  3. India represents a federal state with state assembly elections, whereas Britain is historically a unitary state."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Topic 9 Comprehensive Mastery Check (Part 1)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 9 Mastery Assessment (Part 1)",
                "content": {
                    "questions": [
                        {
                            "question": "What is the primary reason the Election Commission of India assigns graphical symbols to political parties?",
                            "options": [
                                "To decorate the ballot boxes",
                                "To enable illiterate voters to easily identify and vote for their preferred candidates",
                                "To comply with United Nations mandates",
                                "To reduce the cost of printing ballot papers"
                            ],
                            "correct_answer": 1,
                            "explanation": "Graphical symbols are crucial in India to ensure illiterate voters can identify party candidates on Electronic Voting Machines (EVMs)."
                        },
                        {
                            "question": "How many members of the Rajya Sabha are nominated by the President of India for distinguished service in art, science, and literature?",
                            "options": [
                                "2 members",
                                "12 members",
                                "20 members",
                                "50 members"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under the Indian Constitution, the President nominates exactly 12 members to the Rajya Sabha."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Topic 9 Comprehensive Mastery Check (Part 2)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 9 Mastery Assessment (Part 2)",
                "content": {
                    "questions": [
                        {
                            "question": "Which doctrine allows the US Supreme Court to declare Acts of Congress or Executive Orders unconstitutional?",
                            "options": [
                                "Parliamentary Supremacy",
                                "Judicial Review",
                                "Collective Responsibility",
                                "President's Rule"
                            ],
                            "correct_answer": 1,
                            "explanation": "Judicial Review enables the US Supreme Court to invalidate unconstitutional legislative acts and executive orders."
                        },
                        {
                            "question": "Which country operates under an unwritten constitution where Parliament is the supreme legal authority?",
                            "options": [
                                "The United States of America",
                                "Kenya",
                                "Great Britain (United Kingdom)",
                                "India"
                            ],
                            "correct_answer": 2,
                            "explanation": "Great Britain operates under an unwritten constitution governed by Parliamentary Supremacy."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Topic 9 Comprehensive Master Summary",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 9 Master Summary: Electoral Processes and Governance",
                "content": {
                    "text": (
                        "• **Kenya:** Chapter 7 electoral principles, IEBC 12 functions, candidate rules, 2007 Kriegler findings, 2010 constitutional supremacy.\n"
                        "• **Great Britain:** Unwritten constitution (statutes, common law, conventions), constitutional monarchy, House of Commons vs. Lords, Parliamentary Supremacy.\n"
                        "• **United States:** Federalism, 6 advantages, Presidential primaries & Electoral College, Congress (Senate vs. House), separation of powers, Checks and Balances.\n"
                        "• **India:** Federal parliamentary republic, Election Commission of India (symbols, scheduling), Lok Sabha vs. Rajya Sabha, President vs. Prime Minister."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Topic 9 Final Exam Revision Checklist",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Exam Revision Checklist: Topic 9",
                "content": {
                    "steps": [
                        "1. Twelve functions of the IEBC and causes/reforms of the 2007 election crisis.",
                        "2. Qualifications and disqualifications for Kenyan, British, American, and Indian representatives.",
                        "3. Five sources of the unwritten British constitution and limitations of Parliamentary Supremacy.",
                        "4. Six advantages of federalism in the USA and system of checks and balances.",
                        "5. Functions of the Election Commission of India and Sansad bicameral structure.",
                        "6. Master 4-country comparative matrix."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Exam Coaching: Mastering Comparative Governance Questions",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Top Tips for KCSE Comparative History Essays",
                "content": {
                    "text": (
                        "**Examiner's Guidelines:**\n"
                        "- **Use Comparative Connectors:** When comparing institutions (e.g., US Senate vs. UK House of Lords), use explicit comparative phrases (*'On the other hand'*, *'Whereas'*, *'In contrast'*).\n"
                        "- **State Exact Membership Figures:** Memorize key numbers: US Senate (100), US House (435), UK Commons (650), Indian Lok Sabha (545), Indian Rajya Sabha (250).\n"
                        "- **Distinguish Supremacy Principles:** Remember that Kenya, USA, and India practice **Constitutional Supremacy**, while Great Britain practices **Parliamentary Supremacy**."
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Grand Curriculum Synthesis: Form 4 History (Topics 1 to 9)",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Form 4 History Grand Synthesis: Complete Syllabus Mastery",
                "content": {
                    "text": (
                        "• **Topic 1 (The World War):** WWI & WWII origins, course, Allied victory, League of Nations & UN founding.\n"
                        "• **Topic 2 (International Relations):** UN, Commonwealth, NAM, Cold War superpowers & collapse.\n"
                        "• **Topic 3 (Co-operation in Africa):** Pan-Africanism, OAU founding 1963, African Union 2002, EAC, ECOWAS, COMESA.\n"
                        "• **Topic 4 (National Philosophies):** African Socialism (Sessional Paper 10), Harambee, Nyayoism.\n"
                        "• **Topic 5 (Developments in Kenya):** Centralization (1964–1982), multipartyism (1991), 2010 Constitution.\n"
                        "• **Topic 6 (Developments in Africa):** Inherited crises, DRC Congo Crisis & Mobutu, Tanzania Ujamaa & Kiswahili.\n"
                        "• **Topic 7 (Devolved Government):** Colonial local government, Cap 265 councils, 2010 Devolution revolution, 47 Counties.\n"
                        "• **Topic 8 (Public Revenue & Expenditure):** Article 201 principles, National Budget, taxation, constitutional funds, CRA, COB, Auditor-General, CBK.\n"
                        "• **Topic 9 (Electoral Processes & World Governance):** Kenya IEBC & 2007 reforms, UK Parliamentary Monarchy, US Federalism & Checks and Balances, Indian Sansad & Election Commission."
                    )
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "KCSE Examination Final Tip Sheet: Comparative Systems",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Top Examination Tips for Topic 9",
                "content": {
                    "steps": [
                        "1. Clearly distinguish between ex-ante election management (IEBC/ECI) and post-election judicial dispute settlement (Supreme Court).",
                        "2. In questions on US Federalism, highlight resource pooling, defense, and protection of smaller states.",
                        "3. In questions on the British Monarchy, emphasize that royal prerogatives are exercised on the binding advice of the Prime Minister.",
                        "4. In questions on the Indian Lok Sabha, explain its exclusive control over money bills.",
                        "5. Remember that only Great Britain has an unwritten, flexible constitution among the four nations."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "Final Milestone: Complete Form 4 History Course Mastery",
        "blocks": [
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Curriculum Completion Milestone",
                "content": {
                    "text": (
                        "Congratulations! You have completed the entire Form 4 History syllabus. "
                        "You are now fully equipped with deep conceptual knowledge, primary historical source analysis skills, "
                        "and master KCSE point-structure strategies for top national performance."
                    )
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "The Kenyan Electoral Process, IEBC, and Candidate Administration",
        "lesson_title": "The Kenyan Electoral Process: Voting Evolution, IEBC Structure & Functions, Candidate Rules, and Field Administration",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "The 2007 Electoral Crisis, Kriegler Commission Findings, and Post-Crisis Reforms",
        "lesson_title": "The 2007 Electoral Crisis: ECK Failures, Kriegler Commission Findings, and 2010 Constitutional Reforms",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "The British Government and Electoral System: Parliamentary Democracy and Unwritten Constitutionalism",
        "lesson_title": "The British Government: Unwritten Constitution, Electoral Process, Parliament, and Parliamentary Supremacy",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "The United States Government and Electoral System: Federalism, Separation of Powers, and Checks & Balances",
        "lesson_title": "The United States Government: Federalism, Presidential Elections, Congress, and Checks & Balances",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "The Indian Government, Global Comparative Governance, and Master Synthesis",
        "lesson_title": "The Indian Government: Federal Parliamentary System, Sansad, Global Comparative Matrix, and Course Synthesis",
        "pages": LESSON_5_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 9 (ELECTORAL PROCESS & WORLD GOVERNANCE)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        raise ValueError("Curriculum 844 not found.")
    print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    if not grade:
        raise ValueError("Grade Form 4 not found under Curriculum 844.")
    print(f"[*] Found Grade: {grade.name} (ID: {grade.id})")

    subject = Subject.objects.filter(grade=grade, name="History").first()
    if not subject:
        raise ValueError("Subject History not found under Grade Form 4.")
    print(f"[*] Found Subject: {subject.name} (ID: {subject.id})")

    with transaction.atomic():
        topic, topic_created = Topic.objects.get_or_create(
            subject=subject,
            name="The Electoral Process and Functions of Government in Other Parts of the World",
            defaults={"order": 9}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 9
            topic.save()
            print(f"[*] Found Existing Topic: {topic.name} (ID: {topic.id})")

        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for l_def in ALL_LESSONS:
            unit_order = l_def["unit_order"]
            unit_name = l_def["unit_name"]
            lesson_title = l_def["lesson_title"]
            pages = l_def["pages"]

            learning_unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                name=unit_name,
                defaults={"order": unit_order}
            )
            if not u_created:
                learning_unit.order = unit_order
                learning_unit.save()
                print(f"\n[*] Found Existing Learning Unit {unit_order}: {unit_name} (ID: {learning_unit.id})")
            else:
                print(f"\n[+] Created Learning Unit {unit_order}: {unit_name} (ID: {learning_unit.id})")

            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=learning_unit,
                title=lesson_title,
                defaults={
                    "status": "published",
                    "version": 1
                }
            )
            if not l_created:
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.save()
                print(f"  [*] Found Existing Lesson: {lesson_title} (ID: {lesson.id})")
            else:
                print(f"  [+] Created Lesson: {lesson_title} (ID: {lesson.id})")

            if replace:
                deleted_count, _ = lesson.blocks.all().delete()
                print(f"      [!] Cleared {deleted_count} existing blocks for clean rebuild.")
                LessonAsset.objects.filter(lesson=lesson).delete()

            block_order_counter = 10

            for page in pages:
                page_num = page["page_number"]
                page_title = page["page_title"]
                blocks = page["blocks"]
                total_pages += 1

                for comp_idx, block_info in enumerate(blocks, 1):
                    b_type = block_info["block_type"]
                    c_type = block_info["component_type"]
                    b_title = block_info.get("title", page_title)
                    b_content = clean_content_dict(block_info.get("content", {}))

                    block, b_created = LessonBlock.objects.get_or_create(
                        lesson=lesson,
                        page_number=page_num,
                        component_order=comp_idx,
                        defaults={
                            "block_type": b_type,
                            "component_type": c_type,
                            "title": b_title,
                            "page_title": page_title,
                            "order": block_order_counter,
                            "content": b_content,
                            "metadata": {"concept_group": page_title}
                        }
                    )

                    if not b_created:
                        block.block_type = b_type
                        block.component_type = c_type
                        block.title = b_title
                        block.page_title = page_title
                        block.order = block_order_counter
                        block.content = b_content
                        block.metadata = {"concept_group": page_title}
                        block.save()

                    # Attach LessonAsset if this is a media block with url/author/licensing
                    if b_type in ["suggested_image", "suggested_video"] and isinstance(b_content, dict) and b_content.get("url"):
                        media_url = b_content.get("url")
                        author = b_content.get("author", "Educational Resource")
                        licensing = b_content.get("licensing", "Standard")
                        commons_page_url = b_content.get("commons_page_url", "")
                        asset_type = "video" if b_type == "suggested_video" else "image"

                        asset, a_created = LessonAsset.objects.get_or_create(
                            lesson=lesson,
                            title=b_title,
                            defaults={
                                "asset_type": asset_type,
                                "source_type": "external",
                                "storage_type": "url",
                                "status": "attached",
                                "url": media_url,
                                "description": b_content.get("text", b_title),
                                "metadata": {
                                    "author": author,
                                    "licensing": licensing,
                                    "commons_page_url": commons_page_url,
                                    "caption": b_content.get("text", b_title)
                                }
                            }
                        )
                        if not a_created:
                            asset.url = media_url
                            asset.status = "attached"
                            asset.asset_type = asset_type
                            asset.metadata = {
                                "author": author,
                                "licensing": licensing,
                                "commons_page_url": commons_page_url,
                                "caption": b_content.get("text", b_title)
                            }
                            asset.save()

                        asset.blocks.add(block)
                        total_assets += 1

                    block_order_counter += 10
                    total_blocks += 1

            print(f"      [OK] Ingested {len(pages)} Pages for Lesson {unit_order}.")

        print("=" * 80)
        print(f"[SUCCESS] Form 4 History Topic 9 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 9")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
