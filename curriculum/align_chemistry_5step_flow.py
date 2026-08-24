import os, sys, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

print("Applying 5-Step Chemistry Pedagogical Flow...")

# ─────────────────────────────────────────────────────────────────────────────
# 1. Lesson 161: Charles's Law
# 1. Concept Intro -> 2. Recorded Lab -> 3. Content & Theory -> 4. Sim & Worked Examples -> 5. Real World App (Text + Video) -> 6. Think About This -> 7. Questions -> 8. Summary
# ─────────────────────────────────────────────────────────────────────────────
les161 = Lesson.objects.get(id=161)

# Page 1: Concept Introduction
b5749 = LessonBlock.objects.get(id=5749) # learning_goal
b5749.page_number = 1; b5749.order = 1; b5749.save()
b5750 = LessonBlock.objects.get(id=5750) # concept_explanation (Ping Pong ball)
b5750.page_number = 1; b5750.order = 2
b5750.content['text'] = (
    "If a table tennis (ping-pong) ball is accidentally dented during a fast game, you don't need to throw it away. "
    "Dropping the dented ball into a cup of hot water makes it instantly pop back to its original spherical shape!\n\n"
    "Why does this happen? The air trapped inside the ball heats up, and as its temperature rises, the gas expands, pushing the plastic surface back outward.\n\n"
    "This everyday phenomenon is governed by **Charles's Law**. On the next card, watch a laboratory recording demonstrating this temperature-volume relationship in action!"
)
b5750.save()

# Page 2: Recorded Experiment
b28243 = LessonBlock.objects.get(id=28243) # video_ref (Charles's Law Lab)
b28243.page_number = 2; b28243.order = 3; b28243.save()

# Page 3: Content & Theory
b28260 = LessonBlock.objects.get(id=28260) # definition_card
b28260.page_number = 3; b28260.order = 4; b28260.save()
b5751 = LessonBlock.objects.get(id=5751) # concept_explanation (Absolute Zero & Kelvin)
b5751.page_number = 3; b5751.order = 5; b5751.save()
b5753 = LessonBlock.objects.get(id=5753) # concept_explanation (Statement & Formula)
b5753.page_number = 3; b5753.order = 6
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
b5752 = LessonBlock.objects.get(id=5752) # suggested_diagram (V-T Graph)
b5752.page_number = 3; b5752.order = 7; b5752.save()

# Page 4: Interactive Simulation & Worked Examples
b28244 = LessonBlock.objects.get(id=28244) # suggested_simulation
b28244.page_number = 4; b28244.order = 8; b28244.save()
b5755 = LessonBlock.objects.get(id=5755) # worked_example 1
b5755.page_number = 4; b5755.order = 9; b5755.save()
b5756 = LessonBlock.objects.get(id=5756) # worked_example 2
b5756.page_number = 4; b5756.order = 10; b5756.save()

# Page 5: Real-World Application (Explanation FIRST, then Video directly after)
b5754 = LessonBlock.objects.get(id=5754) # real_world_example (Hot air balloon text)
b5754.page_number = 5; b5754.order = 11
b5754.content['text'] = (
    "### Tourism Flights Over the Masai Mara\n"
    "Every morning at sunrise in the **Masai Mara National Reserve**, giant hot-air balloons carry tourists high above roaming herds of wildebeest and zebras.\n\n"
    "The pilot ignites powerful propane burners at the mouth of the balloon envelope. As the trapped air heats up, it expands according to Charles's Law ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$). Because the envelope has an open mouth at the bottom, excess expanding air spills out.\n\n"
    "The remaining heated air inside has fewer particles per unit volume, making it **less dense than the surrounding cold morning air**. This density difference generates a buoyant upward lift, carrying the balloon gracefully into the sky."
)
b5754.save()
b28245 = LessonBlock.objects.get(id=28245) # video_ref (Hot air balloon video)
b28245.page_number = 5; b28245.order = 12; b28245.save()

# Page 6: Think About This & Misconceptions
b5757 = LessonBlock.objects.get(id=5757) # common_misconception
b5757.page_number = 6; b5757.order = 13; b5757.save()

# Page 7: Questions
b5758 = LessonBlock.objects.get(id=5758) # knowledge_check 1
b5758.page_number = 7; b5758.order = 14; b5758.save()
b5759 = LessonBlock.objects.get(id=5759) # knowledge_check 2
b5759.page_number = 7; b5759.order = 15; b5759.save()

# Page 8: Summary
b5760 = LessonBlock.objects.get(id=5760) # summary
b5760.page_number = 8; b5760.order = 16; b5760.save()

print("Aligned Lesson 161 (Charles's Law)")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Lesson 160: Boyle's Law
# ─────────────────────────────────────────────────────────────────────────────
les160 = Lesson.objects.get(id=160)

# Page 1: Concept Intro
b5738 = LessonBlock.objects.get(id=5738); b5738.page_number = 1; b5738.order = 1; b5738.save()
b5739 = LessonBlock.objects.get(id=5739); b5739.page_number = 1; b5739.order = 2
b5739.content['text'] = (
    "When you block the nozzle of a bicycle pump with your thumb and push the plunger down, you feel an increasing resistance. "
    "The more you compress the trapped air into a smaller volume, the harder it pushes back.\n\n"
    "This fundamental pressure-volume behavior is described by **Boyle's Law**. On the next card, watch the laboratory experiment recording verifying this relationship!"
)
b5739.save()

# Page 2: Recorded Experiment
b28242 = LessonBlock.objects.get(id=28242) # video_ref (Boyle's Law Lab)
b28242.page_number = 2; b28242.order = 3; b28242.save()

# Page 3: Content & Theory
b28259 = LessonBlock.objects.get(id=28259); b28259.page_number = 3; b28259.order = 4; b28259.save()
b5740 = LessonBlock.objects.get(id=5740); b5740.page_number = 3; b5740.order = 5
b5740.content['text'] = (
    "### Boyle's Law Statement:\n"
    "**The volume of a fixed mass of gas is inversely proportional to its pressure, provided the temperature remains constant.**\n\n"
    "### Mathematical Formulation:\n\n"
    "$$P \\propto \\frac{1}{V} \\quad \\implies \\quad P \\times V = k \\quad (\\text{constant})$$\n\n"
    "For a gas changing from state 1 ($P_1, V_1$) to state 2 ($P_2, V_2$) at constant temperature:\n\n"
    "$$P_1 V_1 = P_2 V_2$$\n\n"
    "> 🔬 **Interactive Virtual Lab Ahead**: On the next card, test this pressure-volume relationship with the interactive syringe simulator!"
)
b5740.save()
b5741 = LessonBlock.objects.get(id=5741); b5741.page_number = 3; b5741.order = 6; b5741.save()

# Page 4: Interactive Simulation & Worked Examples
b28241 = LessonBlock.objects.get(id=28241); b28241.page_number = 4; b28241.order = 7; b28241.save()
b5743 = LessonBlock.objects.get(id=5743); b5743.page_number = 4; b5743.order = 8; b5743.save()
b5744 = LessonBlock.objects.get(id=5744); b5744.page_number = 4; b5744.order = 9; b5744.save()

# Page 5: Real-World Application
b5742 = LessonBlock.objects.get(id=5742); b5742.page_number = 5; b5742.order = 10; b5742.save()

# Page 6: Think About This & Misconceptions
b5745 = LessonBlock.objects.get(id=5745); b5745.page_number = 6; b5745.order = 11; b5745.save()

# Page 7: Questions
b5746 = LessonBlock.objects.get(id=5746); b5746.page_number = 7; b5746.order = 12; b5746.save()
b5747 = LessonBlock.objects.get(id=5747); b5747.page_number = 7; b5747.order = 13; b5747.save()

# Page 8: Summary
b5748 = LessonBlock.objects.get(id=5748); b5748.page_number = 8; b5748.order = 14; b5748.save()

print("Aligned Lesson 160 (Boyle's Law)")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Lesson 163: Graham's Law
# ─────────────────────────────────────────────────────────────────────────────
les163 = Lesson.objects.get(id=163)

# Page 1: Concept Intro
b5773 = LessonBlock.objects.get(id=5773); b5773.page_number = 1; b5773.order = 1; b5773.save()
b5774 = LessonBlock.objects.get(id=5774); b5774.page_number = 1; b5774.order = 2
b5774.content['text'] = (
    "When a barista in a cafe on **Kenyatta Avenue in Nairobi** grinds fresh roasted coffee beans, the rich aroma reaches customers seated across the room within seconds.\n\n"
    "This spontaneous spreading of particles from high to low concentration is called **Diffusion**.\n\n"
    "On the next card, watch the classic laboratory experiment demonstrating how ammonia and hydrogen chloride gases diffuse toward each other inside a sealed glass tube!"
)
b5774.save()
b28246 = LessonBlock.objects.get(id=28246); b28246.page_number = 1; b28246.order = 3; b28246.save()
b28247 = LessonBlock.objects.get(id=28247); b28247.page_number = 1; b28247.order = 4; b28247.save()

# Page 2: Recorded Experiment (The NH3 + HCl Tube Lab)
b28248 = LessonBlock.objects.get(id=28248); b28248.page_number = 2; b28248.order = 5; b28248.save()
b5776 = LessonBlock.objects.get(id=5776); b5776.page_number = 2; b5776.order = 6; b5776.save()
b5777 = LessonBlock.objects.get(id=5777); b5777.page_number = 2; b5777.order = 7; b5777.save()

# Page 3: Content & Theory
b28261 = LessonBlock.objects.get(id=28261); b28261.page_number = 3; b28261.order = 8; b28261.save()
b5775 = LessonBlock.objects.get(id=5775); b5775.page_number = 3; b5775.order = 9; b5775.save()

# Page 4: Interactive Simulation & Worked Examples
b28251 = LessonBlock.objects.get(id=28251); b28251.page_number = 4; b28251.order = 10; b28251.save()
b5778 = LessonBlock.objects.get(id=5778); b5778.page_number = 4; b5778.order = 11; b5778.save()
b5779 = LessonBlock.objects.get(id=5779); b5779.page_number = 4; b5779.order = 12; b5779.save()

# Page 5: Real-World Applications & Rate Comparisons
b28249 = LessonBlock.objects.get(id=28249); b28249.page_number = 5; b28249.order = 13; b28249.save()
b28250 = LessonBlock.objects.get(id=28250); b28250.page_number = 5; b28250.order = 14; b28250.save()

# Page 6: Think About This & Misconceptions
b5780 = LessonBlock.objects.get(id=5780); b5780.page_number = 6; b5780.order = 15; b5780.save()

# Page 7: Questions
b5781 = LessonBlock.objects.get(id=5781); b5781.page_number = 7; b5781.order = 16; b5781.save()
b5782 = LessonBlock.objects.get(id=5782); b5782.page_number = 7; b5782.order = 17; b5782.save()

# Page 8: Summary
b5783 = LessonBlock.objects.get(id=5783); b5783.page_number = 8; b5783.order = 18; b5783.save()

print("Aligned Lesson 163 (Graham's Law)")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Lessons 164–172: Move Recorded Experiments to Page 2
# ─────────────────────────────────────────────────────────────────────────────
# Lesson 164 (The Mole Concept)
b25805 = LessonBlock.objects.get(id=25805); b25805.page_number = 2; b25805.order = 3; b25805.save()
b5444 = LessonBlock.objects.get(id=5444); b5444.page_number = 2; b5444.order = 4; b5444.save()
b25661 = LessonBlock.objects.get(id=25661); b25661.page_number = 2; b25661.order = 5; b25661.save()

# Lesson 166 (Empirical Formulas)
b25807 = LessonBlock.objects.get(id=25807); b25807.page_number = 2; b25807.order = 3; b25807.save()
b5453 = LessonBlock.objects.get(id=5453); b5453.page_number = 2; b5453.order = 4; b5453.save()
b5454 = LessonBlock.objects.get(id=5454); b5454.page_number = 2; b5454.order = 5; b5454.save()

# Lesson 167 (Molar Solutions)
b28252 = LessonBlock.objects.get(id=28252); b28252.page_number = 2; b28252.order = 3; b28252.save()
b28253 = LessonBlock.objects.get(id=28253); b28253.page_number = 2; b28253.order = 4; b28253.save()
b5463 = LessonBlock.objects.get(id=5463); b5463.page_number = 2; b5463.order = 5; b5463.save()
b25662 = LessonBlock.objects.get(id=25662); b25662.page_number = 2; b25662.order = 6; b25662.save()

# Lesson 169 (Stoichiometry)
b28254 = LessonBlock.objects.get(id=28254); b28254.page_number = 2; b28254.order = 3; b28254.save()
b5481 = LessonBlock.objects.get(id=5481); b5481.page_number = 2; b5481.order = 4; b5481.save()
b25664 = LessonBlock.objects.get(id=25664); b25664.page_number = 2; b25664.order = 5; b25664.save()

# Lesson 170 (Acid-Base Titrations)
b25808 = LessonBlock.objects.get(id=25808); b25808.page_number = 2; b25808.order = 3; b25808.save()
b28255 = LessonBlock.objects.get(id=28255); b28255.page_number = 2; b28255.order = 4; b28255.save()
b28256 = LessonBlock.objects.get(id=28256); b28256.page_number = 2; b28256.order = 5; b28256.save()
b5490 = LessonBlock.objects.get(id=5490); b5490.page_number = 2; b5490.order = 6; b5490.save()
b25665 = LessonBlock.objects.get(id=25665); b25665.page_number = 2; b25665.order = 7; b25665.save()

# Lesson 171 (Back Titrations)
b28257 = LessonBlock.objects.get(id=28257); b28257.page_number = 2; b28257.order = 3; b28257.save()
b5499 = LessonBlock.objects.get(id=5499); b5499.page_number = 2; b5499.order = 4; b5499.save()
b25666 = LessonBlock.objects.get(id=25666); b25666.page_number = 2; b25666.order = 5; b25666.save()

print("SUCCESS: Full 5-Step pedagogical structure applied across all Chemistry modules!")
