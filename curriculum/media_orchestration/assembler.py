import json
from typing import List, Dict, Any
from django.db import transaction

from curriculum.models import Lesson, LessonBlock, LessonAsset, Simulation
from .contracts import LearningExperiencePlan, ExperiencePackage, ResolvedAsset
from .planner import MediaPlanner
from .acquisition import MediaAcquisitionEngine
from .visual_intelligence.engine import VisualIntelligenceEngine

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
        import concurrent.futures
        
        # 1. Plan Media
        manifest = self.planner.generate_manifest(plan)
        
        pedagogical_context = plan.model_dump() if hasattr(plan, 'model_dump') else plan.dict()

        # 2. Parallel Execution: Visual Intelligence & Provider Retrieval
        generated_visuals = []
        resolved_assets = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_visuals = executor.submit(self.visual_engine.process_manifest, manifest, pedagogical_context)
            future_assets = executor.submit(self.acquisition_engine.resolve_manifest, manifest)
            
            generated_visuals, _ = future_visuals.result()
            resolved_assets = future_assets.result()

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
        
        # Backend does NOT assign page_number — the Presentation Engine owns all pagination.
        # page_number is intentionally left as None so PageGroupingService.js uses its
        # cognitive load algorithm to determine page boundaries.
        block_order = 0
        
        for idx, node in enumerate(plan.nodes):
            # page_number=None — Presentation Engine computes pages via cognitive load
            page_num = None
            layout_template = getattr(node.instructional_intent, 'layout_template', None) or 'DiscoveryLayout'
            
            try:
                content_payload = json.loads(node.content)
                if not isinstance(content_payload, dict):
                    content_payload = {'text': node.content}
            except (json.JSONDecodeError, TypeError):
                content_payload = {'text': node.content}

            metadata = {
                'concept_group': node.instructional_intent.concept_group,
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
                title=f"{node.node_id.replace('_', ' ').title()}",
                content=content_payload,
                metadata=metadata,
                order=block_order,
                page_number=page_num,
                page_title=node.instructional_intent.concept_group.title(),
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
                    
                    media_block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"{node.node_id}_media_{asset_idx}",
                        block_type=media_block_type,
                        title=f"Media for {node.node_id.replace('_', ' ').title()}",
                        content={'text': f'Auto-placed {resolved_asset.provenance} visual'},
                        metadata=media_block_metadata,
                        order=block_order,
                        page_number=page_num,
                        page_title=node.node_id.replace('_', ' ').title(),
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
                        title=f"{block.title} Media ({resolved_asset.provenance})",
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
                        title=f"Pending Media for {node.node_id.replace('_', ' ').title()}",
                        content={'text': 'Pending visual slot'},
                        metadata=media_block_metadata,
                        order=block_order,
                        page_number=page_num,
                        page_title=node.node_id.replace('_', ' ').title(),
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
                        title=f"{block.title} Media Slot",
                        description=req.accessibility_requirements,
                        metadata=pending_asset_metadata
                    )
                    asset_obj.blocks.add(media_block)
                        
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
        elif at == 'video':
            return 'video_ref'
        elif at == 'simulation':
            return 'suggested_simulation'
        elif at == 'external_link':
            return 'suggested_external_link'
        else:
            return 'image_placeholder'
