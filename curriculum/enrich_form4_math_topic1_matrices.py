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
    
    # Check if a suggested_diagram block already exists on this page
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

def enrich_topic1_matrices():
    print('=== ENRICHING FORM 4 MATH TOPIC 1: MATRIX AND TRANSFORMATION ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=1).first()
    if not topic:
        print('Error: Topic 1 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 1, found {len(lessons)}')
        return

    l195, l196, l197, l198 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 195: Matrix Action on Coordinate Vectors
    # =========================================================================
    if l195:
        print(f'Enriching Lesson 195: "{l195.title}"')
        
        # P2 SVG: Matrix Acting on Point P(x,y) -> P'(x',y')
        svg_195_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Matrix Action on a Coordinate Vector: Spatial Mapping</text>

  <!-- Left: Coordinate Plane -->
  <g transform="translate(40, 60)">
    <rect width="380" height="320" fill="#0f172a" rx="12" stroke="#1e293b"/>
    <!-- Grid lines -->
    <line x1="40" y1="260" x2="360" y2="260" stroke="#334155" stroke-width="2"/> <!-- X Axis -->
    <line x1="80" y1="40" x2="80" y2="300" stroke="#334155" stroke-width="2"/> <!-- Y Axis -->
    <text x="365" y="265" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">x</text>
    <text x="75" y="32" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">y</text>

    <!-- Vector P (Original) -->
    <line x1="80" y1="260" x2="160" y2="170" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4 2"/>
    <circle cx="160" cy="170" r="6" fill="#38bdf8"/>
    <text x="170" y="165" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">P (2, 3)</text>

    <!-- Arrow from P to P' -->
    <path d="M 170 170 Q 240 130 300 170" fill="none" stroke="#facc15" stroke-width="2" stroke-dasharray="4 4"/>
    <polygon points="300,170 292,165 294,174" fill="#facc15"/>
    <text x="235" y="140" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">× Matrix M</text>

    <!-- Vector P' (Transformed) -->
    <line x1="80" y1="260" x2="320" y2="170" stroke="#4ade80" stroke-width="3"/>
    <circle cx="320" cy="170" r="7" fill="#4ade80"/>
    <text x="325" y="165" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">P' (8, 3)</text>
  </g>

  <!-- Right: Algebraic Calculation Box -->
  <g transform="translate(450, 60)">
    <rect width="350" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="175" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Matrix Multiplication Rule</text>

    <rect x="25" y="60" width="300" height="110" fill="#0f172a" rx="8" stroke="#334155"/>
    <text x="40" y="90" fill="#cbd5e1" font-family="monospace" font-size="16">[ 1  2 ]  [ 2 ]   [ (1×2) + (2×3) ]</text>
    <text x="40" y="125" fill="#cbd5e1" font-family="monospace" font-size="16">[ 0  1 ]  [ 3 ] = [ (0×2) + (1×3) ]</text>
    <text x="150" y="155" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold">= [ 8 , 3 ]ᵀ</text>

    <rect x="25" y="190" width="300" height="105" fill="#0f172a" rx="8" stroke="#334155"/>
    <text x="35" y="215" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Core Geometric Principle:</text>
    <text x="35" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Matrix M acts as a transformer machine.</text>
    <text x="35" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Input vector P(2,3) → Output vector P'(8,3).</text>
    <text x="35" y="278" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12">• Shear along x-axis shifted x by 2y.</text>
  </g>
</svg>"""
        create_or_update_svg_block(l195, 2, 'Matrix Action on Point Vectors: Spatial Mapping P → P\'', 'matrix_action_point', svg_195_p2)

        # P3 SVG: Row-by-Column Multiplication Algorithm
        svg_195_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Step-by-Step Row-by-Column Multiplication</text>

  <g transform="translate(40, 65)">
    <!-- Row 1 Step -->
    <rect width="760" height="140" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">Step 1: Finding New x'-coordinate (Top Row × Vector Column)</text>
    
    <rect x="30" y="45" width="220" height="75" fill="#0f172a" rx="8"/>
    <text x="50" y="80" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold">[ a   b ]</text>
    <text x="50" y="105" fill="#64748b" font-family="monospace" font-size="18">[ c   d ]</text>
    <text x="145" y="80" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold">[ x ]</text>
    <text x="145" y="105" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold">[ y ]</text>

    <text x="270" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="22">=</text>

    <rect x="310" y="55" width="420" height="60" fill="#0f172a" rx="8" stroke="#38bdf8"/>
    <text x="330" y="90" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold">x' = (a × x) + (b × y)</text>
    <text x="330" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Multiply 1st entry by x, 2nd entry by y, then ADD them.</text>
  </g>

  <g transform="translate(40, 225)">
    <!-- Row 2 Step -->
    <rect width="760" height="140" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="1.5"/>
    <text x="20" y="30" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">Step 2: Finding New y'-coordinate (Bottom Row × Vector Column)</text>
    
    <rect x="30" y="45" width="220" height="75" fill="#0f172a" rx="8"/>
    <text x="50" y="80" fill="#64748b" font-family="monospace" font-size="18">[ a   b ]</text>
    <text x="50" y="105" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold">[ c   d ]</text>
    <text x="145" y="80" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold">[ x ]</text>
    <text x="145" y="105" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold">[ y ]</text>

    <text x="270" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="22">=</text>

    <rect x="310" y="55" width="420" height="60" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="330" y="90" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold">y' = (c × x) + (d × y)</text>
    <text x="330" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Multiply 1st entry by x, 2nd entry by y, then ADD them.</text>
  </g>
</svg>"""
        create_or_update_svg_block(l195, 3, 'Row-by-Column Matrix Multiplication Breakdown', 'row_by_column_breakdown', svg_195_p3)

    # =========================================================================
    # LESSON 196: Finding and Interpreting Transformation Matrices
    # =========================================================================
    if l196:
        print(f'Enriching Lesson 196: "{l196.title}"')
        
        # P2 SVG: Unit Square Basis Vector Mapping
        svg_196_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 430" width="100%" height="100%">
  <rect width="840" height="430" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Unit Square: Key to Unlocking Transformation Matrices</text>

  <!-- Left: Original Unit Square -->
  <g transform="translate(40, 65)">
    <rect width="360" height="330" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="180" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. Original Unit Square</text>
    
    <!-- Grid -->
    <line x1="40" y1="270" x2="320" y2="270" stroke="#334155" stroke-width="2"/>
    <line x1="80" y1="50" x2="80" y2="300" stroke="#334155" stroke-width="2"/>
    
    <!-- Unit Square (0,0) (1,0) (1,1) (0,1) -->
    <rect x="80" y="190" width="80" height="80" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2"/>
    
    <!-- Basis Vector i (1,0) -->
    <line x1="80" y1="270" x2="160" y2="270" stroke="#facc15" stroke-width="4"/>
    <polygon points="160,270 152,265 152,275" fill="#facc15"/>
    <text x="115" y="292" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">i (1,0)</text>

    <!-- Basis Vector j (0,1) -->
    <line x1="80" y1="270" x2="80" y2="190" stroke="#4ade80" stroke-width="4"/>
    <polygon points="80,190 75,198 85,198" fill="#4ade80"/>
    <text x="45" y="235" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">j (0,1)</text>
  </g>

  <!-- Right: Transformed Shape & Column Mapping -->
  <g transform="translate(440, 65)">
    <rect width="360" height="330" fill="#1e293b" rx="12" stroke="#facc15" stroke-width="1.5"/>
    <text x="180" y="30" fill="#facc15" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. Transformed Image &amp; Matrix</text>

    <!-- Grid -->
    <line x1="40" y1="270" x2="320" y2="270" stroke="#334155" stroke-width="2"/>
    <line x1="80" y1="50" x2="80" y2="300" stroke="#334155" stroke-width="2"/>

    <!-- Transformed Parallelogram (0,0), (2,1) -> (3,4), (1,3) -->
    <polygon points="80,270 240,210 320,50 160,110" fill="rgba(250, 204, 21, 0.2)" stroke="#facc15" stroke-width="2"/>

    <!-- Transformed i' (2,1) -->
    <line x1="80" y1="270" x2="240" y2="210" stroke="#facc15" stroke-width="3"/>
    <text x="245" y="225" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">i' (2, 1)</text>

    <!-- Transformed j' (1,3) -->
    <line x1="80" y1="270" x2="160" y2="110" stroke="#4ade80" stroke-width="3"/>
    <text x="165" y="105" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">j' (1, 3)</text>

    <!-- Matrix Assembly -->
    <rect x="40" y="280" width="280" height="40" fill="#0f172a" rx="6"/>
    <text x="180" y="305" fill="#38bdf8" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">M = [ i' | j' ] = [ 2  1 ; 1  3 ]</text>
  </g>
</svg>"""
        create_or_update_svg_block(l196, 2, 'The Unit Square Basis Vector Mapping Diagnostic', 'unit_square_mapping', svg_196_p2)

        # P3 SVG: Building Matrix from Basis Point Images
        svg_196_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Building a 2×2 Matrix from Two Basis Points</text>

  <g transform="translate(40, 65)">
    <!-- Column 1 Box -->
    <rect width="360" height="280" fill="#1e293b" rx="12" stroke="#facc15" stroke-width="1.5"/>
    <text x="180" y="35" fill="#facc15" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Step 1: First Column (from (1,0))</text>
    
    <rect x="30" y="60" width="300" height="80" fill="#0f172a" rx="8"/>
    <text x="45" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="14">Where does <tspan fill="#facc15" font-weight="bold">I (1, 0)</tspan> land?</text>
    <text x="45" y="118" fill="#facc15" font-family="monospace" font-size="16" font-weight="bold">I (1,0) → I' (a, b)</text>

    <rect x="30" y="160" width="300" height="90" fill="#0f172a" rx="8"/>
    <text x="45" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">This forms Column 1 of the matrix:</text>
    <text x="150" y="230" fill="#facc15" font-family="monospace" font-size="20" font-weight="bold">[ a ]</text>
    <text x="150" y="245" fill="#facc15" font-family="monospace" font-size="20" font-weight="bold">[ b ]</text>
  </g>

  <g transform="translate(440, 65)">
    <!-- Column 2 Box -->
    <rect width="360" height="280" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="1.5"/>
    <text x="180" y="35" fill="#4ade80" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Step 2: Second Column (from (0,1))</text>
    
    <rect x="30" y="60" width="300" height="80" fill="#0f172a" rx="8"/>
    <text x="45" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="14">Where does <tspan fill="#4ade80" font-weight="bold">J (0, 1)</tspan> land?</text>
    <text x="45" y="118" fill="#4ade80" font-family="monospace" font-size="16" font-weight="bold">J (0,1) → J' (c, d)</text>

    <rect x="30" y="160" width="300" height="90" fill="#0f172a" rx="8"/>
    <text x="45" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">This forms Column 2 of the matrix:</text>
    <text x="150" y="230" fill="#4ade80" font-family="monospace" font-size="20" font-weight="bold">[ c ]</text>
    <text x="150" y="245" fill="#4ade80" font-family="monospace" font-size="20" font-weight="bold">[ d ]</text>
  </g>
</svg>"""
        create_or_update_svg_block(l196, 3, 'Building Matrix Columns from Basis Point Images', 'building_matrix_columns', svg_196_p3)

    # =========================================================================
    # LESSON 197: Successive, Identity and Inverse Transformations
    # =========================================================================
    if l197:
        print(f'Enriching Lesson 197: "{l197.title}"')

        # P2 SVG: Order Matters (T2 T1 != T1 T2)
        svg_197_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Non-Commutative Transformations: T₂T₁ ≠ T₁T₂</text>

  <!-- Left Path: T2 * T1 (Reflection then Rotation) -->
  <g transform="translate(40, 65)">
    <rect width="360" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="180" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Path A: T₂ ∘ T₁ (Reflect X then Rotate 90° CCW)</text>

    <!-- Calculation -->
    <rect x="20" y="55" width="320" height="70" fill="#0f172a" rx="8"/>
    <text x="35" y="85" fill="#cbd5e1" font-family="monospace" font-size="14">[ 0 -1 ] [ 1  0 ]   [ 0  1 ]</text>
    <text x="35" y="108" fill="#cbd5e1" font-family="monospace" font-size="14">[ 1  0 ] [ 0 -1 ] = [ 1  0 ]</text>

    <!-- Diagram -->
    <rect x="20" y="140" width="320" height="140" fill="#0f172a" rx="8"/>
    <text x="160" y="170" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Resulting Composite Matrix:</text>
    <text x="160" y="200" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" text-anchor="middle">Reflection in line <tspan fill="#facc15" font-weight="bold">y = x</tspan></text>
    <text x="160" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Point (2,1) lands at <tspan fill="#4ade80" font-weight="bold">(1,2)</tspan></text>
  </g>

  <!-- Right Path: T1 * T2 (Rotation then Reflection) -->
  <g transform="translate(440, 65)">
    <rect width="360" height="300" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="180" y="30" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Path B: T₁ ∘ T₂ (Rotate 90° CCW then Reflect X)</text>

    <!-- Calculation -->
    <rect x="20" y="55" width="320" height="70" fill="#0f172a" rx="8"/>
    <text x="35" y="85" fill="#cbd5e1" font-family="monospace" font-size="14">[ 1  0 ] [ 0 -1 ]   [ 0 -1 ]</text>
    <text x="35" y="108" fill="#cbd5e1" font-family="monospace" font-size="14">[ 0 -1 ] [ 1  0 ] = [-1  0 ]</text>

    <!-- Diagram -->
    <rect x="20" y="140" width="320" height="140" fill="#0f172a" rx="8"/>
    <text x="160" y="170" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Resulting Composite Matrix:</text>
    <text x="160" y="200" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" text-anchor="middle">Reflection in line <tspan fill="#facc15" font-weight="bold">y = -x</tspan></text>
    <text x="160" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Point (2,1) lands at <tspan fill="#f87171" font-weight="bold">(-1,-2)</tspan></text>
  </g>
</svg>"""
        create_or_update_svg_block(l197, 2, 'Non-Commutative Transformations: Order Matters', 'transformation_order_matters', svg_197_p2)

        # Fix Block 13263 (Page 8): suggested_simulation -> simulation_placeholder
        block_sim = LessonBlock.objects.filter(lesson=l197, page_number=8).first()
        if block_sim:
            block_sim.block_type = 'simulation_placeholder'
            meta = block_sim.metadata or {}
            meta['simulation_key'] = 'math_matrix_transformation'
            meta['archetype'] = 'math_matrix_transformation'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Matrix and Transformation'
            block_sim.metadata = meta
            block_sim.save()
            print(f'  [Page 8] Updated Block {block_sim.id} block_type to simulation_placeholder & set simulation_key!')

    # =========================================================================
    # LESSON 198: Determinant, Area Scale Factor, Shear and Stretch
    # =========================================================================
    if l198:
        print(f'Enriching Lesson 198: "{l198.title}"')

        # P2 SVG: Determinant as Area Scale Factor
        svg_198_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Determinant = Area Scale Factor</text>

  <!-- Left: Area Scaling Case (det M = 6) -->
  <g transform="translate(40, 65)">
    <rect width="360" height="300" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="1.5"/>
    <text x="180" y="30" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Non-Singular Matrix (det M = 6)</text>

    <rect x="30" y="60" width="80" height="80" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2"/>
    <text x="70" y="105" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Area = 1</text>

    <text x="140" y="105" fill="#facc15" font-family="system-ui, sans-serif" font-size="20">→</text>

    <rect x="180" y="60" width="150" height="120" fill="rgba(74, 222, 128, 0.2)" stroke="#4ade80" stroke-width="2"/>
    <text x="255" y="125" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Area = 6</text>

    <rect x="30" y="200" width="300" height="75" fill="#0f172a" rx="8"/>
    <text x="45" y="225" fill="#cbd5e1" font-family="monospace" font-size="14">M = [ 3  0 ; 0  2 ]</text>
    <text x="45" y="250" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold">det(M) = (3)(2) - (0)(0) = 6</text>
  </g>

  <!-- Right: Singular Matrix Collapse Case (det M = 0) -->
  <g transform="translate(440, 65)">
    <rect width="360" height="300" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="180" y="30" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Singular Matrix Collapse (det M = 0)</text>

    <rect x="30" y="60" width="80" height="80" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2"/>
    <text x="70" y="105" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Area = 1</text>

    <text x="140" y="105" fill="#facc15" font-family="system-ui, sans-serif" font-size="20">→</text>

    <line x1="180" y1="140" x2="310" y2="60" stroke="#f87171" stroke-width="4"/>
    <text x="245" y="125" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Area = 0 (Line)</text>

    <rect x="30" y="200" width="300" height="75" fill="#0f172a" rx="8"/>
    <text x="45" y="225" fill="#cbd5e1" font-family="monospace" font-size="14">M = [ 2  4 ; 1  2 ]</text>
    <text x="45" y="250" fill="#f87171" font-family="monospace" font-size="14" font-weight="bold">det(M) = (2)(2) - (4)(1) = 0</text>
  </g>
</svg>"""
        create_or_update_svg_block(l198, 2, 'Determinant as Area Scale Factor Diagnostic', 'determinant_area_scale', svg_198_p2)

        # P3 SVG: Determinant Cross-Diagonal Rule Formula
        svg_198_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The 2×2 Determinant Cross-Diagonal Formula</text>

  <g transform="translate(120, 65)">
    <rect width="600" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Matrix Box -->
    <rect x="50" y="50" width="220" height="180" fill="#0f172a" rx="10" stroke="#334155"/>
    <text x="70" y="110" fill="#4ade80" font-family="monospace" font-size="36" font-weight="bold">a</text>
    <text x="210" y="110" fill="#f87171" font-family="monospace" font-size="36" font-weight="bold">b</text>
    <text x="70" y="190" fill="#f87171" font-family="monospace" font-size="36" font-weight="bold">c</text>
    <text x="210" y="190" fill="#4ade80" font-family="monospace" font-size="36" font-weight="bold">d</text>

    <!-- Diagonal Arrow 1: a -> d (Green / Positive) -->
    <line x1="95" y1="115" x2="200" y2="175" stroke="#4ade80" stroke-width="4"/>
    <polygon points="200,175 190,170 195,182" fill="#4ade80"/>

    <!-- Diagonal Arrow 2: c -> b (Red / Negative) -->
    <line x1="95" y1="175" x2="200" y2="115" stroke="#f87171" stroke-width="4"/>
    <polygon points="200,115 195,127 190,120" fill="#f87171"/>

    <!-- Formula Breakdown -->
    <rect x="300" y="50" width="250" height="180" fill="#0f172a" rx="10" stroke="#38bdf8"/>
    <text x="320" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="16" font-weight="bold">Formula:</text>
    <text x="320" y="125" fill="#38bdf8" font-family="monospace" font-size="22" font-weight="bold">det(M) = ad - bc</text>
    <text x="320" y="165" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13">+ Main diagonal: a × d</text>
    <text x="320" y="190" fill="#f87171" font-family="system-ui, sans-serif" font-size="13">- Off diagonal: b × c</text>
  </g>
</svg>"""
        create_or_update_svg_block(l198, 3, 'The 2x2 Determinant Cross-Diagonal Formula Diagram', 'determinant_cross_formula', svg_198_p3)

    print('\n=== ENRICHMENT OF TOPIC 1 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic1_matrices()
