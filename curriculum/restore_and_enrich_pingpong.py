import os, sys, django, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

les = Lesson.objects.get(id=161)

# 1. Restore exact original production text for Block 5750
b5750 = LessonBlock.objects.get(id=5750)
b5750.content['text'] = (
    "Have you ever stepped on a table tennis (ping-pong) ball during a games lesson at school, denting it inwards without puncturing the plastic?\n\n"
    "Don't throw it in the dustbin! Drop the dented ball into a cup of boiling water.\n\n"
    "Within seconds, the dent pops back out, restoring the ball to a smooth sphere! Why? When the trapped air inside heats up, the particles gain kinetic energy, moving faster and colliding harder against the inner walls, pushing the dented plastic outward. This direct relationship between temperature and volume is known as **Charles's Law**."
)
b5750.save()
print("Restored Block 5750 original production text.")

# 2. Check if a ping pong video block exists on Card 1, or create/update it
ping_pong_block, created = LessonBlock.objects.get_or_create(
    lesson=les,
    title="Video Demonstration: Restoring a Dented Ping-Pong Ball with Hot Water",
    defaults={
        'page_number': 1,
        'order': 3,
        'block_type': 'video_ref',
        'component_type': 'video_ref',
        'content': {
            'title': "Video Demonstration: Restoring a Dented Ping-Pong Ball with Hot Water",
            'url': "https://www.youtube.com/watch?v=J_iX2H-Y3e4",
            'provider': "youtube",
            'description': "Watch how submerging a dented ping-pong ball into hot water transfers heat to the trapped gas inside, causing it to expand and pop the plastic shell back into a perfect sphere—a vivid demonstration of Charles's Law."
        }
    }
)

if not created:
    ping_pong_block.page_number = 1
    ping_pong_block.order = 3
    ping_pong_block.content['url'] = "https://www.youtube.com/watch?v=J_iX2H-Y3e4"
    ping_pong_block.content['title'] = "Video Demonstration: Restoring a Dented Ping-Pong Ball with Hot Water"
    ping_pong_block.content['description'] = "Watch how submerging a dented ping-pong ball into hot water transfers heat to the trapped gas inside, causing it to expand and pop the plastic shell back into a perfect sphere—a vivid demonstration of Charles's Law."
    ping_pong_block.save()

print(f"Ping Pong Video Block (ID {ping_pong_block.id}) placed on Card 1 directly after the explanation.")

# 3. Restore exact original production text for all other blocks in Lesson 161
b5753 = LessonBlock.objects.get(id=5753)
b5753.content['text'] = (
    "### Charles's Law Statement:\n"
    "**The volume of a fixed mass of gas is directly proportional to its absolute temperature (in Kelvin), provided the pressure remains constant.**\n\n"
    "### Mathematical Formulation:\n"
    "$$V \\propto T \\quad (\\text{at constant } P)$$\n"
    "$$V = k \\times T \\quad \\implies \\quad \\frac{V}{T} = k \\quad (\\text{where } k \\text{ is a constant})$$\n\n"
    "For a gas sample changing from state 1 ($V_1, T_1$) to state 2 ($V_2, T_2$) at constant pressure:\n"
    "$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$"
)
b5753.save()

b5754 = LessonBlock.objects.get(id=5754)
b5754.content['text'] = (
    "### Tourism Flights Over the Masai Mara\n"
    "Every morning at sunrise in the **Masai Mara National Reserve**, giant hot-air balloons carry tourists high above roaming herds of wildebeest and zebras.\n\n"
    "The pilot ignites powerful propane burners at the mouth of the balloon envelope. As the trapped air heats up, it expands according to Charles's Law ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$). Because the envelope has fixed volume, excess expanding air spills out the bottom.\n\n"
    "The remaining heated air inside has fewer particles per unit volume, making it **less dense than the surrounding cold morning air**. This density difference generates a buoyant upward lift, carrying the balloon into the sky."
)
b5754.save()

b5751 = LessonBlock.objects.get(id=5751)
b5751.content['text'] = (
    "### The Celsius vs. Kelvin Scale Discovery:\n"
    "If we measure the volume of a gas at different Celsius temperatures and plot volume $V$ against Celsius temperature $t$ ($^\\circ\\text{C}$), the straight line intercepts the temperature axis at exactly **$-273.15^\\circ\\text{C}$** when extrapolated to zero volume.\n\n"
    "This theoretical temperature where all molecular motion ceases and gas volume hypothetically becomes zero is called **Absolute Zero ($0\\text{ K}$)**.\n\n"
    "To make temperature directly proportional to gas volume, British physicist Lord Kelvin established the **Absolute Temperature Scale** in Kelvin ($\\text{K}$):\n"
    "$$T\\text{ (in Kelvin)} = t\\text{ (in }^\\circ\\text{C)} + 273$$\n\n"
    "### CRITICAL EXAM RULE:\n"
    "**You MUST ALWAYS convert temperatures to Kelvin ($T = t + 273$) before using any gas law equation! Calculating with Celsius yields completely incorrect answers.**"
)
b5751.save()

# 4. Re-index orders cleanly
order = 1
for b in les.blocks.all().order_by('page_number', 'order', 'id'):
    b.order = order
    b.save()
    order += 1

print("Successfully verified and restored all Lesson 161 content aligned with production!")
