class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dic={}
        for x in range(len(points)):
            for y in range(x+1,len(points)):
                if(points[y][0]-points[x][0]!=0):
                    m=(points[y][1]-points[x][1])/(points[y][0]-points[x][0])
                    c=points[x][1]-m*points[x][0]
                    d=str(m)+str(c)
                else:
                    d="inf"+str(points[x][0])
                print(points[x],points[y],d)
                if(d in dic.keys()):
                    dic[d].add((points[x][0],points[x][1]))
                    dic[d].add((points[y][0],points[y][1]))
                else:
                    dic[d]=set([(points[x][0],points[x][1]),(points[y][0],points[y][1])])
        print(dic)
        dic=dic.values()
        try:
            return len(max(dic,key=lambda x:len(x)))
        except:
            return 1
