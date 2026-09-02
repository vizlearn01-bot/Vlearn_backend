"""
VLearn CBC Grade 9 CRE — Topic 5: Raising the Widow's Son at Nain (All 6 Lessons)
Database Ingestion & Enrichment Script
"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / '.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
import django
django.setup()

from django.db import transaction
from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    if not text:
        return ''
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|SCENARIO|COMPARISON)[^\]]*\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()

# ─── SVG GENERATORS ──────────────────────────────────────────────────────────

def get_svg_l1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">Geography of Nain &amp; The Plight of Ancient Widows</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#f87171" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="16" font-weight="bold">The Widow's Social Vulnerability</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Loss of Husband (First Protector)</text>
  <text x="75" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Loss of Only Son (Sole Breadwinner)</text>
  <text x="75" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• No Inheritance or Property Rights</text>
  <text x="75" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Severe Economic &amp; Social Despair</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">Location &amp; Context of Nain</text>
  <text x="455" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Hillside Village in Galilee (Plain of Jezreel)</text>
  <text x="455" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• 35 km South of Capernaum</text>
  <text x="455" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Walled Town with Gated Entrance</text>
  <text x="455" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Meaning: 'Delightful' / 'Pleasant'</text>
  <text x="400" y="405" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">Luke 7:12 — 'A dead person was being carried out—the only son of his mother, and she was a widow.'</text>
</svg>"""

def get_svg_l2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Great Collision of Two Crowds at the City Gate</text>
  <rect x="50" y="80" width="300" height="270" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="200" y="115" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="16" font-weight="bold">The Funeral Procession</text>
  <text x="70" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Moving Out of the Gate</text>
  <text x="70" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Led by Weeping Widow &amp; Mourners</text>
  <text x="70" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Atmosphere: Death, Grief, Hopelessness</text>
  <text x="70" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Destination: The Tombs (Decay)</text>
  <circle cx="400" cy="215" r="45" fill="#334155" stroke="#fbbf24" stroke-width="3"/>
  <text x="400" y="210" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">THE GATE</text>
  <text x="400" y="230" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="10">ENCOUNTER</text>
  <rect x="450" y="80" width="300" height="270" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="600" y="115" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">The Procession of Life</text>
  <text x="470" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Moving Into the Gate</text>
  <text x="470" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Led by Jesus &amp; His Disciples</text>
  <text x="470" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Atmosphere: Grace, Authority, Joy</text>
  <text x="470" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Destination: Resurrection &amp; Restoration</text>
  <text x="400" y="405" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">Luke 7:13 — 'When the Lord saw her, his heart went out to her and he said, "Don't cry."'</text>
</svg>"""

def get_svg_l3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Fourfold Miracle of Resurrection at Nain</text>
  <g transform="translate(50, 90)">
    <rect x="0" y="0" width="155" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="77" y="35" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="15" font-weight="bold">1. TOUCH</text>
    <text x="77" y="80" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Jesus touched</text>
    <text x="77" y="105" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">the funeral bier</text>
    <text x="77" y="150" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">Breaks ritual</text>
    <text x="77" y="175" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">taboo with purity</text>
    <rect x="180" y="0" width="155" height="260" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="257" y="35" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="15" font-weight="bold">2. COMMAND</text>
    <text x="257" y="80" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">'Young man, I</text>
    <text x="257" y="105" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">say to you, arise!'</text>
    <text x="257" y="150" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">Divine creative</text>
    <text x="257" y="175" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">authority over death</text>
    <rect x="360" y="0" width="155" height="260" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="437" y="35" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="15" font-weight="bold">3. RESPONSE</text>
    <text x="437" y="80" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">The dead man</text>
    <text x="437" y="105" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">sat up &amp; spoke</text>
    <text x="437" y="150" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">Instant biological</text>
    <text x="437" y="175" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">&amp; neurological life</text>
    <rect x="540" y="0" width="155" height="260" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
    <text x="617" y="35" text-anchor="middle" fill="#c084fc" font-family="sans-serif" font-size="15" font-weight="bold">4. REUNION</text>
    <text x="617" y="80" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">Jesus gave him</text>
    <text x="617" y="105" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="12">back to his mother</text>
    <text x="617" y="150" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">Family covenant</text>
    <text x="617" y="175" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">restored in joy</text>
  </g>
  <text x="400" y="395" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="13">Luke 7:14-15 — 'The dead man sat up and began to talk, and Jesus gave him back to his mother.'</text>
</svg>"""

def get_svg_l4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">Core Christian Virtues Modeled by Jesus at Nain</text>
  <circle cx="400" cy="225" r="70" fill="#1e293b" stroke="#fbbf24" stroke-width="3"/>
  <text x="400" y="220" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">CHRISTLIKE</text>
  <text x="400" y="240" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">VIRTUES</text>
  <rect x="60" y="90" width="180" height="100" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="125" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="14" font-weight="bold">Compassion</text>
  <text x="150" y="155" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Deep visceral empathy</text>
  <rect x="560" y="90" width="180" height="100" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="650" y="125" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">Empathy &amp; Care</text>
  <text x="650" y="155" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Weeping with mourners</text>
  <rect x="60" y="260" width="180" height="100" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="8"/>
  <text x="150" y="295" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold">Generosity</text>
  <text x="150" y="325" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Giving life unconditionally</text>
  <rect x="560" y="260" width="180" height="100" fill="#1e293b" stroke="#c084fc" stroke-width="2" rx="8"/>
  <text x="650" y="295" text-anchor="middle" fill="#c084fc" font-family="sans-serif" font-size="14" font-weight="bold">Humility</text>
  <text x="650" y="325" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Serving without showmanship</text>
  <text x="400" y="410" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">Colossians 3:12 — 'Clothe yourselves with compassion, kindness, humility, gentleness and patience.'</text>
</svg>"""

def get_svg_l5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Compassion Action Model for Youth &amp; Church</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="16" font-weight="bold">Caring for Widows &amp; Orphans</text>
  <text x="75" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">1. Legal Defense &amp; Property Protection</text>
  <text x="75" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">2. Food &amp; Nutritional Relief</text>
  <text x="75" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">3. School Fees &amp; Bursary Support</text>
  <text x="75" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">4. Pastoral Bereavement Counseling</text>
  <text x="75" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">5. Eliminating Harmful Cultural Rites</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">Teenager Compassion in Action</text>
  <text x="455" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="13">1. Comforting Grieving Classmates</text>
  <text x="455" y="190" fill="#cbd5e1" font-family="sans-serif" font-size="13">2. Visiting Elderly &amp; Widowed Neighbors</text>
  <text x="455" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="13">3. Helping with Household Chores</text>
  <text x="455" y="260" fill="#cbd5e1" font-family="sans-serif" font-size="13">4. Sharing Academic Notes &amp; Lunch</text>
  <text x="455" y="295" fill="#cbd5e1" font-family="sans-serif" font-size="13">5. Standing Up Against Bullying</text>
  <text x="400" y="405" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">James 1:27 — 'Religion that God our Father accepts as pure and faultless is to look after orphans and widows.'</text>
</svg>"""

def get_svg_l6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">Resuscitation vs. Resurrection &amp; The Hope of Eternal Life</text>
  <rect x="50" y="80" width="320" height="280" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="210" y="115" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="16" font-weight="bold">Nain: Resuscitation (Miracle)</text>
  <text x="75" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Returned to Mortal Physical Body</text>
  <text x="75" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Still Subject to Sickness &amp; Aging</text>
  <text x="75" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Died Again in Later Years</text>
  <text x="75" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Sign of God's Kingdom Power</text>
  <rect x="430" y="80" width="320" height="280" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="590" y="115" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">Christ: Final Resurrection (Eternal)</text>
  <text x="455" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Transformed Glorified Body</text>
  <text x="455" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Imperishable, Immortal, Holy</text>
  <text x="455" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Never Dies Again (Romans 6:9)</text>
  <text x="455" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="13">• Firstfruits of All Believers</text>
  <text x="400" y="405" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold">John 11:25 — 'I am the resurrection and the life. The one who believes in me will live, even though they die.'</text>
</svg>"""

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR TOPIC 5 (6 LESSONS)
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        'unit_order': 1,
        'unit_name': 'Introduction to Nain, Loss, and Grief',
        'unit_desc': 'The geographic context of Nain, the tragedy of widowhood in the ancient world, and Christian responses to bereavement.',
        'lesson_title': 'Introduction to Nain, Loss, and Grief',
        'svg_fn': get_svg_l1,
        'image': {
            'title': 'The Historic Village of Nain in Galilee',
            'caption': 'Historical view of the village of Nain situated on the northern slope of the hill of Moreh overlooking the Plain of Jezreel.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Nain_from_Mount_Tabor.jpg/800px-Nain_from_Mount_Tabor.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'Public Domain'
        },
        'youtube': {
            'title': 'BibleProject: Luke 1-9 — Jesus and the Power of the Kingdom',
            'description': 'Exploring how Luke presents Jesus bringing the power of the kingdom of God to the poor, outcast, and grieving.',
            'youtube_id': 'dI-iY54n2aA'
        },
        'goals': [
            'Locate the village of Nain geographically and describe its biblical setting',
            'Explain the severe social and economic vulnerability of widows in ancient Israel',
            'Analyze healthy, empathetic Christian responses to grief and bereavement'
        ],
        'intro': 'Imagine the heartbreak of losing your only child after having already lost your spouse. In the ancient world, widowhood often meant poverty and social isolation. When Jesus entered the gate of Nain, everything changed.',
        'scripture': '### Luke 7:11-12
> "Soon afterward, Jesus went to a town called Nain, and his disciples and a large crowd went along with him. As he approached the town gate, a dead person was being carried out—the only son of his mother, and she was a widow. And a large crowd from the town was with her."

### Psalm 68:5
> "A father to the fatherless, a defender of widows, is God in his holy dwelling."

### Psalm 34:18
> "The Lord is close to the brokenhearted and saves those who are crushed in spirit."',
        'theology': 'God is the protector of the vulnerable and brokenhearted. In ancient Israel, a widow without sons lost her legal inheritance and economic support. Jesus purposely intercepted this tragedy to demonstrate God's unfailing mercy.',
        'deep_dive': '### Geography of Nain & The Plight of Ancient Widows
- **Geography:** Nain was a walled Galilean village on the slopes of Little Hermon, 35 km south of Capernaum.
- **Double Tragedy:** The woman was both a widow (lost her husband) and bereft of her only son (her economic and emotional future).
- **Communal Mourning:** The town gathered in solidarity, carrying the body in an open wicker bier to the burial tombs outside the city wall.
- **God's Covenant Compassion:** The encounter shows that God sees unseen suffering and intervenes with sovereign grace.',
        'process': {
            'title': 'Framework: 4-Step Christian Approach to Comforting Grieving Families',
            'steps': [
                {'step': 1, 'title': 'Present Silence & Empathy', 'description': 'Be physically present without offering hollow clichés; listen with compassion.'},
                {'step': 2, 'title': 'Practical Domestic Assistance', 'description': 'Provide meals, run errands, and assist with funeral arrangements.'},
                {'step': 3, 'title': 'Spiritual Comfort & Scripture', 'description': 'Share comforting Psalms and pray for God's peace that surpasses understanding.'},
                {'step': 4, 'title': 'Long-Term Bereavement Care', 'description': 'Continue visiting the family weeks and months after the funeral when loneliness sets in.'}
            ]
        },
        'context': 'In Kenya, communities rally during funerals through Harambee funeral committees. Christians are called to ensure ongoing support for widows and orphans beyond burial day, defending them from land grabbing.',
        'reflection': 'When you or a friend experienced a loss, what words or actions brought the greatest comfort? How does knowing God defends the brokenhearted bring you hope?',
        'summary': [
            'Nain was a Galilean village where Jesus intercepted a funeral procession of an only son.',
            'Widows in ancient Israel faced extreme economic and social vulnerability without male protectors.',
            'God is revealed in Scripture as the defender of widows and the comforter of the brokenhearted (Psalm 68:5).',
            'Christian empathy requires ongoing practical care and emotional support for grieving families.'
        ],
        'mcq': {
            'question': 'Why was the death of her son especially catastrophic for the widow of Nain in ancient Israel?',
            'options': [
                'A) Because she had to pay a large fine to the Roman governor.',
                'B) Because she lost her sole economic provider, legal inheritance protection, and family lineage.',
                'C) Because the villagers would force her to leave the town immediately.',
                'D) Because women were forbidden from attending funerals.'
            ],
            'answer': 'B',
            'explanation': 'In ancient patriarchal society, widows without surviving sons had no property rights or financial income, leaving them completely vulnerable to poverty and destitution.'
        }
    },
    {
        'unit_order': 2,
        'unit_name': 'The Encounter at the Gates of Nain',
        'unit_desc': 'The dramatic convergence of two processions at the city gate and the profound compassion of Jesus Christ.',
        'lesson_title': 'The Encounter at the Gates of Nain',
        'svg_fn': get_svg_l2,
        'image': {
            'title': 'Jesus Meeting the Funeral Procession at the Gate of Nain',
            'caption': 'Classical artistic representation of Jesus speaking words of divine comfort to the weeping widow at the entrance gate of Nain.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Jesus_raising_the_son_of_the_widow_of_Nain.jpg/800px-Jesus_raising_the_son_of_the_widow_of_Nain.jpg',
            'author': 'Lucas Cranach the Younger',
            'licensing': 'Public Domain'
        },
        'youtube': {
            'title': 'BibleProject: Compassion / Splagchnizomai',
            'description': 'Exploring the Greek concept of deep compassion (Splagchnizomai) that moved Jesus to heal the sick and raise the dead.',
            'youtube_id': '4T4r1c3oKkY'
        },
        'goals': [
            'Contrast the two crowds converging at the city gate of Nain (Procession of Life vs Death)',
            'Define biblical compassion (*splagchnizomai*) and describe Jesus' emotional response to the widow',
            'Explain the significance of Jesus' command "Do not cry"'
        ],
        'intro': 'At the city gate of Nain, two entirely different crowds collided: one walking out with death and despair, and another walking in with the Author of Life. What happens when Jesus steps into our deepest sorrow?',
        'scripture': '### Luke 7:12-13
> "As he approached the town gate, a dead person was being carried out—the only son of his mother, and she was a widow. And a large crowd from the town was with her. When the Lord saw her, his heart went out to her and he said, 'Don't cry.'"

### Matthew 9:36
> "When he saw the crowds, he had compassion on them, because they were harassed and helpless, like sheep without a shepherd."

### John 14:27
> "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid."',
        'theology': 'Jesus' compassion is not passive pity; it is *splagchnizomai*—a visceral, gut-wrenching divine love that compels miraculous action. When Jesus said "Do not cry", He was not dismissing her tears, but preparing to eliminate their cause.',
        'deep_dive': '### The Convergence of Two Processions
- **Procession of Death:** Moving out through the gate toward the cemetery, marked by wailing flutes, professional mourners, and tears of hopeless finality.
- **Procession of Life:** Moving into the gate led by Jesus and His joyful disciples who had witnessed the healing of the Centurion's servant.
- **The Divine Interception:** Jesus initiated the encounter unasked; no one asked Him for a miracle. His compassion moved Him to act sovereignly.
- **"Do Not Cry":** A declaration of divine hope that transforms despair into joy.',
        'process': {
            'title': 'Framework: 4 Steps to Cultivating Visceral Empathy in Daily Life',
            'steps': [
                {'step': 1, 'title': 'Observe Without Distraction', 'description': 'Notice quiet distress, isolation, and unvoiced sadness in peers.'},
                {'step': 2, 'title': 'Feel with the Brokenhearted', 'description': 'Allow your heart to be genuinely moved by another's pain (*splagchnizomai*).'},
                {'step': 3, 'title': 'Speak Words of Hope & Comfort', 'description': 'Offer encouraging, life-giving words that lift despair.'},
                {'step': 4, 'title': 'Take Immediate Tangible Action', 'description': 'Intervene practically to relieve burdens without waiting to be asked.'}
            ]
        },
        'context': 'In Kenyan culture, communal respect during bereavement is paramount. When passing a funeral cortège, people stop and remove hats. Jesus went beyond solemn respect by bringing life and restoration.',
        'reflection': 'Have you ever noticed a classmate sitting alone and crying? What stops us from stepping forward with compassion? How can Jesus' example inspire you?',
        'summary': [
            'At the gate of Nain, the Procession of Death encountered Jesus, the Prince of Life.',
            'Jesus acted unprompted because His heart was moved with deep compassion (*splagchnizomai*).',
            'His command "Don't cry" was a divine promise of imminent restoration and joy.',
            'True Christian compassion moves beyond passive sympathy into transformative action.'
        ],
        'mcq': {
            'question': 'What does the Greek word *splagchnizomai*, used to describe Jesus' reaction to the widow, mean?',
            'options': [
                'A) Mild intellectual curiosity.',
                'B) Deep, gut-wrenching visceral compassion that drives a person to take action.',
                'C) Strict adherence to religious legal ritual.',
                'D) Frustration with human weakness.'
            ],
            'answer': 'B',
            'explanation': '*Splagchnizomai* refers to profound empathy felt in one's innermost core that compels immediate, compassionate intervention.'
        }
    },
    {
        'unit_order': 3,
        'unit_name': 'The Miracle of Nain: Raising the Dead',
        'unit_desc': 'Jesus touching the funeral bier, commanding the dead man to arise, and restoring him to his mother.',
        'lesson_title': 'The Miracle of Nain: Raising the Dead',
        'svg_fn': get_svg_l3,
        'image': {
            'title': 'The Dead Youth Sitting Up and Speaking at Nain',
            'caption': 'Nineteenth-century engraving depicting the young man sitting up on the funeral bier and Jesus giving him back to his mother.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Raising_of_the_widow%27s_son.jpg/800px-Raising_of_the_widow%27s_son.jpg',
            'author': 'Julius Schnorr von Carolsfeld',
            'licensing': 'Public Domain'
        },
        'youtube': {
            'title': 'BibleProject: The Gospel of the Kingdom — Miracles and Authority',
            'description': 'How Jesus' miracles over sickness, nature, and death demonstrated the presence of God's restored creation.',
            'youtube_id': 'xmFPS0445X4'
        },
        'goals': [
            'Analyze the four sequential actions of Jesus in performing the miracle at Nain',
            'Explain the ritual implications of Jesus touching the funeral bier (Numbers 19:11-16)',
            'Discuss the crowd's reaction and recognition of Jesus as a great prophet visiting His people'
        ],
        'intro': 'Touching a dead body or a funeral bier made a person ritually unclean for seven days under Levitical law. Yet when Jesus reached out His hand and touched the coffin, death was swallowed up in holiness and life!',
        'scripture': '### Luke 7:14-16
> "Then he went up and touched the bier they were carrying him on, and the bearers stood still. He said, 'Young man, I say to you, get up!' The dead man sat up and began to talk, and Jesus gave him back to his mother. They were all filled with awe and praised God. 'A great prophet has appeared among us,' they said. 'God has come to help his people.'"

### John 5:21
> "For just as the Father raises the dead and gives them life, even so the Son gives life to whom he is pleased to give it."

### Numbers 19:11
> "Whoever touches a human corpse will be unclean for seven days."',
        'theology': 'Jesus is the Author of Life. Instead of contracting ceremonial impurity by touching the bier, Jesus' holy divine nature imparted life and purity, completely reversing decay and death by His authoritative spoken word.',
        'deep_dive': '### The Fourfold Sequential Act of Resurrection
- **1. The Touch:** Jesus stepped forward and touched the open wicker bier. The pallbearers stopped dead in their tracks.
- **2. The Command:** Jesus spoke directly to the corpse: *"Young man, I say to you, arise!"* He did not pray for power; He commanded by His own sovereign authority.
- **3. The Evidence of Life:** The deceased sat up immediately and began to speak, demonstrating complete neurological and biological restoration.
- **4. The Reunion:** Jesus tenderly *"gave him back to his mother"*, restoring family protection, love, and community honor.
- **The Response:** Fear and awe swept the crowd, declaring *"God has visited His people!"* echoing Elijah raising the widow's son at Zarephath (1 Kings 17).',
        'process': {
            'title': 'Framework: 4 Principles of Relying on Christ's Sovereign Authority',
            'steps': [
                {'step': 1, 'title': 'Acknowledge Human Limitations', 'description': 'Recognize that human strength cannot conquer sin, despair, or death.'},
                {'step': 2, 'title': 'Trust Christ's Spoken Word', 'description': 'Stand firm on biblical promises with unshakeable faith in God's power.'},
                {'step': 3, 'title': 'Embrace Divine Transformation', 'description': 'Allow Christ's touch to renew your mind, desires, and moral habits.'},
                {'step': 4, 'title': 'Testify to God's Goodness', 'description': 'Praise God publicly for His interventions and share your testimony.'}
            ]
        },
        'context': 'In Kenya, traditional taboos regarding death and corpses are strong. Jesus shows that God's holiness is stronger than any curse, fear, or ritual pollution, freeing believers from fear of death.',
        'reflection': 'Why did Jesus say "Young man, I say to you, arise" instead of asking God for permission? What does this reveal about His divine identity?',
        'summary': [
            'Jesus broke ritual taboos by touching the funeral bier, imparting life rather than catching impurity.',
            'By His own sovereign authority, Jesus commanded the dead youth to rise.',
            'The youth sat up and spoke, providing undeniable proof of physical resurrection.',
            'The crowd praised God, declaring that a great prophet had appeared and God had visited His people.'
        ],
        'mcq': {
            'question': 'What was the immediate physical proof that the widow's son was fully resurrected and alive?',
            'options': [
                'A) He immediately ran into the desert.',
                'B) He sat up on the bier and began to speak, and Jesus gave him back to his mother.',
                'C) He requested a large meal from the pallbearers.',
                'D) He started preaching to the Roman soldiers.'
            ],
            'answer': 'B',
            'explanation': 'Luke records that the dead man sat up and began to talk, demonstrating full return of breath, brain function, and voice.'
        }
    },
    {
        'unit_order': 4,
        'unit_name': 'Virtues Learnt from the Miracle',
        'unit_desc': 'Christian virtues exemplified by Jesus and required of disciples: compassion, kindness, empathy, generosity, and humility.',
        'lesson_title': 'Virtues Learnt from the Miracle',
        'svg_fn': get_svg_l4,
        'image': {
            'title': 'Acts of Christian Mercy and Compassionate Service',
            'caption': 'Christian volunteers practicing compassion, kindness, and practical care among the needy in an urban community.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Charity_care_service.jpg/800px-Charity_care_service.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Colossians — The New Humanity and Clothed in Virtue',
            'description': 'Exploring how believers put on compassion, kindness, humility, and love as members of Christ's new covenant family.',
            'youtube_id': 'pXTXlDxQ1b4'
        },
        'goals': [
            'Identify and define the key Christian virtues modeled by Jesus at Nain',
            'Explain how compassion, kindness, and humility counteract selfishness and callousness in society',
            'Apply Colossians 3:12 to daily adolescent relationships at school and home'
        ],
        'intro': 'A great miracle does not only reveal supernatural power; it reveals the character of God. In raising the widow's son, Jesus demonstrated a cluster of beautiful virtues that every Christian teenager is called to put on daily.',
        'scripture': '### Colossians 3:12-14
> "Therefore, as God's chosen people, holy and dearly loved, clothe yourselves with compassion, kindness, humility, gentleness and patience. Bear with each other and forgive one another... And over all these virtues put on love, which binds them all together in perfect unity."

### Luke 7:13
> "When the Lord saw her, his heart went out to her."

### Micah 6:8
> "He has shown you, O mortal, what is good. And what does the Lord require of you? To act justly and to love mercy and to walk humbly with your God."',
        'theology': 'Virtues are the moral fruit of a life transformed by the Holy Spirit. Jesus is the supreme embodiment of divine love. Disciples are called to "clothe" themselves with Christlike character, actively blessing those who cannot repay them.',
        'deep_dive': '### The Cluster of Christlike Virtues at Nain
- **Compassion (*Splagchnizomai*):** Feeling deep visceral sympathy that leads to sacrificial action.
- **Kindness:** Tender, benevolent consideration for the dignity and feelings of others.
- **Empathy:** Walking in another person's shoes; weeping with those who weep (Rom 12:15).
- **Generosity:** Giving life, time, and comfort unconditionally without expecting repayment.
- **Humility:** Exercising mighty power gently to serve the vulnerable rather than seeking fame.',
        'process': {
            'title': 'Framework: 4 Steps for Teenagers to Practice Everyday Kindness & Humility',
            'steps': [
                {'step': 1, 'title': 'Practice Active Listening', 'description': 'Give full attention to friends facing challenges without interrupting.'},
                {'step': 2, 'title': 'Perform Quiet Acts of Mercy', 'description': 'Help struggling classmates with homework or chores without boasting.'},
                {'step': 3, 'title': 'Include the Isolated', 'description': 'Invite lonely, shy, or marginalized students to join your study group or meal table.'},
                {'step': 4, 'title': 'Forgive Graciously', 'description': 'Refuse revenge and let go of petty grudges with Christlike patience.'}
            ]
        },
        'context': 'In Kenyan schools, peer bullying and cliques cause loneliness. Practicing Christlike virtues through Christian Unions, Peer Counselors, and Scouts builds a supportive school culture.',
        'reflection': 'Which virtue mentioned in Colossians 3:12 (compassion, kindness, humility, gentleness, patience) is most challenging for you to practice? How can you pray for growth in it?',
        'summary': [
            'Jesus' actions at Nain model compassion, empathy, kindness, generosity, and humility.',
            'Christian virtues are moral garments that believers "put on" daily through the Holy Spirit (Col 3:12).',
            'Humility uses strength to serve the vulnerable without showmanship or selfish ambition.',
            'Active kindness transforms school environments by tearing down bullying and isolation.'
        ],
        'mcq': {
            'question': 'According to Colossians 3:12, what are believers instructed to "clothe" themselves with?',
            'options': [
                'A) Expensive ceremonial robes and jewelry.',
                'B) Compassion, kindness, humility, gentleness, and patience.',
                'C) Pride, competitiveness, and assertiveness in dominance.',
                'D) Cold indifference toward personal emotions.'
            ],
            'answer': 'B',
            'explanation': 'Paul exhorts the church to dress spiritually in the character of Christ: compassion, kindness, humility, gentleness, and patience.'
        }
    },
    {
        'unit_order': 5,
        'unit_name': 'Compassion in Action Today',
        'unit_desc': 'Practical Christian care for widows, orphans, the sick, and marginalized communities in modern Kenya.',
        'lesson_title': 'Compassion in Action Today',
        'svg_fn': get_svg_l5,
        'image': {
            'title': 'Community Support for Widows and Vulnerable Children',
            'caption': 'Community volunteers distributing food and educational supplies to widows and orphans in Kenya.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Community_relief_aid_africa.jpg/800px-Community_relief_aid_africa.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Matthew 25 — The Sheep and the Goats',
            'description': 'How Jesus identifies Himself with the poor, hungry, sick, and imprisoned: "Whatever you did for the least of these, you did for me."',
            'youtube_id': 'oLYORLZOaZE'
        },
        'goals': [
            'Explain the biblical mandate to protect and support widows and orphans (James 1:27, Matthew 25:35-40)',
            'Identify the contemporary challenges faced by widows and vulnerable children in Kenya',
            'Formulate practical community outreach initiatives that Grade 9 learners can implement'
        ],
        'intro': 'True religion is not just singing hymns on Sunday; it is visiting the elderly widow, defending the orphan, and feeding the hungry. How can young Christians become Jesus' hands and feet in Kenya today?',
        'scripture': '### James 1:27
> "Religion that God our Father accepts as pure and faultless is this: to look after orphans and widows in their distress and to keep oneself from being polluted by the world."

### Matthew 25:40
> "The King will reply, 'Truly I tell you, whatever you did for one of the least of these brothers and sisters of mine, you did for me.'"

### Isaiah 1:17
> "Learn to do right; seek justice. Defend the oppressed. Take up the cause of the fatherless; plead the case of the widow."',
        'theology': 'God measures the authenticity of our faith by how we treat the weakest members of society. Serving the marginalized is direct worship and service rendered to King Jesus Himself.',
        'deep_dive': '### Challenges & Church Action in Kenya
- **Plight of Widows:** Property disinheritance, land grabbing by in-laws, emotional trauma, and extreme poverty.
- **Plight of Orphans:** School dropouts, child labor, malnutrition, and lack of medical care.
- **Church Interventions:** Legal aid clinics to protect land titles, sponsorship bursaries for schooling, food distribution SACCOs, and psychological support.
- **Youth Action:** Volunteering at children's homes, cleaning homes of elderly widows, collecting clothes, and tutoring younger orphans.',
        'process': {
            'title': 'Framework: 4-Step Youth Compassion Project for Local Communities',
            'steps': [
                {'step': 1, 'title': 'Needs Assessment', 'description': 'Identify vulnerable widows, orphans, or sick persons in your neighborhood.'},
                {'step': 2, 'title': 'Mobilize Resources', 'description': 'Collect dry foodstuffs, soap, clothing, and books through school or church clubs.'},
                {'step': 3, 'title': 'Execute Service Day', 'description': 'Visit the home, fetch water, chop firewood, clean the compound, and share a meal.'},
                {'step': 4, 'title': 'Sustain Relationships', 'description': 'Establish regular monthly visits and pray consistently for the family.'}
            ]
        },
        'context': 'In Kenya, the Law of Succession Act protects widows' inheritance rights, and community welfare groups like Nyumba Kumi and church Dorcas ministries support bereaved families.',
        'reflection': 'When was the last time you assisted a widow or orphan in your village or estate? How does Jesus' declaration in Matthew 25:40 motivate your charity?',
        'summary': [
            'Pure and undefiled religion before God requires caring for widows and orphans in distress (James 1:27).',
            'Serving the poor and marginalized is direct service to Jesus Christ Himself (Matthew 25:40).',
            'Widows in Kenya face challenges like property disinheritance that require legal and material protection.',
            'Teenagers can practice compassion through practical domestic chores, food drives, and fellowship.'
        ],
        'mcq': {
            'question': 'According to James 1:27, what constitutes pure and faultless religion in the sight of God?',
            'options': [
                'A) Fasting seven days a week in total seclusion.',
                'B) Looking after orphans and widows in their distress and keeping oneself unstained by the world.',
                'C) Building the largest physical cathedral in the capital city.',
                'D) Memorizing all biblical genealogies without error.'
            ],
            'answer': 'B',
            'explanation': 'James explicitly defines pure religion as active compassion toward orphans and widows combined with personal moral purity.'
        }
    },
    {
        'unit_order': 6,
        'unit_name': 'The Christian Belief in the Resurrection',
        'unit_desc': 'The theological distinction between resuscitation and resurrection, Christ as the firstfruits, and eternal life.',
        'lesson_title': 'The Christian Belief in the Resurrection',
        'svg_fn': get_svg_l6,
        'image': {
            'title': 'The Empty Tomb and the Resurrection of Jesus Christ',
            'caption': 'Artistic representation of the empty tomb on Easter morning, symbolizing Christ's triumph over death and the promise of eternal life.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/The_Resurrection_-_Piero_della_Francesca.jpg/800px-The_Resurrection_-_Piero_della_Francesca.jpg',
            'author': 'Piero della Francesca',
            'licensing': 'Public Domain'
        },
        'youtube': {
            'title': 'BibleProject: 1 Corinthians 15 — The Resurrection and the Hope of Glory',
            'description': 'Exploring how Jesus' resurrection guarantees bodily resurrection, new creation, and victory over the final enemy: death.',
            'youtube_id': '6Y2tQ_Mvj9Q'
        },
        'goals': [
            'Distinguish between physical resuscitation (temporary) and bodily resurrection (eternal)',
            'Explain biblical teachings on Jesus Christ as the firstfruits of the resurrection (1 Corinthians 15:20-22)',
            'Articulate how the hope of resurrection removes the fear of death for Christian believers'
        ],
        'intro': 'The young man of Nain was brought back to his mortal body and eventually died again years later. But Jesus rose from the grave with an immortal, glorified body never to die again! What is the true Christian hope of resurrection?',
        'scripture': '### 1 Corinthians 15:20-22
> "But Christ has indeed been raised from the dead, the firstfruits of those who have fallen asleep. For since death came through a man, the resurrection of the dead comes also through a man. For as in Adam all die, so in Christ all will be made alive."

### John 11:25-26
> "Jesus said to her, 'I am the resurrection and the life. The one who believes in me will live, even though they die; and whoever lives by believing in me will never die. Do you believe this?'"

### Romans 6:9
> "For we know that since Christ was raised from the dead, he cannot die again; death no longer has mastery over him."',
        'theology': 'The resurrection is the cornerstone of Christian theology. Jesus conquered death, hell, and the grave. The miracle at Nain was a prophetic sign pointing forward to the ultimate, eternal resurrection of all believers into incorruptible life.',
        'deep_dive': '### Resuscitation vs. Resurrection
- **Resuscitation (The Miracle at Nain):** Restoration of physical life into a mortal body. The widow's son grew older, was still subject to disease, and experienced physical death later.
- **Resurrection (Easter / Eternal Life):** Transformation into a glorified, imperishable, immortal spiritual body (1 Cor 15:42-44) that will never suffer, decay, or die again.
- **Christ the Firstfruits:** Just as the first sheaf of harvest guaranteed the full harvest, Christ's resurrection guarantees the resurrection of all who trust in Him.
- **Victory Over Fear:** Christians grieve with hope (1 Thess 4:13), knowing that death is not the end, but the gateway into the presence of God.',
        'process': {
            'title': 'Framework: 4 Anchors for Living with Resurrection Hope and Boldness',
            'steps': [
                {'step': 1, 'title': 'Anchor in Christ's Victory', 'description': 'Trust daily that Jesus has conquered sin, sorrow, and physical death.'},
                {'step': 2, 'title': 'Live for Eternal Values', 'description': 'Prioritize spiritual growth and kingdom service over temporary earthly wealth.'},
                {'step': 3, 'title': 'Comfort Grieving Believers', 'description': 'Remind brothers and sisters of the promised reunion in God's presence.'},
                {'step': 4, 'title': 'Proclaim the Gospel', 'description': 'Share the message of forgiveness and eternal life with boldness and love.'}
            ]
        },
        'context': 'In African traditional religion, ancestors (*the living-dead*) remain tied to memories. In Christian belief, departed believers are alive with Christ, awaiting the final bodily resurrection at His return.',
        'reflection': 'Jesus asked Martha, "Do you believe this?" How does your personal belief in the resurrection change how you face fear, danger, and the loss of loved ones?',
        'summary': [
            'The miracle at Nain was a physical resuscitation pointing forward to the final eternal resurrection.',
            'Christ's resurrection guarantees that believers will receive glorified, imperishable bodies (1 Cor 15).',
            'Christ is the "firstfruits", the pledge and guarantee of our future victory over death.',
            'The hope of resurrection removes despair and gives believers courage to live holy, fearless lives.'
        ],
        'mcq': {
            'question': 'How does Christ's resurrection differ fundamentally from the raising of the widow's son at Nain?',
            'options': [
                'A) The widow's son did not actually die, but was merely asleep.',
                'B) The widow's son was resuscitated to a mortal body and died again later, whereas Christ rose with an immortal, glorified body never to die again.',
                'C) Christ rose through human medical assistance.',
                'D) There was no difference between the two events.'
            ],
            'answer': 'B',
            'explanation': 'The miracle at Nain was a temporary return to mortal earthly life, while Jesus' resurrection inaugurated eternal, glorified life over which death has no power (Romans 6:9).'
        }
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# EXECUTE INGESTION TRANSACTION
# ─────────────────────────────────────────────────────────────────────────────

with transaction.atomic():
    grade9 = Grade.objects.get(id=18)
    cre, _ = Subject.objects.get_or_create(grade=grade9, name='CRE', defaults={'description': 'CBC Grade 9 Christian Religious Education'})

    topic5, _ = Topic.objects.get_or_create(
        subject=cre,
        order=5,
        defaults={
            'name': "Raising the Widow's Son at Nain",
            'description': 'The historical, theological, and moral implications of Jesus raising the widow's son at Nain, virtues of compassion, care for widows/orphans, and resurrection hope.'
        }
    )
    topic5.name = "Raising the Widow's Son at Nain"
    topic5.description = 'The historical, theological, and moral implications of Jesus raising the widow's son at Nain, virtues of compassion, care for widows/orphans, and resurrection hope.'
    topic5.save()

    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    for cfg in LESSONS_CONFIG:
        unit_obj, _ = LearningUnit.objects.get_or_create(
            topic=topic5,
            order=cfg['unit_order'],
            defaults={'name': cfg['unit_name'], 'description': cfg['unit_desc']}
        )
        unit_obj.name = cfg['unit_name']
        unit_obj.description = cfg['unit_desc']
        unit_obj.save()

        unit_obj.lessons.all().delete()

        lesson = Lesson.objects.create(
            topic=topic5,
            learning_unit=unit_obj,
            title=cfg['lesson_title'],
            status='published',
            version=1,
            immutable_metadata={
                'grade': 'Grade 9',
                'subject': 'CRE',
                'topic_order': 5,
                'topic_name': "Raising the Widow's Son at Nain",
                'unit_order': cfg['unit_order'],
                'author': 'VLearn CRE Ingestion Engine',
                'curriculum_framework': 'CBC Kenya',
                'enrichment_version': 'v3_pedagogical'
            }
        )
        total_lessons += 1

        img_info = cfg['image']
        img_asset = LessonAsset.objects.create(
            lesson=lesson, asset_type='image', source_type='external', storage_type='url', status='attached',
            title=img_info['title'], description=img_info['caption'], url=img_info['url'],
            metadata={'author': img_info['author'], 'licensing': img_info['licensing'], 'caption': img_info['caption']}
        )
        total_assets += 1

        svg_content = cfg['svg_fn']()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson, asset_type='diagram', source_type='ai_generated', storage_type='url', status='attached',
            title=f"Diagram: {cfg['lesson_title']}",
            description=f"Responsive vector diagram illustrating {cfg['lesson_title']}.",
            url=f"https://vlearn.africa/assets/cre/t5_l{cfg['unit_order']}.svg",
            metadata={'svg_xml': svg_content, 'viewBox': '0 0 800 450', 'theme': '#0f172a'}
        )
        total_assets += 1

        yt_info = cfg['youtube']
        yt_asset = LessonAsset.objects.create(
            lesson=lesson, asset_type='youtube', source_type='external', storage_type='url', status='attached',
            title=yt_info['title'], description=yt_info['description'],
            url=f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
            metadata={'youtube_id': yt_info['youtube_id'], 'embed_url': f"https://www.youtube.com/embed/{yt_info['youtube_id']}"}
        )
        total_assets += 1

        # Card 1
        b1 = LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title='Discovery & Objectives', order=10, component_order=1,
            block_type='suggested_image', component_type='suggested_image', title=img_info['title'],
            content={'title': img_info['title'], 'url': img_info['url'], 'caption': img_info['caption'], 'author': img_info['author'], 'licensing': img_info['licensing']}
        )
        b1.assets.add(img_asset)
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title='Discovery & Objectives', order=20, component_order=2,
            block_type='learning_goal', component_type='learning_goal', title='Lesson Objectives',
            content={'goals': cfg['goals']}
        )
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title='Discovery & Objectives', order=30, component_order=3,
            block_type='concept_explanation', component_type='concept_explanation', title='Sharing Experiences & Familiar Connection',
            content={'markdown': cfg['intro']}
        )
        total_blocks += 1

        # Card 2
        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title='Scriptural Exegesis', order=40, component_order=1,
            block_type='concept_explanation', component_type='concept_explanation', title='Core Biblical Foundations',
            content={'markdown': cfg['scripture']}
        )
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title='Scriptural Exegesis', order=45, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Theological Foundations & Principles',
            content={'markdown': cfg['theology']}
        )
        total_blocks += 1

        # Card 3
        b3 = LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title='Pedagogical Diagram', order=50, component_order=1,
            block_type='suggested_diagram', component_type='suggested_diagram', title=f"Visual Architecture: {cfg['lesson_title']}",
            content={'title': f"Visual Architecture: {cfg['lesson_title']}", 'svg': svg_content, 'svg_xml': svg_content}
        )
        b3.assets.add(svg_asset)
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title='Pedagogical Diagram', order=60, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Theological Deep Dive & Analysis',
            content={'markdown': cfg['deep_dive']}
        )
        total_blocks += 1

        # Card 4
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title='Practical Application', order=70, component_order=1,
            block_type='step_process', component_type='step_process', title=cfg['process']['title'],
            content=cfg['process']
        )
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title='Practical Application', order=75, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Kenyan Real-World Context & Integration',
            content={'markdown': cfg['context']}
        )
        total_blocks += 1

        # Card 5
        b5 = LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title='Multimedia & Reflection', order=80, component_order=1,
            block_type='suggested_video', component_type='suggested_video', title=yt_info['title'],
            content={'title': yt_info['title'], 'url': f"https://www.youtube.com/watch?v={yt_info['youtube_id']}", 'youtube_id': yt_info['youtube_id'], 'description': yt_info['description']}
        )
        b5.assets.add(yt_asset)
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title='Multimedia & Reflection', order=90, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Spiritual Reflection & Ethical Introspection',
            content={'markdown': cfg['reflection']}
        )
        total_blocks += 1

        # Card 6
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title='Mastery Check', order=100, component_order=1,
            block_type='summary', component_type='summary', title='Summary & Key Takeaways',
            content={'points': cfg['summary']}
        )
        total_blocks += 1

        mcq_data = cfg['mcq']
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title='Mastery Check', order=110, component_order=2,
            block_type='knowledge_check', component_type='knowledge_check', title='Formative Knowledge Check',
            content={
                'check_type': 'multiple_choice',
                'question': mcq_data['question'],
                'options': mcq_data['options'],
                'answer': mcq_data['answer'],
                'explanation': mcq_data['explanation']
            }
        )
        total_blocks += 1

        print(f"[✓] Ingested Topic 5 Unit {cfg['unit_order']}: {cfg['lesson_title']} (Lesson ID: {lesson.id})")

    print(f"
================================================================================")
    print(f"TOPIC 5 INGESTION COMPLETE: {total_lessons} Lessons, {total_blocks} Blocks, {total_assets} Assets.")
    print(f"================================================================================")
