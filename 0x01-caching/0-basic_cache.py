#!/usr/bin/env python3
"""BasicCache Module"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initializes the cache"""
        super().__init__()

    def put(self, key, item):
        """Assigns the item value to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value linked to key from the cache"""
        return self.cache_data.get(key, None)
