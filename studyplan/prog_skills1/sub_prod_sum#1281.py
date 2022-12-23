class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1=0
        pro1=1
        while(n>0):
            r=n%10
            n=n//10
            sum1+=r
            pro1*=r
        return (pro1-sum1)
