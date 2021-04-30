class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def isCountGreaterThanOrEqualToK(num: int) -> bool:
            row, col = 0, len(matrix) - 1
            count = 0
            while row < len(matrix) and col >= 0:
                if matrix[row][col] <= num:
                    count += col + 1
                    row += 1
                else:
                    col -= 1
            return count >= k

        # find lower & upper bound of binarySearch
        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = left + (right - left) // 2

            if isCountGreaterThanOrEqualToK(mid):
                right = mid # b/c mid is valid need to be considered still
            else:
                left = mid + 1

        return left