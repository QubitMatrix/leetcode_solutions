class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix=[0 for _ in range(len(matrix[0]))]
        self.prefixsum=[[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
        col_sum=[0 for _ in range(len(matrix[0]))]
        for x in range(len(matrix)):
            prefix[0]+=matrix[x][0]
            self.prefixsum[x][0]=prefix[0]
            col_sum[0]+=matrix[x][0]
            for y in range(1,len(matrix[0])):
                col_sum[y]+=matrix[x][y]
                prefix[y]=col_sum[y]+prefix[y-1]
                self.prefixsum[x][y]=prefix[y]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=self.prefixsum[row2][col2]
        sub1=0 if row1==0 else self.prefixsum[row1-1][col2]
        sub2=0 if col1==0 else self.prefixsum[row2][col1-1]
        add1=0 if row1==0 or col1==0 else self.prefixsum[row1-1][col1-1]
        return total-sub1-sub2+add1
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
