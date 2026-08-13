import os
import sys
import django
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db.models import Max
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Form 4 Topic 4: First Half (13 Lessons) ===")

def get_or_create_diagram_block(lesson, page_number, title, component_order=1):
    existing = LessonBlock.objects.filter(
        lesson=lesson, page_number=page_number, block_type='suggested_diagram'
    ).first()
    if existing:
        existing.title = title
        existing.save()
        return existing
    
    max_order = LessonBlock.objects.filter(lesson=lesson).aggregate(m=Max('order'))['m'] or 0
    block = LessonBlock.objects.create(
        lesson=lesson,
        block_id=f"enrich_{lesson.id}_p{page_number}_{uuid4().hex[:6]}",
        block_type='suggested_diagram',
        component_type='suggested_diagram',
        page_number=page_number,
        order=max_order + 1,
        component_order=component_order,
        title=title,
        content={'text': title}
    )
    return block


# =========================================================================
# 1. LESSON 77: Redox Reactions (LU Order 1)
# =========================================================================
l77 = Lesson.objects.get(id=77)
print(f"\nProcessing Lesson 77: {l77.title}")

b77_p2 = get_or_create_diagram_block(l77, 2, "Oxidized and Corroded Iron Nails Demonstrating Spontaneous Electron Loss")
a77_p2, _ = LessonAsset.objects.get_or_create(id=352, defaults={'lesson': l77, 'asset_type': 'image'})
a77_p2.lesson = l77
a77_p2.asset_type = 'image'
a77_p2.source_type = 'external'
a77_p2.storage_type = 'url'
a77_p2.status = 'attached'
a77_p2.title = "Oxidized and Corroded Iron Nails Demonstrating Spontaneous Electron Loss"
a77_p2.description = "Photograph of corroded iron nails showing rust formation resulting from the loss of electrons by metallic iron (Fe -> Fe2+ + 2e-)."
a77_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/%22Swelling%22_of_Iron_nails_due_to_rusting.jpg/800px-%22Swelling%22_of_Iron_nails_due_to_rusting.jpg"
a77_p2.metadata = {
    'author': 'Dr._Sroy',
    'licensing': 'CC BY 4.0',
    'attribution': 'Dr._Sroy / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:%22Swelling%22_of_Iron_nails_due_to_rusting.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Oxidation electron loss'
}
a77_p2.save()
a77_p2.blocks.set([b77_p2])
print("Lesson 77 Page 2: Asset 352 attached.")

b77_p3 = get_or_create_diagram_block(l77, 3, "Vigorous Oxidation of Metallic Magnesium Ribbon in Air")
a77_p3, _ = LessonAsset.objects.get_or_create(id=353, defaults={'lesson': l77, 'asset_type': 'image'})
a77_p3.lesson = l77
a77_p3.asset_type = 'image'
a77_p3.source_type = 'external'
a77_p3.storage_type = 'url'
a77_p3.status = 'attached'
a77_p3.title = "Vigorous Oxidation of Metallic Magnesium Ribbon in Air"
a77_p3.description = "Photograph of magnesium burning brilliantly as magnesium atoms lose electrons to reduce atmospheric oxygen into oxide ions."
a77_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Magnesium_ribbon_burning.jpg/800px-Magnesium_ribbon_burning.jpg"
a77_p3.metadata = {
    'author': 'Capt. John Yossarian',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Capt. John Yossarian / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Magnesium_ribbon_burning.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Redox electron transfer'
}
a77_p3.save()
a77_p3.blocks.set([b77_p3])
print("Lesson 77 Page 3: Asset 353 attached.")

svg_77_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="eArr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24"/>
    </marker>
  </defs>
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ELECTRON TRANSFER MODEL OF REDOX REACTIONS (OIL RIG)</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Oxidation Is Loss of Electrons (OIL) | Reduction Is Gain of Electrons (RIG)</text>
  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="720" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <g transform="translate(40, 30)">
      <rect x="0" y="0" width="280" height="275" rx="10" fill="#020617" stroke="#ef4444" stroke-width="2"/>
      <text x="140" y="30" text-anchor="middle" fill="#f87171" font-size="13" font-weight="bold">OXIDATION HALF-REACTION</text>
      <text x="140" y="50" text-anchor="middle" fill="#fca5a5" font-size="11">Reducing Agent: Zinc Metal (Zn)</text>
      <rect x="80" y="70" width="120" height="70" rx="8" fill="#334155" stroke="#94a3b8"/>
      <text x="140" y="105" text-anchor="middle" fill="#f8fafc" font-size="14" font-weight="bold">Zn(s)</text>
      <text x="140" y="122" text-anchor="middle" fill="#94a3b8" font-size="10">Oxidation State: 0</text>
      <rect x="20" y="165" width="240" height="90" rx="6" fill="#1e293b"/>
      <text x="140" y="190" text-anchor="middle" fill="#f87171" font-size="11" font-family="monospace" font-weight="bold">Zn(s) → Zn²⁺(aq) + 2e⁻</text>
      <text x="140" y="215" text-anchor="middle" fill="#cbd5e1" font-size="10">• Loses 2 electrons</text>
      <text x="140" y="235" text-anchor="middle" fill="#fbbf24" font-size="10">• Oxidation number increases (0 → +2)</text>
    </g>
    <path d="M 325 120 C 360 80 360 80 395 120" fill="none" stroke="#fbbf24" stroke-width="4" stroke-dasharray="4" marker-end="url(#eArr)"/>
    <text x="360" y="70" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">Transfer of 2e⁻</text>
    <g transform="translate(400, 30)">
      <rect x="0" y="0" width="280" height="275" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
      <text x="140" y="30" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">REDUCTION HALF-REACTION</text>
      <text x="140" y="50" text-anchor="middle" fill="#7dd3fc" font-size="11">Oxidizing Agent: Copper(II) Ions (Cu²⁺)</text>
      <rect x="80" y="70" width="120" height="70" rx="8" fill="#1e3a8a" stroke="#38bdf8"/>
      <text x="140" y="105" text-anchor="middle" fill="#f8fafc" font-size="14" font-weight="bold">Cu²⁺(aq)</text>
      <text x="140" y="122" text-anchor="middle" fill="#93c5fd" font-size="10">Oxidation State: +2</text>
      <rect x="20" y="165" width="240" height="90" rx="6" fill="#1e293b"/>
      <text x="140" y="190" text-anchor="middle" fill="#38bdf8" font-size="11" font-family="monospace" font-weight="bold">Cu²⁺(aq) + 2e⁻ → Cu(s)</text>
      <text x="140" y="215" text-anchor="middle" fill="#cbd5e1" font-size="10">• Gains 2 electrons</text>
      <text x="140" y="235" text-anchor="middle" fill="#34d399" font-size="10">• Oxidation number decreases (+2 → 0)</text>
    </g>
  </g>
</svg>'''
b77_p4 = get_or_create_diagram_block(l77, 4, "Redox Electron Transfer Model: Zinc Oxidation and Copper Ion Reduction")
a77_p4, _ = LessonAsset.objects.get_or_create(id=354, defaults={'lesson': l77, 'asset_type': 'diagram'})
a77_p4.lesson = l77
a77_p4.asset_type = 'diagram'
a77_p4.source_type = 'ai_generated'
a77_p4.storage_type = 'file'
a77_p4.status = 'attached'
a77_p4.title = "Redox Electron Transfer Model: Zinc Oxidation and Copper Ion Reduction"
a77_p4.description = "Diagram illustrating electron transfer between zinc metal and copper(II) ions in a spontaneous redox displacement reaction."
a77_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_77_p4)
a77_p4.file.save(f'redox_electron_transfer_{l77.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a77_p4.blocks.set([b77_p4])
print("Lesson 77 Page 4: Asset 354 saved and attached.")


# =========================================================================
# 2. LESSON 78: Oxidation Numbers (LU Order 2)
# =========================================================================
l78 = Lesson.objects.get(id=78)
print(f"\nProcessing Lesson 78: {l78.title}")

b78_p2 = get_or_create_diagram_block(l78, 2, "Deep Purple Potassium Permanganate (KMnO4) Solution with Manganese in (+7) State")
a78_p2, _ = LessonAsset.objects.get_or_create(id=355, defaults={'lesson': l78, 'asset_type': 'image'})
a78_p2.lesson = l78
a78_p2.asset_type = 'image'
a78_p2.source_type = 'external'
a78_p2.storage_type = 'url'
a78_p2.status = 'attached'
a78_p2.title = "Deep Purple Potassium Permanganate (KMnO4) Solution with Manganese in (+7) State"
a78_p2.description = "Photograph of deep purple potassium permanganate solution illustrating the maximum +7 oxidation state of manganese in oxoanions."
a78_p2.url = "https://upload.wikimedia.org/wikipedia/commons/8/8b/A_solution_of_Potassium_Permanganate_being_poured_into_a_well_in_an_Indian_village_to_disinfect_its_water.jpg"
a78_p2.metadata = {
    'author': 'Government of India',
    'licensing': 'Public domain',
    'attribution': 'Photo Division, Ministry of Information / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_solution_of_Potassium_Permanganate_being_poured_into_a_well_in_an_Indian_village_to_disinfect_its_water.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'High oxidation state in transition metals'
}
a78_p2.save()
a78_p2.blocks.set([b78_p2])
print("Lesson 78 Page 2: Asset 355 attached.")

b78_p3 = get_or_create_diagram_block(l78, 3, "Transition Metal Solution Color Array Exhibiting Variable Oxidation States")
a78_p3, _ = LessonAsset.objects.get_or_create(id=356, defaults={'lesson': l78, 'asset_type': 'image'})
a78_p3.lesson = l78
a78_p3.asset_type = 'image'
a78_p3.source_type = 'external'
a78_p3.storage_type = 'url'
a78_p3.status = 'attached'
a78_p3.title = "Transition Metal Solution Color Array Exhibiting Variable Oxidation States"
a78_p3.description = "Photograph showing aqueous transition metal solutions whose distinct colors correspond to different oxidation numbers (e.g. green Fe2+, yellow Fe3+, purple MnO4-)."
a78_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Coloured-transition-metal-solutions.jpg/800px-Coloured-transition-metal-solutions.jpg"
a78_p3.metadata = {
    'author': 'Benjah-bmm27',
    'licensing': 'Public domain',
    'attribution': 'Benjah-bmm27 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Coloured-transition-metal-solutions.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Variable transition metal oxidation numbers'
}
a78_p3.save()
a78_p3.blocks.set([b78_p3])
print("Lesson 78 Page 3: Asset 356 attached.")

svg_78_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">OXIDATION NUMBER SPECTRUM OF TRANSITION METALS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Tracking Electron Loss Across Variable Oxidation States (e.g., Manganese from +7 to 0)</text>
  <g transform="translate(50, 80)">
    <rect x="0" y="0" width="720" height="330" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <g transform="translate(30, 30)">
      <!-- Number line -->
      <line x1="20" y1="90" x2="640" y2="90" stroke="#94a3b8" stroke-width="3"/>
      
      <!-- Nodes -->
      <!-- +7 -->
      <circle cx="50" cy="90" r="22" fill="#7e22ce" stroke="#c084fc" stroke-width="2"/>
      <text x="50" y="96" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">+7</text>
      <text x="50" y="135" text-anchor="middle" fill="#c084fc" font-size="11" font-weight="bold">MnO₄⁻</text>
      <text x="50" y="152" text-anchor="middle" fill="#cbd5e1" font-size="9">Permanganate (Purple)</text>

      <!-- +6 -->
      <circle cx="170" cy="90" r="20" fill="#047857" stroke="#34d399" stroke-width="2"/>
      <text x="170" y="96" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">+6</text>
      <text x="170" y="135" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">MnO₄²⁻</text>
      <text x="170" y="152" text-anchor="middle" fill="#cbd5e1" font-size="9">Manganate (Green)</text>

      <!-- +4 -->
      <circle cx="290" cy="90" r="20" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
      <text x="290" y="96" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">+4</text>
      <text x="290" y="135" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">MnO₂</text>
      <text x="290" y="152" text-anchor="middle" fill="#cbd5e1" font-size="9">Dioxide (Black Solid)</text>

      <!-- +2 -->
      <circle cx="410" cy="90" r="20" fill="#ec4899" stroke="#f472b6" stroke-width="2"/>
      <text x="410" y="96" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">+2</text>
      <text x="410" y="135" text-anchor="middle" fill="#f472b6" font-size="11" font-weight="bold">Mn²⁺</text>
      <text x="410" y="152" text-anchor="middle" fill="#cbd5e1" font-size="9">Manganese(II) (Pale Pink)</text>

      <!-- 0 -->
      <circle cx="530" cy="90" r="20" fill="#475569" stroke="#cbd5e1" stroke-width="2"/>
      <text x="530" y="96" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">0</text>
      <text x="530" y="135" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="bold">Mn(s)</text>
      <text x="530" y="152" text-anchor="middle" fill="#cbd5e1" font-size="9">Pure Metal (Grey)</text>
    </g>
    <rect x="30" y="210" width="660" height="95" rx="8" fill="#020617" stroke="#38bdf8"/>
    <text x="50" y="235" fill="#38bdf8" font-size="11" font-weight="bold">Rules of Notation:</text>
    <text x="50" y="258" fill="#cbd5e1" font-size="10">• Oxidation number is written as SIGN FIRST (+2, -1), while ionic charge is number first (2+, 1-).</text>
    <text x="50" y="278" fill="#fbbf24" font-size="10">• Increase in Oxidation Number = OXIDATION (e.g. Fe²⁺ → Fe³⁺).</text>
    <text x="50" y="296" fill="#4ade80" font-size="10">• Decrease in Oxidation Number = REDUCTION (e.g. MnO₄⁻ → Mn²⁺).</text>
  </g>
</svg>'''
b78_p4 = get_or_create_diagram_block(l78, 4, "Variable Oxidation States of Transition Metals and Color Hierarchy")
a78_p4, _ = LessonAsset.objects.get_or_create(id=357, defaults={'lesson': l78, 'asset_type': 'diagram'})
a78_p4.lesson = l78
a78_p4.asset_type = 'diagram'
a78_p4.source_type = 'ai_generated'
a78_p4.storage_type = 'file'
a78_p4.status = 'attached'
a78_p4.title = "Variable Oxidation States of Transition Metals and Color Hierarchy"
a78_p4.description = "Visual oxidation state scale of manganese compounds illustrating distinct colors corresponding to oxidation numbers from +7 down to 0."
a78_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_78_p4)
a78_p4.file.save(f'oxidation_states_manganese_{l78.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a78_p4.blocks.set([b78_p4])
print("Lesson 78 Page 4: Asset 357 saved and attached.")


# =========================================================================
# 3. LESSON 79: Rules of Assigning Oxidation Numbers (LU Order 3)
# =========================================================================
l79 = Lesson.objects.get(id=79)
print(f"\nProcessing Lesson 79: {l79.title}")

b79_p2 = get_or_create_diagram_block(l79, 2, "Pure Metallic Zinc Plated Surface with Oxidation State of Zero (0)")
a79_p2, _ = LessonAsset.objects.get_or_create(id=358, defaults={'lesson': l79, 'asset_type': 'image'})
a79_p2.lesson = l79
a79_p2.asset_type = 'image'
a79_p2.source_type = 'external'
a79_p2.storage_type = 'url'
a79_p2.status = 'attached'
a79_p2.title = "Pure Metallic Zinc Plated Surface with Oxidation State of Zero (0)"
a79_p2.description = "Photograph of pure elemental metallic zinc illustrating Rule 1: All uncombined free elements have an oxidation number of 0."
a79_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/A_zinc-plated_surface_for_the_protection_from_corrosion.jpg/800px-A_zinc-plated_surface_for_the_protection_from_corrosion.jpg"
a79_p2.metadata = {
    'author': 'Hi-Res Images of Chemical Elements',
    'licensing': 'CC BY 3.0',
    'attribution': 'Hi-Res Images of Chemical Elements / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_zinc-plated_surface_for_the_protection_from_corrosion.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Zero oxidation state in uncombined elements'
}
a79_p2.save()
a79_p2.blocks.set([b79_p2])
print("Lesson 79 Page 2: Asset 358 attached.")

b79_p3 = get_or_create_diagram_block(l79, 3, "Crystalline Solid Reagent Demonstrating Neutral Charge Summation Rule")
a79_p3, _ = LessonAsset.objects.get_or_create(id=359, defaults={'lesson': l79, 'asset_type': 'image'})
a79_p3.lesson = l79
a79_p3.asset_type = 'image'
a79_p3.source_type = 'external'
a79_p3.storage_type = 'url'
a79_p3.status = 'attached'
a79_p3.title = "Crystalline Solid Reagent Demonstrating Neutral Charge Summation Rule"
a79_p3.description = "Photograph of sodium chloride crystals illustrating Rule 2: In neutral compounds, the sum of all oxidation numbers equals zero (+1 for Na, -1 for Cl)."
a79_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Crystals_Halite_on_matrix.jpg/800px-Crystals_Halite_on_matrix.jpg"
a79_p3.metadata = {
    'author': 'IvanSakhno',
    'licensing': 'CC BY 4.0',
    'attribution': 'IvanSakhno / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Crystals_Halite_on_matrix.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Neutral compound oxidation summation'
}
a79_p3.save()
a79_p3.blocks.set([b79_p3])
print("Lesson 79 Page 3: Asset 359 attached.")

svg_79_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SYSTEMATIC RULES FOR ASSIGNING OXIDATION NUMBERS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Mastering the 5 Standard Rules Governed by Electronegativity and Charge Conservation</text>
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="730" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <g transform="translate(20, 20)">
      <!-- Rule 1 -->
      <rect x="0" y="0" width="335" height="85" rx="8" fill="#020617" stroke="#38bdf8"/>
      <text x="15" y="25" fill="#38bdf8" font-size="11" font-weight="bold">RULE 1: FREE UNCOMBINED ELEMENTS</text>
      <text x="15" y="48" fill="#cbd5e1" font-size="10">Oxidation state is ALWAYS 0.</text>
      <text x="15" y="68" fill="#4ade80" font-size="10" font-family="monospace">Examples: Na, Mg, H₂, O₂, Cl₂, S₈, P₄ = 0</text>

      <!-- Rule 2 -->
      <rect x="355" y="0" width="335" height="85" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="370" y="25" fill="#34d399" font-size="11" font-weight="bold">RULE 2: SIMPLE MONATOMIC IONS</text>
      <text x="370" y="48" fill="#cbd5e1" font-size="10">Oxidation state = Charge on the ion.</text>
      <text x="370" y="68" fill="#4ade80" font-size="10" font-family="monospace">Examples: Na⁺ (+1), Mg²⁺ (+2), Al³⁺ (+3), Cl⁻ (-1)</text>

      <!-- Rule 3 -->
      <rect x="0" y="100" width="335" height="90" rx="8" fill="#020617" stroke="#fbbf24"/>
      <text x="15" y="125" fill="#fbbf24" font-size="11" font-weight="bold">RULE 3: HYDROGEN &amp; OXYGEN</text>
      <text x="15" y="148" fill="#cbd5e1" font-size="10">• Hydrogen = +1 (except in metal hydrides NaH = -1)</text>
      <text x="15" y="168" fill="#cbd5e1" font-size="10">• Oxygen = -2 (except in peroxides H₂O₂ = -1, OF₂ = +2)</text>

      <!-- Rule 4 & 5 -->
      <rect x="355" y="100" width="335" height="90" rx="8" fill="#020617" stroke="#a855f7"/>
      <text x="370" y="125" fill="#c084fc" font-size="11" font-weight="bold">RULE 4 &amp; 5: COMPOUNDS &amp; POLYATOMIC IONS</text>
      <text x="370" y="148" fill="#cbd5e1" font-size="10">• Neutral Compound: Sum (Σ) = 0 (e.g. H₂SO₄ = 0)</text>
      <text x="370" y="168" fill="#cbd5e1" font-size="10">• Polyatomic Ion: Sum (Σ) = Ion charge (SO₄²⁻ = -2)</text>
    </g>
    <!-- Calculation Example Bar -->
    <rect x="20" y="225" width="690" height="90" rx="8" fill="#020617" stroke="#38bdf8"/>
    <text x="35" y="248" fill="#38bdf8" font-size="11" font-weight="bold">Worked Example: Determining Oxidation Number of Sulfur in SO₄²⁻</text>
    <text x="35" y="270" fill="#f8fafc" font-size="10" font-family="monospace">Equation: [S] + 4(-2) = -2  ⟹  [S] - 8 = -2  ⟹  [S] = +6</text>
    <text x="35" y="295" fill="#4ade80" font-size="10" font-weight="bold">Result: Sulfur is in the +6 oxidation state in the sulfate ion.</text>
  </g>
</svg>'''
b79_p4 = get_or_create_diagram_block(l79, 4, "Decision Tree and Calculation Rules for Determining Oxidation Numbers")
a79_p4, _ = LessonAsset.objects.get_or_create(id=360, defaults={'lesson': l79, 'asset_type': 'diagram'})
a79_p4.lesson = l79
a79_p4.asset_type = 'diagram'
a79_p4.source_type = 'ai_generated'
a79_p4.storage_type = 'file'
a79_p4.status = 'attached'
a79_p4.title = "Decision Tree and Calculation Rules for Determining Oxidation Numbers"
a79_p4.description = "Summary rules and worked algebraic method for calculating unknown oxidation numbers in neutral compounds and complex polyatomic ions."
a79_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_79_p4)
a79_p4.file.save(f'rules_oxidation_numbers_{l79.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a79_p4.blocks.set([b79_p4])
print("Lesson 79 Page 4: Asset 360 saved and attached.")


# =========================================================================
# 4. LESSON 80: Other Examples of Redox Reactions (LU Order 4)
# =========================================================================
l80 = Lesson.objects.get(id=80)
print(f"\nProcessing Lesson 80: {l80.title}")

b80_p2 = get_or_create_diagram_block(l80, 2, "Crystalline Elemental Sulfur Specimen Used in Bleaching and Combustion Redox Reactions")
a80_p2, _ = LessonAsset.objects.get_or_create(id=361, defaults={'lesson': l80, 'asset_type': 'image'})
a80_p2.lesson = l80
a80_p2.asset_type = 'image'
a80_p2.source_type = 'external'
a80_p2.storage_type = 'url'
a80_p2.status = 'attached'
a80_p2.title = "Crystalline Elemental Sulfur Specimen Used in Bleaching and Combustion Redox Reactions"
a80_p2.description = "Photograph of natural yellow sulfur crystals that burn to form sulfur dioxide (SO2), a key reducing and bleaching agent."
a80_p2.url = "https://upload.wikimedia.org/wikipedia/commons/2/2d/Celestine-Sulfur-j08-12a.jpg"
a80_p2.metadata = {
    'author': 'Robert M. Lavinsky',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Robert M. Lavinsky / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Celestine-Sulfur-j08-12a.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Sulfur redox chemistry'
}
a80_p2.save()
a80_p2.blocks.set([b80_p2])
print("Lesson 80 Page 2: Asset 361 attached.")

b80_p3 = get_or_create_diagram_block(l80, 3, "Commercial Concentrated Acid Battery Fluid Reagent")
a80_p3, _ = LessonAsset.objects.get_or_create(id=362, defaults={'lesson': l80, 'asset_type': 'image'})
a80_p3.lesson = l80
a80_p3.asset_type = 'image'
a80_p3.source_type = 'external'
a80_p3.storage_type = 'url'
a80_p3.status = 'attached'
a80_p3.title = "Commercial Concentrated Acid Battery Fluid Reagent"
a80_p3.description = "Photograph of commercial sulfuric acid used in redox accumulator systems and industrial acid-redox reactions."
a80_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Battery_fluid%2C_plastic_bottle.jpg/800px-Battery_fluid%2C_plastic_bottle.jpg"
a80_p3.metadata = {
    'author': 'Cjp24',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Cjp24 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Battery_fluid,_plastic_bottle.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Industrial redox reagent'
}
a80_p3.save()
a80_p3.blocks.set([b80_p3])
print("Lesson 80 Page 3: Asset 362 attached.")

svg_80_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">COMPARATIVE REDOX BLEACHING MECHANISMS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Permanent Bleaching by Oxidation (Chlorine Water) vs. Temporary Bleaching by Reduction (Sulfur Dioxide)</text>
  <g transform="translate(45, 75)">
    <!-- Chlorine Bleaching -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="172" y="30" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">1. BLEACHING BY OXIDATION (Cl₂ WATER)</text>
      <rect x="15" y="55" width="315" height="65" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="172" y="80" text-anchor="middle" fill="#f8fafc" font-size="10" font-family="monospace">Cl₂(aq) + H₂O(l) ⇌ HOCl(aq) + HCl(aq)</text>
      <text x="172" y="102" text-anchor="middle" fill="#4ade80" font-size="10" font-family="monospace">Dye + HOCl → (Dye + [O]) + HCl</text>
      <rect x="15" y="135" width="315" height="180" rx="8" fill="#020617"/>
      <text x="25" y="160" fill="#34d399" font-size="11" font-weight="bold">• Active Agent: Chloric(I) acid (HOCl)</text>
      <text x="25" y="185" fill="#cbd5e1" font-size="10">• Releases nascent oxygen [O] to oxidize dye</text>
      <text x="25" y="210" fill="#cbd5e1" font-size="10">• Dye loses color permanently</text>
      <text x="25" y="240" fill="#38bdf8" font-size="11" font-weight="bold">Key Exam Property:</text>
      <text x="25" y="265" fill="#4ade80" font-size="10" font-weight="bold">PERMANENT: Exposure to air does NOT restore color</text>
      <text x="25" y="290" fill="#94a3b8" font-size="9">(Cannot be reversed by atmospheric oxygen)</text>
    </g>
    <!-- SO2 Bleaching -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="172" y="30" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">2. BLEACHING BY REDUCTION (SO₂ GAS)</text>
      <rect x="15" y="55" width="315" height="65" rx="8" fill="#020617" stroke="#f59e0b"/>
      <text x="172" y="80" text-anchor="middle" fill="#f8fafc" font-size="10" font-family="monospace">SO₂(g) + 2H₂O(l) ⇌ H₂SO₄(aq) + 2[H]</text>
      <text x="172" y="102" text-anchor="middle" fill="#fde68a" font-size="10" font-family="monospace">Colored Dye + 2[H] → Colorless Reduced Dye</text>
      <rect x="15" y="135" width="315" height="180" rx="8" fill="#020617"/>
      <text x="25" y="160" fill="#fbbf24" font-size="11" font-weight="bold">• Active Agent: Nascent hydrogen [H]</text>
      <text x="25" y="185" fill="#cbd5e1" font-size="10">• Removes oxygen from dye (Reduction)</text>
      <text x="25" y="210" fill="#cbd5e1" font-size="10">• Used for delicate fabrics (wool, silk, straw)</text>
      <text x="25" y="240" fill="#f87171" font-size="11" font-weight="bold">Key Exam Property:</text>
      <text x="25" y="265" fill="#f87171" font-size="10" font-weight="bold">TEMPORARY: Exposure to air RESTORES color</text>
      <text x="25" y="290" fill="#94a3b8" font-size="9">(Atmospheric oxygen re-oxidizes the reduced dye)</text>
    </g>
  </g>
</svg>'''
b80_p4 = get_or_create_diagram_block(l80, 4, "Comparative Mechanisms of Bleaching: Oxidation by Chlorine vs. Reduction by Sulfur Dioxide")
a80_p4, _ = LessonAsset.objects.get_or_create(id=363, defaults={'lesson': l80, 'asset_type': 'diagram'})
a80_p4.lesson = l80
a80_p4.asset_type = 'diagram'
a80_p4.source_type = 'ai_generated'
a80_p4.storage_type = 'file'
a80_p4.status = 'attached'
a80_p4.title = "Comparative Mechanisms of Bleaching: Oxidation by Chlorine vs. Reduction by Sulfur Dioxide"
a80_p4.description = "Side-by-side comparison diagram contrasting permanent bleaching by oxidation (chlorine water) with temporary bleaching by reduction (sulfur dioxide)."
a80_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_80_p4)
a80_p4.file.save(f'bleaching_mechanisms_{l80.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a80_p4.blocks.set([b80_p4])
print("Lesson 80 Page 4: Asset 363 saved and attached.")


# =========================================================================
# 5. LESSON 81: Electrochemical Cell (LU Order 5)
# =========================================================================
l81 = Lesson.objects.get(id=81)
print(f"\nProcessing Lesson 81: {l81.title}")

b81_p2 = get_or_create_diagram_block(l81, 2, "Historical Zinc-Copper Daniell Electrochemical Cell Apparatus")
a81_p2, _ = LessonAsset.objects.get_or_create(id=364, defaults={'lesson': l81, 'asset_type': 'image'})
a81_p2.lesson = l81
a81_p2.asset_type = 'image'
a81_p2.source_type = 'external'
a81_p2.storage_type = 'url'
a81_p2.status = 'attached'
a81_p2.title = "Historical Zinc-Copper Daniell Electrochemical Cell Apparatus"
a81_p2.description = "Photograph of a classic Daniell electrochemical cell showing the porous pot separator, zinc electrode, and copper outer vessel."
a81_p2.url = "https://upload.wikimedia.org/wikipedia/commons/3/34/Daniell_cell.jpg"
a81_p2.metadata = {
    'author': 'Unknown',
    'licensing': 'Public domain',
    'attribution': 'Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Daniell_cell.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Daniell electrochemical cell apparatus'
}
a81_p2.save()
a81_p2.blocks.set([b81_p2])
print("Lesson 81 Page 2: Asset 364 attached.")

b81_p3 = get_or_create_diagram_block(l81, 3, "Precision Digital Multimeter Measuring DC Cell Potential Voltage")
a81_p3, _ = LessonAsset.objects.get_or_create(id=365, defaults={'lesson': l81, 'asset_type': 'image'})
a81_p3.lesson = l81
a81_p3.asset_type = 'image'
a81_p3.source_type = 'external'
a81_p3.storage_type = 'url'
a81_p3.status = 'attached'
a81_p3.title = "Precision Digital Multimeter Measuring DC Cell Potential Voltage"
a81_p3.description = "Photograph of a digital multimeter connected across an electrochemical circuit measuring voltage generated by spontaneous electron transfer."
a81_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg/800px-After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg"
a81_p3.metadata = {
    'author': 'Kmashaye5220',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Kmashaye5220 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:After_burning_up_the_circuit,_the_voltage_of_the_red_wires.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Cell potential measurement'
}
a81_p3.save()
a81_p3.blocks.set([b81_p3])
print("Lesson 81 Page 3: Asset 365 attached.")

svg_81_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="dArr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24"/>
    </marker>
  </defs>
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DANIELL VOLTAIC ELECTROCHEMICAL CELL (Zn/Zn²⁺ ∥ Cu²⁺/Cu)</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Chemical Energy Converted to Electrical Energy via Spontaneous Electron Flow (E°cell = +1.10 V)</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Voltmeter in top wire -->
    <path d="M 130 110 L 130 40 L 310 40" stroke="#fbbf24" stroke-width="3"/>
    <path d="M 390 40 L 570 40 L 570 110" stroke="#fbbf24" stroke-width="3"/>
    <circle cx="350" cy="40" r="30" fill="#020617" stroke="#fbbf24" stroke-width="2"/>
    <text x="350" y="38" text-anchor="middle" fill="#fbbf24" font-size="14" font-weight="bold">1.10 V</text>
    <text x="350" y="54" text-anchor="middle" fill="#94a3b8" font-size="8">Voltmeter</text>

    <!-- Electron Flow Arrow -->
    <path d="M 200 25 L 280 25" stroke="#fbbf24" stroke-width="2" marker-end="url(#dArr)"/>
    <text x="240" y="18" text-anchor="middle" fill="#fbbf24" font-size="9" font-weight="bold">Electron Flow (e⁻)</text>

    <!-- Left Beaker: Zinc Anode -->
    <g transform="translate(50, 110)">
      <rect x="0" y="40" width="160" height="150" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
      <rect x="5" y="80" width="150" height="105" fill="#38bdf8" fill-opacity="0.15"/>
      <rect x="65" y="0" width="30" height="150" rx="3" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="80" y="-10" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">ANODE (-)</text>
      <text x="80" y="15" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">Zinc (Zn)</text>
      <text x="80" y="210" text-anchor="middle" fill="#38bdf8" font-size="10">1.0 M ZnSO₄(aq)</text>
      <text x="80" y="228" text-anchor="middle" fill="#f87171" font-size="9" font-family="monospace">Zn → Zn²⁺ + 2e⁻</text>
    </g>

    <!-- Salt Bridge (U-tube) -->
    <path d="M 180 180 L 180 100 Q 180 80 210 80 L 490 80 Q 520 80 520 100 L 520 180" fill="none" stroke="#a855f7" stroke-width="18" stroke-linecap="round"/>
    <path d="M 180 180 L 180 100 Q 180 80 210 80 L 490 80 Q 520 80 520 100 L 520 180" fill="none" stroke="#c084fc" stroke-width="12" stroke-linecap="round"/>
    <text x="350" y="95" text-anchor="middle" fill="#020617" font-size="9" font-weight="bold">Salt Bridge (KNO₃ in Agar)</text>

    <!-- Right Beaker: Copper Cathode -->
    <g transform="translate(490, 110)">
      <rect x="0" y="40" width="160" height="150" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
      <rect x="5" y="80" width="150" height="105" fill="#0284c7" fill-opacity="0.3"/>
      <rect x="65" y="0" width="30" height="150" rx="3" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="80" y="-10" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">CATHODE (+)</text>
      <text x="80" y="15" text-anchor="middle" fill="#fde68a" font-size="10" font-weight="bold">Copper (Cu)</text>
      <text x="80" y="210" text-anchor="middle" fill="#38bdf8" font-size="10">1.0 M CuSO₄(aq)</text>
      <text x="80" y="228" text-anchor="middle" fill="#34d399" font-size="9" font-family="monospace">Cu²⁺ + 2e⁻ → Cu</text>
    </g>
  </g>
</svg>'''
b81_p4 = get_or_create_diagram_block(l81, 4, "Complete Daniell Electrochemical Cell Architecture and Operation")
a81_p4, _ = LessonAsset.objects.get_or_create(id=366, defaults={'lesson': l81, 'asset_type': 'diagram'})
a81_p4.lesson = l81
a81_p4.asset_type = 'diagram'
a81_p4.source_type = 'ai_generated'
a81_p4.storage_type = 'file'
a81_p4.status = 'attached'
a81_p4.title = "Complete Daniell Electrochemical Cell Architecture and Operation"
a81_p4.description = "Complete diagram of the Daniell voltaic cell showing zinc anode oxidation, copper cathode reduction, external electron circuit, and salt bridge ion flow."
a81_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_81_p4)
a81_p4.file.save(f'daniell_cell_architecture_{l81.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a81_p4.blocks.set([b81_p4])
print("Lesson 81 Page 4: Asset 366 saved and attached.")


# =========================================================================
# 6. LESSON 82: The Tendency of Metals to Form Ions (LU Order 6)
# =========================================================================
l82 = Lesson.objects.get(id=82)
print(f"\nProcessing Lesson 82: {l82.title}")

b82_p2 = get_or_create_diagram_block(l82, 2, "Industrial Zinc-Plated Metal Surface Demonstrating High Ionization Tendency")
a82_p2, _ = LessonAsset.objects.get_or_create(id=367, defaults={'lesson': l82, 'asset_type': 'image'})
a82_p2.lesson = l82
a82_p2.asset_type = 'image'
a82_p2.source_type = 'external'
a82_p2.storage_type = 'url'
a82_p2.status = 'attached'
a82_p2.title = "Industrial Zinc-Plated Metal Surface Demonstrating High Ionization Tendency"
a82_p2.description = "Photograph of zinc-coated steel showcasing zinc's strong tendency to ionize (lose electrons) ahead of iron to provide sacrificial protection."
a82_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/A_zinc-plated_surface_for_the_protection_from_corrosion.jpg/800px-A_zinc-plated_surface_for_the_protection_from_corrosion.jpg"
a82_p2.metadata = {
    'author': 'Hi-Res Images of Chemical Elements',
    'licensing': 'CC BY 3.0',
    'attribution': 'Hi-Res Images of Chemical Elements / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_zinc-plated_surface_for_the_protection_from_corrosion.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Metal ionization tendency'
}
a82_p2.save()
a82_p2.blocks.set([b82_p2])
print("Lesson 82 Page 2: Asset 367 attached.")

b82_p3 = get_or_create_diagram_block(l82, 3, "Polished Copper Metal Specimen Displaying Lower Ionization Tendency")
a82_p3, _ = LessonAsset.objects.get_or_create(id=368, defaults={'lesson': l82, 'asset_type': 'image'})
a82_p3.lesson = l82
a82_p3.asset_type = 'image'
a82_p3.source_type = 'external'
a82_p3.storage_type = 'url'
a82_p3.status = 'attached'
a82_p3.title = "Polished Copper Metal Specimen Displaying Lower Ionization Tendency"
a82_p3.description = "Photograph of copper sulfate crystals illustrating copper's position lower on the electrochemical series with higher reduction tendency."
a82_p3.url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Copper_sulfate_pentahydrate_crystals.jpg"
a82_p3.metadata = {
    'author': 'W. Oelen',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'W. Oelen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Copper_sulfate_pentahydrate_crystals.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Copper low ionization tendency'
}
a82_p3.save()
a82_p3.blocks.set([b82_p3])
print("Lesson 82 Page 3: Asset 368 attached.")

svg_82_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ELECTROCHEMICAL REACTIVITY LADDER: IONIZATION TENDENCY OF METALS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Tendency of Metal Atoms to Lose Electrons: M(s) → Mⁿ⁺(aq) + ne⁻</text>
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <g transform="translate(40, 20)">
      <!-- Ladder Items -->
      <rect x="0" y="0" width="280" height="40" rx="6" fill="#020617" stroke="#ef4444" stroke-width="2"/>
      <text x="20" y="25" fill="#f87171" font-size="12" font-weight="bold">K → K⁺ + e⁻</text>
      <text x="260" y="25" text-anchor="end" fill="#fca5a5" font-size="10">E° = -2.92 V (Highest Tendency)</text>

      <rect x="0" y="50" width="280" height="40" rx="6" fill="#020617" stroke="#f97316"/>
      <text x="20" y="75" fill="#fb923c" font-size="12" font-weight="bold">Na → Na⁺ + e⁻</text>
      <text x="260" y="75" text-anchor="end" fill="#fed7aa" font-size="10">E° = -2.71 V</text>

      <rect x="0" y="100" width="280" height="40" rx="6" fill="#020617" stroke="#fbbf24"/>
      <text x="20" y="125" fill="#fbbf24" font-size="12" font-weight="bold">Mg → Mg²⁺ + 2e⁻</text>
      <text x="260" y="125" text-anchor="end" fill="#fde68a" font-size="10">E° = -2.38 V</text>

      <rect x="0" y="150" width="280" height="40" rx="6" fill="#020617" stroke="#38bdf8"/>
      <text x="20" y="175" fill="#38bdf8" font-size="12" font-weight="bold">Zn → Zn²⁺ + 2e⁻</text>
      <text x="260" y="175" text-anchor="end" fill="#bae6fd" font-size="10">E° = -0.76 V</text>

      <rect x="0" y="200" width="280" height="40" rx="6" fill="#020617" stroke="#64748b"/>
      <text x="20" y="225" fill="#cbd5e1" font-size="12" font-weight="bold">Fe → Fe²⁺ + 2e⁻</text>
      <text x="260" y="225" text-anchor="end" fill="#cbd5e1" font-size="10">E° = -0.44 V</text>

      <rect x="0" y="250" width="280" height="40" rx="6" fill="#020617" stroke="#10b981"/>
      <text x="20" y="275" fill="#34d399" font-size="12" font-weight="bold">Cu → Cu²⁺ + 2e⁻</text>
      <text x="260" y="275" text-anchor="end" fill="#a7f3d0" font-size="10">E° = +0.34 V (Lowest Tendency)</text>
    </g>

    <!-- Side Analysis Card -->
    <rect x="360" y="20" width="300" height="295" rx="10" fill="#020617" stroke="#38bdf8"/>
    <text x="510" y="48" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Key Trends &amp; Principles:</text>
    <text x="380" y="80" fill="#f87171" font-size="11" font-weight="bold">Top of Ladder (Most Negative E°):</text>
    <text x="380" y="100" fill="#cbd5e1" font-size="10">• Strongest reducing agents</text>
    <text x="380" y="118" fill="#cbd5e1" font-size="10">• Readily oxidized to form cations</text>
    <text x="380" y="136" fill="#cbd5e1" font-size="10">• Displaces any metal below it</text>

    <text x="380" y="175" fill="#34d399" font-size="11" font-weight="bold">Bottom of Ladder (Positive E°):</text>
    <text x="380" y="195" fill="#cbd5e1" font-size="10">• Least tendency to lose electrons</text>
    <text x="380" y="213" fill="#cbd5e1" font-size="10">• Ions (Cu²⁺) are easily reduced to metal</text>
    <text x="380" y="231" fill="#cbd5e1" font-size="10">• Acts as cathode in voltaic pairs</text>

    <rect x="375" y="255" width="270" height="45" rx="6" fill="#1e293b"/>
    <text x="510" y="282" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Rule: Higher Metal Displaces Lower Metal</text>
  </g>
</svg>'''
b82_p4 = get_or_create_diagram_block(l82, 4, "Electrochemical Reactivity Ladder and Ionization Tendency Trends")
a82_p4, _ = LessonAsset.objects.get_or_create(id=369, defaults={'lesson': l82, 'asset_type': 'diagram'})
a82_p4.lesson = l82
a82_p4.asset_type = 'diagram'
a82_p4.source_type = 'ai_generated'
a82_p4.storage_type = 'file'
a82_p4.status = 'attached'
a82_p4.title = "Electrochemical Reactivity Ladder and Ionization Tendency Trends"
a82_p4.description = "Hierarchy diagram ranking metals by standard reduction potential and electron-loss tendency in aqueous solution."
a82_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_82_p4)
a82_p4.file.save(f'metal_ionization_ladder_{l82.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a82_p4.blocks.set([b82_p4])
print("Lesson 82 Page 4: Asset 369 saved and attached.")


# =========================================================================
# 7. LESSON 83: Functions of the Salt Bridge (LU Order 7)
# =========================================================================
l83 = Lesson.objects.get(id=83)
print(f"\nProcessing Lesson 83: {l83.title}")

b83_p2 = get_or_create_diagram_block(l83, 2, "High-Purity Potassium Nitrate (KNO3) Salt Crystals for Salt Bridge Preparation")
a83_p2, _ = LessonAsset.objects.get_or_create(id=370, defaults={'lesson': l83, 'asset_type': 'image'})
a83_p2.lesson = l83
a83_p2.asset_type = 'image'
a83_p2.source_type = 'external'
a83_p2.storage_type = 'url'
a83_p2.status = 'attached'
a83_p2.title = "High-Purity Potassium Nitrate (KNO3) Salt Crystals for Salt Bridge Preparation"
a83_p2.description = "Photograph of pure potassium nitrate salt crystals dissolved into agar gel to provide unreactive mobile K+ and NO3- ions for salt bridges."
a83_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/KNO3_crystal.jpg/800px-KNO3_crystal.jpg"
a83_p2.metadata = {
    'author': 'Hjschwarz',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Hjschwarz / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:KNO3_crystal.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'KNO3 electrolyte for salt bridge'
}
a83_p2.save()
a83_p2.blocks.set([b83_p2])
print("Lesson 83 Page 2: Asset 370 attached.")

b83_p3 = get_or_create_diagram_block(l83, 3, "Sealed Laboratory Volumetric Flask with Standard Electrolyte Solution")
a83_p3, _ = LessonAsset.objects.get_or_create(id=371, defaults={'lesson': l83, 'asset_type': 'image'})
a83_p3.lesson = l83
a83_p3.asset_type = 'image'
a83_p3.source_type = 'external'
a83_p3.storage_type = 'url'
a83_p3.status = 'attached'
a83_p3.title = "Sealed Laboratory Volumetric Flask with Standard Electrolyte Solution"
a83_p3.description = "Photograph of standard electrolyte solution glassware used to maintain exact 1.0 M ionic concentrations in galvanic half-cell systems."
a83_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Brand_volumetric_flask_100ml.jpg/800px-Brand_volumetric_flask_100ml.jpg"
a83_p3.metadata = {
    'author': 'Lucasbosch',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Lucasbosch / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Brand_volumetric_flask_100ml.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Standard electrolyte solution'
}
a83_p3.save()
a83_p3.blocks.set([b83_p3])
print("Lesson 83 Page 3: Asset 371 attached.")

svg_83_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">FUNCTIONS OF THE SALT BRIDGE: ELECTRICAL NEUTRALITY</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">How Anions and Cations Migrate to Prevent Charge Buildup and Keep Current Flowing</text>
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <g transform="translate(30, 20)">
      <!-- Left: Anode Neutralization -->
      <rect x="0" y="0" width="305" height="195" rx="10" fill="#020617" stroke="#ef4444"/>
      <text x="152" y="28" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">1. ANODE COMPARTMENT (Zn/Zn²⁺)</text>
      <text x="15" y="60" fill="#cbd5e1" font-size="10">• Zn atoms oxidize into Zn²⁺ ions.</text>
      <text x="15" y="80" fill="#fca5a5" font-size="10">• Threat: Solution builds excess (+) charge.</text>
      <text x="15" y="105" fill="#38bdf8" font-size="11" font-weight="bold">Salt Bridge Action:</text>
      <text x="15" y="125" fill="#38bdf8" font-size="10">NO₃⁻ anions migrate INTO anode beaker</text>
      <text x="15" y="145" fill="#4ade80" font-size="10" font-weight="bold">Result: Neutralizes positive Zn²⁺ buildup</text>
    </g>
    <g transform="translate(365, 20)">
      <!-- Right: Cathode Neutralization -->
      <rect x="0" y="0" width="305" height="195" rx="10" fill="#020617" stroke="#38bdf8"/>
      <text x="152" y="28" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">2. CATHODE COMPARTMENT (Cu²⁺/Cu)</text>
      <text x="15" y="60" fill="#cbd5e1" font-size="10">• Cu²⁺ ions gain electrons and deposit as Cu.</text>
      <text x="15" y="80" fill="#93c5fd" font-size="10">• Threat: Solution leaves excess SO₄²⁻ (-) charge.</text>
      <text x="15" y="105" fill="#fbbf24" font-size="11" font-weight="bold">Salt Bridge Action:</text>
      <text x="15" y="125" fill="#fbbf24" font-size="10">K⁺ cations migrate INTO cathode beaker</text>
      <text x="15" y="145" fill="#4ade80" font-size="10" font-weight="bold">Result: Neutralizes negative SO₄²⁻ buildup</text>
    </g>
    <!-- Summary of 3 Core Functions -->
    <rect x="30" y="230" width="640" height="85" rx="8" fill="#020617" stroke="#a855f7"/>
    <text x="350" y="252" text-anchor="middle" fill="#c084fc" font-size="11" font-weight="bold">Three Essential Functions of the Salt Bridge:</text>
    <text x="45" y="275" fill="#cbd5e1" font-size="10">1. Completes the internal electric circuit by allowing mobile ion movement.</text>
    <text x="45" y="295" fill="#cbd5e1" font-size="10">2. Maintains electrical neutrality in both half-cells to prevent voltage drop to 0 V.</text>
    <text x="45" y="312" fill="#cbd5e1" font-size="10">3. Prevents direct physical mixing of the two separate electrolyte solutions.</text>
  </g>
</svg>'''
b83_p4 = get_or_create_diagram_block(l83, 4, "Sub-Microscopic Salt Bridge Ion Migration and Circuit Completion Mechanism")
a83_p4, _ = LessonAsset.objects.get_or_create(id=372, defaults={'lesson': l83, 'asset_type': 'diagram'})
a83_p4.lesson = l83
a83_p4.asset_type = 'diagram'
a83_p4.source_type = 'ai_generated'
a83_p4.storage_type = 'file'
a83_p4.status = 'attached'
a83_p4.title = "Sub-Microscopic Salt Bridge Ion Migration and Circuit Completion Mechanism"
a83_p4.description = "Diagram detailing the three core functions of the salt bridge and the bidirectional migration of potassium (K+) and nitrate (NO3-) ions."
a83_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_83_p4)
a83_p4.file.save(f'salt_bridge_functions_{l83.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a83_p4.blocks.set([b83_p4])
print("Lesson 83 Page 4: Asset 372 saved and attached.")


# =========================================================================
# 8. LESSON 86: Standard Electrode Potentials (LU Order 8)
# =========================================================================
l86 = Lesson.objects.get(id=86)
print(f"\nProcessing Lesson 86: {l86.title}")

b86_p2 = get_or_create_diagram_block(l86, 2, "Precision Laboratory Galvanic Element and Calibrated Half-Cell Apparatus")
a86_p2, _ = LessonAsset.objects.get_or_create(id=373, defaults={'lesson': l86, 'asset_type': 'image'})
a86_p2.lesson = l86
a86_p2.asset_type = 'image'
a86_p2.source_type = 'external'
a86_p2.storage_type = 'url'
a86_p2.status = 'attached'
a86_p2.title = "Precision Laboratory Galvanic Element and Calibrated Half-Cell Apparatus"
a86_p2.description = "Photograph of standard electrochemical half-cells connected to measure single electrode potentials against reference standards."
a86_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Daniell-element.png/800px-Daniell-element.png"
a86_p2.metadata = {
    'author': 'Fredrik Jonsén',
    'licensing': 'CC0',
    'attribution': 'Fredrik Jonsén / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Daniell-element.png',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Standard half-cell measurement'
}
a86_p2.save()
a86_p2.blocks.set([b86_p2])
print("Lesson 86 Page 2: Asset 373 attached.")

b86_p3 = get_or_create_diagram_block(l86, 3, "Standard 1.0 M Calibrated Volumetric Flask for Standard State Solutions")
a86_p3, _ = LessonAsset.objects.get_or_create(id=374, defaults={'lesson': l86, 'asset_type': 'image'})
a86_p3.lesson = l86
a86_p3.asset_type = 'image'
a86_p3.source_type = 'external'
a86_p3.storage_type = 'url'
a86_p3.status = 'attached'
a86_p3.title = "Standard 1.0 M Calibrated Volumetric Flask for Standard State Solutions"
a86_p3.description = "Photograph of a volumetric flask prepared to standard conditions: 1.0 M ion concentration at 25°C (298 K) for standard electrode potential determinations."
a86_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg/800px-1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg"
a86_p3.metadata = {
    'author': 'Wlwiener',
    'licensing': 'CC BY 4.0',
    'attribution': 'Wlwiener / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Standard thermodynamic solution concentration'
}
a86_p3.save()
a86_p3.blocks.set([b86_p3])
print("Lesson 86 Page 3: Asset 374 attached.")

svg_86_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">STANDARD HYDROGEN ELECTRODE (SHE): REFERENCE ZERO (E° = 0.00 V)</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Standard Conditions: 298 K (25°C) | 1.0 atm H₂ Gas | 1.0 M H⁺(aq) Solution | Platinized Platinum Electrode</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- SHE Half-Cell (Left) -->
    <g transform="translate(50, 20)">
      <rect x="0" y="60" width="220" height="230" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
      <text x="110" y="85" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">STANDARD HYDROGEN ELECTRODE</text>
      <text x="110" y="105" text-anchor="middle" fill="#f8fafc" font-size="14" font-weight="bold">E° = 0.00 V</text>
      <!-- Glass tube with H2 inlet -->
      <rect x="95" y="120" width="30" height="130" fill="#1e293b" stroke="#94a3b8"/>
      <!-- Platinum foil -->
      <rect x="100" y="210" width="20" height="30" fill="#475569" stroke="#fbbf24"/>
      <text x="110" y="230" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="bold">Pt</text>
      <!-- Solution -->
      <rect x="5" y="180" width="210" height="105" fill="#38bdf8" fill-opacity="0.1"/>
      <text x="110" y="275" text-anchor="middle" fill="#7dd3fc" font-size="10">1.0 M H⁺(aq) [HCl]</text>
    </g>

    <!-- Voltmeter -->
    <circle cx="350" cy="80" r="32" fill="#020617" stroke="#fbbf24" stroke-width="2"/>
    <text x="350" y="78" text-anchor="middle" fill="#fbbf24" font-size="14" font-weight="bold">-0.76 V</text>
    <text x="350" y="95" text-anchor="middle" fill="#94a3b8" font-size="8">High-R Voltmeter</text>

    <!-- Zinc Half-Cell (Right) -->
    <g transform="translate(430, 20)">
      <rect x="0" y="60" width="220" height="230" rx="10" fill="#020617" stroke="#f87171" stroke-width="2"/>
      <text x="110" y="85" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">ZINC TEST HALF-CELL</text>
      <text x="110" y="105" text-anchor="middle" fill="#f8fafc" font-size="14" font-weight="bold">Zn²⁺(aq) / Zn(s)</text>
      <!-- Zinc strip -->
      <rect x="95" y="120" width="30" height="130" fill="#475569" stroke="#cbd5e1"/>
      <text x="110" y="160" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Zn</text>
      <!-- Solution -->
      <rect x="5" y="180" width="210" height="105" fill="#f87171" fill-opacity="0.1"/>
      <text x="110" y="275" text-anchor="middle" fill="#fca5a5" font-size="10">1.0 M Zn²⁺(aq) [ZnSO₄]</text>
    </g>

    <!-- Bottom Deduction Box -->
    <rect x="40" y="280" width="620" height="55" rx="8" fill="#020617" stroke="#10b981"/>
    <text x="350" y="302" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="bold">Standard Reduction Potential Deduction:</text>
    <text x="350" y="322" text-anchor="middle" fill="#cbd5e1" font-size="10">Since electrons flow from Zn to SHE, Zn is oxidized. Therefore, E°(Zn²⁺/Zn) = -0.76 V.</text>
  </g>
</svg>'''
b86_p4 = get_or_create_diagram_block(l86, 4, "Standard Hydrogen Electrode (SHE) Cell Configuration and E0 Measurement")
a86_p4, _ = LessonAsset.objects.get_or_create(id=375, defaults={'lesson': l86, 'asset_type': 'diagram'})
a86_p4.lesson = l86
a86_p4.asset_type = 'diagram'
a86_p4.source_type = 'ai_generated'
a86_p4.storage_type = 'file'
a86_p4.status = 'attached'
a86_p4.title = "Standard Hydrogen Electrode (SHE) Cell Configuration and E0 Measurement"
a86_p4.description = "Apparatus setup showing the Standard Hydrogen Electrode connected to a zinc half-cell under standard conditions (298 K, 1 atm H2, 1 M H+) to measure E0."
a86_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_86_p4)
a86_p4.file.save(f'standard_hydrogen_electrode_{l86.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a86_p4.blocks.set([b86_p4])
print("Lesson 86 Page 4: Asset 375 saved and attached.")


# =========================================================================
# 9. LESSON 87: Uses of Standard Electrode Potentials (LU Order 9)
# =========================================================================
l87 = Lesson.objects.get(id=87)
print(f"\nProcessing Lesson 87: {l87.title}")

b87_p2 = get_or_create_diagram_block(l87, 2, "Digital Multimeter Measuring Positive Cell EMF Voltage")
a87_p2, _ = LessonAsset.objects.get_or_create(id=376, defaults={'lesson': l87, 'asset_type': 'image'})
a87_p2.lesson = l87
a87_p2.asset_type = 'image'
a87_p2.source_type = 'external'
a87_p2.storage_type = 'url'
a87_p2.status = 'attached'
a87_p2.title = "Digital Multimeter Measuring Positive Cell EMF Voltage"
a87_p2.description = "Photograph of a digital meter displaying measured electromotive force (e.m.f.) across an operating electrochemical cell."
a87_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg/800px-After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg"
a87_p2.metadata = {
    'author': 'Kmashaye5220',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Kmashaye5220 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:After_burning_up_the_circuit,_the_voltage_of_the_red_wires.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Cell EMF voltage verification'
}
a87_p2.save()
a87_p2.blocks.set([b87_p2])
print("Lesson 87 Page 2: Asset 376 attached.")

b87_p3 = get_or_create_diagram_block(l87, 3, "Working Zinc-Copper Galvanic Electrochemical Couple")
a87_p3, _ = LessonAsset.objects.get_or_create(id=377, defaults={'lesson': l87, 'asset_type': 'image'})
a87_p3.lesson = l87
a87_p3.asset_type = 'image'
a87_p3.source_type = 'external'
a87_p3.storage_type = 'url'
a87_p3.status = 'attached'
a87_p3.title = "Working Zinc-Copper Galvanic Electrochemical Couple"
a87_p3.description = "Photograph of an assembled galvanic cell illustrating the practical application of standard electrode potentials to generate electricity."
a87_p3.url = "https://upload.wikimedia.org/wikipedia/commons/3/34/Daniell_cell.jpg"
a87_p3.metadata = {
    'author': 'Unknown',
    'licensing': 'Public domain',
    'attribution': 'Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Daniell_cell.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electrochemical cell power generation'
}
a87_p3.save()
a87_p3.blocks.set([b87_p3])
print("Lesson 87 Page 3: Asset 377 attached.")

svg_87_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">CALCULATING CELL E.M.F. AND PREDICTING SPONTANEITY</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Mastering the Standard Formula: E°cell = E°(Reduction / Cathode) - E°(Oxidation / Anode)</text>
  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="720" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Step 1 Card -->
    <g transform="translate(30, 20)">
      <rect x="0" y="0" width="310" height="130" rx="8" fill="#020617" stroke="#38bdf8"/>
      <text x="155" y="25" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">STEP 1: IDENTIFY HALF-REACTIONS</text>
      <text x="15" y="50" fill="#cbd5e1" font-size="10">Cathode (Reduction): Cu²⁺ + 2e⁻ → Cu</text>
      <text x="15" y="70" fill="#4ade80" font-size="10" font-family="monospace">E°(reduction) = +0.34 V</text>
      <text x="15" y="95" fill="#cbd5e1" font-size="10">Anode (Oxidation): Zn²⁺ + 2e⁻ → Zn</text>
      <text x="15" y="115" fill="#f87171" font-size="10" font-family="monospace">E°(oxidation) = -0.76 V</text>
    </g>

    <!-- Step 2 Card -->
    <g transform="translate(380, 20)">
      <rect x="0" y="0" width="310" height="130" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="155" y="25" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">STEP 2: APPLY E°CELL FORMULA</text>
      <text x="155" y="55" text-anchor="middle" fill="#f8fafc" font-size="12" font-family="monospace" font-weight="bold">E°cell = E°(cathode) - E°(anode)</text>
      <text x="155" y="80" text-anchor="middle" fill="#fbbf24" font-size="11" font-family="monospace">E°cell = (+0.34 V) - (-0.76 V)</text>
      <text x="155" y="105" text-anchor="middle" fill="#4ade80" font-size="13" font-family="monospace" font-weight="bold">E°cell = +1.10 V</text>
    </g>

    <!-- Spontaneity Rule Box -->
    <rect x="30" y="170" width="660" height="145" rx="8" fill="#020617" stroke="#fbbf24"/>
    <text x="360" y="195" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">The Universal Spontaneity Rule in Kenyan KCSE Chemistry:</text>
    <g transform="translate(45, 215)">
      <rect x="0" y="0" width="280" height="85" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="140" y="25" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="bold">E°cell &gt; 0 (Positive Value)</text>
      <text x="140" y="50" text-anchor="middle" fill="#f8fafc" font-size="10">Reaction is SPONTANEOUS (Feasible)</text>
      <text x="140" y="70" text-anchor="middle" fill="#cbd5e1" font-size="9">Generates electric current in a cell</text>
    </g>
    <g transform="translate(345, 215)">
      <rect x="0" y="0" width="280" height="85" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="140" y="25" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">E°cell &lt; 0 (Negative Value)</text>
      <text x="140" y="50" text-anchor="middle" fill="#f8fafc" font-size="10">Reaction is NON-SPONTANEOUS</text>
      <text x="140" y="70" text-anchor="middle" fill="#cbd5e1" font-size="9">Will NOT occur without external voltage</text>
    </g>
  </g>
</svg>'''
b87_p4 = get_or_create_diagram_block(l87, 4, "Electrochemical Cell Potential (EMF) Calculation and Spontaneity Decision Grid")
a87_p4, _ = LessonAsset.objects.get_or_create(id=378, defaults={'lesson': l87, 'asset_type': 'diagram'})
a87_p4.lesson = l87
a87_p4.asset_type = 'diagram'
a87_p4.source_type = 'ai_generated'
a87_p4.storage_type = 'file'
a87_p4.status = 'attached'
a87_p4.title = "Electrochemical Cell Potential (EMF) Calculation and Spontaneity Decision Grid"
a87_p4.description = "Decision grid showing standard cell potential calculation and determining reaction feasibility based on whether E0cell is positive or negative."
a87_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_87_p4)
a87_p4.file.save(f'emf_spontaneity_grid_{l87.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a87_p4.blocks.set([b87_p4])
print("Lesson 87 Page 4: Asset 378 saved and attached.")


# =========================================================================
# 10. LESSON 88: Comparing Oxidizing and Reducing Power (LU Order 10)
# =========================================================================
l88 = Lesson.objects.get(id=88)
print(f"\nProcessing Lesson 88: {l88.title}")

b88_p2 = get_or_create_diagram_block(l88, 2, "Elemental Bromine Liquid and Dense Brown-Orange Vapor in Glass Ampoule")
a88_p2, _ = LessonAsset.objects.get_or_create(id=379, defaults={'lesson': l88, 'asset_type': 'image'})
a88_p2.lesson = l88
a88_p2.asset_type = 'image'
a88_p2.source_type = 'external'
a88_p2.storage_type = 'url'
a88_p2.status = 'attached'
a88_p2.title = "Elemental Bromine Liquid and Dense Brown-Orange Vapor in Glass Ampoule"
a88_p2.description = "Photograph of pure elemental bromine illustrating strong oxidizing non-metallic elements with positive standard reduction potentials."
a88_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Bromine-ampoule.jpg/800px-Bromine-ampoule.jpg"
a88_p2.metadata = {
    'author': 'Jurii',
    'licensing': 'CC BY 3.0',
    'attribution': 'Jurii / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Bromine-ampoule.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Strong oxidizing halogen power'
}
a88_p2.save()
a88_p2.blocks.set([b88_p2])
print("Lesson 88 Page 2: Asset 379 attached.")

b88_p3 = get_or_create_diagram_block(l88, 3, "Vigorous Burning of Magnesium Ribbon as a Strong Metallic Reducing Agent")
a88_p3, _ = LessonAsset.objects.get_or_create(id=380, defaults={'lesson': l88, 'asset_type': 'image'})
a88_p3.lesson = l88
a88_p3.asset_type = 'image'
a88_p3.source_type = 'external'
a88_p3.storage_type = 'url'
a88_p3.status = 'attached'
a88_p3.title = "Vigorous Burning of Magnesium Ribbon as a Strong Metallic Reducing Agent"
a88_p3.description = "Photograph of magnesium reacting vigorously, illustrating how electropositive metals with negative reduction potentials act as powerful reducing agents."
a88_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Magnesium_ribbon_burning.jpg/800px-Magnesium_ribbon_burning.jpg"
a88_p3.metadata = {
    'author': 'Capt. John Yossarian',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Capt. John Yossarian / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Magnesium_ribbon_burning.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Powerful reducing metal strength'
}
a88_p3.save()
a88_p3.blocks.set([b88_p3])
print("Lesson 88 Page 3: Asset 380 attached.")

svg_88_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">OXIDIZING VS. REDUCING POWER SPECTRUM (E° REDUCTION)</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Most Negative E° = Strongest Reducing Agent | Most Positive E° = Strongest Oxidizing Agent</text>
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Spectrum Ladder -->
    <g transform="translate(40, 20)">
      <rect x="0" y="0" width="280" height="42" rx="6" fill="#020617" stroke="#ef4444"/>
      <text x="15" y="26" fill="#f87171" font-size="11" font-weight="bold">F₂(g) + 2e⁻ ⇌ 2F⁻(aq)</text>
      <text x="265" y="26" text-anchor="end" fill="#fca5a5" font-size="10">+2.87 V</text>

      <rect x="0" y="50" width="280" height="42" rx="6" fill="#020617" stroke="#f97316"/>
      <text x="15" y="76" fill="#fb923c" font-size="11" font-weight="bold">Cl₂(g) + 2e⁻ ⇌ 2Cl⁻(aq)</text>
      <text x="265" y="76" text-anchor="end" fill="#fed7aa" font-size="10">+1.36 V</text>

      <rect x="0" y="100" width="280" height="42" rx="6" fill="#020617" stroke="#fbbf24"/>
      <text x="15" y="126" fill="#fbbf24" font-size="11" font-weight="bold">Cu²⁺(aq) + 2e⁻ ⇌ Cu(s)</text>
      <text x="265" y="126" text-anchor="end" fill="#fde68a" font-size="10">+0.34 V</text>

      <rect x="0" y="150" width="280" height="42" rx="6" fill="#020617" stroke="#94a3b8"/>
      <text x="15" y="176" fill="#cbd5e1" font-size="11" font-weight="bold">2H⁺(aq) + 2e⁻ ⇌ H₂(g)</text>
      <text x="265" y="176" text-anchor="end" fill="#fff" font-size="10">0.00 V (SHE)</text>

      <rect x="0" y="200" width="280" height="42" rx="6" fill="#020617" stroke="#38bdf8"/>
      <text x="15" y="226" fill="#38bdf8" font-size="11" font-weight="bold">Zn²⁺(aq) + 2e⁻ ⇌ Zn(s)</text>
      <text x="265" y="226" text-anchor="end" fill="#bae6fd" font-size="10">-0.76 V</text>

      <rect x="0" y="250" width="280" height="42" rx="6" fill="#020617" stroke="#10b981"/>
      <text x="15" y="276" fill="#34d399" font-size="11" font-weight="bold">K⁺(aq) + e⁻ ⇌ K(s)</text>
      <text x="265" y="276" text-anchor="end" fill="#a7f3d0" font-size="10">-2.92 V</text>
    </g>

    <!-- Side Analysis Cards -->
    <g transform="translate(360, 20)">
      <rect x="0" y="0" width="300" height="135" rx="8" fill="#020617" stroke="#ef4444"/>
      <text x="150" y="25" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">▲ INCREASING OXIDIZING POWER</text>
      <text x="15" y="50" fill="#cbd5e1" font-size="10">• Species on the LEFT with positive E°</text>
      <text x="15" y="70" fill="#cbd5e1" font-size="10">• Readily GAIN electrons (e.g. F₂, Cl₂, MnO₄⁻)</text>
      <text x="15" y="95" fill="#fca5a5" font-size="10" font-weight="bold">F₂ is the strongest oxidizing agent (+2.87 V)</text>
      <text x="15" y="115" fill="#94a3b8" font-size="9">Can oxidize all halide ions below it</text>

      <rect x="0" y="155" width="300" height="135" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="150" y="180" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">▼ INCREASING REDUCING POWER</text>
      <text x="15" y="205" fill="#cbd5e1" font-size="10">• Species on the RIGHT with negative E°</text>
      <text x="15" y="225" fill="#cbd5e1" font-size="10">• Readily LOSE electrons (e.g. K, Na, Mg, Zn)</text>
      <text x="15" y="250" fill="#a7f3d0" font-size="10" font-weight="bold">K(s) is the strongest reducing agent (-2.92 V)</text>
      <text x="15" y="270" fill="#94a3b8" font-size="9">Can reduce all metal cations above it</text>
    </g>
  </g>
</svg>'''
b88_p4 = get_or_create_diagram_block(l88, 4, "Electrochemical Potential Scale: Comparing Oxidizing vs Reducing Power")
a88_p4, _ = LessonAsset.objects.get_or_create(id=381, defaults={'lesson': l88, 'asset_type': 'diagram'})
a88_p4.lesson = l88
a88_p4.asset_type = 'diagram'
a88_p4.source_type = 'ai_generated'
a88_p4.storage_type = 'file'
a88_p4.status = 'attached'
a88_p4.title = "Electrochemical Potential Scale: Comparing Oxidizing vs Reducing Power"
a88_p4.description = "Comparative spectrum ranking chemical species from strongest oxidizing agents (most positive E0) to strongest reducing agents (most negative E0)."
a88_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_88_p4)
a88_p4.file.save(f'oxidizing_reducing_spectrum_{l88.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a88_p4.blocks.set([b88_p4])
print("Lesson 88 Page 4: Asset 381 saved and attached.")


# =========================================================================
# 11. LESSON 89: Predicting Reaction Feasibility (LU Order 11)
# =========================================================================
l89 = Lesson.objects.get(id=89)
print(f"\nProcessing Lesson 89: {l89.title}")

b89_p2 = get_or_create_diagram_block(l89, 2, "Glass Ampoule Containing Pure Elemental Bromine Reagent")
a89_p2, _ = LessonAsset.objects.get_or_create(id=382, defaults={'lesson': l89, 'asset_type': 'image'})
a89_p2.lesson = l89
a89_p2.asset_type = 'image'
a89_p2.source_type = 'external'
a89_p2.storage_type = 'url'
a89_p2.status = 'attached'
a89_p2.title = "Glass Ampoule Containing Pure Elemental Bromine Reagent"
a89_p2.description = "Photograph of pure elemental bromine used in halide displacement feasibility demonstrations (Cl2 + 2Br- -> 2Cl- + Br2)."
a89_p2.url = "https://upload.wikimedia.org/wikipedia/commons/b/bd/Brom_amp.jpg"
a89_p2.metadata = {
    'author': 'de:User:Tomihahndorf',
    'licensing': 'Copyrighted free use',
    'attribution': 'Tomihahndorf / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Brom_amp.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Halogen displacement feasibility'
}
a89_p2.save()
a89_p2.blocks.set([b89_p2])
print("Lesson 89 Page 2: Asset 382 attached.")

b89_p3 = get_or_create_diagram_block(l89, 3, "Deep Purple Potassium Permanganate Strong Oxidizing Solution")
a89_p3, _ = LessonAsset.objects.get_or_create(id=383, defaults={'lesson': l89, 'asset_type': 'image'})
a89_p3.lesson = l89
a89_p3.asset_type = 'image'
a89_p3.source_type = 'external'
a89_p3.storage_type = 'url'
a89_p3.status = 'attached'
a89_p3.title = "Deep Purple Potassium Permanganate Strong Oxidizing Solution"
a89_p3.description = "Photograph of potassium permanganate solution used to test and confirm the feasibility of oxidizing iron(II) to iron(III) based on positive cell EMF."
a89_p3.url = "https://upload.wikimedia.org/wikipedia/commons/8/8b/A_solution_of_Potassium_Permanganate_being_poured_into_a_well_in_an_Indian_village_to_disinfect_its_water.jpg"
a89_p3.metadata = {
    'author': 'Government of India',
    'licensing': 'Public domain',
    'attribution': 'Photo Division, Ministry of Information / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_solution_of_Potassium_Permanganate_being_poured_into_a_well_in_an_Indian_village_to_disinfect_its_water.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Spontaneous redox reaction feasibility'
}
a89_p3.save()
a89_p3.blocks.set([b89_p3])
print("Lesson 89 Page 3: Asset 383 attached.")

svg_89_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">HALIDE DISPLACEMENT FEASIBILITY &amp; PREDICTION MATRIX</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">A Halogen with a More Positive E° Displaces Halide Ions of a Halogen with a Less Positive E°</text>
  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="720" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Halide Displacement Matrix Table -->
    <g transform="translate(30, 20)">
      <rect x="0" y="0" width="660" height="35" rx="6" fill="#1e293b"/>
      <text x="100" y="22" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Reactants</text>
      <text x="270" y="22" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Calculated E°cell</text>
      <text x="440" y="22" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Reaction Prediction</text>
      <text x="580" y="22" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Observation</text>

      <!-- Row 1: Cl2 + 2Br- -->
      <rect x="0" y="45" width="660" height="40" rx="4" fill="#020617" stroke="#10b981"/>
      <text x="100" y="70" text-anchor="middle" fill="#f8fafc" font-size="10" font-family="monospace">Cl₂(g) + 2Br⁻(aq)</text>
      <text x="270" y="70" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">+1.36 - (+1.09) = +0.27 V</text>
      <text x="440" y="70" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">SPONTANEOUS ✓</text>
      <text x="580" y="70" text-anchor="middle" fill="#fb923c" font-size="9">Turns Red-Brown (Br₂)</text>

      <!-- Row 2: Cl2 + 2I- -->
      <rect x="0" y="95" width="660" height="40" rx="4" fill="#020617" stroke="#10b981"/>
      <text x="100" y="120" text-anchor="middle" fill="#f8fafc" font-size="10" font-family="monospace">Cl₂(g) + 2I⁻(aq)</text>
      <text x="270" y="120" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">+1.36 - (+0.54) = +0.82 V</text>
      <text x="440" y="120" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">SPONTANEOUS ✓</text>
      <text x="580" y="120" text-anchor="middle" fill="#c084fc" font-size="9">Turns Dark Brown / Black (I₂)</text>

      <!-- Row 3: I2 + 2Cl- -->
      <rect x="0" y="145" width="660" height="40" rx="4" fill="#020617" stroke="#ef4444"/>
      <text x="100" y="170" text-anchor="middle" fill="#f8fafc" font-size="10" font-family="monospace">I₂(s) + 2Cl⁻(aq)</text>
      <text x="270" y="170" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">+0.54 - (+1.36) = -0.82 V</text>
      <text x="440" y="170" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">NO REACTION ✗</text>
      <text x="580" y="170" text-anchor="middle" fill="#94a3b8" font-size="9">No observable change</text>
    </g>

    <!-- Golden Rule Box -->
    <rect x="30" y="225" width="660" height="90" rx="8" fill="#020617" stroke="#fbbf24"/>
    <text x="360" y="250" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Halide Displacement Order in KCSE Chemistry:</text>
    <text x="360" y="275" text-anchor="middle" fill="#f8fafc" font-size="12" font-family="monospace" font-weight="bold">Fluorine (F₂) &gt; Chlorine (Cl₂) &gt; Bromine (Br₂) &gt; Iodine (I₂)</text>
    <text x="360" y="298" text-anchor="middle" fill="#cbd5e1" font-size="10">Higher halogens have more positive E° values and act as stronger electron grabbers.</text>
  </g>
</svg>'''
b89_p4 = get_or_create_diagram_block(l89, 4, "Halide Displacement Spontaneity Matrix and Feasibility Prediction Table")
a89_p4, _ = LessonAsset.objects.get_or_create(id=384, defaults={'lesson': l89, 'asset_type': 'diagram'})
a89_p4.lesson = l89
a89_p4.asset_type = 'diagram'
a89_p4.source_type = 'ai_generated'
a89_p4.storage_type = 'file'
a89_p4.status = 'attached'
a89_p4.title = "Halide Displacement Spontaneity Matrix and Feasibility Prediction Table"
a89_p4.description = "Summary matrix detailing calculated E0cell values and experimental feasibility for halogen displacement reactions."
a89_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_89_p4)
a89_p4.file.save(f'halide_displacement_matrix_{l89.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a89_p4.blocks.set([b89_p4])
print("Lesson 89 Page 4: Asset 384 saved and attached.")


# =========================================================================
# 12. LESSON 84: Use of Electrochemical Cells (LU Order 12)
# =========================================================================
l84 = Lesson.objects.get(id=84)
print(f"\nProcessing Lesson 84: {l84.title}")

b84_p2 = get_or_create_diagram_block(l84, 2, "Commercial Cylindrical Alkaline and Carbon Dry Cell Batteries")
a84_p2, _ = LessonAsset.objects.get_or_create(id=385, defaults={'lesson': l84, 'asset_type': 'image'})
a84_p2.lesson = l84
a84_p2.asset_type = 'image'
a84_p2.source_type = 'external'
a84_p2.storage_type = 'url'
a84_p2.status = 'attached'
a84_p2.title = "Commercial Cylindrical Alkaline and Carbon Dry Cell Batteries"
a84_p2.description = "Photograph of standard commercial dry cells illustrating primary portable electrochemical power sources."
a84_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/AAA_Alkaline_IMGP6972_wp.jpg/800px-AAA_Alkaline_IMGP6972_wp.jpg"
a84_p2.metadata = {
    'author': 'smial',
    'licensing': 'FAL',
    'attribution': 'smial / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:AAA_Alkaline_IMGP6972_wp.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Commercial primary cells'
}
a84_p2.save()
a84_p2.blocks.set([b84_p2])
print("Lesson 84 Page 2: Asset 385 attached.")

b84_p3 = get_or_create_diagram_block(l84, 3, "Industrial Heavy-Duty Secondary Storage Battery Charger and Power Unit")
a84_p3, _ = LessonAsset.objects.get_or_create(id=386, defaults={'lesson': l84, 'asset_type': 'image'})
a84_p3.lesson = l84
a84_p3.asset_type = 'image'
a84_p3.source_type = 'external'
a84_p3.storage_type = 'url'
a84_p3.status = 'attached'
a84_p3.title = "Industrial Heavy-Duty Secondary Storage Battery Charger and Power Unit"
a84_p3.description = "Photograph of a secondary battery recharging system demonstrating electrical recharging of reversible lead-acid storage cells."
a84_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/1-1111_typical_external_of_a_simple_lead-acid_battery_charger.png/800px-1-1111_typical_external_of_a_simple_lead-acid_battery_charger.png"
a84_p3.metadata = {
    'author': '1-1111',
    'licensing': 'CC BY-SA 4.0',
    'attribution': '1-1111 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:1-1111_typical_external_of_a_simple_lead-acid_battery_charger.png',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Rechargeable secondary cell battery'
}
a84_p3.save()
a84_p3.blocks.set([b84_p3])
print("Lesson 84 Page 3: Asset 386 attached.")

svg_84_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">TAXONOMY OF COMMERCIAL ELECTROCHEMICAL CELLS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Classifying Primary Non-Rechargeable Cells, Secondary Rechargeable Accumulators, and Fuel Cells</text>
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="730" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Category 1: Primary Cells -->
    <g transform="translate(15, 20)">
      <rect x="0" y="0" width="220" height="295" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
      <text x="110" y="30" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">PRIMARY CELLS</text>
      <text x="110" y="50" text-anchor="middle" fill="#7dd3fc" font-size="10">(Irreversible)</text>
      <rect x="15" y="65" width="190" height="1" fill="#334155"/>
      <text x="15" y="90" fill="#f87171" font-size="10" font-weight="bold">• Non-rechargeable</text>
      <text x="15" y="110" fill="#cbd5e1" font-size="9">Chemicals consumed permanently</text>
      <text x="15" y="135" fill="#38bdf8" font-size="10" font-weight="bold">• Examples:</text>
      <text x="15" y="155" fill="#cbd5e1" font-size="9">- Zinc-carbon Leclanché dry cell</text>
      <text x="15" y="175" fill="#cbd5e1" font-size="9">- Alkaline manganese cell</text>
      <text x="15" y="195" fill="#cbd5e1" font-size="9">- Silver oxide button cell</text>
      <text x="15" y="235" fill="#fbbf24" font-size="10" font-weight="bold">• Uses:</text>
      <text x="15" y="255" fill="#cbd5e1" font-size="9">Torches, wall clocks, remotes</text>
    </g>

    <!-- Category 2: Secondary Cells -->
    <g transform="translate(255, 20)">
      <rect x="0" y="0" width="220" height="295" rx="10" fill="#020617" stroke="#10b981" stroke-width="2"/>
      <text x="110" y="30" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">SECONDARY CELLS</text>
      <text x="110" y="50" text-anchor="middle" fill="#a7f3d0" font-size="10">(Rechargeable Accumulators)</text>
      <rect x="15" y="65" width="190" height="1" fill="#334155"/>
      <text x="15" y="90" fill="#4ade80" font-size="10" font-weight="bold">• Fully rechargeable</text>
      <text x="15" y="110" fill="#cbd5e1" font-size="9">Reversible chemical reactions</text>
      <text x="15" y="135" fill="#34d399" font-size="10" font-weight="bold">• Examples:</text>
      <text x="15" y="155" fill="#cbd5e1" font-size="9">- Lead-acid storage battery</text>
      <text x="15" y="175" fill="#cbd5e1" font-size="9">- Lithium-ion battery</text>
      <text x="15" y="195" fill="#cbd5e1" font-size="9">- Nickel-cadmium (Ni-Cd)</text>
      <text x="15" y="235" fill="#fbbf24" font-size="10" font-weight="bold">• Uses:</text>
      <text x="15" y="255" fill="#cbd5e1" font-size="9">Motor vehicles, smartphones, laptops</text>
    </g>

    <!-- Category 3: Fuel Cells -->
    <g transform="translate(495, 20)">
      <rect x="0" y="0" width="220" height="295" rx="10" fill="#020617" stroke="#fbbf24" stroke-width="2"/>
      <text x="110" y="30" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">FUEL CELLS</text>
      <text x="110" y="50" text-anchor="middle" fill="#fde68a" font-size="10">(Continuous Feed)</text>
      <rect x="15" y="65" width="190" height="1" fill="#334155"/>
      <text x="15" y="90" fill="#38bdf8" font-size="10" font-weight="bold">• Continuous external supply</text>
      <text x="15" y="110" fill="#cbd5e1" font-size="9">Does not run down or need recharge</text>
      <text x="15" y="135" fill="#fbbf24" font-size="10" font-weight="bold">• Examples:</text>
      <text x="15" y="155" fill="#cbd5e1" font-size="9">- Hydrogen-oxygen fuel cell</text>
      <text x="15" y="175" fill="#4ade80" font-size="9">2H₂ + O₂ → 2H₂O + Electricity</text>
      <text x="15" y="195" fill="#a7f3d0" font-size="9">Zero toxic emissions (Water only)</text>
      <text x="15" y="235" fill="#fbbf24" font-size="10" font-weight="bold">• Uses:</text>
      <text x="15" y="255" fill="#cbd5e1" font-size="9">Spacecraft, electric buses, grid power</text>
    </g>
  </g>
</svg>'''
b84_p4 = get_or_create_diagram_block(l84, 4, "Taxonomy of Primary, Secondary, and Fuel Electrochemical Cells")
a84_p4, _ = LessonAsset.objects.get_or_create(id=387, defaults={'lesson': l84, 'asset_type': 'diagram'})
a84_p4.lesson = l84
a84_p4.asset_type = 'diagram'
a84_p4.source_type = 'ai_generated'
a84_p4.storage_type = 'file'
a84_p4.status = 'attached'
a84_p4.title = "Taxonomy of Primary, Secondary, and Fuel Electrochemical Cells"
a84_p4.description = "Comparative 3-column framework contrasting primary irreversible cells, secondary rechargeable accumulators, and continuous fuel cells."
a84_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_84_p4)
a84_p4.file.save(f'cells_taxonomy_framework_{l84.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a84_p4.blocks.set([b84_p4])
print("Lesson 84 Page 4: Asset 387 saved and attached.")


# =========================================================================
# 13. LESSON 85: Dry Cells (Leclanché Cell) (LU Order 13)
# =========================================================================
l85 = Lesson.objects.get(id=85)
print(f"\nProcessing Lesson 85: {l85.title}")

b85_p2 = get_or_create_diagram_block(l85, 2, "Classic Cylindrical Dry Cell Battery for Portable Power")
a85_p2, _ = LessonAsset.objects.get_or_create(id=388, defaults={'lesson': l85, 'asset_type': 'image'})
a85_p2.lesson = l85
a85_p2.asset_type = 'image'
a85_p2.source_type = 'external'
a85_p2.storage_type = 'url'
a85_p2.status = 'attached'
a85_p2.title = "Classic Cylindrical Dry Cell Battery for Portable Power"
a85_p2.description = "Photograph of a vintage cylindrical dry cell demonstrating the external form factor of commercial zinc-carbon Leclanché cells."
a85_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/1976_Swedish_Tudor_4_5_V_A_4_5_dry_cell_battery.jpg/800px-1976_Swedish_Tudor_4_5_V_A_4_5_dry_cell_battery.jpg"
a85_p2.metadata = {
    'author': 'R. Henrik Nilsson',
    'licensing': 'CC BY 4.0',
    'attribution': 'R. Henrik Nilsson / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:1976_Swedish_Tudor_4_5_V_A_4_5_dry_cell_battery.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Dry cell battery exterior'
}
a85_p2.save()
a85_p2.blocks.set([b85_p2])
print("Lesson 85 Page 2: Asset 388 attached.")

b85_p3 = get_or_create_diagram_block(l85, 3, "Manganese(IV) Oxide Reagent Used as Chemical Depolarizer in Dry Cells")
a85_p3, _ = LessonAsset.objects.get_or_create(id=389, defaults={'lesson': l85, 'asset_type': 'image'})
a85_p3.lesson = l85
a85_p3.asset_type = 'image'
a85_p3.source_type = 'external'
a85_p3.storage_type = 'url'
a85_p3.status = 'attached'
a85_p3.title = "Manganese(IV) Oxide Reagent Used as Chemical Depolarizer in Dry Cells"
a85_p3.description = "Photograph of black manganese(IV) oxide powder which oxidizes hydrogen gas into water to prevent polarization in dry cells."
a85_p3.url = "https://upload.wikimedia.org/wikipedia/commons/2/27/H2O2_catalytic_decomposition.JPG"
a85_p3.metadata = {
    'author': 'Chemicalinterest',
    'licensing': 'Public domain',
    'attribution': 'Chemicalinterest / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:H2O2_catalytic_decomposition.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'MnO2 chemical depolarizer'
}
a85_p3.save()
a85_p3.blocks.set([b85_p3])
print("Lesson 85 Page 3: Asset 389 attached.")

svg_85_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">CROSS-SECTION OF A ZINC-CARBON (LECLANCHÉ) DRY CELL</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Internal Chemistry: Zinc Anode Oxidation, Carbon Cathode, NH₄Cl Paste Electrolyte, and MnO₂ Depolarizer</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Cutaway Battery Diagram (Left) -->
    <g transform="translate(60, 20)">
      <!-- Outer Zinc Can Anode -->
      <rect x="20" y="30" width="160" height="260" rx="12" fill="#334155" stroke="#94a3b8" stroke-width="2.5"/>
      
      <!-- Ammonium Chloride Paste Layer -->
      <rect x="30" y="40" width="140" height="240" rx="8" fill="#1e293b" stroke="#38bdf8"/>
      
      <!-- MnO2 + Carbon Powder Core -->
      <rect x="45" y="40" width="110" height="240" rx="6" fill="#020617" stroke="#fbbf24"/>
      
      <!-- Central Carbon (Graphite) Rod Cathode -->
      <rect x="88" y="20" width="24" height="245" rx="4" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>

      <!-- Brass Top Cap (+) -->
      <rect x="92" y="5" width="16" height="15" rx="3" fill="#fbbf24"/>
      <text x="100" y="-3" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Brass Cap (+)</text>

      <!-- Bottom Zinc Base (-) -->
      <text x="100" y="310" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">Zinc Base (-)</text>
    </g>

    <!-- Internal Chemical Equations & Roles (Right) -->
    <g transform="translate(300, 20)">
      <!-- Anode Box -->
      <rect x="0" y="10" width="370" height="65" rx="8" fill="#020617" stroke="#f87171"/>
      <text x="15" y="32" fill="#f87171" font-size="11" font-weight="bold">ZINC CASING (ANODE / NEGATIVE ELECTRODE):</text>
      <text x="15" y="55" fill="#fca5a5" font-size="11" font-family="monospace">Zn(s) → Zn²⁺(aq) + 2e⁻  (Oxidation)</text>

      <!-- Cathode Box -->
      <rect x="0" y="85" width="370" height="65" rx="8" fill="#020617" stroke="#38bdf8"/>
      <text x="15" y="107" fill="#38bdf8" font-size="11" font-weight="bold">CARBON ROD (CATHODE / POSITIVE ELECTRODE):</text>
      <text x="15" y="130" fill="#7dd3fc" font-size="11" font-family="monospace">2NH₄⁺ + 2e⁻ → 2NH₃ + H₂(g)  (Reduction)</text>

      <!-- Depolarizer Box -->
      <rect x="0" y="160" width="370" height="75" rx="8" fill="#020617" stroke="#fbbf24"/>
      <text x="15" y="182" fill="#fbbf24" font-size="11" font-weight="bold">MnO₂ DEPOLARIZER ACTION:</text>
      <text x="15" y="202" fill="#cbd5e1" font-size="10">2MnO₂(s) + H₂(g) → Mn₂O₃(s) + H₂O(l)</text>
      <text x="15" y="222" fill="#cbd5e1" font-size="9">• Oxidizes insulating H₂ gas to prevent polarization</text>

      <!-- Why called Dry Cell -->
      <rect x="0" y="245" width="370" height="60" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="15" y="267" fill="#34d399" font-size="10" font-weight="bold">Why called a 'Dry Cell'?</text>
      <text x="15" y="287" fill="#cbd5e1" font-size="9">Electrolyte is a moist paste of NH₄Cl + ZnCl₂, preventing spillage.</text>
    </g>
  </g>
</svg>'''
b85_p4 = get_or_create_diagram_block(l85, 4, "Complete Cross-Section and Reaction Chemistry of a Leclanché Dry Cell")
a85_p4, _ = LessonAsset.objects.get_or_create(id=390, defaults={'lesson': l85, 'asset_type': 'diagram'})
a85_p4.lesson = l85
a85_p4.asset_type = 'diagram'
a85_p4.source_type = 'ai_generated'
a85_p4.storage_type = 'file'
a85_p4.status = 'attached'
a85_p4.title = "Complete Cross-Section and Reaction Chemistry of a Leclanché Dry Cell"
a85_p4.description = "Cross-sectional diagram of a zinc-carbon dry cell showing the zinc anode can, carbon rod cathode, ammonium chloride paste electrolyte, and manganese(IV) oxide depolarizer."
a85_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_85_p4)
a85_p4.file.save(f'dry_cell_cross_section_{l85.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a85_p4.blocks.set([b85_p4])
print("Lesson 85 Page 4: Asset 390 saved and attached.")

print("\n=== First Half of Topic 4 (13 Lessons) Completed Successfully! ===")
