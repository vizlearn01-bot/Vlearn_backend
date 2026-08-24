import os, sys, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Applying pristine formatting to Graham's Law Blocks...")

# Block 5779 (Worked Example 2)
b5779 = LessonBlock.objects.get(id=5779)
b5779.content['text'] = (
    "\n\n> 🎬 **Comparing Diffusion Rates of Gases**: Watch these two laboratory demonstrations below comparing the diffusion speeds of different gases side-by-side to verify how molecular mass directly controls diffusion rate!"
)
b5779.content['steps'] = [
    "**Determine Molecular Masses**:\n- $M(\\text{NH}_3) = 14.0 + 3(1.0) = 17.0\\text{ g mol}^{-1}$\n- $M(\\text{HCl}) = 1.0 + 35.5 = 36.5\\text{ g mol}^{-1}$",
    "**Apply Graham's Law Ratio**:\n\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\sqrt{\\frac{M_{\\text{HCl}}}{M_{\\text{NH}_3}}} = \\sqrt{\\frac{36.5}{17.0}}$$",
    "**Calculate Ratio**:\n\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\sqrt{2.147} \\approx 1.465$$",
    "**Scientific Interpretation**: Ammonia gas diffuses approximately **$1.47\\text{ times faster}$** than hydrogen chloride gas under identical conditions."
]
b5779.save()
print("Updated Block 5779")

# Block 5780 (Misconception)
b5780 = LessonBlock.objects.get(id=5780)
b5780.content['text'] = (
    "### Does a gas with twice the mass take twice as long to diffuse?\n\n"
    "No! Diffusion rates depend on the **square root** of the molecular mass ($\\sqrt{M_r}$), not a direct linear ratio.\n\n"
    "If gas $A$ has 4 times the mass of gas $B$, it diffuses $\\sqrt{4} = 2\\text{ times slower}$ (taking twice as long), not 4 times slower!"
)
b5780.save()
print("Updated Block 5780")

# Block 5783 (Summary)
b5783 = LessonBlock.objects.get(id=5783)
b5783.content['text'] = (
    "### Core Principles: Graham's Law\n"
    "- **Statement**: Rate of diffusion is inversely proportional to square root of density or molecular mass ($R \\propto \\frac{1}{\\sqrt{M_r}}$).\n"
    "- **Rate Equation**:\n\n$$\\frac{R_A}{R_B} = \\sqrt{\\frac{M_B}{M_A}}$$\n\n"
    "- **Time Equation**:\n\n$$\\frac{t_B}{t_A} = \\sqrt{\\frac{M_B}{M_A}}$$\n\n"
    "- **Experimental Proof**: White $\\text{NH}_4\\text{Cl}$ ring in $\\text{NH}_3\\text{--}\\text{HCl}$ tube forms closer to the heavier $\\text{HCl}$ end."
)
b5783.save()
print("Updated Block 5783")

print("SUCCESS: Lesson 163 blocks updated cleanly!")
