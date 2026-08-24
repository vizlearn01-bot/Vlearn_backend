import os, sys, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

print("Reordering video blocks to appear at the start of explanations...")

# ─────────────────────────────────────────────────────────────────────────────
# 1. Lesson 163: Graham's Law
# ─────────────────────────────────────────────────────────────────────────────
les163 = Lesson.objects.get(id=163)

# Page 1: Videos first after learning goal
b5773 = LessonBlock.objects.get(id=5773) # learning_goal
b28246 = LessonBlock.objects.get(id=28246) # video_ref (Potassium Permanganate)
b28247 = LessonBlock.objects.get(id=28247) # video_ref (Ammonia Gas in Air)
b5774 = LessonBlock.objects.get(id=5774) # concept_explanation

b5773.order = 1
b5773.save()
b28246.order = 2
b28246.save()
b28247.order = 3
b28247.save()
b5774.order = 4
b5774.content['text'] = (
    "As demonstrated in the laboratory experiments above, when potassium permanganate dissolves in water or volatile ammonia vapors are released in air, particles spontaneously spread from an area of high concentration to an area of low concentration.\n\n"
    "This spontaneous spreading of particles without external stirring is called **Diffusion**.\n\n"
    "When a barista in a cafe on **Kenyatta Avenue in Nairobi** grinds fresh roasted coffee beans, the rich aroma reaches customers seated at the far end of the room within seconds through this exact process.\n\n"
    "But why do lighter gases diffuse noticeably faster than heavier gases? On the next pages, we explore the mathematical principles of **Graham's Law of Diffusion**."
)
b5774.save()

# Page 2: Experiment video at start, followed by diagram, observation breakdown, and formula
b28261 = LessonBlock.objects.get(id=28261) # definition_card
b28248 = LessonBlock.objects.get(id=28248) # video_ref (NH3 & HCl tube)
b5776 = LessonBlock.objects.get(id=5776) # suggested_diagram
b5777 = LessonBlock.objects.get(id=5777) # concept_explanation (Experiment Breakdown)
b5775 = LessonBlock.objects.get(id=5775) # concept_explanation (Mathematical Statement & Formula)

b28261.order = 5
b28261.save()
b28248.order = 6
b28248.save()
b5776.order = 7
b5776.save()
b5777.order = 8
b5777.content['text'] = (
    "As demonstrated in the laboratory experiment and apparatus diagram above, cotton wool soaked in concentrated ammonia solution ($NH_3$) is placed at one end of a long glass tube, and cotton wool soaked in concentrated hydrochloric acid ($HCl$) is placed at the opposite end.\n\n"
    "### Molecular Properties of the Gases:\n"
    "1. **Ammonia Gas ($NH_3$)**: Relative Molecular Mass $M_r = 14.0 + 3(1.0) = 17.0\\text{ g mol}^{-1}$.\n"
    "2. **Hydrogen Chloride Gas ($HCl$)**: Relative Molecular Mass $M_r = 1.0 + 35.5 = 36.5\\text{ g mol}^{-1}$.\n\n"
    "### Experimental Observation:\n"
    "After several minutes, a **dense white ring of solid ammonium chloride ($NH_4Cl$)** forms inside the tube:\n\n"
    "$$\\text{NH}_3(g) + \\text{HCl}(g) \\rightarrow \\text{NH}_4\\text{Cl}(s)$$\n\n"
    "### Scientific Analysis:\n"
    "Because ammonia molecules are significantly lighter ($M_r = 17.0$) than hydrogen chloride molecules ($M_r = 36.5$), they move with greater average speed (approximately $\\sqrt{36.5 / 17.0} \\approx 1.47\\text{ times faster}$). "
    "Consequently, the ammonia molecules travel a greater distance down the tube, meeting the slower HCl molecules **much closer to the $HCl$ end**."
)
b5777.save()

b5775.order = 9
b5775.content['text'] = (
    "### Graham's Law Statement:\n"
    "**Under identical conditions of temperature and pressure, the rate of diffusion ($R$) of a gas is inversely proportional to the square root of its density ($\\rho$) or relative molecular mass ($M_r$).**\n\n"
    "### Mathematical Formulation:\n\n"
    "$$R \\propto \\frac{1}{\\sqrt{\\rho}} \\quad \\text{and} \\quad R \\propto \\frac{1}{\\sqrt{M_r}}$$\n\n"
    "For two gases ($A$ and $B$) diffusing under identical conditions:\n\n"
    "$$\\frac{R_A}{R_B} = \\sqrt{\\frac{\\rho_B}{\\rho_A}} = \\sqrt{\\frac{M_B}{M_A}}$$\n\n"
    "### Time and Rate Inversion:\n"
    "Since rate is inversely proportional to time taken ($R = \\frac{V}{t}$ or $R \\propto \\frac{1}{t}$):\n\n"
    "$$\\frac{R_A}{R_B} = \\frac{t_B}{t_A} = \\sqrt{\\frac{M_B}{M_A}}$$\n\n"
    "*Note*: A lighter gas diffuses **faster** ($R_A > R_B$) and therefore takes **less time** ($t_A < t_B$) to travel the same distance.\n\n"
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, launch the interactive diffusion tube simulation to test different gas combinations and verify these ratios live!"
)
b5775.save()

# Page 4: Rate comparison videos at start, followed by worked examples
b28249 = LessonBlock.objects.get(id=28249) # video_ref (Do All Gases Diffuse...)
b28250 = LessonBlock.objects.get(id=28250) # video_ref (Rate of Diffusion)
b5778 = LessonBlock.objects.get(id=5778) # worked_example 1
b5779 = LessonBlock.objects.get(id=5779) # worked_example 2

b28249.order = 11
b28249.save()
b28250.order = 12
b28250.save()
b5778.order = 13
b5778.save()
b5779.order = 14
if 'text' in b5779.content:
    del b5779.content['text']
b5779.save()

print("Updated Lesson 163 (Graham's Law)")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Lesson 161: Charles's Law
# ─────────────────────────────────────────────────────────────────────────────
les161 = Lesson.objects.get(id=161)

# Page 4: Video demonstration first, then hot air balloon explanation
b28245 = LessonBlock.objects.get(id=28245) # video_ref (Hot air balloon)
b5754 = LessonBlock.objects.get(id=5754) # real_world_example

b28245.order = 8
b28245.save()
b5754.order = 9
b5754.content['text'] = (
    "### Tourism Flights Over the Masai Mara\n"
    "As demonstrated in the scientific video above, every morning at sunrise in the **Masai Mara National Reserve**, giant hot-air balloons carry tourists high above roaming herds of wildebeest and zebras.\n\n"
    "The pilot ignites powerful propane burners at the mouth of the balloon envelope. As the trapped air heats up, it expands according to Charles's Law ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$). Because the envelope has an open mouth at the bottom, excess expanding air spills out.\n\n"
    "The remaining heated air inside has fewer particles per unit volume, making it **less dense than the surrounding cold morning air**. This density difference generates a buoyant upward lift, carrying the balloon gracefully into the sky."
)
b5754.save()

# Page 6: Lab experiment video first, then misconception explanation
b28243 = LessonBlock.objects.get(id=28243) # video_ref (Charles Law Lab)
b5757 = LessonBlock.objects.get(id=5757) # common_misconception

b28243.order = 12
b28243.save()
b5757.order = 13
b5757.save()

print("Updated Lesson 161 (Charles's Law)")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Lesson 160: Boyle's Law
# ─────────────────────────────────────────────────────────────────────────────
b28242 = LessonBlock.objects.get(id=28242) # video_ref (Boyle's Law Lab)
b5745 = LessonBlock.objects.get(id=5745) # common_misconception

b28242.order = 10
b28242.save()
b5745.order = 11
b5745.save()

print("Updated Lesson 160 (Boyle's Law)")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Lessons 164 - 172: Move videos to top of their respective cards
# ─────────────────────────────────────────────────────────────────────────────
for les_id in [164, 165, 166, 167, 169, 170, 171]:
    les = Lesson.objects.get(id=les_id)
    page_blocks = list(les.blocks.filter(page_number=6).order_by('order'))
    if page_blocks:
        v_blocks = [b for b in page_blocks if b.block_type in ['video_ref', 'suggested_video']]
        non_v = [b for b in page_blocks if b.block_type not in ['video_ref', 'suggested_video']]
        
        # New order: videos first, then non-videos
        new_ordered = v_blocks + non_v
        start_order = min(b.order for b in page_blocks)
        for i, b in enumerate(new_ordered):
            b.order = start_order + i
            b.save()
        print(f"Updated Lesson {les_id} Page 6 block order")

print("SUCCESS: All video blocks repositioned to the start of explanations!")
