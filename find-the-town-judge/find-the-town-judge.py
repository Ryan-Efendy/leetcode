class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        '''
        https://www.youtube.com/watch?v=OVdeIkc6Zmk
        
        find the vertex w/ outdegree == 0 & indegree == N
        '''
        # edge case
        if len(trust) < N - 1: return -1

        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)
        # trust_scores = [0] * (N + 1)

        for out_, in_ in trust:
            outdegree [out_] += 1
            indegree[in_] += 1
            # trust_scores[out_] += 1
            # trust_scores[in_] -= 1

        for i in range(1, N + 1): 
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1