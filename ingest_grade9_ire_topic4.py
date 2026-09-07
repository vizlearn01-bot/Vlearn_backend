"""
VLearn CBC Grade 9 IRE — Topic 4: Selected Hadith (Unity and Avoidance of Ill Motives)
Production Ingestion and Enrichment Script for all 8 Lessons

Target Topic in DB: Topic ID 344 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
"""

import os
import sys
import re
import django
from django.db import transaction
from django.utils import timezone

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations, visual annotations, and normalizes bullet points."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|HADITH REFERENCE|BIBLE REFERENCE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|HISTORICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|MAP|TIMELINE|COMPARISON|INFOGRAPHIC|SVG)[^\]]*\]',
        '', text, flags=re.IGNORECASE
    )
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


# ─── 8 PEDAGOGICAL VECTOR SVGS (viewBox="0 0 880 440", theme #0f172a) ───────

def get_svg_lesson_1():
    """Lesson 2.2.1: The Muslim Ummah as One Interconnected Body"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="heartGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="solidarityGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="feverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE MUSLIM UMMAH AS ONE INTERCONNECTED BODY</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Prophetic Model of Mutual Love (Tawadd), Mercy (Tarahum) &amp; Systemic Solidarity (Sahih Muslim #2586)</text>

  <!-- Central Heart / Core -->
  <g transform="translate(365, 140)" filter="url(#shadow1)">
    <circle cx="75" cy="75" r="70" fill="url(#heartGrad)" stroke="#fca5a5" stroke-width="2.5"/>
    <text x="75" y="58" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">SPIRITUAL CORE</text>
    <text x="75" y="76" fill="#fef08a" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">IMAN &amp; MAWADDAH</text>
    <text x="75" y="94" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"Mutual Love &amp; Mercy"</text>
    <text x="75" y="110" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(Tawadd &amp; Tarahum)</text>
  </g>

  <!-- Node 1: Mind / Vigilance (Top) -->
  <g transform="translate(365, 80)" filter="url(#shadow1)">
    <rect width="150" height="45" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="75" y="20" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">MIND &amp; CONSCIENCE</text>
    <text x="75" y="36" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Moral Alertness &amp; Empathy</text>
  </g>
  <line x1="440" y1="125" x2="440" y2="140" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 3"/>

  <!-- Node 2: Afflicted Limb (Left Side - Pain Origin) -->
  <g transform="translate(45, 140)" filter="url(#shadow1)">
    <rect width="250" height="150" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect width="250" height="32" rx="10" fill="#9f1239"/>
    <text x="125" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">AFFLICTED MEMBER / LIMB</text>
    <text x="20" y="55" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Hardship, Illness, or Exclusion</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Academic struggle or loneliness</text>
    <text x="20" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Family distress or poverty</text>
    <rect x="20" y="110" width="210" height="26" rx="6" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
    <text x="125" y="127" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Pain Signal: "A Limb Aches..."</text>
  </g>
  <line x1="295" y1="215" x2="365" y2="215" stroke="#f43f5e" stroke-width="2.5"/>

  <!-- Node 3: Systemic Physiological Response (Right Side) -->
  <g transform="translate(585, 140)" filter="url(#shadow1)">
    <rect width="250" height="150" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="250" height="32" rx="10" fill="url(#feverGrad)"/>
    <text x="125" y="21" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">SYSTEMIC RESPONSE OF BODY</text>
    <text x="20" y="55" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. AS-SAHAR (Sleeplessness):</text>
    <text x="30" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Active vigilance &amp; collective worry</text>
    <text x="20" y="98" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. AL-HUMMA (Fever):</text>
    <text x="30" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Mobilized resources &amp; active healing</text>
    <rect x="20" y="124" width="210" height="20" rx="4" fill="#0f172a"/>
    <text x="125" y="138" fill="#10b981" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">✓ Entire Ummah Rallies in Aid</text>
  </g>
  <line x1="515" y1="215" x2="585" y2="215" stroke="#f59e0b" stroke-width="2.5"/>

  <!-- Node 4: Action Limbs (Bottom Hands & Feet) -->
  <g transform="translate(240, 315)" filter="url(#shadow1)">
    <rect width="400" height="50" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="200" y="22" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">TA'ATUF: HANDS &amp; FEET IN PRACTICAL ACTION</text>
    <text x="200" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Sharing food • Paying school fees • Offering emotional comfort • Stopping bullies</text>
  </g>
  <line x1="440" y1="290" x2="440" y2="315" stroke="#10b981" stroke-width="2"/>

  <!-- Footer Scripture Ribbon -->
  <rect x="45" y="385" width="790" height="30" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="405" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle" font-style="italic">"When any limb of it aches, the whole body aches, because of sleeplessness and fever." — Sahih Muslim</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 2.2.2: Cliquish & Divided vs United & Cooperative School Community Matrix"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="redHeader" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b91c1c"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
    <linearGradient id="greenHeader" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">SCHOOL COMMUNITY SOCIAL ARCHITECTURE MATRIX</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Contrasting Divided Cliquishness with Islamic Righteous Cooperation (Surah Al-Ma'idah 5:2)</text>

  <!-- Left Column: Cliquish & Divided School -->
  <g transform="translate(45, 85)" filter="url(#shadow2)">
    <rect width="375" height="295" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.6"/>
    <rect width="375" height="38" rx="10" fill="url(#redHeader)"/>
    <text x="187" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">CLIQUISH &amp; DIVIDED ENVIRONMENT (❌ HARMFUL)</text>

    <g transform="translate(20, 52)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
      <text x="12" y="16" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Exclusive Cliques &amp; Tribalism</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Social circles based on wealth, ethnicity, or popularity</text>
    </g>

    <g transform="translate(20, 98)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
      <text x="12" y="16" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Knowledge Hoarding</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Hiding past exam papers and study notes from peers</text>
    </g>

    <g transform="translate(20, 144)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
      <text x="12" y="16" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Public Mockery &amp; Teasing</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Laughing at incorrect answers; filming embarrassing clips</text>
    </g>

    <g transform="translate(20, 190)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
      <text x="12" y="16" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Social Desertion (Tadabur)</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Ignoring isolated students; spreading secret rumors</text>
    </g>

    <rect x="20" y="240" width="335" height="42" rx="6" fill="#450a0a" stroke="#f43f5e" stroke-width="1"/>
    <text x="167" y="258" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">CONSEQUENCE: Chronic anxiety, loneliness &amp; failure</text>
    <text x="167" y="273" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Violates the "One Body" principle of mutual solidarity</text>
  </g>

  <!-- Right Column: United & Cooperative School -->
  <g transform="translate(460, 85)" filter="url(#shadow2)">
    <rect width="375" height="295" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.6"/>
    <rect width="375" height="38" rx="10" fill="url(#greenHeader)"/>
    <text x="187" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">UNITED &amp; COOPERATIVE SCHOOL (✓ TA'AWUN)</text>

    <g transform="translate(20, 52)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="12" y="16" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Inclusive Circles of Welcome</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Every student is invited to lunch tables and study desks</text>
    </g>

    <g transform="translate(20, 98)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="12" y="16" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Collaborative Peer Tutoring</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Sharing notes, library books, and revision materials</text>
    </g>

    <g transform="translate(20, 144)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="12" y="16" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Constructive Encouragement</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Preserving peer dignity with private counsel and patience</text>
    </g>

    <g transform="translate(20, 190)">
      <rect width="335" height="38" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="12" y="16" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Mutual Celebration &amp; Islah</text>
      <text x="12" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Reconciling arguments within 3 days; sharing Salam</text>
    </g>

    <rect x="20" y="240" width="335" height="42" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="167" y="258" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">CONSEQUENCE: Psychological safety, joy &amp; high marks</text>
    <text x="167" y="273" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Fulfills Surah Al-Ma'idah 5:2: "Cooperate in righteousness"</text>
  </g>

  <!-- Bottom Anchor Banner -->
  <rect x="45" y="390" width="790" height="28" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="408" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">DIVINE RULE: "Cooperate in righteousness and piety, but do not cooperate in sin and aggression." [5:2]</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 2.2.3: The 6 Prohibited Ill Motives & Destructive Social Chain Flowchart"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="pillGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="mandateGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">THE 6 PROHIBITED ILL MOTIVES &amp; DESTRUCTIVE SOCIAL CHAIN</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Degenerative Progression from Suspicion to Social Collapse (Sahih al-Bukhari #6064)</text>

  <!-- 5 Sequential Nodes -->
  <!-- Node 1: Zann -->
  <g transform="translate(35, 80)" filter="url(#shadow3)">
    <rect width="145" height="175" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="145" height="30" rx="10" fill="url(#pillGrad)"/>
    <text x="72" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. ZANN (Suspicion)</text>
    <text x="72" y="50" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">COGNITIVE ROOT</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Groundless negative</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  assumptions</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• "Worst of false</text>
    <text x="12" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  tales" (Hadith)</text>
    <rect x="8" y="136" width="129" height="28" rx="5" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
    <text x="72" y="153" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Seeds Paranoia</text>
  </g>
  <line x1="180" y1="165" x2="198" y2="165" stroke="#f43f5e" stroke-width="2"/>

  <!-- Node 2: Tajassus -->
  <g transform="translate(198, 80)" filter="url(#shadow3)">
    <rect width="145" height="175" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="145" height="30" rx="10" fill="#d97706"/>
    <text x="72" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2. TAJASSUS (Spying)</text>
    <text x="72" y="50" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">INVESTIGATION</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Hunting for faults</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  and secrets</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Peeking at phones,</text>
    <text x="12" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  desks, and notes</text>
    <rect x="8" y="136" width="129" height="28" rx="5" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="72" y="153" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Breaches Privacy</text>
  </g>
  <line x1="343" y1="165" x2="361" y2="165" stroke="#f59e0b" stroke-width="2"/>

  <!-- Node 3: Najsh -->
  <g transform="translate(361, 80)" filter="url(#shadow3)">
    <rect width="155" height="175" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="155" height="30" rx="10" fill="#0369a1"/>
    <text x="77" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. NAJSH (Deception)</text>
    <text x="77" y="50" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">EXPLOITATION</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Artificially hiking</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  prices in trade</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Misleading peers</text>
    <text x="12" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  for personal gain</text>
    <rect x="8" y="136" width="139" height="28" rx="5" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="77" y="153" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Destroys Honesty</text>
  </g>
  <line x1="516" y1="165" x2="534" y2="165" stroke="#0284c7" stroke-width="2"/>

  <!-- Node 4: Hasad & Bughd -->
  <g transform="translate(534, 80)" filter="url(#shadow3)">
    <rect width="150" height="175" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="150" height="30" rx="10" fill="#7e22ce"/>
    <text x="75" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4. HASAD &amp; BUGHD</text>
    <text x="75" y="50" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">INTERNAL MALICE</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Resenting peer marks</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  or blessings</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Harboring rancor</text>
    <text x="12" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  and deep hatred</text>
    <rect x="8" y="136" width="134" height="28" rx="5" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="75" y="153" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Hardens the Heart</text>
  </g>
  <line x1="684" y1="165" x2="702" y2="165" stroke="#a855f7" stroke-width="2"/>

  <!-- Node 5: Tadabur -->
  <g transform="translate(702, 80)" filter="url(#shadow3)">
    <rect width="145" height="175" rx="10" fill="#1e293b" stroke="#e11d48" stroke-width="1.5"/>
    <rect width="145" height="30" rx="10" fill="#be123c"/>
    <text x="72" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">5. TADABUR (Desert)</text>
    <text x="72" y="50" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SOCIAL RUPTURE</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Severing ties</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  &amp; boycotting</text>
    <text x="12" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Refusing to say</text>
    <text x="12" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  salam over 3 days</text>
    <rect x="8" y="136" width="129" height="28" rx="5" fill="#0f172a" stroke="#e11d48" stroke-width="1"/>
    <text x="72" y="153" fill="#fda4af" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Breaks Brotherhood</text>
  </g>

  <!-- Bottom Resolution Banner -->
  <g transform="translate(35, 275)" filter="url(#shadow3)">
    <rect width="812" height="120" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="812" height="34" rx="10" fill="url(#mandateGrad)"/>
    <text x="406" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">THE PROPHETIC RESOLUTION: "KUNU IBADALLAHI IKHWAANA" (AND BE SERVANTS OF ALLAH, BROTHERS!)</text>

    <g transform="translate(30, 48)">
      <rect width="225" height="55" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="112" y="20" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1. HUSN AL-ZANN (Good Faith)</text>
      <text x="112" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Assume the best of your brother</text>
    </g>

    <g transform="translate(290, 48)">
      <rect width="230" height="55" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="115" y="20" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">2. SITR (Concealing Faults)</text>
      <text x="115" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Never expose flaws to shame peers</text>
    </g>

    <g transform="translate(555, 48)">
      <rect width="225" height="55" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="112" y="20" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">3. RECONCILIATION IN 3 DAYS</text>
      <text x="112" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Be the first to initiate Salam</text>
    </g>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 2.2.4: Social Media & Digital Communication Ethical Filter Protocol"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="phoneUi" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">SOCIAL MEDIA &amp; DIGITAL COMMUNICATION ETHICAL FILTER</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Prophetic 3-Gate Verification Protocol Before Forwarding, Reposting, or Messaging Online</text>

  <!-- Left: Smartphone UI Mockup -->
  <g transform="translate(50, 80)" filter="url(#shadow4)">
    <rect width="250" height="325" rx="20" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <!-- Screen Notch & Speaker -->
    <rect x="85" y="8" width="80" height="8" rx="4" fill="#334155"/>
    <!-- App Header -->
    <rect x="10" y="24" width="230" height="34" rx="6" fill="url(#phoneUi)"/>
    <text x="125" y="45" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Class WhatsApp Group</text>

    <!-- Incoming Message Bubble -->
    <rect x="18" y="70" width="214" height="75" rx="8" fill="#1e293b" stroke="#e11d48" stroke-width="1"/>
    <text x="26" y="88" fill="#fda4af" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">UNVERIFIED RUMOR:</text>
    <text x="26" y="104" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9">"Did you hear Amina cheated on</text>
    <text x="26" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9">the exam? Forward to everyone!"</text>
    <text x="26" y="136" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">⚠️ Risk: Zann &amp; Cyber-Gheebah</text>

    <!-- Filter Processing Graphic -->
    <rect x="18" y="158" width="214" height="60" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.2"/>
    <text x="125" y="180" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">ETHICAL HOLD TRIGGERED</text>
    <text x="125" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Applying Prophetic 3-Gate Filter</text>

    <!-- User Action Buttons -->
    <rect x="18" y="235" width="100" height="32" rx="6" fill="#be123c"/>
    <text x="68" y="255" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">❌ DELETE</text>

    <rect x="132" y="235" width="100" height="32" rx="6" fill="#059669"/>
    <text x="182" y="255" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">✓ COUNSEL</text>

    <text x="125" y="295" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Protect Your Sister's Dignity (Sitr)</text>
  </g>

  <!-- Right: 3-Gate Ethical Protocol Pipeline -->
  <g transform="translate(330, 80)" filter="url(#shadow4)">
    <rect width="500" height="325" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>

    <!-- Gate 1: Verification -->
    <g transform="translate(20, 16)">
      <rect width="460" height="68" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
      <circle cx="28" cy="34" r="14" fill="#0284c7"/>
      <text x="28" y="39" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="900" text-anchor="middle">1</text>
      <text x="55" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800">GATE 1: TRUTH &amp; VERIFICATION (TABAYYUN)</text>
      <text x="55" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Is this information 100% verified with primary evidence?</text>
      <text x="55" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Surah Al-Hujurat 49:6 — "If a troublemaker brings news, investigate..."</text>
    </g>

    <!-- Gate 2: Privacy -->
    <g transform="translate(20, 96)">
      <rect width="460" height="68" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
      <circle cx="28" cy="34" r="14" fill="#d97706"/>
      <text x="28" y="39" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="900" text-anchor="middle">2</text>
      <text x="55" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800">GATE 2: PRIVACY &amp; SENSITIVITY (SITR)</text>
      <text x="55" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Does this message respect personal privacy and avoid spying (Tajassus)?</text>
      <text x="55" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">No taking secret screenshots of private chats or peeking at unlocked phones.</text>
    </g>

    <!-- Gate 3: Benefit -->
    <g transform="translate(20, 176)">
      <rect width="460" height="68" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
      <circle cx="28" cy="34" r="14" fill="#059669"/>
      <text x="28" y="39" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="900" text-anchor="middle">3</text>
      <text x="55" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800">GATE 3: BENEFIT &amp; SOCIAL HARMONY (ISLAH)</text>
      <text x="55" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Will sharing this build unity and trust, or cause ridicule and division?</text>
      <text x="55" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Prophetic Rule — "Whoever believes in Allah and the Last Day, let him speak good or remain silent."</text>
    </g>

    <!-- Protocol Summary Banner -->
    <g transform="translate(20, 256)">
      <rect width="460" height="52" rx="6" fill="#450a0a" stroke="#e11d48" stroke-width="1.2"/>
      <text x="230" y="22" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">THE ZERO TOLERANCE DIGITAL RULE</text>
      <text x="230" y="40" fill="#fecdd3" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">If a post fails EVEN ONE gate -> DELETE IT IMMEDIATELY &amp; BREAK THE CHAIN!</text>
    </g>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 2.2.5: Dual Pillars of Social Harmony in Hadith"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="unityCol" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="shieldCol" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="archApex" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">DUAL PILLARS OF ISLAMIC SOCIAL HARMONY IN HADITH</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Balancing Positive Construction (Sahih Muslim) with Protective Restraint (Sahih al-Bukhari)</text>

  <!-- Left Pillar: Positive Construction (Muslim) -->
  <g transform="translate(55, 80)" filter="url(#shadow5)">
    <rect width="255" height="295" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="255" height="38" rx="12" fill="url(#unityCol)"/>
    <text x="127" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PILLAR 1: POSITIVE VIRTUE (TAHLIYAH)</text>

    <g transform="translate(15, 50)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="10" y="18" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Mawaddah (Mutual Love)</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Deep spiritual affection uniting all believers</text>
    </g>

    <g transform="translate(15, 102)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="10" y="18" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Tarahum (Mutual Mercy)</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Overlooking faults &amp; soothing suffering</text>
    </g>

    <g transform="translate(15, 154)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="10" y="18" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Ta'atuf (Kindness &amp; Aid)</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Mobilizing practical resources &amp; food</text>
    </g>

    <g transform="translate(15, 206)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
      <text x="10" y="18" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">As-Sahar &amp; Al-Humma</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Sleeplessness &amp; fever in solidarity</text>
    </g>

    <text x="127" y="276" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SOURCE: Sahih Muslim #2586 ("One Body")</text>
  </g>

  <!-- Center Vault / Arch Connector -->
  <g transform="translate(330, 80)" filter="url(#shadow5)">
    <!-- Arch Keystone / Dome -->
    <rect width="220" height="50" rx="10" fill="url(#archApex)"/>
    <text x="110" y="22" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="900" text-anchor="middle">UKHUWWAH</text>
    <text x="110" y="38" fill="#0f172a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">DIVINE BROTHERHOOD</text>

    <!-- Center Balance Box -->
    <rect y="65" width="220" height="230" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="92" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">THE GARDEN PARABLE</text>

    <rect x="15" y="105" width="190" height="50" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="105" y="125" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">PLANTING FLOWERS</text>
    <text x="105" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Loving, giving, caring, sharing</text>

    <text x="110" y="172" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="900" text-anchor="middle">+</text>

    <rect x="15" y="182" width="190" height="50" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="105" y="202" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">PULLING THE WEEDS</text>
    <text x="105" y="219" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Uprooting suspicion, spying, envy</text>

    <rect x="15" y="245" width="190" height="36" rx="6" fill="#064e3b"/>
    <text x="105" y="267" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">MIZAN (PERFECT BALANCE)</text>
  </g>

  <!-- Right Pillar: Protective Restraint (Bukhari) -->
  <g transform="translate(570, 80)" filter="url(#shadow5)">
    <rect width="255" height="295" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.8"/>
    <rect width="255" height="38" rx="12" fill="url(#shieldCol)"/>
    <text x="127" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PILLAR 2: PREVENTIVE SHIELD (TAKHLIYAH)</text>

    <g transform="translate(15, 50)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#b91c1c" stroke-width="1"/>
      <text x="10" y="18" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Anti-Zann (Zero Suspicion)</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Rejecting groundless negative assumptions</text>
    </g>

    <g transform="translate(15, 102)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#b91c1c" stroke-width="1"/>
      <text x="10" y="18" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Anti-Tajassus (Zero Spying)</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Respecting privacy; no hunting for faults</text>
    </g>

    <g transform="translate(15, 154)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#b91c1c" stroke-width="1"/>
      <text x="10" y="18" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Anti-Najsh (Zero Deceit)</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">No manipulation in trade or communication</text>
    </g>

    <g transform="translate(15, 206)">
      <rect width="225" height="42" rx="6" fill="#0f172a" stroke="#b91c1c" stroke-width="1"/>
      <text x="10" y="18" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Anti-Tadabur (Zero Desertion)</text>
      <text x="10" y="32" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Reconciling arguments within 3 days</text>
    </g>

    <text x="127" y="276" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SOURCE: Sahih al-Bukhari #6064 ("Be Brothers")</text>
  </g>

  <!-- Foundation Stone -->
  <rect x="55" y="390" width="770" height="30" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="440" y="410" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">BEDROCK: IMAN (FAITH IN ALLAH) • TAQWA (GOD-CONSCIOUSNESS) • IKHLAS (SINCERITY)</text>
</svg>"""


def get_svg_lesson_6():
    """Lesson 2.2.6: 4-Stage Reconciliation (Islah) Mediation Flowchart"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">4-STAGE ISLAMIC CONFLICT RESOLUTION (ISLAH) MEDIATION FLOWCHART</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Structured Procedural Framework for School &amp; Community Peer Mediation (Surah Al-Hujurat 49:9-10)</text>

  <!-- Stage 1: De-escalate -->
  <g transform="translate(35, 85)" filter="url(#shadow6)">
    <rect width="185" height="280" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.8"/>
    <rect width="185" height="36" rx="10" fill="#be123c"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">1. DE-ESCALATE (Takhfif)</text>

    <text x="15" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Immediate Action:</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Intervene calmly</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Separate shouting</text>
    <text x="15" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  classmates</text>
    <text x="15" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Disperse crowds &amp;</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  stop phone filming</text>
    <text x="15" y="166" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Move to private bench</text>

    <rect x="10" y="225" width="165" height="42" rx="6" fill="#450a0a" stroke="#f43f5e" stroke-width="1"/>
    <text x="92" y="242" fill="#fda4af" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">RULE: Prevent physical</text>
    <text x="92" y="257" fill="#fda4af" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">harm and cool emotions</text>
  </g>
  <line x1="220" y1="225" x2="242" y2="225" stroke="#f43f5e" stroke-width="2"/>

  <!-- Stage 2: Verify -->
  <g transform="translate(242, 85)" filter="url(#shadow6)">
    <rect width="185" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="185" height="36" rx="10" fill="#d97706"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">2. VERIFY (Tabayyun)</text>

    <text x="15" y="60" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Fact-Finding:</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Hear both sides</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  without interruptions</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Strip away rumors</text>
    <text x="15" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  and emotional Zann</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Inquire directly with</text>
    <text x="15" y="166" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  teacher or source</text>

    <rect x="10" y="225" width="165" height="42" rx="6" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
    <text x="92" y="242" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">RULE: Truth before</text>
    <text x="92" y="257" fill="#fde68a" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">any judgment or blame</text>
  </g>
  <line x1="427" y1="225" x2="450" y2="225" stroke="#f59e0b" stroke-width="2"/>

  <!-- Stage 3: Mediate -->
  <g transform="translate(450, 85)" filter="url(#shadow6)">
    <rect width="185" height="280" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.8"/>
    <rect width="185" height="36" rx="10" fill="#0369a1"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">3. MEDIATE (Islah)</text>

    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Spiritual Guidance:</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Remind them: "You are</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  brothers in faith!"</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Cite Hadith of one body</text>
    <text x="15" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Clarify innocent</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  misunderstandings</text>
    <text x="15" y="166" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Soften hearts to forgive</text>

    <rect x="10" y="225" width="165" height="42" rx="6" fill="#082f49" stroke="#0284c7" stroke-width="1"/>
    <text x="92" y="242" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">RULE: Appeal to Iman</text>
    <text x="92" y="257" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">and shared brotherhood</text>
  </g>
  <line x1="635" y1="225" x2="658" y2="225" stroke="#0284c7" stroke-width="2"/>

  <!-- Stage 4: Reconcile -->
  <g transform="translate(658, 85)" filter="url(#shadow6)">
    <rect width="185" height="280" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="185" height="36" rx="10" fill="#047857"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">4. RECONCILE (Sulh)</text>

    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Restoration of Peace:</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Offender offers sincere</text>
    <text x="15" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  and humble apology</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Hurt peer forgives</text>
    <text x="15" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  for the sake of Allah</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Warm handshake &amp;</text>
    <text x="15" y="166" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  exchange of Salam</text>

    <rect x="10" y="225" width="165" height="42" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="92" y="242" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">OUTCOME: Restored</text>
    <text x="92" y="257" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">unity and divine reward</text>
  </g>

  <!-- Bottom Command Banner -->
  <rect x="35" y="385" width="808" height="30" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="405" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">"The believers are but brothers, so make peace between your brothers..." [Surah Al-Hujurat 49:10]</text>
</svg>"""


def get_svg_lesson_7():
    """Lesson 2.2.7: Daily Social Conduct Routine (The Brotherhood Code)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadow7" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">DAILY SOCIAL CONDUCT ROUTINE: THE BROTHERHOOD CODE</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Translating Prophetic Guidance into 4 Daily Touchpoints of Consistent Virtue (Bukhari #6465)</text>

  <!-- Quadrant 1: Morning Intention (Top Left) -->
  <g transform="translate(45, 80)" filter="url(#shadow7)">
    <rect width="380" height="140" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="380" height="30" rx="10" fill="#b45309"/>
    <text x="190" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">TOUCHPOINT 1: MORNING INTENTION (NIYYAH)</text>
    <text x="18" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Time: Dawn &amp; Before Leaving Home</text>
    <text x="18" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Dedicate all social interactions to earning Allah's pleasure</text>
    <text x="18" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Morning Du'a: "O Allah, guard my tongue &amp; hands from harming peers"</text>
    <text x="18" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Resolve to initiate cheerful Salam and overlook minor offenses</text>
    <text x="18" y="124" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Prophetic Hadith: "Actions are judged only by intentions" [Bukhari #1]</text>
  </g>

  <!-- Quadrant 2: School Engagement (Top Right) -->
  <g transform="translate(455, 80)" filter="url(#shadow7)">
    <rect width="380" height="140" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="380" height="30" rx="10" fill="#047857"/>
    <text x="190" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">TOUCHPOINT 2: CLASSROOM BROTHERHOOD (TA'AWUN)</text>
    <text x="18" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Time: Classroom, Break Times &amp; Study Circles</text>
    <text x="18" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Actively share textbooks, stationery, and revision summaries</text>
    <text x="18" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Invite lonely or isolated students to join your lunch table</text>
    <text x="18" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sincerely congratulate classmates on their academic achievements</text>
    <text x="18" y="124" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Quranic Mandate: "And cooperate in righteousness and piety" [5:2]</text>
  </g>

  <!-- Quadrant 3: Digital Hygiene (Bottom Left) -->
  <g transform="translate(45, 235)" filter="url(#shadow7)">
    <rect width="380" height="140" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="380" height="30" rx="10" fill="#0369a1"/>
    <text x="190" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">TOUCHPOINT 3: DIGITAL HYGIENE (ANTI-TAJASSUS)</text>
    <text x="18" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Time: Afternoon &amp; Smartphone Interaction</text>
    <text x="18" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Apply the 3-Gate Ethical Filter before posting, sharing, or liking</text>
    <text x="18" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Exit class gossip groups dedicated to mocking teachers or peers</text>
    <text x="18" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Guard peer privacy: never peek at unlocked screens or forward leaks</text>
    <text x="18" y="124" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Hadith Warning: "Beware of suspicion; suspicion is false tales" [Bukhari]</text>
  </g>

  <!-- Quadrant 4: Evening Self-Audit (Bottom Right) -->
  <g transform="translate(455, 235)" filter="url(#shadow7)">
    <rect width="380" height="140" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="380" height="30" rx="10" fill="#7e22ce"/>
    <text x="190" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">TOUCHPOINT 4: EVENING SELF-AUDIT (MUHASABAH)</text>
    <text x="18" y="52" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Time: Bedtime &amp; Night Reflection</text>
    <text x="18" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Audit the day's speech: Did I backbite or mock anyone today?</text>
    <text x="18" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Actively forgive anyone who offended or insulted you before sleeping</text>
    <text x="18" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Make sincere Istighfar (repentance) and cleanse the heart of malice</text>
    <text x="18" y="124" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Prophetic Advice: "Audit yourselves before you are audited by Allah"</text>
  </g>

  <!-- Bottom Continuity Ribbon -->
  <rect x="45" y="390" width="790" height="28" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="408" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">"The most beloved of deeds to Allah are those that are consistent, even if they are small." — Sahih al-Bukhari #6465</text>
</svg>"""


def get_svg_lesson_8():
    """Lesson 2.2.8: Master Comprehensive Architecture of Social Harmony in Hadith"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="roofGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow8" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">MASTER ARCHITECTURE OF ISLAMIC SOCIAL HARMONY IN HADITH</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comprehensive Synthesis: Unity, Avoidance of Ill Motives, Verification &amp; Daily Living Brotherhood</text>

  <!-- Crown Roof / Canopy -->
  <g transform="translate(190, 75)" filter="url(#shadow8)">
    <rect width="500" height="42" rx="10" fill="url(#roofGrad)"/>
    <text x="250" y="22" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="900" text-anchor="middle">A PEACEFUL, UNITED UMMAH (SURAH AL-HUJURAT 49:10)</text>
    <text x="250" y="35" fill="#0f172a" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Social Justice • Collective Empathy • Psychological Safety • Divine Mercy</text>
  </g>

  <!-- 3 Grand Structural Columns -->
  <!-- Column 1: Positive Construction (Left) -->
  <g transform="translate(45, 130)" filter="url(#shadow8)">
    <rect width="250" height="235" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.6"/>
    <rect width="250" height="32" rx="10" fill="#047857"/>
    <text x="125" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">1. POSITIVE UNITY (MUSLIM)</text>

    <text x="15" y="52" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">The Living Body Model:</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tawadd (Mutual Love)</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tarahum (Mutual Mercy)</text>
    <text x="15" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Ta'atuf (Mutual Kindness)</text>
    <text x="15" y="122" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Collective Reflex:</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• As-Sahar (Sleeplessness / Vigilance)</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Al-Humma (Fever / Mobilized Care)</text>

    <rect x="15" y="172" width="220" height="50" rx="6" fill="#064e3b"/>
    <text x="125" y="192" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">TAHLIYAH: Planting Flowers</text>
    <text x="125" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Active benevolence &amp; shared relief</text>
  </g>

  <!-- Column 2: Operational Protocols (Center) -->
  <g transform="translate(315, 130)" filter="url(#shadow8)">
    <rect width="250" height="235" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.6"/>
    <rect width="250" height="32" rx="10" fill="#0284c7"/>
    <text x="125" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">2. OPERATIONAL TOOLS (QURAN)</text>

    <text x="15" y="52" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Community Mechanisms:</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Ta'awun: Righteous team cooperation</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tabayyun: 3-Gate verification</text>
    <text x="15" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Islah: 4-Stage mediation protocol</text>
    <text x="15" y="122" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Daily Life Routine:</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Morning Niyyah (Pure intention)</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Evening Muhasabah (Self-audit)</text>

    <rect x="15" y="172" width="220" height="50" rx="6" fill="#082f49"/>
    <text x="125" y="192" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">MEDIATION &amp; PRACTICE</text>
    <text x="125" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Turning knowledge into habits</text>
  </g>

  <!-- Column 3: Prohibited Ill Motives (Right) -->
  <g transform="translate(585, 130)" filter="url(#shadow8)">
    <rect width="250" height="235" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.6"/>
    <rect width="250" height="32" rx="10" fill="#b91c1c"/>
    <text x="125" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">3. PROHIBITED VICES (BUKHARI)</text>

    <text x="15" y="52" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Termites of Brotherhood:</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Zann: Negative suspicion</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tajassus: Spying &amp; fault-hunting</text>
    <text x="15" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Najsh: Commercial / verbal deceit</text>
    <text x="15" y="122" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Internal Malice &amp; Rupture:</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Hasad (Envy) &amp; Bughda (Hatred)</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tadabur: Boycott &amp; desertion</text>

    <rect x="15" y="172" width="220" height="50" rx="6" fill="#450a0a"/>
    <text x="125" y="192" fill="#fda4af" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">TAKHLIYAH: Pulling Weeds</text>
    <text x="125" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Purifying the heart from diseases</text>
  </g>

  <!-- Master Foundation Keystone -->
  <g transform="translate(45, 380)" filter="url(#shadow8)">
    <rect width="790" height="40" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="395" y="25" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">FOUNDATION KEYSTONE: IMAN (FAITH) • TAQWA (GOD-CONSCIOUSNESS) • IKHLAS (SINCERE INTENTION)</text>
  </g>
</svg>"""


# ─── DATA MATRIX FOR ALL 8 LESSONS ───────────────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 2.2.1 ───────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Lesson 2.2.1: Hadith on unity: source reading",
        "unit_description": "Examines the foundational Hadith comparing the Muslim Ummah to a single living interconnected body in mutual love, sympathy, and collective support.",
        "lesson_title": "Hadith on Unity: Source Reading",
        "diagram_title": "The Muslim Ummah as One Interconnected Body",
        "svg_fn": get_svg_lesson_1,
        "image": {
            "title": "The Kaaba during Hajj — The Global Unity of the Ummah",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/The_Kaaba_during_Hajj.jpg",
            "caption": "Millions of Muslims from every race, tribe, and culture united in worship at the Kaaba, embodying the single body of the Ummah.",
            "author": "Muhammad Mahdi Karim",
            "licensing": "GNU FDL / CC-BY-SA-3.0",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "The Believers are Like One Body — Hadith Explanation",
            "youtube_id": "ddorxxHB62w",
            "description": "Scholarly exposition of the physiological metaphor in Sahih Muslim illustrating the mutual love, affection, and solidarity required among believers."
        },
        "inquiry_question": "What is the significance of unity in Islam, and how does the Prophet's body analogy explain mutual concern?",
        "connection": "Imagine a cold winter night when your toe is severely stubbed. You do not find your eyes saying, 'We are fine, we do not care about the toe, so we will sleep.' Instead, your whole body stays awake; you feel a fever, your heart beats faster, and your hands reach down to hold the toe. The human body is a single, interconnected system. In this lesson, we will read and analyze the Prophet’s (PBUH) famous statement that compares the entire Muslim community (Ummah) to a single, living body.",
        "goals": [
            "Recite, translate, and analyze the Hadith on the unity of believers recorded in Sahih Muslim.",
            "Explain the biological analogy of the interconnected human body as a model for social solidarity and empathy.",
            "Identify the duties of mutual love (Mawaddah), affection (Tarahum), and fellow-feeling (Ta'atuf) in everyday community life."
        ],
        "authoritative_concept": (
            "Muslim Unity (Ummah) represents the spiritual, moral, and social bond connecting all believers worldwide, "
            "transcending artificial divisions of race, ethnicity, tribe, nationality, and language. Islam conceptualizes "
            "this brotherhood not as a casual association, but as an organic physiological system governed by Tarahum "
            "(mutual mercy) and Ta'atuf (active mutual support). When any member experiences distress, the entire community "
            "is religiously obligated to mobilize relief, sympathy, and practical solidarity."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**Hadith Citation (Sahih Muslim):**\n\n"
            "«مَثَلُ الْمُؤْمِنِينَ فِي تَوَادِّهِمْ وَتَرَاحُمِهِمْ وَتَعَاطُفِهِمْ مَثَلُ الْجَسَدِ إِذَا اشْتَكَى مِنْهُ عُضْوٌ تَدَاعَى لَهُ سَائِرُ الْجَسَدِ بِالسَّهَرِ وَالْحُمَّى»\n\n"
            "> \"The similitude of believers with regard to mutual love, affection, fellow-feeling is that of one body; "
            "when any limb of it aches, the whole body aches, because of sleeplessness and fever.\"\n\n"
            "*Source: Sahih Muslim (Book 45, Hadith 2586; also recorded in Sahih al-Bukhari #6011).*"
        ),
        "deep_explanation": (
            "This Hadith establishes a revolutionary standard for social responsibility in Islam:\n\n"
            "1. **Interdependence:** No Muslim is an isolated island. The joy of one believer is the joy of all; the pain of one is the pain of all.\n"
            "2. **Active Empathy (Ta'atuf):** Passive emotional sadness is insufficient. Believers must actively respond to relieve hardship, just as the physiological system dispatches white blood cells and elevated body temperature to heal a physical wound.\n"
            "3. **Universal Brotherhood:** This organic bond dissolves tribalism, racism, and socioeconomic status, binding all members into an indissoluble fraternity.\n"
            "4. **The Dual Symptoms of Care:** The Hadith highlights sleeplessness (vigilance and acute concern) and fever (mobilization of communal energy and resources) as biological proofs of true spiritual health."
        ),
        "step_process": {
            "title": "The Triadic Virtues of Communal Health in the Hadith",
            "steps": [
                {"step": 1, "title": "Tawadd (Mutual Love)", "description": "Sincere, intentional spiritual affection that binds hearts and inspires proactive goodwill."},
                {"step": 2, "title": "Tarahum (Mutual Mercy)", "description": "Compassionate tenderness that forgives shortcomings, protects vulnerabilities, and overlooks faults."},
                {"step": 3, "title": "Ta'atuf (Active Solidarity)", "description": "Tangible mobilization of hands, finances, and advocacy to lift the afflicted brother or sister."}
            ]
        },
        "worked_example": {
            "scenario": (
                "Ali is a Grade 9 student who is usually cheerful, but lately he sits alone during break time looking visibly stressed "
                "because his family is undergoing severe financial hardship. His classmate, Ibrahim, notices this change. Remembering "
                "the Hadith of the single body, Ibrahim refuses to ignore Ali or play games exclusively with his usual friends. Ibrahim sits "
                "with Ali, shares his lunch, and offers words of comfort. Ibrahim tells his friends: 'We cannot enjoy our games while our "
                "brother Ali is hurting. We are like one body, and we must help him feel supported.'"
            ),
            "analysis": (
                "Ibrahim demonstrates authentic Islamic social empathy. Instead of being indifferent to a peer's misery, he translates "
                "the theoretical 'one body' doctrine into immediate social action: companionship, resource sharing, and peer advocacy."
            ),
            "takeaway": "True faith demands that we treat a classmate's emotional or financial pain as our personal responsibility."
        },
        "real_world_application": (
            "Look around your school and classroom. Identify any student who is being excluded, bullied, or going through a tough time "
            "(such as failing an examination, dealing with bereavement, or coping with illness). Take the initiative to demonstrate "
            "fellow-feeling: sit beside them at lunch, offer help with difficult homework, or simply greet them warmly with sincere Salam. "
            "This transforms prophetic wisdom from textbook theory into living school reality."
        ),
        "reflection": (
            "How would our school environment change if every single student applied the 'one body' analogy to their daily interactions? "
            "What spiritual and social dangers emerge when people develop an attitude of 'that person's problems are none of my business'?"
        ),
        "misconception": {
            "misconception": "Thinking that empathy simply means feeling sorry in your mind without taking any practical action.",
            "correction": "The Hadith specifies fever and sleeplessness—active physiological responses that mobilize the entire body. In Islam, empathy is incomplete until it manifests in concrete assistance, verbal comfort, or material support."
        },
        "mcq": {
            "question": "According to the Hadith recorded by Imam Muslim, what does the entire body experience when a single limb aches?",
            "options": [
                "A) Complete indifference and uninterrupted sleep",
                "B) Irritation and anger at the aching limb for causing trouble",
                "C) Sleeplessness and fever in systemic solidarity with the limb",
                "D) A temporary shutdown of all other sensory functions"
            ],
            "answer": "C",
            "explanation": "The Hadith states that when any limb aches, the whole body responds with sleeplessness (vigilant concern) and fever (mobilized defense and support), illustrating the deep empathy and collective responsibility that must exist among believers."
        },
        "summary": {
            "key_points": [
                "Islam teaches that all believers are bound together like a single living body in mutual love and mercy.",
                "Individual distress is a collective concern; no Muslim can remain indifferent to a brother's or sister's suffering.",
                "True Islamic brotherhood is evidenced through active empathy, practical assistance, and shared burdens."
            ],
            "vocabulary": [
                {"term": "Ummah", "definition": "The global community of Muslim believers bound by shared faith in Allah."},
                {"term": "Tarahum", "definition": "Mutual mercy, compassion, and tenderness of heart exhibited between believers."},
                {"term": "Ta'atuf", "definition": "Active fellow-feeling, mutual kindness, and practical mobilization to help those in distress."},
                {"term": "Similitude (Mathal)", "definition": "A comparative analogy or metaphor used in prophetic speech to illustrate spiritual truths."}
            ]
        },
        "exit_ticket": "Write down one practical way you can show 'sleeplessness and fever' (active concern and tangible support) for a classmate who is struggling academically or socially this week."
    },

    # ─── LESSON 2.2.2 ───────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Lesson 2.2.2: Unity in school and community",
        "unit_description": "Applies the Quranic mandate of Ta'awun (cooperation in righteousness) and the body-analogy Hadith to eradicate school cliquishness, promote inclusion, and foster collective student success.",
        "lesson_title": "Unity in School and Community",
        "diagram_title": "Cliquish & Divided vs United & Cooperative School Community Matrix",
        "svg_fn": get_svg_lesson_2,
        "image": {
            "title": "Interior of Abu Bakr Mosque — Community Cohesion",
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Abu_Bakr_Mosque%2C_Medina_%28Interior%29.jpg",
            "caption": "Community gathering and cooperative prayer, symbolizing egalitarian solidarity and mutual care.",
            "author": "Wikimedia Commons Contributor",
            "licensing": "CC-BY-SA-4.0",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Cooperation in Goodness (Ta'awun) — Quran & Sunnah",
            "youtube_id": "Rywpb0ZYR3c",
            "description": "Understanding the command of Surah Al-Ma'idah (5:2) to cooperate in goodness and reject tribal and social exclusion."
        },
        "inquiry_question": "How do we apply the concept of Muslim unity to our daily school and neighborhood environments?",
        "connection": "Have you ever watched a football team play? If the defenders refuse to pass to the midfielders, or if the striker laughs when the goalkeeper makes a mistake, the team will lose. They must play as one unit, supporting each other's weaknesses. In the same way, the Muslim community in your school and neighborhood must act as a team, building strength through cooperation and mutual respect.",
        "goals": [
            "Analyze the Quranic foundation of community cooperation (Ta'awun) from Surah Al-Ma'idah 5:2.",
            "Contrast the toxic traits of cliquish, divided schools with the attributes of inclusive, cooperative communities.",
            "Formulate concrete strategies to integrate marginalized and isolated students into classroom activities."
        ],
        "authoritative_concept": (
            "Community Cooperation (Ta'awun) is the practical operational engine that actualizes the unity described in the Hadith. "
            "Islam demands active collaboration in righteousness, civic service, and academic excellence, while strictly forbidding "
            "collusion in sin, bullying, and tribal discrimination. Inclusivity ensures that every member of the school and neighborhood "
            "feels valued, protected, and empowered."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**Quranic Foundation (Surah Al-Ma'idah, 5:2):**\n\n"
            "«وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ ۚ وَاتَّقُوا اللَّهَ»\n\n"
            "> \"And cooperate in righteousness and piety, but do not cooperate in sin and aggression. And fear Allah...\"\n\n"
            "*Connection: Cooperation in virtue (Ta'awun) is the practical mechanism that maintains the health of the single body described in the Hadith of Sahih Muslim.*"
        ),
        "deep_explanation": (
            "To build an upright and cohesive school community, students must focus on three core practices:\n\n"
            "1. **Dismantling Cliquishness:** Actively refusing to form closed, elitist cliques based on family wealth, ethnic background, or social popularity. Cliquishness divides the single body into competing, hostile fragments.\n"
            "2. **Collective Problem Solving:** Establishing peer-tutoring networks, organizing joint schoolyard cleanups, and sharing revision textbooks with less fortunate students.\n"
            "3. **Mutual Celebration:** Sincerely rejoicing in a classmate's high marks or athletic accomplishments rather than secretly harboring envy (Hasad).\n"
            "4. **Inclusive Welcome:** Proactively inviting new or quiet students into study groups and sports teams, ensuring zero students face isolation."
        ),
        "comparison_table": {
            "title": "Contrasting School Community Environments",
            "headers": ["Dimension", "Cliquish & Divided School", "United & Cooperative School (Islamic Model)"],
            "rows": [
                ["Social Structure", "Exclusive cliques based on wealth, tribe, or popularity", "Inclusive, open circles welcoming every student warmly"],
                ["Academic Mindset", "Hoarding study notes; rejoicing when others fail exams", "Peer-tutoring circles; sharing revision summaries openly"],
                ["Reaction to Errors", "Public mockery, gossip, and filming embarrassing clips", "Constructive, private encouragement preserving peer dignity"],
                ["Dispute Handling", "Prolonged boycotts, silent treatment, and grudge-holding", "Reconciliation within 3 days; proactive exchange of Salam"],
                ["Community Impact", "Widespread anxiety, low self-esteem, and social fracture", "High collective academic achievement, joy, and peace"]
            ]
        },
        "worked_example": {
            "scenario": (
                "The Grade 9 class is assigned a major community service project: cleaning up the school compound and planting indigenous "
                "trees. Some students from popular groups complain and refuse to work with students from other neighborhoods. Halima steps "
                "forward and says: 'Remember what we learned about being like one body. If we divide ourselves and refuse to work together, "
                "our compound will remain dirty and we will fail our project. Let us mix our groups, share the shovels fairly, and help "
                "those who find digging difficult.' Inspired by her leadership, the class unites and finishes ahead of schedule."
            ),
            "analysis": (
                "Halima acts as a unifying moral leader. By invoking the Islamic principle of the single body, she reframes the project "
                "from an inconvenient chore into an act of righteous cooperation (Ta'awun), successfully dismantling social barriers."
            ),
            "takeaway": "True leadership in Islam means breaking down social cliques and inspiring collective action for the common good."
        },
        "real_world_application": (
            "Design a 'Classroom Unity Pledge.' Collaborate with your classmates to write down three rules that guarantee inclusion: "
            "1. No student ever sits alone at lunch or during break time; 2. We never mock someone who answers a teacher's question incorrectly; "
            "and 3. We automatically share class notes with anyone absent due to sickness. Display this pledge on your classroom wall."
        ),
        "reflection": (
            "Why does dividing into closed, exclusive cliques undermine the spiritual unity of a Muslim community? "
            "How does working shoulder-to-shoulder on humble physical tasks (like cleaning or tree planting) forge lasting friendships?"
        ),
        "misconception": {
            "misconception": "Believing that cooperation means you must always support your friends, even when they are breaking rules or bullying peers.",
            "correction": "Surah Al-Ma'idah 5:2 sets an absolute ethical boundary: 'Cooperate in righteousness and piety, but DO NOT cooperate in sin and aggression.' Supporting a friend doing wrong means advising them to stop, not aiding their wrongdoing."
        },
        "mcq": {
            "question": "Which of the following actions directly fulfills the Islamic command of Ta'awun (cooperation in righteousness) in a school environment?",
            "options": [
                "A) Forming an exclusive club that only admits students from your own neighborhood",
                "B) Organizing a peer-study group to help classmates who are struggling with mathematics",
                "C) Keeping your study notes secret so that you can score the highest grade in the class",
                "D) Ignoring a classmate who is being excluded because it is not your personal responsibility"
            ],
            "answer": "B",
            "explanation": "Organizing peer-study groups embodies Ta'awun by collaborating in intellectual and moral growth, supporting vulnerable learners, and building collective academic excellence."
        },
        "summary": {
            "key_points": [
                "Unity is built through active, daily cooperation in righteous deeds (Ta'awun).",
                "Islam prohibits exclusive cliquishness, tribalism, and social isolation, demanding open inclusivity.",
                "True loyalty to peers means encouraging them in moral goodness while refusing to join in sin or bullying."
            ],
            "vocabulary": [
                {"term": "Ta‘awun", "definition": "Active cooperation in good deeds, piety, and beneficial civic action."},
                {"term": "Birr", "definition": "Comprehensive righteousness, moral integrity, and charitable conduct."},
                {"term": "Udwân", "definition": "Aggression, hostility, and injustice prohibited by Allah."},
                {"term": "Inclusivity", "definition": "The deliberate practice of ensuring all individuals feel welcomed, respected, and supported."}
            ]
        },
        "exit_ticket": "Write down one personal commitment you will make this week to ensure no classmate feels left out or ignored during break time."
    },

    # ─── LESSON 2.2.3 ───────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Lesson 2.2.3: Ill motives: identifying the harms",
        "unit_description": "Examines the severe prophetic prohibitions in Sahih al-Bukhari against suspicion, fault-finding, spying, Najsh (deception), jealousy, hatred, and social desertion.",
        "lesson_title": "Ill Motives: Identifying the Harms",
        "diagram_title": "The 6 Prohibited Ill Motives & Destructive Social Chain Flowchart",
        "svg_fn": get_svg_lesson_3,
        "image": {
            "title": "Classical Sahih al-Bukhari Manuscript Compilation",
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Sahih_al-Bukhari%2C_1890s_%282024-04-02%29.jpg",
            "caption": "Historical manuscript copy of Sahih al-Bukhari containing the authoritative prophetic prohibitions against ill motives.",
            "author": "Ottoman Calligrapher (1890s)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Dangers of Envy, Suspicion and Spying in Islam",
            "youtube_id": "BfE7vM4P6b4",
            "description": "Analysis of the spiritual diseases that rot communal harmony from within and how the Prophet (PBUH) guided believers to root them out."
        },
        "inquiry_question": "What are the seven destructive social behaviors prohibited in the Hadith, and how do they ruin relationships?",
        "connection": "Imagine a beautifully built wooden house. It looks strong and grand, but inside the walls, termites are silently eating the timber. From the outside, everything looks fine, but eventually, the entire house collapses without warning. In our social lives, 'ill motives' like jealousy, hatred, and suspicion are like those spiritual termites. They silently destroy the foundations of our families and communities until they collapse. Let's read the Prophet’s (PBUH) warning against these internal dangers.",
        "goals": [
            "Identify and define the key prohibited vices listed in the Hadith of Sahih al-Bukhari.",
            "Trace the psychological and social chain reaction from internal suspicion (Zann) to open desertion (Tadabur).",
            "Understand the broader ethical definition of Najsh as manipulative exploitation and deceit."
        ],
        "authoritative_concept": (
            "Ill Motives (Amrad al-Qulub) are destructive internal vices—suspicion, jealousy, hatred—that inevitably manifest in "
            "toxic social behaviors: spying, fault-finding, market deception, and interpersonal boycotts. The Prophet (PBUH) diagnosed "
            "these attitudes as spiritual termites that dismantle brotherhood (Ukhuwwah) from within, commanding believers to actively "
            "police their thoughts and cultivate clean hearts."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**Hadith Citation (Sahih al-Bukhari):**\n\n"
            "«إِيَّاكُمْ وَالظَّنَّ، فَإِنَّ الظَّنَّ أَكْذَبُ الْحَدِيثِ، وَلَا تَحَسَّسُوا، وَلَا تَجَسَّسُوا، وَلَا تَنَاجَشُوا، وَلَا تَحَاسَدُوا، وَلَا تَبَاغَضُوا، وَلَا تَدَابَرُوا، وَكُونُوا عِبَادَ اللَّهِ إِخْوَانًا»\n\n"
            "> \"Beware of suspicion, for suspicion is the worst of false tales, and do not look for others’ faults, "
            "and do not spy on one another, and do not practise Najsh (to offer high price for something, in order to allure "
            "a person who is interested in it), and do not be jealous of one another and do not hate one another, "
            "and do not desert (stop talking to) one another. And O, Allah’s worshipers! Be brothers!\"\n\n"
            "*Source: Sahih al-Bukhari (Book 78, Hadith 6064; also recorded in Sahih Muslim #2563).*"
        ),
        "deep_explanation": (
            "The Hadith lists several prohibited behaviors that act as 'termites' undermining communal brotherhood:\n\n"
            "1. **Suspicion (Zann):** Making unfounded negative assumptions about others' intentions and accepting unverified rumors as truth.\n"
            "2. **Fault-Finding (Tahassus):** Inquisitively hunting for flaws, eavesdropping, or searching to uncover peers' hidden mistakes.\n"
            "3. **Spying (Tajassus):** Prying into others' private affairs, desks, and personal diaries.\n"
            "4. **Najsh (Deception in Trade):** Artificially raising bid prices to trick buyers; broadly encompasses all deceptive manipulation and unfair dealings.\n"
            "5. **Jealousy (Hasad):** Resenting another's blessings and wishing that their wealth, intelligence, or happiness be stripped away.\n"
            "6. **Hatred (Bughd):** Harboring malice, grudge, and bitter animosity in the heart.\n"
            "7. **Deserting (Tadabur):** Severing communication, turning one's back, and boycotting a brother or sister for more than three days."
        ),
        "step_process": {
            "title": "The Path of Social Destruction: The 5 Stages of Relational Breakdown",
            "steps": [
                {"step": 1, "title": "Suspicion (Zann)", "description": "Harboring baseless negative assumptions in the mind."},
                {"step": 2, "title": "Spying & Fault-Finding (Tajassus)", "description": "Investigating and snooping to confirm one's suspicions."},
                {"step": 3, "title": "Deception & Envy (Najsh & Hasad)", "description": "Manipulating peers and resenting their blessings and successes."},
                {"step": 4, "title": "Hatred & Rancor (Bughd)", "description": "Hardening of the heart into active hostility and malice."},
                {"step": 5, "title": "Desertion (Tadabur)", "description": "Complete social boycott, broken relationships, and refusal of Salam."}
            ]
        },
        "worked_example": {
            "scenario": (
                "Zainab sees her friend Fatima talking quietly to a new student during lunch. Zainab immediately thinks: 'Fatima is gossiping "
                "about me and trying to replace me' (Suspicion / Zann). Later, she checks Fatima's open desk and asks others what Fatima was "
                "saying (Spying / Tajassus). Zainab feels burning anger and ignores Fatima completely when Fatima greets her with Salam (Deserting / Tadabur). "
                "Zainab's mother reminds her: 'The Prophet (PBUH) warned that suspicion is the worst of false tales. By letting baseless "
                "thoughts grow, you destroyed a beautiful friendship over a misunderstanding. Go and greet her with a pure heart.'"
            ),
            "analysis": (
                "Zainab illustrates how unchecked suspicion rapidly cascades into snooping and social desertion. Had she applied the "
                "prophetic filter at stage 1, the friendship would have been preserved."
            ),
            "takeaway": "Never allow unverified negative thoughts to dictate your emotional attitudes or actions toward peers."
        },
        "real_world_application": (
            "Apply the 'Three-Day Reconciliation Rule' established in Islamic law. If you have had an argument with a friend or family member "
            "and have stopped speaking to them (deserting), make the conscious effort to break the silence within three days. Reach out with "
            "a sincere text, a warm smile, or a heartfelt Salam. The one who initiates peace earns the greatest reward before Allah."
        ),
        "reflection": (
            "Why do you think the Prophet (PBUH) described suspicion as 'the worst of false tales'? "
            "How does harboring suspicion warp our perception of reality and create enemies where none exist?"
        ),
        "misconception": {
            "misconception": "Thinking that Najsh only applies to ancient camel or livestock auctions.",
            "correction": "Najsh represents any form of artificial manipulation, deceptive hype, or dishonest bidding used to trick peers for personal gain, whether in physical trade, online marketplaces, or school swaps."
        },
        "mcq": {
            "question": "What does the Islamic term Najsh refer to in the context of commercial and social ethics in the Hadith?",
            "options": [
                "A) Secretly eavesdropping on a neighbor's private conversation",
                "B) Artificially offering a high price for something to deceive a potential buyer into paying more",
                "C) Wishing that a classmate's achievements and talents are taken away from them",
                "D) Refusing to speak to a family member or peer after a personal argument"
            ],
            "answer": "B",
            "explanation": "Najsh is an exploitative trade practice where a person bids a high price on an item with no intention to buy, merely to trick another genuine buyer into overpaying. It stands as a universal prohibition against trickery and manipulation."
        },
        "summary": {
            "key_points": [
                "The Hadith in Sahih al-Bukhari prohibits seven destructive vices that act as spiritual termites destroying community trust.",
                "Suspicion (Zann) is condemned as the most deceitful speech because it constructs false accusations upon groundless paranoia.",
                "Muslims are commanded to cultivate clean hearts and live as compassionate, supportive brothers and sisters."
            ],
            "vocabulary": [
                {"term": "Zann", "definition": "Negative, groundless suspicion or conjecture treated as established truth."},
                {"term": "Tajassus", "definition": "Spying or intruding into others' private matters and searching for faults."},
                {"term": "Najsh", "definition": "Fraudulent price-hiking or deceptive hype to exploit and deceive buyers."},
                {"term": "Hasad", "definition": "Destructive envy; wishing for the removal of another person's blessings."},
                {"term": "Tadabur", "definition": "Severing relationships, boycotting, and turning one's back on fellow believers."}
            ]
        },
        "exit_ticket": "Name two behaviors from this lesson's Hadith that are most likely to destroy trust in a peer friendship, and state how you will avoid them."
    },

    # ─── LESSON 2.2.4 ───────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Lesson 2.2.4: Ill motives in digital life",
        "unit_description": "Translates the classical prophetic prohibitions against suspicion, cyber-spying (Tajassus), online fault-finding, and WhatsApp exclusion into modern digital communication ethics.",
        "lesson_title": "Ill Motives in Digital Life",
        "diagram_title": "Social Media & Digital Communication Ethical Filter Protocol",
        "svg_fn": get_svg_lesson_4,
        "image": {
            "title": "Modern Mobile Technology and Digital Communications",
            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Smartphone_use_in_public.jpg",
            "caption": "Modern handheld technology connecting global networks, requiring vigilant adherence to Islamic digital ethics.",
            "author": "Wikimedia Commons Contributor",
            "licensing": "CC-BY-SA-4.0",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Islamic Digital Ethics: Social Media, Spying & Rumors",
            "youtube_id": "BfE7vM4P6b4",
            "description": "How the rules of Surah Al-Hujurat and Sahih al-Bukhari govern screenshots, WhatsApp groups, and online privacy."
        },
        "inquiry_question": "How do online rumors, cyber-spying, and WhatsApp exclusion violate the Prophet's warnings against ill motives?",
        "connection": "Imagine a classroom where students write mean secrets about a classmate on a slip of paper and pass it around during class. Now imagine that instead of a paper slip, the secret is posted on a WhatsApp group with 100 students, and within minutes, it is screenshotted and shared across the entire school. The damage is now 100 times worse. Technology has changed how we communicate, but it has also magnified the reach of our 'spiritual termites.' Let's examine how the Prophet’s (PBUH) ancient warnings apply directly to our screens today.",
        "goals": [
            "Demonstrate how classical prohibitions of Zann, Tajassus, and Tadabur manifest in cyberspace.",
            "Analyze the severe moral consequences of cyber-bullying, screen recording, and unauthorized screenshot leaks.",
            "Apply the 3-Step Islamic Digital Communication Ethical Filter before hitting 'Share' or 'Send'."
        ],
        "authoritative_concept": (
            "Islamic Digital Ethics governs the application of Shariah moral principles (truthfulness, privacy, verification, and honor) "
            "to digital platforms, social media, and virtual communications. In the digital age, ancient vices have acquired new tools: "
            "Tajassus manifests as cyber-stalking and hacking; Zann fuels viral misinformation; and Tadabur takes the form of weaponized "
            "group chat exclusion and cyber-bullying."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**Quranic Foundation (Surah Al-Hujurat, 49:12):**\n\n"
            "«يَا أَيُّهَا الَّذِينَ آمَنُوا اجْتَنِبُوا كَثِيرًا مِّنَ الظَّنِّ إِنَّ بَعْضَ الظَّنِّ إِثْمٌ ۖ وَلَا تَجَسَّسُوا وَلَا يَغْتَب بَّعْضُكُم بَعْضًا»\n\n"
            "> \"O you who have believed, avoid much of suspicion. Indeed, some suspicion is sin. And do not spy or backbite each other...\"\n\n"
            "*Unified Standard: The prohibition against spying (Tajassus) in the Hadith and Quran applies identically to physical spaces and digital smartphones.*"
        ),
        "deep_explanation": (
            "The prohibitions in the Hadith map directly to digital behaviors:\n\n"
            "1. **Digital Suspicion (Zann):** Interpreting a delayed reply or a read-receipt (blue ticks) as an intentional insult or plot.\n"
            "2. **Cyber-Spying (Tajassus):** Peeking at unlocked phones, tracking classmates' location without permission, or snooping through private chats.\n"
            "3. **Digital Fault-Finding:** Archiving embarrassing old photos or taking unauthorized screenshots to humiliate a classmate in group chats.\n"
            "4. **Digital Najsh:** Using fake social accounts or bots to artificially boost likes, post fake reviews, or deceive peers.\n"
            "5. **WhatsApp Exclusion (Tadabur):** Creating splinter group chats to deliberately alienate specific classmates, or weaponizing silent blocking to punish peers."
        ),
        "step_process": {
            "title": "The 3-Gate Prophetic Digital Filter Before Sharing",
            "steps": [
                {"step": 1, "title": "Gate 1: Verification (Tabayyun)", "description": "Is this post verified fact or sensational rumor? (Surah Al-Hujurat 49:6)."},
                {"step": 2, "title": "Gate 2: Privacy (Sitr)", "description": "Does this expose someone's private fault or violate their digital privacy? (Anti-Tajassus)."},
                {"step": 3, "title": "Gate 3: Benevolence (Ihsan)", "description": "Will this forward build unity or spread discord and ridicule? (Anti-Bughd)."}
            ]
        },
        "worked_example": {
            "scenario": (
                "Fatima sees an urgent message in a class WhatsApp group alleging that her classmate Amina was caught cheating in an exam. "
                "The message urges: 'Share this with everyone!' Fatima feels tempted to forward it to her friends. However, she pauses and "
                "remembers the Hadith on avoiding suspicion and spying. She reflects: 'This might be mere suspicion, which the Prophet called "
                "the worst of false tales. If I forward this, I am spreading a rumor and humiliating my sister.' Fatima deletes the message "
                "and private-messages the sender: 'Please let us delete this immediately. We must verify before sharing and protect our sister's dignity.'"
            ),
            "analysis": (
                "Fatima acts as a shield for her peer's dignity. By applying the digital verification filter, she terminates the viral spread "
                "of an unverified allegation and counsels the sender in accordance with prophetic etiquette."
            ),
            "takeaway": "Moral courage in the digital age means breaking the chain of viral gossip and refusing to forward unverified allegations."
        },
        "real_world_application": (
            "Perform a 'Digital Clean-up.' Go through your chat groups and social media accounts. If you belong to any group chat that exists "
            "solely to mock teachers or peers, exit that group immediately. If you have blocked a classmate out of petty anger, unblock them "
            "and send a peaceful Salam to clear the air instead of 'deserting' them through silent blocking."
        ),
        "reflection": (
            "Why is it often psychologically easier to be rude, sarcastic, or suspicious behind a screen than face-to-face? "
            "How does physical distance lower our moral guard, and how does cyber-bullying violate the 'one body' principle?"
        ),
        "misconception": {
            "misconception": "Believing that forwarding an unverified rumor is harmless because you did not write the original message.",
            "correction": "The Prophet (PBUH) declared: 'It is enough of a lie for a person to narrate everything he hears' (Sahih Muslim). Forwarding unverified rumors makes you an active co-author of slander."
        },
        "mcq": {
            "question": "Which of the following digital actions directly violates the Prophet's prohibition against Tajassus (spying)?",
            "options": [
                "A) Reporting an offensive account to a platform administrator",
                "B) Leaving a group chat that has become toxic and disrespectful",
                "C) Secretly scrolling through your classmate's private text messages while their phone is left unlocked",
                "D) Sending a polite message to reconcile with a classmate after a misunderstanding"
            ],
            "answer": "C",
            "explanation": "Tajassus is defined as prying or intruding into others' private matters. Secretly reading someone's personal phone messages without explicit consent is a direct physical and digital violation of this prohibition."
        },
        "summary": {
            "key_points": [
                "Islamic moral principles apply equally to virtual environments, group chats, and social media platforms.",
                "Digital spying, stalking, leaked screenshots, and WhatsApp exclusion are modern forms of prohibited Tajassus and Tadabur.",
                "Applying the 3-Gate Ethical Filter (Verification, Privacy, Benevolence) protects individual dignity and community harmony."
            ],
            "vocabulary": [
                {"term": "Digital Ethics", "definition": "Ethical conduct and moral integrity applied to digital communications and virtual spaces."},
                {"term": "Cyber-spying", "definition": "Unlawfully accessing, monitoring, or reading another person's private electronic messages without consent."},
                {"term": "Sitr", "definition": "The Islamic virtue of concealing the private flaws and shortcomings of others."},
                {"term": "Tabayyun", "definition": "The moral duty to rigorously investigate and verify information before accepting or sharing it."}
            ]
        },
        "exit_ticket": "Write down one rule you will follow on your smartphone to ensure your messaging habits build unity rather than division."
    },

    # ─── LESSON 2.2.5 ───────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Lesson 2.2.5: Comparing the two Hadith",
        "unit_description": "Thematic and comparative synthesis of the Hadith on Unity (Sahih Muslim) and the Hadith on Ill Motives (Sahih al-Bukhari), demonstrating the dual pillars of virtue cultivation and vice elimination.",
        "lesson_title": "Comparing the Two Hadith",
        "diagram_title": "Dual Pillars of Social Harmony (Positive Unity vs Proactive Avoidance of Ill Motives)",
        "svg_fn": get_svg_lesson_5,
        "image": {
            "title": "Hadith Manuscript in Nasta'liq Script (1559 CE)",
            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f4/A_manuscript_about_hadiths%2C_in_nasta%27liq%2C_1559.jpg",
            "caption": "Classical 16th-century manuscript illustrating the dual balance of prophetic virtues and legal prohibitions.",
            "author": "Persian Calligrapher (1559 CE)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Takhliyah and Tahliyah: Cleansing the Heart and Planting Virtues",
            "youtube_id": "BfE7vM4P6b4",
            "description": "How Islamic scholars synthesized positive commands of love with negative prohibitions against vice to achieve balance."
        },
        "inquiry_question": "How do positive community-builders compare with destructive ill motives, and how do they balance each other?",
        "connection": "Imagine a garden. To have a beautiful harvest, you must do two things: you must plant good seeds (sunflowers, roses, fruits) and you must actively pull out the weeds that steal the nutrients. If you only plant flowers but never pull the weeds, the weeds will take over and kill the garden. In our spiritual lives, the Hadith on Unity tells us what 'flowers' to plant, while the Hadith on Ill Motives tells us what 'weeds' to pull out. Let's compare these two teachings to see how they work together.",
        "goals": [
            "Compare the pedagogical approaches of the Hadith on Unity (Muslim) and the Hadith on Ill Motives (Bukhari).",
            "Explain the Islamic ethical paradigm of Takhliyah (cleansing vices) and Tahliyah (adorning virtues).",
            "Synthesize both Hadiths into a unified moral framework for sustainable community harmony."
        ],
        "authoritative_concept": (
            "Complementary Moral Architecture in Islam requires both the cultivation of virtues (Tahliyah) and the active elimination "
            "of vices (Takhliyah). The Hadith on Unity provides the positive blueprint of mutual love, mercy, and solidarity, while the "
            "Hadith on Ill Motives erects a protective fence prohibiting behaviors that destroy interpersonal trust. True brotherhood "
            "(Ukhuwwah) cannot survive without both."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**The Two Foundational Traditions:**\n\n"
            "1. **The Positive Builder (Sahih Muslim #2586):**\n"
            "> \"The similitude of believers with regard to mutual love, affection, fellow-feeling is that of one body; "
            "when any limb of it aches, the whole body aches, because of sleeplessness and fever.\"\n\n"
            "2. **The Preventive Shield (Sahih al-Bukhari #6064):**\n"
            "> \"Beware of suspicion... and do not look for others' faults, and do not spy... and do not be jealous... "
            "And O, Allah's worshipers! Be brothers!\"\n\n"
            "*Convergence: Both Hadiths culminate in the identical divine command: to live as sincere, loving brothers and sisters.*"
        ),
        "deep_explanation": (
            "By placing these two Hadiths side by side, we observe a comprehensive system of social ethics:\n\n"
            "1. **The Positive Command (Tahliyah):** Cultivate love (Mawaddah), mercy (Tarahum), and active fellow-feeling (Ta'atuf). These represent planting the 'flowers' of community life.\n"
            "2. **The Preventive Prohibition (Takhliyah):** Actively suppress suspicion, spying, commercial deceit, envy, hatred, and desertion. These represent pulling out the 'weeds'.\n"
            "3. **Organic Equilibrium:** Just as a physical body cannot survive infection without an active immune system, the Ummah cannot unite without expelling internal malice.\n"
            "4. **The Ultimate Goal:** Both Hadiths culminate in the divine mandate: 'Be brothers!' Unity is impossible without purifying the heart first."
        ),
        "comparison_table": {
            "title": "Comparative Analytical Framework of the Two Hadith",
            "headers": ["Dimension", "Hadith on Unity (Sahih Muslim)", "Hadith on Ill Motives (Sahih al-Bukhari)"],
            "rows": [
                ["Pedagogical Focus", "Prescriptive: Commands positive virtues (love, mercy, solidarity)", "Proscriptive: Prohibits destructive vices (suspicion, spying, envy)"],
                ["Primary Metaphor", "Biological organism: interconnected human body responding to pain", "Social hygiene: eradication of spiritual termites and false claims"],
                ["Psychological Domain", "Outward emotional empathy, mutual sympathy, and active aid", "Inward cognitive discipline, cleansing the heart of secret malice"],
                ["Ethical Paradigm", "Tahliyah: Adorning the soul with compassionate deeds", "Takhliyah: Cleansing the heart of hostility, deceit, and suspicion"],
                ["Ultimate Target", "Harmonious collective mobilization under shared faith", "Preservation of interpersonal trust and protection of peer dignity"]
            ]
        },
        "worked_example": {
            "scenario": (
                "During an IRE class discussion, Yusuf says: 'I am a good Muslim because I never fight with anyone, I mind my own business, "
                "and I don't spread rumors. I don't need to join volunteer projects or help classmates as long as I don't hurt them.' "
                "Mr. Bilal smiles and replies: 'Yusuf, you are doing a great job of pulling out the weeds (avoiding harm), but you have not "
                "planted any flowers yet. The Hadith on Unity says that if any part of the body hurts, the whole body must respond with fever "
                "and sleeplessness. Minding your own business is safe, but active brotherhood requires sharing burdens and comforting those in pain.'"
            ),
            "analysis": (
                "Mr. Bilal demonstrates that passive neutrality is incomplete in Islamic morality. Refraining from evil fulfills the preventive "
                "command (Bukhari), but true faith requires positive altruism and active care (Muslim)."
            ),
            "takeaway": "Islamic virtue is not merely the absence of wrongdoing; it is the active presence of loving service and community care."
        },
        "real_world_application": (
            "Perform a 'Weed and Flower Audit' of your daily habits. On a clean sheet of paper, write down one 'weed' (such as harboring "
            "negative suspicion about a peer's motives) that you will actively pull out of your heart today, and one 'flower' (such as "
            "sharing your study notes or helping an excluded student) that you will actively plant."
        ),
        "reflection": (
            "Why is it impossible to sustain a united community if members perform all external religious rituals but harbor jealousy and hatred? "
            "How does removing suspicion create space in our hearts for sincere love and mercy?"
        ),
        "misconception": {
            "misconception": "Believing that being a good believer simply means 'minding your own business' in complete isolation.",
            "correction": "While avoiding intrusive nosiness (Tajassus) is obligatory, total social isolation violates the Hadith of Unity. The Prophet (PBUH) stated that the believer who mixes with people and patiently endures difficulties has greater reward than one who isolates."
        },
        "mcq": {
            "question": "How do the Hadith on Unity and the Hadith on Ill Motives complement each other in building an upright society?",
            "options": [
                "A) They represent contradictory philosophies that cannot be reconciled in Islamic law",
                "B) One teaches us how to isolate ourselves, while the other teaches us how to fight",
                "C) One builds unity by promoting active mercy, while the other protects unity by prohibiting destructive social vices",
                "D) They suggest that only scholars have the responsibility to maintain peace in society"
            ],
            "answer": "C",
            "explanation": "The two Hadiths work together: the Hadith on Unity provides the positive vision of active empathy, while the Hadith on Ill Motives provides the preventive warnings against behaviors that destroy relationships, both working toward true brotherhood."
        },
        "summary": {
            "key_points": [
                "Islamic social ethics requires both doing good (Tahliyah) and preventing harm (Takhliyah).",
                "True brotherhood is achieved by cultivating mercy and actively avoiding suspicion and envy.",
                "The ultimate goal of both Hadiths is a peaceful, united, and God-conscious society."
            ],
            "vocabulary": [
                {"term": "Complementary", "definition": "Completing or mutually balancing two different aspects into a harmonious whole."},
                {"term": "Takhliyah", "definition": "The spiritual process of purifying the soul and community by eliminating vices."},
                {"term": "Tahliyah", "definition": "The spiritual process of adorning character with divine virtues and good deeds."},
                {"term": "Vice", "definition": "An immoral habit or destructive internal attitude that causes spiritual and social harm."}
            ]
        },
        "exit_ticket": "Explain in one sentence why a classroom cannot be truly united if students avoid fighting but continue to spread rumors."
    },

    # ─── LESSON 2.2.6 ───────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Lesson 2.2.6: Community conflict role-play",
        "unit_description": "Interactive simulation and structured mediation protocol for applying Quranic Tabayyun (verification) and Islah (reconciliation) to de-escalate and resolve peer conflicts.",
        "lesson_title": "Community Conflict Role-Play",
        "diagram_title": "4-Stage Reconciliation (Islah) Mediation Flowchart",
        "svg_fn": get_svg_lesson_6,
        "image": {
            "title": "The Prophet's Mosque Courtyard in Madinah",
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Masjid_Nabawi_The_Prophet%27s_Mosque%2C_Madina.jpg",
            "caption": "The Prophet's Mosque in Madinah, historically the premier center for community reconciliation and arbitration.",
            "author": "Wikimedia Commons Contributor",
            "licensing": "CC-BY-SA-4.0",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Conflict Resolution in Islam: The Principles of Islah",
            "youtube_id": "BfE7vM4P6b4",
            "description": "Step-by-step examination of Quranic arbitration, calming hostile parties, and restoring sincere brotherhood."
        },
        "inquiry_question": "How do we apply the rules of verification and non-harmful communication to resolve real conflicts in our school?",
        "connection": "Imagine two of your best friends are shouting at each other in the school hallway over something someone else said. Other students are gathering around, encouraging them to fight, while some are filming on their phones. What do you do? Do you walk away? Do you join the crowd? In this lesson, we will step into a realistic scenario and practice using the Prophet's guidance on verification, avoiding suspicion, and bringing hearts together to resolve conflicts peacefully.",
        "goals": [
            "Internalize the religious and civic obligation of conflict resolution (Islah) from Surah Al-Hujurat.",
            "Execute the 4-Stage Islamic Mediation Protocol to de-escalate interpersonal disputes.",
            "Apply Tabayyun (rigorous investigation) to neutralize rumors and verify facts before passing judgment."
        ],
        "authoritative_concept": (
            "Conflict Resolution (Islah dhat al-Bayn) is a profound moral and religious duty in Islam. The Quran commands believers "
            "to make peace between disputing parties with absolute justice and compassion. Mediators must employ Tabayyun (rigorous "
            "investigation of facts) to eliminate groundless rumors, prevent escalation, and facilitate sincere mutual forgiveness."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**Quranic Foundation (Surah Al-Hujurat, 49:9-10):**\n\n"
            "«وَإِن طَائِفَتَانِ مِنَ الْمُؤْمِنِينَ اقْتَتَلُوا فَأَصْلِحُوا بَيْنَهُمَا ۖ ... إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ فَأَصْلِحُوا بَيْنَ أَخَوَيْكُمْ ۚ وَاتَّقُوا اللَّهَ لَعَلَّكُمْ تُرْحَمُونَ»\n\n"
            "> \"And if two factions among the believers should fight, then make peace between them... indeed, Allah loves those who act justly. "
            "The believers are but brothers, so make peace between your brothers...\"\n\n"
            "**Hadith Foundation (Sahih al-Bukhari #481):**\n"
            "> \"The believer to the believer is like a building whose different parts reinforce each other.\""
        ),
        "deep_explanation": (
            "When resolving a conflict between friends or classmates, follow the structured 4-Stage Islamic Mediation Protocol:\n\n"
            "1. **De-escalate & Contain (Takhfif):** Calm the heated situation immediately, disperse cheering bystanders, and separate the parties to a safe, quiet space.\n"
            "2. **Verify (Tabayyun):** Hear each perspective without interruption. Ask: What actually occurred? Is this claim rooted in verified fact or unverified suspicion (Zann)? Inquire directly with teachers or primary sources.\n"
            "3. **Spiritual Mediation (Islah):** Remind both parties of their sacred brotherhood, citing the Hadith of the single body and the transient nature of worldly ego.\n"
            "4. **Restitution & Forgiveness (Sulh):** Guide the wrongdoer to offer a sincere, humble apology, and encourage the hurt party to accept with mercy and a handshake."
        ),
        "step_process": {
            "title": "The 4-Stage Islamic Mediation Protocol",
            "steps": [
                {"step": 1, "title": "De-escalate & Contain", "description": "Halt shouting, separate parties, disperse cheering crowds, and restore calm."},
                {"step": 2, "title": "Objective Verification (Tabayyun)", "description": "Investigate facts objectively, eliminate rumors, and verify at the source."},
                {"step": 3, "title": "Spiritual Mediation (Islah)", "description": "Invoke the 'One Body' Hadith and appeal to mutual brotherhood in faith."},
                {"step": 4, "title": "Restitution & Sulh", "description": "Facilitate sincere apologies, seal peace with Salam, and restore friendship."}
            ]
        },
        "worked_example": {
            "scenario": (
                "Hussein and Musa are screaming at each other near the lockers. Hussein shouts: 'Musa told the teacher that I copied his "
                "chemistry homework! He is a traitor and a spy!' Musa yells back: 'I never said a word! Hussein is slandering me!' "
                "Other students gather to film the fight. Khalid steps calmly between them, holds up his hands, and says: 'Brothers, stop! "
                "We are like one body; shouting in the hallway solves nothing.' Khalid walks them to a quiet bench. He applies Tabayyun by "
                "asking their chemistry teacher directly what occurred. The teacher clarifies she caught the identical answers herself during "
                "grading and Musa had nothing to do with it. Realizing his wrongful suspicion, Hussein apologizes sincerely to Musa, and they embrace in forgiveness."
            ),
            "analysis": (
                "Khalid exemplifies peer mediation. He halts the fight, removes the crowd, rejects speculative gossip, and verifies facts "
                "directly at the source, resolving a dangerous misunderstanding in minutes."
            ),
            "takeaway": "Effective mediation requires courage to intervene, emotional calmness, and rigorous reliance on verified facts."
        },
        "real_world_application": (
            "Act as a Classroom Peace Ambassador. If you notice two classmates who are 'deserting' each other (refusing to speak due to a "
            "misunderstanding), do not gossip about them. Approach each of them privately, listen with empathy, highlight their shared virtues, "
            "and facilitate a calm, mediated conversation over lunch to help them reconcile."
        ),
        "reflection": (
            "How does standing by and passively filming a school fight violate the Prophet's teaching that we are like 'one body'? "
            "Why does gossip and hearsay make a minor disagreement much harder to resolve?"
        ),
        "misconception": {
            "misconception": "Believing that mediation means taking the side of your closest friend regardless of who was at fault.",
            "correction": "The Quran commands absolute impartiality: 'Be persistently standing firm in justice, witnesses for Allah, even if it be against yourselves or parents and relatives' (Surah An-Nisa 4:135). Mediators must remain strictly just."
        },
        "mcq": {
            "question": "What is the first step an Islamic peer mediator should take when trying to resolve a conflict between two fighting classmates?",
            "options": [
                "A) Take a side immediately based on who is your closer friend",
                "B) De-escalate the anger and separate the parties to prevent immediate harm",
                "C) Encourage them to fight it out so that the conflict ends quickly",
                "D) Walk away and pretend you did not witness anything"
            ],
            "answer": "B",
            "explanation": "Before any fact verification or reconciliation can take place, the mediator must stop immediate confrontation and ensure safety by calming the situation, in accordance with the Islamic principle of preventing harm."
        },
        "summary": {
            "key_points": [
                "Conflict resolution (Islah) is an obligatory religious and moral value to preserve social cohesion.",
                "Verification (Tabayyun) prevents rumors and groundless suspicion from escalating into feuds.",
                "Mediators must remain strictly fair, objective, and focused on restoring sincere brotherhood."
            ],
            "vocabulary": [
                {"term": "Islaah", "definition": "Reconciling differences, peacemaking, and restoring harmony between disputing parties."},
                {"term": "Tabayyun", "definition": "Meticulously investigating and verifying claims before making judgments or acting."},
                {"term": "Sulh", "definition": "Peaceful settlement and formal reconciliation between parties."},
                {"term": "Adl", "definition": "Absolute justice and fair dealing without personal bias or favoritism."}
            ]
        },
        "exit_ticket": "Write down one sentence you could say to two shouting classmates to help them calm down and listen to each other."
    },

    # ─── LESSON 2.2.7 ───────────────────────────────────────────────────────────
    {
        "unit_order": 7,
        "unit_name": "Lesson 2.2.7: Hadith and daily practice",
        "unit_description": "Designs and implements a personal 'Brotherhood Code of Conduct' to translate theoretical Hadith values into daily morning intentions, school interactions, digital habits, and evening self-audits.",
        "lesson_title": "Hadith and Daily Practice",
        "diagram_title": "Daily Social Conduct Routine (Morning Intent, School Engagement, Digital Hygiene, Evening Audit)",
        "svg_fn": get_svg_lesson_7,
        "image": {
            "title": "Prophet's Mosque Minarets and Green Dome",
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Al_Masjid_An_Nabawi.jpg",
            "caption": "Madinah al-Munawwarah, the city where prophetic guidance was translated into daily lived ethics and community routines.",
            "author": "Wikimedia Commons Contributor",
            "licensing": "CC-BY-SA-4.0",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Living the Sunnah: Small Consistent Habits in Islam",
            "youtube_id": "BfE7vM4P6b4",
            "description": "How consistent daily routines and pure intentions transform ordinary school days into acts of worship."
        },
        "inquiry_question": "How do we draft and implement a personal 'Brotherhood Code' to guide our daily choices?",
        "connection": "Have you ever noticed that after a great lesson, it is easy to say, 'That was wonderful,' but within a week we forget everything and go back to our old habits? This is because knowledge without a practical plan is like a cloud that brings no rain. To prevent this, we must turn the Prophet's teachings on unity and avoiding ill motives into a concrete, daily action plan. In this lesson, we will design our own 'Brotherhood Code' for our classroom.",
        "goals": [
            "Understand the spiritual power of small, consistent righteous deeds (Adwamuha wa in qall).",
            "Structure a comprehensive 4-stage daily social conduct routine: Morning Intent, School Engagement, Digital Hygiene, Evening Audit.",
            "Draft an actionable, personalized Classroom Brotherhood Code anchored in sincerity."
        ],
        "authoritative_concept": (
            "Spiritual Accountability (Muhasabah) and Consistency (Istiqamah) require believers to actively monitor their thoughts, speech, "
            "and deeds against prophetic standards. Islam emphasizes that moral knowledge is only beneficial when translated into daily, "
            "practical habits performed with sincere intention (Ikhlas) purely for the sake of Allah."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**Prophetic Hadith on Consistency (Sahih al-Bukhari #6465):**\n"
            "> \"The most beloved of deeds to Allah are those which are done consistently, even if they are small.\"\n\n"
            "**Prophetic Hadith on Intentions (Sahih al-Bukhari #1):**\n"
            "> \"Actions are judged only by their intentions, and each person will have only what they intended.\""
        ),
        "deep_explanation": (
            "To turn the lessons of the Hadiths into a lifelong habit, we create a structured 'Brotherhood Code of Conduct' across three levels of action:\n\n"
            "1. **My Heart (Internal Audit):** Actively combating jealousy and suspicion. When I see a classmate with high marks or a nice item, I immediately say: 'MashaAllah, may Allah bless them,' rooting out Hasad before it takes hold.\n"
            "2. **My Tongue (Speech Audit):** Refusing to participate in backbiting, rumors, and offensive nicknames. When peers begin gossiping, I change the topic or politely leave.\n"
            "3. **My Hands (Action Audit):** Actively seeking opportunities to assist classmates, sharing revision textbooks, welcoming the lonely, and maintaining community peace."
        ),
        "step_process": {
            "title": "The 4 Daily Touchpoints of the Brotherhood Code",
            "steps": [
                {"step": 1, "title": "Morning Touchpoint (Niyyah)", "description": "Formulate the intent: 'O Allah, make my tongue and hands a source of peace and service today.'"},
                {"step": 2, "title": "School Touchpoint (Ta'awun)", "description": "Perform at least one deliberate act of cooperation: sharing notes or encouraging an excluded student."},
                {"step": 3, "title": "Digital Touchpoint (Hygiene)", "description": "Apply the 3-Gate Ethical Filter before forwarding any message or status update."},
                {"step": 4, "title": "Evening Touchpoint (Muhasabah)", "description": "Audit the day's actions, forgive anyone who offended you, and cleanse the heart before sleep."}
            ]
        },
        "worked_example": {
            "scenario": (
                "Fatima notices that before midterm exams, some classmates deliberately hide reference textbooks and study summaries so others "
                "cannot get high marks (an attitude rooted in Hasad and Najsh). Fatima decides to apply her class 'Brotherhood Code.' She organizes "
                "a 'Classroom Knowledge Bank,' placing her personal summaries on a shared shelf and launching a 30-minute after-school study circle. "
                "She tells the class: 'Hiding our books comes from fear and jealousy. If we share our knowledge, Allah will put Barakah (blessing) "
                "in our study, and we will succeed together as one team.' Inspired by her initiative, other students contribute, and class averages rise."
            ),
            "analysis": (
                "Fatima identifies a toxic social practice (knowledge hoarding) and replaces it with institutional Ta'awun. She demonstrates "
                "that sharing knowledge multiplies collective success rather than diminishing individual achievement."
            ),
            "takeaway": "True brotherhood means desiring for your classmates the same academic success and joy you desire for yourself."
        },
        "real_world_application": (
            "Choose one classmate whom you have ignored or felt slightly envious of in the past. Write down a concrete plan to do something kind "
            "for them this week: help them with a difficult subject, invite them to join your lunch group, or offer a sincere compliment on their work. "
            "Keep your intention pure, doing it solely for the sake of Allah without expecting praise."
        ),
        "reflection": (
            "Why does performing small, consistent acts of kindness have a greater impact on your character than doing one large good deed once a year? "
            "How does keeping our intentions sincere prevent us from falling into ostentation and showing off (Riya')?"
        ),
        "misconception": {
            "misconception": "Believing that good deeds are only meaningful if they are public and noticed by teachers and peers.",
            "correction": "In Islam, secret acts of kindness (Ikhlas) performed purely for Allah without human recognition carry the highest spiritual reward and shield the soul from vanity (Riya')."
        },
        "mcq": {
            "question": "What is the primary spiritual purpose of creating and following a personal 'Brotherhood Code'?",
            "options": [
                "A) To show off your moral superiority to your classmates and teachers",
                "B) To win prizes and material rewards from the school administration",
                "C) To translate the Prophet's teachings into consistent, daily actions that please Allah",
                "D) To establish a system of strict rules to punish classmates who make mistakes"
            ],
            "answer": "C",
            "explanation": "A personal moral code is designed to help a believer align their daily actions and intentions with divine guidance, fostering consistent spiritual and moral growth solely for the sake of Allah."
        },
        "summary": {
            "key_points": [
                "Moral knowledge is only beneficial when it is translated into daily, consistent actions.",
                "A personal code helps us audit our thoughts, words, and actions to avoid ill motives.",
                "Sincere intentions (Ikhlas) are the foundation of all righteous deeds in Islam."
            ],
            "vocabulary": [
                {"term": "Istiqamah", "definition": "Steadfast consistency and integrity in adhering to moral principles."},
                {"term": "Muhasabah", "definition": "Rigorous self-examination and moral accounting of one's daily conduct."},
                {"term": "Ikhlas", "definition": "Complete purity and sincerity of intention; acting solely to please Allah."},
                {"term": "Riya’", "definition": "Doing good deeds to show off or win praise from people instead of pleasing Allah."}
            ]
        },
        "exit_ticket": "Write down one 'flower action' from your personal Brotherhood Code that you will perform before the end of the day today."
    },

    # ─── LESSON 2.2.8 ───────────────────────────────────────────────────────────
    {
        "unit_order": 8,
        "unit_name": "Lesson 2.2.8: Unit synthesis",
        "unit_description": "Capstone integrative synthesis of Topic 4, unifying the Hadith on Unity, the Hadith on Ill Motives, Quranic injunctions, conflict mediation, and daily practice into an indomitable framework of Islamic Muamalat.",
        "lesson_title": "Unit Synthesis: Architecture of Social Harmony",
        "diagram_title": "Master Comprehensive Architecture of Social Harmony in Hadith",
        "svg_fn": get_svg_lesson_8,
        "image": {
            "title": "The Kaaba — The Unifying Epicenter of the Muslim Ummah",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/The_Kaaba_during_Hajj.jpg",
            "caption": "The focal point of Muslim prayer worldwide, representing the complete synthesis of faith, unity, and social harmony.",
            "author": "Muhammad Mahdi Karim",
            "licensing": "GNU FDL / CC-BY-SA-3.0",
            "source": "Wikimedia Commons"
        },
        "youtube": {
            "title": "Mastering Islamic Social Ethics: The Complete Framework",
            "youtube_id": "BfE7vM4P6b4",
            "description": "Comprehensive review of the social architecture of the Ummah, from heart purification to community mediation."
        },
        "inquiry_question": "How do we consolidate our understanding of unity, brotherhood, and the social prohibitions of Islam?",
        "connection": "Imagine you have gathered beautiful bricks, strong cement, and perfect wood, but you have not assembled them. They are just a pile of materials. In this final lesson of the unit, we will act as the master architects. We will bring together the Hadith on Unity and the Hadith on Ill Motives, the key terms we studied, the practical scenarios, and our visual diagrams to build a complete, solid understanding of Islamic social relations (Muamalat).",
        "goals": [
            "Synthesize the theological, moral, and practical elements of Topic 4 into an integrated conceptual model.",
            "Master the core terminology: Ummah, Tarahum, Zann, Tajassus, Najsh, Hasad, Tadabur, Islah, and Tabayyun.",
            "Demonstrate mastery across multi-variable ethical scenarios combining online and offline social dilemmas."
        ],
        "authoritative_concept": (
            "Islamic Social Ethics (Muamalat) is the comprehensive, divinely revealed legal and moral architecture that governs human "
            "interaction to secure social justice, psychological safety, and community cohesion. Sincere brotherhood (Ukhuwwah) is achieved "
            "when believers combine active empathy (the single body) with rigorous avoidance of internal malice (the prohibited ill motives)."
        ),
        "scripture_panel": (
            "### Scripture & Sources Panel\n\n"
            "**The Foundational Unit Scriptural Pillars:**\n\n"
            "1. **Surah Al-Hujurat (49:10):**\n"
            "«إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ فَأَصْلِحُوا بَيْنَ أَخَوَيْكُمْ ۚ وَاتَّقُوا اللَّهَ لَعَلَّكُمْ تُرْحَمُونَ»\n"
            "> \"The believers are but brothers, so make peace between your brothers. And fear Allah that you may receive mercy.\"\n\n"
            "2. **Hadith of Sahih Muslim:** \"The similitude of believers... is that of one body...\"\n\n"
            "3. **Hadith of Sahih al-Bukhari:** \"Beware of suspicion... and do not be jealous... and be, O servants of Allah, brothers!\""
        ),
        "deep_explanation": (
            "Let's review the entire unit's core tripartite structure:\n\n"
            "1. **The Vision (Hadith 1 - Unity):** The body analogy. Individual distress is a collective concern requiring active empathy, mutual love (Tawadd), and systemic mobilization (As-Sahar and Al-Humma).\n"
            "2. **The Shield (Hadith 2 - Prohibitions):** The seven social termites. Absolute prohibition against suspicion (Zann), fault-finding (Tahassus), spying (Tajassus), trade deception (Najsh), envy (Hasad), hatred (Bughd), and desertion (Tadabur).\n"
            "3. **The Practical Tools:** Quranic verification (Tabayyun) to filter news, 4-stage conflict mediation (Islah) to resolve disputes, and the 4-touchpoint daily Brotherhood Code to sustain habit."
        ),
        "comparison_table": {
            "title": "Topic 4 Comprehensive Terminology & Conceptual Index",
            "headers": ["Islamic Term", "Literal Meaning", "Core Application in Daily Life"],
            "rows": [
                ["Ummah", "Global community of faith", "Transcending tribal, national, and racial divisions in school"],
                ["Tarahum", "Mutual mercy and compassion", "Feeling acute sympathy and actively helping suffering peers"],
                ["Ta'awun", "Righteous cooperation", "Working collaboratively in peer tutoring, charity, and cleanups"],
                ["Zann", "Unfounded negative suspicion", "Refusing to believe or spread unverified assumptions about peers"],
                ["Tajassus", "Spying and snooping", "Guarding private chats, desks, and phones from intrusive prying"],
                ["Najsh", "Deceptive manipulation in trade", "Absolute honesty in commercial dealings and student exchanges"],
                ["Hasad", "Destructive envy", "Praying for others' blessings (Barakah) instead of wishing their loss"],
                ["Tadabur", "Social desertion and boycott", "Reconciling disputes within 3 days; never giving the silent treatment"],
                ["Tabayyun", "Rigorous verification", "Investigating claims directly before forwarding messages or judging"],
                ["Islah", "Peace-making and mediation", "De-escalating fights and reconciling broken friendships"]
            ]
        },
        "worked_example": {
            "scenario": (
                "Review the following four real-world school situations and identify their corresponding Islamic concepts:\n"
                "1. Amina assumes her friend is ignoring her deliberately because she is arrogant, with zero proof. (Answer: **Suspicion / Zann**)\n"
                "2. Omar works with classmates to set up a library sharing textbooks with needy students. (Answer: **Cooperation / Ta'awun**)\n"
                "3. Zainab secretly peeks at her classmate's unlocked phone screen to read private chats. (Answer: **Spying / Tajassus**)\n"
                "4. Yusuf resolves a loud fight between two friends in the playground by verifying facts. (Answer: **Mediation / Islah**)"
            ),
            "analysis": (
                "Each scenario reflects an immediate application of the commanded virtues or prohibited vices studied in this unit. "
                "Recognizing these ethical patterns allows students to make righteous choices in daily life."
            ),
            "takeaway": "Master Islamic social ethics by continuously diagnosing your thoughts and actions through the lens of Quran and Hadith."
        },
        "real_world_application": (
            "Write an essay or prepare a presentation for your school morning assembly on 'The Importance of Unity and Avoidance of Ill Motives.' "
            "Highlight the body analogy, provide three practical steps students can take to prevent cyber-bullying, and design an infographic poster "
            "for your school notice board."
        ),
        "reflection": (
            "Which concept from this unit did you find most challenging to apply in your personal life? Why? "
            "How does a healthy, united Muslim community contribute to the peace, security, and prosperity of the entire Kenyan nation?"
        ),
        "misconception": {
            "misconception": "Believing that Islamic social teachings are only intended for Muslims dealing with other Muslims.",
            "correction": "Islam commands universal justice, truthfulness, and compassion toward all human beings. Deception (Najsh), spying (Tajassus), and slander are strictly prohibited against any person, regardless of their faith."
        },
        "mcq": {
            "question": "A classmate of yours, Omar, has been absent from school for three days. A malicious rumor circulates on social media claiming he was arrested for theft. Applying the combined prophetic guidance from both Hadiths studied in this unit, what is the most ethically upright action to take?",
            "options": [
                "A) Forward the rumor to your close circle of friends so that they are warned to keep their distance from Omar",
                "B) Assume the rumor is accurate and immediately block Omar from all class social media channels (Deserting)",
                "C) Intercept and delete the rumor in chat groups, verify the truth with a teacher (Tabayyun), and contact Omar's family to offer support if he is unwell (Tarahum)",
                "D) Remain completely passive because Omar's situation does not directly impact your personal exam scores"
            ],
            "answer": "C",
            "explanation": "Option C integrates the complete moral framework: it eradicates suspicion (Anti-Zann), applies rigorous verification (Tabayyun), protects a brother's honor (Sitr), and manifests active empathetic solidarity (the One Body analogy)."
        },
        "summary": {
            "key_points": [
                "True Islamic social relations (Muamalat) require active empathy and the prevention of social vices.",
                "Sincere brotherhood is built by treating others' pain as our own and keeping our hearts free of envy.",
                "We are individually accountable for ensuring our speech and actions build peace."
            ],
            "vocabulary": [
                {"term": "Muamalat", "definition": "Social, legal, and economic interactions in Islamic law."},
                {"term": "Ukhuwwah", "definition": "The spiritual and social bond of sisterhood and brotherhood in faith."},
                {"term": "Mizan", "definition": "The divine balance between positive virtue (Tahliyah) and vice elimination (Takhliyah)."},
                {"term": "Barakah", "definition": "Divine blessing and increase placed by Allah in righteous, shared efforts."}
            ]
        },
        "exit_ticket": "Write down the single most important lesson you have learned in this unit and explain how you will use it to be a better friend and citizen."
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_ire_topic4():
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: GRADE 9 IRE — TOPIC 4: SELECTED HADITH")
    print("Target Topic ID: 344 | Strict Subject & Topic Isolation")
    print("=" * 80)

    with transaction.atomic():
        # Retrieve target topic 344
        topic = Topic.objects.select_related("subject", "subject__grade", "subject__grade__curriculum").get(id=344)
        subject = topic.subject
        grade = subject.grade
        curriculum = grade.curriculum

        print(f"Curriculum : {curriculum.name}")
        print(f"Grade      : {grade.name} (ID: {grade.id})")
        print(f"Subject    : {subject.name} (ID: {subject.id})")
        print(f"Topic      : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print("-" * 80)

        # Update topic metadata
        topic.name = "Selected Hadith (Unity and Avoidance of Ill Motives)"
        topic.description = (
            "Comprehensive study of selected Hadith on unity and the avoidance of ill motives: "
            "source reading of the body analogy (Sahih Muslim), practical unity in school and community (Ta'awun), "
            "identifying the six destructive ill motives (Sahih al-Bukhari), digital ethics and cyber-spying, "
            "comparative synthesis of Tahliyah and Takhliyah, 4-stage conflict mediation (Islah), "
            "personal Brotherhood Code routines, and master architecture of Islamic Muamalat."
        )
        topic.save()

        # Clean existing units under topic 344 (Strictly isolated to Topic 344)
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"[*] Removing {existing_units.count()} existing LearningUnits under Topic 344...")
            existing_units.delete()

        # Clean any orphan lessons under topic 344
        orphan_lessons = Lesson.objects.filter(topic=topic)
        if orphan_lessons.exists():
            print(f"[*] Removing {orphan_lessons.count()} orphan Lessons under Topic 344...")
            orphan_lessons.delete()

        total_units_created = 0
        total_lessons_created = 0
        total_blocks_created = 0
        total_assets_created = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            print(f"\n>>> [Unit {u_order}/8] Ingesting: '{l_title}'")

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=clean_text(cfg["unit_description"])
            )
            total_units_created += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                published_at=timezone.now(),
                immutable_metadata={
                    "grade": "Grade 9",
                    "grade_id": grade.id,
                    "subject": "IRE",
                    "subject_id": subject.id,
                    "topic_id": topic.id,
                    "topic_order": topic.order,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "unit_name": u_name,
                    "author": "VLearn Senior Curriculum Ingestion Specialist",
                    "curriculum_framework": "CBC Kenya Grade 9 IRE Strand 2.0 Sub-strand 2.2",
                    "enrichment_version": "v4_pedagogical_7cards",
                    "diagram_title": cfg["diagram_title"]
                }
            )
            total_lessons_created += 1

            # 3. Create LessonAssets
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
                    "author": img_info.get("author", "Classical Heritage"),
                    "licensing": img_info.get("licensing", "Public Domain"),
                    "source": img_info.get("source", "Wikimedia Commons"),
                    "caption": clean_text(img_info["caption"])
                }
            )

            # Asset 2: Dedicated Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=clean_text(cfg["diagram_title"]),
                description=f"High-quality pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/ire/grade9_topic_4_lesson_{u_order}.svg",
                metadata={
                    "svg_content": svg_content,
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 440",
                    "theme": "#0f172a"
                }
            )

            # Asset 3: Educational YouTube Video
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
            total_assets_created += 3

            # 4. Build 7 Cards / Pages (Standardized Pedagogical Blocks)

            # ───────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Inquiry
            # ───────────────────────────────────────────────────────────────────
            b_p1_img = LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Inquiry",
                order=10, component_order=1,
                block_type="suggested_image", component_type="suggested_image",
                title=clean_text(img_info["title"]),
                content={
                    "title": clean_text(img_info["title"]),
                    "url": img_info["url"],
                    "caption": clean_text(img_info["caption"]),
                    "author": img_info.get("author", "Classical Heritage"),
                    "licensing": img_info.get("licensing", "Public Domain"),
                    "source": img_info.get("source", "Wikimedia Commons")
                }
            )
            b_p1_img.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Inquiry",
                order=20, component_order=2,
                block_type="learning_goal", component_type="learning_goal",
                title="Lesson Objectives & Inquiry Hook",
                content={
                    "inquiry_question": clean_text(cfg["inquiry_question"]),
                    "connection": clean_text(cfg["connection"]),
                    "goals": clean_dict(cfg["goals"]),
                    "markdown": f"### Inquiry Question\n\n**{clean_text(cfg['inquiry_question'])}**\n\n### Connection & Hook\n\n{clean_text(cfg['connection'])}\n\n### Learning Goals\n\n" + "\n".join([f"- {g}" for g in cfg["goals"]])
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Concept & Scripture Panel
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Concept & Scripture",
                order=30, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Authoritative Concept",
                content={"markdown": clean_text(cfg["authoritative_concept"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Concept & Scripture",
                order=40, component_order=2,
                block_type="callout", component_type="callout",
                title="Scripture & Sources Panel",
                content={
                    "text": clean_text(cfg["scripture_panel"]),
                    "markdown": clean_text(cfg["scripture_panel"])
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & Architecture Diagram
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                order=50, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="In-Depth Analysis & Exposition",
                content={"markdown": clean_text(cfg["deep_explanation"])}
            )

            b_p3_diag = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                order=60, component_order=2,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {clean_text(cfg['diagram_title'])}",
                content={
                    "title": f"Diagram: {clean_text(cfg['diagram_title'])}",
                    "caption": f"Pedagogical vector SVG architecture for {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content,
                    "svg_content": svg_content
                },
                metadata={
                    "svg_content": svg_content,
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 440",
                    "theme": "#0f172a"
                }
            )
            b_p3_diag.assets.add(svg_asset)

            # Comparison table on Card 3 (if present)
            if "comparison_table" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                    order=70, component_order=3,
                    block_type="comparison_table", component_type="comparison_table",
                    title=clean_text(cfg["comparison_table"]["title"]),
                    content=clean_dict(cfg["comparison_table"])
                )

            # Step process on Card 3 (if present)
            if "step_process" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                    order=75, component_order=4,
                    block_type="step_process", component_type="step_process",
                    title=clean_text(cfg["step_process"]["title"]),
                    content=clean_dict(cfg["step_process"])
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Worked Example & Relatable Scenario
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Worked Example & Scenario",
                order=80, component_order=1,
                block_type="worked_example", component_type="worked_example",
                title="Relatable Student Scenario & Analysis",
                content={
                    "scenario": clean_text(cfg["worked_example"]["scenario"]),
                    "analysis": clean_text(cfg["worked_example"]["analysis"]),
                    "takeaway": clean_text(cfg["worked_example"]["takeaway"]),
                    "markdown": f"### Scenario\n\n{clean_text(cfg['worked_example']['scenario'])}\n\n### Analytical Breakdown\n\n{clean_text(cfg['worked_example']['analysis'])}\n\n### Core Takeaway\n\n**{clean_text(cfg['worked_example']['takeaway'])}**"
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Real-World Application, Reflection & Misconception
            # ───────────────────────────────────────────────────────────────────
            b_p5_vid = LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=90, component_order=1,
                block_type="suggested_video", component_type="suggested_video",
                title=clean_text(yt_info["title"]),
                content={
                    "title": clean_text(yt_info["title"]),
                    "url": f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                    "youtube_id": yt_info["youtube_id"],
                    "description": clean_text(yt_info["description"])
                }
            )
            b_p5_vid.assets.add(yt_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=100, component_order=2,
                block_type="real_world_example", component_type="real_world_example",
                title="Actionable Real-World Application",
                content={
                    "application": clean_text(cfg["real_world_application"]),
                    "markdown": f"### Real-World Application\n\n{clean_text(cfg['real_world_application'])}"
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=110, component_order=3,
                block_type="reflection", component_type="reflection",
                title="Pause & Reflect",
                content={
                    "prompt": clean_text(cfg["reflection"]),
                    "markdown": f"### Pause & Reflect\n\n{clean_text(cfg['reflection'])}"
                }
            )

            if "misconception" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                    order=120, component_order=4,
                    block_type="common_misconception", component_type="common_misconception",
                    title="Common Misconception & Correction",
                    content={
                        "misconception": clean_text(cfg["misconception"]["misconception"]),
                        "correction": clean_text(cfg["misconception"]["correction"]),
                        "markdown": f"### Common Misconception\n\n❌ *{clean_text(cfg['misconception']['misconception'])}*\n\n### Factual Correction\n\n✓ **{clean_text(cfg['misconception']['correction'])}**"
                    }
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Interactive Assessment / Knowledge Check
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Knowledge Check & Assessment",
                order=130, component_order=1,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Interactive Knowledge Check",
                content=clean_dict(cfg["mcq"])
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary, Key Points & Mini-Activity
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=140, component_order=1,
                block_type="summary", component_type="summary",
                title="Unit Principles & Vocabulary Review",
                content={
                    "title": f"Summary: {l_title}",
                    "key_points": clean_dict(cfg["summary"]["key_points"]),
                    "vocabulary": clean_dict(cfg["summary"]["vocabulary"]),
                    "markdown": f"### Key Principles\n\n" + "\n".join([f"- {kp}" for kp in cfg["summary"]["key_points"]]) + "\n\n### Vocabulary Review\n\n" + "\n".join([f"- **{v['term']}**: {v['definition']}" for v in cfg["summary"]["vocabulary"]])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=150, component_order=2,
                block_type="mini_activity", component_type="mini_activity",
                title="Exit Ticket Challenge",
                content={
                    "activity": clean_text(cfg["exit_ticket"]),
                    "prompt": clean_text(cfg["exit_ticket"]),
                    "markdown": f"### Exit Ticket Challenge\n\n📝 **{clean_text(cfg['exit_ticket'])}**"
                }
            )

            blocks_count = lesson.blocks.count()
            total_blocks_created += blocks_count
            print(f"  [+] Created 7 Cards / Pages with {blocks_count} Blocks and 3 LessonAssets")

        print("\n" + "=" * 80)
        print("TOPIC 344 INGESTION & ENRICHMENT COMPLETE!")
        print(f"  - Subject           : {subject.name} (ID: {subject.id})")
        print(f"  - Topic             : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  - LearningUnits     : {total_units_created}")
        print(f"  - Lessons Published : {total_lessons_created}")
        print(f"  - LessonBlocks      : {total_blocks_created}")
        print(f"  - LessonAssets      : {total_assets_created}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic4()
