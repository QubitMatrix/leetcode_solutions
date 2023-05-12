class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum1=0
        if num==1:
            return False
        for x in range(2,int(num**0.5)+1):
            if(num%x==0):
                sum1+=x+num//x
        return sum1+1==num
