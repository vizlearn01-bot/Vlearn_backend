from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ValidationCheck(BaseModel):
    severity: str = Field(description="'ok', 'warning', or 'error'")
    label: str = Field(description="Short description of the check")
    detail: Optional[str] = Field(default=None, description="Detailed explanation if failed")

class ValidationReport(BaseModel):
    checks: List[ValidationCheck] = Field(default_factory=list)
    
    @property
    def has_errors(self) -> bool:
        return any(c.severity == 'error' for c in self.checks)
        
    def add_error(self, label: str, detail: str):
        self.checks.append(ValidationCheck(severity='error', label=label, detail=detail))
        
    def add_warning(self, label: str, detail: str):
        self.checks.append(ValidationCheck(severity='warning', label=label, detail=detail))
        
    def add_ok(self, label: str, detail: Optional[str] = None):
        self.checks.append(ValidationCheck(severity='ok', label=label, detail=detail))

class QualityScore(BaseModel):
    score: int = Field(description="0-100 deterministic score")
    metrics: Dict[str, Any] = Field(description="Breakdown of deterministic metrics")
    recommendations: List[str] = Field(default_factory=list, description="Optimization recommendations")
    
class EngineReport(BaseModel):
    """The final payload stored in the database for the Content Studio"""
    validation: ValidationReport = Field(default_factory=ValidationReport)
    quality: QualityScore = Field(default_factory=lambda: QualityScore(score=0, metrics={}))
    optimized: bool = Field(default=False)
