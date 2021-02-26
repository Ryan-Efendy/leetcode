"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        mapping = {}
        
        def dfs(node: 'Node') -> 'Node':
            if node in mapping: return mapping[node]
            clone = Node(node.val)
            mapping[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        return dfs(node)
    
        
        