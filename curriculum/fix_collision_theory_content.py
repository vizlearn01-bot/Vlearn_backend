import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

# Block 1685: The Core Principle: What makes a collision "Effective"?
b1685 = LessonBlock.objects.get(id=1685)
b1685.title = 'The Core Principle: What makes a collision "Effective"?'
b1685.page_title = 'The Core Principle: Effective Collisions'
b1685.content = {
    'text': (
        "According to **Collision Theory**, a chemical reaction can only occur when reacting particles undergo an **effective collision**.\n\n"
        "For a collision to be effective and successfully form products, it must satisfy **two strict criteria simultaneously**:\n\n"
        "1. **Sufficient Energy ($\\ge E_a$):** The colliding particles must possess kinetic energy equal to or greater than the **activation energy** ($E_a$) to break existing chemical bonds.\n"
        "2. **Proper Spatial Orientation:** The reacting particles must collide with the correct physical alignment so that reactive atoms come into direct contact to form new bonds."
    )
}
b1685.save()
print(f"Updated Block [{b1685.id}]")

# Block 1686: Detailed Requirements
b1686 = LessonBlock.objects.get(id=1686)
b1686.title = "The Two Requirements for an Effective Collision"
b1686.page_title = "Energy Barrier & Spatial Orientation"
b1686.content = {
    'text': (
        "### 1. Sufficient Kinetic Energy ($\ge E_a$)\n"
        "Reacting particles must collide with enough kinetic energy to overcome electrostatic repulsion between electron clouds and break existing bonds.\n"
        "* **If Kinetic Energy $< E_a$:** The particles bounce apart unchanged with no reaction.\n"
        "* **If Kinetic Energy $\ge E_a$:** The collision has sufficient energy to form the unstable high-energy **activated complex** and proceed to products.\n\n"
        "### 2. Proper Spatial Orientation\n"
        "Even when particles have immense kinetic energy, they will not react unless they collide with the correct geometric alignment.\n"
        "* **Favourable (Head-on) Orientation:** Reactive chemical bonds collide directly, allowing electron redistribution and product formation.\n"
        "* **Unfavourable (Glancing) Orientation:** Ineffective contact causes molecules to deflect without bond cleavage."
    )
}
b1686.save()
print(f"Updated Block [{b1686.id}]")

# Verify Block 1693 as well to make sure there are no other incomplete fragments
b1693 = LessonBlock.objects.filter(id=1693).first()
if b1693:
    print(f"Block 1693: {b1693.title} | {str(b1693.content)[:100]}")
