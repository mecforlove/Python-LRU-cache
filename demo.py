from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def set(self, key, value):
        try:
            self.data.pop(key)
        except KeyError:
            if len(self.data) >= self.capacity:
                self.data.popitem(last=False)
        self.data[key] = value

    def get(self, key):
        try:
            v = self.data.pop(key)
            self.data[key] = v
            return v
        except IndexError:
            return -1