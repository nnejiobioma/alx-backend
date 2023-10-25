#!/usr/bin/python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system:
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    summarize
    Overwrite functions 'put' and 'get' for implement MRU caching system.
    """

    def __init__(self):
        """ Initiliaze.
        """
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """ The dictionary self.cache_data is asigned the item
            value for the key description.
        """
        if key and item is not None:
            if key not in self.cache_data:
                self.cache.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keyF = self.cache.pop(-2)
            self.cache_data.pop(keyF)
            print("DISCARD: {}".format(keyF))

    def get(self, key):
        """ Return:
            The value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data:
            self.cache.remove(key)
            self.cache.append(key)
        return self.cache_data.get(key)
