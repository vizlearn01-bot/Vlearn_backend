#!/usr/bin/env python
"""
add_gas_laws_mole_media_blocks.py
Adds video_ref and suggested_simulation blocks to Form 3 Chemistry
Topic 1 (Gas Laws) and Topic 2 (The Mole) lessons.

Run from Vlearn_backend/:
  venv/bin/python curriculum/add_gas_laws_mole_media_blocks.py
"""
import sys, os, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock
from Resources.models import ExperimentVideo

# ── helpers ─────────────────────────────────────────────────────────────────

def get_next_order(lesson):
    last = LessonBlock.objects.filter(lesson=lesson).order_by('-order').first()
    return (last.order if last else 0) + 1


def add_video_ref_block(lesson, title, description, youtube_url=None, experiment_id=None):
    if LessonBlock.objects.filter(lesson=lesson, title=title).exists():
        print(f"  [SKIP] '{title}'")
        return None

    if youtube_url:
        content = {"url": youtube_url, "title": title, "description": description}
    elif experiment_id:
        ev = ExperimentVideo.objects.get(id=experiment_id)
        cfid = ev.cloudflare_video_id
        content = {
            "title": title,
            "description": description,
            "duration": ev.duration,
            "difficulty": ev.difficulty,
            "playback_url": f"https://videodelivery.net/{cfid}/manifest/video.m3u8",
            "resolved_url": f"https://videodelivery.net/{cfid}/manifest/video.m3u8",
            "experiment_id": experiment_id,
            "cloudflare_video_id": cfid,
        }
    else:
        raise ValueError("Must provide youtube_url or experiment_id")

    block = LessonBlock.objects.create(
        lesson=lesson, block_type='video_ref', title=title,
        content=content, order=get_next_order(lesson), page_number=None,
    )
    print(f"  [+] video_ref #{block.id}: {title}")
    return block


def add_simulation_block(lesson, title, description, archetype):
    if LessonBlock.objects.filter(lesson=lesson, title=title).exists():
        print(f"  [SKIP] sim '{title}'")
        return None

    content = {"archetype": archetype, "title": title, "description": description}
    block = LessonBlock.objects.create(
        lesson=lesson, block_type='suggested_simulation', title=title,
        content=content, order=get_next_order(lesson), page_number=None,
    )
    print(f"  [+] suggested_simulation #{block.id}: {title}")
    return block


# ── Lessons ──────────────────────────────────────────────────────────────────
L159 = Lesson.objects.get(id=159)
L160 = Lesson.objects.get(id=160)
L161 = Lesson.objects.get(id=161)
L162 = Lesson.objects.get(id=162)
L163 = Lesson.objects.get(id=163)
L165 = Lesson.objects.get(id=165)
L166 = Lesson.objects.get(id=166)
L167 = Lesson.objects.get(id=167)
L169 = Lesson.objects.get(id=169)
L170 = Lesson.objects.get(id=170)
L171 = Lesson.objects.get(id=171)


# ── TOPIC 1: GAS LAWS ────────────────────────────────────────────────────────

print("\n=== Lesson 160: Boyle's Law ===")
add_simulation_block(
    L160,
    title="Interactive Simulation: Boyle's Law",
    description="Drag the plunger to compress a gas in a syringe. Watch pressure rise as volume falls — see Boyle's Law confirmed in real time on a live P-V graph.",
    archetype="boyles_law",
)
add_video_ref_block(
    L160,
    title="Video Demonstration: Boyle's Law — Syringe Experiment",
    description="An experimental demonstration showing how gas pressure increases as volume decreases at constant temperature, directly verifying Boyle's Law.",
    youtube_url="https://www.youtube.com/watch?v=0hnBbEWqAJA",
)

print("\n=== Lesson 161: Charles's Law ===")
add_video_ref_block(
    L161,
    title="Laboratory Experiment: Charles's Law — Gas Volume and Temperature",
    description="Recorded lab demonstration showing how a trapped gas expands as its temperature increases at constant pressure, directly verifying Charles's Law.",
    experiment_id=3,
)
add_simulation_block(
    L161,
    title="Interactive Simulation: Charles's Law",
    description="Heat or cool a trapped gas and observe how the piston moves. A live V-T graph shows the direct proportionality and where 0 K (absolute zero) falls.",
    archetype="charles_law_guided",
)
add_video_ref_block(
    L161,
    title="Real-World Application: Hot-Air Balloon Inflation",
    description="Watch hot air balloons inflate and launch — a vivid real-world demonstration of Charles's Law as heated air expands to lift the balloon.",
    youtube_url="https://www.youtube.com/watch?v=4M4gSQT2loY",
)

print("\n=== Lesson 163: Graham's Law of Diffusion ===")
add_video_ref_block(
    L163,
    title="Laboratory Experiment: Diffusion in Liquids (Potassium Permanganate)",
    description="Observing particle movement in water without stirring — potassium permanganate crystals slowly diffuse, demonstrating that diffusion occurs in liquids.",
    experiment_id=14,
)
add_video_ref_block(
    L163,
    title="Laboratory Experiment: Diffusion of Ammonia Gas in Air",
    description="Demonstrating gas diffusion using concentrated ammonia solution and moist litmus paper — litmus paper changes colour as ammonia diffuses through air.",
    experiment_id=10,
)
add_video_ref_block(
    L163,
    title="Laboratory Experiment: Rate of Diffusion — Ammonia and Hydrogen Chloride Gases",
    description="NH3 and HCl diffuse from opposite ends of a glass tube and meet to form a white ring of ammonium chloride, confirming that lighter gases diffuse faster.",
    experiment_id=5,
)
add_video_ref_block(
    L163,
    title="Laboratory Experiment: Do All Gases Diffuse at the Same Rate?",
    description="A side-by-side comparison illustrating Graham's Law — ammonia (lighter) travels further than hydrogen chloride (heavier) in the same time.",
    experiment_id=62,
)
add_video_ref_block(
    L163,
    title="Video Demonstration: Rate of Diffusion",
    description="Video demonstration exploring the rate of diffusion of gases under controlled conditions.",
    youtube_url="https://www.youtube.com/watch?v=lWZXskMza-Q",
)
add_simulation_block(
    L163,
    title="Interactive Simulation: Graham's Law of Diffusion",
    description="Release two gases from opposite ends of a tube. Choose different molar masses and watch the lighter gas travel further — the rate ratio matches the sqrt(MB/MA) formula exactly.",
    archetype="grahams_law_diffusion",
)


# ── TOPIC 2: THE MOLE ────────────────────────────────────────────────────────

print("\n=== Lesson 166: Empirical and Molecular Formulae ===")
add_video_ref_block(
    L166,
    title="Laboratory Experiment: Determining the Empirical Formula of Magnesium Oxide",
    description="Crucible combustion of magnesium ribbon, periodic lid venting, and gravimetric calculations to determine the empirical formula MgO.",
    experiment_id=7,
)

print("\n=== Lesson 167: Concentration of Solutions and Molar Solutions ===")
add_video_ref_block(
    L167,
    title="Laboratory Experiment: Preparing a Standard Molar Solution of NaOH",
    description="Accurate weighing of NaOH, dissolving in distilled water, and making up to exact volume in a calibrated volumetric flask to prepare a known molar concentration.",
    experiment_id=11,
)
add_video_ref_block(
    L167,
    title="Laboratory Experiment: Preparing a Standard Molar Solution from a Liquid Acid",
    description="Carefully diluting concentrated hydrochloric acid to a known molarity — covering pipette technique, safety precautions, and volumetric flask use.",
    experiment_id=13,
)

print("\n=== Lesson 169: Stoichiometry of Chemical Equations ===")
add_video_ref_block(
    L169,
    title="Laboratory Experiment: Verification of Stoichiometric Relationships in a Chemical Reaction",
    description="Using experimental data to confirm mole ratios in a balanced equation — measuring reactants and products to verify the stoichiometry of the reaction.",
    experiment_id=8,
)

print("\n=== Lesson 170: Volumetric Analysis (Acid-Base Titrations) ===")
add_video_ref_block(
    L170,
    title="Laboratory Experiment: Direct Titration of an Acid and a Base",
    description="Standard volumetric analysis technique: pipette handling, burette titration, and phenolphthalein/methyl orange endpoint determination.",
    experiment_id=9,
)
add_video_ref_block(
    L170,
    title="Laboratory Experiment: Titration of a Dibasic Acid with a Base (H2SO4 vs NaOH)",
    description="Titrating sulphuric acid against a standard sodium hydroxide solution — covers two-stage neutralisation and calculation of exact concentration.",
    experiment_id=6,
)
add_video_ref_block(
    L170,
    title="Video Resource: Acid-Base Titration Technique",
    description="Detailed walkthrough of standard acid-base titration — burette setup, endpoint colour change, and concentration calculations.",
    youtube_url="https://www.youtube.com/watch?v=sFpFCPTDv2w",
)

print("\n=== Lesson 171: Back Titrations ===")
add_video_ref_block(
    L171,
    title="Laboratory Experiment: Back Titration",
    description="Determining the amount of a substance (often insoluble or slow-reacting) by adding excess reagent and back-titrating the unreacted excess.",
    experiment_id=12,
)

print("\n=== ALL DONE ===")
for lid, name in [
    (159, 'Introduction'), (160, "Boyle's Law"), (161, "Charles's Law"),
    (162, 'Combined Gas Law'), (163, "Graham's Law"),
    (166, 'Empirical Formulae'), (167, 'Molar Solutions'),
    (169, 'Stoichiometry'), (170, 'Titrations'), (171, 'Back Titrations'),
]:
    lesson = Lesson.objects.get(id=lid)
    vids = LessonBlock.objects.filter(lesson=lesson, block_type='video_ref').count()
    sims = LessonBlock.objects.filter(lesson=lesson, block_type='suggested_simulation').count()
    print(f"  Lesson {lid} ({name}): {vids} video_ref, {sims} simulation blocks")
