class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic={}
        arr=[]
        count=0
        for x in tasks:
            if(x in dic.keys()):
                dic[x]+=1
            else:
                dic[x]=1
            
        for x in dic.values():
            if((x%3)%2==0):
                count+=x//3+(x%3)//2
            elif(x>1 and (x%3+3)%2==0):
                count+=x//3-1+(x%3+3)//2
            elif(x>1 and (x%2+2)%3==0):
                count+=x//2-1+(x%2+2)//3
            elif((x%2)%3==0):
                count+=x//2+(x%2)//3
            else:
                return -1
        return count
