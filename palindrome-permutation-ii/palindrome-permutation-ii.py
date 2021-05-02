class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        '''
        1. get char freq, if odd > 1: return
        2. bactracking (generate only the first half of the palindromic str & append the reverse str of itself to generate the full palindromic str)
            a. add odd char first
            b. add even char to the beginning & end
            
        s = "aaalyal"
        counter = { ✅ less than or equal to 1 odd char
            'a': 4,
            'l': 2,
            'y': 1
        }
        
        st = 'aal' # char freq reduced in half
        
         a                             a
                                       |
         a                             aa
                                /      |          \  
                              /        |           \
         l                 laa         ala         aal            
         
    cur + mid + cur[::-1] laayaal   alayala       aalylaa
                            ✅         ✅             ✅
        '''
        # s = "aabb"
        kv = collections.Counter(s) # {'a': 2, 'b': 2}
        mid = [k for k, v in kv.items() if v%2] # []
        if len(mid) > 1:
            return []

        # add odd char first
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v//2) for k, v in kv.items()]) # half: "ab"
        half = [c for c in half] # half: ["a","b"]
        
        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp) # cur: "ab"
                # add even char to the beginning & end
                ans.append(cur + mid + cur[::-1]) # ans: ["abba"]
            else:
                for i in range(end):
                    if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()
                    
        ans = []
        visited = [False] * len(half) # visited: [false,false]
        backtrack(len(half), [])
        return ans