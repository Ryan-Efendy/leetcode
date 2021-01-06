class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counters = [0] * (len(nums)+1)
        for num in nums:
            counters[num] += 1
        
        res = []
        for i in range(len(counters)):
            if i != 0 and counters[i] == 0:
                res.append(i)
        
        return res
