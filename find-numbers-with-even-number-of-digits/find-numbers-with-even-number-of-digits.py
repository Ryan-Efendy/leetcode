class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def isNumberEven(num):
            cnt = 0
            while num >= 1:
                num /= 10
                cnt += 1
            return cnt % 2 == 0
            
            
        res = 0
        for num in nums:
            if isNumberEven(num):
                res += 1
        
        return res
