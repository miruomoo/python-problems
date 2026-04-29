class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix[0])-1

        while l<r:
            for i in range(r-l):
                top = l
                bot = r
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bot-i][l]
                matrix[bot-i][l] = matrix[bot][r-i]
                matrix[bot][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
            l+=1
            r-=1

                