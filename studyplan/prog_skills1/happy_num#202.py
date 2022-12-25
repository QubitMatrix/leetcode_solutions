class Solution:
    def isHappy(self, n: int) -> bool:
        sum1=0
        arr=set()
        while(n!=1 and n not in arr):
            arr.add(n)
            while(n>0):
                r=n%10
                sum1+=r**2
                n=n//10
            n=sum1
            sum1=0
        return n==1
