# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, node: TreeNode, path: str, res: List[int]):
        if not node: return 

        # Add the current node to the path's list
        if not path:
            path =  f'{node.val}'
        else:
            path += f'->{node.val}'

        if not node.left and not node.right:
            res.append(path) # make a copy
        else:
            self.dfs(node.left, path, res)
            self.dfs(node.right, path, res)