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
    name: str = Field(description="Title for the individual lesson (e.g. 'Lesson 1: Introduction to Aviation Technology').")
    start_page: int = Field(default=1, description="The starting page number in the textbook where this lesson's content begins.")
    description: str = Field(description="One-sentence learning outcome explaining what students will master in this lesson.")


class GeneratedTopic(BaseModel):
    name: str = Field(description="Name of the modular study topic (e.g. 'Foundations of Aviation Technology', 'Flight Operations').")
    start_page: int = Field(default=1, description="The starting page number in the textbook where this topic begins.")
    units: List[GeneratedUnit] = Field(description="Bite-sized lessons (learning units) belonging to this topic.")


class AiIngestionResult(BaseModel):
    topics: List[GeneratedTopic] = Field(description="The complete inferred topic/lesson hierarchy across the textbook.")
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

        # Build a rich page-by-page sample of the textbook content across the entire book
        pages_dict = {}
        for chunk in chunks:
            p = chunk.start_page or 1
            if p not in pages_dict:
                pages_dict[p] = []
            text = (chunk.content_text or "").strip()
            if text:
                pages_dict[p].append(text)

        sampled_outline = []
        # Sample headings and content from each page (up to first 100 pages)
        for p in sorted(pages_dict.keys())[:100]:
            page_text = " ".join(pages_dict[p])
            snippet = page_text[:250].replace("\n", " ").strip()
            if snippet:
                sampled_outline.append(f"[Page {p}]: {snippet}")

        outline_text = "\n".join(sampled_outline) if sampled_outline else "No page content available."

        prompt = (
            f"Subject / Textbook: {kp.subject.name}\n\n"
            f"Here is a page-by-page outline and content samples extracted directly from the uploaded textbook:\n"
            f"================================================================================\n"
            f"{outline_text}\n"
            f"================================================================================\n\n"
            f"Instructions:\n"
            f"1. Analyze the full document content, table of contents/strands, and chapter headers.\n"
            f"2. Group the curriculum into 5 to 15 modular, focused Topics.\n"
            f"3. For each Topic, create 2 to 6 specific, granular Learning Units (Lessons).\n"
            f"4. For EVERY topic and lesson, extract and specify the accurate 'start_page' based on the [Page X] markers above."
        )

        logger.info(
            "[AIIngestion] Calling LLM for KP %d (%d pages sampled).",
            knowledge_pack_id, len(sampled_outline)
        )

        provider = LLMFactory.get_provider()
        result: AiIngestionResult = provider.generate_structured(
            prompt=prompt,
            response_schema=AiIngestionResult,
            system_instruction=SYSTEM_INSTRUCTION,
        )

        if not isinstance(result, AiIngestionResult):
            result = AiIngestionResult.model_validate(result)

        # Build structure directly from LLM-inferred topics, lessons, and start pages
        ai_extracted_structure = []
        for gen_t in result.topics:
            t_page = gen_t.start_page if gen_t.start_page and gen_t.start_page > 0 else 1
            children = []
            for gen_u in gen_t.units:
                u_page = gen_u.start_page if gen_u.start_page and gen_u.start_page > 0 else t_page
                children.append({
                    "id": str(uuid.uuid4()),
                    "title": gen_u.name,
                    "start_page": u_page,
                    "type": "unit",
                    "description": gen_u.description
                })
            ai_extracted_structure.append({
                "id": str(uuid.uuid4()),
                "title": gen_t.name,
                "start_page": t_page,
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
