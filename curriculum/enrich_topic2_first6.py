import os
import sys
import django
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db.models import Max
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Topic 2: First 6 Lessons (38, 39, 16, 40, 41, 42) ===")

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
# 1. LESSON 38: Endothermic and Exothermic Reactions
# =========================================================================
l38 = Lesson.objects.get(id=38)
print(f"\nProcessing Lesson 38: {l38.title}")

# P2: Thermite Reaction (Wikimedia Image)
b38_p2 = get_or_create_diagram_block(l38, 2, "Intense Exothermic Thermite Reaction Producing Molten Iron")
a38_p2, _ = LessonAsset.objects.get_or_create(id=270, defaults={'lesson': l38, 'asset_type': 'image'})
a38_p2.lesson = l38
a38_p2.asset_type = 'image'
a38_p2.source_type = 'external'
a38_p2.storage_type = 'url'
a38_p2.status = 'attached'
a38_p2.title = "Intense Exothermic Thermite Reaction Producing Molten Iron"
a38_p2.description = "Photograph of the highly exothermic thermite reaction between aluminium powder and iron(III) oxide releasing radiant thermal energy and molten elemental iron."
a38_p2.url = "https://upload.wikimedia.org/wikipedia/commons/e/ee/Iron_III_Flame_Thermite_Reaction.jpg"
a38_p2.metadata = {
    'author': 'Denver & Rio Grande',
    'licensing': 'CC0',
    'attribution': 'Denver & Rio Grande / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Iron_III_Flame_Thermite_Reaction.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'High-energy exothermic reaction'
}
a38_p2.save()
a38_p2.blocks.set([b38_p2])
print("Lesson 38 Page 2: Asset 270 attached.")

# P3: Instant Cold Pack (Wikimedia Image)
b38_p3 = get_or_create_diagram_block(l38, 3, "Commercial Instant Cold Pack Utilizing Endothermic Dissolution of Ammonium Nitrate")
a38_p3, _ = LessonAsset.objects.get_or_create(id=271, defaults={'lesson': l38, 'asset_type': 'image'})
a38_p3.lesson = l38
a38_p3.asset_type = 'image'
a38_p3.source_type = 'external'
a38_p3.storage_type = 'url'
a38_p3.status = 'attached'
a38_p3.title = "Commercial Instant Cold Pack Utilizing Endothermic Dissolution of Ammonium Nitrate"
a38_p3.description = "Photograph of an instant cold pack where breaking an internal water pouch triggers the endothermic dissolution of solid ammonium nitrate, absorbing heat from surroundings."
a38_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Daiso_instant_cold_pack_300g.jpg/960px-Daiso_instant_cold_pack_300g.jpg"
a38_p3.metadata = {
    'author': 'Qurren',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Qurren / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Daiso_instant_cold_pack_300g.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Endothermic dissolution in everyday cold packs'
}
a38_p3.save()
a38_p3.blocks.set([b38_p3])
print("Lesson 38 Page 3: Asset 271 attached.")

# P4: Energy Level Diagrams Comparison (Generated SVG)
svg_38_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="exoGlow" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#b91c1c" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="endoGlow" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0e7490" stop-opacity="0.05"/>
    </linearGradient>
    <marker id="arrExo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f87171"/>
    </marker>
    <marker id="arrEndo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ENERGY LEVEL DIAGRAMS: EXOTHERMIC VS. ENDOTHERMIC</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Comparison of Enthalpy Levels ($H$) Between Reactants and Products</text>

  <!-- Left Panel: Exothermic -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="15" y="15" width="315" height="240" rx="10" fill="url(#exoGlow)"/>
    
    <text x="172" y="32" text-anchor="middle" fill="#f87171" font-size="13" font-weight="bold">EXOTHERMIC REACTION (ΔH &lt; 0)</text>
    <text x="172" y="48" text-anchor="middle" fill="#fca5a5" font-size="10">Heat Released to Surroundings (Temp Rises)</text>

    <!-- Energy Axis -->
    <line x1="45" y1="230" x2="45" y2="70" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 40 78 L 45 68 L 50 78" fill="#94a3b8"/>
    <text x="35" y="150" text-anchor="middle" fill="#94a3b8" font-size="10" transform="rotate(-90 35 150)">Enthalpy (H)</text>

    <!-- Reaction Coordinate Axis -->
    <line x1="45" y1="230" x2="300" y2="230" stroke="#94a3b8" stroke-width="2"/>
    <text x="172" y="248" text-anchor="middle" fill="#94a3b8" font-size="10">Reaction Progress</text>

    <!-- Reactants Level (High) -->
    <line x1="65" y1="100" x2="155" y2="100" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>
    <text x="110" y="90" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">Reactants (H₁)</text>

    <!-- Products Level (Low) -->
    <line x1="205" y1="190" x2="295" y2="190" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>
    <text x="250" y="210" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">Products (H₂)</text>

    <!-- Downward Delta H Arrow -->
    <line x1="180" y1="105" x2="180" y2="185" stroke="#f87171" stroke-width="2.5" marker-end="url(#arrExo)"/>
    <text x="188" y="150" fill="#f87171" font-size="11" font-weight="bold">ΔH = -ve</text>

    <!-- Bottom Properties Banner -->
    <rect x="15" y="262" width="315" height="60" rx="8" fill="#020617"/>
    <text x="172" y="284" text-anchor="middle" fill="#fca5a5" font-size="11" font-family="monospace" font-weight="bold">H(products) &lt; H(reactants)</text>
    <text x="172" y="306" text-anchor="middle" fill="#cbd5e1" font-size="10">Examples: Combustion, Neutralization, Respiration</text>
  </g>

  <!-- Right Panel: Endothermic -->
  <g transform="translate(430, 75)">
    <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect x="15" y="15" width="315" height="240" rx="10" fill="url(#endoGlow)"/>

    <text x="172" y="32" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">ENDOTHERMIC REACTION (ΔH &gt; 0)</text>
    <text x="172" y="48" text-anchor="middle" fill="#7dd3fc" font-size="10">Heat Absorbed from Surroundings (Temp Drops)</text>

    <!-- Energy Axis -->
    <line x1="45" y1="230" x2="45" y2="70" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 40 78 L 45 68 L 50 78" fill="#94a3b8"/>
    <text x="35" y="150" text-anchor="middle" fill="#94a3b8" font-size="10" transform="rotate(-90 35 150)">Enthalpy (H)</text>

    <!-- Reaction Coordinate Axis -->
    <line x1="45" y1="230" x2="300" y2="230" stroke="#94a3b8" stroke-width="2"/>
    <text x="172" y="248" text-anchor="middle" fill="#94a3b8" font-size="10">Reaction Progress</text>

    <!-- Reactants Level (Low) -->
    <line x1="65" y1="190" x2="155" y2="190" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    <text x="110" y="210" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">Reactants (H₁)</text>

    <!-- Products Level (High) -->
    <line x1="205" y1="100" x2="295" y2="100" stroke="#a78bfa" stroke-width="4" stroke-linecap="round"/>
    <text x="250" y="90" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">Products (H₂)</text>

    <!-- Upward Delta H Arrow -->
    <line x1="180" y1="185" x2="180" y2="105" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrEndo)"/>
    <text x="188" y="150" fill="#38bdf8" font-size="11" font-weight="bold">ΔH = +ve</text>

    <!-- Bottom Properties Banner -->
    <rect x="15" y="262" width="315" height="60" rx="8" fill="#020617"/>
    <text x="172" y="284" text-anchor="middle" fill="#7dd3fc" font-size="11" font-family="monospace" font-weight="bold">H(products) &gt; H(reactants)</text>
    <text x="172" y="306" text-anchor="middle" fill="#cbd5e1" font-size="10">Examples: Photosynthesis, Thermal Decomposition, NH₄NO₃ in Water</text>
  </g>
</svg>'''
b38_p4 = get_or_create_diagram_block(l38, 4, "Comparative Enthalpy Level Diagrams for Exothermic and Endothermic Reactions")
a38_p4, _ = LessonAsset.objects.get_or_create(id=272, defaults={'lesson': l38, 'asset_type': 'diagram'})
a38_p4.lesson = l38
a38_p4.asset_type = 'diagram'
a38_p4.source_type = 'ai_generated'
a38_p4.storage_type = 'file'
a38_p4.status = 'attached'
a38_p4.title = "Comparative Enthalpy Level Diagrams for Exothermic and Endothermic Reactions"
a38_p4.description = "Side-by-side enthalpy profile diagrams illustrating the relative energy levels of reactants and products with corresponding signs of enthalpy change."
a38_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_38_p4)
a38_p4.file.save(f'enthalpy_level_diagrams_{l38.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a38_p4.blocks.set([b38_p4])
print("Lesson 38 Page 4: Asset 272 saved and attached.")


# =========================================================================
# 2. LESSON 39: Enthalpy Notation
# =========================================================================
l39 = Lesson.objects.get(id=39)
print(f"\nProcessing Lesson 39: {l39.title}")

# P2: Magnesium Combustion (Wikimedia Image)
b39_p2 = get_or_create_diagram_block(l39, 2, "Vigorous Exothermic Combustion of Magnesium Ribbon in Air")
a39_p2, _ = LessonAsset.objects.get_or_create(id=273, defaults={'lesson': l39, 'asset_type': 'image'})
a39_p2.lesson = l39
a39_p2.asset_type = 'image'
a39_p2.source_type = 'external'
a39_p2.storage_type = 'url'
a39_p2.status = 'attached'
a39_p2.title = "Vigorous Exothermic Combustion of Magnesium Ribbon in Air"
a39_p2.description = "Photograph capturing the intense blinding white light and thermal energy released during the standard exothermic combustion of magnesium ribbon."
a39_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Magnesium_ribbon_burning.jpg/960px-Magnesium_ribbon_burning.jpg"
a39_p2.metadata = {
    'author': 'Capt. John Yossarian',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Capt. John Yossarian / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Magnesium_ribbon_burning.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Standard thermochemical enthalpy of combustion'
}
a39_p2.save()
a39_p2.blocks.set([b39_p2])
print("Lesson 39 Page 2: Asset 273 attached.")

# P3: Full Enthalpy Profile with Activation Energy (Generated SVG)
svg_39_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="curveFill" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.05"/>
    </linearGradient>
    <marker id="arrUp" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrDown" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/>
    </marker>
  </defs>

  <text x="400" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">COMPLETE ENERGY PROFILE: ACTIVATION ENERGY &amp; ENTHALPY CHANGE</text>
  <text x="400" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Energy Pathway Showing the Activated Complex Barrier and Net Heat of Reaction</text>

  <!-- Main Graph Frame -->
  <g transform="translate(70, 75)">
    <rect x="0" y="0" width="660" height="330" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Y-Axis (Enthalpy) -->
    <line x1="60" y1="280" x2="60" y2="40" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 55 48 L 60 38 L 65 48" fill="#94a3b8"/>
    <text x="45" y="160" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold" transform="rotate(-90 45 160)">Enthalpy (H)</text>

    <!-- X-Axis (Reaction Coordinate) -->
    <line x1="60" y1="280" x2="600" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <text x="330" y="305" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Reaction Coordinate (Progress of Reaction)</text>

    <!-- Reactants Line -->
    <line x1="80" y1="160" x2="190" y2="160" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    <text x="135" y="148" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Reactants (H_reactants)</text>

    <!-- Energy Curve -->
    <path d="M 190 160 C 260 160 280 55 350 55 C 420 55 440 240 510 240" fill="none" stroke="#f59e0b" stroke-width="3.5"/>

    <!-- Activated Complex Peak -->
    <circle cx="350" cy="55" r="7" fill="#fbbf24"/>
    <text x="350" y="38" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">Activated Complex (Transition State)</text>

    <!-- Products Line -->
    <line x1="510" y1="240" x2="590" y2="240" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>
    <text x="550" y="260" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Products (H_products)</text>

    <!-- Activation Energy Arrow (Ea) -->
    <line x1="220" y1="160" x2="220" y2="60" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrUp)"/>
    <line x1="190" y1="160" x2="240" y2="160" stroke="#64748b" stroke-dasharray="3"/>
    <text x="230" y="110" fill="#fbbf24" font-size="11" font-weight="bold">Ea (Activation Energy)</text>

    <!-- Enthalpy Change Arrow (Delta H) -->
    <line x1="470" y1="160" x2="470" y2="235" stroke="#ef4444" stroke-width="2.5" marker-end="url(#arrDown)"/>
    <line x1="190" y1="160" x2="490" y2="160" stroke="#64748b" stroke-dasharray="3"/>
    <line x1="450" y1="240" x2="510" y2="240" stroke="#64748b" stroke-dasharray="3"/>
    <text x="480" y="200" fill="#f87171" font-size="12" font-weight="bold">ΔH = H_products - H_reactants (&lt; 0)</text>
  </g>
</svg>'''
b39_p3 = get_or_create_diagram_block(l39, 3, "Comprehensive Energy Profile: Activation Energy Barrier and Enthalpy of Reaction")
a39_p3, _ = LessonAsset.objects.get_or_create(id=274, defaults={'lesson': l39, 'asset_type': 'diagram'})
a39_p3.lesson = l39
a39_p3.asset_type = 'diagram'
a39_p3.source_type = 'ai_generated'
a39_p3.storage_type = 'file'
a39_p3.status = 'attached'
a39_p3.title = "Comprehensive Energy Profile: Activation Energy Barrier and Enthalpy of Reaction"
a39_p3.description = "Energy profile diagram indicating reactants, transition state with activation energy barrier Ea, and net enthalpy change Delta H."
a39_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_39_p3)
a39_p3.file.save(f'energy_profile_ea_delta_h_{l39.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a39_p3.blocks.set([b39_p3])
print("Lesson 39 Page 3: Asset 274 saved and attached.")


# =========================================================================
# 3. LESSON 16: Bond Breaking and Bond Formation
# =========================================================================
l16 = Lesson.objects.get(id=16)
print(f"\nProcessing Lesson 16: {l16.title}")

# P2: Alcohol Spirit Burner (Wikimedia Image)
b16_p2 = get_or_create_diagram_block(l16, 2, "Laboratory Alcohol Spirit Lamp Flame Demonstrating Continuous Chemical Combustion")
a16_p2, _ = LessonAsset.objects.get_or_create(id=275, defaults={'lesson': l16, 'asset_type': 'image'})
a16_p2.lesson = l16
a16_p2.asset_type = 'image'
a16_p2.source_type = 'external'
a16_p2.storage_type = 'url'
a16_p2.status = 'attached'
a16_p2.title = "Laboratory Alcohol Spirit Lamp Flame Demonstrating Continuous Chemical Combustion"
a16_p2.description = "Photograph of an illuminated laboratory spirit burner flame where breaking hydrocarbon bonds and forming carbon-oxygen bonds generates heat."
a16_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Alcohol-burner_flame.jpg/960px-Alcohol-burner_flame.jpg"
a16_p2.metadata = {
    'author': 'Marián Hubinský',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Marián Hubinský / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Alcohol-burner_flame.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Combustion bond dynamics'
}
a16_p2.save()
a16_p2.blocks.set([b16_p2])
print("Lesson 16 Page 2: Asset 275 attached.")

# P3: Sub-Microscopic Molecular Bond Dynamics (Generated SVG)
svg_16_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="bondBreak" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="bondForm" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#047857" stop-opacity="0.05"/>
    </linearGradient>
  </defs>

  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SUB-MICROSCOPIC BOND DYNAMICS: H₂ + Cl₂ → 2HCl</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Bond Breaking Requires Energy (+ΔH); Bond Formation Releases Energy (-ΔH)</text>

  <!-- Step 1: Bond Breaking (Endothermic) -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="15" y="15" width="315" height="235" rx="10" fill="url(#bondBreak)"/>

    <text x="172" y="36" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">STEP 1: BOND BREAKING (ENDOTHERMIC)</text>
    <text x="172" y="54" text-anchor="middle" fill="#7dd3fc" font-size="10">Energy Absorbed from Surroundings (+679 kJ)</text>

    <!-- H-H Molecule -->
    <g transform="translate(80, 110)">
      <circle cx="-16" cy="0" r="16" fill="#dc2626"/><text x="-16" y="4" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">H</text>
      <line x1="0" y1="0" x2="32" y2="0" stroke="#f87171" stroke-width="3"/>
      <circle cx="48" cy="0" r="16" fill="#dc2626"/><text x="48" y="4" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">H</text>
      <text x="16" y="32" text-anchor="middle" fill="#cbd5e1" font-size="9">H–H (+436 kJ)</text>
    </g>

    <!-- Cl-Cl Molecule -->
    <g transform="translate(200, 110)">
      <circle cx="-18" cy="0" r="18" fill="#16a34a"/><text x="-18" y="4" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Cl</text>
      <line x1="0" y1="0" x2="36" y2="0" stroke="#4ade80" stroke-width="3"/>
      <circle cx="54" cy="0" r="18" fill="#16a34a"/><text x="54" y="4" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Cl</text>
      <text x="18" y="32" text-anchor="middle" fill="#cbd5e1" font-size="9">Cl–Cl (+243 kJ)</text>
    </g>

    <!-- Free Atoms Formed -->
    <g transform="translate(172, 195)">
      <text x="0" y="0" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">4 Free Gaseous Radicals: 2H• + 2Cl•</text>
      <circle cx="-60" cy="22" r="12" fill="#dc2626"/><text x="-60" y="25" text-anchor="middle" fill="#fff" font-size="8">H</text>
      <circle cx="-20" cy="22" r="12" fill="#dc2626"/><text x="-20" y="25" text-anchor="middle" fill="#fff" font-size="8">H</text>
      <circle cx="20" cy="22" r="14" fill="#16a34a"/><text x="20" y="25" text-anchor="middle" fill="#fff" font-size="8">Cl</text>
      <circle cx="60" cy="22" r="14" fill="#16a34a"/><text x="60" y="25" text-anchor="middle" fill="#fff" font-size="8">Cl</text>
    </g>

    <rect x="15" y="260" width="315" height="60" rx="8" fill="#020617"/>
    <text x="172" y="282" text-anchor="middle" fill="#38bdf8" font-size="11" font-family="monospace" font-weight="bold">Total Energy Absorbed = +679 kJ/mol</text>
    <text x="172" y="304" text-anchor="middle" fill="#94a3b8" font-size="10">Breaking bonds always requires energy input</text>
  </g>

  <!-- Step 2: Bond Formation (Exothermic) -->
  <g transform="translate(430, 75)">
    <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="15" y="15" width="315" height="235" rx="10" fill="url(#bondForm)"/>

    <text x="172" y="36" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">STEP 2: BOND FORMATION (EXOTHERMIC)</text>
    <text x="172" y="54" text-anchor="middle" fill="#6ee7b7" font-size="10">Energy Released to Surroundings (-864 kJ)</text>

    <!-- 2 HCl Molecules Formed -->
    <g transform="translate(85, 125)">
      <circle cx="-14" cy="0" r="14" fill="#dc2626"/><text x="-14" y="4" text-anchor="middle" fill="#fff" font-size="9">H</text>
      <line x1="0" y1="0" x2="28" y2="0" stroke="#34d399" stroke-width="4"/>
      <circle cx="44" cy="0" r="18" fill="#16a34a"/><text x="44" y="4" text-anchor="middle" fill="#fff" font-size="10">Cl</text>
      <text x="15" y="35" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">1st H–Cl (-432 kJ)</text>
    </g>

    <g transform="translate(205, 125)">
      <circle cx="-14" cy="0" r="14" fill="#dc2626"/><text x="-14" y="4" text-anchor="middle" fill="#fff" font-size="9">H</text>
      <line x1="0" y1="0" x2="28" y2="0" stroke="#34d399" stroke-width="4"/>
      <circle cx="44" cy="0" r="18" fill="#16a34a"/><text x="44" y="4" text-anchor="middle" fill="#fff" font-size="10">Cl</text>
      <text x="15" y="35" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">2nd H–Cl (-432 kJ)</text>
    </g>

    <!-- Net Heat Balance -->
    <rect x="25" y="185" width="295" height="55" rx="8" fill="#020617"/>
    <text x="172" y="206" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="bold">Net ΔH = (+679 kJ) + (-864 kJ)</text>
    <text x="172" y="226" text-anchor="middle" fill="#f87171" font-size="12" font-family="monospace" font-weight="bold">Net ΔH = -185 kJ/mol (EXOTHERMIC)</text>

    <rect x="15" y="260" width="315" height="60" rx="8" fill="#020617"/>
    <text x="172" y="282" text-anchor="middle" fill="#34d399" font-size="11" font-family="monospace" font-weight="bold">Energy Released &gt; Energy Absorbed</text>
    <text x="172" y="304" text-anchor="middle" fill="#94a3b8" font-size="10">Forms strong stable bonds with lower potential energy</text>
  </g>
</svg>'''
b16_p3 = get_or_create_diagram_block(l16, 3, "Sub-Microscopic Molecular Bond Dynamics in the Synthesis of Hydrogen Chloride")
a16_p3, _ = LessonAsset.objects.get_or_create(id=276, defaults={'lesson': l16, 'asset_type': 'diagram'})
a16_p3.lesson = l16
a16_p3.asset_type = 'diagram'
a16_p3.source_type = 'ai_generated'
a16_p3.storage_type = 'file'
a16_p3.status = 'attached'
a16_p3.title = "Sub-Microscopic Molecular Bond Dynamics in the Synthesis of Hydrogen Chloride"
a16_p3.description = "Two-stage molecular diagram comparing endothermic bond breaking of H2 and Cl2 with exothermic bond formation of 2HCl."
a16_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_16_p3)
a16_p3.file.save(f'bond_breaking_formation_{l16.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a16_p3.blocks.set([b16_p3])
print("Lesson 16 Page 3: Asset 276 saved and attached.")


# =========================================================================
# 4. LESSON 40: Determination of Enthalpy Changes
# =========================================================================
l40 = Lesson.objects.get(id=40)
print(f"\nProcessing Lesson 40: {l40.title}")

# P2: Coffee Cup Calorimeter (Wikimedia Image)
b40_p2 = get_or_create_diagram_block(l40, 2, "Standard Polystyrene Coffee-Cup Calorimeter Apparatus")
a40_p2, _ = LessonAsset.objects.get_or_create(id=277, defaults={'lesson': l40, 'asset_type': 'image'})
a40_p2.lesson = l40
a40_p2.asset_type = 'image'
a40_p2.source_type = 'external'
a40_p2.storage_type = 'url'
a40_p2.status = 'attached'
a40_p2.title = "Standard Polystyrene Coffee-Cup Calorimeter Apparatus"
a40_p2.description = "Photograph of a laboratory polystyrene coffee-cup calorimeter used to measure heat of solution, neutralization, and displacement with minimal heat loss."
a40_p2.url = "https://upload.wikimedia.org/wikipedia/commons/3/32/Coffee_cup_calorimeter_pic.jpg"
a40_p2.metadata = {
    'author': 'Community College Consortium for Bioscience Credentials',
    'licensing': 'CC BY 3.0',
    'attribution': 'Community College Consortium for Bioscience Credentials / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Coffee_cup_calorimeter_pic.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Laboratory solution calorimetry apparatus'
}
a40_p2.save()
a40_p2.blocks.set([b40_p2])
print("Lesson 40 Page 2: Asset 277 attached.")

# P3: Cross-Section Apparatus of Calorimeter (Generated SVG)
svg_40_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">LABORATORY SOLUTION CALORIMETER APPARATUS</text>
  <text x="400" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Insulated Polystyrene Assembly with Thermometer and Stirrer for Enthalpy Determinations</text>

  <!-- Left: Cross Section Diagram -->
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="360" height="335" rx="14" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>

    <!-- Outer Beaker / Plastic Nest -->
    <rect x="50" y="100" width="260" height="210" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <text x="180" y="325" text-anchor="middle" fill="#94a3b8" font-size="10">Outer Supporting Beaker</text>

    <!-- Cotton Wool / Tissue Paper Insulation -->
    <rect x="70" y="120" width="220" height="175" rx="8" fill="#475569" stroke="#94a3b8" stroke-dasharray="4"/>
    <text x="180" y="275" text-anchor="middle" fill="#cbd5e1" font-size="9">Tissue / Cotton Insulation Nest</text>

    <!-- Inner Polystyrene Cup -->
    <rect x="90" y="135" width="180" height="150" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    
    <!-- Solution Liquid -->
    <rect x="95" y="180" width="170" height="100" rx="4" fill="#0284c7" fill-opacity="0.35"/>
    <text x="180" y="235" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Reacting Solution (m, c)</text>

    <!-- Cardboard Lid -->
    <rect x="80" y="125" width="200" height="16" rx="3" fill="#d97706"/>
    <text x="240" y="118" fill="#fde68a" font-size="9">Cardboard / Plastic Lid</text>

    <!-- Thermometer -->
    <rect x="130" y="30" width="8" height="230" rx="4" fill="#cbd5e1"/>
    <rect x="131" y="180" width="6" height="80" rx="3" fill="#dc2626"/>
    <text x="134" y="22" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">Precision Thermometer (±0.1°C)</text>

    <!-- Stirrer -->
    <path d="M 210 40 L 210 260 L 230 260" fill="none" stroke="#e2e8f0" stroke-width="3" stroke-linecap="round"/>
    <text x="210" y="32" text-anchor="middle" fill="#cbd5e1" font-size="10">Plastic Stirrer</text>
  </g>

  <!-- Right: Key Assumptions and Governing Formula -->
  <g transform="translate(445, 75)">
    <rect x="0" y="0" width="310" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="155" y="30" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">GOVERNING PRINCIPLES</text>

    <!-- Formula Box -->
    <rect x="15" y="45" width="280" height="75" rx="8" fill="#020617"/>
    <text x="140" y="70" text-anchor="middle" fill="#38bdf8" font-size="14" font-family="monospace" font-weight="bold">ΔH = - (m · c · ΔT) / n</text>
    <text x="140" y="95" text-anchor="middle" fill="#cbd5e1" font-size="10">c = 4.2 J g⁻¹ K⁻¹ (Specific heat of water)</text>
    <text x="140" y="110" text-anchor="middle" fill="#cbd5e1" font-size="10">Density of aqueous solution ≈ 1.0 g/cm³</text>

    <!-- Standard Assumptions -->
    <rect x="15" y="130" width="280" height="190" rx="8" fill="#020617"/>
    <text x="25" y="152" fill="#fbbf24" font-size="11" font-weight="bold">Essential Practical Assumptions:</text>
    <text x="25" y="174" fill="#f8fafc" font-size="10">1. Polystyrene has negligible heat capacity</text>
    <text x="25" y="194" fill="#f8fafc" font-size="10">2. No heat is lost to surroundings</text>
    <text x="25" y="214" fill="#f8fafc" font-size="10">3. Density and specific heat capacity</text>
    <text x="35" y="230" fill="#94a3b8" font-size="9">equal those of pure water</text>
    <text x="25" y="254" fill="#4ade80" font-size="10">4. Complete reaction occurs rapidly</text>
    <text x="25" y="280" fill="#fca5a5" font-size="10">5. Correction curve required for exact ΔT</text>
  </g>
</svg>'''
b40_p3 = get_or_create_diagram_block(l40, 3, "Cross-Section Diagram of an Insulated Solution Calorimeter Setup")
a40_p3, _ = LessonAsset.objects.get_or_create(id=278, defaults={'lesson': l40, 'asset_type': 'diagram'})
a40_p3.lesson = l40
a40_p3.asset_type = 'diagram'
a40_p3.source_type = 'ai_generated'
a40_p3.storage_type = 'file'
a40_p3.status = 'attached'
a40_p3.title = "Cross-Section Diagram of an Insulated Solution Calorimeter Setup"
a40_p3.description = "Schematic cross-section showing inner polystyrene cup, outer beaker, cotton insulation, thermometer, stirrer, and governing formula."
a40_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_40_p3)
a40_p3.file.save(f'calorimeter_cross_section_{l40.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a40_p3.blocks.set([b40_p3])
print("Lesson 40 Page 3: Asset 278 saved and attached.")

# P4: Temperature-Time Correction Graph (Generated SVG)
svg_40_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">TEMPERATURE-TIME COOLING CORRECTION GRAPH</text>
  <text x="400" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Extrapolating Cooling Curve to Mixing Time (t = 3.0 min) to Obtain True Instantaneous ΔT</text>

  <g transform="translate(70, 75)">
    <rect x="0" y="0" width="660" height="335" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Graph Grid -->
    <line x1="70" y1="280" x2="600" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="70" y1="280" x2="70" y2="40" stroke="#94a3b8" stroke-width="2"/>
    
    <text x="50" y="160" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold" transform="rotate(-90 50 160)">Temperature (°C)</text>
    <text x="335" y="305" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Time (minutes)</text>

    <!-- X Time Marks -->
    <text x="70" y="295" text-anchor="middle" fill="#94a3b8" font-size="10">0</text>
    <text x="140" y="295" text-anchor="middle" fill="#94a3b8" font-size="10">1.0</text>
    <text x="210" y="295" text-anchor="middle" fill="#94a3b8" font-size="10">2.0</text>
    <text x="280" y="295" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">3.0 (Add)</text>
    <text x="350" y="295" text-anchor="middle" fill="#94a3b8" font-size="10">4.0</text>
    <text x="420" y="295" text-anchor="middle" fill="#94a3b8" font-size="10">5.0</text>
    <text x="490" y="295" text-anchor="middle" fill="#94a3b8" font-size="10">6.0</text>
    <text x="560" y="295" text-anchor="middle" fill="#94a3b8" font-size="10">7.0</text>

    <!-- Initial Steady Line (0 to 2.5 min) -->
    <line x1="70" y1="220" x2="280" y2="220" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="70" cy="220" r="4" fill="#38bdf8"/>
    <circle cx="140" cy="220" r="4" fill="#38bdf8"/>
    <circle cx="210" cy="220" r="4" fill="#38bdf8"/>
    <text x="160" y="210" text-anchor="middle" fill="#7dd3fc" font-size="10">Initial Temp (T₁ = 21.0°C)</text>

    <!-- Vertical Mixing Marker at t = 3.0 min -->
    <line x1="280" y1="280" x2="280" y2="50" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4"/>
    <text x="280" y="42" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Addition at 3.0 min</text>

    <!-- Experimental Curve after addition -->
    <path d="M 280 220 Q 320 100 350 95 L 420 115 L 490 135 L 560 155" fill="none" stroke="#4ade80" stroke-width="3"/>
    <circle cx="350" cy="95" r="4" fill="#4ade80"/>
    <circle cx="420" cy="115" r="4" fill="#4ade80"/>
    <circle cx="490" cy="135" r="4" fill="#4ade80"/>
    <circle cx="560" cy="155" r="4" fill="#4ade80"/>

    <!-- Backward Extrapolation Line (Dashed) to t = 3.0 min -->
    <line x1="560" y1="155" x2="280" y2="75" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5"/>
    <circle cx="280" cy="75" r="5" fill="#ef4444"/>
    <text x="260" y="70" text-anchor="end" fill="#f87171" font-size="11" font-weight="bold">Theoretical Peak (T₂ = 45.5°C)</text>

    <!-- True Delta T Dimension Arrow -->
    <line x1="265" y1="215" x2="265" y2="80" stroke="#f59e0b" stroke-width="3"/>
    <path d="M 260 88 L 265 78 L 270 88" fill="#f59e0b"/>
    <path d="M 260 207 L 265 217 L 270 207" fill="#f59e0b"/>
    <text x="250" y="150" text-anchor="end" fill="#fbbf24" font-size="12" font-weight="bold">True ΔT = 24.5°C</text>

    <!-- Explanation Badge -->
    <rect x="360" y="210" width="225" height="55" rx="6" fill="#020617" stroke="#334155"/>
    <text x="472" y="230" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">Eliminates Cooling Error</text>
    <text x="472" y="248" text-anchor="middle" fill="#cbd5e1" font-size="9">Accounts for heat radiated during stirring</text>
  </g>
</svg>'''
b40_p4 = get_or_create_diagram_block(l40, 4, "Temperature-Time Cooling Curve Extrapolation for True Enthalpy Determination")
a40_p4, _ = LessonAsset.objects.get_or_create(id=279, defaults={'lesson': l40, 'asset_type': 'diagram'})
a40_p4.lesson = l40
a40_p4.asset_type = 'diagram'
a40_p4.source_type = 'ai_generated'
a40_p4.storage_type = 'file'
a40_p4.status = 'attached'
a40_p4.title = "Temperature-Time Cooling Curve Extrapolation for True Enthalpy Determination"
a40_p4.description = "Cooling curve graph showing backward extrapolation of post-mixing temperature to determine true instantaneous temperature change without heat loss error."
a40_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_40_p4)
a40_p4.file.save(f'cooling_curve_extrapolation_{l40.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a40_p4.blocks.set([b40_p4])
print("Lesson 40 Page 4: Asset 279 saved and attached.")


# =========================================================================
# 5. LESSON 41: Standard Conditions for Measuring Enthalpies
# =========================================================================
l41 = Lesson.objects.get(id=41)
print(f"\nProcessing Lesson 41: {l41.title}")

# P2: Precision Barometer (Wikimedia Image)
b41_p2 = get_or_create_diagram_block(l41, 2, "Precision Aneroid Barometer Measuring Standard Atmospheric Pressure")
a41_p2, _ = LessonAsset.objects.get_or_create(id=280, defaults={'lesson': l41, 'asset_type': 'image'})
a41_p2.lesson = l41
a41_p2.asset_type = 'image'
a41_p2.source_type = 'external'
a41_p2.storage_type = 'url'
a41_p2.status = 'attached'
a41_p2.title = "Precision Aneroid Barometer Measuring Standard Atmospheric Pressure"
a41_p2.description = "Photograph of a calibrated aneroid barometer used to verify the standard atmospheric pressure of 101.325 kPa (1 atmosphere) required for thermodynamic enthalpy measurements."
a41_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Aneroid_barometer-MHS_2022-P5200211-black.jpg/960px-Aneroid_barometer-MHS_2022-P5200211-black.jpg"
a41_p2.metadata = {
    'author': 'Rama',
    'licensing': 'CC BY-SA 3.0 fr',
    'attribution': 'Rama / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Aneroid_barometer-MHS_2022-P5200211-black.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Standard pressure condition in thermochemistry'
}
a41_p2.save()
a41_p2.blocks.set([b41_p2])
print("Lesson 41 Page 2: Asset 280 attached.")

# P3: Standard Conditions Triad (Generated SVG)
svg_41_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">THE THREE STANDARD THERMODYNAMIC CONDITIONS</text>
  <text x="400" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Precise Physical Reference Parameters Defined by the Plimsoll Symbol (⦵ or °)</text>

  <!-- 3 Pillar Cards -->
  <g transform="translate(45, 75)">
    <!-- Pillar 1: Temperature -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="220" height="240" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <circle cx="110" cy="50" r="28" fill="#dc2626" fill-opacity="0.2"/>
      <text x="110" y="56" text-anchor="middle" fill="#f87171" font-size="18" font-weight="bold">298 K</text>
      <text x="110" y="100" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">STANDARD TEMPERATURE</text>
      
      <rect x="15" y="115" width="190" height="105" rx="6" fill="#020617"/>
      <text x="105" y="138" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="bold">25°C (298.15 K)</text>
      <text x="105" y="165" text-anchor="middle" fill="#cbd5e1" font-size="10">Note: Distinct from s.t.p.</text>
      <text x="105" y="185" text-anchor="middle" fill="#94a3b8" font-size="9">s.t.p. uses 0°C (273 K)</text>
      <text x="105" y="202" text-anchor="middle" fill="#fca5a5" font-size="9">Thermochemistry = 25°C</text>
    </g>

    <!-- Pillar 2: Pressure -->
    <g transform="translate(245, 0)">
      <rect x="0" y="0" width="220" height="240" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="110" cy="50" r="28" fill="#0284c7" fill-opacity="0.2"/>
      <text x="110" y="56" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">101.3 kPa</text>
      <text x="110" y="100" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">STANDARD PRESSURE</text>
      
      <rect x="15" y="115" width="190" height="105" rx="6" fill="#020617"/>
      <text x="105" y="138" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="bold">1 atm (101,325 Pa)</text>
      <text x="105" y="165" text-anchor="middle" fill="#cbd5e1" font-size="10">760 mmHg at sea level</text>
      <text x="105" y="185" text-anchor="middle" fill="#94a3b8" font-size="9">All gaseous reactants &amp;</text>
      <text x="105" y="202" text-anchor="middle" fill="#7dd3fc" font-size="9">products at 1 atm</text>
    </g>

    <!-- Pillar 3: Concentration -->
    <g transform="translate(490, 0)">
      <rect x="0" y="0" width="220" height="240" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="110" cy="50" r="28" fill="#047857" fill-opacity="0.2"/>
      <text x="110" y="56" text-anchor="middle" fill="#34d399" font-size="18" font-weight="bold">1.0 M</text>
      <text x="110" y="100" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">CONCENTRATION</text>
      
      <rect x="15" y="115" width="190" height="105" rx="6" fill="#020617"/>
      <text x="105" y="138" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="bold">1.0 mol/dm³</text>
      <text x="105" y="165" text-anchor="middle" fill="#cbd5e1" font-size="10">Standard solutions</text>
      <text x="105" y="185" text-anchor="middle" fill="#94a3b8" font-size="9">Substances in most stable</text>
      <text x="105" y="202" text-anchor="middle" fill="#6ee7b7" font-size="9">physical state at 298 K</text>
    </g>
  </g>

  <!-- Bottom Standard Plimsoll Notation -->
  <g transform="translate(45, 330)">
    <rect x="0" y="0" width="710" height="80" rx="10" fill="#020617" stroke="#334155"/>
    <text x="355" y="30" text-anchor="middle" fill="#fbbf24" font-size="14" font-family="monospace" font-weight="bold">ΔH⦵ or ΔH° : "Enthalpy change measured under standard conditions"</text>
    <text x="355" y="55" text-anchor="middle" fill="#cbd5e1" font-size="11">e.g. Standard Enthalpy of Combustion: ΔH°c  |  Standard Enthalpy of Formation: ΔH°f  |  Standard Enthalpy of Neutralization: ΔH°neut</text>
  </g>
</svg>'''
b41_p3 = get_or_create_diagram_block(l41, 3, "The Three Standard Thermodynamic Reference Conditions")
a41_p3, _ = LessonAsset.objects.get_or_create(id=281, defaults={'lesson': l41, 'asset_type': 'diagram'})
a41_p3.lesson = l41
a41_p3.asset_type = 'diagram'
a41_p3.source_type = 'ai_generated'
a41_p3.storage_type = 'file'
a41_p3.status = 'attached'
a41_p3.title = "The Three Standard Thermodynamic Reference Conditions"
a41_p3.description = "Infographic detailing standard temperature 298 K, standard pressure 101.3 kPa, and standard solution concentration 1.0 M with the Plimsoll symbol."
a41_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_41_p3)
a41_p3.file.save(f'standard_conditions_{l41.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a41_p3.blocks.set([b41_p3])
print("Lesson 41 Page 3: Asset 281 saved and attached.")


# =========================================================================
# 6. LESSON 42: Hess's Law
# =========================================================================
l42 = Lesson.objects.get(id=42)
print(f"\nProcessing Lesson 42: {l42.title}")

# P2: Mount Kenya Lenana Peak (Wikimedia Image)
b42_p2 = get_or_create_diagram_block(l42, 2, "Mount Kenya Mountain Peaks Illustrating Independent State Function Paths")
a42_p2, _ = LessonAsset.objects.get_or_create(id=282, defaults={'lesson': l42, 'asset_type': 'image'})
a42_p2.lesson = l42
a42_p2.asset_type = 'image'
a42_p2.source_type = 'external'
a42_p2.storage_type = 'url'
a42_p2.status = 'attached'
a42_p2.title = "Mount Kenya Mountain Peaks Illustrating Independent State Function Paths"
a42_p2.description = "Photograph of Mount Kenya peaks illustrating Hess's Law: total altitude gain between base and summit is independent of whether one climbs directly or follows indirect routes."
a42_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Lenana_and_Austrian_from_Nelion.jpg/960px-Lenana_and_Austrian_from_Nelion.jpg"
a42_p2.metadata = {
    'author': 'Franco Pecchio',
    'licensing': 'CC BY 2.0',
    'attribution': 'Franco Pecchio / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Lenana_and_Austrian_from_Nelion.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'State function and path independence analogy'
}
a42_p2.save()
a42_p2.blocks.set([b42_p2])
print("Lesson 42 Page 2: Asset 282 attached.")

# P3: Hess's Law Constant Heat Summation Principle (Generated SVG)
svg_42_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 430" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrDirect" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrIndirect" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399"/>
    </marker>
  </defs>

  <text x="400" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">HESS'S LAW OF CONSTANT HEAT SUMMATION</text>
  <text x="400" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Total Enthalpy Change for a Reaction is Independent of the Pathway Taken</text>

  <!-- Triangle Energy Cycle Map -->
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="680" height="260" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- State A (Initial Reactants) -->
    <g transform="translate(100, 70)">
      <rect x="-70" y="-35" width="140" height="70" rx="10" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
      <text x="0" y="-5" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">STATE A</text>
      <text x="0" y="16" text-anchor="middle" fill="#f8fafc" font-size="11">Initial Reactants</text>
    </g>

    <!-- State B (Final Products) -->
    <g transform="translate(580, 70)">
      <rect x="-70" y="-35" width="140" height="70" rx="10" fill="#047857" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
      <text x="0" y="-5" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">STATE B</text>
      <text x="0" y="16" text-anchor="middle" fill="#f8fafc" font-size="11">Final Products</text>
    </g>

    <!-- State C (Intermediate Products) -->
    <g transform="translate(340, 205)">
      <rect x="-80" y="-35" width="160" height="70" rx="10" fill="#d97706" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
      <text x="0" y="-5" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">STATE C</text>
      <text x="0" y="16" text-anchor="middle" fill="#f8fafc" font-size="11">Intermediates / Oxides</text>
    </g>

    <!-- Route 1: Direct Pathway (A -> B) -->
    <line x1="175" y1="70" x2="500" y2="70" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrDirect)"/>
    <text x="340" y="55" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">ROUTE 1 (Direct): ΔH₁</text>

    <!-- Route 2: Indirect Step 1 (A -> C) -->
    <line x1="140" y1="110" x2="255" y2="185" stroke="#34d399" stroke-width="3" marker-end="url(#arrIndirect)"/>
    <text x="175" y="165" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">ΔH₂</text>

    <!-- Route 2: Indirect Step 2 (C -> B) -->
    <line x1="425" y1="185" x2="540" y2="110" stroke="#34d399" stroke-width="3" marker-end="url(#arrIndirect)"/>
    <text x="505" y="165" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">ΔH₃</text>
  </g>

  <!-- Bottom Core Hess Equation -->
  <g transform="translate(60, 345)">
    <rect x="0" y="0" width="680" height="65" rx="10" fill="#020617" stroke="#1e293b"/>
    <text x="340" y="28" text-anchor="middle" fill="#fbbf24" font-size="15" font-family="monospace" font-weight="bold">ROUTE 1 = ROUTE 2  ⟹  ΔH₁ = ΔH₂ + ΔH₃</text>
    <text x="340" y="50" text-anchor="middle" fill="#cbd5e1" font-size="11">Reversing an arrow changes the sign: ΔH(reverse) = -ΔH(forward)</text>
  </g>
</svg>'''
b42_p3 = get_or_create_diagram_block(l42, 3, "Hess's Law Constant Heat Summation Principle and Energy Cycle Map")
a42_p3, _ = LessonAsset.objects.get_or_create(id=283, defaults={'lesson': l42, 'asset_type': 'diagram'})
a42_p3.lesson = l42
a42_p3.asset_type = 'diagram'
a42_p3.source_type = 'ai_generated'
a42_p3.storage_type = 'file'
a42_p3.status = 'attached'
a42_p3.title = "Hess's Law Constant Heat Summation Principle and Energy Cycle Map"
a42_p3.description = "Vector cycle schematic illustrating the equality of direct enthalpy route Delta H1 with the sum of indirect steps Delta H2 + Delta H3."
a42_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_42_p3)
a42_p3.file.save(f'hess_law_principle_{l42.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a42_p3.blocks.set([b42_p3])
print("Lesson 42 Page 3: Asset 283 saved and attached.")

# P5: Energy Cycle for Methane Formation (Generated SVG)
svg_42_p5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrHessC" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrHessG" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
    </marker>
  </defs>

  <text x="400" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">HESS'S LAW ENERGY CYCLE: FORMATION OF METHANE (CH₄)</text>
  <text x="400" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Calculating Indirect Enthalpy of Formation (ΔH°f) from Combustion Data</text>

  <!-- Main Energy Cycle Box -->
  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="680" height="260" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>

    <!-- Top Left: Elements in Standard State -->
    <g transform="translate(130, 65)">
      <rect x="-105" y="-30" width="210" height="60" rx="8" fill="#020617" stroke="#38bdf8"/>
      <text x="0" y="5" text-anchor="middle" fill="#38bdf8" font-size="13" font-family="monospace" font-weight="bold">C(s) + 2H₂(g) + 2O₂(g)</text>
    </g>

    <!-- Top Right: Formed Compound -->
    <g transform="translate(550, 65)">
      <rect x="-95" y="-30" width="190" height="60" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="0" y="5" text-anchor="middle" fill="#34d399" font-size="13" font-family="monospace" font-weight="bold">CH₄(g) + 2O₂(g)</text>
    </g>

    <!-- Bottom: Combustion Products -->
    <g transform="translate(340, 205)">
      <rect x="-110" y="-30" width="220" height="60" rx="8" fill="#020617" stroke="#ef4444"/>
      <text x="0" y="5" text-anchor="middle" fill="#f87171" font-size="13" font-family="monospace" font-weight="bold">CO₂(g) + 2H₂O(l)</text>
    </g>

    <!-- Top Arrow: Formation (Target) -->
    <line x1="240" y1="65" x2="445" y2="65" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrHessC)"/>
    <text x="340" y="52" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">Target: ΔH°f(CH₄) = ?</text>

    <!-- Left Arrow: Direct Combustion of Elements -->
    <line x1="130" y1="100" x2="245" y2="185" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrHessC)"/>
    <text x="120" y="160" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">ΔH°c(C) + 2ΔH°c(H₂)</text>
    <text x="120" y="176" text-anchor="middle" fill="#7dd3fc" font-size="10">(-393.5) + 2(-285.8) = -965.1 kJ</text>

    <!-- Right Arrow: Combustion of Methane -->
    <line x1="550" y1="100" x2="435" y2="185" stroke="#10b981" stroke-width="3" marker-end="url(#arrHessG)"/>
    <text x="560" y="160" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">ΔH°c(CH₄)</text>
    <text x="560" y="176" text-anchor="middle" fill="#6ee7b7" font-size="10">-890.4 kJ/mol</text>
  </g>

  <!-- Bottom Calculation Solution Banner -->
  <g transform="translate(60, 345)">
    <rect x="0" y="0" width="680" height="65" rx="10" fill="#020617" stroke="#334155"/>
    <text x="340" y="26" text-anchor="middle" fill="#38bdf8" font-size="13" font-family="monospace" font-weight="bold">ΔH°f(CH₄) + ΔH°c(CH₄) = ΔH°c(C) + 2ΔH°c(H₂)</text>
    <text x="340" y="48" text-anchor="middle" fill="#4ade80" font-size="12" font-family="monospace" font-weight="bold">ΔH°f(CH₄) = -965.1 kJ - (-890.4 kJ) = -74.7 kJ/mol (Exothermic)</text>
  </g>
</svg>'''
b42_p5 = get_or_create_diagram_block(l42, 5, "Thermochemical Energy Cycle for the Formation of Methane from Combustion Data")
a42_p5, _ = LessonAsset.objects.get_or_create(id=284, defaults={'lesson': l42, 'asset_type': 'diagram'})
a42_p5.lesson = l42
a42_p5.asset_type = 'diagram'
a42_p5.source_type = 'ai_generated'
a42_p5.storage_type = 'file'
a42_p5.status = 'attached'
a42_p5.title = "Thermochemical Energy Cycle for the Formation of Methane from Combustion Data"
a42_p5.description = "Thermochemical energy cycle displaying Hess's Law calculation of standard enthalpy of formation of methane from combustion enthalpy data."
a42_p5.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_42_p5)
a42_p5.file.save(f'energy_cycle_methane_{l42.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a42_p5.blocks.set([b42_p5])
print("Lesson 42 Page 5: Asset 284 saved and attached.")

print("\n=== Topic 2 (First 6 Lessons) Visual Enrichment Completed Successfully! ===")
