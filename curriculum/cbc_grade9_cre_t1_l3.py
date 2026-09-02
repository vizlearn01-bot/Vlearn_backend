"""
VLearn CBC Grade 9 CRE — Topic 1: Work
Lesson 3: Virtues, Ethics, and Professional Ethos
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

# High quality responsive SVG Diagram: The Pillars of Workplace Integrity
SVG_PILLARS_DIAGRAM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="pillarLeftGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="pillarRightGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="apexGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="baseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="12" />

  <!-- Header Section -->
  <text x="400" y="34" text-anchor="middle" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="19" font-weight="700" letter-spacing="0.5">
    The Pillars of Workplace Integrity
  </text>
  <text x="400" y="54" text-anchor="middle" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12.5">
    Harmonizing External Professional Codes with Internal Christian Virtues
  </text>

  <!-- Top Apex: The Trustworthy Professional & Thriving Society -->
  <g transform="translate(100, 68)">
    <rect width="600" height="52" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.8" filter="url(#cardShadow)"/>
    <rect width="600" height="24" rx="10" fill="url(#apexGrad)"/>
    <rect width="600" height="10" y="14" fill="url(#apexGrad)"/>
    <text x="300" y="17" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700">
      APEX GOAL: The Trustworthy Professional &amp; Corruption-Free Society
    </text>
    <text x="300" y="40" text-anchor="middle" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11.5" font-weight="500">
      High Public Trust &bull; Quality Service Delivery &bull; Moral Excellence &bull; Divine Blessing
    </text>
  </g>

  <!-- Connecting Lines / Energy Flow -->
  <path d="M 210 170 L 300 120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5 5" fill="none" opacity="0.8"/>
  <path d="M 590 170 L 500 120" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="5 5" fill="none" opacity="0.8"/>

  <!-- Left Pillar: External Professional Codes -->
  <g transform="translate(30, 135)">
    <rect width="355" height="215" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect width="355" height="34" rx="10" fill="url(#pillarLeftGrad)"/>
    <rect width="355" height="12" y="22" fill="url(#pillarLeftGrad)"/>
    <text x="177" y="22" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700">
      PILLAR 1: Professional Codes (External Rules)
    </text>

    <g transform="translate(15, 48)" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11.5">
      <circle cx="6" cy="6" r="3.5" fill="#38bdf8"/>
      <text x="18" y="10" font-weight="600" fill="#7dd3fc">Regulatory Standards:</text>
      <text x="18" y="24" fill="#cbd5e1" font-size="11">Written rules enforced by statutory bodies (TSC, KMPDC, LSK).</text>

      <circle cx="6" cy="42" r="3.5" fill="#38bdf8"/>
      <text x="18" y="46" font-weight="600" fill="#7dd3fc">Client Protection:</text>
      <text x="18" y="60" fill="#cbd5e1" font-size="11">Safeguards patients, students, and citizens from exploitation.</text>

      <circle cx="6" cy="78" r="3.5" fill="#38bdf8"/>
      <text x="18" y="82" font-weight="600" fill="#7dd3fc">Anti-Corruption Firewall:</text>
      <text x="18" y="96" fill="#cbd5e1" font-size="11">Shields professionals from bribery, extortion, and malpractice.</text>

      <circle cx="6" cy="114" r="3.5" fill="#38bdf8"/>
      <text x="18" y="118" font-weight="600" fill="#7dd3fc">Disciplinary Benchmark:</text>
      <text x="18" y="132" fill="#cbd5e1" font-size="11">Clear legal framework for sanctioning and revoking licenses.</text>
    </g>
  </g>

  <!-- Right Pillar: Internal Christian Virtues -->
  <g transform="translate(415, 135)">
    <rect width="355" height="215" rx="10" fill="#1e293b" stroke="#d97706" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect width="355" height="34" rx="10" fill="url(#pillarRightGrad)"/>
    <rect width="355" height="12" y="22" fill="url(#pillarRightGrad)"/>
    <text x="177" y="22" text-anchor="middle" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700">
      PILLAR 2: Christian Virtues (Internal Character)
    </text>

    <g transform="translate(15, 48)" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11.5">
      <circle cx="6" cy="6" r="3.5" fill="#fbbf24"/>
      <text x="18" y="10" font-weight="600" fill="#fde68a">Honesty &amp; Integrity:</text>
      <text x="18" y="24" fill="#cbd5e1" font-size="11">Accurate scales (Prov 11:1); doing right when unmonitored.</text>

      <circle cx="6" cy="42" r="3.5" fill="#fbbf24"/>
      <text x="18" y="46" font-weight="600" fill="#fde68a">Diligence &amp; Skill:</text>
      <text x="18" y="60" fill="#cbd5e1" font-size="11">Working thoroughly as unto the Lord to stand before kings (Prov 22:29).</text>

      <circle cx="6" cy="78" r="3.5" fill="#fbbf24"/>
      <text x="18" y="82" font-weight="600" fill="#fde68a">Faithfulness &amp; Loyalty:</text>
      <text x="18" y="96" fill="#cbd5e1" font-size="11">Honoring covenants, confidentiality, and institutional resources.</text>

      <circle cx="6" cy="114" r="3.5" fill="#fbbf24"/>
      <text x="18" y="118" font-weight="600" fill="#fde68a">Responsibility &amp; Tolerance:</text>
      <text x="18" y="132" fill="#cbd5e1" font-size="11">Serving all clients equitably with empathy, patience, and humility.</text>
    </g>
  </g>

  <!-- Bottom Base: Foundational Scriptural & Moral Architecture -->
  <g transform="translate(30, 360)">
    <rect width="740" height="72" rx="10" fill="url(#baseGrad)" stroke="#475569" stroke-width="1.2" filter="url(#cardShadow)"/>
    <text x="370" y="23" text-anchor="middle" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700">
      FOUNDATION: Godly Stewardship &bull; Transformative Labor (Ephesians 4:28)
    </text>
    <text x="370" y="45" text-anchor="middle" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">
      Written codes mandate compliance &bull; Biblical virtues inspire heart transformation &bull; Together they secure lasting integrity.
    </text>
  </g>
</svg>"""

LESSON_DATA = {
    "unit_order": 3,
    "unit_name": "Virtues, Ethics, and Professional Ethos",
    "unit_description": "Explaining the role of Christian virtues, professional codes of ethics, and professional ethos in guiding human labor, maintaining standards, and eliminating corruption.",
    "lesson_title": "Virtues, Ethics, and Professional Ethos",
    "pages": [
        # Page 1: Discovery & Objectives
        [
            {
                "type": "suggested_image",
                "title": "Medical Professional Upholding Ethical Standards",
                "content": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Female_African_Doctor_in_a_Laboratory_Hopital_Douala.jpg",
                    "caption": "A dedicated healthcare professional conducting vital diagnostic work, exemplifying the high standards of professional ethics, competence, and service in medicine.",
                    "author": "Wikimedia Commons / Max F. Nougues",
                    "licensing": "Creative Commons Attribution-Share Alike 4.0 International"
                }
            },
            {
                "type": "learning_goal",
                "title": "Lesson Learning Goals",
                "content": {
                    "goals": [
                        "Define **professional ethics**, **professional ethos**, and **professional codes of conduct** within the workplace.",
                        "Analyze key **Christian virtues** related to work, including diligence, honesty, integrity, faithfulness, responsibility, and tolerance.",
                        "Evaluate the crucial role of professional codes in regulating behavior, safeguarding client rights, resisting corruption, and maintaining public trust."
                    ]
                }
            },
            {
                "type": "concept_explanation",
                "title": "The Foundation of Workplace Trust",
                "content": {
                    "text": (
                        "When you visit a hospital for medical treatment, enter a courtroom seeking justice, or board a school bus, "
                        "you place your life, safety, and future into the hands of professionals. Why do you trust that a doctor will prescribe "
                        "the right medicine rather than an expired drug? Why do you trust that a civil engineer has used genuine cement rather than "
                        "substandard sand when building a multi-storey bridge or classroom?\n\n"
                        "This profound public trust is not accidental. It is maintained through two vital pillars: **external professional codes** "
                        "(enforceable statutory rules) and **internal Christian virtues** (godly character and conscience). Without ethical boundaries, "
                        "skills and knowledge become dangerous tools for extortion and exploitation. In this lesson, we discover how Christian principles "
                        "and professional ethics unite to build honest, honorable, and flourishing workplaces."
                    )
                }
            }
        ],

        # Page 2: Scriptural Exegesis
        [
            {
                "type": "concept_explanation",
                "title": "Scriptural Foundations: Honesty, Diligence, and Faithful Stewardship",
                "content": {
                    "text": (
                        "### Key Biblical Passages on Workplace Ethics\n\n"
                        "**Proverbs 11:1**\n"
                        "> *\"The Lord detests dishonest scales, but accurate weights find favor with him.\"*\n\n"
                        "**Proverbs 22:29**\n"
                        "> *\"Do you see someone skilled in their work? They will serve before kings; they will not serve before officials of low rank.\"*\n\n"
                        "**Ephesians 4:28**\n"
                        "> *\"Anyone who has been stealing must steal no longer, but must work, doing something useful with their own hands, that they may have something to share with those in need.\"*"
                    )
                }
            },
            {
                "type": "concept_explanation",
                "title": "Theological Exegesis: Divine Justice in the Marketplace",
                "content": {
                    "text": (
                        "The scriptures provide profound theological wisdom regarding how believers must conduct themselves in their careers:\n\n"
                        "1. **Accurate Scales and Divine Holiness (Proverbs 11:1):** In ancient commercial markets, merchants used stone weights on balancing scales to measure grain, oil, and precious metals. Corrupt traders used heavier stones when buying and lighter stones when selling, cheating vulnerable customers. The Bible declares that God *detests* deceitful business practices. God's character is absolute truth and fairness; therefore, every transaction, bill, audit, and medical dosage must reflect uncompromising honesty.\n\n"
                        "2. **Diligence and Excellence as a Witness (Proverbs 22:29):** The Hebrew term *mahir* denotes a worker who is prompt, highly skilled, disciplined, and thorough. True Christian spirituality does not produce sloppy or mediocre work. When a believer cultivates outstanding craftsmanship and reliable diligence, their work is recognized at the highest levels of leadership, bringing glory to God.\n\n"
                        "3. **Transforming from Parasite to Giver (Ephesians 4:28):** The Apostle Paul outlines a radical moral conversion. In the pagan world, theft, shortcuts, and exploitation were commonplace. In Christ, labor is redeemed: the former thief stops exploiting others, works diligently with their hands, and becomes a generous benefactor who uplifts the poor and vulnerable."
                    )
                }
            }
        ],

        # Page 3: Vector SVG Diagram & Deep Dive
        [
            {
                "type": "suggested_diagram",
                "title": "The Pillars of Workplace Integrity: Professional Codes & Christian Virtues",
                "content": {
                    "caption": "A structured vector diagram illustrating how external regulatory codes and internal Christian virtues combine to sustain ethical excellence and public trust.",
                    "svg_content": SVG_PILLARS_DIAGRAM
                }
            },
            {
                "type": "concept_explanation",
                "title": "Deep Dive: Defining Ethics, Ethos, Codes, and Core Virtues",
                "content": {
                    "text": (
                        "### Core Definitions in Workplace Ethics\n\n"
                        "- **Professional Ethics:** The recognized principles and standards of right conduct that govern members of a particular profession, clearly outlining permissible and prohibited actions.\n"
                        "- **Professional Ethos:** The distinctive group character, moral tone, guiding beliefs, and cultural identity that define a specific professional community (e.g., the compassionate bedside manner of nursing or the solemn impartiality of the judiciary).\n"
                        "- **Professional Code of Conduct:** A formalized, systematically arranged statutory document detailing the mandatory standards, duties, ethical boundaries, and disciplinary consequences for members of a profession.\n\n"
                        "### Essential Roles of Professional Codes in Society\n\n"
                        "1. **Regulating Worker Behavior:** Establishing clear rules that prevent professionals from abusing their authority or exploiting vulnerable clients.\n"
                        "2. **Protecting Client Rights:** Guaranteeing that the public receives safe, fair, confidential, and high-quality services.\n"
                        "3. **Safeguarding Professionals from Compromise:** Providing a legal and moral shield for workers when pressured by corrupt employers or clients to commit illegal acts.\n"
                        "4. **Benchmarking Disciplinary Actions:** Giving regulatory councils clear objective standards to investigate misconduct, suspend licenses, or de-register errant practitioners.\n"
                        "5. **Inspiring Public Trust:** Fostering societal confidence and honor in critical institutions like healthcare, law enforcement, and education.\n\n"
                        "### The 6 Key Christian Virtues in the Workplace\n\n"
                        "| Christian Virtue | Practical Workplace Meaning | Biblical Anchor |\n"
                        "| :--- | :--- | :--- |\n"
                        "| **Diligence** | Energetic, thorough, and disciplined dedication to duties without cutting corners. | Proverbs 22:29; Colossians 3:23 |\n"
                        "| **Honesty & Integrity** | Absolute truthfulness in records, finances, and speech; doing right when unmonitored. | Proverbs 11:1; 2 Corinthians 8:21 |\n"
                        "| **Faithfulness** | Steadfast loyalty, keeping covenants, guarding confidentiality, and reliable stewardship. | Luke 16:10; Matthew 25:21 |\n"
                        "| **Responsibility** | Taking moral ownership of decisions, admitting mistakes, and prioritizing public safety. | Galatians 6:5; Genesis 2:15 |\n"
                        "| **Tolerance** | Patient endurance, self-control, and treating colleagues and clients of all backgrounds with dignity. | Colossians 3:12-13; Ephesians 4:2 |\n"
                        "| **Justice & Fairness** | Treating workers, subordinates, and clients impartially without bribery or favoritism. | Micah 6:8; James 5:4 |"
                    )
                }
            }
        ],

        # Page 4: Practical Application
        [
            {
                "type": "step_process",
                "title": "Framework: Developing a Student Code of Personal & Academic Integrity",
                "content": {
                    "description": "A 4-step actionable framework for Junior Secondary learners to build strong ethical habits and personal accountability before entering the workforce.",
                    "steps": [
                        {
                            "step_number": 1,
                            "title": "Commit to Absolute Academic Honesty",
                            "description": "Never participate in examination cheating, copying assignments, or plagiarizing others' work. Value genuine mastery and intellectual growth over unearned grades."
                        },
                        {
                            "step_number": 2,
                            "title": "Practice Diligent Time Stewardship",
                            "description": "Arrive at school and lessons promptly. Complete homework and practical projects on schedule without requiring threats or constant supervision."
                        },
                        {
                            "step_number": 3,
                            "title": "Uphold Mutual Respect and Tolerance",
                            "description": "Treat classmates, teachers, and school support staff (cooks, cleaners, security personnel) with kindness and dignity, respecting cultural and religious diversity."
                        },
                        {
                            "step_number": 4,
                            "title": "Demonstrate Moral Courage & Whistleblowing",
                            "description": "Refuse to yield to negative peer pressure. Confidentially report bullying, theft, examination leaks, or substance abuse to trusted school authorities."
                        }
                    ]
                }
            },
            {
                "type": "concept_explanation",
                "title": "Kenyan Real-World Context: Professional Regulatory Bodies & Resisting Corruption",
                "content": {
                    "text": (
                        "### Institutional Guardians of Professional Standards in Kenya\n\n"
                        "In Kenya, various statutory bodies enforce professional codes to ensure public safety and integrity:\n\n"
                        "- **Kenya Medical Practitioners and Dentists Council (KMPDC):** Licenses medical doctors and dentists, inspects hospitals, and revokes operating licenses from clinics that endanger patient lives or engage in unethical practices.\n"
                        "- **Teachers Service Commission (TSC):** Regulates the teaching service, enforcing the TSC Code of Conduct and Ethics to ensure teachers protect child welfare, avoid absenteeism, and maintain exemplary moral standing.\n"
                        "- **Law Society of Kenya (LSK):** Regulates advocates and magistrates, maintaining the Disciplinary Tribunal to penalize lawyers who misappropriate client funds or violate confidentiality.\n"
                        "- **Ethics and Anti-Corruption Commission (EACC):** Implements Chapter Six of the Constitution of Kenya on Leadership and Integrity, investigating bribery, conflict of interest, and embezzlement in public offices.\n\n"
                        "### The Call for Junior Secondary Learners\n"
                        "Corruption in Kenya—whether in the form of *kitu kidogo* (bribes), academic dishonesty, or nepotism—erodes national development. By developing personal integrity in Grade 9, you become part of a new generation of ethical leaders who honor God and protect our nation."
                    )
                }
            }
        ],

        # Page 5: Multimedia & Reflection
        [
            {
                "type": "suggested_video",
                "title": "BibleProject: Justice & Righteousness",
                "content": {
                    "youtube_id": "A14THPoc4-4",
                    "url": "https://www.youtube.com/watch?v=A14THPoc4-4",
                    "description": "An illuminating exploration by BibleProject examining biblical justice (mishpat) and righteousness (tsedeqah) as the moral blueprint for human society and honest work."
                }
            },
            {
                "type": "concept_explanation",
                "title": "Ethical Dilemma: Whistleblowing vs. Complicity in the Workplace",
                "content": {
                    "text": (
                        "### Scenario: The Test of Moral Courage\n\n"
                        "Imagine you are working as a laboratory assistant in a busy medical clinic. You discover that your senior supervisor is intentionally diluting diagnostic reagents to cut costs and pocketing the extra money. The faulty test results mean patients are receiving incorrect medications for serious illnesses. When you politely question him, he warns you: *\"Keep quiet if you want to keep your job and finish your internship.\"*\n\n"
                        "### Ethical & Scriptural Analysis\n\n"
                        "1. **The Trap of Complicity:** Remaining silent makes one an accomplice to deceit and endangers innocent human lives, violating God's commandment to protect the vulnerable (Proverbs 31:8-9).\n"
                        "2. **The Cost of Whistleblowing:** Reporting wrongdoing requires moral courage (*fortitude*). It may bring temporary hostility or hardship, but standing for truth honors God and protects society.\n"
                        "3. **Biblical Resolution:** A Christian professional must refuse to participate in falsehood, seek appropriate institutional whistleblowing channels (such as the clinic management board or regulatory councils like KMPDC), and trust God for protection.\n\n"
                        "*\"Have nothing to do with the fruitless deeds of darkness, but rather expose them.\"* — Ephesians 5:11"
                    )
                }
            }
        ],

        # Page 6: Mastery Check
        [
            {
                "type": "summary_card",
                "title": "Key Takeaways: Virtues, Ethics, and Professional Ethos",
                "content": {
                    "points": [
                        "Professional ethics provide the rules of conduct for a career, while professional ethos represents the collective character and distinct identity of a profession.",
                        "Professional codes of conduct protect client rights, safeguard workers from corruption, and provide objective standards for accountability.",
                        "Scripture condemns dishonest scales (Proverbs 11:1) and commands believers to practice diligence (Proverbs 22:29) and transformational generosity (Ephesians 4:28).",
                        "Key Christian virtues for the workplace include diligence, honesty, integrity, faithfulness, responsibility, and tolerance.",
                        "Written codes provide external boundaries, but internal Christian character ensures that workers do the right thing even when unmonitored."
                    ]
                }
            },
            {
                "type": "knowledge_check",
                "title": "Mastery Assessment: Professional Codes and Christian Ethics",
                "content": {
                    "question": "What is the primary purpose of a Professional Code of Ethics in modern society?",
                    "options": [
                        "A. To allow senior workers to demand salary increments without attending scheduled shifts.",
                        "B. To regulate worker conduct, protect client welfare, safeguard professionals from corruption, and maintain public trust.",
                        "C. To prevent junior employees from obtaining promotions or pursuing higher education.",
                        "D. To eliminate the need for personal character and moral values in the workplace."
                    ],
                    "correct_answer": "B",
                    "explanation": (
                        "A Professional Code of Ethics sets clear legal and moral benchmarks that regulate employee conduct, "
                        "prevent abuse of power, safeguard client rights, protect professionals against corrupt pressures, and foster "
                        "broad societal trust in institutions."
                    )
                }
            }
        ]
    ]
}

def ingest_grade9_cre_topic1_lesson3(replace=True):
    print("=" * 80)
    print("INGESTING CBC GRADE 9 CRE — TOPIC 1: WORK (LESSON 3)")
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
    ingest_grade9_cre_topic1_lesson3()
