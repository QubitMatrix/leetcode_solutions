class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev=n & 1
        l=math.floor(math.log(n,2))+1
        for x in range(1,l):
            ans=n & 1<<x
            if(ans and prev or not ans and not prev):
                return False
            prev=ans
        return True
