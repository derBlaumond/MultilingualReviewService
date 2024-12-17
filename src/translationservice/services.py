import os
import httpx
from dotenv import load_dotenv

load_dotenv()

async def translate_text(text: str, target_language: str) -> str:
    """
    Translate the given text to the target language using Google Translate API.

    Args:
        text (str): The text to translate.
        target_language (str): The target language (e.g., 'de' for German).

    Returns:
        str: Translated text.
    """
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    if not api_key:
        raise Exception("Google Translate API key is missing. Set GOOGLE_TRANSLATE_API_KEY in the .env file.")

    url = "https://translation.googleapis.com/language/translate/v2"

    params = {
        "q": text,
        "target": target_language,
        "key": api_key,
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)

        if response.status_code != 200:
            raise Exception(f"Translation API Error: {response.status_code} - {response.text}")

        # Await the async JSON parsing
        data = await response.json()
        if not data.get("data") or not data["data"].get("translations"):
            raise Exception("Unexpected response structure")

        return data["data"]["translations"][0]["translatedText"]

    except Exception as e:
        raise Exception(f"Failed to translate text: {str(e)}")