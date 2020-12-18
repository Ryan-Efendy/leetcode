class Solution:
    '''
    [ i
     [1, 3, 5, 7 ],
     [10,11,16,20],
     [23,30,34,50]
               j
    ]
    
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        if not len(matrix) or not len(matrix[0]): return False
        m = len(matrix) # row
        n = len(matrix[0]) # col
        l, r = 0, m*n-1
        while l < r:
            mid = l + (r-l)//2
            row = mid // n
            col = mid % n
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid
        return True if matrix[l//n][l%n] == target else False
        
