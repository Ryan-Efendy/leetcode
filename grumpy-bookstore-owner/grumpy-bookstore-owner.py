class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        '''
        grumpy[i] = 1, otherwise not grumpy, grumpy[i] = 0
        
           customers = [1,0,1,2,1,1,7,5]  X = 3
    grumpy_no_secret = [0,1,0,1,0,1,0,1]  max = 10
  grumpy_with_secret = [0,1,0,1,0,0,0,0]  max = 16
  
        sliding window
        1. get total 
        '''
        total = 0

        # w/o secret
        for i, customer in enumerate(customers):
            if not grumpy[i]:
                total += customer

        # sliding window, get max w/ secret
        l = 0
        extraMax, curr = 0, 0
        # extra maxinum number of customer with secret current : 0
        for r in range(len(customers)):
            if grumpy[r]:
                curr += customers[r]
            
            # shrink window, out of bound of window
            if r-l+1 > X:
                if grumpy[l]:
                    curr -= customers[l]
                l += 1
                
            if r - l + 1 == X:
                extraMax = max(extraMax, curr)
        return total + extraMax
        