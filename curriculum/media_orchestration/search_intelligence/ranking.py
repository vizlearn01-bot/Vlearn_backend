import re
from typing import List, Optional
from curriculum.media_orchestration.contracts import ResolvedAsset

# Keywords in image titles that suggest educational value
_EDUCATIONAL_BOOST_PATTERN = re.compile(
    r'\b(diagram|apparatus|reaction|process|structure|laboratory|lab|'
    r'experiment|cross.section|illustration|schematic|anatomy|cross_section|'
    r'industrial|factory|plant|cycle|mechanism|photograph|scientific|animation|demonstration)\b',
    re.IGNORECASE
)

class AssetRankingEngine:
    """
    Ranks a collection of ResolvedAssets based on deterministic quality heuristics.
    Prioritizes: matching preferred_type, resolution, educational title, license quality, metadata completeness.
    Penalizes: small images, missing metadata.
    """

    def rank_assets(self, assets: List[ResolvedAsset], preferred_type: Optional[str] = None) -> List[ResolvedAsset]:
        if not assets:
            return []

        norm_preferred = (preferred_type or "").lower().strip()

        def score_asset(asset: ResolvedAsset) -> float:
            score = 0.0

            # 0. Preferred type match bonus
            a_type = (asset.asset_type or "").lower().strip()
            if norm_preferred:
                if a_type == norm_preferred:
                    score += 60
                elif norm_preferred == 'video' and a_type in ('video', 'youtube'):
                    score += 60
                elif norm_preferred in ('image', 'diagram') and a_type in ('image', 'diagram'):
                    score += 30

            # 1. Base confidence from provider
            score += asset.confidence_score * 50

            # 2. Verified asset bonus
            if asset.verified or asset.provider == 'YouTube':
                score += 30

            # 3. License quality
            lic = (asset.licensing or "").lower()
            if "cc0" in lic or "public domain" in lic:
                score += 20
            elif "cc-by-sa" in lic or "cc-by" in lic:
                score += 15
            elif "standard youtube license" in lic or "youtube" in lic:
                score += 15
            elif "cc" in lic:
                score += 10
            elif "proprietary" in lic:
                score += 5

            # 4. Metadata completeness
            if asset.author and asset.author not in ("Unknown", "Unknown Author", ""):
                score += 5
            if asset.attribution:
                score += 5

            # 5. Media-specific scoring
            if a_type in ('video', 'youtube') or asset.provider == 'YouTube':
                # Video bonus: verified public oEmbed embed
                if (asset.metadata or {}).get('video_id'):
                    score += 25
            else:
                # Image resolution scoring (only for images/diagrams)
                width = (asset.metadata or {}).get("width", 0) or 0
                height = (asset.metadata or {}).get("height", 0) or 0
                if isinstance(width, (int, float)) and isinstance(height, (int, float)):
                    if width >= 1600 or height >= 1200:
                        score += 20  # Excellent resolution
                    elif width >= 1024 and height >= 768:
                        score += 12
                    elif width >= 800 and height >= 600:
                        score += 6
                    elif width > 0 and height > 0 and (width < 300 or height < 300):
                        score -= 15  # Penalise tiny images

                # File format preference for static images
                url = (asset.url or "").lower()
                if url.endswith(".svg"):
                    score += 12  # SVG diagrams are often clearest
                elif url.endswith(".png"):
                    score += 6
                elif url.endswith((".jpg", ".jpeg")):
                    score += 5

            # 6. Educational title boost
            title = asset.alt_text or ""
            if _EDUCATIONAL_BOOST_PATTERN.search(title):
                score += 15

            return score

        return sorted(assets, key=score_asset, reverse=True)
