class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        cumulative sum + two sum using/ hashmap O(n) Time & Space
        '''
        d = defaultdict(int)
        d[0] += 1 # b/c itertools.accumulate will have the same size as nums, need to init
        presums = list(accumulate(nums))
        res = 0

        for presum in presums:
            diff = presum - k
            if diff in d:
                res += d[diff]
            d[presum] += 1

        return res