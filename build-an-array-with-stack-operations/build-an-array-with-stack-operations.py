class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = set(target)
        s2 = set()
        res = []
        for i in range(1, n+1):
            if i in s:
                res.append("Push")
                s2.add(i)
                if s == s2: return  res
            else:
                res.append("Push")
                res.append("Pop")
        return res