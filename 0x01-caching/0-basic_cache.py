#!/usr/bin/python3
"""
Basic Cache that inherits from
Basic Catching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system.
    Overwrite functions 'put' and 'get'
    A basic cache implementaion class

    The Attributes:
    MAX_ITEMS: number of items that can be store in the cache
    """
    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item
        value for the key.
        Add an item in the cache
        """
        if key and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        This gets an item by key
        Returns the value of in self.cache_data
        linked to key
        """
        return self.cache_data.get(key, None)
