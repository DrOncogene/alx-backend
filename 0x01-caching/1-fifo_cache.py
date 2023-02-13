#!/usr/bin/env  python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Basic caching class
    """

    def __init__(self):
        super().__init__()
        self.last_idx = 0

    def put(self, key, item):
        """add to cache"""
        if not key or not item:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            items = list(self.cache_data.keys())
            print(f'DISCARD: {items[0]}')
            del self.cache_data[items[0]]

    def get(self, key):
        """get from cache"""
        if not key:
            return None

        return self.cache_data.get(key)
