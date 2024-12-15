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
    # Load API key from environment variables
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    if not api_key:
        raise Exception("Google Translate API key is missing. Set GOOGLE_TRANSLATE_API_KEY in the .env file.")

    # Google Translate API URL
    url = "https://translation.googleapis.com/language/translate/v2"

    params = {
        "q": text,
        "target": target_language,
        "key": api_key
    }

    try:
        # Send a POST request to the translation API
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)

        # Check if the response is successful
        if response.status_code != 200:
            raise Exception(f"Translation API Error: {response.status_code} - {response.text}")

        # Parse and return the translated text
        data = response.json()
        if "data" not in data or "translations" not in data["data"] or not data["data"]["translations"]:
            raise Exception("Unexpected response structure from the translation API.")

        return data["data"]["translations"][0]["translatedText"]
    except httpx.RequestError as e:
        raise Exception(f"An error occurred while requesting the translation API: {str(e)}")