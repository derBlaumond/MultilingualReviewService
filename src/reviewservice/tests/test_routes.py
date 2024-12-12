import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from bson import ObjectId
from reviewservice.main import app
from reviewservice.database import reviews_collection 
client = TestClient(app)

# Mock data for testing
mock_review = {
    "_id": ObjectId(),
    "product_id": 123,
    "user_id": 456,
    "rating": 5,
    "content": "This product is amazing!",
    "language": "en",
    "translations": {"fr": "Ce produit est incroyable!"}
}


@pytest.fixture
def mock_mongo():
    """
    Fixture to mock MongoDB operations.
    """
    with patch("reviewservice.database.reviews_collection") as mock_collection:
        yield mock_collection


@pytest.fixture
def mock_translation_service():
    """
    Fixture to mock the TranslationService HTTP request.
    """
    with patch("reviewservice.utils.httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value.json.return_value = {"translated_text": "Ce produit est incroyable!"}
        yield mock_post


@pytest.mark.asyncio
async def test_post_review(mock_mongo, mock_translation_service):
    """
    Test the POST /reviews endpoint to ensure a review is stored and translation is triggered.
    """
    mock_mongo.insert_one.return_value.inserted_id = mock_review["_id"]

    response = client.post(
        "/reviews",
        json={
            "product_id": 123,
            "user_id": 456,
            "rating": 5,
            "content": "This product is amazing!",
            "language": "en"
        },
    )

    assert response.status_code == 200
    assert "id" in response.json()
    mock_mongo.insert_one.assert_called_once()
    mock_translation_service.assert_called_once()


def test_get_reviews(mock_mongo):
    """
    Test the GET /reviews endpoint to ensure reviews are retrieved correctly.
    """
    # Mock MongoDB find method
    mock_mongo.find.return_value = [mock_review]

    response = client.get("/reviews?product_id=123&language=fr")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["content"] == "Ce produit est incroyable!"
    mock_mongo.find.assert_called_once_with({"product_id": 123})
