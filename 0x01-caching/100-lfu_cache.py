#!/usr/bin/python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find and discard the most recently used item
            mru_key = max(self.access_time, key=lambda k: self.access_time[k])
            del self.cache_data[mru_key]
            del self.access_time[mru_key]
            print(f"DISCARD: {mru_key}\n")

        # Update the access time for the current item
        self.access_time[key] = self.current_time
        self.current_time += 1

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Update the access time for the accessed item
        self.access_time[key] = self.current_time
        self.current_time += 1

        return self.cache_data[key]
