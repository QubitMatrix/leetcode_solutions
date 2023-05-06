class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        if(n==1 or n==-1):
            return x if n>0 else 1/x
        elif(n%2==0):
            s=self.myPow(x,n//2)
            return s*s
        else:
            s=self.myPow(x,n//2)
            return s*s*x
