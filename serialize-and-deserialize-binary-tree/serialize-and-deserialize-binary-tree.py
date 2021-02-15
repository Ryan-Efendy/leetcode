# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper1(root, res):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            helper1(root.left, res)
            helper1(root.right, res)
            return ','.join(res)
        
        res = []
        return helper1(root, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return data
        print(data)
        q = collections.deque(data.split(','))
        
        def helper(q):
            if not q or not len(q): return None
            curr = q.popleft()
            if curr == '#': return None
            root = TreeNode(int(curr))
            root.left = helper(q)
            root.right = helper(q)
            return root
            
        return helper(q)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))