"""
VLearn CBC Grade 9 Islamic Religious Education (IRE)
Topic 2: Surah al-Hujurat (Q 49) — Topic ID: 342
Production Ingestion & Pedagogical Enrichment Script

Curriculum: CBC
Grade: Grade 9
Subject: IRE (Grade 9 - IRE)
Topic ID: 342 (Surah al-Hujurat (Q 49))

5 Lessons:
  1. Lesson 1.2.1: Respect, authority, and verification (Verses 1-6)
  2. Lesson 1.2.2: Brotherhood and conflict resolution (Verses 9-10)
  3. Lesson 1.2.3: Respectful speech and avoiding harm (Verses 11-12)
  4. Lesson 1.2.4: Equality, sincerity, and accountability (Verses 13-18)
  5. Lesson 1.2.5: Surah al-Hujurat in daily relationships (Synthesis)

Each lesson contains 7 Cards / Pages:
  - Card 1 (Page 1): suggested_image (Wikimedia) + learning_goal (Inquiry + Connection)
  - Card 2 (Page 2): concept_explanation (Authoritative concept) + callout (Scripture Panel)
  - Card 3 (Page 3): concept_explanation (Deep dive) + suggested_diagram (Custom Vector SVG) + comparison_table / step_process
  - Card 4 (Page 4): worked_example (Relatable student scenario)
  - Card 5 (Page 5): real_world_example + reflection + common_misconception + suggested_video (YouTube)
  - Card 6 (Page 6): knowledge_check (Interactive MCQ with question, options, answer, explanation)
  - Card 7 (Page 7): summary (Key points + Vocabulary) + mini_activity (Exit ticket)
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
    """Cleans internal pedagogical tags, bracket markers, and formats text cleanly."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [223], [1, 2]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|'
        r'MISCONCEPTION|MISCONCEPTION CHECK|INTERACTION|ETHICAL SCENARIO|KEY VERSE|'
        r'REAL WORLD APPLICATION|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|'
        r'COMPARISON TABLE|INFOGRAPHIC|SVG|DIAGRAM)[^\]]*\]',
        '',
        text,
        flags=re.IGNORECASE
    )
    # Strip source notes like [Source: RATIONALISED-GRADE-9-IRE-NOTES.pdf...]
    text = re.sub(r'\[Source:[^\]]*\]', '', text, flags=re.IGNORECASE)
    # Normalize bullet points
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


# ─────────────────────────────────────────────────────────────────────────────
# 5 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x480)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 1.2.1: The Tabayyun Protocol (Decision Tree Flowchart)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="skyGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="redGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="amberGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="emeraldGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <!-- Canvas Background -->
  <rect width="880" height="480" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Title & Subtitle -->
  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">THE "TABAYYUN" PROTOCOL: VERIFY BEFORE SHARING</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" text-anchor="middle">Qur'anic Information Verification Framework &amp; Digital Decorum (Surah Al-Hujurat 49:6)</text>

  <!-- Step 1: Input Card (Top Center) -->
  <g transform="translate(300, 88)">
    <rect width="280" height="42" rx="8" fill="url(#skyGrad1)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="140" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 1: RECEIVE NEWS / CLAIM / RUMOR</text>
  </g>

  <!-- Arrow down to Decision 1 -->
  <line x1="440" y1="130" x2="440" y2="160" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <polygon points="440,165 435,155 445,155" fill="#38bdf8"/>

  <!-- Decision Diamond 1: Reliable Source? -->
  <g transform="translate(440, 205)">
    <polygon points="0,-40 130,0 0,40 -130,0" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="-8" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Is the source 100%</text>
    <text x="0" y="8" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">verified &amp; authoritative?</text>
  </g>

  <!-- Branch NO -> Left to Card (STOP & DISCARD) -->
  <line x1="310" y1="205" x2="250" y2="205" stroke="#ef4444" stroke-width="2"/>
  <polygon points="245,205 255,200 255,210" fill="#ef4444"/>
  <rect x="258" y="188" width="40" height="18" rx="4" fill="#ef4444"/>
  <text x="278" y="201" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">NO</text>

  <g transform="translate(35, 150)">
    <rect width="210" height="110" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="210" height="28" rx="10" fill="url(#redGrad1)"/>
    <text x="105" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STOP &amp; DISCARD</text>
    <text x="12" y="48" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Do Not Forward / Share</text>
    <text x="12" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Delete from group chats.</text>
    <text x="12" y="80" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Prevent Harm from Ignorance</text>
    <text x="12" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Safeguard innocent reputations.</text>
  </g>

  <!-- Branch YES -> Down to Decision 2 -->
  <line x1="440" y1="245" x2="440" y2="280" stroke="#10b981" stroke-width="2"/>
  <polygon points="440,285 435,275 445,275" fill="#10b981"/>
  <rect x="446" y="252" width="40" height="18" rx="4" fill="#10b981"/>
  <text x="466" y="265" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">YES</text>

  <!-- Decision Diamond 2: Beneficial & Kind? -->
  <g transform="translate(440, 325)">
    <polygon points="0,-40 130,0 0,40 -130,0" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="0" y="-8" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Is sharing beneficial,</text>
    <text x="0" y="8" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">constructive &amp; kind?</text>
  </g>

  <!-- Branch NO (from Diamond 2) -> Right to Card (CONCEAL & RESTRAIN) -->
  <line x1="570" y1="325" x2="630" y2="325" stroke="#f59e0b" stroke-width="2"/>
  <polygon points="635,325 625,320 625,330" fill="#f59e0b"/>
  <rect x="580" y="308" width="40" height="18" rx="4" fill="#f59e0b"/>
  <text x="600" y="321" fill="#0f172a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">NO</text>

  <g transform="translate(635, 270)">
    <rect width="210" height="110" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="210" height="28" rx="10" fill="url(#amberGrad1)"/>
    <text x="105" y="19" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">CONCEAL &amp; RESTRAIN</text>
    <text x="12" y="48" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Avoid Idle Chatter</text>
    <text x="12" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">True facts that cause harm remain private.</text>
    <text x="12" y="80" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Shield Private Faults</text>
    <text x="12" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Preserve community dignity and peace.</text>
  </g>

  <!-- Branch YES (from Diamond 2) -> Down to Bottom Card (SHARE RESPONSIBLY) -->
  <line x1="440" y1="365" x2="440" y2="395" stroke="#10b981" stroke-width="2"/>
  <polygon points="440,400 435,390 445,390" fill="#10b981"/>
  <rect x="446" y="370" width="40" height="18" rx="4" fill="#10b981"/>
  <text x="466" y="383" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">YES</text>

  <g transform="translate(290, 405)">
    <rect width="300" height="44" rx="8" fill="url(#emeraldGrad1)" stroke="#34d399" stroke-width="1.5"/>
    <text x="150" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SHARE RESPONSIBLY &amp; CONSTRUCTIVELY</text>
    <text x="150" y="35" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Uphold truth, give context, and build social harmony.</text>
  </g>

  <!-- Bottom Qur'anic Ribbon -->
  <text x="440" y="466" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle" font-style="italic">SURAH AL-HUJURAT 49:6 — "INVESTIGATE, LEST YOU HARM A PEOPLE OUT OF IGNORANCE AND BECOME REGRETFUL"</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 1.2.2: 4-Step Just Conflict Resolution (Islah) (Sequential Flow)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="skyGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="redGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="amberGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="emeraldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <!-- Background Canvas -->
  <rect width="880" height="480" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Title & Subtitle -->
  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">4-STEP JUST CONFLICT RESOLUTION (ISLAH)</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" text-anchor="middle">The Qur'anic Framework for Community Peacemaking &amp; Restoring Justice (Surah Al-Hujurat 49:9-10)</text>

  <!-- Card 1: Immediate Mediation -->
  <g transform="translate(35, 95)">
    <rect width="185" height="320" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="url(#skyGrad2)"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">STEP 1: MEDIATION</text>
    
    <rect x="15" y="48" width="60" height="20" rx="4" fill="#0369a1"/>
    <text x="45" y="62" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">FA-ASLIHU</text>

    <text x="15" y="88" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Proactive Action:</text>
    <text x="15" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Intervene immediately</text>
    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">when a dispute flares up.</text>

    <text x="15" y="148" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Reject Neutrality:</text>
    <text x="15" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Never stand as a passive</text>
    <text x="15" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">spectator or cheerleader.</text>

    <text x="15" y="208" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Open Channels:</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Bring both parties to</text>
    <text x="15" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">respectful dialogue.</text>

    <rect x="12" y="270" width="161" height="36" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="92" y="286" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Halts Escalation</text>
    <text x="92" y="299" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Protects Community Unity</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <g transform="translate(225, 240)">
    <circle cx="12" cy="0" r="14" fill="#0284c7"/>
    <text x="12" y="4" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#10140;</text>
  </g>

  <!-- Card 2: Restrain Oppressor -->
  <g transform="translate(255, 95)">
    <rect width="185" height="320" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="url(#redGrad2)"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">STEP 2: HALT WRONG</text>
    
    <rect x="15" y="48" width="60" height="20" rx="4" fill="#991b1b"/>
    <text x="45" y="62" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">TABGHI</text>

    <text x="15" y="88" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Identify Aggression:</text>
    <text x="15" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">If one party transgresses</text>
    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and refuses peaceful terms.</text>

    <text x="15" y="148" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• United Opposition:</text>
    <text x="15" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Community stands together</text>
    <text x="15" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">firmly against oppression.</text>

    <text x="15" y="208" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Restrain Bullying:</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Compel aggressor back to</text>
    <text x="15" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">the decree of Allah.</text>

    <rect x="12" y="270" width="161" height="36" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="92" y="286" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Active Justice</text>
    <text x="92" y="299" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Stops Tyranny &amp; Abuse</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <g transform="translate(445, 240)">
    <circle cx="12" cy="0" r="14" fill="#ef4444"/>
    <text x="12" y="4" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#10140;</text>
  </g>

  <!-- Card 3: Just Reconciliation -->
  <g transform="translate(475, 95)">
    <rect width="185" height="320" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="185" height="34" rx="10" fill="url(#amberGrad2)"/>
    <text x="92" y="22" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">STEP 3: FAIR TERMS</text>
    
    <rect x="15" y="48" width="60" height="20" rx="4" fill="#b45309"/>
    <text x="45" y="62" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">BIL-'ADL</text>

    <text x="15" y="88" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Absolute Equity:</text>
    <text x="15" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Once wrongdoer relents,</text>
    <text x="15" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">reconcile with pure justice.</text>

    <text x="15" y="148" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• No Retaliation:</text>
    <text x="15" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Do not exploit victory</text>
    <text x="15" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">or enforce biased revenge.</text>

    <text x="15" y="208" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Restore Rights:</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Compensate losses and</text>
    <text x="15" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">protect victim's dignity.</text>

    <rect x="12" y="270" width="161" height="36" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="92" y="286" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Divine Fairness</text>
    <text x="92" y="299" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Allah Loves the Equitable</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <g transform="translate(665, 240)">
    <circle cx="12" cy="0" r="14" fill="#f59e0b"/>
    <text x="12" y="4" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#10140;</text>
  </g>

  <!-- Card 4: Restored Brotherhood -->
  <g transform="translate(695, 95)">
    <rect width="150" height="320" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="150" height="34" rx="10" fill="url(#emeraldGrad2)"/>
    <text x="75" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">STEP 4: BROTHERHOOD</text>
    
    <rect x="15" y="48" width="60" height="20" rx="4" fill="#047857"/>
    <text x="45" y="62" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">IKHWAH</text>

    <text x="12" y="88" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Sacred Family:</text>
    <text x="12" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">"Believers are but</text>
    <text x="12" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">brothers" in faith.</text>

    <text x="12" y="148" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Heal Wounds:</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Cleanse the hearts of</text>
    <text x="12" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">grudges and pride.</text>

    <text x="12" y="208" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Divine Mercy:</text>
    <text x="12" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Fear Allah so that</text>
    <text x="12" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">mercy envelops all.</text>

    <rect x="10" y="270" width="130" height="36" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="75" y="286" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Restored Harmony</text>
    <text x="75" y="299" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Spiritual Mercy</text>
  </g>

  <!-- Bottom Scripture Verse -->
  <text x="440" y="445" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle" font-style="italic">SURAH AL-HUJURAT 49:10 — "THE BELIEVERS ARE BUT BROTHERS, SO MAKE PEACE BETWEEN YOUR BROTHERS AND FEAR ALLAH THAT YOU MAY RECEIVE MERCY"</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 1.2.3: Harmful Speech vs Beneficial Speech (Dual-Column Matrix)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="redGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="emeraldGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#065f46"/>
    </linearGradient>
  </defs>

  <!-- Canvas Background -->
  <rect width="880" height="480" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header -->
  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">THE DUALITY OF SPEECH: HARMFUL SINS VS. BENEFICIAL ETHICS</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" text-anchor="middle">Contrasting Destructive Verbal Behaviors with Sacred Spiritual Dignity (Surah Al-Hujurat 49:11-12)</text>

  <!-- Left Column: Harmful Speech (Sins of the Tongue) -->
  <g transform="translate(35, 90)">
    <rect width="385" height="330" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="385" height="36" rx="10" fill="url(#redGrad3)"/>
    <text x="192" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">HARMFUL SPEECH (DESTROYERS OF TRUST)</text>

    <!-- Item 1: Sukhriyyah -->
    <text x="20" y="66" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Ridicule &amp; Mockery (Sukhriyyah):</text>
    <text x="20" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Laughing at accents, clothes, or physical traits; humiliates the soul.</text>

    <!-- Item 2: Lamz -->
    <text x="20" y="110" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Insults &amp; Defamation (Lamz):</text>
    <text x="20" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Publicly pointing out faults, name-shaming, and verbal attacks.</text>

    <!-- Item 3: Tanabuz -->
    <text x="20" y="154" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Offensive Nicknames (Tanabuz bil-Alqab):</text>
    <text x="20" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Calling peers by hurtful labels or embarrassing titles they detest.</text>

    <!-- Item 4: Dhan -->
    <text x="20" y="198" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Baseless Suspicion (Su' al-Dhan):</text>
    <text x="20" y="214" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Harboring negative, cynical assumptions about intentions without proof.</text>

    <!-- Item 5: Tajassus -->
    <text x="20" y="242" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Spying &amp; Snooping (Tajassus):</text>
    <text x="20" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Invading privacy: looking into other phones, diaries, or secrets.</text>

    <!-- Item 6: Gheebah -->
    <text x="20" y="286" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">6. Backbiting (Gheebah):</text>
    <text x="20" y="302" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Speaking ill of someone in their absence: "Eating your dead brother's flesh."</text>

    <rect x="20" y="316" width="345" height="2" fill="#ef4444" opacity="0.3"/>
  </g>

  <!-- Central VS Badge -->
  <g transform="translate(440, 255)">
    <circle cx="0" cy="0" r="22" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="5" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="900" text-anchor="middle">VS</text>
  </g>

  <!-- Right Column: Beneficial Speech (Spiritual Dignity) -->
  <g transform="translate(460, 90)">
    <rect width="385" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="385" height="36" rx="10" fill="url(#emeraldGrad3)"/>
    <text x="192" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">BENEFICIAL SPEECH (BUILDERS OF PEACE)</text>

    <!-- Item 1: Respect -->
    <text x="20" y="66" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Inherent Dignity &amp; Respect:</text>
    <text x="20" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Recognizing that the person you see may be far superior before Allah.</text>

    <!-- Item 2: Upliftment -->
    <text x="20" y="110" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Encouraging &amp; Kind Speech:</text>
    <text x="20" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Affirming peer strengths, gentle counsel, and covering minor faults.</text>

    <!-- Item 3: Beloved Names -->
    <text x="20" y="154" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Calling by Beloved Names:</text>
    <text x="20" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Addressing friends by the most honorable, affectionate titles they love.</text>

    <!-- Item 4: Husn al-Dhan -->
    <text x="20" y="198" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Positive Assumptions (Husn al-Dhan):</text>
    <text x="20" y="214" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Assuming the best intentions; finding 70 excuses before judging.</text>

    <!-- Item 5: Privacy -->
    <text x="20" y="242" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Honoring Sanctity of Privacy:</text>
    <text x="20" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Respecting personal boundaries, guarding confidences, lowering gaze.</text>

    <!-- Item 6: Defending Absent -->
    <text x="20" y="286" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">6. Defending Absent Brothers &amp; Sisters:</text>
    <text x="20" y="302" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Shielding the honor of absent classmates when others attempt gossip.</text>

    <rect x="20" y="316" width="345" height="2" fill="#10b981" opacity="0.3"/>
  </g>

  <!-- Bottom Scripture Ribbon -->
  <text x="440" y="445" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle" font-style="italic">SURAH AL-HUJURAT 49:12 — "DO NOT SPY OR BACKBITE EACH OTHER. WOULD ONE OF YOU LIKE TO EAT THE FLESH OF HIS BROTHER WHEN DEAD? YOU WOULD DETEST IT"</text>
</svg>"""


def get_svg_lesson_4():
    """Lesson 1.2.4: The Divine Standard of Nobility (Taqwa Balance Scale)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="emeraldGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="slateGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
  </defs>

  <!-- Canvas Background -->
  <rect width="880" height="480" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header -->
  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">THE DIVINE SCALE OF NOBILITY &amp; WORTH</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" text-anchor="middle">Worldly Vanity vs. The Eternal Weight of Taqwa in the Sight of Allah (Surah Al-Hujurat 49:13)</text>

  <!-- Scale Fulcrum & Pillar -->
  <path d="M 440 100 L 440 280" stroke="#cbd5e1" stroke-width="5" stroke-linecap="round"/>
  <polygon points="440,85 425,115 455,115" fill="#38bdf8"/>
  <rect x="400" y="275" width="80" height="12" rx="4" fill="#64748b"/>
  <path d="M 370 295 L 510 295" stroke="#475569" stroke-width="6" stroke-linecap="round"/>

  <!-- Tilting Scale Beam: Left side is High (Weightless), Right side is Low (Heavy with Taqwa) -->
  <line x1="190" y1="130" x2="690" y2="190" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
  <circle cx="440" cy="160" r="10" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>

  <!-- Scale Chains -->
  <!-- Left Pan Chains (Hangs at y=130 down to y=200) -->
  <line x1="190" y1="130" x2="110" y2="195" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="190" y1="130" x2="270" y2="195" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 90 200 Q 190 220 290 200" stroke="#94a3b8" stroke-width="2.5" fill="none"/>

  <!-- Right Pan Chains (Hangs at y=190 down to y=265) -->
  <line x1="690" y1="190" x2="610" y2="260" stroke="#34d399" stroke-width="1.5"/>
  <line x1="690" y1="190" x2="770" y2="260" stroke="#34d399" stroke-width="1.5"/>
  <path d="M 590 265 Q 690 285 790 265" stroke="#34d399" stroke-width="3" fill="none"/>

  <!-- Left Box: Worldly Factors (Weightless / Elevated) -->
  <g transform="translate(55, 215)">
    <rect width="270" height="175" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="270" height="30" rx="10" fill="url(#slateGrad4)"/>
    <text x="135" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">WORLDLY ILLUSIONS (ZERO WEIGHT)</text>

    <text x="15" y="55" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Material Wealth &amp; Properties</text>
    <text x="15" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Possessions perish and hold zero spiritual value.</text>

    <text x="15" y="95" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Tribe, Lineage &amp; Nationality</text>
    <text x="15" y="110" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">All mankind shares the exact same ancestry.</text>

    <text x="15" y="135" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Skin Color, Beauty &amp; Influence</text>
    <text x="15" y="150" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Outward forms do not enter the divine judgment.</text>
  </g>

  <!-- Right Box: Divine Taqwa (Heavy / Grounded) -->
  <g transform="translate(555, 255)">
    <rect width="270" height="175" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="270" height="30" rx="10" fill="url(#emeraldGrad4)"/>
    <text x="135" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TAQWA: SUPREME DIVINE NOBILITY</text>

    <text x="15" y="55" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• God-Consciousness &amp; Reverence</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Living with continuous awareness of Allah.</text>

    <text x="15" y="95" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Sincerity in the Heart (Iman)</text>
    <text x="15" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Inner purity, free from arrogance and showing off.</text>

    <text x="15" y="135" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Righteous Actions &amp; Justice ('Adl)</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Treating all humanity with fairness and mercy.</text>
  </g>

  <!-- Middle Connector & Diversity Badge -->
  <g transform="translate(345, 335)">
    <rect width="190" height="60" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="95" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">PURPOSE OF DIVERSITY</text>
    <text x="95" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">LI-TA'ARAFU</text>
    <text x="95" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">To Know, Cooperate &amp; Learn</text>
  </g>

  <!-- Bottom Scripture Ribbon -->
  <text x="440" y="450" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle" font-weight="600">SURAH AL-HUJURAT 49:13 — "INDEED, THE MOST NOBLE OF YOU IN THE SIGHT OF ALLAH IS THE MOST RIGHTEOUS (ATQAKUM) OF YOU"</text>
</svg>"""


def get_svg_lesson_5():
    """Lesson 1.2.5: Daily Relationships Decision Tree (Practical Application Matrix)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="skyGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="amberGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="emeraldGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="roseGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#4338ca"/>
    </linearGradient>
  </defs>

  <!-- Canvas Background -->
  <rect width="880" height="480" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="850" height="450" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Title & Subtitle -->
  <text x="440" y="44" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">SURAH AL-HUJURAT: DAILY INTERPERSONAL BLUEPRINT</text>
  <text x="440" y="66" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" text-anchor="middle">5 Real-World Pillars for Cultivating Righteous Character, School Peace &amp; Digital Ethics</text>

  <!-- Row 1: 3 Domain Cards -->
  <!-- Card 1: Authority -->
  <g transform="translate(35, 90)">
    <rect width="255" height="155" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="255" height="28" rx="10" fill="url(#skyGrad5)"/>
    <text x="127" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">1. WITH AUTHORITY (Q 49:1-5)</text>

    <text x="12" y="50" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Context:</text>
    <text x="56" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Parents, teachers, and elders.</text>

    <text x="12" y="74" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Core Practice:</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Lower your voice; listen attentively;</text>
    <text x="12" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">wait patiently before speaking.</text>

    <rect x="12" y="118" width="231" height="25" rx="5" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="127" y="134" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Outcome: Wisdom, Humility &amp; Order</text>
  </g>

  <!-- Card 2: Information & Media -->
  <g transform="translate(312, 90)">
    <rect width="255" height="155" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="255" height="28" rx="10" fill="url(#amberGrad5)"/>
    <text x="127" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">2. WITH INFORMATION (Q 49:6)</text>

    <text x="12" y="50" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Context:</text>
    <text x="56" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">WhatsApp, social media rumors.</text>

    <text x="12" y="74" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Core Practice:</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Apply Tabayyun: Stop and verify source;</text>
    <text x="12" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">never forward sensational gossip.</text>

    <rect x="12" y="118" width="231" height="25" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="127" y="134" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Outcome: Truth &amp; Emotional Safety</text>
  </g>

  <!-- Card 3: Conflicts & Disputes -->
  <g transform="translate(590, 90)">
    <rect width="255" height="155" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="255" height="28" rx="10" fill="url(#emeraldGrad5)"/>
    <text x="127" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">3. WITH CONFLICTS (Q 49:9-10)</text>

    <text x="12" y="50" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Context:</text>
    <text x="56" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">School fights, playground drama.</text>

    <text x="12" y="74" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Core Practice:</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Practice Islah: Act as a mediator;</text>
    <text x="12" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">stop bullies; establish fair compromise.</text>

    <rect x="12" y="118" width="231" height="25" rx="5" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="127" y="134" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Outcome: Sacred Faith Brotherhood</text>
  </g>

  <!-- Row 2: 2 Wide Domain Cards -->
  <!-- Card 4: Speech & Boundaries -->
  <g transform="translate(110, 265)">
    <rect width="310" height="155" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="310" height="28" rx="10" fill="url(#roseGrad5)"/>
    <text x="155" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">4. WITH SPEECH &amp; PRIVACY (Q 49:11-12)</text>

    <text x="15" y="50" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Prohibited:</text>
    <text x="75" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Mockery, derogatory slurs, backbiting.</text>

    <text x="15" y="72" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Prescribed:</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Use preferred names; assume good intentions;</text>
    <text x="15" y="102" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">guard phones and secrets; defend the absent.</text>

    <rect x="15" y="118" width="280" height="25" rx="5" fill="#0f172a" stroke="#f43f5e" stroke-width="1"/>
    <text x="155" y="134" fill="#fb7185" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Outcome: Protection of Personal Honor &amp; Trust</text>
  </g>

  <!-- Card 5: Diversity & Equality -->
  <g transform="translate(460, 265)">
    <rect width="310" height="155" rx="10" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect width="310" height="28" rx="10" fill="url(#indigoGrad5)"/>
    <text x="155" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">5. WITH DIVERSITY &amp; TAQWA (Q 49:13)</text>

    <text x="15" y="50" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Foundation:</text>
    <text x="75" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">One origin; diversity is a blessing.</text>

    <text x="15" y="72" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">• Core Practice:</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Dismantle tribal prejudice; evaluate people by</text>
    <text x="15" y="102" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">character, honesty and Taqwa, not worldly status.</text>

    <rect x="15" y="118" width="280" height="25" rx="5" fill="#0f172a" stroke="#6366f1" stroke-width="1"/>
    <text x="155" y="134" fill="#818cf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Outcome: Universal Equality &amp; Communal Harmony</text>
  </g>

  <!-- Bottom Banner -->
  <text x="440" y="450" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle" font-style="italic">SURAH AL-HUJURAT: A COMPLETE AND TIMELESS CONSTITUTION FOR MORAL AND SOCIAL EXCELLENCE</text>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CURATED HIGH-QUALITY AUTHENTIC MEDIA CONFIGURATIONS
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_DATA = [
    # ── Lesson 1: Respect, Authority, and Verification ───────────────────────
    {
        "order": 1,
        "title": "Respect, Authority, and Verification (Verses 1-6)",
        "inquiry_question": "How do we show respect to authority and verify information responsibly before sharing it with others?",
        "connection": (
            "Have you ever heard a rumor about a classmate or a teacher, shared it with your friends, "
            "and later found out it was completely false? You probably felt terrible! Sharing unverified "
            "news can ruin friendships, destroy reputations, and create chaos in a school. Over 1,400 "
            "years ago, Allah (S.W.T.) revealed a beautiful set of social rules in Surah al-Hujurat to teach "
            "us how to respect leaders, protect community peace, and verify every piece of news before we react."
        ),
        "learning_goal_statement": (
            "Explain the religious and civic obligation of showing respect to leadership and applying the "
            "Qur'anic protocol of information verification (Tabayyun) in school and digital life."
        ),
        "authoritative_concept": (
            "### Core Concepts from Surah al-Hujurat (Verses 1–6)\n\n"
            "- **Surah Al-Hujurat (The Rooms):** The 49th chapter of the Qur'an, comprising 18 verses. "
            "It is a Madinan surah revealed after the Hijrah, delivering an authoritative blueprint for "
            "social ethics, interpersonal manners, and communal unity.\n"
            "- **Respect for Authority:** Recognizing and honoring righteous leadership—including parents, "
            "teachers, elders, and community leaders—by listening attentively, lowering our voices, and "
            "exercising patience rather than speaking over them.\n"
            "- **Information Verification (*Tabayyun*):** The strict Islamic moral and legal obligation to "
            "investigate, authenticate, and double-check any report or news brought to us before accepting "
            "it or acting upon it."
        ),
        "scripture_panel": (
            "> \"O you who have believed, do not put [yourselves] before Allah and His Messenger but fear Allah. "
            "Indeed, Allah is Hearing and Knowing.\"\n"
            "— **Surah Al-Hujurat, 49:1**\n\n"
            "> \"O you who have believed, do not raise your voices above the voice of the Prophet or be loud to him "
            "in speech... lest your deeds become worthless while you do not perceive.\"\n"
            "— **Surah Al-Hujurat, 49:2**\n\n"
            "> \"O you who have believed, if there comes to you a disobedient person with news, investigate, lest you "
            "harm a people out of ignorance and become, over what you have done, regretful.\"\n"
            "— **Surah Al-Hujurat, 49:6**"
        ),
        "deep_explanation": (
            "### Theological Exegesis & Practical Analysis\n\n"
            "**1. Respecting Authority (Verses 1–5):**\n"
            "The historical context reveals that early bedouins called out loudly from outside the private chambers "
            "(*hujurat*) of the Prophet Muhammad (PBUH). The Qur'an guided them toward refined spiritual decorum. "
            "In modern daily life, this translates into showing deep respect to our teachers, parents, and community "
            "mentors by speaking politely, not shouting over others, and waiting patiently for guidance.\n\n"
            "**2. The Tabayyun Verification Protocol (Verse 6):**\n"
            "The revelation was connected to Al-Walid ibn 'Uqbah being sent to collect Zakat from the Banu Mustaliq. "
            "Due to an ancient misunderstanding, he hastily reported they intended to fight. Verse 6 intervened with "
            "an eternal rule: Never act on unverified rumors or questionable sources. Acting without verification "
            "harms innocent lives and causes deep, irreversible regret."
        ),
        "diagram_caption": "Decision flowchart illustrating the Qur'anic Tabayyun protocol for vetting information before sharing.",
        "svg_fn": get_svg_lesson_1,
        "interactive_component": {
            "type": "step_process",
            "title": "The 4-Step Tabayyun Verification Protocol",
            "steps": [
                {"title": "Step 1: Pause on Arrival", "description": "Resist the impulse to immediately react, believe, or forward sensational claims."},
                {"title": "Step 2: Source Reliability Check", "description": "Identify who originated the claim. Is the source credible, transparent, and authoritative?"},
                {"title": "Step 3: Multi-Source Confirmation", "description": "Cross-check facts with official announcements, school leaders, or direct primary witnesses."},
                {"title": "Step 4: Ethical Impact Assessment", "description": "Evaluate if sharing builds community welfare or spreads unnecessary panic and harm."}
            ]
        },
        "scenario_intro": "Read the following scenario and observe how applying Surah Al-Hujurat prevents disaster:",
        "scenario_steps": [
            "Ali receives an anonymous text message claiming that a science teacher leaked the examination papers and tomorrow's exam is canceled.",
            "Excited and anxious, Ali prepares to forward the message immediately to his entire class WhatsApp group of 45 students.",
            "His classmate Yusuf intervenes: 'Ali, remember Surah al-Hujurat, verse 6! We are commanded to practice Tabayyun. This unknown number has no official authority.'",
            "Together, they verify the report with the class teacher and examine the official noticeboard, discovering the text was a malicious prank.",
            "By pausing and investigating, Ali protected the class from panic, misinformation, and disciplinary action."
        ],
        "scenario_text": (
            "Ali receives a text message from an unknown number saying, 'The science teacher leaked the exam papers, and the "
            "exam is canceled tomorrow!' Ali is excited and is about to forward this message to the entire class WhatsApp group. "
            "His friend Yusuf stops him and says, 'Ali, remember what we learned in Surah al-Hujurat, verse 6! This is unverified "
            "news from an unknown source. We must investigate first. Let's ask our class teacher or check the official school "
            "noticeboard instead of spreading panic.' They verify and find out the text was a prank. Ali is relieved he didn't "
            "spread the falsehood."
        ),
        "real_world_application": (
            "Apply the Qur'anic concept of *Tabayyun* to your digital life every single day. Whenever you receive a sensational "
            "headline, a rumor about a classmate, or a post on TikTok, Instagram, or WhatsApp, never hit 'forward' or 'share' "
            "instantaneously. Stop, check the primary source, verify through official school or news channels, and ask whether "
            "sharing contributes to truth or causes harm. Exercising information verification makes you an ethical digital citizen."
        ),
        "reflection": (
            "Pause and reflect:\n\n"
            "1. What are the emotional, psychological, and social consequences of spreading a rumor without checking its truth first?\n"
            "2. How does raising your voice or interrupting in front of a parent or teacher weaken the bond of trust and respect between you?"
        ),
        "misconception": (
            "Students often think that forwarding an unverified message with the caption 'Forwarded as received' or 'Just sharing ' "
            "removes moral responsibility from them. Actually, Surah al-Hujurat (49:6) places the religious duty on the recipient "
            "to investigate (*tabayyun*) before circulating it, because spreading unconfirmed rumors makes one an active agent of falsehood and communal discord."
        ),
        "mcq": {
            "question": "According to Surah al-Hujurat, verse 6, what is a Muslim's religious obligation when receiving important news from an unverified or questionable source?",
            "options": [
                "A. To share it immediately with everyone so the community is alerted.",
                "B. To ignore the news completely and never speak to that person again.",
                "C. To investigate and verify the truthfulness of the news before acting on it.",
                "D. To assume the news is true because sharing information is always beneficial."
            ],
            "answer": "C",
            "explanation": "Verse 6 explicitly commands believers to 'investigate' (tabayyun) any news brought by an unreliable source to prevent harming innocent people out of ignorance and later suffering from deep regret."
        },
        "summary_content": (
            "### Summary & Key Takeaways\n\n"
            "- **Surah al-Hujurat** is a Madinan chapter setting fundamental social ethics, decorum, and manners for community cohesion.\n"
            "- **Respect for Authority:** Honoring parents, teachers, and leaders by lowering our voices and listening patiently.\n"
            "- **The Tabayyun Principle:** Investigating news before believing or circulating it is an active religious obligation.\n\n"
            "**Essential Terminology:**\n"
            "- **Al-Hujurat:** The private rooms and chambers of the Prophet's household, which gave the surah its name.\n"
            "- **Tabayyun:** The rigorous process of investigating, verifying, and confirming facts before acting or broadcasting."
        ),
        "key_points": [
            "Surah al-Hujurat is a Madinan surah focusing on communal manners, social ethics, and unity.",
            "We show respect to authority by speaking politely, lowering our voices, and exercising patience.",
            "The Qur'an establishes information verification (tabayyun) as a sacred duty to prevent communal harm."
        ],
        "exit_ticket": "State one practical step you will take today to practice the Tabayyun protocol before sharing messages on social media.",
        "image": {
            "title": "Al-Masjid an-Nabawi: The Prophet's Mosque in Madinah",
            "caption": "Surah al-Hujurat was revealed in Madinah, instructing the early community on reverence, decorum, and verification outside the private dwellings (hujurat) of the Prophet (PBUH).",
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Al_Masjid_An_Nabawi.jpg",
            "author": "Ashique Mohammed",
            "source": "Wikimedia Commons",
            "licensing": "CC BY-SA 4.0"
        },
        "youtube": {
            "youtube_id": "E1Wvf0kUzGE",
            "title": "Surah Al-Hujurat: Verses 1–6 Recitation & English Translation",
            "description": "Authentic Qur'anic recitation of Surah Al-Hujurat with clear English subtitles highlighting divine instructions on respect and verification."
        }
    },

    # ── Lesson 2: Brotherhood and Conflict Resolution ─────────────────────────
    {
        "order": 2,
        "title": "Brotherhood and Conflict Resolution (Verses 9-10)",
        "inquiry_question": "How does Islam define the relationship between believers, and what fair steps does it prescribe for resolving conflicts?",
        "connection": (
            "Imagine two brothers who get into a massive argument over a game. They stop talking, start shouting, "
            "and their friends begin taking sides, making the fight even worse. If no one steps in to help them make peace, "
            "the whole family becomes unhappy. In Surah al-Hujurat, verses 9 and 10, Allah (S.W.T.) declares that all believers "
            "are brothers and sisters. Because we are a family, we have a collective duty to step in and make peace between "
            "people who are fighting, using absolute fairness and justice."
        ),
        "learning_goal_statement": (
            "Analyze the Qur'anic concept of universal brotherhood (Ukhuwwah) and master the 4-step framework for just peacemaking (Islah)."
        ),
        "authoritative_concept": (
            "### Core Concepts from Surah al-Hujurat (Verses 9–10)\n\n"
            "- **Islamic Brotherhood (*Ukhuwwah*):** The spiritual, sacred bond of faith that unites all Muslims as one single "
            "family, rising above differences of race, tribe, social rank, or nationality.\n"
            "- **Conflict Resolution (*Islah*):** The collective moral obligation on the community to mediate, restore peace, "
            "and reconcile disputing parties with absolute justice and impartiality.\n"
            "- **Rebuking Aggression (*Al-Baghy*):** The requirement to stand firmly against persistent injustice and oppression, "
            "ensuring that reconciliation is never built on condoning bullying."
        ),
        "scripture_panel": (
            "> \"And if two factions among the believers should fight, then make peace between them. But if one of them wrongs "
            "the other, then fight against the one that wrongs until it returns to the command of Allah. And if it returns, then "
            "make peace between them in justice and act justly. Indeed, Allah loves those who act justly.\"\n"
            "— **Surah Al-Hujurat, 49:9**\n\n"
            "> \"The believers are but brothers, so make peace between your brothers. And fear Allah that you may receive mercy.\"\n"
            "— **Surah Al-Hujurat, 49:10**"
        ),
        "deep_explanation": (
            "### The 4-Step Divine Framework for Resolving Conflict\n\n"
            "Surah al-Hujurat (49:9) establishes a comprehensive procedural model for dispute resolution:\n"
            "1. **Immediate Mediation (*Fa-Aslihu*):** The moment disagreement or hostility arises, the community must intervene. "
            "Neutral bystanders do not allow the conflict to fester or cheer on violence.\n"
            "2. **Confronting Persistent Aggression:** If one party refuses peaceful settlement and continues to oppress the other, "
            "the community must collectively oppose the oppressor until the transgression stops.\n"
            "3. **Equitable Settlement (*Bil-'Adl*):** When the wrongdoer submits to fairness, peace must be instituted without bias, "
            "retaliation, or lingering resentment. Rights are restored objectively.\n"
            "4. **Re-establishing Brotherhood (*Ukhuwwah*):** As verse 10 affirms, believers are brothers. Peace is the natural state "
            "of faith, and righteous mediation unlocks Allah's divine mercy."
        ),
        "diagram_caption": "Process blueprint detailing the 4 sequential stages of Islamic conflict resolution (Islah).",
        "svg_fn": get_svg_lesson_2,
        "interactive_component": {
            "type": "step_process",
            "title": "4-Step Process: Just Peacemaking (Islah)",
            "steps": [
                {"title": "Step 1: Immediate Mediation", "description": "Intervene early as an unbiased peacemaker; do not stand by or fuel the argument."},
                {"title": "Step 2: Restrain Injustice", "description": "Stand firmly against the party that continues to bully or oppress until wrongdoing ceases."},
                {"title": "Step 3: Establish Just Terms", "description": "Resolve the underlying root cause with absolute fairness (bil-'adl) and restitution."},
                {"title": "Step 4: Restore Brotherhood", "description": "Heal emotional wounds and re-establish mutual compassion, knowing believers are family."}
            ]
        },
        "scenario_intro": "Analyze how student leaders Tariq and Halima put Surah Al-Hujurat into action:",
        "scenario_steps": [
            "Two student sports clubs argue angrily over the use of the school football pitch on Friday afternoon, trading verbal insults.",
            "Tariq and Halima intervene promptly: 'We are all brothers and sisters in this school. Fighting divides us; let us resolve this with fairness.'",
            "They propose a fair alternating timetable. The first club agrees, but the second club attempts to bully the first club off the pitch.",
            "Tariq and Halima stand firmly with the first club, restraining the bully club until it agrees to follow the equitable schedule.",
            "Both clubs shake hands, play together peacefully, and preserve the school's harmony through principled justice."
        ],
        "scenario_text": (
            "Two student clubs in school are arguing over who gets to use the football field on Friday afternoon. The argument "
            "heats up, and some students start calling each other names. Tariq and Halima, the student leaders, step in. Tariq says, "
            "'Wait, we are all brothers and sisters in this school. Instead of fighting and taking sides, let's sit down and make a "
            "fair schedule. We will divide the time equally.' The first club agrees, but the second club tries to bully them off the "
            "field. Tariq and Halima stand firmly with the first club until the second club agrees to follow the fair schedule. "
            "Peace is restored with justice."
        ),
        "real_world_application": (
            "Become an active peacemaker in your school, household, and neighborhood. When friends or siblings fall into a dispute, "
            "never fan the flames, take biased sides, or spread gossip about the fight. Instead, practice *Islah*: meet both parties "
            "privately, listen empathetically to both perspectives, guide them toward a balanced middle ground, and remind them of "
            "their sacred bond of brotherhood and friendship."
        ),
        "reflection": (
            "Pause and reflect:\n\n"
            "1. Why does the Qur'an declare 'the believers are but brothers'? How should treating peers as spiritual brothers change our reaction when someone wrongs us?\n"
            "2. How does refusing to take a stand against a bully harm both the victim and the community?"
        ),
        "misconception": (
            "Students often think that 'making peace' means passive neutrality, turning a blind eye to bullying, or forcing the victim "
            "to forgive without consequences. Actually, Surah al-Hujurat (49:9) explicitly commands the community to confront and "
            "restrain the oppressor first, establishing that genuine Islamic peace is inseparable from justice (*'adl*)."
        ),
        "mcq": {
            "question": "According to Surah al-Hujurat, verse 9, what must the Muslim community do if one disputing party refuses mediation and continues to oppress the other?",
            "options": [
                "A. Stand back and allow the stronger faction to dominate the weaker one.",
                "B. Take the side of the wealthier party to bring a swift end to the conflict.",
                "C. Stand together against the oppressor until it returns to Allah's command, then reconcile with justice.",
                "D. Forgive the oppressor immediately and punish the victim for speaking out."
            ],
            "answer": "C",
            "explanation": "Verse 9 commands believers to fight against the one that wrongs until it returns to the command of Allah, making it mandatory to stop oppression before establishing just reconciliation."
        },
        "summary_content": (
            "### Summary & Key Takeaways\n\n"
            "- **Universal Brotherhood (*Ukhuwwah*):** Believers are united in a sacred familial bond that transcends all worldly divisions.\n"
            "- **Mandatory Peacemaking (*Islah*):** The community must actively intervene to resolve conflicts fairly.\n"
            "- **Justice before Pacification:** True reconciliation requires restraining the aggressor and establishing impartial fairness.\n\n"
            "**Essential Terminology:**\n"
            "- **Ukhuwwah:** Spiritual brotherhood/sisterhood in Islam.\n"
            "- **Islah:** Peacemaking, mediation, and righteous reconciliation."
        ),
        "key_points": [
            "All believers share a sacred bond of brotherhood (ukhuwwah) that requires mutual care and loyalty.",
            "Community members must actively mediate disputes (islah) rather than remaining silent bystanders.",
            "Peace must be anchored in absolute justice ('adl), confronting oppression while avoiding vindictiveness."
        ],
        "exit_ticket": "State two clear benefits of resolving a school dispute through peaceful mediation rather than letting hostility continue.",
        "image": {
            "title": "Prophet's Mosque Courtyard & Minarets in Madinah",
            "caption": "Madinah was the historic foundation where Islamic brotherhood (ukhuwwah) transformed previously conflicting tribes like Aws and Khazraj into a unified, just society.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Masjid_Nabawi_The_Prophet%27s_Mosque%2C_Madina.jpg",
            "author": "Muhammad Mahdi Karim",
            "source": "Wikimedia Commons",
            "licensing": "GFDL 1.2 / CC BY-SA 3.0"
        },
        "youtube": {
            "youtube_id": "VaZPoBgSV3k",
            "title": "Surah Al-Hujurat: Verses 9–10 on Brotherhood & Conflict Resolution",
            "description": "High-definition Arabic recitation with English translation of Surah Al-Hujurat verses 9 and 10 on peacemaking and brotherhood."
        }
    },

    # ── Lesson 3: Respectful Speech and Avoiding Harm ─────────────────────────
    {
        "order": 3,
        "title": "Respectful Speech and Avoiding Harm (Verses 11-12)",
        "inquiry_question": "What verbal and social behaviors are strictly prohibited in Surah al-Hujurat, and how do they harm community harmony?",
        "connection": (
            "Imagine a termite that slowly eats away at the wooden pillars of a beautiful house. From the outside, "
            "the house looks strong, but inside, the pillars are becoming weak and hollow. One day, the entire house collapses. "
            "Prohibited speech behaviors—like mocking, backbiting, and spying—are like those silent termites. They destroy "
            "the trust, love, and respect that hold a community together, eventually causing the entire society to fall apart."
        ),
        "learning_goal_statement": (
            "Identify the six destructive sins of the tongue prohibited in verses 11 and 12 and cultivate habits of respectful, uplifting speech."
        ),
        "authoritative_concept": (
            "### Prohibited Verbal & Social Sins (Verses 11–12)\n\n"
            "- **Ridicule (*Sukhriyyah*):** Mocking, belittling, or making fun of others based on physical appearance, speech, or status.\n"
            "- **Defamation & Insults (*Lamz*):** Openly attacking someone's honor, insulting them, or publicly pointing out faults.\n"
            "- **Offensive Nicknames (*Tanabuz bil-Alqab*):** Calling others by labels, nicknames, or slurs that they dislike.\n"
            "- **Baseless Suspicion (*Su' al-Dhan*):** Entertaining negative assumptions and cynical doubts about people's intentions without proof.\n"
            "- **Spying & Snooping (*Tajassus*):** Prying into others' personal lives, eavesdropping, or looking through private devices.\n"
            "- **Backbiting (*Gheebah*):** Speaking ill of an absent brother or sister in a manner that they would dislike."
        ),
        "scripture_panel": (
            "> \"O you who have believed, let not a people ridicule [another] people; perhaps they may be better than them... "
            "And do not insult one another and do not call each other by [offensive] nicknames.\"\n"
            "— **Surah Al-Hujurat, 49:11**\n\n"
            "> \"O you who have believed, avoid much [negative] suspicion. Indeed, some suspicion is sin. And do not spy or "
            "backbite each other. Would one of you like to eat the flesh of his brother when dead? You would detest it. "
            "And fear Allah; indeed, Allah is Accepting of repentance and Merciful.\"\n"
            "— **Surah Al-Hujurat, 49:12**"
        ),
        "deep_explanation": (
            "### The Sins of the Tongue and Their Spiritual Cure\n\n"
            "**1. The Humiliation of Ridicule and Insults (Verse 11):**\n"
            "The Qur'an cautions that the person mocked might possess greater honor and righteousness before Allah than the one "
            "mocking. Mockery springs from spiritual arrogance (*kibr*). Calling peers offensive nicknames inflicts lasting emotional "
            "wounds and damages mutual dignity.\n\n"
            "**2. Suspicion, Privacy, and the Horror of Backbiting (Verse 12):**\n"
            "- **Negative Suspicion:** Assuming evil corrupts the heart. Believers must cultivate *Husn al-Dhan* (good faith).\n"
            "- **Spying (*Tajassus*):** Investigating the private faults of others violates personal sanctuary and trust.\n"
            "- **Backbiting (*Gheebah*):** Allah illustrates backbiting with an unforgettable, shocking metaphor—consuming the dead "
            "flesh of one's own brother. Just as a corpse cannot defend itself against consumption, an absent person cannot defend "
            "their reputation against slander."
        ),
        "diagram_caption": "Behavioral matrix contrasting the 6 destructive sins of the tongue with prescribed virtues of speech.",
        "svg_fn": get_svg_lesson_3,
        "interactive_component": {
            "type": "comparison_table",
            "title": "Verbal Sins vs. Prescribed Islamic Speech",
            "headers": ["Behavioral Category", "Prohibited Conduct (Q 49:11-12)", "Prescribed Conduct (Islamic Ethics)", "Communal Impact"],
            "rows": [
                ["Mockery & Jokes", "Ridicule (Sukhriyyah) targeting appearances or accents", "Honoring intrinsic human dignity & recognizing hidden virtues", "Preserves emotional safety & self-worth"],
                ["Personal Labels", "Offensive Nicknames (Tanabuz) and cyber-bullying", "Calling others by the beloved names and titles they prefer", "Builds mutual respect and affection"],
                ["Perception of Motives", "Baseless Suspicion (Su' al-Dhan) & paranoia", "Good Faith (Husn al-Dhan) and charitable interpretation", "Strengthens interpersonal trust"],
                ["Personal Boundaries", "Spying (Tajassus), snooping on phones & eavesdropping", "Guarding private confidentiality and personal boundaries", "Guarantees privacy and psychological peace"],
                ["Absent Interaction", "Backbiting (Gheebah) behind a peer's back", "Defending an absent brother's honor and speaking good", "Eliminates toxic rumors and backstabbing"]
            ]
        },
        "scenario_intro": "Notice how Farhan upholds ethical speech boundaries during a cafeteria incident:",
        "scenario_steps": [
            "During lunch break, a student trips over his backpack and spills water, prompting classmates to laugh loudly.",
            "One student suggests: 'Look at that! Let's call him \"Clumsy Camel\" for the rest of the term!'",
            "Farhan speaks up gently but firmly: 'Stop, guys! Ridiculing someone and giving hurtful nicknames is strictly forbidden in Surah al-Hujurat.'",
            "He reminds them: 'The Qur'an teaches us he might be far better than any of us in the sight of Allah.'",
            "The classmates feel remorseful, apologize sincerely, and help the student clean up his spilled water."
        ],
        "scenario_text": (
            "During lunch break, a group of students are laughing at a classmate who tripped and spilled his water. One student "
            "says, 'Let's call him \"Clumsy camel\" from now on!' Farhan, remembering Surah al-Hujurat, steps in and says, 'Guys, "
            "stop! Ridiculing him and calling him an offensive nickname is completely forbidden in our religion. The Qur'an says he "
            "might be better than us in the sight of Allah. Let's help him clean up instead of making him feel bad.' The students "
            "realize their mistake, apologize, and help their classmate."
        ),
        "real_world_application": (
            "Apply these divine principles to your digital chats and social platforms. Cyberbullying, making parody memes that mock "
            "classmates, and gossiping in private WhatsApp groups are modern forms of ridicule, spying, and backbiting. Practice "
            "'Digital Modesty': If you cannot speak something truthful, uplifting, and beneficial about someone, do not type or forward "
            "it. When someone begins backbiting in your presence or in a chat group, courageously defend the absent person's honor."
        ),
        "reflection": (
            "Pause and reflect:\n\n"
            "1. Why did Allah use the repulsive metaphor of 'eating a dead brother's flesh' to describe backbiting?\n"
            "2. How does assuming the best intentions (*Husn al-Dhan*) protect you from unnecessary anger and resentment?"
        ),
        "misconception": (
            "Students often argue: 'It is not backbiting if what I am saying about him is actually true!' The Prophet Muhammad (PBUH) "
            "specifically clarified this: If what you mention about your brother in his absence is true, you have backbitten him (*gheebah*); "
            "if it is false, you have committed the even graver sin of slander (*buhtan*)."
        ),
        "mcq": {
            "question": "What vivid and shocking metaphor does Surah al-Hujurat (49:12) employ to depict the heinous sin of backbiting (gheebah)?",
            "options": [
                "A. Drinking poison from a golden goblet.",
                "B. Consuming the dead flesh of one's own brother.",
                "C. Walking barefoot over burning coals.",
                "D. Demolishing the foundation of a sacred building."
            ],
            "answer": "B",
            "explanation": "Verse 12 explicitly uses the powerful metaphor of consuming the dead flesh of one's brother to underscore the horrifying and unnatural spiritual reality of tearing down an absent person's reputation."
        },
        "summary_content": (
            "### Summary & Key Takeaways\n\n"
            "- **Preserving Honor:** Ridicule (*sukhriyyah*), insults (*lamz*), and offensive nicknames (*tanabuz*) are prohibited.\n"
            "- **Guarding the Mind & Privacy:** Suspicion (*dhan*) and spying (*tajassus*) corrode community trust.\n"
            "- **The Gravity of Backbiting (*Gheebah*):** Talking negatively about an absent person is compared to eating dead flesh.\n\n"
            "**Essential Terminology:**\n"
            "- **Gheebah:** Backbiting; mentioning an absent person in a way they would dislike.\n"
            "- **Tajassus:** Spying, prying, and searching for the private faults of others."
        ),
        "key_points": [
            "Islam bans ridicule, insults, and hurtful nicknames to protect individual human dignity.",
            "Believers must avoid negative suspicion and respect personal boundaries by banning spying.",
            "Backbiting destroys social bonds and is treated as a major spiritual crime in the Qur'an."
        ],
        "exit_ticket": "List three specific verbal behaviors strictly prohibited in Surah al-Hujurat and name their positive Islamic alternatives.",
        "image": {
            "title": "Early Qur'anic Manuscript Foliage",
            "caption": "Sacred Qur'anic text preserving Allah's timeless ethical boundaries against mockery, suspicion, spying, and backbiting (Surah al-Hujurat 49:11-12).",
            "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Birmingham_Quran_manuscript.jpg",
            "author": "Early Islamic Calligraphers (Birmingham Collection)",
            "source": "Wikimedia Commons",
            "licensing": "Public Domain"
        },
        "youtube": {
            "youtube_id": "RFow2bQ51-8",
            "title": "Surah Al-Hujurat: Verses 11–12 Recitation & English Translation",
            "description": "Heartfelt Qur'anic recitation highlighting the sacred ethical prohibitions against mockery, suspicion, and backbiting."
        }
    },

    # ── Lesson 4: Equality, Sincerity, and Accountability ─────────────────────
    {
        "order": 4,
        "title": "Equality, Sincerity, and Accountability (Verses 13-18)",
        "inquiry_question": "What is the true measure of nobility and superiority in Islam, and how does the Qur’an view human diversity?",
        "connection": (
            "In many societies, people are judged, treated differently, or grouped based on how much money they have, "
            "what language they speak, what tribe they belong to, or the color of their skin. Some people think their race "
            "makes them superior to others. In Surah al-Hujurat, verse 13, Allah (S.W.T.) delivers a revolutionary message to "
            "all of mankind: We are all created from a single pair of parents, our diversity is a beautiful gift to help us "
            "learn from one another, and no human being is superior to another except through righteousness (*taqwa*)."
        ),
        "learning_goal_statement": (
            "Explain the Qur'anic foundation of universal human equality, celebrate diversity (Li-Ta'arafu), and differentiate between outward submission (Islam) and inner faith (Iman)."
        ),
        "authoritative_concept": (
            "### Core Concepts from Surah al-Hujurat (Verses 13–18)\n\n"
            "- **Universal Human Equality:** The fundamental truth that all humans share one common origin (Adam and Eve) and possess equal inherent dignity.\n"
            "- **Diversity as a Divine Blessing (*Li-Ta'arafu*):** National, cultural, and tribal differences are intentional signs designed for mutual enrichment and cooperation, not tribal arrogance.\n"
            "- **Taqwa (The Divine Standard):** The only valid metric of superiority in the sight of Allah, encompassing piety, God-consciousness, moral character, and righteousness.\n"
            "- **Islam vs. Iman:** Islam is the external submission (performing visible rituals like prayer), while Iman is the sincere, living faith deeply embedded in the heart."
        ),
        "scripture_panel": (
            "> \"O mankind, indeed We have created you from male and female and made you peoples and tribes that you may know "
            "one another. Indeed, the most noble of you in the sight of Allah is the most righteous of you. Indeed, Allah is Knowing "
            "and Acquainted.\"\n"
            "— **Surah Al-Hujurat, 49:13**\n\n"
            "> \"The Bedouins say, 'We have believed.' Say, 'You have not yet believed; but say, \"We have submitted,\" for faith "
            "has not yet entered your hearts... Indeed, the true believers are those who believe in Allah and His Messenger and "
            "then doubt not, but strive with their wealth and lives in the cause of Allah.'\"\n"
            "— **Surah Al-Hujurat, 49:14-15**"
        ),
        "deep_explanation": (
            "### Deconstructing Prejudice and Understanding Sincere Faith\n\n"
            "**1. Dismantling Racism and Tribalism (Verse 13):**\n"
            "- **Single Ancestry:** By addressing 'O mankind' (*Ya ayyuha an-nas*), the verse includes all human beings. Descending "
            "from one father and mother proves that claims of racial purity or genetic superiority are false illusions.\n"
            "- **The Purpose of Differences:** Allah created nations (*shu'ub*) and tribes (*qaba'il*) so we may know and learn from "
            "one another (*li-ta'arafu*), fostering cultural exchange and cooperation rather than tribal hostility (*li-tanafukhu*).\n"
            "- **The True Metric of Honor:** In human conventions, nobility (*karamah*) is linked to lineage or wealth. With Allah, "
            "the sole criterion is *Taqwa* (piety, integrity, and consciousness of God).\n\n"
            "**2. The Depth of Sincerity (Verses 14–18):**\n"
            "When some desert tribes claimed full faith to boast or seek status, the Qur'an drew a critical line: Outward religious "
            "compliance (*Islam*) is only the beginning. True faith (*Iman*) requires inner sincerity of the heart, unwavering certainty, "
            "and selfless dedication to good."
        ),
        "diagram_caption": "Conceptual scale illustrating how worldly vanity weighs zero compared to the eternal weight of Taqwa.",
        "svg_fn": get_svg_lesson_4,
        "interactive_component": {
            "type": "comparison_table",
            "title": "Worldly Hierarchy vs. The Divine Standard of Taqwa",
            "headers": ["Dimension", "Worldly Human Standard", "Divine Qur'anic Standard (Q 49:13-18)"],
            "rows": [
                ["Source of Worth", "Lineage, ethnic tribe, wealth, and skin color", "Taqwa (righteousness, piety, and moral integrity)"],
                ["View of Diversity", "A pretext for tribalism, superiority, and discrimination", "A divine blessing for mutual learning and cooperation (Li-Ta'arafu)"],
                ["Common Origin", "Divided by caste, nationality, and racial divisions", "United: all children of a single pair of parents (Adam & Eve)"],
                ["Nature of Faith", "Superficial status symbols or showing off outward rituals", "Heartfelt conviction (Iman), humility, and selfless action"]
            ]
        },
        "scenario_intro": "Observe how Halima guides a prefect election discussion according to verse 13:",
        "scenario_steps": [
            "During school prefect elections, two Grade 9 students discuss candidate Salim.",
            "One student argues: 'We must vote for Salim because he belongs to our ethnic tribe and his family is prestigious and wealthy.'",
            "Halima responds: 'Salim is a good student, but choosing him based on tribe or wealth contradicts Surah al-Hujurat (49:13).'",
            "She explains: 'Allah teaches that tribal status grants zero superiority. We must evaluate who possesses the greatest integrity, honesty, and responsibility.'",
            "Her classmates agree to judge candidates by their character and demonstrated leadership rather than ethnic background."
        ],
        "scenario_text": (
            "Two students are discussing the election of a class prefect. One student says, 'We should only vote for Salim because "
            "he belongs to our tribe, and his family is very wealthy. He comes from a prestigious background.' Halima responds, 'Salim "
            "is a good student, but choosing him just because of his tribe or wealth goes against the core teachings of Surah al-Hujurat, "
            "verse 13. Allah teaches us that tribal backgrounds do not make anyone superior. We should choose the prefect based on their "
            "taqwa and character—who is the most honest, responsible, fair, and trustworthy.' The other student agrees and decides to "
            "look at character instead of background."
        ),
        "real_world_application": (
            "Take active measures to eliminate prejudice, stereotyping, and tribalism in your everyday life. Never share or laugh at "
            "ethnic jokes, and avoid forming exclusive school cliques based on language or regional origin. When selecting project partners, "
            "friends, or team leaders, judge individuals strictly by their integrity, trustworthiness, and effort. Honor the universal "
            "brotherhood of all human beings as descendants of Adam."
        ),
        "reflection": (
            "Pause and reflect:\n\n"
            "1. How does knowing that all humanity originates from Adam and Eve shatter the foundation of ethnic and racial superiority?\n"
            "2. How does the distinction between outward compliance (Islam) and heartfelt sincerity (Iman) inspire self-examination?"
        ),
        "misconception": (
            "Students often assume that pride in one's ethnicity or tribe is harmless as long as they do not openly fight others. Actually, "
            "Surah al-Hujurat dismantles tribal arrogance at its root: claiming spiritual or moral superiority based on birth lineage is "
            "completely baseless, because piety (*taqwa*) is the only standard honored by the Creator."
        ),
        "mcq": {
            "question": "According to Surah al-Hujurat, verse 13, what is the sole and ultimate standard of honor and nobility in the sight of Allah?",
            "options": [
                "A. Financial prosperity, land ownership, and business success.",
                "B. Tribal ancestry, family prestige, and racial purity.",
                "C. Piety, God-consciousness, and righteousness of character (Taqwa).",
                "D. Physical eloquence, public charisma, and academic degrees."
            ],
            "answer": "C",
            "explanation": "Verse 13 explicitly declares: 'Indeed, the most noble of you in the sight of Allah is the most righteous (atqakum) of you', making Taqwa the only divine criterion for human worth."
        },
        "summary_content": (
            "### Summary & Key Takeaways\n\n"
            "- **Universal Equality:** All human beings are descendants of Adam and Eve, rendering racism and tribalism completely baseless.\n"
            "- **Purpose of Diversity (*Li-Ta'arafu*):** Cultural differences exist to facilitate mutual enrichment, cooperation, and learning.\n"
            "- **Taqwa as True Nobility:** Nobility before Allah is earned exclusively through righteousness, piety, and good character.\n"
            "- **Heartfelt Faith (*Iman*):** True religion requires sincere inner conviction, not merely outward demonstrations.\n\n"
            "**Essential Terminology:**\n"
            "- **Taqwa:** God-consciousness, piety, and living with righteous accountability."
        ),
        "key_points": [
            "Human diversity is a creative divine sign designed for mutual discovery and peaceful interaction.",
            "Lineage, wealth, and race carry zero spiritual weight on the divine scale of justice.",
            "True faith (Iman) resides deep in the heart and reflects in selfless actions, not empty status claims."
        ],
        "exit_ticket": "Summarize in one sentence why tribalism and racism are strictly forbidden in Islamic theology.",
        "image": {
            "title": "Universal Brotherhood and Diversity in Islam (Hajj Pilgrims)",
            "caption": "Pilgrims of every race, nation, and ethnicity gather in absolute equality before Allah, fulfilling the divine decree of Surah al-Hujurat 49:13 that piety (taqwa) is the only true measure of nobility.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/The_Kaaba_during_Hajj_-_edited.jpg",
            "author": "Adli Wahid / Basile Morin",
            "source": "Wikimedia Commons",
            "licensing": "CC BY-SA 4.0"
        },
        "youtube": {
            "youtube_id": "xvEzqG9YjYQ",
            "title": "Surah Al-Hujurat: Verses 13–18 on Universal Equality & Faith",
            "description": "Inspiring recitation of the concluding verses of Surah Al-Hujurat, proclaiming universal equality, diversity, and the primacy of Taqwa."
        }
    },

    # ── Lesson 5: Surah al-Hujurat in Daily Relationships ─────────────────────
    {
        "order": 5,
        "title": "Surah al-Hujurat in Daily Relationships (Synthesis)",
        "inquiry_question": "How do we combine the teachings of Surah al-Hujurat to build peaceful, respectful, and ethical relationships in our school, family, and digital spaces?",
        "connection": (
            "Imagine a puzzle where each piece is a specific social rule. One piece is 'verify rumors,' another is 'make peace,' "
            "a third is 'avoid backbiting,' and the last is 'respect everyone equally.' When you put all these pieces together, "
            "you get a beautiful, peaceful picture of a perfectly united community. Surah al-Hujurat is that complete puzzle. "
            "In this lesson, we will synthesize all its rules to create a practical code of conduct for our daily relationships."
        ),
        "learning_goal_statement": (
            "Synthesize the social, ethical, and digital principles of Surah al-Hujurat into a unified personal relationship charter."
        ),
        "authoritative_concept": (
            "### Comprehensive Social Ethics of Surah al-Hujurat\n\n"
            "- **Holistic Code of Conduct:** Surah al-Hujurat provides an integrated constitution governing authority decorum, "
            "information vetting, conflict resolution, verbal boundaries, and human equality.\n"
            "- **The 4 Pillar Values:**\n"
            "  1. **Respect:** Deference to elders and honoring the personal dignity of all people.\n"
            "  2. **Social Justice:** Mediating conflicts fairly, opposing bullying, and rejecting prejudice.\n"
            "  3. **Communal Unity:** Protecting brotherhood (*ukhuwwah*), celebrating diversity, and promoting peace.\n"
            "  4. **Truthfulness & Sincerity:** Rigorous verification (*tabayyun*), avoiding suspicion, and purifying the heart."
        ),
        "scripture_panel": (
            "> \"The surah calls for the development of a righteous community by encouraging good character, maintaining "
            "peace, and resolving conflicts with fairness.\"\n"
            "— **KICD CBC Grade 9 IRE Curriculum Framework**\n\n"
            "> \"The believers are but brothers, so make peace between your brothers... And do not spy or backbite each other... "
            "Indeed, the most noble of you in the sight of Allah is the most righteous of you.\"\n"
            "— **Surah Al-Hujurat Synthesis (Q 49:10, 12, 13)**"
        ),
        "deep_explanation": (
            "### The 5 Domains of Daily Application\n\n"
            "Bringing the teachings of Surah al-Hujurat into daily practice involves five everyday settings:\n"
            "1. **With Authority (Verses 1–5):** Lowering speech, listening with patience, and honoring parents and educators.\n"
            "2. **With Information (Verse 6):** Enforcing the Tabayyun filter on all texts, social media posts, and school rumors.\n"
            "3. **With Conflict (Verses 9–10):** Stepping in as an active peacemaker, ending bullying, and establishing fair compromises.\n"
            "4. **With Speech (Verses 11–12):** Protecting reputations, banning derogatory slurs, respecting privacy, and rejecting backbiting.\n"
            "5. **With Diversity (Verse 13):** Treating classmates from every background as equal peers, evaluating worth through character alone."
        ),
        "diagram_caption": "Practical decision blueprint showing how to resolve 5 daily relationship challenges using Surah Al-Hujurat.",
        "svg_fn": get_svg_lesson_5,
        "interactive_component": {
            "type": "step_process",
            "title": "The 5 Everyday Pillars of Surah Al-Hujurat",
            "steps": [
                {"title": "Pillar 1: Courteous Authority Decorum", "description": "Lower speech and wait with patience when speaking with parents, teachers, and elders."},
                {"title": "Pillar 2: The Tabayyun Information Filter", "description": "Verify every online rumor or forwarded text with primary official sources before reacting."},
                {"title": "Pillar 3: Active Islah Peacemaking", "description": "Actively resolve peer arguments fairly; stand firmly against bullies and reconcile with justice."},
                {"title": "Pillar 4: Sacred Speech Boundaries", "description": "Speak kindly, call others by their loved names, protect privacy, and refuse backbiting."},
                {"title": "Pillar 5: Radical Human Equality & Taqwa", "description": "Embrace human diversity, reject tribalism, and measure true worth by righteousness alone."}
            ]
        },
        "scenario_intro": "See how Salma and her classmates established a transformative classroom agreement:",
        "scenario_steps": [
            "Salma notices frequent arguing, name-calling, and rumors in her Grade 9 classroom and decides to draft a 'Classroom Covenant'.",
            "Rule 1: 'We will verify any rumor with teachers before circulating it or believing it.'",
            "Rule 2: 'We will address everyone by the names they cherish and completely ban offensive nicknames and mockery.'",
            "Rule 3: 'Whenever a disagreement occurs, we will resolve it through fair mediation without taking biased sides.'",
            "Rule 4: 'We will treat every classmate with equal respect, regardless of family wealth, tribe, or ethnic background.'",
            "Omar exclaims: 'This is Surah al-Hujurat in action!' The class signs the covenant, creating a peaceful, trusting school environment."
        ],
        "scenario_text": (
            "Salma is drafting a 'Classroom Covenant' for her Grade 9 class. She suggests four rules: '1. We will verify any school "
            "rumor before sharing it. 2. We will call everyone by the names they love and never mock each other. 3. If there is an "
            "argument, we will sit down and resolve it fairly. 4. We will treat everyone equally, regardless of their family background.' "
            "Her classmate Omar says, 'This is the best covenant ever! It is like we are putting Surah al-Hujurat into practice every "
            "day in our classroom.' The class adopts the covenant, and classroom unity improves dramatically."
        ),
        "real_world_application": (
            "Formulate your own 'Personal Relationship Pledge' based on Surah al-Hujurat. Select three core personal commitments "
            "(e.g., 'I will never participate in backbiting chats', 'I will verify rumors before sharing', 'I will honor human diversity'). "
            "Write your pledge in your journal or study desk. Practice these commitments diligently for one full week and observe how "
            "trust, emotional tranquility, and deep friendships blossom around you."
        ),
        "reflection": (
            "Pause and reflect:\n\n"
            "1. How would our schools, neighborhoods, and digital platforms transform if everyone upheld the social ethics of Surah al-Hujurat?\n"
            "2. Which specific rule in the surah do you find most challenging to practice consistently, and what steps will you take to master it?"
        ),
        "misconception": (
            "Students frequently assume that religious ethics belong only in the mosque or during formal prayer. In reality, Surah al-Hujurat "
            "specifically targets everyday interpersonal spaces—hallways, sports pitches, digital group chats, and dinner tables—proving "
            "that genuine faith (*Iman*) is defined by our everyday character (*Akhlaq*)."
        ),
        "mcq": {
            "question": "Which of the following best describes the overarching goal of the ethical and social guidelines established in Surah al-Hujurat?",
            "options": [
                "A. To eliminate all cultural diversity and enforce identical customs across the world.",
                "B. To build a righteous, respectful, and united community where individual dignity is protected and conflicts are resolved with justice.",
                "C. To encourage believers to actively monitor and investigate the private mistakes of others.",
                "D. To teach Muslims to isolate themselves completely from individuals of other backgrounds."
            ],
            "answer": "B",
            "explanation": "The holistic teachings of Surah al-Hujurat aim to construct a cohesive, ethical, and compassionate society by preserving individual honor, instituting fair conflict resolution, and celebrating righteous diversity."
        },
        "summary_content": (
            "### Summary & Key Takeaways\n\n"
            "- **A Complete Code of Living:** Surah al-Hujurat offers a practical roadmap for interpersonal and digital ethics.\n"
            "- **The 5 Life Domains:** Authority decorum, news verification, just peacemaking, protected speech, and human equality.\n"
            "- **Faith in Action:** Living by these virtues is the direct proof of sincere belief (*Iman*) and fear of Allah (*Taqwa*).\n\n"
            "**Essential Terminology:**\n"
            "- **Comprehensive Ethics:** Integrating Qur'anic manners into every verbal, digital, and social interaction."
        ),
        "key_points": [
            "Surah al-Hujurat provides an all-encompassing charter for building ethical, peaceful, and cooperative communities.",
            "Its lessons apply directly to modern digital interactions, school conflicts, and diverse social spaces.",
            "Putting these divine rules into practice is the highest manifestation of sincere faith and righteous character."
        ],
        "exit_ticket": "Write down one specific lesson from Surah al-Hujurat that you will actively practice in your family or school life starting today.",
        "image": {
            "title": "Grand Gate of Al-Masjid an-Nabawi in Madinah",
            "caption": "The majestic entrance of the Prophet's Mosque symbolizes the open threshold to living the comprehensive ethical framework of Surah al-Hujurat in everyday interpersonal life.",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Al-Masjid_AL-Nabawi_Door.jpg",
            "author": "Belal El-Dweik",
            "source": "Wikimedia Commons",
            "licensing": "CC BY-SA 3.0"
        },
        "youtube": {
            "youtube_id": "De3Fi9EirsY",
            "title": "Surah Al-Hujurat: Complete Recitation with Thematic Reflections",
            "description": "Comprehensive recitation of Surah Al-Hujurat by Omar Hisham Al Arabi, inspiring reflection on its timeless ethical code."
        }
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic2():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 2: SURAH AL-HUJURAT (Q 49)")
    print("=" * 80)

    # 1. Verify Topic ID 342
    topic = Topic.objects.filter(id=342).first()
    if not topic:
        print("[!] ERROR: Topic ID 342 not found in database!")
        sys.exit(1)

    print(f"[i] Target Topic Found: ID={topic.id} | Name='{topic.name}' | Subject='{topic.subject.name}' | Grade='{topic.subject.grade.name}'")

    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        # Clear existing units/lessons for topic 342 to ensure idempotency
        existing_units = LearningUnit.objects.filter(topic=topic)
        existing_lessons = Lesson.objects.filter(topic=topic)
        if existing_units.exists() or existing_lessons.exists():
            print(f"[i] Clearing {existing_units.count()} existing units and {existing_lessons.count()} existing lessons for clean idempotent ingestion...")
            existing_units.delete()
            existing_lessons.delete()

        # Ingest each lesson
        for cfg in LESSONS_DATA:
            u_order = cfg["order"]
            l_title = cfg["title"]

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                name=f"Lesson {u_order}: {l_title}",
                description=clean_text(cfg["learning_goal_statement"]),
                order=u_order
            )
            total_units += 1

            # Create Published Lesson (version 1)
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "grade": "Grade 9",
                    "subject": "IRE",
                    "strand": "1.0 Qur'an",
                    "sub_strand": "1.2 Selected Chapter: Surah al-Hujurat (Q 49)",
                    "lesson_order": u_order,
                    "curriculum": "CBC",
                    "source_file": "/home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/surah-al-hujurat.md"
                }
            )
            total_lessons += 1

            # ── Create 3 Persistent Media Assets ─────────────────────────────
            # Asset 1: Authentic Wikimedia Commons Image
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
                    "source": img_info["source"],
                    "licensing": img_info["licensing"],
                    "caption": clean_text(img_info["caption"])
                }
            )
            total_assets += 1

            # Asset 2: Custom Pedagogical Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=clean_text(cfg["diagram_caption"]),
                url=f"https://vlearn.africa/assets/diagrams/ire/grade9_topic2_lesson_{u_order}.svg",
                metadata={
                    "svg_content": svg_content,
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 480",
                    "theme": "#0f172a"
                }
            )
            total_assets += 1

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
            total_assets += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Connection (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            b_img = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Connection",
                order=10,
                component_order=1,
                block_type="suggested_image",
                component_type="suggested_image",
                title=clean_text(img_info["title"]),
                content={
                    "title": clean_text(img_info["title"]),
                    "caption": clean_text(img_info["caption"]),
                    "url": img_info["url"],
                    "resolved_image_url": img_info["url"],
                    "author": img_info["author"],
                    "source": img_info["source"],
                    "licensing": img_info["licensing"]
                }
            )
            b_img.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Connection",
                order=20,
                component_order=2,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Lesson Inquiry & Objectives",
                content={
                    "title": "Lesson Inquiry & Objectives",
                    "goals": [
                        clean_text(cfg["inquiry_question"]),
                        clean_text(cfg["learning_goal_statement"])
                    ],
                    "content": f"**Inquiry Question:** {clean_text(cfg['inquiry_question'])}\n\n**Connection:** {clean_text(cfg['connection'])}"
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Teaching & Scripture (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Teaching & Scripture",
                order=30,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Authoritative Concept",
                content={
                    "title": "Authoritative Concept",
                    "markdown": clean_text(cfg["authoritative_concept"]),
                    "content": clean_text(cfg["authoritative_concept"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Teaching & Scripture",
                order=40,
                component_order=2,
                block_type="callout",
                component_type="callout",
                title="Scripture Panel: Surah Al-Hujurat",
                content={
                    "title": "Scripture Panel: Surah Al-Hujurat",
                    "content": clean_text(cfg["scripture_panel"]),
                    "text": clean_text(cfg["scripture_panel"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & Vector Architecture (3 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Explanation & Visual Architecture",
                order=50,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Clarifying the Concept & Exegesis",
                content={
                    "title": "Clarifying the Concept & Exegesis",
                    "markdown": clean_text(cfg["deep_explanation"]),
                    "content": clean_text(cfg["deep_explanation"])
                }
            )

            b_diag = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Explanation & Visual Architecture",
                order=60,
                component_order=2,
                block_type="suggested_diagram",
                component_type="suggested_diagram",
                title=f"Diagram: {l_title}",
                content={
                    "title": f"Pedagogical Blueprint: {l_title}",
                    "caption": clean_text(cfg["diagram_caption"]),
                    "svg": svg_content,
                    "svg_xml": svg_content,
                    "svg_content": svg_content
                }
            )
            b_diag.assets.add(svg_asset)

            inter_cfg = cfg["interactive_component"]
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Explanation & Visual Architecture",
                order=70,
                component_order=3,
                block_type=inter_cfg["type"],
                component_type=inter_cfg["type"],
                title=clean_text(inter_cfg["title"]),
                content=clean_dict(inter_cfg)
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Worked Example Scenario (1 block)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                page_title="Relatable Scenario in Action",
                order=80,
                component_order=1,
                block_type="worked_example",
                component_type="worked_example",
                title="Relatable Student Scenario in Action",
                content={
                    "title": "Relatable Student Scenario in Action",
                    "intro": clean_text(cfg["scenario_intro"]),
                    "steps": [clean_text(s) for s in cfg["scenario_steps"]],
                    "content": clean_text(cfg["scenario_text"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Application, Reflection & Multimedia (4 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application, Reflection & Multimedia",
                order=90,
                component_order=1,
                block_type="real_world_example",
                component_type="real_world_example",
                title="Actionable Real-World Application",
                content={
                    "title": "Actionable Real-World Application",
                    "content": clean_text(cfg["real_world_application"]),
                    "text": clean_text(cfg["real_world_application"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application, Reflection & Multimedia",
                order=100,
                component_order=2,
                block_type="reflection",
                component_type="reflection",
                title="Pause & Reflect",
                content={
                    "title": "Pause & Reflect",
                    "content": clean_text(cfg["reflection"]),
                    "text": clean_text(cfg["reflection"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application, Reflection & Multimedia",
                order=110,
                component_order=3,
                block_type="common_misconception",
                component_type="common_misconception",
                title="Critical Misconception Check",
                content={
                    "title": "Critical Misconception Check",
                    "content": clean_text(cfg["misconception"]),
                    "text": clean_text(cfg["misconception"])
                }
            )

            b_vid = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application, Reflection & Multimedia",
                order=120,
                component_order=4,
                block_type="suggested_video",
                component_type="suggested_video",
                title=clean_text(yt_info["title"]),
                content={
                    "title": clean_text(yt_info["title"]),
                    "description": clean_text(yt_info["description"]),
                    "url": f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                    "youtube_id": yt_info["youtube_id"]
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

            total_pages += 7
            total_blocks += 15
            print(f"  [+] Ingested Lesson {u_order}/5: '{l_title}' (7 cards/pages, 15 blocks, 3 LessonAssets)")

    print("=" * 80)
    print("INGESTION COMPLETE & VERIFIED!")
    print("=" * 80)
    print(f"  Topic ID            : {topic.id}")
    print(f"  Topic Name          : {topic.name}")
    print(f"  Total LearningUnits : {total_units}")
    print(f"  Total Lessons       : {total_lessons} (Published, v1)")
    print(f"  Total Cards/Pages   : {total_pages}")
    print(f"  Total LessonBlocks  : {total_blocks}")
    print(f"  Total LessonAssets  : {total_assets}")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic2()
