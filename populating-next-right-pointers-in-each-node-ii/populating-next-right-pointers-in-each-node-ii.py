"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        head = root
        while head:
            dummy = Node(0)
            tmp = dummy
            
            while head:
                if head.left:
                    tmp.next = head.left
                    tmp = tmp.next
                if head.right:
                    tmp.next = head.right
                    tmp = tmp.next
                head = head.next
        
            head = dummy.next
    
        return root
        