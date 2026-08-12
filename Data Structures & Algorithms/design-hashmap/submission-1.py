class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        # Insert key value pair into the map
        if self.get(key) == -1:
            self.hashmap.append([key,value])
        else:
        # If key already exists --> update value
            self.remove(key)
            self.hashmap.append([key,value])

    def get(self, key: int) -> int:
        # If key exists return value
        for k,val in self.hashmap:
            if key == k:
                return val
        # Else return -1
        return -1

    def remove(self, key: int) -> None:
        # If key exists --> remove mapping for key
        if self.get(key) != -1:
            for i in range(len(self.hashmap)):
                if self.hashmap[i][0] == key:
                    self.hashmap.pop(i)
                    return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)