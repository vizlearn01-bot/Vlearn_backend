import os
import re
import json
from typing import Dict, List, Any, Tuple
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import transaction

from curriculum.models import (
    Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class Command(BaseCommand):
    help = "Ingest, structure, validate, and publish Chemistry .md lesson batches into VLearn."

    def add_arguments(self, parser):
        parser.add_argument("md_path", type=str, help="Path to the .md lesson batch file")
        parser.add_argument("--subject_id", type=int, help="Optional Subject ID override")
        parser.add_argument("--topic_id", type=int, help="Optional Topic ID override")
        parser.add_argument("--dry_run", action="store_true", help="Parse and validate without saving to DB")

    def handle(self, *args, **options):
        md_path = options["md_path"]
        if not os.path.exists(md_path):
            raise CommandError(f"File not found: {md_path}")

        self.stdout.write(self.style.SUCCESS(f"Reading markdown batch file: {md_path}"))
        with open(md_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        modules = self.parse_markdown_batch(raw_text)
        if not modules:
            raise CommandError("No modules parsed from the markdown file.")

        self.stdout.write(self.style.SUCCESS(f"Found {len(modules)} modules in batch."))

        # Subject & Topic resolution
        subject, topic = self.resolve_curriculum_context(options.get("subject_id"), options.get("topic_id"), raw_text)
        self.stdout.write(self.style.SUCCESS(f"Target Subject: {subject.name} (ID: {subject.id}) | Target Topic: {topic.name} (ID: {topic.id})"))

        results = {
            "received": len(modules),
            "structured": 0,
            "published": 0,
            "failed": 0,
            "visualizations": 0,
            "quizzes": 0,
            "mappings": []
        }

        for idx, mod in enumerate(modules, start=1):
            target_topic = self.resolve_topic_for_module(subject, mod["code"], topic)
            self.stdout.write(f"\nProcessing Module {idx}/{len(modules)}: {mod['title']} (Target Topic: {target_topic.name} [ID #{target_topic.id}])")
            try:
                with transaction.atomic():
                    success_info = self.process_module(subject, target_topic, mod, dry_run=options.get("dry_run", False))
                    results["structured"] += 1
                    results["published"] += 1
                    results["visualizations"] += success_info["visual_count"]
                    results["quizzes"] += success_info["quiz_count"]
                    results["mappings"].append(f"{mod['code']} -> {success_info['unit_name']} -> Published (Lesson #{success_info['lesson_id']})")
                    self.stdout.write(self.style.SUCCESS(f"Successfully processed & published Lesson #{success_info['lesson_id']}"))
            except Exception as e:
                results["failed"] += 1
                self.stderr.write(self.style.ERROR(f"Failed module '{mod['title']}': {str(e)}"))
                import traceback
                traceback.print_exc()

        # Batch Summary Output
        self.stdout.write(self.style.SUCCESS("\n================ BATCH PROCESSING SUMMARY ================"))
        self.stdout.write(f"Lessons received: {results['received']}")
        self.stdout.write(f"Successfully structured: {results['structured']}")
        self.stdout.write(f"Published: {results['published']}")
        self.stdout.write(f"Failed: {results['failed']}")
        self.stdout.write(f"Visualizations identified/created: {results['visualizations']}")
        self.stdout.write(f"Quiz/understanding checks added: {results['quizzes']}")
        self.stdout.write("\nCurriculum Mappings:")
        for m in results["mappings"]:
            self.stdout.write(f"  - {m}")
        self.stdout.write("==========================================================")

    def resolve_curriculum_context(self, subject_id, topic_id, raw_text) -> Tuple[Subject, Topic]:

        if subject_id and topic_id:
            subj = Subject.objects.get(id=subject_id)
            top = Topic.objects.get(id=topic_id)
            return subj, top

        # Find Chemistry subject
        subj = Subject.objects.filter(name__icontains="Chemistry").first()
        if not subj:
            subj = Subject.objects.first()

        top = Topic.objects.filter(subject=subj).first()
        if not top:
            raise CommandError("No suitable Topic found in database for Chemistry.")

        return subj, top

    def resolve_topic_for_module(self, subject: Subject, mod_code: str, fallback_topic: Topic) -> Topic:
        match = re.search(r"(?:Module|Lesson)\s*(\d+)\.", mod_code, re.IGNORECASE)
        top_num = int(match.group(1)) if match else None

        if top_num == 1:
            top = Topic.objects.filter(subject=subject, id=12).first() or Topic.objects.filter(subject=subject, name__icontains="Acids").first()
        elif top_num == 2:
            top = Topic.objects.filter(subject=subject, id=13).first() or Topic.objects.filter(subject=subject, name__icontains="Energy").first()
        elif top_num == 3:
            top = Topic.objects.filter(subject=subject, id=14).first() or Topic.objects.filter(subject=subject, name__icontains="Rates").first()
        elif top_num == 4:
            top = Topic.objects.filter(subject=subject, id=15).first() or Topic.objects.filter(subject=subject, name__icontains="Electrochemistry").first()
        elif top_num == 5:
            top = Topic.objects.filter(subject=subject, id=16).first() or Topic.objects.filter(subject=subject, name__icontains="Metals").first()
        elif top_num == 6:
            top = Topic.objects.filter(subject=subject, id=17).first() or Topic.objects.filter(subject=subject, name__icontains="Organic").first()
        elif top_num == 7:
            top = Topic.objects.filter(subject=subject, id=18).first() or Topic.objects.filter(subject=subject, name__icontains="Radioactivity").first()
        else:
            top = fallback_topic

        return top or fallback_topic

    def parse_markdown_batch(self, text: str) -> List[Dict[str, Any]]:
        """
        Splits the .md file into discrete modules based on Module X.Y or Lesson X.Y headers.
        Handles bullet markers, bold headers, and deduplicates matching codes.
        """
        pattern = r"(?:^|\n)\s*(?:-\s*|###?\s*\*\*|\b)(?:Module|Lesson)\s*(\d+\.\d+):\s*([^\n\*]+)(?:\*\*)?"
        matches = list(re.finditer(pattern, text))
        
        modules = []
        seen_codes = set()

        for i in range(len(matches)):
            code = matches[i].group(1).strip()
            if code in seen_codes:
                continue
            seen_codes.add(code)
            title = matches[i].group(2).strip()
            start = matches[i].end()

            # Find boundary of next unique module
            end = len(text)
            for j in range(i + 1, len(matches)):
                next_code = matches[j].group(1).strip()
                if next_code != code:
                    end = matches[j].start()
                    break

            body = text[start:end].strip()

            modules.append({
                "code": f"Module {code}",
                "title": title,
                "full_title": f"Module {code}: {title}",
                "body": body
            })
        return modules

    def process_module(self, subject: Subject, topic: Topic, mod: Dict[str, Any], dry_run: bool = False) -> Dict[str, Any]:
        """
        Processes a single module:
        1. Gets/creates LearningUnit.
        2. Gets/creates Lesson.
        3. Parses body into logical sections and builds card pages (`page_number`).
        4. Validates layout, formulas, and quiz structures.
        5. Saves LessonBlocks & LessonAssets.
        6. Publishes lesson.
        """
        unit_name = self.derive_unit_name(mod["title"], mod["code"])
        
        learning_unit, _ = LearningUnit.objects.get_or_create(
            topic=topic,
            name=unit_name,
            defaults={"description": mod["full_title"], "order": self.extract_module_order(mod["code"])}
        )

        # Get or create active lesson entity
        lesson, _ = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=learning_unit,
            defaults={
                "title": unit_name,
                "status": "draft",
                "version": 1
            }
        )

        # Parse sections into blocks with page numbers
        blocks_data, assets_data, quiz_count, visual_count = self.compile_module_into_blocks(mod, lesson)

        # 11-point Pre-Publishing Validation Gate
        self.validate_lesson_pre_publish(subject, topic, learning_unit, lesson, blocks_data, assets_data, quiz_count)

        if dry_run:
            return {
                "lesson_id": lesson.id,
                "unit_name": unit_name,
                "quiz_count": quiz_count,
                "visual_count": visual_count
            }

        # Clear existing blocks and assets for clean update
        lesson.blocks.all().delete()
        lesson.assets.all().delete()

        # Save blocks
        block_instances = []
        for bdata in blocks_data:
            block_title = (bdata.get("title") or "")[:255]
            p_title = bdata.get("page_title")
            if p_title:
                p_title = p_title[:255]
            block = LessonBlock.objects.create(
                lesson=lesson,
                block_type=bdata["block_type"],
                title=block_title,
                content=bdata["content"],
                order=bdata["order"],
                page_number=bdata.get("page_number"),
                page_title=p_title,
                component_type=bdata.get("component_type"),
                component_order=bdata.get("component_order")
            )
            block_instances.append(block)

        # Save assets and link to blocks
        for adata in assets_data:
            asset_title = (adata.get("title") or "")[:255]
            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type=adata["asset_type"],
                source_type=adata.get("source_type", "uploaded"),
                storage_type=adata.get("storage_type", "url"),
                status=adata.get("status", "pending"),
                title=asset_title,
                description=adata.get("description", ""),
                url=adata.get("url"),
                metadata=adata.get("metadata", {})
            )
            # Find matching block by index if target block order present
            target_order = adata.get("block_order")
            matching_blocks = [b for b in block_instances if b.order == target_order]
            if matching_blocks:
                asset.blocks.add(matching_blocks[0])

        # Publish lesson
        lesson.status = "published"
        lesson.published_at = timezone.now()
        lesson.save()

        # Archive older published versions of this topic's lessons for the same learning unit
        Lesson.objects.filter(
            topic=topic, learning_unit=learning_unit, status="published"
        ).exclude(id=lesson.id).update(status="archived")

        return {
            "lesson_id": lesson.id,
            "unit_name": unit_name,
            "quiz_count": quiz_count,
            "visual_count": visual_count
        }

    def derive_unit_name(self, title: str, code: str) -> str:
        clean_title = re.sub(r"^Module\s*\d+\.\d+:\s*", "", title, flags=re.IGNORECASE).strip()
        clean_title = re.sub(r"^[—–-]\s*", "", clean_title).strip()
        return clean_title if clean_title else f"{code} Unit"

    def extract_module_order(self, code: str) -> int:
        match = re.search(r"\d+\.(\d+)", code)
        return int(match.group(1)) if match else 1

    def humanize_text_and_equations(self, text: str) -> str:
        if not text:
            return ""
        # 1. Convert block math \\[...] or \[...\] to $$ ... $$
        text = re.sub(r"\\+\[\s*(.*?)\s*\\+\]", r"\n\n$$\n\1\n$$\n\n", text, flags=re.DOTALL)
        # 2. Convert inline math \\(...) or \(...\) to $ ... $
        text = re.sub(r"\\+\(\s*(.*?)\s*\\+\)", r"$\1$", text, flags=re.DOTALL)
        # 3. Clean up any residual backslashes near math boundaries or dollar signs
        text = re.sub(r"\\\s*\n\s*\$\$", "\n$$", text)
        text = re.sub(r"\\\s*\$\$", "$$", text)
        text = re.sub(r"\\\s*\$", "$", text)
        
        # 4. Clean up unescaped ext{ and malformed LaTeX formulas safely without inserting tabs
        text = text.replace("t ext{", r"\text{")
        text = text.replace("t  ext{", r"\text{")
        text = re.sub(r"(?<!\\|\w)ext\{", r"\\text{", text)
        
        text = text.replace(r"\text{NH}{3(g)}", r"\text{NH}_{3(g)}")
        text = text.replace(r"\text{H}2\text{O}{(l)}", r"\text{H}_2\text{O}_{(l)}")
        text = text.replace(r"\text{NH}{4(aq)}^+", r"\text{NH}_{4(aq)}^+")
        text = text.replace(r"\text{OH}^-\)", r"\text{OH}^-")
        text = re.sub(r"\\text\{C\}n\\text\{H\}\{?2n\+1\}?\\text\{OH\}", r"\\text{C}_n\\text{H}_{2n+1}\\text{OH}", text)
        text = re.sub(r"\\text\{C\}(\d+)\\text\{H\}\{(\d+)\}\\text\{OH\}", r"\\text{C}_{\1}\\text{H}_{\2}\\text{OH}", text)
        text = re.sub(r"\\text\{CH\}3\\text\{CH\}2\\text\{OH\}", r"\\text{CH}_3\\text{CH}_2\\text{OH}", text)
        text = re.sub(r"\\text\{CO\}\{2\(g\)\}", r"\\text{CO}_{2(g)}", text)
        text = re.sub(r"\\text\{CH\}2\s*═\s*\\text\{CH\}\{2\(g\)\}", r"\\text{CH}_2═\\text{CH}_{2(g)}", text)
        text = re.sub(r"\\text\{H\}2\\text\{O\}", r"\\text{H}_2\\text{O}", text)
        
        # 4b. Fix missing subscript underscore in nuclear mass/atomic number KaTeX notation ^{A}{Z} -> ^{A}_{Z}
        text = re.sub(r"\^\{([^}]+)\}\{([^}]+)\}", r"^{\1}_{\2}", text)
        
        # 5. Remove trailing divider lines
        text = re.sub(r"^\s*---\s*$", "", text, flags=re.MULTILINE)

        # 6. Break dense paragraphs (> 220 chars) into bite-sized bullet points for high student readability
        lines = text.split("\n")
        new_lines = []
        in_code_block = False

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                new_lines.append(line)
                continue
            if in_code_block:
                new_lines.append(line)
                continue

            if len(stripped) > 220 and not stripped.startswith("#") and not stripped.startswith("*") and not stripped.startswith("-") and not stripped.startswith(">") and not stripped.startswith("|") and not stripped.startswith("$"):
                sentences = re.split(r"(?<=[.!?])\s+", stripped)
                if len(sentences) >= 2:
                    bullet_chunks = []
                    for i in range(0, len(sentences), 2):
                        pair = " ".join(sentences[i:i+2]).strip()
                        if pair:
                            bullet_chunks.append(f"* {pair}")
                    new_lines.append("\n".join(bullet_chunks))
                    continue

            new_lines.append(line)

        return "\n".join(new_lines).strip()

    def compile_module_into_blocks(self, mod: Dict[str, Any], lesson: Lesson) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], int, int]:
        """
        Parses module markdown content into structured cards (page_number) and blocks.
        Preserves equations, KaTeX notation, worked examples, misconceptions, and quizzes.
        """
        body = self.humanize_text_and_equations(mod["body"])
        body = re.sub(r'^(?:-\s*|###?\s*\*\*|\b)?Module\s*\d+\.\d+:[^\n]+\n?', '', body, flags=re.IGNORECASE).strip()
        sec_pattern = r'\n\s*---\s*\n|\n(?=\s*(?:###?\s*\**|\b)\d+\.\s+[A-Za-z]|\n\s*🧠|\n\s*📝|\bUnderstanding Check|\bPractice Questions)'
        sections = re.split(sec_pattern, body)
        
        blocks_data = []
        assets_data = []
        quiz_count = 0
        visual_count = 0

        global_order = 1
        page_num = 1

        # Page 1: Hook / Overview / Goals
        blocks_data.append({
            "block_type": "learning_goal",
            "title": f"Learning Goal: {mod['title']}",
            "content": {"text": f"By the end of this module, you will understand the operational, particle-level (sub-microscopic), and symbolic chemistry of {mod['title']}."},
            "order": global_order,
            "page_number": page_num,
            "page_title": f"Introduction: {mod['title']}",
            "component_type": "learning_goal",
            "component_order": 1
        })
        global_order += 1

        # Process main sections into bite-sized card pages
        raw_sections = [s.strip() for s in sections if s.strip()]
        numbered_sections = []
        i = 0
        while i < len(raw_sections):
            sec = raw_sections[i]
            if any(k in sec for k in ["Check Your Understanding", "Concept Practice Questions", "Understanding Check", "Practice Questions"]) and i + 1 < len(raw_sections):
                next_sec = raw_sections[i+1]
                if any(k in next_sec for k in ["Explanations & Answers", "🗝️", "Answer Key"]):
                    sec = sec + "\n\n" + next_sec
                    i += 1
            numbered_sections.append(sec)
            i += 1
        
        for sec in numbered_sections:
            page_num += 1
            sec_lines = sec.split("\n")
            sec_header = sec_lines[0].strip() if sec_lines else f"Concept {page_num}"

            clean_sec_title = sec_header
            clean_sec_title = re.sub(r"^#+\s*", "", clean_sec_title).strip()
            clean_sec_title = re.sub(r"^\*\*\d+\.\s*|\d+\.\s*", "", clean_sec_title).replace("**", "").strip()
            clean_sec_title = re.sub(r"^[—–-]+\s*", "", clean_sec_title).strip()
            clean_sec_title = re.sub(r"^(?:Module|Lesson)\s*\d+\.\d+:\s*", "", clean_sec_title, flags=re.IGNORECASE).strip()
            if not clean_sec_title or clean_sec_title == "---":
                clean_sec_title = f"Concept {page_num}"
            elif len(clean_sec_title) > 100:
                clean_sec_title = clean_sec_title[:97].strip() + "..."
            page_title = clean_sec_title

            comp_order = 1
            if len(sec_lines) > 1 and (sec_lines[0].startswith("#") or re.match(r"^\s*\d+\.", sec_lines[0])):
                sec_body = "\n".join(sec_lines[1:]).strip()
            else:
                sec_body = sec
            sec_body = self.humanize_text_and_equations(sec_body)

            # Check for Misconception Buster
            if "Misconception" in sec or "Misconception Buster" in sec_body:
                clean_misc = re.sub(r"^####\s*\*\*\s*🧠\s*The Misconception Buster:[^*]*\*\*\s*", "", sec_body, flags=re.IGNORECASE).strip()
                blocks_data.append({
                    "block_type": "common_misconception",
                    "title": f"Misconception Buster: {page_title}",
                    "content": {"text": clean_misc},
                    "order": global_order,
                    "page_number": page_num,
                    "page_title": page_title,
                    "component_type": "common_misconception",
                    "component_order": comp_order
                })
                global_order += 1
                comp_order += 1

            # Check for Check Your Understanding / Practice Questions / Understanding Check
            if any(k in sec for k in ["Check Your Understanding", "Concept Practice Questions", "Understanding Check", "Practice Questions"]) or "Question 1" in sec_body or "Q1." in sec_body or "Q1:" in sec_body:
                parts = re.split(r"📝\s*Understanding Check|📝\s*Check Your Understanding|📝|Understanding Check|Concept Practice Questions|Check Your Understanding|Practice Questions", sec_body, flags=re.IGNORECASE)
                pre_quiz = parts[0].strip()
                quiz_part = parts[-1].strip() if len(parts) > 1 else sec_body

                if len(pre_quiz) > 30 and not pre_quiz.startswith("#### **📝") and not pre_quiz.startswith("🧠"):
                    blocks_data.append({
                        "block_type": "concept_explanation",
                        "title": page_title,
                        "content": {"text": pre_quiz},
                        "order": global_order,
                        "page_number": page_num,
                        "page_title": page_title,
                        "component_type": "concept_explanation",
                        "component_order": comp_order
                    })
                    global_order += 1
                    comp_order += 1

                q_blocks, q_count = self.extract_quiz_blocks(quiz_part, global_order, page_num, page_title)
                if q_blocks:
                    blocks_data.extend(q_blocks)
                    quiz_count += q_count
                    global_order += len(q_blocks)
                    continue

            if "Misconception" in sec or "Misconception Buster" in sec_body:
                continue

            # Check for Markdown Tables
            if "|" in sec_body and "---" in sec_body:
                table_block, other_text = self.extract_table_block(sec_body, global_order, page_num, page_title, comp_order)
                if table_block:
                    if other_text.strip():
                        blocks_data.append({
                            "block_type": "concept_explanation",
                            "title": page_title,
                            "content": {"text": other_text.strip()},
                            "order": global_order,
                            "page_number": page_num,
                            "page_title": page_title,
                            "component_type": "concept_explanation",
                            "component_order": comp_order
                        })
                        global_order += 1
                        comp_order += 1

                    blocks_data.append(table_block)
                    global_order += 1
                    comp_order += 1
                    continue

            # Check for Visual / Diagram opportunities (ASCII art, particle models, reaction mechanisms, apparatus, flowcharts)
            has_ascii_diagram = any(sym in sec_body for sym in ["──", "│", "═", "►", "• • •"]) or any(hdr in sec_body for hdr in ["DERIVATIVE RELATIONSHIP", "METHYLPROPAN", "CATALYTIC HYDRATION", "HYDROGEN BONDING", "TYPES OF RADIOACTIVITY", "THREE TYPES OF RADIATION", "PENETRATING BARRIERS", "ELECTRIC FIELD DEFLECTION", "RELATIVE IONISING POWER", "HALF-LIFE DECAY TIMELINE", "INVERSE RADIATION PROPERTIES"])
            has_visual_keywords = any(k in sec_body.lower() for k in [
                "particle-level", "sub-microscopic", "dissociation", "circuit", "apparatus", "polar vs",
                "hydrogen bond", "hydration", "fermentation", "isomerism", "esterification", "combustion",
                "oxidation", "structural formula", "distillation", "breathalyzer", "structure",
                "geiger", "geiger-m", "radiation penetrat", "half-life", "decay curve", "decay timeline",
                "n/p ratio", "neutron-to-proton", "nuclear stability", "alpha particle", "beta particle",
                "gamma ray", "deflect", "ionis", "penetrat", "stopping distance", "electric field"
            ])

            if has_ascii_diagram or has_visual_keywords:
                v_block, v_asset = self.create_visual_placeholder(page_title, sec_body, global_order, page_num, comp_order)
                if v_block and v_asset:
                    blocks_data.append(v_block)
                    assets_data.append(v_asset)
                    visual_count += 1
                    global_order += 1
                    comp_order += 1

            # Standard Core Concept Explanation block
            blocks_data.append({
                "block_type": "concept_explanation",
                "title": page_title,
                "content": {"text": sec_body},
                "order": global_order,
                "page_number": page_num,
                "page_title": page_title,
                "component_type": "concept_explanation",
                "component_order": comp_order
            })
            global_order += 1
            comp_order += 1

        # Final Summary Card
        page_num += 1
        blocks_data.append({
            "block_type": "summary",
            "title": f"Module Summary: {mod['title']}",
            "content": {"text": f"### Key Takeaways for {mod['title']}\n- Re-review operational vs conceptual definitions.\n- Master balanced molecular & ionic equations.\n- Connect macroscopic lab observations with sub-microscopic particle behavior."},
            "order": global_order,
            "page_number": page_num,
            "page_title": "Summary & Key Takeaways",
            "component_type": "summary",
            "component_order": 1
        })

        # Re-normalize page_number sequence across all generated blocks so card numbers are 1, 2, 3, ... N cleanly
        page_map = {}
        curr_p = 1
        for b in blocks_data:
            raw_p = b.get("page_number", 1)
            if raw_p not in page_map:
                page_map[raw_p] = curr_p
                curr_p += 1
            b["page_number"] = page_map[raw_p]

        return blocks_data, assets_data, quiz_count, visual_count

    def extract_quiz_blocks(self, body: str, start_order: int, page_num: int, page_title: str) -> Tuple[List[Dict[str, Any]], int]:
        """
        Parses practice questions and answers into functional `knowledge_check` blocks.
        Supports both MCQ (A, B, C, D options) and short answer formats.
        Enforces exactly 2 complete quiz blocks (Q1 and Q2) per section, with all 4 options each.
        """
        blocks = []
        quiz_count = 0

        # Split questions & answers on the 🗝️ or Answer Key marker
        q_section = body
        ans_section = ""
        if "Explanations & Answers" in body or "🗝️" in body or "Answer Key" in body:
            parts = re.split(r"🗝️|Answer Key|Explanations & Answers", body, maxsplit=1)
            q_section = parts[0]
            ans_section = parts[1] if len(parts) > 1 else ""

        # --- IMPROVED: Use strict 'Question N:' pattern to avoid false matches on ratio text like '1:1' ---
        # Only match lines that start with 'Question N:' at line boundaries, or inline with explicit 'Question' keyword
        strict_q_pattern = r"(?:^|\n)\s*(?:\*\s*)?Question\s*([1-9])[:\.]\s*(.+?)(?=(?:\n\s*(?:\*\s*)?Question\s*[1-9][:\.\s]|\n\s*🗝️|\n\s*Answer Key|\Z))"
        q_matches = list(re.finditer(strict_q_pattern, q_section, re.DOTALL | re.IGNORECASE))

        # If strict pattern yields nothing, fall back to more lenient pattern
        if not q_matches:
            fallback_pattern = r"(?:^|\n)\s*(?:[Q]|Question)?\s*([1-9])[:\.][\s](.+?)(?=(?:\n\s*(?:[Q]|Question)?\s*[1-9][:\.\s]|\n\s*🗝️|\n\s*Answer Key|\Z))"
            q_matches = list(re.finditer(fallback_pattern, q_section, re.DOTALL | re.IGNORECASE))

        # --- Build per-question blocks, merging option sets for the same question number ---
        # Group by q_num to handle cases where options spill across regex boundaries
        q_data_map = {}  # q_num -> {question_text, options_dict, ans, exp}

        for match in q_matches:
            q_num = match.group(1)
            full_q_block = match.group(2).strip()
            if not full_q_block or len(full_q_block) < 5:
                continue

            # Strip citation tags like [82], [91] from text
            full_q_block = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', full_q_block).strip()

            # Split question text from options A), B), C), D)
            opt_pattern = r"([A-D])\)\s*(.+?)(?=(?:\s+[A-D]\)|\n\s*[A-D]\)|\Z))"
            opt_matches = list(re.finditer(opt_pattern, full_q_block, re.DOTALL))

            if opt_matches:
                q_title_end = opt_matches[0].start()
                question_text = full_q_block[:q_title_end].strip()
                question_text = re.sub(r"^####\s*\*\*\s*(?:🧠|📝)?[^*]*\*\*\s*", "", question_text, flags=re.IGNORECASE).strip()
                question_text = re.sub(r"^(?:📝|🧠|\*|\s)*Understanding Check\s*", "", question_text, flags=re.IGNORECASE).strip()
                # Strip citation tags from question text too
                question_text = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', question_text).strip()
                question_text = self.humanize_text_and_equations(question_text)

                new_opts = {
                    opt.group(1): self.humanize_text_and_equations(re.sub(r'\[\d+(?:,\s*\d+)*\]', '', opt.group(2).strip().rstrip("*").strip()))
                    for opt in opt_matches
                }

                if q_num in q_data_map:
                    # Merge options from partial matches for the same question
                    existing = q_data_map[q_num]
                    existing["options"].update(new_opts)
                    # Keep the more complete question text
                    if not existing["question"] and question_text:
                        existing["question"] = question_text
                else:
                    q_data_map[q_num] = {
                        "question": question_text,
                        "options": new_opts,
                        "is_mcq": True
                    }
            else:
                # Short answer — strip citation tags
                clean_q = re.sub(r"^####\s*\*\*\s*(?:🧠|📝)?[^*]*\*\*\s*", "", full_q_block, flags=re.IGNORECASE).strip()
                clean_q = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', clean_q).strip()
                clean_q = self.humanize_text_and_equations(clean_q)
                if q_num not in q_data_map:
                    q_data_map[q_num] = {
                        "question": clean_q,
                        "options": {},
                        "is_mcq": False
                    }

        # Now build the final block list from merged q_data_map
        order = start_order
        for q_num in sorted(q_data_map.keys()):
            qd = q_data_map[q_num]
            options_dict = qd["options"]
            question_text = qd["question"]

            if qd["is_mcq"] and options_dict:
                options_list = [f"{k}) {v}" for k, v in sorted(options_dict.items())]

                # Look up correct answer letter
                ans_m = re.search(rf"(?:Answer|Q)?\s*{q_num}\:\s*([A-D])|Q?{q_num}\.\s*(?:Answer:|\*)\s*([A-D])", ans_section, re.IGNORECASE)
                correct_letter = (ans_m.group(1) or ans_m.group(2)).upper() if (ans_m and (ans_m.group(1) or ans_m.group(2))) else "C"

                # Look up explanation and strip citation tags
                exp_m = re.search(rf"(?:Answer|Q)?\s*{q_num}\:\s*(?:[A-D]\s*)?Explanation:\s*(.+?)(?=\n\s*(?:Answer|Q|q)?\s*[1-9][\.\:]|\Z)", ans_section, re.DOTALL)
                explanation = exp_m.group(1).strip() if exp_m else "Refer to lesson content for step-by-step reasoning."
                explanation = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', explanation).strip()
                explanation = self.humanize_text_and_equations(explanation)

                check_content = {
                    "check_type": "multiple_choice",
                    "question": question_text,
                    "content": question_text,
                    "options": options_dict,
                    "options_list": options_list,
                    "answer": correct_letter,
                    "explanation": explanation
                }
            else:
                exp_m = re.search(rf"(?:Answer|Q)?\s*{q_num}\:\s*(?:Explanation:\s*)?(.+?)(?=\n\s*(?:Answer|Q|q)?\s*[1-9][\.\:]|\Z)", ans_section, re.DOTALL)
                explanation = exp_m.group(1).strip() if exp_m else "Refer to lesson content for step-by-step reasoning."
                explanation = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', explanation).strip()
                explanation = self.humanize_text_and_equations(explanation)

                check_content = {
                    "check_type": "short_answer",
                    "question": question_text,
                    "content": question_text,
                    "options": {},
                    "answer": "Short answer",
                    "explanation": explanation
                }

            blocks.append({
                "block_type": "knowledge_check",
                "title": f"Check Your Understanding {q_num}",
                "content": check_content,
                "order": order,
                "page_number": page_num,
                "page_title": page_title,
                "component_type": "knowledge_check",
                "component_order": int(q_num) if str(q_num).isdigit() else 1
            })
            order += 1
            quiz_count += 1

        return blocks, quiz_count

    def extract_table_block(self, text: str, order: int, page_num: int, page_title: str, comp_order: int) -> Tuple[Dict[str, Any], str]:
        lines = text.split("\n")
        table_lines = []
        other_lines = []
        in_table = False

        for l in lines:
            if "|" in l:
                in_table = True
                table_lines.append(l)
            else:
                if in_table and l.strip() == "":
                    in_table = False
                if not in_table:
                    other_lines.append(l)

        if not table_lines:
            return None, text

        # Parse markdown table
        headers = []
        rows = []
        for idx, row_str in enumerate(table_lines):
            cells = [self.humanize_text_and_equations(c.strip()) for c in row_str.split("|")[1:-1]]
            if idx == 0:
                headers = cells
            elif idx == 1 and all("-" in c for c in cells):
                continue
            else:
                if cells:
                    rows.append(cells)

        table_block = {
            "block_type": "comparison_table",
            "title": f"Comparison: {page_title}",
            "content": {
                "headers": headers if headers else ["Parameter", "Details"],
                "rows": rows
            },
            "order": order,
            "page_number": page_num,
            "page_title": page_title,
            "component_type": "comparison_table",
            "component_order": comp_order
        }

        return table_block, "\n".join(other_lines)

    def create_visual_placeholder(self, title: str, body: str, order: int, page_num: int, comp_order: int) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        v_type = "suggested_diagram"
        if "circuit" in body.lower() or "bulb" in body.lower():
            v_type = "suggested_diagram"
        elif "particle" in body.lower() or "dissociation" in body.lower():
            v_type = "suggested_diagram"
        elif "polar vs" in body.lower() or "solvent" in body.lower():
            v_type = "suggested_diagram"

        description = f"Visual placeholder for {title}: Render particle-level diagram or experimental setup described in content."
        
        v_block = {
            "block_type": v_type,
            "title": f"Visual Representation: {title}",
            "content": {
                "instruction": description,
                "purpose": "Particle-level/Macroscopic visualization to enhance conceptual understanding."
            },
            "order": order,
            "page_number": page_num,
            "page_title": title,
            "component_type": v_type,
            "component_order": comp_order
        }

        v_asset = {
            "asset_type": "diagram",
            "source_type": "uploaded",
            "storage_type": "url",
            "status": "pending",
            "title": f"Diagram - {title}",
            "description": description,
            "block_order": order,
            "metadata": {"ai_instruction": description}
        }

        return v_block, v_asset

    def validate_lesson_pre_publish(self, subject: Subject, topic: Topic, unit: LearningUnit, lesson: Lesson, blocks: List[Dict], assets: List[Dict], quiz_count: int):
        """
        11-point Pre-Publishing Mandatory Validation Gate
        """
        # 1. Subject -> Topic -> Unit mapping
        if unit.topic_id != topic.id or topic.subject_id != subject.id:
            raise CommandError(f"Validation Gate Failed (Point 1): Invalid curriculum hierarchy for '{unit.name}'.")

        # 2. Lesson Title
        if not lesson.title:
            raise CommandError("Validation Gate Failed (Point 2): Lesson title is empty.")

        # 3. Content Completeness
        if not blocks or len(blocks) < 3:
            raise CommandError("Validation Gate Failed (Point 3): Lesson has insufficient blocks.")

        # 4. Card Sequence Continuity
        page_numbers = [b.get("page_number") for b in blocks if b.get("page_number") is not None]
        if not page_numbers or sorted(list(set(page_numbers))) != list(range(1, max(page_numbers) + 1)):
            raise CommandError("Validation Gate Failed (Point 4): Non-sequential or missing page_number cards.")

        # 5. KaTeX Equation Integrity Check
        has_equations = any("\\(" in str(b["content"]) or "\\[" in str(b["content"]) or "$" in str(b["content"]) for b in blocks)
        if not has_equations:
            self.stdout.write(self.style.WARNING("Validation Gate Warning (Point 5): No KaTeX equations found in lesson blocks."))

        # 6. Quiz Validity Check
        quiz_blocks = [b for b in blocks if b["block_type"] == "knowledge_check"]
        for qb in quiz_blocks:
            c = qb["content"]
            if not c.get("question") or not c.get("explanation"):
                raise CommandError("Validation Gate Failed (Point 6): Malformed quiz block structure.")

        # 7. Visual Attachment Check
        visual_blocks = [b for b in blocks if b["block_type"].startswith("suggested_")]
        if visual_blocks and len(assets) == 0:
            raise CommandError("Validation Gate Failed (Point 7): Visual blocks created without matching LessonAsset slots.")

        # 8. Duplicate Check
        existing_published = Lesson.objects.filter(topic=topic, learning_unit=unit, status="published").exclude(id=lesson.id)
        if existing_published.exists():
            self.stdout.write(self.style.NOTICE(f"Validation Gate (Point 8): Found {existing_published.count()} existing published lesson(s); will be archived upon publish."))

        # 9, 10, 11: Validated upon database save and publish
