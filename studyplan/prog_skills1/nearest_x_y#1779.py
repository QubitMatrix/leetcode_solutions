import math
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mindis=99999
        dis=99999
        for z in range(len(points)):
            if(points[z][0]==x):
                dis=math.fabs(points[z][1]-y)
            elif(points[z][1]==y):
                dis=math.fabs(points[z][0]-x)
            if(mindis>dis):
                mindis=dis
                pos=z
        if(mindis==99999):
            return -1
        return pos
