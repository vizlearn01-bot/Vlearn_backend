"""
TopicModuleGenerationAgent
--------------------------
Given a KnowledgePack whose text chunks have been extracted,
this agent calls the LLM to infer a sensible Topic → LearningUnit
hierarchy and persists the records under the KP's Subject.

The agent intentionally does NOT approve the KP — that remains a
human step.  It simply pre-populates the hierarchy so the reviewer
can inspect and amend it before approval.
"""
import json
import logging
import uuid
from typing import List

from pydantic import BaseModel, Field

from ai_infrastructure.llm_factory import LLMFactory

logger = logging.getLogger("curriculum.ai_ingestion")


# ---------------------------------------------------------------------------
# Pydantic schema for LLM output
# ---------------------------------------------------------------------------

class GeneratedUnit(BaseModel):
    name: str = Field(description="Title for the individual lesson (e.g. 'Lesson 1: Symptoms of Nitrogen Deficiency').")
    description: str = Field(description="One-sentence learning outcome explaining what students will master in this lesson.")


class GeneratedTopic(BaseModel):
    name: str = Field(description="Name of the modular study topic (e.g. 'Soil Fertility & Management', 'Cereal Crop Diseases').")
    units: List[GeneratedUnit] = Field(description="Bite-sized lessons (learning units) belonging to this topic.")


class AiIngestionResult(BaseModel):
    topics: List[GeneratedTopic] = Field(description="The complete inferred topic/lesson hierarchy.")
    notes: str = Field(default="", description="Optional notes about coverage, chapter boundaries, or confidence.")


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

SYSTEM_INSTRUCTION = (
    "You are an expert curriculum architect designing interactive online courses.\n"
    "Your goal is to transform textbook content into a modular, bite-sized Topic → Learning Unit (Lesson) structure.\n\n"
    "CRITICAL RULES:\n"
    "1. AVOID GIANT META-TOPICS: Do NOT combine multiple chapters into one meta-topic. Promote distinct themes into separate, focused TOPICS.\n"
    "2. TOPICS: Must represent clear, focused thematic modules (e.g. 'Acids, Bases & Salts', 'Electrochemistry', 'Organic Chemistry'). Aim for 5–15 topics depending on textbook depth.\n"
    "3. LEARNING UNITS (LESSONS): Each learning unit is an individual 15–30 minute lesson covering a specific subtopic, mechanism, calculation, or experiment.\n"
    "4. COMPREHENSIVE LESSON BREAKDOWN: Each Topic should contain between 3 to 6 distinct, granular Learning Units (Lessons) to ensure thorough curriculum coverage.\n"
    "5. Keep all titles clear, engaging, and concise (≤ 60 characters).\n"
    "6. Do NOT invent unrelated content — infer directly from the extracted text and chapter outline.\n"
    "7. Output MUST conform strictly to the AiIngestionResult JSON schema.\n"
)


class TopicModuleGenerationAgent:
    """
    Agent that infers a Topic/LearningUnit hierarchy from extracted KnowledgePack chunks.
    """

    @staticmethod
    def run(knowledge_pack_id: int) -> AiIngestionResult:
        """
        Run the agent for a given KnowledgePack ID.

        1. Fetches extracted chunks from the KP.
        2. Builds a concise summary prompt from section titles + chunk types.
        3. Calls LLM for structured output (AiIngestionResult).
        4. Persists Topic + LearningUnit records under the KP's Subject.
        5. Updates KP.generation_metadata with the result summary.

        Returns the AiIngestionResult for logging / task metadata.
        """
        from curriculum.models import KnowledgePack, Topic, LearningUnit

        kp = KnowledgePack.objects.select_related('subject').get(id=knowledge_pack_id)
        chunks = kp.chunks.all().order_by('order')

        if not chunks.exists():
            logger.warning(
                "[AIIngestion] KP %d has no chunks yet — skipping hierarchy generation.", knowledge_pack_id
            )
            return AiIngestionResult(topics=[], notes="No chunks available for analysis.")

        # Build a compact representation of the textbook structure
        toc_lines = []
        seen_sections = set()
        for chunk in chunks:
            section = chunk.section_title or ""
            entry = f"[{chunk.chunk_type}] {section} (p{chunk.start_page}–{chunk.end_page})"
            if section and section not in seen_sections:
                seen_sections.add(section)
                toc_lines.append(entry)
            if len(toc_lines) >= 200:  # cap to avoid huge prompts
                break

        # Fallback 1: Use Stage-1 extracted_structure TOC if available
        if not toc_lines and kp.extracted_structure:
            for item in kp.extracted_structure:
                title = item.get('title', '')
                page = item.get('start_page', 1)
                toc_lines.append(f"[topic] {title} (p{page})")
                for child in item.get('children', []):
                    c_title = child.get('title', '')
                    c_page = child.get('start_page', page)
                    toc_lines.append(f"  - [unit] {c_title} (p{c_page})")

        # Fallback 2: Sample text chunks across the book
        if not toc_lines:
            sample_chunks = chunks[:40]
            for c in sample_chunks:
                text_sample = (c.content_text or "").strip()[:100].replace("\n", " ")
                if text_sample:
                    toc_lines.append(f"[p{c.start_page}] {text_sample}")

        toc_text = "\n".join(toc_lines) if toc_lines else "No section titles or content available."

        prompt = (
            f"Textbook: {kp.subject.name}\n\n"
            f"Extracted table of contents / section summary:\n"
            f"---\n{toc_text}\n---\n\n"
            f"Based on the above, generate a Topic → Learning Unit hierarchy."
        )

        logger.info(
            "[AIIngestion] Calling LLM for KP %d (%d sections sampled).",
            knowledge_pack_id, len(toc_lines)
        )

        provider = LLMFactory.get_provider()
        result: AiIngestionResult = provider.generate_structured(
            prompt=prompt,
            response_schema=AiIngestionResult,
            system_instruction=SYSTEM_INSTRUCTION,
        )

        if not isinstance(result, AiIngestionResult):
            result = AiIngestionResult.model_validate(result)

        # Preserve Stage-1 TOC data before overwriting (used for page-number lookup)
        stage1_structure = list(kp.extracted_structure or [])

        # Build a normalized title → start_page lookup from the Stage-1 TOC
        import re as _re
        toc_page_map = {}  # normalized_title → start_page
        for node in stage1_structure:
            title = (node.get('title') or '').strip()
            page = node.get('start_page') or 1
            norm = _re.sub(r'\s+', ' ', title.lower())
            if norm:
                toc_page_map[norm] = page
            for child in node.get('children', []):
                c_title = (child.get('title') or '').strip()
                c_page = child.get('start_page') or page
                c_norm = _re.sub(r'\s+', ' ', c_title.lower())
                if c_norm:
                    toc_page_map[c_norm] = c_page

        def _lookup_page(name: str, fallback: int = 1) -> int:
            """Find the best start_page for an AI-generated name from the TOC map."""
            norm = _re.sub(r'[^\w\s]', '', name.lower().strip())
            # Direct match
            for toc_norm, page in toc_page_map.items():
                cleaned_toc = _re.sub(r'topic\s+\d+:\s*', '', toc_norm)
                cleaned_toc = _re.sub(r'[^\w\s]', '', cleaned_toc).strip()
                if norm == cleaned_toc or norm in cleaned_toc or cleaned_toc in norm:
                    return page

            # Keyword-set overlap scoring
            stop_words = {'and', 'in', 'the', 'of', 'for', 'to', 'a', 'an', 'ii', 'topic'}
            ai_keywords = set(norm.split()) - stop_words
            best_score = 0
            best_page = fallback

            for toc_norm, page in toc_page_map.items():
                cleaned_toc = _re.sub(r'topic\s+\d+:\s*', '', toc_norm)
                toc_keywords = set(_re.sub(r'[^\w\s]', '', cleaned_toc).split()) - stop_words
                overlap = len(ai_keywords & toc_keywords)
                if overlap > best_score and overlap >= 1:
                    best_score = overlap
                    best_page = page

            return best_page

        # Update extracted_structure on the KP so Review Modal reflects AI-generated topics/units
        ai_extracted_structure = []
        for gen_t in result.topics:
            topic_page = _lookup_page(gen_t.name)
            children = []
            for gen_u in gen_t.units:
                unit_page = _lookup_page(gen_u.name, fallback=topic_page)
                children.append({
                    "id": str(uuid.uuid4()),
                    "title": gen_u.name,
                    "start_page": unit_page,
                    "type": "unit",
                    "description": gen_u.description
                })
            ai_extracted_structure.append({
                "id": str(uuid.uuid4()),
                "title": gen_t.name,
                "start_page": topic_page,
                "type": "topic",
                "children": children
            })
        kp.extracted_structure = ai_extracted_structure

        # Store result summary on the KP
        kp.generation_metadata = {
            "topics_created": len(result.topics),
            "units_created": sum(len(t.units) for t in result.topics),
            "agent_notes": result.notes,
        }
        kp.save(update_fields=["extracted_structure", "generation_metadata"])

        logger.info(
            "[AIIngestion] KP %d: created %d topics, %d units.",
            knowledge_pack_id,
            kp.generation_metadata["topics_created"],
            kp.generation_metadata["units_created"],
        )
        return result

    @staticmethod
    def _persist(kp, result: AiIngestionResult) -> None:
        """Create Topic and LearningUnit records. Skips duplicates by name."""
        from curriculum.models import Topic, LearningUnit

        subject = kp.subject
        existing_topic_names = set(
            subject.topics.values_list('name', flat=True)
        )

        for order_t, gen_topic in enumerate(result.topics, start=1):
            # Skip if a topic with this name already exists for the subject
            if gen_topic.name in existing_topic_names:
                topic_obj = subject.topics.get(name=gen_topic.name)
                logger.debug("[AIIngestion] Topic '%s' already exists — reusing.", gen_topic.name)
            else:
                topic_obj = Topic.objects.create(
                    name=gen_topic.name,
                    subject=subject,
                    order=order_t,
                )
                existing_topic_names.add(gen_topic.name)
                logger.debug("[AIIngestion] Created topic: %s", gen_topic.name)

            existing_unit_names = set(
                topic_obj.learning_units.values_list('name', flat=True)
            )
            for order_u, gen_unit in enumerate(gen_topic.units, start=1):
                if gen_unit.name not in existing_unit_names:
                    LearningUnit.objects.create(
                        name=gen_unit.name,
                        topic=topic_obj,
                        order=order_u,
                        description=gen_unit.description,
                    )
                    existing_unit_names.add(gen_unit.name)
                    logger.debug("[AIIngestion] Created unit: %s", gen_unit.name)
