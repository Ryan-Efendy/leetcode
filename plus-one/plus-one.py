class Solution:
    """
    [1,2,3]
    
    [1,1,9] -> [1,2,0]
         
    [9,9,9] -> [1,0,0,0]
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            carry = 0
            for i in range(len(digits)-1,-1,-1):
                if i == 0 and digits[i] == 9:
                    digits[i] = 0
                    digits = [1] + digits
                elif digits[i] < 9:
                    digits[i] += carry
                    carry = 0
                    break
                else:
                    digits[i] = 0
                    carry = 1
        return digits
                        
            
