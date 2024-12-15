from fastapi.testclient import TestClient
from src.translationservice.main import app
import os

print(f"API Key: {os.getenv('GOOGLE_TRANSLATE_API_KEY')}")

client = TestClient(app)

def test_translate_endpoint():
    response = client.post("/translate", json={"text": "Hello", "targetLanguage": "de"})
    assert response.status_code == 200
    assert "translated_text" in response.json()
    assert response.json()["translated_text"] == "Hallo Welt" 