"""
Register Physics Simulations in Django database for the Simulations Hub page.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Simulation

PHYSICS_SIMS = [
    {
        "key": "optics",
        "archetype": "optics",
        "title": "Thin Lens Ray Tracing & Image Formation",
        "subject": "PHYSICS",
        "topic": "Thin Lenses",
        "description": "Manipulate object distance, focal length, and convex/concave lens geometry in real-time to observe principal rays and calculate image distance and magnification.",
        "status": "ACTIVE",
    },
    {
        "key": "crt",
        "archetype": "crt",
        "title": "Cathode Ray Oscilloscope & Electron Beam Deflection",
        "subject": "PHYSICS",
        "topic": "Cathode Rays",
        "description": "Control accelerating anode potential, electrostatic Y-deflection plates, and time-base sweep frequency to observe electron trajectory and CRO waveforms.",
        "status": "ACTIVE",
    },
    {
        "key": "x_ray",
        "archetype": "x_ray",
        "title": "Coolidge X-Ray Tube & Duane-Hunt Cutoff Spectrum",
        "subject": "PHYSICS",
        "topic": "X-Rays",
        "description": "Investigate independent hardness and intensity control in Coolidge tubes and observe Duane-Hunt cutoff wavelength and characteristic line spectra.",
        "status": "ACTIVE",
    },
    {
        "key": "photoelectric",
        "archetype": "photoelectric",
        "title": "Einstein's Photoelectric Effect & Stopping Potential",
        "subject": "PHYSICS",
        "topic": "Photoelectric Effect",
        "description": "Illuminate metal cathode surfaces with variable wavelength and intensity to observe quantum photoelectron emission, stopping potential, and work function.",
        "status": "ACTIVE",
    },
]

def register_simulations():
    print("=" * 80)
    print("REGISTERING PHYSICS SIMULATIONS IN DATABASE")
    print("=" * 80)

    for data in PHYSICS_SIMS:
        sim, created = Simulation.objects.update_or_create(
            key=data["key"],
            defaults={
                "archetype": data["archetype"],
                "title": data["title"],
                "subject": data["subject"],
                "topic": data["topic"],
                "description": data["description"],
                "status": data["status"],
            }
        )
        action = "Created" if created else "Updated"
        print(f"{action} simulation: ID {sim.id} | [{sim.subject}] {sim.title} (Key: {sim.key})")

    print("=" * 80)
    print("ALL PHYSICS SIMULATIONS REGISTERED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    register_simulations()
