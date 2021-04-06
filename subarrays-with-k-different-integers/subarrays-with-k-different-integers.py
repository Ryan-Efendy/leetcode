class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
        Sliding window (two pointers) / Reduce to "Subarrays with at most K different nums"
        Ans = f(K) - f(K-1) # exact K different nums

        Time complexity: 0(n) Space complexity: 0(n)
        '''
        def getKMostCount(nums: List[int], k: int) -> int:
            counter = collections.defaultdict(int)
            left = 0
            res = 0
            for right, num in enumerate(nums):
                counter[num] += 1

                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0: del counter[nums[left]]
                    left += 1

                res += right - left + 1
            return res
        
        return getKMostCount(nums, k) - getKMostCount(nums, k-1)