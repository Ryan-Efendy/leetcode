from itertools import zip_longest
​
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        for i, j, k in zip_longest(arr1, arr2, arr3, fillvalue="_"):
            d[i] += 1
            d[j] += 1
            d[k] += 1
        res = []
        for k, v in d.items():
            if v == 3 and v != "-":
                res.append(k)
        return res
