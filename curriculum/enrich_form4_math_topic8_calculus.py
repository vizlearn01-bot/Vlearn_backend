import os
import sys
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.core.files.base import ContentFile
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

def clean_svg(svg_code):
    is_valid, sanitized, err = validate_and_sanitize_svg(svg_code)
    return sanitized if is_valid else svg_code

def create_or_update_svg_block(lesson, page_num, title, filename_base, svg_string):
    sanitized = clean_svg(svg_string)
    
    block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type='suggested_diagram').first()
    if not block:
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=page_num,
            block_type='suggested_diagram',
            title=title,
            component_order=1,
            metadata={'svg_content': sanitized},
            content={'text': title, 'svg_content': sanitized, 'svg': sanitized}
        )
    else:
        block.title = title
        if not block.metadata:
            block.metadata = {}
        block.metadata['svg_content'] = sanitized
        if not isinstance(block.content, dict):
            block.content = {}
        block.content['svg_content'] = sanitized
        block.content['svg'] = sanitized
        block.save()

    asset = LessonAsset.objects.filter(lesson=lesson, blocks=block, source_type='ai_generated').first()
    if not asset:
        asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type='diagram',
            source_type='ai_generated',
            storage_type='file',
            status='approved',
            title=title,
            description=f'Sanitized vector diagram: {title}',
            metadata={'svg_content': sanitized}
        )
        asset.file.save(f'{filename_base}_{lesson.id}.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        block.assets.add(asset)
    else:
        asset.title = title
        if not asset.metadata:
            asset.metadata = {}
        asset.metadata['svg_content'] = sanitized
        asset.file.save(f'{filename_base}_{lesson.id}.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        asset.save()
    print(f'  [Page {page_num}] SVG saved & attached: "{title}" (Asset {asset.id})')
    return asset

def enrich_topic8_calculus():
    print('=== ENRICHING FORM 4 MATH TOPIC 8: DIFFERENTIATION ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=8).first()
    if not topic:
        print('Error: Topic 8 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 8, found {len(lessons)}')
        return

    l223, l224, l225, l226 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 223: Rates of Change & Derivative from First Principles
    # =========================================================================
    if l223:
        print(f'Enriching Lesson 223: "{l223.title}"')

        # P2 SVG: Secant-to-Tangent Limit Process (h -> 0)
        svg_223_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Secant-to-Tangent Limit Process (h ➔ 0)</text>
  <g transform="translate(60, 60)">
    <rect width="720" height="320" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Secant Chord Slope Δy/Δx = (f(x+h) - f(x)) / h</text>
    <text x="360" y="190" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Lim (h ➔ 0) [Secant Slope] = Tangent Gradient f'(x)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l223, 2, 'Secant-to-Tangent Limit Process (h ➔ 0)', 'secant_to_tangent_limit', svg_223_p2)

        # P3 SVG: First Principles Definition Flowchart
        svg_223_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">First Principles Definition Flowchart</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">f'(x) = lim_{h ➔ 0} [ (f(x+h) - f(x)) / h ]</text>
  </g>
</svg>"""
        create_or_update_svg_block(l223, 3, 'First Principles Definition Flowchart', 'first_principles_flowchart', svg_223_p3)

        # P4 SVG: Worked Example 1 - First Principles Expansion (y = x^2)
        svg_223_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: First Principles Expansion (y = x²)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="120" fill="#facc15" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">f(x+h) - f(x) = (x+h)² - x² = 2xh + h²</text>
    <text x="360" y="170" fill="#4ade80" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">Divide by h: (2xh + h²)/h = 2x + h ➔ 2x (as h ➔ 0)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l223, 4, 'Worked Example 1: First Principles Expansion (y = x²)', 'worked_example_first_principles_x2', svg_223_p4)

        # P9 SVG: Common Misconception - Binomial Expansion Distribution
        svg_223_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Binomial Expansion Distribution Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">(x+h)² = x² + 2xh + h²  ≠  x² + h²  (Do NOT omit middle term 2xh!)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l223, 9, 'Common Error: Binomial Expansion Warning', 'misconception_binomial_expansion', svg_223_p9)

        # Fix Block 13856 (Page 8)
        block_sim223 = LessonBlock.objects.filter(lesson=l223, page_number=8).first()
        if block_sim223:
            block_sim223.block_type = 'simulation_placeholder'
            meta = block_sim223.metadata or {}
            meta['simulation_key'] = 'math_differentiation_explorer'
            meta['archetype'] = 'math_differentiation_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Differentiation'
            block_sim223.metadata = meta
            block_sim223.save()
            print(f'  [Page 8] Updated Block {block_sim223.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 224: Polynomial Differentiation Mechanics and Power Rule
    # =========================================================================
    if l224:
        print(f'Enriching Lesson 224: "{l224.title}"')

        # P2 SVG: Power Rule Derivative Transformation
        svg_224_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Power Rule Derivative Transformation</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle">d/dx [ a · xⁿ ] = (a · n) · xⁿ⁻¹</text>
  </g>
</svg>"""
        create_or_update_svg_block(l224, 2, 'Power Rule Derivative Transformation', 'power_rule_transformation', svg_224_p2)

        # P3 SVG: Power Rule Cheat Sheet & Exponent Rules
        svg_224_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Power Rule Cheat Sheet &amp; Exponent Rules</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1. Negative Powers: d/dx [ x⁻ⁿ ] = -n · x⁻ⁿ⁻¹</text>
    <text x="360" y="150" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">2. Fractional Powers: d/dx [ x^(1/n) ] = (1/n) · x^(1/n - 1)</text>
    <text x="360" y="200" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">3. Constants: d/dx [ c ] = 0</text>
  </g>
</svg>"""
        create_or_update_svg_block(l224, 3, 'Power Rule Cheat Sheet & Exponent Rules', 'power_rule_cheat_sheet', svg_224_p3)

        # P4 SVG: Worked Example 1 - Polynomial Term-by-Term Differentiation
        svg_224_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Polynomial Term-by-Term Differentiation</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="120" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">y = 3x⁴ - 5x² + 7x - 9</text>
    <text x="360" y="170" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">dy/dx = 12x³ - 10x + 7</text>
  </g>
</svg>"""
        create_or_update_svg_block(l224, 4, 'Worked Example 1: Polynomial Differentiation', 'worked_example_polynomial_differentiation', svg_224_p4)

        # P9 SVG: Common Misconception - Differentiating Constants
        svg_224_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Differentiating Constants Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">d/dx [ constant ] = 0  (Do NOT write constant unchanged!)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l224, 9, 'Common Error: Differentiating Constants Warning', 'misconception_differentiating_constants', svg_224_p9)

        # Fix Block 13867 (Page 8)
        block_sim224 = LessonBlock.objects.filter(lesson=l224, page_number=8).first()
        if block_sim224:
            block_sim224.block_type = 'simulation_placeholder'
            meta = block_sim224.metadata or {}
            meta['simulation_key'] = 'math_differentiation_explorer'
            meta['archetype'] = 'math_differentiation_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Differentiation'
            block_sim224.metadata = meta
            block_sim224.save()
            print(f'  [Page 8] Updated Block {block_sim224.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 225: Tangents, Normals, and Stationary Turning Points
    # =========================================================================
    if l225:
        print(f'Enriching Lesson 225: "{l225.title}"')

        # P2 SVG: Tangent, Normal & Turning Point Geometry
        svg_225_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Tangent, Normal Line &amp; Turning Point Geometry</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="120" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Tangent Slope m_T = f'(x₀)  |  Normal Slope m_N = -1 / m_T</text>
    <text x="360" y="180" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Stationary Turning Points: f'(x) = 0 (Horizontal Tangent)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l225, 2, 'Tangent, Normal & Turning Point Geometry', 'tangent_normal_geometry', svg_225_p2)

        # P3 SVG: Stationary Point Classification Test
        svg_225_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Stationary Point Classification Test</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1. Local Maximum: f'(x) sign change  [ + ➔ 0 ➔ - ]</text>
    <text x="360" y="150" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">2. Local Minimum: f'(x) sign change  [ - ➔ 0 ➔ + ]</text>
    <text x="360" y="200" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">3. Point of Inflexion: f'(x) sign unchanged  [ + ➔ 0 ➔ + ]</text>
  </g>
</svg>"""
        create_or_update_svg_block(l225, 3, 'Stationary Point Classification Test', 'stationary_point_classification', svg_225_p3)

        # P4 SVG: Worked Example 1 - Tangent & Normal Equations
        svg_225_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Tangent &amp; Normal Equations at x₀</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="120" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Tangent Line: y - y₀ = m_T (x - x₀)</text>
    <text x="360" y="170" fill="#e879f9" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Normal Line: y - y₀ = (-1 / m_T) (x - x₀)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l225, 4, 'Worked Example 1: Tangent & Normal Equations', 'worked_example_tangent_normal', svg_225_p4)

        # P9 SVG: Common Misconception - Derivative Substitution Inversion
        svg_225_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Derivative Substitution Inversion Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Substitute x₀ into dy/dx for slope m_T, NOT into original y equation!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l225, 9, 'Common Error: Derivative Substitution Warning', 'misconception_derivative_substitution', svg_225_p9)

        # Fix Block 13878 (Page 8)
        block_sim225 = LessonBlock.objects.filter(lesson=l225, page_number=8).first()
        if block_sim225:
            block_sim225.block_type = 'simulation_placeholder'
            meta = block_sim225.metadata or {}
            meta['simulation_key'] = 'math_differentiation_explorer'
            meta['archetype'] = 'math_differentiation_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Differentiation'
            block_sim225.metadata = meta
            block_sim225.save()
            print(f'  [Page 8] Updated Block {block_sim225.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 226: Kinematics Applications and Real-World Optimization
    # =========================================================================
    if l226:
        print(f'Enriching Lesson 226: "{l226.title}"')

        # P2 SVG: Kinematics Differentiation Ladder
        svg_226_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Kinematics Differentiation Ladder</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="110" fill="#38bdf8" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">Displacement s(t)</text>
    <text x="360" y="160" fill="#4ade80" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">⬇ d/dt ➔ Velocity v(t) = ds/dt</text>
    <text x="360" y="210" fill="#facc15" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">⬇ d/dt ➔ Acceleration a(t) = dv/dt</text>
  </g>
</svg>"""
        create_or_update_svg_block(l226, 2, 'Kinematics Differentiation Ladder', 'kinematics_ladder', svg_226_p2)

        # P3 SVG: Real-World Optimization Algorithm
        svg_226_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Real-World Optimization Algorithm</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1. Express Target Quantity (Volume/Area) as single variable f(x)</text>
    <text x="360" y="150" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">2. Solve f'(x) = 0 for stationary point x</text>
    <text x="360" y="200" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">3. Verify Maximum/Minimum via Second Derivative / Sign Test</text>
  </g>
</svg>"""
        create_or_update_svg_block(l226, 3, 'Real-World Optimization Algorithm', 'optimization_algorithm', svg_226_p3)

        # P4 SVG: Worked Example 1 - Motion Graphs s(t), v(t), a(t)
        svg_226_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Motion Graphs s(t), v(t), a(t)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Instantaneous Rest occurs when Velocity v(t) = 0</text>
  </g>
</svg>"""
        create_or_update_svg_block(l226, 4, 'Worked Example 1: Motion Graphs s(t), v(t), a(t)', 'worked_example_motion_graphs', svg_226_p4)

        # P9 SVG: Common Misconception - Confusing v(t)=0 with a(t)=0
        svg_226_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Confusing v(t)=0 with a(t)=0 Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">v(t) = 0 ➔ Particle at Rest  ≠  a(t) = 0 ➔ Constant Velocity / Max Speed</text>
  </g>
</svg>"""
        create_or_update_svg_block(l226, 9, 'Common Error: Velocity vs Acceleration Zero Warning', 'misconception_velocity_acceleration_zero', svg_226_p9)

        # Fix Block 13889 (Page 8)
        block_sim226 = LessonBlock.objects.filter(lesson=l226, page_number=8).first()
        if block_sim226:
            block_sim226.block_type = 'simulation_placeholder'
            meta = block_sim226.metadata or {}
            meta['simulation_key'] = 'math_differentiation_explorer'
            meta['archetype'] = 'math_differentiation_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Differentiation'
            block_sim226.metadata = meta
            block_sim226.save()
            print(f'  [Page 8] Updated Block {block_sim226.id} block_type to simulation_placeholder')

    print('\n=== ENRICHMENT OF TOPIC 8 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic8_calculus()
