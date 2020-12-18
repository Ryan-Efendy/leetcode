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
        
        i, j = 0, len(matrix[0])-1
        while i <= len(matrix)-1 and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
        
