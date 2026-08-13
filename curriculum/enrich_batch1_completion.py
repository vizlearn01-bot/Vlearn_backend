import os
import sys
import django
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db.models import Max
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Second Half of Topic 1 (Lessons 31–37) ===")

def get_or_create_diagram_block(lesson, page_number, title, component_order=1):
    existing = LessonBlock.objects.filter(
        lesson=lesson, page_number=page_number, block_type='suggested_diagram'
    ).first()
    if existing:
        existing.title = title
        existing.save()
        return existing
    
    # Create new block
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
# LESSON 31: Precipitation Reactions
# =========================================================================
l31 = Lesson.objects.get(id=31)
print(f"\nProcessing Lesson 31: {l31.title}")

# P2: Golden Rain (Wikimedia Image)
b31_p2 = get_or_create_diagram_block(l31, 2, "Golden Rain Demonstration: Precipitation of Insoluble Lead(II) Iodide Crystals")
a31_p2, _ = LessonAsset.objects.get_or_create(id=250, defaults={'lesson': l31, 'asset_type': 'image'})
a31_p2.lesson = l31
a31_p2.asset_type = 'image'
a31_p2.source_type = 'external'
a31_p2.storage_type = 'url'
a31_p2.status = 'attached'
a31_p2.title = "Golden Rain Demonstration: Precipitation of Insoluble Lead(II) Iodide Crystals"
a31_p2.description = "Photograph showing glistening golden yellow hexagonal crystals of lead(II) iodide precipitating upon cooling a saturated aqueous solution."
a31_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Golden_rain_demonstration.jpg/960px-Golden_rain_demonstration.jpg"
a31_p2.metadata = {
    'author': 'Sartnuphon',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Sartnuphon / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Golden_rain_demonstration.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Precipitation of insoluble lead(II) iodide'
}
a31_p2.save()
a31_p2.blocks.set([b31_p2])
print("Lesson 31 Page 2: Asset 250 attached.")

# P3: Sub-Microscopic Lattice Formation (Generated SVG)
svg_31_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 430" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SUB-MICROSCOPIC MECHANISM OF PRECIPITATION</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Hydrated Ions Collide to Form a Rigid Insoluble Lattice while Spectator Ions Remain Solvated</text>

  <!-- Left: Reacting Hydrated Ions -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="320" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">REACTANT SOLUTIONS (BaCl₂ + Na₂SO₄)</text>
    
    <rect x="20" y="45" width="295" height="160" rx="8" fill="#0284c7" fill-opacity="0.15" stroke="#0369a1"/>
    <!-- Reactant Ions -->
    <circle cx="70" cy="90" r="16" fill="#0284c7"/><text x="70" y="95" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Ba²⁺</text>
    <circle cx="160" cy="130" r="16" fill="#dc2626"/><text x="160" y="135" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">SO₄²⁻</text>
    <!-- Spectator Ions -->
    <circle cx="230" cy="85" r="12" fill="#64748b"/><text x="230" y="89" text-anchor="middle" fill="#f8fafc" font-size="9">Na⁺</text>
    <circle cx="90" cy="165" r="12" fill="#64748b"/><text x="90" y="169" text-anchor="middle" fill="#f8fafc" font-size="9">Cl⁻</text>
    <circle cx="250" cy="155" r="12" fill="#64748b"/><text x="250" y="159" text-anchor="middle" fill="#f8fafc" font-size="9">Na⁺</text>

    <rect x="20" y="215" width="295" height="90" rx="8" fill="#020617"/>
    <text x="167" y="240" text-anchor="middle" fill="#cbd5e1" font-size="11">Hydration shells overcome by</text>
    <text x="167" y="258" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">strong electrostatic attraction</text>
    <text x="167" y="282" text-anchor="middle" fill="#94a3b8" font-size="10">High lattice enthalpy favors solid</text>
  </g>

  <!-- Right: Insoluble Solid Lattice Precipitate -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="320" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">INSOLUBLE BaSO₄ LATTICE + SPECTATORS</text>
    
    <rect x="20" y="45" width="295" height="160" rx="8" fill="#047857" fill-opacity="0.15" stroke="#10b981"/>
    <!-- Free Spectator Ions in Solution -->
    <circle cx="65" cy="80" r="12" fill="#64748b"/><text x="65" y="84" text-anchor="middle" fill="#f8fafc" font-size="9">Na⁺</text>
    <circle cx="270" cy="80" r="12" fill="#64748b"/><text x="270" y="84" text-anchor="middle" fill="#f8fafc" font-size="9">Cl⁻</text>
    
    <!-- Crystalline Precipitate Grid at Bottom -->
    <g transform="translate(110, 115)">
      <rect x="-10" y="-10" width="135" height="75" rx="6" fill="#020617" stroke="#cbd5e1"/>
      <circle cx="15" cy="15" r="13" fill="#0284c7"/><text x="15" y="19" text-anchor="middle" fill="#fff" font-size="9">Ba²⁺</text>
      <circle cx="55" cy="15" r="13" fill="#dc2626"/><text x="55" y="19" text-anchor="middle" fill="#fff" font-size="8">SO₄²⁻</text>
      <circle cx="95" cy="15" r="13" fill="#0284c7"/><text x="95" y="19" text-anchor="middle" fill="#fff" font-size="9">Ba²⁺</text>
      
      <circle cx="15" cy="45" r="13" fill="#dc2626"/><text x="15" y="49" text-anchor="middle" fill="#fff" font-size="8">SO₄²⁻</text>
      <circle cx="55" cy="45" r="13" fill="#0284c7"/><text x="55" y="49" text-anchor="middle" fill="#fff" font-size="9">Ba²⁺</text>
      <circle cx="95" cy="45" r="13" fill="#dc2626"/><text x="95" y="49" text-anchor="middle" fill="#fff" font-size="8">SO₄²⁻</text>
    </g>

    <rect x="20" y="215" width="295" height="90" rx="8" fill="#020617"/>
    <text x="167" y="240" text-anchor="middle" fill="#34d399" font-size="12" font-family="monospace" font-weight="bold">Ba²⁺(aq) + SO₄²⁻(aq) → BaSO₄(s) ↓</text>
    <text x="167" y="265" text-anchor="middle" fill="#4ade80" font-size="11">White Insoluble Precipitate</text>
    <text x="167" y="285" text-anchor="middle" fill="#94a3b8" font-size="10">Na⁺ and Cl⁻ do not participate in reaction</text>
  </g>
</svg>'''
b31_p3 = get_or_create_diagram_block(l31, 3, "Sub-Microscopic Mechanism of Precipitation: Barium Sulfate Lattice Formation")
a31_p3, _ = LessonAsset.objects.get_or_create(id=251, defaults={'lesson': l31, 'asset_type': 'diagram'})
a31_p3.lesson = l31
a31_p3.asset_type = 'diagram'
a31_p3.source_type = 'ai_generated'
a31_p3.storage_type = 'file'
a31_p3.status = 'attached'
a31_p3.title = "Sub-Microscopic Mechanism of Precipitation: Barium Sulfate Lattice Formation"
a31_p3.description = "Particle-level diagram showing barium and sulfate ions joining into an insoluble crystal lattice while spectator sodium and chloride ions remain solvated."
a31_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_31_p3)
a31_p3.file.save(f'precipitation_mechanism_{l31.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a31_p3.blocks.set([b31_p3])
print("Lesson 31 Page 3: Asset 251 saved and attached.")

# P4: Salt Solubility Rules Matrix (Generated SVG)
svg_31_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SOLUBILITY RULES OF COMMON SALTS IN WATER</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Essential Rules for Predicting Insoluble Precipitates in Double Decomposition Reactions</text>

  <!-- Group 1: All Soluble -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">1. ALWAYS SOLUBLE (NO EXCEPTIONS)</text>
    <rect x="15" y="38" width="305" height="98" rx="6" fill="#020617"/>
    <text x="30" y="62" fill="#f8fafc" font-size="11">• All <tspan fill="#38bdf8" font-weight="bold">Nitrates (NO₃⁻)</tspan> are soluble</text>
    <text x="30" y="86" fill="#f8fafc" font-size="11">• All <tspan fill="#38bdf8" font-weight="bold">Group 1 salts (Na⁺, K⁺, Li⁺)</tspan> are soluble</text>
    <text x="30" y="110" fill="#f8fafc" font-size="11">• All <tspan fill="#38bdf8" font-weight="bold">Ammonium salts (NH₄⁺)</tspan> are soluble</text>
  </g>

  <!-- Group 2: Chlorides & Halides -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="150" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">2. CHLORIDES (Cl⁻)</text>
    <rect x="15" y="38" width="305" height="98" rx="6" fill="#020617"/>
    <text x="30" y="62" fill="#4ade80" font-size="11">✓ Most chlorides are soluble</text>
    <text x="30" y="86" fill="#f87171" font-size="11">✗ <tspan font-weight="bold">Insoluble:</tspan> AgCl, PbCl₂ (soluble in hot water)</text>
    <text x="30" y="110" fill="#94a3b8" font-size="10">PbCl₂ precipitates white when cold, dissolves on boiling</text>
  </g>

  <!-- Group 3: Sulfates -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="335" height="165" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">3. SULFATES (SO₄²⁻)</text>
    <rect x="15" y="38" width="305" height="112" rx="6" fill="#020617"/>
    <text x="30" y="62" fill="#4ade80" font-size="11">✓ Most sulfates are soluble</text>
    <text x="30" y="86" fill="#f87171" font-size="11">✗ <tspan font-weight="bold">Insoluble:</tspan> BaSO₄, PbSO₄</text>
    <text x="30" y="110" fill="#fb923c" font-size="11">⚠ <tspan font-weight="bold">Sparingly Soluble:</tspan> CaSO₄</text>
    <text x="30" y="132" fill="#94a3b8" font-size="10">BaSO₄ is used in medical gastrointestinal imaging</text>
  </g>

  <!-- Group 4: Carbonates & Hydroxides -->
  <g transform="translate(420, 245)">
    <rect x="0" y="0" width="335" height="165" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">4. CARBONATES (CO₃²⁻) &amp; HYDROXIDES (OH⁻)</text>
    <rect x="15" y="38" width="305" height="112" rx="6" fill="#020617"/>
    <text x="30" y="62" fill="#f87171" font-size="11">✗ Most carbonates &amp; hydroxides are INSOLUBLE</text>
    <text x="30" y="86" fill="#4ade80" font-size="11">✓ <tspan font-weight="bold">Soluble exceptions:</tspan> Na⁺, K⁺, NH₄⁺</text>
    <text x="30" y="110" fill="#fb923c" font-size="11">⚠ Ca(OH)₂ is sparingly soluble (Lime water)</text>
    <text x="30" y="132" fill="#94a3b8" font-size="10">Used to test for carbon dioxide gas</text>
  </g>
</svg>'''
b31_p4 = get_or_create_diagram_block(l31, 4, "Solubility Rules of Common Salts in Aqueous Solution")
a31_p4, _ = LessonAsset.objects.get_or_create(id=252, defaults={'lesson': l31, 'asset_type': 'diagram'})
a31_p4.lesson = l31
a31_p4.asset_type = 'diagram'
a31_p4.source_type = 'ai_generated'
a31_p4.storage_type = 'file'
a31_p4.status = 'attached'
a31_p4.title = "Solubility Rules of Common Salts in Aqueous Solution"
a31_p4.description = "Summary matrix classifying salts as soluble, sparingly soluble, or insoluble based on their constituent cations and anions."
a31_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_31_p4)
a31_p4.file.save(f'solubility_rules_{l31.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a31_p4.blocks.set([b31_p4])
print("Lesson 31 Page 4: Asset 252 saved and attached.")


# =========================================================================
# LESSON 32: Complex Ions
# =========================================================================
l32 = Lesson.objects.get(id=32)
print(f"\nProcessing Lesson 32: {l32.title}")

# P2: Deep Blue Tetraamminecopper Solution (Wikimedia Image)
b32_p2 = get_or_create_diagram_block(l32, 2, "Formation of Deep Royal Blue Tetraamminecopper(II) Solution in Excess Ammonia")
a32_p2, _ = LessonAsset.objects.get_or_create(id=253, defaults={'lesson': l32, 'asset_type': 'image'})
a32_p2.lesson = l32
a32_p2.asset_type = 'image'
a32_p2.source_type = 'external'
a32_p2.storage_type = 'url'
a32_p2.status = 'attached'
a32_p2.title = "Formation of Deep Royal Blue Tetraamminecopper(II) Solution in Excess Ammonia"
a32_p2.description = "Photograph of deep royal blue tetraamminecopper(II) sulfate complex solution formed when pale blue copper(II) hydroxide precipitate dissolves in excess aqueous ammonia."
a32_p2.url = "https://upload.wikimedia.org/wikipedia/commons/d/d3/Copper_tetrammine_sulfate.jpg"
a32_p2.metadata = {
    'author': 'W. Oelen',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'W. Oelen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Copper_tetrammine_sulfate.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Complex ion formation with ammonia ligands'
}
a32_p2.save()
a32_p2.blocks.set([b32_p2])
print("Lesson 32 Page 2: Asset 253 attached.")

# P4 (Block 1137): Hydroxide Complex Ions in Excess NaOH (Generated SVG)
svg_32_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">COMPLEX IONS WITH HYDROXIDE LIGANDS (EXCESS NaOH)</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Amphoteric Hydroxides Dissolve in Excess OH⁻ to Form Soluble Complex Anions</text>

  <!-- 3 Dissolving Amphoteric Cations -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="460" height="325" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="230" y="26" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">SOLUBLE IN EXCESS NaOH (AMPHOTERIC CATIONS)</text>

    <!-- Zinc Row -->
    <rect x="15" y="42" width="430" height="75" rx="8" fill="#020617"/>
    <text x="30" y="64" fill="#38bdf8" font-size="11" font-weight="bold">Zinc (Zn²⁺):</text>
    <text x="30" y="84" fill="#cbd5e1" font-size="10" font-family="monospace">Zn(OH)₂(s) + 2OH⁻(aq) → [Zn(OH)₄]²⁻(aq)</text>
    <text x="30" y="102" fill="#4ade80" font-size="10">Tetrahydroxozincate(II) ion (Clear, colourless solution)</text>

    <!-- Aluminium Row -->
    <rect x="15" y="125" width="430" height="75" rx="8" fill="#020617"/>
    <text x="30" y="147" fill="#fbbf24" font-size="11" font-weight="bold">Aluminium (Al³⁺):</text>
    <text x="30" y="167" fill="#cbd5e1" font-size="10" font-family="monospace">Al(OH)₃(s) + OH⁻(aq) → [Al(OH)₄]⁻(aq)</text>
    <text x="30" y="185" fill="#4ade80" font-size="10">Tetrahydroxoaluminate(III) ion (Clear, colourless solution)</text>

    <!-- Lead Row -->
    <rect x="15" y="208" width="430" height="75" rx="8" fill="#020617"/>
    <text x="30" y="230" fill="#c084fc" font-size="11" font-weight="bold">Lead (Pb²⁺):</text>
    <text x="30" y="250" fill="#cbd5e1" font-size="10" font-family="monospace">Pb(OH)₂(s) + 2OH⁻(aq) → [Pb(OH)₄]²⁻(aq)</text>
    <text x="30" y="268" fill="#4ade80" font-size="10">Tetrahydroxoplumbate(II) ion (Clear, colourless solution)</text>

    <text x="230" y="308" text-anchor="middle" fill="#94a3b8" font-size="10">White precipitates dissolve completely in excess alkali</text>
  </g>

  <!-- Insoluble Non-Amphoteric Cations -->
  <g transform="translate(525, 80)">
    <rect x="0" y="0" width="230" height="325" rx="14" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="115" y="26" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">INSOLUBLE IN EXCESS NaOH</text>
    
    <rect x="15" y="42" width="200" height="260" rx="8" fill="#020617"/>
    <text x="25" y="70" fill="#f87171" font-size="11" font-weight="bold">• Cu(OH)₂ (s)</text>
    <text x="25" y="88" fill="#cbd5e1" font-size="10">Pale blue solid remains</text>

    <text x="25" y="125" fill="#f87171" font-size="11" font-weight="bold">• Fe(OH)₂ (s)</text>
    <text x="25" y="143" fill="#cbd5e1" font-size="10">Dirty green solid remains</text>

    <text x="25" y="180" fill="#f87171" font-size="11" font-weight="bold">• Fe(OH)₃ (s)</text>
    <text x="25" y="198" fill="#cbd5e1" font-size="10">Reddish-brown solid remains</text>

    <text x="25" y="235" fill="#f87171" font-size="11" font-weight="bold">• Mg(OH)₂ &amp; Ca(OH)₂</text>
    <text x="25" y="253" fill="#cbd5e1" font-size="10">White solids remain</text>
  </g>
</svg>'''
b32_p4 = LessonBlock.objects.get(id=1137)
b32_p4.title = "Formation of Soluble Hydroxide Complex Ions in Excess Sodium Hydroxide"
b32_p4.save()
a32_p4, _ = LessonAsset.objects.get_or_create(id=254, defaults={'lesson': l32, 'asset_type': 'diagram'})
a32_p4.lesson = l32
a32_p4.asset_type = 'diagram'
a32_p4.source_type = 'ai_generated'
a32_p4.storage_type = 'file'
a32_p4.status = 'attached'
a32_p4.title = "Formation of Soluble Hydroxide Complex Ions in Excess Sodium Hydroxide"
a32_p4.description = "Diagram summarizing the dissolution of amphoteric zinc, aluminium, and lead hydroxides in excess NaOH forming soluble tetrahydroxo complex anions."
a32_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_32_p4)
a32_p4.file.save(f'hydroxide_complex_ions_{l32.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a32_p4.blocks.set([b32_p4])
print("Lesson 32 Page 4: Asset 254 saved and attached.")

# P5 (Block 1139): Ammonia Ligand Discrimination (Generated SVG)
svg_32_p5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DISTINGUISHING CATIONS USING EXCESS AQUEOUS AMMONIA (NH₃)</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Only Zinc and Copper(II) Form Soluble Ammine Complexes with Excess Ammonia</text>

  <!-- Left: Soluble in Excess Ammonia -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">DISSOLVE IN EXCESS NH₃ (SOLUBLE)</text>

    <!-- Zinc -->
    <rect x="15" y="45" width="305" height="110" rx="8" fill="#020617"/>
    <text x="25" y="68" fill="#38bdf8" font-size="11" font-weight="bold">1. Zinc Hydroxide (Zn(OH)₂)</text>
    <text x="25" y="88" fill="#cbd5e1" font-size="9" font-family="monospace">Zn(OH)₂(s) + 4NH₃(aq) → [Zn(NH₃)₄]²⁺ + 2OH⁻</text>
    <text x="25" y="112" fill="#4ade80" font-size="10">✓ Forms colourless [Zn(NH₃)₄]²⁺ solution</text>
    <text x="25" y="132" fill="#94a3b8" font-size="9">Tetraamminezinc(II) ion</text>

    <!-- Copper -->
    <rect x="15" y="165" width="305" height="110" rx="8" fill="#020617"/>
    <text x="25" y="188" fill="#60a5fa" font-size="11" font-weight="bold">2. Copper(II) Hydroxide (Cu(OH)₂)</text>
    <text x="25" y="208" fill="#cbd5e1" font-size="9" font-family="monospace">Cu(OH)₂(s) + 4NH₃(aq) → [Cu(NH₃)₄]²⁺ + 2OH⁻</text>
    <text x="25" y="232" fill="#4ade80" font-size="10">✓ Forms deep royal blue solution</text>
    <text x="25" y="252" fill="#94a3b8" font-size="9">Tetraamminecopper(II) ion</text>

    <text x="167" y="305" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">Dative coordinate covalent bonds donate lone pairs</text>
  </g>

  <!-- Right: Insoluble in Excess Ammonia (Crucial Distinction) -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">INSOLUBLE IN EXCESS NH₃ (KEY TEST!)</text>

    <!-- Aluminium & Lead -->
    <rect x="15" y="45" width="305" height="110" rx="8" fill="#020617"/>
    <text x="25" y="68" fill="#fbbf24" font-size="11" font-weight="bold">Aluminium (Al³⁺) &amp; Lead (Pb²⁺)</text>
    <text x="25" y="92" fill="#f87171" font-size="10">✗ White precipitates DO NOT dissolve</text>
    <text x="25" y="112" fill="#cbd5e1" font-size="9">Al(OH)₃(s) and Pb(OH)₂(s) remain insoluble</text>
    <text x="25" y="132" fill="#fde047" font-size="9">Distinguishes Al³⁺ / Pb²⁺ from Zn²⁺ !</text>

    <!-- Iron & Calcium -->
    <rect x="15" y="165" width="305" height="110" rx="8" fill="#020617"/>
    <text x="25" y="188" fill="#fbbf24" font-size="11" font-weight="bold">Iron (Fe²⁺, Fe³⁺) &amp; Calcium (Ca²⁺)</text>
    <text x="25" y="212" fill="#f87171" font-size="10">✗ Hydroxides remain insoluble in excess</text>
    <text x="25" y="232" fill="#cbd5e1" font-size="9">Fe(OH)₂ (dirty green) and Fe(OH)₃ (brown)</text>
    <text x="25" y="252" fill="#94a3b8" font-size="9">Ca²⁺ produces no precipitate with NH₃(aq)</text>

    <text x="167" y="305" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Primary diagnostic qualitative analysis tool</text>
  </g>
</svg>'''
b32_p5 = LessonBlock.objects.get(id=1139)
b32_p5.title = "Distinguishing Metal Cations Using Excess Aqueous Ammonia"
b32_p5.save()
a32_p5, _ = LessonAsset.objects.get_or_create(id=255, defaults={'lesson': l32, 'asset_type': 'diagram'})
a32_p5.lesson = l32
a32_p5.asset_type = 'diagram'
a32_p5.source_type = 'ai_generated'
a32_p5.storage_type = 'file'
a32_p5.status = 'attached'
a32_p5.title = "Distinguishing Metal Cations Using Excess Aqueous Ammonia"
a32_p5.description = "Diagnostic chart showing how excess aqueous ammonia dissolves zinc and copper(II) hydroxides into soluble ammine complexes while leaving aluminium and lead hydroxides insoluble."
a32_p5.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_32_p5)
a32_p5.file.save(f'ammonia_complex_discrimination_{l32.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a32_p5.blocks.set([b32_p5])
print("Lesson 32 Page 5: Asset 255 saved and attached.")


# =========================================================================
# LESSON 33: Solubility and Solubility Curves
# =========================================================================
l33 = Lesson.objects.get(id=33)
print(f"\nProcessing Lesson 33: {l33.title}")

# P2: Rock Candy Sucrose Crystals (Wikimedia Image)
b33_p2 = get_or_create_diagram_block(l33, 2, "Crystalline Sucrose Formed by Saturated Sugar Solution")
a33_p2, _ = LessonAsset.objects.get_or_create(id=256, defaults={'lesson': l33, 'asset_type': 'image'})
a33_p2.lesson = l33
a33_p2.asset_type = 'image'
a33_p2.source_type = 'external'
a33_p2.storage_type = 'url'
a33_p2.status = 'attached'
a33_p2.title = "Crystalline Sucrose Formed by Saturated Sugar Solution"
a33_p2.description = "Macro photograph of large translucent sucrose crystals grown from a hot supersaturated sugar syrup cooled to ambient temperature."
a33_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Kandiszucker_--_2018_--_3588.jpg/960px-Kandiszucker_--_2018_--_3588.jpg"
a33_p2.metadata = {
    'author': 'Dietmar Rabich',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Dietmar Rabich / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Kandiszucker_--_2018_--_3588.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Crystallization from saturated solution'
}
a33_p2.save()
a33_p2.blocks.set([b33_p2])
print("Lesson 33 Page 2: Asset 256 attached.")

# P3: Dynamic Equilibrium at Saturation (Generated SVG)
svg_33_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrEq" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrEqG" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399"/>
    </marker>
  </defs>

  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DYNAMIC EQUILIBRIUM AT THE SATURATION INTERFACE</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">At Saturation: Rate of Dissolution Equals Rate of Crystallization at Constant Temperature</text>

  <!-- Central Solution Beaker -->
  <g transform="translate(180, 80)">
    <rect x="0" y="0" width="440" height="240" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
    <text x="220" y="28" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">SATURATED SOLUTION (Max Dissolved Solute)</text>

    <!-- Dissolved Ions in Solution -->
    <rect x="25" y="45" width="390" height="110" rx="8" fill="#0284c7" fill-opacity="0.15" stroke="#0369a1"/>
    <circle cx="70" cy="80" r="14" fill="#ef4444"/><text x="70" y="84" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">K⁺</text>
    <circle cx="140" cy="110" r="15" fill="#38bdf8"/><text x="140" y="115" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">NO₃⁻</text>
    <circle cx="220" cy="75" r="14" fill="#ef4444"/><text x="220" y="79" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">K⁺</text>
    <circle cx="300" cy="110" r="15" fill="#38bdf8"/><text x="300" y="115" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">NO₃⁻</text>
    <circle cx="370" cy="75" r="14" fill="#ef4444"/><text x="370" y="79" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">K⁺</text>

    <!-- Undissolved Crystal Layer at Bottom -->
    <rect x="25" y="165" width="390" height="60" rx="6" fill="#334155" stroke="#64748b"/>
    <text x="220" y="200" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Excess Undissolved Solid Salt Crystals</text>

    <!-- Dynamic Double Arrows across interface -->
    <path d="M 120 160 L 120 135" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrEq)"/>
    <text x="100" y="148" text-anchor="end" fill="#38bdf8" font-size="10" font-weight="bold">Dissolution</text>

    <path d="M 320 135 L 320 160" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEqG)"/>
    <text x="340" y="148" text-anchor="start" fill="#34d399" font-size="10" font-weight="bold">Crystallization</text>
  </g>

  <!-- Bottom Equality Banner -->
  <rect x="180" y="335" width="440" height="65" rx="10" fill="#020617" stroke="#1e293b"/>
  <text x="400" y="358" text-anchor="middle" fill="#fbbf24" font-size="13" font-family="monospace" font-weight="bold">Undissolved Solute(s) ⇌ Dissolved Ions(aq)</text>
  <text x="400" y="382" text-anchor="middle" fill="#4ade80" font-size="11">Rate of Dissolution = Rate of Precipitation (Mass of solid remains constant)</text>
</svg>'''
b33_p3 = get_or_create_diagram_block(l33, 3, "Dynamic Equilibrium at the Saturated Solution Interface")
a33_p3, _ = LessonAsset.objects.get_or_create(id=257, defaults={'lesson': l33, 'asset_type': 'diagram'})
a33_p3.lesson = l33
a33_p3.asset_type = 'diagram'
a33_p3.source_type = 'ai_generated'
a33_p3.storage_type = 'file'
a33_p3.status = 'attached'
a33_p3.title = "Dynamic Equilibrium at the Saturated Solution Interface"
a33_p3.description = "Diagram illustrating the balance between dissolving solute ions and recrystallizing solid particles in a saturated solution."
a33_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_33_p3)
a33_p3.file.save(f'saturation_equilibrium_{l33.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a33_p3.blocks.set([b33_p3])
print("Lesson 33 Page 3: Asset 257 saved and attached.")

# P6: Solubility Curves of Multiple Salts (Generated SVG)
svg_33_p6 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="32" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="bold">SOLUBILITY TEMPERATURE CURVES OF COMMON SALTS IN WATER</text>
  <text x="400" y="52" text-anchor="middle" fill="#94a3b8" font-size="11">Solubility (g of solute per 100 g of water) as a Function of Temperature (°C)</text>

  <!-- Graph Grid Background -->
  <g transform="translate(80, 70)">
    <rect x="0" y="0" width="460" height="320" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    
    <!-- Horizontal Grid Lines -->
    <line x1="0" y1="280" x2="460" y2="280" stroke="#1e293b" stroke-width="1"/>
    <line x1="0" y1="210" x2="460" y2="210" stroke="#1e293b" stroke-width="1"/>
    <line x1="0" y1="140" x2="460" y2="140" stroke="#1e293b" stroke-width="1"/>
    <line x1="0" y1="70" x2="460" y2="70" stroke="#1e293b" stroke-width="1"/>

    <!-- Y-Axis Labels (g/100g H2O) -->
    <text x="-12" y="324" text-anchor="end" fill="#94a3b8" font-size="10">0</text>
    <text x="-12" y="244" text-anchor="end" fill="#94a3b8" font-size="10">40</text>
    <text x="-12" y="164" text-anchor="end" fill="#94a3b8" font-size="10">80</text>
    <text x="-12" y="84" text-anchor="end" fill="#94a3b8" font-size="10">120</text>
    <text x="-12" y="14" text-anchor="end" fill="#94a3b8" font-size="10">160</text>
    <text x="-35" y="160" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold" transform="rotate(-90 -35 160)">Solubility (g / 100g H₂O)</text>

    <!-- X-Axis Labels (Temperature °C) -->
    <text x="0" y="338" text-anchor="middle" fill="#94a3b8" font-size="10">0°C</text>
    <text x="115" y="338" text-anchor="middle" fill="#94a3b8" font-size="10">25°C</text>
    <text x="230" y="338" text-anchor="middle" fill="#94a3b8" font-size="10">50°C</text>
    <text x="345" y="338" text-anchor="middle" fill="#94a3b8" font-size="10">75°C</text>
    <text x="460" y="338" text-anchor="middle" fill="#94a3b8" font-size="10">100°C</text>
    <text x="230" y="358" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Temperature (°C)</text>

    <!-- Curve 1: KNO3 (Steep rise) -->
    <path d="M 0 300 Q 200 270 460 25" fill="none" stroke="#ef4444" stroke-width="3.5"/>
    
    <!-- Curve 2: KClO3 (Moderate) -->
    <path d="M 0 315 Q 230 290 460 170" fill="none" stroke="#38bdf8" stroke-width="3"/>

    <!-- Curve 3: NaCl (Nearly Flat) -->
    <path d="M 0 250 L 460 238" fill="none" stroke="#fbbf24" stroke-width="2.5"/>

    <!-- Curve 4: Ce2(SO4)3 (Retrograde decrease) -->
    <path d="M 0 290 Q 230 305 460 315" fill="none" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="4"/>
  </g>

  <!-- Right: Curve Key & Explanations -->
  <g transform="translate(565, 70)">
    <rect x="0" y="0" width="190" height="320" rx="10" fill="#1e293b" stroke="#334155"/>
    <text x="95" y="24" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">BEHAVIOR PATTERNS</text>

    <rect x="10" y="38" width="170" height="60" rx="6" fill="#020617"/>
    <text x="18" y="56" fill="#ef4444" font-size="10" font-weight="bold">● KNO₃ (Steep):</text>
    <text x="18" y="72" fill="#cbd5e1" font-size="9">Large solubility increase</text>
    <text x="18" y="86" fill="#94a3b8" font-size="8">Endothermic dissolution</text>

    <rect x="10" y="105" width="170" height="60" rx="6" fill="#020617"/>
    <text x="18" y="123" fill="#38bdf8" font-size="10" font-weight="bold">● KClO₃ (Moderate):</text>
    <text x="18" y="139" fill="#cbd5e1" font-size="9">Steady increase</text>
    <text x="18" y="153" fill="#94a3b8" font-size="8">Moderate enthalpy change</text>

    <rect x="10" y="172" width="170" height="60" rx="6" fill="#020617"/>
    <text x="18" y="190" fill="#fbbf24" font-size="10" font-weight="bold">● NaCl (Flat):</text>
    <text x="18" y="206" fill="#cbd5e1" font-size="9">Almost independent of temp</text>
    <text x="18" y="220" fill="#94a3b8" font-size="8">Requires evaporation</text>

    <rect x="10" y="239" width="170" height="65" rx="6" fill="#020617"/>
    <text x="18" y="257" fill="#c084fc" font-size="10" font-weight="bold">● Ce₂(SO₄)₃ (Retrograde):</text>
    <text x="18" y="273" fill="#cbd5e1" font-size="9">Decreases with heating</text>
    <text x="18" y="287" fill="#94a3b8" font-size="8">Exothermic dissolution</text>
  </g>
</svg>'''
b33_p6 = get_or_create_diagram_block(l33, 6, "Solubility Temperature Curves of Common Salts in Water")
a33_p6, _ = LessonAsset.objects.get_or_create(id=258, defaults={'lesson': l33, 'asset_type': 'diagram'})
a33_p6.lesson = l33
a33_p6.asset_type = 'diagram'
a33_p6.source_type = 'ai_generated'
a33_p6.storage_type = 'file'
a33_p6.status = 'attached'
a33_p6.title = "Solubility Temperature Curves of Common Salts in Water"
a33_p6.description = "Comparative solubility curves graph for potassium nitrate, potassium chlorate, sodium chloride, and cerium sulfate across 0 to 100 degrees Celsius."
a33_p6.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_33_p6)
a33_p6.file.save(f'solubility_curves_{l33.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a33_p6.blocks.set([b33_p6])
print("Lesson 33 Page 6: Asset 258 saved and attached.")


# =========================================================================
# LESSON 34: Hardness of Water
# =========================================================================
l34 = Lesson.objects.get(id=34)
print(f"\nProcessing Lesson 34: {l34.title}")

# P2 (Block 1168): Limestone Cave (Wikimedia Image)
b34_p2 = LessonBlock.objects.get(id=1168)
b34_p2.title = "Limestone Cave Formations (Stalactites and Stalagmites) from Dissolved Calcium Bicarbonate"
b34_p2.save()
a34_p2, _ = LessonAsset.objects.get_or_create(id=259, defaults={'lesson': l34, 'asset_type': 'image'})
a34_p2.lesson = l34
a34_p2.asset_type = 'image'
a34_p2.source_type = 'external'
a34_p2.storage_type = 'url'
a34_p2.status = 'attached'
a34_p2.title = "Limestone Cave Formations (Stalactites and Stalagmites) from Dissolved Calcium Bicarbonate"
a34_p2.description = "Photograph of mineral stalactites and stalagmites formed inside a limestone cave as calcium hydrogen carbonate solution drips and decomposes back into solid calcium carbonate."
a34_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Ishigaki_Stalactite_Cave_%2852117077161%29.jpg/960px-Ishigaki_Stalactite_Cave_%2852117077161%29.jpg"
a34_p2.metadata = {
    'author': 'Raita Futo from Tokyo, Japan',
    'licensing': 'CC BY 2.0',
    'attribution': 'Raita Futo / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Ishigaki_Stalactite_Cave_(52117077161).jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Limestone weathering and calcium bicarbonate formation'
}
a34_p2.save()
a34_p2.blocks.set([b34_p2])
print("Lesson 34 Page 2: Asset 259 attached.")

# P3 (Block 1170): Soap Lather vs Calcium Stearate Scum (Generated SVG)
svg_34_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SOAP IN SOFT WATER VS. HARD WATER SCUM FORMATION</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Calcium and Magnesium Ions Precipitate Sodium Stearate as Insoluble Scum Curds</text>

  <!-- Left: Soft Water (Rich Lather) -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="310" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">SOFT WATER (NO Ca²⁺ / Mg²⁺)</text>

    <rect x="20" y="45" width="295" height="150" rx="8" fill="#047857" fill-opacity="0.15" stroke="#10b981"/>
    <!-- Soap Bubbles / Foam -->
    <circle cx="80" cy="85" r="22" fill="#38bdf8" fill-opacity="0.4" stroke="#38bdf8"/><text x="80" y="89" text-anchor="middle" fill="#fff" font-size="8">Lather</text>
    <circle cx="140" cy="75" r="28" fill="#38bdf8" fill-opacity="0.4" stroke="#38bdf8"/><text x="140" y="79" text-anchor="middle" fill="#fff" font-size="8">Lather</text>
    <circle cx="210" cy="85" r="24" fill="#38bdf8" fill-opacity="0.4" stroke="#38bdf8"/><text x="210" y="89" text-anchor="middle" fill="#fff" font-size="8">Lather</text>
    <circle cx="110" cy="125" r="20" fill="#38bdf8" fill-opacity="0.4" stroke="#38bdf8"/><text x="110" y="129" text-anchor="middle" fill="#fff" font-size="8">Lather</text>
    <circle cx="180" cy="130" r="22" fill="#38bdf8" fill-opacity="0.4" stroke="#38bdf8"/><text x="180" y="134" text-anchor="middle" fill="#fff" font-size="8">Lather</text>

    <rect x="20" y="205" width="295" height="90" rx="8" fill="#020617"/>
    <text x="167" y="230" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Free Stearate Ions Form Micelles &amp; Foam</text>
    <text x="167" y="255" text-anchor="middle" fill="#4ade80" font-size="11">✓ Instant, rich lather produced with soap</text>
    <text x="167" y="278" text-anchor="middle" fill="#94a3b8" font-size="10">Efficient cleansing • Economical soap usage</text>
  </g>

  <!-- Right: Hard Water (Scum Formation) -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="310" rx="14" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">HARD WATER (CONTAINS Ca²⁺ / Mg²⁺)</text>

    <rect x="20" y="45" width="295" height="150" rx="8" fill="#dc2626" fill-opacity="0.15" stroke="#ef4444"/>
    <!-- Grey Curdy Scum Precipitates -->
    <ellipse cx="90" cy="80" rx="35" ry="12" fill="#64748b" stroke="#cbd5e1"/>
    <text x="90" y="84" text-anchor="middle" fill="#fff" font-size="9">Insoluble Scum</text>
    
    <ellipse cx="230" cy="95" rx="40" ry="14" fill="#64748b" stroke="#cbd5e1"/>
    <text x="230" y="99" text-anchor="middle" fill="#fff" font-size="9">Insoluble Scum</text>

    <ellipse cx="150" cy="140" rx="45" ry="15" fill="#64748b" stroke="#cbd5e1"/>
    <text x="150" y="144" text-anchor="middle" fill="#fff" font-size="9">Calcium Stearate</text>

    <rect x="20" y="205" width="295" height="90" rx="8" fill="#020617"/>
    <text x="167" y="228" text-anchor="middle" fill="#fca5a5" font-size="10" font-family="monospace">2C₁₇H₃₅COO⁻ + Ca²⁺ → (C₁₇H₃₅COO)₂Ca(s)↓</text>
    <text x="167" y="255" text-anchor="middle" fill="#f87171" font-size="11">✗ Forms sticky grey scum curds (No lather)</text>
    <text x="167" y="278" text-anchor="middle" fill="#94a3b8" font-size="10">Soap wasted until all Ca²⁺ is precipitated</text>
  </g>
</svg>'''
b34_p3 = LessonBlock.objects.get(id=1170)
b34_p3.title = "Sub-Microscopic Comparison: Soap Lather in Soft Water vs. Calcium Stearate Scum in Hard Water"
b34_p3.save()
a34_p3, _ = LessonAsset.objects.get_or_create(id=260, defaults={'lesson': l34, 'asset_type': 'diagram'})
a34_p3.lesson = l34
a34_p3.asset_type = 'diagram'
a34_p3.source_type = 'ai_generated'
a34_p3.storage_type = 'file'
a34_p3.status = 'attached'
a34_p3.title = "Sub-Microscopic Comparison: Soap Lather in Soft Water vs. Calcium Stearate Scum in Hard Water"
a34_p3.description = "Particle model comparing micelle foam formation in soft water against insoluble calcium stearate precipitation (soap scum) in hard water."
a34_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_34_p3)
a34_p3.file.save(f'soap_lather_vs_scum_{l34.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a34_p3.blocks.set([b34_p3])
print("Lesson 34 Page 3: Asset 260 saved and attached.")


# =========================================================================
# LESSON 35: Disadvantages of Hard Water
# =========================================================================
l35 = Lesson.objects.get(id=35)
print(f"\nProcessing Lesson 35: {l35.title}")

# P2: Boiler Scale (Wikimedia Image)
b35_p2 = get_or_create_diagram_block(l35, 2, "Thick Calcium Carbonate Boiler Scale Deposited Inside an Industrial Heating Vessel")
a35_p2, _ = LessonAsset.objects.get_or_create(id=261, defaults={'lesson': l35, 'asset_type': 'image'})
a35_p2.lesson = l35
a35_p2.asset_type = 'image'
a35_p2.source_type = 'external'
a35_p2.storage_type = 'url'
a35_p2.status = 'attached'
a35_p2.title = "Thick Calcium Carbonate Boiler Scale Deposited Inside an Industrial Heating Vessel"
a35_p2.description = "Photograph showing thick incrustation of calcium carbonate boiler scale coating metal heat exchange surfaces inside an industrial boiler."
a35_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Boiler_Scale.JPG/960px-Boiler_Scale.JPG"
a35_p2.metadata = {
    'author': '1e4cMET',
    'licensing': 'CC BY-SA 3.0',
    'attribution': '1e4cMET / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Boiler_Scale.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Boiler scale incrustation and pipe clogging'
}
a35_p2.save()
a35_p2.blocks.set([b35_p2])
print("Lesson 35 Page 2: Asset 261 attached.")

# P3: Boiler Scale Thermal Insulation Mechanism (Generated SVG)
svg_35_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">THERMAL HAZARD: BOILER SCALE INSULATION &amp; EXPLOSION RISK</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Poor Thermal Conductivity of CaCO₃ Causes Metal Overheating, Pipe Bulging, and Boiler Burst</text>

  <!-- Cross-Section Diagram of Boiler Pipe Wall -->
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="680" height="210" rx="12" fill="#1e293b" stroke="#dc2626" stroke-width="2"/>

    <!-- Heat Source at Bottom -->
    <rect x="20" y="165" width="640" height="35" rx="6" fill="#b91c1c"/>
    <text x="340" y="188" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">FURNACE FLAME / EXTERNAL HEAT SOURCE (~900°C)</text>

    <!-- Metal Wall (Overheating) -->
    <rect x="20" y="110" width="640" height="50" fill="#f97316"/>
    <text x="340" y="140" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="bold">BOILER STEEL WALL (OVERHEATED &amp; WEAKENED)</text>

    <!-- Insulating Limescale Layer -->
    <rect x="20" y="60" width="640" height="45" fill="#e2e8f0" stroke="#94a3b8"/>
    <text x="340" y="88" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="bold">INSULATING CaCO₃ SCALE LAYER (POOR THERMAL CONDUCTOR)</text>

    <!-- Boiling Water Interior -->
    <rect x="20" y="15" width="640" height="40" rx="6" fill="#0284c7" fill-opacity="0.3"/>
    <text x="340" y="38" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">WATER INTERIOR (Under High Pressure)</text>
  </g>

  <!-- Hazards Summary Box -->
  <g transform="translate(60, 305)">
    <rect x="0" y="0" width="680" height="85" rx="10" fill="#020617" stroke="#334155"/>
    <text x="340" y="28" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">The Triple Danger of Boiler Scale:</text>
    <text x="340" y="50" text-anchor="middle" fill="#cbd5e1" font-size="11">1. Fuel Wasted: Requires massive excess fuel to conduct heat through scale</text>
    <text x="340" y="68" text-anchor="middle" fill="#fca5a5" font-size="11">2. Catastrophic Explosion: Scale cracks → water contacts red-hot metal → violent steam expansion</text>
  </g>
</svg>'''
b35_p3 = get_or_create_diagram_block(l35, 3, "Thermal Insulation and Metal Fatigue Caused by Boiler Scale in Industrial Boilers")
a35_p3, _ = LessonAsset.objects.get_or_create(id=262, defaults={'lesson': l35, 'asset_type': 'diagram'})
a35_p3.lesson = l35
a35_p3.asset_type = 'diagram'
a35_p3.source_type = 'ai_generated'
a35_p3.storage_type = 'file'
a35_p3.status = 'attached'
a35_p3.title = "Thermal Insulation and Metal Fatigue Caused by Boiler Scale in Industrial Boilers"
a35_p3.description = "Cross-section schematic explaining how calcium carbonate boiler scale insulates heat transfer, causing localized steel overheating and steam explosion hazard."
a35_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_35_p3)
a35_p3.file.save(f'boiler_scale_hazard_{l35.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a35_p3.blocks.set([b35_p3])
print("Lesson 35 Page 3: Asset 262 saved and attached.")


# =========================================================================
# LESSON 36: Advantages of Hard Water
# =========================================================================
l36 = Lesson.objects.get(id=36)
print(f"\nProcessing Lesson 36: {l36.title}")

# P2: Heavy Lead Water Main Pipe (Wikimedia Image)
b36_p2 = get_or_create_diagram_block(l36, 2, "Heavy Municipal Lead Water Main Pipe")
a36_p2, _ = LessonAsset.objects.get_or_create(id=263, defaults={'lesson': l36, 'asset_type': 'image'})
a36_p2.lesson = l36
a36_p2.asset_type = 'image'
a36_p2.source_type = 'external'
a36_p2.storage_type = 'url'
a36_p2.status = 'attached'
a36_p2.title = "Heavy Municipal Lead Water Main Pipe"
a36_p2.description = "Photograph of a historic lead drinking water main pipe excavated during municipal infrastructure inspection."
a36_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/DC_WASA_lead_water_main.jpg/960px-DC_WASA_lead_water_main.jpg"
a36_p2.metadata = {
    'author': 'IntangibleArts',
    'licensing': 'CC BY 2.0',
    'attribution': 'IntangibleArts / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:DC_WASA_lead_water_main.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Lead plumbing and internal pipe passivation'
}
a36_p2.save()
a36_p2.blocks.set([b36_p2])
print("Lesson 36 Page 2: Asset 263 attached.")

# P3: Lead Passivation Mechanism (Generated SVG)
svg_36_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">LEAD PIPE PASSIVATION: SOFT WATER VS. HARD WATER</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Hard Water Forms an Insoluble Protective Coating that Prevents Toxic Lead Dissolution</text>

  <!-- Left: Soft Water (Toxic Leaching) -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="310" rx="14" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">SOFT WATER (NO CO₃²⁻ / SO₄²⁻)</text>

    <!-- Pipe Cross Section -->
    <rect x="20" y="45" width="295" height="150" rx="8" fill="#7f1d1d" fill-opacity="0.3" stroke="#ef4444"/>
    <rect x="20" y="45" width="25" height="150" fill="#64748b"/><text x="32" y="125" fill="#fff" font-size="9" transform="rotate(-90 32 125)">Lead Wall</text>
    <rect x="290" y="45" width="25" height="150" fill="#64748b"/>

    <!-- Leached Toxic Pb2+ Ions in Water -->
    <circle cx="100" cy="85" r="14" fill="#dc2626"/><text x="100" y="89" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">Pb²⁺</text>
    <circle cx="190" cy="115" r="14" fill="#dc2626"/><text x="190" y="119" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">Pb²⁺</text>
    <circle cx="130" cy="155" r="14" fill="#dc2626"/><text x="130" y="159" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">Pb²⁺</text>
    <circle cx="230" cy="80" r="14" fill="#dc2626"/><text x="230" y="84" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">Pb²⁺</text>

    <rect x="20" y="205" width="295" height="90" rx="8" fill="#020617"/>
    <text x="167" y="230" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">TOXIC LEAD POISONING RISK</text>
    <text x="167" y="255" text-anchor="middle" fill="#fca5a5" font-size="10">Soft acidic water corrodes bare lead</text>
    <text x="167" y="275" text-anchor="middle" fill="#cbd5e1" font-size="9">Damages neurological and kidney development</text>
  </g>

  <!-- Right: Hard Water (Protective Insoluble Barrier) -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="310" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">HARD WATER (CONTAINS CO₃²⁻ &amp; SO₄²⁻)</text>

    <!-- Pipe Cross Section with Protective Lining -->
    <rect x="20" y="45" width="295" height="150" rx="8" fill="#047857" fill-opacity="0.2" stroke="#10b981"/>
    <rect x="20" y="45" width="20" height="150" fill="#64748b"/>
    <rect x="40" y="45" width="15" height="150" fill="#fde047"/><text x="47" y="125" fill="#0f172a" font-size="8" font-weight="bold" transform="rotate(-90 47 125)">PbCO₃ Layer</text>
    
    <rect x="295" y="45" width="20" height="150" fill="#64748b"/>
    <rect x="280" y="45" width="15" height="150" fill="#fde047"/>

    <!-- Safe Clean Water Interior -->
    <text x="167" y="115" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">SAFE DRINKING WATER</text>
    <text x="167" y="135" text-anchor="middle" fill="#7dd3fc" font-size="10">(No dissolved lead ions)</text>

    <rect x="20" y="205" width="295" height="90" rx="8" fill="#020617"/>
    <text x="167" y="228" text-anchor="middle" fill="#34d399" font-size="10" font-family="monospace">Pb²⁺ + CO₃²⁻ → PbCO₃(s) (Insoluble)</text>
    <text x="167" y="255" text-anchor="middle" fill="#4ade80" font-size="11">✓ Insoluble liner coats pipe interior</text>
    <text x="167" y="275" text-anchor="middle" fill="#cbd5e1" font-size="9">Completely blocks lead from leaching into water</text>
  </g>
</svg>'''
b36_p3 = get_or_create_diagram_block(l36, 3, "Internal Passivation: How Hard Water Prevents Toxic Lead Leaching in Pipes")
a36_p3, _ = LessonAsset.objects.get_or_create(id=264, defaults={'lesson': l36, 'asset_type': 'diagram'})
a36_p3.lesson = l36
a36_p3.asset_type = 'diagram'
a36_p3.source_type = 'ai_generated'
a36_p3.storage_type = 'file'
a36_p3.status = 'attached'
a36_p3.title = "Internal Passivation: How Hard Water Prevents Toxic Lead Leaching in Pipes"
a36_p3.description = "Diagram comparing bare lead corrosion in soft water with insoluble lead(II) carbonate protective passivation in hard water."
a36_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_36_p3)
a36_p3.file.save(f'lead_pipe_passivation_{l36.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a36_p3.blocks.set([b36_p3])
print("Lesson 36 Page 3: Asset 264 saved and attached.")


# =========================================================================
# LESSON 37: Methods of Removing Hardness of Water
# =========================================================================
l37 = Lesson.objects.get(id=37)
print(f"\nProcessing Lesson 37: {l37.title}")

# P2: Natural Zeolite Crystals (Wikimedia Image)
b37_p2 = get_or_create_diagram_block(l37, 2, "Natural Crystalline Zeolite (Goosecreekite) Mineral Used for Ion Exchange")
a37_p2, _ = LessonAsset.objects.get_or_create(id=265, defaults={'lesson': l37, 'asset_type': 'image'})
a37_p2.lesson = l37
a37_p2.asset_type = 'image'
a37_p2.source_type = 'external'
a37_p2.storage_type = 'url'
a37_p2.status = 'attached'
a37_p2.title = "Natural Crystalline Zeolite (Goosecreekite) Mineral Used for Ion Exchange"
a37_p2.description = "Photograph of natural aluminosilicate zeolite crystal mineral containing microporous cage structures and exchangeable cations used in water softening."
a37_p2.url = "https://upload.wikimedia.org/wikipedia/commons/2/2b/Goosecreekite-Quartz-201705.jpg"
a37_p2.metadata = {
    'author': 'Robert M. Lavinsky',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Robert M. Lavinsky / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Goosecreekite-Quartz-201705.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Zeolite structure and ion exchange mineralogy'
}
a37_p2.save()
a37_p2.blocks.set([b37_p2])
print("Lesson 37 Page 2: Asset 265 attached.")

# P3 (Block 1196): Ion Exchange Resin Column & Regeneration (Generated SVG)
svg_37_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrZeo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">ION EXCHANGE COLUMN: WATER SOFTENING &amp; REGENERATION</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Sodium Zeolite (Na₂Z) Exchanges 2Na⁺ for Each Ca²⁺/Mg²⁺ Ion in Both Temporary and Permanent Hard Water</text>

  <!-- Left: Softening Cycle -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">CYCLE 1: HARD WATER SOFTENING</text>

    <!-- Column Cylinder -->
    <rect x="35" y="45" width="265" height="150" rx="8" fill="#0284c7" fill-opacity="0.15" stroke="#0284c7"/>
    <text x="167" y="65" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">Hard Water In (Ca²⁺ + Mg²⁺)</text>

    <!-- Zeolite Resin Bed -->
    <rect x="55" y="80" width="225" height="70" rx="6" fill="#334155" stroke="#38bdf8"/>
    <text x="167" y="110" text-anchor="middle" fill="#fde047" font-size="11" font-weight="bold">Sodium Zeolite Bed (Na₂Z)</text>
    <text x="167" y="130" text-anchor="middle" fill="#cbd5e1" font-size="9">Ca²⁺ trapped → 2Na⁺ released</text>

    <text x="167" y="180" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="bold">Soft Water Out (Na⁺ ions)</text>

    <rect x="15" y="205" width="305" height="105" rx="8" fill="#020617"/>
    <text x="167" y="228" text-anchor="middle" fill="#38bdf8" font-size="10" font-family="monospace">Na₂Z(s) + Ca²⁺(aq) → CaZ(s) + 2Na⁺(aq)</text>
    <text x="167" y="252" text-anchor="middle" fill="#4ade80" font-size="11">✓ Removes both Temp &amp; Perm Hardness</text>
    <text x="167" y="272" text-anchor="middle" fill="#94a3b8" font-size="10">Water contains harmless Na⁺ ions</text>
    <text x="167" y="292" text-anchor="middle" fill="#94a3b8" font-size="9">Continuous flow without boiling or filtering</text>
  </g>

  <!-- Right: Regeneration with Brine -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">CYCLE 2: RESIN REGENERATION (BRINE)</text>

    <!-- Column Cylinder -->
    <rect x="35" y="45" width="265" height="150" rx="8" fill="#047857" fill-opacity="0.15" stroke="#10b981"/>
    <text x="167" y="65" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Concentrated NaCl Brine In</text>

    <!-- Exhausted Bed -->
    <rect x="55" y="80" width="225" height="70" rx="6" fill="#334155" stroke="#10b981"/>
    <text x="167" y="110" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">Exhausted Bed (CaZ)</text>
    <text x="167" y="130" text-anchor="middle" fill="#cbd5e1" font-size="9">High [Na⁺] displaces Ca²⁺ ions</text>

    <text x="167" y="180" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">Waste Brine Out (CaCl₂)</text>

    <rect x="15" y="205" width="305" height="105" rx="8" fill="#020617"/>
    <text x="167" y="228" text-anchor="middle" fill="#34d399" font-size="10" font-family="monospace">CaZ(s) + 2NaCl(aq) → Na₂Z(s) + CaCl₂(aq)</text>
    <text x="167" y="252" text-anchor="middle" fill="#34d399" font-size="11">✓ Resin Fully Restored to Na₂Z</text>
    <text x="167" y="272" text-anchor="middle" fill="#94a3b8" font-size="10">Recharged zeolite ready for reuse</text>
    <text x="167" y="292" text-anchor="middle" fill="#94a3b8" font-size="9">Cost-effective industrial cycle</text>
  </g>
</svg>'''
b37_p3 = LessonBlock.objects.get(id=1196)
b37_p3.title = "Mechanism of Ion Exchange Water Softening and Resin Regeneration"
b37_p3.save()
a37_p3, _ = LessonAsset.objects.get_or_create(id=266, defaults={'lesson': l37, 'asset_type': 'diagram'})
a37_p3.lesson = l37
a37_p3.asset_type = 'diagram'
a37_p3.source_type = 'ai_generated'
a37_p3.storage_type = 'file'
a37_p3.status = 'attached'
a37_p3.title = "Mechanism of Ion Exchange Water Softening and Resin Regeneration"
a37_p3.description = "Schematic of ion exchange zeolite water softening showing displacement of calcium ions by sodium, followed by resin regeneration with brine."
a37_p3.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_37_p3)
a37_p3.file.save(f'ion_exchange_mechanism_{l37.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a37_p3.blocks.set([b37_p3])
print("Lesson 37 Page 3: Asset 266 saved and attached.")

# P4: Classification of Hardness Removal Methods (Generated SVG)
svg_37_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">METHODS FOR REMOVING WATER HARDNESS</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Chemical Applicability Matrix: Temporary Hardness vs. Permanent Hardness</text>

  <!-- Left: Temporary Only Methods -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">TEMPORARY HARDNESS ONLY (Ca(HCO₃)₂)</text>

    <!-- Method 1: Boiling -->
    <rect x="15" y="42" width="305" height="120" rx="8" fill="#020617"/>
    <text x="25" y="64" fill="#fbbf24" font-size="11" font-weight="bold">1. Boiling:</text>
    <text x="25" y="84" fill="#cbd5e1" font-size="9" font-family="monospace">Ca(HCO₃)₂(aq) → CaCO₃(s)↓ + H₂O + CO₂</text>
    <text x="25" y="108" fill="#f87171" font-size="10">✗ Fails for permanent hardness</text>
    <text x="25" y="128" fill="#94a3b8" font-size="9">CaSO₄ / MgSO₄ are thermally stable</text>

    <!-- Method 2: Slaked Lime -->
    <rect x="15" y="175" width="305" height="120" rx="8" fill="#020617"/>
    <text x="25" y="197" fill="#fbbf24" font-size="11" font-weight="bold">2. Addition of Slaked Lime (Ca(OH)₂):</text>
    <text x="25" y="217" fill="#cbd5e1" font-size="9" font-family="monospace">Ca(HCO₃)₂ + Ca(OH)₂ → 2CaCO₃(s)↓ + 2H₂O</text>
    <text x="25" y="241" fill="#fb923c" font-size="10">⚠ Exact stoichiometric amount required</text>
    <text x="25" y="261" fill="#94a3b8" font-size="9">Excess Ca(OH)₂ introduces new hardness</text>
  </g>

  <!-- Right: Both Temporary & Permanent Methods -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">BOTH TEMPORARY &amp; PERMANENT HARDNESS</text>

    <!-- Method 3: Washing Soda -->
    <rect x="15" y="42" width="305" height="85" rx="8" fill="#020617"/>
    <text x="25" y="62" fill="#34d399" font-size="11" font-weight="bold">3. Washing Soda (Na₂CO₃):</text>
    <text x="25" y="80" fill="#cbd5e1" font-size="9" font-family="monospace">Ca²⁺(aq) + CO₃²⁻(aq) → CaCO₃(s)↓</text>
    <text x="25" y="102" fill="#4ade80" font-size="9">✓ Precipitates all Ca²⁺ and Mg²⁺ as carbonates</text>

    <!-- Method 4: Ion Exchange -->
    <rect x="15" y="135" width="305" height="85" rx="8" fill="#020617"/>
    <text x="25" y="155" fill="#38bdf8" font-size="11" font-weight="bold">4. Ion Exchange (Permutit / Zeolite):</text>
    <text x="25" y="173" fill="#cbd5e1" font-size="9" font-family="monospace">Na₂Z(s) + Ca²⁺(aq) → CaZ(s) + 2Na⁺(aq)</text>
    <text x="25" y="195" fill="#4ade80" font-size="9">✓ Modern standard; easily regenerated with brine</text>

    <!-- Method 5: Distillation -->
    <rect x="15" y="228" width="305" height="85" rx="8" fill="#020617"/>
    <text x="25" y="248" fill="#c084fc" font-size="11" font-weight="bold">5. Distillation:</text>
    <text x="25" y="268" fill="#cbd5e1" font-size="9">Pure water vaporizes; all dissolved minerals remain</text>
    <text x="25" y="288" fill="#94a3b8" font-size="9">100% pure deionised water (expensive energy cost)</text>
  </g>
</svg>'''
b37_p4 = get_or_create_diagram_block(l37, 4, "Classification Decision Matrix: Methods for Removing Temporary and Permanent Water Hardness")
a37_p4, _ = LessonAsset.objects.get_or_create(id=267, defaults={'lesson': l37, 'asset_type': 'diagram'})
a37_p4.lesson = l37
a37_p4.asset_type = 'diagram'
a37_p4.source_type = 'ai_generated'
a37_p4.storage_type = 'file'
a37_p4.status = 'attached'
a37_p4.title = "Classification Decision Matrix: Methods for Removing Temporary and Permanent Water Hardness"
a37_p4.description = "Decision matrix classifying the five standard methods for softening water based on whether they remove temporary hardness, permanent hardness, or both."
a37_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_37_p4)
a37_p4.file.save(f'water_softening_classification_{l37.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a37_p4.blocks.set([b37_p4])
print("Lesson 37 Page 4: Asset 267 saved and attached.")

print("\n=== Second Half of Topic 1 (Lessons 31–37) Enriched Successfully! ===")
