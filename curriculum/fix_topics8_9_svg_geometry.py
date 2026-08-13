"""
Fix Topics 8 and 9 — replace ALL text-only SVG blocks with proper geometric diagrams.
Targets production block IDs: 14341–14372
"""
import os, sys, django
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.core.files.base import ContentFile
from curriculum.models import LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

# ─── Helpers ──────────────────────────────────────────────────────────────────
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
        fname = f'fix_t89_{block_id}.svg'
        asset.file.save(fname, ContentFile(svg.encode()), save=True)
        asset.save()
    print(f'  Block {block_id}: {title[:55]}')


def svg(inner, title='', W=840, H=380, title_color='#38bdf8'):
    t = (f'<text x="{W//2}" y="30" fill="{title_color}" font-family="system-ui,sans-serif" '
         f'font-size="16" font-weight="bold" text-anchor="middle">{title}</text>') if title else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">'
            f'<rect width="{W}" height="{H}" fill="{BG}" rx="14"/>'
            f'{t}{inner}</svg>')

def panel(inner, x=50, y=45, w=740, h=300, border='#334155'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#0f172a" rx="10" '
            f'stroke="{border}" stroke-width="1.5"/>{inner}')

def row(cx, y, text, color='#e2e8f0', size=15, anchor='middle', bold=True):
    fw = 'bold' if bold else 'normal'
    return (f'<text x="{cx}" y="{y}" fill="{color}" font-family="monospace" '
            f'font-size="{size}" font-weight="{fw}" text-anchor="{anchor}">{text}</text>')

def warn_svg(line1, line2='', title='COMMON ERROR'):
    inner = (f'<rect x="50" y="45" width="740" height="300" fill="#1c0a0a" rx="10" stroke="#f87171" stroke-width="2"/>'
             f'<text x="420" y="110" fill="#f87171" font-family="system-ui,sans-serif" font-size="22" '
             f'font-weight="bold" text-anchor="middle">{title}</text>'
             f'<line x1="150" y1="130" x2="690" y2="130" stroke="#f87171" stroke-width="1" stroke-dasharray="4 3"/>'
             f'<text x="420" y="185" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="15" '
             f'font-weight="bold" text-anchor="middle">{line1}</text>')
    if line2:
        inner += (f'<text x="420" y="220" fill="#fcd34d" font-family="system-ui,sans-serif" font-size="14" '
                  f'font-weight="normal" text-anchor="middle">{line2}</text>')
    return svg(inner)

def axis(x0, y0, x1, y1, label_x='', label_y='', color='#475569'):
    out = (f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{color}" stroke-width="2"/>'
           f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{color}" stroke-width="2"/>')
    if label_x:
        out += f'<text x="{x1+10}" y="{y0+5}" fill="{color}" font-family="sans-serif" font-size="14" font-weight="bold">{label_x}</text>'
    if label_y:
        out += f'<text x="{x0-4}" y="{y1-8}" fill="{color}" font-family="sans-serif" font-size="14" font-weight="bold">{label_y}</text>'
    return out

def box(x, y, w, h, text, fill='#1e3a5f', stroke='#38bdf8', tcolor='#e2e8f0', size=14):
    lines = text.split('|')
    rects = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" rx="8" stroke="{stroke}" stroke-width="1.5"/>'
    dy = h / (len(lines)+1)
    for i,l in enumerate(lines):
        rects += f'<text x="{x+w//2}" y="{y+int(dy*(i+1))+5}" fill="{tcolor}" font-family="monospace" font-size="{size}" font-weight="bold" text-anchor="middle">{l}</text>'
    return rects

def arrow(x1,y1,x2,y2,color='#64748b'):
    rot = 0 if y2 > y1 else 180
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"/>'
            f'<polygon points="{x2},{y2} {x2-6},{y2-10} {x2+6},{y2-10}" fill="{color}" transform="rotate({rot},{x2},{y2})"/>')

def kin_box(x, y, label, sub, color):
    return (
        f'<rect x="{x}" y="{y}" width="180" height="65" fill="#0f172a" rx="10" stroke="{color}" stroke-width="2"/>'
        f'<text x="{x+90}" y="{y+30}" fill="{color}" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">{label}</text>'
        f'<text x="{x+90}" y="{y+52}" fill="{color}" font-family="sans-serif" font-size="12" text-anchor="middle">{sub}</text>'
    )

def kin_arrow(x1,y1,x2,y2,label,color='#64748b'):
    mx,my=(x1+x2)//2,(y1+y2)//2
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"/>'
        f'<polygon points="{x2},{y2} {x2-8},{y2-14} {x2+8},{y2-14}" fill="{color}"/>'
        f'<text x="{mx+14}" y="{my+5}" fill="{color}" font-family="monospace" font-size="13" font-weight="bold">{label}</text>'
    )

# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 8 — DIFFERENTIATION
# ══════════════════════════════════════════════════════════════════════════════

def topic8():
    print('\n=== TOPIC 8: Differentiation ===')

    # ── L223 P2: Secant-to-Tangent Limit ────────────────────────────────────
    # Parabola y=x^2 scaled, secant from P to Q, then tangent at P
    # X: 80..700  Y: 340..60 (inverted)  domain 0..4  range 0..16
    sx = lambda x: 80 + (x/4)*620
    sy = lambda y: 340 - (y/16)*280
    # curve points  y=x^2
    pts = ' '.join(f'{sx(i*0.05):.1f},{sy((i*0.05)**2):.1f}' for i in range(81))
    # P at x=1, Q at x=3 (secant), then tangent at x=1 slope=2
    px, py = sx(1), sy(1); qx, qy = sx(3), sy(9)
    # secant line extended
    sm = (9-1)/(3-1); sb = 1 - sm*1  # y=sm*x+sb
    sex1, sey1 = sx(0.2), sy(sm*0.2+sb); sex2, sey2 = sx(3.8), sy(sm*3.8+sb)
    # tangent at x=1: slope=2x=2; y-1=2(x-1)
    tm = 2; tb = 1 - tm*1
    tex1, tey1 = sx(0.1), sy(tm*0.1+tb); tex2, tey2 = sx(2.5), sy(tm*2.5+tb)
    inner = (
        panel(
            axis(80,340,720,50,'x','y') +
            f'<polyline points="{pts}" fill="none" stroke="#facc15" stroke-width="3"/>'
            f'<line x1="{sex1:.0f}" y1="{sey1:.0f}" x2="{sex2:.0f}" y2="{sey2:.0f}" stroke="#f87171" stroke-width="2" stroke-dasharray="7 4"/>'
            f'<line x1="{tex1:.0f}" y1="{tey1:.0f}" x2="{tex2:.0f}" y2="{tey2:.0f}" stroke="#4ade80" stroke-width="2.5"/>'
            f'<circle cx="{px:.0f}" cy="{py:.0f}" r="7" fill="#38bdf8" stroke="#fff" stroke-width="1.5"/>'
            f'<circle cx="{qx:.0f}" cy="{qy:.0f}" r="7" fill="#f87171" stroke="#fff" stroke-width="1.5"/>'
            f'<text x="{px:.0f}" y="{py-14:.0f}" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">P(x, f(x))</text>'
            f'<text x="{qx:.0f}" y="{qy-14:.0f}" fill="#f87171" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Q(x+h, f(x+h))</text>'
            f'<text x="640" y="72"  fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">Secant (h&gt;0)</text>'
            f'<text x="560" y="200" fill="#4ade80" font-family="sans-serif" font-size="13" font-weight="bold">Tangent (h&#x2192;0)</text>'
            f'<text x="720" y="190" fill="#facc15" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="end">y = f(x)</text>',
            x=50, y=45, w=740, h=310, border='#38bdf8'
        )
    )
    push(14341, 'Secant-to-Tangent Limit Process (h → 0)',
         svg(inner, 'Secant-to-Tangent: As h → 0, Secant → Tangent at P', title_color='#38bdf8'))


    inner2 = (
        box(80,  60, 680, 50, 'Write:  f(x+h) and f(x)',               fill='#1e3a5f', stroke='#38bdf8', tcolor='#93c5fd') +
        arrow(420,110,420,140,'#38bdf8') +
        box(80, 140, 680, 50, 'Form:  [f(x+h) - f(x)] / h',           fill='#14352b', stroke='#4ade80', tcolor='#86efac') +
        arrow(420,190,420,220,'#4ade80') +
        box(80, 220, 680, 50, 'Expand and CANCEL h from numerator',    fill='#3b2a10', stroke='#facc15', tcolor='#fde68a') +
        arrow(420,270,420,300,'#facc15') +
        box(80, 300, 680, 50, 'Take limit as h → 0  →  f\'(x)',        fill='#2d1a4a', stroke='#a855f7', tcolor='#d8b4fe')
    )
    push(14342, 'First Principles Definition Flowchart',
         svg(panel(inner2, x=50, y=45, w=740, h=320, border='#38bdf8'),
             'First Principles: Step-by-Step Algorithm  f\'(x) = lim[h→0] [f(x+h)-f(x)]/h',
             title_color='#38bdf8'))

    # ── L223 P4: Worked Example y=x^2 ────────────────────────────────────────
    steps = [
        (80,  'f(x+h) = (x+h)^2 = x^2 + 2xh + h^2',         '#facc15'),
        (130, 'f(x+h) - f(x) = x^2 + 2xh + h^2 - x^2',      '#e2e8f0'),
        (175, '          = 2xh + h^2',                         '#e2e8f0'),
        (220, '[f(x+h)-f(x)] / h = (2xh + h^2) / h',         '#38bdf8'),
        (265, '               = 2x + h',                       '#38bdf8'),
        (310, 'As h → 0:  f\'(x) = 2x  ✓',                    '#4ade80'),
    ]
    inner3 = ''.join(row(420, y, t, c, 14) for y,t,c in steps)
    # highlight the cancellation
    inner3 += f'<rect x="380" y="200" width="260" height="32" fill="none" stroke="#facc15" stroke-width="1.5" rx="4" stroke-dasharray="5 3"/>'
    push(14343, 'Worked Example 1: First Principles Expansion (y = x²)',
         svg(panel(inner3, x=50, y=45, w=740, h=310, border='#4ade80'),
             'Worked Example: First Principles for y = x²',
             title_color='#4ade80'))

    # ── L223 P9: Binomial Expansion Warning ─────────────────────────────────
    push(14344, 'Common Error: Binomial Expansion Warning',
         warn_svg('(x + h)^2 = x^2 + 2xh + h^2   NOT   x^2 + h^2',
                  'The middle term 2xh MUST be included — dropping it gives f\'(x) = 0, which is wrong!'))

    # ── L224 P2: Power Rule Transformation ──────────────────────────────────
    # Arrow diagram: ax^n  →multiply by n→  an  →reduce power→  ax^(n-1)
    inner4 = (
        f'<rect x="80"  y="90"  width="200" height="70" fill="#1e3a5f" rx="10" stroke="#38bdf8" stroke-width="2"/>'
        f'<text x="180" y="135" fill="#facc15" font-family="monospace" font-size="24" font-weight="bold" text-anchor="middle">ax^n</text>'
        f'<line x1="280" y1="125" x2="370" y2="125" stroke="#64748b" stroke-width="2"/>'
        f'<polygon points="370,125 358,118 358,132" fill="#64748b"/>'
        f'<text x="325" y="113" fill="#94a3b8" font-family="sans-serif" font-size="12" text-anchor="middle">bring down n</text>'
        f'<rect x="370" y="90"  width="200" height="70" fill="#14352b" rx="10" stroke="#4ade80" stroke-width="2"/>'
        f'<text x="470" y="135" fill="#4ade80" font-family="monospace" font-size="24" font-weight="bold" text-anchor="middle">a·n·x^n</text>'
        f'<line x1="570" y1="125" x2="660" y2="125" stroke="#64748b" stroke-width="2"/>'
        f'<polygon points="660,125 648,118 648,132" fill="#64748b"/>'
        f'<text x="615" y="113" fill="#94a3b8" font-family="sans-serif" font-size="12" text-anchor="middle">reduce power</text>'
        f'<rect x="560" y="90"  width="220" height="70" fill="#2d1a4a" rx="10" stroke="#a855f7" stroke-width="2"/>'
        f'<text x="670" y="135" fill="#a855f7" font-family="monospace" font-size="24" font-weight="bold" text-anchor="middle">an·x^(n-1)</text>'
        # Examples row
        f'<text x="420" y="210" fill="#64748b" font-family="monospace" font-size="13" text-anchor="middle">Examples:</text>'
        f'<text x="180" y="240" fill="#facc15" font-family="monospace" font-size="15" text-anchor="middle">3x^4</text>'
        f'<text x="420" y="240" fill="#4ade80" font-family="monospace" font-size="15" text-anchor="middle">→  12x^3</text>'
        f'<text x="640" y="240" fill="#a855f7" font-family="monospace" font-size="15" text-anchor="middle">(n=4, a=3)</text>'
        f'<text x="180" y="270" fill="#facc15" font-family="monospace" font-size="15" text-anchor="middle">5x^2</text>'
        f'<text x="420" y="270" fill="#4ade80" font-family="monospace" font-size="15" text-anchor="middle">→  10x</text>'
        f'<text x="640" y="270" fill="#a855f7" font-family="monospace" font-size="15" text-anchor="middle">(n=2, a=5)</text>'
        f'<text x="180" y="300" fill="#facc15" font-family="monospace" font-size="15" text-anchor="middle">7x</text>'
        f'<text x="420" y="300" fill="#4ade80" font-family="monospace" font-size="15" text-anchor="middle">→  7</text>'
        f'<text x="640" y="300" fill="#a855f7" font-family="monospace" font-size="15" text-anchor="middle">(n=1, a=7)</text>'
    )
    push(14345, 'Power Rule Derivative Transformation',
         svg(panel(inner4, x=50, y=45, w=740, h=310, border='#38bdf8'),
             'd/dx [ax^n] = an·x^(n-1)  — Power Rule Visual',
             title_color='#38bdf8'))

    # ── L224 P3: Power Rule Cheat Sheet ─────────────────────────────────────
    rules = [
        ('d/dx [x^n]  = n·x^(n-1)',            '#facc15'),
        ('d/dx [c]    = 0   (constant → zero)', '#f87171'),
        ('d/dx [x^-n] = -n·x^(-n-1)',           '#38bdf8'),
        ('d/dx [x^(1/n)] = (1/n)·x^(1/n - 1)', '#4ade80'),
        ('d/dx [cf(x)] = c·f\'(x)  (scalar)',   '#e879f9'),
    ]
    inner5 = ''.join(
        f'<rect x="60" y="{65+i*48}" width="720" height="38" fill="#1e293b" rx="6" stroke="{c}" stroke-width="1.2"/>'
        f'<text x="400" y="{90+i*48}" fill="{c}" font-family="monospace" font-size="15" font-weight="bold" text-anchor="middle">{t}</text>'
        for i,(t,c) in enumerate(rules)
    )
    push(14346, 'Power Rule Cheat Sheet & Exponent Rules',
         svg(panel(inner5, x=50, y=45, w=740, h=310, border='#38bdf8'),
             'Power Rule Cheat Sheet: d/dx Rules for All Exponent Types',
             title_color='#38bdf8'))

    # ── L224 P4: Polynomial Term-by-Term ────────────────────────────────────
    steps4 = [
        (75,  'y = 3x^4 - 5x^2 + 7x - 9',            '#facc15', 16),
        (120, 'dy/dx each term separately:',            '#94a3b8', 13),
        (162, 'd/dx [3x^4]  =  4 × 3 · x^3  = 12x^3', '#38bdf8', 15),
        (200, 'd/dx [-5x^2] =  2 × (-5) · x =  -10x', '#38bdf8', 15),
        (238, 'd/dx [7x]    =  7',                      '#38bdf8', 15),
        (276, 'd/dx [-9]    =  0   (constant!)',        '#f87171', 15),
        (320, 'dy/dx = 12x^3 - 10x + 7  ✓',           '#4ade80', 16),
    ]
    inner6 = ''.join(row(420, y, t, c, s) for y,t,c,s in steps4)
    inner6 += f'<line x1="80" y1="98" x2="760" y2="98" stroke="#facc15" stroke-width="1" stroke-dasharray="5 3"/>'
    inner6 += f'<line x1="80" y1="296" x2="760" y2="296" stroke="#4ade80" stroke-width="1" stroke-dasharray="5 3"/>'
    push(14347, 'Worked Example 1: Polynomial Term-by-Term Differentiation',
         svg(panel(inner6, x=50, y=45, w=740, h=315, border='#4ade80'),
             'Worked Example: y = 3x^4 - 5x^2 + 7x - 9  →  dy/dx = 12x^3 - 10x + 7',
             title_color='#4ade80'))

    # ── L224 P9: Differentiating Constants Warning ───────────────────────────
    push(14348, 'Common Error: Differentiating Constants Warning',
         warn_svg('d/dx [constant] = 0   ALWAYS',
                  'The slope of a horizontal line is ZERO. Never carry a constant into the derivative!'))

    # ── L225 P2: Tangent, Normal & Turning Point Geometry ───────────────────
    # Parabola with tangent, normal, turning point
    sx2 = lambda x: 100 + (x/5)*620
    sy2 = lambda y: 330 - (y/20)*270
    # y = (x-2)^2 + 1  min at x=2, y=1
    pts2 = ' '.join(f'{sx2(i*0.05):.1f},{sy2((i*0.05-2)**2+1):.1f}' for i in range(101))
    tp_x, tp_y = sx2(2), sy2(1)  # turning point
    # tangent at x=3.5: slope=2(3.5-2)=3; y-3.25=3(x-3.5)
    xp=3.5; yp=(xp-2)**2+1; m_t=2*(xp-2); m_n=-1/m_t
    tx1,ty1 = sx2(2.5), sy2(yp+m_t*(2.5-xp))
    tx2,ty2 = sx2(4.5), sy2(yp+m_t*(4.5-xp))
    nx1,ny1 = sx2(3.0), sy2(yp+m_n*(3.0-xp))
    nx2,ny2 = sx2(4.5), sy2(yp+m_n*(4.5-xp))
    dot_x, dot_y = sx2(xp), sy2(yp)
    inner7 = (
        panel(
            axis(80,340,730,50,'x','y') +
            f'<polyline points="{pts2}" fill="none" stroke="#facc15" stroke-width="3"/>'
            # tangent (cyan)
            f'<line x1="{tx1:.0f}" y1="{ty1:.0f}" x2="{tx2:.0f}" y2="{ty2:.0f}" stroke="#22d3ee" stroke-width="2.5"/>'
            # normal (magenta)
            f'<line x1="{nx1:.0f}" y1="{ny1:.0f}" x2="{nx2:.0f}" y2="{ny2:.0f}" stroke="#e879f9" stroke-width="2" stroke-dasharray="6 3"/>'
            # right-angle mark at intersection
            f'<rect x="{dot_x:.0f}" y="{dot_y-14:.0f}" width="11" height="11" fill="none" stroke="#e879f9" stroke-width="1.5"/>'
            # tangent point
            f'<circle cx="{dot_x:.0f}" cy="{dot_y:.0f}" r="7" fill="#22d3ee" stroke="#fff" stroke-width="1.5"/>'
            # turning point (gold)
            f'<circle cx="{tp_x:.0f}" cy="{tp_y:.0f}" r="8" fill="#fbbf24" stroke="#fff" stroke-width="2"/>'
            f'<text x="{tp_x:.0f}" y="{tp_y-16:.0f}" fill="#fbbf24" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Turning Point f\'(x)=0</text>'
            f'<text x="{tx2-20:.0f}" y="{ty2-12:.0f}" fill="#22d3ee" font-family="sans-serif" font-size="13" font-weight="bold">Tangent (m_T)</text>'
            f'<text x="{nx2-20:.0f}" y="{ny2+18:.0f}" fill="#e879f9" font-family="sans-serif" font-size="13" font-weight="bold">Normal (m_N)</text>'
            f'<text x="680" y="68" fill="#facc15" font-family="sans-serif" font-size="13" font-weight="bold">y=f(x)</text>'
            f'<text x="{dot_x+12:.0f}" y="{dot_y-4:.0f}" fill="#22d3ee" font-family="sans-serif" font-size="12">P(x&#x2080;,y&#x2080;)</text>',
            x=50, y=45, w=740, h=310, border='#38bdf8'
        )
    )
    push(14349, 'Tangent, Normal & Turning Point Geometry',
         svg(inner7, 'Tangent Line, Normal Line (90°) and Turning Point on y = f(x)',
             title_color='#38bdf8'))

    # ── L225 P3: Stationary Point Classification ─────────────────────────────
    # Three mini curves: max, min, inflexion with sign-change arrows
    def mini_curve(cx, label, pts_str, dot_color, signs, title_str, title_col):
        return (
            f'<text x="{cx}" y="68" fill="{title_col}" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">{title_str}</text>'
            f'<polyline points="{pts_str}" fill="none" stroke="#facc15" stroke-width="2.5"/>'
            f'<circle cx="{cx}" cy="{dot_color[1]}" r="7" fill="{dot_color[0]}" stroke="#fff" stroke-width="1.5"/>'
            f'<text x="{cx-60}" y="320" fill="{signs[0]}" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">{signs[1]}</text>'
            f'<text x="{cx}"    y="320" fill="#64748b"   font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">0</text>'
            f'<text x="{cx+60}" y="320" fill="{signs[2]}" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">{signs[3]}</text>'
            f'<text x="{cx-60}" y="342" fill="{signs[0]}" font-family="monospace" font-size="11" text-anchor="middle">f\'&lt;0 before</text>'  # noqa
            f'<text x="{cx+60}" y="342" fill="{signs[2]}" font-family="monospace" font-size="11" text-anchor="middle">f\'&gt;0 after</text>'   # noqa
            + label
        )
    inner8 = (
        f'<line x1="280" y1="50" x2="280" y2="355" stroke="#334155" stroke-width="1"/>'
        f'<line x1="560" y1="50" x2="560" y2="355" stroke="#334155" stroke-width="1"/>'
        # LOCAL MAX (left third)
        + mini_curve(140, f'<text x="140" y="355" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Local MAX</text>',
                     '80,280 110,210 140,155 170,210 200,280', ('#f87171',155),
                     ('#4ade80','+ ','#f87171',' -'),'Maximum: f\'(x) = 0','#f87171')
        # LOCAL MIN (middle)
        + mini_curve(420, f'<text x="420" y="355" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Local MIN</text>',
                     '360,160 390,230 420,280 450,230 480,160', ('#4ade80',280),
                     ('#f87171','- ','#4ade80','+ '),'Minimum: f\'(x) = 0','#4ade80')
        # INFLEXION (right third)
        + mini_curve(700, f'<text x="700" y="355" fill="#a855f7" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Inflexion</text>',
                     '640,280 665,220 700,190 735,160 760,100', ('#a855f7',190),
                     ('#4ade80','+ ','#4ade80','+ '),'Inflexion: f\'(x) = 0','#a855f7')
        + f'<text x="420" y="40" fill="#e2e8f0" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">f\'(x) sign change test at stationary point</text>'
    )
    push(14350, 'Stationary Point Classification Test',
         svg(f'<rect width="840" height="380" fill="{BG}" rx="14"/>' + panel(inner8, x=20, y=45, w=800, h=315, border='#334155'),
             '', title_color='#38bdf8'))

    # ── L225 P4: Tangent & Normal Equations ─────────────────────────────────
    steps5 = [
        (80,  'At point P(x₀, y₀) on y = f(x):',         '#94a3b8', 13),
        (118, 'Step 1: Find y₀ = f(x₀)',                  '#facc15', 15),
        (158, 'Step 2: Find m_T = dy/dx at x = x₀',       '#22d3ee', 15),
        (198, 'Step 3: m_N = -1 / m_T  (perpendicular)',   '#e879f9', 15),
        (240, 'Tangent:  y - y₀ = m_T (x - x₀)',          '#22d3ee', 16),
        (280, 'Normal:   y - y₀ = m_N (x - x₀)',          '#e879f9', 16),
        (318, 'm_T × m_N = -1  (perpendicular condition)', '#4ade80', 14),
    ]
    inner9 = (
        ''.join(row(420, y, t, c, s) for y,t,c,s in steps5) +
        f'<line x1="80" y1="98" x2="760" y2="98" stroke="#334155" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<line x1="80" y1="258" x2="760" y2="258" stroke="#334155" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<rect x="80" y="226" width="680" height="38" fill="#14352b" rx="6" stroke="#22d3ee" stroke-width="1"/>'
        f'<rect x="80" y="264" width="680" height="38" fill="#2d1a4a" rx="6" stroke="#e879f9" stroke-width="1"/>'
    )
    push(14351, 'Worked Example 1: Tangent & Normal Equations',
         svg(panel(inner9, x=50, y=45, w=740, h=315, border='#38bdf8'),
             'Tangent and Normal Line Equations at Point P(x₀, y₀)',
             title_color='#38bdf8'))

    # ── L225 P9: Substitution Warning ────────────────────────────────────────
    push(14352, 'Common Error: Derivative Substitution Warning',
         warn_svg('Substitute x₀ into dy/dx to find SLOPE m_T',
                  'Do NOT substitute x₀ into y = f(x) and call the result the slope — that gives the y-coordinate, not the gradient!'))

    # ── L226 P2: Kinematics Differentiation Ladder ───────────────────────────
    inner10 = (
        kin_box(90,  80,  's(t)', 'Displacement',  '#facc15') +
        kin_arrow(270,112,330,112,'d/dt','#38bdf8') +
        kin_box(330, 80,  'v(t)', 'Velocity',      '#38bdf8') +
        kin_arrow(510,112,570,112,'d/dt','#4ade80') +
        kin_box(570, 80,  'a(t)', 'Acceleration',  '#4ade80') +
        # reverse: integrate
        kin_arrow(570,170,510,170,'∫ dt','#e879f9') +
        kin_arrow(330,170,270,170,'∫ dt','#e879f9') +
        f'<text x="420" y="230" fill="#e879f9" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">← Integration reverses the direction</text>'
        f'<text x="420" y="265" fill="#94a3b8" font-family="monospace" font-size="13" text-anchor="middle">v = ds/dt    a = dv/dt = d²s/dt²</text>'
        f'<text x="420" y="300" fill="#facc15" font-family="monospace" font-size="13" text-anchor="middle">At REST: v(t) = 0     MAX SPEED: a(t) = 0</text>'
    )
    push(14353, 'Kinematics Differentiation Ladder',
         svg(panel(inner10, x=50, y=45, w=740, h=290, border='#38bdf8'),
             'Kinematics Ladder: s(t) → v(t) → a(t) via Differentiation',
             title_color='#38bdf8'))

    # ── L226 P3: Optimization Algorithm ─────────────────────────────────────
    opt_steps = [
        (box(90, 65, 660, 45,  'Write the objective function V(x) or A(x)',      fill='#1e3a5f', stroke='#38bdf8', tcolor='#93c5fd') +
         arrow(420,110,420,135,'#38bdf8')),
        (box(90,135, 660, 45, 'Differentiate: find dV/dx or dA/dx',              fill='#14352b', stroke='#4ade80', tcolor='#86efac') +
         arrow(420,180,420,205,'#4ade80')),
        (box(90,205, 660, 45, 'Set derivative = 0  and solve for x',             fill='#3b2a10', stroke='#facc15', tcolor='#fde68a') +
         arrow(420,250,420,275,'#facc15')),
        (box(90,275, 660, 45, 'Verify MAXIMUM or MINIMUM (second derivative test)', fill='#2d1a4a', stroke='#a855f7', tcolor='#d8b4fe') +
         arrow(420,320,420,345,'#a855f7')),
        (box(90,345, 660, 40, 'Substitute x back → find optimal value',          fill='#1a2d1a', stroke='#4ade80', tcolor='#4ade80')),
    ]
    push(14354, 'Real-World Optimization Algorithm',
         svg(panel(''.join(opt_steps), x=50, y=45, w=740, h=355, border='#38bdf8'),
             'Optimization Algorithm: Find Maximum or Minimum Value',
             title_color='#38bdf8', H=420))

    # ── L226 P4: Motion Graphs s(t) v(t) a(t) ───────────────────────────────
    # Three stacked mini-graphs side by side
    def motion_curve(x0, y0, w, h, pts, label, color, note=''):
        return (
            f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#0f172a" rx="8" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x0+10}" y1="{y0+h//2}" x2="{x0+w-10}" y2="{y0+h//2}" stroke="#334155" stroke-width="1"/>'
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.5"/>'
            f'<text x="{x0+w//2}" y="{y0+h+20}" fill="{color}" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">{label}</text>'
            + (f'<text x="{x0+w//2}" y="{y0+h+36}" fill="#64748b" font-family="sans-serif" font-size="11" text-anchor="middle">{note}</text>' if note else '')
        )
    # s(t) = t^2 - 4t + 3: scaled to box
    s_pts = ' '.join(f'{90+i*30},{180-((i*0.5-2)**2*15-15):.0f}' for i in range(9))
    # v(t)=2t-4
    v_pts = ' '.join(f'{90+i*30},{260-((i*0.5*2-4)*12):.0f}' for i in range(9))
    # a(t)=2 (constant)
    a_pts = f'90,310 330,310'
    inner11 = (
        motion_curve(65,  60, 210, 120, s_pts, 's(t)  Displacement', '#facc15', 'position curve') +
        motion_curve(310, 60, 210, 120, v_pts, 'v(t)  Velocity',     '#38bdf8', 'v=0 → particle at rest') +
        motion_curve(555, 60, 210, 120, a_pts, 'a(t)  Acceleration', '#4ade80', 'a=const → uniform accel') +
        # rest annotation
        f'<circle cx="{310+90}" cy="260" r="6" fill="#f87171" stroke="#fff" stroke-width="1.5"/>'
        f'<text x="400" y="250" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">v=0 (rest)</text>'
        f'<text x="420" y="310" fill="#94a3b8" font-family="monospace" font-size="13" text-anchor="middle">d/dt: s(t) → v(t) → a(t)</text>'
    )
    push(14355, 'Worked Example 1: Motion Graphs s(t), v(t), a(t)',
         svg(panel(inner11, x=50, y=45, w=740, h=290, border='#38bdf8'),
             'Motion Graphs: s(t) Displacement → v(t) Velocity → a(t) Acceleration',
             title_color='#38bdf8'))

    # ── L226 P9: v=0 vs a=0 Warning ──────────────────────────────────────────
    push(14356, 'Common Error: Velocity vs Acceleration Zero Warning',
         warn_svg('v(t) = 0 means PARTICLE AT REST  (not maximum speed)',
                  'a(t) = 0 means CONSTANT VELOCITY (maximum speed if started from rest). Never confuse these two!'))

    print('  Topic 8 done — 16 blocks updated.')


# ══════════════════════════════════════════════════════════════════════════════
# TOPIC 9 — INTEGRATION
# ══════════════════════════════════════════════════════════════════════════════

def topic9():
    print('\n=== TOPIC 9: Integration ===')

    sx = lambda x: 80 + (x/5)*640
    sy = lambda y: 330 - (y/14)*270

    # ── L227 P2: Antiderivative as Reverse of Differentiation ────────────────
    inner = (
        f'<rect x="50" y="50" width="740" height="120" fill="#0f172a" rx="10" stroke="#38bdf8" stroke-width="1.5"/>'
        f'<text x="420" y="90"  fill="#facc15" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">Differentiation:  d/dx [ F(x) ] = f(x)</text>'
        f'<text x="420" y="130" fill="#64748b" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle">⇕</text>'
        f'<text x="420" y="160" fill="#4ade80" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">Integration:   ∫ f(x) dx  =  F(x) + C</text>'
        # Arrow diagram
        f'<rect x="50"  y="195" width="310" height="60" fill="#1e3a5f" rx="10" stroke="#38bdf8" stroke-width="2"/>'
        f'<text x="205" y="232" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">F(x)   derivative</text>'
        f'<line x1="360" y1="225" x2="460" y2="225" stroke="#94a3b8" stroke-width="2"/>'
        f'<polygon points="460,225 448,218 448,232" fill="#94a3b8"/>'
        f'<text x="410" y="215" fill="#38bdf8" font-family="monospace" font-size="12" text-anchor="middle">d/dx</text>'
        f'<rect x="460" y="195" width="310" height="60" fill="#14352b" rx="10" stroke="#4ade80" stroke-width="2"/>'
        f'<text x="615" y="232" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">f(x)   integral</text>'
        f'<line x1="460" y1="270" x2="360" y2="270" stroke="#94a3b8" stroke-width="2"/>'
        f'<polygon points="360,270 372,263 372,277" fill="#94a3b8"/>'
        f'<text x="410" y="290" fill="#4ade80" font-family="monospace" font-size="12" text-anchor="middle">∫ dx</text>'
        f'<text x="420" y="340" fill="#94a3b8" font-family="monospace" font-size="13" text-anchor="middle">e.g.  d/dx [x^3] = 3x^2   ↔   ∫ 3x^2 dx = x^3 + C</text>'
    )
    push(14357, 'Antiderivative: Reversing Differentiation',
         svg(inner, 'Antiderivative: Integration Undoes Differentiation', title_color='#38bdf8'))

    # ── L227 P3: Power Rule for Integration ──────────────────────────────────
    rules9 = [
        ('∫ x^n dx  =  x^(n+1) / (n+1)  +  C      (n ≠ -1)',   '#facc15'),
        ('∫ ax^n dx =  a · x^(n+1) / (n+1)  +  C',             '#38bdf8'),
        ('∫ k dx    =  kx  +  C',                                '#4ade80'),
        ('∫ (f + g) dx = ∫ f dx + ∫ g dx   (sum rule)',         '#e879f9'),
        ('ALWAYS add + C for INDEFINITE integrals!',             '#f87171'),
    ]
    inner2 = ''.join(
        f'<rect x="60" y="{62+i*50}" width="720" height="40" fill="#1e293b" rx="6" stroke="{c}" stroke-width="1.2"/>'
        f'<text x="400" y="{88+i*50}" fill="{c}" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">{t}</text>'
        for i,(t,c) in enumerate(rules9)
    )
    push(14358, 'Power Rule for Integration Formula Card',
         svg(panel(inner2, x=50, y=45, w=740, h=315, border='#facc15'),
             'Power Rule for Integration: ∫ x^n dx = x^(n+1)/(n+1) + C', title_color='#facc15'))

    # ── L227 P4: Worked Example Poly Integration ─────────────────────────────
    steps_i = [
        (80,  '∫ (3x^2 - 4x + 5) dx',                    '#facc15', 16),
        (125, '= 3 · x^3/3  -  4 · x^2/2  +  5x  +  C', '#38bdf8', 15),
        (170, '= x^3  -  2x^2  +  5x  +  C  ✓',         '#4ade80', 16),
        (225, 'Check: d/dx [x^3 - 2x^2 + 5x + C]',       '#94a3b8', 13),
        (265, '     = 3x^2 - 4x + 5  ✓  (matches!)',      '#4ade80', 14),
    ]
    inner3 = (
        ''.join(row(420, y, t, c, s) for y,t,c,s in steps_i) +
        f'<line x1="80" y1="98" x2="760" y2="98" stroke="#facc15" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<line x1="80" y1="195" x2="760" y2="195" stroke="#4ade80" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<rect x="80" y="148" width="680" height="34" fill="#14352b" rx="5" stroke="#4ade80" stroke-width="1"/>'
    )
    push(14359, 'Worked Example 1: Polynomial Indefinite Integration',
         svg(panel(inner3, x=50, y=45, w=740, h=310, border='#4ade80'),
             'Worked Example: ∫ (3x^2 - 4x + 5) dx = x^3 - 2x^2 + 5x + C',
             title_color='#4ade80'))

    # ── L227 P9: Forgetting +C Warning ──────────────────────────────────────
    push(14360, 'Common Error: Forgetting +C Warning',
         warn_svg('∫ f(x) dx = F(x)  ← WRONG — always write F(x) + C',
                  'Without + C you are claiming ONE specific antiderivative. The full answer is an infinite family of curves!'))

    # ── L228 P2: Family of Curves (+C Shift) ─────────────────────────────────
    # Draw 5 parabolas shifted vertically
    sx3 = lambda x: 80 + (x/5)*640
    sy3 = lambda y: 330 - (y/16)*270
    parabola = lambda C: ' '.join(f'{sx3(i*0.1):.1f},{sy3((i*0.1-2.5)**2+C):.1f}' for i in range(51))
    curves = [
        ('#1e3a5f','#475569', 4, 'C = +4'),
        ('#1e3a5f','#64748b', 2, 'C = +2'),
        ('#14352b','#4ade80', 0, 'C = 0  (particular)'),
        ('#1e3a5f','#64748b',-2, 'C = -2'),
        ('#1e3a5f','#475569',-4, 'C = -4'),
    ]
    inner4 = axis(80,340,730,50,'x','y') + ''.join(
        f'<polyline points="{parabola(C)}" fill="none" stroke="{sc}" stroke-width="{"3" if sc=="#4ade80" else "1.8"}" stroke-dasharray="{"none" if sc=="#4ade80" else "6 3"}"/>'
        for _,sc,C,_ in curves
    )
    # labels on right edge
    for _,sc,C,lbl in curves:
        y_right = sy3((5-2.5)**2+C)
        if 20 < y_right < 345:
            inner4 += f'<text x="735" y="{y_right:.0f}" fill="{sc}" font-family="monospace" font-size="12" font-weight="bold">{lbl}</text>'
    # highlight the C=0 curve
    inner4 += f'<circle cx="{sx3(2.5):.0f}" cy="{sy3(0):.0f}" r="7" fill="#4ade80" stroke="#fff" stroke-width="1.5"/>'
    inner4 += f'<text x="{sx3(2.5):.0f}" y="{sy3(0)-14:.0f}" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Minimum (turning pt)</text>'
    push(14361, 'Family of Antiderivative Curves (+C Vertical Shift)',
         svg(panel(inner4, x=50, y=45, w=740, h=310, border='#4ade80'),
             'Family of Antiderivative Curves — +C Shifts Curve Vertically',
             title_color='#4ade80'))

    # ── L228 P3: Particular Solution Protocol ────────────────────────────────
    ps_steps = [
        (box(90, 65, 660, 48, 'Step 1: Integrate dy/dx = f(x)  to get y = F(x) + C', fill='#1e3a5f', stroke='#38bdf8', tcolor='#93c5fd') +
         arrow(420,113,420,138,'#38bdf8')),
        (box(90,138, 660, 48, 'Step 2: Substitute boundary point (x₀, y₀)', fill='#14352b', stroke='#facc15', tcolor='#fde68a') +
         arrow(420,186,420,211,'#facc15')),
        (box(90,211, 660, 48, 'Step 3: Solve for C', fill='#3b2a10', stroke='#4ade80', tcolor='#86efac') +
         arrow(420,259,420,284,'#4ade80')),
        (box(90,284, 660, 48, 'Step 4: Write particular solution y = F(x) + C_value', fill='#2d1a4a', stroke='#a855f7', tcolor='#d8b4fe')),
    ]
    push(14362, 'Particular Solution Protocol',
         svg(panel(''.join(ps_steps), x=50, y=45, w=740, h=360, border='#38bdf8'),
             'Particular Solution: 4-Step Protocol to Find Unique Curve',
             title_color='#38bdf8', H=420))

    # ── L228 P4: Worked Example Curve Reconstruction ─────────────────────────
    steps_ps = [
        (80,  'Given: dy/dx = 3x^2 - 4,  passes through (2, 1)', '#facc15', 14),
        (125, 'Step 1: Integrate  →  y = x^3 - 4x + C',          '#38bdf8', 15),
        (170, 'Step 2: Substitute (2, 1):',                       '#94a3b8', 13),
        (210, '   1 = (2)^3 - 4(2) + C  =  8 - 8 + C  =  C',   '#38bdf8', 14),
        (248, '   C = 1',                                          '#facc15', 16),
        (290, 'Particular Solution:  y = x^3 - 4x + 1  ✓',       '#4ade80', 16),
    ]
    inner5 = (
        ''.join(row(420, y, t, c, s) for y,t,c,s in steps_ps) +
        f'<line x1="80" y1="98" x2="760" y2="98" stroke="#facc15" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<rect x="80" y="268" width="680" height="36" fill="#14352b" rx="5" stroke="#4ade80" stroke-width="1.5"/>'
        # boundary point dot
        f'<circle cx="620" cy="160" r="9" fill="#fbbf24" stroke="#fff" stroke-width="1.5"/>'
        f'<text x="636" y="155" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">(2, 1)</text>'
    )
    push(14363, 'Worked Example 1: Curve Reconstruction from dy/dx',
         svg(panel(inner5, x=50, y=45, w=740, h=310, border='#4ade80'),
             'Worked Example: dy/dx = 3x^2 - 4 passing through (2, 1) → y = x^3 - 4x + 1',
             title_color='#4ade80'))

    # ── L228 P9: Substituting into Derivative Warning ────────────────────────
    push(14364, 'Common Error: Substituting into Derivative Warning',
         warn_svg('Substitute boundary point into y = F(x) + C, NOT into dy/dx',
                  'Substituting (x₀, y₀) into the DERIVATIVE gives the gradient — not the constant C!'))

    # ── L229 P2: Definite Integral as Accumulated Area ───────────────────────
    sx4 = lambda x: 80 + (x/4)*620
    sy4 = lambda y: 310 - (y/12)*240
    f4 = lambda x: (x-1)**2 + 2  # y=(x-1)^2+2, min at x=1
    pts4 = ' '.join(f'{sx4(i*0.05):.1f},{sy4(f4(i*0.05)):.1f}' for i in range(81))
    # shaded area a=0.5 to b=3.5
    a4, b4 = 0.5, 3.5
    shade_pts = f'{sx4(a4):.0f},{sy4(0)}'
    for i in range(61):
        xv = a4 + i*(b4-a4)/60
        shade_pts += f' {sx4(xv):.1f},{sy4(f4(xv)):.1f}'
    shade_pts += f' {sx4(b4):.0f},{sy4(0)}'
    inner6 = (
        axis(80,310,710,50,'x','y') +
        f'<polygon points="{shade_pts}" fill="#38bdf8" opacity="0.25"/>'
        f'<polyline points="{pts4}" fill="none" stroke="#facc15" stroke-width="3"/>'
        f'<line x1="{sx4(a4):.0f}" y1="{sy4(0):.0f}" x2="{sx4(a4):.0f}" y2="{sy4(f4(a4)):.0f}" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="5 3"/>'
        f'<line x1="{sx4(b4):.0f}" y1="{sy4(0):.0f}" x2="{sx4(b4):.0f}" y2="{sy4(f4(b4)):.0f}" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="5 3"/>'
        f'<text x="{sx4(a4):.0f}" y="{sy4(0)+18:.0f}" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">a</text>'
        f'<text x="{sx4(b4):.0f}" y="{sy4(0)+18:.0f}" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">b</text>'
        f'<text x="420" y="{sy4(f4(2))+8:.0f}" fill="#38bdf8" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">Shaded Area = ∫ f(x)dx from a to b</text>'
        f'<text x="680" y="70" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold" text-anchor="end">y = f(x)</text>'
        f'<text x="420" y="350" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">= [F(b) - F(a)]</text>'
    )
    push(14365, 'Definite Integral as Accumulated Area Under Curve',
         svg(panel(inner6, x=50, y=45, w=740, h=320, border='#38bdf8'),
             'Definite Integral: Shaded Area = ∫ f(x)dx from a to b = F(b) - F(a)',
             title_color='#38bdf8'))

    # ── L229 P3: Split-Region Rule ────────────────────────────────────────────
    # Curve that dips below x-axis: y=x(x-3) from 0 to 4
    sx5 = lambda x: 80 + (x/5)*640
    sy5 = lambda y: 200 - y*30  # y in range -3..4
    f5 = lambda x: x*(x-3)
    pts5 = ' '.join(f'{sx5(i*0.05):.1f},{sy5(f5(i*0.05)):.1f}' for i in range(81))
    # shade above (0 to 3): below x-axis → red
    shade_neg = f'{sx5(0):.0f},{sy5(0)}'
    for i in range(61): xv=i*3/60; shade_neg += f' {sx5(xv):.1f},{sy5(f5(xv)):.1f}'
    shade_neg += f' {sx5(3):.0f},{sy5(0)}'
    # shade (3 to 4): above x-axis → green
    shade_pos = f'{sx5(3):.0f},{sy5(0)}'
    for i in range(21): xv=3+i/20; shade_pos += f' {sx5(xv):.1f},{sy5(f5(xv)):.1f}'
    shade_pos += f' {sx5(4):.0f},{sy5(0)}'
    inner7 = (
        f'<line x1="70" y1="{sy5(0)}" x2="740" y2="{sy5(0)}" stroke="#475569" stroke-width="2"/>'
        f'<line x1="80" y1="50"       x2="80"  y2="350"       stroke="#475569" stroke-width="2"/>'
        f'<polygon points="{shade_neg}" fill="#f87171" opacity="0.25"/>'
        f'<polygon points="{shade_pos}" fill="#4ade80" opacity="0.25"/>'
        f'<polyline points="{pts5}" fill="none" stroke="#facc15" stroke-width="3"/>'
        f'<circle cx="{sx5(3):.0f}" cy="{sy5(0):.0f}" r="6" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
        f'<text x="{sx5(3):.0f}" y="{sy5(0)+20:.0f}" fill="#e879f9" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">root r=3</text>'
        f'<text x="{sx5(1.5):.0f}" y="{sy5(-1.8):.0f}" fill="#f87171" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">|∫ from 0 to 3|</text>'
        f'<text x="{sx5(3.5):.0f}" y="{sy5(0.5):.0f}" fill="#4ade80" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">∫ 3 to 4</text>'
        f'<text x="680" y="68" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold">y=x(x-3)</text>'
        f'<text x="420" y="340" fill="#e2e8f0" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">Total Area = |red part| + green part</text>'
    )
    push(14366, 'Split-Region Rule: Curve Crosses x-Axis',
         svg(panel(inner7, x=50, y=45, w=740, h=310, border='#f87171'),
             'KCSE Rule: Split Integral at Root — Take |Absolute Value| Below x-Axis',
             title_color='#f87171'))

    # ── L229 P4: Worked Example Definite Integral ────────────────────────────
    steps_def = [
        (80,  'Evaluate: ∫ from 0 to 3 of (x^2 - 4x + 3) dx',    '#facc15', 14),
        (125, '= [x^3/3 - 2x^2 + 3x] from 0 to 3',               '#38bdf8', 15),
        (168, 'At x=3: (27/3 - 18 + 9) = 9 - 18 + 9 = 0',        '#38bdf8', 14),
        (208, 'At x=0: (0 - 0 + 0) = 0',                          '#38bdf8', 14),
        (250, 'Signed result = 0 - 0 = 0',                         '#f87171', 15),
        (295, 'Actual enclosed area &gt; 0 — SPLIT at roots!',      '#4ade80', 14),
    ]
    inner8 = (
        ''.join(row(420, y, t, c, s) for y,t,c,s in steps_def) +
        f'<line x1="80" y1="98" x2="760" y2="98" stroke="#facc15" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<rect x="80" y="230" width="680" height="35" fill="#1c0a0a" rx="5" stroke="#f87171" stroke-width="1"/>'
    )
    push(14367, 'Worked Example 1: Evaluating a Definite Integral',
         svg(panel(inner8, x=50, y=45, w=740, h=310, border='#38bdf8'),
             'Worked Example: ∫ from 0 to 3 of (x^2-4x+3)dx — Net vs Actual Area',
             title_color='#38bdf8'))

    # ── L229 P9: Negative Area Warning ───────────────────────────────────────
    push(14368, 'Common Error: Adding Negative Area Without Splitting',
         warn_svg('Definite integral gives SIGNED area — always split at roots!',
                  'When curve dips below x-axis, the integral is NEGATIVE. Split at f(x)=0 and take absolute values separately!'))

    # ── L230 P2: Area Between Two Curves ─────────────────────────────────────
    sx6 = lambda x: 80 + ((x+2)/7)*640
    sy6 = lambda y: 310 - (y/12)*260
    # parabola y=x^2 and line y=x+2
    pts_par = ' '.join(f'{sx6(i*0.05-2):.1f},{sy6((i*0.05-2)**2):.1f}' for i in range(121))
    pts_line = f'{sx6(-2):.0f},{sy6(0)} {sx6(5):.0f},{sy6(7)}'
    # intersections at x=-1, x=2
    shade6 = f'{sx6(-1):.0f},{sy6(1)}'
    for i in range(61):
        xv = -1 + i*3/60
        shade6 += f' {sx6(xv):.1f},{sy6(xv+2):.1f}'
    for i in range(61):
        xv = 2 - i*3/60
        shade6 += f' {sx6(xv):.1f},{sy6(xv**2):.1f}'
    inner9 = (
        axis(80,310,730,50,'x','y') +
        f'<polygon points="{shade6}" fill="#a855f7" opacity="0.25"/>'
        f'<line x1="{sx6(-2):.0f}" y1="{sy6(0):.0f}" x2="{sx6(4.5):.0f}" y2="{sy6(6.5):.0f}" stroke="#22d3ee" stroke-width="2.5"/>'
        f'<polyline points="{pts_par}" fill="none" stroke="#facc15" stroke-width="2.5"/>'
        f'<circle cx="{sx6(-1):.0f}" cy="{sy6(1):.0f}" r="7" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
        f'<circle cx="{sx6(2):.0f}"  cy="{sy6(4):.0f}" r="7" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
        f'<text x="{sx6(-1)-14:.0f}" y="{sy6(1)-12:.0f}" fill="#e879f9" font-family="monospace" font-size="13" font-weight="bold">(-1,1)</text>'
        f'<text x="{sx6(2)+8:.0f}"  y="{sy6(4)-12:.0f}" fill="#e879f9" font-family="monospace" font-size="13" font-weight="bold">(2,4)</text>'
        f'<text x="{sx6(4):.0f}" y="{sy6(5.5):.0f}" fill="#22d3ee" font-family="monospace" font-size="13" font-weight="bold">y = x+2</text>'
        f'<text x="{sx6(3.5):.0f}" y="{sy6(12):.0f}" fill="#facc15" font-family="monospace" font-size="13" font-weight="bold">y = x^2</text>'
        f'<text x="420" y="346" fill="#a855f7" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">Area = ∫ from -1 to 2 of (UPPER - LOWER) dx</text>'
    )
    push(14369, 'Area Between Two Intersecting Curves',
         svg(panel(inner9, x=50, y=45, w=740, h=320, border='#a855f7'),
             'Area Between y = x+2 (line) and y = x^2 (parabola): Integrate (Upper - Lower)',
             title_color='#a855f7'))

    # ── L230 P3: Kinematics Integration Ladder ───────────────────────────────
    inner10 = (
        kin_box(90,  80, 'a(t)', 'Acceleration', '#4ade80') +
        kin_arrow(270,112,330,112,'∫ dt','#38bdf8') +
        kin_box(330, 80, 'v(t)', 'Velocity',     '#38bdf8') +
        kin_arrow(510,112,570,112,'∫ dt','#facc15') +
        kin_box(570, 80, 's(t)', 'Displacement', '#facc15') +
        # reverse: differentiate
        kin_arrow(570,170,510,170,'d/dt','#f87171') +
        kin_arrow(330,170,270,170,'d/dt','#f87171') +
        f'<text x="420" y="228" fill="#f87171" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">← Differentiation is the REVERSE direction</text>'
        f'<text x="420" y="268" fill="#94a3b8" font-family="monospace" font-size="13" text-anchor="middle">v = ∫ a dt + C    s = ∫ v dt + C</text>'
        f'<text x="420" y="305" fill="#facc15" font-family="monospace" font-size="13" text-anchor="middle">Always include + C when integrating kinematics!</text>'
    )
    push(14370, 'Kinematics Integration Ladder (Reverse Direction)',
         svg(panel(inner10, x=50, y=45, w=740, h=295, border='#4ade80'),
             'Kinematics Integration Ladder: a(t) → v(t) → s(t) via Integration',
             title_color='#4ade80'))

    # ── L230 P4: Worked Example Area y=x^2 and y=x+2 ────────────────────────
    steps_area = [
        (80,  'Find intersections: x^2 = x + 2  →  x^2 - x - 2 = 0',  '#facc15', 14),
        (118, '(x-2)(x+1) = 0   →   x = -1  and  x = 2',              '#facc15', 14),
        (160, 'Area = ∫ from -1 to 2 of (x+2 - x^2) dx',              '#38bdf8', 15),
        (202, '= [x^2/2 + 2x - x^3/3] from -1 to 2',                  '#38bdf8', 14),
        (242, 'At x=2:  2 + 4 - 8/3 = 14/3',                          '#4ade80', 14),
        (280, 'At x=-1: 1/2 - 2 + 1/3 = -7/6',                        '#4ade80', 14),
        (318, 'Area = 14/3 - (-7/6) = 28/6 + 7/6 = 35/6 = 4.5 sq units', '#a855f7', 14),
    ]
    inner11 = (
        ''.join(row(420, y, t, c, s) for y,t,c,s in steps_area) +
        f'<line x1="80" y1="98" x2="760" y2="98" stroke="#facc15" stroke-width="1" stroke-dasharray="4 3"/>'
        f'<rect x="80" y="300" width="680" height="34" fill="#2d1a4a" rx="5" stroke="#a855f7" stroke-width="1.5"/>'
    )
    push(14371, 'Worked Example 1: Area Enclosed by y = x^2 and y = x + 2',
         svg(panel(inner11, x=50, y=45, w=740, h=320, border='#a855f7'),
             'Worked Example: Area Between y = x^2 and y = x+2 = 35/6 ≈ 4.5 sq units',
             title_color='#a855f7'))

    # ── L230 P9: Inverted Subtraction Warning ────────────────────────────────
    push(14372, 'Common Error: Inverted Curve Subtraction Order Warning',
         warn_svg('Always integrate (UPPER - LOWER) dx between intersection points',
                  'Integrating (LOWER - UPPER) gives a negative answer — the area is always POSITIVE!'))

    print('  Topic 9 done — 16 blocks updated.')


if __name__ == '__main__':
    topic8()
    topic9()
    print('\n=== ALL 32 BLOCKS FIXED SUCCESSFULLY ===')
