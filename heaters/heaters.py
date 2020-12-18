import bisect
​
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def binary_search(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
        
        heaters.sort()
        min_radius = float('-inf')
        for house in houses:
            index = binary_search(heaters, house)
            # index = bisect.bisect_left(heaters,house)
            dist_left = house - heaters[index-1] if index - 1 >= 0 else float('inf')
            dist_right = heaters[index] - house if index < len(heaters) else float('inf')
            min_radius = max(min_radius, min(dist_left, dist_right))
        return min_radius
