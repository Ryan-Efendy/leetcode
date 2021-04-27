class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
        
        Assume A[mid] ~ A[mid + k] is sliding window

        case 1: x - A[mid] < A[mid + k] - x, need to move window go left
        -------x----A[mid]-----------------A[mid + k]----------

        case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
        -------A[mid]----x-----------------A[mid + k]----------

        case 3: x - A[mid] > A[mid + k] - x, need to move window go right
        -------A[mid]------------------x---A[mid + k]----------

        case 4: x - A[mid] > A[mid + k] - x, need to move window go right
        -------A[mid]---------------------A[mid + k]----x------

        If x - A[mid] > A[mid + k] - x,
        it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
        and we have mid smaller than the right i.
        So assign left = mid + 1.
        '''
        lo = 0
        hi = len(arr) - k
        while lo < hi:
            mid = lo + (hi-lo) // 2

            if x - arr[mid] > arr[mid+k] - x:
                lo = mid + 1
            else:
                hi = mid

        return arr[lo:lo+k]