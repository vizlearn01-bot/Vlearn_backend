"""
Register Interactive EM Spectrum Bands & Wavelength Analyzer in Django database
and link to Lesson 245 (Experimental Speed of Light and Spectral Band Analysis).
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Simulation, Lesson, LessonBlock, SubjectDomain, SimulationStatus

def register_simulation():
    print("=" * 80)
    print("REGISTERING EM SPECTRUM ANALYZER SIMULATION IN DJANGO DB")
    print("=" * 80)

    sim_data = {
        "key": "em_spectrum_analyzer_bands",
        "archetype": "em_spectrum_analyzer_bands",
        "title": "Interactive EM Spectrum Bands & Wavelength Analyzer",
        "subject": SubjectDomain.PHYSICS,
        "topic": "Electromagnetic Spectrum",
        "status": SimulationStatus.ACTIVE,
        "description": (
            "Continuously explore all 7 major electromagnetic spectrum bands (Radio, Microwave, "
            "Infrared, Visible, Ultraviolet, X-Rays, Gamma Rays) across 24 orders of magnitude. "
            "Examine frequency (c = fλ), photon energy (E = hf), Wien's displacement law, "
            "relative physical scale benchmarks, and ionizing vs. non-ionizing radiation thresholds."
        ),
        "config": {
            "context_spec": {
                "overview": (
                    "Explore the continuous electromagnetic spectrum across all 7 major bands. "
                    "Manipulate wavelength on a 24-order-of-magnitude logarithmic slider, compare scales "
                    "to real-world objects, verify wave equations, and inspect ionizing safety limits."
                ),
                "how_to_use": [
                    "Step 1: Drag the logarithmic slider to span wavelengths from 10⁻¹⁴ m to 10⁴ m.",
                    "Step 2: Jump between all 7 major spectral regions using the quick band buttons.",
                    "Step 3: Analyze the expanded ROYGBIV color breakdown and exact nanometer swatch in the visible band.",
                    "Step 4: Observe the physical scale comparison showing what real-world object matches the current wavelength.",
                    "Step 5: Solve KCSE exam calculation problems with immediate marking scheme feedback."
                ],
                "expected_results": [
                  {
                    "action": "Decreasing Wavelength (λ ↓)",
                    "expected_outcome": "Frequency (f ↑) and photon energy (E ↑) increase inversely.",
                    "key_takeaway": "Wave speed in vacuum c = 3.0×10⁸ m/s remains constant for all EM radiation."
                  },
                  {
                    "action": "Transitioning Past UV Threshold (< 100 nm, E > 10 eV)",
                    "expected_outcome": "Radiation transitions into ionizing hazard.",
                    "key_takeaway": "Ionizing radiation knocks electrons free from atoms and causes double-strand DNA cleavage."
                  }
                ]
            },
            "default_wavelength_nm": 550,
            "min_log_lambda": -14.0,
            "max_log_lambda": 4.0
        }
    }

    sim, created = Simulation.objects.update_or_create(
        key=sim_data["key"],
        defaults=sim_data
    )
    action = "Created" if created else "Updated"
    print(f"{action} Primary Simulation: ID {sim.id} | [{sim.subject}] {sim.title} (Key: {sim.key})")

    # Also register alias keys so factory & router can look it up with any variant
    alias_keys = ["phys_em_spectrum_analyzer_bands", "em_spectrum_analyzer"]
    for a_key in alias_keys:
        a_sim, a_created = Simulation.objects.update_or_create(
            key=a_key,
            defaults={
                **sim_data,
                "key": a_key,
                "title": f"{sim_data['title']} ({a_key})"
            }
        )
        a_act = "Created" if a_created else "Updated"
        print(f"  {a_act} Alias Simulation: ID {a_sim.id} (Key: {a_sim.key})")

    print("\n" + "=" * 80)
    print("LINKING SIMULATION TO LESSON 245")
    print("=" * 80)

    try:
        lesson = Lesson.objects.get(id=245)
        print(f"Target Lesson found: ID {lesson.id} - '{lesson.title}'")

        # Check if suggested_simulation block already exists for this lesson
        sim_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_simulation"
        ).first()

        if not sim_block:
            # Create a dedicated suggested_simulation block on page 6
            max_order_p6 = LessonBlock.objects.filter(lesson=lesson, page_number=6).order_by('-order').first()
            target_order = (max_order_p6.order + 1) if max_order_p6 else 10

            sim_block = LessonBlock.objects.create(
                lesson=lesson,
                block_type="suggested_simulation",
                component_type="suggested_simulation",
                title="Interactive EM Spectrum Bands & Wavelength Analyzer",
                page_number=6,
                page_title="The Complete Electromagnetic Spectrum Continuum",
                order=target_order,
                component_order=4,
                metadata={
                    "simulation_key": "em_spectrum_analyzer_bands",
                    "archetype": "em_spectrum_analyzer_bands",
                    "subject": "PHYSICS",
                    "concept_group": "Interactive Simulation: EM Spectrum Bands",
                    "config": sim_data["config"]
                },
                content={
                    "text": "Launch the Interactive EM Spectrum Bands & Wavelength Analyzer to explore continuous spectral bands, wave equations, real-world scale benchmarks, and ionizing radiation thresholds.",
                    "simulation_key": "em_spectrum_analyzer_bands",
                    "archetype": "em_spectrum_analyzer_bands"
                }
            )
            print(f"Created new suggested_simulation block: ID {sim_block.id} (Order {sim_block.order}, Page {sim_block.page_number})")
        else:
            sim_block.title = "Interactive EM Spectrum Bands & Wavelength Analyzer"
            sim_block.component_type = "suggested_simulation"
            sim_block.metadata = {
                **(sim_block.metadata or {}),
                "simulation_key": "em_spectrum_analyzer_bands",
                "archetype": "em_spectrum_analyzer_bands",
                "subject": "PHYSICS",
                "concept_group": "Interactive Simulation: EM Spectrum Bands",
                "config": sim_data["config"]
            }
            sim_block.content = {
                **(sim_block.content if isinstance(sim_block.content, dict) else {}),
                "text": "Launch the Interactive EM Spectrum Bands & Wavelength Analyzer to explore continuous spectral bands, wave equations, real-world scale benchmarks, and ionizing radiation thresholds.",
                "simulation_key": "em_spectrum_analyzer_bands",
                "archetype": "em_spectrum_analyzer_bands"
            }
            sim_block.save()
            print(f"Updated existing suggested_simulation block: ID {sim_block.id}")

        # Also annotate diagram block 14604 with simulation_key metadata
        b14604 = LessonBlock.objects.filter(id=14604).first()
        if b14604:
            if not b14604.metadata:
                b14604.metadata = {}
            b14604.metadata["simulation_key"] = "em_spectrum_analyzer_bands"
            b14604.metadata["archetype"] = "em_spectrum_analyzer_bands"
            b14604.save()
            print(f"Linked diagram Block 14604 to simulation key 'em_spectrum_analyzer_bands'")

    except Lesson.DoesNotExist:
        print("Warning: Lesson 245 not found in database.")

    print("=" * 80)
    print("EM SPECTRUM ANALYZER SIMULATION REGISTRATION COMPLETE!")
    print("=" * 80)

if __name__ == "__main__":
    register_simulation()
