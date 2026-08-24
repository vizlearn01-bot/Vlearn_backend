#!/usr/bin/env python
"""
add_transition_statements.py
Adds clear, engaging descriptive statements before interactive simulations and laboratory experiment videos.
"""
import sys, os, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

def append_to_block_text(block_id, callout_text):
    b = LessonBlock.objects.filter(id=block_id).first()
    if not b or not b.content:
        print(f"  [!] Block #{block_id} not found or has no content.")
        return
    content = b.content
    text_key = 'text' if 'text' in content else 'content' if 'content' in content else 'body'
    current_text = content.get(text_key, '')
    
    # Avoid duplicate appending
    clean_callout_snippet = callout_text.strip()[:40]
    if clean_callout_snippet in current_text:
        print(f"  [SKIP] Block #{block_id} already has transition callout.")
        return
    
    content[text_key] = current_text.rstrip() + "\n\n" + callout_text.strip()
    b.content = content
    b.save()
    print(f"  [+] Appended transition callout to Block #{block_id} (Lesson {b.lesson_id})")

# ---------------------------------------------------------------------------
# 1. Transitions BEFORE Simulations (End of Card 2 Core Concept)
# ---------------------------------------------------------------------------
print("=== 1. Adding Transitions Before Simulations ===")

# Lesson 160 (Boyle's Law, Card 2, Block #5740)
append_to_block_text(
    5740,
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, open the interactive gas syringe simulation! Drag the plunger to compress the trapped gas, observe particle collisions in real time, and watch the pressure–volume isotherm curve update live."
)

# Lesson 161 (Charles's Law, Card 2, Block #5753)
append_to_block_text(
    5753,
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, launch the interactive thermal chamber simulation! Heat or cool the trapped gas with the Bunsen flame or ice bath, and watch the piston expand and contract live."
)

# Lesson 163 (Graham's Law, Card 2, Block #5777)
append_to_block_text(
    5777,
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, launch the interactive diffusion tube simulation! Select different gases to race against ammonia ($\\text{NH}_3$) and watch the white ammonium chloride precipitation ring form in real time."
)

# ---------------------------------------------------------------------------
# 2. Transitions BEFORE Laboratory Videos (End of Card 5/6 Misconceptions)
# ---------------------------------------------------------------------------
print("\n=== 2. Adding Transitions Before Lab Videos & Experiments ===")

# Lesson 160 (Boyle's Law, Card 6, Block #5745)
append_to_block_text(
    5745,
    "> 🎬 **Laboratory Demonstration**: Watch the recorded practical demonstration below to see Boyle's Law verified using a real-world gas syringe and digital pressure sensor before tackling the practice questions!"
)

# Lesson 161 (Charles's Law, Card 6, Block #5757)
append_to_block_text(
    5757,
    "> 🎬 **Laboratory & Practical Demonstrations**: Watch the laboratory experiment video and real-world demonstration below showing Charles's Law in action—from laboratory thermal expansion tubes to hot-air balloon inflation!"
)

# Lesson 163 (Graham's Law, Card 5, Block #5780)
append_to_block_text(
    5780,
    "> 🎬 **Laboratory Experiment Suite**: Behold! Watch the recorded laboratory experiments below demonstrating diffusion in liquids and gases, including the classic $\\text{NH}_3$ and $\\text{HCl}$ diffusion tube experiment, before testing your knowledge!"
)

# Lesson 166 (Empirical Formulae, Card 6, Block #5458)
append_to_block_text(
    5458,
    "> 🎬 **Laboratory Experiment Video**: Watch the laboratory practical video below demonstrating the crucible combustion of magnesium ribbon to determine the empirical formula of magnesium oxide!"
)

# Lesson 167 (Molar Solutions, Card 6, Block #5467)
append_to_block_text(
    5467,
    "> 🎬 **Laboratory Practical Suite**: Watch the step-by-step laboratory experiment videos below demonstrating the preparation of standard molar solutions from solid sodium hydroxide and liquid hydrochloric acid!"
)

# Lesson 169 (Stoichiometry, Card 6, Block #5485)
append_to_block_text(
    5485,
    "> 🎬 **Laboratory Experiment Video**: Watch the recorded laboratory experiment below verifying stoichiometric reacting mass and gas volume relationships in chemical reactions!"
)

# Lesson 170 (Titrations, Card 6, Block #5494)
append_to_block_text(
    5494,
    "> 🎬 **Laboratory Practical Suite**: Behold! Watch the laboratory titration videos below demonstrating direct acid-base volumetric analysis and dibasic acid ($\\text{H}_2\\text{SO}_4\\text{ vs }\\text{NaOH}$) standardisation techniques!"
)

# Lesson 171 (Back Titrations, Card 6, Block #5503)
append_to_block_text(
    5503,
    "> 🎬 **Laboratory Experiment Video**: Watch the recorded practical video below demonstrating the two-stage back titration method for analyzing insoluble carbonates!"
)

print("\n✅ All transition statements added successfully.")
