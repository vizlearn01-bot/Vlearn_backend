"""
Knowledge Pack Builder - Document Ingestion Service

This module outlines the step-by-step pipeline for extracting structured
knowledge from raw textbooks, supporting PDF, MD, and TXT files deterministically.
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

class DocumentIngestionService:
    def __init__(self, knowledge_pack_id=None):
        if knowledge_pack_id is not None:
            self.kp = KnowledgePack.objects.get(id=knowledge_pack_id)
            if not self.kp.file:
                raise Exception("No file attached to Knowledge Pack.")
            # Retrieve file extension safely without assuming local filesystem storage
            file_name = self.kp.file.name or ""
            ext = os.path.splitext(file_name)[1].lower()
            self.file_bytes = None
            
            # If extension is missing (e.g. Cloudinary public_id stripping), detect by magic bytes
            if not ext:
                bytes_head = self._get_file_bytes()[:10]
                if bytes_head.startswith(b'%PDF'):
                    ext = '.pdf'
                else:
                    ext = '.txt'
            self.file_extension = ext
        else:
            self.kp = None
            self.file_extension = None
            self.file_bytes = None

    def _get_file_bytes(self):
        if self.file_bytes is None:
            self.kp.file.open('rb')
            try:
                self.file_bytes = self.kp.file.read()
            finally:
                self.kp.file.close()
        return self.file_bytes

    def process(self):
        try:
            self.kp.chunks.all().delete()
            
            if self.file_extension == '.pdf':
                self._process_pdf()
            elif self.file_extension in ['.md', '.txt']:
                self._process_text()
            else:
                raise ValueError(f"Unsupported file type: {self.file_extension}")
                
            self.kp.status = 'review'
            self.kp.save()
        except Exception as e:
            print(f"Error processing textbook: {e}")
            self.kp.status = 'failed'
            self.kp.save()
            raise e

    def _process_text(self):
        # Deterministic text processing
        file_data = self._get_file_bytes()
        content = file_data.decode('utf-8', errors='replace')
        
        # Split by paragraphs or simple chunks
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        for idx, para in enumerate(paragraphs):
            KnowledgeChunk.objects.create(
                knowledge_pack=self.kp,
                content_text=para,
                chunk_type=self._classify_text_block(para),
                order=idx
            )
            
    def _process_pdf(self):
        pdf_bytes = self._get_file_bytes()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        toc = doc.get_toc(simple=True)
        filtered_toc = [
            item for item in toc 
            if len(item) >= 2 and not any(dummy in item[1].lower() for dummy in ["table of contents", "contents", "overview", "preface", "foreword"])
        ]
        structure = self._build_toc_structure(filtered_toc)
        if len(structure) < 2:
            structure = self._heuristic_regex_recovery(doc)
        self.kp.extracted_structure = structure
        
        # Build a page → section_title lookup so every chunk knows its section
        page_to_section = self._build_page_to_section(structure)

        for page_num in range(len(doc)):
            page = doc[page_num]
            blocks = page.get_text("blocks")
            is_scanned = len(blocks) == 0 or (len(blocks) == 1 and blocks[0][6] == 1)
            section_title = page_to_section.get(page_num + 1)
            
            if is_scanned and TESSERACT_AVAILABLE:
                self._process_ocr_page(page, page_num, section_title)
            else:
                self._process_digital_page(page, blocks, page_num, section_title)

    @staticmethod
    def _build_page_to_section(structure):
        """
        Given a list of topic/unit nodes (each with start_page), build a dict
        mapping every PDF page number to the nearest section title that precedes it.
        """
        # Collect all (start_page, title) pairs from topics and their children
        page_title_pairs = []
        for node in structure:
            if node.get('start_page') and node.get('title'):
                page_title_pairs.append((node['start_page'], node['title']))
            for child in node.get('children', []):
                if child.get('start_page') and child.get('title'):
                    page_title_pairs.append((child['start_page'], child['title']))
        
        if not page_title_pairs:
            return {}
        
        # Sort by page number
        page_title_pairs.sort(key=lambda x: x[0])
        
        # For each page, assign the most recently started section
        page_to_section = {}
        current_title = None
        pair_idx = 0
        max_page = max(p for p, _ in page_title_pairs) + 300  # generous upper bound
        
        for page_num in range(1, max_page + 1):
            # Advance through sections whose start_page <= current page
            while pair_idx < len(page_title_pairs) and page_title_pairs[pair_idx][0] <= page_num:
                current_title = page_title_pairs[pair_idx][1]
                pair_idx += 1
            if current_title:
                page_to_section[page_num] = current_title
        
        return page_to_section

    def _process_ocr_page(self, page, page_num, section_title):
        try:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Get OCR data with confidence scores
            ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
            
            text_blocks = []
            confidences = []
            
            # Simple aggregation of words into a block
            current_line = []
            for i in range(len(ocr_data['text'])):
                word = ocr_data['text'][i].strip()
                conf = float(ocr_data['conf'][i])
                if word and conf > 0:
                    current_line.append(word)
                    confidences.append(conf)
                    
            if current_line:
                text = " ".join(current_line)
                avg_conf = sum(confidences) / len(confidences) if confidences else 0.0
                
                KnowledgeChunk.objects.create(
                    knowledge_pack=self.kp,
                    content_text=text,
                    chunk_type='core_text',
                    section_title=section_title,
                    start_page=page_num + 1,
                    end_page=page_num + 1,
                    ocr_confidence=avg_conf
                )
        except Exception as e:
            print(f"OCR failed for page {page_num + 1}: {e}")

    def _process_digital_page(self, page, blocks, page_num, section_title=None):
        for idx, block in enumerate(blocks):
            x0, y0, x1, y1, text, block_no, block_type = block
            
            if block_type == 0:  # Text
                clean_text = text.strip()
                if not clean_text:
                    continue
                chunk_type = self._classify_text_block(clean_text)
                KnowledgeChunk.objects.create(
                    knowledge_pack=self.kp,
                    content_text=clean_text,
                    chunk_type=chunk_type,
                    section_title=section_title,
                    bounding_box=[x0, y0, x1, y1],
                    start_page=page_num + 1,
                    end_page=page_num + 1,
                    order=idx
                )
            elif block_type == 1:  # Image
                try:
                    rect = fitz.Rect(x0, y0, x1, y1)
                    pix = page.get_pixmap(clip=rect)
                    img_data = pix.tobytes("png")
                    chunk = KnowledgeChunk(
                        knowledge_pack=self.kp,
                        chunk_type='diagram',
                        bounding_box=[x0, y0, x1, y1],
                        start_page=page_num + 1,
                        end_page=page_num + 1,
                        order=idx
                    )
                    filename = f"diagram_{self.kp.id}_p{page_num+1}_b{idx}.png"
                    chunk.image.save(filename, ContentFile(img_data), save=True)
                except Exception as e:
                    print(f"Failed to extract image block {idx} on page {page_num+1}: {e}")

    def _build_toc_structure(self, toc):
        structure = []
        last_topic = None
        for item in toc:
            if len(item) < 3: continue
            level, title, page = item[0], item[1], item[2]
            node = {
                'id': str(uuid.uuid4()),
                'title': title,
                'start_page': page,
                'type': 'topic' if level == 1 else 'unit',
                'source_type': 'native',
                'children': []
            }
            if level == 1:
                structure.append(node)
                last_topic = node
            elif level >= 2 and last_topic:
                node['type'] = 'unit'
                last_topic['children'].append(node)
        return structure

    @staticmethod
    def _heuristic_regex_recovery(doc, max_scan_pages=None):
        """
        Pure Non-LLM TOC Blueprint Recovery for Ingestion Sandbox.
        Mines the Table of Contents pages (pages 1 to 15) to extract Topics.
        Supports both:
          - "Chapter/Topic N: Title ...... 42"  (with page number)
          - "N. Title"  (no page number — page located by body-text scan)
        Enriches starting page numbers by cross-referencing with body text headings.
        """
        import re
        import uuid

        chapter_re = re.compile(
            r'^(?:Chapter|Topic|Unit|Module|Theme|Part|Section)\s+([0-9IVXLCDM]+)[:\.\-]?\s*(.*)$',
            re.IGNORECASE
        )
        chapter_fallback_re = re.compile(
            r'^([0-9IVXLCDM]+)[\.\:]\s*([A-Z][A-Za-z0-9\s\,\-\(\)\:\'\"]{2,})$',
            re.IGNORECASE
        )
        page_num_re = re.compile(r'^(.*?)\s*(?:[\.\\_\-]{2,}|\s{3,})\s*(\d+)$')

        total_pages = len(doc)
        toc_structure = []
        topic_dict = {}   # key → node
        topic_titles = [] # ordered list of (key, normalized_title) for body scan

        # STEP 1: Parse Table of Contents Pages (Pages 1 to 15)
        for page_num in range(min(15, total_pages)):
            page_text = doc[page_num].get_text()
            lines = [line.strip() for line in page_text.split('\n') if line.strip()]

            for line in lines:
                if line.lower() in ["table of contents", "contents", "page"]:
                    continue

                page_no = None
                clean_line = line

                page_match = page_num_re.match(line)
                if page_match:
                    clean_line = page_match.group(1).strip()
                    try:
                        page_no = int(page_match.group(2))
                    except ValueError:
                        pass

                # Master Topic Header (e.g. "Topic 1: Acids, Bases and Salts" or "1. Acids, Bases and Salts")
                chap_match = chapter_re.match(clean_line) or chapter_fallback_re.match(clean_line)
                if chap_match:
                    chap_num = chap_match.group(1)
                    chap_name = chap_match.group(2).strip() if len(chap_match.groups()) > 1 else ""

                    trailing_num = re.search(r'\s+(\d+)$', chap_name)
                    if trailing_num and not page_no:
                        try:
                            page_no = int(trailing_num.group(1))
                            chap_name = chap_name[:trailing_num.start()].strip()
                        except ValueError:
                            pass

                    full_title = f"Topic {chap_num}: {chap_name}" if chap_name else f"Topic {chap_num}"
                    key = str(chap_num).strip().lower()

                    if key in topic_dict:
                        if page_no:
                            topic_dict[key]['start_page'] = page_no
                    else:
                        node = {
                            'id': str(uuid.uuid4()),
                            'title': full_title,
                            'start_page': page_no,  # may be None — filled in Step 2
                            'type': 'topic',
                            'source_type': 'toc_blueprint',
                            'children': []
                        }
                        toc_structure.append(node)
                        topic_dict[key] = node
                        # Store normalized title for body-scan matching
                        if chap_name:
                            norm = re.sub(r'\s+', ' ', chap_name.lower().strip())
                            topic_titles.append((key, norm))

        # STEP 2a: Enrich page numbers via "Chapter N:" style body headings (original logic)
        if toc_structure:
            for page_num in range(total_pages):
                page_text = doc[page_num].get_text()
                lines = [l.strip() for l in page_text.split('\n') if l.strip()]

                for line in lines:
                    c_match = chapter_re.match(line) or chapter_fallback_re.match(line)
                    if c_match:
                        c_num = c_match.group(1)
                        key = str(c_num).strip().lower()
                        if key in topic_dict:
                            # Only update if current page is beyond front matter
                            existing = topic_dict[key]['start_page'] or 0
                            if existing <= 15 and page_num + 1 > 15:
                                topic_dict[key]['start_page'] = page_num + 1

        # STEP 2b: If topics correspond 1-to-1 with 'Objectives' topic boundaries, align them
        objective_pages = []
        for page_num in range(total_pages):
            if page_num + 1 > 5 and 'Objectives' in doc[page_num].get_text():
                objective_pages.append(page_num + 1)

        if len(objective_pages) == len(toc_structure):
            for idx, node in enumerate(toc_structure):
                node['start_page'] = objective_pages[idx]
        elif topic_titles:
            # STEP 2c: For topics that still have no real start_page, scan body for title text match
            for page_num in range(total_pages):
                page_text = doc[page_num].get_text()
                norm_page = re.sub(r'\s+', ' ', page_text.lower())

                for key, norm_title in topic_titles:
                    node = topic_dict.get(key)
                    if not node:
                        continue
                    existing = node['start_page'] or 0
                    if existing <= 15 and page_num + 1 > 15:
                        words = norm_title.split()[:5]
                        match_phrase = ' '.join(words)
                        if match_phrase and match_phrase in norm_page:
                            node['start_page'] = page_num + 1

        # STEP 3: Fall back to a reasonable page if still None
        for node in toc_structure:
            if not node['start_page']:
                node['start_page'] = 1

        return toc_structure

    @staticmethod
    def _classify_text_block(text):
        text_lower = text.lower().strip()
        if text_lower.startswith("definition:") or "is defined as" in text_lower: return 'definition'
        elif text_lower.startswith("example") or text_lower.startswith("worked example"): return 'worked_example'
        elif text_lower.startswith("exercise") or text_lower.startswith("question"): return 'exercise'
        elif text_lower.startswith("experiment") or text_lower.startswith("practical"): return 'practical'
        else: return 'core_text'

def process_textbook_pipeline(knowledge_pack_id):
    """
    Main orchestrator for Document Ingestion and Knowledge Repository Construction (Phase 2).
    """
    service = DocumentIngestionService(knowledge_pack_id)
    service.process()
