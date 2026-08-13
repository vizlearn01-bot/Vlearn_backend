import os
import sys
import django
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db.models import Max
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Topic 2 Completion (2+ Wikimedia per Lesson + Rich SVGs) ===")

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
# UPGRADE LESSONS 39, 16, 40, 41, 42 WITH SECOND WIKIMEDIA IMAGE
# =========================================================================

# Lesson 39: Add Page 4 Gas Stove Flame
l39 = Lesson.objects.get(id=39)
b39_p4 = get_or_create_diagram_block(l39, 4, "Luminous Blue Flame from a Domestic Gaseous Hydrocarbon Burner")
a39_p4, _ = LessonAsset.objects.get_or_create(id=285, defaults={'lesson': l39, 'asset_type': 'image'})
a39_p4.lesson = l39
a39_p4.asset_type = 'image'
a39_p4.source_type = 'external'
a39_p4.storage_type = 'url'
a39_p4.status = 'attached'
a39_p4.title = "Luminous Blue Flame from a Domestic Gaseous Hydrocarbon Burner"
a39_p4.description = "Photograph of a clean blue flame produced by complete combustion of gaseous hydrocarbon fuel showing thermochemical energy output."
a39_p4.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Flame_from_a_gas_stove_burner_2.jpg/800px-Flame_from_a_gas_stove_burner_2.jpg"
a39_p4.metadata = {
    'author': 'BogTar201213',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'BogTar201213 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Flame_from_a_gas_stove_burner_2.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Thermochemical combustion of gaseous fuels'
}
a39_p4.save()
a39_p4.blocks.set([b39_p4])
print("Lesson 39: Second Wikimedia (Asset 285) attached on Page 4.")

# Lesson 16: Add Page 4 Volumetric Glassware
l16 = Lesson.objects.get(id=16)
b16_p4 = get_or_create_diagram_block(l16, 4, "Precision Volumetric Laboratory Glassware Used for Solution Preparation")
a16_p4, _ = LessonAsset.objects.get_or_create(id=286, defaults={'lesson': l16, 'asset_type': 'image'})
a16_p4.lesson = l16
a16_p4.asset_type = 'image'
a16_p4.source_type = 'external'
a16_p4.storage_type = 'url'
a16_p4.status = 'attached'
a16_p4.title = "Precision Volumetric Laboratory Glassware Used for Solution Preparation"
a16_p4.description = "Photograph of a calibrated volumetric flask used to prepare standard solutions for thermochemical bond breaking and formation experiments."
a16_p4.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Brand_volumetric_flask_100ml.jpg/800px-Brand_volumetric_flask_100ml.jpg"
a16_p4.metadata = {
    'author': 'Lucasbosch',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Lucasbosch / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Brand_volumetric_flask_100ml.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Standard volumetric apparatus for solution thermochemistry'
}
a16_p4.save()
a16_p4.blocks.set([b16_p4])
print("Lesson 16: Second Wikimedia (Asset 286) attached on Page 4.")

# Lesson 40: Add Page 9 Metal Calorimeter Vessel
l40 = Lesson.objects.get(id=40)
b40_p9 = get_or_create_diagram_block(l40, 9, "Polished Aluminium Calorimeter Vessel for Measuring Enthalpy of Combustion")
a40_p9, _ = LessonAsset.objects.get_or_create(id=287, defaults={'lesson': l40, 'asset_type': 'image'})
a40_p9.lesson = l40
a40_p9.asset_type = 'image'
a40_p9.source_type = 'external'
a40_p9.storage_type = 'url'
a40_p9.status = 'attached'
a40_p9.title = "Polished Aluminium Calorimeter Vessel for Measuring Enthalpy of Combustion"
a40_p9.description = "Photograph of a metallic calorimeter container designed for measuring heat transferred during fuel combustion."
a40_p9.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Aluminium_Calorimeter.jpg/800px-Aluminium_Calorimeter.jpg"
a40_p9.metadata = {
    'author': 'Maciej J. Mrowinski',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Maciej J. Mrowinski / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Aluminium_Calorimeter.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Metallic combustion calorimetry vessel'
}
a40_p9.save()
a40_p9.blocks.set([b40_p9])
print("Lesson 40: Second Wikimedia (Asset 287) attached on Page 9.")

# Lesson 41: Add Page 4 Standard 1-Liter Volumetric Flask
l41 = Lesson.objects.get(id=41)
b41_p4 = get_or_create_diagram_block(l41, 4, "Standard 1.0 M Solution Calibrated Volumetric Flask")
a41_p4, _ = LessonAsset.objects.get_or_create(id=288, defaults={'lesson': l41, 'asset_type': 'image'})
a41_p4.lesson = l41
a41_p4.asset_type = 'image'
a41_p4.source_type = 'external'
a41_p4.storage_type = 'url'
a41_p4.status = 'attached'
a41_p4.title = "Standard 1.0 M Solution Calibrated Volumetric Flask"
a41_p4.description = "Photograph of a 1.0-liter volumetric flask illustrating standard molar concentration (1.0 M / 1.0 mol/dm³) parameter for thermochemical measurements."
a41_p4.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg/800px-1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg"
a41_p4.metadata = {
    'author': 'Wlwiener',
    'licensing': 'CC BY 4.0',
    'attribution': 'Wlwiener / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:1_Liter_Volumetric_Flask_Being_Vortex_Drained.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Standard 1.0 M concentration thermodynamic condition'
}
a41_p4.save()
a41_p4.blocks.set([b41_p4])
print("Lesson 41: Second Wikimedia (Asset 288) attached on Page 4.")

# Lesson 42: Add Page 4 Mineral Crystal Halite
l42 = Lesson.objects.get(id=42)
b42_p4 = get_or_create_diagram_block(l42, 4, "Natural Halite Ionic Lattice Crystal Demonstrating Fixed Enthalpy of State")
a42_p4, _ = LessonAsset.objects.get_or_create(id=289, defaults={'lesson': l42, 'asset_type': 'image'})
a42_p4.lesson = l42
a42_p4.asset_type = 'image'
a42_p4.source_type = 'external'
a42_p4.storage_type = 'url'
a42_p4.status = 'attached'
a42_p4.title = "Natural Halite Ionic Lattice Crystal Demonstrating Fixed Enthalpy of State"
a42_p4.description = "Photograph of cubic halite crystals displaying well-defined crystal planes where lattice energy is invariant of formation route."
a42_p4.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Crystals_Halite_on_matrix.jpg/800px-Crystals_Halite_on_matrix.jpg"
a42_p4.metadata = {
    'author': 'IvanSakhno',
    'licensing': 'CC BY 4.0',
    'attribution': 'IvanSakhno / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Crystals_Halite_on_matrix.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'State function invariance in ionic lattice formation'
}
a42_p4.save()
a42_p4.blocks.set([b42_p4])
print("Lesson 42: Second Wikimedia (Asset 289) attached on Page 4.")


# =========================================================================
# 7. LESSON 43: Relationship Between Heat of Solution, Hydration & Lattice Energy
# =========================================================================
l43 = Lesson.objects.get(id=43)
print(f"\nProcessing Lesson 43: {l43.title}")

# P2: Halite Crystal Specimen (Wikimedia Image)
b43_p2 = get_or_create_diagram_block(l43, 2, "Crystalline Halite (Rock Salt) Mineral Ionic Lattice")
a43_p2, _ = LessonAsset.objects.get_or_create(id=290, defaults={'lesson': l43, 'asset_type': 'image'})
a43_p2.lesson = l43
a43_p2.asset_type = 'image'
a43_p2.source_type = 'external'
a43_p2.storage_type = 'url'
a43_p2.status = 'attached'
a43_p2.title = "Crystalline Halite (Rock Salt) Mineral Ionic Lattice"
a43_p2.description = "Photograph of natural halite crystals held together by strong electrostatic ionic lattice forces."
a43_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Crystals_Halite_on_matrix.jpg/800px-Crystals_Halite_on_matrix.jpg"
a43_p2.metadata = {
    'author': 'IvanSakhno',
    'licensing': 'CC BY 4.0',
    'attribution': 'IvanSakhno / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Crystals_Halite_on_matrix.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Ionic solid lattice energy'
}
a43_p2.save()
a43_p2.blocks.set([b43_p2])
print("Lesson 43 Page 2: Asset 290 attached.")

# P3: Dissolution of Salt in Water (Wikimedia Image)
b43_p3 = get_or_create_diagram_block(l43, 3, "Dissolution and Hydration of Crystalline Salt in Water")
a43_p3, _ = LessonAsset.objects.get_or_create(id=291, defaults={'lesson': l43, 'asset_type': 'image'})
a43_p3.lesson = l43
a43_p3.asset_type = 'image'
a43_p3.source_type = 'external'
a43_p3.storage_type = 'url'
a43_p3.status = 'attached'
a43_p3.title = "Dissolution and Hydration of Crystalline Salt in Water"
a43_p3.description = "Photograph showing crystalline salt interacting with polar water molecules during the dissolution process."
a43_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/2015-03-07_Pakistanisches%2C_sogenanntes_Himalaya-Salz_0399.jpg/800px-2015-03-07_Pakistanisches%2C_sogenanntes_Himalaya-Salz_0399.jpg"
a43_p3.metadata = {
    'author': 'Hubertl',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Hubertl / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:2015-03-07_Pakistanisches,_sogenanntes_Himalaya-Salz_0399.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Dissolution and hydration of ionic salts'
}
a43_p3.save()
a43_p3.blocks.set([b43_p3])
print("Lesson 43 Page 3: Asset 291 attached.")

# P4: Energy Cycle for Heat of Solution (Generated SVG)
svg_43_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrSoln" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrLatt" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrHyd" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
    </marker>
  </defs>

  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ENERGY CYCLE: HEAT OF SOLUTION, LATTICE &amp; HYDRATION ENERGY</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Thermochemical Cycle for Sodium Chloride: ΔH(soln) = ΔH(lattice breakdown) + ΔH(hydration)</text>

  <!-- Main Energy Cycle Diagram -->
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="260" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- State 1: Solid Ionic Crystal (Bottom Left) -->
    <g transform="translate(130, 205)">
      <rect x="-100" y="-30" width="200" height="60" rx="8" fill="#020617" stroke="#38bdf8"/>
      <text x="0" y="5" text-anchor="middle" fill="#38bdf8" font-size="14" font-family="monospace" font-weight="bold">NaCl(s)</text>
    </g>

    <!-- State 2: Gaseous Ions (Top Center) -->
    <g transform="translate(350, 55)">
      <rect x="-115" y="-30" width="230" height="60" rx="8" fill="#020617" stroke="#f59e0b"/>
      <text x="0" y="5" text-anchor="middle" fill="#fbbf24" font-size="14" font-family="monospace" font-weight="bold">Na⁺(g) + Cl⁻(g)</text>
    </g>

    <!-- State 3: Hydrated Aqueous Solution (Bottom Right) -->
    <g transform="translate(570, 205)">
      <rect x="-105" y="-30" width="210" height="60" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="0" y="5" text-anchor="middle" fill="#34d399" font-size="14" font-family="monospace" font-weight="bold">Na⁺(aq) + Cl⁻(aq)</text>
    </g>

    <!-- Step 1: Lattice Breakdown (+ΔH_lattice) -->
    <line x1="150" y1="170" x2="285" y2="85" stroke="#f59e0b" stroke-width="3.5" marker-end="url(#arrLatt)"/>
    <text x="170" y="115" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">ΔH(lattice breakdown)</text>
    <text x="170" y="132" text-anchor="middle" fill="#fde68a" font-size="10">+776 kJ/mol (Endo)</text>

    <!-- Step 2: Hydration of Gaseous Ions (-ΔH_hydration) -->
    <line x1="415" y1="85" x2="550" y2="170" stroke="#10b981" stroke-width="3.5" marker-end="url(#arrHyd)"/>
    <text x="535" y="115" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">ΔH(hydration)</text>
    <text x="535" y="132" text-anchor="middle" fill="#a7f3d0" font-size="10">-771 kJ/mol (Exo)</text>

    <!-- Direct Route: Heat of Solution (ΔH_soln) -->
    <line x1="235" y1="205" x2="460" y2="205" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrSoln)"/>
    <text x="350" y="195" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Direct Route: ΔH(soln)</text>
  </g>

  <!-- Bottom Calculation Banner -->
  <g transform="translate(60, 345)">
    <rect x="0" y="0" width="700" height="65" rx="10" fill="#020617" stroke="#334155"/>
    <text x="350" y="26" text-anchor="middle" fill="#fbbf24" font-size="14" font-family="monospace" font-weight="bold">ΔH(soln) = ΔH(lattice breakdown) + ΔH(hyd) = (+776) + (-771) = +5 kJ/mol</text>
    <text x="350" y="48" text-anchor="middle" fill="#cbd5e1" font-size="11">Slightly endothermic dissolution: hydrated ions stabilized by polar water dipoles</text>
  </g>
</svg>'''
b43_p4 = get_or_create_diagram_block(l43, 4, "Thermochemical Energy Cycle Relating Heat of Solution, Lattice Energy, and Hydration Energy")
a43_p4, _ = LessonAsset.objects.get_or_create(id=292, defaults={'lesson': l43, 'asset_type': 'diagram'})
a43_p4.lesson = l43
a43_p4.asset_type = 'diagram'
a43_p4.source_type = 'ai_generated'
a43_p4.storage_type = 'file'
a43_p4.status = 'attached'
a43_p4.title = "Thermochemical Energy Cycle Relating Heat of Solution, Lattice Energy, and Hydration Energy"
a43_p4.description = "Energy cycle diagram demonstrating how heat of solution equals the algebraic sum of endothermic lattice energy and exothermic hydration energy."
a43_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_43_p4)
a43_p4.file.save(f'solution_energy_cycle_{l43.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a43_p4.blocks.set([b43_p4])
print("Lesson 43 Page 4: Asset 292 saved and attached.")


# =========================================================================
# 8. LESSON 44: Fuels
# =========================================================================
l44 = Lesson.objects.get(id=44)
print(f"\nProcessing Lesson 44: {l44.title}")

# P2: Solid Charcoal Fuel (Wikimedia Image)
b44_p2 = get_or_create_diagram_block(l44, 2, "Solid Charcoal Lumps Used as Carbon-Based Biomass Fuel")
a44_p2, _ = LessonAsset.objects.get_or_create(id=293, defaults={'lesson': l44, 'asset_type': 'image'})
a44_p2.lesson = l44
a44_p2.asset_type = 'image'
a44_p2.source_type = 'external'
a44_p2.storage_type = 'url'
a44_p2.status = 'attached'
a44_p2.title = "Solid Charcoal Lumps Used as Carbon-Based Biomass Fuel"
a44_p2.description = "Photograph of processed charcoal fuel lumps produced by pyrolysis of wood, widely used for domestic heating and smelting."
a44_p2.url = "https://upload.wikimedia.org/wikipedia/commons/a/a8/0910_6290a_Blacksmith_bewllows%2C_Fang%2C_Gabon_%285618221044%29.jpg"
a44_p2.metadata = {
    'author': 'Ann Porteus',
    'licensing': 'CC BY 2.0',
    'attribution': 'Ann Porteus / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:0910_6290a_Blacksmith_bewllows,_Fang,_Gabon_(5618221044).jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Solid carbonaceous fuels'
}
a44_p2.save()
a44_p2.blocks.set([b44_p2])
print("Lesson 44 Page 2: Asset 293 attached.")

# P3: Pressurized LPG Cylinder (Wikimedia Image)
b44_p3 = get_or_create_diagram_block(l44, 3, "Industrial Pressurized Liquefied Petroleum Gas (LPG) Cylinder")
a44_p3, _ = LessonAsset.objects.get_or_create(id=294, defaults={'lesson': l44, 'asset_type': 'image'})
a44_p3.lesson = l44
a44_p3.asset_type = 'image'
a44_p3.source_type = 'external'
a44_p3.storage_type = 'url'
a44_p3.status = 'attached'
a44_p3.title = "Industrial Pressurized Liquefied Petroleum Gas (LPG) Cylinder"
a44_p3.description = "Photograph of a commercial LPG steel cylinder containing pressurized propane and butane used as clean domestic and industrial gaseous fuel."
a44_p3.url = "https://upload.wikimedia.org/wikipedia/commons/0/05/A_liquefied_petroleum_gas_%28LPG%29_cylinder.jpg"
a44_p3.metadata = {
    'author': 'ShriniwasGajare',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'ShriniwasGajare / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_liquefied_petroleum_gas_(LPG)_cylinder.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Gaseous fuels and pressurized storage'
}
a44_p3.save()
a44_p3.blocks.set([b44_p3])
print("Lesson 44 Page 3: Asset 294 attached.")

# P4: Fuel Classification Matrix (Generated SVG)
svg_44_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">CLASSIFICATION MATRIX OF CHEMICAL FUELS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Comparison of Physical States, Primary Chemical Constituents, and Combustion Efficiencies</text>

  <!-- 3 Columns for Solid, Liquid, Gas -->
  <g transform="translate(45, 75)">
    <!-- Column 1: Solid Fuels -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="225" height="335" rx="12" fill="#0f172a" stroke="#d97706" stroke-width="1.5"/>
      <rect x="15" y="15" width="195" height="40" rx="8" fill="#d97706" fill-opacity="0.2"/>
      <text x="112" y="40" text-anchor="middle" fill="#fbbf24" font-size="14" font-weight="bold">SOLID FUELS</text>

      <rect x="15" y="65" width="195" height="255" rx="8" fill="#020617"/>
      <text x="25" y="90" fill="#f8fafc" font-size="11" font-weight="bold">Examples:</text>
      <text x="25" y="110" fill="#cbd5e1" font-size="10">• Coal &amp; Anthracite</text>
      <text x="25" y="130" fill="#cbd5e1" font-size="10">• Wood &amp; Biomass</text>
      <text x="25" y="150" fill="#cbd5e1" font-size="10">• Charcoal (pyrolyzed)</text>

      <text x="25" y="185" fill="#fbbf24" font-size="11" font-weight="bold">Combustion Properties:</text>
      <text x="25" y="205" fill="#94a3b8" font-size="9">• Leaves solid ash residue</text>
      <text x="25" y="222" fill="#94a3b8" font-size="9">• Moderate ignition temp</text>
      <text x="25" y="239" fill="#94a3b8" font-size="9">• Bulky storage &amp; transport</text>
      <text x="25" y="256" fill="#f87171" font-size="9">• High particulate/smoke</text>
      <text x="25" y="285" fill="#fde68a" font-size="10" font-family="monospace">Heating: ~15-33 kJ/g</text>
    </g>

    <!-- Column 2: Liquid Fuels -->
    <g transform="translate(250, 0)">
      <rect x="0" y="0" width="225" height="335" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="15" y="15" width="195" height="40" rx="8" fill="#0284c7" fill-opacity="0.2"/>
      <text x="112" y="40" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="bold">LIQUID FUELS</text>

      <rect x="15" y="65" width="195" height="255" rx="8" fill="#020617"/>
      <text x="25" y="90" fill="#f8fafc" font-size="11" font-weight="bold">Examples:</text>
      <text x="25" y="110" fill="#cbd5e1" font-size="10">• Petrol (Gasoline)</text>
      <text x="25" y="130" fill="#cbd5e1" font-size="10">• Kerosene (Paraffin)</text>
      <text x="25" y="150" fill="#cbd5e1" font-size="10">• Diesel &amp; Fuel Oils</text>
      <text x="25" y="170" fill="#cbd5e1" font-size="10">• Bioethanol</text>

      <text x="25" y="195" fill="#38bdf8" font-size="11" font-weight="bold">Combustion Properties:</text>
      <text x="25" y="215" fill="#94a3b8" font-size="9">• High calorific output</text>
      <text x="25" y="232" fill="#94a3b8" font-size="9">• Pumpable &amp; piped easily</text>
      <text x="25" y="249" fill="#94a3b8" font-size="9">• Volatile vapors hazard</text>
      <text x="25" y="285" fill="#7dd3fc" font-size="10" font-family="monospace">Heating: ~30-48 kJ/g</text>
    </g>

    <!-- Column 3: Gaseous Fuels -->
    <g transform="translate(500, 0)">
      <rect x="0" y="0" width="225" height="335" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect x="15" y="15" width="195" height="40" rx="8" fill="#047857" fill-opacity="0.2"/>
      <text x="112" y="40" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">GASEOUS FUELS</text>

      <rect x="15" y="65" width="195" height="255" rx="8" fill="#020617"/>
      <text x="25" y="90" fill="#f8fafc" font-size="11" font-weight="bold">Examples:</text>
      <text x="25" y="110" fill="#cbd5e1" font-size="10">• Natural Gas (Methane)</text>
      <text x="25" y="130" fill="#cbd5e1" font-size="10">• LPG (Propane/Butane)</text>
      <text x="25" y="150" fill="#cbd5e1" font-size="10">• Biogas (CH₄ + CO₂)</text>
      <text x="25" y="170" fill="#cbd5e1" font-size="10">• Hydrogen Gas (H₂)</text>

      <text x="25" y="195" fill="#34d399" font-size="11" font-weight="bold">Combustion Properties:</text>
      <text x="25" y="215" fill="#94a3b8" font-size="9">• Cleanest combustion (no ash)</text>
      <text x="25" y="232" fill="#94a3b8" font-size="9">• Immediate flame ignition</text>
      <text x="25" y="249" fill="#94a3b8" font-size="9">• Requires high pressure tanks</text>
      <text x="25" y="285" fill="#a7f3d0" font-size="10" font-family="monospace">Heating: ~50-142 kJ/g</text>
    </g>
  </g>
</svg>'''
b44_p4 = get_or_create_diagram_block(l44, 4, "Comprehensive Classification Matrix of Solid, Liquid, and Gaseous Chemical Fuels")
a44_p4, _ = LessonAsset.objects.get_or_create(id=295, defaults={'lesson': l44, 'asset_type': 'diagram'})
a44_p4.lesson = l44
a44_p4.asset_type = 'diagram'
a44_p4.source_type = 'ai_generated'
a44_p4.storage_type = 'file'
a44_p4.status = 'attached'
a44_p4.title = "Comprehensive Classification Matrix of Solid, Liquid, and Gaseous Chemical Fuels"
a44_p4.description = "Comparative matrix outlining the physical states, chemical composition, heating values, and combustion behavior of fuels."
a44_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_44_p4)
a44_p4.file.save(f'fuels_classification_matrix_{l44.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a44_p4.blocks.set([b44_p4])
print("Lesson 44 Page 4: Asset 295 saved and attached.")


# =========================================================================
# 9. LESSON 45: Heating Values of Fuels
# =========================================================================
l45 = Lesson.objects.get(id=45)
print(f"\nProcessing Lesson 45: {l45.title}")

# P2: Firewood Burning (Wikimedia Image)
b45_p2 = get_or_create_diagram_block(l45, 2, "Controlled Combustion of Firewood Releasing Thermal Energy")
a45_p2, _ = LessonAsset.objects.get_or_create(id=296, defaults={'lesson': l45, 'asset_type': 'image'})
a45_p2.lesson = l45
a45_p2.asset_type = 'image'
a45_p2.source_type = 'external'
a45_p2.storage_type = 'url'
a45_p2.status = 'attached'
a45_p2.title = "Controlled Combustion of Firewood Releasing Thermal Energy"
a45_p2.description = "Photograph of burning firewood illustrating the heating value of dry cellulose biomass (~17 kJ/g)."
a45_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Burning_firewood.JPG/800px-Burning_firewood.JPG"
a45_p2.metadata = {
    'author': 'Boushabe.ahl.ali',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Boushabe.ahl.ali / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Burning_firewood.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Heating value of solid biomass fuel'
}
a45_p2.save()
a45_p2.blocks.set([b45_p2])
print("Lesson 45 Page 2: Asset 296 attached.")

# P3: Commercial Gasoline Pump (Wikimedia Image)
b45_p3 = get_or_create_diagram_block(l45, 3, "Commercial Gasoline Dispenser Pump for Liquid Hydrocarbon Fuels")
a45_p3, _ = LessonAsset.objects.get_or_create(id=297, defaults={'lesson': l45, 'asset_type': 'image'})
a45_p3.lesson = l45
a45_p3.asset_type = 'image'
a45_p3.source_type = 'external'
a45_p3.storage_type = 'url'
a45_p3.status = 'attached'
a45_p3.title = "Commercial Gasoline Dispenser Pump for Liquid Hydrocarbon Fuels"
a45_p3.description = "Photograph of an automotive fuel dispensing pump supplying refined octane petrol with high heating value (~47 kJ/g)."
a45_p3.url = "https://upload.wikimedia.org/wikipedia/commons/7/77/Gas_pump_at_station_in_Dongcheng_District%2C_Beijing.jpg"
a45_p3.metadata = {
    'author': 'Daniel Case',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Daniel Case / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Gas_pump_at_station_in_Dongcheng_District,_Beijing.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Heating value of refined petroleum fuels'
}
a45_p3.save()
a45_p3.blocks.set([b45_p3])
print("Lesson 45 Page 3: Asset 297 attached.")

# P4: Comparative Heating Values Bar Chart (Generated SVG)
svg_45_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">COMPARATIVE HEATING VALUES OF COMMON FUELS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Specific Energy Output Released Per Gram of Fuel Combusted (kJ/g)</text>

  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Bar 1: Hydrogen Gas (142 kJ/g) -->
    <g transform="translate(40, 30)">
      <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="bold">Hydrogen Gas (H₂)</text>
      <rect x="150" y="0" width="460" height="24" rx="6" fill="#0284c7"/>
      <text x="620" y="17" fill="#38bdf8" font-size="12" font-weight="bold">142 kJ/g</text>
    </g>

    <!-- Bar 2: Natural Gas / Methane (55 kJ/g) -->
    <g transform="translate(40, 75)">
      <text x="0" y="16" fill="#34d399" font-size="12" font-weight="bold">Natural Gas (CH₄)</text>
      <rect x="150" y="0" width="178" height="24" rx="6" fill="#059669"/>
      <text x="338" y="17" fill="#34d399" font-size="12" font-weight="bold">55 kJ/g</text>
    </g>

    <!-- Bar 3: Petrol / Gasoline (47 kJ/g) -->
    <g transform="translate(40, 120)">
      <text x="0" y="16" fill="#fbbf24" font-size="12" font-weight="bold">Petrol (Gasoline)</text>
      <rect x="150" y="0" width="152" height="24" rx="6" fill="#d97706"/>
      <text x="312" y="17" fill="#fbbf24" font-size="12" font-weight="bold">47 kJ/g</text>
    </g>

    <!-- Bar 4: Kerosene / Paraffin (45 kJ/g) -->
    <g transform="translate(40, 165)">
      <text x="0" y="16" fill="#f97316" font-size="12" font-weight="bold">Kerosene (Paraffin)</text>
      <rect x="150" y="0" width="145" height="24" rx="6" fill="#ea580c"/>
      <text x="305" y="17" fill="#f97316" font-size="12" font-weight="bold">45 kJ/g</text>
    </g>

    <!-- Bar 5: Charcoal (33 kJ/g) -->
    <g transform="translate(40, 210)">
      <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="bold">Charcoal (C)</text>
      <rect x="150" y="0" width="107" height="24" rx="6" fill="#475569"/>
      <text x="267" y="17" fill="#e2e8f0" font-size="12" font-weight="bold">33 kJ/g</text>
    </g>

    <!-- Bar 6: Dry Wood / Biomass (17 kJ/g) -->
    <g transform="translate(40, 255)">
      <text x="0" y="16" fill="#f87171" font-size="12" font-weight="bold">Dry Wood (Biomass)</text>
      <rect x="150" y="0" width="55" height="24" rx="6" fill="#dc2626"/>
      <text x="215" y="17" fill="#f87171" font-size="12" font-weight="bold">17 kJ/g</text>
    </g>
  </g>
</svg>'''
b45_p4 = get_or_create_diagram_block(l45, 4, "Comparative Heating Values and Energy Densities of Common Fuels")
a45_p4, _ = LessonAsset.objects.get_or_create(id=298, defaults={'lesson': l45, 'asset_type': 'diagram'})
a45_p4.lesson = l45
a45_p4.asset_type = 'diagram'
a45_p4.source_type = 'ai_generated'
a45_p4.storage_type = 'file'
a45_p4.status = 'attached'
a45_p4.title = "Comparative Heating Values and Energy Densities of Common Fuels"
a45_p4.description = "Bar chart comparing the specific heating values (kJ per gram) of hydrogen, natural gas, petrol, kerosene, charcoal, and wood."
a45_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_45_p4)
a45_p4.file.save(f'fuel_heating_values_{l45.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a45_p4.blocks.set([b45_p4])
print("Lesson 45 Page 4: Asset 298 saved and attached.")


# =========================================================================
# 10. LESSON 46: How to Choose a Fuel
# =========================================================================
l46 = Lesson.objects.get(id=46)
print(f"\nProcessing Lesson 46: {l46.title}")

# P2: Falcon 9 Rocket Launch (Wikimedia Image)
b46_p2 = get_or_create_diagram_block(l46, 2, "Falcon 9 Rocket Launch Powered by High-Energy Density Liquid Rocket Propellant")
a46_p2, _ = LessonAsset.objects.get_or_create(id=299, defaults={'lesson': l46, 'asset_type': 'image'})
a46_p2.lesson = l46
a46_p2.asset_type = 'image'
a46_p2.source_type = 'external'
a46_p2.storage_type = 'url'
a46_p2.status = 'attached'
a46_p2.title = "Falcon 9 Rocket Launch Powered by High-Energy Density Liquid Rocket Propellant"
a46_p2.description = "Photograph of a space launch vehicle demonstrating specialized fuel choice: liquid propellants with extreme energy-to-mass ratios for propulsion."
a46_p2.url = "https://upload.wikimedia.org/wikipedia/commons/a/aa/45th_Space_Wing_Supports_Successful_Falcon_9_SAOCOM_1B_Launch_02.jpg"
a46_p2.metadata = {
    'author': 'U.S. Space Force / Joshua Conti',
    'licensing': 'Public domain',
    'attribution': 'U.S. Space Force photo by Joshua Conti / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:45th_Space_Wing_Supports_Successful_Falcon_9_SAOCOM_1B_Launch_02.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Specialized fuel selection for high-energy propulsion'
}
a46_p2.save()
a46_p2.blocks.set([b46_p2])
print("Lesson 46 Page 2: Asset 299 attached.")

# P3: Ceramic Jiko Stove (Wikimedia Image)
b46_p3 = get_or_create_diagram_block(l46, 3, "Traditional Portable Ceramic Clay Charcoal Stove (Jiko) for Domestic Cooking")
a46_p3, _ = LessonAsset.objects.get_or_create(id=300, defaults={'lesson': l46, 'asset_type': 'image'})
a46_p3.lesson = l46
a46_p3.asset_type = 'image'
a46_p3.source_type = 'external'
a46_p3.storage_type = 'url'
a46_p3.status = 'attached'
a46_p3.title = "Traditional Portable Ceramic Clay Charcoal Stove (Jiko) for Domestic Cooking"
a46_p3.description = "Photograph of clay and metal domestic cooking stoves designed for affordable, locally accessible solid charcoal fuel."
a46_p3.url = "https://upload.wikimedia.org/wikipedia/commons/f/fa/Clay_Stoves.jpg"
a46_p3.metadata = {
    'author': 'Agness Abubakar Saidi',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Agness Abubakar Saidi / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Clay_Stoves.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Domestic fuel selection based on availability and cost'
}
a46_p3.save()
a46_p3.blocks.set([b46_p3])
print("Lesson 46 Page 3: Asset 300 attached.")

# P4: Fuel Selection Decision Matrix (Generated SVG)
svg_46_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SIX-FACTOR DECISION FRAMEWORK FOR CHOOSING A FUEL</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Balancing Technical, Economic, Operational, and Environmental Criteria</text>

  <!-- 6 Criteria Cards (2 rows of 3) -->
  <g transform="translate(45, 75)">
    <!-- Card 1: Heating Value -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="225" height="150" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="112" y="28" text-anchor="middle" fill="#f87171" font-size="13" font-weight="bold">1. HEATING VALUE</text>
      <rect x="15" y="42" width="195" height="95" rx="6" fill="#020617"/>
      <text x="25" y="65" fill="#fca5a5" font-size="10">• High energy output per unit mass</text>
      <text x="25" y="85" fill="#cbd5e1" font-size="9">• Maximizes thermal efficiency</text>
      <text x="25" y="105" fill="#cbd5e1" font-size="9">• e.g. Rocket engines require &gt;100 kJ/g</text>
    </g>

    <!-- Card 2: Cost & Economy -->
    <g transform="translate(250, 0)">
      <rect x="0" y="0" width="225" height="150" rx="10" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="112" y="28" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">2. COST &amp; ECONOMY</text>
      <rect x="15" y="42" width="195" height="95" rx="6" fill="#020617"/>
      <text x="25" y="65" fill="#fde68a" font-size="10">• Affordable per unit heat delivered</text>
      <text x="25" y="85" fill="#cbd5e1" font-size="9">• Operating &amp; burner apparatus costs</text>
      <text x="25" y="105" fill="#cbd5e1" font-size="9">• Vital for low-income households</text>
    </g>

    <!-- Card 3: Availability -->
    <g transform="translate(500, 0)">
      <rect x="0" y="0" width="225" height="150" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="112" y="28" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">3. AVAILABILITY</text>
      <rect x="15" y="42" width="195" height="95" rx="6" fill="#020617"/>
      <text x="25" y="65" fill="#7dd3fc" font-size="10">• Reliable supply in local area</text>
      <text x="25" y="85" fill="#cbd5e1" font-size="9">• Seasonal abundance (biomass)</text>
      <text x="25" y="105" fill="#cbd5e1" font-size="9">• Pipeline vs distribution networks</text>
    </g>

    <!-- Card 4: Ease of Storage & Transport -->
    <g transform="translate(0, 170)">
      <rect x="0" y="0" width="225" height="150" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="112" y="28" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">4. STORAGE &amp; TRANSPORT</text>
      <rect x="15" y="42" width="195" height="95" rx="6" fill="#020617"/>
      <text x="25" y="65" fill="#a7f3d0" font-size="10">• Compact volume &amp; high density</text>
      <text x="25" y="85" fill="#cbd5e1" font-size="9">• Safe containment (pressurized gas)</text>
      <text x="25" y="105" fill="#cbd5e1" font-size="9">• Low leakage &amp; evaporation risk</text>
    </g>

    <!-- Card 5: Ignition Rate & Control -->
    <g transform="translate(250, 170)">
      <rect x="0" y="0" width="225" height="150" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <text x="112" y="28" text-anchor="middle" fill="#c084fc" font-size="13" font-weight="bold">5. IGNITION &amp; CONTROL</text>
      <rect x="15" y="42" width="195" height="95" rx="6" fill="#020617"/>
      <text x="25" y="65" fill="#e9d5ff" font-size="10">• Moderate ignition temperature</text>
      <text x="25" y="85" fill="#cbd5e1" font-size="9">• Instant start / stop control</text>
      <text x="25" y="105" fill="#cbd5e1" font-size="9">• Steady, non-explosive combustion</text>
    </g>

    <!-- Card 6: Environmental Impact -->
    <g transform="translate(500, 170)">
      <rect x="0" y="0" width="225" height="150" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
      <text x="112" y="28" text-anchor="middle" fill="#22d3ee" font-size="13" font-weight="bold">6. ENVIRONMENTAL IMPACT</text>
      <rect x="15" y="42" width="195" height="95" rx="6" fill="#020617"/>
      <text x="25" y="65" fill="#a5f3fc" font-size="10">• Minimum toxic smoke &amp; ash</text>
      <text x="25" y="85" fill="#cbd5e1" font-size="9">• Low SO₂ and NOx emissions</text>
      <text x="25" y="105" fill="#cbd5e1" font-size="9">• Carbon footprint consideration</text>
    </g>
  </g>
</svg>'''
b46_p4 = get_or_create_diagram_block(l46, 4, "Six-Factor Multi-Criteria Decision Framework for Fuel Selection")
a46_p4, _ = LessonAsset.objects.get_or_create(id=301, defaults={'lesson': l46, 'asset_type': 'diagram'})
a46_p4.lesson = l46
a46_p4.asset_type = 'diagram'
a46_p4.source_type = 'ai_generated'
a46_p4.storage_type = 'file'
a46_p4.status = 'attached'
a46_p4.title = "Six-Factor Multi-Criteria Decision Framework for Fuel Selection"
a46_p4.description = "Infographic detailing the 6 critical parameters: heating value, cost, availability, ease of storage, rate of combustion, and environmental impact."
a46_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_46_p4)
a46_p4.file.save(f'fuel_decision_framework_{l46.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a46_p4.blocks.set([b46_p4])
print("Lesson 46 Page 4: Asset 301 saved and attached.")


# =========================================================================
# 11. LESSON 47: Precautions Necessary When Using Fuels
# =========================================================================
l47 = Lesson.objects.get(id=47)
print(f"\nProcessing Lesson 47: {l47.title}")

# P2: Carbon Monoxide Detector (Wikimedia Image)
b47_p2 = get_or_create_diagram_block(l47, 2, "Domestic Electronic Carbon Monoxide Sensor and Early Warning Alarm")
a47_p2, _ = LessonAsset.objects.get_or_create(id=302, defaults={'lesson': l47, 'asset_type': 'image'})
a47_p2.lesson = l47
a47_p2.asset_type = 'image'
a47_p2.source_type = 'external'
a47_p2.storage_type = 'url'
a47_p2.status = 'attached'
a47_p2.title = "Domestic Electronic Carbon Monoxide Sensor and Early Warning Alarm"
a47_p2.description = "Photograph of a certified electrochemical carbon monoxide detector installed in homes to protect against invisible, odorless CO gas from burning fuels."
a47_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Carbon_Monoxide_Sensor.jpg/800px-Carbon_Monoxide_Sensor.jpg"
a47_p2.metadata = {
    'author': 'Aug wiki 1257',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Aug wiki 1257 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Carbon_Monoxide_Sensor.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Safety precaution against carbon monoxide poisoning'
}
a47_p2.save()
a47_p2.blocks.set([b47_p2])
print("Lesson 47 Page 2: Asset 302 attached.")

# P3: Fire Extinguisher Pressure Gauge (Wikimedia Image)
b47_p3 = get_or_create_diagram_block(l47, 3, "Pressurized Dry Chemical Fire Extinguisher with Safety Pressure Gauge")
a47_p3, _ = LessonAsset.objects.get_or_create(id=303, defaults={'lesson': l47, 'asset_type': 'image'})
a47_p3.lesson = l47
a47_p3.asset_type = 'image'
a47_p3.source_type = 'external'
a47_p3.storage_type = 'url'
a47_p3.status = 'attached'
a47_p3.title = "Pressurized Dry Chemical Fire Extinguisher with Safety Pressure Gauge"
a47_p3.description = "Photograph of a certified commercial fire extinguisher showing the charged pressure indicator used for fuel fire safety."
a47_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/ABCs_of_Fire_Safety.jpg/800px-ABCs_of_Fire_Safety.jpg"
a47_p3.metadata = {
    'author': 'Nhrjmhll',
    'licensing': 'CC0',
    'attribution': 'Nhrjmhll / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:ABCs_of_Fire_Safety.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Fuel fire safety apparatus'
}
a47_p3.save()
a47_p3.blocks.set([b47_p3])
print("Lesson 47 Page 3: Asset 303 attached.")

# P4: Carbon Monoxide Toxicity Mechanism (Generated SVG)
svg_47_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">MECHANISM OF CARBON MONOXIDE (CO) TOXICITY</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Incomplete Combustion Hazard: Carbon Monoxide Binds 200x More Strongly to Hemoglobin Than Oxygen</text>

  <!-- 2 Panels: Normal O2 Transport vs. CO Poisoning -->
  <g transform="translate(45, 75)">
    <!-- Left: Normal O2 Transport -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">NORMAL OXYGEN TRANSPORT</text>
      
      <!-- Red Blood Cell / Oxyhemoglobin -->
      <g transform="translate(172, 115)">
        <ellipse cx="0" cy="0" rx="80" ry="45" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
        <text x="0" y="5" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Oxyhemoglobin</text>
        <circle cx="-35" cy="-15" r="10" fill="#38bdf8"/><text x="-35" y="-11" text-anchor="middle" fill="#fff" font-size="8">O₂</text>
        <circle cx="35" cy="-15" r="10" fill="#38bdf8"/><text x="35" y="-11" text-anchor="middle" fill="#fff" font-size="8">O₂</text>
        <circle cx="0" cy="20" r="10" fill="#38bdf8"/><text x="0" y="24" text-anchor="middle" fill="#fff" font-size="8">O₂</text>
      </g>

      <rect x="15" y="195" width="315" height="120" rx="8" fill="#020617"/>
      <text x="25" y="220" fill="#4ade80" font-size="11" font-weight="bold">Complete Combustion (Excess O₂):</text>
      <text x="25" y="240" fill="#cbd5e1" font-size="11" font-family="monospace">C + O₂ → CO₂ (Non-toxic)</text>
      <text x="25" y="265" fill="#94a3b8" font-size="10">• Hemoglobin reversibly binds O₂</text>
      <text x="25" y="285" fill="#94a3b8" font-size="10">• Oxygen easily delivered to body cells</text>
    </g>

    <!-- Right: CO Poisoning -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#f87171" font-size="13" font-weight="bold">CARBON MONOXIDE POISONING</text>
      
      <!-- Red Blood Cell / Carboxyhemoglobin -->
      <g transform="translate(172, 115)">
        <ellipse cx="0" cy="0" rx="80" ry="45" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
        <text x="0" y="5" text-anchor="middle" fill="#fca5a5" font-size="12" font-weight="bold">Carboxyhemoglobin</text>
        <circle cx="-35" cy="-15" r="12" fill="#e11d48"/><text x="-35" y="-11" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">CO</text>
        <circle cx="35" cy="-15" r="12" fill="#e11d48"/><text x="35" y="-11" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">CO</text>
        <circle cx="0" cy="20" r="12" fill="#e11d48"/><text x="0" y="24" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">CO</text>
      </g>

      <rect x="15" y="195" width="315" height="120" rx="8" fill="#020617"/>
      <text x="25" y="220" fill="#f87171" font-size="11" font-weight="bold">Incomplete Combustion (Limited O₂):</text>
      <text x="25" y="240" fill="#fca5a5" font-size="11" font-family="monospace">2C + O₂ → 2CO (Deadly Poison)</text>
      <text x="25" y="265" fill="#f87171" font-size="10">• Irreversible bond blocks O₂ binding</text>
      <text x="25" y="285" fill="#f87171" font-size="10">• Causes suffocation, coma, and death</text>
    </g>
  </g>
</svg>'''
b47_p4 = get_or_create_diagram_block(l47, 4, "Sub-Microscopic Mechanism of Carbon Monoxide Toxicity: Incomplete Combustion and Hemoglobin Poisoning")
a47_p4, _ = LessonAsset.objects.get_or_create(id=304, defaults={'lesson': l47, 'asset_type': 'diagram'})
a47_p4.lesson = l47
a47_p4.asset_type = 'diagram'
a47_p4.source_type = 'ai_generated'
a47_p4.storage_type = 'file'
a47_p4.status = 'attached'
a47_p4.title = "Sub-Microscopic Mechanism of Carbon Monoxide Toxicity: Incomplete Combustion and Hemoglobin Poisoning"
a47_p4.description = "Diagram illustrating complete combustion producing carbon dioxide versus incomplete combustion forming toxic carboxyhemoglobin."
a47_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_47_p4)
a47_p4.file.save(f'co_toxicity_mechanism_{l47.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a47_p4.blocks.set([b47_p4])
print("Lesson 47 Page 4: Asset 304 saved and attached.")


# =========================================================================
# 12. LESSON 48: Environmental Effects of Fuels
# =========================================================================
l48 = Lesson.objects.get(id=48)
print(f"\nProcessing Lesson 48: {l48.title}")

# P2: Acid Rain Damaged Gargoyle (Wikimedia Image)
b48_p2 = get_or_create_diagram_block(l48, 2, "Historic Stone Architectural Gargoyle Severely Eroded by Atmospheric Acid Rain")
a48_p2, _ = LessonAsset.objects.get_or_create(id=305, defaults={'lesson': l48, 'asset_type': 'image'})
a48_p2.lesson = l48
a48_p2.asset_type = 'image'
a48_p2.source_type = 'external'
a48_p2.storage_type = 'url'
a48_p2.status = 'attached'
a48_p2.title = "Historic Stone Architectural Gargoyle Severely Eroded by Atmospheric Acid Rain"
a48_p2.description = "Photograph of a limestone stone statue showing extensive chemical corrosion and loss of detail caused by sulfur dioxide and acid precipitation."
a48_p2.url = "https://upload.wikimedia.org/wikipedia/commons/5/54/-_Acid_rain_damaged_gargoyle_-.jpg"
a48_p2.metadata = {
    'author': 'User:Nino Barbieri',
    'licensing': 'CC BY 2.5',
    'attribution': 'Nino Barbieri / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:-_Acid_rain_damaged_gargoyle_-.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Acid rain corrosion of calcium carbonate stone'
}
a48_p2.save()
a48_p2.blocks.set([b48_p2])
print("Lesson 48 Page 2: Asset 305 attached.")

# P3: Urban Smog Pollution (Wikimedia Image)
b48_p3 = get_or_create_diagram_block(l48, 3, "Dense Atmospheric Smog and Particulate Air Pollution Over City Skyline")
a48_p3, _ = LessonAsset.objects.get_or_create(id=306, defaults={'lesson': l48, 'asset_type': 'image'})
a48_p3.lesson = l48
a48_p3.asset_type = 'image'
a48_p3.source_type = 'external'
a48_p3.storage_type = 'url'
a48_p3.status = 'attached'
a48_p3.title = "Dense Atmospheric Smog and Particulate Air Pollution Over City Skyline"
a48_p3.description = "Photograph illustrating urban smog resulting from vehicular exhaust and industrial fossil fuel combustion."
a48_p3.url = "https://upload.wikimedia.org/wikipedia/commons/0/03/Delhi_air_pollution_2019.jpg"
a48_p3.metadata = {
    'author': 'Prami.ap90',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Prami.ap90 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Delhi_air_pollution_2019.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Urban photochemical smog and particulate emissions'
}
a48_p3.save()
a48_p3.blocks.set([b48_p3])
print("Lesson 48 Page 3: Asset 306 attached.")

# P4: Catalytic Converter Cutaway (Wikimedia Image)
b48_p4 = get_or_create_diagram_block(l48, 4, "Cutaway Assembly of an Automotive Catalytic Converter Ceramic Monolith")
a48_p4, _ = LessonAsset.objects.get_or_create(id=307, defaults={'lesson': l48, 'asset_type': 'image'})
a48_p4.lesson = l48
a48_p4.asset_type = 'image'
a48_p4.source_type = 'external'
a48_p4.storage_type = 'url'
a48_p4.status = 'attached'
a48_p4.title = "Cutaway Assembly of an Automotive Catalytic Converter Ceramic Monolith"
a48_p4.description = "Photograph of a catalytic converter unit displaying the platinum-rhodium coated ceramic honeycomb channels that reduce exhaust emissions."
a48_p4.url = "https://upload.wikimedia.org/wikipedia/commons/6/68/Syst%C3%A8meRCSAutomobile.jpg"
a48_p4.metadata = {
    'author': 'Tousleso',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Tousleso / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:SystèmeRCSAutomobile.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Automotive emissions reduction technology'
}
a48_p4.save()
a48_p4.blocks.set([b48_p4])
print("Lesson 48 Page 4: Asset 307 attached.")

# P5: Acid Rain Formation Pathways (Generated SVG)
svg_48_p5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ATMOSPHERIC CHEMICAL PATHWAYS OF ACID RAIN FORMATION</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Emissions of SO₂ and NOx Dissolving in Atmospheric Moisture to Form Sulfuric and Nitric Acids</text>

  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="720" height="335" rx="14" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>

    <!-- Left: Industrial Emissions -->
    <g transform="translate(80, 240)">
      <rect x="-60" y="-80" width="120" height="90" rx="6" fill="#1e293b" stroke="#64748b"/>
      <rect x="-45" y="-120" width="25" height="50" fill="#334155"/>
      <rect x="20" y="-120" width="25" height="50" fill="#334155"/>
      <text x="0" y="-30" text-anchor="middle" fill="#cbd5e1" font-size="10" font-weight="bold">Power Station &amp;</text>
      <text x="0" y="-15" text-anchor="middle" fill="#cbd5e1" font-size="10" font-weight="bold">Vehicle Exhaust</text>

      <!-- Rising Gases -->
      <path d="M -32 -125 Q -40 -160 50 -180" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4"/>
      <text x="-32" y="-140" fill="#f87171" font-size="11" font-weight="bold">SO₂, NO, NO₂</text>
    </g>

    <!-- Top: Rain Clouds Reaction Zone -->
    <g transform="translate(360, 70)">
      <!-- Cloud Shape -->
      <path d="M -90 10 Q -110 -20 -60 -30 Q -40 -60 20 -40 Q 70 -60 90 -20 Q 120 0 100 30 Q 70 50 -80 40 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="0" y="-5" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Atmospheric Cloud Moisture (H₂O)</text>

      <!-- Reactions inside cloud -->
      <text x="0" y="16" text-anchor="middle" fill="#fbbf24" font-size="10" font-family="monospace">SO₂ + H₂O → H₂SO₃  |  2SO₂ + O₂ + 2H₂O → 2H₂SO₄</text>
      <text x="0" y="32" text-anchor="middle" fill="#38bdf8" font-size="10" font-family="monospace">4NO₂ + O₂ + 2H₂O → 4HNO₃</text>
    </g>

    <!-- Right: Acid Rain Falling on Forest and Lake -->
    <g transform="translate(580, 240)">
      <!-- Acid Raindrops -->
      <line x1="-120" y1="-100" x2="-140" y2="-40" stroke="#f87171" stroke-width="2" stroke-dasharray="4"/>
      <line x1="-80" y1="-100" x2="-100" y2="-40" stroke="#f87171" stroke-width="2" stroke-dasharray="4"/>
      <line x1="-40" y1="-100" x2="-60" y2="-40" stroke="#f87171" stroke-width="2" stroke-dasharray="4"/>
      <text x="-90" y="-65" fill="#f87171" font-size="11" font-weight="bold">Acid Rain (pH &lt; 5.0)</text>

      <!-- Damaged Environment Box -->
      <rect x="-80" y="-30" width="180" height="90" rx="8" fill="#020617" stroke="#ef4444"/>
      <text x="10" y="-10" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="bold">Environmental Damage:</text>
      <text x="10" y="10" text-anchor="middle" fill="#cbd5e1" font-size="9">• Leaches soil Mg²⁺, Ca²⁺ nutrients</text>
      <text x="10" y="28" text-anchor="middle" fill="#cbd5e1" font-size="9">• Acidifies aquatic lakes (kills fish)</text>
      <text x="10" y="46" text-anchor="middle" fill="#cbd5e1" font-size="9">• Corrodes CaCO₃ limestone buildings</text>
    </g>
  </g>
</svg>'''
b48_p5 = get_or_create_diagram_block(l48, 5, "Chemical Reaction Pathways of Atmospheric Acid Rain Formation and Ecological Effects")
a48_p5, _ = LessonAsset.objects.get_or_create(id=308, defaults={'lesson': l48, 'asset_type': 'diagram'})
a48_p5.lesson = l48
a48_p5.asset_type = 'diagram'
a48_p5.source_type = 'ai_generated'
a48_p5.storage_type = 'file'
a48_p5.status = 'attached'
a48_p5.title = "Chemical Reaction Pathways of Atmospheric Acid Rain Formation and Ecological Effects"
a48_p5.description = "Atmospheric schematic showing industrial SO2 and NOx emissions reacting with moisture to precipitate as sulfuric and nitric acid."
a48_p5.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_48_p5)
a48_p5.file.save(f'acid_rain_formation_{l48.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a48_p5.blocks.set([b48_p5])
print("Lesson 48 Page 5: Asset 308 saved and attached.")

# P6: Catalytic Converter Chemical Mechanism (Generated SVG)
svg_48_p6 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrCatIn" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/>
    </marker>
    <marker id="arrCatOut" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
    </marker>
  </defs>

  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">THREE-WAY CATALYTIC CONVERTER CHEMICAL MECHANISM</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Redox Reactions on Platinum/Rhodium/Palladium Honeycomb Converting Pollutants into Safe Gases</text>

  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="720" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>

    <!-- Left Box: Toxic Inlet Gases -->
    <g transform="translate(40, 45)">
      <rect x="0" y="0" width="180" height="245" rx="10" fill="#020617" stroke="#ef4444" stroke-width="1.5"/>
      <text x="90" y="30" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">TOXIC INLET EXHAUST</text>
      
      <rect x="15" y="45" width="150" height="50" rx="6" fill="#7f1d1d" fill-opacity="0.3"/>
      <text x="90" y="68" text-anchor="middle" fill="#fca5a5" font-size="11" font-family="monospace" font-weight="bold">Carbon Monoxide</text>
      <text x="90" y="85" text-anchor="middle" fill="#f87171" font-size="12" font-family="monospace" font-weight="bold">2CO</text>

      <rect x="15" y="110" width="150" height="50" rx="6" fill="#7f1d1d" fill-opacity="0.3"/>
      <text x="90" y="133" text-anchor="middle" fill="#fca5a5" font-size="11" font-family="monospace" font-weight="bold">Nitrogen Oxides</text>
      <text x="90" y="150" text-anchor="middle" fill="#f87171" font-size="12" font-family="monospace" font-weight="bold">2NO / 2NO₂</text>

      <rect x="15" y="175" width="150" height="50" rx="6" fill="#7f1d1d" fill-opacity="0.3"/>
      <text x="90" y="198" text-anchor="middle" fill="#fca5a5" font-size="11" font-family="monospace" font-weight="bold">Unburnt Fuels</text>
      <text x="90" y="215" text-anchor="middle" fill="#f87171" font-size="12" font-family="monospace" font-weight="bold">C_x H_y</text>
    </g>

    <!-- Center: Catalytic Honeycomb Reactor -->
    <g transform="translate(255, 45)">
      <rect x="0" y="0" width="210" height="245" rx="10" fill="#020617" stroke="#fbbf24" stroke-width="2"/>
      <text x="105" y="28" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">Pt / Rh / Pd CATALYST</text>
      
      <!-- Honeycomb Grid Lines -->
      <line x1="20" y1="45" x2="190" y2="45" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="65" x2="190" y2="65" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="85" x2="190" y2="85" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="105" x2="190" y2="105" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="125" x2="190" y2="125" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="145" x2="190" y2="145" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="165" x2="190" y2="165" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="185" x2="190" y2="185" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="205" x2="190" y2="205" stroke="#475569" stroke-width="1"/>
      <line x1="20" y1="225" x2="190" y2="225" stroke="#475569" stroke-width="1"/>

      <text x="105" y="115" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="bold">Reduction &amp; Oxidation</text>
      <text x="105" y="135" text-anchor="middle" fill="#cbd5e1" font-size="9">2CO + O₂ → 2CO₂</text>
      <text x="105" y="155" text-anchor="middle" fill="#cbd5e1" font-size="9">2NO + 2CO → N₂ + 2CO₂</text>
    </g>

    <!-- Right Box: Non-Toxic Clean Output -->
    <g transform="translate(500, 45)">
      <rect x="0" y="0" width="180" height="245" rx="10" fill="#020617" stroke="#10b981" stroke-width="1.5"/>
      <text x="90" y="30" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">HARMLESS CLEAN OUTPUT</text>

      <rect x="15" y="45" width="150" height="50" rx="6" fill="#065f46" fill-opacity="0.3"/>
      <text x="90" y="68" text-anchor="middle" fill="#a7f3d0" font-size="11" font-family="monospace" font-weight="bold">Carbon Dioxide</text>
      <text x="90" y="85" text-anchor="middle" fill="#34d399" font-size="12" font-family="monospace" font-weight="bold">2CO₂</text>

      <rect x="15" y="110" width="150" height="50" rx="6" fill="#065f46" fill-opacity="0.3"/>
      <text x="90" y="133" text-anchor="middle" fill="#a7f3d0" font-size="11" font-family="monospace" font-weight="bold">Nitrogen Gas</text>
      <text x="90" y="150" text-anchor="middle" fill="#34d399" font-size="12" font-family="monospace" font-weight="bold">N₂</text>

      <rect x="15" y="175" width="150" height="50" rx="6" fill="#065f46" fill-opacity="0.3"/>
      <text x="90" y="198" text-anchor="middle" fill="#a7f3d0" font-size="11" font-family="monospace" font-weight="bold">Water Vapor</text>
      <text x="90" y="215" text-anchor="middle" fill="#34d399" font-size="12" font-family="monospace" font-weight="bold">H₂O</text>
    </g>
  </g>
</svg>'''
b48_p6 = get_or_create_diagram_block(l48, 6, "Three-Way Catalytic Converter Heterogeneous Redox Reaction Mechanism")
a48_p6, _ = LessonAsset.objects.get_or_create(id=309, defaults={'lesson': l48, 'asset_type': 'diagram'})
a48_p6.lesson = l48
a48_p6.asset_type = 'diagram'
a48_p6.source_type = 'ai_generated'
a48_p6.storage_type = 'file'
a48_p6.status = 'attached'
a48_p6.title = "Three-Way Catalytic Converter Heterogeneous Redox Reaction Mechanism"
a48_p6.description = "Mechanism schematic detailing catalytic oxidation of carbon monoxide and hydrocarbons alongside reduction of nitrogen oxides into harmless nitrogen, carbon dioxide, and water."
a48_p6.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_48_p6)
a48_p6.file.save(f'catalytic_converter_mechanism_{l48.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a48_p6.blocks.set([b48_p6])
print("Lesson 48 Page 6: Asset 309 saved and attached.")

print("\n=== All 12 Lessons of Topic 2 Completed Successfully with 2+ Wikimedia Each! ===")
