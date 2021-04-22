# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        sumCount = defaultdict(int)
        sumCount[0] = 1 # init for root
        res = 0

        def dfs(node: TreeNode, runningSum: int):
            nonlocal res
            if not node:
                return

            runningSum += node.val

            if (runningSum - targetSum) in sumCount:
                res += sumCount[runningSum-targetSum]

            sumCount[runningSum] += 1

            dfs(node.left, runningSum)
            dfs(node.right, runningSum)

            # backtrack need to pop last item
            sumCount[runningSum] -= 1

        dfs(root, 0)
        return res