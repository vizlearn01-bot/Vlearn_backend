"""
VLearn CBC Grade 9 CRE — Strand 1.0, Sub-Strand 1.1: Work
Lesson 6: Unemployment and Self-Employment
Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Work (ID: 316, Order: 1)
Learning Unit: 6 (Unemployment and Self-Employment)
"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

# Setup Django Environment
BASE_DIR = Path("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
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
    """Removes bracket citations and internal meta tags."""
    if not text:
        return ""
    # Strip bracket citations e.g. [198], [199], [199, 200, 201]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(
        r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION)[^\]]*\]',
        '', text, flags=re.IGNORECASE
    )
    # Normalize list bullet points
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
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


# ─── CUSTOM RESPONSIVE VECTOR SVG (viewBox="0 0 800 450", #0f172a theme) ─────

def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="trapGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b91c1c"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
    <linearGradient id="bridgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
    <linearGradient id="ventureGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadowGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Frame -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="16"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="12"/>

  <!-- Title & Subtitle Header -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">OVERCOMING UNEMPLOYMENT: THE PARADIGM SHIFT</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">From the White-Collar Bottleneck to Faith-Driven Entrepreneurial Self-Reliance</text>

  <!-- LEFT COLUMN: THE WHITE-COLLAR BOTTLENECK -->
  <g transform="translate(35, 88)">
    <rect width="220" height="36" rx="8" fill="url(#trapGrad)"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. WHITE-COLLAR BOTTLENECK</text>

    <!-- Card Body -->
    <rect y="44" width="220" height="236" rx="8" fill="url(#cardGrad)" stroke="#ef4444" stroke-width="1.2" filter="url(#shadowGlow)"/>
    <text x="12" y="70" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Obstacles &amp; Mental Trap</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• High graduate dependency</text>
    <text x="12" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Limited office vacancies</text>
    <text x="12" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Stigma against manual trades</text>
    <text x="12" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Nepotism &amp; unfair barriers</text>
    <text x="12" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Prolonged youth idleness</text>
    
    <rect x="10" y="195" width="200" height="70" rx="6" fill="#450a0a" stroke="#991b1b" stroke-width="1"/>
    <text x="100" y="215" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Proverbs 14:23 Warning</text>
    <text x="100" y="235" fill="#fecaca" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"Mere talk leads only to</text>
    <text x="100" y="250" fill="#fecaca" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">poverty &amp; regret."</text>
  </g>

  <!-- MIDDLE COLUMN: THE TRANSFORMATION BRIDGE (CHURCH & SKILLS) -->
  <g transform="translate(290, 88)">
    <rect width="220" height="36" rx="8" fill="url(#bridgeGrad)"/>
    <text x="110" y="23" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2. THE EMPOWERMENT BRIDGE</text>

    <!-- Card Body -->
    <rect y="44" width="220" height="236" rx="8" fill="url(#cardGrad)" stroke="#f59e0b" stroke-width="1.2" filter="url(#shadowGlow)"/>
    <text x="12" y="70" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Enabling Ecosystem</text>
    <text x="12" y="92" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="10.5">• Church TVET polytechnics</text>
    <text x="12" y="112" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="10.5">• Technical &amp; artisan skills</text>
    <text x="12" y="132" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="10.5">• Seed grants &amp; table banking</text>
    <text x="12" y="152" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="10.5">• Christian work ethic (1 Thess)</text>
    <text x="12" y="172" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="10.5">• Mentorship &amp; resilience</text>

    <rect x="10" y="195" width="200" height="70" rx="6" fill="#451a03" stroke="#b45309" stroke-width="1"/>
    <text x="100" y="215" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1 Thessalonians 4:11-12</text>
    <text x="100" y="235" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"Work with your own hands</text>
    <text x="100" y="250" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">and win respect of outsiders."</text>
  </g>

  <!-- RIGHT COLUMN: SUSTAINABLE SELF-EMPLOYMENT -->
  <g transform="translate(545, 88)">
    <rect width="220" height="36" rx="8" fill="url(#ventureGrad)"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. SELF-EMPLOYED FLOURISHING</text>

    <!-- Card Body -->
    <rect y="44" width="220" height="236" rx="8" fill="url(#cardGrad)" stroke="#10b981" stroke-width="1.2" filter="url(#shadowGlow)"/>
    <text x="12" y="70" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Enterprise Outcomes</text>
    <text x="12" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Financial independence</text>
    <text x="12" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Jua Kali &amp; Agribusiness hubs</text>
    <text x="12" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Local job creator for peers</text>
    <text x="12" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Creative talent stewardship</text>
    <text x="12" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Community transformation</text>

    <rect x="10" y="195" width="200" height="70" rx="6" fill="#064e3b" stroke="#059669" stroke-width="1"/>
    <text x="100" y="215" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Ecclesiastes 11:6</text>
    <text x="100" y="235" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"Sow seed morning and evening;</text>
    <text x="100" y="250" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">you know not which will succeed."</text>
  </g>

  <!-- Flow Arrows connecting columns -->
  <path d="M 260 200 L 285 200" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="285,195 292,200 285,205" fill="#38bdf8"/>
  <path d="M 515 200 L 540 200" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="540,195 547,200 540,205" fill="#38bdf8"/>

  <!-- Bottom Core Takeaway Banner -->
  <rect x="35" y="380" width="730" height="42" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="400" y="406" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    CBC Insight: Dignity in manual labor, practical TVET training, and innovative entrepreneurship overcome youth joblessness.
  </text>
</svg>"""


def ingest_grade9_cre_topic1_lesson6():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE TOPIC 1, LESSON 6: UNEMPLOYMENT AND SELF-EMPLOYMENT")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Scope Entities
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(id=316, subject=subject)

        print(f"Target Scope: Grade '{grade.name}' (ID: {grade.id}), Subject '{subject.name}' (ID: {subject.id}), Topic '{topic.name}' (ID: {topic.id})")

        # 2. Setup / Clean Learning Unit 6
        unit_order = 6
        unit_name = "Unemployment and Self-Employment"
        unit_description = (
            "Examine the causes and challenges of youth unemployment in contemporary Kenya, theological insights "
            "from Christian scripture on work ethic, diligence, and enterprise diversification (Proverbs 14:23, "
            "1 Thessalonians 4:11-12, Ecclesiastes 11:6), and the practical virtues, benefits, and steps for launching "
            "sustainable self-employment micro-enterprises."
        )

        # Remove existing Unit 6 if present to allow clean idempotent re-ingestion
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
        lesson_title = "Unemployment and Self-Employment"
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
            "title": "A Young Kenyan Artisan at Work in the Jua Kali Sector",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Welder_in_Kenya.jpg/800px-Welder_in_Kenya.jpg",
            "caption": "A skilled young Kenyan welder in the vibrant Jua Kali sector turning raw materials into marketable household goods—embodying self-reliance, manual dignity, and economic resilience.",
            "author": "Wikimedia Commons / Africa Renewal",
            "licensing": "CC BY-SA 4.0 / Public Domain",
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
        svg_content = get_svg_lesson_6()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="url",
            status="attached",
            title=f"Diagram: {lesson_title}",
            description="Responsive pedagogical vector SVG diagram illustrating the paradigm shift from the white-collar job bottleneck to entrepreneurial self-employment.",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic1_lesson_6.svg",
            metadata={
                "svg_xml": svg_content,
                "viewBox": "0 0 800 450",
                "theme": "#0f172a"
            }
        )

        # Asset 3: Curated Educational YouTube Video
        yt_info = {
            "title": "BibleProject: Proverbs (Wisdom and the Blessing of Diligent Labor)",
            "youtube_id": "AzmYV8GNDPE",
            "description": "Explore the book of Proverbs and how biblical wisdom celebrates hard work, creativity, and self-reliance while warning against the trap of idleness."
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
                "description": "Explain the causes and socio-economic consequences of unemployment and define self-employment within the Kenyan economic context."
            },
            {
                "level": "Analyzing & Evaluating",
                "description": "Critically analyze biblical scriptures (Proverbs 14:23, 1 Thessalonians 4:11-12, Ecclesiastes 11:6) to evaluate traditional mindsets that favor white-collar jobs over practical manual trades."
            },
            {
                "level": "Applying & Creating",
                "description": "Design a viable, integrity-based micro-enterprise project applying practical vocational skills, diversification, and Christian principles of stewardship."
            }
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=20, component_order=2,
            block_type="learning_goal", component_type="learning_goal",
            title="Lesson Objectives",
            content={"goals": clean_dict(goals_data)}
        )

        intro_text = """### Beyond the Office Desk: Embracing the Dignity of Self-Employment

Have you ever heard a school leaver or university graduate say, *"I am still waiting at home for a real office job with an air-conditioned desk and a computer"*? 

Across Kenya and East Africa, many young people spend years in unproductive idleness because of a deep-seated cultural misconception: the belief that only "white-collar" corporate or civil service employment is prestigious and honorable. Meanwhile, some of the most self-reliant, prosperous, and influential individuals in our communities are those who chose a different path—skilled artisans, bakers, tech freelancers, modern agribusiness farmers, solar installers, and fashion designers in the vibrant **Jua Kali** and SME sectors.

Self-employment is an economic activity initiated, owned, and actively driven by an individual. It transforms a person from being a passive job seeker into an empowered **job creator**. In Christian Religious Education, we discover that God did not create human beings to sit in passive helplessness. When we use our hands, intellect, and creativity to produce goods and provide essential services, we actively mirror the character of God our Creator, overcome the scourge of joblessness, and build resilient communities."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=30, component_order=3,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Introduction: Breaking the White-Collar Mindset",
            content={"markdown": clean_text(intro_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis & Theological Foundations (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        scripture_text = """### Scriptural Foundations: Biblical Wisdom on Industry and Initiative

The Bible directly confronts idleness, celebrates manual and artisanal labor, and provides wise counsel on entrepreneurial enterprise:

#### 1. Proverbs 14:23 — The Contrast Between Diligence and Idle Talk
> *"All hard work brings a profit, but mere talk leads only to poverty."*

#### 2. 1 Thessalonians 4:11-12 — Honorable Manual Labor and Independence
> *"Make it your ambition to lead a quiet life: You should mind your own business and work with your hands, just as we told you, so that your daily life may win the respect of outsiders and so that you will not be dependent on anybody."*

#### 3. Ecclesiastes 11:6 — Enterprise Diversification and Persistent Effort
> *"Sow your seed in the morning, and at evening let your hands not be idle, for you do not know which will succeed, whether this or that, or whether both will do equally well."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Core Biblical Texts on Work and Enterprise",
            content={"markdown": clean_text(scripture_text)}
        )

        theological_exegesis_text = """### Theological Exegesis: Diligence, Manual Dignity, and Diversification

An in-depth study of these scriptures reveals three foundational pillars of Christian work theology:

- **Action vs. Empty Ambition (Proverbs 14:23):**
  Wise King Solomon highlights a common human weakness: spending hours discussing grand business ideas, lamenting poor economic conditions, or daydreaming about wealth without taking concrete action. Scripture warns that *mere words* yield zero return and lead to poverty. In contrast, even modest, unglamorous physical or technical labor (*all hard work*) generates tangible value, profit, and dignity.

- **The Sanctity and Autonomy of Manual Labor (1 Thessalonians 4:11-12):**
  Writing to the young church in Thessalonica—where some believers had stopped working under the mistaken excuse of waiting for Christ's return—the Apostle Paul commanded them to work diligently with their hands. Paul himself worked as a self-employed tentmaker (Acts 18:3) to support his ministry without burdening others. Christian self-employment wins the moral respect of the community and delivers believers from humiliating economic dependency.

- **Strategic Diversification and Risk-Taking (Ecclesiastes 11:6):**
  Ecclesiastes provides brilliant financial and agricultural insight: entrepreneurial success requires relentless industry from morning to evening and multi-stream diversification. Because human beings cannot predict market shifts or weather patterns with certainty, the self-employed Christian spreads their efforts across viable opportunities rather than relying on a single fragile source of income."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Analysis: Diligence, Dignity & Diversification",
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
                "title": "Overcoming Unemployment: White-Collar Trap vs. Self-Employment",
                "caption": "A structured vector diagram contrasting the white-collar job bottleneck with church-supported TVET skills training and flourishing entrepreneurial self-reliance.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        deep_dive_text = """### In-Depth Analysis: Causes, Church Responses, and Self-Employment Realities

#### 1. Understanding Unemployment & Its Structural Causes
Unemployment occurs when individuals who are able, qualified, and actively willing to work cannot secure viable employment or productive economic livelihood. Major causes include:
- **Prejudice Against Manual and Technical Trades:** A widespread social bias that glorifies white-collar desk jobs and looks down on agriculture, masonry, plumbing, and mechanical repairs.
- **Corruption, Nepotism, and Bribery:** Unethical hiring practices where positions are awarded to unqualified relatives or those who pay bribes, locking out deserving candidates.
- **Mismatch of Educational Skills:** Curricula that historically focused on theoretical academic degrees rather than hands-on vocational and entrepreneurial competencies.
- **Unequal Distribution of Resources & Rural-Urban Migration:** Concentration of industries in major urban centers (Nairobi, Mombasa, Kisumu), causing rural youth to migrate into urban joblessness.
- **Lack of Seed Capital & Credit Access:** High interest rates and collateral requirements from financial institutions that prevent innovative youth from launching ventures.

#### 2. The Christian Response and Church Initiatives
Christianity strongly condemns **idleness** and passive hopelessness (2 Thessalonians 3:10: *"The one who is unwilling to work shall not eat"*). The Church responds proactively by:
- **Establishing TVET & Vocational Training Centers:** Founding village polytechnics, technical institutes, and craft training centers (carpentry, tailoring, welding, agriculture, ICT).
- **Providing Micro-Finance & Table Banking:** Creating SACCOs, revolving seed funds, and church-based credit groups that provide youth with low-interest startup capital.
- **Promoting Agricultural Stewardship:** Training youth in sustainable horticultural farming, poultry keeping, and modern greenhouse technology.
- **Advocating for Fair Governance:** Speaking out against public corruption, resource mismanagement, and demanding fair economic policies from national leaders.

#### 3. Benefits and Challenges of Self-Employment
- **Benefits:**
  - **Self-Reliance and Autonomy:** You are your own manager, controlling your working hours and directly determining your profit margins.
  - **Expression of God-Given Gifts:** Provides unlimited creative freedom to innovate and solve immediate community problems.
  - **Job Creation for Others:** As the enterprise grows, it absorbs unemployed peers, multiplying societal well-being.
- **Challenges:**
  - **Capital Constraints:** Difficulty securing initial machinery, workspace, and operating inventory.
  - **Market Competition & High Taxes:** Rivalry with mass-produced imports and navigating municipal business licenses.
  - **Fluctuating Income:** Irregular revenue during low seasons requiring strict budgeting and financial discipline."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Comprehensive Breakdown: Causes, Church Action & Enterprise Realities",
            content={"markdown": clean_text(deep_dive_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 4 (Page 4): Practical Application & Kenyan Context (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        practical_framework = {
            "title": "Youth Micro-Enterprise Launch Framework",
            "description": "A 4-stage practical framework for young Christian entrepreneurs to initiate, sustain, and grow a micro-enterprise with integrity.",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Identify Local Needs & God-Given Talents",
                    "description": "Survey your neighborhood to discover unmet needs (e.g. fresh organic vegetables, mobile phone repairs, bakery snacks, shoe shining, hair braiding). Match the need with your existing practical skills and talents."
                },
                {
                    "step_number": 2,
                    "name": "Low-Cost Bootstrapping & Resource Mobilization",
                    "description": "Start small using available resources at home or joining family table-banking (chamas). Avoid heavy initial debt by reinvesting sweat equity, using borrowed tools, and launching from a kitchen garden or home workshop."
                },
                {
                    "step_number": 3,
                    "name": "Deliver Quality, Fair Pricing & Christian Integrity",
                    "description": "Build unwavering customer trust by delivering top-quality goods, maintaining honest weights and measures (Proverbs 11:1), respecting customer time, and providing excellent after-sales service."
                },
                {
                    "step_number": 4,
                    "name": "Financial Record-Keeping, Reinvestment & Persistence",
                    "description": "Keep meticulous records of income and expenses. Separate business capital from personal pocket money, save systematically, reinvest profits to expand operations, and persevere through tough initial seasons."
                }
            ]
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=70, component_order=1,
            block_type="step_process", component_type="step_process",
            title="Framework: 4 Steps for Youth to Launch a Micro-Enterprise",
            content=clean_dict(practical_framework)
        )

        kenyan_context_text = """### Kenyan Real-World Context: TVETs, Jua Kali & Youth Agribusiness

Kenya's economic landscape offers unprecedented opportunities for youth who embrace practical skills and entrepreneurship:

1. **The TVET Revolution in Kenya:**
   The Kenyan government and church bodies have heavily invested in Technical and Vocational Education and Training (TVET) institutions across all 47 counties. Young people are mastering mechatronics, electrical wiring, plumbing, culinary arts, fashion design, and digital software development, leading directly to self-employment and high-demand contracting.

2. **The Jua Kali Sector as an Economic Engine:**
   The informal Jua Kali (literally *"under the hot sun"*) sector employs millions of Kenyans and accounts for over 80% of new jobs created annually. From metal fabrication in Kamukunji and carpentry in Gikomba to artisanal pottery and leather craft, the sector demonstrates immense resilience, creativity, and self-reliance.

3. **Modern Agribusiness (Agri-preneurship):**
   Agriculture is no longer just traditional subsistence digging. Young Kenyan agri-preneurs are leveraging smart farming: drip irrigation for capsicums and tomatoes, poultry farming, beekeeping, fish farming (aquaculture), and mushroom cultivation on quarter-acre plots, earning substantial, dignified livelihoods.

4. **Financial Literacy and Youth Enterprise Funds:**
   Initiatives like the Youth Enterprise Development Fund (YEDF), Uwezo Fund, and youth church SACCOs provide subsidized capital. Learning to manage cash flows, write simple business proposals, and practice strict financial honesty at a junior secondary level sets the foundation for lifelong economic freedom."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=75, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Kenyan Real-World Context: TVETs, Jua Kali & Agri-preneurship",
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

        reflection_text = """### Personal Spiritual Reflection: Discovering Creative Potential

Take a quiet moment to reflect on your attitudes toward work, enterprise, and your God-given creative abilities:

- **Reflecting the Creative God:**
  In Genesis, God is revealed as a tireless Creator and Master Craftsman who designed the universe with beauty and purpose. When you start a small venture—whether planting seedlings, baking bread, or designing graphics—how are you expressing God's image (*Imago Dei*) within you?

- **Conquering Fear of Failure:**
  Many people never start a business because they fear making a loss or being laughed at by peers. King Solomon wrote in Ecclesiastes 11:4, *"Whoever watches the wind will not plant; whoever looks at the clouds will not reap."* What fears are holding you back from testing your entrepreneurial ideas today?

> **Prayer of an Aspiring Entrepreneur:**
> *"Heavenly Father, You have endowed me with unique talents, creative energy, and capable hands. Deliver me from the spirit of idleness, passivity, and fear. Give me the wisdom to spot opportunities in my community, the diligence to work hard, and the integrity to run an honest enterprise that honors Your Holy Name. Amen."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
            order=90, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Spiritual Reflection: Overcoming Fear & Creating Value",
            content={"markdown": clean_text(reflection_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 6 (Page 6): Review & Mastery Check (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        takeaways_data = [
            "Youth unemployment is exacerbated by negative social attitudes toward manual trades, corruption, skills mismatches, and an excessive preference for scarce white-collar office jobs.",
            "Christian scripture strongly condemns idleness and mere talk, affirming that all honest hard work yields profit and moral dignity (Proverbs 14:23, 2 Thessalonians 3:10).",
            "Apostle Paul championed manual self-employment (tentmaking) as a means of winning the respect of outsiders and achieving dignified economic self-reliance (1 Thessalonians 4:11-12).",
            "Self-employment enables individuals to utilize their God-given talents, create jobs for peers, and stimulate the local economy despite challenges like capital scarcity and market competition.",
            "The Church and TVET institutions play a vital role in curbing unemployment through vocational training centers, table banking, agri-preneurship mentorship, and moral guidance."
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
            "question": "What is a major cause of high youth unemployment in Kenya today, and how does Christian Religious Education guide learners to overcome it?",
            "options": [
                {
                    "label": "A",
                    "text": "A total lack of biblical scriptures on industry; youth should wait indefinitely at home for government appointments."
                },
                {
                    "label": "B",
                    "text": "A persistent preference for prestigious white-collar desk jobs; youth should embrace practical TVET skills and initiate self-employment ventures with diligence and integrity."
                },
                {
                    "label": "C",
                    "text": "An outright legal ban on agricultural entrepreneurship; youth should only seek employment in foreign nations."
                },
                {
                    "label": "D",
                    "text": "The belief that manual labor is spiritually prohibited; youth should avoid all physical trades to maintain religious purity."
                }
            ],
            "correct_answer": "B",
            "explanation": "Option B is correct. Many school leavers and graduates remain unemployed due to a negative societal mindset that disdains manual, technical, and agricultural labor in favor of scarce white-collar office jobs. Christian teaching (Proverbs 14:23, 1 Thessalonians 4:11-12) upholds the dignity of working with one's hands and encourages youth to gain vocational TVET skills, exercise creativity, and start self-sustaining micro-enterprises. Options A, C, and D are factually and scripturally false."
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
    ingest_grade9_cre_topic1_lesson6()
