import pytest
from unittest.mock import AsyncMock
from src.translationservice.services import translate_text


@pytest.mark.asyncio
async def test_translate_text_valid_request(mocker):
    """
    Test translate_text with a valid response from the API.
    """
    # Mock the httpx.AsyncClient.post response
    mock_post = AsyncMock()
    mock_post.return_value.status_code = 200
    mock_post.return_value.json = AsyncMock(
        return_value={"data": {"translations": [{"translatedText": "Hallo Welt"}]}}
    )
    mocker.patch("httpx.AsyncClient.post", return_value=mock_post)

    # Call the function and check the result
    result = await translate_text("Hello world", "de")
    assert result == "Hallo Welt"


@pytest.mark.asyncio
async def test_translate_text_invalid_response_structure(mocker):
    """
    Test translate_text with an invalid response structure from the API.
    """
    # Mock the httpx.AsyncClient.post response with an unexpected structure
    mock_post = AsyncMock()
    mock_post.return_value.status_code = 200
    mock_post.return_value.json = AsyncMock(
        return_value={"unexpected_key": "unexpected_value"}
    )
    mocker.patch("httpx.AsyncClient.post", return_value=mock_post)

    # Call the function and check for the exception
    with pytest.raises(Exception) as exc_info:
        await translate_text("Hello world", "de")
    assert "Unexpected response structure" in str(exc_info.value)


@pytest.mark.asyncio
async def test_translate_text_api_failure(mocker):
    """
    Test translate_text with an API failure response.
    """
    # Mock the httpx.AsyncClient.post response with a 500 error
    mock_post = AsyncMock()
    mock_post.return_value.status_code = 500
    mock_post.return_value.text = "Internal Server Error"
    mocker.patch("httpx.AsyncClient.post", return_value=mock_post)

    # Call the function and check for the exception
    with pytest.raises(Exception) as exc_info:
        await translate_text("Hello world", "de")
    assert "Translation API Error: 500" in str(exc_info.value)


@pytest.mark.asyncio
async def test_translate_text_missing_api_key(mocker):
    """
    Test translate_text when the API key is missing.
    """
    # Temporarily remove the API key from the environment
    mocker.patch.dict("os.environ", {"GOOGLE_TRANSLATE_API_KEY": ""})

    # Call the function and check for the exception
    with pytest.raises(Exception) as exc_info:
        await translate_text("Hello world", "de")
    assert "Google Translate API key is missing" in str(exc_info.value)