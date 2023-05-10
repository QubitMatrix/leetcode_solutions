class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count=1
        startj=starti=0
        endj=endi=n-1
        matrix=[]
        for x in range(n):
            l=[]
            for y in range(n):
                l.append(0)
            matrix.append(l)
            l=[]

        while(count<=n*n):
            for x1 in range(startj,endj+1):
                matrix[starti][x1]=count
                count+=1
            for y1 in range(starti+1,endi):
                matrix[y1][endj]=count
                count+=1
            if(starti==endi):
                break
            for x2 in range(endj,startj-1,-1):
                matrix[endi][x2]=count
                count+=1
            if(startj==endj):
                break
            for y2 in range(endi-1,starti,-1):
                matrix[y2][startj]=count
                count+=1
            starti+=1
            endi-=1
            startj+=1
            endj-=1
        return matrix
