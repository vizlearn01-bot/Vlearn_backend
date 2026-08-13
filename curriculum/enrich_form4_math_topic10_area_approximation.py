import os, sys, django
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.core.files.base import ContentFile
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

def clean_svg(s):
    ok, san, _ = validate_and_sanitize_svg(s)
    return san if ok else s

def attach_svg(lesson, page_num, title, fname, svg):
    san = clean_svg(svg)
    block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num,
                                       block_type='suggested_diagram').first()
    if not block:
        block = LessonBlock.objects.create(
            lesson=lesson, page_number=page_num, block_type='suggested_diagram',
            title=title, component_order=1,
            metadata={'svg_content': san},
            content={'text': title, 'svg_content': san, 'svg': san}
        )
    else:
        block.title = title
        block.metadata = {**(block.metadata or {}), 'svg_content': san}
        block.content  = {**(block.content  or {}), 'svg_content': san, 'svg': san}
        block.save()

    asset = LessonAsset.objects.filter(lesson=lesson, blocks=block,
                                       source_type='ai_generated').first()
    if not asset:
        asset = LessonAsset.objects.create(
            lesson=lesson, asset_type='diagram', source_type='ai_generated',
            storage_type='file', status='approved', title=title,
            description=f'SVG: {title}', metadata={'svg_content': san}
        )
        asset.file.save(f'{fname}_{lesson.id}.svg', ContentFile(san.encode()), save=True)
        block.assets.add(asset)
    else:
        asset.title = title
        asset.metadata = {**(asset.metadata or {}), 'svg_content': san}
        asset.file.save(f'{fname}_{lesson.id}.svg', ContentFile(san.encode()), save=True)
        asset.save()
    print(f'  [Page {page_num}] SVG attached: "{title}" (Asset {asset.id})')

def fix_sim_block(lesson, page_num):
    b = LessonBlock.objects.filter(lesson=lesson, page_number=page_num).first()
    if b:
        b.block_type = 'simulation_placeholder'
        b.metadata   = {**(b.metadata or {}),
                        'simulation_key': 'math_area_approximation_explorer',
                        'archetype': 'math_area_approximation_explorer',
                        'subject': 'MATHEMATICS',
                        'concept_group': 'Area Approximation'}
        b.save()
        print(f'  [Page {page_num}] Block {b.id} -> simulation_placeholder')

# ─── SVG helpers ──────────────────────────────────────────────────────────────
BG   = '#0a0f1d'
DARK = '#0f172a'
PANEL = '#1e293b'

def wrap(inner, title, color='#facc15'):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">'
            f'<rect width="840" height="380" fill="{BG}" rx="16"/>'
            f'<text x="420" y="32" fill="{color}" font-family="system-ui,sans-serif" '
            f'font-size="17" font-weight="bold" text-anchor="middle">{title}</text>'
            f'<g transform="translate(60,50)">'
            f'<rect width="720" height="300" fill="{DARK}" rx="12" stroke="{color}" stroke-width="1.5"/>'
            f'{inner}'
            f'</g>'
            f'</svg>')

def row(y, text, color='#4ade80', size=16):
    return (f'<text x="360" y="{y}" fill="{color}" font-family="monospace" '
            f'font-size="{size}" font-weight="bold" text-anchor="middle">{text}</text>')

def warn(text):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">'
            f'<rect width="840" height="380" fill="{BG}" rx="16"/>'
            f'<g transform="translate(60,50)">'
            f'<rect width="720" height="300" fill="{PANEL}" rx="12" stroke="#f87171" stroke-width="1.5"/>'
            f'<text x="360" y="95" fill="#f87171" font-family="system-ui,sans-serif" '
            f'font-size="22" font-weight="bold" text-anchor="middle">COMMON ERROR</text>'
            f'<text x="360" y="155" fill="#fbbf24" font-family="system-ui,sans-serif" '
            f'font-size="15" font-weight="bold" text-anchor="middle">{text}</text>'
            f'</g>'
            f'</svg>')

# ─── Enrichment ───────────────────────────────────────────────────────────────
def enrich_topic10():
    print('=== ENRICHING FORM 4 MATH TOPIC 10: AREA APPROXIMATION ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=10).first()
    if not topic:
        print('ERROR: Topic 10 not found!'); return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'ERROR: Expected 4 lessons, found {len(lessons)}'); return

    l231, l232, l233, l234 = lessons[:4]

    # ── LESSON 231: Bounding Rectangles ──────────────────────────────────────
    print(f'Enriching Lesson 231: "{l231.title}"')

    attach_svg(l231, 2, 'Inner and Outer Bounding Rectangles Under a Curve', 'bounding_rects_concept',
        wrap(
            # mini-axis
            '<line x1="60" y1="250" x2="660" y2="250" stroke="#475569" stroke-width="2"/>'
            '<line x1="60" y1="30" x2="60" y2="255" stroke="#475569" stroke-width="2"/>'
            # curve: rough parabola y=x^2 from 0 to 4 (scaled)
            '<polyline points="60,250 165,200 270,155 375,115 480,80 585,50 660,25" '
            '  fill="none" stroke="#facc15" stroke-width="3"/>'
            # 3 lower rectangles (blue)
            '<rect x="60"  y="200" width="100" height="50" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>'
            '<rect x="160" y="155" width="100" height="95" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>'
            '<rect x="260" y="115" width="100" height="135" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>'
            # 3 upper rectangles (red outline only)
            '<rect x="60"  y="155" width="100" height="45" fill="#f87171" opacity="0.18" stroke="#f87171" stroke-width="1.5" stroke-dasharray="5 3"/>'
            '<rect x="160" y="115" width="100" height="40" fill="#f87171" opacity="0.18" stroke="#f87171" stroke-width="1.5" stroke-dasharray="5 3"/>'
            '<rect x="260" y="80"  width="100" height="35" fill="#f87171" opacity="0.18" stroke="#f87171" stroke-width="1.5" stroke-dasharray="5 3"/>'
            # labels
            '<text x="360" y="275" fill="#38bdf8" font-family="system-ui,sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Lower Bound (underestimate)</text>'
            '<text x="360" y="295" fill="#f87171" font-family="system-ui,sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Upper Bound (overestimate)</text>'
            '<text x="660" y="16"  fill="#facc15" font-family="system-ui,sans-serif" font-size="14" font-weight="bold" text-anchor="end">y = f(x)</text>'
            '<text x="62"  y="22"  fill="#4ade80" font-family="system-ui,sans-serif" font-size="14" font-weight="bold">y</text>'
            '<text x="665" y="255" fill="#4ade80" font-family="system-ui,sans-serif" font-size="14" font-weight="bold">x</text>',
            'Inner and Outer Bounding Rectangles: Lower and Upper Bound Squeeze'
        )
    )

    attach_svg(l231, 3, 'Rectangular Bounds and Limit Definition Formula', 'bounding_rects_formula',
        wrap(
            row( 80, 'Lower Bound = sum of MIN heights x strip width', '#38bdf8', 14) +
            row(120, 'Upper Bound = sum of MAX heights x strip width', '#f87171', 14) +
            row(165, 'Lower Bound &lt; Exact Area &lt; Upper Bound',   '#4ade80', 16) +
            row(215, 'As n increases: strips narrower, both bounds converge!', '#facc15', 13),
            'Rectangular Bounds Formula: Squeezing to Exact Area'
        )
    )

    attach_svg(l231, 4, 'Worked Example 1: Grid Square Counting and Rectangular Bounds', 'worked_eg_grid_counting',
        wrap(
            row( 80, 'Given: y = x^2 + 1, x in [0, 3], n = 3 strips', '#facc15') +
            row(130, 'h = (3 - 0)/3 = 1',                               '#38bdf8') +
            row(175, 'Lower bound = 1(1) + 1(2) + 1(5) = 8 sq units',  '#38bdf8') +
            row(220, 'Upper bound = 1(2) + 1(5) + 1(10) = 17 sq units', '#f87171') +
            row(265, 'True area lies between 8 and 17',                  '#4ade80', 14),
            'Worked Example 1: Grid Square Counting and Rectangular Bounds'
        )
    )

    attach_svg(l231, 9, 'Common Error: Inverting Bounds for Decreasing Functions',
               'misconception_inverted_bounds',
               warn('For DECREASING f(x): LEFT endpoint gives UPPER bound and RIGHT gives LOWER bound. Always evaluate the function, do not assume direction.'))

    fix_sim_block(l231, 8)

    # ── LESSON 232: Trapezium Rule ────────────────────────────────────────────
    print(f'Enriching Lesson 232: "{l232.title}"')

    attach_svg(l232, 2, 'Trapezium Rule: Straight-Ramp Approximation Under a Curve', 'trapezium_concept',
        wrap(
            '<line x1="60" y1="250" x2="660" y2="250" stroke="#475569" stroke-width="2"/>'
            '<line x1="60" y1="30"  x2="60"  y2="255" stroke="#475569" stroke-width="2"/>'
            # curve
            '<polyline points="60,220 210,160 360,120 510,90 660,70" '
            '  fill="none" stroke="#facc15" stroke-width="3"/>'
            # 3 trapezia (green filled)
            '<polygon points="60,250 60,220 210,160 210,250" fill="#10b981" opacity="0.30" stroke="#10b981" stroke-width="1.5"/>'
            '<polygon points="210,250 210,160 360,120 360,250" fill="#10b981" opacity="0.30" stroke="#10b981" stroke-width="1.5"/>'
            '<polygon points="360,250 360,120 510,90 510,250" fill="#10b981" opacity="0.30" stroke="#10b981" stroke-width="1.5"/>'
            # ordinate lines
            '<line x1="60"  y1="220" x2="60"  y2="250" stroke="#e879f9" stroke-width="2"/>'
            '<line x1="210" y1="160" x2="210" y2="250" stroke="#e879f9" stroke-width="2"/>'
            '<line x1="360" y1="120" x2="360" y2="250" stroke="#e879f9" stroke-width="2"/>'
            '<line x1="510" y1="90"  x2="510" y2="250" stroke="#e879f9" stroke-width="2"/>'
            # ordinate labels
            '<text x="57"  y="215" fill="#e879f9" font-family="monospace" font-size="13" text-anchor="end">y0</text>'
            '<text x="207" y="155" fill="#e879f9" font-family="monospace" font-size="13" text-anchor="end">y1</text>'
            '<text x="357" y="115" fill="#e879f9" font-family="monospace" font-size="13" text-anchor="end">y2</text>'
            '<text x="507" y="85"  fill="#e879f9" font-family="monospace" font-size="13" text-anchor="end">y3</text>'
            '<text x="660" y="62"  fill="#facc15" font-family="monospace" font-size="13" text-anchor="end">y = f(x)</text>'
            '<text x="360" y="285" fill="#4ade80" font-family="system-ui,sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Area = h x [1/2(y0 + yn) + y1 + y2 + ... + yn-1]</text>',
            'Trapezium Rule: Straight-Ramp Trapezia with Ordinate Labels y0, y1, y2, y3'
        )
    )

    attach_svg(l232, 3, 'Trapezium Rule Formula and Ordinate Rules', 'trapezium_formula',
        wrap(
            row( 75, 'Area = h x [ 1/2(y0 + yn) + y1 + y2 + ... + yn-1 ]', '#facc15', 15) +
            row(130, 'h = (b - a) / n   (strip width)',                       '#38bdf8') +
            row(175, 'n strips gives (n+1) ordinates: y0, y1, ..., yn',      '#4ade80', 14) +
            row(225, 'First and last ordinate halved, all middle ones full',  '#e879f9', 13),
            'Trapezium Rule Formula: h x [Half First and Last + All Middle Ordinates]'
        )
    )

    attach_svg(l232, 4, 'Worked Example 1: Trapezium Rule for y = x^2 - 2x + 5', 'worked_eg_trapezium',
        wrap(
            row( 75, 'f(x) = x^2 - 2x + 5, x in [1, 3], n = 4 strips',  '#facc15', 14) +
            row(118, 'h = (3-1)/4 = 0.5',                                 '#38bdf8') +
            row(158, 'y0=4, y1=3.25, y2=3, y3=3.25, y4=4',               '#e879f9', 14) +
            row(200, 'Area = 0.5 x [1/2(4+4) + 3.25 + 3 + 3.25]',       '#38bdf8') +
            row(242, '= 0.5 x [4 + 9.5] = 0.5 x 13.5 = 6.75 sq units',  '#4ade80'),
            'Worked Example 1: Trapezium Rule for y = x^2 - 2x + 5, x in [1,3]'
        )
    )

    attach_svg(l232, 9, 'Common Error: Strip Count vs Ordinate Count Off-By-One',
               'misconception_trapezium_count',
               warn('n strips gives (n+1) ordinates, not n. With 4 strips you need y0, y1, y2, y3, y4 which is five values. Off-by-one loses all marks.'))

    fix_sim_block(l232, 8)

    # ── LESSON 233: Mid-Ordinate Rule ─────────────────────────────────────────
    print(f'Enriching Lesson 233: "{l233.title}"')

    attach_svg(l233, 2, 'Mid-Ordinate Rule: Sampling at Strip Midpoints', 'mid_ordinate_concept',
        wrap(
            '<line x1="60" y1="255" x2="660" y2="255" stroke="#475569" stroke-width="2"/>'
            '<line x1="60" y1="30"  x2="60"  y2="258" stroke="#475569" stroke-width="2"/>'
            # curve
            '<polyline points="60,230 185,175 310,130 435,95 560,70 660,52" '
            '  fill="none" stroke="#facc15" stroke-width="3"/>'
            # 4 mid-ordinate rectangles (purple)
            '<rect x="60"  y="200" width="150" height="55"  fill="#a855f7" opacity="0.25" stroke="#a855f7" stroke-width="1.5"/>'
            '<rect x="210" y="152" width="150" height="103" fill="#a855f7" opacity="0.25" stroke="#a855f7" stroke-width="1.5"/>'
            '<rect x="360" y="115" width="150" height="140" fill="#a855f7" opacity="0.25" stroke="#a855f7" stroke-width="1.5"/>'
            '<rect x="510" y="85"  width="150" height="170" fill="#a855f7" opacity="0.25" stroke="#a855f7" stroke-width="1.5"/>'
            # midpoint dots
            '<circle cx="135" cy="200" r="6" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
            '<circle cx="285" cy="152" r="6" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
            '<circle cx="435" cy="115" r="6" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
            '<circle cx="585" cy="85"  r="6" fill="#e879f9" stroke="#fff" stroke-width="1.5"/>'
            # strip midpoint labels
            '<text x="135"  y="275" fill="#e879f9" font-family="monospace" font-size="12" text-anchor="middle">m1</text>'
            '<text x="285"  y="275" fill="#e879f9" font-family="monospace" font-size="12" text-anchor="middle">m2</text>'
            '<text x="435"  y="275" fill="#e879f9" font-family="monospace" font-size="12" text-anchor="middle">m3</text>'
            '<text x="585"  y="275" fill="#e879f9" font-family="monospace" font-size="12" text-anchor="middle">m4</text>'
            '<text x="360"  y="295" fill="#4ade80" font-family="system-ui,sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Area = h x (m1 + m2 + m3 + m4)</text>'
            '<text x="660"  y="45"  fill="#facc15" font-family="monospace" font-size="13" text-anchor="end">y = f(x)</text>',
            'Mid-Ordinate Rule: Evaluate f(x) at Midpoint of Each Strip m1, m2, m3, m4'
        )
    )

    attach_svg(l233, 3, 'Mid-Ordinate Rule Formula', 'mid_ordinate_formula',
        wrap(
            row( 80, 'Area = h x (m1 + m2 + ... + mn)',                  '#facc15', 18) +
            row(135, 'where mi = f( xi-1 + h/2 ) = midpoint of strip i', '#38bdf8', 14) +
            row(185, 'h = (b - a) / n   (strip width)',                   '#4ade80') +
            row(240, 'Natural error cancellation: over + under ~ 0',      '#e879f9', 14),
            'Mid-Ordinate Rule Formula: h x (m1 + m2 + ... + mn)'
        )
    )

    attach_svg(l233, 4, 'Worked Example 1: Mid-Ordinate Rule for y = x^2 + 3', 'worked_eg_mid_ordinate',
        wrap(
            row( 75, 'f(x) = x^2 + 3, x in [0, 4], n = 4 strips',  '#facc15', 14) +
            row(118, 'h = (4-0)/4 = 1',                              '#38bdf8') +
            row(160, 'Midpoints: x = 0.5, 1.5, 2.5, 3.5',           '#e879f9', 14) +
            row(200, 'm1=3.25, m2=5.25, m3=9.25, m4=15.25',         '#e879f9', 14) +
            row(242, 'Area = 1 x (3.25+5.25+9.25+15.25) = 33.0',   '#4ade80'),
            'Worked Example 1: Mid-Ordinate Rule for y = x^2 + 3, x in [0,4]'
        )
    )

    attach_svg(l233, 9, 'Common Error: Using Right-Hand Boundaries Instead of Midpoints',
               'misconception_midordinate',
               warn('Mid-Ordinate Rule uses midpoints of each strip, not left or right endpoints. Midpoint of strip i = (xi-1 + xi) / 2'))

    fix_sim_block(l233, 8)

    # ── LESSON 234: Comparative Error Analysis ───────────────────────────────
    print(f'Enriching Lesson 234: "{l234.title}"')

    attach_svg(l234, 2, 'Concavity and Error Bounds: Trapezium vs Mid-Ordinate', 'concavity_error_bounds',
        wrap(
            row( 75, 'CONCAVE UP (convex) curve:',                    '#facc15', 15) +
            row(110, 'Trapezium OVERESTIMATES',                        '#f87171', 14) +
            row(140, 'Mid-Ordinate UNDERESTIMATES',                    '#38bdf8', 14) +
            row(185, 'CONCAVE DOWN (concave) curve:',                  '#facc15', 15) +
            row(220, 'Trapezium UNDERESTIMATES',                       '#38bdf8', 14) +
            row(250, 'Mid-Ordinate OVERESTIMATES',                     '#f87171', 14) +
            row(285, 'More strips always reduces error for both!',     '#4ade80', 13),
            'Concavity and Error Bounds: Trapezium vs Mid-Ordinate Comparison'
        )
    )

    attach_svg(l234, 3, 'Comparative Error Analysis Formula Reference', 'error_analysis_formula',
        wrap(
            row( 80, 'Exact area (by integration) = E',                     '#4ade80', 16) +
            row(130, 'Trapezium error = abs(T - E)',                          '#f87171', 15) +
            row(175, 'Mid-Ordinate error = abs(M - E)',                       '#e879f9', 15) +
            row(220, 'Percentage error = abs(approx - exact) / exact x 100%','#facc15', 13) +
            row(265, 'Mid-Ordinate often has LESS error than Trapezium',      '#38bdf8', 13),
            'Comparative Error Analysis Formula Reference'
        )
    )

    attach_svg(l234, 4, 'Worked Example 1: Comparing Trapezium and Mid-Ordinate for y = x^2 + 2', 'worked_eg_comparison',
        wrap(
            row( 70, 'f(x) = x^2 + 2, x in [0, 2], n = 4',              '#facc15', 14) +
            row(108, 'Exact integral = [x^3/3 + 2x] from 0 to 2 = 6.667','#4ade80', 13) +
            row(148, 'Trapezium: 6.750  Error = 0.083',                  '#f87171') +
            row(190, 'Mid-Ordinate: 6.625  Error = 0.042',               '#e879f9') +
            row(235, 'Mid-Ordinate is more accurate here (concave up)',   '#38bdf8', 13) +
            row(272, 'Mid-Ord error is approximately half Trapezium error!','#4ade80', 13),
            'Worked Example 1: Trapezium vs Mid-Ordinate Error for y = x^2 + 2'
        )
    )

    attach_svg(l234, 9, 'Common Error: Misinterpreting Concavity and Over/Underestimation',
               'misconception_concavity',
               warn('For concave-UP curves Trapezium OVERESTIMATES. For concave-DOWN it UNDERESTIMATES. Mid-Ordinate is always the opposite. Do not mix these up.'))

    fix_sim_block(l234, 8)

    print('\n=== TOPIC 10 ENRICHMENT COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic10()
