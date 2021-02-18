class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        if not key or not len(key): return
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        if not prefix or not len(prefix): return None
        res = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                res += val
        
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)