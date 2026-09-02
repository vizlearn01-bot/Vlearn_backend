"""
VLearn CBC Grade 9 CRE — Topic 1: Work
Lesson 1: Understanding Work, Vocation, and Careers

Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Work (ID: 316, Order: 1)
Learning Unit: 1.1 Understanding Work, Vocation, and Careers (Order: 1)
Lesson: Understanding Work, Vocation, and Careers (Order: 1, 6 Cards/Pages, 13 Blocks, 3 Assets)
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
    # Strip bracket citations e.g. [181], [181, 183], [182]
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

def get_svg_spectrum_of_labor():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE SPECTRUM OF LABOR: FROM TASK TO DIVINE CALLING</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Understanding How Work Evolves from Daily Tasks to Purpose-Driven Christian Vocation</text>

  <!-- Progression Flow Arrows (Connecting Line) -->
  <path d="M 140 215 L 285 215 M 395 215 L 435 215 M 545 215 L 590 215" stroke="#475569" stroke-width="3" stroke-dasharray="6 4"/>
  <polygon points="288,215 278,209 278,221" fill="#38bdf8"/>
  <polygon points="438,215 428,209 428,221" fill="#34d399"/>
  <polygon points="593,215 583,209 583,221" fill="#fbbf24"/>

  <!-- 4 Stage Cards -->

  <!-- CARD 1: JOB -->
  <g transform="translate(30, 95)">
    <rect width="180" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="34" rx="10" fill="url(#blueGrad)"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. JOB</text>

    <!-- Badge / Subtitle -->
    <rect x="25" y="46" width="130" height="20" rx="10" fill="#0284c7" fill-opacity="0.25"/>
    <text x="90" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Immediate Wage</text>

    <text x="12" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Definition:</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Specific tasks rendered</text>
    <text x="12" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">in return for pay/wages.</text>

    <text x="12" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Horizon:</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Short-term, transactional,</text>
    <text x="12" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">temporary or casual.</text>

    <text x="12" y="204" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Motivation:</text>
    <text x="12" y="220" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="10.5">Basic survival &amp; income.</text>
  </g>

  <!-- CARD 2: CRAFT & TRADE -->
  <g transform="translate(225, 95)">
    <rect width="170" height="240" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="url(#emeraldGrad)"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">2. CRAFT &amp; TRADE</text>

    <rect x="20" y="46" width="130" height="20" rx="10" fill="#059669" fill-opacity="0.25"/>
    <text x="85" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Manual &amp; Applied Skill</text>

    <text x="12" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Craft:</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Manipulative hand skills</text>
    <text x="12" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">(pottery, woodcarving).</text>

    <text x="12" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Trade:</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Practical technical vocation</text>
    <text x="12" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">(carpentry, masonry, TVET).</text>

    <text x="12" y="204" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Value:</text>
    <text x="12" y="220" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10.5">Practical problem solving.</text>
  </g>

  <!-- CARD 3: CAREER & PROFESSION -->
  <g transform="translate(410, 95)">
    <rect width="175" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="175" height="34" rx="10" fill="url(#amberGrad)"/>
    <text x="87" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. CAREER / PROFESSION</text>

    <rect x="20" y="46" width="135" height="20" rx="10" fill="#d97706" fill-opacity="0.25"/>
    <text x="87" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Lifelong Growth &amp; Ethics</text>

    <text x="12" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Career:</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Long-term journey of</text>
    <text x="12" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">progressive occupations.</text>

    <text x="12" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Profession:</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Advanced specialized study,</text>
    <text x="12" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">strict ethical code &amp; board.</text>

    <text x="12" y="204" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Focus:</text>
    <text x="12" y="220" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10.5">Professional excellence.</text>
  </g>

  <!-- CARD 4: VOCATION (CALLING) -->
  <g transform="translate(600, 95)">
    <rect width="170" height="240" rx="10" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
    <rect width="170" height="34" rx="10" fill="url(#purpleGrad)"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">4. VOCATION</text>

    <rect x="20" y="46" width="130" height="20" rx="10" fill="#7c3aed" fill-opacity="0.3"/>
    <text x="85" y="60" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Divine Calling (Vocare)</text>

    <text x="12" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Meaning:</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">God's personal invitation</text>
    <text x="12" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">to serve Him and society.</text>

    <text x="12" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Perspective:</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Work as holy worship &amp;</text>
    <text x="12" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">service (Col 3:23).</text>

    <text x="12" y="204" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">• Crown:</text>
    <text x="12" y="220" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10.5">Eternal kingdom impact.</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="30" y="355" width="740" height="52" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="376" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">COLOSSIANS 3:23 INTEGRATION: "WHATEVER YOU DO, WORK AT IT WITH ALL YOUR HEART, AS WORKING FOR THE LORD"</text>
  <text x="400" y="394" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Any honest job or craft is elevated into a holy vocation when performed with diligence, integrity, and love for others.</text>

  <!-- Footer Tagline -->
  <text x="400" y="426" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 1: WORK • PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


# ─── LESSON 1 DATA CONFIGURATION ─────────────────────────────────────────────

LESSON_CONFIG = {
    "unit_order": 1,
    "unit_name": "Understanding Work, Vocation, and Careers",
    "unit_description": "Define and distinguish between work, vocation, profession, trade, craft, career, and job, exploring the Christian perspective of work as a divine calling.",
    "lesson_title": "Understanding Work, Vocation, and Careers",
    "image": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Joseph_the_Carpenter_by_Georges_de_La_Tour.jpg/800px-Joseph_the_Carpenter_by_Georges_de_La_Tour.jpg",
        "title": "Visual Hook: Saint Joseph the Carpenter",
        "author": "Georges de La Tour (Musée du Louvre)",
        "licensing": "Public Domain",
        "source": "Wikimedia Commons",
        "caption": "A master craftsman shaping wood in his workshop, demonstrating the manual skill, focus, and sacred dignity of daily labor."
    },
    "youtube": {
        "youtube_id": "YbipxEDPryg",
        "title": "BibleProject: Image of God & The Calling of Humanity",
        "description": "Explores how God created humans in His image and commissioned them to cultivate, steward, and co-rule creation as a divine vocation."
    },
    "svg_fn": get_svg_spectrum_of_labor,
    "goals": [
        "Define and distinguish between work, vocation, profession, trade, craft, career, and job.",
        "Analyze Genesis 1:28, Genesis 2:15, and Colossians 3:23 to explain how Christian theology frames human labor as a divine mandate and stewardship.",
        "Develop a practical framework for identifying personal talents and selecting a career path grounded in service to God and the Kenyan community."
    ],
    "intro": "Think about the activities you engage in from the moment you wake up: sweeping your bedroom, washing dishes, tending to crops on the shamba, solving mathematics problems, or helping a neighbor fix a broken gate. All of these require physical energy, mental concentration, and skill.\n\nAre all these activities 'work'? Why do people engage in labor? While many people assume work exists solely to earn money or put food on the table, Christian Religious Education reveals that work has a far deeper spiritual meaning: it shapes human identity, reflects the character of God, and enables us to serve our families and society.",
    "core_scripture": "### Biblical Foundations of Work\n\n#### Genesis 1:28 — The Creation Mandate\n> *\"God blessed them and said to them, 'Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the sky and over every living creature that moves on the ground.'\"*\n\n#### Genesis 2:15 — The Purpose in the Garden\n> *\"The Lord God took the man and put him in the Garden of Eden to work it and take care of it.\"*\n\n#### Colossians 3:23 — Working with Excellence for the Lord\n> *\"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters.\"*\n\nThese biblical passages establish that work is not a curse or punishment. Work was instituted in the Garden of Eden before the fall of humanity as an honorable partnership with God to develop and safeguard creation.",
    "theological_pillars": "### Theological Dimensions of Labor & Calling\n\n1. **God as the First Worker:** In the opening pages of Genesis, God is revealed as a worker who designs, crafts, orders, and creates the universe. Because humans are made in God's image (*Imago Dei*), working is essential to our humanity.\n2. **Human Co-Creatorship & Stewardship:** Genesis 2:15 shows that God entrusted Adam and Eve with the responsibility to *cultivate* (develop) and *guard* (protect) creation. Human labor continues God's ongoing work of sustaining the world.\n3. **Work as Worship and Vocation:** The Latin root *\"Vocare\"* means *to call*. In the Christian worldview, every person is called by God to use their talents in service. Labor done with honesty and diligence is an act of spiritual worship (Colossians 3:23).",
    "deep_dive": "### Deep Dive: Categorizing the Dimensions of Labor\n\nTo understand our roles in society and navigate our future choices, we distinguish between key terms in Christian ethics:\n\n- **Work:** The application of physical or mental energy to accomplish a purposeful task that improves human life and develops creation.\n- **Vocation:** Derived from Latin *Vocare* (to call). A person's divine life-calling from God where their unique passions, talents, and ethical commitments intersect with the needs of the world.\n- **Profession:** An occupation requiring extensive specialized academic training, mastery of complex knowledge, formal licensing, and strict adherence to a public code of ethics (e.g., medicine, law, engineering, teaching).\n- **Trade:** A skilled practical occupation typically acquired through technical training, apprenticeships, and vocational institutes (e.g., electrical installation, plumbing, hairdressing, masonry).\n- **Craft:** An occupation requiring manipulative manual skill and artistic handcraft to create tangible goods (e.g., pottery, woodcarving, basketry, tailoring).\n- **Career:** The progressive, lifelong journey of learning, job experiences, and occupational milestones that a person pursues throughout their working life.\n- **Job:** Specific duties and tasks performed on a temporary, contract, or permanent basis in exchange for agreed remuneration (wages or salary).",
    "practical": {
        "title": "Action Framework: Discerning Your Calling & Career Pathway",
        "steps": [
            "Step 1: Discover Your God-Given Talents — Reflect on the natural gifts, academic subjects, and practical skills that you enjoy and perform with excellence.",
            "Step 2: Identify Community Needs — Observe the challenges facing your family, school, and neighborhood (e.g., healthcare access, food security, environmental conservation, technical repair).",
            "Step 3: Align Passion with Service — Choose career options where your skills provide meaningful solutions rather than seeking wealth or prestige alone.",
            "Step 4: Pursue Diligent Training — Commit to disciplined study and technical skill acquisition, dedicating every effort to God as an act of faithful stewardship."
        ]
    },
    "kenyan_context": "In Kenya today, the Competency Based Curriculum (CBC) and Technical and Vocational Education and Training (TVET) institutions emphasize that all forms of honest labor are equally honorable. Whether a young person becomes a software engineer, an agricultural entrepreneur, a welder, or a healthcare worker, their labor contributes directly to Vision 2030 and honors God when performed with integrity and excellence.",
    "reflection": "### Ethical Dilemma & Personal Reflection\n\nImagine a student named Baraka who loves agriculture and mechanics, but his friends tell him that working on a farm or fixing engines is 'dirty work' and that he should only aim for an office desk job in the city.\n\n- How does the biblical teaching on work challenge the attitude of Baraka's friends?\n- In what ways does viewing your daily school studies as preparation for God's calling change your attitude toward challenging subjects?",
    "takeaways": [
        "Work is the use of physical or mental energy to improve human life and fulfill God's mandate of creation stewardship (Genesis 1:28, 2:15).",
        "A vocation (from Latin Vocare, 'to call') is a divine life-mission where a person's talents are dedicated to serving God and society.",
        "Labor encompasses diverse forms: jobs (tasks for wages), trades (technical skills), crafts (manual handiwork), and professions (ethics and high training).",
        "Christian ethics elevates all honest labor into an act of worship when performed diligently for the Lord (Colossians 3:23)."
    ],
    "mcq": {
        "question": "Which term specifically refers to an occupation that requires manual dexterity and manipulative hand skills to produce goods, such as woodcarving or pottery?",
        "options": [
            "A) Profession",
            "B) Vocation",
            "C) Craft",
            "D) Job"
        ],
        "answer": "C",
        "explanation": "A craft specifically involves manual, manipulative skills and handiwork to produce tangible items (such as pottery, weaving, or woodcarving), whereas a profession requires advanced academic training, a job is a paid position, and a vocation is a divine calling."
    }
}


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_t1_l1():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE — TOPIC 1, LESSON 1: WORK, VOCATION, AND CAREERS")
    print("=" * 80)

    with transaction.atomic():
        # Grade 9 (ID: 18), Subject: CRE (ID: 50)
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50, grade=grade)
        topic = Topic.objects.get(id=316, subject=subject)

        print(f"Target Curriculum: {grade.curriculum.name}")
        print(f"Target Grade     : {grade.name} (ID: {grade.id})")
        print(f"Target Subject   : {subject.name} (ID: {subject.id})")
        print(f"Target Topic     : {topic.name} (ID: {topic.id}, Order: {topic.order})")

        cfg = LESSON_CONFIG
        u_order = cfg["unit_order"]
        u_name = cfg["unit_name"]
        l_title = cfg["lesson_title"]

        # Clean existing Unit 1 if present
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
                "topic_order": 1,
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
            description=f"Responsive pedagogical vector SVG diagram illustrating The Spectrum of Labor.",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic_1_lesson_1.svg",
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
            title="Sharing Experiences & Familiar Connection",
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
            title="Theological Dimensions of Labor & Calling",
            content={"markdown": clean_text(cfg["theological_pillars"])}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 3 (Page 3): Vector SVG Diagram & Deep Dive (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        b5 = LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=50, component_order=1,
            block_type="suggested_diagram", component_type="suggested_diagram",
            title=f"The Spectrum of Labor: From Task to Calling",
            content={
                "title": "The Spectrum of Labor: Job -> Career -> Vocation",
                "caption": "A comprehensive conceptual spectrum showing how daily tasks evolve into lifetime vocations.",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Vector SVG Diagram & Deep Dive",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Deep Dive: Categorizing the Dimensions of Labor",
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
            title="Kenyan Real-World Context & Technical Trades",
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
            title="Ethical Reflection & Viewing Studies as Calling",
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
    ingest_grade9_cre_t1_l1()
