class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        t=[]
        arr=[]
        if(len(mat)==0):
            return mat
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                t.append(1000000)
            arr.append(t)
            t=[]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if(mat[x][y]==0):
                    arr[x][y]=0
                else:
                    if(x>0):
                        arr[x][y]=min(arr[x][y],arr[x-1][y]+1)
                    if(y>0):
                        arr[x][y]=min(arr[x][y],arr[x][y-1]+1)
        for x in range(len(mat)-1,-1,-1):
            for y in range(len(mat[0])-1,-1,-1):
                if(x<len(mat)-1):
                    arr[x][y]=min(arr[x][y],arr[x+1][y]+1)
                if(y<len(mat[0])-1):
                    arr[x][y]=min(arr[x][y],arr[x][y+1]+1)
        return arr
