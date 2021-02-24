class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.next = self.tail, self.head
        self.head.prev, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.map:
            self.remove(self.map[key])
        self.insert(node)
        self.map[key] = node
        
        if len(self.map) > self.capacity: # evict least recently used key
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.map[node_to_delete.key]
            
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)