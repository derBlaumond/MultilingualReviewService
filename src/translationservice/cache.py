class Cache(dict):
    """
    A simple cache implementation using a dictionary.
    """

    def __init__(self):
        super().__init__()

    def __contains__(self, key: str) -> bool:
        """
        Check if a key exists in the cache.
        """
        return key in self.keys()

    def __setitem__(self, key: str, value: str):
        """
        Add a key-value pair to the cache.
        """
        super().__setitem__(key, value)

    def __getitem__(self, key: str) -> str:
        """
        Retrieve a value from the cache by key.
        """
        return super().__getitem__(key)
    
cache = {}

async def translate_text_with_cache(text: str, target_language: str) -> str:
    cache_key = f"{text}:{target_language}"
    if cache_key in cache:
        return cache[cache_key]

    translated_text = f"Translated '{text}' to {target_language}"
    cache[cache_key] = translated_text
    return translated_text