class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n>0):
            if(n==1):
                return True
            else:
                if(n/2==n//2):
                    n=n/2
                else:
                    return False
        return False
