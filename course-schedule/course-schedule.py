class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        https://www.youtube.com/watch?v=EgI5nU9etnU
        DFS
        prereq = [[0,1], [0,2], [1,3], [1,4], [3,4]]
        
        coursesToPrereqMap = {      visited = set()
            0: [1, 2],
            1: [3, 4],
            2: [],
            3: [4],
            4: []
        }
        '''
        coursesToPrereq = { i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            coursesToPrereq[course].append(prereq)

        visited = set()
        def dfs(course):
            # detect cycle
            if course in visited:
                return False
            # optimization if no prereq or prereq already satisfied
            if not coursesToPrereq[course]:
                return True

            visited.add(course)
            for prereq in coursesToPrereq[course]:
                if not dfs(prereq): return False
            visited.remove(course)
            coursesToPrereq[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True
        
        
        