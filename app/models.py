from pydantic import BaseModel
from typing import Optional, Dict

class Review(BaseModel):
    product_id: int
    user_id: int
    rating: int
    content: str
    language: str
    translations: Optional[Dict[str, str]] = {}
