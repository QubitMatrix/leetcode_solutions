class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for x in range(1,len(matrix)):
            for y in range(1,len(matrix[0])):
                if(matrix[x][y]!=matrix[x-1][y-1]):
                    return False
        return True
        
