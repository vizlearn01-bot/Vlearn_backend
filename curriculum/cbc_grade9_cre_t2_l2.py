"""
VLearn CBC Grade 9 CRE — Topic 2: Christian Moral Values
Lesson 2: Traditional African vs. Christian Understandings of Sexuality

Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Christian Moral Values (ID: 318, Order: 2)
Learning Unit: 2.2 Traditional African vs. Christian Understandings of Sexuality (Order: 2)
Lesson: Traditional African vs. Christian Understandings of Sexuality (Order: 2, 6 Cards/Pages, 13 Blocks, 3 Assets)
"""

import os
import sys
import re
from pathlib import Path
import django
from django.db import transaction

# Setup Django Environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal meta tags."""
    if not text:
        return ""
    # Strip bracket citations e.g. [204], [204, 207], [245, 565, 568]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

def get_svg_cultural_vs_biblical_sexuality():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="africanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="christianGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="synthesisGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">CULTURAL CUSTOMS VS. BIBLICAL TRUTH</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Comparing Traditional African and Christian Understandings of Sexuality &amp; Marriage</text>

  <!-- Left Column: Traditional African Understanding -->
  <g transform="translate(30, 85)">
    <rect width="360" height="260" rx="10" fill="#1e293b" stroke="#d97706" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect width="360" height="38" rx="10" fill="url(#africanGrad)"/>
    <rect width="360" height="15" y="23" fill="url(#africanGrad)"/>
    <text x="180" y="24" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700">
      Traditional African Heritage
    </text>

    <!-- Points -->
    <g transform="translate(16, 52)" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11.5">
      <!-- Point 1 -->
      <circle cx="6" cy="7" r="3.5" fill="#f59e0b"/>
      <text x="18" y="11" font-weight="700" fill="#fbbf24">Purpose of Sex: Procreation Centric</text>
      <text x="18" y="26" fill="#cbd5e1" font-size="10.5">Primary goal is bearing children to perpetuate the clan lineage.</text>

      <!-- Point 2 -->
      <circle cx="6" cy="47" r="3.5" fill="#f59e0b"/>
      <text x="18" y="51" font-weight="700" fill="#fbbf24">Marriage Structure: Polygamy Accepted</text>
      <text x="18" y="66" fill="#cbd5e1" font-size="10.5">Multiple wives permitted for status, wealth, and farm labor.</text>

      <!-- Point 3 -->
      <circle cx="6" cy="87" r="3.5" fill="#f59e0b"/>
      <text x="18" y="91" font-weight="700" fill="#fbbf24">Gender Hierarchy: Patriarchal Superiority</text>
      <text x="18" y="106" fill="#cbd5e1" font-size="10.5">Men held dominant authority; women socialized into subordinate roles.</text>

      <!-- Point 4 -->
      <circle cx="6" cy="127" r="3.5" fill="#f59e0b"/>
      <text x="18" y="131" font-weight="700" fill="#fbbf24">Sex Education: Elder Guidance &amp; Initiation</text>
      <text x="18" y="146" fill="#cbd5e1" font-size="10.5">Taboo in daily talk; taught by grandparents during rites of passage.</text>

      <!-- Point 5 -->
      <circle cx="6" cy="167" r="3.5" fill="#f59e0b"/>
      <text x="18" y="171" font-weight="700" fill="#fbbf24">Moral Standard: Strict Community Chastity</text>
      <text x="18" y="186" fill="#cbd5e1" font-size="10.5">Virginity rewarded; premarital pregnancy punished by heavy fines.</text>
    </g>
  </g>

  <!-- Right Column: Christian Biblical Teachings -->
  <g transform="translate(410, 85)">
    <rect width="360" height="260" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect width="360" height="38" rx="10" fill="url(#christianGrad)"/>
    <rect width="360" height="15" y="23" fill="url(#christianGrad)"/>
    <text x="180" y="24" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700">
      Christian Biblical Truth
    </text>

    <!-- Points -->
    <g transform="translate(16, 52)" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11.5">
      <!-- Point 1 -->
      <circle cx="6" cy="7" r="3.5" fill="#60a5fa"/>
      <text x="18" y="11" font-weight="700" fill="#93c5fd">Purpose of Sex: Holy Covenant &amp; Companionship</text>
      <text x="18" y="26" fill="#cbd5e1" font-size="10.5">Sacred one-flesh union; marriage is complete even without children.</text>

      <!-- Point 2 -->
      <circle cx="6" cy="47" r="3.5" fill="#60a5fa"/>
      <text x="18" y="51" font-weight="700" fill="#93c5fd">Marriage Structure: Monogamous &amp; Permanent</text>
      <text x="18" y="66" fill="#cbd5e1" font-size="10.5">One man and one woman for life as ordained in Genesis 2:24.</text>

      <!-- Point 3 -->
      <circle cx="6" cy="87" r="3.5" fill="#60a5fa"/>
      <text x="18" y="91" font-weight="700" fill="#93c5fd">Gender Dynamic: Mutual Dignity &amp; Sacrificial Love</text>
      <text x="18" y="106" fill="#cbd5e1" font-size="10.5">Equal co-heirs; husbands love like Christ, wives respect (Eph 5:21-33).</text>

      <!-- Point 4 -->
      <circle cx="6" cy="127" r="3.5" fill="#60a5fa"/>
      <text x="18" y="131" font-weight="700" fill="#93c5fd">Mutual Ownership: Equal Marital Rights</text>
      <text x="18" y="146" fill="#cbd5e1" font-size="10.5">Each spouse's body belongs to the other in faithfulness (1 Cor 7:3-5).</text>

      <!-- Point 5 -->
      <circle cx="6" cy="167" r="3.5" fill="#60a5fa"/>
      <text x="18" y="171" font-weight="700" fill="#93c5fd">Moral Standard: Body as Temple of Holy Spirit</text>
      <text x="18" y="186" fill="#cbd5e1" font-size="10.5">Sexual purity honors God from the heart, avoiding lust and immorality.</text>
    </g>
  </g>

  <!-- Bottom Harmonization & Value Anchor Bar -->
  <rect x="30" y="360" width="740" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="380" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">HARMONIZATION &amp; CORE VALUE: MUTUAL RESPECT AND MORAL PURITY</text>
  <text x="400" y="398" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">We honor cultural virtues of elder wisdom and self-control while embracing Christ's standard of monogamy, gender equality, and sacrificial love.</text>

  <!-- Footer Tagline -->
  <text x="400" y="428" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 2: CHRISTIAN MORAL VALUES • PEDAGOGICAL COMPARATIVE MAP</text>
</svg>"""


# ─── LESSON 2 DATA CONFIGURATION ─────────────────────────────────────────────

LESSON_CONFIG = {
    "unit_order": 2,
    "unit_name": "Traditional African vs. Christian Understandings of Sexuality",
    "unit_description": "Compare traditional African cultural practices regarding sexuality and marriage with Christian biblical ethics, identifying points of harmony and areas transformed by Christ.",
    "lesson_title": "Traditional African vs. Christian Understandings of Sexuality",
    "image": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Mijikenda_Wedding_Blessing_Ceremony_%E2%80%93_Coastal_Kenya.jpg",
        "title": "Visual Hook: Traditional Wedding Blessing Ceremony in Coastal Kenya",
        "author": "Victor Ngonzo",
        "licensing": "CC BY-SA 4.0",
        "source": "Wikimedia Commons",
        "caption": "A traditional wedding blessing ceremony in Coastal Kenya, showing community elders and family gathered to impart cultural values, blessings, and wisdom to young couples entering marriage."
    },
    "youtube": {
        "youtube_id": "slyevQ1LW7A",
        "title": "BibleProject: Agapé — Self-Giving Love",
        "description": "Explores the biblical concept of Agapé love as self-sacrificing, covenantal devotion that defines Christian relationships, mutual submission, and marital partnership."
    },
    "svg_fn": get_svg_cultural_vs_biblical_sexuality,
    "goals": [
        "Outline traditional African practices and values regarding human sexuality, marriage, and gender roles.",
        "Analyze Christian teachings from Genesis 1:28, Ephesians 5:21-33, and 1 Corinthians 7:3-5 regarding marital equality, mutual submission, and sexual holiness.",
        "Evaluate areas of harmony and contrast between cultural customs and Christian doctrine, committing to positive cultural virtues while upholding biblical standards of gender equality."
    ],
    "intro": "Every community in Kenya possesses rich cultural heritage, traditions, and customs regarding how boys and girls grow into adulthood, how marriages are arranged, and how families are sustained.\n\nFrom the initiation ceremonies of the Kikuyu and Kalenjin to the traditional wedding blessings of the Mijikenda and Luo, traditional African societies held strict guidelines about human sexuality. But how do these ancient cultural traditions compare with the teachings of Jesus Christ and the Bible? As Christian learners in Grade 9, we are called to appreciate our positive cultural heritage while allowing God's Word to refine and transform our understanding of love, marriage, and gender equality.",
    "core_scripture": "### Core Scriptural Exegesis on Sexuality & Marriage\n\n#### Genesis 1:28 — The Blessing of Fruitfulness and Stewardship\n> *\"God blessed them and said to them, 'Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the sky and over every living creature that moves on the ground.'\"*\n\n#### Ephesians 5:21-25, 33 — Mutual Submission and Sacrificial Love\n> *\"Submit to one another out of reverence for Christ. Wives, submit yourselves to your own husbands as you do to the Lord... Husbands, love your wives, just as Christ loved the church and gave himself up for her... However, each one of you also must love his wife as he loves himself, and the wife must respect her husband.\"*\n\n#### 1 Corinthians 7:3-5 — Equality of Marital Rights and Mutual Belonging\n> *\"The husband should fulfill his marital duty to his wife, and likewise the wife to her husband. The wife does not have authority over her own body but yields it to her husband. In the same way, the husband does not have authority over his own body but yields it to his wife.\"*",
    "theological_pillars": "### Theological Exegesis: Transforming Relationships Through Christ\n\n1. **Mutual Submission in Reverence for Christ (Ephesians 5:21):** Unlike rigid patriarchal models where power is concentrated exclusively in men, Christian relationships begin with mutual submission. Both husband and wife yield their pride to serve one another under the Lordship of Jesus Christ.\n2. **Christ-like Sacrificial Headship:** Ephesians 5 redefines 'headship' not as dominating authority or privilege, but as sacrificial servant leadership. Just as Christ laid down His life for the Church, a husband is commanded to protect, cherish, and sacrifice for his wife with unconditional Agapé love.\n3. **Covenant Companionship vs. Utilitarian Procreation:** In biblical theology, procreation is a joyful gift (Genesis 1:28), but companionship is the foundational essence of marriage (Genesis 2:18). A Christian marriage is complete, holy, and fully valid even if a couple faces infertility.\n4. **Reciprocal Marital Rights (1 Corinthians 7:3-5):** The Apostle Paul emphasizes absolute reciprocity—neither spouse possesses autonomous control over their own body; both share equal dignity, mutual belonging, and lifelong faithfulness in a monogamous covenant.",
    "deep_dive": "### Comparative Deep Dive: Traditional African vs. Christian Understandings\n\nUnderstanding our cultural background alongside biblical principles helps us build healthy, God-honoring relationships:\n\n- **1. Purpose of Sexuality & Sex:**\n  - *Traditional African Heritage:* Sex was viewed primarily as an instrument of procreation to ensure the continuity of the clan lineage. Infertility was often viewed as a disaster and valid grounds for taking additional wives or seeking divorce.\n  - *Christian Biblical View:* Sex is a sacred, unitive gift designed for intimacy, companionship, mutual joy, and procreation within the lifelong covenant of marriage (Genesis 2:24).\n\n- **2. Structure of Marriage:**\n  - *Traditional African Heritage:* Polygamy (polygyny) was culturally acceptable and practiced to expand family labor, social prestige, and clan strength.\n  - *Christian Biblical View:* Monogamy (one man and one woman for life) is God's ordained creation pattern (Matthew 19:4-6, 1 Corinthians 7:2).\n\n- **3. Gender Roles and Decision-Making:**\n  - *Traditional African Heritage:* Strict patriarchal hierarchy where men made all major clan decisions and women were socialized into subordinate roles with limited inheritance rights.\n  - *Christian Biblical View:* Equal spiritual dignity as co-heirs of the grace of life (1 Peter 3:7, Galatians 3:28), marked by mutual respect, shared consultation, and sacrificial love.\n\n- **4. Sex Education and Moral Guidance:**\n  - *Traditional African Heritage:* Sex was considered a sacred taboo never discussed informally in public; education was delivered systematically by grandparents and elders during initiation rites.\n  - *Christian Biblical View:* Comprehensive moral instruction provided openly by parents, pastors, and mentors, emphasizing inner holiness, heart purity, and honoring God's temple (1 Thessalonians 4:3-5).",
    "practical": {
        "title": "Action Framework: 4 Principles for Promoting Gender Equality and Mutual Respect",
        "steps": [
            "Step 1: Affirm Equal Dignity in Daily Language — Reject derogatory stereotypes and cultural myths that portray girls or boys as inferior, recognizing that both reflect God's image.",
            "Step 2: Share School and Domestic Responsibilities Equitably — In classroom group work and home chores, ensure tasks like cleaning, organizing, leading discussions, and problem-solving are shared fairly without gender bias.",
            "Step 3: Stand Against Harmful Cultural Practices — Speak out courageously against early forced child marriage, female genital mutilation (FGM), and gender-based violence, defending the educational rights of all youth.",
            "Step 4: Practice Elder-Guided Moral Discipline — Seek counsel from wise parents, teachers, and Christian mentors on maintaining sexual purity and emotional boundaries in friendships."
        ]
    },
    "kenyan_context": "In Kenya today, Article 27 of the Constitution guarantees equal rights and freedoms for women and men, outlawing discrimination based on sex or cultural traditions. While we celebrate rich cultural practices like paying respectful dowry gifts (symbolizing gratitude between families) and receiving elder blessings, we firmly discard outdated practices such as wife inheritance, forced child marriages, or denying girls secondary education. Christian youth in Kenya lead the way in demonstrating that true masculinity involves protecting and honoring women, while true femininity is marked by dignity, strength, and active leadership.",
    "reflection": "### Cultural Heritage & Personal Reflection\n\nTake time to examine the traditions in your own community and evaluate them in light of Scripture:\n\n- Which traditional values from your culture (such as valuing chastity, respecting elders, and cherishing communal family unity) should we actively preserve and celebrate today?\n- How does Ephesians 5:21 (*'Submit to one another out of reverence for Christ'*) challenge both modern selfish individualism and traditional patriarchal dominance in relationships?",
    "takeaways": [
        "Traditional African culture and Christian ethics both place a high premium on sexual purity, self-control, and the sanctity of marriage.",
        "While traditional culture focused primarily on procreation and permitted polygamy, Christian marriage is a lifelong, monogamous covenant centered on holy companionship and mutual love.",
        "Biblical headship (Ephesians 5) is defined by Christ-like sacrificial service and mutual submission, replacing oppressive patriarchal dominance with equal dignity for women and men.",
        "Kenyan Christian youth are called to preserve positive cultural virtues (elder wisdom, chastity) while rejecting harmful practices (child marriage, gender inequality)."
    ],
    "mcq": {
        "question": "What is a central distinction between the traditional African view of marriage and Christian biblical teaching regarding the purpose of marriage and gender roles?",
        "options": [
            "A) Traditional African society rejected marriage completely, whereas Christianity requires it.",
            "B) Traditional African culture prioritized procreation and accepted polygamy with patriarchal hierarchy, whereas Christianity teaches a permanent monogamous union based on mutual submission, equal dignity, and companionship.",
            "C) Christianity forbids elders and grandparents from offering moral counsel to youth.",
            "D) Traditional African culture promoted unchaperoned adolescent dating, while Christianity insists on isolation."
        ],
        "answer": "B",
        "explanation": "In traditional African society, marriage was centered on childbearing to expand the clan lineage, which often led to polygamy and subordinate roles for women. In contrast, Christianity teaches that marriage is a monogamous, permanent covenant where husband and wife share equal dignity and mutual submission in Christ."
    }
}


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_t2_l2():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE — TOPIC 2, LESSON 2: TRADITIONAL AFRICAN VS. CHRISTIAN UNDERSTANDINGS OF SEXUALITY")
    print("=" * 80)

    with transaction.atomic():
        # Grade 9 (ID: 18), Subject: CRE (ID: 50)
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50, grade=grade)
        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            order=2,
            defaults={"name": "Christian Moral Values"}
        )

        print(f"Target Curriculum: {grade.curriculum.name}")
        print(f"Target Grade     : {grade.name} (ID: {grade.id})")
        print(f"Target Subject   : {subject.name} (ID: {subject.id})")
        print(f"Target Topic     : {topic.name} (ID: {topic.id}, Order: {topic.order})")

        cfg = LESSON_CONFIG
        u_order = cfg["unit_order"]
        u_name = cfg["unit_name"]
        l_title = cfg["lesson_title"]

        # Clean existing Unit 2 if present
        existing_units = LearningUnit.objects.filter(topic=topic, order=u_order)
        if existing_units.exists():
            for eu in existing_units:
                print(f"[*] Removing existing LearningUnit order={u_order} (ID: {eu.id})")
                eu.delete()

        # 1. Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            order=u_order,
            name=u_name,
            description=clean_text(cfg["unit_description"])
        )
        print(f"[+] Created LearningUnit ID: {unit.id} ('{unit.name}', order={unit.order})")

        # 2. Create Published Lesson
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=clean_text(l_title),
            status="published",
            version=1,
            immutable_metadata={
                "grade": "Grade 9",
                "subject": "CRE",
                "topic_order": 2,
                "topic_name": topic.name,
                "unit_order": u_order,
                "author": "VLearn Grade 9 CRE Ingestion Engine",
                "curriculum_framework": "CBC Kenya",
                "enrichment_version": "v3_pedagogical"
            }
        )
        print(f"[+] Created Lesson ID: {lesson.id} ('{lesson.title}', status={lesson.status})")

        # 3. Create LessonAssets (3 Assets)
        # Asset 1: Image Visual Hook
        img_info = cfg["image"]
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

        # Asset 2: Responsive SVG Diagram
        svg_content = cfg["svg_fn"]()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="url",
            status="attached",
            title=f"Diagram: {l_title}",
            description="Responsive pedagogical vector SVG diagram illustrating Cultural Customs vs. Biblical Truth in Sexuality & Marriage.",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic_2_lesson_2.svg",
            metadata={
                "svg_xml": svg_content,
                "viewBox": "0 0 800 450",
                "theme": "#0f172a"
            }
        )

        # Asset 3: Curated Educational YouTube Video
        yt_info = cfg["youtube"]
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
        print(f"[+] Attached 3 LessonAssets (Image, SVG Diagram, YouTube Video)")

        # 4. Create 6 Pages / Cards with LessonBlocks (13 Blocks total)

        # ───────────────────────────────────────────────────────────────────
        # CARD 1 (Page 1): Discovery & Objectives (3 blocks)
        # ───────────────────────────────────────────────────────────────────
        b1 = LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=10, component_order=1,
            block_type="suggested_image", component_type="suggested_image",
            title="Visual Hook: Traditional Wedding Blessing",
            content={
                "title": clean_text(img_info["title"]),
                "image_url": img_info["url"],
                "resolved_image_url": img_info["url"],
                "caption": clean_text(img_info["caption"]),
                "author": img_info["author"],
                "licensing": img_info["licensing"],
                "source": img_info["source"]
            }
        )
        b1.assets.add(img_asset)

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=20, component_order=2,
            block_type="learning_goal", component_type="learning_goal",
            title="Lesson Objectives",
            content={"goals": clean_dict(cfg["goals"])}
        )

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=30, component_order=3,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Cultural Heritage & Biblical Discernment",
            content={"markdown": clean_text(cfg["intro"])}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Biblical Foundations of Sexuality & Marriage",
            content={"markdown": clean_text(cfg["core_scripture"])}
        )

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Exegesis: Transforming Relationships Through Christ",
            content={"markdown": clean_text(cfg["theological_pillars"])}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 3 (Page 3): Vector SVG Diagram & Deep Dive (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        b5 = LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=50, component_order=1,
            block_type="suggested_diagram", component_type="suggested_diagram",
            title="Cultural Customs vs. Biblical Truth",
            content={
                "title": "Cultural Customs vs. Biblical Truth: Sexuality & Marriage",
                "caption": "A comparative pedagogical matrix contrasting traditional African cultural practices with Christian biblical ethics.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Comparative Deep Dive: Traditional African vs. Christian Teachings",
            content={"markdown": clean_text(cfg["deep_dive"])}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 4 (Page 4): Practical Application (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=70, component_order=1,
            block_type="step_process", component_type="step_process",
            title=clean_text(cfg["practical"]["title"]),
            content=clean_dict(cfg["practical"])
        )

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=75, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Kenyan Real-World Context: Gender Equality & Legal Rights",
            content={"markdown": clean_text(cfg["kenyan_context"])}
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

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
            order=90, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Cultural Heritage & Personal Reflection",
            content={"markdown": clean_text(cfg["reflection"])}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 6 (Page 6): Mastery Check & Key Takeaways (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title="Mastery Check",
            order=100, component_order=1,
            block_type="summary", component_type="summary",
            title="Summary & Core Principles",
            content={
                "title": f"Key Takeaways: {l_title}",
                "takeaways": clean_dict(cfg["takeaways"])
            }
        )

        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title="Mastery Check",
            order=110, component_order=2,
            block_type="knowledge_check", component_type="knowledge_check",
            title="Mastery Assessment",
            content=clean_dict(cfg["mcq"])
        )

        print(f"[+] Created 6 Pages (13 Blocks total)")

        print("=" * 80)
        print("INGESTION COMPLETED SUCCESSFULLY!")
        print(f"  - Lesson ID       : {lesson.id}")
        print(f"  - LearningUnit ID : {unit.id}")
        print(f"  - Pages Count     : 6")
        print(f"  - Blocks Count    : {lesson.blocks.count()}")
        print(f"  - Assets Count    : {lesson.assets.count()}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_cre_t2_l2()
