from pydantic import BaseModel

class ReviewRequest(BaseModel):
    file_path: str
