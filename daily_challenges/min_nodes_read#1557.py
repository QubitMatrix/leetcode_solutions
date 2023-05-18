class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr=[]
        flag=0
        mat=[[0 for x in range(n)] for y in range(n)]
        for x,y in edges:
            mat[x][y]=1
        for x in range(n):
            for y in range(n):
                if(mat[y][x]):
                    flag=1
                    break
            if(not flag):
                arr.append(x)
            flag=0
        return arr
