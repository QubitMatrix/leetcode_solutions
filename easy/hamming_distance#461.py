class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if(x!=0):
            a=math.floor(math.log(x,2))
        else:
            a=0
        if(y!=0):
            b=math.floor(math.log(y,2))
        else:
            b=0
        n=max(a,b)+1
        count=0
        for i in range(n):
            if((x & 1<<i) ^ (y & 1<<i)):
                count+=1
        return count
