import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock, LessonAsset

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" width="100%" height="100%" style="background-color: #0b1120; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="reactorGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="pelletGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569" />
      <stop offset="50%" stop-color="#334155" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="ironGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8" />
      <stop offset="100%" stop-color="#64748b" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Title Header -->
  <rect x="20" y="16" width="880" height="52" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="460" y="44" fill="#38bdf8" font-size="17" font-weight="bold" text-anchor="middle">
    Porous Granular Iron (Fe) Catalyst in the Haber-Bosch Synthesis Reactor
  </text>
  <text x="460" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">
    Fused Magnetite Precursor (Fe₃O₄) Reduced to α-Fe with Al₂O₃ (Structural Promoter) &amp; K₂O (Electronic Promoter)
  </text>

  <!-- LEFT PANEL: Industrial Reactor Catalyst Bed -->
  <g transform="translate(30, 85)">
    <rect width="260" height="425" rx="16" fill="url(#reactorGrad)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="130" y="28" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">
      Haber Synthesis Column
    </text>

    <!-- Inflow Gas Arrow -->
    <path d="M 130 40 L 130 70" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4 2"/>
    <polygon points="126,70 134,70 130,78" fill="#38bdf8"/>
    <text x="130" y="55" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle" dx="55">
      N₂ + 3H₂ (200 atm)
    </text>

    <!-- Bed 1 -->
    <rect x="25" y="85" width="210" height="55" rx="8" fill="#334155" stroke="#64748b" stroke-width="1"/>
    <!-- Catalyst Pellets Pattern in Bed 1 -->
    <g fill="#94a3b8" opacity="0.8">
      <circle cx="45" cy="100" r="5"/><circle cx="65" cy="102" r="6"/><circle cx="85" cy="98" r="5"/><circle cx="105" cy="104" r="6"/>
      <circle cx="125" cy="100" r="5"/><circle cx="145" cy="102" r="6"/><circle cx="165" cy="99" r="5"/><circle cx="185" cy="103" r="6"/><circle cx="205" cy="100" r="5"/>
      <circle cx="55" cy="122" r="6"/><circle cx="75" cy="120" r="5"/><circle cx="95" cy="125" r="6"/><circle cx="115" cy="121" r="5"/>
      <circle cx="135" cy="124" r="6"/><circle cx="155" cy="120" r="5"/><circle cx="175" cy="123" r="6"/><circle cx="195" cy="121" r="5"/>
    </g>
    <text x="130" y="116" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" filter="url(#glow)">
      Porous Iron Bed 1 (450°C)
    </text>

    <!-- Cooling / Gas Flow -->
    <path d="M 130 142 L 130 162" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 2"/>
    <polygon points="127,162 133,162 130,168" fill="#38bdf8"/>

    <!-- Bed 2 -->
    <rect x="25" y="172" width="210" height="55" rx="8" fill="#334155" stroke="#64748b" stroke-width="1"/>
    <g fill="#94a3b8" opacity="0.8">
      <circle cx="45" cy="187" r="5"/><circle cx="65" cy="189" r="6"/><circle cx="85" cy="185" r="5"/><circle cx="105" cy="191" r="6"/>
      <circle cx="125" cy="187" r="5"/><circle cx="145" cy="189" r="6"/><circle cx="165" cy="186" r="5"/><circle cx="185" cy="190" r="6"/><circle cx="205" cy="187" r="5"/>
      <circle cx="55" cy="209" r="6"/><circle cx="75" cy="207" r="5"/><circle cx="95" cy="212" r="6"/><circle cx="115" cy="208" r="5"/>
      <circle cx="135" cy="211" r="6"/><circle cx="155" cy="207" r="5"/><circle cx="175" cy="210" r="6"/><circle cx="195" cy="208" r="5"/>
    </g>
    <text x="130" y="203" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" filter="url(#glow)">
      Porous Iron Bed 2
    </text>

    <!-- Bed 3 -->
    <path d="M 130 229 L 130 249" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 2"/>
    <polygon points="127,249 133,249 130,255" fill="#38bdf8"/>
    <rect x="25" y="259" width="210" height="55" rx="8" fill="#334155" stroke="#64748b" stroke-width="1"/>
    <g fill="#94a3b8" opacity="0.8">
      <circle cx="45" cy="274" r="5"/><circle cx="65" cy="276" r="6"/><circle cx="85" cy="272" r="5"/><circle cx="105" cy="278" r="6"/>
      <circle cx="125" cy="274" r="5"/><circle cx="145" cy="276" r="6"/><circle cx="165" cy="273" r="5"/><circle cx="185" cy="277" r="6"/><circle cx="205" cy="274" r="5"/>
      <circle cx="55" cy="296" r="6"/><circle cx="75" cy="294" r="5"/><circle cx="95" cy="299" r="6"/><circle cx="115" cy="295" r="5"/>
      <circle cx="135" cy="298" r="6"/><circle cx="155" cy="294" r="5"/><circle cx="175" cy="297" r="6"/><circle cx="195" cy="295" r="5"/>
    </g>
    <text x="130" y="290" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" filter="url(#glow)">
      Porous Iron Bed 3
    </text>

    <!-- Outflow Arrow -->
    <path d="M 130 318 L 130 365" stroke="#4ade80" stroke-width="3"/>
    <polygon points="126,365 134,365 130,373" fill="#4ade80"/>
    <text x="130" y="398" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">
      Effluent: NH₃ + N₂ + H₂
    </text>
    <text x="130" y="413" fill="#94a3b8" font-size="9" text-anchor="middle">
      Yield ~15% per pass (Recycled)
    </text>
  </g>

  <!-- RIGHT PANEL: Microscopic Pellet Anatomy & Surface Chemisorption Mechanism -->
  <g transform="translate(310, 85)">
    <!-- Pellet Cross-Section -->
    <rect width="580" height="200" rx="16" fill="url(#reactorGrad)" stroke="#64748b" stroke-width="1.5"/>
    <text x="290" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">
      Magnified Porous Catalyst Pellet Microstructure (6–10 mm Grain)
    </text>

    <!-- Pellet Graphic -->
    <g transform="translate(30, 45)">
      <!-- Porous Granular Grain Shape -->
      <polygon points="15,40 45,15 105,10 135,35 140,85 110,120 40,125 10,80" fill="url(#pelletGrad)" stroke="#94a3b8" stroke-width="2"/>
      <!-- Inner Pores & Pockets -->
      <path d="M 40 40 Q 60 55 50 80 Q 70 70 90 85 Q 110 50 120 65" stroke="#0f172a" stroke-width="6" fill="none" stroke-linecap="round"/>
      <path d="M 30 75 Q 50 90 75 100 Q 100 110 120 100" stroke="#0f172a" stroke-width="5" fill="none" stroke-linecap="round"/>
      <!-- Promoters Callout -->
      <circle cx="55" cy="50" r="4" fill="#fbbf24"/>
      <circle cx="95" cy="70" r="4" fill="#a855f7"/>
      <circle cx="80" cy="95" r="4" fill="#fbbf24"/>
      <circle cx="115" cy="85" r="4" fill="#a855f7"/>
    </g>

    <!-- Composition & Roles Legend -->
    <g transform="translate(195, 45)" font-size="11">
      <rect width="360" height="135" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <!-- Component 1: alpha-Fe -->
      <circle cx="20" cy="25" r="5" fill="#94a3b8"/>
      <text x="35" y="29" fill="#f8fafc" font-weight="bold">Active Phase: Reduced α-Iron Crystallites (Fe)</text>
      <text x="35" y="44" fill="#94a3b8" font-size="10">Provides transition-metal d-orbitals to bind and dissociate N₂ and H₂.</text>

      <!-- Component 2: Al2O3 -->
      <circle cx="20" cy="65" r="5" fill="#fbbf24"/>
      <text x="35" y="69" fill="#fbbf24" font-weight="bold">Structural Promoter: Alumina (Al₂O₃ ~2.5%)</text>
      <text x="35" y="84" fill="#94a3b8" font-size="10">Prevents iron grain sintering; preserves extensive internal pore surface area.</text>

      <!-- Component 3: K2O -->
      <circle cx="20" cy="105" r="5" fill="#a855f7"/>
      <text x="35" y="109" fill="#c084fc" font-weight="bold">Electronic Promoter: Potassium Oxide (K₂O ~0.8%)</text>
      <text x="35" y="124" fill="#94a3b8" font-size="10">Donates electron density to Fe, drastically accelerating N≡N bond cleavage.</text>
    </g>

    <!-- LOWER RIGHT: 4-Step Catalytic Surface Mechanism -->
    <g transform="translate(0, 215)">
      <rect width="580" height="210" rx="16" fill="url(#reactorGrad)" stroke="#64748b" stroke-width="1.5"/>
      <text x="290" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">
        Stepwise Heterogeneous Catalytic Mechanism on Fe Active Sites
      </text>

      <!-- Step 1 -->
      <g transform="translate(15, 42)">
        <rect width="125" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
        <text x="62" y="20" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">1. Chemisorption</text>
        <!-- Gas molecules floating down to Fe surface -->
        <circle cx="45" cy="45" r="6" fill="#38bdf8"/><circle cx="57" cy="45" r="6" fill="#38bdf8"/>
        <text x="51" y="48" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">N≡N</text>
        <circle cx="85" cy="55" r="4" fill="#f8fafc"/><circle cx="93" cy="55" r="4" fill="#f8fafc"/>
        <text x="89" y="58" fill="#0f172a" font-size="6" font-weight="bold" text-anchor="middle">H₂</text>
        <!-- Fe Surface Base -->
        <rect x="10" y="115" width="105" height="25" rx="4" fill="#475569"/>
        <text x="62" y="132" fill="#e2e8f0" font-size="10" font-weight="bold" text-anchor="middle">Fe Surface</text>
        <text x="62" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">Gas diffusion into</text>
        <text x="62" y="107" fill="#94a3b8" font-size="9" text-anchor="middle">iron pores</text>
      </g>

      <!-- Step 2 -->
      <g transform="translate(155, 42)">
        <rect width="125" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
        <text x="62" y="20" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">2. Bond Cleavage</text>
        <circle cx="42" cy="105" r="6" fill="#38bdf8"/>
        <text x="42" y="108" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">N</text>
        <circle cx="82" cy="105" r="6" fill="#38bdf8"/>
        <text x="82" y="108" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">N</text>
        <!-- Rate Determining Step Badge -->
        <rect x="15" y="40" width="95" height="20" rx="4" fill="#78350f" stroke="#d97706" stroke-width="1"/>
        <text x="62" y="53" fill="#fef3c7" font-size="8" font-weight="bold" text-anchor="middle">Rate-Limiting Step</text>
        <text x="62" y="80" fill="#bae6fd" font-size="9" text-anchor="middle">N≡N triple bond</text>
        <text x="62" y="92" fill="#bae6fd" font-size="9" text-anchor="middle">dissociates into N(ads)</text>
        <!-- Fe Surface Base -->
        <rect x="10" y="115" width="105" height="25" rx="4" fill="#475569"/>
        <text x="62" y="132" fill="#e2e8f0" font-size="10" font-weight="bold" text-anchor="middle">Fe Surface</text>
      </g>

      <!-- Step 3 -->
      <g transform="translate(295, 42)">
        <rect width="125" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
        <text x="62" y="20" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle">3. Hydrogenation</text>
        <!-- Intermediates NH and NH2 -->
        <circle cx="62" cy="98" r="6" fill="#38bdf8"/>
        <circle cx="56" cy="90" r="3.5" fill="#f8fafc"/>
        <circle cx="68" cy="90" r="3.5" fill="#f8fafc"/>
        <text x="62" y="50" fill="#c084fc" font-size="9" font-weight="bold" text-anchor="middle">Stepwise Addition:</text>
        <text x="62" y="66" fill="#94a3b8" font-size="8.5" text-anchor="middle">N + H → NH</text>
        <text x="62" y="78" fill="#94a3b8" font-size="8.5" text-anchor="middle">NH + H → NH₂</text>
        <text x="62" y="90" fill="#94a3b8" font-size="8.5" text-anchor="middle">NH₂ + H → NH₃</text>
        <!-- Fe Surface Base -->
        <rect x="10" y="115" width="105" height="25" rx="4" fill="#475569"/>
        <text x="62" y="132" fill="#e2e8f0" font-size="10" font-weight="bold" text-anchor="middle">Fe Surface</text>
      </g>

      <!-- Step 4 -->
      <g transform="translate(435, 42)">
        <rect width="130" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
        <text x="65" y="20" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">4. Desorption</text>
        <!-- NH3 molecule rising away -->
        <g transform="translate(45, 50)">
          <circle cx="20" cy="15" r="7" fill="#38bdf8"/>
          <circle cx="12" cy="7" r="4" fill="#f8fafc"/>
          <circle cx="28" cy="7" r="4" fill="#f8fafc"/>
          <circle cx="20" cy="25" r="4" fill="#f8fafc"/>
          <text x="20" y="18" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">N</text>
        </g>
        <path d="M 65 95 L 65 75" stroke="#4ade80" stroke-width="2"/>
        <polygon points="62,75 68,75 65,68" fill="#4ade80"/>
        <text x="65" y="108" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">NH₃(g) Leaves</text>
        <!-- Fe Surface Base -->
        <rect x="10" y="115" width="110" height="25" rx="4" fill="#475569"/>
        <text x="65" y="132" fill="#e2e8f0" font-size="9.5" font-weight="bold" text-anchor="middle">Active Site Free</text>
      </g>
    </g>
  </g>
</svg>"""

# 1. Update Block 5868 in Lesson 75
b5868 = LessonBlock.objects.get(id=5868)
b5868.title = "Porous Granular Iron (Fe) Catalyst Bed and Microstructure in Haber Reactor"
b5868.page_title = "Porous Granular Iron Catalyst"
b5868.block_type = "suggested_diagram"
b5868.component_type = "suggested_diagram"
b5868.content = {
    'svg': svg_content,
    'text': (
        "**Porous Granular Iron Catalyst Bed with Promoters:**\n"
        "In the industrial Haber-Bosch process, fused magnetite ($\\text{Fe}_3\\text{O}_4$) is reduced by hydrogen into **porous $\\alpha$-iron grains**.\n"
        "* **Porous Texture:** Maximizes internal surface area, exposing billions of active iron metal sites.\n"
        "* **Alumina ($\\text{Al}_2\\text{O}_3$ Promoter):** Structural promoter that prevents iron crystallites from sintering (fusing) at high operating temperatures ($450^\\circ\\text{C}$).\n"
        "* **Potassium Oxide ($\\text{K}_2\\text{O}$ Promoter):** Electronic promoter that increases electron density on iron, drastically accelerating the cleavage of the strong $\\text{N}\\equiv\\text{N}$ triple bond ($945\\text{ kJ/mol}$)."
    )
}
b5868.save()
print(f"Updated LessonBlock [{b5868.id}] with accurate Porous Iron Catalyst SVG.")

# 2. Update LessonAsset 346
asset = LessonAsset.objects.get(id=346)
asset.asset_type = 'diagram'
asset.title = "Porous Granular Iron (Fe) Catalyst Bed and Microstructure in Haber Reactor"
asset.url = ''
asset.content = {'svg': svg_content}
asset.metadata = {
    'promoters': ['Al2O3', 'K2O'],
    'temperature_c': 450,
    'pressure_atm': 200,
    'active_phase': 'alpha-Fe'
}
asset.save()
print(f"Updated LessonAsset [{asset.id}].")
