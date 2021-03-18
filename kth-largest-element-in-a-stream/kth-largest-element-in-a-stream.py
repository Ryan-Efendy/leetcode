import bisect
from typing import List

class KthLargest:
    """
    Binary Search + Insertion
    Time: O(NlogN)
    Space: O(N)
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort_left(self.nums, val)
        return self.nums[len(self.nums) - self.k]