class Solution:
    '''
    [-1,0,1,2,-1,-4]
    [-4,-1,-1,0,1,2]  a + b + c = 0 => -4 + b + c = 0 => b + c = 4
         i  j                                            b + c = 1
                  k
    
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        if len(nums) < 3: return []
        nums.sort()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                target = 0 - nums[i]
                curr = nums[j] + nums[k]
                if curr == target:
                    s.add((nums[i],nums[j],nums[k]))
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    j += 1
        return list(s)
                    
