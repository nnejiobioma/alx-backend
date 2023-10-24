#!/usr/bin/python3
"""
BaseCache module for creating a FIFO caching.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
	From BaseCaching and is a caching system.
        Functions Overwrite 'put' and 'get' for
	implement FIFO caching system.
    """

    def __init__(self):
        """
	Initiliaze.
        """
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """
	modify cache data

            Args:
                key: of the dict
                item: value of the key
	Assign to the dictionary self.cache_data the item
        value for the key.
        """
        if key and item is not None:
            self.cache_data[key] = item
            self.cache.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keyF = self.cache.pop(0)
            self.cache_data.pop(keyF)
            print("DISCARD: {}".format(keyF))

    def get(self, key):
        """
	 modify cache data

            Args:
                key: of the dict

            Return:
                value of the key
        """
        return self.cache_data.get(key)
