"""
VisualGeneratorAgent
--------------------
Takes a free-text admin prompt and a LessonBlock, builds focused curriculum
context, calls the VisualReasoner, and safely attaches the result as a LessonAsset.
"""
import logging
from typing import Tuple, Optional

logger = logging.getLogger("curriculum.ai_ingestion.visual")


class VisualGeneratorAgent:
    """
    Wraps the existing VisualReasoner for on-demand visual generation.
    Used by the generate_visual Celery task to fulfil VisualGenerationJob requests.
    """

    @staticmethod
    def run(visual_job_id: int) -> None:
        """
        Execute a VisualGenerationJob.

        1. Fetches the VisualGenerationJob from the DB with full curriculum hierarchy.
        2. Builds focused pedagogical context combining:
           - Curriculum / Grade / Subject / Topic / LearningUnit
           - LessonBlock type and content snippet
           - Existing visual metadata if updating
           - Administrator's explicit instruction
        3. Calls VisualReasoner.evaluate_requirement().
        4. On success:
           - Creates a LessonAsset with generated code.
           - Attaches it to the block.
           - Safely archives/detaches previous visual assets (safe non-destructive replacement).
           - Marks job completed.
        5. On failure:
           - Preserves existing assets completely intact.
           - Marks job failed with the specific failure reason.
        """
        from curriculum.models import VisualGenerationJob, LessonAsset
        from curriculum.media_orchestration.contracts import MediaRequirement
        from curriculum.media_orchestration.visual_intelligence.reasoner import VisualReasoner

        job = VisualGenerationJob.objects.select_related(
            'lesson_block',
            'lesson_block__lesson',
            'lesson_block__lesson__topic',
            'lesson_block__lesson__topic__subject',
            'lesson_block__lesson__topic__subject__grade',
            'lesson_block__lesson__topic__subject__grade__curriculum',
            'lesson_block__lesson__learning_unit',
        ).get(id=visual_job_id)

        job.status = 'generating'
        job.save(update_fields=['status'])

        block = job.lesson_block
        lesson = block.lesson
        topic = lesson.topic if lesson else None
        subject = topic.subject if topic else None
        grade = subject.grade if subject else None
        curriculum = grade.curriculum if grade else None
        learning_unit = lesson.learning_unit if lesson else None

        # Existing visual info (if updating)
        existing_assets = list(block.assets.all())
        existing_visual_summary = None
        if existing_assets:
            primary_asset = existing_assets[0]
            existing_visual_summary = {
                "id": primary_asset.id,
                "asset_type": primary_asset.asset_type,
                "title": primary_asset.title,
                "description": primary_asset.description,
                "format": (primary_asset.metadata or {}).get('visual_format', ''),
            }

        # Content preview (up to 250 chars)
        content_preview = ""
        if isinstance(block.content, dict):
            content_preview = (
                block.content.get('text')
                or block.content.get('question')
                or block.content.get('prompt')
                or str(block.content)
            )[:250]
        elif isinstance(block.content, str):
            content_preview = block.content[:250]

        # Resolve target card context if available
        meta = block.metadata if isinstance(block.metadata, dict) else {}
        target_block_id = meta.get('target_block_id')
        target_card = None

        if target_block_id and lesson:
            target_card = lesson.blocks.filter(id=target_block_id).first()

        MEDIA_TYPES = {
            'suggested_diagram', 'suggested_image', 'suggested_video', 'suggested_simulation',
            'visualization', 'diagram', 'image', 'video', 'image_placeholder', 'diagram_placeholder',
            'video_ref', 'simulation_placeholder', 'suggested_activity', 'suggested_illustration',
            'suggested_infographic', 'suggested_table', 'suggested_graph', 'suggested_timeline',
            'suggested_flowchart', 'suggested_mind_map', 'suggested_gif', 'suggested_external_link',
            'repository_asset'
        }

        # If no target_card linked yet, but this block itself is a content block:
        if not target_card and block.block_type not in MEDIA_TYPES:
            target_card = block

        # If still not found, check other blocks on the same page for the most relevant content card
        if not target_card and lesson and block.page_number:
            same_page_content_blocks = lesson.blocks.filter(
                page_number=block.page_number
            ).exclude(
                id=block.id
            ).exclude(
                block_type__in=MEDIA_TYPES
            ).order_by('order')

            preceding = same_page_content_blocks.filter(order__lt=block.order).last()
            target_card = preceding or same_page_content_blocks.first()

        # Build comprehensive target card summary
        target_card_info = None
        if target_card:
            card_content = target_card.content
            card_details = []
            if isinstance(card_content, dict):
                for k, v in card_content.items():
                    if k in ['status', 'visual_job_id', 'generated_code', 'svg_content', 'last_updated_via', 'user_prompt']:
                        continue
                    if isinstance(v, (str, int, float, bool)):
                        card_details.append(f"{k.capitalize()}: {v}")
                    elif isinstance(v, list):
                        items_str = ", ".join(str(item) for item in v[:12])
                        card_details.append(f"{k.capitalize()}: {items_str}")
                    elif isinstance(v, dict):
                        sub_items = [f"{sk}: {sv}" for sk, sv in v.items() if isinstance(sv, (str, int, float, bool))]
                        card_details.append(f"{k.capitalize()}: {'; '.join(sub_items)}")
            elif isinstance(card_content, str):
                card_details.append(card_content[:1500])

            target_card_info = {
                "id": target_card.id,
                "title": target_card.title or "Target Card",
                "component_type": target_card.component_type or target_card.block_type,
                "details": "\n".join(card_details) if card_details else str(card_content)[:1500],
            }

        # Same-page context for surrounding concepts
        same_page_snippets = []
        if lesson and block.page_number:
            for pb in lesson.blocks.filter(page_number=block.page_number).exclude(id__in=[block.id, getattr(target_card, 'id', None)]).order_by('order')[:4]:
                p_title = pb.title or pb.block_type
                p_text = ""
                if isinstance(pb.content, dict):
                    p_text = pb.content.get('text') or pb.content.get('task') or pb.content.get('question') or ""
                elif isinstance(pb.content, str):
                    p_text = pb.content
                if p_text:
                    same_page_snippets.append(f"[{pb.component_type or pb.block_type}] {p_title}: {str(p_text)[:200]}")
        same_page_summary = "\n".join(same_page_snippets)

        # Extract rich pedagogical context from the lesson
        lesson_context_snippets = []
        if lesson:
            for gb in lesson.blocks.filter(block_type__in=['learning_goal', 'objectives', 'goal'])[:2]:
                if isinstance(gb.content, dict):
                    goals = gb.content.get('goals') or gb.content.get('text')
                    if goals:
                        lesson_context_snippets.append(f"Goals: {str(goals)[:250]}")
            for cb in lesson.blocks.filter(block_type__in=['concept', 'concept_explanation', 'concept_card', 'core_explanation'])[:3]:
                if isinstance(cb.content, dict):
                    txt = cb.content.get('text')
                    if txt:
                        lesson_context_snippets.append(f"Concept: {str(txt)[:300]}")
            for db in lesson.blocks.filter(block_type__in=['definition_card', 'definitions', 'key_terms'])[:3]:
                if isinstance(db.content, dict):
                    term = db.content.get('term')
                    defn = db.content.get('definition') or db.content.get('example')
                    if term:
                        lesson_context_snippets.append(f"Definition ({term}): {str(defn)[:150]}")

        lesson_context_summary = "\n".join(lesson_context_snippets)

        pedagogical_context = {
            "curriculum": curriculum.name if curriculum else "General Curriculum",
            "grade_level": grade.name if grade else "",
            "subject": subject.name if subject else "",
            "topic": topic.name if topic else "",
            "learning_unit": learning_unit.name if learning_unit else (topic.name if topic else ""),
            "lesson_title": lesson.title or "",
            "component_type": block.component_type or block.block_type,
            "block_title": block.title or "",
            "relevant_block_content": content_preview,
            "targeted_card": target_card_info,
            "same_page_context": same_page_summary,
            "lesson_pedagogical_content": lesson_context_summary,
            "existing_visual": existing_visual_summary,
            "administrator_instruction": job.prompt,
            "is_targeted_generation": True,
        }

        try:
            req_desc = (
                f"Subject: {pedagogical_context['subject']} ({pedagogical_context['grade_level']}). "
                f"Topic: {pedagogical_context['topic']} - Unit: {pedagogical_context['learning_unit']}. "
                f"Lesson: {pedagogical_context['lesson_title']}. "
            )
            if target_card_info:
                req_desc += f"Target Card: [{target_card_info['component_type']}] {target_card_info['title']}. "
            req_desc += f"Requested visual: {job.prompt}"

            req = MediaRequirement(
                node_id=f"visual_job_{job.pk}",
                requirement_type="visual",
                description=req_desc,
                search_keywords=job.prompt.split()[:8],
                entity_name=pedagogical_context['topic'] or pedagogical_context['subject'],
            )

            prompt_lower = (job.prompt or '').lower().strip()
            block_type_lower = (block.block_type or '').lower().strip()
            component_type_lower = (block.component_type or '').lower().strip()

            import re
            is_image_slot = any(t in block_type_lower or t in component_type_lower for t in ['image', 'photo', 'picture'])
            photo_keywords = {'photo', 'photograph', 'picture', 'wikimedia', 'specimen', 'real-world', 'real world', 'microscope', 'actual'}
            prompt_wants_photo = any(re.search(rf'\b{re.escape(kw)}\b', prompt_lower) for kw in photo_keywords)
            explicit_diagram_request = bool(re.search(r'\b(?:diagram|flowchart|concept\s*map|svg|draw|drawing|chart|graph|schematic)\b', prompt_lower))

            should_try_wikimedia = (is_image_slot or prompt_wants_photo) and not explicit_diagram_request

            if should_try_wikimedia:
                try:
                    from curriculum.media_orchestration.providers.wikimedia import WikimediaProvider
                    from curriculum.media_orchestration.search_intelligence.models import SearchPayload
                    from curriculum.media_orchestration.assembler import clean_display_title
                    import re

                    clean_search_query = re.sub(
                        r'^(?:add|show|find|fetch|get|create|insert|provide|search\s+for|photo\s+of|image\s+of|picture\s+of|photograph\s+of)\s+',
                        '',
                        job.prompt,
                        flags=re.IGNORECASE
                    ).strip()
                    clean_search_query = re.sub(r'\s+(?:photo|photograph|image|picture)$', '', clean_search_query, flags=re.IGNORECASE).strip()

                    if not clean_search_query:
                        clean_search_query = pedagogical_context.get('topic') or pedagogical_context.get('subject') or "Science"

                    topic_term = pedagogical_context.get('topic', '').strip()
                    subject_term = pedagogical_context.get('subject', '').strip()
                    alt_queries = []
                    if topic_term and topic_term.lower() not in clean_search_query.lower():
                        alt_queries.append(f"{clean_search_query} {topic_term}")
                    if subject_term and subject_term.lower() not in clean_search_query.lower():
                        alt_queries.append(f"{clean_search_query} {subject_term}")
                    if topic_term:
                        alt_queries.append(topic_term)

                    provider = WikimediaProvider()
                    payload = SearchPayload(
                        primary_query=clean_search_query,
                        alternate_queries=alt_queries,
                        preferred_media_category="Real-world Visualization",
                        is_suitable_for_wikimedia=True
                    )

                    wikimedia_assets = provider.search(payload, node_id=f"visual_job_{job.pk}")
                    if wikimedia_assets:
                        best_asset = wikimedia_assets[0]
                        clean_title = clean_display_title(best_asset.alt_text, fallback=target_card.title if target_card else clean_search_query.title())

                        new_asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type='image',
                            source_type='wikimedia',
                            storage_type='url',
                            status='attached',
                            title=clean_title,
                            description=best_asset.alt_text or job.prompt,
                            url=best_asset.url,
                            metadata={
                                'provenance': best_asset.provenance,
                                'licensing': best_asset.licensing,
                                'author': best_asset.author,
                                'attribution': best_asset.attribution,
                                'commons_page_url': (best_asset.metadata or {}).get('commons_page_url', ''),
                                'confidence_score': best_asset.confidence_score,
                                'visual_job_id': job.pk,
                                'component_tag': block.component_type or block.block_type,
                                'admin_instruction': job.prompt,
                                'target_card_id': getattr(target_card, 'id', None),
                                'target_card_title': getattr(target_card, 'title', None),
                            },
                        )
                        new_asset.blocks.add(block)

                        for old_a in existing_assets:
                            old_a.blocks.remove(block)
                            if old_a.blocks.count() == 0:
                                old_a.status = 'archived'
                                old_a.save(update_fields=['status'])

                        block.title = clean_title
                        if isinstance(block.content, dict):
                            block.content['title'] = clean_title
                            block.content['status'] = 'ready'
                            block.content['url'] = best_asset.url
                            block.content['caption'] = best_asset.alt_text
                            block.content['provenance'] = best_asset.provenance
                            block.content['author'] = best_asset.author
                            block.content['licensing'] = best_asset.licensing
                            block.save(update_fields=['title', 'content'])
                        else:
                            block.content = {
                                'title': clean_title,
                                'status': 'ready',
                                'url': best_asset.url,
                                'caption': best_asset.alt_text,
                                'provenance': best_asset.provenance,
                                'author': best_asset.author,
                                'licensing': best_asset.licensing,
                            }
                            block.save(update_fields=['title', 'content'])

                        meta = block.metadata if isinstance(block.metadata, dict) else {}
                        meta['url'] = best_asset.url
                        meta['provenance'] = best_asset.provenance
                        block.metadata = meta
                        block.save(update_fields=['metadata'])

                        job.result_asset = new_asset
                        job.status = 'completed'
                        job.error_message = ''
                        job.save(update_fields=['result_asset', 'status', 'error_message', 'updated_at'])
                        logger.info("[VisualAgent] Job %d completed via Wikimedia — asset #%d created.", job.pk, new_asset.pk)
                        return
                except Exception as wm_err:
                    logger.warning("[VisualAgent] Wikimedia retrieval failed for job %d: %s. Falling back to VisualReasoner.", job.pk, wm_err)

            reasoner = VisualReasoner()
            visual_spec, failure = reasoner.evaluate_requirement(req, pedagogical_context)

            if failure or visual_spec is None:
                reason = failure.reason if failure else "Visual reasoner returned no result."
                job.status = 'failed'
                job.error_message = reason
                job.save(update_fields=['status', 'error_message', 'updated_at'])
                logger.warning("[VisualAgent] Job %d failed: %s", job.pk, reason)
                return

            # Determine format and code
            code = getattr(visual_spec, 'code', None) or getattr(visual_spec, 'generated_code', None) or ""
            fmt = getattr(visual_spec, 'format', None) or getattr(visual_spec, 'visual_format', 'svg') or 'svg'

            # Determine clean student-facing title
            candidate_titles = [
                getattr(visual_spec, 'title', None),
                block.content.get('title') if isinstance(block.content, dict) else None,
                meta.get('target_block_title'),
                target_card.title if target_card else None,
            ]
            clean_title = None
            import re
            for cand in candidate_titles:
                if not cand or not isinstance(cand, str):
                    continue
                c_clean = re.sub(r'^AI\s+Visual:\s*', '', cand, flags=re.IGNORECASE).strip()
                if re.match(r'^(?:Replace|Create|Generate|Make|Draw|Add|Remove|Update|Please|Use)\s+', c_clean, flags=re.IGNORECASE):
                    continue
                c_clean = re.sub(r'\s+(?:Visual|Diagram|Visualization|Video)\s*(?:Card|Slot)?$', '', c_clean, flags=re.IGNORECASE).strip()
                if len(c_clean) > 0:
                    clean_title = c_clean
                    break

            if not clean_title:
                clean_title = (lesson.title if lesson else "Scientific Diagram")

            # Create LessonAsset with the generated code stored in metadata
            new_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type='generated',
                source_type='ai_generated',
                storage_type='url',
                status='attached',
                title=clean_title,
                description=job.prompt,
                metadata={
                    'visual_format': fmt,
                    'generated_code': code,
                    'svg_content': code if fmt == 'svg' or '<svg' in code else '',
                    'alt_text': getattr(visual_spec, 'alt_text', '') or '',
                    'visual_job_id': job.pk,
                    'component_tag': block.component_type or block.block_type,
                    'admin_instruction': job.prompt,
                    'target_card_id': getattr(target_card, 'id', None),
                    'target_card_title': getattr(target_card, 'title', None),
                },
            )
            new_asset.blocks.add(block)

            # Safe replacement: only detach/archive previous assets after the new one succeeded
            for old_a in existing_assets:
                old_a.blocks.remove(block)
                if old_a.blocks.count() == 0:
                    old_a.status = 'archived'
                    old_a.save(update_fields=['status'])

            # Update lesson block title and content to clean title and ready status
            block.title = clean_title
            if isinstance(block.content, dict):
                block.content['title'] = clean_title
                block.content['status'] = 'ready'
                block.content['visual_format'] = fmt
                block.content['alt_text'] = getattr(visual_spec, 'alt_text', '') or ''
                block.content['generated_code'] = code
                if fmt == 'svg' or '<svg' in code:
                    block.content['svg_content'] = code
                block.save(update_fields=['title', 'content'])
            else:
                block.save(update_fields=['title'])

            meta = block.metadata if isinstance(block.metadata, dict) else {}
            meta['generated_code'] = code
            if fmt == 'svg' or '<svg' in code:
                meta['svg_content'] = code
            block.metadata = meta
            block.save(update_fields=['metadata'])

            job.result_asset = new_asset
            job.status = 'completed'
            job.error_message = ''
            job.save(update_fields=['result_asset', 'status', 'error_message', 'updated_at'])
            logger.info("[VisualAgent] Job %d completed — asset #%d created.", job.pk, new_asset.pk)

        except Exception as exc:
            logger.error("[VisualAgent] Job %d errored: %s", job.pk, exc, exc_info=True)
            job.status = 'failed'
            job.error_message = str(exc)
            job.save(update_fields=['status', 'error_message', 'updated_at'])
            raise
