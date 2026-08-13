import os
import sys
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

import requests
from django.core.files.base import ContentFile
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

def clean_svg(svg_code):
    is_valid, sanitized, err = validate_and_sanitize_svg(svg_code)
    return sanitized if is_valid else svg_code

def inject_svg_content_all_assets():
    print('=== INJECTING SVG_CONTENT INTO ASSETS AND BLOCKS ===')
    assets = LessonAsset.objects.filter(asset_type='diagram')
    updated_count = 0
    
    for a in assets:
        svg_text = None
        if a.metadata and a.metadata.get('svg_content'):
            svg_text = a.metadata.get('svg_content')
        elif a.file:
            try:
                raw_bytes = a.file.read()
                svg_text = raw_bytes.decode('utf-8')
            except Exception:
                try:
                    r = requests.get(a.file.url, timeout=5)
                    if r.status_code == 200 and '<svg' in r.text:
                        svg_text = r.text
                except Exception as e:
                    print(f'Error fetching SVG for Asset {a.id}: {e}')
        
        if svg_text and '<svg' in svg_text:
            cleaned_svg = clean_svg(svg_text)
            if not a.metadata:
                a.metadata = {}
            a.metadata['svg_content'] = cleaned_svg
            a.save(update_fields=['metadata'])
            
            for b in a.blocks.all():
                if not b.metadata:
                    b.metadata = {}
                b.metadata['svg_content'] = cleaned_svg
                if isinstance(b.content, dict):
                    b.content['svg_content'] = cleaned_svg
                    b.content['svg'] = cleaned_svg
                b.save(update_fields=['metadata', 'content'])
            updated_count += 1
            print(f'Injected SVG into Asset {a.id} (Lesson {a.lesson_id}): \"{a.title}\"')

    print(f'Successfully injected SVG content into {updated_count} assets and their blocks.\n')

def repair_orphaned_blocks():
    print('=== REPAIRING ORPHANED MEDIA BLOCKS ===')
    
    # 1. Lesson 65: Factor 2 Temperature Effect (B1702)
    try:
        b1702 = LessonBlock.objects.get(id=1702)
        svg_temp = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0a0f1d" rx="16"/>
  <text x="420" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Effect of Temperature on Particle Kinetics &amp; Collision Frequency</text>
  
  <rect x="40" y="65" width="360" height="345" fill="#1e293b" rx="12" stroke="#475569" stroke-width="2"/>
  <text x="220" y="95" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Low Temperature (20°C)</text>
  <circle cx="120" cy="160" r="18" fill="#38bdf8" opacity="0.8"/>
  <path d="M 138 160 L 170 160" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="280" cy="200" r="18" fill="#38bdf8" opacity="0.8"/>
  <path d="M 262 200 L 230 200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="180" cy="280" r="18" fill="#38bdf8" opacity="0.8"/>
  <rect x="60" y="330" width="320" height="60" fill="#0f172a" rx="8"/>
  <text x="220" y="355" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Slower particle movement</text>
  <text x="220" y="375" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Few collisions exceed Activation Energy (Ea)</text>

  <rect x="440" y="65" width="360" height="345" fill="#1e293b" rx="12" stroke="#ef4444" stroke-width="2"/>
  <text x="620" y="95" fill="#f87171" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">High Temperature (60°C)</text>
  <circle cx="520" cy="160" r="18" fill="#ef4444" opacity="0.9"/>
  <path d="M 538 160 L 600 160 M 590 155 L 600 160 L 590 165" stroke="#ef4444" stroke-width="3"/>
  <circle cx="700" cy="180" r="18" fill="#ef4444" opacity="0.9"/>
  <path d="M 682 180 L 620 180 M 630 175 L 620 180 L 630 185" stroke="#ef4444" stroke-width="3"/>
  <polygon points="610,170 615,160 625,165 620,175" fill="#fbbf24"/>
  <circle cx="580" cy="270" r="18" fill="#ef4444" opacity="0.9"/>
  <rect x="460" y="330" width="320" height="60" fill="#0f172a" rx="8"/>
  <text x="620" y="355" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Rapid kinetic motion + higher collision frequency</text>
  <text x="620" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Large fraction of collisions have Energy &gt;= Ea</text>
</svg>"""
        sanitized = clean_svg(svg_temp)
        asset_temp = LessonAsset.objects.create(
            lesson_id=65, asset_type='diagram', source_type='ai_generated', storage_type='file', status='approved',
            title='Temperature Effect on Kinetic Energy and Effective Collision Frequency',
            description='Comparative diagram of reactant particles at low vs high temperatures.',
            metadata={'svg_content': sanitized}
        )
        asset_temp.file.save('temp_effect_65.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        b1702.assets.add(asset_temp)
        b1702.title = 'Temperature Effect on Kinetic Energy and Effective Collision Frequency'
        b1702.metadata = {'svg_content': sanitized}
        b1702.content = {'svg_content': sanitized, 'svg': sanitized}
        b1702.save()
        print('Attached asset to B1702 (Lesson 65)')
    except LessonBlock.DoesNotExist:
        pass

    # 2. Lesson 65: Factor 3 Surface Area (B1705)
    try:
        b1705 = LessonBlock.objects.get(id=1705)
        svg_sa = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0a0f1d" rx="16"/>
  <text x="420" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Effect of Surface Area on Reaction Kinetics</text>
  
  <rect x="40" y="65" width="360" height="345" fill="#1e293b" rx="12" stroke="#475569" stroke-width="2"/>
  <text x="220" y="95" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Solid Marble Lump (Small Surface Area)</text>
  <rect x="140" y="140" width="160" height="130" fill="#64748b" stroke="#cbd5e1" stroke-width="2" rx="4"/>
  <text x="220" y="210" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Trapped Inner Atoms</text>
  <circle cx="100" cy="180" r="10" fill="#38bdf8"/>
  <circle cx="340" cy="220" r="10" fill="#38bdf8"/>
  <rect x="60" y="330" width="320" height="60" fill="#0f172a" rx="8"/>
  <text x="220" y="355" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Only outermost surface atoms can collide</text>
  <text x="220" y="375" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Lower collision rate = Slow Reaction</text>

  <rect x="440" y="65" width="360" height="345" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="620" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Finely Powdered Marble (Large Surface Area)</text>
  <g fill="#94a3b8" stroke="#e2e8f0" stroke-width="1">
    <rect x="480" y="130" width="40" height="35" rx="2"/><rect x="540" y="130" width="40" height="35" rx="2"/><rect x="600" y="130" width="40" height="35" rx="2"/><rect x="660" y="130" width="40" height="35" rx="2"/><rect x="720" y="130" width="40" height="35" rx="2"/>
    <rect x="480" y="180" width="40" height="35" rx="2"/><rect x="540" y="180" width="40" height="35" rx="2"/><rect x="600" y="180" width="40" height="35" rx="2"/><rect x="660" y="180" width="40" height="35" rx="2"/><rect x="720" y="180" width="40" height="35" rx="2"/>
    <rect x="480" y="230" width="40" height="35" rx="2"/><rect x="540" y="230" width="40" height="35" rx="2"/><rect x="600" y="230" width="40" height="35" rx="2"/><rect x="660" y="230" width="40" height="35" rx="2"/><rect x="720" y="230" width="40" height="35" rx="2"/>
  </g>
  <circle cx="500" cy="115" r="8" fill="#38bdf8"/><circle cx="620" cy="115" r="8" fill="#38bdf8"/><circle cx="740" cy="115" r="8" fill="#38bdf8"/>
  <rect x="460" y="330" width="320" height="60" fill="#0f172a" rx="8"/>
  <text x="620" y="355" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Millions of exposed reaction sites simultaneously</text>
  <text x="620" y="375" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">• Higher collision frequency = Rapid Reaction</text>
</svg>"""
        sanitized = clean_svg(svg_sa)
        asset_sa = LessonAsset.objects.create(
            lesson_id=65, asset_type='diagram', source_type='ai_generated', storage_type='file', status='approved',
            title='Sub-Microscopic Surface Area Comparison: Lump vs Powder Kinetics',
            description='Particle diagram showing exposed reaction sites in solid lump vs powder.',
            metadata={'svg_content': sanitized}
        )
        asset_sa.file.save('surface_area_65.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        b1705.assets.add(asset_sa)
        b1705.title = 'Sub-Microscopic Surface Area Comparison: Lump vs Powder Kinetics'
        b1705.metadata = {'svg_content': sanitized}
        b1705.content = {'svg_content': sanitized, 'svg': sanitized}
        b1705.save()
        print('Attached asset to B1705 (Lesson 65)')
    except LessonBlock.DoesNotExist:
        pass

    # 3. Lesson 66: Remove erroneous quiz placeholder block B1729
    try:
        b1729 = LessonBlock.objects.get(id=1729)
        b1729.delete()
        print('Deleted erroneous quiz placeholder block B1729 (Lesson 66)')
    except LessonBlock.DoesNotExist:
        pass

    # 4. Lesson 69: Factor 4 Catalyst Effects (B1766)
    try:
        b1766 = LessonBlock.objects.get(id=1766)
        svg_cat = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0a0f1d" rx="16"/>
  <text x="420" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Catalytic Energy Pathway in Dynamic Reversible Equilibrium</text>
  
  <line x1="80" y1="360" x2="760" y2="360" stroke="#64748b" stroke-width="2"/>
  <line x1="80" y1="360" x2="80" y2="80" stroke="#64748b" stroke-width="2"/>
  <text x="420" y="395" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">Reaction Progress (Forward &lt;--&gt; Reverse)</text>
  <text x="45" y="210" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="14" transform="rotate(-90 45,210)" text-anchor="middle">Potential Energy</text>

  <line x1="80" y1="260" x2="220" y2="260" stroke="#38bdf8" stroke-width="4"/>
  <text x="150" y="245" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Reactants</text>
  
  <line x1="620" y1="300" x2="760" y2="300" stroke="#4ade80" stroke-width="4"/>
  <text x="690" y="285" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">Products</text>

  <path d="M 220 260 Q 420 70 620 300" fill="none" stroke="#f87171" stroke-width="3"/>
  <text x="420" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Uncatalysed Pathway (High Ea)</text>

  <path d="M 220 260 Q 420 160 620 300" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6"/>
  <text x="420" y="185" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Catalysed Pathway (Lower Ea)</text>

  <rect x="180" y="320" width="480" height="30" fill="#1e293b" rx="6"/>
  <text x="420" y="340" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Catalyst lowers Ea for BOTH Forward and Reverse reactions equally (Yield unchanged)</text>
</svg>"""
        sanitized = clean_svg(svg_cat)
        asset_cat = LessonAsset.objects.create(
            lesson_id=69, asset_type='diagram', source_type='ai_generated', storage_type='file', status='approved',
            title='Catalyst Energy Profile: Equal Activation Energy Reduction for Forward & Reverse Rates',
            description='Energy profile comparing uncatalysed vs catalysed pathways in equilibrium.',
            metadata={'svg_content': sanitized}
        )
        asset_cat.file.save('catalyst_effect_69.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        b1766.assets.add(asset_cat)
        b1766.title = 'Catalyst Energy Profile: Equal Activation Energy Reduction for Forward & Reverse Rates'
        b1766.metadata = {'svg_content': sanitized}
        b1766.content = {'svg_content': sanitized, 'svg': sanitized}
        b1766.save()
        print('Attached asset to B1766 (Lesson 69)')
    except LessonBlock.DoesNotExist:
        pass

    # 5. Lesson 77: B3314
    try:
        b3314 = LessonBlock.objects.get(id=3314)
        svg_fe_cu = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0a0f1d" rx="16"/>
  <text x="420" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Sub-Microscopic Electron Transfer: Iron Metal in Copper(II) Sulfate</text>
  
  <rect x="60" y="70" width="320" height="335" fill="#1e293b" rx="12" stroke="#475569" stroke-width="2"/>
  <text x="220" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Iron Nail Surface (Oxidation)</text>
  <rect x="100" y="140" width="100" height="180" fill="#64748b" rx="6"/>
  <text x="150" y="235" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Fe(s)</text>
  <path d="M 210 200 L 290 170 M 280 165 L 290 170 L 285 180" stroke="#f87171" stroke-width="3"/>
  <text x="250" y="160" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Loss of 2e-</text>
  <circle cx="320" cy="180" r="22" fill="#22c55e" opacity="0.8"/>
  <text x="320" y="185" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Fe2+(aq)</text>
  <rect x="80" y="340" width="280" height="45" fill="#0f172a" rx="6"/>
  <text x="220" y="368" fill="#22c55e" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Fe(s) --&gt; Fe2+(aq) + 2e- (Oxidation)</text>

  <rect x="460" y="70" width="320" height="335" fill="#1e293b" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="620" y="105" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Copper Ions Deposit (Reduction)</text>
  <circle cx="520" cy="180" r="22" fill="#0284c7" opacity="0.9"/>
  <text x="520" y="185" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Cu2+(aq)</text>
  <path d="M 550 180 L 630 200 M 620 195 L 630 200 L 625 210" stroke="#38bdf8" stroke-width="3"/>
  <text x="590" y="170" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Gain 2e-</text>
  <rect x="640" y="140" width="100" height="180" fill="#b45309" rx="6"/>
  <text x="690" y="235" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Cu(s)</text>
  <rect x="480" y="340" width="280" height="45" fill="#0f172a" rx="6"/>
  <text x="620" y="368" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Cu2+(aq) + 2e- --&gt; Cu(s) (Reduction)</text>
</svg>"""
        sanitized = clean_svg(svg_fe_cu)
        asset_fe_cu = LessonAsset.objects.create(
            lesson_id=77, asset_type='diagram', source_type='ai_generated', storage_type='file', status='approved',
            title='Sub-Microscopic Electron Transfer: Iron Nail Displacement in Copper Sulfate',
            description='Particulate diagram showing oxidation of Fe atoms and reduction of Cu2+ ions.',
            metadata={'svg_content': sanitized}
        )
        asset_fe_cu.file.save('fe_cu_redox_77.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        b3314.assets.add(asset_fe_cu)
        b3314.title = 'Sub-Microscopic Electron Transfer: Iron Nail Displacement in Copper Sulfate'
        b3314.metadata = {'svg_content': sanitized}
        b3314.content = {'svg_content': sanitized, 'svg': sanitized}
        b3314.save()
        print('Attached asset to B3314 (Lesson 77)')
    except LessonBlock.DoesNotExist:
        pass

    # 6. Lesson 78: B3322
    try:
        b3322 = LessonBlock.objects.get(id=3322)
        svg_scale = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0a0f1d" rx="16"/>
  <text x="420" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Oxidation State Number Line &amp; Electron Flow Direction</text>
  
  <rect x="360" y="70" width="120" height="335" fill="#1e293b" rx="10" stroke="#475569" stroke-width="2"/>
  <text x="420" y="105" fill="#ef4444" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">+7 (KMnO4)</text>
  <text x="420" y="145" fill="#f97316" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">+4 (MnO2)</text>
  <text x="420" y="185" fill="#eab308" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">+2 (Fe2+, Cu2+)</text>
  <text x="420" y="225" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">0 (Fe, Zn, H2)</text>
  <text x="420" y="265" fill="#818cf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">-1 (Cl-, Br-)</text>
  <text x="420" y="305" fill="#a855f7" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">-2 (O2-, S2-)</text>
  <text x="420" y="345" fill="#ec4899" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">-3 (NH3, N3-)</text>

  <g transform="translate(100, 120)">
    <path d="M 120 180 L 120 20 M 110 35 L 120 20 L 130 35" stroke="#ef4444" stroke-width="6"/>
    <text x="100" y="100" fill="#ef4444" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="end">OXIDATION</text>
    <text x="100" y="125" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="13" text-anchor="end">• Increase in Oxidation Number</text>
    <text x="100" y="145" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="13" text-anchor="end">• Loss of electrons (OIL)</text>
  </g>

  <g transform="translate(540, 120)">
    <path d="M 80 20 L 80 180 M 70 165 L 80 180 L 90 165" stroke="#38bdf8" stroke-width="6"/>
    <text x="105" y="100" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="start">REDUCTION</text>
    <text x="105" y="125" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="13" text-anchor="start">• Decrease in Oxidation Number</text>
    <text x="105" y="145" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="13" text-anchor="start">• Gain of electrons (RIG)</text>
  </g>
</svg>"""
        sanitized = clean_svg(svg_scale)
        asset_scale = LessonAsset.objects.create(
            lesson_id=78, asset_type='diagram', source_type='ai_generated', storage_type='file', status='approved',
            title='Oxidation State Vertical Scale: Visualizing Electron Loss (Up) vs Electron Gain (Down)',
            description='Vertical number line illustrating oxidation state changes.',
            metadata={'svg_content': sanitized}
        )
        asset_scale.file.save('oxidation_scale_78.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        b3322.assets.add(asset_scale)
        b3322.title = 'Oxidation State Vertical Scale: Visualizing Electron Loss (Up) vs Electron Gain (Down)'
        b3322.metadata = {'svg_content': sanitized}
        b3322.content = {'svg_content': sanitized, 'svg': sanitized}
        b3322.save()
        print('Attached asset to B3322 (Lesson 78)')
    except LessonBlock.DoesNotExist:
        pass

    # 7. Lesson 79: B3330
    try:
        b3330 = LessonBlock.objects.get(id=3330)
        svg_tree = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0a0f1d" rx="16"/>
  <text x="420" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">Systematic 4-Step Decision Flowchart for Assigning Oxidation Numbers</text>
  
  <rect x="300" y="65" width="240" height="45" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
  <text x="420" y="93" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Free Uncombined Element?</text>
  
  <path d="M 420 110 L 420 145 M 415 135 L 420 145 L 425 135" stroke="#94a3b8" stroke-width="2"/>
  <rect x="580" y="65" width="160" height="45" fill="#0f172a" rx="8" stroke="#22c55e" stroke-width="2"/>
  <text x="660" y="93" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">YES --&gt; Ox No = 0</text>
  <line x1="540" y1="87" x2="580" y2="87" stroke="#22c55e" stroke-width="2"/>

  <rect x="300" y="145" width="240" height="45" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
  <text x="420" y="173" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Simple Monoatomic Ion?</text>

  <path d="M 420 190 L 420 225 M 415 215 L 420 225 L 425 215" stroke="#94a3b8" stroke-width="2"/>
  <rect x="580" y="145" width="180" height="45" fill="#0f172a" rx="8" stroke="#22c55e" stroke-width="2"/>
  <text x="670" y="173" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">YES --&gt; Equal to Ion Charge</text>
  <line x1="540" y1="167" x2="580" y2="167" stroke="#22c55e" stroke-width="2"/>

  <rect x="300" y="225" width="240" height="45" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
  <text x="420" y="253" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. Contains H, O, or Fluorine?</text>

  <path d="M 420 270 L 420 305 M 415 295 L 420 305 L 425 295" stroke="#94a3b8" stroke-width="2"/>
  <rect x="580" y="225" width="220" height="55" fill="#0f172a" rx="8" stroke="#fbbf24" stroke-width="2"/>
  <text x="690" y="248" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">F = -1, H = +1 (hydrides -1)</text>
  <text x="690" y="268" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">O = -2 (peroxides -1)</text>
  <line x1="540" y1="247" x2="580" y2="247" stroke="#fbbf24" stroke-width="2"/>

  <rect x="250" y="315" width="340" height="55" fill="#1e293b" rx="8" stroke="#a855f7" stroke-width="2"/>
  <text x="420" y="338" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">4. Sum of Ox Numbers = Overall Net Charge</text>
  <text x="420" y="358" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Neutral Molecule = 0 | Polyatomic Ion = Ion Charge</text>
</svg>"""
        sanitized = clean_svg(svg_tree)
        asset_tree = LessonAsset.objects.create(
            lesson_id=79, asset_type='diagram', source_type='ai_generated', storage_type='file', status='approved',
            title='Systematic Decision Flowchart for Assigning Oxidation Numbers',
            description='Flowchart illustrating systematic 4-step rules for oxidation numbers.',
            metadata={'svg_content': sanitized}
        )
        asset_tree.file.save('decision_flowchart_79.svg', ContentFile(sanitized.encode('utf-8')), save=True)
        b3330.assets.add(asset_tree)
        b3330.title = 'Systematic Decision Flowchart for Assigning Oxidation Numbers'
        b3330.metadata = {'svg_content': sanitized}
        b3330.content = {'svg_content': sanitized, 'svg': sanitized}
        b3330.save()
        print('Attached asset to B3330 (Lesson 79)')
    except LessonBlock.DoesNotExist:
        pass

if __name__ == '__main__':
    inject_svg_content_all_assets()
    repair_orphaned_blocks()
