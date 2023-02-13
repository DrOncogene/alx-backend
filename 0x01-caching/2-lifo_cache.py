#!/usr/bin/env  python3
"""
LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO caching class
    """

    def __init__(self):
        super().__init__()
        self.last_item = None

    def put(self, key, item):
        """add to cache"""
        if not key or not item:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            print(f'DISCARD: {self.last_item}')
            del self.cache_data[self.last_item]

        self.last_item = key

    def get(self, key):
        """get from cache"""
        if not key:
            return None

        return self.cache_data.get(key)
