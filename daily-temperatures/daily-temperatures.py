class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        s = []
        res = [0] * len(T)
        for i, temp in enumerate(T):
            while s and T[s[-1]] < temp:
                j = s.pop()
                res[j] = i - j
            s.append(i)
        return res