import sys
import os
from fastapi.testclient import TestClient
from src.translationservice.main import app
from unittest.mock import AsyncMock, patch
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

client = TestClient(app)


def test_translate_valid_request():
    """
    Test the /translate endpoint with a valid request.
    """
    mock_translate_text = AsyncMock(return_value="Hallo Welt")
    with patch("src.translationservice.routes.translate_text", mock_translate_text):
        response = client.post(
            "/translate",
            json={"text": "Hello world", "targetLanguage": "de"}
        )
        assert response.status_code == 200
        assert response.json() == {"translated_text": "Hallo Welt"}


def test_translate_invalid_language():
    """
    Test the /translate endpoint with an unsupported language.
    """
    response = client.post(
        "/translate",
        json={"text": "Hello world", "targetLanguage": "fr"}
    )
    assert response.status_code == 422
    assert "detail" in response.json()
    assert "Language 'fr' is not supported" in response.json()["detail"][0]["msg"]


def test_translate_empty_text():
    """
    Test the /translate endpoint with an empty text.
    """
    response = client.post(
        "/translate",
        json={"text": "", "targetLanguage": "de"}
    )
    assert response.status_code == 422
    assert "detail" in response.json()
    assert "String should have at least 1 character" in response.json()["detail"][0]["msg"]


@pytest.mark.asyncio
async def test_translate_text_with_cache():
    """
    Test the cache functionality for translate_text.
    """
    result1 = await translate_text_with_cache("Hello", "de")
    assert result1 == "Translated 'Hello' to de"

    result2 = await translate_text_with_cache("Hello", "de")
    assert result2 == "Translated 'Hello' to de"

    result3 = await translate_text_with_cache("Goodbye", "de")
    assert result3 == "Translated 'Goodbye' to de"