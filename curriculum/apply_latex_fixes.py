import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Applying pristine LaTeX formatting across Gas Laws curriculum...")

# 1. Lesson 160 - Boyle's Law
b5740 = LessonBlock.objects.get(id=5740)
b5740.content['text'] = (
    "### Boyle's Law Statement:\n"
    "**The volume of a fixed mass of gas is inversely proportional to its pressure, provided the temperature remains constant.**\n\n"
    "### Mathematical Formulation:\n\n"
    "$$V \\propto \\frac{1}{P} \\quad (\\text{at constant } T)$$\n\n"
    "$$V = \\frac{k}{P} \\implies P \\times V = k \\quad (\\text{where } k \\text{ is a constant})$$\n\n"
    "For a gas sample changing from an initial state ($P_1, V_1$) to a final state ($P_2, V_2$) at constant temperature:\n\n"
    "$$P_1V_1 = P_2V_2$$\n\n"
    "### Pressure Units in Secondary Chemistry:\n"
    "- **Pascals ($\\text{Pa}$)**: $1\\text{ kPa} = 1000\\text{ Pa} = 1000\\text{ N m}^{-2}$\n"
    "- **Atmospheres ($\\text{atm}$)**: $1\\text{ atm} = 1.01325 \\times 10^5\\text{ Pa} = 101.325\\text{ kPa}$\n"
    "- **Millimetres of Mercury ($\\text{mmHg}$)**: $1\\text{ atm} = 760\\text{ mmHg}$\n\n"
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, open the interactive gas syringe simulation! Drag the plunger to compress the trapped gas, observe particle collisions in real time, and watch the pressure–volume isotherm curve update live."
)
b5740.save()
print("Updated Block 5740 (Boyle's Law Statement & Math)")

# 2. Lesson 161 - Charles's Law
b5753 = LessonBlock.objects.get(id=5753)
b5753.content['text'] = (
    "### Charles's Law Statement:\n"
    "**The volume of a fixed mass of gas is directly proportional to its absolute temperature (in Kelvin), provided the pressure remains constant.**\n\n"
    "### Mathematical Formulation:\n\n"
    "$$V \\propto T \\quad (\\text{at constant } P)$$\n\n"
    "$$V = k \\times T \\implies \\frac{V}{T} = k \\quad (\\text{where } k \\text{ is a constant})$$\n\n"
    "For a gas sample changing from an initial state ($V_1, T_1$) to a final state ($V_2, T_2$) at constant pressure:\n\n"
    "$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$\n\n"
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, launch the interactive thermal chamber simulation! Heat or cool the trapped gas with the Bunsen flame or ice bath, and watch the piston expand and contract live."
)
b5753.save()
print("Updated Block 5753 (Charles's Law Statement & Math)")

# 3. Lesson 162 - Combined Gas Law
b5763 = LessonBlock.objects.get(id=5763)
b5763.content['text'] = (
    "Boyle's and Charles's laws can be combined into one unified equation for a fixed mass of gas:\n\n"
    "* **Boyle's Law**: $V \\propto \\frac{1}{P}$ (at constant $T$)\n"
    "* **Charles's Law**: $V \\propto T$ (at constant $P$)\n\n"
    "Combining both relationships:\n\n"
    "$$V \\propto \\frac{T}{P} \\implies V = k \\frac{T}{P} \\implies \\frac{PV}{T} = k$$\n\n"
    "For a gas sample changing between two states ($P_1, V_1, T_1$) and ($P_2, V_2, T_2$):\n\n"
    "$$\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$$\n\n"
    "### Self-Consistency:\n"
    "- If temperature is constant ($T_1 = T_2$), the equation simplifies to $P_1V_1 = P_2V_2$ (Boyle's Law).\n"
    "- If pressure is constant ($P_1 = P_2$), the equation simplifies to $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$ (Charles's Law)."
)
b5763.save()
print("Updated Block 5763 (Combined Gas Law Statement & Math)")

# Clean Block 5767 & 5768 worked examples in Lesson 162
b5767 = LessonBlock.objects.get(id=5767)
b5767.content['steps'] = [
    "**Given Data**: $P_1 = 740\\text{ mmHg}$, $V_1 = 30\\text{ cm}^3$, $T_1 = 27 + 273 = 300\\text{ K}$.",
    "**Conditions at s.t.p.**: $P_2 = 760\\text{ mmHg}$, $T_2 = 273\\text{ K}$.",
    "**Formula**: $$\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$$",
    "**Substitution**: $$\\frac{740 \\times 30}{300} = \\frac{760 \\times V_2}{273}$$",
    "**Calculation**:\n\n$$\\frac{22,200}{300} = 74$$\n\n$$74 = \\frac{760 V_2}{273} \\implies V_2 = \\frac{74 \\times 273}{760} = \\frac{20,202}{760} \\approx 26.58\\text{ cm}^3$$",
    "**Scientific Meaning**: The volume of the nitrogen gas at s.t.p. is $26.58\\text{ cm}^3$ (or $26.6\\text{ cm}^3$)."
]
b5767.save()
print("Updated Block 5767 (Combined Gas Law Worked Example 1)")

b5768 = LessonBlock.objects.get(id=5768)
b5768.content['steps'] = [
    "**Given Data**: $V_1 = 100\\text{ cm}^3$, $T_1 = -15 + 273 = 258\\text{ K}$, $P_1 = 650\\text{ mmHg}$, $V_2 = 150\\text{ cm}^3$, $P_2 = 680\\text{ mmHg}$.",
    "**Formula**: $$\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$$",
    "**Substitution**: $$\\frac{650 \\times 100}{258} = \\frac{680 \\times 150}{T_2}$$",
    "**Calculation**:\n\n$$251.938 = \\frac{102,000}{T_2} \\implies T_2 = \\frac{102,000}{251.938} \\approx 404.86\\text{ K}$$",
    "**Convert to Celsius**: $$t_2 = 404.86 - 273 = 131.86^\\circ\\text{C}$$",
    "**Scientific Meaning**: The gas reaches $150\\text{ cm}^3$ at a temperature of $131.86^\\circ\\text{C}$."
]
b5768.save()
print("Updated Block 5768 (Combined Gas Law Worked Example 2)")

# 4. Lesson 163 - Graham's Law
b5775 = LessonBlock.objects.get(id=5775)
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
    "*Note*: A lighter gas diffuses **faster** ($R_A > R_B$) and therefore takes **less time** ($t_A < t_B$) to travel the same distance."
)
b5775.save()
print("Updated Block 5775 (Graham's Law Statement & Math)")

b5778 = LessonBlock.objects.get(id=5778)
b5778.content['steps'] = [
    "**Calculate Molecular Mass of $\\text{SO}_2$**:\n\n$$M_r(\\text{SO}_2) = 32.0 + 2(16.0) = 64.0\\text{ g mol}^{-1}$$",
    "**Identify Given Times**:\n- Time for $\\text{SO}_2$: $t_{\\text{SO}_2} = 40\\text{ s}$\n- Time for gas $X$: $t_X = 20\\text{ s}$",
    "**State Graham's Law in terms of Time**:\n\n$$\\frac{t_X}{t_{\\text{SO}_2}} = \\sqrt{\\frac{M_X}{M_{\\text{SO}_2}}}$$",
    "**Substitute Values**:\n\n$$\\frac{20}{40} = \\sqrt{\\frac{M_X}{64.0}} \\implies 0.5 = \\sqrt{\\frac{M_X}{64.0}}$$",
    "**Square Both Sides and Solve**:\n\n$$(0.5)^2 = \\frac{M_X}{64.0} \\implies 0.25 = \\frac{M_X}{64.0}$$\n\n$$M_X = 0.25 \\times 64.0 = 16.0\\text{ g mol}^{-1}$$",
    "**Scientific Conclusion**: The relative molecular mass of unknown gas $X$ is $16.0$ (gas $X$ is methane, $\\text{CH}_4$)."
]
b5778.save()
print("Updated Block 5778 (Graham's Law Worked Example)")

print("SUCCESS: All Gas Laws blocks updated with correct LaTeX!")
