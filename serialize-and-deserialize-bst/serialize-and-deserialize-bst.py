# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def dfs(node):
            nonlocal arr
            if not node:
                arr.append('None')
                return
            # preorder
            arr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        arr = []
        dfs(root)
        return ','.join(arr)

    def deserialize(self, data):
        def buildTree():
            nonlocal idx
            if arr[idx] == 'None':
                return None

            root = TreeNode(arr[idx])
            idx += 1
            root.left = buildTree()
            idx += 1
            root.right = buildTree()
            return root

        idx = 0
        arr = data.split(',')
        return buildTree()

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans