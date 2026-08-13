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

def enrich_topic3_geometry():
    print('=== ENRICHING FORM 4 MATH TOPIC 3: THREE-DIMENSIONAL GEOMETRY (FULL VERTEX & LINE LABELS) ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=3).first()
    if not topic:
        print('Error: Topic 3 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 3, found {len(lessons)}')
        return

    l203, l204, l205, l206 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 203: Geometric Properties of 3D Solids, Skew Lines, and Projections
    # =========================================================================
    if l203:
        print(f'Enriching Lesson 203: "{l203.title}"')

        # P2 SVG: Fully Labelled Cuboid ABCDEFGH (All 8 Vertices + All Line Categories)
        svg_203_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">3D Cuboid ABCDEFGH: Full Vertex &amp; Line Classification</text>

  <!-- Left: 3D Cuboid Wireframe -->
  <g transform="translate(30, 55)">
    <rect width="420" height="340" fill="#0f172a" rx="12" stroke="#1e293b"/>

    <!-- Base ABCD: A(70,260), B(240,260), C(320,190), D(150,190) -->
    <line x1="70" y1="260" x2="240" y2="260" stroke="#38bdf8" stroke-width="4"/> <!-- Parallel AB (Blue) -->
    <line x1="240" y1="260" x2="320" y2="190" stroke="#4ade80" stroke-width="3.5"/> <!-- Intersecting BC (Green) -->
    <line x1="320" y1="190" x2="150" y2="190" stroke="#38bdf8" stroke-width="3.5"/> <!-- Parallel CD (Blue) -->
    <line x1="150" y1="190" x2="70" y2="260" stroke="#475569" stroke-width="2" stroke-dasharray="4 3"/> <!-- DA -->

    <!-- Top EFGH: E(70,120), F(240,120), G(320,50), H(150,50) -->
    <line x1="70" y1="120" x2="240" y2="120" stroke="#64748b" stroke-width="2"/> <!-- EF -->
    <line x1="240" y1="120" x2="320" y2="50" stroke="#64748b" stroke-width="2"/> <!-- FG -->
    <line x1="320" y1="50" x2="150" y2="50" stroke="#64748b" stroke-width="2"/> <!-- GH -->
    <line x1="150" y1="50" x2="70" y2="120" stroke="#64748b" stroke-width="2"/> <!-- HE -->

    <!-- Verticals: AE, BF, CG (Amber Skew to AB), DH -->
    <line x1="70" y1="260" x2="70" y2="120" stroke="#475569" stroke-width="2" stroke-dasharray="4 3"/> <!-- AE -->
    <line x1="240" y1="260" x2="240" y2="120" stroke="#64748b" stroke-width="2"/> <!-- BF -->
    <line x1="320" y1="190" x2="320" y2="50" stroke="#f59e0b" stroke-width="4"/> <!-- Skew Vertical CG (Amber) -->
    <line x1="150" y1="190" x2="150" y2="50" stroke="#64748b" stroke-width="2"/> <!-- DH -->

    <!-- All 8 Vertex Circles & Labels A, B, C, D, E, F, G, H -->
    <circle cx="70" cy="260" r="5" fill="#38bdf8"/>
    <text x="50" y="280" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">A</text>

    <circle cx="240" cy="260" r="5" fill="#38bdf8"/>
    <text x="250" y="280" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">B</text>

    <circle cx="320" cy="190" r="5" fill="#4ade80"/>
    <text x="330" y="205" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">C</text>

    <circle cx="150" cy="190" r="4" fill="#64748b"/>
    <text x="130" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">D</text>

    <circle cx="70" cy="120" r="4" fill="#64748b"/>
    <text x="50" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">E</text>

    <circle cx="240" cy="120" r="4" fill="#64748b"/>
    <text x="250" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">F</text>

    <circle cx="320" cy="50" r="5" fill="#f59e0b"/>
    <text x="330" y="45" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">G</text>

    <circle cx="150" cy="50" r="4" fill="#64748b"/>
    <text x="135" y="45" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">H</text>
  </g>

  <!-- Right: Card Definitions -->
  <g transform="translate(470, 55)">
    <rect width="340" height="340" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <rect x="20" y="25" width="300" height="85" fill="#0f172a" rx="8" stroke="#38bdf8"/>
    <text x="35" y="50" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">1. Parallel Lines (AB ∥ CD ∥ EF ∥ GH)</text>
    <text x="35" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Same direction, same plane, never intersect.</text>
    <text x="35" y="92" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Example: Edge AB ∥ Edge CD</text>

    <rect x="20" y="125" width="300" height="85" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="35" y="150" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">2. Intersecting Lines (AB &amp; BC)</text>
    <text x="35" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Lie in same plane, meet at a single vertex.</text>
    <text x="35" y="192" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Example: Edge AB meets Edge BC at Vertex B</text>

    <rect x="20" y="225" width="300" height="95" fill="#0f172a" rx="8" stroke="#f59e0b"/>
    <text x="35" y="250" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">3. Skew Lines (AB &amp; CG)</text>
    <text x="35" y="272" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Non-parallel AND non-intersecting!</text>
    <text x="35" y="292" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Lie in different parallel planes (ABCD &amp; BCGF)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l203, 2, '3D Cuboid & Line Classification (Parallel, Intersecting, Skew)', 'skew_lines_classification', svg_203_p2)

        # P4 SVG: Worked Example 1 - Fully Labelled Cuboid ABCDEFGH
        svg_203_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Worked Example 1: Full Vertex &amp; Edge Diagnostic in Cuboid ABCDEFGH</text>

  <g transform="translate(40, 55)">
    <rect width="420" height="320" fill="#0f172a" rx="12" stroke="#1e293b"/>

    <!-- Cuboid Wireframe -->
    <line x1="80" y1="250" x2="240" y2="250" stroke="#38bdf8" stroke-width="4"/> <!-- AB -->
    <line x1="240" y1="250" x2="310" y2="190" stroke="#64748b" stroke-width="2"/> <!-- BC -->
    <line x1="310" y1="190" x2="150" y2="190" stroke="#64748b" stroke-width="2"/> <!-- CD -->
    <line x1="150" y1="190" x2="80" y2="250" stroke="#475569" stroke-width="1.5" stroke-dasharray="3 3"/> <!-- DA -->

    <line x1="80" y1="120" x2="240" y2="120" stroke="#64748b" stroke-width="2"/> <!-- EF -->
    <line x1="240" y1="120" x2="310" y2="60" stroke="#64748b" stroke-width="2"/> <!-- FG -->
    <line x1="310" y1="60" x2="150" y2="60" stroke="#f59e0b" stroke-width="4"/> <!-- GH -->
    <line x1="150" y1="60" x2="80" y2="120" stroke="#64748b" stroke-width="2"/> <!-- HE -->

    <line x1="80" y1="250" x2="80" y2="120" stroke="#475569" stroke-width="1.5" stroke-dasharray="3 3"/> <!-- AE -->
    <line x1="240" y1="250" x2="240" y2="120" stroke="#64748b" stroke-width="2"/> <!-- BF -->
    <line x1="310" y1="190" x2="310" y2="60" stroke="#64748b" stroke-width="2"/> <!-- CG -->
    <line x1="150" y1="190" x2="150" y2="60" stroke="#64748b" stroke-width="2"/> <!-- DH -->

    <!-- Vertices A, B, C, D, E, F, G, H -->
    <circle cx="80" cy="250" r="5" fill="#38bdf8"/><text x="60" y="270" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">A</text>
    <circle cx="240" cy="250" r="5" fill="#38bdf8"/><text x="250" y="270" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">B</text>
    <circle cx="310" cy="190" r="4" fill="#cbd5e1"/><text x="320" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">C</text>
    <circle cx="150" cy="190" r="4" fill="#cbd5e1"/><text x="135" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">D</text>

    <circle cx="80" cy="120" r="4" fill="#cbd5e1"/><text x="60" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">E</text>
    <circle cx="240" cy="120" r="4" fill="#cbd5e1"/><text x="250" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">F</text>
    <circle cx="310" cy="60" r="5" fill="#f59e0b"/><text x="320" y="55" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">G</text>
    <circle cx="150" cy="60" r="5" fill="#f59e0b"/><text x="135" y="55" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">H</text>
  </g>

  <g transform="translate(480, 55)">
    <rect width="330" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Line Relationship Diagnostic:</text>

    <rect x="20" y="60" width="290" height="75" fill="#0f172a" rx="8" stroke="#38bdf8"/>
    <text x="35" y="85" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Line 1: Bottom Edge AB</text>
    <text x="35" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Lies on bottom face ABCD between A &amp; B</text>

    <rect x="20" y="150" width="290" height="75" fill="#0f172a" rx="8" stroke="#f59e0b"/>
    <text x="35" y="175" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Line 2: Top Back Edge GH</text>
    <text x="35" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Lies on top face EFGH between G &amp; H</text>

    <rect x="20" y="240" width="290" height="60" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="165" y="275" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Result: AB ∥ GH (PARALLEL)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l203, 4, 'Worked Example 1: Line Relationships in a Cuboid', 'worked_example_1_cuboid_lines', svg_203_p4)

        # Fix Block 14230 (Page 8)
        block_sim203 = LessonBlock.objects.filter(lesson=l203, page_number=8).first()
        if block_sim203:
            block_sim203.block_type = 'simulation_placeholder'
            meta = block_sim203.metadata or {}
            meta['simulation_key'] = 'math_3d_geometry_explorer'
            meta['archetype'] = 'math_3d_geometry_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Three Dimensional Geometry'
            block_sim203.metadata = meta
            block_sim203.save()
            print(f'  [Page 8] Updated Block {block_sim203.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 204: Calculating 3D Lengths and Angles Between Lines
    # =========================================================================
    if l204:
        print(f'Enriching Lesson 204: "{l204.title}"')

        # P2 SVG: Fully Labelled Cuboid ABCDEFGH Space Diagonal
        svg_204_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Compound 3D Pythagoras: Space Diagonal AG in Cuboid ABCDEFGH</text>

  <g transform="translate(40, 55)">
    <rect width="420" height="320" fill="#0f172a" rx="12" stroke="#1e293b"/>

    <!-- Base Diagonal △ABC (Green) -->
    <polygon points="80,250 240,250 310,190" fill="rgba(74, 222, 128, 0.25)"/>
    <line x1="80" y1="250" x2="310" y2="190" stroke="#4ade80" stroke-width="3.5"/> <!-- Base Diagonal AC -->
    <text x="180" y="240" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">AC = √(L² + W²)</text>

    <!-- Vertical Triangle △ACG (Amber) -->
    <polygon points="80,250 310,190 310,60" fill="rgba(245, 158, 11, 0.25)"/>
    <line x1="310" y1="190" x2="310" y2="60" stroke="#38bdf8" stroke-width="2.5"/> <!-- Height CG = H -->
    <line x1="80" y1="250" x2="310" y2="60" stroke="#f59e0b" stroke-width="4"/> <!-- Space Diagonal AG -->
    <text x="170" y="130" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">AG = √(L² + W² + H²)</text>

    <!-- Outer Cuboid Frame -->
    <line x1="80" y1="250" x2="240" y2="250" stroke="#64748b" stroke-width="1.5"/><text x="160" y="268" fill="#cbd5e1" font-size="11">Length L</text>
    <line x1="240" y1="250" x2="310" y2="190" stroke="#64748b" stroke-width="1.5"/><text x="280" y="230" fill="#cbd5e1" font-size="11">Width W</text>
    <line x1="310" y1="190" x2="150" y2="190" stroke="#475569" stroke-dasharray="3 2"/>
    <line x1="150" y1="190" x2="80" y2="250" stroke="#475569" stroke-dasharray="3 2"/>

    <line x1="80" y1="120" x2="240" y2="120" stroke="#64748b" stroke-width="1.5"/>
    <line x1="240" y1="120" x2="310" y2="60" stroke="#64748b" stroke-width="1.5"/>
    <line x1="310" y1="60" x2="150" y2="60" stroke="#64748b" stroke-width="1.5"/>
    <line x1="150" y1="60" x2="80" y2="120" stroke="#64748b" stroke-width="1.5"/>

    <line x1="80" y1="250" x2="80" y2="120" stroke="#475569" stroke-dasharray="3 2"/>
    <line x1="240" y1="250" x2="240" y2="120" stroke="#64748b" stroke-width="1.5"/>
    <line x1="150" y1="190" x2="150" y2="60" stroke="#64748b" stroke-width="1.5"/>

    <!-- All Vertices A, B, C, D, E, F, G, H -->
    <circle cx="80" cy="250" r="5" fill="#facc15"/><text x="60" y="265" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">A</text>
    <circle cx="240" cy="250" r="4" fill="#cbd5e1"/><text x="250" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">B</text>
    <circle cx="310" cy="190" r="5" fill="#4ade80"/><text x="320" y="200" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">C</text>
    <circle cx="150" cy="190" r="4" fill="#cbd5e1"/><text x="135" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">D</text>

    <circle cx="80" cy="120" r="4" fill="#cbd5e1"/><text x="60" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">E</text>
    <circle cx="240" cy="120" r="4" fill="#cbd5e1"/><text x="250" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">F</text>
    <circle cx="310" cy="60" r="5" fill="#f59e0b"/><text x="320" y="55" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">G</text>
    <circle cx="150" cy="60" r="4" fill="#cbd5e1"/><text x="135" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">H</text>
  </g>

  <g transform="translate(480, 55)">
    <rect width="330" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Step-by-Step Derivation:</text>

    <rect x="20" y="60" width="290" height="75" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="35" y="85" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Step 1: Base Diagonal AC (△ABC)</text>
    <text x="35" y="115" fill="#4ade80" font-family="monospace" font-size="15" font-weight="bold">AC² = L² + W²</text>

    <rect x="20" y="150" width="290" height="75" fill="#0f172a" rx="8" stroke="#f59e0b"/>
    <text x="35" y="175" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Step 2: Space Diagonal AG (△ACG)</text>
    <text x="35" y="205" fill="#f59e0b" font-family="monospace" font-size="15" font-weight="bold">AG² = AC² + H²</text>

    <rect x="20" y="240" width="290" height="60" fill="#0f172a" rx="8" stroke="#38bdf8"/>
    <text x="165" y="275" fill="#38bdf8" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">AG = √(L² + W² + H²)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l204, 2, 'Compound 3D Pythagoras Space Diagonal Breakdown', 'pythagoras_3d_breakdown', svg_204_p2)

        # Fix Block 14241 (Page 8)
        block_sim204 = LessonBlock.objects.filter(lesson=l204, page_number=8).first()
        if block_sim204:
            block_sim204.block_type = 'simulation_placeholder'
            meta = block_sim204.metadata or {}
            meta['simulation_key'] = 'math_3d_geometry_explorer'
            meta['archetype'] = 'math_3d_geometry_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Three Dimensional Geometry'
            block_sim204.metadata = meta
            block_sim204.save()
            print(f'  [Page 8] Updated Block {block_sim204.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 205: Angle Between a Line and a Plane
    # =========================================================================
    if l205:
        print(f'Enriching Lesson 205: "{l205.title}"')

        # P3 SVG: Fully Labelled Square Pyramid VABCD Slant Edge Angle
        svg_205_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Square Pyramid VABCD: Slant Edge VA Inclination Angle θ</text>

  <g transform="translate(40, 55)">
    <rect width="420" height="320" fill="#0f172a" rx="12" stroke="#1e293b"/>

    <!-- Base Square ABCD: A(60,240), B(220,240), C(300,170), D(140,170) -->
    <polygon points="60,240 220,240 300,170 140,170" fill="rgba(15,23,42,0.8)" stroke="#334155" stroke-width="1.5"/>

    <!-- Base Diagonals AC & BD meeting at Center O(180, 205) -->
    <line x1="60" y1="240" x2="300" y2="170" stroke="#4ade80" stroke-width="2.5"/> <!-- Half-diagonal AO -->
    <line x1="220" y1="240" x2="140" y2="170" stroke="#334155" stroke-dasharray="3 2"/>

    <!-- Apex V(180, 40) -->
    <!-- Height VO -->
    <line x1="180" y1="40" x2="180" y2="205" stroke="#f87171" stroke-width="2.5" stroke-dasharray="4 3"/>

    <!-- Slant Edges: VA (Blue), VB, VC, VD -->
    <line x1="180" y1="40" x2="60" y2="240" stroke="#38bdf8" stroke-width="4"/> <!-- Slant Edge VA -->
    <line x1="180" y1="40" x2="220" y2="240" stroke="#64748b" stroke-width="1.5"/> <!-- VB -->
    <line x1="180" y1="40" x2="300" y2="170" stroke="#64748b" stroke-width="1.5"/> <!-- VC -->
    <line x1="180" y1="40" x2="140" y2="170" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 2"/> <!-- VD -->

    <!-- Right Triangle VOA fill -->
    <polygon points="180,40 60,240 180,205" fill="rgba(56, 189, 248, 0.2)"/>

    <!-- Angle theta at A -->
    <path d="M 100 240 A 40 40 0 0 0 92 215" fill="none" stroke="#facc15" stroke-width="2.5"/>
    <text x="105" y="215" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">θ</text>

    <!-- Vertices V, A, B, C, D, O -->
    <circle cx="180" cy="40" r="6" fill="#facc15"/><text x="180" y="25" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">V (Apex)</text>
    <circle cx="60" cy="240" r="5" fill="#38bdf8"/><text x="40" y="255" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">A</text>
    <circle cx="220" cy="240" r="4" fill="#cbd5e1"/><text x="230" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">B</text>
    <circle cx="300" cy="170" r="4" fill="#cbd5e1"/><text x="310" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">C</text>
    <circle cx="140" cy="170" r="4" fill="#cbd5e1"/><text x="125" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">D</text>
    <circle cx="180" cy="205" r="5" fill="#f87171"/><text x="190" y="220" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">O (Base Center)</text>
  </g>

  <g transform="translate(480, 55)">
    <rect width="330" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Right Triangle △VOA Elements:</text>

    <text x="25" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">1. Hypotenuse = Slant Edge VA</text>
    <text x="25" y="105" fill="#f87171" font-family="system-ui, sans-serif" font-size="12">2. Opposite Side = Pyramid Height VO</text>
    <text x="25" y="135" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12">3. Adjacent Side = Base Half-Diagonal AO</text>

    <rect x="20" y="165" width="290" height="60" fill="#0f172a" rx="8" stroke="#facc15"/>
    <text x="165" y="200" fill="#facc15" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">tan θ = VO / AO</text>
  </g>
</svg>"""
        create_or_update_svg_block(l205, 3, 'Square Pyramid Slant Edge Inclination Formula Diagram', 'pyramid_slant_inclination', svg_205_p3)

        # Fix Block 14252 (Page 8)
        block_sim205 = LessonBlock.objects.filter(lesson=l205, page_number=8).first()
        if block_sim205:
            block_sim205.block_type = 'simulation_placeholder'
            meta = block_sim205.metadata or {}
            meta['simulation_key'] = 'math_3d_geometry_explorer'
            meta['archetype'] = 'math_3d_geometry_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Three Dimensional Geometry'
            block_sim205.metadata = meta
            block_sim205.save()
            print(f'  [Page 8] Updated Block {block_sim205.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 206: Angle Between Two Planes (Dihedral Angle)
    # =========================================================================
    if l206:
        print(f'Enriching Lesson 206: "{l206.title}"')

        # P2 SVG: Fully Labelled Dihedral Angle Book-Spine Rule
        svg_206_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">The Book-Spine Rule for Dihedral Angles Between Intersecting Planes</text>

  <g transform="translate(60, 55)">
    <rect width="720" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Spine Line AB -->
    <line x1="360" y1="40" x2="360" y2="280" stroke="#facc15" stroke-width="4"/>
    <circle cx="360" cy="40" r="5" fill="#facc15"/><text x="360" y="25" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Spine Vertex A</text>
    <circle cx="360" cy="280" r="5" fill="#facc15"/><text x="360" y="300" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Spine Vertex B</text>

    <!-- Plane 1 (Left, Blue) -->
    <polygon points="120,70 360,40 360,280 120,300" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2"/>
    <text x="180" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Plane Π₁</text>

    <!-- Plane 2 (Right, Green) -->
    <polygon points="600,80 360,40 360,280 600,310" fill="rgba(74, 222, 128, 0.2)" stroke="#4ade80" stroke-width="2"/>
    <text x="540" y="100" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Plane Π₂</text>

    <!-- Common Point X on Spine AB -->
    <circle cx="360" cy="170" r="6" fill="#facc15"/>
    <text x="360" y="195" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">X (Common Point on AB)</text>

    <!-- Perpendicular PX ⊥ AB on Plane 1 -->
    <line x1="200" y1="170" x2="360" y2="170" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="200" cy="170" r="5" fill="#38bdf8"/>
    <text x="180" y="175" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">P (PX ⊥ AB)</text>

    <!-- Perpendicular QX ⊥ AB on Plane 2 -->
    <line x1="360" y1="170" x2="520" y2="180" stroke="#4ade80" stroke-width="3"/>
    <circle cx="520" cy="180" r="5" fill="#4ade80"/>
    <text x="535" y="185" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Q (QX ⊥ AB)</text>

    <!-- Dihedral Angle arc theta = ∠PXQ -->
    <path d="M 310 170 A 50 50 0 0 1 410 173" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <text x="360" y="140" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">θ = ∠PXQ (Dihedral Angle)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l206, 2, 'The Book-Spine Rule for Dihedral Angles Between Intersecting Planes', 'dihedral_book_spine_rule', svg_206_p2)

        # Fix Block 14263 (Page 8)
        block_sim206 = LessonBlock.objects.filter(lesson=l206, page_number=8).first()
        if block_sim206:
            block_sim206.block_type = 'simulation_placeholder'
            meta = block_sim206.metadata or {}
            meta['simulation_key'] = 'math_3d_geometry_explorer'
            meta['archetype'] = 'math_3d_geometry_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Three Dimensional Geometry'
            block_sim206.metadata = meta
            block_sim206.save()
            print(f'  [Page 8] Updated Block {block_sim206.id} block_type to simulation_placeholder')

    print('\n=== ENRICHMENT OF TOPIC 3 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic3_geometry()
