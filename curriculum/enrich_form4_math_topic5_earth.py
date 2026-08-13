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

def enrich_topic5_earth():
    print('=== ENRICHING FORM 4 MATH TOPIC 5: LONGITUDES AND LATITUDES (FULL DIAGRAM LABELS) ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=5).first()
    if not topic:
        print('Error: Topic 5 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 5, found {len(lessons)}')
        return

    l211, l212, l213, l214 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 211: Earth Coordinates and Radii of Great and Small Circles
    # =========================================================================
    if l211:
        print(f'Enriching Lesson 211: "{l211.title}"')

        # P2 SVG: Fully Labelled 3D Earth Globe (Center O, Poles N/S, Equator, Parallel alpha, Radii R/r)
        svg_211_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">3D Earth Globe: Fully Labelled Great Circle (Equator) vs Small Circle (Parallel α)</text>
  <g transform="translate(30, 55)">
    <rect width="420" height="340" fill="#0f172a" rx="12" stroke="#1e293b"/>
    <circle cx="210" cy="170" r="110" fill="none" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Polar Axis N - S -->
    <line x1="210" y1="40" x2="210" y2="300" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 3"/>
    <circle cx="210" cy="60" r="4" fill="#38bdf8"/><text x="210" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">North Pole N</text>
    <circle cx="210" cy="280" r="4" fill="#38bdf8"/><text x="210" y="300" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">South Pole S</text>

    <!-- Earth Center O -->
    <circle cx="210" cy="170" r="5" fill="#4ade80"/><text x="185" y="175" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Center O</text>

    <!-- Equator (Great Circle, R) -->
    <ellipse cx="210" cy="170" rx="110" ry="28" fill="none" stroke="#4ade80" stroke-width="2.5"/>
    <text x="225" y="190" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Equator (R = 6370 km)</text>

    <!-- Parallel Latitude α (Small Circle, r) -->
    <ellipse cx="210" cy="105" rx="90" ry="20" fill="none" stroke="#facc15" stroke-width="2.5"/>
    <circle cx="210" cy="105" r="4" fill="#facc15"/><text x="145" y="100" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Center C'</text>
    <line x1="210" y1="105" x2="300" y2="105" stroke="#facc15" stroke-width="2"/>
    <text x="250" y="98" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">r = R cos α</text>

    <!-- Radius R from O to Parallel Vertex P(300,105) -->
    <line x1="210" y1="170" x2="300" y2="105" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 2"/>
    <circle cx="300" cy="105" r="5" fill="#38bdf8"/><text x="310" y="110" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Point P(α, λ)</text>

    <!-- Angle of Latitude α at O -->
    <path d="M 250 170 A 40 40 0 0 0 245 145" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="260" y="158" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">α</text>
  </g>

  <g transform="translate(470, 55)">
    <rect width="340" height="340" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Fully Labelled Geometry Rules:</text>

    <rect x="20" y="60" width="300" height="75" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="35" y="85" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">1. Great Circle (Equator / Meridians)</text>
    <text x="35" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Passes through Earth Center O. Radius = R = 6370 km</text>

    <rect x="20" y="150" width="300" height="75" fill="#0f172a" rx="8" stroke="#facc15"/>
    <text x="35" y="175" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">2. Small Circle (Parallel of Latitude α)</text>
    <text x="35" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Center C' is on polar axis. Radius r = R cos α</text>

    <rect x="20" y="240" width="300" height="75" fill="#0f172a" rx="8" stroke="#38bdf8"/>
    <text x="35" y="265" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">3. Latitude Angle α</text>
    <text x="35" y="290" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Angle subtended at Earth Center O above Equator</text>
  </g>
</svg>"""
        create_or_update_svg_block(l211, 2, '3D Earth Globe & Sliced Circle Geometry', 'earth_sliced_circles', svg_211_p2)

        # P3 SVG: Small Circle Radius Formula Breakdown
        svg_211_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Small Circle Radius Formula Anatomy: Right Triangle △OC'P</text>

  <g transform="translate(40, 55)">
    <rect width="420" height="320" fill="#0f172a" rx="12" stroke="#1e293b"/>

    <!-- Right Triangle △OC'P: O(80,240), C'(80,80), P(320,80) -->
    <polygon points="80,240 80,80 320,80" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="2"/>

    <!-- Sides: OC' (Vertical), C'P (Small Circle Radius r), OP (Earth Radius R) -->
    <line x1="80" y1="80" x2="320" y2="80" stroke="#facc15" stroke-width="4"/> <!-- Small Circle Radius r -->
    <text x="200" y="70" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">r = R cos α (Adjacent)</text>

    <line x1="80" y1="240" x2="320" y2="80" stroke="#38bdf8" stroke-width="4"/> <!-- Earth Radius R -->
    <text x="200" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">R = 6370 km (Hypotenuse)</text>

    <!-- Right Angle at C'(80,80) -->
    <rect x="80" y="80" width="16" height="16" fill="none" stroke="#4ade80" stroke-width="2"/>

    <!-- Angle alpha at O(80,240) -->
    <path d="M 80 200 A 40 40 0 0 1 115 220" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="100" y="200" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">α (Latitude)</text>

    <!-- Vertices O, C', P -->
    <circle cx="80" cy="240" r="5" fill="#4ade80"/><text x="50" y="260" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">O (Earth Center)</text>
    <circle cx="80" cy="80" r="5" fill="#facc15"/><text x="45" y="70" fill="#facc15" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">C' (Parallel Center)</text>
    <circle cx="320" cy="80" r="5" fill="#38bdf8"/><text x="330" y="85" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">P (Point on Latitude α)</text>
  </g>

  <g transform="translate(480, 55)">
    <rect width="330" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Formula Derivation:</text>

    <text x="25" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">In Right Triangle △OC'P:</text>
    <text x="25" y="105" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold">cos α = Adjacent / Hypotenuse</text>
    <text x="25" y="135" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold">cos α = C'P / OP = r / R</text>

    <rect x="20" y="170" width="290" height="70" fill="#0f172a" rx="8" stroke="#facc15"/>
    <text x="165" y="210" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">r = R cos α</text>
  </g>
</svg>"""
        create_or_update_svg_block(l211, 3, 'Small Circle Radius Formula Anatomy (r = R cos α)', 'small_circle_radius_formula', svg_211_p3)

        # P4 SVG: Worked Example 1 - Longitude Difference Across Prime Meridian
        svg_211_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Worked Example 1: Longitude Difference Δλ Across Prime Meridian (0°)</text>

  <g transform="translate(40, 55)">
    <rect width="420" height="320" fill="#0f172a" rx="12" stroke="#1e293b"/>

    <!-- Parallel Line (Latitude 30°N) -->
    <line x1="40" y1="160" x2="380" y2="160" stroke="#facc15" stroke-width="3"/>
    <text x="390" y="165" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Lat 30°N</text>

    <!-- Prime Meridian 0° (Green Center) -->
    <line x1="210" y1="40" x2="210" y2="280" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="4 3"/>
    <text x="210" y="30" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Prime Meridian 0°</text>

    <!-- Point A(30°N, 20°W) on Left -->
    <line x1="110" y1="60" x2="110" y2="260" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="110" cy="160" r="6" fill="#38bdf8"/>
    <text x="60" y="150" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">A(30°N, 20°W)</text>

    <!-- Point B(30°N, 40°E) on Right -->
    <line x1="310" y1="60" x2="310" y2="260" stroke="#e879f9" stroke-width="2"/>
    <circle cx="310" cy="160" r="6" fill="#e879f9"/>
    <text x="315" y="150" fill="#e879f9" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">B(30°N, 40°E)</text>

    <!-- Angular Gaps -->
    <text x="160" y="185" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">20°W</text>
    <text x="250" y="185" fill="#e879f9" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">40°E</text>

    <!-- Total Gap Arrow -->
    <line x1="110" y1="210" x2="310" y2="210" stroke="#4ade80" stroke-width="3"/>
    <text x="210" y="235" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Δλ = 20° + 40° = 60°</text>
  </g>

  <g transform="translate(480, 55)">
    <rect width="330" height="320" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Rule for Opposite Hemispheres:</text>

    <text x="25" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">When points lie in opposite hemispheres (W &amp; E):</text>
    <rect x="20" y="100" width="290" height="60" fill="#0f172a" rx="8" stroke="#4ade80"/>
    <text x="165" y="135" fill="#4ade80" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">Δλ = λ₁ + λ₂ (ADD)</text>

    <text x="25" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Calculation for A and B:</text>
    <text x="25" y="225" fill="#38bdf8" font-family="monospace" font-size="14" font-weight="bold">Δλ = 20° + 40° = 60°</text>
  </g>
</svg>"""
        create_or_update_svg_block(l211, 4, 'Worked Example 1: Longitude Difference Across Prime Meridian', 'worked_example_lon_diff', svg_211_p4)

        # P9 SVG: Common Error - Polar Radius Assumption Warning
        svg_211_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#f87171" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">Common Error: The Polar Radius Assumption Warning (r ≠ R for α > 0°)</text>

  <g transform="translate(60, 55)">
    <rect width="720" height="320" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>

    <g transform="translate(40, 40)">
      <rect width="300" height="240" fill="#0f172a" rx="10" stroke="#f87171"/>
      <text x="150" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">❌ WRONG ASSUMPTION</text>
      <text x="20" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Using Earth Radius R = 6370 km</text>
      <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">for small latitude circles!</text>
      <text x="20" y="145" fill="#f87171" font-family="monospace" font-size="15" font-weight="bold">r = R (FORGOT cos α)</text>
      <text x="20" y="185" fill="#f87171" font-family="system-ui, sans-serif" font-size="12">Overestimates parallel distance!</text>
    </g>

    <g transform="translate(380, 40)">
      <rect width="300" height="240" fill="#0f172a" rx="10" stroke="#4ade80"/>
      <text x="150" y="35" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">✓ CORRECT FORMULA</text>
      <text x="20" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Parallel radius shrinks with latitude α:</text>
      <text x="20" y="125" fill="#4ade80" font-family="monospace" font-size="16" font-weight="bold">r = R cos α</text>
      <text x="20" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">At Lat 60°: cos 60° = 0.5 ⟹ r = 0.5R</text>
      <text x="20" y="195" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12">Parallel radius is exactly HALF of Earth R!</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l211, 9, 'Common Error: The Polar Radius Assumption Warning', 'misconception_polar_radius', svg_211_p9)

        # Fix Block 13592 (Page 8)
        block_sim211 = LessonBlock.objects.filter(lesson=l211, page_number=8).first()
        if block_sim211:
            block_sim211.block_type = 'simulation_placeholder'
            meta = block_sim211.metadata or {}
            meta['simulation_key'] = 'math_earth_globe_explorer'
            meta['archetype'] = 'math_earth_globe_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Longitudes and Latitudes'
            block_sim211.metadata = meta
            block_sim211.save()
            print(f'  [Page 8] Updated Block {block_sim211.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 212: Distance Calculation Along Great Circles
    # =========================================================================
    if l212:
        print(f'Enriching Lesson 212: "{l212.title}"')

        # P2 SVG: Nautical Mile Definition
        svg_212_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">The 1-Minute-of-Arc Nautical Mile Principle</text>
  <g transform="translate(60, 55)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="110" fill="#facc15" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">1' of Arc = 1 Nautical Mile (nm)</text>
    <text x="360" y="160" fill="#4ade80" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">1° of Arc = 60 Nautical Miles (nm)</text>
    <text x="360" y="220" fill="#38bdf8" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle">Great Circle Distance: D = 60 × θ (nm)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l212, 2, 'Nautical Mile Definition & Great Circle Arc Length', 'nautical_mile_definition', svg_212_p2)

        # P3 SVG: Great Circle Distance Formula Flowchart
        svg_212_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Great Circle Distance Formula Flowchart</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="100" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">In Nautical Miles: D = 60 × θ (nm)</text>
    <text x="360" y="150" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">In Kilometers: D = (θ / 360) × 2πR (km)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l212, 3, 'Great Circle Distance Formula Flowchart', 'great_circle_distance_formula', svg_212_p3)

        # P4 SVG: Worked Example 1 - Meridian Distance
        svg_212_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Meridian Distance Solution</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">θ = 50°N + 20°S = 70° ⟹ D = 60 × 70 = 4200 nm</text>
  </g>
</svg>"""
        create_or_update_svg_block(l212, 4, 'Worked Example 1: Meridian Distance Calculation', 'worked_example_meridian_distance', svg_212_p4)

        # P9 SVG: Common Misconception - Equator Crossing
        svg_212_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Subtracting Across the Equator Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Opposite Hemispheres (N and S) ⟹ ADD latitude angles!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l212, 9, 'Common Error: Equator Crossing Angle Warning', 'misconception_equator_crossing', svg_212_p9)

        # Fix Block 13603 (Page 8)
        block_sim212 = LessonBlock.objects.filter(lesson=l212, page_number=8).first()
        if block_sim212:
            block_sim212.block_type = 'simulation_placeholder'
            meta = block_sim212.metadata or {}
            meta['simulation_key'] = 'math_earth_globe_explorer'
            meta['archetype'] = 'math_earth_globe_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Longitudes and Latitudes'
            block_sim212.metadata = meta
            block_sim212.save()
            print(f'  [Page 8] Updated Block {block_sim212.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 213: Distance Calculation Along Parallels of Latitude
    # =========================================================================
    if l213:
        print(f'Enriching Lesson 213: "{l213.title}"')

        # P2 SVG: Small Circle Arc Length
        svg_213_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Small Circle Arc Length vs Great Circle Shortcut</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">d = 60 × Δλ × cos α (nm)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l213, 2, 'Small Circle Arc Length vs Great Circle Route', 'small_circle_arc_length', svg_213_p2)

        # P3 SVG: Parallel Distance Formula
        svg_213_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Parallel Small Circle Distance Formula Diagram</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">d = 60 × Δλ × cos α (nm)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l213, 3, 'Parallel Small Circle Distance Formula Diagram', 'parallel_distance_formula', svg_213_p3)

        # P4 SVG: Worked Example 1 - Latitude 60N Distance
        svg_213_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Distance Along Latitude 60°N Solution</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">d = 60 × 40° × cos(60°) = 2400 × 0.5 = 1200 nm</text>
  </g>
</svg>"""
        create_or_update_svg_block(l213, 4, 'Worked Example 1: Distance Along Latitude 60°N Solution', 'worked_example_latitude_distance', svg_213_p4)

        # P9 SVG: Common Misconception - Forgetting cos alpha
        svg_213_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Forgetting the cos α Multiplier Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Moving along parallels of latitude MUST include cos α factor!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l213, 9, 'Common Error: Forgetting cos α Multiplier Warning', 'misconception_cos_alpha_multiplier', svg_213_p9)

        # Fix Block 13614 (Page 8)
        block_sim213 = LessonBlock.objects.filter(lesson=l213, page_number=8).first()
        if block_sim213:
            block_sim213.block_type = 'simulation_placeholder'
            meta = block_sim213.metadata or {}
            meta['simulation_key'] = 'math_earth_globe_explorer'
            meta['archetype'] = 'math_earth_globe_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Longitudes and Latitudes'
            block_sim213.metadata = meta
            block_sim213.save()
            print(f'  [Page 8] Updated Block {block_sim213.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 214: Longitude-Time Calculations and Speed in Knots
    # =========================================================================
    if l214:
        print(f'Enriching Lesson 214: "{l214.title}"')

        # P2 SVG: Earth Rotation & Time Conversion
        svg_214_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Earth Rotation &amp; Longitude-Time Conversion Rate</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="120" fill="#facc15" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">15° of Longitude = 1 Hour</text>
    <text x="360" y="160" fill="#4ade80" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">1° of Longitude = 4 Minutes</text>
  </g>
</svg>"""
        create_or_update_svg_block(l214, 2, 'Earth Rotation & Longitude-Time Conversion Rate', 'earth_rotation_time_rate', svg_214_p2)

        # P3 SVG: Speed in Knots Mnemonic
        svg_214_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Speed in Knots &amp; Time Difference Mnemonic</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">1 Knot = 1 Nautical Mile per Hour (1 nm/h)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l214, 3, 'Speed in Knots & Time Difference Mnemonic', 'speed_in_knots_mnemonic', svg_214_p3)

        # P4 SVG: Worked Example 1 - Local Time Shift
        svg_214_p4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Worked Example 1: Local Time Shift Solution (East is Later)</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360" y="140" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">0° (12:00) ⟹ 45°E: +3 Hours ⟹ 15:00 (3:00 PM)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l214, 4, 'Worked Example 1: Local Time Shift Solution', 'worked_example_time_shift', svg_214_p4)

        # P9 SVG: Common Misconception - Speed Unit Mismatch
        svg_214_p9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Common Error: Speed Unit Mismatch (km/h vs Knots) Warning</text>
  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="360" y="140" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Never mix knots with kilometers! 1 Knot = 1 Nautical Mile per hour.</text>
  </g>
</svg>"""
        create_or_update_svg_block(l214, 9, 'Common Error: Speed Unit Mismatch Warning', 'misconception_speed_unit_mismatch', svg_214_p9)

        # Fix Block 13625 (Page 8)
        block_sim214 = LessonBlock.objects.filter(lesson=l214, page_number=8).first()
        if block_sim214:
            block_sim214.block_type = 'simulation_placeholder'
            meta = block_sim214.metadata or {}
            meta['simulation_key'] = 'math_earth_globe_explorer'
            meta['archetype'] = 'math_earth_globe_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Longitudes and Latitudes'
            block_sim214.metadata = meta
            block_sim214.save()
            print(f'  [Page 8] Updated Block {block_sim214.id} block_type to simulation_placeholder')

    print('\n=== ENRICHMENT OF TOPIC 5 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic5_earth()
