#!/usr/bin/env python3
"""Task 0 module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system inherits from BaseCaching"""
    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key"""
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
