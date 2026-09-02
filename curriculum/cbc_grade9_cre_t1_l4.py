"""
VLearn CBC Grade 9 CRE — Strand 1.0, Sub-Strand 1.1: Work
Lesson 4: Duties and Rights in Employment
Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Work (ID: 316, Order: 1)
Learning Unit: 4 (Duties and Rights in Employment)
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

def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="employerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="employeeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d9488"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="covenantGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0284c7" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Background Frame -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="16"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="12"/>

  <!-- Title & Subtitle Header -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE RECIPROCAL COVENANT OF EMPLOYMENT</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Biblical Balance of Mutual Duties &amp; Inherent Rights (Colossians 4:1 &amp; Ephesians 6:5-9)</text>

  <!-- Central Biblical Covenant Seal -->
  <g transform="translate(320, 80)">
    <rect width="160" height="60" rx="10" fill="url(#covenantGrad)" stroke="#fbbf24" stroke-width="1.5" filter="url(#glow)"/>
    <text x="80" y="26" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="900" text-anchor="middle">DIVINE COVENANT</text>
    <text x="80" y="46" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">"Master in Heaven"</text>
  </g>

  <!-- Dynamic Reciprocal Flow Arrows -->
  <path d="M 285 180 C 285 150, 310 120, 320 120" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <path d="M 480 120 C 490 120, 515 150, 515 180" fill="none" stroke="#34d399" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- LEFT COLUMN: EMPLOYER (Duties & Rights) -->
  <g transform="translate(35, 100)">
    <!-- Column Header Box -->
    <rect width="320" height="42" rx="8" fill="url(#employerGrad)"/>
    <text x="160" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">EMPLOYER (Management)</text>

    <!-- Duties Section -->
    <rect y="50" width="320" height="150" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.2"/>
    <rect y="50" width="320" height="24" rx="8" fill="#0369a1" opacity="0.4"/>
    <text x="12" y="67" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">DUTIES TOWARD WORKERS (Responsibilities)</text>
    <text x="12" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Pay prompt, fair wages without delay (James 5:4)</text>
    <text x="12" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Provide safe, hygienic, &amp; equipped workspace</text>
    <text x="12" y="132" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Safeguard human dignity; avoid harsh threats</text>
    <text x="12" y="152" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Grant regulated rest, medical care &amp; leave</text>
    <text x="12" y="172" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Motivate growth &amp; reward professional skill</text>

    <!-- Rights Section -->
    <rect y="210" width="320" height="110" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.2"/>
    <rect y="210" width="320" height="24" rx="8" fill="#0369a1" opacity="0.4"/>
    <text x="12" y="227" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">INHERENT RIGHTS OF EMPLOYER</text>
    <text x="12" y="252" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Expect honest, full day's dedicated labor</text>
    <text x="12" y="272" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Protection of company capital &amp; property</text>
    <text x="12" y="292" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Lawful contract execution, profit &amp; discipline</text>
  </g>

  <!-- RECIPROCAL BALANCE CONNECTOR IN MIDDLE -->
  <g transform="translate(365, 230)">
    <circle cx="35" cy="45" r="28" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <text x="35" y="42" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">&#8644;</text>
    <text x="35" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">JUSTICE</text>
  </g>

  <!-- RIGHT COLUMN: EMPLOYEE (Duties & Rights) -->
  <g transform="translate(445, 100)">
    <!-- Column Header Box -->
    <rect width="320" height="42" rx="8" fill="url(#employeeGrad)"/>
    <text x="160" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">EMPLOYEE (Worker)</text>

    <!-- Duties Section -->
    <rect y="50" width="320" height="150" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
    <rect y="50" width="320" height="24" rx="8" fill="#047857" opacity="0.4"/>
    <text x="12" y="67" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">DUTIES TOWARD EMPLOYER (Responsibilities)</text>
    <text x="12" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Diligent service from the heart, not eyeservice</text>
    <text x="12" y="112" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Faithfully guard employer tools &amp; assets</text>
    <text x="12" y="132" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Comply with lawful contractual obligations</text>
    <text x="12" y="152" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Foster peaceful mediation; reject sabotage</text>
    <text x="12" y="172" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Maintain honesty, punctuality &amp; integrity</text>

    <!-- Rights Section -->
    <rect y="210" width="320" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
    <rect y="210" width="320" height="24" rx="8" fill="#047857" opacity="0.4"/>
    <text x="12" y="227" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">INHERENT RIGHTS OF EMPLOYEE</text>
    <text x="12" y="252" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Prompt, dignified &amp; living compensation</text>
    <text x="12" y="272" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Safe working terms, rest &amp; union protection</text>
    <text x="12" y="292" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Fair grievance hearings &amp; career progression</text>
  </g>

  <!-- Bottom Core Principle Banner -->
  <rect x="35" y="380" width="730" height="42" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="406" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    Ethical Golden Rule: The rights of one party are safeguarded by the conscientious duties of the other.
  </text>
</svg>"""


def ingest_grade9_cre_topic1_lesson4():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE TOPIC 1, LESSON 4: DUTIES AND RIGHTS IN EMPLOYMENT")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Scope Entities
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(id=316, subject=subject)

        print(f"Target Scope: Grade '{grade.name}' (ID: {grade.id}), Subject '{subject.name}' (ID: {subject.id}), Topic '{topic.name}' (ID: {topic.id})")

        # 2. Setup / Clean Learning Unit 4
        unit_order = 4
        unit_name = "Duties and Rights in Employment"
        unit_description = (
            "Explore the moral duties, responsibilities, and reciprocal rights of employers and employees "
            "grounded in Christian ethics, biblical scripture (Ephesians 6:5-9, Colossians 4:1, James 5:4), "
            "and contemporary labor law standards."
        )

        # Remove existing Unit 4 if present to allow clean idempotent re-ingestion
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
        lesson_title = "Duties and Rights in Employment"
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
            "title": "A Fair Employment Contract and Signing of Labor Agreement",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Contract_signing_ceremony.jpg/800px-Contract_signing_ceremony.jpg",
            "caption": "An employment agreement formalizes the reciprocal covenant of labor, defining mutual rights, safe conditions, and honest compensation between employer and employee.",
            "author": "Wikimedia Commons / US Navy Specialist",
            "licensing": "Public Domain / CC BY-SA 4.0",
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
        svg_content = get_svg_lesson_4()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="url",
            status="attached",
            title=f"Diagram: {lesson_title}",
            description=f"Responsive pedagogical vector SVG diagram illustrating the reciprocal covenant of employment duties and rights.",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic1_lesson_4.svg",
            metadata={
                "svg_xml": svg_content,
                "viewBox": "0 0 800 450",
                "theme": "#0f172a"
            }
        )

        # Asset 3: Curated Educational YouTube Video
        yt_info = {
            "title": "BibleProject: Justice / Mishpat (The Biblical Foundation of Fairness and Work)",
            "youtube_id": "A14THPoc4-4",
            "description": "Explore the biblical concept of Justice (Mishpat and Tzedakah) and how God expects employers and workers to honor each other's human dignity in society."
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
                "description": "Identify and explain the specific moral duties and legal rights of employers and employees in modern workplace contexts."
            },
            {
                "level": "Analyzing & Evaluating",
                "description": "Analyze biblical passages (Ephesians 6:5-9, Colossians 4:1, James 5:4) to critique workplace injustices, exploitation, and negligence."
            },
            {
                "level": "Applying & Creating",
                "description": "Apply Christian ethical principles of justice, fair mediation, and mutual dignity to resolve workplace disputes and promote harmonious labor relations."
            }
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=20, component_order=2,
            block_type="learning_goal", component_type="learning_goal",
            title="Lesson Objectives",
            content={"goals": clean_dict(goals_data)}
        )

        intro_text = """### The Covenant of Daily Labor: Understanding Fairness in Employment

Have you ever worked hard to complete a demanding task—washing dishes, tilling a garden, or tutoring a peer—only for the person who promised to reward you to delay, reduce, or refuse your pay? Or have you ever hired someone to help fix something, but they arrived late, handled the tools carelessly, and still demanded full compensation?

Both experiences leave a painful sense of injustice. Work is not a one-sided transaction; it is a **reciprocal covenant** built on mutual respect and shared responsibility. In every employment setting—from corporate offices and construction sites to farms and domestic households—justice depends upon both parties honoring their promises.

Christian Religious Education teaches that employment is rooted in God's divine standard of righteousness. When employers treat workers with honor and pay them promptly, and when employees work faithfully with diligence, labor becomes an avenue for human flourishing and glorifies God."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=30, component_order=3,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Introduction: The Need for Workplace Justice",
            content={"markdown": clean_text(intro_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis & Theological Foundations (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        scripture_text = """### Scriptural Foundations: God's Blueprint for Workplace Relationships

The Bible provides clear, uncompromising guidance on the moral standards governing superiors and subordinates:

#### 1. Colossians 4:1 — Accountability to the Heavenly Master
> *"Masters, provide your slaves with what is right and fair, because you know that you also have a Master in heaven."*

#### 2. Ephesians 6:5-9 — Wholehearted Service and Mutual Dignity
> *"Slaves, obey your earthly masters with respect and fear, and with sincerity of heart, just as you would obey Christ. Obey them not only to win their favor when their eye is on you, but as slaves of Christ, doing the will of God from your heart. Serve wholeheartedly, as if you were serving the Lord, not people, because you know that the Lord will reward each one for whatever good they do... And masters, treat your slaves in the same way. Do not threaten them, since you know that he who is both their Master and yours is in heaven, and there is no favoritism with him."*

#### 3. James 5:4 — Divine Condemnation of Withheld Wages
> *"Look! The wages you failed to pay the workers who mowed your fields are crying out against you. The cries of the harvesters have reached the ears of the Lord Almighty."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Core Biblical Texts on Employment Ethics",
            content={"markdown": clean_text(scripture_text)}
        )

        theological_exegesis_text = """### Theological Exegesis: Transforming Labor into Worship

The biblical texts dismantle worldly hierarchies and replace them with divine accountability:

- **The Shared Master in Heaven (Colossians 4:1, Ephesians 6:9):**
  Paul reminds employers and leaders that human authority is temporary and secondary. Earthly employers are themselves subordinate to God, the supreme Master. Because God shows **no partiality or favoritism**, a manager or boss will be judged by the exact standard of fairness they show toward their workers.

- **Rejection of "Eye-Service" (Ephesians 6:6-7):**
  Christian workers are called to work with authentic sincerity (*singleness of heart*), rather than merely pretending to be busy when the supervisor is watching (*eye-service* or *men-pleasing*). Christians view their daily labor as service rendered directly unto Jesus Christ.

- **The Cry of Oppressed Wages (James 5:4):**
  Withholding or delaying wages is portrayed in Scripture not simply as an administrative dispute, but as a grave moral sin that cries directly into the ears of the Lord of Hosts (*Yahweh Sabaoth*). God acts as the divine defender of vulnerable workers who are deprived of their livelihood."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Analysis: Accountability & Divine Justice",
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
                "title": f"The Reciprocal Covenant: Employer vs. Employee Duties & Rights",
                "caption": "A structured vector diagram illustrating how employer obligations guarantee employee rights, and employee diligence safeguards enterprise viability.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        deep_dive_text = """### In-Depth Analysis: The Reciprocal Framework of Employment

Employment operates on a balanced equation: **the rights of one party are sustained by the faithful duties of the other**.

#### 1. Employer Duties & Inherent Rights
- **Duties toward Employees:**
  - **Prompt and Fair Remuneration:** Paying a just living wage on agreed dates without illegal deductions or delays (Deut 24:14-15, James 5:4).
  - **Occupational Safety and Health:** Providing protective gear, safe machinery, clean drinking water, and sanitary facilities.
  - **Human Dignity and Respect:** Treating workers as human beings made in the image of God (*Imago Dei*), eliminating abusive speech, bullying, and intimidation.
  - **Statutory Leave & Rest:** Granting paid annual leave, sick leave, maternity/paternity leave, and weekly rest days.
  - **Career Development:** Offering fair mentorship, skills training, and merit-based advancement.
- **Rights of the Employer:**
  - **Right to a Full Day's Diligent Labor:** Expecting punctuality, focus, and adherence to performance standards.
  - **Right to Capital and Asset Protection:** Safeguarding equipment, intellectual property, tools, and finances from theft or vandalism.
  - **Right to Lawful Management:** Enforcing workplace policies, codes of conduct, and disciplinary procedures aligned with the contract.

#### 2. Employee Duties & Inherent Rights
- **Duties toward Employers:**
  - **Diligence & Conscientiousness:** Performing tasks to the highest standard without requiring constant supervision.
  - **Loyalty & Honesty:** Guarding confidential information, accounting accurately for materials, and rejecting fraud or kickbacks.
  - **Protection of Property:** Using employer resources responsibly, minimizing waste, and preventing machinery damage.
  - **Peaceful Conflict Resolution:** Engaging in constructive dialogue and following grievance procedures rather than sabotage.
- **Rights of the Employee:**
  - **Right to Timely Living Wages:** Receiving compensation that reflects the dignity and cost of human living.
  - **Right to Safe & Humane Working Hours:** Reasonable shift durations, overtime pay, and adequate rest periods.
  - **Right to Collective Bargaining & Unionization:** Freedom to join lawful trade unions to negotiate terms without victimisation.
  - **Right to Fair Due Process:** Protection against arbitrary termination without lawful notice, fair hearing, and severance."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Comprehensive Breakdown: Duties vs. Rights",
            content={"markdown": clean_text(deep_dive_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 4 (Page 4): Practical Application & Kenyan Context (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        practical_framework = {
            "title": "Christian Workplace Conflict Resolution Framework",
            "description": "A four-stage ethical mediation model for resolving workplace grievances with justice and Christian integrity.",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Direct Honest Dialogue (Matthew 18:15 Principle)",
                    "description": "The aggrieved party approaches the colleague or supervisor privately to discuss the issue objectively, presenting factual evidence without hostility or gossip."
                },
                {
                    "step_number": 2,
                    "name": "Structured Internal Grievance Review",
                    "description": "If unresolved, submit the grievance through formal human resources or shop-steward channels, invoking the employment contract and company code of conduct."
                },
                {
                    "step_number": 3,
                    "name": "Third-Party Christian Mediation & Conciliation",
                    "description": "Engage a neutral mediator (e.g., labor officer, union representative, or pastoral counselor) to facilitate fair compromise and restore working relationships."
                },
                {
                    "step_number": 4,
                    "name": "Legal Arbitration & Labor Court Adjudication",
                    "description": "As a final recourse when fundamental rights or statutory obligations are breached, seek formal legal settlement through industrial tribunals or the Employment and Labour Relations Court."
                }
            ]
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=70, component_order=1,
            block_type="step_process", component_type="step_process",
            title="Practical Application: Resolving Workplace Disputes",
            content=clean_dict(practical_framework)
        )

        kenyan_context_text = """### Kenyan Real-World Application: Labor Laws & Ethical Realities

In Kenya, labor relations are governed by the **Constitution of Kenya (Article 41 on Labour Relations)** and the **Employment Act of 2007**, which strongly reflect biblical principles of justice:

1. **Protection of Domestic Workers:**
   Thousands of households in Kenya employ domestic workers, gardeners, and security guards. Christian ethics require that domestic helpers receive fair wages (meeting national minimum wage guidelines), decent sleeping conditions, nutritious food, regulated working hours, and enrollment in social protections like the Social Health Authority (SHA) and NSSF.

2. **The Role of Trade Unions in Kenya:**
   Bodies like COTU (Central Organization of Trade Unions), KNUT (Kenya National Union of Teachers), and KMPDU (Kenya Medical Practitioners, Pharmacists and Dentists Union) represent employee interests. Christian workers should participate in union activities with integrity, championing constructive negotiation and avoiding violence or vandalism during industrial actions.

3. **Ethical Dilemmas in Student Daily Life:**
   As students, practicing employment ethics begins now:
   - When given paid or volunteer chores, execute them faithfully without cutting corners.
   - When hiring a peer to assist with typing or group project materials, pay the agreed amount promptly.
   - Speak up against the exploitation or mistreatment of support staff (cleaners, cooks, security guards) in your school."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=75, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Kenyan Real-World Context: Labor Laws & Social Responsibility",
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

        reflection_text = """### Personal Spiritual Reflection: The Mirror of Integrity

Take a quiet moment to reflect on your daily attitudes toward authority, service, and those who assist you:

- **How do you treat those who serve you?**
  Consider the domestic helpers in your home, the dining hall workers at school, or the cleaners who sweep the compound. Do you greet them with dignity, thank them for their labor, and respect their humanity, or do you treat them as invisible subordinates?

- **How do you work when unsupervised?**
  When your parents or teachers assign you homework or chores and leave the room, do you continue diligently, or do you engage in "eye-service"—working only when someone is watching?

> **Prayer of a Faithful Worker & Fair Leader:**
> *"Lord God, Master of heaven and earth, teach me to honor everyone who labors for my well-being. Give me a heart of diligence so that I work as unto You, and grant me a spirit of fairness so that I never withhold what is rightfully due to others. Amen."*"""

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
            "Employment is a reciprocal moral covenant where the rights of one party depend upon the faithful duties of the other.",
            "Employers must pay fair living wages promptly, maintain safe working environments, and honor employee dignity as accountable stewards under God (Colossians 4:1, James 5:4).",
            "Employees are called to work wholeheartedly with integrity, honesty, and diligence, avoiding deceptive eye-service (Ephesians 6:5-8).",
            "Kenyan labor laws (Employment Act 2007) and Christian ethics both mandate that vulnerable workers, including domestic helpers, receive just compensation, rest, and humane treatment.",
            "Workplace grievances should be resolved through open dialogue, structured internal mediation, and lawful conciliation rather than destructive sabotage."
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
            "question": "According to Christian teachings (Ephesians 6:5-9, Colossians 4:1) and labor ethics, which of the following best describes the core duty of an employee toward their employer?",
            "options": [
                {
                    "label": "A",
                    "text": "To demand immediate wage increments through unauthorized industrial action and tool boycotts."
                },
                {
                    "label": "B",
                    "text": "To serve wholeheartedly with diligence, honesty, and respect, protecting company assets without requiring constant supervision."
                },
                {
                    "label": "C",
                    "text": "To perform only assigned duties when directly monitored by management to maximize personal leisure time."
                },
                {
                    "label": "D",
                    "text": "To take home company tools and materials as compensation whenever salary increments are delayed."
                }
            ],
            "correct_answer": "B",
            "explanation": "Option B is correct. Christian scripture (Ephesians 6:5-8) instructs workers to serve sincerely from the heart as serving Christ, rather than performing superficial 'eye-service' only when watched. Employees have a moral duty to be diligent, loyal, and protective of their employer's property. Options A, C, and D violate biblical principles of integrity, honesty, and faithful stewardship."
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
    ingest_grade9_cre_topic1_lesson4()
