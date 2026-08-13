import os
import sys
import django

from django.core.files.base import ContentFile
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Lessons 29, 30, 27, 18, 11, 19 ===")

# =========================================================================
# 1. LESSON 29: Strength of Acids
# =========================================================================
lesson_29 = Lesson.objects.get(id=29)
print(f"\nProcessing Lesson 29: {lesson_29.title}")

# Page 2 (Block 1053): Lead-Acid Battery (Wikimedia)
block_29_p2 = LessonBlock.objects.get(id=1053)
block_29_p2.title = "Lead-Acid Car Battery Containing Sulfuric Acid Electrolyte"
block_29_p2.save()

asset_230, _ = LessonAsset.objects.get_or_create(id=230, defaults={'lesson': lesson_29, 'asset_type': 'image'})
asset_230.lesson = lesson_29
asset_230.asset_type = 'image'
asset_230.source_type = 'external'
asset_230.storage_type = 'url'
asset_230.status = 'attached'
asset_230.title = "Lead-Acid Car Battery Containing Sulfuric Acid Electrolyte"
asset_230.description = "Photograph of a commercial lead-acid automotive battery utilizing sulfuric acid electrolyte solution."
asset_230.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/12V_7.5_Ah_Lead_Acid_Battery.JPG/960px-12V_7.5_Ah_Lead_Acid_Battery.JPG"
asset_230.metadata = {
    'author': 'BrittanyJ',
    'licensing': 'Public domain',
    'attribution': 'BrittanyJ / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:12V_7.5_Ah_Lead_Acid_Battery.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Strong acid in industrial and automotive applications'
}
asset_230.save()
asset_230.blocks.set([block_29_p2])
print("Lesson 29 Page 2: Asset 230 attached to Block 1053.")

# Page 3 (Block 1055): Strong vs Weak Acid Dissociation (Generated SVG)
svg_29_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="beakerStrong" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="beakerWeak" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.35"/>
    </linearGradient>
    <radialGradient id="hIon" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </radialGradient>
    <radialGradient id="clIon" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </radialGradient>
  </defs>

  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DEGREE OF DISSOCIATION: STRONG VS. WEAK ACIDS</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Same Molar Concentration (1.0 M) Yielding Completely Different Ion Populations</text>

  <!-- Left: Strong Acid Beaker -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">STRONG ACID: 1.0 M HCl</text>
    <text x="167" y="46" text-anchor="middle" fill="#7dd3fc" font-size="11">100% Complete Dissociation (No Intact HCl Molecules)</text>

    <!-- Beaker Interior -->
    <rect x="25" y="65" width="285" height="150" rx="8" fill="url(#beakerStrong)" stroke="#38bdf8" stroke-width="1"/>
    
    <!-- Dense Ions in Solution -->
    <circle cx="65" cy="100" r="14" fill="url(#hIon)"/><text x="65" y="104" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">H⁺</text>
    <circle cx="120" cy="140" r="16" fill="url(#clIon)"/><text x="120" y="145" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Cl⁻</text>
    
    <circle cx="180" cy="95" r="14" fill="url(#hIon)"/><text x="180" y="99" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">H⁺</text>
    <circle cx="230" cy="135" r="16" fill="url(#clIon)"/><text x="230" y="140" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Cl⁻</text>
    
    <circle cx="150" cy="180" r="14" fill="url(#hIon)"/><text x="150" y="184" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">H⁺</text>
    <circle cx="270" cy="180" r="16" fill="url(#clIon)"/><text x="270" y="185" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Cl⁻</text>

    <!-- Equation and Properties -->
    <rect x="25" y="225" width="285" height="85" rx="8" fill="#020617" stroke="#0f172a"/>
    <text x="167" y="248" text-anchor="middle" fill="#38bdf8" font-size="12" font-family="monospace" font-weight="bold">HCl(aq) → H⁺(aq) + Cl⁻(aq)</text>
    <text x="167" y="272" text-anchor="middle" fill="#4ade80" font-size="11">✓ High [H⁺] ≈ 1.0 mol/dm³ (pH ≈ 0–1)</text>
    <text x="167" y="292" text-anchor="middle" fill="#94a3b8" font-size="10">High electrical conductivity • Vigorous effervescence</text>
  </g>

  <!-- Right: Weak Acid Beaker -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">WEAK ACID: 1.0 M CH₃COOH</text>
    <text x="167" y="46" text-anchor="middle" fill="#fde68a" font-size="11">Partial Dissociation (&lt; 1% Splits into Ions)</text>

    <!-- Beaker Interior -->
    <rect x="25" y="65" width="285" height="150" rx="8" fill="url(#beakerWeak)" stroke="#fbbf24" stroke-width="1"/>
    
    <!-- Intact Molecules Predominate -->
    <g transform="translate(70, 105)">
      <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#475569"/>
      <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">CH₃COOH</text>
    </g>
    <g transform="translate(200, 105)">
      <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#475569"/>
      <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">CH₃COOH</text>
    </g>
    <g transform="translate(135, 150)">
      <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#475569"/>
      <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">CH₃COOH</text>
    </g>
    
    <!-- Rare Single Dissociated Pair -->
    <circle cx="65" cy="180" r="12" fill="url(#hIon)"/><text x="65" y="184" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">H⁺</text>
    <g transform="translate(240, 175)">
      <rect x="-42" y="-10" width="84" height="20" rx="10" fill="#2563eb"/>
      <text x="0" y="4" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">CH₃COO⁻</text>
    </g>

    <!-- Equation and Properties -->
    <rect x="25" y="225" width="285" height="85" rx="8" fill="#020617" stroke="#0f172a"/>
    <text x="167" y="248" text-anchor="middle" fill="#fbbf24" font-size="12" font-family="monospace" font-weight="bold">CH₃COOH ⇌ CH₃COO⁻ + H⁺</text>
    <text x="167" y="272" text-anchor="middle" fill="#fb923c" font-size="11">Low [H⁺] ≈ 0.004 mol/dm³ (pH ≈ 3–4)</text>
    <text x="167" y="292" text-anchor="middle" fill="#94a3b8" font-size="10">Low electrical conductivity • Slow effervescence</text>
  </g>
</svg>'''

block_29_p3 = LessonBlock.objects.get(id=1055)
block_29_p3.title = "Particle-Level Dissociation Comparison: Strong Acid vs. Weak Acid"
block_29_p3.save()

asset_231, _ = LessonAsset.objects.get_or_create(id=231, defaults={'lesson': lesson_29, 'asset_type': 'diagram'})
asset_231.lesson = lesson_29
asset_231.asset_type = 'diagram'
asset_231.source_type = 'ai_generated'
asset_231.storage_type = 'file'
asset_231.status = 'attached'
asset_231.title = "Particle-Level Dissociation Comparison: Strong Acid vs. Weak Acid"
asset_231.description = "Comparative particle diagram showing 100% complete ionization in strong acid (HCl) versus reversible equilibrium (< 1% ionization) in weak acid (CH3COOH)."
asset_231.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Degree of dissociation in strong and weak acids'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_29_p3)
asset_231.file.save(f'strong_vs_weak_acid_{lesson_29.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_231.blocks.set([block_29_p3])
print("Lesson 29 Page 3: Asset 231 saved and attached to Block 1055.")


# =========================================================================
# 2. LESSON 30: Bases and Alkalis
# =========================================================================
lesson_30 = Lesson.objects.get(id=30)
print(f"\nProcessing Lesson 30: {lesson_30.title}")

# Page 2 (Block 1063): Soap Bars (Wikimedia)
block_30_p2 = LessonBlock.objects.get(id=1063)
block_30_p2.title = "Traditional Soap Bars Manufactured via Alkaline Saponification"
block_30_p2.save()

asset_232, _ = LessonAsset.objects.get_or_create(id=232, defaults={'lesson': lesson_30, 'asset_type': 'image'})
asset_232.lesson = lesson_30
asset_232.asset_type = 'image'
asset_232.source_type = 'external'
asset_232.storage_type = 'url'
asset_232.status = 'attached'
asset_232.title = "Traditional Soap Bars Manufactured via Alkaline Saponification"
asset_232.description = "Photograph of natural Marseille and Aleppo bar soaps, everyday alkaline cleaning products."
asset_232.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Bars_of_pure_Marseille_and_Aleppo_soap%2C_2024.jpg/960px-Bars_of_pure_Marseille_and_Aleppo_soap%2C_2024.jpg"
asset_232.metadata = {
    'author': 'DimiTalen',
    'licensing': 'CC0',
    'attribution': 'DimiTalen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Bars_of_pure_Marseille_and_Aleppo_soap,_2024.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Everyday household alkalis and slippery feel of bases'
}
asset_232.save()
asset_232.blocks.set([block_30_p2])
print("Lesson 30 Page 2: Asset 232 attached to Block 1063.")

# Page 4 (Block 1066): Strong vs Weak Alkali Dissociation (Generated SVG)
svg_30_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="beakerStrongB" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#047857" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="beakerWeakB" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.35"/>
    </linearGradient>
    <radialGradient id="ohIon" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </radialGradient>
    <radialGradient id="naIon" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </radialGradient>
  </defs>

  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DEGREE OF DISSOCIATION: STRONG VS. WEAK ALKALIS</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Comparing Ionic Lattice Dissociation (NaOH) vs. Equilibrium Molecule Ionization (NH₃)</text>

  <!-- Left: Strong Alkali -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">STRONG ALKALI: 1.0 M NaOH</text>
    <text x="167" y="46" text-anchor="middle" fill="#6ee7b7" font-size="11">100% Lattice Dissociation into Free Ions</text>

    <!-- Beaker Interior -->
    <rect x="25" y="65" width="285" height="150" rx="8" fill="url(#beakerStrongB)" stroke="#10b981" stroke-width="1"/>
    
    <!-- Dense Ions -->
    <circle cx="70" cy="105" r="14" fill="url(#naIon)"/><text x="70" y="109" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="bold">Na⁺</text>
    <circle cx="130" cy="135" r="16" fill="url(#ohIon)"/><text x="130" y="140" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">OH⁻</text>
    <circle cx="190" cy="100" r="14" fill="url(#naIon)"/><text x="190" y="104" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="bold">Na⁺</text>
    <circle cx="240" cy="140" r="16" fill="url(#ohIon)"/><text x="240" y="145" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">OH⁻</text>
    <circle cx="150" cy="180" r="16" fill="url(#ohIon)"/><text x="150" y="185" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">OH⁻</text>
    <circle cx="260" cy="180" r="14" fill="url(#naIon)"/><text x="260" y="184" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="bold">Na⁺</text>

    <!-- Equation and Properties -->
    <rect x="25" y="225" width="285" height="85" rx="8" fill="#020617" stroke="#0f172a"/>
    <text x="167" y="248" text-anchor="middle" fill="#34d399" font-size="12" font-family="monospace" font-weight="bold">NaOH(s) → Na⁺(aq) + OH⁻(aq)</text>
    <text x="167" y="272" text-anchor="middle" fill="#4ade80" font-size="11">✓ High [OH⁻] ≈ 1.0 mol/dm³ (pH ≈ 13–14)</text>
    <text x="167" y="292" text-anchor="middle" fill="#94a3b8" font-size="10">High electrical conductivity • Strongly caustic</text>
  </g>

  <!-- Right: Weak Alkali -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">WEAK ALKALI: 1.0 M NH₃(aq)</text>
    <text x="167" y="46" text-anchor="middle" fill="#7dd3fc" font-size="11">Partial Ionization (&lt; 1% Reacts with Water)</text>

    <!-- Beaker Interior -->
    <rect x="25" y="65" width="285" height="150" rx="8" fill="url(#beakerWeakB)" stroke="#38bdf8" stroke-width="1"/>
    
    <!-- Intact Ammonia Molecules -->
    <g transform="translate(80, 110)"><circle cx="0" cy="0" r="16" fill="#334155"/><text x="0" y="4" text-anchor="middle" fill="#e2e8f0" font-size="10" font-weight="bold">NH₃</text></g>
    <g transform="translate(200, 110)"><circle cx="0" cy="0" r="16" fill="#334155"/><text x="0" y="4" text-anchor="middle" fill="#e2e8f0" font-size="10" font-weight="bold">NH₃</text></g>
    <g transform="translate(140, 150)"><circle cx="0" cy="0" r="16" fill="#334155"/><text x="0" y="4" text-anchor="middle" fill="#e2e8f0" font-size="10" font-weight="bold">NH₃</text></g>

    <!-- Rare Ion Pair -->
    <g transform="translate(70, 180)"><circle cx="0" cy="0" r="15" fill="#2563eb"/><text x="0" y="4" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">NH₄⁺</text></g>
    <circle cx="230" cy="175" r="16" fill="url(#ohIon)"/><text x="230" y="180" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">OH⁻</text>

    <!-- Equation and Properties -->
    <rect x="25" y="225" width="285" height="85" rx="8" fill="#020617" stroke="#0f172a"/>
    <text x="167" y="248" text-anchor="middle" fill="#38bdf8" font-size="12" font-family="monospace" font-weight="bold">NH₃ + H₂O ⇌ NH₄⁺ + OH⁻</text>
    <text x="167" y="272" text-anchor="middle" fill="#38bdf8" font-size="11">Low [OH⁻] ≈ 0.004 mol/dm³ (pH ≈ 10–11)</text>
    <text x="167" y="292" text-anchor="middle" fill="#94a3b8" font-size="10">Low electrical conductivity • Mildly alkaline</text>
  </g>
</svg>'''

block_30_p4 = LessonBlock.objects.get(id=1066)
block_30_p4.title = "Particle-Level Dissociation Comparison: Strong Alkali vs. Weak Alkali"
block_30_p4.save()

asset_233, _ = LessonAsset.objects.get_or_create(id=233, defaults={'lesson': lesson_30, 'asset_type': 'diagram'})
asset_233.lesson = lesson_30
asset_233.asset_type = 'diagram'
asset_233.source_type = 'ai_generated'
asset_233.storage_type = 'file'
asset_233.status = 'attached'
asset_233.title = "Particle-Level Dissociation Comparison: Strong Alkali vs. Weak Alkali"
asset_233.description = "Comparison of complete lattice dissociation in strong alkali (NaOH) with reversible equilibrium ionization in weak alkali (NH3)."
asset_233.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Degree of dissociation in strong and weak alkalis'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_30_p4)
asset_233.file.save(f'strong_vs_weak_alkali_{lesson_30.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_233.blocks.set([block_30_p4])
print("Lesson 30 Page 4: Asset 233 saved and attached to Block 1066.")

# Page 5 (Block 1068): Ammonia in Water vs Methylbenzene (Generated SVG)
svg_30_p5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SOLVENT EFFECT ON AMMONIA: WATER VS. METHYLBENZENE</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Ionization Requires a Polar Solvent; Non-Polar Solvents Preserve Neutral Molecules</text>

  <!-- Left: Ammonia in Water -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="310" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">AMMONIA IN WATER (Polar)</text>
    
    <rect x="25" y="45" width="285" height="150" rx="8" fill="#0284c7" fill-opacity="0.2" stroke="#0369a1"/>
    <!-- Particles -->
    <circle cx="80" cy="90" r="16" fill="#2563eb"/><text x="80" y="95" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">NH₄⁺</text>
    <circle cx="160" cy="130" r="16" fill="#059669"/><text x="160" y="135" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">OH⁻</text>
    <circle cx="240" cy="90" r="14" fill="#475569"/><text x="240" y="94" text-anchor="middle" fill="#e2e8f0" font-size="9" font-weight="bold">NH₃</text>

    <!-- Results Box -->
    <rect x="25" y="205" width="285" height="90" rx="8" fill="#020617"/>
    <text x="167" y="230" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">NH₃(aq) + H₂O(l) ⇌ NH₄⁺(aq) + OH⁻(aq)</text>
    <text x="167" y="255" text-anchor="middle" fill="#4ade80" font-size="11">✓ Turns Red Litmus Paper BLUE</text>
    <text x="167" y="278" text-anchor="middle" fill="#7dd3fc" font-size="10">Conducts electricity (Bulb glows)</text>
  </g>

  <!-- Right: Ammonia in Methylbenzene -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="310" rx="14" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#cbd5e1" font-size="13" font-weight="bold">AMMONIA IN METHYLBENZENE (Non-Polar)</text>
    
    <rect x="25" y="45" width="285" height="150" rx="8" fill="#334155" fill-opacity="0.2" stroke="#475569"/>
    <!-- Particles -->
    <circle cx="80" cy="100" r="15" fill="#475569"/><text x="80" y="104" text-anchor="middle" fill="#e2e8f0" font-size="9" font-weight="bold">NH₃</text>
    <circle cx="165" cy="120" r="15" fill="#475569"/><text x="165" y="124" text-anchor="middle" fill="#e2e8f0" font-size="9" font-weight="bold">NH₃</text>
    <circle cx="245" cy="95" r="15" fill="#475569"/><text x="245" y="99" text-anchor="middle" fill="#e2e8f0" font-size="9" font-weight="bold">NH₃</text>

    <!-- Results Box -->
    <rect x="25" y="205" width="285" height="90" rx="8" fill="#020617"/>
    <text x="167" y="230" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">No chemical reaction with solvent (No OH⁻)</text>
    <text x="167" y="255" text-anchor="middle" fill="#f87171" font-size="11">✗ Dry Red Litmus Remains RED</text>
    <text x="167" y="278" text-anchor="middle" fill="#94a3b8" font-size="10">Non-conductive (Bulb remains OFF)</text>
  </g>
</svg>'''

block_30_p5 = LessonBlock.objects.get(id=1068)
block_30_p5.title = "Effect of Solvent on Ammonia: Water vs. Methylbenzene"
block_30_p5.save()

asset_234, _ = LessonAsset.objects.get_or_create(id=234, defaults={'lesson': lesson_30, 'asset_type': 'diagram'})
asset_234.lesson = lesson_30
asset_234.asset_type = 'diagram'
asset_234.source_type = 'ai_generated'
asset_234.storage_type = 'file'
asset_234.status = 'attached'
asset_234.title = "Effect of Solvent on Ammonia: Water vs. Methylbenzene"
asset_234.description = "Diagram comparing ammonia dissolving in water with basic ionization versus dissolving in non-polar methylbenzene without ionization."
asset_234.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Solvent influence on alkali dissociation'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_30_p5)
asset_234.file.save(f'solvent_effect_ammonia_{lesson_30.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_234.blocks.set([block_30_p5])
print("Lesson 30 Page 5: Asset 234 saved and attached to Block 1068.")

# Page 6 (Block 1070): Neutralization Mechanism (Generated SVG)
svg_30_p6 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrN" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <text x="400" y="38" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SUB-MICROSCOPIC MECHANISM OF NEUTRALIZATION</text>
  <text x="400" y="62" text-anchor="middle" fill="#94a3b8" font-size="12">Hydrated Hydrogen Ions and Hydroxide Ions Collide to Form Stable Covalent Water</text>

  <!-- Left: Acid Cation + Base Anion -->
  <g transform="translate(60, 95)">
    <rect x="0" y="0" width="280" height="200" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="140" y="30" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">REACTING SPECIES</text>

    <!-- H+ Ion -->
    <circle cx="70" cy="110" r="22" fill="#dc2626"/>
    <text x="70" y="115" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">H⁺</text>
    <text x="70" y="150" text-anchor="middle" fill="#fca5a5" font-size="10">Proton (Acid)</text>

    <text x="140" y="115" text-anchor="middle" fill="#94a3b8" font-size="24">+</text>

    <!-- OH- Ion -->
    <circle cx="210" cy="110" r="24" fill="#059669"/>
    <text x="210" y="115" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">OH⁻</text>
    <text x="210" y="150" text-anchor="middle" fill="#86efac" font-size="10">Hydroxide (Base)</text>
  </g>

  <!-- Center Collision Arrow -->
  <path d="M 360 195 L 420 195" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrN)"/>
  <text x="390" y="180" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Collision</text>

  <!-- Right: Water Molecule Formed -->
  <g transform="translate(440, 95)">
    <rect x="0" y="0" width="300" height="200" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="150" y="30" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">NEUTRAL PRODUCT</text>

    <!-- H2O Molecule -->
    <circle cx="150" cy="100" r="26" fill="#2563eb"/>
    <text x="150" y="96" text-anchor="middle" fill="#ffffff" font-size="12">O</text>
    <circle cx="130" cy="120" r="13" fill="#dc2626"/>
    <text x="130" y="124" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="bold">H</text>
    <circle cx="170" cy="120" r="13" fill="#dc2626"/>
    <text x="170" y="124" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="bold">H</text>
    
    <text x="150" y="165" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">H₂O(l) (Neutral Covalent Water)</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="60" y="315" width="680" height="75" rx="10" fill="#020617" stroke="#1e293b"/>
  <text x="400" y="342" text-anchor="middle" fill="#38bdf8" font-size="13" font-family="monospace" font-weight="bold">H⁺(aq) + OH⁻(aq) → H₂O(l)    (ΔH = -57.4 kJ/mol)</text>
  <text x="400" y="368" text-anchor="middle" fill="#cbd5e1" font-size="11">Spectator ions (e.g. Na⁺ and Cl⁻) remain freely solvated and do not undergo bond formation</text>
</svg>'''

block_30_p6 = LessonBlock.objects.get(id=1070)
block_30_p6.title = "Sub-Microscopic Mechanism of Acid-Base Neutralization"
block_30_p6.save()

asset_235, _ = LessonAsset.objects.get_or_create(id=235, defaults={'lesson': lesson_30, 'asset_type': 'diagram'})
asset_235.lesson = lesson_30
asset_235.asset_type = 'diagram'
asset_235.source_type = 'ai_generated'
asset_235.storage_type = 'file'
asset_235.status = 'attached'
asset_235.title = "Sub-Microscopic Mechanism of Acid-Base Neutralization"
asset_235.description = "Particle model showing the combination of hydrogen and hydroxide ions to form stable covalent water molecules."
asset_235.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Neutralization reaction mechanism'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_30_p6)
asset_235.file.save(f'neutralization_mechanism_{lesson_30.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_235.blocks.set([block_30_p6])
print("Lesson 30 Page 6: Asset 235 saved and attached to Block 1070.")


# =========================================================================
# 3. LESSON 27: Effect of Solvent on Acid-Base Character
# =========================================================================
lesson_27 = Lesson.objects.get(id=27)
print(f"\nProcessing Lesson 27: {lesson_27.title}")

# Page 2 (Block 1088): Dry HCl Gas Litmus Test (Generated SVG)
svg_27_p2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="38" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DRY HYDROGEN CHLORIDE GAS: DRY VS. DAMP LITMUS TEST</text>
  <text x="400" y="62" text-anchor="middle" fill="#94a3b8" font-size="12">Acids Require Water for Ionization to Exhibit Acidic Indicators</text>

  <!-- Left: Dry HCl on Dry Blue Litmus -->
  <g transform="translate(60, 85)">
    <rect x="0" y="0" width="310" height="300" rx="14" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="155" y="28" text-anchor="middle" fill="#cbd5e1" font-size="13" font-weight="bold">TEST 1: DRY BLUE LITMUS PAPER</text>

    <!-- Gas delivery tube -->
    <path d="M 60 70 L 120 70 L 120 160" fill="none" stroke="#94a3b8" stroke-width="6" stroke-linecap="round"/>
    <text x="120" y="60" text-anchor="middle" fill="#7dd3fc" font-size="10" font-weight="bold">Dry HCl(g)</text>

    <!-- Dry Blue Litmus strip -->
    <rect x="100" y="170" width="110" height="30" rx="3" fill="#2563eb"/>
    <text x="155" y="190" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">Dry Blue Litmus</text>

    <!-- Result Banner -->
    <rect x="20" y="225" width="270" height="60" rx="8" fill="#020617"/>
    <text x="155" y="250" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">NO COLOR CHANGE</text>
    <text x="155" y="270" text-anchor="middle" fill="#94a3b8" font-size="10">No water present → No H⁺ ions liberated</text>
  </g>

  <!-- Right: Dry HCl on Damp Blue Litmus -->
  <g transform="translate(430, 85)">
    <rect x="0" y="0" width="310" height="300" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="155" y="28" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">TEST 2: DAMP BLUE LITMUS PAPER</text>

    <!-- Gas delivery tube -->
    <path d="M 60 70 L 120 70 L 120 160" fill="none" stroke="#94a3b8" stroke-width="6" stroke-linecap="round"/>
    <text x="120" y="60" text-anchor="middle" fill="#7dd3fc" font-size="10" font-weight="bold">Dry HCl(g)</text>

    <!-- Damp Litmus strip (turns RED) -->
    <rect x="100" y="170" width="40" height="30" rx="3" fill="#2563eb"/>
    <rect x="140" y="170" width="70" height="30" rx="3" fill="#dc2626"/>
    <text x="155" y="190" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">Turns RED</text>

    <!-- Result Banner -->
    <rect x="20" y="225" width="270" height="60" rx="8" fill="#020617"/>
    <text x="155" y="250" text-anchor="middle" fill="#4ade80" font-size="12" font-weight="bold">INSTANT COLOR CHANGE TO RED</text>
    <text x="155" y="270" text-anchor="middle" fill="#94a3b8" font-size="10">Water dissolves HCl → H⁺(aq) turns litmus red</text>
  </g>
</svg>'''

block_27_p2 = LessonBlock.objects.get(id=1088)
block_27_p2.title = "Dry Hydrogen Chloride Gas: Dry vs. Damp Litmus Paper Test"
block_27_p2.save()

asset_236, _ = LessonAsset.objects.get_or_create(id=236, defaults={'lesson': lesson_27, 'asset_type': 'diagram'})
asset_236.lesson = lesson_27
asset_236.asset_type = 'diagram'
asset_236.source_type = 'ai_generated'
asset_236.storage_type = 'file'
asset_236.status = 'attached'
asset_236.title = "Dry Hydrogen Chloride Gas: Dry vs. Damp Litmus Paper Test"
asset_236.description = "Diagram illustrating that dry hydrogen chloride gas does not affect dry litmus paper but immediately turns damp litmus paper red due to aqueous ionization."
asset_236.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Necessity of water for acid ionization'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_27_p2)
asset_236.file.save(f'hcl_litmus_test_{lesson_27.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_236.blocks.set([block_27_p2])
print("Lesson 27 Page 2: Asset 236 saved and attached to Block 1088.")

# Page 3 (Block 1090): Polar Water vs Non-Polar Methylbenzene (Generated SVG)
svg_27_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 430" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">SUB-MICROSCOPIC BEHAVIOR: HCl IN WATER VS. METHYLBENZENE</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Polar Solvent Induces Bond Cleavage; Non-Polar Solvent Preserves Covalent Molecules</text>

  <!-- Left: HCl in Water -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="320" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">HCl IN WATER (Polar Solvent)</text>
    
    <rect x="25" y="45" width="285" height="160" rx="8" fill="#0284c7" fill-opacity="0.2" stroke="#0369a1"/>
    <!-- Hydrated ions -->
    <circle cx="80" cy="100" r="16" fill="#dc2626"/><text x="80" y="105" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">H⁺(aq)</text>
    <circle cx="160" cy="140" r="18" fill="#2563eb"/><text x="160" y="145" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Cl⁻(aq)</text>
    <circle cx="235" cy="100" r="16" fill="#dc2626"/><text x="235" y="105" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">H⁺(aq)</text>

    <!-- Properties -->
    <rect x="25" y="215" width="285" height="90" rx="8" fill="#020617"/>
    <text x="167" y="238" text-anchor="middle" fill="#38bdf8" font-size="12" font-family="monospace" font-weight="bold">HCl(aq) → H⁺(aq) + Cl⁻(aq)</text>
    <text x="167" y="260" text-anchor="middle" fill="#4ade80" font-size="11">✓ Turns blue litmus red</text>
    <text x="167" y="280" text-anchor="middle" fill="#cbd5e1" font-size="10">Conducts electricity • Reacts with Mg &amp; CaCO₃</text>
  </g>

  <!-- Right: HCl in Methylbenzene -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="320" rx="14" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
    <text x="167" y="28" text-anchor="middle" fill="#fde047" font-size="13" font-weight="bold">HCl IN METHYLBENZENE (Non-Polar)</text>
    
    <rect x="25" y="45" width="285" height="160" rx="8" fill="#eab308" fill-opacity="0.1" stroke="#ca8a04"/>
    <!-- Intact Covalent Molecules -->
    <g transform="translate(80, 100)">
      <circle cx="-10" cy="0" r="10" fill="#dc2626"/><text x="-10" y="3" text-anchor="middle" fill="#fff" font-size="8">H</text>
      <circle cx="10" cy="0" r="14" fill="#2563eb"/><text x="10" y="4" text-anchor="middle" fill="#fff" font-size="9">Cl</text>
    </g>
    <g transform="translate(200, 100)">
      <circle cx="-10" cy="0" r="10" fill="#dc2626"/><text x="-10" y="3" text-anchor="middle" fill="#fff" font-size="8">H</text>
      <circle cx="10" cy="0" r="14" fill="#2563eb"/><text x="10" y="4" text-anchor="middle" fill="#fff" font-size="9">Cl</text>
    </g>
    <g transform="translate(140, 150)">
      <circle cx="-10" cy="0" r="10" fill="#dc2626"/><text x="-10" y="3" text-anchor="middle" fill="#fff" font-size="8">H</text>
      <circle cx="10" cy="0" r="14" fill="#2563eb"/><text x="10" y="4" text-anchor="middle" fill="#fff" font-size="9">Cl</text>
    </g>

    <!-- Properties -->
    <rect x="25" y="215" width="285" height="90" rx="8" fill="#020617"/>
    <text x="167" y="238" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">Remains covalent HCl molecules</text>
    <text x="167" y="260" text-anchor="middle" fill="#f87171" font-size="11">✗ Blue litmus stays BLUE</text>
    <text x="167" y="280" text-anchor="middle" fill="#94a3b8" font-size="10">Non-conductive • No reaction with metals/carbonates</text>
  </g>
</svg>'''

block_27_p3 = LessonBlock.objects.get(id=1090)
block_27_p3.title = "Sub-Microscopic Comparison: HCl in Polar Water vs. Non-Polar Methylbenzene"
block_27_p3.save()

asset_237, _ = LessonAsset.objects.get_or_create(id=237, defaults={'lesson': lesson_27, 'asset_type': 'diagram'})
asset_237.lesson = lesson_27
asset_237.asset_type = 'diagram'
asset_237.source_type = 'ai_generated'
asset_237.storage_type = 'file'
asset_237.status = 'attached'
asset_237.title = "Sub-Microscopic Comparison: HCl in Polar Water vs. Non-Polar Methylbenzene"
asset_237.description = "Particle model demonstrating the cleavage of covalent HCl bonds in polar water into hydrated ions versus preservation of neutral covalent molecules in methylbenzene."
asset_237.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Solute-solvent interactions in acid behavior'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_27_p3)
asset_237.file.save(f'solvent_comparison_{lesson_27.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_237.blocks.set([block_27_p3])
print("Lesson 27 Page 3: Asset 237 saved and attached to Block 1090.")

# Page 4 (Block 1092): Ammonia in Water vs Methylbenzene (Generated SVG)
block_27_p4 = LessonBlock.objects.get(id=1092)
block_27_p4.title = "Behavior of Ammonia in Polar Water vs. Non-Polar Methylbenzene"
block_27_p4.save()

asset_238, _ = LessonAsset.objects.get_or_create(id=238, defaults={'lesson': lesson_27, 'asset_type': 'diagram'})
asset_238.lesson = lesson_27
asset_238.asset_type = 'diagram'
asset_238.source_type = 'ai_generated'
asset_238.storage_type = 'file'
asset_238.status = 'attached'
asset_238.title = "Behavior of Ammonia in Polar Water vs. Non-Polar Methylbenzene"
asset_238.description = "Diagram comparing the basic ionization of ammonia gas in aqueous solution against its unreactive molecular state in non-polar organic solvent."
asset_238.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Solvent influence on alkaline properties'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_30_p5)
asset_238.file.save(f'ammonia_solvent_effect_{lesson_27.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_238.blocks.set([block_27_p4])
print("Lesson 27 Page 4: Asset 238 saved and attached to Block 1092.")


# =========================================================================
# 4. LESSON 18: Amphoteric Oxides and Hydroxides
# =========================================================================
lesson_18 = Lesson.objects.get(id=18)
print(f"\nProcessing Lesson 18: {lesson_18.title}")

# Page 2 (Block 1101): Dual Character Concept (Generated SVG)
svg_18_p2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrAmph" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <text x="400" y="38" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">THE DUAL CHARACTER OF AMPHOTERIC SUBSTANCES</text>
  <text x="400" y="62" text-anchor="middle" fill="#94a3b8" font-size="12">Zinc, Aluminium, and Lead Oxides/Hydroxides React with Both Acids and Strong Bases</text>

  <!-- Left: Acting as a Base -->
  <g transform="translate(45, 95)">
    <rect x="0" y="0" width="220" height="230" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="110" y="30" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">REACTING WITH ACIDS</text>
    <text x="110" y="55" text-anchor="middle" fill="#7dd3fc" font-size="11">Acts as a BASE</text>
    
    <rect x="15" y="80" width="190" height="125" rx="8" fill="#020617"/>
    <text x="105" y="105" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">+ Acid (e.g. HCl / HNO₃)</text>
    <text x="105" y="135" text-anchor="middle" fill="#4ade80" font-size="11">Dissolves to form:</text>
    <text x="105" y="160" text-anchor="middle" fill="#38bdf8" font-size="11" font-family="monospace">Normal Metal Salt</text>
    <text x="105" y="180" text-anchor="middle" fill="#38bdf8" font-size="11" font-family="monospace">+ Water (H₂O)</text>
  </g>

  <!-- Center: Amphoteric Core -->
  <g transform="translate(295, 115)">
    <rect x="0" y="0" width="210" height="190" rx="16" fill="#047857" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
    <text x="105" y="32" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">AMPHOTERIC SOLID</text>
    <text x="105" y="58" text-anchor="middle" fill="#cbd5e1" font-size="11">ZnO / Zn(OH)₂</text>
    <text x="105" y="78" text-anchor="middle" fill="#cbd5e1" font-size="11">Al₂O₃ / Al(OH)₃</text>
    <text x="105" y="98" text-anchor="middle" fill="#cbd5e1" font-size="11">PbO / Pb(OH)₂</text>
    
    <rect x="20" y="120" width="170" height="50" rx="8" fill="#020617"/>
    <text x="105" y="142" text-anchor="middle" fill="#fde047" font-size="11" font-weight="bold">"Chemical Chameleon"</text>
    <text x="105" y="158" text-anchor="middle" fill="#94a3b8" font-size="9">Dissolves in both extremes</text>
  </g>

  <!-- Right: Acting as an Acid -->
  <g transform="translate(535, 95)">
    <rect x="0" y="0" width="220" height="230" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="30" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">REACTING WITH BASES</text>
    <text x="110" y="55" text-anchor="middle" fill="#fde68a" font-size="11">Acts as an ACID</text>
    
    <rect x="15" y="80" width="190" height="125" rx="8" fill="#020617"/>
    <text x="105" y="105" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">+ Strong Base (e.g. NaOH)</text>
    <text x="105" y="135" text-anchor="middle" fill="#4ade80" font-size="11">Dissolves to form:</text>
    <text x="105" y="160" text-anchor="middle" fill="#fbbf24" font-size="11" font-family="monospace">Complex Salt</text>
    <text x="105" y="180" text-anchor="middle" fill="#fbbf24" font-size="10" font-family="monospace">(e.g. Sodium Zincate)</text>
  </g>

  <!-- Connecting arrows -->
  <path d="M 295 210 L 270 210" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrAmph)"/>
  <path d="M 505 210 L 530 210" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrAmph)"/>

  <!-- Bottom rule -->
  <text x="400" y="370" text-anchor="middle" fill="#94a3b8" font-size="11">Key Rule: Insoluble basic oxides (e.g. CuO, Fe₂O₃) do NOT dissolve in sodium hydroxide</text>
</svg>'''

block_18_p2 = LessonBlock.objects.get(id=1101)
block_18_p2.title = "Dual Chemical Reactivity of Amphoteric Oxides and Hydroxides"
block_18_p2.save()

asset_239, _ = LessonAsset.objects.get_or_create(id=239, defaults={'lesson': lesson_18, 'asset_type': 'diagram'})
asset_239.lesson = lesson_18
asset_239.asset_type = 'diagram'
asset_239.source_type = 'ai_generated'
asset_239.storage_type = 'file'
asset_239.status = 'attached'
asset_239.title = "Dual Chemical Reactivity of Amphoteric Oxides and Hydroxides"
asset_239.description = "Conceptual schematic showing amphoteric metal oxides/hydroxides reacting as a base in acidic media and as an acid in strongly alkaline media."
asset_239.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Amphoteric dual reactivity principle'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_18_p2)
asset_239.file.save(f'amphoteric_concept_{lesson_18.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_239.blocks.set([block_18_p2])
print("Lesson 18 Page 2: Asset 239 saved and attached to Block 1101.")

# Page 4 (Block 1104): Zinc Hydroxide Reaction Pathways (Generated SVG)
svg_18_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">DUAL REACTION PATHWAYS OF ZINC HYDROXIDE (Zn(OH)₂)</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Solid White Precipitate Dissolves in Both Dilute Acid and Excess Strong Alkali</text>

  <!-- Center Solid -->
  <g transform="translate(300, 80)">
    <rect x="0" y="0" width="200" height="90" rx="12" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
    <text x="100" y="32" text-anchor="middle" fill="#f8fafc" font-size="13" font-weight="bold">Zn(OH)₂(s) Solid</text>
    <text x="100" y="52" text-anchor="middle" fill="#94a3b8" font-size="11">White Insoluble Gelatinous</text>
    <text x="100" y="70" text-anchor="middle" fill="#cbd5e1" font-size="11">Precipitate</text>
  </g>

  <!-- Left Pathway: Reaction with Acid -->
  <g transform="translate(45, 195)">
    <rect x="0" y="0" width="335" height="215" rx="14" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">PATHWAY 1: REACTION WITH ACID (H⁺)</text>
    <text x="167" y="46" text-anchor="middle" fill="#7dd3fc" font-size="10">Proton transfer from acid to hydroxide ions</text>

    <!-- Ionic Equation -->
    <rect x="15" y="60" width="305" height="55" rx="8" fill="#020617"/>
    <text x="167" y="85" text-anchor="middle" fill="#38bdf8" font-size="12" font-family="monospace" font-weight="bold">Zn(OH)₂(s) + 2H⁺(aq) → Zn²⁺(aq) + 2H₂O(l)</text>
    <text x="167" y="105" text-anchor="middle" fill="#94a3b8" font-size="10">Zinc salt formed: ZnCl₂ / Zn(NO₃)₂</text>

    <!-- Observation -->
    <rect x="15" y="125" width="305" height="70" rx="8" fill="#020617"/>
    <text x="167" y="148" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="bold">Observation:</text>
    <text x="167" y="170" text-anchor="middle" fill="#f8fafc" font-size="11">White precipitate dissolves completely</text>
    <text x="167" y="185" text-anchor="middle" fill="#94a3b8" font-size="10">to form a clear, colourless solution</text>
  </g>

  <!-- Right Pathway: Reaction with Alkali -->
  <g transform="translate(420, 195)">
    <rect x="0" y="0" width="335" height="215" rx="14" fill="#1e293b" stroke="#059669" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">PATHWAY 2: REACTION WITH EXCESS NaOH (OH⁻)</text>
    <text x="167" y="46" text-anchor="middle" fill="#6ee7b7" font-size="10">Complex ion formation (Tetrahydroxozincate)</text>

    <!-- Ionic Equation -->
    <rect x="15" y="60" width="305" height="55" rx="8" fill="#020617"/>
    <text x="167" y="85" text-anchor="middle" fill="#34d399" font-size="11" font-family="monospace" font-weight="bold">Zn(OH)₂(s) + 2OH⁻(aq) → [Zn(OH)₄]²⁻(aq)</text>
    <text x="167" y="105" text-anchor="middle" fill="#94a3b8" font-size="10">Soluble complex ion: Tetrahydroxozincate(II)</text>

    <!-- Observation -->
    <rect x="15" y="125" width="305" height="70" rx="8" fill="#020617"/>
    <text x="167" y="148" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="bold">Observation:</text>
    <text x="167" y="170" text-anchor="middle" fill="#f8fafc" font-size="11">White precipitate dissolves in excess NaOH</text>
    <text x="167" y="185" text-anchor="middle" fill="#94a3b8" font-size="10">to form a clear, colourless solution</text>
  </g>
</svg>'''

block_18_p4 = LessonBlock.objects.get(id=1104)
block_18_p4.title = "Dual Reaction Pathways of Zinc Hydroxide with Acid and Strong Base"
block_18_p4.save()

asset_240, _ = LessonAsset.objects.get_or_create(id=240, defaults={'lesson': lesson_18, 'asset_type': 'diagram'})
asset_240.lesson = lesson_18
asset_240.asset_type = 'diagram'
asset_240.source_type = 'ai_generated'
asset_240.storage_type = 'file'
asset_240.status = 'attached'
asset_240.title = "Dual Reaction Pathways of Zinc Hydroxide with Acid and Strong Base"
asset_240.description = "Flowchart displaying the dual dissolution pathways of solid zinc hydroxide reacting with acid to form hydrated Zn2+ and with excess base to form tetrahydroxozincate complex."
asset_240.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Zinc hydroxide amphoteric reaction mechanism'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_18_p4)
asset_240.file.save(f'zinc_hydroxide_pathways_{lesson_18.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_240.blocks.set([block_18_p4])
print("Lesson 18 Page 4: Asset 240 saved and attached to Block 1104.")


# =========================================================================
# 5. LESSON 11: Salts
# =========================================================================
lesson_11 = Lesson.objects.get(id=11)
print(f"\nProcessing Lesson 11: {lesson_11.title}")

# Page 2 (Block 1113): Copper Sulfate Crystals (Wikimedia)
block_11_p2 = LessonBlock.objects.get(id=1113)
block_11_p2.title = "Crystalline Copper(II) Sulfate Pentahydrate Produced by Neutralization"
block_11_p2.save()

asset_242, _ = LessonAsset.objects.get_or_create(id=242, defaults={'lesson': lesson_11, 'asset_type': 'image'})
asset_242.lesson = lesson_11
asset_242.asset_type = 'image'
asset_242.source_type = 'external'
asset_242.storage_type = 'url'
asset_242.status = 'attached'
asset_242.title = "Crystalline Copper(II) Sulfate Pentahydrate Produced by Neutralization"
asset_242.description = "High-definition photograph of vibrant blue crystalline copper(II) sulfate pentahydrate salt."
asset_242.url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Copper_sulfate_pentahydrate_crystals.jpg"
asset_242.metadata = {
    'author': 'W. Oelen',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'W. Oelen / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Copper_sulfate_pentahydrate_crystals.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Ionic crystals formed by acid-base reaction'
}
asset_242.save()
asset_242.blocks.set([block_11_p2])
print("Lesson 11 Page 2: Asset 242 attached to Block 1113.")

# Page 5 (Block 1118): 4 Pathways to Soluble Salts (Generated SVG)
svg_11_p5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="arrSalt" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">FOUR LABORATORY PATHWAYS TO SOLUBLE SALTS</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Direct Reaction of an Acid with Four Different Metal-Containing Reagents</text>

  <!-- Central Acid Hub -->
  <g transform="translate(320, 175)">
    <rect x="0" y="0" width="160" height="90" rx="14" fill="#dc2626" fill-opacity="0.3" stroke="#ef4444" stroke-width="2"/>
    <text x="80" y="38" text-anchor="middle" fill="#fca5a5" font-size="14" font-weight="bold">DILUTE ACID</text>
    <text x="80" y="62" text-anchor="middle" fill="#f8fafc" font-size="12" font-family="monospace">Source of Anion</text>
  </g>

  <!-- Top-Left: Pathway 1 (Acid + Metal) -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="245" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="122" y="24" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">1. ACID + ACTIVE METAL</text>
    <text x="122" y="48" text-anchor="middle" fill="#ffffff" font-size="10" font-family="monospace">Mg + 2HCl → MgCl₂ + H₂</text>
    <rect x="15" y="62" width="215" height="46" rx="6" fill="#020617"/>
    <text x="122" y="80" text-anchor="middle" fill="#4ade80" font-size="10">Effervescence of H₂(g)</text>
    <text x="122" y="96" text-anchor="middle" fill="#94a3b8" font-size="9">Pop-sound with lighted splint</text>
  </g>

  <!-- Top-Right: Pathway 2 (Acid + Insoluble Base) -->
  <g transform="translate(510, 80)">
    <rect x="0" y="0" width="245" height="120" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="122" y="24" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">2. ACID + INSOLUBLE BASE</text>
    <text x="122" y="48" text-anchor="middle" fill="#ffffff" font-size="10" font-family="monospace">CuO + H₂SO₄ → CuSO₄ + H₂O</text>
    <rect x="15" y="62" width="215" height="46" rx="6" fill="#020617"/>
    <text x="122" y="80" text-anchor="middle" fill="#4ade80" font-size="10">Neutralization (Black CuO dissolves)</text>
    <text x="122" y="96" text-anchor="middle" fill="#94a3b8" font-size="9">Produces blue CuSO₄ solution</text>
  </g>

  <!-- Bottom-Left: Pathway 3 (Acid + Carbonate) -->
  <g transform="translate(45, 250)">
    <rect x="0" y="0" width="245" height="120" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="122" y="24" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">3. ACID + CARBONATE</text>
    <text x="122" y="48" text-anchor="middle" fill="#ffffff" font-size="10" font-family="monospace">ZnCO₃ + 2HCl → ZnCl₂ + CO₂ + H₂O</text>
    <rect x="15" y="62" width="215" height="46" rx="6" fill="#020617"/>
    <text x="122" y="80" text-anchor="middle" fill="#4ade80" font-size="10">Effervescence of CO₂(g)</text>
    <text x="122" y="96" text-anchor="middle" fill="#94a3b8" font-size="9">Turns lime water milky</text>
  </g>

  <!-- Bottom-Right: Pathway 4 (Acid + Alkali / Titration) -->
  <g transform="translate(510, 250)">
    <rect x="0" y="0" width="245" height="120" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="122" y="24" text-anchor="middle" fill="#c084fc" font-size="11" font-weight="bold">4. ACID + ALKALI (TITRATION)</text>
    <text x="122" y="48" text-anchor="middle" fill="#ffffff" font-size="10" font-family="monospace">NaOH + HCl → NaCl + H₂O</text>
    <rect x="15" y="62" width="215" height="46" rx="6" fill="#020617"/>
    <text x="122" y="80" text-anchor="middle" fill="#4ade80" font-size="10">Volumetric Titration</text>
    <text x="122" y="96" text-anchor="middle" fill="#94a3b8" font-size="9">Indicator determines exact endpoint</text>
  </g>

  <!-- Connector Lines -->
  <path d="M 320 200 L 295 160" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrSalt)"/>
  <path d="M 480 200 L 505 160" stroke="#34d399" stroke-width="2" marker-end="url(#arrSalt)"/>
  <path d="M 320 240 L 295 280" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrSalt)"/>
  <path d="M 480 240 L 505 280" stroke="#a855f7" stroke-width="2" marker-end="url(#arrSalt)"/>

  <text x="400" y="415" text-anchor="middle" fill="#cbd5e1" font-size="11">Final Step: Evaporate to saturation point, allow crystals to cool and filter dry</text>
</svg>'''

block_11_p5 = LessonBlock.objects.get(id=1118)
block_11_p5.title = "Four Laboratory Pathways for Preparing Soluble Salts from an Acid"
block_11_p5.save()

asset_243, _ = LessonAsset.objects.get_or_create(id=243, defaults={'lesson': lesson_11, 'asset_type': 'diagram'})
asset_243.lesson = lesson_11
asset_243.asset_type = 'diagram'
asset_243.source_type = 'ai_generated'
asset_243.storage_type = 'file'
asset_243.status = 'attached'
asset_243.title = "Four Laboratory Pathways for Preparing Soluble Salts from an Acid"
asset_243.description = "Summary infographic outlining the 4 standard methods of preparing soluble salts by reacting dilute acid with metals, metal oxides, carbonates, or alkalis."
asset_243.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Methods of salt preparation'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_11_p5)
asset_243.file.save(f'salt_prep_pathways_{lesson_11.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_243.blocks.set([block_11_p5])
print("Lesson 11 Page 5: Asset 243 saved and attached to Block 1118.")


# =========================================================================
# 6. LESSON 19: Fractional Crystallisation
# =========================================================================
lesson_19 = Lesson.objects.get(id=19)
print(f"\nProcessing Lesson 19: {lesson_19.title}")

# Page 3 (Block 1159): Fractional Crystallisation Principle (Generated SVG)
svg_19_p3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%" style="background-color: #0b1329; font-family: system-ui, -apple-system, sans-serif;">
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">PRINCIPLE OF FRACTIONAL CRYSTALLISATION</text>
  <text x="400" y="60" text-anchor="middle" fill="#94a3b8" font-size="12">Separating Two Soluble Salts Exploiting Large Differences in Temperature-Dependent Solubility</text>

  <!-- Left: Solubility Curves -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">SOLUBILITY CURVES (g / 100g H₂O)</text>

    <!-- Graph axes -->
    <line x1="50" y1="210" x2="300" y2="210" stroke="#94a3b8" stroke-width="2"/>
    <line x1="50" y1="60" x2="50" y2="210" stroke="#94a3b8" stroke-width="2"/>
    <text x="175" y="235" text-anchor="middle" fill="#cbd5e1" font-size="10">Temperature (°C): 10°C → 80°C</text>
    <text x="35" y="70" text-anchor="middle" fill="#cbd5e1" font-size="9">g/100g</text>

    <!-- Curve 1: KNO3 (Steep) -->
    <path d="M 50 190 Q 180 160 290 70" fill="none" stroke="#ef4444" stroke-width="3"/>
    <text x="250" y="65" fill="#fca5a5" font-size="10" font-weight="bold">KNO₃ (Steep curve)</text>

    <!-- Curve 2: KClO3 (Moderate) -->
    <path d="M 50 200 Q 180 185 290 140" fill="none" stroke="#34d399" stroke-width="3"/>
    <text x="250" y="135" fill="#86efac" font-size="10" font-weight="bold">KClO₃ (Flatter)</text>

    <rect x="20" y="245" width="295" height="65" rx="8" fill="#020617"/>
    <text x="167" y="268" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Independence Principle:</text>
    <text x="167" y="288" text-anchor="middle" fill="#cbd5e1" font-size="9">Each salt dissolves independently up to its own saturation limit</text>
  </g>

  <!-- Right: Separation Procedure Flow -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="325" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="167" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">SEPARATION PROCEDURE</text>

    <!-- Step 1 -->
    <rect x="20" y="45" width="295" height="55" rx="6" fill="#020617"/>
    <text x="35" y="66" fill="#38bdf8" font-size="10" font-weight="bold">STEP 1: HOT DISSOLUTION</text>
    <text x="35" y="86" fill="#cbd5e1" font-size="9">Dissolve mixture in minimum boiling water at 80°C</text>

    <!-- Step 2 -->
    <rect x="20" y="110" width="295" height="55" rx="6" fill="#020617"/>
    <text x="35" y="131" fill="#38bdf8" font-size="10" font-weight="bold">STEP 2: CONTROLLED COOLING</text>
    <text x="35" y="151" fill="#cbd5e1" font-size="9">Cool solution to 20°C. Less soluble salt crystallizes first</text>

    <!-- Step 3 -->
    <rect x="20" y="175" width="295" height="55" rx="6" fill="#020617"/>
    <text x="35" y="196" fill="#38bdf8" font-size="10" font-weight="bold">STEP 3: FILTRATION</text>
    <text x="35" y="216" fill="#cbd5e1" font-size="9">Filter off pure crystals; more soluble salt stays in mother liquor</text>

    <!-- Bottom summary -->
    <rect x="20" y="245" width="295" height="65" rx="8" fill="#047857" fill-opacity="0.25" stroke="#10b981"/>
    <text x="167" y="268" text-anchor="middle" fill="#6ee7b7" font-size="10" font-weight="bold">High Purity Separation</text>
    <text x="167" y="288" text-anchor="middle" fill="#ffffff" font-size="9">Common industrial method used at Lake Magadi trona extraction</text>
  </g>
</svg>'''

block_19_p3 = LessonBlock.objects.get(id=1159)
block_19_p3.title = "Separation by Fractional Crystallisation Based on Differential Solubility Curves"
block_19_p3.save()

asset_246, _ = LessonAsset.objects.get_or_create(id=246, defaults={'lesson': lesson_19, 'asset_type': 'diagram'})
asset_246.lesson = lesson_19
asset_246.asset_type = 'diagram'
asset_246.source_type = 'ai_generated'
asset_246.storage_type = 'file'
asset_246.status = 'attached'
asset_246.title = "Separation by Fractional Crystallisation Based on Differential Solubility Curves"
asset_246.description = "Diagram connecting solubility temperature curves of mixed salts to the step-by-step hot dissolution and fractional cooling separation process."
asset_246.metadata = {
    'render_format': 'svg',
    'provenance': 'VisualReasoner',
    'enrichment_agent': True,
    'concept': 'Fractional crystallisation separation principle'
}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_19_p3)
asset_246.file.save(f'fractional_crystallisation_{lesson_19.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
asset_246.blocks.set([block_19_p3])
print("Lesson 19 Page 3: Asset 246 saved and attached to Block 1159.")

print("\n=== Halfway Batch 1 Visual Enrichment Completed Successfully! ===")
