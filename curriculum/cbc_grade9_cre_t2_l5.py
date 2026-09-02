"""
VLearn CBC Grade 9 CRE — Strand 2.0, Sub-Strand 2.1: Christian Moral Values (Sexual Purity)
Lesson 5: Biological and Psychological Consequences of Sexual Immorality
Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Christian Moral Values (ID: 318, Order: 2)
Learning Unit: 5 (Biological and Psychological Consequences of Sexual Immorality)
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
    # Strip bracket citations e.g. [216], [218], [519, 1161]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|SCENARIO|TIMELINE|COMPARISON)[^\]]*\]', '', text, flags=re.IGNORECASE)
    # Normalize list bullet points
    text = re.sub(r'^[ 	]*[•●○*][ 	]*', '- ', text, flags=re.MULTILINE)
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
    <linearGradient id="bioGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="psyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#5b21b6"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d9488"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="centerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="100%" stop-color="#c2410c"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#dc2626" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Background Frame -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="16"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="12"/>

  <!-- Title & Subtitle Header -->
  <text x="400" y="38" fill="#f87171" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE BIOLOGICAL &amp; PSYCHOLOGICAL CASCADE OF SEXUAL IMMORALITY</text>
  <text x="400" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">"Whoever sins sexually, sins against their own body" — 1 Corinthians 6:18</text>

  <!-- Central Root Node: Sexual Immorality -->
  <g transform="translate(310, 72)">
    <rect width="180" height="48" rx="8" fill="url(#centerGrad)" stroke="#fdba74" stroke-width="1.5" filter="url(#glow)"/>
    <text x="90" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">SEXUAL IMMORALITY</text>
    <text x="90" y="36" fill="#ffedd5" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Physical &amp; Spiritual Compromise</text>
  </g>

  <!-- Branching Connector Paths -->
  <path d="M 340 120 C 230 140, 200 150, 195 160" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 3"/>
  <path d="M 460 120 C 570 140, 600 150, 605 160" fill="none" stroke="#a78bfa" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- LEFT COLUMN: BIOLOGICAL TOLL (STIs & HIV/AIDS) -->
  <g transform="translate(35, 160)">
    <!-- Column Header -->
    <rect width="340" height="34" rx="6" fill="url(#bioGrad)"/>
    <text x="170" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BIOLOGICAL CONSEQUENCES (Pathology)</text>

    <!-- Content Box -->
    <rect y="40" width="340" height="175" rx="6" fill="#1e293b" stroke="#dc2626" stroke-width="1.2"/>

    <!-- Gonorrhea & Syphilis -->
    <text x="12" y="58" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Gonorrhea &amp; Syphilis (Bacterial)</text>
    <text x="22" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Genital discharge, burning pain; primary chancre sore</text>
    <text x="22" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Long-term: Cardiovascular damage, infertility &amp; madness</text>

    <!-- Herpes & Hepatitis B -->
    <text x="12" y="108" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Genital Herpes &amp; Hepatitis B (Viral)</text>
    <text x="22" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Recurring painful blisters; severe liver cirrhosis &amp; jaundice</text>

    <!-- HIV / AIDS -->
    <text x="12" y="144" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• HIV / AIDS (Immune Destruction)</text>
    <text x="22" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Depletes CD4+ white blood cells; opens doorway to</text>
    <text x="22" y="174" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">opportunistic infections (Tuberculosis, chronic diarrhea)</text>
    <text x="22" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Potential mother-to-child transmission &amp; early mortality</text>
  </g>

  <!-- RIGHT COLUMN: PSYCHOLOGICAL TOLL (Trauma & Distress) -->
  <g transform="translate(425, 160)">
    <!-- Column Header -->
    <rect width="340" height="34" rx="6" fill="url(#psyGrad)"/>
    <text x="170" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PSYCHOLOGICAL CONSEQUENCES (Trauma)</text>

    <!-- Content Box -->
    <rect y="40" width="340" height="175" rx="6" fill="#1e293b" stroke="#7c3aed" stroke-width="1.2"/>

    <!-- Chronic Stress & Fear -->
    <text x="12" y="58" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Chronic Stress &amp; Anxiety</text>
    <text x="22" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Persistent fear of unwanted pregnancy &amp; incurable STIs</text>
    <text x="22" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Panic over social discovery, family shame &amp; expulsion</text>

    <!-- Guilt & Low Self-Esteem -->
    <text x="12" y="108" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Guilt &amp; Shattered Self-Worth</text>
    <text x="22" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Severe loss of self-respect, feelings of defilement &amp; regret</text>

    <!-- Academic Decline & Despair -->
    <text x="12" y="144" fill="#c4b5fd" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Academic Collapse &amp; Despair</text>
    <text x="22" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Insomnia, lack of concentration, dropping out of school</text>
    <text x="22" y="174" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Deep emotional depression &amp; suicidal tendencies</text>
    <text x="22" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Social isolation and broken interpersonal trust</text>
  </g>

  <!-- Bottom Pillar: The Christian Shield of Purity & Compassion -->
  <g transform="translate(35, 385)">
    <rect width="730" height="38" rx="8" fill="url(#shieldGrad)" stroke="#34d399" stroke-width="1.2"/>
    <text x="365" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      CHRISTIAN ETHIC: Chastity / Purity for Prevention  •  Unconditional Compassion for the Infected &amp; Affected
    </text>
  </g>
</svg>"""


def ingest_grade9_cre_topic2_lesson5():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE TOPIC 2, LESSON 5: BIOLOGICAL AND PSYCHOLOGICAL CONSEQUENCES OF SEXUAL IMMORALITY")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Scope Entities
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(id=318, subject=subject)

        print(f"Target Scope: Grade '{grade.name}' (ID: {grade.id}), Subject '{subject.name}' (ID: {subject.id}), Topic '{topic.name}' (ID: {topic.id})")

        # 2. Setup / Clean Learning Unit 5
        unit_order = 5
        unit_name = "Biological and Psychological Consequences of Sexual Immorality"
        unit_description = (
            "Analyze the devastating biological and emotional effects of irresponsible sexual behaviors, "
            "focusing on Sexually Transmitted Infections (Gonorrhea, Syphilis, Herpes, Hepatitis B), "
            "HIV/AIDS opportunistic infections, psychological trauma (guilt, depression, academic decline), "
            "and the Christian duty of purity and compassionate care."
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
        lesson_title = "Biological and Psychological Consequences of Sexual Immorality"
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
        # Asset 1: Authentic Wikimedia Image Hook
        img_info = {
            "title": "Adolescent Health Counseling and Clinical STI Education",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Community_health_worker_counseling_young_people.jpg/800px-Community_health_worker_counseling_young_people.jpg",
            "caption": "A community health worker counsels youth on the medical realities of Sexually Transmitted Infections (STIs) and the vital importance of healthy choices and emotional well-being.",
            "author": "Wikimedia Commons / Community Health Outreach",
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
        svg_content = get_svg_lesson_5()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="url",
            status="attached",
            title=f"Diagram: {lesson_title}",
            description="Responsive pedagogical vector SVG diagram illustrating the biological cascade of STIs/HIV and psychological trauma resulting from sexual immorality.",
            url="https://vlearn.africa/assets/diagrams/cre/grade9_topic2_lesson_5.svg",
            metadata={
                "svg_xml": svg_content,
                "viewBox": "0 0 800 450",
                "theme": "#0f172a"
            }
        )

        # Asset 3: Curated Educational YouTube Video
        yt_info = {
            "title": "BibleProject: Compassion & The Good Samaritan (Loving the Vulnerable and Hurting)",
            "youtube_id": "osfQg4yKtq8",
            "description": "Discover the biblical heart of compassion through Jesus' teaching on the Good Samaritan, illustrating how Christians must care for those suffering from illness, stigma, and loss."
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

        # 5. Create 6 Pages with Standardized Block Types

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
                "description": "Identify and describe the major Sexually Transmitted Infections (Gonorrhea, Syphilis, Herpes Genitalis, Hepatitis B) and explain the biological mechanism of HIV/AIDS."
            },
            {
                "level": "Analyzing & Evaluating",
                "description": "Analyze the profound psychological and social trauma of sexual immorality, including chronic anxiety, guilt, academic decline, and depression."
            },
            {
                "level": "Applying & Creating",
                "description": "Formulate actionable strategies to maintain personal sexual purity while actively practicing Christlike compassion and non-discrimination toward individuals infected or affected by HIV/AIDS."
            }
        ]
        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=20, component_order=2,
            block_type="learning_goal", component_type="learning_goal",
            title="Lesson Learning Goals",
            content={"goals": clean_dict(goals_data)}
        )

        intro_text = """### The Reality of Sexual Choices: Biological and Psychological Truths

Many popular media messages, movies, and music lyrics portray sexual indulgence as a harmless adventure free from consequences. However, medical science and Christian ethics both reveal an undeniable truth: **our sexual choices carry immediate, long-lasting biological and emotional consequences**.

When sexual intimacy is removed from its sacred covenant in marriage, the human body is exposed to aggressive microbial pathogens that can permanently damage reproductive health, vital organs, and the immune system. Simultaneously, the human psyche experiences intense emotional disruption—manifesting in fear of unwanted pregnancy, pervasive guilt, anxiety, social isolation, and academic collapse.

In this lesson, we explore the scientific realities of Sexually Transmitted Infections (STIs) and HIV/AIDS, examine the psychological toll of sexual immorality, and discover the biblical call to live in sexual purity while extending Christ's unconditional compassion to all who suffer from illness and stigma."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title="Discovery & Objectives",
            order=30, component_order=3,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Introduction: The High Cost of Compromise",
            content={"markdown": clean_text(intro_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 2 (Page 2): Scriptural Exegesis & Theological Foundations (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        scripture_text = """### Scriptural Foundations: The Sacred Body and Abundant Life

The Word of God speaks directly to the profound connection between spiritual obedience, bodily health, and mental peace:

#### 1. 1 Corinthians 6:18 — Sinning Against One's Own Body
> *"Flee from sexual immorality. All other sins a person commits are outside the body, but whoever sins sexually, sins against their own body."*

#### 2. John 10:10 — The Thief vs. The Good Shepherd
> *"The thief comes only to steal and kill and destroy; I have come that they may have life, and have it to the full."*

#### 3. Proverbs 5:11-12 — The Bitterness of Regret
> *"At the end of your life you will groan, when your flesh and body are spent. You will say, 'How I hated discipline! How my heart spurned correction!'"*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=40, component_order=1,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Core Biblical Texts on Bodily Purity",
            content={"markdown": clean_text(scripture_text)}
        )

        theological_exegesis_text = """### Theological Exegesis: Understanding "Sinning Against One's Own Body"

The Apostle Paul's warning in **1 Corinthians 6:18** provides deep theological and physiological insight into human design:

- **The Uniqueness of Sexual Sins:**
  While sins such as theft or lying primarily target external people and property, sexual immorality directly engages the intimate biological, neurological, and spiritual core of the human person. The body is the temple of the Holy Spirit (1 Corinthians 6:19); defiling it through immorality introduces physical infection, psychological guilt, and spiritual alienation.

- **The Destruction of the Thief vs. Abundant Life (John 10:10):**
  Jesus contrasts Satan's deceptive agenda—which uses temporary physical pleasure to steal health, kill potential, and destroy futures—with His divine purpose: granting **abundant, holistic life** (*zoe*). Walking in obedience and purity protects a young person's physical vitality, emotional stability, and spiritual destiny.

- **The Harmony of Purity and Divine Peace:**
  God's moral commandments are not designed to restrict our happiness, but to protect us. Biblical chastity acts as a divine shield guarding our biological organs from incurable pathogens and preserving our mental peace from toxic guilt and anxiety."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
            order=45, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Theological Analysis: The Architecture of Moral Purity",
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
                "title": "The Biological & Psychological Cascade of Sexual Immorality",
                "caption": "A structured vector diagram illustrating how irresponsible sexual behavior triggers a double cascade of biological pathogens (STIs, HIV/AIDS) and psychological trauma (stress, guilt, academic decline).",
                "svg": svg_content,
                "svg_xml": svg_content
            }
        )
        b5.assets.add(svg_asset)

        deep_dive_text = """### In-Depth Scientific and Psychological Analysis

Sexual immorality results in tangible biological pathologies and severe mental health distress:

#### 1. Major Sexually Transmitted Infections (STIs)
- **Gonorrhea (*Neisseria gonorrhoeae*):**
  - *Incubation & Symptoms:* Symptoms manifest roughly 2 to 7 days following infection. Involves acute burning sensation during urination, genital inflammation, and thick yellowish or greenish pus discharge.
  - *Long-Term Pathology:* If untreated, the bacterium ascends the reproductive tract, causing pelvic inflammatory disease (PID) in females and epididymitis in males, culminating in permanent infertility. It is curable with specific antibiotics if detected early.
- **Syphilis (*Treponema pallidum*):**
  - *Primary Stage:* A painless open sore (chancre) appears at the infection site. The sore naturally heals after a few weeks, deceiving the individual into believing they are cured.
  - *Latent & Tertiary Stages:* The spirochete bacteria remain hidden in the bloodstream for up to 7 to 10 years, eventually attacking the cardiovascular system, central nervous system, brain, and spinal cord, causing blindness, heart failure, paralysis, and severe madness.
- **Herpes Genitalis (Herpes Simplex Virus - HSV-2):**
  - Characterized by recurring outbreaks of painful, burning clusters of blisters and ulcers in the genital and anal regions.
  - *Medical Status:* HSV-2 has **no permanent cure**; the virus remains dormant in nerve ganglia and reactivates during periods of stress or lowered immunity.
- **Hepatitis B (Hepatitis B Virus - HBV):**
  - A highly infectious virus transmitted through sexual fluids and contaminated blood.
  - *Pathology:* Specifically targets and destroys liver hepatocytes, causing acute jaundice (yellowing of eyes and skin), abdominal pain, chronic fatigue, liver cirrhosis, liver cancer, and death. There is an effective preventive vaccine, but no cure once chronic infection establishes.

#### 2. HIV/AIDS and Opportunistic Infections
- **Biological Mechanism:** Human Immunodeficiency Virus (HIV) selectively infects and destroys CD4+ T-helper lymphocytes, the vital command cells of the human immune system.
- **Progression to AIDS:** When the CD4 cell count drops drastically, the immune defense collapses, leading to Acquired Immunodeficiency Syndrome (AIDS). The patient becomes vulnerable to **opportunistic infections**—pathogens that a healthy body easily repels:
  - Pulmonary and extrapulmonary Tuberculosis (TB)
  - Chronic, debilitating diarrhea and rapid wasting syndrome (drastic weight loss)
  - Severe fungal infections (Oral and esophageal candidiasis)
  - Opportunistic malignancies such as Kaposi's sarcoma

#### 3. Psychological and Emotional Trauma
The psychological damage of sexual immorality often equals or exceeds the physical toll:
- **Chronic Stress & Panic:** Constant anxiety regarding potential pregnancy, fear of contracting incurable diseases, and dread of discovery by parents, teachers, and peers.
- **Low Self-Esteem & Toxic Guilt:** Feelings of personal defilement, worthlessness, self-reproach, and loss of moral integrity.
- **Academic Collapse:** Severe concentration impairment, chronic insomnia, school absenteeism, and sudden drop in academic grades.
- **Severe Depression & Suicidal Ideation:** Overwhelming feelings of hopelessness and social isolation leading to clinical depression and self-harm."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
            order=60, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Comprehensive Medical and Psychological Breakdown",
            content={"markdown": clean_text(deep_dive_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 4 (Page 4): Practical Application & Kenyan Context (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        practical_framework = {
            "title": "4 Pillars of Christian Care & Non-Discrimination for HIV/AIDS",
            "description": "A comprehensive Christian action model for responding to the HIV/AIDS epidemic with unconditional compassion, medical support, and community dignity.",
            "steps": [
                {
                    "step_number": 1,
                    "name": "Eradicating Stigma & Rejection",
                    "description": "Emulate Jesus Christ by welcoming, embracing, and sitting with people living with HIV/AIDS, actively debunking myths that HIV is spread through casual contact, sharing meals, or handshakes."
                },
                {
                    "step_number": 2,
                    "name": "Holistic Support for Orphans & Vulnerable Children (OVCs)",
                    "description": "Provide tangible material, educational, and emotional assistance to children who have lost parents to HIV/AIDS, sharing school supplies, food, and mentorship without gossip or condescension."
                },
                {
                    "step_number": 3,
                    "name": "Promoting Voluntary Medical Testing & Adherence",
                    "description": "Encourage voluntary counseling and testing (VCT) and support individuals living with HIV in strictly adhering to Antiretroviral Therapy (ART) regimens to achieve viral suppression and healthy living."
                },
                {
                    "step_number": 4,
                    "name": "Spiritual Affirmation & Pastoral Accompaniment",
                    "description": "Affirm that every individual possesses inherent dignity as God's image-bearer (Imago Dei), offering prayers, hope, and pastoral care rather than judgmental condemnation."
                }
            ]
        }
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=70, component_order=1,
            block_type="step_process", component_type="step_process",
            title="Action Framework: 4 Pillars of Christian Care",
            content=clean_dict(practical_framework)
        )

        kenyan_context_text = """### Kenyan Real-World Application: Overcoming Stigma and Living with Compassion

In Kenya, the battle against HIV/AIDS and STIs is both a public health effort and a profound moral calling:

1. **National Progress and Continuing Challenges:**
   Kenya has made massive strides through the National AIDS and STI Control Programme (NASCOP) and widespread availability of free Antiretroviral Therapy (ART) in public health centers. However, stigma in schools and communities remains a major hurdle. When young people fear being judged, they avoid medical testing and counseling.

2. **The Christian Witness in the Classroom:**
   In your school or neighborhood, you may encounter classmates whose lives have been touched by HIV/AIDS—either living with the condition or caring for sick relatives as orphans:
   - **Never isolate or mock:** Do not use derogatory language or whisper about someone's health status.
   - **Share daily activities:** Share desks, textbooks, sports equipment, and meals freely; HIV cannot be transmitted through ordinary social contact.
   - **Offer practical help:** Assist peers who miss school due to clinic appointments by sharing class notes and revision materials.

3. **Practicing Personal Abstinence:**
   While extending 100% compassion to those infected, the single most effective, 100% fail-safe shield for unmarried adolescents is **complete sexual abstinence (chastity)**. By guarding your heart and body, you preserve your health and honor God."""

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title="Practical Application",
            order=75, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Kenyan Real-World Context: Compassion in Action",
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

        reflection_text = """### Personal Spiritual Reflection: Purity in the Heart, Compassion in the Hands

Take a quiet moment to reflect on your attitudes toward your own body and toward those who are suffering around you:

- **Evaluating Your Personal Boundaries:**
  Do you treat your body with reverence as the sacred dwelling place of God's Spirit? Are you guarding your eyes, thoughts, and friendships against influences that pressure you toward sexual compromise?

- **Reflecting Christ's Compassion:**
  When you see someone who is sick, vulnerable, or marginalized by society, is your first reaction judgment or Christlike compassion? Remember that Jesus touched the lepers whom society cast out and restored them with love.

> **Prayer for Purity and Compassion:**
> *"Heavenly Father, You have formed my body and called me to live in holiness and peace. Grant me the spiritual strength and self-control to flee from sexual temptation and preserve my body in purity. Fill my heart with Your unconditional love, so that I may always extend compassion, kindness, and support to those who are suffering from illness, stigma, and loss. In Jesus' name, Amen."*"""

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
            order=90, component_order=2,
            block_type="concept_explanation", component_type="concept_explanation",
            title="Spiritual Reflection: Walking in Holiness and Love",
            content={"markdown": clean_text(reflection_text)}
        )

        # ───────────────────────────────────────────────────────────────────
        # CARD 6 (Page 6): Review & Mastery Check (2 blocks)
        # ───────────────────────────────────────────────────────────────────
        takeaways_data = [
            "Sexual immorality brings severe biological pathologies, including bacterial STIs (Gonorrhea, Syphilis) and viral infections (Herpes Genitalis, Hepatitis B, HIV/AIDS).",
            "HIV directly attacks CD4+ white blood cells, leaving the body defenseless against deadly opportunistic infections such as Tuberculosis and chronic diarrhea.",
            "Sexual sin inflicts intense psychological trauma, including persistent anxiety, guilt, loss of self-esteem, academic failure, and clinical depression (1 Corinthians 6:18).",
            "Christians have a sacred duty to maintain 100% sexual purity through abstinence while demonstrating unconditional love and non-discrimination toward those living with HIV/AIDS.",
            "Ending stigma, supporting AIDS orphans, and promoting medical compassion are vital expressions of authentic Christian discipleship."
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
            "question": "Why is Hepatitis B considered an especially dangerous Sexually Transmitted Infection (STI) from a medical standpoint?",
            "options": [
                {
                    "label": "A",
                    "text": "It is an airborne infection that primarily damages the lungs and causes immediate hair loss."
                },
                {
                    "label": "B",
                    "text": "It severely damages the liver, causing jaundice and cirrhosis, has no cure once chronic infection establishes, and can be fatal."
                },
                {
                    "label": "C",
                    "text": "It is easily cured within 24 hours using mild over-the-counter painkillers."
                },
                {
                    "label": "D",
                    "text": "It only affects elderly individuals and is transmitted exclusively through contaminated drinking water."
                }
            ],
            "correct_answer": "B",
            "explanation": "Option B is correct. Hepatitis B is a viral infection transmitted through sexual fluids and infected blood that attacks liver cells, causing severe liver inflammation, cirrhosis, liver cancer, and death. While an effective preventive vaccine exists, there is no permanent cure once a chronic infection takes hold. Options A, C, and D are factually and medically incorrect."
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
    ingest_grade9_cre_topic2_lesson5()
