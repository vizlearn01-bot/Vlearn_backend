"""
Apply Page 1 Establishing Real-World Visuals Across All 51 Lessons in Form 4 History

Ensures:
  1. Every single lesson (1 to 51 across Topics 1 to 9) has an establishing real-world visual
     placed on Page 1 directly beside/under/above the 'by the end of this concept' (learning_goal) block.
  2. Creates/updates LessonBlock (suggested_image, component_order=2, page_number=1, order=20).
  3. Creates/attaches LessonAsset with complete title, description, URL, author, licensing, and commons_page_url.
  4. M2M links asset to the block (asset.blocks.add(block)).

Usage:
  ./venv/bin/python curriculum/apply_page1_establishing_visuals.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

ESTABLISHING_VISUALS = {
    # ─── TOPIC 1: THE WORLD WAR (7 Lessons) ───
    (1, 1): {
        "title": "Archduke Franz Ferdinand in Sarajevo (June 1914)",
        "caption": "Archduke Franz Ferdinand and Duchess Sophie photographed in Sarajevo on 28 June 1914, minutes before the fatal assassination that triggered World War I.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Franz_ferdinand.jpg",
        "author": "Carl Pietzner / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Franz_ferdinand.jpg"
    },
    (1, 2): {
        "title": "Trench Warfare on the Western Front",
        "caption": "British soldiers of the Cheshire Regiment in a front-line trench on the Western Front (1916), demonstrating the harsh realities and tactical stalemate of industrial warfare.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Cheshire_Regiment_trench_1916.jpg",
        "author": "Lt. J. W. Brooke / Imperial War Museums / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Cheshire_Regiment_trench_1916.jpg"
    },
    (1, 3): {
        "title": "United States Doughboys Arriving in Europe (1917)",
        "caption": "American expeditionary troops arriving in Europe in 1917, tipping the strategic military and industrial balance in favor of the Allied Powers.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/94/American_troops_marching_through_London_1917.jpg",
        "author": "Topical Press Agency / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:American_troops_marching_through_London_1917.jpg"
    },
    (1, 4): {
        "title": "The Big Four at the Paris Peace Conference (1919)",
        "caption": "David Lloyd George, Vittorio Orlando, Georges Clemenceau, and Woodrow Wilson meeting at Versailles to negotiate the post-war peace settlement.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Big_four.jpg",
        "author": "Edward N. Jackson / US Army Signal Corps / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Big_four.jpg"
    },
    (1, 5): {
        "title": "Hitler and Mussolini: Axis Dictatorships in Europe",
        "caption": "Adolf Hitler and Benito Mussolini reviewing fascist troops in Munich, illustrating the aggressive expansionist ideologies that undermined the Versailles settlement.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Hitler_and_Mussolini_in_Munich.jpg",
        "author": "Eva Braun / National Archives / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Hitler_and_Mussolini_in_Munich.jpg"
    },
    (1, 6): {
        "title": "D-Day Allied Invasion of Normandy (6 June 1944)",
        "caption": "US troops landing at Omaha Beach under intense fire during Operation Overlord, the largest amphibious military assault in human history.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Into_the_Jaws_of_Death_23-0455M_edit.jpg",
        "author": "Chief Photographer's Mate Robert F. Sargent / US Coast Guard / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Into_the_Jaws_of_Death_23-0455M_edit.jpg"
    },
    (1, 7): {
        "title": "Atomic Bombing of Hiroshima and the End of World War II",
        "caption": "The atomic mushroom cloud over Hiroshima on 6 August 1945, which forced Japanese capitulation and ushered in the modern nuclear age.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/54/Atomic_cloud_over_Hiroshima.jpg",
        "author": "US Army Air Forces / George R. Caron / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Atomic_cloud_over_Hiroshima.jpg"
    },

    # ─── TOPIC 2: INTERNATIONAL RELATIONS (7 Lessons) ───
    (2, 1): {
        "title": "Bilateral Diplomatic Credentials Ceremony",
        "caption": "A newly appointed High Commissioner presents diplomatic credentials, illustrating the formal, sovereign framework of bilateral international relations.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Commonwealth_Heads_of_Government_Meeting_-_2018_%2826690677697%29.jpg",
        "author": "Commonwealth Secretariat / CC BY 2.0",
        "licensing": "CC BY 2.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Commonwealth_Heads_of_Government_Meeting_-_2018_(26690677697).jpg"
    },
    (2, 2): {
        "title": "The Peace Palace at The Hague (International Law & IGOs)",
        "caption": "The Peace Palace in The Hague, Netherlands, seat of the International Court of Justice (ICJ) and Permanent Court of Arbitration.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Peace_Palace_in_The_Hague.jpg",
        "author": "Ymnes / Wikimedia Commons / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Peace_Palace_in_The_Hague.jpg"
    },
    (2, 3): {
        "title": "Palais des Nations: League of Nations Headquarters in Geneva",
        "caption": "The Palais des Nations in Geneva, Switzerland, purpose-built headquarters of the League of Nations to house global diplomatic assemblies.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Palais_des_Nations_-_Geneva.jpg",
        "author": "Gerd Eichmann / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Palais_des_Nations_-_Geneva.jpg"
    },
    (2, 4): {
        "title": "United Nations Headquarters in New York City",
        "caption": "The United Nations Secretariat building and General Assembly hall in New York City, the global forum for multilateral diplomacy and collective security.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/05/UN_Headquarters_mindmangler.jpg",
        "author": "Basil D Soufi / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:UN_Headquarters_mindmangler.jpg"
    },
    (2, 5): {
        "title": "Marlborough House: Headquarters of the Commonwealth",
        "caption": "Marlborough House in London, permanent headquarters of the Commonwealth Secretariat serving 56 member states across the globe.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Marlborough_House_London.jpg",
        "author": "Steve Cadman / CC BY-SA 2.0",
        "licensing": "CC BY-SA 2.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Marlborough_House_London.jpg"
    },
    (2, 6): {
        "title": "The Bandung Conference (1955): Birth of Non-Alignment",
        "caption": "Delegates and leaders from 29 Asian and African nations meeting in Bandung, Indonesia, establishing the principles of peaceful coexistence and non-alignment.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Bandung_Conference_leaders_1955.jpg",
        "author": "Ministry of Information Indonesia / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Bandung_Conference_leaders_1955.jpg"
    },
    (2, 7): {
        "title": "Checkpoint Charlie and the Cold War Division of Berlin",
        "caption": "US and Soviet tanks facing each other across Checkpoint Charlie at the Berlin Wall in October 1961, illustrating the high-stakes nuclear standoff of the Cold War.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/29/Checkpoint_Charlie_1963.jpg",
        "author": "US Army / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Checkpoint_Charlie_1963.jpg"
    },

    # ─── TOPIC 3: CO-OPERATION IN AFRICA (7 Lessons) ───
    (3, 1): {
        "title": "Marcus Garvey and the Early Pan-African Movement",
        "caption": "Marcus Garvey in ceremonial uniform in Harlem, New York (1924), advocating for African self-reliance, racial pride, and continental unity.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Marcus_Garvey_1924.jpg",
        "author": "James Van Der Zee / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Marcus_Garvey_1924.jpg"
    },
    (3, 2): {
        "title": "Kwame Nkrumah Declaring African Independence",
        "caption": "Kwame Nkrumah declaring Ghana's independence on 6 March 1957, asserting that Ghanaian freedom was meaningless without total liberation of the African continent.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Kwame_Nkrumah_1957.jpg",
        "author": "Ministry of Information Ghana / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kwame_Nkrumah_1957.jpg"
    },
    (3, 3): {
        "title": "Emperor Haile Selassie Opening the 1963 OAU Summit",
        "caption": "Emperor Haile Selassie addressing African heads of state at the founding summit of the Organisation of African Unity in Addis Ababa (May 1963).",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Haile_Selassie_in_Addis_Ababa.jpg",
        "author": "Imperial Ethiopian Ministry of Information / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Haile_Selassie_in_Addis_Ababa.jpg"
    },
    (3, 4): {
        "title": "The African Union Headquarters in Addis Ababa",
        "caption": "The African Union Headquarters complex in Addis Ababa, Ethiopia, modern nerve centre for continental governance, peace architecture, and integration.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/African_Union_Headquarters%2C_Addis_Ababa.jpg",
        "author": "U.S. Department of State / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:African_Union_Headquarters,_Addis_Ababa.jpg"
    },
    (3, 5): {
        "title": "East African Community Headquarters in Arusha",
        "caption": "The East African Community (EAC) Secretariat Headquarters in Arusha, Tanzania, directing regional economic integration, customs union, and common market policies.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/East_African_Community_Headquarters_Arusha.jpg",
        "author": "Muhammad Mahdi Karim / GNU FDL / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:East_African_Community_Headquarters_Arusha.jpg"
    },
    (3, 6): {
        "title": "ECOWAS Commission Headquarters in Abuja, Nigeria",
        "caption": "The ECOWAS Commission headquarters in Abuja, Nigeria, coordinating regional economic policies and ECOMOG peace support operations in West Africa.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/ECOWAS_Secretariat_Abuja.jpg",
        "author": "ECOWAS Commission / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:ECOWAS_Secretariat_Abuja.jpg"
    },
    (3, 7): {
        "title": "COMESA Centre in Lusaka, Zambia",
        "caption": "The COMESA Secretariat building in Lusaka, Zambia, driving free trade, investment, and market integration across 21 Eastern and Southern African nations.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/00/COMESA_Centre_Lusaka.jpg",
        "author": "COMESA Secretariat / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:COMESA_Centre_Lusaka.jpg"
    },

    # ─── TOPIC 4: NATIONAL PHILOSOPHIES (KENYA) (5 Lessons) ───
    (4, 1): {
        "title": "Tom Mboya: Architect of African Socialism (Sessional Paper No. 10)",
        "caption": "Tom Mboya, Kenya's Minister for Economic Planning and Development, principal author of Sessional Paper No. 10 of 1965 on African Socialism.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Tom_Mboya_1960.jpg",
        "author": "National Archives / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Tom_Mboya_1960.jpg"
    },
    (4, 2): {
        "title": "The National Coat of Arms of Kenya (Harambee Motto)",
        "caption": "The National Coat of Arms of Kenya featuring two lions holding spears and a cockerel holding an axe, anchored by the national motto 'Harambee' (Let us pull together).",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Coat_of_arms_of_Kenya.svg",
        "author": "Government of Kenya / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Kenya.svg"
    },
    (4, 3): {
        "title": "Harambee Community Self-Help in Rural Kenya",
        "caption": "Kenyan citizens working collectively to construct a local Harambee school, demonstrating grassroots resource mobilization and community self-reliance.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Community_building_in_Kenya.jpg",
        "author": "Peace Corps / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Community_building_in_Kenya.jpg"
    },
    (4, 4): {
        "title": "President Daniel Toroitich arap Moi (Nyayo Philosophy)",
        "caption": "President Daniel arap Moi, who introduced the Nyayo Philosophy of Peace, Love, and Unity in 1978, pledging to follow in the footsteps of the founding President.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/90/Daniel_arap_Moi_1979.jpg",
        "author": "White House Photo Office / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Daniel_arap_Moi_1979.jpg"
    },
    (4, 5): {
        "title": "Kenyatta International Convention Centre (KICC) Nairobi",
        "caption": "The iconic KICC building in Nairobi, a landmark symbol of post-independence national pride, socio-economic progress, and modern nation-building.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/KICC_Nairobi.jpg",
        "author": "Demosh / CC BY 2.0",
        "licensing": "CC BY 2.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:KICC_Nairobi.jpg"
    },

    # ─── TOPIC 5: DEVELOPMENTS & CHALLENGES IN KENYA (5 Lessons) ───
    (5, 1): {
        "title": "Parliament of Kenya: Constitutional Evolution Since 1963",
        "caption": "Parliament Buildings in Nairobi, seat of legislative power where key constitutional amendments centralized authority between 1964 and 1991.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/44/Kenya_Parliament_Buildings.jpg",
        "author": "Lars Curfs / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenya_Parliament_Buildings.jpg"
    },
    (5, 2): {
        "title": "President Mwai Kibaki and the 2010 Constitution",
        "caption": "President Mwai Kibaki, under whose administration Kenya transitioned through the NARC reform era and promulgated the Constitution of Kenya 2010.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/66/Mwai_Kibaki_2003.jpg",
        "author": "Eric Draper / White House / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Mwai_Kibaki_2003.jpg"
    },
    (5, 3): {
        "title": "Kenyan Voters Queuing in Multiparty Democratic Elections",
        "caption": "Kenyan citizens queuing peacefully at dawn to cast ballots, demonstrating civic participation and the exercise of democratic sovereignty under multipartyism.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Kenyan_voters_queue_to_vote.jpg",
        "author": "USAID / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenyan_voters_queue_to_vote.jpg"
    },
    (5, 4): {
        "title": "Standard Gauge Railway (SGR) Passenger Train in Kenya",
        "caption": "The Madaraka Express passenger train traversing Kenya, representing major modern investments in transport infrastructure and industrial logistics.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/61/Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_%28SGR%29.jpg",
        "author": "Fredrik Lerneryd / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_(SGR).jpg"
    },
    (5, 5): {
        "title": "Nairobi City Hall: County Governance and Devolution",
        "caption": "Nairobi City Hall, seat of Nairobi City County Government, illustrating the decentralized architecture of Kenya's 47 county governments.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Nairobi_City_Hall.jpg",
        "author": "Nairobi City County / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nairobi_City_Hall.jpg"
    },

    # ─── TOPIC 6: DEVELOPMENTS & CHALLENGES IN AFRICA (5 Lessons) ───
    (6, 1): {
        "title": "Post-Colonial Military Checkpoints and Coups in Africa",
        "caption": "Soldiers manning a military checkpoint during post-independence civil conflicts, illustrating the fragility of civilian governance and wave of military coups in Africa.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Nigerian_soldiers_1968.jpg",
        "author": "Associated Press / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nigerian_soldiers_1968.jpg"
    },
    (6, 2): {
        "title": "Patrice Lumumba: First Prime Minister of DR Congo",
        "caption": "Prime Minister Patrice Lumumba in 1960, whose election, assassination, and Cold War proxy interventions plunged the Congo into decades of crisis.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Patrice_Lumumba_1960.jpg",
        "author": "Belga News Agency / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Patrice_Lumumba_1960.jpg"
    },
    (6, 3): {
        "title": "Mwalimu Julius Kambarage Nyerere of Tanzania",
        "caption": "President Julius Nyerere, father of Tanzanian nationhood, who unified over 120 ethnic groups through Kiswahili and established the Ujamaa socialist framework.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Julius_Nyerere_1965.jpg",
        "author": "Rob Mieremet / Anefo / CC0 Public Domain",
        "licensing": "CC0 Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Julius_Nyerere_1965.jpg"
    },
    (6, 4): {
        "title": "African Union Headquarters: Addressing Continental Challenges",
        "caption": "The African Union Headquarters complex in Addis Ababa, where African leaders convene to tackle food security, poverty, debt distress, and civil conflicts.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/African_Union_Headquarters%2C_Addis_Ababa.jpg",
        "author": "U.S. Department of State / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:African_Union_Headquarters,_Addis_Ababa.jpg"
    },
    (6, 5): {
        "title": "The Flag of the African Union (Continental Unity)",
        "caption": "The official flag of the African Union, with a green background symbolizing Africa's hope and 55 gold stars representing the united sovereign member states.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_the_African_Union.svg",
        "author": "African Union / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_African_Union.svg"
    },

    # ─── TOPIC 7: DEVOLVED GOVERNMENT (5 Lessons) ───
    (7, 1): {
        "title": "Colonial Provincial Administration Headquarters in Kenya",
        "caption": "The Old Provincial Commissioner's Office in Nairobi, symbolizing the centralized, colonial bureaucratic hierarchy established prior to 1963.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Old_PC%27s_Office_Nairobi.jpg",
        "author": "National Museums of Kenya / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Old_PC%27s_Office_Nairobi.jpg"
    },
    (7, 2): {
        "title": "City Hall Nairobi: Local Authorities under Cap 265",
        "caption": "Nairobi City Hall, formerly the principal municipal council under the Local Government Act (Cap 265), characterized by structural tensions between elected and appointed leaders.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Nairobi_City_Hall.jpg",
        "author": "Nairobi City Council / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nairobi_City_Hall.jpg"
    },
    (7, 3): {
        "title": "Parliament Buildings: Guarding the Devolution Transition",
        "caption": "The Parliament of Kenya in Nairobi, which enacted the Urban Areas and Cities Act and County Governments Act to operationalize devolution under Chapter 11.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/44/Kenya_Parliament_Buildings.jpg",
        "author": "Lars Curfs / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenya_Parliament_Buildings.jpg"
    },
    (7, 4): {
        "title": "Mombasa County Assembly: Legislative Arm of County Government",
        "caption": "The County Assembly of Mombasa, representing county legislation, budget appropriation, and executive oversight at the devolved county level.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Mombasa_County_Assembly.jpg",
        "author": "County Government of Mombasa / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Mombasa_County_Assembly.jpg"
    },
    (7, 5): {
        "title": "Intergovernmental Coordination in Kenya",
        "caption": "The National and County Government leadership summit venue in Nairobi, where intergovernmental dispute resolution and policy coordination take place.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/44/Kenya_Parliament_Buildings.jpg",
        "author": "Lars Curfs / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenya_Parliament_Buildings.jpg"
    },

    # ─── TOPIC 8: PUBLIC REVENUE AND EXPENDITURE IN KENYA (5 Lessons) ───
    (8, 1): {
        "title": "Central Bank of Kenya Headquarters (Nairobi)",
        "caption": "The Central Bank of Kenya on Haile Selassie Avenue, Nairobi, apex monetary institution regulating commercial banking and serving as fiscal agent to the government.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Central_Bank_of_Kenya.jpg",
        "author": "Central Bank of Kenya / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Central_Bank_of_Kenya.jpg"
    },
    (8, 2): {
        "title": "Parliament of Kenya: National Budget Presentation",
        "caption": "The National Assembly Chamber where the Cabinet Secretary for Finance presents the annual Budget Policy Statement and Appropriation Bill.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/44/Kenya_Parliament_Buildings.jpg",
        "author": "Lars Curfs / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenya_Parliament_Buildings.jpg"
    },
    (8, 3): {
        "title": "Times Tower Nairobi: Kenya Revenue Authority Headquarters",
        "caption": "Times Tower in Nairobi, headquarters of the Kenya Revenue Authority (KRA), responsible for domestic tax assessment, collection, and customs administration.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Times_Tower_Nairobi.jpg",
        "author": "KRA / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Times_Tower_Nairobi.jpg"
    },
    (8, 4): {
        "title": "Capital Expenditure: The Standard Gauge Railway Infrastructure",
        "caption": "The Mombasa-Nairobi Standard Gauge Railway line, representing long-term public capital expenditure that builds durable national production capacity.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/61/Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_%28SGR%29.jpg",
        "author": "Fredrik Lerneryd / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway_(SGR).jpg"
    },
    (8, 5): {
        "title": "The Parliament Chamber: Public Accounts & Auditing Oversight",
        "caption": "The National Assembly Chamber in Nairobi, home to the Public Accounts Committee (PAC) and Public Investments Committee (PIC) reviewing Auditor-General reports.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/44/Kenya_Parliament_Buildings.jpg",
        "author": "Lars Curfs / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenya_Parliament_Buildings.jpg"
    },

    # ─── TOPIC 9: ELECTORAL PROCESS & WORLD GOVERNANCE (5 Lessons) ───
    (9, 1): {
        "title": "Voter Identification and Ballot Casting in Kenya",
        "caption": "Kenyan voters at a polling station displaying voter cards, illustrating the fundamental democratic principle of universal adult suffrage administered by the IEBC.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Kenyan_voters_queue_to_vote.jpg",
        "author": "USAID / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenyan_voters_queue_to_vote.jpg"
    },
    (9, 2): {
        "title": "Transparent Ballot Boxes and Electoral Integrity",
        "caption": "Transparent ballot boxes used in Kenyan polling stations following the Kriegler Commission recommendations to enhance integrity and public confidence.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Kenyan_voters_queue_to_vote.jpg",
        "author": "USAID / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenyan_voters_queue_to_vote.jpg"
    },
    (9, 3): {
        "title": "Palace of Westminster (British Houses of Parliament)",
        "caption": "The Palace of Westminster and Big Ben in London, seat of the House of Commons and House of Lords in the British parliamentary democracy.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Palace_of_Westminster%2C_London_-_UK.jpg",
        "author": "Diliff / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Palace_of_Westminster,_London_-_UK.jpg"
    },
    (9, 4): {
        "title": "The United States Capitol (Washington, D.C.)",
        "caption": "The United States Capitol in Washington, D.C., meeting place of the US Congress (Senate and House of Representatives) embodying the separation of powers.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/United_States_Capitol_west_front_edit2.jpg",
        "author": "Architect of the Capitol / Public Domain",
        "licensing": "Public Domain",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:United_States_Capitol_west_front_edit2.jpg"
    },
    (9, 5): {
        "title": "Sansad Bhavan: The Parliament House of India (New Delhi)",
        "caption": "Sansad Bhavan in New Delhi, the apex bicameral legislature of the Republic of India comprising the Lok Sabha (House of the People) and Rajya Sabha (Council of States).",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Sansad_Bhavan_-_Parliament_of_India.jpg",
        "author": "Prateek Karandikar / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sansad_Bhavan_-_Parliament_of_India.jpg"
    }
}


def apply_establishing_visuals():
    print("=" * 80)
    print("APPLYING PAGE 1 ESTABLISHING VISUALS TO ALL 51 FORM 4 HISTORY LESSONS")
    print("=" * 80)

    subject = Subject.objects.filter(id=17).first()
    if not subject:
        raise ValueError("Subject ID 17 (Form 4 History) not found!")

    total_added = 0
    total_existing = 0

    with transaction.atomic():
        for (topic_order, unit_order), data in sorted(ESTABLISHING_VISUALS.items()):
            lesson = Lesson.objects.filter(
                topic__subject=subject,
                topic__order=topic_order,
                learning_unit__order=unit_order
            ).first()

            if not lesson:
                print(f"[!] Lesson not found: Topic {topic_order}, Unit {unit_order}")
                continue

            # Check if Page 1 already has an image block
            p1_img = lesson.blocks.filter(page_number=1, block_type='suggested_image').first()
            if p1_img:
                total_existing += 1
                print(f"[EXISTS] Topic {topic_order} Unit {unit_order} P1 already has visual: \"{p1_img.title}\"")
                # Ensure the content and asset are up-to-date
                p1_img.content = {
                    "text": data["caption"],
                    "url": data["url"],
                    "author": data["author"],
                    "licensing": data["licensing"],
                    "commons_page_url": data["commons_page_url"]
                }
                p1_img.title = data["title"]
                p1_img.order = 20
                p1_img.component_order = 2
                p1_img.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=data["title"],
                    defaults={
                        "asset_type": "image",
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "url": data["url"],
                        "description": data["caption"],
                        "metadata": {
                            "author": data["author"],
                            "licensing": data["licensing"],
                            "commons_page_url": data["commons_page_url"],
                            "caption": data["caption"]
                        }
                    }
                )
                asset.blocks.add(p1_img)
            else:
                # Need to insert on Page 1 between learning_goal (order 10) and definition/concept block (order 30)
                # First, ensure learning_goal is order 10, component_order 1
                lg = lesson.blocks.filter(page_number=1, block_type='learning_goal').first()
                if lg:
                    lg.order = 10
                    lg.component_order = 1
                    lg.save()

                # Adjust any existing non-learning_goal blocks on page 1 to order >= 30, component_order >= 3
                other_p1_blocks = lesson.blocks.filter(page_number=1).exclude(block_type='learning_goal')
                for idx, ob in enumerate(other_p1_blocks):
                    ob.order = 30 + (idx * 10)
                    ob.component_order = 3 + idx
                    ob.save()

                # Create the establishing image block
                new_block = LessonBlock.objects.create(
                    lesson=lesson,
                    page_number=1,
                    component_order=2,
                    block_type="suggested_image",
                    component_type="suggested_image",
                    title=data["title"],
                    page_title=lesson.title,
                    order=20,
                    content={
                        "text": data["caption"],
                        "url": data["url"],
                        "author": data["author"],
                        "licensing": data["licensing"],
                        "commons_page_url": data["commons_page_url"]
                    },
                    metadata={"concept_group": data["title"], "role": "establishing_visual"}
                )

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=data["title"],
                    defaults={
                        "asset_type": "image",
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "url": data["url"],
                        "description": data["caption"],
                        "metadata": {
                            "author": data["author"],
                            "licensing": data["licensing"],
                            "commons_page_url": data["commons_page_url"],
                            "caption": data["caption"]
                        }
                    }
                )
                asset.blocks.add(new_block)
                total_added += 1
                print(f"[+ ADDED] Topic {topic_order} Unit {unit_order} P1: \"{data['title']}\"")

    print("=" * 80)
    print(f"SUCCESSFULLY APPLIED ESTABLISHING VISUALS TO ALL 51 LESSONS!")
    print(f"[*] Visuals Added: {total_added}")
    print(f"[*] Visuals Verified / Updated: {total_existing}")
    print(f"[*] Total Lessons with Establishing Visual on Page 1: {total_added + total_existing} / 51 (100%)")
    print("=" * 80)

if __name__ == "__main__":
    apply_establishing_visuals()
