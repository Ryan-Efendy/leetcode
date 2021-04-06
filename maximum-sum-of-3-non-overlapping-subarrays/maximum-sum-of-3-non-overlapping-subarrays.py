class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int, m = 3) -> List[int]:
        '''
        * dp arr of size n-k+1
        * prefix sum of maxLeft, maxRight of size k
        * O(n) Time & Space
        
                  0  1  2  3  4  5  6  7
        input = [ 1, 2, 1, 2, 6, 7, 5, 1], 2
        
       presum = [ 1, 3, 3, 3, 8,13,12, 6]
   left_max_i = [ 0, 1, 1, 1, 4, 5, 5, 5]
  right_max_i = [ 5, 5, 5, 5, 5, 5, 6, 7]
  
  mid: 2k-1 .. n-k-1 => 3 .. 5
                  0  1  2  3  4  5  6  7
        input = [ 1, 2, 1, 2, 6, 7, 5, 1]
                   mid ->  -------
                   
 max(presum[mid] + presum[left_max_i[mid-k]] + presum[right_max[mid+k]])
        '''
        n = len(nums)
        presum = [0] * n
        
        sum = 0
        for i in range(n):
            sum += nums[i]
            if i >= k:
                sum -= nums[i-k]
            presum[i] = sum
        # print(presum)
            
        left_max_i, right_max_i = [0] * n, [0] * n
        max_left_idx, max_right_idx = 0, n-1
        for i in range(n):
            if presum[i] > presum[max_left_idx]:
                max_left_idx = i
            left_max_i[i] = max_left_idx
            
        for i in range(n-1, -1, -1):
            if presum[i] >= presum[max_right_idx]:
                max_right_idx = i
            right_max_i[i] = max_right_idx
            
        # print(left_max_i)
        # print(right_max_i)
            
        arr_idxs = [0] * m
        max_sum = -1
        for mid in range(2*k-1, n-k):
            left = left_max_i[mid - k]
            right = right_max_i[mid + k]
            sum = presum[left] + presum[mid] + presum[right]
            print(sum)
            if sum > max_sum:
                max_sum = sum
                arr_idxs[0] = left - k + 1
                arr_idxs[1] = mid - k + 1
                arr_idxs[2] = right - k + 1
        
        return arr_idxs
        
        
                
        
        
        