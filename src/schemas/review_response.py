from pydantic import BaseModel
from typing import List, Dict, Any

class AgentOutput(BaseModel):
    category: str
    chunk_id: str
    response: Dict[str, Any]

class ReviewResponse(BaseModel):
    success: bool
    results: List[AgentOutput]
