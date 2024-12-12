cache = {}

async def cached_translate_text(text: str, target_language: str) -> str:
    cache_key = f"{text}:{target_language}"
    if cache_key in cache:
        return cache[cache_key]
    
    # Perform actual translation (mocked for now)
    translated_text = f"Translated '{text}' to {target_language}"
    cache[cache_key] = translated_text
    return translated_text