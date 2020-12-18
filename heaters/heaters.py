import bisect
​
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def search_leftmost(nums, target):
            l, r = 0, len(nums)-1
            while l < r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
        
        def search_rightmost(nums, target):
            l, r = 0, len(nums)-1
            while l < r:
                m = l + (r-l+1)//2
                if nums[m] <= target:
                    l = m
                else:
                    r = m - 1
            return l
        
        houses.sort()
        heaters.sort()
        min_radius = float('-inf')
        for house in houses:
            heater_left = heaters[search_leftmost(heaters, house)]
            heater_right = heaters[search_rightmost(heaters, house)]
            diff_left = abs(house-heater_left)
            diff_right = abs(house-heater_right)
            min_radius = max(min_radius, min(diff_left, diff_right))
        return min_radius
