from heapq import *

class MedianFinder:
    '''
    arr = [1,3,5,4,7,8]         1. insert
           \U0001f446                   2. balance 
     SMALL       LARGE      
     maxpq       minpq
    -------     ------- 
        1
    -------     -------
     SMALL       LARGE  
     maxpq       minpq     arr = [1,3,5,4,7,8]  
    -------     -------             \U0001f446
        1       3
    -------     -------
     SMALL       LARGE  
     maxpq       minpq     arr = [1,3,5,4,7,8]  
    -------     -------               \U0001f446
         1      3 5 ❌ \U0001f448 minpq.pop() -> maxpq.push(3)
    -------     -------
    -------     -------             
       1  3     5
    -------     -------
     SMALL       LARGE  
     maxpq       minpq     arr = [1,3,5,4,7,8]  
    -------     -------                 \U0001f446
        1 3     4 5
    -------     -------
     SMALL       LARGE  
     maxpq       minpq     arr = [1,3,5,4,7,8]  
    -------     -------                   \U0001f446
        1 3     4 5 7 ❌ minpq.pop() -> maxpq.push(4)
    -------     -------
    -------     -------             
    1  3  4     5 7
    -------     -------    
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # the smaller half of the list, MAX heap (invert min-heap)
        self.large = [] # the larger half of the list, MIN heap
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        
    def findMedian(self) -> float:
        # if even
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0])/2
        # return -self.small[0] if len(self.small) > len(self.large) else self.large[0]
        return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()