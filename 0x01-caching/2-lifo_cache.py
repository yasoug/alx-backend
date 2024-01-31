#!/usr/bin/env python3
"""LIFOCache Module"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.last = None

    def put(self, key, item):
        """
        Assigns the item value to the cache
        and discards the last item put in cache when it is full
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.last)
                print(f'DISCARD: {self.last}')
            self.last = key

    def get(self, key):
        """Retrieves the value linked to key from the cache"""
        return self.cache_data.get(key, None)
