"""
Register Lenz's Law & Eddy Currents Damping Explorer in Django database
and link to Lesson 247 (Induced E.M.F., Faraday's Law, and Lenz's Law).
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Simulation, Lesson, LessonBlock, LessonAsset, SubjectDomain, SimulationStatus

def register_simulation():
    print("=" * 80)
    print("REGISTERING LENZ'S LAW & EDDY CURRENTS SIMULATION IN DJANGO DB")
    print("=" * 80)

    sim_data = {
        "key": "lenzs_law_eddy_currents",
        "archetype": "lenzs_law_eddy_currents",
        "title": "Lenz's Law & Eddy Currents Damping Explorer",
        "subject": SubjectDomain.PHYSICS,
        "topic": "Electromagnetic Induction",
        "status": SimulationStatus.ACTIVE,
        "description": (
            "Interactive investigation into Lenz's Law of electromagnetic opposition and eddy current "
            "damping in non-magnetic conducting tubes. Examine induced magnetic poles, center-zero galvanometer "
            "needle deflection, repulsive/attractive mechanical forces opposing hand motion, slow-motion "
            "terminal velocity descent through solid vs slotted copper pipes, and solve authentic KCSE mastery problems."
        ),
        "config": {
            "context_spec": {
                "overview": (
                    "Explore the fundamental principle that induced currents always oppose the magnetic flux "
                    "change producing them. Manipulate bar magnet approach and withdrawal to observe induced coil "
                    "poles and galvanometer deflection, drop neodymium magnets through copper and plastic pipes to "
                    "witness eddy current magnetic braking, and analyze the energy conservation basis of induction."
                ),
                "how_to_use": [
                    "Mode 1: Thrust the North or South pole of the magnet towards and away from the solenoid coil. Observe coil polarity badges, repulsive/attractive force vectors, and galvanometer needle deflection.",
                    "Mode 2: Release magnets simultaneously through the conductive copper pipe and non-conductive plastic pipe. Compare live stopwatches, terminal velocities, and inspect circular eddy current loops.",
                    "Mode 2 (Slots): Toggle 'Slotted Copper' to discover how longitudinal slits interrupt circumferential eddy current loops and increase descent speed.",
                    "Mode 3: Solve KCSE exam problems with instant marking scheme feedback, hints, and step-by-step solutions."
                ],
                "expected_results": [
                  {
                    "action": "Approaching North pole into Solenoid (v > 0 towards coil)",
                    "expected_outcome": "Facing end becomes an induced North pole; repulsive force pushes back against hand.",
                    "key_takeaway": "Work done against repulsion is converted into electrical energy, proving Lenz's Law is a consequence of Conservation of Energy."
                  },
                  {
                    "action": "Dropping magnet through solid copper pipe vs plastic pipe",
                    "expected_outcome": "Magnet in copper pipe reaches terminal velocity (~0.24 m/s) taking ~4 s; magnet in plastic pipe free-falls in ~0.45 s.",
                    "key_takeaway": "Moving flux cuts copper wall, inducing circular eddy currents whose magnetic fields create upward braking forces."
                  },
                  {
                    "action": "Slotted copper pipe with longitudinal slit",
                    "expected_outcome": "Magnet falls significantly faster (~0.8 s) than in solid copper pipe.",
                    "key_takeaway": "Longitudinal slits break continuous circular conduction loops, drastically reducing eddy current braking."
                  }
                ]
            },
            "default_turns": 500,
            "default_facing_pole": "N",
            "tube_length_m": 1.0,
            "copper_damping_coef": 1.25,
            "plastic_damping_coef": 0.0
        }
    }

    sim, created = Simulation.objects.update_or_create(
        key=sim_data["key"],
        defaults=sim_data
    )
    action = "Created" if created else "Updated"
    print(f"{action} Primary Simulation: ID {sim.id} | [{sim.subject}] {sim.title} (Key: {sim.key})")

    # Also register alias keys for router and factory lookups
    alias_keys = [
        "phys_lenzs_law_eddy_currents",
        "lenzs_law",
        "eddy_currents",
        "lenz_law",
        "eddy_currents_damping",
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
        print(f"Target Lesson found: ID {lesson.id} - '{lesson.title}'")

        # Find simulation block in Lesson 247
        sim_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type__in=["suggested_simulation", "simulation_placeholder"]
        ).first()

        if not sim_block:
            # Look for block with sandbox or interactive title
            sim_block = LessonBlock.objects.filter(
                lesson=lesson,
                title__icontains="sandbox"
            ).first()

        if sim_block:
            print(f"Found existing Block ID {sim_block.id} (Type: {sim_block.block_type}) - Updating...")
        else:
            print("Creating new simulation block for Lesson 247...")
            sim_block = LessonBlock(lesson=lesson)

        sim_block.block_type = "suggested_simulation"
        sim_block.component_type = "suggested_simulation"
        sim_block.title = "Lenz's Law & Eddy Currents Damping Explorer"
        sim_block.page_title = "Interactive Simulation: Lenz's Law & Eddy Currents Damping Explorer"

        # Update metadata and content payloads
        content_dict = sim_block.content if isinstance(sim_block.content, dict) else {}
        content_dict.update({
            "simulation_key": "lenzs_law_eddy_currents",
            "archetype": "lenzs_law_eddy_currents",
            "title": "Lenz's Law & Eddy Currents Damping Explorer",
            "subject": "PHYSICS",
            "topic": "Electromagnetic Induction",
            "config": sim.config
        })
        sim_block.content = content_dict

        meta_dict = sim_block.metadata if isinstance(sim_block.metadata, dict) else {}
        meta_dict.update({
            "simulation_key": "lenzs_law_eddy_currents",
            "archetype": "lenzs_law_eddy_currents",
            "subject": "PHYSICS",
            "topic": "Electromagnetic Induction",
            "concept_group": "Lenz's Law & Eddy Currents Damping Explorer",
            "config": sim.config
        })
        sim_block.metadata = meta_dict
        sim_block.save()
        print(f"Updated LessonBlock: ID {sim_block.id} (Page {sim_block.page_number}, Order {sim_block.order})")

        # Create or update attached LessonAsset
        asset, a_created = LessonAsset.objects.get_or_create(
            lesson=lesson,
            asset_type="simulation",
            defaults={
                "source_type": "knowledge_repository",
                "storage_type": "url",
                "status": "approved",
                "title": "Lenz's Law & Eddy Currents Damping Explorer",
                "url": "simulation://lenzs_law_eddy_currents",
                "metadata": {
                    "simulation_key": "lenzs_law_eddy_currents",
                    "archetype": "lenzs_law_eddy_currents",
                    "subject": "PHYSICS",
                    "topic": "Electromagnetic Induction",
                    "config": sim.config
                }
            }
        )
        if not a_created:
            asset.title = "Lenz's Law & Eddy Currents Damping Explorer"
            asset.url = "simulation://lenzs_law_eddy_currents"
            asset.status = "approved"
            asset.metadata = {
                **(asset.metadata or {}),
                "simulation_key": "lenzs_law_eddy_currents",
                "archetype": "lenzs_law_eddy_currents",
                "subject": "PHYSICS",
                "topic": "Electromagnetic Induction",
                "config": sim.config
            }
            asset.save()
        
        sim_block.assets.add(asset)
        act_str = "Created" if a_created else "Updated"
        print(f"{act_str} LessonAsset: ID {asset.id} | Attached to Block {sim_block.id}")

    except Lesson.DoesNotExist:
        print("Lesson 247 not found in database!")

    print("\n" + "=" * 80)
    print("REGISTRATION & LINKING COMPLETE!")
    print("=" * 80)

if __name__ == "__main__":
    register_simulation()
