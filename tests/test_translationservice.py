import pytest
from unittest.mock import AsyncMock
from src.translationservice.services import translate_text

@pytest.mark.asyncio
async def test_translate_text_valid_request(mocker):
    # Mock the HTTP response for a valid API call
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json = AsyncMock(  # Adjusted to match async usage
        return_value={
            "data": {"translations": [{"translatedText": "Hallo Welt"}]}
        }
    )
    mocker.patch("httpx.AsyncClient.post", return_value=mock_response)

    # Call the function being tested
    result = await translate_text("Hello world", "de")
    assert result == "Hallo Welt"


@pytest.mark.asyncio
async def test_translate_text_invalid_response_structure(mocker):
    # Mock the HTTP response for an invalid structure
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json = AsyncMock(
        return_value={"unexpected_key": "unexpected_value"}
    )
    mocker.patch("httpx.AsyncClient.post", return_value=mock_response)

    # Test for an exception due to unexpected response structure
    with pytest.raises(Exception, match="Unexpected response structure"):
        await translate_text("Hello world", "de")


@pytest.mark.asyncio
async def test_translate_text_api_failure(mocker):
    # Mock the HTTP response for an API failure (500 status code)
    mock_response = AsyncMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_response.json = AsyncMock(return_value={})
    mocker.patch("httpx.AsyncClient.post", return_value=mock_response)

    # Test for an exception due to API failure
    with pytest.raises(Exception, match="Translation API Error: 500"):
        await translate_text("Hello world", "de")