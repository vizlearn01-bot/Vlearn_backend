import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

LESSON_ID = 237

print(f"Starting LaTeX resolution for Lesson ID {LESSON_ID}...")

# 1. Block 14435 (Order 2, concept_explanation)
b = LessonBlock.objects.get(id=14435)
b.content['text'] = (
    "### How It Works:\n"
    "A simple microscope consists of a **single converging (convex) lens of short focal length**.\n"
    "The object to be viewed is placed inside the focal point ($u < f$). As light refracts through the lens, diverging rays emerge on the eye side. When the eye looks through the lens, it sees a **virtual, erect, and magnified image**.\n\n"
    "### The Near Point and Distinct Vision ($D$):\n"
    "To view the image with maximum clarity and minimum eye strain, the lens position is adjusted so that the virtual image forms at the **least distance of distinct vision ($D = 25\\text{ cm}$)**, known as the near point of a normal human eye.\n\n"
    "### Angular Magnification (Magnifying Power $M$):\n"
    "$M = \\frac{\\beta}{\\alpha}$\n"
    "where $\\beta$ is the visual angle subtended by the image at the eye with the lens, and $\\alpha$ is the angle subtended by the object at distance $D = 25\\text{ cm}$ without the lens. A lens with a shorter focal length bends light more sharply, producing a larger visual angle $\\beta$ and higher magnifying power."
)
b.save()
print("Fixed Block 14435")

# 2. Block 14436 (Order 3, suggested_diagram)
b = LessonBlock.objects.get(id=14436)
b.content['text'] = "Ray diagram of a simple magnifying glass showing an object placed within focal length $u < f$ forming a virtual, upright, magnified image at near point $D = 25\\text{ cm}$ from the eye."
b.content['instruction'] = "Draw a convex lens with an eye on the right side. Place an object on the left inside focal point $F$ ($u < f$). Trace two rays refracting into the eye. Draw dashed backward projections intersecting at distance $D = 25\\text{ cm}$ to form a large virtual upright image."
b.save()
print("Fixed Block 14436")

# 3. Block 14437 (Order 4, concept_explanation)
b = LessonBlock.objects.get(id=14437)
b.content['text'] = (
    "To achieve magnifications far beyond the capability of a single lens, a **compound microscope** uses two converging lenses in series:\n\n"
    "### 1. The Objective Lens (Short Focal Length $f_o$):\n"
    "- Positioned close to the microscopic specimen.\n"
    "- The specimen is placed just outside its focal point ($f_o < u_o < 2f_o$).\n"
    "- Produces a **real, inverted, and magnified intermediate image ($I_1$)** inside the microscope barrel.\n\n"
    "### 2. The Eyepiece Lens (Focal Length $f_e$, where $f_e > f_o$):\n"
    "- Positioned near the observer's eye.\n"
    "- The barrel length is adjusted so that the intermediate image $I_1$ falls inside the focal length of the eyepiece ($u_e < f_e$).\n"
    "- The eyepiece acts as a magnifying glass, magnifying $I_1$ into a **massive virtual, inverted final image ($I_2$)** at near point $D = 25\\text{ cm}$.\n\n"
    "### Total Magnification Formula:\n"
    "$M_{\\text{total}} = m_o \\times m_e = \\left(\\frac{v_o}{u_o}\\right) \\times \\left(\\frac{v_e}{u_e}\\right)$"
)
b.save()
print("Fixed Block 14437")

# 4. Block 14438 (Order 5, suggested_diagram)
b = LessonBlock.objects.get(id=14438)
b.content['text'] = "Two-lens ray diagram of a compound microscope showing objective lens forming real magnified intermediate image $I_1$ and eyepiece lens forming massive virtual final image $I_2$ at distance $D$."
b.content['instruction'] = "Draw two coaxial lenses: Objective lens (small diameter, short $f_o$) and Eyepiece lens (larger diameter, $f_e$). Trace rays from specimen outside $F_o$ forming inverted real image $I_1$ inside $F_e$. Trace rays from $I_1$ through eyepiece diverging into eye, with dashed projections forming huge virtual inverted final image $I_2$ at $D$."
b.save()
print("Fixed Block 14438")

# 5. Block 14439 (Order 6, concept_explanation)
b = LessonBlock.objects.get(id=14439)
b.content['text'] = (
    "The astronomical telescope is designed to view celestial objects at optical infinity (planets, stars, distant galaxies): ### 1. Objective Lens (Very Large Focal Length $f_o$, Wide Aperture):\n\n"
    "- Gathers maximum starlight and focuses incoming parallel rays to form a **real, inverted, highly diminished intermediate image ($I_1$)** in its focal plane ($F_o$). ### 2. Eyepiece Lens (Short Focal Length $f_e$):\n"
    "- Magnifies the intermediate image $I_1$. ### Normal Adjustment (Viewing at Infinity for a Relaxed Eye):\n"
    "- In normal adjustment, the telescope is set so the focal points of both lenses coincide at the same physical point ($F_o = F_e$).\n"
    "- The intermediate image $I_1$ forms exactly at $F_e$, causing the eyepiece to refract the rays completely parallel to infinity, allowing the observer to view the final image with a completely relaxed, unstrained eye. ### Key Formulas in Normal Adjustment:\n"
    "- **Telescope Barrel Length ($L$):** $L = f_o + f_e$\n"
    "- **Angular Magnification ($M$):** $M = \\frac{f_o}{f_e}$"
)
b.save()
print("Fixed Block 14439")

# 6. Block 14440 (Order 7, suggested_diagram)
b = LessonBlock.objects.get(id=14440)
b.content['text'] = "Ray diagram of an astronomical telescope in normal adjustment showing incoming parallel rays from infinity focusing at shared focal plane $F_o = F_e$ and emerging parallel from eyepiece."
b.content['instruction'] = "Draw objective lens (left) and eyepiece (right) sharing focal plane $F_o = F_e$. Trace tilted parallel rays from distant star focusing to inverted intermediate image $I_1$ at $F_o$. Trace rays from $I_1$ through eyepiece emerging as parallel beam into eye. Label: Barrel Length $L = f_o + f_e$, Final Image at Infinity."
b.save()
print("Fixed Block 14440")

# 7. Block 14441 (Order 8, concept_explanation)
b = LessonBlock.objects.get(id=14441)
b.content['text'] = (
    "A camera is a light-proof enclosure with a converging lens system at one end and a light-sensitive surface (digital sensor or film) at the other: ### Key Functional Components:\n\n"
    "- **Converging Lens System**: Focuses light from an object ($u > 2f$) to form a **real, inverted, diminished image** on the sensor.\n"
    "- **Focusing Mechanism**: The focusing ring physically moves the lens closer to or further from the sensor to ensure sharp focus for objects at different distances ($v$).\n"
    "- **Aperture & Diaphragm**: An adjustable circular iris that regulates the light intensity entering the camera.\n"
    "- **Shutter**: A precision mechanical or electronic gate that opens for a fraction of a second (exposure time, e.g., $1/1000\\text{ s}$) to expose the sensor to light.\n"
    "- **Sensor / Film**: The recording surface coated with photosensitive pixels or chemical emulsion."
)
b.save()
print("Fixed Block 14441")

# 8. Block 14443 (Order 10, concept_explanation)
b = LessonBlock.objects.get(id=14443)
b.content['text'] = (
    "The human eye is a biological optical instrument functioning analogously to a camera: ### Key Anatomical Landmarks:\n\n"
    "- **Cornea**: Tough transparent outer membrane providing the initial and greatest refraction of incoming light.\n"
    "- **Crystalline Lens**: Flexible, double-convex organic lens that provides fine-focusing adjustments.\n"
    "- **Iris & Pupil**: The iris is a coloured muscle that expands or contracts the central aperture (pupil) to regulate light entry.\n"
    "- **Retina**: Light-sensitive screen at the back of the eye coated with photoreceptors (rods and cones) where **real, inverted images** form.\n"
    "- **Optic Nerve**: Transmits electrical signals from the retina to the brain's visual cortex, which inverts the perception upright. ### The Mechanism of Accommodation:\n"
    "Accommodation is the ability of the eye to alter its focal length to focus clearly on both near and distant objects:\n\n"
    "- **Viewing Distant Objects ($u = \\infty$):** Ciliary muscles relax $\\rightarrow$ suspensory ligaments pull taut $\\rightarrow$ crystalline lens is flattened $\\rightarrow$ **focal length increases** to focus parallel rays onto retina.\n"
    "- **Viewing Near Objects ($u = 25\\text{ cm}$):** Ciliary muscles contract $\\rightarrow$ suspensory ligaments loosen $\\rightarrow$ lens bulges into a thicker, more spherical shape $\\rightarrow$ **focal length decreases** to bend divergent rays onto retina."
)
b.save()
print("Fixed Block 14443")

# 9. Block 14448 (Order 15, concept_explanation)
b = LessonBlock.objects.get(id=14448)
b.content['text'] = (
    "### What is Hypermetropia?\n"
    "A long-sighted person can see distant objects clearly, but **near objects (at $25\\text{ cm}$) appear blurred**. ### Physical Causes:\n"
    "1. The eyeball is **too short** from front to back.\n"
    "2. The eye lens is **too flat / too weak** (ciliary muscles cannot contract enough to achieve a short focal length), causing divergent rays from near objects to focus **behind the retina**. ### Optical Correction: Converging (Convex) Lens\n"
    "Placing a **converging (convex) lens** in front of the eye pre-converges the divergent rays from near objects before they enter the eye. The weakened crystalline lens can then easily complete the convergence to form a sharp image directly **on the retina**."
)
b.save()
print("Fixed Block 14448")

# 10. Block 14449 (Order 16, suggested_diagram)
b = LessonBlock.objects.get(id=14449)
b.content['instruction'] = "Draw 2 vertically stacked eye diagrams: (Top) Shortened eye with divergent rays from near object ($25\\text{ cm}$) focusing behind the retina plane. (Bottom) Convex lens placed in front of eye pre-converging rays, allowing eye lens to bring focus directly onto retina surface."
b.save()
print("Fixed Block 14449")

# 11. Block 14452 (Order 19, worked_example)
b = LessonBlock.objects.get(id=14452)
b.content['problem'] = (
    "A research compound microscope consists of an objective lens of focal length $f_o = 1.0\\text{ cm}$ and an eyepiece lens of focal length $f_e = 5.0\\text{ cm}$. An illuminated specimen is placed $1.2\\text{ cm}$ from the objective lens. (a) Calculate the position of the intermediate image ($v_o$) formed by the objective lens.\n"
    "(b) If the final virtual image is formed at the near point $D = 25\\text{ cm}$ from the eyepiece, calculate the required barrel length ($L$) between the two lenses.\n"
    "(c) Determine the total magnification ($M_{\\text{total}}$) produced by the microscope system."
)
b.content['steps'] = [
    "**(a) Objective Lens Image Position ($v_o$):** $\\frac{1}{f_o} = \\frac{1}{u_o} + \\frac{1}{v_o} \\implies \\frac{1}{v_o} = \\frac{1}{1.0} - \\frac{1}{1.2} = 1.0 - 0.833 = 0.167\\text{ cm}^{-1}$, $v_o = \\frac{1}{0.167} = \\mathbf{+6.0\\text{ cm}} \\text{ (inside the barrel)}$",
    "**(b) Eyepiece Object Distance ($u_e$) & Barrel Length ($L$):** Eyepiece forms virtual image at $v_e = -25\\text{ cm}$ with $f_e = +5.0\\text{ cm}$: $\\frac{1}{u_e} = \\frac{1}{f_e} - \\frac{1}{v_e} = \\frac{1}{5.0} - \\left(\\frac{1}{-25}\\right) = \\frac{5}{25} + \\frac{1}{25} = \\frac{6}{25}$, $u_e = \\frac{25}{6} \\approx 4.17\\text{ cm}$. Total barrel separation: $L = v_o + u_e = 6.0\\text{ cm} + 4.17\\text{ cm} = \\mathbf{10.17\\text{ cm}}$",
    "**(c) Total System Magnification ($M_{\\text{total}}$):** Objective magnification: $m_o = \\frac{v_o}{u_o} = \\frac{6.0}{1.2} = 5.0$. Eyepiece magnification: $m_e = \\frac{v_e}{u_e} = \\frac{25}{4.17} = 6.0$. Total magnification: $M_{\\text{total}} = m_o \\times m_e = 5.0 \\times 6.0 = \\mathbf{30\\text{ times}}$",
    "**Physical Conclusion:** The specimen is magnified 5 times into a real intermediate image, which the eyepiece magnifies a further 6 times, producing a sharp, 30-times enlarged virtual image for the researcher."
]
b.save()
print("Fixed Block 14452")

# 12. Block 14454 (Order 21, knowledge_check)
b = LessonBlock.objects.get(id=14454)
b.content['question'] = "A patient cannot read a book held at $25\\text{ cm}$ because divergent light rays from the text converge behind the retina. Diagnose the defect and state the corrective spectacle lens required:"
b.save()
print("Fixed Block 14454")

# 13. Block 14455 (Order 22, knowledge_check)
b = LessonBlock.objects.get(id=14455)
b.content['question'] = "An astronomical telescope in normal adjustment has an objective lens of focal length $f_o = 100\\text{ cm}$ and an eyepiece of focal length $f_e = 5\\text{ cm}$. What is the barrel length ($L$) and angular magnification ($M$) of the telescope?"
b.content['options'] = [
    "$L = 105\\text{ cm}, M = 20$",
    "$L = 95\\text{ cm}, M = 20$",
    "$L = 105\\text{ cm}, M = 500$",
    "$L = 500\\text{ cm}, M = 20$"
]
b.content['explanation'] = "In normal adjustment: 1. Barrel Length: $L = f_o + f_e = 100\\text{ cm} + 5\\text{ cm} = 105\\text{ cm}$. 2. Angular Magnification: $M = \\frac{f_o}{f_e} = \\frac{100}{5} = 20\\text{ times}$."
b.save()
print("Fixed Block 14455")

# 14. Block 14456 (Order 23, summary)
b = LessonBlock.objects.get(id=14456)
b.content['text'] = (
    "### Summary of Optical Instruments:\n"
    "- **Simple Microscope**: Single convex lens ($u < f$), forms virtual, upright, magnified image at near point $D = 25\\text{ cm}$.\n"
    "- **Compound Microscope**: Objective ($f_o$) forms real magnified intermediate image; Eyepiece ($f_e$) magnifies it to massive virtual image ($M = m_o \\times m_e$).\n"
    "- **Astronomical Telescope**: Long $f_o$ objective gathers starlight to focal plane; short $f_e$ eyepiece refracts parallel to infinity ($L = f_o + f_e$, $M = \\frac{f_o}{f_e}$).\n"
    "- **Camera vs. Eye**: Camera focuses by moving lens ($v$), eye focuses by ciliary muscle accommodation (changing curvature $f$).\n"
    "- **Corrective Optometry**: Myopia (short-sighted, rays focus in front $\\rightarrow$ concave lens); Hypermetropia (long-sighted, rays focus behind $\\rightarrow$ convex lens); Presbyopia (bifocals); Astigmatism (cylindrical lens)."
)
b.save()
print("Fixed Block 14456")

print("\nSuccessfully updated all Lesson ID 237 blocks!")
