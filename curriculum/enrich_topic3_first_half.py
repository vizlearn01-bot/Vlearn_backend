import os
import sys
import django
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db.models import Max
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Form 4 Topic 3: First Half (Lessons 63–69) ===")

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
# 1. LESSON 63: Reaction Rates
# =========================================================================
l63 = Lesson.objects.get(id=63)
print(f"\nProcessing Lesson 63: {l63.title}")

# P2: Gas Syringe (Wikimedia Image)
b63_p2 = get_or_create_diagram_block(l63, 2, "Laboratory Gas Syringe Apparatus for Measuring Gas Evolution Rates")
a63_p2, _ = LessonAsset.objects.get_or_create(id=310, defaults={'lesson': l63, 'asset_type': 'image'})
a63_p2.lesson = l63
a63_p2.asset_type = 'image'
a63_p2.source_type = 'external'
a63_p2.storage_type = 'url'
a63_p2.status = 'attached'
a63_p2.title = "Laboratory Gas Syringe Apparatus for Measuring Gas Evolution Rates"
a63_p2.description = "Photograph of a graduated 100 cm³ glass gas syringe used to measure the volume of gas produced over time in reaction rate experiments."
a63_p2.url = "https://upload.wikimedia.org/wikipedia/commons/f/f1/Gas_syringe.jpg"
a63_p2.metadata = {
    'author': 'User:Geni',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'User:Geni / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Gas_syringe.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Gas volume rate measurement apparatus'
}
a63_p2.save()
a63_p2.blocks.set([b63_p2])
print("Lesson 63 Page 2: Asset 310 attached.")

# P3: Effervescent Reaction (Wikimedia Image)
b63_p3 = get_or_create_diagram_block(l63, 3, "Vigorous Effervescence and Gas Generation in an Aqueous Reaction")
a63_p3, _ = LessonAsset.objects.get_or_create(id=311, defaults={'lesson': l63, 'asset_type': 'image'})
a63_p3.lesson = l63
a63_p3.asset_type = 'image'
a63_p3.source_type = 'external'
a63_p3.storage_type = 'url'
a63_p3.status = 'attached'
a63_p3.title = "Vigorous Effervescence and Gas Generation in an Aqueous Reaction"
a63_p3.description = "Photograph capturing rapid carbon dioxide gas evolution and bubble formation during an aqueous acid-carbonate reaction."
a63_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Alka-Seltzer_in_water_2.jpg/800px-Alka-Seltzer_in_water_2.jpg"
a63_p3.metadata = {
    'author': 'F Delventhal',
    'licensing': 'CC BY 2.0',
    'attribution': 'F Delventhal / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Alka-Seltzer_in_water_2.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Observable rate of gas evolution'
}
a63_p3.save()
a63_p3.blocks.set([b63_p3])
print("Lesson 63 Page 3: Asset 311 attached.")

# P4: Rate Graphs & Tangent Slope Determination (Generated SVG)
svg_63_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">REACTION RATE DETERMINATION: VOLUME VS. TIME GRAPH</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Calculating Instantaneous Reaction Rate from the Gradient of the Tangent (Rate = ΔV / Δt)</text>

  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Y Axis: Gas Volume -->
    <line x1="70" y1="280" x2="70" y2="40" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 65 48 L 70 38 L 75 48" fill="#94a3b8"/>
    <text x="50" y="160" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold" transform="rotate(-90 50 160)">Gas Volume (cm³)</text>

    <!-- X Axis: Time -->
    <line x1="70" y1="280" x2="620" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <text x="345" y="305" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Time (seconds)</text>

    <!-- Reaction Curve -->
    <path d="M 70 280 Q 150 110 320 80 L 600 80" fill="none" stroke="#38bdf8" stroke-width="3.5"/>

    <!-- Plateau Completion Line -->
    <line x1="70" y1="80" x2="600" y2="80" stroke="#64748b" stroke-dasharray="4"/>
    <text x="480" y="70" fill="#4ade80" font-size="11" font-weight="bold">Reaction Complete (Rate = 0)</text>

    <!-- Tangent Line at t = 60s -->
    <line x1="90" y1="240" x2="280" y2="100" stroke="#f59e0b" stroke-width="2.5"/>
    <circle cx="170" cy="180" r="5" fill="#fbbf24"/>
    <text x="190" y="175" fill="#fbbf24" font-size="11" font-weight="bold">Point P (t = 60s)</text>

    <!-- Triangle for Gradient Calculation -->
    <line x1="115" y1="220" x2="245" y2="220" stroke="#fbbf24" stroke-dasharray="3"/>
    <line x1="245" y1="220" x2="245" y2="125" stroke="#fbbf24" stroke-dasharray="3"/>
    <text x="255" y="175" fill="#fbbf24" font-size="10">ΔV = 45 cm³</text>
    <text x="180" y="235" text-anchor="middle" fill="#fbbf24" font-size="10">Δt = 60 s</text>

    <!-- Rate Stages Explanation Box -->
    <rect x="360" y="120" width="310" height="135" rx="8" fill="#020617" stroke="#334155"/>
    <text x="375" y="145" fill="#38bdf8" font-size="12" font-weight="bold">Key Rate Interpretation:</text>
    <text x="375" y="170" fill="#f87171" font-size="10">1. Initial Rate (t=0): Maximum gradient (steepest)</text>
    <text x="375" y="195" fill="#fbbf24" font-size="10">2. Rate Slows: Reactants consumed, collisions drop</text>
    <text x="375" y="220" fill="#4ade80" font-size="10">3. Final Rate (Curve flattens): Rate = 0 cm³/s</text>
    <text x="375" y="242" fill="#34d399" font-size="11" font-family="monospace" font-weight="bold">Rate = Gradient = ΔV / Δt = 0.75 cm³/s</text>
  </g>
</svg>'''
b63_p4 = get_or_create_diagram_block(l63, 4, "Determination of Instantaneous Reaction Rate from Volume-Time Gradient")
a63_p4, _ = LessonAsset.objects.get_or_create(id=312, defaults={'lesson': l63, 'asset_type': 'diagram'})
a63_p4.lesson = l63
a63_p4.asset_type = 'diagram'
a63_p4.source_type = 'ai_generated'
a63_p4.storage_type = 'file'
a63_p4.status = 'attached'
a63_p4.title = "Determination of Instantaneous Reaction Rate from Volume-Time Gradient"
a63_p4.description = "Graph showing reaction progress over time and calculation of instantaneous rate using tangent line gradient."
a63_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_63_p4)
a63_p4.file.save(f'reaction_rate_tangent_{l63.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a63_p4.blocks.set([b63_p4])
print("Lesson 63 Page 4: Asset 312 saved and attached.")


# =========================================================================
# 2. LESSON 64: Collision Theory and Activation Energy
# =========================================================================
l64 = Lesson.objects.get(id=64)
print(f"\nProcessing Lesson 64: {l64.title}")

# P2: Flame Providing Activation Energy (Wikimedia Image)
b64_p2 = get_or_create_diagram_block(l64, 2, "Laboratory Burner Flame Supplying Kinetic Activation Energy to Reactants")
a64_p2, _ = LessonAsset.objects.get_or_create(id=313, defaults={'lesson': l64, 'asset_type': 'image'})
a64_p2.lesson = l64
a64_p2.asset_type = 'image'
a64_p2.source_type = 'external'
a64_p2.storage_type = 'url'
a64_p2.status = 'attached'
a64_p2.title = "Laboratory Burner Flame Supplying Kinetic Activation Energy to Reactants"
a64_p2.description = "Photograph of a laboratory flame supplying heat energy to overcome the minimum activation energy barrier (Ea) needed for chemical bonds to react."
a64_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Alcohol-burner_flame.jpg/800px-Alcohol-burner_flame.jpg"
a64_p2.metadata = {
    'author': 'Marián Hubinský',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Marián Hubinský / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Alcohol-burner_flame.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Thermal activation energy input'
}
a64_p2.save()
a64_p2.blocks.set([b64_p2])
print("Lesson 64 Page 2: Asset 313 attached.")

# P3: Energetic Burning Reaction (Wikimedia Image)
b64_p3 = get_or_create_diagram_block(l64, 3, "High-Energy Molecular Collisions Sustaining Exothermic Combustion")
a64_p3, _ = LessonAsset.objects.get_or_create(id=314, defaults={'lesson': l64, 'asset_type': 'image'})
a64_p3.lesson = l64
a64_p3.asset_type = 'image'
a64_p3.source_type = 'external'
a64_p3.storage_type = 'url'
a64_p3.status = 'attached'
a64_p3.title = "High-Energy Molecular Collisions Sustaining Exothermic Combustion"
a64_p3.description = "Photograph illustrating continuous self-sustaining chemical reaction once effective molecular collisions surpass the activation energy threshold."
a64_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Magnesium_ribbon_burning.jpg/800px-Magnesium_ribbon_burning.jpg"
a64_p3.metadata = {
    'author': 'Capt. John Yossarian',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Capt. John Yossarian / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Magnesium_ribbon_burning.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Effective molecular collisions above Ea'
}
a64_p3.save()
a64_p3.blocks.set([b64_p3])
print("Lesson 64 Page 3: Asset 314 attached.")

# P4: Maxwell-Boltzmann Distribution and Collision Theory (Generated SVG)
svg_64_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="t1Shade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="t2Shade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#b91c1c" stop-opacity="0.1"/>
    </linearGradient>
  </defs>

  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">MAXWELL-BOLTZMANN ENERGY DISTRIBUTION &amp; TEMPERATURE EFFECT</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Increasing Temperature Significantly Increases the Fraction of Colliding Particles with Kinetic Energy ≥ Ea</text>

  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Y Axis: Fraction of Particles -->
    <line x1="70" y1="280" x2="70" y2="40" stroke="#94a3b8" stroke-width="2"/>
    <text x="50" y="160" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold" transform="rotate(-90 50 160)">Fraction of Molecules</text>

    <!-- X Axis: Kinetic Energy -->
    <line x1="70" y1="280" x2="640" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <text x="355" y="305" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Kinetic Energy (E)</text>

    <!-- T1 Curve (Lower Temperature - Cyan) -->
    <path d="M 70 280 Q 150 40 240 160 Q 340 250 460 275 L 600 280" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <text x="180" y="95" fill="#38bdf8" font-size="12" font-weight="bold">Lower Temp (T₁)</text>

    <!-- T2 Curve (Higher Temperature - Red/Orange) -->
    <path d="M 70 280 Q 200 130 310 190 Q 420 240 560 270 L 640 280" fill="none" stroke="#ef4444" stroke-width="3"/>
    <text x="290" y="150" fill="#f87171" font-size="12" font-weight="bold">Higher Temp (T₂ &gt; T₁)</text>

    <!-- Activation Energy Vertical Line (Ea) -->
    <line x1="450" y1="280" x2="450" y2="50" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4"/>
    <text x="450" y="42" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">Activation Energy (Ea)</text>

    <!-- Shaded Area for T1 particles with E >= Ea -->
    <path d="M 450 275 Q 490 278 600 280 L 450 280 Z" fill="url(#t1Shade)"/>

    <!-- Shaded Area for T2 particles with E >= Ea -->
    <path d="M 450 248 Q 520 265 640 280 L 450 280 Z" fill="url(#t2Shade)"/>

    <!-- Explanation Badge -->
    <rect x="470" y="100" width="210" height="120" rx="8" fill="#020617" stroke="#fbbf24"/>
    <text x="575" y="125" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Kinetic Consequences:</text>
    <text x="480" y="148" fill="#cbd5e1" font-size="10">• Peak shifts right &amp; lowers</text>
    <text x="480" y="168" fill="#fca5a5" font-size="10">• Greatly expands shaded area</text>
    <text x="480" y="188" fill="#4ade80" font-size="10">• More frequent effective collisions</text>
    <text x="480" y="208" fill="#38bdf8" font-size="10">• Rate doubles per ~10°C rise</text>
  </g>
</svg>'''
b64_p4 = get_or_create_diagram_block(l64, 4, "Maxwell-Boltzmann Energy Distribution and Temperature Shift on Reaction Rate")
a64_p4, _ = LessonAsset.objects.get_or_create(id=315, defaults={'lesson': l64, 'asset_type': 'diagram'})
a64_p4.lesson = l64
a64_p4.asset_type = 'diagram'
a64_p4.source_type = 'ai_generated'
a64_p4.storage_type = 'file'
a64_p4.status = 'attached'
a64_p4.title = "Maxwell-Boltzmann Energy Distribution and Temperature Shift on Reaction Rate"
a64_p4.description = "Distribution curve comparing kinetic energies at two temperatures and demonstrating the sharp increase in particles having energy greater than or equal to Ea."
a64_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_64_p4)
a64_p4.file.save(f'maxwell_boltzmann_{l64.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a64_p4.blocks.set([b64_p4])
print("Lesson 64 Page 4: Asset 315 saved and attached.")


# =========================================================================
# 3. LESSON 65: Factors Affecting the Rate of a Reaction
# =========================================================================
l65 = Lesson.objects.get(id=65)
print(f"\nProcessing Lesson 65: {l65.title}")

# P2: Solid Calcite Crystal Specimen (Wikimedia Image)
b65_p2 = get_or_create_diagram_block(l65, 2, "Crystalline Calcium Carbonate Mineral Specimen (Marble Chips)")
a65_p2, _ = LessonAsset.objects.get_or_create(id=316, defaults={'lesson': l65, 'asset_type': 'image'})
a65_p2.lesson = l65
a65_p2.asset_type = 'image'
a65_p2.source_type = 'external'
a65_p2.storage_type = 'url'
a65_p2.status = 'attached'
a65_p2.title = "Crystalline Calcium Carbonate Mineral Specimen (Marble Chips)"
a65_p2.description = "Photograph of mineral calcite marble chips used in rate of reaction investigations to contrast solid surface area with finely powdered calcium carbonate."
a65_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Calcite_%28Charcas%2C_San_Luis_Potosi%2C_Mexico%29.jpg/800px-Calcite_%28Charcas%2C_San_Luis_Potosi%2C_Mexico%29.jpg"
a65_p2.metadata = {
    'author': 'James St. John',
    'licensing': 'CC BY 2.0',
    'attribution': 'James St. John / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Calcite_(Charcas,_San_Luis_Potosi,_Mexico).jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Surface area of solid reactants'
}
a65_p2.save()
a65_p2.blocks.set([b65_p2])
print("Lesson 65 Page 2: Asset 316 attached.")

# P3: Catalytic Decomposition (Wikimedia Image)
b65_p3 = get_or_create_diagram_block(l65, 3, "Catalytic Decomposition of Hydrogen Peroxide by Manganese(IV) Oxide")
a65_p3, _ = LessonAsset.objects.get_or_create(id=317, defaults={'lesson': l65, 'asset_type': 'image'})
a65_p3.lesson = l65
a65_p3.asset_type = 'image'
a65_p3.source_type = 'external'
a65_p3.storage_type = 'url'
a65_p3.status = 'attached'
a65_p3.title = "Catalytic Decomposition of Hydrogen Peroxide by Manganese(IV) Oxide"
a65_p3.description = "Photograph showing rapid oxygen gas release when solid black manganese(IV) oxide catalyst is added to aqueous hydrogen peroxide."
a65_p3.url = "https://upload.wikimedia.org/wikipedia/commons/2/27/H2O2_catalytic_decomposition.JPG"
a65_p3.metadata = {
    'author': 'Chemicalinterest',
    'licensing': 'Public domain',
    'attribution': 'Chemicalinterest / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:H2O2_catalytic_decomposition.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Catalytic effect on reaction kinetics'
}
a65_p3.save()
a65_p3.blocks.set([b65_p3])
print("Lesson 65 Page 3: Asset 317 attached.")

# P4: Surface Area & Collision Frequency (Generated SVG)
svg_65_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SURFACE AREA EFFECT: SOLID LUMP VS. POWDERED PARTICLES</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Dividing a Solid Increases Exposed Surface Atoms, Greatly Increasing Collision Frequency with Acid Ions</text>

  <g transform="translate(45, 75)">
    <!-- Left: Single Large Lump -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#d97706" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">LARGE SOLID LUMP (LOW SURFACE AREA)</text>

      <!-- Large Solid Cube -->
      <rect x="110" y="65" width="125" height="125" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
      <text x="172" y="132" text-anchor="middle" fill="#cbd5e1" font-size="11">Interior Atoms</text>
      <text x="172" y="148" text-anchor="middle" fill="#94a3b8" font-size="9">(Trapped/Inaccessible)</text>

      <!-- Acid Ions around exterior only -->
      <circle cx="85" cy="100" r="10" fill="#38bdf8"/><text x="85" y="104" text-anchor="middle" fill="#fff" font-size="8">H⁺</text>
      <circle cx="260" cy="100" r="10" fill="#38bdf8"/><text x="260" y="104" text-anchor="middle" fill="#fff" font-size="8">H⁺</text>
      <circle cx="172" cy="45" r="10" fill="#38bdf8"/><text x="172" y="49" text-anchor="middle" fill="#fff" font-size="8">H⁺</text>
      <circle cx="172" cy="210" r="10" fill="#38bdf8"/><text x="172" y="214" text-anchor="middle" fill="#fff" font-size="8">H⁺</text>

      <rect x="15" y="235" width="315" height="85" rx="8" fill="#020617"/>
      <text x="25" y="258" fill="#fbbf24" font-size="11" font-weight="bold">• Only outer surface reacts</text>
      <text x="25" y="278" fill="#94a3b8" font-size="10">• Fewer collisions per second</text>
      <text x="25" y="298" fill="#f87171" font-size="10" font-weight="bold">• Slower reaction rate (mild bubbling)</text>
    </g>

    <!-- Right: Divided Small Particles / Powder -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">DIVIDED POWDER (HIGH SURFACE AREA)</text>

      <!-- 9 Small Cubes Grid -->
      <g transform="translate(95, 60)">
        <rect x="0" y="0" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>
        <rect x="55" y="0" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>
        <rect x="110" y="0" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>

        <rect x="0" y="48" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>
        <rect x="55" y="48" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>
        <rect x="110" y="48" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>

        <rect x="0" y="96" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>
        <rect x="55" y="96" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>
        <rect x="110" y="96" width="36" height="36" rx="4" fill="#475569" stroke="#34d399"/>
      </g>

      <!-- Acid Ions attacking between particles -->
      <circle cx="80" cy="120" r="8" fill="#38bdf8"/><text x="80" y="123" text-anchor="middle" fill="#fff" font-size="7">H⁺</text>
      <circle cx="265" cy="120" r="8" fill="#38bdf8"/><text x="265" y="123" text-anchor="middle" fill="#fff" font-size="7">H⁺</text>
      <circle cx="140" cy="100" r="8" fill="#38bdf8"/><text x="140" y="103" text-anchor="middle" fill="#fff" font-size="7">H⁺</text>
      <circle cx="200" cy="150" r="8" fill="#38bdf8"/><text x="200" y="153" text-anchor="middle" fill="#fff" font-size="7">H⁺</text>

      <rect x="15" y="235" width="315" height="85" rx="8" fill="#020617"/>
      <text x="25" y="258" fill="#34d399" font-size="11" font-weight="bold">• Massive exposed surface area</text>
      <text x="25" y="278" fill="#cbd5e1" font-size="10">• High collision frequency with H⁺ ions</text>
      <text x="25" y="298" fill="#4ade80" font-size="10" font-weight="bold">• Rapid reaction rate (intense effervescence)</text>
    </g>
  </g>
</svg>'''
b65_p4 = get_or_create_diagram_block(l65, 4, "Sub-Microscopic Surface Area Model: Solid Lump vs. Powdered Particle Collision Kinetics")
a65_p4, _ = LessonAsset.objects.get_or_create(id=318, defaults={'lesson': l65, 'asset_type': 'diagram'})
a65_p4.lesson = l65
a65_p4.asset_type = 'diagram'
a65_p4.source_type = 'ai_generated'
a65_p4.storage_type = 'file'
a65_p4.status = 'attached'
a65_p4.title = "Sub-Microscopic Surface Area Model: Solid Lump vs. Powdered Particle Collision Kinetics"
a65_p4.description = "Diagram comparing exposed reactive atoms and collision frequency in a single solid chunk versus finely ground powder."
a65_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_65_p4)
a65_p4.file.save(f'surface_area_kinetics_{l65.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a65_p4.blocks.set([b65_p4])
print("Lesson 65 Page 4: Asset 318 saved and attached.")


# =========================================================================
# 4. LESSON 66: Effect of Pressure on the Rate of Reaction
# =========================================================================
l66 = Lesson.objects.get(id=66)
print(f"\nProcessing Lesson 66: {l66.title}")

# P2: Compressor Piston Apparatus (Wikimedia Image)
b66_p2 = get_or_create_diagram_block(l66, 2, "Industrial Gas Compressor Piston Mechanism Operating Under Elevated Pressures")
a66_p2, _ = LessonAsset.objects.get_or_create(id=319, defaults={'lesson': l66, 'asset_type': 'image'})
a66_p2.lesson = l66
a66_p2.asset_type = 'image'
a66_p2.source_type = 'external'
a66_p2.storage_type = 'url'
a66_p2.status = 'attached'
a66_p2.title = "Industrial Gas Compressor Piston Mechanism Operating Under Elevated Pressures"
a66_p2.description = "Photograph of a commercial refrigeration compressor showing the mechanical piston cylinder used to compress gas reactants into smaller volumes."
a66_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Compressor_Danfoss_SC18CL.jpg/800px-Compressor_Danfoss_SC18CL.jpg"
a66_p2.metadata = {
    'author': 'Лобачев Владимир',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Лобачев Владимир / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Compressor_Danfoss_SC18CL.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Gas compression and pressure elevation'
}
a66_p2.save()
a66_p2.blocks.set([b66_p2])
print("Lesson 66 Page 2: Asset 319 attached.")

# P3: Pressure Gauges and Dials (Wikimedia Image)
b66_p3 = get_or_create_diagram_block(l66, 3, "Calibrated Industrial Pressure Measurement Dials and Control Gauges")
a66_p3, _ = LessonAsset.objects.get_or_create(id=320, defaults={'lesson': l66, 'asset_type': 'image'})
a66_p3.lesson = l66
a66_p3.asset_type = 'image'
a66_p3.source_type = 'external'
a66_p3.storage_type = 'url'
a66_p3.status = 'attached'
a66_p3.title = "Calibrated Industrial Pressure Measurement Dials and Control Gauges"
a66_p3.description = "Photograph of high-precision pressure gauges monitoring gas pressure levels in chemical systems."
a66_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Da_Lat_locomotive_dials.JPG/800px-Da_Lat_locomotive_dials.JPG"
a66_p3.metadata = {
    'author': 'Dragfyre',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Dragfyre / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Da_Lat_locomotive_dials.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Pressure monitoring instrumentation'
}
a66_p3.save()
a66_p3.blocks.set([b66_p3])
print("Lesson 66 Page 3: Asset 320 attached.")

# P4: Sub-Microscopic Gas Compression (Generated SVG)
svg_66_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">PRESSURE EFFECT ON GASEOUS REACTION RATES</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Compressing Gaseous Reactants Increases Particle Concentration, Leading to More Collisions Per Second</text>

  <g transform="translate(45, 75)">
    <!-- Left: Low Pressure (Large Volume) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">LOW PRESSURE (LARGE VOLUME)</text>

      <!-- Syringe Cylinder -->
      <rect x="70" y="60" width="205" height="150" fill="#020617" stroke="#64748b" stroke-width="2"/>
      
      <!-- Piston Position (High) -->
      <rect x="70" y="60" width="205" height="16" fill="#475569" stroke="#94a3b8"/>
      <rect x="165" y="20" width="15" height="40" fill="#94a3b8"/>

      <!-- Sparsely Distributed Gas Particles -->
      <circle cx="100" cy="110" r="8" fill="#f87171"/><text x="100" y="113" text-anchor="middle" fill="#fff" font-size="7">A</text>
      <circle cx="230" cy="120" r="8" fill="#f87171"/><text x="230" y="123" text-anchor="middle" fill="#fff" font-size="7">A</text>
      <circle cx="130" cy="170" r="8" fill="#38bdf8"/><text x="130" y="173" text-anchor="middle" fill="#fff" font-size="7">B</text>
      <circle cx="210" cy="180" r="8" fill="#38bdf8"/><text x="210" y="183" text-anchor="middle" fill="#fff" font-size="7">B</text>
      <circle cx="170" cy="130" r="8" fill="#f87171"/><text x="170" y="133" text-anchor="middle" fill="#fff" font-size="7">A</text>

      <rect x="15" y="230" width="315" height="90" rx="8" fill="#020617"/>
      <text x="25" y="255" fill="#38bdf8" font-size="11" font-weight="bold">• Particles far apart in space</text>
      <text x="25" y="275" fill="#94a3b8" font-size="10">• Low number of collisions per second</text>
      <text x="25" y="295" fill="#cbd5e1" font-size="10" font-weight="bold">• Reaction proceeds at a slow rate</text>
    </g>

    <!-- Right: High Pressure (Compressed Volume) -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">HIGH PRESSURE (COMPRESSED VOLUME)</text>

      <!-- Syringe Cylinder -->
      <rect x="70" y="60" width="205" height="150" fill="#020617" stroke="#64748b" stroke-width="2"/>
      
      <!-- Piston Position (Pushed Down Low) -->
      <rect x="70" y="130" width="205" height="16" fill="#475569" stroke="#34d399"/>
      <rect x="165" y="70" width="15" height="60" fill="#34d399"/>

      <!-- Tightly Packed Gas Particles -->
      <circle cx="95" cy="165" r="8" fill="#f87171"/><text x="95" y="168" text-anchor="middle" fill="#fff" font-size="7">A</text>
      <circle cx="125" cy="185" r="8" fill="#38bdf8"/><text x="125" y="188" text-anchor="middle" fill="#fff" font-size="7">B</text>
      <circle cx="160" cy="160" r="8" fill="#f87171"/><text x="160" y="163" text-anchor="middle" fill="#fff" font-size="7">A</text>
      <circle cx="200" cy="180" r="8" fill="#38bdf8"/><text x="200" y="183" text-anchor="middle" fill="#fff" font-size="7">B</text>
      <circle cx="245" cy="165" r="8" fill="#f87171"/><text x="245" y="168" text-anchor="middle" fill="#fff" font-size="7">A</text>

      <rect x="15" y="230" width="315" height="90" rx="8" fill="#020617"/>
      <text x="25" y="255" fill="#34d399" font-size="11" font-weight="bold">• Particles crowded per unit volume</text>
      <text x="25" y="275" fill="#a7f3d0" font-size="10">• Sharp increase in collision frequency</text>
      <text x="25" y="295" fill="#4ade80" font-size="10" font-weight="bold">• Reaction rate increases significantly</text>
    </g>
  </g>
</svg>'''
b66_p4 = get_or_create_diagram_block(l66, 4, "Sub-Microscopic Piston Model: Pressure and Collision Density in Gaseous Reactions")
a66_p4, _ = LessonAsset.objects.get_or_create(id=321, defaults={'lesson': l66, 'asset_type': 'diagram'})
a66_p4.lesson = l66
a66_p4.asset_type = 'diagram'
a66_p4.source_type = 'ai_generated'
a66_p4.storage_type = 'file'
a66_p4.status = 'attached'
a66_p4.title = "Sub-Microscopic Piston Model: Pressure and Collision Density in Gaseous Reactions"
a66_p4.description = "Piston cylinder diagram illustrating how compressing gas particles into a smaller volume increases particle collision frequency and overall rate."
a66_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_66_p4)
a66_p4.file.save(f'pressure_rate_piston_{l66.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a66_p4.blocks.set([b66_p4])
print("Lesson 66 Page 4: Asset 321 saved and attached.")


# =========================================================================
# 5. LESSON 67: Reversible Reactions
# =========================================================================
l67 = Lesson.objects.get(id=67)
print(f"\nProcessing Lesson 67: {l67.title}")

# P2: Hydrated Copper Sulfate Crystals (Wikimedia Image)
b67_p2 = get_or_create_diagram_block(l67, 2, "Hydrated Copper(II) Sulfate Pentahydrate Blue Crystals")
a67_p2, _ = LessonAsset.objects.get_or_create(id=322, defaults={'lesson': l67, 'asset_type': 'image'})
a67_p2.lesson = l67
a67_p2.asset_type = 'image'
a67_p2.source_type = 'external'
a67_p2.storage_type = 'url'
a67_p2.status = 'attached'
a67_p2.title = "Hydrated Copper(II) Sulfate Pentahydrate Blue Crystals"
a67_p2.description = "Photograph of deep blue copper(II) sulfate pentahydrate crystals that lose water reversibly upon heating to form white anhydrous powder."
a67_p2.url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Copper_sulfate_pentahydrate_crystals.jpg"
a67_p2.metadata = {
    'author': 'W. Oelen',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'W. Oelen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Copper_sulfate_pentahydrate_crystals.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Reversible hydration-dehydration cycle'
}
a67_p2.save()
a67_p2.blocks.set([b67_p2])
print("Lesson 67 Page 2: Asset 322 attached.")

# P3: Reversible Hydrate Reaction Demonstration (Wikimedia Image)
b67_p3 = get_or_create_diagram_block(l67, 3, "Thermal Dehydration and Color Shift in Crystalline Hydrates")
a67_p3, _ = LessonAsset.objects.get_or_create(id=323, defaults={'lesson': l67, 'asset_type': 'image'})
a67_p3.lesson = l67
a67_p3.asset_type = 'image'
a67_p3.source_type = 'external'
a67_p3.storage_type = 'url'
a67_p3.status = 'attached'
a67_p3.title = "Thermal Dehydration and Color Shift in Crystalline Hydrates"
a67_p3.description = "Photograph demonstrating reversible chemical change where adding water restores the original hydrated crystal color and crystalline structure."
a67_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Crystals_Halite_on_matrix.jpg/800px-Crystals_Halite_on_matrix.jpg"
a67_p3.metadata = {
    'author': 'IvanSakhno',
    'licensing': 'CC BY 4.0',
    'attribution': 'IvanSakhno / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Crystals_Halite_on_matrix.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Reversible chemical state change'
}
a67_p3.save()
a67_p3.blocks.set([b67_p3])
print("Lesson 67 Page 3: Asset 323 attached.")

# P4: Dynamic Reversibility Dual Pathway Flowchart (Generated SVG)
svg_67_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrFwd" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrBwd" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24"/>
    </marker>
  </defs>

  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DUAL PATHWAYS OF REVERSIBLE CHEMICAL REACTIONS</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Reversible Systems Simultaneously Support Forward and Backward Reactions Represented by Equilibrium Arrows (⇌)</text>

  <!-- Flowchart Frame -->
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Left: Reactants State -->
    <g transform="translate(130, 95)">
      <rect x="-95" y="-45" width="190" height="90" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
      <text x="0" y="-15" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">HYDRATED FORM</text>
      <text x="0" y="10" text-anchor="middle" fill="#f8fafc" font-size="13" font-family="monospace" font-weight="bold">CuSO₄·5H₂O(s)</text>
      <text x="0" y="30" text-anchor="middle" fill="#7dd3fc" font-size="10">Deep Blue Crystals</text>
    </g>

    <!-- Right: Products State -->
    <g transform="translate(570, 95)">
      <rect x="-95" y="-45" width="190" height="90" rx="10" fill="#020617" stroke="#fbbf24" stroke-width="2"/>
      <text x="0" y="-15" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">ANHYDROUS FORM</text>
      <text x="0" y="10" text-anchor="middle" fill="#f8fafc" font-size="13" font-family="monospace" font-weight="bold">CuSO₄(s) + 5H₂O(l)</text>
      <text x="0" y="30" text-anchor="middle" fill="#fde68a" font-size="10">White Powder + Water</text>
    </g>

    <!-- Forward Reaction Arrow (Top) -->
    <path d="M 235 75 L 465 75" fill="none" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrFwd)"/>
    <text x="350" y="60" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Forward: Heating (+ΔH Endothermic)</text>

    <!-- Backward Reaction Arrow (Bottom) -->
    <path d="M 465 115 L 235 115" fill="none" stroke="#fbbf24" stroke-width="3.5" marker-end="url(#arrBwd)"/>
    <text x="350" y="135" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">Reverse: Adding Water (-ΔH Exothermic)</text>

    <!-- Comparison Summary Box -->
    <rect x="25" y="175" width="650" height="135" rx="8" fill="#020617" stroke="#1e293b"/>
    <text x="40" y="200" fill="#38bdf8" font-size="12" font-weight="bold">Examples of Dynamic Reversibility in the Kenyan Curriculum:</text>
    <text x="40" y="225" fill="#cbd5e1" font-size="11">1. Thermal decomposition of ammonium chloride:  NH₄Cl(s) ⇌ NH₃(g) + HCl(g)</text>
    <text x="40" y="250" fill="#cbd5e1" font-size="11">2. Nitrogen dioxide / dinitrogen tetroxide system:  2NO₂(g) [Brown] ⇌ N₂O₄(g) [Colorless]</text>
    <text x="40" y="275" fill="#cbd5e1" font-size="11">3. Chromate / dichromate ion transition:  2CrO₄²⁻(aq) [Yellow] + 2H⁺ ⇌ Cr₂O₇²⁻(aq) [Orange] + H₂O</text>
  </g>
</svg>'''
b67_p4 = get_or_create_diagram_block(l67, 4, "Dynamic Reversibility Pathways and Chemical Equilibrium Notation")
a67_p4, _ = LessonAsset.objects.get_or_create(id=324, defaults={'lesson': l67, 'asset_type': 'diagram'})
a67_p4.lesson = l67
a67_p4.asset_type = 'diagram'
a67_p4.source_type = 'ai_generated'
a67_p4.storage_type = 'file'
a67_p4.status = 'attached'
a67_p4.title = "Dynamic Reversibility Pathways and Chemical Equilibrium Notation"
a67_p4.description = "Schematic diagram demonstrating forward and reverse reaction pathways, endothermic dehydration versus exothermic hydration."
a67_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_67_p4)
a67_p4.file.save(f'reversible_pathways_{l67.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a67_p4.blocks.set([b67_p4])
print("Lesson 67 Page 4: Asset 324 saved and attached.")


# =========================================================================
# 6. LESSON 68: Equilibrium
# =========================================================================
l68 = Lesson.objects.get(id=68)
print(f"\nProcessing Lesson 68: {l68.title}")

# P2: Universal Indicator Chemical Equilibrium (Wikimedia Image)
b68_p2 = get_or_create_diagram_block(l68, 2, "Universal Indicator Dynamic Equilibrium in Aqueous Solution")
a68_p2, _ = LessonAsset.objects.get_or_create(id=325, defaults={'lesson': l68, 'asset_type': 'image'})
a68_p2.lesson = l68
a68_p2.asset_type = 'image'
a68_p2.source_type = 'external'
a68_p2.storage_type = 'url'
a68_p2.status = 'attached'
a68_p2.title = "Universal Indicator Dynamic Equilibrium in Aqueous Solution"
a68_p2.description = "Photograph showing color changes in an aqueous acid-base indicator solution reaching chemical equilibrium."
a68_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Classification_of_inorganic_compounds%2C_Metals._Magnesium_1.jpg/800px-Classification_of_inorganic_compounds%2C_Metals._Magnesium_1.jpg"
a68_p2.metadata = {
    'author': 'Alvy16',
    'licensing': 'CC BY 4.0',
    'attribution': 'Alvy16 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Classification_of_inorganic_compounds,_Metals._Magnesium_1.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Visual indicator dynamic equilibrium'
}
a68_p2.save()
a68_p2.blocks.set([b68_p2])
print("Lesson 68 Page 2: Asset 325 attached.")

# P3: Precision Glassware Closed System (Wikimedia Image)
b68_p3 = get_or_create_diagram_block(l68, 3, "Closed Reaction Vessel Maintaining Dynamic Equilibrium Conditions")
a68_p3, _ = LessonAsset.objects.get_or_create(id=326, defaults={'lesson': l68, 'asset_type': 'image'})
a68_p3.lesson = l68
a68_p3.asset_type = 'image'
a68_p3.source_type = 'external'
a68_p3.storage_type = 'url'
a68_p3.status = 'attached'
a68_p3.title = "Closed Reaction Vessel Maintaining Dynamic Equilibrium Conditions"
a68_p3.description = "Photograph of a sealed laboratory flask preventing loss of matter to establish dynamic equilibrium."
a68_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Brand_volumetric_flask_100ml.jpg/800px-Brand_volumetric_flask_100ml.jpg"
a68_p3.metadata = {
    'author': 'Lucasbosch',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Lucasbosch / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Brand_volumetric_flask_100ml.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Closed thermodynamic system'
}
a68_p3.save()
a68_p3.blocks.set([b68_p3])
print("Lesson 68 Page 3: Asset 326 attached.")

# P4: Reaction Rates vs Time & Concentrations vs Time Graphs (Generated SVG)
svg_68_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ESTABLISHMENT OF DYNAMIC CHEMICAL EQUILIBRIUM</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">At Dynamic Equilibrium: Forward Rate = Reverse Rate, and Concentrations Remain Constant</text>

  <g transform="translate(45, 75)">
    <!-- Left Graph: Reaction Rates vs Time -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="172" y="30" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">REACTION RATES VS. TIME</text>

      <!-- Axes -->
      <line x1="45" y1="230" x2="45" y2="60" stroke="#94a3b8" stroke-width="2"/>
      <text x="35" y="145" text-anchor="middle" fill="#94a3b8" font-size="10" transform="rotate(-90 35 145)">Reaction Rate</text>
      <line x1="45" y1="230" x2="300" y2="230" stroke="#94a3b8" stroke-width="2"/>
      <text x="172" y="248" text-anchor="middle" fill="#94a3b8" font-size="10">Time</text>

      <!-- Forward Rate Curve (Starts High, Decreases) -->
      <path d="M 45 80 Q 120 155 200 155 L 300 155" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="110" y="105" fill="#38bdf8" font-size="10" font-weight="bold">Forward Rate</text>

      <!-- Reverse Rate Curve (Starts 0, Increases) -->
      <path d="M 45 230 Q 120 155 200 155 L 300 155" fill="none" stroke="#fbbf24" stroke-width="3"/>
      <text x="110" y="215" fill="#fbbf24" font-size="10" font-weight="bold">Reverse Rate</text>

      <!-- Equilibrium Marker -->
      <line x1="200" y1="230" x2="200" y2="60" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3"/>
      <text x="250" y="140" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">Rates Equal</text>

      <rect x="15" y="260" width="315" height="60" rx="8" fill="#020617"/>
      <text x="172" y="282" text-anchor="middle" fill="#4ade80" font-size="11" font-family="monospace" font-weight="bold">Rate(Forward) = Rate(Reverse)</text>
      <text x="172" y="304" text-anchor="middle" fill="#cbd5e1" font-size="9">Reactions continue at equal speed (dynamic state)</text>
    </g>

    <!-- Right Graph: Concentrations vs Time -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="172" y="30" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">CONCENTRATIONS VS. TIME</text>

      <!-- Axes -->
      <line x1="45" y1="230" x2="45" y2="60" stroke="#94a3b8" stroke-width="2"/>
      <text x="35" y="145" text-anchor="middle" fill="#94a3b8" font-size="10" transform="rotate(-90 35 145)">Concentration</text>
      <line x1="45" y1="230" x2="300" y2="230" stroke="#94a3b8" stroke-width="2"/>
      <text x="172" y="248" text-anchor="middle" fill="#94a3b8" font-size="10">Time</text>

      <!-- Reactants Concentration (Decreases to Constant) -->
      <path d="M 45 80 Q 120 170 200 170 L 300 170" fill="none" stroke="#f87171" stroke-width="3"/>
      <text x="120" y="115" fill="#f87171" font-size="10" font-weight="bold">[Reactants]</text>

      <!-- Products Concentration (Increases from 0 to Constant) -->
      <path d="M 45 230 Q 120 120 200 120 L 300 120" fill="none" stroke="#4ade80" stroke-width="3"/>
      <text x="120" y="195" fill="#4ade80" font-size="10" font-weight="bold">[Products]</text>

      <!-- Equilibrium Marker -->
      <line x1="200" y1="230" x2="200" y2="60" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3"/>
      <text x="250" y="90" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">Equilibrium</text>

      <rect x="15" y="260" width="315" height="60" rx="8" fill="#020617"/>
      <text x="172" y="282" text-anchor="middle" fill="#34d399" font-size="11" font-family="monospace" font-weight="bold">[Reactants] &amp; [Products] = Constant</text>
      <text x="172" y="304" text-anchor="middle" fill="#cbd5e1" font-size="9">Concentrations do not have to be equal, only constant</text>
    </g>
  </g>
</svg>'''
b68_p4 = get_or_create_diagram_block(l68, 4, "Comparative Rate and Concentration Graphs of Dynamic Chemical Equilibrium")
a68_p4, _ = LessonAsset.objects.get_or_create(id=327, defaults={'lesson': l68, 'asset_type': 'diagram'})
a68_p4.lesson = l68
a68_p4.asset_type = 'diagram'
a68_p4.source_type = 'ai_generated'
a68_p4.storage_type = 'file'
a68_p4.status = 'attached'
a68_p4.title = "Comparative Rate and Concentration Graphs of Dynamic Chemical Equilibrium"
a68_p4.description = "Side-by-side graphs showing rate of forward and reverse reactions equalizing while chemical concentrations stabilize at constant values."
a68_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_68_p4)
a68_p4.file.save(f'equilibrium_graphs_{l68.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a68_p4.blocks.set([b68_p4])
print("Lesson 68 Page 4: Asset 327 saved and attached.")


# =========================================================================
# 7. LESSON 69: Factors Affecting Equilibrium
# =========================================================================
l69 = Lesson.objects.get(id=69)
print(f"\nProcessing Lesson 69: {l69.title}")

# P2: Chromate-Dichromate Solution Transition (Wikimedia Image)
b69_p2 = get_or_create_diagram_block(l69, 2, "Transition Metal Solution Equilibrium: Yellow Chromate and Orange Dichromate Ions")
a69_p2, _ = LessonAsset.objects.get_or_create(id=328, defaults={'lesson': l69, 'asset_type': 'image'})
a69_p2.lesson = l69
a69_p2.asset_type = 'image'
a69_p2.source_type = 'external'
a69_p2.storage_type = 'url'
a69_p2.status = 'attached'
a69_p2.title = "Transition Metal Solution Equilibrium: Yellow Chromate and Orange Dichromate Ions"
a69_p2.description = "Photograph displaying yellow chromate (CrO4 2-) and orange dichromate (Cr2O7 2-) solutions demonstrating reversible equilibrium shifts with acid/base addition."
a69_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Coloured-transition-metal-solutions.jpg/800px-Coloured-transition-metal-solutions.jpg"
a69_p2.metadata = {
    'author': 'Benjah-bmm27',
    'licensing': 'Public domain',
    'attribution': 'Benjah-bmm27 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Coloured-transition-metal-solutions.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Chromate-dichromate chemical equilibrium'
}
a69_p2.save()
a69_p2.blocks.set([b69_p2])
print("Lesson 69 Page 2: Asset 328 attached.")

# P3: Potassium Dichromate Crystalline Reagent (Wikimedia Image)
b69_p3 = get_or_create_diagram_block(l69, 3, "Solid Potassium Dichromate Crystalline Reagent Used in Reversible Ionic Systems")
a69_p3, _ = LessonAsset.objects.get_or_create(id=329, defaults={'lesson': l69, 'asset_type': 'image'})
a69_p3.lesson = l69
a69_p3.asset_type = 'image'
a69_p3.source_type = 'external'
a69_p3.storage_type = 'url'
a69_p3.status = 'attached'
a69_p3.title = "Solid Potassium Dichromate Crystalline Reagent Used in Reversible Ionic Systems"
a69_p3.description = "Photograph of bright orange potassium dichromate crystals illustrating the product state of chromate-acid equilibrium."
a69_p3.url = "https://upload.wikimedia.org/wikipedia/commons/e/ea/Dichroman_draseln%C3%BD.JPG"
a69_p3.metadata = {
    'author': 'Ondřej Mangl',
    'licensing': 'Public domain',
    'attribution': 'Ondřej Mangl / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Dichroman_draselný.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Equilibrium reagent state'
}
a69_p3.save()
a69_p3.blocks.set([b69_p3])
print("Lesson 69 Page 3: Asset 329 attached.")

# P4: Catalyst Energy Profile on Equilibrium (Generated SVG)
svg_69_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">CATALYST EFFECT ON CHEMICAL EQUILIBRIUM</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">A Catalyst Lowers Activation Energy for Both Forward and Reverse Reactions Equally (No Shift in Equilibrium Position)</text>

  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Y Axis: Potential Energy -->
    <line x1="70" y1="280" x2="70" y2="40" stroke="#94a3b8" stroke-width="2"/>
    <text x="50" y="160" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold" transform="rotate(-90 50 160)">Potential Energy</text>

    <!-- X Axis: Reaction Coordinate -->
    <line x1="70" y1="280" x2="620" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <text x="345" y="305" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Reaction Coordinate</text>

    <!-- Reactants Line -->
    <line x1="80" y1="180" x2="180" y2="180" stroke="#38bdf8" stroke-width="3.5"/>
    <text x="130" y="170" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">Reactants (A + B)</text>

    <!-- Products Line -->
    <line x1="510" y1="220" x2="610" y2="220" stroke="#4ade80" stroke-width="3.5"/>
    <text x="560" y="210" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">Products (C + D)</text>

    <!-- Uncatalyzed Curve (High Peak) -->
    <path d="M 180 180 C 250 180 280 50 350 50 C 420 50 450 220 510 220" fill="none" stroke="#ef4444" stroke-width="3"/>
    <circle cx="350" cy="50" r="5" fill="#ef4444"/>
    <text x="350" y="38" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">Uncatalyzed Pathway (High Ea)</text>

    <!-- Catalyzed Curve (Lower Peak) -->
    <path d="M 180 180 C 250 180 280 115 350 115 C 420 115 450 220 510 220" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="5"/>
    <circle cx="350" cy="115" r="5" fill="#10b981"/>
    <text x="350" y="135" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Catalyzed Pathway (Lower Ea)</text>

    <!-- Core Takeaway Card -->
    <rect x="180" y="235" width="340" height="85" rx="8" fill="#020617" stroke="#fbbf24"/>
    <text x="350" y="258" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Le Chatelier's Principle Takeaway:</text>
    <text x="350" y="278" text-anchor="middle" fill="#f8fafc" font-size="10">• Forward &amp; reverse rates increase by the SAME factor</text>
    <text x="350" y="298" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">• Equilibrium is reached faster, but yield is unchanged!</text>
  </g>
</svg>'''
b69_p4 = get_or_create_diagram_block(l69, 4, "Catalytic Energy Barrier Reduction in Reversible Equilibrium Systems")
a69_p4, _ = LessonAsset.objects.get_or_create(id=330, defaults={'lesson': l69, 'asset_type': 'diagram'})
a69_p4.lesson = l69
a69_p4.asset_type = 'diagram'
a69_p4.source_type = 'ai_generated'
a69_p4.storage_type = 'file'
a69_p4.status = 'attached'
a69_p4.title = "Catalytic Energy Barrier Reduction in Reversible Equilibrium Systems"
a69_p4.description = "Energy profile diagram demonstrating that catalysts lower activation energy equally in both directions without shifting position of equilibrium."
a69_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_69_p4)
a69_p4.file.save(f'catalyst_equilibrium_profile_{l69.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a69_p4.blocks.set([b69_p4])
print("Lesson 69 Page 4: Asset 330 saved and attached.")

print("\n=== First Half of Topic 3 (Lessons 63–69) Completed Successfully! ===")
