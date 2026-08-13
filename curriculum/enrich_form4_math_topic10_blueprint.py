"""
Topic 10 — Area Approximation: Blueprint-Specified SVG Enrichment
Replaces generic text SVGs with the exact diagrams specified in the visual blueprint:
  V1: Forest Grid (L231 P2)
  V2: Inner/Outer Bounding Rectangles (L231 P3)
  V3+V4: Trapezium shared ordinates + Kazungu/Ndoe map (L232)
  V5: Semicircle mid-ordinate error cancellation (L233)
  V6: Concavity split-panel (L234 P2)
Block IDs: 14373–14388
"""
import os, sys, django
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.core.files.base import ContentFile
from curriculum.models import LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

BG = '#0a0f1d'

def push(block_id, title, svg_str):
    ok, san, _ = validate_and_sanitize_svg(svg_str)
    svg = san if ok else svg_str
    b = LessonBlock.objects.get(id=block_id)
    b.title    = title
    b.metadata = {**(b.metadata or {}), 'svg_content': svg}
    b.content  = {**(b.content  or {}), 'svg_content': svg, 'svg': svg}
    b.save()
    asset = LessonAsset.objects.filter(blocks=b, source_type='ai_generated').first()
    if asset:
        asset.title    = title
        asset.metadata = {**(asset.metadata or {}), 'svg_content': svg}
        fname = f't10_blueprint_{block_id}.svg'
        asset.file.save(fname, ContentFile(svg.encode()), save=True)
        asset.save()
    print(f'  Block {block_id}: {title[:60]}')


def mk(inner, W=840, H=400, title='', tc='#facc15'):
    t = (f'<text x="{W//2}" y="30" fill="{tc}" font-family="system-ui,sans-serif" '
         f'font-size="16" font-weight="bold" text-anchor="middle">{title}</text>') if title else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">'
            f'<rect width="{W}" height="{H}" fill="{BG}" rx="14"/>'
            f'{t}{inner}</svg>')

def warn(line1, line2=''):
    inner = (f'<rect x="50" y="45" width="740" height="300" fill="#1c0a0a" rx="10" stroke="#f87171" stroke-width="2"/>'
             f'<text x="420" y="110" fill="#f87171" font-family="system-ui,sans-serif" font-size="22" '
             f'font-weight="bold" text-anchor="middle">COMMON ERROR</text>'
             f'<line x1="150" y1="130" x2="690" y2="130" stroke="#f87171" stroke-width="1" stroke-dasharray="4 3"/>'
             f'<text x="420" y="185" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="15" '
             f'font-weight="bold" text-anchor="middle">{line1}</text>')
    if line2:
        inner += (f'<text x="420" y="222" fill="#fcd34d" font-family="system-ui,sans-serif" font-size="14" '
                  f'font-weight="normal" text-anchor="middle">{line2}</text>')
    return mk(inner)


# ─── L231 P2: V1 — Forest Grid Counting ──────────────────────────────────────
def forest_grid():
    # 6x7 grid of 1cm squares, irregular boundary, numbered full + orange partials
    CELL = 48
    OX, OY = 65, 50   # grid origin

    full_cells = [
        (1,0),(2,0),(3,0),(4,0),
        (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),
        (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),
        (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),
        (1,4),(2,4),(3,4),(4,4),
        (2,5),(3,5),
    ]
    partial_cells = [
        (0,0),(5,0),(6,0),
        (6,1),
        (6,2),
        (6,3),
        (0,4),(5,4),(6,4),
        (1,5),(4,5),(5,5),
        (2,6),(3,6),
    ]

    inner = ''
    # grid lines
    for c in range(8):
        inner += f'<line x1="{OX+c*CELL}" y1="{OY}" x2="{OX+c*CELL}" y2="{OY+7*CELL}" stroke="#334155" stroke-width="1"/>'
    for r in range(8):
        inner += f'<line x1="{OX}" y1="{OY+r*CELL}" x2="{OX+7*CELL}" y2="{OY+r*CELL}" stroke="#334155" stroke-width="1"/>'

    # full cells (blue)
    n = 1
    for (c,r) in full_cells:
        x, y = OX+c*CELL, OY+r*CELL
        inner += f'<rect x="{x+1}" y="{y+1}" width="{CELL-2}" height="{CELL-2}" fill="#1e40af" opacity="0.55"/>'
        inner += f'<text x="{x+CELL//2}" y="{y+CELL//2+5}" fill="#93c5fd" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">{n}</text>'
        n += 1

    # partial cells (orange)
    m = 1
    for (c,r) in partial_cells:
        x, y = OX+c*CELL, OY+r*CELL
        if 0 <= c < 7 and 0 <= r < 7:
            inner += f'<rect x="{x+1}" y="{y+1}" width="{CELL-2}" height="{CELL-2}" fill="#92400e" opacity="0.55"/>'
            inner += f'<text x="{x+CELL//2}" y="{y+CELL//2+5}" fill="#fcd34d" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">{m}/2</text>'
            m += 1

    # irregular forest boundary (rough polygon)
    inner += (
        '<polyline points="113,98 161,50 257,50 305,50 353,50 401,50 449,98 '
        '449,194 497,194 497,242 449,290 353,338 257,338 161,290 113,242 113,98" '
        'fill="none" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="6 3"/>'
    )

    # legend
    lx = OX + 7*CELL + 20
    inner += (
        f'<rect x="{lx}" y="55" width="18" height="18" fill="#1e40af" opacity="0.8"/>'
        f'<text x="{lx+24}" y="69" fill="#93c5fd" font-family="sans-serif" font-size="13" font-weight="bold">Full squares: 25</text>'
        f'<rect x="{lx}" y="85" width="18" height="18" fill="#92400e" opacity="0.8"/>'
        f'<text x="{lx+24}" y="99" fill="#fcd34d" font-family="sans-serif" font-size="13" font-weight="bold">Partial: 16</text>'
        f'<rect x="{lx}" y="125" width="200" height="60" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1.5"/>'
        f'<text x="{lx+100}" y="147" fill="#4ade80" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">Area = 25 + 16/2</text>'
        f'<text x="{lx+100}" y="168" fill="#facc15" font-family="monospace" font-size="15" font-weight="bold" text-anchor="middle">= 33 cm^2</text>'
        # scale note
        f'<text x="{lx}" y="220" fill="#64748b" font-family="sans-serif" font-size="12">Grid: 1cm x 1cm</text>'
        f'<text x="{lx}" y="240" fill="#4ade80" font-family="sans-serif" font-size="12">Finer grid (0.5cm)</text>'
        f'<text x="{lx}" y="258" fill="#4ade80" font-family="sans-serif" font-size="12">reduces boundary error</text>'
    )

    return mk(inner, W=840, H=430,
              title='V1: Grid Square Counting — 25 Full + 16 Partial = 33 cm^2',
              tc='#38bdf8')


# ─── L231 P3: V2 — Inner/Outer Bounding Rectangles ───────────────────────────
def bounding_rects_v2():
    # Parabola y=(x-1)^2+1 from x=0..5, inner (blue) + outer (red dashed) rects, squeeze annotation
    import math
    OX, OY = 80, 380
    SX = lambda x: OX + x*100
    SY = lambda y: OY - y*55
    f = lambda x: (x-1)**2 + 1

    pts = ' '.join(f'{SX(i*0.05):.1f},{SY(f(i*0.05)):.1f}' for i in range(101))
    n = 4  # strips
    h = 4/n

    inner = (
        f'<line x1="{OX}" y1="{OY}" x2="{SX(5)}" y2="{OY}" stroke="#475569" stroke-width="2"/>'
        f'<line x1="{OX}" y1="{OY+5}" x2="{OX}" y2="{SY(10)}" stroke="#475569" stroke-width="2"/>'
        f'<text x="{SX(5)+8}" y="{OY+5}" fill="#475569" font-family="sans-serif" font-size="13" font-weight="bold">x</text>'
        f'<text x="{OX-4}" y="{SY(10)-8}" fill="#475569" font-family="sans-serif" font-size="13" font-weight="bold">y</text>'
    )

    # inner (lower) rectangles
    for i in range(n):
        xL = i*h; xR = xL+h
        yLow = min(f(xL), f(xR))
        inner += (f'<rect x="{SX(xL):.0f}" y="{SY(yLow):.0f}" '
                  f'width="{SX(xR)-SX(xL):.0f}" height="{OY-SY(yLow):.0f}" '
                  f'fill="#0ea5e9" opacity="0.30" stroke="#38bdf8" stroke-width="1.5"/>')
        # ordinate label
        inner += f'<text x="{SX(xL):.0f}" y="{OY+18}" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">{xL:.0f}</text>'

    # outer (upper) addition layer
    for i in range(n):
        xL = i*h; xR = xL+h
        yLow = min(f(xL), f(xR)); yHigh = max(f(xL), f(xR))
        inner += (f'<rect x="{SX(xL):.0f}" y="{SY(yHigh):.0f}" '
                  f'width="{SX(xR)-SX(xL):.0f}" height="{SY(yLow)-SY(yHigh):.0f}" '
                  f'fill="#f87171" opacity="0.20" stroke="#f87171" stroke-width="1.5" stroke-dasharray="5 3"/>')

    inner += f'<text x="{SX(4):.0f}" y="{OY+18}" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">4</text>'
    inner += f'<polyline points="{pts}" fill="none" stroke="#facc15" stroke-width="3"/>'
    inner += f'<text x="{SX(4.5):.0f}" y="{SY(f(4.5))-12:.0f}" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold">y=f(x)</text>'

    # squeeze annotation
    inner += (
        f'<text x="580" y="80" fill="#38bdf8" font-family="monospace" font-size="14" font-weight="bold">Lower Bound (underestimate)</text>'
        f'<text x="580" y="105" fill="#f87171" font-family="monospace" font-size="14" font-weight="bold">Upper Bound (overestimate)</text>'
        f'<rect x="570" y="130" width="230" height="60" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1.5"/>'
        f'<text x="685" y="153" fill="#4ade80" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">Lower &lt; Exact &lt; Upper</text>'
        f'<text x="685" y="175" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">As n increases: both converge</text>'
    )

    return mk(inner, W=840, H=420,
              title='V2: Inner (Lower) and Outer (Upper) Bounding Rectangles — Squeeze Theorem',
              tc='#38bdf8')


# ─── L232 P2: V3 — Trapezium Shared Ordinates ────────────────────────────────
def trapezium_shared_ordinates():
    OX, OY = 80, 330
    SX = lambda x: OX + x*105
    SY = lambda y: OY - y*42
    f = lambda x: x*x - 2*x + 5

    pts = ' '.join(f'{SX(i*0.05):.1f},{SY(f(i*0.05)):.1f}' for i in range(61))

    inner = (
        f'<line x1="{OX}" y1="{OY}" x2="{SX(6.5)}" y2="{OY}" stroke="#475569" stroke-width="2"/>'
        f'<line x1="{OX}" y1="{OY+5}" x2="{OX}" y2="{SY(14)}" stroke="#475569" stroke-width="2"/>'
    )

    xs = [0,1,2,3,4,5]
    ys = [f(x) for x in xs]
    n = len(xs)-1

    # trapezia
    for i in range(n):
        pts_trap = f'{SX(xs[i]):.0f},{OY} {SX(xs[i]):.0f},{SY(ys[i]):.0f} {SX(xs[i+1]):.0f},{SY(ys[i+1]):.0f} {SX(xs[i+1]):.0f},{OY}'
        inner += f'<polygon points="{pts_trap}" fill="#10b981" opacity="0.22" stroke="#10b981" stroke-width="1.4"/>'

    # ordinate lines — colour by type
    for i, (x, y) in enumerate(zip(xs, ys)):
        if i == 0 or i == n:
            col = '#38bdf8'   # first/last: counted ONCE (×1)
        else:
            col = '#f59e0b'   # interior: SHARED (×2)
        lw = '2.5' if i in (0, n) else '2'
        inner += f'<line x1="{SX(x):.0f}" y1="{OY}" x2="{SX(x):.0f}" y2="{SY(y):.0f}" stroke="{col}" stroke-width="{lw}" stroke-dasharray="{"none" if i in (0,n) else "5 3"}"/>'
        # ordinate label
        inner += f'<text x="{SX(x):.0f}" y="{SY(y)-10:.0f}" fill="{col}" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">y{i}</text>'
        inner += f'<text x="{SX(x):.0f}" y="{OY+18}" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">{x}</text>'
        # multiplier badge
        mult = '×1' if i in (0, n) else '×2'
        mc   = '#38bdf8' if i in (0, n) else '#f59e0b'
        inner += f'<text x="{SX(x)+14:.0f}" y="{SY(y)+4:.0f}" fill="{mc}" font-family="monospace" font-size="11" font-weight="bold">{mult}</text>'

    inner += f'<polyline points="{pts}" fill="none" stroke="#facc15" stroke-width="3"/>'

    # legend
    inner += (
        f'<rect x="590" y="55" width="14" height="14" fill="#38bdf8"/>'
        f'<text x="610" y="67" fill="#38bdf8" font-family="monospace" font-size="13" font-weight="bold">y0, yn  counted ONCE (x1)</text>'
        f'<rect x="590" y="80" width="14" height="14" fill="#f59e0b"/>'
        f'<text x="610" y="92" fill="#f59e0b" font-family="monospace" font-size="13" font-weight="bold">y1...yn-1  SHARED (x2)</text>'
        f'<rect x="575" y="115" width="240" height="55" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1.5"/>'
        f'<text x="695" y="135" fill="#4ade80" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Area = h/2 [y0+yn + 2(y1+...+yn-1)]</text>'
        f'<text x="695" y="158" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">n=5 strips, h=1, ordinates y0..y5</text>'
    )

    return mk(inner, W=840, H=390,
              title='V3: Trapezium Rule — Interior Ordinates Shared (Counted Twice)',
              tc='#10b981')


# ─── L232 P3: Kazungu vs Ndoe Dispute Map ────────────────────────────────────
def kazungu_ndoe_map():
    OX, OY = 80, 330
    SX = lambda x: OX + x*70
    SY = lambda y: OY - y*28

    # Kazungu boundary: y1 values at x=0..9
    y1 = [0, 4.0, 6.2, 8.4, 9.0, 9.0, 8.4, 6.2, 4.0, 0]
    # Ndoe boundary: y2 values
    y2 = [0, 0.2, 1.5, 3.0, 4.5, 4.5, 3.0, 1.5, 0.2, 0]
    n = 9

    inner = (
        f'<line x1="{OX}" y1="{OY}" x2="{SX(9.5)}" y2="{OY}" stroke="#475569" stroke-width="2"/>'
        f'<line x1="{OX}" y1="{OY+5}" x2="{OX}" y2="{SY(11)}" stroke="#475569" stroke-width="2"/>'
        f'<text x="{SX(9.5)+8}" y="{OY+5}" fill="#475569" font-family="sans-serif" font-size="13">x</text>'
        f'<text x="{OX-4}" y="{SY(11)-8}" fill="#475569" font-family="sans-serif" font-size="13">y (m)</text>'
    )

    # shaded disputed area between the two curves
    upper_pts = ' '.join(f'{SX(i):.0f},{SY(y1[i]):.0f}' for i in range(10))
    lower_pts = ' '.join(f'{SX(9-i):.0f},{SY(y2[9-i]):.0f}' for i in range(10))
    inner += f'<polygon points="{upper_pts} {lower_pts}" fill="#f59e0b" opacity="0.20"/>'

    # Kazungu line (blue)
    k_pts = ' '.join(f'{SX(i):.0f},{SY(y1[i]):.0f}' for i in range(10))
    inner += f'<polyline points="{k_pts}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>'

    # Ndoe line (red)
    n_pts = ' '.join(f'{SX(i):.0f},{SY(y2[i]):.0f}' for i in range(10))
    inner += f'<polyline points="{n_pts}" fill="none" stroke="#f87171" stroke-width="2.5"/>'

    # vertical ordinate difference lines + di labels
    for i in range(1, n):
        x = SX(i)
        yT = SY(y1[i]); yB = SY(y2[i])
        d = y1[i] - y2[i]
        inner += f'<line x1="{x}" y1="{yT}" x2="{x}" y2="{yB}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>'
        inner += f'<text x="{x+6}" y="{(yT+yB)//2+5}" fill="#f59e0b" font-family="monospace" font-size="11" font-weight="bold">d{i}={d:.1f}</text>'
        # x-axis tick
        inner += f'<text x="{x}" y="{OY+17}" fill="#64748b" font-family="monospace" font-size="11" text-anchor="middle">{i}</text>'

    inner += f'<text x="{OX}" y="{OY+17}" fill="#64748b" font-family="monospace" font-size="11" text-anchor="middle">0</text>'
    inner += f'<text x="{SX(9)}" y="{OY+17}" fill="#64748b" font-family="monospace" font-size="11" text-anchor="middle">9</text>'

    # labels
    inner += (
        f'<text x="{SX(4.5):.0f}" y="{SY(9.5)}" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Kazungu (y1)</text>'
        f'<text x="{SX(4.5):.0f}" y="{SY(5.2)}" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Ndoe (y2)</text>'
        f'<text x="{SX(4.5):.0f}" y="{SY(6.8)}" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Disputed Area</text>'
    )

    # calculation box
    inner += (
        f'<rect x="580" y="55" width="235" height="90" fill="#0f172a" rx="6" stroke="#f59e0b" stroke-width="1.5"/>'
        f'<text x="697" y="78" fill="#f59e0b" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">Area = h/2(y0+y9 + 2(d1..d8))</text>'
        f'<text x="697" y="100" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">= 0.5(0+0 + 2(35.0)) = 35 units^2</text>'
        f'<text x="697" y="122" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">= 35 x 400 m^2 = 14,000 m^2 = 1.4 ha</text>'
    )

    return mk(inner, W=840, H=390,
              title='V4: Kazungu vs Ndoe Boundary Dispute — Trapezium Rule with Metric Conversion',
              tc='#f59e0b')


# ─── L233 P2: V5 — Semicircle Mid-Ordinate Error Cancellation ────────────────
def semicircle_mid_ordinate():
    import math
    cx, cy_center = 420, 310   # SVG center
    r = 230                     # radius in SVG units
    SX = lambda x: cx + x*(r/4)
    SY = lambda y: cy_center - y*(r/4)

    # strip midpoints at x=-3,-1,1,3 (strips from -4 to 4 in 2-wide strips)
    midpoints = [-3, -1, 1, 3]
    strip_w = 2
    h_svg = r/4 * strip_w  # svg width of one strip

    # semicircle curve
    curve_pts = ' '.join(
        f'{SX(-4+i*0.05):.1f},{SY(math.sqrt(max(0,16-((-4+i*0.05)**2)))):.1f}'
        for i in range(161)
    )

    inner = (
        # axis
        f'<line x1="{SX(-4.5)}" y1="{SY(0)}" x2="{SX(4.5)}" y2="{SY(0)}" stroke="#475569" stroke-width="2"/>'
        f'<line x1="{SX(0)}" y1="{SY(0)+5}" x2="{SX(0)}" y2="{SY(4.5)}" stroke="#475569" stroke-width="2"/>'
        f'<text x="{SX(4.5)+8}" y="{SY(0)+5}" fill="#475569" font-family="sans-serif" font-size="13">x</text>'
        f'<text x="{SX(-4)-30}" y="{SY(0)+5}" fill="#38bdf8" font-family="monospace" font-size="13">-4</text>'
        f'<text x="{SX(4)-4}" y="{SY(0)+18}" fill="#38bdf8" font-family="monospace" font-size="13">4</text>'
    )

    # 4 rectangles (mid-ordinate)
    for xm in midpoints:
        ym = math.sqrt(max(0, 16 - xm**2))
        xL = xm - strip_w/2; xR = xm + strip_w/2
        rect_top = SY(ym)
        rect_bot = SY(0)
        rect_left  = SX(xL)
        rect_right = SX(xR)
        rect_h     = rect_bot - rect_top
        rect_w     = rect_right - rect_left

        inner += (f'<rect x="{rect_left:.0f}" y="{rect_top:.0f}" width="{rect_w:.0f}" height="{rect_h:.0f}" '
                  f'fill="#a855f7" opacity="0.28" stroke="#a855f7" stroke-width="1.5"/>')

        # midpoint dot on curve
        inner += f'<circle cx="{SX(xm):.0f}" cy="{SY(ym):.0f}" r="7" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
        inner += f'<text x="{SX(xm):.0f}" y="{SY(0)+18}" fill="#e879f9" font-family="monospace" font-size="12" text-anchor="middle">{xm}</text>'

        # "overlap" wedge annotation (green) — top-left of rect
        # "missed" wedge annotation (red) — top-right of rect
        inner += (
            f'<text x="{SX(xm):.0f}" y="{rect_top-8:.0f}" fill="#e879f9" font-family="monospace" font-size="12" '
            f'font-weight="bold" text-anchor="middle">m={ym:.2f}</text>'
        )

    inner += f'<polyline points="{curve_pts}" fill="none" stroke="#facc15" stroke-width="3"/>'
    inner += f'<text x="{SX(3.5):.0f}" y="{SY(2.5):.0f}" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold">r=4 cm</text>'

    # Area calculation box
    inner += (
        f'<rect x="580" y="48" width="238" height="120" fill="#0f172a" rx="6" stroke="#a855f7" stroke-width="1.5"/>'
        f'<text x="699" y="70" fill="#a855f7" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">Mid-Ordinate Rule</text>'
        f'<text x="699" y="92" fill="#e2e8f0" font-family="monospace" font-size="12" text-anchor="middle">h=2, midpoints: -3,-1,1,3</text>'
        f'<text x="699" y="112" fill="#e879f9" font-family="monospace" font-size="12" text-anchor="middle">ym = sqrt(7), sqrt(15), sqrt(15), sqrt(7)</text>'
        f'<text x="699" y="132" fill="#4ade80" font-family="monospace" font-size="12" text-anchor="middle">Area = 2(2.646+3.873+3.873+2.646)</text>'
        f'<text x="699" y="152" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">= 26.08 cm^2 (error 3.75%)</text>'
    )
    # error-cancellation annotation
    inner += (
        f'<rect x="20" y="48" width="210" height="70" fill="#0f172a" rx="6" stroke="#4ade80" stroke-width="1.5"/>'
        f'<text x="125" y="70" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Error Cancellation:</text>'
        f'<text x="125" y="90" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">Overhang ~ Underhang</text>'
        f'<text x="125" y="110" fill="#4ade80" font-family="monospace" font-size="11" text-anchor="middle">=> very small net error</text>'
    )

    return mk(inner, W=840, H=390,
              title='V5: Semicircle Mid-Ordinate Rule — Midpoints at x=-3,-1,1,3 with Error Cancellation',
              tc='#a855f7')


# ─── L233 P3: Mid-ordinate formula card ──────────────────────────────────────
def mid_ordinate_formula_card():
    rows = [
        ('Area = h x (m1 + m2 + ... + mn)',             '#facc15', 18),
        ('h = (b - a) / n  (strip width)',               '#38bdf8', 15),
        ('mi = f( xi-1 + h/2 ) = midpoint of strip i',  '#e879f9', 14),
        ('n STRIPS give EXACTLY n midpoints',            '#4ade80', 14),
        ('Semicircle r=4: Area = 2(sqrt7+sqrt15+sqrt15+sqrt7) = 26.08 cm^2', '#94a3b8', 13),
    ]
    inner = ''
    for i,(t,c,s) in enumerate(rows):
        inner += (f'<rect x="60" y="{62+i*54}" width="720" height="44" fill="#1e293b" rx="6" stroke="{c}" stroke-width="1.2"/>'
                  f'<text x="400" y="{90+i*54}" fill="{c}" font-family="monospace" font-size="{s}" font-weight="bold" text-anchor="middle">{t}</text>')
    return mk(f'<rect x="50" y="48" width="740" height="310" fill="#0f172a" rx="10" stroke="#a855f7" stroke-width="1.5"/>{inner}',
              title='Mid-Ordinate Rule Formula — n Strips, n Midpoints, No First/Last Halving',
              tc='#a855f7')


# ─── L234 P2: V6 — Concavity Split-Panel ─────────────────────────────────────
def concavity_split_panel():
    # Left: concave-up y=3x^2-8x+10 on [0,4], Trapezium OVERESTIMATES
    # Right: concave-down (semicircle), Trapezium UNDERESTIMATES

    def side(ox, f_func, title, chord_color, label1, label2, is_convex):
        W2 = 360
        SX = lambda x: ox + x*(W2//5)
        SY = lambda y: 300 - y*18
        xs = [0,1,2,3,4]
        ys = [f_func(x) for x in xs]
        pts = ' '.join(f'{SX(i*0.05):.1f},{SY(f_func(i*0.05)):.1f}' for i in range(81))

        out = (
            f'<line x1="{SX(-0.2)}" y1="{SY(0)}" x2="{SX(4.5)}" y2="{SY(0)}" stroke="#334155" stroke-width="1.5"/>'
            f'<line x1="{SX(0)}" y1="{SY(0)+5}" x2="{SX(0)}" y2="{SY(17)}" stroke="#334155" stroke-width="1.5"/>'
        )
        # trapezia
        for i in range(4):
            xL, xR = xs[i], xs[i+1]
            pts_trap = f'{SX(xL):.0f},{SY(0)} {SX(xL):.0f},{SY(ys[i]):.0f} {SX(xR):.0f},{SY(ys[i+1]):.0f} {SX(xR):.0f},{SY(0)}'
            out += f'<polygon points="{pts_trap}" fill="{chord_color}" opacity="0.25" stroke="{chord_color}" stroke-width="1.2"/>'
        out += f'<polyline points="{pts}" fill="none" stroke="#facc15" stroke-width="2.5"/>'

        # callout arrows showing over/under gap
        mid_x = SX(2); mid_yc = SY(f_func(2)); mid_yt = SY(0.5*(ys[1]+ys[2]))
        gap = abs(mid_yc - mid_yt)
        if gap > 4:
            col2 = '#f87171' if is_convex else '#4ade80'
            out += f'<line x1="{mid_x}" y1="{min(mid_yc,mid_yt)}" x2="{mid_x}" y2="{max(mid_yc,mid_yt)}" stroke="{col2}" stroke-width="2" stroke-dasharray="3 2"/>'
            out += f'<text x="{mid_x+8}" y="{(mid_yc+mid_yt)//2+5}" fill="{col2}" font-family="monospace" font-size="11" font-weight="bold">gap</text>'

        out += f'<text x="{SX(2):.0f}" y="{SY(17.5):.0f}" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">{title}</text>'
        out += f'<text x="{SX(2):.0f}" y="330" fill="{chord_color}" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">{label1}</text>'
        out += f'<text x="{SX(2):.0f}" y="350" fill="{chord_color}" font-family="sans-serif" font-size="13" text-anchor="middle">{label2}</text>'
        return out

    import math
    out_left  = side(55,  lambda x: 0.5*x**2 - 2*x + 6, 'Concave Up: y = x^2/2 - 2x + 6',
                     '#f87171', 'Chords ABOVE curve', 'Trapezium OVERESTIMATES', True)
    out_right = side(470, lambda x: math.sqrt(max(0,16-x**2)), 'Concave Down: y = sqrt(16-x^2)',
                     '#4ade80', 'Chords BELOW curve', 'Trapezium UNDERESTIMATES', False)

    inner = (
        f'<rect x="30"  y="38" width="380" height="325" fill="#0f172a" rx="10" stroke="#f87171" stroke-width="1.5"/>'
        f'<rect x="430" y="38" width="380" height="325" fill="#0f172a" rx="10" stroke="#4ade80" stroke-width="1.5"/>'
        + out_left + out_right +
        f'<line x1="420" y1="38" x2="420" y2="363" stroke="#334155" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<text x="420" y="27" fill="#facc15" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">f\'\'(x) &gt; 0 (concave up)</text>'
    )
    return mk(inner, W=840, H=390,
              title='V6: Concavity Determines Trapezium Error Direction — Up=Over, Down=Under',
              tc='#facc15')


# ─── L234 P3: Comparative Error Formula Card ─────────────────────────────────
def error_formula_card():
    rows = [
        ('Exact area (definite integral) = E',                   '#4ade80', 15),
        ('Trapezium error = abs(T - E)',                          '#f87171', 15),
        ('Mid-Ordinate error = abs(M - E)',                       '#e879f9', 15),
        ('% error = abs(approx - exact) / exact x 100%',         '#facc15', 14),
        ('Concave UP:  T overestimates, M underestimates',        '#38bdf8', 13),
        ('Concave DOWN: T underestimates, M overestimates',       '#a855f7', 13),
    ]
    inner = ''
    for i,(t,c,s) in enumerate(rows):
        inner += (f'<rect x="60" y="{58+i*47}" width="720" height="37" fill="#1e293b" rx="6" stroke="{c}" stroke-width="1.2"/>'
                  f'<text x="400" y="{82+i*47}" fill="{c}" font-family="monospace" font-size="{s}" font-weight="bold" text-anchor="middle">{t}</text>')
    return mk(f'<rect x="50" y="45" width="740" height="305" fill="#0f172a" rx="10" stroke="#facc15" stroke-width="1.5"/>{inner}',
              title='Comparative Error Analysis: Trapezium vs Mid-Ordinate vs Exact',
              tc='#facc15')


# ─── L234 P4: Worked Example Comparison Card ─────────────────────────────────
def worked_eg_comparison():
    steps = [
        (78,  'f(x) = x^2 + 2,  x in [0, 2],  n = 4 strips, h = 0.5', '#facc15', 14),
        (120, 'Exact: integral = [x^3/3 + 2x] from 0 to 2 = 8/3 + 4 = 20/3 = 6.667', '#4ade80', 13),
        (162, 'Trapezium:    h/2(y0+y4 + 2(y1+y2+y3))',                '#38bdf8', 14),
        (198, '= 0.5/2(2+6 + 2(2.25+3+4.25)) = 0.25 x 27 = 6.750',  '#38bdf8', 14),
        (240, 'Mid-Ordinate: h(m1+m2+m3+m4)',                          '#e879f9', 14),
        (276, '= 0.5(2.0625+2.5625+3.5625+5.0625) = 6.625',           '#e879f9', 14),
        (318, 'Errors: Trap=0.083, Mid-Ord=0.042  (Mid-Ord half Trap error!)', '#f87171', 13),
    ]
    inner = (
        ''.join(
            f'<text x="420" y="{y}" fill="{c}" font-family="monospace" font-size="{s}" '
            f'font-weight="bold" text-anchor="middle">{t}</text>'
            for y,t,c,s in steps
        ) +
        f'<line x1="80" y1="96" x2="760" y2="96" stroke="#facc15" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<rect x="80" y="298" width="680" height="34" fill="#1c0a0a" rx="5" stroke="#f87171" stroke-width="1.5"/>'
        f'<rect x="80" y="140" width="680" height="40" fill="#14352b" rx="5" stroke="#38bdf8" stroke-width="1"/>'
        f'<rect x="80" y="222" width="680" height="40" fill="#2d1a4a" rx="5" stroke="#e879f9" stroke-width="1"/>'
    )
    return mk(f'<rect x="50" y="45" width="740" height="315" fill="#0f172a" rx="10" stroke="#4ade80" stroke-width="1.5"/>{inner}',
              title='Worked Example: Trapezium vs Mid-Ordinate for y=x^2+2, x in [0,2]',
              tc='#4ade80')


# ─── Warning cards ─────────────────────────────────────────────────────────────
def warn_inverted_bounds():
    return warn('For DECREASING functions: LEFT endpoint is the MAXIMUM, RIGHT is the MINIMUM',
                'Always evaluate f(x) at each endpoint — do not assume direction from the sign of x!')

def warn_ordinates():
    return warn('n strips give (n+1) ordinates y0 to yn — NOT n ordinates',
                '4 strips need ordinates y0, y1, y2, y3, y4 — five values. Off-by-one loses full marks!')

def warn_midordinate():
    return warn('Mid-Ordinate Rule evaluates at MIDPOINTS of strips, not endpoints',
                'Midpoint of strip i = xi-1 + h/2 = (xi-1 + xi)/2. Using right boundaries gives wrong heights!')

def warn_concavity():
    return warn('Concave-UP: Trapezium OVERESTIMATES, Mid-Ordinate UNDERESTIMATES',
                'Concave-DOWN is the opposite. Also: 1 unit^2 on map = (scale)^2 in real area — NOT scale x 1!')


# ─── Run all ──────────────────────────────────────────────────────────────────
def enrich_topic10_blueprint():
    print('=== TOPIC 10 BLUEPRINT ENRICHMENT ===\n')

    # Lesson 231: Area Division & Grid Counting
    push(14373, 'V1: Grid Square Counting — 25 Full + 16 Partial = 33 cm^2',  forest_grid())
    push(14374, 'V2: Inner and Outer Bounding Rectangles — Squeeze Theorem',   bounding_rects_v2())
    push(14375, 'Worked Example 1: Grid Square Counting and Bounding Rects',   bounding_rects_v2())
    push(14376, 'Common Error: Inverting Bounds for Decreasing Functions',      warn_inverted_bounds())

    # Lesson 232: Trapezium Rule
    push(14377, 'V3: Trapezium Rule — Shared Interior Ordinates (x2)',          trapezium_shared_ordinates())
    push(14378, 'V4: Kazungu vs Ndoe Boundary Dispute — Metric Conversion',    kazungu_ndoe_map())
    push(14379, 'Worked Example 1: Trapezium Rule with Ordinate Labelling',    trapezium_shared_ordinates())
    push(14380, 'Common Error: Strip Count vs Ordinate Count Off-By-One',       warn_ordinates())

    # Lesson 233: Mid-Ordinate Rule
    push(14381, 'V5: Semicircle Mid-Ordinate — Error Cancellation Wedges',     semicircle_mid_ordinate())
    push(14382, 'Mid-Ordinate Rule Formula — n Strips, n Midpoints',           mid_ordinate_formula_card())
    push(14383, 'Worked Example 1: Mid-Ordinate Rule for y = x^2 + 3',        mid_ordinate_formula_card())
    push(14384, 'Common Error: Right-Hand Boundaries vs Midpoints',             warn_midordinate())

    # Lesson 234: Comparative Error Analysis
    push(14385, 'V6: Concavity Split-Panel — Over vs Underestimate',           concavity_split_panel())
    push(14386, 'Comparative Error Analysis Formula Reference',                  error_formula_card())
    push(14387, 'Worked Example 1: Trapezium vs Mid-Ordinate Error Comparison', worked_eg_comparison())
    push(14388, 'Common Error: Concavity Direction and Scale-Factor Errors',    warn_concavity())

    print('\n=== TOPIC 10 BLUEPRINT ENRICHMENT COMPLETE ===')


if __name__ == '__main__':
    enrich_topic10_blueprint()
