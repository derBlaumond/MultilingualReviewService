from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    targetLanguage: str