"""
Register Physics Simulations in Django database for the Simulations Hub page.
Includes all Form 4 Physics Topics 8-11 simulations.
"""

import os
import sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")

import django
django.setup()

from curriculum.models import Simulation

PHYSICS_SIMS = [
    # Topic 1: Thin Lenses
    {
        "key": "optics",
        "archetype": "optics",
        "title": "Thin Lens Ray Tracing & Image Formation",
        "subject": "PHYSICS",
        "topic": "Thin Lenses",
        "description": "Manipulate object distance, focal length, and convex/concave lens geometry in real-time to observe principal rays and calculate image distance and magnification.",
        "status": "ACTIVE",
    },
    # Topic 7: Cathode Rays
    {
        "key": "crt",
        "archetype": "crt",
        "title": "Cathode Ray Oscilloscope & Electron Beam Deflection",
        "subject": "PHYSICS",
        "topic": "Cathode Rays",
        "description": "Control accelerating anode potential, electrostatic Y-deflection plates, and time-base sweep frequency to observe electron trajectory and CRO waveforms.",
        "status": "ACTIVE",
    },
    # Topic 8: X-Rays
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
        "key": "xray_intensity_vs_hardness_control",
        "archetype": "xray_intensity_vs_hardness_control",
        "title": "X-Ray Tube Intensity vs Hardness Control Simulator",
        "subject": "PHYSICS",
        "topic": "X-Rays",
        "description": "Control filament heating current and anode accelerating voltage to observe independent effects on spectrum.",
        "status": "ACTIVE",
    },
    {
        "key": "xray_attenuation_radiography",
        "archetype": "xray_attenuation_radiography",
        "title": "X-Ray Attenuation, Half-Value Layer & Radiography Simulator",
        "subject": "PHYSICS",
        "topic": "X-Rays",
        "description": "Simulate differential X-ray absorption in bone, tissue, and industrial welded joints with lead shielding.",
        "status": "ACTIVE",
    },
    {
        "key": "braggs_law_crystal_diffraction",
        "archetype": "braggs_law_crystal_diffraction",
        "title": "Bragg's Law & X-Ray Crystal Diffraction Spectrometer",
        "subject": "PHYSICS",
        "topic": "X-Rays",
        "description": "Investigate crystal lattice diffraction condition n*lambda = 2d*sin(theta).",
        "status": "ACTIVE",
    },
    # Topic 9: Photoelectric Effect
    {
        "key": "photoelectric",
        "archetype": "photoelectric",
        "title": "Einstein's Photoelectric Effect & Stopping Potential",
        "subject": "PHYSICS",
        "topic": "Photoelectric Effect",
        "description": "Illuminate metal cathode surfaces with variable wavelength and intensity to observe quantum photoelectron emission, stopping potential, and work function.",
        "status": "ACTIVE",
    },
    {
        "key": "stopping_potential_planck_graph",
        "archetype": "stopping_potential_planck_graph",
        "title": "Stopping Potential & Planck's Constant Determination",
        "subject": "PHYSICS",
        "topic": "Photoelectric Effect",
        "description": "Plot stopping potential Vs against frequency f to determine Planck constant h/e and threshold frequency f0.",
        "status": "ACTIVE",
    },
    {
        "key": "photon_intensity_vs_current",
        "archetype": "photon_intensity_vs_current",
        "title": "Photon Flux & Photocurrent vs Light Intensity Simulator",
        "subject": "PHYSICS",
        "topic": "Photoelectric Effect",
        "description": "Investigate the linear proportionality between photon flux and saturation photocurrent.",
        "status": "ACTIVE",
    },
    {
        "key": "photocell_circuit_applications",
        "archetype": "photocell_circuit_applications",
        "title": "Photocell Circuit Applications & Light Sensors",
        "subject": "PHYSICS",
        "topic": "Photoelectric Effect",
        "description": "Explore industrial burglar alarm relays, automatic street lighting LDR circuits, and solar meters.",
        "status": "ACTIVE",
    },
    # Topic 10: Radioactivity & Nuclear Physics
    {
        "key": "radioactive_decay_half_life",
        "archetype": "radioactive_decay_half_life",
        "title": "Radioactive Decay Kinetics & Half-Life Explorer",
        "subject": "PHYSICS",
        "topic": "Radioactivity & Nuclear Physics",
        "description": "Track radioactive sample populations over time and determine half-life milestones.",
        "status": "ACTIVE",
    },
    {
        "key": "nuclear_fission_chain_reaction",
        "archetype": "nuclear_fission_chain_reaction",
        "title": "Nuclear Fission, Chain Reaction & Control Rod Reactor Simulator",
        "subject": "PHYSICS",
        "topic": "Radioactivity & Nuclear Physics",
        "description": "Observe neutron-induced fission of U-235, chain reaction multiplication, and control rod absorption.",
        "status": "ACTIVE",
    },
    {
        "key": "radiation_deflection_shielding_alpha_beta_gamma",
        "archetype": "radiation_deflection_shielding_alpha_beta_gamma",
        "title": "Radiation Deflection & Shielding Penetration (Alpha, Beta, Gamma)",
        "subject": "PHYSICS",
        "topic": "Radioactivity & Nuclear Physics",
        "description": "Analyze trajectory deflection of alpha, beta, and gamma emissions in electric/magnetic fields.",
        "status": "ACTIVE",
    },
    {
        "key": "binding_energy_per_nucleon_curve",
        "archetype": "binding_energy_per_nucleon_curve",
        "title": "Nuclear Binding Energy & Mass Defect Curve Explorer",
        "subject": "PHYSICS",
        "topic": "Radioactivity & Nuclear Physics",
        "description": "Investigate nuclear mass defect, binding energy Eb = delta_m * 931.5 MeV, and Fe-56 stability peak.",
        "status": "ACTIVE",
    },
    # Topic 11: Electronics & Logic Gates
    {
        "key": "pn_junction_diode_rectification",
        "archetype": "pn_junction_diode_rectification",
        "title": "P-N Junction Diode & AC Rectification Circuits",
        "subject": "PHYSICS",
        "topic": "Electronics & Logic Gates",
        "description": "Compare half-wave and full-wave bridge rectifier circuits with capacitor smoothing filters on dual-trace oscilloscope.",
        "status": "ACTIVE",
    },
    {
        "key": "digital_logic_gates_truth_tables",
        "archetype": "digital_logic_gates_truth_tables",
        "title": "Digital Logic Gates & Live Truth Table Explorer",
        "subject": "PHYSICS",
        "topic": "Electronics & Logic Gates",
        "description": "Interactive AND, OR, NOT, NAND, NOR, and XOR logic gates with live truth table row evaluation.",
        "status": "ACTIVE",
    },
    {
        "key": "transistor_switch_sensor_circuit",
        "archetype": "transistor_switch_sensor_circuit",
        "title": "Transistor as an Electronic Switch & Sensor Circuit",
        "subject": "PHYSICS",
        "topic": "Electronics & Logic Gates",
        "description": "Demonstrate NPN common-emitter switching with potential divider bias across LDR and thermistor sensors.",
        "status": "ACTIVE",
    },
    {
        "key": "combinational_logic_half_adder",
        "archetype": "combinational_logic_half_adder",
        "title": "Combinational Logic & Binary Half-Adder / Full-Adder Circuit",
        "subject": "PHYSICS",
        "topic": "Electronics & Logic Gates",
        "description": "Build binary adders using XOR and AND gates to perform computer arithmetic addition.",
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
