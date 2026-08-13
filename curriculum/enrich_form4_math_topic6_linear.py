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

def enrich_topic6_linear():
    print('=== ENRICHING FORM 4 MATH TOPIC 6: LINEAR PROGRAMMING ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=6).first()
    if not topic:
        print('Error: Topic 6 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 6, found {len(lessons)}')
        return

    l215, l216, l217, l218 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 215: Formulating Linear Inequalities and Systems of Constraints
    # =========================================================================
    if l215:
        print(f'Enriching Lesson 215: "{l215.title}"')

        # P2 SVG: Verbal-to-Algebraic Constraint Flowchart
        svg_215_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Verbal-to-Algebraic Constraint Formulation Guide</text>

  <g transform="translate(40, 55)">
    <rect width="760" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <g transform="translate(30, 30)">
      <rect width="330" height="70" fill="#0f172a" rx="8" stroke="#4ade80"/>
      <text x="20" y="30" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">"At least" / "Minimum of" ⟹ ≥</text>
      <text x="20" y="52" fill="#cbd5e1" font-family="monospace" font-size="13">Example: x + y ≥ 20</text>
    </g>

    <g transform="translate(400, 30)">
      <rect width="330" height="70" fill="#0f172a" rx="8" stroke="#f87171"/>
      <text x="20" y="30" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">"At most" / "No more than" ⟹ ≤</text>
      <text x="20" y="52" fill="#cbd5e1" font-family="monospace" font-size="13">Example: 2x + y ≤ 80</text>
    </g>

    <g transform="translate(30, 120)">
      <rect width="330" height="70" fill="#0f172a" rx="8" stroke="#facc15"/>
      <text x="20" y="30" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">"Exceeds by at least" ⟹ - ≥</text>
      <text x="20" y="52" fill="#cbd5e1" font-family="monospace" font-size="13">Example: y - x ≥ 10</text>
    </g>

    <g transform="translate(400, 120)">
      <rect width="330" height="70" fill="#0f172a" rx="8" stroke="#38bdf8"/>
      <text x="20" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">"Non-negativity Constraints"</text>
      <text x="20" y="52" fill="#cbd5e1" font-family="monospace" font-size="13">Must include: x ≥ 0, y ≥ 0</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l215, 2, 'Verbal-to-Algebraic Constraint Flowchart', 'verbal_constraint_flowchart', svg_215_p2)

        # P3 SVG: Master Inequality Translation Dictionary
        svg_215_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Master Verbal-to-Algebraic Inequality Dictionary</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">"At Least N" ⟹ x ≥ N</text>
    <text x="360" y="140" fill="#f87171" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">"At Most N" / "Not Exceeding N" ⟹ x ≤ N</text>
    <text x="360" y="180" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">"Ratio y to x is at least k" ⟹ y/x ≥ k ⟹ y ≥ kx</text>
  </g>
</svg>"""
        create_or_update_svg_block(l215, 3, 'Master Verbal-to-Algebraic Inequality Dictionary Card', 'inequality_dictionary_card', svg_215_p3)

        # P4 SVG: Worked Example 1 - Factory Production Constraints
        svg_215_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Production Constraints System</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1. Total Quantity: x + y ≤ 50</text>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">2. Machine Hours: 2x + 3y ≤ 120</text>
    <text x="360" y="180" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">3. Non-negativity: x ≥ 0, y ≥ 0</text>
  </g>
</svg>"""
        create_or_update_svg_block(l215, 4, 'Worked Example 1: Production Constraints System', 'worked_example_production_system', svg_215_p4)

        # P9 SVG: Common Misconception - Symbol Direction
        svg_215_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: "At Least" vs "At Most" Direction Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">"At Least" means MINIMUM ⟹ Use ≥ (Never use ≤!)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l215, 9, 'Common Error: Symbol Direction Warning', 'misconception_symbol_direction', svg_215_p9)

        # Fix Block 13680 (Page 8)
        block_sim215 = LessonBlock.objects.filter(lesson=l215, page_number=8).first()
        if block_sim215:
            block_sim215.block_type = 'simulation_placeholder'
            meta = block_sim215.metadata or {}
            meta['simulation_key'] = 'math_linear_programming_explorer'
            meta['archetype'] = 'math_linear_programming_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Linear Programming'
            block_sim215.metadata = meta
            block_sim215.save()
            print(f'  [Page 8] Updated Block {block_sim215.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 216: Graphical Representation of Inequalities and KCSE Shading
    # =========================================================================
    if l216:
        print(f'Enriching Lesson 216: "{l216.title}"')

        # P2 SVG: KCSE "Shade the Unwanted Region" Principle
        svg_216_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">KCSE Exam Rule: Shade Out the UNWANTED Region (Leave Region R Clean)</text>

  <g transform="translate(40, 55)">
    <rect width="360" height="320" fill="#0f172a" rx="12" stroke="#1e293b"/>
    <rect x="40" y="40" width="280" height="240" fill="#f87171" opacity="0.3"/>
    <polygon points="120,240 280,240 220,100 120,100" fill="#ffffff" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="185" y="175" fill="#0f172a" font-family="system-ui, sans-serif" font-size="24" font-weight="bold" text-anchor="middle">R</text>
    <text x="185" y="200" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">(Clean Region)</text>
    <text x="60" y="70" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Unwanted Shaded</text>
  </g>

  <g transform="translate(440, 55)">
    <rect width="360" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="180" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">KCSE Shading Protocol:</text>

    <rect x="20" y="60" width="320" height="75" fill="#0f172a" rx="8" stroke="#f87171"/>
    <text x="35" y="85" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">1. Test Point (0,0) Evaluation</text>
    <text x="35" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Determine which side satisfies inequality</text>

    <rect x="20" y="150" width="320" height="75" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="35" y="175" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">2. Shade OUT the Invalid Side</text>
    <text x="35" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Draw shading lines over the UNWANTED side</text>

    <rect x="20" y="240" width="320" height="60" fill="#0f172a" rx="8" stroke="#facc15"/>
    <text x="180" y="275" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. Mark Feasible Region R (Clean)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l216, 2, 'KCSE "Shade the Unwanted Region" Principle', 'kcse_unwanted_shading_principle', svg_216_p2)

        # P3 SVG: Boundary Line Plotting & Test Point
        svg_216_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Boundary Line Plotting &amp; Test Point (0,0) Evaluation</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1. Boundary Line: ax + by = c (Solid for ≤, Dashed for &lt;)</text>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">2. Test Point (0,0): Sub (0,0) into ax + by</text>
    <text x="360" y="180" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">3. Shade out side that fails inequality!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l216, 3, 'Boundary Line Plotting & Test Point Evaluation', 'boundary_line_test_point', svg_216_p3)

        # P4 SVG: Worked Example 1 - Feasible Polygon R
        svg_216_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Feasible Polygon R Vertices A, B, C, D</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">A(0,0), B(40,0), C(20,30), D(0,40) ⟹ Feasible Region R</text>
  </g>
</svg>"""
        create_or_update_svg_block(l216, 4, 'Worked Example 1: Feasible Polygon R Vertices', 'worked_example_feasible_polygon', svg_216_p4)

        # P9 SVG: Common Misconception - KCSE Shading Fallacy
        svg_216_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Shading the Wanted Region Warning (KCSE Trap)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">In KCSE, shading the wanted region results in complete mark loss!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l216, 9, 'Common Error: Shading Wanted Region Warning', 'misconception_kcse_shading_fallacy', svg_216_p9)

        # Fix Block 13691 (Page 8)
        block_sim216 = LessonBlock.objects.filter(lesson=l216, page_number=8).first()
        if block_sim216:
            block_sim216.block_type = 'simulation_placeholder'
            meta = block_sim216.metadata or {}
            meta['simulation_key'] = 'math_linear_programming_explorer'
            meta['archetype'] = 'math_linear_programming_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Linear Programming'
            block_sim216.metadata = meta
            block_sim216.save()
            print(f'  [Page 8] Updated Block {block_sim216.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 217: Optimization via Algebraic Corner-Point Evaluation
    # =========================================================================
    if l217:
        print(f'Enriching Lesson 217: "{l217.title}"')

        # P2 SVG: Convex Polygon Corner-Point Optimization Principle
        svg_217_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Convex Polygon Corner-Point Optimization Principle</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Maximum &amp; Minimum of P = ax + by MUST occur at Polygon Corners A, B, C, D</text>
  </g>
</svg>"""
        create_or_update_svg_block(l217, 2, 'Convex Polygon Corner-Point Optimization Principle', 'corner_point_principle', svg_217_p2)

        # P3 SVG: Corner-Point Evaluation Table
        svg_217_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Corner-Point Evaluation Matrix Table</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">A(0,0) ⟹ P = 0</text>
    <text x="360" y="140" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">B(40,0) ⟹ P = 12,000</text>
    <text x="360" y="180" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">C(20,30) ⟹ P = 17,000 (MAXIMUM)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l217, 3, 'Corner-Point Evaluation Matrix Table', 'corner_point_table', svg_217_p3)

        # P4 SVG: Worked Example 1 - Discrete Integer Grid Solution
        svg_217_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Discrete Integer Grid Solution</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">(12.4, 18.7) ⟹ Test Integer Grid Points inside R ⟹ (12, 18)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l217, 4, 'Worked Example 1: Discrete Integer Grid Solution', 'worked_example_discrete_solution', svg_217_p4)

        # P9 SVG: Common Misconception - Naive Decimal Rounding
        svg_217_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Naive Decimal Rounding Outside Region R Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Rounding (12.8, 18.2) ⟹ (13, 18) may land OUTSIDE feasible region R!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l217, 9, 'Common Error: Naive Decimal Rounding Warning', 'misconception_decimal_rounding', svg_217_p9)

        # Fix Block 13702 (Page 8)
        block_sim217 = LessonBlock.objects.filter(lesson=l217, page_number=8).first()
        if block_sim217:
            block_sim217.block_type = 'simulation_placeholder'
            meta = block_sim217.metadata or {}
            meta['simulation_key'] = 'math_linear_programming_explorer'
            meta['archetype'] = 'math_linear_programming_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Linear Programming'
            block_sim217.metadata = meta
            block_sim217.save()
            print(f'  [Page 8] Updated Block {block_sim217.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 218: Optimization via Graphical Search-Line Method
    # =========================================================================
    if l218:
        print(f'Enriching Lesson 218: "{l218.title}"')

        # P2 SVG: Parallel Search-Line Sliding Principle
        svg_218_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Parallel Search-Line Sliding Principle</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Slide Objective Line ax + by = k parallel to itself across Region R</text>
  </g>
</svg>"""
        create_or_update_svg_block(l218, 2, 'The Parallel Search-Line Sliding Principle', 'parallel_search_line_principle', svg_218_p2)

        # P3 SVG: Search-Line Construction & Slope Rules
        svg_218_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Search-Line Construction &amp; Slope Rules</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Slope m = -a/b ⟹ Slide line parallel using set-squares!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l218, 3, 'Search-Line Construction & Slope Rules', 'search_line_slope_rules', svg_218_p3)

        # P4 SVG: Worked Example 1 - Search-Line Contact Point
        svg_218_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Search-Line Contact Point at C(20,30)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Last contact point at Vertex C(20,30) ⟹ Max P = 17,000</text>
  </g>
</svg>"""
        create_or_update_svg_block(l218, 4, 'Worked Example 1: Search-Line Contact Point', 'worked_example_search_line_contact', svg_218_p4)

        # P9 SVG: Common Misconception - Sliding in Wrong Direction
        svg_218_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Sliding Search-Line in Wrong Direction Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">For MAXIMIZATION, slide search-line AWAY from origin!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l218, 9, 'Common Error: Search-Line Direction Warning', 'misconception_search_line_direction', svg_218_p9)

        # Fix Block 13713 (Page 8)
        block_sim218 = LessonBlock.objects.filter(lesson=l218, page_number=8).first()
        if block_sim218:
            block_sim218.block_type = 'simulation_placeholder'
            meta = block_sim218.metadata or {}
            meta['simulation_key'] = 'math_linear_programming_explorer'
            meta['archetype'] = 'math_linear_programming_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Linear Programming'
            block_sim218.metadata = meta
            block_sim218.save()
            print(f'  [Page 8] Updated Block {block_sim218.id} block_type to simulation_placeholder')

    print('\n=== ENRICHMENT OF TOPIC 6 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic6_linear()
