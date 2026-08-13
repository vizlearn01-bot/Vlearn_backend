import os
import sys
import django
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db.models import Max
from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

print("=== Starting Visual Enrichment for Form 4 Topic 3: Second Half (Lessons 70–76) ===")

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
# 1. LESSON 70: Effect of Change in Concentration on Equilibrium
# =========================================================================
l70 = Lesson.objects.get(id=70)
print(f"\nProcessing Lesson 70: {l70.title}")

# P2: Iron Thiocyanate Solution (Wikimedia Image)
b70_p2 = get_or_create_diagram_block(l70, 2, "Aqueous Iron(III) Thiocyanate Complex Solution Demonstrating Concentration Equilibrium Shifts")
a70_p2, _ = LessonAsset.objects.get_or_create(id=331, defaults={'lesson': l70, 'asset_type': 'image'})
a70_p2.lesson = l70
a70_p2.asset_type = 'image'
a70_p2.source_type = 'external'
a70_p2.storage_type = 'url'
a70_p2.status = 'attached'
a70_p2.title = "Aqueous Iron(III) Thiocyanate Complex Solution Demonstrating Concentration Equilibrium Shifts"
a70_p2.description = "Photograph of deep blood-red [Fe(SCN)]2+ complex ions formed reversibly in solution when iron(III) reacts with thiocyanate ions."
a70_p2.url = "https://upload.wikimedia.org/wikipedia/commons/f/f6/Aqueous_ferric_thiocyanate_%28Fe%28SCN%29n%29_hydrate_mix.jpg"
a70_p2.metadata = {
    'author': 'Keministi',
    'licensing': 'CC0',
    'attribution': 'Keministi / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Aqueous_ferric_thiocyanate_(Fe(SCN)n)_hydrate_mix.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Concentration effect on complex ion equilibrium'
}
a70_p2.save()
a70_p2.blocks.set([b70_p2])
print("Lesson 70 Page 2: Asset 331 attached.")

# P3: Reversible Color Shift in Iron-Thiocyanate (Wikimedia Image)
b70_p3 = get_or_create_diagram_block(l70, 3, "Reversible Color Shift in Iron(III) and Thiocyanate Ionic System")
a70_p3, _ = LessonAsset.objects.get_or_create(id=332, defaults={'lesson': l70, 'asset_type': 'image'})
a70_p3.lesson = l70
a70_p3.asset_type = 'image'
a70_p3.source_type = 'external'
a70_p3.storage_type = 'url'
a70_p3.status = 'attached'
a70_p3.title = "Reversible Color Shift in Iron(III) and Thiocyanate Ionic System"
a70_p3.description = "Photograph demonstrating how adding extra reactant ions shifts equilibrium forward to deepen the blood-red color intensity."
a70_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Eisen%28III%29-Ionen_und_Thiocyanat.JPG/800px-Eisen%28III%29-Ionen_und_Thiocyanat.JPG"
a70_p3.metadata = {
    'author': 'Siegert',
    'licensing': 'Public domain',
    'attribution': 'Siegert / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Eisen(III)-Ionen_und_Thiocyanat.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Le Chatelier concentration shift'
}
a70_p3.save()
a70_p3.blocks.set([b70_p3])
print("Lesson 70 Page 3: Asset 332 attached.")

# P4: Concentration Perturbation Dynamics (Generated SVG)
svg_70_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">CONCENTRATION PERTURBATION ON CHEMICAL EQUILIBRIUM</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Le Chatelier's Principle: Adding Reactants or Removing Products Shifts Equilibrium to the Right (Forward)</text>

  <g transform="translate(45, 75)">
    <!-- Case 1: Adding Reactant -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">CASE 1: ADDING REACTANT [Fe³⁺ / SCN⁻]</text>

      <rect x="25" y="60" width="295" height="70" rx="8" fill="#020617" stroke="#38bdf8"/>
      <text x="172" y="85" text-anchor="middle" fill="#f8fafc" font-size="12" font-family="monospace">Fe³⁺(aq) + SCN⁻(aq) ⇌ [Fe(SCN)]²⁺(aq)</text>
      <text x="172" y="110" text-anchor="middle" fill="#fbbf24" font-size="11">Yellow + Colorless ⇌ Blood-Red Complex</text>

      <!-- Seesaw Graphic -->
      <g transform="translate(172, 175)">
        <polygon points="0,0 -20,30 20,30" fill="#64748b"/>
        <!-- Tilted beam (heavy on left) -->
        <line x1="-120" y1="18" x2="120" y2="-18" stroke="#38bdf8" stroke-width="4"/>
        <rect x="-140" y="10" width="40" height="24" rx="4" fill="#ef4444"/>
        <text x="-120" y="26" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">+Fe³⁺</text>
      </g>

      <rect x="20" y="225" width="305" height="95" rx="8" fill="#020617"/>
      <text x="35" y="248" fill="#38bdf8" font-size="11" font-weight="bold">• System opposes change: Consumes added Fe³⁺</text>
      <text x="35" y="268" fill="#cbd5e1" font-size="10">• Equilibrium shifts to the RIGHT (Forward)</text>
      <text x="35" y="288" fill="#f87171" font-size="10" font-weight="bold">• Blood-red color becomes significantly darker</text>
      <text x="35" y="306" fill="#4ade80" font-size="10">Yield of product complex increases</text>
    </g>

    <!-- Case 2: Removing Reactant / Adding Product -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">CASE 2: REMOVING REACTANT (ADD NaF / H₂O)</text>

      <rect x="25" y="60" width="295" height="70" rx="8" fill="#020617" stroke="#f59e0b"/>
      <text x="172" y="85" text-anchor="middle" fill="#f8fafc" font-size="12" font-family="monospace">BiCl₃(aq) + H₂O(l) ⇌ BiOCl(s) + 2HCl(aq)</text>
      <text x="172" y="110" text-anchor="middle" fill="#fbbf24" font-size="11">Clear Solution ⇌ White Turbidity + Acid</text>

      <!-- Seesaw Graphic -->
      <g transform="translate(172, 175)">
        <polygon points="0,0 -20,30 20,30" fill="#64748b"/>
        <!-- Tilted beam (heavy on right) -->
        <line x1="-120" y1="-18" x2="120" y2="18" stroke="#fbbf24" stroke-width="4"/>
        <rect x="100" y="10" width="40" height="24" rx="4" fill="#f59e0b"/>
        <text x="120" y="26" text-anchor="middle" fill="#000" font-size="9" font-weight="bold">+HCl</text>
      </g>

      <rect x="20" y="225" width="305" height="95" rx="8" fill="#020617"/>
      <text x="35" y="248" fill="#fbbf24" font-size="11" font-weight="bold">• Adding excess product (conc. HCl)</text>
      <text x="35" y="268" fill="#cbd5e1" font-size="10">• Equilibrium shifts to the LEFT (Backward)</text>
      <text x="35" y="288" fill="#38bdf8" font-size="10" font-weight="bold">• White precipitate dissolves back to clear solution</text>
      <text x="35" y="306" fill="#4ade80" font-size="10">System replaces consumed reactants</text>
    </g>
  </g>
</svg>'''
b70_p4 = get_or_create_diagram_block(l70, 4, "Concentration Perturbation Mechanics and Reversible Solution Shifts")
a70_p4, _ = LessonAsset.objects.get_or_create(id=333, defaults={'lesson': l70, 'asset_type': 'diagram'})
a70_p4.lesson = l70
a70_p4.asset_type = 'diagram'
a70_p4.source_type = 'ai_generated'
a70_p4.storage_type = 'file'
a70_p4.status = 'attached'
a70_p4.title = "Concentration Perturbation Mechanics and Reversible Solution Shifts"
a70_p4.description = "Seesaw perturbation model demonstrating equilibrium shifts when adding or removing ionic reactants and products."
a70_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_70_p4)
a70_p4.file.save(f'concentration_equilibrium_{l70.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a70_p4.blocks.set([b70_p4])
print("Lesson 70 Page 4: Asset 333 saved and attached.")


# =========================================================================
# 2. LESSON 71: Effect of Pressure on Equilibrium
# =========================================================================
l71 = Lesson.objects.get(id=71)
print(f"\nProcessing Lesson 71: {l71.title}")

# P2: Gas Syringe Apparatus (Wikimedia Image)
b71_p2 = get_or_create_diagram_block(l71, 2, "Laboratory Gas Syringe Apparatus for Investigating Gaseous Volume and Pressure Equilibrium")
a71_p2, _ = LessonAsset.objects.get_or_create(id=334, defaults={'lesson': l71, 'asset_type': 'image'})
a71_p2.lesson = l71
a71_p2.asset_type = 'image'
a71_p2.source_type = 'external'
a71_p2.storage_type = 'url'
a71_p2.status = 'attached'
a71_p2.title = "Laboratory Gas Syringe Apparatus for Investigating Gaseous Volume and Pressure Equilibrium"
a71_p2.description = "Photograph of a gas syringe used to demonstrate volume reduction and pressure shifts in gaseous equilibrium systems such as NO2/N2O4."
a71_p2.url = "https://upload.wikimedia.org/wikipedia/commons/f/f1/Gas_syringe.jpg"
a71_p2.metadata = {
    'author': 'User:Geni',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'User:Geni / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Gas_syringe.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Gas volume and pressure manipulation'
}
a71_p2.save()
a71_p2.blocks.set([b71_p2])
print("Lesson 71 Page 2: Asset 334 attached.")

# P3: Pressurized Gas Cylinder (Wikimedia Image)
b71_p3 = get_or_create_diagram_block(l71, 3, "Industrial High-Pressure Gas Cylinder Storage Vessel")
a71_p3, _ = LessonAsset.objects.get_or_create(id=335, defaults={'lesson': l71, 'asset_type': 'image'})
a71_p3.lesson = l71
a71_p3.asset_type = 'image'
a71_p3.source_type = 'external'
a71_p3.storage_type = 'url'
a71_p3.status = 'attached'
a71_p3.title = "Industrial High-Pressure Gas Cylinder Storage Vessel"
a71_p3.description = "Photograph of a heavy-duty steel pressurized gas cylinder capable of containing high-pressure gaseous systems."
a71_p3.url = "https://upload.wikimedia.org/wikipedia/commons/0/05/A_liquefied_petroleum_gas_%28LPG%29_cylinder.jpg"
a71_p3.metadata = {
    'author': 'ShriniwasGajare',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'ShriniwasGajare / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_liquefied_petroleum_gas_(LPG)_cylinder.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'High pressure industrial gas containment'
}
a71_p3.save()
a71_p3.blocks.set([b71_p3])
print("Lesson 71 Page 3: Asset 335 attached.")

# P4: Gaseous Equilibrium Pressure Shift Model (Generated SVG)
svg_71_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">PRESSURE EFFECT ON GASEOUS CHEMICAL EQUILIBRIUM</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Increasing Pressure Shifts Equilibrium Toward the Side with FEWER Gaseous Moles</text>

  <g transform="translate(45, 75)">
    <!-- Left: Low Pressure (High Volume) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#d97706" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">LOW PRESSURE (LARGE VOLUME)</text>

      <rect x="70" y="60" width="205" height="150" fill="#020617" stroke="#64748b" stroke-width="2"/>
      <rect x="70" y="60" width="205" height="16" fill="#475569" stroke="#94a3b8"/>

      <!-- Nitrogen Dioxide gas molecules (2 moles NO2 - Brown) -->
      <circle cx="100" cy="110" r="10" fill="#b45309"/><text x="100" y="114" text-anchor="middle" fill="#fff" font-size="8">NO₂</text>
      <circle cx="140" cy="160" r="10" fill="#b45309"/><text x="140" y="164" text-anchor="middle" fill="#fff" font-size="8">NO₂</text>
      <circle cx="210" cy="120" r="10" fill="#b45309"/><text x="210" y="124" text-anchor="middle" fill="#fff" font-size="8">NO₂</text>
      <circle cx="230" cy="180" r="10" fill="#b45309"/><text x="230" y="184" text-anchor="middle" fill="#fff" font-size="8">NO₂</text>

      <rect x="15" y="230" width="315" height="90" rx="8" fill="#020617"/>
      <text x="25" y="253" fill="#fbbf24" font-size="11" font-weight="bold">• 2 moles of gas (2NO₂) favored</text>
      <text x="25" y="273" fill="#cbd5e1" font-size="10">• More gas molecules create more collisions</text>
      <text x="25" y="293" fill="#f59e0b" font-size="10" font-weight="bold">• Visual appearance: Deep Dark Brown Gas</text>
    </g>

    <!-- Right: High Pressure (Compressed Volume) -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="172" y="32" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">HIGH PRESSURE (COMPRESSED VOLUME)</text>

      <rect x="70" y="60" width="205" height="150" fill="#020617" stroke="#64748b" stroke-width="2"/>
      <rect x="70" y="125" width="205" height="16" fill="#475569" stroke="#34d399"/>

      <!-- Dinitrogen Tetroxide dimer (1 mole N2O4 - Colorless/Pale) -->
      <rect x="130" y="155" width="85" height="32" rx="10" fill="#334155" stroke="#38bdf8"/>
      <text x="172" y="176" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="bold">N₂O₄ (1 mole)</text>

      <rect x="15" y="230" width="315" height="90" rx="8" fill="#020617"/>
      <text x="25" y="253" fill="#34d399" font-size="11" font-weight="bold">• 1 mole of gas (N₂O₄) favored</text>
      <text x="25" y="273" fill="#cbd5e1" font-size="10">• Equilibrium shifts forward to reduce total molecules</text>
      <text x="25" y="293" fill="#4ade80" font-size="10" font-weight="bold">• Visual appearance: Pale / Colorless Gas</text>
    </g>
  </g>
</svg>'''
b71_p4 = get_or_create_diagram_block(l71, 4, "Gaseous Equilibrium Mole Reduction Model Under Pressure")
a71_p4, _ = LessonAsset.objects.get_or_create(id=336, defaults={'lesson': l71, 'asset_type': 'diagram'})
a71_p4.lesson = l71
a71_p4.asset_type = 'diagram'
a71_p4.source_type = 'ai_generated'
a71_p4.storage_type = 'file'
a71_p4.status = 'attached'
a71_p4.title = "Gaseous Equilibrium Mole Reduction Model Under Pressure"
a71_p4.description = "Diagram demonstrating how increasing pressure shifts the 2NO2 ⇌ N2O4 equilibrium toward the side with fewer gas molecules."
a71_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_71_p4)
a71_p4.file.save(f'pressure_equilibrium_{l71.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a71_p4.blocks.set([b71_p4])
print("Lesson 71 Page 4: Asset 336 saved and attached.")


# =========================================================================
# 3. LESSON 72: Effect of Temperature on Equilibrium
# =========================================================================
l72 = Lesson.objects.get(id=72)
print(f"\nProcessing Lesson 72: {l72.title}")

# P2: Cobalt Chloride Thermal Equilibrium (Wikimedia Image)
b72_p2 = get_or_create_diagram_block(l72, 2, "Cobalt(II) Chloride Aqueous Equilibrium Solution Exhibiting Reversible Thermal Color Transitions")
a72_p2, _ = LessonAsset.objects.get_or_create(id=337, defaults={'lesson': l72, 'asset_type': 'image'})
a72_p2.lesson = l72
a72_p2.asset_type = 'image'
a72_p2.source_type = 'external'
a72_p2.storage_type = 'url'
a72_p2.status = 'attached'
a72_p2.title = "Cobalt(II) Chloride Aqueous Equilibrium Solution Exhibiting Reversible Thermal Color Transitions"
a72_p2.description = "Photograph showing the temperature-dependent color change of aqueous cobalt(II) chloride: pink [Co(H2O)6]2+ in cold water vs blue [CoCl4]2- when heated."
a72_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cobalt_chloride_equilibrium.JPG/800px-Cobalt_chloride_equilibrium.JPG"
a72_p2.metadata = {
    'author': 'Chemicalinterest',
    'licensing': 'Public domain',
    'attribution': 'Chemicalinterest / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Cobalt_chloride_equilibrium.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Temperature-dependent reversible color transition'
}
a72_p2.save()
a72_p2.blocks.set([b72_p2])
print("Lesson 72 Page 2: Asset 337 attached.")

# P3: Laboratory Ice Bath Setup (Wikimedia Image)
b72_p3 = get_or_create_diagram_block(l72, 3, "Laboratory Ice Bath Beaker Setup for Low-Temperature Equilibrium Observation")
a72_p3, _ = LessonAsset.objects.get_or_create(id=338, defaults={'lesson': l72, 'asset_type': 'image'})
a72_p3.lesson = l72
a72_p3.asset_type = 'image'
a72_p3.source_type = 'external'
a72_p3.storage_type = 'url'
a72_p3.status = 'attached'
a72_p3.title = "Laboratory Ice Bath Beaker Setup for Low-Temperature Equilibrium Observation"
a72_p3.description = "Photograph of a laboratory ice-water bath apparatus used to cool reversible reaction mixtures and favor exothermic pathways."
a72_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/%28TiO2%29%5E2%2B_Kation.jpg/800px-%28TiO2%29%5E2%2B_Kation.jpg"
a72_p3.metadata = {
    'author': 'Johannes Schneider',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Johannes Schneider / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:(TiO2)^2+_Kation.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Cooling bath for chemical equilibrium'
}
a72_p3.save()
a72_p3.blocks.set([b72_p3])
print("Lesson 72 Page 3: Asset 338 attached.")

# P4: Temperature Perturbation Thermodynamics (Generated SVG)
svg_72_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">TEMPERATURE PERTURBATION ON CHEMICAL EQUILIBRIUM</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Le Chatelier's Principle: System Shifts in the Endothermic Direction (+ΔH) to Absorb Added Heat</text>

  <g transform="translate(45, 75)">
    <!-- System A: Exothermic Forward (-ΔH) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="172" y="30" text-anchor="middle" fill="#f87171" font-size="13" font-weight="bold">EXOTHERMIC FORWARD (ΔH = -VE)</text>
      
      <rect x="15" y="55" width="315" height="55" rx="8" fill="#020617" stroke="#ef4444"/>
      <text x="172" y="78" text-anchor="middle" fill="#f8fafc" font-size="11" font-family="monospace">N₂(g) + 3H₂(g) ⇌ 2NH₃(g) + HEAT</text>
      <text x="172" y="98" text-anchor="middle" fill="#fca5a5" font-size="10">Forward produces heat (ΔH = -92 kJ/mol)</text>

      <rect x="15" y="125" width="315" height="90" rx="8" fill="#020617" stroke="#334155"/>
      <text x="25" y="148" fill="#ef4444" font-size="11" font-weight="bold">Effect of Heating (Temp Increase):</text>
      <text x="25" y="170" fill="#cbd5e1" font-size="10">• System shifts LEFT to absorb heat</text>
      <text x="25" y="190" fill="#f87171" font-size="10" font-weight="bold">• Yield of NH₃ decreases</text>
      <text x="25" y="208" fill="#94a3b8" font-size="9">Kc decreases with rising temperature</text>

      <rect x="15" y="225" width="315" height="95" rx="8" fill="#020617" stroke="#10b981"/>
      <text x="25" y="248" fill="#34d399" font-size="11" font-weight="bold">Effect of Cooling (Temp Decrease):</text>
      <text x="25" y="270" fill="#cbd5e1" font-size="10">• System shifts RIGHT to release heat</text>
      <text x="25" y="290" fill="#4ade80" font-size="10" font-weight="bold">• Yield of NH₃ increases</text>
      <text x="25" y="308" fill="#38bdf8" font-size="9">Rate slows down, requiring catalyst</text>
    </g>

    <!-- System B: Endothermic Forward (+ΔH) -->
    <g transform="translate(385, 0)">
      <rect x="0" y="0" width="345" height="335" rx="14" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <text x="172" y="30" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">ENDOTHERMIC FORWARD (ΔH = +VE)</text>
      
      <rect x="15" y="55" width="315" height="55" rx="8" fill="#020617" stroke="#0284c7"/>
      <text x="172" y="78" text-anchor="middle" fill="#f8fafc" font-size="11" font-family="monospace">N₂O₄(g) + HEAT ⇌ 2NO₂(g)</text>
      <text x="172" y="98" text-anchor="middle" fill="#7dd3fc" font-size="10">Forward absorbs heat (ΔH = +58 kJ/mol)</text>

      <rect x="15" y="125" width="315" height="90" rx="8" fill="#020617" stroke="#334155"/>
      <text x="25" y="148" fill="#38bdf8" font-size="11" font-weight="bold">Effect of Heating (Temp Increase):</text>
      <text x="25" y="170" fill="#cbd5e1" font-size="10">• System shifts RIGHT to absorb heat</text>
      <text x="25" y="190" fill="#38bdf8" font-size="10" font-weight="bold">• Deep brown color (NO₂) intensifies</text>
      <text x="25" y="208" fill="#94a3b8" font-size="9">Kc increases with rising temperature</text>

      <rect x="15" y="225" width="315" height="95" rx="8" fill="#020617" stroke="#64748b"/>
      <text x="25" y="248" fill="#94a3b8" font-size="11" font-weight="bold">Effect of Cooling (Temp Decrease):</text>
      <text x="25" y="270" fill="#cbd5e1" font-size="10">• System shifts LEFT to produce heat</text>
      <text x="25" y="290" fill="#cbd5e1" font-size="10" font-weight="bold">• Solution becomes pale/colorless (N₂O₄)</text>
      <text x="25" y="308" fill="#7dd3fc" font-size="9">Forward endothermic reaction slows</text>
    </g>
  </g>
</svg>'''
b72_p4 = get_or_create_diagram_block(l72, 4, "Thermodynamic Heat Absorption and Equilibrium Temperature Shifts")
a72_p4, _ = LessonAsset.objects.get_or_create(id=339, defaults={'lesson': l72, 'asset_type': 'diagram'})
a72_p4.lesson = l72
a72_p4.asset_type = 'diagram'
a72_p4.source_type = 'ai_generated'
a72_p4.storage_type = 'file'
a72_p4.status = 'attached'
a72_p4.title = "Thermodynamic Heat Absorption and Equilibrium Temperature Shifts"
a72_p4.description = "Comparative analysis of temperature changes on exothermic versus endothermic reversible chemical reactions."
a72_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_72_p4)
a72_p4.file.save(f'temperature_equilibrium_{l72.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a72_p4.blocks.set([b72_p4])
print("Lesson 72 Page 4: Asset 339 saved and attached.")


# =========================================================================
# 4. LESSON 73: Catalysts and Equilibrium
# =========================================================================
l73 = Lesson.objects.get(id=73)
print(f"\nProcessing Lesson 73: {l73.title}")

# P2: Iron Filings Catalyst (Wikimedia Image)
b73_p2 = get_or_create_diagram_block(l73, 2, "Finely Divided Iron Filings Catalyst Used in Industrial Chemical Synthesis")
a73_p2, _ = LessonAsset.objects.get_or_create(id=340, defaults={'lesson': l73, 'asset_type': 'image'})
a73_p2.lesson = l73
a73_p2.asset_type = 'image'
a73_p2.source_type = 'external'
a73_p2.storage_type = 'url'
a73_p2.status = 'attached'
a73_p2.title = "Finely Divided Iron Filings Catalyst Used in Industrial Chemical Synthesis"
a73_p2.description = "Photograph of finely divided iron metal powder used as a heterogeneous catalyst to speed up the establishment of chemical equilibrium."
a73_p2.url = "https://upload.wikimedia.org/wikipedia/commons/1/10/Fe_filings.JPG"
a73_p2.metadata = {
    'author': 'Chemicalinterest',
    'licensing': 'Public domain',
    'attribution': 'Chemicalinterest / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Fe_filings.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Heterogeneous solid catalyst'
}
a73_p2.save()
a73_p2.blocks.set([b73_p2])
print("Lesson 73 Page 2: Asset 340 attached.")

# P3: Heterogeneous Catalysis (Wikimedia Image)
b73_p3 = get_or_create_diagram_block(l73, 3, "Vigorous Solid-Liquid Heterogeneous Catalysis in Reversible Reaction Systems")
a73_p3, _ = LessonAsset.objects.get_or_create(id=341, defaults={'lesson': l73, 'asset_type': 'image'})
a73_p3.lesson = l73
a73_p3.asset_type = 'image'
a73_p3.source_type = 'external'
a73_p3.storage_type = 'url'
a73_p3.status = 'attached'
a73_p3.title = "Vigorous Solid-Liquid Heterogeneous Catalysis in Reversible Reaction Systems"
a73_p3.description = "Photograph demonstrating rapid catalytic gas generation where the solid catalyst accelerates both forward and backward reaction rates."
a73_p3.url = "https://upload.wikimedia.org/wikipedia/commons/2/27/H2O2_catalytic_decomposition.JPG"
a73_p3.metadata = {
    'author': 'Chemicalinterest',
    'licensing': 'Public domain',
    'attribution': 'Chemicalinterest / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:H2O2_catalytic_decomposition.JPG',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Rapid catalytic acceleration'
}
a73_p3.save()
a73_p3.blocks.set([b73_p3])
print("Lesson 73 Page 3: Asset 341 attached.")

# P4: Catalyst Reaction Time vs Yield (Generated SVG)
svg_73_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">CATALYST ACTION: TIME TO EQUILIBRIUM VS. PRODUCT YIELD</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">A Catalyst Drastically Shortens Reaction Time Without Changing the Final Equilibrium Yield</text>

  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>

    <!-- Y Axis: % Yield of Product -->
    <line x1="70" y1="280" x2="70" y2="40" stroke="#94a3b8" stroke-width="2"/>
    <text x="50" y="160" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold" transform="rotate(-90 50 160)">Product Yield (%)</text>

    <!-- X Axis: Time -->
    <line x1="70" y1="280" x2="620" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <text x="345" y="305" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Time (Hours / Days)</text>

    <!-- Equilibrium Plateau Line (Same for both!) -->
    <line x1="70" y1="90" x2="600" y2="90" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4"/>
    <text x="480" y="80" fill="#fbbf24" font-size="11" font-weight="bold">Equilibrium Yield (15% NH₃)</text>

    <!-- Catalyzed Curve (Fast Rise - Green) -->
    <path d="M 70 280 Q 120 90 220 90 L 600 90" fill="none" stroke="#10b981" stroke-width="3.5"/>
    <text x="180" y="115" fill="#34d399" font-size="11" font-weight="bold">With Catalyst (Fast - Minutes)</text>

    <!-- Uncatalyzed Curve (Slow Rise - Red) -->
    <path d="M 70 280 Q 300 250 480 110 L 600 90" fill="none" stroke="#ef4444" stroke-width="3"/>
    <text x="380" y="170" fill="#f87171" font-size="11" font-weight="bold">Without Catalyst (Slow - Weeks)</text>

    <!-- Key Concept Callout Box -->
    <rect x="250" y="195" width="420" height="75" rx="8" fill="#020617" stroke="#334155"/>
    <text x="460" y="218" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Key Distinction for National Exams:</text>
    <text x="460" y="238" text-anchor="middle" fill="#cbd5e1" font-size="10">✓ Catalyst increases the RATE at which equilibrium is reached.</text>
    <text x="460" y="256" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">✗ Catalyst NEVER alters equilibrium position or percentage yield.</text>
  </g>
</svg>'''
b73_p4 = get_or_create_diagram_block(l73, 4, "Comparative Yield-Time Kinetics for Catalyzed vs. Uncatalyzed Equilibrium")
a73_p4, _ = LessonAsset.objects.get_or_create(id=342, defaults={'lesson': l73, 'asset_type': 'diagram'})
a73_p4.lesson = l73
a73_p4.asset_type = 'diagram'
a73_p4.source_type = 'ai_generated'
a73_p4.storage_type = 'file'
a73_p4.status = 'attached'
a73_p4.title = "Comparative Yield-Time Kinetics for Catalyzed vs. Uncatalyzed Equilibrium"
a73_p4.description = "Graph demonstrating that adding a catalyst significantly reduces time required to reach equilibrium while the final product yield remains identical."
a73_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_73_p4)
a73_p4.file.save(f'catalyst_yield_time_{l73.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a73_p4.blocks.set([b73_p4])
print("Lesson 73 Page 4: Asset 342 saved and attached.")


# =========================================================================
# 5. LESSON 74: Some Industrial Applications of Chemical Equilibrium
# =========================================================================
l74 = Lesson.objects.get(id=74)
print(f"\nProcessing Lesson 74: {l74.title}")

# P2: Heavy Industrial Synthesis Plant (Wikimedia Image)
b74_p2 = get_or_create_diagram_block(l74, 2, "Heavy Industrial Chemical Fertilizer and Synthesis Facility")
a74_p2, _ = LessonAsset.objects.get_or_create(id=343, defaults={'lesson': l74, 'asset_type': 'image'})
a74_p2.lesson = l74
a74_p2.asset_type = 'image'
a74_p2.source_type = 'external'
a74_p2.storage_type = 'url'
a74_p2.status = 'attached'
a74_p2.title = "Heavy Industrial Chemical Fertilizer and Synthesis Facility"
a74_p2.description = "Photograph of industrial chemical reactors, distillation columns, and high-pressure piping in an ammonia and fertilizer manufacturing complex."
a74_p2.url = "https://upload.wikimedia.org/wikipedia/commons/9/9b/Haifa_Gezicht_op_installaties_op_het_terrein_van_een_kunstmestfabriek,_Bestanddeelnr_255-9320.jpg"
a74_p2.metadata = {
    'author': 'Willem van de Poll',
    'licensing': 'CC0',
    'attribution': 'Willem van de Poll / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Haifa_Gezicht_op_installaties_op_het_terrein_van_een_kunstmestfabriek,_Bestanddeelnr_255-9320.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Industrial equilibrium plant operations'
}
a74_p2.save()
a74_p2.blocks.set([b74_p2])
print("Lesson 74 Page 2: Asset 343 attached.")

# P3: Industrial Compressor Mechanism (Wikimedia Image)
b74_p3 = get_or_create_diagram_block(l74, 3, "High-Pressure Industrial Gas Compressor Mechanism in Synthesis Plants")
a74_p3, _ = LessonAsset.objects.get_or_create(id=344, defaults={'lesson': l74, 'asset_type': 'image'})
a74_p3.lesson = l74
a74_p3.asset_type = 'image'
a74_p3.source_type = 'external'
a74_p3.storage_type = 'url'
a74_p3.status = 'attached'
a74_p3.title = "High-Pressure Industrial Gas Compressor Mechanism in Synthesis Plants"
a74_p3.description = "Photograph of an industrial gas compression system used to maintain 200 atm pressures in the Haber ammonia synthesis process."
a74_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Compressor_Danfoss_SC18CL.jpg/800px-Compressor_Danfoss_SC18CL.jpg"
a74_p3.metadata = {
    'author': 'Лобачев Владимир',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Лобачев Владимир / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Compressor_Danfoss_SC18CL.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Industrial gas compression'
}
a74_p3.save()
a74_p3.blocks.set([b74_p3])
print("Lesson 74 Page 3: Asset 344 attached.")

# P4: Industrial Multi-Criteria Equilibrium Optimization (Generated SVG)
svg_74_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <text x="410" y="34" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">INDUSTRIAL EQUILIBRIUM: THE TRIAD OF OPTIMIZATION</text>
  <text x="410" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Chemical Engineering Balances Thermodynamic Yield, Kinetic Reaction Rate, and Plant Operating Costs</text>

  <g transform="translate(60, 75)">
    <rect x="0" y="0" width="700" height="335" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Pillar 1: Temperature Compromise -->
    <g transform="translate(25, 20)">
      <rect x="0" y="0" width="195" height="295" rx="10" fill="#020617" stroke="#ef4444"/>
      <text x="97" y="30" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">1. TEMPERATURE</text>
      <text x="97" y="50" text-anchor="middle" fill="#fca5a5" font-size="10">450°C (Compromise)</text>
      <rect x="15" y="70" width="165" height="1" fill="#334155"/>
      <text x="15" y="95" fill="#38bdf8" font-size="10">• Low T = Higher % Yield</text>
      <text x="15" y="115" fill="#94a3b8" font-size="9">(Exothermic forward shift)</text>
      <text x="15" y="145" fill="#f87171" font-size="10">• Low T = Too Slow Rate</text>
      <text x="15" y="165" fill="#94a3b8" font-size="9">(Particles lack Ea)</text>
      <text x="15" y="200" fill="#4ade80" font-size="10" font-weight="bold">Solution:</text>
      <text x="15" y="220" fill="#cbd5e1" font-size="9">Operate at 450°C + Catalyst for rapid output</text>
    </g>

    <!-- Pillar 2: Pressure Compromise -->
    <g transform="translate(250, 20)">
      <rect x="0" y="0" width="195" height="295" rx="10" fill="#020617" stroke="#38bdf8"/>
      <text x="97" y="30" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">2. PRESSURE</text>
      <text x="97" y="50" text-anchor="middle" fill="#7dd3fc" font-size="10">200 atm (Haber)</text>
      <rect x="15" y="70" width="165" height="1" fill="#334155"/>
      <text x="15" y="95" fill="#34d399" font-size="10">• High P = Higher Yield</text>
      <text x="15" y="115" fill="#94a3b8" font-size="9">(Shifts to fewer gas moles)</text>
      <text x="15" y="145" fill="#fbbf24" font-size="10">• High P = High Risk &amp; Cost</text>
      <text x="15" y="165" fill="#94a3b8" font-size="9">(Thick steel pipes, leaks)</text>
      <text x="15" y="200" fill="#4ade80" font-size="10" font-weight="bold">Solution:</text>
      <text x="15" y="220" fill="#cbd5e1" font-size="9">200 atm gives 15% yield safely and economically</text>
    </g>

    <!-- Pillar 3: Recycling & Catalyst -->
    <g transform="translate(475, 20)">
      <rect x="0" y="0" width="200" height="295" rx="10" fill="#020617" stroke="#10b981"/>
      <text x="100" y="30" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">3. RECYCLING LOOP</text>
      <text x="100" y="50" text-anchor="middle" fill="#a7f3d0" font-size="10">98% Overall Efficiency</text>
      <rect x="15" y="70" width="170" height="1" fill="#334155"/>
      <text x="15" y="95" fill="#fbbf24" font-size="10">• Single pass = 15% yield</text>
      <text x="15" y="115" fill="#94a3b8" font-size="9">(85% unreacted N₂ + H₂)</text>
      <text x="15" y="145" fill="#38bdf8" font-size="10">• Cool to liquefy NH₃</text>
      <text x="15" y="165" fill="#94a3b8" font-size="9">(Boiling pt = -33°C)</text>
      <text x="15" y="200" fill="#4ade80" font-size="10" font-weight="bold">Solution:</text>
      <text x="15" y="220" fill="#cbd5e1" font-size="9">Recycle unreacted gas continuously back to reactor</text>
    </g>
  </g>
</svg>'''
b74_p4 = get_or_create_diagram_block(l74, 4, "Industrial Triad Decision Framework for Chemical Equilibrium Optimization")
a74_p4, _ = LessonAsset.objects.get_or_create(id=345, defaults={'lesson': l74, 'asset_type': 'diagram'})
a74_p4.lesson = l74
a74_p4.asset_type = 'diagram'
a74_p4.source_type = 'ai_generated'
a74_p4.storage_type = 'file'
a74_p4.status = 'attached'
a74_p4.title = "Industrial Triad Decision Framework for Chemical Equilibrium Optimization"
a74_p4.description = "Three-pillar framework diagram illustrating the compromise conditions between yield, reaction rate, and plant operating costs."
a74_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_74_p4)
a74_p4.file.save(f'industrial_triad_equilibrium_{l74.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a74_p4.blocks.set([b74_p4])
print("Lesson 74 Page 4: Asset 345 saved and attached.")


# =========================================================================
# 6. LESSON 75: The Haber Process
# =========================================================================
l75 = Lesson.objects.get(id=75)
print(f"\nProcessing Lesson 75: {l75.title}")

# P2: Finely Divided Iron Catalyst (Wikimedia Image)
b75_p2 = get_or_create_diagram_block(l75, 2, "Porous Granular Iron Metal Catalyst Used in the Haber-Bosch Synthesis Reactor")
a75_p2, _ = LessonAsset.objects.get_or_create(id=346, defaults={'lesson': l75, 'asset_type': 'image'})
a75_p2.lesson = l75
a75_p2.asset_type = 'image'
a75_p2.source_type = 'external'
a75_p2.storage_type = 'url'
a75_p2.status = 'attached'
a75_p2.title = "Porous Granular Iron Metal Catalyst Used in the Haber-Bosch Synthesis Reactor"
a75_p2.description = "Photograph of finely divided iron metal filings that provide the catalytic surface for nitrogen and hydrogen gas adsorption in ammonia synthesis."
a75_p2.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/A_field_of_magnetised_iron_filings.jpg/800px-A_field_of_magnetised_iron_filings.jpg"
a75_p2.metadata = {
    'author': 'The Sandpainter',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'The Sandpainter / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:A_field_of_magnetised_iron_filings.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Iron catalyst in Haber process'
}
a75_p2.save()
a75_p2.blocks.set([b75_p2])
print("Lesson 75 Page 2: Asset 346 attached.")

# P3: Industrial Ammonia Plant (Wikimedia Image)
b75_p3 = get_or_create_diagram_block(l75, 3, "Industrial Multi-Stage Chemical Synthesis Tower and Compression Plant")
a75_p3, _ = LessonAsset.objects.get_or_create(id=347, defaults={'lesson': l75, 'asset_type': 'image'})
a75_p3.lesson = l75
a75_p3.asset_type = 'image'
a75_p3.source_type = 'external'
a75_p3.storage_type = 'url'
a75_p3.status = 'attached'
a75_p3.title = "Industrial Multi-Stage Chemical Synthesis Tower and Compression Plant"
a75_p3.description = "Photograph of a commercial synthesis facility where nitrogen and hydrogen gases are reacted under 200 atm to produce ammonia for agricultural fertilizers."
a75_p3.url = "https://upload.wikimedia.org/wikipedia/commons/9/9b/Haifa_Gezicht_op_installaties_op_het_terrein_van_een_kunstmestfabriek,_Bestanddeelnr_255-9320.jpg"
a75_p3.metadata = {
    'author': 'Willem van de Poll',
    'licensing': 'CC0',
    'attribution': 'Willem van de Poll / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Haifa_Gezicht_op_installaties_op_het_terrein_van_een_kunstmestfabriek,_Bestanddeelnr_255-9320.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Commercial Haber ammonia plant'
}
a75_p3.save()
a75_p3.blocks.set([b75_p3])
print("Lesson 75 Page 3: Asset 347 attached.")

# P4: Industrial Flowsheet of Haber Process (Generated SVG)
svg_75_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="hArr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">INDUSTRIAL HABER PROCESS FLOWSHEET</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Synthesis of Ammonia: N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH = -92 kJ/mol) at 450°C, 200 atm, Fe Catalyst</text>

  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="760" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Stage 1: Gas Feeds -->
    <rect x="20" y="120" width="100" height="85" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
    <text x="70" y="145" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">GAS FEED</text>
    <text x="70" y="165" text-anchor="middle" fill="#f8fafc" font-size="11">N₂ (Air)</text>
    <text x="70" y="185" text-anchor="middle" fill="#f8fafc" font-size="11">+ 3H₂ (Methane)</text>

    <!-- Arrow to Compressor -->
    <path d="M 120 162 L 160 162" stroke="#38bdf8" stroke-width="3" marker-end="url(#hArr)"/>

    <!-- Stage 2: Compressor -->
    <rect x="165" y="120" width="105" height="85" rx="8" fill="#020617" stroke="#f59e0b" stroke-width="2"/>
    <text x="217" y="145" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">COMPRESSOR</text>
    <text x="217" y="170" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">200 atm</text>
    <text x="217" y="190" text-anchor="middle" fill="#94a3b8" font-size="9">Pressure Raised</text>

    <!-- Arrow to Catalytic Reactor -->
    <path d="M 270 162 L 310 162" stroke="#38bdf8" stroke-width="3" marker-end="url(#hArr)"/>

    <!-- Stage 3: Catalytic Converter -->
    <rect x="315" y="85" width="150" height="155" rx="10" fill="#020617" stroke="#ef4444" stroke-width="2"/>
    <text x="390" y="112" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">CATALYTIC REACTOR</text>
    <rect x="330" y="125" width="120" height="40" rx="4" fill="#334155"/>
    <text x="390" y="145" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Finely Divided Iron (Fe)</text>
    <text x="390" y="157" text-anchor="middle" fill="#94a3b8" font-size="8">+ Al₂O₃ Promoter</text>
    <text x="390" y="195" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">450°C</text>
    <text x="390" y="215" text-anchor="middle" fill="#34d399" font-size="10">15% Conversion to NH₃</text>

    <!-- Arrow to Cooler / Condenser -->
    <path d="M 465 162 L 505 162" stroke="#38bdf8" stroke-width="3" marker-end="url(#hArr)"/>

    <!-- Stage 4: Condenser -->
    <rect x="510" y="105" width="125" height="115" rx="8" fill="#020617" stroke="#06b6d4" stroke-width="2"/>
    <text x="572" y="132" text-anchor="middle" fill="#22d3ee" font-size="11" font-weight="bold">CONDENSER</text>
    <text x="572" y="155" text-anchor="middle" fill="#94a3b8" font-size="10">Cools to -33°C</text>
    <text x="572" y="180" text-anchor="middle" fill="#38bdf8" font-size="10">NH₃ Liquefies</text>
    <text x="572" y="200" text-anchor="middle" fill="#94a3b8" font-size="8">N₂ &amp; H₂ remain gases</text>

    <!-- Liquid Ammonia Outlet (Down) -->
    <path d="M 572 220 L 572 275" stroke="#38bdf8" stroke-width="3" marker-end="url(#hArr)"/>
    <rect x="500" y="280" width="145" height="50" rx="8" fill="#0284c7"/>
    <text x="572" y="302" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">LIQUID AMMONIA</text>
    <text x="572" y="320" text-anchor="middle" fill="#e0f2fe" font-size="9">Stored for Fertilizers</text>

    <!-- Recycling Pipe Loop (Top: Back to Compressor) -->
    <path d="M 572 105 L 572 45 L 217 45 L 217 115" fill="none" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="4" marker-end="url(#hArr)"/>
    <rect x="300" y="32" width="180" height="24" rx="4" fill="#020617" stroke="#4ade80"/>
    <text x="390" y="48" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">Recycling Unreacted N₂ &amp; H₂ (85%)</text>
  </g>
</svg>'''
b75_p4 = get_or_create_diagram_block(l75, 4, "Complete Industrial Haber Process Schematic and Gas Recirculation Loop")
a75_p4, _ = LessonAsset.objects.get_or_create(id=348, defaults={'lesson': l75, 'asset_type': 'diagram'})
a75_p4.lesson = l75
a75_p4.asset_type = 'diagram'
a75_p4.source_type = 'ai_generated'
a75_p4.storage_type = 'file'
a75_p4.status = 'attached'
a75_p4.title = "Complete Industrial Haber Process Schematic and Gas Recirculation Loop"
a75_p4.description = "Complete industrial flowsheet of ammonia manufacturing showing gas compression, catalytic reactor at 450°C and 200 atm, cooling condenser, and gas recycling."
a75_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_75_p4)
a75_p4.file.save(f'haber_process_flowsheet_{l75.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a75_p4.blocks.set([b75_p4])
print("Lesson 75 Page 4: Asset 348 saved and attached.")


# =========================================================================
# 7. LESSON 76: The Contact Process
# =========================================================================
l76 = Lesson.objects.get(id=76)
print(f"\nProcessing Lesson 76: {l76.title}")

# P2: Bright Yellow Sulfur Crystals (Wikimedia Image)
b76_p2 = get_or_create_diagram_block(l76, 2, "Crystalline Bright Yellow Elemental Sulfur Mineral Raw Material")
a76_p2, _ = LessonAsset.objects.get_or_create(id=349, defaults={'lesson': l76, 'asset_type': 'image'})
a76_p2.lesson = l76
a76_p2.asset_type = 'image'
a76_p2.source_type = 'external'
a76_p2.storage_type = 'url'
a76_p2.status = 'attached'
a76_p2.title = "Crystalline Bright Yellow Elemental Sulfur Mineral Raw Material"
a76_p2.description = "Photograph of pure yellow elemental sulfur crystals used as the starting feedstock burned to generate sulfur dioxide in the Contact Process."
a76_p2.url = "https://upload.wikimedia.org/wikipedia/commons/2/2d/Celestine-Sulfur-j08-12a.jpg"
a76_p2.metadata = {
    'author': 'Robert M. Lavinsky',
    'licensing': 'CC BY-SA 3.0',
    'attribution': 'Robert M. Lavinsky / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Celestine-Sulfur-j08-12a.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Sulfur raw material for sulfuric acid'
}
a76_p2.save()
a76_p2.blocks.set([b76_p2])
print("Lesson 76 Page 2: Asset 349 attached.")

# P3: Commercial Sulfuric Acid Reagent (Wikimedia Image)
b76_p3 = get_or_create_diagram_block(l76, 3, "Commercial Concentrated Sulfuric Acid Reagent Vessel")
a76_p3, _ = LessonAsset.objects.get_or_create(id=350, defaults={'lesson': l76, 'asset_type': 'image'})
a76_p3.lesson = l76
a76_p3.asset_type = 'image'
a76_p3.source_type = 'external'
a76_p3.storage_type = 'url'
a76_p3.status = 'attached'
a76_p3.title = "Commercial Concentrated Sulfuric Acid Reagent Vessel"
a76_p3.description = "Photograph of high-purity industrial grade sulfuric acid manufactured as the final commercial product of the Contact Process."
a76_p3.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Battery_fluid%2C_plastic_bottle.jpg/800px-Battery_fluid%2C_plastic_bottle.jpg"
a76_p3.metadata = {
    'author': 'Cjp24',
    'licensing': 'CC BY-SA 4.0',
    'attribution': 'Cjp24 / Wikimedia Commons',
    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Battery_fluid,_plastic_bottle.jpg',
    'provenance': 'WikimediaProvider',
    'enrichment_agent': True,
    'concept': 'Sulfuric acid industrial product'
}
a76_p3.save()
a76_p3.blocks.set([b76_p3])
print("Lesson 76 Page 3: Asset 350 attached.")

# P4: Industrial Contact Process Flowsheet (Generated SVG)
svg_76_p4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%" style="background-color: #0a0f1d; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <marker id="cArr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <text x="410" y="32" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="bold">INDUSTRIAL CONTACT PROCESS FLOWSHEET</text>
  <text x="410" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Manufacture of H₂SO₄: 2SO₂(g) + O₂(g) ⇌ 2SO₃(g) at 450°C, 1-2 atm, V₂O₅ Catalyst (98% Yield)</text>

  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="760" height="355" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Stage 1: Sulfur Burner -->
    <rect x="15" y="110" width="115" height="105" rx="8" fill="#020617" stroke="#f59e0b" stroke-width="2"/>
    <text x="72" y="132" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">1. SULFUR BURNER</text>
    <text x="72" y="155" text-anchor="middle" fill="#f8fafc" font-size="10">S(s) + O₂(g) → SO₂(g)</text>
    <text x="72" y="175" text-anchor="middle" fill="#cbd5e1" font-size="9">Air Scrubbed</text>
    <text x="72" y="195" text-anchor="middle" fill="#94a3b8" font-size="8">Dust Precipitator</text>

    <!-- Arrow to Purifier -->
    <path d="M 130 162 L 160 162" stroke="#38bdf8" stroke-width="3" marker-end="url(#cArr)"/>

    <!-- Stage 2: Gas Purifier & Heat Exchanger -->
    <rect x="165" y="110" width="115" height="105" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
    <text x="222" y="132" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">2. PURIFIER UNIT</text>
    <text x="222" y="155" text-anchor="middle" fill="#cbd5e1" font-size="9">Removes As₂O₃</text>
    <text x="222" y="175" text-anchor="middle" fill="#f87171" font-size="9">(Prevents poisoning</text>
    <text x="222" y="192" text-anchor="middle" fill="#f87171" font-size="9">of V₂O₅ catalyst)</text>

    <!-- Arrow to Converter -->
    <path d="M 280 162 L 310 162" stroke="#38bdf8" stroke-width="3" marker-end="url(#cArr)"/>

    <!-- Stage 3: Catalytic Converter (V2O5) -->
    <rect x="315" y="85" width="145" height="155" rx="10" fill="#020617" stroke="#10b981" stroke-width="2"/>
    <text x="387" y="110" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">3. CONVERTER</text>
    <rect x="330" y="122" width="115" height="35" rx="4" fill="#334155"/>
    <text x="387" y="140" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Vanadium(V) Oxide</text>
    <text x="387" y="152" text-anchor="middle" fill="#fde68a" font-size="8">V₂O₅ Catalyst</text>
    <text x="387" y="180" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">450°C | 1-2 atm</text>
    <text x="387" y="200" text-anchor="middle" fill="#f8fafc" font-size="9">2SO₂ + O₂ ⇌ 2SO₃</text>
    <text x="387" y="220" text-anchor="middle" fill="#4ade80" font-size="10" font-weight="bold">98% High Yield</text>

    <!-- Arrow to Absorption Tower -->
    <path d="M 460 162 L 490 162" stroke="#38bdf8" stroke-width="3" marker-end="url(#cArr)"/>

    <!-- Stage 4: Absorption Tower -->
    <rect x="495" y="85" width="125" height="155" rx="8" fill="#020617" stroke="#a855f7" stroke-width="2"/>
    <text x="557" y="110" text-anchor="middle" fill="#c084fc" font-size="10" font-weight="bold">4. ABSORPTION</text>
    <text x="557" y="135" text-anchor="middle" fill="#94a3b8" font-size="9">Absorbed in 98%</text>
    <text x="557" y="152" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">Conc. H₂SO₄</text>
    <text x="557" y="180" text-anchor="middle" fill="#fbbf24" font-size="9">Forms OLEUM</text>
    <text x="557" y="200" text-anchor="middle" fill="#f8fafc" font-size="10">H₂S₂O₇(l)</text>
    <text x="557" y="225" text-anchor="middle" fill="#cbd5e1" font-size="8">(Avoids acid mist)</text>

    <!-- Arrow to Dilution Tank -->
    <path d="M 620 162 L 650 162" stroke="#38bdf8" stroke-width="3" marker-end="url(#cArr)"/>

    <!-- Stage 5: Dilution Tank -->
    <rect x="655" y="110" width="95" height="105" rx="8" fill="#0284c7" stroke="#38bdf8"/>
    <text x="702" y="135" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">5. DILUTION</text>
    <text x="702" y="155" text-anchor="middle" fill="#e0f2fe" font-size="8">+ Water (H₂O)</text>
    <text x="702" y="185" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">98% H₂SO₄</text>
    <text x="702" y="202" text-anchor="middle" fill="#e0f2fe" font-size="8">Final Acid</text>

    <!-- Why 1 atm note at bottom -->
    <rect x="40" y="265" width="680" height="65" rx="8" fill="#020617" stroke="#fbbf24"/>
    <text x="380" y="288" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Exam Insight: Why Pressure is Kept at 1-2 atm (Not High Pressure):</text>
    <text x="380" y="310" text-anchor="middle" fill="#cbd5e1" font-size="10">At 1-2 atm and 450°C with V₂O₅ catalyst, conversion is already 98%. Spending millions on high-pressure equipment is uneconomical.</text>
  </g>
</svg>'''
b76_p4 = get_or_create_diagram_block(l76, 4, "Complete Industrial Contact Process Flowsheet and Oleum Synthesis")
a76_p4, _ = LessonAsset.objects.get_or_create(id=351, defaults={'lesson': l76, 'asset_type': 'diagram'})
a76_p4.lesson = l76
a76_p4.asset_type = 'diagram'
a76_p4.source_type = 'ai_generated'
a76_p4.storage_type = 'file'
a76_p4.status = 'attached'
a76_p4.title = "Complete Industrial Contact Process Flowsheet and Oleum Synthesis"
a76_p4.description = "Complete industrial flowsheet for sulfuric acid manufacture detailing sulfur burning, gas purification, V2O5 catalytic conversion at 450°C, and oleum absorption."
a76_p4.metadata = {'render_format': 'svg', 'provenance': 'VisualReasoner', 'enrichment_agent': True}
is_valid, clean_svg, _ = validate_and_sanitize_svg(svg_76_p4)
a76_p4.file.save(f'contact_process_flowsheet_{l76.id}.svg', ContentFile(clean_svg.encode('utf-8')), save=True)
a76_p4.blocks.set([b76_p4])
print("Lesson 76 Page 4: Asset 351 saved and attached.")

print("\n=== Second Half of Topic 3 (Lessons 70–76) Completed Successfully! ===")
