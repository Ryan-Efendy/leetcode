class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        n = len(height)
        # precompute leftMax, rightMax
        leftMax = [0] * n
        rightMax = [0] * n
        
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1])
            rightMax[n-1-i] = max(rightMax[n-i], height[n-i])
            
        water_and_building = [min(leftMax[i], rightMax[i]) for i in range(n)]   
        
        water = sum([water_and_building[i] - height[i] if water_and_building[i] - height[i] > 0 else 0 for i in range(n)])
            
        # print(leftMax)
        # print(rightMax)
        # print(water_and_building)
        # print(water)
            
        return water