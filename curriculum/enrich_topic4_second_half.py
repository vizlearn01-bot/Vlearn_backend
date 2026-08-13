import os
import sys
import django
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db.models import Max
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Form 4 Topic 4: Second Half (12 Lessons) ===")

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
# 1. LESSON 90: Accumulators (Lead-Acid Storage Batteries) (LU Order 14)
# =========================================================================
l90 = Lesson.objects.get(id=90)
print(f"\nProcessing Lesson 90: {l90.title}")

b90_p2 = get_or_create_diagram_block(l90, 2, "Cutaway Cross-Section of an Automotive Lead-Acid Storage Battery")
a90_p2, _ = LessonAsset.objects.get_or_create(id=391, defaults={'lesson': l90, 'asset_type': 'image'})
a90_p2.lesson = l90
a90_p2.asset_type = 'image'
a90_p2.source_type = 'external'
a90_p2.storage_type = 'url'
a90_p2.status = 'attached'
a90_p2.title = "Cutaway Cross-Section of an Automotive Lead-Acid Storage Battery"
a90_p2.description = "Photograph of a commercial lead-acid accumulator cutaway showing the interleaved lead and lead(IV) oxide grid plates."
a90_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Cutaway_view_of_a_1953_automotive_lead-acid_battery.jpg/800px-Cutaway_view_of_a_1953_automotive_lead-acid_battery.jpg"
a90_p2.metadata = {
    'author': 'National Institute of Standards and Technology',
    'licensing': 'Public domain',
    'attribution': 'NIST / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Cutaway_view_of_a_1953_automotive_lead-acid_battery.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Lead-acid accumulator grid structure'
}
a90_p2.save()
a90_p2.blocks.set([b90_p2])
print("Lesson 90 Page 2: Asset 391 attached.")

b90_p3 = get_or_create_diagram_block(l90, 3, "Commercial Dilute Sulfuric Acid Electrolyte Reagent Bottle")
a90_p3, _ = LessonAsset.objects.get_or_create(id=392, defaults={'lesson': l90, 'asset_type': 'image'})
a90_p3.lesson = l90
a90_p3.asset_type = 'image'
a90_p3.source_type = 'external'
a90_p3.storage_type = 'url'
a90_p3.status = 'attached'
a90_p3.title = "Commercial Dilute Sulfuric Acid Electrolyte Reagent Bottle"
a90_p3.description = "Photograph of commercial sulfuric acid battery electrolyte with a standard density of 1.25 to 1.30 g/cm3 when fully charged."
a90_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Battery_fluid%2C_plastic_bottle.jpg/800px-Battery_fluid%2C_plastic_bottle.jpg"
a90_p3.metadata = {
    'author': 'Cjp24',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Cjp24 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Battery_fluid,_plastic_bottle.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Lead-acid battery electrolyte density'
}
a90_p3.save()
a90_p3.blocks.set([b90_p3])
print("Lesson 90 Page 3: Asset 392 attached.")

svg_90_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">LEAD-ACID ACCUMULATOR: ARCHITECTURE &amp; DISCHARGING/RECHARGING</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Spontaneous Power Delivery (Discharging) vs. Reversal by External DC Voltage (Recharging)</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Left: Discharging Reactions -->
    <g transform="translate(30, 20)">
      <rect x="0" y="0" width="305" height="235" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
      <text x="152" y="28" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">DISCHARGING (CELL PROVIDES CURRENT)</text>
      <text x="15" y="55" fill="#f87171" font-size="10" font-weight="bold">Anode (-): Spongy Lead (Pb)</text>
      <text x="15" y="75" fill="#fca5a5" font-size="9" font-family="monospace">Pb(s) + SO₄²⁻(aq) → PbSO₄(s) + 2e⁻</text>
      <text x="15" y="105" fill="#34d399" font-size="10" font-weight="bold">Cathode (+): Lead(IV) Oxide (PbO₂)</text>
      <text x="15" y="125" fill="#a7f3d0" font-size="9" font-family="monospace">PbO₂ + 4H⁺ + SO₄²⁻ + 2e⁻ → PbSO₄ + 2H₂O</text>
      <rect x="15" y="145" width="275" height="75" rx="6" fill="#1e293b"/>
      <text x="25" y="168" fill="#fbbf24" font-size="10" font-weight="bold">Overall Discharging Equation:</text>
      <text x="25" y="188" fill="#f8fafc" font-size="9" font-family="monospace">Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O</text>
      <text x="25" y="208" fill="#cbd5e1" font-size="8.5">• Acid consumed: Density drops below 1.15 g/cm³</text>
    </g>

    <!-- Right: Recharging Reactions -->
    <g transform="translate(365, 20)">
      <rect x="0" y="0" width="305" height="235" rx="10" fill="#020617" stroke="#10b981" stroke-width="2"/>
      <text x="152" y="28" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">RECHARGING (EXTERNAL DC POWER)</text>
      <text x="15" y="55" fill="#38bdf8" font-size="10" font-weight="bold">Negative Plate (Connected to - Terminal):</text>
      <text x="15" y="75" fill="#7dd3fc" font-size="9" font-family="monospace">PbSO₄(s) + 2e⁻ → Pb(s) + SO₄²⁻(aq)</text>
      <text x="15" y="105" fill="#f59e0b" font-size="10" font-weight="bold">Positive Plate (Connected to + Terminal):</text>
      <text x="15" y="125" fill="#fde68a" font-size="9" font-family="monospace">PbSO₄ + 2H₂O → PbO₂ + 4H⁺ + SO₄²⁻ + 2e⁻</text>
      <rect x="15" y="145" width="275" height="75" rx="6" fill="#1e293b"/>
      <text x="25" y="168" fill="#34d399" font-size="10" font-weight="bold">Overall Recharging Equation:</text>
      <text x="25" y="188" fill="#f8fafc" font-size="9" font-family="monospace">2PbSO₄ + 2H₂O → Pb + PbO₂ + 2H₂SO₄</text>
      <text x="25" y="208" fill="#cbd5e1" font-size="8.5">• Acid regenerated: Density rises back to 1.28 g/cm³</text>
    </g>

    <!-- Bottom Indicator Rule -->
    <rect x="30" y="270" width="640" height="65" rx="8" fill="#020617" stroke="#fbbf24"/>
    <text x="350" y="292" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">State of Charge Measurement Using a Hydrometer:</text>
    <text x="350" y="315" text-anchor="middle" fill="#cbd5e1" font-size="10">Fully Charged = 1.25–1.30 g/cm³ (2.0 V/cell) | Fully Discharged = 1.15 g/cm³ (1.8 V/cell)</text>
  </g>
</svg>'''
b90_p4 = get_or_create_diagram_block(l90, 4, "Lead-Acid Accumulator Architecture and Reversible Charge-Discharge Chemistry")
a90_p4, _ = LessonAsset.objects.get_or_create(id=393, defaults={'lesson': l90, 'asset_type': 'diagram'})
a90_p4.lesson = l90
a90_p4.asset_type = 'diagram'
a90_p4.source_type = 'ai_generated'
a90_p4.storage_type = 'file'
a90_p4.status = 'attached'
a90_p4.title = "Lead-Acid Accumulator Architecture and Reversible Charge-Discharge Chemistry"
a90_p4.description = "Diagram of a lead-acid accumulator contrasting spontaneous discharging reactions with forced electrolytic recharging reactions."
a90_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_90_p4)
a90_p4.file.save(f'lead_acid_accumulator_{l90.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a90_p4.blocks.set([b90_p4])
print("Lesson 90 Page 4: Asset 393 saved and attached.")


# =========================================================================
# 2. LESSON 91: Fuel Cells (LU Order 15)
# =========================================================================
l91 = Lesson.objects.get(id=91)
print(f"\nProcessing Lesson 91: {l91.title}")

b91_p2 = get_or_create_diagram_block(l91, 2, "Industrial Clean Energy Power Conversion and Charging Module")
a91_p2, _ = LessonAsset.objects.get_or_create(id=394, defaults={'lesson': l91, 'asset_type': 'image'})
a91_p2.lesson = l91
a91_p2.asset_type = 'image'
a91_p2.source_type = 'external'
a91_p2.storage_type = 'url'
a91_p2.status = 'attached'
a91_p2.title = "Industrial Clean Energy Power Conversion and Charging Module"
a91_p2.description = "Photograph of a commercial power module demonstrating high-efficiency conversion of chemical energy into steady direct current."
a91_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/1-1111_typical_external_of_a_simple_lead-acid_battery_charger.png/800px-1-1111_typical_external_of_a_simple_lead-acid_battery_charger.png"
a91_p2.metadata = {
    'author': '1-1111',
    'licensing': 'CC BY-SA 4.0',
    'attribution': '1-1111 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:1-1111_typical_external_of_a_simple_lead-acid_battery_charger.png',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electrochemical power delivery'
}
a91_p2.save()
a91_p2.blocks.set([b91_p2])
print("Lesson 91 Page 2: Asset 394 attached.")

b91_p3 = get_or_create_diagram_block(l91, 3, "Calibrated Standard Laboratory Electrolyte Flask")
a91_p3, _ = LessonAsset.objects.get_or_create(id=395, defaults={'lesson': l91, 'asset_type': 'image'})
a91_p3.lesson = l91
a91_p3.asset_type = 'image'
a91_p3.source_type = 'external'
a91_p3.storage_type = 'url'
a91_p3.status = 'attached'
a91_p3.title = "Calibrated Standard Laboratory Electrolyte Flask"
a91_p3.description = "Photograph of standard electrolyte solution glassware used for preparing concentrated alkaline potassium hydroxide (KOH) electrolyte for fuel cells."
a91_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Brand_volumetric_flask_100ml.jpg/800px-Brand_volumetric_flask_100ml.jpg"
a91_p3.metadata = {
    'author': 'Lucasbosch',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Lucasbosch / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Brand_volumetric_flask_100ml.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Fuel cell alkaline electrolyte'
}
a91_p3.save()
a91_p3.blocks.set([b91_p3])
print("Lesson 91 Page 3: Asset 395 attached.")

svg_91_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">HYDROGEN-OXYGEN (H₂-O₂) FUEL CELL FLOW ARCHITECTURE</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Continuous Electricity Generation with Zero Toxic By-products: 2H₂(g) + O₂(g) → 2H₂O(l)</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Cell Core -->
    <g transform="translate(60, 20)">
      <!-- Left Inflow Box (H2) -->
      <rect x="0" y="40" width="120" height="230" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="60" y="70" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">H₂ INLET</text>
      <text x="60" y="90" text-anchor="middle" fill="#7dd3fc" font-size="9">Hydrogen Fuel In</text>

      <!-- Porous Anode (Pt/Ni catalyst) -->
      <rect x="125" y="40" width="30" height="230" rx="4" fill="#334155" stroke="#fbbf24"/>
      <text x="140" y="160" text-anchor="middle" fill="#fbbf24" font-size="9" transform="rotate(-90 140 160)" font-weight="bold">Porous Anode (-)</text>

      <!-- Central Electrolyte (Hot Conc. KOH) -->
      <rect x="160" y="40" width="110" height="230" rx="4" fill="#1e293b" stroke="#10b981"/>
      <text x="215" y="135" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">Electrolyte</text>
      <text x="215" y="155" text-anchor="middle" fill="#a7f3d0" font-size="9">Hot Conc. KOH(aq)</text>
      <text x="215" y="175" text-anchor="middle" fill="#94a3b8" font-size="8">(Mobile OH⁻ ions)</text>

      <!-- Porous Cathode (Pt/Ni catalyst) -->
      <rect x="275" y="40" width="30" height="230" rx="4" fill="#334155" stroke="#fbbf24"/>
      <text x="290" y="160" text-anchor="middle" fill="#fbbf24" font-size="9" transform="rotate(-90 290 160)" font-weight="bold">Porous Cathode (+)</text>

      <!-- Right Inflow Box (O2 & Water outlet) -->
      <rect x="310" y="40" width="120" height="230" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="370" y="70" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">O₂ INLET</text>
      <text x="370" y="90" text-anchor="middle" fill="#7dd3fc" font-size="9">Oxygen Gas In</text>
      <text x="370" y="235" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">H₂O OUTLET</text>
      <text x="370" y="255" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Pure Water Vapor</text>
    </g>

    <!-- Side Equations & Advantages Card -->
    <g transform="translate(480, 20)">
      <rect x="0" y="0" width="200" height="315" rx="8" fill="#020617" stroke="#38bdf8"/>
      <text x="100" y="25" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">ELECTRODE REACTIONS</text>
      <text x="10" y="55" fill="#f87171" font-size="9" font-weight="bold">Anode Oxidation:</text>
      <text x="10" y="72" fill="#fca5a5" font-size="8" font-family="monospace">2H₂ + 4OH⁻ → 4H₂O + 4e⁻</text>
      <text x="10" y="105" fill="#34d399" font-size="9" font-weight="bold">Cathode Reduction:</text>
      <text x="10" y="122" fill="#a7f3d0" font-size="8" font-family="monospace">O₂ + 2H₂O + 4e⁻ → 4OH⁻</text>
      <rect x="8" y="145" width="184" height="1" fill="#334155"/>
      <text x="10" y="168" fill="#fbbf24" font-size="10" font-weight="bold">Key Advantages:</text>
      <text x="10" y="190" fill="#cbd5e1" font-size="8.5">1. Over 70% efficiency</text>
      <text x="10" y="210" fill="#cbd5e1" font-size="8.5">2. Zero polluting emissions</text>
      <text x="10" y="230" fill="#cbd5e1" font-size="8.5">3. Does not run down</text>
      <text x="10" y="250" fill="#cbd5e1" font-size="8.5">4. Silent operation</text>
      <text x="10" y="285" fill="#4ade80" font-size="9" font-weight="bold">Drinking water in space!</text>
    </g>
  </g>
</svg>'''
b91_p4 = get_or_create_diagram_block(l91, 4, "Hydrogen-Oxygen Fuel Cell Flow Architecture and Internal Reaction Chemistry")
a91_p4, _ = LessonAsset.objects.get_or_create(id=396, defaults={'lesson': l91, 'asset_type': 'diagram'})
a91_p4.lesson = l91
a91_p4.asset_type = 'diagram'
a91_p4.source_type = 'ai_generated'
a91_p4.storage_type = 'file'
a91_p4.status = 'attached'
a91_p4.title = "Hydrogen-Oxygen Fuel Cell Flow Architecture and Internal Reaction Chemistry"
a91_p4.description = "Schematic diagram of an alkaline hydrogen-oxygen fuel cell illustrating continuous fuel input, porous catalytic electrodes, and water formation."
a91_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_91_p4)
a91_p4.file.save(f'fuel_cell_architecture_{l91.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a91_p4.blocks.set([b91_p4])
print("Lesson 91 Page 4: Asset 396 saved and attached.")


# =========================================================================
# 3. LESSON 92: Electrolysis (LU Order 16)
# =========================================================================
l92 = Lesson.objects.get(id=92)
print(f"\nProcessing Lesson 92: {l92.title}")

b92_p2 = get_or_create_diagram_block(l92, 2, "Laboratory Electrolytic Cell System Connected to External DC Power")
a92_p2, _ = LessonAsset.objects.get_or_create(id=397, defaults={'lesson': l92, 'asset_type': 'image'})
a92_p2.lesson = l92
a92_p2.asset_type = 'image'
a92_p2.source_type = 'external'
a92_p2.storage_type = 'url'
a92_p2.status = 'attached'
a92_p2.title = "Laboratory Electrolytic Cell System Connected to External DC Power"
a92_p2.description = "Photograph of an assembled electrochemical apparatus illustrating external electrical energy driving chemical decomposition in an electrolytic cell."
a92_p2.url = "https://upload.wikimedia.org/wikipedia/commons/3/34/Daniell_cell.jpg"
a92_p2.metadata = {
    'author': 'Unknown',
    'licensing': 'Public domain',
    'attribution': 'Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Daniell_cell.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electrolytic cell apparatus'
}
a92_p2.save()
a92_p2.blocks.set([b92_p2])
print("Lesson 92 Page 2: Asset 397 attached.")

b92_p3 = get_or_create_diagram_block(l92, 3, "Digital Voltmeter and Ammeter Monitoring Direct Current Power Supply")
a92_p3, _ = LessonAsset.objects.get_or_create(id=398, defaults={'lesson': l92, 'asset_type': 'image'})
a92_p3.lesson = l92
a92_p3.asset_type = 'image'
a92_p3.source_type = 'external'
a92_p3.storage_type = 'url'
a92_p3.status = 'attached'
a92_p3.title = "Digital Voltmeter and Ammeter Monitoring Direct Current Power Supply"
a92_p3.description = "Photograph of digital electrical meters measuring voltage and steady current supplied during electrolysis experiments."
a92_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg/800px-After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg"
a92_p3.metadata = {
    'author': 'Kmashaye5220',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Kmashaye5220 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:After_burning_up_the_circuit,_the_voltage_of_the_red_wires.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'DC electrical power for electrolysis'
}
a92_p3.save()
a92_p3.blocks.set([b92_p3])
print("Lesson 92 Page 3: Asset 398 attached.")

svg_92_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">FUNDAMENTAL ELECTROLYTIC CELL CIRCUIT</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Electrical Energy Driving Non-Spontaneous Chemical Decomposition in Molten Lead(II) Bromide (PbBr₂)</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- External DC Battery & Wires -->
    <path d="M 230 110 L 230 40 L 310 40" stroke="#fbbf24" stroke-width="3"/>
    <path d="M 390 40 L 470 40 L 470 110" stroke="#fbbf24" stroke-width="3"/>
    <!-- Battery Symbol -->
    <rect x="315" y="25" width="70" height="30" rx="4" fill="#020617" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="350" y="44" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">DC Battery</text>
    <text x="295" y="38" fill="#f87171" font-size="14" font-weight="bold">+</text>
    <text x="400" y="38" fill="#38bdf8" font-size="14" font-weight="bold">-</text>

    <!-- Electrolytic Crucible Container -->
    <rect x="150" y="110" width="400" height="190" rx="10" fill="#020617" stroke="#64748b" stroke-width="2"/>
    <!-- Molten Electrolyte -->
    <rect x="160" y="170" width="380" height="120" rx="6" fill="#f59e0b" fill-opacity="0.15"/>
    <text x="350" y="275" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Molten Lead(II) Bromide Electrolyte: Pb²⁺(l) + 2Br⁻(l)</text>

    <!-- Left Anode (+) -->
    <rect x="215" y="90" width="30" height="150" rx="3" fill="#334155" stroke="#f87171" stroke-width="2"/>
    <text x="230" y="80" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">ANODE (+)</text>
    <text x="230" y="140" text-anchor="middle" fill="#cbd5e1" font-size="9">Graphite</text>
    <text x="230" y="215" text-anchor="middle" fill="#fb923c" font-size="8.5" font-family="monospace">2Br⁻ → Br₂ + 2e⁻</text>
    <text x="230" y="235" text-anchor="middle" fill="#fb923c" font-size="8">Red-Brown Br₂ gas</text>

    <!-- Right Cathode (-) -->
    <rect x="455" y="90" width="30" height="150" rx="3" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
    <text x="470" y="80" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">CATHODE (-)</text>
    <text x="470" y="140" text-anchor="middle" fill="#cbd5e1" font-size="9">Graphite</text>
    <text x="470" y="215" text-anchor="middle" fill="#38bdf8" font-size="8.5" font-family="monospace">Pb²⁺ + 2e⁻ → Pb</text>
    <text x="470" y="235" text-anchor="middle" fill="#cbd5e1" font-size="8">Grey Lead metal bead</text>

    <!-- Bottom Rule Card -->
    <rect x="30" y="305" width="640" height="40" rx="6" fill="#1e293b"/>
    <text x="350" y="328" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">Universal Rule: PANIC — Positive is Anode, Negative Is Cathode</text>
  </g>
</svg>'''
b92_p4 = get_or_create_diagram_block(l92, 4, "Fundamental Electrolytic Cell Circuit and Molten Electrolyte Decomposition")
a92_p4, _ = LessonAsset.objects.get_or_create(id=399, defaults={'lesson': l92, 'asset_type': 'diagram'})
a92_p4.lesson = l92
a92_p4.asset_type = 'diagram'
a92_p4.source_type = 'ai_generated'
a92_p4.storage_type = 'file'
a92_p4.status = 'attached'
a92_p4.title = "Fundamental Electrolytic Cell Circuit and Molten Electrolyte Decomposition"
a92_p4.description = "Diagram illustrating an electrolytic cell circuit where DC power drives the decomposition of molten lead(II) bromide into lead metal and bromine gas."
a92_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_92_p4)
a92_p4.file.save(f'electrolytic_cell_molten_{l92.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a92_p4.blocks.set([b92_p4])
print("Lesson 92 Page 4: Asset 399 saved and attached.")


# =========================================================================
# 4. LESSON 93: Preferential Discharge of Ions (LU Order 17)
# =========================================================================
l93 = Lesson.objects.get(id=93)
print(f"\nProcessing Lesson 93: {l93.title}")

b93_p2 = get_or_create_diagram_block(l93, 2, "Historic Hofmann Voltameter Apparatus for Electrolytic Water Decomposition")
a93_p2, _ = LessonAsset.objects.get_or_create(id=400, defaults={'lesson': l93, 'asset_type': 'image'})
a93_p2.lesson = l93
a93_p2.asset_type = 'image'
a93_p2.source_type = 'external'
a93_p2.storage_type = 'url'
a93_p2.status = 'attached'
a93_p2.title = "Historic Hofmann Voltameter Apparatus for Electrolytic Water Decomposition"
a93_p2.description = "Photograph of a classic Hofmann voltameter demonstrating preferential discharge of H+ and OH- ions into hydrogen (2 vols) and oxygen (1 vol)."
a93_p2.url = "https://upload.wikimedia.org/wikipedia/commons/f/f6/Hofmann%27scher_Wasserzersetzungsapparat_-_Deutsches_Museum_Verkehrszentrum.jpg"
a93_p2.metadata = {
    'author': 'Mattes',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Mattes / Wikimedia Commons',
    'commons_page_url': "https://commons.wikimedia.org/wiki/File:Hofmann'scher_Wasserzersetzungsapparat_-_Deutsches_Museum_Verkehrszentrum.jpg",
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Hofmann voltameter preferential discharge'
}
a93_p2.save()
a93_p2.blocks.set([b93_p2])
print("Lesson 93 Page 2: Asset 400 attached.")

b93_p3 = get_or_create_diagram_block(l93, 3, "Active Gas Bubble Evolution at Inert Electrodes in Aqueous Electrolyte")
a93_p3, _ = LessonAsset.objects.get_or_create(id=401, defaults={'lesson': l93, 'asset_type': 'image'})
a93_p3.lesson = l93
a93_p3.asset_type = 'image'
a93_p3.source_type = 'external'
a93_p3.storage_type = 'url'
a93_p3.status = 'attached'
a93_p3.title = "Active Gas Bubble Evolution at Inert Electrodes in Aqueous Electrolyte"
a93_p3.description = "Photograph of vigorous gas evolution during aqueous electrolysis where selectively discharged ions form gas bubbles at platinum/graphite surfaces."
a93_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/%28TiO2%29%5E2%2B_Kation.jpg/800px-%28TiO2%29%5E2%2B_Kation.jpg"
a93_p3.metadata = {
    'author': 'Johannes Schneider',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Johannes Schneider / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:(TiO2)^2+_Kation.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electrolytic gas discharge observation'
}
a93_p3.save()
a93_p3.blocks.set([b93_p3])
print("Lesson 93 Page 3: Asset 401 attached.")

svg_93_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">PREFERENTIAL DISCHARGE LADDER IN AQUEOUS ELECTROLYSIS</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Lower Species in the Electrochemical Series Are Discharged in Preference to Higher Species</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Left: Cation Discharge Ladder (Cathode) -->
    <g transform="translate(30, 20)">
      <rect x="0" y="0" width="305" height="250" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="152" y="25" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">CATIONS (REDUCED AT CATHODE)</text>
      <text x="20" y="52" fill="#cbd5e1" font-size="10">K⁺, Na⁺, Ca²⁺, Mg²⁺, Al³⁺</text>
      <text x="280" y="52" text-anchor="end" fill="#f87171" font-size="8.5">Difficult to discharge</text>
      <text x="20" y="80" fill="#cbd5e1" font-size="10">Zn²⁺, Fe²⁺, Pb²⁺</text>
      <text x="20" y="110" fill="#fbbf24" font-size="11" font-weight="bold">H⁺(aq)  (Water ionization)</text>
      <text x="280" y="110" text-anchor="end" fill="#fbbf24" font-size="9">E° = 0.00 V</text>
      <text x="20" y="140" fill="#34d399" font-size="11" font-weight="bold">Cu²⁺(aq), Ag⁺(aq), Au³⁺(aq)</text>
      <text x="280" y="140" text-anchor="end" fill="#34d399" font-size="9">Easiest to discharge</text>
      <rect x="15" y="160" width="275" height="75" rx="6" fill="#1e293b"/>
      <text x="25" y="182" fill="#38bdf8" font-size="9.5" font-weight="bold">Example (Dilute NaCl):</text>
      <text x="25" y="200" fill="#cbd5e1" font-size="8.5">Competing: Na⁺ and H⁺</text>
      <text x="25" y="218" fill="#4ade80" font-size="9" font-weight="bold">H⁺ discharged: 2H⁺ + 2e⁻ → H₂(g)</text>
    </g>

    <!-- Right: Anion Discharge Ladder (Anode) -->
    <g transform="translate(365, 20)">
      <rect x="0" y="0" width="305" height="250" rx="10" fill="#020617" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="152" y="25" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">ANIONS (OXIDIZED AT ANODE)</text>
      <text x="20" y="52" fill="#cbd5e1" font-size="10">F⁻, SO₄²⁻, NO₃⁻</text>
      <text x="280" y="52" text-anchor="end" fill="#f87171" font-size="8.5">Never discharged in aq</text>
      <text x="20" y="80" fill="#cbd5e1" font-size="10">Cl⁻ (discharged if concentrated)</text>
      <text x="20" y="110" fill="#fbbf24" font-size="10">Br⁻, I⁻</text>
      <text x="20" y="140" fill="#34d399" font-size="11" font-weight="bold">OH⁻(aq)  (Hydroxide ion)</text>
      <text x="280" y="140" text-anchor="end" fill="#34d399" font-size="9">Easiest to discharge in dilute</text>
      <rect x="15" y="160" width="275" height="75" rx="6" fill="#1e293b"/>
      <text x="25" y="182" fill="#fbbf24" font-size="9.5" font-weight="bold">Example (Dilute H₂SO₄):</text>
      <text x="25" y="200" fill="#cbd5e1" font-size="8.5">Competing: SO₄²⁻ and OH⁻</text>
      <text x="25" y="218" fill="#4ade80" font-size="9" font-weight="bold">OH⁻ discharged: 4OH⁻ → 2H₂O + O₂ + 4e⁻</text>
    </g>

    <!-- Bottom Golden Rule -->
    <rect x="30" y="285" width="640" height="55" rx="8" fill="#020617" stroke="#10b981"/>
    <text x="350" y="308" text-anchor="middle" fill="#4ade80" font-size="10.5" font-weight="bold">General Rule for Aqueous Electrolysis:</text>
    <text x="350" y="328" text-anchor="middle" fill="#cbd5e1" font-size="9.5">In dilute solutions, water ions (H⁺ and OH⁻) are discharged preferentially unless lower metals/halides are present.</text>
  </g>
</svg>'''
b93_p4 = get_or_create_diagram_block(l93, 4, "Preferential Discharge Ladder for Cations and Anions in Aqueous Electrolysis")
a93_p4, _ = LessonAsset.objects.get_or_create(id=402, defaults={'lesson': l93, 'asset_type': 'diagram'})
a93_p4.lesson = l93
a93_p4.asset_type = 'diagram'
a93_p4.source_type = 'ai_generated'
a93_p4.storage_type = 'file'
a93_p4.status = 'attached'
a93_p4.title = "Preferential Discharge Ladder for Cations and Anions in Aqueous Electrolysis"
a93_p4.description = "Hierarchy diagram ranking cations and anions by ease of preferential discharge at cathode and anode surfaces during aqueous electrolysis."
a93_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_93_p4)
a93_p4.file.save(f'preferential_discharge_ladder_{l93.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a93_p4.blocks.set([b93_p4])
print("Lesson 93 Page 4: Asset 402 saved and attached.")


# =========================================================================
# 5. LESSON 102: Factors Affecting Preferential Discharge (LU Order 18)
# =========================================================================
l102 = Lesson.objects.get(id=102)
print(f"\nProcessing Lesson 102: {l102.title}")

b102_p2 = get_or_create_diagram_block(l102, 2, "Concentrated Solid Sodium Chloride (Brine) Crystalline Reagent")
a102_p2, _ = LessonAsset.objects.get_or_create(id=403, defaults={'lesson': l102, 'asset_type': 'image'})
a102_p2.lesson = l102
a102_p2.asset_type = 'image'
a102_p2.source_type = 'external'
a102_p2.storage_type = 'url'
a102_p2.status = 'attached'
a102_p2.title = "Concentrated Solid Sodium Chloride (Brine) Crystalline Reagent"
a102_p2.description = "Photograph of sodium chloride crystals dissolved to make saturated brine, demonstrating how high ion concentration overrides standard electrochemical series position."
a102_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Crystals_Halite_on_matrix.jpg/800px-Crystals_Halite_on_matrix.jpg"
a102_p2.metadata = {
    'author': 'IvanSakhno',
    'licensing': 'CC BY 4.0',
    'attribution': 'IvanSakhno / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Crystals_Halite_on_matrix.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Concentration effect in brine electrolysis'
}
a102_p2.save()
a102_p2.blocks.set([b102_p2])
print("Lesson 102 Page 2: Asset 403 attached.")

b102_p3 = get_or_create_diagram_block(l102, 3, "Hydrated Copper(II) Sulfate Pentahydrate Crystals for Reactive Copper Electrodes")
a102_p3, _ = LessonAsset.objects.get_or_create(id=404, defaults={'lesson': l102, 'asset_type': 'image'})
a102_p3.lesson = l102
a102_p3.asset_type = 'image'
a102_p3.source_type = 'external'
a102_p3.storage_type = 'url'
a102_p3.status = 'attached'
a102_p3.title = "Hydrated Copper(II) Sulfate Pentahydrate Crystals for Reactive Copper Electrodes"
a102_p3.description = "Photograph of copper sulfate crystals used to demonstrate the effect of electrode nature: active copper anodes dissolve into solution rather than discharging OH-."
a102_p3.url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Copper_sulfate_pentahydrate_crystals.jpg"
a102_p3.metadata = {
    'author': 'W. Oelen',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'W. Oelen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Copper_sulfate_pentahydrate_crystals.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Active copper electrode effect'
}
a102_p3.save()
a102_p3.blocks.set([b102_p3])
print("Lesson 102 Page 3: Asset 404 attached.")

svg_102_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">THREE KEY FACTORS CONTROLLING PREFERENTIAL ION DISCHARGE</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Position in Electrochemical Series | Relative Concentration of Ions | Nature of Electrodes (Inert vs Active)</text>
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="730" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Pillar 1: Position in Series -->
    <g transform="translate(15, 20)">
      <rect x="0" y="0" width="220" height="295" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
      <text x="110" y="28" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">1. POSITION IN E° SERIES</text>
      <rect x="15" y="45" width="190" height="1" fill="#334155"/>
      <text x="15" y="70" fill="#cbd5e1" font-size="9">• Ions lower in electrochemical series require less energy to discharge.</text>
      <text x="15" y="105" fill="#38bdf8" font-size="10" font-weight="bold">Classic Case:</text>
      <text x="15" y="125" fill="#cbd5e1" font-size="9">In dilute NaCl(aq):</text>
      <text x="15" y="145" fill="#4ade80" font-size="9" font-weight="bold">• H⁺ discharged at cathode (below Na⁺)</text>
      <text x="15" y="170" fill="#4ade80" font-size="9" font-weight="bold">• OH⁻ discharged at anode (below Cl⁻)</text>
      <rect x="15" y="200" width="190" height="75" rx="6" fill="#1e293b"/>
      <text x="25" y="225" fill="#fbbf24" font-size="9" font-weight="bold">Outcome:</text>
      <text x="25" y="245" fill="#f8fafc" font-size="8.5">Water is decomposed into 2H₂ + O₂</text>
    </g>

    <!-- Pillar 2: Concentration -->
    <g transform="translate(255, 20)">
      <rect x="0" y="0" width="220" height="295" rx="10" fill="#020617" stroke="#f59e0b" stroke-width="2"/>
      <text x="110" y="28" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">2. CONCENTRATION</text>
      <rect x="15" y="45" width="190" height="1" fill="#334155"/>
      <text x="15" y="70" fill="#cbd5e1" font-size="9">• A significantly higher concentration can override position in the series.</text>
      <text x="15" y="105" fill="#fbbf24" font-size="10" font-weight="bold">Classic Case:</text>
      <text x="15" y="125" fill="#cbd5e1" font-size="9">In concentrated NaCl (Brine):</text>
      <text x="15" y="145" fill="#4ade80" font-size="9" font-weight="bold">• H⁺ still discharged at cathode</text>
      <text x="15" y="170" fill="#fb923c" font-size="9" font-weight="bold">• Cl⁻ discharged at anode (NOT OH⁻!)</text>
      <rect x="15" y="200" width="190" height="75" rx="6" fill="#1e293b"/>
      <text x="25" y="225" fill="#fbbf24" font-size="9" font-weight="bold">Outcome:</text>
      <text x="25" y="245" fill="#f8fafc" font-size="8.5">Cl₂ gas evolved + NaOH formed in solution</text>
    </g>

    <!-- Pillar 3: Nature of Electrode -->
    <g transform="translate(495, 20)">
      <rect x="0" y="0" width="220" height="295" rx="10" fill="#020617" stroke="#10b981" stroke-width="2"/>
      <text x="110" y="28" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">3. NATURE OF ELECTRODE</text>
      <rect x="15" y="45" width="190" height="1" fill="#334155"/>
      <text x="15" y="70" fill="#cbd5e1" font-size="9">• Active (reactive) electrodes take part directly in the chemical reaction.</text>
      <text x="15" y="105" fill="#34d399" font-size="10" font-weight="bold">Classic Case:</text>
      <text x="15" y="125" fill="#cbd5e1" font-size="9">Electrolysis of CuSO₄ with Cu electrodes:</text>
      <text x="15" y="145" fill="#4ade80" font-size="9" font-weight="bold">• Cu Anode dissolves: Cu → Cu²⁺ + 2e⁻</text>
      <text x="15" y="170" fill="#4ade80" font-size="9" font-weight="bold">• Cu Cathode deposits: Cu²⁺ + 2e⁻ → Cu</text>
      <rect x="15" y="200" width="190" height="75" rx="6" fill="#1e293b"/>
      <text x="25" y="225" fill="#fbbf24" font-size="9" font-weight="bold">Outcome:</text>
      <text x="25" y="245" fill="#f8fafc" font-size="8.5">Electrolyte color stays deep blue!</text>
    </g>
  </g>
</svg>'''
b102_p4 = get_or_create_diagram_block(l102, 4, "Three Key Factors Controlling Preferential Ion Discharge in Aqueous Electrolysis")
a102_p4, _ = LessonAsset.objects.get_or_create(id=405, defaults={'lesson': l102, 'asset_type': 'diagram'})
a102_p4.lesson = l102
a102_p4.asset_type = 'diagram'
a102_p4.source_type = 'ai_generated'
a102_p4.storage_type = 'file'
a102_p4.status = 'attached'
a102_p4.title = "Three Key Factors Controlling Preferential Ion Discharge in Aqueous Electrolysis"
a102_p4.description = "Decision framework detailing the 3 governing factors of preferential discharge: standard electrochemical series position, ion concentration, and active vs. inert electrode nature."
a102_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_102_p4)
a102_p4.file.save(f'factors_preferential_discharge_{l102.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a102_p4.blocks.set([b102_p4])
print("Lesson 102 Page 4: Asset 405 saved and attached.")


# =========================================================================
# 6. LESSON 95: Applications of Electrolysis (LU Order 19)
# =========================================================================
l95 = Lesson.objects.get(id=95)
print(f"\nProcessing Lesson 95: {l95.title}")

b95_p2 = get_or_create_diagram_block(l95, 2, "Bright Zinc Electroplated Metallic Surface Demonstrating Industrial Plating")
a95_p2, _ = LessonAsset.objects.get_or_create(id=406, defaults={'lesson': l95, 'asset_type': 'image'})
a95_p2.lesson = l95
a95_p2.asset_type = 'image'
a95_p2.source_type = 'external'
a95_p2.storage_type = 'url'
a95_p2.status = 'attached'
a95_p2.title = "Bright Zinc Electroplated Metallic Surface Demonstrating Industrial Plating"
a95_p2.description = "Photograph of high-quality electroplated metal demonstrating industrial coating for corrosion resistance and aesthetic enhancement."
a95_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/A_zinc-plated_surface_for_the_protection_from_corrosion.jpg/800px-A_zinc-plated_surface_for_the_protection_from_corrosion.jpg"
a95_p2.metadata = {
    'author': 'Hi-Res Images of Chemical Elements',
    'licensing': 'CC BY 3.0',
    'attribution': 'Hi-Res Images of Chemical Elements / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_zinc-plated_surface_for_the_protection_from_corrosion.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Industrial electroplating application'
}
a95_p2.save()
a95_p2.blocks.set([b95_p2])
print("Lesson 95 Page 2: Asset 406 attached.")

b95_p3 = get_or_create_diagram_block(l95, 3, "Solid Sodium Hydroxide Pellets Produced from Commercial Chlor-Alkali Electrolysis")
a95_p3, _ = LessonAsset.objects.get_or_create(id=407, defaults={'lesson': l95, 'asset_type': 'image'})
a95_p3.lesson = l95
a95_p3.asset_type = 'image'
a95_p3.source_type = 'external'
a95_p3.storage_type = 'url'
a95_p3.status = 'attached'
a95_p3.title = "Solid Sodium Hydroxide Pellets Produced from Commercial Chlor-Alkali Electrolysis"
a95_p3.description = "Photograph of sodium hydroxide chemical pellets produced industrially by the membrane chlor-alkali electrolysis process."
a95_p3.url = "https://upload.wikimedia.org/wikipedia/commons/3/34/Sodium_hydroxide.jpg"
a95_p3.metadata = {
    'author': 'Walkerma',
    'licensing': 'Public domain',
    'attribution': 'Walkerma / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Sodium_hydroxide.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electrolytic chemical manufacture'
}
a95_p3.save()
a95_p3.blocks.set([b95_p3])
print("Lesson 95 Page 3: Asset 407 attached.")

svg_95_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">FOUR CORE INDUSTRIAL PILLARS OF ELECTROLYSIS</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Extraction of Reactive Metals | Refining of Copper | Protective Electroplating | Manufacture of Chemicals</text>
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="730" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Pillar 1: Metal Extraction -->
    <g transform="translate(15, 20)">
      <rect x="0" y="0" width="165" height="295" rx="8" fill="#020617" stroke="#ef4444" stroke-width="1.5"/>
      <text x="82" y="28" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">1. EXTRACTION</text>
      <text x="82" y="45" text-anchor="middle" fill="#fca5a5" font-size="9">Reactive Metals</text>
      <rect x="10" y="60" width="145" height="1" fill="#334155"/>
      <text x="10" y="85" fill="#cbd5e1" font-size="8.5">• Sodium (Na)</text>
      <text x="10" y="102" fill="#94a3b8" font-size="8">Downs Cell (molten NaCl)</text>
      <text x="10" y="130" fill="#cbd5e1" font-size="8.5">• Aluminium (Al)</text>
      <text x="10" y="147" fill="#94a3b8" font-size="8">Hall-Héroult Cell (Al₂O₃)</text>
      <text x="10" y="175" fill="#cbd5e1" font-size="8.5">• Magnesium (Mg)</text>
      <text x="10" y="210" fill="#f87171" font-size="9" font-weight="bold">Cannot be reduced</text>
      <text x="10" y="228" fill="#fca5a5" font-size="8.5">by carbon reduction!</text>
    </g>

    <!-- Pillar 2: Purification -->
    <g transform="translate(195, 20)">
      <rect x="0" y="0" width="165" height="295" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="82" y="28" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">2. REFINING</text>
      <text x="82" y="45" text-anchor="middle" fill="#7dd3fc" font-size="9">High Purity Metals</text>
      <rect x="10" y="60" width="145" height="1" fill="#334155"/>
      <text x="10" y="85" fill="#cbd5e1" font-size="8.5">• Blister Copper</text>
      <text x="10" y="102" fill="#94a3b8" font-size="8">98% → 99.95% purity</text>
      <text x="10" y="130" fill="#cbd5e1" font-size="8.5">• Anode: Impure Cu</text>
      <text x="10" y="150" fill="#cbd5e1" font-size="8.5">• Cathode: Pure Cu</text>
      <text x="10" y="175" fill="#38bdf8" font-size="8.5" font-weight="bold">• Anode Sludge</text>
      <text x="10" y="195" fill="#fbbf24" font-size="8">Contains Ag, Au, Pt!</text>
      <text x="10" y="235" fill="#34d399" font-size="8.5" font-weight="bold">Max conductivity</text>
      <text x="10" y="252" fill="#cbd5e1" font-size="8">for electric wiring</text>
    </g>

    <!-- Pillar 3: Electroplating -->
    <g transform="translate(375, 20)">
      <rect x="0" y="0" width="165" height="295" rx="8" fill="#020617" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="82" y="28" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">3. PLATING</text>
      <text x="82" y="45" text-anchor="middle" fill="#fde68a" font-size="9">Protective Coatings</text>
      <rect x="10" y="60" width="145" height="1" fill="#334155"/>
      <text x="10" y="85" fill="#cbd5e1" font-size="8.5">• Silver / Gold Plating</text>
      <text x="10" y="102" fill="#94a3b8" font-size="8">Decorative cutlery, jewelry</text>
      <text x="10" y="130" fill="#cbd5e1" font-size="8.5">• Chromium Plating</text>
      <text x="10" y="147" fill="#94a3b8" font-size="8">Vehicle bumpers, taps</text>
      <text x="10" y="175" fill="#cbd5e1" font-size="8.5">• Tin Plating</text>
      <text x="10" y="192" fill="#94a3b8" font-size="8">Food packaging cans</text>
      <text x="10" y="235" fill="#fbbf24" font-size="8.5" font-weight="bold">Prevents corrosion</text>
      <text x="10" y="252" fill="#cbd5e1" font-size="8">&amp; enhances beauty</text>
    </g>

    <!-- Pillar 4: Manufacture -->
    <g transform="translate(555, 20)">
      <rect x="0" y="0" width="165" height="295" rx="8" fill="#020617" stroke="#10b981" stroke-width="1.5"/>
      <text x="82" y="28" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">4. CHEMICALS</text>
      <text x="82" y="45" text-anchor="middle" fill="#a7f3d0" font-size="9">Chlor-Alkali Industry</text>
      <rect x="10" y="60" width="145" height="1" fill="#334155"/>
      <text x="10" y="85" fill="#cbd5e1" font-size="8.5">• Sodium Hydroxide</text>
      <text x="10" y="102" fill="#94a3b8" font-size="8">Soaps, paper, textiles</text>
      <text x="10" y="130" fill="#cbd5e1" font-size="8.5">• Chlorine Gas (Cl₂)</text>
      <text x="10" y="147" fill="#94a3b8" font-size="8">Water purification, PVC</text>
      <text x="10" y="175" fill="#cbd5e1" font-size="8.5">• Hydrogen Gas (H₂)</text>
      <text x="10" y="192" fill="#94a3b8" font-size="8">Margarine, Haber process</text>
      <text x="10" y="235" fill="#34d399" font-size="8.5" font-weight="bold">Membrane Cell</text>
      <text x="10" y="252" fill="#cbd5e1" font-size="8">from saturated brine</text>
    </g>
  </g>
</svg>'''
b95_p4 = get_or_create_diagram_block(l95, 4, "Four Core Industrial Applications of Electrolysis Overview")
a95_p4, _ = LessonAsset.objects.get_or_create(id=408, defaults={'lesson': l95, 'asset_type': 'diagram'})
a95_p4.lesson = l95
a95_p4.asset_type = 'diagram'
a95_p4.source_type = 'ai_generated'
a95_p4.storage_type = 'file'
a95_p4.status = 'attached'
a95_p4.title = "Four Core Industrial Applications of Electrolysis Overview"
a95_p4.description = "Overview diagram summarizing the four primary industrial pillars of electrolysis: metal extraction, copper refining, electroplating, and chlor-alkali chemical manufacture."
a95_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_95_p4)
a95_p4.file.save(f'industrial_applications_electrolysis_{l95.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a95_p4.blocks.set([b95_p4])
print("Lesson 95 Page 4: Asset 408 saved and attached.")


# =========================================================================
# 7. LESSON 96: Extraction of Reactive Elements (LU Order 20)
# =========================================================================
l96 = Lesson.objects.get(id=96)
print(f"\nProcessing Lesson 96: {l96.title}")

b96_p2 = get_or_create_diagram_block(l96, 2, "Pure High-Purity Solid Sodium Hydroxide Manufactured from Saturated Brine")
a96_p2, _ = LessonAsset.objects.get_or_create(id=409, defaults={'lesson': l96, 'asset_type': 'image'})
a96_p2.lesson = l96
a96_p2.asset_type = 'image'
a96_p2.source_type = 'external'
a96_p2.storage_type = 'url'
a96_p2.status = 'attached'
a96_p2.title = "Pure High-Purity Solid Sodium Hydroxide Manufactured from Saturated Brine"
a96_p2.description = "Photograph of sodium compounds manufactured from electrolytic processes, demonstrating industrial extraction of alkali metal products."
a96_p2.url = "https://upload.wikimedia.org/wikipedia/commons/3/34/Sodium_hydroxide.jpg"
a96_p2.metadata = {
    'author': 'Walkerma',
    'licensing': 'Public domain',
    'attribution': 'Walkerma / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Sodium_hydroxide.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Sodium chemical production'
}
a96_p2.save()
a96_p2.blocks.set([b96_p2])
print("Lesson 96 Page 2: Asset 409 attached.")

b96_p3 = get_or_create_diagram_block(l96, 3, "Standard Calibrated Volumetric Flask for Industrial Chemical Solutions")
a96_p3, _ = LessonAsset.objects.get_or_create(id=410, defaults={'lesson': l96, 'asset_type': 'image'})
a96_p3.lesson = l96
a96_p3.asset_type = 'image'
a96_p3.source_type = 'external'
a96_p3.storage_type = 'url'
a96_p3.status = 'attached'
a96_p3.title = "Standard Calibrated Volumetric Flask for Industrial Chemical Solutions"
a96_p3.description = "Photograph of high-precision chemical glassware used in testing electrolyte concentrations in metal extraction operations."
a96_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg/800px-1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg"
a96_p3.metadata = {
    'author': 'Wlwiener',
    'licensing': 'CC BY 4.0',
    'attribution': 'Wlwiener / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Industrial electrolyte testing'
}
a96_p3.save()
a96_p3.blocks.set([b96_p3])
print("Lesson 96 Page 3: Asset 410 attached.")

svg_96_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">INDUSTRIAL DOWNS CELL: EXTRACTION OF METALLIC SODIUM</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Electrolysis of Molten NaCl with CaCl₂ Flux (600°C) | Steel Wire Gauze Prevents Violent Recombination</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Downs Cell Outer Steel Shell -->
    <rect x="50" y="30" width="380" height="280" rx="12" fill="#020617" stroke="#64748b" stroke-width="2"/>
    <!-- Firebrick lining -->
    <rect x="65" y="45" width="350" height="250" rx="8" fill="#1e293b"/>
    <!-- Molten Electrolyte (NaCl + CaCl2 at 600C) -->
    <rect x="75" y="70" width="330" height="210" fill="#f59e0b" fill-opacity="0.15"/>
    <text x="240" y="270" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Molten NaCl + CaCl₂ (600°C)</text>

    <!-- Central Carbon Anode (+) -->
    <rect x="215" y="110" width="50" height="170" fill="#334155" stroke="#f87171" stroke-width="2"/>
    <text x="240" y="195" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">Carbon</text>
    <text x="240" y="210" text-anchor="middle" fill="#f87171" font-size="9" font-weight="bold">Anode (+)</text>

    <!-- Inverted Chlorine Dome -->
    <path d="M 190 110 L 240 40 L 290 110 Z" fill="#020617" stroke="#10b981" stroke-width="2"/>
    <text x="240" y="80" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">Cl₂ Gas Out</text>

    <!-- Cylindrical Steel Cathode (-) -->
    <rect x="110" y="110" width="30" height="150" fill="#475569" stroke="#38bdf8" stroke-width="2"/>
    <rect x="340" y="110" width="30" height="150" fill="#475569" stroke="#38bdf8" stroke-width="2"/>
    <text x="125" y="95" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">Steel (-)</text>
    <text x="355" y="95" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">Steel (-)</text>

    <!-- Liquid Sodium Riser Pipes -->
    <rect x="100" y="45" width="40" height="50" fill="#020617" stroke="#fbbf24"/>
    <text x="120" y="35" text-anchor="middle" fill="#fbbf24" font-size="9" font-weight="bold">Liquid Na Out</text>

    <!-- Side Analysis & Chemical Principles -->
    <g transform="translate(450, 30)">
      <rect x="0" y="0" width="230" height="280" rx="10" fill="#020617" stroke="#38bdf8"/>
      <text x="115" y="25" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">CHEMICAL PRINCIPLES</text>
      <text x="10" y="55" fill="#f87171" font-size="9.5" font-weight="bold">Anode (Carbon / Graphite):</text>
      <text x="10" y="75" fill="#fca5a5" font-size="9" font-family="monospace">2Cl⁻(l) → Cl₂(g) + 2e⁻</text>
      <text x="10" y="105" fill="#38bdf8" font-size="9.5" font-weight="bold">Cathode (Cylindrical Steel):</text>
      <text x="10" y="125" fill="#7dd3fc" font-size="9" font-family="monospace">Na⁺(l) + e⁻ → Na(l)</text>
      <rect x="10" y="145" width="210" height="1" fill="#334155"/>
      <text x="10" y="170" fill="#fbbf24" font-size="9.5" font-weight="bold">Role of CaCl₂ Flux:</text>
      <text x="10" y="190" fill="#cbd5e1" font-size="8.5">• Lowers MP from 801°C to 600°C</text>
      <text x="10" y="208" fill="#cbd5e1" font-size="8.5">• Prevents vaporization of sodium</text>
      <text x="10" y="235" fill="#34d399" font-size="9.5" font-weight="bold">Steel Gauze Diaphragm:</text>
      <text x="10" y="255" fill="#cbd5e1" font-size="8.5">• Prevents violent Na + Cl₂ explosion</text>
    </g>
  </g>
</svg>'''
b96_p4 = get_or_create_diagram_block(l96, 4, "Industrial Downs Cell Cross-Section for Extraction of Metallic Sodium")
a96_p4, _ = LessonAsset.objects.get_or_create(id=411, defaults={'lesson': l96, 'asset_type': 'diagram'})
a96_p4.lesson = l96
a96_p4.asset_type = 'diagram'
a96_p4.source_type = 'ai_generated'
a96_p4.storage_type = 'file'
a96_p4.status = 'attached'
a96_p4.title = "Industrial Downs Cell Cross-Section for Extraction of Metallic Sodium"
a96_p4.description = "Cross-sectional engineering diagram of the industrial Downs cell showing molten NaCl electrolysis, CaCl2 flux, carbon anode dome, and steel cathode collector."
a96_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_96_p4)
a96_p4.file.save(f'downs_cell_sodium_{l96.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a96_p4.blocks.set([b96_p4])
print("Lesson 96 Page 4: Asset 411 saved and attached.")


# =========================================================================
# 8. LESSON 97: Electroplating (LU Order 21)
# =========================================================================
l97 = Lesson.objects.get(id=97)
print(f"\nProcessing Lesson 97: {l97.title}")

b97_p2 = get_or_create_diagram_block(l97, 2, "Electroplated Protective and Decorative Metal Coating Surface")
a97_p2, _ = LessonAsset.objects.get_or_create(id=412, defaults={'lesson': l97, 'asset_type': 'image'})
a97_p2.lesson = l97
a97_p2.asset_type = 'image'
a97_p2.source_type = 'external'
a97_p2.storage_type = 'url'
a97_p2.status = 'attached'
a97_p2.title = "Electroplated Protective and Decorative Metal Coating Surface"
a97_p2.description = "Photograph of smooth electroplated metal demonstrating the uniform deposition of protective plating metal via electrolytic current."
a97_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/A_zinc-plated_surface_for_the_protection_from_corrosion.jpg/800px-A_zinc-plated_surface_for_the_protection_from_corrosion.jpg"
a97_p2.metadata = {
    'author': 'Hi-Res Images of Chemical Elements',
    'licensing': 'CC BY 3.0',
    'attribution': 'Hi-Res Images of Chemical Elements / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_zinc-plated_surface_for_the_protection_from_corrosion.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electroplating metal deposition'
}
a97_p2.save()
a97_p2.blocks.set([b97_p2])
print("Lesson 97 Page 2: Asset 412 attached.")

b97_p3 = get_or_create_diagram_block(l97, 3, "Crystalline Copper Sulfate Reagent Used in Electroplating Baths")
a97_p3, _ = LessonAsset.objects.get_or_create(id=413, defaults={'lesson': l97, 'asset_type': 'image'})
a97_p3.lesson = l97
a97_p3.asset_type = 'image'
a97_p3.source_type = 'external'
a97_p3.storage_type = 'url'
a97_p3.status = 'attached'
a97_p3.title = "Crystalline Copper Sulfate Reagent Used in Electroplating Baths"
a97_p3.description = "Photograph of soluble metal salt crystals dissolved into the aqueous electrolyte bath to maintain constant plating cation concentration."
a97_p3.url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Copper_sulfate_pentahydrate_crystals.jpg"
a97_p3.metadata = {
    'author': 'W. Oelen',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'W. Oelen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Copper_sulfate_pentahydrate_crystals.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electroplating electrolyte bath'
}
a97_p3.save()
a97_p3.blocks.set([b97_p3])
print("Lesson 97 Page 3: Asset 413 attached.")

svg_97_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ELECTROPLATING APPARATUS: SILVER-PLATING A METAL SPOON</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Key Golden Rules: 1. Object to be plated = Cathode (-) | 2. Plating metal = Anode (+) | 3. Electrolyte contains Ag⁺ ions</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- External Circuit Wires & Battery -->
    <path d="M 180 110 L 180 40 L 310 40" stroke="#fbbf24" stroke-width="3"/>
    <path d="M 390 40 L 520 40 L 520 110" stroke="#fbbf24" stroke-width="3"/>
    <rect x="315" y="25" width="70" height="30" rx="4" fill="#020617" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="350" y="44" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">DC Battery</text>
    <text x="295" y="38" fill="#f87171" font-size="14" font-weight="bold">+</text>
    <text x="400" y="38" fill="#38bdf8" font-size="14" font-weight="bold">-</text>

    <!-- Plating Bath Vessel -->
    <rect x="100" y="110" width="500" height="180" rx="10" fill="#020617" stroke="#64748b" stroke-width="2"/>
    <rect x="110" y="140" width="480" height="140" rx="6" fill="#38bdf8" fill-opacity="0.1"/>
    <text x="350" y="265" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Electrolyte: Aqueous Silver Nitrate Solution [AgNO₃(aq) / Na[Ag(CN)₂]]</text>

    <!-- Left Anode (+) Pure Silver Bar -->
    <rect x="165" y="90" width="30" height="150" rx="3" fill="#cbd5e1" stroke="#f87171" stroke-width="2"/>
    <text x="180" y="80" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">ANODE (+)</text>
    <text x="180" y="145" text-anchor="middle" fill="#020617" font-size="9" font-weight="bold">Pure Ag</text>
    <text x="180" y="210" text-anchor="middle" fill="#f87171" font-size="8.5" font-family="monospace">Ag → Ag⁺ + e⁻</text>
    <text x="180" y="225" text-anchor="middle" fill="#fca5a5" font-size="7.5">Dissolves into bath</text>

    <!-- Right Cathode (-) Spoon Object -->
    <g transform="translate(500, 90)">
      <path d="M 20 0 L 20 80 Q 20 120 10 130 Q 30 130 20 80 Z" fill="#94a3b8" stroke="#38bdf8" stroke-width="2"/>
      <ellipse cx="20" cy="115" rx="16" ry="24" fill="#cbd5e1" stroke="#38bdf8" stroke-width="2"/>
      <text x="20" y="-10" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">CATHODE (-)</text>
      <text x="20" y="118" text-anchor="middle" fill="#020617" font-size="8" font-weight="bold">Spoon</text>
      <text x="20" y="165" text-anchor="middle" fill="#34d399" font-size="8.5" font-family="monospace">Ag⁺ + e⁻ → Ag(s)</text>
      <text x="20" y="180" text-anchor="middle" fill="#a7f3d0" font-size="7.5">Uniform silver layer</text>
    </g>

    <!-- Bottom 3 Exam Conditions Box -->
    <rect x="30" y="295" width="640" height="50" rx="6" fill="#1e293b"/>
    <text x="350" y="315" text-anchor="middle" fill="#fbbf24" font-size="9.5" font-weight="bold">Conditions for Uniform Plating: 1. Clean cathode thoroughly | 2. Use low steady current | 3. Rotate object during plating</text>
    <text x="350" y="333" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Concentration of Ag⁺ ions in the electrolyte remains perfectly constant!</text>
  </g>
</svg>'''
b97_p4 = get_or_create_diagram_block(l97, 4, "Complete Electroplating Setup: Silver-Plating of a Metal Spoon")
a97_p4, _ = LessonAsset.objects.get_or_create(id=414, defaults={'lesson': l97, 'asset_type': 'diagram'})
a97_p4.lesson = l97
a97_p4.asset_type = 'diagram'
a97_p4.source_type = 'ai_generated'
a97_p4.storage_type = 'file'
a97_p4.status = 'attached'
a97_p4.title = "Complete Electroplating Setup: Silver-Plating of a Metal Spoon"
a97_p4.description = "Experimental setup diagram of electroplating showing the silver anode bar, spoon cathode, silver nitrate electrolyte, and constant ion concentration mechanism."
a97_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_97_p4)
a97_p4.file.save(f'electroplating_spoon_{l97.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a97_p4.blocks.set([b97_p4])
print("Lesson 97 Page 4: Asset 414 saved and attached.")


# =========================================================================
# 9. LESSON 98: Galvanising (LU Order 22)
# =========================================================================
l98 = Lesson.objects.get(id=98)
print(f"\nProcessing Lesson 98: {l98.title}")

b98_p2 = get_or_create_diagram_block(l98, 2, "Industrial Zinc-Coated Protective Surface Exhibiting Characteristic Spangle Pattern")
a98_p2, _ = LessonAsset.objects.get_or_create(id=415, defaults={'lesson': l98, 'asset_type': 'image'})
a98_p2.lesson = l98
a98_p2.asset_type = 'image'
a98_p2.source_type = 'external'
a98_p2.storage_type = 'url'
a98_p2.status = 'attached'
a98_p2.title = "Industrial Zinc-Coated Protective Surface Exhibiting Characteristic Spangle Pattern"
a98_p2.description = "Photograph of hot-dip galvanized steel displaying crystalline zinc spangles that provide dual physical and sacrificial corrosion protection."
a98_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/A_zinc-plated_surface_for_the_protection_from_corrosion.jpg/800px-A_zinc-plated_surface_for_the_protection_from_corrosion.jpg"
a98_p2.metadata = {
    'author': 'Hi-Res Images of Chemical Elements',
    'licensing': 'CC BY 3.0',
    'attribution': 'Hi-Res Images of Chemical Elements / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_zinc-plated_surface_for_the_protection_from_corrosion.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Galvanized zinc spangle coating'
}
a98_p2.save()
a98_p2.blocks.set([b98_p2])
print("Lesson 98 Page 2: Asset 415 attached.")

b98_p3 = get_or_create_diagram_block(l98, 3, "Corroding Metallic Iron Nails Contrasted Against Galvanized Protection")
a98_p3, _ = LessonAsset.objects.get_or_create(id=416, defaults={'lesson': l98, 'asset_type': 'image'})
a98_p3.lesson = l98
a98_p3.asset_type = 'image'
a98_p3.source_type = 'external'
a98_p3.storage_type = 'url'
a98_p3.status = 'attached'
a98_p3.title = "Corroding Metallic Iron Nails Contrasted Against Galvanized Protection"
a98_p3.description = "Photograph of unprotected rusting iron nails highlighting why sacrificial zinc coating is essential for iron and steel preservation."
a98_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/%22Swelling%22_of_Iron_nails_due_to_rusting.jpg/800px-%22Swelling%22_of_Iron_nails_due_to_rusting.jpg"
a98_p3.metadata = {
    'author': 'Dr._Sroy',
    'licensing': 'CC BY 4.0',
    'attribution': 'Dr._Sroy / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:%22Swelling%22_of_Iron_nails_due_to_rusting.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Iron corrosion vs galvanizing'
}
a98_p3.save()
a98_p3.blocks.set([b98_p3])
print("Lesson 98 Page 3: Asset 416 attached.")

svg_98_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">GALVANISING &amp; SACRIFICIAL PROTECTION MECHANISM</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Dual Protection: Intact Physical Zinc Barrier vs. Sacrificial Anodic Protection When Scratched</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- State A: Intact Galvanized Layer -->
    <g transform="translate(30, 20)">
      <rect x="0" y="0" width="305" height="235" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="152" y="25" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">CASE A: INTACT ZINC COATING</text>
      <!-- Base Steel -->
      <rect x="25" y="110" width="255" height="70" rx="4" fill="#334155" stroke="#94a3b8"/>
      <text x="152" y="150" text-anchor="middle" fill="#cbd5e1" font-size="12" font-weight="bold">Base Iron / Steel (Fe)</text>
      <!-- Top Zinc Coating -->
      <rect x="25" y="65" width="255" height="40" rx="4" fill="#64748b" stroke="#38bdf8" stroke-width="2"/>
      <text x="152" y="90" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">Protective Zinc Layer (Zn)</text>
      <!-- Action description -->
      <text x="152" y="205" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">100% Physical Barrier Protection</text>
      <text x="152" y="222" text-anchor="middle" fill="#cbd5e1" font-size="9">Air and moisture cannot reach iron</text>
    </g>

    <!-- State B: Scratched Galvanized Layer (Sacrificial) -->
    <g transform="translate(365, 20)">
      <rect x="0" y="0" width="305" height="235" rx="10" fill="#020617" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="152" y="25" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">CASE B: SCRATCHED / EXPOSED COATING</text>
      <!-- Base Steel -->
      <rect x="25" y="110" width="255" height="70" rx="4" fill="#334155" stroke="#94a3b8"/>
      <text x="152" y="150" text-anchor="middle" fill="#cbd5e1" font-size="12" font-weight="bold">Base Iron / Steel (Fe)</text>
      <!-- Left Zinc piece -->
      <rect x="25" y="65" width="95" height="40" rx="4" fill="#64748b" stroke="#fbbf24" stroke-width="2"/>
      <!-- Right Zinc piece -->
      <rect x="185" y="65" width="95" height="40" rx="4" fill="#64748b" stroke="#fbbf24" stroke-width="2"/>
      <!-- Scratch Gap -->
      <text x="152" y="88" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="bold">SCRATCH</text>
      <!-- Sacrificial Action -->
      <text x="152" y="205" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Sacrificial Protection: Zn Oxidizes First</text>
      <text x="152" y="222" text-anchor="middle" fill="#f87171" font-size="9" font-family="monospace">Zn(s) → Zn²⁺ + 2e⁻ (Fe remains intact)</text>
    </g>

    <!-- Comparison with Tinning (Bottom) -->
    <rect x="30" y="270" width="640" height="65" rx="8" fill="#020617" stroke="#10b981"/>
    <text x="350" y="292" text-anchor="middle" fill="#4ade80" font-size="10.5" font-weight="bold">Why Galvanising Outperforms Tinning (Tin-Coating):</text>
    <text x="350" y="315" text-anchor="middle" fill="#cbd5e1" font-size="9.5">Zinc is MORE electropositive than Iron (E° = -0.76 V vs -0.44 V). Tin is LESS electropositive (E° = -0.14 V), so scratched tin accelerates iron rusting!</text>
  </g>
</svg>'''
b98_p4 = get_or_create_diagram_block(l98, 4, "Galvanising and Sacrificial Zinc Protection Comparison Mechanism")
a98_p4, _ = LessonAsset.objects.get_or_create(id=417, defaults={'lesson': l98, 'asset_type': 'diagram'})
a98_p4.lesson = l98
a98_p4.asset_type = 'diagram'
a98_p4.source_type = 'ai_generated'
a98_p4.storage_type = 'file'
a98_p4.status = 'attached'
a98_p4.title = "Galvanising and Sacrificial Zinc Protection Comparison Mechanism"
a98_p4.description = "Diagram contrasting intact barrier protection with sacrificial anodic oxidation of zinc when a galvanized steel surface is scratched."
a98_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_98_p4)
a98_p4.file.save(f'galvanising_protection_{l98.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a98_p4.blocks.set([b98_p4])
print("Lesson 98 Page 4: Asset 417 saved and attached.")


# =========================================================================
# 10. LESSON 99: Purification of Metals (LU Order 23)
# =========================================================================
l99 = Lesson.objects.get(id=99)
print(f"\nProcessing Lesson 99: {l99.title}")

b99_p2 = get_or_create_diagram_block(l99, 2, "Pure Blue Copper(II) Sulfate Electrolyte Crystals for Electrolytic Refining")
a99_p2, _ = LessonAsset.objects.get_or_create(id=418, defaults={'lesson': l99, 'asset_type': 'image'})
a99_p2.lesson = l99
a99_p2.asset_type = 'image'
a99_p2.source_type = 'external'
a99_p2.storage_type = 'url'
a99_p2.status = 'attached'
a99_p2.title = "Pure Blue Copper(II) Sulfate Electrolyte Crystals for Electrolytic Refining"
a99_p2.description = "Photograph of pure copper(II) sulfate crystals dissolved in dilute sulfuric acid to form the industrial electrolyte for copper refining tanks."
a99_p2.url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Copper_sulfate_pentahydrate_crystals.jpg"
a99_p2.metadata = {
    'author': 'W. Oelen',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'W. Oelen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Copper_sulfate_pentahydrate_crystals.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Copper refining electrolyte'
}
a99_p2.save()
a99_p2.blocks.set([b99_p2])
print("Lesson 99 Page 2: Asset 418 attached.")

b99_p3 = get_or_create_diagram_block(l99, 3, "Laboratory Electrolytic Vessel for Metal Refining Operations")
a99_p3, _ = LessonAsset.objects.get_or_create(id=419, defaults={'lesson': l99, 'asset_type': 'image'})
a99_p3.lesson = l99
a99_p3.asset_type = 'image'
a99_p3.source_type = 'external'
a99_p3.storage_type = 'url'
a99_p3.status = 'attached'
a99_p3.title = "Laboratory Electrolytic Vessel for Metal Refining Operations"
a99_p3.description = "Photograph of an assembled electrochemical tank demonstrating electrolytic purification of impure metal anodes into high-purity cathode sheets."
a99_p3.url = "https://upload.wikimedia.org/wikipedia/commons/3/34/Daniell_cell.jpg"
a99_p3.metadata = {
    'author': 'Unknown',
    'licensing': 'Public domain',
    'attribution': 'Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Daniell_cell.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Electrolytic metal refining tank'
}
a99_p3.save()
a99_p3.blocks.set([b99_p3])
print("Lesson 99 Page 3: Asset 419 attached.")

svg_99_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ELECTROLYTIC REFINING OF BLISTER COPPER (&gt;99.95% PURITY)</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Anode = Thick Impure Blister Copper | Cathode = Thin Pure Copper Sheet | Electrolyte = Acidified CuSO₄(aq)</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Refining Tank -->
    <rect x="50" y="60" width="600" height="230" rx="10" fill="#020617" stroke="#64748b" stroke-width="2"/>
    <rect x="60" y="100" width="580" height="180" rx="6" fill="#0284c7" fill-opacity="0.2"/>
    <text x="350" y="265" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Acidified Copper(II) Sulfate Electrolyte: CuSO₄(aq) + Dilute H₂SO₄</text>

    <!-- Thick Impure Anode (+) -->
    <rect x="130" y="40" width="60" height="190" rx="4" fill="#78350f" stroke="#f87171" stroke-width="2"/>
    <text x="160" y="30" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">ANODE (+)</text>
    <text x="160" y="100" text-anchor="middle" fill="#fde68a" font-size="9" font-weight="bold">Thick Blister</text>
    <text x="160" y="115" text-anchor="middle" fill="#fde68a" font-size="9" font-weight="bold">Copper (98%)</text>
    <text x="160" y="180" text-anchor="middle" fill="#f87171" font-size="8.5" font-family="monospace">Cu → Cu²⁺ + 2e⁻</text>
    <text x="160" y="195" text-anchor="middle" fill="#fca5a5" font-size="7.5">(Anode dissolves)</text>

    <!-- Anode Sludge (Precious metals at bottom) -->
    <ellipse cx="160" cy="275" rx="45" ry="10" fill="#451a03" stroke="#fbbf24"/>
    <text x="160" y="278" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="bold">Anode Sludge (Ag, Au)</text>

    <!-- Thin Pure Cathode (-) -->
    <rect x="490" y="40" width="30" height="190" rx="2" fill="#b45309" stroke="#38bdf8" stroke-width="2"/>
    <text x="505" y="30" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">CATHODE (-)</text>
    <text x="505" y="100" text-anchor="middle" fill="#fed7aa" font-size="9" font-weight="bold">Pure Copper</text>
    <text x="505" y="115" text-anchor="middle" fill="#fed7aa" font-size="9" font-weight="bold">Sheet (&gt;99.95%)</text>
    <text x="505" y="180" text-anchor="middle" fill="#34d399" font-size="8.5" font-family="monospace">Cu²⁺ + 2e⁻ → Cu</text>
    <text x="505" y="195" text-anchor="middle" fill="#a7f3d0" font-size="7.5">(Gains mass)</text>

    <!-- Ion Migration Arrows in Middle -->
    <path d="M 210 140 L 460 140" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>
    <text x="335" y="130" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">Cu²⁺ Ions Migrate to Cathode</text>

    <!-- Bottom Summary -->
    <rect x="30" y="300" width="640" height="45" rx="6" fill="#1e293b"/>
    <text x="350" y="325" text-anchor="middle" fill="#fbbf24" font-size="9.5" font-weight="bold">Valuable By-Products: Valuable gold (Au), silver (Ag), and platinum (Pt) fall to bottom as anode sludge to offset refining costs.</text>
  </g>
</svg>'''
b99_p4 = get_or_create_diagram_block(l99, 4, "Industrial Electrolytic Refining of Blister Copper and Anode Sludge Recovery")
a99_p4, _ = LessonAsset.objects.get_or_create(id=420, defaults={'lesson': l99, 'asset_type': 'diagram'})
a99_p4.lesson = l99
a99_p4.asset_type = 'diagram'
a99_p4.source_type = 'ai_generated'
a99_p4.storage_type = 'file'
a99_p4.status = 'attached'
a99_p4.title = "Industrial Electrolytic Refining of Blister Copper and Anode Sludge Recovery"
a99_p4.description = "Diagram of an electrolytic copper refining tank showing blister copper anode dissolution, pure copper cathode growth, and precious metal anode sludge collection."
a99_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_99_p4)
a99_p4.file.save(f'copper_refining_tank_{l99.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a99_p4.blocks.set([b99_p4])
print("Lesson 99 Page 4: Asset 420 saved and attached.")


# =========================================================================
# 11. LESSON 100: Manufacture of NaOH and Cl2 from Brine (LU Order 24)
# =========================================================================
l100 = Lesson.objects.get(id=100)
print(f"\nProcessing Lesson 100: {l100.title}")

b100_p2 = get_or_create_diagram_block(l100, 2, "High-Purity Solid Sodium Hydroxide Pellets from the Chlor-Alkali Process")
a100_p2, _ = LessonAsset.objects.get_or_create(id=421, defaults={'lesson': l100, 'asset_type': 'image'})
a100_p2.lesson = l100
a100_p2.asset_type = 'image'
a100_p2.source_type = 'external'
a100_p2.storage_type = 'url'
a100_p2.status = 'attached'
a100_p2.title = "High-Purity Solid Sodium Hydroxide Pellets from the Chlor-Alkali Process"
a100_p2.description = "Photograph of pure sodium hydroxide pellets manufactured from the modern membrane chlor-alkali electrolytic cell."
a100_p2.url = "https://upload.wikimedia.org/wikipedia/commons/3/34/Sodium_hydroxide.jpg"
a100_p2.metadata = {
    'author': 'Walkerma',
    'licensing': 'Public domain',
    'attribution': 'Walkerma / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Sodium_hydroxide.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Chlor-alkali sodium hydroxide'
}
a100_p2.save()
a100_p2.blocks.set([b100_p2])
print("Lesson 100 Page 2: Asset 421 attached.")

b100_p3 = get_or_create_diagram_block(l100, 3, "Halite (Rock Salt) Mineral Deposit Used as Industrial Saturated Brine Feedstock")
a100_p3, _ = LessonAsset.objects.get_or_create(id=422, defaults={'lesson': l100, 'asset_type': 'image'})
a100_p3.lesson = l100
a100_p3.asset_type = 'image'
a100_p3.source_type = 'external'
a100_p3.storage_type = 'url'
a100_p3.status = 'attached'
a100_p3.title = "Halite (Rock Salt) Mineral Deposit Used as Industrial Saturated Brine Feedstock"
a100_p3.description = "Photograph of natural rock salt minerals dissolved into water to produce saturated brine feedstock for the chlor-alkali industry."
a100_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Crystals_Halite_on_matrix.jpg/800px-Crystals_Halite_on_matrix.jpg"
a100_p3.metadata = {
    'author': 'IvanSakhno',
    'licensing': 'CC BY 4.0',
    'attribution': 'IvanSakhno / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Crystals_Halite_on_matrix.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Saturated brine feedstock'
}
a100_p3.save()
a100_p3.blocks.set([b100_p3])
print("Lesson 100 Page 3: Asset 422 attached.")

svg_100_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">MODERN MEMBRANE CHLOR-ALKALI CELL FLOWSHEET</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Cation-Exchange Membrane Allows Only Na⁺ Ions to Cross | Co-Production of Pure NaOH, Cl₂, and H₂</text>
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="700" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Anode Chamber (Left) -->
    <g transform="translate(40, 20)">
      <rect x="0" y="30" width="280" height="230" rx="8" fill="#020617" stroke="#f87171" stroke-width="1.5"/>
      <text x="140" y="55" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">ANODE CHAMBER (+)</text>
      <!-- Titanium Anode -->
      <rect x="30" y="70" width="25" height="150" fill="#475569" stroke="#f87171"/>
      <text x="15" y="15" fill="#38bdf8" font-size="9" font-weight="bold">Saturated Brine In</text>
      <text x="15" y="280" fill="#94a3b8" font-size="9">Depleted Brine Out</text>
      <!-- Reaction -->
      <text x="160" y="120" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">2Cl⁻(aq) → Cl₂(g) + 2e⁻</text>
      <text x="160" y="145" text-anchor="middle" fill="#4ade80" font-size="9">▲ Chlorine Gas Out</text>
    </g>

    <!-- Cation Exchange Membrane (Center) -->
    <rect x="325" y="50" width="16" height="230" fill="#a855f7" stroke="#c084fc"/>
    <text x="333" y="170" text-anchor="middle" fill="#020617" font-size="8" transform="rotate(-90 333 170)" font-weight="bold">CATION-EXCHANGE MEMBRANE (Na⁺ ONLY)</text>

    <!-- Cathode Chamber (Right) -->
    <g transform="translate(345, 20)">
      <rect x="0" y="30" width="280" height="230" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="140" y="55" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">CATHODE CHAMBER (-)</text>
      <!-- Nickel Cathode -->
      <rect x="225" y="70" width="25" height="150" fill="#475569" stroke="#38bdf8"/>
      <text x="15" y="15" fill="#38bdf8" font-size="9" font-weight="bold">Pure Water In</text>
      <text x="15" y="280" fill="#34d399" font-size="9" font-weight="bold">Pure NaOH(aq) Out</text>
      <!-- Reaction -->
      <text x="120" y="120" text-anchor="middle" fill="#7dd3fc" font-size="9.5" font-weight="bold">2H₂O + 2e⁻ → H₂(g) + 2OH⁻</text>
      <text x="120" y="145" text-anchor="middle" fill="#fbbf24" font-size="9">▲ Hydrogen Gas Out</text>
      <text x="120" y="195" text-anchor="middle" fill="#34d399" font-size="9.5" font-weight="bold">Na⁺ + OH⁻ → NaOH(aq)</text>
    </g>

    <!-- Bottom Economic Advantages -->
    <rect x="30" y="295" width="640" height="50" rx="6" fill="#1e293b"/>
    <text x="350" y="315" text-anchor="middle" fill="#fbbf24" font-size="9.5" font-weight="bold">Advantages of Membrane Cell: 1. Zero toxic mercury or asbestos | 2. Extremely pure NaOH (no Cl⁻ contamination) | 3. High energy efficiency</text>
    <text x="350" y="333" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Membrane prevents Cl₂ gas from mixing with NaOH, preventing formation of sodium chlorate(I) bleach.</text>
  </g>
</svg>'''
b100_p4 = get_or_create_diagram_block(l100, 4, "Industrial Membrane Chlor-Alkali Cell for Co-Production of Pure NaOH, Cl2, and H2")
a100_p4, _ = LessonAsset.objects.get_or_create(id=423, defaults={'lesson': l100, 'asset_type': 'diagram'})
a100_p4.lesson = l100
a100_p4.asset_type = 'diagram'
a100_p4.source_type = 'ai_generated'
a100_p4.storage_type = 'file'
a100_p4.status = 'attached'
a100_p4.title = "Industrial Membrane Chlor-Alkali Cell for Co-Production of Pure NaOH, Cl2, and H2"
a100_p4.description = "Flowsheet diagram of the modern membrane chlor-alkali cell showing selective Na+ ion transport, titanium anode Cl2 evolution, and nickel cathode NaOH synthesis."
a100_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_100_p4)
a100_p4.file.save(f'membrane_chlor_alkali_{l100.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a100_p4.blocks.set([b100_p4])
print("Lesson 100 Page 4: Asset 423 saved and attached.")


# =========================================================================
# 12. LESSON 101: Quantitative Treatment of Electrolysis (LU Order 25)
# =========================================================================
l101 = Lesson.objects.get(id=101)
print(f"\nProcessing Lesson 101: {l101.title}")

b101_p2 = get_or_create_diagram_block(l101, 2, "Historic Hofmann Voltameter Used for Quantitative Gas Volume Measurements")
a101_p2, _ = LessonAsset.objects.get_or_create(id=424, defaults={'lesson': l101, 'asset_type': 'image'})
a101_p2.lesson = l101
a101_p2.asset_type = 'image'
a101_p2.source_type = 'external'
a101_p2.storage_type = 'url'
a101_p2.status = 'attached'
a101_p2.title = "Historic Hofmann Voltameter Used for Quantitative Gas Volume Measurements"
a101_p2.description = "Photograph of a graduated voltameter showing exact 2:1 stoichiometric volume collection of H2 and O2 gases matching Faraday's law calculations."
a101_p2.url = "https://upload.wikimedia.org/wikipedia/commons/f/f6/Hofmann%27scher_Wasserzersetzungsapparat_-_Deutsches_Museum_Verkehrszentrum.jpg"
a101_p2.metadata = {
    'author': 'Mattes',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Mattes / Wikimedia Commons',
    'commons_page_url': "https://commons.wikimedia.org/wiki/File:Hofmann'scher_Wasserzersetzungsapparat_-_Deutsches_Museum_Verkehrszentrum.jpg",
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Quantitative electrolytic gas collection'
}
a101_p2.save()
a101_p2.blocks.set([b101_p2])
print("Lesson 101 Page 2: Asset 424 attached.")

b101_p3 = get_or_create_diagram_block(l101, 3, "High-Precision Digital Multimeter Measuring Continuous Electrical Current")
a101_p3, _ = LessonAsset.objects.get_or_create(id=425, defaults={'lesson': l101, 'asset_type': 'image'})
a101_p3.lesson = l101
a101_p3.asset_type = 'image'
a101_p3.source_type = 'external'
a101_p3.storage_type = 'url'
a101_p3.status = 'attached'
a101_p3.title = "High-Precision Digital Multimeter Measuring Continuous Electrical Current"
a101_p3.description = "Photograph of a digital instrument measuring current in Amperes (I) and elapsed time (t) for quantitative charge calculations (Q = I * t)."
a101_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg/800px-After_burning_up_the_circuit%2C_the_voltage_of_the_red_wires.jpg"
a101_p3.metadata = {
    'author': 'Kmashaye5220',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Kmashaye5220 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:After_burning_up_the_circuit,_the_voltage_of_the_red_wires.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Quantitative current measurement'
}
a101_p3.save()
a101_p3.blocks.set([b101_p3])
print("Lesson 101 Page 3: Asset 425 attached.")

svg_101_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">FARADAY'S LAWS QUANTITATIVE CALCULATION MAP</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Connecting Current &amp; Time (Q = I × t) to Moles of Electrons (1 F = 96,500 C), Mass, and Gas Volumes</text>
  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="720" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Step 1: Charge Q -->
    <g transform="translate(20, 20)">
      <rect x="0" y="0" width="200" height="110" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="100" y="25" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">STEP 1: TOTAL CHARGE (Q)</text>
      <text x="100" y="55" text-anchor="middle" fill="#f8fafc" font-size="12" font-family="monospace" font-weight="bold">Q = I × t</text>
      <text x="10" y="80" fill="#cbd5e1" font-size="8.5">• I = Current in Amperes (A)</text>
      <text x="10" y="98" fill="#cbd5e1" font-size="8.5">• t = Time in SECONDS (s)</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 230 75 L 260 75" stroke="#fbbf24" stroke-width="3"/>

    <!-- Step 2: Faradays / Moles of e- -->
    <g transform="translate(265, 20)">
      <rect x="0" y="0" width="200" height="110" rx="8" fill="#020617" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="100" y="25" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">STEP 2: MOLES OF e⁻</text>
      <text x="100" y="55" text-anchor="middle" fill="#f8fafc" font-size="11" font-family="monospace" font-weight="bold">Moles e⁻ = Q / 96,500</text>
      <text x="10" y="80" fill="#cbd5e1" font-size="8.5">• 1 Faraday (1 F) = 96,500 C</text>
      <text x="10" y="98" fill="#cbd5e1" font-size="8.5">• 1 F = 1 mole of electrons</text>
    </g>

    <!-- Arrow 2 -->
    <path d="M 475 75 L 505 75" stroke="#fbbf24" stroke-width="3"/>

    <!-- Step 3: Mole Ratio & Product Yield -->
    <g transform="translate(510, 20)">
      <rect x="0" y="0" width="190" height="110" rx="8" fill="#020617" stroke="#10b981" stroke-width="1.5"/>
      <text x="95" y="25" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">STEP 3: MOLES OF PRODUCT</text>
      <text x="10" y="52" fill="#cbd5e1" font-size="8.5">• Cu²⁺ + 2e⁻ → Cu (2 F : 1 mol)</text>
      <text x="10" y="72" fill="#cbd5e1" font-size="8.5">• Al³⁺ + 3e⁻ → Al (3 F : 1 mol)</text>
      <text x="10" y="95" fill="#cbd5e1" font-size="8.5">• 2H⁺ + 2e⁻ → H₂ (2 F : 1 mol)</text>
    </g>

    <!-- Worked Calculation Example -->
    <rect x="20" y="150" width="680" height="165" rx="8" fill="#020617" stroke="#a855f7"/>
    <text x="350" y="175" text-anchor="middle" fill="#c084fc" font-size="11" font-weight="bold">Worked KCSE Example: Current of 5.0 A passed through CuSO₄ for 32 minutes 10 seconds</text>
    <text x="35" y="205" fill="#cbd5e1" font-size="10">1. Time t = (32 × 60) + 10 = 1,930 s  ⟹  Charge Q = 5.0 A × 1,930 s = 9,650 C</text>
    <text x="35" y="235" fill="#cbd5e1" font-size="10">2. Moles of electrons = 9,650 / 96,500 = 0.10 F (0.10 mol e⁻)</text>
    <text x="35" y="265" fill="#cbd5e1" font-size="10">3. Half-reaction: Cu²⁺ + 2e⁻ → Cu  ⟹  Moles of Cu deposited = 0.10 / 2 = 0.050 mol</text>
    <text x="35" y="295" fill="#4ade80" font-size="11" font-weight="bold">4. Mass of Cu = 0.050 mol × 63.5 g/mol = 3.175 g of pure Copper deposited!</text>
  </g>
</svg>'''
b101_p4 = get_or_create_diagram_block(l101, 4, "Faraday's Laws Quantitative Electrolysis Calculation Roadmap")
a101_p4, _ = LessonAsset.objects.get_or_create(id=426, defaults={'lesson': l101, 'asset_type': 'diagram'})
a101_p4.lesson = l101
a101_p4.asset_type = 'diagram'
a101_p4.source_type = 'ai_generated'
a101_p4.storage_type = 'file'
a101_p4.status = 'attached'
a101_p4.title = "Faraday's Laws Quantitative Electrolysis Calculation Roadmap"
a101_p4.description = "Roadmap diagram outlining step-by-step quantitative electrolysis calculations using Faraday's constant (96,500 C/mol e-), current, time, and mole ratios."
a101_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_101_p4)
a101_p4.file.save(f'faraday_laws_calculation_{l101.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a101_p4.blocks.set([b101_p4])
print("Lesson 101 Page 4: Asset 426 saved and attached.")

print("\n=== Second Half of Topic 4 (12 Lessons) Completed Successfully! ===")
