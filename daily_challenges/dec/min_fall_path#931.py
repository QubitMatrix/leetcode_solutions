class Solution:
    def paths(self,matrix,row,col,n,dic):
        ele=matrix[row][col]
        element=ele
        minele=15000
        if(row==n-1):
            return ele
        if(col>0):
            try:
                print("a")
                ele+=dic[str(row+1)+"-"+str(col-1)]
            except:
                print("aa")
                ele+=self.paths(matrix,row+1,col-1,n,dic)
            if(minele>ele):
                minele=ele
            ele=element
        if(col<n-1):
            try:
                print("b")
                ele+=dic[str(row+1)+"-"+str(col+1)]
            except Exception as e:
                print("bb",e)
                ele+=self.paths(matrix,row+1,col+1,n,dic)
            if(minele>ele):
                minele=ele
            ele=element
        try:
            print("c")
            ele+=dic[str(row+1)+"-"+str(col)]
        except:
            print("cc")
            ele+=self.paths(matrix,row+1,col,n,dic)
        if(ele<minele):
            minele=ele
        dic[str(row)+"-"+str(col)]=minele
        return minele
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        minele=15000
        dic={}
        for x in range(len(matrix)):
            ele=self.paths(matrix,0,x,len(matrix),dic)
            if(minele>ele):
                minele=ele
        return minele
