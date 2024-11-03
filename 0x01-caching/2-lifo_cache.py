#!/usr/bin/env python3
"""LIFO Caching Module"""

import collections
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """Initializes the LIFO cache"""
        super().__init__()
        self.cache_data = collections.OrderedDict(self.cache_data)

    def put(self, key, item):
        """Adds items to the cache"""
        if key and item:
            if self.cache_data and \
                    len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    discard_tuple = self.cache_data.popitem()
                    print("DISCARD: {}".format(discard_tuple[0]))
            self.cache_data[key] = item

    def get(self, key):
        """Gets value for given key"""
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
