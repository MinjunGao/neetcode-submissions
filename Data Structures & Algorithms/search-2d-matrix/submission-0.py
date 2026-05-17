class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start <= end:
            mid = (start + end) // 2
            r, c = self.getIdx(mid, n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                start = mid + 1
            elif matrix[r][c] > target:
                end = mid - 1
        return False
    
    def getIdx(self, mid, n):
        return (mid // n, mid % n)