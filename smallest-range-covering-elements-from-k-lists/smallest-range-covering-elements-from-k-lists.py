class Solution:
    def smallestRange(self, lists: List[List[int]]) -> List[int]:
        '''
        greedy sliding window of size k where k is len(lists)
        lists = [  \U0001f447
                  [ 4,10,15,24,26],
                  [ 0, 9,12,20],
                    \U0001f446 
                  [ 5,18,22,30]
                    \U0001f446
         window  ]
          i j k    range        
         {4,0,5}     5     
              move forward min: 0 and push(9) to minHeap
         {4,9,5}     5
              move forward min: 5 and push(10) to minHeap
         {10,9,5}    5
         {10,9,18}   9
         {10,12,18}  8
         {15,12,18}  6
         {15,20,18}  5
         {24,20,18}  6
         {24,20,22}  4 ✅ 
         Output: [20,24]
        
        we want i, j, k to be as close as possible. init i, j, k = 0, 0, 0. Approach is either increase lower or upper bound b/c we are starting at 0, we can only increase lower.
        
        1. Find max, min from the first elements of all the lists
        3. get range = max - min, keep track minRange
        4. pop min & insert next num from the list that had min removed
        5. Repeat: Compute max, min and range again until one of the list is done being computed
        '''
        minHeap = [] # keep track of min
        maxNum = -math.inf # keep track of max
        rangeStart, rangeEnd = 0, math.inf

        # put the 1st element of each array in the max heap
        for arr in lists:
            heappush(minHeap, (arr[0], 0, arr))
            maxNum = max(maxNum, arr[0])

        # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
        # if the array of the top element has more elements, insert the next element in the heap
        while len(minHeap) == len(lists):
            num, i, arr = heappop(minHeap)
            # get minRange
            if rangeEnd - rangeStart > maxNum - num:
                rangeStart = num
                rangeEnd = maxNum

            if i+1 < len(arr):
                # insert the next element in the heap
                heappush(minHeap, (arr[i+1], i+1, arr))
                maxNum = max(maxNum, arr[i+1])

        return [rangeStart, rangeEnd]
