# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        '''
         root = [3,9,20,null,15,7]
            3       Output: [
           / \               [3.00000], # 3/1
          9   20             [14.50000],#(9+20)/2
             / \             [11.00000] # (15+7)/2
            15  7           ]            
        '''
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                res.append(sum(level)/n)
        return res