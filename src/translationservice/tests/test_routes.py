from fastapi.testclient import TestClient
from src.translationservice.routes import router
from fastapi import FastAPI

# Create a FastAPI test app
app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_translate_valid_request():
    """
    Test a valid request to the translation endpoint.
    """
    response = client.post(
        "/translate",
        json={"text": "Hello world", "targetLanguage": "de"}
    )
    assert response.status_code == 200
    assert response.json() == {"translated_text": "Translated 'Hello world' to de"}

def test_translate_invalid_language():
    """
    Test a request with an unsupported target language.
    """
    response = client.post(
        "/translate",
        json={"text": "Hello world", "targetLanguage": "xx"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Language 'xx' is not supported"

def test_translate_empty_text():
    """
    Test a request with empty text.
    """
    response = client.post(
        "/translate",
        json={"text": "", "targetLanguage": "de"}
    )
    assert response.status_code == 422  # Unprocessable Entity