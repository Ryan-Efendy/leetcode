class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        nums.sort(key= lambda x:(d[x],-x))
        return nums