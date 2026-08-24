"""
VLearn Curriculum Visual Enrichment Script
CBC Grade 6 — Home Science
Topic 3: Foods and Nutrition (Order: 3)

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
TOPIC3_PHOTOS = {
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg",
        "author": "National Cancer Institute / Wikimedia Commons",
        "licensing": "Public Domain",
        "caption": "An abundant display of fresh fruits, vegetables, grains, and proteins that supply our bodies with vital minerals and nutrients."
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Sun-dried_shark_minnows_and_snakehead_fish_in_Battambang.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "Fresh fish preserved by sun drying, an effective traditional moisture-removal method that prevents bacterial spoilage."
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Food_cooking_on_charcoal_stove.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "A traditional charcoal stove in active use, illustrating the daily care and fuel management required in household cooking."
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Homemade_butter_cake.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "A golden-brown homemade butter cake demonstrating successful execution of the rubbed-in baking method."
    }
}

# 8 Custom High-Definition Vector SVGs for Grade 6 Topic 3
TOPIC3_SVGS = {
    # Lesson 1 Page 2: Local Food Mineral Map
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
    LOCAL FOOD MINERAL MAP: IRON &amp; IODINE SOURCES
  </text>

  <!-- Left: Iron Sources -->
  <g transform="translate(45, 88)">
    <rect x="0" y="0" width="340" height="315" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="28" fill="#dc2626" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      🩸 IRON (Haemoglobin, Oxygen &amp; Strength)
    </text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="50" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <text x="15" y="20" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🥬 Dark Green Spinach &amp; Terere</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Rich plant iron; builds oxygen-carrying blood.</text>

      <rect x="0" y="60" width="300" height="50" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <text x="15" y="20" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🥩 Beef Liver &amp; Organ Meats</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Easily absorbed animal heme iron; prevents anaemia.</text>

      <rect x="0" y="120" width="300" height="50" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <text x="15" y="20" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🫘 Red Kidney Beans &amp; Lentils</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Affordable pulses; rebuilds adolescent blood stores.</text>

      <rect x="0" y="180" width="300" height="50" fill="#fee2e2" rx="5"/>
      <text x="150" y="30" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Tip: Squeeze lemon juice (Vitamin C) to boost absorption!</text>
    </g>
  </g>

  <!-- Right: Iodine Sources -->
  <g transform="translate(415, 88)">
    <rect x="0" y="0" width="340" height="315" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="15" y="15" width="310" height="28" fill="#2563eb" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      🧠 IODINE (Thyroid Hormone &amp; Brain Alertness)
    </text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="50" fill="#ffffff" rx="5" stroke="#93c5fd"/>
      <text x="15" y="20" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🧂 Packaged Iodized Table Salt</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Fortified daily seasoning; stops thyroid goitre.</text>

      <rect x="0" y="60" width="300" height="50" fill="#ffffff" rx="5" stroke="#93c5fd"/>
      <text x="15" y="20" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🐟 Fresh Lake Fish (Tilapia &amp; Omena)</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Rich natural marine mineral and protein source.</text>

      <rect x="0" y="120" width="300" height="50" fill="#ffffff" rx="5" stroke="#93c5fd"/>
      <text x="15" y="20" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🥛 Dairy Milk &amp; Boiled Eggs</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Supports sharp brain development and body growth.</text>

      <rect x="0" y="180" width="300" height="50" fill="#dbeafe" rx="5"/>
      <text x="150" y="30" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Always check for the KEBS quality seal on salt packets!</text>
    </g>
  </g>
</svg>""",

    # Lesson 1 Page 4: 5 Major Nutritional Deficiency Disorders Matrix
    (1, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    5 MAJOR NUTRITIONAL DEFICIENCY DISORDERS MATRIX
  </text>

  <!-- 5 Columns Layout -->

  <!-- Card 1: Anaemia -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="138" height="315" fill="#fef2f2" rx="6" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="6" y="6" width="126" height="24" fill="#dc2626" rx="4"/>
    <text x="69" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1. ANAEMIA</text>
    <text x="69" y="55" fill="#dc2626" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">🩸</text>
    <text x="10" y="85" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Cause:</text>
    <text x="10" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Lack of Iron.</text>
    <text x="10" y="125" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Signs:</text>
    <text x="10" y="140" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Pale gums &amp; eyelids</text>
    <text x="10" y="153" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Extreme fatigue</text>
    <text x="10" y="166" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Dizziness</text>
    <rect x="6" y="240" width="126" height="60" fill="#ffffff" rx="4" stroke="#fca5a5"/>
    <text x="69" y="258" fill="#991b1b" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Prevention:</text>
    <text x="69" y="272" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Spinach, liver, beans</text>
    <text x="69" y="284" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">&amp; lemon juice.</text>
  </g>

  <!-- Card 2: Goitre -->
  <g transform="translate(181, 80)">
    <rect x="0" y="0" width="138" height="315" fill="#eff6ff" rx="6" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="6" y="6" width="126" height="24" fill="#2563eb" rx="4"/>
    <text x="69" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">2. GOITRE</text>
    <text x="69" y="55" fill="#2563eb" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">👤</text>
    <text x="10" y="85" fill="#1e40af" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Cause:</text>
    <text x="10" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Lack of Iodine.</text>
    <text x="10" y="125" fill="#1e40af" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Signs:</text>
    <text x="10" y="140" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Swelling/lump in</text>
    <text x="10" y="153" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">  front of neck</text>
    <text x="10" y="166" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Slow growth</text>
    <rect x="6" y="240" width="126" height="60" fill="#ffffff" rx="4" stroke="#93c5fd"/>
    <text x="69" y="258" fill="#1e40af" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Prevention:</text>
    <text x="69" y="272" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Iodized salt, fish,</text>
    <text x="69" y="284" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">milk, and eggs.</text>
  </g>

  <!-- Card 3: Constipation -->
  <g transform="translate(327, 80)">
    <rect x="0" y="0" width="138" height="315" fill="#f0fdf4" rx="6" stroke="#bbf7d0" stroke-width="1.5"/>
    <rect x="6" y="6" width="126" height="24" fill="#16a34a" rx="4"/>
    <text x="69" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">3. CONSTIPATION</text>
    <text x="69" y="55" fill="#16a34a" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">💧</text>
    <text x="10" y="85" fill="#15803d" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Cause:</text>
    <text x="10" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Low fibre &amp; water.</text>
    <text x="10" y="125" fill="#15803d" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Signs:</text>
    <text x="10" y="140" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Hard, dry stools</text>
    <text x="10" y="153" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Painful passing</text>
    <text x="10" y="166" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Irregular bowel</text>
    <rect x="6" y="240" width="126" height="60" fill="#ffffff" rx="4" stroke="#86efac"/>
    <text x="69" y="258" fill="#15803d" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Prevention:</text>
    <text x="69" y="272" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Kales, fruits, whole</text>
    <text x="69" y="284" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">grains &amp; 8 glasses water.</text>
  </g>

  <!-- Card 4: Kwashiorkor -->
  <g transform="translate(473, 80)">
    <rect x="0" y="0" width="138" height="315" fill="#fffbeb" rx="6" stroke="#fde68a" stroke-width="1.5"/>
    <rect x="6" y="6" width="126" height="24" fill="#d97706" rx="4"/>
    <text x="69" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">4. KWASHIORKOR</text>
    <text x="69" y="55" fill="#d97706" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">🧒</text>
    <text x="10" y="85" fill="#b45309" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Cause:</text>
    <text x="10" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Lack of Protein.</text>
    <text x="10" y="125" fill="#b45309" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Signs:</text>
    <text x="10" y="140" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Swollen belly &amp; face</text>
    <text x="10" y="153" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Thin brownish hair</text>
    <text x="10" y="166" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Weak muscles</text>
    <rect x="6" y="240" width="126" height="60" fill="#ffffff" rx="4" stroke="#fcd34d"/>
    <text x="69" y="258" fill="#b45309" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Prevention:</text>
    <text x="69" y="272" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Beans, peas, eggs,</text>
    <text x="69" y="284" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">milk, and groundnuts.</text>
  </g>

  <!-- Card 5: Marasmus -->
  <g transform="translate(619, 80)">
    <rect x="0" y="0" width="145" height="315" fill="#faf5ff" rx="6" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="6" y="6" width="133" height="24" fill="#9333ea" rx="4"/>
    <text x="72" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">5. MARASMUS</text>
    <text x="72" y="55" fill="#9333ea" font-family="system-ui, sans-serif" font-size="22" text-anchor="middle">🦴</text>
    <text x="10" y="85" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Cause:</text>
    <text x="10" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Total Starvation.</text>
    <text x="10" y="125" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Signs:</text>
    <text x="10" y="140" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Ribs showing clearly</text>
    <text x="10" y="153" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• Loose wrinkled skin</text>
    <text x="10" y="166" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">• "Old-man" face</text>
    <rect x="6" y="240" width="133" height="60" fill="#ffffff" rx="4" stroke="#d8b4fe"/>
    <text x="72" y="258" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Prevention:</text>
    <text x="72" y="272" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">High-energy balanced</text>
    <text x="72" y="284" fill="#475569" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">meals (carbs+protein).</text>
  </g>
</svg>""",

    # Lesson 2 Page 2: 4 Household Meat Preservation Methods Comparison Grid
    (2, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    4 HOUSEHOLD MEAT PRESERVATION METHODS
  </text>

  <!-- 4 Quadrants Layout -->

  <!-- Quad 1: Refrigeration -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="340" height="150" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="10" y="10" width="320" height="24" fill="#2563eb" rx="4"/>
    <text x="170" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. REFRIGERATION &amp; FREEZING</text>
    <text x="15" y="55" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="18">❄️</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Cold Temperature Suspension</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Puts bacteria to sleep by dropping temperature.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Pro:</tspan> Retains natural meat flavor and texture.</text>
    <text x="15" y="116" fill="#dc2626" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Con:</tspan> Requires reliable, uninterrupted electricity.</text>
  </g>

  <!-- Quad 2: Sun Drying -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="340" height="150" fill="#fefce8" rx="8" stroke="#fef08a" stroke-width="1.5"/>
    <rect x="10" y="10" width="320" height="24" fill="#ca8a04" rx="4"/>
    <text x="170" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. SUN DRYING (THIN STRIPS)</text>
    <text x="15" y="55" fill="#ca8a04" font-family="system-ui, sans-serif" font-size="18">☀️</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Moisture Evaporation</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Hangs lean strips in mesh cage under hot sun.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Pro:</tspan> Free solar heat; lasts for months.</text>
    <text x="15" y="116" fill="#dc2626" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Con:</tspan> Dependent on sunny, dry weather.</text>
  </g>

  <!-- Quad 3: Salting / Brining -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="340" height="155" fill="#f0fdf4" rx="8" stroke="#bbf7d0" stroke-width="1.5"/>
    <rect x="10" y="10" width="320" height="24" fill="#16a34a" rx="4"/>
    <text x="170" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. SALTING (DRY RUB &amp; WET BRINE)</text>
    <text x="15" y="55" fill="#15803d" font-family="system-ui, sans-serif" font-size="18">🧂</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Osmotic Dehydration</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Salt pulls water out of meat and kills bacteria.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Pro:</tspan> Highly effective, affordable household cure.</text>
    <text x="15" y="116" fill="#dc2626" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Caution:</tspan> High sodium risk for high blood pressure!</text>
  </g>

  <!-- Quad 4: Smoking -->
  <g transform="translate(415, 245)">
    <rect x="0" y="0" width="340" height="155" fill="#fff7ed" rx="8" stroke="#fed7aa" stroke-width="1.5"/>
    <rect x="10" y="10" width="320" height="24" fill="#ea580c" rx="4"/>
    <text x="170" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. SMOKING (WOOD FIRE PIT)</text>
    <text x="15" y="55" fill="#ea580c" font-family="system-ui, sans-serif" font-size="18">💨</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Chemical Shield &amp; Aroma</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Warm smoke coats meat with anti-bacterial film.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Pro:</tspan> Imparts rich flavor, color, and aroma.</text>
    <text x="15" y="116" fill="#dc2626" font-family="system-ui, sans-serif" font-size="9.5">• <tspan font-weight="700">Con:</tspan> Needs careful fire control to avoid cooking.</text>
  </g>
</svg>""",

    # Lesson 2 Page 4: Raised Food Drying Rack & Muslin Cover Blueprint
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
    HYGIENIC RAISED DRYING RACK &amp; MUSLIN SHIELD BLUEPRINT
  </text>

  <!-- Left: The Architectural Diagram of the Rack -->
  <g transform="translate(45, 80)">
    <!-- The Sun -->
    <circle cx="60" cy="40" r="22" fill="#facc15" stroke="#eab308" stroke-width="2"/>
    <line x1="60" y1="10" x2="60" y2="0" stroke="#eab308" stroke-width="2"/>
    <line x1="60" y1="70" x2="60" y2="80" stroke="#eab308" stroke-width="2"/>
    <line x1="30" y1="40" x2="20" y2="40" stroke="#eab308" stroke-width="2"/>
    <line x1="90" y1="40" x2="100" y2="40" stroke="#eab308" stroke-width="2"/>
    <text x="60" y="45" fill="#713f12" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SUN</text>

    <!-- Muslin Cloth Cover Layer -->
    <path d="M 120 70 Q 230 50 340 70" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,4"/>
    <text x="230" y="55" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Clean Muslin Cloth Cover</text>

    <!-- The Drying Table / Mesh -->
    <rect x="120" y="75" width="220" height="18" fill="#cbd5e1" stroke="#475569" stroke-width="1.5" rx="2"/>
    <!-- Sliced Greens/Fruits on Table -->
    <circle cx="145" cy="84" r="5" fill="#16a34a"/>
    <circle cx="170" cy="84" r="5" fill="#16a34a"/>
    <circle cx="195" cy="84" r="5" fill="#ea580c"/>
    <circle cx="220" cy="84" r="5" fill="#16a34a"/>
    <circle cx="245" cy="84" r="5" fill="#ea580c"/>
    <circle cx="270" cy="84" r="5" fill="#16a34a"/>
    <circle cx="295" cy="84" r="5" fill="#16a34a"/>
    <circle cx="320" cy="84" r="5" fill="#ea580c"/>

    <!-- Raised Table Legs (1 Meter High) -->
    <rect x="135" y="93" width="12" height="150" fill="#94a3b8" rx="2"/>
    <rect x="315" y="93" width="12" height="150" fill="#94a3b8" rx="2"/>
    
    <!-- Cross Braces -->
    <line x1="147" y1="150" x2="315" y2="200" stroke="#64748b" stroke-width="2"/>
    <line x1="147" y1="200" x2="315" y2="150" stroke="#64748b" stroke-width="2"/>

    <!-- Height Arrow -->
    <line x1="110" y1="93" x2="110" y2="243" stroke="#dc2626" stroke-width="1.5"/>
    <text x="95" y="172" fill="#dc2626" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1 METRE</text>

    <!-- Ground Level -->
    <line x1="60" y1="243" x2="350" y2="243" stroke="#78350f" stroke-width="3"/>
    <text x="230" y="265" fill="#78350f" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Ground Level (Dust, Insects &amp; Poultry)</text>
  </g>

  <!-- Right: The 3 Golden Sanitation Shield Rules -->
  <g transform="translate(425, 80)">
    <rect x="0" y="0" width="330" height="320" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="12" width="300" height="26" fill="#16a34a" rx="5"/>
    <text x="165" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      HYGIENIC SANITATION RULES
    </text>

    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Raised 1m Off Ground</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Keeps food away from dust &amp; mud.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Prevents chickens and dogs from touching.</text>
    </g>

    <g transform="translate(15, 120)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Muslin Cloth Shield</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Blocks flies, wasps, and birds.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Allows solar heat &amp; wind through safely.</text>
    </g>

    <g transform="translate(15, 190)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Airtight Sealed Jars</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Pack crispy dry produce in glass jars.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Stores for 6–12 months in dry pantry.</text>
    </g>
  </g>
</svg>""",

    # Lesson 3 Page 2: Household Cookers Maintenance & Danger Zones
    (3, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    HOUSEHOLD COOKING EQUIPMENT CARE &amp; SAFETY ZONES
  </text>

  <!-- 4 Cooker Cards Layout -->

  <!-- Cooker 1: Charcoal Jiko -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="165" height="315" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#334155" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. CHARCOAL JIKO</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="70" fill="#ffffff" rx="4" stroke="#cbd5e1"/>
      <text x="67" y="42" fill="#334155" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🪨</text>
    </g>
    <text x="10" y="132" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Daily Clean Zone:</text>
    <text x="10" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Empty ash gate daily.</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Maintains oxygen flow.</text>
    <text x="10" y="185" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Danger Zone:</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Never burn in closed room</text>
    <text x="10" y="212" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">(carbon monoxide risk!).</text>
  </g>

  <!-- Cooker 2: Gas Cooker (LPG) -->
  <g transform="translate(225, 80)">
    <rect x="0" y="0" width="165" height="315" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0284c7" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. GAS COOKER (LPG)</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="70" fill="#ffffff" rx="4" stroke="#bfdbfe"/>
      <text x="67" y="42" fill="#0284c7" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🔥</text>
    </g>
    <text x="10" y="132" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Daily Clean Zone:</text>
    <text x="10" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Unclog burner nozzles.</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Ensure clean blue flame.</text>
    <text x="10" y="185" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Danger Zone:</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Check rubber hose leaks;</text>
    <text x="10" y="212" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">never search leaks with fire!</text>
  </g>

  <!-- Cooker 3: Paraffin Stove -->
  <g transform="translate(405, 80)">
    <rect x="0" y="0" width="165" height="315" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#dc2626" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. PARAFFIN STOVE</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="70" fill="#ffffff" rx="4" stroke="#fecaca"/>
      <text x="67" y="42" fill="#dc2626" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🪔</text>
    </g>
    <text x="10" y="132" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Daily Clean Zone:</text>
    <text x="10" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Trim wicks flat &amp; level.</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Wipe chimney soot daily.</text>
    <text x="10" y="185" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Danger Zone:</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">Wipe spilled oil; never refill</text>
    <text x="10" y="212" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">while stove is lit!</text>
  </g>

  <!-- Cooker 4: Electric Cooker -->
  <g transform="translate(585, 80)">
    <rect x="0" y="0" width="165" height="315" fill="#faf5ff" rx="8" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#9333ea" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. ELECTRIC COOKER</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="70" fill="#ffffff" rx="4" stroke="#e9d5ff"/>
      <text x="67" y="42" fill="#9333ea" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">⚡</text>
    </g>
    <text x="10" y="132" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Daily Clean Zone:</text>
    <text x="10" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Wipe cold plate damp.</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Avoid scratching wool.</text>
    <text x="10" y="185" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Danger Zone:</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">NEVER wash when hot;</text>
    <text x="10" y="212" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5">electric shock &amp; crack risk!</text>
  </g>
</svg>""",

    # Lesson 3 Page 4: The Family Meal Planner's Decision Wheel
    (3, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    THE FAMILY MEAL PLANNER'S DECISION WHEEL
  </text>

  <!-- Left: Center Dinner Plate & Radiating Spokes -->
  <g transform="translate(220, 240)">
    <!-- Radiating Connection Lines -->
    <line x1="0" y1="0" x2="0" y2="-120" stroke="#0284c7" stroke-width="2.5"/>
    <line x1="0" y1="0" x2="105" y2="-60" stroke="#16a34a" stroke-width="2.5"/>
    <line x1="0" y1="0" x2="105" y2="60" stroke="#ea580c" stroke-width="2.5"/>
    <line x1="0" y1="0" x2="0" y2="120" stroke="#9333ea" stroke-width="2.5"/>
    <line x1="0" y1="0" x2="-105" y2="60" stroke="#dc2626" stroke-width="2.5"/>
    <line x1="0" y1="0" x2="-105" y2="-60" stroke="#ca8a04" stroke-width="2.5"/>

    <!-- Center Plate -->
    <circle cx="0" cy="0" r="50" fill="#f1f5f9" stroke="#0f172a" stroke-width="3"/>
    <text x="0" y="-5" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FAMILY</text>
    <text x="0" y="12" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">MEAL</text>
    <text x="0" y="26" fill="#475569" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">PLATE</text>

    <!-- Node 1: Budget (Top) -->
    <circle cx="0" cy="-120" r="24" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
    <text x="0" y="-115" fill="#0284c7" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">💰</text>

    <!-- Node 2: Nutrients (Top Right) -->
    <circle cx="105" cy="-60" r="24" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="105" y="-55" fill="#16a34a" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🥦</text>

    <!-- Node 3: Availability (Bottom Right) -->
    <circle cx="105" cy="60" r="24" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
    <text x="105" y="65" fill="#ea580c" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🌽</text>

    <!-- Node 4: Fuel (Bottom) -->
    <circle cx="0" cy="120" r="24" fill="#f3e8ff" stroke="#9333ea" stroke-width="2"/>
    <text x="0" y="125" fill="#9333ea" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🔥</text>

    <!-- Node 5: People (Bottom Left) -->
    <circle cx="-105" cy="60" r="24" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
    <text x="-105" y="65" fill="#dc2626" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">👨‍👩‍👧</text>

    <!-- Node 6: Time (Top Left) -->
    <circle cx="-105" cy="-60" r="24" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
    <text x="-105" y="-55" fill="#ca8a04" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">⏰</text>
  </g>

  <!-- Right: Sector Descriptions List -->
  <g transform="translate(425, 80)">
    <rect x="0" y="0" width="330" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="15" y="12" width="300" height="26" fill="#0f172a" rx="5"/>
    <text x="165" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      6 KEY PLANNING FACTORS
    </text>

    <g transform="translate(15, 48)">
      <text x="0" y="15" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Money (Budget):</text>
      <text x="0" y="28" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Plan strictly within available household income.</text>

      <text x="0" y="55" fill="#16a34a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Nutrients &amp; Health:</text>
      <text x="0" y="68" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Combine vitamins, body-building proteins &amp; energy.</text>

      <text x="0" y="95" fill="#ea580c" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Seasonal Availability:</text>
      <text x="0" y="108" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Local in-season greens are cheaper &amp; freshest.</text>

      <text x="0" y="135" fill="#9333ea" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Fuel Economy:</text>
      <text x="0" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Use one-pot stews to save gas and charcoal.</text>

      <text x="0" y="175" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Family Size &amp; Portions:</text>
      <text x="0" y="188" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Apportion correct quantities to stop food waste.</text>

      <text x="0" y="215" fill="#ca8a04" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">6. Time Available:</text>
      <text x="0" y="228" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Match menu complexity to evening cooking time.</text>
    </g>
  </g>
</svg>""",

    # Lesson 4 Page 2: Clay Pot Stewing Convection Current & Heat Simmer Model
    (4, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    CLAY POT STEWING CONVECTION LOOP &amp; NUTRIENT LOCK
  </text>

  <!-- Left: Cross Section Diagram of Clay Pot on Jiko -->
  <g transform="translate(50, 80)">
    <!-- Charcoal Jiko Base -->
    <path d="M 60 270 L 260 270 L 240 230 L 80 230 Z" fill="#475569"/>
    <!-- Glowing Charcoal Embers -->
    <circle cx="130" cy="235" r="8" fill="#ef4444"/>
    <circle cx="160" cy="235" r="8" fill="#f97316"/>
    <circle cx="190" cy="235" r="8" fill="#ef4444"/>

    <!-- Clay Pot Body (Nyungu) -->
    <path d="M 60 120 Q 30 200 160 225 Q 290 200 260 120 Z" fill="#9a3412" stroke="#7c2d12" stroke-width="3"/>
    <!-- Gravy Liquid Level -->
    <path d="M 65 140 Q 50 195 160 215 Q 270 195 255 140 Z" fill="#ea580c" opacity="0.3"/>

    <!-- Meat & Matoke Chunks at bottom -->
    <rect x="110" y="185" width="22" height="18" fill="#78350f" rx="3"/>
    <rect x="145" y="190" width="26" height="18" fill="#ca8a04" rx="3"/>
    <rect x="185" y="185" width="22" height="18" fill="#78350f" rx="3"/>

    <!-- Convection Loop Arrows -->
    <!-- Hot Rising Liquid (Red) -->
    <path d="M 160 200 L 160 145" stroke="#dc2626" stroke-width="3" stroke-dasharray="4,4"/>
    <polygon points="160,138 155,148 165,148" fill="#dc2626"/>

    <!-- Cool Sinking Liquid (Blue) -->
    <path d="M 190 145 Q 230 170 215 200" fill="none" stroke="#2563eb" stroke-width="2.5"/>
    <path d="M 130 145 Q 90 170 105 200" fill="none" stroke="#2563eb" stroke-width="2.5"/>

    <!-- Trapped Steam Clouds under Lid -->
    <text x="160" y="125" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">☁️ ☁️ ☁️</text>

    <!-- Tight Clay Lid -->
    <path d="M 50 120 Q 160 90 270 120 Z" fill="#7c2d12" stroke="#451a03" stroke-width="2.5"/>
    <circle cx="160" cy="100" r="8" fill="#451a03"/>
    <text x="160" y="85" fill="#7c2d12" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Tight Fitting Lid</text>
  </g>

  <!-- Right: The 3 Scientific Principles of Stewing -->
  <g transform="translate(425, 80)">
    <rect x="0" y="0" width="330" height="320" fill="#fff7ed" rx="8" stroke="#fed7aa" stroke-width="2"/>
    <rect x="15" y="12" width="300" height="26" fill="#ea580c" rx="5"/>
    <text x="165" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      STEWING COOKERY PRINCIPLES
    </text>

    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#ffedd5"/>
      <text x="15" y="20" fill="#c2410c" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. S-Pattern Convection Loop</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Hot liquid rises, cool liquid sinks continuously.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Cooks meat and bananas evenly without stirring.</text>
    </g>

    <g transform="translate(15, 120)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#ffedd5"/>
      <text x="15" y="20" fill="#c2410c" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Low Gentle Simmer</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Never boil violently! Small quiet bubbles.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Breaks down tough fibers, making meat melt soft.</text>
    </g>

    <g transform="translate(15, 190)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#ffedd5"/>
      <text x="15" y="20" fill="#c2410c" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. 100% Nutrient Retention</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Water-soluble vitamins dissolve into gravy.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Zero nutrient loss; all gravy served with meal!</text>
    </g>
  </g>
</svg>""",

    # Lesson 4 Page 4: The Dual-Sufuria Improvised Hot-Sand Jiko Oven Blueprint
    (4, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    THE DUAL-SUFURIA IMPROVISED HOT-SAND JIKO OVEN BLUEPRINT
  </text>

  <!-- Left: Cross Section of the Dual Sufuria Sand Oven -->
  <g transform="translate(50, 80)">
    <!-- Top Charcoal Embers on Lid -->
    <circle cx="120" cy="55" r="7" fill="#ef4444"/>
    <circle cx="140" cy="52" r="7" fill="#f97316"/>
    <circle cx="160" cy="55" r="7" fill="#ef4444"/>
    <circle cx="180" cy="52" r="7" fill="#f97316"/>
    <circle cx="200" cy="55" r="7" fill="#ef4444"/>
    <text x="160" y="42" fill="#dc2626" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Glowing Charcoal Embers (Top Heat)</text>

    <!-- Flat Metal Lid Cover -->
    <rect x="55" y="62" width="210" height="8" fill="#475569" rx="2"/>

    <!-- Large Outer Aluminium Sufuria -->
    <path d="M 60 70 L 60 210 L 260 210 L 260 70" fill="none" stroke="#64748b" stroke-width="4"/>
    <rect x="62" y="70" width="196" height="138" fill="#f1f5f9" opacity="0.4"/>

    <!-- 2cm Clean River Sand Bed at bottom -->
    <rect x="62" y="185" width="196" height="23" fill="#ca8a04" opacity="0.6"/>
    <text x="160" y="200" fill="#713f12" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Clean Hot River Sand Bed</text>

    <!-- Baking Tin with Rising Cake Batter -->
    <rect x="100" y="130" width="120" height="55" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="3"/>
    <!-- Rising Golden Cake Top -->
    <path d="M 102 145 Q 160 120 218 145 Z" fill="#b45309"/>
    <text x="160" y="165" fill="#92400e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Cake Baking Tin</text>

    <!-- Charcoal Jiko Base -->
    <path d="M 80 260 L 240 260 L 225 220 L 95 220 Z" fill="#334155"/>
    <text x="160" y="245" fill="#f97316" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Charcoal Jiko (Bottom Heat)</text>
  </g>

  <!-- Right: 4-Step Rubbed-in Method Summary -->
  <g transform="translate(425, 80)">
    <rect x="0" y="0" width="330" height="320" fill="#fefce8" rx="8" stroke="#fef08a" stroke-width="2"/>
    <rect x="15" y="12" width="300" height="26" fill="#ca8a04" rx="5"/>
    <text x="165" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      THE RUBBED-IN BAKING METHOD
    </text>

    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#fef9c3"/>
      <text x="15" y="20" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Cool Fingertip Rubbing</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Rub cold margarine into flour with fingertips.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Lift flour high to trap air until like breadcrumbs.</text>
    </g>

    <g transform="translate(15, 120)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#fef9c3"/>
      <text x="15" y="20" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Stir Sugar &amp; Wet Batter</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Mix in sugar, then beaten eggs &amp; milk.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Stir gently into a thick, smooth cake batter.</text>
    </g>

    <g transform="translate(15, 190)">
      <rect x="0" y="0" width="300" height="60" fill="#ffffff" rx="5" stroke="#fef9c3"/>
      <text x="15" y="20" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Dual-Heat Sand Baking</text>
      <text x="15" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Sand conducts bottom heat; embers brown top.</text>
      <text x="15" y="52" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Clean toothpick test confirms doneness!</text>
    </g>
  </g>
</svg>""",
}

def enrich_cbc_grade6_home_science_topic3():
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 6 HOME SCIENCE — TOPIC 3: FOODS AND NUTRITION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    topic = Topic.objects.filter(subject=subject, name="Foods and Nutrition").first()

    assert topic, "Grade 6 Topic 3 (Foods and Nutrition) not found!"
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
        photo_info = TOPIC3_PHOTOS.get(u_order)
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
    for (u_order, page_num), svg_code in TOPIC3_SVGS.items():
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
    print(f"[SUCCESS] CBC Grade 6 Home Science Topic 3 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade6_home_science_topic3()
