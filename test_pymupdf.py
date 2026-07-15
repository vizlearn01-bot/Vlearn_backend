import fitz

def test_fitz():
    doc = fitz.open("dummy_textbook.pdf")
    
    # Check outlines
    outlines = doc.get_toc(simple=False)
    print("Outlines:")
    for item in outlines:
        # format is usually [level, title, page_number, dest_details...]
        print(item)
        
    # Check first page blocks
    page = doc[0]
    blocks = page.get_text("blocks")
    print("\nBlocks on page 0:")
    for block in blocks:
        # format: (x0, y0, x1, y1, "text", block_no, block_type)
        # block_type 0 is text, 1 is image
        print(block)

test_fitz()
