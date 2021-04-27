class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        transform 2d matrix m x n -> 1d sorted array of length m x n
        m x n matrix \U0001f449\U0001f3fc  to an array => matrix[x][y] =>  a[x * m + y]
        an array     \U0001f449\U0001f3fc  to n x m matrix => a[x] => matrix[x / m][x % m]
        
        '''
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        l , h = 0 , rows * cols -1        
        while l <= h:
            m = (l + h) //2
            # i, j = mid//len(matrix[0]), mid%len(matrix[0])
            r,c = divmod(m,cols)            
            num = matrix[r][c]            
            if num == target:
                return True
            elif num < target:
                l = m + 1  
            else:
                h = m - 1
        return False
        