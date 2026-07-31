from pypdf import PdfReader
import sys

def print_outline(outlines, level=0):
    if not outlines:
        return
    for item in outlines:
        if isinstance(item, list):
            print_outline(item, level + 1)
        else:
            title = item.title if hasattr(item, 'title') else str(item)
            print("  " * level + f"- {title}")

try:
    reader = PdfReader("media/textbooks/KLB_SECONDARY_CHEMISTRY_FORM_4_Kenya_Literature_Bureau_Z-Library.pdf")
    print("Outlines:")
    print_outline(reader.outline)
except Exception as e:
    print(f"Error: {e}")
