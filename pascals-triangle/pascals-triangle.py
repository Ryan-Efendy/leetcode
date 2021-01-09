class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            intermediate = [] if i == 0 else [1]
            for j in range(1, i):
                intermediate.append(res[i-1][j-1] + res[i-1][j])
            res.append(intermediate + [1])
        return res
