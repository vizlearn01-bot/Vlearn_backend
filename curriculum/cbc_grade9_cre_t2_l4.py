"""
VLearn CBC Grade 9 CRE — Strand 2.0, Sub-Strand 2.1: Christian Moral Values
Lesson 4: Irresponsible Sexual Behaviors
Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Christian Moral Values (ID: 318, Order: 2)
Learning Unit: 4 (Irresponsible Sexual Behaviors)
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
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal meta tags."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [193], [210], [211, 212]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION)[^\]]*\]', '', text, flags=re.IGNORECASE)
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
    <linearGradient id="covenantGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <linearGradient id="sinGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991b1b"/>
      <stop offset="50%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#10b981" flood-opacity="0.3"/>
    </filter>
    <filter id="redGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#ef4444" flood-opacity="0.35"/>
    </filter>
    <marker id="arrowRed" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#ef4444" />
    </marker>
  </defs>

  <!-- Background Frame -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="16"/>
  <rect x="12" y="12" width="776" height="426" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="12"/>

  <!-- Title & Subtitle Header -->
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE BOUNDARY OF HOLINESS: COVENANT VS. DEVIATIONS</text>
  <text x="400" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Biblical Standard of Human Dignity &amp; The Destructive Nature of Sexual Immorality (Gal 5:19-21, 1 Cor 6:18)</text>

  <!-- Central Sanctuary: Sacred Marriage Covenant -->
  <g transform="translate(250, 80)">
    <!-- Outer Shield / Boundary Glow -->
    <rect width="300" height="220" rx="16" fill="#1e293b" stroke="#10b981" stroke-width="2.5" filter="url(#glow)"/>
    
    <!-- Top Header -->
    <rect width="300" height="44" rx="14" fill="url(#covenantGrad)"/>
    <text x="150" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="800" text-anchor="middle">SACRED COVENANT OF MARRIAGE</text>
    
    <!-- Holy Dimensions Inside Covenant -->
    <g transform="translate(18, 56)">
      <!-- Item 1 -->
      <circle cx="10" cy="14" r="5" fill="#34d399"/>
      <text x="24" y="18" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Monogamous &amp; Lifelong Union</text>
      <text x="24" y="32" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">One man and one woman (Gen 2:24)</text>

      <!-- Item 2 -->
      <circle cx="10" cy="52" r="5" fill="#34d399"/>
      <text x="24" y="56" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Mutual Dignity &amp; Companionship</text>
      <text x="24" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Equal image of God; selfless love</text>

      <!-- Item 3 -->
      <circle cx="10" cy="90" r="5" fill="#34d399"/>
      <text x="24" y="94" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Holiness &amp; Temple of God</text>
      <text x="24" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Glorifying God with our bodies (1 Cor 6:19)</text>

      <!-- Item 4 -->
      <circle cx="10" cy="128" r="5" fill="#34d399"/>
      <text x="24" y="132" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Sanctified Procreation &amp; Family</text>
      <text x="24" y="146" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Safe nurturing environment for children</text>
    </g>
  </g>

  <!-- LEFT COLUMN: DESTRUCTIVE DEVIATIONS (Part 1) -->
  <!-- 1. Incest -->
  <g transform="translate(30, 85)">
    <rect width="195" height="64" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2" filter="url(#redGlow)"/>
    <rect width="195" height="20" rx="6" fill="url(#sinGrad)"/>
    <text x="97" y="14" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">INCEST</text>
    <text x="8" y="36" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Blood relative violations</text>
    <text x="8" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Destroys family trust &amp; morals</text>
  </g>

  <!-- 2. Rape / Sexual Violence -->
  <g transform="translate(30, 160)">
    <rect width="195" height="66" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2" filter="url(#redGlow)"/>
    <rect width="195" height="20" rx="6" fill="url(#sinGrad)"/>
    <text x="97" y="14" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">RAPE &amp; DEFILEMENT</text>
    <text x="8" y="36" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Non-consensual violence</text>
    <text x="8" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Min 20 yrs prison (SOA Kenya)</text>
  </g>

  <!-- 3. Fornication -->
  <g transform="translate(30, 237)">
    <rect width="195" height="64" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2" filter="url(#redGlow)"/>
    <rect width="195" height="20" rx="6" fill="url(#sinGrad)"/>
    <text x="97" y="14" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">FORNICATION</text>
    <text x="8" y="36" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Sex outside marriage</text>
    <text x="8" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Driven by peer pressure &amp; lust</text>
  </g>

  <!-- RIGHT COLUMN: DESTRUCTIVE DEVIATIONS (Part 2) -->
  <!-- 4. Adultery -->
  <g transform="translate(575, 85)">
    <rect width="195" height="64" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2" filter="url(#redGlow)"/>
    <rect width="195" height="20" rx="6" fill="url(#sinGrad)"/>
    <text x="97" y="14" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">ADULTERY</text>
    <text x="8" y="36" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Marital covenant breach</text>
    <text x="8" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Breaks homes, causes trauma</text>
  </g>

  <!-- 5. Prostitution & Exploitation -->
  <g transform="translate(575, 160)">
    <rect width="195" height="66" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2" filter="url(#redGlow)"/>
    <rect width="195" height="20" rx="6" fill="url(#sinGrad)"/>
    <text x="97" y="14" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">PROSTITUTION / SPONSORS</text>
    <text x="8" y="36" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Transactional sex for money</text>
    <text x="8" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Exploits poverty; dehumanizing</text>
  </g>

  <!-- 6. Homosexual Practices -->
  <g transform="translate(575, 237)">
    <rect width="195" height="64" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2" filter="url(#redGlow)"/>
    <rect width="195" height="20" rx="6" fill="url(#sinGrad)"/>
    <text x="97" y="14" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">HOMOSEXUALITY</text>
    <text x="8" y="36" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Same-sex sexual relations</text>
    <text x="8" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Against God's creation design</text>
  </g>

  <!-- Divergent / Rupture Arrows pointing AWAY from Covenant -->
  <path d="M 250 117 L 230 117" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>
  <path d="M 250 193 L 230 193" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>
  <path d="M 250 269 L 230 269" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>

  <path d="M 550 117 L 570 117" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>
  <path d="M 550 193 L 570 193" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>
  <path d="M 550 269 L 570 269" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>

  <!-- Bottom Core Principle Banner -->
  <rect x="30" y="325" width="740" height="98" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1.2"/>
  <rect x="40" y="335" width="720" height="24" rx="6" fill="url(#goldGrad)"/>
  <text x="400" y="351" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="900" text-anchor="middle" letter-spacing="0.3">
    THE THREEFOLD CONSEQUENCE OF IRRESPONSIBLE SEXUAL BEHAVIOR
  </text>
  
  <!-- 3 Pillar Summaries at bottom -->
  <g transform="translate(45, 368)">
    <!-- Spiritual -->
    <text x="110" y="16" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">1. Spiritual Separation</text>
    <text x="110" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Grieves Holy Spirit; Kingdom forfeiture</text>
    
    <line x1="230" y1="5" x2="230" y2="45" stroke="#334155" stroke-width="1"/>

    <!-- Legal / Physical -->
    <text x="355" y="16" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">2. Legal &amp; Societal Guilt</text>
    <text x="355" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Severe penal codes; Sexual Offenses Act</text>

    <line x1="480" y1="5" x2="480" y2="45" stroke="#334155" stroke-width="1"/>

    <!-- Biological / Mental -->
    <text x="600" y="16" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">3. Biological &amp; Mental Trauma</text>
    <text x="600" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">STIs, HIV/AIDS, emotional devastation</text>
  </g>
</svg>"""


def ingest_grade9_cre_topic2_lesson4():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE TOPIC 2, LESSON 4: IRRESPONSIBLE SEXUAL BEHAVIORS")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Scope Entities
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(id=318, subject=subject)

        print(f"Target Scope: Grade '{grade.name}' (ID: {grade.id}), Subject '{subject.name}' (ID: {subject.id}), Topic '{topic.name}' (ID: {topic.id})")

        # 2. Setup / Clean Learning Unit 4
        unit_order = 4
        unit_name = "Irresponsible Sexual Behaviors"
        unit_description = (
            "Examine the biblical, ethical, and legal definitions of irresponsible sexual behaviors "
            "including incest, rape, fornication, adultery, prostitution, and homosexuality, analyzing "
            "their severe spiritual, social, and legal consequences under Christian doctrine and Kenyan law."
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
        lesson_title = "Irresponsible Sexual Behaviors"
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
                "topic_order": 2,
                "topic_id": 318,
                "topic_name": topic.name,
                "unit_order": unit_order,
                "author": "VLearn CRE Ingestion Agent",
                "curriculum_framework": "CBC Kenya",
                "enrichment_version": "v3_pedagogical"
            }
        )
        print(f"[+] Created Lesson {lesson.id} ('{lesson.title}') [status={lesson.status}]")

        # 4. Create 3 LessonAssets
        # Asset 1: Authentic Wikimedia Image Hook (Scales of Justice / Law Report)
        img_info = {
            "title": "Scales of Justice and the Rule of Law",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Scales_of_justice.png/800px-Scales_of_justice.png",
            "caption": "The scales of justice represent moral righteousness and legal accountability, safeguarding human dignity and protecting society from sexual crimes and exploitation.",
            "author": "Wikimedia Commons / Dmcdevit",
            "licensing": "CC BY-SA 3.0 / Public Domain",
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
                "alt_text": "Scales of Justice symbol of legal and moral accountability"
            }
        )

        # Asset 2: SVG Diagram Asset
        svg_content = get_svg_lesson_4()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="url",
            status="attached",
            title=clean_text("The Boundary of Holiness: Covenant of Marriage vs. Destructive Deviations"),
            description=clean_text("Architectural vector diagram illustrating God's holy design for marriage contrasted with forbidden sexual behaviors and their spiritual, legal, and biological consequences."),
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic2_lesson_4.svg",
            metadata={
                "svg_xml": svg_content,
                "viewBox": "0 0 800 450",
                "theme": "#0f172a"
            }
        )

        # Asset 3: Curated Educational YouTube Video
        yt_info = {
            "title": "BibleProject: Galatians — Works of the Flesh vs. Fruit of the Spirit",
            "youtube_id": "baXU74vhof0",
            "caption": "Explore the biblical contrast in Galatians 5 between destructive acts of the flesh and living by the Spirit in purity, love, and self-control.",
            "description": "An insightful animation by BibleProject explaining Paul's letter to the Galatians, highlighting how true Christian freedom honors God's moral boundaries rather than indulging sinful desires."
        }
        yt_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="youtube",
            source_type="external",
            storage_type="url",
            status="attached",
            title=clean_text(yt_info["title"]),
            description=clean_text(yt_info["caption"]),
            url=f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
            metadata={
                "youtube_id": yt_info["youtube_id"],
                "platform": "YouTube",
                "channel": "BibleProject",
                "embed_url": f"https://www.youtube.com/embed/{yt_info['youtube_id']}"
            }
        )
        print("[+] Created 3 LessonAssets (Image, SVG Diagram, Video)")

        # 5. Ingest 6 Cards (Pages) with Standardized LessonBlocks

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
                "description": "Define and describe irresponsible sexual behaviors such as incest, rape, fornication, adultery, prostitution, and homosexuality."
            },
            {
                "level": "Analyzing & Evaluating",
                "description": "Analyze biblical teachings (Leviticus 18:6-23, Galatians 5:19-21, 1 Corinthians 6:13-18) to critique modern permissive sexual attitudes and understand their legal and spiritual ramifications."
            },
            {
                "level": "Applying & Creating",
                "description": "Formulate personal moral boundaries and apply assertive decision-making strategies to reject exploitative relationships, transactional sex ('sponsor culture'), and sexual peer pressure."
            }
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=20, component_order=2,
            block_type="learning_goal", component_type="learning_goal",
            title="Lesson Objectives",
            content={"goals": clean_dict(goals_data)}
        )

        intro_text = """### Preserving Human Dignity: The Sacred Call to Moral Boundaries

Human sexuality is one of God's most precious and powerful gifts, designed to foster intimate companionship, mutual joy, and the creation of godly families within the lifelong covenant of marriage. However, because sexuality is deeply intertwined with our physical, emotional, and spiritual identity, its misuse carries profound consequences.

In contemporary society, popular culture, social media, and peer pressure often glamorize sexual permissiveness, treating physical intimacy as casual recreation or a commodity to be bought and sold. When boundaries established by God are ignored, sexuality is degraded from a sacred expression of love into a source of exploitation, violence, and heartbreak.

Christian Religious Education challenges us to examine the moral and legal realities of irresponsible sexual practices. By understanding God's righteous standards and the laws of our nation, we are empowered to guard our bodies as temples of the Holy Spirit and uphold the inviolable dignity of every human person."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=30, component_order=3,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Introduction: The Necessity of Moral Boundaries",
            content={"markdown": clean_text(intro_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis & Theological Foundations (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        scripture_text = """### Biblical Textual Foundations: God's Moral Standard

The Scriptures provide clear, direct prohibitions against sexual practices that violate God's creation order, defile the human person, and destroy community life:

#### 1. Leviticus 18:6-23 — The Sanctity of Family and Nature
> *"None of you shall approach any blood relative to uncover their nakedness: I am the Lord... Do not have sexual relations with your brother’s wife; that would defile your brother... Do not lie with a male as with a woman; that is an abomination. Do not have sexual relations with an animal and defile yourself with it."*

#### 2. Galatians 5:19-21 — Acts of the Flesh vs. The Kingdom of God
> *"The acts of the flesh are obvious: sexual immorality, impurity and debauchery; idolatry and witchcraft; hatred, discord, jealousy, fits of rage, selfish ambition, dissensions, factions and envy; drunkenness, orgies, and the like. I warn you, as I did before, that those who live like this will not inherit the kingdom of God."*

#### 3. 1 Corinthians 6:13-18 — The Body as the Temple of the Holy Spirit
> *"The body, however, is not meant for sexual immorality but for the Lord, and the Lord for the body... Do you not know that your bodies are members of Christ himself? Shall I then take the members of Christ and unite them with a prostitute? Never!... Flee from sexual immorality. All other sins a person commits are outside the body, but whoever sins sexually, sins against their own body."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Core Biblical Prohibitions on Sexual Immorality",
            content={"markdown": clean_text(scripture_text)}
        )

        theological_exegesis_text = """### Theological Exegesis: Divine Intent vs. Human Rebellion

A deep theological examination of these scriptural passages reveals why irresponsible sexual behavior is fundamentally destructive:

- **The Sacred Covenant of Marriage (Genesis 1:27-28, Genesis 2:24):**
  God established sexuality to be expressed exclusively within the lifelong, monogamous union of husband and wife. Within this covenant, sexual union signifies mutual self-giving, unity of soul and body ("one flesh"), and the holy nurture of children. Outside this covenant, sex is stripped of its relational commitment and divine purpose.

- **Acts of the Flesh vs. Kingdom Inheritance (Galatians 5:19-21):**
  Apostle Paul contrasts the *works of the flesh* (*sarx*) with the *fruit of the Spirit*. Sexual immorality (*porneia*), impurity (*akatharsia*), and debauchery (*aselgeia*) represent self-centered indulgence that rebels against God's sovereign rule. Paul solemnly warns that persistent, unrepentant immersion in these sins excludes individuals from inheriting God's eternal Kingdom.

- **The Body as a Sacred Temple (1 Corinthians 6:13-20):**
  Paul counters Greek philosophies that viewed bodily actions as spiritually irrelevant. Because the believer is redeemed by the blood of Christ, the physical body is an indwelling sanctuary of the Holy Spirit (*naos*). Sexual sin is unique because it is a sin *against one's own body*, corrupting the sacred vessel destined for resurrection and divine communion."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Analysis: Covenant Holiness & Divine Judgment",
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
                "title": "The Boundary of Holiness: Covenant of Marriage vs. Destructive Deviations",
                "caption": "A structured vector diagram illustrating God's holy design for marriage contrasted with forbidden sexual behaviors and their spiritual, legal, and biological consequences.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        deep_dive_text = """### Comprehensive Deep Dive: Defining Irresponsible Sexual Behaviors

Christian ethics and statutory law recognize distinct categories of forbidden sexual behavior, each carrying severe moral, psychological, and legal consequences:

#### 1. Incest
- **Definition:** Consensual or forced sexual relations between closely related blood relatives (e.g., parent and child, siblings, uncle and niece).
- **Biblical & Ethical Assessment:** Strictly forbidden in Leviticus 18:6-18. It corrupts the sanctity of the family unit, shatters trust among relatives, and inflicts lifelong psychological trauma.
- **Legal Context in Kenya:** Under the Sexual Offences Act (Act No. 3 of 2006, Section 20), incest is a severe felony carrying imprisonment of not less than 10 years and up to life imprisonment depending on the age of the victim.

#### 2. Rape & Defilement
- **Definition:** Forcing any individual to engage in sexual acts without their freely given consent. When committed against a minor (under 18 years), it constitutes **defilement**.
- **Biblical & Ethical Assessment:** Condemned as a heinous act of sexual violence, abuse of power, and absolute violation of human dignity.
- **Legal Penalty in Kenya:** Under the Sexual Offences Act (Sections 3 & 8), rape carries a **mandatory minimum penalty of 20 years in prison**, which can extend to life imprisonment. Defilement of a child under 11 years carries life imprisonment. Indecent assault attracts up to 5 years imprisonment.

#### 3. Fornication
- **Definition:** Consensual sexual intercourse between unmarried individuals.
- **Causes among Youth:** Curiosity, peer pressure, media influence, lack of self-control, drug and alcohol abuse, and the mistaken desire to prove adulthood.
- **Consequences:** Unplanned teenage pregnancies, school dropouts, risk of incurable STIs and HIV, emotional scarring, and guilt before God (1 Thessalonians 4:3-5).

#### 4. Adultery
- **Definition:** Sexual intercourse committed by a married person with someone other than their lawful spouse.
- **Causes & Impacts:** Lack of self-control, marital conflict, vengeance, or emotional disconnect. It breaks the sacred marriage vow (Exodus 20:14), damages children's emotional stability, and frequently causes divorce and family breakdown.

#### 5. Prostitution & Transactional Sex
- **Definition:** Exchanging sexual acts for money, gifts, shelter, or academic favors (commercial sex work and 'sponsor' relationships).
- **Causes:** Poverty, greed, peer influence, substance abuse, and moral compromise.
- **Consequences:** Extreme vulnerability to violence, dehumanization (reducing a person to an object), STI/HIV transmission, and social stigma.

#### 6. Homosexuality & Lesbianism
- **Definition:** Sexual relations between individuals of the same biological sex (male with male, female with female).
- **Biblical View:** Viewed as a violation of God's original creation order of complementary male and female union (Genesis 1:27, Leviticus 18:22, Romans 1:26-27).
- **Legal Status in Kenya:** Under Sections 162 and 165 of the Penal Code of Kenya, unnatural sexual offenses remain prohibited by law."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Detailed Analysis: Forbidden Sexual Practices & Legal Ramifications",
            content={"markdown": clean_text(deep_dive_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 4 (Page 4): Practical Application & Kenyan Context (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        practical_framework = {
            "title": "4-Step Framework for Resisting 'Sponsor' Culture & Exploitative Relationships",
            "description": "A practical Christian life-skills roadmap for adolescents to recognize predators, reject transactional sex offers, and preserve moral integrity.",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Recognize the Trap (Self-Awareness & Discernment)",
                    "description": "Identify suspicious gifts, unsolicited money, luxury rides, or special favors from older individuals ('sponsors' or predators) as subtle grooming tactics designed to demand sexual favors."
                },
                {
                    "step_number": 2,
                    "name": "Refuse Assertively and Immediately (Firm Boundaries)",
                    "description": "Say a clear, decisive, and polite 'NO' without hesitation or ambiguity. Example: 'Thank you, but I do not accept gifts or rides from people outside my family, and I am committed to my moral purity and studies.'"
                },
                {
                    "step_number": 3,
                    "name": "Remove Yourself from Danger (Physical & Digital Distance)",
                    "description": "Immediately exit the environment, avoid isolated private meetings, block the individual's phone number and social media accounts, and refuse to keep predatory secrets."
                },
                {
                    "step_number": 4,
                    "name": "Report to Trusted Authorities (Safety & Accountability)",
                    "description": "Inform parents, trusted teachers, school guidance counselors, or church leaders. In cases of intimidation or stalking, report to the police or call the Childline Kenya toll-free helpline (116)."
                }
            ]
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=70, component_order=1,
            block_type="step_process", component_type="step_process",
            title="Framework: Resisting Exploitation & Transactional Sex",
            content=clean_dict(practical_framework)
        )

        kenyan_context_text = """### Kenyan Real-World Context: Sexual Offences Act & Youth Protection

In Kenya, sexual exploitation and abuse are strictly regulated under criminal law to protect young people and maintain moral order:

1. **The Sexual Offences Act (Act No. 3 of 2006):**
   Kenya enacted progressive legislation to punish sexual predators severely. The law criminalizes defilement, rape, sexual harassment, deliberate transmission of HIV, and child sex tourism. Any adult who attempts to exploit a school-going youth or minor faces long-term imprisonment.

2. **Overcoming 'Sponsor' Culture in Kenya:**
   In urban and peri-urban Kenya, the phenomenon of wealthy older men or women ('sponsors') targeting vulnerable teenagers with smartphones, pocket money, or designer clothes has caused devastating harm—leading to school dropouts, HIV infections, and mental breakdown. Christian youth must recognize that **human worth is rooted in being created in God's image**, not in material possessions or luxury lifestyles.

3. **Practical Action Steps for Grade 9 Learners:**
   - **Contentment:** Cultivate gratitude for what your parents or guardians provide (Hebrews 13:5), refusing to envy lavish peer lifestyles funded by immoral compromise.
   - **Accountability Circles:** Form positive peer groups with fellow Christian youths who encourage academic excellence, sports, and spiritual growth.
   - **Breaking the Silence:** Never conceal sexual harassment or inappropriate advances by adults or peers. Speak up immediately to school authorities or use child protection helplines."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=75, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Kenyan Real-World Realities: Legal Protection & Youth Empowerment",
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

        reflection_text = """### Ethical Scenario Analysis & Spiritual Reflection

#### Case Study: The Enticing Offer
Wanjiku is an ambitious Grade 9 student whose family faces financial constraints. A well-to-do neighbor offers to buy her the latest smartphone, pay for her weekend salon visits, and provide pocket money, provided she visits his apartment privately after school. Her friends urge her to take the offer, claiming "everyone has a sponsor nowadays."

#### Ethical & Spiritual Analysis:
- **Identifying the Danger:** The offer is not genuine generosity; it is an exploitative gateway to transactional sex and potential defilement.
- **Moral Values at Stake:** 
  - **Integrity:** Doing what is morally right before God even when facing financial difficulties (Proverbs 10:9).
  - **Self-Respect & Self-Control:** Recognizing that her body is a temple of the Holy Spirit that cannot be traded for perishable gadgets.
  - **Assertiveness:** Courageously rejecting the offer, informing her parents, and focusing on her education.

#### Personal Spiritual Reflection:
- *Are there areas in your life where media, music, or peer pressure are tempting you to compromise God's standards of sexual purity?*
- *How can relying on the Holy Spirit give you the strength to flee youthful passions and pursue righteousness with a clean heart (2 Timothy 2:22)?*

> **Adolescent's Prayer for Purity & Wisdom:**
> *"Heavenly Father, You created my body as a sacred dwelling for Your Holy Spirit. Give me wisdom to discern evil traps, the courage to say 'No' to destructive temptations, and the contentment to value my dignity above all worldly possessions. Guide my steps in the path of holiness. Amen."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
            order=90, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Ethical Scenario: Resisting Exploitation with Integrity",
            content={"markdown": clean_text(reflection_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 6 (Page 6): Review & Mastery Check (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        takeaways_data = [
            "God designed human sexuality to be expressed solely within the sacred, loving, and lifelong covenant of marriage (Genesis 2:24).",
            "Irresponsible sexual behaviors—including incest, rape, fornication, adultery, prostitution, and homosexuality—violate God's moral law and degrade human dignity.",
            "Under Kenyan law (Sexual Offences Act 2006), rape and defilement are severe criminal offenses carrying harsh penalties, including a mandatory minimum of 20 years to life imprisonment.",
            "Adolescents must actively resist 'sponsor' culture and transactional sex by practicing contentment, self-control, assertiveness, and immediate reporting of predatory advances.",
            "Our bodies are holy temples of the Holy Spirit (1 Corinthians 6:19-20); we are called to honor God by fleeing sexual immorality and living with integrity."
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
            "question": "Under Kenyan law (The Sexual Offences Act), what is the minimum legal penalty for the crime of rape?",
            "options": [
                {
                    "label": "A",
                    "text": "A monetary fine paid directly to the victim's family."
                },
                {
                    "label": "B",
                    "text": "A minimum of 20 years in prison."
                },
                {
                    "label": "C",
                    "text": "Six months of supervised community service."
                },
                {
                    "label": "D",
                    "text": "Traditional elders' reconciliation without imprisonment."
                }
            ],
            "correct_answer": "B",
            "explanation": "Option B is correct. Under the Sexual Offences Act of Kenya, rape is a serious felony carrying a mandatory minimum penalty of 20 years of imprisonment, and up to life imprisonment, reflecting the state's zero tolerance for sexual violence. Options A, C, and D are incorrect and do not reflect statutory criminal law in Kenya."
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
    ingest_grade9_cre_topic2_lesson4()
