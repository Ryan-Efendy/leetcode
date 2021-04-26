class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''
        https://www.youtube.com/watch?v=5oPLH1CirAA
        Input: n = 3, k = 3
        1."123"
        2."132"
        3."213" ✅
        4."231"
        5."312"
        6."321"
        
        Output: "213"
        
        Brute force - generate all permutations O(n!)
        
        Optimal - divide & conquer, skip some permutations
        "123" \ 1️⃣       
        "132" /  
        "213" \ 2️⃣
        "231" / 
        "312" \ 3️⃣
        "321" /
        
        n = 4, perm(1,2,3,4), k = 15   ans = * * * *
        1 + perm(2,3,4) => 6 | skip
        2 + perm(1,3,4) => 6 | skip
        3 + perm(1,2,4) => 6 <- 15th perm will be in this block, 15-12=3
        4 + perm(1,2,3) => 6
        
        perm(1,2,4), k = 3 ans = 3 * * *
        1 + perm(2,4) => 2 | skip
        2 + perm(1,4) => 2 | 3 falls in this block, 3-2=1
        3 + perm(1,2) => 2
        
        perm(1,4), k=1 ans = 3 2 * *
        1 + perm(4) => 1 ✅ 
        4 + perm(1) => 1
        
        ans = 3 2 1 4
        '''
        # n=4, k=15
        ans = []
        nums = [str(i) for i in range(1, n+1)] # [1,2,3,4]
        fact = [1] * n
        # running sum
        for i in range(1,n):
            fact[i] = i*fact[i-1] # [1,1,2,6]
        k -= 1 #kth permutation index 0?
        
        for i in range(n, 0, -1):
            # divmod(k, fact[i-1]) => 2, 2
            idx = k // fact[i-1] # k=14, fact[3]= 6, 14/6 = 2.3 ~ 2
            k %= fact[i-1] # 14 % 6 = 2 remainder
            ans.append(nums[idx]) # ['3'] -> ['3','2'] -> ['3','2','1','4']
            nums.pop(idx) # [1,2,3,4] -> [1,2,4]
        return ''.join(ans)