from PyPDF2 import PdfReader

try:
    reader = PdfReader("dummy_textbook.pdf")
    outlines = reader.outline
    print("Outlines length:", len(outlines))
    for item in outlines:
        if not isinstance(item, list):
            title = item.title if hasattr(item, 'title') else str(item)
            try:
                page_num = reader.get_destination_page_number(item)
                print(f"{title} -> Page {page_num}")
            except Exception as e:
                print(f"{title} -> Error getting page: {e}")
except Exception as e:
    print(f"Error: {e}")
