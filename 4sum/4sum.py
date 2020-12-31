class Solution:
    '''
    a + b + c + d = 0 => a + b = - c - d
    [1,0,-1,0,-2,2]
    [-2,-1, 0, 0, 1, 2]
      i
         j           k
    
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4: return res
        nums.sort()
​
        for a in range(len(nums)-3):
            if a == 0 or nums[a-1] != nums[a]:
                self.threeSum(nums, a, target, res)
        return res
​
​
    def threeSum(self, nums: List[int], a: int, target: int, res: List[List[int]]):
        for b in range(a+1, len(nums)-2):
            if b == a+1 or nums[b-1] != nums[b]:
                self.twoSum(nums, a, b, target, res)
​
​
    def twoSum(self, nums: List[int], a: int, b: int, target: int, res: List[List[int]]):
        c, d = b+1, len(nums)-1
        while c < d:
            sum = nums[a] + nums[b] + nums[c] + nums[d]
            if  sum == target:
                res.append([nums[a], nums[b], nums[c], nums[d]])
                c += 1
                d -= 1
                while c < d and nums[c-1] == nums[c]:
                    c += 1
                while c < d and nums[d+1] == nums[d]:
                    d -= 1
            elif sum > target:
                d -= 1
            else:
                c += 1
