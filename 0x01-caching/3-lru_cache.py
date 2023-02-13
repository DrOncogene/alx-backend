#!/usr/bin/env  python3
"""
LRU caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching class
    """

    def __init__(self):
        super().__init__()
        self.access_list = {}

    def put(self, key, item):
        """add to cache"""
        if not key or not item:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            least = min(self.access_list.values())
            least_key = None
            for k, v in self.access_list.items():
                if v != least:
                    continue
                least_key = k
                break

            print(f'DISCARD: {least_key}')
            del self.cache_data[least_key]
            del self.access_list[least_key]

        self.cache_data[key] = item
        if not self.access_list.get(key):
            self.access_list[key] = 0

    def get(self, key):
        """get from cache"""
        if not key:
            return None

        if self.access_list.get(key):
            self.access_list[key] += 1

        return self.cache_data.get(key)
