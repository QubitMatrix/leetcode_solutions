class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n==0):
            return False
        if(n==1):
            return True
        else:
            if(n%3!=0):
                return False
            else:
                return self.isPowerOfThree(n//3)
