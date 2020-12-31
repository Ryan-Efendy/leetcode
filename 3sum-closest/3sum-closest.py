class Solution:
    '''
    nums = [-1,2,1,-4], target = 1
             
    nums = [-4,-1,1,2]
             i
                j   k
    
    nums = [ 0, 2, 1,-3] target = 1
           [-3, 0, 1, 2] 
             
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = math.inf
        res = 0
        for i in range(len(nums)-2):
            if i == 0 or nums[i-1] != nums[i]:
                j, k = i+1, len(nums)-1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s-target) < min_diff:
                        res = s
                        min_diff = abs(s-target)
                        # j += 1
                        # k -= 1
                        # while j < k and nums[j-1] == nums[j]:
                        #     j += 1
                        # while j < k and nums[k+1] == nums[k]:
                        #     k -= 1
                    if s > target:
                        k -= 1
                    else:
                        j += 1
        return res
