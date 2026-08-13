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

def enrich_topic4_trigonometry():
    print('=== ENRICHING FORM 4 MATH TOPIC 4: TRIGONOMETRY III (MULTI-CARD VISUALS) ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=4).first()
    if not topic:
        print('Error: Topic 4 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 4, found {len(lessons)}')
        return

    l207, l208, l209, l210 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 207: The Pythagorean Trigonometric Identity
    # =========================================================================
    if l207:
        print(f'Enriching Lesson 207: "{l207.title}"')

        # P2 SVG: Unit Circle Pythagorean Identity
        svg_207_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Unit Circle Origin: Why cos²θ + sin²θ = 1</text>
  <g transform="translate(40, 65)">
    <rect width="400" height="300" fill="#0f172a" rx="12" stroke="#1e293b"/>
    <circle cx="200" cy="150" r="100" fill="none" stroke="#334155" stroke-width="2"/>
    <line x1="80" y1="150" x2="320" y2="150" stroke="#475569" stroke-width="1.5"/>
    <line x1="200" y1="30" x2="200" y2="270" stroke="#475569" stroke-width="1.5"/>
    <polygon points="200,150 270,150 270,79.3" fill="rgba(56, 189, 248, 0.2)"/>
    <line x1="200" y1="150" x2="270" y2="79.3" stroke="#facc15" stroke-width="3"/>
    <line x1="200" y1="150" x2="270" y2="150" stroke="#38bdf8" stroke-width="3"/>
    <line x1="270" y1="150" x2="270" y2="79.3" stroke="#4ade80" stroke-width="3"/>
    <circle cx="270" cy="79.3" r="5" fill="#facc15"/>
    <text x="235" y="165" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">cos θ</text>
    <text x="280" y="120" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">sin θ</text>
    <text x="225" y="105" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">r = 1</text>
    <text x="280" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">(cos θ, sin θ)</text>
  </g>
  <g transform="translate(470, 65)">
    <rect width="330" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Pythagorean Theorem Connection</text>
    <rect x="25" y="55" width="280" height="75" fill="#0f172a" rx="8" stroke="#334155"/>
    <text x="40" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">In Right △: adj² + opp² = hyp²</text>
    <text x="40" y="108" fill="#facc15" font-family="monospace" font-size="16" font-weight="bold">(cos θ)² + (sin θ)² = 1²</text>
    <rect x="25" y="150" width="280" height="125" fill="#0f172a" rx="8" stroke="#38bdf8"/>
    <text x="40" y="180" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold">cos²θ + sin²θ = 1</text>
    <text x="40" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Rearrangement 1: <tspan fill="#4ade80">sin²θ = 1 - cos²θ</tspan></text>
    <text x="40" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Rearrangement 2: <tspan fill="#38bdf8">cos²θ = 1 - sin²θ</tspan></text>
  </g>
</svg>"""
        create_or_update_svg_block(l207, 2, 'Unit Circle Pythagorean Identity Origin', 'unit_circle_pythagoras_identity', svg_207_p2)

        # P3 SVG: Identity Transformation Network
        svg_207_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Trigonometric Identity Network</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="210" y="30" width="300" height="70" fill="#0f172a" rx="10" stroke="#facc15" stroke-width="2"/>
    <text x="360" y="72" fill="#facc15" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle">sin²θ + cos²θ = 1</text>
    <line x1="260" y1="100" x2="160" y2="170" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
    <rect x="40" y="170" width="240" height="80" fill="#0f172a" rx="8" stroke="#38bdf8"/>
    <text x="160" y="200" fill="#38bdf8" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">tan²θ + 1 = sec²θ</text>
    <line x1="460" y1="100" x2="560" y2="170" stroke="#4ade80" stroke-width="2" stroke-dasharray="4 3"/>
    <rect x="440" y="170" width="240" height="80" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="560" y="200" fill="#4ade80" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">1 + cot²θ = csc²θ</text>
  </g>
</svg>"""
        create_or_update_svg_block(l207, 3, 'Trigonometric Identity Transformation Flowchart', 'identity_transformation_network', svg_207_p3)

        # P4 SVG: Worked Example 1 - Complementary Ratios
        svg_207_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example Visual: Complementary Ratios sin(90° - θ) = cos θ</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <g transform="translate(40, 30)">
      <polygon points="40,200 220,200 220,60" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="80" y="190" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">θ</text>
      <text x="195" y="95" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">90°-θ</text>
      <text x="130" y="220" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12">b (adj to θ / opp to 90°-θ)</text>
      <text x="230" y="140" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12">a (opp to θ)</text>
    </g>
    <g transform="translate(380, 30)">
      <rect width="300" height="210" fill="#0f172a" rx="8" stroke="#38bdf8"/>
      <text x="150" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Co-Ratio Identity Rule:</text>
      <text x="25" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">• sin(90° - θ) = cos θ</text>
      <text x="25" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">• cos(90° - θ) = sin θ</text>
      <text x="25" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">• tan(90° - θ) = 1 / tan θ</text>
      <rect x="20" y="165" width="260" height="35" fill="#1e293b" rx="6" stroke="#4ade80"/>
      <text x="150" y="188" fill="#4ade80" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">If sin 30° = 0.5 ⟹ cos 60° = 0.5</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l207, 4, 'Worked Example 1: Complementary Trigonometric Ratios', 'worked_example_complementary_ratios', svg_207_p4)

        # P9 SVG: Common Misconception - Square Index Fallacy
        svg_207_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: The Square Index Fallacy (sin²θ ≠ sin θ²)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <g transform="translate(30, 30)">
      <rect width="310" height="210" fill="#0f172a" rx="8" stroke="#4ade80"/>
      <text x="155" y="35" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">CORRECT NOTATION</text>
      <text x="155" y="80" fill="#4ade80" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">sin²(30°)</text>
      <text x="155" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">= (sin 30°)² = (0.5)²</text>
      <text x="155" y="160" fill="#facc15" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle">= 0.25</text>
    </g>
    <g transform="translate(380, 30)">
      <rect width="310" height="210" fill="#0f172a" rx="8" stroke="#f87171"/>
      <text x="155" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">INCORRECT CONFUSION</text>
      <text x="155" y="80" fill="#f87171" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">sin(30°²)</text>
      <text x="155" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">= sin(900°) = sin(180°)</text>
      <text x="155" y="160" fill="#f87171" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle">= 0.00 (WRONG!)</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l207, 9, 'Common Error: The Square Index Fallacy Visual Warning', 'misconception_square_index_fallacy', svg_207_p9)

        # Fix Block 13504 (Page 8)
        block_sim207 = LessonBlock.objects.filter(lesson=l207, page_number=8).first()
        if block_sim207:
            block_sim207.block_type = 'simulation_placeholder'
            meta = block_sim207.metadata or {}
            meta['simulation_key'] = 'math_trigonometry_wave_explorer'
            meta['archetype'] = 'math_trigonometry_wave_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Trigonometry III'
            block_sim207.metadata = meta
            block_sim207.save()
            print(f'  [Page 8] Updated Block {block_sim207.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 208: Graphing Sine, Cosine, and Tangent Functions: Amplitude and Period
    # =========================================================================
    if l208:
        print(f'Enriching Lesson 208: "{l208.title}"')

        # P2 SVG: Anatomy of a Sine Wave
        svg_208_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Anatomy of a Sinusoidal Wave y = A sin(Bx)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="60" y1="150" x2="660" y2="150" stroke="#475569" stroke-width="2"/>
    <path d="M 60 150 Q 210 30 360 150 T 660 150" fill="none" stroke="#10b981" stroke-width="4"/>
    <line x1="210" y1="150" x2="210" y2="70" stroke="#facc15" stroke-width="2.5"/>
    <text x="220" y="115" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Amplitude (A)</text>
    <line x1="60" y1="260" x2="660" y2="260" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="360" y="280" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Period T = 360° / B</text>
  </g>
</svg>"""
        create_or_update_svg_block(l208, 2, 'Anatomy of a Sinusoidal Wave Diagram', 'sine_wave_anatomy', svg_208_p2)

        # P3 SVG: Amplitude vs Period Wave Scaling
        svg_208_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Wave Scaling: Amplitude (A) vs. Frequency (B)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="60" y1="150" x2="660" y2="150" stroke="#475569" stroke-width="2"/>
    <path d="M 60 150 Q 210 50 360 150 T 660 150" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.6"/>
    <path d="M 60 150 Q 210 -10 360 150 T 660 150" fill="none" stroke="#facc15" stroke-width="3"/>
    <path d="M 60 150 Q 135 50 210 150 T 360 150 Q 435 50 510 150 T 660 150" fill="none" stroke="#4ade80" stroke-width="3"/>
  </g>
</svg>"""
        create_or_update_svg_block(l208, 3, 'Amplitude vs Period Wave Scaling Comparison', 'wave_scaling_comparison', svg_208_p3)

        # P9 SVG: Misconception - Linearity Illusion
        svg_208_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: The Linearity Illusion (sin 2x ≠ 2 sin x)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <g transform="translate(30, 30)">
      <rect width="310" height="210" fill="#0f172a" rx="8" stroke="#4ade80"/>
      <text x="155" y="35" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">sin(2x) : Frequency Doubler</text>
      <text x="155" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Compresses Period to T = 180°</text>
      <text x="155" y="120" fill="#4ade80" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">Peak stays at y = 1.0</text>
    </g>
    <g transform="translate(380, 30)">
      <rect width="310" height="210" fill="#0f172a" rx="8" stroke="#f87171"/>
      <text x="155" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2 sin(x) : Amplitude Doubler</text>
      <text x="155" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Keeps Period T = 360°</text>
      <text x="155" y="120" fill="#f87171" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">Stretches Peak to y = 2.0!</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l208, 9, 'Common Error: Linearity Illusion Visual Warning', 'misconception_linearity_illusion', svg_208_p9)

        # Fix Block 13515 (Page 8)
        block_sim208 = LessonBlock.objects.filter(lesson=l208, page_number=8).first()
        if block_sim208:
            block_sim208.block_type = 'simulation_placeholder'
            meta = block_sim208.metadata or {}
            meta['simulation_key'] = 'math_trigonometry_wave_explorer'
            meta['archetype'] = 'math_trigonometry_wave_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Trigonometry III'
            block_sim208.metadata = meta
            block_sim208.save()
            print(f'  [Page 8] Updated Block {block_sim208.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 209: Wave Transformations and Phase Shifts
    # =========================================================================
    if l209:
        print(f'Enriching Lesson 209: "{l209.title}"')

        # P2 SVG: Phase Shift Visualized
        svg_209_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Phase Shift: Horizontal Translation of Wave Curves</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="60" y1="150" x2="660" y2="150" stroke="#475569" stroke-width="2"/>
    <path d="M 120 150 Q 240 50 360 150 T 600 150" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4 2"/>
    <path d="M 60 150 Q 180 50 300 150 T 540 150" fill="none" stroke="#4ade80" stroke-width="3.5"/>
  </g>
</svg>"""
        create_or_update_svg_block(l209, 2, 'Phase Shift: Horizontal Translation of Wave Curves', 'phase_shift_visualized', svg_209_p2)

        # Fix Block 13526 (Page 8)
        block_sim209 = LessonBlock.objects.filter(lesson=l209, page_number=8).first()
        if block_sim209:
            block_sim209.block_type = 'simulation_placeholder'
            meta = block_sim209.metadata or {}
            meta['simulation_key'] = 'math_trigonometry_wave_explorer'
            meta['archetype'] = 'math_trigonometry_wave_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Trigonometry III'
            block_sim209.metadata = meta
            block_sim209.save()
            print(f'  [Page 8] Updated Block {block_sim209.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 210: Solving Trigonometric Equations Analytically and Graphically
    # =========================================================================
    if l210:
        print(f'Enriching Lesson 210: "{l210.title}"')

        # P2 SVG: Wave Cutting Principle
        svg_210_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">The Wave-Cutting Principle: Graphical Root Solving (sin x = k)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="60" y1="170" x2="660" y2="170" stroke="#475569" stroke-width="2"/>
    <path d="M 60 170 Q 210 70 360 170 T 660 170" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
    <line x1="60" y1="120" x2="660" y2="120" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 3"/>
    <circle cx="110" cy="120" r="7" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <circle cx="310" cy="120" r="7" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
  </g>
</svg>"""
        create_or_update_svg_block(l210, 2, 'The Wave-Cutting Principle: Graphical Root Solving', 'wave_cutting_principle', svg_210_p2)

        # P3 SVG: CAST Quadrants
        svg_210_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">CAST Quadrant Sign Diagram &amp; Reference Angles</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="60" y1="150" x2="660" y2="150" stroke="#475569" stroke-width="2.5"/>
    <line x1="360" y1="30" x2="360" y2="270" stroke="#475569" stroke-width="2.5"/>
    <rect x="90" y="45" width="240" height="90" fill="rgba(56, 189, 248, 0.15)" rx="8" stroke="#38bdf8"/>
    <rect x="390" y="45" width="240" height="90" fill="rgba(74, 222, 128, 0.15)" rx="8" stroke="#4ade80"/>
    <rect x="90" y="165" width="240" height="90" fill="rgba(245, 158, 11, 0.15)" rx="8" stroke="#facc15"/>
    <rect x="390" y="165" width="240" height="90" fill="rgba(248, 113, 113, 0.15)" rx="8" stroke="#f87171"/>
  </g>
</svg>"""
        create_or_update_svg_block(l210, 3, 'CAST Quadrant Sign Diagram & Reference Angles', 'cast_quadrant_diagram', svg_210_p3)

        # Fix Block 13537 (Page 8)
        block_sim210 = LessonBlock.objects.filter(lesson=l210, page_number=8).first()
        if block_sim210:
            block_sim210.block_type = 'simulation_placeholder'
            meta = block_sim210.metadata or {}
            meta['simulation_key'] = 'math_trigonometry_wave_explorer'
            meta['archetype'] = 'math_trigonometry_wave_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Trigonometry III'
            block_sim210.metadata = meta
            block_sim210.save()
            print(f'  [Page 8] Updated Block {block_sim210.id} block_type to simulation_placeholder')

    print('\n=== ENRICHMENT OF TOPIC 4 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic4_trigonometry()
