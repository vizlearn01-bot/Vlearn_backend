"""
VLearn CBC Grade 9 CRE — Topic 1: Work
Lesson 2: Importance of Work: Traditional African vs. Christian Teachings
Database Ingestion & Enrichment Script
"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

# Set up paths and Django environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from django.db import transaction
from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    """Removes developer tags, bracket citations, and normalizes markdown formatting."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[(?:VISUAL|BIBLE REFERENCE|REAL WORLD APPLICATION|REFLECTION):?\s*.*?\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
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

# High quality responsive SVG Diagram comparing Traditional African Communal Labor vs Christian Biblical Work & Sabbath Rest
SVG_COMPARISON_DIAGRAM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="africanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="christianGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="synthesisGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="12" />

  <!-- Header Section -->
  <text x="400" y="38" text-anchor="middle" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" letter-spacing="0.5">
    Comparative Framework: Work Ethics &amp; Philosophy
  </text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="13">
    Traditional African Communal Labor vs. Christian Biblical Work &amp; Rest
  </text>

  <!-- Left Column: Traditional African Perspective -->
  <g transform="translate(30, 80)">
    <rect width="355" height="235" rx="10" fill="#1e293b" stroke="#d97706" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect width="355" height="38" rx="10" fill="url(#africanGrad)"/>
    <rect width="355" height="15" y="23" fill="url(#africanGrad)"/>
    <text x="177" y="24" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700">
      Traditional African Heritage
    </text>

    <!-- Content Items -->
    <g transform="translate(15, 55)" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">
      <circle cx="6" cy="6" r="3.5" fill="#f59e0b"/>
      <text x="18" y="10" font-weight="600" fill="#fbbf24">Communal Solidarity (Mwethya / Harambee):</text>
      <text x="18" y="25" fill="#cbd5e1" font-size="11.5">Work unites the clan; no monetary wages; shared harvest.</text>

      <circle cx="6" cy="46" r="3.5" fill="#f59e0b"/>
      <text x="18" y="50" font-weight="600" fill="#fbbf24">Division by Age &amp; Gender:</text>
      <text x="18" y="65" fill="#cbd5e1" font-size="11.5">Structured roles (defense, farming, herding, nurturing).</text>

      <circle cx="6" cy="86" r="3.5" fill="#f59e0b"/>
      <text x="18" y="90" font-weight="600" fill="#fbbf24">Zero Tolerance for Laziness:</text>
      <text x="18" y="105" fill="#cbd5e1" font-size="11.5">Sloth rebuked through folk songs, proverbs, and ostracism.</text>

      <circle cx="6" cy="126" r="3.5" fill="#f59e0b"/>
      <text x="18" y="130" font-weight="600" fill="#fbbf24">Spiritual Invocation:</text>
      <text x="18" y="145" fill="#cbd5e1" font-size="11.5">Prayers, rituals, and libations seeking divine blessing on land.</text>
    </g>
  </g>

  <!-- Right Column: Christian Biblical Perspective -->
  <g transform="translate(415, 80)">
    <rect width="355" height="235" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect width="355" height="38" rx="10" fill="url(#christianGrad)"/>
    <rect width="355" height="15" y="23" fill="url(#christianGrad)"/>
    <text x="177" y="24" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700">
      Christian Biblical Teachings
    </text>

    <!-- Content Items -->
    <g transform="translate(15, 55)" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">
      <circle cx="6" cy="6" r="3.5" fill="#60a5fa"/>
      <text x="18" y="10" font-weight="600" fill="#93c5fd">God as the Primary Worker &amp; Creator:</text>
      <text x="18" y="25" fill="#cbd5e1" font-size="11.5">Creation is divine labor (Gen 2:1-3); work reflects God's image.</text>

      <circle cx="6" cy="46" r="3.5" fill="#60a5fa"/>
      <text x="18" y="50" font-weight="600" fill="#93c5fd">Stewardship &amp; Co-Creatorship:</text>
      <text x="18" y="65" fill="#cbd5e1" font-size="11.5">Mandated to guard and cultivate Eden (Gen 2:15) with integrity.</text>

      <circle cx="6" cy="86" r="3.5" fill="#60a5fa"/>
      <text x="18" y="90" font-weight="600" fill="#93c5fd">Moral Obligation &amp; Diligence:</text>
      <text x="18" y="105" fill="#cbd5e1" font-size="11.5">"No work, no food" (2 Thess 3:10); learn from the ant (Prov 6:6).</text>

      <circle cx="6" cy="126" r="3.5" fill="#60a5fa"/>
      <text x="18" y="130" font-weight="600" fill="#93c5fd">The Gift of Sabbath Rest:</text>
      <text x="18" y="145" fill="#cbd5e1" font-size="11.5">Mandatory rhythm of work and rest for worship &amp; renewal.</text>
    </g>
  </g>

  <!-- Bottom Synthesis Box: Shared Values & Harmonious Integration -->
  <g transform="translate(30, 330)">
    <rect width="740" height="98" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect width="740" height="28" rx="10" fill="url(#synthesisGrad)"/>
    <rect width="740" height="10" y="18" fill="url(#synthesisGrad)"/>
    <text x="370" y="19" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700">
      Harmonious Convergence: Shared CBC Values
    </text>

    <g transform="translate(20, 42)" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11.5">
      <text x="0" y="12" fill="#a7f3d0" font-weight="600">&#10003; Mutual Dignity of Labor:</text>
      <text x="185" y="12" fill="#f1f5f9">Both view work as a sacred duty sustaining life and building society.</text>

      <text x="0" y="32" fill="#a7f3d0" font-weight="600">&#10003; Rejection of Idleness:</text>
      <text x="185" y="32" fill="#f1f5f9">Both condemn sluggards/parasites who exploit the labor of others.</text>

      <text x="0" y="50" fill="#a7f3d0" font-weight="600">&#10003; Holistic Wellbeing:</text>
      <text x="185" y="50" fill="#f1f5f9">Balancing hard communal exertion with celebration, family time, and spiritual rest.</text>
    </g>
  </g>
</svg>"""

LESSON_DATA = {
    "unit_order": 2,
    "unit_name": "Importance of Work: Traditional African vs. Christian Teachings",
    "unit_description": "Comparing the importance, cultural roles, and attitudes toward work in traditional African societies with Christian biblical teachings on stewardship and rest.",
    "lesson_title": "Importance of Work: Traditional African vs. Christian Teachings",
    "pages": [
        # Page 1: Discovery & Objectives
        [
            {
                "type": "suggested_image",
                "title": "Communal Agricultural Harvest in Africa",
                "content": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Farmers_in_Rwanda.jpg/1280px-Farmers_in_Rwanda.jpg",
                    "caption": "Farmers working together in communal solidarity during harvest season in East Africa.",
                    "author": "Wikimedia Commons / CIAT",
                    "licensing": "Creative Commons Attribution-Share Alike 2.0 Generic"
                }
            },
            {
                "type": "learning_goal",
                "title": "Lesson Learning Goals",
                "content": {
                    "goals": [
                        "Analyze traditional African attitudes toward work, including communal solidarity and role specialization.",
                        "Examine Christian biblical teachings on work, stewardship, co-creatorship, and the commandment of rest.",
                        "Compare the philosophical similarities and distinctions between traditional African labor practices and Christian work ethics."
                    ]
                }
            },
            {
                "type": "concept_explanation",
                "title": "The Spirit of Communal Labor",
                "content": {
                    "text": (
                        "Have you ever participated in a school cleanup day, helped a neighbor build a fence, or joined family members "
                        "during planting and harvest season without expecting monetary payment? In many Kenyan communities, working together "
                        "creates deep bonds of solidarity and makes demanding tasks light and joyful.\n\n"
                        "This communal spirit—exemplified by cultural traditions such as *Mwethya* among the Kamba, *Harambee* nationally, and *Kikao* across "
                        "various communities—formed the bedrock of traditional African work ethics. When we compare these traditions with Christian scriptures, "
                        "we discover rich parallels and complementary insights on how human labor honors God and sustains human dignity."
                    )
                }
            }
        ],

        # Page 2: Scriptural Exegesis
        [
            {
                "type": "concept_explanation",
                "title": "Scriptural Foundations on Work and Rest",
                "content": {
                    "text": (
                        "### Key Biblical Passages on Human Labor\n\n"
                        "**Genesis 2:1-3**\n"
                        "> *\"Thus the heavens and the earth were completed in all their vast array. By the seventh day God had finished the work he had been doing; so on the seventh day he rested from all his work. Then God blessed the seventh day and made it holy, because on it he rested from all the work of creating that he had done.\"*\n\n"
                        "**2 Thessalonians 3:10-12**\n"
                        "> *\"For even when we were with you, we gave you this rule: 'The one who is unwilling to work shall not eat.' We hear that some among you are idle and disruptive... Such people we command and urge in the Lord Jesus Christ to settle down and earn the food they eat.\"*\n\n"
                        "**Proverbs 6:6-8 & 10:4**\n"
                        "> *\"Go to the ant, you sluggard; consider its ways and be wise! It has no commander, no overseer or ruler, yet it stores its provisions in summer and gathers its food at harvest.\"* (Proverbs 6:6-8)\n"
                        "> *\"Lazy hands make for poverty, but diligent hands bring wealth.\"* (Proverbs 10:4)"
                    )
                }
            },
            {
                "type": "concept_explanation",
                "title": "Theological Exegesis: God as the Worker & Human Co-Creatorship",
                "content": {
                    "text": (
                        "Christian theology presents a revolutionary understanding of labor through several foundational truths:\n\n"
                        "1. **God as the Original Worker:** Unlike ancient mythologies where gods created humans as slaves to escape manual labor, the Bible portrays the Sovereign God actively designing, planting, and fashioning the universe (Genesis 1-2). Labor is therefore holy, noble, and inherent to God's divine character.\n\n"
                        "2. **Stewardship and Co-Creatorship:** In Genesis 2:15, God placed man in the Garden of Eden to cultivate (*abad*) and guard (*shamar*) it. Human work is not a curse resulting from sin; it was instituted before the Fall as a sacred partnership where humans steward creation and reflect God's creative order.\n\n"
                        "3. **Moral Obligation and Condemnation of Idleness:** The Apostle Paul writes firmly against freeloading and idleness in the early church (2 Thessalonians 3:10-12). Work provides self-reliance, preserves personal dignity, and generates resources to care for widows, orphans, and the vulnerable.\n\n"
                        "4. **The Principle of Holy Rest:** In Genesis 2:2-3, God rested on the seventh day. This Sabbath rhythm protects humanity from burnout and prevents labor from degenerating into idolatry or slavery."
                    )
                }
            }
        ],

        # Page 3: Vector SVG Diagram & Deep Dive
        [
            {
                "type": "suggested_diagram",
                "title": "Comparative Framework: Traditional African vs. Christian Teachings",
                "content": {
                    "caption": "A structured comparative vector diagram illustrating the dimensions of labor in Traditional African societies versus Christian biblical teachings.",
                    "svg_content": SVG_COMPARISON_DIAGRAM
                }
            },
            {
                "type": "concept_explanation",
                "title": "Deep Dive: Comparative Analysis of Labor Systems",
                "content": {
                    "text": (
                        "### Detailed Comparative Analysis\n\n"
                        "| Dimension | Traditional African Societies | Christian Biblical Teachings |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Primary Motivation** | Communal survival, clan solidarity, and mutual welfare. | Glorifying God, stewardship of creation, and serving neighbors. |\n"
                        "| **Remuneration / Reward** | Shared harvest, communal feast, livestock reciprocity, and social respect. | Sustaining personal/family life, charitable sharing, and eternal reward. |\n"
                        "| **Division of Labor** | Systematic division based on gender and age cohorts (e.g., boys herding, girls fetching water/cooking, elders arbitrating). | Egalitarian empowerment based on spiritual gifts and personal calling, without devaluing manual work. |\n"
                        "| **Attitude to Laziness** | Severely rebuked through ridicule, satirical songs, proverbs, and marriage disqualification. | Strongly condemned as sin; sluggards are urged to learn from the diligence of the ant. |\n"
                        "| **Rest & Renewal** | Seasonal festivals, post-harvest celebrations, and evening storytelling. | Weekly mandatory Sabbath rest (instituted by God) for spiritual worship and physical renewal. |\n\n"
                        "### Synthesis for Modern African Christians\n"
                        "Modern Kenyan learners are called to integrate the best of both heritages: upholding the African spirit of *Harambee* (pulling together) while anchoring their personal ethics in biblical integrity, diligence, and the healthy rhythm of Sabbath rest."
                    )
                }
            }
        ],

        # Page 4: Practical Application
        [
            {
                "type": "step_process",
                "title": "Framework: Cultivating Diligence and Overcoming Procrastination (The Ant's Strategy)",
                "content": {
                    "description": "A 4-step actionable framework based on Proverbs 6:6-11 to develop self-driven discipline and productive work habits.",
                    "steps": [
                        {
                            "step_number": 1,
                            "title": "Self-Initiative (No Commander Needed)",
                            "description": "Start tasks proactively without waiting for parents or teachers to remind or reprimand you. Take personal ownership of your studies and chores."
                        },
                        {
                            "step_number": 2,
                            "title": "Seasonal Foresight (Store in Summer)",
                            "description": "Plan your revision and assignments ahead of time rather than cramming the night before exams or rushing at deadlines."
                        },
                        {
                            "step_number": 3,
                            "title": "Consistent Incremental Action",
                            "description": "Break large projects into manageable daily tasks. Small, steady efforts yield immense progress, just as ants build large mounds crumb by crumb."
                        },
                        {
                            "step_number": 4,
                            "title": "Accountability and Service",
                            "description": "Evaluate your daily labor not just by personal gain, but by how your effort uplifts your family, school, and community."
                        }
                    ]
                }
            },
            {
                "type": "concept_explanation",
                "title": "Kenyan Real-World Context: Communal Work at Home and School",
                "content": {
                    "text": (
                        "### Living Out Work Ethics in Kenya Today\n\n"
                        "As a Grade 9 learner under the CBC framework, work ethics are not abstract theories—they are lived experiences:\n\n"
                        "- **At Home:** Helping with cooking, cleaning the compound, washing utensils, and tending to the kitchen garden without grumbling demonstrates stewardship and relieves pressure on parents.\n"
                        "- **At School:** Participating actively in group projects, environmental club tree planting, and maintaining classroom cleanliness reflects communal solidarity.\n"
                        "- **In the Community:** Engaging in youth community service days (*Mwethya*) reinforces the patriotic and Christian virtue of *Harambee*."
                    )
                }
            }
        ],

        # Page 5: Multimedia & Reflection
        [
            {
                "type": "suggested_video",
                "title": "BibleProject: Sabbath & The Meaning of Rest",
                "content": {
                    "youtube_id": "PFTVETgkZF8",
                    "url": "https://www.youtube.com/watch?v=PFTVETgkZF8",
                    "description": "An insightful exploration by BibleProject examining how God's rhythm of work and Sabbath rest brings liberation and purpose to human labor."
                }
            },
            {
                "type": "concept_explanation",
                "title": "Spiritual Reflection: Balancing Labor and Holy Rest",
                "content": {
                    "text": (
                        "### Reflective Meditation\n\n"
                        "Reflect on your daily schedule:\n\n"
                        "1. **Examining Idleness:** Are there areas in your life (e.g., excessive screen time, procrastination on homework, avoiding chores) where laziness is holding you back from your potential?\n"
                        "2. **Examining Overwork & Burnout:** Do you honor God's gift of rest and worship, or do you find yourself anxious and restless even on the weekend?\n\n"
                        "*\"Come to me, all you who are weary and burdened, and I will give you rest. Take my yoke upon you and learn from me, for I am gentle and humble in heart, and you will find rest for your souls.\"* — Matthew 11:28-29"
                    )
                }
            }
        ],

        # Page 6: Mastery Check
        [
            {
                "type": "summary_card",
                "title": "Key Takeaways: Importance of Work",
                "content": {
                    "points": [
                        "Work is the application of physical and mental energy to create order, sustain life, and serve the community.",
                        "Traditional African societies viewed work as a communal, sacred obligation divided by age and gender, where laziness was universally condemned.",
                        "Christian teachings establish God as the original Worker, humans as co-creators/stewards, and work as a moral necessity.",
                        "The biblical doctrine of Sabbath establishes an essential rhythm of hard labor balanced with spiritual worship and physical rest.",
                        "Learners can embody these dual heritages by practicing self-initiative, diligence, and communal service in daily life."
                    ]
                }
            },
            {
                "type": "knowledge_check",
                "title": "Topic 1 Lesson 2 Mastery Assessment",
                "content": {
                    "question": "Why did God institute the Sabbath rest on the seventh day after creating the universe (Genesis 2:1-3)?",
                    "options": [
                        "A. Because God became physically exhausted from the exertion of creation and needed sleep.",
                        "B. To establish a divine pattern balancing diligent human labor with physical, mental, and spiritual restoration.",
                        "C. Because manual labor on any day of the week is inherently corrupt and sinful.",
                        "D. To decree that human beings should cease all productive activity permanently."
                    ],
                    "correct_answer": "B",
                    "explanation": (
                        "God instituted the Sabbath not out of physical fatigue—for the Almighty does not grow faint or weary (Isaiah 40:28)—"
                        "but to set a divine model for humanity. Sabbath rest sanctifies human labor by ensuring that work does not become an "
                        "oppressive idol, providing dedicated time for spiritual communion, family bonding, and bodily rejuvenation."
                    )
                }
            }
        ]
    ]
}

def ingest_grade9_cre_topic1_lesson2(replace=True):
    print("=" * 80)
    print("INGESTING CBC GRADE 9 CRE — TOPIC 1: WORK (LESSON 2)")
    print("=" * 80)

    # 1. Resolve Grade 9 (Grade ID 18)
    grade = Grade.objects.filter(id=18).first()
    if not grade:
        grade = Grade.objects.filter(name="Grade 9", curriculum__name="CBC").first()
    if not grade:
        raise ValueError("Could not resolve Grade 9 (Grade ID 18) in database.")
    print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id})")

    # 2. Resolve Subject CRE (Subject ID 50)
    subject = Subject.objects.filter(id=50, grade=grade).first()
    if not subject:
        subject, s_created = Subject.objects.get_or_create(
            id=50,
            grade=grade,
            defaults={
                "name": "CRE",
                "description": "CBC Grade 9 Christian Religious Education"
            }
        )
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id})")

    # 3. Resolve or Create Topic 1 'Work'
    topic_description = (
        "Christian ethics regarding work, exploring God's design for human labor, traditional African perspectives, "
        "professional ethos, and contemporary workplace issues."
    )
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={
            "name": "Work",
            "description": topic_description
        }
    )
    if not t_created:
        topic.name = "Work"
        topic.description = topic_description
        topic.save()
    print(f"[*] Resolved Topic 1: {topic.name} (ID: {topic.id})")

    # Metrics
    units_created = 0
    lessons_created = 0
    pages_created = 0
    blocks_created = 0
    assets_created = 0

    with transaction.atomic():
        u_order = LESSON_DATA["unit_order"]
        u_name = LESSON_DATA["unit_name"]
        u_desc = LESSON_DATA["unit_description"]
        l_title = LESSON_DATA["lesson_title"]
        pages = LESSON_DATA["pages"]

        if replace:
            existing_units = LearningUnit.objects.filter(topic=topic, order=u_order)
            for eu in existing_units:
                existing_lessons = Lesson.objects.filter(learning_unit=eu)
                LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
                existing_lessons.delete()
            existing_units.delete()

        # Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            order=u_order,
            name=u_name,
            description=u_desc
        )
        units_created += 1

        # Create Lesson
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=l_title,
            status="published",
            version=1,
            immutable_metadata={
                "author": "VLearn Grade 9 CRE Curriculum Specialist",
                "grade": "Grade 9",
                "subject": "CRE",
                "topic_order": 1,
                "unit_order": u_order,
                "lesson_number": u_order
            }
        )
        lessons_created += 1

        block_counter = 1
        for page_idx, page_blocks in enumerate(pages, 1):
            pages_created += 1
            for block_data in page_blocks:
                b_type = block_data.get("type", "concept_explanation")
                b_title = clean_text(block_data.get("title", f"Page {page_idx} Block"))
                b_content = clean_dict(block_data.get("content", {}))

                block_type_map = {
                    "suggested_image": ("media", "suggested_image"),
                    "learning_goal": ("core", "learning_goal"),
                    "concept_explanation": ("core", "concept_explanation"),
                    "definition_card": ("core", "definition_card"),
                    "comparison_table": ("core", "comparison_table"),
                    "suggested_diagram": ("diagram", "suggested_diagram"),
                    "worked_example": ("practice", "worked_example"),
                    "suggested_video": ("media", "suggested_video"),
                    "real_world_example": ("practice", "real_world_example"),
                    "common_mistake": ("interactive", "common_mistakes"),
                    "step_process": ("practice", "guided_practice"),
                    "knowledge_check": ("assessment", "knowledge_check"),
                    "summary_card": ("core", "summary_card")
                }

                mapped_block_type, mapped_comp_type = block_type_map.get(
                    b_type, ("core", b_type)
                )

                block = LessonBlock.objects.create(
                    lesson=lesson,
                    page_number=page_idx,
                    order=block_counter,
                    block_type=mapped_block_type,
                    component_type=mapped_comp_type,
                    title=b_title,
                    content=b_content
                )
                blocks_created += 1
                block_counter += 1

                # Attach Assets
                if b_type == "suggested_diagram" and "svg_content" in b_content:
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="diagram",
                        source_type="generated",
                        storage_type="embedded",
                        status="attached",
                        title=b_title,
                        description=b_content.get("caption", b_title),
                        metadata={
                            "svg_content": b_content["svg_content"],
                            "width": "100%",
                            "height": "100%"
                        }
                    )
                    block.assets.add(asset)
                    assets_created += 1

                elif b_type == "suggested_image" and "url" in b_content:
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="image",
                        source_type="external",
                        storage_type="url",
                        status="attached",
                        title=b_title,
                        description=b_content.get("caption", b_title),
                        url=b_content["url"],
                        metadata={
                            "author": b_content.get("author", "Wikimedia Commons"),
                            "licensing": b_content.get("licensing", "CC BY-SA")
                        }
                    )
                    block.assets.add(asset)
                    assets_created += 1

                elif b_type == "suggested_video" and "youtube_id" in b_content:
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="youtube",
                        source_type="external",
                        storage_type="url",
                        status="attached",
                        title=b_title,
                        description=b_content.get("description", b_title),
                        url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                        metadata={"youtube_id": b_content["youtube_id"]}
                    )
                    block.assets.add(asset)
                    assets_created += 1

        print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print("INGESTION SUMMARY:")
    print(f"  Subject:          {subject.name} (Grade ID: {grade.id}, Subject ID: {subject.id})")
    print(f"  Topic:            {topic.name} (Order: {topic.order}, ID: {topic.id})")
    print(f"  Units Ingested:   {units_created}")
    print(f"  Lessons Ingested: {lessons_created}")
    print(f"  Pages Ingested:   {pages_created}")
    print(f"  Blocks Ingested:  {blocks_created}")
    print(f"  Assets Attached:  {assets_created}")
    print("=" * 80)

    return {
        "subject_id": subject.id,
        "subject_name": subject.name,
        "topic_id": topic.id,
        "topic_name": topic.name,
        "units": units_created,
        "lessons": lessons_created,
        "pages": pages_created,
        "blocks": blocks_created,
        "assets": assets_created
    }

if __name__ == "__main__":
    ingest_grade9_cre_topic1_lesson2()
