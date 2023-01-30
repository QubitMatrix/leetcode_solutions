class Solution:
    def fun(self,a,b,c,x):
        if(x==-1):
            return c
        x-=1
        return self.fun(b,c,a+b+c,x)
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        arr=[0,1,1]
        if(n<3):
            return arr[n]
        n-=3
        return(self.fun(a,b,c,n))
