import os, sys, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("Moving Absolute Zero & Kelvin Scale to Card 6 (after Charles's Law is fully covered)...")

# Page 1: Concept Intro
b5749 = LessonBlock.objects.get(id=5749); b5749.page_number = 1; b5749.order = 1; b5749.save()
b5750 = LessonBlock.objects.get(id=5750); b5750.page_number = 1; b5750.order = 2; b5750.save()

# Page 2: Recorded Lab Experiment
b28243 = LessonBlock.objects.get(id=28243); b28243.page_number = 2; b28243.order = 3; b28243.save()

# Page 3: Charles's Law Theory & Equations (Directly after the lab!)
b28260 = LessonBlock.objects.get(id=28260); b28260.page_number = 3; b28260.order = 4; b28260.save()
b5753 = LessonBlock.objects.get(id=5753); b5753.page_number = 3; b5753.order = 5
b5753.content['text'] = (
    "### Charles's Law Statement:\n"
    "**The volume of a fixed mass of gas is directly proportional to its absolute temperature (in Kelvin), provided the pressure remains constant.**\n\n"
    "### Mathematical Formulation:\n\n"
    "$$V \\propto T \\quad (\\text{at constant } P)$$\n\n"
    "$$V = k \\times T \\implies \\frac{V}{T} = k \\quad (\\text{where } k \\text{ is a constant})$$\n\n"
    "For a gas sample changing from an initial state ($V_1, T_1$) to a final state ($V_2, T_2$) at constant pressure:\n\n"
    "$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$\n\n"
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, launch the interactive thermal chamber simulation to test these temperature-volume relationships live!"
)
b5753.save()

# Page 4: Interactive Simulation & Worked Calculations
b28244 = LessonBlock.objects.get(id=28244); b28244.page_number = 4; b28244.order = 6; b28244.save()
b5755 = LessonBlock.objects.get(id=5755); b5755.page_number = 4; b5755.order = 7; b5755.save()
b5756 = LessonBlock.objects.get(id=5756); b5756.page_number = 4; b5756.order = 8; b5756.save()

# Page 5: Real-World Application (Explanation + Video)
b5754 = LessonBlock.objects.get(id=5754); b5754.page_number = 5; b5754.order = 9; b5754.save()
b28245 = LessonBlock.objects.get(id=28245); b28245.page_number = 5; b28245.order = 10; b28245.save()

# Page 6: Absolute Zero, The Kelvin Scale & Misconceptions (After Charles's Law is covered)
b5751 = LessonBlock.objects.get(id=5751); b5751.page_number = 6; b5751.order = 11
b5751.content['text'] = (
    "### The Celsius vs. Kelvin Scale Discovery:\n"
    "If we measure the volume of a gas at different Celsius temperatures and plot volume $V$ against Celsius temperature $t$ ($^\\circ\\text{C}$), the straight line intercepts the temperature axis at exactly **$-273.15^\\circ\\text{C}$** when extrapolated to zero volume.\n\n"
    "This theoretical temperature where all molecular motion ceases and gas volume hypothetically becomes zero is called **Absolute Zero ($0\\text{ K}$)**.\n\n"
    "To make temperature directly proportional to gas volume, British physicist Lord Kelvin established the **Absolute Temperature Scale** in Kelvin ($\\text{K}$):\n\n"
    "$$T\\text{ (in Kelvin)} = t\\text{ (in }^\\circ\\text{C)} + 273$$\n\n"
    "### CRITICAL EXAM RULE:\n"
    "**You MUST ALWAYS convert temperatures to Kelvin ($T = t + 273$) before using any gas law equation! Calculating with Celsius yields completely incorrect answers.**"
)
b5751.save()

b5752 = LessonBlock.objects.get(id=5752); b5752.page_number = 6; b5752.order = 12; b5752.save()

b5757 = LessonBlock.objects.get(id=5757); b5757.page_number = 6; b5757.order = 13
b5757.content['text'] = (
    "### Why can't we use Celsius directly in Charles's Law calculations?\n"
    "The Celsius scale sets its zero at the arbitrary freezing point of water ($0^\\circ\\text{C}$), which is not the point of zero kinetic energy. If you calculated $\\frac{V_1}{0^\\circ\\text{C}}$, you would be dividing by zero, which is mathematically undefined!\n\n"
    "Only the Kelvin scale starts at true physical zero energy ($0\\text{ K}$), making $V$ directly proportional to $T$."
)
b5757.save()

# Page 7: Questions
b5758 = LessonBlock.objects.get(id=5758); b5758.page_number = 7; b5758.order = 14; b5758.save()
b5759 = LessonBlock.objects.get(id=5759); b5759.page_number = 7; b5759.order = 15; b5759.save()

# Page 8: Summary
b5760 = LessonBlock.objects.get(id=5760); b5760.page_number = 8; b5760.order = 16; b5760.save()

print("Successfully moved Absolute Zero & Kelvin Scale to Card 6!")
