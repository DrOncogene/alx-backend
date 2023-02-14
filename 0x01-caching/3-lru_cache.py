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
        self.access_list = []

    def put(self, key, item):
        """add to cache"""
        if not key or not item:
            return

        size = len(self.cache_data)
        if size >= self.MAX_ITEMS and key not in self.cache_data:
            lru = self.access_list.pop(0)

            print(f'DISCARD: {lru}')
            del self.cache_data[lru]

        if key in self.cache_data:
            key_idx = self.access_list.index(key)
            self.access_list.pop(key_idx)
            self.access_list.append(key)

        if key not in self.access_list:
            self.access_list.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """get from cache"""
        if not key:
            return None

        if key in self.cache_data:
            key_idx = self.access_list.index(key)
            self.access_list.pop(key_idx)
            self.access_list.append(key)

        return self.cache_data.get(key)
