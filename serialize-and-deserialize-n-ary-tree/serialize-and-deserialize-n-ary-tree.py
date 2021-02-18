from ast import literal_eval as make_tuple

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def preorder(root, res):
            if not root: return
            res.append(str(root.val))
            for child in root.children:
                preorder(child, res)
            res.append('#')   
            return ",".join(res)
        
        res = []
        return preorder(root, res)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return data
        q = collections.deque(data.split(','))
        
        def helper(q):
            if not q or not len(q): return None
            root = Node(int(q.popleft()), [])
            while q[0] != '#':
                root.children.append(helper(q))
            q.popleft()
            return root
            
        return helper(q)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))