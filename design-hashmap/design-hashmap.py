class MyHashMap:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 769
        self.buckets = [Bucket() for i in range(self.size)]
    
    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative
        """
        index = self._hash(key)
        self.buckets[index].insert(key, val)
​
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """    
        index = self._hash(key)
        return self.buckets[index].getValue(key)
​
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self._hash(key)
        self.buckets[index].delete(key)
        
    def _hash(self, key):↔​
        
class Node:↔​
​
class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0, 0)
​
    def insert(self, key, val):
        # if not existed, add the new element to the head.
        if not self.exists(key):
            newNode = Node(key, val, self.head.next)
            # set the new head.
            self.head.next = newNode
        else:
            curr = self.head.next
            while curr is not None:
                if curr.key == key:
                    curr.val = val
                curr = curr.next
​
    def delete(self, key):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.key == key:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
​
    def exists(self, key):
        curr = self.head.next
        while curr is not None:
            if curr.key == key:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False
    
    def getValue(self, key):
        curr = self.head.next
        while curr is not None:
            if curr.key == key:
                # value existed already, do nothing
                return curr.val
            curr = curr.next
        return -1
​
