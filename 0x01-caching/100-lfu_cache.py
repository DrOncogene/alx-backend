#!/usr/bin/env  python3
"""
LFU caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU caching class
    """

    def __init__(self):
        super().__init__()
        self.access_count = {}

    def put(self, key, item):
        """add to cache"""
        if not key or not item:
            return

        size = len(self.cache_data)
        if size >= self.MAX_ITEMS and key not in self.cache_data:
            lfu = min(self.access_count.values())
            lfu_key = [k for k, v in self.access_count.items() if v == lfu]

            print(f'DISCARD: {lfu_key[0]}')
            del self.cache_data[lfu_key[0]]
            del self.access_count[lfu_key[0]]

        self.cache_data[key] = item
        if key not in self.access_count:
            self.access_count[key] = 0
        else:
            self.access_count[key] += 1

    def get(self, key):
        """get from cache"""
        if not key:
            return None

        if key in self.cache_data:
            self.access_count[key] += 1
        return self.cache_data.get(key)
