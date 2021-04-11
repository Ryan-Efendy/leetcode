class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def getAngle(p):
            a = math.atan2(p[0]-location[0], p[1]-location[1]) / (2*math.pi) * 360

            if a < 0:
                a += 360
                
            return a

        angles = []
        same = 0 # if location == point

        for point in points:
            if point == location:
                same += 1
            else:
                angles.append(getAngle(point))

        angles.sort()
        res = 0
        queue = deque()
        
        for a in angles:
            queue.append(a)
            
            while a - queue[0] > angle:
                queue.popleft()
                
            res = max(res, len(queue))
            
        for a in angles:
            a += 360
            queue.append(a)
            
            while a - queue[0] > angle:
                queue.popleft()
                
            res = max(res, len(queue))
            
        return res + same