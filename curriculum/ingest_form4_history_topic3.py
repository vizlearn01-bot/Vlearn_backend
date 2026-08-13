"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 3 (Co-operation in Africa)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 3: Co-operation in Africa (Order: 3)
  - Unit 1: Pan-Africanism — Origin, Causes, and Early Development (Pre-1945) (Lesson 1: 15 Pages)
  - Unit 2: The Manchester Congress (1945) and Movement on African Soil (Lesson 2: 15 Pages)
  - Unit 3: The Organisation of African Unity (OAU) — Formation, Charter, and Performance (Lesson 3: 16 Pages)
  - Unit 4: The African Union (AU) — Rebirth, Structure, and Challenges (Lesson 4: 16 Pages)
  - Unit 5: The East African Community (EAC) — 1967 and 2001 Rebirth (Lesson 5: 18 Pages)
  - Unit 6: The Economic Community of West African States (ECOWAS) (Lesson 6: 15 Pages)
  - Unit 7: The Common Market for Eastern and Southern Africa (COMESA) and Continental Integration (Lesson 7: 18 Pages)

Total: 7 Learning Units, 7 Lessons, 113 Pages, 130+ Blocks, 14 Media Assets (7 Wikimedia Photos + 7 Verified YouTube Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic3.py --replace
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
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 3
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "Introduction to Pan-Africanism",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Pan-Africanism in the Diaspora",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define Pan-Africanism and understand its philosophical origin in the African diaspora\n"
                        "- Analyze the six fundamental root causes that birthed the Pan-African movement\n"
                        "- Evaluate the individual contributions of pioneer leaders (Marcus Garvey, Booker T. Washington, W.E.B. Du Bois)\n"
                        "- Trace the five early diaspora Pan-African Congresses (1900–1927)\n"
                        "- Explain the nine specific barriers that prevented Pan-Africanism from taking root on African soil before 1945"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: Pan-Africanism",
                "content": {
                    "term": "Pan-Africanism",
                    "definition": (
                        "A political, social, and cultural movement based on the belief in the uniqueness and spiritual unity of Black people worldwide, "
                        "acknowledging their shared origin and destiny, and asserting their right to self-determination, racial dignity, and freedom from colonial and racist oppression."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Pioneer Profile: Marcus Garvey and the UNIA",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Marcus Garvey in UNIA Ceremonial Uniform (1924)",
                "content": {
                    "text": "Marcus Garvey wearing the ceremonial uniform of the Universal Negro Improvement Association (UNIA) in New York, reflecting his title as the 'Provisional President of Africa'.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Marcus_Garvey_1924-08-05.jpg",
                    "author": "George Grantham Bain Collection / Library of Congress / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Marcus_Garvey_1924-08-05.jpg"
                }
            },
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Marcus Garvey (1887–1940): The Apostle of Black Pride",
                "content": {
                    "text": (
                        "- **Background:** Born in Jamaica as a descendant of freed slaves. His dark complexion exposed him to intense racism, shaping his lifelong conviction that Black people must take uncompromising pride in their blackness and African heritage.\n"
                        "- **The UNIA (1914):** Founded the Universal Negro Improvement Association (UNIA) in Jamaica and later expanded it in Harlem, New York, aiming to unite all peoples of African descent into a single worldwide brotherhood.\n"
                        "- **The 'Back to Africa' Movement:** Advocated for the physical repatriation of African Americans to Africa (specifically Liberia), urging them to build an independent, prosperous African empire.\n"
                        "- **Economic Self-Reliance:** Believed true liberation required financial independence. He established the **Black Star Line Shipping Company** funded by African American investments to facilitate global Black commerce.\n"
                        "- **Cultural Impact:** Published the widely read newspaper *The Negro World* and founded the African Orthodox Church featuring a Black Patriarch and a Black Madonna as powerful symbols of spiritual decolonization."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Origins in the Diaspora: The Trans-Atlantic Slave Trade",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Why Pan-Africanism Began in the Americas",
                "content": {
                    "text": (
                        "The roots of Pan-Africanism did not originate on the African continent itself, but in the New World (the Americas and the Caribbean) during the 19th Century:\n\n"
                        "- **Shared Trauma of Plantation Slavery:** Between the 15th and 19th centuries, millions of Africans were forcibly captured and transported across the Atlantic. The collective misery, humiliation, and brutality of plantation slavery created a profound racial consciousness among descendants of enslaved people.\n"
                        "- **Yearning for Africa as 'Home':** Dispersed diaspora communities looked back toward Africa as a sacred motherland, viewing continental freedom as essential to their own liberation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Six Root Causes of Pan-Africanism",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Causes of the Rise of Pan-Africanism",
                "content": {
                    "steps": [
                        "1. The Trans-Atlantic Slave Trade: Shared trauma and dispersion created a deep consciousness of common racial origin and shared destiny among Black people in the diaspora.",
                        "2. Imperial Colonization of Africa: The 1884–1885 Berlin Conference partitioned the continent, subjecting Africans to forced labor, land alienation, hut taxation, and political subjugation.",
                        "3. Countering the Myth of European Superiority: European racists promoted pseudo-scientific theories claiming Black people were inferior; Pan-Africanism arose to prove Africans possessed rich, civilized cultures.",
                        "4. Racial Discrimination and Jim Crow Segregation: Across the US South and in white-settler colonies (Kenya, South Africa), Black people were denied voting rights, dispossessed of land, and segregated.",
                        "5. The Rise of an Educated Black Elite: University-educated Black intellectuals in the diaspora and early African scholars abroad provided leadership and organizational skill to articulate grievances.",
                        "6. Discrimination by European Missionaries: White missionaries condemned African traditions and denied Black clergy leadership, prompting the rise of Independent African Churches that preached national liberation."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Pioneer Profile: Booker T. Washington",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Booker T. Washington (1856–1915): Practical Education and Accommodation",
                "content": {
                    "text": (
                        "- **Background:** Born into slavery in Virginia, USA, he later earned a university degree in agriculture.\n"
                        "- **Industrial and Vocational Education:** Strongly argued that Black people must first achieve economic self-reliance through practical, vocational skills (carpentry, farming, mechanics) before demanding political equality.\n"
                        "- **The Tuskegee Institute:** Founded the famous Tuskegee Normal and Industrial Institute in Alabama to train thousands of Black students in technical crafts and agriculture.\n"
                        "- **The Policy of Accommodation:** Adopted a moderate, non-confrontational approach with white authorities, securing philanthropic funding from white industrialists like Andrew Carnegie to finance Black enterprises (e.g., National Negro Business League)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Historical Documentary: Marcus Garvey & the UNIA",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The Story of Marcus Garvey and the UNIA",
                "content": {
                    "url": "https://www.youtube.com/watch?v=bpsKWGIZIhw",
                    "text": "Explore the life and philosophy of Marcus Garvey, the mass mobilization of the Universal Negro Improvement Association (UNIA), and the Black Star Line.",
                    "author": "IBW21st / Historical Archives",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Pioneer Profile: Dr. W.E.B. Du Bois",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Dr. William Edward Burghardt (W.E.B.) Du Bois (1868–1963)",
                "content": {
                    "text": (
                        "- **Background:** Born in Massachusetts, Du Bois was the first African American to earn a PhD from Harvard University, becoming a world-renowned professor of Sociology, History, and Economics.\n"
                        "- **Radical Civil Rights Advocacy:** Strongly rejected Booker T. Washington's 'policy of accommodation', asserting that Black people must demand immediate, full civil and political equality.\n"
                        "- **The NAACP (1910):** Founded the Niagara Movement (1905) and co-founded the **National Association for the Advancement of Colored People (NAACP)** in 1910, leading the legal fight against lynching and segregation.\n"
                        "- **Father of Pan-African Congresses:** Organized and presided over the first four Pan-African Congresses (1919–1927), drafting petitions against colonial land alienation.\n"
                        "- **Relocation to Africa:** In 1961, at the invitation of President Kwame Nkrumah, Du Bois moved to Ghana, became a Ghanaian citizen, and passed away in Accra in 1963."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Dr. W.E.B. Du Bois Portrait",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Dr. W.E.B. Du Bois Portrait (1907)",
                "content": {
                    "text": "Dr. W.E.B. Du Bois, intellectual pioneer of Pan-Africanism, founder of the NAACP, and organizer of the historic Pan-African Congresses.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/W.E.B._Du_Bois_by_James_E._Purdy%2C_1907.jpg",
                    "author": "James E. Purdy / Library of Congress / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:W.E.B._Du_Bois_by_James_E._Purdy,_1907.jpg"
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Supporting Diaspora and African Pioneers",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Other Influential Early Pan-African Figures",
                "content": {
                    "headers": ["Pioneer Leader", "Origin / Base", "Core Contribution to Pan-Africanism"],
                    "rows": [
                        ["Henry Sylvester Williams", "Trinidad", "Brilliant lawyer who sponsored the first Pan-African Conference in London (1900) and formally coined the term 'Pan-Africanism'."],
                        ["George Padmore", "Trinidad", "Influential journalist and author who became the leading organizational strategist of Pan-Africanism after 1945, mentoring African nationalist leaders."],
                        ["Dr. J.E. Kwegyir Aggrey", "Ghana", "Celebrated African educationist who toured Africa and the USA lecturing on racial harmony, Black intellectual ability, and higher education."],
                        ["Edward Wilmot Blyden", "Liberia / St. Thomas", "Early 19th-century intellectual who wrote extensively proving that African cultures and civilizations had contributed richly to world history."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The Early Pan-African Congresses (1900–1927)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "The Five Early Diaspora Congresses",
                "content": {
                    "headers": ["Congress & Year", "Venue", "Key Organizers", "Core Resolutions & Impact"],
                    "rows": [
                        ["First Conference (1900)", "Westminster Town Hall, London", "Henry Sylvester Williams, W.E.B. Du Bois (32 delegates)", "Formally coined the term 'Pan-Africanism'; petitioned Queen Victoria against colonial land grabs in South Africa; Du Bois declared: 'The problem of the 20th Century is the problem of the color line.'"],
                        ["Second Congress (1919)", "Grand Hotel, Paris", "W.E.B. Du Bois & NAACP delegates", "Held during Paris Peace Conference; presented memorandum urging Allies to hold African land in trust, abolish forced labor, and grant educational rights."],
                        ["Third Congress (1921)", "London, Brussels, Paris", "W.E.B. Du Bois (112 delegates)", "Demanded political representation for Black people; exposed Belgian colonial atrocities in the Congo."],
                        ["Fourth Congress (1923)", "London and Lisbon", "W.E.B. Du Bois", "Demanded that colonial governments grant direct African representation in legislative councils and respect indigenous land titles."],
                        ["Fifth Congress (1927)", "New York City, USA", "W.E.B. Du Bois (mostly African Americans)", "Warned against Soviet communist infiltration of Black civil rights organizations; marked the end of the diaspora-dominated phase."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Why Was Pan-Africanism Slow to Establish on African Soil Before 1945?",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Nine Barriers Preventing Pan-Africanism in Africa (Pre-1945)",
                "content": {
                    "steps": [
                        "1. Hostility of Colonial Authorities: Imperial powers banned anti-colonial publications, outlawed cross-border political parties, and jailed activists.",
                        "2. Divide and Rule Policy: Colonial governments restricted travel and communication between neighboring colonies (e.g., between British Kenya and French West Africa).",
                        "3. Low Levels of Western Literacy: Widespread illiteracy meant rural Africans were unaware of international Pan-African developments in America and Europe.",
                        "4. Extreme Poverty: Colonial taxation and land expropriation left Africans without financial resources to fund political travel or purchase literature.",
                        "5. Preoccupation with Pressing Local Grievances: Africans were consumed by daily survival against immediate colonial burdens (Kipande pass laws, forced labor, land alienation).",
                        "6. Lack of a Suitable Independent Venue: The entire continent was colonized (except Ethiopia and Liberia), leaving no safe sovereign territory to host international conferences.",
                        "7. Weakness of Independent States: Ethiopia was recovering from Menelik II's succession and 1935 Italian invasion, while Liberia was heavily dependent on the USA.",
                        "8. The French Assimilation Policy: The educated elite in French colonies (évolués) were granted French citizenship, striving to become 'Black Frenchmen' rather than Pan-Africanists.",
                        "9. Lack of Communication Infrastructure: Zero trans-continental roads, railways, or telecommunications connected Anglophone, Francophone, and Lusophone territories."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Interactive Classification: Pioneer Philosophies",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Pioneer to Their Philosophy and Achievement",
                "content": {
                    "instruction": "Test your mastery of early Pan-African leaders. Match each pioneer to their key accomplishment:",
                    "items": [
                        "1. Founded the UNIA and championed the 'Back to Africa' movement -> **Marcus Garvey**",
                        "2. First Black Harvard PhD, co-founded NAACP, father of Pan-African Congresses -> **Dr. W.E.B. Du Bois**",
                        "3. Founded the Tuskegee Institute and promoted industrial/vocational education -> **Booker T. Washington**",
                        "4. Sponsored the 1900 London Conference and coined the term 'Pan-Africanism' -> **Henry Sylvester Williams**",
                        "5. Wrote extensively proving ancient African cultures were civilized -> **Edward Wilmot Blyden**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "KCSE Examination Coaching: Barriers on African Soil",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Reasons Why the Pan-African Movement was Slow to Establish Itself on African Soil Before 1945 (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Colonial Repression and Hostility:** European colonial administrations outlawed nationalist associations and censored foreign publications, arresting or deporting anyone advocating Pan-African unity. (2 marks)\n\n"
                        "2. **The Divide and Rule Policy:** Colonial authorities restricted cross-border travel and communication between colonies, keeping African ethnic groups isolated from one another. (2 marks)\n\n"
                        "3. **Preoccupation with Local Grievances:** Africans were consumed by daily struggles against immediate oppressive policies—such as land alienation, the Kipande system, and forced labor—rather than global solidarity. (2 marks)\n\n"
                        "4. **Lack of Independent Venues:** Since virtually the entire continent was colonized, there was no safe sovereign African nation capable of hosting international Pan-African summits. (2 marks)\n\n"
                        "5. **The French Policy of Assimilation:** In French West Africa, the educated elite were granted French citizenship, blinding them into identifying with France rather than with African liberation. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Check Your Understanding: Module 3.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 3.1 Mastery Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which pioneer Pan-Africanist founded the Universal Negro Improvement Association (UNIA) and the Black Star Line?",
                            "options": [
                                "Booker T. Washington",
                                "Marcus Garvey",
                                "W.E.B. Du Bois",
                                "Henry Sylvester Williams"
                            ],
                            "correct_answer": 1,
                            "explanation": "Marcus Garvey founded the UNIA in 1914 and the Black Star Line to economically empower the Black race."
                        },
                        {
                            "question": "In which city was the landmark 1900 Pan-African Conference held where the term 'Pan-Africanism' was formally coined?",
                            "options": [
                                "Paris, France",
                                "London, United Kingdom",
                                "New York, USA",
                                "Accra, Ghana"
                            ],
                            "correct_answer": 1,
                            "explanation": "The 1900 conference was held at Westminster Town Hall in London, sponsored by Henry Sylvester Williams."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Pan-Africanism in the Diaspora",
                "content": {
                    "text": (
                        "• **Origins:** Birthed in the diaspora (Americas/Caribbean) through the shared trauma of the Trans-Atlantic slave trade and racial oppression.\n"
                        "• **Key Pioneers:** Marcus Garvey (UNIA, Black pride), Booker T. Washington (Tuskegee vocational education), W.E.B. Du Bois (NAACP, Congress leader), Henry Sylvester Williams (coined term in 1900).\n"
                        "• **Early Congresses (1900–1927):** Dominated by diaspora intellectuals lobbying Western powers for civil rights and colonial land protection.\n"
                        "• **Pre-1945 African Barriers:** Colonial divide-and-rule, lack of sovereign host venues, illiteracy, extreme poverty, and local grievance preoccupation."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Before 1945, Pan-Africanism was primarily an intellectual protest movement in the diaspora.\n"
                        "- It laid the philosophical foundation that transformed into mass African nationalism after World War II."
                    )
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Manchester Congress (1945): The Great Turning Point",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Return of Pan-Africanism to Africa",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Analyze why the 1945 Manchester Congress is regarded as the great turning point in African history\n"
                        "- Identify the prominent African nationalist leaders who organized the Manchester Congress\n"
                        "- Explain the five key factors that accelerated Pan-Africanism on African soil post-1945\n"
                        "- Distinguish between the three competing ideological blocs (Casablanca, Monrovia, Brazzaville)\n"
                        "- Evaluate the achievements and challenges of the Pan-African movement"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Great Turning Point (1945)",
                "content": {
                    "term": "The Manchester Turning Point",
                    "definition": (
                        "The Fifth (technically Sixth) Pan-African Congress held in Manchester, England, in October 1945, which marked the historic transformation "
                        "of Pan-Africanism from a diaspora-led intellectual protest movement into a radical, mass-based liberation movement led by Africans themselves to win immediate independence."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Why Was the Manchester Congress Unique?",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Diaspora Phase (Pre-1945) vs. Manchester Congress (1945)",
                "content": {
                    "headers": ["Feature", "Pre-1945 Diaspora Congresses", "The 1945 Manchester Congress"],
                    "rows": [
                        ["Leadership", "Dominated by African American and West Indian intellectuals (Du Bois, Garvey).", "Dominated by African leaders from the continent (Jomo Kenyatta, Kwame Nkrumah, Kamuzu Banda)."],
                        ["Class Representation", "Elite professionals, lawyers, and academics.", "Broad mass representation including African trade unionists, farmers' cooperatives, and student bodies."],
                        ["Funding & Organization", "Funded and attended by sympathetic white liberals and philanthropists.", "Entirely organized, financed, and directed by Black delegates without white patron influence."],
                        ["Tone of Demands", "Moderate petitions and appeals to colonial powers for better treatment.", "Radical, uncompromising demands for immediate, unconditional political independence from colonial rule."],
                        ["Strategic Method", "Academic lobbying and moral persuasion.", "Direct mass action: strikes, boycotts, trade union agitation, and civil non-cooperation."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Core Resolutions of the Manchester Congress",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Resolutions Passed at Manchester (October 1945)",
                "content": {
                    "steps": [
                        "1. Absolute Demand for Independence: Declared that colonial peoples must actively organize to win political power through strikes, boycotts, and civil non-cooperation.",
                        "2. Mass Mobilization: Urged African intellectuals to return home immediately and mobilize the rural peasants and urban working class into mass nationalist parties.",
                        "3. Establishment of Regional Federations: Recommended creating regional bodies to coordinate anti-colonial struggles across borders.",
                        "4. Formation of WANS: Pursuant to this, Kwame Nkrumah founded the West African National Secretariat (WANS) in London (Dec 1945) to coordinate West African liberation."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Pioneer Profile: Kwame Nkrumah of Ghana",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Kwame Nkrumah, First President of Ghana",
                "content": {
                    "text": "Dr. Kwame Nkrumah, champion of Pan-Africanism, organizer of the 1945 Manchester Congress, and first President of independent Ghana (1957).",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Kwame_Nkrumah_%28JFKWHP-AR6409-A%29.jpg",
                    "author": "White House / US National Archives / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kwame_Nkrumah_(JFKWHP-AR6409-A).jpg"
                }
            },
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Kwame Nkrumah: The Architect of Continental Unity",
                "content": {
                    "text": (
                        "- **Return to Africa:** Returning to the Gold Coast in 1947, Nkrumah founded the Convention People's Party (CPP), mobilizing the masses with the slogan *'Self-Government NOW!'*.\n"
                        "- **Independence of Ghana (6 March 1957):** Ghana became the first sub-Saharan colony to attain independence, providing a secure sovereign base to host Pan-African conferences and fund liberation fighters.\n"
                        "- **Historic Declaration:** Nkrumah proclaimed:\n"
                        "  > *'The independence of Ghana is meaningless unless it is linked up with the total liberation of the African continent.'*"
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Five Factors Accelerating Pan-Africanism Post-1945",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Why Pan-Africanism Activated in Africa After 1945",
                "content": {
                    "steps": [
                        "1. Return of World War II Veterans: Thousands of African ex-soldiers returned from Europe and Asia having fought alongside white soldiers, destroying the myth of white invincibility.",
                        "2. Inspiration from Asian Decolonization: The independence of India and Pakistan in 1947 proved European empires could be defeated, boosting African national confidence.",
                        "3. United Nations Charter: The 1945 UN Charter explicitly championed universal self-determination and human rights, giving international legal backing to anti-colonialism.",
                        "4. Superpower Anti-Colonial Pressure: The USA (seeking open trade markets) and USSR (opposing capitalist empires) pressured Britain and France to dismantle their empires.",
                        "5. Ghana's Independence (1957): Provided a sovereign African territory with resources and diplomatic backing to fund liberation movements across the continent."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Historical Documentary: Kwame Nkrumah's 1957 Address",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Archival Footage: Kwame Nkrumah Independence Day Address (1957)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=hYgyk7kMBSk",
                    "text": "Watch authentic archival newsreel footage of Kwame Nkrumah declaring Ghana's independence in Accra in March 1957, igniting the total decolonization of Africa.",
                    "author": "Historia Africana / Archival Newsreels",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Early Conferences on African Soil: Accra 1958",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Bringing the Movement Home: The Accra Summits (1958)",
                "content": {
                    "text": (
                        "To implement the Manchester resolutions, Kwame Nkrumah convened two historic summits in Accra, Ghana, in 1958:\n\n"
                        "1. **The First Conference of Independent African States (April 1958):**\n"
                        "   - Attended by the only eight independent African states at the time: Ghana, Egypt, Ethiopia, Liberia, Morocco, Tunisia, Sudan, and Libya.\n"
                        "   - Pledged collective material, diplomatic, and financial support to territories still under colonial rule.\n\n"
                        "2. **The All-African Peoples Conference (December 1958):**\n"
                        "   - Chaired by Kenya's young trade unionist **Tom Mboya**, uniting freedom fighters and nationalist leaders from across the colonized continent (including Patrice Lumumba of Congo).\n"
                        "   - Resolved to use 'all means necessary'—including armed guerrilla warfare—to overthrow colonialism, setting the goal of a future *United States of Africa*."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Ideological Splits: The Three Competing Blocs",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "How African Leaders Divided on Continental Unity",
                "content": {
                    "text": (
                        "As dozens of colonies gained independence in the early 1960s, sharp ideological differences emerged regarding the speed and structure of African unity, creating three rival factions:\n\n"
                        "1. **The Brazzaville Group (December 1960):** Comprised 12 Francophone, conservative states. Favored maintaining economic and political ties with France and strongly opposed interfering in the domestic affairs of other states.\n\n"
                        "2. **The Casablanca Group (January 1961):** Radical, militant states led by Kwame Nkrumah (Ghana), Guinea, Mali, Egypt, and Morocco. Demanded immediate political unification under a single continental government, an African High Military Command, and the removal of Western military bases.\n\n"
                        "3. **The Monrovia Group (May 1961):** Moderates led by Nigeria, Liberia, and Senegal who rejected instant political union. Favored gradual unity through economic cooperation while strictly respecting national state sovereignty."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Comparative Analysis: The Three Pre-OAU Blocs",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Comparison of Pre-OAU Factional Blocs (1960–1962)",
                "content": {
                    "headers": ["Bloc Name", "Key Member States", "Ideological Stance", "Vision for African Unity"],
                    "rows": [
                        ["Casablanca Group (Radicals)", "Ghana, Egypt, Guinea, Mali, Morocco, Algerian FLN", "Socialist, anti-imperialist, revolutionary", "Immediate political union under a United States of Africa and a joint continental army."],
                        ["Monrovia Group (Moderates)", "Nigeria, Liberia, Senegal, Sierra Leone, Ethiopia", "Democratic, pro-Western, pragmatic", "Gradual economic integration first, with absolute respect for national sovereignty and borders."],
                        ["Brazzaville Group (Conservatives)", "Ivory Coast, Senegal, Cameroon, Gabon, Chad (12 Francophone states)", "Pro-French, conservative, anti-communist", "Preserve close economic and military ties with France; oppose all political integration."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The 1963 Compromise at Addis Ababa",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Dissolving Factions to Form a Single Continental Body",
                "content": {
                    "text": (
                        "By 1963, African statesmen recognized that division would destroy their collective leverage against remaining colonial regimes.\n\n"
                        "- Through intensive diplomatic shuttle diplomacy led by Emperor Haile Selassie of Ethiopia and President Sékou Touré of Guinea, the three factions agreed to meet in Addis Ababa in May 1963.\n"
                        "- **The Historic Compromise:** Radicals agreed to drop their demand for instant political union, while moderates agreed to create a formal permanent continental organization.\n"
                        "- All three factions formally dissolved themselves upon signing the **Charter of the Organisation of African Unity (OAU) on 25 May 1963**."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Achievements of the Pan-African Movement",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Major Achievements of Pan-Africanism",
                "content": {
                    "steps": [
                        "1. Accelerated Continental Decolonization: Mobilized global public opinion, trade unions, and mass nationalist parties, speeding political independence.",
                        "2. Laid Foundation for Continental Unity: Directly inspired the founding of the Organisation of African Unity (1963) and the African Union (2002).",
                        "3. Restored Black Dignity and Cultural Pride: Systematically dismantled racist myths of white superiority, inspiring global Black self-esteem.",
                        "4. Promoted African Studies & Cultural Preservation: Sparked global academic research into pre-colonial African history, traditional medicine, music, and art.",
                        "5. Mobilized International Anti-Apartheid Solidarity: Enabled the Black diaspora (e.g., US Congressional Black Caucus) to lobby for economic sanctions against apartheid South Africa.",
                        "6. Demonstrated Global Solidarity in Crises: Organized massive worldwide Black protests against Mussolini's 1935 invasion of independent Ethiopia."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Challenges Facing the Pan-African Movement",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Critical Challenges Confronting Pan-Africanism",
                "content": {
                    "steps": [
                        "1. Chronic Financial Shortages: Most member states were impoverished developing economies unable to fund secretariats or major joint projects.",
                        "2. Ideological and Factional Splits: Bitter disagreements between radicals (Casablanca) and moderates (Monrovia/Brazzaville) delayed collective decision-making.",
                        "3. Linguistic and Cultural Divides: Imperial partition left behind deep linguistic barriers (Anglophone, Francophone, Lusophone) hindering administration.",
                        "4. Economic Dependency on Former Colonizers (Neo-Colonialism): Newly independent states remained tied to former colonial masters for aid, loans, and trade.",
                        "5. Rampant Illiteracy and Poverty: Widespread illiteracy prevented the rural masses from understanding or participating in Pan-African initiatives.",
                        "6. Hostile Western Media Propaganda: Western media dominated international news, routinely ridiculing or censoring Pan-African achievements."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Interactive Classification: Pre-OAU Blocs",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Assign the Characteristic to the Correct Pre-OAU Bloc",
                "content": {
                    "instruction": "Test your mastery of the early African nationalist factions (Casablanca, Monrovia, or Brazzaville):",
                    "items": [
                        "1. Demanded immediate political unification and a joint continental army -> **Casablanca Group**",
                        "2. Favored maintaining close political, military, and economic links with France -> **Brazzaville Group**",
                        "3. Advocated gradual economic integration while strictly respecting state sovereignty -> **Monrovia Group**",
                        "4. Led by Kwame Nkrumah of Ghana, Sékou Touré of Guinea, and Gamal Abdel Nasser of Egypt -> **Casablanca Group**",
                        "5. Included Nigeria, Liberia, and Senegal seeking a moderate compromise -> **Monrovia Group**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "KCSE Examination Coaching: Achievements of Pan-Africanism",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Achievements of the Pan-African Movement Since 1900 (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Spearheaded Decolonization:** Mobilized mass political consciousness and trade unions, accelerating the attainment of national independence across Africa. (2 marks)\n\n"
                        "2. **Fostered Continental Unity:** Laid the organizational and philosophical groundwork that led directly to the formation of the OAU in 1963 and the African Union in 2002. (2 marks)\n\n"
                        "3. **Restored Black Dignity and Cultural Pride:** Successfully challenged the myth of white supremacy, restoring cultural pride and self-worth to Black people globally. (2 marks)\n\n"
                        "4. **Fostered International Anti-Apartheid Action:** Channeled global Black diaspora support to lobby for economic and diplomatic sanctions against the racist South African regime. (2 marks)\n\n"
                        "5. **Promoted African Cultural and Historical Research:** Inspired global academic research into African history, languages, and art, founding African studies departments worldwide. (2 marks)"
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
                "title": "Module 3.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which young Kenyan trade unionist served as the Chairman of the historic 1958 All-African Peoples Conference in Accra?",
                            "options": [
                                "Jomo Kenyatta",
                                "Tom Mboya",
                                "Oginga Odinga",
                                "Ronald Ngala"
                            ],
                            "correct_answer": 1,
                            "explanation": "Tom Mboya chaired the 1958 All-African Peoples Conference in Accra, bringing together freedom fighters from across Africa."
                        },
                        {
                            "question": "Which pre-OAU faction demanded immediate political unification of Africa under a single continental government?",
                            "options": [
                                "The Brazzaville Group",
                                "The Casablanca Group",
                                "The Monrovia Group",
                                "The London Group"
                            ],
                            "correct_answer": 1,
                            "explanation": "The radical Casablanca Group, led by Kwame Nkrumah, demanded immediate political union and an African military high command."
                        }
                    ]
                }
            },
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Manchester 1945 & Movement on African Soil",
                "content": {
                    "text": (
                        "• **Manchester Congress (1945):** Great turning point; dominated by African leaders (Nkrumah, Kenyatta), trade unions, and radical independence demands.\n"
                        "• **Accra Summits (1958):** Hosted by Nkrumah; All-African Peoples Conference chaired by Tom Mboya.\n"
                        "• **Three Factions:** Casablanca (radicals), Monrovia (moderates), Brazzaville (Francophone conservatives).\n"
                        "• **1963 Compromise:** Factions dissolved in Addis Ababa to establish the OAU on 25 May 1963."
                    )
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Organisation of African Unity (OAU): Formation and Charter",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Organisation of African Unity",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the founding of the OAU in Addis Ababa on 25 May 1963\n"
                        "- Analyze the structure and principles of the 33-Article OAU Charter\n"
                        "- Describe the composition and specific functions of the 4 principal organs of the OAU\n"
                        "- Evaluate the major political and economic achievements of the OAU\n"
                        "- Explain the systemic failures and limitations of the OAU (including non-interference and the 1994 Rwanda Genocide)"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The Organisation of African Unity (OAU)",
                "content": {
                    "term": "Organisation of African Unity (OAU)",
                    "definition": (
                        "The premier continental intergovernmental body established on 25 May 1963 in Addis Ababa, Ethiopia, by 30 independent African states, "
                        "dedicated to promoting continental unity, eradicating all forms of colonialism and apartheid, defending sovereignty, and fostering socio-economic cooperation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "The Historic Addis Ababa Summit (25 May 1963)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Founding of the OAU and Election of Emperor Haile Selassie",
                "content": {
                    "text": (
                        "- **The Summit:** Between 22 and 25 May 1963, 30 out of the 32 independent African states gathered in Addis Ababa, Ethiopia.\n"
                        "- **Signing the Charter:** On **25 May 1963**, heads of state signed the historic OAU Charter (celebrated annually worldwide as *Africa Day*).\n"
                        "- **First Chairperson:** Host leader **Emperor Haile Selassie I of Ethiopia** was elected the first Chairperson of the OAU.\n"
                        "- **Dissolution of Factions:** Upon signing, the pre-existing Casablanca, Monrovia, and Brazzaville blocs were formally dissolved.\n"
                        "- **Kenya's Admission:** Kenya formally joined the OAU in 1964 upon attaining independence."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Emperor Haile Selassie I Portrait",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Emperor Haile Selassie I of Ethiopia",
                "content": {
                    "text": "Emperor Haile Selassie I of Ethiopia, host of the 1963 Addis Ababa Summit and the first Chairperson of the Organisation of African Unity (OAU).",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/d/df/Haile_Selassie_%281942%29.jpg",
                    "author": "Imperial War Museum / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Haile_Selassie_(1942).jpg"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Historical Documentary: The 1963 Founding of the OAU",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Archival Documentary: The Birth of African Unity in Addis Ababa (1963)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=4W-ovu-TOwI",
                    "text": "Watch authentic archival footage of the May 1963 Addis Ababa summit where 30 African heads of state signed the OAU Charter to unite the continent.",
                    "author": "Ethiopian Historical Archives / Educational Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Structure of the OAU Charter (Articles 1–33)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Key Provisions and Principles of the OAU Charter",
                "content": {
                    "text": (
                        "The OAU Charter was modeled on the UN Charter, but with one unique feature: **no member state held veto power**, ensuring absolute sovereign equality.\n\n"
                        "**Core Examinable Articles:**\n"
                        "- **Article 1–2:** Established the name, aims, and universal African membership.\n"
                        "- **Article 3 (Core Principles):**\n"
                        "  1. Sovereign equality of all member states.\n"
                        "  2. Non-interference in the internal domestic affairs of states.\n"
                        "  3. Respect for the sovereignty and territorial integrity of each state.\n"
                        "  4. Peaceful settlement of disputes by negotiation, mediation, or arbitration.\n"
                        "  5. Unreserved condemnation of political assassination and subversive activities.\n"
                        "- **Article 23 (Financial Cap):** Contributions based on an assessed scale; **no member state was allowed to pay more than 20% of the total budget** (to prevent wealthy states from dominating the OAU).\n"
                        "- **Article 32 (Withdrawal Procedure):** Required a **one-year formal written notice** to withdraw."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Principal Organ 1: The Assembly of Heads of State",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Supreme Governing Parliament of the OAU",
                "content": {
                    "text": (
                        "- **Composition:** Composed of all presidents, prime ministers, and monarchs of member states.\n"
                        "- **Role:** The supreme policy-making organ of the OAU.\n"
                        "- **Meetings:** Met once a year in regular session, with extraordinary sessions called in emergencies.\n"
                        "- **Voting:** Each member held **one vote**; resolutions on substantive matters required a **two-thirds majority**.\n"
                        "- **Chairmanship:** Rotated annually among member states, traditionally held by the host nation's leader."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The 1982 Chair Crisis and Kenya's Stabilizing Role",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Deep Dive: The 1982 Tripoli Crisis",
                "content": {
                    "text": (
                        "**The Crisis:** In 1982, Libyan leader **Colonel Muammar Gaddafi** was scheduled to assume the OAU chairmanship in Tripoli. However, moderate leaders boycotted the summit due to Libya's military involvement in Chad, causing the summit to abort twice for lack of quorum.\n\n"
                        "**Kenya's Leadership:** To prevent the total collapse of the OAU, Kenyan President **Daniel arap Moi** served an unprecedented **two consecutive terms as OAU Chairman (1981 and 1982)**.\n\n"
                        "**The Addis Ababa Agreement:** Following this crisis, the OAU resolved that all future annual summits would permanently be hosted at the headquarters in Addis Ababa, Ethiopia, ending rotational hosting wrangles."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Principal Organs 2 & 3: Council of Ministers and Secretariat",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Executive and Administrative Organs of the OAU",
                "content": {
                    "headers": ["Organ Name", "Composition", "Meeting Schedule", "Primary Functions"],
                    "rows": [
                        ["The Council of Ministers", "Foreign Affairs Ministers of all member states", "Meets twice a year (February and before the annual Assembly)", "Prepares the detailed summit agenda, drafts the annual budget, and executes decisions passed by the Assembly."],
                        ["The General Secretariat", "Headed by Secretary-General with international staff based in Addis Ababa", "Continuous daily administrative service", "Manages daily administrative correspondence, prepares research reports, registers treaties, and oversees specialized commissions. (Notable long-serving leader: Salim Ahmed Salim of Tanzania)."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Principal Organ 4: Commission of Mediation",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Judicial and Peace Settlement Organ",
                "content": {
                    "text": (
                        "- **Composition:** Composed of **21 member states** elected by the Assembly for five-year terms.\n"
                        "- **Role:** Responsible for the peaceful diplomatic settlement of interstate disputes.\n"
                        "- **Mechanisms:** Dispatched mediation panels, fact-finding inquiry missions, and arbitration tribunals to defuse border wars and political clashes without resort to armed conflict."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Major Achievements of the OAU",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Eight Major Successes of the OAU (1963–2002)",
                "content": {
                    "steps": [
                        "1. Total Liberation of Africa: Channeled funds, arms, and training via the OAU Liberation Committee in Dar es Salaam, liberating Angola, Mozambique, Zimbabwe, Namibia, and Guinea-Bissau.",
                        "2. Dismantling Apartheid in South Africa: Lobbied the UN for global trade, sport, and arms embargoes against Pretoria, supporting the ANC until Nelson Mandela's 1994 democratic election.",
                        "3. Mediating Border Conflicts: Successfully defused the 1963 Sand War between Algeria and Morocco, and mediated disputes between Kenya-Somalia and Chad-Nigeria.",
                        "4. Promoting Regional Economic Integration: Facilitated the creation of regional economic blocs (ECOWAS, COMESA, EAC, SADC) as building blocks toward continental unity.",
                        "5. Establishing Common Financial Institutions: Founded the African Development Bank (ADB) in 1964, financing major infrastructure and agricultural development.",
                        "6. Fostering Socio-Cultural Bonding: Launched the All-Africa Games and created URTNA (Union of Radio and Television Networks of Africa) for continental cultural broadcasting.",
                        "7. Coordinating Scientific Research: Specialized agencies advanced research into traditional medicinal herbs and eradicated livestock diseases like East Coast Fever.",
                        "8. Unified Diplomatic Voice: Enabled African states to lobby as a powerful collective voting bloc inside the UN General Assembly on global security and development issues."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Failures and Limitations of the OAU",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The 'Toothless Bulldog': Why the OAU Was Criticized",
                "content": {
                    "text": (
                        "Despite its successes in decolonization, the OAU suffered grave structural failures:\n\n"
                        "- **Non-Interference Shielded Brutal Dictators:** Strict adherence to Article 3 (non-interference) meant the OAU stood by helplessly while ruthless tyrants—such as **Idi Amin in Uganda, Jean-Bédel Bokassa in the Central African Republic, and Mobutu Sese Seko in Zaire**—slaughtered their own citizens.\n"
                        "- **Failure in the 1994 Rwanda Genocide:** The OAU failed to intervene or deploy peacekeepers, watching helplessly as over 800,000 Tutsis and moderate Hutus were murdered in 100 days.\n"
                        "- **Inability to Halt Prolonged Civil Wars:** Paralyzed by factionalism, the OAU could not end devastating civil wars in Angola, Mozambique, Sudan, Somalia, and the DRC.\n"
                        "- **Absence of a Standing Military Force:** The OAU had no army of its own, earning it Muammar Gaddafi's famous nickname, the *'Toothless Bulldog'*.\n"
                        "- **The 1964 Congo Crisis:** Inability to handle secessionist crises led to the assassination of Prime Minister Patrice Lumumba and decades of instability."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Systemic Challenges Confronting the OAU",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Core Challenges Faced by the OAU",
                "content": {
                    "steps": [
                        "1. Chronic Financial Constraints: Many impoverished member states defaulted on annual dues, leaving the Secretariat perpetually underfunded.",
                        "2. Cold War Ideological Divisions: African states were polarized between pro-capitalist Western allies (Kenya, Zaire) and pro-socialist Eastern allies (Tanzania, Ethiopia).",
                        "3. Conflicting Loyalties to Other Blocs: Members prioritized commitments to the Commonwealth, Arab League, or French Community over OAU resolutions.",
                        "4. Superpower Interference: USA and USSR fueled proxy wars in Angola, Zaire, and the Horn of Africa, overriding OAU diplomatic peace initiatives.",
                        "5. Frequent Military Coups: Over 70 military coups occurred during the first 25 years of independence, disrupting leadership and policy continuity.",
                        "6. Voluntary Membership Weakness: States could easily threaten withdrawal whenever OAU resolutions conflicted with domestic regime interests."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Primary Source Inquiry: Non-Interference vs. Human Rights",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Evaluating the Dilemma of Article 3",
                "content": {
                    "text": (
                        "**Historical Dilemma:** In 1975, Ugandan dictator Idi Amin hosted the OAU summit in Kampala and was elected OAU Chairman, even as his secret police carried out mass executions of Ugandan civilians.\n\n"
                        "**Historical Analysis:**\n"
                        "1. **Observe:** Why were OAU leaders unable to legally censure or remove Idi Amin under the 1963 OAU Charter?\n"
                        "2. **Interpret:** How did this incident damage the moral credibility of the OAU on the global stage?\n"
                        "3. **Evolutionary Connection:** How did this fatal flaw inspire the modern African Union (AU) to incorporate Article 4(h)—the right of military intervention against war crimes and genocide?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Interactive Classification: OAU Organs",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the OAU Function to the Correct Organ",
                "content": {
                    "instruction": "Test your mastery of the OAU organizational structure:",
                    "items": [
                        "1. Supreme policy-making organ meeting annually -> **Assembly of Heads of State**",
                        "2. Prepares the summit agenda and annual budget -> **Council of Ministers**",
                        "3. Headed by the Secretary-General based in Addis Ababa -> **General Secretariat**",
                        "4. Arbitrates border and political disputes among 21 states -> **Commission of Mediation, Conciliation & Arbitration**",
                        "5. Channeled funds, arms, and training to southern liberation movements -> **OAU Liberation Committee (Dar es Salaam)**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "KCSE Examination Coaching: OAU Achievements & Failures",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Achievements and Five Failures of the OAU (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "**Achievements:**\n"
                        "1. **Liberation of the Continent:** Supported armed liberation struggles through the Liberation Committee in Dar es Salaam, liberating Mozambique, Angola, Zimbabwe, and Namibia. (2 marks)\n"
                        "2. **Dismantling Apartheid:** Successfully lobbied the UN for international trade and military embargoes against the racist Pretoria regime. (2 marks)\n"
                        "3. **Border Dispute Mediation:** Brokered peaceful ceasefires in disputes such as the 1963 Sand War between Algeria and Morocco. (2 marks)\n\n"
                        "**Failures:**\n"
                        "4. **Failure to Halt the 1994 Rwanda Genocide:** Paralyzed by lack of military force, the OAU failed to stop the massacre of over 800,000 lives. (2 marks)\n"
                        "5. **Shielding Tyrants under Non-Interference:** Strict adherence to non-interference prevented action against brutal dictators like Idi Amin in Uganda and Mobutu in Zaire. (2 marks)"
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
                "title": "Module 3.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What was the maximum percentage of the total OAU annual budget that any single member state was permitted to contribute under Article 23?",
                            "options": [
                                "10%",
                                "20%",
                                "33%",
                                "50%"
                            ],
                            "correct_answer": 1,
                            "explanation": "Article 23 capped contributions at 20% to prevent any single wealthy state from dominating the organization."
                        },
                        {
                            "question": "Why did President Daniel arap Moi of Kenya serve two consecutive terms as OAU Chairman in 1981 and 1982?",
                            "options": [
                                "The OAU Charter was amended to grant Kenya permanent leadership",
                                "A boycott by moderate states aborted the 1982 Tripoli summit under Muammar Gaddafi",
                                "Kenya paid the entire OAU budget for both years",
                                "All other African heads of state had retired"
                            ],
                            "correct_answer": 1,
                            "explanation": "The 1982 Tripoli summit collapsed due to a boycott over Gaddafi's role in Chad, prompting President Moi to serve a second term to maintain stability."
                        }
                    ]
                }
            },
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The Organisation of African Unity",
                "content": {
                    "text": (
                        "• **Founding:** 25 May 1963 in Addis Ababa, Ethiopia; Emperor Haile Selassie elected first chair.\n"
                        "• **Charter:** 33 Articles; Article 3 principles (sovereignty, non-interference); Article 23 budget cap (20%).\n"
                        "• **4 Organs:** Assembly (heads of state), Council of Ministers, General Secretariat, Commission of Mediation.\n"
                        "• **Key Successes:** Complete continental decolonization, anti-apartheid embargoes, border arbitrations, ADB (1964).\n"
                        "• **Key Failures:** Non-interference shielding dictators (Idi Amin), 1994 Rwanda Genocide failure, and lack of a standing army."
                    )
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Rebirth of the African Union (AU)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The African Union",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the chronological evolution from the OAU to the African Union (AU) (1999 Sirte to 2002 Durban)\n"
                        "- Compare and contrast the historical OAU and the modern AU across six key examinable dimensions\n"
                        "- Describe the composition and powers of the ten principal organs of the AU\n"
                        "- Analyze the core functions of the AU Peace and Security Council (PSC)\n"
                        "- Evaluate the strategic initiatives (NEPAD, APRM) and major challenges confronting the AU"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The African Union (AU)",
                "content": {
                    "term": "The African Union (AU)",
                    "definition": (
                        "The continental union consisting of 55 African sovereign states, formally launched on 9 July 2002 in Durban, South Africa, "
                        "designed to succeed the OAU by focusing on economic integration, democratic governance, human rights, and collective peace and security."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Timeline of the AU's Formation (1999–2002)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Four Historic Milestones in the Creation of the AU",
                "content": {
                    "steps": [
                        "1. Sirte Declaration (9 September 1999): Libyan leader Muammar Gaddafi hosted an extraordinary OAU summit in Sirte, Libya, issuing the declaration calling for an African Union.",
                        "2. Adoption of the Constitutive Act (July 2000): Heads of state formally debated and adopted the draft Constitutive Act of the African Union at the Lomé Summit in Togo.",
                        "3. Final OAU Summit (Lusaka 2001): The OAU met in Lusaka, Zambia, to adopt the transition blueprint from the OAU Secretariat to the new AU Commission.",
                        "4. Official Launch in Durban (9 July 2002): The African Union was formally launched in Durban, South Africa. President Thabo Mbeki of South Africa was elected the first AU Chairperson, and Amara Essy was appointed interim Commission Chair."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "OAU vs. AU: High-Yield Exam Comparison Table",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Comprehensive Comparison: The Historical OAU vs. The Modern AU",
                "content": {
                    "headers": ["Feature / Principle", "The Historical OAU (1963–2002)", "The Modern AU (2002–Present)"],
                    "rows": [
                        ["Core Philosophy", "Focused primarily on political liberation, anti-colonialism, and defending newly won sovereignty.", "Focuses on economic integration, democratic governance, human rights, and sustainable development."],
                        ["Intervention vs. Sovereignty", "Strict non-interference in internal affairs, which protected tyrants.", "Rejects absolute non-interference; Article 4(h) permits military intervention in cases of war crimes, genocide, and crimes against humanity."],
                        ["Organizational Nature", "An association of Heads of State; lacked popular citizen participation.", "A union of African peoples; incorporates civil society via Pan-African Parliament and ECOSOCC."],
                        ["Governance & Accountability", "Had no mechanism to monitor democratic standards or hold leaders accountable.", "Established the African Peer Review Mechanism (APRM) as a voluntary self-monitoring governance tool."],
                        ["Development Strategy", "Lacked a comprehensive continental economic growth blueprint.", "Established NEPAD (New Partnership for Africa's Development) to eradicate poverty and mobilize capital."],
                        ["Peace & Enforcement", "Had no standing army or security council; criticized as a 'toothless bulldog'.", "Established the Peace and Security Council (PSC) with a mandate to deploy the African Standby Force."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "African Union Headquarters in Addis Ababa",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "African Union Headquarters, Addis Ababa, Ethiopia",
                "content": {
                    "text": "The modern African Union Headquarters complex in Addis Ababa, Ethiopia, serving as the diplomatic capital and administrative hub of the 55 member states.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/1/14/AU_headquarters%2C_Addis_Ababa.jpg",
                    "author": "US Department of State / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:AU_headquarters,_Addis_Ababa.jpg"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Historical Documentary: The African Union Explained",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Educational Documentary: The African Union — Unity, Freedom, and Development",
                "content": {
                    "url": "https://www.youtube.com/watch?v=VA5fcKZZl2s",
                    "text": "Explore the mission, institutional structure, Peace and Security Council, and vision of Agenda 2063 of the African Union.",
                    "author": "Affluent Afrika / Educational Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Principal Organs 1 & 2: Assembly and Executive Council",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Supreme Governing Organs of the AU",
                "content": {
                    "headers": ["Organ Name", "Composition", "Meeting Schedule", "Primary Mandate"],
                    "rows": [
                        ["The Assembly of the AU", "Heads of State and Government of all 55 member states", "Meets annually in ordinary session", "Supreme decision-making organ; determines common policies, adopts the annual budget, monitors implementation, and appoints judges to the Court of Justice."],
                        ["The Executive Council", "Foreign Affairs Ministers designated by member governments", "Meets at least twice a year in ordinary session", "Responsible to the Assembly; coordinates policies in foreign trade, energy, agriculture, transport, and social security, preparing draft decisions for the Assembly."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Principal Organs 3, 4 & 5: PRC, AU Commission, and STCs",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Administrative and Technical Organs",
                "content": {
                    "text": (
                        "- **The Permanent Representatives Committee (PRC):** Composed of ambassadors accredited to the AU based in Addis Ababa. Prepares the work, agenda, and draft resolutions for the Executive Council.\n"
                        "- **The AU Commission:** The administrative secretariat of the union based in Addis Ababa. Composed of a Chairperson, a Deputy Chairperson, and eight specialized Commissioners managing portfolios (Peace/Security, Trade, Infrastructure, Political Affairs, Rural Economy, etc.).\n"
                        "- **Specialized Technical Committees (STCs):** Composed of senior government technical experts who design and evaluate union projects across health, agriculture, science, education, and transport."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Principal Organs 6, 7 & 8: Pan-African Parliament, Court, ECOSOCC",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Representative, Judicial, and Advisory Organs",
                "content": {
                    "headers": ["Organ Name", "Composition", "Headquarters", "Primary Mandate"],
                    "rows": [
                        ["Pan-African Parliament (PAP)", "Elected MPs nominated from the national parliaments of member states", "Midrand, South Africa", "Ensures democratic civil society participation, debating continental draft legislation and policies."],
                        ["The Court of Justice", "Independent judges elected by the Assembly", "Arusha, Tanzania", "Judicial organ ruling on human rights violations, disputes regarding the Constitutive Act, and treaty compliance."],
                        ["ECOSOCC", "Civic, professional, and non-governmental representatives", "Lusaka, Zambia", "Advisory organ channeling African civil society and grassroots voices directly into AU policymaking."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Financial Institutions of the African Union",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Building Continental Economic Sovereignty",
                "content": {
                    "text": (
                        "Under Article 19 of the Constitutive Act, the AU created three strategic financial institutions to mobilize capital and manage monetary integration:\n\n"
                        "1. **The African Central Bank:** Tasked with eventually issuing a single continental currency and managing continental monetary policy.\n"
                        "2. **The African Monetary Fund:** Designed to manage balance-of-payments emergencies and stabilize African exchange rates.\n"
                        "3. **The African Investment Bank:** Mandated to finance mega-infrastructure projects, energy grids, and trans-continental transportation networks."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The Peace and Security Council (PSC)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Executive Security Enforcer of the AU",
                "content": {
                    "text": (
                        "- **Composition:** Comprises **15 member states** (5 elected for 3-year terms, 10 elected for 2-year terms based on regional representation).\n"
                        "- **Operational Mandate:** Operates continuously to detect security crises, prevent conflicts, and deploy peacekeeping missions.\n"
                        "- **The African Standby Force (ASF):** Backed by regional standby brigades ready for rapid deployment across Africa.\n"
                        "- **Article 4(h) Right of Intervention:** The PSC possesses the constitutional right to authorize military intervention in any member state in cases of genocide, war crimes, and gross human rights violations."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "The Six Core Functions of the Peace and Security Council",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mandated Functions of the PSC (Article 6)",
                "content": {
                    "steps": [
                        "1. Promote Peace and Security: Maintain stability and early detection of emerging threats across the continent.",
                        "2. Early Warning & Preventive Diplomacy: Dispatch fact-finding and mediation missions to defuse crises before armed conflict breaks out.",
                        "3. Peacemaking and Mediation: Facilitate peace accords and ceasefires between warring factions.",
                        "4. Conduct Peace Support Operations: Deploy multinational peacekeeper missions (e.g., AMISOM/ATMIS in Somalia).",
                        "5. Post-Conflict Peacebuilding: Coordinate disarmament, demobilization, and economic reconstruction in post-war zones.",
                        "6. Coordinate Humanitarian Action: Organize emergency food, water, and medical relief for civilians during armed crises."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Strategic Initiatives: NEPAD and APRM",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Promoting Good Governance and Sustainable Development",
                "content": {
                    "text": (
                        "- **NEPAD (New Partnership for Africa's Development):** A comprehensive economic blueprint designed to eradicate poverty, accelerate sustainable growth, foster regional infrastructure, and halt the marginalization of Africa in the global economy.\n"
                        "- **APRM (African Peer Review Mechanism):** A voluntary self-monitoring governance system where member states submit their democratic institutions, economic management, and human rights records to periodic review by fellow African states."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Challenges Facing the African Union",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Five Critical Challenges Confronting the AU",
                "content": {
                    "steps": [
                        "1. Recurrent Civil and Border Conflicts: Chronic wars in Sudan, Somalia, the DRC, and the Sahel stretch AU peacekeeping capabilities and exhaust the Peace Fund.",
                        "2. Sovereignty Resistance from Regional Powers: Major powers (Nigeria, South Africa) are often reluctant to submit to binding AU decisions that constrain national policies.",
                        "3. Deep Ethnic, Religious, and Regional Divisions: Cultural and religious friction within member states undermines national cohesion and sparks instability.",
                        "4. Chronic Financial Dependency on Foreign Donors: Over 60% of the AU's program and peacekeeping budget is financed by external donors (European Union, UN), compromising autonomy.",
                        "5. Persistence of Unconstitutional Military Coups: A resurgence of military coups across West Africa and the Sahel tests the AU's zero-tolerance policy on unconstitutional changes of government."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Interactive Classification: AU Organs and Functions",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the AU Organ to Its Correct Description",
                "content": {
                    "instruction": "Test your mastery of the modern African Union structure:",
                    "items": [
                        "1. 15-member council with mandate to deploy the African Standby Force -> **Peace and Security Council (PSC)**",
                        "2. Elected MPs from national parliaments seated in Midrand, South Africa -> **Pan-African Parliament (PAP)**",
                        "3. Permanent ambassadors based in Addis Ababa preparing Executive Council work -> **Permanent Representatives Committee (PRC)**",
                        "4. Voluntary governance self-monitoring assessment mechanism -> **African Peer Review Mechanism (APRM)**",
                        "5. Advisory body representing civil society and professional associations -> **ECOSOCC**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "KCSE Examination Coaching: OAU vs. AU Comparison",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Compare and Contrast the OAU and the AU in Terms of Principles, Governance, and Security (15 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (3 Marks per fully developed comparative dimension):**\n\n"
                        "1. **Core Philosophy:** The OAU focused primarily on political liberation and decolonization, whereas the AU focuses on economic integration, democratic governance, and sustainable development. (3 marks)\n\n"
                        "2. **Intervention vs. Non-Interference:** The OAU strictly upheld non-interference in domestic affairs, shielding dictators, whereas the AU Constitutive Act under Article 4(h) permits military intervention in cases of genocide, war crimes, and crimes against humanity. (3 marks)\n\n"
                        "3. **Citizen and Civil Society Participation:** The OAU was strictly an association of heads of state, whereas the AU incorporates popular citizen representation through the Pan-African Parliament and ECOSOCC. (3 marks)\n\n"
                        "4. **Governance Accountability:** The OAU had no mechanism to hold leaders accountable for human rights abuses, whereas the AU established the African Peer Review Mechanism (APRM) to evaluate democracy and governance. (3 marks)\n\n"
                        "5. **Military and Security Architecture:** The OAU had no standing peacekeeping organ (labeled a 'toothless bulldog'), whereas the AU established the Peace and Security Council (PSC) backed by the African Standby Force. (3 marks)"
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
                "title": "Module 3.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which article of the AU Constitutive Act authorizes the union to intervene militarily in a member state during genocide or war crimes?",
                            "options": [
                                "Article 3(b)",
                                "Article 4(h)",
                                "Article 12(a)",
                                "Article 23"
                            ],
                            "correct_answer": 1,
                            "explanation": "Article 4(h) grants the AU the explicit right to intervene in a member state in cases of war crimes, genocide, and crimes against humanity."
                        },
                        {
                            "question": "In which South African city was the African Union formally launched on 9 July 2002?",
                            "options": [
                                "Johannesburg",
                                "Cape Town",
                                "Durban",
                                "Pretoria"
                            ],
                            "correct_answer": 2,
                            "explanation": "The AU was launched at the historic Durban Summit on 9 July 2002, with Thabo Mbeki as its first Chairperson."
                        }
                    ]
                }
            },
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The African Union",
                "content": {
                    "text": (
                        "• **Rebirth:** Conceived at Sirte (1999), adopted at Lomé (2000), launched at Durban (2002).\n"
                        "• **OAU vs. AU:** Shifted from decolonization to economic integration; replaced strict non-interference with Article 4(h) right of intervention.\n"
                        "• **Organs:** Assembly, Executive Council, PRC, AU Commission, STCs, Pan-African Parliament, Court of Justice, ECOSOCC, Financial Organs, Peace & Security Council.\n"
                        "• **Security Architecture:** 15-member PSC, African Standby Force, Peace Fund.\n"
                        "• **Key Challenges:** Conflict in the Horn/Sahel, external donor dependency, and unconstitutional coups."
                    )
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "The East African Community (EAC): Evolution and Rebirth",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The East African Community",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the colonial roots of East African cooperation (1902–1961)\n"
                        "- Analyze the 1967 EAC Treaty, its six core objectives, and its specialized corporations\n"
                        "- Explain the eleven distinct factors that caused the collapse of the EAC in 1977\n"
                        "- Trace the tripartite revival path leading to the 2001 EAC rebirth\n"
                        "- Evaluate the four stages of EAC integration and its contemporary challenges"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The East African Community (EAC)",
                "content": {
                    "term": "The East African Community (EAC)",
                    "definition": (
                        "The regional intergovernmental organization of partner states in the African Great Lakes region (originally Kenya, Uganda, and Tanzania; "
                        "now expanded to eight member states including Rwanda, Burundi, South Sudan, DRC, and Somalia), established to foster economic, social, and political integration."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Colonial Roots of East African Integration (1902–1961)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Chronological Foundations of East African Cooperation",
                "content": {
                    "steps": [
                        "1. 1902: East African Court of Appeal established to hear legal appeals from across Kenya, Uganda, and Zanzibar.",
                        "2. 1911: East African Postal Union formed to manage regional post and telegraph communications.",
                        "3. 1917: East African Customs Union created between Kenya and Uganda (Tanganyika joined in 1927) to facilitate duty-free trade.",
                        "4. 1920: East African Currency Board established to issue a single, unified East African Shilling.",
                        "5. 1948: East African High Commission formed, comprising colonial governors managing common railways, harbors, and postal services.",
                        "6. 1961: Replaced by East African Common Services Organisation (EACSO) headquartered in Nairobi to transition joint services to independence."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "The 1967 EAC Treaty and Founding Leaders",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Signing the 1967 East African Community Treaty",
                "content": {
                    "text": (
                        "- **The Philip Commission (1965):** Following independence, a political federation was ruled out, but economic integration remained essential. The Philip Commission recommended a formal community treaty.\n"
                        "- **Founding Signatories:** On **6 June 1967**, Presidents **Jomo Kenyatta (Kenya), Milton Obote (Uganda), and Julius Nyerere (Tanzania)** signed the treaty establishing the East African Community (coming into effect on **1 December 1967**).\n"
                        "- **Headquarters:** Established in **Arusha, Tanzania**."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Six Core Objectives of the 1967 EAC Treaty",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Aims of the 1967 East African Community",
                "content": {
                    "steps": [
                        "1. Promote Balanced Economic Cooperation: Maintain a common market and strengthen trade links among Kenya, Uganda, and Tanzania.",
                        "2. Provide Common Services: Jointly operate and manage regional railways, harbors, telecommunications, aviation, and customs.",
                        "3. Ensure Free Trade: Eliminate custom tariffs and trade barriers on locally manufactured goods.",
                        "4. Maintain a Common Currency: Facilitate transactions using the unified East African Shilling.",
                        "5. Establish Common External Tariffs: Protect infant local industries from external international dumping.",
                        "6. Equitably Share Assets: Fairly distribute community assets and bridge industrial gaps between states."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Organs of the 1967 EAC",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Key Decision-Making Organs (1967 Structure)",
                "content": {
                    "headers": ["Organ Name", "Composition", "Primary Mandate"],
                    "rows": [
                        ["The East African Authority", "The three Heads of State (Kenyatta, Obote, Nyerere)", "Supreme governing organ making major policy decisions by unanimous consensus."],
                        ["The East African Legislative Assembly (EALA)", "36 members chosen from the three partner states", "Enacted laws governing common community corporations and services."],
                        ["The Common Market Tribunal", "Judicial trade specialists", "Arbitrated commercial and tariff disputes between partner states."],
                        ["The Councils", "Five specialized councils (Finance, Common Market, Communications, Economic Consultative, Planning)", "Coordinated sectoral regional development programs."],
                        ["The Central Secretariat", "Headed by Secretary-General in Arusha", "Managed daily administrative coordination of all community activities."],
                        ["The Court of Appeal", "Senior judges from partner states", "Heard legal appeals from national High Courts across all three countries."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "The EAC Corporations and Headquarters Table",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Decentralized Headquarters of EAC Corporations (1967)",
                "content": {
                    "headers": ["Service / Corporation", "Headquarters Location", "Core Regional Function"],
                    "rows": [
                        ["East African Railways Corporation", "Nairobi, Kenya", "Operated the regional railway network, rolling stock, and maintenance workshops."],
                        ["East African Harbours Corporation", "Dar-es-Salaam, Tanzania", "Managed coastal shipping, port docking, off-loading, and lighthouse facilities."],
                        ["East African Post & Telecommunications", "Kampala, Uganda", "Provided regional telephone, telegraph, and postal communication networks."],
                        ["East African Airways Corporation", "Nairobi, Kenya", "Operated joint commercial domestic and international flight operations."],
                        ["East African Customs and Excise", "Mombasa, Kenya", "Collected coastal import duties and enforced common external tariffs."],
                        ["East African Development Bank (EADB)", "Kampala, Uganda", "Provided industrial development loans, prioritizing less-industrialized partners (Uganda and Tanzania)."],
                        ["EA Agriculture & Forestry Research", "Muguga, Kenya", "Conducted agricultural and crop breeding research to boost food security."],
                        ["East African Fisheries Research", "Jinja, Uganda", "Researched freshwater fish breeding and Lake Victoria water management."],
                        ["East African Literature Bureau", "Nairobi, Kenya", "Promoted writing, printing, and distribution of books by African authors."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Eleven Factors Causing the 1977 EAC Collapse",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Why the East African Community Collapsed in 1977",
                "content": {
                    "steps": [
                        "1. Uneven Economic Development: Uganda and Tanzania complained that Kenya benefited disproportionately because its advanced manufacturing sector dominated the common market.",
                        "2. Incompatible Economic Ideologies: Tanzania pursued socialism/Ujamaa, while Kenya and Uganda practiced free-market capitalism, making synchronized economic planning impossible.",
                        "3. Idi Amin's 1971 Military Coup in Uganda: Overthrew President Milton Obote, introducing extreme political instability and violence.",
                        "4. Bitter Personality Clashes: President Julius Nyerere granted asylum to Obote and refused to meet or sit at the same table with Idi Amin, paralyzing the East African Authority.",
                        "5. Conflicting National Priorities: Each state prioritized domestic projects over community plans (e.g., Tanzania invested in the Tazara railway, while Kenya prioritized road transport).",
                        "6. Failure to Remit Financial Dues: Uganda and Tanzania frequently defaulted on their financial contributions to the central secretariat in Arusha.",
                        "7. Dissolution of Common Currency: States abandoned the East African Shilling and introduced national currencies, complicating trade transactions.",
                        "8. Boundary Closures: Diplomatic friction caused boundary closures, culminating in Tanzania closing its common border with Kenya in 1977.",
                        "9. Harassment of Partner Nationals: Kenya complained its citizens working in Tanzanian harbor facilities were harassed and dismissed.",
                        "10. Unilateral Nationalization of EAC Assets: Partner states began unilaterally seizing community assets (ships, wagons, planes) within their borders.",
                        "11. Personal Ambitions of Leaders: Each head of state wanted to be seen as the most dominant political figure in the region."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Arusha International Conference Centre",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Arusha International Conference Centre (AICC)",
                "content": {
                    "text": "The Arusha International Conference Centre in Tanzania, headquarters of the East African Community and venue for landmark regional peace summits.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Arusha_International_Conference_Centre.jpg",
                    "author": "Muhammad Mahdi Karim / CC BY-SA 3.0",
                    "licensing": "CC BY-SA 3.0",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Arusha_International_Conference_Centre.jpg"
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Historical Documentary: The East African Community",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Documentary Video: The East African Community — History, Collapse, and Expansion",
                "content": {
                    "url": "https://www.youtube.com/watch?v=O-HF30d29Tk",
                    "text": "Trace the historical journey of the East African Community from its 1967 roots to its 1977 collapse, 2001 rebirth, and expansion to eight partner states.",
                    "author": "TD Clipz / Regional Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The Tripartite Path to Revival (1993–2001)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Rebirth of the EAC",
                "content": {
                    "steps": [
                        "1. 30 November 1993: Presidents Daniel arap Moi (Kenya), Yoweri Museveni (Uganda), and Ali Hassan Mwinyi (Tanzania) signed the agreement creating the Permanent Tripartite Commission for East African Cooperation.",
                        "2. 14 March 1996: The Secretariat of the Tripartite Commission was launched in Arusha; Ambassador Francis Muthaura of Kenya was appointed the first Secretary-General.",
                        "3. 30 November 1999: The formal Treaty for the Establishment of the East African Community was officially signed in Arusha.",
                        "4. 15 January 2001: The new East African Community (EAC) was formally launched at a historic summit in Arusha."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Organs of the Reborn EAC (2001 Structure)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Decision-Making Bodies of the Modern EAC",
                "content": {
                    "headers": ["Organ Name", "Composition", "Primary Function"],
                    "rows": [
                        ["The Summit", "Heads of State of partner countries", "Gives general political direction and appoints judges."],
                        ["The Council of Ministers", "Regional Cooperation Ministers of partner states", "Main decision-making and implementing organ."],
                        ["The Coordinating Committee", "Permanent Secretaries for regional cooperation", "Coordinates and evaluates reports of Sectoral Committees."],
                        ["Sectoral Committees", "Senior ministerial technical experts", "Design and prepare sector-specific integration programs."],
                        ["East African Court of Justice", "Two judges from each partner state based in Arusha", "Ensures adherence to law and interprets treaty provisions."],
                        ["East African Legislative Assembly (EALA)", "27 elected MPs (9 from each founder state) + 5 ex-officio", "Democratic legislative forum passing regional community laws."],
                        ["The Secretariat", "Rotational Secretary-General appointed for a 5-year term", "Administrative executive based at the EAC headquarters in Arusha."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "The Four Stages of EAC Integration & Customs Union",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Four Integration Pillars of the EAC",
                "content": {
                    "steps": [
                        "Stage 1: Customs Union (Operationalized 2005): Common External Tariff (CET) on non-member imports, duty-free internal trade, and uniform customs administration.",
                        "Stage 2: Common Market (Operationalized 2010): Free movement of goods, labor, services, capital, and the right of establishment and residence.",
                        "Stage 3: Monetary Union (In Progress): Harmonization of monetary and fiscal policies toward a single East African currency.",
                        "Stage 4: Political Federation (Ultimate Goal): Ultimate constitutional unification of member states under a single federal government."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Contemporary Challenges Facing the Modern EAC",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Eight Systemic Challenges of the Modern EAC",
                "content": {
                    "steps": [
                        "1. Perceived Dominance of Kenya: Suspicion remains that Kenya's competitive industrial sector benefits disproportionately.",
                        "2. Unilateral Custom Taxation: Partner customs periodically impose arbitrary tariffs on agricultural imports (e.g., dairy and poultry wrangles).",
                        "3. Cross-Border Smuggling & Crime: Free movement has facilitated smuggling of illegal firearms, contraband goods, and motor vehicle thefts.",
                        "4. Border Cattle Rustling: Armed raids between communities (Pokot of Kenya vs. Karamojong of Uganda) strain diplomatic ties.",
                        "5. Arrest of Fishermen on Lake Victoria: Territorial fishing boundary disputes cause recurrent arrests of Kenyan fishermen by Ugandan and Tanzanian naval police.",
                        "6. The Migingo Island Dispute: Diplomatic tensions between Kenya and Uganda over ownership of the rich fishing island of Migingo.",
                        "7. Lack of a Uniform Currency: Fluctuating national currencies complicate regional commercial transactions.",
                        "8. Divided Loyalties (Overlapping Memberships): Tanzania belongs to SADC, while Kenya and Uganda belong to COMESA, creating conflicting trade obligations."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Primary Evidence Analysis: The 1967 Treaty Signing",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Evaluating the Fragility of Early Regional Pacts",
                "content": {
                    "text": (
                        "**Historical Insight:** The 1967 EAC was celebrated as the most advanced integration model in the developing world, operating joint airlines, railways, and postal systems.\n\n"
                        "**Analytical Inquiry:**\n"
                        "1. **Structural Flaw:** Why was relying on unanimous consensus among only three heads of state (Authority) a fatal design flaw when Idi Amin took power in Uganda?\n"
                        "2. **Economic Conflict:** How did differing economic models (Kenyan capitalism vs. Tanzanian Ujamaa) undermine the Common Market Tribunal?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Interactive Classification: EAC Corporations",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Corporation to Its 1967 Headquarters",
                "content": {
                    "instruction": "Test your mastery of the historical decentralization of EAC corporations:",
                    "items": [
                        "1. East African Railways Corporation -> **Nairobi, Kenya**",
                        "2. East African Harbours Corporation -> **Dar-es-Salaam, Tanzania**",
                        "3. East African Post & Telecommunications -> **Kampala, Uganda**",
                        "4. East African Development Bank (EADB) -> **Kampala, Uganda**",
                        "5. East African Customs and Excise -> **Mombasa, Kenya**",
                        "6. EA Agriculture and Forestry Research -> **Muguga, Kenya**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "KCSE Examination Coaching: 1977 EAC Collapse",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Reasons for the Collapse of the East African Community in 1977 (12 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Uneven Economic Development:** Uganda and Tanzania complained that Kenya benefited disproportionately from the common market because its advanced manufacturing sector drained capital from partners. (2 marks)\n\n"
                        "2. **Incompatible Ideological Differences:** Tanzania pursued socialism/Ujamaa while Kenya and Uganda pursued capitalism, making synchronized regional economic planning impossible. (2 marks)\n\n"
                        "3. **Political Instability in Uganda:** Idi Amin's violent 1971 military coup introduced lawlessness, prompting President Nyerere to refuse to meet with Amin, completely paralyzing the Authority. (2 marks)\n\n"
                        "4. **Failure to Remit Financial Contributions:** Uganda and Tanzania frequently defaulted on their mandatory budgetary remittances to the central secretariat in Arusha. (2 marks)\n\n"
                        "5. **Arbitrary Closure of Borders:** Political tensions culminated in Tanzania closing its common border with Kenya in 1977, completely halting trade and travel. (2 marks)\n\n"
                        "6. **Nationalization of Community Assets:** Partner states unilaterally seized EAC wagons, ships, and aircraft located within their borders, delivering the final blow. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "Check Your Understanding: Module 3.5",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 3.5 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Where was the headquarters of the East African Harbours Corporation located under the 1967 structure?",
                            "options": [
                                "Nairobi, Kenya",
                                "Dar-es-Salaam, Tanzania",
                                "Kampala, Uganda",
                                "Mombasa, Kenya"
                            ],
                            "correct_answer": 1,
                            "explanation": "The East African Harbours Corporation was headquartered in Dar-es-Salaam, Tanzania."
                        },
                        {
                            "question": "Who was appointed as the first Secretary-General of the Permanent Tripartite Commission for East African Cooperation in 1996?",
                            "options": [
                                "Ambassador Francis Muthaura",
                                "Amanya Mushega",
                                "Juma Mwapachu",
                                "Erastus Mwencha"
                            ],
                            "correct_answer": 0,
                            "explanation": "Ambassador Francis Muthaura of Kenya served as the first Secretary-General of the revived secretariat in Arusha."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The East African Community",
                "content": {
                    "text": (
                        "• **Colonial Origins:** 1902 Court of Appeal, 1917 Customs Union, 1948 High Commission, 1961 EACSO.\n"
                        "• **1967 Treaty:** Signed by Kenyatta, Obote, and Nyerere in Arusha; decentralized corporations across capital cities.\n"
                        "• **1977 Collapse:** Caused by uneven development, capitalist vs. Ujamaa ideological clashes, Idi Amin's coup, border closures, and asset seizures.\n"
                        "• **2001 Rebirth:** Tripartite commission (1993) to Arusha Treaty (1999); 4 integration pillars (Customs Union, Common Market, Monetary Union, Political Federation).\n"
                        "• **Contemporary Challenges:** Kenya dominance perception, Migingo Island dispute, Lake Victoria fishing arrests, and overlapping memberships."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Regional integration requires both economic synchronization and political stability.\n"
                        "- The revived EAC is now one of Africa's fastest-growing regional economic blocs."
                    )
                }
            }
        ]
    }
]

LESSON_6_PAGES = [
    {
        "page_number": 1,
        "page_title": "ECOWAS: Regional Integration in West Africa",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: ECOWAS and ECOMOG",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the formation and membership of the Economic Community of West African States (ECOWAS) under the 1975 Treaty of Lagos\n"
                        "- Describe the principal organs and decision-making framework of ECOWAS\n"
                        "- Analyze the peacekeeping role of ECOMOG in resolving civil wars in Liberia and Sierra Leone\n"
                        "- Evaluate the major economic and socio-cultural achievements of ECOWAS\n"
                        "- Explain the eight critical challenges facing West African integration"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: ECOWAS",
                "content": {
                    "term": "ECOWAS (Economic Community of West African States)",
                    "definition": (
                        "A regional economic union of 15 (originally 17) West African sovereign states, established on 28 May 1975 under the Treaty of Lagos, "
                        "dedicated to fostering economic self-reliance, free movement of people, common technical standards, and regional collective security."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Formation and the 1975 Treaty of Lagos",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Lagos Treaty and Membership",
                "content": {
                    "text": (
                        "- **Origins:** Following diplomatic initiatives led by General Yakubu Gowon of Nigeria and President Gnassingbé Eyadéma of Togo, ECOWAS was founded on **28 May 1975** with the signing of the **Treaty of Lagos**.\n"
                        "- **Headquarters:** The Executive Secretariat was established in **Lagos, Nigeria (later moved to Abuja)**.\n"
                        "- **Membership:** Spans Anglophone, Francophone, and Lusophone states across West Africa (Benin, Burkina Faso, Cape Verde, Ivory Coast, Gambia, Ghana, Guinea, Guinea-Bissau, Liberia, Mali, Mauritania [withdrew 2000], Niger, Nigeria, Senegal, Sierra Leone, Togo)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Abuja Federal Capital and ECOWAS Secretariat",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Abuja, Federal Capital Territory, Nigeria",
                "content": {
                    "text": "Abuja, Nigeria, host city to the permanent headquarters of the ECOWAS Commission.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Abuja%2C_Federal_Capital_Territory%2C_Nigeria_%2849283733058%29.jpg",
                    "author": "Kaizenify / CC BY-SA 4.0",
                    "licensing": "CC BY-SA 4.0",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Abuja,_Federal_Capital_Territory,_Nigeria_(49283733058).jpg"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Educational Documentary: ECOWAS Explained",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Documentary Video: What is ECOWAS? Regional Integration in West Africa",
                "content": {
                    "url": "https://www.youtube.com/watch?v=_HUpuuHv0vs",
                    "text": "Understand the history, member nations, economic integration goals, and ECOMOG security operations of ECOWAS.",
                    "author": "Country Neighbors / Educational Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Five Core Objectives of ECOWAS",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Aims of the Economic Community of West African States",
                "content": {
                    "steps": [
                        "1. Foster Economic Integration: Promote cooperation in transport, telecommunications, agriculture, energy, and industry.",
                        "2. Free Movement of Goods, Capital, and Labour: Eliminate tariffs, customs quotas, and visa restrictions across West Africa.",
                        "3. Complete Economic Self-Reliance: Build regional industrial capacity to reduce dependency on Western economies.",
                        "4. Specialized Technical Commissions: Establish joint regional bodies in trade, immigration, and agricultural research.",
                        "5. Improve Living Standards: Enhance employment, social security, and peaceful coexistence among member nations."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Principal Organs of ECOWAS",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Key Decision-Making Bodies of ECOWAS",
                "content": {
                    "headers": ["Principal Organ", "Composition", "Meeting Frequency", "Primary Function"],
                    "rows": [
                        ["The Authority of Heads of State", "Heads of State of all member countries", "Meets once a year (chair rotates annually)", "Supreme governing organ responsible for general policy direction and major community decisions."],
                        ["The Council of Ministers", "Two ministers from each member state", "Meets twice a year", "Oversees daily operations, prepares the agenda and budget, and makes recommendations to the Authority."],
                        ["The Community Court of Justice / Tribunal", "Independent judges appointed by the Authority", "Continuous judicial service", "Interprets the Lagos Treaty and arbitrates disputes between partner states."],
                        ["The Executive Secretariat / Commission", "Headed by President/Executive Secretary based in Abuja", "Continuous administrative service", "Executes community policies, coordinates development programs, and runs daily administration."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Major Achievement: ECOMOG Peacekeeping Operations",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "ECOMOG: Pioneer Regional Peacekeeping in Africa",
                "content": {
                    "text": (
                        "ECOWAS achieved worldwide acclaim by creating the **Economic Community Monitoring Group (ECOMOG)**—a multinational armed peacekeeping force predominantly financed and manned by Nigeria:\n\n"
                        "- **The Liberian Civil War (1990):** When Liberia collapsed into catastrophic civil war under warlord Charles Taylor, ECOMOG deployed thousands of troops to Monrovia, restoring order and supervising democratic elections in 1997.\n"
                        "- **The Sierra Leone Civil War (1997–1999):** ECOMOG intervened decisively to crush the brutal RUF rebel insurgency and reinstate democratically elected President Ahmad Tejan Kabbah."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Other Major Achievements of ECOWAS",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Key Accomplishments of ECOWAS",
                "content": {
                    "steps": [
                        "1. Visa-Free Travel Protocol: Completely waived visa requirements for ECOWAS citizens, enabling 90-day visa-free residency, trade, and travel across West Africa.",
                        "2. Educational Harmonization: Established a unified high school curriculum and examination system through the West African Examinations Council (WAEC).",
                        "3. Discounted Energy Trade: Nigeria supplies discounted crude oil and petroleum products to resource-poor partner states, stabilizing regional fuel supplies.",
                        "4. ECOWAS Development Fund: Founded the Fund for Cooperation, Compensation, and Development in Lomé, Togo, financing cross-border highways and telecommunications.",
                        "5. Regular Political Consultation: Provided a continuous diplomatic platform defusing border tensions and mediating political crises in Guinea-Bissau, Mali, and Gambia."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Eight Critical Challenges Facing ECOWAS",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Systemic Obstacles to West African Integration",
                "content": {
                    "steps": [
                        "1. Influx of Migrant Workers & Expulsions: Free movement led to large migrant influxes into wealthier states; in 1983, Nigeria expelled over two million Ghanaian and foreign workers ('Ghana Must Go'), severely damaging relations.",
                        "2. Arbitrary Border Closures: Recurrent unilateral border closures (e.g., Ghana-Togo, Burkina Faso-Mali) halt regional trade.",
                        "3. Divided Loyalties: Members belong to overlapping organizations (Mano River Union, UEMOA, Commonwealth), creating conflicting commitments.",
                        "4. Anglophone vs. Francophone Rivalry: Persistent friction and mutual suspicion between English-speaking giants (Nigeria, Ghana) and French-speaking nations (Ivory Coast, Senegal).",
                        "5. Foreign Military Interference: Permanent presence of foreign military bases (French and US troops) bred suspicion among neighboring governments.",
                        "6. Currency Disparities: Multiplicity of volatile national currencies and the CFA Franc complicates monetary union.",
                        "7. Chronic Military Coups and Civil Wars: Recurring military takeovers across Guinea, Mali, Burkina Faso, and Niger disrupt integration treaties.",
                        "8. Financial Defaults on Annual Dues: Impoverished member states frequently default on their budgetary payments in foreign exchange."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Primary Source Case Study: The 1983 Nigerian Expulsion",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The 1983 'Ghana Must Go' Crisis",
                "content": {
                    "text": (
                        "**The Event:** In January 1983, amid domestic economic recession, Nigerian President Shehu Shagari issued an executive order giving undocumented immigrants two weeks to leave Nigeria, resulting in the mass exodus of over two million West Africans (mostly Ghanaians).\n\n"
                        "**Analytical Inquiry:**\n"
                        "1. **Observe:** How did the domestic economic crisis in Nigeria override ECOWAS's free movement protocol?\n"
                        "2. **Interpret:** What does this event illustrate about the fragility of regional protocols when national economies enter recession?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Interactive Classification: ECOWAS Achievements vs. Challenges",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify as an Achievement or Challenge of ECOWAS",
                "content": {
                    "instruction": "Categorize each scenario as either an Achievement or a Challenge of ECOWAS:",
                    "items": [
                        "1. Deployment of ECOMOG to quell the Liberian civil war -> **Achievement**",
                        "2. The 1983 mass expulsion of Ghanaian workers from Nigeria -> **Challenge**",
                        "3. Protocol allowing 90-day visa-free movement for citizens -> **Achievement**",
                        "4. Deep-seated rivalry between Francophone and Anglophone member states -> **Challenge**",
                        "5. Harmonized high school testing under WAEC -> **Achievement**",
                        "6. Recurrent military coups across the Sahel region -> **Challenge**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: ECOWAS Performance",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Successes and Five Challenges of ECOWAS Since 1975 (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "**Successes:**\n"
                        "1. **Peacekeeping Military Interventions:** Created ECOMOG, which successfully intervened to restore constitutional order during civil wars in Liberia and Sierra Leone. (2 marks)\n"
                        "2. **Free Movement of People:** Completely eliminated visa requirements for member citizens, facilitating 90-day free travel and cross-border commerce. (2 marks)\n"
                        "3. **Educational Harmonization:** Established a unified regional curriculum and secondary examination system through WAEC. (2 marks)\n\n"
                        "**Challenges:**\n"
                        "4. **Influx of Migrant Labour and Expulsions:** Large migrant flows caused friction, culminating in Nigeria expelling over two million Ghanaian workers in 1983. (2 marks)\n"
                        "5. **Anglophone vs. Francophone Friction:** Linguistic and political rivalry between English-speaking Nigeria and French-speaking nations delayed policy harmonization. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 3.6",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 3.6 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which treaty officially established the Economic Community of West African States (ECOWAS) in May 1975?",
                            "options": [
                                "The Treaty of Abuja",
                                "The Treaty of Lagos",
                                "The Treaty of Lomé",
                                "The Treaty of Accra"
                            ],
                            "correct_answer": 1,
                            "explanation": "ECOWAS was established on 28 May 1975 with the signing of the Treaty of Lagos."
                        },
                        {
                            "question": "What was the name of the ECOWAS military ceasefire monitoring group that intervened in Liberia and Sierra Leone?",
                            "options": [
                                "AMISOM",
                                "ECOMOG",
                                "UNAMID",
                                "MONUSCO"
                            ],
                            "correct_answer": 1,
                            "explanation": "ECOMOG (Economic Community Monitoring Group) was the armed peacekeeping force deployed to restore order in Liberia and Sierra Leone."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: ECOWAS in West African Affairs",
                "content": {
                    "text": (
                        "• **Origins:** Founded 28 May 1975 via Treaty of Lagos under Gowon (Nigeria) and Eyadéma (Togo); HQ in Abuja.\n"
                        "• **Key Organs:** Authority of Heads of State, Council of Ministers, Community Court, Executive Secretariat.\n"
                        "• **Major Successes:** ECOMOG peacekeeping (Liberia/Sierra Leone), visa-free travel protocol, WAEC exams, discounted Nigerian oil.\n"
                        "• **Major Challenges:** 1983 worker expulsion, border closures, Francophone vs. Anglophone friction, military coups, and currency volatility."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- ECOWAS pioneered regional armed peacekeeping in Africa through ECOMOG.\n"
                        "- Balancing national economic sovereignty with regional free movement remains a delicate challenge in West Africa."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Revision Checklist for ECOWAS",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist: Key Examinable Concepts",
                "content": {
                    "steps": [
                        "1. Treaty of Lagos (1975) and Founding Membership (Nigeria, Togo leadership).",
                        "2. Five Objectives: Economic self-reliance, free movement of labor/capital, specialized commissions.",
                        "3. Four Principal Organs: Authority, Council of Ministers, Community Court, Secretariat in Abuja.",
                        "4. ECOMOG Peacekeeping in Liberia (1990) and Sierra Leone (1997).",
                        "5. Visa-free 90-day travel and WAEC educational harmonization.",
                        "6. 1983 Nigerian Expulsion Crisis ('Ghana Must Go') and its causes.",
                        "7. Anglophone vs. Francophone friction and military coup disruptions."
                    ]
                }
            }
        ]
    }
]

LESSON_7_PAGES = [
    {
        "page_number": 1,
        "page_title": "COMESA and Continental Economic Integration",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: COMESA and Continental Integration",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the transition from the Preferential Trade Area (PTA) to COMESA (1981–1994)\n"
                        "- Explain the phased integration timeline and core objectives of COMESA\n"
                        "- Describe the principal organs and specialized financial institutions of COMESA\n"
                        "- Evaluate the major achievements and challenges confronting COMESA\n"
                        "- Explain the ten general structural barriers hindering full continental economic integration across Africa"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: COMESA",
                "content": {
                    "term": "COMESA (Common Market for Eastern and Southern Africa)",
                    "definition": (
                        "The largest regional economic integration bloc in Africa, consisting of 19 (formerly 21) sovereign member states spanning "
                        "from Egypt in the north to Zimbabwe and Eswatini in the south, established in 1994 to replace the PTA and build a fully integrated free trade area, customs union, and monetary union."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Origins: From PTA to the COMESA Treaty (1981–1994)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Evolution of COMESA",
                "content": {
                    "steps": [
                        "1. The PTA Era (December 1981): Founded as the Preferential Trade Area for Eastern and Southern African States (PTA) to reduce tariffs gradually.",
                        "2. The COMESA Treaty (5 November 1993): Partner heads of state met in Kampala, Uganda, and signed the formal treaty transforming the PTA into a common market.",
                        "3. Formal Ratification (8 December 1994): Formally ratified at the first official summit in Lilongwe, Malawi, officially birthing COMESA.",
                        "4. Headquarters: Established in Lusaka, Zambia.",
                        "5. Membership: Spans 19 member countries (Angola, Burundi, Comoros, DR Congo, Djibouti, Egypt, Eritrea, Ethiopia, Kenya, Libya, Madagascar, Malawi, Mauritius, Rwanda, Seychelles, Somalia, Sudan, Tunisia, Uganda, Zambia, Zimbabwe). Note: Tanzania and Namibia withdrew to focus on SADC."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Phased Integration Roadmap of COMESA",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Three Phased Integration Milestones",
                "content": {
                    "steps": [
                        "Phase 1: Free Trade Area (Target: 2000): Complete elimination of internal customs duties and tariffs on all originating goods traded among partner states.",
                        "Phase 2: Customs Union (Target: 2004): Establishment of a Common External Tariff (CET) on all goods imported from non-member countries.",
                        "Phase 3: Monetary Union (Target: 2005): Creation of a single regional central bank and adoption of a common regional currency."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Six Core Objectives of COMESA",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Foundational Aims of COMESA",
                "content": {
                    "steps": [
                        "1. Sustainable Economic Growth: Promote balanced, harmonious development through trade liberalization and marketing coordination.",
                        "2. Macro-Economic Policy Harmonization: Adopt joint financial, monetary, and fiscal policies across member states.",
                        "3. Investment Climate Enhancement: Create an enabling legal and financial environment for domestic and foreign cross-border investments.",
                        "4. Global Trade Competitiveness: Strengthen collective commercial bargaining power with international markets.",
                        "5. Stepping Stone to Continental Unity: Contribute directly to the creation of the wider African Economic Community (AEC).",
                        "6. Peace, Security, and Stability: Promote conflict resolution and diplomatic stability as essential preconditions for economic development."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Principal Organs of COMESA",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Decision-Making Bodies of COMESA",
                "content": {
                    "headers": ["Principal Organ", "Composition", "Primary Function"],
                    "rows": [
                        ["The Authority of Heads of State", "Heads of State of all 19 member countries", "Supreme policy organ meeting annually; reaches decisions by consensus, binding on all subordinate organs."],
                        ["The Council of Ministers", "Ministers designated by member governments", "Oversees financial and administrative management of the secretariat, making policy recommendations."],
                        ["The Court of Justice", "Seven independent judges based in Khartoum (later relocated)", "Ensures proper interpretation of the treaty and arbitrates trade disputes (e.g., mediated 2004 Kenya-Egypt cement dumping dispute)."],
                        ["Central Bank Governors Committee", "Governors of national central banks", "Determines debt limits for the Clearing House, coordinates exchange rates, and oversees monetary cooperation."],
                        ["The Secretariat", "Headed by Secretary-General based in Lusaka, Zambia", "Manages daily administrative, technical, and advisory support (notably led for years by Erastus Mwencha of Kenya)."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Specialized Institutions of COMESA",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Specialized Financial and Technical Bodies",
                "content": {
                    "headers": ["Specialized Body", "Location", "Primary Function"],
                    "rows": [
                        ["PTA Trade and Development Bank (Trade & Development Bank)", "Nairobi, Kenya / Bujumbura", "Provides trade financing facilities, export credit, and developmental investment capital."],
                        ["COMESA Clearing House", "Harare, Zimbabwe", "Enables partner states to settle day-to-day trade transactions using local currencies, economizing scarce US dollars."],
                        ["COMESA Re-Insurance Company (ZEP-RE)", "Nairobi, Kenya", "Provides regional insurance and reinsurance underwriting services to protect commercial investments."],
                        ["COMESA Leather & Leather Products Institute", "Addis Ababa, Ethiopia", "Coordinates research, modern processing technologies, and marketing for regional leather industries."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Lusaka Skyline and COMESA Centre",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Lusaka, Zambia — Headquarters of COMESA",
                "content": {
                    "text": "Lusaka, Zambia, host capital to the permanent COMESA Secretariat and Centre.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/1/12/Lusaka%2C_Zambia.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Lusaka,_Zambia.jpg"
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Educational Documentary: COMESA Explained",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Documentary Video: What is COMESA? Common Market for Eastern and Southern Africa",
                "content": {
                    "url": "https://www.youtube.com/watch?v=1lTNnW-f5OM",
                    "text": "Explore the mission, member countries, trade facilitation programs, and economic impact of COMESA.",
                    "author": "5min Knowledge / Educational Overview",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Major Achievements of COMESA",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Seven Major Accomplishments of COMESA",
                "content": {
                    "steps": [
                        "1. Massive Growth in Intra-Regional Trade: Tariff reductions and quota removals generated unprecedented trade volume among Eastern and Southern African states.",
                        "2. 25% Reduction in Transport and Transit Costs: Harmonized road transit charges, unified cross-border licenses, and single customs documentation significantly lowered logistics costs.",
                        "3. Established World-Class Financial Institutions: Founded the PTA Bank (TDB), COMESA Clearing House, ZEP-RE Reinsurance, and the Leather Institute.",
                        "4. Computerized Customs Clearance Network: Deployed the ASYCUDA automated customs software across border posts, speeding cargo clearance and reducing corruption.",
                        "5. Conflict Mediation and Peacebuilding: Enforced governance and conflict-resolution requirements prior to state accession (e.g., Rwanda and Burundi pre-admission accords).",
                        "6. Joint Industrial Ventures: Promoted multi-national industrial projects, such as joint fertilizer plants in Uganda and leather processing in Ethiopia.",
                        "7. Agricultural and Food Security Coordination: Created early warning systems monitoring regional drought patterns and facilitating cross-border grain transfers."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Challenges Facing COMESA",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Nine Key Challenges Confronting COMESA",
                "content": {
                    "steps": [
                        "1. Hostile External Terms of Trade: High prices for Western industrial imports vs. low prices for raw agricultural exports keep trade balances negative.",
                        "2. Heavy Foreign Debt Burden: Severe debt repayments to Western lenders deplete foreign currency reserves needed for regional investments.",
                        "3. Harsh IMF Structural Adjustment Programmes (SAPs): Forced fiscal austerity and currency devaluations caused economic stagnation and domestic factory closures.",
                        "4. Devastating Natural Calamities: Recurrent droughts and crop failures force states to divert development funds to emergency relief food imports.",
                        "5. Severe Youth Unemployment: High unemployment depresses domestic purchasing power for COMESA manufactured goods.",
                        "6. National Protectionism Overriding Treaties: Member states frequently impose emergency import duties to protect uncompetitive local industries.",
                        "7. Active Civil Strife & Insecurity: Wars in the DRC, Sudan, and Somalia disrupt transit corridors and investor confidence.",
                        "8. Similarity of Agricultural Commodities: Most members produce identical raw crops (tea, coffee, cotton, tobacco), limiting internal trade exchange.",
                        "9. Withdrawal of Key Founder States: The departure of Tanzania and Namibia to join SADC weakened COMESA's geopolitical cohesion."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Ten General Barriers to Continental Economic Integration",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Ten Universal Barriers to Full African Integration",
                "content": {
                    "steps": [
                        "1. Poor Transport and Communication Infrastructure: Inadequate trans-continental highways, rail links, and ports make intra-African shipping slow and expensive.",
                        "2. Uneven Distribution of Natural Resources: Pockets of mineral and oil wealth are concentrated in few countries (Nigeria, South Africa), breeding trade imbalances.",
                        "3. Chronic Foreign Exchange Shortages: Balance of payment deficits leave nations with insufficient hard currency to settle intra-African trade bills.",
                        "4. Political Interference by National Leaders: Nationalistic rulers frequently shut borders, violate tariff pacts, or withdraw from regional blocs during political disputes.",
                        "5. Mutual Suspicion and Border Rivalries: Historical territorial wrangles prevent governments from fully opening borders or permitting free labor migration.",
                        "6. Low Share of Global Trade & Commodity Dependency: African economies are vulnerable price-takers for raw materials, with minimal value addition.",
                        "7. Impact of IMF Structural Adjustment Programmes (SAPs): Austerity measures, retrenchments, and trade liberalization weakened domestic manufacturing capacity.",
                        "8. OAU/AU Historical Non-Interference Principle: Allowed prolonged civil wars to destroy regional transit corridors and regional markets.",
                        "9. Widespread Default on Annual Financial Dues: Financially stressed partner states fail to remit annual dues, crippling integration secretariats.",
                        "10. Legacy of Neo-Colonialism: Structural economic dependency leads African states to maintain closer trade ties with former European colonial powers than with neighbors."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Deep Dive: Infrastructure, Disparities, and Foreign Exchange",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Physical and Monetary Bottlenecks to Unity",
                "content": {
                    "text": (
                        "- **The Infrastructure Deficit:** Colonial transport systems were designed strictly to extract raw minerals from the interior to coastal ports for shipment to Europe. There are virtually no East-West trans-continental highways connecting Central Africa with West or East Africa.\n"
                        "- **Foreign Exchange Scarcity:** Because African currencies are not universally convertible, a Kenyan merchant buying goods from Egypt or Zambia often has to convert shillings into US dollars, paying multiple transaction fees and risking currency depreciation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Deep Dive: Neo-Colonialism and Structural Adjustment",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "External Economic Hegemony",
                "content": {
                    "text": (
                        "- **Neo-Colonial Trade Ties:** Decades after independence, Anglophone African nations still conduct the majority of trade with the UK and USA, while Francophone states trade heavily with France. Preferential European trade agreements often discourage intra-African sourcing.\n"
                        "- **The SAP Shock:** During the 1980s and 1990s, World Bank/IMF Structural Adjustment Programmes forced African governments to cut public subsidies to agriculture and domestic manufacturing, leaving local industries defenseless against foreign competition."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "KCSE Examination Command Words Guide",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Mastering KCSE Paper 2 Answering Techniques",
                "content": {
                    "text": (
                        "In KCSE History Paper 2, marks are awarded strictly based on the command word in the question:\n\n"
                        "- **'State' / 'Name' / 'Identify' (1 mark per point):** Write a concise, factual point without elaboration (e.g., *Name two founder members that withdrew from COMESA:* 1. Tanzania, 2. Namibia).\n"
                        "- **'Define' (2 marks):** Provide the full, formal historical definition of the term.\n"
                        "- **'Explain' / 'Discuss' (2 marks per point):** Always structure your response in three parts: **Point** (1 mark) + **Detailed Explanation / Historical Example** (1 mark)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Primary Source Analysis: The 1994 Lilongwe Statement",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The 1994 Lilongwe Summit",
                "content": {
                    "text": (
                        "**Primary Statement:** *'We are drafting beautiful treaties with zero-tariff timelines. But as long as our railways are broken, our currencies fluctuate against each other, and we must borrow from London and Paris to pay our bills, these documents will remain mere paper.'* (Delegate at 1994 COMESA Summit)\n\n"
                        "**Analytical Questions:**\n"
                        "1. **Identify:** What three structural barriers to regional integration are highlighted in this statement?\n"
                        "2. **Explain:** How does the legacy of neo-colonial debt reinforce the delegate's skepticism?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Interactive Classification: EAC vs. ECOWAS vs. COMESA",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Feature to the Correct Regional Bloc",
                "content": {
                    "instruction": "Test your comparative mastery across the three African economic blocs:",
                    "items": [
                        "1. Established under the 1975 Treaty of Lagos -> **ECOWAS**",
                        "2. Headquartered in Arusha, Tanzania, with 4 integration stages -> **EAC**",
                        "3. Replaced the 1981 PTA and is headquartered in Lusaka, Zambia -> **COMESA**",
                        "4. Created the ECOMOG military peacekeeping force for civil wars -> **ECOWAS**",
                        "5. Operates the Trade and Development Bank (PTA Bank) in Nairobi -> **COMESA**",
                        "6. Collapsed in 1977 due to ideological and political differences -> **EAC**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "KCSE Examination Coaching: COMESA Achievements & Barriers",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five General Barriers Hindering Continental Economic Integration in Africa (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Inadequate Transport and Communication Networks:** Poor trans-continental roads and railways make the movement of goods between regions slow and expensive. (2 marks)\n\n"
                        "2. **Chronic Foreign Exchange Shortages:** Most African states suffer balance of payment deficits, lacking convertible currency to finance regional trade imports. (2 marks)\n\n"
                        "3. **Similarity of Trade Commodities:** Most countries produce identical agricultural raw materials (tea, coffee, cotton), limiting trade exchange with neighbors. (2 marks)\n\n"
                        "4. **Political Interference and Protectionism:** National leaders frequently close borders or violate tariff pacts to protect uncompetitive local industries. (2 marks)\n\n"
                        "5. **The Legacy of Neo-Colonialism:** Structural economic dependency leads African states to prioritize trade and financial ties with former European colonial powers over African neighbors. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "Topic 3 Master Summary & Revision Checklist",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 3 Comprehensive Mastery Check",
                "content": {
                    "questions": [
                        {
                            "question": "In which city was the COMESA treaty signed in November 1993?",
                            "options": [
                                "Lusaka, Zambia",
                                "Kampala, Uganda",
                                "Lilongwe, Malawi",
                                "Nairobi, Kenya"
                            ],
                            "correct_answer": 1,
                            "explanation": "The COMESA treaty was signed in Kampala, Uganda, on 5 November 1993 and later ratified in Lilongwe in December 1994."
                        },
                        {
                            "question": "Which of the following is a key specialized institution of COMESA based in Nairobi, Kenya?",
                            "options": [
                                "The COMESA Clearing House",
                                "The PTA Trade and Development Bank (TDB)",
                                "The Leather and Leather Products Institute",
                                "The African Development Bank"
                            ],
                            "correct_answer": 1,
                            "explanation": "The PTA Bank (Trade and Development Bank) operates from Nairobi, providing trade and investment financing across COMESA."
                        }
                    ]
                }
            },
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 3 Master Summary: Co-operation in Africa",
                "content": {
                    "text": (
                        "• **Pan-Africanism:** Birthed in the diaspora (Garvey, Du Bois, Washington); transformed at Manchester 1945; moved to Africa under Nkrumah and Tom Mboya.\n"
                        "• **OAU (1963–2002):** Addis Ababa charter; liberated Africa and dismantled apartheid; limited by non-interference and lack of army.\n"
                        "• **AU (2002–Present):** Durban launch; Article 4(h) right of intervention against genocide; 10 organs; Peace and Security Council; APRM & NEPAD.\n"
                        "• **EAC (1967 & 2001):** 1967 Treaty collapsed in 1977; revived in 2001; 4 stages (Customs Union, Common Market, Monetary Union, Political Federation).\n"
                        "• **ECOWAS (1975):** Treaty of Lagos; ECOMOG peacekeeping; visa-free travel; challenged by 1983 worker expulsion and coups.\n"
                        "• **COMESA (1994):** Replaced PTA; Lusaka HQ; PTA Bank; challenged by commodity similarity and debt.\n"
                        "• **Continental Barriers:** Transport infrastructure deficit, neo-colonial dependency, foreign exchange scarcity, and protectionism."
                    )
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "Pan-Africanism — Origin, Causes, and Early Development (Pre-1945)",
        "lesson_title": "Pan-Africanism: Origins, Early Pioneers, and the Diaspora Era",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "The Manchester Congress (1945) and Movement on African Soil",
        "lesson_title": "The 1945 Manchester Congress and the Return to African Soil",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "The Organisation of African Unity (OAU) — Formation, Charter, and Performance",
        "lesson_title": "The Organisation of African Unity: Structure, Successes, and Failures",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "The African Union (AU) — Rebirth, Structure, and Challenges",
        "lesson_title": "The African Union: Evolution, Governance, and Security Architecture",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "The East African Community (EAC) — 1967 and 2001 Rebirth",
        "lesson_title": "The East African Community: Evolution, 1977 Collapse, and 2001 Rebirth",
        "pages": LESSON_5_PAGES
    },
    {
        "unit_order": 6,
        "unit_name": "The Economic Community of West African States (ECOWAS)",
        "lesson_title": "ECOWAS: Regional Integration, ECOMOG Peacekeeping, and Dynamics",
        "pages": LESSON_6_PAGES
    },
    {
        "unit_order": 7,
        "unit_name": "The Common Market for Eastern and Southern Africa (COMESA) and Continental Integration",
        "lesson_title": "COMESA and Continental Economic Integration in Africa",
        "pages": LESSON_7_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 3 (CO-OPERATION IN AFRICA)")
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
            name="Co-operation in Africa",
            defaults={"order": 3}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 3
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
        print(f"[SUCCESS] Form 4 History Topic 3 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 3")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
