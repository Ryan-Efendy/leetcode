from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key: int, val: int, count: int):
        self.key = key
        self.val = val
        self.count = count

"""
key2node = {
    1: Node(1, 1, 1),
    2: Node(2, 2, 1),
    3: Node(3, 3, 2),
    4: Node(4, 4, 1)
}

count2node = {
    1: {
        1: Node(1, 1, 1),
        2: Node(2, 2, 1), <--- delete, update count to 2, move to count 2 bucket
        4: Node(4, 4, 1)
    },
    2 : {
        3: Node(3, 3, 2)
    }
}

"""
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.min_count = None

    def get(self, key: int) -> int:
        if key not in self.key2node: return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key]
        
        # clean memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]
        
        node.count += 1
        self.count2node[node.count][key] = node
        
        if not self.count2node[self.min_count]:
            self.min_count += 1
        
        return node.val

    def put(self, key: int, val: int) -> None:
        if not self.capacity: return
        
        if key in self.key2node:
            self.key2node[key].val = val # update val
            self.get(key)
        else:
            if len(self.key2node) == self.capacity:
                k, _ = self.count2node[self.min_count].popitem(last=False)
                del self.key2node[k]
            
            new_node = Node(key, val, 1)
            self.key2node[key] = new_node
            self.count2node[1][key] = new_node
            self.min_count = 1
            
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)