class Solution:
    '''
    nums = [-2,0,1,3], target = 2
    [-2,0,1,3]
     i  j   k
     
    nums = [0,2,1,-3], target = 1
    [-3,0,1,2]
    
    -3,0,1
    -3,0,2
    -3,1,2
    '''
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return 0
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            # if i == 0 or nums[i-1] != nums[i]:
                j, k = i + 1, len(nums)-1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s < target:
                        res += k - j
                        j += 1
                    else:
                        k -= 1
                    # while j < k and nums[j-1] == nums[j]: j += 1
        return res
            
