"""
Master Ingestion & Enrichment Engine for CBC Grade 9 CRE — Topics 1 & 2
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django Environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    return text.strip() if text else ""
def get_svg_t1_l1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Spectrum of Labor: From Task to Calling</text>
  <g transform="translate(50, 80)">
    <rect x="0" y="0" width="150" height="280" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <text x="75" y="35" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="16" font-weight="bold">JOB</text>
    <text x="75" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Temporary Tasks</text>
    <text x="75" y="100" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Wage / Payment</text>
    <text x="75" y="130" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Immediate Need</text>
    <path d="M 160 140 L 180 140" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
    <rect x="190" y="0" width="150" height="280" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="265" y="35" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">CRAFT / TRADE</text>
    <text x="265" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Manual Skill</text>
    <text x="265" y="100" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Apprenticeship</text>
    <text x="265" y="130" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Practical Output</text>
    <path d="M 350 140 L 370 140" stroke="#34d399" stroke-width="3" marker-end="url(#arrow)"/>
    <rect x="380" y="0" width="150" height="280" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="455" y="35" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">CAREER</text>
    <text x="455" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Lifelong Path</text>
    <text x="455" y="100" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Code of Ethics</text>
    <text x="455" y="130" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Professional Growth</text>
    <path d="M 540 140 L 560 140" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
    <rect x="570" y="0" width="150" height="280" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="645" y="35" text-anchor="middle" fill="#f59e0b" font-family="sans-serif" font-size="16" font-weight="bold">VOCATION</text>
    <text x="645" y="70" text-anchor="middle" fill="#fde68a" font-family="sans-serif" font-size="12">Divine Calling</text>
    <text x="645" y="100" text-anchor="middle" fill="#fde68a" font-family="sans-serif" font-size="12">Service to God</text>
    <text x="645" y="130" text-anchor="middle" fill="#fde68a" font-family="sans-serif" font-size="12">Eternal Impact</text>
  </g>
  <text x="400" y="400" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="13">Colossians 3:23 — 'Whatever you do, work at it with all your heart, as working for the Lord.'</text>
</svg>"""

def get_svg_t1_l2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">Traditional African Labor vs. Christian Biblical Work &amp; Rest</text>
  <rect x="50" y="75" width="330" height="290" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="215" y="110" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="16" font-weight="bold">Traditional African View</text>
  <text x="80" y="150" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Communal Solidarity (Mwethya)</text>
  <text x="80" y="185" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Non-monetary Rewards (Food/Unity)</text>
  <text x="80" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Division by Age and Gender</text>
  <text x="80" y="255" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Ridicule of Laziness in Proverbs</text>
  <text x="80" y="290" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Seasonal and Ritual Rest</text>
  <rect x="420" y="75" width="330" height="290" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="585" y="110" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">Christian Biblical View</text>
  <text x="450" y="150" fill="#cbd5e1" font-family="sans-serif" font-size="13">• God as the First Worker (Gen 2:1-3)</text>
  <text x="450" y="185" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Stewardship &amp; Co-creatorship</text>
  <text x="450" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Condemnation of Idleness (2 Thess 3:10)</text>
  <text x="450" y="255" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Sluggard vs. The Ant (Prov 6:6)</text>
  <text x="450" y="290" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Mandatory Sabbath Rest &amp; Worship</text>
  <text x="400" y="410" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold">Synthesis: Work is Sacred Stewardship Balanced by Life-Giving Rest</text>
</svg>"""

def get_svg_t1_l3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Pillars of Workplace Integrity</text>
  <rect x="50" y="80" width="700" height="50" fill="#334155" rx="6"/>
  <text x="400" y="112" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="16" font-weight="bold">PROFESSIONAL CODES &amp; ETHICS (External Standards)</text>
  <g transform="translate(50, 150)">
    <rect x="0" y="0" width="120" height="190" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="60" y="30" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">Diligence</text>
    <text x="60" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Hard work</text>
    <text x="60" y="90" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Energetic</text>
    <rect x="145" y="0" width="120" height="190" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="6"/>
    <text x="205" y="30" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">Honesty</text>
    <text x="205" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Truthfulness</text>
    <text x="205" y="90" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Accurate Scales</text>
    <rect x="290" y="0" width="120" height="190" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="6"/>
    <text x="350" y="30" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="13" font-weight="bold">Integrity</text>
    <text x="350" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Unseen Ethics</text>
    <text x="350" y="90" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Reliability</text>
    <rect x="435" y="0" width="120" height="190" fill="#1e293b" stroke="#c084fc" stroke-width="2" rx="6"/>
    <text x="495" y="30" text-anchor="middle" fill="#c084fc" font-family="sans-serif" font-size="13" font-weight="bold">Faithfulness</text>
    <text x="495" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Loyalty</text>
    <text x="495" y="90" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Trustworthy</text>
    <rect x="580" y="0" width="120" height="190" fill="#1e293b" stroke="#f43f5e" stroke-width="2" rx="6"/>
    <text x="640" y="30" text-anchor="middle" fill="#f43f5e" font-family="sans-serif" font-size="13" font-weight="bold">Tolerance</text>
    <text x="640" y="70" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Patience</text>
    <text x="640" y="90" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Team Peace</text>
  </g>
  <rect x="50" y="360" width="700" height="45" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="6"/>
  <text x="400" y="388" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">FOUNDATION: Proverbs 11:1 — 'Accurate weights find favor with the Lord.'</text>
</svg>"""

def get_svg_t1_l4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Reciprocal Covenant of Employment</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">EMPLOYER DUTIES</text>
  <text x="75" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">1. Pay Fair Wages Promptly</text>
  <text x="75" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">2. Provide Safe Workplace</text>
  <text x="75" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">3. Grant Leave &amp; Medical Rest</text>
  <text x="75" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">4. Respect Human Dignity</text>
  <text x="75" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">5. Motivate &amp; Guide Growth</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">EMPLOYEE DUTIES</text>
  <text x="455" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">1. Work Diligently &amp; Honestly</text>
  <text x="455" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">2. Protect Employer's Property</text>
  <text x="455" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">3. Keep Terms of Contract</text>
  <text x="455" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">4. Work Without Constant Supervision</text>
  <text x="455" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">5. Seek Peaceful Solutions</text>
  <text x="400" y="400" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">Colossians 4:1 — 'Masters, provide what is right and fair, for you have a Master in heaven.'</text>
</svg>"""

def get_svg_t1_l5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Cycle of Child Labor vs. Church Intervention</text>
  <rect x="40" y="80" width="320" height="300" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="10"/>
  <text x="200" y="115" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="16" font-weight="bold">Cycle of Child Labor (Trap)</text>
  <text x="60" y="160" fill="#fca5a5" font-family="sans-serif" font-size="13">1. Extreme Family Poverty &amp; Greed</text>
  <text x="60" y="200" fill="#fca5a5" font-family="sans-serif" font-size="13">2. School Dropout &amp; Hazardous Work</text>
  <text x="60" y="240" fill="#fca5a5" font-family="sans-serif" font-size="13">3. Stunted Cognitive/Physical Growth</text>
  <text x="60" y="280" fill="#fca5a5" font-family="sans-serif" font-size="13">4. Lifelong Economic Vulnerability</text>
  <rect x="440" y="80" width="320" height="300" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="10"/>
  <text x="600" y="115" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">Church &amp; State Intervention</text>
  <text x="460" y="160" fill="#86efac" font-family="sans-serif" font-size="13">1. Rescue Centers &amp; Feeding Support</text>
  <text x="460" y="200" fill="#86efac" font-family="sans-serif" font-size="13">2. Free Basic Education &amp; TVET Skills</text>
  <text x="460" y="240" fill="#86efac" font-family="sans-serif" font-size="13">3. Psychosocial Care &amp; Mentorship</text>
  <text x="460" y="280" fill="#86efac" font-family="sans-serif" font-size="13">4. Empowered, Self-Reliant Youth</text>
  <text x="400" y="415" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="13">Deut 24:14-15 — 'Do not take advantage of a hired worker who is poor and needy.'</text>
</svg>"""

def get_svg_t1_l6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">Overcoming Unemployment Through Entrepreneurship</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#f87171" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="16" font-weight="bold">The White-Collar Trap</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Overemphasis on Office Jobs</text>
  <text x="75" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Avoidance of Manual Labor</text>
  <text x="75" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Dependency &amp; Prolonged Idleness</text>
  <text x="75" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Frustration &amp; Social Despair</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">Self-Employment &amp; Jua Kali</text>
  <text x="455" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Practical Skills &amp; Creativity</text>
  <text x="455" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Job Creation for Community</text>
  <text x="455" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Financial Independence &amp; Dignity</text>
  <text x="455" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• God-Honoring Industry (Prov 14:23)</text>
  <text x="400" y="405" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">Proverbs 14:23 — 'All hard work brings a profit, but mere talk leads only to poverty.'</text>
</svg>"""

def get_svg_t2_l1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Triune Dimensions of Human Sexuality</text>
  <circle cx="320" cy="220" r="120" fill="#1e293b" fill-opacity="0.7" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="480" cy="220" r="120" fill="#1e293b" fill-opacity="0.7" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="400" cy="300" r="120" fill="#1e293b" fill-opacity="0.7" stroke="#34d399" stroke-width="3"/>
  <text x="260" y="180" fill="#38bdf8" font-family="sans-serif" font-size="15" font-weight="bold">BIOLOGICAL</text>
  <text x="260" y="205" fill="#cbd5e1" font-family="sans-serif" font-size="11">Physiology &amp; Body</text>
  <text x="540" y="180" fill="#fbbf24" font-family="sans-serif" font-size="15" font-weight="bold">EMOTIONAL</text>
  <text x="540" y="205" fill="#cbd5e1" font-family="sans-serif" font-size="11">Feelings &amp; Care</text>
  <text x="400" y="370" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="15" font-weight="bold">PSYCHOLOGICAL</text>
  <text x="400" y="390" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Mind &amp; Self-Identity</text>
  <text x="400" y="235" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">SACRED IMAGE</text>
  <text x="400" y="255" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">OF GOD (Gen 1:27)</text>
</svg>"""

def get_svg_t2_l2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">Traditional African Customs vs. Christian Biblical Truth</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="16" font-weight="bold">Traditional African View</text>
  <text x="75" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Procreation Primary Purpose</text>
  <text x="75" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Polygamy Accepted for Status</text>
  <text x="75" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Patriarchal Gender Hierarchy</text>
  <text x="75" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Initiation Rites Sex Education</text>
  <text x="75" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">• High Value on Virginity</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">Christian Biblical View</text>
  <text x="455" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Companionship &amp; Mutual Love</text>
  <text x="455" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Permanent Monogamy (Gen 2:24)</text>
  <text x="455" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Equal Dignity as Co-Heirs</text>
  <text x="455" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Sacrificial Love (Eph 5:25)</text>
  <text x="455" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Mutual Body Ownership (1 Cor 7)</text>
  <text x="400" y="405" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold">Ephesians 5:33 — 'Each one must love his wife as himself, and the wife must respect her husband.'</text>
</svg>"""

def get_svg_t2_l3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Purity Shield: Moral Values &amp; Life Skills</text>
  <circle cx="400" cy="240" r="160" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="400" cy="240" r="115" fill="#0f172a" stroke="#34d399" stroke-width="3"/>
  <circle cx="400" cy="240" r="70" fill="#334155" stroke="#f59e0b" stroke-width="3"/>
  <text x="400" y="235" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">SELF-CONTROL</text>
  <text x="400" y="255" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Holy Spirit Power</text>
  <text x="400" y="160" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">DECISION-MAKING &amp; VALUES</text>
  <text x="400" y="110" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">ASSERTIVENESS (SAYING NO)</text>
  <text x="160" y="410" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Outer Layer: Clear Boundaries</text>
  <text x="400" y="410" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Middle Layer: Ethical Reflection</text>
  <text x="640" y="410" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Core: Spiritual Armor (1 Cor 6:19)</text>
</svg>"""

def get_svg_t2_l4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Boundary of Holiness vs. Destructive Deviations</text>
  <circle cx="400" cy="230" r="110" fill="#1e293b" stroke="#34d399" stroke-width="4"/>
  <text x="400" y="215" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">HOLY MARRIAGE</text>
  <text x="400" y="240" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">COVENANT</text>
  <text x="400" y="265" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">(Genesis 2:24)</text>
  <g fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">
    <text x="130" y="130">• FORNICATION</text>
    <text x="130" y="240">• PROSTITUTION</text>
    <text x="130" y="350">• INCEST (Lev 18)</text>
    <text x="670" y="130" text-anchor="end">• ADULTERY</text>
    <text x="670" y="240" text-anchor="end">• RAPE / VIOLENCE</text>
    <text x="670" y="350" text-anchor="end">• DEFILEMENT</text>
  </g>
  <text x="400" y="410" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="13">Galatians 5:19-21 — 'The acts of the flesh are obvious: sexual immorality, impurity...'</text>
</svg>"""

def get_svg_t2_l5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">Biological and Psychological Consequences of Immorality</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="16" font-weight="bold">Biological Consequences</text>
  <text x="75" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Gonorrhea (Pain &amp; Infertility)</text>
  <text x="75" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Syphilis (Organ &amp; Brain Damage)</text>
  <text x="75" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Hepatitis B (Fatal Liver Damage)</text>
  <text x="75" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">• HIV/AIDS &amp; Opportunistic Illness</text>
  <text x="75" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Unplanned Teenage Pregnancy</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="16" font-weight="bold">Psychological Consequences</text>
  <text x="455" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Chronic Stress &amp; Anxiety</text>
  <text x="455" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Crushing Guilt &amp; Low Self-Esteem</text>
  <text x="455" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Depression &amp; Suicidal Despair</text>
  <text x="455" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Academic Decline &amp; Dropout</text>
  <text x="455" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Stigmatization &amp; Social Isolation</text>
  <text x="400" y="405" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="13">1 Corinthians 6:18 — 'Whoever sins sexually, sins against their own body.'</text>
</svg>"""

def get_svg_t2_l6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">God's Sacred Design vs. Broken Social Alternatives</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">God's Holy Standard</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Sanctity of Life at Conception (Ex 20:13)</text>
  <text x="75" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Permanent Marriage Covenant (Matt 19:6)</text>
  <text x="75" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Mutual Forgiveness &amp; Faithfulness</text>
  <text x="75" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Safe Haven for Children's Growth</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="16" font-weight="bold">Broken Alternatives</text>
  <text x="455" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Induced Abortion (Destruction of Life)</text>
  <text x="455" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Divorce (Tearing Apart the Covenant)</text>
  <text x="455" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Emotional Trauma on Children</text>
  <text x="455" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Physical Harm &amp; Legal Consequences</text>
  <text x="400" y="405" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">Matthew 19:6 — 'What God has joined together, let no one separate.'</text>
</svg>"""

print('SVG definitions loaded successfully!')
