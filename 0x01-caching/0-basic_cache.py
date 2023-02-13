#!/usr/bin/env  python3
"""
basic caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching class
    """

    def put(self, key, item):
        """add to cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get from cache"""
        if not key:
            return None

        return self.cache_data.get(key)
