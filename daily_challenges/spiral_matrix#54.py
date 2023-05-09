class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        starti=startj=0
        endi=len(matrix)-1
        endj=len(matrix[0])-1
        l=[]
        while(endi>=starti and endj>=startj):
            for x1 in range(startj,endj+1):
                l.append(matrix[starti][x1])
            for y1 in range(starti+1,endi):
                l.append(matrix[y1][endj])
            if(starti==endi):
                break
            for x2 in range(endj,startj-1,-1):
                l.append(matrix[endi][x2])
            if(startj==endj):
                break
            for y2 in range(endi-1,starti,-1):
                l.append(matrix[y2][startj])
            starti+=1
            endi-=1
            startj+=1
            endj-=1
        return l
