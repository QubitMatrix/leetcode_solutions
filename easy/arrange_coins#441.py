class Solution:
    def arrangeCoins(self, n: int) -> int:
        step=0
        while(True):
            if(n<step+1):
                break
            step+=1
            n-=step
        return step
