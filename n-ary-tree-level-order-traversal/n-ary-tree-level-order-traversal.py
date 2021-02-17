"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root: return res
        q = collections.deque([root])
        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                root = q.popleft()
                q.extend(root.children)
                tmp.append(root.val)
            res.append(tmp)
        return res
                
                    
            
        