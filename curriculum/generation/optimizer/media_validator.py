from curriculum.models import Lesson
from .models import ValidationReport

class MediaValidator:
    """
    Agent 5: Media Validator.
    Runs POST-Agent 4 to verify that the orchestration engine correctly resolved media.
    """
    
    @staticmethod
    def validate_media(lesson: Lesson) -> ValidationReport:
        report = ValidationReport()
        assets = lesson.assets.all()
        
        total_assets = assets.count()
        if total_assets == 0:
            report.add_warning("No Media", "No media assets were orchestrated for this lesson.")
            return report
            
        pending_assets = assets.filter(status='pending').count()
        attached_assets = assets.filter(status='attached').count()
        
        if pending_assets > 0:
            report.add_warning(
                "Unresolved Media Slots",
                f"{pending_assets} media requirements failed to resolve and degraded to pending slots. Manual authoring required."
            )
        
        if attached_assets > 0:
            report.add_ok("Media Orchestration", f"Successfully resolved {attached_assets} media assets.")
            
        # Check for fallback usage
        fallback_assets = assets.filter(metadata__fallback_used=True).count()
        if fallback_assets > 0:
            report.add_ok(
                "Fallback Utilization", 
                f"{fallback_assets} assets degraded gracefully to a fallback media type."
            )
            
        return report
