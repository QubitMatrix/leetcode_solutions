class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n==0):
            return False
        elif(n==1):
            return True
        else:
            if(n%4):
                return False
            else:
                return self.isPowerOfFour(n//4)
