#!/usr/bin/env python3
""" FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOcache """
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first}")
                del(self.cache_data[first])

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)

        return None
