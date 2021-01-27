"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
​
class Solution:
    def insert(self, head: 'Node', val: int) -> 'Node':
        newNode = Node(val)
        if not head:
            newNode.next = newNode
            return newNode
        
        dummy = head
        while dummy.next != head:
            if dummy.val <= val <= dummy.next.val: break
            if dummy.val > dummy.next.val:
                if (val <= dummy.val and val <= dummy.next.val) or (val >= dummy.val and val >= dummy.next.val):
                    break
            dummy = dummy.next
        newNode.next = dummy.next
        dummy.next = newNode
        return head
