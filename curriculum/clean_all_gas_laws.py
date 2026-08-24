import os, sys, django, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("=== Fixing Lesson 163 (Graham's Law) blocks ===")

# Block 5780 (common_misconception)
b5780 = LessonBlock.objects.get(id=5780)
b5780.content = {
    "text": (
        "### Does a gas with twice the mass take twice as long to diffuse?\n"
        "No! Diffusion rates depend on the **square root** of the molecular mass ($\\sqrt{M_r}$), not a direct linear ratio.\n\n"
        "If Gas B has $4\\times$ the molar mass of Gas A, it diffuses $\\sqrt{4} = 2\\text{ times slower}$ (takes twice as long), not $4\\text{ times slower}$!\n\n"
        "### Does a higher rate mean more or less time?\n"
        "A faster rate means **less time** ($R \\propto \\frac{1}{t}$). Thus, the time ratio is inverted compared to the rate ratio:\n"
        "$$\\frac{t_B}{t_A} = \\frac{R_A}{R_B} = \\sqrt{\\frac{M_B}{M_A}}$$"
    )
}
b5780.save()
print("Fixed Block 5780 (Graham's Law Misconception)")

# Block 5778 (worked_example 1)
b5778 = LessonBlock.objects.get(id=5778)
b5778.content = {
    "problem": "A sample of $100\\text{ cm}^3$ of sulphur(IV) oxide gas ($\\text{SO}_2$) diffuses through a porous plug in $40\\text{ seconds}$. Under identical conditions, $100\\text{ cm}^3$ of an unknown gas $X$ takes $20\\text{ seconds}$ to diffuse through the same plug. Calculate the Relative Molecular Mass of gas $X$. ($S = 32.0, O = 16.0$)",
    "steps": [
        "**Calculate Molecular Mass of $\\text{SO}_2$**:\n\n$$M_r(\\text{SO}_2) = 32.0 + 2(16.0) = 64.0\\text{ g mol}^{-1}$$",
        "**Identify Given Times**:\n- Time for $\\text{SO}_2$: $t_{\\text{SO}_2} = 40\\text{ s}$\n- Time for gas $X$: $t_X = 20\\text{ s}$",
        "**State Graham's Law in terms of Time**:\n\n$$\\frac{t_X}{t_{\\text{SO}_2}} = \\sqrt{\\frac{M_X}{M_{\\text{SO}_2}}}$$",
        "**Substitute Values**:\n\n$$\\frac{20}{40} = \\sqrt{\\frac{M_X}{64.0}} \\implies 0.5 = \\sqrt{\\frac{M_X}{64.0}}$$",
        "**Square Both Sides and Solve**:\n\n$$(0.5)^2 = \\frac{M_X}{64.0} \\implies 0.25 = \\frac{M_X}{64.0}$$\n\n$$M_X = 0.25 \\times 64.0 = 16.0\\text{ g mol}^{-1}$$",
        "**Scientific Conclusion**: The relative molecular mass of unknown gas $X$ is $16.0$ (gas $X$ is methane, $\\text{CH}_4$)."
    ]
}
b5778.save()
print("Fixed Block 5778 (Graham's Law Worked Example 1)")

# Block 5779 (worked_example 2)
b5779 = LessonBlock.objects.get(id=5779)
b5779.content = {
    "problem": "Calculate the relative rate of diffusion of ammonia ($\\text{NH}_3$) compared to hydrogen chloride ($\\text{HCl}$). ($N = 14.0, H = 1.0, \\text{Cl} = 35.5$)",
    "steps": [
        "**Determine Molecular Masses**:\n- $M(\\text{NH}_3) = 14.0 + 3(1.0) = 17.0\\text{ g mol}^{-1}$\n- $M(\\text{HCl}) = 1.0 + 35.5 = 36.5\\text{ g mol}^{-1}$",
        "**Apply Graham's Law Ratio**:\n\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\sqrt{\\frac{M_{\\text{HCl}}}{M_{\\text{NH}_3}}} = \\sqrt{\\frac{36.5}{17.0}}$$",
        "**Calculate Ratio**:\n\n$$\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\sqrt{2.147} \\approx 1.465$$",
        "**Scientific Interpretation**: Ammonia gas diffuses approximately **$1.47\\text{ times faster}$** than hydrogen chloride gas under identical conditions."
    ]
}
b5779.save()
print("Fixed Block 5779 (Graham's Law Worked Example 2)")

# Block 5783 (summary)
b5783 = LessonBlock.objects.get(id=5783)
b5783.content = {
    "text": (
        "### Core Principles: Graham's Law\n"
        "- **Statement**: Rate of diffusion is inversely proportional to square root of density or molecular mass ($R \\propto \\frac{1}{\\sqrt{M_r}}$).\n"
        "- **Rate Equation**:\n\n$$\\frac{R_A}{R_B} = \\sqrt{\\frac{M_B}{M_A}}$$\n\n"
        "- **Time Equation**:\n\n$$\\frac{t_B}{t_A} = \\sqrt{\\frac{M_B}{M_A}}$$\n\n"
        "- **Experimental Proof**: White $\\text{NH}_4\\text{Cl}$ ring in $\\text{NH}_3\\text{--}\\text{HCl}$ tube forms closer to the heavier $\\text{HCl}$ end."
    )
}
b5783.save()
print("Fixed Block 5783 (Graham's Law Summary)")

print("\n=== Auditing all blocks across Lessons 159, 160, 161, 162, 163 ===")
for lid in [159, 160, 161, 162, 163]:
    for b in LessonBlock.objects.filter(lesson_id=lid).order_by('page_number', 'order'):
        raw = json.dumps(b.content)
        # Check for unescaped \times, \frac, control chars, or unbalanced $
        count_dollar = raw.count('$')
        if count_dollar % 2 != 0:
            print(f"  [UNBALANCED $] Lesson {lid} Block {b.id} ({b.block_type}) Page {b.page_number}: {b.title}")
        if '594466' in raw:
            print(f"  [594466 DETECTED] Lesson {lid} Block {b.id} ({b.block_type}) Page {b.page_number}: {b.title}")

print("\nFinished cleaning and auditing Gas Laws modules.")
