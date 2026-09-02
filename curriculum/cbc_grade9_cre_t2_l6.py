"""
VLearn CBC Grade 9 CRE — Strand 2.0, Sub-Strand 2.1: Christian Moral Values (Sexual Purity)
Lesson 6: Abortion and Divorce: Irresponsible Social Behaviors
Database Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Christian Moral Values (ID: 318, Order: 2)
Learning Unit: 6 (Abortion and Divorce: Irresponsible Social Behaviors)
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
    # Strip bracket citations e.g. [221], [222, 223], [243, 249]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|SCENARIO|TIMELINE|COMPARISON)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="divineGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="brokenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="cardLeftGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="100%" stop-color="#0c4a6e"/>
    </linearGradient>
    <linearGradient id="cardRightGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4c0519"/>
      <stop offset="100%" stop-color="#450a0a"/>
    </linearGradient>
    <filter id="glowLeft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#10b981" flood-opacity="0.3"/>
    </filter>
    <filter id="glowRight" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#f43f5e" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Background Frame -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="16"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="12"/>

  <!-- Title & Subtitle Header -->
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">GOD&apos;S DESIGN FOR LIFE &amp; COVENANT VS. BROKEN ALTERNATIVES</text>
  <text x="400" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Contrasting the Sanctity of Life &amp; Marital Permanence Against the Tragedies of Abortion &amp; Divorce</text>

  <!-- LEFT COLUMN: GOD'S SACRED DESIGN (IDEAL) -->
  <g transform="translate(35, 75)">
    <!-- Main Column Container -->
    <rect width="335" height="305" rx="12" fill="url(#cardLeftGrad)" stroke="#10b981" stroke-width="1.5" filter="url(#glowLeft)"/>
    <rect width="335" height="34" rx="12" fill="url(#divineGrad)"/>
    <text x="167" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">GOD&apos;S HOLY DESIGN (SANCTITY &amp; COVENANT)</text>

    <!-- Block 1: Sanctity of Life -->
    <g transform="translate(15, 45)">
      <rect width="305" height="115" rx="8" fill="#0f172a" fill-opacity="0.75" stroke="#34d399" stroke-width="1"/>
      <circle cx="24" cy="22" r="12" fill="#059669"/>
      <text x="24" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#10010;</text>
      <text x="44" y="24" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Sanctity of Human Life</text>
      <text x="14" y="48" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">&#8226; Life begins at conception as a gift from God.</text>
      <text x="14" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; Exodus 20:13: &quot;You shall not murder.&quot;</text>
      <text x="14" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; The maternal womb is a sacred haven of creation.</text>
      <text x="14" y="102" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="600">&#10140; God alone is the Author and Giver of Life.</text>
    </g>

    <!-- Block 2: Marriage Covenant -->
    <g transform="translate(15, 172)">
      <rect width="305" height="118" rx="8" fill="#0f172a" fill-opacity="0.75" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="24" cy="22" r="12" fill="#0284c7"/>
      <text x="24" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#8734;</text>
      <text x="44" y="24" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Permanent Marital Covenant</text>
      <text x="14" y="48" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">&#8226; Lifelong union of one man and one woman.</text>
      <text x="14" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; Matthew 19:6: &quot;What God joined, let no one separate.&quot;</text>
      <text x="14" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; Stable sanctuary for nurturing children &amp; love.</text>
      <text x="14" y="102" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="600">&#10140; Built upon sacrificial love, forgiveness &amp; fidelity.</text>
    </g>
  </g>

  <!-- CENTER DIVIDER & VALUE BRIDGE -->
  <g transform="translate(382, 90)">
    <line x1="18" y1="0" x2="18" y2="280" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
    <circle cx="18" cy="70" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="18" y="75" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">VS</text>

    <circle cx="18" cy="195" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="18" y="199" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">CBC</text>
  </g>

  <!-- RIGHT COLUMN: BROKEN SOCIAL ALTERNATIVES -->
  <g transform="translate(430, 75)">
    <!-- Main Column Container -->
    <rect width="335" height="305" rx="12" fill="url(#cardRightGrad)" stroke="#f43f5e" stroke-width="1.5" filter="url(#glowRight)"/>
    <rect width="335" height="34" rx="12" fill="url(#brokenGrad)"/>
    <text x="167" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">BROKEN SOCIAL REALITIES &amp; SINS</text>

    <!-- Block 1: Induced Abortion -->
    <g transform="translate(15, 45)">
      <rect width="305" height="115" rx="8" fill="#0f172a" fill-opacity="0.75" stroke="#fb7185" stroke-width="1"/>
      <circle cx="24" cy="22" r="12" fill="#e11d48"/>
      <text x="24" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#9888;</text>
      <text x="44" y="24" fill="#fda4af" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Induced Abortion</text>
      <text x="14" y="48" fill="#fecdd3" font-family="system-ui, sans-serif" font-size="10.5">&#8226; Deliberate termination of unborn human life.</text>
      <text x="14" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; Driven by panic, fear of poverty &amp; social stigma.</text>
      <text x="14" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; Severe risks: hemorrhage, infertility &amp; maternal death.</text>
      <text x="14" y="102" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="600">&#10140; Violates God&apos;s 6th Commandment.</text>
    </g>

    <!-- Block 2: Divorce -->
    <g transform="translate(15, 172)">
      <rect width="305" height="118" rx="8" fill="#0f172a" fill-opacity="0.75" stroke="#f87171" stroke-width="1"/>
      <circle cx="24" cy="22" r="12" fill="#b91c1c"/>
      <text x="24" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#10007;</text>
      <text x="44" y="24" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Marital Breakdown (Divorce)</text>
      <text x="14" y="48" fill="#fecdd3" font-family="system-ui, sans-serif" font-size="10.5">&#8226; Legal dissolution of the sacred marriage union.</text>
      <text x="14" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; Malachi 2:16: &quot;I hate divorce, says the Lord.&quot;</text>
      <text x="14" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">&#8226; Causes: adultery, violence, substance abuse, pride.</text>
      <text x="14" y="102" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="600">&#10140; Results in severe emotional trauma for children.</text>
    </g>
  </g>

  <!-- BOTTOM PEDAGOGICAL SUMMARY BAR -->
  <g transform="translate(35, 392)">
    <rect width="730" height="34" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="365" y="21" fill="#fde047" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">
      CHRISTIAN ACTION: Defend Unborn Life with Compassion &#8226; Heal Families through Biblical Reconciliation &amp; Forgiveness
    </text>
  </g>
</svg>"""


def ingest_grade9_cre_topic2_lesson6():
    print("=" * 80)
    print("INGESTING CBC GRADE 9 CRE — TOPIC 2: CHRISTIAN MORAL VALUES")
    print("LESSON 6: Abortion and Divorce: Irresponsible Social Behaviors")
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

    # 3. Ensure Topic 2 'Christian Moral Values' (Order: 2) exists under Subject 50
    topic_description = (
        "Christian ethics regarding human sexuality, contrasting traditional African understandings with Christian teachings, "
        "identifying moral values that foster sexual purity, and analyzing the consequences of irresponsible social behaviors "
        "such as premarital sex, STIs/HIV, abortion, and divorce."
    )
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=2,
        defaults={
            "name": "Christian Moral Values",
            "description": topic_description
        }
    )
    if not t_created:
        topic.name = "Christian Moral Values"
        topic.description = topic_description
        topic.save()
    print(f"[*] Resolved Topic 2: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    with transaction.atomic():
        unit_order = 6
        unit_name = "Abortion and Divorce: Irresponsible Social Behaviors"
        unit_description = (
            "Examining Christian ethical teachings regarding abortion and divorce, the sanctity of human life, "
            "causes and consequences of marital breakdown, and fostering crisis support and reconciliation."
        )
        lesson_title = "Abortion and Divorce: Irresponsible Social Behaviors"

        # Remove existing Unit 6 if present to avoid duplication
        existing_units = LearningUnit.objects.filter(topic=topic, order=unit_order)
        if existing_units.exists():
            for eu in existing_units:
                print(f"[*] Removing existing LearningUnit order={unit_order} (ID: {eu.id})")
                eu.delete()

        # 1. Create LearningUnit 6
        unit = LearningUnit.objects.create(
            topic=topic,
            order=unit_order,
            name=unit_name,
            description=clean_text(unit_description)
        )
        print(f"[+] Created LearningUnit ID: {unit.id} ('{unit.name}', order={unit.order})")

        # 2. Create Published Lesson
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
                "topic_id": topic.id,
                "topic_name": topic.name,
                "unit_order": unit_order,
                "author": "VLearn CRE Ingestion Agent",
                "curriculum_framework": "CBC Kenya",
                "enrichment_version": "v3_pedagogical"
            }
        )
        print(f"[+] Created Lesson ID: {lesson.id} ('{lesson.title}', status={lesson.status})")

        # 3. Create 3 LessonAssets
        # Asset 1: Authentic Visual Hook
        img_info = {
            "title": "A Mother's Embrace: Celebrating the Sanctity of Human Life and Family",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Mother_and_child_-_Africa.jpg/800px-Mother_and_child_-_Africa.jpg",
            "caption": "A loving mother gently cradles her child, reflecting God's holy design for the sanctity of human life, parental nurture, and family protection.",
            "author": "Wikimedia Commons / Africa Care",
            "licensing": "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
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
            description="Responsive pedagogical vector SVG diagram illustrating God's Design for Life and Covenant vs Broken Alternatives (Abortion & Divorce).",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic2_lesson_6.svg",
            metadata={
                "svg_xml": svg_content,
                "viewBox": "0 0 800 450",
                "theme": "#0f172a"
            }
        )

        # Asset 3: Curated Educational YouTube Video
        yt_info = {
            "title": "BibleProject: Covenants (God's Unbreakable Promises and Sacred Partnerships)",
            "youtube_id": "7_CGP-12AE0",
            "description": "Explore how the biblical concept of covenant defines sacred relationships, demonstrating why marriage is a lifelong holy partnership reflecting God's enduring faithfulness."
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
        print("[+] Created 3 LessonAssets: Image, SVG Diagram, and YouTube Video")

        # 4. Create 6 Pages with Standardized Block Types

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
                "description": "Define abortion (spontaneous vs. induced) and divorce, distinguishing between natural miscarriages and intentional terminations, and identifying key reasons why individuals seek them in contemporary society."
            },
            {
                "level": "Analyzing & Evaluating",
                "description": "Analyze core biblical scriptures (Exodus 20:13, Matthew 19:4-6, Malachi 2:16, Luke 12:15) to critique secular justifications for abortion and divorce from the perspective of Christian moral theology."
            },
            {
                "level": "Applying & Creating",
                "description": "Evaluate the medical, psychological, and social consequences of abortion and marital breakdown, formulating practical Christian crisis support, counseling, and reconciliation actions for families and vulnerable youth."
            }
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=20, component_order=2,
            block_type="learning_goal", component_type="learning_goal",
            title="Lesson Learning Objectives",
            content={"goals": clean_dict(goals_data)}
        )

        intro_text = """### The Sacred Sanctuary of Life and Family Covenant

Every human being longs for a safe, loving environment where their life is valued and their dignity is protected. God designed two fundamental institutions to provide this security: **the gift of human life** and **the holy covenant of marriage**.

From the moment of conception, the maternal womb is intended to be a sacred haven where an unborn baby—crafted uniquely in the image of God (*Imago Dei*)—grows in safety. Similarly, marriage is designed to be an unbreakable, lifelong sanctuary of unconditional love, companionship, and mutual protection for husbands, wives, and children.

However, in our contemporary world, socio-economic pressures, moral compromise, relationship conflicts, and selfish desires often lead to tragic decisions that shatter these divine institutions:
- **Abortion**, where the most vulnerable and defenseless human lives are deliberately terminated.
- **Divorce**, where sacred marriage vows are abandoned, fracturing families and inflicting profound emotional trauma on children and spouses.

In this lesson, we examine Christian ethical teachings regarding abortion and divorce, understand why they are classified as irresponsible social behaviors against God's will, and explore how the Christian community can offer compassionate crisis support, reconciliation, and healing."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=30, component_order=3,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Introduction: The Sanctity of Life and the Family Covenant",
            content={"markdown": clean_text(intro_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis & Theological Foundations (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        scripture_text = """### Scriptural Foundations: Life as a Divine Gift & Marriage as an Unbreakable Covenant

The Bible offers definitive, unwavering moral guidance regarding the sanctity of human life, the permanence of marriage, and the danger of selfish greed:

#### 1. Exodus 20:13 — The Sixth Commandment
> *"You shall not murder."*

#### 2. Matthew 19:4-6 — Jesus on the Permanence of Marriage
> *"‘Haven’t you read,’ he replied, ‘that at the beginning the Creator “made them male and female,” and said, “For this reason a man will leave his father and mother and be united to his wife, and the two will become one flesh”? So they are no longer two, but one flesh. Therefore what God has joined together, let no one separate.’"*

#### 3. Malachi 2:16 — God's Verdict on Divorce
> *"‘The man who hates and divorces his wife,’ says the Lord, the God of Israel, ‘does violence to the one he should protect,’ says the Lord Almighty. So be on your guard, and do not be unfaithful."*

#### 4. Luke 12:15 — Guarding Against Greed and Materialism
> *Then he said to them, "Watch out! Be on your guard against all kinds of greed; life does not consist in an abundance of possessions."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Core Scriptural Texts on Life, Marriage, and Materialism",
            content={"markdown": clean_text(scripture_text)}
        )

        theological_exegesis_text = """### Theological Exegesis: Divine Authorship and Covenantal Fidelity

A thorough theological analysis of these scriptures reveals why abortion and divorce stand in direct opposition to God's holy design:

1. **God as the Sovereign Author and Giver of Life (Exodus 20:13):**
   - In Christian theology, human life is not a biological accident or property of the parents; it is a sacred gift sovereignly bestowed by God. Life begins at the moment of conception, where God forms the developing child in the mother's womb (Psalm 139:13-16, Jeremiah 1:5).
   - Because life belongs exclusively to God, human beings do not possess the moral right to extinguish innocent unborn life. Induced abortion directly violates the Sixth Commandment (*"You shall not murder"*), which forbids the deliberate taking of innocent human life.

2. **The "One Flesh" Divine Union (Matthew 19:4-6):**
   - When Jesus was asked about divorce, He pointed back to God's original creation ordinance in Genesis. Marriage is not merely a civil contract that can be dissolved when emotions fade; it is a **sacred covenant instituted by God**.
   - In marriage, God Himself joins a man and a woman into a supernatural "one flesh" union (*henosis*). Because God is the third party and sealer of the covenant, Jesus explicitly commands: *"What God has joined together, let no one separate."*

3. **Divorce as Covenant Treachery and Violence (Malachi 2:16):**
   - The prophet Malachi uses powerful legal and moral language to condemn divorce. Breaking marriage vows is described as treachery (*bagad*) against the wife of one's youth and against God who witnessed the covenant.
   - Divorce is described as "covering one's garment with violence," because it violently tears apart the emotional, spiritual, and physical unity of the home, exposing vulnerable spouses and children to economic and psychological distress.

4. **Greed vs. Divine Trust (Luke 12:15):**
   - Jesus warns that life does not consist in the abundance of material possessions. Many people seek abortions due to financial panic or selfish career ambitions, while many couples divorce over material disputes and greed. Jesus reminds us that human worth and security are rooted in God's providence, not economic convenience."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Exegesis: The Sanctity of Life and Indissoluble Covenant",
            content={"markdown": clean_text(theological_exegesis_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 3 (Page 3): Vector SVG Diagram & Deep Dive (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        b5 = LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=50, component_order=1,
            block_type="suggested_diagram", component_type="suggested_diagram",
            title=f"Visual Architecture: {lesson_title}",
            content={
                "title": "God's Design for Life and Covenant vs. Broken Alternatives",
                "caption": "A comprehensive conceptual vector SVG illustrating how God's holy standard for the sanctity of life and marriage stands in sharp contrast to the tragic realities of abortion and divorce.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        deep_dive_text = """### In-Depth Ethical Analysis: Abortion and Divorce in Modern Society

Let us examine the definitions, underlying causes, and severe consequences of these two irresponsible social behaviors:

---

### Part 1: Abortion — Types, Causes, and Consequences

**1. Definition and Classification:**
- **Abortion** is the termination of a pregnancy before the fetus is capable of surviving independently outside the womb.
- **Spontaneous Abortion (Miscarriage):** Occurs naturally and unintentionally due to medical complications, genetic anomalies, trauma, or maternal health issues. This is not a sin; it is a painful physical tragedy requiring pastoral compassion and medical care.
- **Induced Abortion:** The intentional, deliberate termination and expulsion of a developing fetus through pharmaceutical drugs, surgical instruments, or crude traditional concoctions.

**2. Why People Seek Induced Abortions:**
- **Fear of Socio-Economic Burden:** Poverty, unemployment, or fear of being unable to feed and educate the child.
- **Pregnancies from Sexual Violence:** Pregnancies resulting from the trauma of rape, defilement, or incest.
- **Disruption of Education and Career:** Fear of being expelled from school, losing career opportunities, or disappointing parents.
- **Fear of Social Stigma & Rejection:** Unmarried teenagers fearing public humiliation, peer mockery, and rejection by their families or religious communities.
- **Abandonment by the Partner:** When the male partner denies responsibility and refuses emotional and financial support.

**3. Devastating Physical & Psychological Consequences of Abortion:**
- **Severe Hemorrhage (Bleeding):** Massive blood loss that can lead to hypovolemic shock and rapid death.
- **Uterine Perforation & Cervical Lacerations:** Surgical instruments puncturing the uterus, bladder, or intestines, causing severe internal peritonitis.
- **Chronic Pelvic Infections & Infertility:** Unhygienic procedures introduce dangerous bacteria, causing Pelvic Inflammatory Disease (PID), blocked fallopian tubes, and permanent barrenness.
- **Post-Abortion Psychological Trauma:** Overwhelming guilt, deep clinical depression, insomnia, nightmares, self-hate, and post-traumatic stress disorder (PTSD).

---

### Part 2: Divorce — Causes and Devastating Consequences

**1. Definition:**
- **Divorce** is the legal and formal dissolution of a marriage by a court or customary authority, declaring the marital union null and void.

**2. Major Causes of Divorce in Contemporary Society:**
- **Marital Infidelity (Adultery):** Engaging in extramarital sexual relations, shattering the foundational trust of marriage.
- **Domestic Violence & Physical/Emotional Abuse:** Cruelty, battery, and verbal torment that threaten the physical safety and human dignity of a spouse.
- **Substance Abuse & Addiction:** Chronic alcoholism and drug abuse leading to financial ruin, neglect of family duties, and violent outbursts.
- **Financial Mismanagement & Greed:** Concealing income, irresponsible gambling, or disputes over property and family resources.
- **Interference from In-Laws:** Extended family members exerting toxic control, causing division between the husband and wife.
- **Lack of Forgiveness & Poor Communication:** Inability to resolve daily conflicts, allowing pride, resentment, and bitterness to fester.

**3. Devastating Consequences of Divorce:**
- **Severe Trauma on Children:** Children often suffer intense emotional turmoil, feelings of abandonment, anxiety, behavioral problems, academic decline, and difficulties forming healthy relationships in adulthood.
- **Economic Hardship:** Division of household assets and legal costs frequently plunge single-parent households into acute poverty.
- **Social Isolation & Bitterness:** Broken relationships with extended family and community, leading to profound loneliness and emotional depression."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Comprehensive Analysis: Mechanisms, Causes & Consequences",
            content={"markdown": clean_text(deep_dive_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 4 (Page 4): Practical Application & Kenyan Real-World Context (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        practical_framework = {
            "title": "Christian Crisis Support & Family Reconciliation Guide",
            "description": "A 4-stage practical framework for providing compassionate crisis intervention for vulnerable pregnancies and mediating marital reconciliation.",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Empathetic Listening & Crisis Intervention",
                    "description": "Provide a safe, confidential, and non-judgmental environment for distressed pregnant teenagers or struggling couples. Listen actively without condemnation, helping reduce panic and emotional despair."
                },
                {
                    "step_number": 2,
                    "name": "Holistic Medical, Material & Spiritual Provision",
                    "description": "Mobilize community and church resources to provide proper antenatal care, safe shelter, nutritional support, and spiritual encouragement for vulnerable young mothers, defending both mother and baby."
                },
                {
                    "step_number": 3,
                    "name": "Structured Pastoral Counseling & Conflict Mediation",
                    "description": "Engage experienced clergy, Christian marriage counselors, or respected elders to facilitate open dialogue between spouses, addressing root issues such as unfaithfulness, finances, and in-law interference."
                },
                {
                    "step_number": 4,
                    "name": "Cultivating Christ-Centered Forgiveness & Mentorship",
                    "description": "Guide individuals and couples through biblical forgiveness and emotional healing (Ephesians 4:31-32), establishing ongoing peer mentorship to rebuild broken trust and sustain peaceful family life."
                }
            ]
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=70, component_order=1,
            block_type="step_process", component_type="step_process",
            title="Practical Framework: Christian Crisis Support & Family Reconciliation",
            content=clean_dict(practical_framework)
        )

        kenyan_context_text = """### Kenyan Real-World Context: Constitutional Law, Church Support & Home Peace

Understanding how these moral teachings intersect with Kenyan law, society, and our personal homes is essential for every Grade 9 learner:

1. **The Legal Status of Abortion in Kenya:**
   - Under the **Constitution of Kenya (2010), Article 26(2)**: *"The life of a person begins at conception."*
   - Furthermore, **Article 26(4)** explicitly states that abortion is illegal in Kenya unless, in the opinion of a trained health professional, there is an emergency need for treatment, or the life or health of the mother is in danger, or if permitted by any other written law.
   - Procuring or assisting in an illegal "backstreet" abortion is a severe criminal offense under the Penal Code, punishable by heavy imprisonment.

2. **Supporting Vulnerable Teenagers in Kenyan Communities:**
   - When a schoolgirl becomes pregnant, secular peer pressure and fear often push her toward unsafe illegal abortion clinics.
   - The Ministry of Education's **School Re-entry Policy** allows pregnant girls and young mothers to continue their education after delivery without discrimination.
   - The Church and community must establish supportive rescue centers, crisis pregnancy ministries, and family support groups so that no girl feels abortion is her only option.

3. **Promoting Conflict Resolution & Peace at Home:**
   - As a Grade 9 student, you are an active member of your household:
     - **Pray for Family Unity:** Regularly pray for peace, love, and protection over your parents and guardians.
     - **Avoid Fueling Conflict:** If you witness arguments or misunderstandings at home, do not take sides, spread gossip, or show disrespect.
     - **Practice Quick Forgiveness:** Model Christ's character by apologizing quickly when wrong, obeying family rules, and communicating gently with siblings and parents."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=75, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Kenyan Real-World Context: Constitutional Law & Peace at Home",
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

        reflection_text = """### Personal Spiritual Reflection: Becoming an Agent of Life and Peace

Take a quiet moment to reflect on your attitudes toward the sanctity of human life and family harmony:

- **Defending the Vulnerable:**
  If a close classmate or friend confided in you that she was facing an unplanned pregnancy and contemplating abortion out of panic, how would you respond? Would you condemn and ostracize her, or would you walk beside her with Christlike love, connect her with trusted counselors, and encourage her to protect the precious life in her womb?

- **Fostering Forgiving Relationships:**
  When people hurt, betray, or disagree with you in school or at home, do you harbor grudges and plot retaliation, or do you cultivate a forgiving heart? Remember that strong, enduring marriages and friendships are built upon daily habits of patience and forgiveness formed right now in your youth.

> **Prayer for Families and the Unborn:**
> *"Heavenly Father, Author and Protector of all life, we thank You for the sacred gift of human life and the blessing of family. We pray for all unborn children, that they may be sheltered and welcomed into the world with love. We pray for our homes and families—heal every wounded marriage, remove bitterness and division, and teach us to love and forgive as Christ has forgiven us. Amen."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
            order=90, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Spiritual Reflection: Defending Life and Healing Families",
            content={"markdown": clean_text(reflection_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 6 (Page 6): Review & Mastery Check (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        takeaways_data = [
            "Human life is a sacred gift from God beginning at conception, and deliberate (induced) abortion violates the Sixth Commandment ('You shall not murder', Exodus 20:13).",
            "Spontaneous abortion (miscarriage) occurs naturally due to medical factors, whereas induced abortion is the intentional termination of pregnancy carrying severe risks of hemorrhage, infertility, and maternal death.",
            "Marriage is a permanent, divinely sealed covenant where husband and wife become 'one flesh'; Jesus taught that what God has joined together, no human should separate (Matthew 19:6).",
            "Divorce shatters God's design for family stability (Malachi 2:16), resulting from sins like adultery, domestic abuse, substance addiction, and greed, and causing deep emotional trauma for children.",
            "Under Article 26 of the Constitution of Kenya, the right to life begins at conception, and abortion is illegal except in certified medical emergencies.",
            "The Christian community is called to defend unborn life, support vulnerable mothers with tangible care, and facilitate biblical counseling and reconciliation to heal struggling marriages."
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title="Mastery Check",
            order=100, component_order=1,
            block_type="summary", component_type="summary",
            title="Summary & Core Principles",
            content={
                "title": f"Key Takeaways: {lesson_title}",
                "takeaways": clean_dict(takeaways_data)
            }
        )

        mcq_data = {
            "question": "Why do Christian teachings consider induced abortion to be a grave sin against God's moral law?",
            "options": [
                {
                    "label": "A",
                    "text": "Because medical procedures in hospitals are too costly for the community to finance."
                },
                {
                    "label": "B",
                    "text": "Because God is the sole author and giver of life, and deliberately terminating an unborn child violates the commandment 'You shall not murder' (Exodus 20:13)."
                },
                {
                    "label": "C",
                    "text": "Because traditional African customs exclusively permit grandmothers to conduct termination rites."
                },
                {
                    "label": "D",
                    "text": "Because children are only considered valuable after they reach adulthood and begin paying dowry."
                }
            ],
            "correct_answer": "B",
            "explanation": "Option B is correct. In Christian theology, human life is sacred from conception because it is uniquely created in the image of God (Imago Dei). Only God has sovereign authority over human life; therefore, deliberately extinguishing the life of a developing fetus violates the sanctity of life and the Sixth Commandment ('You shall not murder', Exodus 20:13). Options A, C, and D reflect misconceptions that contradict biblical truth."
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title="Mastery Check",
            order=110, component_order=2,
            block_type="knowledge_check", component_type="knowledge_check",
            title="Formative Mastery Assessment",
            content=clean_dict(mcq_data)
        )

        # 5. Verification and Summary
        blocks_count = lesson.blocks.count()
        assets_count = lesson.assets.count()
        pages_count = lesson.blocks.values_list('page_number', flat=True).distinct().count()

        print("=" * 80)
        print("INGESTION COMPLETED SUCCESSFULLY!")
        print(f"  - Curriculum: {grade.curriculum.name} (Grade: {grade.name}, Level: {grade.level})")
        print(f"  - Subject   : {subject.name} (ID: {subject.id})")
        print(f"  - Topic     : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  - Unit      : {unit.name} (ID: {unit.id}, Order: {unit.order})")
        print(f"  - Lesson    : {lesson.title} (ID: {lesson.id}, Status: {lesson.status})")
        print(f"  - Pages     : {pages_count}")
        print(f"  - Blocks    : {blocks_count}")
        print(f"  - Assets    : {assets_count}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_cre_topic2_lesson6()
