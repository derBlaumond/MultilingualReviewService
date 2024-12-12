import httpx
from bson.objectid import ObjectId
from .database import reviews_collection

async def trigger_translation(review):
    """
    Calls the TranslationService to translate the review content into a specified target language
    and updates the MongoDB record with the translated text.
    """
    try:
        payload = {
            "text": review["content"],
            "targetLanguage": "fr" 
        }

        async with httpx.AsyncClient() as client:
            response = await client.post("http://translationservice:8001/translate", json=payload)
            response.raise_for_status()

        translated_text = response.json().get("translated_text")

        reviews_collection.update_one(
            {"_id": ObjectId(review["_id"])}, 
            {"$set": {f"translations.fr": translated_text}} 
        )
    except httpx.RequestError as e:
        print(f"An error occurred while contacting the TranslationService: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
