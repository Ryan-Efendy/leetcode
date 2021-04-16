class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        '''
        l1 = [[0,2],[5,10],[13,23],[24,25]]
        l2 = [[1,5],[8,12],[15,24],[25,26]]
        
           \U0001f447   \U0001f447     \U0001f447                    \U0001f447 \U0001f447   
       \U0001f539\U0001f539\U0001f539    \U0001f539\U0001f539\U0001f539\U0001f539\U0001f539   \U0001f539\U0001f539\U0001f539\U0001f539\U0001f539\U0001f539\U0001f539\U0001f539\U0001f539\U0001f539\U0001f539 \U0001f539\U0001f539    
          \U0001f538\U0001f538\U0001f538\U0001f538    \U0001f538\U0001f538\U0001f538\U0001f538    \U0001f538\U0001f538\U0001f538\U0001f538\U0001f538\U0001f538\U0001f538\U0001f538\U0001f538 \U0001f538\U0001f538 
          \U0001f446    \U0001f446   \U0001f446          \U0001f446             \U0001f446
        \U0001f53a\U0001f53a\U0001f53a\U0001f53a\U0001f53b\U0001f53a\U0001f53a\U0001f53a\U0001f53a\U0001f53b\U0001f53a\U0001f53a\U0001f53a\U0001f53a\U0001f53b\U0001f53a\U0001f53a\U0001f53a\U0001f53a\U0001f53b\U0001f53a\U0001f53a\U0001f53a\U0001f53a\U0001f53b\U0001f53a\U0001f53a\U0001f53a\U0001f53a\U0001f53b
        0       5      10       15      20      25       30
        
        ans: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        
        start → Max of given start points
        end → Min of given end points
        Moving pointers → based on min end of given ends
        '''
        res = []
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            # start → Max of given start points
            start = max(l1[i][0], l2[j][0])
            # end → Min of given end points
            end = min(l1[i][1], l2[j][1])
            # edge case
            if start <= end:
                res.append([start, end])
            # Moving pointers → based on min end of given ends
            if l1[i][1] < l2[j][1]:
                i += 1
            else:
                j += 1
        return res