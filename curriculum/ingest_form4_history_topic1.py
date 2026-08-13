"""
VLearn Form 4 History — Topic 1: The World War
Authoritative High-Structure Ingestion Engine

Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)
Topic 1: The World War

Architecture:
  7 Learning Units / Lessons:
  - Lesson 1: Causes and Outbreak of World War I (14 Pages)
  - Lesson 2: The Course and Fronts of World War I (16 Pages)
  - Lesson 3: US Entry, Allied Victory, and Results of WWI (15 Pages)
  - Lesson 4: The Peace Settlement and the League of Nations (15 Pages)
  - Lesson 5: World War II: Origins, Causes, and the Path to War (13 Pages)
  - Lesson 6: The Course and Fronts of World War II (16 Pages)
  - Lesson 7: Global Results of WWII and the Rise of the United Nations (14 Pages)
  Total: 103 Pages, ~280 Granular Lesson Blocks

Features:
  - 100% pedagogical fidelity to lessons.md source material
  - Automated regex cleaning of all bracket citations ([60], [207], [1])
  - Pedagogical sequence: Context -> Hook -> Explanation -> Story -> Points -> Evidence -> Table -> Example -> Check -> KCSE Application -> Summary
  - Dedicated slots for authentic Wikimedia Commons photographic and map assets
  - Idempotent and transactional database execution

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic1.py [--replace]
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

def clean_text(raw_str):
    """Remove source citation brackets like [60], [207], [1, 2] and normalize whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# =============================================================================
# LESSON 1 DATA — Causes and Outbreak of World War I (14 Pages)
# =============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "World War I — Meaning, Background, and Causes",
    "lesson_title": "Causes and Outbreak of World War I",
    "pages": [
        {
            "page_number": 1,
            "page_title": "The Spark in the Powder Keg: The Great War",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define and distinguish the concepts of **Total War** and **Mechanized War**\n"
                            "- Explain the long-term causes of World War I (Alliances, Imperialism, Economic Rivalry, Militarism, Nationalism)\n"
                            "- Describe the major pre-war diplomatic crises in Morocco and the Balkans\n"
                            "- Detail the immediate trigger of the war at Sarajevo on 28 June 1914\n"
                            "- Apply the Point-Explanation-Evidence model to score maximum marks on KCSE exam questions"
                        )
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Archduke Franz Ferdinand and Duchess Sophie in Sarajevo",
                    "content": {
                        "text": "Archduke Franz Ferdinand and Duchess Sophie photographed in Sarajevo on 28 June 1914, shortly before the fatal assassination.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Franz_ferdinand.jpg",
                        "author": "Carl Pietzner / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Franz_ferdinand.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Historical Hook: A Local Murder that Engulfed the Globe",
                    "content": {
                        "text": (
                            "On a sunny morning in June 1914, a nineteen-year-old student stepped out of a delicatessen in Sarajevo and fired "
                            "two pistol shots at an open-top motorcar. Within thirty days, those two bullets had triggered a cataclysm that "
                            "mobilized over 65 million soldiers, destroyed four great empires, killed over 15 million human beings, and "
                            "reshaped the political map of the modern world.\n\n"
                            "How could the murder of a single Austrian nobleman ignite a war that consumed Europe, Africa, Asia, and the oceans? "
                            "The answer lies in the deep, dangerous tensions that had been quietly building across Europe for over forty years."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Nature of Modern Conflict: Total and Mechanized War",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Total War",
                    "content": {
                        "term": "Total War",
                        "definition": "A conflict in which participating nations devote all their national resources—military, industrial, financial, agricultural, and human—to the war effort, blurring the distinction between combatants on the frontline and civilians on the home front."
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Mechanized War",
                    "content": {
                        "term": "Mechanized War",
                        "definition": "A war characterized by the mass application of industrial machinery, science, and engineering to warfare—utilizing rapid-fire machine guns, heavy field artillery, armored vehicles, submarines, fighter aircraft, and toxic chemical weapons."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why the First World War Was Fundamentally Different",
                    "content": {
                        "text": (
                            "Prior to 1914, European wars were largely limited conflicts fought by professional armies on localized battlefields. "
                            "World War I broke this pattern entirely. Governments instituted mandatory military conscription, converted textile mills "
                            "into munitions factories, rationed domestic food supplies, and targeted enemy civilian shipping networks to starve opposing economies.\n\n"
                            "Because industrial factories could mass-produce lethal weaponry at unprecedented speed, defense overwhelmed offense, "
                            "transforming the war into a bloody struggle of industrial endurance."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The System of Alliances (1879–1914)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Dividing Europe into Two Armed Camps",
                    "content": {
                        "text": (
                            "In the late nineteenth century, major European powers formed secret mutual-defense treaties. If any member of an alliance "
                            "was attacked, its allies were legally bound to mobilize and declare war on the aggressor. This created a rigid 'domino system' "
                            "where a localized conflict between two countries would automatically drag in the entire continent."
                        )
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "The Opposing Power Blocs in 1914",
                    "content": {
                        "headers": ["Alliance Bloc", "Member States", "Year Established", "Strategic Objective"],
                        "rows": [
                            ["The Triple Alliance (Central Powers)", "Germany, Austria-Hungary, Italy (later joined by Ottoman Empire & Bulgaria)", "1879–1882", "Protect Central Europe from Russian expansion and French revanchism; secure German hegemony."],
                            ["The Triple Entente (Allied Powers)", "Great Britain, France, Russia (later joined by Italy, USA, Japan, Romania)", "1894–1907", "Counterbalance German industrial and military expansion; defend French and Russian borders; preserve British naval supremacy."]
                        ]
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "KCSE Examination Alert: Italy's Shift",
                    "content": {
                        "text": "Note for KCSE: Although Italy was an original member of the Triple Alliance, it declared neutrality in 1914 on the grounds that Germany was the aggressor, and later joined the Allied Triple Entente in 1915 following the secret Treaty of London."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Imperialism and Colonial Competition",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Scramble for Global Territories and Markets",
                    "content": {
                        "text": (
                            "Industrialized European powers required vast quantities of agricultural and mineral raw materials (cotton, rubber, iron, copper, oil) "
                            "and guaranteed overseas markets to consume manufactured goods.\n\n"
                            "Britain and France had established sprawling empires spanning Africa, Asia, and the Americas. Germany, having unified late in 1871, "
                            "entered the colonial race late and possessed few overseas territories (Tanganyika, Cameroon, Togoland, Namibia).\n\n"
                            "Kaiser Wilhelm II declared that Germany demanded its rightful 'place in the sun,' pursuing an aggressive imperial foreign policy "
                            "(*Weltpolitik*) that directly threatened British and French global dominance."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Key Historical Takeaway",
                    "content": {
                        "text": "Imperial competition created mutual suspicion, territorial friction, and diplomatic crises in Africa and Asia that poisoned European diplomatic relations long before 1914."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Economic Rivalry and Industrial Competition",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Challenge to British Economic Hegemony",
                    "content": {
                        "text": (
                            "Throughout the nineteenth century, Great Britain was the undisputed 'workshop of the world,' dominating international maritime "
                            "trade, banking, and industrial manufacturing.\n\n"
                            "However, following German unification in 1871, Germany experienced a phenomenal industrial surge. German steel production, "
                            "chemical synthesis, electrical engineering, and coal mining rapidly outpaced British output. German manufactured goods flooded "
                            "international markets, sparking commercial friction, tariff wars, and deep British economic resentment."
                        )
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Industrial Steel Output in 1914 (Metric Tons)",
                    "content": {
                        "headers": ["Nation", "Approx. Annual Steel Production (1914)", "Economic Impact"],
                        "rows": [
                            ["Germany", "17.3 Million Tons", "Surpassed all European rivals; enabled rapid construction of artillery, dreadnoughts, and railways."],
                            ["Great Britain", "7.6 Million Tons", "Fell behind Germany; heightened British anxiety over imperial defense and naval supremacy."],
                            ["France", "4.6 Million Tons", "Heavily reliant on imported raw materials; vulnerable along industrial northeastern border."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Militarism and the Anglo-German Naval Race",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Build-up of Armies and Dreadnoughts",
                    "content": {
                        "text": (
                            "**Militarism** is the glorification of military power, the elevation of military officers into political decision-making, "
                            "and the massive stockpiling of arms in peacetime.\n\n"
                            "Between 1870 and 1914, standing armies across continental Europe more than doubled through universal conscription. "
                            "Generals developed rigid, complex railway mobilization timetables that, once triggered, could not be stopped without military disaster.\n\n"
                            "Simultaneously, Germany embarked on a massive naval expansion program led by Admiral Alfred von Tirpitz. In response to Britain's "
                            "revolutionary battleship **HMS Dreadnought** (launched in 1906), Germany began building its own dreadnought fleet, directly threatening "
                            "the British Royal Navy's command of the seas."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "The Dreadnought Revolution",
                    "content": {
                        "text": "HMS Dreadnought was so heavily armed with ten 12-inch guns and steam turbine propulsion that it made all existing battleships obsolete overnight, resetting the naval balance and triggering an intense building race between Britain and Germany."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Extreme Nationalism and the Balkan Powder Keg",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "National Pride and Slavic Self-Determination",
                    "content": {
                        "text": (
                            "Two forms of nationalism destabilized pre-1914 Europe:\n\n"
                            "1. **Great Power Chauvinism:** In France, widespread public desire for revenge (*Revanchism*) against Germany aimed to recover "
                            "the mineral-rich provinces of **Alsace and Lorraine**, lost during the Franco-Prussian War of 1870–1871.\n\n"
                            "2. **Balkan Minority Nationalism:** The Balkan peninsula ('the powder keg of Europe') was populated by diverse Slavic ethnic groups "
                            "(Serbs, Bosnians, Croats, Slovenes) ruled by the declining Austro-Hungarian and Ottoman empires. Encouraged by Serbia and supported by "
                            "Russia through **Pan-Slavism**, these groups aggressively demanded independence or union into a 'Greater Serbia'."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Why the Balkans Were Named the 'Powder Keg'",
                    "content": {
                        "text": "The Balkans were called the powder keg of Europe because competing imperial interests (Austria-Hungary seeking expansion, Russia seeking warm-water access, and Serbia seeking a unified Slavic state) made the region volatile enough to detonate a general war."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Pre-War Diplomatic Crises (1905–1913)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Escalating Clashes on the Brink of War",
                    "content": {
                        "text": "Between 1905 and 1913, a series of diplomatic crises repeatedly brought the European powers to the verge of open warfare:"
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Four Critical Pre-War International Crises",
                    "content": {
                        "headers": ["Crisis & Year", "Nations Involved", "Core Conflict", "Historical Consequence"],
                        "rows": [
                            ["First Moroccan Crisis (1905)", "Germany vs France & Britain", "Kaiser Wilhelm II visited Tangier to challenge French control of Morocco.", "At the Algeciras Conference (1906), Britain strongly backed France; Germany was diplomatically isolated."],
                            ["Bosnian Crisis (1908)", "Austria-Hungary vs Serbia & Russia", "Austria-Hungary formally annexed Bosnia-Herzegovina, angering Serbia.", "Germany backed Austria with military threats; Russia was forced to back down in humiliation, vowing never to retreat again."],
                            ["Agadir Crisis (1911)", "Germany vs France & Britain", "Germany sent the gunboat SMS Panther to the Moroccan port of Agadir.", "Britain declared it would fight alongside France; Germany backed down in exchange for minor territory in the Congo."],
                            ["Balkan Wars (1912–1913)", "Balkan League vs Ottoman Empire; Serbia vs Bulgaria", "Balkan nations drove Turkey out of Europe, but fought over the spoils.", "Serbia doubled in size and military confidence; Austria-Hungary became determined to crush Serbia at the next opportunity."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "The Immediate Trigger: The Sarajevo Assassination",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Gavrilo Princip following his arrest in Sarajevo",
                    "content": {
                        "text": "Gavrilo Princip, the nineteen-year-old member of the Serbian nationalist secret society the Black Hand, after his arrest in Sarajevo.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Gavrilo_Princip%2C_1914.jpg",
                        "author": "Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Gavrilo_Princip,_1914.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "28 June 1914: The Fatal Shots in Sarajevo",
                    "content": {
                        "text": (
                            "**Archduke Franz Ferdinand**, heir to the Austro-Hungarian throne, visited Sarajevo, the capital of Bosnia, on 28 June 1914 "
                            "to inspect imperial military maneuvers. The date coincided with Vidovdan, a sacred day of Serbian national identity.\n\n"
                            "A secret Serbian nationalist terrorist society known as **Union or Death (The Black Hand)**, led by Colonel Dragutin Dimitrijević, "
                            "supplied weapons and trained young Bosnian Serb students to assassinate the Archduke.\n\n"
                            "After a failed morning grenade attack by Nedeljko Čabrinović, nineteen-year-old **Gavrilo Princip** encountered the Archduke's car "
                            "turning outside Schiller's Delicatessen on Franz Josef Street and fired two shots, killing both Franz Ferdinand and Duchess Sophie."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Historical Sequence: The July Crisis of 1914",
            "blocks": [
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "The 30-Day Chain Reaction to Global War",
                    "content": {
                        "steps": [
                            "28 June 1914: Archduke Franz Ferdinand and Sophie assassinated in Sarajevo by Gavrilo Princip.",
                            "5 July 1914: Kaiser Wilhelm II of Germany issues the 'Blank Cheque', promising unconditional German military support to Austria-Hungary.",
                            "23 July 1914: Austria-Hungary delivers a harsh 10-point ultimatum to Serbia with a 48-hour deadline.",
                            "25 July 1914: Serbia accepts 8 points but rejects Austrian police involvement; begins partial military mobilization.",
                            "28 July 1914: Austria-Hungary declares war on Serbia and shells Belgrade.",
                            "30 July 1914: Tsar Nicholas II orders full Russian mobilization to defend Serbia.",
                            "1 August 1914: Germany declares war on Russia; France orders general mobilization.",
                            "3 August 1914: Germany declares war on France and invades neutral Belgium (Schlieffen Plan).",
                            "4 August 1914: Great Britain declares war on Germany for violating the 1839 Treaty of London guaranteeing Belgian neutrality."
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "Primary Evidence Interpretation Activity",
            "blocks": [
                {
                    "block_type": "suggested_video",
                    "component_type": "suggested_video",
                    "title": "Historical Documentary: The July Crisis 1914 and the Outbreak of War",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=_pFCpKtwCkI",
                        "text": "CrashCourse World History exploring the July Crisis, the assassination of Archduke Franz Ferdinand, and the web of secret alliances that ignited the First World War.",
                        "author": "CrashCourse",
                        "licensing": "Standard YouTube License"
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Study This Historical Telegram (July 1914)",
                    "content": {
                        "text": (
                            "**Source:** Excerpt from an urgent confidential telegram sent by German Chancellor Theobald von Bethmann-Hollweg "
                            "to the German Ambassador in Vienna during the July Crisis of 1914:\n\n"
                            "> *'We must advise Vienna to act with utmost caution... We must avoid the appearance of wanting to provoke a world war ourselves. "
                            "> If Austria-Hungary refuses all mediation, we shall stand before a conflict in which we will be dragged in, while France and "
                            "> England will be united against us...'* \n\n"
                            "**Historical Analysis Task:**\n"
                            "1. **Observe:** What does this private telegram reveal about Germany's growing anxiety regarding the British and French alliance?\n"
                            "2. **Interpret:** Does this primary source support or challenge the claim that Germany had planned a premeditated world war?\n"
                            "3. **Evaluate Limitations:** Why can private diplomatic telegrams between ministers not reveal the broader public mood across European streets in 1914?"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 12,
            "page_title": "Interactive Task: Categorizing the Causes of WWI",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Classify the Historical Factors",
                    "content": {
                        "instruction": "Test your historical reasoning. Categorize each of the following 6 factors into its correct analytical dimension:",
                        "items": [
                            "1. The construction of HMS Dreadnought and German naval expansion -> **Militarism**",
                            "2. The signing of the Triple Entente in 1907 -> **System of Alliances**",
                            "3. French desire to recover Alsace-Lorraine -> **Nationalism (Revanchism)**",
                            "4. British-German competition for world trade markets -> **Economic Rivalry**",
                            "5. Gavrilo Princip firing two shots in Sarajevo -> **Immediate Trigger**",
                            "6. Kaiser Wilhelm II challenging French influence in Morocco -> **Imperialism**"
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 13,
            "page_title": "KCSE Examination Coaching & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Question: Explain Five Long-Term Causes of World War I (10 Marks)",
                    "content": {
                        "text": (
                            "**Model Answer Structure (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                            "1. **The System of Alliances:** Secret mutual defense pacts divided Europe into two armed camps—the Triple Alliance (Germany, Austria-Hungary, Italy) and the Triple Entente (Britain, France, Russia). A dispute between two nations automatically dragged in their allies. (2 marks)\n\n"
                            "2. **Imperialism and Colonial Rivalry:** Industrialized powers competed aggressively for overseas colonies to secure raw materials and markets. Germany's late entry into the scramble created severe friction with Britain and France over African and Asian territories. (2 marks)\n\n"
                            "3. **Militarism and Arms Race:** Nations built massive standing conscript armies and engaged in a fierce naval race, highlighted by Britain's HMS Dreadnought and Germany's High Seas Fleet, creating mutual fear and military readiness to fight. (2 marks)\n\n"
                            "4. **Economic Rivalry:** Rapid German industrial growth after 1871 challenged Britain's traditional commercial dominance, creating tariff disputes and competition for international trade routes. (2 marks)\n\n"
                            "5. **Extreme Nationalism:** Intense national pride sparked aggressive policies, including French desire to reclaim Alsace-Lorraine and Serbian Pan-Slavic ambitions to liberate Slavs from Austro-Hungarian rule in the Balkan 'powder keg'. (2 marks)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 14,
            "page_title": "Check Your Understanding & Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Module 1.1 Mastery Check",
                    "content": {
                        "question": "Which of the following was the immediate trigger for the outbreak of World War I in July 1914?",
                        "options": [
                            "A) The German naval expansion program",
                            "B) The assassination of Archduke Franz Ferdinand in Sarajevo",
                            "C) The signing of the Triple Entente",
                            "D) The annexation of Alsace-Lorraine by France"
                        ],
                        "correct_answer": "B",
                        "explanation": "The assassination of Archduke Franz Ferdinand and his wife Sophie on 28 June 1914 in Sarajevo by Gavrilo Princip was the direct immediate trigger that set off the July Crisis and World War I."
                    }
                },
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.1 Key Takeaways",
                    "content": {
                        "text": (
                            "- World War I was a **total, mechanized war** that mobilized whole societies and advanced industrial machinery.\n"
                            "- The **five long-term causes** (M-A-I-N-E) were Militarism, Alliances, Imperialism, Nationalism, and Economic rivalry.\n"
                            "- The **immediate cause** was the Sarajevo assassination of Franz Ferdinand on 28 June 1914 by Gavrilo Princip.\n"
                            "- The **July Crisis** transformed a local Balkan conflict into a global war through the domino effect of mutual alliance treaties."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 2 DATA — The Course and Fronts of World War I (16 Pages)
# =============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "The Course and Theatres of World War I",
    "lesson_title": "The Course and Fronts of World War I",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Global Theatres of Conflict",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.2 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain Germany's **Schlieffen Plan** and the four specific reasons why it failed\n"
                            "- Describe the conditions, mechanics, and bloody stalemate of **Trench Warfare** on the Western Front\n"
                            "- Analyze the Eastern Front, the Russian Revolution, and the **Treaty of Brest-Litovsk (1918)**\n"
                            "- Explain the War at Sea, the British naval blockade, and German **unrestricted submarine warfare**\n"
                            "- Detail the **African Theatre**, General Paul von Lettow-Vorbeck's campaign, and the sacrifice of the **Carrier Corps** in Kenya\n"
                            "- List and evaluate the revolutionary new military technologies of the Great War"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Overview: A Multi-Front Global War",
                    "content": {
                        "text": (
                            "World War I was not fought on a single battlefield. It was waged across distinct geographic **theatres**:\n\n"
                            "- **The Western Front:** Static, defensive trench warfare stretching across France and Belgium.\n"
                            "- **The Eastern Front:** High-mobility, massive troop maneuvers across Russia, Poland, and East Prussia.\n"
                            "- **The War at Sea:** Naval blockades, dreadnought skirmishes, and lethal U-boat commerce raiding.\n"
                            "- **The African & Middle Eastern Theatres:** Colonial campaigns over strategic railways, ports, and territories."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The German Schlieffen Plan",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Strategic Blueprint: Avoiding a Two-Front War",
                    "content": {
                        "text": (
                            "Germany faced a dangerous geographical dilemma: France to the west and Russia to the east. "
                            "To avoid fighting both simultaneously, Chief of the German General Staff **Count Alfred von Schlieffen** designed a master strategy:\n\n"
                            "1. **Bypass French Fortifications:** Sweep 90% of the German army through neutral Belgium and northern France.\n"
                            "2. **Knock Out France in Six Weeks:** Rapidly encircle and capture Paris before Russia could mobilize its vast but slow-moving army.\n"
                            "3. **Pivot to the East:** Once France surrendered, transfer the victorious German divisions via rail to the Eastern Front to crush Russia."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "The Crucial Assumption",
                    "content": {
                        "text": "The entire Schlieffen Plan rested on the assumption that Russia would take at least six weeks to mobilize its peasant army, and that neutral Belgium would allow German troops free passage without fighting."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Why the Schlieffen Plan Failed",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Four Decisive Obstacles that Shattered the Plan",
                    "content": {
                        "text": "In KCSE examinations, students must provide clear, distinct points explaining why the German plan collapsed in autumn 1914:"
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Four Causes for the Failure of the Schlieffen Plan",
                    "content": {
                        "headers": ["Failure Factor", "Historical Event", "Impact on the German Army"],
                        "rows": [
                            ["1. Heroic Belgian Resistance", "The Belgian army resisted fiercely at the fortress city of Liège.", "Delayed the German advance by crucial weeks, giving Britain and France time to mobilize and deploy troops."],
                            ["2. British Military Intervention", "Germany's invasion of neutral Belgium violated the 1839 Treaty of London, bringing Great Britain into the war immediately.", "The British Expeditionary Force (BEF) landed in France and fought tenacious delaying actions at Mons."],
                            ["3. Rapid Russian Mobilization", "Russia mobilized in just 10 days and invaded East Prussia in August 1914.", "Germany panicked and was forced to divert two full army corps from the Western Front to defend East Prussia."],
                            ["4. The Battle of the Marne (Sept 1914)", "French and British forces launched a massive counter-attack along the River Marne.", "Halted the German army outside Paris, forcing a retreat and ending all hopes of a swift six-week victory."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Trench Warfare and the Western Stalemate",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "British soldiers entrenched during the Battle of the Somme, 1916",
                    "content": {
                        "text": "Soldiers of the British Cheshire Regiment in a deep frontline trench near the Somme in 1916.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Cheshire_Regiment_trench_Somme_1916.jpg",
                        "author": "John Warwick Brooke / Imperial War Museum",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Cheshire_Regiment_trench_Somme_1916.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Life and Death in the Trenches (1914–1918)",
                    "content": {
                        "text": (
                            "Following the Battle of the Marne, both sides engaged in the 'Race to the Sea,' digging a continuous, parallel system "
                            "of defensive trenches stretching **1,080 kilometers** from the Swiss border to the North Sea.\n\n"
                            "**Trench Mechanics:**\n"
                            "- **No Man's Land:** The barren, cratered wasteland separating opposing trenches, filled with tangled barbed wire and landmines.\n"
                            "- **Defensive Dominance:** Rapid-fire machine guns (firing 450–600 rounds per minute) and heavy artillery made frontal infantry charges suicidal.\n"
                            "- **Daily Miseries:** Soldiers endured waterlogged trenches, knee-deep mud, flesh-rotting **trench foot**, massive lice infestations, disease, and the psychological trauma of constant shellfire (**shell shock**)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Primary Source Evidence: Life on the Frontlines",
            "blocks": [
                {
                    "block_type": "suggested_video",
                    "component_type": "suggested_video",
                    "title": "Archival Footage: Trench Warfare, Artillery, and Life on the Western Front",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=QFj23OFl2Kw",
                        "text": "Educational animation and archival analysis examining the daily reality of soldiers in the trenches of World War I, no-man's land, and artillery barrages.",
                        "author": "Simple History",
                        "licensing": "Standard YouTube License"
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Historical Evidence Interpretation: The Somme Trench",
                    "content": {
                        "text": (
                            "**Study the photograph on Page 4 carefully:**\n\n"
                            "1. **Observe:** Notice the narrow sandbagged walls, duckboards placed over mud, steel helmets, and rifles resting against the parapet.\n"
                            "2. **Interpret:** What does the depth and construction of the trench reveal about how permanently the soldiers expected to remain in these positions?\n"
                            "3. **KCSE Evidence Question:** State two physical health hazards that soldiers in these trenches faced during wet European winters.\n"
                            "*(Answer: Trench foot caused by prolonged immersion in cold muddy water, and respiratory illnesses from cold, damp exposure.)*"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Humanity Amidst Total War: The Christmas Truce of 1914",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "A Spontaneous Moment of Peace in No Man's Land",
                    "content": {
                        "text": (
                            "On Christmas Eve and Christmas Day 1914 (24–25 December), along several sectors of the Western Front, "
                            "German, British, and French soldiers spontaneously ceased hostilities.\n\n"
                            "Soldiers climbed out of their trenches into No Man's Land, shook hands, sang carols (*Silent Night / Stille Nacht*), "
                            "exchanged gifts of cigars, chocolate, and newspapers, and played soccer matches in the snow.\n\n"
                            "Horrified by this outbreak of fraternization, high-ranking military commanders issued strict orders threatening court-martial "
                            "for any future truces, rotating units and ordering continuous artillery bombardments to keep hatred alive."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Battles of Attrition: Verdun and the Somme (1916)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Strategy of 'Bleeding the Enemy White'",
                    "content": {
                        "text": (
                            "Unable to break through fortified trench lines, commanders resorted to **wars of attrition**—attempting to kill and exhaust "
                            "so many enemy soldiers that their army would collapse from lack of manpower."
                        )
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Verdun vs the Somme (1916)",
                    "content": {
                        "headers": ["Battle", "Dates", "Commanders & Strategy", "Casualties & Outcome"],
                        "rows": [
                            ["Battle of Verdun", "Feb – Dec 1916 (10 Months)", "German General Erich von Falkenhayn attacked the historic French fortress city of Verdun to 'bleed France white'. French General Philippe Pétain rallied troops with the motto *'Ils ne passeront pas'* (They shall not pass).", "Over 700,000 total casualties (377,000 French, 337,000 German). French held Verdun, but both armies were devastated."],
                            ["Battle of the Somme", "July – Nov 1916 (5 Months)", "Allied joint offensive led by British General Sir Douglas Haig along the River Somme to relieve pressure on Verdun and break German lines.", "Over 1.1 million casualties. British suffered 57,470 casualties on the very first day (1 July 1916)—the bloodiest day in British military history. Advanced barely 10 km; first use of tanks."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "The Eastern Front and the Russian Collapse",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "High Mobility and Imperial Collapse in the East",
                    "content": {
                        "text": (
                            "Unlike the Western Front, the Eastern Front covered thousands of kilometers across Eastern Europe, making trench networks impractical.\n\n"
                            "**Course of the Eastern Conflict:**\n"
                            "- **Early Disasters:** Russian forces invaded East Prussia but were decisively crushed by German Generals Paul von Hindenburg and Erich Ludendorff at the **Battle of Tannenberg** (August 1914) and the **Battle of Masurian Lakes**.\n"
                            "- **Supply Failures:** Although the Russian army was enormous (12 million conscripts), Russian industry could not provide enough rifles, ammunition, boots, or food. Soldiers were sent into battle unarmed, told to pick up rifles from dead comrades.\n"
                            "- **Revolution of 1917:** Catastrophic military defeats and nationwide bread shortages triggered the **Russian Revolution of March 1917**, forcing Tsar Nicholas II to abdicate. In November 1917, Vladimir Lenin's Bolsheviks seized power, promising 'Peace, Land, and Bread'."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "The Treaty of Brest-Litovsk (March 1918)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Russia Exits the War",
                    "content": {
                        "text": (
                            "Determined to consolidate the communist revolution, Vladimir Lenin sent Leon Trotsky to negotiate peace with the Central Powers.\n\n"
                            "On **3 March 1918**, Russia signed the harsh **Treaty of Brest-Litovsk** with Germany:\n\n"
                            "- Russia surrendered **one-third of its population** (56 million people).\n"
                            "- Russia ceded **one-third of its agricultural land** and **nine-tenths of its coal mines**, giving up control of Poland, Ukraine, Finland, Estonia, Latvia, and Lithuania.\n\n"
                            "**Strategic Significance:** The treaty ended the war on the Eastern Front, allowing Germany to transfer over **1 million battle-hardened soldiers** to the Western Front for a massive final offensive."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "The War at Sea and Submarine Warfare",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Blockades and U-Boat Warfare",
                    "content": {
                        "text": (
                            "Command of the oceans was critical to secure overseas supply lines and starve enemy home fronts.\n\n"
                            "1. **The British Royal Navy Blockade:** Britain blockaded the North Sea and English Channel, cutting off Germany from international imports of food, fertilizers, and industrial ores. By 1918, over **750,000 German civilians** had died from malnutrition and disease.\n\n"
                            "2. **German U-Boat Counter-Blockade:** Lacking a large surface fleet, Germany utilized submarines (**Unterseeboote / U-boats**) to sink merchant ships supplying Britain.\n\n"
                            "3. **The Sinking of RMS Lusitania (May 1915):** A German U-boat torpedoed the British passenger liner off Ireland, killing 1,200 civilians (including 128 Americans), causing international outrage.\n\n"
                            "4. **Unrestricted Submarine Warfare (1917):** In January 1917, desperate to break the British blockade, Germany declared it would sink all vessels (neutral and belligerent) trading with Allied ports on sight. This directly provoked the United States into declaring war."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "The African Theatre: West and South-West Africa",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Colonial Warfare Across Africa",
                    "content": {
                        "text": (
                            "When war erupted in Europe, imperial powers immediately attacked neighboring German colonies across Africa to capture ports, wireless radio stations, and territory:\n\n"
                            "- **Togoland:** Fell rapidly in August 1914 to British forces from the Gold Coast (Ghana) and French forces from Dahomey (Benin), securing the strategic Kamina wireless transmitter.\n"
                            "- **Cameroon:** Resisted for nearly two years before joint British, French, and Belgian forces captured Yaoundé in February 1916.\n"
                            "- **German South-West Africa (Namibia):** Captured in July 1915 by South African forces fighting on behalf of the British Empire."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 12,
            "page_title": "The East African Campaign: Lettow-Vorbeck's Guerrilla War",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "General Paul von Lettow-Vorbeck in East Africa",
                    "content": {
                        "text": "General Paul von Lettow-Vorbeck, commander of German colonial forces in German East Africa (Tanganyika).",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Lettow-Vorbeck_1914.jpg",
                        "author": "Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Lettow-Vorbeck_1914.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Guerrilla Warfare in German East Africa (Tanganyika)",
                    "content": {
                        "text": (
                            "The East African campaign was the longest and most elusive campaign of the entire war.\n\n"
                            "The German commander, **General Paul von Lettow-Vorbeck**, possessed only 3,000 German officers and 11,000 disciplined African soldiers (**Askari**).\n\n"
                            "**Lettow-Vorbeck's Master Strategy:** He recognized he could not defeat the British in open battle. Instead, his goal was to **tie down as many British and Allied troops in East Africa as possible**, preventing them from being deployed to the Western Front in Europe.\n\n"
                            "Operating from Mount Kilimanjaro, he launched raids on the vital **Uganda Railway** in Kenya, repulsed British amphibious landings at **Tanga (November 1914)**, and led Allied forces on a four-year pursuit through Tanganyika, Mozambique, and Zambia. He remained undefeated, only surrendering on **25 November 1918** after hearing of the European armistice."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 13,
            "page_title": "The Carrier Corps: Kenya's Sacrifice & Legacy",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Carrier Corps porters during the East African Campaign",
                    "content": {
                        "text": "African porters of the Carrier Corps transporting heavy military baggage across East Africa during World War I.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Carrier_Corps_East_Africa_WWI.jpg",
                        "author": "Imperial War Museum / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Carrier_Corps_East_Africa_WWI.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Unsung Backbone of the East African War",
                    "content": {
                        "text": (
                            "Because tsetse flies killed transport horses and pack oxen, the British military relied entirely on human portage.\n\n"
                            "Over **200,000 Kenyan and East African men** were conscripted into the **Carrier Corps (*Kariakoo*)**, forced to march up to 30 kilometers a day carrying 25 kg loads of ammunition, food, and artillery parts through dense bush and swamps.\n\n"
                            "**Humanitarian Toll:** Over **50,000 Carrier Corps porters died** from malaria, dysentery, exhaustion, and malnutrition—a mortality rate exceeding 20%.\n\n"
                            "**Historical Legacy in Kenya:** The war shattered the myth of European invincibility. Returning African soldiers and porters realized Europeans were mortal and vulnerable, fueling the birth of early nationalist movements (such as the Kikuyu Central Association and Young Kavirondo Association) in the 1920s."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 14,
            "page_title": "Summary of New Weapons and Technologies in WWI",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Seven Revolutionary Weapons of World War I (KCSE List)",
                    "content": {
                        "headers": ["Weapon / Technology", "Pioneered By", "Tactical Role and Battlefield Impact"],
                        "rows": [
                            ["Machine Guns (Maxim/Vickers)", "All Powers", "Fired 450–600 rounds per minute; created automated defensive kill-zones that decimated advancing infantry."],
                            ["Poison Gas (Chlorine/Mustard)", "Germany (1915 at Ypres)", "Chemical weapon causing blindness, lung burns, and suffocation; forced the universal adoption of gas masks."],
                            ["Armored Tanks", "Great Britain (1916 at Somme)", "Heavy caterpillar-tracked vehicles designed to crush barbed wire, cross trenches, and shield infantry."],
                            ["Submarines (U-boats)", "Germany", "Stealth naval vessels firing torpedoes to sink enemy battleships and cut off commercial merchant shipping."],
                            ["Combat Aircraft & Dogfights", "All Powers", "Initially used for aerial reconnaissance; later equipped with synchronized machine guns and bombs."],
                            ["Dreadnought Battleships", "Great Britain", "Massive turbine-powered warships with heavy long-range caliber guns for naval blockades and shore bombardment."],
                            ["Long-Range Field Artillery", "Germany (e.g. Big Bertha)", "Heavy artillery capable of firing explosive shells over 10–20 km behind enemy frontlines."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 15,
            "page_title": "KCSE Examination Coaching & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Question: Explain Five Factors Leading to Trench Warfare Stalemate on the Western Front (10 Marks)",
                    "content": {
                        "text": (
                            "**Model Answer Structure (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                            "1. **Failure of the Schlieffen Plan:** Because the German plan failed to knock France out in six weeks, both armies were halted at the Marne and forced to dig defensive trenches to avoid annihilation. (2 marks)\n\n"
                            "2. **Superiority of Defensive Technology:** Defensive weapons like rapid-fire machine guns and heavy artillery were vastly superior to offensive infantry tactics, making open frontal assaults suicidal. (2 marks)\n\n"
                            "3. **The Unbroken Trench Line:** Trenches stretched continuously for 1,080 km from the Swiss border to the North Sea, eliminating open flanks and preventing either side from outflanking the enemy. (2 marks)\n\n"
                            "4. **The Obstacle of No Man's Land:** The zone between opposing trenches was heavily fortified with deep barbed wire entanglements and pre-sighted artillery craters, pinning down advancing soldiers. (2 marks)\n\n"
                            "5. **Equal Industrial and Manpower Resources:** Both the Allied and Central Powers possessed similar industrial capacity and troop numbers, allowing them to constantly replace battlefield losses without a decisive breakthrough. (2 marks)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 16,
            "page_title": "Check Your Understanding & Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Module 1.2 Mastery Check",
                    "content": {
                        "question": "What was General Paul von Lettow-Vorbeck's primary strategic objective during the East African Campaign?",
                        "options": [
                            "A) To conquer the British colony of Kenya and seize Nairobi",
                            "B) To tie down large numbers of British and Allied troops, preventing their transfer to Europe",
                            "C) To build a permanent German naval base at Mombasa",
                            "D) To capture the Suez Canal in Egypt"
                        ],
                        "correct_answer": "B",
                        "explanation": "Lettow-Vorbeck's strategy was guerrilla warfare: using a small force of German officers and African Askari to tie down over 300,000 Allied troops in East Africa, diverting them from the main Western Front in Europe."
                    }
                },
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.2 Key Takeaways",
                    "content": {
                        "text": (
                            "- The **Schlieffen Plan failed** due to Belgian resistance, British entry, rapid Russian mobilization, and the Battle of the Marne.\n"
                            "- The Western Front developed into a **bloody four-year stalemate** characterized by trench warfare, machine guns, and battles of attrition at Verdun and the Somme.\n"
                            "- On the Eastern Front, Russia suffered disastrous defeats, leading to the **1917 Bolshevik Revolution** and the **Treaty of Brest-Litovsk (1918)**.\n"
                            "- In East Africa, **General von Lettow-Vorbeck** waged an undefeated guerrilla campaign, while over 200,000 African **Carrier Corps** porters suffered heavy mortality, sparking post-war political consciousness."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 3 DATA — US Entry, Allied Victory, and Results of WWI (15 Pages)
# =============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "US Entry, Reasons for Allied Victory, and Results of WWI",
    "lesson_title": "US Entry, Allied Victory, and Results of WWI",
    "pages": [
        {
            "page_number": 1,
            "page_title": "The Decisive Turning Point: 1917–1918",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.3 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- State the three core reasons why the United States maintained **neutrality (1914–1917)**\n"
                            "- Explain the catalysts that forced **US Entry in April 1917** (Lusitania, Zimmermann Telegram, U-boat warfare)\n"
                            "- Detail the **eight examinable reasons for Allied Victory** over the Central Powers\n"
                            "- Classify and explain the **Demographic, Economic, Political, and Technological Results** of World War I"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Overview: The Balance of Power Shifts",
                    "content": {
                        "text": (
                            "By early 1917, both sides in the Great War were on the brink of exhaustion. Russia was collapsing into revolution, "
                            "the French army was rocked by mutinies, and Germany was starving under the British naval blockade.\n\n"
                            "Two historic events transformed the war in 1917: Russia's exit from the conflict, and the **entry of the United States**. "
                            "The arrival of American manpower, financial credit, and industrial output shattered the stalemate and ensured the total defeat of the Central Powers."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Why the United States Remained Neutral (1914–1917)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Three Pillars of American Neutrality",
                    "content": {
                        "text": "For the first three years of the war, President Woodrow Wilson strictly maintained American neutrality based on three factors:"
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Three Reasons for US Neutrality (KCSE Point-form)",
                    "content": {
                        "headers": ["Neutrality Reason", "Detailed Historical Explanation"],
                        "rows": [
                            ["1. The Policy of Isolationism (Monroe Doctrine)", "The US followed the traditional doctrine established by George Washington and James Monroe: European wars were imperial power struggles that did not threaten America's domestic security."],
                            ["2. Diverse Immigrant Population", "The US population contained over 8 million German-Americans alongside millions of Irish, British, and Russian immigrants. Entering the war risked provoking internal ethnic division and civil unrest."],
                            ["3. Immense Commercial and Economic Gains", "As a neutral nation, American businesses made colossal profits selling grain, cotton, steel, chemicals, and munitions to both the Allied and Central Powers, transforming the US from a debtor nation into the world's leading financial creditor."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Catalysts for American Entry in 1917",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Five Factors that Pushed the US into War",
                    "content": {
                        "text": (
                            "Between 1915 and 1917, German military decisions made continued American neutrality impossible:\n\n"
                            "1. **Unrestricted Submarine Warfare:** German U-boats sank American merchant vessels without warning in the Atlantic war zone.\n"
                            "2. **Sinking of Civilian Passenger Liners:** The sinking of the **RMS Lusitania** (May 1915; 128 Americans killed) and the **Sussex** (1916) turned American public opinion furiously against Germany.\n"
                            "3. **The Zimmermann Telegram (Jan 1917):** British intelligence intercepted a secret proposal from German Foreign Minister Arthur Zimmermann offering Mexico an alliance to reconquer Texas, New Mexico, and Arizona.\n"
                            "4. **Protection of Allied Financial Loans:** American banks had lent over **$2 billion** to Britain and France. An Allied defeat would result in complete loan default, threatening the US banking system.\n"
                            "5. **Defense of Democratic Principles:** Following the overthrow of the Russian Tsar in March 1917, Wilson framed the war as a moral struggle to 'make the world safe for democracy'."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Primary Evidence: The Zimmermann Telegram",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "The Decoded 1917 Zimmermann Telegram",
                    "content": {
                        "text": "The decrypted 1917 Zimmermann Telegram proposing a German-Mexican military alliance against the United States.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Zimmermann_Telegram.jpg",
                        "author": "National Archives and Records Administration / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Zimmermann_Telegram.jpg"
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Analyzing the Decoded Message",
                    "content": {
                        "text": (
                            "**Decoded Text Excerpt:** \n"
                            "> *'We intend to begin on the first of February unrestricted submarine warfare... We make Mexico a proposal of alliance on the following basis: make war together, make peace together, generous financial support and an understanding on our part that Mexico is to reconquer the lost territory in Texas, New Mexico, and Arizona...'* \n\n"
                            "**Historical Impact:** When published in American newspapers in March 1917, this telegram eliminated all remaining isolationist opposition, prompting Congress to declare war on Germany on **6 April 1917**."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Decisive Impact of US Entry",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Tide Turns in Favor of the Allies",
                    "content": {
                        "text": (
                            "The entry of the United States provided four immediate, decisive advantages:\n\n"
                            "- **Massive Fresh Manpower:** Over **2 million American soldiers ('Doughboys')** under General John J. Pershing arrived in France, bolstering Allied lines with 10,000 fresh troops daily by mid-1918.\n"
                            "- **Industrial and Manufacturing Power:** US shipyards, steel mills, and assembly lines mass-produced merchant ships, artillery, and aircraft faster than U-boats could sink them.\n"
                            "- **Financial Liquidity:** Massive US government loans restored Allied financial credit, enabling Britain and France to sustain military operations.\n"
                            "- **Psychological Collapse of German Morale:** German troops, exhausted after four years of trench warfare, realized they could not defeat the combined might of Britain, France, and the United States."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "The 1918 Spring Offensive and Allied Counter-Strike",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Final Clashes on the Western Front",
                    "content": {
                        "text": (
                            "In March 1918, German General Erich Ludendorff launched the **Kaiserschlacht (Spring Offensive)**—a massive final gamble "
                            "using elite stormtrooper divisions freed from the Russian front to break Allied lines before the US army arrived in force.\n\n"
                            "Although the Germans advanced 65 km toward Paris, they suffered **800,000 casualties**, outran their supply lines, and exhausted their troops.\n\n"
                            "In August 1918, the Allies launched the **Hundred Days Offensive** under unified Commander-in-Chief **Marshal Ferdinand Foch**. "
                            "Using coordinated tank assaults, aircraft, and fresh American divisions, the Allies smashed through the German Hindenburg Line, forcing a general German retreat."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Reasons for the Allied Victory (Part 1: Material & Manpower)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why the Allies Won: Core Examinable Factors",
                    "content": {
                        "text": "In KCSE examinations, students must explain the comprehensive reasons for Allied victory using distinct structural points:"
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Allied Victory Factors: Material & Strategic",
                    "content": {
                        "headers": ["Allied Advantage", "Detailed Historical Mechanism"],
                        "rows": [
                            ["1. Superior Demographic & Manpower Advantage", "The Allies had 27 member nations (including the British and French global empires), while the Central Powers had only 4. The Allies could continuously replace battlefield casualties."],
                            ["2. Superior Naval Blockade", "The British Royal Navy completely cut off Germany from global food, fertilizer, and ore imports, causing mass civilian starvation and industrial collapse inside Germany."],
                            ["3. Superior Industrial & Financial Wealth", "Allies controlled global sea routes and colonial raw materials, giving them unlimited access to rubber, oil, iron, and financial credit."],
                            ["4. Decisive Entry of the United States", "Brought 2 million fresh troops, vast manufacturing power, and billions in financial credit in 1917, tilting the balance irreversibly."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Reasons for the Allied Victory (Part 2: Leadership & German Collapse)",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Allied Victory Factors: Leadership & Central Powers Collapse",
                    "content": {
                        "headers": ["Allied Advantage", "Detailed Historical Mechanism"],
                        "rows": [
                            ["5. Unified Military Command", "The Allies appointed French Marshal Ferdinand Foch as supreme commander in 1918, coordinating British, French, and American armies into one synchronized counter-offensive."],
                            ["6. Competent Political Leadership", "Allied political leaders (Woodrow Wilson, David Lloyd George, Georges Clemenceau) inspired their populations and coordinated national war economies effectively."],
                            ["7. Weakness & Desertion of German Allies", "Germany's allies collapsed one by one: Bulgaria surrendered in September 1918, the Ottoman Empire in October, and Austria-Hungary dissolved in November, leaving Germany completely alone."],
                            ["8. Spanish Flu & Domestic Revolution", "The 1918 Spanish Flu devastated starving German soldiers. In November 1918, German sailors mutinied at Kiel, workers revolted, Kaiser Wilhelm II abdicated, and Germany collapsed internally."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "The Armistice: 11 November 1918",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Crowds celebrating Armistice Day in Paris, 11 November 1918",
                    "content": {
                        "text": "Celebrations in Paris following the signing of the Armistice on 11 November 1918 ending the First World War.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Armistice_Day_Paris_1918.jpg",
                        "author": "Maurice-Louis Branger / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Armistice_Day_Paris_1918.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Guns Fall Silent",
                    "content": {
                        "text": (
                            "Following the abdication of Kaiser Wilhelm II and the declaration of a German Republic, German delegates met "
                            "Marshal Foch in a railway carriage inside the Forest of Compiègne.\n\n"
                            "At **11:00 AM on 11 November 1918** ('the eleventh hour of the eleventh day of the eleventh month'), the Armistice took effect. "
                            "World War I had officially come to an end after four years, three months, and fourteen days of total warfare."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Results of WWI: Demographic & Social Impact",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Colossal Human Toll",
                    "content": {
                        "text": (
                            "World War I resulted in unprecedented human suffering:\n\n"
                            "- **Massive Loss of Life:** Over **10 million soldiers** and **7 million civilians** died directly from combat, shellfire, starvation, and gas attacks.\n"
                            "- **Wounded and Maimed:** Over **21 million soldiers** suffered permanent physical disabilities, amputations, blindness, and severe facial disfigurements.\n"
                            "- **The 1918 Spanish Flu Pandemic:** Spread rapidly by troop movements and weakened civilian populations, killing an estimated **20–50 million people** worldwide.\n"
                            "- **Refugee Crisis & Social Disruption:** Millions of families were displaced across France, Belgium, Poland, and the Balkans, creating a 'Lost Generation' of traumatized youth."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "Results of WWI: Economic Devastation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Financial Ruin and Colonial Exploitation",
                    "content": {
                        "text": (
                            "The economic consequences reshaped global finance:\n\n"
                            "- **Destruction of European Infrastructure:** Railways, bridges, factories, coal mines, and arable farms across northern France, Belgium, and Eastern Europe were totally pulverized.\n"
                            "- **Colossal War Debts and Inflation:** European nations spent over **$338 billion** on the war, exhausting their gold reserves and triggering rampant inflation, currency collapse, and the Great Depression.\n"
                            "- **Shift of World Financial Power:** The United States transformed from an international debtor into the world's primary financial powerhouse, shifting the global financial capital from London to New York.\n"
                            "- **Increased Colonial Extraction:** To rebuild their shattered economies, European colonial powers intensified taxation, forced labor, and raw material extraction across Kenya and other African territories."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 12,
            "page_title": "Results of WWI: Political Collapse of Four Empires",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "The Fall of Four Great Dynasties and Creation of New States",
                    "content": {
                        "headers": ["Collapsed Empire", "Imperial Dynasty", "Political Outcome & New Sovereign States"],
                        "rows": [
                            ["German Empire", "Hohenzollern", "Kaiser abdicated; Germany became the Weimar Republic; lost European territory and all colonies."],
                            ["Austro-Hungarian Empire", "Habsburg", "Empire dissolved completely; split into Austria, Hungary, Czechoslovakia, and parts of Yugoslavia and Poland."],
                            ["Russian Empire", "Romanov", "Tsarist autocracy overthrown; world's first communist state established (USSR); lost Finland, Poland, and Baltic states."],
                            ["Ottoman Empire", "Ottoman", "Empire dismantled; Middle East partitioned into British and French League Mandates; modern Republic of Turkey founded."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 13,
            "page_title": "Results of WWI: Technological and Medical Advancements",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Scientific & Medical Breakthroughs Born from War",
                    "content": {
                        "headers": ["Field", "Scientific / Technical Breakthrough", "Post-War Civilization Benefit"],
                        "rows": [
                            ["Aviation", "Advancement of metal airframes, powerful engines, and multi-engine bombers.", "Laid the foundation for international commercial passenger flight and airmail services."],
                            ["Medicine & Surgery", "Pioneering of plastic reconstructive surgery, mobile X-ray units (Marie Curie), and blood preservation for transfusions.", "Saved millions of lives post-war; transformed modern emergency trauma care and antiseptic surgery."],
                            ["Motor Transport", "Mass production of reliable internal combustion trucks, ambulances, and caterpillar tractors.", "Revolutionized civilian cargo logistics, passenger buses, and modern mechanized agriculture."],
                            ["Wireless Communication", "Development of portable field radios and two-way voice transmission.", "Accelerated the creation of civilian public radio broadcasting networks in the 1920s."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 14,
            "page_title": "KCSE Examination Coaching & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Question: Explain Six Reasons Why the Allied Powers Defeated the Central Powers (12 Marks)",
                    "content": {
                        "text": (
                            "**Model Answer Structure (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                            "1. **Superior Manpower Advantage:** The Allied coalition comprised 27 nations with access to imperial populations, allowing continuous troop replenishment, whereas the Central Powers had only 4 nations. (2 marks)\n\n"
                            "2. **Effective Naval Blockade:** Britain's Royal Navy blockaded German ports, starving German industries of vital raw materials and civilians of food, leading to domestic collapse. (2 marks)\n\n"
                            "3. **Decisive Entry of the United States:** In 1917, the US entered the war, providing over 2 million fresh troops, vast industrial capacity, and billions in financial credit that overwhelmed Germany. (2 marks)\n\n"
                            "4. **Unified Military Command:** Under French Marshal Ferdinand Foch, Allied forces operated under a single synchronized military command during the decisive 1918 Hundred Days Offensive. (2 marks)\n\n"
                            "5. **Collapse and Desertion of German Allies:** Bulgaria, the Ottoman Empire, and Austria-Hungary surrendered one after another in late 1918, leaving Germany isolated. (2 marks)\n\n"
                            "6. **Internal Revolution in Germany:** Starvation and military exhaustion provoked the Kiel naval mutiny, widespread strikes, and the abdication of Kaiser Wilhelm II, forcing the new government to sign the armistice. (2 marks)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 15,
            "page_title": "Check Your Understanding & Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Module 1.3 Mastery Check",
                    "content": {
                        "question": "Which of the following was NOT one of the four imperial dynasties that collapsed as a direct result of World War I?",
                        "options": [
                            "A) The Romanov dynasty in Russia",
                            "B) The Hohenzollern dynasty in Germany",
                            "C) The Bourbon dynasty in France",
                            "D) The Habsburg dynasty in Austria-Hungary"
                        ],
                        "correct_answer": "C",
                        "explanation": "The four dynasties that collapsed were the Romanovs (Russia), Hohenzollerns (Germany), Habsburgs (Austria-Hungary), and Ottomans (Turkey). The Bourbon monarchy in France had ended in the nineteenth century."
                    }
                },
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.3 Key Takeaways",
                    "content": {
                        "text": (
                            "- The US entered the war in **April 1917** following unrestricted U-boat warfare, the Lusitania sinking, and the Zimmermann Telegram.\n"
                            "- The Allies defeated the Central Powers due to **superior manpower, naval blockade, industrial wealth, US entry, unified command under Foch**, and German internal collapse.\n"
                            "- The **Armistice was signed on 11 November 1918**, concluding the fighting.\n"
                            "- WWI caused **over 17 million deaths**, devastated European economies, destroyed **four great empires**, created new sovereign states, advanced medical surgery/aviation, and catalyzed African anti-colonial consciousness."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 4 DATA — The Peace Settlement and the League of Nations (15 Pages)
# =============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "The Peace Settlement and the League of Nations",
    "lesson_title": "The Peace Settlement and the League of Nations",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Forging a Fragile Peace: Versailles 1919",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.4 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify the **'Big Four' leaders** at the Paris Peace Conference and explain their contrasting national aims\n"
                            "- State the key principles of Woodrow Wilson’s **Fourteen Points**\n"
                            "- Explain the punitive terms of the **Treaty of Versailles (1919)** imposed on Germany\n"
                            "- Analyze the critical flaws of the Versailles Treaty that sowed the seeds of World War II\n"
                            "- Describe the origin, aims, organs, **achievements, and failures of the League of Nations**\n"
                            "- Explain the six specific reasons why the League of Nations collapsed"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Overview: The High-Stakes Peace Negotiations",
                    "content": {
                        "text": (
                            "In January 1919, leaders from 32 victorious Allied nations gathered at the Palace of Versailles outside Paris "
                            "to redraw the map of the world and construct a framework for lasting international security.\n\n"
                            "However, the conference was deeply compromised by conflicting national ambitions: France demanded harsh vengeance, "
                            "Britain sought commercial stability, Italy sought territorial gains, and the United States championed idealistic self-determination. "
                            "The resulting peace treaties imposed humiliating conditions on the defeated nations, creating bitterness that would detonate another world war twenty years later."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Paris Peace Conference & The 'Big Four'",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "The Big Four Leaders at the Paris Peace Conference, 1919",
                    "content": {
                        "text": "The Big Four Allied leaders at Versailles in 1919: David Lloyd George, Vittorio Orlando, Georges Clemenceau, and Woodrow Wilson.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Big_Four_%28Paris_Peace_Conference%29.jpg",
                        "author": "Edward N. Jackson / US Army Signal Corps / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Big_Four_(Paris_Peace_Conference).jpg"
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "The 'Big Four' Allied Leaders and Their Divergent Aims",
                    "content": {
                        "headers": ["Leader & Country", "Title / Moniker", "National Agenda & Demands at Versailles"],
                        "rows": [
                            ["Georges Clemenceau (France)", "Prime Minister ('The Tiger')", "Demanded harsh revenge, massive financial reparations, permanent German disarmament, and the return of Alsace-Lorraine to guarantee French national security."],
                            ["David Lloyd George (Great Britain)", "Prime Minister", "Sought a pragmatic compromise: punish Germany and seize its colonies and navy, but keep Germany economically viable as a British trading partner and barrier against Russian communism."],
                            ["Woodrow Wilson (USA)", "President", "Advocated for an idealistic, non-punitive peace based on his Fourteen Points, national self-determination for ethnic minorities, and the creation of a League of Nations."],
                            ["Vittorio Orlando (Italy)", "Prime Minister", "Focused strictly on securing Austro-Hungarian territories along the Adriatic coast (Trentino, South Tyrol, Istria) promised to Italy in the 1915 Treaty of London."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Woodrow Wilson's Fourteen Points (1918)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "A Blueprint for Global Collective Security",
                    "content": {
                        "text": (
                            "In January 1918, President Wilson presented his **Fourteen Points** to the US Congress as the moral basis for a just and lasting peace. "
                            "Key examinable principles included:\n\n"
                            "1. **Abolition of Secret Diplomacy:** All international treaties must be openly negotiated and publicly registered.\n"
                            "2. **Freedom of Navigation on the High Seas:** Oceans open to all vessels in peace and war.\n"
                            "3. **Removal of Economic Trade Barriers:** Promotion of fair, non-discriminatory international trade.\n"
                            "4. **Worldwide Disarmament:** Reduction of national armaments to the lowest point consistent with domestic safety.\n"
                            "5. **Impartial Adjustment of Colonial Claims:** Giving equal weight to the interests of colonized populations.\n"
                            "6. **National Self-Determination:** Allowing European ethnic nationalities to choose their own sovereign governments.\n"
                            "7. **Restoration of Sovereign Territories:** Full evacuation of Belgium, return of Alsace-Lorraine to France, and an independent Poland with sea access.\n"
                            "8. **Creation of a League of Nations:** A general association of nations formed under specific covenants to guarantee political independence and territorial integrity to great and small states alike."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Terms of the Treaty of Versailles: War Guilt & Reparations",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Imposition of Sole Guilt and Financial Punishment",
                    "content": {
                        "text": (
                            "Signed on **28 June 1919** in the Hall of Mirrors at Versailles, the treaty contained two devastating clauses:\n\n"
                            "1. **Article 231 (The War Guilt Clause):** Germany was forced to accept sole and absolute responsibility for causing all the loss and damage of the war.\n\n"
                            "2. **Colossal Financial Reparations:** Germany was ordered to pay the astronomical sum of **£6.6 billion (132 billion gold marks)** in annual installments to compensate Allied governments for civilian war damage, pensions, and reconstruction.\n\n"
                            "Because German delegates were excluded from negotiations and forced to sign under threat of Allied invasion, Germans called the treaty a **'Diktat' (a dictated peace)**."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Economic Catastrophe",
                    "content": {
                        "text": "The massive reparations burden stripped Germany of its gold reserves, crippled its industrial recovery, and directly catalyzed the catastrophic hyperinflation crisis of 1923, where one US dollar equaled 4.2 trillion German marks."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Terms of the Treaty of Versailles: Military Disarmament",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Military Restrictions Imposed on Germany (KCSE Point-form)",
                    "content": {
                        "headers": ["Military Category", "Treaty of Versailles Restriction"],
                        "rows": [
                            ["Army Size", "Strictly capped at a maximum of 100,000 volunteer soldiers; general conscription was abolished."],
                            ["General Staff & Training", "The German Imperial General Staff was dissolved; military academies were closed."],
                            ["Heavy Armaments", "Prohibited from manufacturing, importing, or possessing tanks, heavy artillery, poison gas, or armored cars."],
                            ["Air Force (Luftwaffe)", "Completely banned from possessing any military aircraft, fighter planes, or zeppelins."],
                            ["Navy Limitations", "Restricted to 6 pre-dreadnought battleships, 6 light cruisers, and 12 destroyers; submarines (U-boats) were completely banned."],
                            ["The Rhineland", "The Rhineland (German territory west of the Rhine and 50 km east) was permanently demilitarized and occupied by Allied troops for 15 years."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Terms of the Treaty of Versailles: Territorial & Colonial Losses",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "German Territorial Losses in Europe and Africa",
                    "content": {
                        "headers": ["Territory Lost", "Recipient Nation / Authority", "Strategic Significance"],
                        "rows": [
                            ["Alsace and Lorraine", "France", "Returned mineral-rich industrial provinces lost by France in 1871."],
                            ["Eupen and Malmédy", "Belgium", "Ceded following local plebiscites to compensate Belgium."],
                            ["Northern Schleswig", "Denmark", "Returned to Denmark after a democratic plebiscite."],
                            ["West Prussia, Posen, & Upper Silesia", "Poland ('Polish Corridor')", "Ceded to re-create an independent Poland; split East Prussia from the rest of Germany."],
                            ["Danzig (Gdansk)", "League of Nations Free City", "Declared a self-governing city to provide Poland sea access to the Baltic."],
                            ["The Saar Basin", "League of Nations (15 Years)", "Coal mines given to France for 15 years, followed by a plebiscite."],
                            ["Anschluss Ban", "Austria", "Any political or economic union between Germany and Austria was strictly forbidden."],
                            ["All Overseas Colonies", "League of Nations Mandates", "Confiscated and partitioned among Britain (Tanganyika), Belgium (Ruanda-Urundi), and South Africa (Namibia)."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Other Peace Treaties of the Paris Conference",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Treaties Signed with Germany's Allies",
                    "content": {
                        "headers": ["Treaty & Year", "Defeated Nation", "Key Terms and Territorial Changes"],
                        "rows": [
                            ["Treaty of Saint-Germain (1919)", "Austria", "Broke up the Austro-Hungarian Empire; Austria lost South Tyrol and Trieste to Italy, Bohemia and Moravia to Czechoslovakia; army limited to 30,000; Anschluss with Germany banned."],
                            ["Treaty of Neuilly (1919)", "Bulgaria", "Bulgaria ceded land to Greece (losing Aegean Sea access) and Yugoslavia; army limited to 20,000; paid £100m reparations."],
                            ["Treaty of Trianon (1920)", "Hungary", "Hungary lost two-thirds of its territory and 3 million nationals to Romania, Czechoslovakia, and Yugoslavia; army capped at 35,000."],
                            ["Treaty of Sèvres (1920) / Lausanne (1923)", "Ottoman Empire (Turkey)", "Sèvres dismantled the Ottoman Empire, giving Arab lands to Britain and France as Mandates. Mustafa Kemal Atatürk led a national revolt, renegotiating the Treaty of Lausanne (1923) which established the modern sovereign Republic of Turkey."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Critical Flaws of the Treaty of Versailles",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Versailles Failed to Maintain Peace",
                    "content": {
                        "text": (
                            "Historians recognize that Versailles was too harsh to be accepted by Germany, yet not harsh enough to permanently crush German power:\n\n"
                            "1. **Deep German Grievance:** Imposing sole war guilt and astronomical reparations united all Germans in hatred of the treaty, providing Adolf Hitler with the political grievances he used to overthrow democracy.\n"
                            "2. **Violation of Self-Determination:** Millions of German-speaking peoples were placed under foreign rule in Poland (the Polish Corridor) and Czechoslovakia (the Sudetenland), creating ethnic powder kegs.\n"
                            "3. **Disillusionment of Italy and Japan:** Italy received few territorial rewards, fueling Mussolini’s fascist takeover. Japan felt racially insulted by Western rejection of a racial equality clause.\n"
                            "4. **US Senate Rejection:** The US Congress refused to ratify the treaty or join the League of Nations, retreating into isolationism and leaving Britain and France to enforce the settlement alone."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "The League of Nations: Origins & Core Aims",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "The League of Nations",
                    "content": {
                        "term": "The League of Nations",
                        "definition": "The world's first permanent international intergovernmental organization, established on 10 January 1920 with headquarters in Geneva, Switzerland, to maintain global peace, resolve international disputes peacefully, and foster social and economic cooperation."
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Five Core Aims of the League of Nations (KCSE List)",
                    "content": {
                        "headers": ["Core Aim", "Detailed Institutional Mandate"],
                        "rows": [
                            ["1. Maintain International Peace & Security", "Prevent the outbreak of another world war through collective security (an attack on one member is an attack on all)."],
                            ["2. Peaceful Settlement of Disputes", "Arbitrate and resolve international border and political disputes before they escalate into open military conflict."],
                            ["3. Promote Global Disarmament", "Enforce mutual reduction of national armaments to the minimum level necessary for domestic defense."],
                            ["4. Foster Social & Economic Cooperation", "Improve global working conditions, eradicate diseases, combat human trafficking, and assist international refugees."],
                            ["5. Supervise Mandated Trust Territories", "Oversee the humane governance and development of former German and Ottoman colonies until they were ready for self-rule."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Structure of the League of Nations",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Six Principal Organs of the League of Nations",
                    "content": {
                        "headers": ["Organ", "Composition & Frequency", "Primary Functions & Mandate"],
                        "rows": [
                            ["The Council", "4 Permanent Members (Britain, France, Italy, Japan) + 4–9 elected non-permanent members; met 3–4 times yearly.", "Executive organ dealing with urgent disputes, military aggression, international sanctions, and disarmament."],
                            ["The Assembly", "Delegates from all member states (each with 1 vote); met once annually in Geneva.", "General debating body; admitted new members, approved the annual budget, and elected non-permanent Council members."],
                            ["The Secretariat", "International civil servants headed by the Secretary-General (first was Sir Eric Drummond).", "Administrative body; managed daily correspondence, prepared agendas, translated records, and registered treaties."],
                            ["Permanent Court of International Justice", "15 international judges based at The Hague, Netherlands.", "Judicial organ; settled legal disputes between sovereign states and gave advisory opinions to Council and Assembly."],
                            ["International Labour Organization (ILO)", "Representatives of governments, employers, and labor unions.", "Set international labor standards, capped maximum daily work hours, and combated child labor."],
                            ["The Mandates Commission", "Specialized committee of colonial experts.", "Monitored standard of living, education, and political administration in League Mandate territories (e.g. Tanganyika, Togo)."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "Tangible Achievements of the League of Nations (1920–1939)",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Seven Major Achievements of the League (KCSE Point-form)",
                    "content": {
                        "headers": ["Area of Achievement", "Historical Example & Tangible Result"],
                        "rows": [
                            ["1. Preserved General Peace for 20 Years", "Successfully prevented a general European war from 1920 until the German invasion of Poland in 1939."],
                            ["2. Resolved Border Disputes Peacefully", "Settled the **Aaland Islands dispute (1921)** between Sweden and Finland, the **Upper Silesia boundary (1921)** between Germany and Poland, and the **Mosul dispute (1926)** between Turkey and Iraq."],
                            ["3. Solved Post-War Refugee Crises", "The Nansen International Office for Refugees issued the famous 'Nansen Passports', resettling over 400,000 displaced prisoners of war and refugees."],
                            ["4. Improved Global Labor Standards", "The ILO introduced the 8-hour workday, 48-hour workweek, established minimum employment ages, and regulated workplace safety."],
                            ["5. Economic Reconstruction of Europe", "Successfully designed and oversaw financial recovery loans for bankrupt Austria and Hungary in the 1920s."],
                            ["6. Combated Global Diseases & Slavery", "The League Health Organization combated epidemics of typhus, malaria, and cholera; the Anti-Slavery Commission liberated 200,000 slaves in Sierra Leone."],
                            ["7. Provided Blueprint for the UN", "Established the structural, legal, and operational template that was later used to create the United Nations in 1945."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 12,
            "page_title": "Critical Failures: Inability to Stop Aggressor Nations",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Collapse of Collective Security in the 1930s",
                    "content": {
                        "text": (
                            "In the 1930s, the League proved completely incapable of stopping militaristic dictators:\n\n"
                            "1. **The Manchurian Crisis (1931–1933):** Japan invaded the Chinese province of Manchuria. When the League issued the Lytton Report condemning the aggression, Japan simply resigned from the League and retained Manchuria.\n\n"
                            "2. **The Abyssinian (Ethiopian) Crisis (1935–1936):** Benito Mussolini's Fascist Italy invaded sovereign Ethiopia, using poison gas against civilian populations. The League imposed weak economic sanctions (excluding oil, coal, and the Suez Canal), which Mussolini ignored. Italy captured Addis Ababa and withdrew from the League.\n\n"
                            "3. **German Rearmament and Remilitarization (1933–1938):** Adolf Hitler withdrew Germany from the League in 1933, introduced conscription, built the Luftwaffe, and marched troops into the demilitarized Rhineland (1936) without any League military response."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 13,
            "page_title": "Why the League of Nations Failed (KCSE Point-form)",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Six Core Causes for the Collapse of the League (KCSE Mark Scheme)",
                    "content": {
                        "headers": ["Failure Factor", "Detailed Historical Explanation"],
                        "rows": [
                            ["1. Non-Membership of the United States", "The US Congress refused to join, depriving the League of the economic, diplomatic, and naval weight of the world's richest superpower."],
                            ["2. Complete Lack of a Standing Army", "The League had no military force of its own. It depended on member states volunteering troops, which nations refused to do for foreign disputes."],
                            ["3. The British and French Policy of Appeasement", "The leading members (Britain and France) prioritized domestic economic recovery and preferred appeasing dictators rather than taking collective military action."],
                            ["4. Perpetual Financial Insolvency", "Many member states were impoverished by war debts and the Great Depression, failing to pay their annual membership subscriptions on time."],
                            ["5. Dominance of National Sovereignty", "Major powers consistently put their own national and colonial interests ahead of international collective security."],
                            ["6. Weak Enforcement Machinery", "Economic sanctions were easily bypassed through trade with non-member states (like the US) and proved useless against determined aggressors."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 14,
            "page_title": "KCSE Examination Coaching & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Question: Explain Five Reasons Why the League of Nations Failed to Maintain World Peace (10 Marks)",
                    "content": {
                        "text": (
                            "**Model Answer Structure (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                            "1. **Absence of Major Superpowers:** The United States never joined the League, and other key powers (Germany, USSR, Japan) were only brief members or withdrew when criticized, denying the League global diplomatic and economic authority. (2 marks)\n\n"
                            "2. **Lack of an Armed Military Force:** The League possessed no standing army to enforce its covenants, relying entirely on economic sanctions which aggressive dictators like Mussolini and Hitler easily ignored. (2 marks)\n\n"
                            "3. **Policy of Appeasement by Leading Members:** Britain and France were traumatized by WWI casualties and prioritized appeasing aggressive dictators (e.g. over Abyssinia and the Rhineland) rather than risking war to enforce League resolutions. (2 marks)\n\n"
                            "4. **Financial Instability:** Many member states were devastated by the Great Depression (1929) and failed to remit their financial contributions, leaving the League chronically underfunded. (2 marks)\n\n"
                            "5. **National Sovereignty Over Collective Security:** Member states prioritized their own national, economic, and imperial interests over international cooperation, refusing to take risks for distant nations. (2 marks)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 15,
            "page_title": "Check Your Understanding & Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Module 1.4 Mastery Check",
                    "content": {
                        "question": "Under the Treaty of Versailles, what was the status assigned to the mineral-rich Saar Basin?",
                        "options": [
                            "A) It was permanently ceded to Belgium as war compensation",
                            "B) It was placed under League of Nations administration for 15 years with coal going to France",
                            "C) It was declared an independent sovereign kingdom",
                            "D) It was retained by Germany with zero restrictions"
                        ],
                        "correct_answer": "B",
                        "explanation": "The Saar Basin was placed under League of Nations control for 15 years, with its lucrative coal output granted to France, after which a plebiscite was held in 1935 where residents voted to rejoin Germany."
                    }
                },
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.4 Key Takeaways",
                    "content": {
                        "text": (
                            "- The **Paris Peace Conference (1919)** was dominated by the 'Big Four': Wilson (USA), Lloyd George (Britain), Clemenceau (France), and Orlando (Italy).\n"
                            "- The **Treaty of Versailles** imposed Article 231 (War Guilt), £6.6bn reparations, an army cap of 100,000, disarmament, loss of Alsace-Lorraine and Polish Corridor, and colonial confiscation.\n"
                            "- The **League of Nations (1920)** achieved significant humanitarian and border successes, but **failed due to US non-membership, lack of a standing army, appeasement**, and inability to stop aggression in Manchuria and Abyssinia."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 5 DATA — World War II: Origins, Causes, and Path to War (13 Pages)
# =============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "World War II — Origins, Causes, and the Path to War",
    "lesson_title": "World War II: Origins, Causes, and the Path to War",
    "pages": [
        {
            "page_number": 1,
            "page_title": "The Drift Toward Global Catastrophe: 1919–1939",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.5 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain how the **unresolved grievances of Versailles** and the **Great Depression (1929)** fueled fascist expansion\n"
                            "- Identify the major **totalitarian dictators** (Hitler, Mussolini, Tojo) and explain their imperial ideologies (*Lebensraum*)\n"
                            "- Trace the failure of the **Policy of Appeasement** through the Rhineland, Austria, and the Munich Crisis\n"
                            "- Explain the strategic significance of the **Nazi-Soviet Non-Aggression Pact (1939)**\n"
                            "- Detail the immediate trigger: The German invasion of **Poland on 1 September 1939**"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Overview: The Twenty-Year Truce",
                    "content": {
                        "text": (
                            "French Marshal Ferdinand Foch famously observed the Treaty of Versailles in 1919 and warned: "
                            "*'This is not peace. It is an armistice for twenty years.'*\n\n"
                            "His prediction was chillingly accurate. In September 1939, exactly twenty years and two months later, the world was plunged "
                            "into World War II—a conflict that would dwarf the First World War in geographical scope, technological destructiveness, and loss of human life."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Resentment of Versailles and German Revanchism",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Hitler's Rise on the Ashes of Versailles",
                    "content": {
                        "text": (
                            "The harsh terms of Versailles (Article 231 war guilt, £6.6bn reparations, disarmament, and loss of territory) "
                            "created an enduring psychological wound in the German psyche.\n\n"
                            "Right-wing German nationalists propagated the **'Dolchstoßlegende' (Stab-in-the-back myth)**, claiming that the heroic German army "
                            "had not been defeated on the battlefield in 1918, but had been betrayed by socialist and democratic politicians at home.\n\n"
                            "Adolf Hitler and the National Socialist (Nazi) Party rose to power by promising to tear up the 'shameful Diktat of Versailles', "
                            "rebuild the German armed forces, restore national honor, and reclaim lost territories."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Rise of Totalitarian Dictatorships",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Adolf Hitler and Benito Mussolini in Munich, 1938",
                    "content": {
                        "text": "Adolf Hitler and Benito Mussolini during a state conference in Munich in 1938.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Hitler_and_Mussolini_June_1940.jpg",
                        "author": "Eva Braun / National Archives / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Hitler_and_Mussolini_June_1940.jpg"
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "The Three Aggressive Axis Powers and Their Expansionist Ideologies",
                    "content": {
                        "headers": ["Nation & Dictator", "Ideology / Regime", "Expansionist Imperial Objective"],
                        "rows": [
                            ["Nazi Germany (Adolf Hitler)", "Nazism (Fascism + Racial Aryan Supremacy)", "Acquire **Lebensraum ('Living Space')** in Eastern Europe and Russia by subjugating Slavic populations and creating a Greater German Reich."],
                            ["Fascist Italy (Benito Mussolini)", "Fascism (Extreme Nationalism & Militarism)", "Recreate the glory of the ancient **Roman Empire** by dominating the Mediterranean Basin (*Mare Nostrum*) and conquering North and East Africa."],
                            ["Imperial Japan (General Hideki Tojo)", "Militarism (Imperial Hegemony)", "Establish the **Greater East Asia Co-Prosperity Sphere** by conquering China, Manchuria, and Southeast Asia to secure oil, rubber, and iron ore."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The Great Depression (1929) and Economic Chaos",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Economic Collapse that Destroyed Democracy",
                    "content": {
                        "text": (
                            "On 29 October 1929 ('Black Tuesday'), the Wall Street stock market collapsed in the United States, triggering the **Great Depression**.\n\n"
                            "**Global Consequences:**\n"
                            "- **Worldwide Unemployment:** Millions of workers lost their jobs, trade collapsed under protective tariffs, and banks failed across Europe.\n"
                            "- **Disillusionment with Democracy:** Desperate citizens lost faith in moderate democratic governments, turning to extremist political movements.\n"
                            "- **Militaristic Expansion as Economic Solution:** In Germany and Japan, fascist leaders argued that democratic trade had failed, and that the only way to secure employment, food, and raw materials was through **military conquest and territorial annexation**."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "The Failure and Impotence of the League of Nations",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Aggressors Act with Impunity",
                    "content": {
                        "text": (
                            "The total failure of the League of Nations to stop early acts of aggression proved to dictators that international collective security was an empty threat:\n\n"
                            "- **Manchuria (1931):** Japan invaded China; the League did nothing except issue a verbal condemnation, and Japan walked out.\n"
                            "- **Abyssinia (1935):** Italy invaded Ethiopia using chemical mustard gas; League sanctions excluded oil and the Suez Canal remained open to Italian warships.\n"
                            "- **German Rearmament (1935):** Hitler announced re-conscription and created the Luftwaffe in open violation of Versailles; the League took zero military action."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "The Policy of Appeasement (1936–1938)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Concessions in the Hope of Peace",
                    "content": {
                        "text": (
                            "**Appeasement** was the diplomatic policy pursued by British Prime Minister **Neville Chamberlain** and French leaders, "
                            "giving in to Hitler’s territorial demands in the belief that satisfying his grievances would avoid another catastrophic European war.\n\n"
                            "Instead, appeasement convinced Hitler that Western democracies were weak, cowardly, and would never fight."
                        )
                    }
                },
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "Hitler's Unchecked Expansionist Steps",
                    "content": {
                        "steps": [
                            "March 1936: Hitler remilitarizes the Rhineland; Britain and France take no military action.",
                            "March 1938: Anschluss (Annexation of Austria); German troops march into Vienna unopposed.",
                            "September 1938: The Munich Agreement; Britain and France force Czechoslovakia to surrender the Sudetenland to Germany in exchange for Hitler's promise of peace.",
                            "March 1939: Hitler violates the Munich Agreement, invading and conquering the rest of Czechoslovakia; appeasement collapses.",
                            "March 1939: Britain and France issue a formal military guarantee to defend Poland against German aggression."
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "The Axis Alliance and the Nazi-Soviet Pact",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Key Alliances Leading to World War II",
                    "content": {
                        "headers": ["Alliance & Date", "Signatory Nations", "Core Strategic Terms & Consequences"],
                        "rows": [
                            ["Rome-Berlin Axis (1936)", "Germany and Italy", "Mutual diplomatic and military support; formalized fascist cooperation in Europe."],
                            ["Anti-Comintern Pact (1936–1937)", "Germany, Japan, Italy", "Pact directed against the Soviet Union and international communism; formed the Berlin-Rome-Tokyo Axis."],
                            ["Pact of Steel (May 1939)", "Germany and Italy", "Formal military alliance pledging full military assistance in the event of war."],
                            ["Nazi-Soviet Non-Aggression Pact (August 1939)", "Nazi Germany (Hitler) & USSR (Stalin)", "10-year non-aggression agreement with a secret protocol to invade and partition Poland between them. Freed Germany from facing a two-front war when attacking Poland."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "The Immediate Cause: The German Invasion of Poland",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "1 September 1939: World War II Begins",
                    "content": {
                        "text": (
                            "Following the signing of the Nazi-Soviet Pact, Hitler demanded the return of Danzig and the Polish Corridor.\n\n"
                            "At **4:45 AM on 1 September 1939**, without a formal declaration of war, German armored divisions, infantry, and Luftwaffe dive-bombers "
                            "launched a massive invasion of Poland (**Blitzkrieg**).\n\n"
                            "Great Britain and France issued an ultimatum demanding immediate German withdrawal. When Hitler ignored the ultimatum, "
                            "Britain and France honored their defense treaty with Poland and declared war on Germany on **3 September 1939**.\n\n"
                            "World War II had officially begun."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Interactive Task: Categorizing the Causes of WWII",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Classify the Causes of the Second World War",
                    "content": {
                        "instruction": "Test your historical understanding. Categorize each factor into its correct dimension:",
                        "items": [
                            "1. German anger over the loss of the Polish Corridor -> **Legacy of Versailles**",
                            "2. The 1929 Wall Street stock market collapse -> **Economic Crisis (Great Depression)**",
                            "3. The Munich Agreement over the Sudetenland -> **Policy of Appeasement**",
                            "4. Hitler's concept of Lebensraum in the East -> **Totalitarian Ideology (Nazism)**",
                            "5. The signing of the Berlin-Rome-Tokyo Axis -> **Alliance Systems**",
                            "6. German troops crossing the Polish border on 1 Sept 1939 -> **Immediate Trigger**"
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Primary Source Evidence: Chamberlain vs Churchill",
            "blocks": [
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Two Opposing Historical Visions on Appeasement (1938)",
                    "content": {
                        "text": (
                            "**Source A (Neville Chamberlain, returning from Munich, 30 Sept 1938):**\n"
                            "> *'My good friends, this is the second time in our history that there has come back from Germany to Downing Street peace with honour. I believe it is peace for our time... Go home and get a nice quiet sleep.'*\n\n"
                            "**Source B (Winston Churchill, speech in House of Commons, 5 Oct 1938):**\n"
                            "> *'We have sustained a total and unmitigated defeat... You were given the choice between war and dishonour. You chose dishonour, and you will have war.'*\n\n"
                            "**Historical Inquiry Questions:**\n"
                            "1. Why did the British public overwhelmingly celebrate Chamberlain's statement in 1938?\n"
                            "2. How did Churchill's prediction prove accurate within eleven months?"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "KCSE Examination Coaching & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Question: Explain Five Causes of the Second World War (10 Marks)",
                    "content": {
                        "text": (
                            "**Model Answer Structure (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                            "1. **The Harsh Legacy of the Treaty of Versailles:** The humiliation, reparations, and territorial losses imposed on Germany created deep national bitterness which Adolf Hitler exploited to gain power and justify aggressive expansion. (2 marks)\n\n"
                            "2. **Rise of Totalitarian Dictators (Fascism and Nazism):** Aggressive leaders in Germany (Hitler), Italy (Mussolini), and Japan (Tojo) glorified militarism and pursued aggressive imperial conquest (*Lebensraum* and Roman Empire revival). (2 marks)\n\n"
                            "3. **The Great Depression (1929):** Global economic collapse caused widespread unemployment and poverty, destroying faith in democratic governments and allowing militaristic dictators to seize power. (2 marks)\n\n"
                            "4. **Failure of the League of Nations:** The League proved completely incapable of stopping aggression in Manchuria (1931) and Abyssinia (1935), demonstrating to Hitler that international covenants could be broken with impunity. (2 marks)\n\n"
                            "5. **The British and French Policy of Appeasement:** Concessions made to Hitler at Munich (1938) convinced him that Western democracies were weak, encouraging him to make bolder territorial demands in Poland. (2 marks)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 12,
            "page_title": "Knowledge Check: WWII Causes & Dictators",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Module 1.5 Mastery Check",
                    "content": {
                        "question": "What secret agreement was contained in the Nazi-Soviet Non-Aggression Pact of August 1939?",
                        "options": [
                            "A) Germany and the USSR agreed to share atomic research",
                            "B) Germany and the USSR agreed to invade and divide Poland between themselves",
                            "C) The USSR agreed to join the Berlin-Rome-Tokyo Axis",
                            "D) Germany agreed to cede East Prussia to the Soviet Union"
                        ],
                        "correct_answer": "B",
                        "explanation": "The secret protocol of the Molotov-Ribbentrop Pact divided Eastern Europe into Nazi and Soviet spheres of influence, agreeing that both powers would invade and partition Poland."
                    }
                }
            ]
        },
        {
            "page_number": 13,
            "page_title": "Module 1.5 Summary and Takeaways",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.5 Key Takeaways",
                    "content": {
                        "text": (
                            "- World War II was caused by the **grievances of Versailles, the rise of fascist dictatorships, the Great Depression, the failure of the League of Nations**, and the **policy of appeasement**.\n"
                            "- The Axis powers (Germany, Italy, Japan) formed aggressive alliances directed at imperial conquest.\n"
                            "- The **Nazi-Soviet Pact (Aug 1939)** cleared the path for Hitler to attack Poland without fear of a two-front war.\n"
                            "- The **German invasion of Poland on 1 September 1939** directly triggered the declarations of war by Britain and France on 3 September 1939."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 6 DATA — The Course and Fronts of World War II (16 Pages)
# =============================================================================
LESSON_6_DATA = {
    "unit_order": 6,
    "unit_name": "The Course and Theatres of World War II",
    "lesson_title": "The Course and Fronts of World War II",
    "pages": [
        {
            "page_number": 1,
            "page_title": "A Mobile, Mechanized Global Conflict",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.6 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define the German military tactic of **Blitzkrieg** and explain how France fell in six weeks\n"
                            "- Analyze the **Battle of Britain (1940)**, radar defense, and Winston Churchill's leadership\n"
                            "- Explain **Operation Barbarossa (1941)** and why the **Battle of Stalingrad (1942–1943)** was the decisive turning point\n"
                            "- Describe the North African Campaign and General Montgomery's victory at **El Alamein (1942)**\n"
                            "- Detail the Pacific War, the attack on **Pearl Harbor (1941)**, and the atomic bombings of **Hiroshima and Nagasaki (1945)**\n"
                            "- Explain the five key factors that enabled the Allies to win World War II"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Overview: High-Speed Industrial Warfare",
                    "content": {
                        "text": (
                            "Unlike the trench stalemates of WWI, World War II was a war of rapid movement, mechanized armor, aircraft carriers, "
                            "and strategic air bombardment. Fought across Europe, Russia, North Africa, Southeast Asia, and the Pacific Ocean, "
                            "it witnessed the catastrophic rise and ultimate destruction of the Axis empires."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Blitzkrieg Tactic and the Polish Campaign",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Blitzkrieg (Lightning War)",
                    "content": {
                        "term": "Blitzkrieg",
                        "definition": "A high-speed offensive military doctrine combining armored tank divisions (Panzers), motorized infantry, and close tactical dive-bombers (Luftwaffe Stukas) to rapidly penetrate, encircle, and paralyze enemy defensive lines before they can organize resistance."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Overrunning of Poland (September 1939)",
                    "content": {
                        "text": (
                            "German armored columns smashed through Polish defenses, encircling Warsaw within two weeks. "
                            "On **17 September 1939**, the Soviet Red Army invaded Poland from the east under the secret terms of the Nazi-Soviet Pact. "
                            "Attacked from both sides, Polish resistance collapsed by late September, and Poland was partitioned between Germany and the USSR."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Phoney War and the Fall of Western Europe (1940)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "From Inactivity to Lightning Conquest",
                    "content": {
                        "text": (
                            "For eight months (Sept 1939 – April 1940), an eerie lull called the **'Phoney War'** existed on the Western Front as both sides mobilized.\n\n"
                            "**The Blitzkrieg Strikes (Spring 1940):**\n"
                            "- **April 1940:** Germany invaded Denmark (fell in 6 hours) and Norway. British military failures in Norway forced Prime Minister Neville Chamberlain to resign, replaced by **Winston Churchill**.\n"
                            "- **May 1940:** German tanks swept through the Ardennes Forest, bypassing the heavily fortified French Maginot Line, conquering the Netherlands and Belgium in days.\n"
                            "- **Dunkirk Evacuation (Operation Dynamo):** Trapped against the English Channel, **338,000 British and French soldiers** were rescued by an armada of naval destroyers and civilian 'little ships'.\n"
                            "- **Fall of France (June 1940):** German troops entered Paris on 14 June. France surrendered, divided into a German-occupied northern zone and a puppet collaborationist regime in the south (**Vichy France** led by Marshal Philippe Pétain)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Why France Fell So Quickly (KCSE Point-form)",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Three Decisive Factors in the Fall of France (KCSE Mark Scheme)",
                    "content": {
                        "headers": ["Factor", "Detailed Historical Mechanism"],
                        "rows": [
                            ["1. Flawed Defensive Military Doctrine", "French generals were stuck in the static WWI mindset, relying heavily on the concrete Maginot Line which Germany simply bypassed through the Ardennes Forest."],
                            ["2. German Tactical Air Superiority", "The German Luftwaffe systematically bombed French communication lines, road networks, and troop concentrations, paralyzing command centers."],
                            ["3. Psychological Shock and Poor Coordination", "French leadership was stunned by the speed of German armor and failed to coordinate armored counter-offensives with the British army."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "The Battle of Britain (July–October 1940)",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "St Paul's Cathedral surviving during the London Blitz, 1940",
                    "content": {
                        "text": "St Paul's Cathedral rising intact above smoke and destruction during the German Luftwaffe bombing of London in 1940.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/St_Paul%27s_Cathedral_during_the_Blitz.jpg",
                        "author": "Herbert Mason / Daily Mail / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:St_Paul%27s_Cathedral_during_the_Blitz.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Hitler's First Major Defeat",
                    "content": {
                        "text": (
                            "To invade Britain (**Operation Sea Lion**), Germany had to achieve air superiority over the English Channel.\n\n"
                            "For three months, Hermann Göring's Luftwaffe bombed British airfields, radar stations, and civilian cities (**The Blitz**).\n\n"
                            "**Why Britain Survived:**\n"
                            "- **The Royal Air Force (RAF):** Fighter pilots flying fast Supermarine Spitfires and Hawker Hurricanes outfought German bombers.\n"
                            "- **Radar Technology:** Early warning radar networks allowed the RAF to intercept German bombers before they reached targets.\n"
                            "- **Winston Churchill's Leadership:** Churchill rallied national resistance, famously declaring: *'Never in the field of human conflict was so much owed by so many to so few.'*\n\n"
                            "In October 1940, having lost over 1,700 aircraft, Hitler cancelled Operation Sea Lion indefinitely."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "The Eastern Front: Operation Barbarossa (1941)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Invasion of the Soviet Union",
                    "content": {
                        "text": (
                            "On **22 June 1941**, Hitler broke the Nazi-Soviet Pact and launched **Operation Barbarossa**—the largest land invasion in history, "
                            "deploying 3.8 million Axis soldiers along a 2,900 km front.\n\n"
                            "**Course of the Invasion:**\n"
                            "- German armor advanced rapidly, encircling Leningrad (900-day siege) and reaching the outskirts of Moscow by November 1941.\n"
                            "- **The Scorched-Earth Defense:** Soviet forces destroyed all grain stores, railways, factories, and bridges as they retreated, denying Germany supplies.\n"
                            "- **The Russian Winter:** Hitler had expected victory within three months and failed to issue winter uniforms or engine antifreeze. Temperatures plummeted to -40°C, freezing tank engines and decimating German soldiers."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "The Battle of Stalingrad: Decisive Turning Point",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Turning Tide: August 1942 – February 1943",
                    "content": {
                        "text": (
                            "In 1942, German forces pushed south to capture the Soviet oil fields in the Caucasus and the industrial city of **Stalingrad** on the Volga River.\n\n"
                            "**The Battle:**\n"
                            "- Soviet and German troops fought a ferocious room-by-room, street-by-street battle (*'Rattenkrieg'*).\n"
                            "- In November 1942, Soviet Marshal **Georgy Zhukov** launched a massive pincer counter-offensive (**Operation Uranus**), encircling the German 6th Army under Field Marshal Friedrich Paulus.\n"
                            "- Refusing Hitler's orders to fight to the death, Paulus surrendered on **2 February 1943** with 91,000 starving survivors.\n\n"
                            "**Significance:** Stalingrad was the turning point of WWII. Germany lost over **300,000 soldiers** and never regained the offensive on the Eastern Front. From Stalingrad onward, the Red Army relentlessly pushed German forces back toward Berlin."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Why Germany Was Defeated in the USSR (KCSE Point-form)",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Five Reasons for German Defeat in Russia (KCSE Mark Scheme)",
                    "content": {
                        "headers": ["Failure Reason", "Detailed Historical Mechanism"],
                        "rows": [
                            ["1. The Multi-Front War", "Germany was forced to fight simultaneously in Russia, North Africa, the Atlantic, and defend against Western air bombing, diluting military resources."],
                            ["2. Soviet Scorched-Earth Strategy", "Red Army retreated while burning crops and blowing up bridges, leaving advancing German divisions without food or shelter."],
                            ["3. Failure to Prepare for Winter", "Overconfident Nazi leadership failed to provide winter overcoats, boots, or engine lubricants, causing mass frostbite and equipment failure."],
                            ["4. Relocation of Soviet War Industry", "The USSR dismantled 1,500 factories and rebuilt them east of the Ural Mountains, mass-producing superior T-34 tanks and Katyusha rockets out of German bomber range."],
                            ["5. Hitler's Rigid 'No-Retreat' Orders", "Hitler micro-managed the military and forbade tactical retreats, leading directly to the encirclement and destruction of the entire 6th Army at Stalingrad."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "The North African & Mediterranean Theatres",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Struggle for the Suez Canal and Middle Eastern Oil",
                    "content": {
                        "text": (
                            "In 1940, Mussolini invaded Egypt to seize the British-controlled **Suez Canal**, the imperial shipping lifeline to India and the oil fields of the Persian Gulf.\n\n"
                            "**Key Developments:**\n"
                            "- **The Desert Fox:** German General **Erwin Rommel** and his specialized tank divisions (**Afrika Korps**) pushed British forces back to the Egyptian border.\n"
                            "- **The Battle of El Alamein (October–November 1942):** British General **Bernard Montgomery** launched a massive armored offensive at El Alamein in Egypt, decisively crushing Rommel’s forces.\n"
                            "- **Allied Surrender of Axis in Africa (May 1943):** American and British forces landed in Morocco and Algeria (**Operation Torch**), trapping Axis forces in Tunisia, capturing 250,000 prisoners and clearing North Africa."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "The Pacific Theatre & Attack on Pearl Harbor",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "7 December 1941: 'A Date Which Will Live in Infamy'",
                    "content": {
                        "text": (
                            "To conquer Southeast Asia without American naval interference, Japanese aircraft carriers launched a surprise dawn attack on the "
                            "US Pacific Fleet at **Pearl Harbor, Hawaii** on **7 December 1941**.\n\n"
                            "- Over 2,400 Americans were killed, and 8 battleships were sunk or damaged.\n"
                            "- On 8 December 1941, US President Franklin D. Roosevelt declared war on Japan, bringing the United States into WWII.\n\n"
                            "**The Pacific Turning Point:**\n"
                            "At the **Battle of Midway (June 1942)**, US carrier-based dive bombers sank four Japanese aircraft carriers in one day, shattering Japanese naval dominance and initiating the Allied 'island-hopping' counter-offensive toward Tokyo."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "The Allied Counter-Offensive: D-Day to Berlin",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Allied Troops Landing in Normandy on D-Day, 6 June 1944",
                    "content": {
                        "text": "Allied soldiers landing on Omaha Beach during the Normandy Invasion (Operation Overlord) on 6 June 1944.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Into_the_Jaws_of_Death_23-0455M_edit.jpg",
                        "author": "Chief Photographer's Mate Robert F. Sargent / US Coast Guard / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Into_the_Jaws_of_Death_23-0455M_edit.jpg"
                    }
                },
                {
                    "block_type": "suggested_video",
                    "component_type": "suggested_video",
                    "title": "Documentary Footage: The D-Day Normandy Landings (6 June 1944)",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=4cGuB-OWR0g",
                        "text": "Simple History documentary tracing Operation Overlord and the 6 June 1944 D-Day landings in Normandy that opened the Western Front against Nazi Germany.",
                        "author": "Simple History",
                        "licensing": "Standard YouTube License"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "D-Day and the Fall of Nazi Germany",
                    "content": {
                        "text": (
                            "On **6 June 1944 (D-Day)**, under the supreme command of US General **Dwight D. Eisenhower**, Allied forces launched **Operation Overlord**—the "
                            "largest amphibious invasion in history, landing 156,000 American, British, and Canadian troops on the beaches of Normandy, France.\n\n"
                            "**The Final Collapse:**\n"
                            "- Allies liberated Paris in August 1944 and advanced toward the Rhine.\n"
                            "- In the East, the Soviet Red Army swept through Poland and stormed Berlin in April 1945.\n"
                            "- Faced with capture, **Adolf Hitler committed suicide** in his underground Berlin bunker on **30 April 1945**.\n"
                            "- On **8 May 1945 (V-E Day)**, Germany surrendered unconditionally, concluding the war in Europe."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 12,
            "page_title": "The Atomic Bombs on Hiroshima and Nagasaki",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Atomic Bomb Mushroom Cloud over Nagasaki, 9 August 1945",
                    "content": {
                        "text": "The radioactive mushroom cloud rising over Nagasaki, Japan, following the atomic bombing on 9 August 1945.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/54/Nagasaki_1945_-_Nagasaki_blast.jpg",
                        "author": "Charles Levy / US Army Air Forces / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nagasaki_1945_-_Nagasaki_blast.jpg"
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "August 1945: The Dawn of the Nuclear Age",
                    "content": {
                        "text": (
                            "Although facing certain defeat, Japan’s military leadership refused unconditional surrender, deploying suicide **Kamikaze** pilots.\n\n"
                            "To prevent an estimated 1 million casualties from a mainland invasion of Japan, US President **Harry S. Truman** ordered the use of atomic weapons:\n\n"
                            "- **6 August 1945:** The B-29 bomber *Enola Gay* (Col. Paul Tibbets) dropped the uranium bomb 'Little Boy' on **Hiroshima**, killing 78,000 instantly.\n"
                            "- **9 August 1945:** A second plutonium bomb 'Fat Man' was dropped on **Nagasaki**, killing over 40,000.\n"
                            "- On **15 August 1945 (V-J Day)**, Japanese Emperor Hirohito announced surrender, formally signed on **2 September 1945** aboard the USS Missouri."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 13,
            "page_title": "Case Study: The Hiroshima Atomic Bomb",
            "blocks": [
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "Historical Breakdown: Hiroshima (6 August 1945)",
                    "content": {
                        "steps": [
                            "WHO: US Army Air Forces B-29 bomber 'Enola Gay', piloted by Colonel Paul Tibbets under orders from President Harry S. Truman.",
                            "WHEN: Monday, 6 August 1945 at 8:15 AM local time.",
                            "WHERE: The industrial and military garrison city of Hiroshima, Honshu Island, Japan.",
                            "WHAT: Dropped a single 4,400 kg uranium atomic bomb which detonated 580 meters above the city with an energy release equal to 15,000 tons of TNT.",
                            "WHY: To force Japan to surrender unconditionally without a bloody amphibious invasion of the Japanese mainland.",
                            "RESULT: Vaporized 12 square kilometers of the city; killed 78,000 people instantly, with tens of thousands dying later from radiation burns and leukemia.",
                            "SIGNIFICANCE: Concluded World War II, initiated the Nuclear Arms Race, and transformed global geopolitical warfare forever."
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 14,
            "page_title": "Factors Enabling Allied Victory in WWII (KCSE Point-form)",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Five Factors that Won the War for the Allies (KCSE Mark Scheme)",
                    "content": {
                        "headers": ["Allied Factor", "Detailed Historical Mechanism"],
                        "rows": [
                            ["1. Colossal Industrial and Economic Output", "The US mass-produced Liberty ships, B-29 bombers, and Sherman tanks faster than Axis submarines could destroy them; outproduced Axis manufacturing by 3 to 1."],
                            ["2. Decisive Entry of the United States", "Brought fresh millions of troops, absolute financial credit, naval carrier power, and the Manhattan Project atomic bomb."],
                            ["3. Control of Sea Lanes and Air Superiority", "Allied naval dominance protected supply convoys across the Atlantic and Pacific, while round-the-clock strategic bombing flattened German oil refineries and transport."],
                            ["4. Massive Soviet Military Sacrifice", "The USSR mobilized 30 million soldiers, bore the brunt of German ground combat, and destroyed 75% of all German divisions on the Eastern Front."],
                            ["5. Severe Axis Strategic Blunders", "Hitler's failure to prepare for Russian winter, declaring war on the US, and micro-managing generals doomed Axis military strategy."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 15,
            "page_title": "KCSE Examination Coaching & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Question: Explain Five Factors that Enabled the Allies to Win the Second World War (10 Marks)",
                    "content": {
                        "text": (
                            "**Model Answer Structure (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                            "1. **Superior Economic and Industrial Output:** The Allies, led by the United States, outproduced the Axis powers in tanks, aircraft, warships, and munitions, giving them unlimited material supplies. (2 marks)\n\n"
                            "2. **Massive Soviet Military Contribution:** The Soviet Red Army engaged the bulk of the German military on the Eastern Front, inflicting catastrophic defeats at Stalingrad and Kursk that crippled German manpower. (2 marks)\n\n"
                            "3. **Allied Air and Naval Superiority:** Allied air forces bombed German industrial cities and synthetic oil plants, while radar and naval convoys defeated German U-boats in the Battle of the Atlantic. (2 marks)\n\n"
                            "4. **German Strategic and Military Mistakes:** Hitler fought a multi-front war, failed to prepare for the Russian winter, and refused to permit tactical retreats, leading to massive army surrenders. (2 marks)\n\n"
                            "5. **Technological and Scientific Superiority:** Allied breakthroughs in radar, code-breaking (Enigma/Ultra), and the atomic bomb (Manhattan Project) gave the Allies overwhelming tactical and strategic advantages. (2 marks)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 16,
            "page_title": "Check Your Understanding & Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Module 1.6 Mastery Check",
                    "content": {
                        "question": "Which decisive tank battle in November 1942 halted General Erwin Rommel's advance in North Africa?",
                        "options": [
                            "A) The Battle of Stalingrad",
                            "B) The Battle of El Alamein",
                            "C) The Battle of Midway",
                            "D) The Battle of the Bulge"
                        ],
                        "correct_answer": "B",
                        "explanation": "The Second Battle of El Alamein in Egypt (October–November 1942), won by British General Bernard Montgomery, decisively crushed Rommel's Afrika Korps and ended Axis threats to the Suez Canal."
                    }
                },
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.6 Key Takeaways",
                    "content": {
                        "text": (
                            "- Germany conquered Poland and Western Europe in 1939–1940 using **Blitzkrieg tactics**.\n"
                            "- Britain survived the **Battle of Britain (1940)** through the RAF, radar, and Churchill's leadership.\n"
                            "- The **Battle of Stalingrad (1942–1943)** was the decisive turning point on the Eastern Front, shattering German offensive power.\n"
                            "- The US entered after **Pearl Harbor (7 Dec 1941)**; Allied forces invaded France on **D-Day (6 June 1944)**; Germany surrendered on **8 May 1945**.\n"
                            "- The **atomic bombings of Hiroshima and Nagasaki in August 1945** forced Japan's unconditional surrender, ending World War II."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 7 DATA — Global Results of WWII and Rise of the UN (14 Pages)
# =============================================================================
LESSON_7_DATA = {
    "unit_order": 7,
    "unit_name": "Global Results of WWII and the United Nations Organization",
    "lesson_title": "Global Results of WWII and the Rise of the United Nations",
    "pages": [
        {
            "page_number": 1,
            "page_title": "The Dawn of the Post-War World Order",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.7 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Detail the **Social and Demographic Results** of WWII (Loss of life, Holocaust, refugees, women's status)\n"
                            "- Explain the **Economic Results** of WWII (Destruction, debts, European Economic Community founding in 1957)\n"
                            "- Analyze the **Political and Geopolitical Results** (Division of Germany, Superpower rivalry, Cold War outbreak)\n"
                            "- Explain how WWII accelerated **African Nationalism and Decolonisation**\n"
                            "- Describe the founding and mission of the **United Nations Organization (24 October 1945)**"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Overview: A New World Order",
                    "content": {
                        "text": (
                            "World War II ended with the total defeat of Fascism and Nazism, but it left the planet fundamentally transformed. "
                            "The old European colonial empires (Britain, France) were financially bankrupt and militarily exhausted. "
                            "Two new global Superpowers—the United States and the Soviet Union—emerged to divide the world along capitalist and communist lines, "
                            "while colonized peoples in Africa and Asia rose up to demand immediate independence."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Social and Demographic Results of WWII",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Six Major Social Consequences of WWII (KCSE Point-form)",
                    "content": {
                        "headers": ["Social Consequence", "Detailed Historical Impact"],
                        "rows": [
                            ["1. Massive Loss of Human Life", "Between 50 and 70 million people died (approx. 3% of world population), including over 6 million Jews murdered in the Nazi Holocaust."],
                            ["2. Massive Refugee & Displacement Crisis", "Over 20 million displaced persons roamed Europe; led directly to the creation of the State of Israel in 1948 to resettle Jewish refugees."],
                            ["3. Permanent Trauma and Physical Disability", "Tens of millions suffered permanent amputations, psychological trauma, and illness from concentration camps and slave labor."],
                            ["4. Transformation of the Status of Women", "Widespread mobilization of men forced millions of women into factories, offices, and military logistics, catalyzing the post-war women's rights movement."],
                            ["5. Radioactive and Environmental Contamination", "Atomic fallout in Hiroshima and Nagasaki caused cancer, leukemia, and birth defects across generations."],
                            ["6. Erosion of European Superiority Myth", "Widespread atrocities and battlefield defeats suffered by Europeans proved to Africans that white colonizers were mortal and vulnerable."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Economic Consequences of World War II",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Five Economic Results of WWII (KCSE Point-form)",
                    "content": {
                        "headers": ["Economic Result", "Detailed Historical Impact"],
                        "rows": [
                            ["1. Complete Infrastructure Destruction", "Railways, bridges, harbors, power plants, and industrial cities across Germany, Japan, USSR, and Britain were reduced to rubble."],
                            ["2. Bankruptcy of European Powers", "Britain and France spent their national wealth on weapons, emerging heavily indebted to the United States."],
                            ["3. The US Marshall Plan (1948)", "The United States provided $13 billion in economic grants and food aid to rebuild Western European industries and prevent communist revolutions."],
                            ["4. Intensified Colonial Exploitation", "Bankrupt imperial powers extracted agricultural cash crops (tea, coffee, sisal) and forced labor from African colonies to rebuild domestic economies."],
                            ["5. Rise of European Economic Cooperation", "Recognizing that small separate economies could not survive, Western European nations signed the Treaty of Rome (1957) creating the European Economic Community (EEC)."]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Political Results: Emergence of Two Superpowers",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Bipolar World: USA vs USSR",
                    "content": {
                        "text": (
                            "World War II destroyed the traditional European balance of power, creating a **bipolar world** dominated by two superpowers:\n\n"
                            "- **The United States:** Emerged as the undisputed capitalist, democratic superpower, possessing the atomic bomb, the world's largest navy, and 50% of global industrial manufacturing.\n"
                            "- **The Soviet Union (USSR):** Emerged as the undisputed communist superpower, possessing the massive Red Army, occupying Eastern Europe, and developing its own nuclear bomb by 1949."
                        )
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "The Ideological Divide of the Superpowers",
                    "content": {
                        "headers": ["Dimension", "United States (Western Bloc)", "Soviet Union (Eastern Bloc)"],
                        "rows": [
                            ["Economic System", "Capitalism / Free Market / Private Enterprise", "State Socialism / Command Economy / Collectivism"],
                            ["Political System", "Multi-party Democracy / Individual Civil Liberties", "One-Party Communist Rule / Authoritarian State"],
                            ["Military Alliance", "NATO (North Atlantic Treaty Organization, 1949)", "Warsaw Pact (1955)"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "The Division of Germany and the Iron Curtain",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "A Continent Split in Two",
                    "content": {
                        "text": (
                            "At the wartime conferences of Yalta and Potsdam (1945), the Allies agreed to divide Germany and its capital, Berlin, "
                            "into four military occupation zones (American, British, French, and Soviet).\n\n"
                            "**The Permanent Division:**\n"
                            "- **West Germany (Federal Republic of Germany - FRG):** Formed in 1949 by merging American, British, and French zones as a capitalist democracy.\n"
                            "- **East Germany (German Democratic Republic - GDR):** Formed in 1949 under Soviet control as a communist satellite state.\n"
                            "- **The Iron Curtain:** Winston Churchill declared in 1946: *'From Stettin in the Baltic to Trieste in the Adriatic, an iron curtain has descended across the Continent.'*"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "The Outbreak of the Cold War (1947–1991)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Ideological Warfare and the Nuclear Arms Race",
                    "content": {
                        "text": (
                            "The **Cold War** was a state of intense ideological, geopolitical, and economic hostility between the US and the USSR "
                            "that stopped short of direct military combat between their armed forces.\n\n"
                            "**Hallmarks of the Cold War:**\n"
                            "- **The Nuclear Arms Race:** Both superpowers built stockpiles of thousands of intercontinental ballistic missiles (ICBMs) and hydrogen bombs, creating the doctrine of Mutually Assured Destruction (MAD).\n"
                            "- **Proxy Wars:** Fighting through third-party conflicts in Korea (1950–1953), Vietnam (1955–1975), and the Middle East.\n"
                            "- **Espionage and Propaganda:** Spy networks (CIA vs KGB), space exploration race, and political subversion."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Acceleration of African Nationalism & Decolonisation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "WWII as the Catalyst for Kenyan Independence",
                    "content": {
                        "text": (
                            "World War II was the decisive turning point for African liberation movements:\n\n"
                            "1. **Demystification of the White Man:** Over **75,000 Kenyan soldiers** in the King's African Rifles fought in Burma, India, Ethiopia, and Madagascar. They saw Europeans panicking, weeping, dying, and retreating, proving they possessed no innate superiority.\n\n"
                            "2. **Military and Leadership Skills:** Returning veterans (such as Bildad Kaggia, Waruhiu Itote / General China) brought back expert knowledge of firearms, communications, and military tactics, which they directly utilized in the **Mau Mau freedom struggle**.\n\n"
                            "3. **The Atlantic Charter (1941):** Signed by Roosevelt and Churchill, Article 3 stated that all peoples have the right to choose their own sovereign government. African nationalists used this declaration to demand self-determination.\n\n"
                            "4. **Weakened European Imperial Powers:** Britain and France were economically bankrupt and could no longer afford the financial cost of maintaining vast colonial garrisons."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Founding of the United Nations Organization (UNO)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "24 October 1945: A New Hope for Humanity",
                    "content": {
                        "text": (
                            "Learning from the tragic collapse of the League of Nations, Allied leaders established a stronger, more universal peace body.\n\n"
                            "On **24 October 1945**, representatives of 50 nations meeting in San Francisco formally ratified the **United Nations Charter**.\n\n"
                            "**Why the UN Succeeded Where the League Failed:**\n"
                            "- **Universal Superpower Membership:** Both the United States and the Soviet Union were founding permanent members.\n"
                            "- **Enforcement Mechanism:** The UN Security Council was empowered to authorize international peacekeeping forces and military action to repel aggression.\n"
                            "- **Comprehensive Specialized Agencies:** Established WHO, UNESCO, UNICEF, FAO, UNHCR, and the World Bank to address root causes of war (poverty, disease, hunger)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Evidence Interpretation Activity: The Berlin Wall",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "The Berlin Wall physically dividing the city, 1961",
                    "content": {
                        "text": "A segment of the newly erected Berlin Wall in 1961, separating Soviet-backed East Berlin from democratic West Berlin.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Berlin_Wall_1961-11-20.jpg",
                        "author": "National Archives and Records Administration / Public Domain",
                        "licensing": "Public Domain",
                        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Berlin_Wall_1961-11-20.jpg"
                    }
                },
                {
                    "block_type": "suggested_video",
                    "component_type": "suggested_video",
                    "title": "Historical Documentary: The Construction and Fall of the Berlin Wall (1961–1989)",
                    "content": {
                        "url": "https://www.youtube.com/watch?v=A9fQPzZ1-hg",
                        "text": "TED-Ed animation and history of the rise and fall of the Berlin Wall (1961-1989), explaining the Cold War division of Europe.",
                        "author": "TED-Ed",
                        "licensing": "Standard YouTube License"
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Historical Source Inquiry: The Berlin Wall",
                    "content": {
                        "text": (
                            "**Examine the photograph above:**\n\n"
                            "1. **Source Classification:** Is this photograph a primary or secondary source of historical information?\n"
                            "*(Answer: Primary source—it is direct visual photographic evidence captured in November 1961 during the physical construction of the wall.)*\n\n"
                            "2. **Historical Meaning:** What political result of World War II does this wall physically represent?\n"
                            "*(Answer: The ideological division of Germany and the Cold War confrontation between the capitalist West and communist East.)*\n\n"
                            "3. **Historical Limitations:** What does this visual tell us about the Cold War, and what can it NOT tell us?\n"
                            "*(Answer: It shows the physical barrier and military division, but cannot show the private political conversations inside the Kremlin or White House.)*"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Interactive Task: Categorizing the Results of WWII",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Classify the Global Results of World War II",
                    "content": {
                        "instruction": "Test your mastery by sorting each result into its correct analytical category:",
                        "items": [
                            "1. Deaths of over 60 million people and the Holocaust -> **Social / Demographic**",
                            "2. Division of Germany into East and West states -> **Political / Geopolitical**",
                            "3. Founding of the European Economic Community (EEC) in 1957 -> **Economic**",
                            "4. Armed Mau Mau uprising led by returning KAR veterans in Kenya -> **Decolonisation / African Nationalism**",
                            "5. Creation of the United Nations Organization on 24 October 1945 -> **International Institutional**",
                            "6. Nuclear arms race and Cold War proxy conflicts -> **Geopolitical / Military**"
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "KCSE Examination Coaching & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Question: Explain Five Political Results of the Second World War (10 Marks)",
                    "content": {
                        "text": (
                            "**Model Answer Structure (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                            "1. **Rise of the USA and USSR as Superpowers:** The pre-war European balance of power was destroyed, leaving the United States and the Soviet Union as the two dominant opposing superpowers. (2 marks)\n\n"
                            "2. **The Division of Germany and Europe:** Germany was split into democratic West Germany and communist East Germany, while Europe was divided by the 'Iron Curtain'. (2 marks)\n\n"
                            "3. **Outbreak of the Cold War:** The ideological hostility between Western capitalism and Soviet communism led to an intense nuclear arms race and global proxy conflicts. (2 marks)\n\n"
                            "4. **Acceleration of African and Asian Decolonisation:** Bankrupt European powers could no longer resist nationalist struggles, leading to independence for India, Ghana, and Kenya. (2 marks)\n\n"
                            "5. **Founding of the United Nations Organization (UNO):** Established on 24 October 1945 to succeed the failed League of Nations and preserve international peace. (2 marks)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 12,
            "page_title": "Topic 1 Comprehensive Mastery Checklist",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Form 4 History Topic 1: The World War Syllabus Checklist",
                    "content": {
                        "text": (
                            "Ensure you have mastered every examinable section of Topic 1:\n\n"
                            "✔ **Meaning of Total & Mechanized War**\n"
                            "✔ **Long-Term Causes of WWI (M-A-I-N-E) & Sarajevo Trigger (28 June 1914)**\n"
                            "✔ **Schlieffen Plan & Reasons for Failure**\n"
                            "✔ **Trench Warfare on Western Front, Verdun, Somme**\n"
                            "✔ **Eastern Front, Russian Revolution & Treaty of Brest-Litovsk (1918)**\n"
                            "✔ **War at Sea, Naval Blockade & U-boat Campaigns**\n"
                            "✔ **African Theatre: Lettow-Vorbeck & Carrier Corps Sacrifice in Kenya**\n"
                            "✔ **US Entry (1917) & Reasons for Allied Victory (1918)**\n"
                            "✔ **Results of WWI (Demographic, Economic, Political, Colonial, Technological)**\n"
                            "✔ **Big Four, Wilson’s 14 Points & Terms of Versailles Treaty (1919)**\n"
                            "✔ **League of Nations: Aims, Structure, Achievements, and Failure Reasons**\n"
                            "✔ **Causes of WWII: Versailles Legacy, Dictators, Great Depression, Appeasement**\n"
                            "✔ **Course of WWII: Blitzkrieg, Battle of Britain, Stalingrad, El Alamein, D-Day, Hiroshima**\n"
                            "✔ **Results of WWII: Superpowers, Cold War, Decolonisation, and Founding of the UN**"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 13,
            "page_title": "Final Knowledge Check: Results of WWII & UN",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Module 1.7 Mastery Check",
                    "content": {
                        "question": "On what date was the United Nations Charter officially ratified, celebrated annually as United Nations Day?",
                        "options": [
                            "A) 28 June 1919",
                            "B) 11 November 1918",
                            "C) 24 October 1945",
                            "D) 8 May 1945"
                        ],
                        "correct_answer": "C",
                        "explanation": "The United Nations Organization (UNO) officially came into existence on 24 October 1945 following the ratification of the UN Charter by the five permanent members and a majority of signatory nations."
                    }
                }
            ]
        },
        {
            "page_number": 14,
            "page_title": "Topic 1 Complete: Transition to International Relations",
            "blocks": [
                {
                    "block_type": "transition",
                    "component_type": "transition",
                    "title": "Looking Ahead to Topic 2: International Relations",
                    "content": {
                        "text": (
                            "Congratulations! You have completed **Topic 1: The World War**.\n\n"
                            "In **Topic 2: International Relations**, you will delve deeper into how post-war nations cooperate and manage conflict through "
                            "the **United Nations**, the **Commonwealth of Nations**, the **Non-Aligned Movement (NAM)**, and the evolving dynamics of the **Cold War**."
                        )
                    }
                },
                {
                    "block_type": "key_takeaway",
                    "component_type": "key_takeaway",
                    "title": "Final Thought on Topic 1",
                    "content": {
                        "text": "The two World Wars proved that unmanaged imperial rivalry and militarism lead to total devastation. Understanding this history is vital for analyzing modern international relations, peacekeeping, and Kenya's constitutional journey."
                    }
                }
            ]
        }
    ]
}

ALL_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA,
    LESSON_6_DATA,
    LESSON_7_DATA
]


def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 1 (THE WORLD WAR)")
    print("=" * 80)

    with transaction.atomic():
        curriculum = Curriculum.objects.filter(name="844").first()
        if not curriculum:
            curriculum = Curriculum.objects.create(name="844", description="8-4-4 Kenyan National Curriculum")
            print(f"[+] Created Curriculum: {curriculum.name}")
        else:
            print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

        grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
        if not grade:
            grade = Grade.objects.create(curriculum=curriculum, name="Form 4", level=4)
            print(f"[+] Created Grade: {grade.name}")
        else:
            print(f"[*] Found Grade: {grade.name} (ID: {grade.id})")

        subject = Subject.objects.filter(grade=grade, name="History").first()
        if not subject:
            subject = Subject.objects.create(
                grade=grade,
                name="History",
                description="Form 4 History and Government under the 8-4-4 Kenyan Curriculum"
            )
            print(f"[+] Created Subject: {subject.name}")
        else:
            print(f"[*] Found Subject: {subject.name} (ID: {subject.id})")

        topic_name = "The World War"
        topic = Topic.objects.filter(subject=subject, name=topic_name).first()
        if not topic:
            topic = Topic.objects.create(
                subject=subject,
                name=topic_name,
                order=1,
                description=(
                    "Comprehensive Form 4 curriculum unit covering World War I (1914–1918), the Paris Peace Settlement, "
                    "the League of Nations, World War II (1939–1945), and the rise of the United Nations."
                )
            )
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 1
            topic.description = (
                "Comprehensive Form 4 curriculum unit covering World War I (1914–1918), the Paris Peace Settlement, "
                "the League of Nations, World War II (1939–1945), and the rise of the United Nations."
            )
            topic.save()
            print(f"[*] Found Existing Topic: {topic.name} (ID: {topic.id})")

        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for lesson_spec in ALL_LESSONS:
            unit_order = lesson_spec["unit_order"]
            unit_name = lesson_spec["unit_name"]
            lesson_title = lesson_spec["lesson_title"]
            pages = lesson_spec["pages"]

            unit = LearningUnit.objects.filter(topic=topic, order=unit_order).first()
            if not unit:
                unit = LearningUnit.objects.create(
                    topic=topic,
                    name=unit_name,
                    order=unit_order,
                    description=f"Form 4 History Learning Unit {unit_order}: {unit_name}"
                )
                print(f"\n[+] Created Learning Unit {unit_order}: {unit.name} (ID: {unit.id})")
            else:
                unit.name = unit_name
                unit.save()
                print(f"\n[*] Found Existing Learning Unit {unit_order}: {unit.name} (ID: {unit.id})")

            lesson = Lesson.objects.filter(learning_unit=unit).first()
            if not lesson:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
                print(f"  [+] Created Lesson: {lesson.title} (ID: {lesson.id})")
            else:
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.save()
                print(f"  [*] Found Existing Lesson: {lesson.title} (ID: {lesson.id})")

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
        print(f"[SUCCESS] Form 4 History Topic 1 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 1")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
