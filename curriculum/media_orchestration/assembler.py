import json
from typing import List, Dict, Any
from django.db import transaction

from curriculum.models import Lesson, LessonBlock, LessonAsset, Simulation
from .contracts import LearningExperiencePlan, ExperiencePackage, ResolvedAsset
from .planner import MediaPlanner
from .acquisition import MediaAcquisitionEngine
from .visual_intelligence.engine import VisualIntelligenceEngine

import re

def clean_display_title(raw_title: str, fallback: str = "Key Concept") -> str:
    """
    Sanitizes block and card titles to remove drafting terminologies, internal stage prefixes,
    and meta-jargon so student and teacher views have natural, engaging headings.
    """
    if not raw_title:
        return fallback
    cleaned = str(raw_title).strip()
    # Strip markdown headers or list markers
    cleaned = re.sub(r'^[#*\-\s]+', '', cleaned)
    # Strip numbered stage prefixes like "1. ", "Stage 1: ", "Card 1: ", "Part 1: ", "Node: "
    cleaned = re.sub(r'^(?:Stage|Card|Part|Module|Concept|Step)\s*\d+[\s:\-–—\.]*', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'^\d+[\s:\-–—\.]+', '', cleaned)
    cleaned = re.sub(r'\s+(?:Visual|Diagram|Visualization|Video)\s*(?:Card|Slot)?$', '', cleaned, flags=re.IGNORECASE)
    
    # Strip drafting jargon mappings
    drafting_patterns = [
        (r'^(?:Introduction\s*&\s*Hook|Intro\s*&\s*Hook|Introduction\s*Hook|Hook\s*&\s*Intro)\b', 'Introduction & Discovery'),
        (r'^(?:Curiosity\s*Hook|Hook\s*Scenario|Hook)\b', 'Curiosity & Discovery'),
        (r'^(?:Predict|Prediction|Predictive\s*Challenge)\b', 'Initial Prediction Challenge'),
        (r'^(?:Core\s*Principles?\s*&\s*Mechanism|Core\s*Principles?|Core\s*Explanation)\b', 'Fundamental Principles'),
        (r'^(?:Real[\s\-_]*World\s*Applications?\s*&\s*Workings|Real[\s\-_]*World\s*Connection|Real[\s\-_]*World\s*Applications?)\b', 'Real-World Applications'),
        (r'^(?:Worked\s*Example|Step[\s\-_]*by[\s\-_]*Step\s*Worked\s*Example)\b', 'Step-by-Step Problem Solving'),
        (r'^(?:Common\s*Pitfalls?\s*&\s*Practice|Common\s*Misconceptions?|Misconception)\b', 'Common Misconceptions & Pitfalls'),
        (r'^(?:Knowledge\s*Check|Active\s*Practice\s*&\s*Knowledge\s*Check|Check\s*for\s*Understanding)\b', 'Check Your Understanding'),
        (r'^(?:Reflection\s*&\s*Summary|Summary\s*&\s*Reflection|Summary\s*&\s*Key\s*Takeaways|Summary)\b', 'Key Insights & Summary'),
    ]
    for pattern, replacement in drafting_patterns:
        if re.search(pattern, cleaned, flags=re.IGNORECASE):
            cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)
            break
    cleaned = cleaned.strip()
    return cleaned if cleaned else fallback


class ExperienceAssemblyService:
    """
    Module 3: Experience Assembly (Deterministic).
    Compiles a LearningExperiencePlan and its resolved assets into a final ExperiencePackage
    and persists it to the database.
    """

    def __init__(self):
        self.planner = MediaPlanner()
        self.visual_engine = VisualIntelligenceEngine()
        self.acquisition_engine = MediaAcquisitionEngine()

    @transaction.atomic
    def compile_experience(self, lesson: Lesson, plan: LearningExperiencePlan) -> ExperiencePackage:
        # 1. Plan Media
        manifest = self.planner.generate_manifest(plan)
        
        pedagogical_context = plan.model_dump() if hasattr(plan, 'model_dump') else plan.dict()

        # 2. Visual Intelligence & Provider Retrieval
        generated_visuals, _ = self.visual_engine.process_manifest(manifest, pedagogical_context)
        resolved_assets = self.acquisition_engine.resolve_manifest(manifest)

        # Combine all assets
        all_assets = generated_visuals + resolved_assets
        
        # Build a lookup for resolved assets by node_id (List of assets per node)
        assets_by_node = {}
        for asset in all_assets:
            if asset.node_id not in assets_by_node:
                assets_by_node[asset.node_id] = []
            assets_by_node[asset.node_id].append(asset)
            
        # 3. Assemble and Persist
        lesson.blocks.all().delete()
        lesson.assets.all().delete()
        
        # Assign an explicit, dedicated page_number for each node to ensure 7 to 10 distinct cards
        node_page_mapping = {}
        current_page = 1
        for idx, node in enumerate(plan.nodes):
            ntype = (node.node_type or '').lower()
            if idx == 0:
                node_page_mapping[node.node_id] = current_page
            elif idx == 1 and ntype in ('learning_goal', 'hook') and (plan.nodes[0].node_type or '').lower() in ('hook', 'learning_goal'):
                # Learning goal and hook share page 1 as the introduction card
                node_page_mapping[node.node_id] = current_page
            else:
                # Every subsequent major pedagogical step gets its own dedicated card
                current_page += 1
                node_page_mapping[node.node_id] = current_page

        block_order = 0
        
        for idx, node in enumerate(plan.nodes):
            raw_group_name = getattr(node.instructional_intent, 'concept_group', None) or (getattr(node, 'title', None) or node.node_id.replace('_', ' ').title())
            clean_group_name = clean_display_title(raw_group_name, fallback=f"Part {idx + 1}")
            page_num = node_page_mapping.get(node.node_id, idx + 1)
            layout_template = getattr(node.instructional_intent, 'layout_template', None) or 'DiscoveryLayout'
            
            raw_node_title = getattr(node, 'title', None) or node.node_id.replace('_', ' ').title()
            clean_block_title = clean_display_title(raw_node_title, fallback=clean_group_name)

            try:
                content_payload = json.loads(node.content)
                if not isinstance(content_payload, dict):
                    content_payload = {'text': node.content}
            except (json.JSONDecodeError, TypeError):
                # Check if it's an MCQ knowledge check formatted as markdown
                raw_text = str(node.content)
                comp_type = self._map_step_to_legacy_component(node.node_type)
                if comp_type == 'knowledge_check' and ('- **A)**' in raw_text or 'A)' in raw_text):
                    q_match = re.search(r'\*\*Question:\*\*\s*(.*?)(?=\n-|\n\*\*|$)', raw_text, re.DOTALL)
                    question_txt = q_match.group(1).strip() if q_match else raw_text.split('\n')[0]
                    
                    opts = []
                    for letter in ['A', 'B', 'C', 'D']:
                        opt_m = re.search(rf'[-*]?\s*\*\*?{letter}\)?\*\*?\s*(.*?)(?=\n[-*]?\s*\*\*?[A-D]\)?|\n\*\*Correct|\n\*\*Explanation|$)', raw_text, re.DOTALL)
                        if opt_m:
                            opts.append(opt_m.group(1).strip())
                    
                    ans_m = re.search(r'\*\*Correct Answer:\*\*\s*\*\*?([A-D])\b', raw_text)
                    ans = ans_m.group(1) if ans_m else 'A'
                    
                    exp_m = re.search(r'\*\*Explanation:\*\*\s*(.*)', raw_text, re.DOTALL)
                    exp = exp_m.group(1).strip() if exp_m else ''
                    
                    content_payload = {
                        'check_type': 'multiple_choice',
                        'question': question_txt,
                        'options': opts if len(opts) >= 2 else ['Option A', 'Option B', 'Option C', 'Option D'],
                        'answer': ans,
                        'explanation': exp
                    }
                else:
                    content_payload = {'text': node.content}

            # ── Auto-extract and validate any YouTube links from API response ──────
            # Checks node.content, recommended_learning_support, or explicit links provided by the LLM
            combined_prompt_text = f"{str(node.content)} {str(node.instructional_intent.recommended_learning_support or '')}"
            yt_matches = re.findall(r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})', combined_prompt_text)
            if yt_matches:
                from .providers.youtube import YouTubeProvider
                for vid in yt_matches:
                    resolved_yt = YouTubeProvider.resolve_video_id(vid, node.node_id)
                    if resolved_yt:
                        # Clean raw URL from student text so it renders as a dedicated video player block
                        if isinstance(content_payload, dict) and 'text' in content_payload:
                            clean_txt = re.sub(r'https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[a-zA-Z0-9_-]{11}[^\s\)]*', '', content_payload['text']).strip()
                            clean_txt = re.sub(r'\(\s*\)', '', clean_txt).strip()
                            content_payload['text'] = clean_txt
                        
                        if node.node_id not in assets_by_node:
                            assets_by_node[node.node_id] = []
                        # Avoid duplicate video attachments
                        if not any(a.asset_type == 'video' and (a.metadata or {}).get('video_id') == vid for a in assets_by_node[node.node_id]):
                            assets_by_node[node.node_id].insert(0, resolved_yt)
                            all_assets.append(resolved_yt)
                        break

            metadata = {
                'concept_group': clean_group_name,
                'layout_template': layout_template,
                'learning_moment': node.instructional_intent.learning_moment,
                'student_goal': node.instructional_intent.student_goal,
                'required_cognitive_change': node.instructional_intent.required_cognitive_change,
                'evidence_of_understanding': node.instructional_intent.evidence_of_understanding,
                'recommended_learning_support': node.instructional_intent.recommended_learning_support,
                'success_criteria': node.success_criteria,
                'failure_criteria': node.failure_criteria,
                'node_type': node.node_type,
            }
            
            block = LessonBlock.objects.create(
                lesson=lesson,
                block_id=node.node_id,
                block_type=self._map_step_to_legacy_component(node.node_type),
                title=clean_block_title,
                content=content_payload,
                metadata=metadata,
                order=block_order,
                page_number=page_num,
                page_title=clean_block_title,
                component_type=self._map_step_to_legacy_component(node.node_type),
                component_order=idx + 1
            )
            block_order += 1
            
            # Real World Connection auto-enrichment check
            if self._map_step_to_legacy_component(node.node_type) == 'real_world_example':
                # Attempt to find if we already got a Wikimedia reference for this node
                has_wikimedia = False
                if node.node_id in assets_by_node:
                    for a in assets_by_node[node.node_id]:
                        if a.provenance == "Wikimedia Commons":
                            has_wikimedia = True
                            break
                            
                # If not, we could inject one (simplified logic: just mark it in metadata for future)
                if not has_wikimedia:
                    pass # Automatic reference could be injected here if we ran a direct query
            
            # Place all resolved assets
            if node.node_id in assets_by_node:
                node_assets = assets_by_node[node.node_id]
                for asset_idx, resolved_asset in enumerate(node_assets):
                    media_block_type = self._map_asset_type_to_block_type(resolved_asset.asset_type)
                    
                    asset_metadata = {
                        "provenance": resolved_asset.provenance,
                        "licensing": resolved_asset.licensing,
                        "confidence_score": resolved_asset.confidence_score,
                        "fallback_used": resolved_asset.fallback_used,
                        "author": resolved_asset.author,
                        "attribution": resolved_asset.attribution
                    }
                    
                    if resolved_asset.asset_type == 'simulation' or media_block_type == 'suggested_simulation':
                        sim_match = Simulation.objects.filter(status='ACTIVE').first()
                        if sim_match:
                            asset_metadata["simulation_key"] = sim_match.key
                            asset_metadata["archetype"] = sim_match.archetype
                            asset_metadata["config"] = sim_match.config
                            asset_metadata["context_spec"] = sim_match.config.get("context_spec", {})
                    
                    media_block_metadata = {**metadata, **asset_metadata}
                    
                    # Construct specific payload for block type (e.g. YouTube video vs Image)
                    if media_block_type == 'video_ref' or resolved_asset.asset_type == 'video':
                        video_id = (resolved_asset.metadata or {}).get('video_id', '')
                        if not video_id and resolved_asset.url:
                            import re as _re
                            v_m = _re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', resolved_asset.url)
                            if v_m:
                                video_id = v_m.group(1)
                        video_title = resolved_asset.alt_text or f"Demonstration: {clean_block_title}"
                        media_content = {
                            'title': video_title,
                            'url': resolved_asset.url,
                            'youtube_url': resolved_asset.url,
                            'video_id': video_id,
                            'resolved_video_id': video_id,
                            'description': f"Educational video demonstrating {clean_block_title}",
                            'caption': video_title
                        }
                    else:
                        media_content = {
                            'url': resolved_asset.url,
                            'caption': resolved_asset.alt_text,
                            'text': f'Auto-placed {resolved_asset.provenance} visual'
                        }
                    
                    media_title = clean_display_title(resolved_asset.alt_text, fallback=clean_block_title) if resolved_asset.alt_text else clean_block_title
                    media_block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"{node.node_id}_media_{asset_idx}",
                        block_type=media_block_type,
                        title=media_title,
                        content=media_content,
                        metadata=media_block_metadata,
                        order=block_order,
                        page_number=page_num,
                        page_title=clean_block_title,
                        component_type=media_block_type,
                        component_order=2 + asset_idx
                    )
                    block_order += 1
                        
                    asset_obj = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type=resolved_asset.asset_type,
                        source_type=self._map_provenance_to_source_type(resolved_asset.provenance),
                        storage_type='url' if resolved_asset.url else 'file',
                        status='attached',
                        title=f"{clean_block_title} ({resolved_asset.provenance})",
                        description=resolved_asset.alt_text,
                        url=resolved_asset.url,
                        knowledge_chunk_id=resolved_asset.knowledge_chunk_id,
                        metadata=asset_metadata
                    )
                    asset_obj.blocks.add(media_block)
            else:
                # Check if manifest said media was required, but we failed to resolve it
                req = next((r for r in manifest.requirements if r.node_id == node.node_id and r.is_required), None)
                if req:
                    media_block_type = self._map_asset_type_to_block_type(req.preferred_media_type)
                    
                    pending_asset_metadata = {"ai_instruction": req.educational_purpose}
                    if req.preferred_media_type == 'simulation' or media_block_type == 'suggested_simulation':
                        sim_match = Simulation.objects.filter(status='ACTIVE').first()
                        if sim_match:
                            pending_asset_metadata["simulation_key"] = sim_match.key
                            pending_asset_metadata["archetype"] = sim_match.archetype
                            pending_asset_metadata["config"] = sim_match.config
                            pending_asset_metadata["context_spec"] = sim_match.config.get("context_spec", {})

                    media_block_metadata = {**metadata, **pending_asset_metadata}

                    media_block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"{node.node_id}_media_pending",
                        block_type=media_block_type,
                        title=clean_block_title,
                        content={'text': 'Pending visual slot'},
                        metadata=media_block_metadata,
                        order=block_order,
                        page_number=page_num,
                        page_title=clean_block_title,
                        component_type=media_block_type,
                        component_order=2
                    )
                    block_order += 1
                    
                    asset_obj = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type=req.preferred_media_type,
                        source_type='uploaded',
                        storage_type='url',
                        status='pending',
                        title=clean_block_title,
                        description=req.accessibility_requirements,
                        metadata=pending_asset_metadata
                    )
        # ── Mandatory Video Guarantee ──────────────────────────────────────────
        # Ensure every generated lesson has at least one verified educational YouTube video.
        has_video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type__in=['video_ref', 'suggested_video', 'video', 'youtube']
        ).exists()

        if not has_video_block:
            from .providers.youtube import YouTubeProvider
            unit_title = clean_display_title(lesson.title, fallback="")
            topic_title = lesson.topic.name if lesson.topic else ""

            queries = [
                f"{unit_title} {topic_title} educational explanation video".strip(),
                f"{unit_title} experiment demonstration explanation".strip(),
                f"{unit_title} explanation video".strip(),
                f"{unit_title}".strip(),
            ]

            yt_provider = YouTubeProvider()
            fallback_video = None
            for q in queries:
                if len(q) < 3:
                    continue
                vids = yt_provider._execute_search(q, f"mandatory_video_{lesson.id}")
                if vids:
                    fallback_video = vids[0]
                    break

            if fallback_video:
                # Place video on a core explanation or worked example card
                target_block = LessonBlock.objects.filter(
                    lesson=lesson,
                    block_type__in=['concept_explanation', 'worked_example', 'real_world_example']
                ).order_by('page_number', 'order').first()

                target_page = target_block.page_number if target_block else 3
                target_order = (target_block.order + 1) if target_block else (block_order + 1)
                vid_id = (fallback_video.metadata or {}).get('video_id', '')
                video_title = fallback_video.alt_text or f"Demonstration: {unit_title}"

                v_block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"video_concept_{lesson.id}",
                    block_type='video_ref',
                    title=clean_display_title(video_title, fallback="Educational Video Demonstration"),
                    content={
                        'title': video_title,
                        'url': fallback_video.url,
                        'youtube_url': fallback_video.url,
                        'video_id': vid_id,
                        'resolved_video_id': vid_id,
                        'description': f"Educational video demonstrating key concepts for {unit_title}",
                        'caption': video_title
                    },
                    metadata={
                        'provenance': 'YouTube',
                        'licensing': fallback_video.licensing,
                        'author': fallback_video.author,
                        'attribution': fallback_video.attribution,
                        'confidence_score': fallback_video.confidence_score,
                    },
                    order=target_order,
                    page_number=target_page,
                    page_title=target_block.page_title if target_block else unit_title,
                    component_type='video_ref',
                    component_order=99
                )

                asset_obj = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type='video',
                    source_type='external',
                    storage_type='url',
                    status='attached',
                    title=v_block.title,
                    description=v_block.content.get('description', ''),
                    url=fallback_video.url,
                    metadata={
                        'video_id': vid_id,
                        'author': fallback_video.author,
                        'provenance': 'YouTube',
                        'attribution': fallback_video.attribution
                    }
                )
                asset_obj.blocks.add(v_block)
                all_assets.append(fallback_video)
                block_order += 1

        package = ExperiencePackage(
            plan=plan,
            resolved_assets=all_assets
        )
        return package

    def _map_step_to_legacy_component(self, node_type: str) -> str:
        """
        Maps a PedagogicalEngine StrategyNode node_type to a canonical
        LessonBlock block_type that the frontend ConceptComposer knows how
        to route into the correct section.

        Planner node_types are free-form strings, so we normalise to lowercase
        and do substring/prefix matching so that creative LLM variations like
        'hook_intro' or 'predict_step' still resolve correctly.
        """
        nt = (node_type or '').lower().strip()

        # ── Introduction / Hook ──────────────────────────────────────────────
        if any(k in nt for k in ['hook', 'engage', 'motivat', 'wonder', 'scenario']):
            return 'hook'
        if any(k in nt for k in ['story', 'narrative', 'context_setting']):
            return 'story'
        if any(k in nt for k in ['goal', 'objective', 'intro', 'overview', 'orient']):
            return 'learning_goal'

        # ── Core Explanations ────────────────────────────────────────────────
        if any(k in nt for k in ['explain', 'concept', 'core', 'teach', 'present']):
            return 'concept_explanation'
        if any(k in nt for k in ['definition', 'define', 'term', 'vocabulary']):
            return 'definitions'
        if any(k in nt for k in ['analog', 'metaphor', 'comparison']):
            return 'analogy'
        if any(k in nt for k in ['observe', 'watch', 'discover', 'notc']):
            return 'mini_activity'
        if any(k in nt for k in ['predict', 'hypothes', 'wonder', 'anticipat']):
            return 'prediction'

        # ── Worked Examples / Application ────────────────────────────────────
        if any(k in nt for k in ['worked', 'example', 'demonstrat', 'show_how']):
            return 'worked_example'
        if any(k in nt for k in ['real_world', 'real world', 'application', 'context', 'case_study']):
            return 'real_world_example'
        if any(k in nt for k in ['practice', 'apply', 'scaffold', 'guided', 'drill', 'extend', 'extension']):
            return 'worked_example'
        if any(k in nt for k in ['experiment', 'activity', 'lab', 'explore', 'investigate']):
            return 'mini_activity'

        # ── Assessment / Check for Understanding ─────────────────────────────
        if any(k in nt for k in ['assess', 'quiz', 'check', 'test', 'evaluat', 'review']):
            return 'knowledge_check'
        if any(k in nt for k in ['remediat', 'reteach', 'misconception', 'mistake', 'correct', 'clarify']):
            return 'common_misconception'
        if any(k in nt for k in ['reflect', 'journal', 'think', 'metacognit']):
            return 'reflection'

        # ── Summary / Coaching ───────────────────────────────────────────────
        if any(k in nt for k in ['summary', 'summar', 'recap', 'consolidat', 'wrap']):
            return 'summary'
        if any(k in nt for k in ['key_takeaway', 'takeaway', 'tip', 'callout', 'highlight', 'memory']):
            return 'key_takeaway'

        # ── Media Suggestions ────────────────────────────────────────────────
        if any(k in nt for k in ['diagram', 'visual', 'illustrat', 'chart', 'graph', 'figure']):
            return 'suggested_diagram'
        if any(k in nt for k in ['simulat', 'interact', 'phet']):
            return 'suggested_simulation'

        # ── Final fallback ───────────────────────────────────────────────────
        return 'concept_explanation'
        
    def _map_provenance_to_source_type(self, provenance: str) -> str:
        if 'KnowledgeRepository' in provenance:
            return 'knowledge_repository'
        return 'external'

    def _map_asset_type_to_block_type(self, asset_type: str) -> str:
        at = (asset_type or '').lower().strip()
        if at == 'diagram':
            return 'suggested_diagram'
        elif at in ('video', 'youtube'):
            return 'video_ref'
        elif at == 'simulation':
            return 'suggested_simulation'
        elif at == 'external_link':
            return 'suggested_external_link'
        else:
            return 'image_placeholder'
