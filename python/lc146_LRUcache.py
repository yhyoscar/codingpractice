# lc 146
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys   = [None for i in range(capacity)]
        self.values = [None for i in range(capacity)]
        self.rank   = [None for i in range(capacity)]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #print('get ', key, self.keys, self.values, self.rank)
        if key in self.keys:
            if None in self.keys:
                n = self.keys.index(None)
                self.rank[self.keys.index(key)] = max(self.rank[:n]) + 1                
            else:
                self.rank[self.keys.index(key)] = max(self.rank) + 1
            return self.values[self.keys.index(key)]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if None in self.keys:
            n = self.keys.index(None)
            if key in self.keys:
                self.values[self.keys.index(key)] = value
                self.rank[self.keys.index(key)] = max(self.rank[:n]) + 1
            else:
                self.keys[n] = key
                self.values[n] = value
                self.rank[n] = max(self.rank[:n] + [n-1]) + 1
        else:
            if key in self.keys:
                self.values[self.keys.index(key)] = value
                self.rank[self.keys.index(key)] = max(self.rank) + 1
            else:
                old = self.rank.index(min(self.rank))
                self.keys[old] = key
                self.values[old] = value
                self.rank[old] = max(self.rank) + 1
        #print('put ', key, value, self.keys, self.values, self.rank)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

