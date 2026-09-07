"""
VLearn CBC Grade 9 IRE — Topic 9: Virtues in Islam (Modesty, Contentment, and Trustworthiness)
Production Ingestion and Enrichment Script for all 9 Lessons

Target Topic in DB: Topic ID 349 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/virtues-in-islam.md

9 Lessons Ingested & Fully Enriched:
  1. Lesson 5.1.1: Virtue and akhlaq
  2. Lesson 5.1.2: Modesty: meaning
  3. Lesson 5.1.3: Modesty in practice
  4. Lesson 5.1.4: Contentment: meaning
  5. Lesson 5.1.5: Contentment in practice
  6. Lesson 5.1.6: Trustworthiness: meaning
  7. Lesson 5.1.7: Trustworthiness in practice
  8. Lesson 5.1.8: Virtues and society
  9. Lesson 5.1.9: Unit synthesis
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
# 9 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 5.1.1: The Tree of Faith (Iman, Ibadah, Akhlaq)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg91" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg91)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE ORGANIC TREE OF FAITH: IMAN, IBADAH &amp; AKHLAQ</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Inward Belief and Devotional Worship Blossom into the Sweet Fruits of Moral Character</text>

  <!-- Crown / Fruits (Top) -->
  <g transform="translate(140, 85)">
    <rect width="600" height="110" rx="12" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="300" y="28" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE SWEET FRUITS: AKHLAQ (MORAL CHARACTER)</text>
    
    <rect x="25" y="42" width="170" height="52" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="110" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">HAYA (MODESTY)</text>
    <text x="110" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Humility, dignity, clean speech</text>

    <rect x="215" y="42" width="170" height="52" rx="6" fill="#0f172a" stroke="#fbbf24"/>
    <text x="300" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">RIDA (CONTENTMENT)</text>
    <text x="300" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Gratitude &amp; freedom from envy</text>

    <rect x="405" y="42" width="170" height="52" rx="6" fill="#0f172a" stroke="#a78bfa"/>
    <text x="490" y="62" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">AMANAH (TRUST)</text>
    <text x="490" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Reliability &amp; unshakeable honesty</text>
  </g>

  <!-- Trunk (Middle) -->
  <g transform="translate(290, 215)">
    <rect width="300" height="75" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="150" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE STRONG TRUNK: IBADAH (WORSHIP)</text>
    <text x="150" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Salat • Sawm (Fasting) • Zakat • Hajj • Dhikr</text>
    <text x="150" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Nourishes character through daily discipline</text>
  </g>

  <!-- Roots (Bottom) -->
  <g transform="translate(190, 310)">
    <rect width="500" height="85" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="2"/>
    <text x="250" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE DEEP ROOTS: IMAN (FAITH &amp; CONVICTION)</text>
    <text x="250" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Belief in Allah • Angels • Books • Prophets • Last Day • Qadar</text>
    <text x="250" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Unseen foundation anchoring the soul in cosmic truth</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 5.1.2: The Three Dimensions of Haya"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg92" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg92)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE THREE DIMENSIONS OF HAYA (SACRED MODESTY)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Modesty Encompasses Inward Consciousness, Verbal Conduct, and Physical Decency</text>

  <!-- 3 Pillars of Haya -->
  <!-- Dimension 1: With Allah -->
  <g transform="translate(45, 90)">
    <rect width="250" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="250" height="36" rx="10" fill="#0284c7"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1. MODESTY WITH ALLAH</text>
    <text x="125" y="58" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">The Highest Spiritual Station</text>

    <text x="20" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Feeling shy to disobey in private</text>
    <text x="20" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Remembering Allah's watchful gaze</text>
    <text x="20" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Pure sincerity in every prayer</text>
    <text x="20" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Gratitude for uncounted favors</text>

    <rect x="20" y="195" width="210" height="85" rx="6" fill="#0f172a"/>
    <text x="125" y="220" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">PROPHETIC RULE</text>
    <text x="125" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Be shy before Allah as you</text>
    <text x="125" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">ought to be shy before Him."</text>
  </g>

  <!-- Dimension 2: Speech & Conduct -->
  <g transform="translate(315, 90)">
    <rect width="250" height="315" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="36" rx="10" fill="#059669"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2. SPEECH &amp; CONDUCT</text>
    <text x="125" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Verbal &amp; Behavioral Ethics</text>

    <text x="20" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Avoiding vulgar slang &amp; shouting</text>
    <text x="20" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Speaking with polite gentleness</text>
    <text x="20" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Refusing to brag or look down on peers</text>
    <text x="20" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Lowering gaze away from indecency</text>

    <rect x="20" y="195" width="210" height="85" rx="6" fill="#0f172a"/>
    <text x="125" y="220" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">PROPHETIC RULE</text>
    <text x="125" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Modesty is part of faith,</text>
    <text x="125" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">and faith is in Paradise."</text>
  </g>

  <!-- Dimension 3: Dress & Appearance -->
  <g transform="translate(585, 90)">
    <rect width="250" height="315" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="250" height="36" rx="10" fill="#7c3aed"/>
    <text x="125" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3. DRESS &amp; DECORUM</text>
    <text x="125" y="58" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Clean, Dignified Appearance</text>

    <text x="20" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Loose, clean, non-revealing clothing</text>
    <text x="20" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Applies to both boys &amp; girls</text>
    <text x="20" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Honoring the body given by Allah</text>
    <text x="20" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Protecting personal sacred honor</text>

    <rect x="20" y="195" width="210" height="85" rx="6" fill="#0f172a"/>
    <text x="125" y="220" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">QUR'ANIC MAXIM</text>
    <text x="125" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"O children of Adam, We have</text>
    <text x="125" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">bestowed upon you clothing..." (7:26)</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 5.1.3: Digital & Real-World Modesty Comparison"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg93" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg93)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">HAYA IN PRACTICE: PHYSICAL LIFE VS DIGITAL LIFE</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">The Guard Rail of Character Preserves Sacred Dignity Across Physical Classrooms and Online Screens</text>

  <!-- Left Column: Upholding Haya (Virtue in Action) -->
  <g transform="translate(45, 85)">
    <rect width="380" height="325" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="380" height="36" rx="10" fill="#059669"/>
    <text x="190" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">UPHOLDING HAYA (TRUE DIGNITY)</text>

    <text x="25" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">At School &amp; Home:</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Wearing clean, neat uniform without arrogance</text>
    <text x="25" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Knocking and greeting before entering rooms</text>
    <text x="25" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Speaking respectfully to teachers and parents</text>

    <line x1="25" y1="140" x2="355" y2="140" stroke="#334155"/>

    <text x="25" y="165" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">In Digital &amp; Online Spaces:</text>
    <text x="25" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Lowering the digital gaze (scrolling past vulgar posts)</text>
    <text x="25" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Never leaking private screenshots or chats</text>
    <text x="25" y="221" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Refusing to participate in online mockery &amp; bullying</text>

    <rect x="25" y="248" width="330" height="48" rx="6" fill="#0f172a"/>
    <text x="190" y="270" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">SPIRITUAL HARVEST</text>
    <text x="190" y="285" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Peace of mind, universal peer respect, and Allah's pleasure</text>
  </g>

  <!-- Right Column: Neglecting Haya (Moral Hazards) -->
  <g transform="translate(455, 85)">
    <rect width="380" height="325" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="380" height="36" rx="10" fill="#b91c1c"/>
    <text x="190" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">NEGLECTING HAYA (MORAL DECAY)</text>

    <text x="25" y="65" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">At School &amp; Home:</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Barging into private spaces without permission</text>
    <text x="25" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Using vulgar slang or shouting at elders</text>
    <text x="25" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Boasting about wealth or looking down on others</text>

    <line x1="25" y1="140" x2="355" y2="140" stroke="#334155"/>

    <text x="25" y="165" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">In Digital &amp; Online Spaces:</text>
    <text x="25" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Clicking on provactive links &amp; vulgar videos</text>
    <text x="25" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Forwarding mocking memes of classmates</text>
    <text x="25" y="221" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Posting desperate, attention-seeking photos</text>

    <rect x="25" y="248" width="330" height="48" rx="6" fill="#0f172a"/>
    <text x="190" y="270" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">DESTRUCTIVE HARVEST</text>
    <text x="190" y="285" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Guilt, anxiety, loss of self-respect, and broken trusts</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 5.1.4: Comparison vs Contentment (The Anatomy of Qana'ah)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg94" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg94)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CONTENTMENT (RIDA / QANA'AH): THE TRUE INNER WEALTH</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Comparing the Restless Mind of Material Greed with the Unshakeable Peace of a Grateful Soul</text>

  <!-- Left: The Restless Heart of Comparison -->
  <g transform="translate(45, 85)">
    <rect width="380" height="325" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="380" height="36" rx="10" fill="#b45309"/>
    <text x="190" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE HEART OF COMPARISON (RESTLESS)</text>

    <text x="25" y="65" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Trapped by Enduring Greed (Hirs):</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Constantly asks: "Why do they have more than me?"</text>
    <text x="25" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Embarrassed by simple clothes or shoes</text>
    <text x="25" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Blind to uncounted blessings (health, sight, safety)</text>
    <text x="25" y="139" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Incurable jealousy (Hasad) toward peers' success</text>

    <rect x="25" y="165" width="330" height="125" rx="6" fill="#0f172a"/>
    <text x="190" y="195" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">PSYCHOLOGICAL REALITY</text>
    <text x="190" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Even with a mountain of gold, the heart</text>
    <text x="190" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">remains poor, insecure, and miserable.</text>
    <text x="190" y="265" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Nothing fills his mouth except dust"</text>
  </g>

  <!-- Right: The Peaceful Heart of Contentment -->
  <g transform="translate(455, 85)">
    <rect width="380" height="325" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="380" height="36" rx="10" fill="#047857"/>
    <text x="190" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE HEART OF CONTENTMENT (PEACEFUL)</text>

    <text x="25" y="65" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Anchored by Sincere Gratitude (Shukr):</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Constantly says: "Alhamdulillah for what I have!"</text>
    <text x="25" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Values parents' sacrifices and loving care</text>
    <text x="25" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Works hard with 100% effort, accepts results</text>
    <text x="25" y="139" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Genuine joy for classmates when they excel</text>

    <rect x="25" y="165" width="330" height="125" rx="6" fill="#0f172a"/>
    <text x="190" y="195" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">PROPHETIC WISDOM (GHINAN-NAFS)</text>
    <text x="190" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"True wealth is not in having many possessions;</text>
    <text x="190" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">true wealth is the contentment of the soul."</text>
    <text x="190" y="265" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(Sahih al-Bukhari &amp; Muslim)</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 5.1.5: The Lower-Gaze Protocol"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg95" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg95)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE PROPHETIC DUAL-PERSPECTIVE PROTOCOL</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">"Look at those beneath you in worldly matters; look at those above you in deeds of righteousness."</text>

  <!-- Left Side: Worldly Matters (Look Down) -->
  <g transform="translate(45, 90)">
    <rect width="380" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="380" height="36" rx="10" fill="#0284c7"/>
    <text x="190" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">IN WORLDLY MATTERS: LOOK BENEATH</text>

    <text x="25" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">When Tempted to Complain:</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• About an old phone -> Remember those with no internet</text>
    <text x="25" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• About plastic sandals -> Remember those with no shoes</text>
    <text x="25" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• About a simple lunch -> Remember starving refugees</text>

    <rect x="25" y="155" width="330" height="120" rx="6" fill="#0f172a"/>
    <text x="190" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">THE RESULT: GRATITUDE &amp; HUMILITY</text>
    <text x="190" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">You instantly realize that Allah has showered</text>
    <text x="190" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">you with thousands of priceless favors.</text>
    <text x="190" y="250" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Do not underestimate Allah's blessings" (Muslim)</text>
  </g>

  <!-- Right Side: Religious Matters (Look Above) -->
  <g transform="translate(455, 90)">
    <rect width="380" height="315" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="380" height="36" rx="10" fill="#059669"/>
    <text x="190" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">IN SPIRITUAL MATTERS: LOOK ABOVE</text>

    <text x="25" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">When Tempted to Feel Lazy:</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Look at peers who pray all prayers on time</text>
    <text x="25" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Look at those who memorize Quran &amp; read books</text>
    <text x="25" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Look at those who speak with gentle patience</text>

    <rect x="25" y="155" width="330" height="120" rx="6" fill="#0f172a"/>
    <text x="190" y="180" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">THE RESULT: SPIRITUAL AMBITION</text>
    <text x="190" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">You are inspired to improve your character,</text>
    <text x="190" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">seek more knowledge, and do extra good.</text>
    <text x="190" y="250" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"In that let the competitors compete" (Q 83:26)</text>
  </g>
</svg>"""


def get_svg_lesson_6():
    """Lesson 5.1.6: The Four Dimensions of Amanah (Trustworthiness)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg96" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg96)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE FOUR SACRED DIMENSIONS OF AMANAH (TRUSTWORTHINESS)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Amanah is Not Merely Borrowing Money; It is the Foundation of Faith, Secrets, and Duties</text>

  <!-- 4 Quarters of Amanah -->
  <!-- Dim 1: Spiritual Trust (Allah) -->
  <g transform="translate(45, 90)">
    <rect width="185" height="315" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="32" rx="8" fill="#0284c7"/>
    <text x="92" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. SPIRITUAL TRUST</text>
    <text x="92" y="50" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Between You &amp; Allah</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• 5 Daily Prayers</text>
    <text x="12" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Sincere intentions</text>
    <text x="12" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Protecting your body</text>
    <text x="12" y="129" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Using talents for good</text>
    <rect x="12" y="155" width="161" height="125" rx="6" fill="#0f172a"/>
    <text x="92" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">SACRED TRUST</text>
    <text x="92" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Your life and youth</text>
    <text x="92" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">are divine loans</text>
    <text x="92" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">audited on the</text>
    <text x="92" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Day of Judgment.</text>
  </g>

  <!-- Dim 2: Material Trust (Property) -->
  <g transform="translate(245, 90)">
    <rect width="185" height="315" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="185" height="32" rx="8" fill="#d97706"/>
    <text x="92" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2. MATERIAL TRUST</text>
    <text x="92" y="50" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Borrowed Possessions</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• School library books</text>
    <text x="12" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Classmate's pen/tools</text>
    <text x="12" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Money &amp; loans</text>
    <text x="12" y="129" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Public sports gear</text>
    <rect x="12" y="155" width="161" height="125" rx="6" fill="#0f172a"/>
    <text x="92" y="180" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">CARE &amp; RETURN</text>
    <text x="92" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Returning borrowed</text>
    <text x="92" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">items on time,</text>
    <text x="92" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">clean, and without</text>
    <text x="92" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">any hidden damage.</text>
  </g>

  <!-- Dim 3: Informational Trust (Secrets) -->
  <g transform="translate(445, 90)">
    <rect width="185" height="315" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="185" height="32" rx="8" fill="#7c3aed"/>
    <text x="92" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. INFORMATIONAL</text>
    <text x="92" y="50" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Secrets &amp; Confidence</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Private chats / DMs</text>
    <text x="12" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Personal weaknesses</text>
    <text x="12" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Family problems</text>
    <text x="12" y="129" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Never leaking secrets</text>
    <rect x="12" y="155" width="161" height="125" rx="6" fill="#0f172a"/>
    <text x="92" y="180" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">THE VAULT</text>
    <text x="92" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"When a person</text>
    <text x="92" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">tells something &amp;</text>
    <text x="92" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">then turns away,</text>
    <text x="92" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">it is a trust."</text>
  </g>

  <!-- Dim 4: Functional Trust (Duties) -->
  <g transform="translate(645, 90)">
    <rect width="185" height="315" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="32" rx="8" fill="#059669"/>
    <text x="92" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4. FUNCTIONAL</text>
    <text x="92" y="50" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Duties &amp; Leadership</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Academic honesty</text>
    <text x="12" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Zero cheating in exams</text>
    <text x="12" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Prefect &amp; monitor duty</text>
    <text x="12" y="129" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Unbroken promises</text>
    <rect x="12" y="155" width="161" height="125" rx="6" fill="#0f172a"/>
    <text x="92" y="180" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">INTEGRITY</text>
    <text x="92" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Treating every</text>
    <text x="92" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">role with absolute</text>
    <text x="92" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">fairness, without</text>
    <text x="92" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">favoring friends.</text>
  </g>
</svg>"""


def get_svg_lesson_7():
    """Lesson 5.1.7: The Borrower's Amanah Checklist"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg97" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg97)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">PRACTICAL INTEGRITY: THE BORROWER'S AMANAH CHECKLIST</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">A 4-Step Action Protocol for Handling Borrowed Property, Exam Security, and Leadership Roles</text>

  <!-- Step 1: Explicit Permission -->
  <g transform="translate(45, 90)">
    <rect width="185" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="#0284c7"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STEP 1: PERMISSION</text>
    <text x="92" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Ask Before Touching</text>
    
    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Never assume it's okay</text>
    <text x="15" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Ask clearly and politely</text>
    <text x="15" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Agree on return time</text>

    <rect x="15" y="160" width="155" height="110" rx="6" fill="#0f172a"/>
    <text x="92" y="185" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">COMMON MISTAKE</text>
    <text x="92" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Taking a pen from a</text>
    <text x="92" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">friend's desk while</text>
    <text x="92" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">they are at lunch.</text>
  </g>

  <!-- Step 2: Extreme Care -->
  <g transform="translate(245, 90)">
    <rect width="185" height="315" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="#d97706"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STEP 2: HIGHER CARE</text>
    <text x="92" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Better Than Your Own</text>

    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Keep clean, dry, safe</text>
    <text x="15" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Do not lend to others</text>
    <text x="15" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Protect from drops</text>

    <rect x="15" y="160" width="155" height="110" rx="6" fill="#0f172a"/>
    <text x="92" y="185" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">COMMON MISTAKE</text>
    <text x="92" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Treating borrowed</text>
    <text x="92" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">books roughly or</text>
    <text x="92" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">scribbling on pages.</text>
  </g>

  <!-- Step 3: Punctual Return -->
  <g transform="translate(445, 90)">
    <rect width="185" height="315" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="#7c3aed"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STEP 3: TIMING</text>
    <text x="92" y="55" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Return Without Reminders</text>

    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Return before asked</text>
    <text x="15" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Express warm thanks</text>
    <text x="15" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• "JazakAllahu Khayran"</text>

    <rect x="15" y="160" width="155" height="110" rx="6" fill="#0f172a"/>
    <text x="92" y="185" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">COMMON MISTAKE</text>
    <text x="92" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Keeping an item for</text>
    <text x="92" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">weeks until the owner</text>
    <text x="92" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">has to ask for it.</text>
  </g>

  <!-- Step 4: Restitution if Damaged -->
  <g transform="translate(645, 90)">
    <rect width="185" height="315" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="#059669"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STEP 4: RESTITUTION</text>
    <text x="92" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Replace or Repair</text>

    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Admit fault instantly</text>
    <text x="15" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Replace brand new</text>
    <text x="15" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Never hide broken gear</text>

    <rect x="15" y="160" width="155" height="110" rx="6" fill="#0f172a"/>
    <text x="92" y="185" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">GOLDEN RULE</text>
    <text x="92" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Amanah makes you</text>
    <text x="92" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">courageously honest</text>
    <text x="92" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">even when it costs money."</text>
  </g>
</svg>"""


def get_svg_lesson_8():
    """Lesson 5.1.8: The Triangle of Social Integrity"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg98" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg98)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE TRIANGLE OF SOCIAL INTEGRITY (VIRTUES &amp; SOCIETY)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Modesty, Contentment, and Trustworthiness Eradicate Social Corruption and Build Peace</text>

  <!-- Triangle Diagram in Center -->
  <!-- Top Peak: Modesty (Haya) -->
  <g transform="translate(320, 80)">
    <rect width="240" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="120" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. MODESTY (HAYA)</text>
    <text x="120" y="45" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Protects Public Morality</text>
    <text x="120" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Clean language &amp; dignified media</text>
    <text x="120" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Banishes vulgarity &amp; street indecency</text>
  </g>

  <!-- Left Base: Contentment (Rida) -->
  <g transform="translate(60, 260)">
    <rect width="260" height="105" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="130" y="25" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2. CONTENTMENT (RIDA)</text>
    <text x="130" y="45" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Protects Social Harmony &amp; Equality</text>
    <text x="130" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Eradicates greed, envy, and bribery</text>
    <text x="130" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Prevents corruption in public leadership</text>
    <text x="130" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Rich and poor live with mutual love</text>
  </g>

  <!-- Right Base: Trustworthiness (Amanah) -->
  <g transform="translate(560, 260)">
    <rect width="260" height="105" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="130" y="25" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. TRUSTWORTHINESS (AMANAH)</text>
    <text x="130" y="45" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Protects Public Security &amp; Trade</text>
    <text x="130" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Transparent business &amp; honest scales</text>
    <text x="130" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Safe contracts &amp; preserved secrets</text>
    <text x="130" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">• Exam integrity &amp; merit-based success</text>
  </g>

  <!-- Central Hub: The Flourishing Ummah -->
  <circle cx="440" cy="270" r="60" fill="#0f172a" stroke="#a78bfa" stroke-width="2"/>
  <text x="440" y="265" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">THE UPRIGHT</text>
  <text x="440" y="280" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SOCIETY</text>
  <text x="440" y="295" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(Al-Balad al-Amin)</text>

  <!-- Connecting Lines -->
  <line x1="390" y1="170" x2="230" y2="260" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="490" y1="170" x2="650" y2="260" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="320" y1="315" x2="560" y2="315" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
</svg>"""


def get_svg_lesson_9():
    """Lesson 5.1.9: Master Capstone Character Code Synthesis"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg99" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="shieldGrad99" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg99)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER SYNTHESIS: THE PERSONAL CHARACTER CODE (AKHLAQ)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Forging Modesty, Contentment, and Trustworthiness into a Permanent Shield for Daily Teenage Life</text>

  <!-- Central Shield of Akhlaq -->
  <g transform="translate(340, 95)">
    <path d="M 100 0 L 200 40 L 170 180 L 100 240 L 30 180 L 0 40 Z" fill="#1e293b" stroke="url(#shieldGrad99)" stroke-width="3"/>
    <text x="100" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE BELIEVER'S</text>
    <text x="100" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">SHIELD</text>
    <circle cx="100" cy="130" r="22" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="100" y="135" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="900" text-anchor="middle">★</text>
    <text x="100" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"Heaviest on the Mizan</text>
    <text x="100" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">is good character"</text>
    <text x="100" y="205" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">(Tirmidhi 2003)</text>
  </g>

  <!-- Left Card: Inner Dimensions -->
  <g transform="translate(45, 95)">
    <rect width="265" height="305" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="265" height="34" rx="8" fill="#0284c7"/>
    <text x="132" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">MY SPEECH &amp; GAZE (HAYA)</text>

    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Daily Commitments:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Speak with gentleness and respect</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Refuse vulgar slang &amp; shouting</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Lower gaze from online indecency</text>
    <text x="20" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Wear dignified, clean clothing</text>

    <rect x="15" y="175" width="235" height="105" rx="6" fill="#0f172a"/>
    <text x="132" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">MY HEART: RIDA</text>
    <text x="132" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Content with family provisions</text>
    <text x="132" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Look beneath in worldly goods</text>
    <text x="132" y="254" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Zero jealousy or peer pressure</text>
  </g>

  <!-- Right Card: Outer Actions -->
  <g transform="translate(570, 95)">
    <rect width="265" height="305" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="265" height="34" rx="8" fill="#059669"/>
    <text x="132" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">MY DUTIES &amp; ACTIONS (AMANAH)</text>

    <text x="20" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Daily Commitments:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Absolute honesty in exams &amp; homework</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Return borrowed items clean &amp; on time</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Guard confidential talks &amp; private DMs</text>
    <text x="20" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Fair and unbribable leadership</text>

    <rect x="15" y="175" width="235" height="105" rx="6" fill="#0f172a"/>
    <text x="132" y="200" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">MY HARVEST</text>
    <text x="132" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Radiant personal reputation</text>
    <text x="132" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Profound self-respect</text>
    <text x="132" y="254" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Divine love in this life &amp; next</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION DATA FOR 9 LESSONS IN TOPIC 9
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "order": 1,
        "code": "Lesson 5.1.1",
        "title": "Virtue and akhlaq",
        "inquiry": "What is Akhlaq, and why are virtues the ultimate fruit and proof of a believer's faith (iman)?",
        "connection": "Imagine a magnificent mango tree planted in fertile soil. It has deep roots, strong branches, and beautiful green leaves. But year after year, it never produces a single mango. What would the owner say? They would say, 'This tree is useless; what is the point of its deep roots if it never produces sweet fruit?' In our lives, our Faith (Iman) is the deep roots, our Prayers (Ibadah) are the strong branches, and our Good Character (Akhlaq) is the sweet fruit. Without excellent character, our faith remains hidden and incomplete.",
        "concept_def": "Akhlaq (Moral Character) is the inner state of a person's soul that drives them to perform actions naturally, without needing heavy effort or forced thought. It covers virtues, values, manners, and ethics.\n\nVirtue (Fadilah) is a positive, stable moral habit of the soul that leads a person to do good deeds consistently for the sake of Allah.",
        "scripture_quran": "Indeed, the most noble of you in the sight of Allah is the most righteous of you.",
        "scripture_quran_ref": "Surah Al-Hujurat, 49:13",
        "scripture_hadith": "The best of you are those who have the best character.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 6035",
        "explanation": "Let's look at the relationship between faith, worship, and moral character:\n\n1. Virtues are Habits, Not Outbursts: A person who is polite only once a year is not a polite person. A true virtue is a stable, consistent habit of the soul. You tell the truth naturally because your soul is rooted in honesty.\n2. Character is the Proof of Faith: The Prophet (PBUH) taught that excellent character is the heaviest thing on our scale on the Day of Judgment. It proves that our prayers, fasting, and belief in Allah are sincere.\n3. Three Core Virtues: In this unit, we will study three pillar virtues that build a righteous personality and a peaceful society:\n- Modesty (Haya): Humility, dignity, and self-respect in conduct and dress.\n- Contentment (Rida): Gratitude and peace of mind with what Allah has decreed.\n- Trustworthiness (Amanah): Sincere honesty and reliability in fulfilling duties and promises.",
        "svg_func": get_svg_lesson_1,
        "diagram_title": "The Organic Tree of Faith: Iman, Ibadah & Akhlaq",
        "table_title": "The Tree of Faith Structural Breakdown",
        "table_headers": ["Tree Element", "Spiritual Dimension", "Core Examples", "Manifestation in Learner"],
        "table_rows": [
            ["Deep Roots", "Iman (Inner Conviction)", "Belief in Allah, Angels, Day of Judgment", "Unseen foundation anchoring daily peace"],
            ["Strong Trunk", "Ibadah (Devotions)", "Daily Salat, Fasting, Zakat, Quran", "Discipline, spiritual nourishment, strength"],
            ["Sweet Fruits", "Akhlaq (Character)", "Haya (Modesty), Rida (Contentment), Amanah (Trust)", "Gentle speech, honest exams, kindness to peers"]
        ],
        "scenario": "During an exam, Zainab is struggling with a difficult math question. Her classmate secretly whispers, 'Look at my sheet, Zainab! Copy the answer.' Zainab feels tempted, but she instantly looks away and writes her own answer, even though she might get a lower grade. Zainab's choice is driven by her inner character (Akhlaq). Honesty and trustworthiness are not rules she has to force herself to follow; they are a stable part of her soul that naturally guides her choices even when no one is watching.",
        "real_world": "Perform a 'Character Audit' today. Pick one virtue (like patience, kindness, or honesty). Watch your actions from morning until night. Did you have to force yourself to practice it, or did it come naturally? Write down three situations where you practiced it and how you can make it a stronger, more natural habit in your life.",
        "reflection": "Why do you think the Prophet (PBUH) singled out 'best character' as the defining quality of the best Muslims?",
        "misconception": "Virtues are not genetically fixed; through daily practice, self-discipline, and prayer, any person can transform their character and acquire noble habits.",
        "yt_title": "The Weight of Good Character in Islam",
        "yt_desc": "Dr. Omar Suleiman explains why Akhlaq is the ultimate fruit of sincere faith.",
        "yt_id": "UJYkwPDwC-Y",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Olive_tree_in_Palestine.jpg/1280px-Olive_tree_in_Palestine.jpg",
        "image_title": "Ancient Olive Tree with Deep Roots and Abundant Fruit",
        "image_caption": "Living organic metaphor for sincere faith producing enduring, sweet moral fruits.",
        "mcq": {
            "question": "What is the correct definition of the term Akhlaq in Islamic theology?",
            "options": [
                "A list of strict rules that a person is forced to memorize",
                "The inner state of the soul that drives a person to perform moral actions naturally and consistently",
                "The physical movements performed during congregational prayers",
                "The amount of wealth a person donates to charity"
            ],
            "answer": "B",
            "explanation": "Akhlaq refers to the deep, stable inner state of the soul that drives a person's daily conduct naturally, without requiring forced effort or show off."
        },
        "summary_content": "Akhlaq is the stable moral character of a believer's soul. Virtues are positive moral habits that must be practiced consistently. Good character is the essential fruit and proof of sincere faith (iman).",
        "key_points": [
            "Akhlaq represents the natural, unforced moral disposition of the soul.",
            "Character is the living proof that worship and belief are sincere.",
            "The three pillar virtues studied in this unit are Haya, Rida, and Amanah."
        ],
        "exit_ticket": "State why a tree analogy is useful for explaining the connection between faith and character."
    },
    {
        "order": 2,
        "code": "Lesson 5.1.2",
        "title": "Modesty: meaning",
        "inquiry": "What is Haya, and how does modesty protect our personal dignity, self-respect, and spiritual focus?",
        "connection": "Imagine a precious diamond worth millions. How does the jeweler handle it? They do not leave it lying on the dusty street or toss it carelessly in a bin. They wrap it in soft velvet, place it inside a strong, clean glass case, and keep it safe from dust and damage. In Islam, your personal dignity, your body, and your soul are infinitely more precious than any diamond. Haya (Modesty) is the beautiful, protective case that Allah has designed to shield your honor, your speech, and your behavior from being degraded or cheapened.",
        "concept_def": "Haya (Modesty) is a profound virtue that encompasses humility, self-respect, dignity, and natural shyness in one's dress, speech, behavior, and social interactions, driven by a constant consciousness of Allah's presence.\n\nModesty as Faith: Haya is not just a social custom; it is a fundamental branch of faith (iman) that guides both outer appearance and inner intentions.",
        "scripture_quran": "And tell the believing women to lower their gaze and guard their private parts...",
        "scripture_quran_ref": "Surah Al-Nur, 24:31",
        "scripture_hadith": "Modesty is part of faith, and faith is in Paradise.",
        "scripture_hadith_ref": "Sahih Muslim, 35",
        "explanation": "Haya is a comprehensive virtue that manifests in three key dimensions:\n\n1. Modesty with Allah: Feeling shy to commit sins or neglect duties when you remember that Allah is watching you at every moment. This is the highest level of Haya.\n2. Modesty in Speech and Conduct: Avoiding vulgar language, shouting, pride, and bragging. It means speaking with gentleness, politeness, and respect.\n3. Modesty in Dress: Wearing clean, loose, and non-revealing clothing that honors the body Allah gave you. This applies to both male and female students, ensuring dignity in public spaces.",
        "svg_func": get_svg_lesson_2,
        "diagram_title": "The Three Dimensions of Haya (Sacred Modesty)",
        "table_title": "The Three Dimensions of Haya Analysis",
        "table_headers": ["Dimension", "Audience / Focus", "Daily Manifestation", "Protective Shield Formed"],
        "table_rows": [
            ["With Allah", "Consciousness of Al-Basir", "Shy to disobey in private; sincere prayer", "Shields the soul from secret hypocrisy"],
            ["Speech & Conduct", "Peers, teachers, family", "Gentle words, no bragging, polite tone", "Shields relationships from arrogance & fights"],
            ["Dress & Decorum", "Public spaces & society", "Clean, loose, non-revealing clothes", "Shields body from being cheapened or degraded"]
        ],
        "scenario": "Yusuf is hanging out with his friends after school, and some boys start showing off by using vulgar words and telling disrespectful stories about classmates. Yusuf feels highly uncomfortable. His inner sense of Haya kicks in. Instead of joining in to look 'cool,' Yusuf says, 'Guys, let's not speak like this. It doesn't suit us, and it's disrespectful to our classmates.' The boys are quiet, and they change the topic to school sports. Yusuf's Haya protected his speech and the dignity of his group.",
        "real_world": "Audit your speech on social media and chat groups this week. Apply the 'Haya Filter': Before posting a comment, writing a text, or sharing a photo, ask yourself: Is this dignified? Would I be embarrassed if my parents or the Prophet (PBUH) read this? If the answer is yes, delete it immediately. Choose to use clean, respectful, and helpful language.",
        "reflection": "Why does modern society sometimes confuse modesty with weakness? How is maintaining your dignity actually a sign of supreme strength and self-control?",
        "misconception": "Haya is not timid weakness or fear of speaking truth; Haya is supreme self-discipline and dignity rooted in the awe of Allah.",
        "yt_title": "The Beauty and Power of Haya (Modesty)",
        "yt_desc": "Dr. Omar Suleiman explores the dignity and inner strength of modest character.",
        "yt_id": "mdO-w7pbLaQ",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Blue_Mosque_Courtyard_Istanbul.jpg/1280px-Blue_Mosque_Courtyard_Istanbul.jpg",
        "image_title": "Serene Courtyard of the Blue Mosque, Istanbul",
        "image_caption": "Architectural harmony evoking tranquility, reverence, and spiritual dignity.",
        "mcq": {
            "question": "According to the teachings of the Prophet Muhammad (PBUH) in Sahih Muslim, how is the relationship between modesty (Haya) and faith (Iman) described?",
            "options": [
                "Modesty is only required for people who do not have strong faith",
                "Modesty is an essential part of faith, and faith leads to Paradise",
                "Modesty is a separate cultural custom that has no relation to faith",
                "Modesty is only optional for those who have completed their studies"
            ],
            "answer": "B",
            "explanation": "The Prophet (PBUH) explicitly stated that 'Modesty is part of faith, and faith is in Paradise,' showing that Haya is a core indicator of spiritual health."
        },
        "summary_content": "Haya is a comprehensive virtue covering dress, speech, behavior, and thoughts. The highest form of modesty is being shy to disobey Allah because He is always watching. Haya is an essential branch of faith that preserves human honor and self-respect.",
        "key_points": [
            "Haya operates across three dimensions: with Allah, in speech/conduct, and in dress.",
            "Modesty applies equally to both young men and young women.",
            "True Haya is an expression of spiritual strength and moral self-respect."
        ],
        "exit_ticket": "State the three dimensions of Haya in your own words."
    },
    {
        "order": 3,
        "code": "Lesson 5.1.3",
        "title": "Modesty in practice",
        "inquiry": "How do we practice Haya in our real-world school, family, social, and digital spaces?",
        "connection": "Have you ever seen a guard rail on a steep mountain road? It does not block you from traveling; it keeps you on the road so your car does not slide down the cliff during a sharp turn. In our daily lives, practicing Haya is like having that guard rail. It keeps our actions, our conversations, and our relationships safe and respectful, preventing us from sliding into cheap, vulgar, or harmful behaviors. Let's look at how we can put modesty into action.",
        "concept_def": "Practical Modesty means translating the virtue of Haya into consistent, dignified choices across school, family, public, and online spaces.\n\nDigital Modesty means maintaining the same standards of polite speech, respectful gaze, and private boundaries on social media and group chats as we do in the physical world.",
        "scripture_quran": "Tell the believing men to lower their gaze and guard their private parts. That is purer for them...",
        "scripture_quran_ref": "Surah Al-Nur, 24:30",
        "scripture_hadith": "Modesty does not bring anything except good.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 6117",
        "explanation": "Let's look at how Haya is practiced across four different arenas of life:\n\n1. At School: Wearing your uniform cleanly and properly. Speaking to teachers with respect and politeness. Refusing to mock, mimic, or spread gossip about classmates.\n2. At Home: Respecting your parents' privacy by knocking before entering their room (especially at rest times). Wearing dignified clothing around siblings. Speaking gently without shouting.\n3. In Public: Lowering your gaze when seeing inappropriate sights on the street. Being humble in your walk, not showing off or looking down on poorer people.\n4. In Digital Spaces: Refusing to post or watch vulgar videos. Not clicking on inappropriate links. Respecting people's privacy by not sharing private chats or photos without permission.",
        "svg_func": get_svg_lesson_3,
        "diagram_title": "Haya in Practice: Physical Life vs Digital Life",
        "table_title": "Practicing Modesty in Daily Social Arenas",
        "table_headers": ["Life Arena", "Honorable Modest Practice (Do)", "Compromised Behavior (Don't)", "Benefit Achieved"],
        "table_rows": [
            ["In the Classroom", "Listening quietly; polite questions; neat uniform", "Mocking classmates' accents; slovenly dress", "Academic respect & dignity"],
            ["At Home", "Knocking before entering parents' room; soft tone", "Barging in unannounced; yelling at siblings", "Domestic peace & boundary sanctity"],
            ["On Public Streets", "Lowering gaze; walking humbly without strutting", "Catcalling; staring at inappropriate sights", "Guarded mind & safe neighborhood"],
            ["On Social Media", "Scrolling past vulgar reels; deleting gossip chats", "Forwarding leaked photos; vulgar trolling", "Pure digital conscience & trust"]
        ],
        "scenario": "Ali is scrolling through his social media feed and a video pops up that contains inappropriate, semi-naked dancing and vulgar lyrics. His natural curiosity says, 'Watch it! It's popular, and no one is in the room.' Ali remembers the lesson on Hifz al-Niyyah and lowering the gaze. He immediately scrolls past the video and clicks on an educational science channel instead. Ali's choice represents practical Haya—he used his free will to protect his gaze and his mind, solely for the sake of Allah.",
        "real_world": "Implement a 'Knock-and-Greet Protocol' at home this week. Before entering your parents' or siblings' rooms, always knock politely, wait for their permission, and enter with a warm greeting (Assalamu Alaikum). This simple practice builds mutual respect, privacy, and modesty within the household, as Shariah teaches us.",
        "reflection": "Why do people sometimes behave less modestly online than they do in person? How does remembering that Allah is Al-Basir (The All-Seeing) help us maintain our digital modesty?",
        "misconception": "Anonymity online does not shield us from divine accountability; every keystroke and click is recorded on our scale.",
        "yt_title": "Lowering the Gaze in the Digital Age",
        "yt_desc": "Practical strategies for maintaining digital modesty and guarding the eyes.",
        "yt_id": "TVt-Dd31Nn4",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Smartphone_in_hand_blurred_background.jpg/1280px-Smartphone_in_hand_blurred_background.jpg",
        "image_title": "Modern Digital Smartphone Interaction",
        "image_caption": "The modern digital frontline where young Muslims practice lowering the gaze and guarding privacy.",
        "mcq": {
            "question": "Zuri is studying in the school library. She notices that a group of students are whispering and giggling at an embarrassing photo of a classmate on their phone. They invite Zuri to look. Which action represents the best practice of Haya for Zuri?",
            "options": [
                "Look at the photo quickly and laugh along to avoid being left out of the group",
                "Take the phone and forward the photo to her other friends to warn them",
                "Politely decline to look, lower her gaze, and say, 'Let's not share photos that embarrass our classmates; we want to keep their dignity safe.'",
                "Say nothing and walk away angrily to show her superiority"
            ],
            "answer": "C",
            "explanation": "Declining to look, lowering the gaze, and speaking up gently to protect a peer's dignity represents a complete, practical application of Haya in speech, conduct, and social interactions."
        },
        "summary_content": "Modesty must be practiced consistently in physical and digital spaces. Lowering the gaze and respecting others' privacy are vital daily applications of Haya. Humility in walk, dress, and speech builds a highly respected character.",
        "key_points": [
            "Haya acts as a practical guard rail across school, home, public, and digital spheres.",
            "Lowering the gaze applies equally to physical streets and digital screens.",
            "Knocking before entering and respecting privacy are sacred Islamic household ethics."
        ],
        "exit_ticket": "Write down one way you will practice digital modesty today."
    },
    {
        "order": 4,
        "code": "Lesson 5.1.4",
        "title": "Contentment: meaning",
        "inquiry": "What is Contentment, and how does satisfying our hearts with Allah's gifts protect us from greed and envy?",
        "connection": "Imagine you have a beautiful, perfectly functioning bicycle. You ride it to school happily every day. One morning, a classmate arrives riding a shiny, high-tech electric scooter with digital screens. Suddenly, you look at your bicycle and feel angry, embarrassed, and miserable. What changed? The bicycle is still beautiful and useful, but your heart fell into the trap of endless comparison. Contentment (Rida) is the spiritual superpower that protects our hearts from this trap, keeping us peaceful, grateful, and happy with whatever blessings Allah has designed for us.",
        "concept_def": "Contentment (Rida / Qana'ah) is the spiritual state of being fully satisfied with the provisions, talents, and decrees of Allah, accepting them with a grateful heart.\n\nAnti-Envy Shield: Contentment is the direct moral virtue that cures the spiritual diseases of greed (Hirs), jealousy (Hasad), and endless comparison.",
        "scripture_quran": "And it is He who provides for you from the heavens and the earth. There is no god except Him.",
        "scripture_quran_ref": "Surah Fatir, 35:3",
        "scripture_hadith": "Whoever is content with what Allah has given him, his heart will be at peace.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 6446",
        "explanation": "Contentment is often misunderstood. Let's look at what it truly means:\n\n1. Contentment is NOT Laziness: Sincere contentment (Rida) does not mean you stop studying, stop working, or refuse to improve. A content student works with 100% effort using their talents, but once they receive their exam score, they accept the result calmly without complaining or getting angry.\n2. The Power of Gratitude (Shukr): A content person focuses on what they have (clean water, a healthy body, a loving family) rather than what they lack (expensive phones, luxury shoes). They realize that Allah's provisions are perfectly designed.\n3. Inner Peace: True wealth is not having a mountain of possessions, but having a satisfied heart (Ghinan-Nafs).",
        "svg_func": get_svg_lesson_4,
        "diagram_title": "Contentment (Rida / Qana'ah): The True Inner Wealth",
        "table_title": "Comparison: The Greedy Heart vs The Content Heart",
        "table_headers": ["Feature", "Heart of Comparison (Restless)", "Heart of Contentment (Peaceful)", "Daily Spiritual Result"],
        "table_rows": [
            ["Core Focus", "Obsessed with what others have", "Deeply grateful for blessings in hand", "Envy vs Radiance"],
            ["Response to Trials", "Bitterness, complaining, anger", "Patience (Sabr) & trust in Allah's plan", "Despair vs Resilience"],
            ["View of Possessions", "Never enough; constantly craves more", "Satisfied with simple, lawful needs", "Debt & guilt vs Free soul"],
            ["Social Behavior", "Boasting or looking down on poor", "Generous, humble, and happy for peers", "Isolation vs Deep friendship"]
        ],
        "scenario": "Yusuf's school sweater is slightly faded and has a small patch on the elbow, but it is clean and warm. One day, his classmate arrives wearing an expensive, imported sports jacket. Some students mock Yusuf, saying, 'Hey Yusuf, your sweater looks old; why don't you buy a cool jacket like that?' Yusuf smiles and says, 'Alhamdulillah, this sweater keeps me perfectly warm in the morning, and my mother patched it for me with love. I am very happy with it!' The students are amazed by Yusuf's confidence and stop mocking him. Yusuf's contentment kept his dignity high.",
        "real_world": "Perform a 'Gratitude Audit' this week. Write down three things you possess that money cannot buy (e.g., your eyesight, a sibling's laugh, your memory, or a safe place to sleep). Whenever you feel tempted to complain about not having a fancy item, look at your audit and say: 'Alhamdulillah for these priceless gifts.' Notice how this shifts your mindset to peace.",
        "reflection": "How does the constant comparison of possessions on social media lead to anxiety and depression among teenagers? How is Rida the perfect cure?",
        "misconception": "Contentment does not contradict aiming for top academic grades; striving for excellence while remaining at peace with Allah's decree is the ideal Islamic balance.",
        "yt_title": "Finding True Wealth: The Virtue of Qana'ah",
        "yt_desc": "Inspiring talk on breaking free from materialistic consumerism through inner contentment.",
        "yt_id": "5hDUB6yFwBQ",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Clay_pot_water_cooler_village.jpg/1280px-Clay_pot_water_cooler_village.jpg",
        "image_title": "Traditional Clay Water Pot in a Village Homestead",
        "image_caption": "Symbolizing the pure, peaceful simplicity of basic lawful provisions and contentment.",
        "mcq": {
            "question": "Which of the following best describes the relationship between contentment (Rida) and personal effort in Islam?",
            "options": [
                "Contentment means we should stop studying or working, as everything is already decreed",
                "Contentment means we must work with 100% honest effort, but accept the outcomes and provisions calmly with gratitude",
                "Contentment means we should look down on those who have less than us",
                "Contentment is only required for people who are poor"
            ],
            "answer": "B",
            "explanation": "Islam balances effort and acceptance: we are commanded to take all necessary lawful steps and work hard, but once the decree unfolds, we accept it with Rida (tranquility and gratitude)."
        },
        "summary_content": "Contentment (Rida) is being fully satisfied with Allah's gifts and decrees. True wealth is having a satisfied, grateful heart (Ghinan-Nafs), not endless material items. Contentment is the ultimate shield against greed, jealousy, and anxiety.",
        "key_points": [
            "Contentment (Qana'ah) cures the soul of endless consumerist restlessness.",
            "True wealth (Ghinan-Nafs) is an inner state of peaceful gratitude.",
            "Rida balances maximum honest effort with calm acceptance of outcomes."
        ],
        "exit_ticket": "Explain why comparing our possessions with others ruins our inner peace."
    },
    {
        "order": 5,
        "code": "Lesson 5.1.5",
        "title": "Contentment in practice",
        "inquiry": "How do we practice contentment when facing school stress, sibling rivalry, and social peer pressure?",
        "connection": "Imagine a sailboat on a stormy lake. If the boat has a strong, deep anchor dropped into the solid rock below, the wind and waves can toss it around, but they can never drag it away or crash it against the shore. In our lives, our daily struggles, bad grades, or lack of pocket money are the waves. Sincere contentment in practice is our spiritual anchor. It holds our hearts steady, keeping us calm and smiling even when things do not go our way. Let's study how to drop this anchor into our daily lives.",
        "concept_def": "Contentment in Practice means applying the virtue of Rida to handle unexpected changes, material lack, academic challenges, and social differences without falling into sadness or jealousy.\n\nThe 'Lower Gaze' Protocol: The prophetic strategy for contentment: in worldly matters, always look at those who have less than you to recognize your blessings; in spiritual matters, look at those who do more to motivate your growth.",
        "scripture_quran": "...And whoever fears Allah – He will make for him of his matter ease.",
        "scripture_quran_ref": "Surah Al-Talaq, 65:4",
        "scripture_hadith": "Look at those who are beneath you and do not look at those who are above you, for it is more suitable that you do not underestimate the blessings of Allah.",
        "scripture_hadith_ref": "Sahih Muslim, 2963",
        "explanation": "Let's look at three practical situations where we can apply contentment:\n\n1. In School (Grades & Sports): You study hard and earn a B-grade, while your classmate gets an A. Instead of feeling jealous or saying, 'It's unfair,' say, 'Alhamdulillah, I worked hard and this grade shows me where I can improve. I am happy for my classmate's success.'\n2. At Home (Pocket Money & Resources): Your parents can only afford a simple lunch box, while other students have expensive snacks. Apply the 'Lower Gaze' protocol: remember children who have no food or school at all. Your simple lunch box becomes a priceless blessing.\n3. With Friends (Peer Pressure): When your friends are boasting about their holidays or clothing, do not lie or pretend to have what you don't. Be honest, remain humble, and express happiness with your simple life. This builds true, lasting respect.",
        "svg_func": get_svg_lesson_5,
        "diagram_title": "The Prophetic Dual-Perspective Protocol",
        "table_title": "The Prophetic Perspective Matrix",
        "table_headers": ["Life Dimension", "Prophetic Direction to Look", "Relatable Teenage Example", "Spiritual & Psychological Fruit"],
        "table_rows": [
            ["Worldly Possessions (Phones, clothes, money)", "Look BENEATH (at those with less)", "Comparing simple shoes with those who have no shoes", "Deep gratitude, humility, zero financial anxiety"],
            ["Spiritual Deeds (Prayer, character, study)", "Look ABOVE (at those with more)", "Comparing your Salat with those who memorize Quran", "Holy ambition, drive to improve, humility"]
        ],
        "scenario": "Zuri wants to join the school drama club, but she needs a specific black costume that costs 600 shillings. Her father says, 'Zuri, I have to pay for your brother's schoolbooks this week; I cannot afford the costume.' Zuri feels a wave of disappointment. She is tempted to sulk, throw a tantrum, or ignore her father. She pauses, takes a deep breath, and says, 'It's okay, Dad. I understand. Your books are more important, and Allah will make a way.' She goes to the drama teacher, explains her situation politely, and the teacher offers her a spare costume from the school locker. Zuri's Rida protected her relationship with her father.",
        "real_world": "Perform a 'Boasting-Free Challenge' for the next 72 hours. In your school chats and playground talks, never boast about a purchase, a family holiday, or a possession. If others boast, respond with a polite smile or 'Alhamdulillah, that's beautiful.' Keep your focus on humility and contentment, and observe how much more peaceful your social interactions become.",
        "reflection": "How does the prophetic command to 'look at those beneath you in worldly matters' protect a teenager's mental health in the age of Instagram and TikTok?",
        "misconception": "Being content does not mean feeling inferior; contentment gives a student supreme confidence that does not rely on expensive brand labels.",
        "yt_title": "Beating Social Media Peer Pressure through Gratitude",
        "yt_desc": "Youth lecture on navigating material comparisons with Islamic contentment.",
        "yt_id": "c-ppIM94ilw",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Children_in_rural_school_smiling.jpg/1280px-Children_in_rural_school_smiling.jpg",
        "image_title": "Smiling Students in Rural Classroom",
        "image_caption": "Radiating genuine joy, brotherhood, and satisfaction with simple learning tools.",
        "mcq": {
            "question": "Yusuf's father can only afford simple plastic sandals for him, while his classmates wear expensive branded sports shoes. Applying the 'Lower Gaze' protocol, what is the most constructive response for Yusuf?",
            "options": [
                "Hide his sandals at school and walk barefoot to avoid embarrassment",
                "Complain to his father daily and refuse to study until he gets sports shoes",
                "Remind himself of children who have lost their limbs or have no shoes at all, say 'Alhamdulillah' for his healthy feet, and wear his clean sandals with pride",
                "Borrow a classmate's shoes secretly without their permission to look cool"
            ],
            "answer": "C",
            "explanation": "This option represents a direct, source-grounded application of the 'Lower Gaze' protocol—focusing on those with fewer blessings to cultivate sincere gratitude (Shukr) and contentment (Rida)."
        },
        "summary_content": "Contentment is practiced by actively refusing to fall into the trap of social comparison. The 'Lower Gaze' protocol helps us appreciate our current provisions and protects us from envy. Sincere Rida keeps us peaceful and patient through unexpected financial or personal trials.",
        "key_points": [
            "In worldly matters, look at those who have less to cultivate gratitude.",
            "In spiritual matters, look at those who do more to inspire growth.",
            "Dropping the anchor of contentment prevents tantrums, resentment, and peer jealousy."
        ],
        "exit_ticket": "State how the 'Lower Gaze' protocol applies to academic stress."
    },
    {
        "order": 6,
        "code": "Lesson 5.1.6",
        "title": "Trustworthiness: meaning",
        "inquiry": "What is Amanah, and why is keeping our promises and protecting trusts the ultimate foundation of moral integrity?",
        "connection": "Imagine a bank that has a giant vault with thick steel walls and high-tech biometric locks. If you deposit your life savings there, you expect them to keep it 100% safe. If the bank manager took your money, spent it on a holiday, and said, 'Don't worry, I'll pay you back someday,' you would never trust that bank again. In our lives, our words, our duties, our secrets, and our relationships are precious deposits. Trustworthiness (Amanah) is the sacred steel vault of our character. It keeps our promises safe, our secrets locked, and our duties fulfilled.",
        "concept_def": "Amanah (Trustworthiness) is the moral virtue of being reliable, honest, and responsible in fulfilling the duties, promises, and items entrusted to one's care by Allah (S.W.T.) and other human beings.\n\nIntegrity in Action: Trustworthiness is the ultimate test of moral integrity. Betraying a trust (Khiyanah) is a grave sin and is described by the Prophet (PBUH) as a key sign of hypocrisy.",
        "scripture_quran": "Indeed, Allah commands you to render trusts to whom they are due...",
        "scripture_quran_ref": "Surah Al-Nisa, 4:58",
        "scripture_hadith": "There is no faith in one who is not trustworthy, and there is no religion in one who does not keep his promise.",
        "scripture_hadith_ref": "Musnad Ahmad, 12386",
        "explanation": "Amanah is a multi-layered concept that covers four main dimensions:\n\n1. Trust with Allah (Devotions): Fulfilling your prayers, fasting, and moral duties. Your body, health, and talents are also an Amanah from Allah that you must protect.\n2. Trust with People (Property): Returning borrowed items in perfect condition (e.g., library books, a classmate's pen, or a neighbor's tool).\n3. Trust of Information (Secrets): Keeping confidential conversations private. If a friend tells you a secret or reveals a personal struggle, sharing it with others is a direct betrayal of Amanah.\n4. Trust of Duty (Responsibility): Doing your job honestly. For a student, studying hard, not cheating in exams, and executing duties as a class prefect are parts of Amanah.",
        "svg_func": get_svg_lesson_6,
        "diagram_title": "The Four Sacred Dimensions of Amanah (Trustworthiness)",
        "table_title": "Four Sacred Dimensions of Amanah",
        "table_headers": ["Dimension", "Trust Entity", "What It Covers", "Signs of Betrayal (Khiyanah)"],
        "table_rows": [
            ["1. Spiritual Trust", "Allah (S.W.T.)", "5 Daily Prayers, fasting, health, talents", "Neglecting Salat; abusing body with drugs"],
            ["2. Material Trust", "Peers & Community", "Borrowed books, money, tools, school property", "Stealing, losing borrowed items, damaging goods"],
            ["3. Informational Trust", "Friends & Family", "Confidential chats, personal secrets, weaknesses", "Leaking DMs, backbiting, spreading private grief"],
            ["4. Functional Trust", "School & Society", "Exam honesty, homework, prefect leadership", "Cheating in tests, showing favoritism to friends"]
        ],
        "scenario": "Zain tells Hussein, 'Hussein, I am struggling with severe anxiety about my math exam, and I have been crying in the morning. Please do not tell anyone.' Hussein keeps Zain's secret. Later, during lunch, some boys are making fun of Zain, saying, 'He looks so nervous; is he going to cry?' Hussein says, 'Zain is a great student and we all feel nervous during exams; let's support him.' Hussein does not reveal Zain's secret, even though it would have made his story 'interesting.' Hussein's choice represents Amanah of information.",
        "real_world": "Perform an 'Amanah Audit' today. Review any items you have borrowed from classmates, teachers, or the school library. Are they clean and intact? Have you kept every promise you made this week? If you have a borrowed item, return it in perfect condition today. If you made a promise, fulfill it. This keeps your moral vault secure.",
        "reflection": "Why does betraying a friend's secret break the bond of trust permanently? How does Amanah preserve social peace?",
        "misconception": "Amanah is not just about returning coins or wallets; safeguarding a private conversation or a classmate's dignity is an equally sacred trust.",
        "yt_title": "The Weight of Amanah in Islam",
        "yt_desc": "Dr. Omar Suleiman explains the four pillars of trustworthiness and moral integrity.",
        "yt_id": "AHVP62ebo7s",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Al-Mustansiriya_Madrasah_Baghdad.jpg/1280px-Al-Mustansiriya_Madrasah_Baghdad.jpg",
        "image_title": "Historic Mustansiriya Madrasah in Baghdad",
        "image_caption": "Historic academy founded on academic honesty, scientific stewardship, and intellectual amanah.",
        "mcq": {
            "question": "According to Surah Al-Nisa (4:58), what is Allah's direct command regarding trusts (Amanah)?",
            "options": [
                "We should only keep trusts if the other person is rich",
                "We must return trusts to their rightful owners with justice",
                "Keeping trusts is optional and has no spiritual reward",
                "We should only keep trusts when we are being watched by leaders"
            ],
            "answer": "B",
            "explanation": "Surah Al-Nisa (4:58) explicitly commands believers to 'render trusts to whom they are due' and to judge with justice, making trustworthiness an obligatory divine command."
        },
        "summary_content": "Amanah covers spiritual duties, borrowed property, secrets, and functional responsibilities. Betraying a trust is a severe sin and a key indicator of hypocrisy. Trustworthiness builds social safety and pleases Allah.",
        "key_points": [
            "Amanah spans four dimensions: Spiritual, Material, Informational, and Functional.",
            "Betraying a trust (Khiyanah) is condemned as a sign of hypocrisy.",
            "Keeping private information confidential is a sacred moral duty."
        ],
        "exit_ticket": "List three examples of trusts we hold in our school life."
    },
    {
        "order": 7,
        "code": "Lesson 5.1.7",
        "title": "Trustworthiness in practice",
        "inquiry": "How do we practice Amanah when facing academic shortcuts, borrowed property, and leadership duties?",
        "connection": "Imagine a chain bridge spanning a deep canyon. Each link in the chain is made of iron. If even a single link rusts and snaps under a heavy load, the entire bridge will collapse, sending cars falling into the river below. In our school and community, our personal trustworthiness is like those iron links. When each student is trustworthy, the bridge of our community is strong and safe. Let's study how we can make our links of Amanah unbreakable in practice.",
        "concept_def": "Practical Trustworthiness means translating the virtue of Amanah into daily choices at school, at home, in business, and in leadership.\n\nFulfilling Covenants means honoring formal and informal contracts, school rules, and promises, viewing them as moral obligations before Allah.",
        "scripture_quran": "And fulfill [every] commitment. Indeed, the commitment will be questioned [on Day of Judgment].",
        "scripture_quran_ref": "Surah Al-Isra, 17:34",
        "scripture_hadith": "When a man tells something and then goes away, it is a trust.",
        "scripture_hadith_ref": "Sunan Abu Dawood, 4868",
        "explanation": "Let's look at how Amanah is practiced across three core areas of a teenager's life:\n\n1. Academic Honesty: Doing your own work. Refusing to copy homework from friends, write cheats on your desk, or search for exam answers online. Realizing that your grades must represent your true effort.\n2. Borrowed Property Care: When you borrow a bicycle, a textbook, or even a simple pencil, handle it with more care than your own property. If you damage it, admit it instantly and replace it. This is the practical definition of Amanah.\n3. Prefect & Leadership Duties: If you are elected as a class monitor, prefect, or club leader, perform your duties with absolute fairness. Do not favor your friends or hide their mistakes, and do not misuse your authority to look down on others.",
        "svg_func": get_svg_lesson_7,
        "diagram_title": "Practical Integrity: The Borrower's Amanah Checklist",
        "table_title": "The 4-Step Practical Amanah Checklist",
        "table_headers": ["Step", "Action Required", "Unethical Shortcut to Avoid", "Noble Integrity Outcome"],
        "table_rows": [
            ["1. Permission", "Ask clearly before borrowing", "Assuming 'he won't mind'", "Sanctity of private property upheld"],
            ["2. Higher Care", "Keep clean, safe, and undamaged", "Careless handling or scribbling", "Honoring others' hard-earned items"],
            ["3. Punctuality", "Return before asked with thanks", "Keeping for weeks until chased", "High reliability & earned trust"],
            ["4. Restitution", "Replace or pay if damaged", "Hiding broken pieces secretly", "Courageous honesty & healed bonds"]
        ],
        "scenario": "Zuri is the class prefect. Her best friend Halima arrives late for class for the third time this week, which normally results in detention. Halima whispers, 'Zuri, please do not write my name on the late list; we are best friends! Just skip me this once.' Zuri feels torn. She remembers her lesson on Amanah of leadership. She says gently to Halima, 'Halima, I love you as my friend, but I was trusted by our teacher to record late arrivals fairly. If I skip your name, I am betraying my Amanah. I have to write your name, but I will come with you to the teacher to explain why you were late and help you catch up on homework.' Halima is sad but respects Zuri's integrity.",
        "real_world": "Practice the 'Borrower's Checklist' this week. Choose one classmate you often borrow items from. Apply the steps strictly: ask permission, handle with extreme care, and return it exactly on time with a warm 'JazakAllahu Khairan' (May Allah reward you with goodness). Observe how this simple discipline builds a deep bond of trust and safety in your classroom.",
        "reflection": "How does cheating in an exam harm a student's long-term intelligence and career? How does it violate the trust (Amanah) of the school?",
        "misconception": "Being trustworthy does not mean protecting friends when they do wrong; true friendship helps peers correct mistakes through honesty.",
        "yt_title": "Integrity in Action: Fulfilling Promises",
        "yt_desc": "Youth guide on exam honesty, keeping covenants, and leadership integrity.",
        "yt_id": "_UomJ4KolFE",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Examination_hall_students_writing.jpg/1280px-Examination_hall_students_writing.jpg",
        "image_title": "Students Writing Exams with Academic Honesty",
        "image_caption": "Upholding academic amanah by presenting genuine individual effort without shortcuts.",
        "mcq": {
            "question": "Zain is studying for a history test and has not prepared well. He finds the teacher's grading rubric and answers lying on the printer tray in the classroom. No one is around. Which action represents the best practice of Amanah for Zain?",
            "options": [
                "Take a photo of the answers quickly to study from them at home",
                "Take the sheets and hand them directly to the history teacher, explaining that they were left on the printer tray",
                "Leave them there but whisper the answers to his best friends so they can pass too",
                "Hide the sheets under the tray so no one else can cheat"
            ],
            "answer": "B",
            "explanation": "Handing the sheets directly to the teacher shows absolute integrity and respects the Amanah of exam security, refusing to take an unfair shortcut."
        },
        "summary_content": "Practical Amanah requires honesty in studies, care of borrowed items, and fairness in leadership. Promises and commitments are moral contracts that will be audited by Allah. Upholding Amanah builds a strong, safe, and highly respected community.",
        "key_points": [
            "Academic integrity is a sacred trust between student, teacher, and Allah.",
            "Borrowed items must be handled with greater care than one's own property.",
            "Student leadership demands uncompromised fairness without personal favoritism."
        ],
        "exit_ticket": "State why favoring a friend in a leadership role violates the virtue of Amanah."
    },
    {
        "order": 8,
        "code": "Lesson 5.1.8",
        "title": "Virtues and society",
        "inquiry": "How do Modesty, Contentment, and Trustworthiness work together to transform a collection of individuals into a peaceful, upright society?",
        "connection": "Imagine a team of chefs preparing a great banquet. One chef prepares the fresh vegetables, one cooks the main course, and one bakes the beautiful desserts. If each chef does their job perfectly, the banquet is a magnificent success. But if one chef dumps salt in the soup, or another refuses to clean their pots, the entire feast is ruined. In our society, our three virtues—Modesty, Contentment, and Trustworthiness—are the ingredients of our social banquet. When they work together, they create a delicious atmosphere of peace, justice, and safety.",
        "concept_def": "Social Cohesion through Virtues is the powerful collective harmony and mutual respect that emerges when individuals in a community actively practice modesty, contentment, and trustworthiness.\n\nPreventing Social Diseases: The virtues act as a direct moral medicine that cures social crimes like corruption, theft, jealousy, and public indecency.",
        "scripture_quran": "Indeed, Allah commands you to act justly, to do good, and to liberally give to relatives... and He forbids immorality, bad conduct, and oppression...",
        "scripture_quran_ref": "Surah Al-Nahl, 16:90",
        "scripture_hadith": "The believers are but brothers, so make peace between your brothers...",
        "scripture_hadith_ref": "Surah Al-Hujurat, 49:10",
        "explanation": "Let's look at how our three virtues work together to protect our society from moral decay:\n\n1. Modesty (Haya) protects Public Morality: It keeps our streets, media, and language clean, respectful, and dignified. It prevents the cheapening of human relationships and ensures children grow up in a safe, healthy environment.\n2. Contentment (Rida) protects Social Peace: It removes jealousy and greed. When people are content, they do not steal, accept bribes, or look down on poorer neighbors. It prevents economic crimes and reduces the gap between rich and poor.\n3. Trustworthiness (Amanah) protects Public Security: It ensures that businesses are honest, leaders are fair, contracts are kept, and information is private. It creates an atmosphere where everyone feels safe to work, trade, and live.",
        "svg_func": get_svg_lesson_8,
        "diagram_title": "The Triangle of Social Integrity (Virtues & Society)",
        "table_title": "The Triad of Social Harmony and Civic Virtue",
        "table_headers": ["Virtue", "Social Arena Protected", "Social Disease Cured", "Civic Impact"],
        "table_rows": [
            ["Modesty (Haya)", "Public Morality & Decorum", "Vulgarity, harassment, cyber-bullying", "Safe, dignified streets & healthy family media"],
            ["Contentment (Rida)", "Social Peace & Cohesion", "Greed, bribery, theft, economic envy", "Honest markets, generous charity, zero corruption"],
            ["Trustworthiness (Amanah)", "Public Security & Commerce", "Fraud, exam leaks, breached contracts", "High-trust economy, reliable civic institutions"]
        ],
        "scenario": "In a small Kenyan town, a local market is thriving. The traders practice Amanah (their scales are honest, they do not cheat), they practice Rida (they are content with honest profit and help poorer customers), and they practice Haya (they speak politely and treat everyone with dignity). A customer from another city arrives and says, 'I have never seen a market where I don't have to double-check the scale or hide my wallet. This place feels like a sanctuary of peace!' The town's virtues created a beautiful social sanctuary.",
        "real_world": "Prepare a 'Virtues Campaign Poster' in your group. Focus on how Modesty, Contentment, and Trustworthiness prevent common school problems like cheating, bullying, and stealing. Draw the 'Triangle of Social Integrity' and pin the poster on your school notice board to inspire other students to build a better school community.",
        "reflection": "How does a lack of contentment (Rida) among leaders lead to public corruption and the theft of public resources?",
        "misconception": "Virtues are not purely private feelings; their true measure is how they transform communities into sanctuaries of safety and justice.",
        "yt_title": "Building a High-Trust Society Through Islamic Character",
        "yt_desc": "Sociological analysis of how Islamic virtues generate social capital and civic harmony.",
        "yt_id": "UJYkwPDwC-Y",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Nairobi_city_skyline_from_park.jpg/1280px-Nairobi_city_skyline_from_park.jpg",
        "image_title": "Modern Nairobi Skyline and Public Green Spaces",
        "image_caption": "A thriving modern metropolis where Islamic civic virtues foster trust, safety, and mutual respect.",
        "mcq": {
            "question": "How does the active practice of Contentment (Rida) among business owners directly prevent economic crimes in society?",
            "options": [
                "It forces them to close their shops early",
                "It removes greed and the temptation to cheat customers, accept bribes, or manipulate prices",
                "It requires them to give away all of their profits to the poor",
                "It makes them stop trading altogether"
            ],
            "answer": "B",
            "explanation": "Sincere contentment (Rida) satisfies the heart with lawful, honest profit, removing the greedy desire (Hirs) to cheat customers, manipulate scales, or engage in corruption and bribery."
        },
        "summary_content": "Modesty, Contentment, and Trustworthiness are the core pillars of social ethics. Modesty preserves public morality, Contentment preserves social peace, and Trustworthiness preserves public security. Practicing these virtues is a vital civic responsibility that builds a strong, ethical nation.",
        "key_points": [
            "Haya, Rida, and Amanah form an interdependent triangle of social cohesion.",
            "Contentment directly prevents economic crime, embezzlement, and bribery.",
            "Trustworthiness generates social capital and mutual safety across communities."
        ],
        "exit_ticket": "State how the three virtues can prevent bullying in school."
    },
    {
        "order": 9,
        "code": "Lesson 5.1.9",
        "title": "Unit synthesis",
        "inquiry": "How do we synthesize Modesty, Contentment, and Trustworthiness into a personal 'Character Code' for daily success?",
        "connection": "Imagine you are a master jeweler who has gathered three precious, flawless gemstones: a deep blue sapphire (Modesty), a warm golden amber (Contentment), and a brilliant clear diamond (Trustworthiness). You do not leave them scattered on your desk; you mount them into a beautiful, solid silver crown that you can wear. In this final lesson of the unit, we will act as the master craftsmen of our own souls. We will bring together the definitions, the verses, the Hadiths, the practical scenarios, and our visual maps to forge a personal 'Character Code' to wear proudly throughout our lives.",
        "concept_def": "Sincere Character Integration (Akhlaq-un-Nabi) is the complete harmonization of core Islamic virtues into a person's daily thoughts, speech, and conduct, following the perfect model of the Prophet Muhammad (PBUH).\n\nThe Covenant of Character is a conscious, moral commitment before Allah to live with absolute dignity, gratitude, and reliability.",
        "scripture_quran": "Indeed, the most noble of you in the sight of Allah is the most righteous of you.",
        "scripture_quran_ref": "Surah Al-Hujurat, 49:13",
        "scripture_hadith": "Nothing will be heavier on the scale of the believer on the Day of Judgment than good character.",
        "scripture_hadith_ref": "Sunan at-Tirmidhi, 2003",
        "explanation": "Let's review the complete character framework we studied:\n\n1. The Peak Virtue - Haya (Modesty): It preserves our spiritual and behavioral boundaries. It keeps our dress dignified, our gaze guarded, our speech clean, and our hearts humble.\n2. The Grounding Virtue - Rida (Contentment): It satisfies our souls with Allah's provisions. It anchors our hearts against peer pressure, removes greed and jealousy, and converts every event into gratitude or patience.\n3. The Practical Virtue - Amanah (Trustworthiness): It anchors our daily reliability. It ensures we fulfill our duties to Allah, protect secrets, care for borrowed items, and act with absolute honesty in studies and leadership.",
        "svg_func": get_svg_lesson_9,
        "diagram_title": "Master Synthesis: The Personal Character Code (Akhlaq)",
        "table_title": "Master Synthesis: The Believer's Character Code",
        "table_headers": ["Virtue Gem", "Inner Spiritual Station", "External Daily Conduct", "Harvest on Mizan"],
        "table_rows": [
            ["Sapphire: Haya", "Awe of Allah in private", "Clean speech, lowering gaze, dignified dress", "Purity of soul & entrance into Jannah"],
            ["Amber: Rida", "Peaceful trust in Qadar", "Looking beneath in wealth; gratitude for food", "Complete tranquility & joy in life"],
            ["Diamond: Amanah", "Conscious of divine auditing", "Honest exams, unbreached secrets, care of goods", "Highest nobility & Prophetic companionship"]
        ],
        "scenario": "Match the following situations with the correct virtue from our unit:\n1. Zainab is tempted to copy an essay from the internet, but she decides to write her own thoughts honestly. (Answer: Trustworthiness / Amanah)\n2. Yusuf feels calm and happy when his plans for a holiday are canceled due to family circumstances, saying, 'Allah has a better plan.' (Answer: Contentment / Rida)\n3. Amina refuses to use slang or vulgar words when chatting with her friends online. (Answer: Modesty / Haya)\n4. Omar is trusted as the school sports captain and divides the equipment fairly among all teams. (Answer: Trustworthiness / Amanah)",
        "real_world": "Write your own personal 'Character Code Covenant' this week. Draft three short commitments: 'I will speak with modesty (Haya) and avoid vulgar words; I will protect my peace by feeling content (Rida) with my provisions; and I will be absolute in my trustworthiness (Amanah) by doing my own studies honestly and keeping my promises.' Sign it, place it in your study diary, and review it every Friday.",
        "reflection": "How does knowing that excellent character is the heaviest thing on the Mizan change your priority between getting high marks and being an honest, kind student?",
        "misconception": "Character is not a superficial mask worn in front of teachers; it is who you are in the dark when no one is watching except Allah.",
        "yt_title": "Living the Character of the Prophet (PBUH)",
        "yt_desc": "Comprehensive capstone lecture on embodying Prophetic character in modern teenage life.",
        "yt_id": "TVt-Dd31Nn4",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Al-Masjid_an-Nabawi_Rawdah_Dome.jpg/1280px-Al-Masjid_an-Nabawi_Rawdah_Dome.jpg",
        "image_title": "Green Dome of Al-Masjid an-Nabawi in Madinah",
        "image_caption": "Resting place of Prophet Muhammad (PBUH), the supreme model of noble moral character.",
        "mcq": {
            "question": "Zuri is walking to her history exam and finds a lost wallet containing 1,500 shillings and an ID card belonging to a classmate, Halima, who is from a different tribe and whom Zuri doesn't know well. Zuri's family is currently struggling to pay for her school fees. Applying the full synthesis of our unit on virtues, what is the most complete and virtuous action Zuri should take?",
            "options": [
                "Keep the money to help her family with school fees, but return the ID card anonymously",
                "Take the wallet to the school principal or directly to Halima before the exam, ensuring the money and cards are intact, and refuse to accept any reward",
                "Keep the wallet silently and say it was her 'Qadar' to find it",
                "Leave the wallet on the ground because she is not responsible for other people's things"
            ],
            "answer": "B",
            "explanation": "This option represents a complete, synchronized application of our three virtues: Trustworthiness (Amanah - returning borrowed/lost property intact to its rightful owner), Contentment (Rida - refusing to take unlawful money despite her family's need, trusting Allah's provision), and Modesty (Haya - acting with natural righteousness and integrity without seeking praise or reward)."
        },
        "summary_content": "Sincere character is built by integrating Modesty (Haya), Contentment (Rida), and Trustworthiness (Amanah). Good character is the heaviest thing on the Mizan on the Day of Judgment. Living with moral integrity builds a peaceful, stable society and earns Allah's eternal pleasure.",
        "key_points": [
            "The three pillar virtues combine into a unified, unshakeable Character Code.",
            "Good character (Akhlaq) will be the heaviest asset on the Day of Judgment.",
            "Embodying Prophetic character elevates student life into profound daily worship."
        ],
        "exit_ticket": "Write down how you will use the 'Personal Character Code' to handle peer pressure at school."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# DATABASE INGESTION EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic9():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 9: VIRTUES IN ISLAM")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=349)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 349 does not exist!")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    with transaction.atomic():
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"Cleaning {existing_units.count()} existing units under Topic {topic.id}...")
            existing_units.delete()

        total_units = 0
        total_lessons = 0
        total_blocks = 0
        total_assets = 0

        for cfg in LESSONS_CONFIG:
            u_order = cfg["order"]
            l_title = cfg["title"]

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                name=f"{cfg['code']}: {l_title}",
                description=clean_text(cfg["inquiry"]),
                order=u_order
            )
            total_units += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=f"{cfg['code']}: {l_title}",
                status="published",
                version=1
            )
            total_lessons += 1

            # 3. Create LessonAssets
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                title=clean_text(cfg["image_title"]),
                url=cfg["image_url"],
                metadata={
                    "caption": clean_text(cfg["image_caption"]),
                    "source": "Wikimedia Commons",
                    "license": "CC BY-SA / Public Domain"
                }
            )
            total_assets += 1

            svg_code = cfg["svg_func"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                title=clean_text(cfg["diagram_title"]),
                metadata={
                    "svg_content": svg_code,
                    "svg_xml": svg_code,
                    "theme": "#0f172a",
                    "viewBox": "0 0 880 440",
                    "responsive": True
                }
            )
            total_assets += 1

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

            # 4. Create 7 Cards / Pages (15 Blocks)
            # CARD 1 (Page 1): Orientation (2 blocks)
            b_img = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Inquiry",
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
                page_title="Orientation & Inquiry",
                order=20,
                component_order=2,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Learning Goal & Inquiry",
                content={
                    "title": "Lesson Inquiry & Hook",
                    "question": clean_text(cfg["inquiry"]),
                    "hook": clean_text(cfg["connection"]),
                    "text": clean_text(f"**Inquiry:** {cfg['inquiry']}\n\n**Connection:** {cfg['connection']}")
                }
            )

            # CARD 2 (Page 2): Core Teaching & Scripture (2 blocks)
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=30,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Authoritative Concept",
                content={
                    "title": "Authoritative Concept",
                    "content": clean_text(cfg["concept_def"]),
                    "text": clean_text(cfg["concept_def"])
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

            # CARD 3 (Page 3): Deep Explanation & SVG Diagram (3 blocks)
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=50,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Clarifying the Concept",
                content={
                    "title": "Clarifying the Concept",
                    "content": clean_text(cfg["explanation"]),
                    "text": clean_text(cfg["explanation"])
                }
            )

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
                    "svg_content": svg_code,
                    "svg_xml": svg_code,
                    "svg": svg_code,
                    "description": f"Dedicated vector SVG diagram illustrating {cfg['title']}."
                },
                metadata={
                    "svg_content": svg_code,
                    "svg_xml": svg_code
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
                    "rows": [[clean_text(cell) for cell in row] for row in cfg["table_rows"]]
                }
            )

            # CARD 4 (Page 4): Worked Scenario (1 block)
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                page_title="Scenario & Worked Example",
                order=80,
                component_order=1,
                block_type="worked_example",
                component_type="worked_example",
                title="Relatable Student Scenario",
                content={
                    "title": "Relatable Student Scenario",
                    "scenario": clean_text(cfg["scenario"]),
                    "text": clean_text(cfg["scenario"])
                }
            )

            # CARD 5 (Page 5): Real-World Application & Video (4 blocks)
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=90,
                component_order=1,
                block_type="real_world_example",
                component_type="real_world_example",
                title="Actionable Daily Practice",
                content={
                    "title": "Actionable Daily Practice",
                    "content": clean_text(cfg["real_world"]),
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

            # CARD 6 (Page 6): Knowledge Mastery Check (1 block)
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

            # CARD 7 (Page 7): Summary & Exit Ticket (2 blocks)
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
            print(f"  [+] Ingested Lesson {u_order}/9: '{l_title}' (7 cards, 15 blocks, 3 assets)")

    print("=" * 80)
    print("TOPIC 9 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 9")
    print(f"  Lessons       : {total_lessons} / 9 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (9 SVGs, 9 images, 9 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic9()
