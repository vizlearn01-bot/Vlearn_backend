"""
Register Faraday's Law & Magnetic Flux Induction Lab in Django database
and link to Lesson 247 (Induced E.M.F., Faraday's Law, and Lenz's Law).
"""

import os
import sys

# Load environment variables from .env if present
env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ[k.strip()] = v.strip()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")

import django
django.setup()

from curriculum.models import Simulation, Lesson, LessonBlock, SubjectDomain, SimulationStatus

def register_simulation():
    print("=" * 80)
    print("REGISTERING FARADAY'S LAW & MAGNETIC FLUX INDUCTION LAB IN DJANGO DB")
    print("=" * 80)

    sim_data = {
        "key": "faradays_law_magnetic_flux",
        "archetype": "faradays_law_magnetic_flux",
        "title": "Faraday's Law & Magnetic Flux Induction Lab",
        "subject": SubjectDomain.PHYSICS,
        "topic": "Electromagnetic Induction",
        "status": SimulationStatus.ACTIVE,
        "description": (
            "Verify Faraday's Law of Electromagnetic Induction (ε = -N · ΔΦ/Δt) and Lenz's Law. "
            "Interactively drag a bar magnet into and out of multi-turn solenoids (100, 200, 500 turns), "
            "control magnetic flux density B (0.05 to 0.50 T), switch pole orientations, observe animated flux lines, "
            "and measure deflection on a critically damped center-zero galvanometer with a live dual-trace oscilloscope."
        ),
        "config": {
            "context_spec": {
                "overview": (
                    "Explore electromagnetic induction in real time. Manipulate magnet velocity, solenoid turns, "
                    "and magnetic dipole strength. Observe instantaneous magnetic flux linkage, opposing induced poles, "
                    "and center-zero galvanometer needle deflection."
                ),
                "how_to_use": [
                    "Step 1: Grab and drag the bar magnet horizontally into and through the solenoid coil, or use the automated 'Plunge In' / 'Withdraw' / 'Auto Oscillate' buttons.",
                    "Step 2: Adjust coil turns (100, 200, 500 turns) and magnetic field strength B (0.05 to 0.50 T) to observe how induced EMF scales.",
                    "Step 3: Toggle magnet polarity (N-pole leading vs S-pole leading) to observe reversal in galvanometer deflection.",
                    "Step 4: Switch to the 'Lenz's Law & Predictor' tab to test predictions on induced face poles and verify conservation of energy.",
                    "Step 5: Solve KCSE exam calculation problems with instantaneous KNEC marking scheme breakdown."
                ],
                "expected_results": [
                  {
                    "action": "Moving magnet into coil (plunging in)",
                    "expected_outcome": "Needle deflects in one direction while magnet moves; returns to zero immediately when stationary.",
                    "key_takeaway": "Induced EMF is proportional to the rate of change of flux (dΦ/dt), NOT static flux magnitude."
                  },
                  {
                    "action": "Holding magnet stationary inside coil",
                    "expected_outcome": "Deflection drops to strictly ZERO (0 mV).",
                    "key_takeaway": "Without relative motion, ΔΦ/Δt = 0, so no electromotive force is induced."
                  },
                  {
                    "action": "Reversing magnet direction (withdrawing)",
                    "expected_outcome": "Needle deflects in the opposite direction.",
                    "key_takeaway": "Lenz's Law ensures the induced magnetic field opposes the change in flux causing it."
                  },
                  {
                    "action": "Increasing coil turns from 100 to 500",
                    "expected_outcome": "Peak induced EMF increases 5-fold.",
                    "key_takeaway": "Induced voltage is directly proportional to number of turns (ε ∝ N)."
                  }
                ]
            },
            "default_turns": 200,
            "default_b_field": 0.20,
            "default_speed": 0.8,
            "default_polarity": "N_RIGHT",
            "telemetry_events": [
                "magnet_drag_start",
                "magnet_drag_end",
                "change_turns",
                "change_field_strength",
                "change_target_speed",
                "change_motion_mode",
                "toggle_polarity",
                "reset_simulation",
                "predictor_evaluated",
                "kcse_problem_attempted"
            ]
        }
    }

    # Primary simulation
    sim, created = Simulation.objects.update_or_create(
        key=sim_data["key"],
        defaults=sim_data
    )
    action = "Created" if created else "Updated"
    print(f"{action} Primary Simulation: ID {sim.id} | [{sim.subject}] {sim.title} (Key: {sim.key})")

    # Alias keys
    alias_keys = [
        "phys_faradays_law_magnetic_flux",
        "faradays_law",
        "faraday_induction",
        "induction_sandbox"
    ]
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
    print("LINKING SIMULATION TO LESSON 247")
    print("=" * 80)

    try:
        lesson = Lesson.objects.get(id=247)
        print(f"Target Lesson found: ID {lesson.id} - '{lesson.title}' (Topic: {lesson.topic.name})")

        # Check Block 14645
        b14645 = LessonBlock.objects.filter(id=14645).first()
        if b14645:
            b14645.block_type = "suggested_simulation"
            b14645.component_type = "suggested_simulation"
            b14645.title = "Interactive Induction Sandbox: Faraday's Magnetic Flux Linkage & Lenz's Law Deflection"
            
            # Update metadata
            meta = b14645.metadata or {}
            meta.update({
                "simulation_key": "faradays_law_magnetic_flux",
                "archetype": "faradays_law_magnetic_flux",
                "subject": "PHYSICS",
                "concept_group": "Faraday's Law & Magnetic Flux Induction",
                "config": sim_data["config"]
            })
            b14645.metadata = meta

            # Update content
            content = b14645.content if isinstance(b14645.content, dict) else {}
            content.update({
                "text": "Interactive Induction Sandbox: Faraday's Magnetic Flux Linkage & Lenz's Law Deflection",
                "simulation_key": "faradays_law_magnetic_flux",
                "archetype": "faradays_law_magnetic_flux",
            })
            b14645.content = content
            b14645.save()
            print(f"Successfully linked Block 14645 to simulation_key 'faradays_law_magnetic_flux'!")
        else:
            print("Warning: Block 14645 not found. Looking for existing suggested_simulation block...")
            sim_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_simulation"
            ).first()
            if sim_block:
                sim_block.metadata = {
                    **(sim_block.metadata or {}),
                    "simulation_key": "faradays_law_magnetic_flux",
                    "archetype": "faradays_law_magnetic_flux",
                }
                sim_block.save()
                print(f"Linked existing suggested_simulation Block {sim_block.id}")

    except Lesson.DoesNotExist:
        print("Warning: Lesson 247 not found in database.")

    print("=" * 80)
    print("FARADAY'S LAW SIMULATION REGISTRATION COMPLETE!")
    print("=" * 80)

if __name__ == "__main__":
    register_simulation()
