class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix[0])
        row=len(matrix)
        for x in range(row):
            if(target<=matrix[x][col-1]):
                return target in matrix[x]
        return False
