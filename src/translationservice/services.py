import httpx

async def translate_text(text: str, target_language: str) -> str:
    """
    Translate the given text to the target language using Google Translate API.

    Args:
        text (str): The text to translate.
        target_language (str): The target language (e.g., 'de' for German).

    Returns:
        str: Translated text.
    """
    # Google Translate API URL
    url = "https://translation.googleapis.com/language/translate/v2"

    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = "YOUR_API_KEY"

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
            raise Exception(f"Translation API Error: {response.status_code}")

        # Parse and return the translated text
        data = response.json()
        return data["data"]["translations"][0]["translatedText"]

    except httpx.RequestError as e:
        raise Exception(f"HTTP Request failed: {e}")

    except KeyError:
        raise Exception("Unexpected response structure from Translation API.")