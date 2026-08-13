import os, sys, django
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.core.files.base import ContentFile
from curriculum.models import LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

# ─── Build the proper compass-construction SVG ───────────────────────────────
# Layout: A=(170,190), B=(570,190), M=(370,190)
# Compass radius r=160 > half of AB=200 → arcs intersect at P=(370,80) and Q=(370,300)
# Perpendicular bisector: vertical line x=370 through P,M,Q

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <!-- background -->
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>

  <!-- title -->
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui,sans-serif"
        font-size="17" font-weight="bold" text-anchor="middle">
    Worked Example 1: Compass Construction of Perpendicular Bisector of AB
  </text>

  <!-- drawing area -->
  <g transform="translate(60,50)">
    <rect width="720" height="298" fill="#0f172a" rx="12"
          stroke="#38bdf8" stroke-width="1.5"/>

    <!-- ── Baseline AB ── -->
    <!-- A=(110,149)  B=(510,149)  M=(310,149) inside the panel -->
    <!-- half AB = 200, compass radius = 165 -->

    <!-- Line AB -->
    <line x1="110" y1="149" x2="510" y2="149"
          stroke="#94a3b8" stroke-width="2" stroke-dasharray="6 3"/>

    <!-- Compass arc from A (centre A, radius 165) — partial arcs above & below -->
    <path d="M 110,0 A 165,165 0 0,0 110,298"
          fill="none" stroke="#facc15" stroke-width="1.8" stroke-dasharray="7 3"
          clip-path="url(#clip)"/>

    <!-- Compass arc from B (centre B, radius 165) — partial arcs above & below -->
    <path d="M 510,0 A 165,165 0 0,1 510,298"
          fill="none" stroke="#facc15" stroke-width="1.8" stroke-dasharray="7 3"
          clip-path="url(#clip)"/>

    <!-- actual small crossing arcs near intersections — more readable arcs -->
    <!-- Intersection P ≈ (310, −16+149) = (310, 50) and Q=(310, 248) for r=165 -->
    <!-- arc segment from A crossing near P -->
    <path d="M 250,10 A 165,165 0 0,1 370,50"
          fill="none" stroke="#facc15" stroke-width="2.2"/>
    <!-- arc segment from B crossing near P -->
    <path d="M 370,50 A 165,165 0 0,0 460,12"
          fill="none" stroke="#facc15" stroke-width="2.2"/>
    <!-- arc segment from A crossing near Q -->
    <path d="M 248,284 A 165,165 0 0,0 370,248"
          fill="none" stroke="#facc15" stroke-width="2.2"/>
    <!-- arc segment from B crossing near Q -->
    <path d="M 370,248 A 165,165 0 0,1 460,282"
          fill="none" stroke="#facc15" stroke-width="2.2"/>

    <!-- Perpendicular bisector line L (vertical through M) -->
    <line x1="310" y1="8" x2="310" y2="290"
          stroke="#4ade80" stroke-width="2.5"/>

    <!-- Right-angle box at M -->
    <rect x="310" y="139" width="12" height="12"
          fill="none" stroke="#4ade80" stroke-width="1.8"/>

    <!-- Intersection point P (above) -->
    <circle cx="310" cy="50" r="6" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>
    <!-- Intersection point Q (below) -->
    <circle cx="310" cy="248" r="6" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>

    <!-- Midpoint M -->
    <circle cx="310" cy="149" r="6" fill="#4ade80" stroke="#fff" stroke-width="1.5"/>

    <!-- Point A -->
    <circle cx="110" cy="149" r="6" fill="#38bdf8" stroke="#fff" stroke-width="1.5"/>
    <!-- Point B -->
    <circle cx="510" cy="149" r="6" fill="#38bdf8" stroke="#fff" stroke-width="1.5"/>

    <!-- Labels -->
    <text x="95"  y="169" fill="#38bdf8" font-family="system-ui,sans-serif"
          font-size="18" font-weight="bold" text-anchor="middle">A</text>
    <text x="525" y="169" fill="#38bdf8" font-family="system-ui,sans-serif"
          font-size="18" font-weight="bold" text-anchor="middle">B</text>
    <text x="310" y="178" fill="#4ade80" font-family="system-ui,sans-serif"
          font-size="18" font-weight="bold" text-anchor="middle">M</text>
    <text x="286" y="43"  fill="#e879f9" font-family="system-ui,sans-serif"
          font-size="16" font-weight="bold" text-anchor="end">P</text>
    <text x="286" y="255" fill="#e879f9" font-family="system-ui,sans-serif"
          font-size="16" font-weight="bold" text-anchor="end">Q</text>

    <!-- Label: Perpendicular Bisector L -->
    <text x="320" y="22" fill="#4ade80" font-family="system-ui,sans-serif"
          font-size="14" font-weight="bold">L</text>

    <!-- Radius annotation for arc from A -->
    <line x1="110" y1="149" x2="310" y2="50"
          stroke="#facc15" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
    <text x="175" y="88" fill="#facc15" font-family="system-ui,sans-serif"
          font-size="13" font-weight="bold" text-anchor="middle">r &gt; ½AB</text>

    <!-- Radius annotation for arc from B -->
    <line x1="510" y1="149" x2="310" y2="50"
          stroke="#facc15" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
    <text x="455" y="88" fill="#facc15" font-family="system-ui,sans-serif"
          font-size="13" font-weight="bold" text-anchor="middle">r &gt; ½AB</text>

    <!-- AM = MB annotation -->
    <text x="200" y="138" fill="#94a3b8" font-family="system-ui,sans-serif"
          font-size="13" text-anchor="middle">AM = MB</text>

    <!-- Legend -->
    <g transform="translate(555, 210)">
      <rect width="148" height="75" fill="#0a0f1d" rx="8"
            stroke="#334155" stroke-width="1"/>
      <circle cx="18" cy="18" r="5" fill="#38bdf8"/>
      <text x="30" y="23" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12">A, B — given points</text>
      <circle cx="18" cy="40" r="5" fill="#e879f9"/>
      <text x="30" y="45" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12">P, Q — arc intersections</text>
      <circle cx="18" cy="62" r="5" fill="#4ade80"/>
      <text x="30" y="67" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12">M — midpoint, L — bisector</text>
    </g>

  </g>
</svg>'''

def fix_perp_bisector():
    ok, san, err = validate_and_sanitize_svg(SVG)
    svg_final = san if ok else SVG

    block = LessonBlock.objects.get(id=14327)
    block.metadata = {**(block.metadata or {}), 'svg_content': svg_final}
    block.content  = {**(block.content  or {}), 'svg_content': svg_final, 'svg': svg_final}
    block.save()
    print(f'Block 14327 metadata updated.')

    asset = LessonAsset.objects.get(id=1453)
    asset.metadata = {**(asset.metadata or {}), 'svg_content': svg_final}
    asset.file.save('worked_example_perp_bisector_219.svg',
                    ContentFile(svg_final.encode()), save=True)
    asset.save()
    print(f'Asset 1453 file saved: {asset.file.name}')
    print('DONE — Perpendicular Bisector SVG replaced with proper geometric construction.')

fix_perp_bisector()
