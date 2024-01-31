#!/usr/bin/env python3
"""LRUCache Module"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assigns the item value to the cache
        and discards the least recently used item when it is full
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.keys[0])
                print(f'DISCARD: {self.keys[0]}')
                self.keys.pop(0)

    def get(self, key):
        """Retrieves the value linked to key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
