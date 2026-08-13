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
    block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type='suggested_diagram').first()
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

    asset = LessonAsset.objects.filter(lesson=lesson, blocks=block, source_type='ai_generated').first()
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
        b.metadata   = {**(b.metadata or {}), 'simulation_key': 'math_integration_explorer',
                        'archetype': 'math_integration_explorer', 'subject': 'MATHEMATICS',
                        'concept_group': 'Integration'}
        b.save()
        print(f'  [Page {page_num}] Block {b.id} → simulation_placeholder')

# ── SVG helpers ────────────────────────────────────────────────────────────────
BG  = '#0a0f1d'
CARD = '#0f172a'
DARK = '#1e293b'

def header_svg(title, color='#38bdf8'):
    return f'<text x="420" y="35" fill="{color}" font-family="system-ui,sans-serif" font-size="20" font-weight="bold" text-anchor="middle">{title}</text>'

def wrap(inner, title, color='#38bdf8'):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">'
            f'<rect width="840" height="380" fill="{BG}" rx="16"/>'
            f'{header_svg(title, color)}'
            f'<g transform="translate(60,60)">'
            f'<rect width="720" height="290" fill="{DARK}" rx="12" stroke="{color}" stroke-width="1.5"/>'
            f'{inner}'
            f'</g>'
            f'</svg>')

def row(y, text, color='#4ade80', size=17):
    return f'<text x="360" y="{y}" fill="{color}" font-family="monospace" font-size="{size}" font-weight="bold" text-anchor="middle">{text}</text>'

def warn(text):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">'
            f'<rect width="840" height="380" fill="{BG}" rx="16"/>'
            f'<g transform="translate(60,60)">'
            f'<rect width="720" height="290" fill="{DARK}" rx="12" stroke="#f87171" stroke-width="1.5"/>'
            f'<text x="360" y="155" fill="#f87171" font-family="system-ui,sans-serif" font-size="15" font-weight="bold" text-anchor="middle">{text}</text>'
            f'</g>'
            f'</svg>')

# ── Enrichment ─────────────────────────────────────────────────────────────────
def enrich_topic9():
    print('=== ENRICHING FORM 4 MATH TOPIC 9: INTEGRATION ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=9).first()
    if not topic:
        print('ERROR: Topic 9 not found!'); return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'ERROR: Expected 4 lessons, found {len(lessons)}'); return

    l227, l228, l229, l230 = lessons[:4]

    # ── LESSON 227: Antiderivatives & Indefinite Integration ──────────────────
    print(f'Enriching Lesson 227: "{l227.title}"')

    attach_svg(l227, 2, 'Antiderivative: Reversing Differentiation', 'antiderivative_intro',
        wrap(
            row(100, 'Differentiation:  d/dx [ F(x) ] = f(x)',  '#38bdf8') +
            row(150, '⟺',                                        '#64748b', 22) +
            row(200, 'Integration:  ∫ f(x) dx  =  F(x) + C',   '#4ade80'),
            'Antiderivative: Reversing Differentiation (Indefinite Integration)'
        )
    )

    attach_svg(l227, 3, 'Power Rule for Integration Formula Card', 'integration_power_rule',
        wrap(
            row( 85, '∫ xⁿ dx  =  xⁿ⁺¹ / (n+1)  + C        (n ≠ −1)', '#facc15') +
            row(135, '∫ aˣⁿ dx  =  a · xⁿ⁺¹ / (n+1)  + C',             '#38bdf8') +
            row(185, '∫ k dx  =  kx + C',                                 '#4ade80') +
            row(235, 'Always add +C for INDEFINITE integrals!',           '#f87171', 14),
            'Power Rule for Integration Formula Card'
        )
    )

    attach_svg(l227, 4, 'Worked Example 1: Polynomial Indefinite Integration', 'worked_eg_poly_integral',
        wrap(
            row( 95, '∫ (3x² − 4x + 5) dx', '#facc15') +
            row(145, '= 3 · x³/3  −  4 · x²/2  +  5x  + C', '#38bdf8') +
            row(195, '= x³ − 2x² + 5x + C ✓', '#4ade80'),
            'Worked Example 1: Polynomial Indefinite Integration'
        )
    )

    attach_svg(l227, 9, 'Common Error: Forgetting +C Warning',
               'misconception_no_C',
               warn('∫ f(x) dx = F(x)  ← WRONG!  Always write F(x) + C for indefinite integrals!'))

    fix_sim_block(l227, 8)

    # ── LESSON 228: Particular Solutions & Boundary Conditions ────────────────
    print(f'Enriching Lesson 228: "{l228.title}"')

    attach_svg(l228, 2, 'Family of Antiderivative Curves (+C Vertical Shift)', 'family_curves_C',
        wrap(
            row( 95, 'F(x) + 2',  '#64748b', 14) +
            row(125, 'F(x) + 1',  '#64748b', 14) +
            row(155, 'F(x)   ← Particular curve (C found from boundary)', '#22d3ee', 13) +
            row(185, 'F(x) − 1',  '#64748b', 14) +
            row(215, 'All curves have the same gradient function f(x)', '#4ade80', 14),
            'Family of Antiderivative Curves — +C Shifts Curve Vertically'
        )
    )

    attach_svg(l228, 3, 'Particular Solution Protocol', 'particular_solution_protocol',
        wrap(
            row( 90, 'Step 1: Integrate  dy/dx = f(x)  ->  y = F(x) + C',   '#38bdf8') +
            row(140, 'Step 2: Substitute boundary point (x0, y0)',             '#facc15') +
            row(190, 'Step 3: Solve for C  ->  Particular Solution Found!',   '#4ade80'),
            'Particular Solution Protocol: Boundary Condition Anchoring'
        )
    )

    attach_svg(l228, 4, 'Worked Example 1: Curve Reconstruction from dy/dx', 'worked_eg_particular',
        wrap(
            row( 90, 'Given: dy/dx = 3x^2 - 4,  passing through (2, 1)', '#facc15') +
            row(140, 'Integrate: y = x^3 - 4x + C',                       '#38bdf8') +
            row(190, 'Substitute: 1 = 8 - 8 + C  =>  C = 1',              '#4ade80') +
            row(240, 'Particular Solution: y = x^3 - 4x + 1',             '#22d3ee'),
            'Worked Example 1: Curve Reconstruction from dy/dx'
        )
    )

    attach_svg(l228, 9, 'Common Error: Substituting into Derivative Warning',
               'misconception_sub_into_deriv',
               warn('Substitute boundary point into y = F(x) + C, NOT into dy/dx!'))

    fix_sim_block(l228, 8)

    # ── LESSON 229: Definite Integration & Area Under Curves ─────────────────
    print(f'Enriching Lesson 229: "{l229.title}"')

    attach_svg(l229, 2, 'Definite Integral as Accumulated Area Under Curve', 'definite_integral_area',
        wrap(
            row( 90, 'Int_a^b f(x) dx  =  [F(x)] from a to b  =  F(b) - F(a)', '#facc15') +
            row(145, 'Infinitesimal vertical strip width: dx -> 0',              '#38bdf8', 15) +
            row(195, 'Sum of strip areas = Exact definite integral',             '#4ade80', 15),
            'Definite Integral as Accumulated Area: F(b) - F(a)'
        )
    )

    attach_svg(l229, 3, 'Split-Region Rule: Curve Crosses x-Axis', 'split_region_rule',
        wrap(
            row( 85, 'If curve dips BELOW x-axis between [a, b]:',    '#facc15') +
            row(130, 'Split integral at root r where f(r) = 0',         '#38bdf8') +
            row(175, 'Area = |Int_a^r f(x)dx|  +  |Int_r^b f(x)dx|',  '#4ade80') +
            row(225, 'Take ABSOLUTE values of each part separately!',  '#f87171', 14),
            'KCSE Rule: Split-Region Absolute Area When Curve Crosses x-Axis'
        )
    )

    attach_svg(l229, 4, 'Worked Example 1: Evaluating a Definite Integral', 'worked_eg_definite',
        wrap(
            row( 90, 'Int from 0 to 3: (x^2 - 4x + 3) dx',         '#facc15') +
            row(140, '= [x^3/3 - 2x^2 + 3x] from 0 to 3',           '#38bdf8') +
            row(190, '= (9 - 18 + 9) - (0) = 0',                     '#4ade80') +
            row(240, 'Note: Net signed area = 0, but enclosed area is NOT 0!', '#f87171', 13),
            'Worked Example 1: Evaluating a Definite Integral from 0 to 3'
        )
    )

    attach_svg(l229, 9, 'Common Error: Adding Negative Area Without Splitting',
               'misconception_neg_area',
               warn('Int gives SIGNED area. When curve is BELOW x-axis, SPLIT at roots and take absolute values!'))

    fix_sim_block(l229, 8)

    # ── LESSON 230: Area Between Curves & Kinematics ──────────────────────────
    print(f'Enriching Lesson 230: "{l230.title}"')

    attach_svg(l230, 2, 'Area Between Two Intersecting Curves', 'area_between_curves',
        wrap(
            row( 90, 'Step 1: Find intersections f(x) = g(x)  =>  x = x1 and x = x2', '#facc15') +
            row(145, 'Step 2: Identify which curve is on TOP in [x1, x2]',                '#38bdf8') +
            row(200, 'Step 3: Area = Int from x1 to x2 of (UPPER - LOWER) dx',           '#4ade80'),
            'Area Between Two Intersecting Curves'
        )
    )

    attach_svg(l230, 3, 'Kinematics Integration Ladder (Reverse Direction)', 'kinematics_integration_ladder',
        wrap(
            row(100, 'Acceleration a(t)  ─ ∫ dt →  Velocity v(t)',   '#facc15') +
            row(160, 'Velocity v(t)      ─ ∫ dt →  Displacement s(t)', '#38bdf8') +
            row(220, 'Opposite direction to differentiation!',          '#4ade80'),
            'Kinematics Integration Ladder: a(t) → v(t) → s(t)'
        )
    )

    attach_svg(l230, 4, 'Worked Example 1: Area Enclosed by y = x² and y = x + 2', 'worked_eg_area_between',
        wrap(
            row( 80, 'Intersections: x² = x + 2  →  x = −1, x = 2',       '#facc15') +
            row(130, 'Area = Int from -1 to 2 of (x + 2 - x^2) dx',           '#38bdf8') +
            row(180, '= [x^2/2 + 2x - x^3/3] from -1 to 2',                  '#38bdf8') +
            row(230, '= (2 + 4 - 8/3) - (1/2 - 2 + 1/3)  =  4.5 sq units',  '#4ade80'),
            'Worked Example 1: Area Enclosed Between y = x² and y = x + 2'
        )
    )

    attach_svg(l230, 9, 'Common Error: Inverted Curve Subtraction Order Warning',
               'misconception_inverted_subtraction',
               warn('Always integrate (UPPER − LOWER). Reversing to (LOWER − UPPER) gives negative area!'))

    fix_sim_block(l230, 8)

    print('\n=== TOPIC 9 ENRICHMENT COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic9()
