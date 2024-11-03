#!/usr/bin/env python3
"""Task 1 Module"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initializes the cache"""
        super().__init__()

    def put(self, key, item):
        """Adds items in the cache"""
        if key and item:
            if self.cache_data and \
                    len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lis = [key for key in self.cache_data.keys()]
                if key not in lis:
                    key_discard = self.cache_data.pop(lis[0])
                    print("DISCARD: {}".format(lis[0]))
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key"""
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
