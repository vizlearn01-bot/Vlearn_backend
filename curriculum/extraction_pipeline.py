"""
Knowledge Pack Builder - Extraction Pipeline Scaffolding

This module outlines the step-by-step pipeline for extracting structured
knowledge from raw textbooks, following the design principles of the
Knowledge Pack architecture.
"""
import uuid
import os
import fitz  # PyMuPDF
from io import BytesIO
from django.core.files.base import ContentFile
from curriculum.models import KnowledgePack, KnowledgeChunk
try:
    import pytesseract
    from PIL import Image
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False
except Exception:
    TESSERACT_AVAILABLE = False

def build_toc_structure(toc):
    """
    Processes PyMuPDF TOC ([level, title, page]) into a structured list of Topics and Units.
    """
    structure = []
    
    # We maintain pointers to the last seen topic at level 1
    last_topic = None
    
    for item in toc:
        if len(item) < 3:
            continue
        level, title, page = item[0], item[1], item[2]
        
        node = {
            'id': str(uuid.uuid4()),
            'title': title,
            'start_page': page,
            'type': 'topic' if level == 1 else 'unit',
            'children': []
        }
        
        if level == 1:
            structure.append(node)
            last_topic = node
        elif level >= 2 and last_topic:
            # Force everything deeper than 1 into a unit of the last topic for simplicity
            node['type'] = 'unit'
            last_topic['children'].append(node)
            
    return structure

def classify_text_block(text):
    """Heuristic semantic classification of a text block."""
    text_lower = text.lower().strip()
    if text_lower.startswith("definition:") or "is defined as" in text_lower:
        return 'definition'
    elif text_lower.startswith("example") or text_lower.startswith("worked example"):
        return 'worked_example'
    elif text_lower.startswith("exercise") or text_lower.startswith("question"):
        return 'exercise'
    elif text_lower.startswith("experiment") or text_lower.startswith("practical"):
        return 'practical'
    else:
        return 'core_text'

def process_textbook_pipeline(knowledge_pack_id):
    """
    Main orchestrator for Document Ingestion and Knowledge Repository Construction (Phase 2).
    """
    try:
        kp = KnowledgePack.objects.get(id=knowledge_pack_id)
        
        if not kp.file:
            raise Exception("No file attached to Knowledge Pack.")
            
        doc = fitz.open(kp.file.path)
        
        # 1. Extract Curriculum Structure (TOC)
        toc = doc.get_toc(simple=True) # [level, title, page]
        structure = build_toc_structure(toc)
        
        # We keep the structure if it has any items at all.
        if len(structure) == 0:
            print("No TOC found in document.")
            
        kp.extracted_structure = structure
        
        # 2. Extract Pages & Build Knowledge Repository
        # First, clear existing chunks if any (for idempotency)
        kp.chunks.all().delete()
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            blocks = page.get_text("blocks")
            
            # Scanned page heuristic: 0 text blocks, or just 1 massive image block
            is_scanned = len(blocks) == 0 or (len(blocks) == 1 and blocks[0][6] == 1)
            
            if is_scanned and TESSERACT_AVAILABLE:
                # OCR Fallback
                try:
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    text = pytesseract.image_to_string(img)
                    
                    if text.strip():
                        KnowledgeChunk.objects.create(
                            knowledge_pack=kp,
                            content_text=text.strip(),
                            chunk_type='core_text',
                            start_page=page_num + 1,
                            end_page=page_num + 1,
                            ocr_confidence=0.85 # Placeholder confidence
                        )
                except Exception as e:
                    print(f"OCR failed for page {page_num + 1}: {e}")
            else:
                # Digital Document Extraction
                for idx, block in enumerate(blocks):
                    x0, y0, x1, y1, text, block_no, block_type = block
                    
                    if block_type == 0:  # Text
                        clean_text = text.strip()
                        if not clean_text:
                            continue
                            
                        chunk_type = classify_text_block(clean_text)
                        
                        KnowledgeChunk.objects.create(
                            knowledge_pack=kp,
                            content_text=clean_text,
                            chunk_type=chunk_type,
                            bounding_box=[x0, y0, x1, y1],
                            start_page=page_num + 1,
                            end_page=page_num + 1,
                            order=idx
                        )
                    elif block_type == 1:  # Image
                        try:
                            # Render the image region
                            rect = fitz.Rect(x0, y0, x1, y1)
                            pix = page.get_pixmap(clip=rect)
                            img_data = pix.tobytes("png")
                            
                            chunk = KnowledgeChunk(
                                knowledge_pack=kp,
                                chunk_type='diagram',
                                bounding_box=[x0, y0, x1, y1],
                                start_page=page_num + 1,
                                end_page=page_num + 1,
                                order=idx
                            )
                            filename = f"diagram_{kp.id}_p{page_num+1}_b{idx}.png"
                            chunk.image.save(filename, ContentFile(img_data), save=True)
                        except Exception as e:
                            print(f"Failed to extract image block {idx} on page {page_num+1}: {e}")

        kp.status = 'review'
        kp.save()
        
    except Exception as e:
        print(f"Error processing textbook: {e}")
        try:
            kp = KnowledgePack.objects.get(id=knowledge_pack_id)
            kp.status = 'failed'
            kp.save()
        except:
            pass
