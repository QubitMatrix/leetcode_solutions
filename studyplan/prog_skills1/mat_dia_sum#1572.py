class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        for x in range(len(mat)):
            if(x==len(mat)-x-1):
                sum1+=mat[x][x]
            else:
                sum1+=mat[x][x]+mat[x][len(mat)-x-1]
        return sum1
