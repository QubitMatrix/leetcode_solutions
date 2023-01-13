class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=int(c**0.5)
        if(c==0):
            return True
        for x in range(1,a+1):
            if(int((c-x**2)**0.5)**2==(c-x**2)):
                return True
        return False
