class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        max_fruits = 0
        i, j = 0, 0
        d = collections.defaultdict(int)
        while j < len(tree):
            d[tree[j]] += 1
            j += 1
            while len(d) > 2:
                d[tree[i]] -= 1
                if not d[tree[i]]: d.pop(tree[i], None)
                i += 1
            max_fruits = max(max_fruits, j-i)
        return max_fruits
