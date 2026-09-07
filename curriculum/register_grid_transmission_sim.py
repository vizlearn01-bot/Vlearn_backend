"""
Register National Grid High-Voltage Power Transmission Simulator in Django database
and link to Lesson 250 (Grid Supply, High-Voltage Transmission, and Substation Distribution).
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
    print("REGISTERING NATIONAL GRID HIGH-VOLTAGE TRANSMISSION SIMULATOR IN DJANGO DB")
    print("=" * 80)

    sim_data = {
        "key": "high_voltage_grid_transmission",
        "archetype": "high_voltage_grid_transmission",
        "title": "National Grid High-Voltage Power Transmission Simulator",
        "subject": SubjectDomain.PHYSICS,
        "topic": "Mains Electricity",
        "status": SimulationStatus.ACTIVE,
        "description": (
            "Explore why electrical energy is stepped up to hundreds of kilovolts (132 kV, 220 kV, 400 kV) "
            "for national grid transmission. Model Joule heating line loss (P_loss = I²R = P²R / V²), "
            "conductor ampacity limits, cable temperature rise, voltage drop across long transmission spans, "
            "and consumer town substation distribution dynamics."
        ),
        "config": {
            "context_spec": {
                "overview": (
                    "Model national grid transmission physics end-to-end. Control power station output (MW), "
                    "transmission line voltage (kV), transmission distance (km), and conductor specifications. "
                    "Observe animated electron flow, thermal line heating glow, substation step-down transformers, "
                    "and city consumer power reception."
                ),
                "how_to_use": [
                    "Step 1: Select transmission line voltage (11 kV, 33 kV, 66 kV, 132 kV, 220 kV, 400 kV, or catastrophic 240 V).",
                    "Step 2: Adjust power station turbine generation (10 MW to 100 MW) and line distance (10 km to 200 km).",
                    "Step 3: Choose conductor specifications (ACSR Zebra, Lynx, Mink, or hard-drawn copper).",
                    "Step 4: Switch to the 'Voltage Comparison & Proof' tab to study side-by-side quantitative metrics and the 1/V² derivation.",
                    "Step 5: Test your predictive abilities on transmission challenges and solve authentic KCSE exam calculation problems."
                ],
                "expected_results": [
                  {
                    "action": "Transmitting 50 MW at domestic 240 V or 11 kV",
                    "expected_outcome": "Massive current (>4,500 A) causes wire meltdown, extreme Joule heating loss exceeding 100%, and total consumer blackout.",
                    "key_takeaway": "Low-voltage long-distance transmission is physically impossible due to catastrophic I²R heating."
                  },
                  {
                    "action": "Stepping up voltage from 66 kV to 132 kV (doubling V)",
                    "expected_outcome": "Current halves and cable Joule power loss is slashed by a factor of 4 (1/2² = 1/4).",
                    "key_takeaway": "Power loss scales strictly as 1/V² (inversely proportional to voltage squared)."
                  },
                  {
                    "action": "Transmitting at 400 kV Supergrid voltage",
                    "expected_outcome": "Transmission current drops to ~125 A, efficiency exceeds 99%, and conductors remain cool.",
                    "key_takeaway": "High voltage enables light, cost-effective conductors with negligible energy waste."
                  }
                ]
            },
            "default_voltage_kv": 132,
            "default_power_mw": 50,
            "default_distance_km": 100,
            "default_conductor": "acsr_standard",
            "telemetry_events": [
                "change_transmission_voltage",
                "change_generated_power",
                "change_distance",
                "change_conductor",
                "reset_simulation",
                "predictor_challenge_evaluated",
                "kcse_problem_evaluated"
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
        "phys_high_voltage_grid_transmission",
        "grid_transmission_sandbox",
        "grid_transmission",
        "high_voltage_transmission"
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
    print("LINKING SIMULATION TO LESSON 250")
    print("=" * 80)

    try:
        lesson = Lesson.objects.get(id=250)
        print(f"Target Lesson found: ID {lesson.id} - '{lesson.title}' (Topic: {lesson.topic.name if lesson.topic else 'N/A'})")

        # Check Block 14701
        b14701 = LessonBlock.objects.filter(id=14701).first()
        if b14701:
            b14701.block_type = "suggested_simulation"
            b14701.component_type = "suggested_simulation"
            b14701.title = "Interactive Grid Sandbox: High-Voltage Power Loss Calculator & Substation Step-Down Dynamics"

            # Update metadata
            meta = b14701.metadata or {}
            meta.update({
                "simulation_key": "high_voltage_grid_transmission",
                "archetype": "high_voltage_grid_transmission",
                "subject": "PHYSICS",
                "concept_group": "National Grid Power Transmission",
                "config": sim_data["config"]
            })
            b14701.metadata = meta

            # Update content
            content = b14701.content if isinstance(b14701.content, dict) else {}
            content.update({
                "text": "Interactive Grid Sandbox: High-Voltage Power Loss Calculator & Substation Step-Down Dynamics",
                "simulation_key": "high_voltage_grid_transmission",
                "archetype": "high_voltage_grid_transmission",
            })
            b14701.content = content
            b14701.save()
            print(f"Successfully linked Block 14701 to simulation_key 'high_voltage_grid_transmission'!")
        else:
            print("Warning: Block 14701 not found. Looking for existing suggested_simulation block...")
            sim_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_simulation"
            ).first()
            if sim_block:
                sim_block.metadata = {
                    **(sim_block.metadata or {}),
                    "simulation_key": "high_voltage_grid_transmission",
                    "archetype": "high_voltage_grid_transmission",
                }
                sim_block.save()
                print(f"Linked existing suggested_simulation Block {sim_block.id}")

    except Lesson.DoesNotExist:
        print("Warning: Lesson 250 not found in database.")

    print("=" * 80)
    print("NATIONAL GRID TRANSMISSION SIMULATION REGISTRATION COMPLETE!")
    print("=" * 80)

if __name__ == "__main__":
    register_simulation()
