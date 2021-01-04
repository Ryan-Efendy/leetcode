class Solution:
    '''
    [2,6,4,8,10,9,15]
                j
       i
    
    Example 1:
    Input: [1, 2, 5, 3, 7, 10, 9, 12]
    Output: 5
    Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
    Example 2:
            0  1  2  3   4  5   6
    Input: [1, 3, 2, 0, -1, 7, 10]
                                j
    max - 10 end   - 4
    min - -1 start - 0
    
    Output: 5
    Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
    Example 3:
    Input: [1, 2, 3]
    Output: 0
    Explanation: The array is already sorted
    Example 4:
    Input: [3, 2, 1]
    Output: 3
    Explanation: The whole array needs to be sorted.
    '''
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max, min, start, end = nums[0], nums[n-1], -1, -2
        for i in range(1, n):
            j = n - i - 1
            if nums[i] >= max:
                max = nums[i]
            else:
                end = i
            
            if nums[j] <= min:
                min = nums[j]
            else:
                start = j
        
        return end - start + 1
            
            
