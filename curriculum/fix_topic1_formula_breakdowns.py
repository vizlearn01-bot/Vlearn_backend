"""
Fix Topic 1 Module 1.2 Formula Breakdown Blocks with proper Markdown tables and math delimiters.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import LessonBlock

def fix_blocks():
    # Block 14414 (Linear Magnification)
    b14 = LessonBlock.objects.get(id=14414)
    b14.content = {
        "formula": r"$$\text{Magnification } (m) = \frac{\text{Height of Image } (h_i)}{\text{Height of Object } (h_o)} = \frac{\text{Image Distance } (v)}{\text{Object Distance } (u)}$$",
        "content": (
            "Linear magnification ($m$) is a dimensionless ratio comparing the scale of an image to its source object.\n\n"
            "| Symbol | Meaning | Standard Units |\n"
            "|---|---|---|\n"
            "| $m$ | Linear magnification | Dimensionless (pure ratio) |\n"
            "| $h_i$ | Height of the image | $\\text{cm}$ or $\\text{m}$ |\n"
            "| $h_o$ | Height of the object | $\\text{cm}$ or $\\text{m}$ |\n"
            "| $v$ | Distance from lens optical centre to image | $\\text{cm}$ or $\\text{m}$ |\n"
            "| $u$ | Distance from lens optical centre to object | $\\text{cm}$ or $\\text{m}$ |\n\n"
            "### Physical Meaning of the Magnification Value:\n\n"
            "- **If $m > 1$**: The image is **magnified** (larger than object).\n"
            "- **If $m = 1$**: The image is the **same size** as the object (occurs at $u = 2f$).\n"
            "- **If $0 < m < 1$**: The image is **diminished** (smaller than object)."
        )
    }
    b14.save()
    print("Block 14414 updated successfully!")

    # Block 14415 (Lens Formula)
    b15 = LessonBlock.objects.get(id=14415)
    b15.content = {
        "formula": r"$$\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$$",
        "content": (
            "The lens formula relates the focal length ($f$), object distance ($u$), and image distance ($v$) for any thin spherical lens.\n\n"
            "### The 'Real-is-Positive' Sign Convention Rules:\n\n"
            "1. **Focal Length ($f$):**\n"
            "   - Converging (Convex) lens has a real focus $\\rightarrow \\mathbf{+f}$ (Positive).\n"
            "   - Diverging (Concave) lens has a virtual focus $\\rightarrow \\mathbf{-f}$ (Negative).\n\n"
            "2. **Object Distance ($u$):**\n"
            "   - Real object placed in front of the lens $\\rightarrow \\mathbf{+u}$ (Positive).\n\n"
            "3. **Image Distance ($v$):**\n"
            "   - Real image (formed by converging rays on the opposite side) $\\rightarrow \\mathbf{+v}$ (Positive).\n"
            "   - Virtual image (formed by diverging rays on the same side) $\\rightarrow \\mathbf{-v}$ (Negative)."
        )
    }
    b15.save()
    print("Block 14415 updated successfully!")

    # Block 14416 (Optical Power)
    b16 = LessonBlock.objects.get(id=14416)
    b16.content = {
        "formula": r"$$\text{Power } (P) = \frac{1}{f \text{ (in metres)}}$$",
        "content": (
            "The optical power of a lens measures its refractive strength—its ability to bend light rays.\n"
            "A lens with a short focal length bends light sharply and has high power, while a lens with a long focal length bends light gently and has low power.\n\n"
            "| Quantity | Symbol | SI Unit | Note |\n"
            "|---|---|---|---|\n"
            "| Power | $P$ | Diopter ($\\text{D}$ or $\\text{m}^{-1}$) | $1\\text{ D} = 1\\text{ m}^{-1}$ |\n"
            "| Focal Length | $f$ | Metres ($\\text{m}$) | **Must be converted from cm to m!** |\n\n"
            "### Sign Rules for Power:\n\n"
            "- Converging (Convex) lenses have positive power: $\\mathbf{+P}$ (e.g., $+5.0\\text{ D}$).\n"
            "- Diverging (Concave) lenses have negative power: $\\mathbf{-P}$ (e.g., $-2.5\\text{ D}$)."
        )
    }
    b16.save()
    print("Block 14416 updated successfully!")

if __name__ == "__main__":
    fix_blocks()
