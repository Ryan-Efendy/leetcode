class KthLargest:
    class node():
        def __init__(self, val, cnt):
            self.val = val
            self.right = None
            self.left = None
            self.cnt = cnt

    def __init__(self, k: int, nums: List[int]):
        if nums:
            self.root = self.node(nums[0], 0)
            for i in nums[1:]:
                self.root = self.insert(self.root, i)
        else:
            self.root = None
        self.k = k-1
        

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        return self.findKthLargest(self.root, self.k)
    
    def insert(self, root, key):
        if not root:
            return self.node(key, 0)
        
        elif root.val > key:
            root.left = self.insert(root.left, key)
        else:
            root.cnt += 1
            root.right = self.insert(root.right, key)
        
        return root
    
    def findKthLargest(self, root, k):
        if not root: return -1
        
        elif root.cnt == k: return root.val
        
        elif root.cnt > k:
            return self.findKthLargest(root.right, k)
        else:
            return self.findKthLargest(root.left, k - root.cnt -1)
    
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

