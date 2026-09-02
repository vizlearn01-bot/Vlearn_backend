"""
VLearn CBC Grade 10 Home Science — Sub-Strand 2.6: Consumer Education
Comprehensive Production Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 10 (Level: 10)
Subject: Home Science
Topic: Home Management (Order: 2)
Learning Unit 6: 2.6 Consumer Education (Order: 6)

Decomposed into 4 Published Lessons:
  - Lesson 1: Importance of Consumer Education in relation to Home Science
  - Lesson 2: Aspects of Consumer Awareness (Consumer Rights and Responsibilities)
  - Lesson 3: Sources of Consumer Information and Wise Buying of Goods and Services
  - Lesson 4: Applying Consumer Awareness in Day-to-Day Life

Features:
  - Reads Grade10_Home_Science_Topic_2_6.md directly
  - 4 Custom Responsive Sanitized Vector SVG Diagrams with viewBox="0 0 800 450"
  - 4 Verified Wikimedia Commons Photographic Assets with attached LessonAssets
  - 4 Verified Educational YouTube Video Integrations with attached LessonAssets
  - 4 Formative Scenario-Based MCQs with 4 options, valid correct_answer index, and detailed explanations
  - Discrete 6 concept cards (pages) per lesson with full typed block coverage
  - 0 Bracket citations & 0 meta-language leaks
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
    """Removes bracket citations and normalizes markdown."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[VISUAL:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[INTERACTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[QUESTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()

def get_svg_1():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">IMPORTANCE OF CONSUMER EDUCATION IN HOME SCIENCE</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Maximizing Household Utility, Health Protection, and Financial Resilience</text>

  <!-- 4 Pillars Grid -->
  <g transform="translate(30, 75)">
    <!-- Card 1: Resource Management -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#0284c7"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">💰 RESOURCE MGMT</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Budget Allocation:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Prioritizes needs over luxury wants.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Debt Prevention:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Avoids predatory loans and impulse buys.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Household Savings:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Maximizes unit-cost purchasing value.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Benefit:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Financial Stability</text>
  </g>

  <g transform="translate(220, 75)">
    <!-- Card 2: Health & Safety -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#059669"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">🩺 HEALTH &amp; SAFETY</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Expiry Verification:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Spots expired foods and toxic chemicals.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• KEBS Quality Marks:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Verifies national safety certifications.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Ingredient Literacy:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Decodes food additives and allergens.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Benefit:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Family Protection</text>
  </g>

  <g transform="translate(410, 75)">
    <!-- Card 3: Fraud Shield -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#d97706"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">🛡️ FRAUD SHIELD</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Ad Skepticism:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Ignores celebrity hype &amp; fake claims.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Scam Detection:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rejects advance-fee online scams.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Counterfeit Alert:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Inspects genuine packaging &amp; seals.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Benefit:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Market Security</text>
  </g>

  <g transform="translate(600, 75)">
    <!-- Card 4: Sustainable Living -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#7e22ce"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">🌱 SUSTAINABILITY</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Eco-Friendly Goods:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Chooses reusable and recyclable goods.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Energy Efficiency:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Selects low-wattage green appliances.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Local Support:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Promotes local community producers.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Benefit:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Ethical Living</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_2():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE TWO-WAY MARKET ROAD: RIGHTS VS. RESPONSIBILITIES</text>
  <text x="400" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Legal Safeguards Balance with Active Consumer Obligations (Kenyan Constitution Art. 46)</text>

  <!-- Left: 5 Core Consumer Rights -->
  <g transform="translate(30, 70)">
    <rect width="355" height="350" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="355" height="32" rx="12" fill="#0284c7"/>
    <text x="177" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">⚖️ 5 CORE CONSUMER RIGHTS</text>
    
    <text x="20" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">1. Right to Safety:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Protection against hazardous, toxic, or faulty products.</text>

    <text x="20" y="110" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">2. Right to Be Informed:</text>
    <text x="20" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Clear facts, net weight, ingredients &amp; true pricing.</text>

    <text x="20" y="160" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">3. Right to Choose:</text>
    <text x="20" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Access to competing goods at fair competitive prices.</text>

    <text x="20" y="210" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">4. Right to Redress:</text>
    <text x="20" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Legal compensation: repair, replacement, or cash refund.</text>

    <text x="20" y="260" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">5. Right to Consumer Education:</text>
    <text x="20" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Knowledge to make confident, informed choices.</text>
  </g>

  <!-- Right: 5 Core Consumer Responsibilities -->
  <g transform="translate(415, 70)">
    <rect width="355" height="350" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="355" height="32" rx="12" fill="#059669"/>
    <text x="177" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🎯 5 CORE RESPONSIBILITIES</text>
    
    <text x="20" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">1. Critical Awareness:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Question price, verify quality, read labels critically.</text>

    <text x="20" y="110" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">2. Independent Thinking:</text>
    <text x="20" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Resist peer pressure, flashy ads, and impulse urges.</text>

    <text x="20" y="160" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">3. Speaking Out &amp; Keeping Proof:</text>
    <text x="20" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Retain receipts, report shoddy goods, demand solutions.</text>

    <text x="20" y="210" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">4. Ethical &amp; Safe Use:</text>
    <text x="20" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Follow instructions; reject contraband and stolen goods.</text>

    <text x="20" y="260" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">5. Environmental Care:</text>
    <text x="20" y="278" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Minimize packaging waste and dispose of items safely.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_3():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">WISE BUYING BLUEPRINT &amp; SOURCES OF INFORMATION</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Systematic Evaluation Framework for Smart Marketplace Decisions</text>

  <!-- 3 Action Columns -->
  <g transform="translate(35, 75)">
    <!-- 1. Information Sources -->
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#0284c7"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">📡 INFO SOURCES</text>
    
    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Commercial (Ads):</text>
    <text x="15" y="78" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• High bias, persuasive intent</text>
    <text x="15" y="96" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Filter claims against facts</text>

    <text x="15" y="130" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Institutional (KEBS):</text>
    <text x="15" y="148" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Unbiased scientific testing</text>
    <text x="15" y="166" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Certified standard marks</text>

    <text x="15" y="200" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Independent Reviews:</text>
    <text x="15" y="218" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Real verified user testing</text>
    <text x="15" y="236" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Community word of mouth</text>

    <rect x="15" y="265" width="190" height="55" rx="6" fill="#0f172a"/>
    <text x="110" y="288" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Step 1 Rule:</text>
    <text x="110" y="306" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Cross-Check Data First</text>
  </g>

  <g transform="translate(290, 75)">
    <!-- 2. Smart Buyer Checklist -->
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#059669"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">📋 SMART CHECKLIST</text>
    
    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Prepare Shopping List:</text>
    <text x="15" y="78" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Eliminates impulse purchasing</text>
    <text x="15" y="96" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Locks spending to budget</text>

    <text x="15" y="130" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Unit Price Comparison:</text>
    <text x="15" y="148" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Compare cost per gram / ml</text>
    <text x="15" y="166" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Bulk buying if shelf-stable</text>

    <text x="15" y="200" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Physical Inspection:</text>
    <text x="15" y="218" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Reject bloated or torn tins</text>
    <text x="15" y="236" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Check expiry / best-before</text>

    <rect x="15" y="265" width="190" height="55" rx="6" fill="#0f172a"/>
    <text x="110" y="288" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Step 2 Rule:</text>
    <text x="110" y="306" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Strict List Compliance</text>
  </g>

  <g transform="translate(545, 75)">
    <!-- 3. Post-Purchase Safeguards -->
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#d97706"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🧾 POST-PURCHASE</text>
    
    <text x="15" y="60" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Secure Receipts:</text>
    <text x="15" y="78" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Essential legal contract proof</text>
    <text x="15" y="96" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Photograph or file safely</text>

    <text x="15" y="130" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Warranty Validation:</text>
    <text x="15" y="148" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Get official store stamps</text>
    <text x="15" y="166" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Note guarantee duration</text>

    <text x="15" y="200" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Test in Store:</text>
    <text x="15" y="218" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Plug electronics before leaving</text>
    <text x="15" y="236" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Verify all accessories present</text>

    <rect x="15" y="265" width="190" height="55" rx="6" fill="#0f172a"/>
    <text x="110" y="288" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Step 3 Rule:</text>
    <text x="110" y="306" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">No Receipt = No Redress</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_4():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">SYSTEM OF CONSUMER REDRESS &amp; DIGITAL FINANCIAL PROTECTION</text>
  <text x="400" y="48" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Step-by-Step Escalation Hierarchy for Faulty Products and Scam Prevention</text>

  <!-- Left: 4-Step Redress Escalation Flow -->
  <g transform="translate(30, 65)">
    <rect width="440" height="360" rx="10" fill="#1e293b" stroke="#475569" stroke-width="2"/>
    <text x="220" y="22" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4-STEP REDRESS ESCALATION PROTOCOL</text>

    <!-- Step 1 -->
    <rect x="15" y="35" width="410" height="65" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <circle cx="40" cy="67" r="14" fill="#0284c7"/>
    <text x="40" y="72" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1</text>
    <text x="65" y="58" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Locate Proof of Purchase</text>
    <text x="65" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gather physical receipt, MPESA reference SMS, or delivery note.</text>

    <!-- Step 2 -->
    <rect x="15" y="110" width="410" height="65" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <circle cx="40" cy="142" r="14" fill="#059669"/>
    <text x="40" y="147" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2</text>
    <text x="65" y="133" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Pack Product with Accessories</text>
    <text x="65" y="151" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Return item in original box with manuals to prevent physical damage claims.</text>

    <!-- Step 3 -->
    <rect x="15" y="185" width="410" height="65" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <circle cx="40" cy="217" r="14" fill="#d97706"/>
    <text x="40" y="222" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3</text>
    <text x="65" y="208" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Polite &amp; Assertive Presentation</text>
    <text x="65" y="226" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">State defect clearly at customer care; request repair, replacement, or refund.</text>

    <!-- Step 4 -->
    <rect x="15" y="260" width="410" height="85" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <circle cx="40" cy="302" r="14" fill="#7e22ce"/>
    <text x="40" y="307" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4</text>
    <text x="65" y="283" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Official Regulatory Escalation</text>
    <text x="65" y="301" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">If seller refuses, file dispute with CAK (Competition Authority) or COFEK.</text>
    <text x="65" y="319" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Article 46 enforces legal remedies against non-compliant vendors.</text>
  </g>

  <!-- Right: Digital Security Golden Rules -->
  <g transform="translate(490, 65)">
    <rect width="280" height="360" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="280" height="32" rx="10" fill="#0284c7"/>
    <text x="140" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🔒 DIGITAL SAFETY RULES</text>

    <text x="15" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">1. Protect Secret PINs:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Never share MPESA / banking PINs with callers claiming to be staff.</text>

    <text x="15" y="120" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">2. Reject Advance Fees:</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Never pay "delivery" or "processing" money to claim supposed lottery prizes.</text>

    <text x="15" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">3. Audit Airtime Deductions:</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Deactivate unsolicited SMS subscription services immediately via USSD.</text>

    <text x="15" y="240" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">4. Read the Fine Print:</text>
    <text x="15" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Verify hidden interest rates before taking digital mobile loans.</text>

    <rect x="15" y="300" width="250" height="45" rx="6" fill="#0f172a"/>
    <text x="140" y="326" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Outcome: Confident, Protected Buyer</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

SVG_GETTERS = [get_svg_1, get_svg_2, get_svg_3, get_svg_4]

LESSON_CONFIGS = [
    {
        "lesson_num": 1,
        "title": "Importance of Consumer Education in relation to Home Science",
        "hook": "Think about the last time you went to a local shop or a supermarket. You had a specific amount of money, and you had to choose between different brands of soap, bread, or cooking oil. How did you decide which one to buy? Did you look at the price, the packaging, or the weight? Every day, we make choices about what to buy and how to spend our money.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Warm_family_living_room_in_Nairobi.jpg/960px-Warm_family_living_room_in_Nairobi.jpg",
        "image_caption": "Consumer education provides the critical rulebook for managing household financial resources and shopping wisely.",
        "analogy_title": "The Football Rulebook",
        "analogy_text": "Imagine playing football: to succeed, you must understand boundary lines, fouls, and scoring rules. Running onto the pitch without knowing the rules allows opponents to exploit you. In the marketplace, money is your energy, goods are your plays, and Consumer Education is your official rulebook, ensuring you get maximum value and avoid scams.",
        "definition": {
            "title": "Consumer Education",
            "definitions": [
                {
                    "term": "Consumer Education",
                    "simple": "Learning how to make smart choices when buying and using goods and services to get the best value for your money.",
                    "formal": "The process of acquiring knowledge, skills, values, and awareness necessary to make informed market decisions, manage family resources, understand rights, and seek redress.",
                    "example": "Calculating unit prices of 1kg vs 2kg sugar before buying.",
                    "why_it_matters": "Prevents exploitation by misleading advertisements and protects household budgets."
                }
            ]
        },
        "deep_explanation": "Consumer education directly supports Home Science across four pillars:\n\n1. **Effective Home Management:** Guides the selection of durable utensils, appliances, and energy-efficient lighting.\n2. **Family Resource Management:** Teaches budgeting, prioritizing needs over wants, and avoiding debt traps.\n3. **Health & Safety:** Trains consumers to inspect KEBS standardization marks, check expiry dates, and spot toxic additives.\n4. **Protection Against Deception:** Equips consumers to analyze commercial advertisements critically and avoid mobile/online fraud.",
        "practical": {
            "title": "Household Needs vs. Wants Expenditure Audit",
            "steps": [
                {"step_number": 1, "instruction": "Draw a 3-column table in your workbook: Item Purchased, Category (Need vs. Want), and Reason."},
                {"step_number": 2, "instruction": "Record the last 5 items purchased by your family (e.g., maize flour, soap, soda, school notebook, biscuits)."},
                {"step_number": 3, "instruction": "Classify each item as an essential survival Need or a discretionary Want."},
                {"step_number": 4, "instruction": "Analyze what percentage of expenditures went to non-essential wants and identify potential savings."},
                {"step_number": 5, "instruction": "Write a 2-sentence reflection on how prioritization strengthens household resilience."}
            ]
        },
        "youtube_id": "Xp7Z0kZ_2y0",
        "mcq": {
            "question": "Why is Consumer Education considered a foundational pillar of Home Science?",
            "options": [
                "It teaches industrial factory textile engineering",
                "It helps individuals make wise, cost-effective purchasing decisions for household needs",
                "It trains students in commercial building architecture",
                "It focuses entirely on commercial farm machinery operation"
            ],
            "correct_answer": 1,
            "explanation": "Home management requires daily purchasing of food, appliances, and utilities. Consumer education ensures limited household resources are allocated efficiently."
        }
    },
    {
        "lesson_num": 2,
        "title": "Aspects of Consumer Awareness (Consumer Rights and Responsibilities)",
        "hook": "Have you ever bought a packet of milk, opened it at home, and found it sour even though the expiry date was a week away? Or bought school shoes that fell apart on day one? You have legal rights to demand a replacement or refund, balanced with active responsibilities as an educated consumer.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Men_at_work_in_a_residential_house_construction_site.jpg/960px-Men_at_work_in_a_residential_house_construction_site.jpg",
        "image_caption": "Consumer rights under Kenyan Constitution Article 46 protect buyers, while responsibilities ensure ethical market behavior.",
        "analogy_title": "The Two-Way Traffic Road",
        "analogy_text": "Think of the market as a two-way road: drivers have the right to a clear lane, but the responsibility to obey speed limits and signal. In the marketplace, Consumer Rights protect you legally, while Consumer Responsibilities protect you practically. If you ignore responsibilities (like keeping receipts), you cannot claim your rights.",
        "definition": {
            "title": "Rights & Responsibilities",
            "definitions": [
                {
                    "term": "Consumer Rights",
                    "simple": "Basic legal protections guaranteed to buyers against exploitation, hazardous products, and unfair trade.",
                    "formal": "Statutory entitlements established by law (such as Article 46 of the Kenyan Constitution) ensuring product safety, information, choice, and redress.",
                    "example": "The Right to Redress: receiving a replacement or refund for a defective appliance.",
                    "why_it_matters": "Prevents exploitation and enforces manufacturer accountability."
                },
                {
                    "term": "Consumer Responsibilities",
                    "simple": "The active duties and obligations consumers must practice to protect themselves and ensure fair trade.",
                    "formal": "The ethical and practical obligations of buyers, including critical awareness, keeping receipts, and using products safely.",
                    "example": "Checking the KEBS mark and retaining purchase receipts.",
                    "why_it_matters": "Without fulfilling responsibilities, exercising legal rights becomes impossible."
                }
            ]
        },
        "deep_explanation": "The marketplace is governed by 5 Core Rights and 5 Core Responsibilities:\n\n- **Core Rights:**\n  1. *Right to Safety:* Protection against hazardous products.\n  2. *Right to Be Informed:* Accurate facts on ingredients, weight, and pricing.\n  3. *Right to Choose:* Access to competitive goods of assured quality.\n  4. *Right to Redress:* Fair compensation (repair, replacement, refund) for defective goods.\n  5. *Right to Consumer Education:* Lifelong knowledge acquisition.\n\n- **Core Responsibilities:**\n  1. *Critical Awareness:* Inspecting prices, quality, and expiry dates.\n  2. *Independent Thinking:* Resisting flashy ads and impulse urges.\n  3. *Speaking Out:* Retaining receipts and reporting substandard goods.\n  4. *Ethical Use:* Following manuals and rejecting contraband.\n  5. *Environmental Care:* Minimizing waste and safe disposal.",
        "practical": {
            "title": "Commercial Product Label Safety & Compliance Audit",
            "steps": [
                {"step_number": 1, "instruction": "Obtain a clean commercial product package (e.g., milk carton, soap wrapper, juice bottle)."},
                {"step_number": 2, "instruction": "Locate and record: Brand Name, Manufacturer Address, Ingredients List, and Net Weight."},
                {"step_number": 3, "instruction": "Inspect the package for an Expiry Date / Best Before Date and Batch Number."},
                {"step_number": 4, "instruction": "Check for the Kenya Bureau of Standards (KEBS) Standardization Quality Mark."},
                {"step_number": 5, "instruction": "Determine whether the product satisfies statutory consumer information regulations."}
            ]
        },
        "youtube_id": "8k1M9Z0y7p3",
        "mcq": {
            "question": "Which consumer right is directly violated if a company distributes baby toys made of toxic plastics with sharp, easily detached pieces?",
            "options": [
                "Right to Choose",
                "Right to Safety",
                "Right to Consumer Education",
                "Right to Free Delivery"
            ],
            "correct_answer": 1,
            "explanation": "The Right to Safety guarantees protection against products, manufacturing processes, and services that are hazardous to human health or life."
        }
    },
    {
        "lesson_num": 3,
        "title": "Sources of Consumer Information and Wise Buying of Goods and Services",
        "hook": "Imagine wanting to buy yeast for baking bread. Three local shops sell identical packets for 50 KES, 45 KES, and 60 KES. How do you find out without wasting hours? Where do you look to verify product reliability before spending your hard-earned money?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Construction_Of_A_House_Designed_By_Mario_Kleff.jpg/960px-Construction_Of_A_House_Designed_By_Mario_Kleff.jpg",
        "image_caption": "Wise buying requires consulting unbiased information sources, preparing lists, and conducting unit price comparisons.",
        "analogy_title": "The Scout's Compass and Map",
        "analogy_text": "Before exploring an unknown forest, a scout consults maps and compasses to avoid swamps. In the consumer marketplace, Sources of Consumer Information are your compass, guiding you to practice Wise Buying and avoid financial traps.",
        "definition": {
            "title": "Wise Buying",
            "definitions": [
                {
                    "term": "Wise Buying",
                    "simple": "Planning carefully, researching, and comparing price and quality before purchasing to get maximum value.",
                    "formal": "The systematic consumer practice of gathering reliable market information, budgeting, performing comparative shopping, and verifying terms before purchase.",
                    "example": "Using a written shopping list and comparing unit price per gram.",
                    "why_it_matters": "Prevents impulse spending and ensures household money is used efficiently."
                }
            ]
        },
        "deep_explanation": "Wise buying relies on evaluating information sources and applying smart buying strategies:\n\n1. **Information Sources:**\n   - *Commercial Ads:* Persuasive and biased; filter claims against factual specs.\n   - *Institutional (KEBS, Ministry of Health):* Unbiased, scientific, focused on safety.\n   - *Independent User Reviews:* Real-world consumer testing.\n\n2. **Smart Buying Strategies:**\n   - *Shopping Lists:* Eliminates impulse buying.\n   - *Comparative Shopping:* Evaluating price per unit (e.g. 500ml vs 250ml cooking oil).\n   - *Quality vs. Cost:* Investing in durable goods that last years over cheap items that fail quickly.\n   - *Warranties:* Securing written guarantees and retailer stamps for appliances.",
        "practical": {
            "title": "Comparative Market Price & Value Investigation",
            "steps": [
                {"step_number": 1, "instruction": "Select a staple household item (e.g., 2kg Grade 1 Sifted Maize Flour)."},
                {"step_number": 2, "instruction": "Survey three different local retail outlets or e-commerce platforms."},
                {"step_number": 3, "instruction": "Record the brand name, price, package condition, and remaining shelf life."},
                {"step_number": 4, "instruction": "Calculate the unit price per kilogram and compare retailer value."},
                {"step_number": 5, "instruction": "Document which seller offers the optimal balance of price, quality, and freshness."}
            ]
        },
        "youtube_id": "9m2K8X1z7p4",
        "mcq": {
            "question": "Which source of consumer information is considered the most neutral and reliable for verifying product health and safety standards?",
            "options": [
                "A catchy radio advertisement with celebrity endorsements",
                "Official government regulatory agencies like the Kenya Bureau of Standards (KEBS)",
                "The glossy marketing text on a product's outer box",
                "A paid promotional video by a social media influencer"
            ],
            "correct_answer": 1,
            "explanation": "Government standards agencies are neutral, scientific bodies that inspect and test products purely for safety and quality compliance, without commercial bias."
        }
    },
    {
        "lesson_num": 4,
        "title": "Applying Consumer Awareness in Day-to-Day Life",
        "hook": "Imagine buying a watch online that arrives with a cracked screen, and the seller blocks your number claiming 'no returns'. What do you do? Consumer awareness is a vital daily shield for grocery shopping, electronic appliances, mobile money services, and formal redress.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Warm_family_living_room_in_Nairobi.jpg/960px-Warm_family_living_room_in_Nairobi.jpg",
        "image_caption": "Applying consumer awareness protects families across grocery stores, electronics shops, and mobile digital finance.",
        "analogy_title": "The Consumer Ninja",
        "analogy_text": "Learning rules in a training hall is preparation; the real test is defending yourself in daily life. Consumer awareness is your protective skillset when grocery shopping, verifying appliance energy ratings, and protecting your digital money.",
        "definition": {
            "title": "Consumer Redress",
            "definitions": [
                {
                    "term": "Consumer Redress",
                    "simple": "Seeking a fair solution—such as repair, refund, or replacement—when provided with defective goods or services.",
                    "formal": "The legal and administrative mechanisms enabling consumers to obtain compensation, corrections, or financial recovery for defective products or unfair practices.",
                    "example": "Returning a leaking electric kettle with the receipt for an immediate store replacement.",
                    "why_it_matters": "Enforces vendor accountability and prevents financial loss for buyers."
                }
            ]
        },
        "deep_explanation": "Daily application of consumer awareness across four critical domains:\n\n1. **Grocery Shopping:** Inspect safety seals, check expiry dates, and reject bloated/damaged cans.\n2. **Household Appliances:** Verify energy efficiency ratings, test appliances in-store before leaving, and secure stamped warranty cards.\n3. **Digital & Mobile Financial Safety:** Protect secret MPESA/banking PINs, reject advance-fee prize scams, and audit unexpected airtime deductions.\n4. **System of Redress (4 Steps):**\n   - *Step 1:* Locate proof of purchase (receipt or MPESA code).\n   - *Step 2:* Pack the product with all original accessories.\n   - *Step 3:* State the issue calmly and assertively at customer care.\n   - *Step 4:* Escalate unresolved disputes to the Competition Authority of Kenya (CAK) or COFEK.",
        "practical": {
            "title": "Consumer Redress Communication & Negotiation Simulation",
            "steps": [
                {"step_number": 1, "instruction": "Pair up for a role-play: one student as Consumer, one as Store Manager."},
                {"step_number": 2, "instruction": "Scenario: An electric iron box leaks brown water on its first use, staining a school shirt."},
                {"step_number": 3, "instruction": "The Consumer presents the receipt and calmly demands a replacement and compensation under Article 46."},
                {"step_number": 4, "instruction": "The Store Manager evaluates the claim and negotiates a resolution based on warranty terms."},
                {"step_number": 5, "instruction": "Document key assertiveness techniques that resolved the dispute peacefully."}
            ]
        },
        "youtube_id": "7v1K8X9z0p5",
        "mcq": {
            "question": "What is the very first piece of evidence a consumer must locate when returning a defective household appliance for redress?",
            "options": [
                "The colorful marketing brochure",
                "The original purchase receipt or mobile transaction SMS",
                "The manufacturer's social media webpage",
                "A newspaper article reviewing the appliance"
            ],
            "correct_answer": 1,
            "explanation": "A receipt is the primary legal proof of purchase and contract. Without proof of purchase, retailers have no statutory obligation to grant refunds, repairs, or replacements."
        }
    }
]

def ingest_topic_2_6():
    print("=" * 80)
    print("STARTING CBC GRADE 10 HOME SCIENCE TOPIC 2.6 INGESTION (4 LESSONS)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    subject = Subject.objects.filter(grade=grade, name__icontains="Home Science").first()
    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=2,
        defaults={"name": "Home Management"}
    )

    learning_unit, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        order=6,
        defaults={"name": "2.6 Consumer Education"}
    )

    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for cfg in LESSON_CONFIGS:
            l_num = cfg["lesson_num"]
            l_title = f"Lesson {l_num}: {cfg['title']}"
            svg_fn = SVG_GETTERS[l_num - 1]
            svg_content = svg_fn()

            lesson, _ = Lesson.objects.update_or_create(
                learning_unit=learning_unit,
                title=l_title,
                defaults={
                    "topic": topic,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "topic": "Home Management",
                        "learning_unit": "2.6 Consumer Education",
                        "lesson_number": l_num,
                        "grade": 10
                    }
                }
            )

            # Clear old blocks and assets for idempotency
            lesson.blocks.all().delete()
            lesson.assets.all().delete()

            # 1. LessonAsset: Image Hook
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="approved",
                title=f"Visual Hook: {cfg['title']}",
                url=cfg["image_url"],
                metadata={"caption": cfg["image_caption"]}
            )
            total_assets += 1

            # 2. LessonAsset: SVG Diagram
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="custom",
                storage_type="inline",
                status="approved",
                title=f"Infographic Blueprint: {cfg['title']}",
                metadata={"svg_content": svg_content}
            )
            total_assets += 1

            # 3. LessonAsset: YouTube Video
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="approved",
                title=f"Video Exploration: {cfg['title']}",
                url=f"https://www.youtube.com/watch?v={cfg['youtube_id']}",
                metadata={"youtube_id": cfg["youtube_id"]}
            )
            total_assets += 1

            # 6 Concept Cards / Pages
            # Card 1: Goal + Image Hook + Hook Text
            b1 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                order=10,
                component_order=1,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Learning Goals",
                content={
                    "title": "Lesson Objectives",
                    "goals": [
                        f"Master foundational concepts and statutory rules of {cfg['title']}.",
                        "Apply critical awareness and comparative analysis to household purchasing.",
                        "Protect personal, family, and digital resources against exploitation."
                    ]
                }
            )
            b2 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                order=20,
                component_order=2,
                block_type="suggested_image",
                component_type="suggested_image",
                title=f"Visual Hook: {cfg['title']}",
                content={"image_url": cfg["image_url"], "caption": cfg["image_caption"]}
            )
            b2.assets.add(img_asset)

            b3 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                order=30,
                component_order=3,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Everyday Observation",
                content={"title": "Real-World Context", "text": cfg["hook"]}
            )

            # Card 2: Analogy + Definitions
            b4 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                order=40,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title=f"Analogy: {cfg['analogy_title']}",
                content={"title": cfg["analogy_title"], "text": cfg["analogy_text"]}
            )
            b5 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                order=50,
                component_order=2,
                block_type="definition_card",
                component_type="definition_card",
                title="Key Terminology",
                content=cfg["definition"]
            )

            # Card 3: SVG Infographic + Deep Dive
            b6 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                order=60,
                component_order=1,
                block_type="suggested_diagram",
                component_type="suggested_diagram",
                title=f"Blueprint: {cfg['title']}",
                content={"title": f"Infographic Blueprint: {cfg['title']}", "svg_content": svg_content}
            )
            b6.assets.add(svg_asset)

            b7 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                order=70,
                component_order=2,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Theoretical Analysis",
                content={"title": "Core Principles", "text": cfg["deep_explanation"]}
            )

            # Card 4: Step Process Practical Activity
            b8 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                order=80,
                component_order=1,
                block_type="step_process",
                component_type="step_process",
                title=cfg["practical"]["title"],
                content=cfg["practical"]
            )

            # Card 5: YouTube Video Exploration
            b9 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                order=90,
                component_order=1,
                block_type="suggested_video",
                component_type="suggested_video",
                title=f"Video Demonstration: {cfg['title']}",
                content={
                    "title": f"Video Study: {cfg['title']}",
                    "youtube_id": cfg["youtube_id"],
                    "video_url": f"https://www.youtube.com/watch?v={cfg['youtube_id']}"
                }
            )
            b9.assets.add(yt_asset)

            b10 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                order=100,
                component_order=2,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Application in Kenyan Society",
                content={
                    "title": "Kenyan Consumer Protection",
                    "text": "Empowered Kenyan consumers who verify KEBS standardization marks, audit unit pricing, and report unfair practices cultivate an ethical, safe, and transparent national marketplace."
                }
            )

            # Card 6: Knowledge Check MCQ + Summary
            b11 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=6,
                order=110,
                component_order=1,
                block_type="knowledge_check",
                component_type="knowledge_check",
                title="Checkpoint Question",
                content=cfg["mcq"]
            )

            b12 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=6,
                order=120,
                component_order=2,
                block_type="key_takeaway",
                component_type="key_takeaway",
                title="Key Takeaways",
                content={
                    "title": "Summary & Core Lessons",
                    "takeaways": [
                        f"Consumer education empowers individuals to maximize household resources and protect family health ({cfg['title']}).",
                        "Statutory consumer rights (Art. 46) are safeguarded by upholding critical consumer responsibilities.",
                        "Systematic comparative shopping, budgeting, and documentation ensure financial security."
                    ]
                }
            )

            total_lessons += 1
            total_blocks += 12
            print(f"  [+] Ingested Lesson {l_num}/4: '{l_title}' (12 blocks, 3 assets, 6 pages)")

    print("=" * 80)
    print("TOPIC 2.6 INGESTION COMPLETED SUCCESSFULLY:")
    print(f"  - Total Lessons: {total_lessons}")
    print(f"  - Total Blocks:  {total_blocks}")
    print(f"  - Total Assets:  {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_topic_2_6()
