from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(path):
    c = canvas.Canvas(path, pagesize=letter)
    
    # Create an outline tree (Bookmarks)
    c.bookmarkPage("chapter1")
    c.addOutlineEntry("Chapter 1: The Mole", "chapter1", level=0)
    c.drawString(100, 750, "Chapter 1: The Mole")
    c.showPage()
    
    c.bookmarkPage("sec1")
    c.addOutlineEntry("1.1 Avogadro's Constant", "sec1", level=1)
    c.drawString(100, 750, "1.1 Avogadro's Constant")
    c.showPage()
    
    c.bookmarkPage("sec2")
    c.addOutlineEntry("1.2 Molar Mass", "sec2", level=1)
    c.drawString(100, 750, "1.2 Molar Mass")
    c.showPage()
    
    c.bookmarkPage("chapter2")
    c.addOutlineEntry("Chapter 2: Gas Laws", "chapter2", level=0)
    c.drawString(100, 750, "Chapter 2: Gas Laws")
    c.showPage()
    
    c.bookmarkPage("sec3")
    c.addOutlineEntry("2.1 Boyle's Law", "sec3", level=1)
    c.drawString(100, 750, "2.1 Boyle's Law")
    
    c.save()

if __name__ == "__main__":
    create_pdf("dummy_textbook.pdf")
