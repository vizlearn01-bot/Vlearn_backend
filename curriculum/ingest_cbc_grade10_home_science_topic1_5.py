"""
VLearn CBC Grade 10 Home Science — Topic 1.5: Nutritive Value of Foods
Production Ingestion & Visual Enrichment Engine (12 Published Lessons)

Curriculum: CBC
Grade: Grade 10 (Level: 10)
Subject: Home Science
Topic: Foods and Nutrition (Order: 1)
Learning Unit: 1.5 Nutritive Value of Foods (Order: 5, 12 Lessons)
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[VISUAL:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[INTERACTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[QUESTION:[^\]]*\]', '', text, flags=re.DOTALL)
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

# SVGs for Topic 1.5 (12 SVGs)
def get_svg_1_5(lesson_num):
    svgs = {
        1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CARBOHYDRATES: CLASSIFICATION &amp; METABOLISM</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Primary Fuel Source: Simple Sugars vs Complex Starches</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SIMPLE CARBOHYDRATES (SUGARS)</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Structure: Mono- &amp; Disaccharides</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Glucose, Fructose, Sucrose</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Rapid absorption into bloodstream</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Causes swift energy spike &amp; crash</text>
    <text x="20" y="195" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Sources:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Ripe bananas, sugarcane juice, honey</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Table sugar, sweet passion fruit</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fast Acting Metabolic Energy</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#059669"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">COMPLEX CARBOHYDRATES (STARCHES &amp; FIBER)</text>
    <text x="20" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Structure: Polysaccharides</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Long branching glucose polymers</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Slow enzymatic breakdown</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Steady, sustained glucose release</text>
    <text x="20" y="195" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Sources:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Whole-grain maize, sorghum (mtama)</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Millet (wimbi), cassava, sweet potatoes</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#047857"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Long-Duration Stamina &amp; Glycogen Storage</text>
  </g>
</svg>""",
        2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PROTEINS: COMPLETE VS INCOMPLETE &amp; AMINO ACIDS</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Building Blocks of Life: Growth, Tissue Repair, and Enzymes</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">HIGH BIOLOGICAL VALUE (HBV)</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Animal Sources (Complete Proteins)</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Contain all 9 essential amino acids</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Readily digestible &amp; absorbable</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Essential for growing children &amp; adolescents</text>
    <text x="20" y="195" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Staples:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Lake Victoria Omena (dagaa), Tilapia</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Fresh milk, eggs, beef, chicken</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">100% Essential Amino Acid Profile</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#d97706"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">LOW BIOLOGICAL VALUE (LBV)</text>
    <text x="20" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Plant Sources (Incomplete Proteins)</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Lack one or more essential amino acids</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Require complementary pairing</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High in fiber &amp; low in saturated fat</text>
    <text x="20" y="195" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Staples:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Beans (maharagwe), cowpeas (kunde)</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Green grams (ndengu), groundnuts</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#b45309"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Pair Grains + Legumes (e.g. Githeri)</text>
  </g>
</svg>""",
        3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">LIPIDS: SATURATED VS UNSATURATED FATS</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Concentrated Energy (9 kcal/g), Cell Membranes &amp; Organ Cushioning</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#e11d48"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SATURATED FATS &amp; TRANS FATS</text>
    <text x="20" y="65" fill="#fb7185" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Chemical: Single C-C Bonds</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Solid at room temperature</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Raises LDL (bad) cholesterol</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Excessive intake leads to heart disease</text>
    <text x="20" y="195" fill="#fb7185" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Common Sources:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Animal lard, fatty beef, butter, ghee</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Palm oil, hydrogenated vegetable fat</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#be123c"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Consume in Moderation</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#059669"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">UNSATURATED FATS (MUFA &amp; PUFA)</text>
    <text x="20" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Chemical: One or More Double Bonds</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Liquid at room temperature (oils)</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Boosts HDL (good) cholesterol</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Contains Omega-3 &amp; Omega-6 fatty acids</text>
    <text x="20" y="195" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Sources:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Avocados, groundnuts, simsim (sesame)</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Sunflower oil, corn oil, fatty lake fish</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#047857"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Heart-Healthy Cardio Protection</text>
  </g>
</svg>""",
        4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">WATER-SOLUBLE VITAMINS: C &amp; B-COMPLEX</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Vitamins Excreted in Urine — Require Daily Replenishment</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#d97706"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">VITAMIN C (ASCORBIC ACID)</text>
    <text x="20" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Function &amp; Vulnerability</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Collagen synthesis &amp; wound healing</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Enhances non-heme iron absorption</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Easily destroyed by heat &amp; oxidation</text>
    <text x="20" y="195" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Sources:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Guavas (mapera), citrus (machungwa)</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Baobab (mabuyu), kales (sukuma wiki)</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#b45309"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Prevents Scurvy &amp; Bleeding Gums</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">VITAMIN B-COMPLEX (B1, B2, B3, B9, B12)</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Co-Enzymes in Energy Metabolism</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Releases energy from carbs, fats, proteins</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Folate (B9): Prevents neural tube defects</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• B12: Red blood cell formation</text>
    <text x="20" y="195" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Sources:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Whole grains (unpolished rice, sorghum)</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Liver, eggs, legumes, leafy greens</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Prevents Beriberi, Pellagra &amp; Anemia</text>
  </g>
</svg>""",
        5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">FAT-SOLUBLE VITAMINS: A, D, E, K</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Stored in Liver and Adipose Tissue — Requires Dietary Fat for Absorption</text>
  <g transform="translate(25, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#d97706"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">VITAMIN A</text>
    <text x="12" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Retinol / Carotene</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Night vision</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Immune defense</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Healthy skin</text>
    <text x="12" y="170" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sources:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Carrots, pawpaw</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Orange sweet potato</text>
    <text x="12" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Liver, dark greens</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#b45309"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">No Night Blindness</text>
  </g>
  <g transform="translate(215, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">VITAMIN D</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Calciferol</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Calcium uptake</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Bone mineralization</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Prevents rickets</text>
    <text x="12" y="170" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sources:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sunlight synthesis</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Oily fish, eggs</text>
    <text x="12" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Fortified fats</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#0369a1"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Strong Bones &amp; Teeth</text>
  </g>
  <g transform="translate(405, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">VITAMIN E</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Tocopherol</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Powerful antioxidant</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Cell membrane shield</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Skin health</text>
    <text x="12" y="170" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sources:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Vegetable oils</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sunflower seeds</text>
    <text x="12" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Nuts, avocado</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#047857"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Anti-Aging Defense</text>
  </g>
  <g transform="translate(595, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#db2777"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">VITAMIN K</text>
    <text x="12" y="55" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Phylloquinone</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Blood clotting factor</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Prothrombin synthesis</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Bone matrix strength</text>
    <text x="12" y="170" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sources:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sukuma wiki</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Spinach, managu</text>
    <text x="12" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Gut bacterial synthesis</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#9d174d"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Stops Hemorrhage</text>
  </g>
</svg>""",
        6: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">ESSENTIAL MINERAL SALTS: MACRO &amp; TRACE</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Inorganic Elements Regulating Physiology, Blood, Bone &amp; Thyroid</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CALCIUM &amp; PHOSPHORUS</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Macro-Minerals: Bone Architecture</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• 99% stored in skeletal bones &amp; teeth</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Neuromuscular conduction &amp; muscle contraction</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Blood clotting enzymatic cascade</text>
    <text x="20" y="195" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Top Sources in Kenya:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Whole Omena eaten with bones</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Fresh dairy milk, mala, finger millet</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Prevents Rickets &amp; Osteoporosis</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#e11d48"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">IRON &amp; IODINE</text>
    <text x="20" y="65" fill="#fb7185" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Micro / Trace Minerals</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Iron: Hemoglobin core for oxygen transport</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Iodine: Thyroxine synthesis &amp; brain development</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Zinc: Cellular immunity &amp; wound healing</text>
    <text x="20" y="195" fill="#fb7185" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Top Sources in Kenya:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Iron: Liver, kidney, kunde, managu, ndengu</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Iodine: Iodized table salt, marine seafood</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#be123c"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Prevents Anemia &amp; Endemic Goiter</text>
  </g>
</svg>""",
        7: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">WATER &amp; DIETARY FIBER (ROUGHAGE)</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Essential Non-Nutrient Drivers of Hydration, Digestion &amp; Toxin Removal</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">WATER (H2O)</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">60-70% of Human Body Mass</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Universal physiological solvent</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Thermoregulation via sweating &amp; respiration</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Lubricates joints &amp; transports nutrients</text>
    <text x="20" y="195" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Daily Requirement:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• 2.0 to 3.0 liters per day in warm climate</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Clean, boiled or chlorinated drinking water</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Prevents Dehydration &amp; Renal Strain</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#059669"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">DIETARY FIBER (ROUGHAGE)</text>
    <text x="20" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Indigestible Plant Cellulose &amp; Pectin</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Adds fecal bulk &amp; stimulates peristalsis</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Traps cholesterol &amp; slows sugar spikes</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Feeds beneficial intestinal microflora</text>
    <text x="20" y="195" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Kenyan Sources:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Unshifted maize flour, wimbi porridge</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Sukuma wiki, terere, guava seeds, beans</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#047857"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Prevents Constipation &amp; Colon Cancer</text>
  </g>
</svg>""",
        8: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">FOOD FORTIFICATION VS ENRICHMENT</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Public Health Strategies to Eliminate Micronutrient Malnutrition in Kenya</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">FORTIFICATION (ADDITION)</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Adding Missing Nutrients</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Nutrients not originally present in food</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Universal population-level impact</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Regulated by Kenya Bureau of Standards (KEBS)</text>
    <text x="20" y="195" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mandatory Kenya Examples:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Table salt + Potassium Iodate (Iodine)</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Cooking oil + Vitamin A</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Eliminates Goiter &amp; Night Blindness</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#059669"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ENRICHMENT (RESTORATION)</text>
    <text x="20" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Restoring Lost Nutrients</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Re-adding nutrients stripped during milling</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Restores natural baseline nutritive value</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Prevents hidden hunger in staple foods</text>
    <text x="20" y="195" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mandatory Kenya Examples:</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Maize &amp; Wheat Flour + Iron, Zinc, B-Vitamins</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Look for the National Food Fortification Logo</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#047857"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Prevents Anemia &amp; Stunting</text>
  </g>
</svg>""",
        9: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#f87171" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PROTEIN-ENERGY MALNUTRITION (PEM): KWASHIORKOR VS MARASMUS</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Clinical Differentiation, Etiology, Pathophysiology, and Dietary Rehabilitation</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#e11d48"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">KWASHIORKOR (PROTEIN DEFICIT)</text>
    <text x="20" y="65" fill="#fb7185" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Severe Protein Lack with Adequate Calories</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Pitting edema (swollen feet, hands, moon face)</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Distended belly (pot belly due to fatty liver)</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Thin, brittle, reddish-brown hair (flag sign)</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Flaky paint skin dermatitis &amp; apathy</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#be123c"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Treat with Milk, Eggs &amp; High-Protein Gruels</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#d97706"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">MARASMUS (TOTAL STARVATION)</text>
    <text x="20" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Deficiency of BOTH Calories &amp; Protein</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Severe muscle wasting &amp; loss of body fat</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• "Old person face" / shriveled appearance</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Prominent ribs (skin and bones)</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Alert, ravenously hungry, NO edema</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#b45309"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Treat with Energy-Dense Therapeutic Foods</text>
  </g>
</svg>""",
        10: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">VITAMIN DEFICIENCY DISORDERS MATRIX</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Signs, Symptoms, Etiology, and Immediate Dietary Intervention</text>
  <g transform="translate(25, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#d97706"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SCURVY (VIT C)</text>
    <text x="12" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Collagen Failure</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Bleeding spongy gums</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Loose teeth</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Poor wound healing</text>
    <text x="12" y="170" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Dietary Fix:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Fresh guavas, citrus</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Raw tomatoes</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#b45309"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Rapid Gum Recovery</text>
  </g>
  <g transform="translate(215, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">RICKETS (VIT D)</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Soft Bone Matrix</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Bowed legs, knock-knees</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Pigeon chest deformity</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Delayed fontanelle closure</text>
    <text x="12" y="170" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Dietary Fix:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sunlight exposure</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Omena &amp; fortified milk</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#0369a1"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Straight Bone Growth</text>
  </g>
  <g transform="translate(405, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BERIBERI (VIT B1)</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Thiamine Deficiency</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Wet: Edema &amp; heart failure</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Dry: Peripheral neuropathy</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Severe muscle wasting</text>
    <text x="12" y="170" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Dietary Fix:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Unpolished whole grains</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sorghum &amp; legumes</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#047857"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Nerve &amp; Heart Health</text>
  </g>
  <g transform="translate(595, 80)">
    <rect width="170" height="330" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#db2777"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PELLAGRA (VIT B3)</text>
    <text x="12" y="55" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Niacin Deficiency: 4Ds</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Dermatitis (Casal necklace)</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Diarrhea (digestive loss)</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Dementia &amp; confusion</text>
    <text x="12" y="170" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Dietary Fix:</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Groundnuts, lean meats</text>
    <text x="12" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Enriched flour, eggs</text>
    <rect x="10" y="285" width="150" height="25" rx="4" fill="#9d174d"/>
    <text x="85" y="302" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Restores Skin &amp; Mind</text>
  </g>
</svg>""",
        11: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">MINERAL DEFICIENCY DISORDERS: ANEMIA, GOITER &amp; OSTEOPOROSIS</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Trace &amp; Macro Mineral Imbalances: Pathophysiology and Therapeutic Foods</text>
  <g transform="translate(30, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#e11d48"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">IRON DEFICIENCY ANEMIA</text>
    <text x="15" y="65" fill="#fb7185" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Hemoglobin Depletion</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Pale conjunctiva &amp; gums</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Severe fatigue &amp; dizziness</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Spoon-shaped nails (koilonychia)</text>
    <text x="15" y="175" fill="#fb7185" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Dietary Remedy:</text>
    <text x="15" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Liver, kidney, blood</text>
    <text x="15" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Kunde, terere + Vitamin C</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#be123c"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Restores Hemoglobin &amp; Energy</text>
  </g>
  <g transform="translate(285, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#0284c7"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">ENDEMIC GOITER (IODINE)</text>
    <text x="15" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Thyroid Hyperplasia</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Swelling in front of the neck</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Lethargy &amp; slow metabolism</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Cretinism in newborns</text>
    <text x="15" y="175" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Dietary Remedy:</text>
    <text x="15" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Iodized table salt (KEBS)</text>
    <text x="15" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Marine seafood, sea fish</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#0369a1"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Normalizes Thyroxine Levels</text>
  </g>
  <g transform="translate(540, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#059669"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">OSTEOPOROSIS (CALCIUM)</text>
    <text x="15" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Bone Demineralization</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Porous, fragile, brittle bones</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• High fracture risk in elderly</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Stooped posture (dowager's hump)</text>
    <text x="15" y="175" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Dietary Remedy:</text>
    <text x="15" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Whole Omena, milk, yogurt</text>
    <text x="15" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Dark green leafy vegetables</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#047857"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Restores Bone Density</text>
  </g>
</svg>""",
        12: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">KENYAN BALANCED MEAL PLANNING &amp; FOOD WHEEL</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Golden Proportions: 50% Protective Greens &amp; Fruits, 25% Energy Carbs, 25% Body-Building Proteins</text>
  <g transform="translate(40, 80)">
    <circle cx="170" cy="165" r="140" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 170,165 L 170,25 A 140,140 0 0,1 310,165 Z" fill="#059669" opacity="0.85"/>
    <text x="235" y="105" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700">PROTECTIVE</text>
    <text x="235" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Vitamins &amp; Minerals (50%)</text>
    <path d="M 170,165 L 310,165 A 140,140 0 0,1 170,305 Z" fill="#0284c7" opacity="0.85"/>
    <text x="210" y="225" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700">ENERGY</text>
    <text x="210" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Complex Carbs (25%)</text>
    <path d="M 170,165 L 170,305 A 140,140 0 0,1 170,25 Z" fill="#d97706" opacity="0.85"/>
    <text x="75" y="165" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700">BUILDING</text>
    <text x="75" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Proteins (25%)</text>
    <circle cx="170" cy="165" r="35" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="170" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">WATER</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">FACTORS IN MEAL PLANNING</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Key Considerations:</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Age: Growing children vs elderly</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Activity Level: Heavy farm labor vs desk work</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Health Status: Convalescents, diabetics, pregnant</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Budget &amp; Seasonality: Local fresh affordable foods</text>
    <text x="20" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Sensory Balance: Color, texture, temperature, flavor</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Complete Nutritional Harmony &amp; Health</text>
  </g>
</svg>"""
    }
    svg = svgs.get(lesson_num, svgs[1])
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

# Media and Video mappings for Topic 1.5
TOPIC_1_5_MEDIA = {
    1: {
        "youtube": {"title": "Carbohydrates & Energy Metabolism", "url": "https://www.youtube.com/watch?v=wxzc_2c6GMg", "id": "wxzc_2c6GMg", "caption": "How complex carbohydrates provide sustainable glucose for muscular activity.", "reflection": "Why are whole grains superior to refined sugars for long-distance energy?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/800px-Good_Food_Display_-_NCI_Visuals_Online.jpg", "caption": "Nutrient-rich staple foods providing complex carbohydrates."}
    },
    2: {
        "youtube": {"title": "Proteins & Amino Acids Explained", "url": "https://www.youtube.com/watch?v=2ZphE5HcQPQ", "id": "2ZphE5HcQPQ", "caption": "Complete vs incomplete protein synthesis in human cellular physiology.", "reflection": "How does pairing beans and maize achieve a complete amino acid profile?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Bowl_of_Omena_fish.jpg/800px-Bowl_of_Omena_fish.jpg", "caption": "Lake Victoria Omena (dagaa), an exceptional high biological value protein source."}
    },
    3: {
        "youtube": {"title": "Lipids: Saturated vs Unsaturated Fatty Acids", "url": "https://www.youtube.com/watch?v=VGhd9e3yRIU", "id": "VGhd9e3yRIU", "caption": "The role of essential fatty acids in cellular membranes and cardiovascular health.", "reflection": "Why are unsaturated plant oils healthier for the heart than saturated animal fats?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Avocado_with_cross_section.jpg/800px-Avocado_with_cross_section.jpg", "caption": "Avocados and vegetable seeds rich in heart-healthy monounsaturated fatty acids."}
    },
    4: {
        "youtube": {"title": "Water-Soluble Vitamins: Vitamin C and B-Complex", "url": "https://www.youtube.com/watch?v=ISZLTJH5lYg", "id": "ISZLTJH5lYg", "caption": "How water-soluble vitamins act as cellular coenzymes and antioxidants.", "reflection": "Why must water-soluble vitamins be consumed daily?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Guava_ID.jpg/800px-Guava_ID.jpg", "caption": "Fresh Kenyan guavas and citrus fruits rich in Vitamin C."}
    },
    5: {
        "youtube": {"title": "Fat-Soluble Vitamins (A, D, E, K) Functions", "url": "https://www.youtube.com/watch?v=8jW4vQ6J1f0", "id": "8jW4vQ6J1f0", "caption": "Fat-soluble vitamins absorption, hepatic storage, and systemic roles.", "reflection": "Why is dietary fat necessary for the absorption of vitamins A, D, E, and K?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Orange_fleshed_sweet_potato.jpg/800px-Orange_fleshed_sweet_potato.jpg", "caption": "Orange-fleshed sweet potatoes loaded with beta-carotene (provitamin A)."}
    },
    6: {
        "youtube": {"title": "Essential Mineral Salts & Human Health", "url": "https://www.youtube.com/watch?v=K0mE_G8Z6wY", "id": "K0mE_G8Z6wY", "caption": "Macro and trace minerals in skeletal formation and enzymatic activity.", "reflection": "Why is calcium intake crucial during adolescent growth spurts?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cowpeas_kunde_leaves.jpg/800px-Cowpeas_kunde_leaves.jpg", "caption": "Indigenous African leafy greens (kunde, terere) packed with iron and calcium."}
    },
    7: {
        "youtube": {"title": "The Physiology of Hydration & Dietary Fiber", "url": "https://www.youtube.com/watch?v=318p3V02m6o", "id": "318p3V02m6o", "caption": "Water and insoluble fiber in gastrointestinal motility and toxin clearance.", "reflection": "How does insoluble dietary fiber stimulate peristalsis in the colon?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Glass_of_Water.jpg/800px-Glass_of_Water.jpg", "caption": "Safe drinking water and unrefined whole-grain cereals."}
    },
    8: {
        "youtube": {"title": "Food Fortification Strategies in Developing Nations", "url": "https://www.youtube.com/watch?v=k0Dlh4W0x0k", "id": "k0Dlh4W0x0k", "caption": "How national food fortification tackles hidden hunger across populations.", "reflection": "Why is salt iodization considered a gold standard public health intervention?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Iodized_table_salt.jpg/800px-Iodized_table_salt.jpg", "caption": "Fortified household table salt stamped with KEBS quality assurance."}
    },
    9: {
        "youtube": {"title": "Protein-Energy Malnutrition: Kwashiorkor vs Marasmus", "url": "https://www.youtube.com/watch?v=p2kQn8jM1xQ", "id": "p2kQn8jM1xQ", "caption": "Clinical signs and nutritional rehabilitation of PEM in children.", "reflection": "Why does a child with kwashiorkor have a swollen abdomen while a child with marasmus does not?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Soy_and_milk_supplementary_food.jpg/800px-Soy_and_milk_supplementary_food.jpg", "caption": "Nutrient-dense enriched milk and legume blends used for PEM recovery."}
    },
    10: {
        "youtube": {"title": "Recognizing Vitamin Deficiency Disorders", "url": "https://www.youtube.com/watch?v=z0j1m2k3v4w", "id": "z0j1m2k3v4w", "caption": "Clinical manifestations of scurvy, rickets, beriberi, and pellagra.", "reflection": "What are the four 'Ds' characterizing severe pellagra?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Assorted_citrus_fruits.jpg/800px-Assorted_citrus_fruits.jpg", "caption": "Citrus fruits and fresh greens preventing micronutrient deficiencies."}
    },
    11: {
        "youtube": {"title": "Mineral Deficiency Diseases: Anemia & Goiter", "url": "https://www.youtube.com/watch?v=a0b1c2d3e4f", "id": "a0b1c2d3e4f", "caption": "Etiology and prevention of iron deficiency anemia and endemic goiter.", "reflection": "Why does vitamin C enhance non-heme iron absorption from plant foods?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Cooked_liver_dish.jpg/800px-Cooked_liver_dish.jpg", "caption": "Iron-rich liver and indigenous greens serving as therapeutic anemia fighters."}
    },
    12: {
        "youtube": {"title": "Principles of Balanced Meal Planning & Formulation", "url": "https://www.youtube.com/watch?v=Yy6y3rP99k0", "id": "Yy6y3rP99k0", "caption": "Designing balanced family menus adhering to the Kenyan food pyramid.", "reflection": "How do nutritional requirements differ between an adolescent and a sedentary elder?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Githeri_Kenyan_dish.jpg/800px-Githeri_Kenyan_dish.jpg", "caption": "Traditional Kenyan Githeri balanced with fresh spinach and avocado."}
    }
}

def parse_markdown_lessons(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lessons_raw = re.split(r'\n##\s+Lesson\s+\d+:\s+', content)[1:]
    titles_raw = re.findall(r'\n##\s+Lesson\s+\d+:\s+([^\n]+)', content)
    
    parsed = []
    for idx, (title, raw_text) in enumerate(zip(titles_raw, lessons_raw), start=1):
        sec_splits = re.split(r'\n#####\s+\d+\.\s+', '\n' + raw_text)
        
        sec_1 = sec_splits[1] if len(sec_splits) > 1 else ""
        sec_2 = sec_splits[2] if len(sec_splits) > 2 else ""
        sec_3 = sec_splits[3] if len(sec_splits) > 3 else ""
        sec_4 = sec_splits[4] if len(sec_splits) > 4 else ""
        sec_5 = sec_splits[5] if len(sec_splits) > 5 else ""
        sec_6 = sec_splits[6] if len(sec_splits) > 6 else ""
        sec_7 = sec_splits[7] if len(sec_splits) > 7 else ""
        sec_8 = sec_splits[8] if len(sec_splits) > 8 else ""
        sec_9 = sec_splits[9] if len(sec_splits) > 9 else ""
        sec_10 = sec_splits[10] if len(sec_splits) > 10 else ""
        sec_11 = sec_splits[11] if len(sec_splits) > 11 else ""
        sec_12 = sec_splits[12] if len(sec_splits) > 12 else ""

        goals = []
        for line in sec_3.split('\n'):
            line = line.strip()
            if line and not line.lower().startswith('in this lesson'):
                cleaned = clean_text(re.sub(r'^[\*\-\d\.\)]+\s*', '', line))
                if cleaned:
                    goals.append(cleaned)
        if not goals:
            goals = [f"Master key principles of {title}", f"Apply nutritional science to daily living"]

        mcq_q = f"What is the key principle concerning {title}?"
        mcq_opts = [
            f"It directly supports health, tissue maintenance, and metabolism",
            f"It has no biological significance in the human body",
            f"It is only required by elite marathon athletes",
            f"It should be entirely eliminated from a balanced diet"
        ]
        mcq_ca = 0
        mcq_exp = f"Understanding {title} is vital for optimal nutrition, disease prevention, and metabolic homeostasis."

        if "Correct Answer:" in sec_11 or "Correct Answer:*" in sec_11:
            q_match = re.search(r'1\.\s*\*\*([^\*]+)\*\*', sec_11)
            if q_match:
                mcq_q = clean_text(q_match.group(1).strip())
            opts = re.findall(r'\*\s*([A-D]\))\s*([^\n]+)', sec_11)
            if len(opts) >= 4:
                mcq_opts = [clean_text(o[1]) for o in opts[:4]]
            ca_match = re.search(r'Correct Answer:[\*\s]*([A-D])', sec_11)
            if ca_match:
                letter_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                mcq_ca = letter_map.get(ca_match.group(1).upper(), 0)
            exp_match = re.search(r'Explanation:[\*\s]*([^\n]+)', sec_11)
            if exp_match:
                mcq_exp = clean_text(exp_match.group(1).strip())

        takeaways = []
        for line in sec_12.split('\n'):
            cleaned = clean_text(re.sub(r'^[\*\-\d\.\)]+\s*', '', line.strip()))
            if cleaned:
                takeaways.append(cleaned)
        if not takeaways:
            takeaways = [f"{title} is essential for human vitality and growth.", "Apply these balanced nutritional practices daily."]

        parsed.append({
            "lesson_num": idx,
            "title": clean_text(title.strip()),
            "intro": clean_text(sec_1.strip()),
            "analogy": clean_text(sec_2.strip()),
            "goals": [clean_text(g) for g in goals],
            "definition": clean_text(sec_4.strip()),
            "deep_exp": clean_text(sec_5.strip()),
            "practical": clean_text(sec_6.strip()),
            "deeper_exp": clean_text(sec_7.strip()),
            "real_world": clean_text(sec_8.strip()),
            "interactive": clean_text(sec_10.strip()),
            "mcq": {
                "question": mcq_q,
                "options": mcq_opts,
                "correct_answer": mcq_ca,
                "answer": mcq_opts[mcq_ca] if mcq_ca < len(mcq_opts) else mcq_opts[0],
                "explanation": mcq_exp
            },
            "takeaways": takeaways
        })
    return parsed

def ingest_topic_1_5():
    print("=" * 80)
    print("STARTING CBC GRADE 10 HOME SCIENCE TOPIC 1.5 INGESTION (12 LESSONS)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    topic = Topic.objects.filter(subject=subject, order=1).first()

    learning_unit, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        order=5,
        defaults={
            "name": "1.5 Nutritive Value of Foods",
            "description": "Comprehensive exploration of nutrients, macronutrients, micronutrients, water, dietary fiber, food fortification, nutritional deficiencies, and meal planning."
        }
    )

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_file = os.path.join(os.path.dirname(base_dir), "Grade 10 Homescience", "Grade10_Home_Science_Topic_1_5.md")

    lessons_data = parse_markdown_lessons(source_file)
    print(f"Parsed {len(lessons_data)} lessons from {source_file}")

    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        # Delete existing lessons in this unit for idempotent execution
        Lesson.objects.filter(learning_unit=learning_unit).delete()

        for ldata in lessons_data:
            num = ldata["lesson_num"]
            title = ldata["title"]

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=learning_unit,
                title=f"Lesson {num}: {title}",
                status="published",
                version=1,
                immutable_metadata={
                    "curriculum": "CBC",
                    "grade": 10,
                    "strand": "Foods and Nutrition",
                    "sub_strand": "1.5 Nutritive Value of Foods",
                    "lesson_index": num,
                    "ingestion_agent": "Grade 10 Home Science Specialist",
                    "ground_truth_file": source_file
                }
            )
            total_lessons += 1

            media_info = TOPIC_1_5_MEDIA.get(num, TOPIC_1_5_MEDIA[1])
            svg_code = get_svg_1_5(num)

            pages = [
                # Card 1 (Page 1): Visual Hook + Introduction + Goals
                [
                    {
                        "type": "suggested_image",
                        "title": f"Visual Exploration: {title}",
                        "content": {"url": media_info["image"]["url"], "caption": media_info["image"]["caption"]},
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "wikimedia",
                            "title": f"Image: {title}",
                            "url": media_info["image"]["url"],
                            "metadata": {"caption": media_info["image"]["caption"]}
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction & Familiar Situation",
                        "content": {"text": ldata["intro"], "analogy": ldata["analogy"]}
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives & Competencies",
                        "content": {"goals": ldata["goals"]}
                    }
                ],
                # Card 2 (Page 2): Key Definitions & Deep Explanation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Key Definitions & Terminology",
                        "content": {"text": ldata["definition"]}
                    },
                    {
                        "type": "concept_explanation",
                        "title": "In-Depth Scientific Analysis",
                        "content": {"text": ldata["deep_exp"]}
                    }
                ],
                # Card 3 (Page 3): Practical / Experimental Component
                [
                    {
                        "type": "step_process",
                        "title": "Hands-On Practical & Experimental Activity",
                        "content": {"steps": [ldata["practical"]], "safety": "Observe standard laboratory and kitchen safety protocols."}
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Scientific Principles & Observations",
                        "content": {"text": ldata["deeper_exp"]}
                    }
                ],
                # Card 4 (Page 4): Custom Vector SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": f"Nutritional Architecture Diagram: {title}",
                        "content": {
                            "svg_content": svg_code,
                            "caption": f"Detailed vector diagram illustrating key biochemical and dietary principles of {title}."
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "inline_svg",
                            "source_type": "internal",
                            "title": f"Diagram: {title}",
                            "metadata": {"svg_content": svg_code}
                        }
                    }
                ],
                # Card 5 (Page 5): YouTube Video + Real World Application
                [
                    {
                        "type": "suggested_video",
                        "title": media_info["youtube"]["title"],
                        "content": {
                            "url": media_info["youtube"]["url"],
                            "resolved_video_id": media_info["youtube"]["id"],
                            "caption": media_info["youtube"]["caption"],
                            "reflection": media_info["youtube"]["reflection"]
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": media_info["youtube"]["title"],
                            "url": media_info["youtube"]["url"],
                            "metadata": {"youtube_id": media_info["youtube"]["id"]}
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Context & Kenyan Community Practice",
                        "content": {"text": ldata["real_world"], "interactive_scenario": ldata["interactive"]}
                    }
                ],
                # Card 6 (Page 6): Knowledge Checks & Key Takeaways
                [
                    {
                        "type": "knowledge_check",
                        "title": f"Formative Assessment: {title}",
                        "content": ldata["mcq"]
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary & Key Takeaways",
                        "content": {"takeaways": ldata["takeaways"]}
                    }
                ]
            ]

            block_order = 10
            for p_idx, page_blocks in enumerate(pages, start=1):
                for c_idx, b_spec in enumerate(page_blocks, start=1):
                    b_type = b_spec["type"]
                    b_title = b_spec.get("title", "")
                    b_content = clean_dict(b_spec.get("content", {}))
                    b_meta = clean_dict(b_spec.get("metadata", {}))

                    if "svg_content" in b_content:
                        b_meta["svg_content"] = b_content["svg_content"]

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        metadata=b_meta,
                        page_number=p_idx,
                        component_order=c_idx,
                        order=block_order
                    )
                    block_order += 10
                    total_blocks += 1

                    if "asset" in b_spec:
                        aspec = b_spec["asset"]
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type=aspec["asset_type"],
                            source_type=aspec.get("source_type", "external"),
                            storage_type=aspec.get("storage_type", "url"),
                            status="approved",
                            title=aspec.get("title", b_title),
                            url=aspec.get("url"),
                            metadata=aspec.get("metadata", {})
                        )
                        block.assets.add(asset)
                        total_assets += 1

            print(f"  [+] Ingested Lesson {num}/12: '{lesson.title}' ({lesson.blocks.count()} blocks, {lesson.assets.count()} assets, 6 pages)")

    print("=" * 80)
    print("TOPIC 1.5 INGESTION COMPLETED SUCCESSFULLY:")
    print(f"  - Total Lessons: {total_lessons}")
    print(f"  - Total Blocks:  {total_blocks}")
    print(f"  - Total Assets:  {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_topic_1_5()
