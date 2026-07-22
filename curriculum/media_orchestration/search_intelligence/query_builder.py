import re
from curriculum.media_orchestration.contracts import MediaRequirement
from .models import SearchPayload

# Keywords that indicate a concept is concrete and likely to have a good Wikimedia image
_CONCRETE_INDICATORS = {
    'apparatus', 'equipment', 'instrument', 'device', 'machine', 'reactor',
    'cell', 'battery', 'electrode', 'beaker', 'flask', 'tube', 'wire',
    'crystal', 'mineral', 'rock', 'soil', 'plant', 'animal', 'organism',
    'organ', 'tissue', 'cell', 'protein', 'enzyme', 'molecule', 'atom',
    'compound', 'element', 'metal', 'acid', 'base', 'salt',
    'process', 'reaction', 'experiment', 'laboratory', 'industrial',
    'factory', 'quarry', 'mine', 'farm', 'forest', 'river', 'lake',
    'diagram', 'structure', 'cross-section', 'illustration',
}

# Keywords that indicate an abstract concept — less suitable for Wikimedia retrieval
_ABSTRACT_INDICATORS = {
    'entropy', 'enthalpy', 'equilibrium', 'thermodynamics', 'kinetics',
    'activation energy', 'free energy', 'potential energy', 'bond energy',
    'electronegativity', 'oxidation state', 'polarity', 'solubility',
    'theory', 'law', 'principle', 'concept', 'definition', 'formula',
    'calculation', 'equation', 'stoichiometry', 'mole', 'yield',
    'rate', 'constant', 'equilibrium constant',
}

ALWAYS_WIKIMEDIA_CATEGORIES = {
    "Real-world Visualization",
    "Historical Visualization",
    "Reference Material",
}


class QueryBuilder:
    """
    Deterministically transforms a MediaRequirement into a SearchPayload
    with context-rich, layered fallback queries. Uses smart Wikimedia eligibility
    based on concept concreteness rather than a binary category check.
    """

    def build_payload(self, requirement: MediaRequirement) -> SearchPayload:
        is_suitable = self._assess_wikimedia_suitability(requirement)

        # Build primary query with subject/entity context
        primary_query = self._build_primary_query(requirement)
        alternate_queries = self._build_alternate_queries(requirement, primary_query)

        return SearchPayload(
            primary_query=primary_query,
            alternate_queries=alternate_queries,
            entity_type=None,
            preferred_media_category=requirement.media_category,
            filters={},
            is_suitable_for_wikimedia=is_suitable
        )

    def _assess_wikimedia_suitability(self, requirement: MediaRequirement) -> bool:
        """
        Smart eligibility check. Returns True if Wikimedia retrieval is worthwhile.

        Rules:
        1. Always-eligible categories (real-world, historical, reference) → True
        2. If entity_name contains concrete physical indicators → True
        3. If search_keywords contain concrete indicators → True
        4. If entity_name is purely abstract → False
        5. Default → True (attempt retrieval, better to try and fail than skip)
        """
        # Rule 1: Always-eligible media categories
        if requirement.media_category in ALWAYS_WIKIMEDIA_CATEGORIES:
            return True

        entity = (requirement.entity_name or '').lower()
        purpose = (requirement.educational_purpose or '').lower()
        keywords_text = ' '.join(requirement.search_keywords or []).lower()
        combined_text = f"{entity} {purpose} {keywords_text}"

        # Rule 2: Contains concrete physical indicators → eligible
        if any(indicator in combined_text for indicator in _CONCRETE_INDICATORS):
            return True

        # Rule 3: Purely abstract topic → skip (avoid irrelevant images)
        if any(abstract in entity for abstract in _ABSTRACT_INDICATORS):
            return False

        # Rule 4: Default — attempt Wikimedia retrieval
        return True

    def _build_primary_query(self, requirement: MediaRequirement) -> str:
        """
        Builds a context-rich primary query using available metadata.
        Format: "[entity] [educational context]" for best search precision.
        """
        parts = []

        # Entity name is the most reliable anchor
        if requirement.entity_name:
            parts.append(requirement.entity_name)
        elif requirement.scientific_name:
            parts.append(requirement.scientific_name)
        elif requirement.search_keywords:
            parts.append(requirement.search_keywords[0])
        elif requirement.aliases:
            parts.append(requirement.aliases[0])

        # Add educational context enrichment
        if requirement.media_category == "Real-world Visualization":
            # Append a concrete visual context hint
            if parts:
                entity_lower = parts[0].lower()
                # Only append if not already specific
                if not any(c in entity_lower for c in ['diagram', 'apparatus', 'photograph']):
                    parts.append("photograph")

        primary = ' '.join(parts).strip()
        if not primary:
            primary = requirement.educational_purpose or "educational diagram"

        return primary

    def _build_alternate_queries(self, requirement: MediaRequirement, primary_query: str) -> list[str]:
        """
        Builds a layered fallback query chain for progressive search.
        """
        alternates = []
        seen = {primary_query.lower()}

        def _add(q: str):
            q = q.strip()
            if q and q.lower() not in seen:
                seen.add(q.lower())
                alternates.append(q)

        # Fallback 1: entity + scientific name combination
        if requirement.entity_name and requirement.scientific_name:
            _add(f"{requirement.entity_name} {requirement.scientific_name}")

        # Fallback 2: entity + "diagram" or "apparatus"
        if requirement.entity_name:
            _add(f"{requirement.entity_name} diagram")
            _add(f"{requirement.entity_name} scientific illustration")

        # Fallback 3: scientific name alone
        if requirement.scientific_name:
            _add(requirement.scientific_name)

        # Fallback 4: aliases
        for alias in (requirement.aliases or []):
            _add(alias)

        # Fallback 5: search_keywords (domain-specific terms)
        for kw in (requirement.search_keywords or []):
            _add(kw)

        # Fallback 6: related_concepts (broadening)
        for related in (requirement.related_concepts or []):
            _add(related)

        # Fallback 7: educational purpose as last resort
        purpose = requirement.educational_purpose or ''
        if purpose and len(purpose) < 80:
            _add(purpose)

        return alternates
