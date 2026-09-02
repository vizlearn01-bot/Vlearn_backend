"""
VLearn CBC Grade 9 CRE — Topic 2: Christian Moral Values
Lesson 1: Human Sexuality as a Gift from God

Target Grade: Grade 9 (ID: 18)
Target Subject: CRE (ID: 50)
Target Topic: Christian Moral Values (Order: 2)
Learning Unit: 2.1 Human Sexuality as a Gift from God (Order: 1)
Lesson: Human Sexuality as a Gift from God (Order: 1, 6 Cards/Pages, 13 Blocks, 3 Assets)
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
    # Strip bracket citations e.g. [201], [201, 202], [66, 203]
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

def get_svg_triune_dimensions_of_sexuality():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="bioGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="emoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="mentalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7e22ce"/>
    </linearGradient>
    <linearGradient id="centerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE TRIUNE DIMENSIONS OF HUMAN SEXUALITY</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Biological, Emotional, and Mental Identity in God's Holy Design (Genesis 1:27)</text>

  <!-- Intersecting Dimension Circles (Venn Layout) -->
  <!-- Top Circle: Biological / Physiological -->
  <circle cx="400" cy="165" r="95" fill="#0284c7" fill-opacity="0.22" stroke="#38bdf8" stroke-width="2.5"/>

  <!-- Bottom-Left Circle: Emotional / Relational -->
  <circle cx="315" cy="285" r="95" fill="#be185d" fill-opacity="0.22" stroke="#ec4899" stroke-width="2.5"/>

  <!-- Bottom-Right Circle: Mental / Psychological -->
  <circle cx="485" cy="285" r="95" fill="#7e22ce" fill-opacity="0.22" stroke="#a855f7" stroke-width="2.5"/>

  <!-- Central Intersection Highlight: Sacred Whole-Person Identity -->
  <circle cx="400" cy="245" r="42" fill="url(#centerGrad)" filter="url(#glow)" fill-opacity="0.9" stroke="#fef08a" stroke-width="2"/>
  <text x="400" y="238" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">SACRED</text>
  <text x="400" y="252" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">IDENTITY</text>
  <text x="400" y="265" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600" text-anchor="middle">Imago Dei</text>

  <!-- Node Labels & Details -->

  <!-- Top: Biological Dimension Details -->
  <text x="400" y="115" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1. BIOLOGICAL / PHYSICAL</text>
  <text x="400" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Anatomical structures &amp; features</text>
  <text x="400" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Puberty &amp; adolescent development</text>
  <text x="400" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Reproductive capacity &amp; procreation</text>

  <!-- Left: Emotional Dimension Details -->
  <text x="250" y="275" fill="#f472b6" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">2. EMOTIONAL</text>
  <text x="250" y="292" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Affection, love &amp; care</text>
  <text x="250" y="306" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Attraction &amp; desire for connection</text>
  <text x="250" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Empathy &amp; companionship</text>

  <!-- Right: Mental Dimension Details -->
  <text x="550" y="275" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">3. MENTAL / PSYCHOLOGICAL</text>
  <text x="550" y="292" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Self-awareness &amp; identity</text>
  <text x="550" y="306" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Moral decision-making &amp; values</text>
  <text x="550" y="320" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Understanding gender roles</text>

  <!-- Outer Annotation Cards / Pillars -->
  <!-- Left Pillar Box: God's Creation Purpose -->
  <g transform="translate(30, 110)">
    <rect width="135" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect width="135" height="28" rx="8" fill="#0284c7" fill-opacity="0.3"/>
    <text x="67" y="19" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">DIVINE PURPOSES</text>
    <text x="10" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Companionship:</text>
    <text x="10" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Relieving isolation</text>
    <text x="10" y="78" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">(Genesis 2:18)</text>
    <text x="10" y="102" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Complementarity:</text>
    <text x="10" y="117" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Mutual support &amp;</text>
    <text x="10" y="130" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">shared dignity</text>
    <text x="10" y="154" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Procreation:</text>
    <text x="10" y="169" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Fruitfulness &amp;</text>
    <text x="10" y="182" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">family continuity</text>
    <text x="10" y="206" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Sacred Covenant</text>
  </g>

  <!-- Right Pillar Box: Christian Moral Principles -->
  <g transform="translate(635, 110)">
    <rect width="135" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect width="135" height="28" rx="8" fill="#7e22ce" fill-opacity="0.3"/>
    <text x="67" y="19" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">MORAL VALUES</text>
    <text x="10" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Self-Respect:</text>
    <text x="10" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Honor body as</text>
    <text x="10" y="78" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">God's temple</text>
    <text x="10" y="102" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Self-Control:</text>
    <text x="10" y="117" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Chastity &amp; purity</text>
    <text x="10" y="130" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">during adolescence</text>
    <text x="10" y="154" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Modesty &amp; Honor:</text>
    <text x="10" y="169" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Resisting media</text>
    <text x="10" y="182" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">objectification</text>
    <text x="10" y="206" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Clear Boundaries</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="30" y="358" width="740" height="50" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="378" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">INTEGRATED CHRISTIAN VIEW: SEXUALITY IS THE ENTIRE PERSON CREATED IN GOD'S IMAGE</text>
  <text x="400" y="396" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Sexuality is not mere physical instinct; it is our complete biological, emotional, and psychological identity gifted for companionship and holiness.</text>

  <!-- Footer Tagline -->
  <text x="400" y="426" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 2: CHRISTIAN MORAL VALUES • PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


# ─── LESSON 1 DATA CONFIGURATION ─────────────────────────────────────────────

LESSON_CONFIG = {
    "unit_order": 1,
    "unit_name": "Human Sexuality as a Gift from God",
    "unit_description": "Define human sexuality from a Christian perspective, explore its biological, emotional, and mental dimensions, and analyze God's divine design for companionship, complementarity, and holiness.",
    "lesson_title": "Human Sexuality as a Gift from God",
    "image": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/93/Creation_of_Adam_and_Eve_-_Vanderbilt_ACT_-_00001394.jpg",
        "title": "Creation of Adam and Eve",
        "author": "Anne C. Richardson and Jim Womack (Jean and Alexander Heard Libraries, Vanderbilt University)",
        "licensing": "Creative Commons Attribution-Share Alike 4.0 International (CC BY-SA 4.0)",
        "source": "Wikimedia Commons",
        "caption": "A classical relief depicting God's holy creation of humanity as male and female, illustrating equal dignity, companionship, and sacred design in the Garden of Eden."
    },
    "youtube": {
        "youtube_id": "YbipxEDPryg",
        "title": "BibleProject: Image of God & The Calling of Humanity",
        "description": "Explores the biblical concept of humanity created in the Image of God (Genesis 1-2), highlighting human dignity, male-female complementarity, and sacred purpose."
    },
    "svg_fn": get_svg_triune_dimensions_of_sexuality,
    "goals": [
        "Define human sexuality and identify its three interconnected dimensions: biological, emotional, and mental/psychological.",
        "Examine Genesis 1:27-28 and Genesis 2:18-24 to explain God's divine purpose in creating male and female for companionship, equality, and holy covenant.",
        "Develop a personal action framework for cultivating self-respect, resisting negative media body-shaming, and honoring personal boundaries as a temple of the Holy Spirit."
    ],
    "intro": """Think about the changes you experience as you transition from childhood into adolescence. Your body develops new physical features, your emotions become deeper and more nuanced, and your understanding of who you are as a young man or young woman matures.

These physical, emotional, and psychological changes are part of your human sexuality. While modern culture and social media often reduce sexuality to physical attraction or external appearance, Christian Religious Education teaches that sexuality is an integral, sacred gift from God that defines our whole person and reflects His divine character.""",
    "core_scripture": """### Biblical Foundations of Human Sexuality

#### Genesis 1:27-28 — Equal Dignity and the Mandate of Creation
> *"So God created mankind in his own image, in the image of God he created them; male and female he created them. God blessed them and said to them, 'Be fruitful and increase in number; fill the earth and subdue it.'"*

#### Genesis 2:18, 21-24 — Divine Companionship and Sacred Union
> *"The Lord God said, 'It is not good for the man to be alone. I will make a helper suitable for him.' ... Then the Lord God made a woman from the rib he had taken out of the man, and he brought her to the man. The man said, 'This is now bone of my bones and flesh of my flesh; she shall be called woman, for she was taken out of man.' That is why a man leaves his father and mother and is united to his wife, and they become one flesh."*

These foundational scriptures establish that human sexuality is not an afterthought, a cultural construct, or something inherently shameful. Sexuality was purposefully instituted by God in the Garden of Eden as holy, good, and essential for human life and fellowship.""",
    "theological_pillars": """### Theological Exegesis: God's Design for Male and Female

1. **The Imago Dei (Image of God) in Equality:** Both male and female are equally created in the image and likeness of God (Genesis 1:27). Neither gender is superior or inferior; both share identical spiritual worth, moral responsibility, and divine dignity.
2. **Divine Companionship:** In Genesis 2:18, God noted that isolation was "not good" for humanity. Woman was created as a suitable partner (*ezer kenegdo*—a corresponding counterpart of equal dignity) to end loneliness and provide lifelong companionship.
3. **Complementarity:** Men and women are created with distinct yet complementary biological and emotional traits. They are designed to work together, support one another, and cooperate in fulfilling God's creation mandate.
4. **Sacred Covenant of Marriage:** Sexuality finds its complete and holy expression within the permanent, faithful covenant of marriage, where husband and wife become "one flesh" (Genesis 2:24) in mutual love and procreation.""",
    "deep_dive": """### Deep Dive: The Triune Dimensions of Human Sexuality

Christian ethics emphasizes that human sexuality engages the totality of human personhood across three interconnected dimensions:

- **1. Biological / Physiological Dimension:** Refers to the physical body structures, reproductive systems, hormones, and genetic characteristics that distinguish male and female. In adolescence, puberty triggers bodily growth, secondary sexual characteristics, and reproductive maturity designed by God.
- **2. Emotional Dimension:** Encompasses our feelings, capacity for empathy, emotional bonding, affection, and attraction. It shapes how we express love, care for family and friends, and navigate relational closeness in healthy ways.
- **3. Mental / Psychological Dimension:** Involves self-awareness, personal identity, mental maturity, and moral decision-making. It guides how a teenager perceives their worth as a male or female and determines how they respond to peer influence and moral choices.

**God's Fourfold Purpose for Human Sexuality:**
- **Companionship:** Relieving human isolation and fostering lifelong companionship (Genesis 2:18).
- **Complementarity:** Mutual enrichment and cooperation between male and female in community and family life.
- **Procreation:** Continuing the human race by raising children within a loving, secure family environment (Genesis 1:28).
- **Sacred Covenant:** Expressing deep mutual love, commitment, and spiritual unity in holy marriage (Genesis 2:24).""",
    "practical": {
        "title": "Action Framework: 4 Steps to Cultivating Self-Respect & Healthy Teenage Identity",
        "steps": [
            "Step 1: Affirm Your Divine Worth — Recognize that you are fearfully and wonderfully made in God's image (Psalm 139:14), rejecting unrealistic beauty standards on social media.",
            "Step 2: Practice Modesty and Decency — Choose attire, language, and online behavior that demonstrate self-respect and honor your body as a temple of the Holy Spirit.",
            "Step 3: Establish Firm Personal Boundaries — Guard your physical and emotional integrity by saying a firm 'NO' to inappropriate touching, sexual propositions, or exploitative relationships.",
            "Step 4: Seek Trusted Mentorship — Discuss questions about bodily changes, emotional feelings, and peer pressure with parents, CRE teachers, pastors, or responsible adult mentors."
        ]
    },
    "kenyan_context": """In Kenya today, adolescents navigate intense pressure from digital media, music videos, and peer groups that frequently glamorize premature sexual involvement, body-shaming, and indecent exposure. Christian moral values empower Kenyan teenagers to embrace self-control (*kujitawala*), preserve sexual purity, and treat members of both genders with courtesy, honor, and mutual respect in schools, churches, and neighborhoods.""",
    "reflection": """### Spiritual Reflection: The Body as a Temple of the Holy Spirit

In 1 Corinthians 6:19-20, the Bible reminds us: *"Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; you were bought at a price. Therefore honor God with your bodies."*

- How does knowing that God's Holy Spirit dwells within you transform the way you treat your physical body, what you view on your phone, and how you interact with your peers?
- In what practical ways can you support your classmates when they face body-shaming or peer pressure?""",
    "takeaways": [
        "Human sexuality is a sacred gift from God encompassing our whole biological, emotional, and psychological identity as male or female.",
        "Male and female are created in the Image of God (*Imago Dei*) with equal dignity, mutual complementarity, and shared responsibility (Genesis 1:27).",
        "God instituted sexuality for holy companionship, complementarity, procreation, and sacred marital union (Genesis 2:18-24).",
        "Christian youth honor God by maintaining sexual purity, respecting personal boundaries, and caring for their bodies as temples of the Holy Spirit."
    ],
    "mcq": {
        "question": "Which of the following best defines 'human sexuality' from a Christian Religious Education perspective?",
        "options": [
            "A) A purely physical urge that teenagers cannot control",
            "B) A sacred gift from God encompassing our biological, emotional, and mental identity as male or female",
            "C) A cultural taboo that should never be discussed openly in church or school",
            "D) An exclusively reproductive biological function with no emotional or spiritual value"
        ],
        "answer": "B",
        "explanation": "From a Christian perspective, human sexuality is a sacred gift from God that involves the whole person—including biological make-up, emotional capacity for affection, and psychological self-awareness—created for companionship, complementarity, and holiness."
    }
}


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_t2_l1():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE — TOPIC 2, LESSON 1: HUMAN SEXUALITY AS A GIFT FROM GOD")
    print("=" * 80)

    with transaction.atomic():
        # Grade 9 (ID: 18), Subject: CRE (ID: 50)
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50, grade=grade)

        # Ensure Topic 2: Christian Moral Values exists under Subject 50
        topic, created_topic = Topic.objects.get_or_create(
            subject=subject,
            order=2,
            defaults={
                "name": "Christian Moral Values",
                "description": "Explores Christian ethics regarding human sexuality, sexual purity, family values, and responsible Christian living."
            }
        )
        if created_topic:
            print(f"[+] Created Topic 2: '{topic.name}' (ID: {topic.id}) under Subject {subject.name}")
        else:
            print(f"[*] Found existing Topic 2: '{topic.name}' (ID: {topic.id})")

        print(f"Target Curriculum: {grade.curriculum.name}")
        print(f"Target Grade     : {grade.name} (ID: {grade.id})")
        print(f"Target Subject   : {subject.name} (ID: {subject.id})")
        print(f"Target Topic     : {topic.name} (ID: {topic.id}, Order: {topic.order})")

        cfg = LESSON_CONFIG
        u_order = cfg["unit_order"]
        u_name = cfg["unit_name"]
        l_title = cfg["lesson_title"]

        # Clean existing Unit 1 in Topic 2 if present
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
            description=f"Responsive pedagogical vector SVG diagram illustrating The Triune Dimensions of Human Sexuality.",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic_2_lesson_1.svg",
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
            title="Adolescent Growth & Human Identity",
            content={"markdown": clean_text(cfg["intro"])}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Core Biblical Foundations",
            content={"markdown": clean_text(cfg["core_scripture"])}
        )

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Exegesis: Divine Design for Male and Female",
            content={"markdown": clean_text(cfg["theological_pillars"])}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 3 (Page 3): Vector SVG Diagram & Deep Dive (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        b5 = LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=50, component_order=1,
            block_type="suggested_diagram", component_type="suggested_diagram",
            title=f"The Triune Dimensions of Human Sexuality",
            content={
                "title": "The Triune Dimensions of Human Sexuality",
                "caption": "A responsive vector diagram illustrating the biological, emotional, and mental dimensions of sexuality centered on God's sacred design.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Deep Dive: Exploring the Dimensions of Sexuality",
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
            title="Kenyan Real-World Context & Peer Dynamics",
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
            title="Spiritual Reflection: Temple of the Holy Spirit",
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
        print(f"  - Topic ID        : {topic.id} ('{topic.name}')")
        print(f"  - LearningUnit ID : {unit.id} ('{unit.name}')")
        print(f"  - Pages Count     : 6")
        print(f"  - Blocks Count    : {lesson.blocks.count()}")
        print(f"  - Assets Count    : {lesson.assets.count()}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_cre_t2_l1()
