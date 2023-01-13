class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix[0])
        row=len(matrix)
        for x in range(row):
            if(target<=matrix[x][col-1]):
                l=0
                h=col
                while(l<=h):
                    mid=(l+h)//2
                    if(target==matrix[x][mid]):
                        return True
                    elif(target<matrix[x][mid]):
                        h=mid-1
                    else:
                        l=mid+1
                return False
        return False
