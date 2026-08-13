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

def enrich_topic2_statistics():
    print('=== ENRICHING FORM 4 MATH TOPIC 2: STATISTICS II ===\n')
    topic = Topic.objects.filter(subject__name='Mathematics', order=2).first()
    if not topic:
        print('Error: Topic 2 Mathematics not found!')
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
    if len(lessons) < 4:
        print(f'Error: Expected 4 lessons in Topic 2, found {len(lessons)}')
        return

    l199, l200, l201, l202 = lessons[0], lessons[1], lessons[2], lessons[3]

    # =========================================================================
    # LESSON 199: Calculating Mean Using Assumed Mean and Step-Deviation
    # =========================================================================
    if l199:
        print(f'Enriching Lesson 199: "{l199.title}"')

        # P2 SVG: Assumed Mean Benchmark Shift
        svg_199_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Assumed Mean (A): Visual Benchmark Baseline</text>

  <!-- Left: Original Values vs Assumed Mean Baseline -->
  <g transform="translate(40, 65)">
    <rect width="400" height="300" fill="#0f172a" rx="12" stroke="#1e293b"/>
    <text x="200" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Deviations d = x - A (Benchmark A = 50)</text>

    <!-- Benchmark Line y = 50 -->
    <line x1="40" y1="160" x2="360" y2="160" stroke="#facc15" stroke-width="2.5" stroke-dasharray="6 4"/>
    <text x="365" y="165" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">A = 50</text>

    <!-- Data Bars and Deviations -->
    <!-- x = 30 (d = -20) -->
    <rect x="70" y="160" width="24" height="70" fill="rgba(248, 113, 113, 0.4)" stroke="#f87171" stroke-width="1.5"/>
    <text x="82" y="248" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">-20</text>
    <text x="82" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(30)</text>

    <!-- x = 40 (d = -10) -->
    <rect x="130" y="160" width="24" height="35" fill="rgba(248, 113, 113, 0.4)" stroke="#f87171" stroke-width="1.5"/>
    <text x="142" y="212" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">-10</text>
    <text x="142" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(40)</text>

    <!-- x = 50 (d = 0) -->
    <circle cx="202" cy="160" r="5" fill="#facc15"/>
    <text x="202" y="180" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0</text>
    <text x="202" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(50)</text>

    <!-- x = 65 (d = +15) -->
    <rect x="250" y="107" width="24" height="53" fill="rgba(74, 222, 128, 0.4)" stroke="#4ade80" stroke-width="1.5"/>
    <text x="262" y="98" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">+15</text>
    <text x="262" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(65)</text>

    <!-- x = 75 (d = +25) -->
    <rect x="310" y="72" width="24" height="88" fill="rgba(74, 222, 128, 0.4)" stroke="#4ade80" stroke-width="1.5"/>
    <text x="322" y="63" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">+25</text>
    <text x="322" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(75)</text>
  </g>

  <!-- Right: Algebraic Relationship -->
  <g transform="translate(470, 65)">
    <rect width="330" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Assumed Mean Mean Formula</text>

    <rect x="25" y="55" width="280" height="90" fill="#0f172a" rx="8" stroke="#334155"/>
    <text x="40" y="88" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold">x̄ = A + d̄</text>
    <text x="40" y="120" fill="#4ade80" font-family="monospace" font-size="16">x̄ = A + (Σ fd / Σ f)</text>

    <rect x="25" y="160" width="280" height="115" fill="#0f172a" rx="8" stroke="#334155"/>
    <text x="35" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">• A: Chosen Assumed Mean benchmark</text>
    <text x="35" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• d = x - A: Coded deviation from benchmark</text>
    <text x="35" y="235" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12">• Working with smaller d values reduces calculation errors!</text>
  </g>
</svg>"""
        create_or_update_svg_block(l199, 2, 'Assumed Mean Benchmark & Deviation Shift Visual', 'assumed_mean_benchmark', svg_199_p2)

        # P3 SVG: Step-Deviation Formula Breakdown
        svg_199_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Step-Deviation Formula Anatomy</text>

  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Large Formula Box -->
    <rect x="40" y="40" width="640" height="90" fill="#0f172a" rx="10" stroke="#38bdf8"/>
    <text x="80" y="95" fill="#facc15" font-family="monospace" font-size="32" font-weight="bold">x̄  =  A  +  [ ( Σ f t / Σ f )  ×  c ]</text>

    <!-- Component Explanations -->
    <g transform="translate(40, 150)">
      <!-- Box 1: A -->
      <rect x="0" y="0" width="190" height="105" fill="#0f172a" rx="8" stroke="#facc15" stroke-width="1"/>
      <text x="95" y="28" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">A</text>
      <text x="95" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Assumed Mean</text>
      <text x="95" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Midpoint of central class</text>

      <!-- Box 2: t = (x - A)/c -->
      <rect x="220" y="0" width="200" height="105" fill="#0f172a" rx="8" stroke="#38bdf8" stroke-width="1"/>
      <text x="320" y="28" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">t = (x - A) / c</text>
      <text x="320" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Step-Coded Unit</text>
      <text x="320" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Small integers (-2, -1, 0, 1, 2)</text>

      <!-- Box 3: c -->
      <rect x="440" y="0" width="200" height="105" fill="#0f172a" rx="8" stroke="#4ade80" stroke-width="1"/>
      <text x="540" y="28" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">c</text>
      <text x="540" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Class Width</text>
      <text x="540" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Scale multiplier factor</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l199, 3, 'Step-Deviation Formula Anatomy & Coding Transformation', 'step_deviation_anatomy', svg_199_p3)

        # Fix Block 13328 (Page 8)
        block_sim199 = LessonBlock.objects.filter(lesson=l199, page_number=8).first()
        if block_sim199:
            block_sim199.block_type = 'simulation_placeholder'
            meta = block_sim199.metadata or {}
            meta['simulation_key'] = 'math_statistics_ogive_explorer'
            meta['archetype'] = 'math_statistics_ogive_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Statistics II'
            block_sim199.metadata = meta
            block_sim199.save()
            print(f'  [Page 8] Updated Block {block_sim199.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 200: Cumulative Frequency Tables and Ogives
    # =========================================================================
    if l200:
        print(f'Enriching Lesson 200: "{l200.title}"')

        # P2 SVG: Ordinary Histogram vs Ogive
        svg_200_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Ordinary Frequency vs. Cumulative Frequency (Ogive)</text>

  <!-- Left: Frequency Histogram -->
  <g transform="translate(40, 65)">
    <rect width="360" height="300" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="180" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Ordinary Frequency Histogram (Individual)</text>

    <line x1="50" y1="240" x2="330" y2="240" stroke="#334155" stroke-width="2"/>
    <line x1="50" y1="50" x2="50" y2="240" stroke="#334155" stroke-width="2"/>

    <!-- Bars -->
    <rect x="60" y="200" width="50" height="40" fill="#38bdf8" opacity="0.7"/>
    <rect x="115" y="140" width="50" height="100" fill="#38bdf8" opacity="0.7"/>
    <rect x="170" y="80" width="50" height="160" fill="#38bdf8" opacity="0.7"/>
    <rect x="225" y="160" width="50" height="80" fill="#38bdf8" opacity="0.7"/>
    <rect x="280" y="210" width="40" height="30" fill="#38bdf8" opacity="0.7"/>

    <text x="180" y="270" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Class Intervals (Marks)</text>
  </g>

  <!-- Right: Cumulative Ogive -->
  <g transform="translate(440, 65)">
    <rect width="360" height="300" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="1.5"/>
    <text x="180" y="25" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Cumulative Frequency S-Curve (Accumulated)</text>

    <line x1="50" y1="240" x2="330" y2="240" stroke="#334155" stroke-width="2"/>
    <line x1="50" y1="50" x2="50" y2="240" stroke="#334155" stroke-width="2"/>

    <!-- Smooth Ogive Path -->
    <path d="M 50 240 Q 110 230 160 170 T 270 70 L 320 60" fill="none" stroke="#4ade80" stroke-width="3.5"/>
    <circle cx="320" cy="60" r="5" fill="#4ade80"/>
    <text x="300" y="50" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Total N</text>

    <text x="180" y="270" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Upper Class Boundaries (UBC)</text>
  </g>
</svg>"""
        create_or_update_svg_block(l200, 2, 'Ordinary Frequency Histogram vs Cumulative Ogive Curve', 'histogram_vs_ogive', svg_200_p2)

        # P3 SVG: Anatomy of an Ogive Curve
        svg_200_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Anatomy of an Ogive Curve: Plotting &amp; Quantile Drops</text>

  <g transform="translate(60, 60)">
    <rect width="720" height="330" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Axes -->
    <line x1="80" y1="270" x2="680" y2="270" stroke="#334155" stroke-width="2.5"/>
    <line x1="80" y1="40" x2="80" y2="270" stroke="#334155" stroke-width="2.5"/>
    <text x="380" y="300" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Upper Class Boundaries (X-axis)</text>
    <text x="35" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" transform="rotate(-90 35 150)">Cumulative Frequency cf (Y-axis)</text>

    <!-- Ogive Curve -->
    <path d="M 80 270 Q 200 260 300 200 T 500 80 L 640 60" fill="none" stroke="#10b981" stroke-width="4"/>

    <!-- Q1 (N/4) Drop Line -->
    <line x1="80" y1="217" x2="270" y2="217" stroke="#10b981" stroke-dasharray="4 3" stroke-width="2"/>
    <line x1="270" y1="217" x2="270" y2="270" stroke="#10b981" stroke-dasharray="4 3" stroke-width="2"/>
    <circle cx="270" cy="217" r="5" fill="#10b981"/>
    <text x="50" y="222" fill="#10b981" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">N/4</text>
    <text x="270" y="288" fill="#10b981" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Q₁ (25%)</text>

    <!-- Q2 (N/2) Drop Line -->
    <line x1="80" y1="165" x2="365" y2="165" stroke="#facc15" stroke-dasharray="4 3" stroke-width="2"/>
    <line x1="365" y1="165" x2="365" y2="270" stroke="#facc15" stroke-dasharray="4 3" stroke-width="2"/>
    <circle cx="365" cy="165" r="5" fill="#facc15"/>
    <text x="50" y="170" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">N/2</text>
    <text x="365" y="288" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Q₂ (Median)</text>

    <!-- Q3 (3N/4) Drop Line -->
    <line x1="80" y1="112" x2="465" y2="112" stroke="#38bdf8" stroke-dasharray="4 3" stroke-width="2"/>
    <line x1="465" y1="112" x2="465" y2="270" stroke="#38bdf8" stroke-dasharray="4 3" stroke-width="2"/>
    <circle cx="465" cy="112" r="5" fill="#38bdf8"/>
    <text x="45" y="117" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">3N/4</text>
    <text x="465" y="288" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Q₃ (75%)</text>

    <!-- IQR Band -->
    <rect x="270" y="268" width="195" height="4" fill="#facc15"/>
  </g>
</svg>"""
        create_or_update_svg_block(l200, 3, 'Anatomy of an Ogive Curve & Quantile Drop Lines', 'ogive_anatomy_quantiles', svg_200_p3)

        # Fix Block 13339 (Page 8)
        block_sim200 = LessonBlock.objects.filter(lesson=l200, page_number=8).first()
        if block_sim200:
            block_sim200.block_type = 'simulation_placeholder'
            meta = block_sim200.metadata or {}
            meta['simulation_key'] = 'math_statistics_ogive_explorer'
            meta['archetype'] = 'math_statistics_ogive_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Statistics II'
            block_sim200.metadata = meta
            block_sim200.save()
            print(f'  [Page 8] Updated Block {block_sim200.id} block_type to simulation_placeholder')

    # =========================================================================
    # LESSON 201: Median, Quartiles, and Percentiles by Calculation
    # =========================================================================
    if l201:
        print(f'Enriching Lesson 201: "{l201.title}"')

        # P2 SVG: Linear Interpolation Similar Triangles
        svg_201_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Linear Interpolation: Similar Triangles Geometry</text>

  <g transform="translate(40, 65)">
    <rect width="760" height="300" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Left: Zoomed Ogive Segment Triangle -->
    <g transform="translate(40, 30)">
      <rect width="360" height="240" fill="#0f172a" rx="8" stroke="#334155"/>

      <!-- Large Triangle (Class Width c, Frequency f) -->
      <line x1="50" y1="200" x2="310" y2="40" stroke="#4ade80" stroke-width="3"/> <!-- Chord -->
      <line x1="50" y1="200" x2="310" y2="200" stroke="#64748b" stroke-width="2" stroke-dasharray="4 2"/> <!-- Base c -->
      <line x1="310" y1="40" x2="310" y2="200" stroke="#64748b" stroke-width="2" stroke-dasharray="4 2"/> <!-- Height f -->

      <!-- Small Triangle (Distance x - L, Target cf - cf_b) -->
      <line x1="50" y1="200" x2="180" y2="200" stroke="#facc15" stroke-width="2.5"/> <!-- Base x - L -->
      <line x1="180" y1="115" x2="180" y2="200" stroke="#facc15" stroke-width="2.5"/> <!-- Height -->
      <circle cx="180" cy="115" r="5" fill="#facc15"/>

      <!-- Labels -->
      <text x="180" y="220" fill="#facc15" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">x - L</text>
      <text x="180" y="240" fill="#64748b" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Class Width (c = U - L)</text>
      <text x="325" y="125" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Freq (f)</text>
    </g>

    <!-- Right: Proportion Equation -->
    <g transform="translate(440, 30)">
      <rect width="280" height="240" fill="#0f172a" rx="8" stroke="#38bdf8"/>
      <text x="140" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Similar Triangles Ratio</text>

      <rect x="20" y="55" width="240" height="70" fill="#1e293b" rx="6"/>
      <text x="120" y="85" fill="#facc15" font-family="monospace" font-size="15" font-weight="bold" text-anchor="middle">(x - L) / c  =  (target_cf - cf_b) / f</text>

      <rect x="20" y="140" width="240" height="75" fill="#1e293b" rx="6"/>
      <text x="120" y="165" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Solving for Score x:</text>
      <text x="120" y="195" fill="#4ade80" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">x = L + [ (target_cf - cf_b) / f ] × c</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l201, 2, 'Linear Interpolation Similar Triangles Geometric Principle', 'linear_interpolation_geometry', svg_201_p2)

        # P3 SVG: Formula Breakdown for Quantile Interpolation
        svg_201_p3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Quantile Interpolation Formula Breakdown</text>

  <g transform="translate(60, 65)">
    <rect width="720" height="280" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <rect x="40" y="40" width="640" height="80" fill="#0f172a" rx="10" stroke="#38bdf8"/>
    <text x="80" y="90" fill="#facc15" font-family="monospace" font-size="28" font-weight="bold">Q_k  =  L  +  [ ( (k·N/4) - cf_b ) / f ]  ×  c</text>

    <g transform="translate(40, 140)">
      <rect x="0" y="0" width="150" height="110" fill="#0f172a" rx="8" stroke="#facc15"/>
      <text x="75" y="30" fill="#facc15" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">L</text>
      <text x="75" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Lower Boundary</text>
      <text x="75" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Start of quartile class</text>

      <rect x="165" y="0" width="170" height="110" fill="#0f172a" rx="8" stroke="#38bdf8"/>
      <text x="250" y="30" fill="#38bdf8" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">cf_b</text>
      <text x="250" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Prior Cum. Freq</text>
      <text x="250" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Sum before class</text>

      <rect x="350" y="0" width="150" height="110" fill="#0f172a" rx="8" stroke="#4ade80"/>
      <text x="425" y="30" fill="#4ade80" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">f</text>
      <text x="425" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Class Freq</text>
      <text x="425" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Frequency of class</text>

      <rect x="515" y="0" width="125" height="110" fill="#0f172a" rx="8" stroke="#f87171"/>
      <text x="577" y="30" fill="#f87171" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">c</text>
      <text x="577" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Class Width</text>
      <text x="577" y="75" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Interval width</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l201, 3, 'Quantile Linear Interpolation Formula Decomposition', 'quantile_formula_decomposition', svg_201_p3)

    # =========================================================================
    # LESSON 202: Measures of Dispersion, Standard Deviation, and Moving Averages
    # =========================================================================
    if l202:
        print(f'Enriching Lesson 202: "{l202.title}"')

        # P2 SVG: Standard Deviation Spread Comparison
        svg_202_p2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Standard Deviation (σ): Measuring Spread Around the Mean</text>

  <!-- Left: Low Standard Deviation (Consistent) -->
  <g transform="translate(40, 65)">
    <rect width="360" height="300" fill="#1e293b" rx="12" stroke="#4ade80" stroke-width="1.5"/>
    <text x="180" y="30" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Low Standard Deviation (σ = 5)</text>

    <!-- Bell Curve (Narrow) -->
    <path d="M 40 240 Q 140 240 180 60 Q 220 240 320 240" fill="rgba(74, 222, 128, 0.2)" stroke="#4ade80" stroke-width="3"/>
    <line x1="180" y1="60" x2="180" y2="240" stroke="#facc15" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="180" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Mean μ = 50</text>

    <text x="180" y="282" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">High Consistency — Data clustered tightly</text>
  </g>

  <!-- Right: High Standard Deviation (Dispersed) -->
  <g transform="translate(440, 65)">
    <rect width="360" height="300" fill="#1e293b" rx="12" stroke="#f87171" stroke-width="1.5"/>
    <text x="180" y="30" fill="#f87171" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">High Standard Deviation (σ = 20)</text>

    <!-- Bell Curve (Wide) -->
    <path d="M 40 240 Q 110 200 180 120 Q 250 200 320 240" fill="rgba(248, 113, 113, 0.2)" stroke="#f87171" stroke-width="3"/>
    <line x1="180" y1="120" x2="180" y2="240" stroke="#facc15" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="180" y="258" fill="#facc15" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Mean μ = 50</text>

    <text x="180" y="282" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">High Variability — Data widely spread out</text>
  </g>
</svg>"""
        create_or_update_svg_block(l202, 2, 'High vs Low Standard Deviation Spread Visual', 'standard_deviation_spread', svg_202_p2)

        # P7 SVG: Moving Average Smoothing Trendline
        svg_202_p7 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0a0f1d" rx="16"/>
  <text x="420" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Time-Series Analysis: 3-Period Moving Average Smoothing</text>

  <g transform="translate(60, 65)">
    <rect width="720" height="300" fill="#0f172a" rx="12" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Grid -->
    <line x1="60" y1="240" x2="680" y2="240" stroke="#334155" stroke-width="2"/>
    <line x1="60" y1="40" x2="60" y2="240" stroke="#334155" stroke-width="2"/>

    <!-- Raw Sales Data Line (Volatile Blue Line) -->
    <polyline points="80,210 140,120 200,190 260,100 320,170 380,80 440,150 500,70 560,130 620,50" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.6"/>

    <!-- Moving Average Smoothed Line (Emerald Green) -->
    <polyline points="140,173 200,136 260,153 320,116 380,133 440,100 500,116 560,83" fill="none" stroke="#4ade80" stroke-width="4"/>

    <!-- Data Nodes -->
    <circle cx="140" cy="173" r="5" fill="#4ade80"/>
    <circle cx="200" cy="136" r="5" fill="#4ade80"/>
    <circle cx="260" cy="153" r="5" fill="#4ade80"/>
    <circle cx="320" cy="116" r="5" fill="#4ade80"/>
    <circle cx="380" cy="133" r="5" fill="#4ade80"/>
    <circle cx="440" cy="100" r="5" fill="#4ade80"/>

    <!-- Legend -->
    <g transform="translate(480, 260)">
      <line x1="0" y1="0" x2="30" y2="0" stroke="#38bdf8" stroke-width="2.5" opacity="0.6"/>
      <text x="35" y="4" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Raw Monthly Sales</text>

      <line x1="160" y1="0" x2="190" y2="0" stroke="#4ade80" stroke-width="4"/>
      <text x="195" y="4" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">3-Period Moving Trend</text>
    </g>
  </g>
</svg>"""
        create_or_update_svg_block(l202, 7, 'Moving Average Smoothing & Long-Term Trendline', 'moving_average_trendline', svg_202_p7)

        # Fix Block 13361 (Page 8)
        block_sim202 = LessonBlock.objects.filter(lesson=l202, page_number=8).first()
        if block_sim202:
            block_sim202.block_type = 'simulation_placeholder'
            meta = block_sim202.metadata or {}
            meta['simulation_key'] = 'math_statistics_ogive_explorer'
            meta['archetype'] = 'math_statistics_ogive_explorer'
            meta['subject'] = 'MATHEMATICS'
            meta['concept_group'] = 'Statistics II'
            block_sim202.metadata = meta
            block_sim202.save()
            print(f'  [Page 8] Updated Block {block_sim202.id} block_type to simulation_placeholder')

    print('\n=== ENRICHMENT OF TOPIC 2 COMPLETED SUCCESSFULLY ===')

if __name__ == '__main__':
    enrich_topic2_statistics()
