import os, sys, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Applying pristine formatting to Charles's Law Blocks...")

# Block 5755 (Worked Example 1)
b5755 = LessonBlock.objects.get(id=5755)
b5755.content['steps'] = [
    "**Convert Temperatures to Kelvin**:\n- $T_1 = 27^\\circ\\text{C} + 273 = 300\\text{ K}$\n- $T_2 = 127^\\circ\\text{C} + 273 = 400\\text{ K}$",
    "**Identify Volumes**: $V_1 = 450\\text{ cm}^3$, $V_2 = ?$",
    "**State the Formula**:\n\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$",
    "**Substitute Values**:\n\n$$\\frac{450\\text{ cm}^3}{300\\text{ K}} = \\frac{V_2}{400\\text{ K}}$$",
    "**Solve for $V_2$**:\n\n$$1.5 = \\frac{V_2}{400} \\implies V_2 = 1.5 \\times 400 = 600\\text{ cm}^3$$",
    "**Scientific Reflection**: The absolute temperature increased from $300\\text{ K}$ to $400\\text{ K}$ (a factor of $1.33$), so the volume expanded from $450\\text{ cm}^3$ to $600\\text{ cm}^3$."
]
b5755.save()
print("Updated Block 5755")

# Block 5756 (Worked Example 2)
b5756 = LessonBlock.objects.get(id=5756)
b5756.content['steps'] = [
    "**Convert Initial Temperature**: $T_1 = 0^\\circ\\text{C} + 273 = 273\\text{ K}$.",
    "**Identify Given Values**: $V_1 = 200\\text{ cm}^3$, $V_2 = 400\\text{ cm}^3$.",
    "**State Formula**:\n\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$",
    "**Substitute Values**:\n\n$$\\frac{200}{273} = \\frac{400}{T_2} \\implies T_2 = \\frac{400 \\times 273}{200} = 2 \\times 273 = 546\\text{ K}$$",
    "**Convert Final Temperature to Celsius**:\n\n$$t_2 = 546 - 273 = 273^\\circ\\text{C}$$",
    "**Common Exam Trap**: Doubling the volume from $0^\\circ\\text{C}$ requires doubling the *Kelvin* temperature ($273\\text{ K} \\rightarrow 546\\text{ K}$), which corresponds to $273^\\circ\\text{C}$, NOT $0^\\circ\\text{C} \\times 2 = 0^\\circ\\text{C}$!"
]
b5756.save()
print("Updated Block 5756")

# Block 5759 (Knowledge Check)
b5759 = LessonBlock.objects.get(id=5759)
b5759.content['explanation'] = (
    "Convert temperatures to Kelvin: $T_1 = 20 + 273 = 293\\text{ K}$, $T_2 = -10 + 273 = 263\\text{ K}$. "
    "Using Charles's Law: $$\\frac{2.0}{293} = \\frac{V_2}{263} \\implies V_2 = \\frac{2.0 \\times 263}{293} \\approx 1.80\\text{ dm}^3$$"
)
b5759.save()
print("Updated Block 5759")

# Block 5760 (Summary)
b5760 = LessonBlock.objects.get(id=5760)
b5760.content['text'] = (
    "### Core Principles: Charles's Law\n"
    "- **Statement**: Volume is directly proportional to absolute Kelvin temperature at constant pressure ($V \\propto T$).\n"
    "- **Formula**: $$\\frac{V_1}{T_1} = \\frac{V_2}{T_2} = k$$\n"
    "- **Kelvin Conversion**: Always add 273 to Celsius ($T = t + 273$).\n"
    "- **Absolute Zero**: $0\\text{ K} = -273^\\circ\\text{C}$, the point of zero particle kinetic motion."
)
b5760.save()
print("Updated Block 5760")

print("SUCCESS: Charles Law Blocks 5755, 5756, 5759, 5760 updated!")
