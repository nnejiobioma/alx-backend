#!/usr/bin/python3
""" This Module creates a LRU caching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
	Overwrite functions 'put' and 'get' for implement LRU caching system.
    """

    def __init__(self):
        """ Initiliaze.
        """
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """ Assign dictionary self.cache_data the item
        """
        if key and item is not None:
            if key in self.cache_data:
                self.cache.remove(key)
            self.cache_data[key] = item
            self.cache.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keyF = self.cache.pop(0)
            self.cache_data.pop(keyF)
            print("DISCARD: {}".format(keyF))

    def get(self, key):
        """The value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data:
            self.cache.remove(key)
            self.cache.append(key)
        return self.cache_data.get(key)
