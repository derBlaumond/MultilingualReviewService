from fastapi import APIRouter, HTTPException
from .database import reviews_collection
from .models import Review
#from .utils import trigger_translation

router = APIRouter()

#Add review
@router.post("/reviews")
async def add_review(review: Review):
    """
    Adds a new review to MongoDB and triggers the TranslationService to translate the content.
    """
    try:
        review_dict = review.dict()
        #review_dict["translations"] = {}

        result = reviews_collection.insert_one(review_dict)
        review_dict["_id"] = str(result.inserted_id) 

        #await trigger_translation(review_dict)

        return {"message": "Review added", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

#Get reviews by product ID and language
@router.get("/reviews")
async def get_reviews(product_id: int):                                             # language: str = "en" removed
    product_reviews = list(reviews_collection.find({"product_id": product_id}))
    if not product_reviews:
        raise HTTPException(status_code=404, detail="No reviews found")
    return [
        {
            "review_id": str(review["_id"]),
            "product_id": review["product_id"],
            "user_id": review["user_id"],
            "rating": review["rating"],
            "content": review["content"]
            #"language": review["language"],
            #"translations": review.get("translations", {})
        }
        for review in product_reviews
    ]