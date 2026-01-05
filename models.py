#Pydantic models for request/response

from pydantic import BaseModel
from typing import List

# Request model for text input
class AnalyzeRequest(BaseModel):
    text: str
    consent: bool = True
    input_type: str = "text"  # text or screenshot

# Response model
class AnalyzeResponse(BaseModel):
    verdict: str              # Scam / Suspicious / Safe
    confidence: str           # Low / Medium / High
    scam_type: str            # e.g. "account takeover"
    reason: List[str]         # why it's flagged
    recommended_action: List[str]  # what to do
