import os, sys, django, json, uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

les163 = Lesson.objects.get(id=163)
print(f"=== Deep Enriching Lesson {les163.id}: {les163.title} ===")

# Page 1: Concept Introduction
b5773 = LessonBlock.objects.get(id=5773)
b5773.page_number = 1
b5773.order = 1
b5773.content = {
    "text": (
        "In this module, you will explore the phenomenon of diffusion in gases and liquids, "
        "analyze the classical laboratory experiments (Standard Laboratory Demonstrations: Diffusion in Liquids, Ammonia–Hydrogen Chloride Tube, and the Porous Pot Manometer), "
        "derive Graham's Law of Diffusion mathematically ($R \\propto \\frac{1}{\\sqrt{M_r}}$), "
        "and apply diffusion principles to industrial isotope separation, mine safety, and biological gas exchange."
    )
}
b5773.save()

b5774 = LessonBlock.objects.get(id=5774)
b5774.page_number = 1
b5774.order = 2
b5774.content = {
    "text": (
        "### The Aroma of Fresh Coffee & The Invisible Dance of Molecules\n\n"
        "When someone brews a cup of fresh **Kenyan Arabica coffee** in the kitchen or opens a bottle of perfume across a room, "
        "the pleasant scent quickly spreads until it can be smelled in every corner, even in still air without any wind or fan.\n\n"
        "This natural, spontaneous spreading of substances is called **diffusion**.\n\n"
        "### Definition of Diffusion\n"
        "**Diffusion is the spontaneous movement of particles from a region of higher concentration to a region of lower concentration until they are evenly distributed.**\n\n"
        "### Why Do Gases Diffuse Hundreds of Times Faster Than Liquids?\n"
        "According to the **Kinetic Theory of Matter**:\n"
        "- **In liquids**: Particles are packed closely together in continuous contact, constantly colliding with neighbouring particles. Consequently, a diffusing liquid particle experiences trillions of collisions per second, making liquid diffusion a relatively slow process.\n"
        "- **In gases**: Gas molecules are separated by vast empty spaces (over $99.9\\%$ empty vacuum at standard conditions). Gas particles travel at high speeds (several hundred metres per second) in rapid, random, straight lines, allowing them to disperse throughout the available space rapidly.\n\n"
        "Below are two recorded laboratory demonstrations illustrating diffusion in liquids and diffusion of ammonia gas in air."
    )
}
b5774.save()

b28246 = LessonBlock.objects.get(id=28246)
b28246.page_number = 1
b28246.order = 3
b28246.content["description"] = (
    "Demonstration of diffusion in a liquid: A purple potassium manganate(VII) (KMnO4) crystal dissolves and its particles slowly disperse throughout water due to molecular collisions."
)
b28246.save()

b28247 = LessonBlock.objects.get(id=28247)
b28247.page_number = 1
b28247.order = 4
b28247.content["description"] = (
    "Demonstration of gas diffusion: Pungent ammonia gas (NH3) diffuses through air, turning moist red litmus paper blue along the tube."
)
b28247.save()

# Page 2: Laboratory Experiment: Investigating Whether All Gases Diffuse at the Same Rate
b28248 = LessonBlock.objects.get(id=28248)
b28248.page_number = 2
b28248.order = 5
b28248.content["description"] = (
    "Laboratory Experiment: Investigating the rate of diffusion between concentrated ammonia solution (NH3) and concentrated hydrochloric acid (HCl) in a long glass combustion tube."
)
b28248.save()

b28249 = LessonBlock.objects.get(id=28249)
b28249.page_number = 2
b28249.order = 6
b28249.save()

b5776 = LessonBlock.objects.get(id=5776)
b5776.page_number = 2
b5776.order = 7
b5776.content = {
    "purpose": "Apparatus setup for Laboratory Experiment: Long horizontal glass combustion tube with cotton wool plugs soaked in conc. NH3(aq) and conc. HCl(aq), showing the formation of a dense white ring of solid ammonium chloride closer to the HCl end.",
    "instruction": "A 100 cm transparent combustion tube clamped horizontally. Left plug soaked in conc. NH3 (releasing NH3 gas, Mr = 17). Right plug soaked in conc. HCl (releasing HCl gas, Mr = 36.5). White ring of solid NH4Cl forms approximately 60 cm from NH3 end and 40 cm from HCl end.",
    "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.png/800px-Diffusion_of_ammonia_and_hydrogen_chloride.png"
}
b5776.save()

b5777 = LessonBlock.objects.get(id=5777)
b5777.page_number = 2
b5777.order = 8
b5777.content = {
    "text": (
        "### Laboratory Experiment: Investigating Whether All Gases Diffuse at the Same Rate\n\n"
        "In secondary school chemistry, this classic experiment investigates how molecular mass affects the rate at which gases travel.\n\n"
        "#### 1. Apparatus & Reagents\n"
        "- Long glass combustion tube (approx. $100\\text{ cm}$ long)\n"
        "- Cotton wool\n"
        "- Concentrated aqueous ammonia ($\\text{NH}_3(\\text{aq})$)\n"
        "- Concentrated hydrochloric acid ($\\text{HCl}(\\text{aq})$)\n"
        "- Two tight-fitting rubber bungs (stoppers)\n"
        "- Retort stand with clamps and a metre rule\n\n"
        "#### 2. Procedure & Critical Laboratory Precautions\n"
        "1. Clamp the glass combustion tube horizontally on the laboratory bench.\n"
        "2. Soak a piece of cotton wool in concentrated ammonia solution and another piece of equal size in concentrated hydrochloric acid.\n"
        "3. **Simultaneously** insert the ammonia cotton wool into one end and the hydrochloric acid cotton wool into the opposite end.\n"
        "4. **Immediately seal both ends with rubber bungs.**\n\n"
        "> ⚠️ **Crucial Laboratory Precautions**:\n"
        "> - **Both ends must be sealed immediately**: This prevents toxic, pungent fumes from escaping into the laboratory and eliminates external air draughts (convection currents) from distorting the diffusion path.\n"
        "> - **The glass tube must be completely dry**: Any moisture inside the tube would dissolve the highly soluble $\\text{NH}_3$ and $\\text{HCl}$ gases, stopping them from traveling through the air.\n\n"
        "#### 3. Observations & Quantitative Measurement\n"
        "- After $3\\text{ to }5\\text{ minutes}$, a **dense white ring / deposit** appears on the inner glass wall of the tube.\n"
        "- The white ring does **not** form in the centre ($50\\text{ cm}$). Instead, it forms **closer to the hydrochloric acid end** (approximately $60\\text{ cm}$ from the $\\text{NH}_3$ end and $40\\text{ cm}$ from the $\\text{HCl}$ end in a $100\\text{ cm}$ tube).\n\n"
        "#### 4. Chemical Reaction\n"
        "The white deposit is solid **ammonium chloride** ($\\text{NH}_4\\text{Cl}$),\n"
        "formed by the gas-phase acid-base neutralization reaction:\n\n"
        "$$\\text{NH}_3(g) + \\text{HCl}(g) \\longrightarrow \\text{NH}_4\\text{Cl}(s)$$\n\n"
        "#### 5. Scientific Explanation & Kinetic Theory\n"
        "- **Ammonia gas** ($\\text{NH}_3$) has a Relative Molecular Mass:\n"
        "  $$M_r(\\text{NH}_3) = 14.0 + 3(1.0) = 17.0\\text{ g mol}^{-1}$$\n"
        "- **Hydrogen chloride gas** ($\\text{HCl}$) has a Relative Molecular Mass:\n"
        "  $$M_r(\\text{HCl}) = 1.0 + 35.5 = 36.5\\text{ g mol}^{-1}$$\n\n"
        "Since both gases are at the same room temperature, their particles possess the same average kinetic energy ($E_k = \\frac{1}{2}mv^2$). "
        "Because ammonia molecules have less mass ($m = 17$), they must move at a higher average velocity ($v$) than the heavier hydrogen chloride molecules ($m = 36.5$).\n\n"
        "Thus, $\\text{NH}_3$ travels further ($60\\text{ cm}$) than $\\text{HCl}$ ($40\\text{ cm}$) in the exact same time period:\n\n"
        "$$\\frac{\\text{Distance travelled by } \\text{NH}_3}{\\text{Distance travelled by } \\text{HCl}} = \\frac{60\\text{ cm}}{40\\text{ cm}} = 1.5$$\n\n"
        "This experimental ratio of $1.5$ closely matches the theoretical prediction from Graham's Law: $\\sqrt{\\frac{36.5}{17.0}} = \\sqrt{2.147} \\approx 1.465$!"
    )
}
b5777.save()

# Page 3: The Porous Pot (Diffusion Cup) Manometer Demonstration
b28250 = LessonBlock.objects.get(id=28250)
b28250.page_number = 3
b28250.order = 9
b28250.content["description"] = (
    "Video Demonstration: Investigating diffusion rates of different gases (Hydrogen, Air, Carbon(IV) oxide) through a porous pot connected to a water manometer."
)
b28250.save()

porous_block, created = LessonBlock.objects.get_or_create(
    lesson=les163,
    title="The Porous Pot (Diffusion Cup) Manometer Experiment",
    defaults={
        "block_id": f"f3_chem_t1_l163_porous_pot_{uuid.uuid4().hex[:6]}",
        "block_type": "concept_explanation",
        "component_type": "concept_explanation",
        "page_number": 3,
        "page_title": "The Porous Pot (Diffusion Cup) Demonstration",
        "order": 10,
        "component_order": 10,
        "content": {}
    }
)
porous_block.page_number = 3
porous_block.order = 10
porous_block.page_title = "The Porous Pot (Diffusion Cup) Demonstration"
porous_block.content = {
    "text": (
        "### The Porous Pot (Diffusion Cup) & Water Manometer Experiment\n\n"
        "Another classic demonstration in secondary school physical chemistry uses an unglazed **porous ceramic pot** connected by glass tubing to a U-tube **water manometer** to visually demonstrate differential gas diffusion rates.\n\n"
        "An unglazed porous pot has millions of microscopic pores that allow gas particles to pass through.\n\n"
        "---\n\n"
        "#### Case 1: Surrounding the Porous Pot with Hydrogen Gas ($\\text{H}_2$)\n"
        "1. A beaker filled with hydrogen gas ($\\text{H}_2, M_r = 2$) is inverted over the porous pot containing trapped air ($M_r \\approx 28.8$).\n"
        "2. **Observation**: The liquid level in the near limb of the U-tube manometer is immediately pushed **downwards**, and gas bubbles vigorously out through the open water beaker.\n"
        "3. **Scientific Reason**: Hydrogen molecules are extremely light ($M_r = 2$) and have much higher molecular speeds than nitrogen/oxygen particles in air ($M_r \\approx 28.8$). Therefore, **hydrogen diffuses INTO the porous pot faster than air diffuses OUT**.\n"
        "4. This builds up a higher pressure inside the pot, forcing the water level down.\n\n"
        "---\n\n"
        "#### Case 2: Surrounding the Porous Pot with Carbon(IV) Oxide ($\\text{CO}_2$)\n"
        "1. A beaker of carbon(IV) oxide ($\\text{CO}_2, M_r = 44$) is placed over the porous pot containing air ($M_r \\approx 28.8$).\n"
        "2. **Observation**: The liquid level in the near limb of the manometer **rises upwards** into the tube.\n"
        "3. **Scientific Reason**: Carbon(IV) oxide molecules are heavier ($M_r = 44$) and move slower than air molecules ($M_r \\approx 28.8$). Consequently, **air diffuses OUT of the pot faster than $\\text{CO}_2$ diffuses IN**.\n"
        "4. This creates a partial vacuum (pressure drop) inside the pot, causing atmospheric pressure to push water up the manometer limb.\n\n"
        "> 💡 **Key Takeaway**: The direction of water movement in the manometer proves directly that **lighter gases diffuse faster than heavier gases**."
    )
}
porous_block.save()

# Page 4: Formal Statement of Graham's Law & Mathematical Derivations
b28261 = LessonBlock.objects.get(id=28261)
b28261.page_number = 4
b28261.order = 11
b28261.save()

b5775 = LessonBlock.objects.get(id=5775)
b5775.page_number = 4
b5775.order = 12
b5775.content = {
    "text": (
        "### Graham's Law of Diffusion: Statement & Full Mathematical Derivations\n\n"
        "In 1829, Scottish physical chemist Thomas Graham formulated the quantitative relationship governing the rates of effusion and diffusion of gases.\n\n"
        "#### 1. Formal Statement of Graham's Law\n"
        "**Under identical conditions of temperature and pressure, the rate of diffusion of a gas is inversely proportional to the square root of its density ($\\rho$) or relative molecular mass ($M_r$).**\n\n"
        "#### 2. Mathematical Formulations\n"
        "##### A. In Terms of Gas Density ($\\rho$):\n"
        "$$R \\propto \\frac{1}{\\sqrt{\\rho}} \\quad \\implies \\quad \\frac{R_1}{R_2} = \\sqrt{\\frac{\\rho_2}{\\rho_1}}$$\n\n"
        "##### B. In Terms of Relative Molecular Mass ($M_r$):\n"
        "Since Avogadro's Law establishes that at constant temperature and pressure, gas density is directly proportional to molar mass ($\\rho \\propto M_r$):\n"
        "$$R \\propto \\frac{1}{\\sqrt{M_r}} \\quad \\implies \\quad \\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}}$$\n\n"
        "##### C. In Terms of Time Taken ($t$):\n"
        "Diffusion rate is the volume of gas diffusing per unit time ($R = \\frac{V}{t}$). For equal volumes of two gases:\n"
        "$$\\frac{R_1}{R_2} = \\frac{V/t_1}{V/t_2} = \\frac{t_2}{t_1}$$\n\n"
        "Combining with the molecular mass relationship gives the **Time Inversion Equation**:\n"
        "$$\\frac{t_2}{t_1} = \\sqrt{\\frac{M_2}{M_1}} \\quad \\text{or} \\quad \\frac{t_1}{t_2} = \\sqrt{\\frac{M_1}{M_2}}$$\n\n"
        "> ⚠️ **Crucial Rule on Time Ratios**:\n"
        "> A lighter gas has a higher rate ($R_1 > R_2$) but takes **less time** ($t_1 < t_2$) to diffuse. Notice that the subscripts in the time ratio match the mass subscripts under the square root!\n\n"
        "##### D. In Terms of Distance Travelled ($d$):\n"
        "For gases diffusing simultaneously through the same medium over the same time interval ($t$):\n"
        "$$\\frac{d_1}{d_2} = \\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}}$$\n\n"
        "---\n\n"
        "#### 3. Factors Influencing the Rate of Diffusion\n"
        "1. **Relative Molecular Mass / Density**: Lighter gases diffuse faster than denser, heavier gases.\n"
        "2. **Temperature**: Increasing temperature increases the average kinetic energy of gas molecules ($E_k \\propto T$), increasing particle speed and diffusion rate.\n"
        "3. **Concentration Gradient**: A steeper concentration difference between two regions produces faster net diffusion.\n"
        "4. **State of Matter**: Gas particles diffuse roughly $1,000\\times$ faster than dissolved solutes in liquids because of vast intermolecular spacing."
    )
}
b5775.save()

# Page 5: Interactive Simulation Stage
b28251 = LessonBlock.objects.get(id=28251)
b28251.page_number = 5
b28251.order = 13
b28251.save()

# Page 6: Real-World Applications
app_block, created = LessonBlock.objects.get_or_create(
    lesson=les163,
    title="Industrial & Biological Applications of Graham's Law",
    defaults={
        "block_id": f"f3_chem_t1_l163_apps_{uuid.uuid4().hex[:6]}",
        "block_type": "real_world_example",
        "component_type": "real_world_example",
        "page_number": 6,
        "page_title": "Real-World & Industrial Applications",
        "order": 14,
        "component_order": 14,
        "content": {}
    }
)
app_block.page_number = 6
app_block.order = 14
app_block.page_title = "Real-World & Industrial Applications"
app_block.content = {
    "text": (
        "### Industrial & Biological Applications of Graham's Law\n\n"
        "Graham's Law is not just a laboratory concept; it plays a critical role in nuclear energy, mining safety, and human physiology:\n\n"
        "#### 1. Nuclear Energy: Uranium Isotope Separation\n"
        "Naturally occurring uranium contains $99.3\\%$ Uranium-238 ($^{238}\\text{U}$) and only $0.7\\%$ fissile Uranium-235 ($^{235}\\text{U}$). To fuel nuclear reactors, the concentration of $^{235}\\text{U}$ must be enriched.\n\n"
        "In the **gaseous diffusion process**, solid uranium is converted into volatile uranium hexafluoride gas ($\\text{UF}_6$):\n"
        "- $^{235}\\text{UF}_6$ has molecular mass $M_r = 235 + 6(19) = 349\\text{ g mol}^{-1}$\n"
        "- $^{238}\\text{UF}_6$ has molecular mass $M_r = 238 + 6(19) = 352\\text{ g mol}^{-1}$\n\n"
        "According to Graham's Law:\n"
        "$$\\frac{R(^{235}\\text{UF}_6)}{R(^{238}\\text{UF}_6)} = \\sqrt{\\frac{352}{349}} \\approx 1.0043$$\n\n"
        "The lighter $^{235}\\text{UF}_6$ diffuses $0.43\\%$ faster through porous nickel membranes. By passing the gas through thousands of successive diffusion stages (a diffusion cascade), weapons-grade or reactor-grade enriched uranium is harvested!\n\n"
        "---\n\n"
        "#### 2. Underground Mine Safety: Marsh Gas (Methane) Detection\n"
        "In deep coal and gold mines, dangerous pockets of **methane gas** ($\\text{CH}_4$, \"firedamp\") seep from mineral seams.\n"
        "- Methane has $M_r = 12 + 4(1) = 16\\text{ g mol}^{-1}$, making it substantially lighter than ambient air ($M_r \\approx 28.8\\text{ g mol}^{-1}$).\n"
        "- Because of its lower molecular mass, methane diffuses very rapidly upwards and collects in high concentrations along the roofs of mining shafts.\n"
        "- Mine safety systems deploy porous diffusion detectors at tunnel ceilings to catch methane before it reaches explosive threshold limits ($5\\text{--}15\\%$ in air).\n\n"
        "---\n\n"
        "#### 3. Human Respiratory Gas Exchange in Alveoli\n"
        "In human lungs, oxygen ($\\text{O}_2, M_r = 32$) diffuses from the alveoli air sacs across the microscopic respiratory membrane into red blood cells, while carbon(IV) oxide ($\\text{CO}_2, M_r = 44$) diffuses in the opposite direction to be exhaled.\n"
        "Graham's Law, combined with Henry's Law of solubility, dictates the exact physical rates at which our tissues receive life-sustaining oxygen."
    )
}
app_block.save()

# Page 7: Worked Examples
b5778 = LessonBlock.objects.get(id=5778)
b5778.page_number = 7
b5778.order = 15
b5778.save()

b5779 = LessonBlock.objects.get(id=5779)
b5779.page_number = 7
b5779.order = 16
b5779.save()

# Page 8: Common Misconceptions & Practice Questions
b5780 = LessonBlock.objects.get(id=5780)
b5780.page_number = 8
b5780.order = 17
b5780.save()

b5781 = LessonBlock.objects.get(id=5781)
b5781.page_number = 8
b5781.order = 18
b5781.save()

b5782 = LessonBlock.objects.get(id=5782)
b5782.page_number = 8
b5782.order = 19
b5782.save()

# Page 9: Key Takeaways & Summary
b5783 = LessonBlock.objects.get(id=5783)
b5783.page_number = 9
b5783.order = 20
b5783.save()

print("\n=== Graham's Law Full Pedagogical Enrichment Complete! ===")
