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

def enrich_topic7_loci():
    print('=== ENRICHING FORM 4 MATH TOPIC 7: LOCI ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=7).first()
    if not topic:
        print('Error: Topic 7 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 7, found {len(lessons)}')
        return

    l219, l220, l221, l222 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 219: Foundational 2D and 3D Loci: Definitions and Bisectors
    # =========================================================================
    if l219:
        print(f'Enriching Lesson 219: "{l219.title}"')

        # P2 SVG: 4 Standard 2D Loci Catalogue
        svg_219_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Catalogue of the 4 Standard 2D Loci</text>
  <g transform="translate(30, 55)">
    <g transform="translate(0, 0)">
      <rect width="370" height="150" fill="#0f172a" rx="10" stroke="#38bdf8"/>
      <circle cx="90" cy="75" r="45" fill="none" stroke="#facc15" stroke-width="2.5"/>
      <circle cx="90" cy="75" r="4" fill="#38bdf8"/>
      <text x="90" y="70" fill="#38bdf8" font-size="11" text-anchor="middle">Point A</text>
      <text x="155" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">1. Point at Distance r from A</text>
      <text x="155" y="65" fill="#facc15" font-family="monospace" font-size="12">Locus: Circle (Radius r)</text>
    </g>

    <g transform="translate(400, 0)">
      <rect width="370" height="150" fill="#0f172a" rx="10" stroke="#38bdf8"/>
      <line x1="40" y1="75" x2="160" y2="75" stroke="#38bdf8" stroke-width="2.5"/>
      <line x1="40" y1="45" x2="160" y2="45" stroke="#4ade80" stroke-width="2" stroke-dasharray="4 2"/>
      <line x1="40" y1="105" x2="160" y2="105" stroke="#4ade80" stroke-width="2" stroke-dasharray="4 2"/>
      <text x="175" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">2. Distance d from Line L</text>
      <text x="175" y="65" fill="#4ade80" font-family="monospace" font-size="12">Locus: Pair of Parallel Lines</text>
    </g>

    <g transform="translate(0, 165)">
      <rect width="370" height="150" fill="#0f172a" rx="10" stroke="#38bdf8"/>
      <circle cx="50" cy="75" r="4" fill="#38bdf8"/><text x="40" y="95" fill="#38bdf8" font-size="11">A</text>
      <circle cx="130" cy="75" r="4" fill="#38bdf8"/><text x="135" y="95" fill="#38bdf8" font-size="11">B</text>
      <line x1="50" y1="75" x2="130" y2="75" stroke="#64748b" stroke-width="2"/>
      <line x1="90" y1="25" x2="90" y2="125" stroke="#10b981" stroke-width="3"/>
      <text x="155" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">3. Equidistant from A &amp; B</text>
      <text x="155" y="65" fill="#10b981" font-family="monospace" font-size="12">Locus: Perpendicular Bisector</text>
    </g>

    <g transform="translate(400, 165)">
      <rect width="370" height="150" fill="#0f172a" rx="10" stroke="#38bdf8"/>
      <line x1="40" y1="120" x2="140" y2="30" stroke="#38bdf8" stroke-width="2"/>
      <line x1="40" y1="30" x2="140" y2="120" stroke="#38bdf8" stroke-width="2"/>
      <line x1="90" y1="20" x2="90" y2="130" stroke="#e879f9" stroke-width="2.5"/>
      <line x1="35" y1="75" x2="145" y2="75" stroke="#e879f9" stroke-width="2.5"/>
      <text x="160" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">4. Equidistant from 2 Lines</text>
      <text x="160" y="65" fill="#e879f9" font-family="monospace" font-size="12">Locus: Pair of Angle Bisectors</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l219, 2, '4 Standard 2D Loci Catalogue Diagram', 'loci_catalogue_2d', svg_219_p2)

        # P3 SVG: 2D vs 3D Loci Comparison Chart
        svg_219_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">2D vs 3D Spatial Loci Comparison Chart</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="90" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Distance r from Point A: 2D = Circle ⟺ 3D = Sphere</text>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Distance d from Line L: 2D = Parallel Lines ⟺ 3D = Circular Cylinder</text>
    <text x="360" y="190" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Equidistant from A &amp; B: 2D = Bisector Line ⟺ 3D = Bisecting Plane</text>
  </g>
</svg>"""
        create_or_update_svg_block(l219, 3, '2D vs 3D Loci Comparison Chart', 'loci_2d_3d_comparison', svg_219_p3)

        # P4 SVG: Worked Example 1 - Perpendicular Bisector Compass Construction
        svg_219_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Compass Construction of Perpendicular Bisector of AB</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Intersecting Compass Arcs (Radius > ½AB) ⟹ Line L (Midpoint M)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l219, 4, 'Worked Example 1: Compass Construction of Perpendicular Bisector', 'worked_example_perp_bisector', svg_219_p4)

        # P9 SVG: Common Misconception - Angle Bisector Ray Warning
        svg_219_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Stopping Angle Bisectors as Single Rays Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Angle bisectors of 2 intersecting lines form a PAIR of infinite perpendicular lines!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l219, 9, 'Common Error: Angle Bisector Ray Warning', 'misconception_angle_bisector_ray', svg_219_p9)

        # Fix Block 13768 (Page 8)
        block_sim219 = LessonBlock.objects.filter(lesson=l219, page_number=8).first()
        if block_sim219:
            block_sim219.block_type = 'simulation_placeholder'
            meta = block_sim219.metadata or {}
            meta['simulation_key'] = 'math_loci_construction_explorer'
            meta['archetype'] = 'math_loci_construction_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Loci'
            block_sim219.metadata = meta
            block_sim219.save()
            print(f'  [Page 8] Updated Block {block_sim219.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 220: Conditional Loci and Geometric Inequalities
    # =========================================================================
    if l220:
        print(f'Enriching Lesson 220: "{l220.title}"')

        # P2 SVG: Locus Inequality Boundaries
        svg_220_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Locus Inequality Boundaries &amp; Regions</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">d(P, A) ≤ r (Inside Circle) ∩ d(P, A) ≤ d(P, B) (Left of Bisector)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l220, 2, 'Locus Inequality Boundaries & Regions', 'locus_inequality_boundaries', svg_220_p2)

        # P3 SVG: Geometric Inequality Shading Guide
        svg_220_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Geometric Inequality Shading Conventions Guide Card</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1. Boundary Line: Solid for ≤ / ≥, Dashed for &lt; / &gt;</text>
    <text x="360" y="150" fill="#f87171" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">2. KCSE Rule: Shade OUT the UNWANTED region!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l220, 3, 'Geometric Inequality Shading Conventions Guide Card', 'inequality_shading_guide', svg_220_p3)

        # P4 SVG: Worked Example 1 - Compound Locus Inequality Region R
        svg_220_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Compound Locus Inequality Region R</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Feasible Region R is left CLEAN on graph paper</text>
  </g>
</svg>"""
        create_or_update_svg_block(l220, 4, 'Worked Example 1: Compound Locus Inequality Region R', 'worked_example_compound_locus_region', svg_220_p4)

        # P9 SVG: Common Misconception - Shading Target Region
        svg_220_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Shading the Target Region Warning (KCSE Trap)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Shading the wanted region in KCSE loci causes complete mark loss!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l220, 9, 'Common Error: Shading Target Region Warning', 'misconception_shading_target_region', svg_220_p9)

        # Fix Block 13779 (Page 8)
        block_sim220 = LessonBlock.objects.filter(lesson=l220, page_number=8).first()
        if block_sim220:
            block_sim220.block_type = 'simulation_placeholder'
            meta = block_sim220.metadata or {}
            meta['simulation_key'] = 'math_loci_construction_explorer'
            meta['archetype'] = 'math_loci_construction_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Loci'
            block_sim220.metadata = meta
            block_sim220.save()
            print(f'  [Page 8] Updated Block {block_sim220.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 221: Constant Angle Loci and Circle Arc Constructions
    # =========================================================================
    if l221:
        print(f'Enriching Lesson 221: "{l221.title}"')

        # P2 SVG: Constant Angle Locus Principle
        svg_221_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Constant Angle Locus Principle (∠APB = θ)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Locus of P such that ∠APB = θ is an Arc of a Circle</text>
  </g>
</svg>"""
        create_or_update_svg_block(l221, 2, 'Constant Angle Locus Principle (∠APB = θ)', 'constant_angle_locus_principle', svg_221_p2)

        # P3 SVG: Constant Angle Construction Steps
        svg_221_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Constant Angle Locus Construction Steps Diagram</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1. Construct Angle (90° - θ) at A</text>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">2. Intersect with Perpendicular Bisector of AB ⟹ Center O</text>
    <text x="360" y="180" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">3. Draw Circle Arc with Radius OA = OB</text>
  </g>
</svg>"""
        create_or_update_svg_block(l221, 3, 'Constant Angle Locus Construction Steps Diagram', 'constant_angle_construction_steps', svg_221_p3)

        # P4 SVG: Worked Example 1 - Semicircle Locus
        svg_221_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: The Semicircle Locus (∠APB = 90°)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">When θ = 90°, Locus is a SEMICIRCLE with Diameter AB</text>
  </g>
</svg>"""
        create_or_update_svg_block(l221, 4, 'Worked Example 1: The Semicircle Locus (∠APB = 90°)', 'worked_example_semicircle_locus', svg_221_p4)

        # P9 SVG: Common Misconception - Scribing Arc Wrong Side
        svg_221_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Scribing Arc on Wrong Side Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Arcs exist on BOTH sides of AB unless problem restricts to one side!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l221, 9, 'Common Error: Scribing Arc on Wrong Side Warning', 'misconception_arc_wrong_side', svg_221_p9)

        # Fix Block 13790 (Page 8)
        block_sim221 = LessonBlock.objects.filter(lesson=l221, page_number=8).first()
        if block_sim221:
            block_sim221.block_type = 'simulation_placeholder'
            meta = block_sim21.metadata or {} if 'block_sim21' in locals() else block_sim221.metadata or {}
            meta['simulation_key'] = 'math_loci_construction_explorer'
            meta['archetype'] = 'math_loci_construction_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Loci'
            block_sim221.metadata = meta
            block_sim221.save()
            print(f'  [Page 8] Updated Block {block_sim221.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 222: Intersecting Loci and Intersecting Chords Theorem
    # =========================================================================
    if l222:
        print(f'Enriching Lesson 222: "{l222.title}"')

        # P2 SVG: Intersecting Loci Pinpoint Principle
        svg_222_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Intersecting Loci Pinpoint Principle</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">Intersection of Locus 1 and Locus 2 gives exact Point(s) P</text>
  </g>
</svg>"""
        create_or_update_svg_block(l222, 2, 'Intersecting Loci Pinpoint Principle', 'intersecting_loci_pinpoint', svg_222_p2)

        # P3 SVG: Intersecting Chords Theorem Diagram
        svg_222_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Intersecting Chords Theorem Diagram (AP · PB = CP · PD)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">AP × PB = CP × PD (For Chords AB &amp; CD intersecting at P)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l222, 3, 'Intersecting Chords Theorem Diagram (AP · PB = CP · PD)', 'intersecting_chords_theorem', svg_222_p3)

        # P4 SVG: Worked Example 1 - Intersecting Chords Geometry
        svg_222_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Intersecting Chords Geometry</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">AP=4, PB=6, CP=3 ⟹ PD = (4 × 6)/3 = 8 cm</text>
  </g>
</svg>"""
        create_or_update_svg_block(l222, 4, 'Worked Example 1: Intersecting Chords Geometry', 'worked_example_intersecting_chords', svg_222_p4)

        # P9 SVG: Common Misconception - Incenter vs Circumcenter
        svg_222_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Incenter vs Circumcenter Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Incenter = Angle Bisectors ⟺ Circumcenter = Perpendicular Bisectors</text>
  </g>
</svg>"""
        create_or_update_svg_block(l222, 9, 'Common Error: Incenter vs Circumcenter Warning', 'misconception_incenter_circumcenter', svg_222_p9)

        # Fix Block 13801 (Page 8)
        block_sim222 = LessonBlock.objects.filter(lesson=l222, page_number=8).first()
        if block_sim222:
            block_sim222.block_type = 'simulation_placeholder'
            meta = block_sim222.metadata or {}
            meta['simulation_key'] = 'math_loci_construction_explorer'
            meta['archetype'] = 'math_loci_construction_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Loci'
            block_sim222.metadata = meta
            block_sim222.save()
            print(f'  [Page 8] Updated Block {block_sim222.id} block_type to simulation_placeholder')

    print('\n=== ENRICHMENT OF TOPIC 7 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic7_loci()
