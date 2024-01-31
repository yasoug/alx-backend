#!/usr/bin/env python3
"""LFUCache Module"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """
        Assigns the item value to the cache
        and discards the least frequency used item when it is full
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                k = min(self.keys, key=self.keys.get)
                self.cache_data.pop(k)
                print(f'DISCARD: {k}')
                self.keys.pop(k)
            if key not in self.keys:
                self.keys[key] = 0

    def get(self, key):
        """Retrieves the value linked to key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.keys:
            self.keys[key] += 1
        return self.cache_data[key]
