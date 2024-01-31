#!/usr/bin/env python3
"""FIFOCache Module"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initializes the cache"""
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value to the cache
        and discards the first item put in cache when it is full
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key = next(iter(self.cache_data))
                self.cache_data.pop(key)
                print(f'DISCARD: {key}')

    def get(self, key):
        """Retrieves the value linked to key from the cache"""
        return self.cache_data.get(key, None)
