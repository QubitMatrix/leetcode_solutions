class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        arr=[ mat[x][x] if(x==len(mat)-x-1)  else mat[x][x]+mat[x][len(mat)-x-1] for x in range(len(mat))]
        return sum(arr)
