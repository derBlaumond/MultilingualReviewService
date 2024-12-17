from typing import Annotated
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator
from .services import translate_text  # Relative import
from .cache import Cache  # Relative import
from fastapi import HTTPException


router = APIRouter()

# Initialize cache for storing translations
cache = Cache()

SUPPORTED_LANGUAGES = ["de", "en"]

# Define the request schema using Pydantic
class TranslationRequest(BaseModel):
    text: Annotated[str, Field(min_length=1, max_length=500)]  # Limit text size to prevent abuse
    targetLanguage: Annotated[str, Field(pattern="^[a-z]{2}$")]  # Expect ISO 639-1 language codes (e.g., "en", "de")

    # @field_validator("targetLanguage")
    # def validate_language(cls, value):
    #     """
    #     Validate that the targetLanguage is supported.
    #     """
    #     supported_languages = ["de"]  # Only German is supported
    #     if value not in supported_languages:
    #         raise ValueError(f"Language '{value}' is not supported")
    #     return value


# Define the translation endpoint
@router.post(
    "/translate",
    summary="Translate text to the target language",
    response_model=dict,
    status_code=200,
)
async def translate(request: TranslationRequest):
    """
    Translates the given text into the specified target language.

    Args:
        request (TranslationRequest): The request body containing the text and target language.

    Returns:
        dict: A dictionary containing the translated text.
    """
    try:
        # Validate that the target language is supported
        if request.targetLanguage not in SUPPORTED_LANGUAGES:
            raise HTTPException(
                status_code=422,
                detail=f"Language '{request.targetLanguage}' is not supported"
            )

        # Check if the translation is already in the cache
        cache_key = f"{request.text}:{request.targetLanguage}"
        if cache_key in cache:
            return {"translated_text": cache[cache_key]}

        # Call the translation service logic
        translated_text = await translate_text(request.text, request.targetLanguage)

        # Store the result in cache
        cache[cache_key] = translated_text

        return {"translated_text": translated_text}
    except ValueError as ve:
        # Handle validation or service-specific errors
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")