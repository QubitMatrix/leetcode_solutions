class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        posr=posc=0
        flag=0
        arr=[]
        for _ in range(len(grid[0])):
            posc=_
            posr=0
            while(posr<len(grid)):
                if(grid[posr][posc]==1):
                    flag=1
                    posc+=1
                    if(posc==len(grid[0])):
                        arr.append(-1)
                        break
                    if(grid[posr][posc]==-1):
                        arr.append(-1)
                        break
                    posr+=1
                elif(grid[posr][posc]==-1):
                    flag=0
                    posc-=1
                    if(posc==-1):
                        arr.append(-1)
                        break
                    if(grid[posr][posc]==1):
                        arr.append(-1)
                        break
                    posr+=1
            if(posr==len(grid)):
                arr.append(posc)
                print(posc)
        return arr
