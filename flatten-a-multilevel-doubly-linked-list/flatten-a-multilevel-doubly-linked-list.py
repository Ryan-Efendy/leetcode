"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        node = head
        prev = None
        while node:
            if node.child:
                if node.next:
                    nxt = node.next
                    nxt.prev = None
                    stack.append(nxt)
                node.next = node.child
                node.next.prev = node
                node.child = None
            prev = node
            node = node.next
            
        node = prev
        while stack:
            node.next = stack.pop()
            node.next.prev = node
            while node.next:
                node = node.next
        return head

                