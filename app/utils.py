from bson.objectid import ObjectId
from .database import reviews_collection

#Simulate translation by copying the 'content' field into 'translations'.

async def trigger_translation(review):

    try:
        # Use the same content as the translation
        translated_text = review["content"]
        reviews_collection.update_one(
            {"_id": ObjectId(review["_id"])},
            {"$set": {f"translations.fr": translated_text}}, 
        )
    except Exception as e:
        print(f"Error simulating translation: {e}")
