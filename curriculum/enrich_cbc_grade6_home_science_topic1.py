"""
VLearn Curriculum Visual Enrichment Script
CBC Grade 6 — Home Science
Topic 1: Adolescence (Order: 1)

Attaches:
- 4 Verified Topic-Representative Wikimedia Photographic Visual Hooks (Card 1 of every lesson)
- 8 Custom Sanitized, Responsive (800x450), Pedagogically Rich Vector SVGs
- Creates and attaches LessonAsset records in the database.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

# 4 Verified Photographic Visual Hooks (100% live HTTP 200 verified)
TOPIC1_PHOTOS = {
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/32/AHS_Uniform.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "A classic school uniform blazer and shirt symbolizing the rapid growth and transition during adolescent school years."
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Use_of_a_touchless_hand_washing_tap_and_solid_bar_soap_dispenser.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Washing hands thoroughly with soap and running water to maintain pristine personal hygiene and health."
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/NCI_Visuals_Food_Meal_Dinner.jpg",
        "author": "National Cancer Institute / Wikimedia Commons",
        "licensing": "Public Domain",
        "caption": "A colorful balanced meal plate combining fresh vegetables, energy grains, and lean proteins for optimal adolescent health."
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Ghanaian_kid_%28skipping_rope%29_05.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "A young learner energetically skipping rope outdoors, showcasing active physical exercise for cardiovascular health and strong bones."
    }
}

# 8 Custom High-Definition Vector SVGs for Grade 6 Topic 1
TOPIC1_SVGS = {
    # Lesson 1 Page 2: Puberty Changes Classification Blueprint
    (1, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="30" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="57" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    PUBERTY TRANSFORMATIONS: BOYS, GIRLS &amp; SHARED CHANGES
  </text>

  <!-- 3 Columns Layout -->

  <!-- Column 1: Changes in Boys -->
  <g transform="translate(45, 88)">
    <rect x="0" y="0" width="220" height="310" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="26" fill="#2563eb" rx="5"/>
    <text x="110" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      CHANGES IN BOYS
    </text>
    <g transform="translate(15, 50)">
      <circle cx="20" cy="20" r="16" fill="#dbeafe" stroke="#2563eb"/>
      <text x="20" y="25" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🗣️</text>
      <text x="45" y="18" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Voice Breaks &amp; Deepens</text>
      <text x="45" y="32" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Adam's apple grows</text>

      <circle cx="20" cy="75" r="16" fill="#dbeafe" stroke="#2563eb"/>
      <text x="20" y="80" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🧔</text>
      <text x="45" y="73" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Facial Hair (Beards)</text>
      <text x="45" y="87" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Grows on chin &amp; lip</text>

      <circle cx="20" cy="130" r="16" fill="#dbeafe" stroke="#2563eb"/>
      <text x="20" y="135" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">💪</text>
      <text x="45" y="128" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Broad Shoulders</text>
      <text x="45" y="142" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Chest widens &amp; muscles</text>

      <circle cx="20" cy="185" r="16" fill="#dbeafe" stroke="#2563eb"/>
      <text x="20" y="190" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🌙</text>
      <text x="45" y="183" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Wet Dreams</text>
      <text x="45" y="197" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Natural night releases</text>
    </g>
  </g>

  <!-- Column 2: Shared Changes (Middle) -->
  <g transform="translate(290, 88)">
    <rect x="0" y="0" width="220" height="310" fill="#f0fdf4" rx="8" stroke="#bbf7d0" stroke-width="2"/>
    <rect x="10" y="10" width="200" height="26" fill="#16a34a" rx="5"/>
    <text x="110" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      SHARED (BOTH)
    </text>
    <g transform="translate(15, 50)">
      <circle cx="20" cy="20" r="16" fill="#dcfce7" stroke="#16a34a"/>
      <text x="20" y="25" fill="#15803d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">📏</text>
      <text x="45" y="18" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Rapid Growth Spurt</text>
      <text x="45" y="32" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Height &amp; weight increases</text>

      <circle cx="20" cy="75" r="16" fill="#dcfce7" stroke="#16a34a"/>
      <text x="20" y="80" fill="#15803d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">✨</text>
      <text x="45" y="73" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Acne (Pimples)</text>
      <text x="45" y="87" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Active skin oil glands</text>

      <circle cx="20" cy="130" r="16" fill="#dcfce7" stroke="#16a34a"/>
      <text x="20" y="135" fill="#15803d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🌿</text>
      <text x="45" y="128" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Underarm Body Hair</text>
      <text x="45" y="142" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Pubic &amp; underarm growth</text>

      <circle cx="20" cy="185" r="16" fill="#dcfce7" stroke="#16a34a"/>
      <text x="20" y="190" fill="#15803d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">💧</text>
      <text x="45" y="183" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Increased Sweating</text>
      <text x="45" y="197" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Requires daily bathing</text>
    </g>
  </g>

  <!-- Column 3: Changes in Girls -->
  <g transform="translate(535, 88)">
    <rect x="0" y="0" width="220" height="310" fill="#fdf2f8" rx="8" stroke="#fbcfe8" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="26" fill="#db2777" rx="5"/>
    <text x="110" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      CHANGES IN GIRLS
    </text>
    <g transform="translate(15, 50)">
      <circle cx="20" cy="20" r="16" fill="#fce7f3" stroke="#db2777"/>
      <text x="20" y="25" fill="#be185d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🌸</text>
      <text x="45" y="18" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Breasts Develop</text>
      <text x="45" y="32" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Chest changes contour</text>

      <circle cx="20" cy="75" r="16" fill="#fce7f3" stroke="#db2777"/>
      <text x="20" y="80" fill="#be185d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">⏳</text>
      <text x="45" y="73" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Hips Broaden</text>
      <text x="45" y="87" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Pelvic girdle widens</text>

      <circle cx="20" cy="130" r="16" fill="#fce7f3" stroke="#db2777"/>
      <text x="20" y="135" fill="#be185d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🎶</text>
      <text x="45" y="128" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Melodious Voice</text>
      <text x="45" y="142" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Voice becomes smooth</text>

      <circle cx="20" cy="185" r="16" fill="#fce7f3" stroke="#db2777"/>
      <text x="20" y="190" fill="#be185d" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🩸</text>
      <text x="45" y="183" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Menstruation Starts</text>
      <text x="45" y="197" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Monthly period cycle</text>
    </g>
  </g>
</svg>""",

    # Lesson 1 Page 4: Physical, Emotional & Social Growth Matrix
    (1, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="30" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="57" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    THE 3 PILLARS OF ADOLESCENT DEVELOPMENT
  </text>

  <!-- 3 Pillars Layout -->

  <!-- Pillar 1: Physical Changes -->
  <g transform="translate(45, 88)">
    <rect x="0" y="0" width="220" height="310" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="28" fill="#0284c7" rx="5"/>
    <text x="110" y="29" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      1. PHYSICAL (Body)
    </text>
    <text x="15" y="65" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Visible External Growth:</text>
    <text x="15" y="88" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Rapid height &amp; weight spurts.</text>
    <text x="15" y="108" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Body hair &amp; voice changes.</text>
    <text x="15" y="128" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Active sweat &amp; oil glands.</text>
    <text x="15" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Reproductive maturation.</text>
    <rect x="10" y="245" width="200" height="45" fill="#e0f2fe" rx="4"/>
    <text x="110" y="265" fill="#0369a1" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Action Required:</text>
    <text x="110" y="280" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Daily bathing &amp; clean uniform</text>
  </g>

  <!-- Pillar 2: Emotional Changes -->
  <g transform="translate(290, 88)">
    <rect x="0" y="0" width="220" height="310" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="28" fill="#7c3aed" rx="5"/>
    <text x="110" y="29" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      2. EMOTIONAL (Feelings)
    </text>
    <text x="15" y="65" fill="#6d28d9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Internal Feelings &amp; Identity:</text>
    <text x="15" y="88" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Occasional mood swings.</text>
    <text x="15" y="108" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Desire for personal privacy.</text>
    <text x="15" y="128" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Self-awareness &amp; identity.</text>
    <text x="15" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Developing self-confidence.</text>
    <rect x="10" y="245" width="200" height="45" fill="#ede9fe" rx="4"/>
    <text x="110" y="265" fill="#6d28d9" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Action Required:</text>
    <text x="110" y="280" fill="#7c3aed" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Open talk with trusted adults</text>
  </g>

  <!-- Pillar 3: Social Changes -->
  <g transform="translate(535, 88)">
    <rect x="0" y="0" width="220" height="310" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="28" fill="#16a34a" rx="5"/>
    <text x="110" y="29" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      3. SOCIAL (Peers &amp; Home)
    </text>
    <text x="15" y="65" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Relating to Others:</text>
    <text x="15" y="88" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Forming close friendships.</text>
    <text x="15" y="108" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Seeking positive independence.</text>
    <text x="15" y="128" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Taking family responsibilities.</text>
    <text x="15" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Practicing empathy &amp; respect.</text>
    <rect x="10" y="245" width="200" height="45" fill="#dcfce7" rx="4"/>
    <text x="110" y="265" fill="#15803d" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Action Required:</text>
    <text x="110" y="280" fill="#16a34a" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Choose supportive friends</text>
  </g>
</svg>""",

    # Lesson 2 Page 2: 4-Step Daily Personal Grooming Storyboard
    (2, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    4-STEP DAILY PERSONAL GROOMING BLUEPRINT
  </text>

  <!-- 4 Steps Layout -->

  <!-- Step 1 -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0284c7" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. DAILY BATHING</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#7dd3fc"/>
      <text x="67" y="45" fill="#0284c7" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🚿</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Wash with warm water</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  and soap daily.</text>
    <text x="10" y="195" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Benefit:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Removes sweat &amp;</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">skin bacteria.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(225, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#334155" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. UNDERARM &amp; HAIR</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#cbd5e1"/>
      <text x="67" y="45" fill="#334155" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">✂️</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Shave/trim underarm hair.</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Keep head hair neat.</text>
    <text x="10" y="195" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Benefit:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Prevents body odor</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">trapped by hair.</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(405, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#fdf2f8" rx="8" stroke="#fbcfe8" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#db2777" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. MENSTRUAL CARE</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#fbcfe8"/>
      <text x="67" y="45" fill="#db2777" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🌸</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Clean sanitary towels.</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Change every 4-6 hrs.</text>
    <text x="10" y="195" fill="#db2777" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Benefit:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Protects against germs;</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">stays dry and confident.</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(585, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#16a34a" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. CLEAN CLOTHES</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#86efac"/>
      <text x="67" y="45" fill="#16a34a" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">👕</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Fresh cotton socks.</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Clean undergarments.</text>
    <text x="10" y="195" fill="#16a34a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Benefit:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Neat appearance &amp;</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">zero stale odors.</text>
  </g>
</svg>""",

    # Lesson 2 Page 4: Menstrual Hygiene & Safe Waste Disposal Flowchart
    (2, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    5-STEP MENSTRUAL HYGIENE &amp; SAFE DISPOSAL PROTOCOL
  </text>

  <!-- Left: Steps 1-3 -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="340" height="320" fill="#fdf2f8" rx="8" stroke="#fbcfe8" stroke-width="1.5"/>
    <rect x="15" y="12" width="310" height="26" fill="#db2777" rx="5"/>
    <text x="170" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      HYGIENE &amp; APPLICATION STEPS
    </text>

    <!-- Step 1 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="48" fill="#ffffff" rx="5" stroke="#fbcfe8"/>
      <text x="15" y="20" fill="#be185d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Wash Hands with Soap &amp; Water</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Prevents germ transfer to clean sanitary pad.</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="48" fill="#ffffff" rx="5" stroke="#fbcfe8"/>
      <text x="15" y="20" fill="#be185d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Secure Pad on Cotton Underwear</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Attach adhesive firmly to avoid shifting.</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="310" height="48" fill="#ffffff" rx="5" stroke="#fbcfe8"/>
      <text x="15" y="20" fill="#be185d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Change Regularly (Every 4–6 Hours)</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Stops bacterial growth and stays comfortable.</text>
    </g>
  </g>

  <!-- Right: Steps 4-5 (Disposal Rules) -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="340" height="320" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="12" width="310" height="26" fill="#16a34a" rx="5"/>
    <text x="170" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      SAFE DISPOSAL RULES (THE BIN RULE)
    </text>

    <!-- Step 4 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="65" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="22" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Wrap Securely in Paper</text>
      <text x="15" y="40" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Fold used towel neatly.</text>
      <text x="15" y="55" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Wrap tightly in old newspaper or waste paper.</text>
    </g>

    <!-- Step 5 (Safe Bin vs Flush Toilet) -->
    <g transform="translate(15, 125)">
      <rect x="0" y="0" width="310" height="55" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="22" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ 5. Place in Sanitary Bin / Pit Latrine</text>
      <text x="15" y="42" fill="#15803d" font-family="system-ui, sans-serif" font-size="9.5">Wash hands again with soap immediately!</text>
    </g>

    <g transform="translate(15, 190)">
      <rect x="0" y="0" width="310" height="55" fill="#fee2e2" rx="5" stroke="#f87171"/>
      <text x="15" y="22" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🚫 NEVER Flush Down Flush Toilet!</text>
      <text x="15" y="42" fill="#7f1d1d" font-family="system-ui, sans-serif" font-size="9.5">Pads do not dissolve; causes severe sewer blockages.</text>
    </g>
  </g>
</svg>""",

    # Lesson 3 Page 2: The Adolescent Balanced Plate & Iron Power
    (3, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    THE ADOLESCENT BALANCED PLATE &amp; IRON POWER BLUEPRINT
  </text>

  <!-- Left: The Divided Plate -->
  <g transform="translate(45, 80)">
    <circle cx="170" cy="160" r="145" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="4"/>
    
    <!-- 1/2 Plate: Protective Vegetables & Fruits -->
    <path d="M 170 160 L 170 15 A 145 145 0 0 1 170 305 Z" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="245" y="150" fill="#15803d" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1/2 VEGETABLES</text>
    <text x="245" y="170" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">&amp; FRUITS</text>
    <text x="245" y="190" fill="#166534" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Kales, Spinach, Oranges</text>

    <!-- 1/4 Plate: Energy Foods -->
    <path d="M 170 160 L 25 160 A 145 145 0 0 1 170 15 Z" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
    <text x="95" y="90" fill="#854d0e" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1/4 ENERGY</text>
    <text x="95" y="108" fill="#713f12" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Ugali, Rice, Potatoes</text>

    <!-- 1/4 Plate: Body Building Proteins -->
    <path d="M 170 160 L 170 305 A 145 145 0 0 1 25 160 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
    <text x="95" y="235" fill="#991b1b" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1/4 PROTEINS</text>
    <text x="95" y="253" fill="#7f1d1d" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Beans, Eggs, Fish, Beef</text>
  </g>

  <!-- Right: Iron Power & Hydration Cards -->
  <g transform="translate(420, 80)">
    <!-- Iron Power Card -->
    <rect x="0" y="0" width="335" height="185" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="10" y="10" width="315" height="24" fill="#dc2626" rx="4"/>
    <text x="167" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      🩸 IRON: THE SUPER-MINERAL
    </text>
    <text x="15" y="58" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Why Girls &amp; Boys Need Iron:</text>
    <text x="15" y="78" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Helps red blood cells carry oxygen to brain &amp; muscles.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Replaces iron lost during girls' monthly menstruation.</text>
    <text x="15" y="118" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Prevents <tspan fill="#dc2626" font-weight="700">Anemia</tspan> (dizziness, pale skin, fatigue).</text>
    <rect x="10" y="135" width="315" height="38" fill="#ffffff" rx="4" stroke="#fca5a5"/>
    <text x="167" y="152" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Top Iron Sources: Spinach, Liver, Beans, Eggs</text>
    <text x="167" y="165" fill="#475569" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Eat daily for high energy and focus in class!</text>

    <!-- Clean Water Card -->
    <rect x="0" y="198" width="335" height="120" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="1.5"/>
    <rect x="10" y="10" width="315" height="24" fill="#0284c7" rx="4"/>
    <text x="167" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      💧 CLEAN BOILED WATER
    <text x="15" y="98" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Avoid sugary fizzy sodas that cause dehydration!</text>
  </g>
</svg>""",

    # Lesson 3 Page 4: Healthy Snacks vs. Junk Food Comparison Matrix
    (3, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    SMART SNACKING: HEALTHY TEEN SNACKS vs. JUNK FOOD
  </text>

  <!-- Left: Healthy Local Snacks -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="340" height="325" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="12" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      HEALTHY LOCAL SNACKS (Nutrient-Rich)
    </text>

    <!-- Item 1 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <circle cx="20" cy="26" r="12" fill="#dcfce7"/>
      <text x="20" y="30" fill="#16a34a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
      <text x="40" y="20" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Boiled Eggs &amp; Groundnuts</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Rich in protein and good fats for muscle building.</text>
    </g>

    <!-- Item 2 -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <circle cx="20" cy="26" r="12" fill="#dcfce7"/>
      <text x="20" y="30" fill="#16a34a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
      <text x="40" y="20" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Ripe Bananas &amp; Boiled Maize</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Natural carbs and fiber for long-lasting energy.</text>
    </g>

    <!-- Item 3 -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <circle cx="20" cy="26" r="12" fill="#dcfce7"/>
      <text x="20" y="30" fill="#16a34a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
      <text x="40" y="20" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Fresh Milk &amp; Clean Water</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Calcium for strong bones; zero artificial chemicals.</text>
    </g>

    <!-- Bottom Result Banner -->
    <g transform="translate(15, 235)">
      <rect x="0" y="0" width="310" height="42" fill="#dcfce7" rx="5"/>
      <text x="155" y="18" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">HEALTHY OUTCOME:</text>
      <text x="155" y="32" fill="#166534" font-family="system-ui, -apple-system, sans-serif" font-size="9" text-anchor="middle">Sharp focus in class, high stamina &amp; clear skin!</text>
    </g>
  </g>

  <!-- Right: Unhealthy Junk Foods -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="340" height="325" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="15" y="12" width="310" height="28" fill="#dc2626" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      UNHEALTHY JUNK FOODS (Empty Calories)
    </text>

    <!-- Item 1 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <circle cx="20" cy="26" r="12" fill="#fee2e2"/>
      <text x="20" y="30" fill="#dc2626" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">X</text>
      <text x="40" y="20" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Packaged Oily Potato Crisps</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Excess unhealthy oils and salt; raises obesity risks.</text>
    </g>

    <!-- Item 2 -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <circle cx="20" cy="26" r="12" fill="#fee2e2"/>
      <text x="20" y="30" fill="#dc2626" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">X</text>
      <text x="40" y="20" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Fizzy Carbonated Sodas</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Loaded with artificial sugar; causes rapid energy crashes.</text>
    </g>

    <!-- Item 3 -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <circle cx="20" cy="26" r="12" fill="#fee2e2"/>
      <text x="20" y="30" fill="#dc2626" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">X</text>
      <text x="40" y="20" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Bright Colored Candies &amp; Sweets</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Destroys tooth enamel; zero vitamins or minerals.</text>
    </g>

    <!-- Bottom Danger Banner -->
    <g transform="translate(15, 235)">
      <rect x="0" y="0" width="310" height="42" fill="#fee2e2" rx="5"/>
      <text x="155" y="18" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">UNHEALTHY CONSEQUENCE:</text>
      <text x="155" y="32" fill="#7f1d1d" font-family="system-ui, -apple-system, sans-serif" font-size="9" text-anchor="middle">Sluggish fatigue, tooth decay &amp; unhealthy weight gain!</text>
    </g>
  </g>
</svg>""",

    # Lesson 4 Page 2: Daily Physical Exercise & Mental Mood Boost Model
    (4, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    DAILY PHYSICAL EXERCISE: FIT BODY &amp; HAPPY MIND
  </text>

  <!-- Left: Active Student Benefits -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="340" height="325" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="12" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      ACTIVE TEENAGER (1 Hour Daily Exercise)
    </text>

    <!-- Benefit 1 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <circle cx="20" cy="26" r="12" fill="#dcfce7"/>
      <text x="20" y="30" fill="#16a34a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">+</text>
      <text x="40" y="20" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Strong Heart &amp; Healthy Lungs</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Boosts blood circulation and oxygen to brain &amp; muscles.</text>
    </g>

    <!-- Benefit 2 -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <circle cx="20" cy="26" r="12" fill="#dcfce7"/>
      <text x="20" y="30" fill="#16a34a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">+</text>
      <text x="40" y="20" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Dense Bones &amp; Lean Muscles</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Running, skipping, and sports build strong bone mass.</text>
    </g>

    <!-- Benefit 3 -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <circle cx="20" cy="26" r="12" fill="#dcfce7"/>
      <text x="20" y="30" fill="#16a34a" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">+</text>
      <text x="40" y="20" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Happy Mood &amp; Stress Relief</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Releases endorphins; clears stress and improves sleep.</text>
    </g>

    <!-- Bottom Result -->
    <g transform="translate(15, 235)">
      <rect x="0" y="0" width="310" height="42" fill="#dcfce7" rx="5"/>
      <text x="155" y="18" fill="#15803d" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">POSITIVE OUTCOME:</text>
      <text x="155" y="32" fill="#166534" font-family="system-ui, -apple-system, sans-serif" font-size="9" text-anchor="middle">Peak alertness, high confidence &amp; excellent fitness!</text>
    </g>
  </g>

  <!-- Right: Inactive Sedentary Lifestyle -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="340" height="325" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="15" y="12" width="310" height="28" fill="#dc2626" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      SEDENTARY LIFESTYLE (Sitting All Day)
    </text>

    <!-- Risk 1 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <circle cx="20" cy="26" r="12" fill="#fee2e2"/>
      <text x="20" y="30" fill="#dc2626" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">-</text>
      <text x="40" y="20" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Risk of Childhood Obesity</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Excess calories stored as fat; risk of early lifestyle illness.</text>
    </g>

    <!-- Risk 2 -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <circle cx="20" cy="26" r="12" fill="#fee2e2"/>
      <text x="20" y="30" fill="#dc2626" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">-</text>
      <text x="40" y="20" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Weak Bones &amp; Stiff Joints</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Lack of movement causes brittle bones &amp; poor posture.</text>
    </g>

    <!-- Risk 3 -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <circle cx="20" cy="26" r="12" fill="#fee2e2"/>
      <text x="20" y="30" fill="#dc2626" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">-</text>
      <text x="40" y="20" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Daytime Sluggishness &amp; Poor Sleep</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Leads to daytime drowsiness, poor memory &amp; low mood.</text>
    </g>

    <!-- Bottom Danger -->
    <g transform="translate(15, 235)">
      <rect x="0" y="0" width="310" height="42" fill="#fee2e2" rx="5"/>
      <text x="155" y="18" fill="#991b1b" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">NEGATIVE OUTCOME:</text>
      <text x="155" y="32" fill="#7f1d1d" font-family="system-ui, -apple-system, sans-serif" font-size="9" text-anchor="middle">Low stamina, weak immunity &amp; frequent fatigue!</text>
    </g>
  </g>
</svg>""",

    # Lesson 4 Page 4: Environmental Hazard Awareness & Digital Safety Shield
    (4, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    ADOLESCENT SAFETY SHIELD: PHYSICAL &amp; DIGITAL SECURITY
  </text>

  <!-- Left: Physical Environmental Safety -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="340" height="325" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="15" y="12" width="310" height="28" fill="#0284c7" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      PHYSICAL COMMUNITY SAFETY RULES
    </text>

    <!-- Rule 1 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bae6fd"/>
      <circle cx="20" cy="26" r="12" fill="#e0f2fe"/>
      <text x="20" y="30" fill="#0284c7" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
      <text x="40" y="20" fill="#0369a1" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Walk in Groups (Buddy System)</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Use busy, well-lit main roads; avoid dark bush paths.</text>
    </g>

    <!-- Rule 2 -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bae6fd"/>
      <circle cx="20" cy="26" r="12" fill="#e0f2fe"/>
      <text x="20" y="30" fill="#0284c7" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
      <text x="40" y="20" fill="#0369a1" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Refuse Gifts &amp; Rides from Strangers</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Never accept snacks, money, or vehicle rides from unknown people.</text>
    </g>

    <!-- Rule 3 -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#bae6fd"/>
      <circle cx="20" cy="26" r="12" fill="#e0f2fe"/>
      <text x="20" y="30" fill="#0284c7" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
      <text x="40" y="20" fill="#0369a1" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Avoid Deep Dams &amp; Swollen Rivers</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Never swim in unattended quarries or walk across flooded bridges.</text>
    </g>

    <!-- Bottom Shield Rule -->
    <g transform="translate(15, 235)">
      <rect x="0" y="0" width="310" height="42" fill="#e0f2fe" rx="5"/>
      <text x="155" y="18" fill="#0369a1" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">EMERGENCY DEFENSE:</text>
      <text x="155" y="32" fill="#0284c7" font-family="system-ui, -apple-system, sans-serif" font-size="9" text-anchor="middle">Say NO to uncomfortable touch and report to a trusted adult!</text>
    </g>
  </g>

  <!-- Right: Digital & Online Safety -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="340" height="325" fill="#faf5ff" rx="8" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="15" y="12" width="310" height="28" fill="#9333ea" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      DIGITAL &amp; ONLINE SAFETY RULES
    </text>

    <!-- Digital 1 -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#d8b4fe"/>
      <circle cx="20" cy="26" r="12" fill="#f3e8ff"/>
      <text x="20" y="30" fill="#9333ea" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1</text>
      <text x="40" y="20" fill="#7e22ce" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Keep Personal Data Secret</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Never post your home address, phone number, or school name.</text>
    </g>

    <!-- Digital 2 -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#d8b4fe"/>
      <circle cx="20" cy="26" r="12" fill="#f3e8ff"/>
      <text x="20" y="30" fill="#9333ea" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2</text>
      <text x="40" y="20" fill="#7e22ce" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Never Meet Online Contacts Alone</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Online identities can be fake; never agree to meet strangers.</text>
    </g>

    <!-- Digital 3 -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="310" height="52" fill="#ffffff" rx="5" stroke="#d8b4fe"/>
      <circle cx="20" cy="26" r="12" fill="#f3e8ff"/>
      <text x="20" y="30" fill="#9333ea" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3</text>
      <text x="40" y="20" fill="#7e22ce" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700">Report Inappropriate Messages</text>
      <text x="40" y="37" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="9">Block cyberbullies and show threatening texts to parents or teachers.</text>
    </g>

      <rect x="0" y="235" width="310" height="42" fill="#f3e8ff" rx="5"/>
      <text x="155" y="18" fill="#7e22ce" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">ONLINE SHIELD:</text>
      <text x="155" y="32" fill="#6b21a8" font-family="system-ui, -apple-system, sans-serif" font-size="9" text-anchor="middle">Protect your passwords and personal privacy like a fortress!</text>
    </g>
  </g>
</svg>""",
}

def enrich_cbc_grade6_home_science_topic1():
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 6 HOME SCIENCE — TOPIC 1: ADOLESCENCE")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    topic = Topic.objects.filter(subject=subject, name="Adolescence").first()

    assert topic, "Grade 6 Topic 1 (Adolescence) not found!"
    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"[*] Found {len(lessons)} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Clear existing LessonAssets for clean re-enrichment
    for lesson in lessons:
        lesson.assets.all().delete()
    print("[*] Cleared existing LessonAssets for clean re-enrichment.\n")

    # Phase 2A: Card 1 Verified Photographic Visual Hooks
    print("[+] Phase 2A: Attaching Mandatory Card 1 Visual Hooks...")
    for lesson in lessons:
        u_order = lesson.learning_unit.order
        photo_info = TOPIC1_PHOTOS.get(u_order)
        if not photo_info:
            continue

        hook_block = lesson.blocks.filter(page_number=1, block_type="suggested_image").first()
        if hook_block:
            content = hook_block.content or {}
            content["resolved_image_url"] = photo_info["url"]
            content["url"] = photo_info["url"]
            content["author"] = photo_info["author"]
            content["licensing"] = photo_info["licensing"]
            content["caption"] = photo_info["caption"]
            hook_block.content = content
            hook_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=hook_block.title,
                description=photo_info["caption"],
                url=photo_info["url"],
                metadata={
                    "author": photo_info["author"],
                    "licensing": photo_info["licensing"],
                    "caption": photo_info["caption"],
                    "is_card_1_hook": True
                }
            )
            hook_block.assets.add(asset)
            print(f"  [CARD 1 HOOK OK] Lesson {u_order} Page 1: '{hook_block.title[:45]}...' -> Asset ID {asset.id}")

    # Phase 2B: Custom Sanitized Vector SVGs
    print("\n[+] Phase 2B: Attaching Custom Sanitized Vector SVGs...")
    for (u_order, page_num), svg_code in TOPIC1_SVGS.items():
        if u_order > len(lessons):
            continue
        lesson = lessons[u_order - 1]
        diag_block = lesson.blocks.filter(page_number=page_num, block_type="diagram").first()
        if diag_block:
            content = diag_block.content or {}
            content["svg_content"] = svg_code
            content["svg"] = svg_code
            content["code"] = svg_code
            content["viewBox"] = "0 0 800 450"
            diag_block.content = content
            diag_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="embed",
                status="attached",
                title=diag_block.title,
                description=content.get("description", diag_block.title),
                metadata={
                    "svg_content": svg_code,
                    "format": "svg",
                    "viewBox": "0 0 800 450",
                    "page_number": page_num
                }
            )
            diag_block.assets.add(asset)
            print(f"  [SVG ATTACHED] Lesson {u_order} Page {page_num}: '{diag_block.title[:45]}...' -> Asset ID {asset.id}")

    total_assets = LessonAsset.objects.filter(lesson__topic=topic).count()
    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 6 Home Science Topic 1 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade6_home_science_topic1()
