import collections


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                # remove LRU
                self.cache.popitem(False)
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# capacity = 2


obj = LRUCache(2)
# param_1 = obj.get(key)
# obj.put(key,value)
# obj.put(1, 1);
# obj.put(2, 2);
# obj.get(1);       #// returns 1
# obj.put(3, 3);            #// evicts key 2
# obj.get(2);       #// returns -1 (not found)
# obj.put(4, 4);           # // evicts key 1
# obj.get(1);       #// returns -1 (not found)
# obj.get(3);      # // returns 3
# obj.get(4);      # // returns 4

# obj.put(1,1)
# obj.put(2,2)
# obj.get(1)
# obj.put(3,3)
# obj.get(2)
# obj.put(4,4)
# obj.get(1)
# obj.get(3)
# obj.get(4)

obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)
obj.get(1)
obj.get(2)

# find the first unique word from a keep coming string list
# system design question is to set users's preference and make it scable to consistent
