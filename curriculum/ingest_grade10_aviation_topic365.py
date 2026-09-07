"""
VLearn Grade 10 Aviation — Topic 365: Aviation Communication (Subject ID: 44, Topic ID: 365)
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aviation Communication (Topic ID: 365, Order: 7)

Ingests 5 Comprehensive Learning Units & Lessons (50 Concept Cards):
  1. The ICAO Phonetic Alphabet, Numerals, and Time (Unit order: 0) [10 Cards]
  2. Standard Aviation Words and Phraseology (Unit order: 1) [10 Cards]
  3. Radio Transmission Technique and Discipline (Unit order: 2) [10 Cards]
  4. Aircraft Marshalling and Visual Ground Signals (Unit order: 3) [10 Cards]
  5. Communication Careers and Integrated Simulation (Unit order: 4) [10 Cards]

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic365.py [--replace]
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def clean_text(text: str) -> str:
    """Removes bracket citations [88, 89], internal visual prompt text, and normalizes typography."""
    if not text:
        return ""
    # Remove bracket citations e.g. [88], [88, 89], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Remove practical task, scenario, and application internal markers
    text = re.sub(r'\[(?:REAL WORLD APPLICATION|PRACTICAL TASK|SAFETY SCENARIO|SCENARIO)[^\]]*\]', '', text, flags=re.IGNORECASE)
    # Normalize unicode bullets into markdown list dashes
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def build_topic365_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 365."""
    return [
        # =====================================================================
        # LESSON 1: The ICAO Phonetic Alphabet, Numerals, and Time
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "The ICAO Phonetic Alphabet, Numerals, and Time",
            "unit_description": "Foundations of international aviation communication: mastering the 26 ICAO phonetic code words, standard pronunciation of numerals, 24-hour UTC/Zulu time notation, and aircraft radio call signs.",
            "lesson_title": "The ICAO Phonetic Alphabet, Numerals, and Time",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Historical ICAO Radiotelephony Spelling Alphabet Chart",
                        "content": {
                            "title": "Historical ICAO Radiotelephony Spelling Alphabet Chart",
                            "caption": "An official ICAO radiotelephony spelling alphabet reference sheet demonstrating the standardized pronunciation of international aviation letters and numerals to ensure clarity through radio static.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Radiotelephony_Spelling_Alphabet_%281955%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Phonetic Alphabet, Numerals, and Time",
                        "content": {
                            "title": "Learning Focus: Phonetic Alphabet, Numerals, and Time",
                            "goals": [
                                "Pronounce all 26 letters of the English alphabet using official ICAO phonetic code words from Alpha to Zulu.",
                                "Articulate aviation numerals individually according to standardized international phonetic pronunciations from Nadazero to Novenine.",
                                "Convert local times into 24-hour Coordinated Universal Time (UTC / Zulu Time) for operational flight planning.",
                                "Translate commercial and general aviation aircraft call signs into standardized radio transmissions."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Foundational Aviation Communication Terminology",
                        "content": {
                            "title": "Core Radiotelephony Vocabulary",
                            "definitions": [
                                {
                                    "term": "ICAO",
                                    "definition": "The International Civil Aviation Organization, a specialized agency of the United Nations that coordinates global civil aviation safety, regulations, and operational standards.",
                                    "example": "ICAO Annex 10 governs international aeronautical telecommunications."
                                },
                                {
                                    "term": "ICAO Phonetic Alphabet",
                                    "definition": "A standardized spelling alphabet that assigns 26 acoustically distinct code words to the letters of the English alphabet to prevent ambiguity over radio channels.",
                                    "example": "Spelling runway identification 'C' as 'Charlie' to distinguish it from 'B' (Bravo) or 'D' (Delta)."
                                },
                                {
                                    "term": "ICAO Standard Numerals",
                                    "definition": "Standardized spoken pronunciations for numbers 0 through 9 designed to remain intelligible across varied accents and through severe static interference.",
                                    "example": "Pronouncing '9' as 'Novenine' to avoid confusion with the German word 'nein'."
                                },
                                {
                                    "term": "Coordinated Universal Time (UTC)",
                                    "definition": "The primary global time standard regulating international aviation schedules, flight plans, and meteorological reports, commonly known as Zulu Time (Z).",
                                    "example": "A flight departure filed for 1200Z regardless of local daylight saving time or time zones."
                                },
                                {
                                    "term": "Call Sign",
                                    "definition": "A standardized alphanumeric identifier assigned to an aircraft, ground vehicle, or air traffic control facility to establish clear station identity during radiotelephony.",
                                    "example": "Commercial flight KQ540 spoken as 'Kenya Airways five four zero', or light trainer 5Y-KCA spoken as 'Five Yankee Kilo Charlie Alpha'."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): The 26 ICAO Code Words
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 26 ICAO Phonetic Code Words",
                        "content": {
                            "title": "Overcoming Static and Accents in Flight",
                            "text": "In aviation, misunderstanding a single spoken letter over a noisy VHF frequency can cause catastrophic navigation errors or runway incursions. For example, letters like 'B', 'C', 'D', 'E', 'P', and 'T' share similar rhyming vowel sounds that easily blur through cockpit engine noise and atmospheric crackle.\n\nTo eradicate ambiguity, the International Civil Aviation Organization (ICAO) scientifically developed the 26-word spelling alphabet. Each word was rigorously tested across hundreds of native languages and accents to ensure distinct acoustic contours and syllable stress patterns:\n\n- **A to F**: Alpha, Bravo, Charlie, Delta, Echo, Foxtrot\n- **G to L**: Golf, Hotel, India, Juliet, Kilo, Lima\n- **M to R**: Mike, November, Oscar, Papa, Quebec, Romeo\n- **S to X**: Sierra, Tango, Uniform, Victor, Whiskey, X-ray\n- **Y to Z**: Yankee, Zulu\n\nEvery pilot and air traffic controller in the world undergoes extensive training to recite these words automatically. Slang, informal substitutions (such as 'B as in Boy'), or localized words are strictly illegal under civil aviation regulations."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The ICAO Aviation Language Guide: Alphabet, Numerals & Call Signs",
                        "content": {
                            "title": "Standardized Radiotelephony Guide",
                            "caption": "A comprehensive visual guide showing the 26 ICAO phonetic code words, standard digit pronunciations, 24-hour UTC timekeeping, and aircraft call sign structure."
                        }
                    }
                ],
                # Card 5 (Page 5): Standardized Aviation Numbers
                [
                    {
                        "type": "concept_explanation",
                        "title": "Standardized Aviation Numerals",
                        "content": {
                            "title": "Single-Digit Enunciation and Phonetic Numerals",
                            "text": "Numbers represent headings, altitudes, airspeeds, and frequencies in aviation. Combining digits into everyday numbers (such as saying 'thirty-three' or 'twenty-five hundred') is strictly forbidden because grouped numbers sound garbled through radio distortion.\n\nPilots and controllers must pronounce each numeral individually with deliberate, rhythmic enunciation using official ICAO pronunciations:\n\n- **0 (Nadazero)**: Spoken as 'ZEE-RO'\n- **1 (Unaone)**: Spoken as 'WUN'\n- **2 (Bissotwo)**: Spoken as 'TOO'\n- **3 (Terrathree)**: Spoken as 'TREE' (rolling the 'R' without the 'TH' sound to prevent lisping across microphones)\n- **4 (Kartefour)**: Spoken as 'FOW-ER' (two clear syllables)\n- **5 (Pantafive)**: Spoken as 'FIFE' (crisp concluding 'F' to prevent confusion with 'nine')\n- **6 (Soxisix)**: Spoken as 'SIX'\n- **7 (Setteseven)**: Spoken as 'SEV-EN'\n- **8 (Oktoeight)**: Spoken as 'AIT'\n- **9 (Novenine)**: Spoken as 'NIN-ER' or 'Novenine' (two distinct syllables so it is never confused with the German word 'nein' meaning no)\n- **Decimal Point**: Always articulated as 'DECIMAL' (e.g., VHF frequency 118.1 is spoken as 'One one eight decimal one')."
                        }
                    }
                ],
                # Card 6 (Page 6): Number Pronunciation & Confusion Avoidance
                [
                    {
                        "type": "comparison_table",
                        "title": "Aviation Number Pronunciation & Acoustic Safeguards",
                        "content": {
                            "title": "Acoustic Separation of Aviation Digits",
                            "headers": ["Numeral", "Everyday Spoken Form", "ICAO Standard Phonetic", "Acoustic Confusion Prevented"],
                            "rows": [
                                ["3", "Three", "TREE", "Prevents 'three' sounding like 'free' or 'see' through low-bandwidth headset audio"],
                                ["4", "Four", "FOW-ER", "Two-syllable delivery prevents clipping when opening radio squelch"],
                                ["5", "Five", "FIFE", "Hard 'F' ending prevents confusion with 'nine' or 'fire'"],
                                ["9", "Nine", "NIN-ER / Novenine", "Prevents confusion with 'no' or German 'nein' in international airspace"],
                                ["0945 (Time)", "Quarter to ten", "Zero nine four five", "Eliminates morning/evening ambiguity and time zone miscalculations"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Call Signs at Wilson Airport)
                [
                    {
                        "type": "real_world_example",
                        "title": "Aircraft Call Signs at Wilson Airport",
                        "content": {
                            "title": "Decoding Registrations and Airline Flight Numbers",
                            "text": "Wilson Airport in Nairobi is one of the busiest general aviation airports in Africa, handling dozens of flight school trainers, safari charters, and medical evacuation flights simultaneously:\n\n- **General Aviation Call Signs**: In Kenya, civil aircraft carry the national prefix '5Y' followed by three registration letters. A training Cessna with registration **5Y-KCA** is spoken on the radio as: *'Five Yankee Kilo Charlie Alpha'*. Once initial contact is established and no confusion exists, the controller may abbreviate this to the prefix and last two letters: *'Five Charlie Alpha'*.\n- **Commercial Airline Call Signs**: Commercial passenger flights use the airline's registered telephony call sign combined with the flight number. Kenya Airways flights use the call sign 'KENYA'. For example, flight KQ540 from Nairobi to Kisumu is transmitted as: *'Kenya five four zero'*.\n- **Ground Stations**: Ground facilities identify themselves by location name and operational function: *'Wilson Ground'*, *'Wilson Tower'*, or *'Nairobi Approach'*."
                        }
                    }
                ],
                # Card 8 (Page 8): 24-Hour Coordinated Universal Time (UTC)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Global Synchronization with Coordinated Universal Time",
                        "content": {
                            "title": "Why Aviation Runs on Zulu Time",
                            "text": "A commercial flight crossing from Nairobi to London crosses multiple time zones and daylight-saving regimes. If flight plans, air traffic handovers, and weather reports used local clocks, calculating clearances and estimated times of arrival (ETA) would create catastrophic timing errors.\n\nTo achieve absolute global coordination, aviation operates exclusively on **Coordinated Universal Time (UTC)**, historically known as Greenwich Mean Time (GMT) and universally designated by the military and aviation code **Zulu (Z)**:\n\n- **24-Hour Clock**: Aviation time never uses 'AM' or 'PM'. Hours run continuously from 00 to 23, and minutes from 00 to 59.\n- **Digit-by-Digit Speech**: Times are spoken as four distinct digits. For example, 08:15 UTC is spoken as *'Zero eight one five'*, and 16:40 UTC is spoken as *'One six four zero'*.\n- **Local Conversion in Kenya**: Kenya is located in the East Africa Time (EAT) zone, which is permanently UTC+3 hours. To convert Kenyan local time to UTC, pilots subtract 3 hours: 15:00 EAT becomes 12:00 UTC (1200Z)."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airspace and ATC Radiotelephony Communications",
                        "content": {
                            "title": "Airspace: ATC Communications Ground School",
                            "description": "Watch how pilots adjust headsets, pronounce the ICAO phonetic alphabet, articulate numerals, and manage Coordinated Universal Time (Zulu Time) in active airspace.",
                            "url": "https://www.youtube.com/watch?v=-MpdaGEaHJE"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Standard Aviation Numeral Pronunciation",
                        "content": {
                            "question": "How should a pilot pronounce the number 9 over an aviation radio frequency according to official standard procedures?",
                            "options": [
                                "Nine-er",
                                "Novenine",
                                "Nein",
                                "Non-a"
                            ],
                            "answer": "B",
                            "explanation": "Under official ICAO standard radiotelephony numerals, the digit 9 is spelled and pronounced as Novenine (or phonetically NIN-ER) to prevent international pilots from confusing it with the German word 'nein', which means 'no'."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: General Aviation Call Sign Enunciation",
                        "content": {
                            "question": "A training aircraft registered in Kenya with the tail letters 5Y-KCA contacts Wilson Tower. What is the correct radio transmission of its call sign?",
                            "options": [
                                "Fifty-Five Yankee K-C-A",
                                "Five Yankee Kilo Charlie Alpha",
                                "Five Yellow King Cat Apple",
                                "Kenyan Trainer Five Yard Charlie"
                            ],
                            "answer": "B",
                            "explanation": "Aviation call signs must be spoken digit-by-digit and letter-by-letter using the official ICAO phonetic alphabet. '5' is spoken as 'Five', 'Y' as 'Yankee', 'K' as 'Kilo', 'C' as 'Charlie', and 'A' as 'Alpha'."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Standard Aviation Words and Phraseology
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Standard Aviation Words and Phraseology",
            "unit_description": "Mastering the legal vocabulary of radiotelephony: the critical distinction between Roger and Wilco, standard acknowledgments, phraseology discipline, and mandatory clearance readbacks.",
            "lesson_title": "Standard Aviation Words and Phraseology",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aviation Nav/Comm Transceiver Control Unit",
                        "content": {
                            "title": "Aviation Nav/Comm Transceiver Control Unit",
                            "caption": "A standard cockpit navigation and VHF communication radio console showing active frequency displays used by pilots to transmit standard phraseology and receive ATC clearances.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Navcom_radio_Bendix_King.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Standard Radiotelephony Words and Phraseology",
                        "content": {
                            "title": "Learning Focus: Standard Radiotelephony Words and Phraseology",
                            "goals": [
                                "Define the core aviation radiotelephony words including Roger, Wilco, Affirm, Negative, Standby, Say Again, and Correction.",
                                "Analyze the safety distinction between 'Roger' (received and understood) and 'Wilco' (will comply with action).",
                                "Explain why contradictory phrases like 'Over and Out' are strictly prohibited in aviation.",
                                "Execute accurate readbacks for mandatory air traffic control clearances, altitude limits, and runway instructions."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Radiotelephony Phraseology",
                        "content": {
                            "title": "Essential Aviation Words and Meanings",
                            "definitions": [
                                {
                                    "term": "Standard Phraseology",
                                    "definition": "A standardized, regulated vocabulary of predefined terms and sentence structures designed to minimize transmission time and eliminate linguistic ambiguity.",
                                    "example": "Using standard words to ensure a Kenyan controller and a Japanese pilot have zero misinterpretation."
                                },
                                {
                                    "term": "Roger",
                                    "definition": "An acknowledgment meaning 'I have received all of your last transmission and understood it.' It never confirms physical action or compliance.",
                                    "example": "Acknowledging an automated weather broadcast with 'Roger'."
                                },
                                {
                                    "term": "Wilco",
                                    "definition": "An abbreviation of 'Will Comply,' meaning 'I have received your transmission, understand it, and will execute the instruction.'",
                                    "example": "Confirming an instruction to expedite taxiing with 'Wilco'."
                                },
                                {
                                    "term": "Affirm & Negative",
                                    "definition": "The standard aviation words for 'Yes' and 'No,' engineered to avoid sounding like 'Sess', 'Press', or 'Go' through cockpit noise.",
                                    "example": "Responding 'Affirm' to a controller's inquiry regarding runway visual contact."
                                },
                                {
                                    "term": "Read Back",
                                    "definition": "A mandatory safety procedure where a pilot repeats back the exact details of a safety-critical clearance to allow the controller to verify correct comprehension.",
                                    "example": "Repeating back an assigned altitude: 'Climb and maintain flight level one five zero, Kenya five four zero'."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): The Core Aviation Vocabulary
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Ten Core Aviation Transmission Words",
                        "content": {
                            "title": "Legal Precision in Every Transmission",
                            "text": "Everyday conversation thrives on synonyms and casual expressions like 'yeah', 'sure', 'alright', or 'gotcha'. On an aviation radio channel shared by dozens of high-speed aircraft, casual variety creates confusion and fatal hesitation.\n\nAviation enforces a concise set of standard words, each bearing an absolute regulatory meaning:\n\n- **Acknowledge**: 'Let me know that you have received and understood this message.'\n- **Affirm**: 'Yes' (never use 'yeah' or 'yep').\n- **Negative**: 'No', 'Permission not granted', or 'That is incorrect'.\n- **Say Again**: 'Repeat all, or the specified part, of your last transmission.' (Never say 'What?' or 'Repeat').\n- **Correction**: 'An error has been made in this transmission; the correct version is...'\n- **Standby**: 'Wait and I will call you.' It indicates the station is busy and orders the caller to wait without transmitting.\n- **Cleared**: 'Authorized to proceed under the conditions specified.' (Only controllers may issue clearances).\n- **Monitor**: 'Listen on frequency (specified).' No transmission is needed until called.\n- **Contact**: 'Establish radio communication with (station/frequency).'\n- **Unable**: 'I cannot comply with your request, instruction, or clearance.'"
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Phraseology Decision Flow: Roger vs. Wilco Protocol",
                        "content": {
                            "title": "Phraseology Protocol & Decision Tree",
                            "caption": "An operational flowchart illustrating the crucial distinction between Roger and Wilco, mandatory readbacks, and forbidden radio phrases."
                        }
                    }
                ],
                # Card 5 (Page 5): The Critical Difference: Roger vs. Wilco
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Crucial Safety Rule: Roger versus Wilco",
                        "content": {
                            "title": "Hearing an Instruction versus Executing It",
                            "text": "The distinction between **Roger** and **Wilco** is one of the most vital safety doctrines in all of aviation:\n\n- **Roger = Understood**: Roger derives from the historical phonetic letter 'R' for 'Received'. It means: *'I heard your words and comprehend their meaning.'* However, Roger carries **zero commitment to action**. If a controller instructs: *'Five Yankee Kilo Charlie Alpha, turn immediately right heading two seven zero to avoid traffic'*, and the pilot says *'Roger'*, the controller has no verification that the pilot is turning or that the pilot even can turn.\n- **Wilco = Will Comply**: Wilco combines *'Roger'* and *'Action'*. It means: *'I have received your message, understand it, and I am actively executing the maneuver.'*\n- **Mandatory Readback Trumps Both**: For critical instructions—such as altitude changes, runway crossings, and speed restrictions—neither Roger nor Wilco is legally sufficient. The pilot must read back the specific numbers and instructions so the controller can catch any auditory error."
                        }
                    }
                ],
                # Card 6 (Page 6): Everyday Slang versus Aviation Phraseology
                [
                    {
                        "type": "comparison_table",
                        "title": "Everyday Slang versus Regulated Aviation Phraseology",
                        "content": {
                            "title": "Translating Conversational English into Aviation Radiotelephony",
                            "headers": ["Casual Slang (Prohibited)", "Standard Aviation Phrase", "Operational Safety Rationale"],
                            "rows": [
                                ["'Yeah' / 'Yup' / 'Sure'", "Affirm", "Prevents acoustic clipping and vowel confusion in high cockpit noise"],
                                ["'Nope' / 'Uh-uh'", "Negative", "Clear multi-syllable delivery with hard consonants"],
                                ["'What did you say?'", "Say again", "Standardized request preventing casual conversational clutter"],
                                ["'My bad' / 'Oops'", "Correction", "Immediately alerts the listener that incorrect data was just broadcast"],
                                ["'Hold on a sec'", "Standby", "Instructs the other station to remain silent and await contact"],
                                ["'Over and Out'", "NEVER USE TOGETHER", "'Over' invites a reply; 'Out' ends the call. They are exact opposites!"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Clearance Delivery at JKIA)
                [
                    {
                        "type": "real_world_example",
                        "title": "Clearance Delivery at Jomo Kenyatta International Airport",
                        "content": {
                            "title": "Standard Phraseology in International Gate Departures",
                            "text": "At Jomo Kenyatta International Airport (JKIA) in Nairobi, airliners depart around the clock for destinations across Europe, the Middle East, and Africa. Before an aircraft pushes back from the gate, the flight crew contacts Clearance Delivery on VHF:\n\n- **Initial Call**: *'Nairobi Delivery, Kenya five four zero, stand two, Boeing seven eight seven, information Bravo, request IFR clearance to Mombasa.'*\n- **ATC Clearance**: *'Kenya five four zero, cleared to Mombasa via flight planned route, climb to flight level one eight zero, departure runway zero six, squawk six two four one.'*\n- **Mandatory Readback**: The flight crew reads back every element in exact sequence: *'Cleared to Mombasa via flight planned route, flight level one eight zero, runway zero six, squawk six two four one, Kenya five four zero.'*\n\nIf the pilot mishears 'six two four one' as 'six two one four', the controller instantly catches the transposition, stating: *'Kenya five four zero, negative, squawk six two four one.'* This prevents transponder confusion in the radar network."
                        }
                    }
                ],
                # Card 8 (Page 8): Why 'Over and Out' is Forbidden
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Golden Rule: Why 'Over and Out' Does Not Exist",
                        "content": {
                            "title": "Debunking Hollywood Radiotelephony Myths",
                            "text": "In popular action movies, pilots and soldiers frequently end conversations by saying *'Over and Out'*. In real-world aviation, saying these two words together is considered a serious procedural error:\n\n- **Over**: Means *'I have finished my transmission and I expect a response from you.'* It passes the microphone turn to the other party.\n- **Out**: Means *'I have finished speaking, our exchange is completed, and no response is expected or desired.'* It closes the circuit.\n\nSaying *'Over and Out'* is a direct contradiction: it tells the listener *'Please answer me, but do not talk to me.'* Furthermore, on modern simplex VHF frequencies, neither word is typically required during rapid back-and-forth air traffic exchanges because concluding with your aircraft call sign naturally indicates that your transmission has ended."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Standard Phrases for Aviation Radio Communications",
                        "content": {
                            "title": "Standard Radiotelephony Phrases and Clearance Readbacks",
                            "description": "Learn the vital standard phraseology words used by pilots and air traffic controllers, demonstrating crisp pacing, clearance readbacks, and how to eliminate hesitation.",
                            "url": "https://www.youtube.com/watch?v=8uRuqyJfJP4"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Safety Distinction Between Roger and Wilco",
                        "content": {
                            "question": "Why is it highly dangerous for a pilot to respond with 'Roger' to a critical air traffic control instruction such as 'Descend immediately to 3,000 feet'?",
                            "options": [
                                "Because 'Roger' means the pilot does not understand English",
                                "Because 'Roger' only confirms the message was heard, but does not confirm that the pilot will comply and descend, creating a severe collision risk",
                                "Because 'Roger' is a classified word only permitted in military combat operations",
                                "Because saying 'Roger' creates electrical static on the VHF radio transceiver"
                            ],
                            "answer": "B",
                            "explanation": "In aviation safety, there is a fundamental distinction between hearing and acting. 'Roger' only confirms receipt and understanding of the words. To confirm active physical maneuvering, the pilot must respond with 'Wilco' or provide a complete readback of the assigned altitude."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Contradictory Radio Terms",
                        "content": {
                            "question": "Why are the words 'Over' and 'Out' never spoken together in a single aviation radio transmission?",
                            "options": [
                                "Because they represent contradictory instructions: 'Over' expects a response, while 'Out' terminates the conversation with no response expected",
                                "Because saying them together causes the aircraft's radio transmitter circuitry to overheat",
                                "Because 'Over' is only used by ground controllers and 'Out' is only used by airborne pilots",
                                "Because 'Over and Out' is an exclusive commercial trademark of airline manufacturers"
                            ],
                            "answer": "A",
                            "explanation": "'Over' signifies that the speaker is waiting for a reply, whereas 'Out' signifies that the transmission is completely finished and no reply is expected. Using both simultaneously creates an immediate procedural contradiction."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Radio Transmission Technique and Discipline
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Radio Transmission Technique and Discipline",
            "unit_description": "Aviation VHF radio operation, microphone placement, Push-To-Talk (PTT) cycle, frequency discipline, avoiding stepped-on transmissions, and the 4 Ws communication framework.",
            "lesson_title": "Radio Transmission Technique and Discipline",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Cockpit VHF Aviation Transceiver Unit",
                        "content": {
                            "title": "Cockpit VHF Aviation Transceiver Unit",
                            "caption": "An aircraft very high frequency (VHF) transceiver operating within the 118.000 to 136.975 MHz band, equipped with frequency select knobs and transmit status indicators.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/KOYO_KTR-1770.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Radio Transmission Technique and Discipline",
                        "content": {
                            "title": "Learning Focus: Radio Transmission Technique and Discipline",
                            "goals": [
                                "Explain the operational characteristics of VHF line-of-sight aviation communications (118.000 to 136.975 MHz).",
                                "Demonstrate correct headset microphone boom positioning and noise-canceling techniques.",
                                "Execute the 5-step Push-To-Talk (PTT) transmission cycle.",
                                "Structure aviation transmissions using the 4 Ws framework (Who you are calling, Who you are, Where you are, What you want)."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Radio Technique & Operational Terminology",
                        "content": {
                            "title": "VHF Radio and Physical Discipline",
                            "definitions": [
                                {
                                    "term": "VHF Aviation Band",
                                    "definition": "The line-of-sight electromagnetic spectrum between 118.000 MHz and 136.975 MHz allocated exclusively for civil aviation communications.",
                                    "example": "Tuning 118.100 MHz to communicate with the Wilson Airport control tower."
                                },
                                {
                                    "term": "Push-To-Talk (PTT)",
                                    "definition": "A momentary spring-loaded switch located on the pilot's control yoke or headset cord that must be held down to transmit and released to receive.",
                                    "example": "Depressing the yoke PTT button while speaking, then releasing it immediately to hear ATC's reply."
                                },
                                {
                                    "term": "Radio Discipline",
                                    "definition": "The strict habit of keeping all radio communications brief, professional, pre-planned, and clear, eliminating chatter and hesitation.",
                                    "example": "Thinking through your exact words before pressing the transmit switch."
                                },
                                {
                                    "term": "Stepping (Clapping)",
                                    "definition": "The harmful interference that occurs when two stations transmit on the same simplex VHF frequency at the same time, producing an unreadable squeal.",
                                    "example": "Two pilots pressing PTT simultaneously, blocking an emergency message from reaching the tower."
                                },
                                {
                                    "term": "The 4 Ws Framework",
                                    "definition": "A standardized structural sequence for initial radio calls: (1) Who you are calling, (2) Who you are, (3) Where you are, and (4) What you want.",
                                    "example": "'Wilson Ground (1), Five Yankee Kilo Charlie Alpha (2), at the hangar apron (3), request taxi to runway one four (4).'"
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): VHF Physics & Simplex Channels
                [
                    {
                        "type": "concept_explanation",
                        "title": "VHF Radio Physics and Shared Channels",
                        "content": {
                            "title": "Why Aviation Radio Differs from Cell Phones",
                            "text": "Unlike a cellular telephone where both users can talk and listen at the same time (full duplex), civil aviation VHF communications operate in **simplex mode** (half-duplex). On a single assigned frequency (such as 118.1 MHz), only one station can transmit at any given instant.\n\nKey physical principles govern these channels:\n\n- **Shared Airspace Party Line**: Every aircraft, ground vehicle, and controller operating in a 100-nautical-mile radius shares the exact same channel. If one station transmits, everyone hears it.\n- **Destructive Heterodyne Squeal**: If two transmitters key their microphones simultaneously, their carrier waves clash, generating a piercing acoustic squeal known as **stepping** or **clapping**. Neither message can be decoded by the tower, creating an immediate danger during congested airport operations.\n- **Line-of-Sight Limitations**: VHF radio waves travel in straight lines and cannot bend around the curvature of the Earth or penetrate high mountains. If an aircraft flies low behind the Ngong Hills near Nairobi, VHF reception may drop out until line-of-sight is reestablished."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "VHF Radio Setup & Push-To-Talk (PTT) Protocol",
                        "content": {
                            "title": "VHF Radio Architecture & Operating Cycle",
                            "caption": "A detailed layout displaying the cockpit radio panel, headset boom microphone positioning (2 to 3 cm from lips), and the 5-step PTT cycle."
                        }
                    }
                ],
                # Card 5 (Page 5): Physical Handling & Microphone Placement
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physical Handling: Microphone Placement and Speech Pacing",
                        "content": {
                            "title": "Overcoming Engine Roar with Proper Technique",
                            "text": "Cockpits are noisy environments filled with piston engine rumble, propeller slipstream, and avionics cooling fans. Modern aviation headsets incorporate noise-canceling electret microphones designed to reject background sound, but they require proper physical placement:\n\n- **The 2 to 3 Centimeter Rule**: The foam microphone windscreen must be positioned approximately 2 to 3 centimeters (about one finger width) directly in front of the center of your lips. If it touches your lips, breathing and plosive consonants ('P' and 'B') produce loud popping noises. If it is placed further than 3 centimeters away, noise-canceling circuits mistake your voice for background noise and attenuate your speech.\n- **Conversational Volume**: Maintain an even, calm conversational pitch. Do not shout into the microphone, as shouting overdrives the amplifier and distorts the transmission.\n- **Measured Cadence**: Speak at an even tempo of approximately 100 words per minute. Air traffic controllers and other pilots must write down coordinates, headings, and transponder codes as you speak."
                        }
                    }
                ],
                # Card 6 (Page 6): The 5-Step PTT Transmission Cycle
                [
                    {
                        "type": "comparison_table",
                        "title": "The 5-Step Push-To-Talk (PTT) Transmission Cycle",
                        "content": {
                            "title": "Procedural Execution of a Radio Transmission",
                            "headers": ["Step Number", "Phase Action", "Procedural Requirement", "Operational Failure Avoided"],
                            "rows": [
                                ["Step 1", "Listen Before Transmitting", "Monitor frequency for at least 3 seconds", "Prevents stepping on another pilot's ongoing clearance or distress call"],
                                ["Step 2", "Pre-Formulate Message", "Structure the 4 Ws mentally before keying mic", "Eliminates hesitation words like 'uh' and 'um' that congest the channel"],
                                ["Step 3", "Depress PTT Switch", "Press and hold PTT; pause for 0.5 seconds", "Allows radio transmitter relays to energize so the first syllable is not clipped"],
                                ["Step 4", "Speak Clearly", "Deliver concise, standardized phraseology at 100 wpm", "Ensures ground controller transcribes instructions on first pass"],
                                ["Step 5", "Release PTT Switch", "Release immediately after the final syllable", "Opens the receiver so the incoming readback or clearance is heard"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (The 4 Ws at Wilson Circuit)
                [
                    {
                        "type": "real_world_example",
                        "title": "The 4 Ws in the Wilson Airport Traffic Pattern",
                        "content": {
                            "title": "Conducting Structured Calls in Busy Circuit Airspace",
                            "text": "At Wilson Airport, training circuits often operate with eight or more Cessna and Cherokee aircraft flying traffic patterns simultaneously. In this rapid environment, there is no time for conversational storytelling. Every initial transmission must follow the **4 Ws**:\n\n1. **Who are you calling?** *'Wilson Tower'* (identifies the receiving station).\n2. **Who are you?** *'Five Yankee Kilo Charlie Alpha'* (identifies your station call sign).\n3. **Where are you?** *'Downwind runway one four'* (provides exact 3D spatial position).\n4. **What do you want?** *'Request touch-and-go'* (states operational intent).\n\nBecause the call is formatted cleanly into four structured parts, the tower controller can process the request in three seconds: *'Five Yankee Kilo Charlie Alpha, Wilson Tower, number two following a Caravan on base, runway one four, cleared touch-and-go.'*"
                        }
                    }
                ],
                # Card 8 (Page 8): Human Factors Under Stress
                [
                    {
                        "type": "concept_explanation",
                        "title": "Human Factors and Radio Discipline Under Pressure",
                        "content": {
                            "title": "Staying Calm When Systems Fail",
                            "text": "In-flight emergencies—such as an engine failure, sudden cabin smoke, or deteriorating weather—trigger severe adrenaline rushes that naturally cause humans to speak faster, pitch their voices higher, and scramble their sentences.\n\nAviation human factors training teaches pilots to maintain radio discipline through the **Aviation Priorities Rule**:\n\n1. **AVIATE**: Fly the airplane first. Maintain airspeed, altitude, and wings level.\n2. **NAVIGATE**: Steer toward a safe diversion runway or forced landing field.\n3. **COMMUNICATE**: Only once the aircraft is under positive control should the pilot key the radio.\n\nWhen declaring an emergency, pilots use standardized distress calls:\n- **MAYDAY** (repeated three times): Imminent, grave danger requiring immediate assistance.\n- **PAN-PAN** (repeated three times): Urgent safety condition that does not require immediate crash rescue but demands priority.\n\nBoth signals give the pilot total right-of-way on the radio channel, and all other stations must immediately cease transmitting."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Human Factors in Aviation Safety and Communications",
                        "content": {
                            "title": "Human Factors, Situational Awareness, and Communication Traps",
                            "description": "Examine how stress, workload, fatigue, and poor communication discipline contribute to aeronautical errors, and see how standardized procedures build a robust safety net.",
                            "url": "https://www.youtube.com/watch?v=FViSA91DP-8"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Initial Action Before Transmitting",
                        "content": {
                            "question": "What is the very first action a pilot must take before depressing the Push-To-Talk (PTT) switch to transmit a message?",
                            "options": [
                                "Shut down the aircraft engines to reduce background noise",
                                "Shout into the microphone to verify audio volume",
                                "Listen to the frequency for several seconds to ensure another station is not already transmitting",
                                "State their registration and home base three times aloud"
                            ],
                            "answer": "C",
                            "explanation": "Because aviation VHF channels operate in simplex mode, keying the transmitter while another station is speaking creates destructive heterodyne interference ('stepping'), blocking both transmissions. Listening first ensures the frequency is clear."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: The 4 Ws Structure",
                        "content": {
                            "question": "According to the 4 Ws framework, how should a pilot format an initial inbound radio call requesting landing clearance?",
                            "options": [
                                "'I am near the runway, please let me land my plane, I am running low on fuel.'",
                                "'Wilson Tower, Five Yankee Kilo Charlie Alpha, ten miles north, inbound for landing.'",
                                "'Calling you, this is a Cessna training flight, over.'",
                                "'Wilson Tower, please help me find the runway, I am lost in the clouds.'"
                            ],
                            "answer": "B",
                            "explanation": "Option B perfectly follows the 4 Ws sequence: (1) Who you are calling: 'Wilson Tower', (2) Who you are: 'Five Yankee Kilo Charlie Alpha', (3) Where you are: 'ten miles north', (4) What you want: 'inbound for landing'."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Aircraft Marshalling and Visual Ground Signals
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Aircraft Marshalling and Visual Ground Signals",
            "unit_description": "Airport apron safety, the role of aircraft marshallers, hand signals with high-visibility wands, Follow-Me guidance vehicles, and tower light gun signals for radio failure.",
            "lesson_title": "Aircraft Marshalling and Visual Ground Signals",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aircraft Marshaller Guiding an Airplane on the Apron",
                        "content": {
                            "title": "Aircraft Marshaller Guiding an Airplane on the Apron",
                            "caption": "A certified ground operations marshaller holding high-visibility day-glo wands to direct a taxiing transport aircraft safely into its designated parking stand on the apron.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/8/83/A_Polish_airman_marshals_a_U.S._Air_Force_C-130J_Super_Hercules_aircraft_March_13%2C_2014%2C_at_Lask_Air_Base%2C_Poland_140313-F-BH566-088.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Aircraft Marshalling and Visual Signals",
                        "content": {
                            "title": "Learning Focus: Aircraft Marshalling and Visual Signals",
                            "goals": [
                                "Identify the five primary aircraft marshalling hand signals: Proceed Straight, Turn Left, Turn Right, Stop, and Cut Engines.",
                                "Explain the operational role of marshalling wands and high-visibility PPE on noisy airport aprons.",
                                "Describe the deployment and guidance procedures of airport Follow-Me vehicles.",
                                "Interpret airport control tower light gun signals during complete aircraft radio failure."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Apron & Visual Ground Signaling Terminology",
                        "content": {
                            "title": "Visual Ramp Operations Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aircraft Marshaller",
                                    "definition": "A trained ground crew specialist who directs aircraft movements on the apron using standardized hand gestures and illuminated wands.",
                                    "example": "A marshaller guiding an arriving jetliner precisely to the terminal jet bridge centerline."
                                },
                                {
                                    "term": "Apron (Ramp)",
                                    "definition": "The paved area of an aerodrome designated for parking, passenger boarding, baggage loading, aircraft refueling, and maintenance.",
                                    "example": "The bustling international passenger ramp fronting Terminal 1A at JKIA."
                                },
                                {
                                    "term": "Marshalling Wands",
                                    "definition": "Bright orange or neon yellow hand-held batons (internally illuminated with LEDs for night operations) used to extend the visibility of arm signals.",
                                    "example": "Using lighted orange wands to marshal a nighttime cargo arrival."
                                },
                                {
                                    "term": "Follow-Me Vehicle",
                                    "definition": "A dedicated airport operations vehicle equipped with high-intensity flashing yellow light bars and an illuminated rear signboard used to lead taxiing aircraft.",
                                    "example": "Leading an international flight unfamiliar with Wilson Airport along complex taxiways."
                                },
                                {
                                    "term": "Control Tower Light Gun",
                                    "definition": "A focused optical signaling projector in the control tower cab capable of beaming red, green, and white light pulses to aircraft experiencing total radio failure.",
                                    "example": "Flashing a green light to clear a plane with a dead radio for landing."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Why Visual Signals Are Necessary
                [
                    {
                        "type": "concept_explanation",
                        "title": "Visual Communication on the Active Ramp",
                        "content": {
                            "title": "Overcoming Deafening Apron Decibels",
                            "text": "An active airport ramp is one of the most acoustically hostile work environments on Earth. Running turbofan engines produce sound levels exceeding 130 decibels—enough to cause instant, permanent hearing loss without ear protection. Shouting or using unshielded loudspeakers is completely useless.\n\nFurthermore, taxiing pilots face significant blind spots:\n- The pilot sits high above the ground and cannot see the ground directly beneath the aircraft's nose.\n- High-wings and swept wings extend tens of meters to the sides, making it impossible for the captain to judge clearance from baggage loaders, fueling trucks, and adjacent hangars.\n\nThe **Aircraft Marshaller** serves as the pilot's external eyes. Positioned forward of the aircraft along the nosewheel guidance line, the marshaller takes total visual command of the taxiing aircraft until it is parked, chocked, and shut down."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aircraft Marshalling Signals & Tower Light Gun Codes",
                        "content": {
                            "title": "Visual Signaling & Marshalling Reference",
                            "caption": "Diagram demonstrating the five core marshalling wand gestures (Proceed Straight, Turn Left, Turn Right, Stop, and Cut Engines) and the tower light gun color codes."
                        }
                    }
                ],
                # Card 5 (Page 5): The Marshaller's Hand Gestures
                [
                    {
                        "type": "concept_explanation",
                        "title": "Standard Marshalling Hand Gestures",
                        "content": {
                            "title": "Standardized Physical Body Language",
                            "text": "Under ICAO Annex 2 (Rules of the Air), ground marshalling gestures are legally standardized across all civilian and military aerodromes:\n\n- **Proceed Straight Ahead**: Both arms extended upward with palms facing inward, moving the forearms in a steady, rhythmic beckoning motion up and down from the shoulders.\n- **Turn Left (Pilot's Perspective)**: Marshaller points their right arm down toward the right wing, while repeatedly sweeping the left arm upward and inward toward their face in an arc.\n- **Turn Right (Pilot's Perspective)**: Marshaller points their left arm down toward the left wing, while repeatedly sweeping the right arm upward and inward toward their face in an arc.\n- **Normal Stop**: Both arms extended vertically overhead, slowly crossing the wands into an 'X' shape as the nosewheel approaches the stop bar.\n- **Emergency Stop**: Instantly crossing both wands overhead into a rigid, sharp 'X' shape while rapidly waving them to signal imminent collision danger.\n- **Cut (Shutdown) Engines**: Extend the right arm horizontally across the chest and throat, drawing the open hand or wand across the neck in a deliberate slicing motion."
                        }
                    }
                ],
                # Card 6 (Page 6): Tower Light Gun Codes Comparison
                [
                    {
                        "type": "comparison_table",
                        "title": "Control Tower Light Gun Signaling Code",
                        "content": {
                            "title": "Emergency Optical Signals for Radio Failure (NORDO)",
                            "headers": ["Light Signal Type", "Meaning for Aircraft on the Ground", "Meaning for Aircraft in Flight", "Safety Action Required"],
                            "rows": [
                                ["Steady Green", "Cleared for takeoff", "Cleared to land", "Proceed with departure or landing sequence"],
                                ["Flashing Green", "Cleared to taxi", "Return for landing (await steady green)", "Taxi to holding point or enter airport traffic pattern"],
                                ["Steady Red", "STOP IMMEDIATELY", "Give way to other aircraft and continue circling", "Apply aircraft brakes immediately; do not proceed"],
                                ["Flashing Red", "Taxi clear of runway in use", "Airport unsafe; DO NOT LAND", "Clear the runway immediately; divert to alternate aerodrome"],
                                ["Flashing White", "Return to starting point on airport", "Not applicable", "Taxi back to the apron or hangar"],
                                ["Alternating Red & Green", "Exercise extreme caution", "Exercise extreme caution", "Hazard on runway/taxiway; maintain heightened vigilance"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (JKIA Apron Marshalling)
                [
                    {
                        "type": "real_world_example",
                        "title": "Ramp Operations at Jomo Kenyatta International Airport",
                        "content": {
                            "title": "Coordinating Wide-Body Aircraft Docking at JKIA",
                            "text": "When a 250-ton Boeing 787 Dreamliner pulls off Taxiway Echo at JKIA toward Gate 4, ground operations execute a high-precision dance:\n\n- **Marshaller on Centerline**: The lead marshaller stands atop a raised platform on the gate centerline, wearing a reflective safety vest and holding bright orange LED wands.\n- **Wing-Walkers**: Because widebody wingtips span over 60 meters, two trained 'wing-walkers' accompany the aircraft wingtips, holding red flags or wands to ensure tips clear high-mast lighting towers and service vehicles.\n- **Headset Interphone Connection**: Once the pilot brings the nosewheel to rest on the stop line following the marshaller's 'X' signal, the ground handler connects a heavy-duty headset cord directly into an interphone jack on the aircraft's nose landing gear strut. The handler can now speak directly to the cockpit captain via wire, confirming chocks in place and ground power connected."
                        }
                    }
                ],
                # Card 8 (Page 8): Follow-Me Vehicles and FOD Prevention
                [
                    {
                        "type": "concept_explanation",
                        "title": "Follow-Me Guidance and FOD Hazards",
                        "content": {
                            "title": "Leading Lost Aircraft and Ramp Safety Discipline",
                            "text": "At sprawling international hubs with dozens of intersecting taxiways, unfamiliar foreign pilots or pilots landing in heavy nighttime rainstorms can easily become disoriented:\n\n- **Follow-Me Vehicle Protocol**: Ground controllers dispatch a specialized operations vehicle with high-visibility checkerboard livery and rooftop lightbars displaying *'FOLLOW ME'*. The car positions itself 50 meters ahead of the aircraft. The pilot simply tracks the car's path to the designated gate.\n- **Foreign Object Debris (FOD)**: Even a single dropped flashlight battery, stray bolt, or marshalling wand cap lying on the apron can be sucked into a turbofan engine, causing millions of shillings in catastrophic turbine blade damage. All ground crew conduct mandatory FOD sweeps before an aircraft enters the parking bay.\n- **Jet Blast Hazards**: Ground personnel must never walk behind an aircraft with beacon lights illuminated, as jet blast can overturn baggage carts and fling debris at hurricane speeds."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aircraft Marshalling Signals Explained — Hand Signals Every Pilot Must Know",
                        "content": {
                            "title": "Aircraft Marshalling Hand Signals Demonstration",
                            "description": "Watch a certified ground handling professional demonstrate standard airport marshalling wand gestures next to aircraft, highlighting straight taxiing, turns, normal stop, emergency stop, and engine shutdown.",
                            "url": "https://www.youtube.com/watch?v=XEo0q9-i4k0"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Engine Cut Hand Signal",
                        "content": {
                            "question": "What visual hand signal should an airport marshaller perform to instruct a pilot to immediately cut (shut down) their aircraft's engines?",
                            "options": [
                                "Crossing both arms overhead in a stiff 'X' shape",
                                "Waving both arms up and down alongside their thighs",
                                "Extending an arm horizontally next to the throat and drawing the hand in a deliberate slicing motion across the neck",
                                "Turning their back to the aircraft and walking away"
                            ],
                            "answer": "C",
                            "explanation": "Drawing the hand or wand across the throat in a horizontal slicing gesture is the universal international signal for engine shutdown, commanding the flight crew to immediately cut fuel mixture levers."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Light Gun Ground Signals",
                        "content": {
                            "question": "If an air traffic controller points a steady Red Light from an airport control tower light gun at a taxiing aircraft on the ground, what action must the pilot take?",
                            "options": [
                                "Accelerate and take off immediately before the runway closes",
                                "Stop the aircraft immediately",
                                "Turn left and park on the grass shoulder",
                                "Ignore the light and continue taxiing using visual cues"
                            ],
                            "answer": "B",
                            "explanation": "In standard aviation light gun signaling codes, a steady red light aimed at an aircraft on the ground means 'Stop immediately'. It serves as an emergency optical command when radio contact has failed."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Communication Careers and Integrated Simulation
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Communication Careers and Integrated Simulation",
            "unit_description": "Exploring aviation communication professions: Air Traffic Controllers, Flight Dispatchers, Aeronautical Radio Operators, Avionics Engineers, and conducting an integrated airport communication simulation.",
            "lesson_title": "Communication Careers and Integrated Simulation",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Air Traffic Controllers Operating Radar Displays and Radio Consoles",
                        "content": {
                            "title": "Air Traffic Controllers Operating Radar Displays and Radio Consoles",
                            "caption": "Air traffic control specialists managing airspace sectors using live radar monitors and VHF radiotelephony to maintain separation and sequence arrivals and departures.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Air_traffic_controller_Marines_keep_pilots_in_line_DVIDS447875.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Communication Careers and Airport Simulation",
                        "content": {
                            "title": "Learning Focus: Communication Careers and Airport Simulation",
                            "goals": [
                                "Identify key career pathways in aviation communication: Air Traffic Controller, Flight Dispatcher, Ground Handler, Aeronautical Radio Operator, and Communication Engineer.",
                                "Examine the technical duties, licensing, and safety responsibilities associated with each communication profession.",
                                "Demonstrate integrated multi-role airport communication protocols in a simulated scenario.",
                                "Analyze how teamwork and standardized communication prevent catastrophic aviation accidents."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Aviation Communication Careers Vocabulary",
                        "content": {
                            "title": "Professional Roles in Aeronautical Telecommunications",
                            "definitions": [
                                {
                                    "term": "Air Traffic Controller (ATC)",
                                    "definition": "A licensed aviation professional responsible for coordinating the safe, orderly, and expeditious flow of aircraft in the air and on the aerodrome maneuvering area.",
                                    "example": "A tower controller sequencing takeoffs and landings on Wilson Airport Runway 14."
                                },
                                {
                                    "term": "Flight Dispatcher",
                                    "definition": "A licensed aeronautical specialist who shares operational control of a flight with the captain, calculating fuel loads, monitoring en-route weather, and filing flight plans.",
                                    "example": "An airline dispatcher sending digital satellite messages to reroute a flight around severe thunderstorms."
                                },
                                {
                                    "term": "Aeronautical Radio Operator",
                                    "definition": "A telecommunications specialist who operates long-range High Frequency (HF) radio networks and digital satellite links to track aircraft over remote oceans and deserts.",
                                    "example": "Relaying oceanic position reports between aircraft and air traffic centers across the Indian Ocean."
                                },
                                {
                                    "term": "Avionics Communication Engineer",
                                    "definition": "An engineering professional responsible for installing, inspecting, and certifying aircraft radios, transponders, ground radar installations, and instrument landing systems.",
                                    "example": "Conducting bench tests and signal calibration on VHF transceivers to ensure zero harmonic distortion."
                                },
                                {
                                    "term": "Tabletop Simulation",
                                    "definition": "A structured pedagogical exercise where learners role-play operational roles (Pilot, Ground Controller, Tower, Dispatcher) to master communication handoffs.",
                                    "example": "Executing simulated taxi clearances and readbacks on a classroom model of Wilson Airport."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): The Web of Aviation Careers
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Symphony of Aviation Communication Careers",
                        "content": {
                            "title": "A Coordinated Web of Safety Specialists",
                            "text": "Safe flight operations are never the sole responsibility of the pilot sitting in the cockpit. Safe aviation depends on an interconnected chain of communication specialists working in close harmony:\n\n- **The Air Traffic Controller**: Operating in control towers and radar centers, ATCs use radar displays and VHF radios to maintain horizontal and vertical separation between aircraft, issuing clearances for engine start, pushback, taxi, takeoff, and landing.\n- **The Flight Dispatcher**: Stationed in the Airline Operations Center (AOC), the dispatcher prepares the operational flight plan, calculates payload and reserve fuel, and tracks the aircraft throughout its journey via satellite datalinks.\n- **Ground Handling & Marshalling Crew**: Operating on the tarmac, they use hand wands and pushback interphones to steer planes into gates and clear them for apron departure.\n- **Aeronautical Radio Operators**: Connecting trans-continental flights over oceans and deserts outside standard VHF line-of-sight coverage.\n- **Avionics & Telecommunications Engineers**: Ensuring that radio repeaters, antennas, navigation beacons, and satellite receivers maintain 99.999% operational reliability."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Integrated Airport Communication Network: The Safety Web",
                        "content": {
                            "title": "Communication Architecture & Data Links",
                            "caption": "A systems diagram highlighting the multi-directional communication links connecting the Control Tower, Flight Dispatch, Cockpit, Apron Crew, and Avionics Engineering."
                        }
                    }
                ],
                # Card 5 (Page 5): Detailed Roles & Responsibilities
                [
                    {
                        "type": "concept_explanation",
                        "title": "Qualifications and Operational Responsibilities",
                        "content": {
                            "title": "Training, Certification, and Key Duties",
                            "text": "Every career pathway in aviation communication requires rigorous specialized training and civil aviation authority licensing (such as certification by the Kenya Civil Aviation Authority - KCAA):\n\n- **Air Traffic Controllers**: Undergo demanding aptitude tests in spatial reasoning, multi-tasking, and English language proficiency (ICAO Level 4 minimum). They complete simulator training in aerodrome control, radar approach control, and area control.\n- **Flight Dispatchers**: Study advanced meteorology, aerodynamics, aircraft performance tables, and navigation. In commercial airlines, both the Captain and the Flight Dispatcher must sign the dispatch release before the flight can legally depart.\n- **Avionics & Communication Engineers**: Hold specialized diplomas or degrees in electrical engineering, electronics, or telecommunications, certified through Aircraft Maintenance Engineer (AME) avionics licenses covering radio, radar, and instruments."
                        }
                    }
                ],
                # Card 6 (Page 6): Aviation Communication Careers Comparison
                [
                    {
                        "type": "comparison_table",
                        "title": "Aviation Communication Careers Comparison",
                        "content": {
                            "title": "Work Environment, Tools, and Safety Missions",
                            "headers": ["Career Role", "Workplace Environment", "Primary Communication Tools", "Critical Safety Responsibility"],
                            "rows": [
                                ["Tower Controller", "Airport tower cab with 360-degree airfield glass view", "VHF Radios, ASDE-X Ground Radar, Light Gun", "Sequencing takeoffs and landings; preventing runway incursions"],
                                ["Flight Dispatcher", "Airline Operations Center (AOC)", "Flight planning computers, satellite ACARS datalinks", "Co-authoring flight plans; real-time storm avoidance rerouting"],
                                ["Apron Marshaller", "Active airport apron / ramp", "Day-glo wands, headset interphone, VHF ramp radio", "Guiding taxiing aircraft safely clear of obstacles and gates"],
                                ["Aeronautical Station Operator", "Flight information center / oceanic station", "High Frequency (HF) radio, CPDLC digital datalinks", "Long-range tracking and weather relay across remote expanses"],
                                ["Avionics Engineer", "Maintenance hangars, equipment rooms, avionics shops", "Spectrum analyzers, multimeter test benches, wire looms", "Calibrating transceivers and certifying radio airworthiness"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Wilson Simulation Step-by-Step)
                [
                    {
                        "type": "real_world_example",
                        "title": "The Wilson Airport Departure Simulation",
                        "content": {
                            "title": "Step-by-Step Simulation: Cessna 5Y-KCA Departing for Maasai Mara",
                            "text": "To experience how communication roles integrate, let us trace light training aircraft **5Y-KCA** preparing to depart Wilson Airport for the Maasai Mara:\n\n1. **Step 1 (Dispatch Briefing)**: The flight dispatcher provides weather and runway notices: *'Wilson runway one four in use, wind one six zero at eight knots, CAVOK, QNH one zero two two.'*\n2. **Step 2 (Taxi Request)**: Pilot calls Ground: *'Wilson Ground, Five Yankee Kilo Charlie Alpha, light aircraft hangar, request taxi to runway one four.'*\n3. **Step 3 (Ground Clearance)**: Controller issues clearance: *'Five Yankee Kilo Charlie Alpha, Wilson Ground, taxi to holding point runway one four via taxiway Charlie, hold short of runway zero seven.'*\n4. **Step 4 (Mandatory Readback)**: Pilot repeats: *'Taxi to holding point runway one four via taxiway Charlie, hold short of runway zero seven, Five Yankee Kilo Charlie Alpha.'*\n5. **Step 5 (Marshalling)**: Ramp marshaller signals 'Proceed Straight' then 'Normal Stop' as the plane joins Taxiway Charlie.\n6. **Step 6 (Tower Handoff)**: Ground hands off to Tower: *'Five Yankee Kilo Charlie Alpha, contact Wilson Tower on one one eight decimal one.'*"
                        }
                    }
                ],
                # Card 8 (Page 8): Crew Resource Management & Closed-Loop Communication
                [
                    {
                        "type": "concept_explanation",
                        "title": "Crew Resource Management & Closed-Loop Communication",
                        "content": {
                            "title": "Error Trapping and Safety Culture",
                            "text": "Accident investigations over fifty years have shown that the vast majority of aviation accidents are caused not by mechanical failures, but by breakdowns in human communication and teamwork.\n\nModern aviation utilizes **Crew Resource Management (CRM)** and **Closed-Loop Communication** principles:\n\n- **Closed-Loop Verification**: The sender transmits an instruction (e.g., 'Climb to 5,000 feet'). The receiver repeats back the exact numbers ('Climb to 5,000 feet'). The sender listens and confirms with 'Readback correct'. This three-step loop ensures zero ambiguity.\n- **The Sterile Cockpit Rule**: Below 10,000 feet or during taxi operations, all non-essential conversation is legally prohibited. Crew members must focus 100% of their attention on flight guidance, radio traffic, and visual obstacle scanning.\n- **Speaking Up with Assertiveness**: Junior crew members and ground staff are trained to speak up immediately if they observe an unsafe condition, regardless of the rank of the captain."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airport Operations and Airfield Communications Architecture",
                        "content": {
                            "title": "Airport Operations: Aerodrome, Airside, Landside, and Communications",
                            "description": "Explore the physical architecture of modern airports, illustrating how ground control, tower personnel, apron handlers, and flight crews synchronize operations across complex runway systems.",
                            "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Flight Dispatcher Role",
                        "content": {
                            "question": "Which aviation professional is directly responsible for co-authoring the operational flight plan with the pilot and providing real-time weather rerouting updates while the aircraft is airborne?",
                            "options": [
                                "Avionics Communication Engineer",
                                "Flight Dispatcher",
                                "Airport Marshaller",
                                "Aerodrome Firefighter"
                            ],
                            "answer": "B",
                            "explanation": "Flight dispatchers share legal operational responsibility with the captain. They calculate fuel requirements, file flight plans, track the live aircraft via datalink, and communicate rerouting options when weather deteriorates."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Mandatory Hold-Short Readbacks",
                        "content": {
                            "question": "Why are pilots strictly required to Read Back runway instructions such as 'Hold short of runway zero seven' instead of simply acknowledging with 'Roger'?",
                            "options": [
                                "To practice English pronunciation with the control tower",
                                "To allow the controller to verify that the pilot heard and will comply with the exact safety boundary, preventing runway collisions",
                                "Because saying 'Roger' causes an electrical feedback loop on VHF frequencies",
                                "To demonstrate to passengers that the pilot is awake"
                            ],
                            "answer": "B",
                            "explanation": "Readback is a critical safety barrier. If the pilot misheard the clearance as 'Cross runway 07', repeating it back allows the controller to immediately catch and rectify the error, preventing a catastrophic runway incursion."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic365(replace=True):
    """Ingests Grade 10 Aviation Topic 365 curriculum data into Nexus/VLearn database."""
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: Grade 10 Aviation — Topic 365 (ID: 365)")
    print("Aviation Communication")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Grade:      {grade.name} (ID: {grade.id}, Level: {grade.level})")
    print(f"[*] Subject:    {subject.name} (ID: {subject.id})")

    topic = Topic.objects.get(id=365, subject=subject)
    print(f"[*] Topic:      {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic365_curriculum()
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            u_order = unit_data["unit_order"]
            u_name = unit_data["unit_name"]
            u_desc = unit_data["unit_description"]
            l_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            learning_unit, created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": u_desc}
            )
            learning_unit.name = u_name
            learning_unit.description = u_desc
            learning_unit.save()

            # Find or create lesson
            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
                lesson.title = l_title
                lesson.status = "published"
                lesson.version = 1
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=l_title,
                    status="published",
                    version=1
                )

            print(f"  [+] Ingesting Lesson {u_order + 1}: {lesson.title} (Lesson ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Concept Card {page_idx}")
                for b_data in page_blocks:
                    b_type = b_data["type"]
                    b_title = b_data.get("title", first_block_title)
                    b_content = clean_dict(b_data.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_idx,
                        page_title=first_block_title,
                        title=b_title,
                        block_type=b_type,
                        component_type=b_type,
                        component_order=block_order,
                        order=block_order,
                        content=b_content,
                        metadata={}
                    )
                    block_order += 10
                    total_blocks += 1

            total_lessons += 1
            total_pages += lesson_page_count
            print(f"      [OK] Ingested {lesson_page_count} Concept Cards for Lesson {u_order + 1}.")

    print("=" * 80)
    print("[SUCCESS] Grade 10 Aviation Topic 365 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic365(replace=replace_flag)
