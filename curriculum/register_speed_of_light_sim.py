"""
Register Speed of Light Historical Laboratory simulation in Django DB
and link to Lesson 245 (Experimental Speed of Light and Spectral Band Analysis).
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Simulation, SubjectDomain, SimulationStatus, Lesson, LessonBlock, LessonAsset
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

CONFIG = {
    "c_vacuum": 299792458,
    "fizeau_default_distance_km": 8.633,
    "fizeau_default_teeth": 720,
    "fizeau_default_rpm": 0,
    "romer_default_month": 0,
    "telemetry_events": [
        "RPM_CHANGED",
        "PRESET_APPLIED",
        "ROMER_MONTH_SCRUBBED",
        "PRACTICE_SUBMITTED",
        "TAB_CHANGED",
        "RESET_EXPERIMENT",
    ],
    "context_spec": {
        "overview": "Recreate the two landmark historical experiments that determined the finite speed of light c: Hippolyte Fizeau's terrestrial rotating toothed wheel (1849) and Ole Rømer's astronomical observations of Jupiter's moon Io eclipses (1676).",
        "how_to_use": [
            "Step 1: In the Fizeau tab, adjust the wheel RPM to ~724 RPM to observe the first extinction (eclipse) in the eyepiece.",
            "Step 2: Compare the observed eclipse RPM with Fizeau's 1849 measurement (756 RPM) and derive c = 4 D N f.",
            "Step 3: In the Rømer tab, drag the Earth orbital month slider from Jan (opposition) to Jul (conjunction) to observe the +16.6 minute eclipse delay across Earth's orbital diameter.",
            "Step 4: Solve the KCSE practice challenges calculating c from experimental and astronomical parameters."
        ],
        "expected_results": [
            {
                "action": "Increasing wheel RPM to ~724 RPM in Fizeau setup",
                "expected_outcome": "Light beam in telescope eyepiece extinguishes completely (eclipse).",
                "key_takeaway": "Light takes ~57.6 microseconds to travel 17.26 km roundtrip. During this time, the wheel rotates through pi/N radians, placing a tooth directly in the return beam path (c = 4 D N f)."
            },
            {
                "action": "Advancing Earth orbit from opposition to conjunction in Rømer setup",
                "expected_outcome": "Observed Io eclipses accumulate a +16.6 minute delay compared to uniform clock time.",
                "key_takeaway": "Light requires ~1000 seconds (~16.6 minutes) to traverse Earth's orbital diameter (2 AU = 3.0 x 10^8 km), establishing that light travels at finite speed c = 3.0 x 10^8 m/s."
            }
        ]
    }
}

SVG_DIAGRAM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0a0f1d" rx="16"/>
  <text x="420" y="32" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">Speed of Light Historical Laboratory: Fizeau's Toothed Wheel &amp; Rømer's Io Observations</text>
  
  <!-- Left Half: Fizeau's Toothed Wheel (x=30 to 400) -->
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="375" height="340" fill="#111827" rx="10" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="187" y="24" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">FIZEAU'S TOOTHED WHEEL (1849)</text>
    
    <!-- Light Source & Splitter -->
    <rect x="20" y="55" width="40" height="30" fill="#1e293b" stroke="#38bdf8" rx="4"/>
    <circle cx="40" cy="70" r="6" fill="#facc15"/>
    <text x="40" y="100" fill="#94a3b8" font-size="9" text-anchor="middle">Arc Lamp</text>
    
    <!-- Beam Splitter -->
    <line x1="85" y1="58" x2="105" y2="82" stroke="#a855f7" stroke-width="3"/>
    <text x="95" y="50" fill="#a855f7" font-size="9" text-anchor="middle">Splitter</text>
    
    <!-- Toothed Wheel -->
    <circle cx="150" cy="115" r="35" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
    <circle cx="150" cy="115" r="4" fill="#f59e0b"/>
    <!-- Gear notches -->
    <line x1="150" y1="70" x2="150" y2="80" stroke="#f8fafc" stroke-width="4"/>
    <line x1="150" y1="150" x2="150" y2="160" stroke="#f8fafc" stroke-width="4"/>
    <line x1="110" y1="115" x2="120" y2="115" stroke="#f8fafc" stroke-width="4"/>
    <line x1="180" y1="115" x2="190" y2="115" stroke="#f8fafc" stroke-width="4"/>
    <text x="150" y="175" fill="#f59e0b" font-size="9" font-weight="700" text-anchor="middle">N = 720 teeth (ω)</text>
    
    <!-- Distance Path to Mirror -->
    <line x1="150" y1="70" x2="330" y2="70" stroke="#facc15" stroke-width="2" stroke-dasharray="6 3"/>
    <line x1="330" y1="72" x2="150" y2="72" stroke="#38bdf8" stroke-width="2"/>
    <rect x="330" y="55" width="10" height="35" fill="#64748b" stroke="#38bdf8"/>
    <text x="335" y="105" fill="#94a3b8" font-size="9" text-anchor="middle">Mirror (8.63 km)</text>
    
    <!-- Eyepiece & Eclipse -->
    <rect x="75" y="125" width="40" height="25" fill="#1e293b" stroke="#475569" rx="3"/>
    <circle cx="95" cy="137" r="7" fill="#000" stroke="#ef4444" stroke-width="1.5"/>
    <text x="95" y="165" fill="#ef4444" font-size="9" font-weight="700" text-anchor="middle">Eclipse at f₁ = 12.6 rps</text>
    
    <!-- Formula Box -->
    <rect x="15" y="220" width="345" height="105" fill="#0f172a" rx="6" stroke="#334155"/>
    <text x="25" y="240" fill="#94a3b8" font-size="10">Roundtrip distance: 2D = 2 × 8.63 km = 17.26 km</text>
    <text x="25" y="260" fill="#94a3b8" font-size="10">Slot transit time: Δt = π / (N · ω) = 1 / (2·N·f)</text>
    <text x="25" y="285" fill="#22c55e" font-size="13" font-weight="700">Formula: c = 4 · D · N · f₁</text>
    <text x="25" y="308" fill="#facc15" font-size="11" font-weight="700">c ≈ 4 × 8630 × 720 × 12.6 ≈ 3.13 × 10⁸ m/s</text>
  </g>

  <!-- Right Half: Rømer's Io Observations (x=435 to 810) -->
  <g transform="translate(435, 55)">
    <rect x="0" y="0" width="375" height="340" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="187" y="24" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">RØMER'S IO ECLIPSE DELAY (1676)</text>
    
    <!-- Sun at Center -->
    <circle cx="100" cy="115" r="16" fill="#facc15"/>
    <text x="100" y="145" fill="#fde68a" font-size="9" font-weight="700" text-anchor="middle">SUN</text>
    
    <!-- Earth Orbit -->
    <ellipse cx="100" cy="115" rx="55" ry="55" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 3"/>
    <!-- Earth Position 1 (Opposition / Jan) -->
    <circle cx="155" cy="115" r="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="155" y="102" fill="#38bdf8" font-size="8" text-anchor="middle">Earth (Jan)</text>
    
    <!-- Earth Position 2 (Conjunction / Jul) -->
    <circle cx="45" cy="115" r="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="45" y="102" fill="#38bdf8" font-size="8" text-anchor="middle">Earth (Jul)</text>
    
    <!-- Diameter dimension 2R -->
    <line x1="53" y1="128" x2="147" y2="128" stroke="#22c55e" stroke-width="1.5"/>
    <text x="100" y="138" fill="#22c55e" font-size="8" font-weight="700" text-anchor="middle">2 · R_Earth (2 AU)</text>
    
    <!-- Jupiter & Shadow Cone -->
    <circle cx="280" cy="115" r="16" fill="#d97706" stroke="#f59e0b"/>
    <text x="280" y="92" fill="#f59e0b" font-size="9" font-weight="700" text-anchor="middle">JUPITER</text>
    
    <!-- Shadow Cone -->
    <polygon points="296,104 360,95 360,135 296,126" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="335" y="118" fill="#ef4444" font-size="8" text-anchor="middle">Umbra</text>
    
    <!-- Io Moon -->
    <circle cx="310" cy="115" r="3" fill="#fef08a"/>
    <text x="310" y="132" fill="#fef08a" font-size="7" text-anchor="middle">Io</text>
    
    <!-- Formula Box -->
    <rect x="15" y="220" width="345" height="105" fill="#0f172a" rx="6" stroke="#334155"/>
    <text x="25" y="240" fill="#94a3b8" font-size="10">Io Orbital Period: 42.46 hours (~1.77 days)</text>
    <text x="25" y="260" fill="#94a3b8" font-size="10">Diameter transit delay: Δt ≈ 16.6 min = 996 s</text>
    <text x="25" y="285" fill="#22c55e" font-size="13" font-weight="700">Formula: c = (2 · R_Earth) / Δt</text>
    <text x="25" y="308" fill="#38bdf8" font-size="11" font-weight="700">c ≈ (3.0 × 10¹¹ m) / (996 s) ≈ 3.01 × 10⁸ m/s</text>
  </g>
</svg>"""

def main():
    print("=" * 80)
    print("REGISTERING SPEED OF LIGHT SIMULATION IN DJANGO DB")
    print("=" * 80)

    # 1. Register in Simulation table
    sim, created = Simulation.objects.update_or_create(
        key="speed_of_light_experiments",
        defaults={
            "archetype": "speed_of_light_experiments",
            "title": "Speed of Light Historical Laboratory",
            "subject": SubjectDomain.PHYSICS,
            "topic": "Electromagnetic Spectrum",
            "description": "Recreate the landmark historical experiments of Fizeau (rotating toothed wheel) and Rømer (Jupiter's moon Io eclipse delay) to measure the finite speed of light c.",
            "status": SimulationStatus.ACTIVE,
            "config": CONFIG,
        }
    )
    action = "Created" if created else "Updated"
    print(f"[{action}] Simulation ID {sim.id}: {sim.title} (Key: {sim.key})")

    # 2. Check Lesson 245
    lesson245 = Lesson.objects.filter(id=245).first()
    if not lesson245:
        print("ERROR: Lesson 245 not found!")
        return

    print(f"Target Lesson found: ID {lesson245.id} - '{lesson245.title}'")

    # Sanitize SVG
    is_valid, sanitized_svg, err = validate_and_sanitize_svg(SVG_DIAGRAM)
    if not is_valid:
        print(f"SVG Sanitization warning: {err}")
        sanitized_svg = SVG_DIAGRAM

    # 3. Find or create simulation LessonBlock in Lesson 245
    block = LessonBlock.objects.filter(
        lesson=lesson245,
        component_type="suggested_simulation"
    ).first()

    if not block:
        # Also check if any block already has speed_of_light metadata
        block = LessonBlock.objects.filter(
            lesson=lesson245,
            metadata__icontains="speed_of_light"
        ).first()

    if not block:
        # Create new LessonBlock on page 2
        block = LessonBlock.objects.create(
            lesson=lesson245,
            block_id="block_l245_sim_speed_of_light",
            block_type="simulation",
            component_type="suggested_simulation",
            page_number=2,
            page_title="Speed of Light Historical Laboratory",
            component_order=4,
            order=4,
            title="Interactive Simulation: Speed of Light Historical Laboratory (Fizeau & Rømer)",
            content={
                "title": "Speed of Light Historical Laboratory",
                "text": "Interactive laboratory recreating Fizeau's toothed wheel and Rømer's Io eclipse experiments to measure the speed of light.",
                "archetype": "speed_of_light_experiments",
                "simulation_key": "speed_of_light_experiments",
                "subject": "PHYSICS",
                "concept_group": "Electromagnetic Spectrum",
                "config": CONFIG,
                "svg_content": sanitized_svg,
                "svg": sanitized_svg,
            },
            metadata={
                "simulation_key": "speed_of_light_experiments",
                "archetype": "speed_of_light_experiments",
                "subject": "PHYSICS",
                "concept_group": "Electromagnetic Spectrum",
                "title": "Speed of Light Historical Laboratory",
                "config": CONFIG,
                "svg_content": sanitized_svg,
            }
        )
        print(f"[Created] New LessonBlock ID {block.id} for Lesson 245 at order {block.order}")
    else:
        block.title = "Interactive Simulation: Speed of Light Historical Laboratory (Fizeau & Rømer)"
        block.block_type = "simulation"
        block.component_type = "suggested_simulation"
        block.content = {
            **(block.content or {}),
            "title": "Speed of Light Historical Laboratory",
            "text": "Interactive laboratory recreating Fizeau's toothed wheel and Rømer's Io eclipse experiments to measure the speed of light.",
            "archetype": "speed_of_light_experiments",
            "simulation_key": "speed_of_light_experiments",
            "subject": "PHYSICS",
            "concept_group": "Electromagnetic Spectrum",
            "config": CONFIG,
            "svg_content": sanitized_svg,
            "svg": sanitized_svg,
        }
        block.metadata = {
            **(block.metadata or {}),
            "simulation_key": "speed_of_light_experiments",
            "archetype": "speed_of_light_experiments",
            "subject": "PHYSICS",
            "concept_group": "Electromagnetic Spectrum",
            "title": "Speed of Light Historical Laboratory",
            "config": CONFIG,
            "svg_content": sanitized_svg,
        }
        block.save()
        print(f"[Updated] Existing LessonBlock ID {block.id} linked to speed_of_light_experiments")

    # 4. Attach LessonAsset
    asset = LessonAsset.objects.filter(
        lesson=lesson245,
        blocks=block,
        source_type="ai_generated"
    ).first()

    if not asset:
        asset = LessonAsset.objects.create(
            lesson=lesson245,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="embed",
            status="approved",
            title="Speed of Light Historical Laboratory: Fizeau & Rømer",
            description="Vector diagram and interactive simulation anchor for the speed of light historical measurements.",
            metadata={"svg_content": sanitized_svg, "simulation_key": "speed_of_light_experiments"}
        )
        block.assets.add(asset)
        print(f"[Created] Attached LessonAsset ID {asset.id} to LessonBlock {block.id}")
    else:
        asset.title = "Speed of Light Historical Laboratory: Fizeau & Rømer"
        asset.metadata = {**(asset.metadata or {}), "svg_content": sanitized_svg, "simulation_key": "speed_of_light_experiments"}
        asset.save()
        print(f"[Updated] LessonAsset ID {asset.id} for LessonBlock {block.id}")

    print("=" * 80)
    print("SUCCESS: Simulation registered in DB and linked to Lesson 245!")
    print("=" * 80)

if __name__ == "__main__":
    main()
