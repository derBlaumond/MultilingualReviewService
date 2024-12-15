from collections import OrderedDict
from typing import Optional

class Cache:
    """
    A simple in-memory cache with optional size limit and LRU eviction.
    """
    def __init__(self, max_size: Optional[int] = 100):
        self.cache = OrderedDict()
        self.max_size = max_size

    def __contains__(self, key):
        return key in self.cache

    def __getitem__(self, key):
        # Move key to the end to mark it as recently used
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def __setitem__(self, key, value):
        # Evict the oldest entry if the cache exceeds its size limit
        if self.max_size and len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def clear(self):
        self.cache.clear()


cache = {}

async def translate_text_with_cache(text: str, target_language: str) -> str:
    """
    Translates text to the target language and caches the result.

    Args:
        text (str): The text to translate.
        target_language (str): The target language code (e.g., 'en', 'de').

    Returns:
        str: The translated text.
    """
    cache_key = f"{text}:{target_language}"
    if cache_key in cache:
        return cache[cache_key]

    translated_text = f"Translated '{text}' to {target_language}"
    cache[cache_key] = translated_text
    return translated_text