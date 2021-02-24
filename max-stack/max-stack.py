from sortedcontainers import SortedDict

class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class MaxStack:
    def __init__(self):
        self.map = SortedDict()
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head

    def push(self, x: int) -> None:
        node = Node(x)
        self.insert(node)

    def pop(self) -> int:
        node = self.tail.prev
        self.remove(node)
        return node.val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        return self.map.peekitem()[0]

    def popMax(self) -> int:
        key, nodes = self.map.peekitem()
        self.remove(nodes[-1])
        return key
                
    def insert(self, node) -> None:
        prev, nxt = self.tail.prev, self.tail
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node
        
        if node.val in self.map:
            self.map[node.val].append(node)
        else:
            self.map[node.val] = [node]
    
    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
        for i in range(len(self.map[node.val])-1, -1, -1):
            if self.map[node.val][i] == node:
                del self.map[node.val][i]
                if not self.map[node.val] or not len(self.map[node.val]):
                    del self.map[node.val]
            return
        
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()