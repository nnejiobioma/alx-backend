#!/usr/bin/python3
"""
BaseCache module
LIFO Cache Replacement Implementation Class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Define a FIFO algorithm to use cache
    An implementation of LIFO(Last In Fisrt Out) Cache
    """

    def __init__(self):
        """ Initiliaze sets instance attributes
        """
        super().__init__()

    def put(self, key, item):
        """
        modify cache data
        Add an item in the cache
        """
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keyF = list(self.cache_data.keys())
                    lenlast = len(keyF) - 1
                    del self.cache_data[keyF[lenlast]]
                    print("DISCARD: {}".format(keyF[lenlast]))
                else:
                    del self.cache_data[key]
                    self.cache_data[key] = item

    def get(self, key):
        """
            modify cache data

            Args:
                key: of the dict

            Return:
                value of the key
        """

        valuecache = self.cache_data.get(key)
        return valuecache
