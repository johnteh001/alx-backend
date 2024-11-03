#!/usr/bin/env python3
"""LFU Caching"""

import collections
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system"""
    def __init__(self):
        """Initializes cache"""
        super().__init__()
        self.cache_data = collections.OrderedDict(self.cache_data)

    def put(self, key, item):
        """Adds elements to cache"""
        if key and item:
            if self.cache_data and \
                    len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lis = [key for key in self.cache_data.keys()]
                if key not in lis:
                    key_discard = self.cache_data.popitem(last=False)
                    print("DISCARD: {}".format(key_discard[0]))
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache using key"""
        if key and key in self.cache_data.keys():
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
