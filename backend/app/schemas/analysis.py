from pydantic import BaseModel
from typing import List


class AnalysisResponse(BaseModel):
    match_score: int
    skills: List[str]
    missing_skills: List[str]
    improvements: List[str]
    cover_letter: str
