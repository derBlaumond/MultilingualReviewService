import pytest
from src.translationservice.services import translate_text
from src.translationservice.cache import cached_translate_text

@pytest.mark.asyncio
async def test_translate_text_valid():
    """
    Test the translation service with valid inputs.
    """
    result = await translate_text("Hello world", "de")
    assert result == "Translated 'Hello world' to de"

@pytest.mark.asyncio
async def test_translate_text_invalid_language():
    """
    Test the translation service with an unsupported language.
    """
    with pytest.raises(Exception) as exc_info:
        await translate_text("Hello world", "xx")
    assert "Translation API Error" in str(exc_info.value)