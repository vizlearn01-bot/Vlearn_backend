import os
import sys
import django

sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

def clean_svg(svg_code):
    is_valid, sanitized, err = validate_and_sanitize_svg(svg_code)
    return sanitized if is_valid else svg_code

# 1. SVG for Lesson 150 Block 4026 (Writing Equations for Beta Emission)
BETA_EQUATIONS_SVG = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0b1120" rx="16"/>
  <text x="450" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Nuclear Chemistry: Writing and Balancing Beta (β⁻) Decay Equations</text>

  <!-- Left: Fundamental Neutron Transformation -->
  <rect x="40" y="65" width="400" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="240" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Sub-Atomic Particle Mechanism</text>

  <g transform="translate(60, 120)">
    <!-- Neutron Box -->
    <rect x="10" y="20" width="100" height="70" fill="#334155" rx="8" stroke="#94a3b8" stroke-width="1"/>
    <text x="60" y="48" fill="#f8fafc" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">¹₀n</text>
    <text x="60" y="70" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Neutron</text>

    <!-- Arrow -->
    <text x="135" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="22" font-weight="bold">→</text>

    <!-- Proton Box -->
    <rect x="160" y="20" width="90" height="70" fill="#1e3a5f" rx="8" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="205" y="48" fill="#38bdf8" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">¹₁p</text>
    <text x="205" y="70" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Proton</text>

    <text x="265" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="18" font-weight="bold">+</text>

    <!-- Beta Particle Box -->
    <rect x="280" y="20" width="80" height="70" fill="#4c1d95" rx="8" stroke="#a855f7" stroke-width="1.5"/>
    <text x="320" y="48" fill="#c084fc" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">⁰₋₁e (β⁻)</text>
    <text x="320" y="70" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Beta Particle</text>
  </g>

  <g transform="translate(60, 230)">
    <rect x="10" y="10" width="340" height="90" fill="#0f172a" rx="8"/>
    <text x="25" y="35" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Conservation Laws during Beta Decay:</text>
    <text x="25" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">1. Mass Number (A): Remains constant (ΔA = 0)</text>
    <text x="25" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">2. Atomic Number (Z): Increases by 1 (Z → Z + 1)</text>
  </g>

  <!-- Right: Worked Nuclear Equations -->
  <rect x="460" y="65" width="400" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="1.5"/>
  <text x="660" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Balanced Beta Decay Examples</text>

  <!-- Example 1: Carbon-14 to Nitrogen-14 -->
  <rect x="480" y="115" width="360" height="95" fill="#0f172a" rx="8" stroke="#334155" stroke-width="1"/>
  <text x="495" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">1. Radiocarbon Beta Decay:</text>
  <text x="495" y="170" fill="#f8fafc" font-family="monospace" font-size="14" font-weight="bold">¹⁴₆C  →  ¹⁴₇N  +  ⁰₋₁e</text>
  <text x="495" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Mass: 14 = 14 + 0 | Charge: 6 = 7 + (-1) ✓</text>

  <!-- Example 2: Thorium-234 to Protactinium-234 -->
  <rect x="480" y="225" width="360" height="95" fill="#0f172a" rx="8" stroke="#334155" stroke-width="1"/>
  <text x="495" y="250" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">2. Heavy Nuclide Decay (Uranium Series):</text>
  <text x="495" y="280" fill="#f8fafc" font-family="monospace" font-size="14" font-weight="bold">²³⁴₉₀Th  →  ²³⁴₉₁Pa  +  ⁰₋₁e</text>
  <text x="495" y="305" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Mass: 234 = 234 + 0 | Charge: 90 = 91 + (-1) ✓</text>

  <!-- Summary Note -->
  <rect x="480" y="335" width="360" height="75" fill="#052e16" rx="8" stroke="#166534" stroke-width="1"/>
  <text x="495" y="360" fill="#86efac" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Rule for Transmutation:</text>
  <text x="495" y="380" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">The daughter nuclide moves ONE place to the RIGHT in</text>
  <text x="495" y="398" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">the Periodic Table due to the +1 proton gain.</text>
</svg>''')

# 2. SVG for Lesson 12 Block 95 (Alpha, Beta, Gamma Radiation Pathways)
RADIATION_PATHWAYS_SVG = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0a0f1d" rx="16"/>
  <text x="450" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Nuclear Radiation: Types, Composition, and Penetration Barriers</text>

  <!-- Left: Radiation Emission Types -->
  <rect x="40" y="65" width="400" height="365" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="240" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Nuclear Emissions from Unstable Nuclei</text>

  <!-- Alpha Particle -->
  <rect x="60" y="115" width="360" height="85" fill="#0f172a" rx="8" stroke="#ef4444" stroke-width="1"/>
  <circle cx="95" cy="157" r="18" fill="#dc2626"/>
  <text x="95" y="163" fill="#ffffff" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">α (⁴₂He)</text>
  <text x="130" y="145" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Alpha Particle (Helium Nucleus)</text>
  <text x="130" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• 2 Protons + 2 Neutrons (Mass = 4, Charge = +2)</text>
  <text x="130" y="185" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">High ionizing power, lowest penetrating power</text>

  <!-- Beta Particle -->
  <rect x="60" y="215" width="360" height="85" fill="#0f172a" rx="8" stroke="#38bdf8" stroke-width="1"/>
  <circle cx="95" cy="257" r="14" fill="#0284c7"/>
  <text x="95" y="262" fill="#ffffff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">β⁻ (⁰₋₁e)</text>
  <text x="130" y="245" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Beta Particle (Fast Electron)</text>
  <text x="130" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High-speed electron (Mass ≈ 1/1840, Charge = -1)</text>
  <text x="130" y="285" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Moderate ionizing power, penetrates paper</text>

  <!-- Gamma Ray -->
  <rect x="60" y="315" width="360" height="95" fill="#0f172a" rx="8" stroke="#a855f7" stroke-width="1"/>
  <path d="M 80 362 Q 95 345 110 362 T 140 362" stroke="#c084fc" stroke-width="3" fill="none"/>
  <text x="95" y="388" fill="#e9d5ff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">γ</text>
  <text x="130" y="342" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Gamma Ray (EM Wave)</text>
  <text x="130" y="362" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High-frequency photons (Mass = 0, Charge = 0)</text>
  <text x="130" y="382" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Lowest ionizing power, extremely high penetration</text>
  <text x="130" y="398" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Requires thick lead / concrete to attenuate</text>

  <!-- Right: Penetrating Power & Barrier Diagram -->
  <rect x="460" y="65" width="400" height="365" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="1.5"/>
  <text x="660" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Penetration Depths Across Materials</text>

  <g transform="translate(480, 120)">
    <!-- Barriers -->
    <!-- Paper -->
    <rect x="100" y="20" width="12" height="230" fill="#f8fafc" rx="2" stroke="#94a3b8"/>
    <text x="106" y="268" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Paper</text>
    <text x="106" y="283" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(0.1 mm)</text>

    <!-- Aluminium -->
    <rect x="200" y="20" width="18" height="230" fill="#94a3b8" rx="2" stroke="#64748b"/>
    <text x="209" y="268" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Aluminium</text>
    <text x="209" y="283" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(5 mm)</text>

    <!-- Lead -->
    <rect x="310" y="20" width="30" height="230" fill="#475569" rx="3" stroke="#334155"/>
    <text x="325" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Lead</text>
    <text x="325" y="283" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(25 mm+)</text>

    <!-- Alpha Beam (Stops at Paper) -->
    <line x1="10" y1="50" x2="100" y2="50" stroke="#ef4444" stroke-width="4"/>
    <polygon points="100,45 110,50 100,55" fill="#ef4444"/>
    <text x="45" y="42" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Alpha (α)</text>
    <text x="125" y="55" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">STOPPED</text>

    <!-- Beta Beam (Passes Paper, Stops at Aluminium) -->
    <line x1="10" y1="120" x2="200" y2="120" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="200,115 210,120 200,125" fill="#38bdf8"/>
    <text x="45" y="112" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Beta (β)</text>
    <text x="235" y="125" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">STOPPED</text>

    <!-- Gamma Beam (Passes Paper and Aluminium, Attenuated in Lead) -->
    <path d="M 10 190 Q 25 180 40 190 T 70 190 T 100 190 T 130 190 T 160 190 T 190 190 T 220 190 T 250 190 T 280 190 T 310 190" stroke="#c084fc" stroke-width="2.5" fill="none"/>
    <text x="45" y="182" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Gamma (γ)</text>
    <text x="260" y="215" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">ATTENUATED IN LEAD</text>
  </g>
</svg>''')

def update_visuals():
    print('Updating missing visual blocks in Topic 7...')

    # 1. Update Block 4026 (Lesson 150)
    try:
        b4026 = LessonBlock.objects.get(id=4026)
        b4026.metadata['svg_content'] = BETA_EQUATIONS_SVG
        b4026.content = {
            'title': 'Writing and Balancing Nuclear Beta (β⁻) Decay Equations',
            'caption': 'Particle-level transmutation showing a neutron converting into a proton and high-speed beta electron with mass and charge conservation.',
            'svg_content': BETA_EQUATIONS_SVG
        }
        b4026.save()

        # Update or create attached asset
        asset = b4026.assets.first()
        if not asset:
            asset = LessonAsset.objects.create(
                lesson_id=150,
                asset_type='diagram',
                source_type='ai_generated',
                storage_type='file',
                title='Writing and Balancing Nuclear Beta Decay Equations',
                description='Sanitized vector diagram illustrating sub-atomic beta emission mechanism and balanced nuclear equations.',
                status='approved'
            )
            asset.blocks.add(b4026)
        asset.metadata = {'svg_content': BETA_EQUATIONS_SVG}
        asset.status = 'approved'
        asset.save()
        print('Updated Block 4026 (Lesson 150) with Beta Decay SVG diagram!')
    except Exception as e:
        print(f'Error updating Block 4026: {e}')

    # 2. Update Block 95 (Lesson 12)
    try:
        b95 = LessonBlock.objects.get(id=95)
        b95.metadata['svg_content'] = RADIATION_PATHWAYS_SVG
        b95.content = {
            'title': 'Alpha, Beta, and Gamma Emissions & Penetration Barriers',
            'caption': 'Comparison of alpha, beta, and gamma emissions showing particle structure, relative ionizing power, and material shielding thresholds.',
            'svg_content': RADIATION_PATHWAYS_SVG
        }
        b95.save()

        asset95 = b95.assets.first()
        if not asset95:
            asset95 = LessonAsset.objects.create(
                lesson_id=12,
                asset_type='diagram',
                source_type='ai_generated',
                storage_type='file',
                title='Alpha, Beta, and Gamma Radiation Penetration',
                description='Sanitized vector diagram: Alpha, Beta, and Gamma emissions and penetration barriers.',
                status='approved'
            )
            asset95.blocks.add(b95)
        asset95.metadata = {'svg_content': RADIATION_PATHWAYS_SVG}
        asset95.status = 'approved'
        asset95.save()
        print('Updated Block 95 (Lesson 12) with Radiation Pathways SVG diagram!')
    except Exception as e:
        print(f'Error updating Block 95: {e}')

if __name__ == '__main__':
    update_visuals()
