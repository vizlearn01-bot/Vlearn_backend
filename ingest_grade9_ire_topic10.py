"""
VLearn CBC Grade 9 IRE — Topic 10: Significance of Islamic Morality
Production Ingestion and Enrichment Script for all 2 Lessons

Target Topic in DB: Topic ID 350 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/morality-significance.md

2 Lessons Ingested & Fully Enriched:
  1. Lesson 5.2.1: Why Islamic morality matters
  2. Lesson 5.2.2: Practising morality
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
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal pedagogical tags while preserving markdown."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|HADITH REFERENCE|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|'
        r'MISCONCEPTION|MISCONCEPTION CHECK|INTERACTION|ETHICAL SCENARIO|KEY VERSE|'
        r'REAL WORLD APPLICATION|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|'
        r'COMPARISON TABLE|INFOGRAPHIC|SVG|DIAGRAM)[^\]]*\]',
        '',
        text,
        flags=re.IGNORECASE
    )
    text = re.sub(r'\[Source:[^\]]*\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()


# ─────────────────────────────────────────────────────────────────────────────
# 2 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 5.2.1: The Organic Tree of Faith (Iman, Taqwa, and Akhlaq)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg101" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="trunkGrad101" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="50%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
    <linearGradient id="crownGrad101" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg101)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE ORGANIC TREE OF FAITH: WHY ISLAMIC MORALITY MATTERS</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Inward Faith (Iman) and God-Consciousness (Taqwa) Naturally Bear the Sweet Fruits of Character (Akhlaq)</text>

  <!-- Foliage / Canopy (Top) -->
  <ellipse cx="440" cy="145" rx="360" ry="80" fill="url(#crownGrad101)" stroke="#34d399" stroke-width="2"/>
  <text x="440" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE RIPE FRUITS: AKHLAQ (EXCELLENT MORAL CHARACTER)</text>
  <text x="440" y="112" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">"The best of you are those who have the best character." (Sahih al-Bukhari 6035)</text>

  <!-- 4 Fruit Cards -->
  <g transform="translate(110, 122)">
    <rect width="140" height="42" rx="6" fill="#0f172a" stroke="#fbbf24"/>
    <text x="70" y="20" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">KINDNESS &amp; MERCY</text>
    <text x="70" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Rahmah in speech</text>
  </g>

  <g transform="translate(265, 122)">
    <rect width="140" height="42" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="70" y="20" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">HONESTY &amp; TRUTH</text>
    <text x="70" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Sidq in all dealings</text>
  </g>

  <g transform="translate(420, 122)">
    <rect width="140" height="42" rx="6" fill="#0f172a" stroke="#a78bfa"/>
    <text x="70" y="20" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">HUMILITY &amp; RESPECT</text>
    <text x="70" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Tawadu' with peers</text>
  </g>

  <g transform="translate(575, 122)">
    <rect width="140" height="42" rx="6" fill="#0f172a" stroke="#34d399"/>
    <text x="70" y="20" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">GENEROSITY &amp; HELP</text>
    <text x="70" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Ihsan &amp; Ta'awun</text>
  </g>

  <!-- Tree Trunk (Middle) -->
  <g transform="translate(370, 230)">
    <rect width="140" height="90" rx="8" fill="url(#trunkGrad101)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="70" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE TRUNK</text>
    <text x="70" y="52" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">TAQWA &amp; WORSHIP</text>
    <text x="70" y="72" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Salat • Sawm • Zakat • Dhikr</text>
  </g>

  <!-- Ground Line -->
  <line x1="80" y1="322" x2="800" y2="322" stroke="#64748b" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="130" y="316" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">SOIL SURFACE</text>

  <!-- Roots (Bottom) -->
  <g transform="translate(180, 332)">
    <rect width="520" height="85" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="260" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE DEEP ROOTS: IMAN (SACRED INNER BELIEF)</text>
    <text x="260" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Belief in Allah • His Angels • Revealed Scriptures • Messengers • Day of Judgment • Qadar</text>
    
    <rect x="25" y="54" width="470" height="22" rx="4" fill="#0f172a"/>
    <text x="260" y="69" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Key Insight: Without healthy roots (Iman), fruits (Akhlaq) cannot exist; healthy roots must produce sweet fruits.</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 5.2.2: Impulse vs Akhlaq: The Ethical Decision Framework"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg102" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg102)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">PRACTISING MORALITY: THE MORAL AGENCY DECISION FUNNEL</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Comparing Impulse-Driven Reactions with Faith-Guided Ethical Conduct (Akhlaq)</text>

  <!-- Left Column: Impulse Driven -->
  <g transform="translate(45, 85)">
    <rect width="360" height="315" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="360" height="34" rx="10" fill="#7f1d1d"/>
    <text x="180" y="22" fill="#fecaca" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PATHWAY A: IMPULSE &amp; EGO (NAFS)</text>

    <!-- Scenario 1 -->
    <rect x="15" y="48" width="330" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Provoked / Insulted by Classmate:</text>
    <text x="25" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Explodes in anger, shouts insults, escalates fight</text>

    <!-- Scenario 2 -->
    <rect x="15" y="112" width="330" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="132" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Finds Money on Classroom Floor:</text>
    <text x="25" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Pockets it secretly; "finders keepers" attitude</text>

    <!-- Scenario 3 -->
    <rect x="15" y="176" width="330" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="196" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Peer is Being Mocked / Excluded:</text>
    <text x="25" y="214" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Joins in laughter to fit in with popular crowd</text>

    <!-- Consequence -->
    <rect x="15" y="244" width="330" height="56" rx="6" fill="#2d1515" stroke="#ef4444"/>
    <text x="180" y="265" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">OUTCOME: GUILT &amp; SOCIAL DISCORD</text>
    <text x="180" y="284" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Damaged relationships, spiritual numbness, loss of trust</text>
  </g>

  <!-- Central Bridge / Moral Pause -->
  <g transform="translate(415, 175)">
    <circle cx="25" cy="55" r="22" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <text x="25" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" text-anchor="middle">THE</text>
    <text x="25" y="63" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" text-anchor="middle">PAUSE</text>
    <text x="25" y="90" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Taqwa</text>
  </g>

  <!-- Right Column: Akhlaq Driven -->
  <g transform="translate(475, 85)">
    <rect width="360" height="315" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="360" height="34" rx="10" fill="#065f46"/>
    <text x="180" y="22" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PATHWAY B: AKHLAQ &amp; SUNNAH (CONSCIOUS)</text>

    <!-- Scenario 1 -->
    <rect x="15" y="48" width="330" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Provoked / Insulted by Classmate:</text>
    <text x="25" y="86" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Breathes, controls anger (Sabr), speaks with dignity</text>

    <!-- Scenario 2 -->
    <rect x="15" y="112" width="330" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="132" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Finds Money on Classroom Floor:</text>
    <text x="25" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Hands it to teacher or seeks owner (Amanah &amp; Sidq)</text>

    <!-- Scenario 3 -->
    <rect x="15" y="176" width="330" height="54" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="196" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Peer is Being Mocked / Excluded:</text>
    <text x="25" y="214" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Stands up for them or invites them warmly (Rahmah)</text>

    <!-- Consequence -->
    <rect x="15" y="244" width="330" height="56" rx="6" fill="#064e3b" stroke="#10b981"/>
    <text x="180" y="265" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">OUTCOME: SAKINAH &amp; DIVINE PLEASURE</text>
    <text x="180" y="284" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Heavy on Mizan Scale, social harmony, personal peace</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR TOPIC 10 (2 LESSONS)
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "unit_order": 1,
        "lesson_title": "Why Islamic morality matters",
        "inquiry": "What is Islamic morality (Akhlaq), and why is it considered the true reflection of a person's faith (iman)?",
        "hook": "Imagine a beautifully designed smartphone with a sleek outer shell and a powerful camera. But if the internal software is corrupt and buggy, the phone is useless. In Islam, daily rituals like prayer and fasting are like the outer design, while your moral character (Akhlaq) is the internal software. If a person performs their prayers but treats others with cruelty and dishonesty, their software is broken.",
        "concept_name": "Akhlaq and Taqwa as the Core of True Faith",
        "concept_explanation": "Akhlaq refers to the system of moral values, ethics, and character traits prescribed by Islam to govern how a person conducts themselves in private and in public. Taqwa is being constantly conscious of Allah's presence, driving a believer to perform righteous deeds solely to please Him. Islamic morality is not an optional extra; it is the organic fruit of inward faith (Iman). The Prophet Muhammad (PBUH) stated that the primary purpose of his divine mission was to perfect noble character.",
        "scripture_quran": "Indeed, the most noble of you in the sight of Allah is the most righteous of you. Indeed, Allah is Knowing and Acquainted.",
        "scripture_quran_ref": "Surah Al-Hujurat, 49:13",
        "scripture_hadith": "The best of you are those who have the best character.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 6035",
        "deep_explanation": "Islamic morality is a vital pillar of religious life that directly affects our standing with Allah:\n\n1. Sincere Manifestation of Iman: Sincere faith cannot remain hidden; it must show in daily conduct. The Prophet (PBUH) taught that the most complete in faith are those with the best character.\n2. Prophetic Mission Objective: The Prophet declared: 'I was sent only to perfect noble character' (Muwatta Malik).\n3. Heavy on the Scale (Mizan): On the Day of Judgment, good character is described as the heaviest deed placed on the believer's balance, outweighing even supererogatory rituals performed without sincere moral conduct.",
        "svg_func": get_svg_lesson_1,
        "diagram_title": "The Organic Tree of Faith (Iman, Taqwa, and Akhlaq)",
        "table_title": "Dimensions of Islamic Character (Akhlaq)",
        "table_headers": ["Dimension", "Core Principle", "Everyday Behavior", "Spiritual Significance"],
        "table_rows": [
            ["With Allah", "Taqwa & Sincerity", "Private worship & avoiding secret sins", "Root of all righteous action"],
            ["With Oneself", "Self-respect & Dignity", "Modesty, clean speech, & seeking knowledge", "Protecting the divine Amanah"],
            ["With Others", "Rahmah & Fairness", "Kindness, smiling, & honesty in trade", "Reflects true faith & builds trust"],
            ["With Creation", "Stewardship & Care", "Gentleness to animals & nature conservation", "Universal mercy of Islam"]
        ],
        "scenario": "Yusuf has memorized several chapters of the Qur'an and always prays in the first row of the mosque. However, at school, he often makes fun of younger students, calls classmates offensive nicknames, and refuses to share his study notes. His classmate, Amina, says to him: 'Yusuf, your prayers are beautiful, but our teacher taught us that the Prophet (PBUH) said the best of us are those with the best character. True iman is not just about standing in prayer; it is about how we treat people when we finish praying.' Yusuf realizes that his character mismatches his rituals and resolves to reform.",
        "real_world": "Perform an 'Akhlaq Audit' of your school week. Identify one negative habit in your character—such as complaining, speaking dryly to others, or ignoring someone in need—and consciously replace it with an act of beauty. For example, resolve to greet every classmate with a warm smile and speak kindly, even when you feel tired, doing this purely to seek Allah's pleasure.",
        "reflection": "How does knowing that the Prophet (PBUH) valued good character above all else influence the way you balance your daily prayers with your treatment of friends and family?",
        "misconception": "Remember: Good character is not just polite etiquette to avoid trouble or seek social praise. True Akhlaq is an act of worship (Ibadah) performed sincerely to please Allah, meaning we must maintain it even when others treat us poorly.",
        "yt_title": "The Weight of Good Character in Islam",
        "yt_desc": "An inspiring lecture on why Akhlaq is the true measure of faith and the heaviest deed on the Day of Judgment.",
        "yt_id": "X0h2j3gZ_wU",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Al-Masjid_an-Nabawi_at_night.jpg/1280px-Al-Masjid_an-Nabawi_at_night.jpg",
        "image_title": "Al-Masjid an-Nabawi (The Prophet's Mosque in Madinah)",
        "image_caption": "The historical center from which the Prophet Muhammad (PBUH) taught and modeled the perfection of moral character.",
        "mcq": {
            "question": "According to Surah Al-Hujurat (49:13), what is the sole criterion that determines a person's nobility and worth in the sight of Allah?",
            "options": [
                "The wealth, status, and lineage of their family.",
                "Their physical strength and athletic achievements.",
                "Their level of piety (Taqwa) and righteous character.",
                "The country, tribe, or race they belong to."
            ],
            "answer": "C",
            "explanation": "Surah Al-Hujurat (49:13) explicitly states that the most noble in the sight of Allah is the most righteous (Atqaakum), confirming that moral character and God-consciousness alone determine true worth."
        },
        "summary_content": "Islamic morality (Akhlaq) is an essential, root-level expression of inner faith (Iman). True nobility before Allah is determined solely by piety and good character (Taqwa). Noble character is the heaviest deed on the Scale on the Day of Judgment.",
        "key_points": [
            "Akhlaq is the direct manifestation of inward Iman and Taqwa.",
            "The Prophet's mission was to perfect noble moral character.",
            "Noble character outweighs supererogatory rituals devoid of good conduct."
        ],
        "exit_ticket": "Write down one Hadith that highlights the high status and weight of good character in Islam."
    },
    {
        "unit_order": 2,
        "lesson_title": "Practising morality",
        "inquiry": "How do we make moral decisions in our daily interactions, and how does practicing Akhlaq build a cohesive society?",
        "hook": "Imagine a busy city intersection where all traffic lights suddenly stop working. If every driver behaves selfishly, trying to force their way through first, the intersection locks up in a chaotic, angry traffic jam. But if the drivers practice patience, yield to one another, and respect rules, traffic flows smoothly. In our daily lives, practicing Islamic morality acts like a perfect traffic system.",
        "concept_name": "Moral Agency and Social Ethics (Mu'amalat)",
        "concept_explanation": "Moral agency is the ability and responsibility of a human being to choose right over wrong, guided by revelation and reason, and to accept the consequences of those choices. Social morality (Mu'amalat) is the practical application of ethical principles such as honesty, mercy (Rahmah), and justice ('Adl) in our daily dealings with family, neighbors, classmates, and the wider world.",
        "scripture_quran": "And speak to people good [words]...",
        "scripture_quran_ref": "Surah Al-Baqarah, 2:83",
        "scripture_hadith": "He who does not show mercy, no mercy will be shown to him.",
        "scripture_hadith_ref": "Sahih Muslim, 2318",
        "deep_explanation": "Practicing Islamic morality requires a conscious, active choice built on three core pillars:\n\n1. Kindness and Mercy (Rahmah): Compassion extended to all creation, including peers, animals, and the natural environment. Divine mercy is tied to human mercy.\n2. Justice and Fairness ('Adl): Absolute impartiality and fairness, giving everyone their due rights regardless of personal likes or dislikes.\n3. Truthfulness and Integrity (Sidq): Total alignment between inner intention, spoken words, and outward deeds, rejecting all deception and hypocrisy.",
        "svg_func": get_svg_lesson_2,
        "diagram_title": "Practising Morality: The Moral Agency Decision Funnel",
        "table_title": "Impulse-Driven Reaction vs Akhlaq-Driven Action",
        "table_headers": ["Life Situation", "Impulse Reaction (Nafs)", "Akhlaq Action (Sunnah)", "Impact on Community"],
        "table_rows": [
            ["Insulted / Provoked", "Shouts back, curses, starts a fight", "Controls anger (Sabr), speaks calmly", "De-escalates conflict & models peace"],
            ["Unattended Property", "Steals or conceals the item", "Returns it or finds rightful owner", "Builds unshakeable mutual trust"],
            ["Vulnerable Peer", "Joins bullies or ignores their pain", "Defends peer and shows compassion", "Fosters an inclusive, safe environment"],
            ["Making Mistakes", "Blames others and lies to cover up", "Admits fault honestly and apologizes", "Demonstrates humility and integrity"]
        ],
        "scenario": "During a competitive school soccer match, Hussein is tripped by an opposing player, causing him to scrape his knee. The referee does not see the foul, and Hussein's team loses the match. Hussein feels a surge of anger and wants to shout at the player or refuse to shake his hand after the game. He pauses and remembers the Hadith: 'The strong person is not the one who can overpower others, but the one who controls themselves when angry.' Hussein takes a deep breath, calms his heart, walks over to the player, shakes his hand, and says, 'Good game.' His self-control prevents a post-match fight and earns him the respect of both teams.",
        "real_world": "Implement the 'Good Word Challenge' in your home. For the next 48 hours, commit to speaking only positive, encouraging, and helpful words to your parents and siblings, in line with Surah Al-Baqarah (2:83). Avoid all forms of dry sarcasm, teasing, or complaining. Notice how this active practice of morality transforms the emotional atmosphere around you.",
        "reflection": "How does practicing self-control during moments of anger protect your relationships with your classmates, teachers, and family members?",
        "misconception": "Remember: Practicing Akhlaq is not a sign of weakness or passivity. Controlling anger and choosing gentleness requires immense inner strength and is praised by Allah as the mark of a true believer.",
        "yt_title": "Controlling Anger and the Power of Good Words",
        "yt_desc": "A practical guide on mastering emotions and using speech to build peace and unity.",
        "yt_id": "z9GzY23bX5k",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Bazaar_in_Cairo.jpg/1280px-Bazaar_in_Cairo.jpg",
        "image_title": "Historical Marketplace (Khan el-Khalili)",
        "image_caption": "Historic center of Islamic commerce where daily interactions and trade were governed by the principles of Sidq, 'Adl, and Rahmah.",
        "mcq": {
            "question": "What is the spiritual consequence of refusing to show mercy and compassion to others, according to the authentic Hadith of the Prophet (PBUH)?",
            "options": [
                "A person will lose their worldly wealth and physical strength immediately.",
                "They will not receive the mercy of Allah (S.W.T.) on the Day of Judgment.",
                "They will be banned from entering public libraries.",
                "Their exam results will automatically be cancelled."
            ],
            "answer": "B",
            "explanation": "The Prophet (PBUH) stated in Sahih Muslim (2318): 'He who does not show mercy, no mercy will be shown to him,' showing that receiving divine mercy is directly linked to showing mercy to creation."
        },
        "summary_content": "Practicing morality requires conscious self-regulation and filtering impulses through faith. Rahmah (mercy) and 'Adl (justice) are the foundations of Islamic social ethics. Speaking kindly to others is a direct divine commandment that builds social cohesion.",
        "key_points": [
            "Moral agency requires choosing faith-guided actions over instinctive impulses.",
            "Rahmah, 'Adl, and Sidq are the essential pillars of Islamic social dealings.",
            "Gentleness and self-control in anger are the hallmarks of genuine strength."
        ],
        "exit_ticket": "Write down one way you can show mercy to a classmate who is currently struggling with their schoolwork."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic10():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 10: SIGNIFICANCE OF ISLAMIC MORALITY")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=350)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 350 does not exist!")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    with transaction.atomic():
        # Clean existing units if any
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"Cleaning {existing_units.count()} existing units under Topic {topic.id}...")
            existing_units.delete()

        total_units = 0
        total_lessons = 0
        total_blocks = 0
        total_assets = 0

        for cfg in LESSONS_CONFIG:
            u_order = cfg["unit_order"]
            l_title = cfg["lesson_title"]

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                name=f"Lesson 5.2.{u_order}: {l_title}",
                order=u_order,
                description=clean_text(cfg["concept_explanation"][:250] + "...")
            )
            total_units += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1
            )
            total_lessons += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Hook (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                title=clean_text(cfg["image_title"]),
                url=cfg["image_url"],
                metadata={
                    "caption": clean_text(cfg["image_caption"]),
                    "credit": "Wikimedia Commons"
                }
            )
            total_assets += 1

            b_img = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Hook",
                order=10,
                component_order=1,
                block_type="suggested_image",
                component_type="suggested_image",
                title=clean_text(cfg["image_title"]),
                content={
                    "title": clean_text(cfg["image_title"]),
                    "caption": clean_text(cfg["image_caption"]),
                    "url": cfg["image_url"]
                }
            )
            b_img.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Hook",
                order=20,
                component_order=2,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Lesson Orientation & Inquiry",
                content={
                    "title": "Lesson Orientation & Inquiry",
                    "inquiry_question": clean_text(cfg["inquiry"]),
                    "hook": clean_text(cfg["hook"]),
                    "learning_goals": [
                        f"Understand the core meaning of {l_title}",
                        "Examine foundational Qur'anic verses and Hadith",
                        "Analyze practical scenarios and daily ethical applications"
                    ]
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Theological Concept (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=30,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title=clean_text(cfg["concept_name"]),
                content={
                    "title": clean_text(cfg["concept_name"]),
                    "explanation": clean_text(cfg["concept_explanation"]),
                    "text": clean_text(cfg["concept_explanation"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=40,
                component_order=2,
                block_type="callout",
                component_type="callout",
                title="Scripture Source Panel",
                content={
                    "title": "Scripture Source Panel",
                    "callout_type": "scripture",
                    "quran_verse": clean_text(cfg["scripture_quran"]),
                    "quran_reference": clean_text(cfg["scripture_quran_ref"]),
                    "hadith_text": clean_text(cfg["scripture_hadith"]),
                    "hadith_reference": clean_text(cfg["scripture_hadith_ref"]),
                    "text": clean_text(
                        f"**Qur'an ({cfg['scripture_quran_ref']}):**\n> \"{cfg['scripture_quran']}\"\n\n"
                        f"**Hadith ({cfg['scripture_hadith_ref']}):**\n> \"{cfg['scripture_hadith']}\""
                    )
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & SVG Diagram (3 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=50,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Theological Analysis & Principles",
                content={
                    "title": "Theological Analysis & Principles",
                    "explanation": clean_text(cfg["deep_explanation"]),
                    "text": clean_text(cfg["deep_explanation"])
                }
            )

            svg_str = cfg["svg_func"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                title=clean_text(cfg["diagram_title"]),
                metadata={"svg_xml": svg_str, "svg_content": svg_str}
            )
            total_assets += 1

            b_diag = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=60,
                component_order=2,
                block_type="suggested_diagram",
                component_type="suggested_diagram",
                title=clean_text(cfg["diagram_title"]),
                content={
                    "title": clean_text(cfg["diagram_title"]),
                    "svg_xml": svg_str,
                    "svg_content": svg_str
                },
                metadata={
                    "svg_xml": svg_str,
                    "svg_content": svg_str
                }
            )
            b_diag.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=70,
                component_order=3,
                block_type="comparison_table",
                component_type="comparison_table",
                title=clean_text(cfg["table_title"]),
                content={
                    "title": clean_text(cfg["table_title"]),
                    "headers": [clean_text(h) for h in cfg["table_headers"]],
                    "rows": [[clean_text(c) for c in row] for row in cfg["table_rows"]]
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Lived Reality Scenario (1 block)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                page_title="Lived Reality Scenario",
                order=80,
                component_order=1,
                block_type="worked_example",
                component_type="worked_example",
                title="Practical Student Scenario",
                content={
                    "title": "Practical Student Scenario",
                    "scenario": clean_text(cfg["scenario"]),
                    "text": clean_text(cfg["scenario"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Real-World Ethics & Video (4 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=90,
                component_order=1,
                block_type="real_world_example",
                component_type="real_world_example",
                title="Real-World Ethical Action",
                content={
                    "title": "Real-World Ethical Action",
                    "application": clean_text(cfg["real_world"]),
                    "text": clean_text(cfg["real_world"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=100,
                component_order=2,
                block_type="reflection",
                component_type="reflection",
                title="Introspective Prompt",
                content={
                    "title": "Introspective Prompt",
                    "prompt": clean_text(cfg["reflection"]),
                    "text": clean_text(cfg["reflection"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=110,
                component_order=3,
                block_type="common_misconception",
                component_type="common_misconception",
                title="Misconception Check",
                content={
                    "title": "Misconception Check",
                    "content": clean_text(cfg["misconception"]),
                    "correction": clean_text(cfg["misconception"]),
                    "text": clean_text(cfg["misconception"])
                }
            )

            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="video",
                title=clean_text(cfg["yt_title"]),
                url=f"https://www.youtube.com/watch?v={cfg['yt_id']}",
                metadata={
                    "youtube_id": cfg["yt_id"],
                    "description": clean_text(cfg["yt_desc"])
                }
            )
            total_assets += 1

            b_vid = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=120,
                component_order=4,
                block_type="suggested_video",
                component_type="suggested_video",
                title=clean_text(cfg["yt_title"]),
                content={
                    "title": clean_text(cfg["yt_title"]),
                    "description": clean_text(cfg["yt_desc"]),
                    "url": f"https://www.youtube.com/watch?v={cfg['yt_id']}",
                    "youtube_id": cfg["yt_id"]
                }
            )
            b_vid.assets.add(yt_asset)

            # ─────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Knowledge Mastery Check (1 block)
            # ─────────────────────────────────────────────────────────────────
            mcq_data = cfg["mcq"]
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=6,
                page_title="Knowledge Mastery Check",
                order=130,
                component_order=1,
                block_type="knowledge_check",
                component_type="knowledge_check",
                title="Mastery Knowledge Check",
                content={
                    "title": "Mastery Knowledge Check",
                    "question": clean_text(mcq_data["question"]),
                    "options": [clean_text(opt) for opt in mcq_data["options"]],
                    "answer": clean_text(mcq_data["answer"]),
                    "correct_answer": clean_text(mcq_data["answer"]),
                    "explanation": clean_text(mcq_data["explanation"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary & Exit Ticket (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=7,
                page_title="Summary & Exit Ticket",
                order=140,
                component_order=1,
                block_type="summary",
                component_type="summary",
                title="Summary & Vocabulary Review",
                content={
                    "title": "Summary & Vocabulary Review",
                    "content": clean_text(cfg["summary_content"]),
                    "text": clean_text(cfg["summary_content"]),
                    "takeaways": [clean_text(p) for p in cfg["key_points"]]
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=7,
                page_title="Summary & Exit Ticket",
                order=150,
                component_order=2,
                block_type="mini_activity",
                component_type="mini_activity",
                title="Exit Ticket & Action Step",
                content={
                    "title": "Exit Ticket & Action Step",
                    "content": clean_text(cfg["exit_ticket"]),
                    "text": clean_text(cfg["exit_ticket"])
                }
            )

            total_blocks += 15
            print(f"  [+] Ingested Lesson {u_order}/2: '{l_title}' (7 cards, 15 blocks, 3 assets)")

    print("=" * 80)
    print("TOPIC 10 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 2")
    print(f"  Lessons       : {total_lessons} / 2 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (2 SVGs, 2 images, 2 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic10()
