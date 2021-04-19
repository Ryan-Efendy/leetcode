class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        points = [[10,16],[2,8],[1,6],[7,12]]
                \U0001f3f9         \U0001f3f9
         \U0001f388\U0001f388\U0001f388\U0001f388\U0001f388\U0001f388        \U0001f3f9
          \U0001f388\U0001f388\U0001f388\U0001f388\U0001f388\U0001f388\U0001f388     \U0001f3f9
                \U0001f3f9 \U0001f388\U0001f388\U0001f388\U0001f388\U0001f388\U0001f388
                \U0001f3f9       \U0001f388\U0001f388\U0001f388\U0001f388\U0001f388\U0001f388\U0001f388
                \U0001f3f9         \U0001f3f9
                \U0001f3f9         \U0001f3f9  
        |-------|-------|--------|-------|-------|--------|
        0       5      10       15      20      25       30
        
        '''
        if not points:
            return 0

        points.sort()

        ans = 1
        cur_end = points[0][1]
        for point in points:
            if point[0] <= cur_end:
                cur_end = min(cur_end, point[1])
            else:
                ans += 1
                cur_end = point[1]

        return ans