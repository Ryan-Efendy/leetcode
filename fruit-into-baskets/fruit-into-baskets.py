class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        calculate max window w/ at most 2 diff chars
        '''
        counter = defaultdict(int)

        i, j, res = 0, 0, 0
        
        while j < len(tree):
            counter[tree[j]] += 1
            
            while len(counter) > 2:
                counter[tree[i]] -= 1
                if counter[tree[i]] == 0:
                    del counter[tree[i]]
                i += 1
                
            res = max(res, j - i + 1)
            j += 1
            
        return res