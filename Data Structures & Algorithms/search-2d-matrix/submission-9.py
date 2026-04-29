class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = (m*n)-1
        while l<=r:
            mid = ((l+r)//2)
            midM, midN = divmod(mid,n)
            if matrix[midM][midN] < target:
                l = mid+1
            elif matrix[midM][midN] > target:
                r = mid-1
            else:
                return True
        return False