class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # or find n-k smallest num
        '''
        nums = [3,2,1,5,6,4], k = 2 -> [1,2,3,4,5,6]
                                                \U0001f446
        nums = [3,2,3,1,2,4,5,5,6], k = 4 -> [1,2,2,3,3,4,5,5,6]
                                                        \U0001f446              
        '''
        # naive - sorting Time: O(nlgn), Space: O(1)
        '''
        nums.sort()
        n = len(nums)
        return nums[n-k] or n[-k]
        '''
        # min heap/pq - Time: O(nlgk), Space: O(k)
        '''
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)

            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]
        '''
        # quick/select sort& partition + divide & conquer - Time O(n)
        # pick a pivot (p) from left (l) & right (r), move all elems < pivot to the left and elems > pivot to the right (sorting)
        #        p-X, p-X, p-X,..., p, p+X, p+X, p+X ...
        # the pivot is fixed i.e. is pivot=5 it means nums[pivot] is the 5th smallest number
        #                       X,X,X,P,X,X,X
        # if n-k=3 (find n-k smallest num) and pivot > n-k => 5 > 3 search on the left side
        #                      L,x,x,x,P,x,x,x,R
        #                        \U0001f446\U0001f446\U0001f446                        \U0001f447\U0001f447\U0001f447 
        # if pivot < n-k search on the right side   L,x,x,x,P,x,x,x,R
        # quick sort O(nlgn) but we cut the search space in half -> O(n)
        def partition(l, r):
            pivot = nums[r] # random, fixed to last elem
            j = l

            for i in range(l, r):
                if nums[i] < pivot:
                    # swap
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                    # swap pivot
            nums[j], nums[r] = nums[r], nums[j]
            return j
        
        def quickSort(l, r):
            pivotIdx = partition(l, r)
            # quickSort(l, pivot-1)
            # quickSort(pivot+1, r)

            if pivotIdx == n - k:
                return nums[pivotIdx]
            elif pivotIdx > n - k:
                return quickSort(l, pivotIdx-1)  
            else:
                return quickSort(pivotIdx+1, r)
                
        n = len(nums)
        return quickSort(0, n-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        