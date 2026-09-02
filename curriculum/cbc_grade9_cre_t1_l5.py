"""
VLearn CBC Grade 9 CRE — Strand 1.0, Sub-Strand 1.1: Work
Lesson 5: Industrial Action, Child Labor, and the Role of the Church
Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Work (ID: 316, Order: 1)
Learning Unit: 5 (Industrial Action, Child Labor, and the Role of the Church)
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal meta tags."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [193], [192, 194, 195]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION)[^\]]*\]', '', text, flags=re.IGNORECASE)
    # Normalize list bullet points
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()


def clean_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data


# ─── CUSTOM RESPONSIVE VECTOR SVG (viewBox="0 0 800 450", #0f172a theme) ─────

def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="16"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="12"/>

  <!-- Title & Subtitle Header -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE CYCLE OF CHILD LABOR VS. EDUCATED YOUTH</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Christian Social Justice &amp; Church Intervention (Deuteronomy 24:14-15 &amp; Matthew 20:1-16)</text>

  <!-- LEFT PANEL: The Vicious Cycle of Child Exploitation -->
  <g transform="translate(35, 85)">
    <!-- Header Box -->
    <rect width="320" height="42" rx="8" fill="url(#redGrad)" filter="url(#shadow)"/>
    <text x="160" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">VICIOUS CYCLE: CHILD LABOR</text>

    <!-- Cycle Body Box -->
    <rect y="50" width="320" height="235" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2"/>
    
    <!-- Stage 1 -->
    <circle cx="30" cy="80" r="14" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
    <text x="30" y="85" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
    <text x="54" y="77" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Poverty &amp; Employer Greed</text>
    <text x="54" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Family hardship + demand for cheap labor</text>

    <!-- Stage 2 -->
    <circle cx="30" cy="130" r="14" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
    <text x="30" y="135" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
    <text x="54" y="127" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Deprivation of Education</text>
    <text x="54" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Forced out of school into hazardous work</text>

    <!-- Stage 3 -->
    <circle cx="30" cy="180" r="14" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
    <text x="30" y="185" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
    <text x="54" y="177" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Physical &amp; Mental Harm</text>
    <text x="54" y="193" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Stunted development, abuse, toxic hazards</text>

    <!-- Stage 4 -->
    <circle cx="30" cy="230" r="14" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
    <text x="30" y="235" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4</text>
    <text x="54" y="227" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Generational Poverty</text>
    <text x="54" y="243" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Unskilled adulthood traps the next generation</text>
  </g>

  <!-- CENTER: Church Intervention Shield -->
  <g transform="translate(335, 125)">
    <!-- Church Intervention Box -->
    <rect width="130" height="155" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2" filter="url(#shadow)"/>
    <rect x="5" y="5" width="120" height="28" rx="6" fill="url(#goldGrad)"/>
    <text x="65" y="23" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="900" text-anchor="middle">CHURCH RESCUE</text>
    
    <text x="65" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&#10022; Rescue Centers</text>
    <text x="65" y="70" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&#10022; Free Education</text>
    <text x="65" y="88" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&#10022; Child Advocacy</text>
    <text x="65" y="106" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&#10022; Family Support</text>
    <text x="65" y="124" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&#10022; Fair Wage Defense</text>

    <!-- Transmutation Arrow Right -->
    <path d="M 135 75 L 155 75" fill="none" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
    <polygon points="155,71 165,75 155,79" fill="#10b981"/>
  </g>

  <!-- RIGHT PANEL: Virtuous Cycle of Educated Youth -->
  <g transform="translate(445, 85)">
    <!-- Header Box -->
    <rect width="320" height="42" rx="8" fill="url(#greenGrad)" filter="url(#shadow)"/>
    <text x="160" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">VIRTUOUS CYCLE: EDUCATED YOUTH</text>

    <!-- Cycle Body Box -->
    <rect y="50" width="320" height="235" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
    
    <!-- Stage 1 -->
    <circle cx="30" cy="80" r="14" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="30" y="85" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
    <text x="54" y="77" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Child Rights Protection</text>
    <text x="54" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Safe nurture, shelter, and legal defense</text>

    <!-- Stage 2 -->
    <circle cx="30" cy="130" r="14" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="30" y="135" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
    <text x="54" y="127" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Quality Basic Education</text>
    <text x="54" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Holistic CBC schooling, spiritual &amp; mental growth</text>

    <!-- Stage 3 -->
    <circle cx="30" cy="180" r="14" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="30" y="185" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
    <text x="54" y="177" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Skills &amp; Vocational Capacity</text>
    <text x="54" y="193" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Technical, academic, &amp; moral empowerment</text>

    <!-- Stage 4 -->
    <circle cx="30" cy="230" r="14" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="30" y="235" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4</text>
    <text x="54" y="227" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Self-Reliance &amp; Community Flourishing</text>
    <text x="54" y="243" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Honorable career, family stability, and dignity</text>
  </g>

  <!-- BOTTOM BAR: Industrial Action & Biblical Dispute Resolution -->
  <g transform="translate(35, 375)">
    <rect width="730" height="48" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="365" y="21" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      CHRISTIAN ETHIC ON INDUSTRIAL DISPUTES: PEACEFUL DIALOGUE &amp; FAIR LIVING WAGES
    </text>
    <text x="365" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">
      Strikes arise from injustice; resolution requires open negotiation, humane employers, and zero violence (Jeremiah 22:13).
    </text>
  </g>
</svg>"""


def ingest_grade9_cre_topic1_lesson5():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE TOPIC 1, LESSON 5: INDUSTRIAL ACTION, CHILD LABOR, AND THE ROLE OF THE CHURCH")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Scope Entities
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(id=316, subject=subject)

        print(f"Target Scope: Grade '{grade.name}' (ID: {grade.id}), Subject '{subject.name}' (ID: {subject.id}), Topic '{topic.name}' (ID: {topic.id})")

        # 2. Setup / Clean Learning Unit 5
        unit_order = 5
        unit_name = "Industrial Action, Child Labor, and the Role of the Church"
        unit_description = (
            "Explore Christian teachings on wages, analyze the causes and consequences of industrial action (strikes), "
            "examine the destructive effects of child labor, and evaluate the Church's active role in defending vulnerable children "
            "and mediating labor justice."
        )

        # Remove existing Unit 5 if present to allow clean idempotent re-ingestion
        existing_units = LearningUnit.objects.filter(topic=topic, order=unit_order)
        for eu in existing_units:
            print(f"[-] Cleaning up existing LearningUnit {eu.id} ('{eu.name}')")
            for les in eu.lessons.all():
                les.blocks.all().delete()
                les.assets.all().delete()
                les.delete()
            eu.delete()

        unit = LearningUnit.objects.create(
            topic=topic,
            order=unit_order,
            name=unit_name,
            description=clean_text(unit_description)
        )
        print(f"[+] Created LearningUnit {unit.id} (Order: {unit.order}, Name: '{unit.name}')")

        # 3. Create Published Lesson
        lesson_title = "Industrial Action, Child Labor, and the Role of the Church"
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=lesson_title,
            status="published",
            version=1,
            immutable_metadata={
                "grade": "Grade 9",
                "grade_id": 18,
                "subject": "CRE",
                "subject_id": 50,
                "topic_order": 1,
                "topic_id": 316,
                "topic_name": topic.name,
                "unit_order": unit_order,
                "author": "VLearn CRE Ingestion Agent",
                "curriculum_framework": "CBC Kenya",
                "enrichment_version": "v3_pedagogical"
            }
        )
        print(f"[+] Created Lesson {lesson.id} ('{lesson.title}') [status={lesson.status}]")

        # 4. Create 3 LessonAssets
        # Asset 1: Authentic Wikimedia Image Hook
        img_info = {
            "title": "Kenyan Samburu Children in a Classroom Setting",
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Kenyan_Samburu_children_in_a_classroom.jpg",
            "caption": "Access to quality education is the fundamental right of every child. Protecting children from hazardous labor empowers them to break generational poverty and flourish.",
            "author": "Moses Mwombe / Wikimedia Commons (Wiki Loves Africa 2019)",
            "licensing": "Creative Commons Attribution-Share Alike 4.0 International (CC BY-SA 4.0)",
            "source": "Wikimedia Commons"
        }
        img_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            source_type="external",
            storage_type="url",
            status="attached",
            title=clean_text(img_info["title"]),
            description=clean_text(img_info["caption"]),
            url=img_info["url"],
            metadata={
                "author": img_info["author"],
                "licensing": img_info["licensing"],
                "source": img_info["source"],
                "caption": clean_text(img_info["caption"])
            }
        )

        # Asset 2: Pedagogical Vector SVG Diagram
        svg_content = get_svg_lesson_5()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="url",
            status="attached",
            title=f"Diagram: {lesson_title}",
            description="Responsive pedagogical vector SVG diagram illustrating the Cycle of Child Labor vs. Educated Youth and the Church's Intervention.",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic1_lesson_5.svg",
            metadata={
                "svg_xml": svg_content,
                "viewBox": "0 0 800 450",
                "theme": "#0f172a"
            }
        )

        # Asset 3: Curated Educational YouTube Video
        yt_info = {
            "title": "BibleProject: Generosity (Overcoming Greed & Cultivating Economic Justice)",
            "youtube_id": "62CliEkRCso",
            "description": "Explore how God's abundant generosity overcomes human selfishness, greed, and exploitation in economic relationships and work."
        }
        yt_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="youtube",
            source_type="external",
            storage_type="url",
            status="attached",
            title=clean_text(yt_info["title"]),
            description=clean_text(yt_info["description"]),
            url=f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
            metadata={
                "youtube_id": yt_info["youtube_id"],
                "embed_url": f"https://www.youtube.com/embed/{yt_info['youtube_id']}"
            }
        )
        print(f"[+] Created 3 LessonAssets: Image, SVG Diagram, and YouTube Video")

        # 5. Create 6 Pages with Structured Blocks

        # ───────────────────────────────────────────────────────────────────
        # CARD 1 (Page 1): Discovery & Objectives (3 blocks)
        # ───────────────────────────────────────────────────────────────────
        b1 = LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=10, component_order=1,
            block_type="suggested_image", component_type="suggested_image",
            title=clean_text(img_info["title"]),
            content={
                "title": clean_text(img_info["title"]),
                "url": img_info["url"],
                "resolved_image_url": img_info["url"],
                "caption": clean_text(img_info["caption"]),
                "author": img_info["author"],
                "licensing": img_info["licensing"],
                "source": img_info["source"]
            }
        )
        b1.assets.add(img_asset)

        goals_data = [
            {
                "level": "Remembering & Understanding",
                "description": "Define industrial action, strikes, fair wages, and child labor, and state the biblical basis for honoring labor contracts and protecting children."
            },
            {
                "level": "Analyzing & Evaluating",
                "description": "Analyze the underlying causes and socio-economic consequences of labor strikes and the harmful developmental impacts of child labor."
            },
            {
                "level": "Applying & Creating",
                "description": "Apply Christian values of justice, peace, and compassionate advocacy to propose constructive conflict-resolution mechanisms and protect vulnerable children in Kenya."
            }
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=20, component_order=2,
            block_type="learning_goal", component_type="learning_goal",
            title="Lesson Objectives",
            content={"goals": clean_dict(goals_data)}
        )

        intro_text = """### The Cry for Fair Wages and the Protection of the Vulnerable

Imagine working under the scorching sun for ten hours harvesting tea leaves or laying bricks, only to be told at sunset that your employer will pay you half the promised amount—or nothing at all. Or picture a thirteen-year-old child carrying heavy sacks of quarry stones instead of sitting in a classroom preparing for their future.

These harsh realities highlight two major ethical challenges in the world of work:
1. **Labor Disputes and Industrial Action:** When workers are denied fair living wages or subjected to dangerous conditions, frustration boils over into work stoppages and strikes.
2. **Child Labor and Exploitation:** When poverty and greed rob boys and girls of their childhood and education, trapping them in exhausting manual labor.

In Christian Religious Education, we examine work through the lens of God's justice (*Mishpat*). The Bible is clear that withholding wages is a severe sin, and that children are precious gifts from God who must be protected, nurtured, and educated. In this lesson, we explore how Christian principles and the active ministry of the Church bring healing, justice, and peace to labor disputes and vulnerable communities."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=30, component_order=3,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Introduction: Labor Injustice and Child Exploitation",
            content={"markdown": clean_text(intro_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis & Theological Foundations (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        scripture_text = """### Scriptural Foundations: God's Defense of Workers and Children

God's Word sets absolute standards of fairness for employers and calls society to guard children with tender care:

#### 1. Deuteronomy 24:14-15 — The Law of Prompt Daily Wages
> *"Do not take advantage of a hired worker who is poor and needy, whether that worker is a fellow Israelite or a foreigner residing in one of your towns. Pay them their wages each day before sunset, because they are poor and are counting on it. Otherwise they may cry to the Lord against you, and you will be guilty of sin."*

#### 2. Jeremiah 22:13 — Divine Judgment on Unjust Employers
> *"Woe to him who builds his palace by unrighteousness, his upper rooms by injustice, making his own people work for nothing, not paying them for their labor."*

#### 3. Matthew 20:1-16 — The Parable of the Workers in the Vineyard
> *"Take your pay and go. I want to give the one who was hired last the same as I gave you. Don’t I have the right to do what I want with my own money? Or are you envious because I am generous? So the last will be first, and the first will be last."*

#### 4. Ephesians 6:4 & Matthew 18:6 — Nurturing and Protecting Children
> *"Fathers, do not exasperate your children; instead, bring them up in the training and instruction of the Lord."* (Ephesians 6:4)
> *"If anyone causes one of these little ones—those who believe in me—to stumble, it would be better for them to have a large millstone hung around their neck and to be drowned in the depths of the sea."* (Matthew 18:6)"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Core Biblical Scriptures on Wages and Children",
            content={"markdown": clean_text(scripture_text)}
        )

        theological_exegesis_text = """### Theological Exegesis: Justice, Contractual Integrity, and Christ's Heart for Children

An in-depth theological analysis of these scriptures reveals three foundational pillars of Christian labor ethics:

- **1. The Sacred Right to Prompt Remuneration (Deut 24:14-15, Jer 22:13):**
  In the Old Testament economy, casual day-laborers lived from hand to mouth. Delaying payment until the next morning meant a family went to bed hungry. The Torah declared that an unpaid laborer's cry goes directly to God (*Yahweh*), who personally adjudicates their case. Jeremiah pronounces "Woe" (*a prophetic declaration of doom*) against rulers who build lavish estates by withholding wages from builders.

- **2. Sovereign Generosity and Contractual Honesty (Matthew 20:1-16):**
  In the Parable of the Workers in the Vineyard, the landowner fulfills his agreed contract (one denarius) with the early workers while extending radical generosity to those who found work only at the eleventh hour. The parable teaches that God respects just contracts while modeling compassion for those who are disadvantaged in the economic marketplace.

- **3. The Sanctity and Inherent Dignity of Children (Ephesians 6:4, Matthew 18:6):**
  In Graeco-Roman and ancient Near Eastern cultures, children were often treated as economic commodities or disposable labor. Jesus radically overturned this view, identifying Himself with children and issuing severe warnings against anyone who harms or exploits them. Christian theology affirms that childhood is a sacred period for spiritual nurture, moral formation, and schooling—not hazardous economic exploitation."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Analysis: Prophetic Justice & Child Protection",
            content={"markdown": clean_text(theological_exegesis_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 3 (Page 3): Vector SVG Diagram & Deep Dive (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        b5 = LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
            order=50, component_order=1,
            block_type="suggested_diagram", component_type="suggested_diagram",
            title=f"Visual Architecture: {lesson_title}",
            content={
                "title": "The Cycle of Child Labor vs. Educated Youth & Church Intervention",
                "caption": "A structured vector diagram illustrating how the Church breaks the generational trap of child labor by providing rescue, basic education, and advocacy.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        deep_dive_text = """### In-Depth Analysis: Industrial Disputes, Child Exploitation, and Church Action

#### 1. Wages and Industrial Action (Strikes)
- **Understanding Wages:** A wage is legitimate financial compensation earned for physical or intellectual labor. Scripture upholds that workers are worthy of their wages (1 Timothy 5:18, Luke 10:7).
- **Causes of Industrial Strikes:**
  - Inadequate remuneration failing to match the rising cost of living.
  - Delayed payment or unjust salary deductions by management.
  - Unsafe, hazardous, or unsanitary working conditions.
  - Disregard of collective bargaining agreements (CBAs) and lack of respect for employee grievances.
- **Consequences of Strikes:**
  - Severe financial losses for businesses and disruption of public services (e.g., healthcare, education, transport).
  - Loss of income, dismissals, or victimisation of striking workers.
  - Risk of violence, vandalism, police confrontation, injuries, or loss of life.
- **The Christian Response to Strikes:**
  Christianity teaches that conflict is inevitable, but violence is never the solution. Employers must be humane, just, and willing to negotiate in good faith. Workers must exercise patience, maintain open dialogue, and protect company property without resorting to sabotage.

#### 2. The Scourge of Child Labor
Child labor is defined as work that deprives children of their childhood, potential, and dignity, and that is harmful to their physical and mental development.
- **Root Causes:** Household poverty, loss of parents (orphanhood), domestic instability, breakdown of family values, and unscrupulous employers seeking cheap, docile labor.
- **Destructive Effects:**
  - **Educational Loss:** Immediate school dropout, leading to lifelong illiteracy and lack of professional skills.
  - **Physical Hazards:** Exposure to toxic chemicals on agricultural estates, respiratory illnesses in mines/quarries, physical deformities, and chronic exhaustion.
  - **Psychological Trauma:** Emotional abuse, sexual exploitation, fear, and loss of self-worth.
  - **Generational Poverty Trap:** Uneducated children become low-income adults unable to educate their own children.

#### 3. The Multi-Pronged Response of the Church
The Church functions as the prophetic conscience of society in defending children and advocating for labor justice:
- **Direct Rescue and Care:** Establishing rescue centers, children's homes, and orphanages providing food, clothing, shelter, and medical care.
- **Education Provision:** Building and managing primary, secondary, and vocational training institutions offering free or subsidized education.
- **Family Empowerment:** Providing micro-finance initiatives, agricultural training, and pastoral counseling to strengthen vulnerable families.
- **Public Advocacy & Policy:** Lobbying legislative bodies to enact and enforce strict child protection laws and championing fair minimum wage regulations."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Comprehensive Breakdown: Industrial Action & Child Labor",
            content={"markdown": clean_text(deep_dive_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 4 (Page 4): Practical Application & Kenyan Context (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        practical_framework = {
            "title": "4-Step Christian Framework for Conflict Resolution & Child Protection",
            "description": "A biblical and civic action pathway for resolving labor disputes peacefully and safeguarding vulnerable children.",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Identify Injustice & Protect the Vulnerable First",
                    "description": "Assess the situation objectively. If children are involved in hazardous work, remove them from harm immediately and ensure their safety, nutrition, and urgent physical care."
                },
                {
                    "step_number": 2,
                    "name": "Initiate Honest & Constructive Dialogue",
                    "description": "In workplace disputes, bring employers and workers to a round table. Present factual grievances calmly without threats, seeking win-win solutions that preserve human dignity."
                },
                {
                    "step_number": 3,
                    "name": "Engage Official Mediation & Civic Reporting Channels",
                    "description": "Involve neutral arbitrators (labor officers, union representatives, or church elders). Report child labor exploitation to national authorities via Childline 116 or local chiefs."
                },
                {
                    "step_number": 4,
                    "name": "Establish Long-Term Restoration & Empowerment",
                    "description": "Enroll rescued children into schools or vocational polytechnics. Provide social and spiritual support to families to prevent relapse into economic desperation."
                }
            ]
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=70, component_order=1,
            block_type="step_process", component_type="step_process",
            title="Practical Action Framework: Resolving Conflict & Guarding Children",
            content=clean_dict(practical_framework)
        )

        kenyan_context_text = """### Kenyan Real-World Application: Child Protection Laws & Civic Duty

In Kenya, both national law and Christian institutions work actively to eliminate child labor and ensure industrial peace:

1. **Constitutional & Legal Protections in Kenya:**
   - **The Constitution of Kenya (Article 53):** Guarantees every child the right to free and compulsory basic education, protection from abuse, neglect, harmful cultural practices, and all forms of hazardous or exploitative labor.
   - **The Children Act (2022):** Sets the minimum age of general employment at 16 years, strictly criminalizing child labor, human trafficking, and engagement in hazardous work (e.g., quarries, commercial agriculture, night shifts, and bars).

2. **National Reporting Channels — Childline 116:**
   - Any citizen or student who identifies a child being denied education, forced into domestic servitude, or working in harsh conditions can call the **Toll-Free National Child Helpline: 116**.
   - Cases can also be reported to local Area Advisory Councils (AAC), Chiefs, Children's Officers, or nearest police stations.

3. **Church Rescue Centers and Community Advocacy:**
   - Denominational bodies across Kenya (e.g., Catholic Church, ACK, PCEA, AIC, Baptist, and Salvation Army) operate hundreds of children's rescue homes, sponsorship programs, and vocational training centers.
   - Christians are called to be active whistleblowers against child exploitation in their neighborhoods, farms, and market centers."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=75, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Kenyan Real-World Context: Laws, Childline 116 & Church Action",
            content={"markdown": clean_text(kenyan_context_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 5 (Page 5): Multimedia & Reflection (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        b8 = LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
            order=80, component_order=1,
            block_type="suggested_video", component_type="suggested_video",
            title=clean_text(yt_info["title"]),
            content={
                "title": clean_text(yt_info["title"]),
                "url": f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                "youtube_id": yt_info["youtube_id"],
                "description": clean_text(yt_info["description"])
            }
        )
        b8.assets.add(yt_asset)

        reflection_text = """### Personal Spiritual Reflection: The Call to Compassion and Justice

Take time to reflect on your attitude toward resources, fairness, and the vulnerable in your community:

- **Examining Greed vs. Compassion:**
  Why do some business owners choose to hire cheap child laborers instead of paying fair wages to adult breadwinners? It stems from greed—the selfish desire to maximize profits at the expense of human dignity. How does Jesus' teaching on love and generosity challenge this selfish mindset?

- **Your Role as an Advocate:**
  Do you know children in your village, estate, or neighborhood who are missing school to sell groundnuts, herd cattle, or work as domestic househelps? What step can you take to speak up for their rights?

> **Prayer for Workers and Vulnerable Children:**
> *"Heavenly Father, You are the defender of the poor and the protector of little children. Grant our leaders and employers hearts of justice, that they may pay honest wages and treat workers fairly. We pray for all children trapped in harsh labor; rescue them through Your Church and provide them with education, joy, and hope. Amen."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
            order=90, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Spiritual Reflection & Ethical Examination",
            content={"markdown": clean_text(reflection_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 6 (Page 6): Review & Mastery Check (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        takeaways_data = [
            "Workers have a biblical right to receive just, timely living wages without delay or unfair deduction (Deuteronomy 24:14-15, Jeremiah 22:13).",
            "Industrial strikes are work stoppages caused by poor wages, unsafe conditions, and broken agreements; Christians advocate for peaceful dialogue and fair mediation to prevent violence.",
            "Child labor violates children's fundamental rights to education, health, and dignity, exposing them to physical harm and trapping them in generational poverty.",
            "The Church actively condemns child labor, establishes rescue homes and schools, and lobbies for child protection policies.",
            "Under the Constitution of Kenya (Article 53) and Children Act (2022), child exploitation is illegal and can be reported toll-free via Childline 116."
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title="Review & Knowledge Check",
            order=100, component_order=1,
            block_type="summary", component_type="summary",
            title="Summary & Key Takeaways",
            content={
                "title": f"Key Takeaways: {lesson_title}",
                "takeaways": clean_dict(takeaways_data)
            }
        )

        mcq_data = {
            "question": "According to Christian teachings (Deuteronomy 24:14-15, Jeremiah 22:13) and modern labor ethics, what is the most appropriate Christian approach to resolving labor disputes and preventing strikes?",
            "options": [
                {
                    "label": "A",
                    "text": "Encouraging striking workers to vandalize company machinery to compel employers to raise salaries immediately."
                },
                {
                    "label": "B",
                    "text": "Dismissing all protesting employees and replacing them with cheaper, unrepresented child laborers."
                },
                {
                    "label": "C",
                    "text": "Engaging in honest, peaceful dialogue and fair mediation, ensuring timely living wages without violence or destruction."
                },
                {
                    "label": "D",
                    "text": "Ignoring employee grievances completely until workers run out of savings and abandon the industrial strike."
                }
            ],
            "correct_answer": "C",
            "explanation": "Option C is correct. Christianity advocates for peace, fairness, open communication, and just living wages to resolve workplace conflicts constructively (Jeremiah 22:13, Deuteronomy 24:14-15). Options A, B, and D violate biblical justice, promote violence, exploit vulnerable individuals, or exacerbate societal strife."
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title="Review & Knowledge Check",
            order=110, component_order=2,
            block_type="knowledge_check", component_type="knowledge_check",
            title="Formative Knowledge Check",
            content=clean_dict(mcq_data)
        )

        # 6. Verification and Summary
        blocks_count = lesson.blocks.count()
        assets_count = lesson.assets.count()
        pages = lesson.blocks.values_list('page_number', flat=True).distinct().count()

        print("=" * 80)
        print("INGESTION COMPLETED SUCCESSFULLY!")
        print(f"  - Curriculum: {grade.curriculum.name} (Grade: {grade.name}, Level: {grade.level})")
        print(f"  - Subject   : {subject.name} (ID: {subject.id})")
        print(f"  - Topic     : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  - Unit      : {unit.name} (ID: {unit.id}, Order: {unit.order})")
        print(f"  - Lesson    : {lesson.title} (ID: {lesson.id}, Status: {lesson.status})")
        print(f"  - Pages     : {pages}")
        print(f"  - Blocks    : {blocks_count}")
        print(f"  - Assets    : {assets_count}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_cre_topic1_lesson5()

