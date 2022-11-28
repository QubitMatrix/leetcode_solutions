class Solution:
    def addDigits(self, num: int) -> int:
        sums=num
        while(len(str(sums))!=1):
            num=sums
            sums=0
            while(num>0):
                sums+=num%10
                num=num//10
        return sums
