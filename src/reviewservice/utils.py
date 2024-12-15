import os
import httpx
from bson.objectid import ObjectId
from .database import reviews_collection

async def trigger_translation(review):
    """
    Calls the TranslationService to translate the review content into multiple target languages.
    Updates the MongoDB document with the translated texts.
    """
    target_languages = [review["language"], "fr", "de"]  # List of target languages to translate to
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")

    try:
        
        for language in target_languages:

            payload = {
                "text": review["content"],
                "targetLanguage": language,
                "key": api_key
            }

            # Make asynchronous HTTP call to TranslationService
            async with httpx.AsyncClient() as client:
                response = await client.post("http://translationservice:8001/translate", json=payload)
                response.raise_for_status()

            # Extract the translated text from the response
            translated_text = response.json().get("translated_text")

            if translated_text:
            # Update the MongoDB document with the translated text for the current language
                reviews_collection.update_one(
                    {"_id": ObjectId(review["_id"])},
                    {"$set": {f"translations.{language}": review["content"]}}
                )
            else:
                print(f"No translated text received for language '{language}'.")

        print(f"Translations for review ID {review['_id']} updated successfully.")
    except httpx.RequestError as e:
        print(f"An error occurred while contacting the TranslationService: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
