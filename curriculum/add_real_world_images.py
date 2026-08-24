import os, sys, django, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

print("=== Enriching Real-World & Industrial Applications with Wikimedia Images ===")

# 1. Graham's Law (Lesson 163, Block 28266)
b28266 = LessonBlock.objects.get(id=28266)
b28266.content = {
    "text": (
        "### Industrial & Biological Applications of Graham's Law\n\n"
        "Graham's Law is not just a laboratory concept; it plays a critical role in nuclear energy, underground mining safety, and human respiratory physiology:\n\n"
        "---\n\n"
        "#### 1. Nuclear Energy: Uranium Isotope Separation\n"
        "Naturally occurring uranium contains $99.3\\%$ Uranium-238 ($^{238}\\text{U}$) and only $0.7\\%$ fissile Uranium-235 ($^{235}\\text{U}$). To fuel nuclear power plants, the concentration of $^{235}\\text{U}$ must be enriched.\n\n"
        "![Uranium Hexafluoride Gaseous Diffusion Cascade Process](https://upload.wikimedia.org/wikipedia/commons/e/e8/Gaseous_diffusion_process.png)\n\n"
        "In the **gaseous diffusion process**, solid uranium is converted into volatile uranium hexafluoride gas ($\\text{UF}_6$):\n"
        "- $^{235}\\text{UF}_6$ has molecular mass $M_r = 235 + 6(19) = 349\\text{ g mol}^{-1}$\n"
        "- $^{238}\\text{UF}_6$ has molecular mass $M_r = 238 + 6(19) = 352\\text{ g mol}^{-1}$\n\n"
        "According to Graham's Law:\n"
        "$$\\frac{R(^{235}\\text{UF}_6)}{R(^{238}\\text{UF}_6)} = \\sqrt{\\frac{352}{349}} \\approx 1.0043$$\n\n"
        "The lighter $^{235}\\text{UF}_6$ diffuses $0.43\\%$ faster through porous nickel membranes. By passing the gas through thousands of successive diffusion stages (a diffusion cascade), enriched uranium is harvested!\n\n"
        "---\n\n"
        "#### 2. Underground Mine Safety: Marsh Gas (Methane) Detection\n"
        "In deep coal and mineral mines, dangerous pockets of **methane gas** ($\\text{CH}_4$, \"firedamp\") seep from rock seams.\n\n"
        "![Classic Miner Flame Safety Lamp for Methane Detection](https://upload.wikimedia.org/wikipedia/commons/3/38/Davy_lamp.png)\n\n"
        "- Methane has $M_r = 12 + 4(1) = 16\\text{ g mol}^{-1}$, making it substantially lighter than ambient air ($M_r \\approx 28.8\\text{ g mol}^{-1}$).\n"
        "- Because of its lower molecular mass, methane diffuses very rapidly upwards and accumulates along the roofs of mining shafts.\n"
        "- Mining safety equipment and early flame safety lamps take advantage of this differential diffusion to detect methane before it reaches explosive concentration thresholds ($5\\text{--}15\\%$ in air).\n\n"
        "---\n\n"
        "#### 3. Human Respiratory Gas Exchange in Alveoli\n"
        "In human lungs, oxygen ($\\text{O}_2, M_r = 32$) diffuses from microscopic alveoli air sacs across the respiratory membrane into red blood cells, while carbon(IV) oxide ($\\text{CO}_2, M_r = 44$) diffuses in the opposite direction to be exhaled.\n\n"
        "![Alveolar Gas Exchange Diagram](https://upload.wikimedia.org/wikipedia/commons/d/db/Alveoli_diagram.png)\n\n"
        "Graham's Law, along with Henry's Law of solubility, explains the exact physical rates at which oxygen and carbon dioxide diffuse through microscopic alveolar membranes to sustain human life."
    )
}
b28266.save()
print("Enriched Graham's Law Real-World Applications (Block 28266)")

# 2. Boyle's Law (Lesson 160, Block 5743)
b5743 = LessonBlock.objects.get(id=5743)
b5743.content = {
    "text": (
        "### Real-World Application: Scuba Diving & Decompression Physics\n\n"
        "For every $10\\text{ metres}$ a scuba diver descends into seawater, hydrostatic water pressure increases by approximately $1\\text{ atmosphere}$ ($101.3\\text{ kPa}$).\n\n"
        "![Scuba Diver Descending into Deep Water](https://upload.wikimedia.org/wikipedia/commons/e/e2/Scuba_Diver.jpg)\n\n"
        "- **At the Surface ($1\\text{ atm}$)**: A diver's lungs hold a normal volume of air $V$.\n"
        "- **At $10\\text{ m}$ Depth ($2\\text{ atm}$)**: According to Boyle's Law ($P_1V_1 = P_2V_2$), the gas in the diver's lungs is compressed to **half its surface volume** ($\frac{1}{2}V$).\n"
        "- **Ascending to the Surface**: If a diver ascends too rapidly while holding their breath, external pressure drops rapidly from $2\\text{ atm}$ back to $1\\text{ atm}$. The trapped air in the lungs **doubles in volume**, risking severe pulmonary barotrauma!\n\n"
        "> 💡 **Diver's Golden Rule**: Never hold your breath while scuba diving; continuously exhale during ascent to allow expanding gas to escape safely."
    )
}
b5743.save()
print("Enriched Boyle's Law Real-World Applications (Block 5743)")

# 3. Charles's Law (Lesson 161, Block 5754)
b5754 = LessonBlock.objects.get(id=5754)
b5754.content = {
    "text": (
        "### Real-World Application: Hot-Air Balloons & Thermal Buoyancy\n\n"
        "Hot-air balloons are the world's oldest successful flight technology, operating directly on the principles of **Charles's Law**.\n\n"
        "![Hot Air Balloon Safari](https://upload.wikimedia.org/wikipedia/commons/4/41/Hot_Air_Balloon_Safari_in_Maasai_Mara.jpg)\n\n"
        "1. Propane burners blast flames into the open mouth of the giant nylon envelope, heating the air inside to over $100^\\circ\\text{C}$ ($373\\text{ K}$).\n"
        "2. According to Charles's Law ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$), as temperature increases, the air expands. The excess air spills out of the bottom opening.\n"
        "3. Since the same envelope volume now contains fewer gas molecules, the **density of the hot air inside becomes significantly lower** than the cold ambient air outside ($\\rho = \\frac{m}{V}$).\n"
        "4. The surrounding denser atmosphere exerts an upward **buoyant force** (Archimedes' Principle) greater than the balloon's total weight, lifting passengers gracefully into the sky!"
    )
}
b5754.save()
print("Enriched Charles's Law Real-World Applications (Block 5754)")

# 4. Combined Gas Law (Lesson 162, Block 5766)
b5766 = LessonBlock.objects.get(id=5766)
b5766.content = {
    "text": (
        "### Real-World Application: High-Altitude Weather Balloons\n\n"
        "Meteorological services around the world launch thousands of **weather balloons** (radiosondes) daily to record atmospheric pressure, temperature, and humidity.\n\n"
        "![High-Altitude Weather Balloon Launch](https://upload.wikimedia.org/wikipedia/commons/8/84/PHOTO-IMETs-launch-weather-balloon-2023-IMET-training-2023.jpg)\n\n"
        "- **At Launch (Sea Level)**: The latex balloon is only partially inflated with helium gas ($V_1 \\approx 2\\text{ m}^3$) at $P_1 = 101.3\\text{ kPa}$ and $T_1 = 293\\text{ K}$ ($20^\\circ\\text{C}$).\n"
        "- **At Stratospheric Altitudes ($30\\text{ km}$)**: Ambient atmospheric pressure drops drastically to $P_2 \\approx 1\\text{ kPa}$, and temperature falls to $T_2 \\approx 220\\text{ K}$ ($-53^\\circ\\text{C}$).\n"
        "- **Applying the Combined Gas Law**:\n"
        "$$V_2 = V_1 \\times \\frac{P_1}{P_2} \\times \\frac{T_2}{T_1}$$\n"
        "- Although the dropping temperature slightly decreases volume, the **$100\\times$ drop in external pressure** dominates completely! The balloon expands to over **$150\\text{ m}^3$** (more than $75\\times$ its initial size) until the stretched latex bursts, parachuting the instrument package safely back to Earth."
    )
}
b5766.save()
print("Enriched Combined Gas Law Real-World Applications (Block 5766)")

print("\n=== Real-World Applications Wikimedia Enrichment Complete! ===")
