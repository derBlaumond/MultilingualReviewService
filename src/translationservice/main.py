from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

SUPPORTED_LANGUAGES = {"de"}

class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to be translated, cannot be empty.")
    targetLanguage: str = Field(..., description="Target language code (e.g., 'de').")

def translate_text(text: str, target_language: str) -> str:
    if not text:
        raise ValueError("Text cannot be empty")
    if target_language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {target_language}")
    if target_language == "de":
        return "Hallo Welt"
    return "Translation not available"

app = FastAPI()

@app.post("/translate")
async def translate(payload: TranslateRequest):
    try:
        translated_text = translate_text(payload.text, payload.targetLanguage)
        return {"translated_text": translated_text}
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))  # 422 상태 코드 반환
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # 500 상태 코드 반환