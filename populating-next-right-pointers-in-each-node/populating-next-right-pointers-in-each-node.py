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
        '''
        root = [1,2,3,4,5,6,7]
         1           1=▶️❌        
        / \         / \                
       2   3       2=▶️ 3=▶️❌            
      / \ / \     / \  / \            
     4  5 6  7   4=▶️5=▶️6=▶️7=▶️❌
     
     since is perfect binary tree it'll have both left & right
     1. connect curr.left.next = curr.right
     2. if curr.next: curr.right.next = curr.next.left
        '''
        if not root: return root
        
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr.left:
                curr.left.next = curr.right
                
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        
        return root
    