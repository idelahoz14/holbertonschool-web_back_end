#!/usr/bin/env python3
""" LIFO caching """
BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.last}")
                del(self.cache_data[self.last])
            self.last = key

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)

        return None
