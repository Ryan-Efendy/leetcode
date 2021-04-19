class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = [0]*26
        window = [0]*26
        result=[]
        
        for x in p:
            target[ord(x)-ord('a')] += 1
        
        for i, x in enumerate(s):
            window[ord(x)-ord('a')] += 1
            if i >= len(p):
                del_char = s[i-len(p)]
                window[ord(del_char)-ord('a')] -= 1
            if window == target:
                result.append(i-len(p)+1)
        
        return result